# Daily Research — 2026-06-18

**规范：** V3
**窗口：** 2026-06-17T09:00:00+08:00 ～ 2026-06-18T09:00:00+08:00
**状态：** 完成
**Coverage 限制：** 一项已终结的外部日期材料缺口；不影响现有 Candidate/Evidence/Books 结论
**Books：** 纳入本次
**检查时间：** 2026-09-11T15:20:00+08:00

## 1. 结论

canonical raw inventory 共 525 个身份；本轮已逐项读取全部 title + 完整 abstract，冻结 45 个候选、以 family-specific reason 关闭 480 项。相对旧宽池恢复 17 个 false negative；所有恢复项均完成 exact-v1 Evidence Review、V2 评分、ROADMAP owner 与 Books Decision。14 个 Integrate 已在目标 Books 的首个顶层 Review notes 前形成可辨识机制链，31 个 Existing Coverage 已逐项复验。当前合同来源再认证发现 Anthropic `Project Fetch: Phase two` 只有日期、没有可判定 09:00+08 边界的官方发布时间；该项未进入本日候选、评分或 Books，并以精确外部材料请求终结。现有 45 项 Candidate/Evidence/Books 结论不受影响。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260618/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ANTHROPIC | Project Fetch: Phase two 仅披露日期 2026-06-18，无法判定 09:00+08 边界归属；详见 [source recert](../_sources/daily-20260618/CURRENT_SOURCE_RECERT_20260914.md) | 受阻 | 缺官方发布时间与时区；未纳入候选、评分或 Books |
| SRC-GOOGLE-AI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260618/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-META-AI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260618/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-QWEN | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260618/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-DEEPSEEK | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260618/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-MOONSHOT | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260618/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260618/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ZAI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260618/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260618/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260618/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260618/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-MINIMAX | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260618/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ARXIV | 525-identity canonical raw inventory；逐项读取 title + 完整 abstract，冻结 45 Candidate / 480 Close，恢复 17 个旧宽池 false negative；owner 只在 official listing/announcement 可证明时迁移 | 已检查 | 无 |

分母前关闭项保留 identity、完整题摘 hash 与 family-specific closure。全量反向审计不以关键词、ROADMAP 可映射性或候选数量准入；本窗 17 个恢复项均已核验 official exact-v1，未发现 withdrawn retained family。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Breaking the Solver Bottleneck: Training Task Generators at the Learnable Frontier](https://arxiv.org/html/2606.18284v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 TRAIN-DATA 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文锚点：Post-training Data Selection 是当前 Policy 的在线控制环 |
| [Conflict-Aware Retriever Editing for Knowledge Injection Attacks on LLM-Based RAG Systems](https://arxiv.org/html/2606.18310v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 AGENT-RAG 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文锚点：RAG 安全必须覆盖完整状态生命周期 |
| [SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents](https://arxiv.org/html/2606.18356v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Evidence Trail 与最终答案必须分别验收 |
| [JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting](https://arxiv.org/html/2606.18394v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 INFER-SPECULATIVE-DECODING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[owner](../../../../books/part-05-inference-system/48-speculative-decoding.md)；命题锚点：动态候选树必须编译为 Accelerator-safe Commit Plan |
| [CloakLM: Obfuscating GPU Memory Layout to Mitigate Model Ex-filtration for Serving](https://arxiv.org/html/2606.18400v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Weight Streaming 的保密边界在片上明文状态才结束 |
| [Finding Compiler-Platform Interaction Bugs in Deep Learning Pipelines via Cross-Layer Constraints](https://arxiv.org/html/2606.18421v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 INFER-TENSORRT-LLM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；命题锚点：Compiler Frontend 是独立的语义故障层 |
| [Beyond Prediction: Tail-Aware Scheduling for LLM Inference](https://arxiv.org/html/2606.18431v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；命题锚点：当前能放下，不等于未来可完成 |
| [ToolChain-CRC: Conformal Risk Control for Agentic AI Under Retrieval and Tool-Use Drift](https://arxiv.org/html/2606.18467v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Miscoverage 要拆成 Sampling Failure 与 Selection Failure |
| [Ghost Vectors: Soft-Deleted Embeddings Remain Reconstructible in HNSW Vector Databases](https://arxiv.org/html/2606.18497v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 AGENT-RAG 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文锚点：RAG 安全必须覆盖完整状态生命周期 |
| [AI Sandboxes: A Threat Model, Taxonomy, and Measurement Framework](https://arxiv.org/html/2606.18532v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：不可信代码需要 OS 级 Effect Boundary |
| [The Gate Is Only as Honest as Its Contracts: ContractGuard for the Contract Layer of Risk-Aware Causal Gating](https://arxiv.org/html/2606.18550v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Policy-as-Data：可更新规则与模型判断必须分开版本化 |
| [ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters](https://arxiv.org/html/2606.18600v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；命题锚点：Heterogeneous Offload 必须同时预算 Preemption 与 State Transfer |
| [BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training](https://arxiv.org/html/2606.18650v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 TRAIN-DATA 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文锚点：Post-training Data Selection 是当前 Policy 的在线控制环 |
| [EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems](https://arxiv.org/html/2606.18668v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 AGENT-MULTI-AGENT 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；正文锚点：Coordination Failure |
| [Understanding and Mitigating Prompt Leaking Attacks in Real-World LLM-Based Applications](https://arxiv.org/html/2606.18673v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Privacy Boundary 必须覆盖全部 Observable Channels |
| [Stealthy World Model Manipulation via Data Poisoning](https://arxiv.org/html/2606.18697v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-WORLD-MODELS 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；正文锚点：Action-conditioned World Model 要先通过 Integrity Gate |
| [ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving](https://arxiv.org/html/2606.18741v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；命题锚点：DP↔TP 切换是带版本的在线状态转换 |
| [What Must Generalist Agents Remember?](https://arxiv.org/html/2606.18746v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 AGENT-MEMORY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Context 与 Memory 的状态边界 |
| [Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/html/2606.18810v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 TRAIN-GRPO 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；命题锚点：从序列 Reward 到受约束的 Token Credit |
| [GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents](https://arxiv.org/html/2606.18829v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Shared Memory 必须同时通过 Utility、ACL 与 Forgetting Gate |
| [WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents](https://arxiv.org/html/2606.18847v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-EMBODIED-VLA 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；命题锚点：Policy 内部的 Latent Memory 是 Episode State，不是 Agent Memory |
| [EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts](https://arxiv.org/html/2606.18967v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 INFER-SPECULATIVE-DECODING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[owner](../../../../books/part-05-inference-system/48-speculative-decoding.md)；命题锚点：Agent Workflow 让 Proposal Budget 与 Residual State 都变成动态对象 |
| [Spotlight: Synergizing Seed Exploration and Spot GPUs for DiT RL Post-Training](https://arxiv.org/html/2606.19004v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-GPU-SCHEDULER 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-GPU-SCHEDULER，[owner](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)；命题锚点：可回收资源需要 Lease 与 Reclaim Protocol |
| [FoMoE: Breaking the Full-Replica Barrier with a Federation of MoEs](https://arxiv.org/html/2606.19025v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 TRAIN-DISTRIBUTED-TRAINING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[owner](../../../../books/part-04-training-system/36-distributed-training.md)；正文锚点：Expert Parallel 从静态放置到动态 Token + Weight Spill |
| [PhantomSkill: Malicious Code Injection in Agent Skill Ecosystems](https://arxiv.org/html/2606.19191v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Skill Poisoning 的真值是 Side Effect，而不是是否被调用 |
| [Runtime Compliance Verification for AI Agents](https://arxiv.org/html/2606.19242v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Behavioral Contract 把 Invariant、Drift 与 Recovery 变成运行期状态 |
| [Detecting Hidden ML Training With Zero-Overhead Telemetry](https://arxiv.org/html/2606.19262v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-MONITORING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-MONITORING，[owner](../../../../books/part-06-ai-infrastructure/67-monitoring.md)；命题锚点：Host 与 Device 都不可信时，用计算挑战构造旁路遥测 |
| [TurboServe: Serving Streaming Video Generation Efficiently and Economically](https://arxiv.org/html/2606.19271v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 整合：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点：迭代生成与流式会话需要显式 Progress State |

<!-- full-raw-recovered-candidate-rows:start -->
| [Gaussian Mixture Attention: Linear-Time Sequence Mixing via Probabilistic Latent Routing](https://arxiv.org/html/2606.18283v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；3 + 3 + 2 = 8 | 深入完成 | 整合：MODEL-SELF-ATTENTION，[owner](../../../../books/part-02-model/14-self-attention.md)；已实际写入正文；正文锚点：Routing representation 与 cache representation 的条件合并 |
| [SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior](https://arxiv.org/html/2606.18322v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION，[owner](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；命题锚点：可读出不等于可拆卸或可控制 |
| [From Sparse Features to Trustworthy Proxies: Certifying SAE-Based Interpretability](https://arxiv.org/html/2606.18383v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Activation Oracle 的 Confidence 也要校准 |
| [PreUnlearn: Auditing Collateral Knowledge Damage Before Large Language Model Unlearning](https://arxiv.org/html/2606.18473v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：不再回答不是 Deletion Evidence |
| [SFT Overtraining Predicts Rank Inversion via Entropy Collapse Under RLVR](https://arxiv.org/html/2606.18487v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；命题锚点：Exploration 必须与 Verified Progress 对齐 |
| [RouteJudge: An Open Platform for Reproducible and Preference-Aware LLM Routing](https://arxiv.org/html/2606.18774v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Router 上线需要可拒绝的 Gain Certificate |
| [Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architecture for LLM Agents](https://arxiv.org/html/2606.18947v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；命题锚点：Retrieval Control 应成为 Reader 外部的 Typed State |
| [Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation](https://arxiv.org/html/2606.18960v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；命题锚点：从全历史条件到有界 History Bank 与 Self-rollout Distillation |
| [TRAP: Benchmark for Task-completion and Resistance to Active Privacy-extraction](https://arxiv.org/html/2606.18996v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Privacy Boundary 必须覆盖全部 Observable Channels |
| [Lifecycle-Aware Dynamic Analysis for Secure ML Model Execution](https://arxiv.org/html/2606.19023v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；已实际写入正文；正文锚点：从文件哈希到可执行来源链 |
| [Quantifying and Auditing LLM Evaluation via Positive--Unlabeled Learning](https://arxiv.org/html/2606.19057v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：当只有少量确定正例而未标注集混合正负时，evaluation audit 可用 positive-unlabeled inference 估计隐藏错误率 |
| [A Technical Taxonomy of LLM Agent Communication Protocols](https://arxiv.org/html/2606.19135v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-MCP，[owner](../../../../books/part-07-agent/83-mcp.md)；已实际写入正文；正文锚点：从连接会话到显式请求契约 |
| [Pulse: Training Acceleration for Large Diffusion Models with Automatic Pipeline Parallelism](https://arxiv.org/html/2606.19163v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；3 + 3 + 2 = 8 | 深入完成 | 整合：TRAIN-PIPELINE-PARALLEL，[owner](../../../../books/part-04-training-system/38-pipeline-parallel.md)；已实际写入正文；正文锚点：Schedule Abstraction 要先证明依赖合法，再比较 Bubble |
| [User as Engram: Internalizing Per-User Memory as Local Parametric Edits](https://arxiv.org/html/2606.19172v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；已实际写入正文；正文锚点：个性化更新与事实可靠性是两套策略 |
| [DreamReasoner-8B: Block-Size Curriculum Learning for Diffusion Reasoning Models](https://arxiv.org/html/2606.19257v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；命题锚点：Parallel Progress 与 Active Compute 是两条独立成本轴 |
| [Beyond the Current Observation: Evaluating Multimodal Large Language Models in Controllable Non-Markov Games](https://arxiv.org/html/2606.19338v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Agent 与 World Model 的证据要分层闭合 |
| [Native Active Perception as Reasoning for Omni-Modal Understanding](https://arxiv.org/html/2606.19341v1) | 2026-06-18T08:00:00+08:00 ～ 2026-06-18T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-PLANNING，[owner](../../../../books/part-07-agent/79-planning.md)；命题锚点：Active Perception 是信息价值决策，不是固定多看几步 |
<!-- full-raw-recovered-candidate-rows:end -->


## 4. 证据与知识整合

### [Breaking the Solver Bottleneck: Training Task Generators at the Learnable Frontier](https://arxiv.org/html/2606.18284v1)

**2606.18284 — Breaking the Solver Bottleneck: Training Task Generators at the Learnable Frontier**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：训练 task generator 时可用一次 solver-labeled pool 训练 activation probe，把 targeted solve-rate 作为 amortized reward；最终仍由 held-out solver 验证。

**State / data / control owner。** `TRAIN-DATA` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.18284v1 §§4 and 6 Evaluation/Results` 支持 `Math, code and SWE task generation across model scales`；模型 `Qwen2.5-3B/7B and Qwen3.5-27B solver settings`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.18284v1 §3 Probe Rewards; §5 probe data/selection`；counterevidence locator：`arXiv:2606.18284v1 §7 Limitations; mode-collapse findings`。

**Trade-off / failure / coexistence / evolution。** probe 降低 inner-loop solver cost，但 reward hacking、mode collapse 与 solver drift 要求 held-out solver gate。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.18284v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `TRAIN-DATA` owner 为 [books/part-04-training-system/27-data.md](../../../../books/part-04-training-system/27-data.md)。Review notes 前正文 `Post-training Data Selection 是当前 Policy 的在线控制环` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Conflict-Aware Retriever Editing for Knowledge Injection Attacks on LLM-Based RAG Systems](https://arxiv.org/html/2606.18310v1)

**2606.18310 — Conflict-Aware Retriever Editing for Knowledge Injection Attacks on LLM-Based RAG Systems**

**问题与机制变化。** RAG threat model 需覆盖 retriever parameter editing：攻击者可改变 ranking 而不改 corpus；index/model revision、anchor repair 与 retrieval regression 必须同 lifecycle 验证。

**State / data / control owner。** `AGENT-RAG` 是唯一知识 owner；`Books/part-07-agent/77-memory.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18310v1 §3 conflict-aware retriever editing attack; §4 anchor-based repair`；Evaluation=`arXiv:2606.18310v1 §5 multi-dataset/model retrieval and downstream evaluations`；Counterevidence=`Not Disclosed — arXiv:2606.18310v1 has no dedicated limitations section; exact-v1 counterevidence is localized at edit access, retriever architecture, corpus and transfer limitations`。Workload=`knowledge-injection attacks and repair across disclosed RAG datasets`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`attack success, retrieval ranking, downstream answer and clean-utility recovery`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** repair anchors能恢复局部行为却可能伤正常 recall；受测编辑不代表所有 retriever compromise。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18310v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-RAG` owner 为 [books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)。Review notes 前正文 `RAG 安全必须覆盖完整状态生命周期` 已形成 owner-level 机制链；本项已实际 Integrate。

### [SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents](https://arxiv.org/html/2606.18356v1)

**2606.18356 — SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents**

**问题与机制变化。** Agent security EvalSpec 必须分开 semantic compromise、artifact-visible harm evidence 与 sandbox-observed state/tool harm，并保持各自 denominator 和 matched identity。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18356v1 §3.1–3.7 attack surface, threat model, benchmark levels and measurement`；Evaluation=`arXiv:2606.18356v1 §4 experiments; §5 endpoint analyses; appendices J–M calibration/sandbox checks`；Counterevidence=`Not Disclosed — arXiv:2606.18356v1 has no dedicated limitations section; exact-v1 counterevidence is localized at prompt-only defense scope, synthetic stress-test and separate Core/Exec call boundary`。Workload=`600 cases across six attack families plus a 12,000-row matched Core/Exec analysis`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`CoreFail, HarmEvidence, SemanticOnly and sandbox state-oracle harm as separate endpoints`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 多 endpoint改善定位却增加匹配与审计成本；600 合成 case不估计生产 prevalence，prompt policy不替代 runtime control。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18356v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `Evidence Trail 与最终答案必须分别验收`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting](https://arxiv.org/html/2606.18394v1)

**2606.18394 — JetFlow: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting**

**问题与机制变化。** Parallel causal tree drafting仍遵守 proposal tree、target verification、accepted-prefix commit 与 suffix rollback；Ch48 已有该 owner、DARTree/TAPS 与 tree cost/fallback 边界。

**State / data / control owner。** `INFER-SPECULATIVE-DECODING` 是唯一知识 owner；`Books/part-05-inference-system/44-decode.md; Books/part-05-inference-system/56-inference-scheduling.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18394v1 §3 JetSpec parallel causal tree-drafting architecture`；Evaluation=`arXiv:2606.18394v1 §4–§5 vLLM integration and H100 evaluation`；Counterevidence=`Not Disclosed — arXiv:2606.18394v1 has no dedicated limitations section; exact-v1 counterevidence is localized at draft-tree/model/hardware/concurrency scope and branch-waste boundary`。Workload=`speculative decoding with parallel causal draft trees in vLLM`；Model=`Not Disclosed`；Hardware=`NVIDIA H100 GPU`；Evaluator=`accepted length, output throughput/latency and tree-width/depth ablations`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 更宽树提高候选覆盖也增加 verify shape、显存和 branch waste；现有 Ch48 已覆盖该 trade-off，不追加论文特定实现。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18394v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-SPECULATIVE-DECODING` owner 为 [books/part-05-inference-system/48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md)。Review notes 前命题级锚点为 `动态候选树必须编译为 Accelerator-safe Commit Plan`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [CloakLM: Obfuscating GPU Memory Layout to Mitigate Model Ex-filtration for Serving](https://arxiv.org/html/2606.18400v1)

**2606.18400 — CloakLM: Obfuscating GPU Memory Layout to Mitigate Model Ex-filtration for Serving**

**问题与机制变化。** 共享 GPU 上的模型权重保护可在 PCIe traffic、weight order 与 HBM physical page 三层破坏可重建 regularity，同时保留 authorized virtual layout；这是 cost-imposition 而非 secrecy proof。

**State / data / control owner。** `PLATFORM-SECURITY` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18400v1 PDF §3 threat model; §§4–5 CloakLM three-tier design and integration`；Evaluation=`arXiv:2606.18400v1 PDF §§6–7 PyTorch/vLLM LLaMA/Qwen evaluation`；Counterevidence=`arXiv:2606.18400v1 PDF §1/§8 scope: no host OS, hypervisor, firmware or mapping-compromise defense`。Workload=`Four configurations spanning dense and MoE models at tensor parallelism 1 and 2 under PCIe-snooping and HBM-dump attacks`；Model=`Llama 3.1 8B, Qwen 3 14B and Qwen 3 MoE 30B/3B-active`；Hardware=`NVIDIA L40S GPUs with 46 GB HBM and PCIe 4.0 x16 at 32 GB/s one-way bandwidth`；Evaluator=`extraction degradation plus inference latency/throughput overhead`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** layout obfuscation增加 allocator/metadata和可能的访问开销；无法阻止已拿到映射或可改 kernel 的攻击者。


**Claim boundary。** 只使用 `https://arxiv.org/pdf/2606.18400v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Weight Streaming 的保密边界在片上明文状态才结束`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Finding Compiler-Platform Interaction Bugs in Deep Learning Pipelines via Cross-Layer Constraints](https://arxiv.org/html/2606.18421v1)

**2606.18421 — Finding Compiler-Platform Interaction Bugs in Deep Learning Pipelines via Cross-Layer Constraints**

**问题与机制变化。** DL compiler release testing 应抽取跨 model semantics、IR pass 与 hardware feasibility 的 full-stack constraints，并把 assertion pattern作为 behavior-equivalence oracle。

**State / data / control owner。** `INFER-TENSORRT-LLM` 是唯一知识 owner；`Books/part-05-inference-system/48-speculative-decoding.md; Books/part-05-inference-system/54-gpu-memory.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18421v1 §3 XCheck, §§3.1–3.3 constraint extraction, exploration and behavior differentiation`；Evaluation=`arXiv:2606.18421v1 §4.1–4.2 evaluation on TVM, ONNX-MLIR and GeneSys`；Counterevidence=`Not Disclosed — arXiv:2606.18421v1 has no dedicated limitations section; exact-v1 counterevidence is localized at three-compiler/backend scope; no dedicated limitations section`。Workload=`Generated ONNX graphs exercised against TVM, ONNX-MLIR and GeneSys`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`bug-revealing cases, late-stage reach, behavior partitions and extensibility`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 深层 constraint能发现 silent bug却增加规则维护和 false signal；2,034 cases不等于2,034已确认独立生产缺陷。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18421v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-TENSORRT-LLM` owner 为 [books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。Review notes 前命题级锚点为 `Compiler Frontend 是独立的语义故障层`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Beyond Prediction: Tail-Aware Scheduling for LLM Inference](https://arxiv.org/html/2606.18431v1)

**2606.18431 — Beyond Prediction: Tail-Aware Scheduling for LLM Inference**

**问题与机制变化。** LLM scheduler 应直接优化 tail risk，以 cache-aware preemption与完成风险信号决策，而不是依赖易漂移的 output-length point predictor。

**State / data / control owner。** `INFER-SCHEDULING` 是唯一知识 owner；`Books/part-05-inference-system/55-pd-disaggregation.md; Books/part-06-ai-infrastructure/63-gpu-scheduler.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18431v1 §3 tail-aware objective and prediction-free scheduler; §4 cache-aware preemption`；Evaluation=`arXiv:2606.18431v1 §5 production/open-trace evaluation and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.18431v1 has no dedicated limitations section; exact-v1 counterevidence is localized at trace/model/engine and overload-regime boundaries`。Workload=`production and open LLM-serving traces under tail-latency pressure`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`P95/P99 latency, throughput, preemption/recompute and cache-hit effects`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** prediction-free不等于信息免费，tail objective可能牺牲mean/fairness；受测 traces不证明所有SLO最优。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18431v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前命题级锚点为 `当前能放下，不等于未来可完成`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [ToolChain-CRC: Conformal Risk Control for Agentic AI Under Retrieval and Tool-Use Drift](https://arxiv.org/html/2606.18467v1)

**2606.18467 — ToolChain-CRC: Conformal Risk Control for Agentic AI Under Retrieval and Tool-Use Drift**

**问题与机制变化。** Tool/retrieval trajectory release 可把 step risk校准为 trajectory conformal acceptance，并用 supermartingale anytime alarm监测运行中超界；drift时必须重校准或 abstain。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18467v1 §3 trajectory risk and conformal calibration; §4 anytime monitoring and drift extension`；Evaluation=`arXiv:2606.18467v1 §5 retrieval/tool-use experiments and coverage-risk analyses`；Counterevidence=`Not Disclosed — arXiv:2606.18467v1 has no dedicated limitations section; exact-v1 counterevidence is localized at exchangeability, detector delay and tool/retrieval drift limitations`。Workload=`agent trajectories with retrieval and tool-use distribution drift`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`trajectory risk coverage, abstention, alarm delay and false-alarm behavior`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** coverage依赖 calibration分布且 alarm会 false positive；形式保证不证明 scorer或 causal harm标签正确。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18467v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `Miscoverage 要拆成 Sampling Failure 与 Selection Failure`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Ghost Vectors: Soft-Deleted Embeddings Remain Reconstructible in HNSW Vector Databases](https://arxiv.org/html/2606.18497v1)

**2606.18497 — Ghost Vectors: Soft-Deleted Embeddings Remain Reconstructible in HNSW Vector Databases**

**问题与机制变化。** Vector DB deletion 必须追踪 source→embedding→HNSW node→backup/replica 的物理生命周期；soft-delete tombstone 不是擦除，需 epoch key rotation与 signed deletion proof。

**State / data / control owner。** `AGENT-RAG` 是唯一知识 owner；`Books/part-07-agent/77-memory.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18497v1 §3 Ghost Vectors recovery methodology; §4 cryptographic epoch-deletion design`；Evaluation=`arXiv:2606.18497v1 §5 HNSW/database recovery experiments`；Counterevidence=`Not Disclosed — arXiv:2606.18497v1 has no dedicated limitations section; exact-v1 counterevidence is localized at backend/version/access model and cryptographic-key assumptions`。Workload=`soft-deleted embeddings recovered from HNSW vector databases`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`vector reconstruction/re-identification success, purge cost and key-rotation proof checks`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** physical purge或key rotation增加 rebuild、availability与密钥治理成本；受测 HNSW 恢复不覆盖所有 vector stores。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18497v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-RAG` owner 为 [books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)。Review notes 前正文 `RAG 安全必须覆盖完整状态生命周期` 已形成 owner-level 机制链；本项已实际 Integrate。

### [AI Sandboxes: A Threat Model, Taxonomy, and Measurement Framework](https://arxiv.org/html/2606.18532v1)

**2606.18532 — AI Sandboxes: A Threat Model, Taxonomy, and Measurement Framework**

**问题与机制变化。** AI sandbox 应以 threat model和 weakest-link evidence评估 fidelity、controllability、observability、containment、reproducibility与governance，不能把“进程在容器里”当成安全证明。

**State / data / control owner。** `PLATFORM-SECURITY` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18532v1 §3 sandbox threat model and taxonomy; §4 measurement framework`；Evaluation=`arXiv:2606.18532v1 §5 cross-sandbox case studies/measurements`；Counterevidence=`Not Disclosed — arXiv:2606.18532v1 has no dedicated limitations section; exact-v1 counterevidence is localized at coverage of sandbox types, attacker capability and measurement incompleteness`。Workload=`representative AI-agent sandbox designs and attack surfaces`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`six-dimension evidence matrix, containment tests and reproducibility/governance checks`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 更强隔离通常降低 fidelity/性能且扩大运维；框架只能组织证据，不能认证未知 escape或side channel不存在。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18532v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `不可信代码需要 OS 级 Effect Boundary`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [The Gate Is Only as Honest as Its Contracts: ContractGuard for the Contract Layer of Risk-Aware Causal Gating](https://arxiv.org/html/2606.18550v1)

**2606.18550 — The Gate Is Only as Honest as Its Contracts: ContractGuard for the Contract Layer of Risk-Aware Causal Gating**

**问题与机制变化。** Tool safety gate依赖 contract integrity；应对 precondition/effect/risk/authorization字段做 signed provenance、typed attestation与runtime effect verification，且 effect字段比risk标签更load-bearing。

**State / data / control owner。** `PLATFORM-SECURITY` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18550v1 §II threat model; §III two-gate taxonomy; §IV ContractGuard ladder`；Evaluation=`arXiv:2606.18550v1 §VI–VII controlled exhaustive attacker and six-model validation`；Counterevidence=`arXiv:2606.18550v1 §XI Limitations; trusted-attestation, symbolic-space and external-side-effect boundaries`。Workload=`RiskGate 100-tool registry; eight high-risk targets; 256 perturbation configurations per target; 1,898 executed configurations and 5,886 phrasing trials`；Model=`Claude Opus 4.8, Claude Sonnet 4.6, Claude Haiku 4.5, Nova Premier, Nova 2 Lite and GPT-OSS-120B`；Hardware=`Not Disclosed`；Evaluator=`injection success by guard rung, field/compound attacks, honest-contract rejection and model validation`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 完整 ladder增加签名、schema与runtime mediation成本；只在有限 contract perturbation空间给保证，attestation失陷即失效。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18550v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Policy-as-Data：可更新规则与模型判断必须分开版本化`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters](https://arxiv.org/html/2606.18600v1)

**2606.18600 — ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters**

**问题与旧路径。** As large language model (LLM) services become widely adopted, the cost of GPU resources for serving these models in cloud environments has emerged as a critical concern. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 异构 spot serving 必须联合决定 GPU pool、每 stage TP/PP 与不等层分配；中断时以输出重算恢复 request，并让 replacement initialization 与旧 pipeline 服务重叠。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** Llama-3.1-70B 与 Qwen3-32B 在 AWS L4/A10G/L40S 集群上报告吞吐与 offline/online 成本效率改善。 Method=`https://arxiv.org/html/2606.18600v1 — § exact-v1 anchor: 4 Model Placement for Heterogeneous GPUs`；Evaluation=`https://arxiv.org/html/2606.18600v1 — § exact-v1 evaluation anchor: 7 Evaluation`。Benchmark contract：model=`Llama-3.1-70B; Qwen3-32B`；hardware=`AWS L4, A10G and L40S GPUs`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`offline throughput, online TTFT/TPOT and cost efficiency under spot interruption`。

**Trade-off、failure、共存与演进。** 六天单 region 可用性和短上下文重算不能证明跨区供应或长上下文恢复；shared tensor store 也引入新的可用性 owner。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18600v1 — § exact-v1 limitation/counterevidence anchor: 8.1 Limitation`。


Claim boundary：仅 `arXiv:2606.18600v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前命题级锚点为 `Heterogeneous Offload 必须同时预算 Preemption 与 State Transfer`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training](https://arxiv.org/html/2606.18650v1)

**2606.18650 — BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training**

**问题与旧路径。** As Large Language Model (LLM) datasets scale to trillions of tokens, data selection has emerged as a critical frontier to filter out uninformative noise and construct adaptive learning trajectories. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 训练数据选择可把双层 influence objective 改写为带 Lagrange penalty 的单层目标，并让动态 reference 随 proxy trajectory 同步；online selector 用 memoryless randomized block-coordinate Frank-Wolfe。 唯一知识 owner 为 `TRAIN-DATA`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 在作者 LLM pretraining matrix 中比较 BLADE 与 influence、excess-loss baselines，并给出 first-order convergence。 Method=`https://arxiv.org/html/2606.18650v1 — § exact-v1 anchor: penalized single-level objective`；Evaluation=`https://arxiv.org/html/2606.18650v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`TinyLlama-1.1B and Llama2-7B target models with 3B/5B-token continued-pretraining budgets`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`downstream task quality and selection efficiency against influence/excess-loss baselines`。

**Trade-off、failure、共存与演进。** proxy-to-target transfer、penalty 设定与 trajectory drift 仍可能失配；收敛定理不等于目标模型质量普遍提升。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18650v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.18650v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `TRAIN-DATA` owner 为 [books/part-04-training-system/27-data.md](../../../../books/part-04-training-system/27-data.md)。Review notes 前正文 `Post-training Data Selection 是当前 Policy 的在线控制环` 已形成 owner-level 机制链；本项已实际 Integrate。

### [EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems](https://arxiv.org/html/2606.18668v1)

**2606.18668 — EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems**

**问题与旧路径。** In large-scale enterprise settings, centralized multi-agent systems (MAS) are increasingly adopted, in which a coordinator delegates user requests to lightweight, domain-specialized sub-agents. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** sub-agent abstention 应是 typed failure message，携带 ambiguous、misrouted、unsupported 等理由，供 coordinator clarification、reroute 或 fallback，而不是空响应。 唯一知识 owner 为 `AGENT-MULTI-AGENT`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 生产电商 BI assistant 的 overall response pass rate从 68.5% 提升到 78.9%。 Method=`https://arxiv.org/html/2606.18668v1 — § exact-v1 anchor: Explanatory Abstention`；Evaluation=`https://arxiv.org/html/2606.18668v1 — § exact-v1 evaluation anchor: production e-commerce assistant`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`production pass rate under structured abstention labels and rationales`。

**Trade-off、failure、共存与演进。** judge ensemble 与生产流量共享偏差且 backbone 未披露；pass rate 不证明授权、安全或跨域 calibration。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18668v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.18668v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `AGENT-MULTI-AGENT` owner 为 [books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)。Review notes 前正文 `Coordination Failure` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Understanding and Mitigating Prompt Leaking Attacks in Real-World LLM-Based Applications](https://arxiv.org/html/2606.18673v1)

**2606.18673 — Understanding and Mitigating Prompt Leaking Attacks in Real-World LLM-Based Applications**

**问题与旧路径。** Large language model (LLM)-based applications rely on system prompts to encode core logic and developer-defined constraints, making these prompts important intellectual property. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** system-prompt secrecy 不能只靠静态拒答；AREA 用可优化 soft prompt 重锚 attention，但 secret/API key 仍必须移出 prompt 并由外部 reference monitor 管理。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 测量六个平台 1,200 个应用，报告超过 80% 泄漏；AREA 的 usability 与优化开销相对防线比较。 Method=`https://arxiv.org/html/2606.18673v1 — § exact-v1 anchor: attention drift`；Evaluation=`https://arxiv.org/html/2606.18673v1 — § exact-v1 evaluation anchor: 1,200 applications`。Benchmark contract：model=`Llama-2-7B-chat-hf, Llama-3.1-8B-Instruct, Mistral-7B-Instruct, Qwen3-4B-Instruct, Qwen3-32B, Qwen2.5-72B-Instruct and Llama-3.3-70B-Instruct`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`prompt leakage resistance, usability and optimization overhead over 1,200 applications`。

**Trade-off、failure、共存与演进。** attention drift 是受测模型解释，不证明所有泄漏因果；soft prompt 无法把已放入上下文的密钥变成真正 secret。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18673v1 — § exact-v1 limitation/counterevidence anchor: limitations`。


Claim boundary：仅 `arXiv:2606.18673v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Privacy Boundary 必须覆盖全部 Observable Channels`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Stealthy World Model Manipulation via Data Poisoning](https://arxiv.org/html/2606.18697v1)

**2606.18697 — Stealthy World Model Manipulation via Data Poisoning**

**问题与旧路径。** Model-based learning agents use learned world models to predict future states, plan actions, and adapt to new environments. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** world-model fine-tuning data 是 planning control surface：SWAAP 先优化近似 clean dynamics 的低回报目标模型，再以 stealth-constrained gradient matching 修改有限 transition targets。 唯一知识 owner 为 `MULTIMODAL-WORLD-MODELS`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 连续控制任务上评估 planning return、poison detectability，并测试 residual/CUSUM/TRIM 防线。 Method=`https://arxiv.org/html/2606.18697v1 — § exact-v1 anchor: two-stage data poisoning framework`；Evaluation=`https://arxiv.org/html/2606.18697v1 — § exact-v1 evaluation anchor: continuous-control tasks`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`planning return, poison detectability and defense response across three pipeline stages`。

**Trade-off、failure、共存与演进。** 只击败 non-adaptive defenses；低 prediction error 不等于 transition 正确，真实环境 feedback 仍是权威。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18697v1 — § exact-v1 limitation/counterevidence anchor: limitations`。


Claim boundary：仅 `arXiv:2606.18697v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `MULTIMODAL-WORLD-MODELS` owner 为 [books/part-03-multimodal-world-models/25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。Review notes 前正文 `Action-conditioned World Model 要先通过 Integrity Gate` 已形成 owner-level 机制链；本项已实际 Integrate。

### [ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving](https://arxiv.org/html/2606.18741v1)

**2606.18741 — ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving**

**问题与旧路径。** Current large language model (LLM) inference systems universally deploy ultra-large-scale models using a combination of Tensor Parallelism (TP) and Pipeline Parallelism (PP). 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** runtime parallelism 变更要把 topology 与 request state 解耦，并以二维 KV migration 将旧 TP/PP shard 映射到新 topology，再原子切换流量。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 7B–70B models 的多数 topology switch 为 1–7 秒，并报告动态 workload 的 TTFT、TPOT 与 output throughput。 Method=`https://arxiv.org/html/2606.18741v1 — § exact-v1 anchor: two-dimensional KV cache migration`；Evaluation=`https://arxiv.org/html/2606.18741v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`Llama2-7B, Qwen3-30B-A3B, DeepSeek-R1-Distill-Qwen-32B and Llama2-70B`；hardware=`NVIDIA H100 and RTX 5090 platforms`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`reconfiguration downtime, TTFT, TPOT and output throughput`。

**Trade-off、failure、共存与演进。** KV migration 与双份资源会制造瞬时带宽/容量峰值；作者模型与网络不证明任意拓扑可无损切换。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18741v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.18741v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前命题级锚点为 `DP↔TP 切换是带版本的在线状态转换`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [What Must Generalist Agents Remember?](https://arxiv.org/html/2606.18746v1)

**2606.18746 — What Must Generalist Agents Remember?**

**问题与旧路径。** This paper develops a formal account of what generalist agents must store in memory in order to act near-optimally across multiple environments and goals. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 若相同 observation bottleneck 在不同 domain 需要不兼容 action，近最优 policy 必须保存可区分的 memory distribution；足够的 value 信息还可近似重建局部 transition dynamics。 唯一知识 owner 为 `AGENT-MEMORY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 给出 separation theorem 与 transition reconstruction 条件，而非经验 leaderboard。 Method=`https://arxiv.org/html/2606.18746v1 — § exact-v1 anchor: separation theorem`；Evaluation=`https://arxiv.org/html/2606.18746v1 — § exact-v1 evaluation anchor: transition-model reconstruction`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`theorem premises and approximation error for domain disambiguation and local dynamics reconstruction`。

**Trade-off、failure、共存与演进。** 定理依赖形式化 observation/domain 假设；可重建局部 dynamics 不代表 memory 内容真实、授权或可长期维护。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18746v1 — § exact-v1 limitation/counterevidence anchor: assumptions`。


Claim boundary：仅 `arXiv:2606.18746v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `AGENT-MEMORY` owner 为 [books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)。Review notes 前正文 `Context 与 Memory 的状态边界` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/html/2606.18810v1)

**2606.18810 — Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards**

**问题与旧路径。** Reinforcement learning with verifiable rewards (RLVR) has driven substantial progress in training LLMs for reasoning tasks, but representative methods such as GRPO assign uniform credit across all tokens, wasting gradient on routine tokens while under-crediting pivotal reasoning steps. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** SC-GRPO 用 verified trajectory 条件化前后 token KL 作为 GRPO gradient 权重，让 policy 自己暴露 pivotal token，避免外部 PRM/teacher。 唯一知识 owner 为 `TRAIN-GRPO`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 五个 math、code、agentic benchmarks 上相对 GRPO 与 DAPO 报告平均改善和 OOD 结果。 Method=`https://arxiv.org/html/2606.18810v1 — § exact-v1 anchor: Self-Conditioned GRPO`；Evaluation=`https://arxiv.org/html/2606.18810v1 — § exact-v1 evaluation anchor: five benchmarks`。Benchmark contract：model=`Qwen3-1.7B-Base; DeepSeek-R1-Distill-Qwen-1.5B; experiments are limited to models at most 8B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`task accuracy and OOD performance against GRPO, DAPO and OPD`。

**Trade-off、failure、共存与演进。** self-conditioned teacher 与 student 共偏；KL 大小不自动等于因果 credit，verified final answer 也可能掩盖错误路径。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18810v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.18810v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `TRAIN-GRPO` owner 为 [books/part-04-training-system/33-grpo.md](../../../../books/part-04-training-system/33-grpo.md)。Review notes 前命题级锚点为 `从序列 Reward 到受约束的 Token Credit`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents](https://arxiv.org/html/2606.18829v1)

**2606.18829 — GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents**

**问题与旧路径。** Memory benchmarks for LLM agents largely assume single-user settings, leaving shared assistants for hospitals, workplaces, campuses, and households understudied. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 共享 memory 的 admission/read/delete 必须按 principal、role、scope 和 relationship 授权，并把 utility、ACL leakage 与 active forgetting 作为三个独立 Gate。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** GateMem 跨医疗、办公、教育、家庭；多种 memory baselines/backbones 均未同时获得强 utility、ACL 与 forgetting。 Method=`https://arxiv.org/html/2606.18829v1 — § exact-v1 anchor: multi-principal shared-memory agents`；Evaluation=`https://arxiv.org/html/2606.18829v1 — § exact-v1 evaluation anchor: diverse baselines and backbone models`。Benchmark contract：model=`GPT-5.4, DeepSeek-V4-Pro, Llama-4-Maverick, GPT-5-mini, GPT-4o-mini and Gemini-2.5-Flash-Lite`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`legitimate utility, contextual access-control leakage and post-deletion active forgetting`。

**Trade-off、failure、共存与演进。** structured judge 与合成 episode 不证明真实机构合规；long-context 的较高 governance score 伴随 token cost，external memory 仍可能泄漏。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18829v1 — § exact-v1 limitation/counterevidence anchor: limitations`。


Claim boundary：仅 `arXiv:2606.18829v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Shared Memory 必须同时通过 Utility、ACL 与 Forgetting Gate`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents](https://arxiv.org/html/2606.18847v1)

**2606.18847 — WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents**

**问题与旧路径。** To assist humans over extended periods in real homes, embodied agents must remember user routines, world states, and past interactions. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 长期 embodied memory 需保存 visibility-aware observation、action-native state trail 与执行反馈，且旧 state 被覆盖时保留时间身份，供 planning 消费。 唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** WorldLines 同时评 Memory QA 与 Embodied Task Planning；ObsMem 对 partial observability、overwritten state 进行比较。 Method=`https://arxiv.org/html/2606.18847v1 — § exact-v1 anchor: WorldLines`；Evaluation=`https://arxiv.org/html/2606.18847v1 — § exact-v1 evaluation anchor: ObsMem`。Benchmark contract：model=`google/gemini-3.5-flash answer generator; GPT-4o judge; GPT-4o-mini question generator`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`Memory QA and Embodied Task Planning over evidence-linked household traces`。

**Trade-off、failure、共存与演进。** benchmark household traces 不是开放世界；observer-grounded memory 仍可能漏看并把推断状态误写成事实。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18847v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.18847v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `MULTIMODAL-EMBODIED-VLA` owner 为 [books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。Review notes 前命题级锚点为 `Policy 内部的 Latent Memory 是 Episode State，不是 Agent Memory`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts](https://arxiv.org/html/2606.18967v1)

**2606.18967 — EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts**

**问题与旧路径。** Reinforcement learning (RL) has become a representative post-training paradigm for LLMs, enabling strong reasoning and agentic capabilities. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** RL rollout 的 draft policy 可由当前 policy 自身派生，但 acceptance、KV/state rollback 与训练版本 identity 必须共同绑定，避免把 serving speculation 当成离策略数据复用。 唯一知识 owner 为 `INFER-SPECULATIVE-DECODING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 在 RL rollout workloads 上报告 self-speculative speedup、acceptance 与 training quality。 Method=`https://arxiv.org/html/2606.18967v1 — § exact-v1 anchor: system-aware self-speculative decoding`；Evaluation=`https://arxiv.org/html/2606.18967v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`Qwen2.5-7B, Qwen2.5-14B and Llama3.1-8B-Instruct with quantized self-drafters`；hardware=`single NVIDIA A100-80GiB SXM in the decode-cost study`；precision=`FP16 target inference; W4/W8 weight-quantized self-drafters`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`rollout throughput, acceptance and downstream RL quality`。

**Trade-off、failure、共存与演进。** acceptance 随 policy update 漂移；额外 draft computation 和 rollback bookkeeping 可能抵消收益，且不改变 reward validity。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18967v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.18967v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `INFER-SPECULATIVE-DECODING` owner 为 [books/part-05-inference-system/48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md)。Review notes 前命题级锚点为 `Agent Workflow 让 Proposal Budget 与 Residual State 都变成动态对象`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Spotlight: Synergizing Seed Exploration and Spot GPUs for DiT RL Post-Training](https://arxiv.org/html/2606.19004v1)

**2606.19004 — Spotlight: Synergizing Seed Exploration and Spot GPUs for DiT RL Post-Training**

**问题与旧路径。** Reinforcement learning (RL) post-training of Diffusion Transformers (DiTs) is prohibitively expensive, requiring thousands of high-end GPUs. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** DiT RL post-training 可把探索 seed 与 spot GPU availability 联合调度，把可重放 seed state 作为 preemption recovery unit。 唯一知识 owner 为 `PLATFORM-GPU-SCHEDULER`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 比较 seed exploration quality、GPU utilization、成本与训练结果。 Method=`https://arxiv.org/html/2606.19004v1 — § exact-v1 anchor: Seed Exploration and Spot GPUs`；Evaluation=`https://arxiv.org/html/2606.19004v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`Qwen-Image`；hardware=`4 reserved-node H100 GPUs plus 8 H100 GPUs on four spot nodes`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`training reward/quality, GPU utilization and spot cost`。

**Trade-off、failure、共存与演进。** spot reclaim 与 seed replay 会改变样本时序；结果限于 DiT RL，不能外推 LLM RL 或硬实时 SLO。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19004v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.19004v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `PLATFORM-GPU-SCHEDULER` owner 为 [books/part-06-ai-infrastructure/63-gpu-scheduler.md](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)。Review notes 前命题级锚点为 `可回收资源需要 Lease 与 Reclaim Protocol`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [FoMoE: Breaking the Full-Replica Barrier with a Federation of MoEs](https://arxiv.org/html/2606.19025v1)

**2606.19025 — FoMoE: Breaking the Full-Replica Barrier with a Federation of MoEs**

**问题与旧路径。** Pre-training Large Language Models (LLMs) typically demands large-scale infrastructure with tightly coupled hardware accelerators. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 低带宽跨站 MoE 训练不应让每个 site 持有 full replica；FoMoE 分区 expert layers、部分复制 experts，并让 local training 对 non-resident experts 执行 skip-token，再按较低频率同步。 唯一知识 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 通信相对高效 baseline 最多降 1.42x、相对 DDP 降 45.44x，skip-token 吞吐最高 1.4x；100B 只由 cost model 投影。 Method=`https://arxiv.org/html/2606.19025v1 — § exact-v1 anchor: partitioning expert layers across workers`；Evaluation=`https://arxiv.org/html/2606.19025v1 — § exact-v1 evaluation anchor: FoMoE Scalability & Resource Consumption`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`communication volume, local-training throughput and routing stability; 100B results are modeled projections`。

**Trade-off、failure、共存与演进。** non-resident expert skip 会改变本地训练分布，routing stability 只在受测 regimes 成立；100B projection 不是实测，WAN failure/straggler 未闭合。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19025v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.19025v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `TRAIN-DISTRIBUTED-TRAINING` owner 为 [books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)。Review notes 前正文 `Expert Parallel 从静态放置到动态 Token + Weight Spill` 已形成 owner-level 机制链；本项已实际 Integrate。

### [PhantomSkill: Malicious Code Injection in Agent Skill Ecosystems](https://arxiv.org/html/2606.19191v1)

**2606.19191 — PhantomSkill: Malicious Code Injection in Agent Skill Ecosystems**

**问题与旧路径。** Agent skills allow LLM-based coding agents to acquire domain-specific capabilities from third-party packages, but they also introduce a new supply-chain attack surface. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** skill admission 不能只读 SKILL.md；必须审 auxiliary resources、triggerable vulnerabilities 与 runtime effects，并在沙箱中验证 benign utility 与恶意 side effect。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** VulMask 跨 host skills、四类攻击、Cursor backbones 与多个 automated reviewers；GPT-5.5 设置 ASR 58.8%、warning 11.4%。 Method=`https://arxiv.org/html/2606.19191v1 — § exact-v1 anchor: 3 Threat Model`；Evaluation=`https://arxiv.org/html/2606.19191v1 — § exact-v1 evaluation anchor: 5 Evaluation`。Benchmark contract：model=`GPT-5.5, GLM-4.7-Flash and Qwen3-Coder-30B-A3B-Instruct; Opus-4.7, GLM-4.7-Flash and Qwen3-Coder-30B-A3B-Instruct for cross-generator transfer; Cursor backends additionally include Opus-4.7`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`attack success, warning/detection and benign utility across four attack goals`。

**Trade-off、failure、共存与演进。** 攻击 corpus 与触发器由作者构造；静态扫描漏报不证明 runtime containment 无效，检测率也不等于安全。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19191v1 — § exact-v1 limitation/counterevidence anchor: 6 Discussion`。


Claim boundary：仅 `arXiv:2606.19191v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Skill Poisoning 的真值是 Side Effect，而不是是否被调用`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Runtime Compliance Verification for AI Agents](https://arxiv.org/html/2606.19242v1)

**2606.19242 — Runtime Compliance Verification for AI Agents**

**问题与旧路径。** AI agents now handle personal data through tool use, function calls, and multi turn dialogue, which can create obligations under the General Data Protection Regulation (GDPR). 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** Agent compliance 应在每次 tool/message effect 前由外部 runtime monitor 检查 temporal/policy state，而非要求 LLM 自述合规。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 在作者 policies、agent traces 与 violation cases 上评 runtime verification。 Method=`https://arxiv.org/html/2606.19242v1 — § exact-v1 anchor: Runtime Compliance Verification`；Evaluation=`https://arxiv.org/html/2606.19242v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`policy-violation detection and runtime enforcement outcomes`。

**Trade-off、failure、共存与演进。** 形式化 policy 不覆盖未建模 effect，monitor 自身可能成为延迟或可用性瓶颈。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19242v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.19242v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Behavioral Contract 把 Invariant、Drift 与 Recovery 变成运行期状态`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Detecting Hidden ML Training With Zero-Overhead Telemetry](https://arxiv.org/html/2606.19262v1)

**2606.19262 — Detecting Hidden ML Training With Zero-Overhead Telemetry**

**问题与旧路径。** Hardware-enabled monitoring of GPU workloads underpins many proposals for AI compute governance, but if developers can defeat monitoring mechanisms, such schemes are unworkable. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** hidden training detection 可读取已有 accelerator telemetry 的 phase、memory/compute 与 collective signatures，保持 observe-only，不向 workload 注入探针。 唯一知识 owner 为 `PLATFORM-MONITORING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 在多种 ML/non-ML workloads 与 hardware traces 上报告检测质量及 zero-overhead claim。 Method=`https://arxiv.org/html/2606.19262v1 — § exact-v1 anchor: Zero-Overhead Telemetry`；Evaluation=`https://arxiv.org/html/2606.19262v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`Not Disclosed`；hardware=`nine NVIDIA GPU models across four architecture generations`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`hidden-training detection, false positives and telemetry overhead`。

**Trade-off、failure、共存与演进。** 共享 GPU、融合 kernel 与新 compiler 会造成概念漂移；无额外探针不等于 telemetry 免费或不可规避。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19262v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.19262v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `PLATFORM-MONITORING` owner 为 [books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)。Review notes 前命题级锚点为 `Host 与 Device 都不可信时，用计算挑战构造旁路遥测`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [TurboServe: Serving Streaming Video Generation Efficiently and Economically](https://arxiv.org/html/2606.19271v1)

**2606.19271 — TurboServe: Serving Streaming Video Generation Efficiently and Economically**

**问题与旧路径。** Streaming video generation is emerging as a new serving workload in which users interact with long-lived sessions that generate video progressively, chunk by chunk. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** streaming video generation 应以 chunk deadline 为调度单位，联合决定 GPU residency、跨 chunk pipeline 与质量/成本降级，而不是只优化整段 makespan。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** TurboServe 报告 worst-case per-chunk latency 降 37.5%、平均 GPU cost 降 37.2%。 Method=`https://arxiv.org/html/2606.19271v1 — § exact-v1 anchor: Streaming Video Generation`；Evaluation=`https://arxiv.org/html/2606.19271v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`Not Disclosed`；hardware=`GPU clusters with up to 64 NVIDIA B300 GPUs`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`worst-case per-chunk latency, end-to-end quality and GPU operating cost`。

**Trade-off、failure、共存与演进。** 作者 workloads/GPU matrix 不证明交互视频通用 SLO；跨 chunk state 与 quality degradation 仍需独立验收。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19271v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.19271v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前正文 `迭代生成与流式会话需要显式 Progress State` 已形成 owner-level 机制链；本项已实际 Integrate。

<!-- full-raw-recovered-evidence:start -->

### [Gaussian Mixture Attention: Linear-Time Sequence Mixing via Probabilistic Latent Routing](https://arxiv.org/html/2606.18283v1)

**问题、机制与 owner。** Gaussian Mixture Attention 以 K 个 learned mixture components 作为 latent routing/memory slots，用 responsibility overlap 代替显式 N×N affinity，将固定 K 下的激活存储降为 O(NK)；它是 softmax attention/SSM 的替代分支。 唯一知识 owner 为 `MODEL-SELF-ATTENTION`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3.1–3.3 Methodology；Experiments`。低秩、非负 responsibility affinity 限制表达；当前 causal 实现落后 optimized SDPA/Mamba，K、训练稳定与 kernel 成熟度决定是否值得采用。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-02-model/14-self-attention.md](../../../../books/part-02-model/14-self-attention.md) 在 Review notes 前已写入 latent routing、model/runtime/release ownership、低秩瓶颈代价与 softmax/mixed-layer fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior](https://arxiv.org/html/2606.18322v1)

**问题、机制与 owner。** SAE feature 被 clamp 后行为可通过 reconstruction residual 或其他路径恢复；线性可读出/稀疏解释只能作为 sensor，不能直接证明对应因果机制已被删除。 唯一知识 owner 为 `WORLDVIEW-NEURAL-NETWORK-LEARNING`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§4 Post-Intervention Recovery；§5–6 Experiments/Case Study`。结果绑定所测 SAE、行为和 intervention；恢复不证明所有解释无效，但要求独立 behavioral counterfactual 与完整 residual accounting。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-01-worldview/05-what-neural-networks-learn.md](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 在 Review notes 前的 `可读出不等于可拆卸或可控制` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [From Sparse Features to Trustworthy Proxies: Certifying SAE-Based Interpretability](https://arxiv.org/html/2606.18383v1)

**问题、机制与 owner。** 把 SAE 当可解释 proxy 时，应将 proxy risk、reconstruction gap、model–proxy mismatch 与 complexity 一起形成证书；稀疏性或可读性本身不提供可信度。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3–4 risk formulation；theoretical bound；experiments`。证书依赖分布、loss、reconstruction 和 complexity 假设；有限 proxy guarantee 不等于原模型的机制真值或生产安全。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前的 `Activation Oracle 的 Confidence 也要校准` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [PreUnlearn: Auditing Collateral Knowledge Damage Before Large Language Model Unlearning](https://arxiv.org/html/2606.18473v1)

**问题、机制与 owner。** unlearning 前应按语义距离和知识层次预测 collateral damage，并在 target removal 外冻结 retained controls；局部删除效果不能掩盖跨域能力损伤。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3 Three-layer Impact；§4 Pre-unlearn Auditing；Experiments`。影响预测是风险 sensor，不证明因果或不可恢复删除；作者模型/数据外需重新校准，最终仍要 matched retrain/behavior audit。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前的 `不再回答不是 Deletion Evidence` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [SFT Overtraining Predicts Rank Inversion via Entropy Collapse Under RLVR](https://arxiv.org/html/2606.18487v1)

**问题、机制与 owner。** 过度 SFT 会压低 policy entropy，使后续 RLVR 的模型排序反转；SFT checkpoint、entropy/support 与 rollout budget 必须共同作为 post-training admission state。 唯一知识 owner 为 `TRAIN-GRPO`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`analysis of SFT overtraining；RLVR rank-inversion experiments`。相关性和作者 task/model 不证明统一 entropy threshold；降低 SFT 或增加采样可能伤害稳定性，需 held-out outcome gate。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-04-training-system/33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) 在 Review notes 前的 `Exploration 必须与 Verified Progress 对齐` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [RouteJudge: An Open Platform for Reproducible and Preference-Aware LLM Routing](https://arxiv.org/html/2606.18774v1)

**问题、机制与 owner。** router 评估必须在同一 model pool 与 budget 下比较 routing strategy，并保存 query、decision、response、preference、cost、latency 与 task metadata；用户 pairwise preference 只拥有受控相对证据。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`RouteJudge protocol；ORBIT interfaces/submission workflow`。在线用户偏好有 selection/position/population bias，平台结果不证明离线或生产通用最优；模型池与成本改变需重评。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前的 `Router 上线需要可拒绝的 Gain Certificate` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architecture for LLM Agents](https://arxiv.org/html/2606.18947v1)

**问题、机制与 owner。** search grounding 从模型 provider 内部拆为 MCP-compatible gateway，使 provider routing、source rendering、fallback、depth 与 cache 可独立版本化；reader 只消费带 provenance 的 evidence。 唯一知识 owner 为 `AGENT-RAG`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3 Native Search Challenge；§4 DSG；§5 Evaluation`。成本/准确率数据绑定作者 providers、benchmarks 与 e-commerce workload；外置 search 会增加 gateway、cache staleness、privacy 和 prompt-injection surface，native search 在 recency 任务仍可能更强。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md) 在 Review notes 前的 `Retrieval Control 应成为 Reader 外部的 Typed State` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation](https://arxiv.org/html/2606.18960v1)

**问题、机制与 owner。** 遮挡和 wrist-camera 运动使当前 observation 不足时，world model 需要以 4D surfel memory 保存何时何地观察到场景，并按未来 action 检索历史；memory 是可修订 environment state，不是普通视频上下文。 唯一知识 owner 为 `MULTIMODAL-WORLD-MODELS`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3.2 W-VMem；Experiments`。几何重建/检索依赖 calibration 与 surfel quality；14.5% correlation 和 58→72% 只属于作者 manipulation tasks，simulated rollout 不能替代真机安全。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-03-multimodal-world-models/25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 在 Review notes 前的 `从全历史条件到有界 History Bank 与 Self-rollout Distillation` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [TRAP: Benchmark for Task-completion and Resistance to Active Privacy-extraction](https://arxiv.org/html/2606.18996v1)

**问题、机制与 owner。** Agent privacy 评估必须同时测 task completion 与主动 extraction resistance；若敏感字段与 task context 共处同一可见状态，soft instruction 无法提供结构隔离，需字段级 authority 与最小披露。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`TRAP benchmark/method；cross-model evaluation`。benchmark 攻击与合成任务不代表真实发生率；拒答率不是隐私证明，结构隔离也需 tool/effect path 验证。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 在 Review notes 前的 `Privacy Boundary 必须覆盖全部 Observable Channels` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Lifecycle-Aware Dynamic Analysis for Secure ML Model Execution](https://arxiv.org/html/2606.19023v1)

**问题、机制与 owner。** 静态、格式特定的 model scanner 只能发现已知 artifact pattern；动态防护应按 load、deserialize、initialize、execute 等 lifecycle phase 建立允许的 host-effect profile，并以 syscall/side-effect deviation 拦截未知 exploitation path。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`official v1 PDF：method/lifecycle model；77,974 artifacts + 31 CVE PoCs + 334-model evaluation`。动态分析覆盖的是所观测 host effects，不证明模型语义安全；sandbox/monitor 可被规避，framework/OS 更新会漂移 baseline，并增加运行成本与 false positive。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 在 Review notes 前已写入 lifecycle host-effect profile、安全 owner、baseline drift 代价与隔离/受支持格式 fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [Quantifying and Auditing LLM Evaluation via Positive--Unlabeled Learning](https://arxiv.org/html/2606.19057v1)

**问题、机制与 owner。** 选择性人工监督形成 positive–unlabelled 而非普通二分类数据；固定 embedding、partial optimal transport 与 relabelling 可审计 judge 偏差，但必须公开 class-prior/identifiability 与 calibration。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3 Methodology；§4 Guarantee；§5 Experiments`。理论依赖几何分离与可靠正例；embedding drift、label selection 和 verbosity correlation 会破坏解释，不能把校正后分数当真值。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前的 `当只有少量确定正例而未标注集混合正负时，evaluation audit 可用 positive-unlabeled inference 估计隐藏错误率` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [A Technical Taxonomy of LLM Agent Communication Protocols](https://arxiv.org/html/2606.19135v1)

**问题、机制与 owner。** Agent communication protocol 不能只按 transport 命名；应沿 counterparty、payload、interaction state、discovery 与 schema 分层，使 message identity、capability negotiation、session lifecycle 与 error semantics 可组合。 唯一知识 owner 为 `AGENT-MCP`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§4 Taxonomy Development；protocol comparison/case studies`。taxonomy 是分析框架而非统一标准；不同协议的 auth、delivery、ordering、backpressure 与 effect semantics 仍需各自验证，不能从分类推导互操作性。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-07-agent/83-mcp.md](../../../../books/part-07-agent/83-mcp.md) 在 Review notes 前已写入五维协议 taxonomy、adapter/session/policy ownership、映射不完整风险与拒绝连接 fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [Pulse: Training Acceleration for Large Diffusion Models with Automatic Pipeline Parallelism](https://arxiv.org/html/2606.19163v1)

**问题、机制与 owner。** Diffusion model 的 skip connections 让普通连续层切分产生跨 stage 回传和不平衡；pipeline planner 应把 skip-connected layers 的 colocate constraint、partition cost 与 schedule 一起求解，再由 hybrid tuner验证。 唯一知识 owner 为 `TRAIN-PIPELINE-PARALLEL`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§II-C/D problem；§IV skip-aware partition；evaluation`。ILP/DP 与收益绑定作者 DiT、拓扑和训练配置；强制 colocate 可能造成 compute imbalance，模型结构或带宽改变需重规划，不能外推所有 diffusion training。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-04-training-system/38-pipeline-parallel.md](../../../../books/part-04-training-system/38-pipeline-parallel.md) 在 Review notes 前已写入 skip-aware colocate constraint、graph/performance ownership、求解代价与连续切分 fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [User as Engram: Internalizing Per-User Memory as Local Parametric Edits](https://arxiv.org/html/2606.19172v1)

**问题、机制与 owner。** per-user memory 若以整份 LoRA 持有，会让身份事实、推理能力和 base drift 混合。Engram 将用户内容写入局部 hash-addressed rows，共享 adapter 只承载 reasoning，形成可寻址、可组合、可撤销的 parametric memory boundary。 唯一知识 owner 为 `AGENT-MEMORY`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3 LoRA contamination；§4 User as Engram；Experiments`。hash collision、row growth、base/model migration 与删除验证仍是新状态；作者实验不证明任意用户知识可忠实写入，也不替代 external memory/provenance。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 在 Review notes 前已写入 hash-addressed rows、memory/model ownership、collision/migration/deletion 边界与 external-memory fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [DreamReasoner-8B: Block-Size Curriculum Learning for Diffusion Reasoning Models](https://arxiv.org/html/2606.19257v1)

**问题、机制与 owner。** dLLM block-size curriculum 将训练从小 block 的局部依赖逐步扩到大 block 并行推理；block size 是 objective/sampler identity，不只是推理超参数。 唯一知识 owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`official v1 abstract/PDF method and evaluation`。8B 模型和所测 reasoning tasks 不证明 curriculum 通用；大 block 会增加联合错误与训练不稳定，固定 block/AR 在依赖强时仍可取。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 在 Review notes 前的 `Parallel Progress 与 Active Compute 是两条独立成本轴` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Beyond the Current Observation: Evaluating Multimodal Large Language Models in Controllable Non-Markov Games](https://arxiv.org/html/2606.19338v1)

**问题、机制与 owner。** 非 Markov 游戏把当前 observation 相同但 history 不同的 paired states 固定，从而用 Memory Gap 分离感知/推理能力与状态记忆；环境 truth owner 必须保存 hidden state 与 duel pairing。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3 Benchmark Design/Memory Gap；§4 Experiments`。受控游戏不代表开放世界，Memory Gap 仍混入 policy/exploration；配对覆盖不足不能证明模型没有记忆。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前的 `Agent 与 World Model 的证据要分层闭合` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Native Active Perception as Reasoning for Omni-Modal Understanding](https://arxiv.org/html/2606.19341v1)

**问题、机制与 owner。** omni-modal agent 将 observation–thought–action 与 persistent textual memory组成 POMDP loop，主动选择下一观测而非被动消费固定 context；planning owner决定信息获取，memory只保存有 provenance 的结果。 唯一知识 owner 为 `AGENT-PLANNING`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`official v1 method/benchmark sections`。作者环境与模型不证明主动感知总优于一次性输入；额外动作、延迟、误观测与 memory pollution 要进入预算和停止条件。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-07-agent/79-planning.md](../../../../books/part-07-agent/79-planning.md) 在 Review notes 前的 `Active Perception 是信息价值决策，不是固定多看几步` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

<!-- full-raw-recovered-evidence:end -->


### Books / semantic audit

Fresh-context 作者侧审计以 level-2 `Review notes` 为正文边界。45 个冻结候选中，14 项已在正文形成完整机制链，31 项有不依赖 source trace 的命题级覆盖，writeback queue=0。独立写后复核重新读取正文并核对 marker 位置；章末 trace、source marker 和 proposal artifact 均未被用作正文落地证明。

## 5. 缺口与下一步

终态保留项：`Project Fetch: Phase two` 的官方页面只给出 `2026-06-18`，无法判定它是在本窗结束 `2026-06-18T09:00:00+08:00` 之前还是之后发布；本项不用于正面证据、Books 或无遗漏断言。定点重开条件：取得官方发布时间与时区，或带精确时间的官方公告。取得前不归入 06-18 或 06-19，不评分、不进入 Books。

除此以外，本日 raw denominator 与 recovered candidate 的 exact-v1 Evidence Review 已闭合；ordinary evidence pending=0，Books writeback queue=0。

## 6. 复核

当前来源再认证复核者：\`june_11_20_recert\`（独立于原报告作者）。当前合同来源再认证补齐十三个官方 Daily 源；识别同一项 Anthropic owner-day 外部材料缺口并终态保留，未把日期不明材料用于候选、评分或 Books。

复核者：独立 fresh-context reviewer（非作者侧）

结论：通过

Candidate/Evidence/Books 通过；Coverage 以一项已记录的外部日期缺口安全终结。

复核重新检查 525=45 Candidate+480 audited Close、45 项 Books disposition（14 Integrate/31 Existing）、13 项本轮新增 binding 中属于本日的 5 项，以及两套 validator 与限定 diff。5/5 marker 均位于首个顶层 Review notes 前，正文均覆盖旧约束→机制→owner→trade-off/failure→fallback。当前 source recert 新增的是 owner-day material gap，不是可执行审读 pending。
