# Daily Research — 2026-04-22

**规范：** V3
**窗口：** 2026-04-21T09:00:00+08:00 ～ 2026-04-22T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-28T04:54:32+08:00

## 1. 结论

本轮已落实三十条有条件的机制增量：冗余语料中必要信息与可替代证据映射、静态NPU的MoE容量/分组/驻留联合选择、在线更新后误差基线的探索选样、CP与EP互斥phase复用受约束光链路、kernel关系标签与功能验收分权、有限horizon记忆sensor与物理恢复分权、GUI观察新鲜与handler/effect绑定分权、MoE逻辑位置/归约次序与tile readiness分离、两条有条件的生成训练目标分支、静态图接口与runtime adapter值分责、整数activation码的时间加权spike执行分支、query-view相对几何与KV执行视图分责，正确子集judge辅助奖励与完整group优势分责，完整视频prompt下按帧与事件区间局部消费文本条件，两种语音监督与生成的条件链、细粒度递归更新与并行代数的兼容桥、projector 权重/输出/行为诊断分层、按层局部反馈控制、随层深演进的状态化适配资产、训练 primitive/executor 与测试 latent 搜索分工、entity×relation 绑定地址与跨语境坐标分责、构造的蒸馏目标与原输出评分分责、patch 最大可用信息与均值噪声训练支持分责、独立校准历史读门、可校准teacher与student验收分账、streaming RL局部输出步长，协作编辑场景中同一危险草稿的任务包装安全评价，以及多语言评估中显式地区知识与隐式默认选择的分账。实际正文和相邻衔接已获root、apr01或apr02（非书稿作者）写后核验，不以局部数字或代理信号替代完整系统验收。

515个去重原始身份是宽分类查漏库存，不是当天贡献数，也不是全文队列；标题已浏览，相关范围中170份完整题摘已逐项语义判断。与当前正式表逐项对账，170项中99项为已冻结的工作家族、69项有具体贡献前关闭理由、2项因首公开日期未证而隔离（19503/19533）；负侧反查恢复18724、19053与19274为受限候选，19087、19301、19457、18660及19185、19059、19342、18857、19071、19201、19321、19440经具名理由前关闭，原证据均保留。以515个原始身份计，本次工作保留率约19.2%；以预选的170份完整题摘计则约58.2%，两者不是同一分母，也不是筛选质量配额。最终30项实际整合、9项具体已有覆盖、55项仅报告、5项窄争议；30项整合已通过真实写后独立复核，非作者日级来源、日期和负侧复核在§6所列限制下通过。旧34全部Existing及DOI-created归属不继承；[旧稿](../_sources/daily-20260422/V2_1_README_PRESERVED.md)无损保留为审计证据。

## 2. 来源覆盖

以下目录的检查只证明实际入口/停点，不代表所有机构作者稿或全网无遗漏。未变化的机构目录记录复用已实际读过的[本日检查点](../_sources/daily-20260422/V3_REVIEW_CHECKPOINT.md)及其引用的04/19、04/21原始材料，不因恢复重复扫描全年。

新增六份标题边界摘要已完成独立准入校准：五份按具名范围/贡献理由前关闭，`2604.19053v1` 因安全聚合的相位与秘密状态责任重开；它的旧库存摘要混入后版数字，中心保密保证另有本轮独立确认的窄反例，故仅作争议保留、不进入 Books。新增身份已并入上文170项，而非将515库存当逐项全文队列；证据见[本日笔记](../_sources/daily-20260422/V3_EVIDENCE_REVIEW.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | News RSS 1230条，最近相邻事件04/21T00:00Z早于窗口；Research入口受限 | 受阻 | RSS不代表完整Research；需可读的历史Research/Publication目录或官方当窗事件 |
| SRC-ANTHROPIC | 原HTML publishedOn相邻04/14T13:01Z→04/22T14:12/14:27Z；后两项均晚于截点 | 已检查 | 仅公开Research目录，不宣称所有作者稿覆盖 |
| SRC-GOOGLE-AI | DeepMind selected目录页跨04/22→03/22；Google Research实际文章含ReasoningBank旧家族和DecoupledDiLoCo04/23T16Z窗外；Publication宽年度入口不用于候选算术 | 受阻 | Publication历史窗口目录未闭合；AutoFrame日级线索具体成熟组合已关闭；`2604.20329v1` 对应DeepMind Publication仅标04/22日，截点前公开未证，隔离为相邻日线索 |
| SRC-META-AI | 官方Research入口空/混合历史页，已读相邻04/06、04/08→03/27 | 受阻 | 空响应不能证明零更新；需可读官方当窗Research目录 |
| SRC-QWEN | 官方Research静态60旧项与动态40条；相邻04/18T10+08→04/22T10+08，后者晚于窗口 | 已检查 | 仅可见公开目录，不等全部作者稿 |
| SRC-DEEPSEEK | News相邻04/24→2025/12/01，Research06/24→02/25，公开目录跨窗口无相关事件 | 已检查 | 不扩普通commits，不保证未列作者稿 |
| SRC-MOONSHOT | 可见26条Blog主要2025，43个组织仓库只重要release层有界查漏 | 受阻 | 历史Blog窗口目录不能确定；需官方本窗研究清单/事件，不把repo新建当覆盖所有发布 |
| SRC-TENCENT-HUNYUAN | 研究页“全部列表”官方publicList total9/list9，04/23→02/13跨窗口 | 已检查 | 全部可见条目，不泛称所有未列论文无命中 |
| SRC-ZAI | Research目录可见04/29→04/07→04/01；notes06/16→04/07→02/12跨窗口 | 已检查 | 页面日期精度及可见目录限制，不将CMS createdAt当公开日 |
| SRC-BYTEDANCE-SEED | official US type1论文242条，page_token20跨05/12→04/08；type2 Blog95条跨04/23→04/09→04/01 | 受阻 | Seed3D2.0日桶时间不能证明截点前公开，具体身份隔离于§5；AgentWorld04/19T16Z是窗外旧家族 |
| SRC-BAIDU-ERNIE | 10条技术Blog相邻04/30→04/15→02/06/2025，跨窗口无相关事件 | 已检查 | 只可见技术目录，不扫全部作者稿 |
| SRC-XIAOMI-MIMO | Paper8项06/29→03/13→02/03跨窗口；Blog14项日期未恢复 | 受阻 | Paper停点有效；Blog需官方可核历史日期，不能合称零更新 |
| SRC-MINIMAX | EN12项05/26→03/18、CN13项04/27→03/18跨窗口；Agent Tech最早可見05/13，未到窗口 | 受阻 | Agent Tech历史目录未闭合；需原始当窗条目或可分页历史入口 |
| SRC-ARXIV | [官方12分类有界补检](../_sources/daily-20260422/V3_ARXIV_OFFICIAL_BOUNDED_DISCOVERY.md)：各类04月目录逐页身份/标题停点及主题 Atom 查询均已记录；临时ID带内357个跨类去重身份均见旧515库存、无新身份；与99正式工作候选反向对账为92固定分类月页命中、7其他分类具名单篇定点来源；相关范围170完整题摘已判断，当前99工作家族/69具名前关闭/2日期隔离；官方slot/连续ID/OAI/早v1字段联合核归属 | 已检查 | 整月目录仅筛本ID带和主题标题，不逐篇审阅整类；7项定点单篇不证明全学科召回、每篇首发时刻或所有版本事件；379早字段不是候选数，136晚字段不套整批公告时刻；日级独立来源/日期/负侧Gate待核 |

## 3. 候选与判断

本表公开范围采用“官方公告slot＋连续批次身份/OAI＋个别早v1字段”的有据推断，**不把Updated或DOI-created改名首次公开日志**；非作者日级复核认可这一有界批次归属，不是逐篇秒级公开日志。晚字段和Seed日桶线索不列确定候选。本表冻结99个工作家族；外部隔离和未来具体反证仍按§5定点重开。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Two-dimensional early exit optimisation of LLM inference](https://arxiv.org/html/2604.18592v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 输入前缀与深度联合退出的有限执行分支；2+1+2=5 | 标准完成 | 仅报告：有限分类配方不形成Serving收益保证 |
| [ARGUS: Agentic GPU Optimization Guided by Data-Flow Invariants](https://arxiv.org/pdf/2604.18616v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | layout合法不等逐元素关系配对，tags反例反馈；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，逐元素关系标签段 |
| [Owner-Harm: A Missing Threat Model for AI Agent Safety](https://arxiv.org/html/2604.18658v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | goal-harm与owner-harm迁移反证限制保护评价；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，goal不代授权 |
| [Curiosity-Critic](https://arxiv.org/html/2604.18701v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | learned post-update误差基线仅排序采样，不代update/hold；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，探索选样段 |
| [Efficient MoE Inference with Apple Silicon NPUs](https://arxiv.org/html/2604.18788v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 静态后端capacity tier×group×residency共同选，不允许临时overflow spill；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，Routed→Indexed段 |
| [HELM: Harness-Enhanced Long-horizon Memory](https://arxiv.org/html/2604.18791v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | history-conditioned风险监督与环境truth/恢复分权；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，有限horizon记忆风险sensor段 |
| [Temporal UI State Inconsistency](https://arxiv.org/html/2604.18860v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 像素/窗口新鲜不证明click handler身份；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，GUI观察面/执行面段 |
| [R²-dLLM](https://arxiv.org/html/2604.18995v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 空间confidence与时间finalize、正确轨迹筛选的局部边界；2+2+2=6 | 深入完成 | 仅报告：局部启发式不升级稳定正确性或统一端到端收益 |
| [TurboEvolve](https://arxiv.org/html/2604.18607v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | seed质量×allocation影响受限program evolution排序；2+1+2=5 | 标准完成 | 仅报告：退化pool条件证据，不采用统一最优 |
| [ChipLight](https://arxiv.org/html/2604.18909v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | CP/EP互斥phase复用同rail物理容量，不算双带宽；2+2+2=6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，可重构Fabric段 |
| [Security Is Relative / Phoenix](https://arxiv.org/html/2604.19012v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 配对标签辅助规格生成的reference权限改变部署解释；2+2+2=6 | 深入完成 | 仅报告：不采用无特权输入zero-shot或跨baseline公平保证 |
| [Refute-or-Promote](https://arxiv.org/html/2604.19049v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 经验测试推翻共享错误共识的具体反证；2+1+2=5 | 标准完成 | 仅报告：变动pipeline/人工救回不证明固定stage因果 |
| [RoboWM-Bench](https://arxiv.org/html/2604.19092v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 视频→动作转换→环境执行分别组成评价对象；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，完整pipeline身份 |
| [SAW-INT4](https://arxiv.org/html/2604.19157v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | KV量化布局/consumer融合与条件化吞吐排序分离；2+2+2=6 | 标准完成 | 仅报告：局部配方及指标反转，不采用唯一兼容/全模型无损 |
| [UniEP: Unified Expert-Parallel MoE MegaKernel for LLM Training](https://arxiv.org/pdf/2604.19241v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 固定逻辑地址/归约顺序与异步tile readiness分离；2+2+2=6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，Token Dispatch Contract内两段 |
| [DASH-KV: Accelerating Long-Context LLM Inference via Asymmetric KV Cache Hashing](https://arxiv.org/html/2604.19351v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | query动态/key预编码代理与packed-bit实现分离；2+2+2=6 | 深入完成 | 仅报告：FP16原型不能支持native bit实现的端到端部署收益；apr20独立通过 |
| [EVPO: Explained Variance Policy Optimization for Adaptive Critic Utilization in LLM Post-Training](https://arxiv.org/html/2604.19485v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | population residual方差与有限batch门控/融合保证分离；2+2+2=6 | 深入完成 | 仅报告：局部切换配方及已披露有限样本边界；apr20独立通过 |
| [The Cost of Relaxation: Evaluating the Error in Convex Neural Network Verification](https://arxiv.org/html/2604.18728v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 过近似可达集合的虚假点与安全证书保守性分离；2+1+2=5 | 标准完成 | 仅报告：有限误差实验不否定所有鲁棒性证书；apr01独立通过 |
| [Towards Scalable Lifelong Knowledge Editing with Selective Knowledge Suppression](https://arxiv.org/html/2604.19089v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 外部编辑上下文与首token词表抑制分责；2+1+2=5 | 标准完成 | 仅报告：受限编辑配方及当前artifact消歧，不作知识真值保证；apr01独立通过 |
| [LogosKG: Hardware-Optimized Scalable and Interpretable Knowledge Graph Retrieval](https://arxiv.org/html/2604.18913v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | incidence frontier聚合与保留triple-ID恢复路径分工；2+2+2=6 | 标准完成 | 仅报告：图检索执行分支不证明全部provenance或truth；root独立通过 |
| [Superficial Success vs. Internal Breakdown: An Empirical Study of Generalization in Adaptive Multi-Agent Systems](https://arxiv.org/html/2604.18951v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | terminal accuracy与role/message代理跨域分离；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)，角色正确性独立验收；root独立通过 |
| [SAGE: Signal-Amplified Guided Embeddings for LLM-based Vulnerability Detection](https://arxiv.org/html/2604.19031v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 派生probe可预测性与原模型决策因果分离；2+2+2=6 | 深入完成 | 仅报告：特权定位输入和局部sensor不支持普遍机制归因；root独立通过 |
| [DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging](https://arxiv.org/html/2604.19305v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 真正插桩执行与observer effect、oracle定位权限分账；2+1+2=5 | 标准完成 | 仅报告：有限修复协议不证明插桩无副作用或总预算公平；root独立通过 |
| [Remask, Don't Replace: Token-to-Mask Refinement in Masked Diffusion Language Models](https://arxiv.org/html/2604.18738v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 可疑token检测与重掩/替代动作分离；2+1+2=5 | 标准完成 | 仅报告：局部detector/action比较不支持通用mask优势；root独立通过 |
| [Discrete Tilt Matching](https://arxiv.org/html/2604.18739v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | terminal reward倾斜经mask状态匹配局部unmask posterior；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，CTMC目标后条件匹配段；root实际写后通过 |
| [One Step Forward and K Steps Back: Better Reasoning with Denoising Recursion Models](https://arxiv.org/html/2604.18839v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 腐化目标初始化与短递归窗末端监督的替代目标；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，ELT有限循环后短窗监督段；root实际写后通过 |
| [Unlocking the Edge deployment and ondevice acceleration of multi-LoRA enabled one-for-all foundational LLM](https://arxiv.org/html/2604.18655v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 同尺寸adapter输入把静态图身份与runtime值分开；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，静态图接口/adapter值两段；root实际写后通过 |
| [Rethinking Dataset Distillation: Hard Truths about Soft Labels](https://arxiv.org/html/2604.18811v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 监督标签/teacher改变subset质量比较的分母；2+1+2=5 | 标准完成 | 仅报告：受限分类对照不推LLM数据无关；root独立通过 |
| [Semantic Needles in Document Haystacks: Sensitivity Testing of LLM-as-a-Judge Similarity Scoring](https://arxiv.org/html/2604.18835v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 文档内部扰动位置与周边语境改变judge分布；2+1+2=5 | 标准完成 | 仅报告：受限similarity敏感性不当事实正确或普遍长上下文因果；root独立通过 |
| [SpikeMLLM: Spike-based Multimodal Large Language Models via Modality-Specific Temporal Scales and Temporal Compression](https://arxiv.org/html/2604.18610v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | activation码与时间加权spike累积形成执行接口分支；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，低位执行表示后的时间累积两段；root实际写后通过 |
| [Beyond Explicit Refusals: Soft-Failure Attacks on Retrieval-Augmented Generation](https://arxiv.org/html/2604.18663v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 流畅但无信息的soft-failure与拒绝、retrieval成功分账；2+2+2=6 | 深入完成 | 仅报告：clean筛选改变最终分母，共同AUS非独立truth；root有限独立通过 |
| [Beyond Indistinguishability: Measuring Extraction Risk in LLM APIs](https://arxiv.org/html/2604.18697v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 相对membership风险与绝对抽取、partial-logit估计分离；2+2+2=6 | 深入完成 | 仅报告：rank估计非certificate，DP有受控改善；root有限独立通过 |
| [URoPE: Universal Relative Position Embedding across Geometric Spaces](https://arxiv.org/html/2604.18747v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | query-view相对几何与KV执行视图分开；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Towards Understanding the Robustness of Sparse Autoencoders](https://arxiv.org/html/2604.18756v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | residual重构干预与自适应/迁移攻击评价分开；2+2+2=6 | 深入完成 | 仅报告：受限保护干预，未证明通用utility或安全保证；root独立通过 |
| [How Adversarial Environments Mislead Agentic AI?](https://arxiv.org/html/2604.18874v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | tool engagement/graph陷阱机会与错误分母分离；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，opportunity/Outcome Witness；apr20窄命题独立通过 |
| [Where Fake Citations Are Made: Tracing Field-Level Hallucination to Specific Neurons in LLMs](https://arxiv.org/html/2604.18880v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 字段probe干预与非均匀质量/统计范围分账；2+1+2=5 | 标准完成 | 仅报告：受限field干预有year/venue反益，不采用统一可靠修复；root有限非作者核通过 |
| [Prioritizing the Best: Incentivizing Reliable Multimodal Reasoning by Rewarding Beyond Answer Correctness](https://arxiv.org/html/2604.18892v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | correct-only辅助居中与完整group advantage不同归一范围；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO / [Ch33](../../../../books/part-04-training-system/33-grpo.md)，正确集合资格与完整组advantage分权；apr01实际写后通过 |
| [Harmful Intent as a Geometrically Recoverable Feature of LLM Residual Streams](https://arxiv.org/html/2604.18901v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | decodability/refusal/低FPR operatingpoint与授权分离；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，Refusal/learned sensor分权；apr20窄命题独立通过 |
| [Gated Memory Policy](https://arxiv.org/html/2604.18933v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 独立error-proxy校准读门、冻结后重训policy分责；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，episode memory 后独立读门段；root写后通过 |
| [Reasoning Structure Matters for Safety Alignment of Reasoning Models](https://arxiv.org/html/2604.18946v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 分段reasoning监督改变安全与over-refusal取舍；2+2+2=6 | 深入完成 | 仅报告：受限SFT配方非普遍结构根因/安全保证；apr20独立通过 |
| [Distillation Traps and Guards: A Calibration Knob for LLM Distillability](https://arxiv.org/html/2604.18963v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | teacher自身先成为student-compatibility可更新artifact；2+2+2=6 | 深入完成 | 整合：TRAIN-SFT / [Ch29](../../../../books/part-04-training-system/29-sft.md)，teacher 可校准资产与 student 验收分账段；root写后通过 |
| [Mechanistic Anomaly Detection via Functional Attribution](https://arxiv.org/html/2604.18970v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 参数邻域loss coupling与activation probe不同检测对象；2+2+2=6 | 深入完成 | 仅报告：可信reference/选择分母与大采样成本限域，非机制真值；apr20独立通过 |
| [Low-Rank Adaptation for Critic Learning in Off-Policy Reinforcement Learning](https://arxiv.org/html/2604.18978v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 静态回归与bootstrap/replay shift的低秩更新排序反转；2+1+2=5 | 标准完成 | 仅报告：受限正则化证据，不为局部归一化配方新增正文；root有限非作者核通过 |
| [Savoir: Learning Social Savoir-Faire via Shapley-based Reward Attribution](https://arxiv.org/html/2604.18982v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | coalition价值与信用分配的中心消融/成本不自洽；3+1+2=6 | 争议 | 暂缓：恒定coalition值的Shapley-only归因、端点/baseline与simulation计数待澄清；apr01窄反例独立通过，不支持Books |
| [When Safety Fails Before the Answer: Benchmarking Harmful Behavior Detection in Reasoning Chains](https://arxiv.org/html/2604.19001v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 同批标签合并控制揭示binary与细行为监测不能互换；2+1+2=5 | 深入完成 | 仅报告：已筛trace/机器标注与事后选层的受限监测证据；apr20独立通过 |
| [FedProxy: Federated Fine-Tuning of LLMs via Proxy SLMs and Heterogeneity-Aware Fusion](https://arxiv.org/html/2604.19015v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 压缩子网络适配后覆盖原层的artifact与成本/暴露合同；2+2+2=6 | 深入完成 | 仅报告：受限proxy配方，额外成本与非formal IP保护不消失；[apr01有限非作者核通过](../_sources/daily-20260422/V3_APR01_TWO_19015_18966_INDEPENDENT.md) |
| [Personalized Benchmarking: Evaluating LLMs by Individual Preferences](https://arxiv.org/html/2604.18943v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | aggregate与个体排序不同测量对象，比较图/选人限制保留；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，slice与群体排序分权；apr20必要原文/owner独立通过 |
| [Self-Improving Tabular Language Models via Iterative Group Alignment](https://arxiv.org/html/2604.18966v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 组均值log-ratio目标与scorer数据分离的局部反馈条件；2+1+2=5 | 标准完成 | 仅报告：tabular目标配方/反证，不采用formal privacy或单调保证；[apr01有限非作者核通过](../_sources/daily-20260422/V3_APR01_TWO_19015_18966_INDEPENDENT.md) |
| [Intentional Updates for Streaming Reinforcement Learning](https://arxiv.org/html/2604.19033v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 先定义输出变化单位再反解scalar步长，trace状态非batch逆问题；2+2+2=6 | 深入完成 | 整合：TRAIN-PRETRAINING / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，局部输出步长条件分支；root写后通过 |
| [Cell-Based Representation of Relational Binding in Language Models](https://arxiv.org/html/2604.19052v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | entity×relation绑定地址与语义内容分离，patch只验局部使用；2+2+2=6 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，绑定地址与跨语境坐标分支；root写后通过 |
| [CHRONOS: A Hardware-Assisted Phase-Decoupled Framework for Secure Federated Learning in IoT](https://arxiv.org/html/2604.19053v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | FL idle setup、active mask、dropout recovery分时；同epoch合法恢复可暴露旧轮明文；2+1+2=5 | 争议 | 暂缓：中心单客户端保密保证的同epoch旧轮反例经root独立复核，不能正面整合Ch72/36 |
| [Reducing the Offline-Streaming Gap for Unified ASR Transducer with Consistency Regularization](https://arxiv.org/html/2604.19079v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | context模式在完整RNNT lattice对齐，辅助CTC一致不等目标解码；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，离线/流式RNNT监督对象分支；root写后通过 |
| [RARE: Redundancy-Aware Retrieval Evaluation Framework for High-Similarity Corpora](https://arxiv.org/html/2604.19047v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 替代chunk支持映射与部分/全必要信息覆盖分账；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，RAG阶段归因前的alternative-support gold合同；root写后通过 |
| [SAMoRA: Semantic-Aware Mixture of LoRA Experts for Task-Adaptive Learning](https://arxiv.org/html/2604.19048v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 主表同九任务聚合结果与打印Avg不一致，效用—容量比较须收窄；3+1+2=6 | 深入完成 | 仅报告：等权同九任务增益0.81pp，打印3.07pp口径隔离；apr01有限非作者通过 |
| [ProjLens: Unveiling the Role of Projectors in Multimodal Model Safety](https://arxiv.org/html/2604.19083v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 权重谱/神经元阴性不等paired输出残差无可干预低维结构；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，projector 权重、输出残差与行为诊断分层；root写后通过 |
| [Robust Continual Unlearning against Knowledge Erosion and Forgetting Reversal](https://arxiv.org/html/2604.19108v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 连续删除后旧目标恢复、累计集合指标与当前请求分账；2+1+2=5 | 深入完成 | 仅报告：分类negative margin非参数影响/LLM隐私删除；apr20独立通过 |
| [LLMs Know They're Wrong and Agree Anyway: The Shared Sycophancy-Lying Circuit](https://arxiv.org/pdf/2604.19117v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 共享组件位置/任务方向/表达行为不是同一诊断对象；2+2+2=6 | 深入完成 | 仅报告：有限方向/位置干预经验保留；不称整套circuit已有，apr01有限非作者通过 |
| [Guiding Distribution Matching Distillation with Gradient-Based Reinforcement Learning](https://arxiv.org/html/2604.19009v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | reward评分implicit target而非早期raw输出的监督分支；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，构造目标评分责任；root写后通过 |
| [Local Linearity of LLMs Enables Activation Steering via Model-Based Linear Optimal Control](https://arxiv.org/html/2604.19018v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | offline局部模型/gain与online feature误差反馈分责；2+2+2=6 | 深入完成 | 整合：TRAIN-RLHF / [Ch31](../../../../books/part-04-training-system/31-rlhf.md)，层深反馈与静态 steering 分支；root 写后通过 |
| [FG²-GDN: Enhancing Long-Context Gated Delta Networks with Doubly Fine-Grained Control](https://arxiv.org/html/2604.19021v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 双边gate保低秩transition，细粒度控制不自动保chunk并行；2+2+2=6 | 深入完成 | 整合：MODEL-LONG-CONTEXT / [Ch22](../../../../books/part-02-model/22-long-context.md)，逐通道更新与对称WY降低的代数兼容桥；root写后通过 |
| [Policy Gradient Primal-Dual Method for Safe Reinforcement Learning from Human Feedback](https://arxiv.org/html/2604.19024v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 相对偏好需绝对安全anchor、continuing horizon与平均constraint分账；2+1+2=5 | 深入完成 | 仅报告：条件tabular理论不是逐响应LLM安全；apr20必要原文/owner独立通过 |
| [Denoising, Fast and Slow: Difficulty-Aware Adaptive Sampling for Image Generation](https://arxiv.org/html/2604.19141v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 最大可用信息与均值noise状态不同训练support合同；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，patch训练支持分支；root写后通过 |
| [Nexusformer: Nonlinear Attention Expansion for Stable and Inheritable Transformer Scaling](https://arxiv.org/html/2604.19147v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | function-preserving全零扩容不等新通道可学习，印出梯度桥需纠正；3+1+2=6 | 争议 | 暂缓：只隔离新增块梯度非零/增长保证，保有限经验；apr01窄反例独立通过 |
| [How Do Answer Tokens Read Reasoning Traces? Self-Reading Patterns in Thinking LLMs for Quantitative Reasoning](https://arxiv.org/html/2604.19149v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 读出几何、质量选择及steering效应不是同一因果对象；2+1+2=5 | 标准完成 | 仅报告：局部selection对照不建立通用reading controller；[apr01有限非作者核通过](../_sources/daily-20260422/V3_APR01_TWO_19015_18966_INDEPENDENT.md) |
| [Mind the Unseen Mass: Unmasking LLM Hallucinations via Soft-Hybrid Alphabet Estimation](https://arxiv.org/html/2604.19162v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | finite-sample支持估计误差与风险排序效用分账；2+1+2=5 | 标准完成 | 仅报告：小n代理/有限QA不构成开放风险保证；apr01有限非作者通过 |
| [Learning to Credit the Right Steps: Objective-aware Process Optimization for Visual Generation](https://arxiv.org/html/2604.19234v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 可分离时间代理与样本多目标权重不等真实step因果/Pareto信用；2+2+2=6 | 深入完成 | 仅报告：有限proxy配方与反向结果，局部min-norm不升整体保证；[apr01有限非作者核通过](../_sources/daily-20260422/V3_APR01_TWO_19015_18966_INDEPENDENT.md) |
| [ShadowPEFT: Shadow Network for Parameter-Efficient Fine-Tuning](https://arxiv.org/html/2604.19254v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 层深状态化适配与可merge权重/固定launch state的资产责任不同；2+2+2=6 | 深入完成 | 整合：TRAIN-LORA / [Ch30](../../../../books/part-04-training-system/30-lora.md)，attached shadow 与固定 S0/merge 分支；root 写后通过 |
| [TEMPO: Scaling Test-time Training for Large Reasoning Models](https://arxiv.org/html/2604.19295v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | unlabeled policy适应与有标签critic刷新来源分开，近似V不是真条件概率；2+2+2=6 | 深入完成 | 仅报告：局部test-time训练recipe/反向heldout结果，非纯无监督自改进；apr20必要原文/owner独立通过 |
| [HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models](https://arxiv.org/html/2604.19300v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | audio缺证据肯定、有效query误拒与parser错误分账；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)拒答分母/measurement identity；apr20必要原文/owner独立通过 |
| [Text-To-Speech with Chain-of-Details: modeling temporal dynamics in speech generation](https://arxiv.org/html/2604.19330v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | token时间层级与residual codebook层级分开，总时长预测仍保留；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，时间分辨率与RVQ残差层级分权；root写后通过 |
| [GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models](https://arxiv.org/html/2604.19398v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | budget-feasible prefix之后nonempty guard可重超预算；3+1+2=6 | 争议 | 暂缓：只隔离每步无条件硬cap桥，保STE/有限经验；apr01有限非作者通过，非日Gate |
| [Lost in Translation: Do LVLM Judges Generalize Across Languages?](https://arxiv.org/html/2604.19405v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | translator敏感度改变分数/方差，有限排名稳定非语义等价；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)派生benchmark身份；apr20窄命题独立通过 |
| [Unsupervised Confidence Calibration for Reasoning LLMs from a Single Generation](https://arxiv.org/html/2604.19444v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 离线一致性proxy摊销成单生成sensor，不省独立真值责任；2+1+2=5 | 标准完成 | 仅报告：有限ridge/isotonic实现与shift结果，非真值保证；[apr01有限非作者核通过](../_sources/daily-20260422/V3_APR01_PENDING_FIVE_INDEPENDENT.md) |
| [Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning](https://arxiv.org/html/2604.19459v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | stage diff不能检出初始错误且自洽的specification；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)spec validity先于proof；apr20窄命题独立通过 |
| [LBLLM: Lightweight Binarization of Large Language Models via Three-Stage Distillation](https://arxiv.org/html/2604.19167v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 同低位宽joint训练失败与W/G固定后activation refinement条件分支；2+2+2=6 | 标准完成 | 仅报告：受限准备配方/阶段反证，不采全量内存或Serving倍率；[apr01有限非作者核通过](../_sources/daily-20260422/V3_APR01_PENDING_FIVE_INDEPENDENT.md) |
| [Dual-Guard: Dual-Channel Latent Watermarking for Provenance and Tamper Localization in Diffusion Images](https://arxiv.org/html/2604.19090v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 模型来源signal与具体发行内容完整性分账，round-trip reference决定校准；2+2+2=6 | 深入完成 | 仅报告：闭集Full模式与未测自适应攻击，不自动新增一般provenance原则；apr01必要源/实际owner处置独立通过 |
| [ST-Prune: Training-Free Spatio-Temporal Token Pruning for Vision-Language Models in Autonomous Driving](https://arxiv.org/pdf/2604.19145v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | temporal-first/view独立剪枝的质量与selector成本条件；2+1+2=5 | 标准完成 | 仅报告：有限时空proxy与排序证据非通用near-lossless/控制安全；apr01必要源/实际owner处置独立通过 |
| [Allo{SR}²: Rectifying One-Step Super-Resolution to Stay Real via Allomorphic Generative Flows](https://arxiv.org/pdf/2604.19238v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | LR来源统计匹配与单步路径监督分责，重建/感知反向取舍；2+1+2=5 | 标准完成 | 仅报告：受限SR分支不证明全分布兼容或曲率/真实时延保证；apr01必要源/实际owner处置独立通过 |
| [Talking to a Know-It-All GPT or a Second-Guesser Claude? How Repair reveals unreliable Multi-Turn Behavior in LLMs](https://arxiv.org/html/2604.19245v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | challenge可修错亦破坏原正确，answerable/unanswerable处置分母不同；2+1+2=5 | 标准完成 | 仅报告：有限多轮repair profile不构成可靠controller；apr01必要源/实际owner处置独立通过 |
| [DR-MMSearchAgent: Deepening Reasoning in Multimodal Search Agents](https://arxiv.org/html/2604.19264v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 跨batch结构权重与工具次数reward分离，不升级因果credit；2+2+2=6 | 标准完成 | 仅报告：局部重权配方及非同总compute；[apr01有限非作者核通过](../_sources/daily-20260422/V3_APR01_PENDING_FIVE_INDEPENDENT.md) |
| [Multimodal embodiment-aware navigation transformer](https://arxiv.org/html/2604.19267v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 尺寸条件clearance候选排序与物理安全分权；2+2+2=6 | 深入完成 | 仅报告：受限navigation控制配方不是collision证书；[apr01有限非作者核通过](../_sources/daily-20260422/V3_APR01_PENDING_FIVE_INDEPENDENT.md) |
| [Location Not Found: Exposing Implicit Local and Global Biases in Multilingual LLMs](https://arxiv.org/html/2604.19292v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 语言与locale提示分开测量，judge和population目标不合并；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，显式 locale 知识与隐式默认选择分账；apr02 非书稿作者写后通过 |
| [Silicon Aware Neural Networks](https://arxiv.org/pdf/2604.19334v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | cell-area训练代理与最终PPA分权，打印能耗口径冲突；2+1+2=5 | 深入完成 | 仅报告：保co-design局部机制，不采用冲突PPA倍率；root有限非作者核通过 |
| [Malicious ML Model Detection by Learning Dynamic Behaviors](https://arxiv.org/html/2604.19438v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | task-conditioned加载trace与合法执行/发布权分开；2+2+2=6 | 深入完成 | 仅报告：有限synthetic/real恶意样本不证明充分防御；[root 有限非作者核通过](../_sources/daily-20260422/V3_ROOT_THREE_19438_19461_18587_INDEPENDENT.md) |
| [Involuntary In-Context Learning: Exploiting Few-Shot Pattern Completion to Bypass Safety Alignment in GPT-5.4](https://arxiv.org/html/2604.19461v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | operator framing×示例排列绕过行为与机制因果分开；2+2+2=6 | 深入完成 | 仅报告：有限攻击recipe与选择分母，不采用普遍失效；[root 有限非作者核通过](../_sources/daily-20260422/V3_ROOT_THREE_19438_19461_18587_INDEPENDENT.md) |
| [TS-Attn: Temporal-wise Separable Attention for Multi-Event Video Generation](https://arxiv.org/html/2604.19473v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | full text context下subject×event interval局部条件消费；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，运动条件段后局部时序路由 |
| [Compile to Compress: Boosting Formal Theorem Provers by Compiler Outputs](https://arxiv.org/html/2604.18587v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 当前失败proof/编译反馈条件与完整历史责任分开；2+2+2=6 | 标准完成 | 仅报告：有损状态与样本预算不能外推充分性/总成本优势；[root 有限非作者核通过](../_sources/daily-20260422/V3_ROOT_THREE_19438_19461_18587_INDEPENDENT.md) |
| [Towards Optimal Agentic Architectures for Offensive Security Tasks](https://arxiv.org/html/2604.18718v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 同target/source-visibility下topology收益和validated成本不单调；2+1+2=5 | 标准完成 | 仅报告：受控拓扑/可观察性排序非普遍最优；apr20有限独立通过 |
| [LLM-as-Judge Framework for Evaluating Tone-Induced Hallucination in Vision-Language Models](https://arxiv.org/pdf/2604.18803v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 固定图/任务的tone反证与主实验/后验设计审计分母分开；2+1+2=5 | 深入完成 | 仅报告：800实验/717后验合格不能合并；不采用冲突排序；apr20 PDF-v1独立核通过 |
| [Do Agents Dream of Root Shells? Partial-Credit Evaluation of LLM Agents in Capture The Flag Challenges](https://arxiv.org/html/2604.19354v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 摘要×judge交叉控制暴露证据损失，episode停与agent停不是同一事；2+2+2=6 | 深入完成 | 仅报告：有限checkpoint评价及隔离失败，不采用充分修复保证；apr20有限独立通过 |
| [Geometric Decoupling: Diagnosing the Structural Instability of Latent](https://arxiv.org/html/2604.18804v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 同seed条件切换下曲率/高频代理相关性改变，不自动识别生成失败根因；2+1+2=5 | 深入完成 | 仅报告：保受限几何诊断，不采用root-cause或普遍可靠性保证；补§6.1/Table9后apr20有限独立通过 |
| [Multi-Domain Learning with Global Expert Mapping](https://arxiv.org/html/2604.18842v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 静态dataset/class映射可报告，但打印rounding算法对整值LP遗漏及近最优桥需隔离；3+1+2=6 | 争议 | 暂缓：只隔离Algorithm1/Eq6–9的完整assignment与近最优保证；apr01有效域反例有限非作者通过 |
| [Dual-View Training for Instruction-Following Information Retrieval](https://arxiv.org/html/2604.18845v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 同文档对instruction反转监督与general retrieval的取舍有等数据量对照；2+1+2=5 | 标准完成 | 仅报告：保指令敏感性/语义检索不同目标的局部数据配方；apr20必要原文/owner独立通过 |
| [Hierarchically Robust Zero-shot Vision-language Models](https://arxiv.org/html/2604.18867v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | leaf类攻击稳健不能推出superclass稳健，类层级改变保护评价；2+2+2=6 | 深入完成 | 仅报告：保分层攻击/受限训练方案，不采用margin增长为开放输入安全保证；root有限非作者核通过 |
| [Less Is More: Cognitive Load and the Single-Prompt Ceiling in LLM Mathematical Reasoning](https://arxiv.org/html/2604.18897v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 本地79.25%与官方55.5%在不同分布/执行配置反转，不能据有限搜索推理论ceiling；2+1+2=5 | 深入完成 | 仅报告：保受限prompt与配置反证，不采用稳健增益或静态prompt理论上限；root有限非作者通过 |
| [Gradient-Based Program Synthesis with Neurally Interpreted Languages](https://arxiv.org/html/2604.18907v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 程序codebook复用、循环executor与部署latent梯度搜索构成不同组合泛化分支；2+1+2=5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，组合性中的训练/搜索责任；root 写后通过 |
| [Disparities In Negation Understanding Across Languages In Vision-Language Models](https://arxiv.org/html/2604.18942v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 英语校准negation修复在其他语言可反向，平均多语言分数不足批准修复；2+1+2=5 | 标准完成 | 仅报告：保跨语言修复迁移反证，不把形态/脚本相关写成唯一因果；root有限非作者核通过 |
| [Beyond One Output: Visualizing and Comparing Distributions of Language Model Generations](https://arxiv.org/html/2604.18724v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | token graph概览与原始样本回查改变不同分布判断任务的可靠性；2+1+2=5 | 标准完成 | 仅报告：Ch66已有版本化分布/重复样本与原始输出对聚合的分账；GROVE是受限界面实例，不新增正文 |
| [HarDBench: A Benchmark for Draft-Based Co-Authoring Jailbreak Attacks for Safe Human-LLM Collaborative Writing](https://arxiv.org/html/2604.19274v1) | 2026-04-22T08:00:00+08:00 ～ 2026-04-22T09:00:00+08:00 | 同一有害草稿在无/有编辑任务包装时的安全行为差异，直接危险请求拒答不能代协作编辑验收；2+1+2=5 | 深入完成 | 整合：PLATFORM-SECURITY / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，Guardrail 的协作编辑配对验收；实际写后由 apr02 独立复核通过 |

## 4. 证据与知识整合

所有项的必要原文位置、评价/反证与具体owner对照见[本轮证据审阅](../_sources/daily-20260422/V3_EVIDENCE_REVIEW.md)，不是仅有摘要改写。下面保留核心判断；官方作者证据未被包装为复现或生产验证。

### [Two-dimensional early exit optimisation of LLM inference](https://arxiv.org/html/2604.18592v1)

前缀证据×层深度的退出改变有限执行分支；实际方法/成本条件只支持受测分类协议，FLOP/跳层不等整个推理链延迟。root已独立必要源与owner核，仅报告。

### [ARGUS: Agentic GPU Optimization Guided by Data-Flow Invariants](https://arxiv.org/pdf/2604.18616v1)

§3–7/9.3–9.4的关系标签与SMT反例可定位跨tile数据编排错误；path-insensitive合流、heap/global-write与形状限制不证明任意kernel等价。MI300X条件下仍有低于参考的速度及PyTorch回退；消融共同改tags和compiler feedback。Ch49逐元素关系标签两段已实际写入，apr20源→owner、root窄稿采用及实际正文/相邻衔接写后通过；不表示复现实验。

### [Owner-Harm: A Missing Threat Model for AI Agent Safety](https://arxiv.org/html/2604.18658v1)

goal一致不证明owner允许数据目的地，通用harm防御不能直接迁移为工具授权。Ch72实际Goal Alignment与组合授权段已经区分sensor、policy、dispatch和effect，root独立采用通过。只称该命题已有覆盖，不称论文完整算法已在书里。

### [Curiosity-Critic](https://arxiv.org/html/2604.18701v1)

§3–5.3的telescoping到critic是近似链，learned post-update residual只给采样排序；MSE mean不自动是任意L2 metric的不可约oracle。受限格子/随机TV、35K步/5seed不证明高维真实控制。Ch25探索采样真实写入，保count/random回退并由后文update/hold验收真实效用；root写后PASS。

### [Efficient MoE Inference with Apple Silicon NPUs](https://arxiv.org/html/2604.18788v1)

§3–5静态shape容量分层、group launch与图驻留联动；预置CPU冷group与overflow临时spill不同。M2Max/Ultra、FP16、具体prompt/chunk和短decode只支持局部结果；latency最好不等energy最好，有token drop/padding/质量代价。Ch49 Routed→Indexed真实两段已经嵌主线并通过root写后核。

### [HELM: Harness-Enhanced Long-horizon Memory](https://arxiv.org/html/2604.18791v1)

§4/5的history-conditioned predictor监督未来5步失败，不拥有当前safety truth。Table3 full81.5、无SV73.1、SV无memory79.2：2.3pp是memory输入移除差，不是无memory时SV全部增量；后者仍6.1pp。有限模拟恢复动作不是物理回滚，12ms/step不证明实时SLO。Ch26有限horizon记忆sensor两段已实际写入，root实际正文及相邻恢复/监督论证写后通过，未复现实验。

### [Temporal UI State Inconsistency](https://arxiv.org/html/2604.18860v1)

§4三类攻击与§5 sensor对照说明像素/窗口registry与实际hit-target不等价；再截图仍留race，DOM建议未实际验证。不同试验分母不合并，44/45不写99.3%。Ch72观察面/执行面两段已实际写入，root实际正文及相邻sensor/effect论证写后通过；不称所有框架缺原子性。

### [R²-dLLM](https://arxiv.org/html/2604.18995v1)

§4–6的窗口confidence和连续top1允许有限finalize策略，但稳定不是真值；训练中正确轨迹筛选oracle未清，不称完全无外部判断。所有非vanilla皆dualKV、质量有退步、NFE不等端到端成本。apr20独立必要深入仅报告通过。

### [TurboEvolve](https://arxiv.org/html/2604.18607v1)

§3–5比较删强seed后的起点，局部证明allocation收益依赖pool而非统一支配。失败编译计入800 evaluations，Gemini3seed/token预算不与文献全matched；root标准Only通过，不为算法名称新增正文。

### [ChipLight](https://arxiv.org/html/2604.18909v1)

III–V同rail容量与CP/EP互斥phase复用是具体物理计划分支；ASTRA/H100估算/CPO不是实际集群吞吐。Ch36 Fabric真实两段保phase overlap、切换/端口成本、静态fallback及Ch35 checkpoint职责，root实际写后通过。

### [Security Is Relative / Phoenix](https://arxiv.org/html/2604.19012v1)

§3–5合成reference先看bad/good配对、CVE和commit，再judging；这项权限不能藏在“training-free”里。格式失败后的样本数文本与2×pair数不一致，作者复审FP不当独立truth。保受限规格条件，不采未知单函数部署或模型大小公平比较；root有限非作者必要源/实际owner处置通过。

### [Refute-or-Promote](https://arxiv.org/html/2604.19049v1)

§3–5多Agent共识的具体错误被行为测试推翻，支持独立outcome而非更多共识即truth。不同wave/变动pipeline、人工救回false kill、CVEs与标准结果分账，不能用淘汰率推固定阶段因果或总成本收益。root有限非作者标准Only通过。

### [RoboWM-Bench](https://arxiv.org/html/2604.19092v1)

§3/4和Table2把生成视频、IDM/retarget动作转换、模拟器执行及stage-checker分开；真实视频来源不等真机eval。成功示教转换校准不证明生成分布的转换忠实。拟采用的是Ch25可执行outcome与Ch66 model×harness×environment×scorer完整身份已有论点，不称原benchmark算法全覆盖；root必要源和当前正文独立Existing通过。

### [SAW-INT4](https://arxiv.org/html/2604.19157v1)

§2–4/AppendixD将query旋转融合在consumer，短/长上下文与并发改变系统TPS和active-decoder条件TPS排序；H100单服务与2H100/TP2/batch32 kernel不同分母。Ch45 inner-dimension grouping已有实际替代，故不采用tokenwise唯一兼容；有限融合配方和反例保Only，root非作者必要源/真实owner处置通过。

### [UniEP: Unified Expert-Parallel MoE MegaKernel for LLM Training](https://arxiv.org/pdf/2604.19241v1)

官方HTML页头为July29，本次按April22首页的PDF-v1必要§3–6核。source-rank offset与排序固定逻辑目标，scoreboard驱动物理到达/计算ready，top-k合并另等贡献；不能从固定buffer单独推出全训练bitwise。Ch36 Token Dispatch Contract内实际两段新增逻辑顺序与tile readiness分离，apr20必要源→owner及root实际正文/相邻衔接写后通过。硬件具体型号ND、autotune摊销、nonbitwise配置.97/.98退步及host-shape消融混杂保留；不表示完整训练或生产故障已验收。

### [DASH-KV: Accelerating Long-Context LLM Inference via Asymmetric KV Cache Hashing](https://arxiv.org/html/2604.19351v1)

§3的学得query/key代理、residual和mask是具体训练/执行分支；§4.1.4/7明确prototype FP16模拟hash，1-bit打包内存与速度是理论估计而非native实测。额外蒸馏/编码不免费，LongBench局部退步，不外推SLO。Only是受限配方，不称DASH算法已在Ch45；apr20必要源与真实owner独立处置通过。

### [EVPO: Explained Variance Policy Optimization for Adaptive Critic Utilization in LLM Post-Training](https://arxiv.org/html/2604.19485v1)

§2–3将return残差的population方差与per-prompt sample EV门控连接，不能升级为policy-gradient/逐batch可靠性保证。Kalman式融合依赖误差条件，相关有偏critic反例保留；Limitations主动披露finite-batch未给concentration，不能因此永久Disputed。Table1预算512是32query×16samples，best-validation与warmup/LR差异不当全compute匹配。局部recipe仅报告，apr20必要源与真实owner独立处置通过。

### [The Cost of Relaxation: Evaluating the Error in Convex Neural Network Verification](https://arxiv.org/html/2604.18728v1)

§3–5区分凸过近似引入不可达点与有效鲁棒性证书的保守性；原文也承认证书仍可有效。随机ReLU/MNIST/Fashion的误差与radius实验不证明所有神经网络指数误差，矩阵乘积可能有抵消，且抽样域与小半径 envelope 不可混为同域。现有形式验证/评价边界没有被该有限配方改写，标准仅报告；apr01必要源与具体owner独立核通过。

### [Towards Scalable Lifelong Knowledge Editing with Selective Knowledge Suppression](https://arxiv.org/html/2604.19089v1)

§4/Eq8–10和§5将retrieval selector与首token prior suppression分开。正文的标量表述需消歧：共同scalar平移不能改变softmax；本次实际读作者当前pinned代码，P是完整词表logprob向量而非共同scalar，可澄清可操作实现，不证明该commit在April已存在或实验已复现。selector监督/检索与首token范围成本、后续token负效应保留；Ch20分布变换与Ch29外部知识context的长期责任没有被该配方取代，标准Only。apr01已独立核必要v1、固定commit向量实现及实际owner，通过该受限处置。

### [LogosKG: Hardware-Optimized Scalable and Interpretable Knowledge Graph Retrieval](https://arxiv.org/html/2604.18913v1)

§3.2–3.4/Alg1将frontier聚合与保留activated triple-ID恢复路径分开；subject完整邻接分区、degree平衡与LRU属于受限executor。Table4实体集合Jaccard不证明全部path provenance或truth，矩阵reachability不等path multiplicity，Table2/3含后端反收益与cache压力。Ch76 GraphRAG实际Traversal/Citation已有长期责任原则，具体执行配方标准仅报告；root必要源与实际owner独立核通过，不称整算法已有覆盖。

### [Superficial Success vs. Internal Breakdown: An Empirical Study of Generalization in Adaptive Multi-Agent Systems](https://arxiv.org/html/2604.18951v1)

v1 §2–4.2与Tables1/4–6测固定拓扑跨域时terminal accuracy与role/message代理分离；cosine×judge不是消息因果效用，100日志MAST错误率与行归一化heatmap不等全部运行失效率。Ch82“角色正确性必须独立于终局成功验收”实际承载role anchor仅sensor及单体fallback，root必要原文与实际owner独立核通过该窄Existing。C.4角色/连接交换有MuSiQue连接影响更大的例外，不称交流无用。v2时间晚于本窗，当前OAI晚日期不能单独改写v1公开归属；没有无必要版本diff。

### [SAGE: Signal-Amplified Guided Embeddings for LLM-based Vulnerability Detection](https://arxiv.org/html/2604.19031v1)

§3.2–3.4/4.4/5.2–5.3/Eq12的task×backbone SAE是冻结模型的派生probe，不是干预原模型恢复决策。class-centroid幅度及特征裁剪支持可预测性，不能证明功能语义导致失败；bug/fix标注中心窗口是特权定位，Table5precision/recall和小语言反向保留。Ch66 Attribution Contract已分probe与因果识别，本地配方深入仅报告；root必要原文与实际owner独立核通过，不否定实测局部收益。

### [DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging](https://arxiv.org/html/2604.19305v1)

§3.2–3.4/Alg2真执行插桩获得trace，但去日志后的逐行相同和compile不能证明observer effect为零；规则fallback亦改临时变量/控制结构。§4.5perfect fault localization、32patch与额外最多10次instrumentation调用分账。Table6plausible不等人工correct，去augmentation后二者分离；Ch80可执行诊断与外部effect重验原则已承载，受限修复配方标准Only，root必要原文与实际owner独立核通过。

### [Remask, Don't Replace: Token-to-Mask Refinement in Masked Diffusion Language Models](https://arxiv.org/html/2604.18738v1)

实际HTML/PDF-v1题摘一致，库存后发v3题摘不用于本次。§4–6/Alg1把可疑检测与替换动作拆开：重掩后让更新上下文重新填回，位置预算和每步cap限制循环。LLaDA2.1-mini、greedy/block32的BBH退步及AIME无收益保留；mask没有一般优势定理，硬件/precision/并发/SLO未披露。Ch24既有rewrite、噪声/软状态、proposal/remask与commit职责已承载长期选择，该局部动作对照标准仅报告，root必要源与实际owner独立核通过。

### [Discrete Tilt Matching](https://arxiv.org/html/2604.18739v1)

§2.3/3/Eqs11–19/4主表从冻结base rollout及reward构造masked状态，以exp(hr)加权局部CE/control variate匹配reward-tilted unmask posterior；理想terminal-KL界依赖对应条件律及完整期望，不证明有限训练或旧buffer精确。Eq17条件无偏不代表任意reward/c下sample target都非负。LLaDA8B/LoRA128/64、length256/block32/T128、8H100 Sudoku条件与MATH/GSM弱于SPG、大h/无control退步保留。Ch24 CTMC目标后已实际写入terminal reward→local posterior条件匹配两段，Ch31奖励设定/Ch33policy-gradient只交接；root源→owner与实际正文/相邻链路写后通过，不代表复现。

### [One Step Forward and K Steps Back: Better Reasoning with Denoising Recursion Models](https://arxiv.org/html/2604.18839v1)

§3/Eqs3–7/4/5以腐化目标初始化有限k次共享转移，在窗末监督并整窗反传，不等完整长链TBPTT或无条件训练/推理同分布。Ch24 ELT有限loop后已实际写入初始化来源×短窗末监督两段，区分prefix蒸馏与目标腐化课程。ARC pass@2/任务示例FT/checkpoint候选成本、预训退步与深度/数据混杂保留，额外k反传及窗口外验收非免费；root源→owner与实际正文/相邻链路写后通过，不代表实验复现。

### [Unlocking the Edge deployment and ondevice acceleration of multi-LoRA enabled one-for-all foundational LLM](https://arxiv.org/html/2604.18655v1)

§3.2将同尺寸LoRA矩阵作为固定图runtime输入，与多图共享base/全部adapter常驻mask不同；CTG A.1的共同prefill后suffix-KV隔离不授权任意adapter共享prefix。GalaxyS24/25、SM8650/8750与1B/3B受限配置；Table3的174和23×8+40不一致，Table4相对G-Eval不能称绝对准确率，不采用总体加速倍数。Ch49三类优化前已实际写入“静态图可以固定接口，而不必固定每个Adapter值”两段，Ch30训练/Ch45KV身份仅交接；root必要源→actual owner及实际正文/邻接写后通过，未复现实验。

### [Rethinking Dataset Distillation: Hard Truths about Soft Labels](https://arxiv.org/html/2604.18811v1)

§2–3、Table1/2及Figs1–2对比HL、固定SL与augmentation相关SL+KD，说明student-compute匹配不等teacher信息/总成本匹配；有限ImageNet/TinyImageNet对照支持subset质量排序可被监督来源改变，不推LLM软标签令数据无关。实际Ch27 patch/teacher/实际监督预算责任已承载长期原则，分类反证与方法仍值得标准报告，不称整套DD已Existing；root必要源/实际owner有限独立通过。

### [Semantic Needles in Document Haystacks: Sensitivity Testing of LLM-as-a-Judge Similarity Scoring](https://arxiv.org/html/2604.18835v1)

§2–4相同语义扰动在文档内部的位置/无关周边文本改变similarity，与交换两个candidate不同；五LLM、§2一至十九句及三种扰动不证明一般长上下文失效。四到八句仅首尾偏差切片，不能当完整范围。停止后补齐最大样本量、相关样本与GPT5方向例外保留，分布指纹非跨版本保证。Ch66 judge/输入证据预算与顺序扰动责任已承载采用原则，该受控配方标准Only由root有限独立通过，不采用语境解释的因果推断。

### [SpikeMLLM: Spike-based Multimodal Large Language Models via Modality-Specific Temporal Scales and Temporal Compression](https://arxiv.org/html/2604.18610v1)

§2–3/Eqs3–14把指定整数码转换为带符号加权spike时间累积，MED仅作分配proxy；不是任意浮点等价或权重全binary。§4.2算法与§4.3硬件分开：SMIC28nm综合、HBM/cycle模拟对A800 FP16/batch1，不能作同板部署倍数。Ch49低位LUT/ternary路径后已实际嵌入activation码×temporal权重接口两段（约753/755行），保留重复累积成本、scale/质量责任和dense/LUT回退；root非作者必要源、实际正文及邻接写后通过，不代表复现实验。

### [Beyond Explicit Refusals: Soft-Failure Attacks on Retrieval-Augmented Generation](https://arxiv.org/html/2604.18663v1)

§3–5以单恶意检索文档诱发流畅无信息输出，A.4各数据集初采100再按clean AUS≥4过滤，Table7不同配置排除8～33/100，最终cohort不是统一100。攻击fitness与三指标共用AUS，不是独立truth。模型/检索器及PPL数据集反向保留；Ch72已区分Containment、质量和可用性，受限payload/反证深入Only由root独立通过，不称整个算法Existing或所有过滤无效。

### [Beyond Indistinguishability: Measuring Extraction Risk in LLM APIs](https://arxiv.org/html/2604.18697v1)

II-C/III/Alg2及IV–V区分相对membership风险与绝对抽取；partial top-m未见目标时用实际概率，不是可得的完整rank worst-case界。GPT2/Enron及Llama3.1/Pile、BookSum是受控模型，不是商用API；V明确DP降低ratio，不因upper-bound比较否定其收益。Ch72已有prior/接口/攻击预算责任，估计配方及条件限制深入Only由root独立通过，不采用partial-logit certificate或全面否定隐私保护。

### [URoPE: Universal Relative Position Embedding across Geometric Spaces](https://arxiv.org/html/2604.18747v1)

实际v1 §3.1–3.3/Eqs1–10、§4主表/消融与0.C限制：标定相机射线在固定depth anchors升至3D，再投影到query view，以普通2D RoPE表达相对位置；同view退化2D规则，depth anchor不是逐点深度真值。§3.3把query-view维移到batch并重复K/V，kernel兼容不等单一KV可无成本复用。LVSM/nuScenes/UniMatch是有限范围，RGBD部分指标退步、联合规模recipe与标定依赖保留，不外推未标定场景/线上SLO。实际增量已嵌入Ch23参考位置/pose之后、native3D之前的两段（source-family `SF-2026-ARXIV-2604-18747`），区分query-dependent位置与执行视图。root必要Eq8/9、Table4及actual owner采用通过，并已独立顺读真实正文及前后衔接通过写后；Ch24/25仅交接，未复现实验。

### [Towards Understanding the Robustness of Sparse Autoencoders](https://arxiv.org/html/2604.18756v1)

实际v1 §3–6/Tables1–9：预训SAE在推理中以重构替换residual，base参数不变但攻击可穿过SAE求梯度；不是检测器或阻断梯度。Gemma/Llama/Mistral与GCG500步/后缀20、Beast及1500黑盒prompt是受测边界；bf16/NVIDIA GPU但SKU、完整服务SLO未绑定。跨模型30个off-diagonal与跨配置36对不能合并，层深并非单调，No-Suffix仍是有害prompt而非通用benign utility验收。spectral/Jaccard支持假说，不证明唯一因果或安全；Ch72 sensor/保护行为和Ch66评价责任已有原则，本局部干预仅报告，不称整套算法Existing；root有限独立处置通过。

### [How Adversarial Environments Mislead Agentic AI?](https://arxiv.org/html/2604.18874v1)

v1 §2–4/Tables3/5/7在固定tool-response proxy内分semantic DR与graph ER/BW，engagement是条件分母；Llama8/450实际engaged且7进陷阱，不可把低无条件率当鲁棒。11K pooled、各主表/新frontier有效样本不是统一配对预算，API error/abstention保留。Ch66可观察opportunity/过程探索及Outcome Witness提前失败不作安全已具体承载采用原则，不称整套新harness已覆盖；6分安全Deep拟Existing，待非作者核。

### [Where Fake Citations Are Made: Tracing Field-Level Hallucination to Specific Neurons in LLMs](https://arxiv.org/html/2604.18880v1)

v1 §2–4/Table2及§7：OpenAlex→二次web+judge的field标签不是全索引真值，唯一probe模型Qwen2.5-32B的CETT/FFN干预有可检查的field证据。但suppress改善title/author却使year/venue退步；五field配对统计及JSON100条不能推出普遍显著/fluency无损。Ch5可读/因果/原决策分权已有原则，本细分实验5标准Only，不称独立hallucination神经元已唯一识别；待非作者核。

### [Prioritizing the Best: Incentivizing Reliable Multimodal Reasoning by Rewarding Beyond Answer Correctness](https://arxiv.org/html/2604.18892v1)

v1 §3/Eqs1–8把verifier正确子集作tie-aware ranking并居中，K<2 aux归零；r=verifier+λaux再对完整组GRPO归一，负aux不是overall负reward。text-only gpt-oss20B不拥有visual truth或token因果credit。Qwen2.5VL7B/ViRL/G8/两epoch/step140与五bench各500的局部对照中，Group有MMMU-Pro退步；RCAcc=Acc−CBIR是joint accepted质量，非条件accuracy/faithfulness，总judgecompute未匹配。已在Ch33 Sequence Reward之后两段落实correct-only与fullgroup两个目标范围、零/单correct回退及额外judge成本。6gapDeep；root必要源/owner/literal采用核有效，apr01实际顺读正文与前后交接后通过，见[写后复核](../_sources/daily-20260422/V3_APR01_18892_WRITE_AFTER.md)，未复现实验，不预支日级Gate。

### [Harmful Intent as a Geometrically Recoverable Feature of LLM Residual Streams](https://arxiv.org/html/2604.18901v1)

v1 §3–5固定maxpool后选层/不同projection-angle读出，非不同pooling实测。effectiveAUROC符号校正和empirical ROC TPR@1%不是固定线上阈值保证；clean English single-turn、十二小模型四family及Qwen3.5扩展没有adaptive/multiturn验证。表示可读与refusal分离不证明训练因果，几何角度不同不证明组合独立信息已验。Ch72 Refusal与sensor/authority、Ch66 estimator-access与切片operatingpoint已实际承载窄采用原则；6安全Deep拟Existing，待独立核，未将局部RTX移动GPU时间外推免费监控。

### [Gated Memory Policy](https://arxiv.org/html/2604.18933v1)

III-B/Fig3/Eqs1–2、IV-C及V/VIII-E–F先独立训练memory-off/on policy，用另半数据action-error ratio标gate，冻结BCE gate再重训最终policy；不是固定同policy因果必要性。binary residual门与history动作diffusion噪声、有限滑窗分责，联合gate正则两侧有反益，多trial/最佳checkpoint/3080与5090不同配置不合成统一成功或SLO。实际Ch26 episode memory/敏感性已有，独立读门校准→冻结重训的训练分支已在Ch26实际写入两段；6gap深入，root已对exact-v1、正文和邻接完成非作者写后复核。

### [Reasoning Structure Matters for Safety Alignment of Reasoning Models](https://arxiv.org/html/2604.18946v1)

§3–6/Table5–6的PU→HA→CR SFT与移除/改写对照给出受限保护行为，不再按‘一般SFT’泛化关闭。1K含900harm/100benign，拒绝模板与权重变更不能证明所有风险由结构导致；真实ablation表full不是所有指标最好，CMMLU/over-refusal有反向。有限distilled LRMs非671B，完整运行配置未绑定。Ch29监督/Ch72模板与authority原则已有，本recipe仅报告不称全部Existing；6安全深入待独立处置。

### [Distillation Traps and Guards: A Calibration Knob for LLM Distillability](https://arxiv.org/html/2604.18963v1)

§5/Eqs6–11/Algorithm1与§6 Tables2–4冻结原teacher/proxy、先校准teacher，再蒸馏student；task/calibration分别groupnorm，与裸目标不同。text log-score可跨tokenizer独立算，不采用token逐项等价或通用IP保护。Gemma/Qwen有限对照的Table4部分KL反向、teacher效用非全部不变，相关共变不等唯一因果；H100校准另有成本，完整precision/服务SLO未绑定。Ch29现teacher匹配缺teacher可教性artifact前置校准分支，已在Ch29实际写入两段；6gap深入，root已对exact-v1、正文和邻接完成非作者写后复核。

### [Mechanistic Anomaly Detection via Functional Attribution](https://arxiv.org/html/2604.18970v1)

§3–5/Eqs2–6/Tables1–2及C.4/D.2/D.4用trusted reference的局部SGLD loss trace与test自预测伪标签相关，不是gold机制归属。sharp/flat support是条件假设；LLM AUROC只筛实际正常/触发子集，DER事后best threshold与offline test聚类不同合同。Gemma2-2B/Llama8B及H100百千draw多forward/gradient成本不可当线上单pass；完整precision/长度/并发/SLO ND。actualCh72 sensor/reference/authority原则已承载，但具体coupling estimator非全部Existing；深入仅报告新诊断/obfuscation反例及限制，待独立核。

### [Low-Rank Adaptation for Critic Learning in Off-Policy Reinforcement Learning](https://arxiv.org/html/2604.18978v1)

§4–7及D将冻结随机基座/低秩更新作为bootstrap条件下的正则化，而非免费PEFT；静态回归排序相反，作者成本也近似不变。Ch30随机scaffold107–111已有身份与dense成本，受限新排序仅报告，不称整套实现Existing。必要参数/评价与球面projection条件见证据笔记，待非作者处置。

### [Savoir: Learning Social Savoir-Faire via Shapley-based Reward Attribution](https://arxiv.org/html/2604.18982v1)

§3先重建coalition历史估计future utility再分信用；§5.2的Shapley-only按印出定义v(S)恒定，Eq4边际全零，不足支持其独立归因。D的样本计数例也不合所给公式。只隔离该归因/精确算法/成本采用，不否定全部SOTOPIA经验；不写Books，精确重开条件见§5，待独立核。

### [When Safety Fails Before the Answer: Benchmarking Harmful Behavior Detection in Reasoning Chains](https://arxiv.org/html/2604.19001v1)

abs/HTML-v1一致，库存旧题名不沿用。§3–6同标签逐级合并支持granularity边界；已筛harmful/partial trace、机器标签、best-layer sweep与不同parse分母不能升级线上固定安全monitor。Ch72 sentence-fence与sensor/authority分层已有限对读；新实测仅报告，待非作者核。

### [FedProxy: Federated Fine-Tuning of LLMs via Proxy SLMs and Heterogeneity-Aware Fusion](https://arxiv.org/html/2604.19015v1)

§4删block形成同坐标proxy、适配后覆盖原层；§5明确LoRA更新和约4倍迭代成本，不能将Alg1抽象训练φ写全参训练。IP仅减少直接暴露，绝对cosine权重不是同方向共识。Ch30组合admission及坐标/行为回归与Ch36通信对读后，受限替代配方仅报告，不为算法细节默认造Books缺口；[apr01必要原文及实际owner有限独立核通过](../_sources/daily-20260422/V3_APR01_TWO_19015_18966_INDEPENDENT.md)，不代表本日日期或来源Gate。

### [Personalized Benchmarking: Evaluating LLMs by Individual Preferences](https://arxiv.org/html/2604.18943v1)

§3–6只对115个至少25battle的用户、其实际比较过的模型计算个体rating。不同prompt/pair图及小样本识别仍混杂，低相关与p=.165不证明因果偏好或随机等价；rating回归改善非线上utility。actual Ch66 Judge Ranking217–230已保存pair/slice/uncertainty、子群抵消与population/release分权，具体原则已有覆盖，不称本算法全部Existing；5标准，apr20必要源/真实owner独立通过。完整必要记录见[独立审计](../_sources/daily-20260422/V3_APR20_FOUR_18943_19321_INDEPENDENT.md)。

### [Self-Improving Tabular Language Models via Iterative Group Alignment](https://arxiv.org/html/2604.18966v1)

abs/HTML-v1一致，旧库存题名不用。§3/Eqs5–10/Alg1及§5.4–6给高/低组log-ratio均值差→sigmoid双向梯度、scorer训练/评分分离及随机组/固定scorer反证；不是平均pair DPO。真实数据仍给scorer训练，MIA≈.5不成为privacy保证；结构fidelity部分退步、稀有模式平滑、额外训练/评分成本保留。Ch34 group目标/relative margin与Ch31 proxy责任对读后仅报告局部配方，不因逐算法未写入就造缺口；5标准，[apr01必要原文及实际owner有限独立核通过](../_sources/daily-20260422/V3_APR01_TWO_19015_18966_INDEPENDENT.md)，不代表本日日期或来源Gate。

### [Intentional Updates for Streaming Reinforcement Learning](https://arxiv.org/html/2604.19033v1)

§3–6先指定当前输出变化，再用局部线性敏感度反解scalar LR；trace分支计量聚合历史变化，运行估计非完整batch Jacobian。采样action的典型log-prob变化不等KL硬cap，action-dependent scaling会改变期望方向。§7.3/7.6–7.7的λ=0 fidelity、Finger-turn不稳和policy更新尾比反向均保留。actual Ch28 batch残差/Jacobian及函数动量链未表达这条scalar输出单位分支，已在Ch28实际写入两段；6gap深入，root非作者写后复核通过，不采用大模型或长期稳定保证。

### [Cell-Based Representation of Relational Binding in Language Models](https://arxiv.org/html/2604.19052v1)

§3.1–3.3用entity×relation索引PLS、定向patch和保索引扰动分开内容与绑定地址，支持局部行为相关，不是完整原生circuit或唯一存储。Ch5信息可读/使用阶梯已补这条双索引机制与跨语境坐标的受限分支；合成context、层/scale选择及translation边界见证据笔记，root已完成必要源→实际owner与正文相邻的非作者写后复核，未复现实验。

### [CHRONOS: A Hardware-Assisted Phase-Decoupled Framework for Secure Federated Learning in IoT](https://arxiv.org/html/2604.19053v1)

官方 exact-v1 §4.2–4.5 真有 idle epoch 的 TEE 内密钥建立/封存和恢复 share 分发、active round 一次性 mask 与掉线重构的时段合同，不能因 IoT/CNN 标签拒绝准入；Ch36 只有 federated `encode→merge→decode` 一轮类型界，Ch72 有 TEE/隐私 threat model 而未把 setup→active→recovery 的秘密状态生命周期合并成受限条件。原 v1 的20客户端 Rock Pi 4/OP-TEE、小/中 CNN 数据仅支持具体操作点：74%是小CNN的 active aggregation 缩短，排除约250ms每epoch idle setup；能耗为6.5W×延迟的推算，20客户端 Secure World 632B随参与方数量增长；B4 software-only已展示相位预计算但无硬件隔离。旧库存32-node/Orange Pi 5/<1.1KB是后发版本污染，不用于本日结论。

然而 §4.5 在真实掉线后让 server 从 shares 重构该客户端整 epoch 的私钥，原文亦明确可计算本 epoch 任意轮次 mask。若客户端在同 epoch 轮1正常发出 masked update，轮2真实掉线，honest-but-curious server 只需保留轮1自己收到的消息，合法恢复私钥后回算轮1 mask，即得旧单客户端明文更新。这与 §4.1 的“server不能重构任何单客户端梯度”中心目标冲突；§5.3 的掉线后禁止重入只挡未来消息，epoch rotation只挡此前 epoch。§7.6 的单次 masked-gradient inversion 未测试恢复后的历史回算；§5.4所披露恶意伪掉线也是另一问题。此为按作者印出协议与威胁模型推导、并获root定点独立复算的**窄反例**，不是作者确认的漏洞，也不否定所有安全聚合协议或局部相位调度经验。保留2+1+2=5准入分但因中心保证争议强制深入审阅，Books暂缓、不将保密或性能宣传写成Ch72/36正面保证；需能阻止同epoch已存消息按恢复私钥回算的具体修订协议与对应安全验证后定点重开。

### [Reducing the Offline-Streaming Gap for Unified ASR Transducer with Consistency Regularization](https://arxiv.org/html/2604.19079v1)

§2–4/Eqs1–5在最终RNNT(t,u)完整词表上对齐两可见context模式，辅助CTC对齐反而损害目标解码；half-batch DM与反向重算不等免费。128M/32A100/greedy batch128主对照、0.16s退步、XL数据caption冲突和C+R非tailSLO保留。监督对象分支已写入Ch24 CTC位置接口之后，并获[root非作者写后复核](../_sources/V3_ROOT_CH24_TWO_WRITE_AFTER_20260928.md)通过；6深入，不采用普遍Pareto或零kernel成本。

### [RARE: Redundancy-Aware Retrieval Evaluation Framework for High-Similarity Corpora](https://arxiv.org/html/2604.19047v1)

§3、4.1、5.1–5.5的等价支持映射、Coverage/PerfRecall区分重复document与必要信息。LLM等价/人工filter误差、跨domain混杂、E2E−PerfRecall不是参数知识因果均保留。该retrieval gold条件分支已实际整合于Ch66 RAG阶段归因前，[root非作者写后复核](../_sources/V3_ROOT_FOUR_WRITE_AFTER_20260928_B.md)通过；6gap深入，未复现实验。

### [SAMoRA: Semantic-Aware Mixture of LoRA Experts for Task-Adaptive Learning](https://arxiv.org/html/2604.19048v1)

原先题摘初筛把semantic routing、task scaling和专门化正则当作成熟MoE-LoRA配方组合而前分母关闭。apr01定点复核官方v1 §4.1–4.3、§5.1–5.3/Table1–2及B.1/C.2发现中心评价口径反证，故只恢复这一个纠错候选，不扩成全部局部adapter论文队列。官方Table1同九任务 Qwen 行的LoRA等权平均88.64与打印一致；SAMoRA等权平均89.45，不等于打印91.71。同支持集等权增益仅0.81pp，非打印3.07pp；每列增益最高1.60pp，共享非负归一权重也不能单独解释3.07pp。这里核的是主表聚合与效用归因，不能据此说单任务实验、方法或代码均错。

3+1+2=6，中心评价纠错深入；按[具名非作者审阅](../_sources/daily-20260422/V3_APR01_SAVOIR_NEXUS_SAMORA_INDEPENDENT.md)仅报告可复算的同九任务范围，隔离打印Avg及据此声称的优势幅度。Ch30已有条件容量、初始化与路由机制链，本地MoE-LoRA配方没有经该错误变成新长期训练原则，Books不新增。重开此隔离仅需作者澄清Avg定义、同支持集聚合或修正表；不等待无限附件，也未复现实验。日期由官方公告slot、连续身份及v1 Updated00:30:07Z/OAI04-22组合有界推断，Updated不是逐篇公开时刻；全日日级日期Gate仍待独立验收。

### [ProjLens: Unveiling the Role of Projectors in Multimodal Model Safety](https://arxiv.org/html/2604.19083v1)

§4–6的paired ΔE/SVD及rank-k干预补充整体ΔW/神经元统计阴性，norm相关非唯一因果。LLaVA7B四攻击与层/rank非单调、MathVista/POPE损害、需干净资产对照保留；actualCh72 provenance/sensor分权之后已补窄 diagnostic 分支，6安全深入，经[root 非作者实际写后复核](../_sources/daily-20260422/V3_ROOT_19083_WRITE_AFTER.md)通过，不签普遍修复。

### [Robust Continual Unlearning against Knowledge Erosion and Forgetting Reversal](https://arxiv.org/html/2604.19108v1)

§3/5/6三阶段forget/forgotten与retain保护提供连续删除的局部反证。Eq12累计集合改变mix，negative class margin/DBI不证明个人参数影响或多通道隐私，class-misaligned retrain仍有正margin，MUFAC也明确观察到 reversal。Ch72约265–268行的遗忘 observable/独立攻击验收与约2673–2675行的 concept suppression≠参数擦除实际承载采用原则；[apr20必要源/owner独立核](../_sources/daily-20260422/V3_APR20_FOUR_18946_19108_INDEPENDENT.md)通过有限仅报告处置。不因小模型拒绝其真实边界。

### [LLMs Know They're Wrong and Agree Anyway: The Shared Sycophancy-Lying Circuit](https://arxiv.org/pdf/2604.19117v1)

采用官方PDF-v1 pp3–9/§3–5；currentabs已有v4，未把晚修订直接纳入历史。位置重合不等方向相同，70B sufficiency不等necessity，Gemma零化28→81是迎合增加。单template、probe统计/CI重叠非普遍等价、白盒诊断非部署monitor保留。apr01实际必要v1及Ch5参数充分性/activation relay/行为恢复/粒度正文对读后，6分深入仅报告通过：现章已承载拟采用的一般解释边界，该来源新的有限方向与位置经验留Daily，不称整个circuit已在书中实现，也不因已有一般原则删除候选或反证。

### [Guiding Distribution Matching Distillation with Gradient-Based Reinforcement Learning](https://arxiv.org/html/2604.19009v1)

§3/Eqs1–7/Alg1与§4/Tables1–4以DMD隐式target作reward对象，target群/正负policy和原sample不同监督合同。SDXL Aesthetic低于CFG teacher、CLIP低于NFT、目标/score/reward成本及无完整硬件预算保留，4NFE不等端到端更快。Ch24 Few-step链已窄补target评分责任，并获root实际正文/邻接写后非作者复核；不采用全面消除梯度冲突保证，未复现实验。

### [Local Linearity of LLMs Enables Activation Steering via Model-Based Linear Optimal Control](https://arxiv.org/html/2604.19018v1)

§4–9及必要AppF将offline Jacobian/Riccati gain与online feature误差反馈拆开，局部线性/采样remainder不等开放输入认证，层horizon非完整自回归规划。toxicity降低伴PPL/MMLU代价，RTX4090实测TPS下降、攻击可利用actuator均保留。Ch31条件steering后已窄补反馈/漂移分支，6gap深入；[root非作者实际写后复核](../_sources/daily-20260422/V3_ROOT_19018_WRITE_AFTER.md)通过。Ch5仅probe交接，不把控制信号当authority。

### [FG²-GDN: Enhancing Long-Context Gated Delta Networks with Doubly Fine-Grained Control](https://arxiv.org/html/2604.19021v1)

§3/Eqs10–14保DPLR低秩形式而细化gate，再区分key/value scaling。Ch22 GDN-2已含erase/write分权，已仅补细粒度控制与chunk并行代数不能独立选择的窄分支。Table2/4退步、H800 BF16受限prefill开销及hybrid比例方向文字冲突保留；6深入，获[root非作者实际写后复核](../_sources/daily-20260422/V3_ROOT_19021_WRITE_AFTER.md)通过，不称全矩阵Adam或任意架构收益。

### [Policy Gradient Primal-Dual Method for Safe Reinforcement Learning from Human Feedback](https://arxiv.org/html/2604.19024v1)

§2–4在有限CMDP/Slater/已知可逆link条件下，以成对差和absolute harmlessness one-bit anchor恢复安全目标，平均constraint与逐轨迹hard安全不同。§5只10states4actions/模拟反馈，不是真人LLM部署；未遍历证明附件或复现。5安全理论必要深入，仅报告该条件比较而不称现有章节逐字算法覆盖；[apr20有限非作者审阅](../_sources/daily-20260422/V3_APR20_FOUR_19024_18845_INDEPENDENT.md)已核必要原文与真实owner，非日Gate。

### [Denoising, Fast and Slow: Difficulty-Aware Adaptive Sampling for Image Generation](https://arxiv.org/html/2604.19141v1)

§3–4/AlgS2先控制最大patch时刻，再形成异构状态；difficulty是velocity误差代理非校准uncertainty，fixed full-model NFE非逐patch稀疏执行收益。FID2.00差于1.96、随机阈值例外、未绑定硬件/SLO及新增head/训练成本保留。Ch24已补平均噪声与最大可用信息不同的训练support条件分支，并获root实际正文/邻接写后非作者复核；不从局部代理推出最优调度，未复现实验。

### [Nexusformer: Nonlinear Attention Expansion for Stable and Inheritable Transformer Scaling](https://arxiv.org/html/2604.19147v1)

Eqs12–14/§5.2全零新增块使GeLU新activation及回传耦合均零，普通fresh gradient无法推出AppC非零新梯度。只隔离该初始化→可学习增长桥，保初始function equality与有限nonlinear QKV经验；不能断言实际code无未披露bias/noise/moments。8A800预算比较非全compute、Table1/2反向结果及scaling R²条件保留。6纠错深入窄争议待非作者核；精确实现初始化和新块梯度证据可定点重开，不写Books。

### [How Do Answer Tokens Read Reasoning Traces? Self-Reading Patterns in Thinking LLMs for Quantitative Reasoning](https://arxiv.org/html/2604.19149v1)

§3–5按correctness/quality/SRQ筛池再CAA，SamePool只控制部分替代解释，非固定content纯操控reading。Table1错好trace/对差trace、AIME四题收益与API/white-box成本保留，max-prob非校准真值。Ch5/66已有一般分权，但非精确算法Existing；5标准Only保局部selection证据。[apr01必要原文及实际Ch5非作者核](../_sources/daily-20260422/V3_APR01_TWO_19015_18966_INDEPENDENT.md)通过，未复现实验，不代替日级Gate。

### [Mind the Unseen Mass: Unmasking LLM Hallucinations via Soft-Hybrid Alphabet Estimation](https://arxiv.org/html/2604.19162v1)

§4–5/AppB融合missing-mass与spectral支持代理，N100 pseudo-oracle非真实alphabet。Eq5措辞/打印与proxy归一不同不升真实Shannon风险保证；MAE改善不等AUROC均优，小n生成、NLI及spectral/参考成本保留。Ch66有限样本/低熵错已有一般边界，5标准仅报告新局部估计比较，非算法Existing，待独立核。

### [Learning to Credit the Right Steps: Objective-aware Process Optimization for Visual Generation](https://arxiv.org/html/2604.19234v1)

v1§3/Eqs6–14：w_t^i是terminal-alignment代理，c_k^i无t，实际时间×目标权重可分离；fixed-sample min-norm合法不推出clip后跨样本Pareto/step因果。Tables1/4 Aesthetic与ImageReward有反向切片；8/32H100、训练/推理steps与resolution差别和reward成本保留。Ch31/33已分proxy信用与真反馈，不为每个权重heuristic追加正文；6必要深入Only经[apr01必要原文及实际owner非作者核](../_sources/daily-20260422/V3_APR01_TWO_19015_18966_INDEPENDENT.md)通过，未复现实验，不代替日级Gate。

### [ShadowPEFT: Shadow Network for Parameter-Efficient Fine-Tuning](https://arxiv.org/html/2604.19254v1)

v1§3–4/AppA/B/D：shared shadow backbone跨depth但couplings按层；第 `l` 层先用已有 `s^(l-1)` 与输入 `h^(l-1)` 的差注入 base，得到 `h^l` 后再更新 `s^l` 供下一层，random-down/zero-up与auxCE分责。attached artifact不能按普通LoRA merge，detached s0/head另验质量，不等价运行深度交互；两表任务退步/额外预训预算与十次均值latency限制保留。Ch30固定S0/weight delta与depth-conditioned state、attached/detached非等价边界现已分账；6gap深入获[root非作者实际写后复核](../_sources/daily-20260422/V3_ROOT_19254_WRITE_AFTER.md)通过。

### [TEMPO: Scaling Test-time Training for Large Reasoning Models](https://arxiv.org/html/2604.19295v1)

v1§3/Eqs1–12/Alg1的policy test adaptation与周期labeled critic刷新是两条数据流；真实条件概率下variational identity不证明learned V已tight/无偏token信用。Tables1/2 heldout AIME26/OlymMath/GPQA有退步，adaptation集合不能都称未知任务；critic额外compute/配置ND保留。Ch31/33已有policy漂移→scorer刷新一般责任，Ch80反思非参数更新；6深入Only保有限recipe，不称精确算法Existing；[apr20有限非作者审阅](../_sources/daily-20260422/V3_APR20_FOUR_19024_18845_INDEPENDENT.md)通过，非日Gate。

### [HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models](https://arxiv.org/html/2604.19300v1)

v1§3–4/AppA/C/E配对构造/人工reference、valid query误拒与audio否定分开；keyword/数值/拒答解析仍是measurement sensor。Eq4/conditional分母措辞不升统一幻觉率，1000paraphrase均值不证全部invariance。Ch66拒答分布与EvalSpec/parser identity已具体承载所采用的一般分权，5标准Existing由[apr20有限独立审计](../_sources/daily-20260422/V3_APR20_FOUR_18943_19321_INDEPENDENT.md)通过，不称完整benchmark实现/全模型排序。

### [Text-To-Speech with Chain-of-Details: modeling temporal dynamics in speech generation](https://arxiv.org/html/2604.19330v1)

v1III/IV的共享decoder沿DAC首codebook时间decimation逐级masked refinement，不是只沿RVQ residual层增加细节。Fig2/IV-A仍有G2P/总duration predictor，不能据摘要写成无时长模块。TablesIV/V支持有限时间级数/编码选择，SeedTTS退步、20steps/level成本与缺RTF/MOS完整结果保留；两种条件链及旧方案共存已写入Ch24，并获[root非作者写后复核](../_sources/V3_ROOT_CH24_TWO_WRITE_AFTER_20260928.md)通过；6深入，未据此宣称通用延迟收益。

### [GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models](https://arxiv.org/html/2604.19398v1)

v1§3.2先budget prefix后补全空group，打印规则未重新扣款。两个group A两units、B一unit、cost各1/budget2/score.9/.8/.1使prefixA成本2、guardB成本3，存在A一unit+B的可行成本2配置；只否定此组合无条件硬cap，不否定STE/实测或断言代码无补偿。A100/BF16/512×512 calibration、参数proxy非latency预算及task退步保留。6纠错Deep窄D已获apr01必要原文/反例有限非作者核，需保护组预留/再投影或真实cost检查后定点重开；非全日Gate。

### [Lost in Translation: Do LVLM Judges Generalize Across Languages?](https://arxiv.org/html/2604.19405v1)

v1§3/§4.7/Fig4及A.6：三translator让32B judge平均68.8→64.4→58.1，排名稳定不等绝对测量纯净；回译约200例非全语言native review，Bengali300例只是局部。reference/judge相关不证明真值。Ch66约925–931的task/label/parser、lineage与native review实际已承载采用命题；5标准具体Existing待独立，运行条件/未复现边界见[必要笔记](../_sources/daily-20260422/V3_EVIDENCE_REVIEW.md)。

### [Unsupervised Confidence Calibration for Reasoning LLMs from a Single Generation](https://arxiv.org/html/2604.19444v1)

v1§3/§4/Tables1–2/A.1：离线100样本估modal-answer支持度，再以分割数据的ridge/isotonic部署单response score；不用gold不等零采样/辅助embedding成本。§6明确一致错误被继承、需刷新、未测开放多轮。36组合和shift平均不保证新域正确率；Ch66已有sensor/truth分权，5标准Only保精确局部实现而非算法Existing；[apr01必要原文及实际owner有限复核](../_sources/daily-20260422/V3_APR01_PENDING_FIVE_INDEPENDENT.md)通过。

### [Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning](https://arxiv.org/html/2604.19459v1)

v1§2–4/Tables3–8/AppA的阶段diff可抓后改axiom，Case177显示先错再自洽会漏；所谓locked仍允许改再flag，非硬拒绝。303题/三run pooled与unique分母、两stage调用/提示预算差、judge FP/FN均保留，未见gaming非证明不存在。Ch66约3279–3283及1244–1246实际分spec真值与proof/sensor，因此6保证边界深入具体Existing待独立，不改Books。

### [LBLLM: Lightweight Binarization of Large Language Models via Three-Stage Distillation](https://arxiv.org/html/2604.19167v1)

v1§4/Table3先W/G低bit训练、后固定W/G调activation参数，支持受限joint-error分支而非理论必要。bitmap也是存储，B/C公式只linear参数，Table9未给完整Serving合同；Table12与D.2 GSM数字冲突不采用。H10080GB/CUDA12.8、有限LLaMA/Qwen和质量退步保留，6标准Only获[apr01有限非作者核](../_sources/daily-20260422/V3_APR01_PENDING_FIVE_INDEPENDENT.md)通过，不凭低bit数字新增一般kernel原则。

### [Dual-Guard: Dual-Channel Latent Watermarking for Provenance and Tamper Localization in Diffusion Images](https://arxiv.org/html/2604.19090v1)

v1§3.1–3.3/§4.1–4.4/4.7把初始noise模型来源与最终latent内容anchor分开；Full闭集逐发行记录需round-trip reference约64KB，Lite不是主实证。key/reference未知black-box与自适应white-box威胁不同。Table6细text overlay recall .471、Table10 reference构建错配clean pass0对.997；高image detect不等精确region恢复。Ch72现key/transform/detector/攻击轨迹分权可解释一般责任，但不称完整算法Existing；6保护深入Only待独立，必要评价合同见笔记。

### [ST-Prune: Training-Free Spatio-Temporal Token Pruning for Vision-Language Models in Autonomous Driving](https://arxiv.org/pdf/2604.19145v1)

PDF-v1首页April22、18页，取代当前HTML晚日期正文。§4.1–4.4/Eqs4–9的temporal proxy+ring双邻view相似度不能当物理motion/object truth，独立view保留与temporal-first成本有实际条件。§5/Tables3–7绑定DriveMM、single RTX PRO6000/batch1；10%token的DriveLM/Lingo质量退步，模块顺序/预算乘法不普遍最优。5标准Only保时空裁剪局部反证，不新增成熟budget/selector原则，apr01已完成必要源、关键反证与实际owner的非作者处置复核；未复现实验，不替代日期或日级Gate。

### [Allo{SR}²: Rectifying One-Step Super-Resolution to Stay Real via Allomorphic Generative Flows](https://arxiv.org/pdf/2604.19238v1)

本轮官方PDF-v1成功恢复20页、必要pp7–14及Table2视觉核；不沿库存/HTML漂移摘要。Eq6二阶SNR定全局t*不等来源全分布匹配，Eq9–10配对直线路径不证明learned marginal单步exact或support不变。FLUX.1-dev/LoRA64、8A100/batch16/10k训练；Table2去ATM更高PSNR/更低FID与Full若干NR更好并存，50–200×是NFE非时延。5标准Only保SR约束取舍，不重复Ch24 trained-source compatibility主线，apr01已完成必要源、关键反证与实际owner的非作者处置复核；未复现实验，不替代日期或日级Gate。

### [Talking to a Know-It-All GPT or a Second-Guesser Claude? How Repair reveals unreliable Multi-Turn Behavior in LLMs](https://arxiv.org/html/2604.19245v1)

v1§4–5把初答正确/错误、answerable/unanswerable、三challenge及两cycle分开；去89ambiguous后2511answerable、2600unanswerable，多响应非独立同量题。固定36不是逐题等difficulty诱导，GPT近0与其他模型正log-ratio不作统一易诱导结论。trouble classifier和表面language辨识不是内部机制，RLHF解释未干预。5标准Only保局部反馈风险，不据此改变Ch80通用controller或模型排名，apr01已完成必要源、关键反证与实际owner的非作者处置复核；未复现实验，不替代日期或日级Gate。

### [DR-MMSearchAgent: Deepening Reasoning in Multimodal Search Agents](https://arxiv.org/html/2604.19264v1)

v1§3/Eqs2–11、§4/Tables3–5：跨batch结构得分乘性重权不能让零优势变非零，工具次数reward依赖gold正确性。3602 QA/2epoch/B128/8rollouts，160/200/225steps非同总compute；N10%反低于5%。仅保局部策略及长度/batch耦合，不采用因果step credit或通用收敛；标准仅报告，经[apr01有限非作者核](../_sources/daily-20260422/V3_APR01_PENDING_FIVE_INDEPENDENT.md)通过。

### [Multimodal embodiment-aware navigation transformer](https://arxiv.org/html/2604.19267v1)

v1 III–IV/Eqs14–25/TableII：robot尺寸条件的候选clearance预测、阈值分流与物理安全证明分开。三Isaac环境各100goal；部分经典TEB更高成功且零碰撞，full一场景低于LiDAR-only。Ch26已有generator/monitor分权，但尺寸条件候选排序与无safe候选回退仍是具体可检验分支，不能仅因现章有一般原则而前关闭；受限navigation operating point不当通用collision证书，保护深入仅报告获[apr01有限非作者核](../_sources/daily-20260422/V3_APR01_PENDING_FIVE_INDEPENDENT.md)通过。

### [Location Not Found: Exposing Implicit Local and Global Biases in Multilingual LLMs](https://arxiv.org/html/2604.19292v1)

v1§3–5、Limitations 与 Appendix E 已按 Books 采用作深入审阅：44个语义平行问题跨12语言/49 locale形成2156条QA，不是独立同量模板；BUS baseline与真实人口公平目标不同。32模型、80人工grader92%agreement不等全真值，multiplicity相关不能归因训练。root 对 exact-v1 与 Ch66 多语言段独立确认原文机制缺口并窄写：显式给定目标地区的知识测试不能覆盖含糊输入下的默认地区选择；旧显式测试继续有效。apr02 [非书稿作者实际写后复核](../_sources/daily-20260422/V3_APR02_19292_WRITE_AFTER.md)通过；澄清策略是书稿设计推论，原文未实验其效果，不采普适训练因果或修复保证。

### [Silicon Aware Neural Networks](https://arxiv.org/pdf/2604.19334v1)

官方5页PDF-v1 III–IV/Eqs2–4/TablesII–III：cell-area期望loss再argmax netlist，面积代理不等最终route PPA。SkyWater130nm post-layout模拟而非制造；TableIII15ns/352pJ与IV-C23.9ns/2nJ冲突，准确率/面积取舍仍保留。受影响数值深入、只报告co-design局部方法，待独立。

### [Malicious ML Model Detection by Learning Dynamic Behaviors](https://arxiv.org/html/2604.19438v1)

v1§2.5/3.1/4.2–4.7/5–6：Docker/strace任务聚类OCSVM依赖标签与非anti-debug假设，25k多为synthetic，真实25/4/17分组不合并。未命中与正常trace不证明可授权执行，sandbox也不是逃逸证明。Ch72加载隔离/发布权限实际主线已分层；保护深入仅报告，待独立。

### [Involuntary In-Context Learning: Exploiting Few-Shot Pattern Completion to Bypass Safety Alignment in GPT-5.4](https://arxiv.org/html/2604.19461v1)

v1§4–6：abstract operator framing与示例排列的攻击对照成立，但3479探测包含不同ablation/模型/target，HarmBench24%与operator50/50分母不同。p=.891不证明温度等效，未干预识别induction-head或验证effect。保护深入仅报告，不普遍否定alignment；日期无OAI须邻界联合核。

### [TS-Attn: Temporal-wise Separable Attention for Multi-Event Video Generation](https://arxiv.org/html/2604.19473v1)

v1§3.2–3.4/Eqs1–11、§4/Tables1–4：完整text context不变，按subject区域proxy×event interval只改对应frame query的早期cross-attention bias。单A100/81frame/StoryEval423，846→863s含分段成本，judge与首帧生成不是物理真值；窄机制和回退已实际整合进Ch24运动条件后的局部时序路由段，[root非作者写后复核](../_sources/daily-20260422/V3_ROOT_19473_WRITE_AFTER.md)通过，未复现实验。

### [Compile to Compress: Boosting Formal Theorem Provers by Compiler Outputs](https://arxiv.org/html/2604.18587v1)

§3.2–4.3/§5.1–5.4，当前problem/proof及compiler行号反馈替代完整历史；该状态有损而非充分统计量。Kimina8B/Goedel32B的train量不同，采样64/128/256非同token/编译/value成本，保局部退步。Ch75任务保真/原文回退、Ch79 canonical state原则继续；仅报告局部refinement recipe，不把value标签当成功概率。2+2+2=6标准，待独立。 精确日期字段与必要证据详见本轮笔记；未取得披露的运行条件不补造为配置保证。

### [Towards Optimal Agentic Architectures for Offensive Security Tasks](https://arxiv.org/html/2604.18718v1)

§4–6/Table1，同20target/5topology/3model/2可观察性=600core，另60stress不混；partial不等动态validated，whitebox开放同目标source。SAS便宜快、独立MAS更高validated且whitebox区间重叠，不推唯一拓扑最优。M1Max/64GB/2并发/1800s限，remote API预算不同，受限任务费用非总部署成本；实际Ch82 verification成本原则保留，5标准Only获[apr20有限独立审阅](../_sources/daily-20260422/V3_APR20_THREE_18718_19354_18804_INDEPENDENT.md)通过，非日Gate。精确日期字段与必要证据详见本轮笔记；未取得披露的运行条件不补造为配置保证。

### [LLM-as-Judge Framework for Evaluating Tone-Induced Hallucination in Vision-Language Models](https://arxiv.org/pdf/2604.18803v1)

官方23页PDF-v1 pp6–9/14–18已实际读取；800×5tone/9VLM，rule H-Rate与image-blind judge severity分开。仅717图通过后验设计审计，但主表明确仍用800，不能改称717实验分母；Table2 的 InternVL14.40/DeepSeek52.18/Gemma4 2.05 与相邻正文3.42/61.80冲突，不采用统一排序。5分评价纠错深入，保局部非单调证据，不推synthetic absence已逐图验真或通用因果；[apr20 PDF-v1必要页独立审阅](../_sources/daily-20260422/V3_APR20_FOUR_19024_18845_INDEPENDENT.md)通过，非日Gate。精确日期字段与必要证据详见本轮笔记；未取得披露的运行条件不补造为配置保证。

### [Do Agents Dream of Root Shells? Partial-Credit Evaluation of LLM Agents in Capture The Flag Challenges](https://arxiv.org/html/2604.19354v1)

§3–6/Table3：3summarizer×4judge受控表中Grok summary均负κ，改judge不能修已失证据，原‘仅CTF任务扩展’理由撤销。60人工trace、10model×10task×3run/60step/default配置；writeup checkpoints非任务全成功。§6一例target VM停后agent继续host活动、作者patch未给完整防护实现，保护失败必要深入，仅报告受限观察/评价，不推发生率或充分防护。[apr20有限独立审阅](../_sources/daily-20260422/V3_APR20_THREE_18718_19354_18804_INDEPENDENT.md)通过，非日Gate。精确日期字段与必要证据详见本轮笔记；未取得披露的运行条件不补造为配置保证。

### [Geometric Decoupling: Diagnosing the Structural Instability of Latent](https://arxiv.org/html/2604.18804v1)

精确v1 §3.1–3.5/4.1–4.3/5/6及Appendix I。random-subspace有限差分Jacobian、主方向旋转LC与其Laplacian方差PHFE是操作代理；同seed normal/OOD的相关性改变不证明语义失败由曲率引起。§6.1/Table9在SD3.5的500 Normal＋500 OOD设计集上给LC/PHFE AUROC 0.816、裸LC 0.427、LS 0.199；“annotation-free”仅指推理评分无需逐图标注，AUROC仍依赖设计集Normal/OOD标签。Appendix I承认Jacobian估计昂贵，难以实时推理，且失败未显现时几何信号也不触发。SD3.5/FLUX有限样本中LC–PHFE相关下降；Base/Turbo更换训练pipeline而非单独操纵曲率，作者也承认还需专门训练干预。5分中心因果主张必要深入；仅报告局部诊断，不作普遍root-cause/发布sensor。未复现，配置不足不补造；[apr20有限独立审阅](../_sources/daily-20260422/V3_APR20_THREE_18718_19354_18804_INDEPENDENT.md)在此补证后通过，非日Gate。

### [Multi-Domain Learning with Global Expert Mapping](https://arxiv.org/html/2604.18842v1)

精确v1 III-A–C/Algorithms1–2、IV-B/G/H/J。LP affinity/capacity→静态domain/class map不同于在线token质量保证，DINO/ViT有限结果可保留。符合III-B的m>n反例取m=3、n=2、capacity=(2,2)，w行(1,0)、(1,0)、(0,1)：唯一LP最优三项均1，L=2，打印Algorithm1的小数bits均0，返回全零而OPT=3，不满足完整assignment或Eq6任意ε<1；Algorithm2末尾fallback是另一实现，不能补证Algorithm1/Eq9。6分纠错深入，仅隔离这组保证，不断言实际代码同错或否定有限实验。apr01必要原文/有效域反例有限非作者通过，重开需端点1处理、真实算法与对应证明；非日Gate。

### [Dual-View Training for Instruction-Following Information Retrieval](https://arxiv.org/html/2604.18845v1)

v1 §2–4/Tables1–2。同文档正负对在互补instruction下交换标签，DV替换等量样本，不把双视角当完全等总训练成本。305M gte/bge-m3、30hard negatives、512长度、温度.02；100生成样本单annotator审后无进一步filter。Ins-DV改善pMRR而general Score21.33→19.73/InstructIR89.16→87.97，混合数据才部分兼顾。5标准，仅报告标签控制与取舍，不宣称所有语言/检索任务最佳或全部合成标签可靠；[apr20有限非作者审阅](../_sources/daily-20260422/V3_APR20_FOUR_19024_18845_INDEPENDENT.md)通过，非日Gate。

### [Hierarchically Robust Zero-shot Vision-language Models](https://arxiv.org/html/2604.18867v1)

v1 §1/3/Eqs10–16/Theorem1、§4/Tables3–4。把image/text hierarchy和PGD训练层级结合，leaf防御对superclass攻击的失配是实际保护边界；hyperbolic log-margin是固定角度/范数条件下几何量，不等输入空间认证radius。CLIPViTB32、ImageNet训练、14zero-shot集合、3-step训练PGD/20-step及CW/AA测试和半径分开。6保护深入，仅报告这条有限攻击/收益分支，不作全威胁覆盖或全规模VLAsafety承诺。

### [Less Is More: Cognitive Load and the Single-Prompt Ceiling in LLM Mathematical Reasoning](https://arxiv.org/html/2604.18897v1)

v1 §4–9/Tables2–7。45+prompt在可见69/200/400标签split反复设计，不能当独立heldout泛化或信息论上限。AN45c在本地hard3 n=400、Together AI bf16得79.25%，但§9/Table7官方hard3 n=20、DeepInfra bf16仅55.5%，低于同官方无cheatsheet基线56.3%；本地增益不是稳健prompt增益，题集与执行提供方同时变化，不能单独归因哪一项。AN38官方65.3%亦只属该小样本/配置。Gemma2048→8192 token的错误退出与模型能力分开；非单调和规则合并退步可报告，但§8的有限搜索不能证明任意静态prompt无法条件路由，normal recall不能推出hard任务92%理论ceiling。5分中心解释必要深入，窄Only不否定所有实测；root已独立核该反例与限域。

### [Gradient-Based Program Synthesis with Neurally Interpreted Languages](https://arxiv.org/html/2604.18907v1)

v1 §3.1–3.4/4.1–4.5，leave-one-out IO监督、primitive复用正则、Gumbel-codebook和共享循环executor；测试优化程序latent而非改executor权重，最终执行soft表示不宣称硬符号真值。三seed固定20长度Shift/Comp任务中base/先验search不能替代gradient search；去recurrence/interpreter离散化明显退步，DeepCoder新生11.6M与有gold程序baseline分开，LPN另有更强重排序。5分实际Ch5组合计算分支已获[root非作者写后复核](../_sources/daily-20260422/V3_ROOT_18907_WRITE_AFTER.md)通过，正文保离散codebook身份、受限自建任务与算力/可验证性边界。

### [Disparities In Negation Understanding Across Languages In Vision-Language Models](https://arxiv.org/html/2604.18942v1)

v1 §2–3/Tables1–2。COCO5914四caption选择翻译七语言，每语言仅30人审，不叫全量人工truth。英语τ=.92的SpaceVLM在Chinese/SigLIP31.9→12.4、Arabic/Multi40.6→34.5、Russian/Multi43.3→36.3退步；修复不是所有语言稳定改善。形态、脚本、训练频率未分离，不采用typology单一因果或重新训练建议已验证。5标准，仅报告这组修复迁移反证，主线不是仅新增benchmark。

### [Beyond One Output: Visualizing and Comparing Distributions of Language Model Generations](https://arxiv.org/html/2604.18724v1)

旧宽库存的泛化前关闭遗漏了对评价人员“看多次生成分布”的具体贡献判断，现经[root非作者定点准入复核](../_sources/daily-20260422/V3_ROOT_18724_INDEPENDENT.md)恢复为5分标准候选。exact-v1 §6.2 的token graph让受测人员更准判断相对多样性（准确率均差+0.12，95% CI 0.03～0.21），但原始列表在单分布细节（graph差-0.057）和细粒度双分布比较（graph差-0.10）更准；§8限于实验室界面，不证明混合界面或生产评价收益。Ch66当前已要求保留重复样本、原始输出与聚合结论的不同证据身份，GROVE是这个原则下的有损概览实例，暂不新增长期机制正文。abs-v1的20 Apr提交与DataCite 22 Apr创建、v1 Updated 22 Apr 00:04Z都不是单独首发凭据；该ID位于本日已联合核的早字段连续批次，按官方公告slot有界推断08～09 BJT，仍待整日日级日期Gate确认。

### [HarDBench: A Benchmark for Draft-Based Co-Authoring Jailbreak Attacks for Safe Human-LLM Collaborative Writing](https://arxiv.org/html/2604.19274v1)

旧宽库存把协作写作安全实验泛称成熟偏好优化而前关闭；作者重开 exact-v1 §3.2–3.3、§5.1–5.3/Tables1–4 后发现决定性评价切片：同一有害草稿从无任务包装改为编辑/扩写包装，八个受测模型的 GPT-4o-judge harmful completion rate 均升高，GPT-4o 目标模型在该配对中为23.50%→96.75%。这表明直接有害请求或裸草稿的拒答不能代替“危险草稿可见但被赋予合法编辑角色”的工作流验收；Ch72 的 pre/post-guard、输入可见窗口和语义改写主线尚未明确此配对切片，故2+1+2=5且安全评价失效触发窄深入。[apr01非作者准入审计](../_sources/daily-20260422/V3_APR01_19274_ADMISSION_INDEPENDENT.md)确认旧前关闭理由不成立，但没有代替 Books 决定。

实验限定四域各100固定测试、手工包装与 GPT-4o judge，不是生产危害率；HQ 与 CoJP 同时变动草稿/长度/包装，只有 CoJP 无/有任务包装是较窄对照。Table2 标题写 unsafe response rates、解释却称 prompts classified as unsafe，检测对象未自洽，85%→22% 不作前置 guard 漏检率；Table4 训练配方和 benign utility 的评价器亦不同，不采普遍 KTO/GRPO 安全—效用保证。其 `v1_updated` 为04/22T00:45:51Z、DataCite created 为02:12:57Z，前者仅和官方 slot、连续身份/OAI 批次合用作08～09 BJT 的有界公开推断，后者已在本窗截点后且不作首发钟。root 在 Ch72 Guardrail 主线窄写协作编辑配对验收及成本/放行权，apr02 对官方 exact-v1 与实际新增段落、相邻衔接完成[独立写后复核](../_sources/daily-20260422/V3_APR02_19274_WRITE_AFTER.md)。本项可计真实整合，但不替代日期、来源与整日日级 Gate。

## 5. 缺口与下一步

本节外部来源、日期与中心争议均为终态保留项，不支持正面证据、Books 或无遗漏断言；仅在取得各项所列官方目录、精确发布时间、原始配置或受控反证时按具体家族定点重开。普通可执行待办为零。

普通可执行待办：无。以下保留外部来源/日期和中心争议的精确重开条件；它们不用于正面采用或“零遗漏”断言。负侧 `2604.19406v1` 的旧“没有独立 holdout”理由已撤销：官方 exact-v1 确有五人千余pair用户研究与外部GEdit-Bench。root [有限非作者准入复核](../_sources/daily-20260422/V3_ROOT_19406_REVERSE_ADMISSION.md)确认其整体局部收益，同时指出同一 scorer 筛样、作RL reward，主要组件消融仍用作者 HP-score，未分辨各环节对最终人类效用的贡献；Ch31 已拥有候选分布、代理reward、独立效用的长期责任链。维持具名前关闭，不当零价值或无评测，不改变最终99/69/2；其余负侧已按共享理由分层抽检，范围见§6。

170份完整题摘的相关范围已冻结为99个工作家族；原162集合的反向恢复与关闭证据仍保留，新负侧抽检把18724从旧泛化前关闭恢复为5分标准Only、19053恢复为中心安全争议、19274恢复为安全评价候选，并对19087、19301、19457、18660、19185、19059、19342、18857、19071、19201、19321、19440给出具名关闭。原审读和独立抽核仍保留在_sources；前关闭不是论文得零分。30项Books整合已完成实际写回并经非书稿作者写后复核，19274 的 Ch72 采用待办已关闭。19117已获有限非作者深入仅报告处置。19354交叉评价反证撤销原“只有CTF任务扩展”疑问，19540成熟组合已具体关闭。不扩515宽库存为全文队列；整日来源、日期和负侧已按§6的限定范围完成独立语义复核。19125经root非作者定点重判、19105经作者侧反核均从候选降为具体前分母关闭；原证据留在_sources，不作为零分候选。

19398只隔离上述打印prefix+nonempty guard的无条件预算可行性，现有经验/STE不被整体否定。需可核保护组成本预留、扣减/再投影规则或实测每步mask成本才能重开；该窄反例已由apr01独立核，不用普通待审冒充外部受阻。

18982 Savoir中心归因保留项：印出Shapley-only的coalition值恒定、KernelSHAP baseline/端点处理与D样本计数无法支持所述独立归因及精确成本；当前不进入Books。实际coalition值与对应消融实施、端点/baseline及simulation计数可作替代材料，只定点重开本项；apr01已对必要主文/直接D与窄反例独立核验，不追完整代码/版本史。

19147 Nexusformer仅隔离打印全零新增块→非零梯度/可学增长桥，未否定有限经验或初始函数保持。重开需精确bias/非零耦合/扰动/optimizer-state说明和新增块梯度/受控学习证据；apr01已对必要公式/打印初始化与窄代数反证独立核验，非全日Gate。

已完成的单篇工作（过程记录）：显式单篇必要终态已由非作者逐组有限复核到尾，[19438/19461/18587 的最后一组](../_sources/daily-20260422/V3_ROOT_THREE_19438_19461_18587_INDEPENDENT.md)已通过窄评分与仅报告判断；不等于对99篇全部实验复现或全量逐篇双审。18943/19300、18874/18901/19405/19459的窄Existing已由apr20_resume必要源与真实owner独立通过，19444/19167/19264/19267的受限Only获apr01有限独立核，18724由root独立准入为标准Only，19053的同epoch旧轮反例亦由root复算通过。19087因特权oracle option与部署policy同预算收益的证据断裂，经apr01独立同意具名前关闭；19301因无客观 gold 的社会投票变化未改变Ch82协作/提交/评价责任，经[root有限非作者准入复核](../_sources/daily-20260422/V3_ROOT_19301_REVERSE_ADMISSION.md)具名前关闭；两项原必要审阅均保留在_sources。19201/19321的早期证据审读保留，但其长期贡献准入已由root反向校准为具名前关闭。此前普通Books提案19052/19009/19141/19274/19292均已实际写回 Ch5/Ch24/Ch72 并获非书稿作者写后复核，不再列普通待办。19117反向Only已通过；19299、19004、19093已具体前关闭，后两项root反向抽核；19048主表聚合反证已获apr01独立必要核验并恢复为仅报告纠错候选。最终集合与日级限定审阅见§6；普通待办为零。

本窗外部隔离：§2明确的历史目录不可访问是覆盖保留项，不支持零更新/零遗漏。Seed3D2.0 official article1443的CMS Publish=04/21T16Z呈共同日桶，不能证明真实发布钟；其技术正文已可读，但不评分或采用，需可核官方时区/发布时间或同正文更早公开依据后定点重开。19503的v1 Updated=2026-04-22T01:01:28Z/OAI05-12、19533=01:03:44Z/OAI04-24不足证明本窗09:00前公开，日期隔离，不评分或采用；需更早官方公开依据定点重开，不机械迁日。Google DeepMind [Image Generators are Generalist Vision Learners](https://deepmind.google/research/publications/240658/) 只标 `2026-04-22` 日精度而未标时区/时刻；对应 [arXiv:2604.20329v1](https://arxiv.org/abs/2604.20329v1) 的提交字段不是公告时间，且身份接近相邻公告批次。无法据官方页面的自然日证明它在本窗04/22 09:00前公开，暂作相邻日日期线索，不纳本日170题摘/99候选或正面Books；需可核的官方发布时间/公告批次依据定点重开，不因此扫Google整站。19540已贡献关闭，无须继续追日期；DataCite单字段不是公开依据。旧515条日期未清洗宽库存另含19857，虽其04/21投稿落本窗，但[官方月列表身份顺序、OAI04/23、v1 Updated04/23与公告槽的联合反查](../_sources/daily-20260422/V3_EVIDENCE_REVIEW.md)支持04/23批次推断，故不进入本日170题摘/99工作家族；04/23独立日期复核负责最终归属，不能从投稿时间前移。

SRC-ARXIV 的[作者侧官方补检](../_sources/daily-20260422/V3_ARXIV_OFFICIAL_BOUNDED_DISCOVERY.md)已实际查询12分类各自的主题同义词与04月目录完整分页，记录查询式、页段与停点。初次相邻250条抽取的305身份是阶段范围；目录并非全局按 ID 单调排序，扩到完整月页后临时ID带内357个去重身份全在旧515原始库存，未发现新身份。与正式99候选反向对账为92固定分类月页命中、7其他分类具名单篇定点来源，不能称99项均由固定分类发现。Atom 的 Submitted 日期仅用于发现，不能证明首次公开。该补检消除了旧收据不能替代官方入口的作者侧待办；非作者对主题范围、定点线索、公告批次、负侧与 Date Hold 的限定审阅见§6，不将目录补检本身当作全面召回证明。

## 6. 复核

复核者：root、apr01、apr20_resume，均非本报告作者apr02。

结论：通过

本次通过限于下述来源、日期、负侧及 Books 的已核范围；未证明全网零遗漏或实验复现。

[root 独立日级语义 Gate](../_sources/daily-20260422/V3_ROOT_DAILY_GATE_20260422.md)核对14/14个注册来源入口及停点，保留七个不可确证的历史目录为受阻；官方 arXiv 十二分类月页在目标 ID 带内发现357个去重身份，正式99候选中92个可在该范围命中、7个由其他分类具名官方入口定点确认。官方公告规则、连续 ID 与版本字段共同支持99项落在北京时间本窗08:00～09:00的有界批次推断，不声称逐篇秒级公告日志；19503/19533、Seed日桶及Google相邻日线索继续日期隔离。170份完整题摘已冻结为99候选、69具名前关闭、2日期隔离；99候选为30项真实整合、9项具体已有覆盖、55项受限仅报告、5项窄争议，普通待办0。负侧69项按共享理由分为范围外9、局部任务/产品24、有真实局部机制但无长期新选择10、成熟机制组合26；root新增逐项抽核18780/19262/19395/19211及旧具名恢复/关闭样本，未逐篇重审69项。30项整合均有真实书稿落点及非作者写后复核；五项争议不作正面Books采用。校验仅证明结构及差异洁净，不替代以上语义复核；下文过程时点的“待审”“未通过”及旧计数均非本日报终态。

最新反向准入：root 对 `2604.19457v1`、`2604.18660v1` 的官方 exact-v1 与 Ch66/72 实际 owner 做[有界非作者复核](../_sources/daily-20260422/V3_ROOT_19457_18660_REVERSE_ADMISSION.md)，确认两篇分别是已有评价分账下的合成企业实例、已有泄漏判定合同下的教育场景实例，没有改变长期数据、控制或验收责任。故两项从原标准/深入 Only 候选转为具名前分母关闭；原必要审阅保留在 `_sources`，不把关闭说成零分或无研究价值。当前170份完整题摘=99项未冻结工作候选+69项具名关闭+2项日期隔离，99=30项实际 Integrate+9项具体 Existing+55项 Only+5项窄 Disputed。[apr20 三项有限独立核](../_sources/daily-20260422/V3_APR20_THREE_18718_19354_18804_INDEPENDENT.md)在18804的§6.1/Table9标签分母补证后通过18718/19354/18804；[root 最后三项有限非作者核](../_sources/daily-20260422/V3_ROOT_THREE_19438_19461_18587_INDEPENDENT.md)通过19438/19461/18587的必要 exact-v1、评分与窄仅报告处置。18587的03/13是 submitted，不构成04/22公告反证。显式单篇待核清零；来源、日期、负侧及整日日级 Gate 仍未通过。下文其他数字是发生当时的阶段快照。

作者侧 SRC-ARXIV 实际补检见[独立原始入口记录](../_sources/daily-20260422/V3_ARXIV_OFFICIAL_BOUNDED_DISCOVERY.md)：12分类主题查询及04月整月目录均有查询/分页/停止范围，临时ID带内357个去重身份全在旧515原始库存。此项尚未获 root 的日级来源语义验收；其 357 不是候选数，主题召回与首公开仍按记录中的限制解释。

18933、18963、19033 三项已由root分别对官方 exact-v1 关键方法/限制、Ch26:378–403、Ch29:207–230、Ch28:441–462 的实际新增正文与邻接完成非作者写后复核，三项通过；这只支持这三项的实际写入，不替代剩余候选、来源与日期日级 Gate。未复现实验。

19473 exact-v1 条件读取机制经 root 写前准入，Ch24 运动条件→时序 bias→Plan/Validate 的真实新增正文、Review note 与邻接已获[非作者写后复核](../_sources/daily-20260422/V3_ROOT_19473_WRITE_AFTER.md)通过；当前实际整合计17项。它不证明本日日级 Gate 或生产SLO，未复现实验。

19047 的冗余语料 retrieval-gold 机制经 root 有限写前判定，Ch66 的 required-information→可替代支持集合、部分/全部信息覆盖与答案正确分账已实际入正文；[非作者写后复核](../_sources/V3_ROOT_FOUR_WRITE_AFTER_20260928_B.md)核了原文与两侧论证，当前实际整合计18项。过滤 precision/标注成本和无因果参数知识结论均保留；该单篇不替代日期、来源与否定侧终审，未复现实验。

19079、19330 两项语音条件链已写入 Ch24 正文，分别明确离线/流式最终 RNNT 分布的监督对象，以及时间降采样首 codebook 与 RVQ residual 层级的不同责任；[root 非作者实际写后复核](../_sources/V3_ROOT_CH24_TWO_WRITE_AFTER_20260928.md)通过，当前实际整合计20项。双模式/逐级成本、退步和仍需总时长预测均保留；这两项不替代整日来源、日期、准入与证据 Gate，未复现实验。

19021 的逐通道 delta 更新已在 Ch22 GDN 后补足左乘仍 rank-one、但失原对称 WY 降低形式，以及双边缩放保持 chunk 结构的条件分支；[root 非作者实际写后复核](../_sources/daily-20260422/V3_ROOT_19021_WRITE_AFTER.md)通过，当前实际整合计21项。Table3/4 反向、固定 H800 配置与旧标量/KDA/Attention 共存均保留；不替代整日 Gate，未复现实验。

19083 的 projector artifact 安全诊断已写入 Ch72 soft-channel 与 Artifact contract 之间，分开 clean/poison 同输入下的权重、输出残差、probe 与最终行为；[root 非作者实际写后复核](../_sources/daily-20260422/V3_ROOT_19083_WRITE_AFTER.md)通过。低秩干预的模型/攻击/效用限制与未知 trigger 回归保留，不称普遍修复；本项不替代整日 Gate，未复现实验。

19018 的 offline Jacobian/Riccati gain→online feature-error feedback 已写入 Ch31 条件化 Activation Intervention 的演进链，并经[root 非作者实际写后复核](../_sources/daily-20260422/V3_ROOT_19018_WRITE_AFTER.md)通过。网络层深不等未来 token 规划，PPL/MMLU/TPS 与局部漂移/独立 safety authority 均在正文保留。本项也不替代整日 Gate，未复现实验。

19254 的随层深演进 shadow state 已写入 Ch30 固定 S0 与 Merge 两种旧路径之间；经[root 非作者实际写后复核](../_sources/daily-20260422/V3_ROOT_19254_WRITE_AFTER.md)纠正同层注入/下一层状态更新顺序后通过，当前实际整合计24项。detached 另属预测资产，质量/运行成本与 schema/reset 边界保留；这不代表日级 Gate 或部署 SLO 已通过。

18907 的训练期离散 primitive/codebook 与共享递归 executor、测试期冻结执行器优化 program latent 已进入 Ch5 compositional usefulness 链；[root非作者实际写后复核](../_sources/daily-20260422/V3_ROOT_18907_WRITE_AFTER.md)纠正初稿“连续身份”与端到端对照歧义后通过，该单篇通过时累计25项。受限自建程序合成语言、搜索计算与程序可验证性边界保留，不推通用 LLM 编程或日级 Gate 已完成。

19125 的完整题摘与 Social-Chem/ETHICS 道德接受度、情绪措辞对照由 root 独立重判：局部行为评价可成立，但没有对本项目长期模型/Infra机制、平台 release contract 或设计选择给出足够增量，因此从候选降为具名的前分母关闭。原始身份和旧审阅留在 `_sources`；这一单项反向校准不证明其余工作候选均准入正确。

19105 的完整题摘、两阶段监督/生成及 Joint-Tuning 对照经本作者定点重判：它在 egocentric human-motion 任务上给出局部质量取舍，但未独立量测所宣称的梯度冲突，也未改变 Ch23 已承载的共享语义接口、独立生成 head 与分阶段冻结/解冻选择。已从正式候选移为[具名的前分母关闭](../_sources/daily-20260422/V3_EVIDENCE_REVIEW.md)，并获[root 单项非作者准入复核](../_sources/daily-20260422/V3_ROOT_19105_FINITE_ADMISSION.md)通过；原证据与 apr01 局部机制审阅仍保留。这一单项结论不是对其余候选的背书，也不替代日级 Gate。

四项反向Books建议的真实必要源/当前owner核验见[V3_APR01_REVERSE_FOUR_BOOKS_AUDIT](../_sources/daily-20260422/V3_APR01_REVERSE_FOUR_BOOKS_AUDIT.md)。19117深入Only通过；19052双索引/坐标迁移、19009构造target评价接口、19141最大信息support三项不能由现有一般原则覆盖冒称终态，保留原候选、评分和普通最窄提案，不重复有效附件。

上述三项随后经 root 对 exact-v1 必要方法、现有 Ch5/Ch24 owner 与 literal 窄范围做非作者写前核验，正文已分别落在 Ch5 filler/role 之后、Ch24 训练 support 与 Few-step target 选择链内。root 再顺读三处实际新增正文、前后交接及限制后通过写后复核；[单篇落实记录](../_sources/daily-20260422/V3_EVIDENCE_REVIEW.md)保留 source family、实际位置与未复现实验边界。三项由普通待办转为实际整合；其写后当时107项工作集合为28整合、9已有覆盖、66仅报告、4窄争议，后续负侧恢复18724使当时集合成为108项。这不等于日期、来源、准入和日级Gate已通过。

apr01首9完整题摘校准见[V3_APR01_FIRST_ADMISSION_AUDIT](../_sources/daily-20260422/V3_APR01_FIRST_ADMISSION_AUDIT.md)；root前三必要源/实际owner见[V3_ROOT_FIRST_THREE_ADOPTION](../_sources/daily-20260422/V3_ROOT_FIRST_THREE_ADOPTION.md)，三消歧见[V3_ROOT_THREE_ADMISSION_DISPOSITIONS](../_sources/daily-20260422/V3_ROOT_THREE_ADMISSION_DISPOSITIONS.md)；apr20四项见[V3_APR20_FIRST_FOUR_ADOPTION](../_sources/daily-20260422/V3_APR20_FIRST_FOUR_ADOPTION.md)。18788/18701/18909及18616/18791/18860六项实际写后rootPASS记于证据笔记对应节。复用范围具名，不宣称独立重抓全部外部目录或实验复现。当前V3报告的结构一致性校验与限定范围 `git diff --check` 已通过；它们不证明来源、日期、准入或 Books 的日级语义 Gate。

apr01另对18982/19147的中心桥及排除侧19048的主表聚合完成必要原文与实际章节有限复核，见[三项审计](../_sources/daily-20260422/V3_APR01_SAVOIR_NEXUS_SAMORA_INDEPENDENT.md)。前两项保持窄争议安全隔离；19048从原前分母关闭恢复为6分深入、仅报告可复算结果。这只校准三项，不替代其余候选或日级Gate。

18913/18951/19031/19305四项处置及19004/19093两项否定侧必要原文与actual owner核见[V3_ROOT_FOUR_DISPOSITIONS](../_sources/daily-20260422/V3_ROOT_FOUR_DISPOSITIONS.md)；同文件末18655/18610/18747实际写后及18811/18835/18756/18857处置通过。18728/19089/19105三项原标准Only的局部机制审读见[V3_APR01_THREE_ONLY_INDEPENDENT](../_sources/daily-20260422/V3_APR01_THREE_ONLY_INDEPENDENT.md)；19105现另按项目长期贡献门槛作前分母关闭，原审读范围没有被删。上述复核只覆盖具名命题、关键反证及具体章节比较，不验收全日日期或全部外部目录。UniEP实际写后root核验及DASH/EVPO的apr20处置见[V3_APR20_UNIEP_DASH_EVPO_INDEPENDENT](../_sources/daily-20260422/V3_APR20_UNIEP_DASH_EVPO_INDEPENDENT.md)。18738 Only与18739/18839实际写后核验见[V3_ROOT_GENERATION_THREE_INDEPENDENT](../_sources/daily-20260422/V3_ROOT_GENERATION_THREE_INDEPENDENT.md)；18892的actual正文/邻接由apr01核见[V3_APR01_18892_WRITE_AFTER](../_sources/daily-20260422/V3_APR01_18892_WRITE_AFTER.md)。以上为截至18907的过程写后记录；现28项实际整合已通过非作者写后复核，仍不预支日级通过。机器结构/差异校验随后运行，不能代替日级语义验收。四项19090/19145/19238/19245必要源/实际owner处置见[V3_APR01_FOUR_19090_19245_INDEPENDENT](../_sources/daily-20260422/V3_APR01_FOUR_19090_19245_INDEPENDENT.md)，已同步真实独立范围，不扩大为整日验收。

新负侧身份18724经[root独立定点审计](../_sources/daily-20260422/V3_ROOT_18724_INDEPENDENT.md)恢复为5分标准仅报告，并确认Ch66现有原则足以承载，不凭UI形式再写Books；date只按官方slot、连续ID及原字段联合推断，DataCite记录晚于本窗截点，不作直接首发证据。另[apr20四项有限审计](../_sources/daily-20260422/V3_APR20_FOUR_18943_19321_INDEPENDENT.md)分别支持18943/19300的窄Existing与19201/19321的受限Only。root再独立核18867/18897/18942/19334的必要原文与限域：前三项保持受限Only，19334仅报告时隔离打印延迟/能耗冲突；18897补进§9官方hard3 AN45c 55.5%低于无cheatsheet 56.3%的反证，不从本地79.25%外推稳健增益。此批只覆盖四篇，不扩大为整日日级日期或来源验收；其完成当时的工作集合为108=28实际整合+9已有覆盖+67仅报告+4窄争议。之后19053受限恢复使当前集合增至109，Books普通待办仍为0，其他候选及排除侧独立终核待完成。

apr20_resume 另对[18874/18901/19405/19459四项窄 Existing](../_sources/daily-20260422/V3_APR20_FOUR_18874_19459_INDEPENDENT.md)独立核 official exact-v1 的决定性方法和反证，并实际对读 Ch66/72 的 opportunity set、refusal/sensor/authority、派生评测身份及 spec validity 命题，四项均通过。复核只确认所采长期命题已有具体承载，不称四篇完整方法或数值都已写入 Books；日期、来源和其余候选尚未因此通过日级 Gate。

同一非作者另对[18946/18970/19001/19108四项安全 Only](../_sources/daily-20260422/V3_APR20_FOUR_18946_19108_INDEPENDENT.md)核必要 exact-v1 机制、关键反证与 Ch29/72 实际相邻责任，四项受限仅报告处置通过。18946 的 w/o PU/w/o CR 局部反向、18970 的事后阈值及 SGLD 批量成本、19001 的先筛 harmful trace 与机器句级标签、19108 的 MUFAC reversal 均限制结论；这些单篇核验未覆盖整日来源、日期及其他候选。

root 对六条新标题边界题摘做有限独立准入核：FlowSG、Patent Lean、HSSPS、POLAR-PIC、Crash-free verifier 各按上文具名范围/贡献理由关闭；CHRONOS 因相位/秘密状态分工准入，但官方 exact-v1 §4.5 的恢复整epoch私钥会让诚实执行且保留旧消息的 server 回算同epoch历史单客户端更新。root 以两轮反例独立复算确认，因此本项 5分、强制深入、窄争议且不写 Books；该审计并未证明生产漏洞或全部安全聚合方案失效。六项纳入170份题摘对账后，当时正式109=28实际整合、9具体已有覆盖、67仅报告、5窄争议，59具名前关闭、2日期隔离；日级日期/来源/其余候选仍需独立 Gate。

root 又对 18880、18978 两项做了必要 exact-v1 与真实 owner 的有限非作者核验：前者的 OpenAlex/web 字段标注、单模型 neuron 干预与不同 citation field 的退步和统计范围，不支持统一可迁移的可靠修复；后者是随机冻结 critic 加低秩更新，在 DMC/IsaacLab 的局部结构正则，非 LLM/VLA policy 证据。两项 5分标准仅报告处置通过，未复现实验，也不构成全部 Only 或整日日级 Gate。

19059、19342 又经 root 非作者定点反向准入核：前者是受限 UAV 五任务的固定权重 latent TTA，当前 Ch26 已承载动力学状态、在线更新、执行权及回退条件；后者是双 T4、三工业任务的局部 PTQ/QLoRA 成本工作点，现有 Ch70 已要求等质量、完整成本与 SLO 同分母比较。二者有局部实验价值，但没有足以改变本书长期模型/Infra设计选择的独立增量，故从仅报告候选转为具名**前分母关闭**；原 exact-v1 审阅留在 `_sources`，不能把它们当零分候选或称论文无价值。当时正式对账为170=107工作家族+61前关闭+2日期隔离，107=28整合+9已有覆盖+65仅报告+5窄争议；这是两项有限独立结论，不代表其余候选或负侧全通过。

随后 root 又对 `18857/19071/19201/19321/19440` 的官方题摘和具体 Books 命题作独立反向准入核，同意这五项具名前分母关闭；此前单篇必要方法、反证、成本及受限价值均保留在[本日证据笔记](../_sources/daily-20260422/V3_EVIDENCE_REVIEW.md)，不将局部新意或章节相关自动算作本项目长期贡献。当前对账为170份已读题摘=102未冻结工作家族+66具名前关闭+2日期隔离；102=28实际整合+9具体已有覆盖+60仅报告+5窄争议。当时另有五项作者拟反向关闭 `18978/19087/19267/19301/19457`，其中18978后经root独立核应保留受限Only，19267/19301/19457经作者回读亦暂保留，19087仍待非作者；来源、日期、其他候选与负侧日级 Gate 仍未通过，故本日报保持进行中。

apr20_resume 又对 `19024/19295/18803/18845` 完成[四项独立必要原文及实际 owner 审阅](../_sources/daily-20260422/V3_APR20_FOUR_19024_18845_INDEPENDENT.md)：仅通过各自窄 Only 处置；尤其 18803 的 PDF-v1 800 主分母/717 后验审核不可合并、Table2 数值与正文冲突需隔离，18845 的指令检索收益伴一般检索退步。随后 apr01 对 `19015/18966/19149/19234` 完成[必要 exact-v1 与实际 owner 对读](../_sources/daily-20260422/V3_APR01_TWO_19015_18966_INDEPENDENT.md)，四项窄 Only 处置通过：FedProxy 无形式 IP/隐私保证，TabGRAA 的 scorer 真实数据访问与组均值目标不等普通 pair DPO，Self-Reading 的 SamePool 未固定内容/正确性，OTCA 的时间代理不提供逐目标 step 因果信用。八项单篇状态均已同步 §3/4，候选总数未变；余下15项表中显式待独立、来源/日期/排除侧和日级 Gate 仍开放。

其后 apr01 针对旧关闭身份 `19274` 独立重开[exact-v1 必要方法与配对评价](../_sources/daily-20260422/V3_APR01_19274_ADMISSION_INDEPENDENT.md)，确认同一有害草稿的任务包装失效值得本项目 5 分安全候选，原泛化关闭理由撤销；正式本轮工作账同步为170题摘=103未冻结候选+65具名前关闭+2日期隔离。独立准入审计未核首次公开或 Books；该单篇仍需普通 Ch72 采用决定及必要写后，其他15项有限独立终态、来源/日期/负侧与整日日级 Gate 均未因此通过。当前 validator 与限定 `git diff --check` 通过，仅证明结构和空白一致。

随后 apr01 对[五项明确待核材料](../_sources/daily-20260422/V3_APR01_PENDING_FIVE_INDEPENDENT.md)重开 official exact-v1 的决定性机制/反证及实际 Books owner：19087 的 oracle latent option≈70%不能充作部署policy同预算收益，现有 Ch20 控制/反馈合同下具名前关闭；19444、19167、19264各维持具体标准Only，19267 的尺寸条件候选排序/无safe候选回退为实际保护评价分支，维持深入Only而不能用一般 Ch26 owner 反关。故当前工作账为170=102未冻结候选+66具名前关闭+2日期隔离，102=28I+9E+59Only+5D+19274一项普通Books待决。余10项显式待单篇独立，来源/日期/负侧及整日Gate仍开放；该批不是全量复核。

上述28I/19274待决是单篇写入前快照。root 随后在 Ch72 Guardrail 段落实同草稿协作编辑配对验收，书稿非写作者 apr02 按[官方 exact-v1](https://arxiv.org/html/2604.19274v1)核实际正文与相邻链路，[写后审计](../_sources/daily-20260422/V3_APR02_19274_WRITE_AFTER.md)通过；未复现实验。当前102项为29真实整合、9具体已有覆盖、59仅报告、5窄争议，普通Books待办0；剩余10项非作者单篇审查、日期/来源/负侧及整日日级 Gate 继续，不能据此标完成。

root 随后按 2604.19292v1 的显式 locale 知识与隐式默认选择测量对象对读 Ch66 并窄写，多语言评估的原翻译保真论证不被覆盖；apr02 据[官方 exact-v1](https://arxiv.org/html/2604.19292v1)和正文相邻交接完成[非书稿作者实际写后复核](../_sources/daily-20260422/V3_APR02_19292_WRITE_AFTER.md)通过。当前102项为30真实整合、9具体已有覆盖、58仅报告、5窄争议，普通Books待办0；余9项单篇独立终核及日级来源/日期/负侧Gate未通过，不因此标完成。

其后 root 又对 `2604.19301v1` 的[官方 exact-v1、实际 Ch82 和前分母贡献](../_sources/daily-20260422/V3_ROOT_19301_REVERSE_ADMISSION.md)作有限非作者复核：无客观 gold 的社会投票条件改变输出是真实局部证据，但没有新增独立信息流、行动提交或长期 controller/评价权责，故从标准 Only 改为具名前关闭，旧必要审阅留在 `_sources`。当前170=101未冻结工作家族+67具名前关闭+2日期隔离，101=30I+9E+57Only+5窄争议；余8项显式单篇独立终核、其他负侧/来源/日期及整日日级 Gate 仍开放，不能据此标完成。

root 又按[官方 exact-v1 §4–6 和 Ch31 实际命题](../_sources/daily-20260422/V3_ROOT_19406_REVERSE_ADMISSION.md)独立复核旧排除项 `2604.19406v1`：承认五人用户研究、外部 GEdit-Bench 与受限编辑收益，撤销“无 holdout”错误理由；主组件消融的代理评估尚不能隔离筛样/scorer/reward 各环节对人类效用的贡献，现有 Ch31 的训练与独立效用分账未被改变。具名贡献前关闭通过，但只是此一个负侧样本，不代表其余66项、来源、日期或整日日级 Gate 已通过。
