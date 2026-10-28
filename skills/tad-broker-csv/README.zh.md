# TAD 券商 CSV 转换助手 · 0.1.0

[English](README.en.md) · [两份精确模板及中英文字段指南](assets/standard-import/index.html)

帮助支持本地文件和脚本的 AI 助手，把已明确含义的美元股票、标准美股期权数据转换成 TAD 标准 CSV。本次完整流程使用 TAD **1.1.0-alpha.3 或后续兼容版本**。标准 CSV 从 alpha.2 提供，但 alpha.2/r1 存在账户组合限制；旧 alpha.1 不支持。不是“任意券商文件无条件自动导入”；原生 Connector 已支持的原件优先走原生入口。

## 安装或直接读取

从 showcase 的转换助手配套 Release 下载 `TAD-broker-csv-skill-v0.1.0.zip`，核对 SHA256SUMS 后解压。完整 `tad-broker-csv` 文件夹包含 skill、本地辅助工具源码、精确模板与合成示例，不含私有 TAD 应用源码。

Codex 用户可把完整文件夹放入自己配置的 skills 目录（一般为 `~/.codex/skills/`），新建聊天后调用 `$tad-broker-csv`。如果已有同名目录，请保留旧版并明确升级，不混合覆盖部分文件。也可以不全局安装，直接让有文件权限的助手读取：“请读 /绝对路径/tad-broker-csv/SKILL.md，检查我的 CSV，准备映射，并列出阻止转换的问题。”

实际验收范围以 Release 记录为准。直接读取 skill、执行本地脚本和自动发现 skill 是不同能力；其他 AI 应用需使用其支持的安装或读取方式，不保证所有宿主都能安装执行。纯文本 AI 无法验证实际原文件字节或运行工具。

**辅助工具需要用户另备 Python3.10+，只用标准库，无需 pip 依赖。** 这与 TAD Mac 安装包不同：TAD 应用已包含自己的运行时，不要求 Python、Git、Node、模型账户或 API key。本工具是可移植 Python，但本次实际操作系统和版本覆盖以 Mac 验收记录为准，不代表提供 Windows 应用支持。

## 先跑全合成示例

终端进入解压后的 skill 文件夹。以下输出目录必须尚不存在：

```bash
python3 scripts/convert.py inspect examples/custom-transactions.csv
python3 scripts/convert.py convert examples/custom-transactions.csv --profile profiles/custom-transactions.json --output /tmp/tad-custom-activity-new
python3 scripts/convert.py convert examples/custom-positions.csv --profile profiles/custom-positions.json --output /tmp/tad-custom-positions-new
```

核对 `report.md`、`report.json`。预期：买10股 SYN、单价2、净现金−20.50、报告费用0.50；卖4股、单价3、净现金11.50、费用0.50。剩6股、毛已实现收益4、已知交易现金变化−9；独立 book_cash 快照991不是另一笔转账。成本12、市值18、浮盈6由示例原件明确提供，不由工具补算。缺期初证明或完整费用证据时，TAD 会保留适用范围和待核状态。

每个目录会按账户生成 `TAD.transactions.<id>.csv` 或 `TAD.positions.<id>.csv`，靠精确字段而非文件名识别。可运行 `python3 scripts/convert.py validate /绝对路径/输出.csv --role transactions`（持仓用 positions）。退出0仅代表辅助预检，退出2表示阻止。**任一记录待核时，该输入整次不生成可导入 CSV**；已映射部分也不会被包装成完整结果。报告包含原始行定位、来源值和具体问题。原件不改，已有输出目录不覆盖。

## 转换自己的券商文件

让助手读取[映射规范](references/mapping.md)、精确模板和本地原件，确认实际券商、稳定账户引用、单位、净额/毛额/费用、日期时区、成本口径、期初/当前快照范围，再另存有版本的映射 JSON。六份券商映射是**狭窄的合成回归示例**，不能直接用于所有真实导出；尤其 E*TRADE/Moomoo 示例中的账户和日期是明确构造值，不要原样用于个人文件。

缺失不等于0。不猜期权条款、不假定零费用/零成本、不把订单汇总和逐笔成交重复计入、不由快照倒推虚构交易、不把购买力当现金。Journal、过期、行权、指派在 helper0.1 中明确阻止，即使 TAD 标准或原生路径能处理有证据的事件；需要补清来源含义或走适当原生路径。不同但重叠的原文件没有稳定成交ID时，仍需 TAD 核对，不能制造ID绕过去重。

报告清楚后，进入兼容 TAD，选 Standard CSV 或本机文档入口，核对账户、日期与待核项，确认完整期初持仓和账面现金，再明确应用。**已归档＝保存文件；待更新＝尚未应用；已应用不等于全部对账完成。** 不新建重复账户绕过原生/转换来源冲突。

## 兼容范围与实测边界

旧 alpha.2-r1 在同券商、同名但完整账户引用不同的场景中实测出现 `recovery_accounts_overlap`。请使用配套 alpha.3 测试版的修复身份路径，不通过改券商或账户身份绕过旧包问题。同名不同账户、旧身份保留、更新、重启及合成恢复的验收证据随转换助手发布记录。本辅助工具不迁移个人安装。

已在 Codex 中直接读取 skill 并用 Python3.10 前向验证合成示例及 Journal 反例；自动全局发现/安装和其他 AI 宿主尚未实测。公共核心等价测试使用 Python3.12；辅助工具在 Python3.10/3.12、macOS15.2 Apple Silicon 运行验证。

## 隐私与许可

工具本机运行，无网络请求、遥测或 API key，不自动导入或应用 TAD。报告含来源内容，不要公开发布。TAD 的本机导入不会发送券商数据到 TAD 云端；把 CSV 交给外部云端 AI 是用户另行选择的数据传输，不会因为用了 skill 就变成本地处理。保留原件与备份，反馈只用合成或脱敏样例。

新编写 skill、辅助工具和合成映射采用随附 MIT 许可；TAD 应用源码仍为私有专有内容，不授予应用许可。标准模板与字段指南的授权和署名见 LICENSE.txt。该工具不认证券商数据准确性，也不提供交易建议。
