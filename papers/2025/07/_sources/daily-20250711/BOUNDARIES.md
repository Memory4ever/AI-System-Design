# 来源与日期边界

作者独立从原始入口重建 2025-07-10T09:00:00+08:00～2025-07-11T09:00:00+08:00。当前不是零事件日报：贡献筛选发现潜在增量，但必要首次公开证据未能完全落窗。不得以提交时间代替公开时刻。

## 日期定点恢复已停止

- arXiv API 四个主题查询（`capture.py`/各 request.json）限定 submission 2025-07-09T18:00Z～07-10T18:00Z，仅恢复通常于 Thursday 20:00 EDT 公告的线索。此范围不是公告完整覆盖，不能覆盖更早提交但延迟公开者或当窗重要修订。
- 官方日期列表 `/list/cs.CL/20250711`、`/2025-07-11`、`/250711` 等不可恢复；月列表只有月级身份范围，不能证明当窗。
- 官方 advanced search 回应 announcement 仅 year/month 粒度（`announce-search.txt`），日期不能造 exact。
- 官方 [Availability](https://info.arxiv.org/help/availability.html) 规定一般公告时间和可因 moderation 延迟；一般规则不是单篇实际公告证据。
- KVFlow `raw-07400.raw` arXivRaw v1 date=Thu,10 Jul2025 03:39:23GMT，仍为提交。OAI `oai-07400.raw` datestamp=2025-07-11 是 last modification，不等于 first announcement。
- DataCite `datacite-07400.raw` Submitted(v1)=07-10T03:39:23Z、Updated(v1)=07-11T00:13:28Z、Available(v1)=2025-07；registered=07-11T01:25:41Z。Synergy `datacite-07562.raw` Updated(v1)=00:24:56Z、registered=01:30:08Z。Updated 字段未获正文公开语义；registration 是窗尾之后，均不能单独证明公开发生于窗内。
- 作者仓库 Synergy 建立于07-09，窗尾之前仅 initial commit，未提供论文初公开正文的窗内时间上界。其他索引搜索只作恢复线索，不替代 primary。
- root FIRST 已指出 OAI 语义错误，作者已纠正，报告不会采用其日期。按 root 指示停止更多日期镜像与无差别全文；保留完整题摘和已经读到的两篇 v1 HTML，不用于 Books。

重开需要单篇官方历史公告（ID/精确版本及公开时间/批次）或作者首次公开正文的带可信时间记录；不能仅给提交时间、月日期、后来的出版状态或当前修改时刻。日期不确定不是贡献排除。

## 当前撤回/纠错信号轻核

2026-10-07 对本次65项保留身份在两轮官方Atom的title/summary/comment作withdraw/retract/errata/correction轻核；唯一词命中为MagiC摘要的self-correction能力评测，不是论文撤回/勘误。无已捕获的明确撤回通知；仅为当前可得metadata核查，不保证完整历史撤回/全部纠错状态，也不替代安全反证项审阅。

## 动态目录停点

- Hunyuan 官方 research 首查为 JavaScript壳；按清单要求已作浏览器核查尝试，30秒超时，工具内核重置。定点官方 publicList API成功返回9条英语记录，均2026，不能证明2025目录完备。
- ZAI research 首查及 `?page=2` 已保存。第二页真实SSR只延伸至2025-12-07且显示“没有更多”，没有恢复目标窗；不能写当窗零命中。
- Seed 原入口只20/242当前记录。定点2025论文API page_token=0空但total=94/has_more=true，非终点；后续有限分页记录见request。
- Meta research HTML被拦截/无正文；补检受搜索索引限制。其他仅当前主页或当前第一页的机构均不据此声称目标历史覆盖通过。

外部保留项不支持“无遗漏”、正面证据或性能/安全保证。所有来源与判断的实际覆盖由本日README自包含说明；此文件保留恢复失败原因，不另授验收状态。
