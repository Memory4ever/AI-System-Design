# 2026-02-19 V3 日期独立发现与筛选

窗口：[2026-02-18T09:00:00+08:00, 2026-02-19T09:00:00+08:00)。

旧 inventory 仅身份/题摘线索；旧 Updated/相邻 ID 归属和 364/6 完成断言不继承。以下是本次实际读取的完整题摘，未核定落窗者不进入确定候选；EX 不追无关日期。原始字段保持原值。

## 首批准入校准输入

### 2602.15034v1 — EduResearchBench: A Hierarchical Atomic Task Decomposition Benchmark for Full-Lifecycle Educational Research

原始链接：https://arxiv.org/abs/2602.15034v1

Submitted UTC：2026-01-22T09:52:30Z；DOI Created UTC：2026-02-18T02:32:11Z（后者不是首公开时刻）。

While Large Language Models (LLMs) are reshaping the paradigm of AI for Social Science (AI4SS), rigorously evaluating their capabilities in scholarly writing remains a major challenge. Existing benchmarks largely emphasize single-shot, monolithic generation and thus lack the fine-grained assessments required to reflect complex academic research workflows. To fill this gap, we introduce EduResearchBench, the first comprehensive evaluation platform dedicated to educational academic writing. EduResearchBench is built upon our Hierarchical Atomic Task Decomposition (HATD) framework, which decomposes an end-to-end research workflow into six specialized research modules (e.g., Quantitative Analysis, Qualitative Research, and Policy Research) spanning 24 fine-grained atomic tasks. This taxonomy enables an automated evaluation pipeline that mitigates a key limitation of holistic scoring, where aggregate scores often obscure specific capability bottlenecks, and instead provides fine-grained, diagnostic feedback on concrete deficiencies. Moreover, recognizing the high cognitive load inherent in scholarly writing, we propose a curriculum learning strategy that progressively builds competence from foundational skills to complex methodological reasoning and argumentation. Leveraging 55K raw academic samples, we curate 11K high-quality instruction pairs to train EduWrite, a specialized educational scholarly writing model. Experiments show that EduWrite (30B) substantially outperforms larger general-purpose models (72B) on multiple core metrics, demonstrating that in vertical domains, data quality density and hierarchically staged training curricula are more decisive than parameter scale.

### 2602.15091v1 — Mixture-of-Experts under Finite-Rate Gating: Communication--Generalization Trade-offs

原始链接：https://arxiv.org/abs/2602.15091v1

Submitted UTC：2026-02-16T17:26:12Z；DOI Created UTC：2026-02-18T02:33:30Z（后者不是首公开时刻）。

Mixture-of-Experts (MoE) architectures decompose prediction tasks into specialized expert sub-networks selected by a gating mechanism. This letter adopts a communication-theoretic view of MoE gating, modeling the gate as a stochastic channel operating under a finite information rate. Within an information-theoretic learning framework, {we specialize a mutual-information generalization bound and develop a rate-distortion characterization $D(R_g)$ of finite-rate gating, where $R_g:=I(X; T)$, yielding (under a standard empirical rate-distortion optimality condition) $\mathbb{E}[R(W)] \le D(R_g)+δ_m+\sqrt{(2/m)\, I(S; W)}$. }The analysis yields capacity-aware limits for communication-constrained MoE systems, and numerical simulations on synthetic multi-expert models empirically confirm the predicted trade-offs between gating rate, expressivity, and generalization.

### 2602.15156v1 — Panini: Continual Learning in Token Space via Structured Memory

原始链接：https://arxiv.org/abs/2602.15156v1

Submitted UTC：2026-02-16T19:58:03Z；DOI Created UTC：2026-02-18T02:35:00Z（后者不是首公开时刻）。

Language models are increasingly used to reason over content they were not trained on, such as new documents, evolving knowledge, and user-specific data. A common approach is retrieval-augmented generation (RAG), which stores verbatim documents externally (as chunks) and retrieves only a relevant subset at inference time for an LLM to reason over. However, this results in inefficient usage of test-time compute (LLM repeatedly reasons over the same documents); moreover, chunk retrieval can inject irrelevant context that increases unsupported generation. We propose a human-like non-parametric continual learning framework, where the base model remains fixed, and learning occurs by integrating each new experience into an external semantic memory state that accumulates and consolidates itself continually. We present Panini, which realizes this by representing documents as Generative Semantic Workspaces (GSW) -- an entity- and event-aware network of question-answer (QA) pairs, sufficient for an LLM to reconstruct the experienced situations and mine latent knowledge via reasoning-grounded inference chains on the network. Given a query, Panini only traverses the continually-updated GSW (not the verbatim documents or chunks), and retrieves the most likely inference chains. Across six QA benchmarks, Panini achieves the highest average performance, 5%-7% higher than other competitive baselines, while using 2-30x fewer answer-context tokens, supports fully open-source pipelines, and reduces unsupported answers on curated unanswerable queries. The results show that efficient and accurate structuring of experiences at write time -- as achieved by the GSW framework -- yields both efficiency and reliability gains at read time. Code is available at https://github.com/roychowdhuryresearch/gsw-memory.

### 2602.15197v1 — OpaqueToolsBench: Learning Nuances of Tool Behavior Through Interaction

原始链接：https://arxiv.org/abs/2602.15197v1

Submitted UTC：2026-02-16T21:26:37Z；DOI Created UTC：2026-02-18T02:35:57Z（后者不是首公开时刻）。

Tool-calling is essential for Large Language Model (LLM) agents to complete real-world tasks. While most existing benchmarks assume simple, perfectly documented tools, real-world tools (e.g., general "search" APIs) are often opaque, lacking clear best practices or failure modes. Can LLM agents improve their performance in environments with opaque tools by interacting and subsequently improving documentation? To study this, we create OpaqueToolsBench, a benchmark consisting of three distinct task-oriented environments: general function calling, interactive chess playing, and long-trajectory agentic search. Each environment provides underspecified tools that models must learn to use effectively to complete the task. Results on OpaqueToolsBench suggest existing methods for automatically documenting tools are expensive and unreliable when tools are opaque. To address this, we propose a simple framework, ToolObserver, that iteratively refines tool documentation by observing execution feedback from tool-calling trajectories. Our approach outperforms existing methods on OpaqueToolsBench across datasets, even in relatively hard settings. Furthermore, for test-time tool exploration settings, our method is also efficient, consuming 3.5-7.5x fewer total tokens than the best baseline.

### 2602.15200v1 — COMPOT: Calibration-Optimized Matrix Procrustes Orthogonalization for Transformers Compression

原始链接：https://arxiv.org/abs/2602.15200v1

Submitted UTC：2026-02-16T21:31:34Z；DOI Created UTC：2026-02-18T02:36:02Z（后者不是首公开时刻）。

Post-training compression of Transformer models commonly relies on truncated singular value decomposition (SVD). However, enforcing a single shared subspace can degrade accuracy even at moderate compression. Sparse dictionary learning provides a more flexible union-of-subspaces representation, but existing approaches often suffer from iterative dictionary and coefficient updates. We propose COMPOT (Calibration-Optimized Matrix Procrustes Orthogonalization for Transformers), a training-free compression framework that uses a small calibration dataset to estimate a sparse weight factorization. COMPOT employs orthogonal dictionaries that enable closed-form Procrustes updates for the dictionary and analytical single-step sparse coding for the coefficients, eliminating iterative optimization. To handle heterogeneous layer sensitivity under a global compression budget, COMPOT further introduces a one-shot dynamic allocation strategy that adaptively redistributes layer-wise compression rates. Extensive experiments across diverse architectures and tasks show that COMPOT consistently delivers a superior quality-compression trade-off over strong low-rank and sparse baselines, while remaining fully compatible with post-training quantization for extreme compression. Code is available $\href{https://github.com/mts-ai/COMPOT}{here}$.

### 2602.15222v1 — Automatically Finding Reward Model Biases

原始链接：https://arxiv.org/abs/2602.15222v1

Submitted UTC：2026-02-16T22:05:44Z；DOI Created UTC：2026-02-18T02:36:32Z（后者不是首公开时刻）。

Reward models are central to large language model (LLM) post-training. However, past work has shown that they can reward spurious or undesirable attributes such as length, format, hallucinations, and sycophancy. In this work, we introduce and study the research problem of automatically finding reward model biases in natural language. We offer a simple approach of using an LLM to iteratively propose and refine candidate biases. Our method can recover known biases and surface novel ones: for example, we found that Skywork-V2-8B, a leading open-weight reward model, often mistakenly favors responses with redundant spacing and responses with hallucinated content. In addition, we show evidence that evolutionary iteration outperforms flat best-of-N search, and we validate the recall of our pipeline using synthetically injected biases. We hope our work contributes to further research on improving RMs through automated interpretability methods.

### 2602.15318v1 — Sparrow: Text-Anchored Window Attention with Visual-Semantic Glimpsing for Speculative Decoding in Video LLMs

原始链接：https://arxiv.org/abs/2602.15318v1

Submitted UTC：2026-02-17T02:51:36Z；DOI Created UTC：2026-02-18T02:38:46Z（后者不是首公开时刻）。

Although speculative decoding is widely used to accelerate Vision-Language Models (VLMs) inference, it faces severe performance collapse when applied to Video Large Language Models (Vid-LLMs). The draft model typically falls into the trap of attention dilution and negative visual gain due to key-value cache explosion and context window mismatches. We observe a visual semantic internalization phenomenon in Vid-LLMs, indicating that critical visual semantics are implicitly encoded into text hidden states during deep-layer interactions, which renders raw visual inputs structurally redundant during deep inference. To address this, we propose the Sparrow framework, which first utilizes visually-aware text-anchored window attention via hidden state reuse to fully offload visual computation to the target model, and leverages intermediate-layer visual state bridging to train the draft model with semantic-rich intermediate states, thereby filtering out low-level visual noise. Additionally, a multi-token prediction strategy is introduced to bridge the training-inference distribution shift. Experiments show that Sparrow achieves an average speedup of 2.82x even with 25k visual tokens, effectively resolving the performance degradation in long sequences and offering a practical solution for real-time long video tasks.

### 2602.15323v1 — Unforgeable Watermarks for Language Models via Robust Signatures

原始链接：https://arxiv.org/abs/2602.15323v1

Submitted UTC：2026-02-17T03:09:06Z；DOI Created UTC：2026-02-18T02:38:53Z（后者不是首公开时刻）。

Language models now routinely produce text that is difficult to distinguish from human writing, raising the need for robust tools to verify content provenance. Watermarking has emerged as a promising countermeasure, with existing work largely focused on model quality preservation and robust detection. However, current schemes provide limited protection against false attribution. We strengthen the notion of soundness by introducing two novel guarantees: unforgeability and recoverability. Unforgeability prevents adversaries from crafting false positives, texts that are far from any output from the watermarked model but are nonetheless flagged as watermarked. Recoverability provides an additional layer of protection: whenever a watermark is detected, the detector identifies the source text from which the flagged content was derived. Together, these properties strengthen content ownership by linking content exclusively to its generating model, enabling secure attribution and fine-grained traceability. We construct the first undetectable watermarking scheme that is robust, unforgeable, and recoverable with respect to substitutions (i.e., perturbations in Hamming metric). The key technical ingredient is a new cryptographic primitive called robust (or recoverable) digital signatures, which allow verification of messages that are close to signed ones, while preventing forgery of messages that are far from all previously signed messages. We show that any standard digital signature scheme can be boosted to a robust one using property-preserving hash functions (Boyle, LaVigne, and Vaikuntanathan, ITCS 2019).


