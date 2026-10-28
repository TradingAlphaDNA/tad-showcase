# Evaluate your own trading data locally

> **Your broker data stays on your computer.** In the current local TAD app, broker files and account data are imported, processed and saved on your own computer—not uploaded to a TAD cloud service. The interface's “Upload” action submits files to the app running on your computer. Sharing anything yourself through public feedback, email or an external service is a separate action.


[中文](personal-data.zh.md) · [Support matrix](broker-support.en.md) · [Export guide](broker-export.en.md) · [Install and synthetic checks](README.en.md)

**Optional personal-data evaluation, after the supplied synthetic smoke test.**
The app permits supported real files; this is not certification of your exports,
complete history, cash or tax results. The downloadable kit's acceptance cases
remain synthetic-only. These online instructions explain the separate personal
workflow; no binary or old attachment has changed. Signing, hardware and OS
limits in the installation guide still apply.

## 1. Keep synthetic and personal accounts separate

Complete the supplied synthetic test first. For personal evaluation, initialize a
**different, fresh personal directory** using the existing setup option. For example,
drag `Setup.command` from the extracted app into Terminal and append:

```text
--destination "$HOME/Applications/TAD-Personal-Preview" --port 8889
```

Use an unused port. Keep the existing synthetic directory and any other TAD
installation intact. Start/stop the new environment using its own Start.command /
Stop.command; do not run Setup over a live directory, copy a private store into
it, hand-edit configuration or move the initialized directory. Existing directories
are not an automatic upgrade path. If setup refuses a path, retain it and choose
a new location. This guide does not migrate or upgrade an existing installation.

Your originals, documents, drafts and preferences are retained locally by this
preview; there is no automatic broker-file upload. Keep independent originals.
Public issues and external AI services are separate destinations: do not send
personal files, account identifiers, backups, credentials or private logs there.

## 2. Prepare one account with a defensible start

Use the [broker-specific export guide](broker-export.en.md). Begin with one
account and an interval you can substantiate, rather than your entire portfolio.
You need:

- Supported original transactions covering the selected interval and a complete
  positions snapshot for the intended cutoff, when comparing current holdings.
- The correct account/broker/type and actual file dates. Choose an existing
  account only if it is the same account; otherwise use **New account (confirm
  identity first)**. Do not choose an unrelated account to get past a prompt.
- An opening date **before the first included trade**, opening cash, and every
  opening security quantity and **total** cost from that boundary. For example,
  with activity from January 2 onward, use supported balances at January 1 close.
  Do not put today's balances/costs into that earlier opening snapshot.
- Evidence that the selected activity and opening positions are complete. An
  empty opening portfolio is valid only when it really was empty; missing is not
  zero. If you cannot truthfully confirm the required boundary/completeness,
  retain the originals, save a draft and stop before application.

For E*TRADE annual labels, inspect actual year and observed coverage; a year name
alone does not supply missing dates or a complete opening. If a new account's
multi-file history cannot pass the supported boundary checks, save a draft and
report that limitation instead of editing files or claiming completeness.

## 3. Choose the matching upload route

### One account, one activity CSV and one positions CSV

The ordinary **Upload broker files** page can receive several files, but its
**Review selected files** handoff permits **one confirmed account, at most one
activity CSV and one positions CSV per update**. Other uploaded originals are
retained; they are not automatically merged or applied. Select just that pair
(or the one supported file needed for an existing-account update).


Open **Upload broker files**, select the originals, then open each file's
**Review / Read and check** surface. Check recognized broker and kind, account,
period/snapshot date, sample rows and counts. For Moomoo positions, explicitly
confirm the actual snapshot date. Changes that require re-reading must be saved
and the refreshed preview checked before proceeding.

Confirm account association for each file, using consistent identity for files
of the same new account. Optional **Archive as** provides a meaningful document
name; it does not change the broker-original contents or apply an account update.
Save review, then select only the intended transaction/position files for this
update and choose **Review selected files**. A PDF statement follows the archive
route; it is not a financial input for this update.

### Several activity files or several accounts

Use **Batch update** in the upload page navigation, or **Batch update multiple
accounts** from Account data, rather than selecting multiple activity CSVs in
the ordinary handoff. Add the originals there and choose **Add and check files**;
review each account group, actual snapshot dates and any missing facts. Batch
update CSVs are limited to 8 MiB each, 16 MiB and 40 files per account; PDF archives
are limited to 16 MiB each. Smaller export intervals must still form a supported,
complete history; do not truncate rows to meet a limit.

For a new account, use **These files belong to a new account…**, then
**Continue: opening facts** and **Continue with actual opening facts**. The opening
wizard initially uses one primary activity file and at most one latest positions
snapshot, not all selected history. Its cutoff and snapshot must be compatible;
if that cannot be established from the available files, save the draft and report
the limitation instead of confirming incomplete history.

After the opening account has been explicitly applied, use **Return and continue
batch files** / **Return and continue this batch**, then **Recheck unfinished
accounts**. Review and explicitly **Confirm and update … accounts** for remaining
ready files/accounts. Completing the opening wizard alone does not apply every
file retained in the batch. Keep the saved batch receipt to resume work; do not
create another account to process its remaining files.

## 4. Preview and explicitly apply

In the account wizard/batch review, inspect the opening boundary (new account),
new/existing/uncertain row counts, activity dates, latest positions and warnings.
A duplicate-count summary is not a guarantee that every ambiguity is resolved:
genuine identical fills must not be deleted as duplicates.

Check the intended cutoff against the positions date. A snapshot newer than the
covered activity is not a substitute for the missing activity. Multi-account or
multi-file selection is not one undifferentiated result: review **each account
and every selected file's final status**, including any queued follow-up update.
If a file is excluded or still pending, it has not updated analysis.

Only after the evidence matches, choose the existing **Confirm and apply /
Apply account update** action. Wait for completion and confirm that the account
result and intended files show applied. A button click, saved draft, archived
file or ready preview is not completion.

## Understand the states

These are business meanings; exact labels can vary by screen/language.

| State | What changed | What to do next |
| --- | --- | --- |
| Archived / 已归档 | The source/document name and review are retained; no account result is applied by this action | For transactions/positions: select for update, use Review selected files and continue account review; use Batch update for several activity files/accounts. For a statement PDF: archive is the supported endpoint; obtain supported CSVs to update analysis. |
| Pending update / 待更新 | The financial source is not yet applied; identity, dates, completeness, preparation or confirmation may remain | Read the missing-item message, open the saved review/draft, fix only supported facts, check again and explicitly apply. If the UI cannot consume existing evidence, report the system gap. |
| Applied / 已应用 | The accepted input has been adopted into the account's saved result | Verify the account, scope, cutoff and resulting holdings/P&L/cash qualification. This does not mean all history and cash are reconciled. |
| Needs review / partial / 待核 | Some fact, relationship or qualification remains uncertain, including after application | Inspect the affected item and result scope. Add existing evidence through a supported action if available; otherwise retain it and report the specific limitation. Do not assume the uncertain value is zero. |

## 5. Check the result and later updates

- **Positions:** compare all symbols, signed quantities, account and actual snapshot
  date. A filtered/old report cannot prove an absent holding is closed. Do not
  fabricate a closing transaction to remove a discrepancy.
- **P/L and returns:** inspect period, realized versus saved unrealized, costs/fees,
  opening history and the displayed matched scope. A known subset result is not
  total account return. Current saved prices are not live quotes.
- **Cash:** compare opening + known cash movements with a same-date broker balance.
  Keep CASH, buying power, net assets and collateral usage separate; do not add
  cash again to an inclusive total or count shared strategy support twice.
  Full cash qualification may remain partial, including the known retained-opening
  evidence limitation described in the [matrix](broker-support.en.md).
- **Later updates:** use the same existing account, upload supported newer originals,
  check overlap/new rows and cutoff, and explicitly apply again. Do not create
  another account for the same history. Overlap conflicts need review, not manual
  deletion of identical-looking fills.
- **Retention:** stop and restart using this environment's own entries; check that
  personal documents, pending drafts and display settings remain. Do not reinstall
  or clear the directory to resolve an import problem.

## 6. Get help without publishing your records

Use [technical-preview feedback](https://github.com/TradingAlphaDNA/tad-showcase/issues/new?template=technical-preview.yml).
Give kit/app version, chip/OS, broker/report type, synthetic versus personal mode,
step reached, sanitized error, and whether the account is archived/pending/applied
with unresolved items. Say whether the problem affects positions, P/L or cash.
**Do not attach originals, real transaction rows, balances, account IDs, backups,
keys or logs with private paths.** Reproduce with supplied synthetic files where
possible; if those pass but your report does not, preserve the original locally.

Documentation cannot clear a parser, coverage or analysis defect. Record that as
pending system work; do not repeatedly re-upload files or invent missing values.

## Standard CSV for another broker

Use the [Standard CSV guide](standard-import.en.md). TAD accepts this explicit contract in alpha.2; it does not automatically understand arbitrary broker files or validate AI mapping truth. Retain the actual account and unknown facts, and review before explicit apply.
