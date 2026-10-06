# Nov17 Date Field Review

作者Carver，实际读回/对读2026-10-04T19:47:21+08:00。初始66个潜力/范围ID的历史核对保留，OPFormer核心关闭后现65项终态首公开保留，逐项见[SCREENING](SCREENING.md)。每项实际打开exact-v1 AB submission history及`datacite-<id>.json`所有v1日期，64份常规成功数据加两份retry共66（另11445关闭的元数据不计）。`2511.12405`、`2511.12614`本日原请求curl28/000/0，单次具名retry200成功，原失败receipt保留。不是以反复全队列重试抹掉失败。

Readonly逐项对读：66个AB v1 Submitted与DataCite `dateType=Submitted,dateInformation=v1`一致，差异0。此检查只确认字段/身份一致，不确认public；原所有v2/v3等日期与当前摘要不能替代v1。除少数ID外Available v1为`2025-11`，Issued多为`2025`；Updated、created、registered均另保留。DataCite是元数据恢复，不是原官宣。

首批五项具体字段在[FIRST_CALIBRATION_READY](FIRST_CALIBRATION_READY.md)。余下原值在各自JSON，均已实际读回。`2511.12405` v1 Submitted `2025-11-16T00:55:28Z`、Updated `2025-11-18T01:48:54Z`、created `2025-11-18T04:24:01.000Z`；`2511.12614` Submitted `2025-11-16T14:19:52Z`、Updated `2025-11-18T02:03:11Z`、created `2025-11-18T04:28:51.000Z`。月份Available不能定位本日。

特殊身份：`2601.08833` Submitted v1 `2025-11-14T06:42:27Z`，Updated `2026-01-15T01:00:03Z`，Available v1 `2026-01`，created `2026-01-15T02:31:57.000Z`。结合官方ID赋号月份的规则，仅可排除它作为11月arXiv首公告；不能排除他处更早首次公开或补造其January精确公开时刻，仍留家族首公开重开线索而非Nov17正面候选。`2511.21702` Submitted Nov16、Updated Dec1，`2511.16691` Submitted Nov16、Updated Nov24，`2511.17575` Submitted Nov14、Updated Nov25，均显示submitted不能归日报。

## 限定结论

本日终点UTC Nov17 01Z。实际Updated/created跨截止，不把跨界上界当窗外证明，也不将Submitted当public。当前official availability说明Sun–Thu20ET及无Fri/Sat；Nov16 20EST换算就是终点，不能据常规schedule补造本日具体announcement精确时刻。

已做：每项AB原历史+DataCite原日期一次，首批必要原作者/官方域[具名搜索恢复](web-named-date-recovery.json)未得到完全落窗的官宣/上下界。搜索有作者新主页和AMD后年公告，只是身份线索，不采用为2025日期；其他潜力未遍历全部作者附件/社媒，不声称查尽全网。没有常规batch不是没有其他原公开。

原66逐项日期核对保留；root必要core校准使2511.12614 OPFormer范围关闭，不再请求其与关闭无关的日期，现65具名首公开终态保留。仅需本ID对应首公开原announcement、作者原始公开发布及其可靠时间，或可证明完全落窗的首公开上下界；若只arxiv月份/Submitted/Updated或跨截止范围，继续隔离。本次最小原日期仍不足以当窗准入，按该ID精确重开，不自动整日/整月重跑或展开实验/owner。root于2026-10-04T20:33:51+08:00实际独立核65项日期类型/原值并通过本日处理边界，见[ROOT_INDEPENDENT_REVIEW](ROOT_INDEPENDENT_REVIEW.md)；作者2026-10-04T20:43:00+08:00同步普通0，不授首公开已定或受阻Coverage通过。

这些日期保留不用于正面Evidence、Books、Coverage/无遗漏或性能/安全保证。若恢复真实窗内事件，可立即准入/评分并继续必要证据，不用日期hold一律回避。
