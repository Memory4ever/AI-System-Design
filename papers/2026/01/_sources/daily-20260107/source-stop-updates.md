# Jan07 有限原入口恢复与停止

本日 older-fresh.jsonl 四次 `lastUpdatedDate:[...]` 探针均timeout/429，仅失败探索，不是有效零返回。实际重开官方 API User Manual https://info.arxiv.org/help/api/user-manual.html §3.1.1.3（L327）及查询字段说明（L672–687）：lastUpdatedDate是排序参数，文档仅提供submittedDate日期过滤；不能把该未支持过滤语法视为旧论文修订查漏已执行。本日公开revision/mirror历史仍安全隔离：需要原当窗公告/可核实原事件列表才能定点恢复；不扩大到所有旧版本，不授召回或无遗漏。接口连续调用建议间隔3秒；不再快速重试这四探针。

sources-fresh.jsonl补首轮未恢复区域：MiMo tail Paper8可见日期January8→October21，Blog15无日期/More；ZAI release确有2026-01-14→2025-12-22。此前首屏动画/regex空不是零事件证据。

Seed fresh compact四切片 seed-date-slices-fresh.jsonl请求count20却locale visible19/18/14/18，分别total82/94/19/45；API返回原数不补齐到20，pinned/非pinned分别记录。type2-2026虽next空/has_morefalse，14≠19，不能据此授完整历史覆盖。仅日期metadata，不读全年题摘。

Google官方 pubs当前以年为字段、首15非日级目录；fresh官方域查询 `January 6 2026 research` 返回原blog January目录，实际重开 https://research.google/blog/2026/01/ L180–188共9 date-label，最早Jan12，不扩各篇AB；当前月份目录非所有研究/首公开正文。此前较窄Jan6查询0只是那次补检，不应写成所有官方搜索空。DeepMind publications page1/30/9pages currentJan9→Dec3有限桥接保留。Research日级publication限制仍精确隔离，不拿Blog补检证明全机构无事件。

Meta/Qwen/Kimi官方域本日initial Jan6/2026定向search空只搜索限制；HunyuanfreshPOST九条最早Feb3没有Jan07历史恢复，不把total9当本窗零。其余源逐行边界见README和official-date-slices原字段。arXiv窄主题136/14/9 metadata-only start0/max200（narrow-fresh.jsonl），不是逐项关闭队列；原185宽入口cap已停止，新主线题摘仅由具体标题可能增量定点恢复。

official arXiv availability https://info.arxiv.org/help/availability.html L170–189 + holiday https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/ 原公告实际重开：Jan2Fri14～Jan5Mon14ET最早Jan5Mon20ET=Jan6T01Z；ID首次announcement分配/不得backdated与具体DataCite registered upper合取首次arxiv公开区间。registered或Updated均不独立=public时刻。date-probe-specific 43具名日期探针是已存在本窗线索的metadata恢复，非43准入或完整题摘队列；02456 earliest可见UpdatedJan7T01:02:02/registeredJan7T02:33:59是相邻窗线索，不能用SubmittedJan5拉入。Tarragon/Muon/01887/01896/02232修订的真实Updated下界落Jan7或Jan8，不按Jan6/7 Submitted授本窗修订。
