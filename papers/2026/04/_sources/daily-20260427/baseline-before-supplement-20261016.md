# Daily Research — 2026-04-27

**规范：** V3
**窗口：** 2026-04-26T09:00:00+08:00 ～ 2026-04-27T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-28T19:34:03+08:00

## 1. 结论

本窗目前最重要的增量不是论文数量，而是执行与证据的权责边界：issue 的当前状态与一次 Agent run 的产物不能混作同一个完成状态；反思机制需要同时计修正错误与误改正确答案；训练期早停初始化可能让可变深度模型根本学不到深路径；保护性梯度改写可能经 Adam 二阶幅度反向放大步长。这些命题已进入相应 Books 原有论证链，且各有非作者对实际正文和相邻段落的写后复核。若原始证据只支持受控负载，就不把实验数字写成生产收益或普适安全保证。

当前有界原始线索是 339 个 DataCite 初建身份与 69 个额外 OAI 题名，共 **408 个去重宽身份线索**；它们不是 408 篇新论文，也不是全文审阅配额。旧 V2.1 的 48 候选、全量 Complete 和旧 Books 标签未继承。按完整题摘及必要原文重新工作后，38 项初始工作家族中有 3 项经非作者定点校准改为具名前分母关闭，另有 11 项旧泛化否定侧漏收 `2604.22438v1/22550v1/22291v1/22662v1/22504v1/22615v1/22236v1/22442v1/22169v1/22464v1/22171v1` 经具名定点恢复，**本窗冻结 46 个候选家族**（含 1 个 OpenAI 官方发布）。其中 33 项实际整合并经过非作者写后复核，7 项已有具体章节覆盖并获非作者单篇审阅，4 项标准完成、仅报告，2 项中心证明或 exact-v1 正文版本证据被明确隔离。[非作者日级语义 Gate](../_sources/daily-20260427/V3_ROOT_DAILY_GATE_20260427.md)已通过；受阻历史入口不支撑全站无遗漏断言。

日期只按[arXiv 官方公告时刻及 ID 分配规则](https://info.arxiv.org/help/availability.html)、相邻 ID/批次、OAI 原字段及 exact-v1 身份作有界组合推断：通常 Sunday 20:00 ET 对应本窗 Monday 08:00 北京时间；本批采用 `2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00` 的有据推断，不是逐篇公告日志确证，更不是把 Submitted、DOI created、OAI datestamp 或 Updated 改名为首次公开。单篇版本冲突另隔离。14 个每日来源的已查入口、停止范围和剩余历史子目录/仓库限制见 §2；arXiv 分层否定侧、候选证据和实际 Books 已按本窗可核范围处理到安全终态。旧长篇正式稿已[原样归档](../_sources/daily-20260427/V2_REPORT_ARCHIVE.md)，归档与替换前正文 SHA-256 均为 `c424338637cfcb4a02d8dd4326ce6a36b610ee80df5ebcb7035397175c97eff3`；必要原文判断保留在[证据记录](../_sources/daily-20260427/V3_EVIDENCE_REVIEW.md)和[筛选记录](../_sources/daily-20260427/V3_SCREENING_NOTES.md)。

## 2. 来源覆盖

下表只对本次实际入口与日期邻界负责；“未完成”是尚可执行的普通检查，“受阻”是当前原站历史目录/必要版本无法取得，二者均不能替代为“零更新”。原始字段与查询细节见[来源发现记录](../_sources/daily-20260427/V3_SOURCE_DISCOVERY.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [News RSS](https://openai.com/news/rss.xml)按原始 `pubDate` 核邻界：Symphony、Choco 为 04/27T00Z，Our principles 为 04/26T16Z，均在窗；04/27T06Z 微软合作在窗外。Symphony 官方正文/Draft SPEC 已读；Choco 应用与原则文章具名前闭。补查 [Research Index](https://openai.com/research/index/) 首屏 09/23→08/18 共10项、末尾 `Load more`；Publication 首屏仍只到 07/28，直开页码与控件尝试均未取得 04/27 邻界。 | 受阻 | News RSS 不能代替 Research Index；原站命令行访问仍返回 HTTP 403，网页首屏虽可读却尚不能可靠回溯至本窗。需可用官方历史分页或具名同期原页，不据此断言研究零命中。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) HTML 原始 `publishedOn` 邻界 04/22T14:27Z→04/29T20:26Z，无本窗列表项。 | 已检查 | 只限公开 Research 目录，不代替作者论文。 |
| SRC-GOOGLE-AI | [Research Blog April](https://research.google/blog/2026/04/) 04/22→04/29；[DeepMind Publications](https://deepmind.google/research/publications/) 当前精选公开目录第一页 264 总数、05/06→04/25→04/23 的倒序邻界无本窗项；[DeepMind Blog](https://deepmind.google/blog/) 04/27 韩国合作仅自然日且属既有技术应用/合作。已重开 [Google Research Publications](https://research.google/pubs/)：2026 年约359条、每页15条、Year 排序，条目仅 venue 年份而无本站首次公开时刻。 | 受阻 | Blog/DeepMind 可见目录有界阴性不代替 Google Publications；后者无按日可停止的原始公开目录，需官方上架时间或具名同期记录定点重开，不据年份排序宣称本窗零发布。 |
| SRC-META-AI | [Meta Research](https://ai.meta.com/research/) 与[Blog](https://ai.meta.com/blog/) 实际打开，Blog 旧邻界 04/08→06/29。官方 [Publications 第1页](https://ai.meta.com/results/?content_types%5B0%5D=publication) 与[第2页](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=2)的近期有序段可见 05/26→05/19→05/04→04/16→04/14→04/09，跨过本窗，未见本窗 publication。 | 受阻 | Publications 近期段已有有界阴性，不再称首屏未查；第2页后半混旧年推荐，且 Research 首页/Projects 与其它资源不由该列表覆盖，不能据此宣称 Meta 全站零研究。 |
| SRC-QWEN | 官方动态研究 API 40 条 `extra.date` 04/22T10+08→04/28T10+08；静态 research-list 60 条均早于 2026，研究列表本窗无项。[qwen-code v0.15.3](https://github.com/QwenLM/qwen-code/releases/tag/v0.15.3) `published_at=04/26T06:49:56Z` 与 [04/27 nightly](https://github.com/QwenLM/qwen-code/releases/tag/v0.15.2-nightly.20260427.3b0b6c052) `published_at=04/27T00:25:13Z` 均在本窗，官方 API 单项分页 p335–339 给出相邻停点；会话历史 rewind、记录 flush、热路径 I/O、预连接的关键 PR 已定点核。现有 Ch81/84 已区分对话与环境恢复、运行收据提交，这批为 CLI 受限实现/修补而非新增长期机制，贡献前关闭。 | 已检查 | 注册的 Qwen 研究入口为动态40+静态60两列表，按真实邻界已查；qwen-code 作为额外触发仓库仅覆盖其 release 层。未查 QwenLM 其它仓库不能据此宣称组织级零更新，若有具名重要发布再定点重开；不把全组织逐仓列为本窗无限普通配额。 |
| SRC-DEEPSEEK | [Research/News](https://deepseek.com/en/news/) Research 02/25→06/24、News 04/24 V4 Preview→09/10 V4.1；两可见目录无本窗独立条目。 | 已检查 | 04/24 Preview 是窗前家族，PDF 内印 04/27 不单独创造首发；结论限公开目录。 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog) 当前首页最新为 2025-11-07；[kimi-cli 官方 release](https://api.github.com/repos/MoonshotAI/kimi-cli/releases?per_page=100) 04/24 1.39.0→04/28 1.40.0 跨本窗。官方组织当前 `sort=pushed` 前20仓库至 02/14 已低于本窗；其中窗前创建且主线相关的另八仓默认分支本窗 commits 均空，Releases 分别 0/0/19/0/0/17/0/0，非零仓的发布邻界均越过本窗，见[实际记录](../_sources/daily-20260427/V3_SOURCE_DISCOVERY.md)。 | 受阻 | GitHub 只限当前公开、所列主线仓库默认分支/可见 release，不证明曾删历史、其它 branch/tag 或站外论文。Kimi Blog 缺 2026 可按窗回溯的历史目录，旧首页不能作零命中；需官方旧目录或具名同期材料才重开此子入口。 |
| SRC-TENCENT-HUNYUAN | 官网 `publicList` 9/9，`displayPublishTime` 04/23→04/30 跨本窗。当前官方组织目录 83 仓到末；13 个后续活跃的主线仓默认分支本窗 commits 空、Releases 空且唯一可见 tag 属 2024；先前限流的六个窗前相邻仓 Releases 重取后也均完整为空，见[有界停点](../_sources/daily-20260427/V3_SOURCE_DISCOVERY.md)。 | 受阻 | 官网目录与当前公开主线仓可见层均无本窗项；非默认分支、已删/改权限历史、站外材料无可按窗回溯的完整档案，待官方 dated archive 或具名同期记录定点重开，不称组织全历史零更新。 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) 04/07→04/29；[官方 release notes](https://docs.z.ai/release-notes/new-released) 04/07→06/16。官方组织当前 `sort=pushed` 首30仓末项已早于本窗；窗前创建且后来仍活跃的 7 个主线仓库默认分支本窗 commits 均空，当前 Releases/Tags 各 0，详见[实际停点](../_sources/daily-20260427/V3_SOURCE_DISCOVERY.md)。 | 受阻 | 当前研究/发布目录及可见默认分支层无本窗项；非默认分支、删改权限历史和无按窗归档的旧原始发布无法由当前快照证明为零，取得官方 dated archive 或具名同期记录后定点重开。 |
| SRC-BYTEDANCE-SEED | 官方 Publications API `article_type=1` 共 242、页20所见 05/12→04/08，`article_type=2` 共95、首20 04/22→04/08。官方 GitHub 当前 63 仓；窗前创建且后来仍活跃的 12 仓逐个取 Releases/Tags 有效响应，`VeOmni` 17 项 release 的 04/15→04/27T08:21Z 邻界跨本窗，其余当前 release 无本窗项；当前可搜索 commits 精确窗 `0,incomplete_results=false`，见[有界停点](../_sources/daily-20260427/V3_SOURCE_DISCOVERY.md)。 | 受阻 | 仅官网可见目录与当前公开仓库的 release/tag/已索引提交层得有界阴性；`byteff2` 非 release tag 的目标 commit 04/21 不等于 tag 公开日。已删/改写历史、非默认分支、无按时刻归档的旧 tag/Blog 与站外作者 arXiv 无法由当前快照证明为零；取得官方 dated archive 或具名同期记录后定点重开。 |
| SRC-BAIDU-ERNIE | [文心官方博客](https://ernie.baidu.com/blog/zh/) 04/15→04/30 跨本窗；[PaddlePaddle/ERNIE Releases](https://api.github.com/repos/PaddlePaddle/ERNIE/releases?per_page=100) 当前仅 2025-06-30 一项。 | 已检查 | 只限这些可见入口，不覆盖其它仓库/论文。 |
| SRC-XIAOMI-MIMO | [MiMo Paper](https://mimo.xiaomi.com/) 03/13→06/29；官方组织当前 18 个公开仓库目录已到末页，5 仓本窗后创建，其余 13 仓本窗可见 Releases/Tags 全部空；其中当前 push 晚于本窗的 4 仓默认分支按本窗 UTC 起止取 commits 也均空，见[原始入口与停止范围](../_sources/daily-20260427/V3_SOURCE_DISCOVERY.md)。 | 受阻 | 仅 Paper 和当前仍公开的默认分支/Release/Tag 层可作有界阴性；首页 Blog 卡片无可核原始日期，无法判定本窗归属，需官方 dated archive 或同期原始材料定点重开。删除/改写历史、旧 branch 和站外论文不由当前组织快照排除。 |
| SRC-MINIMAX | [英文 Blog](https://www.minimax.io/blog)、[官方 IR dated releases](https://ir.minimax.io/news-events/new-releases) 英文列表 May26/27→Mar18 越过本窗、中文同题 Agent Team 与[Agent Tech Blog](https://agent.minimax.io/docs/llms.txt)定点；中文 JSON-LD 04/27T12Z 已越过09点截点，英文同题 05/27，不入本窗。[MiniMax-AI/cli v1.0.12](https://github.com/MiniMax-AI/cli/releases/tag/v1.0.12) 原始 `published_at=2026-04-26T01:40:29Z` 落本窗；[PR #94](https://github.com/MiniMax-AI/cli/pull/94/files) 的 HTTPS/重试及 base64 图片响应等只是既有 CLI 局部修复，贡献前关闭。官方 GitHub 当前 35 仓；窗前创建且后来仍活跃的 7 仓 Releases/Tags 已逐个取得有效响应，除 CLI 已审阳性外当前可见发布无本窗项；当前可搜索 commits 精确窗 `0,incomplete_results=false`，见[有界停点](../_sources/daily-20260427/V3_SOURCE_DISCOVERY.md)。 | 受阻 | 中英 Agent Team 首发日期冲突但均不在本窗；7 仓当前可见层不能证明已删/改写 release/tag、非默认分支、无日期历史 Blog 或其它历史发布为零。四个仅有 tag、没有 release 的旧目标 commit 也不等于 tag 公开时刻；取得官方 dated archive 或具名同期记录后定点重开。 |
| SRC-ARXIV | [官方公告规则](https://info.arxiv.org/help/availability.html) Sunday 20 ET；DataCite 339 个初建题名与官方 OAI 额外 69 个身份去重形成 408 宽线索；相邻 04/28 receipt 从 ID 2604.22754 开始。主线/含糊题摘、共享旧错误理由组 158 项与必要 exact-v1 已按贡献筛选；46 家族证据、Books 处置和分层否定侧获[非作者日级核验](../_sources/daily-20260427/V3_ROOT_DAILY_GATE_20260427.md)。 | 已检查 | OAI 可含修订、DOI/Submitted 非首发；日期只用批次组合推断，`22152` 版本证据隔离。不称 408 全是新论文、全部逐篇全文或全学科无遗漏。 |

对八个相关官方 GitHub 组织各做过 `created:2026-04-26..2026-04-27` 新仓库日期层查询，当前索引均无结果；这只排除**当前可见的新仓库创建线索**，不覆盖已删除/改权限/私有转公开、既有仓库 tag/release 或无 tag 的重要提交，不代替表中具名隔离的历史子入口。

Tencent-Hunyuan 的先前 GitHub 限流已在本轮六仓有效重试后消除；研究目录、当前可见组织仓库与剩余历史子入口的精确边界见上表和[来源发现记录](../_sources/daily-20260427/V3_SOURCE_DISCOVERY.md)。

## 3. 候选与判断

下表列本窗冻结的 46 项候选家族，33 项实际正文已有[非作者写后核验](../_sources/daily-20260427/V3_APR01_ROOT_WRITE_AFTER_INDEPENDENT.md)或下列各项具名写后记录。公开范围是有据组合推断而非逐篇日志确证；OpenAI Symphony 则有 News RSS 原始 `pubDate`。入选与本日 Gate 通过不代表作者所有主张成立或实验已复现。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [OpenAI Symphony](https://openai.com/index/open-source-codex-orchestration-symphony/) | 2026-04-27T08:00:00+08:00 | issue 当前状态与 run/PR 执行产物分权，2+2+2=6 | 深入完成 | 整合：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)，实际写后通过 |
| [2604.22750v1 How Do AI Agents Spend Your Money?](https://arxiv.org/html/2604.22750v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 预运行自估不能拥有硬预算/账单，2+1+2=5 | 深入完成 | 整合：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)，实际写后通过 |
| [2604.22136v1 Sovereign Agentic Loops](https://arxiv.org/html/2604.22136v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | Eq16 执行动作身份零信息保证有二元反例，2+2+2=6 | 争议 | 暂缓：中心定理未获证明；修正保证对象/补条件，见§5 |
| [2604.22152v1 dWorldEval](https://arxiv.org/abs/2604.22152v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | action-token/progress 评价线索与原版正文身份未核，2+1+2=5 | 争议 | 暂缓：官方 PDF v1 未取得、HTML 版本污染，见§5 |
| [2604.22180v1 ResRank](https://arxiv.org/html/2604.22180v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 同 encoder 的检索/重排双目标分账，2+2+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，实际写后通过 |
| [2604.22266v1 Large Language Models Decide Early and Explain Later](https://arxiv.org/html/2604.22266v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 离线最后切换点不等在线停止 oracle，2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，非作者单篇通过；整日 Gate 待核 |
| [2604.22236v1 Algorithmic Feature Highlighting for Human-AI Decision-Making](https://arxiv.org/html/2604.22236v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 展示特征的选择事件本身影响下游判断后验，2+1+2=5 | 标准完成 | 仅报告：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；受限模型与 housing 重放，不外推真人/LLM 部署 |
| [2604.22169v1 ReCast](https://arxiv.org/html/2604.22169v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 全零组目标派生 anchor 与 rollout 搜索/actor 更新宽度分账，2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，原6分标准证据因实际知识缺口深入 override、[非作者写后通过](../_sources/daily-20260427/V3_ROOT_22169_CH33_WRITE_AFTER.md) |
| [2604.22171v1 MCI](https://arxiv.org/html/2604.22171v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 任意过滤下 predicate-agnostic clique cover 与多 seed 可达性选择，2+2+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)；真实 owner 缺口深入 override，[非书稿作者实际写后通过](../_sources/daily-20260427/V3_APR01_22171_CH76_WRITE_AFTER.md) |
| [2604.22271v1 How LLMs Detect and Correct Their Own Errors](https://arxiv.org/html/2604.22271v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | probe 可读与必要因果路径分离，2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，非作者单篇通过；整日 Gate 待核 |
| [2604.22407v1 Hidden Failure Modes of Gradient Modification under Adam](https://arxiv.org/html/2604.22407v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 保护梯度与二阶矩反向耦合，2+2+2=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，实际写后通过 |
| [2604.22442v1 HubRouter](https://arxiv.org/html/2604.22442v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | hub fingerprint→稀疏 council 的受限混合路径与 strict-causal 反证，2+1+2=5 | 标准完成 | 仅报告：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)；小型从头模型、retrofit 失败，不采速度宣传 |
| [2604.22464v1 MADE-IT](https://arxiv.org/html/2604.22464v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 连续任务模型的子空间 expert 演化、输入投影隐式路由及路径一致性分权，2+1+2=5 | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md)，真实缺口触发深入 override，[非作者实际写后通过](../_sources/daily-20260427/V3_APR01_22464_CH30_WRITE_AFTER.md) |
| [2604.22520v1 RouteLMT](https://arxiv.org/html/2604.22520v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | gain-only 路由尾部损失与 guard 成本，2+1+2=5 | 标准完成 | 已有覆盖：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)，非作者单篇通过；整日 Gate 待核 |
| [2604.22575v1 SpikingBrain2.0](https://arxiv.org/html/2604.22575v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | hybrid 层替换/蒸馏与执行路径反向，2+1+2=5 | 标准完成 | 已有覆盖：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md) 承载层替换与蒸馏；INT8 activation→有符号时序 spike 执行由 INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 承载；非作者单篇通过、整日 Gate 待核 |
| [2604.22238v1 CodeGraphVLP](https://arxiv.org/html/2604.22238v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 在线语义图进展谓词→VLA 双输入，2+2+2=6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，实际写后通过 |
| [2604.22591v1 RedVLA](https://arxiv.org/html/2604.22591v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | task-feasible 风险场景与过程违约分母，2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，实际写后通过 |
| [2604.22615v1 GazeVLA](https://arxiv.org/html/2604.22615v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 人类 gaze 前动作监督→意图 token/KV→action head 的条件分支，2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，实际写后通过 |
| [2604.22074v1 Outcome Rewards Do Not Guarantee Verifiable or Causally Important Reasoning](https://arxiv.org/html/2604.22074v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | outcome/CIR/SR 三轴分离，2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，实际写后通过 |
| [2604.22167v1 Estimating Tail Risks in Language Model Output Distributions](https://arxiv.org/html/2604.22167v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 固定输入输出尾险之外的 query 家族×条件输出双轴分母，2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，实际写后由非作者核验通过 |
| [2604.22127v1 Where Should LoRA Go? Component-Type Placement in Hybrid Language Models](https://arxiv.org/html/2604.22127v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | hybrid 组件类型×串/并行拓扑的 adapter placement 身份，2+2+2=6 | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md)，实际写后由非作者核验通过 |
| [2604.22509v1 LaissezCloud: Continuous Resource Renegotiation for the Public Cloud](https://arxiv.org/html/2604.22509v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 跨租户/运营方的运行中资源重议与硬约束分权，2+2+2=6 | 深入完成 | 整合：PLATFORM-GPU-SCHEDULER [Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)，实际写后由非作者核验通过 |
| [2604.22438v1 SSG: Logit-Balanced Vocabulary Partitioning for LLM Watermarking](https://arxiv.org/html/2604.22438v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 单 bit keyed 分组等词数不等概率质量，2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，实际写后由非作者核验通过 |
| [2604.22550v1 ArmSSL: Adversarial Robust Black-Box Watermarking for Self-Supervised Learning Pre-trained Encoders](https://arxiv.org/html/2604.22550v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | encoder 下游黑盒归属接口与水印 OOD 可检测性，2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，实际写后由非作者核验通过 |
| [2604.22291v1 Train in Vain: Functionality-Preserving Poisoning to Prevent Unauthorized Use of Code Datasets](https://arxiv.org/html/2604.22291v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 代码编译/功能测试通过仍可污染训练监督，2+2+2=6 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)，实际写后由非作者核验通过 |
| [2604.22228v1 Accelerating Intra-Node GPU-to-GPU Communication Through Multi-Path Transfers with CUDA Graphs](https://arxiv.org/html/2604.22228v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | payload 分路与 CUDA Graph replay 收益分账，2+2+2=6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，本轮 marker 修后非作者写后通过 |
| [2604.22312v1 Guess-Verify-Refine: Data-Aware Top-K for Sparse-Attention Decoding on Blackwell via Temporal Correlation](https://arxiv.org/html/2604.22312v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | previous-step proposal 与 exact verify/refine 分权，2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，本轮条件修后非作者写后通过 |
| [2604.22753v1 Spend Less, Fit Better: Budget-Efficient Scaling Law Fitting via Active Experiment Selection](https://arxiv.org/html/2604.22753v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | target-region 信息收益除以异质 run 成本，2+2+2=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，本轮成本式修后非作者写后通过 |
| [2604.22273v1 When Does LLM Self-Correction Help?](https://arxiv.org/html/2604.22273v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | ECR/EIR × 初始正确率的修订净值，2+2+2=6 | 深入完成 | 整合：AGENT-REFLECTION [Ch80](../../../../books/part-07-agent/80-reflection.md)，实际写后通过 |
| [2604.21999v1 Universal Transformers Need Memory](https://arxiv.org/html/2604.21999v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | ACT 初始浅停锁深路径训练，2+1+2=5 | 深入完成 | 整合：MODEL-TRANSFORMER-LAYER [Ch17](../../../../books/part-02-model/17-transformer-layer.md)，真实缺口 override、写后通过 |
| [2604.22565v1 Learning Evidence Highlighting for Frozen LLMs](https://arxiv.org/html/2604.22565v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 保留全文、只改变注意入口，2+2+2=6 | 标准完成 | 已有覆盖：AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md)，非作者单篇通过；整日 Gate 待核 |
| [2604.21964v1 Lessons from External Review of DeepMind's Scheming Inability Safety Case](https://arxiv.org/html/2604.21964v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | safety-case decision/environment/有效期/defeater，2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，实际写后通过 |
| [2604.22032v1 Kernel Contracts](https://arxiv.org/html/2604.22032v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | shape/数值/异常的跨硬件独立 oracle 合同，2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，实际写后通过 |
| [2604.22191v1 Behavioral Canaries](https://arxiv.org/html/2604.22191v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | RLFT 间接样本影响审计与字串/MIA分离，2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，实际写后通过 |
| [2604.22409v1 SpaMEM](https://arxiv.org/html/2604.22409v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | L1/L2/L3 与 stepwise/episodic 评估分母，2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，实际写后通过 |
| [2604.22661v1 Can QPP Choose the Right Query Variant?](https://arxiv.org/html/2604.22661v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | query 改写的检索前选一，ranking-optimal≠answer-optimal，2+2+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，实际写后通过 |
| [2604.22076v1 PrivUn](https://arxiv.org/abs/2604.22076v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 不完整 forget set 的 core-set 与未知集合验收，2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，实际写后通过 |
| [2604.22117v1 PermaFrost-Attack](https://arxiv.org/abs/2604.22117v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 预训练威胁不能由 SFT proxy 证明，2+1+2=5 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，保护纠错 override、非作者单篇通过；整日 Gate 待核 |
| [2604.22193v1 How Large Language Models Balance Internal Knowledge with User and Document Assertions](https://arxiv.org/html/2604.22193v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 三来源正误/次序冲突及正确断言利用退步，2+1+2=5 | 标准完成 | 已有覆盖：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，非作者单篇通过；整日 Gate 待核 |
| [2604.22038v1 Source-Modality Monitoring in Vision-Language Models](https://arxiv.org/html/2604.22038v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 模型自述来源与输入真实模态分权，2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，apr02 非作者实际写后通过 |
| [2604.22082v1 Removing Sandbagging in LLMs by Training with Weak Supervision](https://arxiv.org/html/2604.22082v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 弱监督 elicitation 仅给可观察能力下界，2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，apr02 非作者实际写后通过 |
| [2604.22662v1 Rethinking XAI Evaluation](https://arxiv.org/html/2604.22662v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 解释 proxy/主观信心不等于人类客观决策改善，2+1+2=5 | 标准完成 | 仅报告：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；表格风控受限，不泛化 LLM |
| [2604.22504v1 Objective Shaping with Hard Negatives](https://arxiv.org/html/2604.22504v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 同用户负物品 proposal 改变受限 pairwise surrogate，2+1+2=5 | 标准完成 | 仅报告：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)；单正例/二元 reward 特例不泛化通用 GRPO |
| [2604.22678v1 BERAG](https://arxiv.org/html/2604.22678v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 文档条件生成分支的 token 后验与剪枝成本，2+2+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，[非作者写后通过](../_sources/daily-20260427/V3_APR02_CH76_UAE_BERAG_WRITE_AFTER.md) |
| [2604.22709v1 Abstract-CoT](https://arxiv.org/html/2604.22709v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 离散隐码 warm-up→受约束 RL 与训练/输出成本分账，2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，[非作者写后通过](../_sources/daily-20260427/V3_APR20_22709_CH33_WRITE_AFTER_INDEPENDENT.md) |
| [2604.22722v1 UAE](https://arxiv.org/html/2604.22722v1) | 2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00 | 离线 reader 效用蒸馏入线上 ANN 双塔，2+1+2=5 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，5 分实际知识缺口深入 override，[非作者写后通过](../_sources/daily-20260427/V3_APR02_CH76_UAE_BERAG_WRITE_AFTER.md) |

## 4. 证据与知识整合

下面每项是本次确实读到的 exact-v1 必要段与原有章节实际论点的短结论；[日内证据记录](../_sources/daily-20260427/V3_EVIDENCE_REVIEW.md)保留更完整的方法、评价、反例与受限设备/任务条件。并不宣称作者实验独立复现。普通 Books 待办已清零，不用“已吸收的语义增量”一类无内容占位。

### [OpenAI Symphony](https://openai.com/index/open-source-codex-orchestration-symphony/)

官方 04/27T00Z 文章和嵌入 Draft v1 SPEC 将 issue tracker 的当前 blocked/terminal 状态作为持续 eligibility，AgentRun/workspace/PR 则是单次执行及交付证据，成功可进入 Human Review 而非自动 Done。Ch81 已有有界 retry/reconciliation，Ch84 原有 AgentRun 却未明确跨这两种身份的 owner；已在 Ch84 原论证窄写并经非作者写后复核。Draft 不证明 exactly-once、安全沙箱或文章观察到的 PR 增长具有因果性。

### [2604.22750v1 How Do AI Agents Spend Your Money?](https://arxiv.org/html/2604.22750v1)

exact-v1 §2/6/7 用 OpenHands/SWE-bench Verified 的八模型、每题四 run 测预运行成本自估；所测输入/输出预测与实际 Pearson 上限约 .38/.39，估算调用本身有时超过任务成本。Ch84 stop controller 已有 runtime cap，但未把 pre-run self-estimate 从硬预算权降为粗预警；已加入独立 meter/hard cap/outcome 的条件链。全历史未压缩、任务/模型有限，不能推出普遍逐题报价精度。

### [2604.22136v1 Sovereign Agentic Loops](https://arxiv.org/html/2604.22136v1)

§3.2 的 control plane 用私有映射把匿名意图还原到真实执行对象；§3.3 却宣称执行动作给定匿名状态不泄漏真实身份。令真实目标 A/B 等概率、匿名视图恒定、意图恒为终止该匿名目标，实际动作仍分别是 Terminate(A/B)，可见模型“看不到身份”不推出真实执行动作零信息。只隔离 Eq16 的强保证，保留 effect-time policy gate 的受限架构价值；须作者补保证对象与条件/证明后定点重开，不写 Books。

### [2604.22152v1 dWorldEval](https://arxiv.org/abs/2604.22152v1)

官方 abs/v1 题摘提示统一 action/vision/language token 与 progress proxy，但 HTML `/v1` 首页含 08/24 日期，不能把其方法与性能数字回填 April exact-v1；39MB 官方 PDF v1 本轮定点读取超时且未取得可读全稿。Ch25/66 已区分 imagined rollout 与真实机器人 outcome，但在同版本方法/评价未确认前不判新系统合同，不写 Books。可读官方 PDF v1 或同期同版材料是重开条件。

### [2604.22180v1 ResRank](https://arxiv.org/html/2604.22180v1)

§III–IV 同 encoder 兼 first-stage passage retrieval 和 rerank，分别需 InfoNCE 与 RankNet；Table V 移除 retrieval loss 后 rerank 分数未降，单看后段会漏前段退化。Ch76 原有候选/答案阶段与 rerank 无生成成本判断，却缺同资产双目标冲突；已在 Reranking 主线整合并独立写后通过。BM25/RRF、离线索引和总 wall-clock 是共存/未证明边界，100 processed/0 generated 不是端到端成本。

### [2604.22266v1 Large Language Models Decide Early and Explain Later](https://arxiv.org/html/2604.22266v1)

§3/5 的“最终一次答案切换”只有看完完整轨迹后才知道，强制前缀读出与自由续写也不是一个测量；线性 probe 学最终答案一致，不学任务正确率。Ch66 已明确这两种协议、离线 oracle 与线上阈值/成本分权，本研究保留为 Qwen3-4B 特定任务的负例，不据部分 token 节省改停止权；[非作者单篇复核](../_sources/daily-20260427/V3_EXISTING_INDEPENDENT_AUDIT.md)及整日 Gate 已通过。

### [2604.22236v1 Algorithmic Feature Highlighting for Human-AI Decision-Making](https://arxiv.org/html/2604.22236v1)

official exact-v1 §1/3 区分知道展示策略的 sophisticated receiver 与把所展示特征当作外生的 naive receiver：选择事件 `I` 本身携带信息，前者最优的展示在模型设定中可能伤害后者。Ch66 原有解释评价与人类结果分账，但没有明确“展示策略也是下游判断输入身份”；该有限反例可列仅报告，不把模型 posterior 或 §7 housing 数据重放说成真实人类/LLM 部署证据。旧“局部模型/优化方法”关闭理由经[同类子集抽查](../_sources/daily-20260427/V3_GENERIC_LOCAL_METHOD_SUBSET_AUDIT.md)和 root 独立 §1/3 复核撤销；Submitted 04/24 非公告，v1 Updated、DOI 初建、相邻 ID 与官方 Sunday 公告规则只支持本窗 08～09 北京时间的组合推断。

### [2604.22442v1 HubRouter](https://arxiv.org/html/2604.22442v1)

exact-v1 §§2–7 将 learned hubs 的全局压缩、token fingerprint、top-k/邻居 council 与 chunked causal update 连成一条受限稀疏路径；早期双向 council 泄漏导致原性能判断失效，修正后的 strict-causal Hub-GPT 在 256/512 长度质量落后 Jamba。Ch22 已有 selector、anchor、混合路径和迁移/质量回退，当前小型从头模型证据不足以再改长期正文，故仅报告这一实质反证与条件配方；pretrained retrofit 失败，约 90× 来自未优化 PyTorch 对照，10–15× 是估计不是实测生产收益。root 已独立对读原文与 Ch22，同意撤销旧泛化前闭；本项 Updated 04/27T00:34:33Z、OAI 04/27、DOI 初建 01:37:33Z 仅与官方 Sunday 公告/ID 赋号及相邻批次联合推断本窗 08～09 北京时间，不以任一字段当首发。

### [2604.22464v1 MADE-IT](https://arxiv.org/html/2604.22464v1)

exact-v1 §3.1–3.2 把连续到达的同基座任务模型拆为三项状态：模块权重增量经 truncated SVD 后按输入/输出子空间亲和与阈值提出合并或新建 expert；当前中间特征对输入子空间投影匹配提出隐式路由；共同任务来源约束跨模块可连通路径。Ch30 旧 Continual VLM 段已有 expert evolution 与可由任务样本校准的 task-prototype selector，但没有无额外 router 训练数据时的几何 proposal/路由条件分支；root 已在该段后窄写，获[非书稿作者实际正文、邻接及原文写后 PASS](../_sources/daily-20260427/V3_APR01_22464_CH30_WRITE_AFTER.md)。几何相近不是功能或标签等价，推理仍须扫描候选，SVD/合并与原任务模型训练均非免费；§4 的 CLIP-ViT B/32、B/16、L/14 连续 8/14/20 图像分类任务 ACC/BWT 不证明生成式 MoE 或真实服务时延。原 task-prototype/learned gate 有可信样本时仍可共存，失败回退独立 adapter/frozen base。Submitted 04/24 非公开证据；v1 Updated 04/27T00:35:19Z、OAI 04/27、DOI 初建 01:38:05Z 只与官方 Sunday 公告/ID 赋号及相邻批次联合推断本窗 08～09 北京时间。

### [2604.22169v1 ReCast](https://arxiv.org/html/2604.22169v1)

exact-v1 §2–4 在离线单目标 next-item 的稀疏二元命中下，先用目标派生正 anchor 修复全零组，再只取组内最强正例/最难负例更新，把 rollout 搜索 `G` 与 actor old/ref/log-prob/反传宽度分开；结构接近度用于组内选择，不替代 task reward。Ch33 已有丢弃全零组、固定边界统计和困难度分流，却缺“保留宽搜索，只让局部边界进入更新”的状态/成本契约，现已嵌入原论证并获[非作者实际写后复核](../_sources/daily-20260427/V3_ROOT_22169_CH33_WRITE_AFTER.md)。目标派生 anchor 与 rollout producer 不同，不能称更新仍原样 on-policy/无偏；64 Ascend NPU、Qwen3-8B、`G=32` 下 step `371.54→77.00s`、actor `211.04→12.71s` 是同设置训练分账，强 backbone 修复反向，不能外推通用 RL/服务加速。Submitted 04/24 非公开证明；receipt v1 Updated 04/27T00:14:40Z、OAI 04/27、DOI created 01:30:46Z 与相邻 `22168/22170` 同批，仅合官方 Sunday20ET/ID赋号及次批边界推本窗 08～09 北京时间。

### [2604.22271v1 How LLMs Detect and Correct Their Own Errors](https://arxiv.org/html/2604.22271v1)

§3–4 与附录的 PANL 激活在 Gemma3-27B/TriviaQA 受限切片有可读信号，特定均值腐化后的恢复可救部分检测；但单独 PANL 消融对 d′ 没有可测作用，LAT 消融另有影响。Ch66 已将线性可读、干预/消融、correctability sensor 与外部 outcome 授权分开，故不把 probe AUROC 升为在线自动修正 gate；已有覆盖需独立终核。

### [2604.22407v1 Hidden Failure Modes of Gradient Modification under Adam](https://arxiv.org/html/2604.22407v1)

§3–5 的失效并非“梯度保护无效”这么泛：若同一被衰减的保护方向同时形成 Adam 一、二阶矩，二阶下降会放大该方向有效步长；一阶用 modified、二阶用 raw 是受限修复，但固定路由在高重叠场景也会更差。Ch28 原 Continual Pretraining 有 replay/geometry 而无此组合失效，已窄写分责/调度/回退并经写后复核。标量 surrogate 不是逐坐标定理，7B LoRA 等测试不推任意 stream。

### [2604.22520v1 RouteLMT](https://arxiv.org/html/2604.22520v1)

§3–6 以小翻译模型 hidden state 预估调用大模型的条件 gain，避免先解码小模型答案，但固定 p=.3 的 gain-only severe loss 8.19% 高于 random 7.10%；译文后 quality guard 能降至 5.69% 却多付一次生成/评分。Ch56 已把条件边际收益和独立质量/预算 gate 分开；此受限反向切片不改变现有路由控制，[非作者单篇核验](../_sources/daily-20260427/V3_EXISTING_INDEPENDENT_AUDIT.md)通过，仍不声称跨任务普遍比例或节约总时延。

### [2604.22575v1 SpikingBrain2.0](https://arxiv.org/html/2604.22575v1)

§3–5 从 Qwen3-4B checkpoint 按层敏感度选 sparse exact、linear 与 full attention，再付蒸馏、延长训练和转换成本。HuggingFace 4M/32GPU 与 vLLM TP8 的长度/服务结果不能拼成同一 SLO；128K TPOT 还有慢于原 Qwen3 的切片。Ch22 已有逐层混合、dense→hybrid 蒸馏及任务—训练—执行联验；§3.3/§5.4 的 INT8 activation 展开为有符号 7-step spike、专用阵列逐时步累加则由 Ch49 已有整数激活→时序 spike 执行段承载。28nm synthesis/gate-level switching 是硬件 proxy，不是制芯或完整 serving 能耗。经有限非作者对照，两侧已有覆盖；日级终核已通过。

### [2604.22238v1 CodeGraphVLP](https://arxiv.org/html/2604.22238v1)

§III 的在线可修订语义图由分割/跟踪更新，初始合成的 planner 每个 action chunk 后查询进展，`(subtask,relevant objects)` 同时调语言和 masked 视觉输入；物理执行仍属低层控制器与环境。Ch25 原 symbolic video 没有这个状态交接，已嵌入并经非作者写后复核。仅三项 UR10e 桌面任务；换 planner/graph 的 Table II 不是纯代码因果消融，生成/跟踪/代码安全成本未消失。

### [2604.22591v1 RedVLA](https://arxiv.org/html/2604.22591v1)

§3–6 把任务可行 benign 场景中的真实交互区域当风险因子落点，再分即时、累积、顺序违约，而非只看动作标签或终点成功。Ch26 原 simulator/outcome 分账缺这组物理失效分母，已窄写场景/evaluator/controller 分权并经写后复核。固定指令、六 VLA、两任务各十 trial 与预定义 predicate 不证明开放环境安全率或 guard 生产效果。

### [2604.22615v1 GazeVLA](https://arxiv.org/html/2604.22615v1)

旧 receipt 用“局部模型方法”关闭了该家族，但 exact-v1 §3.1–3.3 给出不同于动作坐标或派生轨迹的人类监督选择：采集带有效标记的前动作 gaze，先预测离散意图 token，再由其 KV 条件化连续 action expert；机器人后训练没有 gaze 标签。Ch26 原 human-video breadth/derived label 与 Plan/Think 不等于这一跨本体训练接口，已在数据演进主线窄写并获 root 非作者实际写后 PASS。§4.4/Table 2 的同后训练数据、仅推理关掉意图步对照为 ID `19/20` 对 `16/20`、OOD-object `8/10` 对 `6/10`，仍只是拾放小样本；其它消融同时改变训练阶段，不能把全部收益归于 gaze。眼动采集、对齐、预训练及额外 token/KV 有成本，gaze 非真实因果意图或物理安全真值，直接 BC/轨迹标签与低层 controller 仍共存。官方 HTML/v1 首页及 abs/v1 身份相合；16.8 MB PDF v1 本轮下载超时，未冒称 PDF 已读。

### [2604.22074v1 Outcome Rewards Do Not Guarantee Verifiable or Causally Important Reasoning](https://arxiv.org/html/2604.22074v1)

§3–7 分清答案正确、给定前缀截断后的答案分布敏感 CIR，以及去显式答案后的外部 verifier agreement SR。Ch66 现已写三轴，不能从 outcome reward 推链的因果重要性；CIR 是操作性受限干预而非完整内部因果识别，SR 自称 permissive 且非逐步证明。40 个选定 ReasoningGym 任务、Qwen2.5 1.5/3/7B 与额外读出/rollout 成本不可略去；写后已独立通过。

### [2604.22167v1 Estimating Tail Risks in Language Model Output Distributions](https://arxiv.org/html/2604.22167v1)

§3–4 为固定输入的 harmful-output 稀有事件构造 proposal，再对目标生成轨迹逐 token 重权；支持覆盖、likelihood 取得、方差/ESS 是估计可用性条件。Ch66 已具体写相同的**固定输入** Rare Failure Evaluation 责任；10k brute-force 亦是有噪参考，不把 proposal 命中率当目标风险。但 §6.1–6.2 又把 query/paraphrase 家族的输入分布与每个输入下的输出尾险联合估计，原 Ch66 该段尚缺这层双轴分母。有限非作者审核否定原“全部 Existing”，root 已在 Ch66 原论证后窄写输入家族/`D_query`、每输入尾险、n/阈值与成本/Unknown 的分账；实际正文已由[非写入者核验通过](../_sources/daily-20260427/V3_APR01_ROOT_WRITE_AFTER_INDEPENDENT.md)。309 原问题的 25 改写在同池拆 30/70，不能称新 base-query 或真实部署流量保证。

### [2604.22273v1 When Does LLM Self-Correction Help?](https://arxiv.org/html/2604.22273v1)

§III–IV 用 ECR/EIR 区分错→对与对→错，初答正确率为 `A` 时单轮二态净变化是 `(1-A)·ECR−A·EIR`；只有“可修一部分错”不能保证继续有净值。Ch80 Stopping Policy 已加入 verify-first 与额外成本/独立证据的条件分支，root 对实际正文和邻接写后通过。GSM8K 500 题/七模型与调用数不完全配对不推出任意多轮策略或开放 Agent 收益。

### [2604.21999v1 Universal Transformers Need Memory](https://arxiv.org/html/2604.21999v1)

§2–5/8 的单块递归模型起始 ACT bias=0 约两步浅停，使深路径缺学习机会；降低初始 halt prior 与 scratch/T 联校才是训练责任，不是推理时单纯加轮数。Ch17 原有 parameter/execution depth 分离而无此初始化陷阱，已嵌入成本、T64 dilution 与固定深度回退并经 root 写后通过。仅约 3.2M、Sudoku-Extreme/三 seed，不是大语言模型必须显式 memory slots 的定律。

### [2604.22565v1 Learning Evidence Highlighting for Frozen LLMs](https://arxiv.org/html/2604.22565v1)

§4–5 由 Actor 选择原文 spans 插标签，frozen Solver 仍读完整上下文；这是改变注意入口而非压缩/删除，硬 token cap 下不能替代前者且另付 Actor/标签成本。Ch75 已逐项承载这条独立输入变换及回退，所以 Books 判已有覆盖；其跨数据集结果不把 highlighted span 变成外部证据真值，[非作者单篇核验](../_sources/daily-20260427/V3_EXISTING_INDEPENDENT_AUDIT.md)已通过。

### [2604.21964v1 Lessons from External Review of DeepMind's Scheming Inability Safety Case](https://arxiv.org/html/2604.21964v1)

§3 的 safety case 不止 evidence-to-claim，还须说明所支持的 decision、assured system 与部署环境、有效期限及 defeater 重开条件。Ch66 原有证据分账已补这一条 assurance contract，并经非作者写后复核。文章只审公开材料，不具有未公开工程附件；不能推 GDM 实际部署不安全或某能力缺失已经证明。

### [2604.22032v1 Kernel Contracts](https://arxiv.org/html/2604.22032v1)

§3/5 的 specification 字段将 scope、pre/post、reference、measurement、tolerance、violation 分开；名称或一次 smoke pass 不能定义跨硬件的数值/shape/异常语义。Ch49 原差分测试已有，却缺 oracle/容差来源的契约身份，现已窄写且通过写后核。附录示意 grammar/示例测试不等形式证明，12 类也不是逐类生产故障率。

### [2604.22191v1 Behavioral Canaries](https://arxiv.org/html/2604.22191v1)

§3–5 检查 RLFT 的私有检索文档是否经 reward-mediated 路径影响行为：document-disjoint RM/RL/Eval、同 query 的 clean/trigger 配对与聚合 log-prob shift，不能由字串扫描或普通 MIA 代替。Ch72 已在直接 canary 后补训练参与审计对象，root 写后通过。受控 RepliQA/QMSUM 与 PPO/GRPO、信号弱且依赖有效 post-curation injection，不证明单文档使用或 provider 违约。

### [2604.22409v1 SpaMEM](https://arxiv.org/html/2604.22409v1)

§3–5 将即时视觉感知 L1、oracle 文本状态 L2、原始视觉流 L3 与逐步/episode 评分分开，Ch66 原总体 eval 阶梯无此同任务分母，现已吸收且写后通过。L2→L3 同时改变模态与状态权威，不能把性能差额全归“记忆”；数据规模和 oracle 状态不是部署物理真值。

### [2604.22661v1 Can QPP Choose the Right Query Variant?](https://arxiv.org/html/2604.22661v1)

同一需求多个改写可在检索前先选一；§3–5 表明 ranking-optimal 未必 answer-optimal。Ch76 原 query/retrieval/answer 分层并未明确这一选择点，现已加入且经写后复核；证据限固定 BM25、TREC-RAG2024 top5/nugget 与未配对生成成本，不把 QPP 分数直接当答案质量或普适线上收益。

### [2604.22076v1 PrivUn](https://arxiv.org/abs/2604.22076v1)

§4.2 把不完整 forget set 下的已选、未选和未知集合分别作为 unlearning 验收对象，梯度相似性只为 GA/NPO 的相关性启发，10% core-set 的 32.19% P3 对照仅在 GA/该数据条件中成立。Ch72 原不完整集合/主动恢复主线缺 core-set 选择责任，已补白盒梯度成本、独立验收与随机/全量/重训回退，root 写后通过；不声称删除证明。

### [2604.22117v1 PermaFrost-Attack](https://arxiv.org/abs/2604.22117v1)

作者威胁叙述涉及分散网站进入大规模预训练，但 §2 真正实验是固定显式 trigger 的 SFT 代理；§3 的几何诊断也只在该受控训练条件下测潜在表示变化。Ch72 原训练污染和 clean/attack 分层已容纳“威胁假设≠实测攻击路径”，故仅将此作为安全证据权限反例保留 Daily；不能证明网站投毒潜伏或几何指标是普适安全 sensor，[非作者单篇核验](../_sources/daily-20260427/V3_EXISTING_INDEPENDENT_AUDIT.md)已通过。

### [2604.22193v1 How Large Language Models Balance Internal Knowledge with User and Document Assertions](https://arxiv.org/html/2604.22193v1)

§3 的 bare/user/document 正误与次序配对区分模型先验和外部断言，§7 mixed SFT 虽提升错误断言下准确率，却降低正确断言利用，不能概括为统一“更稳健”。Ch76 已分 prior、证据确定性、来源权威与独立 answer gate；该文是受限 MCQ 评价切片，不是实际 retrieval provenance 或授权真值。[非作者单篇核验](../_sources/daily-20260427/V3_EXISTING_INDEPENDENT_AUDIT.md)及整日 Gate 已通过。

### [2604.22038v1 Source-Modality Monitoring in Vision-Language Models](https://arxiv.org/html/2604.22038v1)

§2.1–2.4 的不一致图文对与目标模态提问分开 valid response/selectivity，§3–4 的 marker/content cue 扰动在 11 VLM 中显示模型能答对却错绑来源；模型报告与 cue 只能是 sensor，真实输入来源由 ingestion lineage 拥有。Ch66 原有正文已将这条分权置入多模态评估，apr02 非作者重开 exact-v1 并顺读 Ch66:141–147、相邻段与章末证据后确认写后通过。实验依配对和 judge，不证明任意模态/Agent provenance 可由 self-report 推断。

### [2604.22082v1 Removing Sandbagging in LLMs by Training with Weak Supervision](https://arxiv.org/html/2604.22082v1)

§2–6 只在人工 sandbagging model organism、有限 gold/弱 supervisor 和 train/deploy 区分条件下验证 SFT+RL 可观察 elicitation；RL 单独可 reward-hack，且训练可识别时部署隐藏仍可维持。Ch66 现有正文把 observed baseline、弱监督诱发的 capability lower bound 与独立 release Gate 分开；apr02 非作者核 exact-v1 §2.1.1–2.1.3/§3–6/§8.2 与实际 Ch66:149–155、相邻/证据注后写后通过。不能据此宣称真实欺骗已消除或模型内部最大能力已证明。

### [2604.22127v1 Where Should LoRA Go? Component-Type Placement in Hybrid Language Models](https://arxiv.org/html/2604.22127v1)

§3–5 的受控比较显示 adapter 的 target identity 不能只有层位：recurrent/attention 组件在串行或并行混合块中的路径不同，最优经验选择可反转。Ch30 已在 placement 主线补组件类型、实际挂载路径与同预算验收；固定 rank 不代表训练参数量或更新计算匹配，sub-1B、单 seed 和有限任务不支持通用 attention-only 排名。书稿已由[非作者按原文与邻接写后核验通过](../_sources/daily-20260427/V3_APR01_ROOT_WRITE_AFTER_INDEPENDENT.md)。

### [2604.22509v1 LaissezCloud: Continuous Resource Renegotiation for the Public Cloud](https://arxiv.org/html/2604.22509v1)

§2–5 的 tenant/operator 双方私有状态与运行中 allocation 重议，让出价只成为受限资源 proposal，运营方仍拥有仲裁、硬安全及回收权。Ch63 已在 quota/reclaim 主线补此条件分支；8–23% 属 trace/profile 模拟，价格不等真实效用、隐私或全局公平，高重配置成本仍应回退固定 quota/FCFS。书稿已由[非作者按原文与邻接写后核验通过](../_sources/daily-20260427/V3_APR01_ROOT_WRITE_AFTER_INDEPENDENT.md)。

### [2604.22438v1 SSG: Logit-Balanced Vocabulary Partitioning for LLM Watermarking](https://arxiv.org/html/2604.22438v1)

§4–5 揭示 keyed green/red 分组按词数等分时，高概率 token 可聚到同侧，低熵位置几乎无可移动的检测质量。Ch72 已补单 bit 注入侧概率质量边界和模型/tokenizer/context/候选集的重放身份；论文的全词表配对理论界不能直接套 top-k 实现，无原 prompt 与 paraphrase 切片也有反向结果。书稿已由[非作者按原文与邻接写后核验通过](../_sources/daily-20260427/V3_APR01_ROOT_WRITE_AFTER_INDEPENDENT.md)。

### [2604.22550v1 ArmSSL: Adversarial Robust Black-Box Watermarking for Self-Supervised Learning Pre-trained Encoders](https://arxiv.org/html/2604.22550v1)

§III–VI 区分直接看 encoder embedding 与经下游分类头只能看 confidence vector 的归属接口；水印形成的 OOD 密簇也可能被攻击者定位/移除。Ch72 已补可观察 API 身份与这一反向攻击面，不能称统计探针为法律权属或发行链证明。主表冻结 encoder、64 负例观测零误报非总体 FPR 零，`ψ=.1` 自适应移除有约 20% 效用损失。书稿已由[非作者按原文与邻接写后核验通过](../_sources/daily-20260427/V3_APR01_ROOT_WRITE_AFTER_INDEPENDENT.md)。

### [2604.22291v1 Train in Vain: Functionality-Preserving Poisoning to Prevent Unauthorized Use of Code Datasets](https://arxiv.org/html/2604.22291v1)

§2–5 在 Java 代码的执行路径插入所测条件下运行无副作用、却改变 next-token 训练监督的片段：编译和功能测试通过并不足以判定训练效用安全。同模板 DeadBranch 对照在 10% 污染下，clean fine-tuned Pass@1 `.38`、FunPoison `.20`、dead branch `.38`；这是所测 CodeLLM/Java 微调设置的差异，不是任意语料和训练规模的保证。Ch27 已补训练数据准入的功能验收与监督效用分账；攻击配方不入书，实际写后已由[非作者核验通过](../_sources/daily-20260427/V3_APR01_ROOT_WRITE_AFTER_INDEPENDENT.md)。

### [2604.22228v1 Accelerating Intra-Node GPU-to-GPU Communication Through Multi-Path Transfers with CUDA Graphs](https://arxiv.org/html/2604.22228v1)

§4–5 的多路径 payload 分片与 CUDA Graph launch/replay 分别支付路径完成、capture/buffer 成本；四 GPU NVLink/PCIe OMB 不证明 collective 或训练端到端收益。Ch36 原段已给两条收益与单路径/non-Graph 回退；本轮把 source-family `:end` 移到本篇两段后、下一篇 NIMBLE 之前，[非作者修后写后核验通过](../_sources/daily-20260427/V3_APR01_ROOT_WRITE_AFTER_INDEPENDENT.md)。

### [2604.22312v1 Guess-Verify-Refine: Data-Aware Top-K for Sparse-Attention Decoding on Blackwell via Temporal Correlation](https://arxiv.org/html/2604.22312v1)

§4 在 `K≤f(T)≤C` 时先验证候选包含真实 Top-K，再在候选超过 K 时正常 refine；容量条件找不到时才回退。Ch49 旧实写曾把 refine 错说成验证失败，本轮已改正并获[非作者修后写后核验通过](../_sources/daily-20260427/V3_APR01_ROOT_WRITE_AFTER_INDEPENDENT.md)。Blackwell、约 60KB/CTA、时序相关和低相关输入的反向成本保留，不从局部 kernel 指标推出普遍解码 SLO。

### [2604.22753v1 Spend Less, Fit Better: Budget-Efficient Scaling Law Fitting via Active Experiment Selection](https://arxiv.org/html/2604.22753v1)

§4.2/Alg.1 从可负担候选中按目标区预期信息增益相对 `c(x)^α` 成本惩罚评分，不是绝对不确定性降幅最大优先。Ch28 的 pilot 段已补这一条件、mixture/one-step/cost proxy 限制和固定网格回退；原 V2.1 句子遗漏成本项，本轮修后获[非作者写后核验通过](../_sources/daily-20260427/V3_APR01_ROOT_WRITE_AFTER_INDEPENDENT.md)。

### [2604.22662v1 Rethinking XAI Evaluation](https://arxiv.org/html/2604.22662v1)

官方 exact-v1 §2–5 在统一 amortized 计算、固定界面和无解释对照下，比较八类 Shapley 语义及 37 人、3,735 次 tabular risk case review；定量解释 proxy、人类清晰度/信心、客观判断准确率与审查时延不是同一指标。若干解释条件提高主观信心，但未给稳定客观绩效改善，不能因此断言所有解释无效。Ch66 已把 attribution 的对象、受众、evidence/scorer 和发布权分开；此研究提供受限的人类行为反例供评价设计参考，但不能凭表格风控实验给 LLM/Agent 解释新增通用保证或直接写 Books。本次按[非作者准入复核](../_sources/daily-20260427/V3_ROOT_22662_REVERSE_ADMISSION.md)撤销旧“仅 measurement/context”前关闭，标准完成、仅报告。

### [2604.22504v1 Objective Shaping with Hard Negatives](https://arxiv.org/html/2604.22504v1)

官方 exact-v1 §2–4/App A 在受约束物品词表、单目标物品、二元 reward 下，把随机负物品、beam 困难负物品和 windowed partial AUC 的采样分布与隐含 pairwise surrogate 区分。有限 beam 不等于精确 top-tail 目标；WPAUC 与 Recall@K 的联系只在单正例和指定窗口下成立。四个推荐数据集及小模型不能推出一般 GRPO/AUC 定理或线上 Top-K 收益；困难负样本另有计算、覆盖偏差和 false-negative 成本。Ch33 已有 prompt/组采样与 reward 信息量的长期判断，本特例不宜上升为通用书稿机制；本轮按[非作者反向准入复核](../_sources/daily-20260427/V3_ROOT_22504_REVERSE_ADMISSION.md)撤销旧“推荐任务局部”泛化关闭，标准完成、仅报告。Submitted 04/24 只为投稿；相邻 22503/22505 的 v1 Updated、DOI 初建及本项 OAI/官方 Sunday 公告规则共同只支持 04/27 08～09 北京时间的有据组合推断，非逐篇首发日志。

### [2604.22678v1 BERAG](https://arxiv.org/html/2604.22678v1)

exact-v1 §3 Eqs.2–6/§4.8 Table 6 把每篇检索文档变为独立生成分支，在共同 prefix 下用 token likelihood 更新分支权重并剪枝；后验权重不等于事实支持概率。Ch76 原有集合检索和答案 Gate 未承载这一执行状态，root 已窄写于 ResRank 后，并获[apr02 非作者实际写后 PASS](../_sources/daily-20260427/V3_APR02_CH76_UAE_BERAG_WRITE_AFTER.md)。E-VQA K=50 下 naive 分支 470.2、普通拼接 203.0、Top-P 44.4 ms/token 是受限 decode 对照，不能称端到端普遍更快；重复 query/prefill、多个活跃 KV 分支和误剪风险仍要与普通拼接回退共存。

### [2604.22709v1 Abstract-CoT](https://arxiv.org/html/2604.22709v1)

exact-v1 §3–4/Tables 1–2 在语言 CoT bottleneck SFT、prompt-only self-distillation warm-up 后，以 constrained GRPO 训练保留词表中的离散隐码与答案；cold RL-only 表现差。Ch33 原有 SFT→RL 和 token credit 未承载这种训练前置的隐状态责任，root 已在多阶段训练论证内窄写，并获[apr20 非作者实际写后 PASS](../_sources/daily-20260427/V3_APR20_22709_CH33_WRITE_AFTER_INDEPENDENT.md)。已测输出 token 减少不能抵销约 600k SFT、1M RL episodes 与额外硬件训练成本；Qwen3-8B 数学质量有反向切片，隐码不拥有可审解释或正确性真值。

### [2604.22722v1 UAE](https://arxiv.org/html/2604.22722v1)

exact-v1 §2.1–2.2 Eqs.1–5/§3 Table 1 把指定 reader 对已知答案的离线效用，经 pairwise reward proxy 与 softmax KL 蒸馏到仍可线上 ANN 的双塔检索器。Ch76 原有 reader-outcome 评价不等于这一训练目标/索引版本责任；root 已在 Reranking 开头窄写，并获[apr02 非作者实际写后 PASS](../_sources/daily-20260427/V3_APR02_CH76_UAE_BERAG_WRITE_AFTER.md)。QASPER R@1/Gen-F1 48.15/27.0 低于 SePer 59.84/32.6；9 ms 只计该检索阶段，不包括 teacher、索引重建与最终 reader，答案效用也不是证据充分性真值。

### [2604.22171v1 MCI](https://arxiv.org/html/2604.22171v1)

exact-v1 §3–4 用无谓词的 clique-cover 索引近似密邻接，查询时再施加任意谓词，并用多 seed 缓解过滤诱发的子图断连；这给 Ch76 可信 ACL 前筛、稳定 RBAC 分区与 SSD superset traversal 之间增加一个有条件的物理索引选择，不把索引本身升格为授权决策者。[定点反向准入审计](../_sources/daily-20260427/V3_APR01_22171_MCI_REVERSE_ADMISSION.md)与 root 实际 Ch76 比较已支持窄 Books 写前采用。§5 仅 CPU/L2、合成 Zipf 标签下的 Recall@10/QPS；ACORN 在部分低召回点更快，极高召回的 beam/QPS 代价陡增；昂贵谓词评估和 Appendix A 未实证的动态更新都阻止把它写成已验证 ACL churn 或生产 RAG 优势。root 已按此分支窄写 Ch76，并获[非书稿作者实际正文、相邻和章末证据写后 PASS](../_sources/daily-20260427/V3_APR01_22171_CH76_WRITE_AFTER.md)；本项计真实 Integrate，未据此判整日 Gate。

## 5. 缺口与下一步

**普通 Books 与日级可执行待办均已清零。** `2604.22678v1` BERAG、`2604.22709v1` Abstract-CoT、`2604.22722v1` UAE 与否定侧恢复的 `2604.22615v1` GazeVLA、`2604.22169v1` ReCast、`2604.22464v1` MADE-IT、`2604.22171v1` MCI 均已完成真实书稿整合及非写入者的实际写后复核，现列 §3/§4。来源、日期、准入、证据和 Books 已经[非作者日级验收](../_sources/daily-20260427/V3_ROOT_DAILY_GATE_20260427.md)；下文仍区分外部保留项与全站无遗漏断言。

`2604.22167v1` 原列已有覆盖，但[非作者八项审计](../_sources/daily-20260427/V3_EXISTING_INDEPENDENT_AUDIT.md)指出 Ch66 只明确固定输入下的输出尾险，论文 §6.1–6.2 还提供 query/paraphrase 分布与每个输入的尾险组成的双轴评价分母。root 已在 Ch66 Rare Failure Evaluation 段后窄整合，列于 §3，且已获[作者外实际写后复核通过](../_sources/daily-20260427/V3_APR01_ROOT_WRITE_AFTER_INDEPENDENT.md)，计入当前 33 项已通过 I。30/70 拆分仍出自同一 309-base-query 改写池，不能说验证了未见 base query 或真实流量。原八项 Existing 中另七项的有限逐篇复核已通过，其中 SpikingBrain2.0 同时对照 Ch22 与 Ch49；这仍不是日级 Gate。

否定侧恢复的 [`2604.22438v1` SSG](https://arxiv.org/html/2604.22438v1) 与 [`2604.22550v1` ArmSSL](https://arxiv.org/html/2604.22550v1) 各获 apr20 具名[独立审阅](../_sources/daily-20260427/V3_APR20_SSG_INDEPENDENT.md)与[第二项审阅](../_sources/daily-20260427/V3_APR20_ARMSSL_INDEPENDENT.md)，并已由 root 在 Ch72 分别补入低熵单 bit 概率质量与下游黑盒归属/OOD 密簇风险；两项均获[作者外实际写后复核通过](../_sources/daily-20260427/V3_APR01_ROOT_WRITE_AFTER_INDEPENDENT.md)。Submitted 04/24 不等首发；各自 v1 Updated、OAI、DOI 原字段、连续相邻 ID 和[官方公告/赋号规则](https://info.arxiv.org/help/availability.html)共同只支持 04/27 08～09 北京时间的有据公告推断，不冒称逐篇日志，详细值见[筛选记录](../_sources/daily-20260427/V3_SCREENING_NOTES.md)。

上述三项现已列入 §3，普通 Books 待办为 0。`22167/22127/22509/22438/22550/22291` 已获[非作者实际写后复核通过](../_sources/daily-20260427/V3_APR01_ROOT_WRITE_AFTER_INDEPENDENT.md)并列 §3。旧写入 `22228/22312/22753` 的三处语义/来源绑定问题也经定点修正和[非作者修后写后核验](../_sources/daily-20260427/V3_APR01_ROOT_WRITE_AFTER_INDEPENDENT.md)，现列 §3 而非继承旧 V2.1 标签。旧写入的 `22038/22082` 已由 apr02 非作者本轮按实际正文和原文写后通过，现列 §3 而非凭旧标签继承。七项已有覆盖已获[非作者单篇实际对照通过](../_sources/daily-20260427/V3_EXISTING_INDEPENDENT_AUDIT.md)。arXiv 408 原始身份的排除侧已按来源/主题/共享理由做题摘级反查与具名分层抽检，不将全部 raw 转全文；日期组合链及14源的精确限制在日级 Gate 核对。

**本窗安全隔离、只按具名材料重开：** `2604.22136v1` Eq16 执行对象身份零信息保证有反例，需作者修改保证对象及补充真实执行动作的独立性条件/证明；`2604.22152v1` 的 HTML `/v1` 与 April abs/v1 日期/正文身份不一致，且官方 PDF v1 未可读，需可读原版 PDF 或同期同版方法/评价材料。两项均不支撑正面 Books 或性能/安全结论。OpenAI Research Index 尚未可靠翻到本窗、Meta Publications 已见跨窗邻界但 Research 其它子入口未覆盖、Google Publications 等历史目录的精确限制见 §2；只有获得可按本窗回溯的官方目录、原始日期/版本材料，才重开对应入口，不对整日零遗漏作无依据宣称。

上述两项争议及未可回溯的机构历史子入口均为**终态保留项**，不是普通待审。它们不用于正面证据、Books 或无遗漏断言；定点重开条件分别是同版证明/原始正文和带本窗原始日期的官方历史目录或具名同期材料，只重开受影响家族及来源。

旧实写修正终态：`22312` 原句把候选数 `>K` 的正常精确 refine 误说成验证失败，`22753` 原句遗漏成本惩罚，`22228` source-family end 越界；root 已分别窄修，非作者[逐处复读 actual body、相邻与 exact-v1 后 PASS](../_sources/daily-20260427/V3_APR01_ROOT_WRITE_AFTER_INDEPENDENT.md)。三项已从普通待办转 §3 实际 Integrate；整日 Gate 另有独立记录。

**窗外但不扩本窗：** 04/27T06Z OpenAI 微软合作、04/27T12Z MiniMax 中文 Agent Team、04/28T10+08 Qwen 动态研究列表下一条分别归属后窗；DeepSeek V4 Preview 04/24 早家族不按 PDF 印刷 04/27 重报。本次不顺带生成 Weekly 或其它日期。

## 6. 复核

复核者：root（非报告作者；复用具名单篇非作者审阅，并独立检查整日来源、日期、准入、证据与 Books）
结论：通过

[日级语义 Gate](../_sources/daily-20260427/V3_ROOT_DAILY_GATE_20260427.md)记录检查范围与结果；外部入口与两个争议家族按 §5 精确隔离，不支持全网无遗漏或正面 Books 保证。

否定侧恢复的 11 项 `22438/22550/22291/22662/22504/22615/22236/22442/22169/22464/22171` 分别保留在[本轮共享理由子集审计](../_sources/daily-20260427/V3_GENERIC_LOCAL_METHOD_SUBSET_AUDIT.md)及各单篇证据；[MCI 定点审计](../_sources/daily-20260427/V3_APR01_22171_MCI_REVERSE_ADMISSION.md)与 root 实际 source→Ch76 判断确认不能再按“数据库局部方法”前闭。官方公告规则、相邻 ID、OAI 与 DOI 原字段只给这 11 项本窗日期的有界推断，已列冻结候选第 36～46 项。其中 7 项 `22438/22550/22291/22615/22169/22464/22171` 已窄写并获非写入者实际写后复核；`22662/22504/22236/22442` 仅报告。单篇准入与整日日期核的范围不同；恢复证据见[日内证据表](../_sources/daily-20260427/V3_EVIDENCE_REVIEW.md)。

独立复核范围包括：33 项实际 Books 正文/相邻段落写后（见前述各单篇证据）、七项真实 Existing 对照、三项 `22436/22050/22708` 贡献前分母关闭、11 项具名否定侧恢复、`22136` Eq16 二元反例，以及 root [否定侧分层补核](../_sources/daily-20260427/V3_ROOT_NEGATIVE_STRATIFIED_FOLLOWUP.md)的四项具体关闭。正式[46项证据记录](../_sources/daily-20260427/V3_EVIDENCE_REVIEW.md)、[筛选记录](../_sources/daily-20260427/V3_SCREENING_NOTES.md)、[158项同理由反查](../_sources/daily-20260427/V3_GENERIC_LOCAL_METHOD_SUBSET_AUDIT.md)与[14源记录](../_sources/daily-20260427/V3_SOURCE_DISCOVERY.md)已在[独立日级 Gate](../_sources/daily-20260427/V3_ROOT_DAILY_GATE_20260427.md)对账。旧 V2.1 的 Complete/Passed 未参与本轮结论；机器校验结果及全量 cached diff 的既有噪声边界见 Gate 记录。

Tencent-Hunyuan 组织入口另作有限补查：当前公开目录 83 仓库，按 `pushed_at` 与本项目主题挑出的 13 个主线仓库在本窗默认分支查询均无可见 commit，当前 Releases 全空、12 个无 tag，HunyuanVideo 唯一 tag 指向 2024 commit。先前另外六个窗前相邻仓库 release 请求被 GitHub 限流，本轮额度恢复后六份均返回完整空数组；旧限流已不作未决。当前快照仍不能证明已删/改权限、非默认分支或站外历史无发布，故来源仅按这些层得有界阴性，余缺口精确隔离为 `受阻` 而非组织零更新，详见[来源发现记录](../_sources/daily-20260427/V3_SOURCE_DISCOVERY.md)。
