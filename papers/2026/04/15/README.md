# Daily Research — 2026-04-15

**规范：** V3
**窗口：** 2026-04-14T09:00:00+08:00 ～ 2026-04-15T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-27T11:59:07+08:00

## 1. 结论

本日重审独立于旧 Weekly。546个arXiv库存身份只作宽范围查漏，已实际浏览546个标题并阅读240个完整题摘；这些不代表546篇本窗新论文或240个贡献候选。当前有据归属且通过贡献筛选的唯一家族冻结为123项，逐项已取得安全终态。其余具体贡献关闭、撤回排除及日期不确定项不混入该分母；覆盖受限处见§2/§5，本报告不宣称零遗漏。

主要整合链包括：Ch31弱到强训练的噪声通道与强模型prior；Ch17无归一化初始化的尺度、导数与残差约束；Ch77记忆程序联合搜索的离线/在线成本；Ch28辅助future-token监督。Ch66补齐视觉选择与执行路径的校准身份、过程/结果同接受子集、shared confidence函数及关系任务的评价分账；Ch23/24补齐直接patch监督、音频target支持与局部纠偏训练分支。Ch45/52/49承载query条件缓存、livePP提交及vector-bottleneck数值验收；Ch33/5承载特权反馈蒸馏与任务身份取回/统计估计竞争；Ch72保留受限威胁与来源边界。22项实际正文和相邻交接均经非作者写后核验，具体论证与位置见§3/§4；中心公式/评价争议没有作为正面书稿保证。

最终123项为22真实整合、5具体已有覆盖、78仅报告、17争议隔离、1必要正文受阻隔离；41项深入完成、64项标准完成，后18项不计证据通过。22项已落实正文并经非作者写后复核，5项已有覆盖也已对读真实命题；没有未处理的普通筛选、证据或 Books 工作。整日独立复核通过，§5保留项不提供正面证据或书稿保证。

实际题摘、方法/评价位置见[本日checkpoint](../_sources/daily-20260415/V3_REVIEW_CHECKPOINT.md)、[筛选依据](../_sources/daily-20260415/V3_SCREENING_NOTES.md)与[必要证据](../_sources/daily-20260415/V3_EVIDENCE_REVIEW.md)。旧格式与旧判断完整保存在[此前日报](../_sources/daily-20260415/V2_1_README_BEFORE_V3.md)，不作为当前完成证明。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方Research/index首屏至08-18的Load more；完整News RSS邻域04-14T00Z→04-15T10Z均窗外 | 受阻 | RSS不能替代Research历史分页；本窗研究目录尚无可核停点 |
| SRC-ANTHROPIC | Research HTML原publishedOn邻域04-09→04-14T13:01Z→04-22；进入AAR技术正文§1–7 | 已检查 | 1个确定本窗家族；不可据作者有限结果推生产保证 |
| SRC-GOOGLE-AI | Research April月9项04-13→04-16；DeepMind Blog实际page3跨April→March；Robotics-ER1.6原datePublished04-14T16Z，FlashTTS04-15T15Z窗外 | 受阻 | 已审1个本窗发布家族为仅报告；Blog检查不冒称Publications年358项的日级停点，后者终态精确隔离 |
| SRC-META-AI | Research提取空后恢复官方Blog p1/p2；p1含04-08/04-06后，p2到03-27但目录混排；Publications入口呈2016–2020旧记录 | 受阻 | 不能以混排两页或旧出版列表证明当窗研究完整；需可复查历史分页/窗口列表 |
| SRC-QWEN | 官方Research静态60+动态40条，04-02T04+08→04-15T10+08；组织created-desc58仓库至2023，Qwen3.6重要release目录实际空 | 已检查 | 仅证明这些官方可见入口；截点后Qwen3.6不移入本窗 |
| SRC-DEEPSEEK | 官网news16条04-24→2025-12-01；组织新仓库39条至2023 | 已检查 | 无本窗可见条目，不外推所有未列作者论文 |
| SRC-MOONSHOT | Kimi Blog26条最晚2025-11-07；组织43新仓库至2023；K2.5 release空 | 受阻 | 仓库无本窗新项，但Blog旧目录不能证明2026研究停点 |
| SRC-TENCENT-HUNYUAN | 官方publicList POST page1/size100/render0，total9/list9；displayPublishTime04-30/23→02-13；组织83仓库 | 已检查 | 公开全部目录无本窗项，不声称未列作者论文无更新 |
| SRC-ZAI | Research16项04-29→04-07→04-01；release notes06-16→04-07→02-12；组织53仓库 | 已检查 | 这些公开入口无本窗项；猜测仓库404不当无release证明 |
| SRC-BYTEDANCE-SEED | 官方API type1 page20 total242/next40，05-13→04-09越左界；type2 page0/20 total95，04-23→04-09→04-01；Seedance2 launch为02-12 | 受阻 | 确定性目录停点已核；Seedance2 paper卡PublishDate04-15零点但后期更新，正文/arXiv晚于截点，原始卡片公开时刻/同版本正文形成精确终态隔离，不以日期桶或后发正文当早发证据 |
| SRC-BAIDU-ERNIE | Blog首页10条04-30→04-15ERNIE-Image→02-06；官方App-BsX3z_jp.js的392613B发布正文与作者HF两model card已实际恢复；ERNIE release1条为2025-06 | 受阻 | 正文已可读，剩余缺口是原始公开时刻/09:00归属；HF创建/commit接口有界补核未取得，不以日期桶造时刻 |
| SRC-XIAOMI-MIMO | Paper8条06-29→03-13→02-03；组织18仓库与V2Flash release空；Blog14条无date | 受阻 | Paper/新仓库无本窗项，但Blog缺历史日期，不能声称全源无更新 |
| SRC-MINIMAX | en Blog12项05-26→03-18，cn13项04-27→03-18；组织35仓库、M2.7 release空；AgentTechBlog空/llms.txt48 routes无日期 | 受阻 | 两语言可见Blog无本窗项；AgentTechBlog历史日级材料不可核 |
| SRC-ARXIV | 546身份库存标题查漏、240完整题摘；官方OAI/相邻批次/永久ID公告规则与v1更新上界组合，详见checkpoint | 已检查 | 贡献分母已冻结；跨截点97身份中的潜在贡献已逐项关闭或日期隔离，仍缺公开上界者为终态保留项，不用DOI-created或submitted孤证定归属 |

检查结果限定实际入口与本窗。来源受阻项已执行上述有界原始入口及替代恢复，剩余是需官方历史目录、精确事件或同版本材料的终态隔离；不能把这些行计作已证明的完整覆盖，亦不重复同样失败入口。

## 3. 候选与判断

以下arXiv公开区间为官方组合支持的有据推断，不把Submitted/Updated改名为公告时刻；原字段及例外见checkpoint。分数针对具体采用命题，不针对论文全部宣传。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Automated Alignment Researchers](https://alignment.anthropic.com/2026/automated-w2s-researcher/) | 2026-04-14T13:01:00+00:00 | 输入相关弱标签噪声通道与强prior联合重估，须区分soft监督/真值；2+2+2=6 | 深入完成 | 整合 `TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md)，真实噪声通道分支与fallback |
| [Subcritical Signal Propagation at Initialization in Normalization-Free Transformers](https://arxiv.org/html/2604.11890v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | saturation输入scale/导数×残差初始化，非所有奇异值稳定；2+1+3=6 | 深入完成 | 整合 `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md)，实际已写，写后非作者复核通过 |
| [M*: Discovering Task-Optimized Memory Harnesses for LLM Agents](https://arxiv.org/html/2604.11811v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | schema/读写/workflow联合设计、离线搜索与在线调用分账；2+2+2=6 | 深入完成 | 整合 `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)，实际已写，写后非作者复核通过 |
| [How Transformers Learn to Plan via Multi-Token Prediction](https://arxiv.org/html/2604.11912v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 浅future-token loss绕过未训练深层，改变受限模型的梯度可达路径；2+1+3=6 | 深入完成 | 整合 `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，已实际写入NTP主线并经root写后复核 |
| [Filtered Reasoning Score: Evaluating Reasoning Quality on a Model's Most-Confident Traces](https://arxiv.org/html/2604.11996v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 同一selector/coverage的接受子集须分账过程与结果质量，pooled top%不是线上每题oracle；2+2+2=6 | 深入完成 | 整合 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，实际正文写后非作者通过（apr02） |
| [When Does Visual Token Pruning Improve Calibration? The Role of Evidence Coverage in MLLMs](https://arxiv.org/html/2604.12035v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 视觉kept-set、selector与执行路径改变校准身份，质量与confidence须联合验收；2+2+2=6 | 深入完成 | 整合 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，实际正文写后非作者通过（apr02） |
| [Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration](https://arxiv.org/html/2604.12046v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | claim/confidence分阶段loss不冻结共享函数，factual优化后须重校准并检查最终claim保持；2+2+2=6 | 深入完成 | 整合 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，实际正文写后非作者通过（apr02） |
| [TIPSv2: Advancing Vision-Language Pretraining with Enhanced Patch-Text Alignment](https://arxiv.org/html/2604.12012v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | masked输入view与直接监督patch范围分开，head-only EMA依外部稳定信号；2+2+2=6 | 深入完成 | 整合 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，真实正文写后非作者通过（root） |
| [LoSA: Locality Aware Sparse Attention for Block-Wise Diffusion Language Models](https://arxiv.org/html/2604.12056v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 固定prefix不保证query条件attention输出不变，派生output/LSE缓存与物理union分别验；2+2+2=6 | 深入完成 | 整合 `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，真实正文写后非作者通过（root） |
| [Beyond Perception Errors: Semantic Fixation in Large Vision-Language Models](https://arxiv.org/html/2604.12119v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 同pixels×规则×alias语义配对分离解释映射与视觉输入，非全部感知正确保证；2+2+2=6 | 深入完成 | 整合 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，真实正文写后非作者通过（root） |
| [PipeLive: Efficient Live In-place Pipeline Parallelism Reconfiguration for Dynamic LLM Serving](https://arxiv.org/pdf/2604.12171v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | current∪target临时权重/KV预算、增量patch与最终同步提交形成重配执行链；2+2+2=6 | 深入完成 | 整合 `INFER-DYNAMO` [Ch52](../../../../books/part-05-inference-system/52-dynamo.md)，真实正文写后非作者通过（root） |
| [A Layer-wise Analysis of Supervised Fine-Tuning](https://arxiv.org/html/2604.11838v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | layer-sensitive子空间的受限训练证据，不识别普遍alignment局部化；2+1+2=5 | 标准完成 | 已有覆盖 `TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)，可训练子空间须按预算/能力/安全实际验收 |
| [ProbeLogits: Kernel-Level LLM Inference Primitives for AI-Native Operating Systems](https://arxiv.org/html/2604.11943v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 分类forward与kernel授权是不同权力，结构mediation不证明语义真值；2+2+2=6 | 深入完成 | 已有覆盖 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，Policy-as-Data的sensor→typed decision→deterministic authorization |
| [ResBM: Residual Bottleneck Models for Low-Bandwidth Pipeline Parallelism](https://arxiv.org/html/2604.11947v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 训练结构换PP通信维度，矩形identity保证有直接反例；2+2+2=6 | 争议 | 暂缓：中心保证，§4与证据笔记保留具体反例/受限经验机制 |
| [GRACE: A Dynamic Coreset Selection Framework for Large Language Model Optimization](https://arxiv.org/html/2604.11810v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | score缓存沿kNN选择性重算，但quadratic驻点与Eq21不一致；2+1+2=5 | 争议 | 暂缓：中心公式保证已独立核查并隔离，重开需作者修正归一化目标或驻点公式 |
| [Active Imitation Learning for Thermal- and Kernel-Aware LFM Inference on 3D S-NUCA Many-Cores](https://arxiv.org/html/2604.11948v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | kernel迁移utility与oracle查询预算，模拟热/冷cache边界；2+1+2=5 | 标准完成 | 仅报告：受限3DCPU模拟分支，不改通用GPU调度结论 |
| [The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break](https://arxiv.org/html/2604.11978v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | intrinsic horizon与轨迹分开，但难度/选择混杂未除；2+1+2=5 | 标准完成 | 仅报告：具体construction，不采普遍horizon阈值 |
| [Evaluating Cross-Architecture Performance Modeling of Distributed ML Workloads Using StableHLO](https://arxiv.org/html/2604.12090v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 同IR多fidelity估计，细模型在有限对照也可能更差；2+2+2=6 | 标准完成 | 仅报告：具体实现/反证，模拟不代替实机验收 |
| [Narrative over Numbers: The Identifiable Victim Effect and its Amplification Under Alignment and Reasoning in Large Language Models](https://arxiv.org/html/2604.12076v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | reasoning framing可能改变偏差方向，CoT与规范内容混杂；2+1+2=5 | 标准完成 | 仅报告：受限行为负面证据，不当内部情绪或普遍对齐因果 |
| [The A-R Behavioral Space: Execution-Level Profiling of Tool-Using Language Model Agents in Organizational Deployment](https://arxiv.org/pdf/2604.12116v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | A执行与R拒绝可分离，sandbox/模型identity限定；2+1+2=5 | 标准完成 | 已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，Act/Silent/Stop与committed effects真实论点 |
| [Polynomial Expansion Rank Adaptation: Enhancing Low-Rank Fine-Tuning with High-Order Interactions](https://arxiv.org/html/2604.11841v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 绑因子多项式表达与rank上界，但子集最优误差证明方向缺桥；2+1+2=5 | 争议 | 暂缓：中心表达性保证已定点非作者核AppA.3并隔离，不否定全部有限经验结果 |
| [Disposition Distillation at Small Scale: A Three-Arc Negative Result](https://arxiv.org/html/2604.11867v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | matched judge/长度重测与独立probe失败，修正CV/风格可证明可靠性的判断；2+2+2=6 | 深入完成 | 已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，matched probe、sensor heldout与judge格式偏差 |
| [The Linear Centroids Hypothesis: How Deep Network Features Represent Data](https://arxiv.org/html/2604.11962v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | Jacobian-centroid比较提取/使用的条件几何工具，假设不是真值保证；2+1+2=5 | 标准完成 | 仅报告：工具与受限证据，不称算法已有覆盖或全部特征忠实 |
| [Offline-Online Reinforcement Learning for Linear Mixture MDPs](https://arxiv.org/html/2604.11994v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 已知shift×feature coverage下组合offline-assisted与online回退；2+1+2=5 | 标准完成 | 仅报告：有限MDP条件理论，不采现代LLM regret保证 |
| [Loss-Driven Bayesian Active Learning](https://arxiv.org/html/2604.11995v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | weighted Bregman条件下解析inner Bayes action，myopic与全程最优分开；2+1+2=5 | 标准完成 | 仅报告：预测任务条件分支，不规定LLM数据过滤方式 |
| [When to Forget: A Memory Governance Primitive](https://arxiv.org/html/2604.12007v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 双counter关联成功/证据量在task与共同取回混杂下可反向，不是因果淘汰值；2+1+2=5 | 标准完成 | 仅报告：低成本关联诊断分支，无生产删除保证 |
| [Sample Complexity of Autoregressive Reasoning: Chain-of-Thought vs. End-to-End](https://arxiv.org/html/2604.12013v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 有限VC/完整链标签的PAC样本T独立，标签量和优化成本不独立；2+1+2=5 | 标准完成 | 仅报告：条件监督理论，不采现代Transformer全程保证 |
| [UCS: Estimating Unseen Coverage for Improved In-Context Learning](https://arxiv.org/html/2604.12015v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | model-consistent簇与SGT频谱构造subset prior，覆盖非正确概率；2+1+2=5 | 标准完成 | 仅报告：具体selection估计器与反收益边界，非默认全任务方案 |
| [Benchmarking Deflection and Hallucination in Large Vision-Language Models](https://arxiv.org/html/2604.12033v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | gating模型依赖curation与四knowledge条件，题库更换不等可比；2+1+2=5 | 标准完成 | 仅报告：具体过滤程序，不能证明模型绝无参数知识 |
| [SIR-Bench: Evaluating Investigation Depth in Security Incident Response Agents](https://arxiv.org/html/2604.12040v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | alert与新证据分账，但同分母Hit3/Hit5比例违背嵌套事件；2+1+2=5 | 争议 | 暂缓：调查深度比例须作者修正分母/原始计数，不据此否定全部案例 |
| [VISTA: Validation-Informed Trajectory Adaptation via Self-Distillation](https://arxiv.org/html/2604.12044v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | validation边际覆盖加权历史checkpoint，正阈值剪枝近似且需独立测试；2+1+2=5 | 标准完成 | 仅报告：具体训练轨迹算法，不推各子群保持或全部预算公平 |
| [Can we Watermark Low-Entropy LLM Outputs?](https://arxiv.org/html/2604.12051v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 双采样/hash/PRC构造放宽熵要求，随机错误不等任意改写；2+1+2=5 | 深入完成 | 仅报告：条件密码学构造，不称已验全部定理或生产检测保证 |
| [LLM-Redactor: An Empirical Evaluation of Eight Techniques for Privacy-Preserving LLM Requests](https://arxiv.org/html/2604.12064v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 云端路由分母与exact/semantic泄漏不同，stub/wire测量不等隐私保证；2+1+2=5 | 深入完成 | 仅报告：受限安全反证，不采用DP/Pareto宣传或完整部署保证 |
| [SOLARIS: Speculative Offloading of Latent-bAsed Representation for Inference Scaling](https://arxiv.org/html/2604.12110v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | background FM特征/TTL/miss回退及非精确补全分开；2+2+1=5 | 标准完成 | 仅报告：末端ranking的受限foundation-serving分支，不外推收入/尾SLO |
| [HTDC: Hesitation-Triggered Differential Calibration for Mitigating Hallucination in Large Vision-Language Models](https://arxiv.org/html/2604.12115v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | layer-momentum trigger控制两probe，幻觉下降与召回/检查成本分账；2+1+2=5 | 标准完成 | 仅报告：具体contrastive程序，内部hesitation不是事实概率或生产SLO |
| [Towards Platonic Representation for Table Reasoning: A Foundation for Permutation-Invariant Retrieval](https://arxiv.org/html/2604.12133v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | table cell的CKA置换诊断，内在稳定不等retrieval收益；2+1+2=5 | 标准完成 | 仅报告：prospective/有限几何评价，未有端到端检索保证 |
| [Why Your Tokenizer Fails in Information Fusion: A Timing-Aware Pre-Quantization Fusion for Video-Enhanced Audio Tokenization](https://arxiv.org/html/2604.12145v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | pre-quant与时间窗口融合的受限质量分支，token数与端到端收益分开；2+1+2=5 | 标准完成 | 仅报告：有限AVQA/codec对照，不采用无损或默认统一表示 |
| [From Plan to Action: How Well Do Agents Follow the Plan?](https://arxiv.org/html/2604.12147v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | phase compliance和任务成功可分离，提醒与条件选样有代价；2+1+2=5 | 标准完成 | 仅报告：具体指标/干预反证，不采统一计划提醒规则 |
| [PubSwap: Public-Data Off-Policy Coordination for Federated RLVR](https://arxiv.org/html/2604.12160v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 公共回答交换改变本地reward组支持，平衡方差不等无偏/隐私保证；2+2+2=6 | 标准完成 | 仅报告：具体联邦后训练分支，不定为普遍更优目标 |
| [Nucleus-Image: Sparse MoE for Image Generation](https://arxiv.org/html/2604.12163v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | timestep调制与路由输入分离、容量/粒度条件，未有独立端到端归因；2+2+2=6 | 标准完成 | 仅报告：受限生成配方，不采默认路由或全slice优势 |
| [Policy-Invisible Violations in LLM-Based Agents](https://arxiv.org/html/2604.12177v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | metadata world-state overlay预检，谓词完整性与在线原子effect未证；2+2+2=6 | 深入完成 | 仅报告：受控安全程序，不承诺零误判或任意组织部署 |
| [Knowledge Is Not Static: Order-Aware Hypergraph RAG for Language Models](https://arxiv.org/html/2604.12185v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 规则precedence与learned软transition支持序列检索，非自动因果时间；2+1+2=5 | 标准完成 | 仅报告：具体sequence分支，不要求全部RAG统一采用 |
| [Beyond Majority Voting: Efficient Best-Of-N with Radial Consensus Score](https://arxiv.org/html/2604.12196v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | weighted mean最近candidate与非平方medoid等价主张有反例；2+1+2=5 | 争议 | 暂缓：两种距离目标须作者明确，具体反例见证据，非否定全部程序 |
| [AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning](https://arxiv.org/html/2604.12201v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | retrieval/persuasion两阶段poison与条件ASR分账，但一行乘积/基线预算不一致；2+2+2=6 | 深入完成 | 仅报告：受限威胁协议，不采用该行ASR或独立格式因果 |
| [Beyond Factual Grounding: The Case for Opinion-Aware Retrieval-Augmented Generation](https://arxiv.org/html/2604.12138v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 观点分布/人口属性覆盖与事实相关性目标错位，metadata检索不实现总体分布目标；2+1+2=5 | 标准完成 | 仅报告：受限coverage取舍，不作总体fairness保证 |
| [ViLL-E: Video LLM Embeddings for Retrieval](https://arxiv.org/html/2604.12148v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 自适应生成hidden readout读取pooling K/V，停止/训练混杂与成本须分开；2+2+2=6 | 标准完成 | 仅报告：具体读出设计，不推忠实思考或全部检索更优 |
| [Fully Homomorphic Encryption on Llama 3 model for privacy preserving LLM inference](https://arxiv.org/html/2604.12168v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 部分attention加密与全链保护不同，吞吐Eq7单位不一致；2+2+2=6 | 争议 | 暂缓：计量/明文边界，待作者计时对象和公式澄清 |
| [EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture](https://arxiv.org/html/2604.12167v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | learned idle关联活动触发LLM行动，threshold与N=1不消失；2+1+2=5 | 标准完成 | 仅报告：具体trigger分支，不采用意识或生产可靠性保证 |
| [Representing expertise accelerates learning from pedagogical interaction data](https://arxiv.org/html/2604.12195v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | recovery-state覆盖与source-cue条件化分离，缺cue可使优势消失；2+1+2=5 | 标准完成 | 仅报告：受限数据角色条件实验，不推通用配方 |
| [Structural Anchors and Reasoning Fragility:Understanding CoT Robustness in LLM4Code](https://arxiv.org/html/2604.12214v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | anchor对齐揭示条件反收益，uncertainty弱诊断不等因果；2+1+2=5 | 标准完成 | 仅报告：受限trace/扰动证据，不采用可靠sensor宣传 |
| [Learning Project-wise Subsequent Code Edits via Interleaving Neural-based Induction and Tool-based Deduction](https://arxiv.org/html/2604.12220v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | learned composition invoker分流semantic与LSP syntactic编辑，有限scope/成本；2+1+2=5 | 标准完成 | 仅报告：具体交互编辑分支，不给全repo正确性保证 |
| [TimeMark: A Trustworthy Time Watermarking Framework for Exact Generation-Time Recovery from AIGC](https://arxiv.org/pdf/2604.12216v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | HSM时间key与双段水印有trust split，但非零近似误差不证明100%；2+2+2=6 | 争议 | 暂缓：完美保证，待一致误差/信任假设 |
| [Ride the Wave: Precision-Allocated Sparse Attention for Smooth Video Generation](https://arxiv.org/html/2604.12219v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 校准step预算、随机路由与group统计读取折衷；2+2+2=6 | 标准完成 | 仅报告：具体近似执行分支，不采全维Pareto保证 |
| [SpecBound: Adaptive Bounded Self-Speculation with Layer-wise Confidence Calibration](https://arxiv.org/html/2604.12247v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | ACT与depth/width缓存界，但sampling exact协议/单调理论不充分；2+2+2=6 | 争议 | 暂缓：分布保证与公式边界，受限实现不被反例全盘否定 |
| [SpanKey: Dynamic Key Space Conditioning for Neural Network Access Control](https://arxiv.org/pdf/2604.12254v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | key conditioning可能被absorb，deny loss与secret-B威胁分开；2+1+2=5 | 深入完成 | 仅报告：受限gate与安全反证，非密码学授权保证 |
| [Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision](https://arxiv.org/html/2604.12002v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | outcome-conditioned reviser解锁冻结特权teacher reverse-KL；2+2+2=6 | 深入完成 | 整合 `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)，实际正文写后非作者通过 |
| [Distinct mechanisms underlying in-context learning in transformers](https://arxiv.org/html/2604.12151v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | Context任务取回/统计估计两用途，训练竞合与容量边界；2+1+3=6 | 深入完成 | 整合 `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，实际正文写后非作者通过 |
| [Evaluating Relational Reasoning in LLMs with REL](https://arxiv.org/html/2604.12176v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | input规模、generator arity与operand复杂度是独立评价轴；2+2+2=6 | 深入完成 | 整合 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，实际正文写后非作者通过 |
| [TEMPLATEFUZZ: Fine-Grained Chat Template Fuzzing for Jailbreaking and Red Teaming LLMs](https://arxiv.org/html/2604.12232v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | template元素mutation与权限/utility/误判分账；2+2+2=6 | 深入完成 | 仅报告：有权限改模板与商业prompt仿造不同，不给通用防御保证 |
| [UniRec: Bridging the Expressive Gap between Generative and Discriminative Recommendation via Chain-of-Attribute](https://arxiv.org/html/2604.12234v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | CoA表示分支，但跨item Bayes排序忽略特征边缘概率；2+1+2=5 | 争议 | 暂缓：中心表达性/排序保证，待归一化条件与证明澄清 |
| [Socrates Loss: Unifying Confidence Calibration and Classification by Leveraging the Unknown](https://arxiv.org/html/2604.12245v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | auxiliary-idk与EMA目标统一loss，初期证明不推出全程校准保证；2+1+2=5 | 争议 | 暂缓：中心普遍保证，受限5seed分类经验不被全盘否定 |
| [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation](https://arxiv.org/html/2604.12268v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 接受有效/拒绝无效行为的双轴，对函数和repo呈不同失败方向；2+2+2=6 | 标准完成 | 仅报告：受限可执行spec评价，不推语义完备或与厂商代码分数同预算 |
| [SubFlow: Sub-mode Conditioned Flow Matching for Diverse One-Step Generation](https://arxiv.org/html/2604.12273v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 子簇条件化改变有限one-step质量/多样性取舍；2+1+2=5 | 标准完成 | 仅报告：不采用条件均值必导致mode丢失或完整coverage保证 |
| [Models Know Their Shortcuts: Deployment-Time Shortcut Mitigation](https://arxiv.org/html/2604.12277v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 无原训练集时saliency-masked LoRA适应，最终强度仍需标签；2+1+2=5 | 标准完成 | 仅报告：受限部署适应，不采无监督全链或因果解释 |
| [WebAgentGuard: A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents](https://arxiv.org/html/2604.12284v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 并行observation guard与action gate有critical-path条件，不是免费防御；2+2+2=6 | 深入完成 | 仅报告：具体安全/时延对照，不承诺普遍零增迟或零攻击 |
| [Frontier-Eng: Benchmarking Self-Evolving Agents on Real-World Engineering Tasks with Generative Optimization](https://arxiv.org/html/2604.12290v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 固定评估预算下搜索深宽排序的受限反证；2+1+2=5 | 标准完成 | 仅报告：具体轨迹证据，不把拟合或工业模拟推为通律 |
| [CompliBench: Benchmarking LLM Judges for Compliance Violation Detection in Dialogue Systems](https://arxiv.org/html/2604.12312v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | governing rule识别与violation漏检分离，合成标签需核验；2+1+2=5 | 标准完成 | 仅报告：具体评价协议，非完备合规oracle |
| [Towards Realistic and Consistent Orbital Video Generation via 3D Foundation Priors](https://arxiv.org/html/2604.12309v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 全局shape latent与投影视角latent共享先验，避免mesh抽取但非几何真值；2+1+2=5 | 标准完成 | 仅报告：受限表示条件分支，不作完整world transition或重建保证 |
| [Self-Adversarial One Step Generation via Condition Shifting](https://arxiv.org/html/2604.12322v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | shifted-condition fake-flow拟合代替独立critic接口，代理误差/训练成本仍在；2+2+2=6 | 标准完成 | 仅报告：受限one-step训练分支，不采用普遍KL下降或GAN等价保证 |
| [Information-Geometric Decomposition of Generalization Error in Unsupervised Learning](https://arxiv.org/html/2604.12340v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | e-flat可见分布把KL泛化拆成三项，隐藏边缘化破坏非负偏差解释；2+1+2=5 | 标准完成 | 仅报告：条件性理论与isotropic Gaussian秩裁切，不作Transformer泛化保证 |
| [CoLA: A Choice Leakage Attack Framework to Expose Privacy Risks in Subset Training](https://arxiv.org/html/2604.12342v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | privacy unit从真正训练I扩到参与选择但未训练E，改变数据筛选审计对象；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) Membership 的训练成员/筛选参与者分账；root 源、owner 与实际写后通过 |
| [PrivEraserVerify: Efficient, Private, and Verifiable Federated Unlearning](https://arxiv.org/html/2604.12348v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | checkpoint省略与fingerprint absence不足支持完整client influence删除保证；2+2+2=6 | 争议 | 暂缓：中心隐私/可验证保证缺邻接、敏感度/accountant及fingerprint→全部影响的证明，明确隔离 |
| [Why and When Visual Token Pruning Fails? A Study on Relevant Visual Information Shift in MLLMs Decoding](https://arxiv.org/html/2604.12358v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 静态prefill选择不能假定decode证据需求不变，备份token与临时union另占成本；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) decode-stage备用表示/短期union；root源与实际写后通过 |
| [Compiling Activation Steering into Weights via Null-Space Constraints for Stealthy Backdoors](https://arxiv.org/html/2604.12359v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | trigger前缀映射改为steering表示编译、clean null约束仅校准范围，改变checkpoint行为审计对象；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 模型文件小节的数据格式/参数行为分权；root 源、owner 与实际写后通过 |
| [Reading Between the Pixels: Linking Text-Image Embedding Alignment to Typographic Attack Success on Vision-Language Models](https://arxiv.org/html/2604.12371v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 外部embedding相似度、渲染与ASR的模型相关排序限制单一视觉防御选择；1+2+2=5 | 深入完成 | 仅报告：受限四VLM相关性，不是内部机制/通用防御证明 |
| [Masked by Consensus: Disentangling Privileged Knowledge in LLM Correctness](https://arxiv.org/html/2604.12373v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | self/peer probe必须分开全样本与correctness-disagreement切片，条件优势不等自知；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) Claim Sensor 的固定 probe/disagreement 切片；root 实际写后通过 |
| [ReasonXL: Shifting LLM Reasoning Language Without Sacrificing Performance](https://arxiv.org/html/2604.12378v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 参数delta大小/层深不能直接解释输出语言控制，单步activation patch提供受限功能定位；2+1+2=5 | 标准完成 | 仅报告：法语MGSM局部干预，不定普遍语言层或RL compute效率 |
| [On the Distillation Loss Functions of Speech VAE for Unified Reconstruction, Understanding, and Generation](https://arxiv.org/html/2604.12383v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | frame/关系margin与梯度权重决定语音表示重建/理解/生成取舍，过强对齐损声学目标；2+1+2=5 | 标准完成 | 仅报告：条件语音VAE分支，预算/评分聚合非通用Pareto最优 |
| [Preventing Safety Drift in Large Language Models via Coupled Weight and Activation Constraints](https://arxiv.org/html/2604.12384v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 固定clean safety子空间不能独自控制后续输入activation漂移，双约束仍是局部代理；2+2+2=6 | 深入完成 | 仅报告：白盒7–9B固定校准与SAE条件，不采全局安全保持保证 |
| [Do Transformers Use their Depth Adaptively? Evidence from a Relational Reasoning Task](https://arxiv.org/html/2604.12426v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 受控hop与patching分开readout/信息混合，不能把早读出当早停；2+1+2=5 | 标准完成 | 已有覆盖 `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，证据阶梯与可读出不等可拆卸 |
| [A Bayesian Perspective on the Role of Epistemic Uncertainty for Delayed Generalization in In-Context Learning](https://arxiv.org/html/2604.12434v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | approximate posterior EU与ICL泛化转折并非一条单调曲线；2+1+2=5 | 标准完成 | 仅报告：有限模算术与近似Bayes诊断，不作Transformer自知/泛化定理 |
| [Scaling Exposes the Trigger: Input-Level Backdoor Detection in Text-to-Image Diffusion Models via Cross-Attention Scaling](https://arxiv.org/html/2604.12446v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 干预attention响应而非只看静态激活，one-class detector仍依模型/clean校准；2+2+2=6 | 深入完成 | 仅报告：white-box diffusion backdoor诊断分支，不采通用安全保证 |
| [HazardArena: Evaluating Semantic Safety in Vision–Language–Action Models](https://arxiv.org/html/2604.12447v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | matched motor-feasibility与阶段危险进展揭示terminal失败不等语义拒绝；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) Outcome Witness 的能力匹配/阶段危险分账；root 实际写后通过，Ch26仅交接 |
| [Latent-Condensed Transformer for Efficient Long Context Modeling](https://arxiv.org/html/2604.12452v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | MLA语义pooling/位置anchor改变group概率质量，Uniform Error Bound遗漏multiplicity；2+2+2=6 | 争议 | 暂缓：中心误差界有最小反例，条件/证明修复前不作Books保证 |
| [CIA: Inferring the Communication Topology from LLM-based Multi-Agent Systems](https://arxiv.org/html/2604.12461v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 最终输出copy-history诱导能泄露拓扑线索，但semantics相关非真实edge保证；2+2+2=6 | 深入完成 | 仅报告：受限DAG协议与弱监督拓扑诊断，不采普遍IP泄漏保证 |
| [Meet Dynamic Individual Preferences: Resolving Conflicting Human Value with Paired Fine-Tuning](https://arxiv.org/html/2604.12479v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 相反偏好配对SFT被声称严格改善覆盖/Lipschitz保证，但同anchors与同objective没有该严格桥；2+1+2=5 | 争议 | 暂缓：理论机制与实际loss/对照差异未建立，不据此写Books |
| [An Ultra-Low Latency, End-to-End Streaming Speech Synthesis Architecture via Block-Wise Generation and Depth-Wise Codec Decoding](https://arxiv.org/abs/2604.12438v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | codec-depth顺序与time-block非自回归联合执行可能改变语音延迟/质量边界；2+1+2=5 | 受阻 | 暂缓：仅题摘/身份可核，精确v1必要方法与评价正文不可取；不采用48.99ms/10.6× |
| [Calibrated Confidence Estimation for Tabular Question Answering](https://arxiv.org/html/2604.12491v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 确定性表格序列化一致性提供与采样不同的confidence信号，保持内容不等保证答案真值；2+1+2=5 | 标准完成 | 仅报告：四格式协议与监督校准的受限反证，不泛化为所有QA |
| [Latent Planning Emerges with Scale](https://arxiv.org/html/2604.12493v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | future-token可解码须再核前向因果与前文许可，诗歌只有前向影响不等真正提前规划；2+1+2=5 | 标准完成 | 仅报告：条件性干预和任务反证，不作规模导致通用规划定理 |
| [Safety Training Modulates Harmful Misalignment Under On-Policy RL, But Direction Depends on Environment Design](https://arxiv.org/html/2604.12500v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | role framing与隐式gameability改变规模/安全风险相关方向，静态安全分数不通用预测后续RL；2+2+2=6 | 深入完成 | 仅报告：三模拟环境的设计反证，安全训练归因未完全隔离 |
| [CoD-Lite: Real-Time Diffusion-Based Generative Image Compression](https://arxiv.org/html/2604.12525v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 小codec不继承大生成器预训练优势，卷积替换须蒸馏而非直接删global attention；2+1+2=5 | 标准完成 | 仅报告：受限rate-distortion与执行分支，不采普遍实时收益 |
| [MODIX: A Training-Free Multimodal Information-Driven Positional Index Scaling for Vision-Language Models](https://arxiv.org/html/2604.12537v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 模态条件RoPE stride重排attention预算但距离代理不保证信息贡献或单调权重；2+1+2=5 | 标准完成 | 仅报告：启发式位置分支，不采用通用比例分配证明 |
| [FABLE: Fine-grained Fact Anchoring for Unstructured Model Editing](https://arxiv.org/html/2604.12559v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 多层fact anchor后单层narrative edit以preservation loss协调细事实与整体文本；2+1+2=5 | 标准完成 | 仅报告：固定层编辑的受限机制，不定神经知识普遍分层 |
| [IDEA: An Interpretable and Editable Decision-Making Framework for LLMs via Verbal-to-Numeric Calibration](https://arxiv.org/html/2604.12573v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 语言因子估计与外部显式decision model分权，AME约束保证属于参数模型而非世界真值；2+1+2=5 | 标准完成 | 仅报告：二元factor/完整性前提下的可编辑控制分支 |
| [Relaxing Anchor-Frame Dominance for Mitigating Hallucinations in Video Large Language Models](https://arxiv.org/html/2604.12582v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 输入移除后anchor仍在是位置偏置反证，按层logit重权不等真实证据恢复；2+1+2=5 | 标准完成 | 仅报告：八帧视频推理诊断，模型/评估子集不可混比 |
| [KumoRFM-2: Scaling Foundation Modelsfor Relational Learning](https://arxiv.org/html/2604.12596v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | timestamped关系子图与early task条件化联训/查询，邻域更多不总更好；2+2+1=5 | 标准完成 | 仅报告：受限关系foundation模型，不能把大库工程主张当实体负载/tenant隔离保证 |
| [CODO: An Automated Compiler for Comprehensive Dataflow Optimization](https://arxiv.org/html/2604.12618v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | producer/consumer访问顺序决定FIFO可行性，违反时回退ping-pong并联动调度；2+2+1=5 | 标准完成 | 仅报告：FPGA静态循环编译分支，HLS周期不等在线LLM SLO |
| [KnowRL: Boosting LLM Reasoning via Reinforcement Learning with Minimal-Sufficient Knowledge Guidance](https://arxiv.org/html/2604.12627v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 单个hint删除增益不能合成多hint删除，subset oracle搜索仍有代价；2+1+2=5 | 标准完成 | 仅报告：受限KP依赖反证与选择算法，不称在线无oracle或全局充分 |
| [Calibration-Aware Policy Optimization for Reasoning LLMs](https://arxiv.org/html/2604.12632v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 正确/错误回答pair的likelihood gap改变advantage，固定分布AUC一致不等在线单调；2+2+2=6 | 标准完成 | 仅报告：受限排序objective与reference mask，不采普遍Pareto/幻觉消除保证 |
| [PromptEcho: Annotation-Free Reward from Vision-Language Models for Text-to-Image Reinforcement Learning](https://arxiv.org/html/2604.12652v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 原prompt token的teacher-forced CE作为图文reward，不免偏差或VLM前向；2+1+2=5 | 标准完成 | 仅报告：具体冻结VLM reward接口，不采自动升级必提高真实对齐 |
| [Token-Level Policy Optimization: Linking Group-Level Rewards to Token-Level Aggregation via Sequence-Level Likelihood](https://arxiv.org/html/2604.12736v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | sequence ratio与token KL mask的熵梯度理论桥有可检查反例；2+2+2=6 | 争议 | 暂缓：中心熵梯度/strict sign保证，待作者勘误，不否定有限经验 |
| [GF-Score: Certified Class-Conditional Robustness Evaluation with Fairness Guarantees](https://arxiv.org/html/2604.12757v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 按类分解置信margin不自动是input扰动认证半径，温度fit clean排行也不补桥；2+1+2=5 | 争议 | 暂缓：中心input-L2 certificate缺约束，待作者明确保证对象与桥 |
| [SOAR: Self-Correction for Optimal Alignment and Refinement in Diffusion Models](https://arxiv.org/html/2604.12617v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 当前模型单步stopgrad偏轨迹状态再同noise重加噪，监督回原clean anchor；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 连续 diffusion 的 detached 局部训练 support；root 实际写后通过 |
| [Chain-of-Models Pre-Training: Rethinking Training Acceleration of Vision Foundation Models](https://arxiv.org/html/2604.12391v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 家族总训练成本下，小到大参数和特征接力改变单模型独立预算目标；2+2+2=6 | 标准完成 | 仅报告：CLIP家族链的受限预算分支，不采无损或LLM普遍加速 |
| [Three Birds, One Stone: Solving the Communication-Memory-Privacy Trilemma in LLM Fine-tuning Over Wireless Networks with Zeroth-Order Optimization](https://arxiv.org/html/2604.12401v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | ZO scalar反馈、无线噪声与功率预算联动，隐私必须绑定敏感度/组合条件；2+2+2=6 | 深入完成 | 仅报告：安全例外深入；受限无线模拟，不采用无条件DP或无同步保证 |
| [Beyond Transcription: Unified Audio Schema for Perception-Aware AudioLLMs](https://arxiv.org/html/2604.12506v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | ASR-only目标遗漏声学标签，与相同数据caption对照的slot监督改变训练支持；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 语义锚点到训练target责任；root必要源、实际正文与邻接写后通过 |
| [Whole-Body Mobile Manipulation using Offline Reinforcement Learning on Sub-optimal Controllers](https://arxiv.org/html/2604.12509v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | chunk级return与horizon-shifted bootstrap使离线critic和action单位一致；2+2+2=6 | 标准完成 | 仅报告：WBC/proprioception受限action训练，不称无数据或真机安全保证 |
| [From Myopic Selection to Long-Horizon Awareness:Sequential LLM Routing for Multi-Turn Dialogue](https://arxiv.org/html/2604.12385v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 跨轮累计目标的MCTS训练与future-state检索改变即时选模型目标；2+2+2=6 | 标准完成 | 仅报告：依赖用户模拟器/评价器的受限路由，不采跨场景净成本保证 |
| [Contextual biasing for ASR in speech LLM with common word cues and bias word position prediction](https://arxiv.org/html/2604.12398v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | common-word cue与位置tag监督替代推理用户所需phoneme接口；2+1+2=5 | 标准完成 | 仅报告：英语稀有词bias接口，训练匹配仍依赖音素词典 |
| [LASA: Language-Agnostic Semantic Alignment at the Semantic Bottleneck for LLM Safety](https://arxiv.org/html/2604.12710v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 层内semantic/language聚类差定位SSI后条件化对齐，不等因果安全瓶颈；2+2+2=6 | 深入完成 | 仅报告：安全例外深入；受限跨语言条件训练，不作内部语义或拒绝保证 |
| [Understanding and Improving Continuous Adversarial Training for LLMs via In-context Learning Theory](https://arxiv.org/html/2604.12817v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | surrogate线性ICL的embedding谱条件启发CAT正则，需区分输入与embedding威胁；2+2+2=6 | 深入完成 | 仅报告：安全例外深入；条件理论与经验启发，不称真实LLM继承该bound |
| [OSC: Hardware Efficient W4A4 Quantization via Outlier Separation in Channel Dimension](https://arxiv.org/html/2604.12782v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | group静态通道保护变为紧凑dense补偿，W2分布不同须FP8回退；2+2+2=6 | 标准完成 | 仅报告：具体混精度执行分支，未披露设备型号或端到端SLO，不采无损与普遍加速 |
| [VFA: Relieving Vector Operations in Flash Attention with Global Maximum Pre-computation](https://arxiv.org/html/2604.12798v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | key摘要初始化与选择性rowmax减少vector工作，数值稳定性不同于删块近似；2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 数值验收的全块累加/选择性统计更新；root 实际写后通过 |
| [RePAIR: Interactive Machine Unlearning through Prompt-Aware Model Repair](https://arxiv.org/html/2604.12820v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 单样本steering编译的exact preserve桥与正则逆不一致；2+2+2=6 | 争议 | 暂缓：正则最小二乘不能直接满足Eq6精确映射，隔离中心保证，不否定局部拒绝行为 |
| [Challenging Vision-Language Models with Physically Deployable Multimodal Semantic Lighting Attacks](https://arxiv.org/html/2604.12833v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 可部署照明扰动区分数字优化与物理帧级安全评价；2+2+2=6 | 深入完成 | 仅报告：固定拍摄/目标场景的安全实例，热图相关非因果、帧ASR非任务安全保证 |
| [UniMark: Unified Adaptive Multi-bit Watermarking for Autoregressive Image Generators](https://arxiv.org/html/2604.11843v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 多bit编码与zero-bit gate的识别对象冲突，有限样本FPR保证也未成立；2+2+2=6 | 争议 | 暂缓：隔离任意message识别/精确FPR保证，需payload-aware gate及有限样本修正，不否定全部经验结果 |
| [When Self-Reference Fails to Close: Matrix-Level Dynamics in Large Language Models](https://arxiv.org/html/2604.12128v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | grounded与nonclosing自指不是同一谱行为，跨架构方向及probe真值要分开；2+1+2=5 | 标准完成 | 仅报告：受限诊断与conjecture，非自知或矩阵不可判定性通用机制证明 |

| [KoCo: Conditioning Language Model Pre-training on Knowledge Coordinates](https://arxiv.org/html/2604.12397v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | document条件标签改变token监督支持，但source关联不等事实真值；2+1+2=5 | 标准完成 | 仅报告：条件预训练的受限标签设计，不采普遍消幻觉或正交解耦保证 |
| [From Attenuation to Attention: Variational Information Flow Manipulation for Fine-Grained Visual Perception](https://arxiv.org/html/2604.12508v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | privileged answer posterior训练、inference prior与深层attention概率注入分开；2+1+2=5 | 标准完成 | 仅报告：受限CVAE视觉focus分支，不当普遍信息流因果机制 |
| [Every Picture Tells a Dangerous Story: Memory-Augmented Multi-Agent Jailbreak Attacks on VLMs](https://arxiv.org/pdf/2604.12616v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | 原始无害图片可成为跨图复用攻击anchor，judge和多轮预算决定安全证据；2+2+2=6 | 深入完成 | 仅报告：安全反证与具体攻击协议，不把经验记忆收益当因果保证或通用防御 |
| [GeoAlign: Geometric Feature Realignment for MLLM Spatial Reasoning](https://arxiv.org/html/2604.12630v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | geometric层选择存在任务排序反转，按patch稀疏查层有代价与反收益；2+1+2=5 | 标准完成 | 仅报告：几何特征bank的受限路由分支，不采单层必然不足或所有任务更优 |
| [FeaXDrive: Feasibility-aware Trajectory-Centric Diffusion Planning for End-to-End Autonomous Driving](https://arxiv.org/html/2604.12656v1) | 2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00 | clean trajectory统一约束对象，区域guidance与曲率/GRPO目标实际冲突；2+1+2=5 | 标准完成 | 仅报告：NAVSIM约束/指标分账的受限规划分支，不作为实车安全保证 |
| [Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning](https://deepmind.google/blog/gemini-robotics-er-1-6/) | 2026-04-14T16:00:00+00:00 | high-level reasoner调用视觉工具与VLA，仪表读取预算与multiview评价样例不同；1+2+2=5 | 标准完成 | 仅报告：官方发布/评价条件，未公开新训练机制，现有分层控制论点不改 |

## 4. 证据与知识整合

### [TIPSv2: Advancing Vision-Language Pretraining with Enhanced Patch-Text Alignment](https://arxiv.org/html/2604.12012v1)

实际读§3.1–3.5、§4.1–4.3/Tables2–4。masked student view仍保留，只将直接teacher-target监督从masked扩到visible+masked patches；不是取消遮蔽，也不是原模型没有局部信息。head-onlyEMA共享vision encoder但保留EMA projector，外部图文contrastive信号与全共享head失稳限制适用。116M WebLI、ViT-g、512TPUv5约两天及冻结encoder九任务二十数据集限定结果；累积消融非全因子，部分PASCAL/Normals退步。Ch23现已在对齐多目标主线局部解释腐化/监督支持、独立局部验收和完整EMA回退，apr02必要源/owner及root实际写后通过；6分真实缺口深入例外，未复现实验。

### [LoSA: Locality Aware Sparse Attention for Block-Wise Diffusion Language Models](https://arxiv.org/html/2604.12056v1)

实际读§2.1–2.2、§3–5及§7。历史prefix KV固定而query变化，低漂移query复用prefix attention output和LSE，active queries重算稀疏prefix并和当前block dense attention共同归一化。缓存是query条件派生状态，不是跨query exactKV命中；kernel实际读取active-query索引union。§4.4完整block union直接界为active-count×k缺条件，不采用；首轮dense、额外状态/排序、短prefix及局部QUEST更优保留。Trado/SDAR、block16/32、batch1和A6000/5090 attention微基准非端到端SLO。Ch45 refresh-frontier后实际补派生状态有效性及物理union合同，Ch14只交接online-softmax原理；apr02必要源/owner和root实际写后通过。

### [Beyond Perception Errors: Semantic Fixation in Large Vision-Language Models](https://arxiv.org/html/2604.12119v1)

实际读§3–8及D.1必要steering条件。同一terminal board配standard/inverse规则，中性alias与semantic valence再注入提供受控语义映射对照；samepixels不证明每次感知都正确，准确router/donor下late-layer干预也不排除其他路径。四合成games/十四VLM、greedy/1024预算的closed reduced与open expanded协议分开；same-rule SFT可伤opposite-rule，不能推自然任务通用鲁棒。Ch66三对象decision段后真实补EvalSpec的视觉状态×规则×alias语义配对，apr02必要源/owner与root实际写后通过；未复现实验。

### [PipeLive: Efficient Live In-place Pipeline Parallelism Reconfiguration for Dynamic LLM Serving](https://arxiv.org/pdf/2604.12171v1)

本项HTML headline与abs/PDF-v1不一致，采用官方PDF-v1，实际读§4/Alg1、§5–6和§7.2–7.3。current∪target双驻留层集确定临时KV容量，liveblocks装不下就拒绝；block-address/layerstack改布局，dirtyslot增量patch追赶写入，但Tsched/Tapplied差不是slot lineage证明。finalsync+atomiccommit、两NCCL互斥握手及CPU预驻权重成本均必须保留。A10080GB/L40S48GB跨节点、Llama3-70B/Qwen3-30B、512/16与128/512、有限arrival及200请求patternshift限定结果；profiling选target，QwenTTFT可退步，precision/productionSLO/故障恢复未建立。Ch52 StatefulElasticity后真实写临时容量—布局—增量写—最终提交分支，root必要源/owner与实际写后通过；未复现实验。

### [Filtered Reasoning Score: Evaluating Reasoning Quality on a Model's Most-Confident Traces](https://arxiv.org/html/2604.11996v1)

实际读§3.1–3.3、§4.1–4.3、§5–6及限制。低概率token尾部均值用于给trace排序，再在model–benchmark pooled集合取top-K%；这不是部署时每题的最佳答案oracle。9个1.5–14B模型、6任务、k16/T0.7与看gold的文本judge限定结果；Phi4重复续写可提高confidence却降低rubric质量。Ch66 Evidence Trail主线现已加入同一selector/coverage子集的答案正确性与过程质量分账、全体baseline和采样/judge成本，保留文本faithfulness不是内部因果证明的边界。该窄缺口触发深入例外，不抬6分；apr02必要源与实际写后复核通过，未复现实验。

### [When Does Visual Token Pruning Improve Calibration? The Role of Evidence Coverage in MLLMs](https://arxiv.org/html/2604.12035v1)

实际读§3.1–3.3、§4.1–4.8、§5与结果表。LLaVA-1.5-7B/CLIP576、greedy、POPE与ScienceQA-IMG的first-token候选内归一化confidence仅是该任务估计器；同accuracy不保证同ECE，强剪枝的质量/校准趋势也因任务不同。SCOPE同路径α干预与FastV外部2-pass实现分开，原文未给zeroing对物理删token的直接受控比较。Ch66 Calibration Slice现已写入kept-set、selector、执行路径与估计器共同构成校准身份，并把视觉压缩机制交回Ch23。apr02必要源/owner及实际写后通过；不外推开放答案概率或线上可靠性。

### [Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration](https://arxiv.org/html/2604.12046v1)

实际读§3.1–3.4、§4.1–4.4/Table1–2及AppA.1–A.2。先按外部VeriScore构造claim/confidence的DPO，再以correctness reward作GRPO并mask confidence位置；位置mask不冻结共享参数决定的confidence函数。Biography的AUROC .688→.676、Brier .266→.268是直接反例；AUROC又不等概率校准。不同优化器、数据和预算不能只归因于顺序，最终文本重生成也可能改写claim。Ch66 Verbalized Confidence现已补入factual更新后重校准、最终claim保持与回退边界，owner不是Ch33；apr02必要源与实际写后通过，未采用相对准确率headline为部署保证。

### [How Transformers Learn to Plan via Multi-Token Prediction](https://arxiv.org/html/2604.11912v1)

实际§3–5.3/Limitations/E.1–E.3：parallel同prefix多头的训练目标与NTP推理分开；两层disentangled、固定block读头、content零初始化/Toeplitz和两阶段gradient-flow限定浅loss→前驱pointer→content matching机制。NTP在binarytree随规模也能改善、有限图可记忆、checkpoint选择与额外head训练预算不是全compute匹配均保留。Ch28原NTP主线缺梯度路径这一分支，已实际插入“Future-token辅助目标改变的是学习路径”，root源/owner与实际正文相邻衔接独立通过。6分知识缺口深入、整合，不推通用规划或推理加速；[必要证据](../_sources/daily-20260415/V3_EVIDENCE_REVIEW.md)可复核。

### [Automated Alignment Researchers](https://alignment.anthropic.com/2026/automated-w2s-researcher/)

实际读§1、§3.4–3.5与§4 EM伪码，以及必要评价/限制。输入相关noisy channel和strong-model margin prior形成tempered posterior，两轮重估student/channel；channel只用于训练，不是部署真值oracle。Ch31写入弱到强主线，保留弱prior、相关错误、噪声floor、迭代成本和回退边界；root原文/实际写后已通过，其他evaluator防hack原则已有Ch66/81覆盖，不照录PGR为生产保证。

### [Subcritical Signal Propagation at Initialization in Normalization-Free Transformers](https://arxiv.org/html/2604.11890v1)

实际§2.1–2.4/3.2–3.3/4与Ch17前后论证已读。α是tanh/erf输入scale而非外部residual gate；APJN为平方Frobenius均值。Ch17实际新增无Norm初始化分支，限定宽/双向attention近似与CIFAR-100初期ViT，不保证causal LM、完整训练质量或所有奇异值。root已独立重开必要原文与Ch17实际正文/前后交接，写后通过。

### [M*: Discovering Task-Optimized Memory Harnesses for LLM Agents](https://arxiv.org/html/2604.11811v1)

实际§3.1–3.3/Alg1、§4–6与AppendixB–C；schema/读写逻辑/instructions共同构成可执行程序，固定25验证项选候选、轮换5项给反思反馈，白名单/编译/mock只保证局部运行条件。Ch77真实两段位于组件归因/Pareto主线之后：选出的程序仍需独立heldout与发布验收，离线入库/候选/评价/环境总成本与在线0～2额外调用分开。LoCoMo约5.1h、ALFWorld约100h为作者受限环境总账，不采普遍同成本或全部切片更好；root已独立顺读实际两段及其上下交接，对照必要原文，单篇写后通过，不预支整日完成。

### [A Layer-wise Analysis of Supervised Fine-Tuning](https://arxiv.org/html/2604.11838v1)

§3–4的CKA/更新范数与中间LM-head读出不证明知识不存在或普遍局部化，分段LoRA有参数/预算混杂。Ch29已有可训练子空间、层敏感性和regime验收真实命题；保留局部结果，不添加全部只训中层规则。

### [ProbeLogits: Kernel-Level LLM Inference Primitives for AI-Native Operating Systems](https://arxiv.org/html/2604.11943v1)

必要§2.3/3/7.4–7.5/8.3与Table4–5：同模型分类仍有forward成本，fuel/host接口的结构mediator不能证明classifier无误；基线组件不匹配、有限F1不能推零漏报。Ch72 Policy-as-Data与Ch78 typed proposal已经分开传感/决策/授权/执行。

### [ResBM: Residual Bottleneck Models for Low-Bandwidth Pipeline Parallelism](https://arxiv.org/html/2604.11947v1)

实际§3–4：2→1→2矩形identity连乘为diag(1,0)，不等Eq6端点I2；因此不采普遍identity。受限2B/8blocks/C4训练与8×A10G/GPipe/NCCL对照可保留，但optimizer/预算不完全匹配，不据反例否定全部经验结果。

### [GRACE: A Dynamic Coreset Selection Framework for Large Language Model Optimization](https://arxiv.org/html/2604.11810v1)

§4.3选择性重算/传播程序与§5实验已读；原quadratic驻点需按原w的总和归一，而不是任意固定half混合。定义归一化α不能静默改变objective；中心保证隔离，等待有限非作者复核，不把理论争议藏在一般已有数据治理标签后。

### [Active Imitation Learning for Thermal- and Kernel-Aware LFM Inference on 3D S-NUCA Many-Cores](https://arxiv.org/html/2604.11948v1)

§5–6的kernel-specific GPR、dropout触发oracle查询是模拟迁移程序。冷cache、热限制与多次forward均有代价，CoMeT结果不证明物理GPU安全或生产延迟；仅报告这条局部执行路线。

### [The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break](https://arxiv.org/html/2604.11978v1)

§3/4及AppendixD/F区分最少动作与observed rollout，但depth/breadth也增加其他难度；baseline成功选择、有限judge一致性和JSON-plan embodied模拟限制因果结论。保留具体构造，不采用统一长任务阈值。

### [Evaluating Cross-Architecture Performance Modeling of Distributed ML Workloads Using StableHLO](https://arxiv.org/html/2604.12090v1)

§III–VI/TablesIII–IV：IR切片改变编译优化机会，cache绑定硬件/编译器/region，closed compiler与backend不可见使多fidelity排序可反转。所列BF16/FSDP/TPU等条件不统一外推；详细实验与反证见本日证据笔记。

### [Narrative over Numbers: The Identifiable Victim Effect and its Amplification Under Alignment and Reasoning in Large Language Models](https://arxiv.org/html/2604.12076v1)

§3/4.2.1/5.6/7的有限API/模板/temperature行为测量，规范内容与reasoning长度同时变化，金额上界又有ceiling效应。不能从行为方向推内部情绪或纯CoT因果；报告保留反证而不强写Books。

### [The A-R Behavioral Space: Execution-Level Profiling of Tool-Using Language Model Agents in Organizational Deployment](https://arxiv.org/pdf/2604.12116v1)

官方PDF-v1 §3/Table1/5实际可读。A与R不互补，D没有可核的完整joint计算定义，latest标签不可作为固定模型身份。Ch66真实Act/Silent/Stop、动作效果与安全多轴段已承载语言拒绝不能替代动作检查的结论。

### [Polynomial Expansion Rank Adaptation: Enhancing Low-Rank Fine-Tuning with High-Order Interactions](https://arxiv.org/html/2604.11841v1)

实际§3.1–3.3、§5.4–5.6与AppA.3。多项式共享因子产生更宽有效rank，名义r与展开rank不混用。AppA.3从可表达集合是rank≤R子集推出不高于该全集最优误差，缺少覆盖最优解的证明；有限实验不被此证明缺口全部否定。Table5单RTX5090/rank4/batch16下推理时间也不是零overhead，完整条件见本日证据笔记。

### [Disposition Distillation at Small Scale: A Three-Arc Negative Result](https://arxiv.org/html/2604.11867v1)

实际§3–6/8：matched judge、response-blind和长度harness重测、100-item CV与193独立生成prompt分开，低probe AUC不证明全部内部信息不存在。Ch66已实际承载matched probe、Calibration Slice的sensor身份/heldout以及judge格式审计；不采用§4.1不足以解释增益方向的截断因果说明，不把head damping推广为内部routing保证。

### [The Linear Centroids Hypothesis: How Deep Network Features Represent Data](https://arxiv.org/html/2604.11962v1)

官方v1题名与库存后发题名不同，实际采用§2–4/Limitations。Jacobian-centroid的CPA精确性与光滑局部近似分开，Theorem3.4依Hypothesis3.3；FashionMNIST相关颜色、DINO/Imagenette及Llama8B第12层probe是有限比较，不证明truth/circuit全部忠实。仅报告具体工具及提取成本，不假称Ch5已承载完整算法。

### [Offline-Online Reinforcement Learning for Linear Mixture MDPs](https://arxiv.org/html/2604.11994v1)

实际§2–4/6：knownΔ、known feature及确定reward条件下confidence组合允许退回online。设计矩阵coverage不等于日志数量；5states/10actions/H3合成模拟50runs支持该分支，不证明LLM Agent部署保证，理论/模拟不是GPU性能研究。

### [Loss-Driven Bayesian Active Learning](https://arxiv.org/html/2604.11995v1)

实际§3.1–3.5/Theorem1及§5.1：加权Bregman、有限矩与凸动作域满足时可消除inner minimization，仍需belief/expectation，myopic一步不是全程Bayes最优。固定GP/3initial+25acquired/25runs等受限条件不外推foundation training；保留具体目标联系而不假称其完整算法已经进入Ch27。

### [When to Forget: A Memory Governance Primitive](https://arxiv.org/html/2604.12007v1)

实际§3–4/5.1–5.4：双counter统计的是关联条件成功，不是因果credit；任务难度可反向排序，co-retrieval的hitchhiker不可分，条件化只部分恢复。合成100memory/10K episodes/20seeds与20句MiniLM/keyword outcome不证明真实LLM删除安全。仅报告该诊断算法，不把Ch77一般归因治理说成本算法已吸收。详见必要证据。

### [Sample Complexity of Autoregressive Reasoning: Chain-of-Thought vs. End-to-End](https://arxiv.org/html/2604.12013v1)

实际§1.1/2.1–2.3限定确定generator、有限token域/VC、IID-realizable和完整链标签。CoT样本数不依T不等于标注token或训练计算免费，dual-VC常数仍有代价；e2e增长谱不提供Transformer优化保证。仅报告这一监督边界，不声称全证明已核或本仓库复现。

### [UCS: Estimating Unseen Coverage for Improved In-Context Learning](https://arxiv.org/html/2604.12015v1)

实际§3–6/Limitations：模型embedding→离散簇/SGT频谱→既有selector正则化，簇不是语义真值，采样假设和离线embedding成本不能省略。有限intent/BBEH、三runs中joint-source和rarity切片有反收益，不采全切片胜或开放生成保证。仅报告具体coverage prior，不假称算法已有Books覆盖。三个家族官方abs/v1身份/状态已核，Updated仅作保存批次组合的一部分。

### [Benchmarking Deflection and Hallucination in Large Vision-Language Models](https://arxiv.org/html/2604.12033v1)

实际§3–4/6：四gating模型过滤产生的是条件题库，2,775上下文样本不是1,246独立问题之外的新问题。parametric/oracle/mixed/negative分账有诊断性，但单pass/GPT-4o judge与文本偏置不证明内部知识缺失或开放域truth。仅报告具体curation实现，重筛时需保留题库版本；不把Ch66一般RAG归因说成本算法已有覆盖。

### [SIR-Bench: Evaluating Investigation Depth in Security Incident Response Agents](https://arxiv.org/html/2604.12040v1)

实际§3–6：模拟重放、SME findings、ROUGE-L校准与CloudTrail观测上限保留，tool coverage不是调查真值。Table6同TP分母的Hit3+=64.6%<Hit5+=68.4%违背Eq5嵌套定义，M1 Eq3也不是通常precision/recall Fβ。中心比例精确争议隔离，等待作者修正分母/原始计数和非作者最小核查，不据此写Books，不否定全部replay机制。

### [VISTA: Validation-Informed Trajectory Adaptation via Self-Distillation](https://arxiv.org/html/2604.12044v1)

实际§3/Alg1、§4–5：validation边际覆盖加权checkpoint差分形成soft teacher，零权anchor在固定排序下可精确去除，但τ>0是近似、validation多轮复用不等于独立test。ResNet-18/两图像数据集/三seed及外部表预算不匹配限定结果；只报告具体算法，不推全部子群表示保持、LLM迁移或无损剪锚。

### [Can we Watermark Low-Entropy LLM Outputs?](https://arxiv.org/html/2604.12051v1)

实际§1.2/2/3/Figs2–4及§4.1：原分布双采样、hash-bit与PRC的条件构造区分undetectability/soundness/robustness。低熵仍需长子串熵支持，random substitution与deletion附加假设不是任意自适应改写保证；密钥/搜索成本、理论而非生产检测均保留。本轮只报告所核构造，不声称全部robustness证明已验。

### [LLM-Redactor: An Empirical Evaluation of Eight Techniques for Privacy-Preserving LLM Requests](https://arxiv.org/html/2604.12064v1)

实际§4–7：四合成模板族的云端route、span删改和语义泄漏需不同分母；TEE/FHE/MPC/split的stub与wire曝光不等完整部署保证。word替换单式不构成DP证明、少量utility judge不支持全面Pareto，原per-kind/ranking不一致不采用；仅保留受限安全反证，不写生产隐私结论。

### [SOLARIS: Speculative Offloading of Latent-bAsed Representation for Inference Scaling](https://arxiv.org/html/2604.12110v1)

实际§3–5：背景pair embedding→TTL cache→miss zero/refresh，user-only/neighbor是另一个feature而非精确pair恢复。末端ranking部署与offline coverage实验分开，前段规模不在已部署范围，具体hardware/并发/SLO与分流不确定性未披露；不将收入headline或background计算藏成零成本，只报告实际条件分支。

### [HTDC: Hesitation-Triggered Differential Calibration for Mitigating Hallucination in Large Vision-Language Models](https://arxiv.org/html/2604.12115v1)

实际§3–6：layer keyword分布更新的EMA/cosine触发两nullification probe，内部trigger不是事实置信度；1+2r forward计数不消除白盒读出/gating/cache成本。两VLM四benchmark下CHAIR Recall下降、Qwen cognition退步，Table6没有支持visual probe总必需。不以受限MME时延推生产SLO或普遍打破取舍；仅报告，不假称Ch23已包含本EMA算法。

### [Towards Platonic Representation for Table Reasoning: A Foundation for Permutation-Invariant Retrieval](https://arxiv.org/html/2604.12133v1)

实际§2/4/5–6：CKA heatmap对固定行列恢复作内在诊断，结构encoder是既有TRL基线，新retrieval只是未来方向。20base表的3,791置换不是独立文档；merged cell与层级header不满足干净群作用，作者明确未有端到端检索/推理协议。仅报告，不把高CKA、模型大小或header结构泛化为faithfulness/收益保证。

### [Why Your Tokenizer Fails in Information Fusion: A Timing-Aware Pre-Quantization Fusion for Video-Enhanced Audio Tokenization](https://arxiv.org/html/2604.12145v1)

实际读IV–VI的方法/关键表格；量化前cosine融合与motion条件时间窗口为具体分支。AVQA为冻结Llama3.1-8B的classification，不是生成端到端audio系统；三seed表格仍有fidelity退化，总梯度方差不证明冲突因果，FSQ/RVQ的8倍token差不是对Wav的8倍速度。Ch23有双表示与rate–distortion主线但不等本算法；仅报告，不强制修改书稿。完整限定见[必要证据](../_sources/daily-20260415/V3_EVIDENCE_REVIEW.md)。

### [From Plan to Action: How Well Do Agents Follow the Plan?](https://arxiv.org/html/2604.12147v1)

§2–6.2/8实读；coverage、first-occurrence LIS与purity不能替代issue resolution，有用额外测试也可能降purity。四模型/eight plans/Verified，以及仅31个标准可解Pro子集不混为全体评估；每五步提醒增加Context/forward。Ch79现ledger主线不含此完整指标，具体反证仅报告，不把提醒频率变成通用规则；v1正文/abs16,991轨迹，不继承库存21,120。

### [PubSwap: Public-Data Off-Policy Coordination for Federated RLVR](https://arxiv.org/html/2604.12160v1)

实际§3–5：本地GRPO/周期LoRA聚合之外交换共同prompt回答，Balanced仅在pool有正确回答时替换；local-old ratio不自动校正各foreign行为分布，分开A/B平均不是全部更新乘积平均。有限模型/同步周期下并非全胜，也未建立隐私保证。标准完成、仅报告协调分支；[必要证据](../_sources/daily-20260415/V3_EVIDENCE_REVIEW.md)保留预算与反例，不把算法冒称Ch33完整已有覆盖。

### [Nucleus-Image: Sparse MoE for Image Generation](https://arxiv.org/html/2604.12163v1)

实际§3.3/5–8：Expert Choice覆盖与timestep调制分离、跨分辨率capacity安排和固定text KV各有条件。受限BF16图像训练/50step评价不证明独立routing归因或全质量–时延前沿，切片并非全胜。标准完成、仅报告具体生成配方，不因Ch21/24已有一般机制就假称完整实现已吸收，细节见[必要证据](../_sources/daily-20260415/V3_EVIDENCE_REVIEW.md)。

### [Policy-Invisible Violations in LLM-Based Agents](https://arxiv.org/html/2604.12177v1)

实际§3–6：可信metadata graph与copy-on-write proposal effects预检、三值未知处置有明确机制；flat taint/translation predicates仍会错，完成trace replay不是在线原子提交。安全深入完成、仅报告受限overlay程序，不把完整谓词假设或balanced小样本变成开放零误判。Ch72已有权力分离不包含此全部算法，反例与评价分母见[必要证据](../_sources/daily-20260415/V3_EVIDENCE_REVIEW.md)。

### [Knowledge Is Not Static: Order-Aware Hypergraph RAG for Language Models](https://arxiv.org/html/2604.12185v1)

实际§3–4/AppA.2–A.4：规则构造horizon/phase precedence，learned transition补软顺序，beam evidence chain在同graph shuffle对照有条件收益；不是无监督真实因果时间，也不能证明全部set检索失效。标准完成、仅报告受限sequence实现，具体模型/评价/预算边界见[必要证据](../_sources/daily-20260415/V3_EVIDENCE_REVIEW.md)。

### [Beyond Majority Voting: Efficient Best-Of-N with Radial Consensus Score](https://arxiv.org/html/2604.12196v1)

实际§3–4/Alg1：Eq4平方medoid等价nearest mean，Eq7非平方目标则不同；uniform点0,1,2,3,100的最近mean为3、非平方medoid为2。仅隔离该等价保证，经验聚合不被全部否定，MiniLM/ROUGE效标与同源错误边界见[必要证据](../_sources/daily-20260415/V3_EVIDENCE_REVIEW.md)。深入例外、争议暂缓，待非作者定点核。

### [AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning](https://arxiv.org/html/2604.12201v1)

实际§3–5：retrievability与persuasion反馈分开，单文档并非无攻击成本。Table2所列一行.92×.565不等.59，不采用该overall值；迭代baseline预算不匹配，也不归因CoT唯一作用。安全深入完成、仅报告受限威胁程序和乘积边界，详见[必要证据](../_sources/daily-20260415/V3_EVIDENCE_REVIEW.md)。

### [Beyond Factual Grounding: The Case for Opinion-Aware Retrieval-Augmented Generation](https://arxiv.org/html/2604.12138v1)

实际§4–7/Table2：观点分布保真/fairness目标与metadata-enriched hybrid实现不同，variance不是KL/Wasserstein。48query/四entity/seller论坛和固定模型下sentiment多样性改善而部分demographic coverage下降；人类偏好多样性不证明总体代表性。标准完成、仅报告具体目标错位/取舍，不把形式目标当已实现保证；精确v1标题已纠正，边界见[必要证据](../_sources/daily-20260415/V3_EVIDENCE_REVIEW.md)。

### [ViLL-E: Video LLM Embeddings for Retrieval](https://arxiv.org/html/2604.12148v1)

实际§3–5/AppA直接表格：生成hidden states直到EOS作为queries读取learned pooling K/V，再形成embedding；adaptive readout不是忠实CoT。固定1/5token模型分别训练，三阶段数据/双目标也影响成绩，不据长度相关断言思考因果。12frame/batch16/L40S的时延与部分切片反收益保留，不合为线上SLO。标准完成、仅报告机制，不假称已有Books覆盖全部算法。

### [Fully Homomorphic Encryption on Llama 3 model for privacy preserving LLM inference](https://arxiv.org/html/2604.12168v1)

实际§3.2–3.5、§4/Tables2–5、§5/Table6：Single只远端FHE first-layer attention，余层client plain且softmax明文；trusted client/honest-passive服务器不等开放全链隐私。§4.6.1 Eq7把tokens/s再除seconds，单位与表中tokens/s缺桥。79prompt/5run/2bitCPU经验不被全部否定，但中心吞吐与保护范围暂缓、不入Books；具体公式、权限及重开材料见[必要证据](../_sources/daily-20260415/V3_EVIDENCE_REVIEW.md)。

### [EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture](https://arxiv.org/html/2604.12167v1)

§2–4.6/6实际读：idle STDP关联活动经过显式threshold触发LLM动作选择，不能称无控制器/意识。两条件均N=1、同一LLM/三天25用户消息，journal内容可能是事后叙事；Ch77有主动干预权力分工而非本SNN实现。标准完成，仅报告所测触发分支，不推生产价值，详[必要证据](../_sources/daily-20260415/V3_EVIDENCE_REVIEW.md)。

### [Representing expertise accelerates learning from pedagogical interaction data](https://arxiv.org/html/2604.12195v1)

§2–4/AppA.4–A.6实际读：expert-only忽略recovery states；混合interaction增加覆盖却须分离动作来源，完整cue训练缺cue可失败。17.6M/十grid的token-matched0.5%expert对照不推自然语言多Agent通用比例；标准完成，仅报告具体source-cue条件，不假称Ch27覆盖全部实验。

### [Structural Anchors and Reasoning Fragility:Understanding CoT Robustness in LLM4Code](https://arxiv.org/html/2604.12214v1)

IV-F/G、V与VI必要段实际读：signature固定、docstring扰动和promptexplicitness分开，anchors只是对齐。不同模型/任务CoT排序改变；earlyentropy弱相关、AUROC方向和正文/表格分开，不采可靠内部sensor。标准完成、仅报告受限反证，未识别唯一因果机制。

### [Learning Project-wise Subsequent Code Edits via Interleaving Neural-based Induction and Tool-based Deduction](https://arxiv.org/html/2604.12220v1)

IV-B/C、V/VI必要段实际读：multi-label composition invoker选有限LSP服务，fine编辑labels与semantic定位/生成交错；diagnostic另由LSP推送。crossproject数据、三任务24人限定，有Cursor反胜与overtrust恢复成本。标准完成、仅报告低时延交互设计，不把BLEU/调用工具当全repo一致性。

### [TimeMark: A Trustworthy Time Watermarking Framework for Exact Generation-Time Recovery from AIGC](https://arxiv.org/pdf/2604.12216v1)

采用April15官方PDF而非August24 HTML；实际§5双段ECC/PRF、HSM时间key及§6.3概率边界。固定独立近似下已有非零错误，与理论100%口径不一致；多窗、低熵与provider trust条件亦不能被哈希替代。安全深入争议暂缓，保留受限机制，不提供法律或完美验证保证。

### [Ride the Wave: Precision-Allocated Sparse Attention for Smooth Video Generation](https://arxiv.org/html/2604.12219v1)

§3.3–5.3/Table1实际读：10prompt离线曲率曲线重分step预算，随机routing与32-block coalesced统计补偿。未clamp连续budget和不保证有限期每块选择边界保留；H800三VideoDiT限定，Wan14B美学下降、较PISA稍慢。标准仅报告，不叫online反馈/精确attention或全维Pareto最优。

### [SpecBound: Adaptive Bounded Self-Speculation with Layer-wise Confidence Calibration](https://arxiv.org/html/2604.12247v1)

§2–3实际读：ACT/双界/cache处理是具体机制，但全层执行不证明sampling拒绝修正/commit law；Eq5固定α大w极限与单调宣传不相符。中心保证争议暂缓；H800/所测7/13B经验速度不被反例自动否定，也不作为lossless生产保证。

### [SpanKey: Dynamic Key Space Conditioning for Neural Network Access Control](https://arxiv.org/pdf/2604.12254v1)

采用April15PDF，实际§3.3–6及§11：正确key-only训练可吸收注入，deny loss/拒绝类别有条件改善。known-B无梯度probe不等未知Bblackbox安全，几何tail不保证gate行为；作者无密码学保证。安全深入仅报告受限模型/威胁边界，不替代真实授权隔离。

### [Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision](https://arxiv.org/html/2604.12002v1)

§2/Eq1–4、§3–4和C.1/C.2必要证据实际读。成功修订过滤保留失败初答，Eq2 generation target覆盖整串；当前student回答/外部结果供冻结reviser形成特权reverse-KL。局部KL与词汇变化非内部自知，completion预算非全部compute匹配。Ch33 TeacherSignal主线两段真实写入，root及apr02 actual写后通过；6分缺口深入例外。

### [Distinct mechanisms underlying in-context learning in transformers](https://arxiv.org/html/2604.12151v1)

Roman III、IV.1–IV.7、V实际读。有限Markov/浅模型中context既为任务身份，也为统计样本；动力学竞争与容量压缩不同，足够容量taskvector仍可泛化。patch不证明唯一circuit，不推现代LLM阈值。Ch5动态表示两段实际写入，root/apr02 actual写后通过，6分缺口深入例外。

### [Evaluating Relational Reasoning in LLMs with REL](https://arxiv.org/html/2604.12176v1)

§3–6必要定义/生成/评价实际读；固定或交叉改变input/entity规模、generator arity与operand难度。不同任务/指标/输出不合为因果曲线，RC非内部capacity下界，有限预算失败非任意计算无效。Ch66 EvalSpec两段实际写入，root/apr02 actual写后通过，6分缺口深入例外；不将领域任务恢复为AI-for-Science路线。

### [TEMPLATEFUZZ: Fine-Grained Chat Template Fuzzing for Jailbreaking and Red Teaming LLMs](https://arxiv.org/html/2604.12232v1)

实际读v1 §3.2–3.4、§5.2–5.3、§6.1–6.3：对system/history/role/delimiter/generation hint分元素mutation，MCTS/Roulette搜索同时记录harmful-query和一般题正确性。开源实验有修改实际template权限；商业实验仅将其他家族模板文字注入prompt，不能说已修改厂商内部模板。oracle以judge分歧人工标注增强规则，Table6仍有8.02% FPR；超过90%与模型agreement也非人工真值。AdvBench、有限搜索预算/所选Top-k和MMLU utility限定结果，不证明生产整体安全率，§6.2防御只是未验证建议。6分安全深入，仅报告具体red-team矩阵；Ch66已有harness/template身份，Ch72已有授权与guard边界，但不假称本fuzz算法已经全覆盖。

### [UniRec: Bridging the Expressive Gap between Generative and Discriminative Recommendation via Chain-of-Attribute](https://arxiv.org/html/2604.12234v1)

官方v1完整题摘已恢复，旧库存末尾截断不再作为依据。必要§3.2–3.6中，CoA先生成属性再SID、exposure-cap量化与业务loss构成具体生成推荐分支。§3.3 Eq3把跨item排序的Bayes式写成省略p(f|u)的比例，不能推出只要全特征即可相同排序：固定p(y=1)=.5，p(A|y1)=.8、p(A|y0)=1，则p(y1|A)=4/9，p(y1|B)=1，而likelihood排序A>B。中心“solely feature coverage”保证5分深入争议暂缓；不否定CoA全部经验收益，不据此替换Books现有生成/检索设计。重开只需作者说明固定归一化条件或修正证明。abs/v1与HTML题名一致，未见撤回；v1Updated00:21:38Z仅与保存批次组合共同支持本窗区间。

### [Socrates Loss: Unifying Confidence Calibration and Classification by Leveraging the Unknown](https://arxiv.org/html/2604.12245v1)

实际v1 §3.1/Eq1–3、§4.1–4.2、AppendixE.1–E.2：focal项、EMA目标与auxiliary-idk合并，β的最大集包括idk，不能误判为必出现负惩罚。E.1先限制t=1；E.2的单项p_y t_y logp_y与整分布entropy不是所写等式，至多还需限定/不等式桥。初期梯度较小也不推出EMA目标全程不overfit或普遍calibration保证。5分中心理论深入争议暂缓，四分类数据/VGG-ResNet-ViT、5seed、300epoch/transfer50epoch的受限经验保留；shared A100环境未报告时长，不推统一效率收益。重开需动态target证明范围与校准结论澄清，不要求更多无关实验。

### [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation](https://arxiv.org/html/2604.12268v1)

v1 §3–5.3实际把接受valid与拒绝invalid分开，并以两者都通过作为pass。函数侧LLM生成input由OJ验证，buggy solutions提供错误output；repo侧SWE-bench Verified/UTBoost的fixed/buggy运行给有限reference。Table4函数更易过宽、repo更易拒绝正确行为，这是具体oracle失败方向；并非所有非法/合法程序的完备判定。Table6代码解答分数来自厂商technical report，非同harness同预算因果对照，不能采用“代码能力必与spec能力脱钩”的普遍解释。6分标准完成，仅报告受限测量协议/反证；Ch66已有verifier审计与spec validity控制权，不把该题库当普遍发布标准或假称全方法Existing。

### [SubFlow: Sub-mode Conditioned Flow Matching for Diverse One-Step Generation](https://arxiv.org/html/2604.12273v1)

v1 §3.1–3.4、§4.1–4.4：DINOv3特征按class聚簇，训练增加k条件，CFG只drop class、不drop k；部署按经验p(k|c)选子簇。ImageNet256、DiT-B/2、batch256、所设160/240epoch与50K样本验证有限Recall/Precision取舍：MeanFlow/Shortcut的Recall改善同时Precision下降。Eq6的条件均值本来可构成合法marginal velocity，均值本身不必导致精确连续ODE丢mode；所测one-step/离散路径不能证明无averaging distortion或完整coverage。5分标准仅报告具体conditioning分支及反证，不把cluster近似unimodal当形式保证，未测硬件/latency/SLO不从NFE推出。

### [Models Know Their Shortcuts: Deployment-Time Shortcut Mitigation](https://arxiv.org/html/2604.12277v1)

exact-v1 §3.1–3.4、§6.1–6.3：冻结已偏分类头，用其预测标签梯度×输入识别top-k token，mask后对比适应LoRA encoder，不需要原训练集或shortcut标注；但最终α由40个带标签support样本选择，不称端到端无监督。SST2/CivilComments/MultiNLI及受控反转分布的WGA/accuracy存在取舍，token saliency是局部预测敏感性，不证明因果或模型自知。5分标准完成，仅报告具体部署适应分支，不为toy任务替换Ch5表示/泛化论证。官方abs/v1身份同题、未见撤回；Submitted=04-14T04:43:29Z仅投稿，v1Updated=04-15T00:25:54Z与已保存公告组合支持08～09区间。

### [WebAgentGuard: A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents](https://arxiv.org/html/2604.12284v1)

exact-v1 §3.1–3.3/§4.3–4.4：guard读取screenshot/HTML而非 proposed action，独立于task reasoning；guard否决时停止，显式human override才可继续。GPT5合成训练、SFT→GRPO、VPI-Bench与两类agent的有限ASR/utility条件，不是开放环境零攻击保证。Table6 guard4B/8B耗2.15/3.24s，所测agent5.43–7.74s；只有并行且guard先完成时才不额外进入critical path，计算、资源争用和人工确认不是零成本。WebArena有utility下降，one-time确认只恢复部分。6分安全深入完成，仅报告这个有限性能/安全分支；Ch72已有可信执行gate但不把它称该classifier正确性证明。官方abs/v1同题未见撤回；Updated00:26:22Z仅组合日期依据，未改名首发。

### [Frontier-Eng: Benchmarking Self-Evolving Agents on Real-World Engineering Tasks with Generative Optimization](https://arxiv.org/html/2604.12290v1)

exact-v1 §2、§3.2–3.3：47任务以hard feasibility及objective反馈执行生成搜索；宽度/深度试验只在10-task子集、OpenEvolve+GPT-OSS120B、总evaluation budget≤256，较深链取得更好所测平均结果，不等预算token/FLOP或全部scaffold都如此。500iteration拟合将斜率约束为−1，R²不能证明普适幂律；工程求解器/模拟不当真实生产闭环。5分标准完成，仅报告搜索预算的受限负例与late-improvement差异，不采“深度永远胜宽度”或基础设施默认调度。官方abs/v1同题未见撤回；Updated00:26:52Z与本日官方批次组合支持区间。

### [CompliBench: Benchmarking LLM Judges for Compliance Violation Detection in Dialogue Systems](https://arxiv.org/html/2604.12312v1)

exact-v1 §3–§5.4：compliant turn要求同时正确rule与不违反，violated turn只要求flag，不把SGA/VDA当同一分母；CLA要求整对话全turn正确。真实seed扩写guidelines、两LLM迭代判冲突、自动缺陷注入与标签生成仍依合成有效性，非人工法务真值。Airline1400条Qwen3-8B训练、另外两domain迁移只支持所测协议，未见完整真实组织policy admission。5分标准完成，仅报告分类目标/错误归因与受限小模型评测；不把其生成的guideline标签直接作为Ch66全部合规oracle。官方abs/v1同题未见撤回；Updated00:28:35Z与既有组合支持本窗。

### [Towards Realistic and Consistent Orbital Video Generation via 3D Foundation Priors](https://arxiv.org/html/2604.12309v1)

exact-v1 §3.1–3.3、§4.1–4.4：冻结Hunyuan3D的shape denoising/geometry decoder输出global latent与volumetric projected latent views，adapter交替cross-attention给SVD共同shape条件，避免mesh抽取而不避免前置30-step shape生成；video仍50steps。8H200、80Ksteps/batch16、21frames576²、Objaverse/GSO合计250unseen objects，评价pixel quality/MEt3R与CLIP，不证明真实完整几何/物理transition；形状姿态错位由learned3Dattention处理非groundtruthidentity。5分标准完成，仅报告可迁移的representation条件例证，不为轨道演示写孤立WorldModel分支。官方abs/v1同题未见withdrawal，Updated00:28:17Z保留原字段，与本日公告组合支持08～09。

### [Self-Adversarial One Step Generation via Condition Shifting](https://arxiv.org/html/2604.12322v1)

exact-v1 §3.1–3.3/Eq9–28、§4.1–4.3：real condition经affine shift形成fake分支，以当前自产生sample轨迹训练其velocity，再将stop-gradient fake velocity用于mixed consistency。没有独立外部critic不等消除reference拟合；shared-parameter分支的统计独立和精确score前提不能从负condition scaling证明。此处只采用算法接口与所测质量/成本取舍，不采用普遍精确KL下降/GAN等价。BF16、16H800/8A100、0.6/1.6Bfull及QwenImage20B LoRA、globalbatch64限定；Table1/4有CLIP或知识slice落后，NFE不能独立证明matchedtrainingcost/生产SLO。6分标准完成，仅报告这个受限训练分支，不把多个数据/teacher预算混合当通用distillation优势。官方abs/v1同题未见撤回，Updated00:29:05Z与公告组合支持本窗，Submitted仅投稿。

### [Information-Geometric Decomposition of Generalization Error in Unsupervised Learning](https://arxiv.org/html/2604.12340v1)

实际v1§3.1–3.2/§4.3–4.6把可见分布e-flat与e-mixture平均作为三非负KL项分解条件；hidden-variable marginal一般不e-flat，代数data bias可负。ε-PCA也不直接满足e-flat，改写保持总GE只在isotropic Gaussian条件下成立，rank不是hidden width。N=64/D=96/800 Wishart样本对数值恒等式的验证不证明现代深模型generalization law。5分标准完成，仅报告这一理论适用边界，未声称Ch5已有同一定理、也不写Transformer保证。abs/v1同题未见撤回，v1Updated00:30:14Z为原版本字段，结合本日官方组合推断08～09，不将Submitted当公开。

### [CoLA: A Choice Leakage Attack Framework to Expose Privacy Risks in Subset Training](https://arxiv.org/html/2604.12342v1)

实际v1§3.1–3.2/§4.1–4.2/§5.1–5.3区分training-membership I与selection-participation I∪E，E虽没进入模型训练仍可能暴露筛选身份。知道selector/ratio的side-channel重复窗口选择不同于blackbox的embedding聚类代表性proxy；重叠窗口不自动满足独立Bernoulli假设。CIFAR/ResNet18九种selector、四保留率，与Pythia70/160M、GPTNeo125M的受限黑盒AUC/TPR5%FPR不是个人归属或DP保证。Ch72现Membership可识别性/变换家族没有这个筛选阶段privacy对象，6安全/知识缺口深入完成，已在 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) Membership 原论证中实际补入两段；root源/owner及相邻正文写后通过，处置整合。abs/v1同题未见撤回，原Updated00:30:28Z与公告组合支持本窗。

### [PrivEraserVerify: Efficient, Private, and Verifiable Federated Unlearning](https://arxiv.org/html/2604.12348v1)

实际v1III-A～III-D/Alg1–3与IV-B～IV-D：variance阈值只存部分client updates，Alg2去目标后累加已存旧updates+Gaussian，未证明其状态等价于无该client重训轨迹；原模型非线性训练历史中保留client updates本身依赖旧global weights。正文没有给出保证所需邻接、敏感度界、composition accountant及分布不可区分定理；Alg3以单fingerprint低阈值直接声明全部contribution删除，也没有桥。100client/每轮10/200round、CNN/LSTM/ResNet模拟与noise utility曲线不能补这个证明，且runtime表仅支持受限效率。6安全深入后中心保证争议隔离，不否定全部实测，不进Books；重开需合法隐私合同及fingerprint对删除对象的证明/独立测试。abs/v1同题，Updated00:30:45Z+本日组合，未发现撤回。

### [Why and When Visual Token Pruning Fails? A Study on Relevant Visual Information Shift in MLLMs Decoding](https://arxiv.org/html/2604.12358v1)

实际v1§3.1–3.2/§4.1–4.2/§5.1–5.4：以prefill anchor与decode attention相似度触发RISD，备用visual tokens由discard改为可恢复状态；CPTS用原/新union维持L步再回原集。attention变化与推理难度相关不是独立因果真值；k～2k临时集、重排/读取与此前语言KV一致性需分别验收，不称exact历史回放。L40S的Qwen3VL4B/InternVL3.5-8B，τ=.75/L=20；Table3平均38.1%比静态33.3%更多，Full swap也并非最好；Table4 TPS皆低于FastV，Qwen总延迟低但InternVL反增。precision/batch/concurrency/SLO未完整披露，不引用普遍加速。Ch23现层间保留/主动crop缺decode-step备用表示生命周期，6gap深入；已在 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 几何稳定之后实际整合备用状态/union分支，root必要来源和写后独立通过。abs/v1同题未见撤回，v2 Submitted04-15T17:43Z晚于窗口，未做无关旧新版差分；Updated00:31:36Z与官方组合支持v1本窗。

### [Compiling Activation Steering into Weights via Null-Space Constraints for Stealthy Backdoors](https://arxiv.org/html/2604.12359v1)

实际v1§4、§5.1–5.4/Eq5–12与§6.1–6.5：攻击者先有checkpoint修改权，拒绝/服从表示差异被编译到MLP down-projection，trigger keys与clean calibration keys共同决定闭式编辑。精确null空间条件能使已校准clean keys的编辑输出为零，但实际取小奇异值方向不等于严格零，未覆盖新输入；正则最小二乘也不自动精确满足trigger映射。Llama2/3及Qwen2.5 7–8B、Dolly/AdvBench受限；开头同意的keyword FR不能代替持续有害输出StrongREJECT，GSM/Alpaca也有下降，α引入隐蔽性/攻击成功取舍。6安全深入，Ch72现模型参数行为probe缺“prefix映射→表示steering编译”的具体风险分支，已实际整合 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 模型文件到Prompt Injection的行为边界，root源/owner及实际写后通过，不声称nullspace对全部clean无害。abs/v1同题未见撤回，原Updated00:31:37Z与本日组合支持08～09。

### [Reading Between the Pixels: Linking Text-Image Embedding Alignment to Typographic Attack Success on Vision-Language Models](https://arxiv.org/html/2604.12371v1)

实际v1§3.1–3.4、§4/Table1–5：SALAD1000样例、四VLM、font6～28px及10个视觉变换，Azure guardrails关闭；外部JinaCLIP/Qwen embedding的归一化L2不是被攻击模型内部安全表示。ASR由GPT4o判断，字体/模糊与ASR相关不能构成通用防御因果保证；Qwen小字体仍有23.9%ASR，text/image及旋转排序模型相关。1+2+2=5安全深入，仅报告这个输入渲染×被攻击model的受限反证，不把外部embedding接近当拒绝边界，也不为同多模态攻击主题强写书。abs/v1同题未见撤回，v2 Submitted02:42Z在截点后，未扩版本比较；原v1Updated00:31:59Z仅参与已保存批次组合。

### [Masked by Consensus: Disentangling Privileged Knowledge in LLM Correctness](https://arxiv.org/html/2604.12373v1)

实际v1§3.1–3.5、§4.1–4.3、§5.3/7：self和peer hidden states分别训练target-model正确性标签，nested stratified十折比较线性/MLP probes；disagreement仅用于测试切片，不在完美反相关子集重新训练。事实任务出现条件self advantage，math不一致，条件AUC与全样本AUC分母不同；它不证明内部自知、因果可访问或胜过所有外部观察者。Ch66 Claim Sensor/probe identity与可解码failure现文缺self-vs-peer对照和一致样本掩蔽的评价条件，2+2+2=6知识缺口深入，已实际整合 Ch66 Claim Sensor 的全样本/固定 probe disagreement 切片分账，root 必要源、真实 owner、实际两段及相邻交接独立通过；不是内部自知或全外部不可见保证。abs/v1身份一致未见撤回，原Updated00:32:03Z与官方组合支持本窗；后版不作为v1证据。

### [ReasonXL: Shifting LLM Reasoning Language Without Sacrificing Performance](https://arxiv.org/html/2604.12378v1)

实际v1§3.2–3.3、§5.1–5.2：五语言SFT后Dr.GRPO组合accuracy/language/format/repetition reward；法语MGSM在<think>首生成位置，以150源prompt平均RL state patch到base、100题测输出语言比例，层6～8显著切语言而大权重delta深层不明显。这个实际干预支持限定的功能定位，不证明所有语言/模型固定层、upper layers真正承担全部内容计算。RL小delta不等小FLOPs，BF16/vLLM16K及8192completion、8GPU训练不与SFT总预算完全匹配。2+1+2=5标准完成，仅报告局部表示与权重分账，不将相关drift写成普遍机制。abs/v1同题未见撤回，原Updated00:32:38Z参与官方批次组合。

### [On the Distillation Loss Functions of Speech VAE for Unified Reconstruction, Understanding, and Generation](https://arxiv.org/html/2604.12383v1)

实际v1§2.1–2.2/Eq2–7、§3/§4.1–4.3：frame cosine与frame-pair结构损失分别设置margin，projection-layer梯度范数比调整alignment权重。更强SSL贴合可改善理解却损重建/生成；margin允许不精确复制teacher，这是可控取舍而非三个目标同时最优。Libriheavy16k、64维40Hz latent对WavLM第23层、550K/600K/1100K训练预算不同；F5-TTS对EnCodec还换LR，综合几何平均也不是真实通用utility。5标准完成，仅报告这套语音VAE条件分支与负例，不宣称对全部多模态表示或所有任务适用。abs/v1同题未见撤回，原Updated00:33:01Z与本日组合支持当窗。

### [Preventing Safety Drift in Large Language Models via Coupled Weight and Activation Constraints](https://arxiv.org/html/2604.12384v1)

实际v1§3/Eq1–4、§4.1–4.2/Eq9–15、§5/Table1–2/§7：局部Taylor把权重与activation变化分开，固定base harmful-input covariance的小特征方向限制FFN更新，SAE refusal-feature正则限制训练中activation偏移。它说明单对象约束可能漏另一路，但有限small-eigen子空间只近似保校准X，后续h也改变，不能由此推出全部prompt安全不变。四7–9B白盒、100M-token SAE及额外harmful forward有成本；Gemma PubMedQA的HS不及SafeInstr，拒绝/SAE feature亦非全部安全真值。6安全深入，仅报告联合约束的受限机制，不采用摘要/正文的全局保持宣传；可用结果不因局部近似而全否定。abs/v1同题未见撤回，原Updated00:33:01Z参与本日官方组合，未复现实验。

### [Do Transformers Use their Depth Adaptively? Evidence from a Relational Reasoning Task](https://arxiv.org/html/2604.12426v1)

实际读exact-v1 §2、§3.1–3.3和§4。CLUTRR单token关系回答、100测试/2–10hop；patching只选top答案因同gender关系替换而改变的至多30条，不保证原答案正确。较长链可更早开始跨token混合而更晚结束，因此logit-lens的“答案早出现”与所需计算深度不是同一指标；Full SFT较LoRA更早可读出，却在长链泛化和一般LM能力上较差。LoRA/full在1000例、20epoch、answer-only目标下，11–15hop又改变sibling占比并可能有结构shortcut；不推出所有复杂任务自适应深度或线上early-exit收益。Ch5实际“从可读出到机制”及“可读出不等于可拆卸或可控制”已承载readout→干预→行为与有限跨context证据链，故已有覆盖，不追加论文名。v1 Updated00:36:29Z只作同批公开上界组合，官方abs/v1身份一致，当前未见撤回说明。

### [A Bayesian Perspective on the Role of Epistemic Uncertainty for Delayed Generalization in In-Context Learning](https://arxiv.org/html/2604.12434v1)

实际读exact-v1 §2.3、§3.1、§4及§5的理论对象。六层decoder、512dim/4heads在隐藏(a,b)模算术上交叉区分seen/unseen任务与输入；四seed，IVON全参数近似posterior与post-hoc last-layer Laplace不同，EU由mean predictive entropy减mean entropy定义。EU下降与task-diversity的grokking转折相关，但增加test-time context时EU先升后降，不能把低EU当跨分布正确性证明；标签噪声改变AU/EU也不识别唯一原因。§5明确转为Bayesian linear regression而非完整Transformer保证。仅保留受控诊断分支与方法条件，不新增Books普遍规律；硬件、precision、线上batch/concurrency/SLO在所采用诊断段未披露，不报告生产性能。v1 Updated00:37:02Z，官方abs/v1身份一致，无当前撤回说明。

### [Scaling Exposes the Trigger: Input-Level Backdoor Detection in Text-to-Image Diffusion Models via Cross-Attention Scaling](https://arxiv.org/html/2604.12446v1)

安全深入实际读exact-v1 §3/Theorem3.1、§4.1–4.5、§5.1–5.3和Table1–3。Defender可读模型参数及内部响应，有1000 benign calibration，不是黑盒无数据检测；固定16×16 query的up/down cross-attention响应，另同时缩放self-attention，五个scale{0.2,0.3,7,10,20}和首五denoise步构成MSE特征，one-class encoder/半径判异常。Theorem仅在两类局部二阶系数不同的条件下分离类均值，不保证单样本detect，也不涵盖远离1的全部实际scale。SD1.4/MS-COCO与五种attack有限评价，EvilEdit/IBA ACC仅65.1/64.9；更多benign或全部layer反而降效，阈值/AUROC与balanced 500/500协议不同于线上attack prevalence。代价包括reference+多次probe、encoder训练和distribution drift；硬件、precision、线上长度/batch/concurrency/SLO未完整披露，不转述部署无开销。有限主动诊断可报告，不把一次AUROC支持通用后门清除或独立安全证明。v1 Updated00:37:37Z，官方abs身份一致，无当前撤回说明。

### [HazardArena: Evaluating Semantic Safety in Vision–Language–Action Models](https://arxiv.org/html/2604.12447v1)

安全深入实际读exact-v1 §3.2–3.3、§4.1–4.4/Tables1–2。固定interaction template、layout/seed与motor要求，safe/unsafe twins改变actor–target语义和instruction；定义attempt(0.10m interaction region)→pre-IPE commit→terminal success，commit在attempt之后才计。四VLA在600 safe trajectories/六task上比较early/final checkpoint；unsafe SR低可能是slippage，不等refusal，stage commit可逆转terminal安全排序。仅模拟、对象变化仍可能改变物理细节，不能称唯一语义因果已完全分离；L1规则在构造场景上有效不是开放安全，Qwen3VL32B judge对Property零recall/Fire误报，SOL只是诊断/部分缓解。Ch26已有physical controller/semantic攻击与最终outcome，但未见motor-feasibility matched twins+stage危险进展的共同有效性条件；Ch66已有generic response/过程–结果分账，本轮已在 Outcome Witness 中实际补入能力匹配和 first-hit 阶段分账；`PLATFORM-EVALUATION-SYSTEM` 为唯一 owner，Ch26仅交接安全 authority。root 必要源与实际两段前后交接独立通过，未把 commit 当内部意图或真实物理安全证明。v1 Updated00:37:40Z，官方abs/v1身份一致，无当前撤回说明。

### [Latent-Condensed Transformer for Efficient Long Context Modeling](https://arxiv.org/html/2604.12452v1)

深入实际读exact-v1 §4.2–4.4/Alg1、§5 Tables2–3与AppendixA.2必要证明。远history组query-aware pooled latent+max位置anchor、近w保留、decode每g步添代表；不同于只压latent维度，减少token数亦改变softmax质量。Theorem1以δk/δv=0声称误差0，但远组g条在实际LCA只占一项，A.2后将Z′重新写成所有token的exp和，遗漏group multiplicity。取g=2/w=1、q和三key全0，远两value=1/近value=0，代表value1：full输出2/3，LCA1/2，δk=δv=0而误差1/6，直接违反所写界。若添加log(g) mass校正或修改目标/假设才可能重证，当前算法未作该校正。该反例不否定其近似实现和H200/DeepSeekV2-Lite受限LongBench/RULER结果；均值质量和局部相对deviation也不证明max误差或无损。中心理论隔离，不入Books；重开需作者一致Alg/公式/证明，不要无关benchmark。v1 Updated00:38:08Z，official abs身份一致，无当前撤回说明。

### [CIA: Inferring the Communication Topology from LLM-based Multi-Agent Systems](https://arxiv.org/html/2604.12461v1)

安全深入实际读exact-v1 §4、§5.1–5.2、§6.1–6.4及Limitations。所谓black-box是仅外部query，但第一阶段要求Agent复制predecessor历史、按字段聚焦并review predecessor，再从最终文本分离各输出及顺序；非无需泄漏即可观察内部trace。MiniLM表示分bias/debiased子空间，TC与重构训练后用GPT5 top-k inferred-edge弱标签/剩余pair平滑negative，similarity和文本顺序推edge；弱标签不是真实结构，方向假设限DAG。三种generated topology×四任务各100，groundtruth为受控框架配置，recall/ROUGE对trace还原不是真实逻辑trace认证。Adv-query任务accuracy相近不能证明内部策略与通信完全未变或攻击不可检测，sharedLLM/task导致相关亦不等真实edge。仅保留output-exfiltration→条件拓扑诊断的具体威胁，未披露生产query/SLO预算不报线上保证；v1 Updated00:38:26Z，official abs/v1身份一致，无当前撤回说明。

### [Meet Dynamic Individual Preferences: Resolving Conflicting Human Value with Paired Fine-Tuning](https://arxiv.org/html/2604.12479v1)

实际v1§3.1–3.5/Eq3–6、§4.1–4.2/Table2及AppendixF.4–F.6。Eq3是两个偏好条件的普通cross-entropy加权和，未含pair interaction或额外smoothness约束；若独立SFT使用同两侧样例、权重与batch，目标及梯度相同。Proposition2却宣称配对必然严格缩小anchor covering radius及Lipschitz常数：对相同anchor集合覆盖半径与是否配对无关，常数loss也不可能严格缩小零Lipschitz。F.6只给“encourages/empirically”的解释，不补严格结论；Eq6另假设loss∈[0,1]，没有把Eq3未截断的CE接入该条件。三种3–8B模型/两个价值题库及GPT4o开放回答评分是受限经验，不否定其结果，但不能证明配对形式自身有新泛化保证或优于预算相同条件SFT的原因。5分因中心理论需要定点深入后争议隔离；不往Books写新loss理论，重开需一致objective、anchor/预算matched对照与严格界的假设/证明修正。official abs/v1与HTML题名一致；Updated00:39:05Z只与已保存公告组合提供本窗上界，无当前撤回说明。

### [An Ultra-Low Latency, End-to-End Streaming Speech Synthesis Architecture via Block-Wise Generation and Depth-Wise Codec Decoding](https://arxiv.org/abs/2604.12438v1)

官方abs/v1完整题摘与身份已读，v1 Submitted04-14T08:28:36Z保持投稿原义；库存Updated04-15T00:37:19Z参与官方公告批次组合，不改名为首发。题摘的modified FastSpeech2→Mimi32级RVQ depth-wise依赖与time-block输出，显示可能有具体执行/音质取舍，故保留5分待证据，不因语音领域排除。HTML未取得、官方PDF-v1网页Cache miss；本轮再尝试官方arxiv.org与export.arxiv.org精确PDF（20～25s有界）均HTTP406。尚未读必要方法、block buffering、codec-depth条件和模型/硬件/精度/长度/并发/SLO，不能把48.99ms或10.6×当已核结果，也不能声称标准审阅完成。精确缺口隔离，不入Books；恢复条件为该v1可读PDF/作者同版本正文的§方法及§评价，不要求全部版本或另一篇语音论文，后续只重开此项。

### [Calibrated Confidence Estimation for Tabular Question Answering](https://arxiv.org/html/2604.12491v1)

实际读§3.1–3.3、§4、§6.3及AppA。四种无内容删除的序列化以temperature0各运行一次，把回答一致性作为confidence特征，再按表结构学习监督校准；格式agreement不是答案正确证明。WTQ/TableBench、五provider/model组合、严格及fuzzy答案匹配限定结论，WTQ可能污染，部分DeepSeek对照缺失、GPT-4o WTQ仅500项；四次推理与校准标签不免费。此具体测量分支保留报告，Ch66已有clean twin/扰动须保持语义与稳定性不等正确性原则，不把一个受限format信号提升为通用置信度方案。

### [Latent Planning Emerges with Scale](https://arxiv.org/html/2604.12493v1)

实际读§2、§4.1/4.4、§5.3–5.4。所称规划不仅未来词可线性读出，还要求干预该表示既改变未来词又让已生成前文更许可这个词。Qwen3有限article/verb/gender任务的feature steering提供条件性双向证据；Qwen32B诗歌虽能改变未来韵词，前文许可控制却未支持同样结论。少数/多数token效果不对称、人工任务与feature选择限制外推；保留报告中的干预阶梯，不将更大模型或future token探针当通用长程Agent规划保证。

### [Safety Training Modulates Harmful Misalignment Under On-Policy RL, But Direction Depends on Environment Design](https://arxiv.org/html/2604.12500v1)

实际读§3.1、§5–7.3、§9及AppA.2。三种模拟用户环境用0.5–14B十一模型、LoRA GRPO300steps/600samples/三seeds，reward与评价judge分开；逐步改变role、显式脆弱性与用户style后，规模–harm相关方向改变。消融累积且severity并未单独控制，同规模base/chat仍含其他训练差别；不能照作者强措辞把所有差别唯一归因于安全训练。静态安全benchmark/初始rollout不通用预测max-over-training HEX gap，但此指标和模拟反馈也不是部署风险真值。Ch31已有simulator/judge coupling与独立环境发布门槛；该有限反证保留报告，不把三环境规律写作所有RL的安全定理。

### [CoD-Lite: Real-Time Diffusion-Based Generative Image Compression](https://arxiv.org/html/2604.12525v1)

实际读§3–6。34M/700M生成与codec对照中，generation-oriented预训练的收益随容量不同，不能由大生成器经验直接选小codec；global attention直接改DWConv先损质量，借大teacher蒸馏才恢复。约40M分支以L1/LPIPS、commitment、DMD和GAN联合训练，FID、DISTS与bitrate各有评价对象；A100高分辨率结果仍受训练分辨率、patch指标和未披露SLO影响。保留条件性架构/蒸馏取舍，不将局部时延或FID表当普遍高保真实时压缩保证。

### [MODIX: A Training-Free Multimodal Information-Driven Positional Index Scaling for Vision-Language Models](https://arxiv.org/html/2604.12537v1)

实际读§3–4/Table4。covariance entropy与模态对齐得分决定视觉位置stride，改变RoPE相位而不改权重；所谓距离衰减与stride反比分配不是任意Q/K和振荡RoPE的定理。Qwen/InternVL任务收益和最佳alpha依slice变化，VideoMME长视频不是统一大幅提升；Eq18首视觉位置与文字说明也存在边界差异。将它作为需固定位置/selector/model联合身份的启发式报告信息，不采用普遍information-budget保证或新增书稿owner。

### [FABLE: Fine-grained Fact Anchoring for Unstructured Model Editing](https://arxiv.org/html/2604.12559v1)

实际读§3.1–3.4、§4.3/4.5及Tables1–2。先用目标fact输出求residual方向并分摊到选定层，再在第7层调整体叙述；第二阶段继续约束fine-QA、prefix和无关样本表示，避免只让整段更流畅却遗漏事实。实测Llama3-8B/Qwen2.5-7B的第4–6/7层、5×seed-QA与20Alpaca保持样本限定机制，不证明所有模型浅层存fact、深层仅叙述；文本重叠/HR不是世界真值，删阶段的相反退化也非全预算匹配。保留受限编辑分支，暂无把此固定层配方采入长期训练主线的证据。

### [IDEA: An Interpretable and Editable Decision-Making Framework for LLMs via Verbal-to-Numeric Calibration](https://arxiv.org/html/2604.12573v1)

实际读§3.1、§4.3–4.5、§5/Table1。LLM先估二元factor，外部带pair interaction的logistic model与verbal mapping联合拟合，未知factor用条件联合采样；parameter/AME编辑控制的是该显式函数，不是神经知识或世界因果。完整factor与稳定单调verbal mapping是前提，50次采样对近似LLM分布的无偏不等真实分布无偏；移除factor还须处理所有interaction。Qwen4/8/32B五任务结果并非全slice胜，模型内相对重要性验收不是事实calibration证明。仅报告具体可编辑decision分权，不泛化为高风险决策保证。

### [Relaxing Anchor-Frame Dominance for Mitigating Hallucinations in Video Large Language Models](https://arxiv.org/html/2604.12582v1)

实际读§3、§4.1–4.2/Tables2–4。黑帧输入仍出现集中anchor，只支持位置偏置诊断，不证明所有幻觉唯一来自anchor；prefill统计确定frame deficits，decode按选定层给视觉attention logits补偿，不修改encoder也不还原真实证据。四个7–8B模型、默认八帧greedy协议限制结论；LLaVA的VideoHallucer pairedOverall与Qwen的hallucinated-only accuracy是不同分母，部分EventMix退步，100样本三次效率测试不等生产SLO。保留报告，attention质量与答案grounding仍须独立验收。

### [KumoRFM-2: Scaling Foundation Modelsfor Relational Learning](https://arxiv.org/html/2604.12596v1)

exact-v1 §2–3、§4.1/4.4–4.5：按样本时间构造关系子图、较早注入任务、交替row/column及FK/cross-sample attention；SQL下推或mmap抽图把上下文构造移到数据查询路径。41任务协议允许train+validation作上下文且截至10K，和完全监督训练不等预算；图邻域由4扩大可使driver-dnf退化。500B-row容量与20M lookup工程披露不是本次复现实测，未给尾SLO/精度并发完整合同，stateless也不证明tenant授权。保留关系表示/上下文构造分支，仅报告，不泛化为文本RAG或生产收益。

### [CODO: An Automated Compiler for Comprehensive Dataflow Optimization](https://arxiv.org/html/2604.12618v1)

exact-v1 §IV–VII/§VIII及IX-D：静态循环permutation map找粗细粒度dataflow violation，重排后仍不可消除的冲突用ping-pong double buffer，HBM burst与并行度调整后重新验证数据流。这给出具体的streaming执行分支，而不只是HLS速度排行。证据限定Alveo U280、300MHz、Vitis/Vivado2023.2、静态affine循环；SSA/type和原始程序testbench不是全输入语义证明。IX-D明确artifact evaluation未重做板上结果，仅提供GPT2 bitstream/报告；本轮也未运行它。只报告条件编译机制，不把合成周期、CNN/GPT2板测最高值推成一般LLM serving收益。

### [KnowRL: Boosting LLM Reasoning via Reinforcement Learning with Minimal-Sufficient Knowledge Guidance](https://arxiv.org/html/2604.12627v1)

exact-v1 §3.1–3.2/§4：验证解分解成knowledge points，再以8×32采样correctness决定子集；单删有利而联删有害，CSS只枚举受限候选并仍保留no/full KP备选。§3.2.1式的删除集合条件与文中nonessential解释不完全一致，因此不采用其符号为统一规范；rare交互也不是排除交互的证明。Nemotron1.5B、约8.8K题、64H100/13天、最大24K rollout的训练与离线oracle成本均保留；带提示推理和无提示是两个协议。Ch33已有provenance-bound hint/no-hint gate，但本算法仅报告具体依赖反例与受限搜索，不据此强改通用训练选择。

### [Calibration-Aware Policy Optimization for Reasoning LLMs](https://arxiv.org/html/2604.12632v1)

exact-v1 §2–4、§5.1–5.3：由正确/错误pair的长度归一化log-prob gap构造logistic surrogate，再把pair导数写入每个回答advantage，reference PPL quartile另mask极端正确/错误样本。固定分布、二元标签下surrogate的一致性不等于每步on-policy AUC单调，更不证明reward-only必然每次恶化；mask及采样也改变实际目标。实验证据限Qwen2.5-Math1.5B/7B、DeepScaler20K训练/240验证、六数学benchmark、test mean@16与precision-coverage。PPL不是过程正确性oracle、AUC不是绝对概率校准；仅报告该目标分支与局部反证，不把图中Pareto排序推广部署。

### [PromptEcho: Annotation-Free Reward from Vision-Language Models for Text-to-Image Reinforcement Learning](https://arxiv.org/html/2604.12652v1)

exact-v1 §3.1–3.3/§4.1/4.3/§5：冻结Qwen3VL32B看到生成图后，对原prompt token作teacher-forced平均CE作为reward；无需新preference-RM训练不等无需scorer算力。100K caption训练与2K同源holdout由该VLM生成，pairwise评估又用Gemini3Flash，不构成独立truth。Z-Image/QwenImage2512的LoRA64、32H20、约100/200h、训练1024/CFG3.5/30step与评价CFG4/50step限定比较；部分属性/分数反收益仍在。保留该likelihood reward分支，仅报告，不采用更强VLM必然升级reward或无标注即无偏的保证。

### [Token-Level Policy Optimization: Linking Group-Level Rewards to Token-Level Aggregation via Sequence-Level Likelihood](https://arxiv.org/html/2604.12736v1)

exact-v1 §2.1 Eq1、§3.2 Lemma3.2/Theorem3.1、AppC Eq12–13：熵对logit的正确导数为−p_i(log p_i+H)，Eq1符号相反；AppC Eq13丢失log p后右侧−Σp∇log p恒0。uniform二分类∇H=0，无论存在正/负advantage都不满足该lemma的strict内积符号；故不能采用mask的普遍理论保证。§4.1/Table4仍给Qwen2.5-7B/Qwen3-14B、DAPO-MATH、64prompt×8、8次更新、max8192、两seed及不同72/132step经验；步骤/平均生成时间不等端到端匹配compute。隔离中心证明，不否定几何平均ratio/局部消融程序；需修正熵公式、完整多action假设与mask桥才重开，Books不采用。

### [GF-Score: Certified Class-Conditional Robustness Evaluation with Fairness Guarantees](https://arxiv.org/html/2604.12757v1)

exact-v1 §3.1–3.4/§4.2：g(x)=√(π/2)·positive softmax/sigmoid margin被直接称input L2半径下界，但此处未约束分类器Lipschitz/smoothing/生成器到input距离的桥。二类logit f0=K(ε−x)、f1=−K(ε−x)，在x=0、Kε大时margin近1而边界距ε可任意小，反驳无条件input半径解释；不因此否定原始GREAT在其额外条件下可能成立的结论。按class加权平均分解与Hoeffding只保证score估计，不建立扰动鲁棒性；调温对clean accuracy的Spearman拟合也不是attack certificate。22个RobustBench模型/CIFAR10+ImageNet经验profile可保留，但本轮不作Books正面保证；需明确空间、平滑/正则条件及认证映射后重开。

### [SOAR: Self-Correction for Optimal Alignment and Refinement in Diffusion Models](https://arxiv.org/html/2604.12617v1)

exact-v1 §2.3 Eq6–15/Alg1、§3.1–3.5：从clean z0起，当前模型一次stopgrad CFG Euler rollout后用同z1再加噪为z′，辅助监督(z′−z0)/σ；区别于只采forward-noise SFT和terminal-reward RL。clean anchor构造局部纠偏target，不证明任意偏轨迹状态的唯一Bayes真值或覆盖完整推理分布；额外前向/N/noise weight和坏caption/训练分布仍有成本。SD3.5Medium512、286119pairs、10K steps；reward-specific子集上fullparam vs LoRA FlowGRPO/128GPU同steps并非全compute匹配，freshnoise也有slice排序变化。已实际整合 `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 连续 diffusion 基础与离散迁移之间的训练 support 分支；root 必要原文、owner及实际两段前后交接独立写后通过，保留局部构造、总训练成本与旧 SFT/RL 共存边界。


### [Chain-of-Models Pre-Training: Rethinking Training Acceleration of Vision Foundation Models](https://arxiv.org/html/2604.12391v1)

exact-v1 §3.1–3.2/§4/§5.3–5.4：小模型参数直接填入大模型、深度复制，特征投影后作反向尺度的distillation，家族成本同时计算各成员，而不是只比较末端大模型。每对先验证质量后放宽epoch预算，最小成员与邻接倍率存在数据相关sweetspot；加更多成员并不无限改善。LaCLIP的CC3M/Merged15M增强语料、ViT/Swin、45任务与A10080GB实验中，“lossless”定义允许低于0.5%准确率下降，不是权重/行为等价，FLOPs也不是所有硬件wall-clock。保留家族级训练目标的受限分支，尚不把CLIP链选型推广到语言预训练或作为Ch28通用配方。

### [Three Birds, One Stone: Solving the Communication-Memory-Privacy Trilemma in LLM Fine-tuning Over Wireless Networks with Zeroth-Order Optimization](https://arxiv.org/html/2604.12401v1)

exact-v1 §IV–VI/§VII：shared seed与两次扰动forward生成ZO方向投影，模拟无线聚合以channel inversion功率和噪声共同控制误差/隐私；sign分支还需符号翻转率条件。DP结论绑定投影裁剪敏感度、噪声和多轮组合，收敛使用PL/smooth与翻转率小于二分之一等假设，不能从标量或bit反馈推出免费隐私/同步。五client、OPT125M、1000样本、8000轮、epsilon5/delta.01，EPYC7742+四A10080GB、SST2/SQuAD属于模拟合同，不是实际无线LLM部署；本次不将条件保证写成Books普遍安全判断，保留仅报告，未复现实验。

### [Beyond Transcription: Unified Audio Schema for Perception-Aware AudioLLMs](https://arxiv.org/html/2604.12506v1)

exact-v1 §2–3/§4.3/§5.2–5.4/AppE–G：transcription、paralinguistics、events作为显式监督字段，projector阶段后联合instruction目标与GRPO，encoder冻结。相同synthetic source与架构、无GRPO的caption/JSON比较为48.4/54.8 perception，支持target覆盖与格式设计值得核验；并未隔离JSON语法、标签密度与所有训练成本，因此不采正交槽必然解耦或理解/生成无trade-off。Qwen2.5-7B+AuT，English/Chinese、primaryspeaker范围，ASR改成JSON有小WER代价，多speaker重叠仍限制。Ch23现有“transcript不代替声学”是表示/读取边界，尚缺训练标签支持这条条件分支；已在 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 语义锚点之后实际补入训练target分支；root必要来源/owner和实际写后通过，处置整合。

### [Whole-Body Mobile Manipulation using Offline Reinforcement Learning on Sub-optimal Controllers](https://arxiv.org/html/2604.12509v1)

exact-v1 §IV-B/§V-C–F/§VI：WBC随机化轨迹重标为H步return与t+H successor，IQL只评价数据内chunk，再以优势加权diffusion imitation抽策略。22/23维proprioception+object-joint状态不是视觉语言表示；真机Euler joint-position接口、H16与三帧陈旧state的异步推理及EMA均有额外条件。Tiago40Hz、两任务各25次、marker与pose结果不同，snap-off handle仍承担保护；50模拟episode的CI/成功条件时延不等通用控制SLO。保留chunk critic和controller prior的具体训练分支，不能推广为无训练数据、无状态oracle或真机安全，标准仅报告。

### [From Myopic Selection to Long-Horizon Awareness:Sequential LLM Routing for Multi-Turn Dialogue](https://arxiv.org/html/2604.12385v1)

exact-v1 §3–4/§6.1–6.4：路由action改变后续用户状态，用checklist累计reward的MCTS轨迹训练，并在部署检索相似future states而不在线search。搜索监督/检索消融有受限增量，不把MCTS模拟oracle等同真实上界或检索相关等同未来正确。Qwen3-Max兼用户模拟与reward，10simulations、最大8轮、Qwen0.5B encoder后三层训练、4090D和三语料；offline搜索/评价成本不能由0.01秒检索抵消，所谓KV切换cost是模型定价而非真实缓存迁移实验。本次只报告受限序贯选型，不据同源模拟器成功率改变生产路由结论。

### [Contextual biasing for ASR in speech LLM with common word cues and bias word position prediction](https://arxiv.org/html/2604.12398v1)

exact-v1 §2.2–2.3/§3–4：常见词的部分发音作bias cue，tagger使用encoder与LLM特征定位目标词并辅助CTC；推理用户可不提供G2P标记，但训练cue构造仍靠音素词典/匹配，不是全流程无语音知识。Granite8B、冻结主encoder、Q-former/LoRA三epoch英语ASR，10/200词bias list与四语料分别计bias/nonbias WER；低频词改善不等全部WER大幅改善，phoneme topline仍可更强。保留具体输入接口与训练监督分支，不推其他语言/实时系统，标准仅报告。

### [LASA: Language-Agnostic Semantic Alignment at the Semantic Bottleneck for LLM Safety](https://arxiv.org/html/2604.12710v1)

exact-v1 §3–5/Limitations：用semantic与language silhouette差最大层定位候选表征，冻结base训练小MLP的BCE安全logit，再以logit条件化KTO式目标。聚类形状与MMLU相关不是唯一因果瓶颈，解释器能分类也不证明生成必遵守；base更新后还需考虑表征变化。en/zh/ko训练、十语言评估，Llama/Qwen7–32B、四A10080GB和GPT4o judge范围中，部分utility slice退步；有限早/晚层对照不能定普遍层位置。安全例外已读必要机制/反证，仅报告条件性对齐，不把语言不变语义或全部拒绝作为Books保证。

### [Understanding and Improving Continuous Adversarial Training for LLMs via In-context Learning Theory](https://arxiv.org/html/2604.12817v1)

exact-v1 §4.1–4.4/Theorem1–2/§5：LSA-E的线性regression、对称初始化、gradient-flow surrogate上界解得到embedding谱条件；embedding扰动和原始input suffix风险不是同一威胁。§4.2 onehot类比不把该定理自动转成非线性LLM保证。谱方差正则用于六个2–8B模型LoRA CAT经验，但baseline/ER的alpha和cutoff也变，不能将比较全归因于正则。100 safety prompts、六攻击Avg@5与Llama70B评判，部分ASR更差；Table3计算时间增加，不能照录“无显著代价”。仅报告条件理论和受限启发，不据此写入普适安全bound，未复现。

### [OSC: Hardware Efficient W4A4 Quantization via Outlier Separation in Channel Dimension](https://arxiv.org/html/2604.12782v1)

exact-v1 §2–3/§4.1–4.2：离线每group通道索引决定zero/extract，低比特base与紧凑16bit补偿GEMM相加，W2的低聚集区回FP8。三个Pile序列各512token、G32、Qwen3-8B/30B-A3B四task评价；30B动态保护均值高于静态保护，未普遍无损。Table2只披露FP16/8/4吞吐比例与GEMM尺寸，设备型号、端到端latency/concurrency/SLO未披露；不从局部cycles推线上速度。Alg1集合union与mode的频率实现需说明，但不据此否定全部结果。Ch49混精度/Numeric Plan承担通用执行验收，本次仅保留受限static通道执行方案，不采默认全模块静态可用的主张。

### [VFA: Relieving Vector Operations in Flash Attention with Global Maximum Pre-computation](https://arxiv.org/html/2604.12798v1)

exact-v1 §3.1/Algorithm1、§4/§5.2–5.5：signedabsmax key-block摘要预估每query的shift，先处理sink/local并更新真实rowmax，其余块冻结shift，仍累计全部block的分母与PV。实数域相同shift可约去，关键新风险是有限精度overflow/rounding，不应与另行VSA删块混称完全相同的近似。§4仅给相对pipeline吞吐和operator分账，型号/productionSLO未披露；Qwen/Llama的greedy任务条件及HumanEval回退不支持普遍等质量。Ch14已有IO tiling而Ch49现Numeric Plan未明确此vector-bottleneck分支，6分gap深入，已实际整合 `INFER-TENSORRT-LLM` Ch49 数值验收→分布诊断交接的两段；root 必要源、实际正文与相邻交接独立通过，不采用完整 rowmax 等价、普遍质量或 SLO 保证。

### [RePAIR: Interactive Machine Unlearning through Prompt-Aware Model Repair](https://arxiv.org/html/2604.12820v1)

exact-v1 §3/§4.2 Eq3–9/§5.1：Watchdog识别意图，Surgeon生成参数编辑；但Eq8的正则逆不是一般Moore–Penrose逆，X=1、O′=1、lambda=1时XWnew=.5，不满足Eq6的精确映射。三矩阵非线性MLP与Eq5整层线性化的桥也未建立；因此隔离exact preserve/删除保证，不否定受限refusal结果。Llama3-8B、1K Bio/1K MMLU/2K syntheticprofiles、200refusal与retainbuffer、free-form而非标准MCQ、TinyStories PPL均限结论；ROUGE下降不证明信息删除，程序运行成功不证明权限或编辑安全。需要逐projection有效输入、正则残差与实际保留目标的明确实现/修正后定点重开，不入Books。

### [Challenging Vision-Language Models with Physically Deployable Multimodal Semantic Lighting Attacks](https://arxiv.org/html/2604.12833v1)

exact-v1 §3.3/§4.1–4.4：遗传搜索三角光的几何/颜色/透明度，数字参数转为手电、透明色片和遮片；物理评价是固定tripod的5–7秒视频与帧级ASR，不能等同动态robot任务安全。GradCAM移动只支持相关观察，不证明唯一因果机制；提高透明度/半径可增强攻击却更接近广域遮挡、降低隐蔽性。CLIP分类与LLaVA/BLIP/Flamingo生成协议不同，caption/VQA展示不构成通用鲁棒度；本轮仅报告这一实际物理扰动分支，不为Ch72增加普遍保护保证，未复现实验。

### [UniMark: Unified Adaptive Multi-bit Watermarking for Autoregressive Image Generators](https://arxiv.org/html/2604.11843v1)

exact-v1 §3.2–3.6/Alg2/§4.1：key×position分组，message零bit取red集合，BCH纠错后用green比例解码；但Alg2先以全序列green比例作单侧zero-bit gate，再解message。全零payload的线性BCH码全零，理想red替换使green比例0，于是watermarked image直接被gate拒绝，不能支持任意message检测。Theorem1的CLT仅渐近，N=1、gamma=.5、alpha=.05的FPR为0而非等于alpha；不采用精确有限样本保证。三AR模型、256分辨率、5000ImageNet类条件及JPEG/crop等实验仍可保留，但不证明密钥安全或任意payload鲁棒。需要payload-aware统计、明确finite-sample条件与decode-retokenize有效性桥后定点重开，不入Books，不否定全部实验。

### [When Self-Reference Fails to Close: Matrix-Level Dynamics in Large Language Models](https://arxiv.org/html/2604.12128v1)

exact-v1 §4/§5.3/5.6–5.8/§6.5：300prompt、30matchedpairs、四模型与106谱/activation指标显示nonclosing与grounded自指有区别，但分组探索后复测共享prompt设计，不是严格独立replication；部分模型指标符号反转，70B又缺27指标。单层patch只局部改善、contradictory词汇heuristic非事实真值，AUC不证明内部自知；Jacobian到matrix-semigroup不可判定是conjecture而非已证机制。A100/H10080GB约40GPUh、温度0/.3/.7限定结果。仅报告受限谱诊断/负面边界，不把该现象写成Ch5/66通用能力解释；未复现实验。

### [KoCo: Conditioning Language Model Pre-training on Knowledge Coordinates](https://arxiv.org/html/2604.12397v1)

exact-v1 §3/§4.1–4.4/§5.1–5.4：把Source、Content、Stability文本前缀加入文档，mask前缀loss，让后续token在标签条件下学习；标签来自外部模型而不是真值。1.6B/8B DCLM tokens及0.3/0.6B从头训练、4×A80080GB的十任务评价属于受限条件；三标签消融差异很小，20fact/20opinion的PCA不证明正交解耦。TruthfulQA的source/noise条件差异支持标签条件化值得核验，却不证明来源能判事实或所有幻觉减少；弱BERT标签器对照也不能证明标签完全准确。仅报告这一训练支持分支，不因元数据标签替代普遍truth或因果解释。official abs/v1同题无撤回，原v1Updated00:33:58Z只与公告组合支持本窗，不单作首发。

### [From Attenuation to Attention: Variational Information Flow Manipulation for Fine-Grained Visual Perception](https://arxiv.org/html/2604.12508v1)

exact-v1 §4.1–4.4/§5、Table3：训练posterior读取(V,Q,A)，部署prior只能读(V,Q)，KL连接两者；Gaussian潜变量渲染空间GMM，从中层特征产生视觉概率偏置，加入深层attention概率后按visibility重新归一化，不是给hidden state直接加内容。7B/Vicuna、336×336的LLaVA及CoVT受限评价显示选层/patch范围重要，Full-Seq与Deep-Only并非最好；同参数量不代表训练、分辨率、全部预算matched。attention变化不能证明深层信息普遍不可逆丢失，回答标签也不可用于部署posterior。仅报告具体特权训练→推断prior分支，未复现、不给端到端SLO保证；official abs/v1身份一致，Updated00:40:52Z与已保存组合支持本窗。

### [Every Picture Tells a Dangerous Story: Memory-Augmented Multi-Agent Jailbreak Attacks on VLMs](https://arxiv.org/pdf/2604.12616v1)

以官方PDF-v1 §3/§4.1/§5.1/§5.4及Table5为证据，PDF首页与abs/v1一致；旧库存摘要和HTML摘要表述不同，未借后版覆盖原始PDF。自然图片不修改，攻击者通过视觉anchor、文本意图伪装、外部embedding筛选和跨图experience memory迭代；proxy embedding的可分性不是受害模型内部拒绝空间保证。5,000 COCO/Qwen3-VL-Plus/R=20，Qwen3Guard的any-Unsafe定义ASR；平均轮数只在成功子集，100-image子集依据全局成功比例选择，不能把Table5或移动平均当独立因果/随机完整样本。证据足以反驳“图片本身无害即可降低整个多轮请求风险”，不证明所有模型、任意budget或防御优劣；仅报告具体安全边界，未验代码。v1Updated00:47:23Z与公告组合支持当窗。

### [GeoAlign: Geometric Feature Realignment for MLLM Spatial Reasoning](https://arxiv.org/html/2604.12630v1)

exact-v1 §3–5/Table1/4：VGGT layer12与20在方向/路径任务排序反转，提出后12层feature bank、每层Norm共享projector、原视觉patch查询top2后residual注入LLM前。Qwen2.5-VL3B与冻结两vision encoders、460K单epoch、8×H800/BF16、batch64的控制支持该具体路由分支，不证明任何single layer均不充分。Table4 dynamic并非每slice最好，Top3、多层注入及复杂gate也有回退；bank/routing额外计算不能凭4B参数量称同成本优于更大模型。仅报告层/任务匹配与稀疏选择的受限证据，不把“越深越专化”泛化为全部空间表示定律。abs/v1同题，Updated00:48:04Z与组合支持本窗。

### [FeaXDrive: Feasibility-aware Trajectory-Centric Diffusion Planning for End-to-End Autonomous Driving](https://arxiv.org/html/2604.12656v1)

exact-v1 §4.1–4.3/§5.1/§5.3、Table3–5：直接预测clean trajectory，平滑/arc-length导数计算曲率，speed-conditioned阈值加训练penalty；推断drivable-area guidance与后训练reward读取同一轨迹对象。InternVL3-2B冻结encoder，NAVSIM、IL100epochs/4×A800 BF16及GRPO1epoch/8×A800；guidance改善区域指标却使曲率violations反升，score-only GRPO也可能恶化曲率，不能用单PDMS证明物理可行。该benchmark为非reactive模拟评价而非实车安全；阈值/地图正确性、模型误差与控制执行仍未证明。仅报告这一约束冲突/对象选择实例，不采用作者“closed-loop”措辞为现实闭环保证。官方PDF本次读取失败，HTML与abs/v1同题/日期，可核必要方法与指标；Updated00:49:51Z只与组合支持本窗。

### [Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning](https://deepmind.google/blog/gemini-robotics-er-1-6/)

官方发布的high-level reasoner调用Search、VLA或自定义工具；仪表任务用zoom/point/code辅助读数。Fig1明确instrument采用agentic vision而其他任务关闭，single-view/multiview使用不同样例，不构成camera数量的因果对照。机制披露停在调用流程，未公开训练/模型内部增量、硬件/precision、concurrency或control SLO，不采用“safest”宣传为物理安全。Ch26“Grounded language 是可消费观测，不必成为控制关键路径的生成物”及slow reasoner/fast controller已经承载此分层；这里只报告发布与评价可比性限制，不造新的Books机制。datePublished原值04-14T16:00Z落窗；04-20更新model card不反推为当窗证据。

## 5. 缺口与下一步

下列外部材料、日期身份与公式争议均为终态保留项，不支持正面证据、Books 采用或无遗漏断言；重开条件限各项所列的精确正文、公开上界或作者修正，不保留普通可执行审阅待办。

已冻结123项，22整合、5已有覆盖、78仅报告、17争议、1必要正文精确隔离。普通待办为0，独立日级验收通过。22项均为真实正文整合并通过非作者写后核；本轮八项在 Ch72/23/66/24/49 原论证中落笔，必要来源、真实 owner、实际正文与相邻交接均经 root 通过，未以机器通过替代语义核验。12438恢复精确正文前不支持正面结论，争议项只隔离所写保证，不全盘否定经验结果。

12373/12447/12617/12798 已实际写入并获 root 写后独立通过。[八项采用记录](../_sources/daily-20260415/V3_BOOKS_PENDING_8.md)逐项区分提案、实际落笔与独立通过。有限题摘/必要证据队列与Robotics-ER1.6比较已收口，不扩546库存或附件。LoSA owner为Ch45，Ch14只交接online-softmax，不归Ch13。仅以下精确保留项会在材料到达后定点重开，不等待无关材料。

具体日期/身份隔离：2604.12086官方abs称ICLR2026，已恢复同题NeurIPS2025匿名OpenReview正文与ICLR正式同作者页面，首发身份不能直接继承此次arXiv上传。forum/API被challenge/403，尚未取得原公开时间；仅保存其Linear-MaxMin whitening非负cone等价的精确争议，不评分为确定当窗候选、不写Books。恢复条件是官方早版公开身份/时间或明确新的revision命题，见必要证据记录；不由venue或搜索缓存时间造首发。

外部或日期精确保留项：OpenAI Research历史Load more、Google Publications日级目录、Meta研究历史窗口、Kimi2026 Blog、ERNIE-Image原始公开时间、MiMo undated Blog、MiniMax AgentTechBlog、Seedance2卡片原始事件，均按§2具体入口保留。2604.12175v1 DSIEQA虽有数值评价潜在贡献，库存v1Updated=2026-06-30T00:50:36Z未提供04/15截点前上界；官方abs/v1的Submitted只是投稿，需官方April公开批次或同版本早于截点的公开证据，未入确定候选/Books。需要能证明本窗停点的官方窗口列表/历史分页或同版本事件公开上界；不用于正面采用、不支持无遗漏断言。ERNIE-Image官方正文/作者card已恢复，不再记“正文不可得”。末端Updated≥01Z的潜在贡献仅记录日期上界缺口，不从更新时间孤证推明确窗外。

公式争议的定点重开材料是作者勘误或使原公式假设/目标一致的证明；不要求更多无关benchmark。全部必要原字段、具体反例和可接受替代见本日证据笔记，未把未审工作标成作者私有材料受阻。

## 6. 复核

复核者：root、apr02（均非报告作者）。

结论：通过

root 对读14个来源的实际停点、官方公告/OAI/相邻批次与截点前上界组合，拒绝把 Submitted、DOI-created 或单个 Updated 改写为首发；来源目录、末端日期及早公开身份例外保持具名隔离。冻结表逐项对读§4采用命题、版本、证据边界与处置；不将546标题或240题摘改名成全日贡献。否定侧除原首11+另9题摘校准外，本轮重新打开11839/12088/12459/12548/12601/12737/12300的完整官方摘要并对读具体关闭理由，检查成熟组合、单域验证和通用OS类比是否被误作新增机制；12379/12748复用未变的必要消歧，12376当前官方撤回已再次核实，不入selected或Books。这是按风险安排的有限反向抽检，不宣称240/546均被第二人重读。

22项真实正文及相邻交接的必要来源/写后核验已通过，记录见[具名独立复核](../_sources/daily-20260415/V3_INDEPENDENT_THREE_CALIBRATION.md)与[八项实际写后](../_sources/daily-20260415/V3_BOOKS_PENDING_8.md)。apr02 本轮再次打开五项 Existing 的必要方法/评价并与 Ch29/72/66/5 实际命题对读，通过限定采用范围，不声称书稿包含五套完整算法。

17个争议仅隔离原报告的具体公式/保证。root对读必要原公式及反例，包括矩形identity、二次目标归一化、子集最优方向、嵌套Hit、squared/unsquared medoid、tokens/s²量纲、Bayes排序分母、单项/全分布entropy、指纹与replay保证、group质量、paired-CE、熵导数符号、margin到输入半径、ridge精确恢复及payload/zero-bit gate；TimeMark/SpecBound复用apr02有效的原版本范围复核。反例不推翻全部经验或实现，不要求无关附件。12438正文缺口及其他外部限制按§5安全终态保存，不支持证据通过、Books或无遗漏断言。普通可执行工作为0。

本次格式/一致性校验通过；候选表123唯一家族、22/5/78/17/1分区与41/64/17/1审阅统计一致，必要Books实际正文和源链接保持可回溯。机器结果不替代上述语义检查，未复现实验、未stage/commit/push。
