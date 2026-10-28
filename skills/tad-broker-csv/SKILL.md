---
name: tad-broker-csv
description: Use when converting broker activity or position CSV files to TAD standard templates, especially for a broker or export layout that TAD does not natively support.
---

# TAD broker CSV conversion assistant

Convert source observations for **local TAD review**, not automatic adoption. Use the existing `tad.standard-csv.v1` contract; never impersonate a supported broker. Prefer TAD's native Connector for a supported original export.

Read [the field guide](assets/standard-import/index.html) and [mapping rules](references/mapping.md) before choosing semantics. Exact templates and their fingerprints are under `assets/standard-import/` and `references/contract.json`. [English](README.en.md) / [中文](README.zh.md) cover installation, commands and compatibility.

## Work with the user's actual file

1. Preserve original bytes. Inspect with `python3 scripts/convert.py inspect "source.csv"`; reports may contain private rows, so keep them local. Do not claim a hash or original-file validation from pasted text.
2. Establish the actual broker, stable account reference, currency, date interpretation, quantity units, amount/fee basis and snapshot scope from source evidence and user confirmation. Save a versioned JSON mapping. `profiles/` are narrow **synthetic examples**, not universal broker detection. Ask concrete questions for unresolved meanings; do not ask users to repeat facts already present.
3. Convert with `python3 scripts/convert.py convert "source.csv" --profile "mapping.json" --output "NEW-directory"`. The tool preserves original hash and physical line spans, and accounts for every data record. It never overwrites an existing output directory. Any blocked record prevents **all** importable CSV output for that input; `report.md`/`report.json` explain what to resolve. Do not present the mapped subset as a completed conversion.
4. Check both reports and independently compare counts, actions, quantities, amounts, account boundaries and source dates. Run `python3 scripts/convert.py validate "output.csv" --role transactions` (or `positions`). This is lightweight preflight, not authoritative financial certification.
5. Return output paths, input/output/excluded/blocked counts, scope, unresolved questions and next TAD action. Import into compatible TAD (alpha.3 or later compatible build), inspect the account/opening facts and rejected rows, then let the user explicitly apply. Archived means stored, not applied; applied does not mean fully reconciled.

Use the matching alpha.3 app: alpha.2/r1 has a same-name distinct-account composition limitation. Preserve source identity; do not work around an old package by changing broker or account references. See README compatibility scope.

## Non-negotiable source meanings

- Missing is not zero. Never invent fees, historical cost, executions, zero-price closures, source completeness or execution IDs. Do not infer zero fees from net matching price × quantity.
- Preserve distinct fills; order summaries are not extra executions. Use stable real execution IDs when supplied; otherwise original SHA + physical locator. Renaming output or changing mapping version must not create a new occurrence. Different overlapping originals without stable execution IDs require TAD/user review, not fabricated identity or silent deduplication.
- Signed positions and positive trade quantities differ. Standard US options use whole contracts and multiplier100 with explicit terms; no adjusted deliverables or FX inference. Supplied costs/valuations must agree; never calculate missing cost or P/L to make an export pass.
- CASH book balances are position observations, not deposits, buying power or NAV. Snapshots cannot manufacture buys/sells or prove absent holdings closed. Keep partial snapshots partial. Journal, expiry, assignment and exercise are deliberately blocked by helper0.1; resolve from evidence or use a suitable native path, never relabel them as ordinary trades.
- Local dates may lack exact time; preserve actual offset-aware execution time when known. Named-zone mapping must reject ambiguous/nonexistent DST times until source offset is resolved.
- This skill does not upload, call an AI API, apply account updates or compute investment/strategy returns. External cloud AI submission is a separate user-authorized transfer. Python3.10+ is a helper prerequisite, separate from the self-contained TAD application. Do not install runtimes, skills globally or change settings without corresponding user authority.
