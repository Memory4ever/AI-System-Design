# Daily Research — 2026-06-30

**规范：** V3
**窗口：** 2026-06-29T09:00:00+08:00 ～ 2026-06-30T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T09:36:20+08:00

## 1. 结论

本窗恢复 1132 个 canonical arXiv identity，逐项以完整题摘按当前“大模型与大模型基础设施”贡献门槛重审，冻结 55 个候选。旧 V2.1 的 231 个候选只作 provenance，其中 177 项因垂直任务、领域 benchmark、局部表示/方法或仅能映射 ROADMAP 而在候选前关闭；MOPD 是从更广的题摘审计池中纠正准入，因此不改变该旧候选降级账目。没有以 Books trace 反向证明准入。

本轮候选前关闭（不计入 Candidate Denominator）：

- `2606.28666` / `SF-2026-ARXIV-2606-28666` — 把既有 TRiSM、least privilege 与 defence-in-depth 用于医疗报告；题摘给出垂直实证，没有新增可迁移的 agent security state/authority contract
- `2606.29030` / `SF-2026-ARXIV-2606-29030` — 在 MCQ agent 中插入错误 memory 并测 accuracy/ASR，只复现 memory 可污染输出；没有 memory admission/provenance/repair 或新的评估控制契约
- `2606.29775` / `SF-2026-ARXIV-2606-29775` — 摘要明确目标是 MIG 上的 smaller ML models；MF-MARL repartition 与 heuristic scheduling 是通用 GPU job scheduler，不是大模型基础设施特有贡献

候选均复用可核实的 exact-v1 Method / Evaluation / Limitations 定位。Books 结果为 6 项整合、49 项已有覆盖；本次同步没有修改 Books、LEARNING_STATE 或跨日索引。

2026-09-14 按当前来源清单重放 13 个机构每日源并复用仍匹配的 arXiv / exact-v1 / Evidence / Books 证据。机构源补查恢复 Meta BCI 垂直研究并确认 MiMo MOPD 与 arXiv:2606.30406v1 是同一 Source Family；前者题摘关闭，后者因改变 post-training 的 rollout/data/control ownership 而重开，冻结分母由 54 调整为 55。详细过程见 [当前合同再认证](../_sources/daily-20260630/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)。/root 非作者独立复核意见已落实。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [当前合同再认证](../_sources/daily-20260630/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列与窗口定点检索；本窗无范围内新增 | 已检查 | 无 |
| SRC-ANTHROPIC | [当前合同再认证](../_sources/daily-20260630/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-GOOGLE-AI | [当前合同再认证](../_sources/daily-20260630/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：DeepMind / Google Research 官方索引；本窗无范围内新增 | 已检查 | 无 |
| SRC-META-AI | [当前合同再认证](../_sources/daily-20260630/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：06-29 脑信号句子解码是 BCI 垂直研究，无可迁移系统机制，题摘关闭 | 已检查 | 无 |
| SRC-QWEN | [当前合同再认证](../_sources/daily-20260630/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方博客时间序列；本窗无新 family / 重要 revision | 已检查 | 无 |
| SRC-DEEPSEEK | [当前合同再认证](../_sources/daily-20260630/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research / 发布索引；本窗无新 family / 重要 revision | 已检查 | 无 |
| SRC-MOONSHOT | [当前合同再认证](../_sources/daily-20260630/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：Kimi Blog 与官方仓库发布时序；本窗无范围内新增 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | [当前合同再认证](../_sources/daily-20260630/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 publicList 8/8 条按展示首发日期检查；本窗无范围内新增 | 已检查 | 无 |
| SRC-ZAI | [当前合同再认证](../_sources/daily-20260630/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [当前合同再认证](../_sources/daily-20260630/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research、论文目录与发布页；本窗无范围内新增 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [当前合同再认证](../_sources/daily-20260630/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方技术博客与仓库发布时序；本窗无范围内新增 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [当前合同再认证](../_sources/daily-20260630/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：MOPD 与本日 arXiv:2606.30406v1 同 family；按 arXiv 首发归属并纳入候选，官网仅作跨源 provenance | 已检查 | 无 |
| SRC-MINIMAX | [当前合同再认证](../_sources/daily-20260630/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：中英文博客与 Agent Tech Blog；相邻条目为 06-09/06-01，本窗无新增 | 已检查 | 无 |
| SRC-ARXIV | [canonical raw inventory](../_sources/daily-20260630/canonical-raw-identity-inventory-v2.1.json.gz)；1132 个 owner identity 完成题摘筛选；[V3 audit](../_sources/daily-20260630/v3-admission-audit-20260910.json) | 已检查 | 无 |

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability；只有当前题摘贡献成立时才复用旧分数与 exact-v1 定位。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [ConCise: Training-Free Conclusion-Chain State Compression for Cost-Efficient Multi-Step RAG Services](https://arxiv.org/html/2606.28361v1) | 2026-06-30T08:00:00+08:00 | AGENT-RAG；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-RAG，[目标章](../../../../books/part-07-agent/76-rag.md)“跨轮压缩应保存可续写的结论状态，而不是反复搬运历史”下“最直接的多轮 RAG 会把此前检索结果与推理文本重新送入下一轮”段落 |
| [LEDGER: Scaling Agentic Document Editing with Dependency-aware Graph Retrieval](https://arxiv.org/html/2606.28379v1) | 2026-06-30T08:00:00+08:00 | AGENT-WORKFLOW；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[目标章](../../../../books/part-07-agent/81-workflow.md)“Template、Realized Graph 与 Trace 不是同一个对象” |
| [Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems](https://arxiv.org/html/2606.28425v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-SECURITY；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Building to the Test: Coding Agents Deliver What You Check, Not What You Requested](https://arxiv.org/html/2606.28430v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [SWE-MeM: Learning Adaptive Memory Management for Long-Horizon Coding Agents](https://arxiv.org/html/2606.28434v1) | 2026-06-30T08:00:00+08:00 | AGENT-MEMORY；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [Dockerless: Environment-Free Program Verifier for Coding Agents](https://arxiv.org/html/2606.28436v1) | 2026-06-30T08:00:00+08:00 | TRAIN-GRPO；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：TRAIN-GRPO，[目标章](../../../../books/part-04-training-system/33-grpo.md)“Tool-use RL 的训练对象包含环境编排” |
| [KernelSight-LM: A Kernel-Level LLM Inference Simulator](https://arxiv.org/html/2606.28565v1) | 2026-06-30T08:00:00+08:00 | INFER-REQUEST-LIFECYCLE；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-REQUEST-LIFECYCLE，[目标章](../../../../books/part-05-inference-system/42-what-happens-during-inference.md)“请求生命周期把 admission、Prefill、Decode、完成与取消作为显式状态” |
| [When More Sampling Hurts: The Modal Ceiling and Correlation Ceiling of Test-Time Scaling](https://arxiv.org/html/2606.28661v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“相关采样会抬高 Coverage，却压低 Selection 上限”下“把每次采样视为独立，并假定‘只要正确答案出现过，系统就会选中’，在错误模式分散且 selector 近似 oracle 时是合理近似”段落 |
| [Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks](https://arxiv.org/html/2606.28679v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Formal Security Analysis of Agent Protocol Composition](https://arxiv.org/html/2606.28690v1) | 2026-06-30T08:00:00+08:00 | AGENT-MCP；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-MCP，[目标章](../../../../books/part-07-agent/83-mcp.md)“MCP 不等于 Tool Authorization；从单工具扫描到组合级 Admission” |
| [Agent Safety Is Action Alignment](https://arxiv.org/html/2606.28739v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [HyphaeDB: A Living Knowledge Topology for Agent-First Memory](https://arxiv.org/html/2606.28781v1) | 2026-06-30T08:00:00+08:00 | AGENT-MEMORY；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression](https://arxiv.org/html/2606.28831v1) | 2026-06-30T08:00:00+08:00 | INFER-KV-CACHE；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-KV-CACHE，[目标章](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)“从不可逆 Eviction 到可恢复的分层 Recall” |
| [The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems -- and Auditing the Claims It Enables](https://arxiv.org/html/2606.28839v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation](https://arxiv.org/html/2606.28925v1) | 2026-06-30T08:00:00+08:00 | AGENT-MULTI-AGENT；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[目标章](../../../../books/part-07-agent/82-multi-agent.md)“Message 不是 State；Verification Delay 也是拓扑控制状态” |
| [When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration](https://arxiv.org/html/2606.28958v1) | 2026-06-30T08:00:00+08:00 | AGENT-MULTI-AGENT；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[目标章](../../../../books/part-07-agent/82-multi-agent.md)“Message 不是 State；Verification Delay 也是拓扑控制状态” |
| [Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations](https://arxiv.org/html/2606.29033v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation](https://arxiv.org/html/2606.29054v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes](https://arxiv.org/html/2606.29073v1) | 2026-06-30T08:00:00+08:00 | AGENT-MCP；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MCP，[目标章](../../../../books/part-07-agent/83-mcp.md)“MCP 不等于 Tool Authorization；从单工具扫描到组合级 Admission” |
| [DiLaServe: High SLO Attainment Serving for Diffusion Language Models](https://arxiv.org/html/2606.29094v1) | 2026-06-30T08:00:00+08:00 | INFER-SCHEDULING；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-SCHEDULING，[目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md)“SLO-aware Admission；Expert weights 与 KV 的联合 working set” |
| [CADENZA: Compiling Natural-Language Intent into Task-Specific Operator DAGs for Semantic Query Processing](https://arxiv.org/html/2606.29151v1) | 2026-06-30T08:00:00+08:00 | AGENT-RAG；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-RAG，[目标章](../../../../books/part-07-agent/76-rag.md)“从固定 Retriever 演进到可提交的 Logical / Physical Plan”下“外置 retrieval state 后，复杂查询不必直接绑定一个固定 backend”段落 |
| [Pooled Leaderboards Hide System-Specific Winners: A Reporting-Protocol Audit of Offline Root-Cause Analysis Benchmarks](https://arxiv.org/html/2606.29159v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [KernelFlume: Elastic Core-Attention Scaling for Agentic Long-Context Decoding](https://arxiv.org/html/2606.29207v1) | 2026-06-30T08:00:00+08:00 | INFER-DECODE；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-DECODE，[目标章](../../../../books/part-05-inference-system/44-decode.md)“Decode 的结束条件；Decode-only Compute Branch 仍必须尊重单一 KV Owner” |
| [PolicyGuard: A Dialogue-Grounded Sub-Agent Verifier for Policy Adherence in LLM Agents](https://arxiv.org/html/2606.29225v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-SECURITY；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts](https://arxiv.org/html/2606.29279v1) | 2026-06-30T08:00:00+08:00 | AGENT-MEMORY；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [EntroRouter: Learning Efficient Model Routing via Entropy Regulation](https://arxiv.org/html/2606.29424v1) | 2026-06-30T08:00:00+08:00 | INFER-SCHEDULING；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md)“SLO-aware Admission；Expert weights 与 KV 的联合 working set” |
| [Agent-Computer Observation Interfaces Enable Dynamic Computer Use](https://arxiv.org/html/2606.29472v1) | 2026-06-30T08:00:00+08:00 | AGENT-PLATFORM；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-PLATFORM，[目标章](../../../../books/part-07-agent/84-agent-platform.md)“Observation Interface 必须独立于 Action Clock”下“一次动作配一张截图，在静态网页、低交互频率任务中最简单”段落 |
| [Reported Confidence in LLMs Tracks Commitment More Than Correctness](https://arxiv.org/html/2606.29490v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Optimizer Memory Makes Shuffle Order a First-Order Source of Fine-Tuning Noise](https://arxiv.org/html/2606.29554v1) | 2026-06-30T08:00:00+08:00 | TRAIN-PRETRAINING；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-PRETRAINING，[目标章](../../../../books/part-04-training-system/28-pretraining.md)“Optimizer State 也必须服从数据与硬件契约” |
| [Coverage-Driven KV Cache Eviction for Efficient and Improved Inference of LLM](https://arxiv.org/html/2606.29563v1) | 2026-06-30T08:00:00+08:00 | INFER-KV-CACHE；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[目标章](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)“从不可逆 Eviction 到可恢复的分层 Recall” |
| [Speculative Pre-Positioning: Decoding Stateful Sessions to the Next Decision Point Off the Critical Path](https://arxiv.org/html/2606.29565v1) | 2026-06-30T08:00:00+08:00 | INFER-REQUEST-LIFECYCLE；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-REQUEST-LIFECYCLE，[目标章](../../../../books/part-05-inference-system/42-what-happens-during-inference.md)“从机制演进到系统设计”下“请求生命周期最初以一次 prompt→response 为边界”段落 |
| [Langshaw: Declarative Interaction Protocols Based on Sayso and Conflict](https://arxiv.org/html/2606.29601v1) | 2026-06-30T08:00:00+08:00 | AGENT-MULTI-AGENT；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MULTI-AGENT，[目标章](../../../../books/part-07-agent/82-multi-agent.md)“声明式协议约束 Transition，而不是相信参与者会协调”下“集中 coordinator 逐条批准消息和动作”段落 |
| [Energy-Efficient Multimodal Inference Serving with Tri-serve](https://arxiv.org/html/2606.29629v1) | 2026-06-30T08:00:00+08:00 | INFER-SCHEDULING；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md)“SLO-aware Admission；Expert weights 与 KV 的联合 working set” |
| [Demystifying the Design Space and Best Practices for Heterogeneous LLM Inference and Serving](https://arxiv.org/html/2606.29708v1) | 2026-06-30T08:00:00+08:00 | INFER-PD-DISAGGREGATION；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：INFER-PD-DISAGGREGATION，[目标章](../../../../books/part-05-inference-system/55-pd-disaggregation.md)“PD state ownership、异构 memory tier、transfer/SLO 与同步回退” |
| [Diagnosing and Mitigating Context Rot in Long-horizon Search](https://arxiv.org/html/2606.29718v1) | 2026-06-30T08:00:00+08:00 | AGENT-CONTEXT；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-CONTEXT，[目标章](../../../../books/part-07-agent/75-context.md)“Context Compression 必须保留执行状态，而不只是语义” |
| [MemLeak: Diagnosing Information Leaks in Multimodal Agent Memory](https://arxiv.org/html/2606.29788v1) | 2026-06-30T08:00:00+08:00 | AGENT-MEMORY；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [AI Training Manager: Bounded Closed-Loop Control of Adaptive Training Recipes](https://arxiv.org/html/2606.29871v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-TRAINING-OPERATOR；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-TRAINING-OPERATOR，[目标章](../../../../books/part-06-ai-infrastructure/60-training-operator.md)“Live Training Control 必须是可审计 Proposal，而不是直接改 Run” |
| [MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation](https://arxiv.org/html/2606.29914v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios?](https://arxiv.org/html/2606.29920v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [SWE-Together: Evaluating Coding Agents in Interactive User Sessions](https://arxiv.org/html/2606.29957v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Beyond Uniform Experts: Cost-Aware Expert Execution for Efficient Multi-Device MoE Inference](https://arxiv.org/html/2606.29982v1) | 2026-06-30T08:00:00+08:00 | MODEL-MOE；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：MODEL-MOE，[目标章](../../../../books/part-02-model/21-moe.md)“Router 选择 Expert，Placement 决定这次选择能否低成本执行” |
| [HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators](https://arxiv.org/html/2606.29986v1) | 2026-06-30T08:00:00+08:00 | INFER-PD-DISAGGREGATION；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：INFER-PD-DISAGGREGATION，[目标章](../../../../books/part-05-inference-system/55-pd-disaggregation.md)“PD state ownership、异构 memory tier、transfer/SLO 与同步回退” |
| [LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via State Proprioception](https://arxiv.org/html/2606.30005v1) | 2026-06-30T08:00:00+08:00 | AGENT-CONTEXT；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-CONTEXT，[目标章](../../../../books/part-07-agent/75-context.md)“Context Compression 必须保留执行状态，而不只是语义” |
| [On the Internet, Nobody Knows You're an LLM Bot: Unmasking Web Agents with Multi-Layer Fingerprinting](https://arxiv.org/html/2606.30119v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-SECURITY；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [When Is a Draft Accepted? A Theory of Acceptance in Speculative Decoding](https://arxiv.org/html/2606.30265v1) | 2026-06-30T08:00:00+08:00 | INFER-SPECULATIVE-DECODING；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[目标章](../../../../books/part-05-inference-system/48-speculative-decoding.md)“Acceptance 不是独立常数，在线决策必须结算系统状态” |
| [Whose Side Is Your Agent On? Multi-Party Principal Loyalty in LLM Agents](https://arxiv.org/html/2606.30383v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-SECURITY；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Predict, Reuse, and Repair: Accelerating Dynamic Sparse Attention for Long-Context LLM Decoding](https://arxiv.org/html/2606.30389v1) | 2026-06-30T08:00:00+08:00 | INFER-DECODE；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-DECODE，[目标章](../../../../books/part-05-inference-system/44-decode.md)“Decode 的结束条件；Decode-only Compute Branch 仍必须尊重单一 KV Owner” |
| [Energy-Aware Scheduling for Serverless LLM Serving on Shared GPUs](https://arxiv.org/html/2606.30391v1) | 2026-06-30T08:00:00+08:00 | INFER-SCHEDULING；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md)“SLO-aware Admission；Expert weights 与 KV 的联合 working set” |
| [Internal-State Probes Read the Situation, Not the Action: Three Negative Results for Pre-Action Misalignment Monitoring](https://arxiv.org/html/2606.30449v1) | 2026-06-30T08:00:00+08:00 | PLATFORM-MONITORING；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-MONITORING，[目标章](../../../../books/part-06-ai-infrastructure/67-monitoring.md)“calibration-bound sensor、direct profile fallback 与 monitor 不拥有 truth/commit” |
| [Entity Binding Failures in Tool-Augmented Agents](https://arxiv.org/html/2606.30531v1) | 2026-06-30T08:00:00+08:00 | AGENT-TOOL-CALLING；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[目标章](../../../../books/part-07-agent/78-tool-calling.md)“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract” |
| [TraceLab: Characterizing Coding Agent Workloads for LLM Serving](https://arxiv.org/html/2606.30560v1) | 2026-06-30T08:00:00+08:00 | INFER-SCHEDULING；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md)“SLO-aware Admission；Expert weights 与 KV 的联合 working set” |
| [Forensic Trajectory Signatures for Agent Memory Poisoning Detection](https://arxiv.org/html/2606.30566v1) | 2026-06-30T08:00:00+08:00 | AGENT-MEMORY；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [MESA: Prioritizing Vulnerable Communication Channels for Securing Multi-Agent Systems](https://arxiv.org/html/2606.30602v1) | 2026-06-30T08:00:00+08:00 | AGENT-MULTI-AGENT；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[目标章](../../../../books/part-07-agent/82-multi-agent.md)“Message 不是 State；Verification Delay 也是拓扑控制状态” |
| [One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining](https://arxiv.org/html/2606.30634v1) | 2026-06-30T08:00:00+08:00 | TRAIN-PIPELINE-PARALLEL；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-PIPELINE-PARALLEL，[目标章](../../../../books/part-04-training-system/38-pipeline-parallel.md)“异步 Pipeline：去掉 Bubble 会把成本移到参数版本” |
| [MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training](https://arxiv.org/html/2606.30406v1) | 2026-06-29T22:51:28+08:00 | TRAIN-GRPO；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-GRPO，[目标章](../../../../books/part-04-training-system/33-grpo.md)“Rollout Artifact：从样本变为版本化训练对象”下的 OPD 状态所有权、teacher signal、outcome verifier 与 lineage 主线 |

## 4. 证据与知识整合

### [MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training](https://arxiv.org/html/2606.30406v1)

**机制与贡献。** MOPD 将“多域能力同时优化”拆成两个阶段：各领域从同一 SFT 起点独立执行 RL，形成并行 domain teachers；student 再在自己生成的 on-policy rollouts 上按领域路由到冻结 teacher，读取 token-level dense distribution，并用 reverse-KL 更新。这样把 capability production 的 owner 留给各领域 teacher，把可达状态和 rollout data ownership 留给 student，把 integration commit 留给 student learner；teacher 不拥有 rollout，也不自动拥有 outcome truth。实现侧把 teacher 作为独立 prefill service，并可让 teacher prefill 与 student sampling 异步重叠。

**Evaluation contract。** exact-v1 以 Qwen3-30B-A3B 的共同 SFT checkpoint 为起点，覆盖数学、instruction following 与 SWE 三域，对比 Mix-RL、Cascade RL、Off-Policy Finetune 与 Param-Merge。主要评测是 AIME 2025/2026（`avg@32`）、IFBench/IFEval 与 SWE-bench Verified；数学/IF 的最大序列长度为 32,768，SWE 为 65,536，MOPD batch size 2048、每题 1 rollout、领域比例 0.35/0.35/0.30、top-k=64、token advantage clip=5。作者另报告 MiMo-V2-Flash 309B 部署，但没有为该规模提供完整 matched baselines。

**证明与未证明。** 作者实验支持：在披露的三域、模型和超参数下，student-owned rollouts 加 dense teacher distribution 可以比所列基线更好地整合能力；top-k corrected loss 和独立 teacher prefill service 给出可实现路径。它不证明普遍优于 joint RL：MOPD 并非每个原始 benchmark 都最佳，MiMo 结果存在 IFBench 与 SWE 小幅回退；更强但不同起源的 teacher 在 controlled test 中导致初始 KL 从约 0.04 升至约 0.19 并训练崩溃，说明 same-origin/distribution similarity 是成立条件。论文未披露硬件、precision、并发、teacher service SLO 或端到端成本，因而“几乎无 wall-clock overhead”不能外推到生产。

**Trade-off 与 failure mode。** 独立 domain RL 降低跨域耦合、允许并行开发，并以 student on-policy state 减少 offline exposure bias；代价是额外 teacher forward、路由与 logits 传输、多个 teacher artifact 和服务生命周期。domain router 错误、teacher/student distribution divergence、teacher 本身弱于 student、top-k 截断、异步结果陈旧或领域比例变化都会把 dense signal 变成错误更新。任务同质、teacher 服务成本过高或静态示范已覆盖部署状态时，Mix-RL、离线蒸馏或单 teacher 路径仍更简单。

**Books。** 当前唯一 owner 为 `TRAIN-GRPO`。[books/part-04-training-system/33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) 顶层 Review notes 前已经规定：student 产生自身 on-policy rollout；teacher 只提供 token guidance；outcome verifier 决定轨迹接纳；teacher/student lineage、domain、support 与 objective 进入 artifact identity；teacher mismatch 时必须拒绝或回退。MOPD 的多 teacher 路由是这条既有主线的多域实例，没有改变 owner 或长期结论，故为 `No Change — Existing Coverage`。

### [ConCise: Training-Free Conclusion-Chain State Compression for Cost-Efficient Multi-Step RAG Services](https://arxiv.org/html/2606.28361v1)

**机制与贡献。** Multi-step retrieval-augmented generation (RAG) has been widely deployed as LLM-powered web services for complex question answering, where iterative retrieval-reasoning rounds deliver strong multi-hop accuracy. However, this paradigm causes historical documents and reasoning traces to accumulate across rounds, inflating cumulative input tokens approximately as $O(N^2)$ with progressively increasing noise density.

**证据边界。** exact-v1 Method：arXiv:2606.28361v1 §III model; §IV Algorithm; §V analysis；Evaluation：arXiv:2606.28361v1 §VI Experiment；Limitations / counterevidence：arXiv:2606.28361v1 §VI-D deployment implications; §VIII。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-RAG`。已在 [books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md) 顶层 Review notes 前反查机制正文；`SF-2026-ARXIV-2606-28361` 在正文出现 1 次、后置 trace 出现 4 次。
### [LEDGER: Scaling Agentic Document Editing with Dependency-aware Graph Retrieval](https://arxiv.org/html/2606.28379v1)

**机制与贡献。** We introduce LEDGER to tackle the novel context engineering challenge of agentic document editing, where localized edits to long, structured documents must be applied efficiently without breaking cross-references or semantic consistency. LEDGER constructs a lightweight dependency graph that explicitly models document structure, including hierarchical organization, explicit references, implicit dependencies, and semantic relationships.

**证据边界。** exact-v1 Method：arXiv:2606.28379v1 §3 LEDGER (graph, retrieval and consistency)；Evaluation：arXiv:2606.28379v1 §4 Experiments; Appendices C–E；Limitations / counterevidence：arXiv:2606.28379v1 §5 Conclusion and absence of a formal semantic guarantee。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-WORKFLOW`。[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md) 顶层 Review notes 前的“Template、Realized Graph 与 Trace 不是同一个对象”已覆盖通用命题，不重复追加。
### [Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems](https://arxiv.org/html/2606.28425v1)

**机制与贡献。** Increasingly autonomous agentic AI systems pose novel multi-agent risks, such as secret collusion via covert communication channels. The natural defence to these collusion attempts is to monitor plain-text communication, but the efficacy of monitors has been called into doubt by increasingly sophisticated model steganography; indeed, some theoretical schemes have been proposed that are information-theoretically or computationally indistinguishable from good-faith plain-text communication.

**证据边界。** exact-v1 Method：arXiv:2606.28425v1 — §Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems; §3 Methodology; §Algorithmic coordination.；Evaluation：arXiv:2606.28425v1 — §2 Background and Problem Setup; §4 Experiments；Limitations / counterevidence：arXiv:2606.28425v1 — §Monitored-channel threat model.; §4.4 Limitations; §5 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [Building to the Test: Coding Agents Deliver What You Check, Not What You Requested](https://arxiv.org/html/2606.28430v1)

**机制与贡献。** Benchmarks are widely used to evaluate task completion by Large Language Models (LLMs), but this approach has accumulated construction-validity problems, and a passing score may not show whether the requested task was delivered. We study both problems.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28430v1 — §3 Library audit methodology; An honest oracle is enough; the exposed signal is not the per-subsystem driver.; c9 removes c3’s guards by design, and remains honest.；Evaluation：https://arxiv.org/html/2606.28430v1 — §2 Setup; Unit of analysis: the production agent.; Code-generation benchmarks.；Limitations / counterevidence：https://arxiv.org/html/2606.28430v1 — §6 Threats to validity; 8 Discussion; 9 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [SWE-MeM: Learning Adaptive Memory Management for Long-Horizon Coding Agents](https://arxiv.org/html/2606.28434v1)

**机制与贡献。** Long-horizon software engineering agents often need to manage lengthy and noisy interaction histories under limited context budgets. Existing memory management methods typically rely on static compression workflows or impose rigid constraints on compression timing and granularity.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28434v1 — §2 Proposed Approach; 2.1 Memory Management Tool Design; Appendix A Method Details；Evaluation：https://arxiv.org/html/2606.28434v1 — §3 Experiment; 3.3 Experiment Details; 3.4 Main Results；Limitations / counterevidence：https://arxiv.org/html/2606.28434v1 — §6 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已覆盖通用命题，不重复追加。
### [Dockerless: Environment-Free Program Verifier for Coding Agents](https://arxiv.org/html/2606.28436v1)

**机制与贡献。** Program verifiers play a central role in training coding agents, including selecting trajectories for supervised fine-tuning (SFT) and providing rewards for reinforcement learning (RL). Standard execution-based verification requires running unit tests inside per-repository environments such as Docker images, incurring substantial environment setup costs.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28436v1 — §2 Methodology; 2.2 Architecture of Dockerless; 2.3 Dockerless Training；Evaluation：https://arxiv.org/html/2606.28436v1 — §3 Experimental Settings; Benchmarks.; Evaluation protocol.；Limitations / counterevidence：https://arxiv.org/html/2606.28436v1 — §6 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `TRAIN-GRPO`。[books/part-04-training-system/33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) 顶层 Review notes 前的“Tool-use RL 的训练对象包含环境编排”已覆盖通用命题，不重复追加。
### [KernelSight-LM: A Kernel-Level LLM Inference Simulator](https://arxiv.org/html/2606.28565v1)

**机制与贡献。** As large language models (LLMs) move into production serving, practitioners must rapidly evaluate inference performance across diverse hardware, models, and serving parameters to meet cost and latency targets. However, the end-to-end behavior of LLMs couples serving-layer policies with low-level GPU kernel execution and rapidly evolving architectures, forcing slow, deployment-specific benchmarking that is hard to generalize.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28565v1 — §2.1. Modern LLMs and Inference Frameworks; 3.3. Gaps in Existing Approaches; 4. Tool Architecture and Methodologies；Evaluation：https://arxiv.org/html/2606.28565v1 — §5.2. Production Kernel Microbenchmarking; 6. Experimental Setup; 7. Results and Analysis；Limitations / counterevidence：https://arxiv.org/html/2606.28565v1 — §8. Conclusions; Appendix B Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-REQUEST-LIFECYCLE`。[books/part-05-inference-system/42-what-happens-during-inference.md](../../../../books/part-05-inference-system/42-what-happens-during-inference.md) 顶层 Review notes 前的“请求生命周期把 admission、Prefill、Decode、完成与取消作为显式状态”已覆盖通用命题，不重复追加。
### [When More Sampling Hurts: The Modal Ceiling and Correlation Ceiling of Test-Time Scaling](https://arxiv.org/html/2606.28661v1)

**机制与贡献。** People overthink; language models over-sample, and the extra effort can talk both into a worse answer. Reasoning systems answer a hard question by sampling it many times (test-time scaling), and the more they draw, the more often a correct answer turns up somewhere, so coverage, the fraction of problems with at least one correct try, climbs and appears to be progress.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28661v1 — §Proposition 1 (Design effect of test-time sampling) .; Two-stage design effect.；Evaluation：https://arxiv.org/html/2606.28661v1 — §1 Introduction and roadmap; 2 Test-time sampling is cluster sampling；Limitations / counterevidence：https://arxiv.org/html/2606.28661v1 — §6 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。已在 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前反查机制正文；`SF-2026-ARXIV-2606-28661` 在正文出现 2 次、后置 trace 出现 1 次。
### [Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks](https://arxiv.org/html/2606.28679v1)

**机制与贡献。** Tool-using LLM agents increasingly read untrusted content while holding side-effecting tools such as payments, email, CRM, and infrastructure APIs, yet common framework defaults still conflate tool exposure with authorization. We audit whether LangChain/LangGraph, LlamaIndex, and the Stripe Agent Toolkit re-authorize each model-emitted call, with concrete argument values, before execution.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28679v1 — §Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; III The Cross-Framework Gap; III-A Method and selection；Evaluation：https://arxiv.org/html/2606.28679v1 — §VI Evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.28679v1 — §Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; II Threat Model; II-A Boundary and adversary；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [Formal Security Analysis of Agent Protocol Composition](https://arxiv.org/html/2606.28690v1)

**机制与贡献。** AI agent protocols define how agents use tools, delegate work, and coordinate across software systems, but their security requirements remain incomplete and inconsistently enforced across deployments. We present AgentThread, a source-linked framework for security assurance analysis of agent protocols, from specification text to running SDKs.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28690v1 — §4. The AgentThread Framework; 4.5. Composition Methodology；Evaluation：https://arxiv.org/html/2606.28690v1 — §Formal Security Analysis of Agent Protocol Composition; 6. Evaluation; 6.1. Evaluation Setup；Limitations / counterevidence：https://arxiv.org/html/2606.28690v1 — §6.4. RQ3: Composition Failures; 7. Discussion; 9. Threats to Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MCP`。[books/part-07-agent/83-mcp.md](../../../../books/part-07-agent/83-mcp.md) 顶层 Review notes 前的“MCP 不等于 Tool Authorization；从单工具扫描到组合级 Admission”已覆盖通用命题，不重复追加。
### [Agent Safety Is Action Alignment](https://arxiv.org/html/2606.28739v1)

**机制与贡献。** Large language models increasingly act as agents: they call tools, move money, delete records, and send messages on a user's behalf. To keep them safe, practitioners imported the chatbot-era recipe (train the model to refuse unsafe inputs) into the agentic setting, and treat the resulting capability loss as a manageable ``alignment tax.'' We argue this is a \emph{category error}.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28739v1 — §Report GitHub Issue; Agent Safety Is Action Alignment；Evaluation：https://arxiv.org/html/2606.28739v1 — §5.3. Relational and Deployment-Conditioned Evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.28739v1 — §5.2. External Enforcement at the Action Boundary; 7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [HyphaeDB: A Living Knowledge Topology for Agent-First Memory](https://arxiv.org/html/2606.28781v1)

**机制与贡献。** Every existing vector database and agent memory framework treats memory as passive storage that agents query explicitly. No system propagates knowledge between agents through the memory layer itself.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28781v1 — §2.1 Agent Memory Systems; 3 Architecture; 4.1 Propagation Algorithm；Evaluation：https://arxiv.org/html/2606.28781v1 — §6 Theoretical Analysis; 8 Competitive Analysis；Limitations / counterevidence：https://arxiv.org/html/2606.28781v1 — §9 Discussion; 9.2 Limitations and Future Work; 10 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已覆盖通用命题，不重复追加。
### [HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression](https://arxiv.org/html/2606.28831v1)

**机制与贡献。** Long-context LLM inference faces a fundamental conflict: head-adaptive compression algorithms (e.g., Top-$p$ nucleus sampling) offer superior accuracy by dynamically fluctuating memory budgets, yet modern inference engines (e.g., vLLM) demand rigid, static memory patterns to leverage CUDA Graphs and PagedAttention. We resolve this ``Static-Dynamic'' mismatch with HARD-KV, a unified framework that that bridges dynamic selection with rigid system constraints.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28831v1 — §System-Algorithm Co-Design in LLM Inference; 3 The Hard-KV Design; 3.1 The Framework Overview；Evaluation：https://arxiv.org/html/2606.28831v1 — §4 Experiment; Appendix C Experiments Details; C.3 Further Experiment Results；Limitations / counterevidence：https://arxiv.org/html/2606.28831v1 — §5 Conclusion and Future Work; Appendix B Further Discussions on KV Index Regularization; B.2 Discussion on trade-off in the Index Management for Layerwise Selection；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-KV-CACHE`。[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 顶层 Review notes 前的“从不可逆 Eviction 到可恢复的分层 Recall”已覆盖通用命题，不重复追加。
### [The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems -- and Auditing the Claims It Enables](https://arxiv.org/html/2606.28839v1)

**机制与贡献。** We introduce the Contagion Tensor, a measurement framework for quantifying how large language model (LLM) output distributions couple across modalities, agents, and time steps. From the tensor we derive the Coupling Amplification Factor (CAF), a family of ratio-based metrics sharing the form CAF = E[T_condition] / E[T_baseline], providing unitless, baseline-referenced measurement with bootstrap confidence intervals.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28839v1 — §The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems —and Auditing the Claims It Enables; Multi-agent LLM systems.; Network contagion and spectral methods.；Evaluation：https://arxiv.org/html/2606.28839v1 — §LLM bias evaluation.; 4.1.2 Experiment 1: Full CAF Matrix; 4.1.3 Experiment 2: Modality Ablation；Limitations / counterevidence：https://arxiv.org/html/2606.28839v1 — §4.1.4 Experiment 3: Real-API with Functional BOUNDARY_SYNC; 6 Discussion; 7 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation](https://arxiv.org/html/2606.28925v1)

**机制与贡献。** Tool and agent routing from natural-language prompts is naturally a set-valued prediction problem: a single query may require multiple agents, while over-selection increases execution cost. The benchmark introduced here is derived from WildChat and contains 3,000 prompts over a fixed 12-agent catalog, with AI-assisted heuristic labels under a fixed schema and controlled rebalancing for multi-label evaluation.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28925v1 — §2.1. Tool/Agent Routing in LLM Systems; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 2.6. Multi-Agent Systems and Task Decomposition；Evaluation：https://arxiv.org/html/2606.28925v1 — §Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 3.1. Problem setup and notation；Limitations / counterevidence：https://arxiv.org/html/2606.28925v1 — §7. Discussion; 8. Limitations; 10. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MULTI-AGENT`。[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md) 顶层 Review notes 前的“Message 不是 State；Verification Delay 也是拓扑控制状态”已覆盖通用命题，不重复追加。
### [When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration](https://arxiv.org/html/2606.28958v1)

**机制与贡献。** LLM agents can share more than text. In some systems, an agent can send a short visible message while also passing its full KV-cache state to another model.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28958v1 — §Report GitHub Issue; When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration；Evaluation：https://arxiv.org/html/2606.28958v1 — §5 Benchmark and Experimental Setup; 8 Defense Diagnostics and Trade-Off Analysis；Limitations / counterevidence：https://arxiv.org/html/2606.28958v1 — §3 Problem Setting and Threat Model; 8.4 Transport Integrity and Fail-Closed Boundary; 9 Failure Modes and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MULTI-AGENT`。[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md) 顶层 Review notes 前的“Message 不是 State；Verification Delay 也是拓扑控制状态”已覆盖通用命题，不重复追加。
### [Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations](https://arxiv.org/html/2606.29033v1)

**机制与贡献。** Evaluating AI/Agentic system outputs reliably requires human judgment, but how one incorporates the human determines whether one gets a real quality signal or expensive theater. The common approaches either accidentally anchor human experts (leading to rubber-stamping) or leave them unsupported in cognitively demanding labeling tasks.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.29033v1 — §Approach 1: Human Verification of AI Proposals.; Approach 2: Manual Test Sets.; Approach 3: Humans Specify Criteria, AI Applies Them at Scale.；Evaluation：https://arxiv.org/html/2606.29033v1 — §Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations; 4. Avoiding Evaluation Tropes；Limitations / counterevidence：https://arxiv.org/html/2606.29033v1 — §6. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation](https://arxiv.org/html/2606.29054v1)

**机制与贡献。** Large language models (LLMs) deployed for structured generation (NER, JSON extraction, QA, and classification) lack formal reliability guarantees, and standard heuristic abstention policies miss user-specified risk targets by 7.5--12.5%. We characterize when conformal risk control (CRC) can certify structured LLM outputs and when it provably cannot.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.29054v1 — §2 Method; Ministral violations expose framework limits.; Practical decision framework.；Evaluation：https://arxiv.org/html/2606.29054v1 — §Problem setup.; 3 Experiments; 3.1 Setup；Limitations / counterevidence：https://arxiv.org/html/2606.29054v1 — §4 Discussion; 6 Conclusion; Threats to validity and limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes](https://arxiv.org/html/2606.29073v1)

**机制与贡献。** Model Context Protocol (MCP)-style ecosystems give language-model applications a practical connection layer for tools, resources, prompts, and transports. As agents move from connection to execution, security decisions often remain split across clients, servers, prompts, approval dialogs, OAuth deployments, and logs.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.29073v1 — §5 HCP Design; 6 Benchmark Method; 7.7 Ecosystem Measurement；Evaluation：https://arxiv.org/html/2606.29073v1 — §From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes; 6 Benchmark Method; 7 Evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.29073v1 — §3 Threat Model; 6.3 Reproducibility Boundary; 8 Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MCP`。[books/part-07-agent/83-mcp.md](../../../../books/part-07-agent/83-mcp.md) 顶层 Review notes 前的“MCP 不等于 Tool Authorization；从单工具扫描到组合级 Admission”已覆盖通用命题，不重复追加。
### [DiLaServe: High SLO Attainment Serving for Diffusion Language Models](https://arxiv.org/html/2606.29094v1)

**机制与贡献。** Diffusion language models (DLMs) have recently emerged as a promising alternative to conventional autoregressive language models. By generating multiple tokens in parallel during each denoising step, they offer higher inference throughput while maintaining competitive quality.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.29094v1 — §3.1. Design Overview; Appendix C Algorithm for Supporting Approximate KV Caching；Evaluation：https://arxiv.org/html/2606.29094v1 — §5. Evaluation; 5.1. Experimental Setup; 5.3. Accuracy Benchmarks；Limitations / counterevidence：https://arxiv.org/html/2606.29094v1 — §7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-SCHEDULING`。[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 顶层 Review notes 前的“SLO-aware Admission；Expert weights 与 KV 的联合 working set”已覆盖通用命题，不重复追加。
### [CADENZA: Compiling Natural-Language Intent into Task-Specific Operator DAGs for Semantic Query Processing](https://arxiv.org/html/2606.29151v1)

**机制与贡献。** Semantic query processing engines (SQPEs) extend relational query processing with semantic operators that are executed via model inference over unstructured data. Optimizing such queries is inherently multi-objective: model inference dominates latency and monetary cost, and outputs are stochastic and backend-dependent, so quality must be optimized alongside efficiency.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.29151v1 — §2.2 System Architecture; 4 Logical Planner; 5 Physical Planner；Evaluation：https://arxiv.org/html/2606.29151v1 — §7 Experiments; 7.1 Experimental Setup；Limitations / counterevidence：https://arxiv.org/html/2606.29151v1 — §6.3 Robustness; G Validation Set Noise。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-RAG`。已在 [books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md) 顶层 Review notes 前反查机制正文；`SF-2026-ARXIV-2606-29151` 在正文出现 1 次、后置 trace 出现 2 次。
### [Pooled Leaderboards Hide System-Specific Winners: A Reporting-Protocol Audit of Offline Root-Cause Analysis Benchmarks](https://arxiv.org/html/2606.29159v1)

**机制与贡献。** Offline root-cause-analysis (RCA) benchmarks commonly rank methods by a single pooled top-1 accuracy across multiple subsystems, and engineers often read the pooled winner as a recommendation for their own subsystem. We audit that reading on three public RCA benchmark families -- OpenRCA, RCAEval, and PetShop -- covering 11 subsystems and 778 matched scoring units.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.29159v1 — §Root-cause-analysis methods on offline benchmarks; reporting-protocol formulation；Evaluation：https://arxiv.org/html/2606.29159v1 — §Benchmark validity and leaderboard instability in ML; system-specific results；Limitations / counterevidence：https://arxiv.org/html/2606.29159v1 — §6 Discussion, Limitations, and Recommendations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [KernelFlume: Elastic Core-Attention Scaling for Agentic Long-Context Decoding](https://arxiv.org/html/2606.29207v1)

**机制与贡献。** LLM serving is increasingly dominated by long and dynamic decode workloads from agents, reasoning models, and extended conversations. When bursty long-context demand exceeds deployed capacity, existing serving systems typically scale out by launching additional serving instances with model replicas.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.29207v1 — §3 System Overview; KernelFlume generation and verification pipeline；Evaluation：https://arxiv.org/html/2606.29207v1 — §6 Evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.29207v1 — §2.4 Limitations of Existing Elastic Scaling。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-DECODE`。[books/part-05-inference-system/44-decode.md](../../../../books/part-05-inference-system/44-decode.md) 顶层 Review notes 前的“Decode 的结束条件；Decode-only Compute Branch 仍必须尊重单一 KV Owner”已覆盖通用命题，不重复追加。
### [PolicyGuard: A Dialogue-Grounded Sub-Agent Verifier for Policy Adherence in LLM Agents](https://arxiv.org/html/2606.29225v1)

**机制与贡献。** LLM agents handle user requests on behalf of organizations through tool calls and must follow the company policies stated in their system prompts. Prior work approaches this as a safeguarding problem -- external checks that block non-compliant agent actions.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.29225v1 — §3 Method; PolicyGuard pre-commit policy gate；Evaluation：https://arxiv.org/html/2606.29225v1 — §4 Experiments；Limitations / counterevidence：https://arxiv.org/html/2606.29225v1 — §Discussion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts](https://arxiv.org/html/2606.29279v1)

**机制与贡献。** LLM agents carry conclusions across steps and sessions in compressed memory, and memory products (e.g., mem0, LangMem) rewrite conversation into stored "facts" that later steps trust. We show this rewriting manufactures confidence: across our constructed agent settings, a casual, hedged remark becomes a confident, dated assertion the agent then obeys like a verified fact, granting every above-clearance request it faces.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.29279v1 — §Agent memory and compression; hearsay-provenance mechanism；Evaluation：https://arxiv.org/html/2606.29279v1 — §3 Results；Limitations / counterevidence：https://arxiv.org/html/2606.29279v1 — §Conclusion and source-provenance scope。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已覆盖通用命题，不重复追加。
### [EntroRouter: Learning Efficient Model Routing via Entropy Regulation](https://arxiv.org/html/2606.29424v1)

**机制与贡献。** Model routing balances solution accuracy and computational cost by selecting among models of varying capabilities. While recent multi-round frameworks interleave reasoning and planning, we identify a structural failure mode termed Trust Region Collapse.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.29424v1 — §2.1 Problem Formulation; EntroRouter；Evaluation：https://arxiv.org/html/2606.29424v1 — §4 Experiments；Limitations / counterevidence：https://arxiv.org/html/2606.29424v1 — §5 Discussion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-SCHEDULING`。[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 顶层 Review notes 前的“SLO-aware Admission；Expert weights 与 KV 的联合 working set”已覆盖通用命题，不重复追加。
### [Agent-Computer Observation Interfaces Enable Dynamic Computer Use](https://arxiv.org/html/2606.29472v1)

**机制与贡献。** SWE-agent established the action interface as an underexplored design axis for software-engineering agents; we make the analogous case for the observation interface in computer-use (CU) agents. Current CU agents, closed and open-source alike, tie observation to action--one screenshot every 3-5 s, no audio--leaving them blind and deaf between screenshots to video, animations, transient UI events, meetings, and spoken instructions.

**证据边界。** exact-v1 Method：https://arxiv.org/pdf/2606.29472v1 — §3 Agent-Computer Observation Interface: gated keyframes, audio transcription and persistent narration；Evaluation：https://arxiv.org/pdf/2606.29472v1 — §4 DynaCU-Bench design; 5 Main results and ablations；Limitations / counterevidence：https://arxiv.org/pdf/2606.29472v1 — §5 per-model component ablation: keyframe regression through image-token dilution。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-PLATFORM`。已在 [books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md) 顶层 Review notes 前反查机制正文；`SF-2026-ARXIV-2606-29472` 在正文出现 1 次、后置 trace 出现 2 次。
### [Reported Confidence in LLMs Tracks Commitment More Than Correctness](https://arxiv.org/html/2606.29490v1)

**机制与贡献。** Confidence is an estimate of the probability that a chosen answer is correct. Verbal confidence reports are widely used as uncertainty measures in large language models, but whether they are best understood as estimates of correctness is unclear.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.29490v1 — §1.1 Supplemental Methods; confidence-commitment calibration；Evaluation：https://arxiv.org/html/2606.29490v1 — §1.2 Supplemental Results；Limitations / counterevidence：https://arxiv.org/html/2606.29490v1 — §Conclusion and evaluated-distribution scope。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [Optimizer Memory Makes Shuffle Order a First-Order Source of Fine-Tuning Noise](https://arxiv.org/html/2606.29554v1)

**机制与贡献。** Shuffle order can be a larger source of fine-tuning noise than a memoryless analysis predicts: fixed-clock optimizer memory makes local equal-multiset contrasts first order in the learning rate rather than second order, and the resulting order channel can be large enough for a single seed to flip a close A/B comparison. We isolate this mechanism and derive a fit-free way to size the noise it produces.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.29554v1 — §Optimizer-shuffle exponent and mechanism；Evaluation：https://arxiv.org/html/2606.29554v1 — §5 Empirical evidence；Limitations / counterevidence：https://arxiv.org/html/2606.29554v1 — §7 Discussion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `TRAIN-PRETRAINING`。[books/part-04-training-system/28-pretraining.md](../../../../books/part-04-training-system/28-pretraining.md) 顶层 Review notes 前的“Optimizer State 也必须服从数据与硬件契约”已覆盖通用命题，不重复追加。
### [Coverage-Driven KV Cache Eviction for Efficient and Improved Inference of LLM](https://arxiv.org/html/2606.29563v1)

**机制与贡献。** Large language models (LLMs) excel at complex tasks like question answering and summarization, thanks to their ability to handle long-context inputs. However, deploying LLMs is costly, not only due to the high computational demands of quadratic complexity of self-attention and auto-regressive generation, but also because of the significant memory overhead required for storing the key-value (KV) cache during inference.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.29563v1 — §3 Coverage Hypothesis for KV-Cache Eviction; 4 KV Cache Eviction with Coverage；Evaluation：https://arxiv.org/html/2606.29563v1 — §5 Experiments; 5.1 Experimental setup；Limitations / counterevidence：https://arxiv.org/html/2606.29563v1 — §5.3 Discussion; 5.3.5 Computational Complexity。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-KV-CACHE`。[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 顶层 Review notes 前的“从不可逆 Eviction 到可恢复的分层 Recall”已覆盖通用命题，不重复追加。
### [Speculative Pre-Positioning: Decoding Stateful Sessions to the Next Decision Point Off the Critical Path](https://arxiv.org/html/2606.29565v1)

**机制与贡献。** A stateless inference server (vLLM, SGLang, TensorRT-LLM) idles between requests while the accelerator waits; a stateful session reclaims that idle time. Speculative pre-positioning decodes the session forward to its next decision point with the target model's own forward pass and no draft model, moving the cross-request prefill and entry-decode off the critical path: the next request resumes from a pre-paid entry on its delta, or, when a confidence gate fires, is answered from a cached distribution in one near-constant vocabulary scan with no decode, at a cost only of energy and a rare, bounded false accept.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.29565v1 — §2 Problem Formulation; speculative pre-positioning state machine；Evaluation：https://arxiv.org/html/2606.29565v1 — §4 Experimental Setup; 5 Evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.29565v1 — §6 Discussion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-REQUEST-LIFECYCLE`。已在 [books/part-05-inference-system/42-what-happens-during-inference.md](../../../../books/part-05-inference-system/42-what-happens-during-inference.md) 顶层 Review notes 前反查机制正文；`SF-2026-ARXIV-2606-29565` 在正文出现 1 次、后置 trace 出现 2 次。
### [Langshaw: Declarative Interaction Protocols Based on Sayso and Conflict](https://arxiv.org/html/2606.29601v1)

**机制与贡献。** Current languages for specifying multiagent protocols either over-constrain protocol enactments or complicate capturing their meanings. We propose Langshaw, a declarative protocol language based on (1) sayso, a new construct that captures who has priority over setting each attribute, and (2) nono and nogo, two constructs to capture conflicts between actions.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.29601v1 — §Approach; sayso, nono and nogo protocol semantics；Evaluation：https://arxiv.org/html/2606.29601v1 — §6.2 Empirical Results; safety and liveness procedures；Limitations / counterevidence：https://arxiv.org/html/2606.29601v1 — §7 Discussion: Conclusion and Perspectives。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MULTI-AGENT`。已在 [books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md) 顶层 Review notes 前反查机制正文；`SF-2026-ARXIV-2606-29601` 在正文出现 1 次、后置 trace 出现 2 次。
### [Energy-Efficient Multimodal Inference Serving with Tri-serve](https://arxiv.org/html/2606.29629v1)

**机制与贡献。** Multimodal model inference creates substantial energy demand with growing performance requirements. Within GPUs, power is autonomously managed by an on-board power management unit (PMU), which makes frequency boosting/throttling decisions.

**证据边界。** exact-v1 Method：https://arxiv.org/pdf/2606.29629v1 — §III Tri-serve software DVFS controller: stall-, arithmetic-intensity-, and thermal-aware policies；Evaluation：https://arxiv.org/pdf/2606.29629v1 — §II-C1 Frequency-locked Roofline Benchmarking; IV Evaluation；Limitations / counterevidence：https://arxiv.org/pdf/2606.29629v1 — §V Conclusion; evaluated Qwen-Omni/GPU-cluster boundary。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-SCHEDULING`。[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 顶层 Review notes 前的“SLO-aware Admission；Expert weights 与 KV 的联合 working set”已覆盖通用命题，不重复追加。
### [Demystifying the Design Space and Best Practices for Heterogeneous LLM Inference and Serving](https://arxiv.org/html/2606.29708v1)

**机制与贡献。** Heterogeneous prefill-decode (PD) inference is now in production: prefill on cost-efficient or supply-available accelerators, decode on bandwidth-strong ones, and KV state crossing mixed interconnects in mixed numerical formats. Each deployment makes these decisions on its own.

**证据边界。** exact-v1 Method：arXiv:2606.29708v1 — §Demystifying the Design Space and Best Practices for Heterogeneous LLM Inference and Serving; §2.1 Design Axes Behind the Boundary；Evaluation：arXiv:2606.29708v1 — §1 Introduction; §2 The PD Boundary; §2.1 Design Axes Behind the Boundary；Limitations / counterevidence：arXiv:2606.29708v1 — §2 The PD Boundary; §2.1 Design Axes Behind the Boundary; §2.2 Three Boundary Decisions。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-PD-DISAGGREGATION`。[books/part-05-inference-system/55-pd-disaggregation.md](../../../../books/part-05-inference-system/55-pd-disaggregation.md) 顶层 Review notes 前的“PD state ownership、异构 memory tier、transfer/SLO 与同步回退”已覆盖通用命题，不重复追加。
### [Diagnosing and Mitigating Context Rot in Long-horizon Search](https://arxiv.org/html/2606.29718v1)

**机制与贡献。** Extensive context has become the norm as Large Language Models (LLMs) are increasingly deployed in long-horizon search tasks. The concern that increasing context length degrades model capabilities, known as context rot, has become a widely recognized issue for these applications.

**证据边界。** exact-v1 Method：arXiv:2606.29718v1 — §Appendix D Effect of the Threshold on Other Context Management Methods；Evaluation：arXiv:2606.29718v1 — §3.3 Experimental Setup and Results; §Setup; §Main Results；Limitations / counterevidence：arXiv:2606.29718v1 — §5 Conclusion; §Appendix G Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-CONTEXT`。[books/part-07-agent/75-context.md](../../../../books/part-07-agent/75-context.md) 顶层 Review notes 前的“Context Compression 必须保留执行状态，而不只是语义”已覆盖通用命题，不重复追加。
### [MemLeak: Diagnosing Information Leaks in Multimodal Agent Memory](https://arxiv.org/html/2606.29788v1)

**机制与贡献。** When a multimodal AI agent is asked to forget a fact, current memory systems usually delete the text entry and report success. We find that the fact can remain recoverable from retained user images, including images tagged to entirely different facts, because VLMs use implicit visual cues at inference time.

**证据边界。** exact-v1 Method：arXiv:2606.29788v1 — §2.4 Per-Architecture IPG Analysis; §4.1 Systems Evaluated; §5 Design Implications；Evaluation：arXiv:2606.29788v1 — §2.4 Per-Architecture IPG Analysis; §3 The MemLeak Benchmark; §4 Experiments；Limitations / counterevidence：arXiv:2606.29788v1 — §6 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已覆盖通用命题，不重复追加。
### [AI Training Manager: Bounded Closed-Loop Control of Adaptive Training Recipes](https://arxiv.org/html/2606.29871v1)

**机制与贡献。** We present the AI Training Manager, a bounded LLM-based supervisory controller for adaptive machine learning training. Standard training pipelines often rely on fixed recipes or single-axis schedulers, which can struggle with mid-run failures such as severe overfitting, loss imbalance, exploration collapse, or unsafe exploration.

**证据边界。** exact-v1 Method：arXiv:2606.29871v1 — §AI Training Manager: Bounded Closed-Loop Control of Adaptive Training Recipes; §II-A Inner-Loop Heuristics and Adaptive Training Methods; §II-B Hyperparameter Optimization, AutoML, and Population-Based Training；Evaluation：arXiv:2606.29871v1 — §IV Experiments and Results; §IV-A TinyStories Language-Model Experiments; §IV-B Robotic-Arm Reinforcement-Learning Experiments；Limitations / counterevidence：arXiv:2606.29871v1 — §V Discussion and Limitations; §VI Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-TRAINING-OPERATOR`。[books/part-06-ai-infrastructure/60-training-operator.md](../../../../books/part-06-ai-infrastructure/60-training-operator.md) 顶层 Review notes 前的“Live Training Control 必须是可审计 Proposal，而不是直接改 Run”已覆盖通用命题，不重复追加。
### [MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation](https://arxiv.org/html/2606.29914v1)

**机制与贡献。** Agent memory systems are increasingly evaluated against RAG and full-context baselines, but reported gains often mix changes in the memory method with changes in the language model, embedding model, or retrieval pipeline, making it unclear what is actually being measured. We present MemDelta, a controlled evaluation protocol that varies one component at a time on LongMemEval-S (500 questions, 50+ sessions, three model families).

**证据边界。** exact-v1 Method：arXiv:2606.29914v1 — §Memory systems and benchmarks.; §B.3 When Might Architecture Matter?; §Memory systems.；Evaluation：arXiv:2606.29914v1 — §MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation; §Memory systems and benchmarks.; §Confounds in memory evaluation.；Limitations / counterevidence：arXiv:2606.29914v1 — §4.2 Model Behavior: Three Models, Three Conclusions; §Sonnet’s length-driven failure.; §5 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios?](https://arxiv.org/html/2606.29920v1)

**机制与贡献。** Rubric-based scoring has become a widely used paradigm in model evaluation, typically with LLM-as-a-Judge (LaaJ) for rubric scoring. However, the reliability of LaaJ for rubric scoring remains underexplored.

**证据边界。** exact-v1 Method：arXiv:2606.29920v1 — §1 Introduction; §2 Related Work; §Rubric-based evaluation；Evaluation：arXiv:2606.29920v1 — §Rubric-based evaluation; §3.3 Benchmark Statistics; §4 Experiments；Limitations / counterevidence：arXiv:2606.29920v1 — §5 Conclusion; §Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [SWE-Together: Evaluating Coding Agents in Interactive User Sessions](https://arxiv.org/html/2606.29957v1)

**机制与贡献。** Most coding-agent benchmarks are static: an agent receives a complete task description up front and is judged only by its final code. Real coding assistance is interactive, with users clarifying goals, adding constraints, and correcting mistakes over multiple turns.

**证据边界。** exact-v1 Method：arXiv:2606.29957v1 — §2.3 Evaluation Method；Evaluation：arXiv:2606.29957v1 — §2.3 Evaluation Method; §3 Experiments and Results; §3.1 Main Result；Limitations / counterevidence：arXiv:2606.29957v1 — §5 Limitations and Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [Beyond Uniform Experts: Cost-Aware Expert Execution for Efficient Multi-Device MoE Inference](https://arxiv.org/html/2606.29982v1)

**机制与贡献。** Mixture-of-Experts (MoE) architectures enable language models to achieve unprecedented scale via sparse activation. However, their inference performance is often limited by data movement bottlenecks.

**证据边界。** exact-v1 Method：arXiv:2606.29982v1 — §II-B Multi-Device Systems; §IV System Design；Evaluation：arXiv:2606.29982v1 — §III Analysis and Challenges; §III-A 1 Quantitative Analysis; §III-B 1 Quantitative Analysis；Limitations / counterevidence：arXiv:2606.29982v1 — §VII Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `MODEL-MOE`。[books/part-02-model/21-moe.md](../../../../books/part-02-model/21-moe.md) 顶层 Review notes 前的“Router 选择 Expert，Placement 决定这次选择能否低成本执行”已覆盖通用命题，不重复追加。
### [HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators](https://arxiv.org/html/2606.29986v1)

**机制与贡献。** LLM inference comprises a compute-bound prefill phase and a memory-bound decode phase, and recent systems disaggregate them onto separate hardware. Yet today's datacenter GPUs rely on costly HBM whose bandwidth sits almost entirely idle during prefill.

**证据边界。** exact-v1 Method：arXiv:2606.29986v1 — §3. Design；Evaluation：arXiv:2606.29986v1 — §4. Evaluation；Limitations / counterevidence：arXiv:2606.29986v1 — §6. Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-PD-DISAGGREGATION`。[books/part-05-inference-system/55-pd-disaggregation.md](../../../../books/part-05-inference-system/55-pd-disaggregation.md) 顶层 Review notes 前的“PD state ownership、异构 memory tier、transfer/SLO 与同步回退”已覆盖通用命题，不重复追加。
### [LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via State Proprioception](https://arxiv.org/html/2606.30005v1)

**机制与贡献。** Long-horizon tool agents are bottlenecked by how their context grows toward the limits of the context window. Recent systems make context management agent- or system-controlled, but they either learn compression policies that discard evidence or manage context in a layer the agent never sees.

**证据边界。** exact-v1 Method：arXiv:2606.30005v1 — §Methodology; §Appendix C Method Capability Comparison；Evaluation：arXiv:2606.30005v1 — §Problem Setup; §Experiments; §Experiment Setup；Limitations / counterevidence：arXiv:2606.30005v1 — §Limitations; §Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-CONTEXT`。[books/part-07-agent/75-context.md](../../../../books/part-07-agent/75-context.md) 顶层 Review notes 前的“Context Compression 必须保留执行状态，而不只是语义”已覆盖通用命题，不重复追加。
### [On the Internet, Nobody Knows You're an LLM Bot: Unmasking Web Agents with Multi-Layer Fingerprinting](https://arxiv.org/html/2606.30119v1)

**机制与贡献。** Since 2023, a new class of bots has emerged: Web Agents. They can automate complex tasks on the Web, going beyond traditional browser automation tools such as Selenium, Puppeteer, or Playwright.

**证据边界。** exact-v1 Method：arXiv:2606.30119v1 — §3. Methodology; §3.1.3. Honeysite Design；Evaluation：arXiv:2606.30119v1 — §3.2. Experimental Protocol; §7.1. Multi-Layer Classification Setup; §7.2. Multi-Layer Classification Evaluation；Limitations / counterevidence：arXiv:2606.30119v1 — §8. Limitations and Discussion; §10. Conclusion & Future Work。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [When Is a Draft Accepted? A Theory of Acceptance in Speculative Decoding](https://arxiv.org/html/2606.30265v1)

**机制与贡献。** Speculative decoding accelerates language model inference by using a fast drafter to propose candidate tokens that are then verified by a larger target model. Existing theory largely studies the stochastic, distribution-preserving setting, where the goal is to exactly sample from the target distribution.

**证据边界。** exact-v1 Method：arXiv:2606.30265v1 — §1 Introduction; §2 Related Works; §Architectural variants.；Evaluation：arXiv:2606.30265v1 — §Theoretical analysis.; §4.1 Setup; §5.1 Setup and Notation；Limitations / counterevidence：arXiv:2606.30265v1 — §7 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-SPECULATIVE-DECODING`。[books/part-05-inference-system/48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md) 顶层 Review notes 前的“Acceptance 不是独立常数，在线决策必须结算系统状态”已覆盖通用命题，不重复追加。
### [Whose Side Is Your Agent On? Multi-Party Principal Loyalty in LLM Agents](https://arxiv.org/html/2606.30383v1)

**机制与贡献。** A rapidly growing class of LLM agents is multi-party: the agent acts for a principal (who briefs it, sends follow-ups, and receives results) while also conversing in a separate channel with a counterparty whose interests may diverge (negotiating with a vendor, screening inbound requests, or mediating between employees). Here "help whoever you are talking to" is the wrong objective.

**证据边界。** exact-v1 Method：arXiv:2606.30383v1 — §Methods.；Evaluation：arXiv:2606.30383v1 — §Setup.; §Agent benchmarks are two-party.; §Privacy benchmarks isolate information flow, not adversarial pressure.；Limitations / counterevidence：arXiv:2606.30383v1 — §Why one failure axis is not enough.; §Failures compound: a worked trace.; §9 Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [Predict, Reuse, and Repair: Accelerating Dynamic Sparse Attention for Long-Context LLM Decoding](https://arxiv.org/html/2606.30389v1)

**机制与贡献。** Dynamic sparse attention (DSA) accelerates long-context LLM decoding by attending to only the top-K KV blocks relevant to each query, but it introduces a serialized selection-to-attention dependency that emerges as a new latency bottleneck. We present PRR, a speculate-reuse-repair runtime that exploits temporal locality in DSA selections to predict likely blocks, speculate the attention over them while selection is in flight, and incrementally repair missed blocks once the true selected set is known.

**证据边界。** exact-v1 Method：arXiv:2606.30389v1 — §3 The Design Space; §4 Design；Evaluation：arXiv:2606.30389v1 — §5 Evaluation; §5.1 Experiment Setups; §5.2 Accelerate Evaluation；Limitations / counterevidence：arXiv:2606.30389v1 — §7 Conclusion; §Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-DECODE`。[books/part-05-inference-system/44-decode.md](../../../../books/part-05-inference-system/44-decode.md) 顶层 Review notes 前的“Decode 的结束条件；Decode-only Compute Branch 仍必须尊重单一 KV Owner”已覆盖通用命题，不重复追加。
### [Energy-Aware Scheduling for Serverless LLM Serving on Shared GPUs](https://arxiv.org/html/2606.30391v1)

**机制与贡献。** As LLM inference becomes a major cloud workload, its growing energy footprint makes cluster-wide energy optimization increasingly important. Serverless LLM serving helps platforms absorb traffic volatility by elastically sharing GPU resources across models, but this sharing also makes energy optimization difficult.

**证据边界。** exact-v1 Method：arXiv:2606.30391v1 — §3. Festina Design; §3.1. System Overview; §Appendix I Prior Energy-Efficient LLM Serving Systems；Evaluation：arXiv:2606.30391v1 — §4. Evaluation; §4.1. Experimental Setup; §4.4. Micro-benchmarks；Limitations / counterevidence：arXiv:2606.30391v1 — §6. Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-SCHEDULING`。[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 顶层 Review notes 前的“SLO-aware Admission；Expert weights 与 KV 的联合 working set”已覆盖通用命题，不重复追加。
### [Internal-State Probes Read the Situation, Not the Action: Three Negative Results for Pre-Action Misalignment Monitoring](https://arxiv.org/html/2606.30449v1)

**机制与贡献。** Probes on model internals could help monitor agentic systems if they identify harmful text or tool actions before those actions are generated. We ask when an internal readout supports this stronger pre-action claim, rather than merely describing the prompt, construction contrast, or current trajectory.

**证据边界。** exact-v1 Method：arXiv:2606.30449v1 — §3 Methods; §Appendix A Methodology details; §A.1 Methodology divergences from the closest prior work；Evaluation：arXiv:2606.30449v1 — §In-context misalignment evaluations.; §4 Experiments; §5 Results；Limitations / counterevidence：arXiv:2606.30449v1 — §6 Discussion; §7 Limitations; §8 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-MONITORING`。[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md) 顶层 Review notes 前的“calibration-bound sensor、direct profile fallback 与 monitor 不拥有 truth/commit”已覆盖通用命题，不重复追加。
### [Entity Binding Failures in Tool-Augmented Agents](https://arxiv.org/html/2606.30531v1)

**机制与贡献。** Tool-augmented language-model agents are often evaluated by whether they select the correct tool, produce valid API arguments, and complete the requested task. However, an agent may choose the right tool and still act on the wrong external entity.

**证据边界。** exact-v1 Method：arXiv:2606.30531v1 — §III Problem Formulation; §IV Method; §V-E Methods Compared；Evaluation：arXiv:2606.30531v1 — §V Experimental Setup; §V-G Evaluation Protocol; §VI Results；Limitations / counterevidence：arXiv:2606.30531v1 — §Entity Binding Failures in Tool-Augmented Agents; §VI-C Failure Modes by Ambiguity Type; §VII Discussion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-TOOL-CALLING`。[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md) 顶层 Review notes 前的“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract”已覆盖通用命题，不重复追加。
### [TraceLab: Characterizing Coding Agent Workloads for LLM Serving](https://arxiv.org/html/2606.30560v1)

**机制与贡献。** Coding agents are rapidly becoming a major application of agentic LLMs, but serving them efficiently remains challenging. Progress on this challenge requires understanding real workload patterns, yet the data needed for such analysis is largely absent.

**证据边界。** exact-v1 Method：arXiv:2606.30560v1 — §4.5 Takeaways and Systems Opportunities; §5.5 Takeaways and Systems Opportunities; §6.4 Takeaways and System Opportunities；Evaluation：arXiv:2606.30560v1 — §2.2 Existing Datasets and Benchmarks; §8.3 Coding-agent benchmarks and tool-use evaluation；Limitations / counterevidence：arXiv:2606.30560v1 — §9 Limitations and Future Work; §10 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-SCHEDULING`。[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 顶层 Review notes 前的“SLO-aware Admission；Expert weights 与 KV 的联合 working set”已覆盖通用命题，不重复追加。
### [Forensic Trajectory Signatures for Agent Memory Poisoning Detection](https://arxiv.org/html/2606.30566v1)

**机制与贡献。** We discover a behavioral invariant in LLM agents under persistent memory poisoning and characterize its deployment boundary. In architectures where retrieval is routed through observable memory-tool invocations, successful attacks require calling memory_recall_fact before email_send_email, a transition mechanistically forced by the attack's information-retrieval dependency.

**证据边界。** exact-v1 Method：arXiv:2606.30566v1 — §2 Methodology; §Training data scope.; §Behavioral detection in agentic systems.；Evaluation：arXiv:2606.30566v1 — §2.4 Classifiers and Evaluation; §3 Results; §Expanded frontier evaluation.；Limitations / counterevidence：arXiv:2606.30566v1 — §2.1 Threat Model; §3.8 Evasion Boundary; §4 Discussion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已覆盖通用命题，不重复追加。
### [MESA: Prioritizing Vulnerable Communication Channels for Securing Multi-Agent Systems](https://arxiv.org/html/2606.30602v1)

**机制与贡献。** Multi-agent systems (MAS) are increasingly used to automate complex, distributed workflows. However, their inter-agent communication channels introduce new attack surfaces that remain poorly understood and are difficult to defend against.

**证据边界。** exact-v1 Method：arXiv:2606.30602v1 — §MESA: Prioritizing Vulnerable Communication Channels for Securing Multi-Agent Systems; §II-A MAS Design & Topologies; §III-C Problem Formulation；Evaluation：arXiv:2606.30602v1 — §V Experimental Setup; §VI Evaluation; §VI-B RQ2: Application Analysis of Mesa Efficacy；Limitations / counterevidence：arXiv:2606.30602v1 — §III-B Threat Model; §VI-E 1 Exposure-aware threat surface; §VIII Discussion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MULTI-AGENT`。[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md) 顶层 Review notes 前的“Message 不是 State；Verification Delay 也是拓扑控制状态”已覆盖通用命题，不重复追加。
### [One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining](https://arxiv.org/html/2606.30634v1)

**机制与贡献。** Modern large-scale LLM pretraining benefits from utilizing Pipeline Parallelism; however, synchronous implementations leave GPUs idle during pipeline bubbles, wasting computational resources. Asynchronous Pipeline Parallelism eliminates these bubbles, maximizing throughput at the cost of gradient staleness.

**证据边界。** exact-v1 Method：arXiv:2606.30634v1 — §One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining; §E.1 Hyperparameters and Training Details; §E.2 Model architectures；Evaluation：arXiv:2606.30634v1 — §2.2 Hyperparameter Sensitivity and Benchmarking; §4 Theoretical analysis; §5 Large Scale Experiments；Limitations / counterevidence：arXiv:2606.30634v1 — §8 Discussion and Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `TRAIN-PIPELINE-PARALLEL`。[books/part-04-training-system/38-pipeline-parallel.md](../../../../books/part-04-training-system/38-pipeline-parallel.md) 顶层 Review notes 前的“异步 Pipeline：去掉 Bubble 会把成本移到参数版本”已覆盖通用命题，不重复追加。

## 5. 缺口与下一步

无

闭合账目：raw=1132；旧候选 provenance=231；当前候选=55；旧候选降级=177；另从更广题摘审计池纠正准入 MOPD 1 项。FP 全量重裁与 24 项 FN 分层抽检均未发现其他待处理问题；全部 Integrate 已反查当前 owner 的顶层 Review notes 前正文；全部 Existing Coverage 已绑定正文命题锚点。

## 6. 复核

复核者：V3 恢复语义复核（独立于旧 V2.1 报告作者；2026-09-10）

结论：通过

当前合同来源再认证由作者侧执行，`/root` 以非作者身份独立复核准入与 Books 边界；其提出的 MOPD 候选重开意见已经落实。

独立复核覆盖 canonical owner 日期、撤回排除、旧候选 FP 全量重裁、24 项 FN 分层抽样、closure taxonomy、exact-v1 定位、每个 Integrate 的顶层 Review notes 前正文，以及每个 Existing Coverage 的正文命题锚点。审计明确区分“题摘准入”与“Books trace”，并排除 AI for Science、纯领域 benchmark、局部模型/表示改进和仅凭 ROADMAP 映射的材料。机器校验只证明结构一致性。
