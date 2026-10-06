# Daily Research — 2026-04-29

**规范：** V3
**窗口：** 2026-04-28T09:00:00+08:00 ～ 2026-04-29T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-30T19:57:26+08:00

## 1. 结论

本日重要增量集中于执行计划的真实状态边界、评价证据与授权的分权，以及训练反馈的共源风险。FlashQLA的部分融合/CP、空模态rank的SP dummy形状、CacheFlow恢复依赖图均不能由算子加速外推服务SLO；SUDP用密不交密仍依赖完整操作绑定、可信呈现与custodian；ProDa、Libra-VLA与Semi-DPO分别补共享规格污染、串行粗细动作和分时偏好标签的边界。

有界来源与题摘工作不继承旧V2.1的446/385或全通过声明。宽代理并集1286仅供查漏；实际106个唯一论文完整题摘为65潜在、38具名前闭、3已证早公开。65潜在中6项历史首公开仍不明，隔离后为59篇论文，加4机构事件，共63家族。最终32整合、9已有覆盖、11仅报告、11中央争议暂缓；32处实际正文与前后衔接全部获独立写后通过，所有候选的证据与Books处置已非作者有限终核。25724因真实cold-readiness差额从Only恢复，ViPO采用正确Ch34命题。普通待核/待写/待写后均为0，独立日级验收通过；外部/日期与争议保留项不作正面证据或全网覆盖保证。

## 2. 来源覆盖

实际入口、查询和原字段见[本日原始覆盖与停点](../_sources/daily-20260429/V3_REOPEN_NOTES.md)§日源分批覆盖，以及[最新数量/有限裁定](../_sources/daily-20260429/V3_CLOSE_RECONCILIATION.md)。下表的已检查只指所述有界范围已处理，历史子目录受限不支撑全网无遗漏；未可恢复项在§5明确隔离。每周来源未扫描；仅实际触发的官方代码/发布证据定点打开。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research index、official News RSS相邻项、04/28 release notes；RSS将community-safety/openai-on-aws归04/28 08BJT前窗，04/29cyber/compute/goblins为后窗；picker产品改动前闭 | 已检查 | RSS非所有artifact历史档案，不宣称全站零 |
| SRC-ANTHROPIC | Research首屏止08/2026、官方域具名补检、16812v1/v2必要正文差分；Introspection v2仅链接/引用补充；CreativeWork产品、BioMysteryBench科学应用、RSP治理权责均具体前闭 | 已检查 | SeeMore历史分页不可恢复，已隔离；日标签贡献前闭不补造时刻 |
| SRC-GOOGLE-AI | April Blog ERA04/29→04/22；DeepMind page3 04/30→27→23；Publications默认1–15/11555；ERA四AI-for-Science应用前闭，Growing-to-Looping定点归02/18旧v1 | 已检查 | 2026 Publications360项交互筛选不可恢复，不以默认title页证明历史零 |
| SRC-META-AI | Blog06/29→04/08；Publications页1至05/26，页2新近05/19→05/04→04/16/14/09；所查邻接未列本窗新稿，Research抽取零由可读目录补检 | 已检查 | 页2后半2018–21混排，不能证明全库按日期闭合 |
| SRC-QWEN | 官方Research API path=flashqla、04/28固定README/benchmark ref；FlashQLA一个家族确定本窗；当前SM100/120与后发tags不倒灌 | 已检查 | 旧article URL404，由official API和历史commit限定核心机制 |
| SRC-DEEPSEEK | news相邻09/10→04/24→2025/12/01，research06/24→02/25→01/28；新PR26缩18、DeepEP610具名补检；181/616后窗合并，610只是NIC选择/ibstat fallback前闭；epv2主干release后窗 | 已检查 | 两个查看全部不可分页，PR查询不覆盖全部旧merge/私有转公开 |
| SRC-MOONSHOT | Kimi Platform Blog可见26项2025/11→2024/05；1.40release与2087/2045；创建16PR核四审批未合并；1.40为一个已发布家族，2003前窗累计背景，未合并提案不倒灌 | 已检查 | Blog历史2026未显示、query只限创建日/具名version |
| SRC-TENCENT-HUNYUAN | 官网实际publicList render0 9/9与render1 6/6 English；同响应三日期字段；id100039内部publishedApr26但public/displayApr30，不入窗；R-DMesh Apr29 07:36Z后窗 | 已检查 | 仅当前公开English目录，不证删除/中文目录/所有repo |
| SRC-ZAI | Research05/20→04/29→04/07、release notes06/16→04/07、ImageMining/RPC-Bench必要公开内容；ScalingPain04/29 16BJT后窗；RPC旧论文/May13数据；ImageMining历史README/217题仅图像使用时点与crop/search切片，无受控model/tool/no-image证据，未改变已有multimodal评价合同而贡献前闭 | 已检查 | repo created/commit不独证历史public，未扫描所有既有repo |
| SRC-BYTEDANCE-SEED | Research05/16→04/26→04/22、论文目录API两页1–40/242第二页05/12→04/08；VeOmni相邻release/触发PR；697实际SP dummy修复保留；705dispatch与706accessor前闭；699/700未合并 | 已检查 | 27505 CMS日粗且arxiv后窗终态隔离；不全扫13页/私有转公开 |
| SRC-BAIDU-ERNIE | Blog05/09→04/30→04/15→02/06；ERNIE release/main本窗API；实际触发FastDeploy两PR；ERNIE已查repo事件未命中；FastDeploy7655受限保留，7623文字与diff反证前闭 | 已检查 | 不把Paddle全组织90PR当候选；release/默认branch范围不覆盖全部支线 |
| SRC-XIAOMI-MIMO | Paper06/29→03/13→02/03；Blog首15缺日期；ASR2/3创建PR与MiMoCode相邻release；ASR两PR未合并，兼容/文档前闭；已查main/release无窗项 | 已检查 | Blog日期不可恢复；repo创建/merge空不等所有artifact零 |
| SRC-MINIMAX | 英/中文Blog06月→05/26/27→03/18；techblog llms.txt agent-team单篇；CLI119–121与创建/mergequery；AgentTeam英文05/27中文04/27日期分歧不拿旧家族加本窗；CLI三PR均截止后 | 已检查 | techblog只当前索引范围，目录/创建查询不覆盖全历史 |
| SRC-ARXIV | CL/LG/DC/AI及CV/RO/AR/PL/OS/PF/IR/MA主题窄检，MM MarkIt定点；OAI/API/DOI宽代理仅查漏；106完整题摘=65潜在+38前闭+3早公开；潜在6日期隔离，59当窗论文；官方公告规则+24764/65和25918/19 v1边界+邻DOI联合支持08BJT批 | 已检查 | 历史new?date忽略参数；1286宽并集不是新稿/摘要/候选；联合批次是有据推断，仍保六项例外 |
| 表外：[FastDeploy](https://github.com/PaddlePaddle/FastDeploy/pull/7655) | 只核7655/7623原动机及最小files diff，非90PR逐项筛选；7655workspace上界有实际改变 | 已检查 | 作者未给accuracy tests，不称全路径修复/生产安全 |

## 3. 候选与判断

论文首次公开采用范围 `2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00`：公告时分配ID、两侧v1边界和相邻DOI代理的联合推断已获root独立认可，不是submitted/DOI单字段首公开证明。各家族更早公开的六项例外已剔出确定当窗清单；稿内August日期等排版字段不覆盖版本身份。评分为本次实际增量的Design Delta+System Reach+Durability，旧评分不继承。5–6分若真实知识缺口/安全纠错触发，已对采用部分局部深入；以下“完成”描述作者必要审阅，非整日非作者Gate。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Semantic Denial of Service in LLM-controlled robots](https://arxiv.org/html/2604.24790v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 未认证安全告警可造成hard-stop/acknowledge非任务动作，来源格式与control DSR须分账；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；见§4 |
| [Versioned Late Materialization for Ultra-Long Sequence Training in Recommendation Systems at Scale](https://arxiv.org/html/2604.24806v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 晚物化历史降低写放大但事件时间范围不能单独保证训练重建旧输入；3+2+3=8 | 争议 | 暂缓：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)；见§4 |
| [Nautile-370M: Spectral Memory Meets Attention in a Small Reasoning Model](https://arxiv.org/html/2604.24809v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 有限谱状态与周期attention尝试改变sequence容量/执行取舍；3+2+3=8 | 争议 | 暂缓：MODEL-TRANSFORMER-LAYER [Ch17](../../../../books/part-02-model/17-transformer-layer.md)；见§4 |
| [Programming with Data: Test-Driven Data Engineering for Self-Improving LLMs from Raw Corpora](https://arxiv.org/html/2604.24819v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 共享知识层级同时生成训练L1/L2与测试L3，可以把失败题回溯成具名repair proposal；同源图并不赋予holdout独立性，LLM缺概念/缺推理标签不是因果诊断。拟在failure-driven段后一段，再在lineage段复用而不重复；3+2+2=7 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)；见§4 |
| [Salca: A Sparsity-Aware Hardware Accelerator for Efficient Long-Context Attention Decoding](https://arxiv.org/html/2604.24820v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | exact selector在严格K/精确排名重要时合理；近似score+histogram threshold可以减少选择器代价，但阈值桶ties会膨胀预算，原K/V上的attention只对选中项精确；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；Ch49:787–791，apr28 source→owner/写后通过 |
| [Latent Agents: A Post-Training Procedure for Internalized Multi-Agent Debate](https://arxiv.org/html/2604.24881v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 完整辩论轨迹蒸馏与长度奖励换在线token但失去外显独立交互；2+1+2=5 | 标准完成 | 仅报告：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；见§4 |
| [VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations](https://arxiv.org/html/2604.24885v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 自适应patch/grid与可控1Dlatent把输入分辨率、长度和生成目标解耦；2+1+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；见§4 |
| [VISION-SLS: Safe Perception-Based Control from Learned Visual Representations via System Level Synthesis](https://arxiv.org/html/2604.24894v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 视觉压缩误差envelope与reachable tube联系controller可行性；3+2+2=7 | 争议 | 暂缓：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；见§4 |
| [Safety Drift After Fine-Tuning: Evidence from High-Stakes Domains](https://arxiv.org/html/2604.24902v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 温和微调、PEFT类别和参数距离不能代替派生artifact的构念分层安全评测；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；见§4 |
| [SUDP: Secret-Use Delegation Protocol for Agentic Systems](https://arxiv.org/html/2604.24920v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 把secret-use授权绑定scope/operation/custodian及可信render而不向Agent暴露秘密；3+2+3=8 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；见§4 |
| [Libra-VLA: Achieving Learning Equilibrium via Asynchronous Coarse-to-Fine Dual-System](https://arxiv.org/html/2604.24921v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 离散/连续二选之外，粗离散方向序列可串行条件化细连续动作，绑定codebook/horizon/observation及teacher→predicted exposure切换。拟在action表示处两段，不重复已有异步lease合同；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；见§4 |
| [Large Language Models Explore by Latent Distilling](https://arxiv.org/html/2604.24927v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 生成期间共享在线latent distiller增加候选多样性但改变采样状态；2+2+2=6 | 争议 | 暂缓：MODEL-SAMPLING [Ch20](../../../../books/part-02-model/20-sampling.md)；见§4 |
| [GAIA-v2-LILT: Multilingual Adaptation of Agent Benchmark beyond Translation](https://arxiv.org/html/2604.24929v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 多语言benchmark需保持query-answer/locale可解性而非翻译流利即可；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；见§4 |
| [Learning from Noisy Preferences: A Semi-Supervised Learning Approach to Direct Preference Optimization](https://arxiv.org/html/2604.24952v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 现有update gate不改变pair真值；受限分支可按去噪时段将无标注pair的margin符号作为伪标签，分时阈值准入且保clean anchors。拟两段，若peer认为只是已有admission的局部recipe，则Only不强写；2+1+2=5 | 深入完成 | 整合：TRAIN-DPO [Ch34](../../../../books/part-04-training-system/34-dpo.md)；见§4 |
| [ViPO: Visual Preference Optimization at Scale](https://arxiv.org/html/2604.24953v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 不同受测偏好数据状态下Poly-DPO的α工作点变化，修正复杂loss必然胜过标准DPO的判断；2+1+2=5 | 标准完成 | 仅报告：TRAIN-DPO [Ch34](../../../../books/part-04-training-system/34-dpo.md)；见§4 |
| [BenchGuard: Who Guards the Benchmarks? Automated Auditing of LLM Agent Benchmarks](https://arxiv.org/html/2604.24955v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 发布前互核instruction×reference program×scoring code×environment；已有Agent trace只作反例，benchmark owner/专家裁决；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Ch66:1169–1173，apr28 source→owner/写后通过 |
| [Compute Aligned Training: Optimizing for Test Time Inference](https://arxiv.org/html/2604.24957v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 可解析test-time聚合算子用边际权重近似不同于实际运行controller；2+2+2=6 | 争议 | 暂缓：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)；见§4 |
| [PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference](https://arxiv.org/html/2604.24971v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 一次压缩多reader暴露公共prefix的质量—物理容量边界；2+2+2=6 | 争议 | 暂缓：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；见§4 |
| [Adaptive Prompt Embedding Optimization for LLM Jailbreaking](https://arxiv.org/html/2604.24983v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 白盒连续embedding注入与普通text-only重新lookup不是同一攻击接口；2+1+2=5 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；见§4 |
| [Why Does Reinforcement Learning Generalize? A Feature-Level Mechanistic Study of Post-Training in Large Language Models](https://arxiv.org/html/2604.25011v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 共同crosscoder坐标与双向干预为RL/SFT泛化比较提供局部因果证据；2+2+2=6 | 标准完成 | 仅报告：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)；见§4 |
| [Why Search When You Can Transfer? Amortized Agentic Workflow Design from Structural Priors](https://arxiv.org/html/2604.25012v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 其它任务搜索轨迹可凝成带版本的结构先验与输出contract，新任务免逐任务搜索但仍要编译/执行验收。拟topology段后两段区分来源搜索资产与目标任务执行事实；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；Ch82:179–183，apr28 source→owner/写后通过 |
| [DiscreteRTC: Discrete Diffusion Policies are Natural Asynchronous Executors](https://arxiv.org/html/2604.25050v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 不再另写prefix原则；仅补原生随机mask训练如何使离散policy用已解码prefix补全suffix、近端s项解完可早停、未解码proposal状态可带入下一轮；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；Ch26:559–563，apr28 source→owner/写后通过 |
| [Beyond Accuracy: Benchmarking Cross-Task Consistency in Unified Multimodal Models](https://arxiv.org/html/2604.25072v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 同一scene/fact identity同时冻结理解正确、生成正确与agreement，并显式统计两边同错、缺失节点及歧义匹配。拟identity或多模态评价两段，采用测量设计不正面采用覆盖率不清的公式；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Ch66:207–211，apr28 source→owner/写后通过 |
| [CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration](https://arxiv.org/html/2604.25080v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | KV恢复分token/layer/stage依赖图与整批I/O优先级联动；3+3+2=8 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；见§4 |
| [Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling](https://arxiv.org/html/2604.25098v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 删整层与小比例权重mask对多thinking预算的退化不同；2+1+2=5 | 标准完成 | 仅报告：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；见§4 |
| [One Perturbation, Two Failure Modes: Probing VLM Safety via Embedding-Guided Typographic Perturbations](https://arxiv.org/html/2604.25102v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 低ASR可能来自模型读不懂退化字形，不能直接称安全拒绝；2+1+2=5 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；Ch72:1053–1057，apr28 source→owner/写后通过 |
| [Structured Security Auditing and Robustness Enhancement for Untrusted Agent Skills](https://arxiv.org/html/2604.25109v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 多文件skill预加载审计的risk flagged与malicious recall必须分开；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；见§4 |
| [Evaluation without Generation: Non-Generative Assessment of Harmful Model Specialization with Applications to CSAM](https://arxiv.org/html/2604.25119v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 输出不宜生成时，可用绑定base/adapter/probe/layer/time/label/threshold的无输出内部功能探针作分发前受限证据；直接训练类别与危险生成能力分账；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Ch66:194–198，apr28 source→owner/写后通过 |
| [What Makes Good Instruction-Tuning Data? An In-Context Learning Perspective](https://arxiv.org/html/2604.25132v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 样本自身难度与one-shot邻域帮助不是同一数据选择proxy；2+1+2=5 | 标准完成 | 仅报告：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)；见§4 |
| [Training Transformers as a Universal Computer](https://arxiv.org/html/2604.25166v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 有限操作语义模板与稀有stack plan采样让局部解释规则可训练；外部call/ret帧清理使在线上下文按活跃空间而非累计轨迹；2+1+2=5 | 深入完成 | 整合：MODEL-DECODER-ONLY [Ch18](../../../../books/part-02-model/18-decoder-only.md)；Ch18:282–286，apr28 source→owner/写后通过 |
| [AgentDID: Trustless Identity Authentication for AI Agents](https://arxiv.org/html/2604.25189v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 去中心化身份凭证不替代effect-time context与实际权限；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；见§4 |
| [BARRED: Synthetic Training of Custom Policy Guardrails via Asymmetric Debate](https://arxiv.org/html/2604.25203v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 定制policy边界生成与标签核验通过直接消融分开；2+1+2=5 | 标准完成 | 仅报告：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)；见§4 |
| [When the Forger Is the Judge: GPT-Image-2 Cannot Recognize Its Own Faked Documents](https://arxiv.org/html/2604.25213v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 局部生成文档编辑使传统splice取证检测退化并暴露自审盲点；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；见§4 |
| [VLM Judges Can Rank but Cannot Score: Task-Dependent Uncertainty in Multimodal Evaluation](https://arxiv.org/html/2604.25235v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 视觉judge排序与绝对score区间可用性按任务分账；2+2+2=6 | 争议 | 暂缓：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；见§4 |
| [Below-Chance Blindness: Prompted Underperformance in Small LLMs Produces Positional Bias Rather than Answer Avoidance](https://arxiv.org/html/2604.25249v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | below-chance未命中不能排除能力压低，选项位置偏差另验；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；见§4 |
| [QFlash: Bridging Quantization and Memory Efficiency in Vision Transformer Attention](https://arxiv.org/html/2604.25306v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 整数online-softmax必须共同定义跨tile rowmax比较单位、累加/scale-release、整数指数近似与scale生成/重标定成本，不只是QK/PV换dtype；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；Ch49:1026–1030，apr28 source→owner/写后通过 |
| [FusionCIM: Accelerating LLM Inference with Fusion-Driven Computing-in-Memory Architecture](https://arxiv.org/html/2604.25317v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 不另写diagonal rowmax；仅CIM write昂贵时KV-stationary vs Q/O-stationary改变多query重载/转置/partial sum，KV stream与FP16SFU共同定价；2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；Ch49:756–760，apr28 source→owner/写后通过 |
| [Benchmarking and Improving GUI Agents in High-Dynamic Environments](https://arxiv.org/html/2604.25380v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 动作间漏观测单独成为高动态GUI EvalSpec轴；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；见§4 |
| [Biased Dreams: Limitations to Epistemic Uncertainty Quantification in Latent Dynamics Models](https://arxiv.org/html/2604.25416v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | latent attractor会让ensemble一步分歧降低但同动作/horizon下物理误差或奖励乐观增长；uncertainty必须按rollout horizon对真实outcome校准，低分歧不是低错误；3+2+3=8 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；Ch25:273–277，apr28 source→owner/写后通过 |
| [JURY-RL: Votes Propose, Proofs Dispose for Label-Free RLVR](https://arxiv.org/html/2604.25419v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | plurality提案、Lean proof奖励与拒证residual探索必须分责；2+2+2=6 | 争议 | 暂缓：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)；见§4 |
| [FED-FSTQ: Fisher-Guided Token Quantization for Communication-Efficient Federated Fine-Tuning of LLMs on Edge Devices](https://arxiv.org/html/2604.25421v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | Fisher-guided token压缩需计codec/端侧资源/目标质量总成本；2+2+2=6 | 争议 | 暂缓：TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；见§4 |
| [The Forensic Cost of Watermark Removal: From Dedicated Attacks to Image Editing](https://arxiv.org/html/2604.25491v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 水印移除ASR、图像质量和独立移除痕迹TPR@FPR为三轴；第三轴正例只能触发triage，不证明来源/权属/恶意；2+1+2=5 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；Ch72:905–909，apr28 source→owner/写后通过 |
| [Walking Through Uncertainty: An Empirical Study of Uncertainty Estimation for Audio-Aware Large Language Models](https://arxiv.org/html/2604.25591v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 音频不确定性sensor在正常与不可答任务的排名反转；2+1+2=5 | 标准完成 | 仅报告：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；见§4 |
| [Refinement via Regeneration: Enlarging Modification Space Boosts Image Refinement in Unified Multimodal Models](https://arxiv.org/html/2604.25636v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 保留精确像素资产的edit与保留语义意图的regen是两种contract；后者可只消费initial视觉语义与prompt，不带原VAE像素，训练也须匹配重生而非edit目标；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；Ch24:1210–1214，apr28 source→owner/写后通过 |
| [NVLLM: A 3D NAND-Centric Architecture Enabling Edge on-Device LLM Inference](https://arxiv.org/html/2604.25699v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | FFN权重留NANDcompute而attention/KV留LPDDR，error快检/慢纠正用scoreboard补缺segment MAC后才可提交；权重放置、错误authority与剩余KV瓶颈一起预算；2+2+2=6 | 深入完成 | 整合：INFER-GPU-MEMORY [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)；Ch54:528–532，apr28 source→owner/写后通过 |
| [Step-Audio-R1.5 Technical Report](https://arxiv.org/html/2604.25719v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 音频输入—文本回答的分数不能签发输出韵律/沉浸改善；2+1+2=5 | 深入完成 | 仅报告：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)；见§4 |
| [Scalable Inference Architectures for Compound AI Systems: A Production Deployment Study](https://arxiv.org/html/2604.25724v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 复合workflow的model-specific arrival/readiness与冷启依赖影响端到端关键路径；2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；Ch56:648–652，apr28 source→owner/写后通过 |
| [Toward Scalable Terminal Task Synthesis via Skill Graphs](https://arxiv.org/html/2604.25727v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | skill graph生成路径与实际scenario-skill轨迹覆盖是不同数据分母；2+2+2=6 | 争议 | 暂缓：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)；见§4 |
| [Barriers to Universal Reasoning With Transformers (And How to Overcome Them)](https://arxiv.org/html/2604.25800v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 表达可模拟TM≠有限trace可学长度泛化；固定alphabet、位置/计算语言与learner假设决定负结果，可增长signpost/value-change日志又是不同正条件；3+1+3=7 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；Ch5:80–84，apr28 source→owner/写后通过 |
| [Mutual Forcing: Dual-Mode Self-Evolution for Fast Autoregressive Audio-Video Character Generation](https://arxiv.org/html/2604.25819v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 共享权重Few产历史，Multi在Few历史上学真实当前flow，再stopgrad反教Few区间位移，训练history producer与reference双向耦合，部署Few；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；Ch24:358–362，apr28 source→owner/写后通过 |
| [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/html/2604.25850v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | harness演进的修复预测和实际fix/regression集合不等价；2+1+2=5 | 标准完成 | 仅报告：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)；见§4 |
| [SIEVES: Selective Prediction Generalizes through Visual Evidence Scoring](https://arxiv.org/html/2604.25855v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 黑盒视觉定位/crop回答连贯性补充选择性回答sensor；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；见§4 |
| [Privileged Foresight Distillation: Zero-Cost Future Correction for World Action Models](https://arxiv.org/pdf/2604.25859v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 同backbone/noise只换future attention mask，teacher真实未来与当前base的action velocity差作为stopgrad residual，adapter部署只读当前frame；区别future-feature表示监督；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；Ch26:284–288，apr28 source→owner/写后通过 |
| [When Errors Can Be Beneficial: A Categorization of Imperfect Rewards for Policy Gradient](https://arxiv.org/html/2604.25872v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | pairwise RM accuracy不能代替当前policy概率/相对误奖下的真实更新收益；3+2+3=8 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)；见§4 |
| [MarkIt: Training-Free Visual Markers for Precise Video Temporal Grounding](https://arxiv.org/html/2604.25886v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | query-mask与frame index共同外显但视觉overlay也是有损输入变换；2+1+2=5 | 标准完成 | 仅报告：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；见§4 |
| [Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers](https://arxiv.org/html/2604.25891v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 冻结checkpoint/干预×训练cue类别×标准/同义/反义/格式×任务矩阵，普通EM零不代签训练条件行为清除；3+2+3=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Ch66:343–347，apr28 source→owner/写后通过 |
| [Pythia: Exploiting Workflow Predictability for Efficient Agent-Native LLM Serving](https://arxiv.org/html/2604.25899v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | workflow/session/role低权限身份供cache/priority/replica共同可降级预测；2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；见§4 |
| [How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum](https://arxiv.org/html/2604.25907v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 逐例成功边际P^−q改变跨样本目标权重，GARL prior-rollout与PAFT posterior-resample梯度路径不同；不是只补全零group或调LR；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)；Ch33:437–441，apr28 source→owner/写后通过 |
| [Recursive Multi-Agent Systems](https://arxiv.org/html/2604.25917v1) | 2026-04-29T08:00:00+08:00 ～ 2026-04-29T09:00:00+08:00 | 冻结backbone的跨latent环训练可作受限观察，但frozen backbone的RecLink跨latent循环终局CE更新links确有受限设计，但中央梯度稳定保证未立。若peer允许非争议机制，必须明说train/deploy depth identity并保text/单模型回退；2+2+2=6 | 争议 | 暂缓：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；见§4 |
| [FlashQLA: CP-/Bwd-Friendly Fused Linear Attention Kernels for GDN](https://github.com/QwenLM/FlashQLA/blob/59849a34dc0baeae5f56012f25f3f5726fc3fabc/README.md) | 2026-04-28T10:00:00+08:00 | 小batch×heads使全融合欠占用，CP预处理与两段融合共同选择；gate-decay warmup只是有限近似；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；见§4 |
| [Kimi CLI 1.40.0](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.40.0) | 2026-04-28T21:51:04+08:00 | 审批presence与autoapproval正交，等待policy与turn/source清理不等用户拒绝；2+2+2=6 | 深入完成 | 整合：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)；见§4 |
| [VeOmni #697: Fix vision dummy forward under sequence parallelism](https://github.com/ByteDance-Seed/VeOmni/pull/697) | 2026-04-28T10:50:22+08:00 | 空模态rank参加collective的dummy路径必须与真实输入保持local tensor/metadata layout parity；2+2+2=6 | 深入完成 | 整合：TRAIN-MEGATRON [Ch40](../../../../books/part-04-training-system/40-megatron.md)；见§4 |
| [FastDeploy #7655: multimodal routing buffer bound](https://github.com/PaddlePaddle/FastDeploy/pull/7655) | 2026-04-28T21:52:03+08:00 | scheduler文本token上界不等multimodal内部routing激活上界，workspace sizing改读max_chunk_tokens；2+1+2=5 | 标准完成 | 仅报告：INFER-PREFILL [Ch43](../../../../books/part-05-inference-system/43-prefill.md)；见§4 |

## 4. 证据与知识整合

原始exact-v1及必要位置支持下述受限判断；作者结果、独立评价、实现核与复现分开。没有本地GPU/机器人/芯片实验，未披露的生产concurrency/SLO为Not Disclosed或不适用；微基准、架构模拟与单任务均值不拼成端到端保证。已有覆盖指本章明确承载的命题，不称论文结果已由书稿独立测出。

### [Semantic Denial of Service in LLM-controlled robots](https://arxiv.org/html/2604.24790v1)

未认证安全告警可造成hard-stop/acknowledge非任务动作，来源格式与control DSR须分账。模拟四VLM/七prompt，不是真实STT或机械臂；防御有显著减轻反例；Ch72:1630–1639现有可用性与authority分账，root认Existing [必要原文位置与直接反证](../_sources/daily-20260429/V3_REOPEN_NOTES.md)。Books：已有覆盖，唯一owner `PLATFORM-SECURITY`（[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [Versioned Late Materialization for Ultra-Long Sequence Training in Recommendation Systems at Scale](https://arxiv.org/html/2604.24806v1)

晚物化历史降低写放大但事件时间范围不能单独保证训练重建旧输入。§3精确重建前提与§4删除/compaction冲突；迟到事件/等长替换反例；需pinned generation/可见性/失败路径，不采O2O无条件保证 [必要原文位置与直接反证](../_sources/daily-20260429/V3_VERSIONED_LATE_MATERIALIZATION_24806_BOUNDED_REVIEW.md)。Books：暂缓，唯一owner `TRAIN-DATA`（[Ch27](../../../../books/part-04-training-system/27-data.md)）；中央争议不作正面依据、不新增书稿，保留局部观察；精确重开材料见§5及单篇笔记。

### [Nautile-370M: Spectral Memory Meets Attention in a Small Reasoning Model](https://arxiv.org/html/2604.24809v1)

有限谱状态与周期attention尝试改变sequence容量/执行取舍。Theorem1取d=t=1的L2积分发散；query含目标h；有限谱不足任意exact recall，1024context/未匹配训练预算不证明通用替代 [必要原文位置与直接反证](../_sources/daily-20260429/V3_NAUTILE_24809_BOUNDED_REVIEW.md)。Books：暂缓，唯一owner `MODEL-TRANSFORMER-LAYER`（[Ch17](../../../../books/part-02-model/17-transformer-layer.md)）；中央争议不作正面依据、不新增书稿，保留局部观察；精确重开材料见§5及单篇笔记。

### [Programming with Data: Test-Driven Data Engineering for Self-Improving LLMs from Raw Corpora](https://arxiv.org/html/2604.24819v1)

共享知识层级同时生成训练L1/L2与测试L3，可以把失败题回溯成具名repair proposal；同源图并不赋予holdout独立性，LLM缺概念/缺推理标签不是因果诊断。拟在failure-driven段后一段，再在lineage段复用而不重复。§2.1–2.2、§4.1–4.3/Eq5，§3.4/Table2：Eq5的输入分流不排除L2组合复现L3；Llama C-Eval60.64→50.23反驳通用能力完全保留。必须另测item/语义重合、source-chunk split及独立能力holdout。 实际owner对照：Failure-driven Curriculum 与 Typed Lineage Graph，当前453–475、766–790。root源→owner与实际写后已通过，采用原两段literal。  [必要原文位置与直接反证](../_sources/daily-20260429/V3_PRODA_24819_BOUNDED_REVIEW.md)。Books：整合，唯一owner `TRAIN-DATA`（[Ch27](../../../../books/part-04-training-system/27-data.md)）；仅上述机制与限定边界已实际落正文，独立写后记录见§6。

### [Salca: A Sparsity-Aware Hardware Accelerator for Efficient Long-Context Attention Decoding](https://arxiv.org/html/2604.24820v1)

exact selector在严格K/精确排名重要时合理；近似score+histogram threshold可以减少选择器代价，但阈值桶ties会膨胀预算，原K/V上的attention只对选中项精确。 §3.1–3.2、§4、§5.1–5.3/Tables3/6：2bitKey/3bitQuery/heavy channels是受限工作点；Vicuna质量下降，5.8%设计点≠9.4%质量协议；RTL+综合+U280功耗不等流片/Serving；对旧ASIC比较是假设供给公式折算。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_SALCA_24820_BOUNDED_REVIEW.md)。Books：整合，唯一owner `INFER-TENSORRT-LLM`（[当前章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)），实际两段位于Ch49:787–791；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [Latent Agents: A Post-Training Procedure for Internalized Multi-Agent Debate](https://arxiv.org/html/2604.24881v1)

完整辩论轨迹蒸馏与长度奖励换在线token但失去外显独立交互。§2–4/Table1、AppP/Q：MMLU-Pro/GSM8K有退步，前置训练未匹配；角色style干预≠内部独立Agent；Ch82显式/latent权限既有 [必要原文位置与直接反证](../_sources/daily-20260429/V3_LATENT_AGENTS_24881_BOUNDED_REVIEW.md)。Books：仅报告，唯一owner `AGENT-MULTI-AGENT`（[Ch82](../../../../books/part-07-agent/82-multi-agent.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations](https://arxiv.org/html/2604.24885v1)

自适应patch/grid与可控1Dlatent把输入分辨率、长度和生成目标解耦。§3–5/Tables：179G仅无KV单forward，generalist低于specialist；Ch23 resolution/aspect、N/K、decoder与matched generator frontier已有具体承载 [必要原文位置与直接反证](../_sources/daily-20260429/V3_VIBETOKEN_24885_BOUNDED_REVIEW.md)。Books：已有覆盖，唯一owner `MULTIMODAL-REPRESENTATION`（[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [VISION-SLS: Safe Perception-Based Control from Learned Visual Representations via System Level Synthesis](https://arxiv.org/html/2604.24894v1)

视觉压缩误差envelope与reachable tube联系controller可行性。Prop3需真实有界残差；Eq31可slack，经验覆盖91.4–99%与car违约1.6%不能成硬安全；需可证真实残差/无slack条件再开 [必要原文位置与直接反证](../_sources/daily-20260429/V3_VISION_SLS_24894_BOUNDED_REVIEW.md)。Books：暂缓，唯一owner `MULTIMODAL-EMBODIED-VLA`（[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)）；中央争议不作正面依据、不新增书稿，保留局部观察；精确重开材料见§5及单篇笔记。

### [Safety Drift After Fine-Tuning: Evidence from High-Stakes Domains](https://arxiv.org/html/2604.24902v1)

温和微调、PEFT类别和参数距离不能代替派生artifact的构念分层安全评测。§3–4 Figure4与judgeprompt反转；31生态样本与受控配置非同预算100独立模型；Ch72派生artifact完整回归/Ch31平均KL非slice保证已承载 [必要原文位置与直接反证](../_sources/daily-20260429/V3_SAFETY_DRIFT_24902_BOUNDED_REVIEW.md)。Books：已有覆盖，唯一owner `PLATFORM-SECURITY`（[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [SUDP: Secret-Use Delegation Protocol for Agentic Systems](https://arxiv.org/html/2604.24920v1)

把secret-use授权绑定scope/operation/custodian及可信render而不向Agent暴露秘密。§协议/威胁模型：adapter完整性、one-use、可信render和custodian前提，availability除外；root source→owner及写后PASS Ch72:2197–2201 [必要原文位置与直接反证](../_sources/daily-20260429/V3_REOPEN_NOTES.md)。Books：整合，唯一owner `PLATFORM-SECURITY`（[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)）；仅上述机制与限定边界已实际落正文，独立写后记录见§6。

### [Libra-VLA: Achieving Learning Equilibrium via Asynchronous Coarse-to-Fine Dual-System](https://arxiv.org/html/2604.24921v1)

离散/连续二选之外，粗离散方向序列可串行条件化细连续动作，绑定codebook/horizon/observation及teacher→predicted exposure切换。拟在action表示处两段，不重复已有异步lease合同。§2.1–2.2、§3.1–3.4、§4.3/Tables3–6、§5：FIFO后M−1步不重算，尚无动态意图有效性验证；N10只四bin工作点；M2→5平均122→104ms同时success97.2→95.3；保单头/同步/独立安全controller。 实际owner对照：VLA policy135–143，Serving/control547–555。root源→owner与实际写后已通过，采用原两段literal。  [必要原文位置与直接反证](../_sources/daily-20260429/V3_LIBRAVLA_24921_BOUNDED_REVIEW.md)。Books：整合，唯一owner `MULTIMODAL-EMBODIED-VLA`（[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)）；仅上述机制与限定边界已实际落正文，独立写后记录见§6。

### [Large Language Models Explore by Latent Distilling](https://arxiv.org/html/2604.24927v1)

生成期间共享在线latent distiller增加候选多样性但改变采样状态。§4–5/AppA.2：两步r1=r2=1满足零后永零却Q1=1+γ，反驳逐步最优；实际LD亦不满足理想定义；低预算/共享prompt有反退，暂不采理论保证 [必要原文位置与直接反证](../_sources/daily-20260429/V3_ESAMP_24927_BOUNDED_REVIEW.md)。Books：暂缓，唯一owner `MODEL-SAMPLING`（[Ch20](../../../../books/part-02-model/20-sampling.md)）；中央争议不作正面依据、不新增书稿，保留局部观察；精确重开材料见§5及单篇笔记。

### [GAIA-v2-LILT: Multilingual Adaptation of Agent Benchmark beyond Translation](https://arxiv.org/html/2604.24929v1)

多语言benchmark需保持query-answer/locale可解性而非翻译流利即可。§方法/评价：165题五语言、10.9–32.7百分点局部反转，共现issue非因果；Ch66派生benchmark语义保持编译与locale切片已承载 [必要原文位置与直接反证](../_sources/daily-20260429/V3_GAIA_LILT_24929_BOUNDED_REVIEW.md)。Books：已有覆盖，唯一owner `PLATFORM-EVALUATION-SYSTEM`（[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [Learning from Noisy Preferences: A Semi-Supervised Learning Approach to Direct Preference Optimization](https://arxiv.org/html/2604.24952v1)

现有update gate不改变pair真值；受限分支可按去噪时段将无标注pair的margin符号作为伪标签，分时阈值准入且保clean anchors。拟两段，若peer认为只是已有admission的局部recipe，则Only不强写。§3.3/Eq8–10、App6.2/Eq16、App6.9/Table7、§4/Tables2/4：五proxy共识非人类真值；margin不是校准概率；同clean test portion调阈值；二元组间variance不证明次优收敛；晚段准确率59%；两轮质量不能与一轮132GPUh混用。 实际owner对照：Probability-geometry Gate208–234，相邻Ch31 preference truth / Ch24 diffusion time。root源→owner与实际写后已通过，采用原两段literal。  [必要原文位置与直接反证](../_sources/daily-20260429/V3_SEMIDPO_24952_BOUNDED_REVIEW.md)。Books：整合，唯一owner `TRAIN-DPO`（[Ch34](../../../../books/part-04-training-system/34-dpo.md)）；仅上述机制与限定边界已实际落正文，独立写后记录见§6。

### [ViPO: Visual Preference Optimization at Scale](https://arxiv.org/html/2604.24953v1)

exact-v1 Eq9–10在标准DPO上增加α(1−p)，梯度额外乘1+αp；§5.2三个视觉偏好设置分别选择正、负和近零α，支持复杂loss收益依赖受测数据条件的局部反例，不是已交付的自动噪声诊断器。三组同时改变生成模型、标注与SFT，不能唯一归因于标签质量；五RM共识不是人类真值，Table1视频3万与正文30万冲突隔离，不用于规模或成本保证。Table2/4又有已发布checkpoint和SFT组合混杂，不能把所有收益归α。[必要原文位置与直接反证](../_sources/daily-20260429/V3_VIPO_24953_BOUNDED_REVIEW.md)。Books：仅报告，唯一机制owner `TRAIN-DPO`（[Ch34](../../../../books/part-04-training-system/34-dpo.md)）；原偏好数据/目标分账由Ch31交接，尚无可迁移α控制规则，不为局部配方另写。非作者已核必要原文与实际owner，最终处置通过；见§6。

### [BenchGuard: Who Guards the Benchmarks? Automated Auditing of LLM Agent Benchmarks](https://arxiv.org/html/2604.24955v1)

发布前互核instruction×reference program×scoring code×environment；已有Agent trace只作反例，benchmark owner/专家裁决。 §3.1–3.3、§4–5/Tables2–3：12确认缺陷非102task全误报率；BIX17修订task拆24issue、20/24exact对齐不是50task真precision；五模型union非独立，$14.38不含人工。无oracle或不可逆effect不套检出率。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_BENCHGUARD_24955_BOUNDED_REVIEW.md)。Books：整合，唯一owner `PLATFORM-EVALUATION-SYSTEM`（[当前章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)），实际两段位于Ch66:1169–1173；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [Compute Aligned Training: Optimizing for Test Time Inference](https://arxiv.org/html/2604.24957v1)

可解析test-time聚合算子用边际权重近似不同于实际运行controller。Eq7/Table1系数与AppB不同扰动导数/安全下降语句冲突；Pass@N特例与有限MATH结果保留；需统一公式/近似条件，暂不Book正面采用 [必要原文位置与直接反证](../_sources/daily-20260429/V3_CAT_24957_BOUNDED_REVIEW.md)。Books：暂缓，唯一owner `TRAIN-GRPO`（[Ch33](../../../../books/part-04-training-system/33-grpo.md)）；中央争议不作正面依据、不新增书稿，保留局部观察；精确重开材料见§5及单篇笔记。

### [PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference](https://arxiv.org/html/2604.24971v1)

一次压缩多reader暴露公共prefix的质量—物理容量边界。§3.2uint8索引与3bit存储公式不自洽；§3.3每Agent解压DynamicCache，Table4池字节≠并发peak；需packing和allocator/ownership证据；Ch45/47已有物理峰值/COW责任 [必要原文位置与直接反证](../_sources/daily-20260429/V3_REOPEN_NOTES.md)。Books：暂缓，唯一owner `INFER-KV-CACHE`（[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)）；中央争议不作正面依据、不新增书稿，保留局部观察；精确重开材料见§5及单篇笔记。

### [Adaptive Prompt Embedding Optimization for LLM Jailbreaking](https://arxiv.org/html/2604.24983v1)

白盒连续embedding注入与普通text-only重新lookup不是同一攻击接口。§4Algorithm1返回E*，nearest-token仅报告；双judge非truth；Ch72内部state/softprompt与文本可达性已分账，不把白盒效果推公开API [必要原文位置与直接反证](../_sources/daily-20260429/V3_PEO_24983_BOUNDED_REVIEW.md)。Books：已有覆盖，唯一owner `PLATFORM-SECURITY`（[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [Why Does Reinforcement Learning Generalize? A Feature-Level Mechanistic Study of Post-Training in Large Language Models](https://arxiv.org/html/2604.25011v1)

共同crosscoder坐标与双向干预为RL/SFT泛化比较提供局部因果证据。§3–4/7/AppA/B：效果是条件答对/答错分母，监督/rollout/LR不匹配，不能solely归训练范式；Ch33/31已有probe—干预—行为与共存条件 [必要原文位置与直接反证](../_sources/daily-20260429/V3_REOPEN_NOTES.md)。Books：仅报告，唯一owner `TRAIN-GRPO`（[Ch33](../../../../books/part-04-training-system/33-grpo.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [Why Search When You Can Transfer? Amortized Agentic Workflow Design from Structural Priors](https://arxiv.org/html/2604.25012v1)

其它任务搜索轨迹可凝成带版本的结构先验与输出contract，新任务免逐任务搜索但仍要编译/执行验收。拟topology段后两段区分来源搜索资产与目标任务执行事实。 §3.1–3.3、§4.1–4.4/Tables1–5、§5：边际$.004不含来源搜索$112.50，约五任务摊销；Gemma MATH反退58.23→48.35；静态数学/代码任务不支持有不可逆effect的开放Agent。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_TWO_ADMISSION_BOUNDARIES_25012_25072.md)。Books：整合，唯一owner `AGENT-MULTI-AGENT`（[当前章节](../../../../books/part-07-agent/82-multi-agent.md)），实际两段位于Ch82:179–183；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [DiscreteRTC: Discrete Diffusion Policies are Natural Asynchronous Executors](https://arxiv.org/html/2604.25050v1)

不再另写prefix原则；仅补原生随机mask训练如何使离散policy用已解码prefix补全suffix、近端s项解完可早停、未解码proposal状态可带入下一轮。 §2–4、§5/AppB–D：Flow RTC混合噪声须ΠGDM/VJP correction，仍有效；同backbone但LR/loss/head不同；20次两任务不是安全保证；DynamicPick+50百分点非相对50%；max-confidence可能耗尽8步。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_DISCRETE_RTC_25050_BOUNDED_REVIEW.md)。Books：整合，唯一owner `MULTIMODAL-EMBODIED-VLA`（[当前章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)），实际两段位于Ch26:559–563；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [Beyond Accuracy: Benchmarking Cross-Task Consistency in Unified Multimodal Models](https://arxiv.org/html/2604.25072v1)

同一scene/fact identity同时冻结理解正确、生成正确与agreement，并显式统计两边同错、缺失节点及歧义匹配。拟identity或多模态评价两段，采用测量设计不正面采用覆盖率不清的公式。 §3.2–3.3、§4/Tables2–8、§5：MMaDA raw.630而AW.144；matched coverage14.3–79.3%；F共享facts与Table4 allnodes口径未解不能称完整场景；Hungarian同label无cost拒绝；黑盒相关不能证明AR因果优越。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_TWO_ADMISSION_BOUNDARIES_25012_25072.md)。Books：整合，唯一owner `PLATFORM-EVALUATION-SYSTEM`（[当前章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)），实际两段位于Ch66:207–211；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration](https://arxiv.org/html/2604.25080v1)

KV恢复分token/layer/stage依赖图与整批I/O优先级联动。§3.1–3.3/§4：boundary activations额外身份；半调和/理想1S依假设，longest remaining heuristic非全局最优；root实际写后PASS Ch45:1384–1388 [必要原文位置与直接反证](../_sources/daily-20260429/V3_REOPEN_NOTES.md)。Books：整合，唯一owner `INFER-KV-CACHE`（[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)）；仅上述机制与限定边界已实际落正文，独立写后记录见§6。

### [Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling](https://arxiv.org/html/2604.25098v1)

删整层与小比例权重mask对多thinking预算的退化不同。具体粒度/模型/预算对照保反退；参数稀疏未量实际加速；Ch28质量门与真正sparse kernel成本门已分账，不据局部曲线另写 [必要原文位置与直接反证](../_sources/daily-20260429/V3_PRUNING_TTS_25098_BOUNDED_REVIEW.md)。Books：仅报告，唯一owner `TRAIN-PRETRAINING`（[Ch28](../../../../books/part-04-training-system/28-pretraining.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [One Perturbation, Two Failure Modes: Probing VLM Safety via Embedding-Guided Typographic Perturbations](https://arxiv.org/html/2604.25102v1)

低ASR可能来自模型读不懂退化字形，不能直接称安全拒绝。 §2–4：50个条件选择样本非自然分母；GPT/Claude baseline0存在selection；embedding关联不是prompt因果；输出judge不是独立OCR；保可信输入快路径与解析不确定隔离。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_TYPO_VLM_25102_BOUNDED_REVIEW.md)。Books：整合，唯一owner `PLATFORM-SECURITY`（[当前章节](../../../../books/part-06-ai-infrastructure/72-security.md)），实际两段位于Ch72:1053–1057；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [Structured Security Auditing and Robustness Enhancement for Untrusted Agent Skills](https://arxiv.org/html/2604.25109v1)

多文件skill预加载审计的risk flagged与malicious recall必须分开。§3–8/AppG/I：581sample的重叠视图、截断读取/已知rewrites/开发切片限制；Ch72跨说明脚本source-sink facts与runtime effect授权、Ch84 catalog admission已有 [必要原文位置与直接反证](../_sources/daily-20260429/V3_REOPEN_NOTES.md)。Books：已有覆盖，唯一owner `PLATFORM-SECURITY`（[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [Evaluation without Generation: Non-Generative Assessment of Harmful Model Specialization with Applications to CSAM](https://arxiv.org/html/2604.25119v1)

输出不宜生成时，可用绑定base/adapter/probe/layer/time/label/threshold的无输出内部功能探针作分发前受限证据；直接训练类别与危险生成能力分账。 §2–5、§7：仍需扩散前向，非零成本；高危样本18/34/74、FLUX4探针；rescale鲁棒非自适应鲁棒；陰性不自动放行，政策authority/人工隔离独立；允许合规行为采样时旧路径继续。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_EWG_25119_BOUNDED_REVIEW.md)。Books：整合，唯一owner `PLATFORM-EVALUATION-SYSTEM`（[当前章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)），实际两段位于Ch66:194–198；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [What Makes Good Instruction-Tuning Data? An In-Context Learning Perspective](https://arxiv.org/html/2604.25132v1)

样本自身难度与one-shot邻域帮助不是同一数据选择proxy。§6.1Table3正Spearman与摘要负相关冲突只隔离方向；16forward/sample非wallclock；Ch27 proxy→heldout选择合同已有 [必要原文位置与直接反证](../_sources/daily-20260429/V3_WICI_25132_BOUNDED_REVIEW.md)。Books：仅报告，唯一owner `TRAIN-DATA`（[Ch27](../../../../books/part-04-training-system/27-data.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [Training Transformers as a Universal Computer](https://arxiv.org/html/2604.25166v1)

有限操作语义模板与稀有stack plan采样让局部解释规则可训练；外部call/ret帧清理使在线上下文按活跃空间而非累计轨迹。 §2.1–2.3、§3.1/3.3/Tables1–2、§5：100%是token-level，不是自治full-run；36bit/216SAT程序、context内打印行、有限primitive；语言完备不证明有限模型任意程序可靠；PENCIL是外部scaffold非新架构。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_MICROPY_25166_BOUNDED_REVIEW.md)。Books：整合，唯一owner `MODEL-DECODER-ONLY`（[当前章节](../../../../books/part-02-model/18-decoder-only.md)），实际两段位于Ch18:282–286；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [AgentDID: Trustless Identity Authentication for AI Agents](https://arxiv.org/html/2604.25189v1)

去中心化身份凭证不替代effect-time context与实际权限。印刷context自证明边界已root有限PASS；Ch72既有issuer/proof/context/authorization分权实际论点不新增，原中央强句不正面采用 [必要原文位置与直接反证](../_sources/daily-20260429/V3_AGENTDID_PRINTED_STATE_GUARANTEE.md)。Books：已有覆盖，唯一owner `PLATFORM-SECURITY`（[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [BARRED: Synthetic Training of Custom Policy Guardrails via Asymmetric Debate](https://arxiv.org/html/2604.25203v1)

定制policy边界生成与标签核验通过直接消融分开。§3Algorithm1/Table4人工.85对未验.58与selfrefine.53支持有限标签有效性；同GPT5mini双judge非truth，两条筛后rules/单GAIA错误限制；Ch27/72已有label admission不靠成熟组合拒真反例 [必要原文位置与直接反证](../_sources/daily-20260429/V3_THREE_GUARDRAIL_SPLIT_ADMISSION.md)。Books：仅报告，唯一owner `TRAIN-DATA`（[Ch27](../../../../books/part-04-training-system/27-data.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [When the Forger Is the Judge: GPT-Image-2 Cannot Recognize Its Own Faked Documents](https://arxiv.org/html/2604.25213v1)

局部生成文档编辑使传统splice取证检测退化并暴露自审盲点。两个校准集不能单因果更换generator；.532是balanced accuracy，6.8%ambiguous不漏分母；Ch66 detector/referencedistribution/FPFN/judgeauthority已承载 [必要原文位置与直接反证](../_sources/daily-20260429/V3_FORGER_JUDGE_25213_BOUNDED_REVIEW.md)。Books：已有覆盖，唯一owner `PLATFORM-EVALUATION-SYSTEM`（[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [VLM Judges Can Rank but Cannot Score: Task-Dependent Uncertainty in Multimodal Evaluation](https://arxiv.org/html/2604.25235v1)

视觉judge排序与绝对score区间可用性按任务分账。印刷finite-sample guarantee与boundary-adjustment98%coverage构造冲突；任务残差/边界截断不能无条件保覆盖；需正确分位数/独立校准与原残差数据再开，不Books保证 [必要原文位置与直接反证](../_sources/daily-20260429/V3_VLM_JUDGE_25235_BOUNDED_REVIEW.md)。Books：暂缓，唯一owner `PLATFORM-EVALUATION-SYSTEM`（[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)）；中央争议不作正面依据、不新增书稿，保留局部观察；精确重开材料见§5及单篇笔记。

### [Below-Chance Blindness: Prompted Underperformance in Small LLMs Produces Positional Bias Rather than Answer Avoidance](https://arxiv.org/html/2604.25249v1)

below-chance未命中不能排除能力压低，选项位置偏差另验。§2–4预注册0/12cells、探索C3不是H1成功；未随机重排不识别内部策略；Ch66 ObservedCapability/ElicitationCeiling及permutation×accuracy/PositionBias已有 [必要原文位置与直接反证](../_sources/daily-20260429/V3_BCB_25249_BOUNDED_REVIEW.md)。Books：已有覆盖，唯一owner `PLATFORM-EVALUATION-SYSTEM`（[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [QFlash: Bridging Quantization and Memory Efficiency in Vision Transformer Attention](https://arxiv.org/html/2604.25306v1)

整数online-softmax必须共同定义跨tile rowmax比较单位、累加/scale-release、整数指数近似与scale生成/重标定成本，不只是QK/PV换dtype。 §3.1–3.3、§4/Algorithm1、§5/Tables1–5、AppB.1–B.3：单RTX5090仅视觉attention七shape；余层float；SQNR低于mixed，Swin-T80.06<FP3281.35；对I-ViT倍率非FA2；无普适误差或ServingSLO；回退FP16/mixed。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_QFLASH_25306_BOUNDED_REVIEW.md)。Books：整合，唯一owner `INFER-TENSORRT-LLM`（[当前章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)），实际两段位于Ch49:1026–1030；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [FusionCIM: Accelerating LLM Inference with Fusion-Driven Computing-in-Memory Architecture](https://arxiv.org/html/2604.25317v1)

不另写diagonal rowmax；仅CIM write昂贵时KV-stationary vs Q/O-stationary改变多query重载/转置/partial sum，KV stream与FP16SFU共同定价。 §III、§IV/TableI–II/Fig6–9：28nm模拟/综合非硅片；SFUFP16非全INT8；29.4sys和P3ViT23.2macro不能公平比较；无任务质量消融；保KV-stationary/GPU容量与质量fallback。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_FUSIONCIM_25317_BOUNDED_REVIEW.md)。Books：整合，唯一owner `INFER-TENSORRT-LLM`（[当前章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)），实际两段位于Ch49:756–760；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [Benchmarking and Improving GUI Agents in High-Dynamic Environments](https://arxiv.org/html/2604.25380v1)

动作间漏观测单独成为高动态GUI EvalSpec轴。exactv1 §3–5；DP-only17.4%与完整22.1%不同，Table6归因混淆隔离；root prewrite+apr02独立真实写后PASS Ch66动作间观测盲区段 [必要原文位置与直接反证](../_sources/daily-20260429/V3_DYNAMIC_GUI_25380_BOUNDED_REVIEW.md)。Books：整合，唯一owner `PLATFORM-EVALUATION-SYSTEM`（[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)）；仅上述机制与限定边界已实际落正文，独立写后记录见§6。

### [Biased Dreams: Limitations to Epistemic Uncertainty Quantification in Latent Dynamics Models](https://arxiv.org/html/2604.25416v1)

latent attractor会让ensemble一步分歧降低但同动作/horizon下物理误差或奖励乐观增长；uncertainty必须按rollout horizon对真实outcome校准，低分歧不是低错误。 §2、§4–6：4DMC/5seed/1Mstep/50rollout；物理decoder也是proxy，HalfCheetah不同协议不唯一归因attractor；不声称已验证通用repair，回退短rollout/真实刷新/独立结果。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_BIASED_DREAMS_25416_BOUNDED_REVIEW.md)。Books：整合，唯一owner `MULTIMODAL-WORLD-MODELS`（[当前章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)），实际两段位于Ch25:273–277；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [JURY-RL: Votes Propose, Proofs Dispose for Label-Free RLVR](https://arxiv.org/html/2604.25419v1)

plurality提案、Lean proof奖励与拒证residual探索必须分责。AppA.2 dissent仍cα²>0反驳整链只奖已证，G.5 verifier precision约85%不否定Lean kernel；formalization/GT额外成本；无零假阳性保证，暂缓新机制 [必要原文位置与直接反证](../_sources/daily-20260429/V3_JURY_RL_25419_BOUNDED_REVIEW.md)。Books：暂缓，唯一owner `TRAIN-GRPO`（[Ch33](../../../../books/part-04-training-system/33-grpo.md)）；中央争议不作正面依据、不新增书稿，保留局部观察；精确重开材料见§5及单篇笔记。

### [FED-FSTQ: Fisher-Guided Token Quantization for Communication-Efficient Federated Fine-Tuning of LLMs on Edge Devices](https://arxiv.org/html/2604.25421v1)

Fisher-guided token压缩需计codec/端侧资源/目标质量总成本。中央153.6MB/55.2s/98.5J与2GB全模型口径印刷矛盾见笔记；保TableVII局部quality，不Books绝对量；需同协议字节/算时/能耗/资源分账 [必要原文位置与直接反证](../_sources/daily-20260429/V3_FEDFSTQ_25421_BOUNDED_REVIEW.md)。Books：暂缓，唯一owner `TRAIN-DISTRIBUTED-TRAINING`（[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)）；中央争议不作正面依据、不新增书稿，保留局部观察；精确重开材料见§5及单篇笔记。

### [The Forensic Cost of Watermark Removal: From Dedicated Attacks to Image Editing](https://arxiv.org/html/2604.25491v1)

水印移除ASR、图像质量和独立移除痕迹TPR@FPR为三轴；第三轴正例只能触发triage，不证明来源/权属/恶意。 §3–6/Tables2–4：seen attacks与orig-ID70/10/20；TPR@1e−3:DiffPure约.25 WMForger约.8，未见DiffPure约.133；百万件约1000FP不能自动处罚；unknown/adaptive保inconclusive和凭证复核。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_WATERMARK_REMOVAL_25491_BOUNDED_REVIEW.md)。Books：整合，唯一owner `PLATFORM-SECURITY`（[当前章节](../../../../books/part-06-ai-infrastructure/72-security.md)），实际两段位于Ch72:905–909；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [Walking Through Uncertainty: An Empirical Study of Uncertainty Estimation for Audio-Aware Large Language Models](https://arxiv.org/html/2604.25591v1)

音频不确定性sensor在正常与不可答任务的排名反转。§III–V/VIII三模型K10/受约束答案/.25router；AUROC/AURAC非部署阈值，MMAR有退步；Ch66 calibration slice已可承载，无新通用sensor [必要原文位置与直接反证](../_sources/daily-20260429/V3_AUDIO_UNCERTAINTY_25591_BOUNDED_REVIEW.md)。Books：仅报告，唯一owner `PLATFORM-EVALUATION-SYSTEM`（[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [Refinement via Regeneration: Enlarging Modification Space Boosts Image Refinement in Unified Multimodal Models](https://arxiv.org/html/2604.25636v1)

保留精确像素资产的edit与保留语义意图的regen是两种contract；后者可只消费initial视觉语义与prompt，不带原VAE像素，训练也须匹配重生而非edit目标。 §3–4.1、Tables1–2：删VAE不保证identity；Table2有限DPGBench对比支持分支非所有编辑优越；100k/60k/1k数据16H80015kstep+50采样不是免费；需资产保持时回退edit。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_REOPEN_NOTES.md)。Books：整合，唯一owner `MULTIMODAL-GENERATIVE-PARADIGMS`（[当前章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)），实际两段位于Ch24:1210–1214；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [NVLLM: A 3D NAND-Centric Architecture Enabling Edge on-Device LLM Inference](https://arxiv.org/html/2604.25699v1)

FFN权重留NANDcompute而attention/KV留LPDDR，error快检/慢纠正用scoreboard补缺segment MAC后才可提交；权重放置、错误authority与剩余KV瓶颈一起预算。 §3–4：模拟3D-FPIM/Ramulator2/C++/28nm synthesis，OPT1.3–30BINT8/RBER非实机；37.9×A800 out-of-coreSSD非同容量HBMGPU；5.63×只movement energy；保DRAM/数字/ECC fallback。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_NVLLM_25699_BOUNDED_REVIEW.md)。Books：整合，唯一owner `INFER-GPU-MEMORY`（[当前章节](../../../../books/part-05-inference-system/54-gpu-memory.md)），实际两段位于Ch54:528–532；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [Step-Audio-R1.5 Technical Report](https://arxiv.org/html/2604.25719v1)

音频输入—文本回答的分数不能签发输出韵律/沉浸改善。§2纯文本输出，§3.3阶段无matched消融，§4S2T表SpokenMQA反退；声学headline未测单独隔离；既有Ch31奖励proxy/Ch24输出模态/Ch66构念分账不增机制 [必要原文位置与直接反证](../_sources/daily-20260429/V3_REOPEN_NOTES.md)。Books：仅报告，唯一owner `TRAIN-RLHF`（[Ch31](../../../../books/part-04-training-system/31-rlhf.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [Scalable Inference Architectures for Compound AI Systems: A Production Deployment Study](https://arxiv.org/html/2604.25724v1)

复合workflow的model-specific arrival/readiness与冷启依赖影响端到端关键路径 exact-v1 §3.2、4.2.2、4.4–4.5把入口触发下游并行预热、关键模型常驻/非关键scale0连到graph-dependent冷启路径。180=30+150是依赖串行相加而非乘法；65s不能只由并行150s公式推出。生产日志再合成和多工具质量混杂不证明原生产突发率或唯一服务因果，高利用率常驻/反应式路径保留。现Ch56一般placement与Pythia预测未承载该cold readiness接口，实际差额已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_COMPOUND_SERVING_25724.md)。Books：整合，唯一owner `INFER-SCHEDULING`（[当前章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)），实际两段位于Ch56:648–652；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [Toward Scalable Terminal Task Synthesis via Skill Graphs](https://arxiv.org/html/2604.25727v1)

skill graph生成路径与实际scenario-skill轨迹覆盖是不同数据分母。AppD节点82073但最大连通分量118806矛盾；oracle95.7%≠双验92%；需修正图统计/原生成与执行覆盖，不Book正面采未明图保证 [必要原文位置与直接反证](../_sources/daily-20260429/V3_SKILLSYNTH_25727_BOUNDED_REVIEW.md)。Books：暂缓，唯一owner `TRAIN-DATA`（[Ch27](../../../../books/part-04-training-system/27-data.md)）；中央争议不作正面依据、不新增书稿，保留局部观察；精确重开材料见§5及单篇笔记。

### [Barriers to Universal Reasoning With Transformers (And How to Overcome Them)](https://arxiv.org/html/2604.25800v1)

表达可模拟TM≠有限trace可学长度泛化；固定alphabet、位置/计算语言与learner假设决定负结果，可增长signpost/value-change日志又是不同正条件。 §3/Theorems3.4/3.8、AppA.2、§4–5：25M6layer合成30/50训练约2×测试，randomoffset已暴露test位置；S5约1.7×；marker不等无穷新token；理想正证明非现实无界可靠。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_COT_LENGTH_25800_BOUNDED_REVIEW.md)。Books：整合，唯一owner `WORLDVIEW-REPRESENTATION`（[当前章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)），实际两段位于Ch5:80–84；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [Mutual Forcing: Dual-Mode Self-Evolution for Fast Autoregressive Audio-Video Character Generation](https://arxiv.org/html/2604.25819v1)

共享权重Few产历史，Multi在Few历史上学真实当前flow，再stopgrad反教Few区间位移，训练history producer与reference双向耦合，部署Few。 §3.2–3.3、§4/Table2、AppD.2：另有online fake score model不是一个模型零aux成本；Table2同预算SC/DMD混合目标不隔离整个双向loop或全训练成本；4NFE WER/LSE-C有反退；25s非无限视频；保普通teacher/已验证独立蒸馏。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_MUTUAL_FORCING_25819_BOUNDED_REVIEW.md)。Books：整合，唯一owner `MULTIMODAL-GENERATIVE-PARADIGMS`（[当前章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)），实际两段位于Ch24:358–362；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/html/2604.25850v1)

harness演进的修复预测和实际fix/regression集合不等价。§3–4Algorithm1同89task开发，precision/recall33.7/51.4与回归11.8/11.1有限反证；部分仓库退步；Ch84版本化model-harness、独立replay/commitrollback已有 [必要原文位置与直接反证](../_sources/daily-20260429/V3_AHE_25850_BOUNDED_REVIEW.md)。Books：仅报告，唯一owner `AGENT-PLATFORM`（[Ch84](../../../../books/part-07-agent/84-agent-platform.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [SIEVES: Selective Prediction Generalizes through Visual Evidence Scoring](https://arxiv.org/html/2604.25855v1)

黑盒视觉定位/crop回答连贯性补充选择性回答sensor。§3–5/AppA–B：可见定位质量≠答案truth；risk阈值不自动可靠，成本/quality切片与abstain分账；root真实写后PASS Ch66 visual evidence sensor段 [必要原文位置与直接反证](../_sources/daily-20260429/V3_SIEVES_25855_BOUNDED_REVIEW.md)。Books：整合，唯一owner `PLATFORM-EVALUATION-SYSTEM`（[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)）；仅上述机制与限定边界已实际落正文，独立写后记录见§6。

### [Privileged Foresight Distillation: Zero-Cost Future Correction for World Action Models](https://arxiv.org/pdf/2604.25859v1)

同backbone/noise只换future attention mask，teacher真实未来与当前base的action velocity差作为stopgrad residual，adapter部署只读当前frame；区别future-feature表示监督。 官方PDF-v1 pp3–8 §3–5/Tables与mask图：LIBEROObject直接finetune96.70/shuffled96.62/PFD98.10；adapter-only96.6<baseline96.95；训练extra forward未匹配；H100190→192ms推理非全成本零；未来不可部署当观测。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_PFD_25859_BOUNDED_REVIEW.md)。Books：整合，唯一owner `MULTIMODAL-EMBODIED-VLA`（[当前章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)），实际两段位于Ch26:284–288；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [When Errors Can Be Beneficial: A Categorization of Imperfect Rewards for Policy Gradient](https://arxiv.org/html/2604.25872v1)

pairwise RM accuracy不能代替当前policy概率/相对误奖下的真实更新收益。§3–5有限正交linear-softmax定理；HAcc相关弱且另一RM作truthproxy、IFBenchpartialreward正反例；root写后PASS Ch31:460–462 [必要原文位置与直接反证](../_sources/daily-20260429/V3_BENEFICIAL_ERRORS_25872_BOUNDED_REVIEW.md)。Books：整合，唯一owner `TRAIN-RLHF`（[Ch31](../../../../books/part-04-training-system/31-rlhf.md)）；仅上述机制与限定边界已实际落正文，独立写后记录见§6。

### [MarkIt: Training-Free Visual Markers for Precise Video Temporal Grounding](https://arxiv.org/html/2604.25886v1)

query-mask与frame index共同外显但视觉overlay也是有损输入变换。§II–IV maskα.5遮挡使质量反退，主模型trainingfree仍有tagLM/YOLOE/渲染成本；Ch23坐标/时间/groundingproposal身份已承载 [必要原文位置与直接反证](../_sources/daily-20260429/V3_REOPEN_NOTES.md)。Books：仅报告，唯一owner `MULTIMODAL-REPRESENTATION`（[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)）；不为该受限案例造diff，非作者已核必要原文与实际owner，最终处置通过；见§6。

### [Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers](https://arxiv.org/html/2604.25891v1)

冻结checkpoint/干预×训练cue类别×标准/同义/反义/格式×任务矩阵，普通EM零不代签训练条件行为清除。 §2.1–2.3、§3.1、§4.1、§6、AppF.3/F.5/F.7–F.9：GPT4o普通0但marinecue非0；GPT4.1/Pythonstring22.3/31.2受限；onpolicy有时局部0、有时残留，不称全无效；人工SFT非生产RL，filter/judge共同偏差/逐题分母保留。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_CONDITIONAL_MISALIGNMENT_25891_BOUNDED_REVIEW.md)。Books：整合，唯一owner `PLATFORM-EVALUATION-SYSTEM`（[当前章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)），实际两段位于Ch66:343–347；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [Pythia: Exploiting Workflow Predictability for Efficient Agent-Native LLM Serving](https://arxiv.org/html/2604.25899v1)

workflow/session/role低权限身份供cache/priority/replica共同可降级预测。§4.1–4.2/5/7初始trace+控制面不可升authority；经验输出分位数非分布外保证，有效期是工程推断；root预核/真实写后PASS Ch56预测workflow段 [必要原文位置与直接反证](../_sources/daily-20260429/V3_REOPEN_NOTES.md)。Books：整合，唯一owner `INFER-SCHEDULING`（[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)）；仅上述机制与限定边界已实际落正文，独立写后记录见§6。

### [How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum](https://arxiv.org/html/2604.25907v1)

逐例成功边际P^−q改变跨样本目标权重，GARL prior-rollout与PAFT posterior-resample梯度路径不同；不是只补全零group或调LR。 §2–7/Eq11及限制：q0期望成功/q1latent marginal非allteacherforcedSFT；单例连续flow需score norm假设非Adam速度保证；finiteM bias非一致coldstart；0.6B三任务单seed/错误label记忆/GARL peak collapse保留。 实际owner具体缺口已独立核准。 [必要原文位置与直接反证](../_sources/daily-20260429/V3_TSALLIS_25907_BOUNDED_REVIEW.md)。Books：整合，唯一owner `TRAIN-GRPO`（[当前章节](../../../../books/part-04-training-system/33-grpo.md)），实际两段位于Ch33:437–441；apr28非作者已核source→实际差额和写后邻接，受限结论/旧路径保留，见[有限复核](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)。

### [Recursive Multi-Agent Systems](https://arxiv.org/html/2604.25917v1)

冻结backbone的RecLink跨latent环以终局CE更新links，构成受限设计观察；但中央普遍梯度稳定保证未立，不作正面采用，train/deploy depth身份与text/单模型回退仍应保留。§3–6/Theorem4.1、AppA.1–A.2：最大奇异值下界不保证每方向/整环梯度：diag(1,α)反复相乘弱方向α^r衰减；W3=I/Kaiming假设不覆盖训练后异构投影。只报告有限TextMAS比较，不Books正面采用该保证。 apr28已定点复核v1方法/定理与当前Ch82，中央普遍稳定保证不成立，裁为争议隔离而非否定实验/代码。  [必要原文位置与直接反证](../_sources/daily-20260429/V3_RECURSIVE_MAS_25917_BOUNDED_REVIEW.md)。Books：暂缓，唯一owner `AGENT-MULTI-AGENT`（[Ch82](../../../../books/part-07-agent/82-multi-agent.md)）；中央争议不作正面依据、不新增书稿，保留局部观察；精确重开材料见§5及单篇笔记。

### [FlashQLA: CP-/Bwd-Friendly Fused Linear Attention Kernels for GDN](https://github.com/QwenLM/FlashQLA/blob/59849a34dc0baeae5f56012f25f3f5726fc3fabc/README.md)

小batch×heads使全融合欠占用，CP预处理与两段融合共同选择；gate-decay warmup只是有限近似。H200固定ref，FLA0.5/FlashInfer0.6.9/TileLang0.1.8；短shape对FlashInfer有反退，不倒灌SM100/120，不推端到端SLO；root写后PASS Ch49 recurrent执行段。整合；原事件、历史ref、实际diff与反例见[本日机构必要记录](../_sources/daily-20260429/V3_REOPEN_NOTES.md)，root已核采用范围。机构发布时间分别取官方article ISO字段/release published_at/PR merged_at；PR创建不代签修复发布，版本累计背景不另计家族。

### [Kimi CLI 1.40.0](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.40.0)

审批presence与autoapproval正交，等待policy与turn/source清理不等用户拒绝。2087与2045实际实现必要核；无限等待不保服务liveness，手测四情形未完成不称全验证；2003前窗背景；root写后PASS Ch84 Human/Workspace交接。整合；原事件、历史ref、实际diff与反例见[本日机构必要记录](../_sources/daily-20260429/V3_REOPEN_NOTES.md)，root已核采用范围。机构发布时间分别取官方article ISO字段/release published_at/PR merged_at；PR创建不代签修复发布，版本累计背景不另计家族。

### [VeOmni #697: Fix vision dummy forward under sequence parallelism](https://github.com/ByteDance-Seed/VeOmni/pull/697)

空模态rank参加collective的dummy路径必须与真实输入保持local tensor/metadata layout parity。files历史patch切pixel_values但保full grid_thw，不能两边重复slice；作者test非我方GPU/NPU复现；root写后PASS Ch40 SP/CP边界。整合；原事件、历史ref、实际diff与反例见[本日机构必要记录](../_sources/daily-20260429/V3_REOPEN_NOTES.md)，root已核采用范围。机构发布时间分别取官方article ISO字段/release published_at/PR merged_at；PR创建不代签修复发布，版本累计背景不另计家族。

### [FastDeploy #7655: multimodal routing buffer bound](https://github.com/PaddlePaddle/FastDeploy/pull/7655)

scheduler文本token上界不等multimodal内部routing激活上界，workspace sizing改读max_chunk_tokens。release2.6 PR受限版本事实、空增长条件改变；无accuracy tests/全路径范围，root认可Standard受限Only，不强写长期机制。仅报告；原事件、历史ref、实际diff与反例见[本日机构必要记录](../_sources/daily-20260429/V3_REOPEN_NOTES.md)，root已核采用范围。机构发布时间分别取官方article ISO字段/release published_at/PR merged_at；PR创建不代签修复发布，版本累计背景不另计家族。

## 5. 缺口与下一步

普通可执行工作：0。全部63候选的证据与Books处置、32整合的实际写后及日级独立汇总已通过。以下仅为本窗终态保留项与窗外恢复线索，不支持正面证据、Books或全网“无遗漏”断言；取得明确所列新材料时只重开受影响项。共享索引与LEARNING_STATE归root，本作者未改。

本窗终态保留项（外部/日期限制）（不支持候选正面证据、Books或“无遗漏”）：

- 首公开历史不可裁的6家族：2604.24832、25183、25326、25555、25642、25783。必要论文/会议/作者历史repo已定点尝试，早期同题机制存在但当时public不可恢复；只要取得当时公开archive/平台日志、文章全文开放时刻或官方发布记录，按各单篇末尾定点重开，不遍历全Git/会议。
- Seed27505（Image Editing verifier RL）：CMS仅Apr28/29粗日期、arxiv提交在截止后，不能凭目录日标签归09:00前；需文章级明确公开时刻/首发archive才能重开。
- 官方历史子目录：Anthropic SeeMore、Google2026 Publications互动filter、Meta页2混排、Moonshot2026 blog、MiMo blog日期、DeepSeek查看全部及Hunyuan其它语言历史均未恢复；已有有界邻接与具名补检不代表其全历史零。仅出现具体本窗文章/分页archive时恢复受影响源段，不借限制扩整月/全年。

中央争议采用边界：24806 immutable snapshot重建、24809谱L2精确检索、24894无条件视觉硬安全、24927逐步最优、24957统一算子梯度安全近似、24971packed bytes/concurrent peak、25235有限样本区间/边界调整、25419整链只奖已证/零假阳性、25421绝对算时/能量/2GB资源、25727图统计与覆盖、25917整环梯度稳定。各项可保局部受限观察但不采争议保证；必要修正公式/假设、明确representation/allocated bytes/同时存活trace或原校准/图数据等最小重开材料，已在相应§4笔记逐项列出。25189印刷context保证已root有限隔离，既有授权正文No Change，不增新的正面证明。

窗外恢复线索：24801作者完整PDF04/27早发、24890公共研究摘要02/15、25779同作者项目03/11核心实验；OpenAI goblins04/30 04BJT、ZAI ScalingPain04/29 16BJT、Hunyuan100039 Apr30 public、RDMesh Apr29 07:36Z。只交真实归属日，不扩本窗，不阻本日安全终态。

## 6. 复核

复核者：apr28_close（04/28作者，非本日作者）；root先行有限源/准入与写后结论按未变身份、版本、命题复用。

结论：通过

见[本日唯一最终独立记录](../_sources/daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md)页末最终Gate。

独立范围为全部63家族的身份、评分/实际审阅深度、必要证据和反证、唯一actual owner与Books终裁：32整合（既有/root12 + apr28新授20）均具名真实正文与相邻写后通过；9已有覆盖、11仅报告、11中央争议暂缓全部终态。25724恢复真实cold-readiness差额，ViPO纠正为Ch34的局部loss条件反例；不因备好提案、已有章节主题或旧完成标签自动通过。32处具体采用与写后边界见上述独立记录、[root三项](../_sources/daily-20260429/V3_ROOT_THREE_OWNER_REVIEW.md)及§4。

来源十四行与表外触发的实际范围/停止点、arXiv有据08–09批次推断、6日期例外、Seed27505及历史源限制均已核；不以submitted/DOI单字段签首公开，不把1286宽库存变队列。排除侧独立具名范围32/38：17项必要原版/实际owner、root4项有效复用、11项完整题摘与有界原记录分层抽核。余6不称逐项必要正文审阅，25110无法回取的原版不冒称全文已读；未发现共同错误理由或未处理普通项。具体样本及限制详见独立记录，有限抽核不证明全网或全集无遗漏。

普通待核/待写/待写后为0，Structural Candidate为0。外部保留和中央争议仅按§5具名边界隔离，不被Gate转成证据成立、生产SLO或真实安全保证；未复现实验。

机器检查：完成状态的正式V3报告validate_research通过，限定Books/Report/_sources的git diff --check通过，本地引用目标均存在；机器结果只验可判定结构，不替代上述非作者语义验收。既有staged/dirty修改保留，本作者未stage、commit、push，未写共享索引或LEARNING_STATE。
