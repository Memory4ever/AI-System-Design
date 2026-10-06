[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Why Diffusion Language Models Struggle with Truly Parallel (Non-Autoregressive) Decoding?

[3] h6: Abstract

[4] p: Diffusion Language Models (DLMs) are often advertised as enabling parallel token generation, yet practical “fast” DLMs frequently converge to left-to-right, autoregressive (AR)-like decoding dynamics. In contrast, genuinely non-AR generation is promising because it removes AR’s sequential bottleneck, better exploiting parallel hardware to reduce synchronization/communication overhead and improve latency scaling with output length. We argue that a primary driver of AR-like decoding is a mismatch between DLM objectives and the highly sequential structure of widely used training data, including standard pre-training corpora and long chain-of-thought (CoT) supervision. Motivated by this diagnosis, we propose NAP (Non-Autoregressive Parallel DLMs), a proof-of-concept, data-centric approach that better aligns supervision with non-AR parallel decoding. NAP curates examples as multiple independent reasoning trajectories and couples them with a parallel-forced decoding strategy that encourages multi-token parallel updates. Across math reasoning benchmarks, NAP yields stronger performance under parallel decoding than DLMs trained on standard long CoT data, with gains growing as parallelism increases. Our results suggest that revisiting data and supervision is a principled direction for mitigating AR-like behavior and moving toward genuinely non-autoregressive parallel generation in DLMs. Our code is available at https://github.com/pixeli99/NAP .

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] p: Large language models (LLMs) have become a cornerstone of modern AI, yet their rapidly growing computational and environmental footprints raise pressing sustainability concerns ( Patterson et al., 2021 ; Luccioni et al., 2023 ) . This motivates renewed interest in alternative generation paradigms that can reduce inference latency and cost without sacrificing capability. Diffusion Language Models (DLMs) have recently emerged as a compelling candidate: by iteratively denoising a sequence, DLMs can in principle enable parallel token generation , offering a path toward faster, more efficient generation ( Austin et al., 2021a ; Lou et al., 2023 ; Shi et al., 2024b ; Sahoo et al., 2024a ; Nie et al., 2025b ; Gong et al., 2024 ; Ye et al., 2025 ) . When paired with established inference accelerators, such as KV caching ( Ma et al., 2025 ; Wu et al., 2025 ; Liu et al., 2025 ) and speculative decoding ( Christopher et al., 2025 ; Gao et al., 2025 ; Chen et al., 2026 ) , DLM-based systems are often claimed as substantially faster alternatives to standard autoregressive (AR) decoding.

[8] figure: (a) LLaDA-8B (AO) (b) Dream-7B (AO) (c) Random (d) Ours Figure 1 : Visualization of decoding dynamics. We plot the token position being unmasked (y-axis) against the decoding step (x-axis). (a, b) Despite using confidence-based Arbitrary Order (AO) decoding, standard DLMs (LLaDA and Dream) exhibit a strict linear diagonal pattern, revealing that their behavior collapses into autoregressive (left-to-right) generation. (c) Random decoding eliminates AR bias but lacks structure. (d) Our method (NAP) breaks the single-stream bottleneck, generating multiple reasoning trajectories simultaneously.

[9] p: Yet, despite their promise, practical “fast” DLMs exhibit a striking and under-discussed behavior: many methods that aim for highly parallel decoding converge toward AR-like generation , where the effective reasoning trajectory proceeds largely from left to right ( Nie et al., 2025b ; Israel et al., 2025 ; Wu et al., 2025 ; Gong et al., 2025 ) . In other words, even when the model architecture permits bidirectional context and parallel refinement, the realized decoding dynamics can resemble a sequential construction of the output. This phenomenon makes real-world DLM usage more nuanced than the headline promise of “truly parallel decoding”: speedups are often coupled to subtle quality trade-offs, and the conditions under which DLMs depart meaningfully from AR behavior remain unclear ( Kang et al., 2025 ) .

[10] p: The payoff for achieving genuinely (non-AR) parallel decoding is substantial : AR-style decoding is fundamentally sequential, every token depends on the previous one, so generation latency scales roughly with output length. Although we can switch to fast parallel decoding in subsequent blocks after earlier blocks have largely converged, the need to wait for upstream stabilization introduces a sequential critical path, leading to extra latency and communication cost ( Wang et al., 2025 ; Fu et al., 2025 ) . In contrast, truly non-AR parallel decoding is naturally compatible with the distributed hardware, i.e., when dependencies across spans are weak, decoding is naturally compatible with distributed hardware and can be distributed across devices, with only occasional synchronization to maintain global consistency.

[11] p: In this work, we argue that one primary caveat of this AR-bias is a mismatch between the learning objective and the training data . Existing DLM pipelines blindly reuse training data originally designed for AR models, where reasoning trajectories are implicitly encoded as left-to-right progressions, e.g., next-token prediction–style ordering ( Ye et al., 2025 ; Allal et al., 2025 ; Li et al., 2024 ) , or sequential Chain-of-Thought (CoT) rationales ( Zhao et al., 2025 ; Lambert et al., 2024 ) . As a result, even if the diffusion process is nominally position-agnostic, the model can learn denoising strategies that preferentially reconstruct outputs in an AR-shaped manner. This “AR-shaped data” effect not only limits the extent to which DLMs can exploit genuine parallelism, but also complicates evaluation: a method may appear effective while largely reproducing AR model’s dynamics under a different wrapper.

[12] figure: Figure 2 : Performance on GSM8K (left) and MATH-500 (right). Forcing low-ARness behavior (Random decoding) generally causes reasoning performance to collapse. Notably, for LLaDA, we employ a constrained block-wise decoding strategy to ensure generation validity. This preserves local structural integrity, resulting in the Arbitrary Order (AO) decoding maintaining comparable performance, unlike the sharp drop observed in fully unstructured random decoding.

[13] figure: (a) OpenR1-Math SeqDep (b) Fineweb SeqDep Figure 3 : Sequential Dependence (SeqDep) Analysis on (a) OpenR1-Math and (b) FineWeb Datasets. The consistently high and rising SeqDep scores indicate that standard training corpora possess strong intrinsic sequentiality, driving models to internalize AR-like dependencies.

[14] p: To test this conjecture, we conduct a systematic analysis of the decoding behavior of commonly used DLMs. The main findings are summarized below.

[15] p: I. Widely used training corpora are strongly sequential. We quantify the sequential dependency of datasets by measuring how strongly the token at one position is determined by its preceding context. We show a consistent trend: commonly used pre-training corpora (i.e., FineWeb ( Penedo et al., 2024 ) ) and long CoT reasoning datasets (i.e., Open-R1-Math ( Team, 2025 ) ) display strong sequence dependence.

[16] p: II. DLM decoding remains largely autoregressive. Across widely used DLM families such as LLaDA ( Nie et al., 2025c ) and Dream ( Ye et al., 2025 ) , ARness remains high: the model still tends to “lock in” decisions in a quasi-left-to-right pattern, despite the nominally arbitrary decoding rules. Conversely, forcing genuinely low ARness behavior, for instance, by randomizing the update order aggressively, can reduce ARness but typically causes reasoning performance to collapse. Taken together, these results indicate a non-trivial tradeoff: in standard setups, either ARness stays high to maintain capacity, or lowering ARness breaks reasoning.

[17] p: III. Training on long CoT data escalates ARness. Continued post-training on standard long CoT datasets further increases ARness over time. While DLMs trained from scratch (e.g., LLaDA) tend to exhibit lower ARness than those adapted from pre-trained AR models (e.g., Dream), this gap gradually narrows with sustained CoT supervision. Intuitively, long CoT supervision provides an explicit step-by-step trajectory with a privileged ordering. Matching such training targets rewards the model for producing and stabilizing earlier tokens before later ones, thereby progressively shifting the learned decoding dynamics toward increasingly autoregressive behavior.

[18] p: IV. Recent parallel fast-DLM methods gain speed by amplifying , not removing, AR-like generation. Despite being motivated by parallel decoding, many recent fast-DLM approaches achieve practical speedups by reinforcing an underlying autoregressive computation pattern. In particular, they rely on increasingly confident early predictions or staged block-wise updates that stabilize prefixes before allowing limited parallelism downstream. As a result, parallelism is effectively gated by an AR-like convergence order, and the achieved acceleration stems from exaggerating this sequential structure rather than eliminating it.

[19] p: The above findings suggest that even though the DLMs permit arbitrary decoding strategy, as DLMs are trained on highly sequentially structured data, the model tends to internalize an AR-like computational strategy. In other words, the training distribution teaches the model that reasoning is a chain with a privileged order, and changing the decoding procedure alone is often insufficient to undo this learned reliance. Addressing the issue therefore requires revisiting the data and supervision that shape the model’s generation strategy in the first place.

[20] p: To this end, we propose NAP ( Non-Autoregressive Parallel DLMs ), a proof-of-concept approach that tackles the problem from a data and decoding codesign perspective. First, we curate supervision in which each example consists of multiple independent reasoning trajectories generated in parallel, this format deemphasizes any privileged token order and is naturally compatible with denoising-style learning in DLMs. Second, we introduce a parallel-forced decoding strategy that explicitly encourages multi-token parallel updates at different reasoning traces, further steering generation away from AR-like critical paths. Together, these two components provide a simple and effective way to better align DLM behavior with truly parallel decoding. Across a range of math reasoning benchmarks, our results show that NAP, fine-tuned with 103K samples, consistently yields stronger performance under parallel decoding than the baseline trained on standard long CoT datasets. Moreover, the improvement becomes more pronounced as we increase the degree of parallelism, indicating that NAP is better aligned with non-AR decoding dynamics rather than relying on an implicit sequential critical path.

[21] p: Note that our goal is not to claim that NAP fully resolves the challenges of non-AR parallel decoding. Rather, we aim to use this small-scale post-training only result to show that revisiting data and supervision design is a promising direction for mitigating AR-like behavior in DLMs and moving toward genuinely non-autoregressive parallel generation. We hope our results motivate further work on data-centric approaches to unlock the full efficiency potential of DLMs.

[22] h2: 2 Related Work

[23] h3: 2.1 Diffusion Language Models

[24] p: Diffusion models ( Sohl-Dickstein et al., 2015 ; Ho et al., 2020 ; Song et al., 2021 ) , best known for their success in image generation ( Rombach et al., 2022 ; Nichol et al., 2022 ; Saharia et al., 2022 ) , are increasingly studied as a non-autoregressive alternative for text generation. Bringing diffusion from continuous variables to discrete tokens can be formalized by treating the forward corruption as a Markov process over a finite vocabulary: D3PM ( Austin et al., 2021b ) instantiates this idea with discrete-time transition matrices, while subsequent work extends it to continuous time through CTMC formulations ( Campbell et al., 2022 ) . A particularly practical family is masked diffusion, which can be viewed as an absorbing-state construction in the D3PM lineage and operates directly in token space via random masking ( Shi et al., 2024a ) . This paradigm has produced strong results across scales, from smaller models such as MDLM ( Sahoo et al., 2024b ) and RADD ( Ou et al., 2025 ) to large systems like LLaDA ( Nie et al., 2025a ) and Dream ( Ye et al., 2025 ) . Beyond text-only settings, MMaDA ( Yang et al., 2025 ) further generalizes large diffusion models to multimodal generation with a shared probabilistic view and modality-agnostic architecture, while the broader literature highlights potential benefits such as parallelizable decoding and flexible (non left-to-right) generation orders that may be useful for complex reasoning.

[25] h3: 2.2 Decoding Order and Sampling Schedules

[26] p: A key degree of freedom in masked diffusion language models is the sampling path—which positions are updated (or committed) at each refinement step and in what order. Rather than being a mere implementation detail, several works treat order as an explicit control knob for quality/efficiency trade-offs. P2 ( Peng et al., 2025 ) cast order selection as a planning problem, where a separate planner chooses which tokens to denoise at each step, decoupling where/when to update from how to update. Prophet ( Li et al., 2025 ) further leverages model confidence to early-commit, switching from iterative refinement to one-shot completion when the top-2 gap indicates convergence. Order-awareness has also been pushed into training, e.g., by encouraging simpler and more coherent sampling paths ( Zhu et al., ) . Meanwhile, Ni et al. (2026) caution that arbitrary-order flexibility can be a double-edged sword: models may preferentially resolve low-uncertainty tokens and bypass high-uncertainty branching points, collapsing the effective reasoning space, suggesting that constraining or regularizing generation order can sometimes improve reasoning.

[27] h2: 3 Preliminaries

[28] h3: 3.1 Diffusion Language Models

[29] p: We consider diffusion language models (DLMs), and in particular masked diffusion models (MDMs), which generate discrete token sequences by iteratively denoising a partially masked state. Let x x denote the input prompt and let y 0 = ( y 0 1 , … , y 0 L ) ∈ 𝒱 L y_{0}=(y_{0}^{1},\dots,y_{0}^{L})\in\mathcal{V}^{L} denote a clean output sequence of length L L over vocabulary 𝒱 \mathcal{V} . MDMs define a forward masking process indexed by a continuous time variable t ∈ [ 0 , 1 ] t\in[0,1] , where t t represents the masking ratio. Given y 0 y_{0} , the forward process independently masks each token with probability t t :

[30] table: q ⁡ ( y t i ∣ y 0 i ) = { [MASK] , with prob. ​ t , y 0 i , with prob. ​ 1 − t , q\!\left(y_{t}^{i}\mid y_{0}^{i}\right)=\begin{cases}\texttt{[MASK]},&\text{with prob. }t,\\ y_{0}^{i},&\text{with prob. }1-t,\end{cases} (1)

[31] p: and factorizes across positions as q ⁡ ( y t ∣ y 0 ) = ∏ i = 1 L q ⁡ ( y t i ∣ y 0 i ) q(y_{t}\mid y_{0})=\prod_{i=1}^{L}q(y_{t}^{i}\mid y_{0}^{i}) . At t = 1 t=1 , the sequence is fully masked; at t = 0 t=0 , it remains unchanged.

[32] h3: 3.2 Measuring Autoregressive Bias

[33] p: To quantify how autoregressive-like a DLM decoding trajectory is, we adopt the ARness metrics proposed by Gong et al. (2025) , which distinguish between global left-to-right bias and local sequential continuity. Let the decoding process be represented by a sequence of unmasked positions 𝐩 = ( p 1 , p 2 , … , p L ) \mathbf{p}=(p_{1},p_{2},\dots,p_{L}) , where p c ∈ { 1 , … , L } p_{c}\in\{1,\dots,L\} denotes the position index of the token committed at decoding step c c . Let M c − 1 M_{c-1} be the set of masked positions just before step c c .

[34] h4: Global ARness.

[35] p: This metric measures the tendency to prioritize unmasking the leftmost remaining tokens, capturing a front-to-back filling strategy. For a tolerance window k ≥ 1 k\geq 1 , we define an indicator 𝕀 global ​ ( c , k ) \mathbb{I}_{\text{global}}(c,k) that is 1 1 if the chosen position p c p_{c} is among the k k earliest positions in M c − 1 M_{c-1} :

[36] table: 𝕀 global ​ ( c , k ) = { 1 , if ​ p c ∈ smallest- ​ k ​ ( M c − 1 ) , 0 , otherwise . \mathbb{I}_{\text{global}}(c,k)=\begin{cases}1,&\text{if }p_{c}\in\text{smallest-}k(M_{c-1}),\\ 0,&\text{otherwise}.\end{cases} (2)

[37] p: The Global ARness score is the average over the sequence:

[38] table: Global-ARness ​ @ ​ k = 1 L ​ ∑ c = 1 L 𝕀 global ​ ( c , k ) ∈ [ 0 , 1 ] . \text{Global-ARness}@k=\frac{1}{L}\sum_{c=1}^{L}\mathbb{I}_{\text{global}}(c,k)\in[0,1]. (3)

[39] p: A score of 1.0 (at k = 1 k=1 ) indicates a strict autoregressive (left-to-right) generation order.

[40] p: Unless otherwise stated, we use Global-ARness@1 as the primary measure of ARness in our analysis, as it directly quantifies the adherence to a causal generation order.

[41] h3: 3.3 Measuring Sequential Dependence (SeqDep)

[42] p: To quantify the intrinsic sequentiality of a dataset, we measure how much the prediction of a current text segment relies on its preceding generation history compared to relying solely on the initial prompt. Let x x denote the input prompt. Suppose the corresponding output sequence is divided into N N segments 𝐬 = ( s 1 , … , s N ) \mathbf{s}=(s_{1},\dots,s_{N}) . Using an external autoregressive scorer p AR p_{\mathrm{AR}} (e.g., a pretrained LLM), we define the Sequential Dependence (SeqDep) as the average log-probability gain provided by the prefix context:

[43] table: SeqDep ⁡ ( x , 𝐬 ) = 1 N − 1 ​ ∑ n = 2 N ( log ⁡ p AR ​ ( s n ∣ x , s < n ) CLOSE OPEN − log ⁡ p AR ​ ( s n ∣ x ) ) \begin{split}\mathrm{SeqDep}(x,\mathbf{s})&=\frac{1}{N-1}\sum_{n=2}^{N}\Big(\log p_{\mathrm{AR}}(s_{n}\mid x,s_{<n})\\ &\quad-\log p_{\mathrm{AR}}(s_{n}\mid x)\Big)\end{split} (4)

[44] p: Intuitively, this metric captures the conditional dependence between reasoning steps. A SeqDep \mathrm{SeqDep} score near 0 0 indicates that the segment s n s_{n} is conditionally independent of previous segments s < n s_{<n} given the prompt x x , implying that the sequence components could theoretically be generated in parallel. Conversely, a high positive SeqDep \mathrm{SeqDep} score indicates a strong chain-like structure—meaning later tokens are heavily dictated by the immediate preceding context, a hallmark of standard left-to-right autoregressive reasoning.

[45] h2: 4 Decoding Behaviors of DLMs

[46] p: In this section, we conduct a systematic analysis of the decoding behavior of commonly used DLMs. We fix the pretrained masked diffusion model, the token budget, the number of refinement steps, and the mask-ratio schedule, and vary only the decoding rule. This isolates the effect of the induced generation order from all other factors. Our main findings are summarized below.

[47] h3: 4.1 Strong Sequential Dependence in Training Corpora

[48] p: A primary driver of sequential behavior is the data itself. We hypothesize that if the training distribution is highly sequential, the model learns an implicit left-to-right dependency that persists even under parallel decoding objectives.

[49] p: We quantify this using the SeqDep \mathrm{SeqDep} metric (Sec. 3.3 ) on two representative datasets: FineWeb (pre-training corpora) and OpenR1-Math (long-CoT reasoning). As shown in Figure 3(b) and 3(a) , both datasets display strong sequence dependence. Notably, reasoning steps in OpenR1-Math exhibit increasing dependence as the chain progresses ( p AR p_{\mathrm{AR}} predicts later steps with much higher confidence given the prefix). This suggests that standard training data teaches the model that reasoning is a fundamentally ordered chain, creating a mismatch with position-agnostic diffusion objectives.

[50] h3: 4.2 DLMs’ Decoding Remains Largely Autoregressive

[51] p: Given sequential training data, we examine how DLMs behave during inference. We evaluate two popular models, LLaDA-8B ( Nie et al., 2025c ) and Dream-7B ( Ye et al., 2025 ) , under three distinct decoding strategies: (i) Autoregressive (AR) Order : committing the leftmost unresolved tokens at each step, mimicking standard left-to-right generation; (ii) Arbitrary Order (AO) : a confidence-based strategy that commits the most certain tokens first regardless of their positions; and (iii) Random : committing a uniformly random subset of tokens at each step.

[52] p: Unlike Dream-7B, which handles fully unstructured parallel updates relatively well, LLaDA-8B exhibits severe degradation on structured mathematical tasks if unmasked entirely at random. This is largely an artifact of its specific supervised fine-tuning (SFT) phase. To ensure valid and comparable generation quality for LLaDA, we apply a constrained block-wise modification ( Arriola et al., 2025 ) to the AO and Random strategies.

[53] figure: Table 1 : Quantifying Autoregressive Bias (ARness) and Accuracy. Comparison of sequential bias and performance across different decoding strategies. While AR Order implies strict sequentiality (1.00), AO (Conf) maintains high ARness and competitive accuracy. Model AR Order AO (Conf) ARness Acc ARness Acc LLaDA-8B ( Nie et al., 2025c ) 1.00 71.9 0.73 51.9 + Fast-dLLM ( Wu et al., 2025 ) 1.00 71.9 0.87 51.6 Dream-7B ( Ye et al., 2025 ) 1.00 78.2 0.92 78.2 + Fast-dLLM ( Wu et al., 2025 ) 1.00 78.3 0.94 78.1

[54] p: High ARness in DLM Decoding. Table 1 reports the ARness scores. While AR order is 1.0 by definition, AO decoding converges to extremely high ARness ( ∼ 0.92 \sim 0.92 for Dream), indicating that the model’s most “confident” tokens are almost always the next tokens in the sequence. As a result, DLMs exhibit behavior closely resembling autoregressive generation.

[55] p: The Accuracy–ARness Tradeoff. Is it possible to force genuinely parallel behavior? We test this using a Random decoding strategy, which successfully yields near-zero ARness. However, as shown in Figure 2 , this comes at a severe cost: reasoning accuracy on GSM8K ( Cobbe et al., 2021 ) and MATH 500 ( Lightman et al., 2023 ) collapses when the model is prevented from following a sequential path. These results suggest that strong reasoning performance is often obtained at the cost of genuine parallelism, as improved accuracy tends to coincide with higher AR-ness under standard setups.

[56] h3: 4.3 Long-CoT Supervision Escalates AR-ness

[57] figure: Table 2 : Long-CoT Supervision Increases ARness. Comparison of Global ARness@1 scores (using AO decoding) before and after fine-tuning. Model Base (Pretrained) Long-CoT (SFT) Change LLaDA-8B 0.73 0.81 ↑ \uparrow 0.08 Dream-7B 0.92 0.93 ↑ \uparrow 0.01

[58] figure: Figure 4 : Long-CoT Supervision Increases ARness. The positive deltas show models converging toward strict left-to-right generation (1.0), confirming that current supervision methods actively discourage non-autoregressive parallel decoding.

[59] p: We further investigate how supervised fine-tuning (SFT) on long Chain-of-Thought (CoT) data affects decoding dynamics. We compare the ARness of base models against checkpoints post-trained on standard CoT datasets (Open-R1 Math ( Team, 2025 ) ).

[60] p: As shown in Table 2 and Figure 4 , results indicate a clear trend: post-training further increases ARness . For instance, LLaDA’s base ARness under AO decoding rises from 0.73 to 0.81 after CoT tuning. Intuitively, CoT supervision provides explicit step-by-step trajectories with a privileged order. Minimizing the loss on such data rewards the model for stabilizing earlier tokens before later ones, effectively ”baking in” the AR order and making it harder for the model to utilize genuine parallel decoding during inference.

[61] h3: 4.4 Current Fast DLMs Reinforce Sequentiality

[62] p: Finally, we analyze whether specialized ”fast” decoding algorithms can unlock genuine parallelism. We evaluate Fast-dLLM ( Wu et al., 2025 ) , a state-of-the-art acceleration method that employs block-wise parallel decoding.

[63] p: As shown in Table 1 , these methods do not reduce sequential dependence; in fact, they exacerbate it. For instance, while standard AO decoding for LLaDA has an ARness of 0.73, applying Fast-dLLM pushes this score up to 0.87 . Similarly, for Dream-7B, the ARness rises to 0.94 , nearly indistinguishable from strict autoregressive decoding (1.00).

[64] figure: [Input Query] A shirt costs $50 and is on sale for 20% off. What is the final price? [Model Output] ⟨ \langle think 1 ⟩ \rangle Method: Calculate discount amount first. Discount = 50 × 0.20 = 10 50\times 0.20=10 . Final Price = 50 − 10 = 40 50-10=40 . ⟨ \langle /think 1 ⟩ \rangle ⟨ \langle think 2 ⟩ \rangle Direct multiplier. Since it’s 20% off, we pay 100 % − 20 % = 80 % 100\%-20\%=80\% . Final Price = 50 × 0.8 = 40 50\times 0.8=40 . ⟨ \langle /think 2 ⟩ \rangle ⟨ \langle think 3 ⟩ \rangle 20 % 20\% of 50 50 is 10 10 . Final Price = 50 − 10 = 30 50-10=30 . [Calculation Error] ⟨ \langle /think 3 ⟩ \rangle ⟨ \langle summary ⟩ \rangle By analyzing multiple reasoning processes above, I concluded that: The final answer is 40 . ⟨ \langle /summary ⟩ \rangle Figure 5 : A compact training instance. The model generates parallel paths (including distinct methods and a noisy path) and aggregates them into a correct summary.

[65] p: This empirical evidence suggests that current ”fast” DLMs achieve speedups not by enabling non-sequential generation, but by effectively identifying and accelerating the underlying autoregressive critical path. The parallelism in these systems is gated by the convergence of the prefix, meaning they optimize the execution of the sequential chain rather than eliminating the bottleneck. This diagnosis reinforces our core premise: achieving true non-autoregressive parallelism requires revisiting the supervision signal itself, rather than relying solely on inference-time algorithmic optimizations.

[66] h2: 5 NAP: Non-Autoregressive Parallel DLMs

[67] figure: Figure 6 : Overview of the parallel-forced decoding framework . The model concurrently generates multiple independent reasoning paths within structured thinking blocks. These parallel trajectories are then synthesized into a result within a designated summary block.

[68] h3: 5.1 Overview

[69] p: To bridge the gap between DLM objectives and the sequential nature of reasoning data, we propose NAP ( Non-Autoregressive Parallel DLMs ). NAP is a data-decoding co-design framework that breaks the implicit autoregressive lock-in by restructuring both the supervision signal and the inference process. The framework operates on two levels: first, it curates training examples as multiple independent reasoning trajectories rather than a single linear chain, thereby removing the notion of a privileged order; second, it employs a parallel-forced decoding strategy that explicitly enforces multi-stream updates during inference, preventing the model from collapsing into a sequential critical path.

[70] h3: 5.2 Data Curation

[71] p: Standard chain-of-thought (CoT) data typically encodes a single canonical left-to-right reasoning order, creating a natural mismatch with the objective of parallel DLM decoding. To address this, we curate a dataset 𝒟 parallel \mathcal{D}_{\text{parallel}} whose supervision is inherently parallel.

[72] h4: Generating Parallel Reasoning Traces.

[73] p: Similar to ParaThinker ( Wen et al., 2025 ) , given a query x x , we prompt a strong teacher model to generate P P independent reasoning traces { r ( 1 ) , … , r ( P ) } \{r^{(1)},\dots,r^{(P)}\} . We employ a high sampling temperature ( τ = 1.0 \tau=1.0 ) to induce diverse problem-solving approaches or distinct logical orderings. Unlike standard augmentation which treats these as separate samples, NAP groups them into a single training instance. This ensures that the parallel paths represent truly independent explorations rather than redundant copies.

[74] h4: Summary and Aggregation.

[75] p: To teach the model to resolve conflicts, we construct the summary block S S by conditioning the ground-truth answer a a on the concatenation of these diverse (and potentially noisy) paths. The final training instance follows the format in Eq. ( 5 ), as illustrated in Figure 5 . In this setup, the model observes multiple parallel paths—some of which may contain errors (e.g., Path 3)—followed invariably by the correct result in S S . This supervision forces the model to implicitly learn how to identify valid reasoning streams and filter out noise to match the ground truth, treating the parallel paths as supporting evidence rather than a linear chain. We fine-tune the DLM on this structured data using the standard masked diffusion objective.

[76] h3: 5.3 Parallel-Forced Decoding

[77] p: To enable the model to reason in parallel, we design a decoding canvas that spatially separates reasoning streams and enforce a structure-aware update schedule.

[78] h4: Decoding Canvas.

[79] p: We define a structured output format containing m m independent reasoning blocks and one summary block:

[80] table: Y = [ B 1 , R ( 1 ) , B 2 , R ( 2 ) , … , B m , R ( m ) , B S , S ] , Y\;=\;\big[\,B_{1},R^{(1)},\;B_{2},R^{(2)},\;\dots,\;B_{m},R^{(m)},\;B_{\mathrm{S}},S\,\big], (5)

[81] p: where B j B_{j} are fixed textual headers (e.g., “ <think #j> ”), R ( j ) R^{(j)} are free-form reasoning contents for the j j -th path, and S S is a final summary containing the answer. Given a prompt x x , we initialize a canvas of length L = ∑ ( | B j | + L j ) + ( | B S | + L S ) L=\sum(|B_{j}|+L_{j})+(|B_{\mathrm{S}}|+L_{\mathrm{S}}) , where fixed headers are clamped and reasoning slots are initialized to [MASK] . This layout effectively enforces conditional independence between R ( i ) R^{(i)} and R ( j ) R^{(j)} given the prompt, as there is no causal masking order between them in a bidirectional model.

[82] h4: Macro-Parallel, Micro-Confidence Updates.

[83] p: Standard arbitrary-order decoding often degenerates into global sequential generation because the model preferentially resolves the immediate next tokens. NAP-D prevents this via a hierarchical schedule. At the macro level, we enforce strict parallelism: the unmasking budget is distributed across all m m reasoning blocks { R ( 1 ) , … , R ( m ) } \{R^{(1)},\dots,R^{(m)}\} at every step. This constraint prevents the model from stabilizing upstream paths before initiating downstream ones. At the micro level, within each individual block R ( j ) R^{(j)} , we apply a confidence-based strategy (i.e., masking low-confidence tokens). We do not enforce a left-to-right order locally; instead, tokens are committed based on their confidence scores. This combination ensures that the global process is parallel (evolving multiple trajectories simultaneously) while local generation retains the flexibility of non-autoregressive refinement.

[84] h2: 6 Experiments

[85] figure: Table 3 : Benchmark results on LLaDA-8B-Instruct and Dream-7B-Instruct under different step budgets. Tok/Step denotes the number of tokens decoded per decoding step; larger Tok/Step corresponds to higher decoding parallelism. Benchmark Steps Tok/Step LLaDA 8B LLaDA 8B (Long-CoT) NAP-LLaDA 8B Dream-7B Dream-7B (Long-CoT) NAP-Dream-7B Mathematics & Scientific GSM8K 256 4 46.4 54.1 56.1 (+2.0) 35.0 46.5 60.9 (+14.4) 336 3 54.4 60.9 63.3 (+2.4) 49.4 56.9 70.9 (+14.0) 512 2 62.0 82.0 82.6 (+0.4) 58.5 66.8 79.2 (+12.4) 1024 1 66.5 83.5 84.1 (+0.6) 68.9 78.0 83.6 (+5.6) MATH-500 256 4 17.8 21.4 26.6 (+5.2) 8.8 16.2 23.8 (+7.6) 336 3 20.6 26.6 35.4 (+8.8) 11.4 25.6 31.4 (+5.8) 512 2 28.0 41.2 43.0 (+1.8) 20.8 40.0 43.0 (+3.0) 1024 1 30.4 45.0 47.0 (+2.0) 35.0 47.4 49.6 (+2.2) GPQA 336 3 12.5 15.4 19.0 (+3.6) 5.8 7.3 10.5 (+3.2) 512 2 18.8 21.2 25.9 (+4.7) 14.7 19.4 22.5 (+3.1) 1024 1 20.8 23.0 28.6 (+5.6) 26.1 28.6 29.5 (+0.9)

[86] p: This section evaluates whether our decoding strategy can (i) improve reasoning performance over standard diffusion decoding rules, (ii) reshape the induced generation order as measured by ARness (Section 3.2 ), and (iii) mitigate order sensitivity in regimes where long-form rationales exhibit strong sequential dependence (Eq. ( 4 )). Unless otherwise stated, all results use the same pretrained masked diffusion model and differ only in the decoding rule.

[87] p: Evaluation protocol. We evaluate on a suite of reasoning benchmarks including GSM8K ( Cobbe et al., 2021 ) , MATH-500 ( Lightman et al., 2023 ) , and GPQA ( Rein et al., 2024 ) . Each example is prompted to produce a thinking path and a final answer in a fixed format; we extract answers with a deterministic parser and report accuracy.

[88] p: Models and Training. We conduct experiments on two state-of-the-art diffusion language models: LLaDA-8B-Instruct ( Nie et al., 2025c ) and Dream-7B-Instruct ( Ye et al., 2025 ) . To validate our proposed method, we fine-tune these base models on the parallel reasoning dataset 𝒟 parallel \mathcal{D}_{\text{parallel}} curated via the pipeline described in Section 5.2 . For a fair comparison, we also train a Long-CoT baseline on the same set of reasoning trajectories but serialized in the standard autoregressive format. Crucially, this baseline is evaluated using standard decoding—its optimal inference setting—rather than our parallel strategy, ensuring a strong and fair comparison. Both variants are trained using the standard masked diffusion objective for 3 epochs. We use the AdamW optimizer with a learning rate of 2e-6 and a global batch size of 256. All experiments are conducted on 8 NVIDIA A800 GPUs.

[89] p: Decoding baselines. We compare several widely used unmasking rules under the common mask-and-predict framework. AR order commits the leftmost unresolved tokens at each step (a diffusion realization of left-to-right decoding). Arbitrary order (AO) commits the most confident positions. Random order (Rand) commits a uniformly random subset at each step, serving as a low-ARness control. Our method generates m m multiple independent reasoning paths and a final summary commit on a structured canvas. To ensure a fair budget, PaS-Dec uses the same total token cap L L by allocating per-path budgets 330 330 and a summary budget 32 32 such that the overall canvas length matches the baseline. The summary block is the only region used for answer extraction and scoring.

[90] h3: 6.1 Main Results

[91] p: Table 3 summarizes the performance across three benchmarks. Across all benchmarks and step budgets, our method achieves higher accuracy than both the Base model and the Long-CoT baseline. For instance, on GSM8K with Dream-7B (1024 steps), NAP-Dream-7B reaches 83.6%, surpassing the Long-CoT model (78.0%) despite using the same amount of compute and training data. This suggests that organizing reasoning into parallel streams is a more effective supervision signal for DLMs than forcing a single long chain.

[92] p: The most significant advantage of NAP appears in the low-step regime, e.g., 256 steps (4x parallel), where the model must generate more than one token per forward pass. Standard Long-CoT models degrade sharply as parallelism increases. On Dream-7B/GSM8K, accuracy drops from 78.0% (1024 steps) to 46.5% (256 steps). This confirms that standard supervision creates a dependency on sequential stability; when forced to hurry, the reasoning collapses. In the same setting, NAP-Dream-7B maintains strong accuracy at 60.9%, compared to 46.5% of the Long-CoT baseline, thereby retaining substantially more capability. Notably, the gap between NAP and Long-CoT widens as parallel decoding is made more aggressive, increasing from +5.6% at 1024 steps to +14.4% at 256 steps. This result validates our core hypothesis: by training on data that lacks a privileged order, the model learns to be less reliant on the immediate left-side context, enabling effective Non-AR parallel decoding.

[93] p: To further understand how NAP achieves these results, we analyze the relationship between performance and the sequential nature of generation (ARness). As shown in Figure 1 , standard models (LLaDA/Dream) using Arbitrary Order (AO) decoding exhibit a strict diagonal pattern. Even though they can decode anywhere, they effectively collapse into a left-to-right process (High ARness). In contrast, NAP (Figure 1 (d)) displays distinct parallel bands, confirming that multiple reasoning trajectories are being generated simultaneously.

[94] h3: 6.2 Ablation Studies

[95] p: We investigate the individual contributions of the supervision data and the decoding strategy using Dream-7B on the GSM8K benchmark.

[96] p: The Necessity of Data-Decoding Co-design. We first isolate the impact of our proposed decoding method versus the parallel-aligned data. As shown in Table 4 , applying our Parallel-Forced Decoding strategy to a standard base model that has not been trained with our data leads to a larger performance drop than standard Arbitrary Order (AO) decoding. This suggests that without training support, the original Dream-7B struggles to handle the fragmented context of simultaneous generation. In addition, the decoding strategy becomes critical when parallelism is high. Specifically at the aggressive 256-step budget, our Parallel-Forced decoding outperforms AO (60.9% vs. 57.4%). This confirms that while the data provides the foundational reasoning capability, aligning the decoding strategy is essential to maintain robustness when forcing the model to generate multiple tokens in parallel.

[97] figure: Table 4 : GSM8K accuracy using Dream-7B. Simply applying parallel decoding to a base model hurts performance; gains require aligned supervision. Training Data Decoding 256 512 1024 Base (Pretrained) AO 35.0 58.5 68.9 Base (Pretrained) Parallel-Forced 31.0 52.6 60.2 NAP (Ours) AO 57.4 78.9 85.1 NAP (Ours) Parallel-Forced 60.9 79.2 83.6

[98] p: Impact of Parallel Width ( m m ). We further analyze how the number of parallel reasoning paths affects performance while keeping the total token budget constant. As detailed in Table 5 , increasing the number of reasoning paths from a single chain ( m = 1 m=1 ) to three ( m = 3 m=3 ) provides consistent accuracy gains across both model families. Specifically, NAP-Dream sees a substantial improvement from 75.4% to 83.6%, while NAP-LLaDA rises from 79.4% to 84.1%. This monotonic trend supports the view that NAP benefits from an “internal ensemble” effect, where the final summary block effectively aggregates insights from multiple diverse trajectories generated in parallel to derive a more robust answer.

[99] figure: Table 5 : Accuracy on GSM8K with varying m m . Total token budget is fixed. Method 1 Path 2 Paths 3 Paths NAP-Dream 75.4 78.9 83.6 NAP-LLaDA 79.4 82.6 84.1

[100] p: Intrinsic Parallelism of Curated Data. To verify that our data curation pipeline effectively reduces the autoregressive bottleneck, we analyze the Sequential Dependence (SeqDep) of our constructed dataset 𝒟 parallel \mathcal{D}_{\text{parallel}} . As illustrated in Figure 7 , the SeqDep score remains remarkably stable (mean ≈ 12 \approx 12 ) even as the sequence length grows from 500 to over 1000 tokens. Unlike standard long-chain reasoning (as shown in Section 4 ), where dependence often escalates with depth, our parallel-structured data maintains a consistent level of information density. This ”flat” dependency profile confirms that the reasoning trajectories within our data possess high conditional independence, providing the necessary learning signal for the model to perform effective parallel updates during inference.

[101] figure: Figure 7 : SeqDep Analysis on 𝒟 parallel \mathcal{D}_{\text{parallel}} . We visualize the Sequential Dependence (SeqDep) of our curated parallel reasoning data against token length. The green curve (binned mean) shows that SeqDep remains stable and relatively low across varying lengths.

[102] h2: 7 Conclusion

[103] p: In this work, we argue that the struggle of Diffusion Language Models (DLMs) to achieve genuine parallel decoding stems largely from the implicit sequentiality of standard training data. Our proposed method, NAP, demonstrates that aligning supervision with parallel decoding dynamics effectively mitigates this autoregressive collapse. By training on parallel reasoning trajectories and enforcing multi-stream updates, NAP decouples reasoning capability from sequential order, achieving superior performance in high-parallelism regimes while significantly reducing global ARness. These results suggest that unlocking the full potential of non-autoregressive generation requires moving beyond decoding heuristics to fundamentally rethink how we structure supervision for parallel reasoning.

[104] h4: Limitations.

[105] p: While NAP demonstrates the feasibility of aligning supervision with genuinely parallel decoding, our current implementation serves primarily as a proof-of-concept. The method is evaluated in a post-training setting on a relatively small scale ( ∼ \sim 100K samples). As scaling laws dictate much of DLMs’ behavior, a broader pre-training phase with inherently non-sequential, parallel-structured data may be required to completely eliminate the autoregressive bottleneck.

[106] h2: References

[107] h2: Instructions for reporting errors

[108] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[109] p: Tip: You can select the relevant text first, to include it in your report.

[110] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[111] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
