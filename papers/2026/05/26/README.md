# Daily Research — 2026-05-26

**规范：** V3

**窗口：** 2026-05-25T09:00:00+08:00 ～ 2026-05-26T09:00:00+08:00

**状态：** 完成

**Books：** 纳入本次

**检查时间：** 2026-09-16T10:00:13+08:00

## 1. 结论

旧 V2.1 `Complete`、1208 raw 与 170 candidates 不再拥有当前状态。当前 first-public owner 仅为 2026-05-26 08:00 BJT 的 263 项 arXiv official announcement batch；MiniMax 技术页官方 JSON-LD `datePublished=2026-05-27T00:00:00Z` 属 05-27，不进入本日正面或 no-hit 投影。全日守恒为 **263 = 86 retained + 177 pre-denominator closure + 0 withdrawn**。

Evidence 为 **86 = 74 deep complete + 12 standard complete + 0 blocked**；评分分布为 `{6: 12, 7: 9, 8: 50, 9: 15}`。Books 对账为 **86 = 37 Applied + 0 Integrate + 42 No Change + 5 Structural Candidate + 2 Report Only**。16 个 05-26 root-action semantic body、paired marker 与独立 `source-family` marker 均已存在且位于 Review notes 前。此前 fresh review 发现并有界修复了 `2605.24423` 的 denominator false negative；另一名未参与修复和 Books 写回的 fresh non-author reviewer 已完成独立终审并通过 Complete Gate。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | official News/Research RSS; two 05-25 08:00 BJT events are one hour before this window | 已检查 | 0 raw; both outside window |
| SRC-ANTHROPIC | official Research; nearest dated research event 05-22 | 已检查 | none |
| SRC-GOOGLE-AI | DeepMind Research/Google Publications; adjacent dated items 05-19 and 05-28 | 已检查 | year-only cards do not support site-wide no-hit |
| SRC-META-AI | official Publications entry | 受阻 | empty/internal-error response; not used for no-hit |
| SRC-QWEN | official article index; adjacent 05-20 and 05-29 | 已检查 | none |
| SRC-DEEPSEEK | official News/Research; adjacent 04-24 and 06-24 | 已检查 | none |
| SRC-MOONSHOT | official Kimi Blog; no dated research/release/RFC in window | 已检查 | none |
| SRC-TENCENT-HUNYUAN | official publicList; visible records outside window | 已检查 | none |
| SRC-ZAI | official Research; adjacent 05-20 and 06-16 | 已检查 | none |
| SRC-BYTEDANCE-SEED | official Research/Public Papers; adjacent 05-16 and 05-29 | 已检查 | none |
| SRC-BAIDU-ERNIE | official technical Blog; latest explicit date before window is 05-09 | 已检查 | none |
| SRC-XIAOMI-MIMO | official dated papers; adjacent 03-13 and 06-29 | 受阻 | undated cards do not support day-level no-hit |
| SRC-MINIMAX | official Research/Blog JSON-LD `datePublished=2026-05-27T00:00:00Z` | 已检查 | 05-26 window 为 0 raw；事件由 05-27 08:00 BJT owner |
| SRC-ARXIV | official 05-25 20:00 ET announcement migrated to 05-26 08:00 BJT | 已检查 | 263 raw = 86 retained + 177 closure |

完整 owner 与 event receipt 见 [`official-owner-batch-evidence-v3.json`](../_sources/daily-20260526/official-owner-batch-evidence-v3.json)，14-source 结构化记录见 [`source-coverage-v3.json`](../_sources/daily-20260526/source-coverage-v3.json)，263 条逐项结果与 family-aware closure 理由见 [`screening-outcomes-v3.json`](../_sources/daily-20260526/screening-outcomes-v3.json)。受阻或无日级时间的入口不支持全站 no-hit；普通 commit/PR 未扩入 denominator。

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


## 5. 缺口与下一步

终态保留项：Meta 历史入口的空响应/internal error 与 MiMo 未标日期卡片无法证明本窗无事件；两者均不用于支持正面证据、Books 或无遗漏断言。定点重开条件是取得能够唯一归入本窗的官方事件页、带时区发布时间或可重放的官方历史索引；触发后只重开命中的来源切片或 Source Family，不扩窗、不扩源。

1. root 已按 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260526/root-books-writeback-queue-v3.json) 完成全部 16 项 Books 写入/marker 动作，pending root queue 为 0；机械验收见 [`ROOT_MARKER_ONLY_REPAIR_20260916.md`](../_sources/daily-20260526/ROOT_MARKER_ONLY_REPAIR_20260916.md)。
2. 当前没有待补材料、待审候选或待写 Books；仅当 exact-v1 identity、owner date、正文证据或已吸收命题发生实质变化时重开本日。
3. MiniMax 事件继续只由 05-27 owner 承担，不在 05-26 重复计分或形成 no-hit 结论。

## 6. 复核

复核者：fresh non-author reviewer R3（未参与 05-26 author repair、`2605.24423` 恢复或 root Books 写回）

结论：通过

本轮以反例优先方式独立复核冻结结果。窗口与 owner、`263 = 86 + 177 + 0`、Evidence `74 deep + 12 standard`、Books `37 Applied + 42 No Change + 5 Structural + 2 Report Only`、16 个正文 binding、MiniMax 的 05-27 归属以及 pending root queue=0 均通过；`2605.24423` 的 exact-v1、score 8、`AGENT-MULTI-AGENT` 与 No Change 判断成立。最终 receipt 见 [`FRESH_NONAUTHOR_V3_FINAL_REVIEW_20260916_R3.md`](../_sources/daily-20260526/FRESH_NONAUTHOR_V3_FINAL_REVIEW_20260916_R3.md)。
