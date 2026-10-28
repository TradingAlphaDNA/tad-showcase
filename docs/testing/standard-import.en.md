# Standard CSV import — TAD 1.1.0-alpha.2

[中文](standard-import.zh.md) · [Bilingual field guide and downloads](../standard-import/index.html)

Your broker data is imported, processed and saved on your own Mac. The TAD upload action sends files to the local app, not to a TAD cloud service. Source code remains private; this is an under-development, intended-shareware technical preview.

## Download the two templates

- [Activity: TAD.transactions.v1.csv](../standard-import/TAD.transactions.v1.csv)
- [Positions + CASH: TAD.positions.v1.csv](../standard-import/TAD.positions.v1.csv)
- [Filled activity example](../standard-import/examples/TAD.transactions.example.csv) · [filled positions example](../standard-import/examples/TAD.positions.example.csv)

Requires **alpha.2 or later with Standard CSV Connector**. Earlier alpha.1 cannot import these files. Keep every header column; blank templates contain no account evidence. The field guide provides every field and the mapping checklist in English and Chinese.

## Try the constructed case first

In a **fresh** TAD test environment, choose Create account → Standard CSV. Import the filled activity example. Confirm account reference `sample-account`, source broker `sample_broker`, opening close `2026-01-01`, cash `1000`, no opening securities and activity through `2026-01-03`. Confirm the complete synthetic opening/activity and explicitly apply. Then use Upload files / Update accounts to associate the filled positions example with that existing account, inspect it and explicitly apply. The current snapshot is not an opening balance.

Expected: bought10 shares at2, sold4 at3; remaining6 shares, remaining cost12, realized gross gain4. The dated price3 gives market value18 and unrealized P/L6. CASH992 is a balance observation and adds no new deposit or profit. Fees remain qualified by available source evidence; no completeness certification is implied. Repeated identical activity must not create another gain. An account's current snapshots/quotes use their saved date, independently of realized-period filters.

## Convert an unsupported broker locally

1. Retain the original unchanged. Choose a stable actual broker key and account reference; one broker/account/currency per CSV. One fill row must be one real execution, not an invented split of an order total.
2. Map explicit observations using the field guide. Preserve actual execution IDs or original hash/document+row locators across repeated exports. Do not invent dates, fees, zero amounts, cost, proceeds, expiry/assignment/exercise records or completeness.
3. Use `net_cash` for signed actual cash including fees, `gross_trade` for nonnegative gross magnitude, or `unqualified`. `remaining_total` cost is signed (short negative); `average_unit` is a nonnegative per-unit cost. The opening form separately asks for total cost magnitude. Current position value must agree with quantity×quote×multiplier and reported unrealized P/L with market−signed cost.
4. Review account, dates, known/unparsed rows, partial coverage and unresolved items. Archived means saved; Pending update means not yet applied; only explicit Apply adopts results. Existing native and Standard channels cannot silently mix; do not create a second account for the same history.
5. Keep personal testing separate from the synthetic exercise. Setup does not upgrade an existing installation; preserve it and choose a new destination. See [personal-data evaluation](personal-data.en.md).

AI conversion is optional and happens outside TAD. Prefer a local converter. Sending originals to a cloud AI is your separate voluntary data transfer; TAD does not do it. Review the AI mapping row by row before applying; TAD validates structure and consistency, not whether an AI truthfully read the original.

## Bounds and pending items

USD equities and standard100-multiplier US equity options only; no adjusted/nonstandard deliverables, FX conversion, futures or crypto. Position valuation rows require source cost/basis, price, market value, unrealized P/L and quote date; missing facts remain pending, not zero. Partial snapshots do not close absent positions. Only one account book_cash balance is admitted; buying power, NAV and TOTAL are not cash. Source hashes and completeness flags are declarations, not independent broker-original or full-history proof. Quantity termination without proceeds cannot manufacture P/L. Conflicting occurrences/uncertain overlap require review; unknown identity cannot be guessed. The retained historical opening/posted-cash qualification limitation remains disclosed in the support matrix.

Use sanitized [feedback](https://github.com/TradingAlphaDNA/tad-showcase/issues/new?template=technical-preview.yml); never attach real account rows, originals, backups, keys or private logs publicly.

## Optional conversion assistant

[Download companion skill0.1.0](https://github.com/TradingAlphaDNA/tad-showcase/releases/tag/tad-broker-csv-v0.1.0) and read its [English guide](../../skills/tad-broker-csv/README.en.md). It uses the same two templates, explicit source mappings, a local Python3.10+ helper and per-row reports. No app source is included. Use alpha.3 for the reviewed same-name multi-account path; alpha.2/r1 has a known identity-composition limitation. Unknown Journal/lifecycle events block output. External cloud AI submission is a separate voluntary transfer.
