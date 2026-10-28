# TAD broker CSV conversion assistant · 0.1.0

[中文](README.zh.md) · [Exact templates and bilingual field guide](assets/standard-import/index.html)

For supported USD stocks and standard US equity options, this companion helps a local-file-capable AI assistant prepare TAD CSVs. Use TAD **1.1.0-alpha.3 or later compatible versions** for this reviewed workflow. The CSV schema first appeared in alpha.2; earlier alpha.2/r1 builds have an account-composition limitation, and alpha.1 cannot read the templates. It is not a universal broker importer. Use a native Connector first when your original format is supported.

## Install or load

Download `TAD-broker-csv-skill-v0.1.0.zip` from the showcase companion Release, verify SHA256SUMS, and extract the `tad-broker-csv` folder. This public folder contains the skill, helper source, exact templates and constructed examples, not the private TAD application source.

For Codex, place that whole folder in your configured skills directory (normally `~/.codex/skills/`), then start a new chat and invoke `$tad-broker-csv`. If that directory already contains the skill, retain the old version and choose an explicit upgrade path. Do not merge partial folders. An AI assistant with permitted filesystem access can also read the extracted SKILL.md directly without global installation: “Read /absolute/path/tad-broker-csv/SKILL.md and use it to inspect my CSV, prepare a mapping, and report anything that prevents conversion.”

Verified scope is documented in the release acceptance report. Manual skill loading and local helper invocation can be tested independently of automatic skill discovery. Other AI applications have different installation/file/script capabilities: use their supported skill-import mechanism or ask them to read the folder. No promise is made that every AI host can install or execute it. A text-only AI cannot verify actual file bytes or run the tool.

**Helper prerequisite: Python3.10+ (standard library only), separately installed by you if needed.** This is different from the TAD Mac app, which bundles its own runtime and does not require Python/Git/Node/API keys. The helper is portable Python; this release's actual OS/runtime test coverage is limited to the recorded Mac evidence. No Windows application support is implied. No pip packages or AI account are required by the helper.

## Try the entirely synthetic example

In Terminal, change to the extracted skill folder. These outputs must be NEW directories:

```bash
python3 scripts/convert.py inspect examples/custom-transactions.csv
python3 scripts/convert.py convert examples/custom-transactions.csv --profile profiles/custom-transactions.json --output /tmp/tad-custom-activity-new
python3 scripts/convert.py convert examples/custom-positions.csv --profile profiles/custom-positions.json --output /tmp/tad-custom-positions-new
```

Inspect both `report.md` and `report.json`. Expected activity: 10 SYN bought at2 with net−20.50 and reported fee0.50; 4 sold at3 with net11.50 and fee0.50. Remaining6, gross realized4, known trade cash change−9; a separate book_cash snapshot is991, not another transfer. Current source cost12/value18/unrealized6 is supplied, not invented by the helper. TAD may keep return/cash qualification partial when opening proof or complete fee evidence is missing.

Each directory contains per-account `TAD.transactions.<id>.csv` or `TAD.positions.<id>.csv`. The exact header contract, rather than the output filename, identifies the format. Run `python3 scripts/convert.py validate /absolute/output.csv --role transactions` (or positions). Exit0 means preflight only; exit2 means blocked. Any blocked record means **no importable CSV for that input**, including otherwise mapped rows. Reports explain the physical lines, source values and questions. No original is modified or output folder overwritten.

## Prepare your own broker mapping

Have the AI read [mapping rules](references/mapping.md), the exact templates and your local file. Keep actual broker/account references stable; confirm unknown quantity, fees/net/gross, account dates, timezone, cost basis and opening/current scope. Save a separate mapping JSON with a version. The six broker profiles are narrow **synthetic regression examples**, not a safe default for every real export. In particular, the E*TRADE/Moomoo dates and account metadata in those profiles are constructed examples—never apply them to personal data unchanged.

The helper does not infer option terms from a symbol, assume zero fees/cost, expand order totals into fills, guess Journal/expiry/assignment/exercise, derive trades from a position snapshot or treat buying power as cash. Helper0.1 deliberately blocks lifecycle events even though TAD's standard/native paths may support evidence-backed events. Ask for missing evidence or use the appropriate native path. Different overlapping originals without stable execution IDs still require TAD review.

Once reports are clear, open compatible TAD, choose Standard CSV or the local document workflow, review the actual account and date range, confirm opening holdings/book cash, inspect pending items, then explicitly apply. **Archived = stored; pending update = not applied; applied ≠ fully reconciled.** Do not create another account to bypass a native/converted collision.

## Compatibility and verified scope

Earlier alpha.2-r1 was observed to reject same-name/same-broker accounts with different full account references (`recovery_accounts_overlap`). Use the matching alpha.3 preview for the corrected account identity path; do not rename broker/account identities to work around an old package. Acceptance evidence for same-name distinct accounts, legacy identity preservation, updates, restart and synthetic recovery is recorded with the companion release. This helper does not migrate personal installations.

Manual filesystem loading in Codex with Python3.10 has been forward-tested on the synthetic example and a Journal counterexample; automatic global skill discovery/installation and other AI hosts have not been verified. Source-core parity tests used Python3.12; helper runs were checked on Python3.10/3.12, macOS15.2 Apple Silicon.

## Privacy and license

The helper runs locally, makes no network requests, uses no API key/telemetry and does not import/apply into TAD. Reports contain source data; do not post them publicly. Your TAD broker data stays on your computer. Giving CSVs to an external cloud AI is a separate voluntary data transfer governed by that service; this skill does not make it local. Keep originals and backups, and share only constructed/redacted examples for feedback.

The newly written skill/helper and its constructed mapping examples use the included MIT license. TAD application source remains private/proprietary; no application license is granted. Bundled standard templates/guide retain the permissions and attribution in LICENSE.txt. This helper does not certify broker accuracy or recommend trades.
