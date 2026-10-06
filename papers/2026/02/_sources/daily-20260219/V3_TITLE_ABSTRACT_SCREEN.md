# 2026-02-19 V3 主线题名查漏后的完整题摘

旧 364 身份宽 inventory 仅作题名查漏；按模型表示/架构/优化、训练/后训练、生成、GPU运行时、评估与Agent机制选择下列99份完整题摘，未把全部宽列表变队列。以下全部本轮已读；字段来自旧身份记录，摘要可能已随后版更新，**下方v1仅标本窗事件身份，不代表摘要是v1快照**。15195实际v1与当前v3题摘有实质差异，故后版摘要仅用于发现；准入及证据须回到[精确v1题摘](V3_EXACT_V1_ABSTRACTS.json)与原文。当前官方 API 只轻查修订/撤回信号，不将 Published 当公开时刻。

必要日期逐家族核验：官方 availability 说明 identifier/DOI 只在announcement时赋值，Monday14ET～Tuesday14ET 的提交最早 Tuesday20ET 公告。Submitted:v1 晚于2026-02-16T19:00Z且不晚于2026-02-17T19:00Z的家族，其首次arXiv公开下界为2026-02-18T01:00Z；同身份DataCite Created/Registered在2026-02-19T01:00Z之前提供上界。两者共同限定落窗，不借Updated、相邻ID或月归档。早Submitted或注册上界跨截止仍日期保留；更早作者公开线索须定点核去重。

## 2602.15037v1 — CircuChain: Disentangling Competence and Compliance in LLM Circuit Analysis

原始链接：https://arxiv.org/abs/2602.15037v1

Submitted UTC：2026-01-29T06:13:44Z；DOI Created UTC：2026-02-18T02:32:15Z。

As large language models (LLMs) advance toward expert-level performance in engineering domains, reliable reasoning under user-specified constraints becomes critical. In circuit analysis, for example, a numerically correct solution is insufficient if it violates established methodological conventions such as mesh directionality or polarity assignments, errors that can propagate in safety-critical systems. Yet it remains unclear whether frontier models truly apply first-principles reasoning or rely on entrenched training priors that conflict with explicit instructions. We introduce CircuChain, a diagnostic benchmark designed to disentangle instruction compliance from physical reasoning competence in electrical circuit analysis. CircuChain consists of counterbalanced Control/Trap problem pairs across five canonical circuit topologies, augmented with systematic variations in sign conventions, current orientations, and polarity definitions. A multi-stage verification pipeline, combining symbolic solvers, SPICE simulation, and an LLM-based error taxonomy, enables fine-grained attribution of failures to convention errors, physics errors, arithmetic mistakes, or hallucinations. Across 100 tasks per model, we observe a consistent Compliance-Competence Divergence. The strongest model evaluated exhibits near-perfect physical reasoning but a high rate of convention violations when Trap conditions deliberately invert natural sign patterns. Conversely, weaker models display lower physical fidelity yet superior adherence to explicit instructions. These results suggest that increased model capability does not guarantee improved constraint alignment and highlight the need for new evaluation frameworks that stress instruction-following under mathematically rigid domains. CircuChain provides one such framework and offers actionable insights for both engineering education and AI alignment research.

## 2602.15055v1 — Beyond Context Sharing: A Unified Agent Communication Protocol (ACP) for Secure, Federated, and Autonomous Agent-to-Agent (A2A) Orchestration

原始链接：https://arxiv.org/abs/2602.15055v1

Submitted UTC：2026-02-11T17:02:12Z；DOI Created UTC：2026-02-18T02:32:40Z。

In the artificial intelligence space, as we transition from isolated large language models to autonomous agents capable of complex reasoning and tool use. While foundational architectures and local context management protocols have been established, the challenge of cross-platform, decentralized, and secure interaction remains a significant barrier to the realization of a truly Agentic Web. Building upon the foundations of AI agent architectures and the Model Context Protocol (MCP) for multi-agent coordination, this paper introduces the Agent Communication Protocol (ACP). ACP provides a standardized framework for Agent-to-Agent (AA) interaction, enabling heterogeneous agents to discover, negotiate, and execute collaborative workflows across disparate environments. We propose a federated orchestration model that integrates decentralized identity verification, semantic intent mapping, and automated service-level agreements. Our evaluation demonstrates that ACP reduces inter-agent communication latency by % while maintaining a zero-trust security posture. This work represents a critical advancement toward a scalable and interoperable ecosystem of autonomous digital entities

## 2602.15112v1 — ResearchGym: Evaluating Language Model Agents on Real-World AI Research

原始链接：https://arxiv.org/abs/2602.15112v1

Submitted UTC：2026-02-16T19:00:03Z；DOI Created UTC：2026-02-18T02:33:59Z。

We introduce ResearchGym, a benchmark and execution environment for evaluating AI agents on end-to-end research. To instantiate this, we repurpose five oral and spotlight papers from ICML, ICLR, and ACL. From each paper's repository, we preserve the datasets, evaluation harness, and baseline implementations but withhold the paper's proposed method. This results in five containerized task environments comprising 39 sub-tasks in total. Within each environment, agents must propose novel hypotheses, run experiments, and attempt to surpass strong human baselines on the paper's metrics. In a controlled evaluation of an agent powered by GPT-5, we observe a sharp capability--reliability gap. The agent improves over the provided baselines from the repository in just 1 of 15 evaluations (6.7%) by 11.5%, and completes only 26.5% of sub-tasks on average. We identify recurring long-horizon failure modes, including impatience, poor time and resource management, overconfidence in weak hypotheses, difficulty coordinating parallel experiments, and hard limits from context length. Yet in a single run, the agent surpasses the solution of an ICML 2025 Spotlight task, indicating that frontier agents can occasionally reach state-of-the-art performance, but do so unreliably. We additionally evaluate proprietary agent scaffolds including Claude Code (Opus-4.5) and Codex (GPT-5.2) which display a similar gap. ResearchGym provides infrastructure for systematic evaluation and analysis of autonomous agents on closed-loop research.

## 2602.15143v1 — Protecting Language Models Against Unauthorized Distillation through Trace Rewriting

原始链接：https://arxiv.org/abs/2602.15143v1

Submitted UTC：2026-02-16T19:40:07Z；DOI Created UTC：2026-02-18T02:34:42Z。

Knowledge distillation is a widely adopted technique for transferring capabilities from LLMs to smaller, more efficient student models. However, unauthorized use of knowledge distillation takes unfair advantage of the considerable effort and cost put into developing frontier models. We investigate methods for modifying teacher-generated reasoning traces to achieve two objectives that deter unauthorized distillation: (1) \emph{anti-distillation}, or degrading the training usefulness of query responses, and (2) \emph{API watermarking}, which embeds verifiable signatures in student models. We introduce several approaches for dynamically rewriting a teacher's reasoning outputs while preserving answer correctness and semantic coherence. Two of these leverage the rewriting capabilities of LLMs, while others use gradient-based techniques. Our experiments show that a simple instruction-based rewriting approach achieves a strong anti-distillation effect while maintaining or even improving teacher performance. Furthermore, we show that our rewriting approach also enables embedding watermarks that can be reliably detected with essentially no false alarms. Our code is available at https://github.com/xhOwenMa/trace-rewriting.

## 2602.15156v1 — Panini: Continual Learning in Token Space via Structured Memory

原始链接：https://arxiv.org/abs/2602.15156v1

Submitted UTC：2026-02-16T19:58:03Z；DOI Created UTC：2026-02-18T02:35:00Z。

Language models are increasingly used to reason over content they were not trained on, such as new documents, evolving knowledge, and user-specific data. A common approach is retrieval-augmented generation (RAG), which stores verbatim documents externally (as chunks) and retrieves only a relevant subset at inference time for an LLM to reason over. However, this results in inefficient usage of test-time compute (LLM repeatedly reasons over the same documents); moreover, chunk retrieval can inject irrelevant context that increases unsupported generation. We propose a human-like non-parametric continual learning framework, where the base model remains fixed, and learning occurs by integrating each new experience into an external semantic memory state that accumulates and consolidates itself continually. We present Panini, which realizes this by representing documents as Generative Semantic Workspaces (GSW) -- an entity- and event-aware network of question-answer (QA) pairs, sufficient for an LLM to reconstruct the experienced situations and mine latent knowledge via reasoning-grounded inference chains on the network. Given a query, Panini only traverses the continually-updated GSW (not the verbatim documents or chunks), and retrieves the most likely inference chains. Across six QA benchmarks, Panini achieves the highest average performance, 5%-7% higher than other competitive baselines, while using 2-30x fewer answer-context tokens, supports fully open-source pipelines, and reduces unsupported answers on curated unanswerable queries. The results show that efficient and accurate structuring of experiences at write time -- as achieved by the GSW framework -- yields both efficiency and reliability gains at read time. Code is available at https://github.com/roychowdhuryresearch/gsw-memory.

## 2602.15166v1 — Fast and Fusiest: An Optimal Fusion-Aware Mapper for Accelerator Design

原始链接：https://arxiv.org/abs/2602.15166v1

Submitted UTC：2026-02-16T20:08:51Z；DOI Created UTC：2026-02-18T02:35:14Z。

A low-latency and energy-efficient tensor algebra accelerator design must optimize how data movement and operations are scheduled (i.e., mapped) in the accelerator architecture. A key mapping optimization is fusion, meaning holding data on-chip between computation steps in the workload, which has been shown to reduce energy and latency by reducing expensive off-chip data movement. However, the optimal fusion choice depends on the workload and workload shape, and a mapper, which searches for the optimal mapping, can improve energy and latency significantly. However, prior mappers cannot find optimal mappings with fusion (i.e., fused mappings) in a feasible runtime because the number of fused mappings to search increases exponentially with the number of computation steps in the workload.
 In this paper, we introduce the Fast and Fusiest Mapper (FFM), a mapper to quickly find optimal mappings in a comprehensive fused mapspace for tensor algebra workloads. FFM shrinks the search space by pruning subsets of mappings (i.e., partial mappings) that are shown to never be a part of optimal mappings, quickly eliminating all suboptimal mappings containing those partial mappings. Then FFM joins partial mappings to construct optimal fused mappings. Using FFM, we demonstrate an energy-delay-product (EDP) reduction by up to $1.8\times$ compared to TransFusion, a state-of-the-art accelerator with hand-optimized fusion. Moreover, we show that FFM finds mappings orders of magnitude faster ($&gt;10,000\times$) than prior automated mappers TileFlow and SET, and given the same runtime, reduces EDP by $&gt;2\times$.

## 2602.15172v1 — The Turbo-Charged Mapper: Fast and Optimal Mapping for Energy-efficient and Low-latency Accelerator Design

原始链接：https://arxiv.org/abs/2602.15172v1

Submitted UTC：2026-02-16T20:21:40Z；DOI Created UTC：2026-02-18T02:35:22Z。

The energy and latency of an accelerator running a deep neural network (DNN) depend on how the computation and data movement are scheduled in the accelerator (i.e., mapping), and picking an optimal mapping is essential to achieve high-performance accelerators. However, it is challenging to find mappings that maximize accelerator performance. The space of mappings is large, and prior works cannot guarantee finding optimal mappings because they use heuristics or metaheuristics to narrow the search space.
 To address this challenge, we propose the Turbo-Charged Mapper (TCM), a fast mapper that finds optimal mappings. The key to our approach is that we define a new mapping concept called dataplacement, which, like the prior concept of dataflow, allows for clear analysis and comparison of mappings. Through it, we identify opportunities to prune redundant and suboptimal mappings, reducing search space by up to 32 orders of magnitude ($10^{37}\rightarrow10^5$).
 TCM leverages these insights to perform full mapspace searches, making it the first mapper that can find optimal mappings in feasible runtime. Compared to prior mappers, TCM improves accelerator energy-delay-product by $1.2-6.5\times$ while simultaneously reducing mapping search time by $1000\times$ (5 hours $\rightarrow$ 17 seconds).

## 2602.15173v1 — Mind the (DH) Gap! A Contrast in Risky Choices Between Reasoning and Conversational LLMs

原始链接：https://arxiv.org/abs/2602.15173v1

Submitted UTC：2026-02-16T20:24:54Z；DOI Created UTC：2026-02-18T02:35:24Z。

The use of large language models either as decision support systems, or in agentic workflows, is rapidly transforming the digital ecosystem. However, the understanding of LLM decision-making under uncertainty remains limited. We study LLM risky choices along two dimensions: (1) prospect representation (based on an explicit representation or outcome history) and (2) decision rationale (explanation). Our study, which involves 20 frontier and open LLMs, is complemented by a matched human subjects experiment, which provides one reference point, while an expected payoff maximizing rational agent model provides another. We find that LLMs cluster into two categories: reasoning models (RMs) and conversational models (CMs). RMs tend towards rational behavior, are insensitive to the order of prospects, gain/loss framing, and explanations, and behave similarly whether prospects are explicit or presented via a history of outcomes. CMs are significantly less rational, slightly more human-like, sensitive to prospect ordering, framing, and explanation, and exhibit a large description-history gap. Paired comparisons of open LLMs suggest that a key factor differentiating RMs and CMs is training for mathematical reasoning.

## 2602.15183v1 — Seeing to Generalize: How Visual Data Corrects Binding Shortcuts

原始链接：https://arxiv.org/abs/2602.15183v1

Submitted UTC：2026-02-16T20:43:12Z；DOI Created UTC：2026-02-18T02:35:38Z。

Vision Language Models (VLMs) are designed to extend Large Language Models (LLMs) with visual capabilities, yet in this work we observe a surprising phenomenon: VLMs can outperform their underlying LLMs on purely text-only tasks, particularly in long-context information retrieval. To investigate this effect, we build a controlled synthetic retrieval task and find that a transformer trained only on text achieves perfect in-distribution accuracy but fails to generalize out of distribution, while subsequent training on an image-tokenized version of the same task nearly doubles text-only OOD performance. Mechanistic interpretability reveals that visual training changes the model's internal binding strategy: text-only training encourages positional shortcuts, whereas image-based training disrupts them through spatial translation invariance, forcing the model to adopt a more robust symbolic binding mechanism that persists even after text-only examples are reintroduced. We further characterize how binding strategies vary across training regimes, visual encoders, and initializations, and show that analogous shifts occur during pretrained LLM-to-VLM transitions. Our findings suggest that cross-modal training can enhance reasoning and generalization even for tasks grounded in a single modality.

## 2602.15189v1 — ScrapeGraphAI-100k: Dataset for Schema-Constrained LLM Generation

原始链接：https://arxiv.org/abs/2602.15189v1

Submitted UTC：2026-02-16T20:56:59Z；DOI Created UTC：2026-02-18T02:35:47Z。

Producing output that conforms to a specified JSON schema underlies tool use, structured extraction, and knowledge base construction in modern large language models. Despite this centrality, public datasets for the task remain small, synthetic, or text-only, and rarely pair real page content with the prompts and schemas used in practice. We introduce ScrapeGraphAI-100k, 93,695 schema-constrained extraction events collected via opt-in ScrapeGraphAI telemetry in Q2--Q3 2025, deduplicated and balanced by schema from 9M raw events. The corpus spans 18 000+ unique schemas across 15 named languages plus a long-tail Other category, with English and Traditional Chinese covering 88% of detected content, each instance pairs Markdown-converted page content with a prompt, schema, LLM response, and per-example jsonschema-rs structural conformance labels (semantic correctness is out of scope, and raw HTML is deferred beyond v1.0). We characterize structural diversity across the corpus and identify sharp failure thresholds as schema complexity grows. As a case study, a 1.7B student fine-tuned on this data closely tracks the output distribution of its GPT-5-nano teacher, though it still trails a 30B-A3B reference (3.3B active parameters) on schema compliance. We offer this distillation result as preliminary evidence that grounding schema-constrained generation in real practitioner workloads at scale enables training and benchmarking that prior synthetic or text-only corpora could not support.

## 2602.15195v1 — Weight space Detection of Backdoors in LoRA Adapters

原始链接：https://arxiv.org/abs/2602.15195v1

Submitted UTC：2026-02-16T21:20:47Z；DOI Created UTC：2026-02-18T02:35:55Z。

LoRA adapters let users fine-tune large language models (LLMs) efficiently. However, LoRA adapters are shared through open repositories like Hugging Face Hub \citep{huggingface_hub_docs}, making them vulnerable to backdoor attacks. Current detection methods require running the model with test input data -- making them impractical for screening thousands of adapters where the trigger for backdoor behavior is unknown. We detect poisoned adapters by analyzing their weight matrices directly, without running the model -- making our method trigger-agnostic. For each attention projection (Q, K, V, O), our method extracts five spectral statistics from the low-rank update $ΔW$, yielding a 20-dimensional signature for each adapter. A logistic regression detector trained on this representation separates benign and poisoned adapters across three model families -- Llama-3.2-3B~\citep{llama3}, Qwen2.5-3B~\citep{qwen25}, and Gemma-2-2B~\citep{gemma2} -- on unseen test adapters drawn from instruction-following, reasoning, question-answering, code, and classification tasks. Across all three architectures, the detector achieves 100\% accuracy.

## 2602.15197v1 — OpaqueToolsBench: Learning Nuances of Tool Behavior Through Interaction

原始链接：https://arxiv.org/abs/2602.15197v1

Submitted UTC：2026-02-16T21:26:37Z；DOI Created UTC：2026-02-18T02:35:57Z。

Tool-calling is essential for Large Language Model (LLM) agents to complete real-world tasks. While most existing benchmarks assume simple, perfectly documented tools, real-world tools (e.g., general "search" APIs) are often opaque, lacking clear best practices or failure modes. Can LLM agents improve their performance in environments with opaque tools by interacting and subsequently improving documentation? To study this, we create OpaqueToolsBench, a benchmark consisting of three distinct task-oriented environments: general function calling, interactive chess playing, and long-trajectory agentic search. Each environment provides underspecified tools that models must learn to use effectively to complete the task. Results on OpaqueToolsBench suggest existing methods for automatically documenting tools are expensive and unreliable when tools are opaque. To address this, we propose a simple framework, ToolObserver, that iteratively refines tool documentation by observing execution feedback from tool-calling trajectories. Our approach outperforms existing methods on OpaqueToolsBench across datasets, even in relatively hard settings. Furthermore, for test-time tool exploration settings, our method is also efficient, consuming 3.5-7.5x fewer total tokens than the best baseline.

## 2602.15198v1 — Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems

原始链接：https://arxiv.org/abs/2602.15198v1

Submitted UTC：2026-02-16T21:27:38Z；DOI Created UTC：2026-02-18T02:35:59Z。

Multi-agent systems, where LLM agents communicate through free-form language, enable sophisticated coordination for solving complex cooperative tasks. This surfaces a unique safety problem when a group of agents forms a coalition and colludes to pursue secondary goals and degrade the joint objective. In this paper, we present Colosseum, a framework for auditing LLM agents' collusive behavior in multi-agent settings. We ground how agents cooperate through a formal multi-agent decision-making framework and measure action-based collusive behavior in actions via regret relative to the cooperative optimum and compare it with communication-based collusive behavior. Colosseum enables audits of LLM agents for collusion under benign settings, different coalition objectives, persuasion tactics, and network topologies. We then introduce a new behavioral probe by creating secret communication channels between agents, showing that most out-of-the-box models exhibit a propensity to collude under this probe, which we term emergent collusion. Furthermore, we discover ``collusion on paper'' when agents plan to collude in text but often pick non-collusive actions. Colosseum provides a new way to audit collusion in cooperative multi-agent systems while presenting observations about how collusion emerges, what affects collusion efficacy, and which strategies may mitigate it.

## 2602.15200v1 — COMPOT: Calibration-Optimized Matrix Procrustes Orthogonalization for Transformers Compression

原始链接：https://arxiv.org/abs/2602.15200v1

Submitted UTC：2026-02-16T21:31:34Z；DOI Created UTC：2026-02-18T02:36:02Z。

Post-training compression of Transformer models commonly relies on truncated singular value decomposition (SVD). However, enforcing a single shared subspace can degrade accuracy even at moderate compression. Sparse dictionary learning provides a more flexible union-of-subspaces representation, but existing approaches often suffer from iterative dictionary and coefficient updates. We propose COMPOT (Calibration-Optimized Matrix Procrustes Orthogonalization for Transformers), a training-free compression framework that uses a small calibration dataset to estimate a sparse weight factorization. COMPOT employs orthogonal dictionaries that enable closed-form Procrustes updates for the dictionary and analytical single-step sparse coding for the coefficients, eliminating iterative optimization. To handle heterogeneous layer sensitivity under a global compression budget, COMPOT further introduces a one-shot dynamic allocation strategy that adaptively redistributes layer-wise compression rates. Extensive experiments across diverse architectures and tasks show that COMPOT consistently delivers a superior quality-compression trade-off over strong low-rank and sparse baselines, while remaining fully compatible with post-training quantization for extreme compression. Code is available $\href{https://github.com/mts-ai/COMPOT}{here}$.

## 2602.15206v1 — MAVRL: Learning Reward Functions from Multiple Feedback Types with Amortized Variational Inference

原始链接：https://arxiv.org/abs/2602.15206v1

Submitted UTC：2026-02-16T21:36:28Z；DOI Created UTC：2026-02-18T02:36:10Z。

Reward learning typically relies on a single feedback type or combines multiple feedback types using manually weighted loss terms. Currently, it remains unclear how to jointly learn reward functions from heterogeneous feedback types such as demonstrations, comparisons, ratings, and stops that provide qualitatively different signals. We address this challenge by formulating reward learning from multiple feedback types as Bayesian inference over a shared latent reward function, where each feedback type contributes information through an explicit likelihood. We introduce a scalable amortized variational inference approach that learns a shared reward encoder and feedback-specific likelihood decoders and is trained by optimizing a single evidence lower bound. Our approach avoids reducing feedback to a common intermediate representation and eliminates the need for manual loss balancing. Across discrete and continuous-control benchmarks, we show that jointly inferred reward posteriors outperform single-type baselines, exploit complementary information across feedback types, and yield policies that are more robust to environment perturbations. The inferred reward uncertainty further provides interpretable signals for analyzing model confidence and consistency across feedback types.

## 2602.15210v1 — ÜberWeb: Insights from Multilingual Curation for a 20-Trillion-Token Dataset

原始链接：https://arxiv.org/abs/2602.15210v1

Submitted UTC：2026-02-16T21:40:03Z；DOI Created UTC：2026-02-18T02:36:16Z。

Multilinguality is a core capability for modern foundation models, yet training high-quality multilingual models remains challenging due to uneven data availability across languages. A further challenge is the performance interference that can arise from joint multilingual training, commonly referred to as the "curse of multilinguality". We study multilingual data curation across thirteen languages and find that many reported regressions are not inherent to multilingual scaling but instead stem from correctable deficiencies in data quality and composition rather than fundamental capacity limits. In controlled bilingual experiments, improving data quality for any single language benefits others: curating English improves non-English performance in 12 of 13 languages, while curating non-English yields reciprocal improvements in English. Bespoke per-language curation produces substantially larger within-language improvements. Extending these findings to large-scale general-purpose training mixtures, we show that curated multilingual allocations comprising under 8% of total tokens remain remarkably effective. We operationalize this approach within an effort that produced a 20T-token pretraining corpus derived entirely from public sources. Models with 3B and 8B parameters trained on a 1T-token random subset achieve competitive multilingual accuracy with 4-10x fewer training FLOPs than strong public baselines, establishing a new Pareto frontier in multilingual performance versus compute. Moreover, these benefits extend to frontier model scale: the 20T-token corpus served as part of the pretraining dataset for Trinity Large (400B/A13B), which exhibits strong multilingual performance relative to its training FLOPs. These results show that targeted, per-language data curation mitigates multilingual interference and enables compute-efficient multilingual scaling.

## 2602.15222v1 — Automatically Finding Reward Model Biases

原始链接：https://arxiv.org/abs/2602.15222v1

Submitted UTC：2026-02-16T22:05:44Z；DOI Created UTC：2026-02-18T02:36:32Z。

Reward models are central to large language model (LLM) post-training. However, past work has shown that they can reward spurious or undesirable attributes such as length, format, hallucinations, and sycophancy. In this work, we introduce and study the research problem of automatically finding reward model biases in natural language. We offer a simple approach of using an LLM to iteratively propose and refine candidate biases. Our method can recover known biases and surface novel ones: for example, we found that Skywork-V2-8B, a leading open-weight reward model, often mistakenly favors responses with redundant spacing and responses with hallucinated content. In addition, we show evidence that evolutionary iteration outperforms flat best-of-N search, and we validate the recall of our pipeline using synthetically injected biases. We hope our work contributes to further research on improving RMs through automated interpretability methods.

## 2602.15228v1 — An Empirical Study on the Effects of System Prompts in Instruction-Tuned Models for Code Generation

原始链接：https://arxiv.org/abs/2602.15228v1

Submitted UTC：2026-02-16T22:11:21Z；DOI Created UTC：2026-02-18T02:36:41Z。

Instruction-tuned Language Models (ILMs) have become essential components of modern AI systems, demonstrating exceptional versatility across natural language and reasoning tasks. Among their most impactful applications is code generation, where ILMs -- commonly referred to as Code Language Models (CLMs) -- translate human intent into executable programs. While progress has been driven by advances in scaling and training methodologies, one critical aspect remains underexplored: the impact of system prompts on both general-purpose ILMs and specialized CLMs for code generation. We systematically evaluate how system prompts of varying instructional detail, along with model scale, prompting strategy, and programming language, affect code assistant. Our experimental setting spans 360 configurations across four models, five system prompts, three prompting strategies, two languages, and two temperature settings. We find that (1) increasing system-prompt constraint specificity does not monotonically improve correctness -- prompt effectiveness is configuration-dependent and can help or hinder based on alignment with task requirements and decoding context; (2) for larger code-specialized models, few-shot examples can degrade performance relative to zero-shot generation, contrary to conventional wisdom; and (3) programming language matters, with Java exhibiting significantly greater sensitivity to system prompt variations than Python, suggesting language-specific prompt engineering strategies may be necessary.

## 2602.15238v1 — Closing the Distribution Gap in Adversarial Training for LLMs

原始链接：https://arxiv.org/abs/2602.15238v1

Submitted UTC：2026-02-16T22:34:52Z；DOI Created UTC：2026-02-18T02:36:54Z。

Adversarial training for LLMs is one of the most promising methods to reliably improve robustness against adversaries. However, despite significant progress, models remain vulnerable to simple in-distribution exploits, such as rewriting prompts in the past tense or translating them into other languages. We argue that this persistent fragility stems from a fundamental limitation in current adversarial training algorithms: they minimize adversarial loss on their training set but inadequately cover the data distribution, resulting in vulnerability to seemingly simple attacks. To bridge this gap, we propose Distributional Adversarial Training, DAT. We leverage Diffusion LLMs to approximate the true joint distribution of prompts and responses, enabling generation of diverse, high-likelihood samples that address generalization failures. By combining optimization over the data distribution provided by the diffusion model with continuous adversarial training, DAT achieves substantially higher adversarial robustness than previous methods.

## 2602.15241v1 — GenAI for Systems: Recurring Challenges and Design Principles from Software to Silicon

原始链接：https://arxiv.org/abs/2602.15241v1

Submitted UTC：2026-02-16T22:45:33Z；DOI Created UTC：2026-02-18T02:36:59Z。

Generative AI is reshaping how computing systems are designed, optimized, and built, yet research remains fragmented across software, architecture, and chip design communities. This paper takes a cross-stack perspective, examining how generative models are being applied from code generation and distributed runtimes through hardware design space exploration to RTL synthesis, physical layout, and verification. Rather than reviewing each layer in isolation, we analyze how the same structural difficulties and effective responses recur across the stack. Our central finding is one of convergence. Despite the diversity of domains and tools, the field keeps encountering five recurring challenges (the feedback loop crisis, the tacit knowledge problem, trust and validation, co-design across boundaries, and the shift from determinism to dynamism) and keeps arriving at five design principles that independently emerge as effective responses (embracing hybrid approaches, designing for continuous feedback, separating concerns by role, matching methods to problem structure, and building on decades of systems knowledge). We organize these into a challenge--principle map that serves as a diagnostic and design aid, showing which principles have proven effective for which challenges across layers. Through concrete cross-stack examples, we show how systems navigate this map as they mature, and argue that the field needs shared engineering methodology, including common vocabularies, cross-layer benchmarks, and systematic design practices, so that progress compounds across communities rather than being rediscovered in each one. Our analysis covers more than 275 papers spanning eleven application areas across three layers of the computing stack, and distills open research questions that become visible only from a cross-layer vantage point.

## 2602.15257v1 — How to Train Your Long-Context Visual Document Model

原始链接：https://arxiv.org/abs/2602.15257v1

Submitted UTC：2026-02-16T23:26:51Z；DOI Created UTC：2026-02-18T02:37:21Z。

We present the first comprehensive, large-scale study of training long-context vision language models up to 344K context, targeting long-document visual question answering with measured transfer to long-context text. While several such strong are open-weight, namely Qwen3 VL and GLM 4.5/6V, their training recipes and data pipelines are not reproducible. We systematically study continued pretraining, supervised finetuning, and preference optimization for 24B and 32B parameter models, backed by extensive LC evaluations and ablations to bridge this gap, and achieve state-of-the-art performance on MMLongBenchDoc for both parameter scales. In addition to this, our key findings include: (i) training on context lengths that match evaluation context lengths outperforms training on longer contexts, (ii) training and evaluating with page indices provides a simple, high-impact boost to long-document performance, (iii) our synthetic data pipelines enable self-improvement via continued pretraining and supervised finetuning, and (iv) we extend the known text-to-visual long context transfer to the reverse, showing that visual long context training transfers to long-context text performance. We also release MMLBD-C, a manually corrected version of MMLongBenchDoc to reduce erroneous and low quality examples in the benchmark.

## 2602.15260v1 — Fast and Effective On-policy Distillation from Reasoning Prefixes

原始链接：https://arxiv.org/abs/2602.15260v1

Submitted UTC：2026-02-16T23:28:54Z；DOI Created UTC：2026-02-18T02:37:26Z。

On-policy distillation (OPD), which samples trajectories from the student model and supervises them with a teacher at the token level, avoids relying solely on verifiable terminal rewards and can yield better generalization than off-policy distillation. However, OPD requires expensive on-the-fly sampling of the student policy during training, which substantially increases training cost, especially for long responses. Our initial analysis shows that, during OPD, training signals are often concentrated in the prefix of each output, and that even a short teacher-generated prefix can significantly help the student produce the correct answer. Motivated by these observations, we propose a simple yet effective modification of OPD: we apply the distillation objective only to prefixes of student-generated outputs and terminate each sampling early during distillation. Experiments on a suite of AI-for-Math and out-of-domain benchmarks show that on-policy prefix distillation matches the performance of full OPD while reducing training FLOP by 2x-47x.

## 2602.15274v1 — When Remembering and Planning are Worth it: Navigating under Change

原始链接：https://arxiv.org/abs/2602.15274v1

Submitted UTC：2026-02-17T00:15:47Z；DOI Created UTC：2026-02-18T02:37:45Z。

We explore how different types and uses of memory can aid spatial navigation in changing uncertain environments. In the simple foraging task we study, every day, our agent has to find its way from its home, through barriers, to food. Moreover, the world is non-stationary: from day to day, the location of the barriers and food may change, and the agent's sensing such as its location information is uncertain and very limited. Any model construction, such as a map, and use, such as planning, needs to be robust against these challenges, and if any learning is to be useful, it needs to be adequately fast. We look at a range of strategies, from simple to sophisticated, with various uses of memory and learning. We find that an architecture that can incorporate multiple strategies is required to handle (sub)tasks of a different nature, in particular for exploration and search, when food location is not known, and for planning a good path to a remembered (likely) food location. An agent that utilizes non-stationary probability learning techniques to keep updating its (episodic) memories and that uses those memories to build maps and plan on the fly (imperfect maps, i.e. noisy and limited to the agent's experience) can be increasingly and substantially more efficient than the simpler (minimal-memory) agents, as the task difficulties such as distance to goal are raised, as long as the uncertainty, from localization and change, is not too large.

## 2602.15286v1 — AI-Paging: Lease-Based Execution Anchoring for Network-Exposed AI-as-a-Service

原始链接：https://arxiv.org/abs/2602.15286v1

Submitted UTC：2026-02-17T01:11:26Z；DOI Created UTC：2026-02-18T02:38:01Z。

With AI-as-a-Service (AIaaS) now deployed across multiple providers and model tiers, selecting the appropriate model instance at run time is increasingly outside the end user's knowledge and operational control. Accordingly, the 6G service providers are envisioned to play a crucial role in exposing AIaaS in a setting where users submit only an intent while the network helps in the intent-to-model matching (resolution) and execution placement under policy, trust, and Quality of Service (QoS) constraints. The network role becomes to discover candidate execution endpoints and selects a suitable model/anchor under policy and QoS constraints in a process referred here to as AI-paging (by analogy to cellular call paging). In the proposed architecture, AI-paging is a control-plane transaction that resolves an intent into an AI service identity (AISI), a scoped session token (AIST), and an expiring admission lease (COMMIT) that authorizes user-plane steering to a selected AI execution anchor (AEXF) under a QoS binding. AI-Paging enforces two invariants: (i) lease-gated steering (without COMMIT, no steering state is installed) and (ii) make-before-break anchoring to support continuity and reliability of AIaaS services under dynamic network conditions. We prototype AI-Paging using existing control- and user-plane mechanisms (service-based control, QoS flows, and policy-based steering) with no new packet headers, ensuring compatibility with existing 3GPP-based exposure and management architectures, and evaluate transaction latency, relocation interruption, enforcement correctness under lease expiry, and audit-evidence overhead under mobility and failures.

## 2602.15287v1 — Consistency-Preserving Diverse Video Generation

原始链接：https://arxiv.org/abs/2602.15287v1

Submitted UTC：2026-02-17T01:12:20Z；DOI Created UTC：2026-02-18T02:38:03Z。

Text-to-video generation is expensive, so only a few samples are typically produced per prompt. In this low-sample regime, maximizing the value of each batch requires high cross-video diversity. Recent methods improve diversity for image generation, but for videos they often degrade within-video temporal consistency and require costly backpropagation through a video decoder. We propose a joint-sampling framework for flow-matching video generators that improves batch diversity while preserving temporal consistency. Our approach applies diversity-driven updates and then removes only the components that would decrease a temporal-consistency objective. To avoid image-space gradients, we compute both objectives with lightweight latent-space models, avoiding video decoding and decoder backpropagation. Experiments on a state-of-the-art text-to-video flow-matching model show diversity close to strong joint-sampling baselines while substantially improving temporal consistency and color naturalness. Our code is available at https://github.com/XinshuangL/Diverse-Video.

## 2602.15288v1 — AI Sessions for Network-Exposed AI-as-a-Service

原始链接：https://arxiv.org/abs/2602.15288v1

Submitted UTC：2026-02-17T01:16:32Z；DOI Created UTC：2026-02-18T02:38:04Z。

Cloud-based Artificial Intelligence (AI) inference is increasingly latency- and context-sensitive, yet today's AI-as-a-Service is typically consumed as an application-chosen endpoint, leaving the network to provide only best-effort transport. This decoupling prevents enforceable tail-latency guarantees, compute-aware admission control, and continuity under mobility. This paper proposes Network-Exposed AI-as-a-Service (NE-AIaaS) built around a new service primitive: the AI Session (AIS)-a contractual object that binds model identity, execution placement, transport Quality-of-Service (QoS), and consent/charging scope into a single lifecycle with explicit failure semantics. We introduce the AI Service Profile (ASP), a compact contract that expresses task modality and measurable service objectives (e.g., time-to-first-response/token, p99 latency, success probability) alongside privacy and mobility constraints. On this basis, we specify protocol-grade procedures for (i) DISCOVER (model/site discovery), (ii) AI PAGING (context-aware selection of execution anchor), (iii) two-phase PREPARE/COMMIT that atomically co-reserves compute and QoS resources, and (iv) make-before-break MIGRATION for session continuity. The design is standard-mappable to Common API Framework (CAPIF) style northbound exposure, ETSI Multi-access Edge Computing (MEC) execution substrates, 5G QoS flows for transport enforcement, and Network Data Analytics Function (NWDAF) style analytics for closed-loop paging/migration triggers.

## 2602.15293v1 — The Information Geometry of Softmax: Probing and Steering

原始链接：https://arxiv.org/abs/2602.15293v1

Submitted UTC：2026-02-17T01:33:28Z；DOI Created UTC：2026-02-18T02:38:11Z。

This paper concerns the question of how AI systems encode semantic structure into the geometric structure of their representation spaces. The motivating observation is that the natural geometry of these representation spaces should reflect the way models use representations to produce behavior. We focus on the important special case of representations that define softmax distributions. In this case, we argue that the natural geometry is information geometry. Our focus is on the role of information geometry on semantic encoding and the linear representation hypothesis. As an illustrative application, we develop "dual steering", a method for robustly steering representations to exhibit a particular concept using linear probes. We prove that dual steering optimally modifies the target concept while minimizing changes to off-target concepts. Empirically, we find that dual steering enhances the controllability and stability of concept manipulation.

## 2602.15307v1 — What Do Neurons Listen To? A Neuron-level Dissection of a General-purpose Audio Model

原始链接：https://arxiv.org/abs/2602.15307v1

Submitted UTC：2026-02-17T02:08:40Z；DOI Created UTC：2026-02-18T02:38:31Z。

In this paper, we analyze the internal representations of a general-purpose audio self-supervised learning (SSL) model from a neuron-level perspective. Despite their strong empirical performance as feature extractors, the internal mechanisms underlying the robust generalization of SSL audio models remain unclear. Drawing on the framework of mechanistic interpretability, we identify and examine class-specific neurons by analyzing conditional activation patterns across diverse tasks. Our analysis reveals that SSL models foster the emergence of class-specific neurons that provide extensive coverage across novel task classes. These neurons exhibit shared responses across different semantic categories and acoustic similarities, such as speech attributes and musical pitch. We also confirm that these neurons have a functional impact on classification performance. To our knowledge, this is the first systematic neuron-level analysis of a general-purpose audio SSL model, providing new insights into its internal representation.

## 2602.15313v1 — Mnemis: Dual-Route Retrieval on Hierarchical Graphs for Long-Term LLM Memory

原始链接：https://arxiv.org/abs/2602.15313v1

Submitted UTC：2026-02-17T02:44:03Z；DOI Created UTC：2026-02-18T02:38:39Z。

AI Memory, specifically how models organizes and retrieves historical messages, becomes increasingly valuable to Large Language Models (LLMs), yet existing methods (RAG and Graph-RAG) primarily retrieve memory through similarity-based mechanisms. While efficient, such System-1-style retrieval struggles with scenarios that require global reasoning or comprehensive coverage of all relevant information. In this work, We propose Mnemis, a novel memory framework that integrates System-1 similarity search with a complementary System-2 mechanism, termed Global Selection. Mnemis organizes memory into a base graph for similarity retrieval and a hierarchical graph that enables top-down, deliberate traversal over semantic hierarchies. By combining the complementary strength from both retrieval routes, Mnemis retrieves memory items that are both semantically and structurally relevant. Mnemis achieves state-of-the-art performance across all compared methods on long-term memory benchmarks, scoring 93.9 on LoCoMo and 91.6 on LongMemEval-S using GPT-4.1-mini.

## 2602.15318v1 — Sparrow: Text-Anchored Window Attention with Visual-Semantic Glimpsing for Speculative Decoding in Video LLMs

原始链接：https://arxiv.org/abs/2602.15318v1

Submitted UTC：2026-02-17T02:51:36Z；DOI Created UTC：2026-02-18T02:38:46Z。

Although speculative decoding is widely used to accelerate Vision-Language Models (VLMs) inference, it faces severe performance collapse when applied to Video Large Language Models (Vid-LLMs). The draft model typically falls into the trap of attention dilution and negative visual gain due to key-value cache explosion and context window mismatches. We observe a visual semantic internalization phenomenon in Vid-LLMs, indicating that critical visual semantics are implicitly encoded into text hidden states during deep-layer interactions, which renders raw visual inputs structurally redundant during deep inference. To address this, we propose the Sparrow framework, which first utilizes visually-aware text-anchored window attention via hidden state reuse to fully offload visual computation to the target model, and leverages intermediate-layer visual state bridging to train the draft model with semantic-rich intermediate states, thereby filtering out low-level visual noise. Additionally, a multi-token prediction strategy is introduced to bridge the training-inference distribution shift. Experiments show that Sparrow achieves an average speedup of 2.82x even with 25k visual tokens, effectively resolving the performance degradation in long sequences and offering a practical solution for real-time long video tasks.

## 2602.15322v1 — On Surprising Effectiveness of Masking Updates in Adaptive Optimizers

原始链接：https://arxiv.org/abs/2602.15322v1

Submitted UTC：2026-02-17T02:57:12Z；DOI Created UTC：2026-02-18T02:38:51Z。

Training large language models (LLMs) relies almost exclusively on dense adaptive optimizers with increasingly sophisticated preconditioners. We challenge this by showing that randomly masking parameter updates can be highly effective, with a masked variant of RMSProp consistently outperforming recent state-of-the-art optimizers. Our analysis reveals that the random masking induces a curvature-dependent geometric regularization that smooths the optimization trajectory. Motivated by this finding, we introduce Momentum-aligned gradient masking (Magma), which modulates the masked updates using momentum-gradient alignment. Extensive LLM pre-training experiments show that Magma is a simple drop-in replacement for adaptive optimizers with consistent gains and negligible computational overhead. Notably, for the 1B model size, Magma reduces perplexity by over 19\% and 9\% compared to Adam and Muon, respectively.

## 2602.15323v1 — Unforgeable Watermarks for Language Models via Robust Signatures

原始链接：https://arxiv.org/abs/2602.15323v1

Submitted UTC：2026-02-17T03:09:06Z；DOI Created UTC：2026-02-18T02:38:53Z。

Language models now routinely produce text that is difficult to distinguish from human writing, raising the need for robust tools to verify content provenance. Watermarking has emerged as a promising countermeasure, with existing work largely focused on model quality preservation and robust detection. However, current schemes provide limited protection against false attribution. We strengthen the notion of soundness by introducing two novel guarantees: unforgeability and recoverability. Unforgeability prevents adversaries from crafting false positives, texts that are far from any output from the watermarked model but are nonetheless flagged as watermarked. Recoverability provides an additional layer of protection: whenever a watermark is detected, the detector identifies the source text from which the flagged content was derived. Together, these properties strengthen content ownership by linking content exclusively to its generating model, enabling secure attribution and fine-grained traceability. We construct the first undetectable watermarking scheme that is robust, unforgeable, and recoverable with respect to substitutions (i.e., perturbations in Hamming metric). The key technical ingredient is a new cryptographic primitive called robust (or recoverable) digital signatures, which allow verification of messages that are close to signed ones, while preventing forgery of messages that are far from all previously signed messages. We show that any standard digital signature scheme can be boosted to a robust one using property-preserving hash functions (Boyle, LaVigne, and Vaikuntanathan, ITCS 2019).

## 2602.15327v1 — Prescriptive Scaling Reveals the Evolution of Language Model Capabilities

原始链接：https://arxiv.org/abs/2602.15327v1

Submitted UTC：2026-02-17T03:13:51Z；DOI Created UTC：2026-02-18T02:38:58Z。

Machine learning model performance improvements tend to arise from competition and application. For deployment, we consider prescriptive scaling laws: given a pre-training compute budget, what downstream accuracy is attainable with contemporary post-training practice, and how stable is that mapping as the field evolves? Using large-scale observational evaluations with 5k existing and 2k newly evaluated model checkpoints spanning 2022-2026 across six benchmarks, we estimate capability boundaries, high conditional quantiles of benchmark scores as a function of log pre-training FLOPs, via smoothed quantile regression with a monotone, saturating sigmoid parameterization. We validate temporal reliability by fitting on earlier model generations and evaluating on later releases: across four of six tasks, the out-of-distribution coverage error remains below 2%, while math reasoning exhibits a consistently advancing boundary over time. For instance, at a budget of 10^24 FLOPs, the estimated attainable accuracies are 0.83 on IFEval and 0.54 on MATH Lvl 5. We then extend our approach to analyze task-dependent saturation and to probe contamination-related shifts on math reasoning tasks. Finally, we introduce a balanced I-optimal sampling algorithm that recovers near-full-data frontiers using roughly 20% of the parameter-count-weighted evaluation budget, as low as 5% on some tasks, while maintaining comparable calibration. Together, our work releases Proteus-2k, the latest model performance evaluation dataset, and introduces a practical methodology for translating compute budgets into reliable performance expectations and for monitoring when capability boundaries shift across time.

## 2602.15329v1 — EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use

原始链接：https://arxiv.org/abs/2602.15329v1

Submitted UTC：2026-02-17T03:17:24Z；DOI Created UTC：2026-02-18T02:39:01Z。

Online video understanding requires models to perform continuous perception and long-range reasoning within potentially infinite visual streams. Its fundamental challenge lies in the conflict between the unbounded nature of streaming media input and the limited context window of Multimodal Large Language Models (MLLMs). Current methods primarily rely on passive processing, which often face a trade-off between maintaining long-range context and capturing the fine-grained details necessary for complex tasks. To address this, we introduce EventMemAgent, an active online video agent framework based on a hierarchical memory module. Our framework employs a dual-layer strategy for online videos: short-term memory detects event boundaries and utilizes event-granular reservoir sampling to process streaming video frames within a fixed-length buffer dynamically; long-term memory structuredly archives past observations on an event-by-event basis. Furthermore, we integrate a multi-granular perception toolkit for active, iterative evidence capture and employ Agentic Reinforcement Learning (Agentic RL) to end-to-end internalize reasoning and tool-use strategies into the agent's intrinsic capabilities. Experiments show that EventMemAgent achieves competitive results on online video benchmarks. The code will be released here: https://github.com/lingcco/EventMemAgent.

## 2602.15332v1 — Directional Reasoning Trajectory Change (DRTC): Identifying Critical Trace Segments in Reasoning Models

原始链接：https://arxiv.org/abs/2602.15332v1

Submitted UTC：2026-02-17T03:38:16Z；DOI Created UTC：2026-02-18T02:39:05Z。

Understanding how language models carry out long-horizon reasoning remains an open challenge. Existing interpretability methods often highlight tokens correlated with an answer, but rarely reveal where consequential reasoning turns occur, which earlier context triggers them under causal intervention, or whether highlighted text actually steers the rollout. We introduce Directional Reasoning Trajectory Change (DRTC), a process-causal method that (i) detects pivot decision points via uncertainty and distribution-shift signals and (ii) applies receiver-side interventions that preserve the realized continuation without resampling while blocking information flow from selected earlier chunks only at a pivot. DRTC measures how each intervention redirects the log-probability trajectory relative to the realized rollout direction, yielding signed per-chunk attributions; we also compute logit-space curvature changes and curvature signatures as a complementary geometric diagnostic. Across four reasoning models, influence is sharply concentrated (Gini approximately 0.50-0.58, top-5% mass approximately 0.23-0.28), and learned pivots induce stronger effects than matched random spans. In a 500-problem MATH scaling study with R1-Distill-Qwen-1.5B, learned spans continue to outperform matched random spans (median Delta=0.409, 355/500 positive; p=2.3e-21), and curvature-impact co-localizes with DRTC within traces as a diagnostic. We benchmark against gradient- and perturbation-based chunk attributions and show graded outcome linkage: under embedding-interpolation edits, top-ranked DRTC chunks reduce teacher-forced gold-answer log-probability more than strict position-matched random chunks on a stability-filtered subset. Overall, DRTC provides a causally grounded view of how specific context elements steer on-policy reasoning trajectories.

## 2602.15338v1 — Discovering Implicit Large Language Model Alignment Objectives

原始链接：https://arxiv.org/abs/2602.15338v1

Submitted UTC：2026-02-17T03:58:55Z；DOI Created UTC：2026-02-18T02:39:13Z。

Large language model (LLM) alignment relies on complex reward signals that often obscure the specific behaviors being incentivized, creating critical risks of misalignment and reward hacking. Existing interpretation methods typically rely on pre-defined rubrics, risking the omission of "unknown unknowns", or fail to identify objectives that comprehensively cover and are causal to the model behavior. To address these limitations, we introduce Obj-Disco, a framework that automatically decomposes an alignment reward signal into a sparse, weighted combination of human-interpretable natural language objectives. Our approach utilizes an iterative greedy algorithm to analyze behavioral changes across training checkpoints, identifying and validating candidate objectives that best explain the residual reward signal. Extensive evaluations across diverse tasks, model sizes, and alignment algorithms demonstrate the framework's robustness. Experiments with popular open-source reward models show that the framework consistently captures &gt; 90% of reward behavior, a finding further corroborated by human evaluation. Additionally, a case study on alignment with an open-source reward model reveals that Obj-Disco can successfully identify latent misaligned incentives that emerge alongside intended behaviors. Our work provides a crucial tool for uncovering the implicit objectives in LLM alignment, paving the way for more transparent and safer AI development.

## 2602.15344v1 — ER-MIA: Black-Box Adversarial Memory Injection Attacks on Long-Term Memory-Augmented Large Language Models

原始链接：https://arxiv.org/abs/2602.15344v1

Submitted UTC：2026-02-17T04:19:45Z；DOI Created UTC：2026-02-18T02:39:22Z。

Large language models (LLMs) are increasingly augmented with long-term memory systems to overcome finite context windows and enable persistent reasoning across interactions. However, recent research finds that LLMs become more vulnerable because memory provides extra attack surfaces. In this paper, we present the first systematic study of black-box adversarial memory injection attacks that target the similarity-based retrieval mechanism in long-term memory-augmented LLMs. We introduce ER-MIA, a unified framework that exposes this vulnerability and formalizes two realistic attack settings: content-based attacks and question-targeted attacks. In these settings, ER-MIA includes an arsenal of composable attack primitives and ensemble attacks that achieve high success rates under minimal attacker assumptions. Extensive experiments across multiple LLMs and long-term memory systems demonstrate that similarity-based retrieval constitutes a fundamental and system-level vulnerability, revealing security risks that persist across memory designs and application scenarios.

## 2602.15356v1 — Co-Design and Evaluation of a CPU-Free MPI GPU Communication Abstraction and Implementation

原始链接：https://arxiv.org/abs/2602.15356v1

Submitted UTC：2026-02-17T04:50:06Z；DOI Created UTC：2026-02-18T02:39:38Z。

Removing the CPU from the communication fast path is essential to efficient GPU-based ML and HPC application performance. However, existing GPU communication APIs either continue to rely on the CPU for communication or rely on APIs that place significant synchronization burdens on programmers. In this paper we describe the design, implementation, and evaluation of an MPI-based GPU communication API enabling easy-to-use, high-performance, CPU-free communication. This API builds on previously proposed MPI extensions and leverages HPE Slingshot 11 network card capabilities. We demonstrate the utility and performance of the API by showing how the API naturally enables CPU-free gather/scatter halo exchange communication primitives in the Cabana/Kokkos performance portability framework, and through a performance comparison with Cray MPICH on the Frontier and Tuolumne supercomputers. Results from this evaluation show up to a 50% reduction in medium message latency in simple GPU ping-pong exchanges and a 28% speedup improvement when strong scaling a halo-exchange benchmark to 8,192 GPUs of the Frontier supercomputer.

## 2602.15364v1 — MarkSweep: A No-box Removal Attack on AI-Generated Image Watermarking via Noise Intensification and Frequency-aware Denoising

原始链接：https://arxiv.org/abs/2602.15364v1

Submitted UTC：2026-02-17T05:19:00Z；DOI Created UTC：2026-02-18T02:39:50Z。

AI watermarking embeds invisible signals within images to provide provenance information and identify content as AI-generated. In this paper, we introduce MarkSweep, a novel watermark removal attack that effectively erases the embedded watermarks from AI-generated images without degrading visual quality. MarkSweep first amplifies watermark noise in high-frequency regions via edge-aware Gaussian perturbations and injects it into clean images for training a denoising network. This network then integrates two modules, the learnable frequency decomposition module and the frequency-aware fusion module, to suppress amplified noise and eliminate watermark traces. Theoretical analysis and extensive experiments demonstrate that invisible watermarks are highly vulnerable to MarkSweep, which effectively removes embedded watermarks, reducing the bit accuracy of HiDDeN and Stable Signature watermarking schemes to below 67%, while preserving perceptual quality of AI-generated images.

## 2602.15373v1 — Far Out: Evaluating Language Models on Slang in Australian and Indian English

原始链接：https://arxiv.org/abs/2602.15373v1

Submitted UTC：2026-02-17T05:59:20Z；DOI Created UTC：2026-02-18T02:40:02Z。

Language models exhibit systematic performance gaps when processing text in non-standard language varieties, yet their ability to comprehend variety-specific slang remains underexplored for several languages. We present a comprehensive evaluation of slang awareness in Indian English (en-IN) and Australian English (en-AU) across seven state-of-the-art language models. We construct two complementary datasets: WEB, containing 377 web-sourced usage examples from Urban Dictionary, and GEN, featuring 1,492 synthetically generated usages of these slang terms, across diverse scenarios. We assess language models on three tasks: target word prediction (TWP), guided target word prediction (TWP$^*$) and target word selection (TWS). Our results reveal four key findings: (1) Higher average model performance TWS versus TWP and TWP$^*$, with average accuracy score increasing from 0.03 to 0.49 respectively (2) Stronger average model performance on WEB versus GEN datasets, with average similarity score increasing by 0.03 and 0.05 across TWP and TWP$^*$ tasks respectively (3) en-IN tasks outperform en-AU when averaged across all models and datasets, with TWS demonstrating the largest disparity, increasing average accuracy from 0.44 to 0.54. These findings underscore fundamental asymmetries between generative and discriminative competencies for variety-specific language, particularly in the context of slang expressions despite being in a technologically rich language such as English.

## 2602.15379v1 — FlashMem: Supporting Modern DNN Workloads on Mobile with GPU Memory Hierarchy Optimizations

原始链接：https://arxiv.org/abs/2602.15379v1

Submitted UTC：2026-02-17T06:23:40Z；DOI Created UTC：2026-02-18T02:40:11Z。

The increasing size and complexity of modern deep neural networks (DNNs) pose significant challenges for on-device inference on mobile GPUs, with limited memory and computational resources. Existing DNN acceleration frameworks primarily deploy a weight preloading strategy, where all model parameters are loaded into memory before execution on mobile GPUs. We posit that this approach is not adequate for modern DNN workloads that comprise very large model(s) and possibly execution of several distinct models in succession. In this work, we introduce FlashMem, a memory streaming framework designed to efficiently execute large-scale modern DNNs and multi-DNN workloads while minimizing memory consumption and reducing inference latency. Instead of fully preloading weights, FlashMem statically determines model loading schedules and dynamically streams them on demand, leveraging 2.5D texture memory to minimize data transformations and improve execution efficiency. Experimental results on 11 models demonstrate that FlashMem achieves 2.0x to 8.4x memory reduction and 1.7x to 75.0x speedup compared to existing frameworks, enabling efficient execution of large-scale models and multi-DNN support on resource-constrained mobile GPUs.

## 2602.15382v1 — The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems

原始链接：https://arxiv.org/abs/2602.15382v1

Submitted UTC：2026-02-17T06:31:53Z；DOI Created UTC：2026-02-18T02:40:15Z。

Multi-Agent Systems (MAS) powered by Large Language Models have unlocked advanced collaborative reasoning, yet they remain bottlenecked by discrete text communication, which imposes runtime overhead and information quantization loss. While latent state transfer offers an alternative, existing approaches either assume homogeneous sender--receiver architectures or rely on pair-specific learned translators, limiting scalability across diverse model families with disjoint manifolds. We reconceptualize the visual interface of Vision-Language Models (VLMs), trained for natural images, as a continuous communication channel between heterogeneous agents, and instantiate this idea as the \textbf{Vision Wormhole}: a Universal Visual Codec maps reasoning traces into a shared continuous reference space and injects them into the receiver's visual pathway, yielding cross-architecture latent state transfer without per-pair translators. The framework adopts a hub-and-spoke topology that reduces alignment complexity from $O(N^2)$ to $O(N)$, and is trained by label-free teacher--student distillation against the text channel, requiring no parallel hidden-state supervision. Extensive experiments across heterogeneous VLM families (Qwen-VL, Gemma, SmolVLM2, LFM2.5-VL) and nine reasoning benchmarks show that the Vision Wormhole reduces end-to-end wall-clock time across most evaluated settings and yields positive macro-average $Δ$-accuracy.

## 2602.15384v1 — World-Model-Augmented Web Agents with Action Correction

原始链接：https://arxiv.org/abs/2602.15384v1

Submitted UTC：2026-02-17T06:37:31Z；DOI Created UTC：2026-02-18T02:40:18Z。

Web agents based on large language models have demonstrated promising capability in automating web tasks. However, current web agents struggle to reason out sensible actions due to the limitations of predicting environment changes, and might not possess comprehensive awareness of execution risks, prematurely performing risky actions that cause losses and lead to task failure. To address these challenges, we propose WAC, a web agent that integrates model collaboration, consequence simulation, and feedback-driven action refinement. To overcome the cognitive isolation of individual models, we introduce a multi-agent collaboration process that enables an action model to consult a world model as a web-environment expert for strategic guidance; the action model then grounds these suggestions into executable actions, leveraging prior knowledge of environmental state transition dynamics to enhance candidate action proposal. To achieve risk-aware resilient task execution, we introduce a two-stage deduction chain. A world model, specialized in environmental state transitions, simulates action outcomes, which a judge model then scrutinizes to trigger action corrective feedback when necessary. Experiments show that WAC achieves absolute gains of 1.8% on VisualWebArena and 1.3% on Online-Mind2Web.

## 2602.15391v1 — Improving LLM Reliability through Hybrid Abstention and Adaptive Detection

原始链接：https://arxiv.org/abs/2602.15391v1

Submitted UTC：2026-02-17T07:00:09Z；DOI Created UTC：2026-02-18T02:40:28Z。

Large Language Models (LLMs) deployed in production environments face a fundamental safety-utility trade-off either a strict filtering mechanisms prevent harmful outputs but often block benign queries or a relaxed controls risk unsafe content generation. Conventional guardrails based on static rules or fixed confidence thresholds are typically context-insensitive and computationally expensive, resulting in high latency and degraded user experience. To address these limitations, we introduce an adaptive abstention system that dynamically adjusts safety thresholds based on real-time contextual signals such as domain and user history. The proposed framework integrates a multi-dimensional detection architecture composed of five parallel detectors, combined through a hierarchical cascade mechanism to optimize both speed and precision. The cascade design reduces unnecessary computation by progressively filtering queries, achieving substantial latency improvements compared to non-cascaded models and external guardrail systems. Extensive evaluation on mixed and domain-specific workloads demonstrates significant reductions in false positives, particularly in sensitive domains such as medical advice and creative writing. The system maintains high safety precision and near-perfect recall under strict operating modes. Overall, our context-aware abstention framework effectively balances safety and utility while preserving performance, offering a scalable solution for reliable LLM deployment.

## 2602.15396v1 — Efficient Generative Modeling beyond Memoryless Diffusion via Adjoint Schrödinger Bridge Matching

原始链接：https://arxiv.org/abs/2602.15396v1

Submitted UTC：2026-02-17T07:06:20Z；DOI Created UTC：2026-02-18T02:40:35Z。

Diffusion models often yield highly curved trajectories and noisy score targets due to an uninformative, memoryless forward process that induces independent data-noise coupling. We propose Adjoint Schrödinger Bridge Matching (ASBM), a generative modeling framework that recovers optimal trajectories in high dimensions via two stages. First, we view the Schrödinger Bridge (SB) forward dynamic as a coupling construction problem and learn it through a data-to-energy sampling perspective that transports data to an energy-defined prior. Then, we learn the backward generative dynamic with a simple matching loss supervised by the induced optimal coupling. By operating in a non-memoryless regime, ASBM produces significantly straighter and more efficient sampling paths. Compared to prior works, ASBM scales to high-dimensional data with notably improved stability and efficiency. Extensive experiments on image generation show that ASBM improves fidelity with fewer sampling steps. We further showcase the effectiveness of our optimal trajectory via distillation to a one-step generator.

## 2602.15397v1 — ActionCodec: What Makes for Good Action Tokenizers

原始链接：https://arxiv.org/abs/2602.15397v1

Submitted UTC：2026-02-17T07:07:15Z；DOI Created UTC：2026-02-18T02:40:37Z。

Vision-Language-Action (VLA) models leveraging the native autoregressive paradigm of Vision-Language Models (VLMs) have demonstrated superior instruction-following and training efficiency. Central to this paradigm is action tokenization, yet its design has primarily focused on reconstruction fidelity, failing to address its direct impact on VLA optimization. Consequently, the fundamental question of \textit{what makes for good action tokenizers} remains unanswered. In this paper, we bridge this gap by establishing design principles specifically from the perspective of VLA optimization. We identify a set of best practices based on information-theoretic insights, including maximized temporal token overlap, minimized vocabulary redundancy, enhanced multimodal mutual information, and token independence. Guided by these principles, we introduce \textbf{ActionCodec}, a high-performance action tokenizer that significantly enhances both training efficiency and VLA performance across diverse simulation and real-world benchmarks. Notably, on LIBERO, a SmolVLM2-2.2B fine-tuned with ActionCodec achieves a 95.5\% success rate without any robotics pre-training. With advanced architectural enhancements, this reaches 97.4\%, representing a new SOTA for VLA models without robotics pre-training. We believe our established design principles, alongside the released model, will provide a clear roadmap for the community to develop more effective action tokenizers.

## 2602.15400v1 — One Agent to Guide Them All: Empowering MLLMs for Vision-and-Language Navigation via Explicit World Representation

原始链接：https://arxiv.org/abs/2602.15400v1

Submitted UTC：2026-02-17T07:13:48Z；DOI Created UTC：2026-02-18T02:40:40Z。

A navigable agent needs to understand both high-level semantic instructions and precise spatial perceptions. Building navigation agents centered on Multimodal Large Language Models (MLLMs) demonstrates a promising solution due to their powerful generalization ability. However, the current tightly coupled design dramatically limits system performance. In this work, we propose a decoupled design that separates low-level spatial state estimation from high-level semantic planning. Unlike previous methods that rely on predefined, oversimplified textual maps, we introduce an interactive metric world representation that maintains rich and consistent information, allowing MLLMs to interact with and reason on it for decision-making. Furthermore, counterfactual reasoning is introduced to further elicit MLLMs' capacity, while the metric world representation ensures the physical validity of the produced actions. We conduct comprehensive experiments in both simulated and real-world environments. Our method establishes a new zero-shot state-of-the-art, achieving 48.8\% Success Rate (SR) in R2R-CE and 42.2\% in RxR-CE benchmarks. Furthermore, to validate the versatility of our metric representation, we demonstrate zero-shot sim-to-real transfer across diverse embodiments, including a wheeled TurtleBot 4 and a custom-built aerial drone. These real-world deployments verify that our decoupled framework serves as a robust, domain-invariant interface for embodied Vision-and-Language navigation.

## 2602.15423v1 — GaiaFlow: Semantic-Guided Diffusion Tuning for Carbon-Frugal Search

原始链接：https://arxiv.org/abs/2602.15423v1

Submitted UTC：2026-02-17T08:35:11Z；DOI Created UTC：2026-02-18T02:41:13Z。

As the burgeoning power requirements of sophisticated neural architectures escalate, the information retrieval community has recognized ecological sustainability as a pivotal priority that necessitates a fundamental paradigm shift in model design. While contemporary neural rankers have attained unprecedented accuracy, the substantial environmental externalities associated with their computational intensity often remain overlooked in large-scale deployments. We present GaiaFlow, an innovative framework engineered to facilitate carbon-frugal search by operationalizing semantic-guided diffusion tuning. Our methodology orchestrates the convergence of retrieval-guided Langevin dynamics and a hardware-independent performance modeling strategy to optimize the trade-off between search precision and environmental preservation. By incorporating adaptive early exit protocols and precision-aware quantized inference, the proposed architecture significantly mitigates operational carbon footprints while maintaining robust retrieval quality across heterogeneous computing infrastructures. Extensive experimental evaluations demonstrate that GaiaFlow achieves a superior equilibrium between effectiveness and energy efficiency, offering a scalable and sustainable pathway for next-generation neural search systems.

## 2602.15438v1 — Logit Distance Bounds Representational Similarity

原始链接：https://arxiv.org/abs/2602.15438v1

Submitted UTC：2026-02-17T09:00:56Z；DOI Created UTC：2026-02-18T02:41:33Z。

For a broad family of discriminative models that includes autoregressive language models, identifiability results imply that if two models induce the same conditional distributions, then their internal representations are equal up to an invertible linear transformation. We ask whether an analogous conclusion holds approximately when the distributions are close instead of equal. Building on the observation of Nielsen et al. (2025) that closeness in KL divergence need not imply high linear representational similarity, we study a distributional distance based on logit differences and show that closeness in this distance does yield linear similarity guarantees. Specifically, we define a representational dissimilarity measure based on the models' identifiability class and prove that it is bounded by the logit distance. We further show that, when model probabilities are bounded away from zero, KL divergence upper-bounds logit distance; yet the resulting bound fails to provide nontrivial control in practice. As a consequence, KL-based distillation can match a teacher's predictions while failing to preserve linear representational properties, such as linear-probe recoverability of human-interpretable concepts. In distillation experiments on synthetic and image datasets, logit-distance distillation yields students with higher linear representational similarity and better preservation of the teacher's linearly recoverable concepts.

## 2602.15449v1 — TAROT: Test-driven and Capability-adaptive Curriculum Reinforcement Fine-tuning for Code Generation with Large Language Models

原始链接：https://arxiv.org/abs/2602.15449v1

Submitted UTC：2026-02-17T09:29:18Z；DOI Created UTC：2026-02-18T02:41:48Z。

Large Language Models (LLMs) are changing the coding paradigm, known as vibe coding, yet synthesizing algorithmically sophisticated and robust code still remains a critical challenge. Incentivizing the deep reasoning capabilities of LLMs is essential to overcoming this hurdle. Reinforcement Fine-Tuning (RFT) has emerged as a promising strategy to address this need. However, most existing approaches overlook the heterogeneous difficulty and granularity inherent in test cases, leading to an imbalanced distribution of reward signals and consequently biased gradient updates during training. To address this, we propose Test-driven and cApability-adaptive cuRriculum reinfOrcement fine-Tuning (TAROT). TAROT systematically constructs, for each problem, a four-tier test suite (basic, intermediate, complex, edge), providing a controlled difficulty landscape for curriculum design and evaluation. Crucially, TAROT decouples curriculum progression from raw reward scores, enabling capability-conditioned evaluation and principled selection from a portfolio of curriculum policies rather than incidental test-case difficulty composition. This design fosters stable optimization and more efficient competency acquisition. Extensive experimental results reveal that the optimal curriculum for RFT in code generation is closely tied to a model's inherent capability, with less capable models achieving greater gains with an easy-to-hard progression, whereas more competent models excel under a hard-first curriculum. TAROT provides a reproducible method that adaptively tailors curriculum design to a model's capability, thereby consistently improving the functional correctness and robustness of the generated code. All code and data are released to foster reproducibility and advance community research at https://github.com/deep-diver/TAROT.

## 2602.15456v1 — In Agents We Trust, but Who Do Agents Trust? Latent Source Preferences Steer LLM Generations

原始链接：https://arxiv.org/abs/2602.15456v1

Submitted UTC：2026-02-17T09:45:22Z；DOI Created UTC：2026-02-18T02:41:58Z。

Agents based on Large Language Models (LLMs) are increasingly being deployed as interfaces to information on online platforms. These agents filter, prioritize, and synthesize information retrieved from the platforms' back-end databases or via web search. In these scenarios, LLM agents govern the information users receive, by drawing users' attention to particular instances of retrieved information at the expense of others. While much prior work has focused on biases in the information LLMs themselves generate, less attention has been paid to the factors that influence what information LLMs select and present to users. We hypothesize that when information is attributed to specific sources (e.g., particular publishers, journals, or platforms), current LLMs exhibit systematic latent source preferences- that is, they prioritize information from some sources over others. Through controlled experiments on twelve LLMs from six model providers, spanning both synthetic and real-world tasks, we find that several models consistently exhibit strong and predictable source preferences. These preferences are sensitive to contextual framing, can outweigh the influence of content itself, and persist despite explicit prompting to avoid them. They also help explain phenomena such as the observed left-leaning skew in news recommendations in prior work. Our findings advocate for deeper investigation into the origins of these preferences, as well as for mechanisms that provide users with transparency and control over the biases guiding LLM-powered agents.

## 2602.15460v1 — On the Out-of-Distribution Generalization of Reasoning in Multimodal LLMs for Simple Visual Planning Tasks

原始链接：https://arxiv.org/abs/2602.15460v1

Submitted UTC：2026-02-17T09:51:40Z；DOI Created UTC：2026-02-18T02:42:04Z。

Integrating reasoning in large language models and large vision-language models has recently led to significant improvement of their capabilities. However, the generalization of reasoning models is still vaguely defined and poorly understood. In this work, we present an evaluation framework to rigorously examine how well chain-of-thought (CoT) approaches generalize on a simple planning task. Specifically, we consider a grid-based navigation task in which a model is provided with a map and must output a sequence of moves that guides a player from a start position to a goal while avoiding obstacles. The versatility of the task and its data allows us to fine-tune model variants using different input representations (visual and textual) and CoT reasoning strategies, and systematically evaluate them under both in-distribution (ID) and out-of-distribution (OOD) test conditions. Our experiments show that, while CoT reasoning improves in-distribution generalization across all representations, out-of-distribution generalization (e.g., to larger maps) remains very limited in most cases when controlling for trivial matches with the ID data. Surprisingly, we find that reasoning traces which combine multiple text formats yield the best (and non-trivial) OOD generalization. Finally, purely text-based models consistently outperform those utilizing image-based inputs, including a recently proposed approach relying on latent space reasoning.

## 2602.15473v1 — POP: Prior-Fitted First-Order Optimization Policies

原始链接：https://arxiv.org/abs/2602.15473v1

Submitted UTC：2026-02-17T10:27:07Z；DOI Created UTC：2026-02-18T02:42:22Z。

Gradient-based optimizers are highly sensitive to design choices in their adaptive learning rate mechanisms. To address this limitation, we introduce POP, a meta-learned Reinforcement Learning (RL) policy that predicts adaptive learning rates for gradient descent, conditioned on the contextual information provided in the optimization trajectory. Our method introduces a novel RL reward formulation, a new function-scaling strategy for in-distribution generalization, and a novel prior that is used to sample millions of synthetic optimization problems. We evaluate POP on an established benchmark including 43 optimization functions of various complexity, where it significantly outperforms gradient-based methods. Our evaluation demonstrates strong generalization capabilities without task-specific tuning.

## 2602.15481v1 — LLM-as-Judge on a Budget

原始链接：https://arxiv.org/abs/2602.15481v1

Submitted UTC：2026-02-17T10:35:41Z；DOI Created UTC：2026-02-18T02:42:33Z。

LLM-as-a-judge has emerged as a cornerstone technique for evaluating large language models by leveraging LLM reasoning to score prompt-response pairs. Since LLM judgments are stochastic, practitioners commonly query each pair multiple times to estimate mean scores accurately. This raises a critical challenge: given a fixed computational budget $B$, how to optimally allocate queries across $K$ prompt-response pairs to minimize estimation error? We present a principled variance-adaptive approach leveraging multi-armed bandit theory and concentration inequalities. Our method dynamically allocates queries based on estimated score variances, concentrating resources where uncertainty is highest. Further, our algorithm is shown to achieve a worst-case score-estimation error of $\tilde{O}\left(\sqrt{\frac{\sum_{i=1}^K σ_i^2}{B}}\right)$, $σ_i^2$ being the unknown score variance for pair $i \in [K]$ with near-optimal budget allocation. Experiments on \emph{Summarize-From-Feedback} and \emph{HelpSteer2} demonstrate that our method significantly outperforms uniform allocation, reducing worst-case estimation error while maintaining identical budgets. Our work establishes a theoretical foundation for efficient LLM evaluation with practical implications for AI safety, model alignment, and automated assessment at scale.

## 2602.15485v1 — SecCodeBench-V2 Technical Report

原始链接：https://arxiv.org/abs/2602.15485v1

Submitted UTC：2026-02-17T10:47:06Z；DOI Created UTC：2026-02-18T02:42:39Z。

We introduce SecCodeBench-V2, a publicly released benchmark for evaluating Large Language Model (LLM) copilots' capabilities of generating secure code. SecCodeBench-V2 comprises 98 generation and fix scenarios derived from Alibaba Group's industrial productions, where the underlying security issues span 22 common CWE (Common Weakness Enumeration) categories across five programming languages: Java, C, Python, Go, and JavaScript. SecCodeBench-V2 adopts a function-level task formulation: each scenario provides a complete project scaffold and requires the model to implement or patch a designated target function under fixed interfaces and dependencies. For each scenario, SecCodeBench-V2 provides executable proof-of-concept (PoC) test cases for both functional validation and security verification. All test cases are authored and double-reviewed by security experts, ensuring high fidelity, broad coverage, and reliable ground truth. Beyond the benchmark itself, we build a unified evaluation pipeline that assesses models primarily via dynamic execution. For most scenarios, we compile and run model-generated artifacts in isolated environments and execute PoC test cases to validate both functional correctness and security properties. For scenarios where security issues cannot be adjudicated with deterministic test cases, we additionally employ an LLM-as-a-judge oracle. To summarize performance across heterogeneous scenarios and difficulty levels, we design a Pass@K-based scoring protocol with principled aggregation over scenarios and severity, enabling holistic and comparable evaluation across models. Overall, SecCodeBench-V2 provides a rigorous and reproducible foundation for assessing the security posture of AI coding assistants, with results and artifacts released at https://alibaba.github.io/sec-code-bench. The benchmark is publicly available at https://github.com/alibaba/sec-code-bench.

## 2602.15488v1 — Efficient Approximate Nearest Neighbor Search under Multi-Attribute Range Filter

原始链接：https://arxiv.org/abs/2602.15488v1

Submitted UTC：2026-02-17T10:52:57Z；DOI Created UTC：2026-02-18T02:42:43Z。

Nearest neighbor search on high-dimensional vectors is fundamental in modern AI and database systems. In many real-world applications, queries involve constraints on multiple numeric attributes, giving rise to range-filtering approximate nearest neighbor search (RFANNS). While there exist RFANNS indexes for single-attribute range predicates, extending them to the multi-attribute setting is nontrivial and often ineffective. In this paper, we propose KHI, an index for multi-attribute RFANNS that combines an attribute-space partitioning tree with HNSW graphs attached to tree nodes. A skew-aware splitting rule bounds the tree height by $O(\log n)$, and queries are answered by routing through the tree and running greedy search on the HNSW graphs. Experiments on four real-world datasets show that KHI consistently achieves high query throughput while maintaining high recall. Compared with the state-of-the-art RFANNS baseline, KHI improves QPS by $2.46\times$ on average and up to $16.22\times$ on the hard dataset, with larger gains for smaller selectivity, larger $k$, and higher predicate cardinality.

## 2602.15491v1 — The Equalizer: Introducing Shape-Gain Decomposition in Neural Audio Codecs

原始链接：https://arxiv.org/abs/2602.15491v1

Submitted UTC：2026-02-17T10:59:33Z；DOI Created UTC：2026-02-18T02:42:47Z。

Neural audio codecs (NACs) typically encode the short-term energy (gain) and normalized structure (shape) of speech/audio signals jointly within the same latent space. As a result, they are poorly robust to a global variation of the input signal level in the sense that such a variation has a strong influence on the embedding vectors at the output of the encoder and their quantization. This methodology is inherently inefficient, leading to codebook redundancy and suboptimal bitrate-distortion performance. To address these limitations, we propose to introduce shape-gain decomposition, widely used in classical speech and audio coding, into the NAC framework. The principle of the proposed Equalizer methodology, easily applicable to any NAC, is to decompose the input signal---before the NAC encoder---into gain and normalized shape vector on a short-term basis. The shape vector is processed by the NAC, while the gain is quantized with scalar quantization and transmitted separately. The output (decoded) signal is reconstructed from the normalized output of the NAC and the quantized gain. Our experiments conducted on speech signals with four different prominent codecs show that this general methodology enables a substantial gain in bitrate-distortion performance, as well as a massive reduction in quantizer complexity.

## 2602.15503v1 — Approximation Theory for Lipschitz Continuous Transformers

原始链接：https://arxiv.org/abs/2602.15503v1

Submitted UTC：2026-02-17T11:16:52Z；DOI Created UTC：2026-02-18T02:43:04Z。

Stability and robustness are critical for deploying Transformers in safety-sensitive settings. A principled way to enforce such behavior is to constrain the model's Lipschitz constant. However, approximation-theoretic guarantees for architectures that explicitly preserve Lipschitz continuity have yet to be established. In this work, we bridge this gap by introducing a class of gradient-descent-type in-context Transformers that are Lipschitz-continuous by construction. We realize both MLP and attention blocks as explicit Euler steps of negative gradient flows, ensuring inherent stability without sacrificing expressivity. We prove a universal approximation theorem for this class within a Lipschitz-constrained function space. Crucially, our analysis adopts a measure-theoretic formalism, interpreting Transformers as operators on probability measures, to yield approximation guarantees independent of token count. These results provide a rigorous theoretical foundation for the design of robust, Lipschitz continuous Transformer architectures.

## 2602.15513v1 — HIMM: Human-Inspired Long-Term Memory Modeling for Embodied Exploration and Question Answering

原始链接：https://arxiv.org/abs/2602.15513v1

Submitted UTC：2026-02-17T11:41:28Z；DOI Created UTC：2026-02-18T02:43:18Z。

Deploying Multimodal Large Language Models as the brain of embodied agents remains challenging, particularly under long-horizon observations and limited context budgets. Existing memory assisted methods often rely on textual summaries, which discard rich visual and spatial details and remain brittle in non-stationary environments. In this work, we propose a non-parametric memory framework that explicitly disentangles episodic and semantic memory for embodied exploration and question answering. Our retrieval-first, reasoning-assisted paradigm recalls episodic experiences via semantic similarity and verifies them through visual reasoning, enabling robust reuse of past observations without rigid geometric alignment. In parallel, we introduce a program-style rule extraction mechanism that converts experiences into structured, reusable semantic memory, facilitating cross-environment generalization. Extensive experiments demonstrate state-of-the-art performance on embodied question answering and exploration benchmarks, yielding a 7.3% gain in LLM-Match and an 11.4% gain in LLM MatchXSPL on A-EQA, as well as +7.7% success rate and +6.8% SPL on GOAT-Bench. Analyses reveal that our episodic memory primarily improves exploration efficiency, while semantic memory strengthens complex reasoning of embodied agents.

## 2602.15515v1 — The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes

原始链接：https://arxiv.org/abs/2602.15515v1

Submitted UTC：2026-02-17T11:44:10Z；DOI Created UTC：2026-02-18T02:43:21Z。

Training against white-box deception detectors has been proposed as a way to make AI systems honest. However, such training risks models learning to obfuscate their deception to evade the detector. Prior work has studied obfuscation only in artificial settings where models were directly rewarded for harmful output. We construct a realistic coding environment where reward hacking via hardcoding test cases naturally occurs, and show that obfuscation emerges in this setting. We introduce a taxonomy of possible outcomes when training against a deception detector. The model either remains honest, or becomes deceptive via two possible obfuscation strategies. (i) Obfuscated activations: the model outputs deceptive text while modifying its internal representations to no longer trigger the detector. (ii) Obfuscated policy: the model outputs deceptive text that evades the detector, typically by including a justification for the reward hack. Empirically, obfuscated activations arise from representation drift during RL, with or without a detector penalty. The detector penalty only incentivizes obfuscated policies; we theoretically show this is expected for policy gradient methods. Sufficiently high KL regularization and detector penalty can yield honest policies, establishing white-box deception detectors as viable training signals for tasks prone to reward hacking.

## 2602.15521v1 — ExpertWeaver: Unlocking the Inherent MoE in Dense LLMs with GLU Activation Patterns

原始链接：https://arxiv.org/abs/2602.15521v1

Submitted UTC：2026-02-17T11:50:58Z；DOI Created UTC：2026-02-18T02:43:29Z。

Mixture-of-Experts (MoE) effectively scales model capacity while preserving computational efficiency through sparse expert activation. However, training high-quality MoEs from scratch is prohibitively expensive. A promising alternative is to convert pretrained dense models into sparse MoEs. Existing dense-to-MoE methods fall into two categories: \textbf{dynamic structural pruning} that converts dense models into MoE architectures with moderate sparsity to balance performance and inference efficiency, and \textbf{downcycling} approaches that use pretrained dense models to initialize highly sparse MoE architectures. However, existing methods break the intrinsic activation patterns within dense models, leading to suboptimal expert construction. In this work, we argue that the Gated Linear Unit (GLU) mechanism provides a natural blueprint for dense-to-MoE conversion. We show that the fine-grained neural-wise activation patterns of GLU reveal a coarse-grained structure, uncovering an inherent MoE architecture composed of consistently activated universal neurons and dynamically activated specialized neurons. Leveraging this discovery, we introduce ExpertWeaver, a training-free framework that partitions neurons according to their activation patterns and constructs shared experts and specialized routed experts with layer-adaptive configurations. Our experiments demonstrate that ExpertWeaver significantly outperforms existing methods, both as a training-free dynamic structural pruning technique and as a downcycling strategy for superior MoE initialization.

## 2602.15532v1 — Quantifying construct validity in large language model evaluations

原始链接：https://arxiv.org/abs/2602.15532v1

Submitted UTC：2026-02-17T12:15:57Z；DOI Created UTC：2026-02-18T02:43:45Z。

The LLM community often reports benchmark results as if they are synonymous with general model capabilities. However, benchmarks can have problems that distort performance, like test set contamination and annotator error. How can we know that a benchmark is a reliable indicator of some capability that we want to measure? This question concerns the construct validity of LLM benchmarks, and it requires separating benchmark results from capabilities when we model and predict LLM performance.
 Both social scientists and computer scientists propose formal models - latent factor models and scaling laws - for identifying the capabilities underlying benchmark scores. However, neither technique is satisfactory for construct validity. Latent factor models ignore scaling laws, and as a result, the capabilities they extract often proxy model size. Scaling laws ignore measurement error, and as a result, the capabilities they extract are both uninterpretable and overfit to the observed benchmarks.
 This thesis presents the structured capabilities model, the first model to extract interpretable and generalisable capabilities from a large collection of LLM benchmark results. I fit this model and its two alternatives on a large sample of results from the OpenLLM Leaderboard. Structured capabilities outperform latent factor models on parsimonious fit indices, and exhibit better out-of-distribution benchmark prediction than scaling laws. These improvements are possible because neither existing approach separates model scale from capabilities in the appropriate way. Model scale should inform capabilities, as in scaling laws, and these capabilities should inform observed results up to measurement error, as in latent factor models. In combining these two insights, structured capabilities demonstrate better explanatory and predictive power for quantifying construct validity in LLM evaluations.

## 2602.15537v1 — ZeroSyl: Simple Zero-Resource Syllable Tokenization for Spoken Language Modeling

原始链接：https://arxiv.org/abs/2602.15537v1

Submitted UTC：2026-02-17T12:38:45Z；DOI Created UTC：2026-02-18T02:43:52Z。

Pure speech language models aim to learn language directly from raw audio without textual resources. A key challenge is that discrete tokens from self-supervised speech encoders result in excessively long sequences, motivating recent work on syllable-like units. However, methods like Sylber and SyllableLM rely on intricate multi-stage training pipelines. We propose ZeroSyl, a simple training-free method to extract syllable boundaries and embeddings directly from a frozen WavLM model. Using L2 norms of features in WavLM's intermediate layers, ZeroSyl achieves competitive syllable segmentation performance. The resulting segments are mean-pooled, discretized using K-means, and used to train a language model. ZeroSyl outperforms prior syllabic tokenizers across lexical, syntactic, and narrative benchmarks. Scaling experiments show that while finer-grained units are beneficial for lexical tasks, our discovered syllabic units exhibit better scaling behavior for syntactic modeling.

## 2602.15539v1 — Dynamic Training-Free Fusion of Subject and Style LoRAs

原始链接：https://arxiv.org/abs/2602.15539v1

Submitted UTC：2026-02-17T12:42:30Z；DOI Created UTC：2026-02-18T02:43:54Z。

Recent studies have explored the combination of multiple LoRAs to simultaneously generate user-specified subjects and styles. However, most existing approaches fuse LoRA weights using static statistical heuristics that deviate from LoRA's original purpose of learning adaptive feature adjustments and ignore the randomness of sampled inputs. To address this, we propose a dynamic training-free fusion framework that operates throughout the generation process. During the forward pass, at each LoRA-applied layer, we dynamically compute the KL divergence between the base model's original features and those produced by subject and style LoRAs, respectively, and adaptively select the most appropriate weights for fusion. In the reverse denoising stage, we further refine the generation trajectory by dynamically applying gradient-based corrections derived from objective metrics such as CLIP and DINO scores, providing continuous semantic and stylistic guidance. By integrating these two complementary mechanisms-feature-level selection and metric-guided latent adjustment-across the entire diffusion timeline, our method dynamically achieves coherent subject-style synthesis without any retraining. Extensive experiments across diverse subject-style combinations demonstrate that our approach consistently outperforms state-of-the-art LoRA fusion methods both qualitatively and quantitatively.

## 2602.15543v1 — Selective Perception for Robot: Task-Aware Attention in Multimodal VLA

原始链接：https://arxiv.org/abs/2602.15543v1

Submitted UTC：2026-02-17T12:48:59Z；DOI Created UTC：2026-02-18T02:44:00Z。

In robotics, Vision-Language-Action (VLA) models that integrate diverse multimodal signals from multi-view inputs have emerged as an effective approach. However, most prior work adopts static fusion that processes all visual inputs uniformly, which incurs unnecessary computational overhead and allows task-irrelevant background information to act as noise. Inspired by the principles of human active perception, we propose a dynamic information fusion framework designed to maximize the efficiency and robustness of VLA models. Our approach introduces a lightweight adaptive routing architecture that analyzes the current text prompt and observations from a wrist-mounted camera in real-time to predict the task-relevance of multiple camera views. By conditionally attenuating computations for views with low informational utility and selectively providing only essential visual features to the policy network, Our framework achieves computation efficiency proportional to task relevance. Furthermore, to efficiently secure large-scale annotation data for router training, we established an automated labeling pipeline utilizing Vision-Language Models (VLMs) to minimize data collection and annotation costs. Experimental results in real-world robotic manipulation scenarios demonstrate that the proposed approach achieves significant improvements in both inference efficiency and control performance compared to existing VLA models, validating the effectiveness and practicality of dynamic information fusion in resource-constrained, real-time robot control environments.

## 2602.15547v1 — jina-embeddings-v5-text: Task-Targeted Embedding Distillation

原始链接：https://arxiv.org/abs/2602.15547v1

Submitted UTC：2026-02-17T12:50:50Z；DOI Created UTC：2026-02-18T02:44:05Z。

Text embedding models are widely used for semantic similarity tasks, including information retrieval, clustering, and classification. General-purpose models are typically trained with single- or multi-stage processes using contrastive loss functions. We introduce a novel training regimen that combines model distillation techniques with task-specific contrastive loss to produce compact, high-performance embedding models. Our findings suggest that this approach is more effective for training small models than purely contrastive or distillation-based training paradigms alone. Benchmark scores for the resulting models, jina-embeddings-v5-text-small and jina-embeddings-v5-text-nano, exceed or match the state-of-the-art for models of similar size. jina-embeddings-v5-text models additionally support long texts (up to 32k tokens) in many languages, and generate embeddings that remain robust under truncation and binary quantization. Model weights are publicly available, hopefully inspiring further advances in embedding model development.

## 2602.15549v1 — VLM-DEWM: Dynamic External World Model for Verifiable and Resilient Vision-Language Planning in Manufacturing

原始链接：https://arxiv.org/abs/2602.15549v1

Submitted UTC：2026-02-17T12:54:18Z；DOI Created UTC：2026-02-18T02:44:08Z。

Vision-language model (VLM) shows promise for high-level planning in smart manufacturing, yet their deployment in dynamic workcells faces two critical challenges: (1) stateless operation, they cannot persistently track out-of-view states, causing world-state drift; and (2) opaque reasoning, failures are difficult to diagnose, leading to costly blind retries. This paper presents VLM-DEWM, a cognitive architecture that decouples VLM reasoning from world-state management through a persistent, queryable Dynamic External World Model (DEWM). Each VLM decision is structured into an Externalizable Reasoning Trace (ERT), comprising action proposal, world belief, and causal assumption, which is validated against DEWM before execution. When failures occur, discrepancy analysis between predicted and observed states enables targeted recovery instead of global replanning. We evaluate VLM-DEWM on multi-station assembly, large-scale facility exploration, and real-robot recovery under induced failures. Compared to baseline memory-augmented VLM systems, VLM DEWM improves state-tracking accuracy from 56% to 93%, increases recovery success rate from below 5% to 95%, and significantly reduces computational overhead through structured memory. These results establish VLM-DEWM as a verifiable and resilient solution for long-horizon robotic operations in dynamic manufacturing environments.

## 2602.15556v1 — Revealing and Enhancing Core Visual Regions: Harnessing Internal Attention Dynamics for Hallucination Mitigation in LVLMs

原始链接：https://arxiv.org/abs/2602.15556v1

Submitted UTC：2026-02-17T13:08:06Z；DOI Created UTC：2026-02-18T02:44:18Z。

LVLMs have achieved strong multimodal reasoning capabilities but remain prone to hallucinations, producing outputs inconsistent with visual inputs or user instructions. Existing training-free methods, including contrastive decoding and auxiliary expert models, which incur several times more computational overhead and may introduce potential interference, as well as static internal signal enhancement, are often vulnerable to the attention sink phenomenon. We find that internal Positive Attention Dynamics (PAD) in LVLMs naturally reveal semantically core visual regions under the distortions of attention sinks. Based on this, we propose Positive Attention Dynamics Enhancement (PADE), a training-free attention intervention that constructs a PAD map to identify semantically core visual regions, applies per-head Median Absolute Deviation Scaling to adaptively control the intervention strength, and leverages System-Token Compensation to maintain attention to complex user instructions and support long-term output consistency. Experiments on multiple LVLMs and benchmarks show that PADE improves visual grounding and reduces hallucinations, validating the effectiveness of leveraging internal attention dynamics for reliable multimodal reasoning.

## 2602.15563v1 — 1-Bit Wonder: Improving QAT Performance in the Low-Bit Regime through K-Means Quantization

原始链接：https://arxiv.org/abs/2602.15563v1

Submitted UTC：2026-02-17T13:23:26Z；DOI Created UTC：2026-02-18T02:44:27Z。

Quantization-aware training (QAT) is an effective method to drastically reduce the memory footprint of LLMs while keeping performance degradation at an acceptable level. However, the optimal choice of quantization format and bit-width presents a challenge in practice. The full design space of quantization is not fully explored in the context of QAT, and the precise trade-off between quantization and downstream performance is poorly understood, as comparisons often rely solely on perplexity-based evaluations. In this work, we address these shortcomings with an empirical study of QAT in the low-bit regime. We show that k-means based weight quantization outperforms integer formats and can be implemented efficiently on standard hardware. Furthermore, we find that, under a fixed inference memory budget, the best performance on generative downstream tasks is achieved with $1$-bit quantized weights.

## 2602.15564v1 — Beyond Static Pipelines: Learning Dynamic Workflows for Text-to-SQL

原始链接：https://arxiv.org/abs/2602.15564v1

Submitted UTC：2026-02-17T13:24:56Z；DOI Created UTC：2026-02-18T02:44:28Z。

Text-to-SQL has recently achieved impressive progress, yet remains difficult to apply effectively in real-world scenarios. This gap stems from the reliance on single static workflows, fundamentally limiting scalability to out-of-distribution and long-tail scenarios. Instead of requiring users to select suitable methods through extensive experimentation, we attempt to enable systems to adaptively construct workflows at inference time. Through theoretical and empirical analysis, we demonstrate that optimal dynamic policies consistently outperform the best static workflow, with performance gains fundamentally driven by heterogeneity across candidate workflows. Motivated by this, we propose SquRL, a reinforcement learning framework that enhances LLMs' reasoning capability in adaptive workflow construction. We design a rule-based reward function and introduce two effective training mechanisms: dynamic actor masking to encourage broader exploration, and pseudo rewards to improve training efficiency. Experiments on widely-used Text-to-SQL benchmarks demonstrate that dynamic workflow construction consistently outperforms the best static workflow methods, with especially pronounced gains on complex and out-of-distribution queries. The codes are available at https://github.com/Satissss/SquRL

## 2602.15567v1 — Constraining Streaming Flow Models for Adapting Learned Robot Trajectory Distributions

原始链接：https://arxiv.org/abs/2602.15567v1

Submitted UTC：2026-02-17T13:27:05Z；DOI Created UTC：2026-02-18T02:44:33Z。

Robot motion distributions often exhibit multi-modality and require flexible generative models for accurate representation. Streaming Flow Policies (SFPs) have recently emerged as a powerful paradigm for generating robot trajectories by integrating learned velocity fields directly in action space, enabling smooth and reactive control. However, existing formulations lack mechanisms for adapting trajectories post-training to enforce safety and task-specific constraints. We propose Constraint-Aware Streaming Flow (CASF), a framework that augments streaming flow policies with constraint-dependent metrics that reshape the learned velocity field during execution. CASF models each constraint, defined in either the robot's workspace or configuration space, as a differentiable distance function that is converted into a local metric and pulled back into the robot's control space. Far from restricted regions, the resulting metric reduces to the identity; near constraint boundaries, it smoothly attenuates or redirects motion, effectively deforming the underlying flow to maintain safety. This allows trajectories to be adapted in real time, ensuring that robot actions respect joint limits, avoid collisions, and remain within feasible workspaces, while preserving the multi-modal and reactive properties of streaming flow policies. We demonstrate CASF in simulated and real-world manipulation tasks, showing that it produces constraint-satisfying trajectories that remain smooth, feasible, and dynamically consistent, outperforming standard post-hoc projection baselines.

## 2602.15569v1 — What Are You Doing? Effects of Intermediate Feedback from Agentic LLM In-Car Assistants During Multi-Step Processing

原始链接：https://arxiv.org/abs/2602.15569v1

Submitted UTC：2026-02-17T13:27:50Z；DOI Created UTC：2026-02-18T02:44:35Z。

Agentic AI assistants that autonomously perform multi-step tasks raise open questions for user experience: how should such systems communicate progress and reasoning during extended operations, especially in attention-critical contexts such as driving? We investigate feedback timing and verbosity from agentic LLM-based in-car assistants through a controlled, mixed-methods study (N=45) comparing planned steps and intermediate results feedback against silent operation with final-only response. Using a dual-task paradigm with an in-car voice assistant, we found that intermediate feedback significantly improved perceived speed, trust, and user experience while reducing task load - effects that held across varying task complexities and interaction contexts. Interviews further revealed user preferences for an adaptive approach: high initial transparency to establish trust, followed by progressively reducing verbosity as systems prove reliable, with adjustments based on task stakes and situational context. We translate our empirical findings into design implications for feedback timing and verbosity in agentic assistants, balancing transparency and efficiency.

## 2602.15580v1 — How Vision Becomes Language: A Layer-wise Information-Theoretic Analysis of Multimodal Reasoning

原始链接：https://arxiv.org/abs/2602.15580v1

Submitted UTC：2026-02-17T13:49:49Z；DOI Created UTC：2026-02-18T02:44:51Z。

When a multimodal Transformer answers a visual question, is the prediction driven by visual evidence, linguistic reasoning, or genuinely fused cross-modal computation -- and how does this structure evolve across layers? We address this question with a layer-wise framework based on Partial Information Decomposition (PID) that decomposes the predictive information at each Transformer layer into redundant, vision-unique, language-unique, and synergistic components. To make PID tractable for high-dimensional neural representations, we introduce \emph{PID Flow}, a pipeline combining dimensionality reduction, normalizing-flow Gaussianization, and closed-form Gaussian PID estimation. Applying this framework to LLaVA-1.5-7B and LLaVA-1.6-7B across six GQA reasoning tasks, we uncover a consistent \emph{modal transduction} pattern: visual-unique information peaks early and decays with depth, language-unique information surges in late layers to account for roughly 82\% of the final prediction, and cross-modal synergy remains below 2\%. This trajectory is highly stable across model variants (layer-wise correlations $&gt;$0.96) yet strongly task-dependent, with semantic redundancy governing the detailed information fingerprint. To establish causality, we perform targeted Image$\rightarrow$Question attention knockouts and show that disrupting the primary transduction pathway induces predictable increases in trapped visual-unique information, compensatory synergy, and total information cost -- effects that are strongest in vision-dependent tasks and weakest in high-redundancy tasks. Together, these results provide an information-theoretic, causal account of how vision becomes language in multimodal Transformers, and offer quantitative guidance for identifying architectural bottlenecks where modality-specific information is lost.

## 2602.15593v1 — A unified theory of feature learning in RNNs and DNNs

原始链接：https://arxiv.org/abs/2602.15593v1

Submitted UTC：2026-02-17T14:06:34Z；DOI Created UTC：2026-02-18T02:45:10Z。

Recurrent and deep neural networks (RNNs/DNNs) are cornerstone architectures in machine learning. Remarkably, RNNs differ from DNNs only by weight sharing, as can be shown through unrolling in time. How does this structural similarity fit with the distinct functional properties these networks exhibit? To address this question, we here develop a unified mean-field theory for RNNs and DNNs in terms of representational kernels, describing fully trained networks in the feature learning ($μ$P) regime. This theory casts training as Bayesian inference over sequences and patterns, directly revealing the functional implications induced by the RNNs' weight sharing. In DNN-typical tasks, we identify a phase transition when the learning signal overcomes the noise due to randomness in the weights: below this threshold, RNNs and DNNs behave identically; above it, only RNNs develop correlated representations across timesteps. For sequential tasks, the RNNs' weight sharing furthermore induces an inductive bias that aids generalization by interpolating unsupervised time steps. Overall, our theory offers a way to connect architectural structure to functional biases.

## 2602.15602v1 — Certified Per-Instance Unlearning Using Individual Sensitivity Bounds

原始链接：https://arxiv.org/abs/2602.15602v1

Submitted UTC：2026-02-17T14:18:47Z；DOI Created UTC：2026-02-18T02:45:22Z。

Certified machine unlearning can be achieved via noise injection leading to differential privacy guarantees, where noise is calibrated to worst-case sensitivity. Such conservative calibration often results in performance degradation, limiting practical applicability. In this work, we investigate an alternative approach based on adaptive per-instance noise calibration tailored to the individual contribution of each data point to the learned solution. This raises the following challenge: how can one establish formal unlearning guarantees when the mechanism depends on the specific point to be removed? To define individual data point sensitivities in noisy gradient dynamics, we consider the use of per-instance differential privacy. For ridge regression trained via Langevin dynamics, we derive high-probability per-instance sensitivity bounds, yielding certified unlearning with substantially less noise injection. We corroborate our theoretical findings through experiments in linear settings and provide further empirical evidence on the relevance of the approach in deep learning settings.

## 2602.15620v1 — STAPO: Stabilizing Reinforcement Learning for LLMs by Silencing Rare Spurious Tokens

原始链接：https://arxiv.org/abs/2602.15620v1

Submitted UTC：2026-02-17T14:46:48Z；DOI Created UTC：2026-02-18T02:45:47Z。

Reinforcement Learning (RL) has significantly improved large language model reasoning, but existing RL fine-tuning methods rely heavily on heuristic techniques such as entropy regularization and reweighting to maintain stability. In practice, they often suffer from late-stage performance collapse, leading to degraded reasoning quality and unstable training. We identify a key factor behind this instability: a small fraction of tokens, termed spurious tokens (around 0.01%), which contribute little to the reasoning outcome but receive disproportionately amplified gradient updates due to inheriting the full sequence-level reward. We present a unified framework for evaluating token-level optimization impacts across spurious risk, gradient norms, and entropy changes. Building on the analysis of token characteristics that severely disrupt optimization, we propose the Silencing Spurious Tokens (S2T) mechanism to efficiently suppress their gradient perturbations. Incorporating this mechanism into a group-based objective, we propose Spurious-Token-Aware Policy Optimization (STAPO), which promotes stable and effective large-scale model refinement. Across six mathematical reasoning benchmarks using Qwen 1.7B, 8B, and 14B base models, STAPO consistently demonstrates superior entropy stability and achieves an average performance improvement of 11.49% ($ρ_{\mathrm{T}}$=1.0, top-p=1.0) and 3.73% ($ρ_{\mathrm{T}}$=0.7, top-p=0.9) over GRPO, 20-Entropy, and JustRL.

## 2602.15654v1 — Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections

原始链接：https://arxiv.org/abs/2602.15654v1

Submitted UTC：2026-02-17T15:28:24Z；DOI Created UTC：2026-02-18T02:46:36Z。

Self-evolving LLM agents update their internal state across sessions, often by writing and reusing long-term memory. This design improves performance on long-horizon tasks but creates a security risk: untrusted external content observed during a benign session can be stored as memory and later treated as instruction. We study this risk and formalize a persistent attack we call a Zombie Agent, where an attacker covertly implants a payload that survives across sessions, effectively turning the agent into a puppet of the attacker.
 We present a black-box attack framework that uses only indirect exposure through attacker-controlled web content. The attack has two phases. During infection, the agent reads a poisoned source while completing a benign task and writes the payload into long-term memory through its normal update process. During trigger, the payload is retrieved or carried forward and causes unauthorized tool behavior. We design mechanism-specific persistence strategies for common memory implementations, including sliding-window and retrieval-augmented memory, to resist truncation and relevance filtering. We evaluate the attack on representative agent setups and tasks, measuring both persistence over time and the ability to induce unauthorized actions while preserving benign task quality. Our results show that memory evolution can convert one-time indirect injection into persistent compromise, which suggests that defenses focused only on per-session prompt filtering are not sufficient for self-evolving agents.

## 2602.15669v1 — PERSONA: Dynamic and Compositional Inference-Time Personality Control via Activation Vector Algebra

原始链接：https://arxiv.org/abs/2602.15669v1

Submitted UTC：2026-02-17T15:47:58Z；DOI Created UTC：2026-02-18T02:46:56Z。

Current methods for personality control in Large Language Models rely on static prompting or expensive fine-tuning, failing to capture the dynamic and compositional nature of human traits. We introduce PERSONA, a training-free framework that achieves fine-tuning level performance through direct manipulation of personality vectors in activation space. Our key insight is that personality traits appear as extractable, approximately orthogonal directions in the model's representation space that support algebraic operations. The framework operates through three stages: Persona-Base extracts orthogonal trait vectors via contrastive activation analysis; Persona-Algebra enables precise control through vector arithmetic (scalar multiplication for intensity, addition for composition, subtraction for suppression); and Persona-Flow achieves context-aware adaptation by dynamically composing these vectors during inference. On PersonalityBench, our approach achieves a mean score of 9.60, nearly matching the supervised fine-tuning upper bound of 9.61 without any gradient updates. On our proposed Persona-Evolve benchmark for dynamic personality adaptation, we achieve up to 91% win rates across diverse model families. These results provide evidence that aspects of LLM personality are mathematically tractable, opening new directions for interpretable and efficient behavioral control.

## 2602.15671v1 — Revisiting Backdoor Threat in Federated Instruction Tuning from a Signal Aggregation Perspective

原始链接：https://arxiv.org/abs/2602.15671v1

Submitted UTC：2026-02-17T15:54:45Z；DOI Created UTC：2026-02-18T02:46:59Z。

Federated learning security research has predominantly focused on backdoor threats from a minority of malicious clients that intentionally corrupt model updates. This paper challenges this paradigm by investigating a more pervasive and insidious threat: \textit{backdoor vulnerabilities from low-concentration poisoned data distributed across the datasets of benign clients.} This scenario is increasingly common in federated instruction tuning for language models, which often rely on unverified third-party and crowd-sourced data. We analyze two forms of backdoor data through real cases: 1) \textit{natural trigger (inherent features as implicit triggers)}; 2) \textit{adversary-injected trigger}. To analyze this threat, we model the backdoor implantation process from signal aggregation, proposing the Backdoor Signal-to-Noise Ratio to quantify the dynamics of the distributed backdoor signal. Extensive experiments reveal the severity of this threat: With just less than 10\% of training data poisoned and distributed across clients, the attack success rate exceeds 85\%, while the primary task performance remains largely intact. Critically, we demonstrate that state-of-the-art backdoor defenses, designed for attacks from malicious clients, are fundamentally ineffective against this threat. Our findings highlight an urgent need for new defense mechanisms tailored to the realities of modern, decentralized data ecosystems.

## 2602.15689v1 — A Content-Based Framework for Cybersecurity Refusal Decisions in Large Language Models

原始链接：https://arxiv.org/abs/2602.15689v1

Submitted UTC：2026-02-17T16:12:21Z；DOI Created UTC：2026-02-18T02:47:24Z。

Large language models and LLM-based agents are increasingly used for cybersecurity tasks that are inherently dual-use. Existing approaches to refusal, spanning academic policy frameworks and commercially deployed systems, often rely on broad topic-based bans or offensive-focused taxonomies. As a result, they can yield inconsistent decisions, over-restrict legitimate defenders, and behave brittlely under obfuscation or request segmentation. We argue that effective refusal requires explicitly modeling the trade-off between offensive risk and defensive benefit, rather than relying solely on intent or offensive classification. In this paper, we introduce a content-based framework for designing and auditing cyber refusal policies that makes offense-defense tradeoffs explicit. The framework characterizes requests along five dimensions: Offensive Action Contribution, Offensive Risk, Technical Complexity, Defensive Benefit, and Expected Frequency for Legitimate Users, grounded in the technical substance of the request rather than stated intent. We demonstrate that this content-grounded approach resolves inconsistencies in current frontier model behavior and allows organizations to construct tunable, risk-aware refusal policies.

## 2602.15682v1 — The Next Paradigm Is User-Centric Agent, Not Platform-Centric Service

原始链接：https://arxiv.org/abs/2602.15682v1

Submitted UTC：2026-02-17T16:07:44Z；DOI Created UTC：2026-02-18T02:47:14Z。

Modern digital services have evolved into indispensable tools, driving the present large-scale information systems. Yet, the prevailing platform-centric model, where services are optimized for platform-driven metrics such as engagement and conversion, often fails to align with users' true needs. While platform technologies have advanced significantly-especially with the integration of large language models (LLMs)-we argue that improvements in platform service quality do not necessarily translate to genuine user benefit. Instead, platform-centric services prioritize provider objectives over user welfare, resulting in conflicts against user interests. This paper argues that the future of digital services should shift from a platform-centric to a user-centric agent. These user-centric agents prioritize privacy, align with user-defined goals, and grant users control over their preferences and actions. With advancements in LLMs and on-device intelligence, the realization of this vision is now feasible. This paper explores the opportunities and challenges in transitioning to user-centric intelligence, presents a practical device-cloud pipeline for its implementation, and discusses the necessary governance and ecosystem structures for its adoption.

## 2602.15725v1 — Recursive Concept Evolution for Compositional Reasoning in Large Language Models

原始链接：https://arxiv.org/abs/2602.15725v1

Submitted UTC：2026-02-17T17:01:42Z；DOI Created UTC：2026-02-18T02:48:14Z。

Large language models achieve strong performance on many complex reasoning tasks, yet their accuracy degrades sharply on benchmarks that require compositional reasoning, including ARC-AGI-2, GPQA, MATH, BBH, and HLE. Existing methods improve reasoning by expanding token-level search through chain-of-thought prompting, self-consistency, or reinforcement learning, but they leave the model's latent representation space fixed. When the required abstraction is not already encoded in this space, performance collapses. We propose Recursive Concept Evolution (RCE), a framework that enables pretrained language models to modify their internal representation geometry during inference. RCE introduces dynamically generated low-rank concept subspaces that are spawned when representational inadequacy is detected, selected through a minimum description length criterion, merged when synergistic, and consolidated via constrained optimization to preserve stability. This process allows the model to construct new abstractions rather than recombining existing ones. We integrate RCE with Mistral-7B and evaluate it across compositional reasoning benchmarks. RCE yields 12-18 point gains on ARC-AGI-2, 8-14 point improvements on GPQA and BBH, and consistent reductions in depth-induced error on MATH and HLE.

## 2602.15727v1 — Spanning the Visual Analogy Space with a Weight Basis of LoRAs

原始链接：https://arxiv.org/abs/2602.15727v1

Submitted UTC：2026-02-17T17:02:38Z；DOI Created UTC：2026-02-18T02:48:16Z。

Visual analogy learning enables image editing via demonstration rather than textual description, allowing users to specify complex transformations difficult to articulate in words. Given a triplet $\{\mathbf{a}$, $\mathbf{a}'$, $\mathbf{b}\}$, the goal is to generate $\mathbf{b}'$ such that $\mathbf{a} : \mathbf{a}' :: \mathbf{b} : \mathbf{b}'$. Recent methods adapt text-to-image models with a single Low-Rank Adaptation (LoRA) module, but they face a fundamental limitation: attempting to capture the diverse space of visual transformations within a fixed module constrains generalization. Inspired by recent work showing that LoRAs in constrained domains span meaningful, interpolatable semantic spaces, we propose LoRWeB, which specializes the model for each analogy task in a single inference pass. LoRWeB dynamically composes learned transformation primitives, informally, choosing a point in a "space of LoRAs". We introduce two key components: (1) a learnable basis of LoRAs to span the space of different visual transformations, and (2) a lightweight encoder that dynamically weighs these basis LoRAs given the input analogy pair. Comprehensive evaluations demonstrate state-of-the-art performance and significantly improved generalization to unseen transformations. Our findings suggest LoRA basis decompositions are a promising direction for flexible visual manipulation tasks. See https://research.nvidia.com/labs/par/lorweb for code.

## 2602.15749v1 — A Generative-First Neural Audio Autoencoder

原始链接：https://arxiv.org/abs/2602.15749v1

Submitted UTC：2026-02-17T17:26:12Z；DOI Created UTC：2026-02-18T02:48:48Z。

Neural autoencoders underpin generative models. Practical, large-scale use of neural autoencoders for generative modeling necessitates fast encoding, low latent rates, and a single model across representations. Existing approaches are reconstruction-first: they incur high latent rates, slow encoding, and separate architectures for discrete vs. continuous latents and for different audio channel formats, hindering workflows from preprocessing to inference conditioning. We introduce a generative-first architecture for audio autoencoding that increases temporal downsampling from 2048x to 3360x and supports continuous and discrete representations and common audio channel formats in one model. By balancing compression, quality, and speed, it delivers 10x faster encoding, 1.6x lower rates, and eliminates channel-format-specific variants while maintaining competitive reconstruction quality. This enables applications previously constrained by processing costs: a 60-second mono signal compresses to 788 tokens, making generative modeling more tractable.

## 2602.15756v1 — A Note on Non-Composability of Layerwise Approximate Verification for Neural Inference

原始链接：https://arxiv.org/abs/2602.15756v1

Submitted UTC：2026-02-17T17:41:59Z；DOI Created UTC：2026-02-18T02:48:58Z。

A natural and informal approach to verifiable (or zero-knowledge) ML inference over floating-point data is: ``prove that each layer was computed correctly up to tolerance $δ$; therefore the final output is a reasonable inference result''. This short note gives a simple counterexample showing that this inference is false in general: for any neural network, we can construct a functionally equivalent network for which adversarially chosen approximation-magnitude errors in individual layer computations suffice to steer the final output arbitrarily (within a prescribed bounded range).

## 2602.15758v1 — ChartEditBench: Evaluating Grounded Multi-Turn Chart Editing in Multimodal Language Models

原始链接：https://arxiv.org/abs/2602.15758v1

Submitted UTC：2026-02-17T17:45:34Z；DOI Created UTC：2026-02-18T02:49:01Z。

While Multimodal Large Language Models (MLLMs) perform strongly on single-turn chart generation, their ability to support real-world exploratory data analysis remains underexplored. In practice, users iteratively refine visualizations through multi-turn interactions that require maintaining common ground, tracking prior edits, and adapting to evolving preferences. We introduce ChartEditBench, a benchmark for incremental, visually grounded chart editing via code, comprising 5,000 difficulty-controlled modification chains and a rigorously human-verified subset. Unlike prior one-shot benchmarks, ChartEditBench evaluates sustained, context-aware editing. We further propose a robust evaluation framework that mitigates limitations of LLM-as-a-Judge metrics by integrating execution-based fidelity checks, pixel-level visual similarity, and logical code verification. Experiments with state-of-the-art MLLMs reveal substantial degradation in multi-turn settings due to error accumulation and breakdowns in shared context, with strong performance on stylistic edits but frequent execution failures on data-centric transformations. ChartEditBench, establishes a challenging testbed for grounded, intent-aware multimodal programming.

## 2602.15761v1 — A Differential Fuzzing-Based Evaluation of Functional Equivalence in LLM-Generated Code Refactorings

原始链接：https://arxiv.org/abs/2602.15761v1

Submitted UTC：2026-02-17T17:47:13Z；DOI Created UTC：2026-02-18T02:49:05Z。

With the rapid adoption of large language models (LLMs) in automated code refactoring, assessing and ensuring functional equivalence between LLM-generated refactoring and the original implementation becomes critical. While prior work typically relies on predefined test cases to evaluate correctness, in this work, we leverage differential fuzzing to check functional equivalence in LLM-generated code refactorings. Unlike test-based evaluation, a differential fuzzing-based equivalence checker needs no predefined test cases and can explore a much larger input space by executing and comparing thousands of automatically generated test inputs. In a large-scale evaluation of six LLMs (CodeLlama, Codestral, StarChat2, Qwen-2.5, Olmo-3, and GPT-4o) across three datasets and two refactoring types, we find that LLMs show a non-trivial tendency to alter program semantics, producing 19-35% functionally non-equivalent refactorings. Our experiments further demonstrate that about 21% of these non-equivalent refactorings remain undetected by the existing test suites of the three evaluated datasets. Collectively, the findings of this study imply that reliance on existing tests might overestimate functional equivalence in LLM-generated code refactorings, which remain prone to semantic divergence.

## 2602.15763v1 — GLM-5: from Vibe Coding to Agentic Engineering

原始链接：https://arxiv.org/abs/2602.15763v1

Submitted UTC：2026-02-17T17:50:56Z；DOI Created UTC：2026-02-18T02:49:08Z。

We present GLM-5, a next-generation foundation model designed to transition the paradigm of vibe coding to agentic engineering. Building upon the agentic, reasoning, and coding (ARC) capabilities of its predecessor, GLM-5 adopts DSA to significantly reduce training and inference costs while maintaining long-context fidelity. To advance model alignment and autonomy, we implement a new asynchronous reinforcement learning infrastructure that drastically improves post-training efficiency by decoupling generation from training. Furthermore, we propose novel asynchronous agent RL algorithms that further improve RL quality, enabling the model to learn from complex, long-horizon interactions more effectively. Through these innovations, GLM-5 achieves state-of-the-art performance on major open benchmarks. Most critically, GLM-5 demonstrates unprecedented capability in real-world coding tasks, surpassing previous baselines in handling end-to-end software engineering challenges. Code, models, and more information are available at https://github.com/zai-org/GLM-5.

## 2602.15769v1 — ViTaB-A: Evaluating Multimodal Large Language Models on Visual Table Attribution

原始链接：https://arxiv.org/abs/2602.15769v1

Submitted UTC：2026-02-17T18:01:35Z；DOI Created UTC：2026-02-18T02:49:16Z。

Multimodal Large Language Models (mLLMs) are often used to answer questions in structured data such as tables in Markdown, JSON, and images. While these models can often give correct answers, users also need to know where those answers come from. In this work, we study structured data attribution/citation, which is the ability of the models to point to the specific rows and columns that support an answer. We evaluate several mLLMs across different table formats and prompting strategies. Our results show a clear gap between question answering and evidence attribution. Although question answering accuracy remains moderate, attribution accuracy is much lower, near random for JSON inputs, across all models. We also find that models are more reliable at citing rows than columns, and struggle more with textual formats than images. Finally, we observe notable differences across model families. Overall, our findings show that current mLLMs are unreliable at providing fine-grained, trustworthy attribution for structured data, which limits their usage in applications requiring transparency and traceability.

## 2602.15772v1 — Understanding vs. Generation: Navigating Optimization Dilemma in Multimodal Models

原始链接：https://arxiv.org/abs/2602.15772v1

Submitted UTC：2026-02-17T18:04:13Z；DOI Created UTC：2026-02-18T02:49:20Z。

Current research in multimodal models faces a key challenge where enhancing generative capabilities often comes at the expense of understanding, and vice versa. We analyzed this trade-off and identify the primary cause might be the potential conflict between generation and understanding, which creates a competitive dynamic within the model. To address this, we propose the Reason-Reflect-Refine (R3) framework. This innovative algorithm re-frames the single-step generation task into a multi-step process of "generate-understand-regenerate". By explicitly leveraging the model's understanding capability during generation, we successfully mitigate the optimization dilemma, achieved stronger generation results and improved understanding ability which are related to the generation process. This offers valuable insights for designing next-generation unified multimodal models. Code is available at https://github.com/sen-ye/R3.

## 2602.15776v1 — GlobeDiff: State Diffusion Process for Partial Observability in Multi-Agent Systems

原始链接：https://arxiv.org/abs/2602.15776v1

Submitted UTC：2026-02-17T18:05:48Z；DOI Created UTC：2026-02-18T02:49:26Z。

In the realm of multi-agent systems, the challenge of \emph{partial observability} is a critical barrier to effective coordination and decision-making. Existing approaches, such as belief state estimation and inter-agent communication, often fall short. Belief-based methods are limited by their focus on past experiences without fully leveraging global information, while communication methods often lack a robust model to effectively utilize the auxiliary information they provide. To solve this issue, we propose Global State Diffusion Algorithm~(GlobeDiff) to infer the global state based on the local observations. By formulating the state inference process as a multi-modal diffusion process, GlobeDiff overcomes ambiguities in state estimation while simultaneously inferring the global state with high fidelity. We prove that the estimation error of GlobeDiff under both unimodal and multi-modal distributions can be bounded. Extensive experimental results demonstrate that GlobeDiff achieves superior performance and is capable of accurately inferring the global state.

## 2602.15785v1 — This human study did not involve human subjects: Validating LLM simulations as behavioral evidence

原始链接：https://arxiv.org/abs/2602.15785v1

Submitted UTC：2026-02-17T18:18:38Z；DOI Created UTC：2026-02-18T02:49:38Z。

A growing literature uses large language models (LLMs) as synthetic participants to generate cost-effective and nearly instantaneous responses in social science experiments. However, there is limited guidance on when such simulations support valid inference about human behavior. We contrast two strategies for obtaining valid estimates of causal effects and clarify the assumptions under which each is suitable for exploratory versus confirmatory research. Heuristic approaches seek to establish that simulated and observed human behavior are interchangeable through prompt engineering, model fine-tuning, and other repair strategies designed to reduce LLM-induced inaccuracies. While useful for many exploratory tasks, heuristic approaches lack the formal statistical guarantees typically required for confirmatory research. In contrast, statistical calibration combines auxiliary human data with statistical adjustments to account for discrepancies between observed and simulated responses. Under explicit assumptions, statistical calibration preserves validity and provides more precise estimates of causal effects at lower cost than experiments that rely solely on human participants. Yet the potential of both approaches depends on how well LLMs approximate the relevant populations. We consider what opportunities are overlooked when researchers focus myopically on substituting LLMs for human participants in a study.

## 2602.15799v1 — The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety

原始链接：https://arxiv.org/abs/2602.15799v1

Submitted UTC：2026-02-17T18:39:15Z；DOI Created UTC：2026-02-18T02:49:57Z。

Fine-tuning aligned language models on benign tasks unpredictably degrades safety guardrails, even when training data contains no harmful content and developers have no adversarial intent. We show that the prevailing explanation, that fine-tuning updates should be orthogonal to safety-critical directions in high-dimensional parameter space, offers false reassurance: we show this orthogonality is structurally unstable and collapses under the dynamics of gradient descent. We then resolve this through a novel geometric analysis, proving that alignment concentrates in low-dimensional subspaces with sharp curvature, creating a brittle structure that first-order methods cannot detect or defend. While initial fine-tuning updates may indeed avoid these subspaces, the curvature of the fine-tuning loss generates second-order acceleration that systematically steers trajectories into alignment-sensitive regions. We formalize this mechanism through the Alignment Instability Condition, three geometric properties that, when jointly satisfied, lead to safety degradation. Our main result establishes a quartic scaling law: alignment loss grows with the fourth power of training time, governed by the sharpness of alignment geometry and the strength of curvature coupling between the fine-tuning task and safety-critical parameters. These results expose a structural blind spot in the current safety paradigm. The dominant approaches to safe fine-tuning address only the initial snapshot of a fundamentally dynamic problem. Alignment fragility is not a bug to be patched; it is an intrinsic geometric property of gradient descent on curved manifolds. Our results motivate the development of curvature-aware methods, and we hope will further enable a shift in alignment safety analysis from reactive red-teaming to predictive diagnostics for open-weight model deployment.

## 2602.15809v1 — Decision Quality Evaluation Framework at Pinterest

原始链接：https://arxiv.org/abs/2602.15809v1

Submitted UTC：2026-02-17T18:45:55Z；DOI Created UTC：2026-02-18T02:50:11Z。

Online platforms require robust systems to enforce content safety policies at scale. A critical component of these systems is the ability to evaluate the quality of moderation decisions made by both human agents and Large Language Models (LLMs). However, this evaluation is challenging due to the inherent trade-offs between cost, scale, and trustworthiness, along with the complexity of evolving policies. To address this, we present a comprehensive Decision Quality Evaluation Framework developed and deployed at Pinterest. The framework is centered on a high-trust Golden Set (GDS) curated by subject matter experts (SMEs), which serves as a ground truth benchmark. We introduce an automated intelligent sampling pipeline that uses propensity scores to efficiently expand dataset coverage. We demonstrate the framework's practical application in several key areas: benchmarking the cost-performance trade-offs of various LLM agents, establishing a rigorous methodology for data-driven prompt optimization, managing complex policy evolution, and ensuring the integrity of policy content prevalence metrics via continuous validation. The framework enables a shift from subjective assessments to a data-driven and quantitative practice for managing content safety systems.

## 2602.15813v1 — FAST-EQA: Efficient Embodied Question Answering with Global and Local Region Relevancy

原始链接：https://arxiv.org/abs/2602.15813v1

Submitted UTC：2026-02-17T18:49:43Z；DOI Created UTC：2026-02-18T02:50:16Z。

Embodied Question Answering (EQA) combines visual scene understanding, goal-directed exploration, spatial and temporal reasoning under partial observability. A central challenge is to confine physical search to question-relevant subspaces while maintaining a compact, actionable memory of observations. Furthermore, for real-world deployment, fast inference time during exploration is crucial. We introduce FAST-EQA, a question-conditioned framework that (i) identifies likely visual targets, (ii) scores global regions of interest to guide navigation, and (iii) employs Chain-of-Thought (CoT) reasoning over visual memory to answer confidently. FAST-EQA maintains a bounded scene memory that stores a fixed-capacity set of region-target hypotheses and updates them online, enabling robust handling of both single and multi-target questions without unbounded growth. To expand coverage efficiently, a global exploration policy treats narrow openings and doors as high-value frontiers, complementing local target seeking with minimal computation. Together, these components focus the agent's attention, improve scene coverage, and improve answer reliability while running substantially faster than prior approaches. On HMEQA and EXPRESS-Bench, FAST-EQA achieves state-of-the-art performance, while performing competitively on OpenEQA and MT-HM3D.

## 2602.15814v1 — Avey-B

原始链接：https://arxiv.org/abs/2602.15814v1

Submitted UTC：2026-02-17T18:50:40Z；DOI Created UTC：2026-02-18T02:50:18Z。

Compact pretrained bidirectional encoders remain the backbone of industrial NLP under tight compute and memory budgets. Their effectiveness stems from self-attention's ability to deliver high-quality bidirectional contextualization with sequence-level parallelism, as popularized by BERT-style architectures. Recently, Avey was introduced as an autoregressive, attention-free alternative that naturally admits an encoder-only adaptation. In this paper, we reformulate Avey for the encoder-only paradigm and propose several innovations to its architecture, including decoupled static and dynamic parameterizations, stability-oriented normalization, and neural compression. Results show that this reformulated architecture compares favorably to four widely used Transformer-based encoders, consistently outperforming them on standard token-classification and information-retrieval benchmarks while scaling more efficiently to long contexts.

## 2602.15816v1 — Developing AI Agents with Simulated Data: Why, what, and how?

原始链接：https://arxiv.org/abs/2602.15816v1

Submitted UTC：2026-02-17T18:53:27Z；DOI Created UTC：2026-02-18T02:50:21Z。

As insufficient data volume and quality remain the key impediments to the adoption of modern subsymbolic AI, techniques of synthetic data generation are in high demand. Simulation offers an apt, systematic approach to generating diverse synthetic data. This chapter introduces the reader to the key concepts, benefits, and challenges of simulation-based synthetic data generation for AI training purposes, and to a reference framework to describe, design, and analyze digital twin-based AI simulation solutions.

## 2602.15823v1 — CrispEdit: Low-Curvature Projections for Scalable Non-Destructive LLM Editing

原始链接：https://arxiv.org/abs/2602.15823v1

Submitted UTC：2026-02-17T18:58:04Z；DOI Created UTC：2026-02-18T02:50:30Z。

A central challenge in large language model (LLM) editing is capability preservation: methods that successfully change targeted behavior can quietly game the editing proxy and corrupt general capabilities, producing degenerate behaviors reminiscent of proxy/reward hacking. We present CrispEdit, a scalable and principled second-order editing algorithm that treats capability preservation as an explicit constraint, unifying and generalizing several existing editing approaches. CrispEdit formulates editing as constrained optimization and enforces the constraint by projecting edit updates onto the low-curvature subspace of the capability-loss landscape. At the crux of CrispEdit is expressing capability constraint via Bregman divergence, whose quadratic form yields the Gauss-Newton Hessian exactly and even when the base model is not trained to convergence. We make this second-order procedure efficient at the LLM scale using Kronecker-factored approximate curvature (K-FAC) and a novel matrix-free projector that exploits Kronecker structure to avoid constructing massive projection matrices. Across standard model-editing benchmarks, CrispEdit achieves high edit success while keeping capability degradation below 1% on average across datasets, significantly improving over prior editors.

## 2602.15829v1 — Operationalising the Superficial Alignment Hypothesis via Task Complexity

原始链接：https://arxiv.org/abs/2602.15829v1

Submitted UTC：2026-02-17T18:59:39Z；DOI Created UTC：2026-02-18T02:50:39Z。

The superficial alignment hypothesis (SAH) posits that large language models learn most of their knowledge during pre-training, and that post-training merely surfaces this knowledge. The SAH, however, lacks a precise definition, which has led to (i) different and seemingly orthogonal arguments supporting it, and (ii) important critiques to it. We propose a new metric called task complexity: the length of the shortest program that achieves a target performance on a task. In this framework, the SAH simply claims that pre-trained models drastically reduce the complexity of achieving high performance on many tasks. Our definition unifies prior arguments supporting the SAH, interpreting them as different strategies to find such short programs. Experimentally, we estimate the task complexity of mathematical reasoning, machine translation, and instruction following; we then show that these complexities can be remarkably low when conditioned on a pre-trained model. Further, we find that pre-training enables access to strong performances on our tasks, but it can require programs of gigabytes of length to access them. Post-training, on the other hand, collapses the complexity of reaching this same performance by several orders of magnitude. Overall, our results highlight that task adaptation often requires surprisingly little information -- often just a few kilobytes.
