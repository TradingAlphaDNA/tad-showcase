# TAD technical preview — evaluation notice / 测试用途说明

> **Your broker data stays on your computer.** In the current local TAD app, broker files and account data are imported, processed and saved on your own computer—not uploaded to a TAD cloud service. The interface's “Upload” action submits files to the app running on your computer. Sharing anything yourself through public feedback, email or an external service is a separate action.

> **券商数据留在你的电脑上。** 当前本地版 TAD 在你的电脑上导入、处理和保存券商文件与账户数据，不会上传到 TAD 云端。界面中的“上传”是把文件交给本机运行的程序；用户自行通过公开反馈、邮件或外部服务分享资料，是另外的动作。


This preview is provided for local evaluation and feedback. You may download
and run the supplied preview for that purpose. TAD is under active development
and planned as proprietary shareware; future pricing and general distribution
terms are not announced. The full application source remains private. Neither
this download nor the public showcase grants access to that private source or
an open-source license. Bundled third-party components retain their notices.

Ad-hoc signed; NOT notarized. Planned coverage is Apple Silicon M1 and later
M-series on release macOS 15/26/27. VERIFIED scope is the development Mac on
macOS15.2, with constructed cases and independent same-Mac review. Test-user
download/Finder/security-prompt results are pending. Do not downgrade your OS,
disable system protections or overwrite a personal installation to test it.

Begin with synthetic files. No automatic upgrade or automatic trading-data
upload is provided. Financial history and cash qualification have limitations:
reference arithmetic is not full broker reconciliation, and saved prices are
not live quotes. Stop at damaged/malware/hash-mismatch warnings and report them.
Compiled bytecode is inspectable; omission of readable Python files is not a
promise against reverse engineering. SHA checks are not publisher authentication.

本预览供本地试用和反馈，可以为此下载运行。TAD 仍在开发，计划采用专有 shareware
方式提供，未来价格及一般分发条款未公布。程序完整源码保持私有；公开下载和
showcase 均不授予私有源码访问或开源许可，第三方组件保留各自声明。

临时签名，尚未公证。计划范围是 Apple Silicon M1 及后续 M 系列、macOS15/26/27
正式版；已验证范围仅为开发机 macOS15.2、合成案例及同机独立审阅。
测试用户下载、Finder 和安全提示仍待验收。无需降级系统，不关闭系统保护，
不覆盖个人安装。先用合成资料，不自动升级或上传交易资料。
现金核验及历史完整性仍有限制：参考算术不代表券商对账通过，保存报价不是实时行情。
遇到恶意软件、损坏或校验不符提示应停止并反馈。字节码仍可分析，不承诺防逆向。

## Optional personal-data route / 可选个人数据流程

After synthetic checks pass, you may evaluate supported personal files locally in
a separate fresh environment. See [English personal-data guide](personal-data.en.md),
[broker support](broker-support.en.md) and [export checks](broker-export.en.md).
This does not certify complete history or cash, and does not modify the unchanged
download kit or expand its hardware/financial verification. Statements remain
archive-only in the ordinary upload flow. Archived, applied and fully reconciled
are different states. No generic standard-file importer is available yet.

合成检查通过后，可在独立新环境本地试用受支持的个人文件。见[真实数据上手](personal-data.zh.md)、
[支持矩阵](broker-support.zh.md)和[导出检查](broker-export.zh.md)。不代表历史／现金完整，
不修改原下载套件或扩大已验证范围。普通上传流程中 statement 仍仅归档；归档、应用与
完整对账是不同状态，通用标准文件导入尚未提供。
