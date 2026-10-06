# 03/16 第二批有限题摘与当前metadata

本日收窄主题152去重标题线索及定点primary的语义补检22项（其中12595来自初始较宽命中，不伪称全部属于152）；完整v1题摘实际读取，current API版本/comments轻量检查不替代完整版本史。另已读22 current官方abs header/comments，见V3_SECOND_CURRENT_HEADERS。没有withdraw/明确纠错字段命中；版本变化本身未授重要修订。Submitted仅发现，不是公开。分项贡献/日期见SCREENING；不以数量配额或旧30池决定。

```json
[
  {
    "id": "http://arxiv.org/abs/2603.12901v1",
    "title": "A theory of learning data statistics in diffusion models, from easy to hard",
    "submitted": "2026-03-13T11:07:01Z",
    "updated": "2026-03-13T11:07:01Z",
    "comment": "",
    "abstract": "While diffusion models have emerged as a powerful class of generative models, their learning dynamics remain poorly understood. We address this issue first by empirically showing that standard diffusion models trained on natural images exhibit a distributional simplicity bias, learning simple, pair-wise input statistics before specializing to higher-order correlations. We reproduce this behaviour in simple denoisers trained on a minimal data model, the mixed cumulant model, where we precisely control both pair-wise and higher-order correlations of the inputs. We identify a scalar invariant of the model that governs the sample complexity of learning pair-wise and higher-order correlations that we call the diffusion information exponent, in analogy to related invariants in different learning paradigms. Using this invariant, we prove that the denoiser learns simple, pair-wise statistics of the inputs at linear sample complexity, while more complex higher-order statistics, such as the fourth cumulant, require at least cubic sample complexity. We also prove that the sample complexity of learning the fourth cumulant is linear if pair-wise and higher-order statistics share a correlated latent structure. Our work describes a key mechanism for how diffusion models can learn distributions of increasing complexity.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12744v1",
    "title": "TaoBench: Do Automated Theorem Prover LLMs Generalize Beyond MathLib?",
    "submitted": "2026-03-13T07:39:47Z",
    "updated": "2026-03-13T07:39:47Z",
    "comment": "",
    "abstract": "Automated theorem proving (ATP) benchmarks largely consist of problems formalized in MathLib, so current ATP training and evaluation are heavily biased toward MathLib's definitional framework. However, frontier mathematics is often exploratory and prototype-heavy, relying on bespoke constructions that deviate from standard libraries. In this work, we evaluate the robustness of current ATP systems when applied to a novel definitional framework, specifically examining the performance gap between standard library problems and bespoke mathematical constructions. We introduce TaoBench, an undergraduate-level benchmark derived from Terence Tao's Analysis I, which formalizes analysis by constructing core mathematical concepts from scratch, without relying on standard Mathlib definitions, as well as by mixing from-scratch and MathLib constructions. For fair evaluation, we build an agentic pipeline that automatically extracts a compilable, self-contained local environment for each problem. To isolate the effect of definitional frameworks, we additionally translate every problem into a mathematically equivalent Mathlib formulation, yielding paired TaoBench-Mathlib statements for direct comparison. While state-of-the-art ATP models perform capably within the MathLib framework, performance drops by an average of roughly 26% on the definitionally equivalent Tao formulation. This indicates that the main bottleneck is limited generalization across definitional frameworks rather than task difficulty. TaoBench thus highlights a gap between benchmark performance and applicability, and provides a concrete foundation for developing and testing provers better aligned with research mathematics.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12740v1",
    "title": "ToolTree: Efficient LLM Agent Tool Planning via Dual-Feedback Monte Carlo Tree Search and Bidirectional Pruning",
    "submitted": "2026-03-13T07:37:06Z",
    "updated": "2026-03-13T07:37:06Z",
    "comment": "ICLR 2026",
    "abstract": "Large Language Model (LLM) agents are increasingly applied to complex, multi-step tasks that require interaction with diverse external tools across various domains. However, current LLM agent tool planning methods typically rely on greedy, reactive tool selection strategies that lack foresight and fail to account for inter-tool dependencies. In this paper, we present ToolTree, a novel Monte Carlo tree search-inspired planning paradigm for tool planning. ToolTree explores possible tool usage trajectories using a dual-stage LLM evaluation and bidirectional pruning mechanism that enables the agent to make informed, adaptive decisions over extended tool-use sequences while pruning less promising branches before and after the tool execution. Empirical evaluations across both open-set and closed-set tool planning tasks on 4 benchmarks demonstrate that ToolTree consistently improves performance while keeping the highest efficiency, achieving an average gain of around 10\\% compared to the state-of-the-art planning paradigm.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12707v1",
    "title": "Cost-Efficient Multimodal LLM Inference via Cross-Tier GPU Heterogeneity",
    "submitted": "2026-03-13T06:42:35Z",
    "updated": "2026-03-13T06:42:35Z",
    "comment": "",
    "abstract": "Multimodal large language model (MLLM) inference splits into two phases with opposing hardware demands: vision encoding is compute-bound, while language generation is memory-bandwidth-bound. We show that under standard transformer KV caching, the modality boundary (between vision encoder and language model) minimizes cross-device transfer among all partition points that preserve standard stage-based execution. Partitioning here reduces transfer complexity from $O(L * s_ctx)$ bytes (GB-scale KV caches under stage-level disaggregation) to $O(N_v * d)$ bytes (MB-scale embeddings), an O(L) reduction where L is the transformer depth. The result holds across attention mechanisms (MHA/GQA), dynamic vision resolutions, and model scales, and the advantage grows as models deepen. A direct implication is that existing stage-level disaggregation systems are constrained to high-bandwidth interconnects (e.g., NVLink), whereas modality-level disaggregation enables cross-tier heterogeneous serving over commodity PCIe. A closed-form cost model shows that heterogeneous deployment is cost-optimal under phase-separable workloads (predicts 31.4% savings; observed 40.6%). We build HeteroServe, a phase-aware runtime with modality-level partitioning and cross-tier scheduling, and evaluate it on LLaVA-1.5-7B and Qwen2.5-VL against vLLM v0.3.0. On identical 4xA100 hardware, engine optimizations raise throughput by up to 54%. Under a fixed budget, a heterogeneous cluster (\\$38k) improves Tokens/\\$ by 37% over a homogeneous baseline (\\$64k) without degrading latency.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12397v1",
    "title": "Not Just the Destination, But the Journey: Reasoning Traces Causally Shape Generalization Behaviors",
    "submitted": "2026-03-12T19:19:10Z",
    "updated": "2026-03-12T19:19:10Z",
    "comment": "",
    "abstract": "Chain-of-Thought (CoT) is often viewed as a window into LLM decision-making, yet recent work suggests it may function merely as post-hoc rationalization. This raises a critical alignment question: Does the reasoning trace causally shape model generalization independent of the final answer? To isolate reasoning's causal effect, we design a controlled experiment holding final harmful answers constant while varying reasoning paths. We construct datasets with \\textit{Evil} reasoning embracing malice, \\textit{Misleading} reasoning rationalizing harm, and \\textit{Submissive} reasoning yielding to pressure. We train models (0.6B--14B parameters) under multiple paradigms, including question-thinking-answer (QTA), question-thinking (QT), and thinking-only (T-only), and evaluate them in both think and no-think modes. We find that: (1) CoT training could amplify harmful generalization more than standard fine-tuning; (2) distinct reasoning types induce distinct behavioral patterns aligned with their semantics, despite identical final answers; (3) training on reasoning without answer supervision (QT or T-only) is sufficient to alter behavior, proving reasoning carries an independent signal; and (4) these effects persist even when generating answers without reasoning, indicating deep internalization. Our findings demonstrate that reasoning content is causally potent, challenging alignment strategies that supervise only outputs.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12350v1",
    "title": "TASTE-Streaming: Towards Streamable Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling",
    "submitted": "2026-03-12T18:13:48Z",
    "updated": "2026-03-12T18:13:48Z",
    "comment": "Work in progress",
    "abstract": "Text-speech joint spoken language modeling (SLM) aims at natural and intelligent speech-based interactions, but developing such a system may suffer from modality mismatch: speech unit sequences are much longer than text tokens. Prior work reduces this gap with text-aligned tokenization and embedding (TASTE), producing speech tokens that align in lengths with their textual counterparts. However, the dependence on an external ASR system and the use of a non-causal decoder limits streaming use. To address this limitation, we propose TASTE-S, a streamable extension of TASTE suitable for real-time usage. TASTE-S integrates a CTC-based ASR module into the encoder for instant dual-modality encoding. We also redesign the unit decoder to enable on-the-fly decoding. With joint training, we show that TASTE-S matches TASTE's performance while significantly reducing latency. Further investigations reveal that TASTE-S remains robust to transcriptions and enables long-form encoding and decoding.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.13215v1",
    "title": "Out of Sight, Out of Mind? Evaluating State Evolution in Video World Models",
    "submitted": "2026-03-13T17:51:14Z",
    "updated": "2026-03-13T17:51:14Z",
    "comment": "https://glab-caltech.github.io/STEVOBench/",
    "abstract": "Evolutions in the world, such as water pouring or ice melting, happen regardless of being observed. Video world models generate \"worlds\" via 2D frame observations. Can these generated \"worlds\" evolve regardless of observation? To probe this question, we design a benchmark to evaluate whether video world models can decouple state evolution from observation. Our benchmark, STEVO-Bench, applies observation control to evolving processes via instructions of occluder insertion, turning off the light, or specifying camera \"lookaway\" trajectories. By evaluating video models with and without camera control for a diverse set of naturally-occurring evolutions, we expose their limitations in decoupling state evolution from observation. STEVO-Bench proposes an evaluation protocol to automatically detect and disentangle failure modes of video world models across key aspects of natural state evolution. Analysis of STEVO-Bench results provide new insight into potential data and architecture bias of present-day video world models. Project website: https://glab-caltech.github.io/STEVOBench/. Blog: https://ziqi-ma.github.io/blog/2026/outofsight/",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12875v1",
    "title": "Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks",
    "submitted": "2026-03-13T10:24:19Z",
    "updated": "2026-03-13T10:24:19Z",
    "comment": "",
    "abstract": "Direct evaluation of LLMs on benchmarks can be misleading because comparatively strong performance may reflect task familiarity rather than capability. The train-before-test approach controls for task familiarity by giving each model task-relevant training before evaluation, originally through supervised finetuning. However, suitable training data is often hard to come by, and evaluation results vary with the data chosen. In this paper, we propose a two-stage test-time reinforcement learning (RL) alignment method for train-before-test. First, RL with a single sample provides a first alignment of the model to the task format, and second, test-time RL with majority-voting reward aligns the model to the benchmark distribution. Our test-time RL alignment method aligns similarly well as SFT-based train-before test, but without requiring a task-specific training set. On a domain-specific benchmark without training data, we show that direct evaluation underestimates base models which perform substantially better once aligned, yielding a more faithful evaluation of their capabilities. Moreover, for reasoning tasks, the performance gap between fine-tuned models and their base models largely disappears after alignment, suggesting that many gains from RLVR/SFT reported in the literature are not a difference in reasoning capability, but rather artifacts of task familiarity.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.13201v1",
    "title": "Neuron-Aware Data Selection In Instruction Tuning For Large Language Models",
    "submitted": "2026-03-13T17:39:03Z",
    "updated": "2026-03-13T17:39:03Z",
    "comment": "",
    "abstract": "Instruction Tuning (IT) has been proven to be an effective approach to unlock the powerful capabilities of large language models (LLMs). Recent studies indicate that excessive IT data can degrade LLMs performance, while carefully selecting a small subset of high-quality IT data can significantly enhance their capabilities. Therefore, identifying the most efficient subset data from the IT dataset to effectively develop either specific or general abilities in LLMs has become a critical challenge. To address this, we propose a novel and efficient framework called NAIT. NAIT evaluates the impact of IT data on LLMs performance by analyzing the similarity of neuron activation patterns between the IT dataset and the target domain capability. Specifically, NAIT captures neuron activation patterns from in-domain datasets of target domain capabilities to construct reusable and transferable neuron activation features. It then evaluates and selects optimal samples based on the similarity between candidate samples and the expected activation features of the target capabilities. Experimental results show that training on the 10\\% Alpaca-GPT4 IT data subset selected by NAIT consistently outperforms methods that rely on external advanced models or uncertainty-based features across various tasks. Our findings also reveal the transferability of neuron activation features across different capabilities of LLMs. In particular, IT data with more logical reasoning and programmatic features possesses strong general transferability, enabling models to develop stronger capabilities across multiple tasks, while a stable core subset of data is sufficient to consistently activate fundamental model capabilities and universally improve performance across diverse tasks.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.13189v1",
    "title": "LLM Constitutional Multi-Agent Governance",
    "submitted": "2026-03-13T17:21:26Z",
    "updated": "2026-03-13T17:21:26Z",
    "comment": "Accepted for publication in 20th International Conference on Agents and Multi-Agent Systems: Technologies and Applications (AMSTA 2026), to appear in Springer Nature proceedings (KES Smart Innovation Systems and Technologies). The final authenticated version will be available online at Springer",
    "abstract": "Large Language Models (LLMs) can generate persuasive influence strategies that shift cooperative behavior in multi-agent populations, but a critical question remains: does the resulting cooperation reflect genuine prosocial alignment, or does it mask erosion of agent autonomy, epistemic integrity, and distributional fairness? We introduce Constitutional Multi-Agent Governance (CMAG), a two-stage framework that interposes between an LLM policy compiler and a networked agent population, combining hard constraint filtering with soft penalized-utility optimization that balances cooperation potential against manipulation risk and autonomy pressure. We propose the Ethical Cooperation Score (ECS), a multiplicative composite of cooperation, autonomy, integrity, and fairness that penalizes cooperation achieved through manipulative means. In experiments on scale-free networks of 80 agents under adversarial conditions (70% violating candidates), we benchmark three regimes: full CMAG, naive filtering, and unconstrained optimization. While unconstrained optimization achieves the highest raw cooperation (0.873), it yields the lowest ECS (0.645) due to severe autonomy erosion (0.867) and fairness degradation (0.888). CMAG attains an ECS of 0.741, a 14.9% improvement, while preserving autonomy at 0.985 and integrity at 0.995, with only modest cooperation reduction to 0.770. The naive ablation (ECS = 0.733) confirms that hard constraints alone are insufficient. Pareto analysis shows CMAG dominates the cooperation-autonomy trade-off space, and governance reduces hub-periphery exposure disparities by over 60%. These findings establish that cooperation is not inherently desirable without governance: constitutional constraints are necessary to ensure that LLM-mediated influence produces ethically stable outcomes rather than manipulative equilibria.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12631v1",
    "title": "Collaborative Multi-Agent Optimization for Personalized Memory System",
    "submitted": "2026-03-13T04:04:17Z",
    "updated": "2026-03-13T04:04:17Z",
    "comment": "",
    "abstract": "Memory systems are crucial to personalized LLMs by mitigating the context window limitation in capturing long-term user-LLM conversations. Typically, such systems leverage multiple agents to handle multi-granular memory construction and personalized memory retrieval tasks. To optimize the system, existing methods focus on specializing agents on their local tasks independently via prompt engineering or fine-tuning. However, they overlook cross-agent collaboration, where independent optimization on local agents hardly guarantees the global system performance. To address this issue, we propose a Collaborative Reinforcement Learning Framework for Multi-Agent Memory Systems (CoMAM), jointly optimizing local agents to facilitate collaboration. Specifically, we regularize agents' execution as a sequential Markov decision process (MDP) to embed inter-agent dependencies into the state transition, yielding both local task rewards (e.g., information coverage for memory construction) and global rewards (i.e., query-answer accuracy). Then, we quantify each agent's contribution via group-level ranking consistency between local and global rewards, treating them as adaptive weights to assign global credit and integrate local-global rewards. Each agent is optimized by these integrated rewards, aligning local improvements with the global performance. Experiments show CoMAM outperforms leading memory systems, validating the efficacy of our proposed collaborative reinforcement learning for joint optimization.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12646v1",
    "title": "98$\\times$ Faster LLM Routing Without a Dedicated GPU: Flash Attention, Prompt Compression, and Near-Streaming for the vLLM Semantic Router",
    "submitted": "2026-03-13T04:33:53Z",
    "updated": "2026-03-13T04:33:53Z",
    "comment": "",
    "abstract": "System-level routers that intercept LLM requests for safety classification, domain routing, and PII detection must be both fast and operationally lightweight: they should add minimal latency to every request, yet not require a dedicated GPU -- an expensive resource better used for LLM inference itself. When the router co-locates on the same GPU as vLLM serving instances, standard attention's $O(n^2)$ memory makes long-context classification (8K--32K tokens) impossible: at 8K tokens, three concurrent classifiers need ${\\sim}$4.5\\,GB for attention masks alone, far exceeding the memory left by vLLM. We present three staged optimizations for the vLLM Semantic Router, benchmarked on AMD Instinct MI300X, that solve both the latency and the memory problem. \\emph{Stage~1}: a custom CK Flash Attention operator for ONNX Runtime on ROCm reduces attention memory from $O(n^2)$ to $O(n)$ and end-to-end (E2E) latency from 4{,}918\\,ms to 127\\,ms (\\textbf{38.7$\\times$}), enabling 8K--32K tokens where SDPA OOMs. \\emph{Stage~2}: classical NLP prompt compression (TextRank, position weighting, TF-IDF, and novelty scoring) reduces all inputs to ${\\sim}$512 tokens without neural inference, capping both latency and GPU memory at a constant regardless of original prompt length (E2E 127$\\to$62\\,ms, \\textbf{2.0$\\times$}). \\emph{Stage~3}: near-streaming body processing with adaptive chunking and zero-copy JSON eliminates serialization overhead (E2E 62$\\to$50\\,ms, \\textbf{1.2$\\times$}). Cumulatively: \\textbf{98$\\times$} improvement (4{,}918\\,ms to 50\\,ms), 16K-token routing in 108\\,ms, and a total router GPU footprint under 800\\,MB -- small enough to share a GPU with LLM serving and removing the need for a dedicated accelerator. Stage~1 targets AMD ROCm (NVIDIA GPUs already have FlashAttention via cuDNN); Stages~2 and~3 are hardware-agnostic.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12595v1",
    "title": "Swap-guided Preference Learning for Personalized Reinforcement Learning from Human Feedback",
    "submitted": "2026-03-13T02:51:50Z",
    "updated": "2026-03-13T02:51:50Z",
    "comment": "ICLR 2026",
    "abstract": "Reinforcement Learning from Human Feedback (RLHF) is a widely used approach to align large-scale AI systems with human values. However, RLHF typically assumes a single, universal reward, which overlooks diverse preferences and limits personalization. Variational Preference Learning (VPL) seeks to address this by introducing user-specific latent variables. Despite its promise, we found that VPL suffers from posterior collapse. While this phenomenon is well known in VAEs, it has not previously been identified in preference learning frameworks. Under sparse preference data and with overly expressive decoders, VPL may cause latent variables to be ignored, reverting to a single-reward model. To overcome this limitation, we propose Swap-guided Preference Learning (SPL). The key idea is to construct fictitious swap annotators and use the mirroring property of their preferences to guide the encoder. SPL introduces three components: (1) swap-guided base regularization, (2) Preferential Inverse Autoregressive Flow (P-IAF), and (3) adaptive latent conditioning. Experiments show that SPL mitigates collapse, enriches user-specific latents, and improves preference prediction. Our code and data are available at https://github.com/cobang0111/SPL",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12760v1",
    "title": "HIFICL: High-Fidelity In-Context Learning for Multimodal Tasks",
    "submitted": "2026-03-13T08:03:35Z",
    "updated": "2026-03-13T08:03:35Z",
    "comment": "Accepted to CVPR 2026. Code available at https://github.com/bbbandari/HiFICL",
    "abstract": "In-Context Learning (ICL) is a significant paradigm for Large Multimodal Models (LMMs), using a few in-context demonstrations (ICDs) for new task adaptation. However, its performance is sensitive to demonstration configurations and computationally expensive. Mathematically, the influence of these demonstrations can be decomposed into a dynamic mixture of the standard attention output and the context values. Current approximation methods simplify this process by learning a \"shift vector\". Inspired by the exact decomposition, we introduce High-Fidelity In-Context Learning (HIFICL) to more faithfully model the ICL mechanism. HIFICL consists of three key components: 1) a set of \"virtual key-value pairs\" to act as a learnable context, 2) a low-rank factorization for stable and regularized training, and 3) a simple end-to-end training objective. From another perspective, this mechanism constitutes a form of context-aware Parameter-Efficient Fine-Tuning (PEFT). Extensive experiments show that HiFICL consistently outperforms existing approximation methods on several multimodal benchmarks. The code is available at https://github.com/bbbandari/HiFICL.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.13176v1",
    "title": "Perceive What Matters: Relevance-Driven Scheduling for Multimodal Streaming Perception",
    "submitted": "2026-03-13T17:11:20Z",
    "updated": "2026-03-13T17:11:20Z",
    "comment": "Accepted to ICRA 2026",
    "abstract": "In modern human-robot collaboration (HRC) applications, multiple perception modules jointly extract visual, auditory, and contextual cues to achieve comprehensive scene understanding, enabling the robot to provide appropriate assistance to human agents intelligently. While executing multiple perception modules on a frame-by-frame basis enhances perception quality in offline settings, it inevitably accumulates latency, leading to a substantial decline in system performance in streaming perception scenarios. Recent work in scene understanding, termed Relevance, has established a solid foundation for developing efficient methodologies in HRC. However, modern perception pipelines still face challenges related to information redundancy and suboptimal allocation of computational resources. Drawing inspiration from the Relevance concept and the information sparsity in HRC events, we propose a novel lightweight perception scheduling framework that efficiently leverages output from previous frames to estimate and schedule necessary perception modules in real-time based on scene context. The experimental results demonstrate that the proposed perception scheduling framework effectively reduces computational latency by up to 27.52% compared to conventional parallel perception pipelines, while also achieving a 72.73% improvement in MMPose activation recall. Additionally, the framework demonstrates high keyframe accuracy, achieving rates of up to 98%. The results validate the framework's capability to enhance real-time perception efficiency without significantly compromising accuracy. The framework shows potential as a scalable and systematic solution for multimodal streaming perception systems in HRC.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.13085v1",
    "title": "Influence Malleability in Linearized Attention: Dual Implications of Non-Convergent NTK Dynamics",
    "submitted": "2026-03-13T15:33:34Z",
    "updated": "2026-03-13T15:33:34Z",
    "comment": "",
    "abstract": "Understanding the theoretical foundations of attention mechanisms remains challenging due to their complex, non-linear dynamics. This work reveals a fundamental trade-off in the learning dynamics of linearized attention. Using a linearized attention mechanism with exact correspondence to a data-dependent Gram-induced kernel, both empirical and theoretical analysis through the Neural Tangent Kernel (NTK) framework shows that linearized attention does not converge to its infinite-width NTK limit, even at large widths. A spectral amplification result establishes this formally: the attention transformation cubes the Gram matrix's condition number, requiring width $m = Ω(κ^6)$ for convergence, a threshold that exceeds any practical width for natural image datasets. This non-convergence is characterized through influence malleability, the capacity to dynamically alter reliance on training examples. Attention exhibits 6--9$\\times$ higher malleability than ReLU networks, with dual implications: its data-dependent kernel can reduce approximation error by aligning with task structure, but this same sensitivity increases susceptibility to adversarial manipulation of training data. These findings suggest that attention's power and vulnerability share a common origin in its departure from the kernel regime.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12368v1",
    "title": "Multi-Step Semantic Reasoning in Generative Retrieval",
    "submitted": "2026-03-12T18:38:50Z",
    "updated": "2026-03-12T18:38:50Z",
    "comment": "Accepted at ECIR2026",
    "abstract": "Generative retrieval (GR) models encode a corpus within model parameters and generate relevant document identifiers directly for a given query. While this paradigm shows promise in retrieval tasks, existing GR models struggle with complex queries in numerical contexts, such as those involving semantic reasoning over financial reports, due to limited reasoning capabilities. This limitation leads to suboptimal retrieval accuracy and hinders practical applicability. We propose ReasonGR, a framework designed to enhance multi-step semantic reasoning in numerical contexts within GR. ReasonGR employs a structured prompting strategy combining task-specific instructions with stepwise reasoning guidance to better address complex retrieval queries. Additionally, it integrates a reasoning-focused adaptation module to improve the learning of reasoning-related parameters. Experiments on the FinQA dataset, which contains financial queries over complex documents, demonstrate that ReasonGR improves retrieval accuracy and consistency, indicating its potential for advancing GR models in reasoning-intensive retrieval scenarios.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12634v1",
    "title": "Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents",
    "submitted": "2026-03-13T04:10:27Z",
    "updated": "2026-03-13T04:10:27Z",
    "comment": "",
    "abstract": "Test-time scaling has become a dominant paradigm for improving LLM agent reliability, yet current approaches treat compute as an abundant resource, allowing agents to exhaust token and tool budgets on redundant steps or dead-end trajectories. Existing budget-aware methods either require expensive fine-tuning or rely on coarse, trajectory-level heuristics that cannot intervene mid-execution. We propose the Budget-Aware Value Tree (BAVT), a training-free inference-time framework that models multi-hop reasoning as a dynamic search tree guided by step-level value estimation within a single LLM backbone. Another key innovation is a budget-conditioned node selection mechanism that uses the remaining resource ratio as a natural scaling exponent over node values, providing a principled, parameter-free transition from broad exploration to greedy exploitation as the budget depletes. To combat the well-known overconfidence of LLM self-evaluation, BAVT employs a residual value predictor that scores relative progress rather than absolute state quality, enabling reliable pruning of uninformative or redundant tool calls. We further provide a theoretical convergence guarantee, proving that BAVT reaches a terminal answer with probability at least $1-ε$ under an explicit finite budget bound. Extensive evaluations on four multi-hop QA benchmarks across two model families demonstrate that BAVT consistently outperforms parallel sampling baselines. Most notably, BAVT under strict low-budget constraints surpasses baseline performance at $4\\times$ the resource allocation, establishing that intelligent budget management fundamentally outperforms brute-force compute scaling.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.13017v1",
    "title": "Structured Distillation for Personalized Agent Memory: 11x Token Reduction with Retrieval Preservation",
    "submitted": "2026-03-13T14:21:58Z",
    "updated": "2026-03-13T14:21:58Z",
    "comment": "6 figures. Code: https://github.com/Process-Point-Technologies-Corporation/searchat",
    "abstract": "Long conversations with an AI agent create a simple problem for one user: the history is useful, but carrying it verbatim is expensive. We study personalized agent memory: one user's conversation history with an agent, distilled into a compact retrieval layer for later search. Each exchange is compressed into a compound object with four fields (exchange_core, specific_context, thematic room_assignments, and regex-extracted files_touched). The searchable distilled text averages 38 tokens per exchange. Applied to 4,182 conversations (14,340 exchanges) from 6 software engineering projects, the method reduces average exchange length from 371 to 38 tokens, yielding 11x compression. We evaluate whether personalized recall survives that compression using 201 recall-oriented queries, 107 configurations spanning 5 pure and 5 cross-layer search modes, and 5 LLM graders (214,519 consensus-graded query-result pairs). The best pure distilled configuration reaches 96% of the best verbatim MRR (0.717 vs 0.745). Results are mechanism-dependent. All 20 vector search configurations remain non-significant after Bonferroni correction, while all 20 BM25 configurations degrade significantly (effect sizes |d|=0.031-0.756). The best cross-layer setup slightly exceeds the best pure verbatim baseline (MRR 0.759). Structured distillation compresses single-user agent memory without uniformly sacrificing retrieval quality. At 1/11 the context cost, thousands of exchanges fit within a single prompt while the verbatim source remains available for drill-down. We release the implementation and analysis pipeline as open-source software.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12554v1",
    "title": "Reinforcement Learning for Diffusion LLMs with Entropy-Guided Step Selection and Stepwise Advantages",
    "submitted": "2026-03-13T01:38:44Z",
    "updated": "2026-03-13T01:38:44Z",
    "comment": "",
    "abstract": "Reinforcement learning (RL) has been effective for post-training autoregressive (AR) language models, but extending these methods to diffusion language models (DLMs) is challenging due to intractable sequence-level likelihoods. Existing approaches therefore rely on surrogate likelihoods or heuristic approximations, which can introduce bias and obscure the sequential structure of denoising. We formulate diffusion-based sequence generation as a finite-horizon Markov decision process over the denoising trajectory and derive an exact, unbiased policy gradient that decomposes over denoising steps and is expressed in terms of intermediate advantages, without requiring explicit evaluation of the sequence likelihood. To obtain a practical and compute-efficient estimator, we (i) select denoising steps for policy updates via an entropy-guided approximation bound, and (ii) estimate intermediate advantages using a one-step denoising reward naturally provided by the diffusion model, avoiding costly multi-step rollouts. Experiments on coding and logical reasoning benchmarks demonstrate state-of-the-art results, with strong competitive performance on mathematical reasoning, outperforming existing RL post-training approaches for DLMs. Code is available at https://github.com/vishnutez/egspo-dllm-rl.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12996v1",
    "title": "Dependency-Aware Parallel Decoding via Attention for Diffusion LLMs",
    "submitted": "2026-03-13T13:52:02Z",
    "updated": "2026-03-13T13:52:02Z",
    "comment": "",
    "abstract": "Parallel decoding for diffusion LLMs (dLLMs) is difficult because each denoising step provides only token-wise marginal distributions, while unmasking multiple tokens simultaneously requires accounting for inter-token dependencies. We propose Dependency-Aware Parallel Decoding (DAPD), a simple, training-free decoding method that uses self-attention to induce a conditional dependency graph over masked tokens. At each iteration, edges in this graph capture strong token interactions, while non-edges indicate weak dependence. Parallel decoding is then reduced to selecting an independent set on the graph and unmasking the selected tokens in parallel. This avoids co-updating strongly coupled tokens without auxiliary models or retraining. Experiments on LLaDA and Dream show that DAPD improves the accuracy-steps trade-off over existing methods and enables more globally distributed parallel updates that better exploit the any-order generation capability of dLLMs.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12541v1",
    "title": "As Language Models Scale, Low-order Linear Depth Dynamics Emerge",
    "submitted": "2026-03-13T00:51:53Z",
    "updated": "2026-03-13T00:51:53Z",
    "comment": "",
    "abstract": "Large language models are often viewed as high-dimensional nonlinear systems and treated as black boxes. Here, we show that transformer depth dynamics admit accurate low-order linear surrogates within context. Across tasks including toxicity, irony, hate speech and sentiment, a 32-dimensional linear surrogate reproduces the layerwise sensitivity profile of GPT-2-large with near-perfect agreement, capturing how the final output shifts under additive injections at each layer. We then uncover a surprising scaling principle: for a fixed-order linear surrogate, agreement with the full model improves monotonically with model size across the GPT-2 family. This linear surrogate also enables principled multi-layer interventions that require less energy than standard heuristic schedules when applied to the full model. Together, our results reveal that as language models scale, low-order linear depth dynamics emerge within contexts, offering a systems-theoretic foundation for analyzing and controlling them.",
    "request_suffix": "v1"
  },
  {
    "id": "http://arxiv.org/abs/2603.12744v1",
    "title": "TaoBench: Do Automated Theorem Prover LLMs Generalize Beyond MathLib?",
    "submitted": "2026-03-13T07:39:47Z",
    "updated": "2026-03-13T07:39:47Z",
    "comment": "",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.12740v1",
    "title": "ToolTree: Efficient LLM Agent Tool Planning via Dual-Feedback Monte Carlo Tree Search and Bidirectional Pruning",
    "submitted": "2026-03-13T07:37:06Z",
    "updated": "2026-03-13T07:37:06Z",
    "comment": "ICLR 2026",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.12707v1",
    "title": "Cost-Efficient Multimodal LLM Inference via Cross-Tier GPU Heterogeneity",
    "submitted": "2026-03-13T06:42:35Z",
    "updated": "2026-03-13T06:42:35Z",
    "comment": "",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.12397v1",
    "title": "Not Just the Destination, But the Journey: Reasoning Traces Causally Shape Generalization Behaviors",
    "submitted": "2026-03-12T19:19:10Z",
    "updated": "2026-03-12T19:19:10Z",
    "comment": "",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.12350v1",
    "title": "TASTE-Streaming: Towards Streamable Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling",
    "submitted": "2026-03-12T18:13:48Z",
    "updated": "2026-03-12T18:13:48Z",
    "comment": "Work in progress",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.13215v1",
    "title": "Out of Sight, Out of Mind? Evaluating State Evolution in Video World Models",
    "submitted": "2026-03-13T17:51:14Z",
    "updated": "2026-03-13T17:51:14Z",
    "comment": "https://glab-caltech.github.io/STEVOBench/",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.12875v1",
    "title": "Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks",
    "submitted": "2026-03-13T10:24:19Z",
    "updated": "2026-03-13T10:24:19Z",
    "comment": "",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.13201v1",
    "title": "Neuron-Aware Data Selection In Instruction Tuning For Large Language Models",
    "submitted": "2026-03-13T17:39:03Z",
    "updated": "2026-03-13T17:39:03Z",
    "comment": "",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.13189v1",
    "title": "LLM Constitutional Multi-Agent Governance",
    "submitted": "2026-03-13T17:21:26Z",
    "updated": "2026-03-13T17:21:26Z",
    "comment": "Accepted for publication in 20th International Conference on Agents and Multi-Agent Systems: Technologies and Applications (AMSTA 2026), to appear in Springer Nature proceedings (KES Smart Innovation Systems and Technologies). The final authenticated version will be available online at Springer",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.12646v1",
    "title": "98$\\times$ Faster LLM Routing Without a Dedicated GPU: Flash Attention, Prompt Compression, and Near-Streaming for the vLLM Semantic Router",
    "submitted": "2026-03-13T04:33:53Z",
    "updated": "2026-03-13T04:33:53Z",
    "comment": "",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.12595v1",
    "title": "Swap-guided Preference Learning for Personalized Reinforcement Learning from Human Feedback",
    "submitted": "2026-03-13T02:51:50Z",
    "updated": "2026-03-13T02:51:50Z",
    "comment": "ICLR 2026",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.12554v2",
    "title": "Reinforcement Learning for Diffusion LLMs with Entropy-Guided Step Selection and Stepwise Advantages",
    "submitted": "2026-03-13T01:38:44Z",
    "updated": "2026-05-14T15:00:13Z",
    "comment": "",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.12996v2",
    "title": "DAPD: Dependency-Aware Parallel Decoding via Attention for Diffusion LLMs",
    "submitted": "2026-03-13T13:52:02Z",
    "updated": "2026-06-01T14:39:20Z",
    "comment": "Accepted at ICML 2026",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.13085v2",
    "title": "Linearized Attention Cannot Enter the Kernel Regime at Any Practical Width",
    "submitted": "2026-03-13T15:33:34Z",
    "updated": "2026-05-07T12:38:25Z",
    "comment": "",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.13176v1",
    "title": "Perceive What Matters: Relevance-Driven Scheduling for Multimodal Streaming Perception",
    "submitted": "2026-03-13T17:11:20Z",
    "updated": "2026-03-13T17:11:20Z",
    "comment": "Accepted to ICRA 2026",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.12901v2",
    "title": "A theory of learning data statistics in diffusion models, from easy to hard",
    "submitted": "2026-03-13T11:07:01Z",
    "updated": "2026-06-10T13:28:42Z",
    "comment": "",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.12368v1",
    "title": "Multi-Step Semantic Reasoning in Generative Retrieval",
    "submitted": "2026-03-12T18:38:50Z",
    "updated": "2026-03-12T18:38:50Z",
    "comment": "Accepted at ECIR2026",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.12634v1",
    "title": "Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents",
    "submitted": "2026-03-13T04:10:27Z",
    "updated": "2026-03-13T04:10:27Z",
    "comment": "",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.13017v1",
    "title": "Structured Distillation for Personalized Agent Memory: 11x Token Reduction with Retrieval Preservation",
    "submitted": "2026-03-13T14:21:58Z",
    "updated": "2026-03-13T14:21:58Z",
    "comment": "6 figures. Code: https://github.com/Process-Point-Technologies-Corporation/searchat",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.12631v2",
    "title": "Joint Optimization of Multi-agent Memory System",
    "submitted": "2026-03-13T04:04:17Z",
    "updated": "2026-04-27T03:20:35Z",
    "comment": "",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.12541v1",
    "title": "As Language Models Scale, Low-order Linear Depth Dynamics Emerge",
    "submitted": "2026-03-13T00:51:53Z",
    "updated": "2026-03-13T00:51:53Z",
    "comment": "",
    "request_suffix": ""
  },
  {
    "id": "http://arxiv.org/abs/2603.12760v4",
    "title": "HIFICL: High-Fidelity In-Context Learning for Multimodal Tasks",
    "submitted": "2026-03-13T08:03:35Z",
    "updated": "2026-03-27T14:36:57Z",
    "comment": "Accepted to CVPR 2026. Code available at https://github.com/bbbandari/HiFICL",
    "request_suffix": ""
  }
]
```
