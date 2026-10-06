# Jan10 KLJudge 必要原源

仅exact-v1拟采用KL条件分支及关键理论反侧；缓存为原web返回，不替代作者推断或代码复现。

Internal Error ()
citeturn26839view0 [wordlim: 200] Source: open({"ref_id":"https://arxiv.org/abs/2601.04609v1","lineno":null}); Total lines: 1
L0: Failed to fetch https://arxiv.org/abs/2601.04609v1: Cache miss
--------------------------------------------------------------------------------
Revisiting Judge Decoding from First Principles via Training-Free Distributional Divergence (https://arxiv.org/html/2601.04766v1)
citeturn26839view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04766v1","lineno":null}); Total lines: 432
L0: ##### Report GitHub Issue
L1: 
L2: [Button: ×]
L3: 
L4: Title: [Input: Enter title]
L5: 
L6: Content selection saved. Describe the issue below:
L7: 
L8: Description:
L9: 
L10: [Button: Submit without GitHub] [Button: Submit in GitHub]
L11: 
L12: cite0†Back to arXiv L13: 
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Background L18:     1. cite8†2.1 Speculative Decoding L19:     2. cite9†2.2 Judge Decoding L20:   4. cite10†3 The Bottlenecks of Supervision in Judge Decoding L21:     1. cite11†3.1 Judge Decoding With Manual Annotation L22:     2. cite12†3.2 Judge Decoding Without Manual Annotation L23:   5. cite13†4 Can We Bypass Data Annotation? L24:     1. cite14†4.1 Empirical Perspective L25:     2. cite15†4.2 Theoretical Perspective L26:   6. cite16†5 Experiment L27:     1. cite17†5.1 Experimental Setup and Baselines L28:       1. cite18†Benchmarks and Models. L29:       2. cite19†Baselines and Metrics. L30:     2. cite20†5.2 Main Results L31:       1. cite21†Superior Efficiency-Accuracy Trade-off. L32:       2. cite22†Robustness to Domain Shift. L33:       3. cite23†Real-world Speedup in vLLM. L34:       4. cite24†Efficiency in Long-Chain Reasoning. L35:   7. cite25†6 Related Work L36:     1. cite26†Speculative Decoding. L37:     2. cite27†Judge Decoding. L38:   8. cite28†7 Conclusion L39:   9. cite29†References L40:   10. cite30†A Appendix L41:     1. cite31†A.1 Proof of Theorem L42:       1. cite32†A.1.1 KL as a Bregman divergence and Fisher second-order approximation L43:       2. cite33†A.1.2 Pairwise form: KL as a Fisher-weighted sum of primitives L44:       3. cite34†A.1.3 Top-K inconsistency and boundary-crossing primitive L45:       4. cite35†A.1.4 From boundary-crossing primitives to a KL lower bound L46:       5. cite36†A.1.5 Why a linear classifier trained on “importance” aligns with KL screening L47:     2. cite37†A.2 Additional Experiment Details L48:     3. cite38†A.3 Potential of LLM Annotation L49: cite39†License: arXiv.org perpetual non-exclusive license†info.arxiv.org L50: 
L51: arXiv:2601.04766v1 [cs.CL] 08 Jan 2026
L52: # Revisiting Judge Decoding from First Principles via Training-Free Distributional Divergence
L53: Shengyin Sun^{*} Affiliation: City University of Hong Kong Email: shengysun4-c@my.cityu.edu.hk    Yiming Li ^{†}^{†}thanks: Equal contribution.
L54: Affiliation: Huawei Technologies Email: li.yiming3@huawei.com    Renxi Liu Affiliation: Huawei Technologies Email: chenma@cityu.edu.hk    Weizhe Lin Affiliation: Huawei Technologies    Hui-Ling Zhen Affiliation: Huawei Technologies    Xianzhi Yu Affiliation: Huawei Technologies    Mingxuan Yuan Affiliation: Huawei Technologies    Chen Ma ^{†}^{†}thanks: Corresponding author. Affiliation: City University of Hong Kong
L55: ###### Abstract
L56: Judge Decoding accelerates LLM inference by relaxing the strict verification of Speculative Decoding, yet it typically relies on expensive and noisy supervision. In this work, we revisit this paradigm from first principles, revealing that the “criticality” scores learned via costly supervision are intrinsically encoded in the draft-target distributional divergence.
L57: We theoretically prove a structural correspondence between learned linear judges and Kullback-Leibler (KL) divergence, demonstrating they rely on the same underlying logit primitives. Guided by this, we propose a simple, training-free verification mechanism based on KL divergence.
L58: Extensive experiments across reasoning and coding benchmarks show that our method matches or outperforms complex trained judges (e.g., AutoJudge), offering superior robustness to domain shifts and eliminating the supervision bottleneck entirely.
L59: ## 1 Introduction
L60: Large Language Models (LLMs) have demonstrated remarkable capabilities in reasoning and generation (cite40†OpenAI et al., 2024 ; cite41†DeepSeek-AI et al., 2025 ; cite42†Grattafiori et al., 2024 ; cite43†Yang et al., 2025 ), yet their deployment is severely constrained by the high latency and memory bandwidth costs of autoregressive decoding (cite44†Pope et al., 2023 ; cite45†Ivanov et al., 2021 ; cite46†Naveed et al., 2025 ).
L61: To mitigate this, Speculative Decoding (SD) has emerged as a standard acceleration paradigm cite47†Leviathan et al. (2023) ; cite48†Chen et al. (2023) ; cite49†Xia et al. (2024) ; cite50†Sun et al. (2025) . By leveraging a smaller draft model to propose candidate token sequences that are verified in parallel by the larger target model, SD converts memory-bound sequential generation into compute-bound efficient parallel verification.
L62: Standard SD, however, adheres to a strict lossless criterion. It rejects any draft token that does not strictly align with the target model’s distribution. This verification is often overly conservative, rejecting semantically equivalent tokens (e.g., “6+1=7” vs. “6 plus 1 equals 7”) and limiting potential speedups.
L63: To address this, recent research has pivoted towards Judge Decoding (cite51†Bachmann et al., 2025 ), a lossy variant that employs a learned classifier (a “judge”) to assess the semantic validity of draft tokens. These methods rely on expensive supervision (detailed in Section cite10†3 ), including manual annotation cite51†Bachmann et al. (2025) or heuristic mining cite52†Garipov et al. (2025) ; cite53†Yoon et al. (2025) ; cite54†Fu et al.
L64: (2025) , to teach a classifier to distinguish between “critical” errors and harmless deviations.
L65: cite55†Image: Refer to caption Figure 1: Relationship between AutoJudge score and token-level KL divergence. Higher AutoJudge scores indicate more critical tokens, which coincide with larger KL divergence and stronger target–draft disagreement (Case 1: inconsistent key numbers). Conversely, low scores correspond to small KL divergence and minor, non-semantic deviations (Case 2: capitalization only).
L66: Despite the empirical success of judge decoding, the underlying nature of the “criticality” captured by these methods remains opaque. In this work, we investigate the relationship between the learned scoring mechanism of the classifier and the intrinsic distributional statistics of the draft and target models, uncovering a fundamental connection that prior works have overlooked.
L67: As illustrated in Figure cite56†1 , taking AutoJudge (cite52†Garipov et al., 2025 ) as a representative instance, we observe that its assigned criticality scores exhibit a high degree of alignment with the token-level Kullback-Leibler (KL) divergence.
L68: In Case 1, where the draft model introduces a factual error by miscalculating the time (predicting “$4/4$” instead of the correct “$4/1$”), this discrepancy manifests as a sharp distributional shift between the draft and target models, resulting in both a high AutoJudge score and a large KL divergence. Conversely, in Case 2, a non-semantic capitalization difference triggers neither a high judge score nor a significant distributional divergence.
L69: These observations motivate a first-principle hypothesis: the “criticality” learned by complex judges is already inherently encoded in the draft–target distributional divergence. We argue that the scoring function acquired through costly supervision (e.g., in AutoJudge) is essentially a proxy for intrinsic model disagreement.
L70: By bridging learned scoring mechanisms with these intrinsic statistics, we propose that a simple, training-free distributional check can effectively substitute for judges that rely on complex supervision signal mining. We ground this proposal theoretically by proving that learned judges and intrinsic divergence share identical logit primitives (linear vs.
L71: quadratic), suggesting that the efficacy of expensive supervision can be achieved through purely statistical means while naturally avoiding the generalization fragility of task-specific training. Our contributions are summarized as follows:
L72:   1. 1.
L73: 
L74: We empirically revisit judge decoding and find that supervision-trained criticality scores are strongly aligned with draft–target distributional disagreement at the token level, suggesting the “criticality” signal is model-intrinsic.
L75: 
L76:   2. 2.
L77: 
L78: We theoretically establish a structural correspondence between learned judges and KL divergence, proving that the learned “criticality” relies on the same logit primitives as intrinsic divergence metrics.
L79: 
L80:   3. 3.
L81: Guided by our theoretical findings, we propose a training-free verification method. Empirical validation confirms that simple distributional metrics (e.g., KL divergence) effectively replace costly trained classifiers, achieving comparable or superior performance.
L82: cite57†Image: Refer to caption Figure 2: Judge decoding as learning distributional discrepancy. (a) Manual-annotation pipeline. (b) Divergence-point mining without manual labels; (c) We show that a linear judge’s score is empirically correlated with and theoretically connected to distributional divergence (e.g., KL divergence).
L83: ## 2 Background
L84: 
L85: To contextualize our approach, we briefly review the paradigm of speculative decoding and its recent evolution towards semantic-level verification, specifically judge decoding.
L86: ### 2.1 Speculative Decoding
L87: To accelerate the memory-bound autoregressive inference of LLMs, SD employs a draft-then-verify strategy to increase concurrency cite48†Chen et al. (2023) ; cite47†Leviathan et al. (2023) . Instead of generating one token at a time, a smaller draft model $\mathcal{M}_{D}$ first autoregressively produces a candidate block of $\gamma$ tokens, $\mathbf{d}_{t:t+\gamma-1}$, given a prefix $\mathbf{x}_{<t}$. The large target model $\mathcal{M}_{T}$ then evaluates all candidates in a single parallel forward pass.
L88: To ensure the output distribution matches $\mathcal{M}_{T}$ exactly (lossless decoding), a rejection sampling mechanism is applied: a token $d_{t+i}$ is accepted with probability $\min(1,\frac{P_{T}(d_{t+i})}{P_{D}(d_{t+i})})$. This paradigm allows the system to generate multiple tokens per expensive model call, effectively converting memory-bound sequential operations into compute-bound parallel verification.
L89: ### 2.2 Judge Decoding
L90: 
L91: While SD guarantees mathematical equivalence to the target distribution, this strict alignment can be overly conservative. For instance, a draft “6+1=7” might be rejected if the target model prefers “6 plus 1 equals 7”, despite their semantic equivalence. This strictness limits the effective speedup.
L92: To address this, recent works have proposed judge decoding cite51†Bachmann et al. (2025) ; cite52†Garipov et al. (2025) . The core motivation stems from the insight that a model’s reaction to processing a token reveals more than just softmax probabilities. Specifically, the last hidden layer embeddings of erroneous tokens effectively “flag” errors and contradictions, reflecting the model’s intrinsic tendency to rectify mistakes immediately cite51†Bachmann et al. (2025) ; cite58†Servedio et al.
L93: (2025) ; cite59†Azaria and Mitchell (2023) . Leveraging this latent error-signaling behavior, judge decoding employs a learnable verifier (or “judge”) $f_{\phi}$, typically a lightweight classifier on top of the embeddings $\mathbf{h}$, to assess the validity of the drafted block. A candidate is accepted if $f_{\phi}(\mathbf{h})>\tau$ for a predefined threshold $\tau$.
L94: By shifting from rigid probability comparisons to analyzing these internal validity signals, judge decoding optimizes the trade-off between throughput and generation fidelity, accepting plausibly correct tokens that standard SD would reject. The pipeline of judge decoding is depicted in Figure cite60†2 (c).
L95: ## 3 The Bottlenecks of Supervision in Judge Decoding
L96: While judge decoding represents a paradigm shift in speculative decoding by introducing semantic verification, its efficacy is fundamentally constrained by the quality and acquisition cost of the supervision signals used to train the judge. As shown in Figure cite60†2 , current approaches typically derive supervision either from expensive manual annotation or heuristic model rollouts, inevitably inheriting the generalization fragility of task-specific training.
L97: This section critically examines these two paradigms to highlight the trade-offs between annotation cost, label granularity, and signal stability.
L98: ### 3.1 Judge Decoding With Manual Annotation
L99: 
L100: cite51†Bachmann et al. (2025) introduced the judge decoding framework as a verification paradigm that augments the target model with a lightweight classifier to assess token acceptability. This design effectively highlights the promise of learning correctness-aware verification beyond traditional probability alignment. However, two critical limitations hinder its widespread adoption:
L101: 
L102:   1. 1.
L103: Costly and Misaligned Supervision. Training relies on manual annotations of factual or reasoning mistakes. This process is not only prohibitively expensive but also prone to alignment mismatch: human annotators judge plausibility based on external knowledge, which may differ from the model’s intrinsic “knowledge boundary”. A token might be factually true but out-of-distribution for the model, or vice versa.
L104: 
L105:   2. 2.
L106: Coarse-grained Span Labeling. Existing schemes typically employ a span-based labeling strategy: once an error occurs, all subsequent tokens are labeled as Critical Tokens (negative samples). As shown in Figure cite61†3 , this design fails to isolate the Logic-pivoting Token—the specific token that triggers the reasoning shift. Once the answer includes “Portugal”, every subsequent token is labeled as critical, even though only “Portugal” and “Poland” are the true logic-pivoting tokens.
L107: Figure 3: Illustration of overextended labeling boundaries in manual annotation, adapted from cite51†Bachmann et al. (2025) . Key: Non-critical Tokens, Critical Tokens, Logic-pivoting Tokens. The span-based labeling (red) obscures the true logic-pivoting tokens (red underline), creating noisy supervision signals. cite62†Image: Refer to caption Figure 4: Efficiency analysis of AutoJudge dataset mining.
L108: The substantial growth in GPU hours and memory footprint for larger models highlights a significant scalability bottleneck.
L109: ### 3.2 Judge Decoding Without Manual Annotation
L110: 
L111: To mitigate human dependency, cite52†Garipov et al. (2025) proposed AutoJudge, which mines critical tokens by checking if a token substitution alters the final answer. While this approach automates data collection, it introduces new computational and statistical challenges:
L112: 
L113:   1. 1.
L114: Prohibitive Mining Costs. AutoJudge necessitates counterfactual rollouts at each divergence point. Figure cite63†4 shows that mining supervision for GSM8K with a 70B model consumes about 2,700 GPU hours (NVIDIA L40). This prohibitive cost of data mining undermines the efficiency benefits of speculative decoding and hinders scalability, implicitly constraining the judge’s generalization capabilities due to the difficulty of covering diverse data distributions.
L115: 
L116:   2. 2.
L117: Stochastic Instability. LLM generation is inherently stochastic. A token labeled as “critical” in one rollout might be deemed “non-critical” in another simply due to inherent non-determinism in the generation process. Figure cite64†5 reveals that only 25.4% of tokens maintain consistent criticality across four trials. This high variance injects significant label noise, causing the judge to learn spurious correlations rather than distinguishing between causal logic errors and aleatoric uncertainty.
L118: cite65†Image: Refer to caption Figure 5: Consistency analysis of critical tokens. The low percentage of consistently critical tokens (Level 4) indicates that heuristic mining is heavily influenced by generation randomness.
L119: Summary. Current paradigms face a dilemma: manual annotation provides stable labels but is labor-intensive and coarse, while heuristic mining offers automation but is plagued by high computational costs and stochastic noise. These limitations underscore the need for an efficient and robust alternative, motivating the following section.
L120: ## 4 Can We Bypass Data Annotation?
L121: 
L122: The revisiting analysis in Section cite10†3 exposes critical bottlenecks in current paradigms, thereby naturally leading to a key question: Must the identification of critical tokens rely on external supervision, or can such signals be revealed directly through the models themselves?
L123: ### 4.1 Empirical Perspective
L124: 
L125: To answer the above question, we compare the “criticality” captured by the classifier in AutoJudge against the intrinsic probabilistic states derived from the target distribution $\mathbf{p}_{t}=\mathcal{M}_{T}(\mathbf{x}_{<t})$ and the draft distribution $\mathbf{q}_{t}=\mathcal{M}_{D}(\mathbf{x}_{<t})$. We quantify these states using the following two metrics:
L126: 
L127:   1. 1.
L128: Uncertainty (Entropy) quantifies the predictive uncertainty of the model. For any distribution $\pi\in\{\mathbf{p}_{t},\mathbf{q}_{t}\}$, the entropy is defined as:
L129: 
L130:  | $$H(\pi)=-\sum_{v\in\mathcal{V}}\pi(v)\log\pi(v),$$  |  | (1)
L131: 
L132: where higher entropy indicates a more dispersed probability distribution over the vocabulary $\mathcal{V}$.
L133: 
L134:   2. 2.
L135: 
L136: Disagreement (KL Divergence) captures the structural deviation between the draft and target reasoning paths via:
L137:  | $$D_{\text{KL}}(\mathbf{p}_{t}||\mathbf{q}_{t})=\sum_{v\in\mathcal{V}}\mathbf{p}_{t}(v)\log\frac{\mathbf{p}_{t}(v)}{\mathbf{q}_{t}(v)},$$  |  | (2)
L138: 
L139: which quantifies the distributional disagreement between the two models.
L140: Using these metrics, we investigate the correlation between the learned criticality scores from AutoJudge and intrinsic statistics on the GSM8K dataset. Specifically, we stratify the classifier’s output probabilities, where higher values indicate greater importance to the final answer, into equally spaced bins and compute the average value of the intrinsic indicators within each bin.
L141: As shown in Figure cite66†6 , we observe a strong positive correlation: the average KL divergence rises consistently as the classifier assigns higher criticality scores. This implies that influential tokens typically coincide with regions of high distributional disagreement between the target and draft models. Consequently, the token-level influence that AutoJudge learns to approximate via costly supervision appears to be inherently encoded in the divergence between the models’ probability distributions.
L142: cite67†Image: Refer to caption Figure 6: Correlation between supervised criticality scores and intrinsic model statistics on GSM8K. Samples are stratified into 10 bins based on AutoJudge scores (x-axis). Top: The mean KL divergence (red line) shows a clear upward trend as criticality increases, whereas model entropy (dashed lines) shows no significant correlation. Bottom: The sample count distribution across probability bins (i.e., AutoJudge scores).
L143: Key Insight. The observed correlation suggests an intrinsic connection between criticality and the model’s predictive uncertainty. Rather than requiring additional supervision, this relationship indicates that the existing probabilistic behavior of the models conveys informative cues for identifying critical tokens. Thus, the KL divergence serves as a training-free proxy for locating logic pivots.
L144: To further enhance robustness in practice, we employ a lightweight confidence mask: when the target model exhibits high certainty (i.e., the top-1 probability exceeds 0.9), the system defaults to standard speculative sampling to ensure precision, reserving the KL-based relaxation specifically for tokens where the model faces genuine uncertainty.
L145: ### 4.2 Theoretical Perspective
L146: 
L147: This section characterizes the theoretical alignment between KL-based thresholding and the AutoJudge linear classifier. We first summarize the main intuition in the takeaway below, and then formalize it in Theorem cite68†4.1 .
L148: ###### Takeaway.
L149: 
L150: AutoJudge and KL-based thresholding rely on the same signal, namely how much the target model shifts the draft model’s relative token preferences, expressed via $\Delta_{ij}(x)$ (defined in Eq. (cite69†3 )). AutoJudge learns a linear decision rule over these shifts, while the KL divergence provides a quadratic aggregation of their overall magnitude. As a result, KL-based thresholding can act as a proxy for the same “logic pivots” without dataset mining.
L151: To facilitate the following analysis, we first introduce some necessary notation. Let $x=[h_{t};h_{d}]$ be the concatenated feature vector, where $h_{t},h_{d}\in\mathbb{R}^{d}$ denote the hidden states of the target and draft models. The corresponding logits are given by $z_{t}=W_{t}h_{t}+b_{t}$ and $z_{d}=W_{d}h_{d}+b_{d}$, yielding the output distributions $P_{t}=\mathrm{softmax}(z_{t})$ and $P_{d}=\mathrm{softmax}(z_{d})$.
L152: The theoretical link between the KL measure and the trained classifier is the pairwise logit-gap difference $\Delta_{ij}(x)$, defined for any vocabulary indices $(i,j)$ as
L153:  | $$\Delta_{ij}(x):=(z_{t}(i)-z_{t}(j))-(z_{d}(i)-z_{d}(j)),$$  |  | (3)
L154: 
L155: a fundamental linear primitive that captures the shift in relative preference between tokens when transitioning from the draft to the target model.
L156: 
L157: cite70†Image: Refer to caption L158: 
L159: cite71†Image: Refer to caption L160: 
L161: Figure 7: Accuracy and MAT on GSM8K for Llama-3.2-1B-Instruct/Llama-3.1-8B-Instruct (left) and Llama-3.1-8B-Instruct/Llama-3.1-70B-Instruct (right).
L162: 
L163: cite72†Image: Refer to caption L164: 
L165: cite73†Image: Refer to caption L166: Figure 8: Accuracy and MAT on LiveCodeBench for Llama-3.2-1B-Instruct/Llama-3.1-8B-Instruct (left) and Llama-3.1-8B-Instruct/Llama-3.1-70B-Instruct (right).
L167: ###### Theorem 4.1 (Structural Correspondence of KL and Linear Classifiers).
L168: The empirical alignment between KL-based thresholding and the trained linear classification stems from their shared dependence on the primitives $\Delta_{ij}(x)$: (i) KL Divergence as Quadratic Aggregation: Under a second-order expansion, the KL divergence acts as a weighted quadratic sum of the primitives $\Delta_{ij}(x)$. In this view, KL-based thresholding defines a quadratic decision boundary in the primitive space, sensing the total magnitude of distribution shifts.
L169: (ii) Trained Classifier as Linear Partitioning: The linear classifier identifies critical tokens by defining a linear decision surface in the space of primitives $\Delta_{ij}(x)$, partitioning the feature space based on whether token mismatches lead to a deviation in output quality.
L170: ###### Proof.
L171: 
L172: See Appendix cite31†A.1 for details. ∎
L173: 
L174: Theorem cite68†4.1 attributes the stable agreement between both methods to their shared foundation in the linear primitives $\Delta_{ij}(x)$, differing only in whether they employ quadratic or linear geometry to distinguish token criticality.
L175: ## 5 Experiment
L176: 
L177: cite74†Image: Refer to caption L178: 
L179: cite75†Image: Refer to caption L180: 
L181: Figure 9: Accuracy and MAT on MATH-500-Hard for Llama-3.2-1B-Instruct/Llama-3.1-8B-Instruct (left) and Llama-3.1-8B-Instruct/Llama-3.1-70B-Instruct (right).
L182: 
L183: cite76†Image: Refer to caption L184: 
L185: cite77†Image: Refer to caption L186: 
L187: Figure 10: Accuracy and MAT on MMLU-Pro for Llama-3.2-1B-Instruct/Llama-3.1-8B-Instruct (left) and Llama-3.1-8B-Instruct/Llama-3.1-70B-Instruct (right).
L188: 
L189: ### 5.1 Experimental Setup and Baselines
L190: ##### Benchmarks and Models.
L191: We adopt standard speculative decoding protocols (cite52†Garipov et al., 2025 ) across four benchmarks: GSM8K (cite78†Cobbe et al., 2021 ) and MATH-500-Hard (cite79†Hendrycks et al., 2021 ) for mathematics, LiveCodeBench (cite80†Jain et al., 2025 ) for coding, and MMLU-Pro (cite81†Wang et al., 2024 ) for comprehensive knowledge. Our primary model pairs are Llama-3.2-1B-Instruct/Llama-3.1-8B-Instruct and Llama-3.1-8B-Instruct/Llama-3.1-70B-Instruct (cite42†Grattafiori et al., 2024 ).
L192: Additionally, we evaluate the Qwen3-0.6B/Qwen3-8B pair (cite43†Yang et al., 2025 ) to investigate performance on reasoning-specialized models.
L193: ##### Baselines and Metrics.
L194: We compare our method against five baselines: (i) Vanilla SP (cite48†Chen et al., 2023 ) (standard speculative decoding); (ii) Top-K cite51†Bachmann et al. (2025) , which relaxes verification based on token ranking; (iii) AutoJudge (cite52†Garipov et al., 2025 ), a training-based classifier approach; and two entropy-based methods, (iv) Target-Entropy and (v) Draft-Entropy cite82†Wang et al. (2025) .
L195: Evaluation metrics include Mean Accepted Tokens (MAT) for efficiency, benchmark-specific scores for quality, and end-to-end wall-clock speedup relative to Vanilla SP implemented in vLLM (cite83†Kwon et al., 2023 ). Further details are in Appendix cite37†A.2 .
L196: Table 1: Inference deployment results with vLLM on GSM8K for Llama-3.2-1B-Instruct/Llama-3.1-8B-Instruct (left) and Llama-3.1-8B-Instruct/Llama-3.1-70B-Instruct (right), tested on 8$\times$V100 GPUs. Speed is measured in tokens/s, and Speedup is reported relative to standard speculative decoding (i.e., Vanilla SP).
L197: Method  | Metric  | Llama-3.2-1B-Instruct & Llama-3.1-8B-Instruct
L198: AutoJudge  | Threshold  | 0.01  | 0.07  | 0.09  | 0.14  | 0.22
L199: Acc  | 82.50%  | 80.29%  | 79.39%  | 78.40%  | 75.59%
L200: Speed  | 39.11  | 45.06  | 47.12  | 48.87  | 53.70
L201: Speedup  | 1.02$\times$  | 1.17$\times$  | 1.23$\times$  | 1.27$\times$  | 1.40$\times$
L202: KL  | Threshold  | 0.10  | 0.30  | 0.40  | 0.50  | 0.90
L203: Acc  | 82.77%  | 80.96%  | 81.07%  | 79.46%  | 77.13%
L204: Speed  | 39.58  | 45.35  | 48.35  | 50.96  | 61.45
L205: Speedup  | 1.03$\times$  | 1.18$\times$  | 1.26$\times$  | 1.33$\times$  | 1.60$\times$
L206: Vanilla SP  | Acc  | 82.50%
L207: Speed  | 38.40
L208: Method  | Metric  | Llama-3.1-8B-Instruct & Llama-3.1-70B-Instruct
L209: AutoJudge  | Thr  | 0.04  | 0.07  | 0.09  | 0.14  | 0.22
L210: Acc  | 92.77%  | 92.54%  | 92.09%  | 91.08%  | 89.96%
L211: Speed  | 27.34  | 29.55  | 30.98  | 32.57  | 35.07
L212: Speedup  | 1.13$\times$  | 1.22$\times$  | 1.28$\times$  | 1.35$\times$  | 1.45$\times$
L213: KL  | Thr  | 0.20  | 0.40  | 0.50  | 0.90  | 1.40
L214: Acc  | 92.69%  | 91.94%  | 91.88%  | 91.28%  | 90.27%
L215: Speed  | 27.21  | 30.10  | 31.49  | 33.21  | 35.10
L216: Speedup  | 1.12$\times$  | 1.24$\times$  | 1.30$\times$  | 1.37$\times$  | 1.45$\times$
L217: Vanilla SP  | Acc  | 93.00%
L218: Speed  | 24.19
L219: ### 5.2 Main Results
L220: ##### Superior Efficiency-Accuracy Trade-off.
L221: We first compare methods on GSM8K and LiveCodeBench (Figures cite84†7 -cite85†8 ). The training-free KL thresholding exhibits highly consistent trends with the training-based AutoJudge, often outperforming it slightly. Specifically, on the Llama-1B/8B pair for GSM8K, KL thresholding improves MAT by 63.5% (10.61$\rightarrow$17.35) over Vanilla SP with only a $\sim$2% accuracy drop. Similarly, on the 8B/70B pair, MAT increases by 128.8% (13.35$\rightarrow$30.55) with a negligible $\sim$1% accuracy decrease.
L222: In contrast, baselines like Top-K and entropy-based strategies suffer from a much sharper accuracy degradation as MAT increases. A similar MAT–accuracy trade-off is also observed on LiveCodeBench, where code generation requires strict precision. KL thresholding improves MAT by 104.0% (1B/8B, 8.83$\rightarrow$18.01) and 53.7% (8B/70B, 11.49$\rightarrow$17.66) with only minimal performance loss. Its performance is comparable to AutoJudge, and is even slightly better in some settings.
L223: In comparison, Top-K and entropy-based strategies often fail to preserve code correctness, frequently resulting in non-executable programs. Overall, the consistently similar trends observed between KL thresholding and AutoJudge suggest that KL thresholding can serve as a strong and effective proxy for the verification signal, which aligns well with our motivation outlined in Section cite13†4 to leverage model-intrinsic signals for judge decoding.
L224: ##### Robustness to Domain Shift.
L225: To evaluate generalization, we test on MATH-500-Hard and MMLU-Pro benchmarks (Figures cite86†9 -cite87†10 ) using the AutoJudge classifier trained only on GSM8K, as domain-specific supervision is often unavailable. The results indicate that KL thresholding demonstrates superior robustness compared to AutoJudge.
L226: Specifically, on MATH-500-Hard, KL thresholding improves MAT from 13.93 to 32.02 (1B/8B) with a negligible $<$1% performance drop, and also increases MAT from 13.18 to 26.67 (8B/70B) with about a 1.5% performance drop. Conversely, the GSM8K-trained AutoJudge classifier becomes brittle under this domain shift, showing clear accuracy degradation comparable to the weaker Top-K baseline.
L227: This observation confirms that simple, training-free distributional statistics serve as a more reliable proxy for verification signals than classifiers trained on limited domains.
L228: ##### Real-world Speedup in vLLM.

