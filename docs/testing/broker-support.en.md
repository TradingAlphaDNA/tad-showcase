# Supported broker files — 1.1.0-alpha.2

> **Your broker data stays on your computer.** In the current local TAD app, broker files and account data are imported, processed and saved on your own computer—not uploaded to a TAD cloud service. The interface's “Upload” action submits files to the app running on your computer. Sharing anything yourself through public feedback, email or an external service is a separate action.


[中文](broker-support.zh.md) · [Export guide](broker-export.en.md) · [Use your own data](personal-data.en.md) · [Install and synthetic checks](README.en.md)

**Support means the specific file layouts below, not every export from a broker.**
This public kit contains app **1.1.0-alpha.2**. All three native Connectors and the Standard CSV Connector are included. The first personal-data evaluation scope is **USD
investment accounts, stocks and supported standard US equity-option records**.
Other currencies, regions, languages, products and adjusted/nonstandard options
are not promised by the broker name. There is no automatic broker login or sync.

## Choose the files

| Broker | Transaction input | Current positions input | Additional evidence and limits |
| --- | --- | --- | --- |
| Moomoo | English-header order/fill-history CSV with execution details and available fees | CSV with `Symbol`, `Quantity`, `Current price`, `Average Cost`, `Market Value`, `Unrealized P/L`, `Currency` | Confirm the actual snapshot date. These positions do not by themselves establish a cash balance. Order history is not complete non-trade cash activity. |
| Chase / J.P. Morgan investment accounts | Complete **31-column** investment-transactions CSV, including account identity, dates, type, security description, quantities and USD amounts | Complete **71-column** investment positions CSV, including `As of`, `Ticker`, `Quantity`, `Asset Class`, `Pricing Date` | A realized gain/loss CSV reader exists for historical comparison/reconciliation. It is **not** a third financial input in the ordinary upload/update flow. Checking, credit-card and merchant CSVs are not this format. |
| E*TRADE | `Account Activity for ...` CSV, with explicit date range or supported Current Year / Prior Year header, and the full 13-column activity table | Complete `View Summary - All Positions` portfolio CSV with account summary, `Net Account Value`, full positions table and `Generated at ... ET` | A CASH row is a balance observation. Cash Purchasing Power is not cash; TOTAL already includes cash. Filtered portfolio views and missing account/date metadata are not supported substitutes. |
| Standard CSV (converted / user supplied) | TAD.transactions.v1.csv | TAD.positions.v1.csv with separate CASH | USD equity / standard100 US options; declared provenance; exact account identity, unknown values and incomplete coverage remain explicit. [Guide](standard-import.en.md). |

Native formats preserve broker originals and use the same core reconstruction
and analysis. A CSV that is recognized can still require review before it can be
applied. Renaming XLSX/PDF to CSV, translating headers or converting another
broker into a Moomoo-looking file does not make it supported. **For unsupported brokers, use the [Standard CSV Connector and templates](standard-import.en.md), not a forged native layout.**

## What has actually been checked?

| Level | Evidence / boundary |
| --- | --- |
| Implemented | Three separate versioned Connectors, shared core, account review, preview, explicit application and update paths. |
| Checked in the downloadable binary on the development Mac | Constructed cases for each broker: new account, transactions plus positions, incremental update, overlap/dedup and repeat application; saved results and retained documents/draft/display preference. The Moomoo case also checks options/shared support. |
| Existing private project history | Prior real-account import/reconciliation work informed the readers. This is not certification of a new tester's files and does not publish private evidence. |
| Pending | Test-user Mac compatibility and each tester's real export/account/history. Chase/E*TRADE public synthetic cases are simple stock/cash cases, not full option-lifecycle certification. |

Mac signing and hardware/OS limits remain in the [installation guide](README.en.md).
This documentation update does not rebuild the binary or expand its tested scope.

## What might need review?

| Item | Effect on results | Next step |
| --- | --- | --- |
| Missing earlier buys, opening quantity/cost, or uncertain account identity | Closed-chain P/L, remaining cost and strategy support can be incomplete; current snapshot values do not repair missing history | Use the same account's earlier originals or a supported, evidenced opening boundary. Do not invent trades or assume zero. Save the draft if confirmation is not possible. |
| Missing cash activity or independent balance evidence | Trade/position results may be useful while cash remains partial; buying power, net assets and cash are different quantities | Check opening cash, transfers, dividends, interest, fees and balance date. A bank/statement PDF archived alone does not qualify cash. |
| E*TRADE Current Year / Prior Year | The reader derives the absolute year from observed rows, not today's date. It does not prove full-year coverage; empty or mixed-year annual files need review | Prefer an explicit date-range original. If source coverage and the opening boundary cannot be confirmed, save a draft and report the sanitized issue; do not edit the header to force acceptance. |
| Changed schema, unknown action, adjusted option, transfer/expiry/assignment ambiguity | May block reading or leave an affected chain/position/result unqualified | Keep the original locally; report the version, report type and sanitized error. Re-export a supported report if available. Do not rewrite the event as an ordinary trade. |
| Incremental update with retained historical opening evidence | A known core limitation can leave posted-cash qualification partial even when the opening evidence is already retained | Preserve that evidence and report the issue. This can be system work, not missing user files. Do not repeatedly upload or alter balances to clear the status. |

**Applied is not the same as fully reconciled.** Current values are saved broker
observations, not live quotes. Known P/L may be shown while some costs, returns or
cash are unavailable; a matched-subset return is not a whole-account return.
See [the states and next actions](personal-data.en.md#understand-the-states).

## Statements and historical reference files

PDF statements can be archived and associated with an account for later inspection.
**General PDF extraction, automatic statement-to-trade conversion and automatic
cash reconciliation from an archived PDF are not supported.**

Chase's realized gain/loss reference reader supports existing historical
reconciliation capabilities, but the ordinary public file-first workflow only
applies transaction and position files. Do not relabel a gain/loss file as
transactions. The guide does not claim a self-service historical-reference
adoption button; if the normal workflow cannot consume an existing proof, retain
it locally and report the gap without attaching the original publicly.
