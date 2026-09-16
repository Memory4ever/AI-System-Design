# Daily Research — 2026-06-29

**规范：** V3
**窗口：** 2026-06-28T09:00:00+08:00 ～ 2026-06-29T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T09:36:20+08:00

## 1. 结论

本窗恢复 380 个 canonical arXiv identity，逐项以完整题摘按当前“大模型与大模型基础设施”贡献门槛重审，冻结 24 个候选。旧 V2.1 的 63 个候选只作 provenance，39 项因垂直任务、领域 benchmark、局部表示/方法或仅能映射 ROADMAP 而在候选前关闭；没有以 Books trace 反向证明准入。

本轮候选前关闭（不计入 Candidate Denominator）：

- `2606.27558` / `SF-2026-ARXIV-2606-27558` — LinkedIn race/ethnicity fairness measurement 的通用产品 ML 隐私方案；不是大模型或大模型基础设施贡献
- `2606.27841` / `SF-2026-ARXIV-2606-27841` — 面向 295 个通用 neural architectures 的 task-independent layer-wise energy estimator；没有形成 LLM-specific inference/service contract
- `2606.27997` / `SF-2026-ARXIV-2606-27997` — 主要对象是 TSC/推荐数据集子集选择，MTEB 只是补充实验；排名保持是通用 benchmark 方法，不是大模型系统贡献

候选均复用可核实的 exact-v1 Method / Evaluation / Limitations 定位。Books 结果为 2 项整合、22 项已有覆盖；本次同步没有修改 Books、LEARNING_STATE 或跨日索引。

2026-09-14 按当前来源清单重放 13 个机构每日源并复用仍匹配的 arXiv / exact-v1 / Evidence / Books 证据。机构源补查没有新增候选或 Books 工作；冻结分母仍为 24。详细过程见 [当前合同再认证](../_sources/daily-20260629/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)。/root 非作者独立复核已通过。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [当前合同再认证](../_sources/daily-20260629/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列与窗口定点检索；本窗无范围内新增 | 已检查 | 无 |
| SRC-ANTHROPIC | [当前合同再认证](../_sources/daily-20260629/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-GOOGLE-AI | [当前合同再认证](../_sources/daily-20260629/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：DeepMind / Google Research 官方索引；本窗无范围内新增 | 已检查 | 无 |
| SRC-META-AI | [当前合同再认证](../_sources/daily-20260629/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-QWEN | [当前合同再认证](../_sources/daily-20260629/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方博客时间序列；本窗无新 family / 重要 revision | 已检查 | 无 |
| SRC-DEEPSEEK | [当前合同再认证](../_sources/daily-20260629/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research / 发布索引；本窗无新 family / 重要 revision | 已检查 | 无 |
| SRC-MOONSHOT | [当前合同再认证](../_sources/daily-20260629/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：Kimi Blog 与官方仓库发布时序；本窗无范围内新增 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | [当前合同再认证](../_sources/daily-20260629/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 publicList 8/8 条按展示首发日期检查；本窗无范围内新增 | 已检查 | 无 |
| SRC-ZAI | [当前合同再认证](../_sources/daily-20260629/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research 时间序列；本窗无范围内新增 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [当前合同再认证](../_sources/daily-20260629/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Research、论文目录与发布页；本窗无范围内新增 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [当前合同再认证](../_sources/daily-20260629/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方技术博客与仓库发布时序；本窗无范围内新增 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [当前合同再认证](../_sources/daily-20260629/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：官方 Paper / Blog 与仓库；本窗无范围内新增 | 已检查 | 无 |
| SRC-MINIMAX | [当前合同再认证](../_sources/daily-20260629/CURRENT_CONTRACT_RECERTIFICATION_20260914.md)：中英文博客与 Agent Tech Blog；相邻条目为 06-09/06-01，本窗无新增 | 已检查 | 无 |
| SRC-ARXIV | [canonical raw inventory](../_sources/daily-20260629/canonical-raw-identity-inventory-v2.1.json.gz)；380 个 owner identity 完成题摘筛选；[V3 audit](../_sources/daily-20260629/v3-admission-audit-20260910.json) | 已检查 | 无 |

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability；只有当前题摘贡献成立时才复用旧分数与 exact-v1 定位。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Towards Evaluation of Implicit Software World Models in Coding LLMs](https://arxiv.org/html/2606.27406v1) | 2026-06-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement](https://arxiv.org/html/2606.27409v1) | 2026-06-29T08:00:00+08:00 | AGENT-MULTI-AGENT；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[目标章](../../../../books/part-07-agent/82-multi-agent.md)“Message 不是 State；Verification Delay 也是拓扑控制状态” |
| [Glite ARF: Verifier-Driven Research with Parallel LLM Coding Agents](https://arxiv.org/html/2606.27416v1) | 2026-06-29T08:00:00+08:00 | AGENT-PLATFORM；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[目标章](../../../../books/part-07-agent/84-agent-platform.md)“Agent Runtime State Machine；Harness、Protocol 与 Credit 都是 Platform-owned Artifact” |
| [Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving](https://arxiv.org/html/2606.27457v1) | 2026-06-29T08:00:00+08:00 | PLATFORM-GATEWAY；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-GATEWAY，[目标章](../../../../books/part-06-ai-infrastructure/62-gateway.md)“policy/path/endpoint identity 与 route/fallback receipt” |
| [Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents](https://arxiv.org/html/2606.27472v1) | 2026-06-29T08:00:00+08:00 | AGENT-MEMORY；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery” |
| [When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems](https://arxiv.org/html/2606.27511v1) | 2026-06-29T08:00:00+08:00 | PLATFORM-SECURITY；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction](https://arxiv.org/html/2606.27550v1) | 2026-06-29T08:00:00+08:00 | INFER-SPECULATIVE-DECODING；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[目标章](../../../../books/part-05-inference-system/48-speculative-decoding.md)“Acceptance 不是独立常数，在线决策必须结算系统状态” |
| [On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models](https://arxiv.org/html/2606.27567v1) | 2026-06-29T08:00:00+08:00 | PLATFORM-SECURITY；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration](https://arxiv.org/html/2606.27578v1) | 2026-06-29T08:00:00+08:00 | TRAIN-RLHF；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-RLHF，[目标章](../../../../books/part-04-training-system/31-rlhf.md)“Reward Heterogeneity 同时存在于 Rater Identity 与反馈时间” |
| [Retroactive Advantage Correction: Closed-Form V-Trace Bias Correction for Delay-Aware RLHF](https://arxiv.org/html/2606.27580v1) | 2026-06-29T08:00:00+08:00 | TRAIN-RLHF；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-RLHF，[目标章](../../../../books/part-04-training-system/31-rlhf.md)“Reward Heterogeneity 同时存在于 Rater Identity 与反馈时间” |
| [When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search](https://arxiv.org/html/2606.27669v1) | 2026-06-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [From Signals to Transfer: A Factorised Study of Probe-Based Uncertainty Estimation in Large Language Models](https://arxiv.org/html/2606.27679v1) | 2026-06-29T08:00:00+08:00 | PLATFORM-MONITORING；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：PLATFORM-MONITORING，[目标章](../../../../books/part-06-ai-infrastructure/67-monitoring.md)“calibration-bound sensor、direct profile fallback 与 monitor 不拥有 truth/commit” |
| [CBD: API-Only LLM Black-Box Unlearning through Controlled Behavioral Divergence](https://arxiv.org/html/2606.27683v1) | 2026-06-29T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [End-to-End Dynamic Sparsity for Resource-Adaptive LLM Inference](https://arxiv.org/html/2606.27743v1) | 2026-06-29T08:00:00+08:00 | INFER-SCHEDULING；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：INFER-SCHEDULING，[目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md)“SLO-aware Admission；Expert weights 与 KV 的联合 working set” |
| [Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems](https://arxiv.org/html/2606.27797v1) | 2026-06-29T08:00:00+08:00 | TRAIN-DISTRIBUTED-TRAINING；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[目标章](../../../../books/part-04-training-system/36-distributed-training.md)“Teacher 与 Student 不应共享一份并行 Plan”下“知识蒸馏在 teacher 与 student 规模接近、激活生命周期相似时”段落 |
| [Agent vs. Parametric World Models: Hybrid Planning for Reliable Language Agents](https://arxiv.org/html/2606.27806v1) | 2026-06-29T08:00:00+08:00 | AGENT-PLANNING；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-PLANNING，[目标章](../../../../books/part-07-agent/79-planning.md)“学习到的 Transition 只能验证候选，不能提交环境事实”下“只让语言模型在同一 Context 中想象 state delta 并继续规划”段落 |
| [Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking](https://arxiv.org/html/2606.27934v1) | 2026-06-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents](https://arxiv.org/html/2606.27944v1) | 2026-06-29T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement Autoformalization](https://arxiv.org/html/2606.28013v1) | 2026-06-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA](https://arxiv.org/html/2606.28050v1) | 2026-06-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Evaluation Identity 必须包含 Harness 与 Environment” |
| [ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents](https://arxiv.org/html/2606.28061v1) | 2026-06-29T08:00:00+08:00 | PLATFORM-SECURITY；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)“Canonical Action 与 Effect-time Authorization” |
| [Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability](https://arxiv.org/html/2606.28116v1) | 2026-06-29T08:00:00+08:00 | PLATFORM-MONITORING；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-MONITORING，[目标章](../../../../books/part-06-ai-infrastructure/67-monitoring.md)“calibration-bound sensor、direct profile fallback 与 monitor 不拥有 truth/commit” |
| [Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software](https://arxiv.org/html/2606.28235v1) | 2026-06-29T08:00:00+08:00 | AGENT-PLATFORM；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-PLATFORM，[目标章](../../../../books/part-07-agent/84-agent-platform.md)“Agent Runtime State Machine；Harness、Protocol 与 Credit 都是 Platform-owned Artifact” |
| [Agentic Hardware Design as Repository-Level Code Evolution](https://arxiv.org/html/2606.28279v1) | 2026-06-29T08:00:00+08:00 | AGENT-WORKFLOW；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[目标章](../../../../books/part-07-agent/81-workflow.md)“Template、Realized Graph 与 Trace 不是同一个对象” |

## 4. 证据与知识整合

### [Towards Evaluation of Implicit Software World Models in Coding LLMs](https://arxiv.org/html/2606.27406v1)

**机制与贡献。** Software engineering, whether performed by humans or by AI agents, requires reasoning about how software behaves. We call the internal model that supports such reasoning the software world model, and view current code-execution benchmarks as covering one well-studied slice of it -- control flow.

**证据边界。** exact-v1 Method：arXiv:2606.27406v1 — §2 Data; §3 Metrics; §4 Experiment Setup；Evaluation：arXiv:2606.27406v1 — §5 Results Discussion；Limitations / counterevidence：arXiv:2606.27406v1 — §6 Limitations; §7 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement](https://arxiv.org/html/2606.27409v1)

**机制与贡献。** Multi-agent large language model (LLM) systems often rely on verifier and critic agents to suppress hallucinations, but verification is delayed. During this delay, false claims can propagate through the agent network.

**证据边界。** exact-v1 Method：arXiv:2606.27409v1 — §3 Model; §4 Stability and the verification dose; §5 Optimal corrector placement；Evaluation：arXiv:2606.27409v1 — §7 Empirical validation; §7.1 Onset at the predicted dose limit (RQ1)；Limitations / counterevidence：arXiv:2606.27409v1 — §8 Discussion; §10 Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MULTI-AGENT`。[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md) 顶层 Review notes 前的“Message 不是 State；Verification Delay 也是拓扑控制状态”已覆盖通用命题，不重复追加。
### [Glite ARF: Verifier-Driven Research with Parallel LLM Coding Agents](https://arxiv.org/html/2606.27416v1)

**机制与贡献。** LLM coding agents make it tempting to automate empirical research by delegating experiments to them directly, but naive delegation does not scale to large projects: low-rate instruction lapses compound into broken, irreproducible artefacts. To address this problem, we present Glite ARF, an open-source Python framework for running many LLM coding agents in parallel on a research repository without sacrificing reproducibility or auditability.

**证据边界。** exact-v1 Method：arXiv:2606.27416v1 — §3 System; §3.1 Architecture and seven principles; §5 The framework in use；Evaluation：arXiv:2606.27416v1 — §Evaluation regime.; §Workflow, provenance, and experiment management.; §4.3 Headline result；Limitations / counterevidence：arXiv:2606.27416v1 — §Limitations.; §Appendix D Observed failure modes。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-PLATFORM`。[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md) 顶层 Review notes 前的“Agent Runtime State Machine；Harness、Protocol 与 Credit 都是 Platform-owned Artifact”已覆盖通用命题，不重复追加。
### [Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving](https://arxiv.org/html/2606.27457v1)

**机制与贡献。** Efficient deployment of large language models (LLMs) in production forces a trade-off between accuracy and cost. Operators often default to a single model that is either expensive for easy queries or insufficient for hard ones.

**证据边界。** exact-v1 Method：arXiv:2606.27457v1 — §Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving; §3 System Overview; §Appendix B Framework Extensibility: AIME Pool Expansion；Evaluation：arXiv:2606.27457v1 — §4.3 Pareto Analysis and Model Selection; §7 Experiments and Results; §Appendix A Inference Setup；Limitations / counterevidence：arXiv:2606.27457v1 — §8 Conclusion and Future Work; §Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-GATEWAY`。[books/part-06-ai-infrastructure/62-gateway.md](../../../../books/part-06-ai-infrastructure/62-gateway.md) 顶层 Review notes 前的“policy/path/endpoint identity 与 route/fallback receipt”已覆盖通用命题，不重复追加。
### [Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents](https://arxiv.org/html/2606.27472v1)

**机制与贡献。** Large language model (LLM) agents operate over long, multi-session interactions in which facts change: a user moves, a price updates, a plan is revised. Acting correctly requires using the current value of a fact and discarding values that have been superseded.

**证据边界。** exact-v1 Method：arXiv:2606.27472v1 — §Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents; §Memory systems and RL for memory.; §Deployed memory systems.；Evaluation：arXiv:2606.27472v1 — §Long-term memory benchmarks.; §4 Experimental Setup; §Training setup.；Limitations / counterevidence：arXiv:2606.27472v1 — §Failure modes.; §6 Discussion; §7 Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-MEMORY`。[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md) 顶层 Review notes 前的“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”已覆盖通用命题，不重复追加。
### [When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems](https://arxiv.org/html/2606.27511v1)

**机制与贡献。** Large Language Model (LLM)-based question-answering (QA) systems are increasingly deployed in sensitive domains such as healthcare, mental health counseling, and legal consultation. Federated learning (FL) enables collaborative training without sharing raw client data, for which locally trained models are aggregated at a central server (i.e., a cloud service provider) to obtain a global model.

**证据边界。** exact-v1 Method：arXiv:2606.27511v1 — §When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems; §2.3 Fine-Tuning Strategies in FL Training; §5 Methodology；Evaluation：arXiv:2606.27511v1 — §6 Evaluations; §6.1 Experimental Setup; §Appendix C Experiment Details.；Limitations / counterevidence：arXiv:2606.27511v1 — §2.4 Federated LLMs and Server-side Threats; §3 Threat Model; §8 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction](https://arxiv.org/html/2606.27550v1)

**机制与贡献。** Multi-token prediction has been shown to increase data density during training, improve downstream text-generation quality, and serves as the defacto approach for self-speculative decoding. Existing foundation and open source models that use MTP heads commit to a static tree-based attention topology throughout the entire generation sequence, meaning the speculation depth, and thus the compute required during verification, stays constant regardless of the context.

**证据边界。** exact-v1 Method：arXiv:2606.27550v1 — §3 Optimizing Task-Specific Greedy Draft Trees; §4 Inference-Time Tree Scheduler；Evaluation：arXiv:2606.27550v1 — §5 Evaluation Methodology; §6 Results；Limitations / counterevidence：arXiv:2606.27550v1 — §Appendix C More Frontiers。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-SPECULATIVE-DECODING`。[books/part-05-inference-system/48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md) 顶层 Review notes 前的“Acceptance 不是独立常数，在线决策必须结算系统状态”已覆盖通用命题，不重复追加。
### [On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models](https://arxiv.org/html/2606.27567v1)

**机制与贡献。** Prompt injection is the top security risk for LLM-integrated applications, yet every defense proposed so far has been broken. We prove this is not a coincidence: in shared-embedding architectures that lack enforced control-data separation, perfect prompt-injection prevention is mathematically impossible.

**证据边界。** exact-v1 Method：arXiv:2606.27567v1 — §2 Formal Framework; §Architectures outside scope.；Evaluation：arXiv:2606.27567v1 — §4.7 Main Result: Impossibility of Perfect Semantic-Faithful Control; §8 Connection to Existing Results; §Impossibility results in AI.；Limitations / counterevidence：arXiv:2606.27567v1 — §3 Threat Model and Scope; §9 Discussion; §10 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration](https://arxiv.org/html/2606.27578v1)

**机制与贡献。** Reward models for Reinforcement Learning from Human Feedback (RLHF) pool preferences across thousands of annotators and fit one global affine calibrator, collapsing raters with systematically different rating-scale offsets and slopes into a single average-rater fit that does not match any individual annotator. PEBS is a per-rater empirical-Bayes shrinkage estimator: it fits per-rater affine calibrators on a held-out slice of each annotator's ratings and applies Morris-James-Stein empirical-Bayes shrinkage toward the population mean, in closed form and without retraining the reward model.

**证据边界。** exact-v1 Method：arXiv:2606.27578v1 — §2 Method; §Base-model training details.；Evaluation：arXiv:2606.27578v1 — §2.3 PRISM setup and base reward model; §3 Experiments；Limitations / counterevidence：arXiv:2606.27578v1 — §3.9 Ablations and failure cases; §4 Discussion; §5 Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `TRAIN-RLHF`。[books/part-04-training-system/31-rlhf.md](../../../../books/part-04-training-system/31-rlhf.md) 顶层 Review notes 前的“Reward Heterogeneity 同时存在于 Rater Identity 与反馈时间”已覆盖通用命题，不重复追加。
### [Retroactive Advantage Correction: Closed-Form V-Trace Bias Correction for Delay-Aware RLHF](https://arxiv.org/html/2606.27580v1)

**机制与贡献。** Reinforcement learning from human feedback (RLHF) in production does not always have a synchronous reward signal. Code-execution verifiers, slow judge ensembles, and queued human review can return several gradient steps after the rollout that produced them, breaking the synchronous-reward assumption underlying standard PPO.

**证据边界。** exact-v1 Method：arXiv:2606.27580v1 — §2 Method: Retroactive Advantage Correction；Evaluation：arXiv:2606.27580v1 — §Setup.; §K = 2 K{=}2 result and cost-quality Pareto.; §Scope of the closed-form result.；Limitations / counterevidence：arXiv:2606.27580v1 — §4 Conclusion; §Appendix E Limitations and Discussion; §Background and discussion.。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `TRAIN-RLHF`。[books/part-04-training-system/31-rlhf.md](../../../../books/part-04-training-system/31-rlhf.md) 顶层 Review notes 前的“Reward Heterogeneity 同时存在于 Rater Identity 与反馈时间”已覆盖通用命题，不重复追加。
### [When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search](https://arxiv.org/html/2606.27669v1)

**机制与贡献。** Search agents powered by large language models (LLMs) are increasingly used to solve complex information-seeking tasks, requiring multi-step retrieval and reasoning to fulfill user goals. However, existing benchmarks often assume that user queries are complete and explicit, overlooking the fact that real-world search requests are frequently vague, underspecified, or even factually incorrect.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.27669v1 — §4 Methodology of Dataset Construction; Benchmark Design and Methodology.; Evaluation Framework and User Simulator.；Evaluation：https://arxiv.org/html/2606.27669v1 — §2.1 Web Search Benchmark; 2.2 Ambiguity Benchmark; 2.3 Interactive Clarification Benchmark；Limitations / counterevidence：https://arxiv.org/html/2606.27669v1 — §Search-heavy guessing reveals a major failure mode.; 6 Conclusion; Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [From Signals to Transfer: A Factorised Study of Probe-Based Uncertainty Estimation in Large Language Models](https://arxiv.org/html/2606.27679v1)

**机制与贡献。** Probe-based uncertainty estimation (UE) has emerged as a prominent approach to detect hallucinations in Large Language Models (LLMs) by learning uncertainty from internal model signals. Yet, recent methods vary simultaneously across feature design, training data construction, and evaluation setting, obscuring what actually drives performance.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.27679v1 — §Probe Training.; Probe Architecture and Training Size.；Evaluation：https://arxiv.org/html/2606.27679v1 — §Toolkits, Benchmarks, and Evaluation.; 3.1 Experimental Setup; Evaluation Metrics.；Limitations / counterevidence：https://arxiv.org/html/2606.27679v1 — §4.2 Results and Discussion; 5 Conclusion; Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-MONITORING`。[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md) 顶层 Review notes 前的“calibration-bound sensor、direct profile fallback 与 monitor 不拥有 truth/commit”已覆盖通用命题，不重复追加。
### [CBD: API-Only LLM Black-Box Unlearning through Controlled Behavioral Divergence](https://arxiv.org/html/2606.27683v1)

**机制与贡献。** Edge devices increasingly invoke large language models (LLMs) through API services for context aware edge intelligence, while edge generated data may be collected to improve LLMs and may introduce sensitive, copyrighted, harmful, or outdated information into model behavior. Machine unlearning offers a practical way to remove the influence of undesired data without retraining LLMs.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.27683v1 — §III Preliminaries and Framework; III-A White-Box and Gray-Box Unlearning Methods; III-B API-Only Scenario and Proposed Framework；Evaluation：https://arxiv.org/html/2606.27683v1 — §VI Experiments; VI-A Experimental Setup; VI-B Performance Evaluation；Limitations / counterevidence：https://arxiv.org/html/2606.27683v1 — §VII Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [End-to-End Dynamic Sparsity for Resource-Adaptive LLM Inference](https://arxiv.org/html/2606.27743v1)

**机制与贡献。** Large Language Models (LLMs) inference is typically deployed under a static resource assumption, where models execute a fixed computational graph regardless of the runtime environment. However, real-world cloud infrastructure is inherently dynamic, characterized by fluctuating availability (e.g., spot instance preemption) and tiered Quality-of-Service requirements.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.27743v1 — §3 Methodology; 3.5 Training and Inference；Evaluation：https://arxiv.org/html/2606.27743v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results；Limitations / counterevidence：https://arxiv.org/html/2606.27743v1 — §4.6 Discussion and Limitations; 5 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `INFER-SCHEDULING`。[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 顶层 Review notes 前的“SLO-aware Admission；Expert weights 与 KV 的联合 working set”已覆盖通用命题，不重复追加。
### [Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems](https://arxiv.org/html/2606.27797v1)

**机制与贡献。** Knowledge Distillation (KD) enables training smaller student models under the guidance of larger teacher models, and the widely adopted TRL library implements it. Yet, TRL treats both models symmetrically, missing opportunities to exploit their pronounced asymmetry in memory footprint, and communication requirements.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.27797v1 — §Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems; 2 Background: LLM Training and Parallelism; 2.1 LLM Training；Evaluation：https://arxiv.org/html/2606.27797v1 — §3 Testing Setup; 4 GKD Analysis and Improvements; 4.1 Experimental Results；Limitations / counterevidence：https://arxiv.org/html/2606.27797v1 — §6 Conclusions。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`。已在 [books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md) 顶层 Review notes 前反查机制正文；`SF-2026-ARXIV-2606-27797` 在正文出现 2 次、后置 trace 出现 1 次。
### [Agent vs. Parametric World Models: Hybrid Planning for Reliable Language Agents](https://arxiv.org/html/2606.27806v1)

**机制与贡献。** Language agents plan by generating not only actions but also implicit predictions of how the world will change. These imagined state updates make agents flexible, but they also create a distinct failure mode: hallucinated state claims can be written into context and propagated across subsequent decisions.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.27806v1 — §Our approach: GILP.; LLM API ecosystem.; 4 Method: Grounded Iterative Language Planning；Evaluation：https://arxiv.org/html/2606.27806v1 — §5 Experiments; Setup.; Cost analysis.；Limitations / counterevidence：https://arxiv.org/html/2606.27806v1 — §6 Discussion; 7 Limitations; 8 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-PLANNING`。已在 [books/part-07-agent/79-planning.md](../../../../books/part-07-agent/79-planning.md) 顶层 Review notes 前反查机制正文；`SF-2026-ARXIV-2606-27806` 在正文出现 2 次、后置 trace 出现 1 次。
### [Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking](https://arxiv.org/html/2606.27934v1)

**机制与贡献。** Performance numbers reported for hardware are accepted on trust: the reader cannot recompute them, the apparatus is gone, and the silicon itself can be silently wrong, with fleet studies reporting on the order of one core in a thousand returning incorrect arithmetic with no error raised. We make a reported hardware measurement a tamper-evident, independently checkable record.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.27934v1 — §Approach.；Evaluation：https://arxiv.org/html/2606.27934v1 — §Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking；Limitations / counterevidence：https://arxiv.org/html/2606.27934v1 — §10 Threat model and guarantees; 12 Physical stress and the trust boundary; 14 Scope and limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents](https://arxiv.org/html/2606.27944v1)

**机制与贡献。** Phone-use Agents can execute complex tasks end to end across real mobile applications. By operating a real device on the user's behalf, they reach far more functionalities than CLI agents, which amplifies the real-world harm they can cause when driven for malicious purposes.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.27944v1 — §4 Misuse Collection and the Awareness-to-Action Evaluation Framework; 4.3 Evaluation Framework；Evaluation：https://arxiv.org/html/2606.27944v1 — §4 Misuse Collection and the Awareness-to-Action Evaluation Framework; 4.3 Evaluation Framework; 5 Evaluation Results；Limitations / counterevidence：https://arxiv.org/html/2606.27944v1 — §3 Threat Model; 8 Discussion and Limitation; 9 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement Autoformalization](https://arxiv.org/html/2606.28013v1)

**机制与贡献。** Headline type-correctness (TC\%) of LLM autoformalization has climbed from $\sim$53\% to $\sim$76\% in two years, yet this scalar conceals which errors each method resolves. We propose a signal-coverage matrix that crosses the Lean elaborator (pass/fail) with a semantic-equivalence judgment (equivalent/not), sorting every output into one of four cells: true success (TS), type-only (TO), semantic-only (SO), or both fail (BF).

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28013v1 — §Methods.; 5.1 Per-method cell decomposition; 5.4 A predictive regularity: stratum-rates are method-invariant；Evaluation：https://arxiv.org/html/2606.28013v1 — §4 Experimental Setup; 5 Experimental Results and Analysis；Limitations / counterevidence：https://arxiv.org/html/2606.28013v1 — §6 Discussion and Limitations; 7 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA](https://arxiv.org/html/2606.28050v1)

**机制与贡献。** LLM-as-a-Judge and self-evaluation pipelines implicitly assume that evaluation is easier than generation. We test this in a controlled in-context QA setting where a context passage is the sole information source and each model judges the answer it generated, removing the parametric-knowledge confound of open-domain comparisons.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28050v1 — §3 Methodology; Hard-negative generation for evaluator training.; LoRA training budget.；Evaluation：https://arxiv.org/html/2606.28050v1 — §Generation–evaluation asymmetry.; 3.1 Task Asymmetry Analysis; Evaluation task ( 𝒯 eval \mathcal{T}_{\text{eval}} ).；Limitations / counterevidence：https://arxiv.org/html/2606.28050v1 — §5 Results and Discussion; 6 Conclusion; Limitations。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`。[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 顶层 Review notes 前的“Evaluation Identity 必须包含 Harness 与 Environment”已覆盖通用命题，不重复追加。
### [ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents](https://arxiv.org/html/2606.28061v1)

**机制与贡献。** Large language models (LLMs) have increasingly moved from standalone text generation systems to agents that invoke external tools, access environments, and execute multi-step tasks. However, conventional function-calling benchmarks mainly evaluate task completion and API correctness, while privacy evaluation benchmarks typically focus on final responses or privacy judgments.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28061v1 — §4.7 System Modules；Evaluation：https://arxiv.org/html/2606.28061v1 — §ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents Note: This work was supported by the Beijing Advanced Innovation Center for Future Blockchain and Privacy Computing (GJJ-25-009).; 2.1 Privacy Evaluation of Large Language Models; 2.2 Tool-Using Agents and Agent Benchmarks；Limitations / counterevidence：https://arxiv.org/html/2606.28061v1 — §8 Representative Failure Cases; 9 Discussion and Implications; 10 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-SECURITY`。[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 顶层 Review notes 前的“Canonical Action 与 Effect-time Authorization”已覆盖通用命题，不重复追加。
### [Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability](https://arxiv.org/html/2606.28116v1)

**机制与贡献。** Frontier large language model training consumes massive accelerator fleets and long wall-clock computation, making stability failures costly when they occur. After a numerical or a hyperparameter fault has already destabilized the training dynamics, it may continue for thousands of steps while loss and gradient norms still appear normal.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28116v1 — §Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability; Training-stability monitors.; 5 Designing Module-Specific Monitors from First Principles；Evaluation：https://arxiv.org/html/2606.28116v1 — §Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability; 1 Introduction；Limitations / counterevidence：https://arxiv.org/html/2606.28116v1 — §6 Limitations; 7 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `PLATFORM-MONITORING`。[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md) 顶层 Review notes 前的“calibration-bound sensor、direct profile fallback 与 monitor 不拥有 truth/commit”已覆盖通用命题，不重复追加。
### [Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software](https://arxiv.org/html/2606.28235v1)

**机制与贡献。** Autonomous coding agents now open and merge pull requests in shared repositories at scale, and the field evaluates them the way it has always evaluated components, one agent at a time, on isolated benchmark tasks. Yet agents that each pass their own tests still leave repositories that accumulate problems no single contribution accounts for.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28235v1 — §Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software; II-C Software ecosystems and coordination cost; II-D Emergence and complex adaptive systems；Evaluation：https://arxiv.org/html/2606.28235v1 — §IV-B Level of analysis and why multilevel models; V Results；Limitations / counterevidence：https://arxiv.org/html/2606.28235v1 — §VI Discussion; VII Threats to Validity; VIII Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-PLATFORM`。[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md) 顶层 Review notes 前的“Agent Runtime State Machine；Harness、Protocol 与 Credit 都是 Platform-owned Artifact”已覆盖通用命题，不重复追加。
### [Agentic Hardware Design as Repository-Level Code Evolution](https://arxiv.org/html/2606.28279v1)

**机制与贡献。** We present HORIZON, a self-evolving agent framework that treats hardware design as repository-level code evolution. A Markdown harness is compiled into a project pack containing domain knowledge, an executable evaluator, an acceptance predicate, and a git/runtime policy; a hands-free agent loop then evolves an isolated git worktree, using repository operations for state management, tracing, and replay.

**证据边界。** exact-v1 Method：https://arxiv.org/html/2606.28279v1 — §Agentic Hardware Design as Repository-Level Code Evolution; Benchmarks for RTL design and verification.; 3 The HORIZON Framework；Evaluation：https://arxiv.org/html/2606.28279v1 — §Benchmarks for RTL design and verification.; 4 Experiments; Setup and protocol.；Limitations / counterevidence：https://arxiv.org/html/2606.28279v1 — §4.3 Detailed discussion on test-generation tasks; 5 Discussion and Limitations; 6 Conclusion。定位只支持作者披露的模型、workload 与设置，不外推到未测规模、生产尾部或普遍保证。

**Books。** 当前唯一 owner 为 `AGENT-WORKFLOW`。[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md) 顶层 Review notes 前的“Template、Realized Graph 与 Trace 不是同一个对象”已覆盖通用命题，不重复追加。

## 5. 缺口与下一步

无

闭合账目：raw=380；旧候选 provenance=63；V3 候选=24；旧候选降级=39。FP 全量重裁与 24 项 FN 分层抽检均未发现待处理问题；全部 Integrate 已反查当前 owner 的顶层 Review notes 前正文；全部 Existing Coverage 已绑定正文命题锚点。

## 6. 复核

复核者：V3 恢复语义复核（独立于旧 V2.1 报告作者；2026-09-10）

结论：通过

独立复核覆盖 canonical owner 日期、撤回排除、旧候选 FP 全量重裁、24 项 FN 分层抽样、closure taxonomy、exact-v1 定位、每个 Integrate 的顶层 Review notes 前正文，以及每个 Existing Coverage 的正文命题锚点。审计明确区分“题摘准入”与“Books trace”，并排除 AI for Science、纯领域 benchmark、局部模型/表示改进和仅凭 ROADMAP 映射的材料。机器校验只证明结构一致性。
