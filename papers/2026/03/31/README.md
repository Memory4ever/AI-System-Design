# Daily Research — 2026-03-31

**规范：** V3
**窗口：** 2026-03-30T09:00:00+08:00 ～ 2026-03-31T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-13T04:27:44+08:00
**窗口说明：** 用户授权仅补遗漏；原窗口、候选日期/评分及连续§4逐字冻结，旧完成声明不代替本轮验收。
**补充窗口：** 2026-03-30 ～ 2026-03-30

## 1. 结论

本轮仅补 **2026-03-30 北京时间完整自然日**。原窗口/旧0候选和连续§4逐字保留，最终归并冻结 **45个新增唯一家族**：**26项实际Books整合/refine、1项具体已有覆盖、5项5分仅报告、12项4分局部关闭、1项中心证明资格争议隔离**。全部已达到相应必要审阅要求与具体处置；26处真实正文、完整邻接及自身静态注已经非写入者实际POST接纳。Ask撤回原Planning重复后只计canonical Workflow一次refine，RPS也只计既有family一次refine。必要审阅不代表作者全部主张、附件、代码、实验复现或生产保证。

26项采用横跨表示读出、训练中间量复用、token-layer路由、调度profile、教程reference、生成正则/删除、GPU指令归因与片上collective。RPS是对既有同family局部的最小refine，不重复计为两处新机制；能耗模型不授整机物理归因、片上RTL/解析结果不授跨GPU训练实现。普通扫描/准入/必要Source与Books落实待办0；来源限制已定点隔离，六部分最终独立DAY已经root实际验收通过，本轮作者不自行增加日级分子。

补查发现采用四个主题窄query与受影响尾片；同Agent/eval窗口中段漏掉的5个title已定点补齐，不扩55篇全文。151跨查询槽、46个cs.DC月页title及63份精确v1完整题摘均是不同层的检查量，不是当日贡献分母；题摘潜力不等必要实验审阅完成。Qwen字段日期冲突、arXiv必要公告日门与机构历史slice继续隔离，不支撑正面覆盖或“无遗漏”。

补查前原报告以旧小时窗确认0候选，其36题摘/34日期/具名关闭仍作为原窗口记录保留；旧root通过与普通0只是该轮结果，不代替当前补查。旧稿及旧停点见[V3旧稿快照](../_sources/daily-20260331/V3_LEGACY_REPORT.md)与[V3停点](../_sources/daily-20260331/V3_WORKING_STOPPOINT.md)；当前实际分层与剩余工作见[本轮停点](../_sources/daily-20260331/SUP_WORKING_STOP_20261012.md)。

## 2. 来源覆盖

本轮仅检查03-30自然日的主线主题，14个每日来源全部已执行到下列有限停止或精确外部隔离位置；不扫描每周组，不由机构宽目录生成逐篇队列。补查执行跨2026-10-12～13；本轮官方投影见[原字段](../_sources/daily-20260331/SUP_OFFICIAL_FIELDS_20261012.json)，完整入口/参数/停止与分层理由见[本轮停点](../_sources/daily-20260331/SUP_WORKING_STOP_20261012.md)。未变化的身份/日期层定点复用原件，不复用别日候选/评分或用Weekly反推。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方RSS](https://openai.com/news/rss.xml)当前403，复用本日有效1242项/757893B的[原pubDate投影](../_sources/daily-20260331/V3_OPENAI_RSS_FIELDS.json)，只读Mar29–Apr1三邻接。Mar29T22:15GMT为03-30BJT06:15，属于补窗；Disaster workshop/customGPT核心仅已有方法应用，具体贡献前关闭。31T13Z融资/Apr1T02Z GradientLabs窗外，停止三邻接，不读1242正文 | 已检查 | 无；仅此有限RSS日期/核心范围，不授整个历史站点无遗漏 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)当前403/可见页较晚；有效March Sanity九条title/publishedOn定点复用[原字段位置](../_sources/daily-20260320/V3_WORKING_STOPPOINT.md)。Mar24T10:41Z→Mar31T22:17Z之间未见03-30；只Research九条，不外推News/全档案 | 已检查 | 无；当前访问失败不抹去有效原目录日层，也不补授全部历史覆盖 |
| SRC-GOOGLE-AI | [March Blog](https://research.google/blog/2026/03/)12卡/page1与[原page2两卡](../_sources/daily-20260305/V3_OFFICIAL_RECOVERY_12.md)Mar6/4定点复用；两Mar31核心是补窗外原N3/N4，保原处置。DeepMind真实[page3](https://deepmind.google/blog/page/3/)24卡、六March≤26日有限停止；pubs当前1–15/11569，2026filter372不是目标历史slice | 受阻 | H1仅pubs本窗dated历史slice；不把可见Blog有限停止当全部publication覆盖 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)0行；[Blog](https://ai.meta.com/blog/)当前页10卡+真实Nextpage2十二非时序卡，Mar26/27→Apr6/8；[有效/results444原文](../_sources/daily-20260325/V3_RAW_META_PUBLICATIONS.md)仅当前Sep/Aug。停止Blog两页，不扩全部题摘 | 受阻 | H2仅Research/publication目标历史slice；0行不是零命中 |
| SRC-QWEN | 官方API本轮40个title/path/extra.date有限投影；Omni同id/path的extra.date03-30T04+08与body01-07冲突，必要[机制核心](../_sources/daily-20260331/SUP_QWEN_CORE_20261012.txt)已读。定点同family官方发布/card入口、AlibabaCloud地区availability及Tongyi原thread恢复未闭首次公开日；停止这些原入口，不选更合理字段 | 受阻 | Qwen3.5-Omni必要首次公开日门；不评分/不进Books，不用Apr17论文回填 |
| SRC-DEEPSEEK | [en/news](https://www.deepseek.com/en/news/)Next16与有限Research脚本JSON，定点复用[原9467B数组字段](../_sources/daily-20260320/V3_WORKING_STOPPOINT.md)。NewsApr24/Sep10→2025、ResearchFeb25→Jun24跨补窗，包含hidden字段恢复；停止有限News/Research，不由旧platform止2025推2026无研究 | 已检查 | 无；不授全历史召回 |
| SRC-MOONSHOT | [真实Kimi en/blog](https://www.kimi.com/en/blog)19个dated卡，Feb9→Apr20跨补窗，停止19；不扩旧平台或GitHub全repo | 已检查 | 无；仅可见dated列表 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)生产publicList POST(renderType0/pageNum1/pageSize20)，code0、返回11/total11；11 title/id/published/display成对核，原秒字段保停点。Feb3/13之后相邻100061 displayApr23但publishedJun24，不能互换为firstpublic；停止11 | 已检查 | 无；公开/展示字段不混用 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)15卡Mar15→Apr1；[release](https://docs.z.ai/release-notes/new-released)16个dates/models，Feb12→Apr7跨补窗；有限两目录停止 | 已检查 | 无；不扩全部模型repo |
| SRC-BYTEDANCE-SEED | 本轮同API/year2026/count100/order_descfalse四个窄投影：[字段](../_sources/daily-20260331/SUP_OFFICIAL_FIELDS_20261012.json)。Blog token0返回9/total23/next20，token20返回3/total23/next空；Paper token20返回14/total82/next40，token40返回2/total82/next60（可见Apr7/21）。实际标题/date已读到这些停止，旧20/82、14/19及Mar31首条原raw只作历史证据，不冒当前值 | 受阻 | H4仅目标窗未返回身份/日期及统计口径差额；不由total机械推出11新论文或全82队列，不声称当前Paper40有旧Mar31首条 |
| SRC-BAIDU-ERNIE | [ZH Blog](https://ernie.baidu.com/blog/zh/)当前10卡May/Apr→Feb/Jan→2025跨补窗，停止当前页，不扩所有repo | 已检查 | 无；不授机构全部历史 |
| SRC-XIAOMI-MIMO | [首页](https://mimo.xiaomi.com/)有限GET，Paper8 dated June29→Mar13/Feb3→2025与Blog15 nondated标题；Pro/Omni正确原route及[原官方March18日期](../_sources/daily-20260320/V3_WORKING_STOPPOINT.md)定点复用、属补窗前，不重读body | 受阻 | H3仅目标datedBlog历史slice；不是Pro/Omni正文缺失，不扩15 body |
| SRC-MINIMAX | [EN](https://www.minimax.io/blog)12/[CN](https://www.minimaxi.com/blog)13 dated卡，Mar18→May26EN/Apr27CN；ForgeENFeb14/CNFeb12各留原口径。AgentTech[有效actual.md](../_sources/daily-20260319/V3_SOURCE_STOPPOINTS.md)仅May13当前dated行，窗外且无具体补窗线索；停止这些目录 | 已检查 | 无；不虚造整个TechBlog历史缺口 |
| SRC-ARXIV | [四主线窄主题](../_sources/daily-20260331/SUP_THEME_DISCOVERY_20261012.json)submittedDate[202603261800 TO 202603271800]、asc start0/max25，total1/31/32/55返回76跨主题槽；[三个受影响desc尾片](../_sources/daily-20260331/SUP_TOPIC_TAIL_20261012.json)同窗共75槽；同Agent/eval [start25/max5](../_sources/daily-20260331/SUP_TOPIC_MIDDLE5_20261013.json)只恢复中段5标题。cs.DC月页skip300/show50实际46 title-only，相关26435/26438完整AB/date定点补，26965窗外。63唯一精确v1完整AB=45候选+14具体EX+3日门+1窗外；Cognis另为April标题止。公告下界与实际arxiv.content/findable上界闭03-30自然日，不把Submitted/registered当精确公告 | 受阻 | 26845/26846/28651必要公开范围跨30–31，另原D1–D34小时窗请求保留；不授全分类/全学科召回或宽列表全negative |

以上8源有限已检查、6源受阻，不把隔离项标为Coverage通过。官方day-only按官方日值；相关/含糊题摘及安全反侧逐批独立校准，明确无贡献者具体停止，候选证据与Books处置见§3–4。

63题摘中的14具名贡献前关闭均经root定点校准，完整v1题摘保存在[主批](../_sources/daily-20260331/SUP_AB_DATE_20261012.json)、[额外批](../_sources/daily-20260331/SUP_AB_EXTRA_20261012.json)及[中段](../_sources/daily-20260331/SUP_AB_MIDDLE5_20261013.json)：MAGNET25813四组件/三case未新增执行或合并协议；SAEholism26207论辩未新增模型机制/可核反证；26100/26085 recommendation两blueprint未披露新控制/正确性接口；DataFlex26164成熟注册/缓存/cadence接口未新增无中心协调一致性或故障保证；uncertainty26363重表述既有filter/entropy/cluster未改变采用条件；Hand26362局部label阈值/LoRA未提供新controlled边界；Clawed26221借成熟policy/isolation/provenance的未来scorecard未验证新协议；AmongUs26635角色/语言相关未修正具体执行设计；MemBoost26557固定重复流的cache+MC oracle未测新reuse资格/近似误命中；Quantum26494仅1/2qubit序列与noise，没有直连本项目模型机制的新桥；openness26539版本/compound归因建议未新增推断条件；Knowdit26270既有KG/fuzz/reflection领域应用未新增LLM执行验证合同；disability26252成熟grounding协作的三层角色未新增协议/干预/可靠性边界。相关模糊或安全信号只读决定core（Clawed实际§6.2/6.3/7，不扩其50论文）；其余明确标题线索未宣全量negative，领域、综述或任务数标签均不是排除理由。

## 3. 候选与判断

原窗口确定候选0不搬移旧日期；补03-30自然日最终冻结新增45家族，全部必要审阅/具体处置已完成，26真实整合与1具体已有覆盖均经独立复核。公开日采用实际arxiv.content/findable上界与常规公告下界的复合日级证据，不把Submitted或registered冒称精确公告时刻。日门隔离项不列为确定候选，也不把来源/title/AB槽位计入45。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Do All Vision Transformers Need Registers? A Cross-Architectural Reassessment](https://arxiv.org/abs/2603.25803v1) | 2026-03-30 | 跨架构分开norm、attention与实际读出；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[MULTIMODAL-REPRESENTATION](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，具体位置见§4及必要证据；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_25803_20261012.md) |
| [Second-Order, First-Class: A Composable Stack for Curvature-Aware Training](https://arxiv.org/abs/2603.25976v1) | 2026-03-30 | snapshot→实际update→控制信号复用分责；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-PRETRAINING`，[TRAIN-PRETRAINING](../../../../books/part-04-training-system/28-pretraining.md)，具体位置见§4及必要证据；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_25976_20261012.md) |
| [Switch Attention: Towards Dynamic and Fine-grained Hybrid Transformers](https://arxiv.org/abs/2603.26380v1) | 2026-03-30 | token-layer动态路由与budget/proxy资格；2 + 2 + 2 = 6 | 深入完成 | 整合：`MODEL-LONG-CONTEXT`，[MODEL-LONG-CONTEXT](../../../../books/part-02-model/22-long-context.md)，具体位置见§4及必要证据；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26380_20261012.md) |
| [Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal Large Language Model Inference](https://arxiv.org/abs/2603.26498v1) | 2026-03-30 | latency×KV分类、per-model profile与aging/SLO边界refine；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-SCHEDULING`，[INFER-SCHEDULING](../../../../books/part-05-inference-system/56-inference-scheduling.md)，具体位置见§4及必要证据；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26498_20261012.md) |
| [Dynamic Tokenization via Reinforcement Patching: End-to-end Training and Zero-shot Transfer](https://arxiv.org/abs/2603.26097v1) | 2026-03-30 | 离散切分策略与硬token预算接口；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[MULTIMODAL-REPRESENTATION](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，具体位置见§4及必要证据；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26097_20261013.md) |
| [GUIDE: Resolving Domain Bias in GUI Agents through Real-Time Web Video Retrieval and Plug-and-Play Annotation](https://arxiv.org/abs/2603.26266v1) | 2026-03-30 | 实时教程检索提供reference而非directive；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-PLANNING`，[AGENT-PLANNING](../../../../books/part-07-agent/79-planning.md)，具体位置见§4及必要证据；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26266_20261013.md) |
| [The Limits of Learning from Pictures and Text: Vision-Language Models and Embodied Scene Understanding](https://arxiv.org/abs/2603.26589v1) | 2026-03-30 | 人类条件描述分布与解释干预分责；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，具体位置见§4及必要证据；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26589_20261013.md) |
| [Finding Distributed Object-Centric Properties in Self-Supervised Transformers](https://arxiv.org/abs/2603.26127v1) | 2026-03-30 | 同型Q/K/V相似与跨层/head对象读出；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[MULTIMODAL-REPRESENTATION](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，具体位置见§4及必要证据；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26127_20261013.md) |
| [DiReCT: Disentangled Regularization of Contrastive Trajectories for Physics-Refined Video Generation](https://arxiv.org/abs/2603.25931v1) | 2026-03-30 | negative条件、输出方向与参数梯度分责；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[MULTIMODAL-GENERATIVE-PARADIGMS](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，具体位置见§4及必要证据；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_25931_20261013.md) |
| [Neighbor-Aware Localized Concept Erasure in Text-to-Image Diffusion Models](https://arxiv.org/abs/2603.25994v1) | 2026-03-30 | 局部概念删除与neighborhood保留验收；2 + 1 + 2 = 5 | 深入完成 | 整合：`PLATFORM-SECURITY`，[PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)，具体位置见§4及必要证据；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_25994_20261013.md) |
| [Wattchmen: Watching the Wattchers -- High Fidelity, Flexible GPU Energy Modeling](https://arxiv.org/abs/2603.26435v1) | 2026-03-30 | 指令归因与总device/整机measurement分责；2 + 1 + 2 = 5 | 深入完成 | 整合：`PLATFORM-COST`，[PLATFORM-COST](../../../../books/part-06-ai-infrastructure/70-cost.md)，具体位置见§4及必要证据；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26435_20261013.md) |
| [A Lightweight High-Throughput Collective-Capable NoC for Large-Scale ML Accelerators](https://arxiv.org/abs/2603.26438v1) | 2026-03-30 | 片上router借FPU与mask/争用资格；2 + 1 + 2 = 5 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING`，[TRAIN-DISTRIBUTED-TRAINING](../../../../books/part-04-training-system/36-distributed-training.md)，具体位置见§4及必要证据；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26438_20261013.md) |
| [On the Expressive Power of Contextual Relations in Transformers](https://arxiv.org/abs/2603.25860v1) | 2026-03-30 | coupling表示定理的support/supnorm桥资格争议；2 + 1 + 2 = 5 | 争议 | 暂缓：必要选择桥反例隔离，不判主定理必假；[依据](../_sources/daily-20260331/SUP_SOURCE_DISPUTE_25860_20261012.md) |
| [H-Node Attack and Defense in Large Language Models](https://arxiv.org/abs/2603.26045v1) | 2026-03-30 | 内部probe可被操纵而不改善外部行为；2 + 1 + 2 = 5 | 深入完成 | 仅报告：已有具体行为/内部sensor分责，不新增防御保证；[依据](../_sources/daily-20260331/SUP_SOURCE_REPORT_26045_20261012.md) |
| [Gaussian Shannon: High-Precision Diffusion Model Watermarking Based on Communication](https://arxiv.org/abs/2603.26167v1) | 2026-03-30 | 完整payload恢复与检测工作点分账；2 + 1 + 2 = 5 | 深入完成 | 仅报告：成熟LDPC/repeat局部恢复配方不新增来源认证条件；[依据](../_sources/daily-20260331/SUP_SOURCE_REPORT_26167_20261013.md) |
| [Maintaining Difficulty: A Margin Scheduler for Triplet Loss in Siamese Networks Training](https://arxiv.org/abs/2603.26389v1) | 2026-03-30 | 局部adaptive margin阈值步增配方；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部单组件优化，不升重要通用机制；[依据](../_sources/daily-20260331/SUP_ADMISSION_CORE_26389v1_20261012.txt) |
| [FairLLaVA: Fairness-Aware Parameter-Efficient Fine-Tuning for Large Vision-Language Assistants](https://arxiv.org/abs/2603.26008v1) | 2026-03-30 | CLUB surrogate与LoRA/projector交替冻结更新；1 + 1 + 2 = 4 | 已关闭 | 仅报告：成熟MI+PEFT在人口上的局部组合，无新一般有效性边界；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26008_20261013.md) |
| [Policy-Guided World Model Planning for Language-Conditioned Visual Navigation](https://arxiv.org/abs/2603.25981v1) | 2026-03-30 | policy prior暖启与latent terminalcost MPPI局部配方；1 + 1 + 2 = 4 | 已关闭 | 仅报告：收益不新建一般初始化/规划边界；[依据](../_sources/daily-20260331/SUP_ADMISSION_25981v1_20261013.txt) |
| [ViGoR-Bench: How Far Are Visual Generative Models From Zero-Shot Visual Reasoners?](https://arxiv.org/abs/2603.25823v1) | 2026-03-30 | visual reasoning局部hypothesis与常规GT评价；1 + 1 + 2 = 4 | 已关闭 | 仅报告：规模曲线未识别新受控因果或适用条件；[依据](../_sources/daily-20260331/SUP_ADMISSION_25823v1_20261013.txt) |
| [DFM-VLA: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching](https://arxiv.org/abs/2603.26320v1) | 2026-03-30 | 离散action CTMC局部参数化与末greedy；1 + 1 + 2 = 4 | 已关闭 | 仅报告：借用成熟DFM与新action应用，不认证动作距离/收敛；[依据](../_sources/daily-20260331/SUP_SOURCE_PREP_26320_20261013.md) |
| [MemCam: Memory-Augmented Camera Control for Consistent Video Generation](https://arxiv.org/abs/2603.26193v1) | 2026-03-30 | 逐target视野覆盖与条件空间压缩；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[MULTIMODAL-WORLD-MODELS](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，具体位置见§4及必要证据；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26193_20261013.md) |
| [Towards GUI Agents: Vision-Language Diffusion Models for GUI Grounding](https://arxiv.org/abs/2603.26211v1) | 2026-03-30 | anchor可见/extent全mask的结构条件与预算；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[MULTIMODAL-GENERATIVE-PARADIGMS](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，具体位置见§4及必要证据；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26211_20261013.md) |
| [IP-Bench: Benchmark for Image Protection Methods in Image-to-Video Generation Scenarios](https://arxiv.org/abs/2603.26154v1) | 2026-03-30 | 派生image扰动存留与consumer效果、frame/video代理分账；2 + 1 + 2 = 5 | 深入完成 | 整合：`PLATFORM-SECURITY`，[PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)，输入保护两段后；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26154_20261013.md) |
| [MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization](https://arxiv.org/abs/2603.25973v1) | 2026-03-30 | 同用户来源资格须绑定ranking/rating目标；2 + 1 + 2 = 5 | 深入完成 | 整合：`AGENT-MEMORY`，[AGENT-MEMORY](../../../../books/part-07-agent/77-memory.md)，content/length段后；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_25973_20261013.md) |
| [Mitigating the Reasoning Tax in Vision-Language Fine-Tuning with Input-Adaptive Depth Aggregation](https://arxiv.org/abs/2603.26330v1) | 2026-03-30 | 跨boundary中间状态检索与层内适配分责；2 + 1 + 2 = 5 | 深入完成 | 整合：`MODEL-TRANSFORMER-LAYER`，[MODEL-TRANSFORMER-LAYER](../../../../books/part-02-model/17-transformer-layer.md)，ExoFormer两段后、Norm前；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26330_20261013.md) |
| [MPDiT: Multi-Patch Global-to-Local Transformer Architecture For Efficient Flow Matching and Diffusion Model](https://arxiv.org/abs/2603.26357v1) | 2026-03-30 | 单forward粗细token不同深度计算预算；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[MULTIMODAL-GENERATIVE-PARADIGMS](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，并行与少步生成标题后；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26357_20261013.md) |
| [Realtime-VLA V2: Learning to Run VLAs Fast, Smooth, and Accurate](https://arxiv.org/abs/2603.26360v1) | 2026-03-30 | 已有retime/MPC/HITL的局部实机配方；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部配方/受限代理不改变长期机制；[依据](../_sources/daily-20260331/SUP_SOURCE_26360v1_20261013.txt) |
| [VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation](https://arxiv.org/abs/2603.26666v1) | 2026-03-30 | 成熟on-policy distillation用于VLA的局部更新；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部配方/受限代理不改变长期机制；[依据](../_sources/daily-20260331/SUP_SOURCE_26666v1_20261013.txt) |
| [Vision2Web: A Hierarchical Benchmark for Visual Website Development with Agent Verification](https://arxiv.org/abs/2603.26648v1) | 2026-03-30 | 网站功能节点与视觉评价的局部校准；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部配方/受限代理不改变长期机制；[依据](../_sources/daily-20260331/SUP_ADMISSION_26648v1_20261013.txt) |
| [Reflect to Inform: Boosting Multimodal Reasoning via Information-Gain-Driven Verification](https://arxiv.org/abs/2603.26348v1) | 2026-03-30 | 自产trace训练与代理grounding/IG权限分开；2 + 1 + 2 = 5 | 深入完成 | 仅报告：局部配方/受限代理不改变长期机制；[依据](../_sources/daily-20260331/SUP_SOURCE_REPORT_26348_20261013.md) |
| [Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents](https://arxiv.org/abs/2603.26233v1) | 2026-03-30 | detector/执行clarification gate最小refine；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-WORKFLOW`，[clarification gate原段最小refine](../../../../books/part-07-agent/81-workflow.md)；[依据](../_sources/daily-20260331/SUP_ASK_OWNER_MERGE_PRE_20261013.md) |
| [VGGRPO: Towards World-Consistent Video Generation with 4D Latent Reward](https://arxiv.org/abs/2603.26599v1) | 2026-03-30 | latent geometry evaluator旁路与配对校准；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[metric-geometry后、Plan前](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26599_20261013.md) |
| [InstaVSR: Taming Diffusion for Efficient and Temporally Consistent Video Super-Resolution](https://arxiv.org/abs/2603.26134v1) | 2026-03-30 | 输入重排与自产SR buffer训练条件人口；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Training/Inference mismatch，SF05966两段后](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26134_20261013.md) |
| [Why Models Know But Don't Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models](https://arxiv.org/abs/2603.26410v1) | 2026-03-30 | 同影响人口两生成text渠道与detector/cap分账；2 + 1 + 2 = 5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[CoT instrument两段后](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26410_20261013.md) |
| [PerceptionComp: A Video Benchmark for Complex Perception-Centric Reasoning](https://arxiv.org/abs/2603.26653v1) | 2026-03-30 | 组合题完整唯一与每条件必要性构造验收；2 + 1 + 2 = 5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[视频shortcut两段后、online memory前](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26653_20261013.md) |
| [Make Geometry Matter for Spatial Reasoning](https://arxiv.org/abs/2603.26639v1) | 2026-03-30 | 训练visionmask×geometrygate与完整输入部署；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[GeoSense完整两段后](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26639_20261013.md) |
| [Learning to Commit: Generating Organic Pull Requests via Online Repository Memory](https://arxiv.org/abs/2603.26664v1) | 2026-03-30 | 历史盲做→参考diff编译procedural memory；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[temporal repository正文856–862](../../../../books/part-07-agent/77-memory.md)；[依据](../_sources/daily-20260331/SUP_SOURCE_COVERAGE_26664_20261013.md) |
| [AgentCollab: A Self-Evaluation-Driven Collaboration Paradigm for Efficient LLM Agents](https://arxiv.org/abs/2603.26034v1) | 2026-03-30 | selfprogress切换与连续失败有界接管局部配方；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部配方/采用权限不足，不改变长期知识；[依据](../_sources/daily-20260331/SUP_SOURCE_REPORT_26034_20261013.md) |
| [ATime-Consistent Benchmark for Repository-Level Software Engineering Evaluation](https://arxiv.org/abs/2603.26137v1) | 2026-03-30 | temporal snapshot及promptgranularity局部校准；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部配方/采用权限不足，不改变长期知识；[依据](../_sources/daily-20260331/SUP_SOURCE_REPORT_26137_20261013.md) |
| [From Human Cognition to Neural Activations: Probing the Computational Primitives of Spatial Reasoning in LLMs](https://arxiv.org/abs/2603.26323v1) | 2026-03-30 | 空间primitive probe/patch与末答的局部分责；2 + 1 + 2 = 5 | 深入完成 | 仅报告：局部配方/采用权限不足，不改变长期知识；[依据](../_sources/daily-20260331/SUP_SOURCE_REPORT_26323_20261013.md) |
| [AIRA_2: Overcoming Bottlenecks in AI Research Agents](https://arxiv.org/abs/2603.26499v1) | 2026-03-30 | hidden-consistent评价与async/ReAct局部系统配方；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部配方/采用权限不足，不改变长期知识；[依据](../_sources/daily-20260331/SUP_SOURCE_REPORT_26499_20261013.md) |
| [DiffusionAnything: End-to-End In-context Diffusion Learning for Unified Navigation and Pre-Grasp Motion](https://arxiv.org/abs/2603.26322v1) | 2026-03-30 | 候选trajectory depth支持域与预测/观测分责；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[occupancy预测段后、对象pose估计前](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26322_20261013.md) |
| [When Chain-of-Thought Backfires: Evaluating Prompt Sensitivity in Medical Language Models](https://arxiv.org/abs/2603.25960v1) | 2026-03-30 | 同题生成/next-token读出反侧与跨QA采用权限；2 + 1 + 2 = 5 | 深入完成 | 仅报告：局部配方/采用权限不足，不改变长期知识；[依据](../_sources/daily-20260331/SUP_SOURCE_REPORT_25960_20261013.md) |
| [AMALIA Technical Report: A Fully Open Source Large Language Model for European Portuguese](https://arxiv.org/abs/2603.26511v1) | 2026-03-30 | Portugal data/继续训练与native locale评价局部配方；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部配方/采用权限不足，不改变长期知识；[依据](../_sources/daily-20260331/SUP_SOURCE_REPORT_26511_20261013.md) |
| [CADSmith: Multi-Agent CAD Generation with Programmatic Geometric Validation](https://arxiv.org/abs/2603.26512v1) | 2026-03-30 | export/kernel/mesh/render通过与关键连接用途验收；2 + 1 + 2 = 5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[物理几何评价段后、GUI测试前](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；[依据](../_sources/daily-20260331/SUP_SOURCE_PRE_26512_20261013.md) |

## 4. 证据与知识整合

没有确定本窗候选，故证据完成和本轮Books改动均0；不是以访问受阻、已有覆盖或审阅费时缩池。34个潜在线索仅支持具体待核验命题，不支持摘要性能、安全、精确公告或部署保证；不为隔离项写“已有覆盖”或Books采用。

作者已完整读[首8 exact-v1题摘/history](../_sources/daily-20260331/V3_FIRST_ADMISSION.json)、[后8](../_sources/daily-20260331/V3_SECOND_ADMISSION.json)及补段[3已知身份](../_sources/daily-20260331/V3_GAP_KNOWN_PRIMARY.json)、[8有限机制](../_sources/daily-20260331/V3_GAP_FINITE_ABSTRACTS.json)、[2官方web恢复](../_sources/daily-20260331/V3_GAP_TWO_WEB_PRIMARY.json)、[7安全/反证](../_sources/daily-20260331/V3_GAP_SAFETY_COUNTER_ABSTRACTS.json)，合计36份完整AB，不是36必要实验全文。27539定点准入消歧见N2；28405实际§3.1–3.4/§4.1–4.2与直接Table1/3/限制：局部KD surrogate组合后仍要global finetune，3→1失败收窄searchspace；教师400K与学生额外100K、capacity不同不授全部质量归因，NPUprofile不是fullgeneration安全证明。

两弱信号已仅定点实际core后停止：[SCP27094v1](https://arxiv.org/html/2603.27094v1) §III-B–E/IV/VII-E定义返回带许可内容前阻塞audit、日志失败即失败的访问路径，日志追溯不等撤销已消费内容或训练权重，保留潜在protocol边界而不因MCP/成熟组件一刀切；[SkillTester28815v1](https://arxiv.org/html/2603.28815v1) §2.2–2.3/3.1–4.4区分实际invocation、same-task/model no-skill比较、both-success成本及独立security probes，保留评测contract潜在增量，Pass只描述当前suite、不当认证。两项未验证日期/实验，不评分、不写Books，未扩PDF/App/artifact。

具名贡献前关闭（5项，不是全库存负侧）：

- **N1 [27960v1](https://arxiv.org/abs/2603.27960v1)**：完整题摘的四类visual compression/memory-serving/architecture/decoding归纳与agenda未建立改变具体选择的新机制/验证反证；不因survey标签否定价值，不以later“Towards…”覆盖v1真实题名。
- **N2 [27539v1](https://arxiv.org/html/2603.27539v1)**：完整题摘可能sign-reversal反证，故实际核§1L68/Table1L100、§4.3L138–140、§5.4L185–188、§6.2L200–214：无新实证，FinMem23→−22借FINSABER，不能归为受控coordination干预；CBS=Δp/2只是收益覆盖spread，当前empirical不可计算、区域illustrative。以具体重述/未验证命题关闭，不以financial/survey/缺实验单独关闭；日期未精确不影响处置。
- **N3 [Google Raters Blog](https://research.google/blog/building-better-ai-benchmarks-how-many-raters-are-enough/)**：core104–163实际全读，N×K预算与metric-dependent rater/instance实验协议本身有长期价值；官方Paper[AAAI39659](https://ojs.aaai.org/index.php/AAAI/article/view/39659)完整AB与Published2026-03-14已核，原AB已有同N/K和metricdependence、>10/~1000结论，本次Blog无独立新机制/重要revision event。关闭本次重呈现，不声明原论文已全文审阅/无贡献，不另追Blog日期。
- **N4 [Google Quantum disclosure](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/)**：实际core104–133主线是Shor/ECDLP量子线路、cryptocurrency迁移与ZK披露，不是foundation模型/训练/推理/Agent机制；不借Ch72安全类比扩大范围，不采用20倍/量子硬件等结果。
- **N5 [Seed TDDFT29257](https://arxiv.org/abs/2603.29257)**：明确分子电子激发态/量子化学；wrapper首条完整AB实际可见，GPU4PySCF、A100实现不改变其AIforScience领域计算身份，按ROADMAP暂缓，既不借runtime节点纳入也不穷查firstpublic。

### 03-30 自然日补充：最终45个唯一家族

上方连续原§4为补查前旧小时窗证据，原样冻结；其中“0”和旧完成语句不适用于本轮。以下新增依据不改写旧判断。

### [Do All Vision Transformers Need Registers? A Cross-Architectural Reassessment](https://arxiv.org/abs/2603.25803v1)

采用精确v1。跨架构分开norm、attention与实际读出；必要命题已采用并通过实际非writer POST，归属[MULTIMODAL-REPRESENTATION](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PRE_25803_20261012.md)；本记录不声称全部附件、代码或复现完成。

### [Second-Order, First-Class: A Composable Stack for Curvature-Aware Training](https://arxiv.org/abs/2603.25976v1)

采用精确v1。snapshot→实际update→控制信号复用分责；必要命题已采用并通过实际非writer POST，归属[TRAIN-PRETRAINING](../../../../books/part-04-training-system/28-pretraining.md)。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PRE_25976_20261012.md)；本记录不声称全部附件、代码或复现完成。

### [Switch Attention: Towards Dynamic and Fine-grained Hybrid Transformers](https://arxiv.org/abs/2603.26380v1)

采用精确v1。token-layer动态路由与budget/proxy资格；必要命题已采用并通过实际非writer POST，归属[MODEL-LONG-CONTEXT](../../../../books/part-02-model/22-long-context.md)。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26380_20261012.md)；本记录不声称全部附件、代码或复现完成。

### [Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal Large Language Model Inference](https://arxiv.org/abs/2603.26498v1)

采用精确v1。latency×KV分类、per-model profile与aging/SLO边界refine；必要命题已采用并通过实际非writer POST，归属[INFER-SCHEDULING](../../../../books/part-05-inference-system/56-inference-scheduling.md)。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26498_20261012.md)；本记录不声称全部附件、代码或复现完成。

### [Dynamic Tokenization via Reinforcement Patching: End-to-end Training and Zero-shot Transfer](https://arxiv.org/abs/2603.26097v1)

采用精确v1。离散切分策略与硬token预算接口；必要命题已采用并通过实际非writer POST，归属[MULTIMODAL-REPRESENTATION](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26097_20261013.md)；本记录不声称全部附件、代码或复现完成。

### [GUIDE: Resolving Domain Bias in GUI Agents through Real-Time Web Video Retrieval and Plug-and-Play Annotation](https://arxiv.org/abs/2603.26266v1)

采用精确v1。实时教程检索提供reference而非directive；必要命题已采用并通过实际非writer POST，归属[AGENT-PLANNING](../../../../books/part-07-agent/79-planning.md)。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26266_20261013.md)；本记录不声称全部附件、代码或复现完成。

### [The Limits of Learning from Pictures and Text: Vision-Language Models and Embodied Scene Understanding](https://arxiv.org/abs/2603.26589v1)

采用精确v1。人类条件描述分布与解释干预分责；必要命题已采用并通过实际非writer POST，归属[PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26589_20261013.md)；本记录不声称全部附件、代码或复现完成。

### [Finding Distributed Object-Centric Properties in Self-Supervised Transformers](https://arxiv.org/abs/2603.26127v1)

采用精确v1。同型Q/K/V相似与跨层/head对象读出；必要命题已采用并通过实际非writer POST，归属[MULTIMODAL-REPRESENTATION](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26127_20261013.md)；本记录不声称全部附件、代码或复现完成。

### [DiReCT: Disentangled Regularization of Contrastive Trajectories for Physics-Refined Video Generation](https://arxiv.org/abs/2603.25931v1)

采用精确v1。negative条件、输出方向与参数梯度分责；必要命题已采用并通过实际非writer POST，归属[MULTIMODAL-GENERATIVE-PARADIGMS](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PRE_25931_20261013.md)；本记录不声称全部附件、代码或复现完成。

### [Neighbor-Aware Localized Concept Erasure in Text-to-Image Diffusion Models](https://arxiv.org/abs/2603.25994v1)

采用精确v1。局部概念删除与neighborhood保留验收；必要命题已采用并通过实际非writer POST，归属[PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PRE_25994_20261013.md)；本记录不声称全部附件、代码或复现完成。

### [Wattchmen: Watching the Wattchers -- High Fidelity, Flexible GPU Energy Modeling](https://arxiv.org/abs/2603.26435v1)

采用精确v1。指令归因与总device/整机measurement分责；必要命题已采用并通过实际非writer POST，归属[PLATFORM-COST](../../../../books/part-06-ai-infrastructure/70-cost.md)。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26435_20261013.md)；本记录不声称全部附件、代码或复现完成。

### [A Lightweight High-Throughput Collective-Capable NoC for Large-Scale ML Accelerators](https://arxiv.org/abs/2603.26438v1)

采用精确v1。片上router借FPU与mask/争用资格；必要命题已采用并通过实际非writer POST，归属[TRAIN-DISTRIBUTED-TRAINING](../../../../books/part-04-training-system/36-distributed-training.md)。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26438_20261013.md)；本记录不声称全部附件、代码或复现完成。

### [On the Expressive Power of Contextual Relations in Transformers](https://arxiv.org/abs/2603.25860v1)

采用精确v1。coupling表示定理的support/supnorm桥资格争议；暂缓：必要选择桥反例隔离，不判主定理必假。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_DISPUTE_25860_20261012.md)；本记录不声称全部附件、代码或复现完成。

### [H-Node Attack and Defense in Large Language Models](https://arxiv.org/abs/2603.26045v1)

采用精确v1。内部probe可被操纵而不改善外部行为；仅报告：已有具体行为/内部sensor分责，不新增防御保证。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_REPORT_26045_20261012.md)；本记录不声称全部附件、代码或复现完成。

### [Gaussian Shannon: High-Precision Diffusion Model Watermarking Based on Communication](https://arxiv.org/abs/2603.26167v1)

采用精确v1。完整payload恢复与检测工作点分账；仅报告：成熟LDPC/repeat局部恢复配方不新增来源认证条件。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_REPORT_26167_20261013.md)；本记录不声称全部附件、代码或复现完成。

### [Maintaining Difficulty: A Margin Scheduler for Triplet Loss in Siamese Networks Training](https://arxiv.org/abs/2603.26389v1)

采用精确v1。局部adaptive margin阈值步增配方；仅报告：局部单组件优化，不升重要通用机制。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_ADMISSION_CORE_26389v1_20261012.txt)；本记录不声称全部附件、代码或复现完成。

### [FairLLaVA: Fairness-Aware Parameter-Efficient Fine-Tuning for Large Vision-Language Assistants](https://arxiv.org/abs/2603.26008v1)

采用精确v1。CLUB surrogate与LoRA/projector交替冻结更新；仅报告：成熟MI+PEFT在人口上的局部组合，无新一般有效性边界。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26008_20261013.md)；本记录不声称全部附件、代码或复现完成。

### [Policy-Guided World Model Planning for Language-Conditioned Visual Navigation](https://arxiv.org/abs/2603.25981v1)

采用精确v1。policy prior暖启与latent terminalcost MPPI局部配方；仅报告：收益不新建一般初始化/规划边界。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_ADMISSION_25981v1_20261013.txt)；本记录不声称全部附件、代码或复现完成。

### [ViGoR-Bench: How Far Are Visual Generative Models From Zero-Shot Visual Reasoners?](https://arxiv.org/abs/2603.25823v1)

采用精确v1。visual reasoning局部hypothesis与常规GT评价；仅报告：规模曲线未识别新受控因果或适用条件。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_ADMISSION_25823v1_20261013.txt)；本记录不声称全部附件、代码或复现完成。

### [DFM-VLA: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching](https://arxiv.org/abs/2603.26320v1)

采用精确v1。离散action CTMC局部参数化与末greedy；仅报告：借用成熟DFM与新action应用，不认证动作距离/收敛。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PREP_26320_20261013.md)；本记录不声称全部附件、代码或复现完成。

### [MemCam: Memory-Augmented Camera Control for Consistent Video Generation](https://arxiv.org/abs/2603.26193v1)

采用精确v1。逐target视野覆盖与条件空间压缩；已通过实际非writer POST，归属[MULTIMODAL-WORLD-MODELS](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26193_20261013.md)；本记录不声称全部附件、代码或复现完成。

### [Towards GUI Agents: Vision-Language Diffusion Models for GUI Grounding](https://arxiv.org/abs/2603.26211v1)

采用精确v1。anchor可见/extent全mask的结构条件与预算；已通过实际非writer POST，归属[MULTIMODAL-GENERATIVE-PARADIGMS](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。关键方法、直接反侧、对照条件与不采用的保证见[本family必要证据及实际处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26211_20261013.md)；本记录不声称全部附件、代码或复现完成。

### [IP-Bench: Benchmark for Image Protection Methods in Image-to-Video Generation Scenarios](https://arxiv.org/abs/2603.26154v1)

JPEG后像素扰动几乎存留而消费端效果近消失，FVD与frame质量排名相反；预算、作者重实现及300图/openconsumer限制方法归因，未授真实滥用/通用防护。 整合：`PLATFORM-SECURITY`，[输入保护两段后](../../../../books/part-06-ai-infrastructure/72-security.md)，实际POST已通过。 具体证据与采用边界见[必要审阅](../_sources/daily-20260331/SUP_SOURCE_PRE_26154_20261013.md)。

### [MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization](https://arxiv.org/abs/2603.25973v1)

v1§4.4–4.5多源ranking改善并不覆盖绝对rating误差，来源内容与长度共同变化；活跃review人口、离线proxy、单run及query cutoff未披露限制真实偏好/满意结论。 整合：`AGENT-MEMORY`，[content/length段后](../../../../books/part-07-agent/77-memory.md)，实际POST已通过。 具体证据与采用边界见[必要审阅](../_sources/daily-20260331/SUP_SOURCE_PRE_25973_20261013.md)。

### [Mitigating the Reasoning Tax in Vision-Language Fine-Tuning with Input-Adaptive Depth Aggregation](https://arxiv.org/abs/2603.26330v1)

v1§3–4/T1–4采用 pooled query 检索前block boundary states再gated加回，backbone共享attention保留。模态split并非主增益且感知反退，容量/lr混杂及sigmoid近零非identity限制归因/稳定结论。 整合：`MODEL-TRANSFORMER-LAYER`，[ExoFormer两段后、Norm前](../../../../books/part-02-model/17-transformer-layer.md)，实际POST已通过。 具体证据与采用边界见[必要审阅](../_sources/daily-20260331/SUP_SOURCE_PRE_26330_20261013.md)。

### [MPDiT: Multi-Patch Global-to-Local Transformer Architecture For Efficient Flow Matching and Diffusion Model](https://arxiv.org/abs/2603.26357v1)

v1§3–4/T3–6单forward深度预算与新embeddings分开；fineinput跳过不是质量证书，conditioning混杂/FID退步与GFLOPs非wallclock保留，不授任意大T2I/T2V无损。 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[并行与少步生成标题后](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，实际POST已通过。 具体证据与采用边界见[必要审阅](../_sources/daily-20260331/SUP_SOURCE_PRE_26357_20261013.md)。

### [Realtime-VLA V2: Learning to Run VLAs Fast, Smooth, and Accurate](https://arxiv.org/abs/2603.26360v1)

v1§4.1–4.2/5.1–5.2保留局部实机结果，但成熟retime/MPC/HITL未建立新可推广控制权限。nearfailed标签被丢弃的survivor人口、加速度量纲与软硬约束措辞冲突限制安全/最优性，1+1+2=4关闭。 仅报告，不新增Books。 具体证据与采用边界见[必要审阅](../_sources/daily-20260331/SUP_SOURCE_26360v1_20261013.txt)。

### [VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation](https://arxiv.org/abs/2603.26666v1)

v1§3.2–3.4/Eq5–7/4.1及必要评价显示teacher在student状态读出、停止梯度logratio的局部OPD配方。Reverse-KL/tokenreward未认证有界、entropy非epistemic，局部heldout不证明免遗忘或总费用优势，1+1+2=4关闭。 仅报告，不新增Books。 具体证据与采用边界见[必要审阅](../_sources/daily-20260331/SUP_SOURCE_26666v1_20261013.txt)。

### [Vision2Web: A Hierarchical Benchmark for Visual Website Development with Agent Verification](https://arxiv.org/abs/2603.26648v1)

v1§3.1–3.2/Alg1/4.4的DAG共享state、功能/视觉分账是成熟测试设计，guided〈O,A,V〉为prompt而非硬动作限制。250节点12.8%误判及100prototype相关.66保留局部反侧，未建立新可靠性边界，1+1+2=4关闭。 仅报告，不新增Books。 具体证据与采用边界见[必要审阅](../_sources/daily-20260331/SUP_ADMISSION_26648v1_20261013.txt)。

### [Reflect to Inform: Boosting Multimodal Reasoning via Information-Gain-Driven Verification](https://arxiv.org/abs/2603.26348v1)

v1§3/Alg1、T1–3、A配置与B3/Eq7保留局部SFT-RL-SFT效果；trace仍由外部两judge过滤，累加阶段预算未控。单target NLL不等image条件互信息，attention/低KL非真实grounding因果；中心权限隔离不抹去局部结果，也不作整篇无效。 仅报告，不新增Books。 具体证据与采用边界见[必要审阅](../_sources/daily-20260331/SUP_SOURCE_REPORT_26348_20261013.md)。

### [Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents](https://arxiv.org/abs/2603.26233v1)

detector每轮提missing-information flag、执行路径先ask再消费回答；保oracle/同模型与预算混杂，事后已问子群非uncertainty校准。Ch79重复已撤回，canonical Ch81最小refine经实际POST通过。 整合：`AGENT-WORKFLOW`，[clarification gate原段最小refine](../../../../books/part-07-agent/81-workflow.md)；[必要证据及采用范围](../_sources/daily-20260331/SUP_ASK_OWNER_MERGE_PRE_20261013.md)。

### [VGGRPO: Towards World-Consistent Video Generation with 4D Latent Reward](https://arxiv.org/abs/2603.26599v1)

v1§3.2–3.3/4.1/4.3/T2与B1–B2只支持配对latent/RGB校准的评价旁路。reward-only省decode不认证完整训练倍率，dynamic-degree反退、自一致proxy与clean/noisy支持区别保留；实际POST通过。 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[metric-geometry后、Plan前](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；[必要证据及采用范围](../_sources/daily-20260331/SUP_SOURCE_PRE_26599_20261013.md)。

### [InstaVSR: Taming Diffusion for Efficient and Temporally Consistent Video Super-Resolution](https://arxiv.org/abs/2603.26134v1)

v1§3.1–3.3/4.1/T3/4.4只采用input重排与自产SR条件，输入保值不等outputlossless。mixed buffer/discriminator口径未统一、时序只定性及指标反侧保留，不授通用速度/长期无闪烁。 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Training/Inference mismatch，SF05966两段后](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。[必要证据与处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26134_20261013.md)。

### [Why Models Know But Don't Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models](https://arxiv.org/abs/2603.26410v1)

v1§3/4.5–4.6/5.5–5.6同keyword在thinking/answer两流得到四组合，局部披露差额不等真实知道或intent。只hint-followed人口，长度、释义、cap及模型分母限制风险外推。 整合：`PLATFORM-EVALUATION-SYSTEM`，[CoT instrument两段后](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。[必要证据与处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26410_20261013.md)。

### [PerceptionComp: A Video Benchmark for Complex Perception-Centric Reasoning](https://arxiv.org/abs/2603.26653v1)

v1§3.3/3.6人工复核conjunctive题无proper subset唯一与sequential referent，区分题目长和条件实际必要。未披露全子集程序枚举，不授全部捷径消除；保实际可见帧、annotation与调用费用。 整合：`PLATFORM-EVALUATION-SYSTEM`，[视频shortcut两段后、online memory前](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。[必要证据与处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26653_20261013.md)。

### [Make Geometry Matter for Spatial Reasoning](https://arxiv.org/abs/2603.26639v1)

v1§3/4.3–4.4结合遮挡与学习gate消费几何；naivegeometry可弱于nogeometry、β过高退步。attention/gate不是几何真值或forced因果，网格对齐、训练/部署人口及全部费用保留。 整合：`MULTIMODAL-REPRESENTATION`，[GeoSense完整两段后](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。[必要证据与处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26639_20261013.md)。

### [Learning to Commit: Generating Organic Pull Requests via Online Repository Memory](https://arxiv.org/abs/2603.26664v1)

v1§3.1–3.5/4/T2–4的chronological snapshot、盲做issue→oracle diff编译memory核心链已由现temporalrepository完整承载。24history/7future单repo的file/logic收益不等functional correct，scope/style局部反退；不新增正文/末注。 已有覆盖：`AGENT-MEMORY`，[temporal repository正文856–862](../../../../books/part-07-agent/77-memory.md)。[必要证据与处置](../_sources/daily-20260331/SUP_SOURCE_COVERAGE_26664_20261013.md)。

### [AgentCollab: A Self-Evaluation-Driven Collaboration Paradigm for Efficient LLM Agents](https://arxiv.org/abs/2603.26034v1)

v1§2–3/T1–2只有成熟budget/routing局部组合，selfprogress非真值、低switching非cache因果，body/staticAlg return不同。保质量仍低强模型的实验，不授新一般control资格。 仅报告，Books0。[必要证据与处置](../_sources/daily-20260331/SUP_SOURCE_REPORT_26034_20261013.md)。

### [ATime-Consistent Benchmark for Repository-Level Software Engineering Evaluation](https://arxiv.org/abs/2603.26137v1)

v1§3–7 matched augmentation A/B仅提案，实测仅baseline file-localization。prompt详细度改变局部失败人口，不认证knowledgeaugmentation因果或patch正确，exacttemplates/leakagefilters及CI不足。 仅报告，Books0。[必要证据与处置](../_sources/daily-20260331/SUP_SOURCE_REPORT_26137_20261013.md)。

### [From Human Cognition to Neural Activations: Probing the Computational Primitives of Spatial Reasoning in LLMs](https://arxiv.org/abs/2603.26323v1)

v1§4/T2–3/A7保counterfactual activation patch局部输出变化，但finalprobe下降不证明信息丢失。单choice/partialcredit、Table3/body与Algorithm1multi-hop资格冲突隔离，不授纯空间/人类认知或跨语统一路径。 仅报告，Books0。[必要证据与处置](../_sources/daily-20260331/SUP_SOURCE_REPORT_26323_20261013.md)。

### [AIRA_2: Overcoming Bottlenecks in AI Research Agents](https://arxiv.org/abs/2603.26499v1)

v1§3.3/4.3.2–3固定/隐藏/外置/holdout整体改变；late下降消失不能唯一归noise，test曲线不排memorization。ReAct/static差距随时间缩小；保局部实验，不把成熟组合升级为新一般机制。 仅报告，Books0。[必要证据与处置](../_sources/daily-20260331/SUP_SOURCE_REPORT_26499_20261013.md)。

### [DiffusionAnything: End-to-End In-context Diffusion Learning for Unified Navigation and Pre-Grasp Motion](https://arxiv.org/abs/2603.26322v1)

v1III-A4/Eq10与IV-A/G–H只沿waypoint预测depth，区别于densegeometry/occupancy预算。teacher/GT描述未统一，未覆盖侧面/扫掠体；不能据预测或有限无碰撞试验认证collision check/10Hz控制。 整合：`MULTIMODAL-EMBODIED-VLA`，[occupancy预测段后、对象pose估计前](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；actual非writer POST已通过。[必要证据与处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26322_20261013.md)。

### [When Chain-of-Thought Backfires: Evaluating Prompt Sensitivity in Medical Language Models](https://arxiv.org/abs/2603.25960v1)

v1§3–5/T8/0F–G保4B同MedMCQA4183 direct/cloze局部差额；27B cloze来自MedMCQA1000而38.2生成来自PubMedQA，不证同题规模/知识恢复。first-valid regex/cap和不同样本限制pureoverthinking/latentknow解释。 仅报告，Books0。[必要证据与处置](../_sources/daily-20260331/SUP_SOURCE_REPORT_25960_20261013.md)。

### [AMALIA Technical Report: A Fully Open Source Large Language Model for European Portuguese](https://arxiv.org/abs/2603.26511v1)

v1§3–6成熟继续训练/SFT/DPO和native四任务不新建一般主线机制。translated与native不是配对同任务，固定A的70题与Gemini多turn locale评分分别保instrument/人口限制，不因低资源语言标签关闭。 仅报告，Books0。[必要证据与处置](../_sources/daily-20260331/SUP_SOURCE_REPORT_26511_20261013.md)。

### [CADSmith: Multi-Agent CAD Generation with Programmatic Geometric Validation](https://arxiv.org/abs/2603.26512v1)

v1III-D–H/IV-D/V的T3_019高F1/IoU与kernel/三固定view Judge同过却仍有未连接near-miss。中心/ICP对齐和voxel身份限制原坐标/用途，执行成功不等100%几何或可制造，具体检查分责进入正文。 整合：`PLATFORM-EVALUATION-SYSTEM`，[物理几何评价段后、GUI测试前](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；actual非writer POST已通过。[必要证据与处置](../_sources/daily-20260331/SUP_SOURCE_PRE_26512_20261013.md)。

## 5. 缺口与下一步

普通扫描、初筛、必要Source、Books写入和实际POST待办0；最终六部分非报告作者root实际DAY通过。没有未读材料被转作外部HOLD，以下仅是已隔离的终态保留项。

补窗终态保留项（不用于正面证据、Books或无遗漏断言）：Qwen同event官方extra.date03-30与body01-07冲突，有限同family发布日期恢复未闭03-30；26845/26846/28651必要公开范围跨30–31，旧scheduled_match不足公告（[四v1题摘/日字段](../_sources/daily-20260331/SUP_AB_MIDDLE5_20261013.json)、[实际client字段](../_sources/daily-20260331/SUP_DATACITE_MIDDLE5_20261013.json)、[28651原日层](../_sources/daily-20260331/SUP_AB_DATE_20261012.json)）；Google/Meta/MiMo历史slice与Seed未返身份/统计口径没有支撑无遗漏。定点重开条件：取得同一机制的可信首次公开日或对应v1官方公开批次使范围封闭到补窗；历史slice须恢复目标窗dated原身份/必要差额说明，含相关机制才审其core，不扩机构全历史。

D1–D34为原小时窗日期请求，保持原身份、原字段与原窗口口径，不移日、不作为本轮普通0或验收声明。H1–H4采用本轮可核的有限来源范围，收尾更新如下，不将旧目录数字当当前结果。

D1–D34共同缺口：该exact-v1首次公开的官方批次/作者原发时间仍不能把范围封闭到31日09:00前。实际[availability](https://info.arxiv.org/help/availability.html) L170–199（ID/DOI不可advance）与[arXiv DOI](https://info.arxiv.org/help/doi.html)、[DataCite registered定义](https://support.datacite.org/docs/what-is-the-difference-between-the-created-and-registered-date-in-the-datacite-rest-api)/[states](https://support.datacite.org/docs/doi-states)支持复合边界：所有v1 Submitted介于Fri27T14EDT与Mon30T14EDT，**最早可能Mon30T20EDT=31日08:00BJT**。32项owned client arxiv.content、state findable的registered原UTC秒+1秒给含端点上界，均跨31T09右端（D32实际Apr1上界），不是registered等于实际公告；D26/D27该字段一次API SSL EOF与web InternalError未恢复，只可保留日期缺口，不能伪造上界或firstpublic。不以Created/Updated/Available月份、scheduledslot、索引日期或月membership补造时刻。初将Sunday误算最早30BJT08已在首批校准前纠正。复合范围不证明更早作者页首次公开；合法月表/联合精确检索未恢复官方exact批次，不继续日期代码考古。

重开条件（各身份只一次请求）：取得对应v1官方公告/公开批次原字段或作者原版本首次公开与时区，使整个公开范围落本窗；若实际窗外则恢复真实归属日，不扩本日。届时只审表中命题所需核心方法/对照/反证，尚未读完不冒充外部终态。下表Submitted/registered是原UTC字段，不是first-public。

| 保留身份 | Submitted v1 UTC；registered UTC | 潜在增量与采用边界 |
| --- | --- | --- |
| D1 [SCIN28239v1](https://arxiv.org/abs/2603.28239v1) | 03/30 09:59:11；03/31 03:39:41 | GPU触发NVLS仍需return→ISA触发memory-semantics+broadcast/INQ；只潜在控制路径，不采FPGA倍数/实机普适保证 |
| D2 [CirrusBench28569v1](https://arxiv.org/abs/2603.28569v1) | 03/30 15:26:00；03/31 03:47:27 | 真实cloudtickets依赖/multi-turn与correctness不能覆盖resolution efficiency；不是仅因新benchmark准入 |
| D3 [StreamingVLA28565v1](https://arxiv.org/abs/2603.28565v1) | 03/30 15:23:27；03/31 03:47:22 | 串行observe/generate/execute→生成执行重叠+saliency早观察；未核成功率/延迟归因 |
| D4 [LLaVADyMoE27481v1](https://arxiv.org/abs/2603.27481v1) | 03/29 02:30:55；03/31 03:21:51 | 冻结旧expert仍可能routing drift→token分类/regularization约束；不授遗忘普遍消除 |
| D5 [OpenClaw27517v1](https://arxiv.org/abs/2603.27517v1) | 03/29 04:51:27；03/31 03:22:40 | advisory composition/lexical allowlist bypass与skills dropper可能修正exec-only保护；采用v1真实taxonomy题名，不把May改名/修订回填 |
| D6 [HiddenAds27522v1](https://arxiv.org/abs/2603.27522v1) | 03/29 05:14:04；03/31 03:22:47 | 自然推荐行为trigger可与correct/helpful回答和未授权广告共存；不采用近零FP/迁移/防御无效保证 |
| D7 [ITQ3_S27914v1](https://arxiv.org/abs/2603.27914v1) | 03/30 00:03:22；03/31 03:31:59 | rotation量化与shared-memory inverse FWHT fused路径；必须区分rotation roundtrip与有损量化，严格优于任意3bit/1.5倍仅作者主张 |
| D8 [HISA28458v1](https://arxiv.org/abs/2603.28458v1) | 03/30 13:59:51；03/31 03:44:50 | sparse kernel节省≠indexer线性扫前缀→block filter/token refinement；top-k形状不等相同集合，不授99%IoU等价保证 |
| D9 [R_dm28460v1](https://arxiv.org/abs/2603.28460v1) | 03/30 14:01:31；03/31 03:44:53 | 独立DMD+RL loss→distribution-matching reward/group-normalization及IS；需核重加权目标/稳定性，未授高质实时 |
| D10 [EdgeDiT28405v1](https://arxiv.org/abs/2603.28405v1) | 03/30 13:14:30；03/31 03:43:33 | 局部surrogateKD组合后global FT与3→1失败界定搜索粒度；只定点准入消歧，不以NAS组合或性能数准入，不把额外训练收益纯归architecture |
| D11 [D2Skill28716v1](https://arxiv.org/abs/2603.28716v1) | 03/30 17:32:11；03/31 03:50:52 | task/step bank维护由same-policy baseline/skill-injected paired rollout差额信号；需核配对/资源代价，不采普遍transfer或modest overhead |
| D12 [EmergentRisks27771v1](https://arxiv.org/abs/2603.27771v1) | 03/29 17:10:28；03/31 03:28:40 | shared-resource竞争/handoff/aggregation可能使agent-level safeguards不足；不能从作者“frequent”推出真实生产风险率或所有guard失败 |
| D13 [ResAdapt28610v1](https://arxiv.org/abs/2603.28610v1) | 03/30 15:57:32；03/31 03:48:25 | post-encoding压缩不省encoder像素→input-side contextual-bandit分配保native接口；未核质量/训练/成本同预算，不采用16倍数字 |
| D14 [HyperP28743v1](https://arxiv.org/abs/2603.28743v1) | 03/30 17:51:47；03/31 03:51:29 | Frobenius-sphere/Muon下weight-decay一阶no-op与DepthμP/gate粒度条件；须核假设/transfer控制，不把有限指标bounded升普遍训练稳定 |
| D15 [Aging27439v1](https://arxiv.org/abs/2603.27439v1) | 03/28 23:03:27；03/31 03:20:53 | 交换律输入置换可保持当前加法正确却改变非对称老化压力；不授64%/寿命数字或任意硬件保证 |
| D16 [FARE27141v1](https://arxiv.org/abs/2603.27141v1) | 03/28 05:33:42；03/31 03:13:51 | routing/log-likelihood公平变化不必转移到decoded generation；masking知识/偏差纠缠，不授无代价公平 |
| D17 [SafetyDrift27148v1](https://arxiv.org/abs/2603.27148v1) | 03/28 05:52:04；03/31 03:14:01 | individual安全steps不能替代序列风险状态；absorbing monotone有限模型条件不推出所有生产agents必违规 |
| D18 [CodebaseMemory27277v1](https://arxiv.org/abs/2603.27277v1) | 03/28 14:18:12；03/31 03:17:04 | persistent结构查询与file-exploration在quality/token-cost及graph-native任务的边界；不是MCP/66语言组件数量准入，未核控制 |
| D19 [SCP27094v1](https://arxiv.org/abs/2603.27094v1) | 03/28 02:28:41；03/31 03:12:46 | blocking audit失败不返回content/license envelope；post-access仅合同/追溯，不能凭hash授防共享/撤销训练权重 |
| D20 [PreconditionedAttention27153v1](https://arxiv.org/abs/2603.27153v1) | 03/28 06:30:45；03/31 03:14:09 | head conditioning对ill-conditioned attention优化的条件和drop-in成本；理论假设/效率未审，不授稳定普适性 |
| D21 [CurriculumLimits27226v1](https://arxiv.org/abs/2603.27226v1) | 03/28 10:43:36；03/31 03:15:53 | 按实际任务复杂度、多schedule/模型/SFT-RL检验排序相对random边界；局部反证不推所有curriculum无效 |
| D22 [EFlow27086v1](https://arxiv.org/abs/2603.27086v1) | 03/28 02:06:55；03/31 03:12:33 | t→s solution-flow与token-droppable attention、path-drop指导target关系；未采倍数或任意drop等价 |
| D23 [CARE27240v1](https://arxiv.org/abs/2603.27240v1) | 03/28 11:31:16；03/31 03:16:12 | causal-mediation选择及visual/text eigensubspace的adaptive projection边界；不授跨全部未知攻击保证 |
| D24 [LatentBiopsy27412v1](https://arxiv.org/abs/2603.27412v1) | 03/28 21:19:58；03/31 03:20:17 | refusal移除后geometry与不同family相反方向要求direction-agnostic anomaly；不把几何sensor当恶意真值 |
| D25 [ET3 26984v1](https://arxiv.org/abs/2603.26984v1) | 03/27 20:53:04；03/31 03:10:07 | energy-guided输入变换的分类证明条件与LVLM任务转移边界；不授LVLM通用安全，v2窗后不回填 |
| D26 [UniWorldVLA27287v1](https://arxiv.org/abs/2603.27287v1) | 03/28 14:39:51；未恢复 | imagined frame/action interleave可针对rollout drift；imagination闭环不等真实sensor/安全闭环，registered失败不伪造日期 |
| D27 [StructuralGraph27070v1](https://arxiv.org/abs/2603.27070v1) | 03/28 01:14:40；未恢复 | co-activation graph与targeted perturbation输出变化的接口；correlation/局部intervention不等完整causal circuit |
| D28 [GRACE27139v1](https://arxiv.org/abs/2603.27139v1) | 03/28 05:22:00；03/31 03:13:48 | CLIP ID/OOD/adversarial三轴取舍和curvature扰动/feature-alignment条件；不授通用foundation robustness |
| D29 [ReliabilityLimits26993v1](https://arxiv.org/abs/2603.26993v1) | 03/27 21:07:42；03/31 03:10:20 | 固定exogenous information/有限无环delegation的central Bayes比较；不等真实有限LLM总优于multiagent |
| D30 [VerificationHurts27076v1](https://arxiv.org/abs/2603.27076v1) | 03/28 01:35:59；03/31 03:12:18 | 不同upstream质量下verification反效应；不把proof-state局部差额变生产阈值或取消全部verification |
| D31 [SemanticMemory27116v1](https://arxiv.org/abs/2603.27116v1) | 03/28 04:01:59；03/31 03:13:17 | continuous kernel/threshold与有限intrinsic dimension中竞争质量增加的retention边界；不推全部memory系统必忘 |
| D32 [SkillTester28815v1](https://arxiv.org/abs/2603.28815v1) | 03/28 14:56:18；04/01 01:56:17 | invocation-gated matched baseline utility/成本与独立security probes分账；标签只当前suite非认证，Apr1 upper不是实际公告 |
| D33 [CumulativeState27343v1](https://arxiv.org/abs/2603.27343v1) | 03/28 17:25:11；03/31 03:18:41 | K/非算术/yoked控制区分completion与累计state构念；predictive correlation不授agent能力因果，普通Bonferroni-corrected非erratum |
| D34 [KAWHI27375v1](https://arxiv.org/abs/2603.27375v1) | 03/28 18:40:14；03/31 03:19:26 | visual salient聚合/关键head到paragraph reward-credit分配；attention proxy不等groundtruth或通用因果归因 |

4组来源限制分别定点重开，不把所有loadmore未知材料当永久请求：

| 保留项 | 缺什么、不能采用的原因 | 可接受替代与重开位置 |
| --- | --- | --- |
| H1 [Google pubs](https://research.google/pubs/) | 当前1–15/11569与2026filter372没有本窗publication历史定位；Blog2/2/DeepMindpage3已可核，不受此限制改写 | 本窗dated publication导出/原event，仅重开相关publication；不全扫11569 |
| H2 [Meta Research/publications](https://ai.meta.com/research/) | Research0行、当前/results444只Sep/Aug；Blog22有限卡不能证明全部publications历史 | 本窗可读官方research/publication slice或dated原event；不把零响应/搜索0当无命中 |
| H3 [MiMo Blog](https://mimo.xiaomi.com/) | 当前15Blog卡无date，不能裁定哪些在本窗；Pro/Omni正确原页March18已恢复且明确在本窗前 | 本窗datedBlog slice或具名原event与时区；不再请求相同Pro/Omni正文、不开全15body |
| H4 [Seed目录API](https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2026&page_token=0&count=100&order_desc=false) | 当前Blog0实际9/total23/next20、Blog20实际3/total23/next空；Paper20实际14/82/next40、Paper40实际2/82/next60，四投影并非全目录。未返回身份与total/paging语义尚不能证明目标窗无遗漏；旧14/19或缺5不是本轮数量 | 目标03-30窗dated原身份/差额说明；含主线机制才定点读core，不由统计差额生成11或82篇新队列，不再扩新分页 |

## 6. 复核

复核者：root（非报告作者）

结论：通过

root于2026-10-13T04:26:10+08:00实际顺读本轮全部六部分、45候选与对应证据小节、14来源有限停止及§5完整隔离范围，DAY通过并在[原唯一停点顶部](../_sources/daily-20260331/SUP_WORKING_STOP_20261012.md)持久。root已逐批独立校准全部45拟入选家族、14具名排除项及有关安全/反证必要core；所有45候选达到各自审阅与Books判断要求，不代表无差别全文/附件验证。26项必要原证、唯一owner、逐字PRE、真实正文完整邻接及自身静态注actual非writerPOST均已通过；RPS合并既有family只计一次refine，Ask发现Ch79重复后撤回并转Ch81 canonical gate、重新实际POST，只计一次。Commit以Ch77具体temporalrepository论点已有覆盖，非靠引用相似标题。5分仅报告保局部有效证据并限定中心代理权限，1中心证明资格争议不判主定理必假。

来源范围已限定到四主线窄query/受影响尾片/中段5 title、相关cs.DC标题切片及14机构有限投影；不把151槽、46 title或63 AB当候选分母或全学科negative。必要日期/当前官方撤回纠错轻核与直接反侧逐项复核，不扩无关版本/附件。原窗口/旧0候选/连续原§4已由root独立字节前缀比较baseline通过；旧日期34请求、必要首公开4项与4个机构slice保持隔离，不支撑正面覆盖、性能或安全保证。

实际DAY发现§3表内空行会打断GFM呈现，已仅删除空行并回核为连续45行单表，字段不变；此问题未被格式脚本捕获。补查前root旧六部分验收只作历史证据，不能替代本轮DAY。最终45行同步后实际V3格式检查通过（1份），83个去重本地引用全部存在，官方投影JSON可解析，45唯一家族与26整合/17仅报告/1具体覆盖/1暂缓一致；原窗口和2446字符连续原§4实际比对保持。限定本日报告/source的git diff --check通过，已有目标Books/两日报/LS的限定cached检查由root实际通过，不宣全cached clean。机器结果仅支持各自检查范围；本次DAY依据root真实独核，不由作者或机器自授，完成态FINAL仍须root实际读回后接纳。未stage、commit、push，不改LS/索引、其他日或月份。
