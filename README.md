# TradingAlphaDNA (TAD)

**Understand your strategies, per-stock results and capital efficiency.**

**Under active development · Demo available on request · Planned distribution: shareware**

Pricing and usage terms are not yet announced. The public website, PDFs and screenshots provide a product introduction; a product demo is available on request.

TAD is a local application for reviewing stock and options trading. It brings supported broker exports into account, stock and strategy views, helping individual investors understand their positions, costs and trading results.

This repository presents the product and selected engineering decisions from an AI-assisted software project. The application source remains private. All demonstration screenshots use wholly synthetic data.

## Project highlights

- **Product & financial logic:** Designed stock and options review workflows covering strategy contributions, per-stock P&L, trading costs, and capital efficiency.
- **Data architecture & curation:** Designed extensible, layered data models with user review and traceable corrections to improve data quality and support additional brokers and analyses.
- **AI-native development:** Built and iterated the application, coordinating specialized AI agents for implementation, code review, testing, and release.

## Explore the project

| Start here | What you will find |
| --- | --- |
| [Bilingual product website](https://tradingalphadna.github.io/tad-showcase/) | Browse the product introduction directly; select **中文** for Chinese |
| [English product introduction](TADIntro.en.pdf) | A four-page overview with actual product screens |
| [中文版产品介绍](TADIntro.cn.pdf) | 四页中文介绍：策略表现、个股盈亏与资金效率 |
| [Bilingual HTML introduction](index.html) | Product capabilities and expandable screenshots; select **中文** for Chinese |
| [Engineering case study](docs/engineering-case-study.md) | Architecture, financial correctness, recovery and validation tradeoffs |

The product website opens directly in your browser. GitHub's file view displays the HTML as source. To read it offline, download this repository and open `index.html`; keep the two PDFs beside it for the download links to work.

## The questions TAD helps answer

- **Strategy:** Which traded strategies contributed gains or losses?
- **Stock:** How do stock trades, related options and dividends contribute to one security's result?
- **Capital:** What did a trade cost, how long was capital used, and which return or efficiency measures can be established?

Users can review supported transaction exports from Chase, Moomoo and E*TRADE, inspect holdings and trade chains, and move from a result to the related trades. Support depends on the export format and available transaction history.

![TAD holdings view with wholly synthetic data](assets/screenshots/tad-product-holdings.jpg)

*Actual product screen: remaining positions, costs and unrealized P/L at a saved price. The displayed amounts are artificial demonstration values, not investment performance claims.*

<details>
<summary>More product screens: overview and trade review</summary>

![TAD overview with wholly synthetic data](assets/screenshots/tad-product-overview.jpg)

![TAD trade review with wholly synthetic data](assets/screenshots/tad-product-trades.jpg)

</details>

## Engineering in brief

The application combines a Python backend with `Decimal` financial arithmetic, SQLite revision and application history, and native JavaScript/CSS browser views. It runs locally without a model or API key. AI assisted implementation and review; deterministic rules produce the financial results.

The [engineering case study](docs/engineering-case-study.md) explains the choices behind incomplete-result handling, repeat imports, supported corrections, source-based rebuilding and workspace recovery.

## Current boundaries

Results retain their scope: period realized profit, current unrealized P/L and complete-trade ROI are different measures. Short-Call income may be only one contribution to a covered-call or PMCC strategy; supporting-asset P/L is separate. Missing information stays visible, rather than becoming zero.

The preview does not promise complete historical returns for every strategy or whole-account growth. Prices are saved observations, not live quotes. General statement-PDF extraction, automated trading and a multiuser cloud service are outside the demonstrated scope.

The private application baseline has passed its CI checks. That validation belongs to the private implementation; this presentation repository does not distribute or execute the application test suite.
