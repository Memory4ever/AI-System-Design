# 本窗日期推定与停止点

窗口为 2026-01-19 09:00 ～ 2026-01-20 09:00 北京时间。Submitted 区间只是发现，四组 query JSON 中保留原查询、总数与停止点，不能以提交日替代公开日。

[arXiv 官方 availability](https://info.arxiv.org/help/availability.html) 2026-10-04 实际读 L170–176、L182–193：正文在 scheduled announcement 公开；最终 ID 在 announced 时分配，不能提前得到 ID/DOI。1 月冬令时 Thursday 14EST 至 Friday 14EST 的正常 cohort（01/15 19UTC 至 01/16 19UTC）最早 Sunday 20EST，即 01/19 01UTC/09BJT。Monday 01/19 MLK 延期影响次日终点公告，不能将整个窗口视为零。Moderation 可以迟发，所以只有提交日不构成当窗确认。

对正常 cohort 的具名语义准入/贡献含糊项，DataCite arXiv-owned DOI 已记录最终 arXiv ID，created/registered 01/19 02UTC、当前 state=findable。**最终 ID 不能提前取得**使注册最终 ID 的外部事件提供 announced 已发生的上界，不把 generic 当前 state 外推为历史首次 findable，不把 Updated 或 registered 秒数等同正文公开秒数。报告使用完全落窗的保守范围 **2026-01-19T09:00:00+08:00 ～ 2026-01-19T12:00:00+08:00**（含下界不含上界），所有正常相关注册均早于 03UTC；每项 Submitted/Updated/created/registered 原值在 DATE_POTENTIALS.json。11359 后因 root 校准加入，原值：Submitted 2026-01-16T15:14:04Z；Updated v1 2026-01-19T01:41:26Z；created 2026-01-19T02:34:42.000Z；registered 2026-01-19T02:34:43.000Z；state=findable。没有发现早于 arXiv 正文的原始公开证据；若出现，定点重开家族首公开归属，不扩扫其他日。

[DataCite DOI States](https://support.datacite.org/docs/doi-states) 实际读：Registered state 可以不是公开 metadata，Findable/Registered 可转换。因此通用 current state 不证明历史首公开。[具体 registered 字段定义](https://support.datacite.org/docs/what-is-the-difference-between-the-created-and-registered-date-in-the-datacite-rest-api) 又写 global handle 注册（findable state）及 draft→findable 的日期区别。采用上面的 arXiv final-ID 依据，不需要在这两页定义边界之间伪造正文时刻。DataCite 只支持身份/版本/外部上界，元数据不支持贡献或实验结论。

异常家族：2601.11663、11667、11676、11683（registered 01/21）；14295（01/22）；16225（01/26）；19936（01/29）；2602.06976（02/10）。Submitted 可早于原稿真实 announced，多种 admin/moderation 原因不由作者猜测。当前已尝试官方可见分类月列表、advanced announced_date_first 日筛选（无结果；其原公开索引按年/月，空结果不证零）、abs 版本页、DataCite 官方日期与有界原始搜索。未取得完全落窗的公开上界，不列当窗候选、不评分、不作正面 Evidence/Books/Coverage；外部终态保留，仅在出现该条原始公告/可核同期原文公开证据时重开。

官方当前 cs.CL 月目录 2168 条只是补身份，不带 Jan19 公告组，不作 2168 项工作队列；其他主题由多模态、系统、IR/MA 四组原查询补齐，不拿 CL 代表全部。
