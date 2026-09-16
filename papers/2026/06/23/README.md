# Daily Research — 2026-06-23

**规范：** V3
**窗口：** 2026-06-22T09:00:00+08:00 ～ 2026-06-23T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T09:36:20+08:00

## 1. 结论

本窗口按 canonical first-public owner 恢复 1556 个 arXiv identity；逐项复用保存的完整题摘并按当前“大模型与大模型基础设施”贡献门槛重新判断，冻结 50 个候选。旧 V2.1 的 235 个候选仅作 provenance，其中 185 项因垂直应用、局部 benchmark/recipe 或只能映射章节而未改变长期设计选择，降回候选前关闭；撤回项不进入候选或采用链。

50 项都复用了可核实的 exact-v1 Method / Evaluation / Limitations 定位。Books 结果为 11 项整合（均已在当前 owner 的顶层 Review notes 前反查正文）和 39 项已有覆盖（均给出正文命题锚点）；本次同步没有修改 Books、LEARNING_STATE 或跨日索引。

2026-09-14 按当前来源清单重放 13 个机构每日源并复用仍匹配的 arXiv / exact-v1 / Evidence / Books 证据。机构源补查只恢复 A24 合作公告，题摘/正文未提供大模型或基础设施机制，已在候选前关闭；冻结分母仍为 50。详细过程见 [当前合同再认证](../_sources/daily-20260623/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)。/root 非作者独立复核已通过。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [当前合同再认证](../_sources/daily-20260623/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列与窗口定点检索；本窗无范围内新增 | 已检查 | 无 |
| SRC-ANTHROPIC | [当前合同再认证](../_sources/daily-20260623/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-GOOGLE-AI | [当前合同再认证](../_sources/daily-20260623/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：A24 合作公告于 06-22 22:30 北京时间落窗；无模型/系统机制，候选前关闭 | 已检查 | 无 |
| SRC-META-AI | [当前合同再认证](../_sources/daily-20260623/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-QWEN | [当前合同再认证](../_sources/daily-20260623/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方博客时间序列；本窗无新 family / 重要 revision | 已检查 | 无 |
| SRC-DEEPSEEK | [当前合同再认证](../_sources/daily-20260623/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research / 发布索引；本窗无新 family / 重要 revision | 已检查 | 无 |
| SRC-MOONSHOT | [当前合同再认证](../_sources/daily-20260623/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：Kimi Blog 与官方仓库发布时序；本窗无范围内新增 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | [当前合同再认证](../_sources/daily-20260623/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 publicList 8/8 条按展示首发日期检查；本窗无范围内新增 | 已检查 | 无 |
| SRC-ZAI | [当前合同再认证](../_sources/daily-20260623/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [当前合同再认证](../_sources/daily-20260623/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research、论文目录与发布页；本窗无范围内新增 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [当前合同再认证](../_sources/daily-20260623/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方技术博客与仓库发布时序；本窗无范围内新增 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [当前合同再认证](../_sources/daily-20260623/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Paper / Blog 与仓库；本窗无范围内新增 | 已检查 | 无 |
| SRC-MINIMAX | [当前合同再认证](../_sources/daily-20260623/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：中英文博客与 Agent Tech Blog；相邻条目为 06-09/06-01，本窗无新增 | 已检查 | 无 |
| SRC-ARXIV | [canonical raw inventory](../_sources/daily-20260623/canonical-raw-identity-inventory-v2.1.json.gz)；1556 个 first-public owner identity 完成题摘筛选；[V3 audit](../_sources/daily-20260623/v3-admission-audit-20260910.json) | 已检查 | 无 |

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability。本轮独立复核已按当前候选实际新增的命题逐项重评，不沿用旧分数，也不因既有证据已经深入审阅而倒推高分：单一 owner 内的局部机制按单组件 reach 计，只有原文实际跨越系统边界才计跨边界；实验性 operating point 默认是可复用约束而非长期认知基础。既有深审证据继续保留，评分只决定最低投入，不反向删除已读证据。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [BELLS-O: Evaluating the Operational Trade-offs of LLM Supervision Systems](https://arxiv.org/html/2606.20668v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [How Much Coordination Gain Is Real? A Paired Noise-Floor Protocol for Multi-Agent LLM Benchmarks](https://arxiv.org/html/2606.20695v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [When Web Agents Finish but Still Fail: Reproducible Triggers and Trace Diagnostics for Parallel Web Exploration](https://arxiv.org/html/2606.20724v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [CELEUS: Certifiable and Efficient LLM Evaluation via E-Processes](https://arxiv.org/html/2606.20820v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Think Twice Before You Act: Protecting LLM Agents Against Tool Description Poisoning via Isolated Planning](https://arxiv.org/html/2606.20922v1) | 2026-06-23T08:00:00+08:00 | AGENT-TOOL-CALLING；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[目标章](../../../../books/part-07-agent/78-tool-calling.md)“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract” |
| [Learning What Not to Forget: Long-Horizon Agent Memory from a Few Kilobytes of Learning](https://arxiv.org/html/2606.20954v1) | 2026-06-23T08:00:00+08:00 | AGENT-MEMORY；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [Demystifying Numerical Instability in LLM Inference: Achieving Reproducible Inference for Mission-Critical Tasks with HEAL](https://arxiv.org/html/2606.21023v1) | 2026-06-23T08:00:00+08:00 | INFER-GPU-MEMORY；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-GPU-MEMORY，[目标章](../../../../books/part-05-inference-system/54-gpu-memory.md)“新证据如何改变本章的设计边界”下“异构 GPU 上 greedy decode 仍会因 kernel-boundary downcast 累积而翻转”段落 |
| [Repeated post-training is not Self-improving: Diagnosing Scientific Amnesia in Continual DPO Pipelines](https://arxiv.org/html/2606.21089v1) | 2026-06-23T08:00:00+08:00 | TRAIN-DPO；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：TRAIN-DPO，[目标章](../../../../books/part-04-training-system/34-dpo.md)“Online Discovery 与 Offline Preference Update 可以分权” |
| [Self-Improvement Can Self-Regress: The Rise-and-Collapse Failure Mode of LLM Self-Training](https://arxiv.org/html/2606.21090v1) | 2026-06-23T08:00:00+08:00 | TRAIN-GRPO；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：TRAIN-GRPO，[目标章](../../../../books/part-04-training-system/33-grpo.md)“Tool-use RL 的训练对象包含环境编排” |
| [AgenticOS: An Intent-Oriented Secure Operating System Architecture for Autonomous AI Agents](https://arxiv.org/html/2606.21129v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Recency/Frequency Adaptive KV Caching for Large Language Model Serving](https://arxiv.org/html/2606.21238v1) | 2026-06-23T08:00:00+08:00 | INFER-KV-CACHE；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[目标章](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)“从不可逆 Eviction 到可恢复的分层 Recall” |
| [SCOPE: Sequential Conformal Probing for Reliable OOD Rejection in LLM Services](https://arxiv.org/html/2606.21255v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| ["What Happens Locally, Leaks Globally": Detecting Privacy Leakage Risks in MCP Servers](https://arxiv.org/html/2606.21338v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Calibration Is Not Control: Why LLM-Agent Oversight Needs Intervention](https://arxiv.org/html/2606.21399v1) | 2026-06-23T08:00:00+08:00 | AGENT-PLATFORM；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[目标章](../../../../books/part-07-agent/84-agent-platform.md)“Agent Runtime State Machine；Harness、Protocol 与 Credit 都是 Platform-owned Artifact” |
| [SwarmX: Agentic Scheduling for Low-Latency Agentic Systems](https://arxiv.org/html/2606.21401v1) | 2026-06-23T08:00:00+08:00 | INFER-SCHEDULING；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md)“SLO-aware Admission；Expert weights 与 KV 的联合 working set” |
| [Don't Blindly Trust It: How Unreliable Feedback Breaks Tool-Using LLM Agents](https://arxiv.org/html/2606.21409v1) | 2026-06-23T08:00:00+08:00 | AGENT-TOOL-CALLING；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[目标章](../../../../books/part-07-agent/78-tool-calling.md)“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract” |
| [HERALD: High-Throughput Block Diffusion LLM Serving via CPU-GPU Cooperative KV Cache Retrieval](https://arxiv.org/html/2606.21633v1) | 2026-06-23T08:00:00+08:00 | INFER-KV-CACHE；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[目标章](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)“从不可逆 Eviction 到可恢复的分层 Recall” |
| [Toward Open Weight Models Without Risks: Separating Public and Private Capabilities in LLMs](https://arxiv.org/html/2606.21638v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Hallucination as Context Drift: Synchronization Protocols for Multi-Agent LLM Systems](https://arxiv.org/html/2606.21666v1) | 2026-06-23T08:00:00+08:00 | AGENT-MULTI-AGENT；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[目标章](../../../../books/part-07-agent/82-multi-agent.md)“Message 不是 State；Verification Delay 也是拓扑控制状态” |
| [Decodable but Not Faithful: Coupling Natural-Language Rationales to Programmatic Verifiers](https://arxiv.org/html/2606.21678v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [BatchGen: An Architecture for Scalable and Efficient Batch Inference](https://arxiv.org/html/2606.21712v1) | 2026-06-23T08:00:00+08:00 | INFER-SCHEDULING；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md)“SLO-aware Admission；Expert weights 与 KV 的联合 working set” |
| [Safe to Check, Unsafe to Use: Relinking at the Compression Boundary of LLM Agents](https://arxiv.org/html/2606.21732v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [CalVerT: Augmenting Agents with Calibrated Verifier Telemetry Improves Action and Learning in Knowledge-Intensive Tasks](https://arxiv.org/html/2606.21777v1) | 2026-06-23T08:00:00+08:00 | AGENT-RAG；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-RAG，[目标章](../../../../books/part-07-agent/76-rag.md)“Retrieval Control 应成为 Reader 外部的 Typed State” |
| [Agent-Assisted Side-Channel Attacks on Non-Prefix KV Cache in RAG](https://arxiv.org/html/2606.21842v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-SECURITY；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [WiSP: A Working-Set View of Mixture-of-Experts Serving on Extremely Low-Resource Hardware](https://arxiv.org/html/2606.21868v1) | 2026-06-23T08:00:00+08:00 | INFER-SCHEDULING；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md)“SLO-aware Admission；Expert weights 与 KV 的联合 working set” |
| [AgentRiskBOM: A Risk-Scoping Security Bill of Materials for Agentic AI Systems](https://arxiv.org/html/2606.21877v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Load Testing for Machine Learning Model Serving Systems at Scale](https://arxiv.org/html/2606.22013v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-PRODUCTION；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：PLATFORM-PRODUCTION，[目标章](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md)“Load test 是 SLO boundary search” |
| [When Does Belief-Based Agent Memory Help? Reliability-Conditional Updating and Provenance-Capped Poisoning Defense](https://arxiv.org/html/2606.22030v1) | 2026-06-23T08:00:00+08:00 | AGENT-MEMORY；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [Drowning in Routine: Signal Dilution in Multi-Turn Agent Training](https://arxiv.org/html/2606.22164v1) | 2026-06-23T08:00:00+08:00 | TRAIN-GRPO；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：TRAIN-GRPO，[目标章](../../../../books/part-04-training-system/33-grpo.md)“Tool-use RL 的训练对象包含环境编排” |
| [StickyInvoc: Rethinking Task Models for High-throughput Workflows in the LLM Era](https://arxiv.org/html/2606.22175v1) | 2026-06-23T08:00:00+08:00 | AGENT-WORKFLOW；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[目标章](../../../../books/part-07-agent/81-workflow.md)“Template、Realized Graph 与 Trace 不是同一个对象” |
| [When Is Emergent Consensus Real? A Measured Coupling Gain and a Validity Diagnostic for LLM Agent Societies](https://arxiv.org/html/2606.22203v1) | 2026-06-23T08:00:00+08:00 | AGENT-MULTI-AGENT；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[目标章](../../../../books/part-07-agent/82-multi-agent.md)“Message 不是 State；Verification Delay 也是拓扑控制状态” |
| [Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice](https://arxiv.org/html/2606.22327v1) | 2026-06-23T08:00:00+08:00 | INFER-SCHEDULING；3 + 2 + 2 = 7 | 深入完成 | 整合：INFER-SCHEDULING，[目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md)“从局部结果到可执行的系统边界”下“把 online LLM scheduling 建模为带几何长度/剩余工作量的 admission 与排队问题”段落 |
| [BabelJudge: Measuring LLM-as-a-Judge Reliability Across Languages and Agent Trajectories](https://arxiv.org/html/2606.22329v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Lingering Authority: Revocable Resource-and-Effect Capabilities for Coding Agents](https://arxiv.org/html/2606.22504v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-SECURITY；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“从局部结果到可执行的系统边界”下“把 agent authority 从 task-wide tool visibility 改为 resource/effect/phase scoped capability”段落 |
| [Governance Decay: How Context Compaction Silently Erases Safety Constraints in Long-Horizon LLM Agents](https://arxiv.org/html/2606.22528v1) | 2026-06-23T08:00:00+08:00 | AGENT-CONTEXT；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-CONTEXT，[目标章](../../../../books/part-07-agent/75-context.md)“从局部结果到可执行的系统边界”下“把 context compaction 识别为治理控制面”段落 |
| [ASAP: A Disaggregated and Asynchronous Inference System for MoE Prefill](https://arxiv.org/html/2606.22541v1) | 2026-06-23T08:00:00+08:00 | INFER-PD-DISAGGREGATION；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-PD-DISAGGREGATION，[目标章](../../../../books/part-05-inference-system/55-pd-disaggregation.md)“从局部结果到可执行的系统边界”下“MoE prefill 不应把 attention、expert dispatch 与 communication 绑成同步 barrier”段落 |
| [Evidence-Bound Gateway-Path Provenance for Third-Party LLM Inference](https://arxiv.org/html/2606.22560v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-GATEWAY；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-GATEWAY，[目标章](../../../../books/part-06-ai-infrastructure/62-gateway.md)“从局部结果到可执行的系统边界”下“第三方 LLM gateway 不能仅返回 provider name”段落 |
| [On Good Authority: Release-Authority Measurement for Registry-Mediated Package Ecosystems](https://arxiv.org/html/2606.22593v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-MODEL-REGISTRY；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-MODEL-REGISTRY，[目标章](../../../../books/part-06-ai-infrastructure/59-model-registry.md)“从局部结果到可执行的系统边界”下“registry 的 release authority 不是 package presence”段落 |
| [Confidently Wrong: Severity-Aware Calibration of Prompt-Injection Detectors under Attack Shift](https://arxiv.org/html/2606.22659v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“从局部结果到可执行的系统边界”下“prompt-injection detector 的 calibration 要按 attack severity 与 shift slice”段落 |
| [Black-Box Forensics for Conversational LLM Agents](https://arxiv.org/html/2606.22698v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-TRACE；2 + 1 + 2 = 5 | 深入完成 | 整合：PLATFORM-TRACE，[目标章](../../../../books/part-06-ai-infrastructure/69-trace.md)“从局部结果到可执行的系统边界”下“black-box agent forensics 需要固定 probe transcript”段落 |
| [GroundEval: A Deterministic Replacement for LLM-as-Judge in Stateful Agent Evaluation](https://arxiv.org/html/2606.22737v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 2 + 2 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“从局部结果到可执行的系统边界”下“stateful Agent evaluation 可由确定性 environment transition、predicate 与 event log 计算 GroundEval”段落 |
| [GRADE: Graph Representation of LLM Agent Dependency and Execution](https://arxiv.org/html/2606.22741v1) | 2026-06-23T08:00:00+08:00 | AGENT-WORKFLOW；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[目标章](../../../../books/part-07-agent/81-workflow.md)“Template、Realized Graph 与 Trace 不是同一个对象” |
| [Factored Gossip DiLoCo: Reducing Blocking Communication in DiLoCo](https://arxiv.org/html/2606.22768v1) | 2026-06-23T08:00:00+08:00 | TRAIN-DISTRIBUTED-TRAINING；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[目标章](../../../../books/part-04-training-system/36-distributed-training.md)“异步训练必须分开 Throughput、Freshness 与 Objective Ownership” |
| [Intent-Governed Tool Authorization for AI Agents](https://arxiv.org/html/2606.22916v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training](https://arxiv.org/html/2606.22932v1) | 2026-06-23T08:00:00+08:00 | TRAIN-DISTRIBUTED-TRAINING；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[目标章](../../../../books/part-04-training-system/36-distributed-training.md)“Gradient 不必在 Backward 与 Optimizer 之间完整物化”下“传统 reverse-mode 先把每层 weight gradient 写入全局内存”段落 |
| [MOCAP: Wafer-Scale-Chip-Oriented Memory-Orchestrated Chunked Pipelining Framework for Prefill-Only LLM Inference](https://arxiv.org/html/2606.22968v1) | 2026-06-23T08:00:00+08:00 | INFER-PREFILL；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-PREFILL，[目标章](../../../../books/part-05-inference-system/43-prefill.md)“Prefill pipeline、chunk/memory orchestration 与 placement contract” |
| [LiveServe: Interaction-Aware Serving for Real-Time Omni-Modal LLMs](https://arxiv.org/html/2606.22983v1) | 2026-06-23T08:00:00+08:00 | INFER-SCHEDULING；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md)“SLO-aware Admission；Expert weights 与 KV 的联合 working set” |
| [Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory](https://arxiv.org/html/2606.23195v1) | 2026-06-23T08:00:00+08:00 | AGENT-MEMORY；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [GIF: Locally Sound Geometric Information Flow Control for LLMs](https://arxiv.org/html/2606.23277v1) | 2026-06-23T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference](https://arxiv.org/html/2606.23521v1) | 2026-06-23T08:00:00+08:00 | INFER-DECODE；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-DECODE，[目标章](../../../../books/part-05-inference-system/44-decode.md)“Decode 的结束条件；Decode-only Compute Branch 仍必须尊重单一 KV Owner” |

## 4. 证据与知识整合

### [BELLS-O: Evaluating the Operational Trade-offs of LLM Supervision Systems](https://arxiv.org/html/2606.20668v1)

**机制与贡献。** LLM supervision systems, namely input/output moderation filters and jailbreak detectors, are the primary safeguard against misuse in deployed AI applications, yet existing benchmarks are often vendor-biased, omit cost and latency, and rarely compare specialized guardrails against repurposed generalist LLMs. We present BELLS-O (Benchmark for the Evaluation of LLM Supervision Systems, Operational), the first independent operational benchmark of LLM supervision systems.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.20668v1 — § exact-v1 anchor: BELLS-O；Evaluation：https://arxiv.org/html/2606.20668v1 — § exact-v1 evaluation anchor: 28 systems from 17 providers；Limitations / counterevidence：https://arxiv.org/html/2606.20668v1 — § exact-v1 limitation/counterevidence anchor: use-case-dependent tradeoffs。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。现有 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已承载通用命题，本材料不要求重复追加。
### [How Much Coordination Gain Is Real? A Paired Noise-Floor Protocol for Multi-Agent LLM Benchmarks](https://arxiv.org/html/2606.20695v1)

**机制与贡献。** Multi-agent LLM coordination papers report small benchmark deltas as evidence that one architecture beats another. A prior question: how much paired trial-0 disagreement do two protocols produce on the same model and benchmark when their API inputs are configuration-equivalent (matched by code inspection plus a SHA-256 byte audit), short of full identity-replay?

**证据边界。** exact-v1 Method：arXiv:2606.20695v1 §4 ET-MCP Architecture; §5 Implementation；Evaluation：arXiv:2606.20695v1 §6 Evaluation (§6.1 benchmarks; §6.2 metrics; §6.3 paired/noise-floor results; §6.4 probes; §6.5 threshold)；Limitations / counterevidence：arXiv:2606.20695v1 §6.3.3 no detectable effect at stated power; §6.6 Limitations; §7 Forward Work。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。现有 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已承载通用命题，本材料不要求重复追加。
### [When Web Agents Finish but Still Fail: Reproducible Triggers and Trace Diagnostics for Parallel Web Exploration](https://arxiv.org/html/2606.20724v1)

**机制与贡献。** Long-horizon web agents often fail in ways hidden by final-answer evaluation: they may visit useful pages, produce a well-formed answer, and terminate confidently while still missing fields, over-including unsupported items, or relying on stale evidence. We study these failures with Parallel WebBench, a parallel web-exploration benchmark containing 1,679 verified records: 350 manually curated parallel tasks and 1,329 reconstructed records with verified URL-based trajectories.

**证据边界。** exact-v1 Method：arXiv:2606.20724v1 §3 reproducible failure triggers; §4 trace-diagnostic taxonomy；Evaluation：arXiv:2606.20724v1 §5 parallel web-exploration experiments and reruns；Limitations / counterevidence：Not Disclosed — arXiv:2606.20724v1 has no dedicated limitations section; exact-v1 counterevidence is localized at site volatility, task/sample, browser/harness and trigger-generalization limits。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。现有 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已承载通用命题，本材料不要求重复追加。
### [CELEUS: Certifiable and Efficient LLM Evaluation via E-Processes](https://arxiv.org/html/2606.20820v1)

**机制与贡献。** Can we trust evaluation scores to capture an LLM's true real-world performance? Certifiable evaluation answers this question by providing guarantee for LLM evaluation.

**证据边界。** exact-v1 Method：https://www.researchgate.net/publication/397008000_CELEUS_Certifiable_and_Efficient_LLM_Evaluation_via_E-Processes — §2 Certifiable and Efficient Evaluation: Setup and Overview；Evaluation：https://www.researchgate.net/publication/397008000_CELEUS_Certifiable_and_Efficient_LLM_Evaluation_via_E-Processes — §5 Empirical Evaluation；Limitations / counterevidence：https://www.researchgate.net/publication/397008000_CELEUS_Certifiable_and_Efficient_LLM_Evaluation_via_E-Processes — §Appendix A.5 Limitations。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。现有 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已承载通用命题，本材料不要求重复追加。
### [Think Twice Before You Act: Protecting LLM Agents Against Tool Description Poisoning via Isolated Planning](https://arxiv.org/html/2606.20922v1)

**机制与贡献。** The integration of external tools has substantially expanded the capabilities of large language model (LLM) agents, but it also introduces new attack surfaces beyond prompt injection. In particular, cross-tool description poisoning can manipulate planner-visible tool metadata to steer an agent's trajectory, even if the poisoned tool itself is never chosen.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.20922v1#S4 — §4 Isolated Planning Defense；Evaluation：https://arxiv.org/html/2606.20922v1#S5 — §5 Implementation, Performance, and Overhead；Limitations / counterevidence：https://arxiv.org/html/2606.20922v1#S6 — §6 Limitations。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `AGENT-TOOL-CALLING`。现有 [books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md) 顶层 Review notes 前的“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract”已承载通用命题，本材料不要求重复追加。
### [Learning What Not to Forget: Long-Horizon Agent Memory from a Few Kilobytes of Learning](https://arxiv.org/html/2606.20954v1)

**机制与贡献。** Long-running language-model systems accumulate interaction history that outgrows the context window, so they must continually evict. When an eviction policy drops a load-bearing detail, for example an access token issued at login or a path the next call needs, the action fails.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.20954v1#S3 — §3 Long-Horizon Memory Methodology；Evaluation：https://arxiv.org/html/2606.20954v1#S4 — §4 Experimental Setup and §5 Results；Limitations / counterevidence：https://arxiv.org/html/2606.20954v1#S6 — §6 Limitations。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。现有 [books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已承载通用命题，本材料不要求重复追加。
### [Demystifying Numerical Instability in LLM Inference: Achieving Reproducible Inference for Mission-Critical Tasks with HEAL](https://arxiv.org/html/2606.21023v1)

**机制与贡献。** As Large Language Models (LLMs) deploy into mission-critical domains (e.g., finance, medicine, and law), output reproducibility has become a strict system requirement. While practitioners use greedy decoding to eliminate algorithmic stochasticity, empirical deployments with 16-bit precisions still exhibit catastrophic output divergence across heterogeneous GPUs.

**证据边界。** exact-v1 Method：arXiv:2606.21023v1 §2.3 The Microscopic Origin: Boundary Truncation; §3 HEAL; Appendix C HEAL Implementation；Evaluation：arXiv:2606.21023v1 §4 Evaluation; Appendix A Detailed Experimental Setup; Appendix D Additional Performance Results; Appendix E MCR-Bench；Limitations / counterevidence：arXiv:2606.21023v1 §6 Conclusion; Appendix B error, flip-rate and truncation studies。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `INFER-GPU-MEMORY`。已在 [books/part-05-inference-system/54-gpu-memory.md](../../../../books/part-05-inference-system/54-gpu-memory.md) 顶层 Review notes 前定位机制正文（`SF-2026-ARXIV-2606-21023` 正文 1 次、后置 trace 1 次），故保留整合结论。
### [Repeated post-training is not Self-improving: Diagnosing Scientific Amnesia in Continual DPO Pipelines](https://arxiv.org/html/2606.21089v1)

**机制与贡献。** Industrial LLM teams often ship behavior updates by repeatedly DPO-training a base model on sequences of related preference-data campaigns. The dominant failure mode in this regime is not always classical catastrophic forgetting: a pipeline may preserve previously learned behaviors while still failing to accumulate reusable methodological knowledge about how to train the next campaign.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.21089v1 — § exact-v1 anchor: scientific amnesia；Evaluation：https://arxiv.org/html/2606.21089v1 — § exact-v1 evaluation anchor: single-seed 5-condition；Limitations / counterevidence：https://arxiv.org/html/2606.21089v1 — § exact-v1 limitation/counterevidence anchor: diagnostic, not a claim。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `TRAIN-DPO`。现有 [books/part-04-training-system/34-dpo.md](../../../../books/part-04-training-system/34-dpo.md) 顶层 Review notes 前的“Online Discovery 与 Offline Preference Update 可以分权”已承载通用命题，本材料不要求重复追加。
### [Self-Improvement Can Self-Regress: The Rise-and-Collapse Failure Mode of LLM Self-Training](https://arxiv.org/html/2606.21090v1)

**机制与贡献。** Self-improvement can self-regress. In REINFORCE post-training for code, a model can quickly improve on its optimized metric and then collapse within the same training campaign.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.21090v1 — § exact-v1 anchor: rise-then-collapse pattern；Evaluation：https://arxiv.org/html/2606.21090v1 — § exact-v1 evaluation anchor: 10 sequential 20-step campaigns；Limitations / counterevidence：https://arxiv.org/html/2606.21090v1 — § exact-v1 limitation/counterevidence anchor: mixed evidence。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `TRAIN-GRPO`。现有 [books/part-04-training-system/33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) 顶层 Review notes 前的“Tool-use RL 的训练对象包含环境编排”已承载通用命题，本材料不要求重复追加。
### [AgenticOS: An Intent-Oriented Secure Operating System Architecture for Autonomous AI Agents](https://arxiv.org/html/2606.21129v1)

**机制与贡献。** Traditional OS security models based on "resource exposure plus permission checks" face structural challenges as LLM-driven autonomous agents acquire capabilities for planning, tool use, network access, and code execution. Once an agent runtime is compromised through prompt injection or malicious tool outputs, an attacker can compose POSIX-style resource primitives into behaviors far beyond the user's task authorization.

**证据边界。** exact-v1 Method：arXiv:2606.21129v1 §2 Threat Model; §3 Design; §4 Intent ABI；Evaluation：arXiv:2606.21129v1 §5 Security Analysis; §6 Capability Migration；Limitations / counterevidence：arXiv:2606.21129v1 §7 Discussion and Limitations。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。现有 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已承载通用命题，本材料不要求重复追加。
### [Recency/Frequency Adaptive KV Caching for Large Language Model Serving](https://arxiv.org/html/2606.21238v1)

**机制与贡献。** Key-value (KV) caching is a powerful technique for accelerating large language model inference and generation. Inference workloads are large and diverse, which makes them difficult to cache effectively.

**证据边界。** exact-v1 Method：arXiv:2606.21238v1 §3 Method；Evaluation：arXiv:2606.21238v1 §4 Evaluation (DQA, conversation, batch and adaptive partitioning)；Limitations / counterevidence：arXiv:2606.21238v1 §5 Conclusion; §6 Future Work。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `INFER-KV-CACHE`。现有 [books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 顶层 Review notes 前的“从不可逆 Eviction 到可恢复的分层 Recall”已承载通用命题，本材料不要求重复追加。
### [SCOPE: Sequential Conformal Probing for Reliable OOD Rejection in LLM Services](https://arxiv.org/html/2606.21255v1)

**机制与贡献。** Rejecting inputs outside the defined in-distribution (IND) service scope is critical for large language model (LLM) services, where unsupported requests should be filtered before full generation. Existing out-of-distribution (OOD) detectors often rely on final outputs or final-layer representations, leaving unclear where service-boundary signals are most clearly encoded inside the model; they also lack a theoretical guarantee for held-out inputs.

**证据边界。** exact-v1 Method：arXiv:2606.21255v1 §3 Method (§3.2 Calibrated Gate; §3.3 Certifying Boundary)；Evaluation：arXiv:2606.21255v1 §4 Experiments; Appendices A–C and E–F；Limitations / counterevidence：arXiv:2606.21255v1 §5 Conclusion; Appendix D Boundary Construction。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。现有 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已承载通用命题，本材料不要求重复追加。
### ["What Happens Locally, Leaks Globally": Detecting Privacy Leakage Risks in MCP Servers](https://arxiv.org/html/2606.21338v1)

**机制与贡献。** The Model Context Protocol (MCP) has rapidly become the de facto standard for connecting large language models (LLMs) to external resources, but it also introduces a class of privacy risks that existing tools are ill-equipped to detect. Unlike conventional exfiltration bugs, leakage in MCP servers is largely protocol-induced: credentials, API keys, and Personally Identifiable Information (PII) cross the local/LLM boundary simply by being returned, logged, or raised inside a tool handler, with no explicit outbound request in the source code.

**证据边界。** exact-v1 Method：arXiv:2606.21338v1 §3 MCPPrivacyDetector and Taint Analysis；Evaluation：arXiv:2606.21338v1 §4 Evaluation；Limitations / counterevidence：arXiv:2606.21338v1 §6 Conclusion and evaluated MCP/tool boundary。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。现有 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已承载通用命题，本材料不要求重复追加。
### [Calibration Is Not Control: Why LLM-Agent Oversight Needs Intervention](https://arxiv.org/html/2606.21399v1)

**机制与贡献。** Runtime oversight for LLM agents is commonly framed as scalar risk prediction: estimate failure likelihood, confidence, or uncertainty, then intervene once the score crosses a threshold. We argue that this framing targets the wrong object for control.

**证据边界。** exact-v1 Method：arXiv:2606.21399v1 §2 Scalar-control Sufficiency; §3 Prefix Branching; §4 Action-conditioned Controller；Evaluation：arXiv:2606.21399v1 §5 Results; Appendices B–C；Limitations / counterevidence：arXiv:2606.21399v1 §7 Conclusion and action/benchmark boundary。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `AGENT-PLATFORM`。现有 [books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md) 顶层 Review notes 前的“Agent Runtime State Machine；Harness、Protocol 与 Credit 都是 Platform-owned Artifact”已承载通用命题，本材料不要求重复追加。
### [SwarmX: Agentic Scheduling for Low-Latency Agentic Systems](https://arxiv.org/html/2606.21401v1)

**机制与贡献。** Agentic AI applications compose multiple model calls and tool executions, creating new scheduling challenges for GPU-CPU clusters. Their inference time and model-call structure often depend on prompt semantics, making conventional scheduling approaches ineffective for low-latency serving.

**证据边界。** exact-v1 Method：arXiv:2606.21401v1 §3 SwarmX Design; §4 Implementation；Evaluation：arXiv:2606.21401v1 §5 Evaluation (production and overhead)；Limitations / counterevidence：arXiv:2606.21401v1 §6 Production and Operation Experience; §8 Conclusion。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `INFER-SCHEDULING`。现有 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 顶层 Review notes 前的“SLO-aware Admission；Expert weights 与 KV 的联合 working set”已承载通用命题，本材料不要求重复追加。
### [Don't Blindly Trust It: How Unreliable Feedback Breaks Tool-Using LLM Agents](https://arxiv.org/html/2606.21409v1)

**机制与贡献。** Tool-augmented agents are typically evaluated by their gains under reliable external feedback. Yet these gains leave open a key counterfactual: when feedback is unreliable, would the agent be better off receiving no task evidence?

**证据边界。** exact-v1 Method：arXiv:2606.21409v1 §2 Controlled Matched-loop Design；Evaluation：arXiv:2606.21409v1 §3 Inversion; §4 Scope; §5 Failure Structure; Appendices B–C；Limitations / counterevidence：arXiv:2606.21409v1 §6 Fallback-limited Repairs; §9 Limitations。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `AGENT-TOOL-CALLING`。现有 [books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md) 顶层 Review notes 前的“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract”已承载通用命题，本材料不要求重复追加。
### [HERALD: High-Throughput Block Diffusion LLM Serving via CPU-GPU Cooperative KV Cache Retrieval](https://arxiv.org/html/2606.21633v1)

**机制与贡献。** The KV cache dominates GPU memory in long-context LLM serving, crowding out batch capacity and leaving GPU compute idle. Offloading the cache to CPU DRAM restores capacity, but the limited PCIe bandwidth forces state-of-the-art offloading systems to pair it with sparse attention, fetching only a small critical subset of the cache to the GPU.

**证据边界。** exact-v1 Method：arXiv:2606.21633v1 §3 Motivation; §4 HERALD (CPU-GPU retrieval and kernel); §5 Implementation；Evaluation：arXiv:2606.21633v1 §6 Evaluation；Limitations / counterevidence：arXiv:2606.21633v1 §8 Conclusion and evaluated platform boundary。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `INFER-KV-CACHE`。现有 [books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 顶层 Review notes 前的“从不可逆 Eviction 到可恢复的分层 Recall”已承载通用命题，本材料不要求重复追加。
### [Toward Open Weight Models Without Risks: Separating Public and Private Capabilities in LLMs](https://arxiv.org/html/2606.21638v1)

**机制与贡献。** Open-weight Large Language Models (LLMs) enable scientific progress and broad deployment. However, they make it difficult to control access to sensitive capabilities.

**证据边界。** exact-v1 Method：arXiv:2606.21638v1 §3 Tiered Language Models and Training Protocol；Evaluation：arXiv:2606.21638v1 §4 Capability Separation; §5 Cost; §6 Robustness; §7 Scaling；Limitations / counterevidence：arXiv:2606.21638v1 §9 Limitations。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。现有 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已承载通用命题，本材料不要求重复追加。
### [Hallucination as Context Drift: Synchronization Protocols for Multi-Agent LLM Systems](https://arxiv.org/html/2606.21666v1)

**机制与贡献。** Multi-agent LLM systems routinely produce hallucinated outputs that cannot be explained by model deficiencies alone. A significant class of these failures arises not from model incapacity but from context drift: the divergence of internal knowledge states between concurrent agents.

**证据边界。** exact-v1 Method：arXiv:2606.21666v1 §3 Framework (agent context, divergence and shared verification)；Evaluation：arXiv:2606.21666v1 §4 Setup; §5 Results；Limitations / counterevidence：arXiv:2606.21666v1 §6.2 Limitations; §6.3 Contamination。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `AGENT-MULTI-AGENT`。现有 [books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md) 顶层 Review notes 前的“Message 不是 State；Verification Delay 也是拓扑控制状态”已承载通用命题，本材料不要求重复追加。
### [Decodable but Not Faithful: Coupling Natural-Language Rationales to Programmatic Verifiers](https://arxiv.org/html/2606.21678v1)

**机制与贡献。** Language models can generate plausible rationales for their predictions, but these explanations may not faithfully represent the model's internal reasoning. We propose verifier-coupled reasoning, a framework that inserts inline claims into reasoning traces and trains an auxiliary consistency head to predict programmatic verifier outputs from rationale-span hidden states.

**证据边界。** exact-v1 Method：arXiv:2606.21678v1 §4 Method (format, objective, information constraints and diagnostic ladder)；Evaluation：arXiv:2606.21678v1 §5 Experiments; Appendices A–C；Limitations / counterevidence：arXiv:2606.21678v1 §6 Discussion: structural decodability-faithfulness gap。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。现有 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已承载通用命题，本材料不要求重复追加。
### [BatchGen: An Architecture for Scalable and Efficient Batch Inference](https://arxiv.org/html/2606.21712v1)

**机制与贡献。** Batch inference has become a central mode of AI computation, yet existing inference engines still rely on execution models designed for interactive serving. When scaled to millions of sequences, batch workloads reveal two fundamental requirements: the ability to handle extreme inter- and intra-sequence load variation that emerges only at runtime, and the ability to sustain high utilization across large fleets of GPUs.

**证据边界。** exact-v1 Method：arXiv:2606.21712v1 §3 Design Intuitions; §4 Sequence Coroutine; §5 System Design；Evaluation：arXiv:2606.21712v1 §6 Evaluation；Limitations / counterevidence：arXiv:2606.21712v1 §7 Limitations and Future Work。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `INFER-SCHEDULING`。现有 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 顶层 Review notes 前的“SLO-aware Admission；Expert weights 与 KV 的联合 working set”已承载通用命题，本材料不要求重复追加。
### [Safe to Check, Unsafe to Use: Relinking at the Compression Boundary of LLM Agents](https://arxiv.org/html/2606.21732v1)

**机制与贡献。** Summarization-based prompt compression is increasingly used by LLM agents to shorten long, distributed contexts, but it shifts the security boundary: filters inspect the pre-compression prompt while the backend acts on a newly generated compressed context. We identify relinking, a compression-boundary vulnerability where the compressor behaves as a confused deputy, summarizing distributed, locally benign fragments into a complete malicious instruction.

**证据边界。** exact-v1 Method：arXiv:2606.21732v1 §2 System Model; §3 Hypotheses; §4 Attack; §5 Threat; §6 Method; §8 Defense；Evaluation：arXiv:2606.21732v1 §7 Evaluation; Appendices A–C；Limitations / counterevidence：arXiv:2606.21732v1 §10 Conclusion; adaptive-adversary boundary。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。现有 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已承载通用命题，本材料不要求重复追加。
### [CalVerT: Augmenting Agents with Calibrated Verifier Telemetry Improves Action and Learning in Knowledge-Intensive Tasks](https://arxiv.org/html/2606.21777v1)

**机制与贡献。** LLM agents in knowledge intensive question answering take retrieval and reasoning actions with incomplete knowledge about whether their current answer is uncertain, unsupported, or already complete. This produces two failure modes: committing to confident but unsupported answers, which hurts accuracy, and over-retrieving when the evidence in hand already suffices, resulting in wasted compute.

**证据边界。** exact-v1 Method：arXiv:2606.21777v1 §3 Calibrated Verifier Telemetry；Evaluation：arXiv:2606.21777v1 §4 Experiments; Appendices A–G；Limitations / counterevidence：arXiv:2606.21777v1 §5 Conclusion and model-scale/QA scope。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `AGENT-RAG`。现有 [books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md) 顶层 Review notes 前的“Retrieval Control 应成为 Reader 外部的 Typed State”已承载通用命题，本材料不要求重复追加。
### [Agent-Assisted Side-Channel Attacks on Non-Prefix KV Cache in RAG](https://arxiv.org/html/2606.21842v1)

**机制与贡献。** Modern Large Language Model (LLM) serving engines increasingly rely on Retrieval-Augmented Generation (RAG) and non-prefix Key-Value (KV) cache fusion to accelerate long-context, multi-tenant inference. While existing KV cache side-channel attacks require strict linear prefix alignment--rendering them ineffective against real-world RAG queries that contain unique, user-specific private prefixes--we uncover a critical class of structural vulnerabilities inherent to chunk-aware memory scheduling.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.21842v1 — §IV Overview; §V SpliceLeak: Semantic Extraction Methodology; §VI SpliceDefense；Evaluation：https://arxiv.org/html/2606.21842v1 — §VII Evaluation; §VII-A Experimental Setup；Limitations / counterevidence：https://arxiv.org/html/2606.21842v1 — §III Motivation: Limitations of Existing Works; Appendix A Discussion and Future Work。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。现有 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已承载通用命题，本材料不要求重复追加。
### [WiSP: A Working-Set View of Mixture-of-Experts Serving on Extremely Low-Resource Hardware](https://arxiv.org/html/2606.21868v1)

**机制与贡献。** Modern local and agentic workloads often need large-model capacity at low concurrency, but run on GPUs that cannot keep a frontier-scale model resident. Mixture-of-Experts (MoE) models are a natural fit because they activate only a small subset of experts per token, but their sparsity saves computation, not residency: the full expert pool still has to be stored, and any expert used by a layer must be in GPU memory when that layer runs.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.21868v1 — §3 Working-Set Predictor and Runtime Integration；Evaluation：https://arxiv.org/html/2606.21868v1 — §4 Routing Signal and Decode Throughput; §5 Working-Set Value；Limitations / counterevidence：https://arxiv.org/html/2606.21868v1 — §6 Limitations; simulated-constrained-device disclosure。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `INFER-SCHEDULING`。现有 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 顶层 Review notes 前的“SLO-aware Admission；Expert weights 与 KV 的联合 working set”已承载通用命题，本材料不要求重复追加。
### [AgentRiskBOM: A Risk-Scoping Security Bill of Materials for Agentic AI Systems](https://arxiv.org/html/2606.21877v1)

**机制与贡献。** Agentic AI systems retrieve private context, invoke tools, write files, call external services, coordinate with other agents, and may act without human approval. Existing bill of materials artifacts improve transparency for dependencies, model metadata, and training provenance, but leave an agentic transparency gap: capability opacity, the absence of a structured account of what a deployed agent can access, remember, change, delegate, and prove afterward.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.21877v1 — §III AgentRiskBOM Design; §IV Implementation；Evaluation：https://arxiv.org/html/2606.21877v1 — §V Evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.21877v1 — §VII Limitations。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。现有 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已承载通用命题，本材料不要求重复追加。
### [Load Testing for Machine Learning Model Serving Systems at Scale](https://arxiv.org/html/2606.22013v1)

**机制与贡献。** Machine learning (ML) model serving has become a dominant consumer of GPU infrastructure, yet capacity planning in these systems remains largely ad hoc. Under-provisioning leads to service-level objective (SLO) violations and production incidents, while over-provisioning results in substantial resource waste.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.22013v1 — §2 System Design and Methodology; §2.2 Load Testing Strategies; §2.3 Health Assessment Engine；Evaluation：https://arxiv.org/html/2606.22013v1 — §3 Experimental Methodology; §4 Results；Limitations / counterevidence：https://arxiv.org/html/2606.22013v1 — §5 Discussion; Threats to Validity。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-PRODUCTION`。现有 [books/part-06-ai-infrastructure/73-production-best-practice.md](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md) 顶层 Review notes 前的“Load test 是 SLO boundary search”已承载通用命题，本材料不要求重复追加。
### [When Does Belief-Based Agent Memory Help? Reliability-Conditional Updating and Provenance-Capped Poisoning Defense](https://arxiv.org/html/2606.22030v1)

**机制与贡献。** We investigate when belief-based memory actually improves large language model (LLM) agents. Our vehicle is Nous, a long-term memory architecture that represents each entity-attribute pair as a categorical probability distribution updated through closed-form Bayesian inference, with information-theoretic surprise driving belief revision and entropy-based forgetting.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.22030v1 — §3 The Nous Architecture; §3.3 Bayesian Update; §3.7 Pipelines；Evaluation：https://arxiv.org/html/2606.22030v1 — §4 Experimental Setup; §5 Results; §6 Analysis；Limitations / counterevidence：https://arxiv.org/html/2606.22030v1 — §7 Limitations and Future Work; §5 A caveat on the A-MEM comparison。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。现有 [books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已承载通用命题，本材料不要求重复追加。
### [Drowning in Routine: Signal Dilution in Multi-Turn Agent Training](https://arxiv.org/html/2606.22164v1)

**机制与贡献。** Multi-turn agents interleave consequential decisions with routine execution: some actions change the downstream return distribution, while others are necessary but reward-equivalent. The cost of trajectory-level credit assignment, often attributed to long horizons, is in fact governed by decision density $ρ$: the fraction of turns whose actions affect the return.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.22164v1 — §2 Preliminaries; §3 The Signal Dilution Problem；Evaluation：https://arxiv.org/html/2606.22164v1 — §4 Experimental Setup; §5 Results；Limitations / counterevidence：https://arxiv.org/html/2606.22164v1 — §7 Discussion; Appendix A assumptions; Appendix B Diluted Doors。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `TRAIN-GRPO`。现有 [books/part-04-training-system/33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) 顶层 Review notes 前的“Tool-use RL 的训练对象包含环境编排”已承载通用命题，本材料不要求重复追加。
### [StickyInvoc: Rethinking Task Models for High-throughput Workflows in the LLM Era](https://arxiv.org/html/2606.22175v1)

**机制与贡献。** The integration of LLMs into high-throughput workflows is creating a new class of workloads on HPC clusters that promises to accelerate advances in scientific discovery with unprecedented generative capabilities. However, the traditional task model imposes a prohibitive overhead in this new domain: each task must create its computational state from scratch and destroy it upon completion.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.22175v1 — §II Implementation of an LLM-integrated Claim Verification Workflow; §III Transforming the Workflow to Enable StickyInvoc；Evaluation：https://arxiv.org/html/2606.22175v1 — §IV Evaluation; §IV-A Experiment Settings；Limitations / counterevidence：https://arxiv.org/html/2606.22175v1 — §I-E Limitation of the Proposed Approach。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `AGENT-WORKFLOW`。现有 [books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md) 顶层 Review notes 前的“Template、Realized Graph 与 Trace 不是同一个对象”已承载通用命题，本材料不要求重复追加。
### [When Is Emergent Consensus Real? A Measured Coupling Gain and a Validity Diagnostic for LLM Agent Societies](https://arxiv.org/html/2606.22203v1)

**机制与贡献。** LLM "agent societies" are studied via demonstrations of emergent consensus or polarization -- with no measurable control parameter, no theory of when each regime appears, and no test of whether an outcome is a genuine social dynamic or a model artifact. We introduce the coupling gain gamma, measured per-agent by counterfactually perturbing a neighbour's stated opinion.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.22203v1 — §3 The Coupling Gain; §4 Theory；Evaluation：https://arxiv.org/html/2606.22203v1 — §5 Experiments and Results；Limitations / counterevidence：https://arxiv.org/html/2606.22203v1 — §6 Limitations; §5.4 context-dependent transfer boundary。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `AGENT-MULTI-AGENT`。现有 [books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md) 顶层 Review notes 前的“Message 不是 State；Verification Delay 也是拓扑控制状态”已承载通用命题，本材料不要求重复追加。
### [Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice](https://arxiv.org/html/2606.22327v1)

**机制与贡献。** The explosive demand for interactive Large Language Model serving has highlighted the management of the Key-Value cache's dynamic memory footprint as a critical area for performance optimization in inference engines. Modern inference systems overwhelmingly rely on time-centric scheduling heuristics, such as Shortest Job First.

**证据边界。** exact-v1 Method：arXiv:2606.22327v1 §3 Geometry-Aware Online Scheduling; theoretical bound and system design；Evaluation：arXiv:2606.22327v1 §4.1 Evaluation; §4 Experiments；Limitations / counterevidence：arXiv:2606.22327v1 §5 Discussion and Conclusion。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `INFER-SCHEDULING`。已在 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 顶层 Review notes 前定位机制正文（`SF-2026-ARXIV-2606-22327` 正文 1 次、后置 trace 1 次），故保留整合结论。
### [BabelJudge: Measuring LLM-as-a-Judge Reliability Across Languages and Agent Trajectories](https://arxiv.org/html/2606.22329v1)

**机制与贡献。** LLM-as-a-judge has become the dominant approach to scalable evaluation in NLP pipelines, yet judges themselves carry systematic biases that raw accuracy hides: they favor responses placed in slot A (position bias), they prefer longer responses regardless of quality (verbosity bias), and their reliability degrades sharply in lower-resource languages. We introduce BabelJudge, an open-source benchmark and reliability audit framework that measures all four failure modes -- position bias, verbosity bias, order inconsistency, and cross-lingual degradation -- on any judge model, without requiring human preference labels.

**证据边界。** exact-v1 Method：arXiv:2606.22329v1 §3 Methodology；Evaluation：arXiv:2606.22329v1 §5 Results；Limitations / counterevidence：arXiv:2606.22329v1 §8 Limitations and Future Work。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。现有 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已承载通用命题，本材料不要求重复追加。
### [Lingering Authority: Revocable Resource-and-Effect Capabilities for Coding Agents](https://arxiv.org/html/2606.22504v1)

**机制与贡献。** Coding agents often receive broad tool access for an entire task, even when a resource is needed only for one subgoal. We call this gap lingering authority: a temporary resource/effect capability remains exposed after the episode that justified it has closed.

**证据边界。** exact-v1 Method：arXiv:2606.22504v1 §3 Problem and Threat Model; §4 Model of Capabilities and Interfaces; §5 Portico as a Reference Monitor；Evaluation：arXiv:2606.22504v1 §6 Experimental Questions and Setup; §7 Results；Limitations / counterevidence：arXiv:2606.22504v1 §8 Discussion: Revocation Scope and External Validity。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。已在 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前定位机制正文（`SF-2026-ARXIV-2606-22504` 正文 1 次、后置 trace 1 次），故保留整合结论。
### [Governance Decay: How Context Compaction Silently Erases Safety Constraints in Long-Horizon LLM Agents](https://arxiv.org/html/2606.22528v1)

**机制与贡献。** Modern LLM agents increasingly rely on context compaction, summarization, or eviction to keep long-running sessions within a token budget. We show that this context-management layer is a safety-critical failure surface: in-context governance constraints that agents reliably obey while visible can be silently removed by compaction, causing the same agent to perform prohibited tool actions later in the session.

**证据边界。** exact-v1 Method：arXiv:2606.22528v1 §3 Compaction-Eviction Attack; §4 Constraint Pinning；Evaluation：arXiv:2606.22528v1 §5 Results and Robustness；Limitations / counterevidence：arXiv:2606.22528v1 §6 Limitations。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `AGENT-CONTEXT`。已在 [books/part-07-agent/75-context.md](../../../../books/part-07-agent/75-context.md) 顶层 Review notes 前定位机制正文（`SF-2026-ARXIV-2606-22528` 正文 1 次、后置 trace 1 次），故保留整合结论。
### [ASAP: A Disaggregated and Asynchronous Inference System for MoE Prefill](https://arxiv.org/html/2606.22541v1)

**机制与贡献。** Mixture-of-Experts (MoE) models have become the de facto standard for scaling large language models. To maintain computational efficiency, modern MoE serving systems typically employ a hybrid parallelism strategy, combining Data Parallelism (DP) for attention stages with Expert Parallelism (EP) for MoE stages.

**证据边界。** exact-v1 Method：arXiv:2606.22541v1 §3 ASAP Design；Evaluation：arXiv:2606.22541v1 §5 Evaluation；Limitations / counterevidence：arXiv:2606.22541v1 §6 Discussion and Conclusion。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `INFER-PD-DISAGGREGATION`。已在 [books/part-05-inference-system/55-pd-disaggregation.md](../../../../books/part-05-inference-system/55-pd-disaggregation.md) 顶层 Review notes 前定位机制正文（`SF-2026-ARXIV-2606-22541` 正文 1 次、后置 trace 1 次），故保留整合结论。
### [Evidence-Bound Gateway-Path Provenance for Third-Party LLM Inference](https://arxiv.org/html/2606.22560v1)

**机制与贡献。** Third-party LLM gateways have become a critical infrastructure layer between applications and external LLM providers. Conventional gateways do more than forward traffic: they decide which provider and model are called, whether fallback occurred, which stream is delivered, and what usage record should be billed.

**证据边界。** exact-v1 Method：arXiv:2606.22560v1 §3 Provenance Model; §4 Gateway-Path Binding; §5 Implementation；Evaluation：arXiv:2606.22560v1 §7 Evaluation；Limitations / counterevidence：arXiv:2606.22560v1 §9 Limitations and Conclusion。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-GATEWAY`。已在 [books/part-06-ai-infrastructure/62-gateway.md](../../../../books/part-06-ai-infrastructure/62-gateway.md) 顶层 Review notes 前定位机制正文（`SF-2026-ARXIV-2606-22560` 正文 1 次、后置 trace 1 次），故保留整合结论。
### [On Good Authority: Release-Authority Measurement for Registry-Mediated Package Ecosystems](https://arxiv.org/html/2606.22593v1)

**机制与贡献。** Dependency graphs reveal where released code can flow; release-authority records reveal how a release reached users. A package can keep the same downstream exposure while its public authority path changes: a new publisher account, a repository relink, a new workflow, a provenance change, a signing-key movement, or a shift in publication mediation.

**证据边界。** exact-v1 Method：arXiv:2606.22593v1 §3 Authority Model and Measurement; §3.4 Evaluation；Evaluation：arXiv:2606.22593v1 §4 Results；Limitations / counterevidence：arXiv:2606.22593v1 §5 Limitations and Discussion。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-MODEL-REGISTRY`。已在 [books/part-06-ai-infrastructure/59-model-registry.md](../../../../books/part-06-ai-infrastructure/59-model-registry.md) 顶层 Review notes 前定位机制正文（`SF-2026-ARXIV-2606-22593` 正文 1 次、后置 trace 1 次），故保留整合结论。
### [Confidently Wrong: Severity-Aware Calibration of Prompt-Injection Detectors under Attack Shift](https://arxiv.org/html/2606.22659v1)

**机制与贡献。** Prompt-injection detectors are deployed as guards: a model scores an input and a downstream system trusts or blocks it on that score. I study the confidence of these scores, not only their accuracy, when the attack distribution shifts away from the clean benchmark on which the operating point was chosen.

**证据边界。** exact-v1 Method：arXiv:2606.22659v1 §3 Method；Evaluation：arXiv:2606.22659v1 §4 Results；Limitations / counterevidence：arXiv:2606.22659v1 §5 Discussion and Bounded Scope。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。已在 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前定位机制正文（`SF-2026-ARXIV-2606-22659` 正文 1 次、后置 trace 1 次），故保留整合结论。
### [Black-Box Forensics for Conversational LLM Agents](https://arxiv.org/html/2606.22698v1)

**机制与贡献。** As LLM-powered scams proliferate, black-box forensics for conversational LLM agents offers a path to accountability for systems hidden behind anonymous endpoints. Identifying the base model behind a chatbot endpoint (attribution), without model parameter access or knowledge of the hidden system prompt, would let investigators trace AI-enabled scams back to the providers whose models power them.

**证据边界。** exact-v1 Method：arXiv:2606.22698v1 §3 Approach；Evaluation：arXiv:2606.22698v1 §4 Experiments; §4.3 Evaluation；Limitations / counterevidence：arXiv:2606.22698v1 §7 Limitations。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-TRACE`。已在 [books/part-06-ai-infrastructure/69-trace.md](../../../../books/part-06-ai-infrastructure/69-trace.md) 顶层 Review notes 前定位机制正文（`SF-2026-ARXIV-2606-22698` 正文 1 次、后置 trace 1 次），故保留整合结论。
### [GroundEval: A Deterministic Replacement for LLM-as-Judge in Stateful Agent Evaluation](https://arxiv.org/html/2606.22737v1)

**机制与贡献。** Before letting an agent operate over real context, can you prove it used the right evidence? GroundEval turns that question into a deterministic test of what the agent searched, fetched, cited, and was permitted to access.

**证据边界。** exact-v1 Method：arXiv:2606.22737v1 §3 GroundEval Framework；Evaluation：arXiv:2606.22737v1 §5 Evaluation；Limitations / counterevidence：arXiv:2606.22737v1 §10 Limitations。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。已在 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前定位机制正文（`SF-2026-ARXIV-2606-22737` 正文 1 次、后置 trace 1 次），故保留整合结论。
### [GRADE: Graph Representation of LLM Agent Dependency and Execution](https://arxiv.org/html/2606.22741v1)

**机制与贡献。** Can one graph represent every kind of LLM agent's run? A trace records what each step did, never what it relied on, the state it read, and the results it reused.

**证据边界。** exact-v1 Method：arXiv:2606.22741v1 — §2.2 The Formal Class; §Appendix A Formal Class and Subsumption; §A.1 The Formal Tuple and Recovery Maps；Evaluation：arXiv:2606.22741v1 — §E.2 The Limits of the Localization Result；Limitations / counterevidence：arXiv:2606.22741v1 — §3 Two Layers, Two Failure Modes; §3.1 The Two Layers and Their Failure Modes; §4.1 Dependency Structure Predicts Failure Within a Corpus。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `AGENT-WORKFLOW`。现有 [books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md) 顶层 Review notes 前的“Template、Realized Graph 与 Trace 不是同一个对象”已承载通用命题，本材料不要求重复追加。
### [Factored Gossip DiLoCo: Reducing Blocking Communication in DiLoCo](https://arxiv.org/html/2606.22768v1)

**机制与贡献。** To make large-scale distributed training practical outside high-bandwidth datacenters, we must reduce blocking, high-volume synchronization. While DiLoCo communicates infrequently, its outer synchronization remains bandwidth-heavy and brittle to stragglers and transient failures.

**证据边界。** exact-v1 Method：arXiv:2606.22768v1 — §5.1 Training experiments; §Appendix A Factored Gossip DiLoCo: Detailed Algorithm；Evaluation：arXiv:2606.22768v1 — §Appendix E Consensus Error Result and Proof；Limitations / counterevidence：arXiv:2606.22768v1 — §7 Conclusion and Future Work; §Appendix C Further Discussion。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`。现有 [books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md) 顶层 Review notes 前的“异步训练必须分开 Throughput、Freshness 与 Objective Ownership”已承载通用命题，本材料不要求重复追加。
### [Intent-Governed Tool Authorization for AI Agents](https://arxiv.org/html/2606.22916v1)

**机制与贡献。** Tool-using AI agents commonly operate under integration credentials whose static permissions exceed a user's current request. We present Intent-Governed Access Control (IGAC), a server-side authorization layer that converts a trusted request into a short-lived intent certificate, narrows the statically authorized tool manifest, and checks proposed tool and payload effects before execution.

**证据边界。** exact-v1 Method：arXiv:2606.22916v1 — §I-A Relationship to OpenPort Protocol; §IV Threat Model; §IV-A System Boundary；Evaluation：arXiv:2606.22916v1 — §X Evaluation Design; §X-F Expected Analysis Without Fabricated Results; §X-I First-Batch External Benchmark Adaptation；Limitations / counterevidence：arXiv:2606.22916v1 — §IV-E Out of Scope; §XI Limitations and Threats to Validity; §XII-H Effect Estimation and Conservative Failure。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。现有 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已承载通用命题，本材料不要求重复追加。
### [FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training](https://arxiv.org/html/2606.22932v1)

**机制与贡献。** Reverse-mode differentiation computes every weight gradient, writes it to memory, and only then lets the optimizer read it back. This two-phase schedule sets the memory ceiling of modern training: at the seam between the phases, every layer's gradient is live at once.

**证据边界。** exact-v1 Method：arXiv:2606.22932v1 — §FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training; §Our approach.; §2 Method；Evaluation：arXiv:2606.22932v1 — §Appendix E Measurement protocol and variance；Limitations / counterevidence：arXiv:2606.22932v1 — §5 Conclusion; §Scope of the optimizer sweep.。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`。已在 [books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md) 顶层 Review notes 前定位机制正文（`SF-2026-ARXIV-2606-22932` 正文 1 次、后置 trace 1 次），故保留整合结论。
### [MOCAP: Wafer-Scale-Chip-Oriented Memory-Orchestrated Chunked Pipelining Framework for Prefill-Only LLM Inference](https://arxiv.org/html/2606.22968v1)

**机制与贡献。** Large language models (LLMs) are increasingly used in prefill-only workloads, where end-to-end latency is dominated by the prefill phase. For long-context prefill, communication overhead grows with sequence length and quickly becomes a bottleneck on conventional GPU systems, making wafer-scale chips (WSCs) a promising substrate due to their high communication bandwidth and large aggregate compute and memory capacity.

**证据边界。** exact-v1 Method：arXiv:2606.22968v1 — §MOCAP: Wafer-Scale-Chip-Oriented Memory-Orchestrated Chunked Pipelining Framework for Prefill-Only LLM Inference; §3.1 Memory Imbalance Limits Feasible Sequence Length; §4 MOCAP Framework；Evaluation：arXiv:2606.22968v1 — §5 Evaluation；Limitations / counterevidence：arXiv:2606.22968v1 — §7 Conclusion。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `INFER-PREFILL`。现有 [books/part-05-inference-system/43-prefill.md](../../../../books/part-05-inference-system/43-prefill.md) 顶层 Review notes 前的“Prefill pipeline、chunk/memory orchestration 与 placement contract”已承载通用命题，本材料不要求重复追加。
### [LiveServe: Interaction-Aware Serving for Real-Time Omni-Modal LLMs](https://arxiv.org/html/2606.22983v1)

**机制与贡献。** Realtime omni-modal LMs support speech-centric conversations where users stream inputs, hear generated audio, and interrupt freely. Existing Omni-LM serving systems still rely on throughput-oriented LLM scheduling and LRU KV offloading.

**证据边界。** exact-v1 Method：arXiv:2606.22983v1 — §3. OmniCast Architecture；Evaluation：arXiv:2606.22983v1 — §7. Experimental Evaluation; §7.1. Experiment Settings; §7.3. Analysis；Limitations / counterevidence：arXiv:2606.22983v1 — §9. Conclusion。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `INFER-SCHEDULING`。现有 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 顶层 Review notes 前的“SLO-aware Admission；Expert weights 与 KV 的联合 working set”已承载通用命题，本材料不要求重复追加。
### [Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory](https://arxiv.org/html/2606.23195v1)

**机制与贡献。** Large Language Model (LLM) agents increasingly rely on memory systems to maintain long-term coherence. Recent work shows that agent memories degrade during continuous consolidation.

**证据边界。** exact-v1 Method：arXiv:2606.23195v1 — §Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory; §3 Method; §3.2 Memory Store and Consolidation；Evaluation：arXiv:2606.23195v1 — §4.4 Results: Phase 4 (Dose-Response Analysis); §A.3 Retrieved Memory Analysis; §A.5 Sensitivity Analysis: Additive Model Assumption；Limitations / counterevidence：arXiv:2606.23195v1 — §5 Discussion; §6 Conclusion。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。现有 [books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已承载通用命题，本材料不要求重复追加。
### [GIF: Locally Sound Geometric Information Flow Control for LLMs](https://arxiv.org/html/2606.23277v1)

**机制与贡献。** Large language models increasingly mediate interactions between sensitive data, untrusted inputs, and privileged actions in agentic systems, creating security and privacy risks. These range from prompt injections that manipulate downstream tool use to leakage of confidential information through model outputs.

**证据边界。** exact-v1 Method：arXiv:2606.23277v1 — §IV-B System Details; §V-B RQ2: How well does GIF detect policy violations with an LLM-as-a-declassifier design?；Evaluation：arXiv:2606.23277v1 — §III-C Operational Measurement of GIF; §V Evaluation; §V-C 2 Surrogate analysis models；Limitations / counterevidence：arXiv:2606.23277v1 — §VII Conclusion。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。现有 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已承载通用命题，本材料不要求重复追加。
### [Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference](https://arxiv.org/html/2606.23521v1)

**机制与贡献。** Long-running LLM agents keep valuable state resident on GPUs: KV caches, request schedulers, communication state, and sometimes online adapters. Losing this state after a GPU or communicator failure can discard minutes to hours of work, yet existing recovery mechanisms either restart the whole serving stack or require application-specific checkpoint logic inside every attention and runtime component.

**证据边界。** exact-v1 Method：arXiv:2606.23521v1 — §3. Design; §Host-mapped memory.; §4.3. Optional Cross-Architecture Execution and GPU-Initiated Networking；Evaluation：arXiv:2606.23521v1 — §2.4. Motivating Experiment: Host-Side Dirty Detection; §5. Evaluation；Limitations / counterevidence：arXiv:2606.23521v1 — §7. Discussion; §7.5. Limitations and Future Work; §8. Conclusion。这些定位只支持作者披露的模型、workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。

**Books。** 当前唯一 owner 为 `INFER-DECODE`。现有 [books/part-05-inference-system/44-decode.md](../../../../books/part-05-inference-system/44-decode.md) 顶层 Review notes 前的“Decode 的结束条件；Decode-only Compute Branch 仍必须尊重单一 KV Owner”已承载通用命题，本材料不要求重复追加。

## 5. 缺口与下一步

无

准入闭合账目：raw identities=1556；旧候选 provenance=235；V3 候选=50；旧候选降级=185。全部整合项均在当前唯一 owner 的顶层 Review notes 前定位到正文，全部已有覆盖项均绑定正文命题锚点；没有 Books 待写、普通待审或 Materials Request。闭合分类统计已写入 V3 audit：{"AI-for-Science/垂直领域或具身任务，不改变通用基础设施约束": 353, "可映射 ROADMAP，但未改变长期 mechanism/ownership/evaluation/release contract": 429, "局部模型、表示或训练 recipe，未形成长期系统机制": 214, "领域 benchmark/dataset，未形成可迁移评价或发布契约": 510}。

## 6. 复核

复核者：V3 恢复语义复核（独立于旧 V2.1 报告作者；2026-09-10）

结论：通过

复核覆盖 canonical owner 日期、撤回排除、全部旧候选的 false-positive 重裁、32 项分层 false-negative 抽样、closure taxonomy、exact-v1 证据定位、每个 Integrate 的顶层 Review notes 前正文，以及每个 Existing Coverage 的正文命题锚点。压力复核将候选从 80 项进一步收紧为 50 项；明确排除 AI for Science、纯领域 benchmark、局部模型/表示改进和仅凭 ROADMAP 映射的材料，也没有以 Books trace 反向证明准入。机器校验只证明结构一致性。
