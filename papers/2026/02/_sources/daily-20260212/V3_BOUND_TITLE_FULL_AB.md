# 本日有界新线索：精确 v1 完整题摘

来源：一次官方分类相关标题补检；仅下列20个家族的完整题摘，不是全部月表。作者原文字段以官方 exact-v1 abs 请求取得，current history仅身份/说明轻检。未授准入、日期落窗、评分或Books；不再追加同义发现查询。

## 2602.09448v1

请求：https://arxiv.org/abs/2602.09448v1；HTTP 200

Title: The Wisdom of Many Queries: Complexity-Diversity Principle for Dense Retriever Training

Abstract: Prior work reports conflicting results on query diversity in synthetic data generation for dense retrieval. We identify this conflict and design Q-D metrics to quantify diversity's impact, making the problem measurable. Through experiments on 4 benchmark types (31 datasets), we find query diversity especially benefits multi-hop retrieval. Deep analysis on multi-hop data reveals that diversity benefit correlates strongly with query complexity ($r$$\geq$0.95, $p$$&lt;$0.05 in 12/14 conditions), measured by content words (CW). We formalize this as the Complexity-Diversity Principle (CDP): query complexity determines optimal diversity. CDP provides actionable thresholds (CW$&gt;$10: use diversity; CW$&lt;$7: avoid it). Guided by CDP, we propose zero-shot multi-query synthesis for multi-hop tasks, achieving state-of-the-art performance.

Submission history From: Xincan Feng [ view email ] [v1] Tue, 10 Feb 2026 06:33:10 UTC (47 KB) [v2] Tue, 24 Feb 2026 15:35:33 UTC (50 KB) [v3] Thu, 26 Feb 2026 08:33:54 UTC (50 KB) [v4] Mon, 16 Mar 2026 12:57:55 UTC (50 KB)

## 2602.09616v1

请求：https://arxiv.org/abs/2602.09616v1；HTTP 200

Title: With Argus Eyes: Assessing Retrieval Gaps via Uncertainty Scoring to Detect and Remedy Retrieval Blind Spots

Abstract: Reliable retrieval-augmented generation (RAG) systems depend fundamentally on the retriever's ability to find relevant information. We show that neural retrievers used in RAG systems have blind spots, which we define as the failure to retrieve entities that are relevant to the query, but have low similarity to the query embedding. We investigate the training-induced biases that cause such blind spot entities to be mapped to inaccessible parts of the embedding space, resulting in low retrievability. Using a large-scale dataset constructed from Wikidata relations and first paragraphs of Wikipedia, and our proposed Retrieval Probability Score (RPS), we show that blind spot risk in standard retrievers (e.g., CONTRIEVER, REASONIR) can be predicted pre-index from entity embedding geometry, avoiding expensive retrieval evaluations. To address these blind spots, we introduce ARGUS, a pipeline that enables the retrievability of high-risk (low-RPS) entities through targeted document augmentation from a knowledge base (KB), first paragraphs of Wikipedia, in our case. Extensive experiments on BRIGHT, IMPLIRET, and RAR-B show that ARGUS achieves consistent improvements across all evaluated retrievers (averaging +3.4 nDCG@5 and +4.5 nDCG@10 absolute points), with substantially larger gains in challenging subsets. These results establish that preemptively remedying blind spots is critical for building robust and trustworthy RAG systems (Code and Data).

Submission history From: Zeinab Sadat Taghavi [ view email ] [v1] Tue, 10 Feb 2026 10:04:55 UTC (19,415 KB) [v2] Wed, 15 Jul 2026 08:11:18 UTC (15,986 KB)

## 2602.09229v1

请求：https://arxiv.org/abs/2602.09229v1；HTTP 200

Title: Beyond the Unit Hypersphere: Embedding Magnitude in Contrastive Learning

Abstract: Cosine similarity is prevalent in contrastive learning, yet it makes an implicit assumption: embedding magnitude is noise. Prior work occasionally found dot product and cosine similarity comparable, but left unanswered WHAT information magnitude carries, WHEN it helps, and HOW to leverage it. We conduct a systematic study through a $2 \times 2$ ablation that independently controls input-side and output-side normalization across text and vision models. Our findings reveal three key insights. First, in text retrieval, output (document) magnitude strongly correlates with relevance (Cohen's $d$ up to 1.80), yielding the largest gains on reasoning-intensive tasks. Second, input and output magnitudes serve asymmetric roles: output magnitude directly scales similarity scores while input magnitude modulates training dynamics. Third, magnitude learning benefits asymmetric tasks (text retrieval, RAG) but harms symmetric tasks (STS, text-image alignment). These findings establish a task symmetry principle: the choice between cosine and dot product depends on whether the task has distinct input roles, enabling cost-free improvements by simply removing an unnecessary constraint.

Submission history From: Xincan Feng [ view email ] [v1] Mon, 9 Feb 2026 21:53:23 UTC (94 KB) [v2] Thu, 5 Mar 2026 12:45:26 UTC (147 KB) [v3] Thu, 7 May 2026 19:21:00 UTC (143 KB)

## 2602.09764v1

请求：https://arxiv.org/abs/2602.09764v1；HTTP 200

Title: Self-Supervised Learning as Discrete Communication

Abstract: Most self-supervised learning (SSL) methods learn continuous visual representations by aligning different views of the same input, offering limited control over how information is structured across representation dimensions. In this work, we frame visual self-supervised learning as a discrete communication process between a teacher and a student network, where semantic information is transmitted through a fixed-capacity binary channel. Rather than aligning continuous features, the student predicts multi-label binary messages produced by the teacher. Discrete agreement is enforced through an element-wise binary cross-entropy objective, while a coding-rate regularization term encourages effective utilization of the constrained channel, promoting structured representations. We further show that periodically reinitializing the projection head strengthens this effect by encouraging embeddings that remain predictive across multiple discrete encodings. Extensive experiments demonstrate consistent improvements over continuous agreement baselines on image classification, retrieval, and dense visual prediction tasks, as well as under domain shift through self-supervised adaptation. Beyond backbone representations, we analyze the learned binary codes and show that they form a compact and informative discrete language, capturing semantic factors reusable across classes.

Submission history From: Kawtar Zaher [ view email ] [v1] Tue, 10 Feb 2026 13:24:06 UTC (4,005 KB) [v2] Mon, 15 Jun 2026 12:48:13 UTC (4,222 KB)

## 2602.10024v1

请求：https://arxiv.org/abs/2602.10024v1；HTTP 200

Title: Overview of the TREC 2025 RAGTIME Track

Abstract: The principal goal of the RAG TREC Instrument for Multilingual Evaluation (RAGTIME) track at TREC is to study report generation from multilingual source documents. The track has created a document collection containing Arabic, Chinese, English, and Russian news stories. RAGTIME includes three task types: Multilingual Report Generation, English Report Generation, and Multilingual Information Retrieval (MLIR). A total of 125 runs were submitted by 13 participating teams (and as baselines by the track coordinators) for three tasks. This overview describes these three tasks and presents the available results.

Submission history From: Eugene Yang [ view email ] [v1] Tue, 10 Feb 2026 17:47:20 UTC (248 KB) [v2] Fri, 8 May 2026 04:11:25 UTC (215 KB)

## 2602.09552v1

请求：https://arxiv.org/abs/2602.09552v1；HTTP 200

Title: Comprehensive Comparison of RAG Methods Across Multi-Domain Conversational QA

Abstract: Conversational question answering increasingly relies on retrieval-augmented generation (RAG) to ground large language models (LLMs) in external knowledge. Yet, most existing studies evaluate RAG methods in isolation and primarily focus on single-turn settings. This paper addresses the lack of a systematic comparison of RAG methods for multi-turn conversational QA, where dialogue history, coreference, and shifting user intent substantially complicate retrieval. We present a comprehensive empirical study of vanilla and advanced RAG methods across eight diverse conversational QA datasets spanning multiple domains. Using a unified experimental setup, we evaluate retrieval quality and answer generation using generator and retrieval metrics, and analyze how performance evolves across conversation turns. Our results show that robust yet straightforward methods, such as reranking, hybrid BM25, and HyDE, consistently outperform vanilla RAG. In contrast, several advanced techniques fail to yield gains and can even degrade performance below the No-RAG baseline. We further demonstrate that dataset characteristics and dialogue length strongly influence retrieval effectiveness, explaining why no single RAG strategy dominates across settings. Overall, our findings indicate that effective conversational RAG depends less on method complexity than on alignment between the retrieval strategy and the dataset structure. We publish the code used.\footnote{\href{ this https URL }{GitHub Repository}}

Submission history From: Jan Strich [ view email ] [v1] Tue, 10 Feb 2026 08:59:23 UTC (2,144 KB)

## 2602.09801v1

请求：https://arxiv.org/abs/2602.09801v1；HTTP 200

Title: Tiny Moves: Game-based Hypothesis Refinement

Abstract: Most machine learning approaches to scientific discovery frame hypotheses as end-to-end predictions, obscuring the incremental structure of scientific reasoning. We propose The Hypothesis Game, a symbolic formalism for hypothesis refinement in which LLM agents operate on a shared hypothesis state using a fixed grammar of reasoning moves. The framework is motivated by the observation that scientific progress often proceeds through small, localized revisions, grounded in domain context, rather than extensive rewrites. We instantiate a minimal game with LLM agents and evaluate it on pathway-level mechanistic refinement tasks. In the primary setting of corruption recovery, where hypotheses contain controlled errors, the game-based approach consistently removes more errors and achieves higher precision than strong prompting baselines, while preserving valid structure through incremental edits. In a secondary reconstruction setting from partial cues, it performs comparably to the strongest baseline, indicating that explicit move-based refinement remains competitive even when ground-truth recovery is difficult. These findings support game-based reasoning as a principled route to more controllable, interpretable, and transferable hypothesis refinement systems for scientific discovery.

Submission history From: Anna Gogleva [ view email ] [v1] Tue, 10 Feb 2026 14:04:29 UTC (2,159 KB)

## 2602.09270v1

请求：https://arxiv.org/abs/2602.09270v1；HTTP 200

Title: Collective Behavior of AI Agents: the Case of Moltbook

Abstract: We present a large scale data analysis of Moltbook, a Reddit-style social media platform exclusively populated by AI agents. Analyzing over 369,000 posts and 3.0 million comments from approximately 46,000 active agents, we find that AI collective behavior exhibits many of the same statistical regularities observed in human online communities: heavy-tailed distributions of activity, power-law scaling of popularity metrics, and temporal decay patterns consistent with limited attention dynamics. However, we also identify key differences, including a sublinear relationship between upvotes and discussion size that contrasts with human behavior. These findings suggest that, while individual AI agents may differ fundamentally from humans, their emergent collective dynamics share structural similarities with human social systems.

Submission history From: Giordano De Marzo [ view email ] [v1] Mon, 9 Feb 2026 23:10:34 UTC (88 KB)

## 2602.09170v1

请求：https://arxiv.org/abs/2602.09170v1；HTTP 200

Title: Quantifying Epistemic Uncertainty in Diffusion Models

Abstract: To ensure high quality outputs, it is important to quantify the epistemic uncertainty of diffusion models. Existing methods are often unreliable because they mix epistemic and aleatoric uncertainty. We introduce a method based on Fisher information that explicitly isolates epistemic variance, producing more reliable plausibility scores for generated data. To make this approach scalable, we propose FLARE (Fisher-Laplace Randomized Estimator), which approximates the Fisher information using a uniformly random subset of model parameters. Empirically, FLARE improves uncertainty estimation in synthetic time-series generation tasks, achieving more accurate and reliable filtering than other methods. Theoretically, we bound the convergence rate of our randomized approximation and provide analytic and empirical evidence that last-layer Laplace approximations are insufficient for this task.

Submission history From: N. Benjamin Erichson [ view email ] [v1] Mon, 9 Feb 2026 20:22:33 UTC (2,670 KB)

## 2602.09276v1

请求：https://arxiv.org/abs/2602.09276v1；HTTP 200

Title: Effective Reasoning Chains Reduce Intrinsic Dimensionality

Abstract: Chain-of-thought (CoT) reasoning and its variants have substantially improved the performance of language models on complex reasoning tasks, yet the precise mechanisms by which different strategies facilitate generalization remain poorly understood. While current explanations often point to increased test-time computation or structural guidance, establishing a consistent, quantifiable link between these factors and generalization remains challenging. In this work, we identify intrinsic dimensionality as a quantitative measure for characterizing the effectiveness of reasoning chains. Intrinsic dimensionality quantifies the minimum number of model dimensions needed to reach a given accuracy threshold on a given task. By keeping the model architecture fixed and varying the task formulation through different reasoning strategies, we demonstrate that effective reasoning strategies consistently reduce the intrinsic dimensionality of the task. Validating this on GSM8K with Gemma-3 1B and 4B, we observe a strong inverse correlation between the intrinsic dimensionality of a reasoning strategy and its generalization performance on both in-distribution and out-of-distribution data. Our findings suggest that effective reasoning chains facilitate learning by better compressing the task using fewer parameters, offering a new quantitative metric for analyzing reasoning processes.

Submission history From: Archiki Prasad [ view email ] [v1] Mon, 9 Feb 2026 23:32:12 UTC (848 KB) [v2] Thu, 28 May 2026 19:23:27 UTC (853 KB)

## 2602.09331v1

请求：https://arxiv.org/abs/2602.09331v1；HTTP 200

Title: Beyond Uniform Credit: Causal Credit Assignment for Policy Optimization

Abstract: Policy gradient methods for language model reasoning, such as GRPO and DAPO, assign uniform credit to all generated tokens - the filler phrase &#34;Let me think&#34; receives the same gradient update as the critical calculation &#34;23 + 45 = 68.&#34; We propose counterfactual importance weighting: mask reasoning spans, measure the drop in answer probability, and upweight tokens accordingly during policy gradient updates. Our method requires no auxiliary models or external annotation, instead importance is estimated directly from the policy model's own probability shifts. Experiments on GSM8K across three models spanning the Qwen and Llama families demonstrate consistent improvements over uniform baselines and faster convergence to equivalent accuracy. Inverting the importance signal hurts performance, confirming we capture genuine causal structure rather than noise. Analysis shows the method correctly prioritizes calculation steps over scaffolding text. We view these findings as establishing counterfactual importance weighting as a foundation for further research rather than a complete solution.

Submission history From: Mykola Khandoga [ view email ] [v1] Tue, 10 Feb 2026 01:57:02 UTC (497 KB)

## 2602.09394v1

请求：https://arxiv.org/abs/2602.09394v1；HTTP 200

Title: The Critical Horizon: Inspection Design Principles for Multi-Stage Operations and Deep Reasoning

Abstract: Manufacturing lines, service journeys, supply chains, and AI reasoning chains share a common challenge: attributing a terminal outcome to the intermediate stage that caused it. We establish an information-theoretic barrier to this credit assignment problem: the signal connecting early steps to final outcomes decays exponentially with depth, creating a critical horizon beyond which no algorithm can learn from endpoint data alone. We prove four results. First, a Signal Decay Bound: sample complexity for attributing outcomes to early stages grows exponentially in the number of intervening steps. Second, Width Limits: parallel rollouts provide only logarithmic relief, with correlation capping the effective number of independent samples. Third, an Objective Mismatch: additive reward aggregation optimizes the wrong quantity when sequential validity requires all steps to be correct. Fourth, Optimal Inspection Design: uniform checkpoint spacing is minimax-optimal under homogeneous signal attenuation, while a greedy algorithm yields optimal non-uniform schedules under heterogeneous attenuation. Together, these results provide a common analytical foundation for inspection design in operations and supervision design in AI.

Submission history From: Seyed Morteza Emadi [ view email ] [v1] Tue, 10 Feb 2026 04:02:29 UTC (138 KB) [v2] Fri, 13 Feb 2026 00:34:46 UTC (142 KB)

## 2602.09413v1

请求：https://arxiv.org/abs/2602.09413v1；HTTP 200

Title: LARV: Data-Free Layer-wise Adaptive Rescaling Veneer for Model Merging

Abstract: Model merging aims to combine multiple fine-tuned models into a single multi-task model without access to training data. Existing task-vector merging methods such as TIES, TSV-M, and Iso-C/CTS differ in their aggregation rules but treat all layers nearly uniformly. This assumption overlooks the strong layer-wise heterogeneity in large vision transformers, where shallow layers are sensitive to interference while deeper layers encode stable task-specific features. We introduce LARV, a training-free, data-free, merger-agnostic Layer-wise Adaptive Rescaling Veneer that plugs into any task-vector merger and assigns a per-layer scale to each task vector before aggregation, and show it consistently boosts diverse merging rules. LARV adaptively suppresses shallow-layer interference and amplifies deeper-layer alignment using a simple deterministic schedule, requiring no retraining or modification to existing mergers. To our knowledge, this is the first work to perform layer-aware scaling for task-vector merging. LARV computes simple data-free layer proxies and turns them into scales through a lightweight rule; we study several instantiations within one framework (e.g., tiered two/three-level scaling with fixed values, or continuous mappings) and show that tiered choices offer the best robustness, while continuous mappings remain an ablation. LARV is orthogonal to the base merger and adds negligible cost. On FusionBench with Vision Transformers, LARV consistently improves all task-vector baselines across 8/14/20-task settings; for example, Iso-C + LARV reaches 85.9% on ViT-B/32, 89.2% on ViT-B/16, and 92.6% on ViT-L/14. Layerwise analysis and corruption tests further indicate that LARV suppresses shallow-layer interference while modestly amplifying deeper, task-stable features, turning model merging into a robust, layer-aware procedure rather than a uniform one.

Submission history From: Xinyu Wang [ view email ] [v1] Tue, 10 Feb 2026 05:10:31 UTC (4,477 KB)

## 2602.09621v1

请求：https://arxiv.org/abs/2602.09621v1；HTTP 200

Title: AlignTune: Modular Toolkit for Post-Training Alignment of Large Language Models

Abstract: Post-training alignment is central to deploying large language models (LLMs), yet practical workflows remain split across backend-specific tools and ad-hoc glue code, making experiments hard to reproduce. We identify backend interference, reward fragmentation, and irreproducible pipelines as key obstacles in alignment research. We introduce AlignTune, a modular toolkit exposing a unified interface for supervised fine-tuning (SFT) and RLHF-style optimization with interchangeable TRL and Unsloth backends. AlignTune standardizes configuration, provides an extensible reward layer (rule-based and learned), and integrates evaluation over standard benchmarks and custom tasks. By isolating backend-specific logic behind a single factory boundary, AlignTune enables controlled comparisons and reproducible alignment experiments.

Submission history From: Pratinav Seth [ view email ] [v1] Tue, 10 Feb 2026 10:08:51 UTC (11,764 KB) [v2] Wed, 11 Feb 2026 18:51:19 UTC (11,765 KB)

## 2602.09805v1

请求：https://arxiv.org/abs/2602.09805v1；HTTP 200

Title: Decomposing Reasoning Efficiency in Large Language Models

Abstract: Large language models trained for reasoning trade off inference tokens against accuracy, yet standard evaluations report only final accuracy, obscuring where tokens are spent or wasted. We introduce a trace-optional framework that decomposes token efficiency into interpretable factors: completion under a fixed token budget (avoiding truncation), conditional correctness given completion, and verbosity (token usage). When benchmark metadata provides per-instance workload proxies, we further factor verbosity into two components: mean verbalization overhead (tokens per work unit) and a coupling coefficient capturing how overhead scales with task workload. When reasoning traces are available, we add deterministic trace-quality measures (grounding, repetition, prompt copying) to separate degenerate looping from verbose-but-engaged reasoning, avoiding human labeling and LLM judges. Evaluating 25 models on CogniLoad, we find that accuracy and token-efficiency rankings diverge (Spearman $\rho=0.63$), efficiency gaps are often driven by conditional correctness, and verbalization overhead varies by about 9 times (only weakly related to model scale). Our decomposition reveals distinct bottleneck profiles that suggest different efficiency interventions.

Submission history From: Daniel Kaiser [ view email ] [v1] Tue, 10 Feb 2026 14:09:18 UTC (150 KB) [v2] Mon, 18 May 2026 15:01:48 UTC (150 KB)

## 2602.09842v1

请求：https://arxiv.org/abs/2602.09842v1；HTTP 200

Title: Step-Size Stability in Stochastic Optimization: A Theoretical Perspective

Abstract: We present a theoretical analysis of stochastic optimization methods in terms of their sensitivity with respect to the step size. We identify a key quantity that, for each method, describes how the performance degrades as the step size becomes too large. For convex problems, we show that this quantity directly impacts the suboptimality bound of the method. Most importantly, our analysis provides direct theoretical evidence that adaptive step-size methods, such as SPS or NGN, are more robust than SGD. This allows us to quantify the advantage of these adaptive methods beyond empirical evaluation. Finally, we show through experiments that our theoretical bound qualitatively mirrors the actual performance as a function of the step size, even for nonconvex problems.

Submission history From: Fabian Schaipp [ view email ] [v1] Tue, 10 Feb 2026 14:46:14 UTC (6,625 KB) [v2] Tue, 26 May 2026 14:40:02 UTC (6,645 KB)

## 2602.09891v1

请求：https://arxiv.org/abs/2602.09891v1；HTTP 200

Title: Stemphonic: All-at-once Flexible Multi-stem Music Generation

Abstract: Music stem generation, the task of producing musically-synchronized and isolated instrument audio clips, offers the potential of greater user control and better alignment with musician workflows compared to conventional text-to-music models. Existing stem generation approaches, however, either rely on fixed architectures that output a predefined set of stems in parallel, or generate only one stem at a time, resulting in slow inference despite flexibility in stem combination. We propose Stemphonic, a diffusion-/flow-based framework that overcomes this trade-off and generates a variable set of synchronized stems in one inference pass. During training, we treat each stem as a batch element, group synchronized stems in a batch, and apply a shared noise latent to each group. At inference-time, we use a shared initial noise latent and stem-specific text inputs to generate synchronized multi-stem outputs in one pass. We further expand our approach to enable one-pass conditional multi-stem generation and stem-wise activity controls to empower users to iteratively generate and orchestrate the temporal layering of a mix. We benchmark our results on multiple open-source stem evaluation sets and show that Stemphonic produces higher-quality outputs while accelerating the full mix generation process by 25 to 50%. Demos at: this https URL .

Submission history From: Shih-Lun Wu [ view email ] [v1] Tue, 10 Feb 2026 15:30:12 UTC (864 KB)

## 2602.09983v1

请求：https://arxiv.org/abs/2602.09983v1；HTTP 200

Title: Coupled Inference in Diffusion Models for Semantic Decomposition

Abstract: Many visual scenes can be described as compositions of latent factors. Effective recognition, reasoning, and editing often require not only forming such compositional representations, but also solving the decomposition problem. One popular choice for constructing these representations is through the binding operation. Resonator networks, which can be understood as coupled Hopfield networks, were proposed as a way to perform decomposition on such bound representations. Recent works have shown notable similarities between Hopfield networks and diffusion models. Motivated by these observations, we introduce a framework for semantic decomposition using coupled inference in diffusion models. Our method frames semantic decomposition as an inverse problem and couples the diffusion processes using a reconstruction-driven guidance term that encourages the composition of factor estimates to match the bound vector. We also introduce a novel iterative sampling scheme that improves the performance of our model. Finally, we show that attention-based resonator networks are a special case of our framework. Empirically, we demonstrate that our coupled inference framework outperforms resonator networks across a range of synthetic semantic decomposition tasks.

Submission history From: Chun Ho Calvin Yeung [ view email ] [v1] Tue, 10 Feb 2026 17:10:05 UTC (1,891 KB)

## 2602.10058v1

请求：https://arxiv.org/abs/2602.10058v1；HTTP 200

Title: Evaluating Disentangled Representations for Controllable Music Generation

Abstract: Recent approaches in music generation rely on disentangled representations, often labeled as structure and timbre or local and global, to enable controllable synthesis. Yet the underlying properties of these embeddings remain underexplored. In this work, we evaluate such disentangled representations in a set of music audio models for controllable generation using a probing-based framework that goes beyond standard downstream tasks. The selected models reflect diverse unsupervised disentanglement strategies, including inductive biases, data augmentations, adversarial objectives, and staged training procedures. We further isolate specific strategies to analyze their effect. Our analysis spans four key axes: informativeness, equivariance, invariance, and disentanglement, which are assessed across datasets, tasks, and controlled transformations. Our findings reveal inconsistencies between intended and actual semantics of the embeddings, suggesting that current strategies fall short of producing truly disentangled representations, and prompting a re-examination of how controllability is approached in music generation.

Submission history From: Laura Ibáñez Martínez [ view email ] [v1] Tue, 10 Feb 2026 18:25:04 UTC (31 KB) [v2] Sun, 15 Feb 2026 20:31:32 UTC (31 KB)

## 2602.09533v1

请求：https://arxiv.org/abs/2602.09533v1；HTTP 200

Title: Autoregressive Direct Preference Optimization

Abstract: Direct preference optimization (DPO) has emerged as a promising approach for aligning large language models (LLMs) with human preferences. However, the widespread reliance on the response-level Bradley-Terry (BT) model may limit its full potential, as the reference and learnable models are assumed to be autoregressive only after deriving the objective function. Motivated by this limitation, we revisit the theoretical foundations of DPO and propose a novel formulation that explicitly introduces the autoregressive assumption prior to applying the BT model. By reformulating and extending DPO, we derive a novel variant, termed Autoregressive DPO (ADPO), that explicitly integrates autoregressive modeling into the preference optimization framework. Without violating the theoretical foundations, the derived loss takes an elegant form: it shifts the summation operation in the DPO objective outside the log-sigmoid function. Furthermore, through theoretical analysis of ADPO, we show that there exist two length measures to be considered when designing DPO-based algorithms: the token length $\mu$ and the feedback length $\mu$'. To the best of our knowledge, we are the first to explicitly distinguish these two measures and analyze their implications for preference optimization in LLMs.

Submission history From: Masanari Oi [ view email ] [v1] Tue, 10 Feb 2026 08:45:30 UTC (1,968 KB) [v2] Wed, 10 Jun 2026 06:12:57 UTC (1,968 KB)

