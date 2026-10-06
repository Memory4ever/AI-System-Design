# Daily Research — 2026-05-08

**规范：** V3

**窗口：** 2026-05-07T09:00:00+08:00 ～ 2026-05-08T09:00:00+08:00

**状态：** 完成

**阶段：** fresh non-author final review 已通过；Daily、Evidence 与 Books Gate 均为 Complete

**Books：** 纳入本次

**检查时间：** 2026-09-15T19:39:26+08:00

## 1. 结论

本次按当前合同重新认证 2026-05-08，不继承旧报告的 `Complete`。旧库存 814 条中，619 条属于北京时间 08:00 的 official arXiv announcement batch；195 条 DataCite initial-created proxy 没有官方当窗 owner 证据，全部排除于本日报 raw 与候选之外。13 个非 arXiv Daily 来源按严格窗口定点复查，日期粒度不足的结果只作为隔离限制。

作者已对当前 184 个候选完成 Score V3 与相应深度的 exact-v1 审阅：108 项为 7～9 分、76 项为 5～6 分；129 项深入审阅、55 项标准审阅。最新一轮只重开 fresh non-author review 指定的 18 个 closure false negative；没有扩大来源、日期、sibling 或重扫全部 raw identities。机械账本为 `619 = 184 + 435`，当前候选未见 withdrawn，`Review Pending = 0`。

Books 对读得到 108 项 `Integrate — Applied` 与 76 项 `No Change — Existing Coverage`。本轮 18 项中，15 项新的长期命题已经由 root 写入唯一 owner；`2605.05386`、`2605.05495`、`2605.06040` 分别由 Planning 的 belief/information-gain、Transformer 的 recurrent execution-depth、Planning 的 ToT pruning/budget 主正文具体承载。fresh non-author reviewer 已确认当前正文和 marker 未漂移，整体日报闭合。

`2605.05219` 的残缺 evaluation contract 与 disposition 冲突已修正。cross-day owner 结论未变化：`2605.05250` 只在 05-08 当前活动账本拥有候选身份；`2605.06225`、`2605.06241` 归 05-12 official batch；`2605.05686` 不属于 05-08 canonical 619。root 的 4 项新增 Books 写入与 2 项章内重排已通过上一轮非作者复核；该 reviewer 随后确认的 9 个 false negative 也已完成 exact-v1、评分、Evidence、owner 与 Books 对读，6 项必要写回已落实。本轮最终独立验收通过。

## 2. 来源覆盖

本轮只检查 Daily 来源，不扫描 Weekly 来源。arXiv 归属按官方 scheduled announcement process：May 使用 EDT，Wednesday 20:00 ET 对应北京时间 Thursday 08:00；不按逐项 `submitted`、`updated` 或 DataCite ingestion 拆分同一 announcement batch。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/News 历史目录；定点检查本窗及 05-07 相邻条目 | 已检查 | 05-07 仅日期条目无法证明在 09:00 后公开；不支持当窗候选，出现精确时刻时定点重开 |
| SRC-ANTHROPIC | Research 历史目录；定点检查本窗及 05-07 相邻条目 | 已检查 | Natural Language Autoencoders 仅给 05-07 日期，无法证明在 09:00 后公开；不支持当窗候选 |
| SRC-GOOGLE-AI | DeepMind / Google Research Publications；有界检查本窗与相邻日期 | 受阻 | 历史列表日期粒度不足；仅隔离，不支持候选、Books 或零遗漏断言 |
| SRC-META-AI | Meta / FAIR Publications；本窗可见日期与 arXiv family 交叉去重 | 已检查 | 未恢复独立当窗事件；动态目录只支持可见范围 |
| SRC-QWEN | Qwen Blog / Research；定点检查 05-07 条目 | 已检查 | 05-07 产品更新仅给日期且机制未披露；不支持截点归属或机制结论 |
| SRC-DEEPSEEK | 官网与公开 Research 入口 | 受阻 | 缺可分页历史日级研究目录；出现官方日级索引或可核实条目时定点重开 |
| SRC-MOONSHOT | Kimi / MoonshotAI 官方研究与博客入口 | 已检查 | 本窗未见可唯一归属的独立研究事件 |
| SRC-TENCENT-HUNYUAN | Hunyuan Research“全部”列表；检查本窗及相邻条目 | 已检查 | 相邻可核实条目为 04-30 与 05-21 |
| SRC-ZAI | 智谱 Research 列表；检查本窗及相邻条目 | 已检查 | 相邻可核实条目为 04-29 与 05-20 |
| SRC-BYTEDANCE-SEED | Seed Research / Publications；检查本窗及相邻条目 | 已检查 | 相邻可核实条目为 04-26 与 05-16；AI for Science 暂缓 |
| SRC-BAIDU-ERNIE | ERNIE 技术博客；检查本窗及相邻条目 | 已检查 | 相邻可核实条目为 04-30 与 05-09 |
| SRC-XIAOMI-MIMO | MiMo Papers / Blog；检查本窗可见日级条目 | 受阻 | Blog 历史日期粒度不足；不支持候选或零遗漏断言 |
| SRC-MINIMAX | MiniMax Research / Blog / News；检查本窗及相邻条目 | 已检查 | 本窗未见可核实独立研究事件；部分卡片缺稳定日级时间 |
| SRC-ARXIV | official Wednesday 20:00 ET announcement batch；619 个 identity 依照三信号规则复核 | 已检查 | 当前作者快照为 184 个已审阅候选与 435 个 closure；18 项限定返修及 15 项 root 写回完成，仅待新的非作者 post-write review |

逐 family 候选终态见 [`V3_RECERTIFICATION.json`](../_sources/daily-20260508/V3_RECERTIFICATION.json)；日期三信号及 619/195 分组见 [`ARXIV_OWNER_RECONCILIATION_V3.md`](../_sources/daily-20260508/ARXIV_OWNER_RECONCILIATION_V3.md)，统一批次规则见 [`ARXIV_ANNOUNCEMENT_PROVENANCE.md`](../_sources/ARXIV_ANNOUNCEMENT_PROVENANCE.md)。旧 owner receipt 只保留身份、摘要与原始时间信号，不再独立代表当前 owner 或准入判断。

## 3. 候选与判断

三项分数依次为 `Design Delta + System Reach + Durability = Total`；公开时间统一是本批次官方公告时刻。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [SAT: Sequential Agent Tuning for Coordinator Free Plug and Play Multi-LLM Training with Monotonic Improvement Guarantees](https://arxiv.org/html/2605.05216v1) | 2026-05-08T08:00:00+08:00 | multi-Agent 顺序更新的 occupancy 与 trust-region contract；2+2+3=7 | 深入完成 | 整合：AGENT-MULTI-AGENT [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [Sparse Prefix Caching for Hybrid and Recurrent LLM Serving](https://arxiv.org/html/2605.05219v1) | 2026-05-08T08:00:00+08:00 | durable AI System mechanism, ownership, evaluation or execution-contract delta；2+2+2=6 | 深入完成 | 整合：INFER-KV-CACHE [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Adaptive Computation Depth via Learned Token Routing in Transformers](https://arxiv.org/html/2605.05222v1) | 2026-05-08T08:00:00+08:00 | durable AI System mechanism, ownership, evaluation or execution-contract delta；2+1+2=5 | 标准完成 | 已有覆盖：INFER-SCHEDULING [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Structural Instability of Feature Composition](https://arxiv.org/html/2605.05223v1) | 2026-05-08T08:00:00+08:00 | 非正交 feature 组合干预的结构性坍塌；2+1+3=6 | 深入完成 | 整合：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md) |
| [Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods](https://arxiv.org/html/2605.05227v1) | 2026-05-08T08:00:00+08:00 | checkpoint-coupled 在线数据重加权；2+2+2=6 | 深入完成 | 整合：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction](https://arxiv.org/html/2605.05242v1) | 2026-05-08T08:00:00+08:00 | direct corpus interaction raises interface resolution with composable search/read operations, while moving index cost into agent steps, context management and permission risk.；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-CONTEXT [章节](../../../../books/part-07-agent/75-context.md) |
| [Towards Dependable Retrieval-Augmented Generation Using Factual Confidence Prediction](https://arxiv.org/html/2605.05244v1) | 2026-05-08T08:00:00+08:00 | RAG confidence must distinguish retrieval support, claim entailment and answer uncertainty instead of using generation probability as evidence confidence.；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-RAG [章节](../../../../books/part-07-agent/76-rag.md) |
| [DADL: A Declarative Description Language for Enterprise Tool Libraries in LLM Agent Systems](https://arxiv.org/html/2605.05247v1) | 2026-05-08T08:00:00+08:00 | A declarative tool language can compile schemas into deterministic validation and adapters; runtime authorization and effect commit remain separate authorities.；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING [章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [SecureMCP: A Policy-Enforced LLM Data Access Framework for AIoT Systems via Model Context Protocol](https://arxiv.org/html/2605.05260v1) | 2026-05-08T08:00:00+08:00 | MCP data access must be policy-enforced at the effect boundary rather than delegated to model intent；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-MCP [章节](../../../../books/part-07-agent/83-mcp.md) |
| [Maximizing Rollout Informativeness under a Fixed Budget: A Submodular View of Tree Search for Tool-Use Agentic Reinforcement Learning](https://arxiv.org/html/2605.05262v1) | 2026-05-08T08:00:00+08:00 | tool-use rollout selection should optimize marginal information under a budget rather than expand a search tree uniformly；2+2+2=6 | 深入完成 | 整合：AGENT-PLANNING [章节](../../../../books/part-07-agent/79-planning.md) |
| [Sealing the Audit-Runtime Gap for LLM Skills](https://arxiv.org/html/2605.05274v1) | 2026-05-08T08:00:00+08:00 | LLM skills require a sealed audit-to-runtime identity so the reviewed artifact is the artifact actually executed；3+2+3=8 | 深入完成 | 整合：AGENT-PLATFORM [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [Securing the Agent: Vendor-Neutral, Multitenant Enterprise Retrieval and Tool Use](https://arxiv.org/html/2605.05287v1) | 2026-05-08T08:00:00+08:00 | enterprise agent retrieval and tool use require tenant-scoped identity and effect authorization；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Partial Evidence Bench: Benchmarking Authorization-Limited Evidence in Agentic Systems](https://arxiv.org/html/2605.05379v1) | 2026-05-08T08:00:00+08:00 | agent evaluation must model authorization-limited evidence rather than assume universal access to ground truth；3+2+3=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [From History to State: Constant-Context Skill Learning for LLM Agents](https://arxiv.org/html/2605.05413v1) | 2026-05-08T08:00:00+08:00 | recurring procedures can move from growing prompts into learned modules while deterministic workflow state remains explicit；2+2+2=6 | 深入完成 | 整合：AGENT-WORKFLOW [章节](../../../../books/part-07-agent/81-workflow.md) |
| [Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure](https://arxiv.org/html/2605.05440v1) | 2026-05-08T08:00:00+08:00 | authorization must propagate through delegation, aggregation and time, not attach only to the initiating identity；2+3+3=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Nitsum: Serving Tiered LLM Requests with Adaptive Tensor Parallelism](https://arxiv.org/html/2605.05467v1) | 2026-05-08T08:00:00+08:00 | tensor parallelism can become a runtime control surface jointly optimized with PD split and request scheduling；3+3+2=8 | 深入完成 | 整合：INFER-SCHEDULING [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [WAAA! Web Adversaries Against Agentic Browsers](https://arxiv.org/html/2605.05509v1) | 2026-05-08T08:00:00+08:00 | agentic-browser threat models must include ordinary web attacks and confused-deputy effects, not only prompt injection；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [OpenG2G: A Simulation Platform for AI Datacenter-Grid Runtime Coordination](https://arxiv.org/html/2605.05519v1) | 2026-05-08T08:00:00+08:00 | datacenter workload control and grid response form one closed-loop runtime coordination problem；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-COST [章节](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [Accelerating MoE with Dynamic In-Switch Computing on Multi-GPUs](https://arxiv.org/html/2605.05607v1) | 2026-05-08T08:00:00+08:00 | 1) Dynamic multimem addressing co-designs ISA, architecture, and runtime, as a dynamic extension to…；2+2+2=6 | 深入完成 | 整合：TRAIN-TENSOR-PARALLEL [章节](../../../../books/part-04-training-system/37-tensor-parallel.md) |
| [Towards Compute-Aware In-Switch Computing for LLMs Tensor-Parallelism on Multi-GPU Systems](https://arxiv.org/html/2605.05628v1) | 2026-05-08T08:00:00+08:00 | While in-switch computing, exemplified by NVLink SHARP (NVLS), accelerates collective operations by reducing redundant data transfer, its communication-centric design philosophy introduces the mismatch between its communication mode and the memory semantic requirement of LLM's computation kernel.；3+2+2=7 | 深入完成 | 整合：TRAIN-TENSOR-PARALLEL [章节](../../../../books/part-04-training-system/37-tensor-parallel.md) |
| [Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization](https://arxiv.org/html/2605.05683v1) | 2026-05-08T08:00:00+08:00 | activation/gradient spectrum 训练诊断；2+1+2=5 | 深入完成 | 整合：TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [DataDignity: Training Data Attribution for Large Language Models](https://arxiv.org/html/2605.05687v1) | 2026-05-08T08:00:00+08:00 | given a prompt, a target-model response, and a candidate corpus, rank the documents that best support the response.；2+1+2=5 | 标准完成 | 已有覆盖：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [Irminsul: MLA-Native Position-Independent Caching for Agentic LLM Serving](https://arxiv.org/html/2605.05696v1) | 2026-05-08T08:00:00+08:00 | We present Irminsul, which extends SGLang's radix cache with content-hash keying over CDC-chunked segments and a $δ$-rotation rule for $k_r$.；2+2+2=6 | 标准完成 | 已有覆盖：INFER-KV-CACHE [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Budgeted Attention Allocation: Cost-Conditioned Compute Control for Efficient Transformers](https://arxiv.org/html/2605.05697v1) | 2026-05-08T08:00:00+08:00 | 单 checkpoint 的 budget-conditioned head gate 把请求预算映射为 hard compute mask；3+2+2=7 | 深入完成 | 整合：MODEL-SELF-ATTENTION [章节](../../../../books/part-02-model/14-self-attention.md) |
| [When Quantization Is Free: An int4 KV Cache That Outruns fp16 on Apple Silicon](https://arxiv.org/html/2605.05699v1) | 2026-05-08T08:00:00+08:00 | a single fused Metal kernel (sign-randomized FFT $+$ per-channel $λ$ $+$ per-group abs-max $+$ int4 nibble pack), exposed as a HuggingFace \texttt{Cache} subclass, runs \emph{faster than fp16} across…；2+1+2=5 | 标准完成 | 已有覆盖：INFER-KV-CACHE [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Inference-Time Budget Control for LLM Search Agents](https://arxiv.org/html/2605.05701v1) | 2026-05-08T08:00:00+08:00 | tool/token 双预算下的 VOI action selection 与 typed finalizer；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-PLANNING [章节](../../../../books/part-07-agent/79-planning.md) |
| [On the Blessing of Pre-training in Weak-to-Strong Generalization](https://arxiv.org/html/2605.05710v1) | 2026-05-08T08:00:00+08:00 | pretraining 作为受限 spectral warm start；2+1+3=6 | 标准完成 | 已有覆盖：TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [More Is Not Always Better: Cross-Component Interference in LLM Agent Scaffolding](https://arxiv.org/html/2605.05716v1) | 2026-05-08T08:00:00+08:00 | degradation when components interact destructively.；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-PLATFORM [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [Auto Research with Specialist Agents Develops Effective and Non-Trivial Training Recipes](https://arxiv.org/html/2605.05724v1) | 2026-05-08T08:00:00+08:00 | We study auto research as a closed empirical loop driven by external measurement.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Transformers Provably Implement In-Context Reinforcement Learning with Policy Improvement](https://arxiv.org/html/2605.05755v1) | 2026-05-08T08:00:00+08:00 | linear attention 的 in-context RL 可表达性边界；2+1+3=6 | 标准完成 | 已有覆盖：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md) |
| [Revealing Modular Gradient Noise Imbalance in LLMs: Calibrating Adam via Signal-to-Noise Ratio](https://arxiv.org/html/2605.05794v1) | 2026-05-08T08:00:00+08:00 | To establish a more principled approach, we first analyze the noise-damping behavior of Adam in high-noise modules and introduce \textbf{Module-wise Learning Rate Scaling via SNR (MoLS)}.；2+1+2=5 | 深入完成 | 整合：TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [Selective Rollout: Mid-Trajectory Termination for Multi-Sample Agent RL](https://arxiv.org/html/2605.05802v1) | 2026-05-08T08:00:00+08:00 | 用组内 prefix divergence 决定 GRPO group 的 mid-rollout early termination；3+2+2=7 | 深入完成 | 整合：TRAIN-GRPO [章节](../../../../books/part-04-training-system/33-grpo.md) |
| [HCInfer: An Efficient Inference System via Error Compensation for Resource-Constrained Devices](https://arxiv.org/html/2605.05819v1) | 2026-05-08T08:00:00+08:00 | Motivated by this opportunity, we propose HCInfer, a heterogeneous inference system that offloads residual compensation to the CPU while executing the compressed backbone on the GPU, and further introduces an asynchronous compensation pipeline and sensitivity-aware dynamic rank allocation…；2+2+2=6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Evaluation Awareness in Language Models Has Limited Effect on Behaviour](https://arxiv.org/html/2605.05835v1) | 2026-05-08T08:00:00+08:00 | evaluation awareness 的负面/非充分证据；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SkillScope: Toward Fine-Grained Least-Privilege Enforcement for Agent Skills](https://arxiv.org/html/2605.05868v1) | 2026-05-08T08:00:00+08:00 | In this paper, we present SkillScope, a framework for fine-grained least-privilege enforcement in Agent Skills.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [CITE: Anytime-Valid Statistical Inference in LLM Self-Consistency](https://arxiv.org/html/2605.05873v1) | 2026-05-08T08:00:00+08:00 | 任意停止下的 response-mode certificate；3+1+3=7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MoE-Hub: Taming Software Complexity for Seamless MoE Overlap with Hardware-Accelerated Communication on Multi-GPU Systems](https://arxiv.org/html/2605.05888v1) | 2026-05-08T08:00:00+08:00 | MoE destination-agnostic communication hub；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-TENSOR-PARALLEL [章节](../../../../books/part-04-training-system/37-tensor-parallel.md) |
| [VisMMOE: Exploiting Visual-Expert Affinity for Efficient Visual-Language MoE Offloading](https://arxiv.org/html/2605.05899v1) | 2026-05-08T08:00:00+08:00 | visual-token compression 改变 expert working-set、cache 与 prefetch plan；3+3+2=8 | 深入完成 | 整合：INFER-TENSORRT-LLM [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Near-Policy: Accelerating On-Policy Distillation via Asynchronous Generation and Selective Packing](https://arxiv.org/html/2605.05940v1) | 2026-05-08T08:00:00+08:00 | 异步 distillation 的 policy-lag gate；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md) |
| [HaM-World: Soft-Hamiltonian World Models with Selective Memory for Planning](https://arxiv.org/html/2605.05951v1) | 2026-05-08T08:00:00+08:00 | 结构化动力学与 selective memory world state；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Towards Reliable LLM Evaluation: Correcting the Winner's Curse in Adaptive Benchmarking](https://arxiv.org/html/2605.05973v1) | 2026-05-08T08:00:00+08:00 | We study inference for this procedure-level target under explicit tuning budgets.；3+2+3=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Requests of a Feather Must Flock Together: Batch Size vs. Prefix Homogeneity in LLM Inference](https://arxiv.org/html/2605.06046v1) | 2026-05-08T08:00:00+08:00 | prefix homogeneity 与 batch-size 反转；3+2+2=7 | 深入完成 | 整合：INFER-SCHEDULING [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Towards Generation-Efficient Uncertainty Estimation in Large Language Models](https://arxiv.org/html/2605.06053v1) | 2026-05-08T08:00:00+08:00 | partial/input-only uncertainty estimator 前移观测时点并减少生成成本；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Normalized Architectures are Natively 4-Bit](https://arxiv.org/html/2605.06067v1) | 2026-05-08T08:00:00+08:00 | hypersphere-normalized geometry 与 NVFP4 的 architecture–precision 共设计；3+3+3=9 | 深入完成 | 整合：TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [VibeServe: Can AI Agents Build Bespoke LLM Serving Systems?](https://arxiv.org/html/2605.06068v1) | 2026-05-08T08:00:00+08:00 | We propose VibeServe, the first agentic loop that generates entire LLM serving stacks end-to-end.；1+2+2=5 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training](https://arxiv.org/html/2605.06076v1) | 2026-05-08T08:00:00+08:00 | post-training 后 mechanistic localization 漂移；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Shallow Prefill, Deep Decoding: Efficient Long-Context Inference via Layer-Asymmetric KV Visibility](https://arxiv.org/html/2605.06105v1) | 2026-05-08T08:00:00+08:00 | We introduce \emph{Shallow Prefill, dEEp Decode} (SPEED), a phase-asymmetric KV-visibility policy that materializes non-anchor prompt-token KV states only in lower layers while keeping Decode-phase tokens full-depth.；2+2+2=6 | 标准完成 | 已有覆盖：INFER-PREFILL [章节](../../../../books/part-05-inference-system/43-prefill.md) |
| [Policy-Guided Stepwise Model Routing for Cost-Effective Reasoning](https://arxiv.org/html/2605.06116v1) | 2026-05-08T08:00:00+08:00 | CMDP 在每个 reasoning step 路由模型并校准成本/正确性 threshold；3+2+2=7 | 深入完成 | 已有覆盖：INFER-SCHEDULING [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Breaking, Stale, or Missing? Benchmarking Coding Agents on Project-Level Test Evolution](https://arxiv.org/html/2605.06125v1) | 2026-05-08T08:00:00+08:00 | 测试演化拆为 breaking、stale、missing，修正“tests pass 即 coverage 有效”；3+2+2=7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [BUILD-AND-FIND: An Effort-Aware Protocol for Evaluating Agent-Managed Codebases](https://arxiv.org/html/2605.06136v1) | 2026-05-08T08:00:00+08:00 | Even when strong agents nearly satisfy the visible behavioral objective, repositories can differ in how clearly they expose the intended behavior and design choices behind that behavior.；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Stateful Agent Backdoor](https://arxiv.org/html/2605.06158v1) | 2026-05-08T08:00:00+08:00 | 持久 R/W 组件让跨 session sub-backdoor 组成 Mealy machine；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges](https://arxiv.org/html/2605.06161v1) | 2026-05-08T08:00:00+08:00 | LLM-as-a-Judge pipelines have become the de facto evaluator for agent safety, yet existing benchmarks treat their verdicts as ground-truth proxies without checking whether the verdicts depend on the agent's behavior or merely on how the evaluation policy happens…；3+2+3=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ClawGuard: Out-of-Band Detection of LLM Agent Workflow Hijacking via EM Side Channel](https://arxiv.org/html/2605.06205v1) | 2026-05-08T08:00:00+08:00 | host 外 EM/temperature side channel 形成独立 evidence plane；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Federation of Experts: Communication Efficient Distributed Inference for Large Language Models](https://arxiv.org/html/2605.06206v1) | 2026-05-08T08:00:00+08:00 | 按 expert/KV-head group 改写通信图，以组内 all-to-all + 组间 all-reduce 替代全局 all-to-all；3+3+3=9 | 深入完成 | 整合：MODEL-MOE [章节](../../../../books/part-02-model/21-moe.md) |
| [UniPrefill: Universal Long-Context Prefill Acceleration via Block-wise Dynamic Sparsification](https://arxiv.org/html/2605.06221v1) | 2026-05-08T08:00:00+08:00 | To this end, we propose UniPrefill, a prefill acceleration framework applicable to virtually any model architecture, which directly accelerates the model's computation at the token level.；2+2+2=6 | 标准完成 | 已有覆盖：INFER-PREFILL [章节](../../../../books/part-05-inference-system/43-prefill.md) |
| [Correct Code, Vulnerable Dependencies: A Large Scale Measurement Study of LLM-Specified Library Versions](https://arxiv.org/html/2605.06279v1) | 2026-05-08T08:00:00+08:00 | dependency pin 需要独立的漏洞、安装、类型与运行验收；2+3+3=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Measuring Evaluation-Context Divergence in Open-Weight LLMs: A Paired-Prompt Protocol with Pilot Evidence of Alignment-Pipeline-Specific Heterogeneity](https://arxiv.org/html/2605.06327v1) | 2026-05-08T08:00:00+08:00 | We define evaluation-context divergence as an observable within-item change in behavior induced by framing a fixed task as an evaluation, a live deployment interaction, or a neutral request, and present a paired-prompt protocol that measures it in open-weight…；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MANTRA: Synthesizing SMT-Validated Compliance Benchmarks for Tool-Using LLM Agents](https://arxiv.org/html/2605.06334v1) | 2026-05-08T08:00:00+08:00 | manual/tool schema 到 symbolic world model、trace checks 与 SMT consistency/repair 的机器可检验评测链；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [A Regime Theory of Controller Class Selection for LLM Action Decisions](https://arxiv.org/html/2605.06339v1) | 2026-05-08T08:00:00+08:00 | residual signal、样本量与 partition geometry 决定 controller class 是否可辨识；2+2+2=6 | 标准完成 | 已有覆盖：INFER-SCHEDULING [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Is Escalation Worth It? A Decision-Theoretic Characterization of LLM Cascades](https://arxiv.org/html/2605.06350v1) | 2026-05-08T08:00:00+08:00 | post-generation cascade 与 pre-generation router 具有不同累计成本结构；3+3+3=9 | 深入完成 | 整合：INFER-SCHEDULING [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [From Agent Loops to Deterministic Graphs: Execution Lineage for Reproducible AI-Native Work](https://arxiv.org/html/2605.06365v1) | 2026-05-08T08:00:00+08:00 | an execution model in which AI-native work is represented as a directed acyclic graph (DAG) of artifact-producing computations with explicit dependencies, stable intermediate boundaries, and identity-based replay.；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-WORKFLOW [章节](../../../../books/part-07-agent/81-workflow.md) |
| [Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](https://arxiv.org/html/2605.06388v1) | 2026-05-08T08:00:00+08:00 | reconstruction 与 semantic latent 在 visual fidelity、action recoverability 和 policy relevance 上排序不同；3+2+3=8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Constraining Host-Level Abuse in Self-Hosted Computer-Use Agents via TEE-Backed Isolation](https://arxiv.org/html/2605.06393v1) | 2026-05-08T08:00:00+08:00 | The proposed design keeps ordinary functionality on the constrained REE path, while protecting security-critical classification, authorization, binding, evidence generation, and selected execution-control decisions inside a cloud-native TEE-backed trusted operation plane.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SparseForge: Efficient Semi-Structured LLM Sparsification via Annealing of Hessian-Guided Soft-Mask](https://arxiv.org/html/2605.06402v1) | 2026-05-08T08:00:00+08:00 | Hessian-guided soft-mask annealing 收敛到硬件可执行 2:4 structure；3+2+3=8 | 深入完成 | 整合：INFER-TENSORRT-LLM [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Constraint Decay: The Fragility of LLM Agents in Backend Code Generation](https://arxiv.org/html/2605.06445v1) | 2026-05-08T08:00:00+08:00 | behavioral tests 与 architecture/database/ORM structural verifier 联合验收；2+2+3=7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [PrefixGuard: From LLM-Agent Traces to Online Failure-Warning Monitors](https://arxiv.org/html/2605.06455v1) | 2026-05-08T08:00:00+08:00 | We introduce PrefixGuard, a trace-to-monitor framework with an offline StepView induction step followed by supervised monitor training.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-MONITORING [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Beyond Task Success: Measuring Workflow Fidelity in LLM-Based Agentic Payment Systems](https://arxiv.org/pdf/2605.06457v1.pdf) | 2026-05-08T08:00:00+08:00 | transition precision/recall 揭示 task success 与 handoff set 隐藏的 checkpoint skip；2+2+3=7 | 深入完成 | 已有覆盖：AGENT-WORKFLOW [章节](../../../../books/part-07-agent/81-workflow.md) |
| [Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management](https://arxiv.org/html/2605.06472v1) | 2026-05-08T08:00:00+08:00 | Experiments on three workflow benchmarks show that PBKV achieves up to $1.85\times$ speedup over LRU on dynamic workflows, and up to $1.26\times$ speedup over the SOTA baseline KVFlow on the static workflow.；2+2+2=6 | 标准完成 | 已有覆盖：INFER-KV-CACHE [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation](https://arxiv.org/html/2605.06481v1) | 2026-05-08T08:00:00+08:00 | persistent object address 与 mutable content/next state 分离；3+2+3=8 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors](https://arxiv.org/html/2605.06490v1) | 2026-05-08T08:00:00+08:00 | deterministic environment state 分离任务完成与 policy-violating shortcut；2+2+3=7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [On the Implicit Reward Overfitting and the Low-rank Dynamics in RLVR](https://arxiv.org/html/2605.06523v1) | 2026-05-08T08:00:00+08:00 | rank-1 substitution 暴露 train reward 与 test generalization 分离，并把 spectral dynamics 作为受限诊断；2+1+2=5 | 标准完成 | 已有覆盖：TRAIN-GRPO [章节](../../../../books/part-04-training-system/33-grpo.md) |
| [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/html/2605.06527v1) | 2026-05-08T08:00:00+08:00 | To rigorously evaluate this capability, we introduce STALE, a benchmark of 400 expert-validated conflict scenarios (1,200 evaluation queries across three probing dimensions) spanning over 100 everyday topics with contexts up to 150K tokens.；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-MEMORY [章节](../../../../books/part-07-agent/77-memory.md) |
| [CCL-Bench 1.0: A Trace-Based Benchmark for LLM Infrastructure](https://arxiv.org/html/2605.06544v1) | 2026-05-08T08:00:00+08:00 | We present CCL-Bench, a trace-based benchmark that addresses the limitations of existing benchmarks by recording reusable evidence for every ML workload.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Long Context Pre-Training with Lighthouse Attention](https://arxiv.org/html/2605.06554v1) | 2026-05-08T08:00:00+08:00 | training-only multi-resolution attention 通过末期 dense SDPA recovery 生成部署 artifact；3+3+3=9 | 深入完成 | 整合：TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [The Structural Origin of Attention Sink: Variance Discrepancy, Super Neurons, and Dimension Disparity](https://arxiv.org/html/2605.06611v1) | 2026-05-08T08:00:00+08:00 | attention sink 的结构性条件机制；3+1+3=7 | 深入完成 | 整合：MODEL-LONG-CONTEXT [章节](../../../../books/part-02-model/22-long-context.md) |
| [SkillOS: Learning Skill Curation for Self-Evolving Agents](https://arxiv.org/html/2605.06614v1) | 2026-05-08T08:00:00+08:00 | frozen executor、RL curator 与 external SkillRepo 分离长期 skill state；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-MEMORY [章节](../../../../books/part-07-agent/77-memory.md) |
| [Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents](https://arxiv.org/html/2605.06635v1) | 2026-05-08T08:00:00+08:00 | We introduce the first source attribution evaluation framework that uses a reproducible AST parser to extract and evaluate inline citations from LLM-generated Markdown reports at scale.；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Recursive Agent Optimization](https://arxiv.org/html/2605.06639v1) | 2026-05-08T08:00:00+08:00 | shared policy 学习何时递归委派、如何写 subtask 与 aggregate；3+3+3=9 | 深入完成 | 整合：AGENT-MULTI-AGENT [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [When No Benchmark Exists: Validating Comparative LLM Safety Scoring Without Ground-Truth Labels](https://arxiv.org/html/2605.06652v1) | 2026-05-08T08:00:00+08:00 | 无标签时以 known contrast、target sensitivity 与 rerun stability 验证 measurement instrument；3+3+3=9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Optimizer-Model Consistency: Full Finetuning with the Same Optimizer as Pretraining Forgets Less](https://arxiv.org/html/2605.06654v1) | 2026-05-08T08:00:00+08:00 | pretraining/SFT optimizer lineage 与遗忘；2+1+2=5 | 深入完成 | 整合：TRAIN-SFT [章节](../../../../books/part-04-training-system/29-sft.md) |
| [Why Global LLM Leaderboards Are Misleading: Small Portfolios for Heterogeneous Supervised ML](https://arxiv.org/html/2605.06656v1) | 2026-05-08T08:00:00+08:00 | global leaderboard 的 subgroup cancellation；3+2+3=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [UniPool: A Globally Shared Expert Pool for Mixture-of-Experts](https://arxiv.org/html/2605.06665v1) | 2026-05-08T08:00:00+08:00 | Motivated by this redundancy, we propose UniPool, an MoE architecture that treats expert capacity as a global architectural budget by replacing per-layer expert ownership with a single shared pool accessed by independent per-layer routers.；2+2+2=6 | 标准完成 | 已有覆盖：MODEL-MOE [章节](../../../../books/part-02-model/21-moe.md) |
| [PARNESS: A Paper Harness for End-to-End Automated Scientific Research with Dynamic Workflows, Full-Text Indexing, and Cross-Run Knowledge Accumulation](https://arxiv.org/html/2605.05258v1) | 2026-05-08T08:00:00+08:00 | editable YAML DAG、typed Agent/verifier contract 与跨运行 knowledge state；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW [章节](../../../../books/part-07-agent/81-workflow.md) |
| [ZAYA1-8B Technical Report](https://arxiv.org/html/2605.05365v1) | 2026-05-08T08:00:00+08:00 | bounded-tail Markovian reasoning state、batched stages 与 rollout/trainer consistency；3+3+2=8 | 深入完成 | 整合：INFER-SCHEDULING [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)；状态：已写回 |
| [Weight-Decay Turns Transformer Loss Landscapes Villani: Functional-Analytic Foundations for Optimization and Generalization](https://arxiv.org/html/2605.06599v1) | 2026-05-08T08:00:00+08:00 | weight decay 的 coercive geometry 与 functional-inequality 条件边界；2+2+3=7 | 深入完成 | 已有覆盖：TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [When and Why SignSGD Outperforms SGD: A Theoretical Study Based on ell-1-norm Lower Bounds](https://arxiv.org/html/2605.06615v1) | 2026-05-08T08:00:00+08:00 | optimizer 选择绑定 ell-infinity geometry 与 separable sparse-noise regime；3+2+3=8 | 深入完成 | 整合：TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md)；状态：已写回 |
| [StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction](https://arxiv.org/html/2605.06642v1) | 2026-05-08T08:00:00+08:00 | explicit strategy state 与 strategy/action 两层 credit group；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [章节](../../../../books/part-04-training-system/33-grpo.md)；状态：已写回 |
| [Beyond Negative Rollouts: Positive-Only Policy Optimization with Implicit Negative Gradients](https://arxiv.org/html/2605.06650v1) | 2026-05-08T08:00:00+08:00 | positive-set bounded importance、implicit negative gradients 与 EMA anchor；3+2+2=7 | 深入完成 | 整合：TRAIN-GRPO [章节](../../../../books/part-04-training-system/33-grpo.md)；状态：已写回 |
| [The Cost of Context: Mitigating Textual Bias in Multimodal Retrieval-Augmented Generation](https://arxiv.org/html/2605.05594v1) | 2026-05-08T08:00:00+08:00 | oracle 文本可压制视觉 attention mass/sharpness 并 recorrupt 正确答案；3+2+2=7 | 深入完成 | 整合：AGENT-RAG [章节](../../../../books/part-07-agent/76-rag.md)；状态：已写回 |
| [Retrieval-Conditioned Topology Selection with Provable Budget Conservation for Multi-Agent Code Generation](https://arxiv.org/html/2605.05657v1) | 2026-05-08T08:00:00+08:00 | code structure 驱动 topology selection，并在执行前验证资源预算守恒；3+2+3=8 | 深入完成 | 整合：AGENT-MULTI-AGENT [章节](../../../../books/part-07-agent/82-multi-agent.md)；状态：已写回 |
| [An Empirical Study of Proactive Coding Assistants in Real-World Software Development](https://arxiv.org/html/2605.05700v1) | 2026-05-08T08:00:00+08:00 | 真实 IDE trace 揭示 simulation-only Agent evaluation 的外推失效；2+2+3=7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LeakDojo: Decoding the Leakage Threats of RAG Systems](https://arxiv.org/html/2605.05818v1) | 2026-05-08T08:00:00+08:00 | modular、stateful RAG extraction 暴露 faithfulness 与 confidentiality 冲突；3+2+3=8 | 深入完成 | 整合：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；状态：已写回 |
| [MDN: Parallelizing Stepwise Momentum for Delta Linear Attention](https://arxiv.org/html/2605.05838v1) | 2026-05-08T08:00:00+08:00 | 二阶 momentum recurrence 对齐 chunk-parallel training 与 recurrent decode；3+2+3=8 | 深入完成 | 整合：MODEL-LONG-CONTEXT [章节](../../../../books/part-02-model/22-long-context.md)；状态：已写回 |
| [Quantizing With Randomized Hadamard Transforms: Efficient Heuristic Now Proven](https://arxiv.org/html/2605.06014v1) | 2026-05-08T08:00:00+08:00 | scalar 与 block quantizer 需要不同 RHT 分布保证与自适应 transform count；3+3+3=9 | 深入完成 | 整合：INFER-TENSORRT-LLM [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；状态：已写回 |
| [Toward Visually Realistic Simulation: A Benchmark for Evaluating Robot Manipulation in Simulation](https://arxiv.org/html/2605.06311v1) | 2026-05-08T08:00:00+08:00 | lighting/material realism 是 embodied sim-to-real evaluation contract 的一部分；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Teaching Thinking Models to Reason with Tools: A Full-Pipeline Recipe for Tool-Integrated Reasoning](https://arxiv.org/html/2605.06326v1) | 2026-05-08T08:00:00+08:00 | tool-suited trajectory admission、mixture、checkpoint 与 SFT→RLVR handoff；3+2+3=8 | 深入完成 | 整合：TRAIN-SFT [章节](../../../../books/part-04-training-system/29-sft.md)；状态：已写回 |
| [Task-Aware Answer Preservation under Audio Compression for Large Audio Language Models](https://arxiv.org/html/2605.06631v1) | 2026-05-08T08:00:00+08:00 | worst-family excess answer error 与统计置信区间约束 compression release；3+2+3=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；状态：已写回 |

| [Decision-aware User Simulation Agent for Evaluating Conversational Recommender Systems](https://arxiv.org/html/2605.05250v1) | 2026-05-08T08:00:00+08:00 | 将 utility selection 与 overload-aware commitment 分开，修正 user-simulator fidelity 与 acceptance measurement；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SOCpilot: Verifying Policy Compliance for LLM-Assisted Incident Response](https://arxiv.org/html/2605.05501v1) | 2026-05-08T08:00:00+08:00 | 模型只提出 typed plan，外置 deterministic verifier 持有 catalog、policy 与 approval authority；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Chain of Risk: Safety Failures in Large Reasoning Models and Mitigation via Adaptive Multi-Principle Steering](https://arxiv.org/html/2605.05678v1) | 2026-05-08T08:00:00+08:00 | reasoning 与 answer 必须分阶段测量，visible trace 不能冒充内部 faithful computation；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes](https://arxiv.org/html/2605.05715v1) | 2026-05-08T08:00:00+08:00 | hidden-state failure signal 可解码不等于 intervention 有效，probe 只可支持校准后的 abstention；3+2+3=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；状态：已落实 |
| [RVPO: Risk-Sensitive Alignment via Variance Regularization](https://arxiv.org/html/2605.05750v1) | 2026-05-08T08:00:00+08:00 | reward 均值会掩盖 must-have bottleneck，SoftMin 是带噪声与 schedule 风险的条件分支；3+2+2=7 | 深入完成 | 整合：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md)；状态：已落实 |
| [Optimal Transport for LLM Reward Modeling from Noisy Preference](https://arxiv.org/html/2605.06036v1) | 2026-05-08T08:00:00+08:00 | partial OT 允许拒绝 noisy preference mass，但依赖 clean-more-consistent 前提并引入二次成本；2+2+2=6 | 深入完成 | 整合：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md)；状态：已落实 |
| [Milestone-Guided Policy Learning for Long-Horizon Language Agents](https://arxiv.org/html/2605.06078v1) | 2026-05-08T08:00:00+08:00 | milestone credit 位于 terminal reward 与逐 action causal credit 之间，boundary 必须由环境冻结；3+2+2=7 | 深入完成 | 整合：TRAIN-GRPO [章节](../../../../books/part-04-training-system/33-grpo.md)；状态：已落实 |
| [A$^2$TGPO: Agentic Turn-Group Policy Optimization with Adaptive Turn-level Clipping](https://arxiv.org/html/2605.06200v1) | 2026-05-08T08:00:00+08:00 | `(prompt, turn-index)` normalization 是受限 comparison key，turn index 不等于真实 state equivalence；3+2+2=7 | 深入完成 | 整合：TRAIN-GRPO [章节](../../../../books/part-04-training-system/33-grpo.md)；状态：已落实 |
| [Measuring Black-Box Confidence via Reasoning Trajectories: Geometry, Coverage, and Verbalization](https://arxiv.org/html/2605.06308v1) | 2026-05-08T08:00:00+08:00 | confidence 应拆为 coverage、trajectory geometry 与 verbalization 等异质 sensor，并按风险校准；3+2+2=7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

| [Understanding Annotator Safety Policy with Interpretability](https://arxiv.org/html/2605.05329v1) | 2026-05-08T08:00:00+08:00 | 保存 annotator/policy identity 并区分 operational failure、policy ambiguity 与 value pluralism；3+2+3=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；状态：已落实并通过独立复核 |
| [ViTok-v2](https://arxiv.org/html/2605.05331v1) | 2026-05-08T08:00:00+08:00 | representation artifact 绑定 native-resolution policy、compression、decoder capacity 与 loss identity；3+2+3=8 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；状态：已落实并通过独立复核 |
| [BitCal-TTS](https://arxiv.org/html/2605.05561v1) | 2026-05-08T08:00:00+08:00 | precision 进入 halting sensor/controller identity；2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)；状态：已落实并通过独立复核 |
| [When Can Voting Help, Hurt, or Change Course?](https://arxiv.org/html/2605.05592v1) | 2026-05-08T08:00:00+08:00 | 异质样本下 voting curve 可非单调；3+2+3=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；状态：已落实并通过独立复核 |
| [Architecture Matters](https://arxiv.org/html/2605.05632v1) | 2026-05-08T08:00:00+08:00 | RAG architecture 改变 poisoning failure path；3+2+2=7 | 深入完成 | 整合：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；状态：已落实并通过独立复核 |
| [Text-Graph Synergy](https://arxiv.org/html/2605.05643v1) | 2026-05-08T08:00:00+08:00 | 双向校验与可恢复的 pruned graph state；2+2+2=6 | 深入完成 | 整合：AGENT-RAG [章节](../../../../books/part-07-agent/76-rag.md)；状态：已落实并通过独立复核 |
| [ReFlect](https://arxiv.org/html/2605.05737v1) | 2026-05-08T08:00:00+08:00 | deterministic harness 分离 error detection 与 recovery；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW [章节](../../../../books/part-07-agent/81-workflow.md) |
| [Adaptive Selection of LoRA Components](https://arxiv.org/html/2605.05769v1) | 2026-05-08T08:00:00+08:00 | DP federated LoRA 的逐层逐轮 component control；3+2+2=7 | 深入完成 | 整合：TRAIN-LORA [章节](../../../../books/part-04-training-system/30-lora.md)；状态：已落实并通过独立复核 |
| [Distribution-Aligned Adversarial Distillation](https://arxiv.org/html/2605.05777v1) | 2026-05-08T08:00:00+08:00 | 黑盒 uncertainty proxy 的 calibration/drift 边界；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LoopTrap](https://arxiv.org/html/2605.05846v1) | 2026-05-08T08:00:00+08:00 | context poisoning 可劫持 termination authority；3+3+3=9 | 深入完成 | 整合：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；状态：已落实并通过独立复核 |
| [Hallucination as an Anomaly](https://arxiv.org/html/2605.05953v1) | 2026-05-08T08:00:00+08:00 | anomaly sensor 与 correction authority 分离；3+2+2=7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；状态：已落实并通过独立复核 |
| [Selective Eligibility Traces for RLVR](https://arxiv.org/html/2605.05965v1) | 2026-05-08T08:00:00+08:00 | sparse token-credit artifact；3+2+2=7 | 深入完成 | 整合：TRAIN-GRPO [章节](../../../../books/part-04-training-system/33-grpo.md)；状态：已落实并通过独立复核 |
| [Schedule-and-Calibrate](https://arxiv.org/html/2605.06111v1) | 2026-05-08T08:00:00+08:00 | task utility 联合控制 curriculum 与 per-task KL；3+2+2=7 | 深入完成 | 整合：TRAIN-GRPO [章节](../../../../books/part-04-training-system/33-grpo.md)；状态：已落实并通过独立复核 |
| [DualSFT](https://arxiv.org/html/2605.06166v1) | 2026-05-08T08:00:00+08:00 | 共享 gradient matrix 联合 data/parameter selection；2+2+2=6 | 深入完成 | 整合：TRAIN-SFT [章节](../../../../books/part-04-training-system/29-sft.md)；状态：已落实并通过独立复核 |
| [OPSD Compresses What RLVR Teaches](https://arxiv.org/html/2605.06188v1) | 2026-05-08T08:00:00+08:00 | SFT→RLVR→OPSD 的条件化 compaction stage；3+2+3=8 | 深入完成 | 整合：TRAIN-GRPO [章节](../../../../books/part-04-training-system/33-grpo.md)；状态：已落实并通过独立复核 |
| [TIDE](https://arxiv.org/html/2605.06216v1) | 2026-05-08T08:00:00+08:00 | 逐层重注入 token identity；3+1+3=7 | 深入完成 | 整合：MODEL-EMBEDDING [章节](../../../../books/part-02-model/12-embedding.md)；状态：已落实并通过顺序复核 |
| [Joint Consistency](https://arxiv.org/html/2605.06219v1) | 2026-05-08T08:00:00+08:00 | independent fields 与 pairwise interaction 共同定义 aggregation；3+2+2=7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Profiling for Pennies](https://arxiv.org/html/2605.06232v1) | 2026-05-08T08:00:00+08:00 | search→inference→aggregation 的 derived privacy；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [LatentRAG](https://arxiv.org/html/2605.06285v1) | 2026-05-08T08:00:00+08:00 | latent query/retrieval 降 latency 但削弱可观察性；3+2+3=8 | 深入完成 | 整合：AGENT-RAG [章节](../../../../books/part-07-agent/76-rag.md)；状态：已落实并通过独立复核 |
| [Adaptive Task Graphs](https://arxiv.org/html/2605.06320v1) | 2026-05-08T08:00:00+08:00 | evolving coordination graph 拥有依赖、分配与进度；3+2+2=7 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [Pop Quiz Attack](https://arxiv.org/html/2605.06423v1) | 2026-05-08T08:00:00+08:00 | quiz-style black-box membership audit；3+2+2=7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Continuous Latent Diffusion Language Model](https://arxiv.org/pdf/2605.06548v1) | 2026-05-08T08:00:00+08:00 | global latent prior 与 local token realization 分层；3+2+3=8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；状态：已落实并通过顺序复核 |
| [FedAttr](https://arxiv.org/html/2605.06596v1) | 2026-05-08T08:00:00+08:00 | secure aggregation 下的 client attribution/leakage ledger；3+2+2=7 | 深入完成 | 整合：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；状态：已落实并通过独立复核 |
| [Transformers Efficiently Perform In-Context Logistic Regression via Normalized Gradient Descent](https://arxiv.org/html/2605.06609v1) | 2026-05-08T08:00:00+08:00 | 受限构造中每层执行一次 normalized-gradient update；3+2+3=8 | 深入完成 | 整合：MODEL-TRANSFORMER-LAYER [章节](../../../../books/part-02-model/17-transformer-layer.md)；状态：已落实并通过独立复核 |
| [Crafting Reversible SFT Behaviors](https://arxiv.org/html/2605.06632v1) | 2026-05-08T08:00:00+08:00 | sparse causal carrier 与 reversible SFT control；3+2+2=7 | 深入完成 | 整合：TRAIN-SFT [章节](../../../../books/part-04-training-system/29-sft.md)；状态：已落实并通过独立复核 |
| [Verifier-Backed Hard Problem Generation for Mathematical Reasoning](https://arxiv.org/html/2605.06660v1) | 2026-05-08T08:00:00+08:00 | setter–solver–verifier 分离 validity 与 difficulty authority；3+3+3=9 | 深入完成 | 整合：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md)；状态：已落实并通过独立复核 |
| [Expert Routing for Communication-Efficient MoE via Finite Expert Banks](https://arxiv.org/html/2605.05278v1) | 2026-05-08T08:00:00+08:00 | routing information 与可达 distortion 分离；2+2+2=6 | 深入完成 | 整合：MODEL-MOE [章节](../../../../books/part-02-model/21-moe.md)；状态：已落实并通过非作者写后复核 |
| [ReaComp: Compiling LLM Reasoning into Symbolic Solvers for Efficient Program Synthesis](https://arxiv.org/html/2605.05485v1) | 2026-05-08T08:00:00+08:00 | reasoning trace 编译为可复用 solver artifact；3+2+3=8 | 深入完成 | 整合：AGENT-WORKFLOW [章节](../../../../books/part-07-agent/81-workflow.md)；状态：已落实并通过非作者写后复核 |
| [MUSE: Resolving Manifold Misalignment in Visual Tokenization via Topological Orthogonality](https://arxiv.org/html/2605.05646v1) | 2026-05-08T08:00:00+08:00 | topology、semantic value 与 residual texture 分责；3+2+3=8 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；状态：已落实并通过非作者写后复核 |
| [Knowledge-Graph Paths as Intermediate Supervision for Self-Evolving Search Agents](https://arxiv.org/html/2605.05702v1) | 2026-05-08T08:00:00+08:00 | construction path 连接 data admission 与 bounded waypoint reward；3+2+2=7 | 深入完成 | 整合：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md)；状态：已落实并通过非作者写后复核 |
| [Conceal, Reconstruct, Jailbreak: Exploiting the Reconstruction-Concealment Tradeoff in MLLMs](https://arxiv.org/html/2605.05709v1) | 2026-05-08T08:00:00+08:00 | reconstruction–concealment 攻击跨越原始输入检查层；3+2+3=8 | 深入完成 | 整合：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；状态：已落实并通过非作者写后复核 |
| [Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention](https://arxiv.org/html/2605.05892v1) | 2026-05-08T08:00:00+08:00 | fixed vector 演进为 time/concept-conditioned flow intervention；3+2+2=7 | 深入完成 | 已有覆盖：MODEL-TRANSFORMER-LAYER / [Evaluation](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [P-Guide: Parameter-Efficient Prior Steering for Single-Pass CFG Inference](https://arxiv.org/html/2605.06124v1) | 2026-05-08T08:00:00+08:00 | 逐步双 pass CFG 前移为 initial-prior steering；3+2+2=7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；状态：已落实并通过非作者写后复核 |
| [EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields](https://arxiv.org/html/2605.06192v1) | 2026-05-08T08:00:00+08:00 | kinematic action realization 与 environment response 分权；3+2+2=7 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Taming the Entropy Cliff: Variable Codebook Size Quantization for Autoregressive Visual Generation](https://arxiv.org/html/2605.06207v1) | 2026-05-08T08:00:00+08:00 | position-indexed codebook capacity 与 coarse-to-fine 分配；3+2+3=8 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；状态：已落实并通过非作者写后复核 |

| [Nonsense Helps: Prompt Space Perturbation Broadens Reasoning Exploration](https://arxiv.org/html/2605.05566v1) | 2026-05-08T08:00:00+08:00 | LoPE 把 GRPO 的探索 actuator 从重复采样扩展到 prompt-space perturbation，并以 response regrouping 与 signal shaping 恢复稀有成功轨迹；exact-v1 的模型、数学任务与硬件边界已核验，Books 已有对应控制契约。；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-GRPO [章节](../../../../books/part-04-training-system/33-grpo.md) |
| [Nearly Optimal Attention Coresets](https://arxiv.org/html/2605.05602v1) | 2026-05-08T08:00:00+08:00 | 在 unit-norm keys/values、bounded query radius 与 additive-error 合同下给出与序列长度无关的 attention subset coreset 上界及 matching lower bound，补足长上下文压缩的理论可行性边界。；3+2+3=8 | 深入完成 | 整合：MODEL-LONG-CONTEXT [章节](../../../../books/part-02-model/22-long-context.md)；状态：已落实并通过非作者写后复核 |
| [Decomposing the Basic Abilities of Large Language Models: Mitigating Cross-Task Interference in Multi-Task Instruct-Tuning](https://arxiv.org/html/2605.05676v1) | 2026-05-08T08:00:00+08:00 | Badit 从静态奇异子空间初始化演进到按当前梯度方向动态重分组，使 LoRA expert 的 grouping identity 成为训练中持续维护的状态，并显式暴露 CPU 聚类与额外训练成本。；2+2+2=6 | 深入完成 | 整合：TRAIN-LORA [章节](../../../../books/part-04-training-system/30-lora.md)；状态：已落实并通过非作者写后复核 |
| [Steering Visual Generation in Unified Multimodal Models with Understanding Supervision](https://arxiv.org/html/2605.05781v1) | 2026-05-08T08:00:00+08:00 | UNO 通过冻结 understanding expert，让理解监督的梯度进入 noised generative representation，同时用 re-caption、prompt masking 与 metaquery 控制泄漏，补足统一生成中的监督路径与边界。；3+2+2=7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；状态：已落实并通过非作者写后复核 |
| [AGPO: Asymmetric Group Policy Optimization for Verifiable Reasoning and Search Ads Relevance at JD](https://arxiv.org/html/2605.05826v1) | 2026-05-08T08:00:00+08:00 | AGPO 以 variance-constrained positive advantage 与 gated negative signal 分开处理成功和失败轨迹，提供 RLVR support narrowing 的受限机制证据；Books 已有 zero-positive group、coverage 与 verifier authority 契约。；3+2+2=7 | 深入完成 | 已有覆盖：TRAIN-GRPO [章节](../../../../books/part-04-training-system/33-grpo.md) |
| [Logic-Regularized Verifier Elicits Reasoning from LLMs](https://arxiv.org/html/2605.05893v1) | 2026-05-08T08:00:00+08:00 | LoVer 用 hidden-state verifier 与逻辑一致性约束形成无标签 correctness sensor，但假设候选含正确答案且依赖白盒状态；Books 已明确 learned verifier 不拥有 truth 及其 fallback。；3+2+2=7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MINER: Mining Multimodal Internal Representation for Efficient Retrieval](https://arxiv.org/html/2605.06460v1) | 2026-05-08T08:00:00+08:00 | MINER 以 layer probe、validation-driven neuron mask 与多层 fusion 压成单向量索引，给出 retrieval quality 与 persisted index 成本的受限证据；Books 已有该 frontier 与 provenance 契约。；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-RAG [章节](../../../../books/part-07-agent/76-rag.md) |
| [MARBLE: Multi-Aspect Reward Balance for Diffusion RL](https://arxiv.org/html/2605.06507v1) | 2026-05-08T08:00:00+08:00 | MARBLE 保留 per-reward advantage/gradient ownership，再以约束优化和 EMA 平滑选择共同 update direction，补足多 reward 从 scalar mixing 到 gradient-space harmonization 的演进。；3+2+3=8 | 深入完成 | 整合：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md)；状态：已落实并通过非作者写后复核 |
| [Coordination Matters: Evaluation of Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/html/2605.06557v1) | 2026-05-08T08:00:00+08:00 | STAT 把 return 与 conflict、assignment diversity、throughput 等过程指标分账，并沿 agent/task/environment 三轴扩展；Books 已有 outcome、coordination cost 与 process evidence 的独立核算。；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [Are We Making Progress in Multimodal Domain Generalization? A Comprehensive Benchmark Study](https://arxiv.org/html/2605.06643v1) | 2026-05-08T08:00:00+08:00 | 统一实验合同显示 clean multimodal ranking、corruption/missing-modality、MisD 与 OOD 排名不可互相代理，补足多模态发布证据必须按 failure axis 分账的长期判断。；3+2+3=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；状态：已落实并通过非作者写后复核 |

| [XL-SafetyBench](https://arxiv.org/html/2605.05662v1) | 2026-05-08T08:00:00+08:00 | ASR、NSR、CSR 分轴，避免把安全韧性、文化敏感度与生成失败压成单一分数；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Large Vision-Language Models Get Lost in Attention](https://arxiv.org/html/2605.05668v1) | 2026-05-08T08:00:00+08:00 | residual geometry/entropy 区分 Attention reconfiguration 与 FFN expansion，并以选择性替换提供视觉路由冗余反证；3+2+3=8 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；状态：已落实并通过非作者写后复核 |
| [Weak-to-Strong Generalization is Nearly Inevitable (in Linear Models)](https://arxiv.org/html/2605.05742v1) | 2026-05-08T08:00:00+08:00 | 条件化线性理论反证 capacity mismatch 是 weak-to-strong 的必要机制；3+1+3=7 | 深入完成 | 整合：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md)；状态：已落实并通过非作者写后复核 |
| [ArenaPO](https://arxiv.org/html/2605.06070v1) | 2026-05-08T08:00:00+08:00 | pairwise arena verdict 经 capability posterior 变为连续 offline reward；3+2+2=7 | 深入完成 | 整合：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md)；状态：已落实并通过非作者写后复核 |
| [DynT2I-Eval](https://arxiv.org/html/2605.06170v1) | 2026-05-08T08:00:00+08:00 | fresh prompt、difficulty scheduler 与 uncertainty-aware late-entry ranking 组成动态 benchmark lifecycle；3+3+3=9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；状态：已落实并通过非作者写后复核 |
| [VL-LCM](https://arxiv.org/html/2605.06201v1) | 2026-05-08T08:00:00+08:00 | 无标注 logical-consistency sensor 与 accuracy/truth 分账；3+2+2=7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [FreeSpec](https://arxiv.org/html/2605.06509v1) | 2026-05-08T08:00:00+08:00 | long-video window 的 spectral concentration 由 global low-rank guidance 与 local high-rank reconstruction 修复；3+2+3=8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；状态：已落实并通过非作者写后复核 |
| [TriRelVLA](https://arxiv.org/html/2605.05714v1) | 2026-05-08T08:00:00+08:00 | appearance-entangled state 改为 object–hand–task relation graph 与 action bottleneck；3+2+3=8 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；状态：已落实并通过非作者写后复核 |
| [HyperLens](https://arxiv.org/html/2605.05741v1) | 2026-05-08T08:00:00+08:00 | layer-wise confidence trajectory 只作 processing-effort sensor，并暴露 SFT 后 trace/accuracy 退化；3+2+2=7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；handoff [TRAIN-SFT](../../../../books/part-04-training-system/29-sft.md) |
| [Hypothesis generation and updating in large language models](https://arxiv.org/html/2605.05851v1) | 2026-05-08T08:00:00+08:00 | hypothesis evaluation、generation 与未观察域 extrapolation 是不同能力接口；3+2+3=8 | 深入完成 | 整合：WORLDVIEW-LLM-INTELLIGENCE [章节](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md)；状态：已落实并通过非作者写后复核 |
| [Post Reasoning](https://arxiv.org/html/2605.06165v1) | 2026-05-08T08:00:00+08:00 | answer-first/optional-justification factorization 分开 answer latency 与解释成本；2+2+2=6 | 深入完成 | 整合：MODEL-SAMPLING [章节](../../../../books/part-02-model/20-sampling.md)；状态：已落实并通过非作者写后复核 |
| [PAGE / DomLoRA](https://arxiv.org/html/2605.06183v1) | 2026-05-08T08:00:00+08:00 | initial projected-gradient energy 只提出 adapter placement，held-out Gate 决定发布；2+2+2=6 | 深入完成 | 整合：TRAIN-LORA [章节](../../../../books/part-04-training-system/30-lora.md)；状态：已落实并通过非作者写后复核 |
| [Gaming the Metric, Not the Harm](https://arxiv.org/html/2605.06324v1) | 2026-05-08T08:00:00+08:00 | metric-as-security-object、semantic-envelope 与含 annotation/protocol error 的 certificate；3+2+3=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；状态：已落实并通过非作者写后复核 |
| [SKOP](https://arxiv.org/html/2605.06342v1) | 2026-05-08T08:00:00+08:00 | query-space steering 的 focus-to-tail QK rerouting 与 selective key-orthogonal repair；3+2+3=8 | 深入完成 | 整合：MODEL-SELF-ATTENTION [章节](../../../../books/part-02-model/14-self-attention.md)；状态：已落实并通过非作者写后复核 |
| [Trace-Prior RL](https://arxiv.org/html/2605.06529v1) | 2026-05-08T08:00:00+08:00 | partial observability 下 outcome-equivalent shortcut 需以 distributional trace prior + KL 约束修复；3+2+3=8 | 深入完成 | 整合：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md)；状态：已落实并通过非作者写后复核 |

| [AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/html/2605.05245v1) | 2026-05-08T08:00:00+08:00 | gap-aware controller 持有 evidence set、entity ledger、unresolved gaps 与 token budget，迭代修复多跳检索；2+3+2=7 | 深入完成 | 整合：AGENT-RAG [章节](../../../../books/part-07-agent/76-rag.md)；状态：已落实并通过非作者写后复核 |
| [GLiNER Guard: Unified Encoder Family for Production LLM Safety and Privacy](https://arxiv.org/html/2605.05277v1) | 2026-05-08T08:00:00+08:00 | 共享 encoder 合并 moderation 与 PII sensor，最终 policy authority 与 hard-case cascade 保持独立；2+3+2=7 | 深入完成 | 整合：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；状态：已落实并通过非作者写后复核 |
| [BALAR : A Bayesian Agentic Loop for Active Reasoning](https://arxiv.org/html/2605.05386v1) | 2026-05-08T08:00:00+08:00 | factorized latent belief 与 expected information gain 驱动 ask/act/stop，并保留 belief 非 authority 边界；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-PLANNING [章节](../../../../books/part-07-agent/79-planning.md) |
| [Information Theoretic Adversarial Training of Large Language Models](https://arxiv.org/html/2605.05415v1) | 2026-05-08T08:00:00+08:00 | f-divergence ambiguity set 将均匀 adversarial aggregation 改为受半径约束的 worst-case reweighting；3+2+2=7 | 深入完成 | 整合：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md)；状态：已落实并通过非作者写后复核 |
| [On Semantic Loss Fine-Tuning Approach for Preventing Model Collapse in Causal Reasoning](https://arxiv.org/html/2605.05438v1) | 2026-05-08T08:00:00+08:00 | label loss 与 graph-consistency semantic constraint 分账，防止结构推理被表面 accuracy 掩盖；2+2+2=6 | 深入完成 | 整合：TRAIN-SFT [章节](../../../../books/part-04-training-system/29-sft.md)；状态：已落实并通过非作者写后复核 |
| [Shortcut Solutions Learned by Transformers Impair Continual Compositional Reasoning](https://arxiv.org/html/2605.05495v1) | 2026-05-08T08:00:00+08:00 | shared recurrent execution depth 暴露 compositional shortcut 与 forward-transfer 的受限条件；2+1+2=5 | 标准完成 | 已有覆盖：MODEL-TRANSFORMER-LAYER [章节](../../../../books/part-02-model/17-transformer-layer.md) |
| [Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks](https://arxiv.org/html/2605.05503v1) | 2026-05-08T08:00:00+08:00 | watermark 验收从单次 paraphrase 扩展到 rewrite model/style/hop/threshold 组成的多跳 laundering threat state；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；状态：已落实并通过非作者写后复核 |
| [Scaling Pretrained Representations Enables Label-Free Out-of-Distribution Detection Without Fine-Tuning](https://arxiv.org/html/2605.05638v1) | 2026-05-08T08:00:00+08:00 | label-free OOD 将 backbone representation geometry 与 detector choice、calibration state 分账；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；状态：已落实并通过非作者写后复核 |
| [Enabling Federated Inference via Unsupervised Consensus Embedding](https://arxiv.org/html/2605.05718v1) | 2026-05-08T08:00:00+08:00 | consensus embedding 对齐异构 intermediate states，使 cooperative inference 不必共享 raw input、参数或统一 encoder；3+2+2=7 | 深入完成 | 整合：INFER-DYNAMO [章节](../../../../books/part-05-inference-system/52-dynamo.md)；状态：已落实并通过非作者写后复核 |
| [TACT: Mitigating Overthinking and Overacting in Coding Agents via Activation Steering](https://arxiv.org/html/2605.05980v1) | 2026-05-08T08:00:00+08:00 | trajectory drift sensor 只提出 activation intervention，不取得任务成功或效果 authority；2+2+2=6 | 深入完成 | 整合：AGENT-REFLECTION [章节](../../../../books/part-07-agent/80-reflection.md)；状态：已落实并通过非作者写后复核 |
| [Novelty-based Tree-of-Thought Search for LLM Reasoning and Planning](https://arxiv.org/html/2605.06040v1) | 2026-05-08T08:00:00+08:00 | novelty judge 调整 ToT branching/pruning，但受 hard budget、judge quality 与 verifier 约束；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-PLANNING [章节](../../../../books/part-07-agent/79-planning.md) |
| [XtraMAC: An Efficient MAC Architecture for Mixed-Precision LLM Inference on FPGA](https://arxiv.org/html/2605.06052v1) | 2026-05-08T08:00:00+08:00 | INT/FP 共享 product datapath，datatype-specific sign/exponent/accumulation 保留数值语义；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；状态：已落实并通过非作者写后复核 |
| [CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models](https://arxiv.org/html/2605.06247v1) | 2026-05-08T08:00:00+08:00 | learnable-query compression 与 router/adapter 分权形成异构 World Action Model 的 contextual transfer interface；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；状态：已落实并通过非作者写后复核 |
| [Continuous-Time Distribution Matching for Few-Step Diffusion Distillation](https://arxiv.org/html/2605.06376v1) | 2026-05-08T08:00:00+08:00 | few-step distillation 从固定离散 anchor 扩展到 continuous schedule 与 off-trajectory velocity alignment；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；状态：已落实并通过非作者写后复核 |
| [Patch-Effect Graph Kernels for LLM Interpretability](https://arxiv.org/html/2605.06480v1) | 2026-05-08T08:00:00+08:00 | activation patch 转为可比较 graph artifact，但 graph builder 只拥有 compression/diagnostic authority；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；状态：已落实并通过非作者写后复核 |
| [Improved techniques for fine-tuning flow models via adjoint matching: a deterministic control pipeline](https://arxiv.org/html/2605.06583v1) | 2026-05-08T08:00:00+08:00 | terminal reward adjoint 为 flow velocity field 提供 trajectory credit，并显式暴露 truncation 的早期 credit 风险；3+2+2=7 | 深入完成 | 整合：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md)；状态：已落实并通过非作者写后复核 |
| [Patch2Vuln: Agentic Reconstruction of Vulnerabilities from Linux Distribution Binary Patches](https://arxiv.org/html/2605.06601v1) | 2026-05-08T08:00:00+08:00 | binary-patch Agent 拆成 resumable typed stages，使 pre-model、reasoning 与 validation failure 可独立归因；2+2+2=6 | 深入完成 | 整合：AGENT-WORKFLOW [章节](../../../../books/part-07-agent/81-workflow.md)；状态：已落实并通过非作者写后复核 |
| [ActCam: Zero-Shot Joint Camera and 3D Motion Control for Video Generation](https://arxiv.org/html/2605.06667v1) | 2026-05-08T08:00:00+08:00 | camera/depth condition 在 denoising phase 间交接，分离 global geometry 与 high-frequency motion；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；状态：已落实并通过非作者写后复核 |

184 个候选均为本窗唯一 Source Family；同一 family 的项目页、实现或后续版本不会重复计分。canonical 最低 Evidence 路线仍为 `129 deep + 55 standard`；其中 10 个 5～6 分候选因实际进入 Books，在正式表中按 Integration Gate 的补读结果记为“深入完成”，不改变 frozen route 算术。最新 18 项的逐篇 Method、evaluation、direct limitation/non-proof 与 Books 对读见 [`V3_AUTHOR_BOUNDED_REPAIR_EIGHTEEN_FALSE_NEGATIVES_20260915.md`](../_sources/daily-20260508/V3_AUTHOR_BOUNDED_REPAIR_EIGHTEEN_FALSE_NEGATIVES_20260915.md)；15 项写回已按 [`ROOT_BOOKS_WRITEBACK_QUEUE_EIGHTEEN_FALSE_NEGATIVES_20260915.json`](../_sources/daily-20260508/ROOT_BOOKS_WRITEBACK_QUEUE_EIGHTEEN_FALSE_NEGATIVES_20260915.json) 落实并通过 fresh non-author 写后复核。


## 4. 证据与知识整合

以下均使用 exact-v1 HTML；正文只采用支撑目标命题所需的方法、关键评价与限制。作者 benchmark 只在披露的模型、数据、硬件、精度、长度、batch、并发、SLO 与 evaluator 范围内成立，未披露项不补造。

### [Understanding Annotator Safety Policy with Interpretability](https://arxiv.org/html/2605.05329v1)

APM 从既有 binary safety labels 建立共享 concept space，再为每个 annotator 拟合非负 logistic 或 DNF policy model；它把概念提取与 annotator policy approximation 分权。论文在 BeaverTails、WildGuardMix、五个 LLM annotator 和 DICES human annotations 上报告 held-out、controlled recovery 与 counterfactual faithfulness，但 concept space 仍依赖 LLM 生成与 embedding labeling，也不能解释价值分歧的真实原因或证明部署安全。长期增量是保存 annotator/policy identity，并将 disagreement 区分为 operational failure、policy ambiguity 与 value pluralism。

**Books 结论：** 整合到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已落实并通过独立复核。

### [ViTok-v2](https://arxiv.org/html/2605.05331v1)

ViTok-v2 以 NaFlex variable-resolution、2D RoPE、浅 encoder/大 decoder 和 DINOv3 perceptual loss 构造视觉 representation artifact，并在约 2B images、88M～4.5B decoder 和多个 compression ratio 上分别评价 reconstruction 与 downstream generation。作者披露 128 H200、BF16/FP8 GEMM 与 batch 8192；这些结果不证明任意视觉分布、视频或生产 decoder latency。长期比较必须同时冻结 resolution/aspect-ratio policy、compression、latent channels、decoder capacity、loss identity 与 generator capacity。

**Books 结论：** 整合到 [MULTIMODAL-REPRESENTATION](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；已落实并通过独立复核。

### [BitCal-TTS](https://arxiv.org/html/2605.05561v1)

4-bit quantization 会扭曲 adaptive test-time compute 的 uncertainty 与 trace-stability signal；bit-conditioned rescaling、post-marker confirmation horizon 与在线 proxy 因而共同决定 halting。证据只覆盖 greedy 4-bit Qwen2.5-Instruct 7B/14B、GSM8K 小型子集与 token cap 512，且作者明确给出 Wilson 95% CI 和统计功效不足；不能外推到其他 precision、sampler、任务或生产 SLO。

**Books 结论：** 整合到 [INFER-SCHEDULING](../../../../books/part-05-inference-system/56-inference-scheduling.md)；已落实并通过独立复核。

### [When Can Voting Help, Hurt, or Change Course?](https://arxiv.org/html/2605.05592v1)

在 exchangeable repeated correctness 的 latent mixture 下，多数投票曲线可以非单调并反复转向；完整 odd-budget curve 表达的是 signed voting signature，而不是单一 competence。证据主要是 de Finetti 表示与 signed Hausdorff moments 的理论结果，fixed-depth labels 只能揭示有限前缀，也不覆盖非交换采样、开放答案聚类或任意 judge。

**Books 结论：** 整合到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已落实并通过独立复核。

### [Architecture Matters](https://arxiv.org/html/2605.05632v1)

论文比较四种 RAG architecture 在单文档 poisoning 下的不同 failure path，并把 retrieval 命中、content reasoning、contradiction detection 与 resolution 分开。921 个 Natural Questions 和 clean/naive/CorruptRAG-AK 支持受限比较；MADAM-RAG 属于 reimplementation，contradiction judge precision 约 48.5%，non-answer 也较高，因此不能外推通用 attack rate。

**Books 结论：** 整合到 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)；已落实并通过独立复核。

### [Text-Graph Synergy](https://arxiv.org/html/2605.05643v1)

graph-to-text voting 重排文本证据，text-to-graph orphan bridging 从 search history 重开被 pruning 的 reasoning path，因此 deferred node 必须保存 identity 与 provenance。多项 multi-hop benchmark 支持该方向，但完整运行条件和 graph freshness/production latency 未披露，不能把局部相对增益外推为通用 RAG 结论。

**Books 结论：** 整合到 [AGENT-RAG](../../../../books/part-07-agent/76-rag.md)；已落实并通过独立复核。

### [ReFlect](https://arxiv.org/html/2605.05737v1)

ReFlect 的 deterministic wrapper 独立拥有 error detection 与 recovery，而不是让同一模型执行无约束 self-critique；六类 reasoning domain 和六个模型显示 harness 相对 self-critique 的受限收益，同时小模型可能无法填充结构化 state。现有 Ch81 已明确 verifier、recovery operator、budget 与 commit 的责任边界。

**Books 结论：** 已有覆盖到 [AGENT-WORKFLOW](../../../../books/part-07-agent/81-workflow.md)。

### [Adaptive Selection of LoRA Components](https://arxiv.org/html/2605.05769v1)

该方法在每层、每轮依据 curvature-aware score 选择 LoRA component，以避免统一固定 schedule 的 aggregation floor；selection 必须继承 privacy accountant。GLUE、SQuAD、CIFAR-100 与 Tiny-ImageNet 的严格 DP/non-IID 结果不覆盖恶意 client 或任意 DP mechanism，但确立了逐层逐轮 component control 的长期边界。

**Books 结论：** 整合到 [TRAIN-LORA](../../../../books/part-04-training-system/30-lora.md)；已落实并通过独立复核。

### [Distribution-Aligned Adversarial Distillation](https://arxiv.org/html/2605.05777v1)

model-specific lightweight proxy 以 adversarial distillation 近似黑盒输出分布，再产生 uncertainty sensor，试图减少多采样成本。作者报告约 1% target size 仍可量化 uncertainty，但 slice 与漂移条件不足；proxy fidelity 不等于 truth，仍需 deployment-slice calibration、drift 与 risk–coverage Gate。

**Books 结论：** 已有覆盖到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [LoopTrap](https://arxiv.org/html/2605.05846v1)

不可信 context 可以劫持 progress/termination judgment；LoopTrap 按行为画像选择并迭代攻击。8 个 Agent、60 个任务和 10 种攻击报告平均 3.57×、峰值 25× step amplification，但不能证明开放生产系统发生率或防御充分性；长期边界是 termination authority 不得与被污染 reasoning 共置。

**Books 结论：** 整合到 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)；已落实并通过独立复核。

### [Hallucination as an Anomaly](https://arxiv.org/html/2605.05953v1)

probabilistic circuit 对 residual stream 做 tractable density estimation，只在 NLL anomaly 时触发 latent-density contrastive decoding，从而把 sensor 与 correction authority 分开。四个 1B～8B 模型和四类 benchmark 只支持论文层选择与 factual-manifold 假设下的 detection/correction 证据，不能外推为 truth guarantee。

**Books 结论：** 整合到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已落实并通过独立复核。

### [Selective Eligibility Traces for RLVR](https://arxiv.org/html/2605.05965v1)

低熵 token mask 形成 sparse eligibility trace，替代把 trajectory advantage 均匀广播给所有 token。Qwen3 1.7B、4B、8B 的 pass@16 与 sample/token efficiency 不能证明低熵等于因果贡献，也未覆盖异步 rollout；它只建立条件化 token-credit artifact。

**Books 结论：** 整合到 [TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md)；已落实并通过独立复核。

### [Schedule-and-Calibrate](https://arxiv.org/html/2605.06111v1)

task utility 同时驱动 hierarchical data scheduling 与 per-task KL calibration，使 curriculum 与 regularization 共享训练状态而非分别调参。两个 LLM、四类 code task 的相对增益不证明其他 utility、任务组合或训练成本；该机制只作为受限多任务 RL controller 分支。

**Books 结论：** 整合到 [TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md)；已落实并通过独立复核。

### [DualSFT](https://arxiv.org/html/2605.06166v1)

在同一 validation objective 下，gradient interaction matrix 的行列聚合共同产生 data utility 与 parameter importance，以减少两个 selector 的重复计算与状态漂移。3B～9B LLM 的 matched-budget trade-off 仍只是局部一/二阶 response surrogate，不证明全局 bilevel optimum。

**Books 结论：** 整合到 [TRAIN-SFT](../../../../books/part-04-training-system/29-sft.md)；已落实并通过独立复核。

### [OPSD Compresses What RLVR Teaches](https://arxiv.org/html/2605.06188v1)

correct/incorrect rollout 分离显示，OPSD 对 thinking-enabled reasoning 更像压缩正确轨迹，而不是纠正错误轨迹，因此 pipeline 应条件化为 SFT→RLVR→OPSD。证据限于 thinking-enabled 数学推理和所列 correct-only/incorrect-only groups，不覆盖短输出或所有任务。

**Books 结论：** 整合到 [TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md)；已落实并通过独立复核。

### [TIDE](https://arxiv.org/html/2605.06216v1)

EmbeddingMemory 使用 K 个 context-free bank、depth-conditioned router 与 null bank，在每层重新注入 token identity，以缓解 rare-token under-training 与 contextual collapse。理论和多项 LM/downstream 实验不证明所有表示失效都来自单次注入，也缺大规模 serving cost；它是相对输入一次性 embedding 的条件分支。

**Books 结论：** 整合到 [MODEL-EMBEDDING](../../../../books/part-02-model/12-embedding.md)；已落实并通过顺序复核。

### [Joint Consistency](https://arxiv.org/html/2605.06219v1)

constrained Ising-type energy 同时消费 independent evaluation fields 与 pairwise judge interactions，并将 voting/weighted aggregation 表达为特例。math/code benchmark 与理论解释依赖 answer-level homogeneity；现有 Ch66 已把 per-item evidence、interaction graph 与 aggregation revision 绑定进 Evaluation Identity。

**Books 结论：** 已有覆盖到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Profiling for Pennies](https://arxiv.org/html/2605.06232v1)

从显式搜索、context inference 到跨源 aggregation，公开记录也可组合成敏感 derived profile。IcebergExplorer 的受控现实案例只报告所设搜索面的时间、成本与 factual accuracy，不能证明任意人群或风险发生率；query budget、最小暴露与 derived privacy 仍是控制边界。

**Books 结论：** 已有覆盖到 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [LatentRAG](https://arxiv.org/html/2605.06285v1)

一次 forward 产生 latent thought/subquery tokens，并与 dense retriever 在 latent space 对齐；parallel decoder 只提供可见解释视图。七个 benchmark 与作者报告的约 90% latency reduction 未完整绑定硬件、backend、batch/concurrency/SLO，latent trace 也不自动可审计，因此必须保留显式 trace/fallback。

**Books 结论：** 整合到 [AGENT-RAG](../../../../books/part-07-agent/76-rag.md)；已落实并通过独立复核。

### [Adaptive Task Graphs](https://arxiv.org/html/2605.06320v1)

团队共同维护带 dependency、assignment 与 progress 的 evolving coordination graph，在 partial observability 和 communication constraints 下动态分工。多类协作任务比较 token、wall-clock、communication、file conflict 与 accuracy；现有 Ch82 已具体承载 authoritative graph owner、ready set、commit/rebase 与 adaptive participation。

**Books 结论：** 已有覆盖到 [AGENT-MULTI-AGENT](../../../../books/part-07-agent/82-multi-agent.md)。

### [Pop Quiz Attack](https://arxiv.org/html/2605.06423v1)

方法将目标训练记录转成 quiz-style multiple-choice queries，以黑盒回答推断 membership；六个模型、四个数据集及 instruction/filter/DP defense 给出受限 ROC-AUC。它不等于法律归因或任意数据可恢复；membership signal 仍须绑定 sample identity、controls、query budget、低 FPR 与 defense boundary。

**Books 结论：** 已有覆盖到 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [Continuous Latent Diffusion Language Model](https://arxiv.org/pdf/2605.06548v1)

Text VAE 负责 text↔latent，block-causal DiT transport global semantic prior，conditional decoder 负责 local text realization，区别于 token-level observation denoising。8 个 benchmark、matched 约 2B AR/LLaDA baseline 与约 2000 EFLOPs scaling 不证明更大规模、生产 latency 或统一多模态表现；它只是改变生成 factorization 的条件分支。

**Books 结论：** 整合到 [MULTIMODAL-GENERATIVE-PARADIGMS](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；已落实并通过顺序复核。

### [FedAttr](https://arxiv.org/html/2605.06596v1)

成对 secure-aggregation subset queries 估计 client update，再以 watermark detector 差分评分并跨轮 Stouffer aggregation。作者设置报告 100% TPR、0% FPR、6.3% overhead 和每轮 mutual-information bound，但不覆盖恶意 server/client、任意 watermark 或法律归因；client subset、detector 与轮次必须保存在 attribution ledger。

**Books 结论：** 整合到 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)；已落实并通过独立复核。

### [Transformers Efficiently Perform In-Context Logistic Regression via Normalized Gradient Descent](https://arxiv.org/html/2605.06609v1)

论文构造 softmax-attention Transformer，使每层精确执行一次 in-context logistic loss 的 normalized-gradient step，并以 one-step GD teacher 监督单层后循环应用。线性收敛和 OOD guarantee 只在特定函数类、数据分布和参数共享条件下成立，不证明真实 LLM 的任意 ICL 都执行梯度下降，也不能把 hidden state 当成可观察 optimizer truth。

**Books 结论：** 整合到 [MODEL-TRANSFORMER-LAYER](../../../../books/part-02-model/17-transformer-layer.md)；已落实并通过独立复核。

### [Crafting Reversible SFT Behaviors](https://arxiv.org/html/2605.06632v1)

LCDD 在 utility budget 下联合优化 routing mask 与 weights，将 SFT behavior 压入 sparse causal carrier；SFT-Eraser 以 carrier-channel activation matching 的 soft prompt 尝试反转。多种行为与模型的结果不证明任意行为可定位，也不证明反转无副作用，因此必须保留 ordinary SFT 和完整回归验证作为 fallback。

**Books 结论：** 整合到 [TRAIN-SFT](../../../../books/part-04-training-system/29-sft.md)；已落实并通过独立复核。

### [Verifier-Backed Hard Problem Generation for Mathematical Reasoning](https://arxiv.org/html/2605.06660v1)

setter–solver–verifier 三方 self-play 将 validity 与 difficulty 交给不同 authority，且明确区分 hard symbolic verifier 与 soft LLM verifier。indefinite integration/general math 的 generation/filter funnel、ablation 与 subgroup 证据不等同通用数学正确性：hard guarantee 只覆盖窄域，soft judge 仍会接受错误、欠规格题或 reward-hacking artifact，baseline budget/mixture/schedule 也未完全匹配。

**Books 结论：** 整合到 [TRAIN-DATA](../../../../books/part-04-training-system/27-data.md)；已落实并通过独立复核。

### [SAT: Sequential Agent Tuning for Coordinator Free Plug and Play Multi-LLM Training with Monotonic Improvement Guarantees](https://arxiv.org/html/2605.05216v1)

exact-v1 §4/§6–7 将 team policy 写成顺序 block-coordinate 更新：每次在当前中间 occupancy 上更新一个 Agent，并以成员级 KL trust region 约束策略漂移。论文在 factorized team-policy 与采样/正则假设下给出单调改进并在七个 benchmark 测试；这不证明开放式通信、shared-parameter team 或生产 runtime 同样成立。已把 team revision、occupancy、重采样成本与冻结 peers fallback 写入 Ch82。

**Books 结论：** 整合到 [AGENT-MULTI-AGENT](../../../../books/part-07-agent/82-multi-agent.md)。

### [Sparse Prefix Caching for Hybrid and Recurrent LLM Serving](https://arxiv.org/html/2605.05219v1)

<!-- claim:SF-2026-ARXIV-2605-05219:start -->
- **Problem:** Prefix caching is a key latency optimization for autoregressive LLM serving, yet existing systems assume dense per-token key/value reuse.
- **Old path / changed constraint:** Prefix caching is a key latency optimization for autoregressive LLM serving, yet existing systems assume dense per-token key/value reuse.
- **Mechanism / ownership:** For hybrid and recurrent LLMs, store exact recurrent states only at a sparse set of prefix positions; on a partial-prefix hit, restore the nearest checkpoint and replay the missing suffix. Choose checkpoint positions from the observed overlap-depth distribution with an exact dynamic program, preserving exact outputs when recurrent state extraction and restoration are exact.
- **Evaluation contract:** exact-v1 比较 dense per-token KV-prefix caching、无 recurrent-state reuse 与不同 sparse checkpoint placement；结论只在模型能够精确抽取/恢复 recurrent state、请求前缀分布和论文实现范围内成立。缓存收益必须同时绑定 checkpoint density、prefix-overlap distribution、replay cost、state size 与 backend。
- **Proof / non-proof:** 论文不证明任意 hybrid/recurrent architecture 都能暴露 exact state，也没有证明分布漂移、restore error 或生产并发下的通用收益。
- **Trade-off / failure mode:** For chat-like workloads, where each consecutive request within a conversation contains the previous one as a substring, the optimal strategy is obviously to store only the last state, so our method does not bring additional benefits (but also incurs no overhead).
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.05219v1](https://arxiv.org/abs/2605.05219v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.05219v1.html.html`。
- **Disposition:** `Integrate — Applied`；Ch45 已拥有 sparse checkpoint、nearest restore 与 suffix replay 的机制正文。本轮只修复证据说明，不重复写入，也不把 Applied 误写成 No Change。
<!-- claim:SF-2026-ARXIV-2605-05219:end -->

**Books 结论：** 整合到 [INFER-KV-CACHE](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。

### [Adaptive Computation Depth via Learned Token Routing in Transformers](https://arxiv.org/html/2605.05222v1)

<!-- claim:SF-2026-ARXIV-2605-05222:start -->
- **Problem:** Standard transformer architectures apply the same number of layers to every token regardless of contextual difficulty.
- **Old path / changed constraint:** 固定深度 Transformer 为每个 token 执行相同 block 数，控制流规则且便于批处理；但 token 难度不同时，它会在简单 token 上浪费计算，也无法给困难 token 分配更多深度。
- **Mechanism / ownership:** Token-wise Scaling Architecture 在 block 间学习连续的逐 token residual gate，使每个 token 的残差更新幅度成为可训练状态；只有稀疏执行实现真正跳过被 gate 抑制的计算，路由决策由模型层产生，runtime 负责兑现 skip。
- **Evaluation contract:** 实验限于约 5–6M 参数模型、合成任务、Tiny Shakespeare 与 enwik8，并在 Apple M1 Pro 上比较固定深度、early exit、soft gating 与 sparse-TSA 的质量和吞吐；新增参数约 1.7%，soft gating 开销约 1%。未提供 LLM 规模、GPU 集群或线上 batching/SLO 证据。
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** 连续 soft gate 本身不减少 wall-clock FLOPs，必须由稀疏 kernel/runtime 利用 skip 才可能节省计算；逐 token 不规则路径会增加 batching、load balance 和实现复杂度。规模扩展、训练期内存收益以及 gate 与 token entropy/frequency 的关系仍未解决，因此不能从小模型结果外推到 LLM serving。
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.05222v1](https://arxiv.org/abs/2605.05222v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.05222v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-05222:end -->

**Books 结论：** 已有覆盖到 [INFER-SCHEDULING](../../../../books/part-05-inference-system/56-inference-scheduling.md)。

### [Structural Instability of Feature Composition](https://arxiv.org/html/2605.05223v1)

exact-v1 §3–4 与 Appendix G 解释非正交稀疏 feature 在 ReLU 锥中的组合坍塌与单向 ratchet，并用 CLEVR 结构化语义 feature 检查现象。随机过完备字典和受控任务不能证明 SAE 是普适因果字典；因此只采用“联合干预必须整体验收”的边界，写入 Ch31，失败时回退单方向/较小幅度或权重级后训练。

**Books 结论：** 整合到 [TRAIN-RLHF](../../../../books/part-04-training-system/31-rlhf.md)。

### [Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods](https://arxiv.org/html/2605.05227v1)

exact-v1 §3.4/§6–7 用当前 learner 的 loss、相似度和质量信号在线重加权样本，并在相同 FLOPs 的 instruction tuning 与 pretraining 对照中报告收益。结果受模型、语料与 proxy 约束，不能给出通用样本价值；Ch27 新增 checkpoint-coupled data control、selector drift、审计状态与冻结 mixture fallback。

**Books 结论：** 整合到 [TRAIN-DATA](../../../../books/part-04-training-system/27-data.md)。

### [Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction](https://arxiv.org/html/2605.05242v1)

exact-v1 §3 把 retrieval 从单次相似度排名改为 `search/read/refine` 的可组合 corpus interface，并让截断、compaction 与 summarization 成为 Agent 可见状态；§4 在 BrowseComp-Plus、multi-hop QA、BEIR/BRIGHT 和 tool/context ablation 中比较该路径。它提高 observation resolution，也把更多 index I/O、context 管理、工具权限与 step cost 交给 Agent；固定 corpus、proprietary backbone 与 API 成本不能证明它应替代高 QPS 或强访问控制下的 indexed retrieval。Ch75 已把 context 视为有 provenance、预算和权限的 observation state，故不重复新增正文。

**Books 结论：** 已有覆盖到 [AGENT-CONTEXT](../../../../books/part-07-agent/75-context.md)。

### [Towards Dependable Retrieval-Augmented Generation Using Factual Confidence Prediction](https://arxiv.org/html/2605.05244v1)

问题与旧路径：RAG confidence must distinguish retrieval support, claim entailment and answer uncertainty instead of using generation probability as evidence confidence. 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。exact-v1 §3.1 定义两阶段 factual-confidence 概念，§3.2 单独估计 retrieval confidence，§3.3 再估计 response confidence；这改变的是 confidence 的观测对象和分责，而不是仅增加一个模型名称。

Evaluation contract：exact-v1 §4.1 披露 experimental setup，§4.2 与 §4.3 分别报告 retrieval/response confidence 结果。论文没有独立 Limitations 章节，因此反证边界不能伪装成作者已完整披露：现有证据只支持其数据、模型与 confidence target，硬件、并发、生产 SLO 与跨域校准均为 Not Disclosed；§5 的 Conclusion 也没有把该方法提升为通用事实置信度。Artifact：exact-v1 未给出可冻结的 event-time repository/commit。<!-- claim:SF-RAG-CONFIDENCE-EVIDENCE-DECOMPOSITION:start -->长期结论只保留为：RAG confidence 必须拆开 retrieval support 与 response faithfulness；论文的 predictor score 不等于 claim correctness，也不能代替可引用证据、独立 verifier、fallback 与 rollback。<!-- claim:SF-RAG-CONFIDENCE-EVIDENCE-DECOMPOSITION:end -->

**Books 结论：** 已有覆盖到 [AGENT-RAG](../../../../books/part-07-agent/76-rag.md)。

### [DADL: A Declarative Description Language for Enterprise Tool Libraries in LLM Agent Systems](https://arxiv.org/html/2605.05247v1)

exact-v1 的 Method/Design 定义 enterprise tool-library grammar 与 compiler，把自然语言工具说明收缩为可静态验证的 schema、adapter 和 invocation contract；evaluation 检查 validation、tool selection 与 library scale。它能减少描述漂移，却不能让声明式语言接管 runtime authorization、side-effect commit 或动态后端 truth；语言覆盖、backend 兼容和工具变化仍是限制。Ch78 已区分 tool proposal、schema validation、authorization、execution 与 receipt，故判断为已有覆盖。

**Books 结论：** 已有覆盖到 [AGENT-TOOL-CALLING](../../../../books/part-07-agent/78-tool-calling.md)。

### [SecureMCP: A Policy-Enforced LLM Data Access Framework for AIoT Systems via Model Context Protocol](https://arxiv.org/html/2605.05260v1)

问题与机制：MCP data access must be policy-enforced at the effect boundary rather than delegated to model intent 旧路径在低风险、短轨迹或固定 workload 下仍成立。Method locator：`https://arxiv.org/html/2605.05260v1 https://arxiv.org/pdf/2605.05260v1 §3.3–3.5 — sequential fail-closed pipeline: table/column/operation RBAC, cost gate, SQL interceptor, risk classifier and database isolation own distinct pre-execution decisions — mechanism: The deployment of Large Language Model (LLM)-generated SQL queries in Artificial Intelligence of Things (AIoT) systems introduces critical security risks, as prompt injection attacks can manipulate LLMs into producing unauthorized queries that expose sensitive data or execute destructive operations.`。

Evaluation：`https://arxiv.org/html/2605.05260v1 https://arxiv.org/pdf/2605.05260v1 §4.1–4.6; §5.1–5.5 — IoT-SQL subset, Qwen3-8B-FP8 via vLLM 0.8, A6000, four clean-query roles and 2,400 adversarial queries; reported results remain bound to that contract — disclosed scope: Experiment A demonstrates that defense modules preserve execution accuracy, with EX-in-ALLOW remaining within 65.1%-76.4% across four RBAC roles, matching the unprotected baseline of 63.8%.`。Non-proof：`https://arxiv.org/html/2605.05260v1 https://arxiv.org/pdf/2605.05260v1 §6.3–6.4 — single model and benchmark, researcher-designed attacks, auditor-only adversarial role, rule-based blind spots and a coarse global cost threshold — no generalization beyond disclosed model, workload, hardware, precision and SLO`。Artifact：`https://arxiv.org/pdf/2605.05260v1 §4.6 — Python 3.11/sqlparse custom modules plus mysql-mcp-server-sse configuration are disclosed; immutable event-time implementation commit Not Disclosed`。
<!-- claim:SF-SECUREMCP-A-POLICY-ENFORCED-LLM-DATA-ACCESS-FRAMEWORK-FOR-AIOT-SYSTEMS-V:start -->长期结论仅限上述 exact-v1 披露边界；不外推到未测模型、硬件、并发、精度或 SLO。<!-- claim:SF-SECUREMCP-A-POLICY-ENFORCED-LLM-DATA-ACCESS-FRAMEWORK-FOR-AIOT-SYSTEMS-V:end -->

**Books 结论：** 已有覆盖到 [AGENT-MCP](../../../../books/part-07-agent/83-mcp.md)。

### [Maximizing Rollout Informativeness under a Fixed Budget: A Submodular View of Tree Search for Tool-Use Agentic Reinforcement Learning](https://arxiv.org/html/2605.05262v1)

问题与机制：tool-use rollout selection should optimize marginal information under a budget rather than expand a search tree uniformly 旧路径在低风险、短轨迹或固定 workload 下仍成立。Method locator：`https://arxiv.org/html/2605.05262v1 §4 Method: InfoTree — mechanism: We present InfoTree, a training-time tree-search framework coupling UUCB with a learned Adaptive Budget Allocator (ABA) and an asynchronous Speculative Expansion scheme.`。

Evaluation：`https://arxiv.org/html/2605.05262v1 §5 Experiments — disclosed scope: Across nine benchmarks spanning math reasoning (AIME 2024 and 2025, MATH-500, OlympiadBench, USAMO), web-search agents (GAIA, HLE-100, BrowseComp-lite), and tool-rich coding and OS agents (APPS-verified, AgentBench-OS), InfoTree outperforms flat GRPO, DeepSearch, Tree-GRPO, AT2PO, CW-GRPO, and RC-GRPO.`。Non-proof：`https://arxiv.org/html/2605.05262v1 §6 Conclusion; Broader Impact — no generalization beyond disclosed model, workload, hardware, precision and SLO`。Artifact：`https://arxiv.org/html/2605.05262v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-MAXIMIZING-ROLLOUT-INFORMATIVENESS-UNDER-A-FIXED-BUDGET-A-SUBMODULAR-VIE:start -->长期结论仅限上述 exact-v1 披露边界；不外推到未测模型、硬件、并发、精度或 SLO。<!-- claim:SF-MAXIMIZING-ROLLOUT-INFORMATIVENESS-UNDER-A-FIXED-BUDGET-A-SUBMODULAR-VIE:end -->

**Books 结论：** 整合到 [AGENT-PLANNING](../../../../books/part-07-agent/79-planning.md)。

### [Sealing the Audit-Runtime Gap for LLM Skills](https://arxiv.org/html/2605.05274v1)

问题与机制：LLM skills require a sealed audit-to-runtime identity so the reviewed artifact is the artifact actually executed 旧路径在低风险、短轨迹或固定 workload 下仍成立。Method locator：`https://arxiv.org/html/2605.05274v1 §3 Audit-Runtime Gap; §4 Sealing Mechanism — mechanism: We present SIGIL, the first framework that seals the audit-runtime gap for LLM skills.`。

Evaluation：`https://arxiv.org/html/2605.05274v1 §5 Evaluation — disclosed scope: Together, these results show that LLM skills can be cryptographically bound from publication through runtime at practical cost.`。Non-proof：`https://arxiv.org/html/2605.05274v1 §6 Limitations — no generalization beyond disclosed model, workload, hardware, precision and SLO`。Artifact：`https://arxiv.org/html/2605.05274v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-SEALING-THE-AUDIT-RUNTIME-GAP-FOR-LLM-SKILLS:start -->长期结论仅限上述 exact-v1 披露边界；不外推到未测模型、硬件、并发、精度或 SLO。<!-- claim:SF-SEALING-THE-AUDIT-RUNTIME-GAP-FOR-LLM-SKILLS:end -->

**Books 结论：** 整合到 [AGENT-PLATFORM](../../../../books/part-07-agent/84-agent-platform.md)。

### [Securing the Agent: Vendor-Neutral, Multitenant Enterprise Retrieval and Tool Use](https://arxiv.org/html/2605.05287v1)

问题与机制：enterprise agent retrieval and tool use require tenant-scoped identity and effect authorization 旧路径在低风险、短轨迹或固定 workload 下仍成立。Method locator：`https://arxiv.org/html/2605.05287v1 §3 Vendor-Neutral Multitenant Architecture — mechanism: However, real enterprise environments introduce challenges largely absent from academic treatments and consumer-facing APIs: multiple tenants with heterogeneous data, strict access-control requirements, regulatory compliance, and cost pressures that demand shared infrastructure.`。

Evaluation：`https://arxiv.org/html/2605.05287v1 §4 Retrieval and Tool Isolation; §5 Evaluation — disclosed scope: We formalize this gap and analyze additional shortcomings--including tool-mediated disclosure, context accumulation across turns, and client-side orchestration bypass--that arise when agentic systems conflate relevance with authorization.`。Non-proof：`https://arxiv.org/html/2605.05287v1 §6 Threats and Limitations — no generalization beyond disclosed model, workload, hardware, precision and SLO`。Artifact：`https://arxiv.org/html/2605.05287v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-SECURING-THE-AGENT-VENDOR-NEUTRAL-MULTITENANT-ENTERPRISE-RETRIEVAL-AND-T:start -->长期结论仅限上述 exact-v1 披露边界；不外推到未测模型、硬件、并发、精度或 SLO。<!-- claim:SF-SECURING-THE-AGENT-VENDOR-NEUTRAL-MULTITENANT-ENTERPRISE-RETRIEVAL-AND-T:end -->

**Books 结论：** 已有覆盖到 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [Partial Evidence Bench: Benchmarking Authorization-Limited Evidence in Agentic Systems](https://arxiv.org/html/2605.05379v1)

问题与机制：agent evaluation must model authorization-limited evidence rather than assume universal access to ground truth 旧路径在低风险、短轨迹或固定 workload 下仍成立。Method locator：`https://arxiv.org/html/2605.05379v1 §3 Authorization-Limited Evidence Contract — mechanism: Checked-in baselines show that silent filtering is catastrophically unsafe across all shipped families, while explicit fail-and-report behavior eliminates unsafe completeness without collapsing the task into trivial abstention.`。

Evaluation：`https://arxiv.org/html/2605.05379v1 §4 Benchmark Design; §5 Results — disclosed scope: Checked-in baselines show that silent filtering is catastrophically unsafe across all shipped families, while explicit fail-and-report behavior eliminates unsafe completeness without collapsing the task into trivial abstention.`。Non-proof：`https://arxiv.org/html/2605.05379v1 §6 Limitations — no generalization beyond disclosed model, workload, hardware, precision and SLO`。Artifact：`https://arxiv.org/html/2605.05379v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-PARTIAL-EVIDENCE-BENCH-BENCHMARKING-AUTHORIZATION-LIMITED-EVIDENCE-IN-AG:start -->长期结论仅限上述 exact-v1 披露边界；不外推到未测模型、硬件、并发、精度或 SLO。<!-- claim:SF-PARTIAL-EVIDENCE-BENCH-BENCHMARKING-AUTHORIZATION-LIMITED-EVIDENCE-IN-AG:end -->

**Books 结论：** 整合到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [From History to State: Constant-Context Skill Learning for LLM Agents](https://arxiv.org/html/2605.05413v1)

问题与机制：recurring procedures can move from growing prompts into learned modules while deterministic workflow state remains explicit 旧路径在低风险、短轨迹或固定 workload 下仍成立。Method locator：`https://arxiv.org/html/2605.05413v1 §3 History-to-State Skill Learning — mechanism: We propose constant-context skill learning, a context-to-weights framework for recurring agent workflows: reusable procedures are learned in lightweight task-family modules, while inference conditions only on the current observation and a compact state block.`。

Evaluation：`https://arxiv.org/html/2605.05413v1 §4 Experiments — disclosed scope: Across ALFWorld, WebShop, and SciWorld, our agents achieve strong performance across Qwen3-4B, Qwen3-8B and Llama-3.1-8B.`。Non-proof：`https://arxiv.org/html/2605.05413v1 §5 Limitations — no generalization beyond disclosed model, workload, hardware, precision and SLO`。Artifact：`https://arxiv.org/html/2605.05413v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-FROM-HISTORY-TO-STATE-CONSTANT-CONTEXT-SKILL-LEARNING-FOR-LLM-AGENTS:start -->长期结论仅限上述 exact-v1 披露边界；不外推到未测模型、硬件、并发、精度或 SLO。<!-- claim:SF-FROM-HISTORY-TO-STATE-CONSTANT-CONTEXT-SKILL-LEARNING-FOR-LLM-AGENTS:end -->

**Books 结论：** 整合到 [AGENT-WORKFLOW](../../../../books/part-07-agent/81-workflow.md)。

### [Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure](https://arxiv.org/html/2605.05440v1)

问题与机制：authorization must propagate through delegation, aggregation and time, not attach only to the initiating identity 旧路径在低风险、短轨迹或固定 workload 下仍成立。Method locator：`https://arxiv.org/html/2605.05440v1 §3 Identity and Authorization Propagation — mechanism: The security discussion around agentic AI focuses heavily on prompt injection.`。

Evaluation：`https://arxiv.org/html/2605.05440v1 §4 System Model; §5 Evaluation — disclosed scope: This paper argues that multi-agent systems also create a distinct authorization problem: maintaining authorization invariants as non-human principals retrieve data, delegate tasks, and synthesize results across changing boundaries.`。Non-proof：`https://arxiv.org/html/2605.05440v1 §6 Limitations — no generalization beyond disclosed model, workload, hardware, precision and SLO`。Artifact：`https://arxiv.org/html/2605.05440v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-AUTHORIZATION-PROPAGATION-IN-MULTI-AGENT-AI-SYSTEMS-IDENTITY-GOVERNANCE-:start -->长期结论仅限上述 exact-v1 披露边界；不外推到未测模型、硬件、并发、精度或 SLO。<!-- claim:SF-AUTHORIZATION-PROPAGATION-IN-MULTI-AGENT-AI-SYSTEMS-IDENTITY-GOVERNANCE-:end -->

**Books 结论：** 已有覆盖到 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [Nitsum: Serving Tiered LLM Requests with Adaptive Tensor Parallelism](https://arxiv.org/html/2605.05467v1)

问题与机制：tensor parallelism can become a runtime control surface jointly optimized with PD split and request scheduling 旧路径在低风险、短轨迹或固定 workload 下仍成立。Method locator：`https://arxiv.org/html/2605.05467v1 §3 Nitsum Design; §4 Adaptive TP Controller — mechanism: We present Nitsum, a distributed LLM serving system that treats tensor parallelism (TP) as a first-class runtime control surface rather than a static deployment choice.`。

Evaluation：`https://arxiv.org/html/2605.05467v1 §5 Implementation; §6 Evaluation — disclosed scope: Experiments on real traces and targeted microbenchmarks show that Nitsum improves SLO-compliant goodput over SoTA by up to 5.3 times.`。Non-proof：`https://arxiv.org/html/2605.05467v1 §7 Discussion and Limitations — no generalization beyond disclosed model, workload, hardware, precision and SLO`。Artifact：`https://arxiv.org/html/2605.05467v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-NITSUM-SERVING-TIERED-LLM-REQUESTS-WITH-ADAPTIVE-TENSOR-PARALLELISM:start -->长期结论仅限上述 exact-v1 披露边界；不外推到未测模型、硬件、并发、精度或 SLO。<!-- claim:SF-NITSUM-SERVING-TIERED-LLM-REQUESTS-WITH-ADAPTIVE-TENSOR-PARALLELISM:end -->

**Books 结论：** 整合到 [INFER-SCHEDULING](../../../../books/part-05-inference-system/56-inference-scheduling.md)。

### [WAAA! Web Adversaries Against Agentic Browsers](https://arxiv.org/html/2605.05509v1)

问题与机制：agentic-browser threat models must include ordinary web attacks and confused-deputy effects, not only prompt injection 旧路径在低风险、短轨迹或固定 workload 下仍成立。Method locator：`https://arxiv.org/html/2605.05509v1 §3 Threat Model; §4 WAAA Attacks — mechanism: In this paper, we propose the first web-focused threat model for agentic browsers and use it to derive a taxonomy of 20 attacks across both the web and LLM space, and implement 18 of the attacks.`。

Evaluation：`https://arxiv.org/html/2605.05509v1 §5 Evaluation — disclosed scope: In this paper, we propose the first web-focused threat model for agentic browsers and use it to derive a taxonomy of 20 attacks across both the web and LLM space, and implement 18 of the attacks.`。Non-proof：`https://arxiv.org/html/2605.05509v1 §6 Limitations — no generalization beyond disclosed model, workload, hardware, precision and SLO`。Artifact：`https://arxiv.org/html/2605.05509v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-WAAA-WEB-ADVERSARIES-AGAINST-AGENTIC-BROWSERS:start -->长期结论仅限上述 exact-v1 披露边界；不外推到未测模型、硬件、并发、精度或 SLO。<!-- claim:SF-WAAA-WEB-ADVERSARIES-AGAINST-AGENTIC-BROWSERS:end -->

**Books 结论：** 已有覆盖到 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [OpenG2G: A Simulation Platform for AI Datacenter-Grid Runtime Coordination](https://arxiv.org/html/2605.05519v1)

问题与机制：datacenter workload control and grid response form one closed-loop runtime coordination problem 旧路径在低风险、短轨迹或固定 workload 下仍成立。Method locator：`https://arxiv.org/html/2605.05519v1 §3 OpenG2G Design — mechanism: AI's growing compute demand and new datacenter buildouts present major capacity and reliability challenges for the electricity grid, leading to multi-year interconnection delays for new datacenters and bottlenecking AI growth.`。

Evaluation：`https://arxiv.org/html/2605.05519v1 §4 Grid/AI Workload Scenarios; §5 Evaluation — disclosed scope: We describe the design of OpenG2G and demonstrate its usefulness through realistic grid scenarios and AI workloads.`。Non-proof：`https://arxiv.org/html/2605.05519v1 §6 Limitations — no generalization beyond disclosed model, workload, hardware, precision and SLO`。Artifact：`https://arxiv.org/html/2605.05519v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-OPENG2G-A-SIMULATION-PLATFORM-FOR-AI-DATACENTER-GRID-RUNTIME-COORDINATIO:start -->长期结论仅限上述 exact-v1 披露边界；不外推到未测模型、硬件、并发、精度或 SLO。<!-- claim:SF-OPENG2G-A-SIMULATION-PLATFORM-FOR-AI-DATACENTER-GRID-RUNTIME-COORDINATIO:end -->

**Books 结论：** 已有覆盖到 [PLATFORM-COST](../../../../books/part-06-ai-infrastructure/70-cost.md)。

### [Accelerating MoE with Dynamic In-Switch Computing on Multi-GPUs](https://arxiv.org/html/2605.05607v1)

机制边界：To bridge the functionality gap, we propose DySHARP, an integral dynamic in-switch computing solution to accelerate MoE, encompassing both communication primitives and communication-aware scheduling: 1) Dynamic multimem addressing co-designs ISA, architecture, and runtime, as a dynamic extension to…。Method/identity locator：`https://arxiv.org/html/2605.05607v1 §3 DySHARP Design — mechanism: To bridge the functionality gap, we propose DySHARP, an integral dynamic in-switch computing solution to accelerate MoE, encompassing both communication primitives and communication-aware scheduling: 1) Dynamic multimem addressing co-designs ISA, architecture, and runtime, as a dynamic extension to…`；evaluation locator：`https://arxiv.org/html/2605.05607v1 §4 Evaluation — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.05607v1 §5 Discussion and Conclusion — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.05607v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-ACCELERATING-MOE-WITH-DYNAMIC-IN-SWITCH-COMPUTING-ON-MULTI-GPUS:start -->DySHARP 只证明在论文披露的多 GPU、MoE 路由与可编程 switch 资源下，动态 addressing、collective 与 communication-aware scheduling 能协同减少通信停顿；它不证明任意互连或交换芯片都具备同样原语。<!-- claim:SF-ACCELERATING-MOE-WITH-DYNAMIC-IN-SWITCH-COMPUTING-ON-MULTI-GPUS:end -->
当 switch 不支持动态地址/规约、拓扑较小或兼容性优先时，普通 NCCL collectives 与 GPU-side expert parallel 仍是更稳妥的路径。

**Books 结论：** 整合到 [TRAIN-TENSOR-PARALLEL](../../../../books/part-04-training-system/37-tensor-parallel.md)。

### [Towards Compute-Aware In-Switch Computing for LLMs Tensor-Parallelism on Multi-GPU Systems](https://arxiv.org/html/2605.05628v1)

机制边界：While in-switch computing, exemplified by NVLink SHARP (NVLS), accelerates collective operations by reducing redundant data transfer, its communication-centric design philosophy introduces the mismatch between its communication mode and the memory semantic requirement of LLM's computation kernel.。Method/identity locator：`https://arxiv.org/html/2605.05628v1 §III CAIS Design — mechanism: While in-switch computing, exemplified by NVLink SHARP (NVLS), accelerates collective operations by reducing redundant data transfer, its communication-centric design philosophy introduces the mismatch between its communication mode and the memory semantic requirement of LLM's computation kernel.`；evaluation locator：`https://arxiv.org/html/2605.05628v1 §IV Experimental Methodology; §V Experimental Results — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.05628v1 §V-D Hardware Overhead; §VII Conclusion — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.05628v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-TOWARDS-COMPUTE-AWARE-IN-SWITCH-COMPUTING-FOR-LLMS-TENSOR-PARALLELISM-ON:start -->CAIS 只在论文给定的 NVLS-like in-switch compute、tensor-parallel kernel 与 memory-semantic 假设下证明通信模式和计算语义可联合设计；不能外推为所有算子或内存模型都可下沉。<!-- claim:SF-TOWARDS-COMPUTE-AWARE-IN-SWITCH-COMPUTING-FOR-LLMS-TENSOR-PARALLELISM-ON:end -->
对不受支持的算子、跨节点拓扑或需要通用 kernel 语义的 workload，host/GPU collectives 仍保留 canonical fallback。

**Books 结论：** 整合到 [TRAIN-TENSOR-PARALLEL](../../../../books/part-04-training-system/37-tensor-parallel.md)。

### [Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization](https://arxiv.org/html/2605.05683v1)

exact-v1 §2.1/§6 及附录以 activation covariance 和 per-sample gradient SVD 诊断训练几何，在 12/36/48 层受控 NanoGPT 家族中显示 batch size 可在相近 loss 下改变谱形，早期谱与 token efficiency 相关。SVD 成本、样本规模与架构外推均未解决；Ch28 只把 spectrum 作为 bounded sensor，不授予自动调参或停止权。

**Books 结论：** 整合到 [TRAIN-PRETRAINING](../../../../books/part-04-training-system/28-pretraining.md)。

### [DataDignity: Training Data Attribution for Large Language Models](https://arxiv.org/html/2605.05687v1)

机制边界：We study this as pinpoint provenance: given a prompt, a target-model response, and a candidate corpus, rank the documents that best support the response.。Method/identity locator：`https://arxiv.org/html/2605.05687v1 §3 FakeWiki Benchmark; §4 Methods — mechanism: We study this as pinpoint provenance: given a prompt, a target-model response, and a candidate corpus, rank the documents that best support the response.`；evaluation locator：`https://arxiv.org/html/2605.05687v1 §5 Experimental Setup; §6 Results — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.05687v1 §6.2 per-method results; Limitations — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.05687v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-DATADIGNITY-TRAINING-DATA-ATTRIBUTION-FOR-LARGE-LANGUAGE-MODELS:start -->DataDignity 的结果限于给定 prompt、target response 与 candidate corpus 上的 pinpoint-provenance 排序；它没有证明文档对参数更新的因果贡献，也不能据此推断训练数据所有权。<!-- claim:SF-DATADIGNITY-TRAINING-DATA-ATTRIBUTION-FOR-LARGE-LANGUAGE-MODELS:end -->
当候选语料不完备或需要 corpus-level 因果审计时，数据 lineage、许可记录与训练前后对照仍不可替代。

**Books 结论：** 已有覆盖到 [TRAIN-DATA](../../../../books/part-04-training-system/27-data.md)。

### [Irminsul: MLA-Native Position-Independent Caching for Agentic LLM Serving](https://arxiv.org/html/2605.05696v1)

机制边界：We present Irminsul, which extends SGLang's radix cache with content-hash keying over CDC-chunked segments and a $δ$-rotation rule for $k_r$.。Method/identity locator：`https://arxiv.org/html/2605.05696v1 §3–§7 Agentic Workload, Position Invariance and Irminsul — mechanism: We present Irminsul, which extends SGLang's radix cache with content-hash keying over CDC-chunked segments and a $δ$-rotation rule for $k_r$.`；evaluation locator：`https://arxiv.org/html/2605.05696v1 §7.4 Recovery Measurement; Appendix H Output Consistency — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.05696v1 §7.3 RoPE Pitfall; Appendix D/F/G — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.05696v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-IRMINSUL-MLA-NATIVE-POSITION-INDEPENDENT-CACHING-FOR-AGENTIC-LLM-SERVING:start -->Irminsul 只证明在 MLA、CDC chunk、content hash 与论文给出的 RoPE rotation 条件下可复用位置无关 prefix state；该状态不能与普通 MHA KV 或不同模型 revision 任意互换。<!-- claim:SF-IRMINSUL-MLA-NATIVE-POSITION-INDEPENDENT-CACHING-FOR-AGENTIC-LLM-SERVING:end -->
当模型结构、RoPE 语义、tokenizer 或内容身份无法严格匹配时，逐请求精确 prefill 仍是 correctness fallback。

**Books 结论：** 已有覆盖到 [INFER-KV-CACHE](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。

### [When Quantization Is Free: An int4 KV Cache That Outruns fp16 on Apple Silicon](https://arxiv.org/html/2605.05699v1)

机制边界：We show it is \emph{inverted} on Apple Silicon's unified memory: a single fused Metal kernel (sign-randomized FFT $+$ per-channel $λ$ $+$ per-group abs-max $+$ int4 nibble pack), exposed as a HuggingFace \texttt{Cache} subclass, runs \emph{faster than fp16} across…。Method/identity locator：`https://arxiv.org/html/2605.05699v1 §3 Method; §5 Learning the Rotation — mechanism: We show it is \emph{inverted} on Apple Silicon's unified memory: a single fused Metal kernel (sign-randomized FFT $+$ per-channel $λ$ $+$ per-group abs-max $+$ int4 nibble pack), exposed as a HuggingFace \texttt{Cache} subclass, runs \emph{faster than fp16} across…`；evaluation locator：`https://arxiv.org/html/2605.05699v1 §4 Experiments; §7 End-to-end Deployment — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.05699v1 §8 Discussion; §9 Conclusion — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.05699v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-WHEN-QUANTIZATION-IS-FREE-AN-INT4-KV-CACHE-THAT-OUTRUNS-FP16-ON-APPLE-SI:start -->该结果只覆盖 Apple unified memory、所述 fused Metal kernel、模型与长度；“int4 更快”不等于 CUDA/datacenter 环境通用，也不等于量化对质量无损。<!-- claim:SF-WHEN-QUANTIZATION-IS-FREE-AN-INT4-KV-CACHE-THAT-OUTRUNS-FP16-ON-APPLE-SI:end -->
硬件缺少对应融合路径、质量门槛更严或回退成本不可接受时，fp16/bf16 dense KV 仍合理。

**Books 结论：** 已有覆盖到 [INFER-KV-CACHE](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。

### [On the Blessing of Pre-training in Weak-to-Strong Generalization](https://arxiv.org/html/2605.05710v1)

exact-v1 §3–5 把 pretraining 解释为高维 single-index 模型的 spectral warm start，并报告 checkpoint 随规模出现的 phase-transition 线索；限制部分明确预训练在某些理论设定并非必要。该证据为表示/优化已有主线提供条件性解释，但没有改变 Ch28 已有的 data–objective–optimizer contract，判断为已有覆盖。

**Books 结论：** 已有覆盖到 [TRAIN-PRETRAINING](../../../../books/part-04-training-system/28-pretraining.md)。

### [More Is Not Always Better: Cross-Component Interference in LLM Agent Scaffolding](https://arxiv.org/html/2605.05716v1)

机制边界：We study cross-component interference (CCI): degradation when components interact destructively.。Method/identity locator：`https://arxiv.org/html/2605.05716v1 §3 Problem Setup; §6 Analysis Framework — mechanism: We study cross-component interference (CCI): degradation when components interact destructively.`；evaluation locator：`https://arxiv.org/html/2605.05716v1 §4–§5 Main Results; §7 Robustness — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.05716v1 §8 Error Analysis; §9 Discussion; Appendix E — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.05716v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-MORE-IS-NOT-ALWAYS-BETTER-CROSS-COMPONENT-INTERFERENCE-IN-LLM-AGENT-SCAF:start -->论文在披露的 agent scaffold 与任务中测得 component interaction 会破坏单组件收益；它不证明组件数量单调导致退化，也不覆盖未测试的组合与模型。<!-- claim:SF-MORE-IS-NOT-ALWAYS-BETTER-CROSS-COMPONENT-INTERFERENCE-IN-LLM-AGENT-SCAF:end -->
单组件或经过组合回归测试的静态 scaffold 仍可成立，新增组件必须以组合级行为证据而非局部指标准入。

**Books 结论：** 已有覆盖到 [AGENT-PLATFORM](../../../../books/part-07-agent/84-agent-platform.md)。

### [Auto Research with Specialist Agents Develops Effective and Non-Trivial Training Recipes](https://arxiv.org/html/2605.05724v1)

机制边界：We study auto research as a closed empirical loop driven by external measurement.。Method/identity locator：`https://arxiv.org/html/2605.05724v1 §3 Closed-Loop Auto Research Methodology — mechanism: We study auto research as a closed empirical loop driven by external measurement.`；evaluation locator：`https://arxiv.org/html/2605.05724v1 §4 Experiments; submitted-trial lineage — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.05724v1 §5 Analysis; §6 Discussion; evaluator-owned scope — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.05724v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-AUTO-RESEARCH-WITH-SPECIALIST-AGENTS-DEVELOPS-EFFECTIVE-AND-NON-TRIVIAL-:start -->该 specialist-agent loop 只在论文的 trial budget、任务与 evaluator 下证明可以提出并筛选训练 recipe；它没有把科学有效性或可复现性 authority 交给 agent。<!-- claim:SF-AUTO-RESEARCH-WITH-SPECIALIST-AGENTS-DEVELOPS-EFFECTIVE-AND-NON-TRIVIAL-:end -->
高风险研究结论仍需固定实验合同、独立复跑与人工判读；开放式 agent search 只是 proposal mechanism。

**Books 结论：** 已有覆盖到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Transformers Provably Implement In-Context Reinforcement Learning with Policy Improvement](https://arxiv.org/html/2605.05755v1)

exact-v1 §3–5 证明特定 linear self-attention 可实现 SARSA/actor-critic，并在 teacher-mimicking 与 richness 假设下给出局部指数收敛；实验为随机 tabular MDP。它支持 in-context RL 的可表达性，不证明深层非线性 LLM、真实工具环境或 RLHF pipeline 的训练保证；Ch31 已区分 policy distribution、credit 与 verifier，判断为已有覆盖。

**Books 结论：** 已有覆盖到 [TRAIN-RLHF](../../../../books/part-04-training-system/31-rlhf.md)。

### [Revealing Modular Gradient Noise Imbalance in LLMs: Calibrating Adam via Signal-to-Noise Ratio](https://arxiv.org/html/2605.05794v1)

机制边界：To establish a more principled approach, we first analyze the noise-damping behavior of Adam in high-noise modules and introduce \textbf{Module-wise Learning Rate Scaling via SNR (MoLS)}.。Method/identity locator：`https://arxiv.org/html/2605.05794v1 §3 Motivation; §4 Methodology — mechanism: To establish a more principled approach, we first analyze the noise-damping behavior of Adam in high-noise modules and introduce \textbf{Module-wise Learning Rate Scaling via SNR (MoLS)}.`；evaluation locator：`https://arxiv.org/html/2605.05794v1 §5 Experiments; §6 Additional Investigations — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.05794v1 Appendix D Discussion and Future Work — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.05794v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-REVEALING-MODULAR-GRADIENT-NOISE-IMBALANCE-IN-LLMS-CALIBRATING-ADAM-VIA-:start -->MoLS 的 module-wise SNR 是论文模型与 optimizer 下的诊断及缩放信号，不是跨架构通用的 layer learning-rate oracle，也未证明能替代全局稳定性控制。<!-- claim:SF-REVEALING-MODULAR-GRADIENT-NOISE-IMBALANCE-IN-LLMS-CALIBRATING-ADAM-VIA-:end -->
在模块噪声差异不稳定、估计成本过高或跨阶段不可校准时，全局 LR schedule、gradient clipping 与 loss/gradient 监控仍是基线。

**Books 结论：** 整合到 [TRAIN-PRETRAINING](../../../../books/part-04-training-system/28-pretraining.md)。

### [HCInfer: An Efficient Inference System via Error Compensation for Resource-Constrained Devices](https://arxiv.org/html/2605.05819v1)

机制边界：Motivated by this opportunity, we propose HCInfer, a heterogeneous inference system that offloads residual compensation to the CPU while executing the compressed backbone on the GPU, and further introduces an asynchronous compensation pipeline and sensitivity-aware dynamic rank allocation…。Method/identity locator：`https://arxiv.org/html/2605.05819v1 §3 Observations; §4 HCInfer — mechanism: Motivated by this opportunity, we propose HCInfer, a heterogeneous inference system that offloads residual compensation to the CPU while executing the compressed backbone on the GPU, and further introduces an asynchronous compensation pipeline and sensitivity-aware dynamic rank allocation…`；evaluation locator：`https://arxiv.org/html/2605.05819v1 §5 Evaluation; Appendix C — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.05819v1 §6 Conclusion; Appendix B assumptions — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.05819v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-HCINFER-AN-EFFICIENT-INFERENCE-SYSTEM-VIA-ERROR-COMPENSATION-FOR-RESOURC:start -->HCInfer 只在披露的 edge CPU/GPU、压缩 backbone、residual rank 与异步 pipeline 下证明异构补偿可改善效率；它不构成通用 split-inference 最优解。<!-- claim:SF-HCINFER-AN-EFFICIENT-INFERENCE-SYSTEM-VIA-ERROR-COMPENSATION-FOR-RESOURC:end -->
设备内存足够、CPU/GPU 传输成为瓶颈或误差补偿不稳定时，GPU-only 完整模型或普通量化仍更合适。

**Books 结论：** 已有覆盖到 [INFER-TENSORRT-LLM](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。

### [Evaluation Awareness in Language Models Has Limited Effect on Behaviour](https://arxiv.org/html/2605.05835v1)

exact-v1 §3–5 对八个 open-weight reasoning models、四类 benchmark 做 on/off-policy intervention；verbalized evaluation awareness 对平均行为影响有限。该负面结果不能排除 latent awareness、closed models 或其他任务中的适应性，也不证明 evaluation contamination 无害；Ch66 已要求隐藏/可见条件、provider revision 与反事实评测，判断为已有覆盖。

**Books 结论：** 已有覆盖到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [SkillScope: Toward Fine-Grained Least-Privilege Enforcement for Agent Skills](https://arxiv.org/html/2605.05868v1)

机制边界：In this paper, we present SkillScope, a framework for fine-grained least-privilege enforcement in Agent Skills.。Method/identity locator：`https://arxiv.org/html/2605.05868v1 §3 SkillScope design; graph and replay enforcement — mechanism: In this paper, we present SkillScope, a framework for fine-grained least-privilege enforcement in Agent Skills.`；evaluation locator：`https://arxiv.org/html/2605.05868v1 §5 Evaluation; replay ablations — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.05868v1 §6 Discussion; stated limitations — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.05868v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-SKILLSCOPE-TOWARD-FINE-GRAINED-LEAST-PRIVILEGE-ENFORCEMENT-FOR-AGENT-SKI:start -->SkillScope 的 graph/replay enforcement 只约束已声明并被策略覆盖的 skill effects；它不能发现未声明副作用，也不能抵抗被攻陷的 enforcement plane。<!-- claim:SF-SKILLSCOPE-TOWARD-FINE-GRAINED-LEAST-PRIVILEGE-ENFORCEMENT-FOR-AGENT-SKI:end -->
未知技能、不可解释副作用或高风险写操作仍应使用 deny-by-default sandbox、独立授权与 effect receipt。

**Books 结论：** 已有覆盖到 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [CITE: Anytime-Valid Statistical Inference in LLM Self-Consistency](https://arxiv.org/html/2605.05873v1)

exact-v1 §4–7 给出基于 e-process 的 anytime-valid unique-mode certificate，可在未知回答类别和任意合法停止时刻控制声明误差。certificate 只证明 response mode 占优，不证明答案 correctness、事实性或安全；Ch66 新增 model/sampler、停止规则、独立性与 external verifier 的分责及固定样本 fallback。

**Books 结论：** 整合到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [MoE-Hub: Taming Software Complexity for Seamless MoE Overlap with Hardware-Accelerated Communication on Multi-GPU Systems](https://arxiv.org/html/2605.05888v1)

exact-v1 §II/V–IX 以 destination-agnostic MoE communication 和 hardware hub 承担地址分配/控制面，报告作者平台上的 layer 与 end-to-end 加速。结果依赖 simulator、硬件 co-design、模型和互连，不能外推部署 goodput；Ch37 已覆盖 expert communication、collective 和硬件共设计的责任边界，判断为已有覆盖。

**Books 结论：** 已有覆盖到 [TRAIN-TENSOR-PARALLEL](../../../../books/part-04-training-system/37-tensor-parallel.md)。

### [Near-Policy: Accelerating On-Policy Distillation via Asynchronous Generation and Selective Packing](https://arxiv.org/html/2605.05940v1)

exact-v1 §3–6 将 student generation 与训练异步化，用 sparse update 与 Δ-IFD filter 限制 policy lag 和噪声，作者报告相对 on-policy 的吞吐/质量结果。filter 是 heuristic，代码与跨模型泛化仍是 future work；Ch31 已要求 sample freshness、policy revision 和异步 rollout admission，判断为已有覆盖。

**Books 结论：** 已有覆盖到 [TRAIN-RLHF](../../../../books/part-04-training-system/31-rlhf.md)。

### [HaM-World: Soft-Hamiltonian World Models with Selective Memory for Planning](https://arxiv.org/html/2605.05951v1)

exact-v1 §4–8 把 world state 拆成 canonical `(q,p)` 与 context，用 Hamiltonian-like core、residual/control dynamics 和 selective memory 支撑规划；实验限于 DeepMind Control Suite、OOD perturbation 与 CEM。Ch25 新增状态/历史/动作 authority 分离和真实 observation correction，不把近似物理当作开放世界因果真值。

**Books 结论：** 整合到 [MULTIMODAL-WORLD-MODELS](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。

### [Towards Reliable LLM Evaluation: Correcting the Winner's Curse in Adaptive Benchmarking](https://arxiv.org/html/2605.05973v1)

机制边界：We study inference for this procedure-level target under explicit tuning budgets.。Method/identity locator：`https://arxiv.org/html/2605.05973v1 §3 Adaptive Benchmarking Model — mechanism: We study inference for this procedure-level target under explicit tuning budgets.`；evaluation locator：`https://arxiv.org/html/2605.05973v1 §4–§5 Experiments and Winner's-Curse Analysis — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.05973v1 §6 Discussion and Limitations — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.05973v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-TOWARDS-RELIABLE-LLM-EVALUATION-CORRECTING-THE-WINNER-S-CURSE-IN-ADAPTIV:start -->winner’s-curse 修正只在论文明确的 adaptive tuning budget、选择过程与统计假设下校准 procedure-level uncertainty；它不消除 contamination 或 evaluator bias。<!-- claim:SF-TOWARDS-RELIABLE-LLM-EVALUATION-CORRECTING-THE-WINNER-S-CURSE-IN-ADAPTIV:end -->
无法记录调参轨迹、选择次数或独立评估集时，冻结 holdout 与预注册 evaluation contract 仍是更可信基线。

**Books 结论：** 整合到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Requests of a Feather Must Flock Together: Batch Size vs. Prefix Homogeneity in LLM Inference](https://arxiv.org/html/2605.06046v1)

exact-v1 §4–6 显示大而异质的 batch 可能输给较小的 prefix-homogeneous batch，并以 RL scheduler 与 Chunked Hash Tree 联合控制队列和 prefix locality。vLLM/SGLang 结果受模型、硬件、prefix 分布与并发约束；Ch56 新增 batch size–locality–fairness 的联合决策及普通 continuous batching fallback。

**Books 结论：** 整合到 [INFER-SCHEDULING](../../../../books/part-05-inference-system/56-inference-scheduling.md)。

### [VibeServe: Can AI Agents Build Bespoke LLM Serving Systems?](https://arxiv.org/html/2605.06068v1)

机制边界：We propose VibeServe, the first agentic loop that generates entire LLM serving stacks end-to-end.。Method/identity locator：`https://arxiv.org/html/2605.06068v1 §3 VibeServe Design; §4 Agentic Search Loop — mechanism: We propose VibeServe, the first agentic loop that generates entire LLM serving stacks end-to-end.`；evaluation locator：`https://arxiv.org/html/2605.06068v1 §5 Evaluation — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.06068v1 §6 Limitations; §7 Conclusion — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.06068v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-VIBESERVE-CAN-AI-AGENTS-BUILD-BESPOKE-LLM-SERVING-SYSTEMS:start -->VibeServe 只证明 agent 能在论文审计的 search space 和 evaluator 中生成 serving stack；它没有证明产物具备生产 correctness、可移植性、安全性或长期可维护性。<!-- claim:SF-VIBESERVE-CAN-AI-AGENTS-BUILD-BESPOKE-LLM-SERVING-SYSTEMS:end -->
生产服务仍需已验证 engine/reference stack、行为测试、故障注入与人工 release gate；agent 产物只能作为候选。

**Books 结论：** 已有覆盖到 [INFER-TENSORRT-LLM](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。

### [Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training](https://arxiv.org/html/2605.06076v1)

exact-v1 §2–6 与 Appendix G 表明 mechanistic localization 会在 post-training 后漂移；静态定位图不能直接复用为新 checkpoint 的干预依据。论文只覆盖披露模型、任务与定位方法，不能证明所有机制完全迁移或完全失效；Ch66 已要求 measurement identity 随 checkpoint/revision 重验，判断为已有覆盖。

**Books 结论：** 已有覆盖到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Shallow Prefill, Deep Decoding: Efficient Long-Context Inference via Layer-Asymmetric KV Visibility](https://arxiv.org/html/2605.06105v1)

机制边界：We introduce \emph{Shallow Prefill, dEEp Decode} (SPEED), a phase-asymmetric KV-visibility policy that materializes non-anchor prompt-token KV states only in lower layers while keeping Decode-phase tokens full-depth.。Method/identity locator：`https://arxiv.org/html/2605.06105v1 §3 Layer-Asymmetric KV Visibility; §4 System Integration — mechanism: We introduce \emph{Shallow Prefill, dEEp Decode} (SPEED), a phase-asymmetric KV-visibility policy that materializes non-anchor prompt-token KV states only in lower layers while keeping Decode-phase tokens full-depth.`；evaluation locator：`https://arxiv.org/html/2605.06105v1 §5 Experiments — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.06105v1 §6 Limitations — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.06105v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-SHALLOW-PREFILL-DEEP-DECODING-EFFICIENT-LONG-CONTEXT-INFERENCE-VIA-LAYER:start -->SPEED 只在披露模型与长上下文任务中验证 prefill/decode 的 layer-asymmetric KV visibility；不能假定任意层、任务或模型都可无损省略 prompt KV。<!-- claim:SF-SHALLOW-PREFILL-DEEP-DECODING-EFFICIENT-LONG-CONTEXT-INFERENCE-VIA-LAYER:end -->
当 anchor 选择不稳定、质量回归不可接受或模型未经校准时，full-depth prefill 仍是 correctness fallback。

**Books 结论：** 已有覆盖到 [INFER-PREFILL](../../../../books/part-05-inference-system/43-prefill.md)。

### [BUILD-AND-FIND: An Effort-Aware Protocol for Evaluating Agent-Managed Codebases](https://arxiv.org/html/2605.06136v1)

机制边界：Even when strong agents nearly satisfy the visible behavioral objective, repositories can differ in how clearly they expose the intended behavior and design choices behind that behavior.。Method/identity locator：`https://arxiv.org/html/2605.06136v1 §3 Build-and-Find protocol; §4 effort metrics — mechanism: Even when strong agents nearly satisfy the visible behavioral objective, repositories can differ in how clearly they expose the intended behavior and design choices behind that behavior.`；evaluation locator：`https://arxiv.org/html/2605.06136v1 §5 Evaluation — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.06136v1 §6 Scope and limitations — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.06136v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-BUILD-AND-FIND-AN-EFFORT-AWARE-PROTOCOL-FOR-EVALUATING-AGENT-MANAGED-COD:start -->BUILD-AND-FIND 在披露 repository/task 中测量行为可见性与定位 effort；该协议不能单独证明代码语义正确、安全或可维护，也不是通用 coding-agent 排名。<!-- claim:SF-BUILD-AND-FIND-AN-EFFORT-AWARE-PROTOCOL-FOR-EVALUATING-AGENT-MANAGED-COD:end -->
行为测试、静态/动态安全检查与人工设计审阅仍需并列存在，尤其用于协议未覆盖的隐藏副作用。

**Books 结论：** 已有覆盖到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges](https://arxiv.org/html/2605.06161v1)

机制边界：LLM-as-a-Judge pipelines have become the de facto evaluator for agent safety, yet existing benchmarks treat their verdicts as ground-truth proxies without checking whether the verdicts depend on the agent's behavior or merely on how the evaluation policy happens…。Method/identity locator：`https://arxiv.org/html/2605.06161v1 §3 Policy Invariance Score and paired perturbations — mechanism: LLM-as-a-Judge pipelines have become the de facto evaluator for agent safety, yet existing benchmarks treat their verdicts as ground-truth proxies without checking whether the verdicts depend on the agent's behavior or merely on how the evaluation policy happens…`；evaluation locator：`https://arxiv.org/html/2605.06161v1 §4 Evaluation — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.06161v1 §5 Limitations and calibration caveats — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.06161v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-BEYOND-ACCURACY-POLICY-INVARIANCE-AS-A-RELIABILITY-TEST-FOR-LLM-SAFETY-J:start -->policy-invariance test 只检测 judge 在论文扰动合同下是否受 policy framing 影响；通过不等于 judge 正确或安全，失败也不能唯一定位因果机制。<!-- claim:SF-BEYOND-ACCURACY-POLICY-INVARIANCE-AS-A-RELIABILITY-TEST-FOR-LLM-SAFETY-J:end -->
具备 ground truth 或专家判断的场景仍应保留锚点，invariance 只能作为 evaluator sensitivity 的一条反证通道。

**Books 结论：** 整合到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [UniPrefill: Universal Long-Context Prefill Acceleration via Block-wise Dynamic Sparsification](https://arxiv.org/html/2605.06221v1)

机制边界：To this end, we propose UniPrefill, a prefill acceleration framework applicable to virtually any model architecture, which directly accelerates the model's computation at the token level.。Method/identity locator：`https://arxiv.org/html/2605.06221v1 §3 UniPrefill; §4 Continuous-Batching Integration — mechanism: To this end, we propose UniPrefill, a prefill acceleration framework applicable to virtually any model architecture, which directly accelerates the model's computation at the token level.`；evaluation locator：`https://arxiv.org/html/2605.06221v1 §5 Experiments — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.06221v1 §6 Ablations and Limitations — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.06221v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-UNIPREFILL-UNIVERSAL-LONG-CONTEXT-PREFILL-ACCELERATION-VIA-BLOCK-WISE-DY:start -->UniPrefill 只在披露模型、block policy 与 workload 上证明动态稀疏化可减少 prefill 计算；“universal”不等于所有架构、长度和质量约束下都获得净收益。<!-- claim:SF-UNIPREFILL-UNIVERSAL-LONG-CONTEXT-PREFILL-ACCELERATION-VIA-BLOCK-WISE-DY:end -->
短上下文、稀疏选择开销较高或质量门槛严格时，full prefill 与普通 continuous batching 仍是基线。

**Books 结论：** 已有覆盖到 [INFER-PREFILL](../../../../books/part-05-inference-system/43-prefill.md)。

### [Measuring Evaluation-Context Divergence in Open-Weight LLMs: A Paired-Prompt Protocol with Pilot Evidence of Alignment-Pipeline-Specific Heterogeneity](https://arxiv.org/html/2605.06327v1)

机制边界：We define evaluation-context divergence as an observable within-item change in behavior induced by framing a fixed task as an evaluation, a live deployment interaction, or a neutral request, and present a paired-prompt protocol that measures it in open-weight…。Method/identity locator：`https://arxiv.org/html/2605.06327v1 §2 Paired-Prompt Protocol; §3 Evaluation-Context Divergence — mechanism: We define evaluation-context divergence as an observable within-item change in behavior induced by framing a fixed task as an evaluation, a live deployment interaction, or a neutral request, and present a paired-prompt protocol that measures it in open-weight…`；evaluation locator：`https://arxiv.org/html/2605.06327v1 §4 Pilot Evaluation — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.06327v1 §5 Limitations; familiarity is only a contamination proxy — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.06327v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-MEASURING-EVALUATION-CONTEXT-DIVERGENCE-IN-OPEN-WEIGHT-LLMS-A-PAIRED-PRO:start -->paired-prompt pilot 只测得披露 open-weight models 对 evaluation framing 的行为差异；它不证明模型存在隐藏评测意识，也不能把差异因果归于特定 alignment pipeline。<!-- claim:SF-MEASURING-EVALUATION-CONTEXT-DIVERGENCE-IN-OPEN-WEIGHT-LLMS-A-PAIRED-PRO:end -->
盲测、held-out task 与 provider/version 固定仍是 evaluation 基线，paired framing 只提供敏感性检查。

**Books 结论：** 已有覆盖到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [MANTRA: Synthesizing SMT-Validated Compliance Benchmarks for Tool-Using LLM Agents](https://arxiv.org/html/2605.06334v1)

exact-v1 §3.1 先把自然语言 manual 与 tool schema 编译为 dependency graph、scenario 与 tool relevance；§3.2 独立生成 trace-level compliance checks 和 symbolic world model，§3.3 再用 bounded SMT search 查找二者冲突，执行 deterministic repair，并把无法自动消解的冲突交给 human fallback。§4 在 6 个领域、285 个任务和最长 50+ 页 manual 上比较 benchmark generation 与 agent execution；§5 明确讨论 automation、scope、evaluation coverage 与 benchmark correctness 的限制，Appendix B 给出 check grammar、world-model DSL 和 SMT encoding。

它证明的是“检查规则与有限 world model 在所述 DSL/边界内可机器检查并相互校验”，不证明原始 manual 无歧义、生成器覆盖所有业务语义、SMT model 等同真实环境，或受测 agent 在开放世界合规。短流程、规则少或语义仍需人工解释时，人工编写 assertions 与 outcome tests 成本更低；复杂长程流程才值得承担 DSL、solver、repair 和 manual-version 管理成本。Ch66 已经把 process compliance 与 outcome success 分开，并要求冻结 manual revision、required-state inventory 与 intermediate trace；Ch81 已把 verifier、runtime effect owner 和 human gate 分开，因此作者侧判定 No Change — Existing Coverage，以 PLATFORM-EVALUATION-SYSTEM 为 canonical owner、AGENT-WORKFLOW 只作 handoff，不写共享 Books。该判定仍需新一轮独立复核。

**Books 结论：** 已有覆盖到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [From Agent Loops to Deterministic Graphs: Execution Lineage for Reproducible AI-Native Work](https://arxiv.org/html/2605.06365v1)

机制边界：We introduce execution lineage: an execution model in which AI-native work is represented as a directed acyclic graph (DAG) of artifact-producing computations with explicit dependencies, stable intermediate boundaries, and identity-based replay.。Method/identity locator：`https://arxiv.org/html/2605.06365v1 §4 Deterministic Execution Graph; §5 lineage model — mechanism: We introduce execution lineage: an execution model in which AI-native work is represented as a directed acyclic graph (DAG) of artifact-producing computations with explicit dependencies, stable intermediate boundaries, and identity-based replay.`；evaluation locator：`https://arxiv.org/html/2605.06365v1 §8 Experiments — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.06365v1 §9.6 What This Paper Does Not Claim; §9.7 Limitations — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.06365v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-FROM-AGENT-LOOPS-TO-DETERMINISTIC-GRAPHS-EXECUTION-LINEAGE-FOR-REPRODUCI:start -->execution-lineage DAG 只对论文建模的 artifact boundary、dependency 与 replay identity 提供确定性；它不证明节点语义正确，也无法让外部副作用天然可重放。<!-- claim:SF-FROM-AGENT-LOOPS-TO-DETERMINISTIC-GRAPHS-EXECUTION-LINEAGE-FOR-REPRODUCI:end -->
涉及网络、人工审批或不可逆 effect 时仍需 receipt、幂等协议、补偿动作与独立 verification。

**Books 结论：** 已有覆盖到 [AGENT-WORKFLOW](../../../../books/part-07-agent/81-workflow.md)。

### [Constraining Host-Level Abuse in Self-Hosted Computer-Use Agents via TEE-Backed Isolation](https://arxiv.org/html/2605.06393v1)

机制边界：The proposed design keeps ordinary functionality on the constrained REE path, while protecting security-critical classification, authorization, binding, evidence generation, and selected execution-control decisions inside a cloud-native TEE-backed trusted operation plane.。Method/identity locator：`https://arxiv.org/html/2605.06393v1 §III Operation-Centric Threat Model; §IV TEE Trusted Plane — mechanism: The proposed design keeps ordinary functionality on the constrained REE path, while protecting security-critical classification, authorization, binding, evidence generation, and selected execution-control decisions inside a cloud-native TEE-backed trusted operation plane.`；evaluation locator：`https://arxiv.org/html/2605.06393v1 §V Prototype; §VI Evaluation — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.06393v1 §VII Security Analysis and Limitations — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.06393v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-CONSTRAINING-HOST-LEVEL-ABUSE-IN-SELF-HOSTED-COMPUTER-USE-AGENTS-VIA-TEE:start -->TEE trusted plane 只在论文 threat model 内保护列出的 classification、authorization、binding 与 evidence operations；它不覆盖 side channel、TEE compromise 或远端 effect authority。<!-- claim:SF-CONSTRAINING-HOST-LEVEL-ABUSE-IN-SELF-HOSTED-COMPUTER-USE-AGENTS-VIA-TEE:end -->
host sandbox、远端最小权限、独立凭证与人工 override 仍需保留，不能因存在 TEE 而下放全部控制权。

**Books 结论：** 已有覆盖到 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [PrefixGuard: From LLM-Agent Traces to Online Failure-Warning Monitors](https://arxiv.org/html/2605.06455v1)

机制边界：We introduce PrefixGuard, a trace-to-monitor framework with an offline StepView induction step followed by supervised monitor training.。Method/identity locator：`https://arxiv.org/html/2605.06455v1 §4 Method: prefix event extraction and monitors — mechanism: We introduce PrefixGuard, a trace-to-monitor framework with an offline StepView induction step followed by supervised monitor training.`；evaluation locator：`https://arxiv.org/html/2605.06455v1 §5 Experiments — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.06455v1 §6 Limitations and Conclusion — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.06455v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-PREFIXGUARD-FROM-LLM-AGENT-TRACES-TO-ONLINE-FAILURE-WARNING-MONITORS:start -->PrefixGuard 的 learned monitor 只对记录 trace distribution 与披露 failure labels 有效；它不保证识别 novel failure、对抗性轨迹或长期 drift。<!-- claim:SF-PREFIXGUARD-FROM-LLM-AGENT-TRACES-TO-ONLINE-FAILURE-WARNING-MONITORS:end -->
确定性 guard、权限边界与 human stop 仍是硬控制；learned warning 只能提供可校准的提前信号。

**Books 结论：** 已有覆盖到 [PLATFORM-MONITORING](../../../../books/part-06-ai-infrastructure/67-monitoring.md)。

### [Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management](https://arxiv.org/html/2605.06472v1)

机制边界：Experiments on three workflow benchmarks show that PBKV achieves up to $1.85\times$ speedup over LRU on dynamic workflows, and up to $1.26\times$ speedup over the SOTA baseline KVFlow on the static workflow.。Method/identity locator：`https://arxiv.org/html/2605.06472v1 §3 Workflow-Path Prediction; §4 KV Management — mechanism: Experiments on three workflow benchmarks show that PBKV achieves up to $1.85\times$ speedup over LRU on dynamic workflows, and up to $1.26\times$ speedup over the SOTA baseline KVFlow on the static workflow.`；evaluation locator：`https://arxiv.org/html/2605.06472v1 §5 Evaluation — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.06472v1 §6 Limitations and Conclusion — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.06472v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-EFFICIENT-SERVING-FOR-DYNAMIC-AGENT-WORKFLOWS-WITH-PREDICTION-BASED-KV-C:start -->PBKV 的收益只来自论文三个 workflow benchmark 上可预测的路径与 KV reuse；预测漂移、低重用或公平性约束可能使其劣于 LRU/静态策略。<!-- claim:SF-EFFICIENT-SERVING-FOR-DYNAMIC-AGENT-WORKFLOWS-WITH-PREDICTION-BASED-KV-C:end -->
路径不稳定或缺少可靠 workflow identity 时，LRU、显式静态 plan 与保守 eviction 仍是可解释 fallback。

**Books 结论：** 已有覆盖到 [INFER-KV-CACHE](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。

### [On the Implicit Reward Overfitting and the Low-rank Dynamics in RLVR](https://arxiv.org/html/2605.06523v1)

exact-v1 §2 用 periodic rank-1 substitution 干预训练后权重，区分 rank-1 reasoning component、其余知识成分与 train reward/test generalization 的分离；§3 检查非 rank-1 成分、不同线性层的 singular spectrum 与 heavy-tail 现象，§4 用 LoRA output-space alignment 和理论推导描述训练动态，§5 给出对应实验，§7 主动限制结论范围。Appendix A–C 补充算法关系和更多 singular-spectrum 结果。

该论文提供的是受限 mechanistic evidence：在作者模型、数学推理任务、RLVR recipe、decomposition 与 substitution protocol 中，训练 reward 不是泛化的充分统计量，低秩方向也不能被解释为保存模型全部知识。它没有证明所有 RLVR 都由 rank-1 成分支配，没有建立 low-rank dynamics 与 generalization 的普遍因果关系，也没有给出可以直接接管训练控制面的阈值。普通 reward/held-out evaluation、checkpoint slice 与 optimizer/gradient telemetry 仍应并存。Ch33 已经把训练 reward 与 held-out/generalization 分离，把 checkpoint slice、turnover 与 optimizer/gradient telemetry 作为并列诊断，并明确诊断信号不能直接拥有 update control；该论文的 rank-1 substitution 与 spectrum 只是在特定设置中的解释性案例，不改变现有设计结论。因此作者侧判定 No Change — Existing Coverage，仍待新一轮独立复核，本轮不写共享 Books。

**Books 结论：** 已有覆盖到 [TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md)。

### [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/html/2605.06527v1)

机制边界：To rigorously evaluate this capability, we introduce STALE, a benchmark of 400 expert-validated conflict scenarios (1,200 evaluation queries across three probing dimensions) spanning over 100 everyday topics with contexts up to 150K tokens.。Method/identity locator：`https://arxiv.org/html/2605.06527v1 §3 Memory-Validity Model; §4 STALE — mechanism: To rigorously evaluate this capability, we introduce STALE, a benchmark of 400 expert-validated conflict scenarios (1,200 evaluation queries across three probing dimensions) spanning over 100 everyday topics with contexts up to 150K tokens.`；evaluation locator：`https://arxiv.org/html/2605.06527v1 §5 Evaluation — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.06527v1 §6 Limitations — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.06527v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-STALE-CAN-LLM-AGENTS-KNOW-WHEN-THEIR-MEMORIES-ARE-NO-LONGER-VALID:start -->STALE 的 400 个 conflict scenario 与 150K context 只证明特定模型识别旧记忆冲突的能力边界；benchmark 本身不是通用 truth-maintenance 机制。<!-- claim:SF-STALE-CAN-LLM-AGENTS-KNOW-WHEN-THEIR-MEMORIES-ARE-NO-LONGER-VALID:end -->
生产记忆仍需 provenance、revision、TTL、retrieval-time validation 与可撤销写入，不能只依赖模型自判。

**Books 结论：** 已有覆盖到 [AGENT-MEMORY](../../../../books/part-07-agent/77-memory.md)。

### [CCL-Bench 1.0: A Trace-Based Benchmark for LLM Infrastructure](https://arxiv.org/html/2605.06544v1)

机制边界：We present CCL-Bench, a trace-based benchmark that addresses the limitations of existing benchmarks by recording reusable evidence for every ML workload.。Method/identity locator：`https://arxiv.org/html/2605.06544v1 §3 Trace-Based Benchmark Contract; §4 Workloads — mechanism: We present CCL-Bench, a trace-based benchmark that addresses the limitations of existing benchmarks by recording reusable evidence for every ML workload.`；evaluation locator：`https://arxiv.org/html/2605.06544v1 §4 Evaluation; Appendix C run scripts — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.06544v1 §5 Discussion and Limitations — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.06544v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-CCL-BENCH-1-0-A-TRACE-BASED-BENCHMARK-FOR-LLM-INFRASTRUCTURE:start -->CCL-Bench 的 trace contract 只为披露 workload 记录可复用运行证据；它不证明这些 workload 代表生产流量，也不能跨硬件直接比较未归一化结果。<!-- claim:SF-CCL-BENCH-1-0-A-TRACE-BASED-BENCHMARK-FOR-LLM-INFRASTRUCTURE:end -->
目标系统仍需 workload-specific replay、版本固定和 SLO 绑定；合成/通用 trace 只作补充。

**Books 结论：** 已有覆盖到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [The Structural Origin of Attention Sink: Variance Discrepancy, Super Neurons, and Dimension Disparity](https://arxiv.org/html/2605.06611v1)

exact-v1 §4–6 通过受控干预把 attention sink 与 value variance discrepancy、FFN super-neuron、dimension disparity 联系起来，并给出 head-wise RMSNorm proof-of-concept。它是条件性机制假说，不是所有 sink 的统一因果解释；Ch22 新增分层诊断、质量验收与保留 BOS/anchor 的 fallback。

**Books 结论：** 整合到 [MODEL-LONG-CONTEXT](../../../../books/part-02-model/22-long-context.md)。

### [Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents](https://arxiv.org/html/2605.06635v1)

机制边界：We introduce the first source attribution evaluation framework that uses a reproducible AST parser to extract and evaluate inline citations from LLM-generated Markdown reports at scale.。Method/identity locator：`https://arxiv.org/html/2605.06635v1 §2 Attribution Taxonomy; §3 citation parsing and verification — mechanism: We introduce the first source attribution evaluation framework that uses a reproducible AST parser to extract and evaluate inline citations from LLM-generated Markdown reports at scale.`；evaluation locator：`https://arxiv.org/html/2605.06635v1 §4 Evaluation — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.06635v1 §5 Limitations — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.06635v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-CITED-BUT-NOT-VERIFIED-PARSING-AND-EVALUATING-SOURCE-ATTRIBUTION-IN-LLM-:start -->AST parser 只可靠提取 Markdown 中满足语法的 inline citation 并执行配置检查；它不证明被引来源真实、claim entailment 成立或材料未被曲解。<!-- claim:SF-CITED-BUT-NOT-VERIFIED-PARSING-AND-EVALUATING-SOURCE-ATTRIBUTION-IN-LLM-:end -->
高风险结论仍需 claim-level source verification、版本定位与人工反证；语法 attribution 只是第一层 gate。

**Books 结论：** 已有覆盖到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Optimizer-Model Consistency: Full Finetuning with the Same Optimizer as Pretraining Forgets Less](https://arxiv.org/html/2605.06654v1)

exact-v1 §6 与附录比较 pretraining→full-finetuning 的 optimizer continuity，作者设置中保持同类 optimizer 能减少部分遗忘；Muon 在所测 reasoning SFT 上可能因 memorization 更差。它不支持通用 optimizer 排名；Ch29 新增 optimizer lineage、状态继承/重置与目标/retain 双臂验收。

**Books 结论：** 整合到 [TRAIN-SFT](../../../../books/part-04-training-system/29-sft.md)。

### [Why Global LLM Leaderboards Are Misleading: Small Portfolios for Heterogeneous Supervised ML](https://arxiv.org/html/2605.06656v1)

exact-v1 §3/§5 以 89K Arena comparisons、116 languages 与 52 LLMs 说明全局 Bradley–Terry 会抵消 coherent subgroup 偏好，并提出覆盖群组的小 portfolio。它不证明未来人群或生产最优选择；Ch66 新增 slice identity、异质性区间/portfolio 与 release owner 分责。

**Books 结论：** 整合到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [UniPool: A Globally Shared Expert Pool for Mixture-of-Experts](https://arxiv.org/html/2605.06665v1)

机制边界：Motivated by this redundancy, we propose UniPool, an MoE architecture that treats expert capacity as a global architectural budget by replacing per-layer expert ownership with a single shared pool accessed by independent per-layer routers.。Method/identity locator：`https://arxiv.org/html/2605.06665v1 §3 Routing Probe; §4 UniPool; §5 Pool-Level Balance — mechanism: Motivated by this redundancy, we propose UniPool, an MoE architecture that treats expert capacity as a global architectural budget by replacing per-layer expert ownership with a single shared pool accessed by independent per-layer routers.`；evaluation locator：`https://arxiv.org/html/2605.06665v1 §6 Experiments — disclosed evaluation scope only`；counterevidence/limitations：`https://arxiv.org/html/2605.06665v1 §7 Analysis and Limitations — no generalization beyond disclosed workload/model/evaluator`；artifact locator：`https://arxiv.org/html/2605.06665v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-UNIPOOL-A-GLOBALLY-SHARED-EXPERT-POOL-FOR-MIXTURE-OF-EXPERTS:start -->UniPool 只在披露模型、router 与 balance objective 下证明共享 expert pool 可减少 per-layer 冗余；它不证明所有层都应失去独立 expert ownership。<!-- claim:SF-UNIPOOL-A-GLOBALLY-SHARED-EXPERT-POOL-FOR-MIXTURE-OF-EXPERTS:end -->
层间专业化强、路由干扰或跨设备通信代价高时，per-layer MoE 甚至 dense FFN 仍可能更稳。

**Books 结论：** 已有覆盖到 [MODEL-MOE](../../../../books/part-02-model/21-moe.md)。

<!-- may08-author-reopen:start -->

**重开 24 项的逐篇证据如下。**

### [Budgeted Attention Allocation: Cost-Conditioned Compute Control for Efficient Transformers](https://arxiv.org/html/2605.05697v1)

- **机制：** §3 训练 budget-conditioned、单调的 layer/head gate，以 soft cost regularization 学习多预算 operating point；部署时转为 hard top-k mask，必要时从 dense warm start 做 hard-gate adaptation。
- **评价：** §5–6 覆盖 synthetic task、AG News/DBpedia 子集、BERT-Tiny/BERT-Mini 与 DistilBERT pilot；仅有限 CPU/GPU hard-gate latency，主要 cost 仍为估算。
- **未证明：** §9 明确 soft gate cost 不等于 wall-clock；A100 eager execution 不自动加速，数据、seed 与模型规模有限，dense warm start 还增加训练成本。

**Books 结论：** `Integrate — Applied → MODEL-SELF-ATTENTION`。共享正文已写入，并由此前独立 reviewer 通过。

### [Inference-Time Budget Control for LLM Search Agents](https://arxiv.org/html/2605.05701v1)

- **机制：** §4 先由 task-level VOI controller 在 Search/Decompose/Answer 间分配 tool/token budget，再由保守 finalizer 只修复 typed answer-form 错误；budget penalty、value-per-cost 与 deterministic guard 共同约束动作。
- **评价：** §5 使用 Qwen3-32B、Qwen3.5-122B 与 GPT-5.4-Mini，在 HotpotQA、2Wiki、MuSiQue、Bamboogle 的硬预算下比较多种 search controller；高预算并不单调占优，BATS 在部分格点仍有竞争力。
- **未证明：** §6 说明 controller 不能修复错误 retrieval 或 unresolved bridge，且 backbone、预算与任务改变会改变收益。

**Books 结论：** 已有覆盖到 [AGENT-PLANNING](../../../../books/part-07-agent/79-planning.md)；对读依据和精确证据定位见 [作者侧 exact-v1 完成记录](../_sources/daily-20260508/AUTHOR_EXACT_V1_COMPLETION.md)。

### [Selective Rollout: Mid-Trajectory Termination for Multi-Sample Agent RL](https://arxiv.org/html/2605.05802v1)

- **机制：** §3 在固定 prefix 长度 `K=10` 比较组内轨迹 edit divergence；低 divergence 组在 rollout 中途终止，位于 pre-rollout filtering 与 post-rollout filtering 之间，直接改变 trajectory lifecycle。
- **评价：** §3.1、§4–5 使用 ALFWorld、Qwen2.5-7B-Instruct、group size 8、horizon 30，并做 rollout-only、off-policy 与 on-policy 三层验证；低 divergence 可捕获部分 all-success/all-fail 组，但对 high-divergence all-fail 无能为力，online 改善是方向性而非显著性定论。
- **未证明：** 固定模型、环境、`K` 与少量 seed 不证明跨任务最优 gate；错误早停会删掉稀有学习信号，gate 必须与 policy revision 和完整组身份绑定。

**Books 结论：** `Integrate — Applied → TRAIN-GRPO`。共享正文已写入，并由此前独立 reviewer 通过。

### [VisMMOE: Exploiting Visual-Expert Affinity for Efficient Visual-Language MoE Offloading](https://arxiv.org/html/2605.05899v1)

- **机制：** §3 先压缩 visual tokens 以缩小 expert working set，再用 compression-guided lookahead predictor 驱动 dynamic expert cache 与异步 CPU→GPU prefetch；miss 时仍由 CPU fallback 执行真实 expert。
- **评价：** §4 在 Qwen3-VL-30B-A3B、DeepSeek-VL2 与 A100-40GB、RTX3090-24GB、Jetson Orin 32GB 上报告 MME/OCRBench/POPE/MMBench 质量及 prefill/decode 时间，并给出 compressor、predictor、cache 的消融。
- **未证明：** 结果绑定两类 VL-MoE、特定 offload runtime 与硬件；Orin 路径使用 OS swap，未证明生产并发、tail SLO 或任意 modality/router 分布收益。

**Books 结论：** `Integrate — Applied → INFER-TENSORRT-LLM`。共享正文已写入，并由此前独立 reviewer 通过。

### [Towards Generation-Efficient Uncertainty Estimation in Large Language Models](https://arxiv.org/html/2605.06053v1)

- **机制：** §4.1 用 partial generation 的 Logit Magnitude 配合 early stop/top-M 估计不确定性；§4.2 用冻结 encoder 与 MLP 从输入预测由 Logit Magnitude 产生的 pseudo-label，把观测时点前移到生成前。
- **评价：** §5 在 CoQA、NewsQA、emrQA 与 Qwen/Gemma/Llama family 上比较 AUROC、AURAC、balanced accuracy 和生成 token 数；主要硬件是 RTX 6000 Ada 48GB，较大配置用 96GB。
- **未证明：** §6/附录只覆盖开放式 QA；Llama3-emrQA 出现 calibration failure，长文生成、domain shift 与生产 abstention SLO 未被充分验证。

**Books 结论：** 已有覆盖到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；对读依据和精确证据定位见 [作者侧 exact-v1 完成记录](../_sources/daily-20260508/AUTHOR_EXACT_V1_COMPLETION.md)。

### [Normalized Architectures are Natively 4-Bit](https://arxiv.org/html/2605.06067v1)

- **机制：** §3–4 将 hypersphere-normalized geometry 的 constructive signal accumulation 与量化 SNR、较平坦 loss landscape 联系起来，使 NVFP4 end-to-end training 可省去随机 Hadamard 与逐 tensor scaling；这是 architecture–precision 共设计，而非普通 PTQ。
- **评价：** §5/Appendix C 覆盖 1.2B dense 1T tokens、hybrid Mamba-Transformer MoE 400M/600M 与 3B/30B 500B tokens，并在 Blackwell 上报告学习率鲁棒性和加速。
- **未证明：** Appendix E 说明主分析集中在较小模型/宽度，3B/30B 训练 horizon 远短于超大规模生产训练；正相关来源仍未完全解释。

**Books 结论：** `Integrate — Applied → TRAIN-PRETRAINING`。共享正文已写入，并由此前独立 reviewer 通过。

### [Policy-Guided Stepwise Model Routing for Cost-Effective Reasoning](https://arxiv.org/html/2605.06116v1)

- **机制：** §3–4 将每个 reasoning step 的模型选择写成 CMDP，用 V-trace、trust-region constrained policy learning 与联合阈值校准控制成本/相对正确性；verifier 只在训练中提供信号。
- **评价：** §5 在 GSM8K、MATH500、OmniMath 上比较 Qwen2.5 Math 小/大模型与 Qwen→GPT-4.1-mini，开放模型路由较稳定，跨 API 路径受 top-logprob 与格式限制且未报告直接 latency。
- **未证明：** 证据限数学推理与所列模型；confidence proxy、API 可见性和阈值都可能漂移，未证明跨域或生产 SLO。

**Books 结论：** 已有覆盖到 [INFER-SCHEDULING](../../../../books/part-05-inference-system/56-inference-scheduling.md)；对读依据和精确证据定位见 [作者侧 exact-v1 完成记录](../_sources/daily-20260508/AUTHOR_EXACT_V1_COMPLETION.md)。

### [Breaking, Stale, or Missing? Benchmarking Coding Agents on Project-Level Test Evolution](https://arxiv.org/html/2605.06125v1)

- **机制：** §1–2 将 project-level test evolution 分为 breaking、stale、missing 三态；测试能运行只证明 breaking 被修复，不能证明需求变化后的语义 coverage 仍存在。
- **评价：** §2–4 构造 314 个实例、10 个 Java/Defects4J 项目和七种 Agent 配置，分别测 identification 与 update；stale/missing 是主要盲点。
- **未证明：** §6 指出 developer patch 不是唯一正确 test evolution，项目/语言范围有限，coverage overlap 只是 construct proxy。

**Books 结论：** `Integrate — Applied → PLATFORM-EVALUATION-SYSTEM`。共享正文已写入，并由此前独立 reviewer 通过。

### [Stateful Agent Backdoor](https://arxiv.org/html/2605.06158v1)

- **机制：** §3–4 将持久读写组件作为跨 session key-value state，用 Mealy machine 把攻击分解成多个单次看似无害的 sub-backdoor transition。
- **评价：** §5 覆盖四个模型、四类工具、1000 trajectories、五会话 episode，并检查主链、branch-and-merge 与 note-based 变体。
- **未证明：** §6.4 依赖共享 R/W channel、跨会话可见性与训练成功；容量、拓扑和 cascade attenuation 会限制攻击，不证明所有持久 Agent 都可同样后门化。

**Books 结论：** 已有覆盖到 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)；对读依据和精确证据定位见 [作者侧 exact-v1 完成记录](../_sources/daily-20260508/AUTHOR_EXACT_V1_COMPLETION.md)。

### [ClawGuard: Out-of-Band Detection of LLM Agent Workflow Hijacking via EM Side Channel](https://arxiv.org/html/2605.06205v1)

- **机制：** §V 用 host 外 SDR 采集 EM 与 temperature side channel，先粗粒度识别 workload、再细粒度恢复 skill sequence，形成不依赖被监控 host telemetry 的 evidence plane。
- **评价：** §VI 在 laptop/Raspberry Pi、16 benign 与 22 attack skills 上做 prototype、LOCO CV、robustness/transfer/cost；主语料 12,232 records/7.82TB。
- **未证明：** §VIII 显示 flat 16-class macro-F1 很低，近似资源模式、adaptive mimicking、短攻击、DVFS 和设备/日期漂移均会失效；只证明单设备 feasibility。

**Books 结论：** 已有覆盖到 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)；对读依据和精确证据定位见 [作者侧 exact-v1 完成记录](../_sources/daily-20260508/AUTHOR_EXACT_V1_COMPLETION.md)。

### [Federation of Experts: Communication Efficient Distributed Inference for Large Language Models](https://arxiv.org/html/2605.06206v1)

- **机制：** §3 按独立 expert/KV-head group 重构每层，使全局 all-to-all 变为 group 内 all-to-all 与 group 间 all-reduce；这是模型架构改变通信图，而非仅改变 placement。
- **评价：** §4 在 1B/7B、单节点 8×H100 与双节点 InfiniBand、FlexServe/LongBench Poisson workload 下测 forward、TTFT、TBT、负载和生成质量。
- **未证明：** §5 说明单 GPU 只有新增 all-reduce、无收益；证据依赖同构拓扑、需要重新训练，未覆盖更大模型、异构 fabric 与长期质量。

**Books 结论：** `Integrate — Applied → MODEL-MOE`。共享正文已写入，并由此前独立 reviewer 通过。

### [Correct Code, Vulnerable Dependencies: A Large Scale Measurement Study of LLM-Specified Library Versions](https://arxiv.org/html/2605.06279v1)

- **机制：** §3–4 把模型生成的 dependency version pin 单独送入 OSV、隔离 uv environment、static typing 与动态 tests；代码正确与 dependency 安全/兼容被拆成不同 admission evidence。
- **评价：** §4–6 覆盖 10 个 LLM、1000 PinTrace tasks 和 BigCodeBench 子集，比较 prompt mode、漏洞暴露、版本兼容与 mitigation probe。
- **未证明：** §8 限于 PyPI/Python 与固定时间锚点，provider 默认参数和 cutoff 部分为推断；measurement 不证明所有模型存在同一因果偏差。

**Books 结论：** 已有覆盖到 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)；对读依据和精确证据定位见 [作者侧 exact-v1 完成记录](../_sources/daily-20260508/AUTHOR_EXACT_V1_COMPLETION.md)。

### [A Regime Theory of Controller Class Selection for LLM Action Decisions](https://arxiv.org/html/2605.06339v1)

- **机制：** §2 在 fixed、partition、instance 与 prior-gated controller class 间做有限样本选择，并用 residual mass、样本数和 partition geometry 判断复杂 router 是否可辨识。
- **评价：** §3/Appendix C–E 在 SMS Spam、HallusionBench、A-OKVQA、FOLIO 与受控 synthetic setting 中做 nested cross-validation；TextVQA 的 prior gate 另作补充。
- **未证明：** Appendix A 说明结论依赖 action/loss/features/judge；gold rationale branch 不可部署，单一 judge 与少量 benchmark 不证明通用 class boundary。

**Books 结论：** 已有覆盖到 [INFER-SCHEDULING](../../../../books/part-05-inference-system/56-inference-scheduling.md)；对读依据和精确证据定位见 [作者侧 exact-v1 完成记录](../_sources/daily-20260508/AUTHOR_EXACT_V1_COMPLETION.md)。

### [Is Escalation Worth It? A Decision-Theoretic Characterization of LLM Cascades](https://arxiv.org/html/2605.06350v1)

- **机制：** §3–5 推导 k-model threshold cascade 的累计 cost/quality、pairwise envelope、shadow price 与 marginal quality-per-cost；cascade 必须先支付廉价模型成本，而 pre-generation router 可直接选择强模型。
- **评价：** §6 用八个模型、五家 provider 和 MMLU、TriviaQA、MATH、SimpleQA、LiveCodeBench，做 50 个 calibration/test split；learned pre-generation router 在 4/5 数据集更优，TriviaQA 是反例。
- **未证明：** 只覆盖 deterministic threshold cascade、所列 pool 与 token price；没有 latency、长输出和丰富 hybrid router 结论，不能宣称 cascade 普遍劣于 router。

**Books 结论：** `Integrate — Applied → INFER-SCHEDULING`。共享正文已写入，并由此前独立 reviewer 通过。

### [Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](https://arxiv.org/html/2605.06388v1)

- **机制：** §2–5 在 action-conditioned latent diffusion 中分离 reconstruction-aligned 与 semantic encoder，并分别检验 action recoverability、task semantics、visual fidelity、planning 与 policy-in-world-model。
- **评价：** §3–4 使用 Bridge V2、CEM planning、OpenVLA 固定 policy、inverse dynamics、success classifier 与 VLM consensus；不同 latent 在视觉和 policy relevance 上排序不同。
- **未证明：** §7 限于单 embodiment/Bridge V2，固定 policy evaluation 不是 policy improvement 或 sim-to-real，VLM judge 也可能偏置。

**Books 结论：** 已有覆盖到 [MULTIMODAL-WORLD-MODELS](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；对读依据和精确证据定位见 [作者侧 exact-v1 完成记录](../_sources/daily-20260508/AUTHOR_EXACT_V1_COMPLETION.md)。

### [SparseForge: Efficient Semi-Structured LLM Sparsification via Annealing of Hessian-Guided Soft-Mask](https://arxiv.org/html/2605.06402v1)

- **机制：** §4 联合优化 weights 与 soft mask，用 Hessian-guided structured target 和 progressive quenching 将可训练稀疏性收敛到硬件可执行 2:4 mask；遍历/annealing 是算法语义的一部分。
- **评价：** §5/Appendix A–C 覆盖 GPT-2、OPT、LLaMA2、Qwen3、DeepSeek-MoE 的 124M–16B 模型与 L20A；给出 PPL/zero-shot、消融和特定 2:4 端到端 speedup。
- **未证明：** Appendix D 说明语料、模型和 mask family 范围有限；硬件支持不等于所有 serving shape/并发都加速，恢复成本也未被通用摊销。

**Books 结论：** `Integrate — Applied → INFER-TENSORRT-LLM`。共享正文已写入，并由此前独立 reviewer 通过。

### [Constraint Decay: The Fragility of LLM Agents in Backend Code Generation](https://arxiv.org/html/2605.06445v1)

- **机制：** §3 固定 functional spec，逐步增加 architecture、database、ORM 等 structural constraints；验收取 behavioral tests 与 static verifier 的交集。
- **评价：** §4–5 覆盖八种 framework、Mini-SWE/OpenHands、多模型和 generation/feature implementation task，观察 constraint load 与 framework sensitivity。
- **未证明：** Appendix C–G 说明 static regex verifier 可能误判，ground truth 不是唯一实现，子集和成本限制约束外推。

**Books 结论：** 已有覆盖到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；对读依据和精确证据定位见 [作者侧 exact-v1 完成记录](../_sources/daily-20260508/AUTHOR_EXACT_V1_COMPLETION.md)。

### [Beyond Task Success: Measuring Workflow Fidelity in LLM-Based Agentic Payment Systems](https://arxiv.org/pdf/2605.06457v1.pdf)

- **机制：** §3 将 expected/observed trajectory 转成 transition multiset，以 Transition Recall、Transition Precision 及其 F1 定义 Agentic Success Rate；最终 task success 与 handoff set 都可能掩盖 checkpoint skip。
- **评价：** §3–4 在 HMASP payment workflow、18 个模型、1000 points×5 repeats（90,000 instances）下比较 TSR/HF1/ASR，并用 prompt refinement 与 deterministic routing guard 做诊断性修复。
- **未证明：** 单一支付 workflow、固定 expected path 与 bigram/multiset metric 不能覆盖全部长程顺序、状态语义或多合法路径；修复混合 prompt 与 guard，不能把收益归因给 metric 本身。

**Books 结论：** 已有覆盖到 [AGENT-WORKFLOW](../../../../books/part-07-agent/81-workflow.md)；对读依据和精确证据定位见 [作者侧 exact-v1 完成记录](../_sources/daily-20260508/AUTHOR_EXACT_V1_COMPLETION.md)。

### [OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation](https://arxiv.org/html/2605.06481v1)

- **机制：** §3 用 persistent object-slot address 维持跨视角 identity，同时把 mutable content、action chunk 与 per-object next state 分开；address 参与每层 attention，避免把对象身份与瞬时外观合并。
- **评价：** §4 在 LIBERO、SimplerEnv、LIBERO-Plus 做三 seed、消融、视觉/对象鲁棒性和 latency；附录披露多阶段训练与组件耗时。
- **未证明：** 证据以 simulation/visual matching 为主，不证明真实物理安全；地址依赖 detection/tracking 和 slot count，frozen perception 约 95ms、trunk/head 约 5.6ms，实时瓶颈并未消失。

**Books 结论：** `Integrate — Applied → MULTIMODAL-WORLD-MODELS`。共享正文已写入，并由此前独立 reviewer 通过。

### [Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors](https://arxiv.org/html/2605.06490v1)

- **机制：** §3 用 deterministic environment state 同时标记 task completion 与是否采用 policy-violating shortcut，并以 controlled variants 改变 shortcut usefulness/necessity。
- **评价：** 七任务、八 variants、三 repeats、十模型，共 1680 runs；基础发生率较低，环境激励比 verbal stakes 更能改变 shortcut 行为。
- **未证明：** §5 明确 behavior 不等于 latent goal；短时 terminal sandbox 不含长期制度、multi-agent 或不可逆副作用，样本量、evaluation awareness 与 provider drift 均限制结论。

**Books 结论：** 已有覆盖到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；对读依据和精确证据定位见 [作者侧 exact-v1 完成记录](../_sources/daily-20260508/AUTHOR_EXACT_V1_COMPLETION.md)。

### [Long Context Pre-Training with Lighthouse Attention](https://arxiv.org/html/2605.06554v1)

- **机制：** §3–5 在 stock attention kernel 外构建 multi-resolution QKV pyramid，selection 后 gather→FlashAttention→scatter；训练末期使用同一 optimizer/dataloader 恢复 dense SDPA，使稀疏训练路径与 dense deployment artifact 分离。
- **评价：** §6 在 530M、C4、98K context、50B tokens、B200 上比较 scaling、recoverability 与 throughput，并扩展到多节点/1M context；作者报告 ≥100K 下约 1.4–1.7× training speed。
- **未证明：** 所有 query 同时存在，因此该路径不兼容 autoregressive decode；下游结果只在 dense resume 后获得，内部 attention 对选择后序列仍为二次复杂度，serving integration 未证明。

**Books 结论：** `Integrate — Applied → TRAIN-PRETRAINING`。共享正文已写入，并由此前独立 reviewer 通过。

### [SkillOS: Learning Skill Curation for Self-Evolving Agents](https://arxiv.org/html/2605.06614v1)

- **机制：** §3 分离 frozen executor、RL-trained skill curator 与 external SkillRepo；curator 跨 grouped task stream 写入/更新 skills，用未来任务结果优化写入策略。
- **评价：** §4–5 在 ALFWorld、WebShop、DeepMath、Qwen3-8B curator 与多种 frozen executor 上比较 ReasoningBank/MemP，并在 16×H100/verl 配置训练。
- **未证明：** Appendix D 说明 BM25 retrieval、单 Markdown skill、冻结 executor miscalibration 与联合优化成本；未覆盖脚本/资源、层次 skill 或安全授权。

**Books 结论：** 已有覆盖到 [AGENT-MEMORY](../../../../books/part-07-agent/77-memory.md)；对读依据和精确证据定位见 [作者侧 exact-v1 完成记录](../_sources/daily-20260508/AUTHOR_EXACT_V1_COMPLETION.md)。

### [Recursive Agent Optimization](https://arxiv.org/html/2605.06639v1)

- **机制：** §2 让同一 shared policy 在递归树的所有节点决定是否 delegation、怎样写 subtask、怎样 aggregate；训练加入 subagent reward 与 inverse-frequency depth weighting，使递归本身成为被优化的 inference-time scaling policy。
- **评价：** §3–5 覆盖 TextCraft-Synth、Oolong-Real、DeepDive，并报告 context chunking、并行/深度使用和消融；DeepDive 的披露结果从 0.24 提升到 0.40。
- **未证明：** §7/Appendix A 说明需要 per-domain training，子任务需与父任务相似，recursive rollout 昂贵，未覆盖 heterogeneous agents、权限或安全。

**Books 结论：** `Integrate — Applied → AGENT-MULTI-AGENT`。共享正文已写入，并由此前独立 reviewer 通过。

### [When No Benchmark Exists: Validating Comparative LLM Safety Scoring Without Ground-Truth Labels](https://arxiv.org/html/2605.06652v1)

- **机制：** §3–6 将 scenario、rubric、auditor、judge、target 与 sampling 固定为 measurement instrument；无 ground-truth label 时只通过 known contrast、target-driven variance 与 rerun stability 建立比较有效性链。
- **评价：** §4–7 使用本地 Qwen ladder、abliterated targets、八场景 Norwegian safety/legal pack 与 SimpleAudit/Petri，比较 judge–auditor 配置、critical-miss agreement、稳定性和 token cost。
- **未证明：** §9 明确 validation chain 是必要而非充分条件；scenario construct 与 auditor 支配结果，范围有限，不能把 comparative score 升级为 safety certification。

**Books 结论：** `Integrate — Applied → PLATFORM-EVALUATION-SYSTEM`。共享正文已写入，并由此前独立 reviewer 通过。

<!-- may08-author-reopen:end -->

<!-- may08-denominator-challenge:start -->

### [PARNESS: A Paper Harness for End-to-End Automated Scientific Research with Dynamic Workflows, Full-Text Indexing, and Cross-Run Knowledge Accumulation](https://arxiv.org/html/2605.05258v1)

- **机制：** §5.1–5.3、§6.2/§6.3/§6.7 将 workflow definition 固化为可编辑 YAML DAG，以四字段 Agent contract、typed verifier output、全文/图表索引及跨运行知识图分离定义态、执行态、验证态和 durable knowledge。
- **评价：** §8 验证控制流执行、恢复与系统测试，证明的是 workflow harness 的可运行性与状态可追踪性，不是科学研究质量优于其他系统。
- **未证明：** §9 没有共享任务上的 head-to-head、最终论文的人类质量评价或 cognitive-role ablation；不能据此声称自动研究质量普遍提高。

**Books 结论：** `No Change — Existing Coverage`。现有 [AGENT-WORKFLOW](../../../../books/part-07-agent/81-workflow.md) 已拥有 editable/versioned DAG、typed transition、template/realized graph、replay 与 rollback；该文是具体实现证据，不新增 owner。

### [ZAYA1-8B Technical Report](https://arxiv.org/html/2605.05365v1)

- **机制：** §VI 的 Markovian RSA 把多轮 reasoning 的跨轮状态压成固定 tail，并把单条不断增长的 decode 改为有界 active context 的 batched stages；§IV 同时要求 rollout engine 与 trainer 在 BF16/选择性 FP32 下保持数值身份。
- **评价：** 报告验证披露的 8B 系统与多阶段 reasoning 配置；bounded active context 不等于 bounded total work，且缺少与所有 full-chain alternative 的 matched end-to-end comparison。
- **未证明：** §VII 限于 8B 与 DP+CP，指出 stale/mixed policy 配合 KL-in-reward 可引入 length bias；不能外推到其他规模、拓扑或通用成本收益。

**Books 结论：** `Integrate — Applied → INFER-SCHEDULING`。Ch56“长推理可以把跨轮状态与完整历史分开”已把 round boundary、carried tail、batch ownership、总 decode 成本与 full-history fallback 放在同一机制链。

### [Weight-Decay Turns Transformer Loss Landscapes Villani: Functional-Analytic Foundations for Optimization and Generalization](https://arxiv.org/html/2605.06599v1)

- **机制：** Theorem 1 在 bounded input 与 `lambda > 0` 等假设下，把 regularized Transformer loss 的 coercivity/Villani 条件连接到 log-Sobolev、Poincaré 及 Langevin/PAC-Bayes 边界。
- **评价：** §VI 只在 GPT-Neo-125M、Penn Treebank/WikiText-103、单 A100-80GB、BF16 加 FP32 master weights 上给出实验支持。
- **未证明：** §VII-A 明确限于 decoder-only、uniform decay 与 tuned temperature，常数依赖 `lambda`、维度和序列长度，高维界较松且未验证 7B 以上规模。

**Books 结论：** `No Change — Existing Coverage`。现有 [TRAIN-PRETRAINING](../../../../books/part-04-training-system/28-pretraining.md) 已把 weight decay 放在 geometry、curvature、regularization 与稳定性条件中；该 theorem 收紧证据边界但不改变设计路线。

### [When and Why SignSGD Outperforms SGD: A Theoretical Study Based on ell-1-norm Lower Bounds](https://arxiv.org/html/2605.06615v1)

- **机制：** §3–4 在 ell-1 stationarity、ell-infinity smoothness 与 coordinate-separable sparse noise 下比较 SignSGD 与 SGD，并给出连接 Muon 的 matrix analogue；结论是条件化 optimizer branch，不是无条件排名。
- **评价：** §4.2 仅以 nanoGPT GPT-2-small 124M、10K steps、batch 512、sequence length 512 和 learning-rate grid 作有限 corroboration。
- **未证明：** 论文没有独立 limitations section；theorem assumptions 与单一小模型实验构成 non-proof boundary，未证明在 dense/correlated noise 或其他 geometry 下仍占优。

**Books 结论：** `Integrate — Applied → TRAIN-PRETRAINING`。Ch28“Sign Step 的优势取决于范数几何与噪声结构”已把 optimizer 选择绑定 geometry/noise contract，并保留 SGD/AdamW fallback。

### [StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction](https://arxiv.org/html/2605.06642v1)

- **机制：** §4.1 从初始 observation 生成 strategy 并将其固定为整条 trajectory 的显式条件；§4.2 采样 `N` 个 strategy、每个 `M` 条 rollout，以 strategy-group 与 action-group 两级相对目标分离高低层 credit。
- **评价：** §5 在 AgentGym 的 ALFWorld、WebShop、SciWorld 上对照 PPO、RLOO、GRPO 与 GiGPO。
- **未证明：** 初始 strategy 在环境变化后可能 stale，`N×M` 层次采样增加 rollout cost，且未验证更广环境、在线修订 strategy 或生产安全。

**Books 结论：** `Integrate — Applied → TRAIN-GRPO`。Ch33“Hierarchy of Groups”已区分 strategy state 与 action trace，并保留 reactive/revisable strategy fallback。

### [Beyond Negative Rollouts: Positive-Only Policy Optimization with Implicit Negative Gradients](https://arxiv.org/html/2605.06650v1)

- **机制：** §3 用 positive-set bounded/self-normalized importance objective、softmax denominator 产生的 implicit negative token gradients，以及 EMA siamese anchor 和 bounded representation penalty，构成不依赖显式 negative-rollout advantage 的 RLVR 分支。
- **评价：** §4 在公开数学 benchmark 与 Qwen、DeepSeek、Llama 系列最高 7B 模型上报告结果和组件消融。
- **未证明：** §5 限于 sparse binary reward、text-only math 与不超过 7B；zero-positive batch、dense reward 与跨域条件都没有建立。

**Books 结论：** `Integrate — Applied → TRAIN-GRPO`。Ch33“Positive-only 不是没有负向梯度”已明确 positive-set/update ownership、EMA 成本、zero-positive failure 与标准 GRPO/PPO fallback。

<!-- may08-denominator-challenge:end -->

<!-- may08-independent-false-negative-repair:start -->

### [The Cost of Context: Mitigating Textual Bias in Multimodal Retrieval-Augmented Generation](https://arxiv.org/html/2605.05594v1)

- **机制：** 论文从“原本正确、加入 oracle text 后变错”的 recorruption 样本出发，把失效定位为视觉 attention mass/sharpness 下降与文本位置偏置；BAIR 用额外 reference pass 在 prefill 重平衡跨模态证据。
- **评价：** 只在披露的 6 个模型、IU-Chest/FACET/NWPU 与 RTX A5000 配置中建立；代码为 `HoinJung/BAIR`。
- **未证明：** 增加 prefill 成本且阈值任务相关；不能修复错误 retrieval、歧义图像、模型强先验，也不是 correctness certificate。

**Books 结论：** `Integrate — Applied → AGENT-RAG`；向 `MULTIMODAL-REPRESENTATION` 只作 modality-fusion handoff。

### [Retrieval-Conditioned Topology Selection with Provable Budget Conservation for Multi-Agent Code Generation](https://arxiv.org/html/2605.05657v1)

- **机制：** 从层次代码索引抽取结构复杂度，再选择 multi-agent DAG；在 deterministic tool cost、bounded retrieval depth 与 finite action space 下可于执行前验证资源预算守恒。
- **评价：** sub-ms DAG、线性索引扩展和 10 个 synthetic issue 主要验证编排开销，不证明真实软件质量。
- **未证明：** 成本随机时静态 certificate 不成立，必须回退 runtime accounting；外部有效性有限。

**Books 结论：** `Integrate — Applied → AGENT-MULTI-AGENT`。

### [An Empirical Study of Proactive Coding Assistants in Real-World Software Development](https://arxiv.org/html/2605.05700v1)

- **机制与评价：** 从 1,246 名开发者三天内约 4M IDE trace 形成 5,492 样本，以时间切分比较 13 个 LLM/RAG/Agent baseline；真实 trace 与模拟 trace 在多样性、时间结构与探索行为上不同。
- **未证明：** developer intent 不可直接观察，LLM/proxy label 可能漏标；只覆盖三天与受控人群，exact-v1 未发现公开 artifact。

**Books 结论：** `No Change — Existing Coverage → PLATFORM-EVALUATION-SYSTEM`。现有章节已经要求 synthetic evidence 只有在 exchangeability 成立时才可外推，并将 simulator/replay 与 deployment truth 分开。

### [LeakDojo: Decoding the Leakage Threats of RAG Systems](https://arxiv.org/html/2605.05818v1)

- **机制：** 可配置 RAG/attack/defense，并保留跨轮 extraction state；query generation 与 adversarial instruction 是可独立组合的泄露因素。
- **评价：** 6 attacks、14 LLMs、4 datasets；部分 faithfulness 组件可能扩大泄露，第一方 GitHub artifact 由 exact-v1 链接。
- **未证明：** 固定预算、英文与有限 rewriter/reranker/summarizer 不能代表所有 pipeline。

**Books 结论：** `Integrate — Applied → PLATFORM-SECURITY`。

### [MDN: Parallelizing Stepwise Momentum for Delta Linear Attention](https://arxiv.org/html/2605.05838v1)

- **机制：** 二阶 momentum recurrence 通过 coefficient reordering 获得 causal chunk-parallel training，同时保持 recurrent decode；backward 重建 correction values，而非保存完整 state。
- **评价：** 400M/1.3B，在 language modeling、long-context、retrieval 与 needle 任务上比较；提供 Triton artifact `HuuYuLong/MomentumDeltaNet`。
- **未证明：** 未验证 7B+ 与 TP；增加 momentum state/correction values，训练吞吐仍可能低于优化 GDN/Comba。

**Books 结论：** `Integrate — Applied → MODEL-LONG-CONTEXT`。

### [Quantizing With Randomized Hadamard Transforms: Efficient Heuristic Now Proven](https://arxiv.org/html/2605.06014v1)

- **机制：** 两次 RHT 的固定坐标近高斯保证足以支撑 scalar quantization；sparse input 的 block VQ 仍可能保留相关，三次 RHT 才对 fixed bounded block 给出衰减 covariance；`l3`/`linfinity` moment check 用于选择次数。
- **评价：** 这是 theorem/algorithmic evidence，没有 empirical throughput 或公开实现。
- **未证明：** Hadamard-compatible dimension、fixed block/codebook 与渐近项限制外推；额外 transform 有实际算力/带宽成本。

**Books 结论：** `Integrate — Applied → INFER-TENSORRT-LLM`。

### [Toward Visually Realistic Simulation: A Benchmark for Evaluating Robot Manipulation in Simulation](https://arxiv.org/html/2605.06311v1)

- **机制与评价：** 用 shadows、specular highlights 与 PBR material 建立仿真视觉真实性 contract；14 curated、8 reconstructed 及生成任务，Google Robot/WidowX，两类 policy 的 sim-real matching 平均 Pearson 报告为 0.92。
- **未证明：** 任务、policy 与 embodiment 范围有限，每任务试验数少；相关性不能替代实机安全验证，exact-v1 未发现第一方 artifact。

**Books 结论：** `No Change — Existing Coverage → MULTIMODAL-EMBODIED-VLA`。现有章节已覆盖 camera/lighting/texture gap、real calibration 与 physical authority 边界。

### [Teaching Thinking Models to Reason with Tools: A Full-Pipeline Recipe for Tool-Integrated Reasoning](https://arxiv.org/html/2605.06326v1)

- **机制：** tool-use SFT 需要 tool-suited task 与可学习 teacher trajectory，并混合 text-only trajectory；checkpoint 同时看 `pass@k` 与 response length，通过后才交带 mode-collapse safeguard 的 RLVR。
- **评价：** Qwen3 4B/30B、competition math 与 4,325 个 RLVR examples；观察到 SFT 的 `form → substance → noise` 动态。
- **未证明：** 数学与两个模型规模不能代表通用 Agent workflow；透明 trace 和人类/领域验证仍缺，exact-v1 未发现公开仓库。

**Books 结论：** `Integrate — Applied → TRAIN-SFT`；向 `TRAIN-GRPO` 与 `AGENT-TOOL-CALLING` 作短 handoff。

### [Task-Aware Answer Preservation under Audio Compression for Large Audio Language Models](https://arxiv.org/html/2605.06631v1)

- **机制：** compression release 以相对 raw audio 的 excess answer error 为指标，重点约束 worst semantic/query family，并对 query-conditioned frontier 给出统计置信度。
- **评价：** 5 个英文 prompted MC audio-QA 数据集，Qwen2-Audio-7B 与 Qwen2.5-Omni-7B；selector、backbone 与 family partition 会改变结果。
- **未证明：** aggregate average 会掩盖局部 harm，v1 keyword partition 较粗；没有测量真实 rate-theoretic frontier，也未证明统一收益。

**Books 结论：** `Integrate — Applied → PLATFORM-EVALUATION-SYSTEM`，扩展现有 compression-release contract。

以上 9 项完整公式、artifact、owner 对读与 root 写回要求见 [作者侧 false-negative 修复记录](../_sources/daily-20260508/V3_FALSE_NEGATIVE_REPAIR_20260914.md) 和 [Books 写回队列](../_sources/daily-20260508/BOOKS_WRITEBACK_QUEUE_FALSE_NEGATIVES.md)。

<!-- may08-independent-false-negative-repair:end -->

<!-- may08-postwrite-false-negative-repair-round2:start -->

### Post-write false-negative 作者修复（4 个指定项 + 5 个同类 closure 漏项）

以下 9 项均确认属于本窗 official batch，exact-v1 可读且未见 withdrawal。这里保留足以解释准入、证据边界与 Books 判断的摘要；逐项 Method、实验、non-proof、trade-off、fallback 与 closure 反查样本见 [完整作者修复记录](../_sources/daily-20260508/V3_FALSE_NEGATIVE_REPAIR_ROUND2_20260914.md)。

### [Decision-aware User Simulation Agent for Evaluating Conversational Recommender Systems](https://arxiv.org/html/2605.05250v1)

Hesitator 将候选 utility selection 与 overload-aware commitment 分开。证据仅覆盖 Amazon Electronics/Video Games、静态 persona、每配置 40 sessions、最多 20 turns 与 `gpt-oss-20b`，不能外推到动态偏好或生产用户。

**Books 结论：** 已有覆盖到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Ch66 已承载 simulator behavioral realism、decision fidelity 与 disengagement。

### [SOCpilot: Verifying Policy Compliance for LLM-Assisted Incident Response](https://arxiv.org/html/2605.05501v1)

模型只生成 typed plan proposal，由 deterministic verifier 检查 catalog、ordering、policy 与 approval。200 个匿名 production SOC incidents 与 `1147/1147` public action mapping 只证明 plan compliance，不证明真实工具效果或 runtime security。

**Books 结论：** 已有覆盖到 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)；Ch72 已把模型输出定义为 untrusted proposal。

### [Chain of Risk: Safety Failures in Large Reasoning Models and Mitigation via Adaptive Multi-Principle Steering](https://arxiv.org/html/2605.05678v1)

论文分别测 reasoning 与 answer safety。15 个 reasoning models、每模型约 41K prompts 及有限白盒 steering 不能证明 visible trace 忠实于内部 computation，也不能替代 runtime authorization 与 outcome verification。

**Books 结论：** 已有覆盖到 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)；Ch72/Ch66 已区分 trace、output、action 与 outcome authority。

### [Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes](https://arxiv.org/html/2605.05715v1)

29 个 fixed-linear intervention configuration 的负面结果表明 failure signal 可解码不等于可被同方向纠正。两个 7–8B model、主要 MedQA 的结果不覆盖所有 steering；probe 失败时只可支持校准后的 abstention/escalation，不能拥有 correction authority。

**Books 结论：** 整合到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；状态为已落实。

### [RVPO: Risk-Sensitive Alignment via Variance Regularization](https://arxiv.org/html/2605.05750v1)

多 reward 算术均值会让高分目标补偿 must-have bottleneck；SoftMin/variance penalty 是受 `k`、group size、schedule 与 noisy reward 影响的条件分支，不能替代 deterministic hard gate。

**Books 结论：** 整合到 [TRAIN-RLHF](../../../../books/part-04-training-system/31-rlhf.md)；状态为已落实。

### [Optimal Transport for LLM Reward Modeling from Noisy Preference](https://arxiv.org/html/2605.06036v1)

partial optimal transport 允许 reward-model data owner 拒绝 noisy preference mass，却依赖 clean samples 更一致的前提，并引入 `O(N²)` cost matrix、quota 与 embedding identity 成本；理论上界只约束 selected subset。

**Books 结论：** 整合到 [TRAIN-RLHF](../../../../books/part-04-training-system/31-rlhf.md)；状态为已落实。

### [Milestone-Guided Policy Learning for Long-Horizon Language Agents](https://arxiv.org/html/2605.06078v1)

milestone segment credit 位于 terminal reward 与逐 action causal credit 之间，boundary 必须由 environment/harness 冻结。ALFWorld、WebShop、ScienceWorld 的离散 text-action 结果不覆盖 continuous control 或无可验证 transition 的任务。

**Books 结论：** 整合到 [TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md)；状态为已落实。

### [A$^2$TGPO: Agentic Turn-Group Policy Optimization with Adaptive Turn-level Clipping](https://arxiv.org/html/2605.06200v1)

`(prompt, turn-index)` normalization、sqrt-depth rescale 与 turn clipping 可细化 multi-turn credit，但 turn index 不是真实 state equivalence。证据限于 7 个 QA benchmark、3 个 Qwen backbone、本地 Wikipedia retrieval 与 8×H20/VeRL。

**Books 结论：** 整合到 [TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md)；状态为已落实。

### [Measuring Black-Box Confidence via Reasoning Trajectories: Geometry, Coverage, and Verbalization](https://arxiv.org/html/2605.06308v1)

black-box confidence 融合 coverage、trajectory geometry 与 verbalization，matched setting 中 `K=4` 对 `SC@8` 有成本优势；但 coverage 仍由 judge 解释，verbalization 只在 6/18 settings 提供增量，也无法恢复从未进入 candidate set 的真值。

**Books 结论：** 已有覆盖到 [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Ch66 已承载异质 sensor、校准、risk–coverage 与 abstention。

5 项 proposition、位置与边界见 [第二轮 Books 写回队列](../_sources/daily-20260508/BOOKS_WRITEBACK_QUEUE_FALSE_NEGATIVES_ROUND2.md)，root 写回证据见 [Root Books Writeback](../_sources/daily-20260508/ROOT_BOOKS_WRITEBACK_20260914.md)。作者侧修复与 root 写回均不构成独立 Gate。

<!-- may08-postwrite-false-negative-repair-round2:end -->

<!-- may08-final-closure-repair:start -->

### 4.1 最终 closure 修复（2026-09-15）

上一轮独立终审确认 17 个 closure false negative。本轮逐项取得 exact-v1、确认本窗 owner 与未撤稿，完成 Score、深度审阅、owner/相邻章节对读和 Books Decision；随后只在八类共享错误模式中有界复核 59 个 closure，新增确认 5 个 false negative，其余 54 项保持关闭。完整 Method、evaluation、non-proof 与处置见 [最终 closure 修复记录](../_sources/daily-20260508/V3_FINAL_CLOSURE_REPAIR_20260915.md)。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books 决定 |
| --- | --- | --- | --- | --- |
| [BitCal-TTS](https://arxiv.org/html/2605.05561v1) | 2026-05-08T08:00:00+08:00 | precision 进入 halting sensor/controller identity；2+2+2=6 | 深入完成 | 已落实并通过独立复核：`INFER-SCHEDULING` |
| [When Can Voting Help, Hurt, or Change Course?](https://arxiv.org/html/2605.05592v1) | 2026-05-08T08:00:00+08:00 | 异质样本下 voting curve 可非单调；3+2+3=8 | 深入完成 | 已落实并通过独立复核：`PLATFORM-EVALUATION-SYSTEM` |
| [Architecture Matters](https://arxiv.org/html/2605.05632v1) | 2026-05-08T08:00:00+08:00 | RAG architecture 改变 poisoning failure path；3+2+2=7 | 深入完成 | 已落实并通过独立复核：`PLATFORM-SECURITY` |
| [Text-Graph Synergy](https://arxiv.org/html/2605.05643v1) | 2026-05-08T08:00:00+08:00 | 双向校验与可恢复的 pruned graph state；2+2+2=6 | 深入完成 | 已落实并通过独立复核：`AGENT-RAG` |
| [ReFlect](https://arxiv.org/html/2605.05737v1) | 2026-05-08T08:00:00+08:00 | deterministic harness 分离 error detection 与 recovery；3+3+3=9 | 深入完成 | 已有覆盖：`AGENT-WORKFLOW` |
| [Adaptive Selection of LoRA Components](https://arxiv.org/html/2605.05769v1) | 2026-05-08T08:00:00+08:00 | DP federated LoRA 的逐层逐轮 component control；3+2+2=7 | 深入完成 | 已落实并通过独立复核：`TRAIN-LORA` |
| [Distribution-Aligned Adversarial Distillation](https://arxiv.org/html/2605.05777v1) | 2026-05-08T08:00:00+08:00 | 黑盒 uncertainty proxy 的 calibration/drift 边界；2+2+2=6 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` |
| [LoopTrap](https://arxiv.org/html/2605.05846v1) | 2026-05-08T08:00:00+08:00 | context poisoning 可劫持 termination authority；3+3+3=9 | 深入完成 | 已落实并通过独立复核：`PLATFORM-SECURITY` |
| [Hallucination as an Anomaly](https://arxiv.org/html/2605.05953v1) | 2026-05-08T08:00:00+08:00 | anomaly sensor 与 correction authority 分离；3+2+2=7 | 深入完成 | 已落实并通过独立复核：`PLATFORM-EVALUATION-SYSTEM` |
| [Selective Eligibility Traces for RLVR](https://arxiv.org/html/2605.05965v1) | 2026-05-08T08:00:00+08:00 | sparse token-credit artifact；3+2+2=7 | 深入完成 | 已落实并通过独立复核：`TRAIN-GRPO` |
| [Schedule-and-Calibrate](https://arxiv.org/html/2605.06111v1) | 2026-05-08T08:00:00+08:00 | task utility 联合控制 curriculum 与 per-task KL；3+2+2=7 | 深入完成 | 已落实并通过独立复核：`TRAIN-GRPO` |
| [DualSFT](https://arxiv.org/html/2605.06166v1) | 2026-05-08T08:00:00+08:00 | 共享 gradient matrix 联合 data/parameter selection；2+2+2=6 | 深入完成 | 已落实并通过独立复核：`TRAIN-SFT` |
| [OPSD Compresses What RLVR Teaches](https://arxiv.org/html/2605.06188v1) | 2026-05-08T08:00:00+08:00 | SFT→RLVR→OPSD 的条件化 compaction stage；3+2+3=8 | 深入完成 | 已落实并通过独立复核：`TRAIN-GRPO` |
| [TIDE](https://arxiv.org/html/2605.06216v1) | 2026-05-08T08:00:00+08:00 | 逐层重注入 token identity；3+1+3=7 | 深入完成 | 已落实并通过顺序复核：`MODEL-EMBEDDING` |
| [Joint Consistency](https://arxiv.org/html/2605.06219v1) | 2026-05-08T08:00:00+08:00 | independent fields 与 pairwise interaction 共同定义 aggregation；3+2+2=7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` |
| [Profiling for Pennies](https://arxiv.org/html/2605.06232v1) | 2026-05-08T08:00:00+08:00 | search→inference→aggregation 的 derived privacy；3+2+3=8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` |
| [LatentRAG](https://arxiv.org/html/2605.06285v1) | 2026-05-08T08:00:00+08:00 | latent query/retrieval 降 latency 但削弱可观察性；3+2+3=8 | 深入完成 | 已落实并通过独立复核：`AGENT-RAG` |
| [Adaptive Task Graphs](https://arxiv.org/html/2605.06320v1) | 2026-05-08T08:00:00+08:00 | evolving coordination graph 拥有依赖、分配与进度；3+2+2=7 | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT` |
| [Pop Quiz Attack](https://arxiv.org/html/2605.06423v1) | 2026-05-08T08:00:00+08:00 | quiz-style black-box membership audit；3+2+2=7 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` |
| [Continuous Latent Diffusion Language Model](https://arxiv.org/pdf/2605.06548v1) | 2026-05-08T08:00:00+08:00 | global latent prior 与 local token realization 分层；3+2+3=8 | 深入完成 | 已落实并通过顺序复核：`MULTIMODAL-GENERATIVE-PARADIGMS` |
| [FedAttr](https://arxiv.org/html/2605.06596v1) | 2026-05-08T08:00:00+08:00 | secure aggregation 下的 client attribution/leakage ledger；3+2+2=7 | 深入完成 | 已落实并通过独立复核：`PLATFORM-SECURITY` |
| [Crafting Reversible SFT Behaviors](https://arxiv.org/html/2605.06632v1) | 2026-05-08T08:00:00+08:00 | sparse causal carrier 与 reversible SFT control；3+2+2=7 | 深入完成 | 已落实并通过独立复核：`TRAIN-SFT` |

16 项精确写回合同见 [结构化 Books queue](../_sources/daily-20260508/BOOKS_WRITEBACK_QUEUE_FINAL_CLOSURE_REPAIR.json)。六项 No Change 均以具体既有命题为依据：Ch81 的 verification/recovery artifact 与 budget/commit；Ch66 的 calibrated sensor、pairwise aggregation identity；Ch72 的 derived privacy、membership sample/query contract；Ch82 的 authoritative coordination graph 与 commit transition。它们不是因篇幅或低分关闭。

<!-- may08-final-closure-repair:end -->

### 4.2 九项 false negative 限定返修（2026-09-15）

fresh non-author review 指定的 9 项已逐篇完成 exact-v1 Method、evaluation contract、limitations/non-proof、withdrawal、Score V2、Stable Node 与当前 Books 命题对读。完整证据见 [限定返修记录](../_sources/daily-20260508/V3_BOUNDED_REPAIR_NINE_FALSE_NEGATIVES_20260915.md)。

其中 6 项已由 root 按精确 [Books 写回队列](../_sources/daily-20260508/ROOT_BOOKS_WRITEBACK_QUEUE_BOUNDED_REPAIR_20260915.json) 落实：MoE routing information budget、reasoning trace 编译为 solver artifact、视觉表示的 topology/semantic/texture 分责、construction path 的 admission/reward 双重使用、initial-prior single-pass guidance、position-indexed visual codebook capacity。3 项 No Change 分别由 Ch72 的 reconstruction-layer attack、Ch66 的 nonlinear intervention evidence gate 与 Ch25 的 action-realization/environment-response owner 分离完整承载。

### [Expert Routing for Communication-Efficient MoE via Finite Expert Banks](https://arxiv.org/html/2605.05278v1)

论文把 gate 建模为输入到 expert index 的随机信道，以 routing information 和 rate–distortion 分离路由选择性与任务损失。有限 CNN expert bank / MNIST 结果只支持一个 workload-specific design proxy；它不证明端到端 LLM MoE、跨节点通信或生产阈值。**Books 结论：** 已由 root 整合到 [MODEL-MOE](../../../../books/part-02-model/21-moe.md)，等待新的独立复核。

### [ReaComp: Compiling LLM Reasoning into Symbolic Solvers for Efficient Program Synthesis](https://arxiv.org/html/2605.05485v1)

方法从多条 LLM reasoning trace 离线归纳 reusable symbolic solver，在线 solver-first、未覆盖或失败时 LLM fallback。两个结构化 DSL 的结果支持可摊销 executable artifact，不证明开放任务可被通用编译；run-to-run 波动、best-run selection 与 verifier 依赖必须保留。**Books 结论：** 已由 root 整合到 [AGENT-WORKFLOW](../../../../books/part-07-agent/81-workflow.md)，等待新的独立复核。

### [MUSE: Resolving Manifold Misalignment in Visual Tokenization via Topological Orthogonality](https://arxiv.org/html/2605.05646v1)

方法将 structural topology、semantic value 与 residual texture 分到不同表示/梯度路径，以缓解统一视觉 tokenizer 的 reconstruction–abstraction 冲突。同 backbone/data/teacher 的对照与 ablation 不证明 Q/K–V 分工的因果唯一性或跨模态普适性。**Books 结论：** 已由 root 整合到 [MULTIMODAL-REPRESENTATION](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，等待新的独立复核。

### [Knowledge-Graph Paths as Intermediate Supervision for Self-Evolving Search Agents](https://arxiv.org/html/2605.05702v1)

任务生成保存的 KG construction path 同时服务 data admission 与 solver waypoint partial credit，让 proposer/reward 共享同一版本化 artifact；terminal verifier 仍拥有最终正确性。证据限于 Wikidata factoid multi-hop，图谱与抽取误差可能同时污染问题和奖励。**Books 结论：** 已由 root 整合到 [TRAIN-DATA](../../../../books/part-04-training-system/27-data.md)，等待新的独立复核。

### [Conceal, Reconstruct, Jailbreak: Exploiting the Reconstruction-Concealment Tradeoff in MLLMs](https://arxiv.org/html/2605.05709v1)

攻击在 concealment 与 victim-side reconstruction 之间取舍，使恶意语义绕过原始输入检查后在多模态重建层恢复。HADES、五类风险、五个攻击基线和作者 judge 只证明披露攻击合同。**Books 结论：** root 已将 reconstruction-layer attack、data/reconstruction 双层校验、identity、trade-off 与 fallback 写入 [PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md) 主正文，状态为 `Integrate — Applied`，等待新的独立复核。

### [Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention](https://arxiv.org/html/2605.05892v1)

FLAS 用 concept/time-conditioned velocity field 与数值积分替代固定 residual steering vector，形成 state-adaptive curved intervention。AxBench、Gemma 与单层 FlowBlock 证据不证明多概念、跨层或跨模型因果迁移。**Books 结论：** [PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已要求 nonlinear/local intervention 重新证明 target effect、control survival 与 OOD evidence，`No Change — Existing Coverage`。

### [P-Guide: Parameter-Efficient Prior Steering for Single-Pass CFG Inference](https://arxiv.org/html/2605.06124v1)

方法把每个采样步的 conditional/unconditional 双 forward 近似前移到 initial latent prior，以条件均值/方差模块 steering 后执行 single-pass sampling。一阶等价、class-conditioned image workload 与单 RTX4090 结果不能外推生产并发或 tail SLO。**Books 结论：** 已由 root 整合到 [MULTIMODAL-GENERATIVE-PARADIGMS](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，等待新的独立复核。

### [EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields](https://arxiv.org/html/2605.06192v1)

方法用 kinematics 与 calibration 构造 camera-aligned action field，再与事件/视觉状态融合；simulation ablation 只支持其模型与指标，不证明真实物理控制。**Books 结论：** [MULTIMODAL-WORLD-MODELS](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 已由“Action realization 与 environment response 应由不同 owner 承担”完整承载，`No Change — Existing Coverage`。

### [Taming the Entropy Cliff: Variable Codebook Size Quantization for Autoregressive Visual Generation](https://arxiv.org/html/2605.06207v1)

论文指出 uniform codebook 的累计容量会在序列早期跨过 empirical data uncertainty，并以 position-varying codebook 形成 coarse-to-fine capacity schedule。ImageNet 256 的受控比较不证明其他数据、模态或语言的统一最优 schedule。**Books 结论：** 已由 root 整合到 [MULTIMODAL-REPRESENTATION](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，等待新的独立复核。

### 十项限定返修 Evidence（2026-09-15）

以下 10 项只补充 fresh non-author reviewer 点名的 false negatives；exact-v1 locator、withdrawal、artifact 与机器可查字段见 [限定 Evidence JSON](../_sources/daily-20260508/V3_EXACT_V1_TEN_FALSE_NEGATIVES_20260915.json)。

### [Nonsense Helps: Prompt Space Perturbation Broadens Reasoning Exploration](https://arxiv.org/html/2605.05566v1)

LoPE 针对 GRPO 全失败 group 的 zero-advantage 与重复采样低收益，把探索 actuator 从 logit temperature 扩展到 prompt-space perturbation，再通过 response regrouping、importance-ratio shaping 与 advantage shaping恢复稀有成功轨迹的训练信号。作者只在 Qwen3-1.7B/4B、Qwen2.5-Math-7B、OpenR1-Math 与所列数学 benchmark 上比较，并使用 4/8 张 80GB A100；随机 Lorem、off-policy correction、取消 KL 与任务理解损伤都进入方法边界。

**Score / owner：** `2+2+2=6`，Standard；`TRAIN-GRPO`。Ch33 已明确区分入口收窄与进入后的完成能力，并要求 exploration signal 只控制采样、group builder 固定 membership、outcome verifier 保留真值权以及重采样收益递减时使用 bounded intervention/fallback。结论：`No Change — Existing Coverage`。

### [Nearly Optimal Attention Coresets](https://arxiv.org/html/2605.05602v1)

论文在 unit-norm keys/values、bounded query radius 与 additive error 下证明 softmax attention 存在与序列长度无关的 subset coreset，并给出 matching communication/coreset lower bounds。它直接限定“attention state 能压到多小”，但主要是存在性/理论边界，不是生产可执行的 causal KV eviction 算法，也不保留逐 token provenance。

**Score / owner：** `3+2+3=8`，Deep；`MODEL-LONG-CONTEXT`。Ch22 已比较完整 KV、recurrent state 与 compressed checkpoint，却没有这条带 upper/lower bound 的 attention-subset 可行性边界。结论：`Integrate — Applied`。

### [Decomposing the Basic Abilities of Large Language Models: Mitigating Cross-Task Interference in Multi-Task Instruct-Tuning](https://arxiv.org/html/2605.05676v1)

Badit 用高奇异值方向初始化多个 LoRA experts，再按 rank-1 component 的当前梯度方向做动态分组，使 expert 间近似正交、expert 内更一致，从而缓解 multi-task instruction tuning 的共享参数干扰。SuperNI、六个 LLM、五 seed 与 gradient-angle/ablation 支持受限机制；DOG 包含 CPU spherical clustering 与 integer optimization，作者报告相对 LoRAMoE 平均约 `1.22×` 训练时间，不能外推为通用能力分解。

**Score / owner：** `2+2+2=6`，Standard；`TRAIN-LORA`。Ch30 已有静态奇异子空间解除 expert cold-start，却未说明训练会重新破坏正交性及如何维护动态 grouping state。结论：`Integrate — Applied`。

### [Steering Visual Generation in Unified Multimodal Models with Understanding Supervision](https://arxiv.org/html/2605.05781v1)

UNO 冻结 understanding expert，让它从 noised generative representation 解码语义重述或回归视觉 encoder 特征，使理解损失的梯度进入生成路径；prompt masking、semantic re-caption 与 metaquery 用于限制条件复制和目标泄漏。证据限 BAGEL-7B、5K iterations、作者图像生成/编辑数据与 benchmark，PCA 可视化和 judge 分数不能证明一般表征因果或所有模态收益。

**Score / owner：** `3+2+2=7`，Deep；`MULTIMODAL-GENERATIVE-PARADIGMS`。Ch24 已有 unified generation 的共享状态与 modality interference，但没有 frozen understanding expert → generative representation 的监督路径及 leakage boundary。结论：`Integrate — Applied`。

### [AGPO: Asymmetric Group Policy Optimization for Verifiable Reasoning and Search Ads Relevance at JD](https://arxiv.org/html/2605.05826v1)

AGPO 用 group variance 约束正向相对 advantage，并为错误路径保持 gated negative signal，试图减缓 RLVR 对 base-policy reasoning support 的收窄。作者在三类 LLM、五个数学 benchmark 与一个 JD search-ads teacher pipeline 上报告 pass@k、entropy、PIR 和两天 A/B 指标；这些数字受 reward、group size、KL、256-sample evaluator 与业务分布约束，不构成通用边界保持保证。

**Score / owner：** `3+2+2=7`，Deep；`TRAIN-GRPO`。Ch33 已把 zero-positive group、negative update、入口概率与条件完成率、pass@k coverage、entropy 与 verifier authority 分开，并保留普通 group sampling/regularization。结论：`No Change — Existing Coverage`。

### [Logic-Regularized Verifier Elicits Reasoning from LLMs](https://arxiv.org/html/2605.05893v1)

LoVer 从白盒 LLM hidden state 训练二层 MLP verifier，以 negation、同答案组内一致性和答案组间唯一正确三类逻辑约束替代人工标签。该 sensor 假设候选中至少有一个正确答案，且同一 final answer 的 reasoning truth 可合并；实验覆盖 GSM8K、MMLU-Pro、HotpotQA、BIG-Bench Hard/iGSM 与若干 OOD split，但没有外部 correctness oracle，也不适用于黑盒模型。

**Score / owner：** `3+2+2=7`，Deep；`PLATFORM-EVALUATION-SYSTEM`。Ch66 已明确 hidden-state probe、self-consistency 与 learned verifier 只能形成校准 sensor，不拥有 truth，漂移或白盒状态不可得时必须回退外部证据、deterministic verifier 或 abstention。结论：`No Change — Existing Coverage`。

### [MINER: Mining Multimodal Internal Representation for Efficient Retrieval](https://arxiv.org/html/2605.06460v1)

MINER 冻结视觉文档 retriever backbone，以逐层 probe、validation-driven neuron mask 与多层 fusion 形成单一 compact embedding，在不改变向量维度与搜索复杂度的前提下利用内部层信号。ViDoRe、三个 backbones 与 Qdrant 对照只支持所列 retrieval/index 条件；训练数据可用性、layer/mask 选择、validation overfit 与未披露生产并发限制外推。

**Score / owner：** `2+2+2=6`，Standard；`AGENT-RAG`。Ch76 已把 late-interaction 质量、multi-vector storage/memory traffic、single-vector 吞吐与 budgeted compression/fusion 统一为 persisted index frontier，并要求 encoder/vector budget/distance rule/rebuild provenance。结论：`No Change — Existing Coverage`。

### [MARBLE: Multi-Aspect Reward Balance for Diffusion RL](https://arxiv.org/html/2605.06507v1)

MARBLE 保留每个 reward 的独立 advantage 与 policy gradient，再用约束优化选择共同 update direction；为避免每步 `R+1` 次 backward 和单 batch 系数抖动，周期性求解并用 EMA 平滑、其余 step 复用标量系数。实验限 SD3.5-M、rank-32 LoRA、五个 reward、16 H200 与作者图像指标，未证明更大 reward set、视频/world model 或生产稳定性。

**Score / owner：** `3+2+3=8`，Deep；`TRAIN-RLHF`。Ch31 已有根据梯度方差/方向分歧调整混合权重的原则，但没有 per-reward advantage/gradient ownership、QP harmonization 与 amortized coefficient state。结论：`Integrate — Applied`。

### [Coordination Matters: Evaluation of Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/html/2605.06557v1)

STAT 在 commitment-constrained spatial task allocation 中把 return 与 conflict count/rate、conflicts per task、assignment diversity、throughput 分账，并沿 agent/task/environment 三个轴做 matched scaling。五 seed、A100、2M/20M timestep 与 95% CI 支持该受控诊断；环境刻意排除 partial observability、通信、异构 Agent、拥塞与复杂路径，不能外推开放式 LLM Agent。

**Score / owner：** `3+2+3=8`，Deep；`AGENT-MULTI-AGENT`。Ch82 已要求 outcome 与 overlap/conflict/commit/rebase/tests/executable result/coordination cost 同时记录，并明确 throughput、重复动作、handoff 和恢复属于不同证据。结论：`No Change — Existing Coverage`。

### [Are We Making Progress in Multimodal Domain Generalization? A Comprehensive Benchmark Study](https://arxiv.org/html/2605.06643v1)

MMDG-Bench 固定 splits、batch、optimizer、training-domain model selection 与 search budget，对六数据集、三任务、六 modality configurations、九方法进行统一比较，再单独测试 corruption、missing modality、MisD 与 OOD。结果显示 clean ranking、故障鲁棒性和不同 trustworthiness 指标会互相反转；论文只覆盖 discriminative/regression、两种 corruption 与所列 backbone，不能外推生成任务或生产 sensor failure。

**Score / owner：** `3+2+3=8`，Deep；`PLATFORM-EVALUATION-SYSTEM`。Ch66 有通用 distribution/slice 与 calibration 原则，但没有把 clean multimodal ranking、missing-modality/corruption、MisD 与 OOD 明确列为不可替代的证据轴。结论：`Integrate — Applied`。

本轮没有材料访问阻断，也没有重开指定 9 项以外的 closure。作者未编辑 Books；root 写回不构成独立终审，双方都不能自签 final Gate。


### [XL-SafetyBench](https://arxiv.org/html/2605.05662v1)

5,500 个案例、10 个 country-language pair 与 ASR/NSR/CSR 分轴支持“安全韧性、文化敏感度、理解/生成失败不可压成一个总分”。双 native-speaker 和抽样 judge/human 复核不消除国家覆盖、语言代理、样本量与退化输出偏差；Ch66 已有同等主正文命题，故 `No Change`。

### [Large Vision-Language Models Get Lost in Attention](https://arxiv.org/html/2605.05668v1)

RID/MixIG 与 selected-layer attention replacement 支持 Attention reconfiguration、FFN expansion 及视觉路由冗余的受限反证；证据仅覆盖所测家族、层和 benchmark，不能推出 Attention 普遍无用。结论为 `MULTIMODAL-REPRESENTATION` 写回等待中。

### [Weak-to-Strong Generalization is Nearly Inevitable (in Linear Models)](https://arxiv.org/html/2605.05742v1)

linear logistic regression、approximate ellipticity、gradient-flow/随机分析支持“capacity mismatch 不是 weak-to-strong 的必要机制”。该结论不外推 frontier LLM 或任意非凸/noisy feedback；结论为 `TRAIN-RLHF` 写回等待中。

### [ArenaPO](https://arxiv.org/html/2605.06070v1)

pairwise arena preference 先拟合 capability distributions，再通过条件 latent gap 形成连续 offline reward；Pick-a-Pic/HPD 与 diffusion 实验只支持作者设置，Gaussian fit 与 selection bias 仍是误差源。结论为 `TRAIN-RLHF` 写回等待中。

### [DynT2I-Eval](https://arxiv.org/html/2605.06170v1)

结构化 prompt space、difficulty-aware sampling、三轴 pairwise judge、micro-batch 与 Bayesian ranking 支持动态 benchmark lifecycle；450 对人工复核和模拟不消除 generator/judge bias，也不证明动态 prompt 天然无污染。结论为 `PLATFORM-EVALUATION-SYSTEM` 写回等待中。

### [VL-LCM](https://arxiv.org/html/2605.06201v1)

sufficient/necessary 问法把逻辑一致性变成无标注辅助 sensor，MMMU/NaturalBench 等结果显示 accuracy 与 consistency 分离；额外调用昂贵且 consistency 不是真值。Ch66 已有同等 sensor/authority 边界，故 `No Change`。

### [FreeSpec](https://arxiv.org/html/2605.06509v1)

exact-v1 将 long-video window 的 spectral concentration 与粗结构保留、细节/运动损失关联，再以 global low-rank guidance 和 local high-rank basis 重建；Wan2.1/LTX-Video 结果不证明跨 backbone 普遍成立。结论为 `MULTIMODAL-GENERATIVE-PARADIGMS` 写回等待中。

### [TriRelVLA](https://arxiv.org/html/2605.05714v1)

object、hand、task primitives 经 task-guided graph 与 relational bottleneck 进入 action head，形成从 appearance state 到 action-relevant relation state 的机制链；关系抽取、mask、坐标与跨机器人边界均未消除。结论为 `MULTIMODAL-EMBODIED-VLA` 写回等待中。

### [HyperLens](https://arxiv.org/html/2605.05741v1)

后续层放大早期 confidence 变化并形成 refinement-area sensor；有限模型/SFT 实验提示 blind confidence，但 focal depth 依模型变化，trajectory 未校准为 correctness probability。Ch29 和 Ch66 已覆盖 trace 先退化及 sensor 权限，故 `No Change`。

### [Hypothesis generation and updating in large language models](https://arxiv.org/html/2605.05851v1)

number game 的 posterior prediction、candidate evaluation、free generation 与 1–100→1–200 extrapolation 显示这些接口不能互相代理；一维有限 hypothesis family 不能外推一般智能。结论为 `WORLDVIEW-LLM-INTELLIGENCE` 写回等待中。

### [Post Reasoning](https://arxiv.org/html/2605.06165v1)

answer-first、answer-conditioned justification 与 answer-loss masking 把提交延迟和解释成本分离；多任务回退、复杂搜索需求与 post-hoc fidelity 风险保留。结论为 `MODEL-SAMPLING` 写回等待中，`TRAIN-SFT` 只作 handoff。

### [PAGE / DomLoRA](https://arxiv.org/html/2605.06183v1)

PAGE 以 LoRA 初始 projected gradient energy 提出 placement；两个 8B 家族、四类任务提示浅层 FFN down-projection 集中，但局部梯度不是最终能力因果证明，也不覆盖 MoE/VLM。结论为 `TRAIN-LORA` 写回等待中。

### [Gaming the Metric, Not the Harm](https://arxiv.org/html/2605.06324v1)

transformation graph、semantic class、envelope repair 与含 annotation/protocol error 的 certificate 把公开 metric 变成安全对象；有限枚举与 solver replay 不证明现实 semantic class 或 harm 真值。结论为 `PLATFORM-EVALUATION-SYSTEM` 写回等待中。

### [SKOP](https://arxiv.org/html/2605.06342v1)

query-space steering 通过相对 QK logit 改变造成 focus-to-tail rerouting；只在风险 heads 上投影 focus-tail key difference 可改善所测 efficacy/utility。其白盒、calibration set、threshold 与模型边界保留；结论为 `MODEL-SELF-ATTENTION` 写回等待中。

### [Trace-Prior RL](https://arxiv.org/html/2605.06529v1)

two-hotel POMDP 显示 RevPAR 近似达标仍可对应错误 action trace；lagged-trace distributional prior 与 KL-constrained stochastic policy 给出受限修复。单一模拟器、固定竞争者和 prior 质量不支持开放 Agent 外推；结论为 `TRAIN-RLHF` 写回等待中。

完整 Method、evaluation、limitations、Score 与章节对读见 [十五项作者限定返修](../_sources/daily-20260508/V3_AUTHOR_BOUNDED_REPAIR_FIFTEEN_FALSE_NEGATIVES_20260915.md)。

### 十八项 false negative 限定返修 Evidence（2026-09-15）

### [AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/html/2605.05245v1)

fixed top-k 与 additive retrieval 在多跳问题中不能显式修复 bridge-fact gap。§3.1～3.4 让 controller 持有 `evidence set / entity ledger / unresolved gaps / token budget`，由 gap micro-query、question fallback 与 coverage/corroboration/novelty/redundancy utility 更新集合。§4～5 只在 HotpotQA clean/redundancy/noise 与 `k=3` 下比较 evidence F1、grounding 和 token；预算甚至未充分 binding，启发式权重、web-scale 与 conservative abstention 未解决。额外 ledger、LLM primitives 与停止校准换来更小 context 和显式 repair；gap 不可靠时回退 question-anchored retrieval，低风险单跳仍用 fixed top-k。该增量已写入 `AGENT-RAG`。

### [GLiNER Guard: Unified Encoder Family for Production LLM Safety and Privacy](https://arxiv.org/html/2605.05277v1)

moderation 与 PII 分开运行会重复编码；§3 用共享 encoder 在一次 forward 中输出 classification 与 span extraction，uni/bi/omni 分支分别交换 schema interaction、label cache、吞吐与 transfer，policy 仍拥有最终判决。§4～6 与 Appendix D 的 serving 只绑定 single A100、作者 batching/context、公开 safety suites 和合成俄语 PII-Bench；response moderation、长上下文、多语言仍弱，端到端 PII 还混有规则组件。always-on encoder 降低成本但牺牲复杂推理；不确定请求升级 autoregressive moderator，detector 失校准则人工/规则 fail-closed。该 execution boundary 已写入 `PLATFORM-SECURITY`。

### [BALAR : A Bayesian Agentic Loop for Active Reasoning](https://arxiv.org/html/2605.05386v1)

§4.2～4.7 维护 factorized latent belief，以 expected mutual information 选择澄清问题，并在现有维度不足时扩展 state；§5～7 只支持三个作者 benchmark 与其 LLM/user simulator。结构化 belief 和 sleep-time initialization 降低每轮搜索，却引入 prior、likelihood、维度生成与用户回答噪声；高风险或 belief 不可校准时回退直接 tool observation、显式澄清或人工判断。`AGENT-PLANNING` 已明确 `policy(goal, belief, plan)`、主动查询 latent state，以及 `belief + tool reliability + expected information gain → ask/act/verify/stop`，并保留主观概率不是 authority 的边界；结论为 `No Change — Existing Coverage`。

### [Information Theoretic Adversarial Training of Large Language Models](https://arxiv.org/html/2605.05415v1)

continuous adversarial training 对观测攻击样本近似均匀聚合。§3 让 training objective 在 f-divergence ambiguity set 内求 worst-case reweighting；KL dual 形成 log-sum-exp，`epsilon/lambda` 拥有 robustness–utility 强度。§4～5 只覆盖披露的 instruction-tuned models、HarmBench subset 与 CAT/CAPO/MixAT attack pipeline；重权 hard observed samples 不证明 unseen attacks robust。该机制更关注 residual vulnerability，却可能过拟合少数高 loss 样本并引入 dual 超参；半径或 utility regression 不稳时回退 uniform aggregation 与更广 attack suite。该增量已写入 `TRAIN-RLHF`。

### [On Semantic Loss Fine-Tuning Approach for Preventing Model Collapse in Causal Reasoning](https://arxiv.org/html/2605.05438v1)

cross-entropy 只奖励标签，在 class imbalance/structured reasoning 下可由 constant answer 取得表面高 accuracy。§4 用 graph-consistency semantic constraint 与动态 lambda 将结构违反纳入 SFT objective。§5～6、Appendix A/B 只覆盖 Gemma 270M、transitivity/d-separation 与作者构造数据；`200k+` evaluation samples 不能证明通用 causal reasoning，论文的 “essential” 措辞不得外推。结构约束阻止局部 collapse，却依赖正确 graph/schema 和 loss schedule；结构先验错误时会固化偏差，无可靠规则时回退 CE、balanced slices 与 behavioral tests。label loss 与 semantic constraint 的 objective 分权已写入 `TRAIN-SFT`。

### [Shortcut Solutions Learned by Transformers Impair Continual Compositional Reasoning](https://arxiv.org/html/2605.05495v1)

§3～5 在受控 continual compositional task 中比较 BERT feed-forward 与 ALBERT shared recurrent block；前者形成 shortcut，后者对 forward transfer 更有利，但两者跨 experience composition 仍失败，replay/combined experience 的收益也非通用。小模型、人工代数任务与 architecture confound 不证明 recurrence 普遍优于 depth；固定 stack 在吞吐、可预测和开放任务证据不足时仍是默认。`MODEL-TRANSFORMER-LAYER` 已完整拥有 `fixed parameter stack → shared recurrent block → execution-depth state`、组合任务证据、shortcut/停止/吞吐 failure 与 fixed-depth fallback；结论为 `No Change — Existing Coverage`。

### [Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks](https://arxiv.org/html/2605.05503v1)

单次 paraphrase robustness 不能代表 provenance signal 的多轮存活。§3～5 将 rewrite model/style/hop 与 detector threshold 组成 threat state，连续无密钥 rewriting 使原始 DLM watermark 信号接近 null。证据只绑定 LLaDA-8B-Instruct、同一 watermark 配置、四个 1.5B～8B rewriter、五种 style、约 300-token outputs；不证明所有 DLM watermark 或更长文本同样失效。watermark 便宜但在语义保持的变换链上脆弱；release/attribution 不得由单 detector 拥有，需 provenance、签名或受控 origin record 交叉验证。multi-hop laundering threat contract 已写入 `PLATFORM-SECURITY`。

### [Scaling Pretrained Representations Enables Label-Free Out-of-Distribution Detection Without Fine-Tuning](https://arxiv.org/html/2605.05638v1)

class-conditional labels 或专用 fine-tuning 常被视为 OOD 必需；§3～5 对 frozen representation 同时应用 global Mahalanobis 与 local score-curvature probe，并把 detector difference 与 backbone representation geometry 分账。59 个 vision/language backbone-task pairing 支持作者范围的收敛趋势；只比较两类 label-free detector，未覆盖所有 modality、hard shift 或 production threshold。无标签 probe 便宜且可部署，却会把 representation saturation/geometry drift 变成 calibration state；检测器失配时回退 labeled slice、task-specific detector 与人工 release gate。该受限演进已写入 `PLATFORM-EVALUATION-SYSTEM`。

### [Enabling Federated Inference via Unsupervised Consensus Embedding](https://arxiv.org/html/2605.05718v1)

conventional federation/cooperative inference 共享 raw input、parameters 或 common encoder。§III 用 unlabeled shared data 训练 consensus embedding 与 cooperative output，使 heterogeneous intermediate states 对齐后再 ensemble。§IV 覆盖 CIFAR、text/time-series 与 non-IID slices；alignment 是主要瓶颈，reconstruction test 不等于 privacy proof，规模、通信与 advanced attacks 未验证。少共享换来 alignment training、通信与新的 intermediate-leakage surface；对齐或隐私不成立时回退 solo inference、同构 ensemble 或受控 parameter federation。跨组织 heterogeneous model state 的 inference contract 已写入 `INFER-DYNAMO`，tenant/privacy 边界交给 `PLATFORM-MULTI-TENANT`。

### [TACT: Mitigating Overthinking and Overacting in Coding Agents via Activation Steering](https://arxiv.org/html/2605.05980v1)

只在 tool failure 后 reflection 无法提前识别 overthinking/overacting。§2 把 trajectory step 标注为 calibrated/两类 drift，抽取正交 residual axes，并在 test time 把 activation 拉回 calibrated region。§3 在 SWE-bench Verified、Terminal-Bench 2.0、CLAW-Eval 与两模型报告 outcome/steps；LLM-as-judge 标签、线性可分与 coding domain 不证明 causal、跨模型或安全泛化。无额外 LLM call 换来 white-box activation access、probe calibration 与错误 steering 风险；轴漂移时回退 observation-based loop guard、budget/stop rule 和外部 verifier。trajectory drift sensor 与 intervention authority 的分离已写入 `AGENT-REFLECTION`。

### [Novelty-based Tree-of-Thought Search for LLM Reasoning and Planning](https://arxiv.org/html/2605.06040v1)

novelty judge 以额外 prompts 判断 node 与既有 search tree 的重复或新颖性，换取 branch pruning；作者实验既报告良好配置下大幅 token 节省，也报告错误配置近零 solve rate 和成本上升。novelty 实质常退化为 duplicate detection，没有 solution-quality guarantee，judge 与 proposer 也可能共享盲点；配置不稳时回退 fixed-width/单链搜索、hard budget 与外部 verifier。`AGENT-PLANNING` 已完整表达 ToT 的指数分支、pruning/heuristic/budget/verifier、动态 branching 校准与“搜索更多不单调可靠”；结论为 `No Change — Existing Coverage`。

### [XtraMAC: An Efficient MAC Architecture for Mixed-Precision LLM Inference on FPGA](https://arxiv.org/html/2605.06052v1)

fixed-datatype datapath、upcast 或复制 MAC 会浪费 FPGA DSP。§III～V 将 INT/FP mantissa 归一为共享 integer product，用 datatype-specific sign/exponent/accumulation 与 dynamic packing 实现 cycle-level switching。§VI 只绑定 AMD Xilinx U55c、所列 formats/kernels 与 simulation/representative LLM workloads；component density、constant latency 不证明完整 serving goodput 或 GPU/NPU 可迁移。共享 datapath 提高利用率，却增加 packing/control、format coverage 与数值验证；不支持的 shape/dtype 回退固定精度 MAC。该硬件 lowering 分支已写入 `INFER-TENSORRT-LLM`。

### [CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models](https://arxiv.org/html/2605.06247v1)

output imitation/dense hidden matching 假设 teacher/student interface 同构且更新成本高。§3 从 teacher intermediate states 以 learnable-query cross-attention 压缩，再经 always-on adapter、router、sparse specialized adapters 注入 student text conditioning；backbones frozen。§4～5 只覆盖 LIBERO-Plus、四个 real tasks 与作者 WAM/backbone；1.17% trainable parameters 和 success rate 不证明开放环境、跨架构语义对齐或 physical safety。compact context 减少改动，却引入压缩丢失、router collapse、teacher bias 与 latent interface mismatch；失败时回退 output distillation、full tuning 或独立模型。heterogeneous WAM contextual interface 已写入 `MULTIMODAL-WORLD-MODELS`。

### [Continuous-Time Distribution Matching for Few-Step Diffusion Distillation](https://arxiv.org/html/2605.06376v1)

few-step DMD 在固定离散 anchors 上匹配，reverse-KL mode seeking/trajectory truncation 易丢细节，常依赖 GAN/reward auxiliary。§3 用随机长度 continuous schedule 与 student-velocity off-trajectory alignment 修正 truncation drift。§4 与 appendices 只覆盖 SD3-Medium、Longcat-Image、作者 metrics 与 few-step settings；不证明 continuous supervision 对其他 modalities/backbones 或 production latency 普遍占优。去掉辅助模块换来更复杂 trajectory sampling/velocity estimation，off-trajectory state 错误会放大；训练不稳时回退 discrete DMD、consistency 或更多 steps。该 distillation 演进已写入 `MULTIMODAL-GENERATIVE-PARADIGMS`。

### [Patch-Effect Graph Kernels for LLM Interpretability](https://arxiv.org/html/2605.06480v1)

大量 activation patches 是不可比较的 raw tensor。§3 将 component interventions 变成 direct-influence/partial-correlation/co-influence graph，再用 kernels 比较 slice；graph builder 只拥有 compression/diagnostic artifact。§4～5 在 GPT-2 Small、IOI/induction/GT 与 DistilGPT-2 pilot 中比较 graph、prompt-only、raw tensor、learned encoder；§6 明确不是 task-general causal-circuit proof，full DI 仍有 `O(|V|²)` cost。图提高结构可读性却引入 edge-definition、screening bias 与 compression loss，必须保留 raw/surface controls 和 paired patching。interpretability artifact 的 evidence hierarchy 已写入 `PLATFORM-EVALUATION-SYSTEM`。

### [Improved techniques for fine-tuning flow models via adjoint matching: a deterministic control pipeline](https://arxiv.org/html/2605.06583v1)

flow-model preference tuning 常用 full-trajectory quadratic/KL control。§3～4 把 pretrained velocity field 视为 base dynamics、trainable delta 视为 control，以 terminal reward adjoint 产生 matching target；truncation 只反传 reward-relevant terminal segment，并允许非二次 regularizer。§5、Appendix D 只覆盖 SiT-XL/2、FLUX.2-Klein-4B 与作者 metrics；terminal concentration、deterministic dynamics 与最佳 truncation 尚非通用，未覆盖 stochastic control、video 或 discrete diffusion。该方法节省 trajectory compute、保留 diversity，却可能遗漏早期 credit，并依赖 VJP/base model 和 truncation calibration；不稳时回退 full adjoint 或普通 reward/KL fine-tuning。flow velocity-field optimal-control 分支已写入 `TRAIN-RLHF`。

### [Patch2Vuln: Agentic Reconstruction of Vulnerabilities from Linux Distribution Binary Patches](https://arxiv.org/html/2605.06601v1)

end-answer security Agent 会把 diff/ranker/context/reasoning/validation failure 混在一起。§4 将 ELF extraction、binary diff、function ranking、dossier export、offline reasoning 与 bounded validation 做成 resumable typed stages，各阶段保存 failure receipt。§5～6、Appendix E 仅有 25 个 Ubuntu `.deb` pairs；10/20 localization、11/20 root-cause 与两个 behavior differential，不含 crash/exploit proof，六项先败于 diff/ranker、一项败于 context export。分段归因提高可恢复性却增加工具链、oracle annotation 与敏感 artifact；证据不足保持 `Unknown`，回退人工 reverse engineering。binary-patch pipeline 的 pre-model failure ownership 已写入 `AGENT-WORKFLOW`，并 handoff `PLATFORM-SECURITY`。

### [ActCam: Zero-Shot Joint Camera and 3D Motion Control for Video Generation](https://arxiv.org/html/2605.06667v1)

pose-only control 不能同时约束 viewpoint，持续 depth guidance 又会过约束细节。§3 构造 target-camera-aligned pose/depth，并在同一 denoising run 早期用 pose+depth 锁定 global geometry、后期仅用 pose 恢复 high-frequency motion。§4 只覆盖固定 backbone、公开/作者 camera-motion benchmarks、human preference 与 ablation；depth/pose estimation、occlusion、多角色和真实 3D consistency 未获得保证。staged condition 减少 static/dynamic interference，却依赖 calibration、depth alignment 与 schedule；失败时回退 pose-only、固定 camera 或训练式 controller。condition ownership 随 denoising phase 转移的分支已写入 `MULTIMODAL-GENERATIVE-PARADIGMS`。

上述 18 项完整作者记录见 [限定返修附件](../_sources/daily-20260508/V3_AUTHOR_BOUNDED_REPAIR_EIGHTEEN_FALSE_NEGATIVES_20260915.md)；15 项 root 写回与 3 项 `No Change` 均已通过 fresh non-author final review。本轮没有重新打开 Evidence 或 Books。

## 5. 缺口与下一步

当前没有材料访问阻断。当前 184 个候选均已完成 exact-v1、withdrawal、Score V3、Evidence、Stable Node 与 Books 对读；最新重开的 18 项没有扩大来源、日期、sibling 或重新枚举 619 个 raw identity，所需 15 项长期命题均已由 root 写入唯一 owner。当前机械账为 `619 = 184 retained + 435 closure`、184/184 Evidence complete、`129 deep + 55 standard`、`108 score 7～9 + 76 score 5～6`、`108 Applied + 76 No Change`，`Review Pending = 0`，Books pending writeback = `0`。fresh non-author final review 已通过，没有剩余可执行 Gate。

### 历史修复轨迹（已被 2026-09-15 当前状态取代）

> 以下内容只保留早期审计范围与证据链接，不能作为当前 Gate。当前权威账目与下一步见第 1 节、Round 3 返修记录及第 6 节末尾。

### 历史阻断项（已被十项限定返修取代）

上一轮 post-write 修复已经落实。指定 9 个新 false negative 的作者侧限定返修也已完成；检查到此停止，不扩大来源、其他 closure 或重扫 619 个 raw identity。当前剩余阻断为：

1. 新 reviewer 复核变化范围及 `619 = 141 + 478` 分流，不复用本轮作者或 root 判断冒充独立 Gate；
2. 逐项核验 6 个新 marker 的 owner、正文语义、证据边界和相邻演进位置，以及 3 个 No Change locator；
3. 独立确认 cross-day owner：`2605.05250` 只在 05-08 活动账本拥有候选身份；`2605.06225`、`2605.06241` 归 05-12；`2605.05686` 不属于 05-08 canonical 619。

### 历史 141 项候选检查点（已被当前状态取代）

- 题名与完整摘要反查重开的 24 项已全部取得 exact-v1：23 项使用官方 HTML，`arXiv:2605.06457v1` 使用官方 PDF；没有材料受阻、争议或 withdrawn。
- 24 项逐篇记录了实际 Method、关键 evaluation contract、direct limitation/non-proof、Score V2、owner 与 Books disposition，见 [作者侧 exact-v1 完成记录](../_sources/daily-20260508/AUTHOR_EXACT_V1_COMPLETION.md)。
- 上一轮独立终审指出的 9 个 false negative 已全部取得 exact-v1 HTML、确认本窗 owner 与未撤稿，完成 Score V2、相应深度 Evidence Review、owner/相邻章节对读与 Books Decision；没有材料受阻。
- 本轮 4 个指定 false negative 与有界同类 closure 反查新增的 5 项，也已全部取得 exact-v1、确认 owner 与未撤稿，并完成 Deep Review 与 Books Decision；详见 [第二轮作者修复](../_sources/daily-20260508/V3_FALSE_NEGATIVE_REPAIR_ROUND2_20260914.md)。
- fresh non-author review 新指出的 9 项也已全部取得 exact-v1、确认本窗 owner 与未撤稿，完成 9 项 Deep Review、Stable Node 与 Books Decision；详见 [9 项限定返修](../_sources/daily-20260508/V3_BOUNDED_REPAIR_NINE_FALSE_NEGATIVES_20260915.md)。
- 当前 canonical 工作账本是 [`V3_RECERTIFICATION.json`](../_sources/daily-20260508/V3_RECERTIFICATION.json)：作者侧机械状态为 `619 = 141 reviewed retained + 478 closure`，`Review Pending = 0`。旧 `screening-ledger-final.json` 只保留历史过程，不代表当前候选分母；新 reviewer 完成前，该分流仍不视为最终独立冻结。

### 历史 Books writeback queue（已被当前状态取代）

以下 12 项完成深入证据审阅和 current owner/adjacent 对读，作者判断存在正文尚未承载的长期增量；root 已按 owner/日期协调写入，下一步由非作者 reviewer 逐项检查正文是否忠实承载且不破坏相邻交接：

| Source Family | Owner | 要写入的最小语义增量 |
| --- | --- | --- |
| `SF-2026-ARXIV-2605-05697` | MODEL-SELF-ATTENTION | 单 checkpoint 的请求预算→head compute gate；soft cost 与实际 execution speed 分离，缺 kernel 时回退 dense |
| `SF-2026-ARXIV-2605-05802` | TRAIN-GRPO | mid-rollout informativeness gate；controller 提议早停、group builder 冻结 membership、optimizer 只消费同版本完整组 |
| `SF-2026-ARXIV-2605-05899` | INFER-TENSORRT-LLM | modality compression 改变 expert working-set/cache/prefetch，router 真值与 placement hint 分权 |
| `SF-2026-ARXIV-2605-06067` | TRAIN-PRETRAINING | normalized geometry 与 NVFP4 的 architecture–precision 共设计，保留 BF16/FP8 fallback |
| `SF-2026-ARXIV-2605-06125` | PLATFORM-EVALUATION-SYSTEM | test evidence 拆为 executable、freshness、requirement coverage，需求 revision 后必须重绑 suite identity |
| `SF-2026-ARXIV-2605-06206` | MODEL-MOE | 改变 expert/KV-head ownership 以替换 collective；需要重训且单卡/强层专业化时标准 EP 仍成立 |
| `SF-2026-ARXIV-2605-06350` | INFER-SCHEDULING | post-generation cascade 与 pre-generation router 的累计成本结构不同，升级取决于 marginal quality/cost |
| `SF-2026-ARXIV-2605-06402` | INFER-TENSORRT-LLM | mask learning/annealing 必须与 runtime 可执行 2:4 structure 绑定；无 kernel/质量回归时回退 dense |
| `SF-2026-ARXIV-2605-06481` | MULTIMODAL-WORLD-MODELS | persistent object address 与 mutable content/next state 分离，tracking 失效时进入 uncertain identity |
| `SF-2026-ARXIV-2605-06554` | TRAIN-PRETRAINING | training-only sparse attention 经 dense recovery 形成部署 artifact，不冒充 autoregressive serving mechanism |
| `SF-2026-ARXIV-2605-06639` | AGENT-MULTI-AGENT | 区分静态 delegation 与训练出的 recursive-delegation policy；每层仍保留 authority/budget/receipt |
| `SF-2026-ARXIV-2605-06652` | PLATFORM-EVALUATION-SYSTEM | 无标签时先以 contrast/sensitivity/stability 验证 measurement instrument，再报告比较分数，不升级为 safety certification |

本轮另有 5 项作者侧判断需要写回，现已由 root 落实：

| Source Family | Owner | 要写入的最小语义增量 |
| --- | --- | --- |
| `SF-2026-ARXIV-2605-05715` | PLATFORM-EVALUATION-SYSTEM | decodability、intervention efficacy 与 decision authority 分离；fixed-linear steering 失败时只允许校准后的 abstention/escalation |
| `SF-2026-ARXIV-2605-05750` | TRAIN-RLHF | multi-reward mean 会掩盖 must-have bottleneck；SoftMin 是受 noise、`k` 与 schedule 约束的条件分支，不能替代 hard gate |
| `SF-2026-ARXIV-2605-06036` | TRAIN-RLHF | partial OT 可拒绝 noisy preference mass，但 clean-more-consistent 是待验证前提，需保存 selection identity 与 dispute path |
| `SF-2026-ARXIV-2605-06078` | TRAIN-GRPO | milestone credit 是 terminal reward 与 action-level causal credit 的中间粒度，boundary 由 environment/harness 冻结 |
| `SF-2026-ARXIV-2605-06200` | TRAIN-GRPO | turn-index group 是受限 comparison key，不是真实 state equivalence；group builder 持有 membership，optimizer 只消费冻结 credit |

写回位置、证据范围与 fallback 见 [第二轮精确 Books 写回队列](../_sources/daily-20260508/BOOKS_WRITEBACK_QUEUE_FALSE_NEGATIVES_ROUND2.md)。

其余 12 项重开候选均已在对应章节找到具体承载命题，结论为 `No Change — Existing Coverage`，不是因分数、篇幅或 Books 已满而关闭。精确对读理由见作者完成记录。

challenge 另从旧 closure 中纠正 6 个 false negative：2 项由现有章节承载，4 项形成 [精确写回队列](../_sources/daily-20260508/BOOKS_WRITEBACK_QUEUE_CHALLENGE.md)。这四项现已由 root 按唯一 owner 写入，并完成直接相邻机制的首轮对读；最终语义有效性仍由新的非作者 reviewer 验收。

上一轮独立终审指出的 9 个 false negative 已由修复作者逐项完成：`2605.05700` 与 `2605.06311` 为 `No Change — Existing Coverage`；其余 7 项已由 root 写入共享 Books，并通过 post-write semantic audit，现已同步为 `Applied`。该通过结论只关闭上一轮 9 项，不覆盖本轮 4 个指定项与同类反查新增的 5 项。

### 隔离限制与已知修正

- Google Research、DeepSeek 与 MiMo 的历史日级目录粒度不足，是本窗终态保留项；它们不支持正面证据、Books 或“无遗漏”断言。定点重开条件是取得带精确日期/时刻的官方研究索引、公告或对应原始论文身份；材料到达后只重开本日期的相关 Source Family。
- OpenAI、Anthropic 与 Qwen 在 2026-05-07 的日期级条目无法证明位于 09:00 截点之后，且现有页面没有足够机制或唯一 owner 证据；出现官方时间戳时定点重开，不移动 arXiv owner。
- `arXiv:2605.05527v1` 已降为分母前关闭。Ch56 的 source-family marker 已移除，而 deadline risk、model choice、early exit、batch 与剩余 slack 的泛化调度正文保留；该正文不再由 EdgeServing 单篇证据取得 owner。
- 619 条 owner 使用 DataCite initial registration、OAI 初始 batch date、arXiv ID/version 与 official announcement cadence 交叉确认，公开时间标为 `public-batch-derived`；submitted-v1 较早或 current OAI 被后续 revision 覆盖都不单独构成冲突。另 195 条缺同批次 OAI confirmation，保持在本日报 raw 之外。
- **独立终审结果与修复状态：** 原独立终审已通过当时 88 项 current ledger、51 项 No Change 与 37 项 Books 正文，并从 closure 发现 9 个 false negative。后续各轮已完成相应作者修复和必要写回；这些数字均为历史轨迹。当前权威状态是 `619=184+435`、`129+55`、`108 Applied+76 No Change`，final review 已通过。

## 6. 复核

复核者：`fresh non-author final reviewer（未参与 05-08 作者返修或 root Books 写回）`

结论：通过

- **作者当前自检：** 已核对 `619 = 184 retained + 435 closure`、184/184 exact-v1 Evidence、108/76 评分分层、129/55 审阅深度、`108 Applied + 76 No Change`、`Review Pending = 0`，以及 blocked / disputed / withdrawn = 0 / 0 / 0。
- **限定返修：** 只重开最新 reviewer 点名的 18 项；没有扩大日期、来源、sibling 或 raw identity，也没有重开已通过的 166 项。
- **Books：** 15 项精确 root 写回均已进入唯一 owner 主正文，3 项 `No Change` 由 owner 主正文具体命题承载；作者没有编辑 Books。
- **结论：** 通过；Daily、Evidence 与 Books Gate 均为 Complete。
- **机器检查：** V3 validator、JSON、候选/评分/Books 算术、marker 与 scoped `git diff --check` 均通过；机器结果不替代独立语义复核。

### 历史：Fresh-context 最终独立复核（2026-09-14，已被当前状态取代）

新的非作者 reviewer 已复算 `619 = 106 + 513`、106 项 Score/Evidence 路由、49 项 Applied 正文、57 项 No Change 具体覆盖及 cross-day/withdrawal/source terminal。当前 Applied 与 No Change 范围可以通过，但整体 Gate 仍未通过：在 513 个 closure 的高风险语义反查中，官方 exact-v1 题摘直接确认至少 17 个 false negative；`2605.05219` 的 Evidence 小节另有 evaluation contract 残句及 Applied/No Change 解释冲突。

精确 family、原文反例、owner 建议与最小修复范围见 [V3 fresh-context 最终独立复核](../_sources/daily-20260508/V3_FRESH_CONTEXT_FINAL_REVIEW_20260914.md)。本轮没有扩展来源、日期或 raw identity，也没有修改 Books。日报保持 `进行中`；只有这 17 项及同类高风险 closure 的有界反查完成、必要 Books 写回落实并由另一位未参与修复者通过后，才能登记 Complete。
### 历史 Gate 检查点（2026-09-15，已被当前状态取代）

- **Canonical ledger：** [V3_RECERTIFICATION.json](../_sources/daily-20260508/V3_RECERTIFICATION.json)，`619 = 141 retained + 478 closure`。
- **Evidence：** 141/141 complete，101 deep + 40 standard，`Review Pending = 0`。
- **Books：** 当前 75 `Integrate — Applied` + 66 `No Change — Existing Coverage`；69/63 已通过上一轮非作者定位，本轮新增 6/3 等待新的统一终审。
- **Materials：** blocked / disputed / withdrawn = 0 / 0 / 0。
- **Author repair：** fresh non-author closure challenge 指定的 9 个 false negative 已全部重开并完成；没有扩大到其他 closure。
- **尚未闭合：** 新的 non-author final Gate。
- **状态：** `Ongoing`，`final_independent_signoff = false`。

### 历史：Fresh-context 最终独立复核 Round 2（2026-09-15，已被当前状态取代）

作为上一轮失败记录，新的非作者 reviewer 当时复算 `619 = 128 retained + 491 closure`、128/128 Evidence、49 项 Applied + 16 项已写回但仍待独立 post-write review + 63 项 No Change，并直接检查了 16 项 root Books 写回。16 个 marker 均唯一且位于 `Review notes` 之前，但 `2605.06216` 与 `2605.06548` 的新机制分别早于本章 baseline / 基础机制说明，章内演进顺序仍需修正。

整体 Gate **未通过**。对 closure 的独立 exact-v1 反查确认 `2605.05329`、`2605.05331`、`2605.06609`、`2605.06660` 四个 false negative；它们分别涉及 annotator policy/evaluation、multimodal representation artifact、Transformer in-context mechanism 与 verifier-backed synthetic training。第 3 节候选表当时另缺 22 项。上述 Evidence、展示层与状态问题现已由作者 Round 3 修复；Books 写回与重排已经完成，新的非作者终审仍未完成。

完整证据、具体 owner 建议与最小修复范围见 [V3 fresh-context 最终语义终审 Round 2](../_sources/daily-20260508/V3_FRESH_FINAL_REVIEW_ROUND2_20260915.md)。本轮没有修改 Books，也没有扩大来源或 raw identity；状态继续为 `Ongoing`，`final_independent_signoff = false`。

### 历史：作者定点返修 Round 3（2026-09-15，已被当前状态取代）

作者已完成四项 false negative 的 exact-v1 深入审阅与 Books Decision、有界复核 12 个同错误层 closure、补齐第 3 节 22 个既有候选，并同步 canonical ledger。详细 Method、evaluation、limitations 与 family-specific closure 理由见 [Round 3 作者返修记录](../_sources/daily-20260508/V3_AUTHOR_TARGETED_REPAIR_ROUND3_20260915.md)。

root 已严格按 [Round 3 Books 写入/重排队列](../_sources/daily-20260508/ROOT_BOOKS_WRITEBACK_QUEUE_ROUND3_20260915.json) 完成 4 项新插入与 2 项既有块移动。作者与 root 都不签署最终通过。当前状态为 `Ongoing`，`final_independent_signoff = false`。

### 历史：Fresh non-author 最终复核（2026-09-15，已被当前状态取代）

新的非作者 reviewer 已复算当前快照 `619 = 132 retained + 487 closure`，核验 132 项 Evidence/Score/owner/disposition、4 个 Round 3 新增正文、2 个移动块、69 个 Applied main-body locator/owner 与 63 个 No Change 命题 locator。上述范围以及当前 withdrawal/access/materials 状态均通过。

整体 Gate 仍 **未通过**：对 487 个 closure 做独立分层反查时，官方 exact-v1 题摘确认至少 9 个 false negative：`2605.05278`、`2605.05485`、`2605.05646`、`2605.05702`、`2605.05709`、`2605.05892`、`2605.06124`、`2605.06192`、`2605.06207`。这些项目分别涉及 MoE routing/control、reasoning-to-executable artifact、visual-tokenizer objective/capacity、synthetic task/reward ownership、multimodal reconstruction safety、activation intervention、single-pass generative inference 与 action-conditioned world state。它们来自既有 619 raw set，不扩大来源或日期。

精确 primary 反例、owner 建议和最小返修范围见 [V3 fresh non-author 最终复核](../_sources/daily-20260508/V3_FRESH_NONAUTHOR_FINAL_REVIEW_20260915.md)。日报保持 `进行中`，`final_independent_signoff = false`；返修不得推倒本轮已验收的现有 132 Evidence 与 69/63 Books 范围。

候选表和 Evidence 小节内旧的中间复核 suffix 已在本轮同步清除；69 项既有 Applied 的 item-level 状态与上一轮通过结论一致。

### 历史：九项限定返修检查点（2026-09-15，已被当前状态取代）

作者只重开 `2605.05278`、`2605.05485`、`2605.05646`、`2605.05702`、`2605.05709`、`2605.05892`、`2605.06124`、`2605.06192`、`2605.06207`。9 项均完成 exact-v1、withdrawal、Score V2、Evidence、Stable Node 与 Books compare；账本现为 `619 = 141 retained + 478 closure`。

6 项需要新增长期命题，已由 root 按 [精确 queue](../_sources/daily-20260508/ROOT_BOOKS_WRITEBACK_QUEUE_BOUNDED_REPAIR_20260915.json) 写回并登记 item-level 状态；3 项由具体既有命题承载。作者没有编辑 Books，也不签署独立 Gate。当前最终状态仍是 `Ongoing`，`final_independent_signoff = false`。

### 历史：九项返修后的 fresh non-author 终审（2026-09-15，已被当前状态取代）

新 reviewer 复算并通过 `619 = 141 retained + 478 closure`、141 项 Evidence/Score/owner/disposition、
`101 deep + 40 standard`、`75 Applied + 66 No Change` 的机械账；9 个 reopened family 的 exact-v1、
withdrawal/access 状态与 6 个 root Books 新段也通过。六个新段无需返工。

整体 Gate 仍 **未通过**。`2605.05709` 的 `No Change` 所引用命题只存在于 Ch72 `Review notes` 后的历史归档句，
主正文没有承载 reconstruction-layer attack；另对 478 个 closure 的 12 项有界高风险题摘挑战确认 10 个新的
contribution-gate false negative。精确 family、原文增量、建议 owner 与最小返修范围见
[九项返修后的 fresh non-author 终审](../_sources/daily-20260508/V3_FRESH_NONAUTHOR_FINAL_REVIEW_AFTER_NINE_20260915.md)。
本日报继续保持 `Ongoing`，不得重开已通过的 141 项 Evidence 或 6 个新 Books 段。

### 历史：十项限定返修后的作者检查点（2026-09-15，已被当前状态取代）

作者只重开 `2605.05566`、`2605.05602`、`2605.05676`、`2605.05781`、`2605.05826`、`2605.05893`、`2605.06460`、`2605.06507`、`2605.06557`、`2605.06643`。10/10 exact-v1 可访问且未见 withdrawal banner；8 项 Deep、2 项 Standard；`2605.05676` 因进入 Books 按 Integration Gate 提升为 Deep。11 个同错误理由 sibling challenge 没有新增 false negative。

`2605.05709` 已由 root 写入 Ch72 主正文并同步为 `Integrate — Applied`。新增 5 项也已由 root 按 [精确写回队列](../_sources/daily-20260508/ROOT_BOOKS_WRITEBACK_QUEUE_TEN_FALSE_NEGATIVES_20260915.json) 落入唯一 owner，marker 均位于 `Review notes` 前。作者没有修改共享 Books，也不签署独立 Gate。

当前 canonical 机械账为 `619 = 151 retained + 468 closure`；Evidence 151/151 complete，`109 deep + 42 standard`，`90 score 7–9 + 61 score 5–6`；Books 为 `81 Applied + 70 No Change`。状态保持 `Ongoing`，`final_independent_signoff = false`。

### 历史：十项返修后的 fresh non-author 最终复核（2026-09-15，已被当前状态取代）

新 reviewer 已通过 `619 = 151 retained + 468 closure`、151/151 Evidence、`109 deep + 42 standard`、
`81 Applied + 70 No Change` 的机械账，并核验十个 reopened family、分层抽样的现有 Evidence/Books 处置及六个 root Books marker。
六个 marker 均唯一、位于 `Review notes` 前，owner 和正文语义无需返工。

整体 Gate 仍 **未通过**。对 closure 固定做 24 项风险分层题摘挑战时确认 15 个 contribution-gate false negative：
`2605.05662`、`2605.05668`、`2605.05742`、`2605.06070`、`2605.06170`、`2605.06201`、`2605.06509`、
`2605.05714`、`2605.05741`、`2605.05851`、`2605.06165`、`2605.06183`、`2605.06324`、`2605.06342`、
`2605.06529`。它们来自既有 619 raw set，不扩大来源或日期。

精确题摘反例、owner 建议和有限返修范围见
[十项返修后的 fresh non-author 最终复核](../_sources/daily-20260508/V3_FRESH_NONAUTHOR_FINAL_REVIEW_AFTER_TEN_20260915.md)。
本日报继续保持 `Ongoing`，`final_independent_signoff = false`；不得重开本轮已通过的 151 项 Evidence、81/70 Books 分流与六个 Books 段。

### 历史：十五项返修后的 fresh non-author 最终复核（2026-09-15，已被当前状态取代）

新 reviewer 复算并通过当前快照 `619 = 166 retained + 453 closure`、166/166 Evidence、`124 deep + 42 standard` 与 Score V3 算术；十五个 reopened exact-v1 均可访问且未见 withdrawal。3 项 No Change 均由主正文具体命题承载；12 个新增 Books marker 均唯一、owner 正确、位于 `Review notes` 前，且完整表达基线、约束变化、机制/状态责任、trade-off/failure、fallback 与非外推边界。Books 本体无需返工。

整体 Gate 仍 **未通过**。对既有 453 个 closure 固定抽取 28 个跨模型/训练、推理/硬件、多模态、Evaluation/Security 与 Agent 的高风险 family，逐项读取完整摘要后确认 18 个 contribution-gate false negative：`2605.05245`、`2605.05277`、`2605.05386`、`2605.05415`、`2605.05438`、`2605.05495`、`2605.05503`、`2605.05638`、`2605.05718`、`2605.05980`、`2605.06040`、`2605.06052`、`2605.06247`、`2605.06376`、`2605.06480`、`2605.06583`、`2605.06601`、`2605.06667`。这些材料都来自既有 619 raw identities，不扩大来源或日期。

另一个状态不一致必须同批修复：十二项实际写回已经存在且通过验收，但 canonical ledger 的 item-level `books_disposition` 仍为 `Integrate — Pending root writeback`，需要同步为 `Integrate — Applied`。精确题摘反例、建议 owner、继续 closure 的十项样本与限定返修范围见 [十五项返修后的 fresh non-author 最终复核](../_sources/daily-20260508/V3_FRESH_NONAUTHOR_FINAL_REVIEW_AFTER_FIFTEEN_20260915.md)。本日报继续保持 `Ongoing`，不得推倒已经通过的 166 项 Evidence、3 项 No Change 或 12 个 Books 段。

### 历史：十八项限定返修后的作者检查点（2026-09-15，已被当前 final review 取代）

作者只重开上一节指定的 18 个既有 Source Family。18/18 official exact-v1 HTML 可访问，题名与账本一致，未见 withdrawal banner；全部完成 Score V3、相应深度 Evidence、Stable Node 与目标/相邻 Books 对读。没有扩展日期、来源、sibling 或重新枚举 619 raw identities。

| Source Family | Score / Review | Stable Node | 当前 Books Decision |
| --- | --- | --- | --- |
| `2605.05245` | `2+3+2=7` / Deep | `AGENT-RAG` | Integrate — Applied；待 fresh post-write review |
| `2605.05277` | `2+3+2=7` / Deep | `PLATFORM-SECURITY` | Integrate — Applied；待 fresh post-write review |
| `2605.05386` | `2+2+2=6` / Standard | `AGENT-PLANNING` | No Change — Existing Coverage |
| `2605.05415` | `3+2+2=7` / Deep | `TRAIN-RLHF` | Integrate — Applied；待 fresh post-write review |
| `2605.05438` | `2+2+2=6` / Standard | `TRAIN-SFT` | Integrate — Applied；待 fresh post-write review |
| `2605.05495` | `2+1+2=5` / Standard | `MODEL-TRANSFORMER-LAYER` | No Change — Existing Coverage |
| `2605.05503` | `2+2+2=6` / Standard | `PLATFORM-SECURITY` | Integrate — Applied；待 fresh post-write review |
| `2605.05638` | `2+2+2=6` / Standard | `PLATFORM-EVALUATION-SYSTEM` | Integrate — Applied；待 fresh post-write review |
| `2605.05718` | `3+2+2=7` / Deep | `INFER-DYNAMO` | Integrate — Applied；待 fresh post-write review |
| `2605.05980` | `2+2+2=6` / Standard | `AGENT-REFLECTION` | Integrate — Applied；待 fresh post-write review |
| `2605.06040` | `2+1+2=5` / Standard | `AGENT-PLANNING` | No Change — Existing Coverage |
| `2605.06052` | `2+2+2=6` / Standard | `INFER-TENSORRT-LLM` | Integrate — Applied；待 fresh post-write review |
| `2605.06247` | `2+2+2=6` / Standard | `MULTIMODAL-WORLD-MODELS` | Integrate — Applied；待 fresh post-write review |
| `2605.06376` | `2+2+2=6` / Standard | `MULTIMODAL-GENERATIVE-PARADIGMS` | Integrate — Applied；待 fresh post-write review |
| `2605.06480` | `2+2+2=6` / Standard | `PLATFORM-EVALUATION-SYSTEM` | Integrate — Applied；待 fresh post-write review |
| `2605.06583` | `3+2+2=7` / Deep | `TRAIN-RLHF` | Integrate — Applied；待 fresh post-write review |
| `2605.06601` | `2+2+2=6` / Standard | `AGENT-WORKFLOW` | Integrate — Applied；待 fresh post-write review |
| `2605.06667` | `2+2+2=6` / Standard | `MULTIMODAL-GENERATIVE-PARADIGMS` | Integrate — Applied；待 fresh post-write review |

完整的 baseline、约束变化、机制/state ownership、evaluation、trade-off/failure/fallback 与 evidence boundary 见 [18 项限定返修记录](../_sources/daily-20260508/V3_AUTHOR_BOUNDED_REPAIR_EIGHTEEN_FALSE_NEGATIVES_20260915.md)。15 项精确 root 写回要求见 [Books writeback queue](../_sources/daily-20260508/ROOT_BOOKS_WRITEBACK_QUEUE_EIGHTEEN_FALSE_NEGATIVES_20260915.json)。三项 No Change 由主正文具体命题承载，不依赖 Review notes。

当前机械账为 `619 = 184 retained + 435 closure`；184/184 Evidence complete，`129 deep + 55 standard`，`108 score 7～9 + 76 score 5～6`；Books 为 `108 Applied + 76 No Change`。blocked / disputed / withdrawn = `0 / 0 / 0`。root 已完成 15 项正文写回；作者与 root 均不签署最终 Gate，状态保持 `Ongoing`，`final_independent_signoff = false`。

### 历史：十五项 root Books 写回（2026-09-15，已被当前 final review 取代）

root 已按唯一 owner 将 15 项机制增量合并到 Books 主正文，并保持“旧方案成立条件 → 新约束 → 状态/控制责任变化 → trade-off、failure 与 fallback → exact-v1 证据边界”的叙述链。15/15 Source Family 各有唯一 `semantic-body-binding`，均位于对应章节首个 `## Review notes` 之前；没有把论文摘要或通用“已吸收”标签当成正文。

写回记录见 [root 审计](../_sources/daily-20260508/ROOT_BOOKS_WRITEBACK_EIGHTEEN_FALSE_NEGATIVES_20260915.md)。下一步只允许新的 non-author reviewer 复核这 15 个段落、全局状态守恒与最终 Gate；不能由作者或 root 自签。

### 当前 fresh non-author final review（2026-09-15）

新的 reviewer 未参与作者返修或 root Books 写回。第 3 节与第 4 节各有 184 个唯一候选并与 canonical retained 集合完全相同；独立复算 `619=184+435`、`184=129 deep+55 standard`、`184=108 Applied+76 No Change`。最新 15 个 binding 当前仍全局唯一、成对、位于对应 owner 首个 `## Review notes` 前，正文没有漂移；3 个 `No Change` 的主正文承载也仍成立。最终验收记录见 [fresh non-author final review](../_sources/daily-20260508/V3_FRESH_NONAUTHOR_FINAL_REVIEW_184_PROJECTION_20260915.md)。
