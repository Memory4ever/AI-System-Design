# 2026-04-22 arXiv 官方分类与主题补检（作者侧，非日级 Gate）

执行：2026-09-28 约 19:13–19:46 Asia/Shanghai。目标窗口固定为 `[2026-04-21 09:00, 2026-04-22 09:00) Asia/Shanghai`。本记录只补 `SRC-ARXIV` 的约定分类入口与主题检索停点；旧 [515 身份 receipt](../arxiv-owner-replay-20260903/20260422/arxiv-owner-receipt.json) 仅用于身份去重，不是本次官方分类页、首次公开日志或候选分母。

## 日期与方法边界

- [arXiv Availability](https://info.arxiv.org/help/availability.html) 明确 ID 在公告时赋予，可能晚于 submitted；常规周二 20:00 美东公告在夏令时相当于本窗 04-22 08:00 北京时间。月列表与 API 当前 metadata 均不逐篇给出公告秒级时刻。本补检采用此前日内相邻 ID/官方 slot/OAI/版本字段形成的 **`2604.18585`–`2604.19498` 有界待归属 ID 带**，不是宣布带内全部论文已逐篇证明首发。`19503/19533` 等晚字段继续单项 Date Hold；04-23 页面出现的其他线索也不因 submitted 早而自动迁入。
- [12 分类路由](../../../../../docs/RESEARCH_SOURCES.md#arxiv-查哪些分类)按本项目主题作发现，非逐条全文扫描。月列表用 `https://arxiv.org/list/{category}/2026-04?skip={n}&show=2000`，对完整分页的页面主 `<dt>` 条目提取 arXiv ID；标题语义判断复用此前 515 身份标题全览及本次主题查询，不把完整月页宣称为逐篇重新读题摘。大分类逐页读到尾页，小分类一页读完。初次 `show=250` 的相邻页探索虽得到 305 个去重 ID，但发现月目录会把不同条目段串在一起，**全局并非按 ID 单调排序**：例如 `cs.AI` 的 `18724/18874/18946/18982/19089/19354/19398/19459` 在首 2000 条约第 962–993 条，而另一批本 ID 带身份在 `skip=3750/4000`。所以邻页“本带 0”不能当全月停点，已改用下表整月有界分页再按目标 ID 带与主题裁剪。跨列去重并与 receipt 比对。当前月列表可含 cross-list/replacement，标题可受晚版本影响，仅作发现；ID/页位置不是公告日证明。
- 官方 [Atom 查询接口](https://export.arxiv.org/api/query)另按下表主题执行 `search_query=cat:{分类} AND (ti:{词1} OR …) AND submittedDate:[202604200000 TO 202604230000]`，`sortBy=submittedDate&sortOrder=descending`，`start=0/100&max_results=100` 直至报告的 `totalResults`。日期筛子是**发现线索**而非首次公开筛子，先前提交、后公告可能被漏；月列表 ID 带定位与此前 515 身份标题全览共同补此局限。同义词组只覆盖登记的 AI System 主题，不声称整个学科零遗漏。

## 月列表实际分页停点与主题查询

`月页带内` 是该分类在上述临时 ID 带的去重身份数，不是本窗确定首公开数；`主题总量/分页` 是 Atom 查询的全响应量，不是候选数。主题响应经 ID 带过滤后与旧 receipt 比对，均无新身份。下列 12 分类完整 04 月目录的 ID 带并集共有 **357 个跨类去重 ID**，**357/357 均在旧 receipt**；这只说明本次检索未新增身份，不说明 515 全部官方首发。整月分页是廉价身份定位，标题判断复用旧库存全览与本次主题查询，**未**把各分类全部条目逐篇读题摘或全文。

| 分类 | 官方月列表实际 `skip/show` 与总条目停点 | 月页带内 | 主题标题词（`ti:`，用 OR） | Atom 总量/分页；带内身份 |
| --- | --- | ---: | --- | --- |
| `cs.CL` | `0/2000`、`2000/2000`（尾页 532；全 2532） | 78 | `"language model"`, transformer, reasoning, agent, alignment | 136；`0/100`、`100/100`；31 |
| `cs.LG` | `0/2000`、`2000/2000`（尾页 1898；全 3898） | 108 | `"language model"`, transformer, MoE, `"foundation model"`, `"reinforcement learning"` | 69；`0/100`；13 |
| `cs.DC` | `0/2000`（全 388） | 18 | `"language model"`, GPU, inference, training, distributed | 17；`0/100`；4 |
| `cs.AI` | `0/2000`、`2000/2000`、`4000/2000`（尾页 1030；全 5030） | 149 | agent, `"language model"`, reasoning, `"tool use"`, planning | 196；`0/100`、`100/100`；44 |
| `cs.CV` | `0/2000`、`2000/2000`（尾页 1262；全 3262） | 88 | `"vision language"`, video, diffusion, `"world model"`, multimodal | 95；`0/100`；16 |
| `cs.RO` | `0/2000`（全 976） | 25 | `"vision language action"`, VLA, robot, `"world model"` | 40；`0/100`；6 |
| `cs.AR` | `0/2000`（全 227） | 7 | accelerator, GPU, kernel, inference | 6；`0/100`；1 |
| `cs.PL` | `0/2000`（全 138） | 5 | compiler, kernel, `"language model"`, agent | 3；`0/100`；0 |
| `cs.OS` | `0/2000`（全 37） | 2 | `"language model"`, GPU, runtime, scheduler | 3；`0/100`；1 |
| `cs.PF` | `0/2000`（全 69） | 0 | `"language model"`, GPU, inference, performance | 2；`0/100`；0 |
| `cs.IR` | `0/2000`（全 512） | 9 | RAG, retrieval, `"language model"`, memory | 25；`0/100`；3 |
| `cs.MA` | `0/2000`（全 348） | 8 | agent, `"language model"`, coordination, multiagent | 22；`0/100`；6 |

示例可复查 URL：[cs.AI 首页段](https://arxiv.org/list/cs.AI/2026-04?skip=0&show=2000)、[cs.AI 中页段](https://arxiv.org/list/cs.AI/2026-04?skip=2000&show=2000)、[cs.AI 尾页段](https://arxiv.org/list/cs.AI/2026-04?skip=4000&show=2000)；其余 URL 按表中分类和 `skip/show` 原样代入，不另造入口。Atom 示例：[cs.CL 主题第一页](https://export.arxiv.org/api/query?search_query=cat%3Acs.CL%20AND%20%28ti%3A%22language%20model%22%20OR%20ti%3Atransformer%20OR%20ti%3Areasoning%20OR%20ti%3Aagent%20OR%20ti%3Aalignment%29%20AND%20submittedDate%3A%5B202604200000%20TO%20202604230000%5D&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending)。

本次 12 分类月页/主题查询的 ID 带内匹配均已落在 515 旧身份库存，因此**没有新身份需要加入当前 170 份已读题摘的筛选队列**。这不等于对 515 份全文、全部修订、所有未命中的新命名机制或首公开时刻完成审计；现有 99/69/2 仍依各家族题摘/必要原文与独立日级 Gate 决定。此项补检与先前作者侧 170 题摘是不同层：来源发现不证明准入，旧 receipt 状态也不反向覆盖 V3 的具名贡献裁决。

## 与正式候选的反向对账

再把正式表的 99 个工作候选逐 ID 与上述 **357 个整月月页带内身份**相交，92 个位于这些官方分类目录，7 个不在；所以“357/357 已见旧 receipt”绝不等于“99/99 均由固定 12 分类页发现”。对后 7 个用官方 [Atom `id_list` 定点身份入口](https://export.arxiv.org/api/query?id_list=2604.19012,2604.19031,2604.19090,2604.19305,2604.19330,2604.19438,2604.19461&start=0&max_results=7)核其身份/当前分类；该接口当前版本/分类不是 exact-v1 方法证据，也不是首次公开时间证据。逐篇 exact-v1 方法与受限评价另在[本日证据笔记](./V3_EVIDENCE_REVIEW.md)和日报 §4。

- 初次 250 条抽取页段未覆盖的 8 个 `cs.AI` primary：`18724`、`18874`、`18946`、`18982`、`19089`、`19354`、`19398`、`19459`，现均由 `cs.AI` `skip=0&show=2000` 主条目找回。`18697` 虽 primary 为 `cs.CR`，也在固定分类的 `cs.CL/cs.LG` cross-list 页出现；故这 9 个不再称月页未命中。
- 最终仍不在固定 12 分类月页、按具名线索定点进入的 7 个：`19012`、`19031`、`19090`、`19438`、`19461`（primary `cs.CR`）、`19305`（`cs.SE`）、`19330`（`eess.AS`）。其他分类线索不改写 12 个常规分类的入口约束；它们已分别使用官方单篇来源审阅，不要求为此无界扫 `cs.CR/cs.SE/eess.AS` 全月。

上述反向对账确认 99 个候选中有 92 个由本次固定分类目录命中，另 7 个通过具名单篇线索保留；它不能证明所有相关首次公开事件均被当前月页登记、这 7 篇的逐篇首发秒级时刻或当前 API 版本等于当窗 v1。来源独立语义 Gate 仍需检查这些限定、实际查询停点与日期联合归属。
