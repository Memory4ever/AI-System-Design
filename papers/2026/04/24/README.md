# Daily Research — 2026-04-24

**规范：** V3
**窗口：** 2026-04-23T09:00:00+08:00 ～ 2026-04-24T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-30T16:39:12+08:00

## 1. 结论

本次重要线索集中在可训练历史状态、稀疏读取、评价分母与保护边界：有限后续行为对齐不等任意未来记忆恢复；训练 gist 的读取预算不等原 KV 驻留；测试标签跨题回流、必要信息传达与泄漏平均值不能再当独立单题成功率。本窗二十九项长期差异已经进入真实章节正文，并有非作者写后核验；不是章末增加“已吸收”标记。

实际漏斗为496唯一标题有界查漏、162相关/含糊题摘语义筛选；宽951 submitted API库存不是本窗新论文。原100工作项中，独立复核将20897、21203、21265、21461、21592、21677、21772、21776判为只有类比、局部算子/应用 operating point、已有分层诊断或未隔离归因，缺本项目可保留的长期设计增量；CSC 21416 也因只验证通用图像分类器的投毒防护、未建立大模型或其 Infra 的直接增量，转具名前分母关闭。再经[反向准入校准](../_sources/daily-20260424/V3_ROOT_REVERSE_ADMISSION_RAMEN_PRISMADV.md)，Ramen与PrismaDV的局部算法/通用数据工程反馈也转具名初筛关闭；[HAT-VTR 反查](../_sources/daily-20260424/V3_ROOT_HAT_VTR_REVERSE_ADMISSION.md)及[两项局部探针反查](../_sources/daily-20260424/V3_ROOT_TWO_THEORY_PROBE_REVERSE_ADMISSION.md)纠正原收据与正式稿间的准入冲突。[SPIRE 日期反证](../_sources/daily-20260424/V3_ROOT_SPIRE_FIRST_PUBLIC_CORRECTION.md)证明同族材料最迟已在04/06公开，不再算本窗首次公开。原始证据留在 `_sources`。现为84 arXiv家族加GPT模型/card一家族的**85冻结候选**，不是85项已证实贡献：作者必要审阅44深入、26标准、15中心争议；处置为29项本窗真实整合、0普通Books待办、10已有覆盖、31仅报告、15争议暂缓。SPIRE 的 Ch76 机制文字保留为已核来源支持的书稿内容，但不再计入04/24日报产出。日级独立复核已完成，全部85家族获得安全终态处置；外部限制仍隔离，不声称所有来源可核或所有论文主张成立，不继承旧V2.1 Complete。

日期使用[arXiv官方公告规则](https://info.arxiv.org/help/availability.html)、永久ID公告赋号、相邻批次和精确v1处理簇的组合，有限推断其余arXiv工作候选公开范围为04/24 08:00～09:00；并非把Submitted、Updated、OAI或DOI created改名为首次公开，也不是逐篇公告日志确证。22日期例外、SPIRE窗前同族和DeepSeek相交日历日单项另列，不强推整批落窗。必要方法/反证读足即停，未复现实验、未验证生产SLO。

旧正式稿已[逐字无损归档](../_sources/daily-20260424/V2_REPORT_ARCHIVE.md)，两文件归档时SHA-256相同；原始证据保留。本文只更新本日，不借旧Weekly扩池，也不重跑其它日期。

## 2. 来源覆盖

本表自包含实际入口/停点与限制，原始依据见[机构窗口记录](../_sources/daily-20260424/V3_INSTITUTION_NOTES.md)、[题摘与日期记录](../_sources/daily-20260424/V3_SCREENING_NOTES.md)。已检查仅表示这些约定入口/主题被有界处理，不表示全站无遗漏；受阻项已具名隔离，不能借此掩盖尚可执行的候选/Books工作。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [News RSS](https://openai.com/news/rss.xml)1230项；相邻04/22→04/25；GPT公告/card 04/23T11:00Z、Academy10:00Z。必要card§7.2已读；两GPT条目合一家族、指南具体关闭。 | 受阻 | RSS不替Research/Index历史分页；未取得不可变原版card全稿，后发API/生物改动不回填。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)原始publishedOn：04/22T14:12:30.673Z、14:27:03.434Z→04/29T20:26Z；此公开目录本窗无条目。 | 已检查 | 无；结论仅限可见研究目录。 |
| SRC-GOOGLE-AI | [Research April](https://research.google/blog/2026/04/)9条04/29→22→21→16→…03；DeepMind April页3七日期04/30/27/23/22/15/14/02；DiLoCo原文与21428同族。 | 受阻 | Research Publications year2026本窗历史停点未恢复；博客日历日不独证首发时刻。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)实际空正文；April Blog邻界不是Research完整停点。 | 受阻 | 本窗研究历史列表/相关artifact目录不可核；不称零研究。 |
| SRC-QWEN | 官方api/page_config?code=research.research-list静态60项≤2025；api/v2/article/retrieval动态40项，04/22T10+08→04/28T10+08；公开concat列表本窗无项，组织58仓库无next。 | 已检查 | 组织created仅是新artifact线索，不覆盖旧仓库所有release或私有转公开。 |
| SRC-DEEPSEEK | [News](https://www.deepseek.com/news/)Sep10→Apr24 V4-preview→2025Dec1；Research June24→Feb25→Jan28；官方preview/card/Transparency已定点读；39仓库无next。 | 受阻 | V4-preview仅Apr24日历日，缺09点前可得上界；单项DATE-DEEPSEEK-V4-PREVIEW-APR24隔离。 |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog)26条最新2025Nov7；官方组织43仓库created倒序无next。 | 受阻 | 旧Blog首屏不能证明2026历史覆盖；旧仓库release/私有转公开未覆盖。 |
| SRC-TENCENT-HUNYUAN | POST api.hunyuan.tencent.com/api/blog/publicList：pageNum1,pageSize100,renderType0，9/9；displayPublishTime1776873600=04/23T00+08→04/30T15+08；全部可见目录无本窗项；83仓库无next。 | 已检查 | Hy3不因页面Apr23日历日进入09点后的窗口；目录外未列论文不作零断言。 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)raw200恢复15 rendered cards；May20→Apr29→Apr7→Apr1→Mar15，本窗无目录项；53仓库无next。 | 已检查 | createAt/媒体收录不冒充公开时刻；旧release/public转换仍有限制。 |
| SRC-BYTEDANCE-SEED | GET api/get_article_list_v2，x-tt-locale:US，type1 page0+20/count20,total242,next40：04/26→04/23T00+08→04/22；type2 total95/page0+20已到2025，邻06/19→04/23→04/09→04/01；63仓库。 | 已检查 | 21921有早目录线索及午夜日期粒度，单族公开归属隔离；SimArt仅既有家族artifact组合关闭。 |
| SRC-BAIDU-ERNIE | [中文Blog](https://ernie.baidu.com/blog/zh/)raw200首10条，日期04/30T00Z→04/15T00Z→Feb06，本窗无可见条目。 | 已检查 | 仅公开Blog日期目录，不据此推作者/仓库全面零论文。 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)Paper8：June29→Mar13→Feb03；Blog14缺日期；组织18仓库；本窗MiMo-ASR/Skills核心说明已具体前分母关闭。 | 受阻 | Blog14日期不可得；created不证明首次public；未披露RL目标不据WER榜单采用机制。 |
| SRC-MINIMAX | EN Blog12日期May27/26→Mar18；CN Blog13 Apr27→Mar18；AgentTech可见May13；35仓库无next，公开列表本窗无项。 | 已检查 | 只限已读目录与新仓库线索，不推全部旧release无变化。 |
| SRC-ARXIV | 本日496唯一身份标题有界查漏、162相关/含糊完整题摘；12分类主线主题去重。官方ID公告赋号+Thu20EDT slot、相邻批次和精确v1簇支持当前84个arXiv工作候选家族08–09有据推断。 | 已检查 | 22具名日期例外及SPIRE窗前同族另列；951 submitted API库存不当公开批次，未宣称496全摘要/全文或全学科召回。 |

## 3. 候选与判断

本表为独立准入、日期与日级验收后的85家族冻结集合。公开范围为有据推断而非精确日志；原字段与时区在证据记录中。29项本窗必要Books增量已真实写入并通过非作者写后复核；10已有覆盖、31仅报告、15争议均有具体处置，普通Books待办为0。SPIRE已核文字保留，但不计本窗产出。来源、日期和中心争议限制按§5隔离，不支持全站无遗漏或通用性能/安全保证。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [2604.20987 Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks](https://arxiv.org/html/2604.20987v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | policy 与 Skill bank 双侧共适应，需要交叉冻结组合分离消费者和库升级。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [2604.21018 Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations](https://arxiv.org/html/2604.21018v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 测试答案标签跨题回流改变评价单位，输出 token 匹配不等完整反馈预算。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.21308 CI-Work: Benchmarking Contextual Integrity in Enterprise LLM Agents](https://arxiv.org/html/2604.21308v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 必需信息传达、敏感 entry 泄露和整例违规必须分别计数。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.21505 Assessing the Impact of Requirement Ambiguity on LLM-based Function-Level Code Generation](https://arxiv.org/html/2604.21505v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 开放需求的合法多解不能仅由原测试或输出冲突率判错误。 2+1+2=5 | 标准完成 | 已有覆盖：非作者命题复核通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.21159 Adaptive Instruction Composition for Automated LLM Red-Teaming](https://arxiv.org/html/2604.21159v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 组合特征 bandit 改变 red-team 搜索预算与迁移条件，embedding 多样性不等完整覆盖。 2+1+2=5 | 深入完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21232 ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures](https://arxiv.org/html/2604.21232v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 级联指标的 log 斜率与概率比定义不一致，影响保护曲线的解释。 2+1+2=5 | 争议 | 暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.20874 The Root Theorem of Context Engineering](https://arxiv.org/html/2604.20874v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 有限窗口不推出无限任务必须累积完整历史或压缩为唯一架构。 2+1+2=5 | 争议 | 暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21251 CAP: Controllable Alignment Prompting for Unlearning in LLMs](https://arxiv.org/html/2604.21251v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 固定 query 条件下确定 reference 的条件 MI 为零，跨 query 负例桥不成立。 2+1+2=5 | 争议 | 暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.20994 Breaking MCP with Function Hijacking Attacks: Novel Threats for Function Calling and Agentic Models](https://arxiv.org/html/2604.20994v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 工具描述可操纵 selection，但不等于获权执行或绕过 tool authorization。 2+2+2=6 | 深入完成 | 已有覆盖：非作者命题复核通过；AGENT-MCP [Ch83](../../../../books/part-07-agent/83-mcp.md) |
| [2604.21160 Reinforcing 3D Understanding in Point-VLMs via Geometric Reward Credit Assignment](https://arxiv.org/html/2604.21160v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | JSON geometry 字段 span 各自路由 group advantage，background credit 另分账。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [2604.21794 Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems](https://arxiv.org/html/2604.21794v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 上游 trace detach 与全 stage 梯度传播叙述冲突，端到端训练桥未统一。 2+2+2=6 | 争议 | 暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21829 Black-Box Skill Stealing Attack from Proprietary LLM Agents: An Empirical Study](https://arxiv.org/html/2604.21829v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 有限接口 skill 复述风险不独证非公开秘密来源，best-of-three 不等每请求成功率。 2+2+2=6 | 深入完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21725 AEL: Agent Evolving Learning for Open-Ended Environments](https://arxiv.org/html/2604.21725v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 快 bandit 与慢反思分工有受限可行性，冻结测试不等无限在线稳定。 2+1+2=5 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21741 Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training](https://arxiv.org/pdf/2604.21741v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 模拟失败状态 rollback/branch 的人类纠正片段需与真实执行验收分权。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [2604.21632 To See the Unseen: on the Generalization Ability of Transformers in Symbolic Reasoning](https://arxiv.org/html/2604.21632v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 未见 label 的 tied output 行仍受归一化/weight decay，影响新符号区分。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；MODEL-EMBEDDING [Ch12](../../../../books/part-02-model/12-embedding.md) |
| [2604.21686 WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/pdf/2604.21686v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 跨模型动作 adapter 与三类 proxy 评价值得报告，但不代表物理控制真值。 2+2+2=6 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21700 Stealthy Backdoor Attacks against LLMs Based on Natural Style Triggers](https://arxiv.org/html/2604.21700v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 长回答的 target-credit 选择性训练与风格 trigger 需绑定资产写权限和 sensor。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2604.21724 Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling](https://arxiv.org/html/2604.21724v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 频率分配、局部 n-gram 提取及层位注入共同决定 embedding 扩容的训练责任。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；MODEL-EMBEDDING [Ch12](../../../../books/part-02-model/12-embedding.md) |
| [2604.21590 AgenticQwen: Training Small Agentic Language Models with Dual Data Flywheels for Industrial-Scale Tool Use](https://arxiv.org/html/2604.21590v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 行为树路径扩展反推 environment/user/SOP，改变合成任务触发条件的职责。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [2604.21611 Process Supervision via Verbal Critique Improves Reasoning in Large Language Models](https://arxiv.org/html/2604.21611v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 文字 critique 对强弱 actor 的条件收益与额外 supervisor 预算不能混账。 2+2+2=6 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21571 Separable Expert Architecture: Toward Privacy-Preserving LLM Personalization via Composable Adapters and Deletable User Proxies](https://arxiv.org/html/2604.21571v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 可删除 proxy 隔离新增个性化资产，但不证明全管线遗忘或 base 无旧信息。 2+2+2=6 | 深入完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21579 A Metamorphic Testing Approach to Diagnosing Memorization in LLM-Based Program Repair](https://arxiv.org/html/2604.21579v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 语义变形下 repair 退化与 NLL 相关不独证训练泄漏或修复正确性。 2+2+2=6 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21593 Language as a Latent Variable for Reasoning Optimization](https://arxiv.org/html/2604.21593v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 语言 prompt 改变 RL 探索条件，不证明内部语言潜变量的唯一因果。 2+1+2=5 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21598 DryRUN: On the Role of Public Tests in LLM-Driven Code Generation](https://arxiv.org/html/2604.21598v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 无真实执行的代码 mental trace 与公共测试取舍，收益和调用预算依模型反转。 2+2+2=6 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.20902 Frequency-Forcing](https://arxiv.org/html/2604.20902v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | pixel/频率双流条件生成有局部分支，流身份与 block mask 的实现桥尚需澄清。 2+2+2=6 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.20933 IRIS](https://arxiv.org/html/2604.20933v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 自对弈 log-ratio 权重有条件机制；α 极限与印刷不等式不支持普遍等价。 2+2+2=6 | 深入完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.20911 Omission Constraints Decay](https://arxiv.org/html/2604.20911v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 格式规则随深度衰减是受限反证，不升级成凭据/执行安全阈值。 2+2+2=6 | 深入完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.20915 Absorber LLM](https://arxiv.org/html/2604.20915v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 有限后续 hidden-state teacher 对齐是历史吸收目标，不保证任意未来恢复。 2+1+2=5 | 深入完成 | 整合：实际正文及写后已通过；MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [2604.20920 Gist Sparse Attention](https://arxiv.org/html/2604.20920v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 训练 gist 用于 query 路由并保可展开 raw KV，active read 不等 resident bytes。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [2604.21428 Decoupled DiLoCo](https://arxiv.org/html/2604.21428v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | minimum quorum 与有限 grace 分离可用性及贡献权，保 staleness 和退步条件。 2+3+2=7 | 深入完成 | 整合：实际正文及写后已通过；TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [2604.20913 FairyFuse](https://arxiv.org/html/2604.20913v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 多子 GEMV 共享 ternary 解码是 LUT 之外执行分支，仍付 scale 与精度成本。 2+1+2=5 | 深入完成 | 整合：实际正文及写后已通过；INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [2604.20930 SafeRedirect](https://arxiv.org/html/2604.20930v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | prompt 失败许可不是 runtime hard stop，judge 剩余类别未取得安全证明。 2+2+2=6 | 深入完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.20854 ERA](https://arxiv.org/pdf/2604.20854v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | one-hot 标签使印刷 Dirichlet 参数全零，中心分布模型未定义。 2+2+2=6 | 争议 | 暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.20938 HARBOR](https://arxiv.org/html/2604.20938v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | Boolean Matérn 与仿射 Hamming 不等价，替代 surrogate 不能继承后验保证。 2+2+2=6 | 争议 | 暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21026 MCAP](https://arxiv.org/html/2604.21026v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 条件 top-k ranking 恢复界不等删层/低精度后的任务质量保证。 2+1+2=5 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.20932 Adaptive RAG Defense](https://arxiv.org/html/2604.20932v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 动态 hook/controller 与静态防线的协议差异，零 ASR 不推出开放安全。 2+2+2=6 | 深入完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.20917 The Path Not Taken / DexBench](https://arxiv.org/html/2604.20917v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | forward coverage 与逆输入生成的联合分数不证明同次内部因果理解。 2+1+2=5 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.20903 Sensitivity–Uncertainty Alignment in Large Language Models](https://arxiv.org/html/2604.20903v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 平均扰动、sup divergence 与 entropy 的风险桥有不等号/替换错误。 2+2+2=6 | 争议 | 暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.20904 Normative Simulacra](https://arxiv.org/html/2604.20904v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 正确和错置 norm universe 的差分 reward，训练 proxy 与规范授权分权。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [2604.20937 SToP](https://arxiv.org/html/2604.20937v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 累计 attention 仅是 sink 排名 proxy，不能识别短峰或无条件删除静态对象。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2604.20940 Sema](https://arxiv.org/html/2604.20940v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 客户端 codec/server 重建改变 placement，但离散 code 不等任意模型可直接理解。 2+2+2=6 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.20985 Differentially Private Model Merging](https://arxiv.org/html/2604.20985v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 随机发布一个 DP 资产与同时发布/参数合并的 privacy accounting 不同。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2604.20995 Value-Conflict Diagnostics Reveal Widespread Alignment Faking in Language Models](https://arxiv.org/html/2604.20995v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 受控 value-conflict 行为差异不识别持久价值、战略意图或自然总体比例。 2+2+2=6 | 深入完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21016 SGD at the Edge of Stability: The Stochastic Sharpness Gap](https://arxiv.org/html/2604.21016v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 梯度噪声与 restoring force 的条件 sharpness gap，不作通用 Adam 调参公式。 2+1+2=5 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21041 Projected Gradient Unlearning for Text-to-Image Diffusion Models: Defending Against Concept Revival Attacks](https://arxiv.org/html/2604.21041v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 局部投影保留等式不保证全网输出或未来任意微调不可恢复。 2+2+2=6 | 争议 | 暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21072 Distributed Generative Inference of LLM at Internet Scales with Multi-Dimensional Communication Optimization](https://arxiv.org/html/2604.21072v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 低带宽层位、microbatch、KV 联合预算，lossless 字节压缩不等量化。 2+2+2=6 | 标准完成 | 已有覆盖：非作者命题复核通过；INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [2604.21079 Foveated Reasoning: Stateful, Action-based Visual Focusing for Vision-Language Models](https://arxiv.org/html/2604.21079v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 同一 AR trajectory 内连续 foveation 动作头与 correct-only 面积目标分账。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2604.21083 Behavioral Consistency and Transparency Analysis on Large Language Model API Gateways](https://arxiv.org/html/2604.21083v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 行为 identity classifier 不是 backend attestation，计费 token 仍非独立证据。 2+2+2=6 | 深入完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21098 Propensity Inference: Environmental Contributors to LLM Behaviour](https://arxiv.org/html/2604.21098v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 随机环境因素给受限行为 effects，odds ratio 和意图因果份额不等概率。 2+2+2=6 | 深入完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21045 Hierarchical Policy Optimization for Simultaneous Translation of Unbounded Speech](https://arxiv.org/html/2604.21045v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | latency reward 质量门槛有机制，但所列 objective 与归一化实现未统一。 2+2+2=6 | 争议 | 暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21057 TRACES: Tagging Reasoning Steps for Adaptive Cost-Efficient Early-Stopping](https://arxiv.org/html/2604.21057v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | step 角色比例可作早停 sensor，gold forced-readout 不等线上已知正确。 2+1+2=5 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21100 Preconditioned DeltaNet: Curvature-aware Sequence Modeling for Linear Recurrences](https://arxiv.org/html/2604.21100v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 在线 ridge 的预条件写入几何改变线性状态更新，不保存全部历史 token。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [2604.21106 How Much Is One Recurrence Worth? Iso-Depth Scaling Laws for Looped Language Models](https://arxiv.org/pdf/2604.21106v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 固定执行深度下 recurrence 共享参数与训练 token/宽度预算必须分账。 2+1+2=5 | 深入完成 | 整合：实际正文及写后已通过；TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [2604.21131 Cross-Session Threats in AI Agents: Benchmark, Evaluation, and Algorithms](https://arxiv.org/html/2604.21131v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 跨 session 保护评价与 prefix sensor 受限，低召回不代表全部长上下文防御失败。 2+2+2=6 | 深入完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21139 Slot Machines: How LLMs Keep Track of Multiple Entities](https://arxiv.org/html/2604.21139v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | entity 信息可读出、交换干预和实际下游使用是三种不同命题。 2+1+2=5 | 标准完成 | 已有覆盖：非作者命题复核通过；WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2604.21164 MAGIC-TTS: Fine-Grained Controllable Speech Synthesis with Explicit Local Duration and Pause Control](https://arxiv.org/html/2604.21164v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 逐 token 时长/停顿控制有实现分支，但零与 missing 的输出区分未保证。 2+1+2=5 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21189 Full-Body Dynamic Safety for Robot Manipulators: 3D Poisson Safety Functions for CBF-Based Safety Filters](https://arxiv.org/html/2604.21189v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 连续表面 ε 覆盖与空间内缩才支撑几何安全，不由采样间距替代。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [2604.21192 How VLAs (Really) Work In Open-World Environments](https://arxiv.org/html/2604.21192v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 失败类按 task 出现与全事件频率不同，near-hazard/terminal/机会须分账。 2+2+2=6 | 深入完成 | 已有覆盖：非作者命题复核通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.21197 Toward Efficient Membership Inference Attacks against Federated Large Language Models: A Projection Residual Approach](https://arxiv.org/html/2604.21197v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 成员 span 可包含非成员表示，残差零不能确定训练 record 身份。 2+2+2=6 | 争议 | 暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21215 The Recurrent Transformer: Greater Effective Depth and Efficient Decoding](https://arxiv.org/html/2604.21215v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 同层历史输出 KV 与当前 temporary 输入 KV 分权，时间递归有并行代价。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [2604.21221 Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](https://arxiv.org/html/2604.21221v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 训练期同时覆盖 persistent/local cache 与稀疏 mask，pool proxy 不等细粒度真值。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2604.21229 EngramaBench: Evaluating Long-Term Conversational Memory with Structured Graph Retrieval](https://arxiv.org/html/2604.21229v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 结构图在 cross-space 与 aggregate 的收益反向，不形成 Graph 普遍优势。 2+1+2=5 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21241 CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors](https://arxiv.org/html/2604.21241v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 印刷 anchor/GT 同定义使 δ=0，正容忍 corridor 的桥未成立。 2+2+2=6 | 争议 | 暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21254 Hyperloop Transformers](https://arxiv.org/html/2604.21254v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | loop 边界而非每子层 mixing，需分执行深度与独特权重驻留。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；MODEL-TRANSFORMER-LAYER [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [2604.21255 When Agents Look the Same: Quantifying Distillation-Induced Similarity in Tool-Use Behaviors](https://arxiv.org/html/2604.21255v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 成功 tool 交集不是逻辑必需证明，行为相似性不能 attestation 训练来源。 2+1+2=5 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21268 Measure Twice, Click Once: Co-evolving Proposer and Visual Critic via Reinforcement Learning for GUI Grounding](https://arxiv.org/html/2604.21268v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | proposer/critic 的共同 proxy 训练是受限 GUI 操作点，不证明 critic 真值。 2+2+2=6 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21276 Do LLM Decoders Listen Fairly? Benchmarking How Language Model Priors Shape Bias in Speech Recognition](https://arxiv.org/html/2604.21276v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 全组 WER 很高可压缩差距，不能据此称 fairness 改善。 2+2+2=6 | 标准完成 | 已有覆盖：非作者命题复核通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.21327 Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning](https://arxiv.org/html/2604.21327v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 每 prompt 印刷 advantage 均值≤0 与后期正均值日志解释冲突。 2+2+2=6 | 争议 | 暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21330 Teacher-Guided Routing for Sparse Vision Mixture-of-Experts](https://arxiv.org/html/2604.21330v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 外部 dense feature 空间形成路由训练 proxy，teacher backbone 与 router 更新分权。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md) |
| [2604.21335 Sub-Token Routing in LoRA for Adaptation and Query-Aware KV Compression](https://arxiv.org/html/2604.21335v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | V 分组恢复与 query 联合 Top-M 是两分支，预测 query 信号不等已观察新 query。 2+2+2=6 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21343 Latent Denoising Improves Visual Alignment in Large Multimodal Models](https://arxiv.org/html/2604.21343v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | projector 后腐化、LMM 中间层恢复 clean 视觉 target 的训练责任。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2604.21346 Symbolic Grounding Reveals Representational Bottlenecks in Abstract Visual Reasoning](https://arxiv.org/html/2604.21346v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 特权生成程序提供接口诊断上界，不独证视觉 encoder 是唯一瓶颈。 2+2+2=6 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21361 Time, Causality, and Observability Failures in Distributed AI Inference Systems](https://arxiv.org/html/2604.21361v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 应用时戳负 span 与真实失败/吞吐不同，health 恢复不证明时钟恢复。 2+1+2=5 | 标准完成 | 已有覆盖：非作者命题复核通过；PLATFORM-TRACE [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [2604.21391 From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges](https://arxiv.org/html/2604.21391v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 条件独立起点 score 不推出 CFM 条件速度独立，anchor 必要性桥被反例否定。 2+2+2=6 | 争议 | 暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21395 Supervised Learning Has a Necessary Geometric Blind Spot: Theory, Consequences, and Minimal Repair](https://arxiv.org/html/2604.21395v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 协方差恒等式不保证 Gaussian 唯一性，条件 MI 与 TDI 上界桥也不成立。 2+2+2=6 | 争议 | 暂缓：中心主张争议；不入Books，定点重开见§5 |
| [2604.21326 MiMIC: Mitigating Visual Modality Collapse in Universal Multimodal Retrieval While Avoiding Semantic Misalignment](https://arxiv.org/html/2604.21326v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 融合点及缺 caption 的训练支持联合验收，latent TopK 不等语义独立。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2604.21275 Optimizing High-Throughput Distributed Data Pipelines for Reproducible Deep Learning at Scale](https://arxiv.org/html/2604.21275v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | worker 返回顺序与 shuffle seed 分权，正常路径确定性不等故障恢复。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [2604.21454 Reasoning Primitives in Hybrid and Non-Hybrid LLMs](https://arxiv.org/html/2604.21454v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 状态更新×检索两轴已有判断，Think/Instruction 推理预算并未匹配。 2+2+2=6 | 标准完成 | 已有覆盖：非作者命题复核通过；MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [2604.21477 MCP Pitfall Lab: Exposing Developer Pitfalls in MCP Tool Server Security under Multi-Vector Attacks](https://arxiv.org/html/2604.21477v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 静态 findings、动态 sink 和可信 predicate 的分母不能混为全部防御。 2+2+2=6 | 深入完成 | 已有覆盖：非作者命题复核通过；PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2604.21480 Efficient Agent Evaluation via Diversity-Guided User Simulation](https://arxiv.org/html/2604.21480v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 完整状态分叉节约有限模拟预算，定向失败率不等真实用户风险分布。 2+2+2=6 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21511 From Tokens to Concepts: Leveraging SAE for SPLADE](https://arxiv.org/html/2604.21511v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 倒排维度改为训练 latent 字典，并与检索目标联合更新，非 concept 真值。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [2604.21523 Seeing Isn't Believing: Uncovering Blind Spots in Evaluator Vision-Language Models](https://arxiv.org/html/2604.21523v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 三类 evaluator 指标对象不同，低失败率排序不直接证明更可靠。 2+2+2=6 | 标准完成 | 仅报告：受限机制/证据，不改长期正文 |
| [2604.21549 Unbiased Prevalence Estimation with Multicalibrated LLMs](https://arxiv.org/pdf/2604.21549v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 组内残差在重加权总体重新出现，prevalence 无偏依赖条件校准与支持重叠。 2+2+2=6 | 深入完成 | 整合：实际正文及写后已通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.21570 SpecSyn: LLM-based Synthesis and Refinement of Formal Specifications for Real-world Program Verification](https://arxiv.org/html/2604.21570v1) | 2026-04-24T08:00:00+08:00 ～ 2026-04-24T09:00:00+08:00 | 印刷 refinement 递推移除能区分 mutant 的 spec，中心过滤对象未一致。 2+2+2=6 | 争议 | 暂缓：中心主张争议；不入Books，定点重开见§5 |
| [GPT-5.5 公告与 System Card](https://deploymentsafety.openai.com/gpt-5-5) | 2026-04-23T19:00:00+08:00 | coding-prefix成对重采样与monitor漏检切片是受限评价，不独证未知风险或真实副作用。2+2+2=6 | 深入完成 | 已有覆盖：非作者命题复核通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

## 4. 证据与知识整合

### [2604.20987 Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks](https://arxiv.org/html/2604.20987v1)

2+2+2=6，真实知识缺口深入完成，实际整合 AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)的可训练 Skill 维护→独立 admission 主线。复用[apr02必要源→owner审阅](../_sources/daily-20260424/V3_APR02_COS_ICL_CAP_CI_INDEPENDENT.md) §3、§4.1–4.3、§5.2、Appendix F 和已完成 root 写后复核，本轮实际再读正文三段及相邻交接。action/retrieval 消费 bank，maintenance 改变下一轮消费输入；policy×bank 交叉组合区分两侧共适应与单纯累积。六游戏、8B 和五功能 LoRA 的有限对照未匹配 frontier 总训练预算，episode-end 与 skill-switch reward 粒度差异不补造统一 credit。正文保额外 rollout、维护与回归成本及冻结库/人工维护回退，不声明共同训练普遍更优，未复现。

当前Books处置：整合：实际正文及写后已通过；AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20987同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21018 Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations](https://arxiv.org/html/2604.21018v1)

2+2+2=6，评价知识缺口深入完成，实际整合 PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的 feedback-channel→长期 artifact 主线。复用[apr02必要源→owner审阅](../_sources/daily-20260424/V3_APR02_COS_ICL_CAP_CI_INDEPENDENT.md) §4.2、Algorithm1、§5及 root 实际写后通过；本轮再读正文两段及前后。ground-truth oracle 移除已解题并将成功回答回流同一 test pool，评价单位因而是有标签跨题适应序列，不是独立题或可部署 selector。正文 active set 与 Algorithm1 全 test pool 定义差异保留；四轮与一次 warmup、少数 API 模型不能推全配置改善。output-token 匹配不包含 ICL prefill、oracle 和池维护成本，无法恢复反馈/池状态时退回独立 snapshot，而不补造部署等价，未复现。

当前Books处置：整合：实际正文及写后已通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21018同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21308 CI-Work: Benchmarking Contextual Integrity in Enterprise LLM Agents](https://arxiv.org/html/2604.21308v1)

2+2+2=6，保护评价深入完成，实际整合 PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的任务必要传达×隐私→危险进展对照。复用[apr02审阅](../_sources/daily-20260424/V3_APR02_COS_ICL_CAP_CI_INDEPENDENT.md) §3–5.1、Appendix E及 root 写后通过，本轮再读正文与相邻交接。essential-entry conveyance、sensitive-entry leakage 与至少一次泄漏的 case violation 是不同分母；安全沉默不证明完成任务，平均 leakage 也不替代过程权限证据。125 seed 是25人工+100 Gemini-3-Pro 扩充，GPT-5.2用于后续场景/评价链路，不能改称其生成全部 seed；每例4+4 entries、五信息流方向只是受限模拟，不代表真实企业 incident 分布或独立 judge 真值。同源生成/模拟/评分限制及额外 judging 成本写入正文，未复现。

当前Books处置：整合：实际正文及写后已通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21308同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21505 Assessing the Impact of Requirement Ambiguity on LLM-based Function-Level Code Generation](https://arxiv.org/html/2604.21505v1)

2+1+2=5，标准完成，拟已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的开放需求/多种合法实现与“合法多解、缺少条件的不同动作”正文。实际补读§5.1–5.4/§6，与已读四类定义、§4.1三阶段人审结合：沿用原测试的Pass@k只能证明原始规范接受，不能把其它可合理解释的行为都判模型失败；conflict rate是在相同输入时实现输出不同，不是错误率。检测、定位、提出澄清选项是不同接口，GPT-4 judge的50人工样本96%agreement不足以给全部模型/歧义类型的真实识别保证，约50%precision也不能改写成可靠在线澄清Gate。

当前Books处置：已有覆盖：非作者命题复核通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21505同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21159 Adaptive Instruction Composition for Automated LLM Red-Teaming](https://arxiv.org/html/2604.21159v1)

2+1+2=5，安全评价预算触发深入必要审阅完成，拟仅报告。复用§4.1–4.3/Alg1后补读§5.1–5.4/§6–8：query/tactic embedding降维拼接，K500随机候选池上的小bandit适应成功反馈；成功组合去重，探索正则改变覆盖与局部成功的取舍。评价的受限方法差异成立，但embedding相似度/unique query计数不证明语义风险空间覆盖。三个目标模型、Mixtral攻击者和LlamaGuard训练judge，两个目标间迁移5Ktrial与本域10Ktrial区别；aggressive一种迁移仅保留原本56%表现，不承诺普适迁移。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21159同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21232 ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures](https://arxiv.org/html/2604.21232v1)

2+1+2=5，纠错深入必要审阅完成，拟中心评价定义争议/Books暂缓。复用已实际§3.1–3.5/AppD.1–D.3：action/subgoal/trajectory三个预测/重选接口和first-error后续风险的匹配观测并非因果干预。主文Eq6用log后错概率的负斜率，AppD.3用q(k)/q(1)；q1=.5、q2=.25分别得到ln2与.5，不能把两者当同一PAC指标比较恢复/级联曲线。EPR匹配也没有自动剥离困难样本选择。

当前Books处置：暂缓：中心主张争议；不入Books，定点重开见§5。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21232同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20874 The Root Theorem of Context Engineering](https://arxiv.org/html/2604.20874v1)

2+1+2=5，纠错深入完成，拟争议/Books暂缓；作者已读的§3–8必要推导和apr20非作者§3–7.6记录未变，复用[具名审计](../_sources/daily-20260424/V3_APR20_SIX_MINIMAL_ADMISSION_AUDIT.md)，不重读全部附件。给定填充条件的质量下降与有限窗口不蕴含任务次数增长时必须保留完整历史：有限canonical state加有界read-time检索可以完成无限重复任务而保持窗口有界。§7.3另加full-history累积条件，不能在§7.5省略后称压缩是唯一长期架构。§3的first-order linear fidelity也不是所有LLM的无条件单调定律。仅隔离这些中心普遍保证，保留60+session受限实例与压缩可能有效的经验，不由反例否定所有context研究。

当前Books处置：暂缓：中心主张争议；不入Books，定点重开见§5。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20874同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21251 CAP: Controllable Alignment Prompting for Unlearning in LLMs](https://arxiv.org/html/2604.21251v1)

2+1+2=5，纠错深入完成，拟中心理论争议/Books暂缓。复用作者§3.1–3.3、Eq1–4、AppB和[apr02实际非作者核](../_sources/daily-20260424/V3_APR02_COS_ICL_CAP_CI_INDEPENDENT.md)：固定benchmark query的reference A=a(Q)时H(A|Q)=0，I(Y;A|Q)=0；跨query reference负例没有成为固定q下p(a|q)的条件抽样，因此不能将InfoNCE式直接作为该条件MI随prefix变化的下界。B.2的embedding proxy也不是实际KL证书。只隔离条件MI解释与privacy-compliance保证，保留冻结模型、训练可撤销prefix的受限行为抑制接口和实验，不声称所有prompt效果不存在。

当前Books处置：暂缓：中心主张争议；不入Books，定点重开见§5。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21251同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20994 Breaking MCP with Function Hijacking Attacks: Novel Threats for Function Calling and Agentic Models](https://arxiv.org/html/2604.20994v1)

2+2+2=6，安全接口深入完成，拟已有覆盖：AGENT-MCP [Ch83](../../../../books/part-07-agent/83-mcp.md)“Tool Description是可执行的Discovery Interface”及“MCP不等于Tool Authorization”。实际§4/5、§6.3、§7–9：攻击方可修改一个已列工具的description，不能改user query；离线梯度搜索作用于所测模型，转移评价另有边界。这证明tool-selection surface可由描述变化操纵，不证明未获权限的工具已执行或任意black-box系统都可破。名字命中与带参数完整调用不是同一ASR，BFCL-v3 multiple 200题/2–4工具与五模型有限配置不外推总体生产风险。

当前Books处置：已有覆盖：非作者命题复核通过；AGENT-MCP [Ch83](../../../../books/part-07-agent/83-mcp.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20994同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21160 Reinforcing 3D Understanding in Point-VLMs via Geometric Reward Credit Assignment](https://arxiv.org/html/2604.21160v1)

2+2+2=6，真实知识缺口触发深入必要审阅完成，TRAIN-GRPO Ch33窄分支已实际写入并获root非作者写后通过。实际重开§3.3–3.5/Eq6–16、§4.2/Table3与§4.5：JSON字符span按累计解码offset回到token index，四geometry field各自产生group-relative advantage，仅路由本字段span；语义/格式background另接平均字段advantage与RPC混合。RPC比较预测3D投影与预测2D，相互一致不是独立几何真值；KPA是落入GT box的containment，不是关键点坐标逐一正确。解析/char-token对应、字段group support及background混合是不同于完整回答reward或集合Shapley span的具体训练接口。

当前Books处置：整合：实际正文及写后已通过；TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21160同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21794 Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems](https://arxiv.org/html/2604.21794v1)

评分2+2+2=6，纠错触发深入审阅，拟中心实现/保证范围争议、Books暂缓。实际读exact-v1 Figure1、§3.1–3.4、§4.1–4.2、§6、AppendixA/C/D：四顺序Agent将固定数量latent KV片段追加到共享trace，不覆写旧片段，最终输出的teacher-forced CE只更新LoRA而base冻结。但Figure1写上游trace构造without gradient updates、只更新最终Agent的LoRA；§3.3及AppendixC却写梯度跨全部stage、联合训练上游编码与下游解释。共享参数在最终stage更新也可能改变上游下一次forward，并不等于梯度实际经过本次上游计算；必要实现图、detach位置和参数共享/优化清单未统一，不能将本稿直接作端到端joint training的正面实现依据。

当前Books处置：暂缓：中心主张争议；不入Books，定点重开见§5。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21794同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21829 Black-Box Skill Stealing Attack from Proprietary LLM Agents: An Empirical Study](https://arxiv.org/html/2604.21829v1)

评分2+2+2=6，保护行为触发深入完成，拟仅报告。实际exact-v1 §III、§IV-B–E、§V-A–D：公开用户/API权限无backend直接读取，但runtime读取skill后可在文本响应复述。主实验目标是公开的find-skills SKILL.md，不能以目标复现单独证明非公开秘密仅从当次runtime流出、厂商后端泄漏或版权归属；若要证明这些，需独立未知canary、启用/停用加载对照及访问trace。本稿120个自动生成probe和最多三次尝试支持有限接口风险，best-of-three不是每请求成功率。EM为规范化完整目标子串命中，ROUGE/embedding cosine不是泄露字节比例；target-aware模型judge也只是其语义sensor。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21829同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21725 AEL: Agent Evolving Learning for Open-Ended Environments](https://arxiv.org/html/2604.21725v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。实际§3–4：fast Thompson选择memory策略，slow窗口反思诊断并影响prompt；低pool reward条件下新增retrieval arm，默认planner/tool固定。训练/validation/test顺序划分，test全部bandit/memory/evolution冻结，不是无限在线稳定适应。208episode/10ticker/五seed，复杂planner/tool/credit等变体反退；反思文字称“causal insight”不构成唯一因果识别。先诊断再扩策略池有受限可行性，但小样本Beta历史、合成先验与模板偏差不能推出普遍稳定。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21725同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21741 Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training](https://arxiv.org/pdf/2604.21741v1)

2+2+2=6，真实训练/模拟状态缺口深入必要审阅完成。采用实际官方 PDF v1 §3.5/§4.1–4.4及Table2；HTML内部Aug24标签不作原始v1依据：policy在action-conditioned world model闭环，失败前状态缓存允许human短纠正后返还policy，同一模拟状态rollback/branch多次，纠正片段和真实演示合并posttrain。Ch26原有human在线RL与counterfactual proxy/real residual分权，现于其后补入“模拟失败状态复用→分支纠正片段→真实重新验收”的数据采集责任；不把模拟终态升为物理事实。具名[写前复核](../_sources/daily-20260424/V3_APR02_THREE_21632_21724_21741_INDEPENDENT.md)与[实际写后复核](../_sources/daily-20260424/V3_ROOT_FOUR_WRITE_AFTER.md)均通过；不代替日期或日级Gate。

当前Books处置：整合：实际正文及写后已通过；MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21741同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21632 To See the Unseen: on the Generalization Ability of Transformers in Symbolic Reasoning](https://arxiv.org/html/2604.21632v1)

2+2+2=6，知识缺口及理论限定深入必要审阅完成。实际§3–6、AppA/B/E：input/output tying使未作为label出现的softmax row仍受归一化梯度与weight decay，未见token的输出行差异可能收缩，从而损害多个新符号的区分；copy shortcut、冻结/reset及训练符号diversity分别改变读出、参数与数据支持，并非一个通用解决方案。Ch12原weight tying只讲共享参数，现于其后补入该训练支持压力及局部干预分支。具名[写前复核](../_sources/daily-20260424/V3_APR02_THREE_21632_21724_21741_INDEPENDENT.md)与[实际写后复核](../_sources/daily-20260424/V3_ROOT_FOUR_WRITE_AFTER.md)均通过；不代替日期或日级Gate。

当前Books处置：整合：实际正文及写后已通过；MODEL-EMBEDDING [Ch12](../../../../books/part-02-model/12-embedding.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21632同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21686 WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/pdf/2604.21686v1)

2+2+2=6，标准必要审阅完成，经非作者有限核仍仅报告。以官方PDF v1首页日期及§3.4/4为本次机制和实验依据：共享WASD/LR通过每模型adapter标定step/yaw，再在同场景/动作下比较六模型、三轴八指标。HTML `/v1` 的内部脚注却显示2026-08-24，与PDF v1首页的2026-04-24不一致，不能用HTML日期证明本窗版本；本次未从HTML引入PDF v1没有的后发结论。六模型/500cases、50参考场景及合成第三视角、20–60s有限协议不是所有world model能力。DROID-SLAM几何和Gemini3.1Pro判断仍是proxy，动作选择与评分共享VLM、adapter语义等价未有独立全域校准证明；有限人评rank相关不等真实物理控制真值。Ch25现有perceptual/geometry/action分权足以承担长期边界，本suite作为受限操作点报告，不称全算法已有覆盖。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21686同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21700 Stealthy Backdoor Attacks against LLMs Based on Natural Style Triggers](https://arxiv.org/html/2604.21700v1)

2+2+2=6，保护深入必要审阅完成，已在Ch72真实正文吸收窄训练/评价分支，root非作者写后通过。实际§III、§IV-A及C–F：有权修改隐藏system prompt或注入LoRA的提供方，用自然风格输入触发指定内容；这是资产/配置写权限威胁，不是普通用户仅靠低权限输入突破sandbox。长答案whole-response CE会稀释目标片段监督，另设poison强化/clean抑制target loss改变训练选择性。Ch72现有trigger邻域/强度矩阵未解释这一长生成target-credit分支。

当前Books处置：整合：实际正文及写后已通过；PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21700同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21724 Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling](https://arxiv.org/html/2604.21724v1)

2+2+2=6，知识缺口深入必要审阅完成。实际§4/§5.1–5.5：频繁token专用表、尾部频率平衡bucket/alias与多hash混合；局部causal ShortConv/SwiGLU重新提取动态n-gram，再按层注入value与residual。这不同于只把词表变大：更新频率分配、局部提取器与层位职责需共同验收。Ch12原静态hash容量/collision/skew与allocation frontier之后，现补入训练支持、局部提取和层位责任。具名[写前复核](../_sources/daily-20260424/V3_APR02_THREE_21632_21724_21741_INDEPENDENT.md)与[实际写后复核](../_sources/daily-20260424/V3_ROOT_FOUR_WRITE_AFTER.md)均通过；不代替日期或日级Gate。

当前Books处置：整合：实际正文及写后已通过；MODEL-EMBEDDING [Ch12](../../../../books/part-02-model/12-embedding.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21724同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21590 AgenticQwen: Training Small Agentic Language Models with Dual Data Flywheels for Industrial-Scale Tool Use](https://arxiv.org/html/2604.21590v1)

2+2+2=6，真实知识缺口深入必要审阅完成，已在TRAIN-DATA Ch27真实正文吸收，root非作者写后通过。实际复用§4及重新读§3.1–3.3/Algorithm1：linear轨迹先扩条件behavior tree，再选branch反推environment state/user instruction/agent SOP，令目标路径由条件变得必需；mock user可提出误导要求，正确branch需由环境/权限条件支持。这改变的是合成任务的触发条件与输入职责，而不是仅把旧题随机变难。Ch27 synthetic generator/judge同源错误、evidence-first真实trace反推QA已有；尚未明确“路径扩展→逆生成触发条件→三输入分权”的模拟数据分支，拟仅在synthetic compilation主线窄补。

当前Books处置：整合：实际正文及写后已通过；TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21590同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21611 Process Supervision via Verbal Critique Improves Reasoning in Large Language Models](https://arxiv.org/html/2604.21611v1)

2+2+2=6，标准必要审阅完成；[非作者有限复核](../_sources/daily-20260424/V3_ROOT_TWO_ONLY_FINITE.md)确认仅报告处置。实际§3–4.4，actor参数固定，supervisor step-level文字critique条件化再生成，非gradient policy update/可执行局部reward。所谓matched compute的SC@5只约五倍actor tokens且无supervisor；Reflexion同supervisor并限制outcome critique，但原文没有逐调用完整token/硬件成本matched证明。R=1–4非单调、强actor被critique后可低于standalone，r=.90只是有限model-pair相关，不证明headroom唯一因果或第四条普律。§3“ideal fixed point”无可验全局收敛条件，不采用收敛保证。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21611同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21571 Separable Expert Architecture: Toward Privacy-Preserving LLM Personalization via Composable Adapters and Deletable User Proxies](https://arxiv.org/html/2604.21571v1)

2+2+2=6，保护主张深入必要审阅完成，拟仅报告，待非作者核。实际§2–5：冻结base及共享domain LoRA，用户routing bias/steering/personal LoRA另存proxy，删除/旁路proxy后在有限heldout prompts比较基线分布。这个架构确实把新增个人适配的写入目标从共享权重移到可撤销资产；但不训练共享参数并不证明base原来没有该用户信息，也不覆盖merged副本、cache与日志。§2的KL阈值只是受限验证：§3四合成用户/四域、20prompts、140runs，§4约82–89%通过并非所有输出严格恢复；keyword style count及Jaccard相似都不是完整隐私或membership攻击验收。DP-SGD只是可兼容扩展，未取得端到端DP保证。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21571同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21579 A Metamorphic Testing Approach to Diagnosing Memorization in LLM-Based Program Repair](https://arxiv.org/html/2604.21579v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际§III–VI：自然/语义保持代码变换后比较test-adequate repair，原文件NLL percentile与SR差值作关联；§IV-A只以原始至少一轮能解决的bug为分母，闭源每prompt5patch而开源1patch，不是matched search预算。Defects4J广泛下降而GitBug-Java平均趋势弱，NLL相关只在四开源模型和低NLL半区；复杂度/项目/基准年龄与自然性仍可能共同影响。关联与变形敏感性不能单独确定训练泄漏、更不能给修复语义正确性。§IV-B最高NLL区域也会更脆弱，不能把所有下降归记忆。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21579同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21593 Language as a Latent Variable for Reasoning Optimization](https://arxiv.org/html/2604.21593v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。实际§3–5：同题五rollout，一条语言不约束、四条从language set抽语言prompt，规则answer+format reward、组相对归一化；在多语数学数据上改变探索条件，而非测得内部潜变量因果。语言受约束/不受约束配比和language set消融有局部机制证据，但100字符format条件不等跨语言同token工作，输出语言遵守及entropy又随训练改变，不能从较高早期entropy推出唯一增益原因或普遍最佳内部路径。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21593同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21598 DryRUN: On the Role of Public Tests in LLM-Driven Code Generation](https://arxiv.org/html/2604.21598v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际§3–5：去公共示例的spec先两轮无外部反馈plan refinement，再两轮自造输入/mental trace更新plan并重新生码，最后polish；这研究弱公共测试与自生成反思的条件差异，mental trace不是真执行。§4基于80道March2025后LiveCodeBench、两API模型minimal reasoning/三runs，消融仅gpt5mini的37hard；DryRUN和CodeSIM总体方向因模型反转，std重叠，既不是equivalence检验也非相同调用/token预算。去公共示例同时改变计划/循环次数与输入策略，不能唯一归因去测试；作者§5.3自己不主张据此删公共测试。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21598同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20902 Frequency-Forcing](https://arxiv.org/html/2604.20902v1)

2+2+2=6，标准必要审阅完成，拟仅报告/实现表述待澄清，不预先写Books。实际 §3.1–3.4/Eq1–5、Algorithm1、§4.1–4.3/Table2、§5：保留 pixel 插值，早成熟频率流作条件，learnable wavelet 与冻结副本另付训练成本。Ch24 分层 latent/连续路径尚没有此精确分支，但缺口不自动证明实现充分。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20902同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20933 IRIS](https://arxiv.org/html/2604.20933v1)

2+2+2=6；纠错深入必要审阅完成，拟仅报告，理论采用边界待非作者核。实际读§3.1–3.3/Eq4–10、§4.1/Table2–3、AppendixB.1–B.3/C.1。real与synthetic分别按log-ratio指数倾斜、batch内归一化，order调整改变梯度分配；不是普通chosen/rejected标签。Ch34当前Bradley–Terry pair-loss与reference坐标不包含此完整objective，但本轮不能把“统一所有self-play散度”或“α→1两边均uniform”写成长期事实：Eq8在α→1的synthetic weight仍为pθ/pold，不一般等1；population期望的该梯度可相消不等每样本uniform。Eq4后的Rényi等式缺α/(α−1)比例。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20933同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20911 Omission Constraints Decay](https://arxiv.org/html/2604.20911v1)

拟2+2+2=6，保护边界深入完成，作者提案**仅报告**，待非作者采用核。实际读exact-v1 §2.1–2.6、§3.1–3.5、§4.2–4.5：12模型、4416 trials只测8条任意格式规则；per-constraint纵向只四模型，ArmC只Gemini/Llama且不在主要易受影响组。ArmB/C平均482/620 tokens，未严格匹配，不能采用“唯一attention dilution因果”。正向incident-ID保持与no-bullet失败是受限独立反证，但不证明凭据/执行安全、模型架构成因或全provider。STD为六深度上50%格式通过率的插值，不是安全session阈值；reinjection段无独立防御验收。Ch72现有policy owner独立于code proposal（约733行）、白盒/黑盒接口区分（约674行）及guard-visible window（约1620行）已有长期执行边界，本项尚不足将格式proxy改成安全runtime设计规则；保留新受限观察而非声称原八约束实验全已覆盖。precision/batch/concurrency/SLO未披露；API身份部分未pin，非生产攻击复现。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20911同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20915 Absorber LLM](https://arxiv.org/html/2604.20915v1)

2+1+2=5，真实知识缺口深入完成，已实际整合 MODEL-LONG-CONTEXT Ch22，root 非作者写后通过。实读§3.1–3.3 Eq2–6/Alg1–2、§4.1–4.6：LoRA让无X的学生在有限后续Y上对齐full-context模型的hidden states，而非KV在线回归目标；滑窗把X吸收后继续Y。写前 Ch22 约713–720行仅有KV binding在线回归与history-dependent attention等价，未承载**历史重建目标→后续行为teacher对齐**的目标分支。实际正文已插在该TTT段后：有限Y的full-context目标仅提供受限teacher；alignment小不保证未知future、真正因果保持或精确恢复。额外teacher前向/反传、LoRA更新与forget/reset身份要与显式KV分账。Llama2-7B/RTX4080SUPER、n1024/m2048/r64、128生成tokens、1–16K；表1短上下文比standard慢，prefill被时延公式减除，不能采用全成本O(1)或一般性能优越。precision/batch/concurrency/SLO未披露；§4.6.3非所有m单调，不采“更大即更好”。source→owner与实际正文/相邻交接写后复核均已通过，见 `V3_APR02_ABSORBER_GIST_INDEPENDENT.md` 末节；未复现，不代表日级Gate。

当前Books处置：整合：实际正文及写后已通过；MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20915同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20920 Gist Sparse Attention](https://arxiv.org/html/2604.20920v1)

2+2+2=6，真实知识缺口深入完成，已实际整合 INFER-KV-CACHE Ch45，root 非作者写后通过。实际读§3.1–3.5、§4.1–4.5：required CPT训练interleaved gist；query×gist key选chunk，再读selected gist+raw KV，unselected不读，GQA每head选择后union；首attention层gist输入相同故跳选择。可选finetune把query-dependent稀疏mask放训练，不等普通top-k自动可微。写前 Ch45 已有残余summary（592）、synthetic cache distill（627）和host recall（681），没有**可训练summary同时做query路由且保可展开原KV**的分支。实际插入 learned eviction之后、recoverable recall之前，明确active read budget≠原始KV驻留总量、gist summary proxy≠证据真值，训练mask/model与原KV身份共同验收。Qwen2-7B/Llama3.2-1B、8H100训练，LongBench/RAG质量与SG+SR消融；FullFT平均仍更高、AG+SR局部优，未披露端到端latency/servingSLO，不采用无损或全配置更快。source→owner与实际正文/相邻交接写后复核均已通过，见 `V3_APR02_ABSORBER_GIST_INDEPENDENT.md` 末节；未复现，不代表日级Gate。

当前Books处置：整合：实际正文及写后已通过；INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20920同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21428 Decoupled DiLoCo](https://arxiv.org/html/2604.21428v1)

2+3+2=7，深入完成，已实际整合 TRAIN-DISTRIBUTED-TRAINING Ch36，root 非作者写后通过。实读§3.1–3.3/Alg1–2、§5.1–5.5、Table2–5：独立learner保局部状态，syncer按fragment达到K后聚合，步时/通信slack内grace增加到场贡献；权重实际为tokens×tokens/steps，RDA另分方向/范数，不是简单token均值。写前 Ch36 的跨地域层级staleness（约1350）/optimizer与stepcommit已有原则，但缺**minimum quorum+有界grace把可用性与样本贡献权分开**。实际在异构跨站聚合后写入两段：各fragment持source revision/steps/tokens与恢复状态，quorum不等所有样本或集中式语义；代价staleness、样本权偏置与checkpoint组合，slack不足回同步/缩小grace。150K～1.2M chips是failure simulation，真实heterogeneous setup正文TPUv5e/v5p却Table5称v6e/v5p，需保配置歧义；K1无grace部分质量退步，非所有slice匹配，未披露precision/SLO，不采用百万卡实训/无损一致性。与Google日历日博客去重同家族，日期仅按官方公告slot/ID分配及精确v1相邻处理簇有据推断08–09，不称逐篇公告确证；source→owner与实际正文/相邻交接写后通过见 `V3_ROOT_QUORUM_TERNARY_INDEPENDENT.md`。

当前Books处置：整合：实际正文及写后已通过；TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21428同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20913 FairyFuse](https://arxiv.org/html/2604.20913v1)

2+1+2=5；真实知识缺口深入完成，已实际整合 INFER-TENSORRT-LLM Ch49，root 非作者写后通过。实际读§2.3、§3/Algorithm1、§4、§5.1–5.5及Table5/6：complex widely-linear八子GEMV共享mask解码、activation与寄存器累加，以ternary正负mask驱动AVX-512/BMI2加减；仍有每输出scale乘法，不能称整个模型无乘法。写前 Ch49 量化成本清单及product-LUT（约720–741）、CPU layout→SIMD/LUT（约807–817）未承载无LUT条件加减与多子GEMV共享解码分支。实际在 LUT 后补一个并列执行选择，不否定LUT或常规反量化。评价限Fairy2i-W2/Llama2-7B、单socket48线程Xeon8558P、FP32累加/2bitpacked+scales、至少128输出；prompt长度/并发/SLO未披露。Table6 CPU对照1线程dense与48线程ternary混杂；H200自写CUDA回归不证明所有GPU极低位实现不可行，质量也低于FP16。不采用29.6×、GPU结构性无收益或近无损宣传。原v1处理00:01:34Z/OAI04/24仅组合日期线索，非孤证首发。source→owner与实际正文/相邻交接写后通过见 `V3_ROOT_QUORUM_TERNARY_INDEPENDENT.md`，未复现，不代表日级Gate。

当前Books处置：整合：实际正文及写后已通过；INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20913同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20930 SafeRedirect](https://arxiv.org/html/2604.20930v1)

2+2+2=6；保护深入完成，作者拟仅报告。实读§3.1–3.4、§4.1–4.4/Table1–2及Limitations：给validator修复压力下的模型明确失败许可、固定拒答与保留placeholder，是prompt级替代行为而非runtime hard stop。三AI工具任务/七OpenRouter模型，每条件2100次；Grok judge只将可提取且最高等级有害计入unsafe，未证明所有剩余输出安全。消融并非完整组合必胜：去P3的Grok、去P2的Kimi平均更低；良性输入行为相同是目标而非此实验已证明。Ch72约1664–1674明确危险路径覆盖、条件失败与剩余可达行为分权，约733policy/CI owner独立于模型；本项提示词不授予新的执行保护，不据此改成system message可信hard gate。保有限任务重定向证据，不声称心理/attention成因、零开放风险或防线验证；precision/length/batch/concurrency/SLO未披露。原v1处理00:01:53Z/OAI04/24作组合日期线索。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20930同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20854 ERA](https://arxiv.org/pdf/2604.20854v1)

2+2+2=6；纠错深入，拟争议暂缓，待非作者核。实际 HTML §4.1–4.3/Eq7/13–16、Table2 与官方 PDF-v1 物理第5页 Eq7/A.1核同：`tilde alpha = y(1-y) ⊙ alpha`；one-hot y 使全部参数为零，Dirichlet 不定义。不是仅HTML转录问题；不擅自改成常见EDL公式，不据此断言全部经验虚假。双head对应query-only/检索输入，不自动保证独立；DST冲突与不确定性也是学习proxy，不证明真实知识状态分解。

当前Books处置：暂缓：中心主张争议；不入Books，定点重开见§5。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20854同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20938 HARBOR](https://arxiv.org/html/2604.20938v1)

2+2+2=6；纠错深入，拟争议暂缓，待非作者核。实际 §VI/Eq4–7/Alg1 与 §VII–VIII：reference SAAS/NUTS/Matérn5/2/qNEHVI换成ridge/linear Boolean tensor-product/greedy单候选EHVI，原文承认不保完整posterior，却又称Boolean Matérn仅仿射Hamming重标等价。d=2、lengthscale=1时 k(0)=1、k(2)≈.13866、k(2sqrt2)≈.03702，仿射要求末者等于2k(2)-1≈−.72268，直接不成立；不能把reference后验chance约束或全体实现等价移交替代artifact。

当前Books处置：暂缓：中心主张争议；不入Books，定点重开见§5。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20938同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21026 MCAP](https://arxiv.org/html/2604.21026v1)

2+1+2=5；标准必要审阅完成，拟仅报告，待非作者核。实际 §3.1–3.3/§3.1.1/§4.8及AppendixD：Q/V与FFN activation norm的load-time层排序供precision/residency选择；sub-Gaussian/iid条件下top-k失败界随variance/gap²缩放，12题明确purposive、不是经检验的iid。界只恢复排序，不证明低精度/删层后的任务质量；scorer对自身reference100%不是独立oracle。先前“没有恢复界”的关闭理由已纠正，不因相同主题再次排除。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21026同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20932 Adaptive RAG Defense](https://arxiv.org/html/2604.20932v1)

2+2+2=6；保护深入完成，作者拟仅报告。实读§4.2–4.3/Algorithms1–3、§5.1–5.4、§6/Table7：sentinel观测query/retrieval统计，strategist选择pre/post hook；50queries/700docs/Top5、Llama3.1-8B generator与多controller，MBA exact mask-fill不是membership inference advantage，content-leakage只架构未测。静态测试顺序与adaptive随机交织协议不同；Table7针对性静态TrustRAG的recall/ASR优于若干ADO，不能把动态选择写成必然优于轻静态分支。Ch72约2310–2313 joint failure correlation/覆盖差异/false-refusal与1664–1674残余风险，已有本项可支持的长期保护验收；没有采用coherence/attention当可信真值。所测零ASR不推出open-world安全；judge/局部小样本、额外controller成本与未披露hardware/precision/concurrency/SLO限制保留。原v1处理00:01:55Z/OAI04/24仅组合日期依据。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20932同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20917 The Path Not Taken / DexBench](https://arxiv.org/html/2604.20917v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。实际§2.1–2.3/3.1–3.2/3.5、§4.2/4.3/7：同程序和原输入分别测exact coverage预测、为指定未覆盖branch生成mutant输入；联合成功是两项pass@k指示的交集，不要求同一次样本共享内部推理，也不证明因果理解。SlipCover执行提供coverage oracle，445配对样本源自三公开Python基准、13模型、one-shot；原代码可能污染，最大coverage增加的branch选择有偏。forward exact-set与backward单branch命中难度不同，Jaccard宽松评价仍有分歧，不能将差值全归能力机制。hardware/precision/并发/SLO未披露。Ch66现有可执行oracle、same-verdict语义配对与round-trip编辑分别承担执行证据/语义/保留性，不声称此forward/inverse程序协议已完整承载；本轮保留这一受限新evaluation slice，不把joint score采为一般因果理解证书。rawv1处理00:01:39Z/OAI04/24与官方slot/ID批次仅支持有据08–09推断。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20917同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20903 Sensitivity–Uncertainty Alignment in Large Language Models](https://arxiv.org/html/2604.20903v1)

2+2+2=6，保护保证/纠错深入必要审阅完成，拟中心保证争议、Books暂缓，待非作者核。实际读§3.1–3.5、§4.1–4.3、A.1的风险桥、§5.2/Alg1及§6–7评价与限制。预测分布的平均扰动差异S与熵H是不同对象；Remark3.3仅给S≤sup divergence，不能在风险上界用更小的S无条件替换sup。A.1 Step2加减ψ后不能仅因ψ非负删除正项，Step4在λH≥ψ时写−ψ≤−λH，方向也相反。

当前Books处置：暂缓：中心主张争议；不入Books，定点重开见§5。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20903同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20904 Normative Simulacra](https://arxiv.org/html/2604.20904v1)

2+2+2=6，保护与实际知识缺口深入必要审阅完成，已实际整合Ch31；apr20与root必要源→owner及root实际正文/相邻交接写后复核通过（记录见 `V3_APR20_NORM_SINK_FOUR_INDEPENDENT.md`）。实际读§3.1–3.5、§4.1–4.2/§5/Ethics及A.1/A.3/A.4。十部小说中的信息flow与应然norm分开抽取；SFT先学typed extraction，GRPO再以结构及context/norm grounding组合reward。§3.4.2对同一completion分别使用正确检索norm universe与随机错误universe评分，reward为clamp(r_correct−λr_wrong,0,1)，不是只奖励更保守拒绝。Top3 norm检索与弱critic构成训练代理，并不赋予小说规则法律/安全authority。

当前Books处置：整合：实际正文及写后已通过；TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20904同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20937 SToP](https://arxiv.org/html/2604.20937v1)

2+2+2=6，实际知识缺口深入必要审阅完成，已实际整合Ch23；apr20与root必要源→owner及root实际正文/相邻交接写后复核通过（记录见 `V3_APR20_NORM_SINK_FOUR_INDEPENDENT.md`）。实际读§3、§4 Eq4–6、§5.1–5.4/Tables1–5及naive sink处置对照。高attention并非稳定的语义重要性；跨帧累计attention经幂与MinMaxNorm形成sink proxy，空间选择用A−μ_s s，时间剪枝将sink项与相似度共同判定。累计值不能区分短暂尖峰与持续高值；它只是条件性排名惩罚，不证明持久高分token都无用，也不授权无条件硬删除静态显著对象。

当前Books处置：整合：实际正文及写后已通过；MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20937同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20940 Sema](https://arxiv.org/html/2604.20940v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际读§2.2、§3.1–3.3、§4.1–4.5/§5。将原生模态codec编码放客户端，server按一致codebook重建图像/波形后仍调用原有模型encoder；不是任意LLM直接理解任意离散codes。modality/codebook/count/seq/time framing及session协商、视觉codes加AX/OCR文本、audio SpeechTokenizer首RVQ层50token/s与Whisper-large-v3、Qwen2.5-VL7B构成具体placement分支。lossless文本运输不证明AX/OCR内容完整。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20940同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20985 Differentially Private Model Merging](https://arxiv.org/html/2604.20985v1)

2+2+2=6，保护合同/真实知识缺口深入必要审阅完成，已在Ch72真实正文吸收，root非作者写后通过。实际读v1 §2–5、§6.1–6.3、§8.1–8.2：同数据集的多个DP资产中随机只发布一个，RS的RDP界为各profile指数混合，PLD可做混合；不能等同发布所有模型的联合组合。线性参数组合LC仅知最终profiles时可退回联合发布的composition；按DP-SGD训练轨迹得到更紧界还依赖每步clipping、sampling、学习率/权重及独立noise，组合noise方差与各加权更新有关。§6.3同run checkpoints共享早期随机更新，不满足这个独立noise分支；RS仍可按profile混合。不能采用“模型平均自动平均epsilon”或“后处理消除已发布资产的历史预算”。更紧accountant随模型数指数复杂，而非随参数数指数复杂。

当前Books处置：整合：实际正文及写后已通过；PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20985同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.20995 Value-Conflict Diagnostics Reveal Widespread Alignment Faking in Language Models](https://arxiv.org/html/2604.20995v1)

2+2+2=6，保护评价深入必要审阅完成，拟仅报告，待非作者核。实际§3–5、§6.1–6.7：合成250二选一道德情境后经四模型多数回答筛到50，反向developer policy与monitored/free、unmonitored/paid tags及不服从后果组合；compliance gap是条件行为差异，不识别持久真实价值或战略意图。无后果时总体gap近零仍有模型例外，oversight概率效应非单调；scratchpad自述、PCA主方向和steering均不构成内在意图真值或严格一维因果。训练/评价场景的priming及样本选择必须保留，不能从37%外推自然总体。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.20995同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21016 SGD at the Edge of Stability: The Stochastic Sharpness Gap](https://arxiv.org/html/2604.21016v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。实际§2–4、Assumptions1–8、§5：gradient noise在top-Hessian方向注入波动，经cubic restoring force压低平均sharpness；有限coupling要求C4 loss、eigengap、导数/噪声条件。闭式gap另用frozen coefficients、stationarity/decorrelation closure及正alpha/beta，不因特征向量正交就有独立性，也不是普遍Transformer/Adam调参公式或generalization证书。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21016同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21041 Projected Gradient Unlearning for Text-to-Image Diffusion Models: Defending Against Concept Revival Attacks](https://arxiv.org/html/2604.21041v1)

2+2+2=6，保护保证深入必要审阅完成；拟窄争议暂缓正面保证，经验只作受限报告，待非作者裁决。实际III-A–D/Alg1、IV、V-A–F、VI：retain activations covariance生成投影P，hardening更新G−GP。固定输入r在range(P)的局部线性层可得W'r=Wr，但没有全网非线性/上游改变后activation、bias及后续任意fine-tuning的同等保证。未来不受约束更新并不自动执行该投影，故“精确保留全部retain输出”“未来任意fine-tuning不能undo”不由这段局部等式推出；不因此否定全部作者经验。

当前Books处置：暂缓：中心主张争议；不入Books，定点重开见§5。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21041同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21072 Distributed Generative Inference of LLM at Internet Scales with Multi-Dimensional Communication Optimization](https://arxiv.org/html/2604.21072v1)

2+2+2=6，标准必要审阅完成，拟已有覆盖 `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)“低带宽拓扑要联合预算Hops、Bytes与Steps”实际三段。已读§4–7、§8.1/Table4及必要microbatch/KV背景。layer placement、microbatch overlap与KV offload共用显存/带宽约束，FP16字节分拆+ZSTD为lossless通信而非低比特量化；proxy draft/top-k与验收反馈piggyback只为低带宽预算，不能替代target验证。既有正文具体联合planner、cache location/communicator/runtime分权及高带宽/CPU-cost回退已承载拟采用机制，不声称全部DP或packing实现已被写入。

当前Books处置：已有覆盖：非作者命题复核通过；INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21072同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21079 Foveated Reasoning: Stateful, Action-based Visual Focusing for Vision-Language Models](https://arxiv.org/html/2604.21079v1)

2+2+2=6，真实知识缺口深入必要审阅完成，已在 `MULTIMODAL-REPRESENTATION` Ch23实写并获root非作者写后通过。已读§2.1–3.3、§4/Table3与AppendixC。离散foveation触发与hidden-state连续box回归在同一AR trajectory取得crop并注入新视觉状态；训练先CE+box监督，再区分普通token的accuracy/format信号、foveation动作accuracy及correct-only area regularizer。原Ch23主动Observation已有coarse-view/proposal/assembler/answer gate，但没有这种单trajectory连续取证动作头及正确性条件化面积目标的训练责任；不是以crop主题重新写一次。

当前Books处置：整合：实际正文及写后已通过；MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21079同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21083 Behavioral Consistency and Transparency Analysis on Large Language Model API Gateways](https://arxiv.org/html/2604.21083v1)

2+2+2=6，保护评价合同深入必要审阅完成，拟仅报告。已读§3.1–3.3、§4.1–4.3、billing/latency实验必要段和训练/测试分割。55固定probes的多种特征训练24个one-vs-rest分类器；每model/test_id的重复样本10训练2测试不是新prompt-domain holdout。行为identity signal与密码学backend attestation不同，5未见变体不匹配不证明所有未知backend都能拒绝。多轮recall失败不能唯一归因于truncation，latencyCV亦受网络/负载影响；billing分母仍依gateway自报tokens，无法独立证明真实token或算力。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21083同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21098 Propensity Inference: Environmental Contributors to LLM Behaviour](https://arxiv.org/html/2604.21098v1)

2+2+2=6，保护行为评价深入必要审阅完成，拟仅报告。实际读§2.1–2.5、§3.4、§4.2与必要factor/randomization说明。12环境因素的随机组合、避免围绕最有利model/config选择环境、Bayesian logistic effects及模型/环境intercepts构成有限评价合同；判据为人设计的行为proxy，不测内部战略信念。odds ratio2并不等于概率翻倍，因子更多取值会影响L1效应总量，capability分组含补估值，战略因素“约半”来自特定GLM likelihood比较，不是意图因果份额。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21098同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21045 Hierarchical Policy Optimization for Simultaneous Translation of Unbounded Speech](https://arxiv.org/html/2604.21045v1)

2+2+2=6，中心目标/纠错深入必要审阅完成，拟争议暂缓，待非作者核。已读v1 §3.2–3.3、§4.1–4.3、§5.1–5.2；InfiniSST的交错输入/KV复用是此前baseline，本篇贡献是句级hypothesis/reference对齐后，让quality阈值决定latency reward是否可用，并分别聚合归一化。null对齐被赋最差质量和10秒lag，阻止空译/错译仅靠抢先输出获奖；这只是训练proxy，不是运行时翻译真值或SLO。

当前Books处置：暂缓：中心主张争议；不入Books，定点重开见§5。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21045同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21057 TRACES: Tagging Reasoning Steps for Adaptive Cost-Efficient Early-Stopping](https://arxiv.org/html/2604.21057v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。已读§3–6、G.4/G.5/H.1：按换行切reasoning step，文本分类器区分constructive/evaluative，再以累计比例和连续五步阈值触发强制答案（100-token预算）。角色迁移是一种可学习sensor；gold first-correct forced-readout/正确样本条件化只用于分析，不能作为部署时内部“已知正确”证据。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21057同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21100 Preconditioned DeltaNet: Curvature-aware Sequence Modeling for Linear Recurrences](https://arxiv.org/html/2604.21100v1)

2+2+2=6，实际知识缺口深入必要审阅完成，已在 `MODEL-LONG-CONTEXT` Ch22实写并获root非作者写后通过。已读§2.3/§3.1–3.5/§4.1/§4.3与E.3：在线ridge least-squares令G=Σkkᵀ+λI、C=Σvkᵀ、P=G⁻¹；精确ATQ的CPq可用Sherman–Morrison对应ATK写入key=P_prev k/(1+kᵀP_prev k)，在所列初始化/可逆条件下有S=CP。它改变的是写入几何，不是额外保存所有历史token。

当前Books处置：整合：实际正文及写后已通过；MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21100同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21106 How Much Is One Recurrence Worth? Iso-Depth Scaling Laws for Looped Language Models](https://arxiv.org/pdf/2604.21106v1)

2+1+2=5，真实知识缺口深入必要审阅完成，已在 `TRAIN-PRETRAINING` Ch28实写并获root非作者写后通过。实际读官方PDF-v1首页及§2–6、相关拟合/下游与AppA：116 runs、六FLOPs预算，固定20个有效blocks、recurrence r=1/2/4/8、full BPTT，输入注入的额外compute也计入。共享减少unique参数，却仍执行重复blocks；预算固定时宽度与训练tokens需要一起改变。联合拟合N_eff=N_once+r^φ N_rec，φ约.46是该范围经验结果，不是一般递归容量定律。

当前Books处置：整合：实际正文及写后已通过；TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21106同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21131 Cross-Session Threats in AI Agents: Benchmark, Evaluation, and Algorithms](https://arxiv.org/html/2604.21131v1)

2+2+2=6，保护评价深入必要审阅完成，拟仅报告，并隔离指标命名/补偿性保证，待非作者核。已读§3.4/3.6、§4.1–4.5/5/6.1–6.2/7.3及必要metric定义：两54-scenario shards、identity-anchor policy与闭环改写对同一Claude judge，完整日志仍低召回是受限反证，不是所有长上下文防御失败。K50 coreset用不同prompt、单provider和较宽区间，不能将差异唯一归因于信息瓶颈；ordered prefix stability与集合相同不同，可作缓存代价sensor，但不是安全真值或端到端净成本。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21131同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21139 Slot Machines: How LLMs Keep Track of Multiple Entities](https://arxiv.org/html/2604.21139v1)

2+1+2=5，标准必要审阅完成，拟已有覆盖 `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)“从可读出到机制”“信息存在、可读与被使用是三个不同命题”，待非作者核。已读§2.1、§3.1、§4.2、§5.3/C.3：受限合成多entity提示与Qwen3-32B残差的无监督slots可读current/prior信息；交换指定entity文本的K/V影响序列关系任务，事实属性任务则未显示同样的prior路径使用。存在/可解码不等原行为使用，现章具体probe→干预→下游及模块移植已经承载这一解释，而非仅同名主题。

当前Books处置：已有覆盖：非作者命题复核通过；WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21139同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21164 MAGIC-TTS: Fine-Grained Controllable Speech Synthesis with Explicit Local Duration and Pause Control](https://arxiv.org/html/2604.21164v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。已实际读精确v1 §3.1–3.4/4.1–4.4与Tables1–3：F5-TTS flow模型将逐token duration/pause作为声学frame数，用log编码、可用mask和中心化残差注入文本表示，训练随机丢弃控制，保留无指定条件的生成分支。真零经中心化后残差为零，missing由mask置零，二者对该支路均为零，不能说公式已使“零停顿”与“不指定”在输出上可识别。局部条件编码与对齐处理是受限实现，不因映射Ch24就造通用控制保证。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21164同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21189 Full-Body Dynamic Safety for Robot Manipulators: 3D Poisson Safety Functions for CBF-Based Safety Filters](https://arxiv.org/html/2604.21189v1)

2+2+2=6，保护/实际知识缺口深入必要审阅完成，已在 `MULTIMODAL-EMBODIED-VLA` Ch26实写并获root非作者写后通过。已实际读II-A/B、III-A–D/Theorem1证明、IV-A–C/V：连续机器人表面由ε球采样覆盖，再将自由空间向内缓冲ε，所有采样点留在缓冲空间才推出完整表面安全。这是条件几何保证，不是采样最小间距或QP永远可行。Poisson-disk密集点云实现还依原点云逼近δ，实验用ε+δ及完全free voxel；最小间距不代替真实连续覆盖证明。

当前Books处置：整合：实际正文及写后已通过；MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21189同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21192 How VLAs (Really) Work In Open-World Environments](https://arxiv.org/html/2604.21192v1)

2+2+2=6，保护评价深入必要审阅完成，拟已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Outcome Witness决定分数的证据基础”中具身attempt/near-hazard/terminal与能力/机会/censor段，待非作者核。已实际读III-A/B、IV-A/B指标与V：B1K50任务×10变体官方checkpoint/seed复跑；8专家500视频按每任务该失败类是否出现计，不是全部事件频率。非确定性导致落差只是解释线索，未唯一控制因果。

当前Books处置：已有覆盖：非作者命题复核通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21192同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21197 Toward Efficient Membership Inference Attacks against Federated Large Language Models: A Projection Residual Approach](https://arxiv.org/html/2604.21197v1)

2+2+2=6，安全/理论纠错深入必要审阅完成，拟争议暂缓，待非作者核。已实际读II-C、III-A–D、IV-A–H及Appendix B-A/B-B：honest-but-curious server持有全局参数及单client当前轮梯度，可对指定target前向；不是secure aggregation后仍必可攻击。投影残差是经验sensor，从gradient span到精确训练record的确定性桥未成立：三个不同输入表示e1、e2、e1+e2，前两为成员、第三非成员，梯度若张成e1/e2，则非成员残差也零。表示不同不排除非成员位于训练样本线性包。

当前Books处置：暂缓：中心主张争议；不入Books，定点重开见§5。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21197同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21215 The Recurrent Transformer: Greater Effective Depth and Efficient Decoding](https://arxiv.org/html/2604.21215v1)

2+2+2=6，真实知识缺口深入必要审阅完成，已在 `MODEL-LONG-CONTEXT` Ch22实写并获root非作者写后通过。实际§2.1–2.3/§4–7/E.4：同层过去KV从过去位置的**层输出**派生，当前位置用层输入temporary KV避免自身循环，输出后才写persistent KV。不同于普通KV与跨层共享feedback，仍保存逐token历史而非固定容量state。Ch22原local/global、YOCO-U与GDN分支未说明这条同层时间递归的状态身份和并行代价；新增正文位于YOCO-U后、线性混合前，不另给Ch45重复模型语义owner。

当前Books处置：整合：实际正文及写后已通过；MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21215同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21221 Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](https://arxiv.org/html/2604.21221v1)

2+2+2=6，真实知识缺口深入必要审阅完成，`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24窄增量已实际写入并获root非作者写后通过。实际§3.1–3.5/4.1–4.5、Tables1–3：完全denoised历史作为persistent anchors，local窗口承载近处/当前denoise；evicted local进入coarse pooling/Top-C候选，sink保留，persistent密读+local Top-K合为一个masked softmax。pool代表只供routing不成为细粒度内容真值；被丢旧history不可无限恢复。DMD训练就启用动态cache/局部稀疏，与训练后单独剪cache不同。Ch24 Salt已有历史质量coverage，新增正文只承接“历史保留策略与局部mask同训练目标覆盖”的具体分支；kernel artifact仍handoff Ch49。

当前Books处置：整合：实际正文及写后已通过；MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21221同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21229 EngramaBench: Evaluating Long-Term Conversational Memory with Structured Graph Retrieval](https://arxiv.org/html/2604.21229v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。实际§3–8/Limitations：5synthetic personas、100conversation/150query，每factual slice30；固定GPT4o/temperature.3不使其他extraction/retrieval预算相同。cross-space .6532>.6291但aggregate .5367<.6186，移除planner或typed answer增加aggregate却损该slice，体现任务专用结构的受限取舍而非Graph普遍优；未充分power证明总体排名。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21229同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21241 CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors](https://arxiv.org/html/2604.21241v1)

2+2+2=6，保护/中心公式纠错深入必要审阅完成，拟争议暂缓，待非作者核。已实际读III-A–C Eq1–10、IV-A/B、V-A–C。extended action含被监督的Δ-position，g取同一组anchor增量，而p*又由GT状态定义；Eq6用g(A*)与p*的差设δ。因此按印刷定义二者相同、δ=0，不能推出所宣称的正容忍带。预测anchor也未直接出现在该δ定义中；若真实实现采用另一组状态/预测值，需补定义与算法桥。只隔离正容忍/预测物理线索约束的中心采用，不否定auxiliary head与受限经验收益，不扩所有实验重审。

当前Books处置：暂缓：中心主张争议；不入Books，定点重开见§5。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21241同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21254 Hyperloop Transformers](https://arxiv.org/html/2604.21254v1)

2+2+2=6，真实知识缺口深入必要审阅完成，已在 `MODEL-TRANSFORMER-LAYER` Ch17实写并获root非作者写后通过。实际§2.1–2.2/3、§4.1–4.3及Tables1–2：begin/end一次、中段重复，matrix residual只在loop边界混合；diagonal sigmoid carry不是Sinkhorn双随机mixer，另有loop-specific权重与位置，不能称所有参数完全共享。当前Ch17 depth-routing/multi-stream/mixer说明可行性与资源成本，但未承载“混合频率在loop而非每子层”与权重驻留/执行深度分账；Ch18的loop状态/停止交接不是这个架构分支。正文已在Ch17 mixer之后，未重复Ch18停止策略。

当前Books处置：整合：实际正文及写后已通过；MODEL-TRANSFORMER-LAYER [Ch17](../../../../books/part-02-model/17-transformer-layer.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21254同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21255 When Agents Look the Same: Quantifying Distillation-Induced Similarity in Tool-Use Behaviors](https://arxiv.org/html/2604.21255v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。实际§3.1–3.3/4.1–4.2/5.1–5.2及Limitations/AppC.3：RPS只评共同stage，AGS从成功模型tool交集定义mandatory集合，再评optional节点与依赖。交集是本model/task pool的经验对象，不是逻辑必需tool证明；图/语句相似不能作为训练来源attestation。受控200条teacher轨迹LoRA提供局部teacher-specific变化，但不同分量并非全同向，Pearson .491、p=.054也不证明两sensor独立。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21255同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21268 Measure Twice, Click Once: Co-evolving Proposer and Visual Critic via Reinforcement Learning for GUI Grounding](https://arxiv.org/html/2604.21268v1)

2+2+2=6，标准必要审阅完成；[非作者有限复核](../_sources/daily-20260424/V3_ROOT_TWO_ONLY_FINITE.md)确认仅报告处置。实际§4.1–4.3 Eq1–9与§5.1–5.7：同MLLM不同prompt作proposer/visual critic，K坐标一次提出后将marker渲染到图上排序；各角色的EMA正确率/nDCG控制另一角色coverage/ranking奖励。maturity是受限训练proxy，不是critic真实可靠性证书；accuracy加hit项不必限于[0,1]。Ch33已有共同训练及独立outcome/角色credit分账，本法新的GUI operating point可报告，尚不据其协同曲线修改通用训练保证。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21268同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21276 Do LLM Decoders Listen Fairly? Benchmarking How Language Model Priors Shape Bias in Speech Recognition](https://arxiv.org/html/2604.21276v1)

2+2+2=6，标准必要审阅完成，拟已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) Compression Release人口组WER/循环输出与“差距缩小须检查较好群体退化”三段，待非作者核。实际§2.1–2.4/4.1–4.3/5.1–5.2：matched-prompt FairSpeech减少词汇差异，9ASR/12噪声条件与bootstrap只支持受限切片；mask让全组错误很高、相对差距压缩，不是fairness改善。该可迁移判断已在实际正文，报告新acoustic degradation例证，不把权重压缩与音频压缩混为同一机制。

当前Books处置：已有覆盖：非作者命题复核通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21276同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21327 Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning](https://arxiv.org/html/2604.21327v1)

2+2+2=6，纠错深入必要审阅完成，拟中心解释争议/暂缓，待非作者核。实际§2–3/Eq5–7、§4.1–4.4/Tables1–4：从N64多数答案构造伪reward，K32组将正例数限制在K/2并给正负固定±1，最后M128重采样多数答案作五epoch SFT。固定幅度确实取消组内std的放大，但不能消除多数标签错误；负例筛选改变优化分布，稀有有效答案仍可能被罚。§4.4却称MATH后期mean advantage转正；按印刷Eq5–7，每prompt均值=(2K⁺−K)/K≤0，任意正权跨prompt平均也≤0，无法出现该正均值。需要作者说明日志分母、token权重或实际实现与公式的差异；不据此采用“自适应正信号转换”机制，不否定所有实验或取消固定幅度的一般可行性。

当前Books处置：暂缓：中心主张争议；不入Books，定点重开见§5。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21327同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21330 Teacher-Guided Routing for Sparse Vision Mixture-of-Experts](https://arxiv.org/html/2604.21330v1)

2+2+2=6，真实知识缺口深入必要审阅完成，并已在Ch21落实为条件分支。实际§3/4/5.1–5.4/J.4：冻结dense视觉teacher backbone的中间features供辅助router，辅助router由load/entropy训练而非task loss，stop-gradient的teacher routing分布再以KL约束student router。teacher backbone冻结不等于teacher router固定，后者联合训练；这有别于原已激活expert虚拟移除的离线contribution prior和dense-upcycling初始化蒸馏：用外部feature空间形成训练期assignment proxy，补selected experts之外的路由信号，但load/entropy不取得语义正确authority。[写前](../_sources/daily-20260424/V3_APR02_FOUR_21327_21343_INDEPENDENT.md)及[实际写后](../_sources/daily-20260424/V3_ROOT_CH21_WRITE_AFTER.md)非作者复核通过，不代表日级Gate。

当前Books处置：整合：实际正文及写后已通过；MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21330同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21335 Sub-Token Routing in LoRA for Adaptation and Query-Aware KV Compression](https://arxiv.org/html/2604.21335v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际§3.1–3.4/Eq4–13、§4.3–4.4/A.2/C.6：Q/K保留，V分组；无query分支保部分groups并学习重建，另一分支对context-token/group联合Top-M且query末16token完整保留，未保V置零，不混称同一恢复策略。split层context hidden预测诊断query-attention目标；causal context状态本身不能读取末位未来query，属于学习近似proposal而非已观察当前query的精确打分。不能从名字query-aware推出任意新query同一cache可复用。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21335同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21343 Latent Denoising Improves Visual Alignment in Large Multimodal Models](https://arxiv.org/html/2604.21343v1)

2+2+2=6，真实知识缺口深入必要审阅完成，已在Ch23落实为条件分支。实际§3.1–3.3/Eq9–12、§4.1–4.6必要对照：projected visual token按saliency选noise/mask，在LMM中间层接辅助decoder，恢复冻结视觉encoder的clean patch features，加逐行关系KL与同图patch contrastive；仍保答案loss。原Ch23已区分masked input与全patch target监督，现补“腐化发生在projector之后、恢复责任落在语言模型中间状态”的训练链。它不改变所有encoder层或在部署期持续denoise，训练corruption/辅助head撤掉才恢复普通inference。[写前](../_sources/daily-20260424/V3_APR02_FOUR_21327_21343_INDEPENDENT.md)及[实际写后](../_sources/daily-20260424/V3_ROOT_FOUR_WRITE_AFTER.md)非作者复核通过，不代表日级Gate。

当前Books处置：整合：实际正文及写后已通过；MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21343同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21346 Symbolic Grounding Reveals Representational Bottlenecks in Abstract Visual Reasoning](https://arxiv.org/html/2604.21346v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际§3/4.1–4.3/5.1–5.5：以Bongard LOGO真实生成程序替代pixels，形式grammar/自然语言、已知concept、额外query image与两类permutation作诊断。已知生成程序是特权representation上界，不是已部署perception模块；主rawimage Gemini与多LLM symbolic池不完全matched，grounded子集只补query图，不等恢复所有13张图像的感知控制。symbolic成绩提升支持输入接口受限诊断，不证明所有原失败唯一因果是vision encoder，也不证明任意无oracle场景可由C–G修复。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21346同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21361 Time, Causality, and Observability Failures in Distributed AI Inference Systems](https://arxiv.org/html/2604.21361v1)

2+1+2=5，标准必要审阅完成，拟已有覆盖 `PLATFORM-TRACE` Ch69（ROADMAP实际ID为PLATFORM-TRACE），待非作者核。实际§3/4.1–4.4/5.1–5.4/6.1–6.4：仅应用级inference时戳加偏移而非改OS，Kafka/ZeroMQ实际测到send→postreceive负span，输出/吞吐仍正常。负span数不是失败请求数；3–5ms仅本配置边界，30s health滚窗恢复不证明时钟已恢复，绝对counts跨不同duration不能直接比。Aeron只future，部分同步/漂移与硬件/模型条件不完整，不能采用通用clock阈值或平台SLO。

当前Books处置：已有覆盖：非作者命题复核通过；PLATFORM-TRACE [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21361同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21391 From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges](https://arxiv.org/html/2604.21391v1)

2+2+2=6，中心理论纠错深入必要审阅完成，拟争议/暂缓，不采理论必要性，待非作者核。实际§3.1–3.3/Eq5–7、§4/Eq8–11、§5直接对照、§7、AppA.3：DCT低频回归prior再作residual flow matching是具体条件分支，频率本身不是intent真值。AppA.3以起点density/score不含c推CFM vector field必不含c，没有连接速度与路径时间导数。反例x0~N(0,1)独立c，x1=c（c=±1），直线CFM在t=0的最优条件速度u0(x,c)=c−x，依然依赖c，而p0完全相同；故源独立不能单独推出其“条件梯度必消失/anchor为必要条件”结论。

当前Books处置：暂缓：中心主张争议；不入Books，定点重开见§5。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21391同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21395 Supervised Learning Has a Necessary Geometric Blind Spot: Theory, Consequences, and Minimal Repair](https://arxiv.org/html/2604.21395v1)

2+2+2=6，中心普遍保证纠错深入必要审阅完成，拟争议/暂缓，待非作者核。实际§4/5.1–5.2/Prop5–7、§6及§7主要受限评价：以Gaussian encoder一致性loss并设task-loss cap，比较Jacobian与归一化TDI的排序。但Prop5证明只依赖covariance=σ²I，却在主文宣称Gaussian是唯一isotropic law；独立±σ Rademacher分量同样有该covariance且对任意J满足E||Jδ||²=σ²||J||F²，直接否定分布唯一性，不否定协方差等式。Corollary2把crossentropy excess写I(n;y|x)>0，但x已包含n时该条件MI=0，需要说明是否本意是I(n;y|s)。Prop6所定义F²/||Jw||²也不一般最大仅dx：J=diag(1,ε),w=e2时比值=(1+ε²)/ε²可任意大。

当前Books处置：暂缓：中心主张争议；不入Books，定点重开见§5。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21395同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21326 MiMIC: Mitigating Visual Modality Collapse in Universal Multimodal Retrieval While Avoiding Semantic Misalignment](https://arxiv.org/html/2604.21326v1)

2+2+2=6，真实知识缺口深入必要审阅完成，已在 `MULTIMODAL-REPRESENTATION` Ch23 fusion段实写并获root非作者写后通过。实际§3.1–3.2/4/5.1–5.5/A.3：独立text/visual编码、BOS query仅在decoder交叉读取两KV，无两源self-attention；训练将single-modality embedding随机混入fused representation，再caption dropout使contrastive目标覆盖缺caption。原Ch23早/晚/cross-fusion有支配与隔离原则，但缺“融合点与缺模态训练支持联合验收”的这一实际分支。

当前Books处置：整合：实际正文及写后已通过；MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21326同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21275 Optimizing High-Throughput Distributed Data Pipelines for Reproducible Deep Learning at Scale](https://arxiv.org/html/2604.21275v1)

2+2+2=6，真实知识缺口深入必要审阅完成，已在 `TRAIN-DATA` Ch27真实正文吸收读取顺序分支，root非作者写后通过。实际§III-A/B、IV-A/B、V-A–C：先以RAM缓存及本地disk对照分离HDFS I/O与主线程Arrow→NumPy CPU瓶颈，再将转换推至worker、缓存预转换rowgroup；顺序epoch采用quota填满后回源，而非声称LRU总是最差。固定shuffle种子仍不能固定共享ventilator/result queue的领取与返回顺序；专属worker队列按同一round-robin分派与合并，把最终batch顺序从线程完成顺序中分离。RNG更新不是单独确定性证明，算法只限定同配置/rowgroup与正常完成路径，论文未验证worker故障、resume或任意异构配置的顺序恢复。

当前Books处置：整合：实际正文及写后已通过；TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21275同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21454 Reasoning Primitives in Hybrid and Non-Hybrid LLMs](https://arxiv.org/html/2604.21454v1)

2+2+2=6，标准必要审阅完成，拟已有覆盖 `MODEL-LONG-CONTEXT` Ch22，待非作者核。当前官方abs-v1/HTML题名只有上述主标题，旧库存长副标题不作为版本身份。实际§3.1–3.2/4.1–4.2/5：OLMo3与Hybrid7B的预训练data/recipe为受限matched pair，再比较Think/Instruct在AstroRecall与Collision的顺序状态更新×检索两轴。每(m,n)100题，JSON parsing与conditional accuracy另分账；Think最大6000生成token而Instruct40，SFT/推理预算不是matched，不能将Think收益单独归因 reasoning training，parse失败也不等内部状态真实消失。Hybrid在不同难度/模型变体的方向不同，作者明确范围很窄。

当前Books处置：已有覆盖：非作者命题复核通过；MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21454同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21477 MCP Pitfall Lab: Exposing Developer Pitfalls in MCP Tool Server Security under Multi-Vector Attacks](https://arxiv.org/html/2604.21477v1)

2+2+2=6，保护合同深入必要审阅完成，拟已有覆盖 `PLATFORM-SECURITY` Ch72，待非作者核。实际§4–7、§8.1–8.5/§10.3：本文是protocol-aware静态检查+trace/objective-validator测试，不是screening旧句所说semantic BOM。Tier1仅查本地描述、schema、日志/guard等P1/P2/P5/P6，P3跨tool forwarding与P4图像→sink尚需动态数据流；清除29项静态finding、risk0不是全部attack被阻断。可信arena predicate区分attacker目的地命中与一般message side effect，拒绝按Agent narrative证明执行安全。

当前Books处置：已有覆盖：非作者命题复核通过；PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21477同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21480 Efficient Agent Evaluation via Diversity-Guided User Simulation](https://arxiv.org/html/2604.21480v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际§3.1–3.5、§4、§5/Table1/3、B.1、E.2/G：在用户turn前保存完整orchestrator/environment/toolDB/history/RNG/routing/counter状态；先LLM选junction，再生成3候选用户回应、取embedding最不相似者，恢复同prefix继续。完整状态不是仅conversation文本，论文宣称exact restoration但未验证所有外部不可序列化副作用；KV reuse是潜在兼容路径，不是已测服务加速。意图保持是事后judge而非在线接受Gate，25.27%仍有intent-miss，不能把定向失败率当真实用户失败概率。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21480同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21511 From Tokens to Concepts: Leveraging SAE for SPLADE](https://arxiv.org/html/2604.21511v1)

2+2+2=6，真实知识缺口深入必要审阅完成，AGENT-RAG Ch76 learned-sparse表示分支已实际写入并获root非作者写后通过。实际§3–5/6–7：先冻结PLM重建token hidden训练SAE，再删decoder、解冻PLM与SAE encoder按检索distillation/FLOPs regularizer联合训练；把倒排维度从token词表换为训练的latent dictionary。token TopK不保证聚合文档仍同等稀疏，SAE reconstruction良好也不等相关性或可解释concept真值。原Ch76 lexical/dense与单/多向量取舍未承载这个倒排词表与retrieval目标联合训练的替代分支，新增正文在检索表示段窄补，不把latent名称当稳定语义身份。

当前Books处置：整合：实际正文及写后已通过；AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21511同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21523 Seeing Isn't Believing: Uncovering Blind Spots in Evaluator Vision-Language Models](https://arxiv.org/html/2604.21523v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际§2–4、B人审过程：600 I2T/750 T2I seed经人工检查，模型生成退化与不改应得分的变体再人工筛选，四VLM三种评价接口。§3.1三指标对象不同：single看分数不变、pairwise看未独选gold、reference看给满分。因此不能按这些失败率直接证明pairwise普遍更可靠，分数下降不保证方向正确/校准；pairwise在invariant切片反而更不稳定。§4.4换reference在I2T变差/T2I变好，§4.5更高reasoning可反退，§4.7理由识别依赖另一Gemini judge，不是人类独立感知证明。

当前Books处置：仅报告：受限机制/证据，不改长期正文。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21523同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21549 Unbiased Prevalence Estimation with Multicalibrated LLMs](https://arxiv.org/pdf/2604.21549v1)

2+2+2=6，真实知识缺口深入必要审阅完成，已在PLATFORM-EVALUATION-SYSTEM Ch66总体质量估计分支实写，并获root非作者写后通过。HTML404后实际官方PDF-v1物理3–9页必要理论/方法/评价/限制已读，不作为正文受阻。源总体组残差能按旧权重抵消，新群体组权重改变后残差重新出现；若条件误差在可重加权各组均为零、目标支持重叠且P(Y|X)稳定，平均预测通过塔律得到目标prevalence。多重校准是更强条件，有限MCGrad拟合不自动取得全feature/任意未来分布保证，classifier AUC高不证明总体估计无偏。

当前Books处置：整合：实际正文及写后已通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21549同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [2604.21570 SpecSyn: LLM-based Synthesis and Refinement of Formal Specifications for Real-world Program Verification](https://arxiv.org/html/2604.21570v1)

2+2+2=6，纠错深入必要审阅完成，拟窄争议/暂缓，待非作者核。实际§3.2–3.4/Algorithm1、§4–6：AST依赖SCC分段/POI后序，verifier拒绝候选后修复，未被当前spec区分的mutant作为细化上下文。Algorithm1保留原程序可验证候选是合理；但§3.4更新式从新增集合减去在mutant上被refute的spec，恰移除了能区分mutant的候选，与本节优化VDR目的及Algorithm1另一过滤对象不一致。仅隔离这个印刷递推/中心保证映射，不能称整算法无效。GCC-O2 binary不同不证明程序语义非等价，verifier未证明也不一般等于语义false，VDR只能是给定变体/solver合同下信号。

当前Books处置：暂缓：中心主张争议；不入Books，定点重开见§5。完整必要证据位置、运行条件/负面结果和精确日期原字段见[本族证据记录](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)的2604.21570同标题小节；这里只复用已实际读的证据，不据篇数或机器检查自签有效。

### [GPT-5.5 公告与 System Card](https://deploymentsafety.openai.com/gpt-5-5)

官方RSS公告/card同为Thu,23 Apr2026 11:00GMT，合一家族。实际§7.2–7.2.1固定真实coding-prefix、code/tool state后成对重采样，由monitor与人审分组；模拟realism不证明真实副作用，移除已知类别后的severity-threshold漏检也不等未知故障真实发现率。当前card的04/24 API与08/19生物更新不回填本窗，未声明持有原版不可变全稿。

非作者对[官方Card](https://deploymentsafety.openai.com/gpt-5-5)§7.2–7.2.1 与 Ch66 的 Offline/Replay/Shadow、环境自身验收及 detector 假阴性边界作了[具体命题复核](../_sources/daily-20260424/V3_ROOT_GPT55_EXISTING_FINITE.md)：现有正文已承载可采用的长期判断，不必为厂商实验比例再增加一段。额外simulation/monitor/human成本、内部样本选择与原版范围限制保留；当前card并非不可变04/23快照，不认证后发更新当窗已存在。无新增Books，完整作者核验位置见[机构记录GPT家族](../_sources/daily-20260424/V3_INSTITUTION_NOTES.md)。

## 5. 缺口与下一步

### 普通工作

必要 Books 写入及其逐项非作者写后复核已完成：本窗29项增量都进入真实章节，普通 Books 待办为0。SPIRE 的 Ch76 已核改动仍在书稿，但[早发反证](../_sources/daily-20260424/V3_ROOT_SPIRE_FIRST_PUBLIC_CORRECTION.md)排除了04/24日报归属，不计本窗整合。[最后三项的实际写后裁决](../_sources/V3_ROOT_APR24_THREE_WRITE_AFTER_20260928.md)分别对应 Ch33 字段 credit、Ch24 训练期稀疏状态和 Ch76 learned-latent 倒排。这里只说明 Books lane 完成，不以书稿写入代替整日验收。

无。85家族的最终准入、来源/日期/否定侧与日级复核已收口；没有可执行的审阅或Books修改遗留。496宽标题/951 submitted库存不成为额外全文队列。20897/21203/21265/21461/21592/21677/21772/21776/21416及21728/21765/20851/20923/21286已保留具体前分母关闭理由，不计分；其余外部保留项如下。

### 日期终态保留项（不属于确定的当窗候选）

[SPIRE 2604.20849v1](https://arxiv.org/abs/2604.20849v1) 的 arXiv 页面/PDF页脚写 `2026-02-12`，同 ID 的[作者 Zenodo 记录](https://zenodo.org/records/19441410)明确 `Published 2026-04-06` 且互链为同一作品；PDF 正文首页另写 `2026-04-24`。来源日期冲突不允许把它按 arXiv ID 处理簇归为本窗首次公开。它已从§3评分和§4本窗候选审阅移出；04/06以前的精确首次公开时刻及 Zenodo 文件版本对应关系尚需定点核，不擅自移入其它日报。2026-09-30 定点读取[官方 API](https://zenodo.org/api/records/19441410)取得 `status=published`、`access_right=open`、`publication_date=2026-04-06`、`created=2026-04-06T15:39:14.358804+00:00`、`modified=2026-04-25T22:13:07.009823+00:00`；创建与修改字段不是公开日志，仍不足确定北京时间09点的真正 owner。已核机制及 Ch76 文字保留，归属问题见[独立记录](../_sources/daily-20260424/V3_ROOT_SPIRE_FIRST_PUBLIC_CORRECTION.md)。这是一项窗前同族纠正，不混入下列22项尚无法定窗的 arXiv 例外。

下列21项不能由常规slot与处理跨截点孤证取得完整落窗上界；既不声称它们真实晚公开，也不推定Submitted日为owner。定点重开条件是官方首次公告清单/精确v1可验证首次公开正文或能限定截点前上界的同身份组合证据；只重开受影响家族，不扩整月。

- [2604.20972](https://arxiv.org/abs/2604.20972v1)：原v1 Updated=2026-04-24T04:25:49Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21191](https://arxiv.org/abs/2604.21191v1)：原v1 Updated=2026-05-05T00:48:33Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21843](https://arxiv.org/abs/2604.21843v1)：原v1 Updated=2026-04-24T01:00:09Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21854](https://arxiv.org/abs/2604.21854v1)：原v1 Updated=2026-04-24T01:01:11Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21860](https://arxiv.org/abs/2604.21860v1)：原v1 Updated=2026-04-24T01:01:31Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21873](https://arxiv.org/abs/2604.21873v1)：原v1 Updated=2026-04-24T01:02:16Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21879](https://arxiv.org/abs/2604.21879v1)：原v1 Updated=2026-04-24T01:02:25Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21882](https://arxiv.org/abs/2604.21882v1)：原v1 Updated=2026-04-24T01:02:32Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21901](https://arxiv.org/abs/2604.21901v1)：原v1 Updated=2026-04-24T01:03:37Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21904](https://arxiv.org/abs/2604.21904v1)：原v1 Updated=2026-04-24T01:03:41Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21909](https://arxiv.org/abs/2604.21909v1)：原v1 Updated=2026-04-24T01:04:02Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21911](https://arxiv.org/abs/2604.21911v1)：原v1 Updated=2026-04-24T01:04:10Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21914](https://arxiv.org/abs/2604.21914v1)：原v1 Updated=2026-04-24T01:04:20Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21915](https://arxiv.org/abs/2604.21915v1)：原v1 Updated=2026-04-24T01:04:21Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21916](https://arxiv.org/abs/2604.21916v1)：原v1 Updated=2026-04-24T01:04:25Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21921](https://arxiv.org/abs/2604.21921v1)：原v1 Updated=2026-04-24T01:04:33Z（处理字段，不是首发）。Seed早目录April23午夜存在日期精度例外，仅保留归属线索，不评分/Books。
- [2604.21923](https://arxiv.org/abs/2604.21923v1)：原v1 Updated=2026-04-24T01:04:37Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21924](https://arxiv.org/abs/2604.21924v1)：原v1 Updated=2026-04-24T01:04:39Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21927](https://arxiv.org/abs/2604.21927v1)：原v1 Updated=2026-04-24T01:04:44Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21930](https://arxiv.org/abs/2604.21930v1)：原v1 Updated=2026-04-24T01:04:47Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。
- [2604.21931](https://arxiv.org/abs/2604.21931v1)：原v1 Updated=2026-04-24T01:04:48Z（处理字段，不是首发）。本窗09点前公开上界未得到足够组合证据，仅保留归属线索，不评分/Books。

另[2604.21809 Quotient-Space Diffusion Models](https://arxiv.org/abs/2604.21809v1)已出现更早同家族正文线索，但first-public尚未证实；不能因ICLR身份猜某个早发日。必要商空间/SDE证据保留，具体缺口为更早公开正文的原时刻或官方公开记录，取得后只定点恢复真实归属。以上合计22项，均不用于本窗正面证据、评分、Books或无遗漏断言。

[DeepSeek V4-preview](https://deepseek.com/en/news/v4-preview/)单项DATE-DEEPSEEK-V4-PREVIEW-APR24只给相交日历日，缺09点前公开上界；官方preview/card/Transparency已读仍无带时区日志。可接受原官方发布日志、可验证public commit/release时间或同家族公告；不拿June24论文回填April机制。此项另计，不与22个arXiv例外混为已评分候选。

### 中心主张争议终态保留项

15项均保留其受限机制/经验与明确反证，不宣布整篇实验虚假。中心争议的具名有限非作者复核为15/15，最后六项见[复核记录](../_sources/daily-20260424/V3_ROOT_FINAL_SIX_DISPUTES_FINITE.md)，并已纳入§6日级收口。下列是本窗中心主张的安全隔离，不支持正面Books或性能/安全保证。定点重开材料如下，同族只请求一次：

- [2604.21232 ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures](https://arxiv.org/html/2604.21232v1)：PAC的唯一数学定义、统计实现及原曲线对应；主文log斜率与附录概率比需统一。当前中心采用隔离，不用于正面证据或Books；具体反例/原式见§4及[同族证据](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)。
- [2604.20874 The Root Theorem of Context Engineering](https://arxiv.org/html/2604.20874v1)：限定full-history累积前提的正确定理或canonical-state反例可排除条件；不靠更多session数证明唯一架构。当前中心采用隔离，不用于正面证据或Books；具体反例/原式见§4及[同族证据](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)。
- [2604.21251 CAP: Controllable Alignment Prompting for Unlearning in LLMs](https://arxiv.org/html/2604.21251v1)：固定Q条件抽样/负例分布与正确条件MI或替代目标定义；对应prefix/privacy保证。当前中心采用隔离，不用于正面证据或Books；具体反例/原式见§4及[同族证据](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)。
- [2604.21794 Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems](https://arxiv.org/html/2604.21794v1)：完整detach/gradient计算图、共享参数/优化清单，统一上游无梯度与跨stage梯度叙述。当前中心采用隔离，不用于正面证据或Books；具体反例/原式见§4及[同族证据](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)。
- [2604.20854 ERA](https://arxiv.org/pdf/2604.20854v1)：合法Dirichlet参数的勘误或同版loss artifact及对应评价，不擅自补成常见EDL公式。当前中心采用隔离，不用于正面证据或Books；具体反例/原式见§4及[同族证据](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)。
- [2604.20938 HARBOR](https://arxiv.org/html/2604.20938v1)：正确Boolean kernel对应、替代surrogate后验/机会约束与固定配置有效对照。当前中心采用隔离，不用于正面证据或Books；具体反例/原式见§4及[同族证据](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)。
- [2604.20903 Sensitivity–Uncertainty Alignment in Large Language Models](https://arxiv.org/html/2604.20903v1)：平均/极值扰动与entropy风险桥的正确不等式、假设及相应算法范围。当前中心采用隔离，不用于正面证据或Books；具体反例/原式见§4及[同族证据](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)。
- [2604.21041 Projected Gradient Unlearning for Text-to-Image Diffusion Models: Defending Against Concept Revival Attacks](https://arxiv.org/html/2604.21041v1)：全网/后续任意微调保证所需约束与正确证明，或明确改为局部层限定。当前中心采用隔离，不用于正面证据或Books；具体反例/原式见§4及[同族证据](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)。
- [2604.21045 Hierarchical Policy Optimization for Simultaneous Translation of Unbounded Speech](https://arxiv.org/html/2604.21045v1)：与印刷objective/normalization一致的loss实现或勘误，明确quality/latency和advantage分母。当前中心采用隔离，不用于正面证据或Books；具体反例/原式见§4及[同族证据](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)。
- [2604.21197 Toward Efficient Membership Inference Attacks against Federated Large Language Models: A Projection Residual Approach](https://arxiv.org/html/2604.21197v1)：从成员gradient span到record身份所需非成员独立性/可分条件与修正证明。当前中心采用隔离，不用于正面证据或Books；具体反例/原式见§4及[同族证据](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)。
- [2604.21241 CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors](https://arxiv.org/html/2604.21241v1)：区分GT与预测anchor的正确δ定义、物理状态来源及实现桥。当前中心采用隔离，不用于正面证据或Books；具体反例/原式见§4及[同族证据](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)。
- [2604.21327 Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning](https://arxiv.org/html/2604.21327v1)：实际日志分母、token加权/代码定义或修正Eq5–7，解释何以出现正均值。当前中心采用隔离，不用于正面证据或Books；具体反例/原式见§4及[同族证据](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)。
- [2604.21391 From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges](https://arxiv.org/html/2604.21391v1)：score到路径时间导数/vector field的合法连接和条件限定，不能由起点独立直接推速度。当前中心采用隔离，不用于正面证据或Books；具体反例/原式见§4及[同族证据](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)。
- [2604.21395 Supervised Learning Has a Necessary Geometric Blind Spot: Theory, Consequences, and Minimal Repair](https://arxiv.org/html/2604.21395v1)：Gaussian唯一性、条件MI对象与TDI上界的修正/明确假设，不否定协方差恒等式。当前中心采用隔离，不用于正面证据或Books；具体反例/原式见§4及[同族证据](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)。
- [2604.21570 SpecSyn: LLM-based Synthesis and Refinement of Formal Specifications for Real-world Program Verification](https://arxiv.org/html/2604.21570v1)：refinement递推与Algorithm1过滤集合统一；不可证明与false、mutant语义非等价判据分开。当前中心采用隔离，不用于正面证据或Books；具体反例/原式见§4及[同族证据](../_sources/daily-20260424/V3_EVIDENCE_NOTES.md)。

### 来源外部终态保留项

OpenAI Research/Index历史分页、Google Research Publications本窗停点、Meta Research空正文、Moonshot2026目录、MiMo Blog14条日期及旧仓库release/私有转公开缺口分别见§2。已有目录/RSS/官方API/组织列表不能替这些缺失入口证明零更新或全站覆盖。最小重开材料是相应官方本窗历史目录/分页终点与原日期清单、或具名相关artifact的首次public记录；不扫描历年或普通PR。它们不用于无遗漏断言，不阻塞本窗已完成的安全终态验收；材料到达后只重开相应来源/家族。

窗外/贡献关闭与撤回处置只保留[原始筛选理由](../_sources/daily-20260424/V3_SCREENING_NOTES.md)，不放回候选或评分；不将窗外恢复线索冒充当前日报已审重复项。

## 6. 复核

复核者：root（日级非作者收口）；apr02、apr20_resume 的既存具名单篇非作者结果仅在身份、采用命题及证据未变的范围内复用。

结论：通过

2026-09-30 对正式 §2–5、85家族逐项准入理由、证据处置和实际 Books 对账完成日级收口；不是重新全文审计全部附件，也不继承旧V2.1完成标签。

- 来源：14个每日ID均有实际入口、停点与限制，按[独立来源对账](../_sources/daily-20260424/V3_ROOT_SOURCE_SCOPE_RECONCILIATION.md)核其使用范围；未将951 submitted库存或496宽标题变为全文队列。八项有限入口已检查，六项外部覆盖限制仍按§5隔离，不支持全站零遗漏。
- 日期：接受官方公告赋号、Thu20EDT公告槽、相邻批次与84家族原v1处理簇的组合支持08～09有界归属；处理字段不是独立的公开证明。22个具体日期例外、DeepSeek相交日期及SPIRE窗前同族均不进入确定候选。SPIRE提前公开反证已纠正本窗计数，不擅自迁入另一日报。
- 准入：逐项核正式85家族的具体机制、设计分歧或评价反证与其必要审阅，复用未变的具名单篇非作者校准。最后不改书不构成倒删候选理由；章节名称、局部应用指标和通用系统类比也不构成准入。独立校准已将14项误收转具名前分母关闭，原始证据保留；SPIRE另因日期移出。
- 负侧：按[10项分层样本](../_sources/daily-20260424/V3_ROOT_NEGATIVE_STRATA_SAMPLE.md)检查安全、检索、生产应用、Agent工具、表示与多模态类比的共享误排风险；结合[首批正反校准](../_sources/daily-20260424/V3_ROOT_FIRST_ADMISSION_AUDIT.md)、[六项消歧](../_sources/daily-20260424/V3_APR20_SIX_MINIMAL_ADMISSION_AUDIT.md)与[最后五项准入](../_sources/daily-20260424/V3_APR20_LAST_FIVE_ADMISSION.md)，具体纠错/保护反证均有具名裁决。明确范围排除没有逐条全文重读；抽样不等于证明全部负侧或外部目录无遗漏。
- 证据：44深入、26标准、15争议与§3/4逐族对应。31仅报告与10已有覆盖均有具体命题及有限非作者依据；15争议的印刷定义/推导反证已独立核验，仅作安全隔离，不证明整篇实验无效。来源、争议与日期保留项的重开条件在§5，均没有普通未读工作伪装成外部阻塞。
- Books：重新检查29个本窗整合家族的实际正文绑定（在章末Review notes之前）及相邻过渡，并对账既存写后裁决；不是只有“已吸收”标签。当前29整合、10已有覆盖、31仅报告、15争议均有最终处置，普通Books待办为0。SPIRE已核正文保留，但不计本窗产出。
- 验收范围仅是本日合同、所列有限来源与已冻结85家族；没有宣称全机构覆盖、作者实验复现、所有主张成立或生产SLO。机器校验和差异检查另列结果，不能替代上述语义验收。

原有逐族来源、owner及写后记录仍保留于本日证据目录与§4引用；本轮未重扫其它日期、未重跑旧Weekly，未stage、commit或push。
