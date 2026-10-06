# 03/13 首8当前官方事件页标记补核

实际执行2026-10-02T01:22:43+08:00附近（clock UTC17:22:43）。只检查首8当前abs页面header、Comments和页面已有版本身份；没有读取新正文或逐版比较。完整v1题摘已在V3_FIRST_ABSTRACTS.md，后20当前事件页轻量检查记录复用。

| 官方当前页 | 当前header版本与日期字段 | Comments / 影响处置的信号 |
| --- | --- | --- |
| [Cornserve12118](https://arxiv.org/abs/2603.12118) | v2，last revised2026-04-28；v1Submitted03/12 | CAIS2026 Demo、开源和演示链接；未见撤回/勘误说明 |
| [DapQ11564](https://arxiv.org/abs/2603.11564) | v1，Submitted03/12 | 当前页面无Comments行；未见明确撤回/纠错标记 |
| [ET11535](https://arxiv.org/abs/2603.11535) | v1，Submitted03/12 | 当前页面无Comments行；未见明确撤回/纠错标记 |
| [Attention Sinks11487](https://arxiv.org/abs/2603.11487) | v5，last revised2026-04-17；v1Submitted03/12 | Comments仅页数/图数；未见明确撤回/勘误说明。版本号本身不授重要修订 |
| [IndexCache12201](https://arxiv.org/abs/2603.12201) | v1，Submitted03/12 | 当前页面无Comments行；未见明确撤回/纠错标记 |
| [AdaFuse11873](https://arxiv.org/abs/2603.11873) | v1，Submitted03/12 | Comments记AAAI2026 accepted，且官方admin note："substantial text overlap with arXiv:2405.17741"。保留此信号，不据此推撤回或全部贡献重复 |
| [Slow-Fast12038](https://arxiv.org/abs/2603.12038) | v1，Submitted03/12 | 当前页面无Comments行；未见明确撤回/纠错标记 |
| [EBFT12248](https://arxiv.org/abs/2603.12248) | v2，last revised2026-03-16；v1Submitted03/12 | 当前页面无Comments行；未见明确撤回/纠错标记 |

读取路径：web实际打开上述8个不带版本的官方abs；HTTPS定点提取dateline和metatable，并逐项读取。第一次窄提取Comments class未匹配，未用于判断；随后完整metatable提取成功才建立本表。只限当前页面可见说明，不认证全部历史、未公开勘误或版本正文一致。

本次日期裁决未变：26潜在/含糊项仍没有完全落窗上界，未评分、未进入必要正文Evidence或Books。AdaFuse新增原创/重复关系未决：当且仅当日期恢复需要采用该项时，先围绕token-level pre-gating/fused kernel的拟采用增量与2405.17741作必要定点核验；不因admin note无正文证据而删除潜在项，也不把它记贡献已通过。当前无可采用的本窗命题，不展开窗外论文正文/完整版本史。
