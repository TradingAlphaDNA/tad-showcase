# TradingAlphaDNA (TAD)

**See what your stock and options trades actually earned.**

Your broker lists transactions and positions. But when a stock holding, option trades and several accounts are involved, the questions get harder: How do the gains and losses add up? How much capital did they use, and for how long?

TAD connects related trading records so investors can review profit and loss, returns and capital use by account, stock and strategy.

[See the product](https://tradingalphadna.github.io/tad-showcase/) · [Request a demo](mailto:hhuang68@gmail.com) · [Engineering case study](docs/engineering-case-study.md)

## Who it is for

Investors who actively manage stocks and options, especially across brokerage accounts or through strategies such as covered calls, cash-secured puts, PMCC and LEAPS. If you already piece together broker records in a spreadsheet to understand your trades, TAD addresses that work.

## You collected the call premium. How did the whole trade perform?

The stock can lose more than the premium earned. A useful review brings the stock and option results into view together, then asks how much capital was committed and for how long.

TAD lets you follow related trades and inspect their contributions. Some strategies currently show only part of the result; those gaps are marked beside the analysis.

![TAD holdings view with wholly synthetic data](assets/screenshots/tad-product-holdings.jpg)

*Actual product screen using artificial demonstration data.*

## Project highlights

- **Product & financial logic:** Designed stock and options review workflows covering strategy contributions, per-stock P&L, trading costs, and capital efficiency.
- **Data architecture & curation:** Designed extensible, layered data models with user review and traceable corrections to improve data quality and support additional brokers and analyses.
- **AI-native development:** Built and iterated the application, coordinating specialized AI agents for implementation, code review, testing, and release.

The project began with a practical trading-review problem and grew into a working local application: broker-data import, trade reconstruction, strategy identification and analysis. The [engineering case study](docs/engineering-case-study.md) explains the product decisions, implementation and validation behind it.

## Explore TAD

- [Bilingual product introduction](https://tradingalphadna.github.io/tad-showcase/) — choose **中文** for Chinese.
- [English PDF](TADIntro.en.pdf) · [中文 PDF](TADIntro.cn.pdf).
- [Latest downloadable presentation](https://github.com/TradingAlphaDNA/tad-showcase/releases/latest) — introduction materials, not an application installer.
- [Engineering case study](docs/engineering-case-study.md).

## How it works

Import supported transaction exports from Chase, moomoo or E*TRADE, review the connected trades and holdings, and explore results by account, stock or strategy. Support varies by export format and available history.

The application runs on your computer without a model or API key. Financial calculations use Python rules and Decimal arithmetic. The interface uses HTML, CSS and JavaScript; SQLite retains application and correction history. AI tools assist development and review.

## Availability and use

**Under active development · [Demo available on request](mailto:hhuang68@gmail.com) · Planned distribution: shareware**

Pricing and usage terms are not yet announced. This public repository contains product presentations, synthetic screenshots and selected engineering explanations. The full application source remains private. Publishing these materials does not release the application as open-source software or grant an application-use license.

## Current limitations

Some historical strategy results are incomplete. A short-call premium alone does not describe the whole CC or PMCC trade. Return and capital-efficiency figures show their calculation basis and period.

Prices are saved observations, not live quotes. General statement-PDF extraction, automated trading and a multiuser cloud service are outside the demonstrated scope.

