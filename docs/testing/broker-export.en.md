# Export the right broker files

> **Your broker data stays on your computer.** In the current local TAD app, broker files and account data are imported, processed and saved on your own computer—not uploaded to a TAD cloud service. The interface's “Upload” action submits files to the app running on your computer. Sharing anything yourself through public feedback, email or an external service is a separate action.


[中文](broker-export.zh.md) · [Support matrix](broker-support.en.md) · [Import your own data](personal-data.en.md)

These are **report-selection and output checks for this TAD build**. Broker
menus vary by region, account and UI version; the logged-in click paths have not
been independently verified for every tester. Navigation names below are hints,
not a promise of a particular current menu. Use the broker's own support if its
export differs. A menu saying CSV does not prove TAD compatibility.

## Before exporting

1. Select **one investment account** and record its account type and date range
   privately. Export each retirement/brokerage account separately.
2. Download original CSVs with English headers and unchanged metadata. Keep a
   separate local copy; do not edit/re-save originals in a spreadsheet.
3. Include all activity in the intended interval, including relevant fees,
   dividends, interest and transfers where the report provides them. Do not
   filter to one ticker or only profitable/closed trades.
4. Obtain a complete latest positions export with its actual date. A positions
   snapshot is not past transaction history or an opening balance.
5. Retain earlier originals or statements supporting the opening boundary.
   Missing earlier history must remain visible; do not invent an opening trade.

## Moomoo

In the desktop trading account, look for order/trade **History**, choose the
account and interval, and use the history export/download action. Export the
current account's **Positions** separately. Do not use a market/watchlist export
or a PDF statement as the trading CSV.

The supported history layout includes `Side`, `Symbol`, `Name`, `Order Price`,
`Order Qty`, `Status`, `Filled@Avg Price`, `Order Time`, `Order Type`, `Fill Qty`,
`Fill Price`, `Fill Amount`, `Fill Time`, `Options Regulatory Fees`, `OCC Fees`,
`Total`; retain optional fee/source columns too. Preserve the order/fill layout,
including partial executions; do not collapse rows or add an order total again
as another fill. A cancelled/unfilled order is not an executed trade.

Keep the original history filename if it contains `Margin Account(...)` or
`Cash Account(...)`; it can help account recognition, but confirm ownership in
TAD. A display label or matching last four digits alone is not identity proof.

Positions must contain the seven fields in the [matrix](broker-support.en.md).
Record the **actual snapshot date** yourself if it is not embedded in the file.
Do not choose the upload date merely because it is today. This positions layout
has no independently qualified cash balance; retain separate cash evidence.

## Chase / J.P. Morgan investment accounts

Open the **investment account**, then locate its transaction/activity download.
Choose the complete investment CSV, not a spending/checking/credit-card report.
The supported transaction layout has **31 columns**; representative headers are
`Trade Date`, `Post Date`, `Settlement Date`, `Account Number`, `Account Name`,
`Type`, `Security Type`, `Description`, `Ticker`, `Quantity`, `Price USD`,
`Amount USD`, `Commissions USD`, `Local Currency`. These names are identifiers,
**not a shortened template**: keep the entire original export and one account.

Export the complete investment **Positions** report separately: the supported
layout has **71 columns** and includes `As of`, `Ticker`, `Quantity`, `Asset Class`,
`Pricing Date`, `Base CCY`, `Price`, `Value`, `Cost`, `Unrealized G/L Amt.`.
Do not remove unused columns or total/cash rows.

If the account has earlier closed lots, retain the **realized gain/loss** report
as additional comparison evidence. Its layout includes `Account Number`,
`Acquired Date`, `Sale Date`, `Cost Basis USD`, `Market Cost/Proceeds USD`,
`Total Realized Gain Loss USD`. It is not a transaction replacement, and the
ordinary public upload flow does not automatically apply this reference report.

## E*TRADE

Within the selected investment account, look for **Activity / Transactions** and
its download/export action. Select all activity and an explicit start/end period
where available. Download a **CSV**, not an XLSX or an order-tool export with a
different layout. Keep the title, account block, headers and footer.

The supported title is `Account Activity for <name> -<account> from YYYY-MM-DD to
YYYY-MM-DD`, or the supported `Current Year` / `Prior Year` variant. The activity
table must retain this **exact 13-column sequence**:

```text
Activity/Trade Date,Transaction Date,Settlement Date,Activity Type,Description,Symbol,Cusip,Quantity #,Price $,Amount $,Commission,Category,Note
```

Current Year / Prior Year is not an absolute-year or complete-history guarantee.
The reader uses actual row years; empty/mixed-year annual files cannot establish
a unique annual period. Prefer explicit date-range exports, and inspect TAD's
coverage before confirming an account. Do not edit titles to bypass a rejection.

From **Portfolio / Positions**, choose **All Positions / all securities**, clear
ticker filters and export the complete CSV. Retain the account summary,
`Net Account Value`, `View Summary - All Positions`, the all-security filter
metadata and `Generated at ... ET`. The supported positions table is:

```text
Symbol,Last Price $,Change $,Change %,Quantity,Price Paid $,Day's Gain $,Total Gain $,Total Gain %,Value $
```

Keep CASH and TOTAL rows. TOTAL includes cash; purchasing power is a separate
summary measure, not another cash asset. A report with only displayed/filtered
securities cannot prove the account is otherwise empty.

## If your export does not match

Keep it locally. Re-export the supported report if available. **Do not rename
XLSX to CSV, add placeholder columns, translate headers or impersonate another
broker.** Save a TAD draft if needed and report broker, report type, platform,
app version and sanitized error/header names only. Do not attach account rows,
originals or screenshots containing personal details to public issues.

There is no published generic import template in this release. Supplied
synthetic broker files demonstrate supported layouts; they are not conversion
instructions for unsupported brokers.
