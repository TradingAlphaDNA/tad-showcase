# 导出正确的券商文件

[English](broker-export.en.md) · [支持矩阵](broker-support.zh.md) · [导入自己的数据](personal-data.zh.md)

本指南说明**本版 TAD 所需报表及导出结果检查**。券商菜单随地区、账户、界面
版本变化；尚未逐一登录验证所有测试者的点击路径。以下菜单名是查找提示，不是
当前界面承诺；不同版本请询问券商自身支持。下载菜单写着 CSV 不等于兼容 TAD。

## 导出前

1. 一次选择**一个投资账户**，本地记录账户类型和区间；退休、普通账户分别导出。
2. 下载英文表头原始 CSV，保留另一份本地原件，不用表格软件编辑后覆盖。
3. 选择目标区间全部活动，保留报表可提供的费用、分红、利息和转账；不只导出
   单个 ticker、盈利交易或已平仓记录。
4. 单独导出带真实日期的完整最新持仓；最新持仓不等于历史流水，也不是期初余额。
5. 保留支持期初边界的早期原件／statement；缺历史应明确待核，不编造期初交易。

## Moomoo

在桌面端交易账户查找订单／成交的 **History／历史**，选择账户和区间后导出；
另在该账户的 **Positions／持仓** 导出当前仓位。不要用行情／自选股导出或
PDF statement 代替交易 CSV。

支持的历史结构包含 `Side`、`Symbol`、`Name`、`Order Price`、`Order Qty`、
`Status`、`Filled@Avg Price`、`Order Time`、`Order Type`、`Fill Qty`、`Fill Price`、
`Fill Amount`、`Fill Time`、`Options Regulatory Fees`、`OCC Fees`、`Total`；
同时保留可选费用／来源列。保留订单和部分成交层次，不合并原始行，也不把订单
合计再当一笔成交；撤单／未成交订单不应成为交易。

若历史文件原名含 `Margin Account(...)` 或 `Cash Account(...)`，保留原名有助识别，
仍需在 TAD 确认归属。显示名称或仅末四位相同，不足以证明同一账户。

持仓需包含[矩阵](broker-support.zh.md)列出的七个字段。若文件未内嵌日期，记录
**实际仓位日期**；不要直接填今天的上传日期。该格式不能独立证明现金，另保留
现金依据。

## Chase／J.P. Morgan 投资账户

进入**投资账户**，查找交易／活动记录下载，选择完整投资 CSV，不使用消费统计、
支票或信用卡报表。支持的交易结构共 **31 列**，代表性表头包括 `Trade Date`、
`Post Date`、`Settlement Date`、`Account Number`、`Account Name`、`Type`、
`Security Type`、`Description`、`Ticker`、`Quantity`、`Price USD`、`Amount USD`、
`Commissions USD`、`Local Currency`。这些只用于识别，**不是精简模板**；需保留
完整原件，一个文件对应一个账户。

另导出完整投资 **Positions** 报表：支持结构共 **71 列**，包含 `As of`、`Ticker`、
`Quantity`、`Asset Class`、`Pricing Date`、`Base CCY`、`Price`、`Value`、`Cost`、
`Unrealized G/L Amt.`；不删除暂时无用列、合计或现金行。

有早期已平仓批次时，保留 **realized gain/loss／已实现损益** 报表作补充核对依据。
其结构包含 `Account Number`、`Acquired Date`、`Sale Date`、`Cost Basis USD`、
`Market Cost/Proceeds USD`、`Total Realized Gain Loss USD`。它不能替代交易流水，
普通公开上传流程也不会自动应用这类参考报表。

## E*TRADE

在所选投资账户查找 **Activity／Transactions** 及下载动作，选择全部活动，
有条件时指定明确起止日期。下载 **CSV**，不是 XLSX 或另一个结构的订单工具导出；
保留标题、账户块、表头和尾注。

支持标题为 `Account Activity for <name> -<account> from YYYY-MM-DD to YYYY-MM-DD`，
或支持的 `Current Year`／`Prior Year` 版本；交易表必须保留以下 **13 列顺序**：

```text
Activity/Trade Date,Transaction Date,Settlement Date,Activity Type,Description,Symbol,Cusip,Quantity #,Price $,Amount $,Commission,Category,Note
```

Current Year／Prior Year 不证明绝对年份或全年完整；Reader 根据实际行确定年份，
空年度文件／跨年混合无法确认唯一年度。优先明确日期区间，确认账户前检查 TAD
显示的覆盖范围；不要改标题绕过拒绝。

在 **Portfolio／Positions** 选择 **All Positions／所有证券**，清除 ticker 筛选后
导出完整 CSV，保留账户汇总、`Net Account Value`、`View Summary - All Positions`、
全证券筛选信息及 `Generated at ... ET`。支持的持仓表头为：

```text
Symbol,Last Price $,Change $,Change %,Quantity,Price Paid $,Day's Gain $,Total Gain $,Total Gain %,Value $
```

保留 CASH、TOTAL；TOTAL 已含现金，购买力是不同汇总指标，不是另一份现金资产。
只含筛选证券的报表不能证明账户其余仓位为空。

## 文件对不上时怎么办？

本地保留原件，如有则重新导出支持报表。**不把 XLSX 改后缀成 CSV，不填假列、
不翻译表头、不伪装其他券商。** 必要时保存 TAD 草稿；公开反馈只提供券商、报表
类型、平台、应用版本及脱敏错误／表头名，不附账户行、原件或含私人信息截图。

本版没有公开通用导入模板。套件合成 CSV 是已支持券商格式示例，不是其他券商
数据的转换指南。
