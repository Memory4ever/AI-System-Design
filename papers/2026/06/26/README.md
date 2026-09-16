# Daily Research — 2026-06-26

**规范：** V3
**窗口：** 2026-06-25T09:00:00+08:00 ～ 2026-06-26T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T09:36:20+08:00

## 1. 结论

本窗恢复 566 个 canonical arXiv identity，逐项以完整题摘按当前“大模型与大模型基础设施”贡献门槛重审，冻结 36 个候选。旧 V2.1 的 85 个候选只作 provenance，49 项因垂直任务、领域 benchmark、局部表示/方法或仅能映射 ROADMAP 而在候选前关闭；没有以 Books trace 反向证明准入。

本轮候选前关闭（不计入 Candidate Denominator）：

- `2606.27005` / `SF-2026-ARXIV-2606-27005` — 通用异构 AI model population 的 fairness/interpretability composite-utility simulation；没有大模型特有 workload/state 或真实基础设施 contract

候选均复用可核实的 exact-v1 Method / Evaluation / Limitations 定位。Books 结果为 1 项整合、35 项已有覆盖；本次同步没有修改 Books、LEARNING_STATE 或跨日索引。

2026-09-14 按当前来源清单重放 13 个机构每日源并复用仍匹配的 arXiv / exact-v1 / Evidence / Books 证据。机构源补查确认 Qwen weekly 为旧变更汇总、混元 06-25 后端时间为站点迁移，均不是新研究事件；冻结分母仍为 36。详细过程见 [当前合同再认证](../_sources/daily-20260626/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)。/root 非作者独立复核已通过。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [当前合同再认证](../_sources/daily-20260626/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列与窗口定点检索；本窗无范围内新增 | 已检查 | 无 |
| SRC-ANTHROPIC | [当前合同再认证](../_sources/daily-20260626/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-GOOGLE-AI | [当前合同再认证](../_sources/daily-20260626/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：DeepMind / Google Research 官方索引；本窗无范围内新增 | 已检查 | 无 |
| SRC-META-AI | [当前合同再认证](../_sources/daily-20260626/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-QWEN | [当前合同再认证](../_sources/daily-20260626/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：06-25 weekly post 是汇总；可定位变更首发/合并于 06-18，本窗无新 family | 已检查 | 无 |
| SRC-DEEPSEEK | [当前合同再认证](../_sources/daily-20260626/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research / 发布索引；本窗无新 family / 重要 revision | 已检查 | 无 |
| SRC-MOONSHOT | [当前合同再认证](../_sources/daily-20260626/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：Kimi Blog 与官方仓库发布时序；本窗无范围内新增 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | [当前合同再认证](../_sources/daily-20260626/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：publicList 8/8 条；06-25 后端时间对应展示日期 04-23 的站点迁移，不是新事件 | 已检查 | 无 |
| SRC-ZAI | [当前合同再认证](../_sources/daily-20260626/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [当前合同再认证](../_sources/daily-20260626/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research、论文目录与发布页；本窗无范围内新增 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [当前合同再认证](../_sources/daily-20260626/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方技术博客与仓库发布时序；本窗无范围内新增 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [当前合同再认证](../_sources/daily-20260626/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Paper / Blog 与仓库；本窗无范围内新增 | 已检查 | 无 |
| SRC-MINIMAX | [当前合同再认证](../_sources/daily-20260626/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：中英文博客与 Agent Tech Blog；相邻条目为 06-09/06-01，本窗无新增 | 已检查 | 无 |
| SRC-ARXIV | [canonical raw inventory](../_sources/daily-20260626/canonical-raw-identity-inventory-v2.1.json.gz)；566 个 owner identity 完成题摘筛选；[V3 audit](../_sources/daily-20260626/v3-admission-audit-20260910.json) | 已检查 | 无 |

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability。本轮独立复核已按当前候选实际新增的命题逐项重评，不沿用旧分数，也不因既有证据已经深入审阅而倒推高分：单一 owner 内的局部机制按单组件 reach 计，只有原文实际跨越系统边界才计跨边界；实验性 operating point 默认是可复用约束而非长期认知基础。既有深审证据继续保留，评分只决定最低投入，不反向删除已读证据。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kiko: Programming Agents to Enact Interaction Protocols](https://arxiv.org/html/2606.26156v1) | 2026-06-26T08:00:00+08:00 | AGENT-MULTI-AGENT；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[目标章](../../../../books/part-07-agent/82-multi-agent.md)“Message 不是 State；Verification Delay 也是拓扑控制状态” |
| [Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations](https://arxiv.org/html/2606.26185v1) | 2026-06-26T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems](https://arxiv.org/html/2606.26298v1) | 2026-06-26T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [The Verification Horizon: No Silver Bullet for Coding Agent Rewards](https://arxiv.org/html/2606.26300v1) | 2026-06-26T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Axon: A Synthesizing Superoptimizer for Tensor Programs](https://arxiv.org/html/2606.26344v1) | 2026-06-26T08:00:00+08:00 | INFER-TENSORRT-LLM；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[目标章](../../../../books/part-05-inference-system/49-tensorrt-llm.md)“Generated Kernel 必须先进入 Typed Schedule IR” |
| [Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems](https://arxiv.org/html/2606.26356v1) | 2026-06-26T08:00:00+08:00 | AGENT-PROMPT；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-PROMPT，[目标章](../../../../books/part-07-agent/74-prompt.md)“条件化机制分支与共存边界” |
| [Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats](https://arxiv.org/html/2606.26377v1) | 2026-06-26T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [SOLAR: AI-Powered Speed-of-Light Performance Analysis](https://arxiv.org/html/2606.26383v1) | 2026-06-26T08:00:00+08:00 | PLATFORM-MONITORING；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-MONITORING，[目标章](../../../../books/part-06-ai-infrastructure/67-monitoring.md)“条件化机制分支与共存边界”下“性能监控可用 speed-of-light model 将硬件峰值、数据移动和 workload 参数分解成可校准上界”段落 |
| [DualEval: Joint Model-Item Calibration for Unified LLM Evaluation](https://arxiv.org/html/2606.26429v1) | 2026-06-26T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [ProvenAI: Provenance-Native Traces of Evidence in Generated Answers](https://arxiv.org/html/2606.26449v1) | 2026-06-26T08:00:00+08:00 | PLATFORM-TRACE；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-TRACE，[目标章](../../../../books/part-06-ai-infrastructure/69-trace.md)“provenance/evidence 不等于 truth” |
| [Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization](https://arxiv.org/html/2606.26453v1) | 2026-06-26T08:00:00+08:00 | INFER-TENSORRT-LLM；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[目标章](../../../../books/part-05-inference-system/49-tensorrt-llm.md)“Generated Kernel 必须先进入 Typed Schedule IR” |
| [Epiphany-Aware KV Cache Eviction Without the Attention Matrix](https://arxiv.org/html/2606.26472v1) | 2026-06-26T08:00:00+08:00 | INFER-KV-CACHE；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[目标章](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)“从不可逆 Eviction 到可恢复的分层 Recall” |
| [Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents](https://arxiv.org/html/2606.26479v1) | 2026-06-26T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge](https://arxiv.org/html/2606.26511v1) | 2026-06-26T08:00:00+08:00 | AGENT-MEMORY；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills](https://arxiv.org/html/2606.26524v1) | 2026-06-26T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Moebius: Serving Mixture-of-Expert Models with Seamless Runtime Parallelism Switch](https://arxiv.org/html/2606.26607v1) | 2026-06-26T08:00:00+08:00 | INFER-SCHEDULING；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md)“SLO-aware Admission；Expert weights 与 KV 的联合 working set” |
| [Autoformalization of Agent Instructions into Policy-as-Code](https://arxiv.org/html/2606.26649v1) | 2026-06-26T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [PersistentKV: Page-Aware Decode Scheduling for Long-Context LLM Serving on Commodity GPUs](https://arxiv.org/html/2606.26666v1) | 2026-06-26T08:00:00+08:00 | INFER-KV-CACHE；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[目标章](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)“从不可逆 Eviction 到可恢复的分层 Recall” |
| [SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills](https://arxiv.org/html/2606.26669v1) | 2026-06-26T08:00:00+08:00 | AGENT-TOOL-CALLING；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[目标章](../../../../books/part-07-agent/78-tool-calling.md)“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract” |
| [Knowledge-Based Pull Requests: A Trusted Workflow for Agent-Mediated Knowledge Collaboration](https://arxiv.org/html/2606.26721v1) | 2026-06-26T08:00:00+08:00 | AGENT-WORKFLOW；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[目标章](../../../../books/part-07-agent/81-workflow.md)“Template、Realized Graph 与 Trace 不是同一个对象” |
| [HyperDFlash: Hyper-Connection-Aligned Block Speculative Decoding with Gated Residual Reduction](https://arxiv.org/html/2606.26744v1) | 2026-06-26T08:00:00+08:00 | INFER-SPECULATIVE-DECODING；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[目标章](../../../../books/part-05-inference-system/48-speculative-decoding.md)“Acceptance 不是独立常数，在线决策必须结算系统状态” |
| [The Capability Frontier: Benchmarks Miss 82% of Model Performance](https://arxiv.org/html/2606.26836v1) | 2026-06-26T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Information-Aware KV Cache Compression for Long Reasoning](https://arxiv.org/html/2606.26875v1) | 2026-06-26T08:00:00+08:00 | INFER-KV-CACHE；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[目标章](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)“从不可逆 Eviction 到可恢复的分层 Recall” |
| [Diagnosing Task Insensitivity in Language Agents](https://arxiv.org/html/2606.26918v1) | 2026-06-26T08:00:00+08:00 | AGENT-PLANNING；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-PLANNING，[目标章](../../../../books/part-07-agent/79-planning.md)“学习到的 Transition 只能验证候选，不能提交环境事实” |
| [A Deterministic Control Plane for LLM Coding Agents](https://arxiv.org/html/2606.26924v1) | 2026-06-26T08:00:00+08:00 | AGENT-PLATFORM；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[目标章](../../../../books/part-07-agent/84-agent-platform.md)“Agent Runtime State Machine；Harness、Protocol 与 Credit 都是 Platform-owned Artifact” |
| [To Run or Not to Run: Analyzing the Cost-Effectiveness of Code Execution in LLM-Based Program Repair](https://arxiv.org/html/2606.26978v1) | 2026-06-26T08:00:00+08:00 | AGENT-TOOL-CALLING；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[目标章](../../../../books/part-07-agent/78-tool-calling.md)“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract” |
| [How Much Static Structure Do Code Agents Need? A Study of Deterministic Anchoring](https://arxiv.org/html/2606.26979v1) | 2026-06-26T08:00:00+08:00 | AGENT-CONTEXT；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-CONTEXT，[目标章](../../../../books/part-07-agent/75-context.md)“Context Compression 必须保留执行状态，而不只是语义” |
| [Decision-Aligned Evaluation of Uncertainty Quantification](https://arxiv.org/html/2606.26990v1) | 2026-06-26T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [RolloutPipe: Overlapping Pipelined Rollout and Training in Disaggregated On-Policy LLM Reinforcement Learning](https://arxiv.org/html/2606.26997v1) | 2026-06-26T08:00:00+08:00 | TRAIN-DISTRIBUTED-TRAINING；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[目标章](../../../../books/part-04-training-system/36-distributed-training.md)“异步训练必须分开 Throughput、Freshness 与 Objective Ownership” |
| [Semantic Early-Stopping for Iterative LLM Agent Loops](https://arxiv.org/html/2606.27009v1) | 2026-06-26T08:00:00+08:00 | AGENT-WORKFLOW；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[目标章](../../../../books/part-07-agent/81-workflow.md)“Template、Realized Graph 与 Trace 不是同一个对象” |
| [ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP](https://arxiv.org/html/2606.27027v1) | 2026-06-26T08:00:00+08:00 | AGENT-MCP；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MCP，[目标章](../../../../books/part-07-agent/83-mcp.md)“MCP 不等于 Tool Authorization；从单工具扫描到组合级 Admission” |
| [The Spec Growth Engine: Spec-Anchored, Code-Coupled, Drift-Enforced Architecture for AI-Assisted Software Development](https://arxiv.org/html/2606.27045v1) | 2026-06-26T08:00:00+08:00 | AGENT-CONTEXT；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-CONTEXT，[目标章](../../../../books/part-07-agent/75-context.md)“Context Compression 必须保留执行状态，而不只是语义” |
| [DMuon: Efficient Distributed Muon Training with Near-Adam Overhead](https://arxiv.org/html/2606.27153v1) | 2026-06-26T08:00:00+08:00 | TRAIN-DISTRIBUTED-TRAINING；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[目标章](../../../../books/part-04-training-system/36-distributed-training.md)“异步训练必须分开 Throughput、Freshness 与 Objective Ownership” |
| [OpenRCA 2.0: From Outcome Labels to Causal Process Supervision](https://arxiv.org/html/2606.27154v1) | 2026-06-26T08:00:00+08:00 | PLATFORM-TRACE；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-TRACE，[目标章](../../../../books/part-06-ai-infrastructure/69-trace.md)“provenance/evidence 不等于 truth” |
| [Ask, Don't Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement](https://arxiv.org/html/2606.27226v1) | 2026-06-26T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models](https://arxiv.org/html/2606.27288v1) | 2026-06-26T08:00:00+08:00 | AGENT-MULTI-AGENT；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[目标章](../../../../books/part-07-agent/82-multi-agent.md)“Message 不是 State；Verification Delay 也是拓扑控制状态” |

## 4. 证据与知识整合

### [Kiko: Programming Agents to Enact Interaction Protocols](https://arxiv.org/html/2606.26156v1)

**机制与贡献。** Realizing a multiagent system involves implementing member agents who interact based on a protocol while making decisions in a decentralized manner. Current programming models for agents offer poor abstractions for decision making and fail to adequately bridge an agent's internal decision logic with its public decisions.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26156v1 — §2 Information Protocols; 3 Kiko Programming Model；Evaluation：https://arxiv.org/html/2606.26156v1 — §4 Operational Semantics; protocol-compliance proof；Limitations / counterevidence：https://arxiv.org/html/2606.26156v1 — §5 Discussion and conference-era implementation scope。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MULTI-AGENT`。[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md) 顶层 Review notes 前的“Message 不是 State；Verification Delay 也是拓扑控制状态”已覆盖通用命题，不重复追加。
### [Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations](https://arxiv.org/html/2606.26185v1)

**机制与贡献。** LLM-as-judge ("grader") components are now standard in evaluation harnesses, including safety evaluations where a pass/fail verdict may gate downstream deployment decisions. A widespread assumption is that setting the grader's sampling temperature to 0 makes grading deterministic.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26185v1 — §Temperature-control and reproducibility protocol for LLM-as-judge safety evaluation；Evaluation：https://arxiv.org/html/2606.26185v1 — §Cross-temperature, repeat-run and judge-agreement evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.26185v1 — §Temperature control is necessary but not sufficient; prompt/model/vendor drift remains。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems](https://arxiv.org/html/2606.26298v1)

**机制与贡献。** Autonomous AI agents may begin to perform consequential, irreversible actions such as clinical prescribing and production software deployment. This paper observes that human institutions have governed powerful autonomous actors not by monitoring their reasoning but by requiring independently attested evidence at the point of consequential action.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26298v1 — §Governing Actions, Not Agents; Institutional Attestation model；Evaluation：https://arxiv.org/html/2606.26298v1 — §Action-level attestation scenarios and governance analysis；Limitations / counterevidence：https://arxiv.org/html/2606.26298v1 — §Institutional model is a governance proposal, not a deployed enforcement benchmark。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [The Verification Horizon: No Silver Bullet for Coding Agent Rewards](https://arxiv.org/html/2606.26300v1)

**机制与贡献。** A classical intuition holds that verifying a solution is easier than producing one. For today's coding agents, this intuition is being inverted: as foundation models develop stronger reasoning capabilities and engineering harnesses grow more sophisticated, generating complex candidate solutions is no longer difficult -- reliably verifying them has become the harder problem.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26300v1 — §Verification Horizon formulation for coding-agent rewards；Evaluation：https://arxiv.org/html/2606.26300v1 — §Reward-verification experiments across coding horizons；Limitations / counterevidence：https://arxiv.org/html/2606.26300v1 — §No universal reward verifier; longer horizons and hidden environment state remain。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [Axon: A Synthesizing Superoptimizer for Tensor Programs](https://arxiv.org/html/2606.26344v1)

**机制与贡献。** Writing high performance kernels for AI accelerators requires deep expertise in tiling, instruction selection, data layout, and operator fusion placing a significant burden on programmers. In this paper, we focus on tile based AI accelerator programs and present Axon, a synthesizing superoptimizer for tensor programs: it uses program synthesis to automatically generate target instructions from semantics specifications, and explores semantically equivalent program variants to select the best performing kernel empirically.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26344v1 — §Axon synthesizing superoptimizer; tensor-program search and verification；Evaluation：https://arxiv.org/html/2606.26344v1 — §Kernel synthesis evaluation and generated-program performance；Limitations / counterevidence：https://arxiv.org/html/2606.26344v1 — §Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-TENSORRT-LLM`。[books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 顶层 Review notes 前的“Generated Kernel 必须先进入 Typed Schedule IR”已覆盖通用命题，不重复追加。
### [Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems](https://arxiv.org/html/2606.26356v1)

**机制与贡献。** Practitioners of prompt-composed agentic systems report a recurring failure mode: editing one prompt module silently shifts the behavior of others despite no shared variable or executable dependency. We formalize this as compositional behavioral leakage (CBL): interference between modules sharing a context window.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26356v1 — §Instruction Bleed formulation; prompt-composed module interference；Evaluation：https://arxiv.org/html/2606.26356v1 — §Cross-module interference experiments and mitigations；Limitations / counterevidence：https://arxiv.org/html/2606.26356v1 — §Prompt/module families tested do not establish universal isolation or adversarial robustness。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-PROMPT`。[books/part-07-agent/74-prompt.md](../../../../books/part-07-agent/74-prompt.md) 顶层 Review notes 前的“条件化机制分支与共存边界”已覆盖通用命题，不重复追加。
### [Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats](https://arxiv.org/html/2606.26377v1)

**机制与贡献。** Large language models (LLMs) are increasingly deployed in interactive applications, yet they remain vulnerable to adversarial interactions that induce harmful, deceptive, or policy-violating outputs. Existing defenses typically analyze either user prompts or generated outputs, but not both.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26377v1 — §Unified intent-and-harm verification defense；Evaluation：https://arxiv.org/html/2606.26377v1 — §Threat-generation and defense evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.26377v1 — §Evaluated threat families and judges only; intent inference is not proof of harmless execution。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [SOLAR: AI-Powered Speed-of-Light Performance Analysis](https://arxiv.org/html/2606.26383v1)

**机制与贡献。** How fast could a deep-learning model run on target hardware, and how far is today's implementation from that limit? These questions are central to software, hardware, and algorithm optimizations.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26383v1 — §SOLAR speed-of-light performance model; bottleneck decomposition and bound calculation；Evaluation：https://arxiv.org/html/2606.26383v1 — §Predicted-vs-observed latency and throughput analysis；Limitations / counterevidence：https://arxiv.org/html/2606.26383v1 — §Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-MONITORING`。已在 [books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md) 顶层 Review notes 前反查机制正文；`SF-2026-ARXIV-2606-26383` 在正文出现 2 次、后置 trace 出现 1 次。
### [DualEval: Joint Model-Item Calibration for Unified LLM Evaluation](https://arxiv.org/html/2606.26429v1)

**机制与贡献。** Current LLM evaluation relies on two complementary but often disconnected signals: static benchmarks with objective correctness labels and arena-style preference data that better reflect open-ended user interactions. We introduce DualEval, a latent model-item calibration framework that represents models and evaluation items in a shared space, jointly estimating model ability together with item difficulty and sharpness.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26429v1 — §DualEval joint model-item calibration；Evaluation：https://arxiv.org/html/2606.26429v1 — §Unified LLM evaluation experiments and calibration analysis；Limitations / counterevidence：https://arxiv.org/html/2606.26429v1 — §Joint calibration assumes the evaluated item/model pool; new distributions require refitting。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [ProvenAI: Provenance-Native Traces of Evidence in Generated Answers](https://arxiv.org/html/2606.26449v1)

**机制与贡献。** Retrieval-augmented systems routinely present citations alongside generated answers, yet a citation does not confirm that the corresponding source meaningfully shaped the output. This paper introduces ProvenAI, a framework that decomposes transparency in multi-hop question answering into three independently measurable layers: answer correctness, citation fidelity against benchmark supporting evidence, and per-document influence under leave-one-resource-out intervention.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26449v1 — §ProvenAI provenance-native trace schema and evidence links；Evaluation：https://arxiv.org/html/2606.26449v1 — §Generated-answer trace/evidence evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.26449v1 — §Trace completeness depends on instrumented producers; provenance does not imply source truth。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-TRACE`。[books/part-06-ai-infrastructure/69-trace.md](../../../../books/part-06-ai-infrastructure/69-trace.md) 顶层 Review notes 前的“provenance/evidence 不等于 truth”已覆盖通用命题，不重复追加。
### [Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization](https://arxiv.org/html/2606.26453v1)

**机制与贡献。** We present KernelPro, a closed-loop multi-agent system that automatically generates, profiles, and iteratively optimizes GPU kernel code by integrating large language model (LLM) code generation with hardware profiler feedback and pluggable bottleneck detection tools. KernelPro introduces four contributions: (1) a semantic feedback operator that encodes expert heuristics as pluggable micro-profiling tools, transforming raw hardware metrics into actionable natural language guidance; (2) a two-stage tool invocation architecture where roofline-based bottleneck classification filters which specialized analysis tools execute, combining kernel-level (ncu), instruction-level (SASS), and system-level (nsys) profiling; (3) a domain-adapted MCTS with progressive widening, asymmetric branching, log-reward calibration, dead-end pruning, and search memory for cross-iteration learning; and (4) direct CuTe source-level code generation via autonomous code search over the CUTLASS/CuTe codebase.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26453v1 — §Micro-profiling tools as expert surrogates for LLM CUDA optimization；Evaluation：https://arxiv.org/html/2606.26453v1 — §Generated-kernel correctness, profiling and speed evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.26453v1 — §Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-TENSORRT-LLM`。[books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 顶层 Review notes 前的“Generated Kernel 必须先进入 Typed Schedule IR”已覆盖通用命题，不重复追加。
### [Epiphany-Aware KV Cache Eviction Without the Attention Matrix](https://arxiv.org/html/2606.26472v1)

**机制与贡献。** As reasoning models emit chains of thought tens of thousands of tokens long, KV cache increasingly becomes a deployment bottleneck. Existing cache eviction methods rank tokens by attention weight, which is a noisy importance proxy in long reasoning traces, and prohibits the use of fused kernels in production inference by forcing the model to materialize the attention matrix.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26472v1 — §Epiphany score from forward-pass representation change; attention-matrix-free eviction；Evaluation：https://arxiv.org/html/2606.26472v1 — §Long-reasoning cache/quality evaluation and 16x feasible-context claim；Limitations / counterevidence：https://arxiv.org/html/2606.26472v1 — §Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-KV-CACHE`。[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 顶层 Review notes 前的“从不可逆 Eviction 到可恢复的分层 Recall”已覆盖通用命题，不重复追加。
### [Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents](https://arxiv.org/html/2606.26479v1)

**机制与贡献。** Recent work (2024 to 2026) has converged on a strategy for defending tool-using LLM agents against indirect prompt injection: rather than training the model to refuse malicious instructions, enforce security outside the model with a deterministic policy that mediates the agent's actions. Systems such as CaMeL, FIDES, Progent, RTBAS, and FORGE realize this with capabilities, information-flow labels, and reference monitors, and several report near-elimination of attacks on the AgentDojo benchmark.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.26479v1 — §Out-of-band prompt-injection defenses organized as reference monitors and integrity policies；Evaluation：https://arxiv.org/html/2606.26479v1 — §Adaptive evaluation methodology against policy-aware attackers；Limitations / counterevidence：https://arxiv.org/html/2606.26479v1 — §Position/evaluation paper; static AgentDojo results do not establish adaptive robustness。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge](https://arxiv.org/html/2606.26511v1)

**机制与贡献。** Retrieval-augmented generation (RAG) gives agents access to accumulated knowledge, but has no model of time. When a fact changes (e.g., a function is renamed or API restructured), RAG retrieves both the stale and current value with near-identical embedding similarity.

**证据边界。** exact-v1 Method：arXiv:2606.26511v1 — §4 The MemStrata Architecture; §4.3 The “retain, then supersede” design；Evaluation：arXiv:2606.26511v1 — §4.5 Marker-free benchmark construction; §5 Experiments; §5.3 Stale-fact error: the structural result；Limitations / counterevidence：arXiv:2606.26511v1 — §6 Discussion; §7 Limitations; §8 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已覆盖通用命题，不重复追加。
### [VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills](https://arxiv.org/html/2606.26524v1)

**机制与贡献。** Agentic systems increasingly act through third-party skills, allowing model-generated decisions to affect files, communication channels, and cyber-physical devices. These skills often include natural-language specifications that define access permissions, disclosure limits, execution privileges, and required preconditions.

**证据边界。** exact-v1 Method：arXiv:2606.26524v1 — §IV The Vigil Framework; §IV-A Algorithm Overview；Evaluation：arXiv:2606.26524v1 — §VII Evaluation; §VII-A Experimental Setup；Limitations / counterevidence：arXiv:2606.26524v1 — §III-C Threat Model; §IX Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [Moebius: Serving Mixture-of-Expert Models with Seamless Runtime Parallelism Switch](https://arxiv.org/html/2606.26607v1)

**机制与贡献。** Mixture-of-Experts (MoE) architectures scale large language models (LLMs) to hundreds of billions of parameters. Serving a single MoE model requires multiple GPUs operating in parallel, typically through tensor parallelism (TP) or expert parallelism (EP).

**证据边界。** exact-v1 Method：arXiv:2606.26607v1 — §4 System Design; §Appendix B End-to-End Training Projection；Evaluation：arXiv:2606.26607v1 — §6 Evaluation; §6.1 Experimental Setup；Limitations / counterevidence：arXiv:2606.26607v1 — §2.2 Real World Workloads Cross the Boundary; §8 Discussion; §9 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-SCHEDULING`。[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 顶层 Review notes 前的“SLO-aware Admission；Expert weights 与 KV 的联合 working set”已覆盖通用命题，不重复追加。
### [Autoformalization of Agent Instructions into Policy-as-Code](https://arxiv.org/html/2606.26649v1)

**机制与贡献。** Agent safety in high-stakes domains requires formal policy enforcement, but most existing approaches either rely on probabilistic guardrails (fine-tuned classifiers, prompt-based steering) that offer no formal guarantees, or on hand-coded symbolic enforcement that does not scale to the breadth of real policy specifications. We present an autoformalization pipeline that translates agent prompts, MCP tool descriptions, and natural language policy documents into formally verified policies using an LLM-based generator-critic loop.

**证据边界。** exact-v1 Method：arXiv:2606.26649v1 — §2 Approach；Evaluation：arXiv:2606.26649v1 — §3 Evaluation；Limitations / counterevidence：arXiv:2606.26649v1 — §4 Discussion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [PersistentKV: Page-Aware Decode Scheduling for Long-Context LLM Serving on Commodity GPUs](https://arxiv.org/html/2606.26666v1)

**机制与贡献。** Autoregressive large language model (LLM) serving is increasingly limited by key-value (KV) cache movement rather than dense matrix multiplication. Modern paged-attention systems reduce fragmentation, and mature kernels like FlashInfer provide highly optimized decode attention.

**证据边界。** exact-v1 Method：arXiv:2606.26666v1 — §3 Methodology；Evaluation：arXiv:2606.26666v1 — §4 Experiments; §4.1 Experimental Setup; §4.3 Main Serving Results；Limitations / counterevidence：arXiv:2606.26666v1 — §5 Discussion; §5.1 Threats to Validity; §6 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-KV-CACHE`。[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 顶层 Review notes 前的“从不可逆 Eviction 到可恢复的分层 Recall”已覆盖通用命题，不重复追加。
### [SKILL-DISCO: Distilling and Compiling Agent Traces into Reusable Procedural Skills](https://arxiv.org/html/2606.26669v1)

**机制与贡献。** Agents often repeatedly solve similar task instances from scratch, leading to unnecessary reasoning cost and long execution traces. Prior work has explored workflow reuse and executable skill induction, but it remains unclear which task scenarios admit procedural skills and how the shared procedural structure should be represented across successful traces.

**证据边界。** exact-v1 Method：arXiv:2606.26669v1 — §3 The Skill-DisCo Framework; §3.1 Framework Overview；Evaluation：arXiv:2606.26669v1 — §4 Experiments; §4.1 Experimental Setup; §Appendix A Full Results: Token Usage and Inference Cost；Limitations / counterevidence：arXiv:2606.26669v1 — §6 Conclusion; §Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-TOOL-CALLING`。[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md) 顶层 Review notes 前的“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract”已覆盖通用命题，不重复追加。
### [Knowledge-Based Pull Requests: A Trusted Workflow for Agent-Mediated Knowledge Collaboration](https://arxiv.org/html/2606.26721v1)

**机制与贡献。** AI coding agents are changing the bottleneck in software collaboration: code is increasingly cheap, while understanding intent, negotiating scope, and governing long-term project responsibility remain costly. This paper proposes \emph{Knowledge-Based Pull Requests} (KPR), a trusted workflow for agent-mediated software collaboration across trust boundaries, including open source, enterprise, vendor, contractor, and customer-driven settings.

**证据边界。** exact-v1 Method：arXiv:2606.26721v1 — §6. Prototype Architecture: A Collaboration Gateway；Evaluation：arXiv:2606.26721v1 — §8. Evaluation Agenda；Limitations / counterevidence：arXiv:2606.26721v1 — §3.3. The Trust Boundary; §9. Risks and Limitations; §10. Discussion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-WORKFLOW`。[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md) 顶层 Review notes 前的“Template、Realized Graph 与 Trace 不是同一个对象”已覆盖通用命题，不重复追加。
### [HyperDFlash: Hyper-Connection-Aligned Block Speculative Decoding with Gated Residual Reduction](https://arxiv.org/html/2606.26744v1)

**机制与贡献。** We present HyperDFlash, a block-parallel speculative decoding framework tailored to DeepSeek-V4's Hyper-Connections (HC). Despite the strong performance of DeepSeek-V4's native Multi-Token Prediction (MTP) module on initial token drafting, its draft accuracy degrades sharply at later positions, as error accumulation from unverified intermediate tokens harms draft acceptance rates.

**证据边界。** exact-v1 Method：arXiv:2606.26744v1 — §2 Method；Evaluation：arXiv:2606.26744v1 — §3 Experiments; §3.2 Benchmarks; §3.5 Main Results；Limitations / counterevidence：arXiv:2606.26744v1 — §5 Conclusion; §Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-SPECULATIVE-DECODING`。[books/part-05-inference-system/48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md) 顶层 Review notes 前的“Acceptance 不是独立常数，在线决策必须结算系统状态”已覆盖通用命题，不重复追加。
### [The Capability Frontier: Benchmarks Miss 82% of Model Performance](https://arxiv.org/html/2606.26836v1)

**机制与贡献。** Existing benchmarks typically report accuracy for a single model on a single run. This systematically understates real-world LLM capabilities, particularly under heterogeneous data distributions: (i) different models get different questions correct according to their specializations, and (ii) given a budget, multiple generations can be sampled and selectively retained.

**证据边界。** exact-v1 Method：arXiv:2606.26836v1 — §4 Oracle Bias and Debiasing Methods; §4.3 Debiasing Methods; §4.3.1 Method 1: Extrapolation；Evaluation：arXiv:2606.26836v1 — §The Capability Frontier: Benchmarks Miss 82% of Model Performance; §5 Experimental Setup; §Benchmarks.；Limitations / counterevidence：arXiv:2606.26836v1 — §7 Limitations; §8 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [Information-Aware KV Cache Compression for Long Reasoning](https://arxiv.org/html/2606.26875v1)

**机制与贡献。** Reasoning capability has advanced rapidly in large language models (LLMs), leading to an increasing size of key-value (KV) cache in both prefilling and decoding stages. Existing KV cache compression methods mainly rely on attention weights to estimate token importance.

**证据边界。** exact-v1 Method：arXiv:2606.26875v1 — §3 Methodology；Evaluation：arXiv:2606.26875v1 — §4 Experiments; §4.1 Setup; §5 Analysis；Limitations / counterevidence：arXiv:2606.26875v1 — §6 Conclusion; §Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-KV-CACHE`。[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 顶层 Review notes 前的“从不可逆 Eviction 到可恢复的分层 Recall”已覆盖通用命题，不重复追加。
### [Diagnosing Task Insensitivity in Language Agents](https://arxiv.org/html/2606.26918v1)

**机制与贡献。** Large language models can serve as capable long-horizon agents, but their out-of-distribution (OOD) generalization remains weak. We identify a key source of this failure as task insensitivity: when faced with similar but distinct tasks, models might apply patterns learned during training and fail to solve the task at hand.

**证据边界。** exact-v1 Method：arXiv:2606.26918v1 — §3 Diagnostics: Task Insensitivity in Agentic Training; §3.2 Training-Time Dynamics Associated with Overfitting; §4 Observed Attention Drift During Training；Evaluation：arXiv:2606.26918v1 — §6 Experiments; §6.1 Experimental Setup; §6.2 Main Results；Limitations / counterevidence：arXiv:2606.26918v1 — §7 Conclusion; §Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-PLANNING`。[books/part-07-agent/79-planning.md](../../../../books/part-07-agent/79-planning.md) 顶层 Review notes 前的“学习到的 Transition 只能验证候选，不能提交环境事实”已覆盖通用命题，不重复追加。
### [A Deterministic Control Plane for LLM Coding Agents](https://arxiv.org/html/2606.26924v1)

**机制与贡献。** LLM coding harnesses grant agents broad file and shell access, yet the configuration layer that steers them -- rules files, agent definitions, IDE-specific markdown -- is largely unmanaged. A prevalence study of 10,008 public GitHub repositories (n=6,145 agent config files) finds that agent configurations propagate as undeclared shared components: 10.1% of tracked paths are SHA-256 exact duplicates across independent repositories (fork-adjusted, threshold-independent), with 75.5% of clone pairs crossing organisational boundaries.

**证据边界。** exact-v1 Method：arXiv:2606.26924v1 — §2.2 Orchestration frameworks and Autonomous Agents; §3. System Architecture; §Lifecycle design rationale；Evaluation：arXiv:2606.26924v1 — §6.2 Conformance results; §7.2 Results；Limitations / counterevidence：arXiv:2606.26924v1 — §Trust boundary: cooperative trace linkage; §5. Threat Model; §7.4 Limitations of the study。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-PLATFORM`。[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md) 顶层 Review notes 前的“Agent Runtime State Machine；Harness、Protocol 与 Credit 都是 Platform-owned Artifact”已覆盖通用命题，不重复追加。
### [To Run or Not to Run: Analyzing the Cost-Effectiveness of Code Execution in LLM-Based Program Repair](https://arxiv.org/html/2606.26978v1)

**机制与贡献。** LLM-based agents for program repair are increasingly built on a "generate-run-revise" paradigm, iteratively executing tests to evaluate and refine patches. This execution-based approach has become standard practice in state-of-the-art systems.

**证据边界。** exact-v1 Method：arXiv:2606.26978v1 — §3. Experimental Setup; §3.5. Implementation Details；Evaluation：arXiv:2606.26978v1 — §4. Evaluation; §4.2. RQ2: Effectiveness and Cost Analysis；Limitations / counterevidence：arXiv:2606.26978v1 — §5.2. Threats to Validity; §7. Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-TOOL-CALLING`。[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md) 顶层 Review notes 前的“模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract”已覆盖通用命题，不重复追加。
### [How Much Static Structure Do Code Agents Need? A Study of Deterministic Anchoring](https://arxiv.org/html/2606.26979v1)

**机制与贡献。** LLM-based code agents navigate repositories through keyword search but miss the structural relationships, such as call graphs, inheritance hierarchies, and configuration dependencies, that define how software actually works. This makes agent navigation stochastic and difficult to reproduce across runs.

**证据边界。** exact-v1 Method：arXiv:2606.26979v1 — §4. Approach; §4.1. System Overview；Evaluation：arXiv:2606.26979v1 — §3. Motivation and Problem Analysis; §4.2. CodeAnchor Tags: Static-Analysis-Based Structured Comments; §5. Evaluation；Limitations / counterevidence：arXiv:2606.26979v1 — §6. Discussion; §7. Threats to Validity and Limitations; §9. Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-CONTEXT`。[books/part-07-agent/75-context.md](../../../../books/part-07-agent/75-context.md) 顶层 Review notes 前的“Context Compression 必须保留执行状态，而不只是语义”已覆盖通用命题，不重复追加。
### [Decision-Aligned Evaluation of Uncertainty Quantification](https://arxiv.org/html/2606.26990v1)

**机制与贡献。** Uncertainty estimates in machine learning are typically evaluated using generic metrics such as the negative log-likelihood and expected calibration error, yet good performance on such metrics does not necessarily imply high utility in downstream decisions. We introduce decision-alignment, a criterion that reveals which evaluation metrics meaningfully align with downstream utilities.

**证据边界。** exact-v1 Method：arXiv:2606.26990v1 — §Remark 3.3 (On the choice of our framework) .；Evaluation：arXiv:2606.26990v1 — §Decision-Aligned Evaluation of Uncertainty Quantification; §Common UQ evaluation metrics in ML; §5 Experiments；Limitations / counterevidence：arXiv:2606.26990v1 — §6 Conclusion; §Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [RolloutPipe: Overlapping Pipelined Rollout and Training in Disaggregated On-Policy LLM Reinforcement Learning](https://arxiv.org/html/2606.26997v1)

**机制与贡献。** Large language model (LLM) post-training for reasoning increasingly relies on reinforcement learning with verifiable rewards (RLVR), where models learn from ground-truth feedback on mathematical, logical, and scientific tasks. To enable flexible resource allocation and support heterogeneous training setups, modern RLVR systems adopt disaggregated architectures that decouple rollout generation and policy training across independent GPU pools.

**证据边界。** exact-v1 Method：arXiv:2606.26997v1 — §RolloutPipe: Overlapping Pipelined Rollout and Training in Disaggregated On-Policy LLM Reinforcement Learning; §3 RolloutPipe Design; §3.2 Training-Side Complete-Group Pipelining；Evaluation：arXiv:2606.26997v1 — §5 Performance Evaluation; §5.1 Experimental Setup; §5.2 Results Analysis；Limitations / counterevidence：arXiv:2606.26997v1 — §7 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`。[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md) 顶层 Review notes 前的“异步训练必须分开 Throughput、Freshness 与 Objective Ownership”已覆盖通用命题，不重复追加。
### [Semantic Early-Stopping for Iterative LLM Agent Loops](https://arxiv.org/html/2606.27009v1)

**机制与贡献。** Multi-agent large language model (LLM) loops, for example a Writer that drafts and a Critic that revises, are almost always terminated by a fixed iteration cap (max_iterations). This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones.

**证据边界。** exact-v1 Method：arXiv:2606.27009v1 — §Uncertainty and orchestration in multi-LLM systems.; §IV Method；Evaluation：arXiv:2606.27009v1 — §RAG evaluation.; §V Theoretical Analysis; §VI A Judge-Efficient Evaluation Protocol；Limitations / counterevidence：arXiv:2606.27009v1 — §IX Discussion; §X Limitations; §XI Conclusion and Future Work。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-WORKFLOW`。[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md) 顶层 Review notes 前的“Template、Realized Graph 与 Trace 不是同一个对象”已覆盖通用命题，不重复追加。
### [ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP](https://arxiv.org/html/2606.27027v1)

**机制与贡献。** With the rapid evolution of LLM-driven agents, Model Context Protocol (MCP), an open protocol bridging LLMs with external tools, has quickly become foundational to modern agent ecosystems. However, the expanding adoption of MCP has also introduced novel security concerns such as Tool Poisoning Attack (TPA), which exploit LLM-server interactions to inject malicious prompts.

**证据边界。** exact-v1 Method：arXiv:2606.27027v1 — §4. ShareLock: a Multi-Tool Threshold Poisoning Attack Framework; §D.1. System Prompt for Zero-Shot Detection；Evaluation：arXiv:2606.27027v1 — §5. Evaluation; §5.1. Experimental Setup; §Appendix D Experimental details of Safety Classification Task；Limitations / counterevidence：arXiv:2606.27027v1 — §3.3. Threat Model; §6. Discussion and Limitations; §7. Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MCP`。[books/part-07-agent/83-mcp.md](../../../../books/part-07-agent/83-mcp.md) 顶层 Review notes 前的“MCP 不等于 Tool Authorization；从单工具扫描到组合级 Admission”已覆盖通用命题，不重复追加。
### [The Spec Growth Engine: Spec-Anchored, Code-Coupled, Drift-Enforced Architecture for AI-Assisted Software Development](https://arxiv.org/html/2606.27045v1)

**机制与贡献。** AI coding agents dramatically accelerate implementation speed but introduce two structural failure modes that existing spec-driven approaches do not fully solve: (1) context explosion -- the agent must reason over an entire repository at once, degrading output quality as the context window fills; and (2) silent spec-code drift -- code evolves, the specification does not, and the divergence becomes invisible until it is costly to repair. We present the Spec Growth Engine, a lightweight framework that addresses both failure modes through a machine-readable spec graph whose nodes carry explicit contract/design separation, a Spine context assembler that scopes agent context to an ownership path, a vertical-slice growth protocol that enforces hardest-first ordering, and a drift gate that makes spec-code divergence a blocking merge condition.

**证据边界。** exact-v1 Method：arXiv:2606.27045v1 — §5 The Spec Growth Engine; §5.2 The Spec Graph: Nodes and Edges; §5.4 Drift Validation: Intent Graph vs. Evidence Graph；Evaluation：arXiv:2606.27045v1 — §6 Development Workflow; §7 Worked Example: Growing a Checkout；Limitations / counterevidence：arXiv:2606.27045v1 — §9 Discussion; §Limitations.; §10 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-CONTEXT`。[books/part-07-agent/75-context.md](../../../../books/part-07-agent/75-context.md) 顶层 Review notes 前的“Context Compression 必须保留执行状态，而不只是语义”已覆盖通用命题，不重复追加。
### [DMuon: Efficient Distributed Muon Training with Near-Adam Overhead](https://arxiv.org/html/2606.27153v1)

**机制与贡献。** Matrix-orthogonalization-based optimizers, exemplified by Muon, have demonstrated strong convergence behavior across a wide range of modern deep learning workloads. The matrix-aware updates offer a compelling alternative to conventional element-wise optimization, particularly as model architectures continue to grow in scale and heterogeneity.

**证据边界。** exact-v1 Method：arXiv:2606.27153v1 — §DMuon: Efficient Distributed Muon Training with Near-Adam Overhead; §2.2 Sharded Training Abstractions; §3 System Design；Evaluation：arXiv:2606.27153v1 — §5 Evaluation; §Setup.；Limitations / counterevidence：arXiv:2606.27153v1 — §5.3 Limitations; §7 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`。[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md) 顶层 Review notes 前的“异步训练必须分开 Throughput、Freshness 与 Objective Ownership”已覆盖通用命题，不重复追加。
### [OpenRCA 2.0: From Outcome Labels to Causal Process Supervision](https://arxiv.org/html/2606.27154v1)

**机制与贡献。** Root cause analysis (RCA) poses a holistic test of LLM agentic capabilities, such as long-context understanding, multi-step reasoning, and tool use. However, existing datasets suffer from a fundamental gap: they label only the root cause, not the propagation path connecting it to the observed symptom, which largely simplifies the task to naive pattern matching.

**证据边界。** exact-v1 Method：arXiv:2606.27154v1 — §Appendix B Benchmark Systems and Topology; §B.1 Systems Overview; §F.1 Agent Evaluation Framework；Evaluation：arXiv:2606.27154v1 — §2.1 Setup: Forward Verification from a Known Intervention; §3 Experiments; §3.1 Experimental Setup；Limitations / counterevidence：arXiv:2606.27154v1 — §3.3 Failure Mode Characterization; §5 Assumptions and Threats to Validity; §6 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-TRACE`。[books/part-06-ai-infrastructure/69-trace.md](../../../../books/part-06-ai-infrastructure/69-trace.md) 顶层 Review notes 前的“provenance/evidence 不等于 truth”已覆盖通用命题，不重复追加。
### [Ask, Don't Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement](https://arxiv.org/html/2606.27226v1)

**机制与贡献。** Evaluating LLM outputs remains a major bottleneck in NLP: human evaluation is expensive and slow, lexical metrics correlate poorly with human judgments on open-ended generation, and holistic LLM judges often produce opaque scores that are hard to debug. We propose BINEVAL, a framework that decomposes evaluation criteria into atomic binary questions and aggregates the resulting verdicts into interpretable, multi-dimensional scores.

**证据边界。** exact-v1 Method：arXiv:2606.27226v1 — §3 Method; §Appendix C Automatic Prompt Update Algorithm；Evaluation：arXiv:2606.27226v1 — §Ask, Don’t Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement; §3.2 Binary Evaluation and Scoring; §4 Experimental Setup；Limitations / counterevidence：arXiv:2606.27226v1 — §6 Discussion; §7 Conclusion; §A.2.3 Example 3: Failure Case — Relevance (SummEval)。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models](https://arxiv.org/html/2606.27288v1)

**机制与贡献。** Multi-model LLM systems such as routing, voting, cascades, fusion, and mixture-of-agents are used to beat single-model accuracy. We show that their gain is capped by a quantity the field rarely reports.

**证据边界。** exact-v1 Method：arXiv:2606.27288v1 — §3 Problem Formulation; §Proposition 1 (Ceiling, gain localization, and a realizability certificate) .；Evaluation：arXiv:2606.27288v1 — §4 Experimental Setup; §5 Results；Limitations / counterevidence：arXiv:2606.27288v1 — §7 Limitations; §Honest limits.; §8 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MULTI-AGENT`。[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md) 顶层 Review notes 前的“Message 不是 State；Verification Delay 也是拓扑控制状态”已覆盖通用命题，不重复追加。

## 5. 缺口与下一步

无

闭合账目：raw=566；旧候选 provenance=85；V3 候选=36；旧候选降级=49。FP 全量重裁与 24 项 FN 分层抽检均未发现待处理问题；全部 Integrate 已反查当前 owner 的顶层 Review notes 前正文；全部 Existing Coverage 已绑定正文命题锚点。

## 6. 复核

复核者：V3 恢复语义复核（独立于旧 V2.1 报告作者；2026-09-10）

结论：通过

独立复核覆盖 canonical owner 日期、撤回排除、旧候选 FP 全量重裁、24 项 FN 分层抽样、closure taxonomy、exact-v1 定位、每个 Integrate 的顶层 Review notes 前正文，以及每个 Existing Coverage 的正文命题锚点。审计明确区分“题摘准入”与“Books trace”，并排除 AI for Science、纯领域 benchmark、局部模型/表示改进和仅凭 ROADMAP 映射的材料。机器校验只证明结构一致性。
