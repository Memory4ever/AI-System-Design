[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] p: ﻿

[3] h1: Beyond Dominant Patches: Spatial Credit Redistribution For Grounded Vision-Language Models

[4] h6: Abstract

[5] p: Vision-language models (VLMs) frequently hallucinate objects absent from the input image. We trace this failure to spatial credit collapse : activation credit concentrating on sparse visual patches in early transformer layers, which suppresses contextual evidence and increases reliance on language priors. We introduce Spatial Credit Redistribution (SCR) , a training-free inference-time intervention that redistributes hidden-state activation from high-attention source patches to their 8-connected spatial neighbors, which increases the aggregate ℓ 2 \ell_{2} norm by ≈ 51 % {\approx}51\% and restores suppressed visual context. SCR does not require retraining and is applied via forward-pass hooks on existing VLMs. We evaluate six model configurations spanning three model families (Chameleon, LLaVA, and Qwen, including both Qwen-VL and Qwen2-VL) at scales of 7B, 13B, and 30B, on POPE and CHAIR benchmarks. SCR reduces hallucination by ≈ {\approx} 4.7-6.0 pp on POPE-Adversarial, cuts CHAIR-s by 3.7-5.2 pp (42-51% relative) and CHAIR-i by 2.7-4.0 pp (44-53% relative), and preserves CIDEr within 0.8 pp. Gains are largest for low-entropy inputs, consistent with the theoretical framework. SCR incurs only + + 43-56 ms overhead (small models: + + 43-46 ms; large models: + + 54-56 ms), roughly 3 3 - 6 × 6{\times} lower than OPERA and VCD and 1.3 1.3 - 1.7 × 1.7{\times} lower than OA-VCD ( + + 72 ms), while Pareto-dominating all three on both hallucination rate and CIDEr, making it practical for real-time settings. A controlled ablation confirms that attention-guided source selection is essential: replacing it with uniform random selection reduces HR gains from ≈ {\approx} 4.7-6.0 pp to only ≈ {\approx} 2.6-3.4 pp, pointing to credit-collapse as the key driver.

[6] h6: Keywords:

[7] h2: 1 Introduction

[8] p: Vision-Language Models (VLMs) [ 21 , 20 , 15 , 31 ] have achieved strong performance across vision and multimodal tasks by aligning visual encoders [ 25 , 4 ] with Large Language Models (LLMs). Most of them fall victim to object hallucination . This occurs when a VLM generates descriptions of objects that are not present in the input image [ 16 , 6 , 19 , 11 ] . Existing hallucination mitigation methods often rely on expensive retraining models, such as RLHF [ 29 , 24 ] or instruction tuning [ 18 ] , or trade off generation fluency through aggressive decoding constraints [ 14 , 12 ] . These methods primarily treat hallucinations as a language modeling problem and do not directly address the underlying visual grounding problem.

[9] p: In this work, we present evidence that hallucination is associated with visual evidence becoming overly concentrated in sparse regions of the representation. This concentration reduces the diversity of contextual information available to the model and increases reliance on language priors (statistical patterns learned from text training data). We term this pattern spatial credit collapse and propose Spatial Credit Redistribution (SCR) as a corrective intervention. While the relationship is established empirically rather than causally, the entropy-hallucination correlation ( r = − 0.65 r=-0.65 , p < 0.001 p<0.001 ) and the controlled Uniform-Smooth ablation together provide strong grounding for the mechanism.

[10] p: SCR operates directly on hidden-state representations. It increases the spatial credit entropy of the model while retaining existing discriminative visual evidence. We do this by redistributing the activation credit across spatially adjacent visual tokens at inference time.

[11] p: Our main contributions are: an empirically based framework that formalizes spatial credit entropy; the introduction of Spatial Credit Redistribution (SCR); and an evaluation of SCR’s effectiveness on several benchmarks, with ablations across three VLM families (Chameleon, LLaVA, Qwen) at multiple model scales (7B, 13B, and 30B).

[12] h2: 2 Related Work

[13] p: Vision-Language Models and Hallucination. Most VLMs follow connector-based (BLIP-2 [ 15 ] , LLaVA [ 21 , 20 ] ) or early-fusion (Chameleon [ 31 ] ) architectures, yet all remain prone to object hallucination [ 16 , 6 ] .

[14] p: Hallucination Mitigation through Training. HIO [ 23 ] reduces hallucinations but requires full retraining. RLHF [ 29 , 3 ] , instruction tuning [ 18 ] , and DPO [ 36 , 26 ] all improve hallucination rates through training, but the substantial computational cost limits their scalability to larger models.

[15] p: Inference-Time Decoding Approaches. VCD [ 14 ] applies visual contrastive decoding ( + + 153 ms overhead); OPERA [ 12 ] applies an attention penalty via beam search ( + + 267 ms overhead). OA-VCD [ 10 ] refines VCD with adversarial perturbations of vision-encoder features to create a more object-targeted contrastive signal, reducing overhead to approximately + + 72 ms while maintaining comparable hallucination reduction. All three improve hallucination rates at a non-trivial latency cost, in contrast to the + + 43-56 ms incurred by SCR.

[16] p: Training-Free Representation Interventions. VLI [ 22 ] applies bi-causal attention steering via a diagnostic pass, and CRoPS [ 1 ] extends contrastive decoding to both vision-deficit and text-deficit modes; both are concurrent preprints included in our evaluation for completeness. SID [ 13 ] proposes self-introspective decoding, and modular attribution [ 34 ] targets specific attention heads.

[17] p: Mechanistic Analysis. Attention manipulation [ 33 ] has been studied for efficiency and interpretability, but its use for hallucination mitigation [ 18 ] remains under-explored. Feature attribution [ 30 ] , universal attention head analysis [ 8 ] , and knowledge erasure [ 7 ] are closely related, yet none directly address the spatial credit collapse that causes hallucinations.

[18] p: Hallucination Evaluation Paradigms. We distinguish two paradigms used throughout. Type I refers to open-ended caption hallucination, where hallucinated objects are counted post-hoc in free-form descriptions. Type II refers to closed-set discriminative queries answered as yes/no. CHAIR [ 27 ] (Type I) measures hallucinated object rates in COCO [ 17 ] captions via sentence-level (CHAIR-s) and instance-level (CHAIR-i) metrics. POPE [ 16 ] (Type II) provides three difficulty splits (random, popular, and adversarial) with 1,000 samples each.

[19] h2: 3 Methodology

[20] figure: (a) Two-pass SCR pipeline - Pass 1 : (1) extract attention, (2) select top- K K sources, (3) map 8-connected neighbors; Pass 2 : (4) redistribute credit in early layers (model-dependent; see Section 4 ), (5) generate corrected output. (b) 8-connected neighborhood. Source patch (red) redistributes activation to 8 neighbors (blue): 𝐡 n ← 𝐡 n + ( λ − 1 ) ​ 𝐡 s \mathbf{h}_{n}\leftarrow\mathbf{h}_{n}+(\lambda{-}1)\mathbf{h}_{s} ; source is scaled by 1 / λ 1/\lambda . Figure 1 : SCR methodology overview. (a) Full two-pass inference pipeline. (b) Spatial credit redistribution via 8-connected neighborhood structure.

[21] p: Figure 1(a) illustrates the full pipeline. SCR is an inference-time intervention that operates during the model’s forward pass, making it applicable to any existing VLM without retraining. It operates in two passes: in the first pass , a diagnostic forward pass captures attention maps, identifies the top- K K high-attention patches, and maps their 8-connected spatial neighbors; in the second pass , credit is redistributed from source patches to those neighbors during forward propagation through the early layers (0-15 for Chameleon-7B and Qwen, 0-20 for Chameleon-30B, 0-11 for LLaVA).

[22] h3: 3.1 Patch Selection and Neighbor Mapping

[23] p: Attention Map Computation. All three architectures use unified causal self-attention over an interleaved sequence of image and text tokens; none employs a separate cross-attention module. For Chameleon, image tokens are discrete VQ-VAE codebook entries; for LLaVA and Qwen, they are projected patch embeddings. In all cases, we locate the N v N_{v} image token positions in the input sequence, where N v = H img × W img / P 2 N_{v}=H_{\text{img}}\times W_{\text{img}}/P^{2} for patch size P P , and extract self-attention weights from text query positions to those visual positions. Weights are averaged across all heads and layers 8-16 to obtain the mean spatial attention map A ∈ ℝ N v A\in\mathbb{R}^{N_{v}} . For Qwen2-VL, which supports variable-resolution inputs, N v N_{v} is computed dynamically from the image dimensions.

[24] p: Top- K K Selection and Neighbor Mapping. Ablations (Appendix E) identify K = 32 K=32 as the optimal number of source patches; border rows and columns are excluded to prevent attention-sink artifacts. To avoid redistribution interference, sources are processed in descending attention order: a patch cannot act as both source and neighbor, and conflicts among overlapping source-neighbor pairs are resolved by priority, with higher-attention sources claiming neighbors first.

[25] h3: 3.2 Intervention Mechanism

[26] p: Injection point relative to LayerNorm. All three architectures (Chameleon, LLaVA-1.5, Qwen/Qwen2-VL) use Pre-LayerNorm (Pre-RMSNorm) transformer blocks [ 35 ] . Each block l l processes the residual stream 𝐱 \mathbf{x} via:

[27] table: 𝐱 ← 𝐱 + Attn ⁡ ( LN 1 ​ ( 𝐱 ) ) , 𝐱 ← 𝐱 + FFN ⁡ ( LN 2 ​ ( 𝐱 ) ) . \mathbf{x}\;\leftarrow\;\mathbf{x}+\mathrm{Attn}\!\bigl(\mathrm{LN}_{1}(\mathbf{x})\bigr),\qquad\mathbf{x}\;\leftarrow\;\mathbf{x}+\mathrm{FFN}\!\bigl(\mathrm{LN}_{2}(\mathbf{x})\bigr).

[28] p: SCR hooks are placed on the residual stream immediately after the second residual addition of block l l - equivalently, before block l + 1 l{+}1 ’s LN 1 \mathrm{LN}_{1} . Because the residual stream is never renormalized at this position, the ℓ 2 \ell_{2} -norm amplification introduced by the redistribution persists across layers: each downstream Pre-LN sub-layer normalizes its own input internally, but the amplified residual propagates intact through the additive skip connections. This cumulative propagation explains the 48-56% aggregate norm increase measured at the output of the final intervention layer (see Appendix C, Table C2). The norm amplification is therefore a property of the residual stream , not of the post-LN activations seen by individual attention or FFN sub-layers.

[29] p: The intervention redistributes activation from source patch h i s h_{i_{s}} to its 8-connected spatial neighbors (see Figure 1(b) ), while the source itself is scaled down using a fixed factor λ = 1.10 \lambda=1.10 .

[30] table: 𝐡 i n ← 𝐡 i n + ( λ − 1 ) ⋅ 𝐡 i s , 𝐡 i s ← 1 λ ⋅ 𝐡 i s \mathbf{h}_{i_{n}}\leftarrow\mathbf{h}_{i_{n}}+(\lambda-1)\cdot\mathbf{h}_{i_{s}},\quad\mathbf{h}_{i_{s}}\leftarrow\frac{1}{\lambda}\cdot\mathbf{h}_{i_{s}} (1)

[31] p: The total ℓ 2 \ell_{2} norm of the hidden states consequently increases by a factor of approximately 1.51 (51% amplification). This is by design: SCR adds scaled copies of source activations to neighbors while retaining 91% of the source ( 1 / λ ≈ 0.91 1/\lambda\approx 0.91 ), amplifying spatial context rather than merely redistributing it. Because hallucination-prone samples exhibit suppressed early-layer activations, this amplification improves visual grounding with minimal impact on caption fluency (CIDEr decreases by less than 0.8%). The modification is applied to layers 0-15 for Chameleon-7B and Qwen, layers 0-20 for Chameleon-30B, and layers 0-11 for LLaVA; later layers are left unchanged to avoid interfering with language generation.

[32] h3: 3.3 Theoretical Foundation

[33] p: Empirical Finding (EF1)-Norm-Credit Proxy. We define visual credit c i c_{i} at spatial location i i as c i = 𝔼 𝐡 i ​ [ ∂ log ⁡ P ⁡ ( y | ℐ , 𝒬 ) ∂ 𝐡 i ] ⋅ ‖ 𝐡 i ‖ 2 c_{i}=\mathbb{E}_{\mathbf{h}_{i}}\left[\frac{\partial\log P(y|\mathcal{I},\mathcal{Q})}{\partial\mathbf{h}_{i}}\right]\cdot\|\mathbf{h}_{i}\|_{2} , where 𝐡 i \mathbf{h}_{i} is the hidden state. We empirically observe that in early transformer layers ‖ 𝐡 i ‖ 2 \|\mathbf{h}_{i}\|_{2} is a useful approximation to c i c_{i} (Pearson r = 0.72 r=0.72 averaged across all six models; see Appendix C for full per-model validation). This is a correlational finding that motivates using norm as a practical proxy; it does not constitute a formal proof of equivalence.

[34] p: Credit Concentration Entropy. We quantify spatial credit concentration via the normalized entropy of credit weights. Lower values indicate credit concentrated on few spatial locations; higher values reflect a more distributed allocation:

[35] table: H credit = − ∑ i = 1 n c i ∑ j c j log c i ∑ j c j . H_{\text{credit}}=-\sum_{i=1}^{n}\frac{c_{i}}{\sum_{j}c_{j}}\log\frac{c_{i}}{\sum_{j}c_{j}}. (2)

[36] p: Hallucination-Entropy Relationship. Heuristically, low credit entropy H credit < H min H_{\text{credit}}<H_{\min} limits I ⁡ ( Y ; 𝐇 S ¯ | 𝐇 S ) I(Y;\mathbf{H}_{\bar{S}}|\mathbf{H}_{S}) , creating conditions favorable to hallucination. Empirically, we observe a negative correlation ( r = − 0.65 r=-0.65 , p < 0.001 p<0.001 ) between credit entropy and hallucination rate across all models; a full report is in Section 5 ( Tab. 6 ).

[37] p: Design Rationale-8-Connected Neighborhoods. Natural images exhibit spatial autocorrelation that decays with patch distance [ 5 , 28 ] . An 8-connected neighborhood captures diagonal patch correlations at distance 2 \sqrt{2} ( ρ ⁡ ( 2 ) ≈ 0.62 \rho(\sqrt{2})\approx 0.62 , estimated from autocorrelation decay on POPE images; see Appendix A) that a 4-connected scheme ignores, at roughly twice the cost. Larger-radius neighborhoods introduce excessive smoothing with diminishing hallucination benefit, as confirmed in the ablation ( Figure 4(a) ): 8-connected achieves HR = 13.5% versus 16.5% for 4-connected and 18.2% for radius-2, confirming 8-connected as the best configuration.

[38] p: Proposition (Peak-Preserving Expansion). For λ ∈ [ 1.05 , 1.15 ] \lambda\in[1.05,1.15] , SCR provably approximates (see Appendix A for the full proof):

[39] table: max 𝐇 ′ ⁡ λ 1 ​ H credit ​ ( 𝐇 ′ ) − λ 2 ​ ‖ 𝐇 ′ − 𝐇 ‖ F 2 s.t. max i ⁡ ‖ 𝐡 i ′ ‖ ≥ τ ​ max j ​ ‖ 𝐡 j ‖ , \max_{\mathbf{H}^{\prime}}\,\lambda_{1}H_{\text{credit}}(\mathbf{H}^{\prime})-\lambda_{2}\|\mathbf{H}^{\prime}-\mathbf{H}\|_{F}^{2}\quad\text{s.t.}\quad\max_{i}\|\mathbf{h}^{\prime}_{i}\|\geq\tau\max_{j}\|\mathbf{h}_{j}\|,

[40] p: with τ = 1 / λ ≈ 0.91 \tau=1/\lambda\approx 0.91 .

[41] p: All formal proofs and derivations are provided in Appendix A.

[42] h2: 4 Experimental Setup

[43] p: Selected Models. Chameleon-7B/30B [ 31 ] (layers 0-15 / 0-20); LLaVA-1.5-7B/13B [ 20 ] (layers 0-11 for both; validated by the layer-selection ablation in Appendix E, which shows diminishing returns beyond layer 11 regardless of depth); and Qwen-VL/Qwen2-VL-7B [ 2 , 32 ] (layers 0-15). All layer ranges were selected on a held-out validation set of 200 COCO train2014 images, fully disjoint from the POPE and CHAIR evaluation sets; no evaluation data was used in hyperparameter selection.

[44] p: Computational Setup. All experiments were run on a workstation with an AMD Ryzen Threadripper PRO CPU and a single NVIDIA A100 GPU (fp16 precision).

[45] p: Benchmarks. POPE [ 16 ] in 3 splits (1,000 samples each) and COCO [ 17 ] (3,000-image val2014 subset) for CHAIR and CIDEr evaluation.

[46] p: Baselines. OPERA [ 12 ] (attention penalty, + + 267 ms), VCD [ 14 ] (contrastive decoding, + + 153 ms), OA-VCD [ 10 ] (adversarial contrastive decoding, + + 72 ms), and training-free representation methods SID [ 13 ] , VLI [ 22 ] , and CRoPS [ 1 ] . We also include Uniform-Smooth as a controlled ablation baseline: it applies the same redistribution operation as SCR ( λ = 1.10 \lambda=1.10 , K = 32 K=32 , same layer range) but selects source patches uniformly at random rather than by attention, isolating the contribution of attention-guided source identification.

[47] p: Metrics. Hallucination Rate HR = = FP/(FP + + TN) (false positive rate for absent objects [ 16 ] ), Accuracy, CIDEr, CHAIR-s, CHAIR-i, and Attention Entropy.

[48] h2: 5 Results

[49] h3: 5.1 Multi-Model and Benchmark Evaluation

[50] p: Tabs. 1 and 2 report POPE-Adversarial and CIDEr results for all six model configurations. Figure 2 summarizes the hallucination-rate trends visually. SCR reduces hallucination rates (HR) while maintaining generation quality across all tested configurations.

[51] figure: Table 1: POPE-Adversarial HR (% ↓ \downarrow ), Accuracy (% ↑ \uparrow ), and CIDEr ( ↑ \uparrow ) for small-scale models. Mean ± \pm std over 3 runs. Green = best HR per group; blue = second best. Δ \Delta HR is relative to each group’s Vanilla baseline. OA-VCD [ 10 ] is an efficient adversarial variant of VCD ( + + 72 ms vs. + + 153 ms) that improves over VCD on both HR and CIDEr but is Pareto-dominated by SCR. Uniform-Smooth is the attention-unguided ablation of SCR (same λ \lambda , K K , layers; random source selection): its consistently higher HR (2.6-3.4 pp worse than SCR) demonstrates that attention-guided source identification-not spatial smoothing per se-is the operative mechanism. Model Method HR ↓ \downarrow Acc ↑ \uparrow CIDEr ↑ \uparrow Δ \Delta HR ↓ \downarrow Cham-7B Vanilla 19.5 ± \pm .8 80.2 ± \pm .7 102.3 ± \pm 1.4 - OPERA 16.4 ± \pm 1.1 83.1 ± \pm .8 100.1 ± \pm 1.5 − - 3.1 VCD 15.3 ± \pm 1.2 84.5 ± \pm .9 97.8 ± \pm 1.8 − - 4.2 OA-VCD 14.9 ± \pm 1.0 84.8 ± \pm .8 99.6 ± \pm 1.4 − - 4.6 VLI 15.6 ± \pm .9 84.0 ± \pm .7 100.4 ± \pm 1.2 − - 3.9 CRoPS 14.7 ± \pm 1.0 85.1 ± \pm .8 98.6 ± \pm 1.4 − - 4.8 SID 15.1 ± \pm .8 84.6 ± \pm .6 99.2 ± \pm 1.1 − - 4.4 Uniform-Smooth 16.1 ± \pm .9 83.7 ± \pm .7 99.4 ± \pm 1.3 − - 3.4 SCR 13.5 ± \pm .7 86.2 ± \pm .5 101.7 ± \pm .9 − 6.0 \mathbf{-6.0} LLaVA-1.5-7B Vanilla 18.8 ± \pm .7 80.9 ± \pm .6 108.5 ± \pm 1.3 - OPERA 15.9 ± \pm 1.0 83.7 ± \pm .7 106.4 ± \pm 1.2 − - 2.9 VCD 14.6 ± \pm 1.1 85.0 ± \pm .8 104.2 ± \pm 1.6 − - 4.2 OA-VCD 14.3 ± \pm .9 85.4 ± \pm .7 105.7 ± \pm 1.2 − - 4.5 VLI 15.3 ± \pm .8 84.4 ± \pm .6 106.6 ± \pm 1.0 − - 3.5 CRoPS 14.2 ± \pm 1.0 85.5 ± \pm .7 104.9 ± \pm 1.3 − - 4.6 SID 14.7 ± \pm .7 84.9 ± \pm .5 105.6 ± \pm 1.1 − - 4.1 Uniform-Smooth 15.8 ± \pm .8 83.9 ± \pm .7 105.2 ± \pm 1.2 − - 3.0 SCR 13.1 ± \pm .6 86.5 ± \pm .5 107.8 ± \pm .8 − 5.7 \mathbf{-5.7} Qwen-VL Vanilla 18.5 ± \pm .6 81.2 ± \pm .6 115.2 ± \pm 1.0 - OPERA 15.6 ± \pm .9 84.0 ± \pm .6 113.4 ± \pm 1.0 − - 2.9 VCD 14.4 ± \pm 1.0 85.2 ± \pm .7 111.2 ± \pm 1.4 − - 4.1 OA-VCD 14.0 ± \pm .9 85.7 ± \pm .6 112.5 ± \pm 1.1 − - 4.5 VLI 14.8 ± \pm .7 84.9 ± \pm .5 113.2 ± \pm .9 − - 3.7 CRoPS 13.9 ± \pm .9 85.8 ± \pm .6 111.8 ± \pm 1.2 − - 4.6 SID 14.3 ± \pm .6 85.4 ± \pm .5 112.5 ± \pm .8 − - 4.2 Uniform-Smooth 15.3 ± \pm .8 84.4 ± \pm .6 111.7 ± \pm 1.0 − - 3.2 SCR 12.9 ± \pm .5 86.8 ± \pm .4 114.6 ± \pm .7 − 5.6 \mathbf{-5.6} Qwen2-VL-7B Vanilla 17.0 ± \pm .5 82.7 ± \pm .5 118.5 ± \pm .9 - OPERA 14.6 ± \pm .8 85.1 ± \pm .5 116.7 ± \pm .9 − - 2.4 VCD 13.1 ± \pm .9 86.5 ± \pm .7 114.6 ± \pm 1.3 − - 3.9 OA-VCD 12.7 ± \pm .8 87.0 ± \pm .6 115.4 ± \pm 1.0 − - 4.3 VLI 13.7 ± \pm .6 86.0 ± \pm .5 116.3 ± \pm .8 − - 3.3 CRoPS 12.6 ± \pm .8 87.1 ± \pm .6 115.1 ± \pm 1.1 − - 4.4 SID 13.2 ± \pm .5 86.5 ± \pm .4 116.0 ± \pm .7 − - 3.8 Uniform-Smooth 14.0 ± \pm .7 85.8 ± \pm .5 115.1 ± \pm .9 − - 3.0 SCR 11.4 ± \pm .5 88.2 ± \pm .4 117.9 ± \pm .6 − 5.6 \mathbf{-5.6}

[52] figure: Table 2: POPE-Adversarial HR (% ↓ \downarrow ), Accuracy (% ↑ \uparrow ), and CIDEr ( ↑ \uparrow ) for large-scale models. Mean ± \pm std over 3 runs. Color coding as in Tab. 1 . On LLaVA-13B, CRoPS achieves the lowest HR but degrades CIDEr by 3.6 pp (from 114.8 to 111.2); OA-VCD achieves 13.0 pp HR at only − - 2.6 pp CIDEr cost but still trails SCR (12.8 pp HR, − - 0.7 pp CIDEr, + + 54 ms vs. OA-VCD’s + + 72 ms). SCR achieves the best Acc and CIDEr across both large models; maximum CIDEr cost is 0.8 pp (Cham-30B). Model Method HR ↓ \downarrow Acc ↑ \uparrow CIDEr ↑ \uparrow Δ \Delta HR ↓ \downarrow Cham-30B Vanilla 18.2 ± \pm .7 81.5 ± \pm .6 108.2 ± \pm 1.2 - OPERA 15.4 ± \pm 1.0 84.2 ± \pm .6 106.8 ± \pm 1.1 − - 2.8 VCD 14.3 ± \pm 1.1 85.4 ± \pm .8 103.8 ± \pm 1.7 − - 3.9 OA-VCD 13.8 ± \pm .9 86.0 ± \pm .6 105.2 ± \pm 1.1 − - 4.4 VLI 14.9 ± \pm .8 84.8 ± \pm .6 106.2 ± \pm 1.0 − - 3.3 CRoPS 13.6 ± \pm .9 86.1 ± \pm .7 104.4 ± \pm 1.3 − - 4.6 SID 14.1 ± \pm .7 85.6 ± \pm .5 105.1 ± \pm .9 − - 4.1 Uniform-Smooth 15.6 ± \pm .8 84.1 ± \pm .6 105.3 ± \pm 1.1 − - 2.6 SCR 12.6 ± \pm .6 87.1 ± \pm .4 107.4 ± \pm .8 − 5.6 \mathbf{-5.6} LLaVA-1.5-13B Vanilla 17.5 ± \pm .6 82.2 ± \pm .5 114.8 ± \pm 1.1 - OPERA 14.9 ± \pm .9 84.8 ± \pm .6 112.8 ± \pm 1.0 − - 2.6 VCD 13.4 ± \pm 1.0 86.2 ± \pm .7 110.6 ± \pm 1.5 − - 4.1 OA-VCD 13.0 ± \pm .8 86.7 ± \pm .6 112.2 ± \pm .9 − - 4.5 VLI 14.1 ± \pm .7 85.6 ± \pm .5 112.4 ± \pm .9 − - 3.4 CRoPS 12.6 ± \pm .9 87.0 ± \pm .6 111.2 ± \pm 1.2 − - 4.9 SID 13.3 ± \pm .6 86.4 ± \pm .5 111.9 ± \pm .8 − - 4.2 Uniform-Smooth 14.9 ± \pm .7 84.8 ± \pm .6 112.5 ± \pm 1.0 − - 2.6 SCR 12.8 ± \pm .5 87.4 ± \pm .4 114.1 ± \pm .7 − 4.7 \mathbf{-4.7}

[53] p: Observations. Tabs. 1 and 2 reveal six key patterns: (1) On LLaVA-1.5-13B, CRoPS achieves a marginally lower HR (12.6 vs. 12.8 pp), but at a higher CIDEr cost ( − - 3.6 pp vs. − - 0.7 pp). (2) OA-VCD improves over VCD on both HR ( ≈ {\approx} 0.3-0.5 pp) and CIDEr ( ≈ {\approx} 0.8-1.8 pp uplift), confirming that adversarial, object-targeted perturbations are more effective than isotropic noise; nevertheless, SCR Pareto-dominates OA-VCD on all three axes (HR, CIDEr, and latency) across all six model configurations. (3) SCR preserves CIDEr within 0.8 pp of baseline, while VCD and CRoPS degrade it by 3.4-4.5 pp, and OA-VCD by 2.6-3.1 pp. (4) The method generalizes across early-fusion (Chameleon) and connector-based (LLaVA, Qwen) architectures. (5) All SCR gains over all baselines are statistically significant ( p < 0.001 p<0.001 , paired t t -test). (6) The Uniform-Smooth ablation confirms that attention guidance is essential : unguided random redistribution reduces HR by only 2.6-3.4 pp versus SCR’s 4.7-6.0 pp, a ≈ {\approx} 1.7 × \times gap that points to credit-guided source selection, not spatial smoothing, as the key driver. On latency, SCR is 3 3 - 6 × 6{\times} faster than OPERA and VCD ( + + 43-56 ms vs. + + 153-267 ms) and 1.3 1.3 - 1.7 × 1.7{\times} faster than OA-VCD, while achieving strictly better hallucination rates and CIDEr than all three.

[54] figure: Figure 2 : SCR performance across six VLM configurations (Cham-7B/30B, LLaVA-1.5-7B/13B, Qwen-VL, Qwen2-VL-7B) on POPE-Adversarial. SCR reduces hallucination rate by ≈ {\approx} 4.7-6.0 pp across both early-fusion (Chameleon) and connector-based (LLaVA, Qwen) models across all tested architectures.

[55] h3: 5.2 POPE Split Analysis

[56] p: As shown in Tab. 3 , SCR generalizes across all POPE difficulty levels and model architectures.

[57] figure: Table 3: POPE split analysis (HR%) across model architectures. Each cell shows Vanilla → \to SCR. The adversarial-split column matches the HR values in Tabs. 1 and 2 , where full comparisons against all five baselines (OPERA, VCD, VLI, CRoPS, SID) are reported. SCR achieves consistent reductions across all splits and architectures; Random and Popular splits follow analogous relative trends. Model Random Popular Adversarial Chameleon-7B 12.5 → \to 8.8 15.8 → \to 10.9 19.5 → \to 13.5 Chameleon-30B 11.2 → \to 7.5 14.5 → \to 9.4 18.2 → \to 12.6 LLaVA-1.5-7B 11.8 → \to 8.2 15.0 → \to 10.6 18.8 → \to 13.1 LLaVA-1.5-13B 10.5 → \to 7.6 13.8 → \to 9.8 17.5 → \to 12.8 Qwen-VL 11.5 → \to 7.9 14.8 → \to 10.3 18.5 → \to 12.9 Qwen2-VL-7B 10.2 → \to 7.1 13.5 → \to 9.0 17.0 → \to 11.4

[58] h3: 5.3 Latency and Optimization

[59] p: SCR incurs an additional inference cost due to the diagnostic forward pass. It adds roughly +43-46 ms for smaller-scale models (Cham-7B, LLaVA-7B, Qwen variants) and +54-56 ms for larger-scale models (Cham-30B, LLaVA-13B), which is below OPERA (+267 ms) and VCD (+153 ms). SCR does not increase memory usage, since all modifications are applied through in-place hooks on hidden states. All latency numbers correspond to end-to-end wall-clock time. To reduce this overhead further, we evaluate an optional One-Pass SCR variant.

[60] p: Note on scope: One-Pass SCR is not training-free. It requires training a lightweight 2-layer MLP predictor (hidden dim 256, ≈ {\approx} 120K parameters) on 5,000 attention maps from COCO train2014, which is fully disjoint from all evaluation sets. The primary contribution of this paper-two-pass SCR-requires no training of any kind . One-Pass SCR is offered solely as a latency-sensitive deployment option.

[61] p: This predictor estimates source patch locations directly from layer-0 hidden states, eliminating the diagnostic forward pass. Results are reported in Tab. 4 .

[62] figure: Table 4: One-pass vs. two-pass SCR: accuracy-latency trade-off on POPE-Adversarial across all six model configurations. The one-pass variant uses a lightweight MLP predictor, reducing overhead from ∼ \sim 43-56 ms to ∼ \sim 6-11 ms at a cost of ∼ \sim 1.3 pp HR. Model Variant HR ↓ \downarrow Acc ↑ \uparrow Latency Chameleon-7B Two-Pass SCR 13.5% 86.2% +45ms One-Pass SCR 14.9% 84.8% +7ms Chameleon-30B Two-Pass SCR 12.6% 87.1% +56ms One-Pass SCR 13.9% 85.8% +11ms LLaVA-1.5-7B Two-Pass SCR 13.1% 86.5% +44ms One-Pass SCR 14.4% 85.3% +6ms LLaVA-1.5-13B Two-Pass SCR 12.8% 87.4% +54ms One-Pass SCR 14.0% 85.7% +9ms Qwen-VL Two-Pass SCR 12.9% 86.8% +46ms One-Pass SCR 14.2% 85.4% +7ms Qwen2-VL-7B Two-Pass SCR 11.4% 88.2% +43ms One-Pass SCR 12.7% 86.9% +6ms

[63] h3: 5.4 Caption-Level Hallucination: CHAIR Results

[64] p: Tab. 5 shows the CHAIR metrics for the six models on 3,000 COCO val2014 captions. POPE gains (Type II) transfer to open-ended caption hallucinations (Type I).

[65] figure: Table 5: CHAIR metrics on COCO captions (3,000 images), comparing vanilla baseline against SCR. CHAIR evaluates open-ended caption generation (Type I). Average reductions: CHAIR-s 45 % 45\% , CHAIR-i 48 % 48\% relative. Full multi-baseline comparisons (OPERA, VCD, VLI, CRoPS, SID) are in Appendix B. Model CHAIR-s Base CHAIR-s SCR CHAIR-i Base CHAIR-i SCR Chameleon-7B 12.3% 7.1% 8.5% 4.5% Chameleon-30B 10.8% 5.8% 7.2% 3.6% LLaVA-1.5-7B 10.2% 5.9% 7.1% 4.0% LLaVA-1.5-13B 9.1% 4.7% 6.3% 3.1% Qwen-VL 8.9% 5.2% 6.1% 3.4% Qwen2-VL-7B 8.2% 4.0% 5.7% 2.7% Average 9.9% 5.5% 6.8% 3.6%

[66] h3: 5.5 Theoretical Prediction Validation

[67] p: With SCR, we validate four empirical predictions across all six models utilizing the POPE-Adversarial split. These predictions are labeled P1 - P4 and are distinct from the three formal Propositions in Section 3 : P1 and P2 are observational predictions derived from the hallucination-entropy relationship (Section 3 ); P3 is the empirical test of Proposition 2 (spatial autocorrelation); P4 is the empirical test of Proposition 3 (inverted-U λ \lambda relationship). Proposition 1 (norm-credit proxy) is validated separately in Appendix C.

[68] p: P1: Entropy-Hallucination Correlation. Across samples and models, lower spatial credit entropy is associated with higher hallucination rates. Tab. 6 shows negative correlations across architectures.

[69] figure: Table 6: Entropy-hallucination correlation (Pearson r r ) across models. Model Pearson r r p p -value Chameleon-7B − 0.68 -0.68 2.4 × 10 − 5 2.4{\times}10^{-5} Chameleon-30B − 0.63 -0.63 4.1 × 10 − 4 4.1{\times}10^{-4} LLaVA-1.5-7B − 0.72 -0.72 8.7 × 10 − 6 8.7{\times}10^{-6} LLaVA-1.5-13B − 0.69 -0.69 1.8 × 10 − 5 1.8{\times}10^{-5} Qwen-VL − 0.61 -0.61 6.3 × 10 − 4 6.3{\times}10^{-4} Qwen2-VL-7B − 0.58 -0.58 1.2 × 10 − 3 1.2{\times}10^{-3} Average − 0.65 -0.65 -

[70] p: Samples with H < 4.0 H<4.0 show elevated HR across all models (mean 24.5%), while those with H ≥ 4.0 H\geq 4.0 exhibit significantly lower rates (mean 14.0%).

[71] p: P2: Stratified Gains by Baseline Entropy. As shown in Figure 3 , inputs with highly concentrated credit ( H < 3.5 H<3.5 ) see the largest HR reductions, averaging 9.8pp across all six models. For inputs with already-distributed credit ( H > 4.5 H>4.5 ), reductions are smaller, averaging 2.4pp. This validates our theoretical prediction that SCR provides the greatest benefit when credit entropy is lowest.

[72] figure: Figure 3 : Entropy-stratified HR reduction across all six model configurations. SCR provides the greatest benefit for low-entropy inputs ( H < 3.5 H<3.5 , avg. 9.8 pp reduction) where credit is most collapsed, and diminishing gains for already-distributed credit ( H > 4.5 H>4.5 , avg. 2.4 pp), validating our theoretical framework.

[73] p: P3 and P4. Predictions on spatial autocorrelation dependence and the inverted-U λ \lambda relationship are confirmed across all models; full results are in Appendix D.

[74] h2: 6 Ablations and Limitations

[75] h3: 6.1 Ablation Study Summary

[76] p: (a) Attention Guidance. Replacing attention-guided source selection with uniform random selection (Uniform-Smooth, same λ \lambda / K K /layers) reduces HR gains from 4.7-6.0 pp to 2.6-3.4 pp across all six model configurations (Tables 1 - 2 ). This ≈ {\approx} 1.7 × \times gap isolates the contribution of credit-guided source identification: spatial amplification alone helps, but directing it to the highest-credit patches is essential for the full benefit.

[77] p: (b) Topology. The 8-connected scheme (HR = 13.5%) outperforms 4-connected (16.5%) and radius-2 (18.2%) in Figure 4(a) , confirming diagonal neighbors at 2 \sqrt{2} encode meaningful spatial information.

[78] p: (c) Signal vs. Noise. In Figure 4(b) , Gaussian noise raises entropy to 5.2 nats yet degrades HR to 25.5%, demonstrating that gains stem from semantic structure rather than artificially higher entropy values alone.

[79] p: (d) Hyperparameters. From the head-selectivity ablation ( Figure 4(c) ), adaptive selection intervenes on only 20% of heads (a 5 × \times reduction) while retaining 95% of the benefit; optimal settings are λ = 1.10 \lambda=1.10 , K = 32 K=32 sources, layers 0-15. Full ablations are in Appendix E.

[80] figure: (a) Neighbor topology: 8-connected (HR 13.5%) outperforms 4-connected (16.5%) and radius-2 (18.2%), validating diagonal inclusion. (b) Signal vs. noise: Gaussian noise raises entropy to 5.2 nats yet degrades HR to 25.5%, confirming gains require semantic structure. (c) Head selectivity: intervening on only 20% of heads (5 × \times reduction) retains 95% of the benefit ( λ = 1.10 \lambda=1.10 , K = 32 K=32 , layers 0-15). Figure 4 : Ablation studies. (b) Neighbor topology comparison. (c) Semantic structure vs. entropy control. (d) Head-selectivity and computational cost trade-off. See ablation (a) in text for the Uniform-Smooth attention-guidance comparison (Tables 1 - 2 ).

[81] h3: 6.2 Limitations

[82] p: Scope. Our first empirical finding (EF1) characterizes the norm-credit proxy as a correlational observation ( r = 0.72 r=0.72 ) rather than a proven equivalence, and the entropy-hallucination relationship as an associative rather than causal claim. While neither probes deeper causal mechanisms, together they support the SCR design. The 51% norm amplification was determined empirically based on its impact on calibration behavior. SCR addresses spatial grounding; relational reasoning is outside the present scope.

[83] p: Failure modes. We analyze SCR’s remaining errors and identify three dominant patterns: (1) very small objects ( < < 2% image area) account for 26% of residual errors, as redistribution dilutes their already-weak signals; (2) edge-located objects account for 56% of errors, since boundary exclusion can remove valid high-attention regions; (3) ambiguous neighbor pairs account for 18% of errors, where amplifying visually similar neighbors triggers false positives.

[84] p: Trade-offs. SCR changes 15% of all predictions relative to the vanilla baseline; of these changes, approximately 70% are corrections (wrong → \to right) and 30% are new errors (right → \to wrong), yielding a net accuracy gain of ≈ 6 {\approx}6 pp ( 0.15 × ( 0.70 − 0.30 ) = 0.06 0.15\times(0.70-0.30)=0.06 ). Robustness to adversarial visual inputs is not evaluated and is left as future work.

[85] h2: 7 Conclusion

[86] p: SCR (Spatial Credit Redistribution) is a training-free intervention applied to early transformer layers that redistributes hidden-state activation from high-attention patches to their spatial neighbors, reducing over-concentration of evidence that precedes object hallucination. Evaluated on POPE and CHAIR across six model configurations (Chameleon 7B/30B, LLaVA 7B/13B, Qwen-VL, Qwen2-VL-7B), hallucination rates decrease while caption quality remains within baseline variance. A lightweight spatial intervention recovers much of the benefit at lower cost: SCR is 3 3 - 6 × 6{\times} faster than OPERA and VCD and 1.3 1.3 - 1.7 × 1.7{\times} faster than OA-VCD, while Pareto-dominating all three on both hallucination rate and CIDEr, making it practical for latency-sensitive deployment.

[87] p: Beyond the empirical results, we examine the behavior of spatial credit through an information-theoretic lens and observe a systematic connection between low spatial entropy and hallucination frequency. Since SCR requires no retraining, it applies directly to any existing model. Extension to video-VLMs, combining with RLHF, learned spatial patterns, and application to audio-visual and medical domains are directions for future work. Evaluation on broader multi-task hallucination suites such as HallusionBench [ 9 ] and MME [ 6 ] -which probe relational and compositional reasoning beyond object presence-would further characterize SCR’s scope and boundary conditions, and is ongoing.

[88] p: Supplementary material includes: formal proofs and derivations (App. A), extended CHAIR comparisons across all baselines (App. B), per-model norm-credit correlation (App. C), extended theoretical validation of P3 and P4 (App. D), and detailed hyperparameter ablations (App. E).

[89] h2: References

[90] h2: Instructions for reporting errors

[91] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[92] p: Tip: You can select the relevant text first, to include it in your report.

[93] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[94] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
