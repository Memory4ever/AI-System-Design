# 2026-06-11、12、15～19 Fresh Final Audit

**审计角色：** 非作者 fresh-context reviewer
**审计范围：** 七份 Daily 的 V3 candidate denominator、Books proposal、reverse audit、目标章节正文与 `Review notes` 边界
**结论：** `Change 已同步`。candidate denominator 已按长期系统贡献门槛冻结，24 条错误 adoption residue 已清理；Books 仍有 216 个 family 需要 canonical owner 正文，七份日报因此保持进行中。

## 1. 判定合同

保留候选必须至少改变一项可迁移的长期边界：状态/数据/控制权、执行与资源契约、evaluation/release contract，或修正 Books 既有结论。单一 benchmark、局部算法、模型/表示小改、框架案例、ROADMAP 可映射性本身均不足以准入。标题足以确定范围时直接闭合；边界不清时使用本地账本中的完整摘要。

Books 判定只承认 `Review notes` 之前的连贯机制正文。source trace、marker、Review notes 后的“已吸收语义”不能替代正文；Existing Coverage 必须落到既有命题级锚点；真正新增内容按 canonical owner 合并。

## 2. 总体结果

| 日期 | 旧 retained | 终审 retained | 恢复误删 | 撤销旧准入 | 已实际 Integrate | Existing Coverage | Books pending | owner groups | Gate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 2026-06-11 | 27 | 24 | 0 | 3 | 1 | 4 | 19 | 11 | Denominator Pass / Books Pending |
| 2026-06-12 | 30 | 24 | 0 | 6 | 1 | 3 | 20 | 14 | Denominator Pass / Books Pending |
| 2026-06-15 | 32 | 22 | 0 | 10 | 0 | 0 | 22 | 14 | Denominator Pass / Books Pending |
| 2026-06-16 | 107 | 58 | 4 | 53 | 1 | 0 | 57 | 22 | Denominator Pass / Books Pending |
| 2026-06-17 | 38 | 28 | 0 | 10 | 0 | 0 | 28 | 15 | Denominator Pass / Books Pending |
| 2026-06-18 | 35 | 28 | 0 | 7 | 0 | 1 | 27 | 14 | Denominator Pass / Books Pending |
| 2026-06-19 | 61 | 47 | 1 | 15 | 1 | 3 | 43 | 17 | Denominator Pass / Books Pending |
| **合计** | **330** | **231** | **5** | **104** | **4** | **11** | **216** | **28 unique owners** | **Books Pending** |

终审保留率按 canonical raw identity 计算为 `231 / 4429 = 5.2%`；该比率只是逐项判断结果，不是配额。最终 231 个候选中，4 项已实际形成正文机制链、11 项已有命题级覆盖、216 项进入 28 个 canonical owner 写回队列。

## 3.1 2026-06-11 逐项审计

| arXiv | 标题 | 旧状态 → 终审 | Books 判定 | 独立判断 |
| --- | --- | --- | --- | --- |
| `2606.11257` | Energy-Efficient On-Device RAG on a Mobile NPU: System Design and Benchmark on Snapdragon X Elite | `de_admit` → `de-admit` | — | 特定硬件或单一部署点的性能案例；没有改变可迁移的执行、状态或控制契约。 |
| `2606.11265` | When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines | `integrate` → `retain` | Integrate proposal — `AGENT-RAG` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We identify retrieval granularity mismatch as a key reason for this failure: document-level adversarial signals are often fragmented during chunking, while rerankers favor locally coherent and answer-bearing pa… |
| `2606.11270` | Quantifying Subliminal Behavioral Transfer Ratios in Language Model Distillation | `integrate` → `retain` | Integrate proposal — `TRAIN-DATA` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Distillation of a language model intended to transfer benign behavior to a student model may also transfer undesirable characteristics, if they are present in the teacher model, a phenomenon known as subliminal… |
| `2606.11290` | FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse | `integrate` → `retain` | Integrate proposal — `AGENT-WORKFLOW` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To this end, we present FlowBank, a three-stage framework for portfolio-based agentic workflow optimization |
| `2606.11349` | Knowing When to Ask: Self-Gated Clarification for Hierarchical Language Agents | `no_change_existing_coverage` → `retain` | Existing Coverage — `books/part-07-agent/79-planning.md` / `先校准不确定性，再决定行动、询问或探索` | 保留：摘要给出可定位机制——Rather than treating clarification as an external uncertainty trigger, we propose ACTION-RATING, a formulation that places it inside the agent's action space on a shared ordinal scale with navigation, so that a… |
| `2606.11357` | TileFuse: A Fused Mixed-Precision Kernel Library for Efficient Quantized LLM Inference on AMD NPUs | `integrate` → `retain` | Integrate proposal — `INFER-DECODE` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——In this work, we present TileFuse, a close-to-metal mixed-precision kernel library for AMD XDNA2 NPUs that targets GEMM/GEMV-based operators in quantized LLM inference |
| `2606.11375` | When Probing Accuracy Saturates, Fragility Resolves: A Complementary Metric for LLM Pre-Training Analysis | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.11387` | Small Experiments, Cheaper Decisions: A Case Study in Staged Promotion for Micro-Pretraining | `integrate` → `retain` | Existing Coverage — `books/part-04-training-system/28-pretraining.md` / `Scaling-law Pilot 也是有预算的实验调度` | 保留：摘要给出可定位机制——Short pretraining runs can reduce experimental cost, but they can also over-promote configurations that only look strong at tiny budgets |
| `2606.11409` | Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models | `integrate` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We propose a compute-aware evaluation framework based on computational pressure, measured in cumulative floating-point operations (FLOPs), as a proxy for adversarial effort |
| `2606.11445` | Forecasting Future Behavior as a Learning Task | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.11520` | ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories | `no_change_existing_coverage` → `retain` | Existing Coverage — `books/part-04-training-system/27-data.md` / `Synthetic data：从“先生成再打分”到 Specification Compilation` | 保留：摘要给出可定位机制——We propose ISE (Intent -&gt; Simulate -&gt; Execute), a three-stage synthesis paradigm that addresses these gaps jointly |
| `2606.11522` | Search Discipline for Long-Horizon Research Agents | `de_admit` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.11543` | SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior | `integrate` → `retain` | Integrate proposal — `AGENT-REFLECTION`；`条件化机制分支与共存边界` 约 L252 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We present SkillJuror, a framework for evaluating Skill writing paradigms through semantically controlled variants, matched multi-trial evaluations, and trajectory evidence while holding task knowledge fixed |
| `2606.11632` | Sovereign Assurance Boundary: Certificate-Bound Admission for Agentic Infrastructure | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Agentic infrastructure introduces a critical control-plane authorization problem: non-deterministic reasoning systems can propose high-stakes mutations to production resources, yet existing security mechanisms … |
| `2606.11671` | Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present Runtime Skill Audit (RSA), a dynamic analysis method that audits skills by asking what the skill-mediated agent actually does under targeted runtime conditions |
| `2606.11686` | Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness | `integrate` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present layer-isolated evaluation: a deployed ordering agent is decomposed into a fixed taxonomy of layers (ontology, intent, routing, decomposition, escalation, safety, memory, and cross-cutting envelope/de… |
| `2606.11688` | Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents | `integrate` → `retain` | Integrate proposal — `AGENT-WORKFLOW` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present Autopilot, an execution model that makes silent fabricated success structurally impossible rather than merely rarer |
| `2606.11690` | Beyond Per-Token Pricing: A Concurrency-Aware Methodology for LLM Infrastructure Cost Estimation | `integrate` → `retain` | Integrated — `books/part-06-ai-infrastructure/70-cost.md` / `Utilization 应由实际负载推出，而不是由计算器假定`（Review notes 前完整机制链） | 保留：摘要给出可定位机制——We show that this assumption is the dominant source of error: on identical H100 hardware, effective cost spans \$0.21 to \$15.25 per million output tokens, an underutilization penalty of 2.5-24x across low-to-m… |
| `2606.11718` | Making Locality-aware GEMM Compatible with Page-Granularity Placement on Chiplet GPUs | `integrate` → `retain` | Integrate proposal — `INFER-GPU-MEMORY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We propose Chiplet-Contiguous Layout, a global memory layout that stores chiplet-local data contiguously |
| `2606.11806` | External Experience Serving in Production LLM Systems: A Deployment-Oriented Study of Quality-Cost Trade-offs | `integrate` → `retain` | Integrate proposal — `AGENT-MEMORY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Production LLM systems accumulate reusable operational experience, but the practical deployment issue is not merely whether such experience can help |
| `2606.11871` | WarpGuard: Protected-Site Control-Flow Integrity for CUDA SASS Binaries | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present WarpGuard, to our knowledge the first protected-site CFI system for CUDA device binaries operating on executed SASS |
| `2606.11878` | Gerrymandering the Warp: Non-Control-Data Attacks on CUDA Collective Decision | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We identify this participation metadata as decision-making non-control data |
| `2606.11916` | Characterizing Software Aging in GPU-Based LLM Serving Systems | `integrate` → `retain` | Integrate proposal — `PLATFORM-MONITORING`；`条件化机制分支与共存边界` 约 L331 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——This paper proposes an empirical methodology to study software aging in GPU-based LLM serving systems |
| `2606.11949` | Online Shift Detection and Conformal Adaptation for Deployed Safety Classifiers | `integrate` → `retain` | Integrate proposal — `PLATFORM-MONITORING`；`条件化机制分支与共存边界` 约 L331 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——Reasoning models deployed as safety monitors exhibit a systematic vulnerability: reasoning-token budget starvation |
| `2606.11998` | Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce \emph{bootstrapped monitoring}, a protocol that addresses this by inserting a stronger, intermediate untrusted model with transparent chain-of-thought reasoning into the oversight chain |
| `2606.12243` | VIA-SD: Verification via Intra-Model Routing for Speculative Decoding | `no_change_existing_coverage` → `retain` | Existing Coverage — `books/part-05-inference-system/48-speculative-decoding.md` / `两级 draft/full verification 的中间 routed verifier 分支` | 保留：摘要给出可定位机制——Yet we find that many rejected tokens can be verified correctly by a slim submodel derived from the full verifier via intra-model routing, instead of the full verifier |
| `2606.12320` | A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.12329` | PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents | `integrate` → `retain` | Integrate proposal — `AGENT-MEMORY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present projectmem, an open-source, local-first memory and judgment layer for AI coding agents |
| `2606.12370` | Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling | `integrate` → `retain` | Integrate proposal — `INFER-SPECULATIVE-DECODING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To address this bottleneck, we present Bebop, a systematic study of MTP in LLM post-training, and offer practical recipes to integrate MTP into large-scale RL pipelines |

## 3.2 2026-06-12 逐项审计

| arXiv | 标题 | 旧状态 → 终审 | Books 判定 | 独立判断 |
| --- | --- | --- | --- | --- |
| `2606.12385` | Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs | `integrate` → `retain` | Integrate proposal — `TRAIN-DATA` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce ModSleuth, an agentic system that recursively reconstructs LLM dependency graphs from public artifacts with source-grounded evidence |
| `2606.12469` | Influence Factors on RAG Poisoning | `integrate` → `retain` | Integrate proposal — `AGENT-RAG` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Retrieval-Augmented Generation (RAG) systems enhance large language models by grounding responses in retrieved documents from external knowledge sources at inference time |
| `2606.12487` | DynamicPTQ: Mitigating Activation Quantization Collapse via Residual-Stream Dynamics | `integrate` → `retain` | Integrate proposal — `INFER-TENSORRT-LLM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——In this paper, we show that massive activations emerge and disappear in a phase-wise pattern across network depth, triggering large residual changes |
| `2606.12556` | ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories | `integrate` → `retain` | Integrate proposal — `INFER-GPU-MEMORY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——In this paper, we propose ITME (Inference Tiered Memory Expansion), which leverages a CXL-hybrid memory to present a massive, TB-scale byte-addressable remote memory expansion |
| `2606.12688` | M*: A Modular, Extensible, Serving System for Multimodal Models | `integrate` → `retain` | Integrate proposal — `INFER-KSERVE-TOPOLOGY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Here we present M*, a universal serving system for efficient serving of composite AI models |
| `2606.12703` | SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present Signed Memory with Smoothed Retrieval (SMSR), the first defence with a certified robustness bound for this setting |
| `2606.12736` | Benchmarking AI Agents for Addressing Scientific Challenges Across Scales | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.12737` | PI-Hunter: Automated Red-Teaming for Exposing and Localizing Prompt Injections | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We propose PI-Hunter, an automated agentic auditing framework for proactive vulnerability exposure in LLM agents |
| `2606.12764` | Detecting Functional Memorization in Code Language Models | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.12765` | Rigel: Reverse-Engineering the Metal 4.1 Tensor Compute Path on the Apple M4 Max GPU | `integrate` → `retain` | Integrate proposal — `INFER-TENSORRT-LLM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present Rigel, an empirical characterization of this path on a single Apple M4 Max (a pre-neural-accelerator generation) |
| `2606.12797` | The Containment Gap: How Deployed Agentic AI Frameworks Fail Public-Facing Safety Requirements | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Agentic large language model systems that autonomously invoke tools, maintain persistent memory, and execute multi-step plans are increasingly deployed in public-facing domains, including government services, h… |
| `2606.12918` | MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.12950` | Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-Based Multi-Agent Systems | `integrate` → `retain` | Integrate proposal — `INFER-SCHEDULING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present Maestro, a workload-aware scheduling system designed for LLM-MAS serving under strict GPU budgets |
| `2606.12978` | Trajectory-Level Redirection Attacks on Vision-Language-Action Models | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-EMBODIED-VLA` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We identify a stronger trajectory-level failure mode: a prompt that still $\textit{appears}$ to specify the intended task but redirects the final physical outcome |
| `2606.13003` | The Illusion of Multi-Agent Advantage | `no_change_existing_coverage` → `retain` | Existing Coverage — `books/part-07-agent/82-multi-agent.md` / `多 Agent 拓扑必须先通过 Equal-budget Pareto Admission` | 保留：摘要给出可定位机制——To isolate these failures from limitations inherent to task structure, we introduce a diagnostic synthetic dataset tailored for MAS featuring explicit task decomposition, context separation and parallelization … |
| `2606.13044` | No Hidden Prompts Needed! You Can Game AI Peer Review with Presentation-Only Revisions | `integrate` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.13053` | EV-WM: Event-Verified World Models for Long-Horizon Robotic Manipulation | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-WORLD-MODELS` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce \textbf{EV-WM}, a predicate-grounded verification framework for world-model planning |
| `2606.13092` | Certified World Models: Predictability Across Configuration, Horizon, and Resolution | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-WORLD-MODELS` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Scale buys interpolation; structure buys certifiable transfer |
| `2606.13145` | The Clustering Strikes Back: Building Cost-Effective and High-Performance ANNS at Scale with Helmsman | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.13174` | Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents | `integrate` → `retain` | Integrate proposal — `AGENT-WORKFLOW`；`条件化机制分支与共存边界` 约 L815 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We introduce Test-time Rule Acquisition and Compiled Enforcement (TRACE), a drop-in skill-layer pipeline for coding-agent runtimes that mines user corrections, rewrites them as atomic rules, and compiles them i… |
| `2606.13221` | From Uncertain Judgments to Calibrated Rankings: Conformal Elo Estimation for LLM Evaluation | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.13392` | MiniMax Sparse Attention | `no_change_existing_coverage` → `retain` | Existing Coverage — `books/part-02-model/22-long-context.md` / `Native Sparse Attention 的 selector 与 execution contract` | 保留：摘要给出可定位机制——We introduce MiniMax Sparse Attention (MSA), a blockwise sparse attention built upon Grouped Query Attention (GQA) |
| `2606.13426` | Accelerating Speculative Diffusions via Block Verification | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-GENERATIVE-PARADIGMS` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——In this work, we introduce a novel scheme that efficiently implements the original speculative sampling mechanism for diffusion models |
| `2606.13449` | Toward Instructions-as-Code: Understanding the Impact of Instruction Files on Agentic Pull Requests | `integrate` → `retain` | Integrated — `books/part-07-agent/74-prompt.md` / `Prompt 生命周期`（Review notes 前完整机制链） | 保留：摘要给出可定位机制——We find that specifying instructions for AI-agents does not necessarily lead to better results |
| `2606.13496` | Budget-Constrained Step-Level Diffusion Caching | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-GENERATIVE-PARADIGMS` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——In this work, we propose BudCache, which inverts this formulation: rather than letting per-step error thresholds dictate the runtime cost, we fix the compute budget in advance and search for the cache policy th… |
| `2606.13501` | GF-DiT: Scheduling Parallelism for Diffusion Transformer Serving | `integrate` → `retain` | Integrate proposal — `INFER-SCHEDULING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present GF-DiT, a policy-programmable runtime for elastic DiT serving that dynamically adapts the parallelism of running requests according to workload demands and service objectives |
| `2606.13608` | AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility | `integrate` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We further introduce AgentBeats as a concrete realization of AAA: we identify five practical operation modes that make standardized assessment compatible with real-world constraints on openness, privacy, and re… |
| `2606.13610` | One Polluted Page Is Enough: Evaluating Web Content Pollution in LLM Recommenders | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.13621` | Beyond Runtime Enforcement: Shield Synthesis as Defensibility Analysis for Adversarial Networks | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.13629` | Valid Inference with Synthetic Data via Task Exchangeability | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.13643` | Recursive Agent Harnesses | `no_change_existing_coverage` → `retain` | Existing Coverage — `books/part-07-agent/81-workflow.md` / `Evaluator-Driven Search：Harness revision local search` | 保留：摘要给出可定位机制——Recursive language models (RLMs) showed that recursion over model calls is an effective strategy for long-context reasoning, and production coding agents have begun to write code that spawns subagents at scale,… |
| `2606.13662` | EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.13663` | HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents | `integrate` → `retain` | Integrate proposal — `AGENT-TOOL-CALLING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce \textbf{HyperTool}, a unified executable MCP-style tool interface that changes the model-visible unit of tool execution |
| `2606.13681` | EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments | `integrate` → `retain` | Integrate proposal — `AGENT-MEMORY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To address this gap, we introduce EvoArena, a benchmark suite that models environment changes as sequences of progressive updates across terminal, software, and social domains |

## 3.3 2026-06-15 逐项审计

| arXiv | 标题 | 旧状态 → 终审 | Books 判定 | 独立判断 |
| --- | --- | --- | --- | --- |
| `2606.13708` | Tiara: A Programmable Line-Rate ISA for Remote Memory Access | `integrate` → `retain` | Integrate proposal — `INFER-PD-DISAGGREGATION` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present Tiara, a compact, statically verifiable instruction set that executes on the memory-side NIC |
| `2606.13733` | How Task Structure Limits Multi-Agent Success: An Information-Theoretic Analysis | `integrate` → `retain` | Integrate proposal — `AGENT-MULTI-AGENT` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Multi-agent systems (MAS) were expected to overcome the limitation of single-agent systems (SAS) through collaboration |
| `2606.13740` | Efficient On-Device Diffusion LLM Inference with Mobile NPU | `integrate` → `de-admit` | — | 特定硬件或单一部署点的性能案例；没有改变可迁移的执行、状态或控制契约。 |
| `2606.13757` | SEVRA-BENCH: Social Engineering of Vulnerabilities in Review Agents | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.13873` | Natively Unlearnable Large Language Models | `integrate` → `retain` | Integrate proposal — `TRAIN-DATA`；`条件化机制分支与共存边界` 约 L763 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We propose NULLs (Natively Unlearnable LLMs), a model class that satisfies the two opposing goals of isolating source-specific contributions and learning jointly across sources, by training a set of shared back… |
| `2606.13904` | SANA: What Matters for QA Agents over Massive Data Lakes? | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.13949` | Minim: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We propose MINIM, a trusted local broker that performs privacy-aware minimization on the client side before any observation leaves the device |
| `2606.13968` | STREAM: Multi-Tier LLM Inference Middleware with Dual-Channel HPC Token Streaming | `integrate` → `retain` | Integrate proposal — `PLATFORM-GATEWAY`；`条件化机制分支与共存边界` 约 L168 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——Researchers and practitioners working with large language models face a fragmented landscape: local models are free and private but hardware limits the model size and context windows a researcher can use; insti… |
| `2606.13994` | Hidden in Plain Sight: Benchmarking Agent Safety Against Decomposition Attacks with DECOMPBENCH | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.14000` | Formalizing Numerical Analysis: An Agent Pipeline and Quality Audit Beyond Kernel Acceptance | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.14027` | Same-Origin Policy for Agentic Browsers | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To address this problem, we propose SOPGuard, an SOP enforcement mechanism tailored to agentic browsers |
| `2606.14106` | Naive Visual Memory is Not Enough: A Failure-Mode Study of GUI Agents | `integrate` → `retain` | Integrate proposal — `AGENT-MEMORY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To systematically analyze the effect of visual memory, we introduce a taxonomy of four GUI agent failures (i.e., cognitive failure, visual state misunderstanding, hidden operation blindness, and grounding error… |
| `2606.14130` | Contract-Based Compositional Shielding for Safe Multi-Agent Reinforcement Learning | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.14154` | SkillMutator: Benchmarking and Defending Language-and-Code Cross-modal Attacks on LLM Agent Skills | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To address this gap, we introduce SkillMutator, the first benchmark for install-time detection of language-and-code cross-modal attacks on Agent Skills |
| `2606.14179` | CacheRL:Multi-Turn Tool-Calling Agents via Cached Rollouts and Hybrid Reward | `no_change_existing_coverage` → `retain` | Integrate proposal — `TRAIN-GRPO`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We present CacheRL, a system for training small agent foundation models that achieves 92 percent process accuracy on multi-step tool-calling tasks, approaching GPT-5's 94 percent while requiring 100 times less … |
| `2606.14200` | When Should Agent Trust Be Conditional? Characterizing and Attacking Skill-Conditional Reputation in Agent Swarms | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.14239` | SkillAudit: Ground-Truth-Free Skill Evolution via Paired Trajectory Auditing | `no_change_existing_coverage` → `retain` | Integrate proposal — `AGENT-WORKFLOW`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We introduce SkillAudit, a framework for evolving agent skills without ground-truth feedback |
| `2606.14249` | HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry | `no_change_existing_coverage` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.14275` | WikiKV: Schema-Evolving Path-Indexed Storage for Hierarchical Knowledge Navigation | `integrate` → `retain` | Integrate proposal — `AGENT-MEMORY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present WikiKV, a path-indexed key-value storage model purpose-built for this workload, comprising three components: (i) a data-driven schema that bootstraps the hierarchy via Intent-Anchored Schema Inductio… |
| `2606.14350` | Design Methodology and Performance Trade-offs Management for Distributed and Compound AI Systems | `no_change_existing_coverage` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.14356` | PLAIground: SLO-Driven Runtime Model Selection for Compound AI Systems in the Edge-Cloud-Space Continuum | `no_change_existing_coverage` → `retain` | Integrate proposal — `INFER-SCHEDULING`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We present PLAIground, a framework that enables runtime model selection for Compound AI systems |
| `2606.14445` | tap: A File-Based Protocol for Heterogeneous LLM Agent Collaboration | `no_change_existing_coverage` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.14470` | GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge | `no_change_existing_coverage` → `retain` | Integrate proposal — `AGENT-MEMORY`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——Large language model reasoning leaves no trace once it is done |
| `2606.14474` | Verifiable User Simulation for Search and Recommendation Systems | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.14516` | Every Eval Ever: A Unifying Schema and Community Repository for AI Evaluation Results | `no_change_existing_coverage` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We introduce Every Eval Ever, the first shared schema and community-crowdsourced repository for AI evaluation results |
| `2606.14517` | From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To systematically expose this threat, we design a beam-search optimization framework that crafts natural-language payloads to maximize guardrail reasoning length, utilizing an LLM proposer guided by a strategy … |
| `2606.14518` | Behavioral Audit of Machine Unlearning Has a Privacy Cost | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——The removal of learned data from Machine Learning models through Machine Unlearning (MU) has been widely studied; however, there has yet to be an agreed-upon scheme for auditing MU |
| `2606.14571` | StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance | `no_change_existing_coverage` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We introduce StreamMemBench, a streaming benchmark that constructs a two-step task sequence around each evidence anchor from EgoLife egocentric streams |
| `2606.14574` | SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model | `integrate` → `retain` | Integrate proposal — `AGENT-PLANNING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To address this gap, we introduce SIMMER, a benchmark for evaluating latent failures in LLM planning through a human-curated symbolic world model grounded in the kitchen domain |
| `2606.14589` | When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime | `integrate` → `retain` | Integrate proposal — `PLATFORM-MONITORING`；`条件化机制分支与共存边界` 约 L331 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We present a longitudinal study of silent failures in one such system: a personal-assistant agent runtime in continuous production since March 2026, with roughly 40 scheduled jobs, 8 LLM providers, a tool-gover… |
| `2606.14598` | Realizing Native INT8 Compute for Diffusion Transformers on Consumer GPUs: A Fused INT8 GEMM Kernel for Ideogram 4.0 | `no_change_existing_coverage` → `de-admit` | — | 特定硬件或单一部署点的性能案例；没有改变可迁移的执行、状态或控制契约。 |
| `2606.14620` | Neither Parallel Nor Sequential: How DiffusionGemma Actually Commits Tokens | `no_change_existing_coverage` → `retain` | Integrate proposal — `MULTIMODAL-GENERATIVE-PARADIGMS`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——Across a 686-prompt, six-regime probe suite we find that its decoding is neither parallel nor block-autoregressive: it follows a partial left-to-right commit bias whose apparent strength depends almost entirely… |
| `2606.14629` | When Good Verifiers Go Bad: Self-Improving VLMs Can Regress on New Tasks | `integrate` → `retain` | Integrate proposal — `AGENT-REFLECTION` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We show that this assumption can fail because verifier quality is highly task-specific |
| `2606.14672` | Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows | `no_change_existing_coverage` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.14674` | AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition | `no_change_existing_coverage` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We introduce AgentSpec, a modular specification framework that represents embodied agents as typed compositions of reusable policy components with standardized interfaces |

## 3.4 2026-06-16 逐项审计

| arXiv | 标题 | 旧状态 → 终审 | Books 判定 | 独立判断 |
| --- | --- | --- | --- | --- |
| `2606.14779` | Unified KV Pooling to Accelerate Long-Context LLM Serving | `integrate` → `retain` | Integrate proposal — `INFER-GPU-MEMORY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To address the problems, we propose unified KV pooling, which aggregates multiple host-memory modules and SSDs into a single logical pool and distributes KV caches across devices based on their bandwidth |
| `2606.14783` | The Vision Encoder as a Privacy Boundary: Visual-Token Side Channels in Encoder-Free Vision-Language Models | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——A vision encoder compresses image pixels into semantic embeddings, implicitly acting as a privacy boundary by preserving semantic content while attenuating pixel-local detail required for exact text recovery |
| `2606.14790` | XFlow: An Executable Protocol Programming System for Reliable Multi-Agent Workflows | `integrate` → `retain` | Integrate proposal — `AGENT-WORKFLOW` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present \textbf{XFlow}, an executable protocol programming system for reliable multi-agent workflows, and \textbf{XPF} (XFlow Protocol Format), its domain-specific protocol programming language |
| `2606.14805` | Knowledge-Based Zero-Replay Debugging of Multi-Agent LLM Traces | `integrate` → `retain` | Integrate proposal — `PLATFORM-TRACE`；`条件化机制分支与共存边界` 约 L226 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We do not propose a new replay oracle; we propose a method to predict its results without paying the replay cost |
| `2606.14832` | PhoneHarness: Harnessing Phone-Use Agents through Mixed GUI, CLI, and Tool Actions | `de_admit` → `retain` | Integrate proposal — `AGENT-TOOL-CALLING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce PhoneHarness, a mixed-action benchmark and execution harness for studying phone-use agents on verifiable mobile workflows |
| `2606.14885` | Dr-DCI: Scaling Direct Corpus Interaction via Dynamic Workspace Expansion | `integrate` → `de-admit` | — | 摘要虽与 LLM/Agent 相邻，但贡献停留在局部模型、表示、任务或实现案例，未达到长期系统设计准入门槛。 |
| `2606.14945` | Remember, Don't Re-read: Stateful ReAct Agents for Token-Efficient Autonomous Experimentation | `no_change_existing_coverage` → `de-admit` | — | 摘要虽与 LLM/Agent 相邻，但贡献停留在局部模型、表示、任务或实现案例，未达到长期系统设计准入门槛。 |
| `2606.15004` | CREST: Deployment-Realistic Hardware-in-the-Loop NAS for Embedded Sensing Systems | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.15008` | Security Engineering of OpenClaw: Analyzing Attack Surface Expansion and Trust-Boundary Violations | `no_change_existing_coverage` → `de-admit` | — | 摘要虽与 LLM/Agent 相邻，但贡献停留在局部模型、表示、任务或实现案例，未达到长期系统设计准入门槛。 |
| `2606.15017` | Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents | `no_change_existing_coverage` → `de-admit` | — | 摘要虽与 LLM/Agent 相邻，但贡献停留在局部模型、表示、任务或实现案例，未达到长期系统设计准入门槛。 |
| `2606.15020` | Semantic Integrity Failures in Document-to-LLM Supply Chains | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY`；`条件化机制分支与共存边界` 约 L1375 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We show that this layer enables split-view PDFs: one document can have two semantic views before model reasoning |
| `2606.15029` | Metric Match: A Subset Selection Approach to Evaluating LLM Judge Reliability | `de_admit` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15034` | OSGuard: A Benchmark for Safety in Computer-Use Agents | `no_change_existing_coverage` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15045` | NEURON-Fabric: CXL-Side Low-Bit Gradient Aggregation for Distributed Training | `integrate` → `retain` | Integrate proposal — `TRAIN-DISTRIBUTED-TRAINING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present NEURON-Fabric, a CXL-side controller architecture that performs packed gradient-binary (G-Binary) sign-count aggregation and gradient-ternary (G-Ternary) gated aggregation near CXL memory, with a con… |
| `2606.15050` | Solyx AI Grid: Hardware-Telemetry-Aware Routing Across Geographically Distributed GPU Clusters | `integrate` → `retain` | Integrate proposal — `PLATFORM-GATEWAY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present Solyx AI Grid, a cross-site inference routing control plane that integrates GPU hardware telemetry (DCGM), vLLM application metrics, and real-time WAN signals (RTT, jitter) into per-request placement… |
| `2606.15057` | AutoDojo: Adaptive Black-Box Attacks Reveal the Limits of IPI Defenses and Task-Specification Effects in LLM Agents | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15070` | Stop When Further Reasoning Won't Help: Attention-State Adaptive Generation in Reasoning Models | `integrate` → `retain` | Integrate proposal — `INFER-DECODE`；`条件化机制分支与共存边界` 约 L231 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——By incorporating test-time compute scaling, large reasoning models (LRMs) can solve complex problems through explicit chain-of-thought (CoT) reasoning processes |
| `2606.15079` | Ling and Ring 2.6 Technical Report: Efficient and Instant Agentic Intelligence at Trillion-Parameter Scale | `no_change_existing_coverage` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15099` | Think Less, Act Early: Reinforced Latent Reasoning with Early Exit in Vision-Language-Action Models | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15122` | The Hitchhiker's Guide to Program Analysis, Part III: Mostly Harmless LLMs | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15127` | Beyond Accuracy: Measuring Bias Acknowledgment in Chain-of-Thought Reasoning for Responsible AI Evaluation | `no_change_existing_coverage` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15153` | False Sense of Safety in Selective Signal Classification: Auditing Bound Tightness and Exchangeability for Risk Control | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.15157` | PolyKV: Heterogeneous Retention and Allocation for KV Cache Compression | `integrate` → `retain` | Integrate proposal — `INFER-KV-CACHE` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present PolyKV, a layer-wise KV cache optimization framework that considers design space with method selection and budget allocation |
| `2606.15177` | Coordinated Scheduling for MoE LLM Serving | `integrate` → `retain` | Integrate proposal — `INFER-SCHEDULING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To address this gap, we propose Gimbal, a coordinated cross-level scheduling system for efficient MoE-based LLM serving |
| `2606.15179` | CONCORD: Asynchronous Sparse Aggregation for Device-Cloud RAG under Document Isolation | `integrate` → `retain` | Integrate proposal — `AGENT-RAG` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To address this issue, we propose CONCORD, an asynchronous sparse aggregation framework for dual-end RAG under document isolation |
| `2606.15210` | Generation Quality-Latency Tradeoff-Aware Inference Offloading for Multimodal LLMs in Cloud-Edge Continuum | `de_admit` → `de-admit` | — | 摘要虽与 LLM/Agent 相邻，但贡献停留在局部模型、表示、任务或实现案例，未达到长期系统设计准入门槛。 |
| `2606.15216` | Spokes: Optimizing for Diverse Pretraining Data Selection | `de_admit` → `de-admit` | — | 摘要虽与 LLM/Agent 相邻，但贡献停留在局部模型、表示、任务或实现案例，未达到长期系统设计准入门槛。 |
| `2606.15242` | Benign in Isolation, Harmful in Composition: Security Risks in Agent Skill Ecosystems | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce SCR-Bench to evaluate this risk in controlled, sandboxed skill environments |
| `2606.15258` | Mask-Proof: An LLM-based Automated Data Curation Pipeline on Mathematical Proofs | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.15285` | Acting While Understanding: Asynchronous Semantic-Action Decoupling for Real-Time Vision-Language-Action Models | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-EMBODIED-VLA` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We propose an asynchronous semantic-action decoupling framework that separates semantic understanding from action generation along the internal semantic-action interface of existing VLAs, without redesigning th… |
| `2606.15306` | LatentGym: A Testbed For Cross-Task Experiential Learning With Controllable Latent Structure | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15308` | Forced Deferral: Manipulating Routing Decisions in Multimodal LLM Cascades | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Motivated by this vulnerability, we introduce the Forced Deferral Attack (FDA), an adversarial image attack that lowers the weak model's confidence and causes cascades to route queries to the strong model |
| `2606.15319` | Adaptive Resource Management and Quality Control for Streaming Video Generation | `integrate` → `retain` | Integrate proposal — `INFER-SCHEDULING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Guided by these insights, we present SlackServe, a playout-slack-driven serving system that preserves playout continuity in real-time streaming video generation |
| `2606.15333` | Replay What Matters: Off-Policy Replay for Efficient LLM Reinforcement Unlearning | `de_admit` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.15335` | Privacy-Preserving Text Sanitization for Distributed Agents Collaboration via Disentangled Representations | `no_change_existing_coverage` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.15341` | CausalDrive: Real-time Causal World Models for Autonomous Driving | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-WORLD-MODELS` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To bridge this gap, we present CausalDrive, a controllable, real-time foundation driving world renderer |
| `2606.15345` | Beyond Monolingual Deep Research: Evaluating Agents and Retrievers with Cross-Lingual BrowseComp-Plus | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15363` | APEX: Adaptive Principle EXtraction A Three-Layer Self-Evolution Framework for Production AI Agents | `no_change_existing_coverage` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.15367` | S1-DeepResearch: Beyond Search, Toward Real-World Long-Horizon Research Agents | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.15376` | CoAgent: Concurrency Control for Multi-Agent Systems | `integrate` → `retain` | Integrate proposal — `AGENT-MULTI-AGENT`；`条件化机制分支与共存边界` 约 L594 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——Multi-agent LLM systems -- coding agents, devops agents, document agents -- now routinely run several agents in parallel against the same git tree, Kubernetes cluster, or document |
| `2606.15378` | Rethinking the Role of Efficient Attention in Hybrid Architectures | `integrate` → `retain` | Integrate proposal — `MODEL-LONG-CONTEXT` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——First, from a scaling perspective, we find that efficient-attention design primarily affects how fast long-context capability emerges, while different hybrids eventually converge to comparable long-context perf… |
| `2606.15385` | Reward Hacking in Language Model Agents: Revisiting AI Safety Gridworlds | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15390` | Not All Skills Help: Measuring and Repairing Agent Knowledge | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.15405` | T-Mem: Memory That Anticipates, Not Archives | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.15441` | Defending against Adaptive Prompt Injection Attacks via Reasoning-enabled Task Alignment | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To address these gaps, we propose RETA, a training-based method that grounds defense decisions on the user tasks rather than attacker-controlled data |
| `2606.15453` | A Spatio-Temporal Expert Prefetching Framework for Efficient MoE-based LLM Inference | `integrate` → `retain` | Integrate proposal — `INFER-GPU-MEMORY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Based on this insight, we propose ST-MoE, a spatio-temporal expert prefetching framework that proactively stages experts ahead of use to overlap expert loading with ongoing computation |
| `2606.15455` | Understanding Diversity Collapse in RLVR via the Lens of Overtraining | `integrate` → `retain` | Integrate proposal — `TRAIN-GRPO` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Building on these findings, we propose \emph{Bayesian Boundary Gating} (BBG), which redirects optimization away from overtraining by estimating each problem's marginal contribution to the reasoning boundary |
| `2606.15474` | Who Drifted: the System or the Judge? Anytime-Valid Attribution in LLM Evaluation Pipelines | `integrate` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Continuous evaluation of LLM products relies on a strong LLM judge treated as ground truth: a cheap monitor scores every interaction and a team is paged when the score drifts down |
| `2606.15476` | FARM: Find Anything using Relational Spatial Memory | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.15493` | Model Stealing Through the Lens of Model Multiplicity | `de_admit` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.15508` | ToolMenuBench: Benchmarking Tool-Menu Filtering Strategies for Reliable and Efficient LLM Agents | `de_admit` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.15549` | One Goal, Many Commands: Characterizing Denylist Fragility in AI Agents | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——The adoption of AI agents is increasing rapidly |
| `2606.15555` | Service-Induced Congestion in Memory-Constrained LLM Serving | `integrate` → `retain` | Integrate proposal — `INFER-SCHEDULING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We develop a discrete-time dynamical model of memory-constrained LLM inference that captures admission, memory growth, and eviction under continuous batching |
| `2606.15594` | Pixels to Proofs: Probabilistically-Safe Latent World Model Control via Parallel Conformal Robust MPC | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-WORLD-MODELS` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present SLS^2, a framework for safe feedback motion planning from pixels using robust model predictive control (MPC) in learned latent world models |
| `2606.15608` | On the Adversarial Robustness of Multimodal LLM Judges | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15609` | FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We propose FragFuse, the first attack that enables unprivileged users to bypass agent access control by exploiting this temporal channel introduced by long-term memory |
| `2606.15610` | LLM Judges Have Dark Current: A Psychometric Datasheet for LLM-as-a-Judge Evaluation | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15621` | Re-feeding Is Not Replaying: Measuring Replay Noise in Counterfactual Token-Credit Estimation | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.15625` | Conflict-Aware Federated Fine-Tuning of Large Language Models with Mixture-of-Experts | `de_admit` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.15631` | Retrieve, Don't Retrain: Extending Vision Language Action Models to New Tasks at Test Time | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.15652` | MosaicQuant: Inlier-Outlier Disaggregation for Unified 4-Bit LLM Quantization | `integrate` → `retain` | Integrate proposal — `INFER-TENSORRT-LLM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We propose \textbf{MosaicQuant}, a unified 4-bit LLM quantization paradigm built on a novel principle of \emph{inlier--outlier disaggregation} |
| `2606.15682` | ReQAT: Achieving Full-Precision Reasoning Accuracy with 4-bit Floating-Point Quantization-Aware Training | `de_admit` → `retain` | Integrate proposal — `INFER-TENSORRT-LLM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We identify that FP4 failures concentrate on low-entropy tokens--precise symbolic commitments such as digits and operators--where quantization noise inflates sampling errors that cascade through reasoning trace… |
| `2606.15712` | Odds Law: The Decomposition Algebra On How Intelligence Organizes Itself to Solve Difficult Problems Reliably | `no_change_existing_coverage` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15734` | Retrievable Gradients: Continual Post-Training Without Cumulative Weight Drift | `integrate` → `retain` | Integrated — `books/part-04-training-system/30-lora.md` / `从持续改写共享权重到可检索的临时参数更新`（Review notes 前完整机制链） | 保留：摘要给出可定位机制——In this paper, we propose ReGrad (Retrievable Gradients), a new paradigm that treats gradients as retrievable units of knowledge |
| `2606.15762` | Snyk VulnBench JS 1.0: Can LLMs Find the Same Bugs Twice? | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15789` | Approaching Shannon Bound with Lossless LLM Weight Compression | `integrate` → `retain` | Integrate proposal — `INFER-GPU-MEMORY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Through a comprehensive entropy study across models from 1.5B to 405B parameters and numeric formats ranging from bf16 to int4 and AWQ/SQ8, we find that LLM weights contain far less intrinsic randomness than th… |
| `2606.15805` | Mean-Field Parallel Decoding for Discrete Diffusion Language Models | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-GENERATIVE-PARADIGMS` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce a training-free decoding framework that coordinates these parallel updates |
| `2606.15811` | FuseChain: Runtime Evidence Reconstruction for Software Supply-Chain Attacks | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.15822` | TrustedARI: Towards Trust-Native Agentic Routing Infrastructure for Agentic AI | `integrate` → `retain` | Integrate proposal — `PLATFORM-GATEWAY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To address this problem, we present TrustedARI, the first trust-native agentic routing infrastructure for agentic AI |
| `2606.15828` | Configuration Smells in AGENTS.md Files: Common Mistakes in Configuring Coding Agents | `de_admit` → `de-admit` | — | 摘要虽与 LLM/Agent 相邻，但贡献停留在局部模型、表示、任务或实现案例，未达到长期系统设计准入门槛。 |
| `2606.15834` | AIChilles: Automatically Uncovering Hidden Weaknesses in AI-Evolved Systems | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15841` | Heteroskedastic Signals in Budgeted LLM Verification: Structural Heterogeneity Limits Optimization Gains | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15859` | EPIC: A System Framework for Efficient Egocentric Perception on Embodied AR Glasses | `integrate` → `de-admit` | — | 特定硬件或单一部署点的性能案例；没有改变可迁移的执行、状态或控制契约。 |
| `2606.15874` | LLM-as-Code: Agentic Programming for Agent Harness | `integrate` → `de-admit` | — | 摘要虽与 LLM/Agent 相邻，但贡献停留在局部模型、表示、任务或实现案例，未达到长期系统设计准入门槛。 |
| `2606.15899` | SkillVetBench: LLM-as-Judge for Multi-Dimensional Security Risk Evaluation in Open-Source LLM Agent Skills | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.15903` | Control-Plane Placement Shapes Forgetting: An Architectural Study of Agent Memory Across Thirteen System Configurations | `integrate` → `retain` | Integrate proposal — `AGENT-MEMORY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Where an LLM sits in an agent memory pipeline -- between the recall plane that retrieves stored facts (extensively benchmarked) and the control plane that mutates them via supersede, release, purge (largely unt… |
| `2606.15963` | PreLort: Prefix-Nested LoRA for Federated Fine-Tuning under Rank Heterogeneity | `de_admit` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.15964` | PromptShift-CRC: Drift-Aware Conformal Risk Control for Foundation Models Under Prompt and Domain Shift | `integrate` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Foundation models are now used in settings where the prompts they receive can change quickly |
| `2606.15980` | Do Activation Monitors Survive Model Updates? Benchmarking, Predicting, and Repairing Activation-Monitor Staleness | `integrate` → `retain` | Integrate proposal — `PLATFORM-MONITORING`；`条件化机制分支与共存边界` 约 L331 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We present the first systematic test of whether this implicit contract holds: whether activation monitors trained on a base model remain reliable after these routine model updates |
| `2606.15991` | Fearless Concurrency on the GPU | `integrate` → `retain` | Integrate proposal — `INFER-TENSORRT-LLM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present cuTile Rust, a tile-based system for safe, idiomatic GPU kernel authoring in Rust |
| `2606.15994` | Agentic Framework for Deep Learning workload migration via In-Context Learning | `de_admit` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.16000` | GRACE-DS: a Guarded Reward-guided Agent Correction Environment in Data Science | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.16062` | Auditing Reward Hackability in Code RL Training Environments | `integrate` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We measure the rate at which code RL environments accept incorrect solutions as correct |
| `2606.16070` | Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games | `integrate` → `de-admit` | — | 摘要虽与 LLM/Agent 相邻，但贡献停留在局部模型、表示、任务或实现案例，未达到长期系统设计准入门槛。 |
| `2606.16100` | Your "Pro" LLM Subscription May Actually Be "Free": Exposing Fingerprint Spoofing Risks in LLM Inference Services | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce a novel threat termed fingerprint spoofing, where a malicious provider stealthily serves a weaker model that has been parameter-efficiently fine-tuned to mimic a stronger model, thereby evading use… |
| `2606.16106` | Edge-Inference Governors Need Memory-Clock State | `integrate` → `retain` | Integrate proposal — `INFER-SCHEDULING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We show this with a deployed, measured governor on Jetson Orin: an EMC-blind GPU-only fit misses 25-28% of cycles at tight deadlines, whereas an EMC-aware two-cell refit holds misses to &lt;=0.9% under a 2% QoS… |
| `2606.16110` | Auditing Machine Unlearning: A Systematic Research on Whether Models Truly Forget | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.16135` | SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing | `integrate` → `retain` | Integrate proposal — `INFER-KV-CACHE` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To address these two challenges, we propose SwiftCache, a collaborative inference system that enables heterogeneous models to share underutilized GPU memory and NVLink bandwidth within a server |
| `2606.16190` | Embedded Arena: Iterative Optimization via Hardware Feedback | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.16242` | Rapid Poison: Practical Poisoning Attacks Against the Rapid Response Framework | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.16264` | Tropical: Enhancing SLO Attainment in Disaggregated LLM Serving via SLO-Aware Multiplexing | `integrate` → `retain` | Integrate proposal — `INFER-PD-DISAGGREGATION` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To guarantee service quality in transformer based large language model (LLM) serving, it is essential to meet the latency constraints of both the prefill phase (measured by Time-to-First-Token, TTFT) and the de… |
| `2606.16287` | Dynamic Malicious Skills in Agentic AI | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To mitigate this vulnerability, we propose a system-level defense that prevents dynamic modification of skills using operating system kernel-enforced read-only mounts |
| `2606.16310` | QK-Normed MLA: QK normalization without full key caching | `integrate` → `retain` | Integrate proposal — `MODEL-LONG-CONTEXT`；`Draft Attention 可以提供稀疏候选，但 Target 仍拥有语义` 约 L644 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We show this apparent incompatibility is an implementation artifact, not an architectural constraint |
| `2606.16322` | PaperJury: Due-Process Review for Bounded LaTeX Revision | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.16332` | SMEPilot: Characterizing and Optimizing LLM Inference with Scalable Matrix Extensions | `integrate` → `de-admit` | — | 摘要虽与 LLM/Agent 相邻，但贡献停留在局部模型、表示、任务或实现案例，未达到长期系统设计准入门槛。 |
| `2606.16341` | Filtered ANN as a Phase Transition: When Selectivity-Estimation Error Causes Plan Regret | `de_admit` → `retain` | Integrate proposal — `AGENT-RAG` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——A filtered approximate-nearest-neighbor (ANN) query returns the k nearest vectors among those satisfying an attribute predicate P of selectivity s |
| `2606.16352` | Communication-Efficient Verifiable Attention for LLM Inference | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Computation integrity of remote large language model (LLM) serving can be questionable |
| `2606.16358` | The Proxy Knows Too Much: Sealing LLM API Routers with Attested TEEs | `integrate` → `retain` | Integrate proposal — `PLATFORM-GATEWAY`；`条件化机制分支与共存边界` 约 L168 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We propose AEGIS, a provider-transparent attested API router whose data path is a client-verified faithful passthrough |
| `2606.16364` | Looking Is Not Picking: An Attention-Segment Account of Tool-Selection Failures in LLM Agents | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.16384` | Mixtures of Subspaces for Bandwidth Efficient Context Parallel Training | `integrate` → `retain` | Integrate proposal — `TRAIN-DISTRIBUTED-TRAINING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We propose a compression method for communication-efficient context parallelism in decentralized settings, achieving a remarkable compression rate of over 95\% with negligible overhead and no loss in convergenc… |
| `2606.16420` | Transferable Self-Evolving Playbooks for Agentic Security Auditing | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.16429` | Taylor-Calibrate: Principled Initialization for Hybrid Linear Attention Distillation | `de_admit` → `de-admit` | — | 摘要虽与 LLM/Agent 相邻，但贡献停留在局部模型、表示、任务或实现案例，未达到长期系统设计准入门槛。 |
| `2606.16461` | Privacy from Symmetry: Orthogonally Equivariant Transformers for LLM Inference | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.16494` | Lost at the End: Primacy Bias in Multimodal Retrieval-Augmented Question Answering | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.16496` | REFLEX: Reflective Evolution from LLM Experience | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.16511` | Tail-Shape Estimation in LLM Evaluation Is Fragile: A Protocol for Diagnosing False Positives | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.16519` | BadWorld: Adversarial Attacks on World Models | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce BadWorld, a label-free adversarial framework tailored for autoregressive VWMs that systematically overcomes both constraints |
| `2606.16523` | SkillWiki: A Living Knowledge Infrastructure for Agent Skills | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.16527` | DoubtProbe: Black-Box Jailbreak Defense via Structural Verification and Semantic Auditing | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.16541` | The Faithfulness Gap: Certifying Semantic Equivalence Between Natural-Language and Formal Mathematical Statements | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.16603` | VeriGraph: Towards Verifiable Data-Analytic Agents | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.16605` | ARB4WM: An Adversarial Robustness Benchmark for World Models in Continuous Control | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.16682` | Multimodal Evaluator Preference Collapse: Cross-Modal Coupling in Self-Evolving Agents | `integrate` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We show that Evaluator Preference Collapse (EPC) is dramatically amplified in multimodal settings |
| `2606.16690` | PATCH: Action-Chunk-Conditioned Latent Patch Innovation Monitoring for Robot Manipulation | `de_admit` → `retain` | Integrate proposal — `MULTIMODAL-EMBODIED-VLA` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce PATCH, an action-chunk-conditioned latent patch innovation monitor for deployment-time intervention |
| `2606.16707` | User as Code: Executable Memory for Personalized Agents | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.16710` | Misinformation Propagation in Benign Multi-Agent Systems | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.16748` | MyPCBench: A Benchmark for Personally Intelligent Computer-Use Agents | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.16751` | Automated jailbreak attack targeting multiple defense strategies | `de_admit` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.16768` | Taming Curvature: Architecture Warm-Up for Stable Transformer Training | `integrate` → `de-admit` | — | 摘要虽与 LLM/Agent 相邻，但贡献停留在局部模型、表示、任务或实现案例，未达到长期系统设计准入门槛。 |
| `2606.16774` | OpenClaw-Skill: Collective Skill Tree Search for Agentic Large Language Models | `de_admit` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.16813` | GIST-CMTF: Goal-State Inference for Causal Minimal Tool Filtering in LLM Agents | `integrate` → `retain` | Integrate proposal — `AGENT-TOOL-CALLING`；`Tool Admission 与 Interaction Latency 必须分开控制` 约 L396 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We introduce GIST-CMTF, a goal-state inference layer that predicts candidate symbolic goals over the same state-transition vocabulary used by CMTF, estimates ambiguity, and either applies CMTF or exposes clarif… |
| `2606.16821` | How Much Can We Trust LLM Search Agents? Measuring Endorsement Vulnerability to Web Content Manipulation | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce SearchGEO, a controlled evaluation framework for measuring endorsement corruption in LLM-based web-search agents, combining a web-evidence manipulation pipeline, a five-mode attack taxonomy, and mu… |
| `2606.16824` | CacheWise: Understanding Workloads and Optimizing KVCache Management for Efficiently Serving LLM Coding Agents | `integrate` → `retain` | Integrate proposal — `INFER-KV-CACHE` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Based on our analysis, we present CacheWise, a KVCache management layer that improves KVCache reuse for coding agent workloads |
| `2606.16907` | Tangram: Hiding GPU Heterogeneity for Efficient LLM Parallelization | `integrate` → `retain` | Integrate proposal — `TRAIN-DISTRIBUTED-TRAINING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——The scale of LLM training jobs requires parallelization planning over large GPU clusters |
| `2606.16914` | Greed Is Learned: Visible Incentives as Reward-Hacking Triggers | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We show that reinforcement learning can make a policy \emph{addicted} to such a visible self-benefit channel |
| `2606.16988` | Agent trajectories as programs: fingerprinting and programming coding-agent behavior | `integrate` → `retain` | Integrate proposal — `AGENT-WORKFLOW`；`条件化机制分支与共存边界` 约 L815 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——In this work, we introduce methods for comparing agents procedurally in different contexts, where the model, tasks, and approaches vary |
| `2606.17005` | Bayesian Inference and Decision Audits for Public Archives of Frontier AI Evaluations | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.17016` | TokenPilot: Cache-Efficient Context Management for LLM Agents | `no_change_existing_coverage` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.17029` | DEEPRUBRIC: Evidence-Tree Rubric Supervision for Efficient Reinforcement Learning of Deep Research Agents | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.17034` | KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing | `integrate` → `retain` | Integrate proposal — `INFER-KV-CACHE`；`条件化机制分支与共存边界` 约 L1098 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We introduce KVEraser, a learned KV-cache editing method for efficient localized context erasing |

## 3.5 2026-06-17 逐项审计

| arXiv | 标题 | 旧状态 → 终审 | Books 判定 | 独立判断 |
| --- | --- | --- | --- | --- |
| `2606.17081` | The Price of Anarchy in Disaggregated Inference | `integrate` → `retain` | Integrate proposal — `INFER-PD-DISAGGREGATION` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Based on this analysis, we design an adaptive controller that detects saturation transitions in real time and adjusts routing parameters accordingly, shifting from cache-affinity exploitation to load-balanced c… |
| `2606.17090` | ANEForge: Python for direct computation on the Apple Neural Engine | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.17099` | Software Delegation Contracts: Measuring Reviewability in AI Coding-Agent Work | `integrate` → `retain` | Integrate proposal — `AGENT-WORKFLOW` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——AI coding agents increasingly accept assigned software tasks, modify repositories under bounded authority, and return work packages for review |
| `2606.17104` | Prefill/Decode-Aware Evaluation of LLM Inference on Emerging AI Accelerators | `integrate` → `retain` | Integrate proposal — `INFER-PD-DISAGGREGATION` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——As large language models (LLMs) are increasingly deployed in latency- and cost-sensitive settings, inference efficiency has become a central systems challenge |
| `2606.17107` | Models Take Notes at Prefill: KV Cache Can Be Editable and Composable | `integrate` → `retain` | Integrate proposal — `INFER-KV-CACHE` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Prefix caching reuses prefill only across an exactly shared prefix, so one changed field invalidates the entire downstream cache |
| `2606.17110` | Loss Landscape Poisoning: Targeted Extraction of Unseen Training Data from LLMs | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We show that the attack is thwarted when the model is trained to be differentially private |
| `2606.17114` | An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.17122` | TrustErase: Auditable Instant Machine Unlearning with Passport-Embedded Representations | `integrate` → `retain` | Integrate proposal — `TRAIN-DATA` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce TrustErase, a verifiable, data-free unlearning framework leveraging passport-embedded representations for instant, modular, and auditable forgetting |
| `2606.17182` | Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems | `integrate` → `retain` | Integrate proposal — `AGENT-MULTI-AGENT` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Multi-agent LLM systems share state through memory stores, vector indices, and tool registries |
| `2606.17200` | ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.17209` | Beyond Parallel Sampling: Diverse Query Initialization for Agentic Search | `de_admit` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.17229` | Rift: A Conflict Signature for Deception in Language Models | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.17241` | Beyond Benchmarks: Continuous Edge Inference for Fine-Grained Roadside Perception | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.17283` | ARVO: Atlas of Reproducible Vulnerabilities for Open-Source Software | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.17328` | MemTrace: Probing What Final Accuracy Misses in Long-Term Memory | `no_change_existing_coverage` → `retain` | Integrate proposal — `AGENT-MEMORY`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We introduce MemTrace, a benchmark whose unit of measurement is the knowledge point: a single typed fact about the user, rather than an individual question |
| `2606.17378` | RISE: Relay Inference and Online Scheduling for Efficient Edge-Device Collaborative Diffusion Model Services | `integrate` → `retain` | Integrate proposal — `INFER-SCHEDULING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To bridge this gap, we propose RISE, a method for edge-device diffusion model services that combines relay inference with online scheduling |
| `2606.17383` | Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation | `integrate` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Agentic artificial intelligence systems introduce a new class of model risk |
| `2606.17421` | Bifrost: Hybrid TEE-FHE Inference for Privacy-Preserving Transformer and LLM Serving | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present Bifrost, a hybrid TEE-FHE serving architecture in which secrets are provisioned only to an attested CPU TEE, while the accelerator, device memory, driver/runtime stack, and host software remain outsi… |
| `2606.17454` | Dissecting model behavior through agent trajectories | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.17467` | PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents | `integrate` → `retain` | Integrate proposal — `AGENT-RAG` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce PARSE (Provenance-Aware Retrieval Sanitization), a domain-aware, fact-preserving sanitization pipeline that classifies each sentence by injection likelihood, extracts structured facts before rewrit… |
| `2606.17518` | SpecGen: Accelerating Agentic Kernel Optimization with Speculative Generation | `integrate` → `retain` | Integrate proposal — `INFER-TENSORRT-LLM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present SpecGen, an agentic kernel optimization system with \emph{speculative generation} |
| `2606.17519` | Scaling Enterprise Agent Routing: Degradation, Diagnosis, and Recovery | `integrate` → `retain` | Integrate proposal — `AGENT-TOOL-CALLING`；`Tool Admission 与 Interaction Latency 必须分开控制` 约 L396 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——Production LLM assistants route user requests to growing libraries of specialized tools, but how does routing accuracy degrade as the catalog scales |
| `2606.17533` | SNAS: A Multi-Layer Defense-in-Depth Architecture for Secure Egress in Sandboxed Workloads | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.17546` | SEAGym: An Evaluation Environment for Self-Evolving LLM Agents | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.17566` | AoiZora: Topology-Aware Auto-Parallel Optimization for Inference of Diffusion Transformers | `integrate` → `retain` | Integrate proposal — `INFER-TENSORRT-LLM`；`条件化机制分支与共存边界` 约 L1305 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——Video diffusion has quickly grown into a key generative serving workload, yet producing each clip demands many denoising iterations over large spatio-temporal latents, which puts low-latency inference out of re… |
| `2606.17573` | Cordon: Semantic Transactions for Tool-Using LLM Agents | `integrate` → `retain` | Integrate proposal — `AGENT-WORKFLOW` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Tool-using LLM agents are shifting the unit of computation from explicit human-issued commands to model-driven tasks with stateful consequences |
| `2606.17591` | Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning | `integrate` → `retain` | Integrate proposal — `AGENT-MEMORY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We identify four requirements for navigating this dilemma -- outcome-driven evaluation, persistent structured evidence, non-monotonic knowledge lifecycle, and compositional governance -- and show that existing … |
| `2606.17609` | The Benchmark Illusion: Pruned LLMs Can Pass Multiple Choice but Fail to Answer | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.17730` | ActWorld: From Explorable to Interactive World Model via Action-Aware Memory | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-WORLD-MODELS` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——In this work, we present ActWorld, an interactive world model that extends prior navigation-centric generators to support mid-rollout object interaction within a chunk-autoregressive framework |
| `2606.17787` | LUMEN: Coordinated Failure Recovery for Distributed LLM Serving | `integrate` → `retain` | Integrate proposal — `INFER-SCHEDULING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present LUMEN, a fault-tolerant LLM serving system that treats recovery as a load-aware coordination problem across three decision points: checkpoint placement before failures, interrupted-request distributi… |
| `2606.17819` | A Framework for Evaluating Agentic Skills at Scale | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.17872` | AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor | `integrate` → `retain` | Integrate proposal — `INFER-KV-CACHE` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We propose AnchorKV, a drop-in modification to KV cache compression that biases token retention scores away from directions in key space associated with harmful prompts |
| `2606.17929` | PreAct: Computer-Using Agents that Get Faster on Repeated Tasks | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.17930` | How Inference Compute Shapes Frontier LLM Evaluation | `integrate` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We find three main results |
| `2606.17949` | RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving | `integrate` → `retain` | Integrate proposal — `PLATFORM-GATEWAY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present RouteBalance, a serving-aware scheduling layer that fuses both into a single online assignment over concrete model instances, jointly trading off quality, latency, and cost |
| `2606.18037` | ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents | `integrate` → `retain` | Integrate proposal — `AGENT-RAG` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce ProvenanceGuard, a source-aware verifier for MCP-grounded answers |
| `2606.18051` | Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.18121` | On the Reliability of Networks of AI Agents: Density Evolution, Stopping Sets, and Architecture Optimization | `integrate` → `retain` | Integrate proposal — `AGENT-MULTI-AGENT` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Modern AI systems increasingly solve a task not with a single model call but with several imperfect agents working together: some propose pieces of a solution, others verify them, and the results are combined |
| `2606.18144` | Memory as a Wasting Asset: Pricing Flash Endurance for Embodied Agents, and the Limits of Doing So | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.18168` | All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code | `integrate` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Software practitioners increasingly use AI coding agents that generate test code alongside production code in open source pull requests (PRs) |
| `2606.18198` | Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Through an empirical study of existing skill scanners, we find that current defenses primarily rely on textual descriptions, manifests, and source code as the main signals for security analysis, which can leave… |
| `2606.18208` | Looped World Models | `no_change_existing_coverage` → `retain` | Integrate proposal — `MULTIMODAL-WORLD-MODELS`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——Current world models face a fundamental tension: faithful long-horizon simulation demands deep computation, but deeper models are expensive to deploy and prone to compounding errors |
| `2606.18247` | Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-EMBODIED-VLA` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——In this paper, we propose VERITAS, a generator-verifier framework for generalist robot policies for inference-time policy steering and self-improvement |

## 3.6 2026-06-18 逐项审计

| arXiv | 标题 | 旧状态 → 终审 | Books 判定 | 独立判断 |
| --- | --- | --- | --- | --- |
| `2606.18284` | Breaking the Solver Bottleneck: Training Task Generators at the Learnable Frontier | `integrate` → `retain` | Integrate proposal — `TRAIN-DATA` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce PROPEL, a solver-amortized framework for training task generators at the targeted solve rate |
| `2606.18286` | CODEBLOCK: Learning to Supervise Code at the Right Granularity | `de_admit` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.18310` | Conflict-Aware Retriever Editing for Knowledge Injection Attacks on LLM-Based RAG Systems | `integrate` → `retain` | Integrate proposal — `AGENT-RAG` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——In this paper, we propose conflict-aware retriever editing, i.e., CAREATTACK, a model-centric retriever attack framework for malicious knowledge injection in RAG |
| `2606.18322` | SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.18356` | SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents | `integrate` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce SafeClawBench, a staged benchmark for tool-using agent security with 600 controlled adversarial tasks across six attack families: direct and indirect prompt injection, tool-return injection, memory… |
| `2606.18379` | RankGraph-2: Lifecycle Co-Design for Billion-Node Graph Learning in Recommendation | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.18383` | From Sparse Features to Trustworthy Proxies: Certifying SAE-Based Interpretability | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.18394` | JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting | `no_change_existing_coverage` → `retain` | Integrate proposal — `INFER-SPECULATIVE-DECODING`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We propose JetSpec, a head-based SD framework that combines one-forward drafting efficiency with branch-wise causal conditioning |
| `2606.18400` | CloakLM: Obfuscating GPU Memory Layout to Mitigate Model Ex-filtration for Serving | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present CloakLM, a software-only memory-obfuscation framework that removes this structural regularity without changing the inference stack's logical view of memory |
| `2606.18421` | Finding Compiler-Platform Interaction Bugs in Deep Learning Pipelines via Cross-Layer Constraints | `integrate` → `retain` | Integrate proposal — `INFER-TENSORRT-LLM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——In this work, we propose a scalable, automated DL compiler testing framework for, in tandem, (1) finding compiler-platform interaction bugs and (2) enabling behavior equivalence partitioning |
| `2606.18431` | Beyond Prediction: Tail-Aware Scheduling for LLM Inference | `integrate` → `retain` | Integrate proposal — `INFER-SCHEDULING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We show that these prediction-driven policies can be fragile under distribution shifts, bursty arrivals, and GPU memory pressure, while offering limited control over the tail latency (P90-P99) that dominates us… |
| `2606.18448` | VISUALSKILL: Multimodal Skills for Computer-Use Agents | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.18467` | ToolChain-CRC: Conformal Risk Control for Agentic AI Under Retrieval and Tool-Use Drift | `integrate` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We propose ToolChain-CRC, a conformal risk-control method for retrieval-augmented and tool-using agents under drift |
| `2606.18497` | Ghost Vectors: Soft-Deleted Embeddings Remain Reconstructible in HNSW Vector Databases | `integrate` → `retain` | Integrate proposal — `AGENT-RAG` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Using the Vec2Text inversion model without domain-specific fine-tuning, we show this vulnerability on multiple real-world datasets and data modalities |
| `2606.18532` | AI Sandboxes: A Threat Model, Taxonomy, and Measurement Framework | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——AI systems are increasingly evaluated in bounded environments that combine isolation, simulation, instrumentation, supervision, and evidence capture |
| `2606.18550` | The Gate Is Only as Honest as Its Contracts: ContractGuard for the Contract Layer of Risk-Aware Causal Gating | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Third, we introduce ContractGuard, a verifier between the registry and the gate that layers signed provenance, typed contract attestation, and runtime effect verification; on a controlled benchmark it restores … |
| `2606.18600` | ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters | `integrate` → `retain` | Integrate proposal — `INFER-SCHEDULING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——As large language model (LLM) services become widely adopted, the cost of GPU resources for serving these models in cloud environments has emerged as a critical concern |
| `2606.18619` | Code-Augur: Agentic Vulnerability Detection via Specification Inference | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.18650` | BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training | `no_change_existing_coverage` → `retain` | Integrate proposal — `TRAIN-DATA`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We propose BLADE (Bi-Level Adaptive Data sElection), a Hessian-free framework for data selection |
| `2606.18668` | EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems | `no_change_existing_coverage` → `retain` | Integrate proposal — `AGENT-MULTI-AGENT`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——To address this challenge, we present EARS (Explanatory Abstention for Reliable Sub-Agent Modeling), a production-oriented framework that reframes sub-agent abstention as an inter-agent communication protocol: … |
| `2606.18673` | Understanding and Mitigating Prompt Leaking Attacks in Real-World LLM-Based Applications | `no_change_existing_coverage` → `retain` | Integrate proposal — `PLATFORM-SECURITY`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——Guided by this insight, we propose AREA, a practical defense that re-anchors the model's attention using an optimizable soft prompt |
| `2606.18697` | Stealthy World Model Manipulation via Data Poisoning | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-WORLD-MODELS` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——In this paper, we propose SWAAP, the first two-stage data poisoning framework for learned world models |
| `2606.18741` | ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving | `integrate` → `retain` | Integrate proposal — `INFER-SCHEDULING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Current large language model (LLM) inference systems universally deploy ultra-large-scale models using a combination of Tensor Parallelism (TP) and Pipeline Parallelism (PP) |
| `2606.18746` | What Must Generalist Agents Remember? | `no_change_existing_coverage` → `retain` | Integrate proposal — `AGENT-MEMORY`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——This paper develops a formal account of what generalist agents must store in memory in order to act near-optimally across multiple environments and goals |
| `2606.18810` | Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards | `no_change_existing_coverage` → `retain` | Integrate proposal — `TRAIN-GRPO`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We propose SC-GRPO (Self-Conditioned GRPO), which uses KL divergence mentioned before as a multiplicative weight on GRPO gradients |
| `2606.18829` | GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents | `no_change_existing_coverage` → `retain` | Integrate proposal — `PLATFORM-SECURITY`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We introduce GateMem, a benchmark for multi-principal shared-memory agents |
| `2606.18831` | Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning | `de_admit` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.18847` | WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-EMBODIED-VLA` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce WorldLines, a project-driven benchmark for long-horizon embodied household assistance |
| `2606.18874` | Externalizing Research Synthesis and Validation in AI Scientists through a Research Harness | `de_admit` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.18958` | LiveStack: OS Support for Cluster-Scale Full-Stack Live Simulation | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.18967` | EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts | `integrate` → `retain` | Integrate proposal — `INFER-SPECULATIVE-DECODING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present EfficientRollout, a system-aware self-SD framework designed to address this gap for RL rollouts |
| `2606.18996` | TRAP: Benchmark for Task-completion and Resistance to Active Privacy-extraction | `no_change_existing_coverage` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.19004` | Spotlight: Synergizing Seed Exploration and Spot GPUs for DiT RL Post-Training | `no_change_existing_coverage` → `retain` | Existing Coverage — `books/part-06-ai-infrastructure/63-gpu-scheduler.md` / `从固定 Job Shape 到 Elastic Configuration Portfolio；可回收资源需要 Lease 与 Reclaim Protocol` | 保留：摘要给出可定位机制——We present Spotlight, the first system that harvests spot GPUs for DiT RL post-training |
| `2606.19025` | FoMoE: Breaking the Full-Replica Barrier with a Federation of MoEs | `integrate` → `retain` | Integrate proposal — `TRAIN-DISTRIBUTED-TRAINING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——In this work, we introduce FoMoE, a system that breaks the full-replica paradigm by partitioning expert layers across workers and skipping non-resident experts during local training |
| `2606.19057` | Quantifying and Auditing LLM Evaluation via Positive--Unlabeled Learning | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.19111` | Leadership as Coordination Control: Behavioral Signatures and the Recovery-Advantage Boundary in Multi-Agent LLM Teams | `no_change_existing_coverage` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.19191` | PhantomSkill: Malicious Code Injection in Agent Skill Ecosystems | `no_change_existing_coverage` → `retain` | Integrate proposal — `PLATFORM-SECURITY`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We present PhantomSkill, an attack framework that hides malicious behavior in a skill's auxiliary resources rather than in its textual description |
| `2606.19242` | Runtime Compliance Verification for AI Agents | `no_change_existing_coverage` → `retain` | Integrate proposal — `PLATFORM-SECURITY`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We propose C-Trace (Compliance Trace based Runtime Agent Conformance Enforcement), a verification framework that: (i) expresses a subset of GDPR requirements, including consent, purpose limitation, data minimiz… |
| `2606.19262` | Detecting Hidden ML Training With Zero-Overhead Telemetry | `integrate` → `retain` | Integrate proposal — `PLATFORM-MONITORING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We develop a classifier that achieves 98.2% binary accuracy at identifying training workloads across the whole corpus, and 43-87% accuracy against the most challenging unexpected workloads even when they are ad… |
| `2606.19271` | TurboServe: Serving Streaming Video Generation Efficiently and Economically | `no_change_existing_coverage` → `retain` | Integrate proposal — `INFER-SCHEDULING`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We present TurboServe, the first serving system designed specifically for streaming video generation workloads |

## 3.7 2026-06-19 逐项审计

| arXiv | 标题 | 旧状态 → 终审 | Books 判定 | 独立判断 |
| --- | --- | --- | --- | --- |
| `2606.19376` | Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees | `no_change_existing_coverage` → `retain` | Integrate proposal — `INFER-SCHEDULING`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We introduce SLARouter, an online routing algorithm that learns a cost-optimal policy from the sparse, one-sided user feedback available in production systems |
| `2606.19380` | ClayBuddy: A Framework, Evaluation, &amp; Mitigation of Coding Agent Failures | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Across 8 evaluations that stress test these mechanisms, we find that frontier models are difficult to steer, elicit dangerous behavior through just 3 conditioning examples, and can randomly generate destructive… |
| `2606.19382` | DynAMO:Dynamic Asset Management Orchestration via Topological Multi-Agent Scheduling | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.19386` | Bistable by Construction: Wall-Clock-Calibrated State Monitors Have No Moment-Detection Regime at Agent Cadence | `integrate` → `retain` | Integrate proposal — `PLATFORM-MONITORING`；`条件化机制分支与共存边界` 约 L331 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——Runtime monitors for autonomous agents commonly threshold an accumulated internal state - a behavioural baseline, a drift statistic, or, in our prior work, a modelled affective state |
| `2606.19390` | Execution-bound advisory automation for agentic AI: a reproducible AIBOM-driven CSAF-VEX framework | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——A protocol driven framework is presented that binds SBOM and AIBOM artefacts to deterministic environment capture and structured runtime telemetry |
| `2606.19409` | OpenRath: Session-Centered Runtime State for Agent Systems | `no_change_existing_coverage` → `retain` | Existing Coverage — `books/part-07-agent/84-agent-platform.md` / `Agent Definition 与 Run Identity（typed Session 主线）` | 保留：摘要给出可定位机制——Modern agent systems often suffer from fragmented runtime state: transcripts, tool effects, memory events, workspace placement, branch provenance, and replay evidence are recorded separately and become difficul… |
| `2606.19464` | Deontic Policies for Runtime Governance of Agentic AI Systems | `no_change_existing_coverage` → `retain` | Integrate proposal — `PLATFORM-SECURITY`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We propose AgenticRei, which realizes key governance requirements such as obligations, dispensations, policy conflict resolutions, and reasoning over policies, as well as the basic permit/prohibit constraints |
| `2606.19535` | FloatDoor: Platform-Triggered Backdoors in LLMs | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce FloatDoor, the first input-independent, platform-triggered backdoor attack against generative LLMs |
| `2606.19544` | Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias | `no_change_existing_coverage` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We present the largest systematic evaluation of LLM-as-a-Judge to date: 21 judges from nine providers across MT-Bench, JudgeBench, and RewardBench, evaluated under three protocols (agreement, consistency, bias … |
| `2606.19559` | Uncertainty Decomposition for Clarification Seeking in LLM Agents | `no_change_existing_coverage` → `retain` | Integrate proposal — `AGENT-PLANNING`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——To evaluate it, we introduce two clarification-augmented benchmarks (WebShop-Clarification and ALFWorld-Clarification) in which 50% of tasks are deliberately underspecified, and systematically compare the propo… |
| `2606.19595` | IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows | `no_change_existing_coverage` → `retain` | Integrate proposal — `AGENT-WORKFLOW`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——We introduce IHBench (Interruption Handling Benchmark), a benchmark that evaluates post-interruption recovery in voice agents executing state-machine-driven workflows across 10 enterprise domains |
| `2606.19613` | StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns | `integrate` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM`；`条件化机制分支与共存边界` 约 L2236 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We introduce StaminaBench, a benchmark that measures the stamina of coding agents: how many consecutive interaction turns (change requests) they can handle before failing |
| `2606.19667` | CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference | `integrate` → `retain` | Integrate proposal — `INFER-KV-CACHE` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present CacheWeaver, a lightweight prompt-layer method for cache-aware evidence ordering |
| `2606.19692` | When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems | `integrate` → `retain` | Integrate proposal — `AGENT-RAG`；`条件化机制分支与共存边界` 约 L580 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——Vector hubness, where a few points become nearest neighbors of many queries, creates a poisoning risk in retrieval-augmented generation (RAG): one injected document can influence unrelated requests |
| `2606.19704` | Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents | `integrate` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We propose ranking configurations by predictive validity, the correlation between in-sample and out-of-sample rank, rather than in-sample mean, and report a twelve-tier measurement apparatus that exposes the de… |
| `2606.19714` | AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.19719` | Closing the Operational Gap in Semantic Caching | `integrate` → `retain` | Integrate proposal — `AGENT-RAG`；`条件化机制分支与共存边界` 约 L580 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We show this mismatch leads to systematically poor deployment choices, as models with the highest PR-AUC are often the worst in operation |
| `2606.19746` | SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL | `integrate` → `retain` | Integrate proposal — `INFER-KV-CACHE` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To address this, we propose SAC, the first efficient disaggregated KV cache system optimized for sparse attention models |
| `2606.19753` | Grounded Inference: Principles for Deterministically Encapsulated Generative Models | `no_change_existing_coverage` → `retain` | Existing Coverage — `books/part-06-ai-infrastructure/73-production-best-practice.md` / `Production Contract` | 保留：摘要给出可定位机制——The incorporation of generative models into traditional computational systems presents both enormous opportunity and tremendous peril |
| `2606.19755` | SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling | `integrate` → `retain` | Integrate proposal — `INFER-SPECULATIVE-DECODING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We propose SafeSpec, a safety-aware speculative inference framework that integrates risk estimation directly into the verification process |
| `2606.19758` | SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.19769` | Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-EMBODIED-VLA` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We develop three insights |
| `2606.19795` | Agentic Electronic Design Automation: A Handoff Perspective | `integrate` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.19803` | Policy-aware Vector Search: A Vision for Fine Grained Access Control in Vector Databases | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY`；`条件化机制分支与共存边界` 约 L1375 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——In this paper, we present a vision for Policy-aware Vector Search by formalizing the FGAC policy model in vector databases as well as the enforcement problem |
| `2606.19808` | Think Again or Think Longer? Selective Verification for Budget-Aware Reasoning | `integrate` → `retain` | Integrate proposal — `INFER-SCHEDULING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce \sevra, Selective Verification for Reasoning Allocation, a serving-layer controller that decides whether to preserve a frozen solver's initial answer or invoke active verification |
| `2606.19847` | AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts | `integrate` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.19849` | ViCoStream: Streaming VideoLLMs Can Run Beyond 100 FPS with Stage-Wise Coordinated Inference | `integrate` → `retain` | Integrate proposal — `INFER-SCHEDULING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Building on this formulation, we propose ViCoStream (Video Coordinated Streaming), a stage-wise coordinated streaming framework that combines chunk-wise execution, CUDA-stream overlap, visual token control, bou… |
| `2606.19868` | A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models | `no_change_existing_coverage` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM`；本轮未找到可接受的既有命题锚点 | 保留：摘要给出可定位机制——To address this gap, we present a systematic review of black-box UE methods and organize them into five categories: verbalization-based, sampling-based, explanation-based, multi-agent, and hybrid methods |
| `2606.19887` | FinRED: An Expert-Guided Benchmark Generation and Evaluation Framework for Financial LLM Red-Teaming | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.19898` | Query-aware Routing for Filtered Approximate Nearest Neighbors Search | `de_admit` → `retain` | Integrate proposal — `AGENT-RAG` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Therefore, we propose a query-aware routing framework |
| `2606.19899` | Measuring Biological Capabilities and Risks of AI Agents | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.19911` | Multi-Agent Transactive Memory | `integrate` → `retain` | Integrate proposal — `AGENT-MEMORY`；`条件化机制分支与共存边界` 约 L1168 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We propose Multi-Agent Transactive Memory (MATM), a framework for population-level storage and retrieval of agent-generated trajectories, where producer agents contribute trajectories to a shared repository and… |
| `2606.19989` | Online Dynamic Batching with Formal Guarantees for LLM Training | `integrate` → `retain` | Integrate proposal — `TRAIN-DISTRIBUTED-TRAINING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce Online Dynamic Batching (ODB), a DataLoader-side drop-in system that moves batch formation to this point of accurate observability while preserving DDP step alignment |
| `2606.19992` | Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services | `integrate` → `retain` | Integrated — `books/part-07-agent/83-mcp.md` / `从静态 Endpoint 到受限 Tool Program`（Review notes 前完整机制链） | 保留：摘要给出可定位机制——We present ToolPro, which represents an agent's tool intent as an \emph{executable tool program} that compactly encodes multi-step service interactions with explicit effect types |
| `2606.19998` | Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.20002` | Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.20005` | StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation | `integrate` → `retain` | Integrate proposal — `TRAIN-DISTRIBUTED-TRAINING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present StreamKL, the first fused GPU primitive for attention KL divergence that eliminates this quadratic materialization |
| `2606.20023` | When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents | `integrate` → `retain` | Integrate proposal — `AGENT-TOOL-CALLING`；`Tool Admission 与 Interaction Latency 必须分开控制` 约 L396 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We introduce ToolPrivBench to evaluate whether agents choose higher-privilege tools despite sufficient lower-privilege alternatives, measuring both initial selection and escalation after transient tool failures |
| `2606.20047` | PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.20113` | When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation | `integrate` → `retain` | Integrate proposal — `AGENT-TOOL-CALLING`；`Tool Admission 与 Interaction Latency 必须分开控制` 约 L396 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——Streaming Retrieval-Augmented Generation (Streaming RAG) hides tool latency by issuing retrieval queries in parallel with the user's still-arriving input, before the utterance is complete |
| `2606.20122` | ScaffoldAgent: Utility-Guided Dynamic Outline Optimization for Open-Ended Deep Research | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.20128` | The Correctness Illusion in LLM-Generated GPU Kernels | `integrate` → `retain` | Integrate proposal — `TRAIN-DISTRIBUTED-TRAINING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Benchmarks for LLM-generated GPU kernels (KernelBench, TritonBench, GEAK) score correctness through fixed-shape, small-sample allclose-style checks |
| `2606.20158` | N-Version Programming with Coding Agents | `integrate` → `retain` | Integrate proposal — `AGENT-WORKFLOW` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——This paper revisits the classical concept on N-version programming in the setting of contemporary AI coding agents |
| `2606.20235` | ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search in Open Literature Environments | `de_admit` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.20243` | Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs | `de_admit` → `de-admit` | — | 单一方法/框架/recipe 的局部改进；未形成跨 workload 可复用的 state、data、control 或 release 边界。 |
| `2606.20245` | Navigating Unreliable Parametric and Contextual Knowledge: Explicit Knowledge Conflict Resolution for LLM Inference | `no_change_existing_coverage` → `retain` | Existing Coverage — `books/part-07-agent/75-context.md` / `Context Assembly Pipeline` | 保留：摘要给出可定位机制——To address these limitations, we propose a novel framework MACR for LLM knowledge conflict resolution that moves beyond the conventional binary choice paradigm and incorporates an explicit conflict-resolution m… |
| `2606.20254` | Quantization as a Malicious Task: Removing Quantization-Conditioned Backdoors via Task Arithmetic | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY`；`条件化机制分支与共存边界` 约 L1375 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——Here, we present QVec, a parameter-space perspective for defending against QCBs |
| `2606.20318` | AgenticDB: Self-Evolving Reconfiguration Framework for Database Workloads | `integrate` → `de-admit` | — | 范围外：对象不是大模型/Agent/其基础设施的长期机制，或属于当前明确延期的 AI for Science/行业任务。 |
| `2606.20363` | Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.20374` | ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters | `integrate` → `retain` | Integrate proposal — `PLATFORM-TRACE` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We propose ARGUS, a low-overhead, fine-grained, always-on tracing and real-time analysis system for training workloads in 10,000+ GPU-scale production clusters |
| `2606.20381` | Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe | `integrate` → `retain` | Integrate proposal — `TRAIN-DISTRIBUTED-TRAINING` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——In this study, we identify a fundamental limitation of that choice: non-uniform formats such as E2M1 inherently suffer from Shrinkage Bias, a systematic negative rounding error caused by the geometric asymmetry… |
| `2606.20408` | NRT-Bench: Benchmarking Multi-Turn Red-Teaming of LLM Operator Agents in Safety-Critical Control Rooms | `no_change_existing_coverage` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.20470` | Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on Agentic AI Systems | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.20474` | UltraQuant: 4-bit KV Caching for Context-Heavy Agents | `integrate` → `retain` | Integrate proposal — `INFER-KV-CACHE` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Third, we present serving optimizations on AMD GPUs, including optimized decode-attention kernels and UltraQuant, an FP4 approximation path that uses FP8 queries, FP4 KV tensors, UE8M0 group scales, and native … |
| `2606.20475` | Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.20487` | Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems | `integrate` → `retain` | Integrate proposal — `AGENT-WORKFLOW` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We propose \textbf{H-RePlan}, a hierarchical replanning framework for multi-device agents with unified API--CLI--GUI execution |
| `2606.20493` | Contagion Networks: Evaluator Preference Propagation in Multi-Agent LLM Systems | `integrate` → `retain` | Integrate proposal — `AGENT-MULTI-AGENT` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce Contagion Networks, a formal framework for measuring how evaluator preferences spread across interacting LLM agents |
| `2606.20502` | Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software | `no_change_existing_coverage` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.20510` | Efficient and Sound Probabilistic Verification for AI Agents | `integrate` → `retain` | Integrate proposal — `AGENT-WORKFLOW` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——Securing AI agents that operate in complex digital environments has become a critical need, and runtime monitoring approaches that formulate and enforce policies expressed in a formal language like Datalog offe… |
| `2606.20512` | Probe-and-Refine Tuning of Repository Guidance for Coding Agents | `integrate` → `de-admit` | — | 局部 benchmark、指标或任务级方法；摘要未给出足以改变长期系统设计判断的新契约。 |
| `2606.20520` | Sovereign Execution Broker: Enforcing Certificate-Bound Authority in Agentic Control Planes | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We present the SEB execution model, certificate and replay-verification predicates, scoped identity semantics, bypass-prevention deployment patterns, failure behavior, and a concrete prototype implementation |
| `2606.20529` | LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents | `integrate` → `retain` | Integrate proposal — `AGENT-MEMORY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce \textsc{LedgerAgent}, an inference-time method for tool-calling agents that maintains observed task states in a separate ledger and renders the states into the prompt |
| `2606.20536` | The FID Lottery: Quantifying Hidden Randomness in Generative-Model Evaluation | `integrate` → `retain` | Integrate proposal — `PLATFORM-EVALUATION-SYSTEM` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——The Frechet Inception Distance (FID) is the de facto arbiter of image generation, yet most papers report just a single number from a single trained model using a single sampling seed |
| `2606.20537` | Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving | `integrate` → `retain` | Integrate proposal — `INFER-REQUEST-LIFECYCLE`；`条件化机制分支与共存边界` 约 L286 只有 source-bound 片段，须并入 owner 论证链 | 保留：摘要给出可定位机制——We introduce execution-state capsules, a graph-bound checkpoint and restore mechanism for the complete restorable state at a committed boundary |
| `2606.20545` | Current World Models Lack a Persistent State Core | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-WORLD-MODELS` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——We introduce \textbf{WRBench}, the first systematic diagnostic benchmark that treats camera motion as an intervention on observability and resolves evaluation into a human-calibrated chain that asks whether the… |
| `2606.20553` | From Efficiency to Leakage -- Privacy Backdoor in Federated Language Model Fine-Tuning | `integrate` → `retain` | Integrate proposal — `PLATFORM-SECURITY` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——In this paper, we show that a malicious parameter server can stealthily corrupt a PEFT adapter into a privacy backdoor that implicitly memorizes the client's training samples as isolated per-sample parameter up… |
| `2606.20562` | MemoryWAM: Efficient World Action Modeling with Persistent Memory | `integrate` → `retain` | Integrate proposal — `MULTIMODAL-EMBODIED-VLA` owner 级合并，不逐论文追加 | 保留：摘要给出可定位机制——To address this challenge, we introduce MemoryWAM, a world action model with efficient persistent memory |

## 4. Canonical owner 级正文 proposal

以下 216 个 family 尚未写入正文，按 28 个 canonical owner 合并。它们不是待追加的论文列表；每个 owner 只写可成立的机制演进链，并在写后重新判断是否仍应 Integrate。

### AGENT-MEMORY

- Source families：`2606.11806`, `2606.12329`, `2606.13681`, `2606.14106`, `2606.14275`, `2606.14470`, `2606.15903`, `2606.17328`, `2606.17591`, `2606.18746`, `2606.19911`, `2606.20529`
- 合并问题：External Experience Serving in Production LLM Systems: A Deployment-Oriented Study of Quality-Cost Trade-offs；PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents；EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments；另 9 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### AGENT-MULTI-AGENT

- Source families：`2606.13733`, `2606.15376`, `2606.17182`, `2606.18121`, `2606.18668`, `2606.20493`
- 合并问题：How Task Structure Limits Multi-Agent Success: An Information-Theoretic Analysis；CoAgent: Concurrency Control for Multi-Agent Systems；Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems；另 3 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### AGENT-PLANNING

- Source families：`2606.14574`, `2606.19559`
- 合并问题：SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model；Uncertainty Decomposition for Clarification Seeking in LLM Agents
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### AGENT-RAG

- Source families：`2606.11265`, `2606.12469`, `2606.15179`, `2606.16341`, `2606.17467`, `2606.18037`, `2606.18310`, `2606.18497`, `2606.19692`, `2606.19719`, `2606.19898`
- 合并问题：When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines；Influence Factors on RAG Poisoning；CONCORD: Asynchronous Sparse Aggregation for Device-Cloud RAG under Document Isolation；另 8 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### AGENT-REFLECTION

- Source families：`2606.11543`, `2606.14629`
- 合并问题：SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior；When Good Verifiers Go Bad: Self-Improving VLMs Can Regress on New Tasks
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### AGENT-TOOL-CALLING

- Source families：`2606.13663`, `2606.14832`, `2606.16813`, `2606.17519`, `2606.20023`, `2606.20113`
- 合并问题：HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents；PhoneHarness: Harnessing Phone-Use Agents through Mixed GUI, CLI, and Tool Actions；GIST-CMTF: Goal-State Inference for Causal Minimal Tool Filtering in LLM Agents；另 3 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### AGENT-WORKFLOW

- Source families：`2606.11290`, `2606.11688`, `2606.13174`, `2606.14239`, `2606.14790`, `2606.16988`, `2606.17099`, `2606.17573`, `2606.19595`, `2606.20158`, `2606.20487`, `2606.20510`
- 合并问题：FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse；Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents；Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents；另 9 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### INFER-DECODE

- Source families：`2606.11357`, `2606.15070`
- 合并问题：TileFuse: A Fused Mixed-Precision Kernel Library for Efficient Quantized LLM Inference on AMD NPUs；Stop When Further Reasoning Won't Help: Attention-State Adaptive Generation in Reasoning Models
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### INFER-GPU-MEMORY

- Source families：`2606.11718`, `2606.12556`, `2606.14779`, `2606.15453`, `2606.15789`
- 合并问题：Making Locality-aware GEMM Compatible with Page-Granularity Placement on Chiplet GPUs；ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories；Unified KV Pooling to Accelerate Long-Context LLM Serving；另 2 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### INFER-KSERVE-TOPOLOGY

- Source families：`2606.12688`
- 合并问题：M*: A Modular, Extensible, Serving System for Multimodal Models
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### INFER-KV-CACHE

- Source families：`2606.15157`, `2606.16135`, `2606.16824`, `2606.17034`, `2606.17107`, `2606.17872`, `2606.19667`, `2606.19746`, `2606.20474`
- 合并问题：PolyKV: Heterogeneous Retention and Allocation for KV Cache Compression；SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing；CacheWise: Understanding Workloads and Optimizing KVCache Management for Efficiently Serving LLM Coding Agents；另 6 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### INFER-PD-DISAGGREGATION

- Source families：`2606.13708`, `2606.16264`, `2606.17081`, `2606.17104`
- 合并问题：Tiara: A Programmable Line-Rate ISA for Remote Memory Access；Tropical: Enhancing SLO Attainment in Disaggregated LLM Serving via SLO-Aware Multiplexing；The Price of Anarchy in Disaggregated Inference；另 1 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### INFER-REQUEST-LIFECYCLE

- Source families：`2606.20537`
- 合并问题：Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### INFER-SCHEDULING

- Source families：`2606.12950`, `2606.13501`, `2606.14356`, `2606.15177`, `2606.15319`, `2606.15555`, `2606.16106`, `2606.17378`, `2606.17787`, `2606.18431`, `2606.18600`, `2606.18741`, `2606.19271`, `2606.19376`, `2606.19808`, `2606.19849`
- 合并问题：Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-Based Multi-Agent Systems；GF-DiT: Scheduling Parallelism for Diffusion Transformer Serving；PLAIground: SLO-Driven Runtime Model Selection for Compound AI Systems in the Edge-Cloud-Space Continuum；另 13 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### INFER-SPECULATIVE-DECODING

- Source families：`2606.12370`, `2606.18394`, `2606.18967`, `2606.19755`
- 合并问题：Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling；JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting；EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts；另 1 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### INFER-TENSORRT-LLM

- Source families：`2606.12487`, `2606.12765`, `2606.15652`, `2606.15682`, `2606.15991`, `2606.17518`, `2606.17566`, `2606.18421`
- 合并问题：DynamicPTQ: Mitigating Activation Quantization Collapse via Residual-Stream Dynamics；Rigel: Reverse-Engineering the Metal 4.1 Tensor Compute Path on the Apple M4 Max GPU；MosaicQuant: Inlier-Outlier Disaggregation for Unified 4-Bit LLM Quantization；另 5 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### MODEL-LONG-CONTEXT

- Source families：`2606.15378`, `2606.16310`
- 合并问题：Rethinking the Role of Efficient Attention in Hybrid Architectures；QK-Normed MLA: QK normalization without full key caching
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### MULTIMODAL-EMBODIED-VLA

- Source families：`2606.12978`, `2606.15285`, `2606.16690`, `2606.18247`, `2606.18847`, `2606.19769`, `2606.20562`
- 合并问题：Trajectory-Level Redirection Attacks on Vision-Language-Action Models；Acting While Understanding: Asynchronous Semantic-Action Decoupling for Real-Time Vision-Language-Action Models；PATCH: Action-Chunk-Conditioned Latent Patch Innovation Monitoring for Robot Manipulation；另 4 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### MULTIMODAL-GENERATIVE-PARADIGMS

- Source families：`2606.13426`, `2606.13496`, `2606.14620`, `2606.15805`
- 合并问题：Accelerating Speculative Diffusions via Block Verification；Budget-Constrained Step-Level Diffusion Caching；Neither Parallel Nor Sequential: How DiffusionGemma Actually Commits Tokens；另 1 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### MULTIMODAL-WORLD-MODELS

- Source families：`2606.13053`, `2606.13092`, `2606.15341`, `2606.15594`, `2606.17730`, `2606.18208`, `2606.18697`, `2606.20545`
- 合并问题：EV-WM: Event-Verified World Models for Long-Horizon Robotic Manipulation；Certified World Models: Predictability Across Configuration, Horizon, and Resolution；CausalDrive: Real-time Causal World Models for Autonomous Driving；另 5 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### PLATFORM-EVALUATION-SYSTEM

- Source families：`2606.11409`, `2606.11686`, `2606.13608`, `2606.14516`, `2606.14571`, `2606.14674`, `2606.15474`, `2606.15964`, `2606.16062`, `2606.16682`, `2606.17383`, `2606.17930`, `2606.18168`, `2606.18356`, `2606.18467`, `2606.19544`, `2606.19613`, `2606.19704`, `2606.19868`, `2606.20536`
- 合并问题：Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models；Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness；AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility；另 17 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### PLATFORM-GATEWAY

- Source families：`2606.13968`, `2606.15050`, `2606.15822`, `2606.16358`, `2606.17949`
- 合并问题：STREAM: Multi-Tier LLM Inference Middleware with Dual-Channel HPC Token Streaming；Solyx AI Grid: Hardware-Telemetry-Aware Routing Across Geographically Distributed GPU Clusters；TrustedARI: Towards Trust-Native Agentic Routing Infrastructure for Agentic AI；另 2 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### PLATFORM-MONITORING

- Source families：`2606.11916`, `2606.11949`, `2606.14589`, `2606.15980`, `2606.19262`, `2606.19386`
- 合并问题：Characterizing Software Aging in GPU-Based LLM Serving Systems；Online Shift Detection and Conformal Adaptation for Deployed Safety Classifiers；When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime；另 3 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### PLATFORM-SECURITY

- Source families：`2606.11632`, `2606.11671`, `2606.11871`, `2606.11878`, `2606.11998`, `2606.12703`, `2606.12737`, `2606.12797`, `2606.13949`, `2606.14027`, `2606.14154`, `2606.14517`, `2606.14518`, `2606.14783`, `2606.15020`, `2606.15242`, `2606.15308`, `2606.15441`, `2606.15549`, `2606.15609`, `2606.16100`, `2606.16287`, `2606.16352`, `2606.16519`, `2606.16821`, `2606.16914`, `2606.17110`, `2606.17421`, `2606.18198`, `2606.18400`, `2606.18532`, `2606.18550`, `2606.18673`, `2606.18829`, `2606.19191`, `2606.19242`, `2606.19380`, `2606.19390`, `2606.19464`, `2606.19535`, `2606.19803`, `2606.20254`, `2606.20520`, `2606.20553`
- 合并问题：Sovereign Assurance Boundary: Certificate-Bound Admission for Agentic Infrastructure；Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security；WarpGuard: Protected-Site Control-Flow Integrity for CUDA SASS Binaries；另 41 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### PLATFORM-TRACE

- Source families：`2606.14805`, `2606.20374`
- 合并问题：Knowledge-Based Zero-Replay Debugging of Multi-Agent LLM Traces；ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### TRAIN-DATA

- Source families：`2606.11270`, `2606.12385`, `2606.13873`, `2606.17122`, `2606.18284`, `2606.18650`
- 合并问题：Quantifying Subliminal Behavioral Transfer Ratios in Language Model Distillation；Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs；Natively Unlearnable Large Language Models；另 3 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### TRAIN-DISTRIBUTED-TRAINING

- Source families：`2606.15045`, `2606.16384`, `2606.16907`, `2606.19025`, `2606.19989`, `2606.20005`, `2606.20128`, `2606.20381`
- 合并问题：NEURON-Fabric: CXL-Side Low-Bit Gradient Aggregation for Distributed Training；Mixtures of Subspaces for Bandwidth Efficient Context Parallel Training；Tangram: Hiding GPU Heterogeneity for Efficient LLM Parallelization；另 5 项同 owner 证据
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。

### TRAIN-GRPO

- Source families：`2606.14179`, `2606.15455`, `2606.18810`
- 合并问题：CacheRL:Multi-Turn Tool-Calling Agents via Cached Rollouts and Hybrid Reward；Understanding Diversity Collapse in RLVR via the Lens of Overtraining；Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards
- 写作要求：只吸收共同的长期 mechanism delta；正文须位于 Review notes 前，并明确旧路径、状态/控制权、证据边界、trade-off 与 fallback。
## 5. 旧采用链清理队列复核

28 条旧 adoption residue 已按 exact Source Family 复核：24 条错误残留已从 Books 删除，4 条 fresh audit 恢复项保留。清理没有使用整段或章尾覆盖，不影响并行写入的其他正文。

| Source Family | 原定位 / 当前状态 | Fresh disposition |
| --- | --- | --- |
| `SF-2026-ARXIV-2606-11257` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-11522` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-13145` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-13621` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-15153` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-15210` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-15216` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-15258` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-15333` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-15493` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-15508` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-15625` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-15682` | `books/part-05-inference-system/49-tensorrt-llm.md` | 恢复准入：保留原 adoption chain；Books 仍按 owner-level proposal 审核 |
| `SF-2026-ARXIV-2606-15963` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-15994` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-16000` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-16341` | `books/part-07-agent/76-rag.md` | 恢复准入：保留原 adoption chain；Books 仍按 owner-level proposal 审核 |
| `SF-2026-ARXIV-2606-16429` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-16541` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-16690` | `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` | 恢复准入：保留原 adoption chain；Books 仍按 owner-level proposal 审核 |
| `SF-2026-ARXIV-2606-16751` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-16774` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-17209` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-17533` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-18144` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-18286` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-18831` | 原账本定位；当前 Books 检索为 0 | 已清理：删除精确 source-specific trace/marker；未删除相邻独立机制 |
| `SF-2026-ARXIV-2606-19898` | `books/part-07-agent/76-rag.md` | 恢复准入：保留原 adoption chain；Books 仍按 owner-level proposal 审核 |

## 6. Gate 结论

- **Candidate Denominator：Pass。** 七日 378 个边界条目逐项终审，最终 retained 231、de-admit 147；5 项恢复、104 项撤销旧准入。
- **Books 已决项：Pass。** 当前 39 项实际 Integrated 与 65 项 Existing Coverage 均定位到 Review notes 前的命题级正文；其中本批关闭全部 51 个 `AGENT-*` pending（13 Integrated / 38 Existing），并同步主任务已裁定的 Model、Multimodal 与 Training 结果（22 Integrated / 16 Existing）。
- **Books Integration：Pending。** 其余 127 个 family 归属 14 个 canonical owner；均为 `INFER-*` 或 `PLATFORM-*`，不把 proposal、trace 或 source marker 当作完成。
- **旧采用链：Pass。** 24 条明确错误 residue 已清理；4 条恢复项保留。
- **Daily Complete：Fail / Pending。** 七份 Daily 已同步终审结果并通过结构校验，但真实 Books 正文与 post-write fresh audit 尚未完成，状态保持进行中。

逐日当前账目如下；`Pending` 均不包含已决 Agent / Model / Multimodal / Training family：

| 日期 | Retained | Integrated | Existing Coverage | Pending |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-11 | 24 | 3 | 9 | 12 |
| 2026-06-12 | 24 | 6 | 8 | 10 |
| 2026-06-15 | 22 | 3 | 7 | 12 |
| 2026-06-16 | 58 | 8 | 12 | 38 |
| 2026-06-17 | 28 | 4 | 9 | 15 |
| 2026-06-18 | 28 | 8 | 3 | 17 |
| 2026-06-19 | 47 | 7 | 17 | 23 |

剩余 owner groups：`INFER-DECODE`、`INFER-GPU-MEMORY`、`INFER-KSERVE-TOPOLOGY`、`INFER-KV-CACHE`、`INFER-PD-DISAGGREGATION`、`INFER-REQUEST-LIFECYCLE`、`INFER-SCHEDULING`、`INFER-SPECULATIVE-DECODING`、`INFER-TENSORRT-LLM`、`PLATFORM-EVALUATION-SYSTEM`、`PLATFORM-GATEWAY`、`PLATFORM-MONITORING`、`PLATFORM-SECURITY`、`PLATFORM-TRACE`。

## 7. 给共享写入者的剩余执行顺序

1. 按以上 14 个 Stable Node owner 合并 127 个 pending family；同 owner 不逐论文追加。
2. 每个 owner 写回后重新顺读相邻正文，必要时把证据降为 Existing Coverage 或 de-admit。
3. 由未参与写入的 reviewer 做 post-write fresh audit，再把对应 Daily 从进行中升级为完成。
4. 逐日运行 `validate_research.py`、`check_report_v3.py` 并检查 `git diff --check`。
