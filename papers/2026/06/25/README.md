# Daily Research — 2026-06-25

**规范：** V3
**窗口：** 2026-06-24T09:00:00+08:00 ～ 2026-06-25T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T09:36:20+08:00

## 1. 结论

本窗恢复 526 个 canonical arXiv identity，并补入 1 个落窗的机构源 Source Family；逐项以完整题摘按当前“大模型与大模型基础设施”贡献门槛重审，冻结 28 个候选。旧 V2.1 的 65 个候选只作 provenance，38 项因垂直任务、领域 benchmark、局部表示/方法或仅能映射 ROADMAP 而在候选前关闭；没有以 Books trace 反向证明准入。

本轮候选前关闭（不计入 Candidate Denominator）：

- `2606.25082` / `SF-2026-ARXIV-2606-25082` — 通用 AI/ML job 的单 MIG simulation/RL repartitioning；题摘没有 LLM token、KV、parallel state 或大模型 lifecycle contract
- `2606.25285` / `SF-2026-ARXIV-2606-25285` — EPTS/MS-HiLoRA 与 feature mixer 是多稀疏度局部模型压缩 recipe；可部署多个 sparsity 不等于 runtime/serving control contract
- `2606.25453` / `SF-2026-ARXIV-2606-25453` — EmuGEMM 面向科学计算高精度 GEMM 的低精度 Tensor Core 精度模拟；不是大模型或大模型基础设施特有的长期机制
- `2606.25608` / `SF-2026-ARXIV-2606-25608` — 把既有 HybridRAG、KG 与 Multi-LLM 组合用于德国 IT-Grundschutz 认证；贡献对象是垂直认证流程，没有新的通用 security authority/effect/release 机制

候选均具备与其证据类型匹配的 Source Review；论文复用可核实的 exact-v1 Method / Evaluation / Limitations 定位，官方发布则严格限制到公开的 release/security contract。Books 结果为 1 项整合、27 项已有覆盖；本次同步没有修改 Books、LEARNING_STATE 或跨日索引。

2026-09-14 按当前来源清单重放 13 个机构每日源并复用仍匹配的 arXiv / exact-v1 / Evidence / Books 证据。机构源补查恢复 Gemini computer-use 的安全契约并重开为候选；独立复核纠正了 DeepSeek-V4 的日期线索：官方首次发布是 2026-04-24，不属于本窗。冻结分母由 27 调整为 28。详细过程见 [当前合同再认证](../_sources/daily-20260625/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [当前合同再认证](../_sources/daily-20260625/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列与窗口定点检索；本窗无范围内新增 | 已检查 | 无 |
| SRC-ANTHROPIC | [当前合同再认证](../_sources/daily-20260625/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-GOOGLE-AI | [当前合同再认证](../_sources/daily-20260625/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：Gemini 3.5 Flash computer-use 于 06-25 00:00 北京时间落窗；其 adversarial training 与两项 enterprise safeguard 改变 Agent action/security release contract，已纳入候选 | 已检查 | 无 |
| SRC-META-AI | [当前合同再认证](../_sources/daily-20260625/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-QWEN | [当前合同再认证](../_sources/daily-20260625/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方博客时间序列；本窗无新 family / 重要 revision | 已检查 | 无 |
| SRC-DEEPSEEK | [当前合同再认证](../_sources/daily-20260625/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 V4 / V4 Preview 与 API changelog 的首次发布为 2026-04-24；本窗无新增 | 已检查 | 无 |
| SRC-MOONSHOT | [当前合同再认证](../_sources/daily-20260625/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：Kimi Blog 与官方仓库发布时序；本窗无范围内新增 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | [当前合同再认证](../_sources/daily-20260625/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 publicList 8/8 条按展示首发日期检查；本窗无范围内新增 | 已检查 | 无 |
| SRC-ZAI | [当前合同再认证](../_sources/daily-20260625/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [当前合同再认证](../_sources/daily-20260625/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research、论文目录与发布页；本窗无范围内新增 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [当前合同再认证](../_sources/daily-20260625/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方技术博客与仓库发布时序；本窗无范围内新增 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [当前合同再认证](../_sources/daily-20260625/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Paper / Blog 与仓库；本窗无范围内新增 | 已检查 | 无 |
| SRC-MINIMAX | [当前合同再认证](../_sources/daily-20260625/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：中英文博客与 Agent Tech Blog；相邻条目为 06-09/06-01，本窗无新增 | 已检查 | 无 |
| SRC-ARXIV | [canonical raw inventory](../_sources/daily-20260625/canonical-raw-identity-inventory-v2.1.json.gz)；526 个 owner identity 完成题摘筛选；[V3 audit](../_sources/daily-20260625/v3-admission-audit-20260910.json) | 已检查 | 无 |

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability。本轮独立复核已按当前候选实际新增的命题逐项重评，不沿用旧分数，也不因既有证据已经深入审阅而倒推高分：单一 owner 内的局部机制按单组件 reach 计，只有原文实际跨越系统边界才计跨边界；实验性 operating point 默认是可复用约束而非长期认知基础。既有深审证据继续保留，评分只决定最低投入，不反向删除已读证据。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Unprivileged Topology Certificates for Cloud GPU Attestation](https://arxiv.org/html/2606.24934v1) | 2026-06-25T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Dustin: Draft-Augmented Sparse Verification for Efficient Long-Context Generation with Speculative Decoding](https://arxiv.org/html/2606.24957v1) | 2026-06-25T08:00:00+08:00 | INFER-SPECULATIVE-DECODING；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[目标章](../../../../books/part-05-inference-system/48-speculative-decoding.md)“Acceptance 不是独立常数，在线决策必须结算系统状态” |
| [From Forecasting Leaderboards to Deployment Decisions: A Fail-Closed Certification Protocol](https://arxiv.org/html/2606.24996v1) | 2026-06-25T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Internal Data Repetition Destroys Language Models](https://arxiv.org/html/2606.24998v1) | 2026-06-25T08:00:00+08:00 | TRAIN-DATA；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：TRAIN-DATA，[目标章](../../../../books/part-04-training-system/27-data.md)“Data Mixture 应先被当作交互实验，而不是比例预测” |
| [Speculation at a Distance: Where Edge-Cloud Speculative Decoding Actually Pays Off](https://arxiv.org/html/2606.25091v1) | 2026-06-25T08:00:00+08:00 | INFER-SPECULATIVE-DECODING；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[目标章](../../../../books/part-05-inference-system/48-speculative-decoding.md)“Acceptance 不是独立常数，在线决策必须结算系统状态” |
| [Speculative Decoding at Temperature Zero: A Scoped Safety-Invariance Screen with a 48,072-Sample Expansion](https://arxiv.org/html/2606.25097v1) | 2026-06-25T08:00:00+08:00 | INFER-SPECULATIVE-DECODING；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[目标章](../../../../books/part-05-inference-system/48-speculative-decoding.md)“Acceptance 不是独立常数，在线决策必须结算系统状态” |
| [Power-Flexible AI Data Centers: A New Paradigm for Grid-Responsive Compute](https://arxiv.org/html/2606.25098v1) | 2026-06-25T08:00:00+08:00 | PLATFORM-GPU-SCHEDULER；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-GPU-SCHEDULER，[目标章](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)“Power Budget 是分层资源契约” |
| [Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory](https://arxiv.org/html/2606.25115v1) | 2026-06-25T08:00:00+08:00 | AGENT-MEMORY；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory](https://arxiv.org/html/2606.25161v1) | 2026-06-25T08:00:00+08:00 | AGENT-MEMORY；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [ActPlane: Programmable OS-Level Policy Enforcement for Agent Harnesses](https://arxiv.org/html/2606.25189v1) | 2026-06-25T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [To Isolate or to Score? Model-Adaptive Assessment for Cost-Efficient Multi-Agent RAG](https://arxiv.org/html/2606.25191v1) | 2026-06-25T08:00:00+08:00 | AGENT-RAG；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-RAG，[目标章](../../../../books/part-07-agent/76-rag.md)“Retrieval Control 应成为 Reader 外部的 Typed State” |
| [General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference](https://arxiv.org/html/2606.25349v1) | 2026-06-25T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Cache-Resident LLM Inference in GB-Scale Last-Level Caches](https://arxiv.org/html/2606.25353v1) | 2026-06-25T08:00:00+08:00 | INFER-PREFILL；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-PREFILL，[目标章](../../../../books/part-05-inference-system/43-prefill.md)“条件化机制分支与共存边界”下“Prefill 可把 weight execution 与 attention state 分成独立放置路径”段落 |
| [The Interplay of Harness Design and Post-Training in LLM Agents](https://arxiv.org/html/2606.25447v1) | 2026-06-25T08:00:00+08:00 | AGENT-WORKFLOW；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[目标章](../../../../books/part-07-agent/81-workflow.md)“Template、Realized Graph 与 Trace 不是同一个对象” |
| [Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One](https://arxiv.org/html/2606.25449v1) | 2026-06-25T08:00:00+08:00 | AGENT-MEMORY；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring](https://arxiv.org/html/2606.25487v1) | 2026-06-25T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models](https://arxiv.org/html/2606.25519v1) | 2026-06-25T08:00:00+08:00 | INFER-GPU-MEMORY；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-GPU-MEMORY，[目标章](../../../../books/part-05-inference-system/54-gpu-memory.md)“GPU memory lifecycle、precision/materialization 与条件化共存” |
| [Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints](https://arxiv.org/html/2606.25605v1) | 2026-06-25T08:00:00+08:00 | AGENT-TOOL-CALLING；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[目标章](../../../../books/part-07-agent/78-tool-calling.md)“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract” |
| [Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution](https://arxiv.org/html/2606.25721v1) | 2026-06-25T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication](https://arxiv.org/html/2606.25759v1) | 2026-06-25T08:00:00+08:00 | TRAIN-DISTRIBUTED-TRAINING；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[目标章](../../../../books/part-04-training-system/36-distributed-training.md)“异步训练必须分开 Throughput、Freshness 与 Objective Ownership” |
| [Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets](https://arxiv.org/html/2606.25760v1) | 2026-06-25T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation](https://arxiv.org/html/2606.25782v1) | 2026-06-25T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability](https://arxiv.org/html/2606.25819v1) | 2026-06-25T08:00:00+08:00 | AGENT-TOOL-CALLING；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[目标章](../../../../books/part-07-agent/78-tool-calling.md)“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract” |
| [Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It](https://arxiv.org/html/2606.26027v1) | 2026-06-25T08:00:00+08:00 | TRAIN-GRPO；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：TRAIN-GRPO，[目标章](../../../../books/part-04-training-system/33-grpo.md)“Tool-use RL 的训练对象包含环境编排” |
| [Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem](https://arxiv.org/html/2606.26028v1) | 2026-06-25T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems](https://arxiv.org/html/2606.26057v1) | 2026-06-25T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment](https://arxiv.org/html/2606.26071v1) | 2026-06-25T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Introducing computer use in Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) | 2026-06-25T00:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“从‘文本是否恶意’到‘谁获得了行为控制权’”；AGENT-TOOL-CALLING 仅作 action handoff |

## 4. 证据与知识整合

### [Introducing computer use in Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/)

**机制与贡献。** Google 将 computer use 合并进 Gemini 3.5 Flash，并公开三类安全控制：针对该能力的 targeted adversarial training；对敏感或不可逆动作提供可选的显式用户确认；识别到间接 prompt injection 时自动停止任务。这改变的是 Agent action 的 release contract，而不是证明模型已经“安全”：模型侧检测只产生风险信号，确认与停止策略仍由运行时和用户持有最终 effect authority。

**证据边界。** 官方正文与 `datePublished=2026-06-24T16:00:00Z` 只证明发布方公开的产品能力和 safeguard。页面没有披露 adversarial-training 数据与算法、检测阈值、误报/漏报、攻击覆盖、独立评测协议，也没有给出可复现的模型、硬件、精度、长度、并发或 SLO 合同；因此不能据此宣称已解决 prompt injection、不可逆动作风险或开放环境安全。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“从‘文本是否恶意’到‘谁获得了行为控制权’”已经规定 model sensor 不能成为 authority，高风险 action 必须由 scope、approval、sandbox 与确定性 policy 控制；[AGENT-TOOL-CALLING](../../../../books/part-07-agent/78-tool-calling.md) 已按 side-effect class 要求不可逆动作 approval。该发布没有提供足以改变这些长期命题的新机制，结论为 `No Change — Existing Coverage`。

### [Unprivileged Topology Certificates for Cloud GPU Attestation](https://arxiv.org/html/2606.24934v1)

**机制与贡献。** Cloud GPU tenants receive a model name and a region, but cannot directly inspect the physical accelerator that runs their job. We present a software-only attestation primitive for this setting.

**证据边界。** exact-v1 Method：arXiv:2606.24934v1 — §3 Attestation Model; §4 GPU Probe; §11 Packaging；Evaluation：arXiv:2606.24934v1 — §5 Certificate Stability Under Load; §6 Cross-Die Fingerprint Attestation; §7–§10 Attestation experiments；Limitations / counterevidence：arXiv:2606.24934v1 — §12 Limitations; §13 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [Dustin: Draft-Augmented Sparse Verification for Efficient Long-Context Generation with Speculative Decoding](https://arxiv.org/html/2606.24957v1)

**机制与贡献。** While speculative decoding improves inference throughput for multi-batch long-context Large Language Models (LLMs), its efficiency is often limited by a verification bottleneck where Key-Value (KV) cache loading dominates latency. Existing compression methods fail in this regime: static eviction incurs accuracy loss due to saliency shift, while dynamic selection introduces prohibitive computational overhead during the verification path.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24957v1 — §3 Observation; 4 Dustin Sparse Verification；Evaluation：https://arxiv.org/html/2606.24957v1 — §5 Experiment; Accuracy and End-to-End Decode Throughput；Limitations / counterevidence：https://arxiv.org/html/2606.24957v1 — §L Limitations; I Porting Overhead。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-SPECULATIVE-DECODING`。[books/part-05-inference-system/48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md) 顶层 Review notes 前的“Acceptance 不是独立常数，在线决策必须结算系统状态”已覆盖通用命题，不重复追加。
### [From Forecasting Leaderboards to Deployment Decisions: A Fail-Closed Certification Protocol](https://arxiv.org/html/2606.24996v1)

**机制与贡献。** Forecasting leaderboards rank models by predictive quality, but their winners are often read as deployment-ready top-1 advice. That reading can fail when forecasts are passed through a fixed decision interface, such as an alert threshold, a top-k budget, or a switching-cost policy.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24996v1 — §2 Results: Two Roles for the Certification Protocol；Evaluation：https://arxiv.org/html/2606.24996v1 — §A Report-Card and Gate Procedure; C/D Robustness Controls；Limitations / counterevidence：https://arxiv.org/html/2606.24996v1 — §3 Discussion: Limitations and scope; first-failing-gate audit。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [Internal Data Repetition Destroys Language Models](https://arxiv.org/html/2606.24998v1)

**机制与贡献。** Language models are running out of high-quality training data, and even aggressively deduplicated corpora retain some amount of repetition. Earlier controlled studies predated Chinchilla-style scaling laws and could only measure the cost of repetition indirectly.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24998v1 — §3 Methods; Repeated-pool construction；Evaluation：https://arxiv.org/html/2606.24998v1 — §4 Results; F Training and Evaluation Details；Limitations / counterevidence：https://arxiv.org/html/2606.24998v1 — §H Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `TRAIN-DATA`。[books/part-04-training-system/27-data.md](../../../../books/part-04-training-system/27-data.md) 顶层 Review notes 前的“Data Mixture 应先被当作交互实验，而不是比例预测”已覆盖通用命题，不重复追加。
### [Speculation at a Distance: Where Edge-Cloud Speculative Decoding Actually Pays Off](https://arxiv.org/html/2606.25091v1)

**机制与贡献。** Speculative decoding (SD) accelerates LLM inference by $1.5$-$3$ times when the draft and target models are co-located. This has motivated a distributed variant (DSD) that places the draft model on an edge device while the target stays in the cloud.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25091v1 — §II Background and Setting; III Gain Window；Evaluation：https://arxiv.org/html/2606.25091v1 — §III-A/B/C comparisons; IV Pipelining；Limitations / counterevidence：https://arxiv.org/html/2606.25091v1 — §V Conclusion and explicit verifier-interface/RTT boundary。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-SPECULATIVE-DECODING`。[books/part-05-inference-system/48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md) 顶层 Review notes 前的“Acceptance 不是独立常数，在线决策必须结算系统状态”已覆盖通用命题，不重复追加。
### [Speculative Decoding at Temperature Zero: A Scoped Safety-Invariance Screen with a 48,072-Sample Expansion](https://arxiv.org/html/2606.25097v1)

**机制与贡献。** Speculative decoding accelerates inference by letting a draft model propose tokens for a target model to verify, raising a concrete safety question: at temperature zero, can draft-side behavior leak into safety-scored outputs? We answer with Typical-Acceptance Invariance Screen (TAIS), a behavioral-equivalence screen that pairs target-only and speculative outputs on the same safety battery and requires byte-identity evidence, TOST equivalence at +/-3pp, and per-task Cohen's h below a calibrated null cutoff of |h| &lt; 0.1.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25097v1 — §3 Methods; Serving-stack Configuration; TAIS Screen；Evaluation：https://arxiv.org/html/2606.25097v1 — §4 Results; E0/E1/E2/E5; B Reproducibility；Limitations / counterevidence：https://arxiv.org/html/2606.25097v1 — §5.3 Limitations and Threats to Validity。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-SPECULATIVE-DECODING`。[books/part-05-inference-system/48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md) 顶层 Review notes 前的“Acceptance 不是独立常数，在线决策必须结算系统状态”已覆盖通用命题，不重复追加。
### [Power-Flexible AI Data Centers: A New Paradigm for Grid-Responsive Compute](https://arxiv.org/html/2606.25098v1)

**机制与贡献。** The rapid expansion of artificial intelligence (AI) infrastructure is driving unprecedented growth in electricity demand from data centers. Traditional power-system planning treats large computing facilities as inflexible peak loads, leading to costly infrastructure upgrades and long delays in grid interconnection.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25098v1 — §3 Architecture for Power-Flexible AI Infrastructure；Evaluation：https://arxiv.org/html/2606.25098v1 — §4 Experimental Demonstration; 5 Grid Services; 6 Geo-Load Shifting；Limitations / counterevidence：https://arxiv.org/html/2606.25098v1 — §7 Discussion and service-level preservation scope。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-GPU-SCHEDULER`。[books/part-06-ai-infrastructure/63-gpu-scheduler.md](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) 顶层 Review notes 前的“Power Budget 是分层资源契约”已覆盖通用命题，不重复追加。
### [Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory](https://arxiv.org/html/2606.25115v1)

**机制与贡献。** On-device language-model agents improve by accumulating experience in retrieved memory rather than by updating weights. This memory is hard-bounded and exposed: it consumes RAM and energy, reaches peers through a thin uplink, and becomes an attack surface because it is writable by what the agent reads.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25115v1 — §III System Design; Net-Value-Density; Three Decisions；Evaluation：https://arxiv.org/html/2606.25115v1 — §V Evaluation; Trust Under Poisoning; Real Hardware；Limitations / counterevidence：https://arxiv.org/html/2606.25115v1 — §VI Related Work and deployment-specific score calibration。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已覆盖通用命题，不重复追加。
### [TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory](https://arxiv.org/html/2606.25161v1)

**机制与贡献。** Large language model (LLM) agents rely on long-term memory to support extended interactions and personalized assistance beyond finite context windows. Existing memory agents actively update external memory through generated write, revise, and delete operations, but these updates may omit important information, corrupt existing memory, or introduce unsupported hallucinated content.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25161v1 — §3 Method; Memory Transition Verifier; Transition-Ranked GRPO；Evaluation：https://arxiv.org/html/2606.25161v1 — §4 Experiment; HaluMem; Reliability of Consolidation；Limitations / counterevidence：https://arxiv.org/html/2606.25161v1 — §D Memory Transition Error Judge Prompt and evaluated datasets。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已覆盖通用命题，不重复追加。
### [ActPlane: Programmable OS-Level Policy Enforcement for Agent Harnesses](https://arxiv.org/html/2606.25189v1)

**机制与贡献。** AI agents increasingly run in production through harnesses, the software around the LLM, including an engine that enforces safety and effectiveness policies, e.g., 'run tests before committing.' Enforcing these policies requires bridging a semantic gap: policy intent is expressed in underspecified natural language, while enforcement must act on concrete system actions, e.g., which test to run. Many policies also define event ordering or data flow actions.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25189v1 — §3 Design; Policy DSL; Information-Flow Control；Evaluation：https://arxiv.org/html/2606.25189v1 — §5 Evaluation; Compliance; Macro/Micro Overhead；Limitations / counterevidence：https://arxiv.org/html/2606.25189v1 — §2.3 Existing Approaches; evaluated policy/harness scope。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [To Isolate or to Score? Model-Adaptive Assessment for Cost-Efficient Multi-Agent RAG](https://arxiv.org/html/2606.25191v1)

**机制与贡献。** Multi-agent document assessment for retrieval-augmented generation is computationally expensive, driving practitioners toward smaller, deployable models whose assessment mechanisms remain poorly understood. We conduct a controlled study of training-free interventions on 7B-9B instruction-tuned models across diverse QA benchmarks, revealing a sharp dichotomy in how models benefit from assessment.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25191v1 — §3 Reasoning-Score Coupling; 4 Candidate Treatments; MADARA；Evaluation：https://arxiv.org/html/2606.25191v1 — §5 Experimental Setup; 6 Results; K Cost-Accuracy；Limitations / counterevidence：https://arxiv.org/html/2606.25191v1 — §7 Discussion boundaries; D/F calibration sensitivity。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-RAG`。[books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md) 顶层 Review notes 前的“Retrieval Control 应成为 Reader 外部的 Typed State”已覆盖通用命题，不重复追加。
### [General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference](https://arxiv.org/html/2606.25349v1)

**机制与贡献。** In secure two-party Transformer inference, linear layers are typically evaluated using Fully Homomorphic Encryption (FHE) through plaintext-ciphertext or ciphertext-ciphertext matrix multiplications, where key switching primarily occurs and dominates computational overhead in both FHE-based and hybrid FHE-MPC systems. Existing optimizations rely heavily on packing-specific algorithms, limiting their general applicability.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25349v1 — §IV Two-Party Secure Inference Algorithm; V Storage-Communication Trade-off; VI Fused Relinearization and Rotation；Evaluation：https://arxiv.org/html/2606.25349v1 — §VII Evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.25349v1 — §VIII Conclusion; exact-v1 analytical-evaluation-only note。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [Cache-Resident LLM Inference in GB-Scale Last-Level Caches](https://arxiv.org/html/2606.25353v1)

**机制与贡献。** Large language model (LLM) inference is increasingly dominated by data movement across the memory hierarchy. Recent 3D-stacked cache technologies have enabled GB-scale last-level caches in modern server CPUs, making it possible to keep reusable model weights on chip and exploit cache bandwidth and latency.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25353v1 — §3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation；Evaluation：https://arxiv.org/html/2606.25353v1 — §5 Experiment Setup; 6 Evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.25353v1 — §7 Discussion; 7.2 Future Works。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-PREFILL`。已在 [books/part-05-inference-system/43-prefill.md](../../../../books/part-05-inference-system/43-prefill.md) 顶层 Review notes 前反查机制正文；`SF-2026-ARXIV-2606-25353` 在正文出现 2 次、后置 trace 出现 1 次。
### [The Interplay of Harness Design and Post-Training in LLM Agents](https://arxiv.org/html/2606.25447v1)

**机制与贡献。** Tool-integrated LLM agents are often wrapped within a harness: the scaffolding that determines which tools are exposed, how they are described, and what auxiliary information accompanies each per-step observation. While agents are routinely post-trained, this scaffolding is typically treated as a fixed engineering detail, with design effort limited to the training-free regime.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25447v1 — §3 Experiment Setup; 3.2 Harness; 3.3 Tool Schema; 3.4 Task Type；Evaluation：https://arxiv.org/html/2606.25447v1 — §4 Analysis; 4.1 Evaluation Protocol; 4.4 OOD Robustness；Limitations / counterevidence：https://arxiv.org/html/2606.25447v1 — §B Benchmark Details; C Experimental Details; stated ALFWorld boundary。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-WORKFLOW`。[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md) 顶层 Review notes 前的“Template、Realized Graph 与 Trace 不是同一个对象”已覆盖通用命题，不重复追加。
### [Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One](https://arxiv.org/html/2606.25449v1)

**机制与贡献。** A language model's memory can be worse than no memory at all when the model or its interface is disposed to act on it: a memory that keeps a wrong conclusion but drops the work behind it leads a model to re-emit the stale value as a confident answer, where an empty memory leads it to abstain. We call this brittle memory.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25449v1 — §3 Brittle Memory and Reclaim Evaluation; 3.2 Reclaim Protocol；Evaluation：https://arxiv.org/html/2606.25449v1 — §4 Experimental Setup; 5 Results; 5.7 Boundary of the Fix；Limitations / counterevidence：https://arxiv.org/html/2606.25449v1 — §7 Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已覆盖通用命题，不重复追加。
### [How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring](https://arxiv.org/html/2606.25487v1)

**机制与贡献。** Almost every paper on LLM jailbreaks and prompt injection reports an attack-success rate (ASR), and that number is assigned not by people but by an automated judge: either a safety classifier trained for the task, or a general chat model prompted to grade. The judge is rarely checked.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25487v1 — §3 Setup; Appendix A Prompts, wrappers, and attack configuration；Evaluation：https://arxiv.org/html/2606.25487v1 — §4 Results; 4.1 Calibration against human labels; 4.3 white-box attack；Limitations / counterevidence：https://arxiv.org/html/2606.25487v1 — §6 Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models](https://arxiv.org/html/2606.25519v1)

**机制与贡献。** Quantization is widely used to reduce the inference cost of large language models, but its effect on reasoning models is not fully captured by final-answer accuracy or per-token latency. We show that low-bit post-training quantization can introduce a hidden test-time compute cost: quantized reasoning models often generate longer chains of thought even when they still answer correctly.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25519v1 — §3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy；Evaluation：https://arxiv.org/html/2606.25519v1 — §D Additional evaluation details; D.1 Benchmarks and evaluation protocol；Limitations / counterevidence：https://arxiv.org/html/2606.25519v1 — §7 Can We Reduce Reasoning-Token Inflation; D.2 Model details。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-GPU-MEMORY`。[books/part-05-inference-system/54-gpu-memory.md](../../../../books/part-05-inference-system/54-gpu-memory.md) 顶层 Review notes 前的“GPU memory lifecycle、precision/materialization 与条件化共存”已覆盖通用命题，不重复追加。
### [Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints](https://arxiv.org/html/2606.25605v1)

**机制与贡献。** Tool Calling and Structured Output are two core capabilities of modern Agent systems, yet their interaction under joint deployment conditions remains insufficiently understood. This paper reports a reproducible phenomenon observed in a production Agent system: when Tool Calling and JSON Schema constraints are simultaneously enabled, multiple open-weight models cease invoking tools despite maintaining high schema compliance.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25605v1 — §3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution；Evaluation：https://arxiv.org/html/2606.25605v1 — §5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency；Limitations / counterevidence：https://arxiv.org/html/2606.25605v1 — §7.5 Failure Cases and Limitations; 8.4 Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-TOOL-CALLING`。[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md) 顶层 Review notes 前的“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract”已覆盖通用命题，不重复追加。
### [Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution](https://arxiv.org/html/2606.25721v1)

**机制与贡献。** Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate model outputs through malicious retrieved documents. Existing detection methods typically rely on auxiliary classifiers or additional LLM-based verification, introducing substantial computational overhead.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25721v1 — §4 Method; 4.1 Keyword Searching; 4.2 Secondary Verification；Evaluation：https://arxiv.org/html/2606.25721v1 — §5 Evaluation; 5.1 Setup; 5.2 Results；Limitations / counterevidence：https://arxiv.org/html/2606.25721v1 — §6 Discussion; baseline and hyperparameter sensitivity。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication](https://arxiv.org/html/2606.25759v1)

**机制与贡献。** Large-scale neural-network training repeatedly aggregates gradients across devices, making communication a central cost in distributed learning. Low-bit gradient aggregation can reduce this cost, but applying it as a static replacement for full-precision communication can destabilize training because safe precision depends on training phase, model structure, runtime bucketization, and the communication substrate.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25759v1 — §3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing；Evaluation：https://arxiv.org/html/2606.25759v1 — §7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope；Limitations / counterevidence：https://arxiv.org/html/2606.25759v1 — §9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`。[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md) 顶层 Review notes 前的“异步训练必须分开 Throughput、Freshness 与 Objective Ownership”已覆盖通用命题，不重复追加。
### [Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets](https://arxiv.org/html/2606.25760v1)

**机制与贡献。** Computer-use agents turn vision-language model (VLM) predictions into executable GUI clicks, so reliable uncertainty estimates are essential for rejection, calibration, miss-severity ranking, and spatial safety regions. Yet evidence on post-hoc uncertainty quantification (UQ) for these agents is fragmented across isolated model and dataset pairs, leaving it unclear whether UQ rankings stay stable when the agent, benchmark, or observable interface changes.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25760v1 — §3 Benchmark and Evaluation Protocol; 7 Inductive-Conformal Click Disks；Evaluation：https://arxiv.org/html/2606.25760v1 — §4 UQ Generalizes Selectively; 5 Graded Error and Calibration；Limitations / counterevidence：https://arxiv.org/html/2606.25760v1 — §A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation](https://arxiv.org/html/2606.25782v1)

**机制与贡献。** With the widespread adoption of large language models (LLMs) in chatbots and everyday applications, companies increasingly need guardrails that are effective while remaining low-cost and low-latency. Safety evaluation of LLM outputs has generally relied on LLM-based judges, which can be effective but are often slow and expensive to deploy at scale.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25782v1 — §2 Dataset; 3 Adversarial Attack Methodology; 4 Safety Judge Panel；Evaluation：https://arxiv.org/html/2606.25782v1 — §5 Evaluation Protocol; 6 Results; 6.3 Cost and Latency Trade-offs；Limitations / counterevidence：https://arxiv.org/html/2606.25782v1 — §OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability](https://arxiv.org/html/2606.25819v1)

**机制与贡献。** Large language models are increasingly deployed as agents that solve tasks by interacting with external tool environments. Although recent tool-use benchmarks increasingly cover complex task settings, they still largely assume clean, stable, and trustworthy tool environments, leaving tool-environment unreliability insufficiently examined.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.25819v1 — §ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection；Evaluation：https://arxiv.org/html/2606.25819v1 — §Experiments; Experimental Setup; Further Analysis; Error Analysis；Limitations / counterevidence：https://arxiv.org/html/2606.25819v1 — §Canonical recovery-path construction and five injected-hazard boundary。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-TOOL-CALLING`。[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md) 顶层 Review notes 前的“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract”已覆盖通用命题，不重复追加。
### [Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It](https://arxiv.org/html/2606.26027v1)

**机制与贡献。** Tool use enables large language models (LLMs) to perform complex tasks, and recent agentic reinforcement learning (RL) methods show promise for enhancing model capabilities. However, RL alone often leads to instability or limited gains in tool-use tasks.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26027v1 — §4 Method; 4.2 catastrophic collapse; 4.4 supervisory fixes；Evaluation：https://arxiv.org/html/2606.26027v1 — §5 Experiments; 5.1 Dataset and Models; D Detailed Evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.26027v1 — §B Training Details; C Qwen3 Training; E Training Dynamic。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `TRAIN-GRPO`。[books/part-04-training-system/33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) 顶层 Review notes 前的“Tool-use RL 的训练对象包含环境编排”已覆盖通用命题，不重复追加。
### [Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem](https://arxiv.org/html/2606.26028v1)

**机制与贡献。** As autonomous AI agents increasingly transact across organizational boundaries, a fundamental trust challenge emerges: how can an agent assess whether an unknown counterpart is trustworthy? The ERC-8004 protocol addresses this challenge with the first permissionless trust layer for AI agent economies, built around three on-chain registries for Identity, Reputation, and Validation.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26028v1 — §3 System Model: ERC-8004 Protocol; 7 Reputation Market Security；Evaluation：https://arxiv.org/html/2606.26028v1 — §4 Dataset; 5 Agent Identity and Adoption; 6 Reputation Market；Limitations / counterevidence：https://arxiv.org/html/2606.26028v1 — §9 Limitations and Future Work; C x402 attribution challenges。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems](https://arxiv.org/html/2606.26057v1)

**机制与贡献。** AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26057v1 — §2 Threat Model; 3 Requirements; 4 Design; 5 Implementation；Evaluation：https://arxiv.org/html/2606.26057v1 — §6 Evaluation; 6.4 Machine-Checked Fail-Closed Invariant; 6.5 Live containment；Limitations / counterevidence：https://arxiv.org/html/2606.26057v1 — §8.3 Limitations and Future Work; Artifact and Reproducibility。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment](https://arxiv.org/html/2606.26071v1)

**机制与贡献。** A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26071v1 — §4 Protocol and Methods; 5 Environments; 7 Methodological Insights；Evaluation：https://arxiv.org/html/2606.26071v1 — §6 Case Studies; 8 Recommendations；Limitations / counterevidence：https://arxiv.org/html/2606.26071v1 — §10 Limitations and Future Work; negative-results and confounding boundary。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。

## 5. 缺口与下一步

无

闭合账目：arXiv raw=526；机构源新增候选=1；旧候选 provenance=65；当前候选=28；旧候选降级=38。FP 全量重裁与 24 项 FN 分层抽检均未发现待处理问题；全部 Integrate 已反查当前 owner 的顶层 Review notes 前正文；全部 Existing Coverage 已绑定正文命题锚点。

## 6. 复核

复核者：V3 恢复语义复核（独立于旧 V2.1 报告作者；2026-09-10）

结论：通过

当前合同来源再认证由作者侧执行，`/root` 以非作者身份独立复核日期、准入与 Books 边界；其提出的 DeepSeek 日期和 Gemini 候选准入修正均已落实。

独立复核覆盖 canonical owner 日期、撤回排除、旧候选 FP 全量重裁、24 项 FN 分层抽样、closure taxonomy、exact-v1 定位、每个 Integrate 的顶层 Review notes 前正文，以及每个 Existing Coverage 的正文命题锚点。审计明确区分“题摘准入”与“Books trace”，并排除 AI for Science、纯领域 benchmark、局部模型/表示改进和仅凭 ROADMAP 映射的材料。机器校验只证明结构一致性。
