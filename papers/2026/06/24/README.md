# Daily Research — 2026-06-24

**规范：** V3
**窗口：** 2026-06-23T09:00:00+08:00 ～ 2026-06-24T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T09:36:20+08:00

## 1. 结论

本窗恢复 507 个 canonical arXiv identity，逐项以完整题摘按当前“大模型与大模型基础设施”贡献门槛重审，冻结 29 个候选。旧 V2.1 的 45 个候选只作 provenance，16 项因垂直任务、领域 benchmark、局部表示/方法或仅能映射 ROADMAP 而在候选前关闭；没有以 Books trace 反向证明准入。

候选均复用可核实的 exact-v1 Method / Evaluation / Limitations 定位。Books 结果为 1 项整合、28 项已有覆盖；本次同步没有修改 Books、LEARNING_STATE 或跨日索引。

2026-09-14 按当前来源清单重放 13 个机构每日源并复用仍匹配的 arXiv / exact-v1 / Evidence / Books 证据。机构源补查只恢复 Seed2.1 发布事实；公开页没有披露可复用机制，已在候选前关闭；冻结分母仍为 29。详细过程见 [当前合同再认证](../_sources/daily-20260624/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)。/root 非作者独立复核已通过。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [当前合同再认证](../_sources/daily-20260624/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列与窗口定点检索；本窗无范围内新增 | 已检查 | 无 |
| SRC-ANTHROPIC | [当前合同再认证](../_sources/daily-20260624/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-GOOGLE-AI | [当前合同再认证](../_sources/daily-20260624/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：DeepMind / Google Research 官方索引；本窗无范围内新增 | 已检查 | 无 |
| SRC-META-AI | [当前合同再认证](../_sources/daily-20260624/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-QWEN | [当前合同再认证](../_sources/daily-20260624/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方博客时间序列；本窗无新 family / 重要 revision | 已检查 | 无 |
| SRC-DEEPSEEK | [当前合同再认证](../_sources/daily-20260624/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research / 发布索引；本窗无新 family / 重要 revision | 已检查 | 无 |
| SRC-MOONSHOT | [当前合同再认证](../_sources/daily-20260624/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：Kimi Blog 与官方仓库发布时序；本窗无范围内新增 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | [当前合同再认证](../_sources/daily-20260624/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 publicList 8/8 条按展示首发日期检查；本窗无范围内新增 | 已检查 | 无 |
| SRC-ZAI | [当前合同再认证](../_sources/daily-20260624/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [当前合同再认证](../_sources/daily-20260624/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：Seed2.1 官方页日期 06-23；仅能力/厂商 benchmark、机制未披露，候选前关闭 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [当前合同再认证](../_sources/daily-20260624/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方技术博客与仓库发布时序；本窗无范围内新增 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [当前合同再认证](../_sources/daily-20260624/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Paper / Blog 与仓库；本窗无范围内新增 | 已检查 | 无 |
| SRC-MINIMAX | [当前合同再认证](../_sources/daily-20260624/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：中英文博客与 Agent Tech Blog；相邻条目为 06-09/06-01，本窗无新增 | 已检查 | 无 |
| SRC-ARXIV | [canonical raw inventory](../_sources/daily-20260624/canonical-raw-identity-inventory-v2.1.json.gz)；507 个 owner identity 完成题摘筛选；[V3 audit](../_sources/daily-20260624/v3-admission-audit-20260910.json) | 已检查 | 无 |

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability。本轮独立复核已按当前候选实际新增的命题逐项重评，不沿用旧分数，也不因既有证据已经深入审阅而倒推高分：单一 owner 内的局部机制按单组件 reach 计，只有原文实际跨越系统边界才计跨边界；实验性 operating point 默认是可复用约束而非长期认知基础。既有深审证据继续保留，评分只决定最低投入，不反向删除已读证据。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Sol Video Inference Engine: Agent-Native Full-Stack Acceleration Framework for Efficient Video Generation](https://arxiv.org/html/2606.23743v1) | 2026-06-24T08:00:00+08:00 | INFER-TENSORRT-LLM；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-TENSORRT-LLM，[目标章](../../../../books/part-05-inference-system/49-tensorrt-llm.md)“从局部结果到可执行的系统边界”下“video inference optimization 应把 graph transformation、kernel/execution plan、memory schedule 与 serving config 绑定同一可重建 artifact”段落 |
| [ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents](https://arxiv.org/html/2606.23752v1) | 2026-06-24T08:00:00+08:00 | AGENT-MEMORY；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [Cryptographic certificates of validity for trustworthy AI](https://arxiv.org/html/2606.23768v1) | 2026-06-24T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes](https://arxiv.org/html/2606.23797v1) | 2026-06-24T08:00:00+08:00 | AGENT-WORKFLOW；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[目标章](../../../../books/part-07-agent/81-workflow.md)“Template、Realized Graph 与 Trace 不是同一个对象” |
| [Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs](https://arxiv.org/html/2606.23915v1) | 2026-06-24T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems](https://arxiv.org/html/2606.23927v1) | 2026-06-24T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents](https://arxiv.org/html/2606.23937v1) | 2026-06-24T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets](https://arxiv.org/html/2606.23961v1) | 2026-06-24T08:00:00+08:00 | INFER-KV-CACHE；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[目标章](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)“从不可逆 Eviction 到可恢复的分层 Recall” |
| [The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing](https://arxiv.org/html/2606.23969v1) | 2026-06-24T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Maestro Order: A Model-Agnostic Orchestration Harness](https://arxiv.org/html/2606.23983v1) | 2026-06-24T08:00:00+08:00 | AGENT-PLATFORM；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[目标章](../../../../books/part-07-agent/84-agent-platform.md)“Agent Runtime State Machine；Harness、Protocol 与 Credit 都是 Platform-owned Artifact” |
| [You Don't Need to Run Every Eval](https://arxiv.org/html/2606.24020v1) | 2026-06-24T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [RoPE-Aware Bit Allocation for KV-Cache Quantization](https://arxiv.org/html/2606.24033v1) | 2026-06-24T08:00:00+08:00 | INFER-KV-CACHE；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[目标章](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)“从不可逆 Eviction 到可恢复的分层 Recall” |
| [When Top-1 Fails: Calibrating LoRA Monitors for Masked Diffusion LMs](https://arxiv.org/html/2606.24119v1) | 2026-06-24T08:00:00+08:00 | PLATFORM-MONITORING；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-MONITORING，[目标章](../../../../books/part-06-ai-infrastructure/67-monitoring.md)“calibration-bound sensor、direct profile fallback 与 monitor 不拥有 truth/commit” |
| [Holistic Data Scheduler for LLM Pre-training via Multi-Objective Reinforcement Learning](https://arxiv.org/html/2606.24133v1) | 2026-06-24T08:00:00+08:00 | TRAIN-DATA；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：TRAIN-DATA，[目标章](../../../../books/part-04-training-system/27-data.md)“Data Mixture 应先被当作交互实验，而不是比例预测” |
| [AsyncOPD: How Stale Can On-Policy Distillation Be?](https://arxiv.org/html/2606.24143v1) | 2026-06-24T08:00:00+08:00 | TRAIN-DISTRIBUTED-TRAINING；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[目标章](../../../../books/part-04-training-system/36-distributed-training.md)“异步训练必须分开 Throughput、Freshness 与 Objective Ownership” |
| [Metis: Bridging Text and Code Memory for Self-Evolving Agents](https://arxiv.org/html/2606.24151v1) | 2026-06-24T08:00:00+08:00 | AGENT-MEMORY；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [AutoSpec: Safety Rule Evolution for LLM Agents via Inductive Logic Programming](https://arxiv.org/html/2606.24245v1) | 2026-06-24T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [LemonHarness Technical Report](https://arxiv.org/html/2606.24311v1) | 2026-06-24T08:00:00+08:00 | AGENT-PLATFORM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[目标章](../../../../books/part-07-agent/84-agent-platform.md)“Agent Runtime State Machine；Harness、Protocol 与 Credit 都是 Platform-owned Artifact” |
| [Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees](https://arxiv.org/html/2606.24322v1) | 2026-06-24T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Poisoned Playbooks: Demystifying Knowledge Poisoning Effects on AI Security Agents](https://arxiv.org/html/2606.24402v1) | 2026-06-24T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Natural Identifiers for Privacy and Data Audits in Large Language Models](https://arxiv.org/html/2606.24408v1) | 2026-06-24T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning](https://arxiv.org/html/2606.24428v1) | 2026-06-24T08:00:00+08:00 | AGENT-MEMORY；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference](https://arxiv.org/html/2606.24467v1) | 2026-06-24T08:00:00+08:00 | INFER-KV-CACHE；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[目标章](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)“从不可逆 Eviction 到可恢复的分层 Recall” |
| [CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation](https://arxiv.org/html/2606.24506v1) | 2026-06-24T08:00:00+08:00 | INFER-GPU-MEMORY；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-GPU-MEMORY，[目标章](../../../../books/part-05-inference-system/54-gpu-memory.md)“GPU memory lifecycle、precision/materialization 与条件化共存” |
| [Governed Shared Memory for Multi-Agent LLM Systems](https://arxiv.org/html/2606.24535v1) | 2026-06-24T08:00:00+08:00 | AGENT-MEMORY；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents](https://arxiv.org/html/2606.24551v1) | 2026-06-24T08:00:00+08:00 | AGENT-TOOL-CALLING；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[目标章](../../../../books/part-07-agent/78-tool-calling.md)“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract” |
| [Toward Self-Evolution-Ready Workflow Harnesses: A Reversible Migration Path and Convertibility Taxonomy for Expert LLM Pipelines](https://arxiv.org/html/2606.24598v1) | 2026-06-24T08:00:00+08:00 | AGENT-WORKFLOW；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[目标章](../../../../books/part-07-agent/81-workflow.md)“Template、Realized Graph 与 Trace 不是同一个对象” |
| [SAFARI: Scaling Long Horizon Agentic Fault Attribution via Active Investigation](https://arxiv.org/html/2606.24626v1) | 2026-06-24T08:00:00+08:00 | PLATFORM-TRACE；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-TRACE，[目标章](../../../../books/part-06-ai-infrastructure/69-trace.md)“provenance/evidence 不等于 truth” |
| [Are We Ready For An Agent-Native Memory System?](https://arxiv.org/html/2606.24775v1) | 2026-06-24T08:00:00+08:00 | AGENT-MEMORY；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |

## 4. 证据与知识整合

### [Sol Video Inference Engine: Agent-Native Full-Stack Acceleration Framework for Efficient Video Generation](https://arxiv.org/html/2606.23743v1)

**机制与贡献。** Modern video diffusion models achieve higher generation quality through scaling, but this also increases inference cost. Although many acceleration methods have been proposed, a central challenge is that the most effective acceleration strategy is highly instance-specific: a recipe that works well for one combination of model, hardware, and inference configuration often does not transfer to another.

**证据边界。** exact-v1 Method：arXiv:2606.23743v1 §3 Sol Architecture; §4 Agent-Native Optimization；Evaluation：arXiv:2606.23743v1 §5 Experiments；Limitations / counterevidence：arXiv:2606.23743v1 §6 Limitations and Future Work。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-TENSORRT-LLM`。已在 [books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 顶层 Review notes 前反查机制正文；`SF-2026-ARXIV-2606-23743` 在正文出现 1 次、后置 trace 出现 1 次。
### [ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents](https://arxiv.org/html/2606.23752v1)

**机制与贡献。** Software developers increasingly work with multiple LLM coding agents, switching among tools such as Codex, Grok, Claude Code, and other assistants as context windows fill, sessions end, or a particular agent becomes better suited to a subtask. Each agent, however, persists its conversation in a private and vendor-specific log.

**证据边界。** exact-v1 Method：arXiv:2606.23752v1 — §ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents; §2.2 Agent Memory; §4 Architecture；Evaluation：arXiv:2606.23752v1 — §8 Self-Referential Case Study；Limitations / counterevidence：arXiv:2606.23752v1 — §9 Discussion; §Validation Scope; §10 Future Work。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已覆盖通用命题，不重复追加。
### [Cryptographic certificates of validity for trustworthy AI](https://arxiv.org/html/2606.23768v1)

**机制与贡献。** We propose cryptographic certificates of validity for agentic AI systems. The core idea is to formally specify a correctness or policy condition as a logical predicate, compile this predicate to a witness-checking problem over polynomial constraints, and use a succinct cryptographic proof system (and optionally zero-knowledge) to certify that the condition holds.

**证据边界。** exact-v1 Method：arXiv:2606.23768v1 — §2 A compact slice of maths; §4 How to apply this mathematics to AI agents；Evaluation：arXiv:2606.23768v1 — §3 Examples; §3.2 A recursive example；Limitations / counterevidence：arXiv:2606.23768v1 — §5 Related work; §6 Conclusions。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes](https://arxiv.org/html/2606.23797v1)

**机制与贡献。** Graph and multi-agent orchestration frameworks make production large language model (LLM) workflows practical, but they do not by themselves solve conversational continuity when users maintain several interdependent objectives. This conceptual systems paper focuses on the high-complexity end of that design space, where goals can be suspended, resumed, revised, and invalidated by actions in other goals.

**证据边界。** exact-v1 Method：arXiv:2606.23797v1 — §9.5 Turn-Level Algorithm; §10 Design Principles; §11 Evaluation Protocol；Evaluation：arXiv:2606.23797v1 — §11 Evaluation Protocol；Limitations / counterevidence：arXiv:2606.23797v1 — §15 Contributions, Scope, and Validity; §16 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-WORKFLOW`。[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md) 顶层 Review notes 前的“Template、Realized Graph 与 Trace 不是同一个对象”已覆盖通用命题，不重复追加。
### [Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs](https://arxiv.org/html/2606.23915v1)

**机制与贡献。** Practice often treats automatic metrics for attribution in LLM retrieval-augmented generation as interchangeable. We audit eight automatic scorers -- lexical, embedding, and BERTScore baselines alongside entailment/grounding-trained models (clean and FEVER NLI, the checker MiniCheck) -- across three evaluation constructs (provenance/topicality, generated-answer attribution, and fact-check entailment), asking whether any scorer transfers: stays within the 95% confidence interval of the best audited scorer on every dataset of a multi-dataset construct.

**证据边界。** exact-v1 Method：arXiv:2606.23915v1 — §3 A Sentence-Unit Provenance-Ranking Score; §3.1 Provenance/topicality；Evaluation：arXiv:2606.23915v1 — §4 The Cross-Dataset Audit; §5 ERCR as a Boundary Probe; §F Independent Replication and Robustness；Limitations / counterevidence：arXiv:2606.23915v1 — §An external boundary: long-form alone does not predict the NLI failure.; §7 Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems](https://arxiv.org/html/2606.23927v1)

**机制与贡献。** Agentic AI systems powered by large language models (LLMs) are rapidly evolving into autonomous decision-making systems, exposing attack vectors beyond those of traditional LLM vulnerabilities. Existing security evaluations are often tied to specific implementations or domains, limiting unified comparison across heterogeneous systems.

**证据边界。** exact-v1 Method：arXiv:2606.23927v1 — §4 NodeSpec: System Representation; §6 RIFT-Bench Framework; §F.2 Framework and Architecture Matrix；Evaluation：arXiv:2606.23927v1 — §7.1 Structure Identifier Evaluation; §Appendix A Additional Comparison to Agentic Security Evaluation; §E.3 Evaluation Metrics；Limitations / counterevidence：arXiv:2606.23927v1 — §8 Discussion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents](https://arxiv.org/html/2606.23937v1)

**机制与贡献。** Exact-match retrieval recall is often used as a proxy for whether a retriever supplies useful policy context to a downstream decision model. We test this proxy for pre-action policy classification in tau-bench using Qwen2.5-3B/7B classifiers.

**证据边界。** exact-v1 Method：arXiv:2606.23937v1 — §Sensitivity to domain and query construction.；Evaluation：arXiv:2606.23937v1 — §Decision models and evaluation.; §Analysis of informative nonmatching clauses.; §B.1 Primary 3B result；Limitations / counterevidence：arXiv:2606.23937v1 — §Contribution and scope.; §Construct scope.; §7 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets](https://arxiv.org/html/2606.23961v1)

**机制与贡献。** Long-context and agentic LLM workloads push the KV cache past any fixed memory budget, forcing the inference stack to permanently evict tokens at every step of a continuous-inference stream. Existing methods all share the same template, a per-step direct-attention score followed by deterministic top-$K$ selection, which converts a single below-cutoff step into an irreversible verdict and permanently erases any subtly important token that direct attention cannot single out from noise.

**证据边界。** exact-v1 Method：arXiv:2606.23961v1 — §2 Nexus Sampling; §2.2 Nexus Scoring; §2.3 Weighted Reservoir Block Selection；Evaluation：arXiv:2606.23961v1 — §5 Experiments; §5.1 Setup; §5.2–§5.6 Results and Ablations；Limitations / counterevidence：arXiv:2606.23961v1 — §7 Conclusion; §A.5 Eviction Quality Under Approximate Future Utility。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-KV-CACHE`。[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 顶层 Review notes 前的“从不可逆 Eviction 到可恢复的分层 Recall”已覆盖通用命题，不重复追加。
### [The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing](https://arxiv.org/html/2606.23969v1)

**机制与贡献。** GPU Confidential Computing (GPU-CC) now preserves GPU-local performance: on NVIDIA B300, BF16 matmul runs at 0.998x of non-confidential performance. Yet LLM serving under Intel TDX plus GPU-CC still loses 13-27% of throughput, and KV-cache restore latency can more than double.

**证据边界。** exact-v1 Method：arXiv:2606.23969v1 — §3 Platforms and Method; §4.1 Compute and GPU-Local Memory Are at Parity; §5.6 Runtime Design Rule；Evaluation：arXiv:2606.23969v1 — §3.3 Experiment Families; §5 Case Study: Policy Inversion in the Serving Runtime; §6 Case Study: Movement Engineering for Loading and KV State；Limitations / counterevidence：arXiv:2606.23969v1 — §3.4 Comparability and Claim Scope; §11 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [Maestro Order: A Model-Agnostic Orchestration Harness](https://arxiv.org/html/2606.23983v1)

**机制与贡献。** A single forward pass of a capable model is a fast, fluent, and unreliable problem-solver: it is right often enough to be useful and wrong often enough to be dangerous; in language models, such confident errors are known as hallucinations. We present Maestro Order, a model-agnostic orchestration harness that turns unreliable solvers into reliable problem-solving systems by composing them according to four structural primitives (decompose, ensemble, verify, and recurse) and a budget-aware controller that decides where to spend compute.

**证据边界。** exact-v1 Method：arXiv:2606.23983v1 — §3. From Algebra to Architecture; §4. Harness Architecture; §5. Design Rationale and System Invariants；Evaluation：arXiv:2606.23983v1 — §12. Evaluation Methodology; §Simulation study (this paper).；Limitations / counterevidence：arXiv:2606.23983v1 — §15. Discussion: Failure Modes and Guidance; §16. Limitations and Threats to Validity; §17. Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-PLATFORM`。[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md) 顶层 Review notes 前的“Agent Runtime State Machine；Harness、Protocol 与 Credit 都是 Platform-owned Artifact”已覆盖通用命题，不重复追加。
### [You Don't Need to Run Every Eval](https://arxiv.org/html/2606.24020v1)

**机制与贡献。** A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. But do we need to run every eval?

**证据边界。** exact-v1 Method：arXiv:2606.24020v1 — §You Don’t Need to Run Every Eval Yuchen Zeng & Dimitris Papailiopoulos; §1 Introduction [You Don't Need to Run Every Eval exact-v1 method boundary]；Evaluation：arXiv:2606.24020v1 — §4 BenchPress : A Low-rank Benchmark Score Predictor; §4.3 BenchPress vs. LLMs as Benchmark Score Predictors; §5 What BenchPress Enables for Model Evaluation；Limitations / counterevidence：arXiv:2606.24020v1 — §7 Discussion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [RoPE-Aware Bit Allocation for KV-Cache Quantization](https://arxiv.org/html/2606.24033v1)

**机制与贡献。** Existing low-bit KV-cache quantizers often treat each cached key as a flat vector. Under RoPE, however, a key's contribution to a future attention logit decomposes into a position-dependent sum over two-dimensional frequency blocks.

**证据边界。** exact-v1 Method：arXiv:2606.24033v1 — §RoPE-Aware Bit Allocation for KV-Cache Quantization; §1 Introduction [RoPE-Aware Bit Allocation for KV-Cache Quantization exact-v1 method boundary]；Evaluation：arXiv:2606.24033v1 — §6.3 Downstream Evaluation；Limitations / counterevidence：arXiv:2606.24033v1 — §7 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-KV-CACHE`。[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 顶层 Review notes 前的“从不可逆 Eviction 到可恢复的分层 Recall”已覆盖通用命题，不重复追加。
### [When Top-1 Fails: Calibrating LoRA Monitors for Masked Diffusion LMs](https://arxiv.org/html/2606.24119v1)

**机制与贡献。** Discrete diffusion language model (DLM) fine-tuning inherits inexpensive diagnostics from denoising-time confidence monitors, but their PEFT-training meaning is untested. We test top-1 argmax concentration as a collapse warning.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24119v1 — §3 Methodology; 3.2 Experimental Setup；Evaluation：https://arxiv.org/html/2606.24119v1 — §4 Experiments and Results; 4.1 Calibrated Triage；Limitations / counterevidence：https://arxiv.org/html/2606.24119v1 — §D Mechanism and Boundary Audit; Definitions and non-portability。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-MONITORING`。[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md) 顶层 Review notes 前的“calibration-bound sensor、direct profile fallback 与 monitor 不拥有 truth/commit”已覆盖通用命题，不重复追加。
### [Holistic Data Scheduler for LLM Pre-training via Multi-Objective Reinforcement Learning](https://arxiv.org/html/2606.24133v1)

**机制与贡献。** The composition of training data, governed by the diversity of sources and their mixing strategy, is a cornerstone of Large Language Model (LLM) pre-training. Online Data Mixing (ODM), the technique of adaptively adjusting data mixtures during training, has emerged as a promising direction to improve efficiency.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24133v1 — §2 Methodology: The Holistic Data Scheduler; 2.2 Online Data Mixing；Evaluation：https://arxiv.org/html/2606.24133v1 — §3 Experiments and Analysis; 3.1 Experimental Setup；Limitations / counterevidence：https://arxiv.org/html/2606.24133v1 — §B Sensitivity Analysis of Reward Weights; C Hyperparameter Sensitivity。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `TRAIN-DATA`。[books/part-04-training-system/27-data.md](../../../../books/part-04-training-system/27-data.md) 顶层 Review notes 前的“Data Mixture 应先被当作交互实验，而不是比例预测”已覆盖通用命题，不重复追加。
### [AsyncOPD: How Stale Can On-Policy Distillation Be?](https://arxiv.org/html/2606.24143v1)

**机制与贡献。** On-policy distillation (OPD) trains a student on its own rollouts guided by teacher feedback and is becoming increasingly important for large language model (LLM) post-training. Like reinforcement learning (RL), however, OPD faces an on-policy systems bottleneck, as rollouts can dominate training time for reasoning workloads.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24143v1 — §4 Forward- and Reverse-KL OPD Under Staleness; 7 AsyncOPD；Evaluation：https://arxiv.org/html/2606.24143v1 — §7 AsyncOPD Experimental Results; G Scheduler Details；Limitations / counterevidence：https://arxiv.org/html/2606.24143v1 — §8 Limitations and Future Work。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`。[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md) 顶层 Review notes 前的“异步训练必须分开 Throughput、Freshness 与 Objective Ownership”已覆盖通用命题，不重复追加。
### [Metis: Bridging Text and Code Memory for Self-Evolving Agents](https://arxiv.org/html/2606.24151v1)

**机制与贡献。** Self-evolving agents improve over time by distilling experience from past executions and reusing it in future tasks. Existing systems represent such experience either as natural-language text injected into the agent context or as code exposed as callable tools.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24151v1 — §3 The Metis System; 3.2 Text Reflection; 3.3 Code Generation; 3.4 Memory Manager；Evaluation：https://arxiv.org/html/2606.24151v1 — §4 Experiments; A.1 Profiling Experiments；Limitations / counterevidence：https://arxiv.org/html/2606.24151v1 — §A.1 Per-Axis Analysis and reported construction/transfer trade-offs。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已覆盖通用命题，不重复追加。
### [AutoSpec: Safety Rule Evolution for LLM Agents via Inductive Logic Programming](https://arxiv.org/html/2606.24245v1)

**机制与贡献。** Large language model (LLM) agents increasingly automate complex tasks by integrating language models with external tools and environments. However, their autonomy poses significant safety risks: agents may execute destructive commands, leak sensitive data, or violate domain constraints.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24245v1 — §3 Overview; 4 Approach; ILP-Guided Predicate Learning；Evaluation：https://arxiv.org/html/2606.24245v1 — §5 Experimental Setup; 6 Evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.24245v1 — §7 Discussion and Threats to Validity。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [LemonHarness Technical Report](https://arxiv.org/html/2606.24311v1)

**机制与贡献。** As large language model (LLM) agents are applied to longer tasks, they increasingly modify workspace state across multiple rounds of iteration. However, agents typically observe only tool outputs and log fragments, while the actual state changes occur in the file system.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24311v1 — §3 Method; 3.2 Integrated Execution Framework; 3.5 Structured Tool Boundary；Evaluation：https://arxiv.org/html/2606.24311v1 — §4 Experiments; Terminal-Bench 2.0/2.1；Limitations / counterevidence：https://arxiv.org/html/2606.24311v1 — §5 Limitations and Future Work。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-PLATFORM`。[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md) 顶层 Review notes 前的“Agent Runtime State Machine；Harness、Protocol 与 Credit 都是 Platform-owned Artifact”已覆盖通用命题，不重复追加。
### [Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees](https://arxiv.org/html/2606.24322v1)

**机制与贡献。** LLM agents increasingly rely on persistent long-term memory, which creates a critical vulnerability that we study here: memory poisoning. An adversary can store untrusted content in one session that later steers a consequential action, such as a payment, a setting change, or data exfiltration, in a future session.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24322v1 — §II Threat Model; III TMA-NM; IV Formal Model；Evaluation：https://arxiv.org/html/2606.24322v1 — §V MEM-INV-Bench; VI Evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.24322v1 — §IX Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [Poisoned Playbooks: Demystifying Knowledge Poisoning Effects on AI Security Agents](https://arxiv.org/html/2606.24402v1)

**机制与贡献。** AI security agents increasingly rely on Retrieval-Augmented Generation (RAG) to use external security knowledge for vulnerability analysis and exploit reasoning. This creates a new risk: poisoned write-ups can be operationalized into incorrect exploit behavior.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24402v1 — §3 Problem Setting and Study Design; 5 Verification Boundary；Evaluation：https://arxiv.org/html/2606.24402v1 — §4 Poisoning Outcomes; 6 Generalization; 7 Mitigations；Limitations / counterevidence：https://arxiv.org/html/2606.24402v1 — §8 Discussions and Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [Natural Identifiers for Privacy and Data Audits in Large Language Models](https://arxiv.org/html/2606.24408v1)

**机制与贡献。** Assessing the privacy of large language models (LLMs) presents significant challenges. In particular, most existing methods for auditing differential privacy require the insertion of specially crafted canary data during training, making them impractical for auditing already-trained models without costly retraining.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24408v1 — §3 Natural Identifiers; 4 DP Auditing; 5 Dataset Inference；Evaluation：https://arxiv.org/html/2606.24408v1 — §H DP-SGD Auditing; I/J/K Additional Evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.24408v1 — §M Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning](https://arxiv.org/html/2606.24428v1)

**机制与贡献。** Experience-driven self-evolution is critical for large language model (LLM) agents to improve through open-world interaction. However, existing experience learning methods mostly rely on single-agent loops, where the same agent executes tasks, summarizes outcomes, and determines memory content.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24428v1 — §3 Self-Confirmation Trap; 4 Execute-Distill-Verify；Evaluation：https://arxiv.org/html/2606.24428v1 — §5 Experiments; Memory Quality and Contamination；Limitations / counterevidence：https://arxiv.org/html/2606.24428v1 — §G Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已覆盖通用命题，不重复追加。
### [CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference](https://arxiv.org/html/2606.24467v1)

**机制与贡献。** Long-context large language model (LLM) inference is increasingly constrained by the memory footprint and decoding cost of key-value (KV) caches, limiting sustainable deployment on resource-constrained hardware. Existing KV cache eviction methods typically apply heuristic token scoring over all heads in GQA-based LLMs.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24467v1 — §3 CompressKV; Retrieval Head Identification; Layer-Adaptive Allocation；Evaluation：https://arxiv.org/html/2606.24467v1 — §4 Experiments; LongBench/NIAH; Memory and Latency；Limitations / counterevidence：https://arxiv.org/html/2606.24467v1 — §4.5 Ablations; 4.6 Orthogonality tests。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-KV-CACHE`。[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 顶层 Review notes 前的“从不可逆 Eviction 到可恢复的分层 Recall”已覆盖通用命题，不重复追加。
### [CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation](https://arxiv.org/html/2606.24506v1)

**机制与贡献。** Emerging LLM services increasingly host many sparse MoE models, yet most models receive sparse requests and remain cold. This creates a GPU memory problem: model weights are stable and model-determined, while KV-cache is transient and demand-determined.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24506v1 — §3 CrossPool Design; KV Planner; Layer-wise Scheduler; Control Lowering；Evaluation：https://arxiv.org/html/2606.24506v1 — §5 Experiments; Context Scalability; Overall Performance；Limitations / counterevidence：https://arxiv.org/html/2606.24506v1 — §6 Discussion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-GPU-MEMORY`。[books/part-05-inference-system/54-gpu-memory.md](../../../../books/part-05-inference-system/54-gpu-memory.md) 顶层 Review notes 前的“GPU memory lifecycle、precision/materialization 与条件化共存”已覆盖通用命题，不重复追加。
### [Governed Shared Memory for Multi-Agent LLM Systems](https://arxiv.org/html/2606.24535v1)

**机制与贡献。** Multi-agent LLM environments require robust mechanisms for shared knowledge management. This paper formalizes the fleet-memory problem and identifies four foundational failure modes: unauthorized leakage, stale propagation, contradiction persistence, and provenance collapse.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24535v1 — §3 Fleet-Memory Problem; 5 Governed Shared Memory Architecture；Evaluation：https://arxiv.org/html/2606.24535v1 — §7 Evaluation Methodology; 8 Results；Limitations / counterevidence：https://arxiv.org/html/2606.24535v1 — §10 Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已覆盖通用命题，不重复追加。
### [GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents](https://arxiv.org/html/2606.24551v1)

**机制与贡献。** Computer-use agents can execute software tasks through either graphical interfaces or programmatic command interfaces, but existing evaluations confound interaction modality with differences in tasks, initial states, verifiers, and permitted actions. We introduce a matched execution-layer benchmark of 440 desktop tasks across 18 applications and 12 workflow categories, where screen-only GUI agents and skill-mediated CLI agents receive identical goals, states, and final-state verifiers while being restricted to modality-native actions.

**证据边界。** exact-v1 Method：arXiv:2606.24551v1 — §3.2 Benchmark Construction; §A.3 Visual Design Example；Evaluation：arXiv:2606.24551v1 — §3 Benchmark; §3.1 Benchmark Scope and Composition; §3.2 Benchmark Construction；Limitations / counterevidence：arXiv:2606.24551v1 — §3.1 Benchmark Scope and Composition; §UI Navigation and Control Discovery Failure.; §Workflow Execution Failure.。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-TOOL-CALLING`。[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md) 顶层 Review notes 前的“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract”已覆盖通用命题，不重复追加。
### [Toward Self-Evolution-Ready Workflow Harnesses: A Reversible Migration Path and Convertibility Taxonomy for Expert LLM Pipelines](https://arxiv.org/html/2606.24598v1)

**机制与贡献。** While expert-validated "LLM + script" workflows deliver significant value, they remain static: they encode hard-won domain knowledge yet fail to adapt execution based on feedback. Existing agent research predominantly targets greenfield agents and synthetic benchmarks, leaving the migration of active legacy workflows unresolved.

**证据边界。** exact-v1 Method：arXiv:2606.24598v1 §3 Migration Method; §4 Architecture; §7 Convertibility Taxonomy；Evaluation：arXiv:2606.24598v1 §5 WeChat Case Study; §6 Evaluation；Limitations / counterevidence：arXiv:2606.24598v1 §9 Discussion and Threats to Validity; abstract explicitly limits evidence to one case and readiness, not validated self-learning。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-WORKFLOW`。[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md) 顶层 Review notes 前的“Template、Realized Graph 与 Trace 不是同一个对象”已覆盖通用命题，不重复追加。
### [SAFARI: Scaling Long Horizon Agentic Fault Attribution via Active Investigation](https://arxiv.org/html/2606.24626v1)

**机制与贡献。** As autonomous agents tackle increasingly complex multi-step, multi-agent tasks, their execution trajectories have scaled beyond the constraints of even the largest context windows. Current methods for effectively diagnosing agent failures load the full trajectory into an LLM's context window, which suffers from attention dilution and fails when agentic traces inevitably exceed context limits.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24626v1 — §2 Methodology: SAFARI；Evaluation：https://arxiv.org/html/2606.24626v1 — §3 Experimental Setup; 4 Results; A/B/C appendices；Limitations / counterevidence：https://arxiv.org/html/2606.24626v1 — §D Future Work。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-TRACE`。[books/part-06-ai-infrastructure/69-trace.md](../../../../books/part-06-ai-infrastructure/69-trace.md) 顶层 Review notes 前的“provenance/evidence 不等于 truth”已覆盖通用命题，不重复追加。
### [Are We Ready For An Agent-Native Memory System?](https://arxiv.org/html/2606.24775v1)

**机制与贡献。** Memory for large language model (LLM) agents has rapidly evolved from simple retrieval-augmented mechanisms into a data management system that supports persistent information storage, retrieval, update, consolidation, and dynamic lifecycle governance throughout agent execution. Despite this evolution, existing evaluations still benchmark agent memory mainly through end-to-end task success metrics (e.g., F1, BLEU), while treating the underlying system as a monolithic black box.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.24775v1 — §3 Method Overview; Representation, Extraction, Retrieval, Maintenance；Evaluation：https://arxiv.org/html/2606.24775v1 — §4 End-to-End Assessment; 5 Component Comparison；Limitations / counterevidence：https://arxiv.org/html/2606.24775v1 — §4.3 Evolution Robustness; 4.4 Long-Horizon Stability; 4.5 Cost。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已覆盖通用命题，不重复追加。

## 5. 缺口与下一步

无

闭合账目：raw=507；旧候选 provenance=45；V3 候选=29；旧候选降级=16。FP 全量重裁与 24 项 FN 分层抽检均未发现待处理问题；全部 Integrate 已反查当前 owner 的顶层 Review notes 前正文；全部 Existing Coverage 已绑定正文命题锚点。

## 6. 复核

复核者：V3 恢复语义复核（独立于旧 V2.1 报告作者；2026-09-10）

结论：通过

独立复核覆盖 canonical owner 日期、撤回排除、旧候选 FP 全量重裁、24 项 FN 分层抽样、closure taxonomy、exact-v1 定位、每个 Integrate 的顶层 Review notes 前正文，以及每个 Existing Coverage 的正文命题锚点。审计明确区分“题摘准入”与“Books trace”，并排除 AI for Science、纯领域 benchmark、局部模型/表示改进和仅凭 ROADMAP 映射的材料。机器校验只证明结构一致性。
