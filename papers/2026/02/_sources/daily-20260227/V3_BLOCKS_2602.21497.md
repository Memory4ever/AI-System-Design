[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: See It, Say It, Sorted: An Iterative Training-Free Framework for Visually-Grounded Multimodal Reasoning in LVLMs

[3] h6: Abstract

[4] p: Recent large vision-language models (LVLMs) have demonstrated impressive reasoning ability by generating long chain-of-thought (CoT) responses. However, CoT reasoning in multimodal contexts is highly vulnerable to visual hallucination propagation: once an intermediate reasoning step becomes inconsistent with the visual evidence, subsequent steps—even if logically valid—can still lead to incorrect final answers. Existing solutions attempt to mitigate this issue by training models to “think with images” via reinforcement learning (RL). While effective, these methods are costly, model-specific, and difficult to generalize across architectures. Differently, we present a lightweight method that bypasses RL training and provides an iterative, training-free, plug-and-play framework for visually-grounded multimodal reasoning. Our key idea is to supervise each reasoning step at test time with visual evidence, ensuring that every decoded token is justified by corresponding visual cues. Concretely, we construct a textual visual-evidence pool that guides the model’s reasoning generation. When existing evidence is insufficient, a visual decider module dynamically extracts additional relevant evidence from the image based on the ongoing reasoning context, expanding the pool until the model achieves sufficient visual certainty to terminate reasoning and produce the final answer. Extensive experiments on multiple LVLM backbones and benchmarks demonstrate the effectiveness of our approach. Our method achieves 16.5%–29.5% improvements on TreeBench and 13.7% RH-AUC gains on RH-Bench, substantially reducing hallucination rates while improving reasoning accuracy without additional training.

[5] figure: Figure 1 : Reasoning pattern comparison. (a) Greedy decoding: the base VLM selects the top-1 token at each step; any hallucination in an intermediate step propagates to an incorrect final answer. (b) RLHF-based “think-with-images”: the model learns when to call tools to zoom or crop the image and re-inject cropped regions into the reasoning context—effective but costly and model-specific. (c) Ours: a lightweight, training-free, model-agnostic framework. A supervisor maintains a dynamic visual-evidence pool to detect and correct hallucination steps. When uncertainty arises, it invokes a visual decider to extract new evidence, enabling visually grounded reasoning throughout the chain.

[6] h2: 1 Introduction

[7] p: Large vision–language models (LVLMs) now generate long chain-of-thought (CoT) explanations and solve diverse multimodal reasoning tasks [ 22 , 23 , 7 , 18 , 20 ] . Yet, the very ability to “think more” often coincides with “seeing less”. [ 10 ] During inference-time decoding, a model must balance three competing contexts: the image, a growing textual context, and instruction tokens. As the context lengthens, subtle but decisive visual cues are easily dominated by language priors. Even a single token that departs from the visual evidence can steer the remaining chain of thought toward a fluent but visually inconsistent trajectory ( Fig. 1 (a)). This reasoning–perception drift originates at decoding time—not because the model lacks visual understanding, but because long-horizon token generation gradually amplifies language priors over visual grounding [ 25 , 11 , 9 , 17 ] .

[8] p: A prevailing solution is to explicitly train models to “think with images” by learning when and where to zoom or crop during CoT generation ( Fig. 1 (b)). These RL- or preference-optimization pipelines train a policy to call visual tools, inspect regions, and re-inject pixels into the reasoning context. While effective, they rely on curated data, reward design, heavy computation, and tight coupling to specific backbones. The learned policy intertwines spatial exploration with the CoT, repeatedly encoding cropped views and incurring latency. As model scale increases, such visually grounded training becomes prohibitively expensive, limiting accessibility for broader use.

[9] p: To address these limitations, we pursue a different principle: rather than learning when to look at training time, we supervise each reasoning step with visual evidence at test time ( Fig. 1 (c)). We introduce an iterative, training-free, plug-and-play framework that treats decoding as a sequence of evidence-justified token selections. The system maintains a textual evidence pool that operates alongside the base LVLM. At each step, the LVLM proposes a compact top-k set of candidate tokens from its local probability distribution. A lightweight supervisor computes an evidence-induced preference over these candidates and negotiates a reweighted distribution with the base probabilities, preserving confident behavior while reallocating probability mass toward tokens consistent with accumulated evidence. When residual uncertainty remains, a visual decider inspects the image under the current reasoning context and generates a concise micro-observation in natural language. This observation is appended to the evidence pool and reused in all subsequent reasoning steps.

[10] p: This design exhibits three key properties that directly mitigate the limitations of RL-based pipelines such as PixelReasoner [ 19 ] and DeepEyes [ 29 ] . First, it is training-free and inherently transferable: the framework wraps around a frozen LVLM with a lightweight decider, requiring no task-specific finetuning or policy optimization. Second, it is cost-aware by construction. A simple uncertainty test on the negotiated distribution determines whether to invoke the decider, ensuring that additional visual computation occurs only when most likely to prevent a hallucination. Third, it represents evidence in text rather than pixels, enabling subsequent tokens to directly reference prior micro-observations without repeatedly re-encoding image crops. This textual form makes the framework easier to deploy at inference time and substantially reduces computational overhead compared with pixel-level reasoning.

[11] p: Empirically, the framework improves both grounding and end-task accuracy across backbones and benchmarks while keeping overhead modest. Because evidence is accumulated on demand, fine-grained cues can be reused downstream to stabilize the remainder of the chain. Qualitative analyses show that many previously cascading failures reduce to one or two decisive micro-observations that the decider contributes precisely at uncertain steps; Quantitatively, we observe a clear accuracy–latency trade-off as the uncertainty threshold varies, allowing flexible adaptation to different deployment budgets.

[12] p: The main contributions are summarized as follows:

[13] p: We present a training-free, plug-and-play decoding framework that supervises token selection with a growing textual evidence pool and negotiates next-token probabilities with the base model rather than relying on learned tool-calling policies.

[14] p: An uncertainty-triggered visual decider emits concise, reusable micro-evidence only when necessary, yielding strong cost–accuracy trade-offs.

[15] p: The approach transfers across LVLM backbones and consistently reduces hallucination while obviously improving task accuracy on a wide range of benchmarks.

[16] figure: Figure 2 : Overview of evidence-constrained reweighting decoding (ECRD) at decoding step i i . The base VLM emits a top-k candidate set; the supervisor builds an evidence-induced distribution from the current evidence pool and negotiates with the base probabilities to reweight candidates. If confidence remains low, the visual decider reads the image with the current prefix, commits a token, and adds a short textual evidence for later steps.

[17] h2: 2 Methodology

[18] h3: 2.1 Visual Description Grounded Decoding

[19] p: Let a VLM define, at decoding step i i , a next-token distribution:

[20] table: p i ​ ( w ) = p VLM ​ ( x i = w ∣ x < i ) , w ∈ 𝒱 . p_{i}(w)\;=\;p_{\text{VLM}}(x_{i}{=}w\mid x_{<i}),\qquad w\in\mathcal{V}.\vskip-4.0pt (1)

[21] p: Visual description grounded decoding (VDGD) first asks the model to produce one global textual description d = ( d 1 , … , d L ) d=(d_{1},\dots,d_{L}) of image and then constrains decoding by knee truncation to select top- ​ k \text{top-}k plausible tokens and a description-based KL preference. If p ( 1 ) ≥ p ( 2 ) ≥ ⋯ p_{(1)}\!\geq\!p_{(2)}\!\geq\!\cdots are sorted probabilities of p i p_{i} , the knee index can be defined as follows:

[22] table: k ⋆ = arg ⁡ max k ⁡ ( p ( k ) − p ( k + 1 ) ) . k^{\star}=\arg\max_{k}\big(p_{(k)}-p_{(k+1)}\big).\vskip-4.0pt (2)

[23] p: And then we can define the candidate set:

[24] table: 𝒞 i = Top- ​ k ⋆ ​ ( p i ) . \mathcal{C}_{i}=\text{Top-}k^{\star}\!\big(p_{i}\big).\vskip-4.0pt (3)

[25] p: For a candidate token w ∈ 𝒞 i w\in\mathcal{C}_{i} and a prefix of description length j j ( 1 ≤ j ≤ L 1\leq j\leq L ), VDGD measures the deviation:

[26] table: KL ( onehot ( w ) ∥ p VLM ( ⋅ ∣ d < j ) ) = − log p VLM ( w ∣ d < j ) , \mathrm{KL}\!\left(\mathrm{onehot}(w)\,\big\|\,p_{\text{VLM}}(\cdot\mid d_{<j})\right)=-\log p_{\text{VLM}}(w\mid d_{<j}), (4)

[27] p: then takes a minimum value over j j (the best prefix) and replaces the base logits with these values before softmax. While effective in its one-shot setting, fixed logit replacement tied to a single static caption is less self-adaptive, and it does not preserve the base model’s calibrated confidence on already-confident steps.

[28] h3: 2.2 Distribution Supervisor

[29] p: As shown in Fig. 2 , The distribution supervisor keeps the spirit of description-guided preference yet makes two principled changes: (a) we convert VDGD’s min-over-prefix KL into a mean-over-prefix probability that is further averaged across multiple evidences, and (b) we mix the evidence-induced distribution with the base model instead of overwriting logits.

[30] p: From VDGD’s KL to ECRD’s evidence score. Let ℰ i = ( e 1 , … , e L ) \mathcal{E}_{i}=(e_{1},\dots,e_{L}) be a piece of evidence sentence. VDGD’s min-over-prefix KL is well suited to the static captioning regime where the most supportive partial description is selected. In our dynamic regime, where evidence accrues incrementally over steps and will be mixed with the base distribution, thus, we need an aggregator that rewards sustained support across the sentence rather than one sharp peak without robustness, and compiles smoothly across multiple evidence. We therefore replace the min with a mean-over-prefix probability:

[31] table: q ℰ ​ ( w ) = 1 L ​ ∑ j = 1 L p VLM ​ ( w ∣ e < j ) . q_{\mathcal{E}}(w)\;=\;\frac{1}{L}\sum_{j=1}^{L}p_{\text{VLM}}(w\mid e_{<j}). (5)

[32] p: Given a pool E i = { ℰ 1 , … , ℰ N } E_{i}=\{\mathcal{E}_{1},\dots,\mathcal{E}_{N}\} of evidence available at step i i , we average their supports:

[33] table: S i ​ ( w ) = − log ⁡ ( 1 N ​ ∑ ℰ q ℰ ​ ( w ) ) , S_{i}(w)\;=\;-\log\!\Big(\tfrac{1}{N}\sum_{\mathcal{E}}q_{\mathcal{E}}(w)\Big), (6)

[34] p: and restrict to 𝒞 i \mathcal{C}_{i} to obtain the evidence-induced distribution:

[35] table: r i ​ ( w ) = { exp ⁡ { − S i ​ ( w ) } ∑ u ∈ 𝒞 i exp ⁡ { − S i ​ ( u ) } , w ∈ 𝒞 i , 0 , otherwise . r_{i}(w)=\begin{cases}\displaystyle\dfrac{\exp\{-S_{i}(w)\}}{\sum_{u\in\mathcal{C}_{i}}\exp\{-S_{i}(u)\}},&w\in\mathcal{C}_{i},\\[8.0pt] 0,&\text{otherwise}.\end{cases} (7)

[36] p: Negotiated reweighting. Let p i p_{i} be the base distribution. We form a mass-matched version r ~ i \tilde{r}_{i} , the rationale is as follows: p i p_{i} and the evidence-induced distribution r i r_{i} are not on the same scale. r i r_{i} is normalized only over the candidate set 𝒞 i \mathcal{C}_{i} (and zero elsewhere), whereas p i p_{i} spreads probability over the full vocabulary. We therefore perform a proportional rescaling of r i r_{i} within 𝒞 i \mathcal{C}_{i} so that the total mass assigned to 𝒞 i \mathcal{C}_{i} matches that of p i p_{i} . The resulting scaled distribution is denoted r ~ i \tilde{r}_{i} . Concretely,

[37] table: r ~ i ​ ( w ) = { r i ​ ( w ) ⋅ ∑ u ∈ 𝒞 i p i ​ ( u ) ∑ u ∈ 𝒞 i r i ​ ( u ) , w ∈ 𝒞 i , 0 , otherwise , \tilde{r}_{i}(w)\;=\;\begin{cases}\displaystyle r_{i}(w)\cdot\frac{\sum_{u\in\mathcal{C}_{i}}p_{i}(u)}{\sum_{u\in\mathcal{C}_{i}}r_{i}(u)},&w\in\mathcal{C}_{i},\\[6.0pt] 0,&\text{otherwise},\end{cases} (8)

[38] p: which ensures that we only reallocate the probability mass within 𝒞 i \mathcal{C}_{i} without varying its total amount:

[39] table: ∑ w ∈ 𝒞 i r ~ i ​ ( w ) = ∑ w ∈ 𝒞 i p i ​ ( w ) . \sum_{w\in\mathcal{C}_{i}}\tilde{r}_{i}(w)=\sum_{w\in\mathcal{C}_{i}}p_{i}(w). (9)

[40] p: and then let the base distribution and the evidence-induced distribution negotiate a mixture:

[41] table: p i mix ​ ( w ) = { α i ​ p i ​ ( w ) + ( 1 − α i ) ​ r ~ i ​ ( w ) , w ∈ 𝒞 i , α i ​ p i ​ ( w ) , w ∉ 𝒞 i . p_{i}^{\text{mix}}(w)=\begin{cases}\alpha_{i}\,p_{i}(w)+(1-\alpha_{i})\,\tilde{r}_{i}(w),&w\in\mathcal{C}_{i},\\[4.0pt] \alpha_{i}\,p_{i}(w),&w\notin\mathcal{C}_{i}.\end{cases} (10)

[42] p: The adaptive weight is chosen without hyper-parameters as:

[43] table: α i = p ( 1 ) , \alpha_{i}\;=\;p_{(1)}, (11)

[44] p: the top probability of the base model before mixing. This choice aligns with empirical statistics reported by [ 5 ] : hallucination steps tend to have larger knee-selected k ⋆ k^{\star} and diffuse local distributions with small variance. However, non-hallucination steps are sharply peaked with average k ⋆ ≈ 1 k^{\star}\!\approx\!1 . Consequently, when p ( 1 ) p_{(1)} is large (confident step), we keep the base distribution predominates; when p ( 1 ) p_{(1)} is small (hallucination-critical moments), evidence receives more weight. It reflects a general intervention principle: when the base distribution is sharp, evidence should act as a light prior; when it is diffuse, evidence should carry more weight. This makes mixture responsive to local uncertainty while preserving the behavior of base model in easy steps.

[45] p: When to acquire new evidence. After Eq. 10 , we inspect the negotiated margin:

[46] table: Δ i = p ( 1 ) mix − p ( 2 ) mix . \Delta_{i}\;=\;p^{\text{mix}}_{(1)}-p^{\text{mix}}_{(2)}. (12)

[47] p: If k ⋆ > 1 k^{\star}>1 and Δ i ≤ δ \Delta_{i}\leq\delta ( δ \delta is a hyperparameter), we consider step i i a probable trigger for hallucination and acquire new evidence. Otherwise, we directly select p ( 1 ) mix p^{\text{mix}}_{(1)} .

[48] h3: 2.3 Dynamic evidence pool and the visual decider

[49] p: Invocation and interface. When the trigger in Eq. 12 fires, we call a lightweight visual decider instantiated by GRIT [ 4 ] , which built on Qwen2.5-VL-3B [ 1 ] , except for the basic answer, it can optionally output the coordinates of one or more image regions that the model needs to refer to during its reasoning process when generating an answer. GRIT receives the image, the tail of the textual prefix, and the candidates 𝒞 i \mathcal{C}_{i} . It should be noted that GRIT does not receive the original question at this stage, as we only aim to mitigate possible hallucinations occurring in the current step. The model is required to resolve the content of this step alone, rather than the complete question. We obtain (i) a choice w ⋆ ∈ 𝒞 i w^{\star}\in\mathcal{C}_{i} , (ii) a single human-readable evidence sentence ℰ i \mathcal{E}_{i} from its answer. We then force w ⋆ w^{\star} at step i i and append the sentence to the evidence pool:

[50] table: E i + 1 ← E i ∪ { ℰ i } . E_{i+1}\;\leftarrow\;E_{i}\cup\{\mathcal{E}_{i}\}. (13)

[51] p: Representation. Crucially, only the text participates in scoring via Eqs. 5 , 6 and 7 , and coordinates are stored as annotations for interpretability and for binding the sentence to concrete regions but never participate in scoring steps. This design is deliberate. Injecting raw crops back into the context, such as in zoom-in pipelines, repeatedly couples pixel processing with the entire reasoning chain and typically requires additional supervision or preference optimization for the model to learn when and where to zoom. In contrast, textual evidence is compact, semantic, and model-native: it lives in the same token space as the decoder, can be scored without revisiting pixels, and naturally composes with prior sentences. This keeps the intervention lightweight while saving a verifiable trail.

[52] p: Initialization and growth. We initialize E 0 E_{0} with a global description d global d_{\text{global}} to provide broad coverage but not to act as the sole evidence source. Thereafter the evidence pool grows only on demand. This maintains modest computation, preserves determinism in non-ambiguous regions, and lets evidence accumulate precisely where it is most useful for subsequent decisions.

[53] p: Semantics and micro-views. Although textual, each sentence implicitly refers to one or multiple related subviews of the image, especially when GRIT generates the answer with coordinates. Because every sentence is generated to resolve a specific local choice, the evidence pool accumulates a set of semantically linked micro-observations that remain logically connected to the evolving chain of thought. Eqs. 6 and 7 convert these micro-observations into reusable probability mass, allowing later steps to benefit from earlier visual disambiguation without re-encoding crops. Therefore ECRD is a bridge that allows base model to interact with a collection of subviews organized by reasoning needs, rather than with isolated cropped regions, thereby enabling reuse across the whole sequence.

[54] figure: Perception Reasoning Overall Attr. Mater. Phys. ObjRet. OCR Persp. Order. Cont.&Oc. Contain. Compar. Private Models Gemini-2.5-Flash-0520 [ 2 ] 45.9 48.3 53.9 69.6 68.8 75.0 15.3 19.3 56.1 72.4 43.2 GPT-4o-1120 [ 15 ] 46.9 51.7 61.5 65.2 43.8 69.1 18.8 38.6 48.8 72.4 43.2 Gemini-2.5-Pro-0605 [ 3 ] 54.1 51.7 61.5 56.5 75.0 83.8 20.0 36.8 65.9 86.2 54.6 o3-0416 [ 16 ] 54.8 69.0 69.2 65.2 68.8 79.4 22.4 38.6 61.0 86.2 50.0 Open-source General Models Qwen2.5-VL-7B [ 1 ] 37.0 55.2 53.8 56.5 62.5 27.9 20.0 35.1 39.0 44.8 43.2 + ECRD 47.9 ↑ \uparrow 10.9 72.4 ↑ \uparrow 17.2 53.8 0.0 73.9 ↑ \uparrow 17.4 62.5 0.0 54.4 ↑ \uparrow 26.5 20.0 0.0 35.1 0.0 56.1 ↑ \uparrow 17.1 75.9 ↑ \uparrow 31.1 45.5 ↑ \uparrow 2.3 Qwen2.5-VL-32B [ 1 ] 42.5 51.7 53.8 69.6 62.5 54.4 16.5 33.3 46.3 62.1 38.6 + ECRD 48.6 ↑ \uparrow 6.1 62.1 ↑ \uparrow 10.4 53.8 0.0 73.9 ↑ \uparrow 4.3 62.5 0.0 60.3 ↑ \uparrow 5.9 23.5 ↑ \uparrow 7.0 35.1 ↑ \uparrow 1.8 61.0 ↑ \uparrow 14.7 65.5 ↑ \uparrow 3.4 45.5 ↑ \uparrow 6.9 Qwen2.5-VL-72B [ 1 ] 42.2 65.5 69.2 56.5 56.3 48.5 11.8 33.3 51.2 72.4 38.6 + ECRD 49.9 ↑ \uparrow 7.7 65.5 0.0 69.2 0.0 65.2 ↑ \uparrow 8.7 62.5 ↑ \uparrow 6.2 69.1 ↑ \uparrow 20.6 20.0 ↑ \uparrow 8.2 36.8 ↑ \uparrow 3.5 58.5 ↑ \uparrow 7.3 75.9 ↑ \uparrow 3.5 40.9 ↑ \uparrow 2.3 LLaVA-OneVision-7B [ 8 ] 37.3 55.2 53.8 56.5 50.0 32.4 21.2 22.8 41.5 72.4 36.4 + ECRD 43.5 ↑ \uparrow 6.2 55.2 0.0 61.5 ↑ \uparrow 7.7 60.9 ↑ \uparrow 4.4 56.3 ↑ \uparrow 6.3 47.1 ↑ \uparrow 14.7 23.5 ↑ \uparrow 2.3 28.0 ↑ \uparrow 5.2 53.7 ↑ \uparrow 12.2 72.4 0.0 40.9 ↑ \uparrow 4.5 LLaVA-OneVision-72B [ 8 ] 40.5 62.1 53.8 65.2 62.5 36.8 12.9 28.1 53.7 65.5 47.7 + ECRD 46.9 ↑ \uparrow 6.4 62.1 0.0 61.5 ↑ \uparrow 7.7 69.6 ↑ \uparrow 4.4 68.8 ↑ \uparrow 6.3 51.5 ↑ \uparrow 14.7 18.8 ↑ \uparrow 5.9 29.8 ↑ \uparrow 1.7 61.0 ↑ \uparrow 7.3 72.4 ↑ \uparrow 6.9 52.3 ↑ \uparrow 4.6 InternVL3-8B [ 30 ] 38.8 51.7 69.2 56.5 56.3 33.7 21.2 24.6 39.0 72.4 43.2 + ECRD 45.2 ↑ \uparrow 6.4 51.7 0.0 69.2 0.0 69.6 ↑ \uparrow 13.1 62.5 ↑ \uparrow 6.2 50.0 ↑ \uparrow 16.3 24.7 ↑ \uparrow 3.5 29.8 ↑ \uparrow 5.2 43.9 ↑ \uparrow 4.9 72.4 0.0 50.0 ↑ \uparrow 6.8 InternVL3-38B [ 30 ] 42.0 51.7 61.5 52.2 68.8 51.5 12.9 33.3 56.1 65.5 38.6 + ECRD 48.4 ↑ \uparrow 6.4 51.7 0.0 69.2 ↑ \uparrow 7.7 65.2 ↑ \uparrow 13.0 75.0 ↑ \uparrow 6.2 58.8 ↑ \uparrow 7.3 22.4 ↑ \uparrow 9.5 36.8 ↑ \uparrow 3.5 56.1 0.0 69.0 ↑ \uparrow 3.5 50.0 ↑ \uparrow 11.4 InternVL3-78B [ 30 ] 46.4 62.1 61.5 52.2 68.8 52.9 16.5 33.3 61.0 86.2 45.5 + ECRD 50.9 ↑ \uparrow 4.5 65.5 ↑ \uparrow 3.4 69.2 ↑ \uparrow 7.7 65.2 ↑ \uparrow 13.0 75.0 ↑ \uparrow 6.2 60.3 ↑ \uparrow 7.4 21.2 ↑ \uparrow 4.7 35.1 ↑ \uparrow 1.8 63.4 ↑ \uparrow 2.4 86.2 0.0 47.7 ↑ \uparrow 2.2 Open-source Visual Grounded Reasoning Models DeepEyes-7B [ 29 ] 37.5 62.1 53.8 65.2 68.8 51.5 11.8 24.6 36.6 51.7 47.7 Pixel-Reasoner-7B [ 19 ] 39.0 58.6 61.5 65.2 50.0 48.5 14.1 31.6 39.0 44.8 40.9 TreeVGR-7B [ 24 ] 50.4 65.5 53.8 82.6 68.8 63.3 22.4 36.8 61.0 69.0 45.5 Table 1: Results of different models on TreeBench. Best performances for open-source models are highlighted in bold . ECRD consistently improves open-source general models across architectures and scales, confirming training-free plug-and-play applicability.

[55] h2: 3 Experiment

[56] h3: 3.1 Setups

[57] p: We evaluate ECRD across benchmarks grouped by the capabilities they probe: (i) visual grounded reasoning under long chains, (ii) reasoning–perception balance and hallucination control, and (iii) broad multimodal competence. In the experiments reported in Tabs. 1 , 4 , 5 , 3 and 2 , we set the uncertainty threshold δ = 0.08 \delta=0.08 . No additional training are used.

[58] h3: 3.2 Benchmarks and base models

[59] p: Benchmarks. We evaluate on three groups of benchmarks. TreeBench [ 24 ] probes “thinking with images” by separating Perception (identify, localize, read, attribute) from Reasoning (operate over aggregated visual evidence such as occlusion, containment, ordering, perspective); the metric is answer accuracy. RH-Bench [ 10 ] reports Reason and Perception scores and RH-AUC [ 10 ] , which summarizes the trade-off between reasoning length and hallucination (higher is better). For general multimodal competence, we use V*Bench [ 27 ] , MathVista [ 13 ] , ChartQA [ 14 ] , OCRBench [ 12 ] , and HallusionBench [ 6 ] , evaluated by accuracy.

[60] p: Base models. Unless otherwise specified, the visual decider is GRIT-3B [ 4 ] , which is built upon Qwen2.5-VL-3B [ 1 ] and optimized for visual grounding. To assess plug-and-play generality and scale robustness, we also attach ECRD without any finetuning to three open-source general model families: LLaVA-OneVision [ 8 ] (7B and 72B), Qwen2.5-VL [ 1 ] (7B, 32B and 72B), and InternVL3 [ 30 ] (8B, 38B and 78B). All checkpoints and inference recipes follow the authors’ official releases. ECRD modifies only the decoding procedure at test time and leaves the underlying encoders or decoders frozen. For reference lines on TreeBench, we also report private models GPT-4o [ 15 ] and o3 [ 16 ] as well as Gemini-2.5-Flash [ 2 ] and Gemini-2.5-Pro [ 3 ] , and include recent RL-based visually-grounded reasoning systems DeepEyes [ 29 ] , Pixel-Reasoner [ 19 ] , and TreeVGR-7B [ 24 ] for comparison. The paper that presents the TreeVGR-7B [ 24 ] method also introduces TreeBench.

[61] h3: 3.3 Main results and analysis

[62] p: As demonstrated in Tab. 1 , ECRD delivers consistent gains across all open-source general backbones and scales on TreeBench, showing that the method is truly plug-and-play rather than model-specific. On Qwen2.5-VL-7B the overall accuracy rises from 37.0% to 47.9%, and similar improvements appear on LLaVA-OneVision-7B and InternVL3-8B, as well as on larger models such as Qwen2.5-VL-32B/72B, LLaVA-OneVision-72B, and InternVL3-38B/78B, where the absolute lifts are typically in the +4-8 point band. The sub-category pattern matches our design: competencies that rely on checkable visual facts such as OCR, Physical State and Comparison benefit the most. Compared to RLHF-based visual-grounded reasoning models, ECRD on Qwen2.5-VL-7B surpasses DeepEyes-7B and Pixel-Reasoner-7B and approaches TreeVGR-7B, yet it requires no additional training, curated traces, or reinforcement optimization. It also exceeds several strong closed models such as Gemini-2.5-Flash and GPT-4o while still trailing Gemini-2.5-Pro and o3.

[63] p: To further position ECRD against established training-free baselines beyond RL-based systems, we compare it on TreeBench using the same base model (Qwen2.5-VL-7B) with: inference-time correction (Woodpecker [ 28 ] ), programmatic reasoning (ViperGPT [ 21 ] ), and visual prompting (ControlMLLM [ 26 ] ). We also evaluate standard decoding alternatives, including beam search, self-consistency, and diverse sampling. As shown in Tab. 2 , all these baselines underperform ECRD, indicating a significantly better performance of ECRD among plug-and-play approaches.

[64] figure: Method Base Woodpecker ViperGPT ControlMLLM Beam Self-cons. Diverse ECRD Overall 37.0 36.3 38.3 40.5 38.8 39.0 38.3 47.9 Table 2: Comparison with training-free baselines and decoding alternatives on TreeBench. Best result are highlighted in bold . ECRD performs markedly better among all plug-and-play settings.

[65] figure: Perception Reasoning Overall Attr. Mater. Phys. ObjRet. OCR Persp. Order. Cont.&Oc. Contain. Compar. GRIT-3B [ 4 ] 30.1 31.0 23.1 56.5 25.0 39.7 21.2 17.5 36.6 48.3 20.5 Qwen2.5-VL-7B [ 1 ] 37.0 55.2 53.8 56.5 62.5 27.9 20.0 35.1 39.0 44.8 43.2 Qwen2.5-VL-7B + VDGD 39.5 58.6 53.8 52.2 62.5 50.0 17.6 29.8 39.0 48.3 40.9 Qwen2.5-VL-7B + supervisor 40.7 58.6 53.8 56.5 62.5 51.5 18.8 31.6 41.5 44.8 43.2 Qwen2.5-VL-7B + ECRD (Qwen2.5-VL-3B as visual decider) 43.7 62.1 53.8 69.6 62.5 52.9 20.0 31.6 43.9 62.1 43.2 Qwen2.5-VL-7B + ECRD 47.9 72.4 53.8 73.9 62.5 54.4 20.0 35.1 56.1 75.9 45.5 Table 3: TreeBench ablations on Qwen2.5-VL-7B. Best performances are highlighted in bold . The supervisor provides a stable boost and the visual decider adds the remaining lift; both components are necessary and complementary.

[66] figure: Model RH-Bench Reas. Perc. RH-AUC Qwen2.5-VL-7B [ 1 ] 39.6 50.2 0.51 Qwen2.5-VL-7B + supervisor 42.0 53.3 0.54 Qwen2.5-VL-7B + ECRD 46.4 57.1 0.58 Table 4 : Results on RH-Bench. Reas. indicates Reasoning , and Perc. indicates Perception . Best performances are highlighted in bold . ECRD improves both Reasoning and Perception while increasing RH-AUC, indicating a better balance between reasoning and hallucination over longer chains.

[67] figure: Model V* Bench MathVista ChartQA OCRBench HallusionBench Attr Spatial Overall LLaVA-OneVision-7B [ 8 ] 73.0 60.5 68.1 63.2 80.0 62.2 55.1 LLaVA-OneVision-7B + ECRD 74.8 65.8 71.2 67.9 86.3 73.8 63.7 Qwen2.5-VL-7B [ 1 ] 73.9 67.1 71.2 68.2 84.4 82.3 61.3 Qwen2.5-VL-7B + supervisor 73.9 71.1 72.8 69.8 86.8 85.7 67.5 Qwen2.5-VL-7B + ECRD 74.8 75.0 74.9 72.3 88.3 90.7 72.5 Table 5 : Results on five general multimodal benchmarks. Better performances are highlighted in bold . ECRD brings consistent gains across diverse tasks on both Qwen2.5-VL-7B and LLaVA-OneVision-7B, demonstrating backbone-agnostic, task-general effectiveness.

[68] p: Tab. 4 shows that ECRD improves Reasoning from 39.6% to 46.4% and Perception from 50.2% to 57.1%, lifting RH-AUC from 0.51 to 0.58 on RH-Bench . A higher RH-AUC value indicates that as the chain grows longer, accuracy remains at a higher level and the balance between reasoning and hallucination is better maintained.

[69] p: Finally, across five general multimodal benchmarks in Tab. 5 , ECRD brings broad, task-general gains on both Qwen2.5-VL-7B and LLaVA-OneVision-7B: V*Bench overall rises by several points, MathVista and ChartQA see steady improvements, OCRBench jumps by around +8–12 points, and HallusionBench improves by roughly +8–11 points, reflecting fewer visually induced slips that would otherwise propagate through the chain.

[70] h3: 3.4 Ablation study

[71] p: The ablations on Qwen2.5-VL-7B in Tab. 3 isolate where the lift comes from. First, GRIT-3B alone yields the lowest TreeBench accuracy among all rows, yet ECRD, invoking GRIT-3B only at uncertain steps, reaches 47.9% (+17.8 over GRIT-3B and +10.9 over the 7B base), which rules out the hypothesis that gains are driven by a stronger perception model and points instead to the decoding design, specifically ECRD’s ability to fully leverage the small model exactly where it matters. Second, replacing VDGD’s prefix-wise minimum with our mean-over-prefix evidence scoring already helps without any decide, confirming that averaging stabilizes token selection. Third, adding a grounded decider matters: using Qwen2.5-VL-3B, a generic VLM, as the decider improves further, and swapping in the grounding-oriented GRIT-3B yields the full ECRD gains, with the largest margins on visually consequential categories. The same staged pattern appears beyond TreeBench: as shown in Tabs. 4 and 5 , on RH-Bench and on the five general multimodal benchmarks, the variant without the decider consistently lies between the base and the full method, showing that both parts are necessary: the supervisor provides a robust, always-on stabilization under uncertainty, and the visual decider supplies sparse but decisive micro-observations only when ambiguity persists, converting the remaining hard steps and propagating benefits through rest of chain.

[72] figure: Figure 3 : Analysis of the uncertainty threshold δ \delta : accuracy as a function of δ \delta across five benchmarks, and the average visual decider invocation rate (calls per question) as δ \delta varies. The gray dashed line marks δ = 0.08 \delta=0.08 .

[73] figure: Benchmark V* Bench MathVista ChartQA OCRBench HallusionBench t 0 t_{0} 8.98 12.92 9.76 3.24 11.67 l 0 l_{0} 1.32 1.46 1.30 1.12 1.43 Table 6 : Average time per question at δ = 0 \delta=0 ( t 0 t_{0} , seconds per question) and global average latency of a single visual decider call ( l 0 l_{0} , seconds). Note that l 0 l_{0} is computed as an overall mean across all benchmarks and δ \delta settings, and is not restricted to the δ = 0 \delta=0 condition. All tests are conducted on a single H20-NVLink GPU.

[74] figure: Figure 4 : Two typical application cases of ECRD.

[75] figure: Figure 5 : Breakdown of ECRD’s gain on TreeBench based on Qwen2.5-VL-7B.

[76] h3: 3.5 Efficiency analysis and uncertainty threshold

[77] p: ECRD adds two sources of computation on top of the base decoder: (i) evidence scoring over the knee-selected candidate set and (ii) decider calls triggered when uncertainty persists. The former is lightweight. At step t t , after knee truncation produces 𝒞 t = { w 1 , … , w k } \mathcal{C}_{t}=\{w_{1},\ldots,w_{k}\} , scoring requires a pass over the evidence pool E t E_{t} to form the KL-style preference s ⁡ ( w i | E t ) s(w_{i}|E_{t}) . Because each evidence contributes precomputed log-likelihoods on a separate and cache-disabled backend (stored as FP16 on CPU), the inference-time computation is O ⁡ ( k ​ | E t | ) O(k|E_{t}|) with negligible GPU pressure. In practice k k is single-digit and | E t | |E_{t}| grows slowly, so this path contributes only a small fraction of total latency.

[78] p: The heavier component is the visual decider. Let r r denote the average number of decider calls per question. As Fig. 3 shows, increasing the uncertainty threshold δ \delta monotonically raises r r (right panel), while accuracy (left panel) exhibits a consistent elbow: a rapid lift for small δ \delta , followed by saturation. The knee for all five benchmarks concentrates around the gray dashed line ( δ ≈ 0.08 \delta\approx 0.08 ), which is precisely where the negotiated distribution most often flags genuinely ambiguous, visually charged steps. Benchmarks whose items hinge on precise perceptual grounding such as OCRBench and HallusionBench benefit early and strongly, their curves rise steeply with a small number of calls, whereas tasks that already align well with text-only priors like ChartQA show milder, earlier saturation. MathVista and V* Bench lie in between: accuracy improves steadily as a handful of targeted micro-observations are injected, then flattens when further calls add little new information. Importantly, beyond the knee, the invocation of visual decider grows faster than accuracy, and some curves even level off or gently fluctuate, reflecting diminishing returns once the few decisive ambiguities have been resolved.

[79] p: The cost trend aligns with a simple latency model grounded in Tab. 6 . Let t 0 t_{0} be the base time per question at δ = 0 \delta=0 (no calls) and l 0 l_{0} be the average marginal latency of a single call. Then the end-to-end time obeys

[80] table: T ⁡ ( δ ) ≈ t 0 + l 0 ​ r ​ ( δ ) . T(\delta)\approx t_{0}+l_{0}\,r(\delta). (14)

[81] p: with t 0 t_{0} varying by benchmark and l 0 l_{0} staying in a narrow band (single-second scale) across settings. Combined with Fig. 3 , this explains the observed cost–accuracy balance: near δ ≈ 0.08 \delta\approx 0.08 , accuracy captures most of the attainable gain while r r remains in the low single-digit regime, yielding modest overhead relative to t 0 t_{0} , whereas pushing δ \delta higher mainly increases r r (and thus T T ) with little additional accuracy. Hence we adopt δ = 0.08 \delta=0.08 as a default: it lies at the elbow where added calls cease to be cost-effective, yet the model already recovers most of the gains in Tabs. 1 , 4 , 5 , 3 and 2 .

[82] h3: 3.6 Qualitative analysis: how ECRD works

[83] p: As shown in Figs. 2 and 4 , we present three representative cases that correct typical failure modes, corresponding to ECRD’s two components—the supervisor and the visual decider: (i) negotiated reweighting with textual evidence and (ii) on-demand visual arbitration when uncertainty persists.

[84] p: Case A: Negotiated evidence resolves the step. As shown in Fig. 4 , the question asks whether rubber cars are fewer than brown jets. At critical steps, ECRD does not trigger the decider because of the large reweighted gap, instead, it reweights the candidates so that tokens consistent with evidence are favored, yielding the correct answer “Yes” .

[85] p: Case B.1: Visual decider supplies mid-chain grounding. As shown in Fig. 2 (full examples are provided in supplementary material), at the key step the candidate set is { “blue”, “red” }. The base slightly prefers “red”, while the evidence-induced distribution prefers “blue”; the negotiated gap remains small, so the trigger fires. This choice is pivotal for the rest of the chain: if the model commits to “red”, the subsequent localization and description would drift toward the red garment and propagate errors. The visual decider reads the image with the current prefix and returns the grounding sentence: “The first dress from the right-hand side is blue, partially hidden by the tree.” ECRD forces “blue” for the current step and adds this sentence to the pool. Later tokens then follow this micro-observation to correctly describe all three dresses and reach the right final color judgment for the queried position.

[86] p: Case B.2: Visual decider supplies the final answer. As shown in Fig. 4 , here the candidate set at the decisive step is { “5”, “3” }. The base leans toward “5”, the evidence-induced distribution leans toward “3”, and the small negotiated gap triggers the decider. The visual decider localizes the tag behind the box and returns: “The number behind the cardboard box with the ‘favorita’ brand and banana illustration is ‘300’ .” ECRD commits token “3” and inserts the sentence into the pool; at the next two steps the supervisor prefers tokens consistent with this evidence, selecting “0” then “0” without additional calls. The chain thus outputs the correct answer “300” .

[87] p: Where the gains come from. Based on a detailed statistical analysis of the experimental results, we find that on Qwen2.5-VL-7B, ECRD yields a +10.9-point overall improvement on TreeBench. As shown in Fig. 5 , within this lift, cases where the visual decider directly outputs the final answer account for 11.4% of the gain, while cases where the decider injects a mid-chain visual grounding that unlocks the rest of the reasoning account for 18.2%. The remaining improvement primarily comes from the supervisor’s negotiated reweighting and the indirect benefits of an expanding evidence pool, which stabilizes later token choices even when no further decider calls are needed.

[88] h2: 4 Conclusion

[89] p: We presented ECRD, a decoding-time, training-free, plug-and-play framework for visually grounded reasoning. By reconciling base probabilities with an evidence-guided distribution, ECRD preserves model confidence, invokes a lightweight visual decider only when necessary, and propagates visual grounding through reasoning chain. Experiments show consistent gains across diverse benchmarks.

[90] h2: References

[91] h2: Instructions for reporting errors

[92] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[93] p: Tip: You can select the relevant text first, to include it in your report.

[94] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[95] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
