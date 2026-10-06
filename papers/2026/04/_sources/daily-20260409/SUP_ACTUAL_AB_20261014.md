# Apr09第二批官方AB只读恢复

### Phase-Associative Memory: Sequence Modeling in Complex Hilbert Space — actual official AB

URL：https://arxiv.org/abs/2604.05030v1；本轮Node fetch HTTP200，41659字符；完整题摘已实际读，不作Source完成或first-public证明。

Abstract: We present Phase-Associative Memory (PAM), a recurrent sequence model in which all representations are complex-valued, associations accumulate in a matrix state $S_{t}$ $\in$ $\mathbb{C}^{d \times d}$ via outer products, and retrieval operates through the conjugate inner product $K_t^* \cdot Q_t / \sqrt{d}$. At $\sim$100M parameters on WikiText-103, PAM reaches validation perplexity 30.0, within $\sim$10\% of a matched transformer (27.1) trained under identical conditions, despite $4\times$ arithmetic overhead from complex computation and no custom kernels. We trace the experimental path from vector-state models, where holographic binding fails due to the $O(1/\sqrt{n})$ capacity degradation of superposed associations, to the matrix state that resolves it. The competitiveness of an architecture whose native operations are complex-valued superposition and conjugate retrieval is consistent with recent empirical evidence that semantic interpretation in both humans and large language models exhibits non-classical contextuality, and we discuss what this implies for the choice of computational formalism in language modeling.

原始字段：Submission history From: Christopher Agostino PhD [ view email ] [v1] Mon, 6 Apr 2026 18:00:03 UTC (42 KB) [v2] Tue, 28 Apr 2026 16:30:21 UTC (307 KB)

某并发请求20秒有界fetch失败；已通过web读取的精确URL按相应具名条目保留，不由空响应证明零命中。

### Hierarchical Contrastive Learning for Multimodal Data — actual official AB

URL：https://arxiv.org/abs/2604.05462v1；本轮Node fetch HTTP200，41525字符；完整题摘已实际读，不作Source完成或first-public证明。

Abstract: Multimodal representation learning is commonly built on a shared-private decomposition, treating latent information as either common to all modalities or specific to one. This binary view is often inadequate: many factors are shared by only subsets of modalities, and ignoring such partial sharing can over-align unrelated signals and obscure complementary information. We propose Hierarchical Contrastive Learning (HCL), a framework that learns globally shared, partially shared, and modality-specific representations within a unified model. HCL combines a hierarchical latent-variable formulation with structural sparsity and a structure-aware contrastive objective that aligns only modalities that genuinely share a latent factor. Under uncorrelated latent variables, we prove identifiability of the hierarchical decomposition, establish recovery guarantees for the loading matrices, and derive parameter estimation and excess-risk bounds for downstream prediction. Simulations show accurate recovery of hierarchical structure and effective selection of task-relevant components. On multimodal electronic health records, HCL yields more informative representations and consistently improves predictive performance.

原始字段：Submission history From: Huichao Li [ view email ] [v1] Tue, 7 Apr 2026 05:53:04 UTC (681 KB)

某并发请求20秒有界fetch失败；已通过web读取的精确URL按相应具名条目保留，不由空响应证明零命中。

某并发请求20秒有界fetch失败；已通过web读取的精确URL按相应具名条目保留，不由空响应证明零命中。

某并发请求20秒有界fetch失败；已通过web读取的精确URL按相应具名条目保留，不由空响应证明零命中。

### Fine-Grained Power and Energy Attribution on AMD GPU/APU-Based Exascale Nodes — actual official AB

URL：https://arxiv.org/abs/2604.06056v1；本轮Node fetch HTTP200，43001字符；完整题摘已实际读，不作Source完成或first-public证明。

Abstract: Modern exascale GPU- and APU-based systems provide multiple power and energy sensors, but differences in scope, update rate, timing, and filtering complicate the attribution of short-lived accelerator activity. This paper presents a methodology to characterize and correct these effects on Cray EX systems with AMD Instinct MI250X GPUs (Frontier) and MI300A APUs (Portage). Using controlled square-wave workloads, we quantify update intervals, delay, aliasing, and variability across up to 512 GPUs and 480 APUs with on-chip (rocm-smi/amd-smi) and off-chip Cray Power Management sensors. We reconstruct power from cumulative energy counters to achieve faster response times, validate it against on-chip, off-chip, and node-level sensors, and integrate the resulting streams into a Score-P/PAPI-based tool for time-aligned, phase-level attribution. Applied to rocHPL, rocHPL-MxP, and HPG-MxP, the method separates energy savings due to reduced runtime from changes in power. Mixed precision reduces node energy on Frontier by 79% for rocHPL-MxP and 31% for HPG-MxP, with similar trends on Portage. These results provide portable guidance for sensor validation and power-aware optimization on current and future exascale systems.

原始字段：Submission history From: Wael Elwasif [ view email ] [v1] Tue, 7 Apr 2026 16:42:47 UTC (10,563 KB) [v2] Thu, 9 Apr 2026 20:44:46 UTC (10,608 KB)

### From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection — actual official AB

URL：https://arxiv.org/abs/2604.06066v1；本轮Node fetch HTTP200，41692字符；完整题摘已实际读，不作Source完成或first-public证明。

Abstract: Intrinsic self-correction in Large Language Models (LLMs) frequently fails in open-ended reasoning tasks due to ``hallucination snowballing,&#39;&#39; a phenomenon in which models recursively justify early errors during free-text reflection. While structured feedback can mitigate this issue, existing approaches often rely on externally trained critics or symbolic tools, reducing agent autonomy. This study investigates whether enforcing structured reflection purely through Outlines-based constrained decoding can disrupt error propagation without additional training. Evaluating an 8-billion-parameter model (Qwen3-8B), we show that simply imposing structural constraints does not improve self-correction performance. Instead, it triggers a new failure mode termed ``structure snowballing.&#39;&#39; We find that the cognitive load required to satisfy strict formatting rules pushes the model into formatting traps. This observation helps explain why the agent achieves near-perfect superficial syntactic alignment yet fails to detect or resolve deeper semantic errors. These findings expose an ``alignment tax&#39;&#39; inherent to constrained decoding, highlighting a tension between structural granularity and internal model capacity in autonomous workflows. Code and raw logs are available in the GitHub repository: this https URL .

原始字段：Submission history From: Hongxu Zhou [ view email ] [v1] Tue, 7 Apr 2026 16:47:37 UTC (398 KB)

某并发请求20秒有界fetch失败；已通过web读取的精确URL按相应具名条目保留，不由空响应证明零命中。

某并发请求20秒有界fetch失败；已通过web读取的精确URL按相应具名条目保留，不由空响应证明零命中。

