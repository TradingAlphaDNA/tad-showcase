# TAD — public technical preview for your Mac

> **Your broker data stays on your computer.** In the current local TAD app, broker files and account data are imported, processed and saved on your own computer—not uploaded to a TAD cloud service. The interface's “Upload” action submits files to the app running on your computer. Sharing anything yourself through public feedback, email or an external service is a separate action.


**Two separate paths:** this page and the alpha.2 download kit describe synthetic acceptance. After that passes, optional local personal-data evaluation is described in the [personal-data guide](personal-data.en.md). Check the [supported broker files](broker-support.en.md) and [export instructions](broker-export.en.md) first. Do not mix synthetic and personal accounts in the same environment. The synthetic-only instructions below remain applicable to the acceptance exercise; they are not a claim that the app rejects supported real files.


Distribution: **1.1.0-alpha.2 public technical preview**. Bundled application: **1.1.0-alpha.2**, rebuilt with the accepted Standard CSV import and shared-core changes. Installation on a test user's Mac has NOT yet been verified.

Download: https://github.com/TradingAlphaDNA/tad-showcase/releases/tag/tad-test-v1.1.0-alpha.2
Feedback: https://github.com/TradingAlphaDNA/tad-showcase/issues/new?template=technical-preview.yml
The application is 1.1.0-alpha.2, Apple Silicon arm64, tested
on the development Mac running macOS 15.2. The initial COMPATIBILITY TARGET is
Apple Silicon M1 and later M-series Macs with release versions of macOS 15, 26 or 27. This is a target, not a certification
of every chip/OS combination or a measured market-share claim. Only the
development Mac's macOS 15.2 is verified so far; keep your own supported system
and current security updates. Do not downgrade to 15.2 for this test.
Intel and older macOS versions are outside the initial target. TAD is under development, planned shareware;
the application source stays private. This kit contains artificial data only.

## Before starting

- Use the TEST USER'S own Mac in the target range and a fresh personal environment;
  the project owner does not need to provide a second computer. Record the
  chip, exact macOS version, tester, date and transfer method in ACCEPTANCE.en.md.
- No private repository, Git, Python, Node, Xcode, model account or API key is
  required. A browser and the standard macOS Terminal/Finder are sufficient.
- Keep the existing TAD installation and all personal data/settings untouched.
  Do not use real broker files, a personal backup or any keys for this test.
- The installer preserves a free-space reserve of at least about 10 GiB and
  needs additional working room. Do not assume the small ZIP size is sufficient.
- Default local port is 8888. Existing ports/processes are left untouched.
- This app is ad-hoc signed and NOT notarized. If macOS blocks Setup, the inner
  executable, Start or Stop, record the exact alert and stop that test step.
  Do not disable Gatekeeper, remove quarantine attributes, use sudo or ignore a
  damaged/malware/hash warning. A system-provided, single-app exception is the
  tester's own decision after checking the source; it is not guaranteed or an
  unattended-agent step. See https://support.apple.com/en-us/102445 .

## 1. Download, check and open the application

On the Release page, choose **TAD-1.1.0-alpha.2-macOS-arm64-test-kit.zip**. GitHub's automatic Source code ZIP/TAR contains showcase documents, not the application. The download already includes constructed files and an acceptance sheet. Unzip it, then continue below.

Unzip the outer kit. Open START-HERE.html for the English/Chinese overview.
The reviewed application ZIP is in application/. Its SHA256 is:

`4a0c44f748802302223ca149672cf223e237f804518fdfec2d27fa8259400cb9`

Optional operator check: open Terminal, type `cd `, drag the extracted kit folder
onto it and press Return; run `shasum -a 256 -c SHA256SUMS`. All entries should
say OK. A mismatch means stop; SHA is identity checking, not Apple notarization.

Extract the inner application ZIP. The ordinary first-user path is to double-click
Setup.command. Its default destination is ~/Applications/TAD-Test. If it already
exists, do not overwrite it or assume rerunning Setup upgrades the program.

For this first public test, use the default fresh ~/Applications/TAD-Test.
If that destination already exists or is incomplete, keep it intact. To choose a
NEW folder, drag Setup.command into Terminal and append
` --destination "$HOME/Applications/TAD-Preview-New"` before pressing Return.
If port 8888 is occupied, use ` --port 8889` with an unused port. No JSON editing
is needed. Record any command-line fallback separately; it does NOT prove Finder
double-click worked.

In the created personal folder, double-click Start.command. Wait for readiness;
the browser should open automatically. If it does not, record that failure and
use the printed URL only as a diagnostic fallback. The default is
http://127.0.0.1:8888 . Expect an empty upload screen and 0 accounts.
Never initialize under the downloaded application folder or move an initialized
personal folder; its independent data/configuration are bound to their paths.

## 2. Moomoo first import — complete the happy path first

All dates here are historical TEST dates in 2026, not today.

- Folder: cases/moomoo/01-initial/ . Select its activity and positions CSVs in
  Upload files, then Upload and read. Keep the activity filename unchanged:
  History-Margin Account(0001).csv carries the constructed source identity.
- In each file's View / review, confirm broker Moomoo and the correct file kind.
  The positions file's Actual position date is 2026-01-06. If changing that field
  causes rereading, save first, inspect the refreshed preview, then confirm owner.
- Account association: New account (confirm identity first). Name Synthetic
  Moomoo, last four digits 0001, account type Margin. Use the same values on both
  files. Check the ownership box and Save review. Archiving is optional.
- Select Use in this update for those TWO files only, then Review selected files.
  In the resulting account wizard, confirm these opening facts:
  account/source identity 0001; opening date 2026-01-01; cash USD 10,000;
  opening security positions EMPTY; end date 2026-01-06. Confirm complete opening
  positions and complete activity because the supplied constructed history is
  complete. Do not copy current positions back into the opening section.
- Review the summary and explicitly Confirm and apply. A document status such
  as Archived or Pending update is not the final applied account result.

Expected initial positions: SYN stock +10; SYN280121C50000 +1;
SYN270115C100000 -1; SYN270219C100000 -1. Initial saved unrealized total is
USD 370, realized profit 0, cash arithmetic 8,400. The latest prices are TEST
observations on 2026-01-06, not live quotes. These CSVs contain no cash snapshot
row for Moomoo; its cash number is an arithmetic reference from the opening and
trades, not independent broker cash evidence.

## 3. Moomoo update, duplicate and restart

Upload both files from cases/moomoo/02-update/; choose the existing Synthetic
Moomoo account and positions date 2026-01-07. Review and confirm ownership.
The cumulative activity contains 4 existing rows and 1 new sale: four SYN shares
sold at USD 12. Preview must not apply; Confirm and apply performs the update.

Compare in Analysis with all strategies and this account selected, realized
period 2026 and the current saved date shown. After update:

- SYN stock +6, remaining stock cost USD 60; the three option quantities stay
  +1, -1, -1. Stock sale cost 40, proceeds 48, realized profit USD 8.
- Saved stock unrealized USD 12, long-call unrealized 200, short calls 100 and 50;
  saved unrealized total USD 362. Realized plus those saved estimates is 370.
- Cash arithmetic: 10,000 - 100 - 2,000 + 300 + 200 + 48 = USD 8,448.
  Cash plus saved net security market value 1,922 = net assets 10,370.
- One long call cannot be counted as TWO independent long calls fully supporting
  both shorts. The ten/six stock shares also cannot become 100 shares. Partial
  support or evidence qualifications must stay visible. Do not force a pairing.
- Check the visible scopes of return/capital-efficiency metrics. Do not compare
  a matched subset rate with whole-account profit or add shared support costs twice.

Try the same cumulative activity again. It must report no additional new trade;
do not create a duplicate account. If a second application is offered, the held
quantities and results must stay unchanged. Archive the sample PDF, leave a new
update draft pending and change the account display setting. Stop and restart;
then restart the Mac and start again. Confirm all saved items/settings remain.
Repeat Setup only against its OWN completed environment; it must preserve its
version/config/port/data rather than silently upgrade. Do not test overwriting a
personal folder. Record a busy-port or incomplete-target refusal if encountered.

## 4. Chase and E*TRADE cases

Repeat the same upload/review/apply/update sequence, one broker at a time.
Both start with cash USD 1,000 and no security positions on 2026-01-01.

| Field | Chase | E*TRADE |
| --- | --- | --- |
| Name | Synthetic Chase | Synthetic ETRADE Roth |
| Identity / last four | 0000 | 0000 |
| Type | Brokerage | Roth IRA |
| Initial folder | cases/chase/01-initial/ | cases/etrade/01-initial/ |
| Initial positions/end date | 2026-01-02 | 2026-01-02 |
| Update folder | cases/chase/02-update/ | cases/etrade/02-update/ |
| Update positions/end date | 2026-01-07 | 2026-01-07 |

Initial: buy 10 SYN at 2; stock cost/value 20, cash 980, unrealized/realized 0.
Update: one existing buy plus one new sale of 4 at 3. Expected stock 6, cost 12,
realized 4, saved unrealized 6, CASH 992, net assets 1,010. E*TRADE deliberately
reports Cash Purchasing Power 9,999: it is NOT the CASH balance. TOTAL already
includes cash; do not add CASH to that total again. Combined all-account figures
after all three updates: realized 16, saved unrealized 374, cash arithmetic 10,432,
saved net assets 12,390. Use per-account checks first and show all three accounts
before comparing aggregate figures.

## 5. Archive, evidence and limitations

The valid PDF cases/archive-only/SYNTHETIC-statement.pdf is for document archival
only. Rename it meaningfully, reopen/download it and check it survived restart.
It must not create trades, alter cash or be treated as opening-balance evidence.

Cash arithmetic is separate from reconciliation qualification. This kit confirms
opening values manually and does not independently prove complete posted-cash or
available-cash coverage. Cash may remain partial/pending, with qualified ending
balance unavailable; that is not a requirement to display 8,448/992 as verified
cash. Retained historical opening proofs have a separate known limitation after
updates. Record each reason/impact; never fill unknowns with zero or mark cash
reconciled just because arithmetic matches. Saved prices and synthetic results
do not certify real broker history.

Complete ACCEPTANCE.en.md with actual outcomes: pass, blocked, known limitation,
not run, and sanitized screenshots. Keep local technical evidence separate from
public feedback. Do not send originals, account numbers, logs with personal paths,
backups, passwords or keys. The kit does not automatically upload your trading data. Submit feedback yourself using the public feedback link, after removing personal information.

This preview is published so users can report their actual download, security prompts and installation results. Those results are still pending: it does not certify Apple notarization, Intel, every target OS, automated upgrade or real-data restore. Publishing it does not upgrade your existing installation. Start with the supplied synthetic cases; using your own records later is optional and remains local. Read TESTING-NOTICE.md for evaluation scope.

Compatibility references (hardware/OS eligibility, not TAD certification):
https://support.apple.com/en-us/120282 , https://support.apple.com/en-us/122867 ,
https://support.apple.com/en-us/109033 . First collect an end-to-end result on an
available test user's machine; use M1/M2 and the lower target OS to probe the lower
boundary when available, then add newer-OS results. Do not delay all testing while
waiting for a specific chip, and do not require users to change their installed OS.

[Standard CSV guide and two templates](standard-import.en.md) — alpha.2 adds converted activity and positions/CASH. Earlier alpha.1 is incompatible.
