# Daily Research — 2026-05-26

**规范：** V3

**窗口：** 2026-05-25T09:00:00+08:00 ～ 2026-05-26T09:00:00+08:00

**窗口说明：** 用户明确只补遗漏，保留原候选完整行、日期评分、原小时窗口及有效连续旧§4，不移动旧材料。新增材料仅按补充自然日处理。

**补充窗口：** 2026-05-25 ～ 2026-05-25

**冻结候选日期：** [补查前原报告](../_sources/daily-20260526/baseline-before-supplement-20261021.md)

**状态：** 完成

**Books：** 纳入本次

**检查时间：** 2026-09-16T10:00:13+08:00

**补查检查时间：** 2026-10-21T11:49:26+08:00（完成态保存；来源请求与分批停止见补查记录）

## 1. 结论

本次只补BJT May25完整自然日的遗漏，新增 **38家族＝37篇arXiv＋1份Anthropic披露**，均完成必要证据审阅（32深入、6标准），Books为 **30实际整合＋8具体已有覆盖**；所有30项正文/完整邻接与本人注均由指定非writer实际POST通过，写入16个唯一owner。新增不是由1081宽记录逐项“全关”得来，旧86候选/日期评分/小时窗及连续旧§4保持原样。

真正改变设计解释的链路包括：跨账户外传不能靠域名allowlist关闭；diffusion relay/cache、typed checkpointables与数据可见事件须明确状态资格；rubric/skill/code-test共演化的反馈不授真值；多视图/时空grounding/双目评价须把实际输入支持、参照与能力claim分开。局部实验与理论边界、训练/执行全费和旧方案退路均近机制保留，不把作者结果写成生产保证。9项跨日日期资格和4类历史来源子层只作终态隔离，不评分、不用于Books/覆盖或“无遗漏”保证。当前普通研究/Books待办0，独立完整六部分DAY已实际通过（R31），本次完成以新审阅和实际POST为依据；完成态有限FINAL回读另见§6。依据：[作者A1–A19](../_sources/daily-20260526/SUP_SOURCES_20261021.md)、[独立复核](../_sources/daily-20260526/SUP_REVIEW_20261021.md)。

保留层与新增层合计 **124候选＝原86＋新38**；Books合计 **67整合＋50已有覆盖＋5结构候选＋2仅报告**。旧结构候选/仅报告为原有效处置，不由此次补查重新改写；旧行历史措辞由其原R3有效终审限定。

以下为原小时窗口的历史完成结果，冻结复用，不代表本次补充自然日的覆盖或验收：

旧 V2.1 `Complete`、1208 raw 与 170 candidates 不再拥有当前状态。当前 first-public owner 仅为 2026-05-26 08:00 BJT 的 263 项 arXiv official announcement batch；MiniMax 技术页官方 JSON-LD `datePublished=2026-05-27T00:00:00Z` 属 05-27，不进入本日正面或 no-hit 投影。全日守恒为 **263 = 86 retained + 177 pre-denominator closure + 0 withdrawn**。

Evidence 为 **86 = 74 deep complete + 12 standard complete + 0 blocked**；评分分布为 `{6: 12, 7: 9, 8: 50, 9: 15}`。Books 对账为 **86 = 37 Applied + 0 Integrate + 42 No Change + 5 Structural Candidate + 2 Report Only**。16 个 05-26 root-action semantic body、paired marker 与独立 `source-family` marker 均已存在且位于 Review notes 前。此前 fresh review 发现并有界修复了 `2605.24423` 的 denominator false negative；另一名未参与修复和 Books 写回的 fresh non-author reviewer 已完成独立终审并通过 Complete Gate。

## 2. 来源覆盖

以下为补充窗口 **2026-05-25** 的本次实际检查，检查于2026-10-21；旧小时窗的263公告批仅作原86候选去重/有效层复用，不作为May25覆盖。原件、查询、分页/停止及纠正见[补查A1–A19](../_sources/daily-20260526/SUP_SOURCES_20261021.md)，不是旧表的无条件重用。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 实际RSS及两份May25 00:00GMT/08:00BJT原文：AI first hire经济使用案例、Folha/UOL商业授权；均读核心后贡献前关闭 | 已检查 | 两者在补窗内，不沿用旧“小时窗外=不查”；不以RSS担保已删除历史 |
| SRC-ANTHROPIC | Research与FRT/Alignment/Interpretability/Economics/Societal/Engineering实际目录；相邻May22→Jun03、May08→Jul08、May07→Jul06、Apr22→Jun16、Apr30→Jun12；Engineering准入Containment | 已检查 | 当前相关目录切片，非全历史完备；Science暂缓不展开 |
| SRC-GOOGLE-AI | Google Research May月档4项May1/19/27/28；DeepMind真实page2/3连续July→June→May→April，官方原页Jun03 Gemma4-12B→May20 Singapore夹住目标 | 受阻 | 两Blog当前切片已检查无May25；Publications只有year筛选，缺日级历史切片，不授该子层阴性覆盖 |
| SRC-META-AI | 实际Research/Publications入口及有限恢复，官方Sorry/unavailable原件 | 受阻 | 目标日历史研究目录不可取得；需官方有日期事件/可重放归档，非零命中 |
| SRC-QWEN | 本日实际GET qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US，success=true/data仅articles，无分页；40行非日期排序，逐extra.date核完，May20 Qwen3.7→May29 QwenVLA夹目标（LiveTranslate May19） | 已检查 | 当前公共目录40行无May25，不授被删除历史完备；新原件见作者A20，旧shell缺段已解除 |
| SRC-DEEPSEEK | 实际Change Log完整日期heading Oct17/Sep10/Aug21/Aug13/Jul31→Apr24后2025；官网入口并核 | 已检查 | 当前官方changelog切片无May25，不误称文档首页失败，也不担保所有未保存Research |
| SRC-MOONSHOT | Kimi Blog实际仅2025，MoonshotAI首30项creation有Apr20/May22→July边界 | 受阻 | creation不等release，目标研究/发布历史slice缺失；需有日期官方事件/归档 |
| SRC-TENCENT-HUNYUAN | 真实Research bundle调用api.hunyuan.tencent.com/api/blog/publicList，pageNum1/pageSize100/renderType0；zh11=total11、en9=total9逐条三日期字段读完 | 已检查 | 当前目录无May25（display邻May21/Jul06）；跨字段日期不冒称first-public，错误host404不计覆盖 |
| SRC-ZAI | 实际官方Research当前目录May20→Jun16跨目标，相关切片读回 | 已检查 | 当前目录切片无May25，非被删除历史完备 |
| SRC-BYTEDANCE-SEED | 真实article_type=1 papers page_token0/20共38可见逐条日期递减，May26→May16；Blog type2 p0 12可见/total24/next20，Jun23→Apr23跨窗 | 已检查 | 停在已跨日的真实排序边界，不把ignored page或错误type0空响应当依据；目录publish非arXiv首次公开 |
| SRC-BAIDU-ERNIE | 官方技术Blog实际当前列表，最新明确日期May09在目标前 | 已检查 | 当前可见切片，未声称所有历史被删事件不存在 |
| SRC-XIAOMI-MIMO | Paper完整8行Jun29→Mar13→Feb03→Jan08→2025；Blog15张undated cards+More，org18项creation只辅助 | 受阻 | Paper当前切片已核无May25；仅Blog历史日期/后页未恢复，不把creation授发布 |
| SRC-MINIMAX | 实际Blog完整日期卡片：Jun01→May27 Mavis→May26 SparseTokenForgetting→Mar18 M2.7→Feb14；目标夹在May26/Mar18 | 已检查 | 当前Blog目录无May25；旧May27 JSON-LD只证明该事件，不代表本窗全覆盖 |
| SRC-ARXIV | Main discovery为arxiv.content注册UTC May24 16:00～May25 15:59:59两页1000+81=1081唯一findable记录，按模型/训练/推理/Agent/多模态系统题义收窄；CL1150/100与LG3100/100相关标题、DC0/250作有界查漏 | 已检查 | 宽列表不逐项关闭；错误API range/500及窗外target/bound探针不计覆盖。37家族用唯一v1+官方公告/发号规则+exactDOI registered联合日门；9跨日资格保留不授正面Evidence或无遗漏 |

实际主题含foundation/language model、Transformer/MoE、训练优化/校准/蒸馏、GPU/通信/kernel/checkpoint/serving、Agent工具/规划/技能/记忆/评价，以及生成/World Model/VLA。标题含糊者读完整精确题摘，准入不以关键词或章节映射决定；本次只每日14源，没有常规扩扫每周组。具名9项与May25旧有效事件精确去重不重列；末3个239xx未定日线索另见§5。代表贡献前关闭覆盖技术综述、Cypher反馈、LaTeX预处理、抽象类比、机器人控制、defense倡议及next-token理论，具体理由和独核范围见[作者A9/A11/A12](../_sources/daily-20260526/SUP_SOURCES_20261021.md)与[reader R19–R29](../_sources/daily-20260526/SUP_REVIEW_20261021.md)。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [2605.24321 Unified 3D Scene Understanding Through Physical World Modeling](https://arxiv.org/html/2605.24321v1) | 2026-05-26T08:00:00+08:00 | 把 World Model 的 task head 改写为对同一 RGB/flow/camera 图的 observation/query traversal；旧的 task-specific heads 仍是低成本、强约束 fallback，随机访问失配会造成局部不一致。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：MULTIMODAL-WORLD-MODELS |
| [2605.24322 Causal Physics Steering in Video World Models via Concept Activation Vectors](https://arxiv.org/html/2605.24322v1) | 2026-05-26T08:00:00+08:00 | 把 World Model 的物理表示从只读 probe 提升为受限的 inference-time control surface：PEZ layer 的 probe weight 作为 CAV 写入 hidden state。它免训练但依赖 representation localization，错误 layer/方向会产生不真实 steering；因此只作为 rollout proposal，以真实观察/模拟器 gate，并在物理一致性失败时回退无 steering 基；3+2+3=8 | 深入完成 | 整合：root 已写入且本轮写后语义复核通过，待不同 fresh reviewer 最终复核 [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：MULTIMODAL-WORLD-MODELS |
| [2605.24326 ScaleAcross Explorer: Exploring Communication Optimization for Scale-Across AI Model Training](https://arxiv.org/html/2605.24326v1) | 2026-05-26T08:00:00+08:00 | 把单机房 collective tuning 扩展为跨楼宇 placement、path、collective schedule 与 failure-domain 的联合搜索；跨域训练用通信优化换更大的 tail latency、模拟误差和故障面，收益失效时回退单站点或固定 hierarchy。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/36-distributed-training.md)：TRAIN-DISTRIBUTED-TRAINING |
| [2605.24330 Interdomain Attention: Beyond Token-Level Key-Value Memory](https://arxiv.org/html/2605.24330v1) | 2026-05-26T08:00:00+08:00 | 在 attention 的 query addressing 与 SSM 固定状态之间增加 query-conditioned basis projection；固定状态降低长度成本但牺牲精确 recall，超出状态预算或 recall gate 失败时回退 softmax/hybrid attention。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-02-model/17-transformer-layer.md)：MODEL-TRANSFORMER-LAYER |
| [2605.24331 CurveRL: Principled Distribution-Aware Context Reweighting for LLM Reasoning](https://arxiv.org/html/2605.24331v1) | 2026-05-26T08:00:00+08:00 | Building on this optimality framework, we propose a distribution-aware prompt reweighting approach, called CurveRL, based on a quantile coordinate transform, in which the weight assigned to each prompt depends not on the absolute value of p；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-04-training-system/33-grpo.md)：TRAIN-GRPO |
| [2605.24350 PACT: Proactive Asking for Continual Task Assistance in Human-Robot Collaboration](https://arxiv.org/html/2605.24350v1) | 2026-05-26T08:00:00+08:00 | Proactive ask-or-act planning combines current observation with cross-day history and evaluates clarification utility as assistance accuracy against clarification frequency, instead of treating every uncertainty as either silent inference o；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/79-planning.md)：AGENT-PLANNING |
| [2605.24366 Structure-Aware RAG: Structured Retrieval Augmented Generation from Noisy Data for Conversational Agents](https://arxiv.org/html/2605.24366v1) | 2026-05-26T08:00:00+08:00 | 把 noisy corpus 的表格从被动文档格式提升为带质量状态的 intermediate retrieval interface：metadata normalization/effectiveness 先受控更新，再以 semantic/structural consistency gate 生成表格。它减少噪声却新增表格化信息损失、metadata drift 和离线构建成本；失败时回退原文 chunk/hybrid retrieval，并保留 row/cell 到；3+2+3=8 | 深入完成 | 整合：root 已写入且本轮写后语义复核通过，待不同 fresh reviewer 最终复核 [章节](../../../../books/part-07-agent/76-rag.md)：AGENT-RAG |
| [2605.24375 Distilling Game Code World Model Generation into Lightweight Large Language Models](https://arxiv.org/html/2605.24375v1) | 2026-05-26T08:00:00+08:00 | Executable game world models can be post-trained with a four-tier verifier spanning static structure, fuzzed dynamics, semantic rule traces and information consistency, so SFT/RLVR optimize more than code syntax.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：MULTIMODAL-WORLD-MODELS |
| [2605.24383 A governance horizon for ethical-use constraints in open-weight AI models](https://arxiv.org/html/2605.24383v1) | 2026-05-26T08:00:00+08:00 | 把 open-weight restriction 从可选 model-card 文本升级为随 lineage/merge 传播的 machine-readable governance state；声明继承降低发布摩擦但会产生 orphan/merge undecidability，无法解析时必须阻断自动合规结论并转人工。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.24384 Side-by-side Comparison Amplifies Dialect Bias in Language Models](https://arxiv.org/html/2605.24384v1) | 2026-05-26T08:00:00+08:00 | Encouragingly, we show that counterfactual fairness finetuning can mitigate covert dialect bias for some stereotypical traits, reducing average disparities when evaluating tweets in isolation, however, these improvements do not consistently；2+2+2=6 | 标准完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.24391 MX-SAFE: Versatile Inference- and Training-Proof Microscaling Format with On-the-Fly Exponent and Mantissa Bit Allocation](https://arxiv.org/html/2605.24391v1) | 2026-05-26T08:00:00+08:00 | In this work, we present a versatile MXFP format, called MX-SAFE (MXSF in short), that adaptively uses two modes, i.e., a wider mantissa mode (FP8 E2M5) and a subnormal FP mode (FP5 E3M2), to support both training and direct-cast inference.；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)：INFER-TENSORRT-LLM |
| [2605.24396 Understanding and Mitigating Premature Confidence for Better LLM Reasoning](https://arxiv.org/html/2605.24396v1) | 2026-05-26T08:00:00+08:00 | We find such a signal in how the model's confidence evolves during reasoning: premature confidence, the tendency to commit to an answer early and use the remaining tokens to rationalize it, strongly predicts flawed reasoning across tasks an；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.24420 Batch Normalization Amplifies Memorization and Privacy Risks](https://arxiv.org/html/2605.24420v1) | 2026-05-26T08:00:00+08:00 | Batch-coupled normalization statistics amplify atypical-sample influence and memorization, and the measured amplification carries through to membership-inference susceptibility; privacy comparisons must therefore hold normalization and batc；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.24421 Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content](https://arxiv.org/html/2605.24421v1) | 2026-05-26T08:00:00+08:00 | We introduce a four-class taxonomy of log-substrate attacks: direct override (S1), persona hijack (S2), context manipulation (S3), and obfuscated payloads (S4).；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.24423 Benchmarking the Limits of In-Context Reinforcement Learning for Ad-Hoc Teamwork](https://arxiv.org/html/2605.24423v1) | 2026-05-26T08:00:00+08:00 | history-conditioned ICRL 与更长 context 不足以证明 partner adaptation；必须独立测量 partner-policy inference 与 adaptation gain。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/82-multi-agent.md)：AGENT-MULTI-AGENT |
| [2605.24425 Momentum Streams for Optimizer-Inspired Transformers](https://arxiv.org/html/2605.24425v1) | 2026-05-26T08:00:00+08:00 | The residual update of a pre-norm Transformer layer admits an interpretation as one step of a first-order optimizer acting on a surrogate token energy, wherein the attention and MLP sublayers function as gradient oracles.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-02-model/17-transformer-layer.md)：MODEL-TRANSFORMER-LAYER |
| [2605.24426 SEAL: Synergistic Co-Evolution of Agents and Learning Environments](https://arxiv.org/html/2605.24426v1) | 2026-05-26T08:00:00+08:00 | We propose SEAL, a closed-loop co-evolution framework for interactive tool-use agents.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/31-rlhf.md)：TRAIN-RLHF |
| [2605.24432 Found in Conversation: LLMs Teach Themselves to Close the Multi-Turn Gap](https://arxiv.org/html/2605.24432v1) | 2026-05-26T08:00:00+08:00 | 把单轮能力到多轮能力的迁移建模为 information-equivalent views 的自蒸馏，并把未充分信息时的 defer/clarify 写入训练目标；视图不等价会蒸馏错误，失败时回退显式澄清策略与外部 teacher。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/29-sft.md)：TRAIN-SFT |
| [2605.24433 Smoother Action Chunking Flow Policy via Prior-Corrected Orthogonal Trust-Region Guidance](https://arxiv.org/html/2605.24433v1) | 2026-05-26T08:00:00+08:00 | We propose POTR, a **p**rior-corrected **o**rthogonal **t**rust-**r**egion guidance method.；2+2+2=6 | 标准完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：MULTIMODAL-EMBODIED-VLA |
| [2605.24461 Provisioning to Runtime Optimization of a 100 MW-Scale AI Cluster](https://arxiv.org/html/2605.24461v1) | 2026-05-26T08:00:00+08:00 | We present detailed power measurements for a 150 MW datacenter hosting a cluster of 83K GB200 GPUs.；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)：PLATFORM-GPU-SCHEDULER |
| [2605.24468 SAM: State-Adaptive Memory for Long-Horizon Reasoning Agent](https://arxiv.org/html/2605.24468v1) | 2026-05-26T08:00:00+08:00 | To this end, we propose State-Adaptive Memory~(SAM), a standalone framework that consolidates ongoing interaction into compact memory cues while preserving raw trajectory pages for intent-driven recall.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/77-memory.md)：AGENT-MEMORY |
| [2605.24486 AgentFugue: Agent Scaling for Long-Horizon Tasks through Collective Reasoning](https://arxiv.org/html/2605.24486v1) | 2026-05-26T08:00:00+08:00 | Recent progress on long-horizon agentic tasks has been driven largely by scaling up individual agents through stronger models, better tools, and more effective scaffolding.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/82-multi-agent.md)：AGENT-MULTI-AGENT |
| [2605.24497 Reasoning as an Attack Surface: Adaptive Evolutionary CoT Jailbreaks for LLMs](https://arxiv.org/html/2605.24497v1) | 2026-05-26T08:00:00+08:00 | To overcome these limitations, we propose an adaptive evolutionary CoT jailbreak framework, called AE-CoT.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.24509 Φ-Noise: Training-Free Temporal Video Conditioning via Phase-Based Noise Manipulation](https://arxiv.org/html/2605.24509v1) | 2026-05-26T08:00:00+08:00 | Low-frequency phase from a reference video can condition diffusion noise without model retraining, while energy balancing limits the amplitude distortion introduced by spectral substitution.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)：MULTIMODAL-GENERATIVE-PARADIGMS |
| [2605.24517 ECHO: Terminal Agents Learn World Models for Free](https://arxiv.org/html/2605.24517v1) | 2026-05-26T08:00:00+08:00 | 把 agent rollout 中环境 observation tokens 从只读 context 升级为辅助预测目标，与 action policy gradient 分责；dense signal 可能奖励可预测而非可控环境，故要以 task verifier/held-out dynamics gate，并可回退标准 GRPO。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/31-rlhf.md)：TRAIN-RLHF |
| [2605.24518 Grammatically-Guided Sparse Attention for Efficient and Interpretable Transformers](https://arxiv.org/pdf/2605.24518v1) | 2026-05-26T08:00:00+08:00 | Part-of-speech-derived hard or soft masks reduce the theoretical self-attention graph, but the disclosed CPU mask generation, tiny model and length-128 experiment do not establish production speedup or long-context quality.；2+2+2=6 | 标准完成 | 已有覆盖 [章节](../../../../books/part-02-model/14-self-attention.md)：MODEL-SELF-ATTENTION |
| [2605.24535 Steering Beyond the Support: Adversarial Training on Unsupervised Jailbroken Activation Simulation](https://arxiv.org/html/2605.24535v1) | 2026-05-26T08:00:00+08:00 | We propose a bi-level adversarial training framework for zero-shot jailbreak defense.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.24538 Is Decentralized AI Governable? From Regulative Policy to Constitutive Protocol](https://arxiv.org/html/2605.24538v1) | 2026-05-26T08:00:00+08:00 | When model, training, compute, harness, identity and ownership are decentralized together, governance can lose both an addressable principal and an actor capable of changing the running system, motivating protocol-level constitutive constra；3+2+3=8 | 深入完成 | 结构候选：无唯一 owner |
| [2605.24539 DemoEvolve: Overcoming Sparse Feedback in Agentic Harness Evolution with Demonstrations](https://arxiv.org/html/2605.24539v1) | 2026-05-26T08:00:00+08:00 | 把 harness evolution 的 reward-only search 改成 demonstration-guided program edit localization；demonstration 提高可诊断性但引入示范偏差和额外审计成本，固定种子 paired gate 失败时回退人工 harness 与不变基线。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/84-agent-platform.md)：AGENT-PLATFORM |
| [2605.24541 SemanticZip: A Pilot Framework for Lossy Text Compression with LLMs as Semantic Decompressors](https://arxiv.org/html/2605.24541v1) | 2026-05-26T08:00:00+08:00 | Rather, we introduce a reproducible experimental interface for studying lossy, LLM-decompressible text codes and a design principle: safety-critical and exact commitments should remain protected, while predictable low-risk context may be se；2+2+2=6 | 标准完成 | 结构候选：无唯一 owner |
| [2605.24545 Rethinking Federated Unlearning via the Lens of Memorization](https://arxiv.org/html/2605.24545v1) | 2026-05-26T08:00:00+08:00 | 把 federated unlearning 的删除目标从参数距离或整类性能改为待删数据的 unique memorization，并保留与 remaining clients 重叠的知识。Grouped Memorization Evaluation 与 prune/reinitialize/fine-tune 提供近似路径，但定位错误会删错共享知识；高风险删除仍以 retraining/attack audit 为 gate，失败时回退完整重训。；3+2+3=8 | 深入完成 | 整合：root 已写入且本轮写后语义复核通过，待不同 fresh reviewer 最终复核 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.24547 RL with Learnable Textual Feedback: A Bilevel Approach](https://arxiv.org/html/2605.24547v1) | 2026-05-26T08:00:00+08:00 | Textual feedback is a learnable policy component coupled bilevel to the actor, rather than a fixed correct annotation; Bi-NAC trains the critic for downstream reward improvement and the actor to exploit that feedback.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/31-rlhf.md)：TRAIN-RLHF |
| [2605.24549 PALoRA: Projection-Adaptive LoRA for Preserving Reasoning in Large Language Models](https://arxiv.org/html/2605.24549v1) | 2026-05-26T08:00:00+08:00 | 在 LoRA 更新前用冻结 SVF probe 标记 skill-critical singular subspace，再约束知识注入的投影；probe 失配会保护错误子空间且增加两阶段成本，回退普通 LoRA、全量回归测试或停止注入。；3+2+3=8 | 深入完成 | 整合：root 已写入且本轮写后语义复核通过，待不同 fresh reviewer 最终复核 [章节](../../../../books/part-04-training-system/30-lora.md)：TRAIN-LORA |
| [2605.24550 Jailbreak to Protect: Buffering and Reinforcing via Temporary Jailbreaking for Safe Fine-Tuning in Large Language Models](https://arxiv.org/html/2605.24550v1) | 2026-05-26T08:00:00+08:00 | Based on this insight, we propose a Buffer-and-Reinforce fine-tuning framework that buffers harmful updates during user fine-tuning and reinforces safety after adaptation.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.24552 Ellipsoid Control: A White-list Jailbreak Defense via Benign Latent Modeling](https://arxiv.org/html/2605.24552v1) | 2026-05-26T08:00:00+08:00 | To answer this, we propose Ellipsoid Control, a test-time defense.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.24556 The Multilingual Curse at the Retrieval Layer: Evidence from Amharic](https://arxiv.org/html/2605.24556v1) | 2026-05-26T08:00:00+08:00 | We argue that this assumption breaks down for underrepresented, morphologically rich languages, and use Amharic as a diagnostic case.；2+2+2=6 | 标准完成 | 已有覆盖 [章节](../../../../books/part-07-agent/76-rag.md)：AGENT-RAG |
| [2605.24570 PILOT: Policy-Informed Learned Optimization for Adaptive Deep Network Training](https://arxiv.org/html/2605.24570v1) | 2026-05-26T08:00:00+08:00 | Gradient-direction agreement controls an online learned optimizer policy that changes its mixture of momentum, normalization and sign-based updates across locally stable or noisy regimes, but evidence is limited to small vision datasets/mod；2+2+2=6 | 标准完成 | 结构候选：无唯一 owner |
| [2605.24577 Polymorphism Is Rotation: Operational Mechanistic Interpretability from a Two-Layer Transformer to Pythia-70m](https://arxiv.org/html/2605.24577v1) | 2026-05-26T08:00:00+08:00 | Independently trained transformers compute the same function in residual-stream bases that differ by a uniform random rotation on $\mathrm{SO}(d_{\mathrm{model}})$.；3+2+2=7 | 深入完成 | 仅报告 [章节](../../../../books/part-02-model/14-self-attention.md)：MODEL-SELF-ATTENTION |
| [2605.24578 World Models as Group Actions](https://arxiv.org/html/2605.24578v1) | 2026-05-26T08:00:00+08:00 | World Model 除视觉质量外还要通过 identity/inverse/composition action probes；latent surrogate 降低成本但不等于真实 state dynamics，pose recovery 或 group assumption 失效时回退真实 rollout/状态测量。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：MULTIMODAL-WORLD-MODELS |
| [2605.24579 WhenLoss: Diagnosing Write and Retrieval Bottlenecks in Long-Context Memory Systems](https://arxiv.org/html/2605.24579v1) | 2026-05-26T08:00:00+08:00 | We introduce a four-condition diagnostic protocol that evaluates a fixed reader under truncated full context (TFC), oracle evidence (OE), complete stored memory (CSM), and retrieved memory (RM).；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/77-memory.md)：AGENT-MEMORY |
| [2605.24583 Measuring Alignment-Induced Activation Shifts Correctly: A Template-Controlled Difference-in-Differences Protocol](https://arxiv.org/html/2605.24583v1) | 2026-05-26T08:00:00+08:00 | A template-controlled four-way difference-in-differences protocol separates chat-format shift from alignment-induced activation shift, and causal projection ablation—not singular-value order—tests whether the recovered subspace is behaviora；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.24597 Learning to Reason Efficiently with A* Post-Training](https://arxiv.org/html/2605.24597v1) | 2026-05-26T08:00:00+08:00 | We frame natural language inference as a search problem where the final answer is the valid proof itself, requiring a reasoning procedure in which intermediate inferences are correct.；3+2+2=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-04-training-system/31-rlhf.md)：TRAIN-RLHF |
| [2605.24598 Hera: Learning Long-Horizon Coordination for Device-Cloud Collaborative LLM Agents](https://arxiv.org/html/2605.24598v1) | 2026-05-26T08:00:00+08:00 | To address this issue, we present Hera, a step-level device--cloud LLM agent coordinator for long-horizon tasks achieving a strong performance--cost Pareto frontier.；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/82-multi-agent.md)：AGENT-MULTI-AGENT |
| [2605.24602 Correcting Visual Blur Induced by Attention Distraction to Reduce Hallucinations: Algorithm and Theory](https://arxiv.org/html/2605.24602v1) | 2026-05-26T08:00:00+08:00 | In this work, we reveal that hallucinations are strongly associated with a human-like attention distraction phenomenon, where humans under divided focus experience degraded visual clarity and produce inaccurate descriptions, while in models；3+2+2=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)：MULTIMODAL-REPRESENTATION |
| [2605.24613 Guarded Repair for Harm-Aware Post-hoc Replacement of LLM Mathematical Reasoning](https://arxiv.org/html/2605.24613v1) | 2026-05-26T08:00:00+08:00 | We present GuardedRepair, a guarded best-of-N repair framework that diagnoses cached reasoning traces, selectively triggers repair, and accepts answer-changing candidates only when deterministic verification guards support replacement.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.24614 Measuring the Depth of LLM Unlearning via Activation Patching](https://arxiv.org/html/2605.24614v1) | 2026-05-26T08:00:00+08:00 | To address these limitations, we propose the Unlearning Depth Score (UDS), a metric that quantifies the mechanistic depth of unlearning via activation patching.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.24618 FC-TTS: Style and Timbre Control in Zero-Shot Text-to-Speech with Disentangled Speech Representations](https://arxiv.org/html/2605.24618v1) | 2026-05-26T08:00:00+08:00 | In this paper, we present FC-TTS, a zero-shot TTS framework that enables disentangled control of style and timbre by conditioning on two distinct reference utterances.；2+2+2=6 | 标准完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)：MULTIMODAL-REPRESENTATION |
| [2605.24619 Synthesizing Inductive Invariants for Distributed Protocols via IC3 and Large Language Models](https://arxiv.org/html/2605.24619v1) | 2026-05-26T08:00:00+08:00 | We present IC3Syn, a neuro-symbolic framework that synthesizes inductive invariants by executing an IC3-style process over TLA+ states with the assistance of Large Language Models (LLMs).；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/78-tool-calling.md)：AGENT-TOOL-CALLING |
| [2605.24624 Vision-Language Binding in In-Context Image Generation](https://arxiv.org/html/2605.24624v1) | 2026-05-26T08:00:00+08:00 | We show that an implicit cross-modal binding emerges between the text tokens and the reference image: the text tokens absorb visual reference content during the forward pass, and that absorbed content causally influences the generated outpu；3+2+2=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)：MULTIMODAL-GENERATIVE-PARADIGMS |
| [2605.24630 DexSIM: Real-time Dexterous Simulation with Unified Causal Video Diffusion](https://arxiv.org/html/2605.24630v1) | 2026-05-26T08:00:00+08:00 | We propose DexSIM, a dexterous simulation framework for simulating dexterous manipulation in real-time.；3+2+2=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：MULTIMODAL-WORLD-MODELS |
| [2605.24642 Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models](https://arxiv.org/html/2605.24642v1) | 2026-05-26T08:00:00+08:00 | Recent work explores new opportunities at the intersection of vision-language-action models (VLAs) and geometric foundation models (GFMs) for 3D reconstruction, such as VGGT.；3+2+2=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：MULTIMODAL-EMBODIED-VLA |
| [2605.24647 Know You Before You Speak: User-State Modeling for LLM Personalization in Multi-Turn Conversation](https://arxiv.org/html/2605.24647v1) | 2026-05-26T08:00:00+08:00 | PUMA maintains a belief over latent user state, updates an action-conditioned user world model, and selects dialogue actions by expected free energy rather than using profile/history retrieval as the whole personalization policy.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/79-planning.md)：AGENT-PLANNING |
| [2605.24652 AVBench: Human-Aligned and Automated Evaluation Benchmark for Audio-Video Generative Models](https://arxiv.org/html/2605.24652v1) | 2026-05-26T08:00:00+08:00 | To address these issues, we introduce AVBench, a fully automated benchmark tailored for human-centric AV generation.；2+2+2=6 | 标准完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.24657 Beyond Inference-Only Deployment: Comparing Weight-Based Consolidation Against Cascading Compaction](https://arxiv.org/html/2605.24657v1) | 2026-05-26T08:00:00+08:00 | Major LLM platforms deploy models in an inference-only configuration: the model serves requests but never updates per-user weights.；2+2+2=6 | 标准完成 | 仅报告 [章节](../../../../books/part-07-agent/77-memory.md)：AGENT-MEMORY |
| [2605.24659 IterInject: Indirect Prompt Injection Against LLM Agents via Feedback-Guided Iterative Optimization](https://arxiv.org/html/2605.24659v1) | 2026-05-26T08:00:00+08:00 | We introduce \oursys, a feedback-guided iterative framework that closes the loop between injection, diagnosis, and refinement: a rule-based diagnoser produces structured outcome labels with behavioral descriptions, and an LLM-based optimize；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.24660 How Many Tools Should an LLM Agent See? A Chance-Corrected Answer](https://arxiv.org/html/2605.24660v1) | 2026-05-26T08:00:00+08:00 | Bits-over-Random chance-corrects tool-shortlist coverage at each depth, making tool count an evaluated control and enabling per-query depth policies without an arbitrary depth penalty.；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/78-tool-calling.md)：AGENT-TOOL-CALLING |
| [2605.24661 Measuring Reasoning Quality in LLMs: A Multi-Dimensional Behavioral Framework](https://arxiv.org/html/2605.24661v1) | 2026-05-26T08:00:00+08:00 | Reasoning evaluation separates correctness, consistency, robustness, local logical coherence, efficiency and stability, and deployment-aware aggregation can invert rankings hidden by final-answer accuracy.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.24662 OpenTwin: Closed-Loop Digital Twins for Trustworthy Policy Deployment in Open RAN](https://arxiv.org/html/2605.24662v1) | 2026-05-26T08:00:00+08:00 | A deployment-calibrated digital twin re-synchronizes from streamed measurements and admits a proposed control action only when a conformal fidelity gate places its predicted outcome inside an operator-defined safe region.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.24667 When Mean CE Fails: Median CE Can Better Track Language Model Quality](https://arxiv.org/html/2605.24667v1) | 2026-05-26T08:00:00+08:00 | First, in Qwen2.5-1.5B SFT on synthetic fact-learning, we find that mean CE rises substantially after the initial learning phase while held-out fact-recall accuracy remains near its peak.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/28-pretraining.md)：TRAIN-PRETRAINING |
| [2605.24674 Reasoning to Align: Implicit Reasoning in Diffusion Transformers for Video Editing](https://arxiv.org/html/2605.24674v1) | 2026-05-26T08:00:00+08:00 | Granularity-routed conditioning separates shallow edit-intent tokens from deeper native visual/text evidence, while a training-only reference branch aligns attention without adding the same branch at inference.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)：MULTIMODAL-GENERATIVE-PARADIGMS |
| [2605.24683 B.O.D.Y.: Beyond-Overlay Deterministic topologY -- A Layer-2 Declarative Ground Truth for AIOps Pipelines under Fragmented Administrative Boundaries](https://arxiv.org/html/2605.24683v1) | 2026-05-26T08:00:00+08:00 | A deterministic Layer-2 topology and asset-identity substrate gives probabilistic AIOps reasoning an auditable physical ground truth when administrative boundaries make ordinary discovery incomplete.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md)：PLATFORM-MONITORING |
| [2605.24687 HoloFair: Unified T2I Fairness Evaluation and Fair-GRPO Debiasing](https://arxiv.org/html/2605.24687v1) | 2026-05-26T08:00:00+08:00 | Multi-attribute group fairness is measured jointly and optimized with a multi-objective Fair-GRPO reward, whose disclosed reward-hacking behavior remains part of the evidence boundary.；2+2+2=6 | 标准完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.24693 CP-Agent: A Calibrated Risk-Controlled Agent for Feedback-Driven Competitive Programming](https://arxiv.org/html/2605.24693v1) | 2026-05-26T08:00:00+08:00 | Large language models still struggle with contest-level programming, while many agentic remedies rely on massive inference-time sampling or expensive multi-stage post-training.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/79-planning.md)：AGENT-PLANNING |
| [2605.24696 CALIBURN: Operationally Calibrated Streaming Intrusion Detection with Regime-Dependent Conformal Risk Control](https://arxiv.org/html/2605.24696v1) | 2026-05-26T08:00:00+08:00 | 把 streaming alert threshold 从离线调参改成由 operator cost、alert budget 与 SLO 共同派生的 versioned control，并把 calibration、CRC 与 multi-window burn-rate 串成一条验收链。收益受 prevalence/exchangeability 强约束；CRC overshoot、density degeneracy 或 base-rate inversion 触发时回；3+3+3=9 | 深入完成 | 整合：root 已写入且本轮写后语义复核通过，待不同 fresh reviewer 最终复核 [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md)：PLATFORM-MONITORING |
| [2605.24697 The Path Matters: Learning a Token-Commitment Policy for Diffusion Language Models](https://arxiv.org/html/2605.24697v1) | 2026-05-26T08:00:00+08:00 | We argue that token commitment can instead be learned as a reusable trace-state policy.；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)：MULTIMODAL-GENERATIVE-PARADIGMS |
| [2605.24702 Do Image-Text Metrics Respect Semantic Invariances?](https://arxiv.org/html/2605.24702v1) | 2026-05-26T08:00:00+08:00 | We present an invariance probe on five popular evaluators (CLIPScore, PAC-S, UMIC, FLEUR, and a deterministic LLM judge) under semantics-preserving perturbations along three axes -- spatial (flips, context-preserving repositioning, light ro；3+2+2=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.24709 Streaming Reinforcement Learning under Partial Observability with Real-Time Recurrent Learning](https://arxiv.org/html/2605.24709v1) | 2026-05-26T08:00:00+08:00 | Streaming reinforcement learning has emerged as an online learning paradigm that conforms to the restrictions of natural learning agents that process data incrementally, i.e. with a batch size of 1 and no replay buffer.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/31-rlhf.md)：TRAIN-RLHF |
| [2605.24718 The Tokenizer Tax Across 25 European Languages: Domain Invariance, Cross-Lingual Few-Shot Effects, and the Ukrainian Penalty](https://arxiv.org/html/2605.24718v1) | 2026-05-26T08:00:00+08:00 | 把 tokenizer fertility 作为 language×domain 的成本与可达性 contract，而不是只看平均 tokens；扩 vocab/continued pretraining 会增加兼容、checkpoint 与序列成本，失败时保留旧 tokenizer 并按语言路由或预算。；3+2+3=8 | 深入完成 | 整合：root 已写入且本轮写后语义复核通过，待不同 fresh reviewer 最终复核 [章节](../../../../books/part-02-model/11-tokenizer.md)：MODEL-TOKENIZER |
| [2605.24727 Fundamental Limitation in Explaining AI](https://arxiv.org/html/2605.24727v1) | 2026-05-26T08:00:00+08:00 | Environment complexity, model performance, explanation interpretability and complete faithfulness cannot all hold simultaneously; governance must treat an explanation as an incomplete sensor rather than a complete behavioral account.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.24728 Hylos: Operability Contracts for Model-Native Spatial Intelligence](https://arxiv.org/html/2605.24728v1) | 2026-05-26T08:00:00+08:00 | Foundation models can increasingly describe, reconstruct, and generate 3D objects, assemblies, scenes, and environments, but visually plausible spatial output is not yet operable 3D.；3+2+2=7 | 深入完成 | 结构候选：无唯一 owner |
| [2605.24733 StepGap: A Hybrid NLI-LLM Checker for Step-Level Evidence-Gap Detectionin Multi-Hop Question Answering](https://arxiv.org/html/2605.24733v1) | 2026-05-26T08:00:00+08:00 | We present \textbf{StepGap}, a hybrid NLI-LLM decision tree that detects step-level evidence gaps in multi-hop QA and emits one of three typed labels: \textsc{Contradicted Claim} (CC), \textsc{Irrelevant Evidence} (IE), or \textsc{Missing B；3+2+2=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.24737 Who judges the judges? Governance from metrics: a runtime framework for continuous LLM compliance monitoring](https://arxiv.org/html/2605.24737v1) | 2026-05-26T08:00:00+08:00 | 把 compliance 从一次性 audit 改成 versioned runtime signal，并将 judge disagreement 作为人工仲裁触发而非 truth；judge bias/drift 会污染路由，故保留静态审核、规则检查与人工 override。；3+2+3=8 | 深入完成 | 整合：root 已写入且本轮写后语义复核通过，待不同 fresh reviewer 最终复核 [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md)：PLATFORM-MONITORING |
| [2605.24743 Bilevel Optimization of Synthetic Trajectories for Multi-Turn LLM Fine-Tuning](https://arxiv.org/html/2605.24743v1) | 2026-05-26T08:00:00+08:00 | We propose BOOST, a bilevel optimization framework where the inner level trains the LLM on reweighted data and the outer level trains a lightweight reweighting head on held-out real validation tasks, assigning continuous trajectory-level we；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/27-data.md)：TRAIN-DATA |
| [2605.24749 How Neural Reward Models Learn Features for Policy Optimization: A Single-Index Analysis](https://arxiv.org/html/2605.24749v1) | 2026-05-26T08:00:00+08:00 | Reward modeling is not only a prediction problem: in KL-regularized policy optimization, the learned reward is exponentiated to define the deployed policy, so downstream value depends on errors in reward-tilted regions.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/31-rlhf.md)：TRAIN-RLHF |
| [2605.24754 Motion-Compensated Weight Compression](https://arxiv.org/html/2605.24754v1) | 2026-05-26T08:00:00+08:00 | We propose Motion-Compensated Weight Compression (MCWC), a weight-only codec that aligns permutation-symmetric blocks (e.g., hidden units and attention heads) to maximize cross-layer correspondence, turning depth into a predictable sequence；2+2+2=6 | 标准完成 | 已有覆盖 [章节](../../../../books/part-05-inference-system/54-gpu-memory.md)：INFER-GPU-MEMORY |
| [2605.24756 Proper Scoring Rules for Agentic Uncertainty Quantification](https://arxiv.org/html/2605.24756v1) | 2026-05-26T08:00:00+08:00 | Building on prequential proper scoring, we introduce the Trajectory Proper Score (TPS), a predictor-agnostic family of strictly proper trajectory-level scoring rules for any per-step uncertainty signal calibrated into a probability of event；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.24759 A Contractive Feedback Semantics for Reinforcement Learning](https://arxiv.org/html/2605.24759v1) | 2026-05-26T08:00:00+08:00 | Discounted policy evaluation can be expressed as guarded contractive feedback over typed open decision components, allowing local approximation and safety/resource contracts to lift through admitted wiring contexts rather than assuming ever；3+2+3=8 | 深入完成 | 结构候选：无唯一 owner |
| [2605.24761 Drift-Resistant Navigation World Model with Anchored Epipolar Guidance](https://arxiv.org/html/2605.24761v1) | 2026-05-26T08:00:00+08:00 | We propose Drift-Resistant Navigation World Model, a generative model that mitigates both perceptual drift and geometric drift in conventional rollout-based navigation world models.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：MULTIMODAL-WORLD-MODELS |
| [2605.24764 Spectral Retrieval: Multi-Scale Sinc Convolution over Token Embeddings for Localized Retrieval in LLM Multi-Agent Systems](https://arxiv.org/html/2605.24764v1) | 2026-05-26T08:00:00+08:00 | Multi-scale sinc convolution over token embeddings interpolates between per-token MaxSim and mean pooling for localized retrieval, but its disclosed evidence is synthetic plus LIMIT-small and leaves production latency/calibration open.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/76-rag.md)：AGENT-RAG |
| [2605.24770 Muon in Vision Transformers: Optimizer-Recipe Interactions and Gradient Spectra](https://arxiv.org/html/2605.24770v1) | 2026-05-26T08:00:00+08:00 | Muon is a recently developed matrix-aware optimizer that has shown strong results in transformer training, but its behavior in vision transformers (ViTs) is not yet well understood.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/28-pretraining.md)：TRAIN-PRETRAINING |
| [2605.24775 PRIMA: Operational Patterns for Resilient Multi-Agent Research with Verifiable Identity and Convergent Feedback](https://arxiv.org/html/2605.24775v1) | 2026-05-26T08:00:00+08:00 | Long-running multi-agent work needs a typed pause/resume record, structural operating rules and an explicit cross-document harmonization phase so rate limits or process restarts do not force converged work to be replayed.；3+3+3=9 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/84-agent-platform.md)：AGENT-PLATFORM |
| [2605.24779 Complement Submodular Information Measures for Balanced and Robust Data Selection](https://arxiv.org/html/2605.24779v1) | 2026-05-26T08:00:00+08:00 | Complement Submodular Information scores shared structure between a selected subset and its complement, making rare-slice preservation and outlier suppression explicit in data/benchmark split selection.；2+2+2=6 | 标准完成 | 已有覆盖 [章节](../../../../books/part-04-training-system/27-data.md)：TRAIN-DATA |
| [2605.24785 PANDO: Efficient Multimodal AI Agents via Online Skill Distillation](https://arxiv.org/html/2605.24785v1) | 2026-05-26T08:00:00+08:00 | 把 agent skill library 当作在线可升降级的 versioned state，并同时记 success、steps、tokens 与 cache reuse；错误 skill 会复用放大且在线评估可能污染，失败时 demote/blacklist 并回退无技能单次执行。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/84-agent-platform.md)：AGENT-PLATFORM |
| [2605.24786 CONF-KV: Confidence-Aware KV Cache Eviction with Mixed-Precision Storage for Long-Horizon LLM](https://arxiv.org/html/2605.24786v1) | 2026-05-26T08:00:00+08:00 | We introduce CONF-KV, a KV-cache manager that converts the next-token distribution into a scalar confidence score and uses it to choose the per-step cache budget, retaining more context when the model is uncertain and pruning aggressively w；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)：INFER-KV-CACHE |
| [2605.24793 Beyond the Target: From Imitation to Collaboration in Speculative Decoding](https://arxiv.org/html/2605.24793v1) | 2026-05-26T08:00:00+08:00 | Inspired by this, we introduce \textbf{Collaborative Speculative Decoding (CoSpec)}, a generalization of SPD that no longer treats the target model as the sole token-level authority.；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-05-inference-system/48-speculative-decoding.md)：INFER-SPECULATIVE-DECODING |
| [2605.24794 DUEL: Adversarial Self-Play for Multimodal Reasoning](https://arxiv.org/html/2605.24794v1) | 2026-05-26T08:00:00+08:00 | We propose a self-evolving post-training framework, DUEL, where supervision emerges from adversarial interactions between two policies initialized from the same pretrained VLM.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-04-training-system/31-rlhf.md)：TRAIN-RLHF |
| [Anthropic How we contain Claude across products](https://www.anthropic.com/research/how-we-contain-claude) | 2026-05-25 | domain allowlist仍可跨账户外传→VM内session-token provenance代理→网络允许与凭据权限分责；3+2+3=8 | 深入完成 | 整合：[章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY；执行环境与可验证的安全边界开篇两段 |
| [2605.22949 MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination](https://arxiv.org/pdf/2605.22949v1) | 2026-05-25 | 固定离线校准遇到responder漂移→每agent/per-band EWMA与shrinkage→在线校准须计反馈选择偏差；2+2+2=6 | 标准完成 | 已有覆盖：[章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)：INFER-SCHEDULING；Calibration是在线Routing State |
| [2605.23057 ModeSwitch-LLM: A Lightweight Phase-Aware Controller for Cross-Mode LLM Inference on a Single GPU](https://arxiv.org/html/2605.23057v1) | 2026-05-25 | 静态mode配置→request-boundary轻量选择固定mode→重考router与装载成本；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)：INFER-SCHEDULING；SLO-aware Admission前两段 |
| [2605.23348 XWind: A Cross-site Router for Large Language Model Inference Serving at Renewable Energy Farms](https://arxiv.org/html/2605.23348v1) | 2026-05-25 | 可变电力站点→local profile加跨site reactive routing→容量不只GPU数；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)：PLATFORM-GPU-SCHEDULER；Power Budget段01837后两段 |
| [2605.22967 Learned Relay Representations for Forward-Thinking Discrete Diffusion Models](https://arxiv.org/html/2605.22967v1) | 2026-05-25 | 离散diffusion跨轮丢state→masked relay与truncated BPTT→cache资格和训练费分责；2+2+3=7 | 深入完成 | 整合：[章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)：MULTIMODAL-GENERATIVE-PARADIGMS；masked schedule段后两段 |
| [2605.23080 The Attribution Contract: Feature Attribution for Generative Language Models](https://arxiv.org/html/2605.23080v1) | 2026-05-25 | 生成归因混淆被解释对象→固定prefix/输出span/feature path合同→解释接口版本化；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM；Attribution Contract中semantic-delta:20260526-supp-attribution-contract |
| [2605.23146 Infra-Bayesian Reinforcement Learning Agents Outperform Classical RL For Worst-Case Robustness](https://arxiv.org/html/2605.23146v1) | 2026-05-25 | point prior平均风险→有限imprecise hypotheses的maximin→声明鲁棒目标与支持；2+1+2=5 | 深入完成 | 整合：[章节](../../../../books/part-07-agent/79-planning.md)：AGENT-PLANNING；prior段后一段 |
| [2605.23268 Coupled Training with Privileged Information and Unlabeled Data](https://arxiv.org/html/2605.23268v1) | 2026-05-25 | privileged teacher错误传递→paired unlabeled下joint calibration→重考独立蒸馏；2+1+2=5 | 深入完成 | 整合：[章节](../../../../books/part-04-training-system/29-sft.md)：TRAIN-SFT；多Teacher Debate标题前两段 |
| [2605.23590 Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents](https://arxiv.org/html/2605.23590v1) | 2026-05-25 | 事后rubric→外置step-level learned rubric与preaction单retry→判断与权限分责；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-07-agent/80-reflection.md)：AGENT-REFLECTION；AEWM后、普通多约束任务前两段 |
| [2605.23128 $\pi_0$-EqM: Equilibrium Matching for Closed-Loop Vision-Language-Action Control](https://arxiv.org/html/2605.23128v1) | 2026-05-25 | 固定flow步数→stationarity residual加iteration cap→停止不等动作可执行；3+2+2=7 | 深入完成 | 已有覆盖：[章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：MULTIMODAL-EMBODIED-VLA；EqM现有fixed-point/residual两段 |
| [2605.23243 Are Frontier LLMs Ready for Cybersecurity? Evidence for Vertical Foundation Models from Dual-Mode Vulnerability Benchmarks](https://arxiv.org/html/2605.23243v1) | 2026-05-25 | 安全benchmark单分母→whitebox函数FPR与blackbox finding precision分开→能力声明条件化；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM；Compound Artifact标题前一段 |
| [2605.23071 The Efficiency Frontier: A Unified Framework for Cost-Performance Optimization in LLM Context Management](https://arxiv.org/html/2605.23071v1) | 2026-05-25 | 一次性token比较→N次复用的摊销成本→压缩/检索选择须算upfront；2+2+2=6 | 标准完成 | 已有覆盖：[章节](../../../../books/part-07-agent/75-context.md)：AGENT-CONTEXT；预建索引upfront与完整压缩break-even段 |
| [2605.23764 HyperParallel-MoE: Multi-Core Interleaved Scheduling for Fast MoE Training on Ascend NPUs](https://arxiv.org/html/2605.23764v1) | 2026-05-25 | MoE核间阶段串行→remote data-ready event与合法tile split→调度合法性优先；2+3+3=8 | 深入完成 | 整合：[章节](../../../../books/part-04-training-system/36-distributed-training.md)：TRAIN-DISTRIBUTED-TRAINING；FlashOverlap后两段 |
| [2605.23500 B-GRTO: Bootstrapped Group Relative Tool Optimization for Referring Segmentation](https://arxiv.org/html/2605.23500v1) | 2026-05-25 | 冻结模型工具失配→policy surrogate与tool可微surrogate双更新→梯度责任分开；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-04-training-system/33-grpo.md)：TRAIN-GRPO；Sequence Reward标题前两段 |
| [2605.23657 OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents](https://arxiv.org/html/2605.23657v1) | 2026-05-25 | skill读取被当收益→实际调用/步序/artifact outcome分测→区分遵循与有效性；2+2+2=6 | 标准完成 | 已有覆盖：[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM；control-path/no-skill/Trigger-Compliance-Boundary链 |
| [2605.23345 SCOPE: Simulating Cross-game Operations in Playable Environments for FPS World Models](https://arxiv.org/html/2605.23345v1) | 2026-05-25 | 全帧统一action条件→local discrete/global continuous双通路→控制支持显式化；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：MULTIMODAL-WORLD-MODELS；action-conditioned首段后两段 |
| [2605.23904 SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/html/2605.23904v1) | 2026-05-25 | 反复文本编辑失控→bounded patch/rejected buffer/protected slow-meta→编辑状态版本化；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-07-agent/74-prompt.md)：AGENT-PROMPT；SkillMOO后两段 |
| [2605.23454 ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning](https://arxiv.org/html/2605.23454v1) | 2026-05-25 | 开放任务缺exact verifier→source-grounded QA/reference/weighted rubric共生成→数据与判分资格分责；2+1+2=5 | 深入完成 | 整合：[章节](../../../../books/part-04-training-system/27-data.md)：TRAIN-DATA；synthetic首段后两段 |
| [2605.23163 Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving](https://arxiv.org/html/2605.23163v1) | 2026-05-25 | 固定schema仍逐token生成→scaffold/value分责与section-causal cache→格式不替动作验收；2+2+3=7 | 深入完成 | 整合：[章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：MULTIMODAL-EMBODIED-VLA；联合模型物理接口段前两段 |
| [2605.23025 World Machine: Towards Generative World Modeling for Time-Series](https://arxiv.org/html/2605.23025v1) | 2026-05-25 | state只能由encoder给→跨epoch预测回写与mask/break/local训练→参数与数据state共同生命周期；2+1+2=5 | 深入完成 | 整合：[章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：MULTIMODAL-WORLD-MODELS；Latent dynamics首边界段后两段 |
| [2605.23395 Convex Compositional Reasoning Models](https://arxiv.org/html/2605.23395v1) | 2026-05-25 | 只扩搜索→非负凸factor组合与convex relaxation→优化几何与离散validity分责；2+2+3=7 | 深入完成 | 整合：[章节](../../../../books/part-07-agent/79-planning.md)：AGENT-PLANNING；Search/Pruning首边界段后两段 |
| [2605.23055 Decomposing and Measuring Evaluation Awareness](https://arxiv.org/html/2605.23055v1) | 2026-05-25 | 评测识别率被当行为因果→environment/recognition/propensity分拆→sensor不授control；2+2+2=6 | 深入完成 | 已有覆盖：[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM；Evaluation-awareness必须分开Representation、Verbalization与Control |
| [2605.23393 Every Component is a Lookup: Token Attribution and Composition from a Single Decomposition](https://arxiv.org/html/2605.23393v1) | 2026-05-25 | 分开attention/MLP解释→统一KV/key-side递归credit→固定forward分解与反事实分开；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM；Interpretability Graph旧06480 binding前两段 |
| [2605.23096 Encrypted Neural Networks without Overflows](https://arxiv.org/html/2605.23096v1) | 2026-05-25 | 采样activation范围不足→合法输入overflow与逐层误差传播bounds→poly替换合同重审；3+2+3=8 | 深入完成 | 整合：[章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY；隐私明文边界TEE段后两段 |
| [2605.23262 Design and Report Benchmarks for Knowledge Work](https://arxiv.org/html/2605.23262v1) | 2026-05-25 | 知识工作benchmark抽象能力→activity/setting/workproduct绑定claim→成品分数不代真实工作流；1+2+2=5 | 标准完成 | 已有覆盖：[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM；EvalSpec/GDPval/native-editability实际链 |
| [2605.23668 OnePred: Next-Query Prediction via Recursive Intent Memory in Multi-Turn Conversations](https://arxiv.org/html/2605.23668v1) | 2026-05-25 | 全历史开销→下一query预测的bounded intent state→预测与压缩分责；2+2+2=6 | 标准完成 | 已有覆盖：[章节](../../../../books/part-07-agent/75-context.md)：AGENT-CONTEXT；OnePred bounded intent-state两段 |
| [2605.23826 Decomposing Queries into Tool Calls for Long-Video Keyframe Retrieval](https://arxiv.org/html/2605.23826v1) | 2026-05-25 | 单scorer视频召回→typed tool rankings与Boolean merge→覆盖不等QA足证；2+1+2=5 | 标准完成 | 已有覆盖：[章节](../../../../books/part-07-agent/76-rag.md)：AGENT-RAG；ToolMerge typed toolcalls/rankings/Boolean merge两段 |
| [2605.23701 Metadata Predictability Is Not Evidence Dependence: An Intervention-Based Audit for Weak-Label Benchmarks](https://arxiv.org/html/2605.23701v1) | 2026-05-25 | metadata可预测被当证据依赖→跨item evidence配对置换→reader与难度混杂分开；3+2+2=7 | 深入完成 | 整合：[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM；historical预测负控17692第二段后两段 |
| [2605.23595 Cost-Effective Model Evaluation with Meta-Learning](https://arxiv.org/html/2605.23595v1) | 2026-05-25 | 逐模型测性能昂贵→train/target hidden-state摘要的amortized evaluator→标签权限显式化；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM；Forecastability15134 marker后两段 |
| [2605.23066 Orbax: Distributed Checkpointing with JAX](https://arxiv.org/html/2605.23066v1) | 2026-05-25 | 单体checkpoint→typed separable checkpointables及abstract/concrete接口→加载和完整resume分责；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-04-training-system/35-checkpoint.md)：TRAIN-CHECKPOINT；reshard/load与weights-only分界后两段 |
| [2605.23045 The TIME Machine: On The Power of Motion for Efficient Perception](https://arxiv.org/html/2605.23045v1) | 2026-05-25 | 外观主导video表示→whole-track masked motion tokens→运动与外观独立消费；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)：MULTIMODAL-REPRESENTATION；时间同步/augmentation段后两段 |
| [2605.23176 DRIVESPATIAL: A Benchmark for Spatiotemporal Intelligence in VLMs for Autonomous Driving](https://arxiv.org/html/2605.23176v1) | 2026-05-25 | 跨view题可单view偷答→camera/track图约束构题→支持集进入EvalSpec；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM；三view00799后两段 |
| [2605.23216 CaST-Bench: Benchmarking Causal Chain-Grounded Spatio-Temporal Reasoning for Video Question Answering](https://arxiv.org/html/2605.23216v1) | 2026-05-25 | 只看答案正确→多实例时空证据链匹配与联合分项→grounding/答案分责；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM；PerceptionComp26653后两段 |
| [2605.23491 CoSPlay: Cooperative Self-Play at Test-Time with Self-Generated Code and Unit Test](https://arxiv.org/html/2605.23491v1) | 2026-05-25 | code/tests互相修复偏移→重算execution matrix与nontrivial支持→consensus不授真值；2+2+3=7 | 深入完成 | 整合：[章节](../../../../books/part-07-agent/80-reflection.md)：AGENT-REFLECTION；主动分裂15669后/AEWM前两段 |
| [2605.23237 StereoGenBench: A Synthetic Multi-Camera Benchmark for Stereo Generation under Controlled Baseline Regimes](https://arxiv.org/html/2605.23237v1) | 2026-05-25 | stereo混输入与目标camera→controlled baseline/geometry tiers→同scene诊断协议；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM；SGC19048第二段后两段 |
| [2605.23733 Any2Any: Efficient Cross-Embodiment Transfer for Humanoid Whole-Body Tracking](https://arxiv.org/html/2605.23733v1) | 2026-05-25 | 冻结policy输入语义失配→layout/joint/hip/closed-chain先对齐再LoRA dynamics→身体与参数分责；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：MULTIMODAL-EMBODIED-VLA；canonical手型16712后两段 |
| [2605.23255 Learning-Augmented Online Scheduling with Parsimonious Preemption](https://arxiv.org/html/2605.23255v1) | 2026-05-25 | 预测work只用于排序→milestone队列/epoch rounding→completion与preemption共同条件界；2+1+2=5 | 深入完成 | 整合：[章节](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)：PLATFORM-GPU-SCHEDULER；victim段后/quota重议前一段 |
| [2605.23651 How Human-Like Are Large Language Models? A Register-Aware Linguistic Evaluation Framework](https://arxiv.org/html/2605.23651v1) | 2026-05-25 | 总体像人分数→register匹配的human-reference two-sample MMD→参照人口进入量尺；2+2+2=6 | 深入完成 | 整合：[章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM；人类描述26589第二段后一段 |

## 4. 证据与知识整合

结构化 exact-version、locator、score、adopted proposition 与 non-proof boundary 见 [`evidence-review-v3.json`](../_sources/daily-20260526/evidence-review-v3.json)；Books 当前正文比较见 [`books-comparison-v3.json`](../_sources/daily-20260526/books-comparison-v3.json)。

### [2605.24321 Unified 3D Scene Understanding Through Physical World Modeling](https://arxiv.org/html/2605.24321v1)

<!-- review:SF-2026-ARXIV-2605-24321:start -->
证据位置：§3.1 local random-access sequence; §3.2 inference pathways；§4 Results; Appendix A.4 ablations；Appendix A.8 Limitations & Future Work。
<!-- claim:SF-2026-ARXIV-2605-24321:start -->把 World Model 的 task head 改写为对同一 RGB/flow/camera 图的 observation/query traversal；旧的 task-specific heads 仍是低成本、强约束 fallback，随机访问失配会造成局部不一致。<!-- claim:SF-2026-ARXIV-2605-24321:end -->
证据边界、trade-off、failure 与 fallback：`Unified 3D Scene Understanding Through Physical World Modeling` 只支持 exact-v1 披露的数据、backbone 与任务；感知质量不等于 physical/action fidelity。新增控制换来训练与评估成本，跨场景漂移时回退专用模型、真实状态 probe 或人工 gate。
Books：Applied；owner=MULTIMODAL-WORLD-MODELS。
<!-- review:SF-2026-ARXIV-2605-24321:end -->

### [2605.24322 Causal Physics Steering in Video World Models via Concept Activation Vectors](https://arxiv.org/html/2605.24322v1)

<!-- review:SF-2026-ARXIV-2605-24322:start -->
证据位置：§3.2 Physics Emergence Zone; §3.3 CAV; §3.4–§3.5 inference-time/per-block steering；§5.1–§5.6 steering, layer ablation and subspace tests；§7 Future Work; §8 Broader Impact; IntPhys/VideoMAE boundary。
<!-- claim:SF-2026-ARXIV-2605-24322:start -->把 World Model 的物理表示从只读 probe 提升为受限的 inference-time control surface：PEZ layer 的 probe weight 作为 CAV 写入 hidden state。它免训练但依赖 representation localization，错误 layer/方向会产生不真实 steering；因此只作为 rollout proposal，以真实观察/模拟器 gate，并在物理一致性失败时回退无 steering 基线。<!-- claim:SF-2026-ARXIV-2605-24322:end -->
证据边界、trade-off、failure 与 fallback：`Causal Physics Steering in Video World Models via Concept Activation Vectors` 只支持 exact-v1 披露的数据、backbone 与任务；感知质量不等于 physical/action fidelity。新增控制换来训练与评估成本，跨场景漂移时回退专用模型、真实状态 probe 或人工 gate。
Books：Applied；owner=MULTIMODAL-WORLD-MODELS。
<!-- review:SF-2026-ARXIV-2605-24322:end -->

### [2605.24326 ScaleAcross Explorer: Exploring Communication Optimization for Scale-Across AI Model Training](https://arxiv.org/html/2605.24326v1)

<!-- review:SF-2026-ARXIV-2605-24326:start -->
证据位置：§3–§6 placement, scheduling, network and ScaleAcross Explorer；§6.3 results; Appendix A testbed/simulation；§7 Lessons Learned; §8 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-24326:start -->把单机房 collective tuning 扩展为跨楼宇 placement、path、collective schedule 与 failure-domain 的联合搜索；跨域训练用通信优化换更大的 tail latency、模拟误差和故障面，收益失效时回退单站点或固定 hierarchy。<!-- claim:SF-2026-ARXIV-2605-24326:end -->
证据边界、trade-off、failure 与 fallback：`ScaleAcross Explorer: Exploring Communication Optimization for Scale-Across AI Model Training` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。
Books：Applied；owner=TRAIN-DISTRIBUTED-TRAINING。
<!-- review:SF-2026-ARXIV-2605-24326:end -->

### [2605.24330 Interdomain Attention: Beyond Token-Level Key-Value Memory](https://arxiv.org/html/2605.24330v1)

<!-- review:SF-2026-ARXIV-2605-24330:start -->
证据位置：§3.1–§3.4 Interdomain Attention and complexity；§4 FineWeb-Edu; Appendix B/C scaling；§4 Recall and limitations; §5 Future Work。
<!-- claim:SF-2026-ARXIV-2605-24330:start -->在 attention 的 query addressing 与 SSM 固定状态之间增加 query-conditioned basis projection；固定状态降低长度成本但牺牲精确 recall，超出状态预算或 recall gate 失败时回退 softmax/hybrid attention。<!-- claim:SF-2026-ARXIV-2605-24330:end -->
证据边界、trade-off、failure 与 fallback：`Interdomain Attention: Beyond Token-Level Key-Value Memory` 只在披露规模、数据与架构上成立。新增 representation/token-mixing 假设换取效率或可控性但可能损失 recall/兼容性；回归失败时回退标准 tokenizer/attention/layer。
Books：Applied；owner=MODEL-TRANSFORMER-LAYER。
<!-- review:SF-2026-ARXIV-2605-24330:end -->

### [2605.24331 CurveRL: Principled Distribution-Aware Context Reweighting for LLM Reasoning](https://arxiv.org/html/2605.24331v1)

<!-- review:SF-2026-ARXIV-2605-24331:start -->
证据位置：§3 utility-dependent context-distribution control; §4.1–§4.3 CurveRL；§5.1–§5.2 main results and mechanism analysis; Appendix C；§7 Discussion and Conclusion; Appendix D discussions; no dedicated limitations section。
<!-- claim:SF-2026-ARXIV-2605-24331:start -->Building on this optimality framework, we propose a distribution-aware prompt reweighting approach, called CurveRL, based on a quantile coordinate transform, in which the weight assigned to each prompt depends not on the absolute value of pass rates but on its rank and density to reflect the distributional structure of the pass rates in the learning dynamics.<!-- claim:SF-2026-ARXIV-2605-24331:end -->
证据边界、trade-off、failure 与 fallback：`CurveRL: Principled Distribution-Aware Context Reweighting for LLM Reasoning` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。
Books：No Change — Existing Coverage；owner=TRAIN-GRPO。
<!-- review:SF-2026-ARXIV-2605-24331:end -->

### [2605.24350 PACT: Proactive Asking for Continual Task Assistance in Human-Robot Collaboration](https://arxiv.org/html/2605.24350v1)

<!-- review:SF-2026-ARXIV-2605-24350:start -->
证据位置：§2.1 proactive ask-or-act; §2.2 clarification utility；§3.2–§3.3 main results and clarification analysis; Appendices D–E；§4 Discussion and Limitations。
<!-- claim:SF-2026-ARXIV-2605-24350:start -->Proactive ask-or-act planning combines current observation with cross-day history and evaluates clarification utility as assistance accuracy against clarification frequency, instead of treating every uncertainty as either silent inference or mandatory questioning.<!-- claim:SF-2026-ARXIV-2605-24350:end -->
证据边界、trade-off、failure 与 fallback：`PACT: Proactive Asking for Continual Task Assistance in Human-Robot Collaboration` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：No Change — Existing Coverage；owner=AGENT-PLANNING。
<!-- review:SF-2026-ARXIV-2605-24350:end -->

### [2605.24366 Structure-Aware RAG: Structured Retrieval Augmented Generation from Noisy Data for Conversational Agents](https://arxiv.org/html/2605.24366v1)

<!-- review:SF-2026-ARXIV-2605-24366:start -->
证据位置：§3.3 quality-aware metadata; §3.4 table generation; §3.5 structure-aware RAG；§4.2–§4.6 main results, table-quality analysis, ablation and cases；Limitations after §5; Appendix C offline/online case boundary。
<!-- claim:SF-2026-ARXIV-2605-24366:start -->把 noisy corpus 的表格从被动文档格式提升为带质量状态的 intermediate retrieval interface：metadata normalization/effectiveness 先受控更新，再以 semantic/structural consistency gate 生成表格。它减少噪声却新增表格化信息损失、metadata drift 和离线构建成本；失败时回退原文 chunk/hybrid retrieval，并保留 row/cell 到原文 provenance。<!-- claim:SF-2026-ARXIV-2605-24366:end -->
证据边界、trade-off、failure 与 fallback：`Structure-Aware RAG: Structured Retrieval Augmented Generation from Noisy Data for Conversational Agents` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：Applied；owner=AGENT-RAG。
<!-- review:SF-2026-ARXIV-2605-24366:end -->

### [2605.24375 Distilling Game Code World Model Generation into Lightweight Large Language Models](https://arxiv.org/html/2605.24375v1)

<!-- review:SF-2026-ARXIV-2605-24375:start -->
证据位置：§4.1 data; §4.2 four-tier verification; §4.3 SFT/RLVR；§5.1–§5.2 experiments; Appendix E ablation；§5.2 disclosed SFT/RLVR limitations; §6 Future Work。
<!-- claim:SF-2026-ARXIV-2605-24375:start -->Executable game world models can be post-trained with a four-tier verifier spanning static structure, fuzzed dynamics, semantic rule traces and information consistency, so SFT/RLVR optimize more than code syntax.<!-- claim:SF-2026-ARXIV-2605-24375:end -->
证据边界、trade-off、failure 与 fallback：`Distilling Game Code World Model Generation into Lightweight Large Language Models` 只支持 exact-v1 披露的数据、backbone 与任务；感知质量不等于 physical/action fidelity。新增控制换来训练与评估成本，跨场景漂移时回退专用模型、真实状态 probe 或人工 gate。
Books：No Change — Existing Coverage；owner=MULTIMODAL-WORLD-MODELS。
<!-- review:SF-2026-ARXIV-2605-24375:end -->

### [2605.24383 A governance horizon for ethical-use constraints in open-weight AI models](https://arxiv.org/html/2605.24383v1)

<!-- review:SF-2026-ARXIV-2605-24383:start -->
证据位置：§2 governance-horizon evidence; §4 lineage methods；§2.1–§2.5 and supplements S1–S6；§3.3 Limitations and outlook。
<!-- claim:SF-2026-ARXIV-2605-24383:start -->把 open-weight restriction 从可选 model-card 文本升级为随 lineage/merge 传播的 machine-readable governance state；声明继承降低发布摩擦但会产生 orphan/merge undecidability，无法解析时必须阻断自动合规结论并转人工。<!-- claim:SF-2026-ARXIV-2605-24383:end -->
证据边界、trade-off、failure 与 fallback：`A governance horizon for ethical-use constraints in open-weight AI models` 只覆盖披露的 threat model、模型和攻击预算，不证明一般安全。新增 detector/defense 会引入误拒与适应性绕过；证据不足时回退隔离、最小权限、规则验证与人工处置。
Books：Applied；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-24383:end -->

### [2605.24384 Side-by-side Comparison Amplifies Dialect Bias in Language Models](https://arxiv.org/html/2605.24384v1)

<!-- review:SF-2026-ARXIV-2605-24384:start -->
证据位置：§3 Experimental Setup, especially §3.2 matched-guise and §3.4 metrics；§4.1–§4.3 absolute/contrastive bias and fairness fine-tuning；§7 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24384:start -->Encouragingly, we show that counterfactual fairness finetuning can mitigate covert dialect bias for some stereotypical traits, reducing average disparities when evaluating tweets in isolation, however, these improvements do not consistently hold across traits when evaluating SAE / AAVE tweets side by side.<!-- claim:SF-2026-ARXIV-2605-24384:end -->
证据边界、trade-off、failure 与 fallback：`Side-by-side Comparison Amplifies Dialect Bias in Language Models` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-24384:end -->

### [2605.24391 MX-SAFE: Versatile Inference- and Training-Proof Microscaling Format with On-the-Fly Exponent and Mantissa Bit Allocation](https://arxiv.org/html/2605.24391v1)

<!-- review:SF-2026-ARXIV-2605-24391:start -->
证据位置：§IV MX-SAFE format; §V accelerator；§VI Experimental Results；§VII Conclusion; tested MXSF hardware/model boundary。
<!-- claim:SF-2026-ARXIV-2605-24391:start -->In this work, we present a versatile MXFP format, called MX-SAFE (MXSF in short), that adaptively uses two modes, i.e., a wider mantissa mode (FP8 E2M5) and a subnormal FP mode (FP5 E3M2), to support both training and direct-cast inference.<!-- claim:SF-2026-ARXIV-2605-24391:end -->
证据边界、trade-off、failure 与 fallback：`MX-SAFE: Versatile Inference- and Training-Proof Microscaling Format with On-the-Fly Exponent and Mantissa Bit Allocation` 的收益受模型、硬件、精度、长度、batch/concurrency 与 SLO 限制。新增压缩/路由状态会产生误差和管理成本；质量或 tail-latency gate 失败时回退 dense/full-precision/原生 decode。
Books：Applied；owner=INFER-TENSORRT-LLM。
<!-- review:SF-2026-ARXIV-2605-24391:end -->

### [2605.24396 Understanding and Mitigating Premature Confidence for Better LLM Reasoning](https://arxiv.org/html/2605.24396v1)

<!-- review:SF-2026-ARXIV-2605-24396:start -->
证据位置：§2 correlation analysis; §3 Progressive Confidence Shaping；§2.2 and §3.2 results; Appendices C–G；§4 factors affecting premature confidence; §5 Conclusion; no dedicated limitations section。
<!-- claim:SF-2026-ARXIV-2605-24396:start -->We find such a signal in how the model's confidence evolves during reasoning: premature confidence, the tendency to commit to an answer early and use the remaining tokens to rationalize it, strongly predicts flawed reasoning across tasks and model scales.<!-- claim:SF-2026-ARXIV-2605-24396:end -->
证据边界、trade-off、failure 与 fallback：`Understanding and Mitigating Premature Confidence for Better LLM Reasoning` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-24396:end -->

### [2605.24420 Batch Normalization Amplifies Memorization and Privacy Risks](https://arxiv.org/html/2605.24420v1)

<!-- review:SF-2026-ARXIV-2605-24420:start -->
证据位置：§3 Methodology; §5 theory; §6 mitigation；§4 Experiments; §4.3 membership inference；Appendix A.3 theoretical limitations; tested normalization/model/data boundary。
<!-- claim:SF-2026-ARXIV-2605-24420:start -->Batch-coupled normalization statistics amplify atypical-sample influence and memorization, and the measured amplification carries through to membership-inference susceptibility; privacy comparisons must therefore hold normalization and batch composition fixed.<!-- claim:SF-2026-ARXIV-2605-24420:end -->
证据边界、trade-off、failure 与 fallback：`Batch Normalization Amplifies Memorization and Privacy Risks` 只覆盖披露的 threat model、模型和攻击预算，不证明一般安全。新增 detector/defense 会引入误拒与适应性绕过；证据不足时回退隔离、最小权限、规则验证与人工处置。
Books：Applied；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-24420:end -->

### [2605.24421 Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content](https://arxiv.org/html/2605.24421v1)

<!-- review:SF-2026-ARXIV-2605-24421:start -->
证据位置：§2 Threat Model; §3 taxonomy; §4 pipeline/defenses；§5 Experiments；§6.4 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24421:start -->We introduce a four-class taxonomy of log-substrate attacks: direct override (S1), persona hijack (S2), context manipulation (S3), and obfuscated payloads (S4).<!-- claim:SF-2026-ARXIV-2605-24421:end -->
证据边界、trade-off、failure 与 fallback：`Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content` 只覆盖披露的 threat model、模型和攻击预算，不证明一般安全。新增 detector/defense 会引入误拒与适应性绕过；证据不足时回退隔离、最小权限、规则验证与人工处置。
Books：Applied；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-24421:end -->

### [2605.24423 Benchmarking the Limits of In-Context Reinforcement Learning for Ad-Hoc Teamwork](https://arxiv.org/html/2605.24423v1)

<!-- review:SF-2026-ARXIV-2605-24423:start -->
证据位置：§3 problem setting；§4 ICRL4AHT benchmark、teammate suite 与 learning-history pipeline；§5 结果、adaptation curves 与 longer-context/scale/recurrent diagnostics；§6 与 Appendix G limitations。
<!-- claim:SF-2026-ARXIV-2605-24423:start -->History-conditioned ICRL is not itself sufficient evidence of partner adaptation: under controlled unseen-teammate/layout shifts and partial observability, AD/DPT and longer-context/model/recurrent diagnostics often fail to improve within context. Multi-agent evaluation must measure partner-policy inference and adaptation gain separately from memory capacity.<!-- claim:SF-2026-ARXIV-2605-24423:end -->
证据边界、trade-off、failure 与 fallback：负结果只覆盖 OvercookedV2、有限 teammate suite、两玩家固定非自适应伙伴、AD/DPT 与披露 diagnostics，不能证明其他环境中的 ICRL 都无法适应。更丰富的 partner-state probe 会增加评测成本并可能过拟合有限 suite；有效性失败时回退显式 partner-policy 测试、held-out shift 与 no-adaptation baseline，不能把长 context 当作适应证据。
Books：No Change — Existing Coverage；owner=AGENT-MULTI-AGENT。
<!-- review:SF-2026-ARXIV-2605-24423:end -->

### [2605.24425 Momentum Streams for Optimizer-Inspired Transformers](https://arxiv.org/html/2605.24425v1)

<!-- review:SF-2026-ARXIV-2605-24425:start -->
证据位置：§§3–5 optimizer view, optimizer-inspired block and momentum stream；§4.2; §§5–6; Appendix D Experimental Details；§7 Conclusion; architecture/scale/recipe boundary。
<!-- claim:SF-2026-ARXIV-2605-24425:start -->The residual update of a pre-norm Transformer layer admits an interpretation as one step of a first-order optimizer acting on a surrogate token energy, wherein the attention and MLP sublayers function as gradient oracles.<!-- claim:SF-2026-ARXIV-2605-24425:end -->
证据边界、trade-off、failure 与 fallback：`Momentum Streams for Optimizer-Inspired Transformers` 只在披露规模、数据与架构上成立。新增 representation/token-mixing 假设换取效率或可控性但可能损失 recall/兼容性；回归失败时回退标准 tokenizer/attention/layer。
Books：Applied；owner=MODEL-TRANSFORMER-LAYER。
<!-- review:SF-2026-ARXIV-2605-24425:end -->

### [2605.24426 SEAL: Synergistic Co-Evolution of Agents and Learning Environments](https://arxiv.org/html/2605.24426v1)

<!-- review:SF-2026-ARXIV-2605-24426:start -->
证据位置：§3 verifier-grounded diagnosis, interface evolution and advantage reweighting；§4 Experiments; Appendix C controlled protocol；§5 Conclusion and Limitations。
<!-- claim:SF-2026-ARXIV-2605-24426:start -->We propose SEAL, a closed-loop co-evolution framework for interactive tool-use agents.<!-- claim:SF-2026-ARXIV-2605-24426:end -->
证据边界、trade-off、failure 与 fallback：`SEAL: Synergistic Co-Evolution of Agents and Learning Environments` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。
Books：Applied；owner=TRAIN-RLHF。
<!-- review:SF-2026-ARXIV-2605-24426:end -->

### [2605.24432 Found in Conversation: LLMs Teach Themselves to Close the Multi-Turn Gap](https://arxiv.org/html/2605.24432v1)

<!-- review:SF-2026-ARXIV-2605-24432:start -->
证据位置：§3.1 SFT grounded context; §3.2 view-asymmetric self-distillation；§4 Results and ablations；§6 limitations; Appendix C evaluation limits。
<!-- claim:SF-2026-ARXIV-2605-24432:start -->把单轮能力到多轮能力的迁移建模为 information-equivalent views 的自蒸馏，并把未充分信息时的 defer/clarify 写入训练目标；视图不等价会蒸馏错误，失败时回退显式澄清策略与外部 teacher。<!-- claim:SF-2026-ARXIV-2605-24432:end -->
证据边界、trade-off、failure 与 fallback：`Found in Conversation: LLMs Teach Themselves to Close the Multi-Turn Gap` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。
Books：Applied；owner=TRAIN-SFT。
<!-- review:SF-2026-ARXIV-2605-24432:end -->

### [2605.24433 Smoother Action Chunking Flow Policy via Prior-Corrected Orthogonal Trust-Region Guidance](https://arxiv.org/html/2605.24433v1)

<!-- review:SF-2026-ARXIV-2605-24433:start -->
证据位置：§III-A prior-corrected weight; §III-B orthogonal trust-region guidance; §III-C algorithm；§IV-A–§IV-H experiments and ablations；§V Conclusion; evidence is bounded to the disclosed LIBERO/π0.5 setting。
<!-- claim:SF-2026-ARXIV-2605-24433:start -->We propose POTR, a **p**rior-corrected **o**rthogonal **t**rust-**r**egion guidance method.<!-- claim:SF-2026-ARXIV-2605-24433:end -->
证据边界、trade-off、failure 与 fallback：`Smoother Action Chunking Flow Policy via Prior-Corrected Orthogonal Trust-Region Guidance` 只支持 exact-v1 披露的数据、backbone 与任务；感知质量不等于 physical/action fidelity。新增控制换来训练与评估成本，跨场景漂移时回退专用模型、真实状态 probe 或人工 gate。
Books：No Change — Existing Coverage；owner=MULTIMODAL-EMBODIED-VLA。
<!-- review:SF-2026-ARXIV-2605-24433:end -->

### [2605.24461 Provisioning to Runtime Optimization of a 100 MW-Scale AI Cluster](https://arxiv.org/html/2605.24461v1)

<!-- review:SF-2026-ARXIV-2605-24461:start -->
证据位置：§3 power hierarchy; §§4–6 provisioning, validation and active operation；§4.2 empirical data; §§5–7 deployment/runtime measurements；§8 Research Wishlist; §10 Conclusion; single 150MW/83K-GB200 site boundary。
<!-- claim:SF-2026-ARXIV-2605-24461:start -->We present detailed power measurements for a 150 MW datacenter hosting a cluster of 83K GB200 GPUs.<!-- claim:SF-2026-ARXIV-2605-24461:end -->
证据边界、trade-off、failure 与 fallback：`Provisioning to Runtime Optimization of a 100 MW-Scale AI Cluster` 提供受限机制线索，但当前没有唯一稳定 owner 或足够外部验证；不把原型结果升级为通用系统保证，失败时保持现有架构并在季度结构复核中重开。
Books：Applied；owner=PLATFORM-GPU-SCHEDULER。
<!-- review:SF-2026-ARXIV-2605-24461:end -->

### [2605.24468 SAM: State-Adaptive Memory for Long-Horizon Reasoning Agent](https://arxiv.org/html/2605.24468v1)

<!-- review:SF-2026-ARXIV-2605-24468:start -->
证据位置：§2.2–§2.3 State-Adaptive Memory and optimization；§3 Experiments; §4 Discussions；Appendix A Limitations and Broader Impact。
<!-- claim:SF-2026-ARXIV-2605-24468:start -->To this end, we propose State-Adaptive Memory~(SAM), a standalone framework that consolidates ongoing interaction into compact memory cues while preserving raw trajectory pages for intent-driven recall.<!-- claim:SF-2026-ARXIV-2605-24468:end -->
证据边界、trade-off、failure 与 fallback：`SAM: State-Adaptive Memory for Long-Horizon Reasoning Agent` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：No Change — Existing Coverage；owner=AGENT-MEMORY。
<!-- review:SF-2026-ARXIV-2605-24468:end -->

### [2605.24486 AgentFugue: Agent Scaling for Long-Horizon Tasks through Collective Reasoning](https://arxiv.org/html/2605.24486v1)

<!-- review:SF-2026-ARXIV-2605-24486:start -->
证据位置：§2.1 problem setting; §2.2 shared hub; §2.3 optimization；§3.3–§3.6 results and ablations; Appendix E cases；Appendix G Limitations and Broader Impact。
<!-- claim:SF-2026-ARXIV-2605-24486:start -->Recent progress on long-horizon agentic tasks has been driven largely by scaling up individual agents through stronger models, better tools, and more effective scaffolding.<!-- claim:SF-2026-ARXIV-2605-24486:end -->
证据边界、trade-off、failure 与 fallback：`AgentFugue: Agent Scaling for Long-Horizon Tasks through Collective Reasoning` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：No Change — Existing Coverage；owner=AGENT-MULTI-AGENT。
<!-- review:SF-2026-ARXIV-2605-24486:end -->

### [2605.24497 Reasoning as an Attack Surface: Adaptive Evolutionary CoT Jailbreaks for LLMs](https://arxiv.org/html/2605.24497v1)

<!-- review:SF-2026-ARXIV-2605-24497:start -->
证据位置：§3.2–§3.5 formulation, structured search, adaptive evolutionary optimization and fitness；§4.2–§4.8 transfer, efficiency, ablation and defense analysis; Appendices C–J；§5 Conclusion and Impact Statement; no dedicated limitations section。
<!-- claim:SF-2026-ARXIV-2605-24497:start -->To overcome these limitations, we propose an adaptive evolutionary CoT jailbreak framework, called AE-CoT.<!-- claim:SF-2026-ARXIV-2605-24497:end -->
证据边界、trade-off、failure 与 fallback：`Reasoning as an Attack Surface: Adaptive Evolutionary CoT Jailbreaks for LLMs` 只覆盖披露的 threat model、模型和攻击预算，不证明一般安全。新增 detector/defense 会引入误拒与适应性绕过；证据不足时回退隔离、最小权限、规则验证与人工处置。
Books：No Change — Existing Coverage；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-24497:end -->

### [2605.24509 Φ-Noise: Training-Free Temporal Video Conditioning via Phase-Based Noise Manipulation](https://arxiv.org/html/2605.24509v1)

<!-- review:SF-2026-ARXIV-2605-24509:start -->
证据位置：§3 spectral analysis; §4 phase substitution and energy balancing；§6.2–§6.4 comparisons and generalization; Appendix B；§7 Limitations and Conclusion。
<!-- claim:SF-2026-ARXIV-2605-24509:start -->Low-frequency phase from a reference video can condition diffusion noise without model retraining, while energy balancing limits the amplitude distortion introduced by spectral substitution.<!-- claim:SF-2026-ARXIV-2605-24509:end -->
证据边界、trade-off、failure 与 fallback：`Φ-Noise: Training-Free Temporal Video Conditioning via Phase-Based Noise Manipulation` 只支持 exact-v1 披露的数据、backbone 与任务；感知质量不等于 physical/action fidelity。新增控制换来训练与评估成本，跨场景漂移时回退专用模型、真实状态 probe 或人工 gate。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-24509:end -->

### [2605.24517 ECHO: Terminal Agents Learn World Models for Free](https://arxiv.org/html/2605.24517v1)

<!-- review:SF-2026-ARXIV-2605-24517:start -->
证据位置：§3 ECHO objective and observation targets；§4–§5 TerminalBench evaluation；§7 Conclusion; disclosed terminal-observation boundary。
<!-- claim:SF-2026-ARXIV-2605-24517:start -->把 agent rollout 中环境 observation tokens 从只读 context 升级为辅助预测目标，与 action policy gradient 分责；dense signal 可能奖励可预测而非可控环境，故要以 task verifier/held-out dynamics gate，并可回退标准 GRPO。<!-- claim:SF-2026-ARXIV-2605-24517:end -->
证据边界、trade-off、failure 与 fallback：`ECHO: Terminal Agents Learn World Models for Free` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。
Books：Applied；owner=TRAIN-RLHF。
<!-- review:SF-2026-ARXIV-2605-24517:end -->

### [2605.24518 Grammatically-Guided Sparse Attention for Efficient and Interpretable Transformers](https://arxiv.org/pdf/2605.24518v1)

<!-- review:SF-2026-ARXIV-2605-24518:start -->
证据位置：PDF v1 pp.3–5 §3 Methodology and §4.1 architecture/implementation；PDF v1 pp.5–7 §4.5 strategies and §5 Results and Discussions；PDF v1 pp.7–8 §6 Conclusion/Future Work and Limitations。
<!-- claim:SF-2026-ARXIV-2605-24518:start -->Part-of-speech-derived hard or soft masks reduce the theoretical self-attention graph, but the disclosed CPU mask generation, tiny model and length-128 experiment do not establish production speedup or long-context quality.<!-- claim:SF-2026-ARXIV-2605-24518:end -->
证据边界、trade-off、failure 与 fallback：`Grammatically-Guided Sparse Attention for Efficient and Interpretable Transformers` 只在披露规模、数据与架构上成立。新增 representation/token-mixing 假设换取效率或可控性但可能损失 recall/兼容性；回归失败时回退标准 tokenizer/attention/layer。
Books：No Change — Existing Coverage；owner=MODEL-SELF-ATTENTION。
<!-- review:SF-2026-ARXIV-2605-24518:end -->

### [2605.24535 Steering Beyond the Support: Adversarial Training on Unsupervised Jailbroken Activation Simulation](https://arxiv.org/html/2605.24535v1)

<!-- review:SF-2026-ARXIV-2605-24535:start -->
证据位置：§4 Learnable Steering; §5 bi-level adversarial training；§6–§9 main, mechanistic and ablation results；Appendix A Limitations and Future Work。
<!-- claim:SF-2026-ARXIV-2605-24535:start -->We propose a bi-level adversarial training framework for zero-shot jailbreak defense.<!-- claim:SF-2026-ARXIV-2605-24535:end -->
证据边界、trade-off、failure 与 fallback：`Steering Beyond the Support: Adversarial Training on Unsupervised Jailbroken Activation Simulation` 只覆盖披露的 threat model、模型和攻击预算，不证明一般安全。新增 detector/defense 会引入误拒与适应性绕过；证据不足时回退隔离、最小权限、规则验证与人工处置。
Books：No Change — Existing Coverage；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-24535:end -->

### [2605.24538 Is Decentralized AI Governable? From Regulative Policy to Constitutive Protocol](https://arxiv.org/html/2605.24538v1)

<!-- review:SF-2026-ARXIV-2605-24538:start -->
证据位置：§2 six-layer decentralization/governance vacuum; §4 protocol as architectural constraint；§4.3 early protocol experiments; conceptual analysis rather than controlled benchmark；§4.4 ethical conditions; §5 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-24538:start -->When model, training, compute, harness, identity and ownership are decentralized together, governance can lose both an addressable principal and an actor capable of changing the running system, motivating protocol-level constitutive constraints subject to legitimacy and contestability.<!-- claim:SF-2026-ARXIV-2605-24538:end -->
证据边界、trade-off、failure 与 fallback：`Is Decentralized AI Governable? From Regulative Policy to Constitutive Protocol` 提供受限机制线索，但当前没有唯一稳定 owner 或足够外部验证；不把原型结果升级为通用系统保证，失败时保持现有架构并在季度结构复核中重开。
Books：Structural Candidate；owner=无唯一 owner。
<!-- review:SF-2026-ARXIV-2605-24538:end -->

### [2605.24539 DemoEvolve: Overcoming Sparse Feedback in Agentic Harness Evolution with Demonstrations](https://arxiv.org/html/2605.24539v1)

<!-- review:SF-2026-ARXIV-2605-24539:start -->
证据位置：§3 harness-evolution information regimes；§4 Liar's Dice/Balatro controls；§6 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24539:start -->把 harness evolution 的 reward-only search 改成 demonstration-guided program edit localization；demonstration 提高可诊断性但引入示范偏差和额外审计成本，固定种子 paired gate 失败时回退人工 harness 与不变基线。<!-- claim:SF-2026-ARXIV-2605-24539:end -->
证据边界、trade-off、failure 与 fallback：`DemoEvolve: Overcoming Sparse Feedback in Agentic Harness Evolution with Demonstrations` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：Applied；owner=AGENT-PLATFORM。
<!-- review:SF-2026-ARXIV-2605-24539:end -->

### [2605.24541 SemanticZip: A Pilot Framework for Lossy Text Compression with LLMs as Semantic Decompressors](https://arxiv.org/html/2605.24541v1)

<!-- review:SF-2026-ARXIV-2605-24541:start -->
证据位置：§3 formulation; §4 semantic-compression regimes; §5 hybrid protected/lossy architecture；§6 setup; §7 pilot results；§9 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24541:start -->Rather, we introduce a reproducible experimental interface for studying lossy, LLM-decompressible text codes and a design principle: safety-critical and exact commitments should remain protected, while predictable low-risk context may be semantically zipped.<!-- claim:SF-2026-ARXIV-2605-24541:end -->
证据边界、trade-off、failure 与 fallback：`SemanticZip: A Pilot Framework for Lossy Text Compression with LLMs as Semantic Decompressors` 提供受限机制线索，但当前没有唯一稳定 owner 或足够外部验证；不把原型结果升级为通用系统保证，失败时保持现有架构并在季度结构复核中重开。
Books：Structural Candidate；owner=无唯一 owner。
<!-- review:SF-2026-ARXIV-2605-24541:end -->

### [2605.24545 Rethinking Federated Unlearning via the Lens of Memorization](https://arxiv.org/html/2605.24545v1)

<!-- review:SF-2026-ARXIV-2605-24545:start -->
证据位置：§4 memorization definitions; §5 grouped metric; §6.1–§6.2 FedMemPrune；§7.2 results; §7.3 ablations; Appendices F–G metric checks；§7.4 and Appendix H discussion; retraining remains the reference boundary。
<!-- claim:SF-2026-ARXIV-2605-24545:start -->把 federated unlearning 的删除目标从参数距离或整类性能改为待删数据的 unique memorization，并保留与 remaining clients 重叠的知识。Grouped Memorization Evaluation 与 prune/reinitialize/fine-tune 提供近似路径，但定位错误会删错共享知识；高风险删除仍以 retraining/attack audit 为 gate，失败时回退完整重训。<!-- claim:SF-2026-ARXIV-2605-24545:end -->
证据边界、trade-off、failure 与 fallback：`Rethinking Federated Unlearning via the Lens of Memorization` 只覆盖披露的 threat model、模型和攻击预算，不证明一般安全。新增 detector/defense 会引入误拒与适应性绕过；证据不足时回退隔离、最小权限、规则验证与人工处置。
Books：Applied；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-24545:end -->

### [2605.24547 RL with Learnable Textual Feedback: A Bilevel Approach](https://arxiv.org/html/2605.24547v1)

<!-- review:SF-2026-ARXIV-2605-24547:start -->
证据位置：§2 problem formulation; §3 bilevel natural-language actor-critic；§4 Experiments; Appendix A.5 efficiency；§5 Conclusion; tested task/model and higher-order-gradient boundary。
<!-- claim:SF-2026-ARXIV-2605-24547:start -->Textual feedback is a learnable policy component coupled bilevel to the actor, rather than a fixed correct annotation; Bi-NAC trains the critic for downstream reward improvement and the actor to exploit that feedback.<!-- claim:SF-2026-ARXIV-2605-24547:end -->
证据边界、trade-off、failure 与 fallback：`RL with Learnable Textual Feedback: A Bilevel Approach` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。
Books：Applied；owner=TRAIN-RLHF。
<!-- review:SF-2026-ARXIV-2605-24547:end -->

### [2605.24549 PALoRA: Projection-Adaptive LoRA for Preserving Reasoning in Large Language Models](https://arxiv.org/html/2605.24549v1)

<!-- review:SF-2026-ARXIV-2605-24549:start -->
证据位置：§3 PALoRA two-phase projection constraint；§4 experiments and ablations；Appendix A.6 limitation; Appendix C overhead。
<!-- claim:SF-2026-ARXIV-2605-24549:start -->在 LoRA 更新前用冻结 SVF probe 标记 skill-critical singular subspace，再约束知识注入的投影；probe 失配会保护错误子空间且增加两阶段成本，回退普通 LoRA、全量回归测试或停止注入。<!-- claim:SF-2026-ARXIV-2605-24549:end -->
证据边界、trade-off、failure 与 fallback：`PALoRA: Projection-Adaptive LoRA for Preserving Reasoning in Large Language Models` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。
Books：Applied；owner=TRAIN-LORA。
<!-- review:SF-2026-ARXIV-2605-24549:end -->

### [2605.24550 Jailbreak to Protect: Buffering and Reinforcing via Temporary Jailbreaking for Safe Fine-Tuning in Large Language Models](https://arxiv.org/html/2605.24550v1)

<!-- review:SF-2026-ARXIV-2605-24550:start -->
证据位置：§3 threat model; §4 buffering analysis; §5 BufferLoRA/ReinforceLoRA；§6 and §6.1–§6.3 results; Appendix B；§7 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24550:start -->Based on this insight, we propose a Buffer-and-Reinforce fine-tuning framework that buffers harmful updates during user fine-tuning and reinforces safety after adaptation.<!-- claim:SF-2026-ARXIV-2605-24550:end -->
证据边界、trade-off、failure 与 fallback：`Jailbreak to Protect: Buffering and Reinforcing via Temporary Jailbreaking for Safe Fine-Tuning in Large Language Models` 只覆盖披露的 threat model、模型和攻击预算，不证明一般安全。新增 detector/defense 会引入误拒与适应性绕过；证据不足时回退隔离、最小权限、规则验证与人工处置。
Books：No Change — Existing Coverage；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-24550:end -->

### [2605.24552 Ellipsoid Control: A White-list Jailbreak Defense via Benign Latent Modeling](https://arxiv.org/html/2605.24552v1)

<!-- review:SF-2026-ARXIV-2605-24552:start -->
证据位置：§III-B benign constraints; §III-C/§III-D projection; §III-E/§III-F derivation and implementation；§IV-A–§IV-I evaluation; §V cost；§VII Limitations and Future Work。
<!-- claim:SF-2026-ARXIV-2605-24552:start -->To answer this, we propose Ellipsoid Control, a test-time defense.<!-- claim:SF-2026-ARXIV-2605-24552:end -->
证据边界、trade-off、failure 与 fallback：`Ellipsoid Control: A White-list Jailbreak Defense via Benign Latent Modeling` 只覆盖披露的 threat model、模型和攻击预算，不证明一般安全。新增 detector/defense 会引入误拒与适应性绕过；证据不足时回退隔离、最小权限、规则验证与人工处置。
Books：No Change — Existing Coverage；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-24552:end -->

### [2605.24556 The Multilingual Curse at the Retrieval Layer: Evidence from Amharic](https://arxiv.org/html/2605.24556v1)

<!-- review:SF-2026-ARXIV-2605-24556:start -->
证据位置：§3.1 benchmark/relevance metrics; §3.2 models; §3.3 training and indexing；§4.1–§4.3 zero-shot, fine-tuned and reranking results；§5 Discussion; §7 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24556:start -->We argue that this assumption breaks down for underrepresented, morphologically rich languages, and use Amharic as a diagnostic case.<!-- claim:SF-2026-ARXIV-2605-24556:end -->
证据边界、trade-off、failure 与 fallback：`The Multilingual Curse at the Retrieval Layer: Evidence from Amharic` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：No Change — Existing Coverage；owner=AGENT-RAG。
<!-- review:SF-2026-ARXIV-2605-24556:end -->

### [2605.24570 PILOT: Policy-Informed Learned Optimization for Adaptive Deep Network Training](https://arxiv.org/html/2605.24570v1)

<!-- review:SF-2026-ARXIV-2605-24570:start -->
证据位置：§3.2.1–§3.2.4 gradient agreement, policy and online update；§4.1–§4.5 datasets, stability, ablations and transfer；§5.1 Limitations; §5.2 Future Work。
<!-- claim:SF-2026-ARXIV-2605-24570:start -->Gradient-direction agreement controls an online learned optimizer policy that changes its mixture of momentum, normalization and sign-based updates across locally stable or noisy regimes, but evidence is limited to small vision datasets/models.<!-- claim:SF-2026-ARXIV-2605-24570:end -->
证据边界、trade-off、failure 与 fallback：`PILOT: Policy-Informed Learned Optimization for Adaptive Deep Network Training` 提供受限机制线索，但当前没有唯一稳定 owner 或足够外部验证；不把原型结果升级为通用系统保证，失败时保持现有架构并在季度结构复核中重开。
Books：Structural Candidate；owner=无唯一 owner。
<!-- review:SF-2026-ARXIV-2605-24570:end -->

### [2605.24577 Polymorphism Is Rotation: Operational Mechanistic Interpretability from a Two-Layer Transformer to Pythia-70m](https://arxiv.org/html/2605.24577v1)

<!-- review:SF-2026-ARXIV-2605-24577:start -->
证据位置：§2 operational bars; §3 five-lens stack; §8 rotation audit and hypothesis；§6–§8 within-seed, cross-seed and Pythia-70m tests; Appendices A–E；§10 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24577:start -->Independently trained transformers compute the same function in residual-stream bases that differ by a uniform random rotation on $\mathrm{SO}(d_{\mathrm{model}})$.<!-- claim:SF-2026-ARXIV-2605-24577:end -->
证据边界、trade-off、failure 与 fallback：`Polymorphism Is Rotation: Operational Mechanistic Interpretability from a Two-Layer Transformer to Pythia-70m` 只在披露规模、数据与架构上成立。新增 representation/token-mixing 假设换取效率或可控性但可能损失 recall/兼容性；回归失败时回退标准 tokenizer/attention/layer。
Books：Report Only；owner=MODEL-SELF-ATTENTION。
<!-- review:SF-2026-ARXIV-2605-24577:end -->

### [2605.24578 World Models as Group Actions](https://arxiv.org/html/2605.24578v1)

<!-- review:SF-2026-ARXIV-2605-24578:start -->
证据位置：§2 group-action formulation; §3 latent regularization；§4 experiments; Appendix C–E probes；Appendix A.4 approximation; Appendix H scope。
<!-- claim:SF-2026-ARXIV-2605-24578:start -->World Model 除视觉质量外还要通过 identity/inverse/composition action probes；latent surrogate 降低成本但不等于真实 state dynamics，pose recovery 或 group assumption 失效时回退真实 rollout/状态测量。<!-- claim:SF-2026-ARXIV-2605-24578:end -->
证据边界、trade-off、failure 与 fallback：`World Models as Group Actions` 只支持 exact-v1 披露的数据、backbone 与任务；感知质量不等于 physical/action fidelity。新增控制换来训练与评估成本，跨场景漂移时回退专用模型、真实状态 probe 或人工 gate。
Books：Applied；owner=MULTIMODAL-WORLD-MODELS。
<!-- review:SF-2026-ARXIV-2605-24578:end -->

### [2605.24579 WhenLoss: Diagnosing Write and Retrieval Bottlenecks in Long-Context Memory Systems](https://arxiv.org/html/2605.24579v1)

<!-- review:SF-2026-ARXIV-2605-24579:start -->
证据位置：§3 four-condition diagnostic; §4 expected predictive compression；§5 Experimental Setup; §6 Results; §7 Analysis；§7 Analysis and §8 Conclusion; tested readers, memories and two benchmarks。
<!-- claim:SF-2026-ARXIV-2605-24579:start -->We introduce a four-condition diagnostic protocol that evaluates a fixed reader under truncated full context (TFC), oracle evidence (OE), complete stored memory (CSM), and retrieved memory (RM).<!-- claim:SF-2026-ARXIV-2605-24579:end -->
证据边界、trade-off、failure 与 fallback：`WhenLoss: Diagnosing Write and Retrieval Bottlenecks in Long-Context Memory Systems` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：Applied；owner=AGENT-MEMORY。
<!-- review:SF-2026-ARXIV-2605-24579:end -->

### [2605.24583 Measuring Alignment-Induced Activation Shifts Correctly: A Template-Controlled Difference-in-Differences Protocol](https://arxiv.org/html/2605.24583v1)

<!-- review:SF-2026-ARXIV-2605-24583:start -->
证据位置：§§2–4 separability metric and three confound-control tests；§§5–6 calibration and current-alignment audit；§7 Scope; §8 open problem and failed spectral-gap claim。
<!-- claim:SF-2026-ARXIV-2605-24583:start -->A template-controlled four-way difference-in-differences protocol separates chat-format shift from alignment-induced activation shift, and causal projection ablation—not singular-value order—tests whether the recovered subspace is behaviorally active.<!-- claim:SF-2026-ARXIV-2605-24583:end -->
证据边界、trade-off、failure 与 fallback：`Measuring Alignment-Induced Activation Shifts Correctly: A Template-Controlled Difference-in-Differences Protocol` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。
Books：Applied；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-24583:end -->

### [2605.24597 Learning to Reason Efficiently with A* Post-Training](https://arxiv.org/html/2605.24597v1)

<!-- review:SF-2026-ARXIV-2605-24597:start -->
证据位置：§2 A* hypergraph formulation; §3.1 verbalized traces; §3.2 A*-informed process rewards；§4.1–§4.3 SFT and RL experiments; Appendices B–C；§6 Conclusion; Appendix A cost-function boundary; no dedicated limitations section。
<!-- claim:SF-2026-ARXIV-2605-24597:start -->We frame natural language inference as a search problem where the final answer is the valid proof itself, requiring a reasoning procedure in which intermediate inferences are correct.<!-- claim:SF-2026-ARXIV-2605-24597:end -->
证据边界、trade-off、failure 与 fallback：`Learning to Reason Efficiently with A* Post-Training` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。
Books：No Change — Existing Coverage；owner=TRAIN-RLHF。
<!-- review:SF-2026-ARXIV-2605-24597:end -->

### [2605.24598 Hera: Learning Long-Horizon Coordination for Device-Cloud Collaborative LLM Agents](https://arxiv.org/html/2605.24598v1)

<!-- review:SF-2026-ARXIV-2605-24598:start -->
证据位置：§5 Hera step-level device-cloud coordinator；§6 Experiment; §6.2–§6.4；Appendix E Limitations and Future Work。
<!-- claim:SF-2026-ARXIV-2605-24598:start -->To address this issue, we present Hera, a step-level device--cloud LLM agent coordinator for long-horizon tasks achieving a strong performance--cost Pareto frontier.<!-- claim:SF-2026-ARXIV-2605-24598:end -->
证据边界、trade-off、failure 与 fallback：`Hera: Learning Long-Horizon Coordination for Device-Cloud Collaborative LLM Agents` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：Applied；owner=AGENT-MULTI-AGENT。
<!-- review:SF-2026-ARXIV-2605-24598:end -->

### [2605.24602 Correcting Visual Blur Induced by Attention Distraction to Reduce Hallucinations: Algorithm and Theory](https://arxiv.org/html/2605.24602v1)

<!-- review:SF-2026-ARXIV-2605-24602:start -->
证据位置：§3.2 spatial inconsistency; §3.3 temporal fading; §4.1–§4.2 correction mechanisms；§6.1–§6.3 comparisons and sensitivity; Appendix D ablations/cases；§7 Conclusion; disclosed benchmark/head-layer scope; no dedicated limitations section。
<!-- claim:SF-2026-ARXIV-2605-24602:start -->In this work, we reveal that hallucinations are strongly associated with a human-like attention distraction phenomenon, where humans under divided focus experience degraded visual clarity and produce inaccurate descriptions, while in models the same mechanism manifests as spatial inconsistency in multi-head attention and temporal fading of attention to image tokens during decoding.<!-- claim:SF-2026-ARXIV-2605-24602:end -->
证据边界、trade-off、failure 与 fallback：`Correcting Visual Blur Induced by Attention Distraction to Reduce Hallucinations: Algorithm and Theory` 只支持 exact-v1 披露的数据、backbone 与任务；感知质量不等于 physical/action fidelity。新增控制换来训练与评估成本，跨场景漂移时回退专用模型、真实状态 probe 或人工 gate。
Books：No Change — Existing Coverage；owner=MULTIMODAL-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-24602:end -->

### [2605.24613 Guarded Repair for Harm-Aware Post-hoc Replacement of LLM Mathematical Reasoning](https://arxiv.org/html/2605.24613v1)

<!-- review:SF-2026-ARXIV-2605-24613:start -->
证据位置：§3.1 formulation; §3.2 diagnostics/trigger; §3.3 guarded best-of-N repair；§5.1–§5.4 results/ablations/portability; §6 candidate-flow and cost analysis；§7 Limitations and Threats to Validity。
<!-- claim:SF-2026-ARXIV-2605-24613:start -->We present GuardedRepair, a guarded best-of-N repair framework that diagnoses cached reasoning traces, selectively triggers repair, and accepts answer-changing candidates only when deterministic verification guards support replacement.<!-- claim:SF-2026-ARXIV-2605-24613:end -->
证据边界、trade-off、failure 与 fallback：`Guarded Repair for Harm-Aware Post-hoc Replacement of LLM Mathematical Reasoning` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-24613:end -->

### [2605.24614 Measuring the Depth of LLM Unlearning via Activation Patching](https://arxiv.org/html/2605.24614v1)

<!-- review:SF-2026-ARXIV-2605-24614:start -->
证据位置：§3 Unlearning Depth Score and activation patching；§4 Meta-Evaluation; §5 case studies；Limitations after §7 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-24614:start -->To address these limitations, we propose the Unlearning Depth Score (UDS), a metric that quantifies the mechanistic depth of unlearning via activation patching.<!-- claim:SF-2026-ARXIV-2605-24614:end -->
证据边界、trade-off、failure 与 fallback：`Measuring the Depth of LLM Unlearning via Activation Patching` 只覆盖披露的 threat model、模型和攻击预算，不证明一般安全。新增 detector/defense 会引入误拒与适应性绕过；证据不足时回退隔离、最小权限、规则验证与人工处置。
Books：No Change — Existing Coverage；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-24614:end -->

### [2605.24618 FC-TTS: Style and Timbre Control in Zero-Shot Text-to-Speech with Disentangled Speech Representations](https://arxiv.org/html/2605.24618v1)

<!-- review:SF-2026-ARXIV-2605-24618:start -->
证据位置：§3.1 factorized codec/flow matching; §3.2.1–§3.2.3 hierarchical generation, style encoding and consistency loss；§4.2.1–§4.2.4 zero-shot/control/ablation results; Appendix D；§6 Limitations; §7 Ethical Considerations。
<!-- claim:SF-2026-ARXIV-2605-24618:start -->In this paper, we present FC-TTS, a zero-shot TTS framework that enables disentangled control of style and timbre by conditioning on two distinct reference utterances.<!-- claim:SF-2026-ARXIV-2605-24618:end -->
证据边界、trade-off、failure 与 fallback：`FC-TTS: Style and Timbre Control in Zero-Shot Text-to-Speech with Disentangled Speech Representations` 只支持 exact-v1 披露的数据、backbone 与任务；感知质量不等于 physical/action fidelity。新增控制换来训练与评估成本，跨场景漂移时回退专用模型、真实状态 probe 或人工 gate。
Books：No Change — Existing Coverage；owner=MULTIMODAL-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-24618:end -->

### [2605.24619 Synthesizing Inductive Invariants for Distributed Protocols via IC3 and Large Language Models](https://arxiv.org/html/2605.24619v1)

<!-- review:SF-2026-ARXIV-2605-24619:start -->
证据位置：§4 Design; §5 Implementation；§6 Evaluation；§7.2 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24619:start -->We present IC3Syn, a neuro-symbolic framework that synthesizes inductive invariants by executing an IC3-style process over TLA+ states with the assistance of Large Language Models (LLMs).<!-- claim:SF-2026-ARXIV-2605-24619:end -->
证据边界、trade-off、failure 与 fallback：`Synthesizing Inductive Invariants for Distributed Protocols via IC3 and Large Language Models` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：No Change — Existing Coverage；owner=AGENT-TOOL-CALLING。
<!-- review:SF-2026-ARXIV-2605-24619:end -->

### [2605.24624 Vision-Language Binding in In-Context Image Generation](https://arxiv.org/html/2605.24624v1)

<!-- review:SF-2026-ARXIV-2605-24624:start -->
证据位置：§3 Methods; §4.2 text-token content; §4.3 causal knockout/patching；§4.1–§4.4 editing tasks, interventions and binding location; Appendices A–D；§4.5 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24624:start -->We show that an implicit cross-modal binding emerges between the text tokens and the reference image: the text tokens absorb visual reference content during the forward pass, and that absorbed content causally influences the generated output.<!-- claim:SF-2026-ARXIV-2605-24624:end -->
证据边界、trade-off、failure 与 fallback：`Vision-Language Binding in In-Context Image Generation` 只支持 exact-v1 披露的数据、backbone 与任务；感知质量不等于 physical/action fidelity。新增控制换来训练与评估成本，跨场景漂移时回退专用模型、真实状态 probe 或人工 gate。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-24624:end -->

### [2605.24630 DexSIM: Real-time Dexterous Simulation with Unified Causal Video Diffusion](https://arxiv.org/html/2605.24630v1)

<!-- review:SF-2026-ARXIV-2605-24630:start -->
证据位置：§4.1 task formulation; §4.2 architecture; §4.3 rollout training with spatial cache；§5.1–§5.5 quantitative, qualitative and ablation results；§6 Conclusion; no dedicated limitations section。
<!-- claim:SF-2026-ARXIV-2605-24630:start -->We propose DexSIM, a dexterous simulation framework for simulating dexterous manipulation in real-time.<!-- claim:SF-2026-ARXIV-2605-24630:end -->
证据边界、trade-off、failure 与 fallback：`DexSIM: Real-time Dexterous Simulation with Unified Causal Video Diffusion` 只支持 exact-v1 披露的数据、backbone 与任务；感知质量不等于 physical/action fidelity。新增控制换来训练与评估成本，跨场景漂移时回退专用模型、真实状态 probe 或人工 gate。
Books：No Change — Existing Coverage；owner=MULTIMODAL-WORLD-MODELS。
<!-- review:SF-2026-ARXIV-2605-24630:end -->

### [2605.24642 Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models](https://arxiv.org/html/2605.24642v1)

<!-- review:SF-2026-ARXIV-2605-24642:start -->
证据位置：§3.1 VLA geometry-injection strategies; §3.2 cross-attention fusion; §4 probes；§5.1–§5.5 design-choice studies; Appendices B–E；§6 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24642:start -->Recent work explores new opportunities at the intersection of vision-language-action models (VLAs) and geometric foundation models (GFMs) for 3D reconstruction, such as VGGT.<!-- claim:SF-2026-ARXIV-2605-24642:end -->
证据边界、trade-off、failure 与 fallback：`Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models` 只支持 exact-v1 披露的数据、backbone 与任务；感知质量不等于 physical/action fidelity。新增控制换来训练与评估成本，跨场景漂移时回退专用模型、真实状态 probe 或人工 gate。
Books：No Change — Existing Coverage；owner=MULTIMODAL-EMBODIED-VLA。
<!-- review:SF-2026-ARXIV-2605-24642:end -->

### [2605.24647 Know You Before You Speak: User-State Modeling for LLM Personalization in Multi-Turn Conversation](https://arxiv.org/html/2605.24647v1)

<!-- review:SF-2026-ARXIV-2605-24647:start -->
证据位置：§3 free-energy belief/world-model setup; §4.1–§4.4 PUMA user state and action selection；§5.2–§5.5 results, ablation and cross-dataset tests；§6 Conclusion; Appendix D simulator boundary; no dedicated limitations section。
<!-- claim:SF-2026-ARXIV-2605-24647:start -->PUMA maintains a belief over latent user state, updates an action-conditioned user world model, and selects dialogue actions by expected free energy rather than using profile/history retrieval as the whole personalization policy.<!-- claim:SF-2026-ARXIV-2605-24647:end -->
证据边界、trade-off、failure 与 fallback：`Know You Before You Speak: User-State Modeling for LLM Personalization in Multi-Turn Conversation` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：No Change — Existing Coverage；owner=AGENT-PLANNING。
<!-- review:SF-2026-ARXIV-2605-24647:end -->

### [2605.24652 AVBench: Human-Aligned and Automated Evaluation Benchmark for Audio-Video Generative Models](https://arxiv.org/html/2605.24652v1)

<!-- review:SF-2026-ARXIV-2605-24652:start -->
证据位置：§3.1 curation; §3.2 hard-negative mining; §3.3 evaluator SFT; §3.4 suite；§4.1–§4.3 model evaluation and human-alignment validation; §9；§5 Limitation。
<!-- claim:SF-2026-ARXIV-2605-24652:start -->To address these issues, we introduce AVBench, a fully automated benchmark tailored for human-centric AV generation.<!-- claim:SF-2026-ARXIV-2605-24652:end -->
证据边界、trade-off、failure 与 fallback：`AVBench: Human-Aligned and Automated Evaluation Benchmark for Audio-Video Generative Models` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-24652:end -->

### [2605.24657 Beyond Inference-Only Deployment: Comparing Weight-Based Consolidation Against Cascading Compaction](https://arxiv.org/html/2605.24657v1)

<!-- review:SF-2026-ARXIV-2605-24657:start -->
证据位置：§2 Method; memory taxonomy and consolidation/compaction pipelines；§3 Evaluation；§4 Discussion — Limitations。
<!-- claim:SF-2026-ARXIV-2605-24657:start -->Major LLM platforms deploy models in an inference-only configuration: the model serves requests but never updates per-user weights.<!-- claim:SF-2026-ARXIV-2605-24657:end -->
证据边界、trade-off、failure 与 fallback：`Beyond Inference-Only Deployment: Comparing Weight-Based Consolidation Against Cascading Compaction` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：Report Only；owner=AGENT-MEMORY。
<!-- review:SF-2026-ARXIV-2605-24657:end -->

### [2605.24659 IterInject: Indirect Prompt Injection Against LLM Agents via Feedback-Guided Iterative Optimization](https://arxiv.org/html/2605.24659v1)

<!-- review:SF-2026-ARXIV-2605-24659:start -->
证据位置：§3 Threat Model; §4 feedback-guided payload optimization；§5 Experimental Setup; §6 Evaluation；Limitations after §7 Conclusion; tested agents/channels only。
<!-- claim:SF-2026-ARXIV-2605-24659:start -->We introduce \oursys, a feedback-guided iterative framework that closes the loop between injection, diagnosis, and refinement: a rule-based diagnoser produces structured outcome labels with behavioral descriptions, and an LLM-based optimizer refines payloads conditioned on the full optimization history.<!-- claim:SF-2026-ARXIV-2605-24659:end -->
证据边界、trade-off、failure 与 fallback：`IterInject: Indirect Prompt Injection Against LLM Agents via Feedback-Guided Iterative Optimization` 只覆盖披露的 threat model、模型和攻击预算，不证明一般安全。新增 detector/defense 会引入误拒与适应性绕过；证据不足时回退隔离、最小权限、规则验证与人工处置。
Books：No Change — Existing Coverage；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-24659:end -->

### [2605.24660 How Many Tools Should an LLM Agent See? A Chance-Corrected Answer](https://arxiv.org/html/2605.24660v1)

<!-- review:SF-2026-ARXIV-2605-24660:start -->
证据位置：§3 Bits-over-Random and MDP exposure policy；§4 Empirical Evaluation；§5.3 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24660:start -->Bits-over-Random chance-corrects tool-shortlist coverage at each depth, making tool count an evaluated control and enabling per-query depth policies without an arbitrary depth penalty.<!-- claim:SF-2026-ARXIV-2605-24660:end -->
证据边界、trade-off、failure 与 fallback：`How Many Tools Should an LLM Agent See? A Chance-Corrected Answer` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：Applied；owner=AGENT-TOOL-CALLING。
<!-- review:SF-2026-ARXIV-2605-24660:end -->

### [2605.24661 Measuring Reasoning Quality in LLMs: A Multi-Dimensional Behavioral Framework](https://arxiv.org/html/2605.24661v1)

<!-- review:SF-2026-ARXIV-2605-24661:start -->
证据位置：§4 multi-dimensional behavioral framework and aggregation；§5 Results；§6.2 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24661:start -->Reasoning evaluation separates correctness, consistency, robustness, local logical coherence, efficiency and stability, and deployment-aware aggregation can invert rankings hidden by final-answer accuracy.<!-- claim:SF-2026-ARXIV-2605-24661:end -->
证据边界、trade-off、failure 与 fallback：`Measuring Reasoning Quality in LLMs: A Multi-Dimensional Behavioral Framework` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-24661:end -->

### [2605.24662 OpenTwin: Closed-Loop Digital Twins for Trustworthy Policy Deployment in Open RAN](https://arxiv.org/html/2605.24662v1)

<!-- review:SF-2026-ARXIV-2605-24662:start -->
证据位置：§II–§IV OpenTwin closed-loop data assimilation, calibration and policy-validation workflow；§A Experimental Setup; §B Experimental Results；§V Limitations; real-network drift and Open-RAN testbed boundary。
<!-- claim:SF-2026-ARXIV-2605-24662:start -->A deployment-calibrated digital twin re-synchronizes from streamed measurements and admits a proposed control action only when a conformal fidelity gate places its predicted outcome inside an operator-defined safe region.<!-- claim:SF-2026-ARXIV-2605-24662:end -->
证据边界、trade-off、failure 与 fallback：`OpenTwin: Closed-Loop Digital Twins for Trustworthy Policy Deployment in Open RAN` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-24662:end -->

### [2605.24667 When Mean CE Fails: Median CE Can Better Track Language Model Quality](https://arxiv.org/html/2605.24667v1)

<!-- review:SF-2026-ARXIV-2605-24667:start -->
证据位置：§§3–4 mean/median CE interventions and top-K self-distillation；§3.2; §§4.2–4.4; Appendix C protocol；§5 Discussion — Limitations。
<!-- claim:SF-2026-ARXIV-2605-24667:start -->First, in Qwen2.5-1.5B SFT on synthetic fact-learning, we find that mean CE rises substantially after the initial learning phase while held-out fact-recall accuracy remains near its peak.<!-- claim:SF-2026-ARXIV-2605-24667:end -->
证据边界、trade-off、failure 与 fallback：`When Mean CE Fails: Median CE Can Better Track Language Model Quality` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。
Books：Applied；owner=TRAIN-PRETRAINING。
<!-- review:SF-2026-ARXIV-2605-24667:end -->

### [2605.24674 Reasoning to Align: Implicit Reasoning in Diffusion Transformers for Video Editing](https://arxiv.org/html/2605.24674v1)

<!-- review:SF-2026-ARXIV-2605-24674:start -->
证据位置：§3 problem statement; §4.2 routed token conditioning; §4.3 reference-anchored attention；§5.1–§5.3 main, ablation and method analysis; Appendix D；§6 Conclusion; no dedicated limitations section。
<!-- claim:SF-2026-ARXIV-2605-24674:start -->Granularity-routed conditioning separates shallow edit-intent tokens from deeper native visual/text evidence, while a training-only reference branch aligns attention without adding the same branch at inference.<!-- claim:SF-2026-ARXIV-2605-24674:end -->
证据边界、trade-off、failure 与 fallback：`Reasoning to Align: Implicit Reasoning in Diffusion Transformers for Video Editing` 只支持 exact-v1 披露的数据、backbone 与任务；感知质量不等于 physical/action fidelity。新增控制换来训练与评估成本，跨场景漂移时回退专用模型、真实状态 probe 或人工 gate。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-24674:end -->

### [2605.24683 B.O.D.Y.: Beyond-Overlay Deterministic topologY -- A Layer-2 Declarative Ground Truth for AIOps Pipelines under Fragmented Administrative Boundaries](https://arxiv.org/html/2605.24683v1)

<!-- review:SF-2026-ARXIV-2605-24683:start -->
证据位置：§III deterministic L2 topology, identity loop and HIL protocol；§IV Implementation and Results；§V Limitations and Constraints。
<!-- claim:SF-2026-ARXIV-2605-24683:start -->A deterministic Layer-2 topology and asset-identity substrate gives probabilistic AIOps reasoning an auditable physical ground truth when administrative boundaries make ordinary discovery incomplete.<!-- claim:SF-2026-ARXIV-2605-24683:end -->
证据边界、trade-off、failure 与 fallback：`B.O.D.Y.: Beyond-Overlay Deterministic topologY -- A Layer-2 Declarative Ground Truth for AIOps Pipelines under Fragmented Administrative Boundaries` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。
Books：Applied；owner=PLATFORM-MONITORING。
<!-- review:SF-2026-ARXIV-2605-24683:end -->

### [2605.24687 HoloFair: Unified T2I Fairness Evaluation and Fair-GRPO Debiasing](https://arxiv.org/html/2605.24687v1)

<!-- review:SF-2026-ARXIV-2605-24687:start -->
证据位置：§3.1 taxonomy/data; §3.2 classifier; §3.3 metric; §3.4 Fair-GRPO；§4.3–§4.4 benchmark/debiasing, ablation and reward-hacking analysis；Appendix A Limitations and Future Work。
<!-- claim:SF-2026-ARXIV-2605-24687:start -->Multi-attribute group fairness is measured jointly and optimized with a multi-objective Fair-GRPO reward, whose disclosed reward-hacking behavior remains part of the evidence boundary.<!-- claim:SF-2026-ARXIV-2605-24687:end -->
证据边界、trade-off、failure 与 fallback：`HoloFair: Unified T2I Fairness Evaluation and Fair-GRPO Debiasing` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-24687:end -->

### [2605.24693 CP-Agent: A Calibrated Risk-Controlled Agent for Feedback-Driven Competitive Programming](https://arxiv.org/html/2605.24693v1)

<!-- review:SF-2026-ARXIV-2605-24693:start -->
证据位置：§2 calibrated feedback-control theory; §3.1–§3.4 verification, augmentation, experience and tools；§4.2 calibration/auditability; §4.3–§4.7 results and ablations; Appendix D；§6 Conclusion plus Appendix C structural conditions; no dedicated limitations section。
<!-- claim:SF-2026-ARXIV-2605-24693:start -->Large language models still struggle with contest-level programming, while many agentic remedies rely on massive inference-time sampling or expensive multi-stage post-training.<!-- claim:SF-2026-ARXIV-2605-24693:end -->
证据边界、trade-off、failure 与 fallback：`CP-Agent: A Calibrated Risk-Controlled Agent for Feedback-Driven Competitive Programming` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：No Change — Existing Coverage；owner=AGENT-PLANNING。
<!-- review:SF-2026-ARXIV-2605-24693:end -->

### [2605.24696 CALIBURN: Operationally Calibrated Streaming Intrusion Detection with Regime-Dependent Conformal Risk Control](https://arxiv.org/html/2605.24696v1)

<!-- review:SF-2026-ARXIV-2605-24696:start -->
证据位置：§3.2 change-point detector; §3.3 SLO threshold; §3.4 calibration/CRC; §3.5 burn-rate；§5.1–§5.6 three prevalence regimes, calibration and ablation；§6.1–§6.4 operating regimes and threats to validity。
<!-- claim:SF-2026-ARXIV-2605-24696:start -->把 streaming alert threshold 从离线调参改成由 operator cost、alert budget 与 SLO 共同派生的 versioned control，并把 calibration、CRC 与 multi-window burn-rate 串成一条验收链。收益受 prevalence/exchangeability 强约束；CRC overshoot、density degeneracy 或 base-rate inversion 触发时回退静态保守阈值、隔离与人工调查。<!-- claim:SF-2026-ARXIV-2605-24696:end -->
证据边界、trade-off、failure 与 fallback：`CALIBURN: Operationally Calibrated Streaming Intrusion Detection with Regime-Dependent Conformal Risk Control` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。
Books：Applied；owner=PLATFORM-MONITORING。
<!-- review:SF-2026-ARXIV-2605-24696:end -->

### [2605.24697 The Path Matters: Learning a Token-Commitment Policy for Diffusion Language Models](https://arxiv.org/html/2605.24697v1)

<!-- review:SF-2026-ARXIV-2605-24697:start -->
证据位置：§3 future-stability labels, learned commitment and TraceLock deployment；§4 Experiments; §§4.2–4.4；§5 Conclusion; frozen generator/tested diffusion backbones boundary。
<!-- claim:SF-2026-ARXIV-2605-24697:start -->We argue that token commitment can instead be learned as a reusable trace-state policy.<!-- claim:SF-2026-ARXIV-2605-24697:end -->
证据边界、trade-off、failure 与 fallback：`The Path Matters: Learning a Token-Commitment Policy for Diffusion Language Models` 只支持 exact-v1 披露的数据、backbone 与任务；感知质量不等于 physical/action fidelity。新增控制换来训练与评估成本，跨场景漂移时回退专用模型、真实状态 probe 或人工 gate。
Books：Applied；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-24697:end -->

### [2605.24702 Do Image-Text Metrics Respect Semantic Invariances?](https://arxiv.org/html/2605.24702v1)

<!-- review:SF-2026-ARXIV-2605-24702:start -->
证据位置：§3.1–§3.5 curation, perturbations, protocol, RRF and calibrated scoring；§5.1–§5.6 invariance and ranking-flip results; Appendices A.6–A.12/B；§7 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24702:start -->We present an invariance probe on five popular evaluators (CLIPScore, PAC-S, UMIC, FLEUR, and a deterministic LLM judge) under semantics-preserving perturbations along three axes -- spatial (flips, context-preserving repositioning, light rotations), object (scale, category), and socio-linguistic framing (cultural/economic adjectives with neutral and length-matched controls).<!-- claim:SF-2026-ARXIV-2605-24702:end -->
证据边界、trade-off、failure 与 fallback：`Do Image-Text Metrics Respect Semantic Invariances?` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-24702:end -->

### [2605.24709 Streaming Reinforcement Learning under Partial Observability with Real-Time Recurrent Learning](https://arxiv.org/html/2605.24709v1)

<!-- review:SF-2026-ARXIV-2605-24709:start -->
证据位置：§3 Methodology; streaming partially-observed recurrent policy with exact RTRL；§4 Experiments；§6 Discussion and Limitations。
<!-- claim:SF-2026-ARXIV-2605-24709:start -->Streaming reinforcement learning has emerged as an online learning paradigm that conforms to the restrictions of natural learning agents that process data incrementally, i.e. with a batch size of 1 and no replay buffer.<!-- claim:SF-2026-ARXIV-2605-24709:end -->
证据边界、trade-off、failure 与 fallback：`Streaming Reinforcement Learning under Partial Observability with Real-Time Recurrent Learning` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。
Books：Applied；owner=TRAIN-RLHF。
<!-- review:SF-2026-ARXIV-2605-24709:end -->

### [2605.24718 The Tokenizer Tax Across 25 European Languages: Domain Invariance, Cross-Lingual Few-Shot Effects, and the Ukrainian Penalty](https://arxiv.org/html/2605.24718v1)

<!-- review:SF-2026-ARXIV-2605-24718:start -->
证据位置：§3 tokenizer/dataset/protocol；§4 cross-domain/cross-lingual experiments；§6 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24718:start -->把 tokenizer fertility 作为 language×domain 的成本与可达性 contract，而不是只看平均 tokens；扩 vocab/continued pretraining 会增加兼容、checkpoint 与序列成本，失败时保留旧 tokenizer 并按语言路由或预算。<!-- claim:SF-2026-ARXIV-2605-24718:end -->
证据边界、trade-off、failure 与 fallback：`The Tokenizer Tax Across 25 European Languages: Domain Invariance, Cross-Lingual Few-Shot Effects, and the Ukrainian Penalty` 只在披露规模、数据与架构上成立。新增 representation/token-mixing 假设换取效率或可控性但可能损失 recall/兼容性；回归失败时回退标准 tokenizer/attention/layer。
Books：Applied；owner=MODEL-TOKENIZER。
<!-- review:SF-2026-ARXIV-2605-24718:end -->

### [2605.24727 Fundamental Limitation in Explaining AI](https://arxiv.org/html/2605.24727v1)

<!-- review:SF-2026-ARXIV-2605-24727:start -->
证据位置：§3 four explanation conditions; §4 quadrilemma theorem/implications；formal construction and implications in §4；§5 Conclusion, limitations and future work。
<!-- claim:SF-2026-ARXIV-2605-24727:start -->Environment complexity, model performance, explanation interpretability and complete faithfulness cannot all hold simultaneously; governance must treat an explanation as an incomplete sensor rather than a complete behavioral account.<!-- claim:SF-2026-ARXIV-2605-24727:end -->
证据边界、trade-off、failure 与 fallback：`Fundamental Limitation in Explaining AI` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。
Books：Applied；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-24727:end -->

### [2605.24728 Hylos: Operability Contracts for Model-Native Spatial Intelligence](https://arxiv.org/html/2605.24728v1)

<!-- review:SF-2026-ARXIV-2605-24728:start -->
证据位置：§4 operability state/graph, spatial transactions and effect diffs; §5 agency gates；§6 repair stress test; §7 qualitative result；§1.2 Scope of Claims; prototype/trajectory does not establish general runtime validity。
<!-- claim:SF-2026-ARXIV-2605-24728:start -->Foundation models can increasingly describe, reconstruct, and generate 3D objects, assemblies, scenes, and environments, but visually plausible spatial output is not yet operable 3D.<!-- claim:SF-2026-ARXIV-2605-24728:end -->
证据边界、trade-off、failure 与 fallback：`Hylos: Operability Contracts for Model-Native Spatial Intelligence` 提供受限机制线索，但当前没有唯一稳定 owner 或足够外部验证；不把原型结果升级为通用系统保证，失败时保持现有架构并在季度结构复核中重开。
Books：Structural Candidate；owner=无唯一 owner。
<!-- review:SF-2026-ARXIV-2605-24728:end -->

### [2605.24733 StepGap: A Hybrid NLI-LLM Checker for Step-Level Evidence-Gap Detectionin Multi-Hop Question Answering](https://arxiv.org/html/2605.24733v1)

<!-- review:SF-2026-ARXIV-2605-24733:start -->
证据位置：§3 formulation; §4 hybrid checker; §5 typed process reward；§6 checker evaluation; §7 GRPO training；Limitations after §8 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-24733:start -->We present \textbf{StepGap}, a hybrid NLI-LLM decision tree that detects step-level evidence gaps in multi-hop QA and emits one of three typed labels: \textsc{Contradicted Claim} (CC), \textsc{Irrelevant Evidence} (IE), or \textsc{Missing Bridge} (MB), each tied to a concrete repair action.<!-- claim:SF-2026-ARXIV-2605-24733:end -->
证据边界、trade-off、failure 与 fallback：`StepGap: A Hybrid NLI-LLM Checker for Step-Level Evidence-Gap Detectionin Multi-Hop Question Answering` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-24733:end -->

### [2605.24737 Who judges the judges? Governance from metrics: a runtime framework for continuous LLM compliance monitoring](https://arxiv.org/html/2605.24737v1)

<!-- review:SF-2026-ARXIV-2605-24737:start -->
证据位置：§3 governance-from-metrics; §4 govllm architecture；§6 preliminary experiments；§6.3 and §7.4 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24737:start -->把 compliance 从一次性 audit 改成 versioned runtime signal，并将 judge disagreement 作为人工仲裁触发而非 truth；judge bias/drift 会污染路由，故保留静态审核、规则检查与人工 override。<!-- claim:SF-2026-ARXIV-2605-24737:end -->
证据边界、trade-off、failure 与 fallback：`Who judges the judges? Governance from metrics: a runtime framework for continuous LLM compliance monitoring` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。
Books：Applied；owner=PLATFORM-MONITORING。
<!-- review:SF-2026-ARXIV-2605-24737:end -->

### [2605.24743 Bilevel Optimization of Synthetic Trajectories for Multi-Turn LLM Fine-Tuning](https://arxiv.org/html/2605.24743v1)

<!-- review:SF-2026-ARXIV-2605-24743:start -->
证据位置：§3 bilevel synthetic-trajectory weighting; §4 theory；§§5–6 experiments and learned-weight analysis；§7 Conclusion; three tasks and synthetic-generator boundary。
<!-- claim:SF-2026-ARXIV-2605-24743:start -->We propose BOOST, a bilevel optimization framework where the inner level trains the LLM on reweighted data and the outer level trains a lightweight reweighting head on held-out real validation tasks, assigning continuous trajectory-level weights without requiring an external judge.<!-- claim:SF-2026-ARXIV-2605-24743:end -->
证据边界、trade-off、failure 与 fallback：`Bilevel Optimization of Synthetic Trajectories for Multi-Turn LLM Fine-Tuning` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。
Books：Applied；owner=TRAIN-DATA。
<!-- review:SF-2026-ARXIV-2605-24743:end -->

### [2605.24749 How Neural Reward Models Learn Features for Policy Optimization: A Single-Index Analysis](https://arxiv.org/html/2605.24749v1)

<!-- review:SF-2026-ARXIV-2605-24749:start -->
证据位置：§§3–5 reward-weighted feature recovery and tilted-policy value gap；theory and deployment-temperature analysis in §§4–5；§6 Conclusion and Discussion; single-index/theoretical-assumption boundary。
<!-- claim:SF-2026-ARXIV-2605-24749:start -->Reward modeling is not only a prediction problem: in KL-regularized policy optimization, the learned reward is exponentiated to define the deployed policy, so downstream value depends on errors in reward-tilted regions.<!-- claim:SF-2026-ARXIV-2605-24749:end -->
证据边界、trade-off、failure 与 fallback：`How Neural Reward Models Learn Features for Policy Optimization: A Single-Index Analysis` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。
Books：Applied；owner=TRAIN-RLHF。
<!-- review:SF-2026-ARXIV-2605-24749:end -->

### [2605.24754 Motion-Compensated Weight Compression](https://arxiv.org/html/2605.24754v1)

<!-- review:SF-2026-ARXIV-2605-24754:start -->
证据位置：§3 setup; §4 functional alignment; §5 predictive coding; §6 residual quantization/rate-distortion；§7.1 main results; Appendices H–L robustness, latency and ablation；Appendix M restricted-symmetry scope; Appendix O.2 Limitations。
<!-- claim:SF-2026-ARXIV-2605-24754:start -->We propose Motion-Compensated Weight Compression (MCWC), a weight-only codec that aligns permutation-symmetric blocks (e.g., hidden units and attention heads) to maximize cross-layer correspondence, turning depth into a predictable sequence.<!-- claim:SF-2026-ARXIV-2605-24754:end -->
证据边界、trade-off、failure 与 fallback：`Motion-Compensated Weight Compression` 的收益受模型、硬件、精度、长度、batch/concurrency 与 SLO 限制。新增压缩/路由状态会产生误差和管理成本；质量或 tail-latency gate 失败时回退 dense/full-precision/原生 decode。
Books：No Change — Existing Coverage；owner=INFER-GPU-MEMORY。
<!-- review:SF-2026-ARXIV-2605-24754:end -->

### [2605.24756 Proper Scoring Rules for Agentic Uncertainty Quantification](https://arxiv.org/html/2605.24756v1)

<!-- review:SF-2026-ARXIV-2605-24756:start -->
证据位置：§4 proper trajectory scores under complete and censored observation；§5 metrics; §6 Experiments；§7 Conclusion and Limitations。
<!-- claim:SF-2026-ARXIV-2605-24756:start -->Building on prequential proper scoring, we introduce the Trajectory Proper Score (TPS), a predictor-agnostic family of strictly proper trajectory-level scoring rules for any per-step uncertainty signal calibrated into a probability of eventual success.<!-- claim:SF-2026-ARXIV-2605-24756:end -->
证据边界、trade-off、failure 与 fallback：`Proper Scoring Rules for Agentic Uncertainty Quantification` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。
Books：Applied；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-24756:end -->

### [2605.24759 A Contractive Feedback Semantics for Reinforcement Learning](https://arxiv.org/html/2605.24759v1)

<!-- review:SF-2026-ARXIV-2605-24759:start -->
证据位置：§4 traced Bellman semantics; §5 compositionality; §6 abstraction; §7 quantale contracts；§10 minimal modular-robustness examples; Appendix A proofs；§9 Scope and Limitations。
<!-- claim:SF-2026-ARXIV-2605-24759:start -->Discounted policy evaluation can be expressed as guarded contractive feedback over typed open decision components, allowing local approximation and safety/resource contracts to lift through admitted wiring contexts rather than assuming every RL morphism has a global trace.<!-- claim:SF-2026-ARXIV-2605-24759:end -->
证据边界、trade-off、failure 与 fallback：`A Contractive Feedback Semantics for Reinforcement Learning` 提供受限机制线索，但当前没有唯一稳定 owner 或足够外部验证；不把原型结果升级为通用系统保证，失败时保持现有架构并在季度结构复核中重开。
Books：Structural Candidate；owner=无唯一 owner。
<!-- review:SF-2026-ARXIV-2605-24759:end -->

### [2605.24761 Drift-Resistant Navigation World Model with Anchored Epipolar Guidance](https://arxiv.org/html/2605.24761v1)

<!-- review:SF-2026-ARXIV-2605-24761:start -->
证据位置：§3.2 anchor-guided rollout; §3.3 epipolar masking; §3.4 anchor-conditioned DiT; §3.5 training；§4.2 drift, §4.3 planning and §4.4 ablations; Appendices C–E；§5 Conclusion; geometric assumptions in Appendices A–B; no dedicated limitations section。
<!-- claim:SF-2026-ARXIV-2605-24761:start -->We propose Drift-Resistant Navigation World Model, a generative model that mitigates both perceptual drift and geometric drift in conventional rollout-based navigation world models.<!-- claim:SF-2026-ARXIV-2605-24761:end -->
证据边界、trade-off、failure 与 fallback：`Drift-Resistant Navigation World Model with Anchored Epipolar Guidance` 只支持 exact-v1 披露的数据、backbone 与任务；感知质量不等于 physical/action fidelity。新增控制换来训练与评估成本，跨场景漂移时回退专用模型、真实状态 probe 或人工 gate。
Books：No Change — Existing Coverage；owner=MULTIMODAL-WORLD-MODELS。
<!-- review:SF-2026-ARXIV-2605-24761:end -->

### [2605.24764 Spectral Retrieval: Multi-Scale Sinc Convolution over Token Embeddings for Localized Retrieval in LLM Multi-Agent Systems](https://arxiv.org/html/2605.24764v1)

<!-- review:SF-2026-ARXIV-2605-24764:start -->
证据位置：§III-B–§III-H sinc kernel, score, recovery, two-stage retrieval and production notes；§VI synthetic and §VII LIMIT-small evaluation；§VIII Limitations and Threats; §V-C what it does not solve。
<!-- claim:SF-2026-ARXIV-2605-24764:start -->Multi-scale sinc convolution over token embeddings interpolates between per-token MaxSim and mean pooling for localized retrieval, but its disclosed evidence is synthetic plus LIMIT-small and leaves production latency/calibration open.<!-- claim:SF-2026-ARXIV-2605-24764:end -->
证据边界、trade-off、failure 与 fallback：`Spectral Retrieval: Multi-Scale Sinc Convolution over Token Embeddings for Localized Retrieval in LLM Multi-Agent Systems` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：No Change — Existing Coverage；owner=AGENT-RAG。
<!-- review:SF-2026-ARXIV-2605-24764:end -->

### [2605.24770 Muon in Vision Transformers: Optimizer-Recipe Interactions and Gradient Spectra](https://arxiv.org/html/2605.24770v1)

<!-- review:SF-2026-ARXIV-2605-24770:start -->
证据位置：§§2–5 Muon geometry and recipe interaction；§§3–6; Appendices C–E；§7 Conclusions and limitations。
<!-- claim:SF-2026-ARXIV-2605-24770:start -->Muon is a recently developed matrix-aware optimizer that has shown strong results in transformer training, but its behavior in vision transformers (ViTs) is not yet well understood.<!-- claim:SF-2026-ARXIV-2605-24770:end -->
证据边界、trade-off、failure 与 fallback：`Muon in Vision Transformers: Optimizer-Recipe Interactions and Gradient Spectra` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。
Books：Applied；owner=TRAIN-PRETRAINING。
<!-- review:SF-2026-ARXIV-2605-24770:end -->

### [2605.24775 PRIMA: Operational Patterns for Resilient Multi-Agent Research with Verifiable Identity and Convergent Feedback](https://arxiv.org/html/2605.24775v1)

<!-- review:SF-2026-ARXIV-2605-24775:start -->
证据位置：§III identity; §§IV–VIII protocol, scoring, orchestration and persistence；reported operational examples and convergence traces in §§VI–VIII；§I/§II claim scope; pattern/prototype rather than general production proof。
<!-- claim:SF-2026-ARXIV-2605-24775:start -->Long-running multi-agent work needs a typed pause/resume record, structural operating rules and an explicit cross-document harmonization phase so rate limits or process restarts do not force converged work to be replayed.<!-- claim:SF-2026-ARXIV-2605-24775:end -->
证据边界、trade-off、failure 与 fallback：`PRIMA: Operational Patterns for Resilient Multi-Agent Research with Verifiable Identity and Convergent Feedback` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：No Change — Existing Coverage；owner=AGENT-PLATFORM。
<!-- review:SF-2026-ARXIV-2605-24775:end -->

### [2605.24779 Complement Submodular Information Measures for Balanced and Robust Data Selection](https://arxiv.org/html/2605.24779v1)

<!-- review:SF-2026-ARXIV-2605-24779:start -->
证据位置：§3 CSI definition/properties; §4 instantiations; §5 optimization；§6.1 synthetic and §6.2 hidden-slice subset selection；§7 Conclusion; synthetic/hidden-slice boundary; no dedicated limitations section。
<!-- claim:SF-2026-ARXIV-2605-24779:start -->Complement Submodular Information scores shared structure between a selected subset and its complement, making rare-slice preservation and outlier suppression explicit in data/benchmark split selection.<!-- claim:SF-2026-ARXIV-2605-24779:end -->
证据边界、trade-off、failure 与 fallback：`Complement Submodular Information Measures for Balanced and Robust Data Selection` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。
Books：No Change — Existing Coverage；owner=TRAIN-DATA。
<!-- review:SF-2026-ARXIV-2605-24779:end -->

### [2605.24785 PANDO: Efficient Multimodal AI Agents via Online Skill Distillation](https://arxiv.org/html/2605.24785v1)

<!-- review:SF-2026-ARXIV-2605-24785:start -->
证据位置：§3 cost decomposition; §4 PANDO framework；§5–§6 results/ablation; Appendix I/N；§7 Limitations; Appendix K residual failures。
<!-- claim:SF-2026-ARXIV-2605-24785:start -->把 agent skill library 当作在线可升降级的 versioned state，并同时记 success、steps、tokens 与 cache reuse；错误 skill 会复用放大且在线评估可能污染，失败时 demote/blacklist 并回退无技能单次执行。<!-- claim:SF-2026-ARXIV-2605-24785:end -->
证据边界、trade-off、failure 与 fallback：`PANDO: Efficient Multimodal AI Agents via Online Skill Distillation` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。
Books：Applied；owner=AGENT-PLATFORM。
<!-- review:SF-2026-ARXIV-2605-24785:end -->

### [2605.24786 CONF-KV: Confidence-Aware KV Cache Eviction with Mixed-Precision Storage for Long-Horizon LLM](https://arxiv.org/html/2605.24786v1)

<!-- review:SF-2026-ARXIV-2605-24786:start -->
证据位置：§3 confidence-aware mixed-precision cache manager；§§4–6 setup, results and ablations；§7 failure modes; §8 Limitations and conclusion。
<!-- claim:SF-2026-ARXIV-2605-24786:start -->We introduce CONF-KV, a KV-cache manager that converts the next-token distribution into a scalar confidence score and uses it to choose the per-step cache budget, retaining more context when the model is uncertain and pruning aggressively when it is confident.<!-- claim:SF-2026-ARXIV-2605-24786:end -->
证据边界、trade-off、failure 与 fallback：`CONF-KV: Confidence-Aware KV Cache Eviction with Mixed-Precision Storage for Long-Horizon LLM` 的收益受模型、硬件、精度、长度、batch/concurrency 与 SLO 限制。新增压缩/路由状态会产生误差和管理成本；质量或 tail-latency gate 失败时回退 dense/full-precision/原生 decode。
Books：No Change — Existing Coverage；owner=INFER-KV-CACHE。
<!-- review:SF-2026-ARXIV-2605-24786:end -->

### [2605.24793 Beyond the Target: From Imitation to Collaboration in Speculative Decoding](https://arxiv.org/html/2605.24793v1)

<!-- review:SF-2026-ARXIV-2605-24793:start -->
证据位置：§3 utility view, collaborative arbitration and RL training；§4 Experiments; §§4.2–4.4；§5 Conclusion and Appendix A tested-model/benchmark boundary。
<!-- claim:SF-2026-ARXIV-2605-24793:start -->Inspired by this, we introduce \textbf{Collaborative Speculative Decoding (CoSpec)}, a generalization of SPD that no longer treats the target model as the sole token-level authority.<!-- claim:SF-2026-ARXIV-2605-24793:end -->
证据边界、trade-off、failure 与 fallback：`Beyond the Target: From Imitation to Collaboration in Speculative Decoding` 的收益受模型、硬件、精度、长度、batch/concurrency 与 SLO 限制。新增压缩/路由状态会产生误差和管理成本；质量或 tail-latency gate 失败时回退 dense/full-precision/原生 decode。
Books：Applied；owner=INFER-SPECULATIVE-DECODING。
<!-- review:SF-2026-ARXIV-2605-24793:end -->

### [2605.24794 DUEL: Adversarial Self-Play for Multimodal Reasoning](https://arxiv.org/html/2605.24794v1)

<!-- review:SF-2026-ARXIV-2605-24794:start -->
证据位置：§3.1 paired claims; §3.2 calibrated verification; §3.3 paired-GRPO self-play；§5.2–§5.6 main, transfer, ablation, efficiency and sensitivity; Appendices D–G；Appendix A Limitations。
<!-- claim:SF-2026-ARXIV-2605-24794:start -->We propose a self-evolving post-training framework, DUEL, where supervision emerges from adversarial interactions between two policies initialized from the same pretrained VLM.<!-- claim:SF-2026-ARXIV-2605-24794:end -->
证据边界、trade-off、failure 与 fallback：`DUEL: Adversarial Self-Play for Multimodal Reasoning` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。
Books：No Change — Existing Coverage；owner=TRAIN-RLHF。
<!-- review:SF-2026-ARXIV-2605-24794:end -->


### 补充自然日新增证据（原§4以上部分连续保留）

补充38家族均实际读完整题摘/官方核心、必要方法/对照与直接反侧，独立Source已通过；30项具体Books缺口进一步深入并实际写入，8项NC指出承载语义，所有实际改动均由指定非writer一次POST通过。以下“未核artifact/复现”适用于全部新增项，不将论文审阅写成实验复现或生产验收。精确Source/PRE/POST分批依据见[本日作者](../_sources/daily-20260526/SUP_SOURCES_20261021.md)与[独立reader](../_sources/daily-20260526/SUP_REVIEW_20261021.md)。

日期共同依据：37篇唯一exact-v1提交均在May21 18:00UTC～May22 18:00UTC之间；适用的[arXiv公告/发号规则](https://info.arxiv.org/help/availability.html)在EDT下给最早May25 08:00BJT，逐精确DOI的arxiv.content/findable registered最晚界也全在May25，整个可能区间同日才列2026-05-25。registered不是实际发布时间，created不作替代；逐原字段保留在[两页DataCite原件](../_sources/daily-20260526/SUP_dc_may25_20261021.raw.json)与[尾页](../_sources/daily-20260526/SUP_dc_may25_tail_20261021.raw.json)、exact-v1题摘及作者A4–A12。该联合约束不授全球首发保证；已有更早原文/撤回/实质修订线索另处理。Containment取官方May25日期。

### [Anthropic How we contain Claude across products](https://www.anthropic.com/research/how-we-contain-claude)

采用精确官方正文，必要证据：官方正文L108–136/170–181；事故与修复L123–127。批准api域名后，攻击者自有APIkey可通过FilesAPI外传；修复只转发该VM预配sessiontoken并拦server-fetch headers。Agentloop/localMCP已在host，不能说由VM隔离；代理在VM内，未给guest-root/全路径bypass证明，也未量化开销。只采用厂商事故披露的具体失效与修复边界，未独立复现、未采宣传攻击率。

Books：整合 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)，执行环境与可验证的安全边界开篇两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.22949 MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination](https://arxiv.org/pdf/2605.22949v1)

采用精确v1，必要证据：PDF §3/Eq3–8/Alg1、§5–7/T4–7、§10.3–11。HTML masthead August24与v1身份冲突已用exact-v1 PDF核复；仅verified binary outcomes、持续标签和non-strategic前提。对静态离线baseline的优势不证明胜过同信息在线校准，ECE不等单任务正确概率。当前per-model/per-band、delay/selection/forgetting、冷启动和反馈bias正文实际承载采用命题。

Books：已有覆盖 [INFER-SCHEDULING](../../../../books/part-05-inference-system/56-inference-scheduling.md)，Calibration是在线Routing State。仅采用上述收窄命题，指定reader实际读目标完整局部后确认语义承载，不声称覆盖论文全部超参数/排名。

### [2605.23057 ModeSwitch-LLM: A Lightweight Phase-Aware Controller for Cross-Mode LLM Inference on a Single GPU](https://arxiv.org/html/2605.23057v1)

采用精确v1，必要证据：§4–6/T1–3。A10040GB/Llama3.1-8B/vLLM的请求边界一次选择，不是请求内部phase-switch；known benchmark/workload tag是输入。CPU路由overhead非完整加载切换费，synthetic ROUGE proxy及部分量化accuracy退化近结论保留；605-row learned对照oracle-match非最终目标，不混不同平均分母。

Books：整合 [INFER-SCHEDULING](../../../../books/part-05-inference-system/56-inference-scheduling.md)，SLO-aware Admission前两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23348 XWind: A Cross-site Router for Large Language Model Inference Serving at Renewable Energy Farms](https://arxiv.org/html/2605.23348v1)

采用精确v1，必要证据：§4/Alg1–2、§5.1–5.4/T1、§7。64A10040GB/TP2/Llama3.1-8B、三emulated sites、150/175RPS及Poisson/Azure长度。Reactive只指workload telemetry；仍使用15min oracular power、线性插值与站点profile阈值，忽略WANdelay，不写无预测/无profile或真实WAN收益。

Books：整合 [PLATFORM-GPU-SCHEDULER](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)，Power Budget段01837后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.22967 Learned Relay Representations for Forward-Thinking Discrete Diffusion Models](https://arxiv.org/html/2605.22967v1)

采用精确v1，必要证据：§3/Eq2–8/Alg1、§4/T1–2、§6、A2/B。32%来自NFE88.3vs130.7，排除prefill/final-cache-update，非实测全请求latency。Teacher-forced token值与不求导的离散位置分开；仅masked relay更新保cache。K2BPTT增加训练compute/liveactivation，no-op optimizer/eager/FA2-off的profile不能认证完整训练免费。

Books：整合 [MULTIMODAL-GENERATIVE-PARADIGMS](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，masked schedule段后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23080 The Attribution Contract: Feature Attribution for Generative Language Models](https://arxiv.org/html/2605.23080v1)

采用精确v1，必要证据：§2–5/Def1/T1/Eq5–41。Method-contract specification：固定prefix仍forward但不在归因path，原生成re-score不等重新生成。只采用固定量/eligible feature/target与生成过程分责，不授因果真值、自动一致或后版MoE。既有23080 source-family复用，仅新增独有semantic-delta，防重复归属。

Books：整合 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，Attribution Contract中semantic-delta:20260526-supp-attribution-contract。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23146 Infra-Bayesian Reinforcement Learning Agents Outperform Classical RL For Worst-Case Robustness](https://arxiv.org/html/2605.23146v1)

采用精确v1，必要证据：§4–6。有限stateless extremal a-measures与known reward matrix/predictor，无在线学习；例中uniform Bayes也可同选arm2，regret仍linear。只采不确定假设集合与条件worst-case分责，不采普胜classical RL或LLM鲁棒保证。

Books：整合 [AGENT-PLANNING](../../../../books/part-07-agent/79-planning.md)，prior段后一段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23268 Coupled Training with Privileged Information and Unlabeled Data](https://arxiv.org/html/2605.23268v1)

采用精确v1，必要证据：§1.1/§2–5。需配对部署X与privileged Z，joint不等同步更新；ρstar是分析量。Squareloss/convex理论不授randomforest/logistic或非配对LLM，26seed Bank与单seed Parkinson分开。保留teacher/student两份误差、约束方向、全部更新费与普通两阶段退路。

Books：整合 [TRAIN-SFT](../../../../books/part-04-training-system/29-sft.md)，多Teacher Debate标题前两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23590 Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents](https://arxiv.org/html/2605.23590v1)

采用精确v1，必要证据：§3–4/T1–3/Limitations。Rubric ranking训练与preaction verify/single retry可采，LLM judge非gold truth。未经训练rubric反退，更多tool calls/预算未匹配，Gemini prompt-only不是同RL训练泛化；不将更好排序/可读检查表升级安全授权。

Books：整合 [AGENT-REFLECTION](../../../../books/part-07-agent/80-reflection.md)，AEWM后、普通多约束任务前两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23128 $\pi_0$-EqM: Equilibrium Matching for Closed-Loop Vision-Language-Action Control](https://arxiv.org/html/2605.23128v1)

采用精确v1，必要证据：III/Eq1–9、IV–VI。局部gradient potential与μ0理论不授部署Nesterov全局收敛；两任务threshold scan、objective/stopping/warmstart未完全分离，matched300steps非同walltime。当前EqM两段实际已含固定点/阈值/cap/warmstart、controllerfallback及GeCO/LoopVLA反侧，具体NC而非泛主题覆盖。

Books：已有覆盖 [MULTIMODAL-EMBODIED-VLA](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，EqM现有fixed-point/residual两段。仅采用上述收窄命题，指定reader实际读目标完整局部后确认语义承载，不声称覆盖论文全部超参数/排名。

### [2605.23243 Are Frontier LLMs Ready for Cybersecurity? Evidence for Vertical Foundation Models from Dual-Mode Vulnerability Benchmarks](https://arxiv.org/html/2605.23243v1)

采用精确v1，必要证据：§3.1–3.6/4.1–4.2/5–7/Limitations。五localhost apps/118GT，函数benign分母与提交finding分母不同。Model/training/budget/harness共同变化，不授methodology唯一因果、deterministic confirmation=zeroFP；abstract4–8%与表口径矛盾不采用。Duplicate/invalid/no-impact与可利用分开，并计失败尝试/triage全费。

Books：整合 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，Compound Artifact标题前一段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23071 The Efficiency Frontier: A Unified Framework for Cost-Performance Optimization in LLM Context Management](https://arxiv.org/html/2605.23071v1)

采用精确v1，必要证据：III–V采用域及直接cost反侧。仅amortized effective-token proxy，不是实测latency/$/energy；Hotpot5k/seed42/GPT5.4mini与oracle检索条件不授部署最优。TFIDF零LLMtoken不等索引免费。当前219预建索引upfront和313完整compressor+target break-even/质量与硬件长批重算承载采用命题，不重复论文N公式。

Books：已有覆盖 [AGENT-CONTEXT](../../../../books/part-07-agent/75-context.md)，预建索引upfront与完整压缩break-even段。仅采用上述收窄命题，指定reader实际读目标完整局部后确认语义承载，不声称覆盖论文全部超参数/排名。

### [2605.23764 HyperParallel-MoE: Multi-Core Interleaved Scheduling for Fast MoE Training on Ascend NPUs](https://arxiv.org/html/2605.23764v1)

采用精确v1，必要证据：§3–6/Alg1/T1–3。put_mem_signal在data globally visible后发，SplitSpec保持K reduction，不匹配回退unsplit。SSC编译窗外；64A3/bf16/4096/mb2的balanced模块1.58不等step1.08–1.09，8Kmicro反退保留，不授任意shape/GPU。原评分2+3+3=8未改。

Books：整合 [TRAIN-DISTRIBUTED-TRAINING](../../../../books/part-04-training-system/36-distributed-training.md)，FlashOverlap后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23500 B-GRTO: Bootstrapped Group Relative Tool Optimization for Referring Segmentation](https://arxiv.org/html/2605.23500v1)

采用精确v1，必要证据：§3/Eq1–10、§4/T1–2、§5。Sequence importance stopgrad权重只给工具更新；BCE/softIoU不是最终IoU精确导数，不穿离散tool选择。有限replay仅近似posterior，ReasonSeg过拟合/跨域退步及两学习率失配保留；offline rollouts/storage/工具optimizer全计费。

Books：整合 [TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md)，Sequence Reward标题前两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23657 OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents](https://arxiv.org/html/2605.23657v1)

采用精确v1，必要证据：§2–4/6/A1。677自动任务/30受欢迎skill快照，force-read不等执行；3–5x含cache token非$/latency。Opusjudge与四人100样本不授全可靠。当前1444–1458、1487及Trigger/full-read/compliance/boundary/outcome正文实际承载采用测量单位，未称全benchmark已覆盖。

Books：已有覆盖 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，control-path/no-skill/Trigger-Compliance-Boundary链。仅采用上述收窄命题，指定reader实际读目标完整局部后确认语义承载，不声称覆盖论文全部超参数/排名。

### [2605.23345 SCOPE: Simulating Cross-game Operations in Playable Environments for FPS World Models](https://arxiv.org/html/2605.23345v1)

采用精确v1，必要证据：§3.1–3.4/4.1–4.4/T1–4/5。Per-pixel visual/time query机制可采；跨模型baseline先经Gemini译telemetry为text有输入瓶颈，同telemetry消融才支持局部架构差额。合成初帧短片不等持久state/真实physics，5B端到端适配、CFG等费用保留。

Books：整合 [MULTIMODAL-WORLD-MODELS](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，action-conditioned首段后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23904 SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/html/2605.23904v1)

采用精确v1，必要证据：§3–4/B/C。Strict reused selection gate非独立最终测试，不授全局泛化/安全；offline rollouts、optimizer和更长skill context全计费，没新增optimizer calls非零部署费。Baseline缺测不混排，harness/judge改变重验并保原短skill/旧已验版本。

Books：整合 [AGENT-PROMPT](../../../../books/part-07-agent/74-prompt.md)，SkillMOO后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23454 ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning](https://arxiv.org/html/2605.23454v1)

采用精确v1，必要证据：§3.2/4.1–4.4/A/E/F。Qwen3-4B/32Bjudge/8A100；QC检查自足/忠实/覆盖/格式。平均0.9不授每任务普胜，GeneralRubric Health/Writing与Reference Health更好、IFEval反退保留；预算未闭不授唯一因果，同源generator/judge非独立真值。

Books：整合 [TRAIN-DATA](../../../../books/part-04-training-system/27-data.md)，synthetic首段后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23163 Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving](https://arxiv.org/html/2605.23163v1)

采用精确v1，必要证据：§3–4/T1–5/A/C。Greedy首错+bonus不授随机verifier精确AR分布；单H100/bs1 TPS含scaffold，11.8x还含SGLang工程，不全归算法。仅open-loop无edge/闭环安全，轨迹均值1/N需独立残差且多模态平均不一定可执行。

Books：整合 [MULTIMODAL-EMBODIED-VLA](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，联合模型物理接口段前两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23025 World Machine: Towards Generative World Modeling for Time-Series](https://arxiv.org/html/2605.23025v1)

采用精确v1，必要证据：§3–5。Toy1D两层/state128只说明可训练；15模型protocol与9600配置各一次且剔除发散分开。浅预测弱、多轮遍历和state维护有费，没有真多模态或LLM省费证据；不把回写向量当真实环境标签。

Books：整合 [MULTIMODAL-WORLD-MODELS](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，Latent dynamics首边界段后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23395 Convex Compositional Reasoning Models](https://arxiv.org/html/2605.23395v1)

采用精确v1，必要证据：v1 §2.1–4/6–7/C；v2有限§3/4/6/7。Compact convex relaxation+非负convex factors；正确certificate仍需invalid marginγ与2εΣw<γ。Birkhoff非完整NQueens凸包，greedy decode另步；随机S64/T140与正文S8/T50、convex landscape multimodal矛盾不拼recipe。v1/v2采用域规范文本相同，无重要修订差额，不重复评分。

Books：整合 [AGENT-PLANNING](../../../../books/part-07-agent/79-planning.md)，Search/Pruning首边界段后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。本窗相关v2采用域有限比较相同，不因版本号新增家族或重评分。

### [2605.23055 Decomposing and Measuring Evaluation Awareness](https://arxiv.org/html/2605.23055v1)

采用精确v1，必要证据：§2.1/3–6/B1/B3。Aware/unaware是同task观测分组非随机操纵，不能采awareness tax为因果效应。CoT/summaries只verbalized recognition；judge48aware vs human37–40且κ.64–.74，不使观测率成为严格lowerbound。正式只采用信号/因果/control分责，当前4713完整段实际承载，不为八因素术语制造diff。

Books：已有覆盖 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，Evaluation-awareness必须分开Representation、Verbalization与Control。仅采用上述收窄命题，指定reader实际读目标完整局部后确认语义承载，不声称覆盖论文全部超参数/排名。

### [2605.23393 Every Component is a Lookup: Token Attribution and Composition from a Single Decomposition](https://arxiv.org/html/2605.23393v1)

采用精确v1，必要证据：§3.1–3.3/5/B2/E。V1已有Pile1000评分/200heldout、selected5components/layer的communication-cut knockout，校准聚合分数不证明token/path counterfactual truth。Softfloor破严格conservation，深层path volume/known mode/top2000/pruning/pre-norm限制近文；严格在旧06480 binding之外保存。

Books：整合 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，Interpretability Graph旧06480 binding前两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23096 Encrypted Neural Networks without Overflows](https://arxiv.org/html/2605.23096v1)

采用精确v1，必要证据：§3–6/C。需输入域I、verifier soundness及数值roots假设；前层approx误差进入后层bounds，不能只验原NN。宽bounds/degree/illscaledcoefficients成本保留；形式界明确不含CKKS noise，不授密文全栈零错/IND-CPAD/Transformer普适安全，artifact未核。

Books：整合 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)，隐私明文边界TEE段后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23262 Design and Report Benchmarks for Knowledge Work](https://arxiv.org/html/2605.23262v1)

采用精确v1，必要证据：§3–6。三步+三case是设计论证，不把18活动taxonomy当部署绩效实证。正式采用范围限claim绑定对象；当前149–188 EvalSpec intended-use/population/scorer、one-shot不代表澄清迭代监督、native-editability维护已实际承载，不仅因三个术语关闭。

Books：已有覆盖 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，EvalSpec/GDPval/native-editability实际链。仅采用上述收窄命题，指定reader实际读目标完整局部后确认语义承载，不声称覆盖论文全部超参数/排名。

### [2605.23668 OnePred: Next-Query Prediction via Recursive Intent Memory in Multi-Turn Conversations](https://arxiv.org/html/2605.23668v1)

采用精确v1，必要证据：§3–4/A/K。k500+当前exchange不是完整会话memory；stage1 500+stage2 200、best-of3/LLMjudge、trajectory advantage广播非精确credit。22x是输入tokens非cachematched decode/$，detail-shift FullHistory反优，curation筛predictable不授全用户。当前703–707 boundedstate/detail-loss/quiet-confirmfallback承载收窄采用，不采全训练recipe。

Books：已有覆盖 [AGENT-CONTEXT](../../../../books/part-07-agent/75-context.md)，OnePred bounded intent-state两段。仅采用上述收窄命题，指定reader实际读目标完整局部后确认语义承载，不声称覆盖论文全部超参数/排名。

### [2605.23826 Decomposing Queries into Tool Calls for Long-Video Keyframe Retrieval](https://arxiv.org/html/2605.23826v1)

采用精确v1，必要证据：§3–5/A。RankANDmax/ORmin、OCR先验rank1+NMS；direct question plainSigLIP可相当/胜，TREN均值近中性、rawscore同rankmean。Caption-bound单interval且筛困难answerer题，Hit不等QA足证，固定工具无audio。现1447–1451 physicalplan/coverage/evidenceGate/scorerfallback承载采用范围。

Books：已有覆盖 [AGENT-RAG](../../../../books/part-07-agent/76-rag.md)，ToolMerge typed toolcalls/rankings/Boolean merge两段。仅采用上述收窄命题，指定reader实际读目标完整局部后确认语义承载，不声称覆盖论文全部超参数/排名。

### [2605.23701 Metadata Predictability Is Not Evidence Dependence: An Intervention-Based Audit for Weak-Label Benchmarks](https://arxiv.org/html/2605.23701v1)

采用精确v1，必要证据：§2–5。K8是permutation人口SD非SE/显著性，Δacc≈0非outputs完全不变；positive只该reader的evidence sensitivity非semantic reasoning。ReconstructedHotpot heuristiclabels578:22不等原Hotpot天然无证据，SNLI强reader reversal/FEVER正控保留。

Books：整合 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，historical预测负控17692第二段后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23595 Cost-Effective Model Evaluation with Meta-Learning](https://arxiv.org/html/2605.23595v1)

采用精确v1，必要证据：§3–6尤其4.2。Unseen-model adaptation用(SD_i,M_i*)真accuracy support，label-free仅最终target；还需原训练集与hidden representations，非任意blackboxAPI。512context微调非免permodel学习，referenceIDs/细表依code未核，不授普适低MAE/interval calibration；1–2min/946$非端到端部署费。

Books：整合 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，Forecastability15134 marker后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23066 Orbax: Distributed Checkpointing with JAX](https://arxiv.org/html/2605.23066v1)

采用精确v1，必要证据：§2–5/C–E/F2–F3。Shape/dtype/sharding摘要提出cast/reshard/partialload而非完整resume。Async hostsnapshot后IO、global metadata/finalize完才持久化；20次隔离IO/CPU-only multislice非完整训练收益，n2broadcast反退与subchunk/QPS/metadata费保留。

Books：整合 [TRAIN-CHECKPOINT](../../../../books/part-04-training-system/35-checkpoint.md)，reshard/load与weights-only分界后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23045 The TIME Machine: On The Power of Motion for Efficient Perception](https://arxiv.org/html/2605.23045v1)

采用精确v1，必要证据：§3–5。Local/global displacement、neighbor、occlusion与动点加权；static-camera Kubric250K/4A10080G/120h。依赖外部tracker及其误差/预训练/推理费；4orders为video-hours非全pipeline compute，frozen features下游仍train linearprobe，纯motion丢appearance与Exo筛/crop边界保留。

Books：整合 [MULTIMODAL-REPRESENTATION](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，时间同步/augmentation段后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23176 DRIVESPATIAL: A Benchmark for Spatiotemporal Intelligence in VLMs for Autonomous Driving](https://arxiv.org/html/2605.23176v1)

采用精确v1，必要证据：§3–5/B1/B3/C3。20tasks/15.6kQA源于5ADdatasets，camera可见性与跨track身份规则可采。BEV GT/HDMap/LiDAR boxes为privileged诊断且排Const，非部署感知；人mini1000不限回放与模型32A100greedy非同预算，不把28.4gap当全量/因果瓶颈。

Books：整合 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，三view00799后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23216 CaST-Bench: Benchmarking Causal Chain-Grounded Spatio-Temporal Reasoning for Video Question Answering](https://arxiv.org/html/2605.23216v1)

采用精确v1，必要证据：§3–5/T3/Eq3/14.2。MCQ、IM-t/vIoU、threshold.1联合度量分开，F/S不强行互补。低grounding也可能format/坐标表达失败，maskfilter+GT-chain提示不认证因果faithfulness；LLM/SAV/人审与video/1FPS输入不同保留。

Books：整合 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，PerceptionComp26653后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23491 CoSPlay: Cooperative Self-Play at Test-Time with Self-Generated Code and Unit Test](https://arxiv.org/html/2605.23491v1)

采用精确v1，必要证据：v1 §2–4/A1/A2/E/L；v2有限§2/3/4/A1/A2。每次池变重算，ERR作缺证的pairwise-compatible群是order-dependent。Round0独立采样/q1>q0不延续自演化；signature theorem需anti-concentration/iid/有限空间，共同常量bug反侧保留。2H10080G/vLLM，main全4bench与3seed200题分开；token/call非墙钟全费。v2采用域相同无重要修订，partial raw不称全附件。

Books：整合 [AGENT-REFLECTION](../../../../books/part-07-agent/80-reflection.md)，主动分裂15669后/AEWM前两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。本窗相关v2采用域有限比较相同，不因版本号新增家族或重评分。

### [2605.23237 StereoGenBench: A Synthetic Multi-Camera Benchmark for Stereo Generation under Controlled Baseline Regimes](https://arxiv.org/html/2605.23237v1)

采用精确v1，必要证据：§3–6/H。G0 oraclegeometry/G1camera metadata/G2monocular不可混榜；main每scene一pair，metadata支持15pairs不等已跑allpairs sweep。PPSNR可奖励复制纹理，SD依fixedmatcher/validfilter/offset fit；framewise/FVD不证明flicker或temporalmodel，synthetic不授realworld。

Books：整合 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，SGC19048第二段后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23733 Any2Any: Efficient Cross-Embodiment Transfer for Humanoid Whole-Body Tracking](https://arxiv.org/html/2605.23733v1)

采用精确v1，必要证据：§3.3–3.4/4.1/4.3/5。Similar humanoid topology的手工对齐/PPO/privilegedcritic，MuJoCo非实机；injective map剔除redundantjoints不授任意Nr/T双向无损，物理参数少不证明policy低秩。1%复用已付pretraining非总训练减99%，保samplingrate/hardware混杂与retarget/alignment成本。

Books：整合 [MULTIMODAL-EMBODIED-VLA](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，canonical手型16712后两段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23255 Learning-Augmented Online Scheduling with Parsimonious Preemption](https://arxiv.org/html/2605.23255v1)

采用精确v1，必要证据：§1.1/1.2/2/3.1–3.3proof/5/6。主理论allavailable t0、knownrates、underpredict，overpredict需g上界/reset；checkpoint只累计work milestone非持久化checkpoint。m10/n100 synthetic与修改heuristic SNAP不授真实GPU迁移/LLM SLO/任意arrival。原EX按core具体条件界撤回，准入5分经独核，未用审阅成本缩池。

Books：整合 [PLATFORM-GPU-SCHEDULER](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)，victim段后/quota重议前一段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。

### [2605.23651 How Human-Like Are Large Language Models? A Register-Aware Linguistic Evaluation Framework](https://arxiv.org/html/2605.23651v1)

采用精确v1，必要证据：§3–6/9/A/B/I。English67features/600样本/400–440词，register内固定归一与RBFbandwidth；human-human重采样非语义/偏好等价，prompt稳定性仅BNC且fewshot可反退。1–2A10080G/vLLM/temp1/top-p1；不由较小MMD推事实/流畅/安全或训练因果。

Books：整合 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，人类描述26589第二段后一段。已实际保存并经指定reader唯一非writer POST通过；条件、全费和旧路径退路随正文保留。


## 5. 缺口与下一步

普通研究、来源扫描/筛选、候选必要证据、Books写入与实际POST待办为0；非报告作者完整六部分DAY（R31）及保存完成态有限FINAL（R32）均已实际通过，本日没有未处理的可执行普通工作。

以下为本窗终态保留项，不支持正面证据、Books或无遗漏断言；它们不等Coverage/Evidence通过，各项定点重开条件随身份列明。

- 来源历史子层：Meta Research/Publications不可得；Moonshot Blog只有2025且Github creation不能代release；MiMo仅Blog undated/More缺历史日期（Paper8行已核）；Google Publications只有year不能提供日级历史。实际入口与有限恢复见§2。取得目标官方有日期事件或可重放历史目录时只重开命中来源切片；当前不用于阴性覆盖，不因部分入口失败无限全站逆向。DeepMind真实分页、DeepSeek Change Log、MiMo Paper已恢复，不再虚列受阻。
- 公开日期资格9项：[SCRIPT22894](https://arxiv.org/abs/2605.22894v1)、[GEM4D22882](https://arxiv.org/abs/2605.22882v1)、[ReadingCalibratedUncertainty22864](https://arxiv.org/abs/2605.22864v1)、[EDRM22873](https://arxiv.org/abs/2605.22873v1)、[LatentCacheFlow22863](https://arxiv.org/abs/2605.22863v1)、[QASC22834](https://arxiv.org/abs/2605.22834v1)、[TritonMoE23911](https://arxiv.org/abs/2605.23911v1)、[VineLM23914](https://arxiv.org/abs/2605.23914v1)、[ModelParkingTax23918](https://arxiv.org/abs/2605.23918v1)。完整精确题摘具潜力，但v1最早公告界在目标前；前6 exactDOI registered在May25，后3在May26 03:02:25/30/35Z，组合区间均跨日。注册日、ID月份或更新日不能强行截成May25/窗外；有限原页/月表/精确DOI与具名旧记录检查未恢复直接日门，未列确定候选或贡献EX。需要精确ID官方日公告、带日期首次正文或可信归档使整个公开区间落同一BJT日，届时只重开这9项的日期资格及相应归属；当前不进Books/正面Evidence。SCRIPT May25 v2提交最早公告已到May26，不作为本补May25修订，QASC v2更晚。
- 精确版本边界：MARGIN只采已核exact-v1 PDF，HTML August24 masthead不作首公开；ModeSwitch不倒灌现题RequestRouter。CCEM/CoSPlay采用域v1/v2有限比较一致，没有本窗重要修订差额；局部raw未全下载不冒称全附件。没有结论依赖的未读附件被改称外部阻塞。

上述保留身份/必要字段/有限恢复与重开位置见[作者A9/A19](../_sources/daily-20260526/SUP_SOURCES_20261021.md)、[独立reader R24及后续](../_sources/daily-20260526/SUP_REVIEW_20261021.md)。原小时窗口的263/86、16项历史写回与MiniMax May27归属继续按原有效记录复用；不是这次自然日的来源或完成证明。不移动旧材料，不启动其它日期、Live、Weekly或2025。

## 6. 复核

复核者：supp_may26_reader（独立于本报告作者和Books写入者）

结论：通过

R31实际六部分DAY与R32保存完成态有限FINAL均通过；最后仅行政同步既成结果，不第三读有效Source/POST。

已实际覆盖38新增家族的精确题摘/准入、日期组合与必要Source，30处Books逐字PRE及保存后完整新增/直接两侧/本人注POST；8项具体已有覆盖实际核承载段。对有安全/设计反证信号的排除RAS22937、Defense23448、next-token23278追加必要核心，代表EX另含23715/22923/23578/23568，scope EX23130/22929与两OpenAI事件分别具理由；不是1081条全文全量独读。实际查询/停止、9跨日资格与源历史子层按[独立复核记录](../_sources/daily-20260526/SUP_REVIEW_20261021.md)处理，首批准入校准与已有效Source/POST不重复验收。R31完整六部分DAY及R32保存完成态有限FINAL已实际通过，无待核层，不重做有效Source/POST。

历史小时窗独核：原fresh non-author R3已通过原86、74deep/12standard、37Applied/42NC/5Structural/2ReportOnly和16写回层，具体[原R3记录](../_sources/daily-20260526/FRESH_NONAUTHOR_V3_FINAL_REVIEW_20260916_R3.md)继续有效；该结论不代本次May25补窗DAY/FINAL。完成态机械检查：V3通过，173个本地引用0 missing，原86行顺序逐字不变、原小时窗不变、冻结档案bytes与启动tmp一致，旧§4连续保留；报告/作者SUP/16实际Books owner的限定working/cached diff-check通过。机械检查不替代语义复核。
