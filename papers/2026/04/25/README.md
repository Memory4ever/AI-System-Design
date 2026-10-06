# Daily Research — 2026-04-25

**规范：** V3
**窗口：** 2026-04-24T09:00:00+08:00 ～ 2026-04-25T09:00:00+08:00
**补充窗口：** 2026-04-24 ～ 2026-04-24
**窗口说明：** 用户授权只补已有Daily来源遗漏；原候选整行、日期评分、旧小时窗及连续原§4保留，旧材料仅定点去重，不搬归属。
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-16T04:13:12+08:00

## 1. 结论

自然日补查新增20个确定材料家族：19份arXiv与DeepSeek当次API版本事实；原Kimi CLI 1.39.0整行、日期评分、旧09:00小时窗及连续原§4均保留，合21个正式候选。21921因更早项目/目录线索的首次公开日未闭合单列缺口，不凑入确定候选；同事件旧审阅不搬日或重评分。发现与筛选已经限定停止，详见[唯一补充记录](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

主要增量是把相似但不相同的对象分开：事实正确与名称访问、grammar前缀权重与神经未来条件概率、对话末轮迎合与逐轮漂移、视觉收敛与刺激选择、对象存在识别与错误预设拒绝，以及代码形态/评审人口/出题角色改变后的评价目标。模型与系统路径则新增有界缓存到类别聚合、骨架文字接口、有序视频表示、视觉场景记忆及发现顺序/控制分工。Books本次15项整合正文已保存，15项均已完成非写作者actualPOST、root接纳并释放窄锁；1项已有覆盖不改书，DeepSeek只报告API版本事实。root已实际完成六部分增量DAY并授权保存完成态；普通研究与Books工作均已落实，保存后的最小FINAL只核本次收尾状态。

21860的history/oracle与成功单位，21901的对角训练最优性，以及21101的梯度乘积/时间依赖保证各自保中心争议、暂缓Books；它们不是被删去的候选，也不令其全部局部构造/实验一刀切无效。机构历史目录和21921必要日期仍按§5外部终态隔离，不支持正面证据、性能/安全保证或“全网无遗漏”。本轮没有运行论文代码、复现实验或测试远端服务。旧报告有效Kimi研究与新证据分层复用，不继承旧完成标签。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 原actual [News RSS](https://openai.com/news/rss.xml)1230项：Apr23T10/11Z在自然日前、jobs Apr25T00Z在后；只复用该具体停点。 | 受阻 | Research/Publication历史窗口清单未恢复，RSS不证明全机构零研究。 |
| SRC-ANTHROPIC | 原actual [Research](https://www.anthropic.com/research) publishedOn Apr22T14:12/14:27Z→Apr29T20:26Z跨Apr24。 | 已检查 | 限官网可见目录，未列作者稿不声称全查。 |
| SRC-GOOGLE-AI | 原[Research April](https://research.google/blog/2026/04/)9项Apr22→29；[DiLoCo](https://deepmind.google/blog/decoupled-diloco/)既有JSON-LD Apr23T16Z=Apr24北京，与原04-24的21428已审同事件去重。 | 受阻 | Blog有限停点有效，Publications历史页缺段不由Blog替代；当前SSL失败不抹原有效原件。 |
| SRC-META-AI | 原actual Research空提取、Blog Apr8/6→Mar27混排；未取得可核Apr24的历史分页。 | 受阻 | 需官方本窗清单/有界分页；空响应不记零。 |
| SRC-QWEN | 原[目录API](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)40项Apr22T10+08→Apr28T10+08→Apr30T12+08。 | 已检查 | 可见目录跨Apr24，非所有作者稿覆盖。 |
| SRC-DEEPSEEK | 本轮actual [Apr24 News](https://deepseek.com/en/news/v4-preview/)和[APIupdates](https://api-docs.deepseek.com/updates/)Apr24核心；reader独立有限事实核验。 | 已检查 | 恢复日级release；当前标日页面非April原字节，未披露机制不采用；June论文不倒填。 |
| SRC-MOONSHOT | 原actual [CLI releases](https://github.com/MoonshotAI/kimi-cli/releases)100项Apr22→1.39 Apr24T06:22:19Z→Apr28；原1.39必要源码/Ch84真实POST复用。 | 受阻 | 同release不新计；Platform Blog四月历史段仍缺。 |
| SRC-TENCENT-HUNYUAN | 原actual官方“全部”publicList page1/100/render0，total9/list9，Apr30/23→Feb13跨Apr24。 | 已检查 | 限该可见目录，不称未列作者稿全查。 |
| SRC-ZAI | 原actual Research15项Apr29→7→1，releaseNotesJun16→Apr7→Feb12。 | 已检查 | 只按官方日级，不补钟或遍历commits。 |
| SRC-BYTEDANCE-SEED | 原actual get_article_list_v2/US：paper type1 page20/20 total242 next40，Apr25T16Z→Apr22T16Z；blog type2 page0/20 total95已到2025。当前research页April26/22局部复核。 | 受阻 | PublishDate不重定论文first-public；仅21921早目录/项目单族first-public资格受阻，其他已处理目录有效，不等全源缺失/零命中。 |
| SRC-BAIDU-ERNIE | 原actual技术Blog10条Apr30→15→Feb6→2025跨Apr24。 | 已检查 | 限技术Blog可见清单，非全公司研究。 |
| SRC-XIAOMI-MIMO | 原actual Paper8项Jun29→Mar13→Feb3跨Apr24，Blog14项缺可核发布日期。 | 受阻 | Paper停点有效；Blog需历史日期/排序原件。 |
| SRC-MINIMAX | 原actual CLI release26项Apr17T20:51:17Z→Apr26T01:40:29Z；ENBlogMay26→Mar18、CN Apr27→Mar18跨窗。 | 受阻 | Agent Tech最早可见May13，不认证四月历史段；不以CLI代研究全覆盖。 |
| SRC-ARXIV | 本轮四主题发现范围submittedDate:[202604221800 TO 202604231800]仅作常规批次线索；MODEL214首次截断后start0/50/100/150/200每50补齐，AGENT77/MULTIMODAL67/SYSTEM36返完整；官方April分类列表只title/identity查漏，CV补第二页。 | 受阻 | 宽分类不成逐项全文队列；相关/含糊才完整题摘，P以exactv1必要层审。日期公告ID/月列表/v1处理/publisher联合，Submitted/created非单证；仅21921必要first-public资格受阻，其余目录/19确定候选已处理，不否定有效层。 |
| 表外：[MemPalace官方GitHub](https://github.com/MemPalace/mempalace) | 因21284具体纠错触发，actual Issue29/8comments、pinned v3.1.0 tree与目标blob；只用Apr7审计、Apr9维护者回复及指定代码行 | 已检查 | 不采其余推广评论/新外部实验，不扩全仓库；原纠错不搬本日 |

来源复用只针对未变的具体列表、分页与邻界，不复用他日的候选池或“完成”。机构受阻历史段与arXiv日期例外精确隔离；原常规批次在旧09:00窗前、却在补充自然日内，现已按贡献与有效同事件去重处理。完整查询、停止与负侧理由见[SUP A1/A9/A16–20/A23](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。本轮不扫每周来源、Live、其他年份或普通仓库commits。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi CLI 1.39.0](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.39.0) | 2026-04-24T14:22:19+08:00 | 原始Tool schema与后端wire投影分责；默认自动发现模式下同名Skill优先级决定实际加载版本；2+2+2=6 | 深入完成 | 整合：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md) Skill作用域解析与run身份，实际正文及非作者写后通过；Ch78兼容修复先仅报告 |
| [2604.21101 A Hybridizable Neural Time Integrator for Stable Autoregressive Forecasting](https://arxiv.org/html/2604.21101v1) | 2026-04-24 | 连续神经动力学梯度易爆→mixed-FEM/mortar/SBP scaffold→稳定选择须核乘积与时间条件；2+1+2=5 | 争议 | 暂缓：仅中心梯度/长期稳定保证隔离，构造与局部实证仍报告；A29/A31 |
| [2604.21144 Using Machine Mental Imagery for Representing Common Ground in Situated Dialogue](https://arxiv.org/html/2604.21144v1) | 2026-04-24 | 纯文字易混淆可描绘实体→按POV增量场景图＋命题/关系文字→记忆表示须分工；2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)，场景图/命题与原文分责，actualPOST已通过 |
| [2604.21152 Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles](https://arxiv.org/html/2604.21152v1) | 2026-04-24 | 显式profile与dialect代理不等价→条件输出/拒绝与质量分母变化→重审cue构念；2+1+2=5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，cue构念与全部/非拒答分母 |
| [2604.21191 Prefix Parsing is Just Parsing](https://arxiv.org/html/2604.21191v1) | 2026-04-24 | 专用prefix parser实现耦合→prefix grammar＋lattice/AD全扩展权重→复用普通parser的新取舍；2+1+2=5 | 深入完成 | 整合：MODEL-SAMPLING [Ch20](../../../../books/part-02-model/20-sampling.md)，prefix grammar及条件化代数AD，actualPOST通过 |
| [2604.21360 Prototype-Based Test-Time Adaptation of Vision-Language Models](https://arxiv.org/html/2604.21360v1) | 2026-04-24 | 每类有界M样本cache需检索→C类聚合原型EMA→比较状态规模与漂移滞后；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，冻结encoder的聚合读出；A28；实际正文及非作者写后已通过 |
| [2604.21363 A Deployable Embodied Vision-Language Navigation System with Hierarchical Cognition and Context-Aware Exploration](https://arxiv.org/html/2604.21363v1) | 2026-04-24 | 发现目标即可停而非遍历全部→weighted cumulative latency＋CMG分批异步读→探索顺序与控制分权；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，weighted discovery与CMG分批；实际正文及root写后已通过 |
| [2604.21444 HiCrew: Hierarchical Reasoning for Long-Form Video Understanding via Question-Aware Multi-Agent Collaboration](https://arxiv.org/html/2604.21444v1) | 2026-04-24 | 全局视觉聚类可能混时序→ordered shot外层＋query局部展开/字幕→表示容量按问题分配；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，有序外层/局部细化，actualPOST通过 |
| [2604.21481 Preferences of a Voice-First Nation: Large-Scale Pairwise Evaluation and Preference Analysis for TTS in Indian Languages](https://arxiv.org/html/2604.21481v1) | 2026-04-24 | 只增总judgments混淆目标→rater×sentence两轴对rank/CI不同→采样预算需分责；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，采样轴与排序/精度目标；A29/A31；实际正文及非作者写后已通过 |
| [2604.21510 OptiVerse: A Comprehensive Benchmark towards Optimization Problem Solving](https://arxiv.org/html/2604.21510v1) | 2026-04-24 | 重读需求易把代码解释成原意→code-only盲回译＋需求提取再三角比较→audit输入隔离；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，盲代码回译/需求审计；A29/A31；实际正文及非作者写后已通过 |
| [2604.21564 Measuring Opinion Bias and Sycophancy via LLM-based Coercion](https://arxiv.org/html/2604.21564v1) | 2026-04-24 | 只问意见漏用户依赖→direct/debate×三persona＋末轮/逐轮分开→测输出行为非内心；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，对话行为分类与漂移分账，actualPOST通过 |
| [2604.21668 Encoder-Free Human Motion Understanding via Structured Motion Descriptions](https://arxiv.org/html/2604.21668v1) | 2026-04-24 | motion encoder对齐耦合→确定骨架事件文字＋任务LoRA→可替代输入接口及失真取舍；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，确定骨架描述；A28；实际正文及非作者写后已通过 |
| [2604.21716 From If-Statements to ML Pipelines: Revisiting Bias in Code-Generation](https://arxiv.org/html/2604.21716v1) | 2026-04-24 | if条件代理漏pipeline feature use→同任务改变代码形态并审抽取→评价对象不能互代；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，代码形态/feature use与harm分责，actualPOST通过 |
| [2604.21836 Modulating Cross-Modal Convergence with Single-Stimulus, Intra-Modal Dispersion](https://arxiv.org/html/2604.21836v1) | 2026-04-24 | 总体表示收敛混刺激人口→GPA残差分层再测跨模态邻域→对齐分数须保未筛基线；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，stimulus分层诊断，actualPOST通过 |
| [2604.21860 Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models](https://arxiv.org/html/2604.21860v1) | 2026-04-24 | 孤立轮交互的累计风险→TTI attacker/history与oracle实际路径→单轮安全口径需重核；2+2+2=6 | 争议 | 暂缓：history/oracle及success unit/PAIR预算未闭，不入Books；A12 |
| [2604.21882 Revisiting Non-Verbatim Memorization in Large Language Models: The Role of Entity Surface Forms](https://arxiv.org/html/2604.21882v1) | 2026-04-24 | 单canonical混知识与访问→同实体多surface双向flip→nonverbatim记忆测量分责；2+1+2=5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，事实/名称访问与配对测量，actualPOST通过 |
| [2604.21901 GiVA: Gradient-Informed Bases for Vector-Based Adaptation](https://arxiv.org/html/2604.21901v1) | 2026-04-24 | vector adapter高rank→gradient-informedbasis→实际对角训练最优性须核；2+1+2=5 | 争议 | 暂缓：Γ对角约束推导/任意正交B最优桥未闭，不入Books；A28 |
| [2604.21911 When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs](https://arxiv.org/html/2604.21911v1) | 2026-04-24 | 视觉识别好不等拒错误预设→固定图像改变对象存在承诺→正识别/拒预设联合验收；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，query预设与正侧反侧，actualPOST通过 |
| [2604.21916 MathDuels: Evaluating LLMs as Problem Posers and Solvers](https://arxiv.org/html/2604.21916v1) | 2026-04-24 | 固定题池只看solver→同模型author/solver双轴＋disagreement verifier→出题难度与真值分责；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，派生author分与核验盲区；A28；实际正文及非作者写后已通过 |
| [2604.21931 Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/html/2604.21931v1) | 2026-04-24 | fps/播放速率/场景运动混淆→速度等变＋绝对anchor→时间标签不能冒采集真值；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，播放速度/时钟分责；实际正文及root写后已通过 |
| [DeepSeek V4 Preview / API](https://deepseek.com/en/news/v4-preview/) | 2026-04-24 | 显式模型ID/模式与旧alias路由、退役约束改变调用兼容身份；1+2+1=4 | 已关闭 | 仅报告：当次API版本事实，未披露机制/不改长期知识；不将model ID当不可变snapshot |

本次确定新增20家族（19 arXiv＋DeepSeek），与原Kimi合21；不把同事件重复材料重列、21921资格缺口或具名前分母EX纳入。19份arXiv必要层已按采用命题处理，中心争议三项保留且不支撑正面结论；Books已落实15整合/1已有覆盖/3暂缓，另DeepSeek仅报告。15项新正文actualPOST均已通过，全部窄锁释放；root六部分增量DAY实际通过。官方公开日期只记日级；21191/v1 Updated后处理异常保留原字段，以官方月列表/公告身份及同批publisher信息联合支持Apr24，而非Submitted/DOI单证。

## 4. 证据与知识整合

### [Kimi CLI 1.39.0](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.39.0)

官方tag的`published_at=2026-04-24T06:22:19Z`属于本窗。已读release列出的schema兼容、thinking.keep、项目skill覆盖及少量消息格式修复；它们在同一版本中发布，不意味着所有相关PR首次当日公开。必要源码定位为tag `1.39.0` 的 [`kimi.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/packages/kosong/src/kosong/chat_provider/kimi.py) `_convert_tool`、[`jsonschema.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/packages/kosong/src/kosong/utils/jsonschema.py) `ensure_property_types` 及[转换测试](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/packages/kosong/tests/test_kimi_tool_conversion.py)。这一路径为provider-facing schema建副本、递归补缺失`type`，源`Tool.parameters`不被转换函数原地改写；测试包含 enum-only、已有typed字段、输入未变和builtin工具分支。代码/测试已阅读，未执行测试或模拟真实provider调用。

关键取舍是 wire 格式被某后端接受、原工具输入schema保留、运行时实际参数语义与业务授权分别验收。`ensure_property_types` 从enum/const/结构推断，不可推断时默认`string`；混合型enum或组合schema可能被收窄，不能因此说所有合法输入保持等价，也不能把静态转换测试当本地执行器已按原schema完整校验的实测。发布说明未给兼容修复的失败率、性能、线上负载或端到端correctness。

同一release的[PR2044](https://github.com/MoonshotAI/kimi-cli/pull/2044)在本窗已合并；实际读取tag中的[`skill/__init__.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/src/kimi_cli/skill/__init__.py)与[`config.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/src/kimi_cli/config.py)：默认自动发现模式下，Skill root从扁平列表变成带`project/user/extra/builtin`来源的列表，同名首个匹配遵守`Project > User > Extra(config) > Extra(plugin) > Built-in`；显式`skills_dirs`会替代Project/User自动发现并居首。系统提示按scope分组，`merge_all_available_skills`默认false→true。相同Skill名称可能因此解析到另一份正文；目录发现、最终选择和模型看到的说明应共同版本化，不能拿仅显示路径代替真实加载版本。PR声称有多项测试，本次只读必要代码与说明、未运行测试，也不认为“project优先”本身是普遍安全策略：恶意/错误项目Skill同样可能遮盖builtin，effect权限仍由独立执行器决定。`thinking.keep`及[PR2028](https://github.com/MoonshotAI/kimi-cli/pull/2028)的`skip_yolo_prompt_injection`是其他局部行为线索；后者关闭的是yolo提示注入provider，不是自动批准工具的权限开关，不能冒充prompt-injection攻击防护或授权收紧。

2+2+2=6，因已有Ch84具体缺口作必要深入。实际[Ch78 Tool Contract](../../../../books/part-07-agent/78-tool-calling.md)已明确typed schema、后端含义不稳定、schema validation、authorization与effect-time分权；其wire投影修复暂仅作局部release证据。[Ch84 Skill registry/Agent definition](../../../../books/part-07-agent/84-agent-platform.md)原已要求Skill来源、版本、权限、activation与run身份，但未具体解释同名多scope优先级如何改变已加载定义、prompt呈现与版本化运行身份之间的关系。现已在这一主线中补入作用域解析/同名遮蔽/可信admission窄条件，保留static allowlist、手工pin版本及effect-time权限作为共存和回退，不推出该CLI已验证所有环境或能防御恶意Skill。该Books提案获[非作者源→actual owner写前校准](../_sources/daily-20260425/V3_APR01_KIMI_139_INDEPENDENT.md)，[实际正文写后复核](../_sources/daily-20260425/V3_ROOT_KIMI_139_WRITE_AFTER.md)也已通过；这是单篇整合，不替代本日来源/日期/分母的独立Gate。精确证据与未验边界见[审阅笔记](../_sources/daily-20260425/V3_REVIEW_CHECKPOINT.md)。

### 贡献前关闭与日期隔离

OpenAI的[职业转型原文](https://openai.com/index/modeling-ai-jobs-transition/)在窗内，研究任务自动化、劳动需求与经济过渡；当前 AI-System-Design 的大模型/Infra机制没有因此新增可定位设计选择，故不进入候选，也不以大机构名提升分数。DeepSeek的[V4 Preview](https://deepseek.com/en/news/v4-preview/)与[API更新日志](https://api-docs.deepseek.com/updates/)确有04/24日级发布线索和模型/API版本事实，但不能以不明时区自然日证明首次公开在04/24 09:00以后；现有官方Research技术报告列06/24，不能逆向当成本窗方法全文。只保存精确日期保留项，不将“百万context/DSA”等发布描述无条件导入Books。

### Books判断

Books流程在本次范围内，没有由旧零候选跳过。Kimi的Ch78兼容修复目前仅报告；Ch84作用域解析/版本身份窄gap已实际纳入正文，非作者写后复核已通过。该单篇Books判断完成，但不能代替本日来源/日期/分母Gate。

### 自然日补充：以下新增证据不改写上方连续原§4

### [2604.21101 A Hybridizable Neural Time Integrator for Stable Autoregressive Forecasting](https://arxiv.org/html/2604.21101v1)

构造保留二阶动力学的分段状态与边界连续性，但不约束任意Transformer自动获得Hamiltonian条件。AppC1将C_J的幂吸收到未说明与N无关的常数，末界又含exp(cT/M)；固定h/M不能同时让T不随N增长，故不采用uniform-time/任意长rollout稳定保证。Lorenz同初值轨迹与shear不同容量/预训练对照只作局部证据。5分争议/暂缓，只重开乘积常数、h/T/M/N依赖或明确有限经验命题；不否定整篇所有实验、不以Science标签排除。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A29/A31](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21144 Using Machine Mental Imagery for Representing Common Ground in Situated Dialogue](https://arxiv.org/html/2604.21144v1)

exact-v1 §3–7/T1–2/Fig5/7：New/Continue/Skip按说话者视角生产示意图，非可描绘信息和跨场景关系留文字。每次五候选与自验证不生成新观察；图局部忠实仍可漏关系、Skip否定仍可误写状态。200对话的图文检索配置并非纯模态同预算，混合在inferred任务亦低于纯图；不推图像普遍更准/更便宜。Ch77确定渲染/原文日志之后已补两段，reader实际完整邻接与本人注POST、root接纳释放。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A27](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21152 Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles](https://arxiv.org/html/2604.21152v1)

exact-v1 §3/T1/§4–6.1/A2：六条件并非完整profile×dialect交叉，BERTScore/Regard不是事实/安全真值；Qwen零拒答使拒答模型主要是Gemma。1705 soft noncompletion多是固定一句completion中的澄清/回避，不等1705次policy bypass；质量只在非拒答人口计算。中心lexicalgate/dialectjailbreak因果不采用。Ch66现有cue构念与硬拒答/无效/回避、条件分母实际承载所采长期边界，root必要Source与具体NC通过，不为制造diff再写。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A24](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21191 Prefix Parsing is Just Parsing](https://arxiv.org/html/2604.21191v1)

exact-v1 §2–4/Fig1/AppB/Limitations：语法转换保前缀语言/权重，lattice、纯半环算术及theta独立控制流下反向AD取得全next-token权重；不是神经模型未来合法suffix的条件概率。输入长度依赖可保，grammar预处理仍膨胀，≤4倍仅算术ops非wallclock/HBM/SLO。Ch20 trie后两段含这些条件及费用/回退；reader必要Source/修订与actualPOST均通过，root接纳释放。v1 Updated被后处理到May5，官方月列表item1362/公告身份与Apr24同批投影合证，不重写原字段。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A13](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21360 Prototype-Based Test-Time Adaptation of Vision-Language Models](https://arxiv.org/html/2604.21360v1)

exact-v1 §3–4/T1–2/A3–A5/A8：旧缓存本就固定M/class，PTA是MC×d到C×d，不是无限增长到常数；另有文本初始化状态。各类置信度EMA与原零样本分支共存，Eq5不作硬几何锚定宣传。3090/B1/三顺序对照不是生产请求SLO，T2亦略低ADAPT；shuffle不证明突变域可靠，聚合丢样本级淘汰。reader必要Source/具体owner/PRE通过；已在已有改参数ProtoTTA之后补两段，reader实际POST通过、root接纳释放。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A28](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21363 A Deployable Embodied Vision-Language Navigation System with Hierarchical Cognition and Context-Aware Exploration](https://arxiv.org/html/2604.21363v1)

exact-v1 III/IV：anchor—对象二部图及ILP至少min(r,现有anchors数)次覆盖只保已检测对象；按任务读子图与低层控制异步，WTRP用启发式语义权重，不等目标概率或真实最优发现时间。2D跨楼、误检、小对象/运动模糊仍失败；桌面100episodes和真机每组20指令不授云最坏时限/碰撞安全。Ch26 LiveVLN后两段已按root窄lease保存，root实际POST通过、窄锁释放。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A26](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21444 HiCrew: Hierarchical Reasoning for Long-Form Video Understanding via Question-Aware Multi-Agent Collaboration](https://arxiv.org/html/2604.21444v1)

exact-v1 II/III-A–C：镜头顺序外层、相关镜头内部KMeans及类型化字幕，与多Agent读出组成路径。去整棵树同时改变采样和细节，主干相同也不隔离全部预算，不能把差额全归时间拓扑。问题集合参与字幕生产，索引不是任意未来query可复用事实；镜头/字幕/模型调用全计费。Ch23 FlexMem后两段已保存，root actual前后及本人注POST通过并释放。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A25](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21481 Preferences of a Voice-First Nation: Large-Scale Pairwise Evaluation and Preference Analysis for TTS in Indian Languages](https://arxiv.org/html/2604.21481v1)

exact-v1 §3–4：5357句/10语/7system/1915rater、BT/500bootstrap；rank correlation参照full评价而非质量真值，rank可稳定而区间仍宽。100–200rater与500/1000sentence仅该系统数/语言人口，不能当通用quota；默认voice、支持语言、cluster/tie与同人六维相关性限制保留。reader必要Source/实际Ch66/PRE通过，已在clusteredanalysis后补两段，reader实际POST通过、root接纳释放。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A29](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21510 OptiVerse: A Comprehensive Benchmark towards Optimization Problem Solving](https://arxiv.org/html/2604.21510v1)

exact-v1 §3–5/8/F2：需求分支见problem+initialmath，盲分支只见code，再合三者判差额、非空才repair。空差额不证语义正确；500抽样98.4%judge校准、goldschemakeys/数值及非数等价也不授全域真值。无仅移除blindness同calls消融，30–67s比无框架6–16s明显增加；不采无额外时间。reader必要Source/actualCh66/PRE通过，已在AgentDevel后补两段，reader实际POST通过、root接纳释放。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A29](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21564 Measuring Opinion Bias and Sycophancy via LLM-based Coercion](https://arxiv.org/html/2604.21564v1)

采用exact-v1 Coercion，不用后版Persuasion题名倒填。§3–5.6/7的三persona九bucket与逐轮drift是不同事件：首轮就顺从可有较低后续flip。user/judge agreement不是准确率或方差分解；289/299 valid、BR-Portuguese话题与freeform参数限制保留，不采“真实信念/训练唯一因果”。Ch66 PPT后两段及本人注已获root必要独核和actualPOST。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A14](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21668 Encoder-Free Human Motion Understanding via Structured Motion Descriptions](https://arxiv.org/html/2604.21668v1)

exact-v1 §3–4/T1–7：22joint坐标/角度/位移经平滑和事件阈值形成文字，top3约1k而all约4ktokens；无learnedencoder不等无训练，QA/caption各LoRA和监督。top3可好问答却伤caption，trajectory去除也非全指标退；同语言主干不匹配所有预训练预算。H200下915–1154ms只给定QA输出，非一般加速/因果attention。reader Source/owner/PRE通过，已在camera-motion旁侧读出之后补两段，reader实际POST通过、root接纳释放。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A28](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21716 From If-Statements to ML Pipelines: Revisiting Bias in Code-Generation](https://arxiv.org/html/2604.21716v1)

exact-v1 §3–7/Limitations/A1/B1/B3：350prompt、不同codeforms与nonsense属性控制；CBS是属性进入决策的代理，不是全代码执行/训练后伤害，也不作法律断言。126手标样本的extractor准确不认证全域，各正文总比例冲突不拼倍率；usage识别分数与生成不用是不同事件。Ch66人口cue之后两段已保存并由root实际两侧/本人注POST通过。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A25](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21836 Modulating Cross-Modal Convergence with Single-Stimulus, Intra-Modal Dispersion](https://arxiv.org/html/2604.21836v1)

exact-v1 §2–4/S1–2：4视觉encoder、WIT1024配对、12LM，GPA残差mean/PC1切高低分歧再CKNNA(k10)。同刺激拟合/分层、LM取最佳层；held-out视觉模型不等新刺激或新dataset泛化。只说明选择输入可改变convergence评价，不证明模型训练变接近或共享真实世界。Ch23 GPA后两段、费用/反侧及本人注经reader actualPOST/root接纳。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A12](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21860 Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models](https://arxiv.org/html/2604.21860v1)

exact-v1 IV/V/VI-C：intro说只保留last response，formal attacker却看累计history；target是独立M(pi)，不能说无状态目标内部alignment被逐轮腐蚀。formal unsafe即停oracle与实验未具名classifier关系未闭；17/50=34%又被表写hits，PAIR共同分母/预算不明。API远端不能借ColabT4冒硬件，安全排名/优越与全费用均不采用。6分争议保留，不因中心桥失败退EX；需history权限、oracle身份和统一成功单位/预算后重开。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A12](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21882 Revisiting Non-Verbatim Memorization in Large Language Models: The Role of Entity Surface Forms](https://arxiv.org/html/2604.21882v1)

exact-v1 §2–4/Limitations/B2/B4/B5：固定实体/关系/答案而变surface，13模型配对双向correctnessflip；both-wrong一致不等可靠。频率控制限可见语料子集且仅相关，B5不是内部实体地址识别。Ch5 rate-distortion后两段保命名访问/事实正确、全费用与未证明边界，reader actual179–211/本人注及diff POST、root接纳释放。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A4](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21901 GiVA: Gradient-Informed Bases for Vector-Based Adaptation](https://arxiv.org/html/2604.21901v1)

exact-v1 §3/Eq1–5/AppA/§4/5/6：Γ=diagγ，但Eq3→4按full矩阵梯度优化，漏对角投影。reader最小G=diag(2,1)、A=[1,0]、正交B=[0,1]ᵀ反例：真首步0/误差²5而放松式给误差²1，故任意正交B实际首步最优未证；不是所有实验失效。单seedinstruction/参考loss选LR、完整SVD/状态成本保留，root接纳5分争议。修正diag/B资格或明确经验启发式并给必要对照后重开。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A28](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21911 When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs](https://arxiv.org/html/2604.21911v1)

exact-v1 §3–5/T1–4/A2/B/C1/D/E：同图present/random absent/plausible absent和false-presupp问法有诊断价值，detector+LVLM缺席仍代理标签，yes/no与自由拒预设不同。DPO后缺席否认改善但正识别94.85→84.30，高对比集偏拒绝，短caption也可降低幻觉；不唯一归因视觉backbone无错。Ch23 MOH后两段保生成/验证/调参全费与联合验收，reader actualPOST/root接纳。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A12](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21916 MathDuels: Evaluating LLMs as Problem Posers and Solvers](https://arxiv.org/html/2604.21916v1)

exact-v1为Evaluating LLMs as Problem Posers and Solvers；19models每人30题570，去11invalid后559×18答案。author分是题难均值派生、错误gold收益封顶、等权综合是价值选择；不能叫通用创造能力。只在至少一非author答案不等gold才verify，全体共错可漏，414触发题再judge高agreement不授全池truth。新增模型题数275与每人30口径冲突，自动抬高难度的定量结论不采；reader Source/owner/PRE通过；Ch66所示位置两段已实际保存，reader实际POST通过、root接纳释放。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A28](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [2604.21931 Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/html/2604.21931v1)

exact-v1 §3/§5.1–5.2/C1等必要层：原声pitch弱标速度切换，视觉估速的k倍等变只定相对尺度，已知速率样本校准绝对值。检测测试只留人工/弱标签同意片段，连续速度111视频由网页title/description确认，两套人口不混；慢动作本身/低运动会误导。只采用时间身份和标注接口，不采生成/超分SOTA或物理动力学保证。Ch23时间provenance处两段已按修订PRE保存，root actualPOST通过、窄锁释放。 具体必要位置、费用/未披露字段、独立角色与逐字PRE见[唯一补充记录 A26](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### [DeepSeek V4 Preview / API](https://deepseek.com/en/news/v4-preview/)

官方Apr24 News与APIupdates足以恢复新增自然日资格；原小时窗的09:00隔离只保原历史语义，不据它继续阻止日级事实。采用保base_url、显式v4-pro/flash model ID与mode、旧chat/reasoner当期转Flash对应模式及July24退役预告；不认为ID是不可变snapshot，当前标Apr24页也不是历史原字节冻结证据。1+2+1=4，已关闭/仅报告：版本兼容事实不新增长期机制；token-wisecompression/DSA/1M虽被披露，但April核心无足够受控方法，June技术稿不倒填，也未测API/权重/性能。reader实际有限核心独核、root接纳，见[SUP A18/A30](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。

### 补充去重、具名排除与采用边界

原04-24的21330/21215/21523等同精确v1事件已有有效必要证据与Books处置，本日仅定点复用，不搬原日期/评分或重计新增；最初暂定重复提案已撤并保留更正路径。21284并非自动与旧artifact同族：Apr7 Issue29/Apr9维护者已公开核心recall_any≠QA与top-k bypass纠错，新论文增加的架构归纳/星级框架未形成额外项目设计增量，故经root实际最小primary校准具名前分母关闭。21344的human/MLM问题来自不同图像/难度人口，27.4%总体差不单独构成author/evaluator新条件；21748的event/timestamp聚合与synthesis未增加新资格/失效控制，按旧具体EX复用。21282三prompt+local review不是新game机制，zeroAPI并非总免费、local约50s推翻3x全流程宣传，具名安全费用信号已独立实际核，仍EX。各项支持和反侧保在[SUP A9/A15–17/A23/A28/A30](../_sources/daily-20260425/SUP_SOURCES_20261016.md)，不因关键词/小模型/已有owner排除。21921 early project/目录归属不确定仅见§5，不假装已按Apr24完成正面Source。

## 5. 缺口与下一步

普通研究与Books可执行工作为0：本稿完整六部分非作者DAY已通过，15项新Books实际POST均已完成并获root接纳，所有本轮窄锁释放。保存完成态后的最小FINAL仅核行政收尾，不重复Source、POST或DAY；其他必要Source、准入与具体Books判断已处理到有限安全终态，不再扩查或重复原证。

外部终态保留项如下；这些不支持正面证据、Books或无遗漏断言，到材料到达时仅按具体条件定点重开受影响族/来源：

- 机构历史目录：OpenAI Research/Publication、Google Publications、Meta Research、Kimi Platform Blog、MiMo Blog、MiniMax Agent Tech尚缺可复核Apr24历史分页/原始清单。需相应官方窗口清单、日期排序及停止位置；RSS/Blog或空响应不能替它们签全覆盖。已穷尽本轮可用有界入口，不要求无界重抓。
- [2604.21921 Context Unrolling](https://arxiv.org/html/2604.21921v1)：Apr24 arXiv公开合证并不能消除更早Seed Apr23目录metadata/项目仅标April2026的同核心线索；缺早正文或项目release实际公开日与内容归属。复用[原有效必要层/原件定位](../_sources/daily-20260424/SUP_SOURCES_20261015.md)，不评分、不列确定当窗candidate、不Books；取得官方日级早正文/原始项目发布后只重该族，不搬旧归属或追全月。
- [21860 TTI](https://arxiv.org/html/2604.21860v1)：需要一致的attacker/target可见history与formal/experimental oracle身份、成功单位及PAIR预算；当前中心安全优越/排名不能采用。保有限事实，不把架构或所有实验清空。
- [21901 GiVA](https://arxiv.org/html/2604.21901v1)：需要修正Γ对角约束的真实梯度/具体B资格，或明确退回经验启发式并给其必要对照；当前首步最优桥不正面采用。局部实验保留，不反推皆无效。
- [21101 HNODE](https://arxiv.org/html/2604.21101v1)：需补C_J乘积吸收常数、h/T/M/N依赖条件的正确证明，或收窄有限经验稳定并给对应证据；当前不授任意长rollout/全时间梯度保证，不否定所有构造与实验。
- DeepSeek已核Apr24有限API版本事实；缺当次可核机制细节时只报告，不以June技术报告倒填。若以后出现April同版本原始方法，仅重相应拟采用命题，不追无关版本/精确秒。

本轮不把以上外部资格或中心主张争议伪装为Source正面通过；其余具名前分母关闭若无新notice或实质反例，不因版本号变化重跑。Books现有及并发修改保留，不stage、commit、push，不由作者写LS/index。

## 6. 复核

复核者：root（非日报作者）；supp_apr25_review_fresh（独立准入/必要Source/指定actualPOST，非报告或Books写作者）。

结论：通过

root完整六部分增量DAY及15项新整合非作者实际POST通过，已授权保存完成态；最小FINAL仅核保存后的收尾状态。

已发生范围见[唯一SUP A10–15/A19/A21/A23–31](../_sources/daily-20260425/SUP_SOURCES_20261016.md)：首四/两代表EX由root校准；去重修正撤三重复新增；reader有限13及后25题摘/指定最小门事实、旧EX复用/current notice、部分必要Source/实际owner与POST已完成；root互斥必要Source/具体EX、字面/写位协调及对应POST已完成。共19份新arXiv需要的必要层按采用命题获独立处理，不等所有主张成立，三中心D明确隔离；DeepSeek reader有限核心独核4分Only。最后五份正文已由reader实际完整两侧/本人注/diff POST并获root接纳，15项新整合全部落实、无窄锁；旧Kimi有效必要代码/真实POST只复用，不重计新整合。

其余明确EX按来源/主题/理由分层校准：21478/21104（非泛化地理/Science硬排）、21193/21003（NLI/外循环命名）、旧六具名EX、21344/21748（最小门事实）、21284（原Issue/维护者/代码纠错归属）、21282（安全/费用信号）均有实际范围；不是无差别独核全部缓存。root实际读新20全部§4及§1/2/3/5/6、来源与查询停止边界、EX分层范围，确认15I/1NC/3D/1Only与21921单族资格隔离、Books真实落实及六部分一致；旧Kimi身份/v/命题未变层仅有效复用，不声称重新全文审老或继承旧完成标签。另实际机器核21=原1＋新20、原候选各一次/旧窗口/连续原§4保留、14 Daily ID、本地引用零缺失、围栏与六标题、V3及限定diff0；这些静态检查与已发生的语义DAY分别记账，见[SUP A33](../_sources/daily-20260425/SUP_SOURCES_20261016.md)。
