#!/usr/bin/env python3
"""Local, explicit CSV mapping and preflight. TAD remains the import authority."""
import argparse
import csv
from datetime import date, datetime
from decimal import Decimal
import hashlib
import io
import json
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
VERSION = '0.1.0'


def contract():
    value = json.loads((ROOT/'references/contract.json').read_text())
    for role, spec in value['roles'].items():
        raw = (ROOT/f'assets/standard-import/TAD.{role}.v1.csv').read_bytes()
        if hashlib.sha256(raw).hexdigest() != spec['template_sha256']:
            raise ValueError('Bundled template integrity mismatch')
        if next(csv.reader(io.StringIO(raw.decode('utf-8-sig')))) != spec['columns']:
            raise ValueError('Bundled contract/template columns differ')
    return value


def number(v, required=False):
    if v == '' and not required:
        return None
    if not re.fullmatch(r'[-+]?\d+(?:\.\d+)?', v):
        raise ValueError('Expected plain decimal; missing is not zero')
    return Decimal(v)


def day(v, required=False):
    if not v and not required:
        return None
    if date.fromisoformat(v).isoformat() != v:
        raise ValueError('Expected ISO date YYYY-MM-DD')
    return v


def validate(role, r):
    """Check supplied observations; never create costs, returns or executions."""
    if r['schema_version'] != 'tad.standard-csv.v1' or r['currency'] != 'USD':
        raise ValueError('Requires tad.standard-csv.v1 and USD; no FX inference')
    for k in ('source_broker','account_ref','account_name','account_type','mapping_version'):
        if not r[k] or len(r[k]) > 160:
            raise ValueError('Confirm missing/invalid account metadata: '+k)
    if not re.fullmatch(r'[a-z][a-z0-9_-]{0,63}', r['source_broker']):
        raise ValueError('Use the actual source broker slug, not an impersonated supported broker')
    if r['timezone']:
        ZoneInfo(r['timezone'])
    if r['source_kind'] not in ('converted','user_supplied'):
        raise ValueError('Invalid source kind')
    for k in ('source_document_id','source_record_id'):
        if not r[k] or r[k].startswith(('/', '\\')) or re.match(r'^[A-Za-z]:',r[k]):
            raise ValueError('Require portable original record locator: '+k)
    if not re.fullmatch('[a-f0-9]{64}',r['source_file_sha256']):
        raise ValueError('Require actual original-file SHA256')
    def terms():
        asset=r['asset_type'];mult=number(r['multiplier'],True)
        if asset=='equity':
            if re.fullmatch(r'[A-Z][A-Z0-9]*[0-9]{6}[CP][0-9]+',r['symbol']):raise ValueError('Option-like symbol requires explicit option terms; do not declare it equity')
            if r['multiplier']!='1' or any(r[k] for k in ('underlying','expiration','right','strike')) or not re.fullmatch('[A-Z][A-Z0-9]*(?:[.-][A-Z0-9]+)*',r['symbol']):
                raise ValueError('Confirm equity identity and multiplier1')
        elif asset=='option':
            if r['multiplier']!='100' or r['right'] not in ('call','put') or not re.fullmatch('[A-Z][A-Z0-9]*(?:[.-][A-Z0-9]+)*',r['underlying']):
                raise ValueError('Only explicit standard100 US equity option terms supported')
            exp=day(r['expiration'],True);strike=number(r['strike'],True)
            if strike<=0 or strike*1000!=(strike*1000).to_integral_value():
                raise ValueError('Unsupported option strike')
            canonical=r['underlying']+date.fromisoformat(exp).strftime('%y%m%d')+r['right'][0].upper()+str(int(strike*1000))
            if r['symbol'] and r['symbol']!=canonical:
                raise ValueError('Option symbol conflicts with explicit terms')
        else:
            raise ValueError('Confirm supported asset type; no adjusted deliverable inference')
        return mult
    if role=='transactions':
        action=r['activity'];fills={'buy','sell','short_sell','cover'};cash={'dividend','interest','transfer','fee'}
        # Lifecycle events deliberately require a specialized reviewed mapping, outside this tool's first version.
        if action not in fills|cash:
            raise ValueError('Unresolved event (Journal/expiry/assignment/exercise): do not infer or drop; use native Connector or source clarification')
        q=number(r['quantity'],action in fills);price=number(r['price']);amount=number(r['amount']);commission=number(r['commission']);fees=number(r['fee_total'])
        for v in (price,commission,fees):
            if v is not None and v<0:raise ValueError('Price/fees must be nonnegative source observations')
        if fees is not None and commission is not None and fees<commission:raise ValueError('Total fees cannot be less than commission')
        if r['amount_basis'] not in ('net_cash','gross_trade','unqualified'):raise ValueError('Confirm net/gross amount basis')
        day(r['trade_date'],True);day(r['post_date']);day(r['settlement_date'])
        if r['position_effect'] not in ('','unknown','open','close'):raise ValueError('Unknown position effect')
        if r['trade_time']:
            t=datetime.fromisoformat(r['trade_time'].replace('Z','+00:00'))
            if not t.tzinfo or not r['timezone'] or t.astimezone(ZoneInfo(r['timezone'])).date().isoformat()!=r['trade_date']:
                raise ValueError('Confirm offset-aware execution time and source timezone/date')
        if action in fills:
            mult=terms()
            if q<=0 or r['asset_type']=='option' and q!=q.to_integral_value():raise ValueError('Positive units required; options use whole contracts')
            gross=q*price*mult if price is not None else None
            if r['amount_basis']=='gross_trade' and amount is not None and (amount<0 or gross is not None and abs(amount-gross)>Decimal('.01')):
                raise ValueError('Gross amount does not match source quantity/price/multiplier')
            if r['amount_basis']=='net_cash' and amount is not None:
                sign=-1 if action in ('buy','cover') else 1
                if sign*amount<0:raise ValueError('Net cash sign conflicts with action')
                if gross is not None:
                    implied=sign*gross-amount
                    if implied<Decimal('-.01') or commission is not None and implied+Decimal('.01')<commission:
                        raise ValueError('Net cash contradicts source quote/commission')
                    if fees is not None and abs(amount-(sign*gross-fees))>Decimal('.01'):
                        raise ValueError('Net cash contradicts reported total fees')
        elif r['amount_basis']!='net_cash' or amount is None or q not in (None,0):
            raise ValueError('Cash activity requires signed net amount, not a balance or quantity')
        else:
            if not r['asset_type'] and not r['symbol']:
                pass
            elif r['asset_type']=='cash' and r['symbol'] in ('','CASH') and r['multiplier'] in ('','1') and not any(r[k] for k in ('underlying','expiration','right','strike')):
                pass
            else:
                terms()  # An attributed dividend needs explicit security terms.
    else:
        day(r['as_of'],True)
        if r['snapshot_role'] not in ('opening','current') or r['snapshot_complete'] not in ('true','false'):
            raise ValueError('Confirm snapshot role and completeness; never infer completeness')
        if r['record_type']=='cash':
            if r['balance_category']!='book_cash' or r['symbol']!='CASH' or any(r[k] for k in ('asset_type','quantity','cost_amount','cost_basis','price','market_value','unrealized_pnl')):
                raise ValueError('CASH must be a separate book_cash observation, not buying power/NAV/flow')
            number(r['cash_amount'],True)
        elif r['record_type']=='position':
            mult=terms();q=number(r['quantity'],True);cost=number(r['cost_amount'],True);price=number(r['price'],True);market=number(r['market_value'],True);pnl=number(r['unrealized_pnl'],True)
            if not q or price<0 or r['asset_type']=='option' and q!=q.to_integral_value():raise ValueError('Invalid source position quantity/price')
            if r['cost_basis'] not in ('remaining_total','average_unit'):raise ValueError('Confirm cost basis; never derive missing historical cost')
            total=cost if r['cost_basis']=='remaining_total' else cost*q*mult
            if r['cost_basis']=='average_unit' and cost<0 or total*q<0:raise ValueError('Cost sign/basis contradicts long/short quantity')
            if abs(market-q*price*mult)>Decimal('.01') or abs(pnl-(market-total))>Decimal('.01'):
                raise ValueError('Source valuation/cost/P&L disagree; preserve source values and ask')
            if day(r['quote_as_of'],True)>r['as_of']:raise ValueError('Quote date is after snapshot')
        else:
            raise ValueError('Record must be position or cash')


def canonicalize_terms(values):
    expected={'equity':'1','option':'100','cash':'1'}.get(values['asset_type'])
    supplied=values['multiplier']
    changes=[]
    if expected and supplied and supplied!=expected and number(supplied,True)==Decimal(expected):
        values['multiplier']=expected
        changes.append(dict(field='multiplier',supplied=supplied,output=expected,reason='Canonical equivalent units; not inferred from missing data'))
    return changes


def mapped(spec, raw):
    if not isinstance(spec,dict) or 'column' not in spec or spec['column'] not in raw:
        raise ValueError('Missing configured source column')
    if set(spec)-{'column','values','date_format','datetime_format','timezone','number'}:raise ValueError('Unknown mapping operation')
    v=raw[spec['column']].strip()
    if 'values' in spec:
        if v not in spec['values']:raise ValueError('Unmapped source value '+repr(v)+' in '+spec['column'])
        v=spec['values'][v]
    if not isinstance(v,str):raise ValueError('Mapped values must be explicit text')
    if v and 'datetime_format' in spec:
        t=datetime.strptime(v,spec['datetime_format'])
        if t.tzinfo is not None:raise ValueError('Use a naive source format with explicit IANA mapping timezone')
        zone=ZoneInfo(spec['timezone']);aware=t.replace(tzinfo=zone)
        if aware.utcoffset()!=t.replace(tzinfo=zone,fold=1).utcoffset():raise ValueError('Ambiguous/nonexistent local time; source offset required')
        v=aware.isoformat()
    elif v and 'date_format' in spec:v=datetime.strptime(v,spec['date_format']).date().isoformat()
    if v and 'number' in spec:
        n=number(v,True)
        if spec['number']=='abs':n=abs(n)
        elif spec['number']!='plain':raise ValueError('Unknown number operation')
        v=format(n,'f')
    return v


def convert(source, profile, output):
    source=Path(source);output=Path(output);c=contract();role=profile.get('role')
    if profile.get('schema')!='tad.csv-map.v1' or role not in c['roles']:raise ValueError('Unknown mapping schema/role')
    if set(profile)-{'schema','mapping_version','role','header_record','metadata','defaults','columns','rules','exclusions','assertions'}:raise ValueError('Unknown profile setting')
    cols=c['roles'][role]['columns'];protected={'schema_version','mapping_version','source_kind','source_document_id','source_file_sha256','source_record_id'}
    for entry in [profile,*profile.get('rules',[])]:
        if (set(entry.get('defaults',{}))|set(entry.get('columns',{})))-set(cols):raise ValueError('Unknown target field')
        if (set(entry.get('defaults',{}))|set(entry.get('columns',{})))&protected:raise ValueError('Mapping cannot override provenance fields')
    if set(profile.get('metadata',{}))-set(cols) or set(profile.get('metadata',{}))&protected:raise ValueError('Invalid metadata field')
    if output.exists():raise ValueError('Choose a new output directory; existing files never overwritten')
    payload=source.read_bytes();digest=hashlib.sha256(payload).hexdigest();reader=csv.reader(io.StringIO(payload.decode('utf-8-sig'),newline=''))
    record=profile.get('header_record',1)
    if not isinstance(record,int) or record<1:raise ValueError('header_record must be a positive CSV record index')
    preamble=[];headers=None;previous=0
    for i,row in enumerate(reader,1):
        start=previous+1;previous=reader.line_num
        if i==record:headers=row;break
        preamble.append(dict(locator=f'lines:{start}-{previous}',raw=row,reason='Configured preamble before header'))
    if not headers or len(set(headers))!=len(headers):raise ValueError('Missing or duplicate source header')
    report=dict(tool_version=VERSION,schema=c['version'],mapping_version=profile.get('mapping_version',''),profile_sha256=hashlib.sha256(json.dumps(profile,sort_keys=True).encode()).hexdigest(),source_sha256=digest,source_name=source.name,state='blocked',qualification='Declared mapped observations; lightweight preflight, NOT final TAD import/reconciliation certification',preamble=preamble,counts=dict(input=0,converted=0,excluded=0,blocked=0,output=0),rows=[],outputs=[],mapping=profile)
    groups={};seen={};metadata={};snapshots=set()
    for row in reader:
        start=previous+1;previous=reader.line_num;locator=f'lines:{start}-{previous}';raw=dict(zip(headers,row));item=dict(locator=locator,raw=row,state='blocked',errors=[]);report['rows'].append(item);report['counts']['input']+=1
        try:
            if not row or not any(x.strip() for x in row):item.update(state='excluded',reason='Empty physical record');continue
            exclusion=next((x for x in profile.get('exclusions',[]) if raw.get(x['column'])==x['equals']),None)
            if exclusion:
                if not exclusion.get('reason'):raise ValueError('Exclusion needs a reviewable reason')
                item.update(state='excluded',reason=exclusion['reason']);continue
            if len(row)!=len(headers):raise ValueError('Row column count differs from configured header')
            for assertion in profile.get('assertions',[]):
                if assertion['column'] not in raw:raise ValueError('Missing asserted source column')
                expected=raw[assertion['equals_column']] if 'equals_column' in assertion else assertion['equals']
                if raw[assertion['column']]!=expected:raise ValueError('Source layout assertion failed: '+assertion['column'])
            values={k:'' for k in cols};values.update(profile.get('metadata',{}));values.update(profile.get('defaults',{}));columns=dict(profile.get('columns',{}))
            matches=[x for x in profile.get('rules',[]) if raw.get(x['when']['column'])==x['when']['equals']]
            if len(matches)>1:raise ValueError('Ambiguous row rules')
            for rule in matches:values.update(rule.get('defaults',{}));columns.update(rule.get('columns',{}))
            for k,spec in columns.items():values[k]=mapped(spec,raw)
            values.update(schema_version=c['version'],mapping_version=profile.get('mapping_version',''),source_kind='converted',source_document_id='sha256:'+digest,source_file_sha256=digest,source_record_id=locator)
            if any(not isinstance(v,str) for v in values.values()):raise ValueError('All mapped values must be text; blank means unknown')
            item['normalizations']=canonicalize_terms(values)
            validate(role,values)
            group=(values['source_broker'],values['account_ref'],values['currency'])
            signature=tuple(values[k] for k in ('account_name','account_type','timezone','as_of','snapshot_role','snapshot_complete') if k in values)
            if group in metadata and metadata[group]!=signature:raise ValueError('Conflicting metadata/snapshot scope within account')
            metadata[group]=signature
            if role=='positions':
                identity=group+tuple(values[k] for k in ('record_type','symbol','underlying','expiration','right','strike','balance_category'))
                if identity in snapshots:raise ValueError('Duplicate position/CASH snapshot; do not sum balances or cost lots')
                snapshots.add(identity)
            if values['execution_id']:
                identity=group+(values['execution_id'],)
                facts={k:v for k,v in values.items() if k not in protected}
                if identity in seen:
                    if seen[identity]!=facts:raise ValueError('Conflicting same execution identity; review correction, do not create a new ID')
                    item.update(state='excluded',reason='Exact duplicate execution ID and mapped facts');continue
                seen[identity]=facts
            groups.setdefault(group,[]).append(values);item.update(state='converted',mapped=values)
        except (ValueError,KeyError,TypeError) as e:
            item['errors'].append(str(e))
    for item in report['rows']:report['counts'][item['state']]+=1
    if not report['counts']['input'] or not groups:
        report['file_error']='No usable data records; empty templates are not import data'
    if not report['counts']['blocked'] and groups:
        report['state']='ready_for_TAD_review'
    output.mkdir(parents=True,exist_ok=False)
    if report['state']=='ready_for_TAD_review':
        for group,values in sorted(groups.items()):
            suffix=hashlib.sha256(json.dumps(group).encode()).hexdigest()[:12];name=f'TAD.{role}.{suffix}.csv'
            with (output/name).open('x',encoding='utf-8',newline='') as f:
                w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(values)
            report['outputs'].append(name);report['counts']['output']+=len(values)
    (output/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    lines=['# TAD CSV conversion / 券商CSV转换', '', '**'+report['state']+'**', '', 'Original SHA256: '+digest, '', 'Counts: '+json.dumps(report['counts']), '', 'No importable CSV is generated if ANY record is blocked. / 任一记录待核时，本次不生成可导入CSV。', 'Originals stay unchanged. Review in TAD, then explicitly apply. / 原件保持不变，在TAD核对后明确应用。', '', 'This report contains local source data: do not post it publicly. / 报告含本机来源内容，不要公开发布。', '']
    for item in report['rows']:
        lines.append('- '+item['locator']+' · '+item['state']+' · '+(item.get('reason') or '; '.join(item['errors']) or ('Mapped; normalizations: '+json.dumps(item['normalizations']) if item.get('normalizations') else 'Mapped; inspect report.json')))
    if report.get('file_error'):lines.append(report['file_error'])
    (output/'report.md').write_text('\n'.join(lines)+'\n')
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='command',required=True)
    a=sub.add_parser('inspect');a.add_argument('source',type=Path)
    a=sub.add_parser('convert');a.add_argument('source',type=Path);a.add_argument('--profile',type=Path,required=True);a.add_argument('--output',type=Path,required=True)
    a=sub.add_parser('validate');a.add_argument('source',type=Path);a.add_argument('--role',choices=['transactions','positions'],required=True)
    args=p.parse_args()
    try:
        if args.command=='inspect':
            data=args.source.read_bytes();rows=list(csv.reader(io.StringIO(data.decode('utf-8-sig'),newline='')))
            print(json.dumps(dict(sha256=hashlib.sha256(data).hexdigest(),record_count=len(rows),first_records=rows[:10]),ensure_ascii=False,indent=2));return 0
        if args.command=='convert':
            report=convert(args.source,json.loads(args.profile.read_text()),args.output)
            print(report['state']+' · '+str(args.output/'report.md'));return 0 if report['state']=='ready_for_TAD_review' else 2
        c=contract();errors=[]
        with args.source.open(encoding='utf-8-sig',newline='') as f:
            reader=csv.DictReader(f)
            if reader.fieldnames!=c['roles'][args.role]['columns']:raise ValueError('Exact canonical column order required by this helper')
            n=0
            for n,row in enumerate(reader,2):
                try:validate(args.role,row)
                except (ValueError,TypeError,KeyError) as e:errors.append(dict(record=n,error=str(e)))
        if not n:errors.append(dict(error='Empty template; add source-backed rows'))
        print(json.dumps(dict(state='blocked' if errors else 'preflight_only',errors=errors),indent=2));return 2 if errors else 0
    except (ValueError,OSError,UnicodeError,csv.Error,KeyError,TypeError) as e:
        print('Blocked / 已停止: '+str(e),file=sys.stderr);return 2


if __name__=='__main__':
    raise SystemExit(main())
