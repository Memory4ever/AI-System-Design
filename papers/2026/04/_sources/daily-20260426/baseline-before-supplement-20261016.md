# Daily Research — 2026-04-26

**规范：** V3
**窗口：** 2026-04-25T09:00:00+08:00 ～ 2026-04-26T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-28T20:51:01+08:00

## 1. 结论

本窗已对十四个每日来源逐项恢复可见目录的日期邻界或写明无法取得的历史入口；尚无能以原始首公开链确认落窗的贡献候选，因此当前确定候选、完成证据审阅和 Books 新增均为 0。这个结论不等于本窗互联网或机构研究零发布。[Seed MegaScale-Omni](https://seed.bytedance.com/en/public_papers/megascale-omni-a-hyper-scale-workload-resilient-system-for-multimodal-llm-training-in-production) 的官网目录时间落窗；[DeepMind ProEval](https://deepmind.google/research/publications/238239/) 的官网日级日期与本窗相交。两者题摘都有与当前主线相关的具体机制线索，但“现时目录日期／arXiv 提交／DOI 建立”均不足以确认当时公众可读的原始正文，故只保留两项具名日期隔离，不评分、不倒灌后来的全文或写入 Books。

本窗北京时间周六 09:00 至周日 09:00 没有 arXiv 官方正常公告槽；这只约束常规 arXiv 公告，不替代机构先发项目页、异常公告或版本事件的检查。旧 V2.1 报告的“DataCite created 0 条／Complete”不是 V3 证据，旧稿已保存在[本日旧档](../_sources/daily-20260426/V2_1_README_BEFORE_V3.md)。本轮实际入口、原始字段及有界停止理由见[作者续跑记录](../_sources/daily-20260426/V3_REOPEN_NOTES.md)。来源范围、两项日期隔离与零确定候选分母已通过[非作者日级语义 Gate](../_sources/daily-20260426/V3_ROOT_DAILY_GATE_20260426.md)；完成不表示受阻子入口已覆盖或两篇论文已获正面证实。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方 News RSS](https://openai.com/news/rss.xml) 的邻近 pubDate 为 04/25T00Z（本窗前）和 04/26T16Z（本窗后），可见 News 层无本窗项 | 受阻 | RSS 不能代替[Research 历史入口](https://openai.com/research/)；缺本窗可复核的 Research 列表或分页停点 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 可见 publishedOn 邻界 04/22T14:12/14:27Z → 04/29T20:26Z，当前目录跨过本窗 | 已检查 | 仅限当前可见官方 Research 目录，不证明未列作者稿不存在 |
| SRC-GOOGLE-AI | [Google Research 四月 Blog](https://research.google/blog/2026/04/) 可见 04/22→04/29；[DeepMind Publications](https://deepmind.google/research/publications/) 可见 04/23→04/25 ProEval→05/06；已核 ProEval 原始页与所链 arXiv 提交身份 | 受阻 | ProEval 04/25 仅日级可信，首次全文时刻未证；Google Research Publications 与 DeepMind Blog 的本窗历史精确停点未完成，不能由 Blog 零项推广 |
| SRC-META-AI | [Meta Blog](https://ai.meta.com/blog/) 当前首屏可见 04/08 与后续 06/29 等混排卡片；Research/Publications 直开未得可核历史窗页 | 受阻 | 混排首屏及空响应不是本窗无论文证据；需官方可排序历史目录或具体原始发布 |
| SRC-QWEN | [动态研究列表](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US) 的 extra.date 邻界 04/22T10+08→04/28T10+08；[qwen-code release p338](https://api.github.com/repos/QwenLM/qwen-code/releases?per_page=1&page=338) 04/24T12:11:44Z→[p337](https://api.github.com/repos/QwenLM/qwen-code/releases?per_page=1&page=337) 04/26T06:49:56Z，两个 release 均窗外 | 已检查 | 研究目录与该仓库 release 层停点有效；不据此断言其它仓库 tag/普通提交均无事件 |
| SRC-DEEPSEEK | [官方 News/Research](https://deepseek.com/en/news/) 可见 News 04/24 V4 Preview→09/10，Research 02/25 DualPath→06/24 技术报告；没有本窗目录项 | 已检查 | 仅当前两个官方可见目录；旧 04/24 日级 V4 时间争议不回填本窗 |
| SRC-MOONSHOT | [Kimi CLI 1.39.0](https://api.github.com/repos/MoonshotAI/kimi-cli/releases/tags/1.39.0) 04/24T06:22:19Z→[1.40.0](https://api.github.com/repos/MoonshotAI/kimi-cli/releases/tags/1.40.0) 04/28T13:51:04Z；该仓库 release 层跨窗。[Platform Blog](https://platform.kimi.com/blog) 当前列表止于2025-11 | 受阻 | Blog 缺 2026 可核历史档；release 阴性不替代 Blog 或其它仓库 |
| SRC-TENCENT-HUNYUAN | 官方 Research“全部”同源 [publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，pageNum1/pageSize100/renderType0，实际 totalNum=9/list=9；displayPublishTime 04/23→04/30 跨窗 | 已检查 | 仅全部公共列表，不声称所有未列作者论文已被枚举 |
| SRC-ZAI | [官方 Research](https://www.zhipuai.cn/zh/research) 当前可见 04/07 GLM-5.1→04/29 Scaling Pain；[官方发布说明](https://docs.z.ai/release-notes/new-released) 04/07→06/16，均跨本窗 | 已检查 | 限两项可见官方目录，不推广到所有仓库/作者稿 |
| SRC-BYTEDANCE-SEED | [官方论文目录](https://seed.bytedance.com/en/research?view_from=homepage_tab) 列 04/26 MegaScale-Omni；同源 papers API 的 article_type=1/page_token=20 返回 ID1605、PublishDate=04/25T16Z；Blog type2/page0 最近04/22T16Z→04/08T16Z | 受阻 | 目录字段不能证当时可读全文，当前卡片已更新并指向五月 arXiv；ACM published-online 仅自然日精度，需当窗首公开链 |
| SRC-BAIDU-ERNIE | [ERNIE 技术 Blog](https://ernie.baidu.com/blog/zh/) 当前可见 04/15 ERNIE-Image→04/30 Preview；[官方仓库 release API](https://api.github.com/repos/PaddlePaddle/ERNIE/releases?per_page=100) 当前一条旧版，均无本窗可见项 | 已检查 | 限 Blog/该 repo release 层，不推断全部作者论文或无 tag 提交 |
| SRC-XIAOMI-MIMO | [MiMo 首页](https://mimo.xiaomi.com/) Paper 卡片 03/13→06/29 跨窗；同页 Blog 卡片无历史可核日期 | 受阻 | Paper 停点有效；Blog 需原始发布时间或可排序历史入口 |
| SRC-MINIMAX | [英文 Blog](https://www.minimax.io/blog) 03/18→05/26 跨窗；[Agent Tech Blog](https://agent.minimax.io/docs/techblog) 当前仅可见 05/13 项；[CLI release API](https://api.github.com/repos/MiniMax-AI/cli/releases?per_page=100) 04/17T20:51Z→04/26T01:40:29Z，后者晚于本窗 UTC01Z 截点 | 受阻 | 中文 Blog 本轮只得导航、Agent Tech 无四月历史停点；单仓 release 阴性不代表全机构零研究 |
| SRC-ARXIV | [官方公告日历](https://info.arxiv.org/help/availability.html) 正常在美东周日至周四公告，周五/六无正常批次；本窗 UTC 04/25T01Z→04/26T01Z 无正常公告时刻。旧按 submittedDate 枚举的419个身份不作当窗公开集合 | 已检查 | 正常日历不能排除异常公告或机构先发全文；具体正线索已分别隔离，不作全网零论文断言 |

补查 Github 官方当前可见新仓库创建层与少量主线 repo release，只用于查漏，不能把组织新仓库零结果或上述几仓的 release 阴性扩大成全组织零更新；实际八组织、新仓库及 VeOmni release 停点见[本日原始记录](../_sources/daily-20260426/V3_REOPEN_NOTES.md)。未扫描每周来源；无实际触发的按需来源不整站扫描。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

当前没有能确认首次公开完全落在本窗的贡献候选，因此没有对 Seed/ProEval 先评分或称为“已审完全文”。它们不是贡献前否定：Seed 的动态模态与长度负载下 encoder/LLM 并行及重分片、ProEval 的预训练 GP surrogate 加 Bayesian quadrature/superlevel-set failure sampling，都有值得在归属确认后核验的具体系统/评价边界。两者目前只在 §5 作为日期隔离，不混入确定分母。

## 4. 证据与知识整合

### [MegaScale-Omni](https://seed.bytedance.com/en/public_papers/megascale-omni-a-hyper-scale-workload-resilient-system-for-multimodal-llm-training-in-production)

官网目录标 04/26，Seed API 的 PublishDate=1777132800000 毫秒对应本窗 04/26 00:00 北京，题摘提出 encoder 长短序列并行、LLM 5D 并行、统一 encoder–LLM 表示/流水线和按 rank 的自适应 resharding，作者给出自有动态多模态负载相对四个系统的吞吐 1.27×–7.57×。这是题摘主张，不是已核实验配置、控制对照或普遍生产收益。该卡片 UpdateTime 在07/01，当前外链 [arXiv 2605.08962](https://arxiv.org/abs/2605.08962) 的 v1 在五月才提交；[Crossref DOI 记录](https://api.crossref.org/works/10.1145%2F3767295.3803587) created=04/24T20:20:04Z 是记录建立，published-online=04/26 只有日期，不能判断 09:00 北京前后。ACM PDF 直连未取得。没有本窗公众可读原始全文的时刻链，不能将后来全文机制/实验回填本日。源与同一研究家族的会议发表身份可保留，但不据此决定本窗 Books。

### [ProEval](https://deepmind.google/research/publications/238239/)

DeepMind 官方页标 04/25，完整题摘描述以预训练 Gaussian Process 为性能函数 surrogate，用 Bayesian quadrature 估计和 superlevel-set sampling 发现失败，涉及 Ch66 Evaluation 的潜在设计选择。当前页 JSON-LD 的 datePublished=2026-04-25T00:00:00Z 与日级显示相同且为整点零分秒；同站另一条 04/22 出版页也将日级日期写成 UTC 零点，不能独证真实上线时刻。[arXiv 2604.23099v1](https://arxiv.org/abs/2604.23099v1) 的周六 04/25T01:33:57Z 是提交，不是本窗公告；官方日历无正常周末公告。机构 [ProEval GitHub repo](https://api.github.com/repos/google-deepmind/proeval) created=04/17T23:59:55Z，但当前可见最早 commit 为04/27T18:13:15Z，截止本窗的 commit 查询与 release 均空：只约束这一仓库的可见记录，不证明官网未先发，也不证明本窗已发。未确定首次正文 owner 前，不读后续 v2 的方法/表来做本日证据和 Books 正面判断。

### Books 决定

Books 纳入任务范围，但两条潜在贡献都处于首公开日期隔离，尚无确认落窗候选可支持写入；本次 Books 实际新增 0。不是仅因 Ch36/Ch66 主题相关就宣称“已有覆盖”。若后续原始时间链证实其中一条属于本窗，再按精确当时版本读必要方法、主对照与反证，并与实际知识 owner 比较；共享章节动笔前先协调写锁。

## 5. 缺口与下一步

作者侧可访问材料的定点查询和上述贡献/日期分层已处理；十四来源停止范围、两条首公开隔离及当前零确定候选分母已由非作者核验。普通可执行审阅待办为零；下列项目仅是不能支持正面断言的具名外部保留项，取得原始证据后定点重开。

本窗外部终态保留项只隔离受影响断言，不删除已核目录事实，也不支持正面候选、Books 或“无遗漏”保证：

- **Seed MegaScale-Omni 首公开：**需作者/ACM/会议原始论文正文在 04/25T01Z～04/26T01Z 内公众可访问的精确时刻，或可验证历史卡片/全文快照；当前 Seed CMS PublishDate、后续 UpdateTime、五月 arXiv 和 Crossref created/日级 online date 的组合不能证明。若确认窗外，只迁回真实 owner 日，不把此题摘算本窗候选。
- **DeepMind ProEval 首公开：**需官网历史上线时间/快照或官方 arXiv 实际公告身份与当时 v1 正文；当前整日 04/25 页面日期、零点 JSON-LD 与周六提交均不能单独决定 09:00 北京边界。取得后只重开此项的日期、必要证据和 Ch66 对读。
- **来源历史入口：**OpenAI Research、Google Research Publications/DeepMind Blog、Meta Research/Publications、Kimi 2026 Blog、MiMo 无日期 Blog、MiniMax 中文 Blog/Agent Tech 四月档缺可复查本窗分页/发布时间。各自需要原站有序历史目录、可核本窗列表或具名发布正文；此前可读的 RSS、Blog、Paper 或 repo 切片不替代这些子入口。当前隔离不等于断言它们发布为零，若出现具体相关事件仅重开该来源/家族。
- **正常公告与索引边界：**arXiv 官方正常日历不排除异常公告；按 submittedDate 的旧 419 宽身份和 DOI created 不能作首公开队列。发现官方特殊公告身份或原站先发文档时定点重开，不重扫整个宽库。

窗外已核 release 不阻塞本窗：MiniMax CLI v1.0.12 于04/26 09:40:29北京、Qwen qwen-code v0.15.3 于04/26 14:49:56北京，均归后窗；Kimi CLI 1.39.0 属前窗。普通未读论文全文不被伪装成外部阻断，因为日期未先证实的两条目前只以题摘信号和明确重开条件保留。

## 6. 复核

复核者：root（非本日报作者）。
结论：通过

保留 §5 的具名外部隔离；核验范围和事实边界见[独立语义 Gate](../_sources/daily-20260426/V3_ROOT_DAILY_GATE_20260426.md)。十四每日来源已逐行对照，Seed 与 ProEval 的日期仍不能证明落窗，因此确定候选为零，Books 实际新增零；未把 News RSS、几仓 release 或旧 submittedDate 宽库存冒充机构全量覆盖。
