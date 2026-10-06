# 仅本日日期依据澄清

原始 DataCite Created 与 Registered 保留在 V3_PRIMARY_DATE_FIELDS.json，不将任一字段命名为 publication。采用同身份的 Registered（秒精度扩大一秒为半开上界），不用 Updated 或邻接 ID。公开下界仍由 exact-v1 Submitted 与官方公告表限定：02/12 19:00Z 后至 02/13 19:00Z 的提交最早 Sunday 20:00 ET，即 02/16 01:00Z；早 Submitted 无此下界，继续隔离。

[官方 availability](https://info.arxiv.org/help/availability.html) L171–175：公开由 announcement 流程进行，final arXiv ID/DOI 不能提前提供；L185 给出周末公告表。[官方 DOI FAQ](https://info.arxiv.org/help/doi.html) L159/L168/L174：对应 ID 的 DOI/元数据提交 DataCite，后版更新相同 DOI，canonical DOI 指向最新 abs，因而 registration 可作已公告上界而不能签精确版本正文内容或精确公告时刻。与逐项 Submitted、身份/title 和 Registered 原值联合推定区间，不把元数据字段孤立当发表时间。

本次只修日期说明和报告区间，不重抓 inventory、不恢复全部 revision；不改变 77 确定贡献候选和外部日期终态项。官方 DOI 角色与版本身份分开；首公开早稿信号另定点处理。
