# 2026-02-18 第三批准入校准

仅有限主题发现中已经实际读完整题摘、具有具体待核增量的八项；不继承旧候选，不代表候选冻结或证据完成。题摘原始复用 inventory.json 对应同 ID 字段，body 仅复用同 exact-v1 的原始抓取，必要日期待逐项 live 核。Submitted 原值本身不是 first-public。

## 2602.13594 — Hippocampus: An Efficient and Scalable Memory Module for Agentic AI

原文：[exact-v1](https://arxiv.org/html/2602.13594v1)。Submitted线索 UTC：2026-02-14T04:25:20Z，不用于精确公开。

完整摘要：

Agentic AI require persistent memory to store user-specific histories beyond the limited context window of LLMs. Existing memory systems use dense vector databases or knowledge-graph traversal (or hybrid), incurring high retrieval latency and poor storage scalability. We introduce Hippocampus, an agentic memory management system that uses compact binary signatures for semantic search and lossless token-ID streams for exact content reconstruction. Its core is a Dynamic Wavelet Matrix (DWM) that compresses and co-indexes both streams to support ultra-fast search in the compressed domain, thus avoiding costly dense-vector or graph computations. This design scales linearly with memory size, making it suitable for long-horizon agentic deployments. Empirically, our evaluation shows that Hippocampus reduces end-to-end retrieval latency by up to 31$\times$ and cuts per-query token footprint by up to 14$\times$, while maintaining accuracy on both LoCoMo and LongMemEval benchmarks.

作者初筛：persistent memory 的 dense/graph 召回成本→binary signature 与 lossless token-ID 共同压缩/共索引→判断能否不解压执行语义候选检索而保留精确内容；不能把二进制压缩名称当系统增量。 拟 2+1+2=5；尚待必要日期、标准/受影响深入与 Books 判断。

## 2602.13967 — Neuromem: A Granular Decomposition of the Streaming Lifecycle in External Memory for LLMs

原文：[exact-v1](https://arxiv.org/html/2602.13967v1)。Submitted线索 UTC：2026-02-15T02:53:37Z，不用于精确公开。

完整摘要：

Most evaluations of External Memory Module assume a static setting: memory is built offline and queried at a fixed state. In practice, memory is streaming: new facts arrive continuously, insertions interleave with retrievals, and the memory state evolves while the model is serving queries. In this regime, accuracy and cost are governed by the full memory lifecycle, which encompasses the ingestion, maintenance, retrieval, and integration of information into generation. We present Neuromem, a scalable testbed that benchmarks External Memory Modules under an interleaved insertion-and-retrieval protocol and decomposes its lifecycle into five dimensions including memory data structure, normalization strategy, consolidation policy, query formulation strategy, and context integration mechanism. Using three representative datasets LOCOMO, LONGMEMEVAL, and MEMORYAGENTBENCH, Neuromem evaluates interchangeable variants within a shared serving stack, reporting token-level F1 and insertion/retrieval latency. Overall, we observe that performance typically degrades as memory grows across rounds, and time-related queries remain the most challenging category. The memory data structure largely determines the attainable quality frontier, while aggressive compression and generative integration mechanisms mostly shift cost between insertion and retrieval with limited accuracy gain.

作者初筛：离线构建固定 memory 的评价→插入/召回交错并在同服务栈分账成本→验证 compression/integration 收益是否仅把成本搬到另一个生命周期阶段。 拟 2+1+2=5；尚待必要日期、标准/受影响深入与 Books 判断。

## 2602.13977 — WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL

原文：[exact-v1](https://arxiv.org/html/2602.13977v1)。Submitted线索 UTC：2026-02-15T03:48:20Z，不用于精确公开。

完整摘要：

Reinforcement learning (RL) promises to unlock capabilities beyond imitation learning for Vision--Language--Action (VLA) models, but its requirement for massive real-world interaction prevents direct deployment on physical robots. Recent work attempts to use learned world models as simulators for policy optimization, yet closed-loop imagined rollouts inevitably suffer from hallucination and long-horizon error accumulation. Such errors not only degrade visual fidelity, but also mislead policy optimization by providing unreliable learning signals. We propose WoVR, a reliable world-model-based RL framework for post-training VLA policies. Instead of assuming a faithful world model, WoVR explicitly regulates how RL interacts with imperfect imagined dynamics. It improves rollout stability through a controllable action-conditioned video world model, reshapes imagined interaction to reduce effective error depth via Keyframe-Initialized Rollouts, and maintains policy--simulator alignment through World Model-Policy co-evolution. Extensive experiments demonstrate that WoVR enables stable long-horizon imagined rollouts and effective policy optimization, achieving superior LIBERO performance and consistent real-world gains across multiple robotic platforms. These results show that world models can serve as practical simulators for RL when hallucination is explicitly controlled. Additional visualization results are available at https://wovr-corl.github.io.

作者初筛：learned simulator 不可靠的长 imagined rollout→keyframe 初始化缩短 error depth 与 policy/world co-evolution→决定 post-training 能否在不假定真实模拟器下采用，并保留 closed-loop alignment 条件。 拟 2+2+2=6；尚待必要日期、标准/受影响深入与 Books 判断。

## 2602.14093 — GUI-GENESIS: Automated Synthesis of Efficient Environments with Verifiable Rewards for GUI Agent Post-Training

原文：[exact-v1](https://arxiv.org/html/2602.14093v1)。Submitted线索 UTC：2026-02-15T10:58:01Z，不用于精确公开。

完整摘要：

Post-training GUI agents in interactive environments is critical for developing generalization and long-horizon planning capabilities. However, training on real-world applications is hindered by high latency, poor reproducibility, and unverifiable rewards relying on noisy visual proxies. To address the limitations, we present GUI-GENESIS, the first framework to automatically synthesize efficient GUI training environments with verifiable rewards. GUI-GENESIS reconstructs real-world applications into lightweight web environments using multimodal code models and equips them with code-native rewards, executable assertions that provide deterministic reward signals and eliminate visual estimation noise. Extensive experiments show that GUI-GENESIS reduces environment latency by 10 times and costs by over $28,000 per epoch compared to training on real applications. Notably, agents trained with GUI-GENESIS outperform the base model by 14.54% and even real-world RL baselines by 3.27% on held-out real-world tasks. Finally, we observe that models can synthesize environments they cannot yet solve, highlighting a pathway for self-improving agents.

作者初筛：真实GUI慢且visual reward有噪→合成可执行 web 环境和code-native assertion→核 deterministic oracle是否只是合成语义内可验证、是否真实held-out迁移，而不是回报值就是现实正确。 拟 2+2+2=6；尚待必要日期、标准/受影响深入与 Books 判断。

## 2602.14200 — TS-Haystack: A Multi-Task Retrieval Benchmark for Long-Context Time-Series Reasoning

原文：[exact-v1](https://arxiv.org/html/2602.14200v1)。Submitted线索 UTC：2026-02-15T15:50:02Z，不用于精确公开。

完整摘要：

Time Series Language Models (TSLMs) promise reasoning over real-world temporal data, but their ability to retrieve and reason over long time-series remains largely untested. We introduce TS-Haystack, a multi-domain retrieval benchmark with ten event-grounded question-answering tasks over contexts from 100 seconds to 24 hours, spanning direct retrieval, temporal reasoning, multi-step reasoning, and contextual anomaly detection. Existing TSLMs exhibit severe long-context degradation: accuracy declines with context length, direct-tokenization models run out of memory beyond 100 seconds on high-rate signals, and time-interval-grounded tasks collapse toward near-zero accuracy when increasing the time-series lengths, aligning with existing literature on text and multi-modal long context retrieval. An agentic retrieval framework using specialized time-series classifier tools matches or outperforms SoTA TSLMs on 9 of 10 tasks, highlighting agentic retrieval as a promising approach for long-context TSLMs.

作者初筛：把长时间轴退步都归上下文记忆→direct tokenizer高采样率资源崩溃与interval grounding相区别→验证长时序评价是否混杂表示容量、时间identity与实际检索。 拟 2+1+2=5；尚待必要日期、标准/受影响深入与 Books 判断。

## 2602.14337 — LongCLI-Bench: A Preliminary Benchmark and Study for Long-horizon Agentic Programming in Command-Line Interfaces

原文：[exact-v1](https://arxiv.org/html/2602.14337v1)。Submitted线索 UTC：2026-02-15T23:12:57Z，不用于精确公开。

完整摘要：

Recent advances in AI-assisted programming have empowered agents to execute complex workflows via command-line interfaces, however, existing benchmarks are limited by short task horizons, data contamination from GitHub scraping, and a lack of fine-grained evaluation metrics, fail to rigorously evaluate the long-horizon planning and execution capabilities essential for realistic software engineering. To address these gaps, we introduce LongCLI-Bench, a comprehensive benchmark designed to evaluate agentic capabilities across long-horizon, realistic tasks. We curated 20 high-quality, long-horizon tasks from over 1,000 computer science assignments and real-world workflows, covering four engineering categories: from scratch, feature addition, bug fixing, and refactoring. We propose a dual-set testing protocol for LongCLI-Bench, which measures requirement fulfillment (fail-to-pass) and regression avoidance (pass-to-pass), and incorporates step-level scoring to pinpoint execution failures. Extensive experiments reveal that even state-of-the-art agents achieve pass rates below 20% in LongCLI-Bench. Step-level analysis further indicates that the majority of tasks stall at less than 30% completion, highlighting that critical failures often occur in the early stages. Although self-correction offers marginal gains, human-agent collaboration through plan injection and interactive guidance yields significantly higher improvements. These results highlight that future research must emphasize the development of synergistic human-agent workflows alongside advances in agents' planning and execution capabilities to overcome key challenges in long-horizon task performance.

作者初筛：低pass总分不足定位长CLI失败→双测试集与step级进度、plan injection/interactive guidance对照→判断早期执行停滞是否可由规划提示解决，不把更长benchmark单独计贡献。 拟 2+1+2=5；尚待必要日期、标准/受影响深入与 Books 判断。

## 2602.14516 — Efficient Multi-round LLM Inference over Disaggregated Serving

原文：[exact-v1](https://arxiv.org/html/2602.14516v1)。Submitted线索 UTC：2026-02-16T07:07:30Z，不用于精确公开。

完整摘要：

With the rapid evolution of Large Language Models (LLMs), multi-round workflows, such as autonomous agents and iterative retrieval, have become increasingly prevalent. However, this raises hurdles for serving LLMs under prefill-decode (PD) disaggregation, a widely adopted paradigm that separates the compute-bound prefill phase and memory-bound decode phase onto individual resources. Specifically, existing systems overlook the interleaved prefill-decode workload pattern in multi-round inference, leading to sub-optimal handling of the incremental prefill workloads and model deployment for the two phases.
 In this work, we present AMPD, a brand new disaggregated serving framework for multi-round LLM inference. The core of AMPD is to coordinate the prefill workloads based on real-time workloads by adaptively determining where to carry out these workloads and how they are scheduled, in order to maximize service level objective (SLO) attainment. In addition, we tailor a planning algorithm for our scenario, facilitating the deduction of optimal resource allocation and parallel strategies for the two phases. Empirical results demonstrate that AMPD substantially improves SLO attainment compared to state-of-the-art baselines.

作者初筛：多轮 incremental prefill打破一次PD放置假设→负载驱动执行位置/排队与阶段deployment共同规划→改变多轮PD的placement和SLO选择；最优须核假设。 拟 2+2+2=6；尚待必要日期、标准/受影响深入与 Books 判断。

## 2602.14849 — Atomix: Timely, Transactional Tool Use for Reliable Agentic Workflows

原文：[exact-v1](https://arxiv.org/html/2602.14849v1)。Submitted线索 UTC：2026-02-16T15:46:19Z，不用于精确公开。

完整摘要：

LLM agents execute multi-step workflows that mutate external state through tools. Common orchestrators treat tool return as the settlement trigger, so faults, speculation, and concurrent agents can leave partial effects, losing-branch residue, stale writes, or irreversible sends. Correct settlement needs two facts that retries, checkpoint replay, locks, and compensation each conflate: which effects must settle together, and when earlier conflicting work is exhausted. Atomix makes this split explicit with progress-aware transactions. The runtime records reads and effects during execution, seals a transaction when its footprint is complete, and commits only after per-resource frontiers show that no earlier conflicting work can still arrive. Commit is final settlement: Atomix releases bufferable effects, accepts reversible external effects as final, and lets irreversible effects leave the gate. Abort suppresses unreleased effects and compensates externalized reversible effects where possible. On representative agent workloads, this composition improves clean recovery under injected faults, isolates contending and speculative work, and prevents correctly classified irreversible actions from leaking; microbenchmarks show microsecond-scale wrapper overhead relative to tool latency.

作者初筛：工具return被当settlement、重试/补偿混淆effect grouping和时序→footprint sealing与resource frontier分别定义→改变何时外部效果可finalize，并核irreversible分类/补偿限制。 拟 3+3+2=8；尚待必要日期、标准/受影响深入与 Books 判断。

## 精确版本校正（仅有实际差信号的两项）

上面 TS-Haystack 与 Atomix 完整摘要是 discovery inventory 的当前版本，不是本窗精确v1；发现此差异后只校正受影响命题，不扩整家族revision史。

### TS-Haystack 2602.14200v1

实际完整v1摘要，`exact-v1-bodies/2602.14200v1.txt`:106–115：

Time Series Language Models (TSLMs) are emerging as unified models for reasoning over continuous signals in natural language. However, long-context retrieval remains a major limitation: existing models are typically trained and evaluated on short sequences, while real-world time-series sensor streams can span millions of datapoints. This mismatch requires precise temporal localization under strict computational constraints, a regime that is not captured by current benchmarks. We introduce TS-Haystack, a long-context temporal retrieval benchmark comprising ten task types across four categories: direct retrieval, temporal reasoning, multi-step reasoning and contextual anomaly. The benchmark uses controlled needle insertion by embedding short activity bouts into longer longitudinal accelerometer recordings, enabling systematic evaluation across context lengths ranging from seconds to 2 hours per sample. We hypothesize that existing TSLM time series encoders overlook temporal granularity as context length increases, creating a task-dependent effect: compression aids classification but impairs retrieval of localized events. Across multiple model and encoding strategies, we observe a consistent divergence between classification and retrieval behavior. Learned latent compression preserves or improves classification accuracy at compression ratios up to 176×, but retrieval performance degrades with context length, incurring in the loss of temporally localized information. These results highlight the importance of architectural designs that decouple sequence length from computational complexity while preserving temporal fidelity.

v1准入收窄：classification可提高却不保证localized retrieval → controlled insertion与gold segmentation oracle区分高率表示资源/时间定位限制 → 核表示budget不能替代task-grounded fidelity。保持2+1+2=5，不采用current-v6 agentic9/10/24h结果。

### Atomix 2602.14849v1

实际完整v1摘要，`exact-v1-bodies/2602.14849v1.txt`:124–125：

LLM agents increasingly act on external systems, yet tool effects are immediate. Under failures, speculation, or contention, losing branches can leak unintended side effects with no safe rollback. We introduce Atomix, a runtime that provides progress-aware transactional semantics for agent tool calls. Atomix tags each call with an epoch, tracks per-resource frontiers, and commits only when progress predicates indicate safety; bufferable effects can be delayed, while externalized effects are tracked and compensated on abort. Across real workloads with fault injection, transactional retry improves task success, while frontier-gated commit strengthens isolation under speculation and contention. The code and artifacts of Atomix are available at https://github.com/mpi-dsg/atomix .

v1准入收窄：toolreturn/补偿不说明较早工作是否耗尽 → epoch与显式resource frontier/finalization及effect-class分工 → 核何时可受条件settle，保持3+3+2=8；不采用后来v2 footprint sealing，orchestrator耗尽证明必须真实成立。root必要v1/PRE及实际Ch81正文邻接/末注POST通过，仅修正frontier≥epoch，非严格>。

