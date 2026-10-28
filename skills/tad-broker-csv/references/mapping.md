# Explicit mapping v1 · helper 0.1.0

The helper is newly written public transformation/preflight code; private TAD Readers and investment calculations are not included. TAD's shared core remains authoritative. Public standard: tad.standard-csv.v1, USD stocks and standard multiplier100 US equity options. Native broker routes and this skill are complementary.

A profile uses `schema: tad.csv-map.v1`, `mapping_version`, `role: transactions|positions`, `header_record` (1-based CSV record index, not a physical-line guess), `metadata`, `defaults`, `columns`, optional exact `rules`, `exclusions`, `assertions`. Unknown keys/target columns are rejected. See the runnable JSON examples.

- Metadata declares source_broker/account_ref/account_name/account_type/currency/timezone. These must describe the actual source/account, not the synthetic examples. Per-row metadata columns split account outputs; conflicting account or snapshot metadata blocks conversion. Stable references are not filenames or display labels.
- Defaults are explicit confirmed source/report facts, not guesses. Account dates, units, `amount_basis`, cost basis and snapshot flags need evidence. Never put an invented fee/cost/zero into defaults. Review reports list the whole mapping and mapped rows so defaults remain visible.
- A column spec contains `column`; optional `values` is an exact whitelist (unmapped values block), `number: plain|abs`, `date_format` for dates, or `datetime_format` plus explicit IANA `timezone` for local times. Use `abs` only when the source sign convention and mapped action are confirmed. No arbitrary code/eval, thousands/currency stripping, locale guessing, fill expansion or arithmetic to invent missing observations. Plain decimals only. ISO offset timestamps can be mapped directly without conversion.
- A rule matches exactly `when: {column, equals}`, adds `defaults` and overrides `columns`. Multiple matching rules block. CASH examples clear security fields and map only a separate book balance. No row is excluded because its amount is unknown.
- An exclusion matches exact `{column, equals, reason}` and is reported with its physical locator/raw row. Blank rows are explicitly reported. Configured preamble before the header is retained in the report separately. No wildcard footer skipping.
- Assertions require `{column, equals}` or `{column, equals_column}`. The narrow Moomoo example requires full single-fill rows (Order Qty=Fill Qty and Status=Filled). Hierarchical orders, partial/multiple fills and new layouts require a new reviewed mapping or the native Connector. Do not map order totals and individual fills simultaneously.

Explicit numerically equivalent multipliers such as1.0 for equity and100.0 for a standard option are emitted as the contract strings1 and100. Each such normalization is recorded beside the source row in both reports; it changes representation only. Missing or unsupported multipliers are never inferred. The validate command requires the canonical strings. contract.json distinguishes schema_introduced_app(alpha.2) from this companion workflow compatible_app_min(alpha.3).

Each derived row has actual source_file_sha256, `source_document_id=sha256:<original hash>`, source_record_id physical `lines:start-end`, mapping_version, and optional original execution_id/order_id. The helper cannot override these provenance fields through a profile. A changed mapping does not change occurrence identity. Identical repeated execution IDs are reported as exclusions; conflicting same IDs block. Without stable IDs, different overlapping originals cannot be automatically proven duplicates. TAD's native/converted overlap checks and user review remain necessary. Declared provenance never certifies broker originality or coverage.

The helper checks supplied quote × units × multiplier, signed cost/value/P&L consistency, amount direction/basis, reported fee relationships, dates and timezones. These checks reject contradictions; they do not reconstruct economic history, create absent P/L/cash values or certify all fees complete. Lifecycle events, adjusted contracts, non-USD and semantic uncertainty are blocked. The bundled standard may express more events than helper0.1 safely converts.

## Accumulated broker lessons

| Reference | Reused lesson | Example boundary |
|---|---|---|
| Chase | Type/action, signed quantity vs positive trade units, account/date columns, net vs commission; separate book cash in positions | Constructed stock Buy/Sell and fixed position layout; source Account Number is preserved |
| E*TRADE | Activity header after report preamble, net Amount $, reported Commission, annual period metadata; summary purchasing power is not book cash; CASH/TOTAL/footer distinguished | Constructed header-record7 activity and record10 positions; dates/account in example metadata are explicit synthetic confirmations |
| Moomoo | Actual fill quantities/prices/times vs order summary, gross Fill Amount vs reported Total fee, explicit timezone; average unit cost vs signed position value | Constructed single full fills and stock-only current snapshot; options require explicit terms from a reviewed mapping |
| Custom synthetic | Different field names/order/date format, signed fee-inclusive net amount, independent cash observation | Demonstration of an unknown layout, not certification of any fourth real broker |

Native sources can contain events or evidence beyond these example profiles. An unknown event must block and surface a question, not disappear. A complete opening inventory and book cash/date boundary still need confirmation in TAD; a current snapshot is not an opening inventory.
