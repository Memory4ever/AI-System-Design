[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Modality Collapse as Mismatched Decoding: Information-Theoretic Limits of Multimodal LLMs

[3] h6: Abstract

[4] p: Multimodal LLMs can process speech and images, but they cannot hear a speaker’s voice or see an object’s texture. We show this is not a failure of encoding: speaker identity, emotion, and visual attributes survive through every LLM layer (3–55 × \times above chance in linear probes), yet removing 64–71% of modality-specific variance improves decoder loss. The decoder has no learned use for these directions; their presence is noise.

[5] p: We formalize this as a mismatched decoder problem: a decoder trained on text can only extract information along text-aligned directions. Accessible information is bounded by the Generalized Mutual Information (GMI), with degradation scaling with distributional distance and decoder sensitivity. The bound is a property of the decoder’s scoring rule, not of any particular architecture; it applies whether non-text inputs arrive through a learned projection, a discrete codebook, or no explicit adapter at all. We validate this across five models spanning speech and vision. A controlled experiment (two Prismatic VLMs differing only in encoder text-alignment) confirms the bottleneck is the decoder’s scoring rule, not the encoder or projection. A LoRA intervention demonstrates the fix: training with an emotion objective improves emotion accessibility ( + + 7.5%) without affecting other attributes, confirming that the training objective determines what becomes accessible.

[6] p: Code: https://github.com/jb1999/modality_collapse_paper

[7] h2: 1 Introduction

[8] p: Multimodal LLMs follow a common recipe: an encoder processes the non-text input (speech, image), a learned projection maps it into the LLM’s embedding space, and the LLM generates text ( Liu et al., 2023 ; Dai et al., 2023 ; Fixie AI, 2024 ; Chu et al., 2024 ; Karamcheti et al., 2024 ) . By standard benchmarks these systems appear to work well: speech models transcribe accurately, vision models caption faithfully. But this success is a mirage. These systems excel at tasks requiring only text-correlated information (the words spoken, the objects visible) while silently discarding everything else. A speech model that transcribes perfectly may have no access to who is speaking or how they feel; a vision model that names every object may be blind to spatial layout or texture. This paper shows that the loss is structural and predictable.

[9] p: The obvious explanation, that the projection fails to encode non-text information, is wrong. Linear probes show that speaker identity, emotion, and visual attributes survive through every LLM layer, remaining 3–55 × \times above chance at the final layer (e.g., speaker identity .556 .556 vs. .025 .025 chance in Ultravox; object category .792 .792 vs. .014 .014 chance in Prismatic-DINOv2). The information is there. The LLM does not use it.

[10] p: Worse, modality-specific information degrades decoding. Removing 64% of the variance in modality-specific directions improves cross-entropy loss; the decoder works better with less information. Lexical probe accuracy nearly doubles from the adapter to the final LLM layer (the decoder amplifies what it knows how to use), while speaker probe accuracy drops by up to 39% over the same path. The mechanism is not active suppression: the decoder simply has no learned response to non-text directions. It is indifferent to them, but that indifference has consequences, because the decoder treats unfamiliar variance as noise. Where the collapse manifests depends on the encoder: non-aligned encoders (Whisper, DINOv2) pass rich representations the decoder is blind to; text-aligned encoders (CLIP, SigLIP) discard non-textual information before it reaches the decoder. Either way, the information is lost (Appendix Table 6 ).

[11] p: Our thesis. We formalize this as a mismatched decoder problem ( Merhav et al., 1994 ; Scarlett et al., 2020 ) . The LLM’s scoring rule was learned from text, so it can only extract information along text-aligned directions. Accessible information is bounded by the Generalized Mutual Information (GMI), not the standard mutual information. We call the difference the information accessibility gap . The gap is not about architecture; it is about the scoring rule. No explicit adapter module is required: any system where a text-trained decoder processes non-text representations faces the same constraint, whether the representations arrive through a learned projection, a discrete codebook, or the LLM’s own layers. At inference, every trained model has fixed weights: the scoring rule is whatever the training procedure produced. A model trained predominantly on text has a text-shaped scoring rule regardless of whether the LLM was frozen or fine-tuned during training. What matters is the training objective, not which components were updated (§ 6.1 ).

[12] p: What determines the size of the gap? A linear probe simply measures whether the information it was trained to detect is present. The decoder is a different instrument entirely. It is a deep transformer trained on text, and it is highly sensitive to its input, responding to variance in every direction, including non-text directions (we confirm this empirically via gradient isotropy in § 5.5 ). But its response to non-text variance is unproductive: the decoder interprets unfamiliar structure as noise, and that noise disrupts its text processing. This is why removing modality-specific directions helps : not because the decoder ignores them, but because it responds to them in ways that degrade output. We formalize this: degradation scales with both the distributional distance between modal and text representations and the decoder’s sensitivity to that distance (Theorem 2 ), and the decoder’s sensitivity is up to 30 × 30\times that of a probe (Theorem 3 , § A.4 ). Text-aligned encoders reduce the distance (§ 5.3 ), but only by discarding non-textual information upstream. The collapse happens earlier, not less.

[13] p: Contributions. (1) We formalize modality collapse as mismatched decoding and prove that accessible information is bounded by the GMI, with degradation governed by distributional distance and decoder sensitivity (§ 4 ). (2) Across five models and two modalities, we demonstrate the information accessibility gap: non-text information survives through the LLM but degrades decoding because the decoder has no learned use for it (§ 5.2 , § 5.4 ). (3) A controlled experiment with Prismatic VLMs (same architecture, same LLM, only encoder text-alignment differs) isolates the scoring rule as the causal variable (§ 5.3 ). (4) A LoRA intervention confirms the prescription: training with an emotion objective teaches the decoder to respond to that dimension ( + + 7.5%), while a text-centric objective leaves it indifferent (§ 6.1 ).

[14] h2: 2 Related work

[15] p: Multimodal LLMs and the adapter paradigm. The strategy of projecting encoded features into an LLM’s embedding space has become standard for both vision ( Liu et al., 2023 ; Dai et al., 2023 ; Zhu et al., 2024 ; Karamcheti et al., 2024 ; Tong et al., 2024 ) and speech ( Fixie AI, 2024 ; Chu et al., 2024 ) . These systems achieve strong performance on text-centric benchmarks but struggle with tasks requiring modality-specific information, an observation that has been noted empirically but not explained theoretically.

[16] p: Modality gap. Liang et al. (2022) showed that CLIP embeddings of different modalities occupy distinct regions of the shared space, separated by a persistent “modality gap.” Huh et al. (2024) observed convergence of representations across modalities. Our work complements these geometric observations with an information-theoretic mechanism: the gap matters not because information is destroyed, but because the decoder cannot access information in unfamiliar directions.

[17] p: Mismatched decoding. The theory of mismatched decoders ( Merhav et al., 1994 ; Lapidoth, 1996 ; Scarlett et al., 2020 ) characterizes the information rate achievable when a decoder is designed for a different channel than the one actually used. We import this framework into the multimodal LLM setting: at inference, any LLM whose scoring rule was shaped by text-dominated training is a mismatched decoder for non-text inputs. The mismatch is determined by the training objective, not by which components were updated.

[18] p: Representation probing. Linear probes are a standard tool for measuring information content in neural representations ( Alain & Bengio, 2017 ; Conneau et al., 2018 ; Hewitt & Manning, 2019 ; Belinkov, 2022 ) . We use probes not to claim information is “encoded” in a representation, but to demonstrate the gap between information present (probe-recoverable) and information accessible (decoder-extractable).

[19] p: Rate-distortion in ML. Blau & Michaeli (2019) introduced the rate-distortion-perception tradeoff, showing that perceptual quality constraints can increase the rate needed for lossy compression. Our theoretical framework shares the insight that the output distribution shape (here, conformity to the text manifold) imposes additional costs beyond standard rate-distortion.

[20] h2: 3 Problem formulation

[21] p: Having described the phenomenon, we now formalize the architecture and the mismatch that causes it.

[22] p: Architecture. We consider the standard multimodal LLM pipeline:

[23] table: X → E ϕ H → P θ Z → L ψ ​ ( ⋅ , C ) Y ^ X\xrightarrow{E_{\phi}}H\xrightarrow{P_{\theta}}Z\xrightarrow{L_{\psi}(\cdot,C)}\hat{Y} (1)

[24] p: where X X is a non-text input (speech waveform or image), E ϕ E_{\phi} is a pre-trained encoder (e.g., Whisper ( Radford et al., 2023 ) , CLIP ( Radford et al., 2021 ) ), P θ P_{\theta} is a learned adapter (linear or MLP projection), Z ∈ ℝ d Z\in\mathbb{R}^{d} are the hidden states consumed by the LLM L ψ L_{\psi} , C C is the text context (prompt), and Y ^ \hat{Y} is the generated output. At inference, all components are fixed: the scoring rule q ψ q_{\psi} is whatever the training procedure produced. In the common adapter paradigm, only P θ P_{\theta} is trained while E ϕ E_{\phi} and L ψ L_{\psi} are pre-trained; in end-to-end approaches, all components are jointly trained. Either way, at inference the decoder’s scoring rule is fixed, and our theory describes what that fixed scoring rule can extract. The specific form of P θ P_{\theta} varies (linear, MLP, Q-Former ( Dai et al., 2023 ) , perceiver, codebook), but the mismatch depends on the scoring rule, not the adapter type (§ 6.1 ).

[25] p: Text law and modal law. Let q ψ ​ ( y | z , c ) = L ψ ​ ( z , c ) q_{\psi}(y|z,c)=L_{\psi}(z,c) denote the LLM’s next-token distribution at inference. During pre-training, the LLM processes hidden states drawn from the text law P T ​ ( C , Z , Y ) P_{\!T}(C,Z,Y) . When processing adapted non-text inputs, the hidden states follow a different modal law P M ​ ( C , Z , Y ) P_{\!M}(C,Z,Y) .

[26] h6: Assumption 1 (Shared marginal) .

[27] p: The text and modal laws share the same prompts and target tokens: P M ​ ( C , Y ) = P T ​ ( C , Y ) P_{\!M}(C,Y)=P_{\!T}(C,Y) .

[28] p: In other words, the task is the same (e.g., “transcribe this speech”), and only the internal representations Z Z differ. This isolates the effect of the representation distribution from confounds in the task itself.

[29] p: Modality collapse. We define modality collapse as the systematic degradation or stagnation of non-text information through a text-trained decoder, depending on the mismatch intensity. For an attribute A τ A_{\tau} of type τ \tau (e.g., speaker identity, emotion), the information accessibility gap is:

[30] table: Δ access ​ ( τ ) = I ⁡ ( Z , A τ ) − GMI P M ​ ( A τ ∣ ψ ) \Delta_{\text{access}}(\tau)=I(Z;A_{\tau})-\mathrm{GMI}_{P_{\!M}}(A_{\tau}\mid\psi) (2)

[31] p: where I ⁡ ( Z , A τ ) I(Z;A_{\tau}) is the mutual information (recoverable by an optimal probe) and GMI P M ​ ( A τ | ψ ) \mathrm{GMI}_{P_{\!M}}(A_{\tau}|\psi) is the information actually extractable by the decoder’s fixed scoring rule. When Δ access = 0 \Delta_{\text{access}}=0 , the decoder extracts everything the probe can; when Δ access \Delta_{\text{access}} is large, information is present but inaccessible.

[32] p: Text-aligned encoders as correlation mappings. Contrastive encoders like CLIP ( Radford et al., 2021 ) and SigLIP ( Zhai et al., 2023 ) do not merge the modality manifolds (the modality gap persists ( Liang et al., 2022 ) ), but they align the informative directions : attributes that co-occur with text descriptions occupy dimensions also used by text representations. When such an encoder feeds an LLM, the modal law P M P_{\!M} has high overlap with P T P_{\!T} along informative dimensions, so the distributional distance is small and the accessibility gap is correspondingly small (§ A.2 formalizes this via the Wasserstein distance). Non-contrastive encoders like DINOv2 ( Oquab et al., 2024 ) lack this alignment: their informative directions may be orthogonal to P T P_{\!T} , making the information effectively inaccessible to the decoder. We return to this in § 5.3 , where the Prismatic comparison provides direct evidence.

[33] h2: 4 Theoretical framework

[34] p: The formulation above makes the information loss quantifiable. We establish three results (formal statements, assumptions, and proofs in Appendix A ):

[35] p: 1. The decoder has a ceiling. Standard mutual information I ⁡ ( Z , Y ) I(Z;Y) measures how much information Z Z contains about Y Y assuming an optimal decoder. But the LLM is not optimal for non-text inputs. The relevant quantity is instead the Generalized Mutual Information (GMI) ( Merhav et al., 1994 ; Scarlett et al., 2020 ) , which measures the maximum rate extractable by a fixed decoder with a given scoring rule. Regardless of how much information a probe can extract from Z Z , the decoder can never exceed GMI P M ​ ( q ψ ) \mathrm{GMI}_{P_{\!M}}(q_{\psi}) (Theorem 1 ).

[36] p: 2. The ceiling drops with distributional distance. When modal representations P M P_{\!M} differ from the text representations P T P_{\!T} the decoder was trained on, the GMI degrades. We bound this degradation (Theorem 2 ): it scales with the product of two empirically measurable quantities: (i) the Wasserstein distance W 1 ​ ( P M , P T ) W_{\!1}(P_{\!M},P_{\!T}) , measuring how far modal representations are from text representations, and (ii) the decoder’s Lipschitz constant L log L_{\log} , measuring how sensitive its log-probability is to shifts in the input. The bound makes a clear prediction: models with larger L log ⋅ W 1 L_{\log}\cdot W_{\!1} should show more degradation, which we validate in § 5.5 .

[37] p: 3. Probes and decoders respond differently to the same shift. A linear probe’s sensitivity to distributional shift is controlled by its own (small) Lipschitz constant L h L_{h} (Theorem 3 ). The decoder’s sensitivity is controlled by L log L_{\log} , which is empirically 30 × \times larger. The same W 1 W_{\!1} shift therefore produces small degradation for probes but large degradation for the decoder. This is why information can be present (probes recover it) yet inaccessible (the decoder cannot use it).

[38] h2: 5 Experimental validation

[39] p: The bound in Theorem 2 makes three quantities empirically measurable: (i) the Lipschitz constant L log L_{\log} , estimated via gradient norms, measuring the decoder’s sensitivity to input perturbations; (ii) the Wasserstein distance W 1 ​ ( P M , P T ) W_{\!1}(P_{\!M},P_{\!T}) , estimated between modal and text hidden states at matched layers; and (iii) the mode alignment spectrum α ~ ​ ( u k ) \tilde{\alpha}(u_{k}) , which decomposes W 1 W_{\!1} geometrically by identifying which directions carry the mismatch. We validate each in turn.

[40] h3: 5.1 Setup

[41] p: Models. We study five multimodal LLMs spanning two modalities (Table 1 ). For speech: Ultravox-v0.6 ( Fixie AI, 2024 ) (Whisper encoder, MLP adapter with SwiGLU, Llama-3.1-8B) and Qwen2-Audio-7B ( Chu et al., 2024 ) (Whisper encoder, linear adapter, Qwen2-7B). For vision: LLaVA-v1.5-7B ( Liu et al., 2023 ) (CLIP-ViT, MLP adapter, Vicuna-7B) and two Prismatic VLMs ( Karamcheti et al., 2024 ) sharing the same MLP adapter and Vicuna-7B backbone but differing only in their vision encoder: DINOv2 (not text-aligned) and SigLIP (text-aligned via contrastive loss).

[42] figure: Model Encoder Text-aligned? LLM Ultravox Whisper No Llama-3.1-8B Qwen2-Audio Whisper No Qwen2-7B LLaVA CLIP-ViT Yes Vicuna-7B Prismatic-D DINOv2 No Vicuna-7B Prismatic-S SigLIP Yes Vicuna-7B Table 1: Models studied. Prismatic-D and Prismatic-S share the same architecture, adapter, training recipe, and LLM backbone; only the vision encoder differs.

[43] p: Datasets. Speech: LibriSpeech ( Panayotov et al., 2015 ) (2,620 samples, 50 words, 40 speakers), CREMA-D ( Cao et al., 2014 ) (7,442 samples, 6 emotions, 91 speakers), ESC-50 ( Piczak, 2015 ) (2,000 samples, 50 sound classes). Vision: MS-COCO ( Lin et al., 2014 ) (5,000 images, 69 object categories, 12 super-categories).

[44] p: Probing protocol. We extract representations at four hook points per model: encoder output, adapter output, LLM layer 16, and LLM final layer (after LayerNorm). Representations are mean-pooled across sequence positions (restricting to audio-only tokens yields nearly identical results; Appendix Table 9 ). We train ℓ 2 \ell_{2} -regularized logistic regression probes (5 seeds, 80/20 stratified split, z z -score normalization) for each combination of hook point, information type, and dataset.

[45] p: Information types. Speech: lexical (word identity), speaker (speaker identity), emotion (6-way), acoustic (sound class). Vision: lexical (caption-based word prediction), object category (69-way), super-category (12-way).

[46] p: The Prismatic pair (shared architecture, different encoder) and the two speech models (shared encoder, different LLM) provide controlled contrasts that isolate specific variables.

[47] h3: 5.2 Modality-specific structure interferes with decoding

[48] p: We directly test whether the decoder’s scoring rule functionally depends on modality-specific (MS) directions by projecting them out at inference time and measuring the change in cross-entropy. Unlike probing, which tests representational presence, this is a direct intervention on the decoder’s input.

[49] p: We decompose the adapter output into eigenmodes (principal directions of variance) and ask: how much of this variance does the text distribution also use? Each eigenmode u k u_{k} gets a text alignment score α ~ ​ ( u k ) = u k ⊤ ​ Σ T ​ u k / λ k \tilde{\alpha}(u_{k})=u_{k}^{\top}\Sigma_{T}u_{k}/\lambda_{k} , the fraction of its variance that text representations share (§ 5.6 ). Modes with α ~ < 0.5 \tilde{\alpha}<0.5 are modality-specific (MS): most of their variance comes from the non-text modality. We then surgically remove selected directions from the decoder’s input ( z ′ = z − ∑ k ∈ S ( z ⊤ ​ u k ) ​ u k z^{\prime}=z-\sum_{k\in S}(z^{\top}u_{k})\,u_{k} ) and measure the effect on cross-entropy. We compare three conditions (200 samples per model): (i) ablate all MS modes, (ii) ablate a matched number of top text-aligned (TA) modes, (iii) no ablation.

[50] figure: Model Condition Modes Var. % Δ \Delta Loss (%) Non-aligned encoders Ultravox MS (all) 11 63.6 − - 1.4 TA-matched 11 29.4 − - 0.3 Random 11 2.8 + + 0.3 Prismatic-D MS (all) 53 71.0 − - 11.1 TA-matched 47 29.0 − - 0.07 Random 53 39.1 − - 5.1 Text-aligned encoder Prismatic-S MS (all) 14 24.6 − - 0.5 TA-matched 14 36.2 − - 0.7 Random 14 10.6 − - 0.2 Table 2: Causal ablation at the adapter output. Eigenmodes are classified as modality-specific (MS; α ~ < 0.5 \tilde{\alpha}<0.5 ) or text-aligned (TA), and matched subsets are projected out. Random controls ablate the same number of modes chosen uniformly at random (seed-averaged). For non-aligned encoders, removing MS modes improves loss while removing equal-sized TA subsets has negligible effect; the contrast is 160 × 160\times for Prismatic-D ( t = − 25.2 t=-25.2 vs. t = − 0.4 t=-0.4 ). Random ablation gives intermediate effects proportional to variance removed. For SigLIP, few modes are MS and all effects are < 1 % {<}1\% .

[51] p: MS structure is not merely unused; its presence degrades decoding. Unlike concept erasure methods such as LEACE ( Belrose et al., 2023 ) , which project out directions predictive of a labeled attribute, our ablation targets directions identified by distributional mismatch between modal and text covariances, without requiring any concept labels. The question is not whether a concept can be erased, but whether the decoder uses these distribution-mismatched directions at all.

[52] p: Table 2 reveals a stark asymmetry across all three models. For Ultravox, removing 11 MS modes (63.6% of variance) slightly improves cross-entropy ( − - 1.4%, t = − 7.0 t=-7.0 ), while removing a matched TA subset has negligible effect ( − - 0.3%, t = − 2.2 t=-2.2 ). The Prismatic-D result is even more striking: ablating 53 MS modes (71% of variance) reduces loss by 11.1% ( t = − 25.2 t=-25.2 ), while ablating the top 47 TA modes (29% of variance) has no measurable effect ( − - 0.07%, t = − 0.4 t=-0.4 , p = 0.69 p=0.69 ). The decoder is functionally indifferent to the directions where most adapter variance concentrates, precisely as the mismatched-decoder theory predicts.

[53] p: For Prismatic-S (text-aligned), only 14 of 100 modes are MS (24.6% of variance) and all ablation effects are below 1%, consistent with SigLIP producing representations the decoder already expects.

[54] h3: 5.3 Controlled experiment: text-aligned vs. non-aligned encoders

[55] p: The causal ablation establishes that MS directions interfere with decoding. We now isolate why some models have more MS variance than others, using the Prismatic pair as a controlled comparison that holds everything constant except encoder text alignment.

[56] p: Both Prismatic VLMs share the same MLP adapter, Vicuna-7B backbone, and training recipe. The only difference is the vision encoder: DINOv2 ( Oquab et al., 2024 ) (no text alignment) versus SigLIP ( Zhai et al., 2023 ) (contrastive text–image loss). If our theory is correct, SigLIP should produce representations closer to P T P_{\!T} , yielding smaller W 1 ​ ( P M , P T ) W_{\!1}(P_{\!M},P_{\!T}) and less information loss.

[57] p: The results confirm the prediction (Appendix Figure 1 , Table 10 ). With DINOv2, visual information passes through the LLM essentially unchanged ( − - 0.0% object category). With SigLIP, the same information types improve ( + + 1.9% object category, + + 2.3% super-category). This pattern replicates across modalities: in speech, Whisper-based encoders show dramatic lexical recovery ( + + 92–95%) alongside speaker collapse ( − - 8% to − - 39%); in LLaVA (CLIP encoder, text-aligned), all information types improve (Appendix Table 7 ).

[58] h3: 5.4 The information accessibility gap in practice

[59] p: The causal ablation (§ 5.2 ) establishes that the decoder does not use MS directions, and the controlled comparison (§ 5.3 ) traces this to encoder text alignment. Probes confirm the information has not been destroyed (Appendix Tables 7 , 5 ).

[60] p: At the final LLM layer, all non-text information types remain 3–55 × \times above chance: speaker identity in Ultravox at .556 .556 vs. .025 .025 chance ( 22 × 22\times ), object categories in Prismatic-D at .792 .792 vs. .014 .014 chance ( 55 × 55\times ). Both speech models show the same split: lexical accuracy nearly doubles through the LLM ( + + 92% Ultravox, + + 95% Qwen2-Audio), while speaker identity degrades monotonically ( − - 8% to − - 39%). This asymmetric amplification is the signature of a text-trained scoring rule: sharp gradients along text-aligned directions, flat gradients elsewhere. When the encoder is text-aligned (CLIP in LLaVA), P M ≈ P T P_{\!M}\approx P_{\!T} and all information types improve ( + + 5–8%). This is consistent with findings from the LISTEN benchmark ( Chen et al., 2026 ) , which demonstrates that audio LLMs rely on lexical transcription cues rather than acoustic features for emotion recognition, a behavioral manifestation of the decoder indifference we characterize here.

[61] p: Three non-textual visual attributes (object count, size, spatial spread) derived from COCO annotations but absent from captions confirm the pattern in a milder mismatch regime ( L log ⋅ W 1 ≈ 13 L_{\log}\cdot W_{\!1}\approx 13 – 54 54 vs. 162 162 for speech), explaining stagnation rather than degradation (Appendix Table 10 ).

[62] h3: 5.5 Validating the bound

[63] p: Theorem 2 predicts that GMI degradation scales with L log ⋅ W 1 L_{\log}\cdot W_{\!1} . We estimate both quantities empirically (full results in Appendix Table 8 ). L log L_{\log} is finite for all nine model-dataset combinations, confirming the Lipschitz log-score assumption (Assumption 2 , Appendix A.2 ). Three patterns emerge: (i) L log L_{\log} is content-dependent, decreasing as audio moves away from text ( 9.08 9.08 speech → \to 3.66 3.66 environmental sounds in Ultravox); (ii) L log L_{\log} varies 30 × 30\times across architectures ( 0.29 0.29 LLaVA to 9.08 9.08 Ultravox); (iii) Prismatic-S has 2.8 × 2.8\times higher L log L_{\log} than Prismatic-D ( 1.12 1.12 vs. 0.40 0.40 ), consistent with the LLM being more responsive to text-aligned representations. W 1 W_{\!1} ranges from 17.8 to 50.4 across models.

[64] p: Gradient isotropy. The mean gradient norm along modality-specific directions ( g MS g_{\text{MS}} ) is nearly identical to that along text-aligned directions ( g TA g_{\text{TA}} ): g TA / g MS = 0.94 × g_{\text{TA}}/g_{\text{MS}}=0.94\times , Spearman r = 0.11 r=0.11 , p = 0.28 p=0.28 . This validates the scalar L log L_{\log} assumption: the decoder responds with similar magnitude to perturbations in any direction. But MS modes carry structured variance that pushes predictions away from text distributions, while TA modes carry variance the decoder was trained to exploit. Same sensitivity, different semantic effect.

[65] p: The product L log ⋅ W 1 L_{\log}\cdot W_{\!1} is largest for Ultravox ( 162 162 ), which shows the most dramatic degradation ( − - 39% speaker), and smallest for LLaVA ( 13.4 13.4 ), where all information types improve. Prismatic-S has a higher product ( 53.7 53.7 ) than Prismatic-D ( 20.2 20.2 ) despite showing less degradation; this reflects higher decoder responsiveness to text-aligned representations rather than greater mismatch. The bound’s prefactor is also smaller for Prismatic-S because its effective support diameter is smaller ( D = 16.2 D=16.2 vs. 35.7 35.7 ).

[66] p: The raw bound uses the ambient representation diameter D D , which makes the prefactor vacuously large. The support-restricted bound (Appendix A.3 ) allows replacing D D with the effective support diameter D eff D_{\text{eff}} , estimated via the participation ratio of the pooled representation covariance. This yields L log ⋅ D eff ∈ [ 3 , 7 ] L_{\log}\cdot D_{\text{eff}}\in[3,7] , making the prefactor moderate ( ∼ \sim 20–1100). The bound is structural rather than tight: it identifies L log ⋅ W 1 L_{\log}\cdot W_{\!1} as the governing quantity and correctly predicts which models collapse most.

[67] p: Per-type prediction. The theory correctly predicts the aggregate pattern: text-aligned information recovers or improves, while non-text types degrade or stagnate. A finer prediction (degradation correlating with each type’s MS-variance share) does not hold at this granularity (Spearman ρ = − 0.40 \rho=-0.40 , p = 0.60 p=0.60 ), likely because the content-dependent L log L_{\log} (which varies 2.5 × 2.5\times across audio types) modulates degradation beyond geometric alignment alone.

[68] h3: 5.6 Mode alignment

[69] p: The bound explains how much information is lost; mode alignment explains which directions carry the mismatch. We decompose the adapter output into its principal directions of variance (eigenmodes of Σ M \Sigma_{M} ) and measure, for each direction, the fraction of its variance that the text distribution shares: α ~ ​ ( u k ) = u k ⊤ ​ Σ T ​ u k / λ k \tilde{\alpha}(u_{k})=u_{k}^{\top}\Sigma_{T}u_{k}/\lambda_{k} . A score near 1 means the direction is shared with text; near 0 means it is unique to the modality (Appendix Table 11 , Figure 2 ).

[70] p: For non-aligned encoders, the largest direction (Mode 0) is modality-specific ( α ~ ≤ 0.034 \tilde{\alpha}\leq 0.034 ), capturing 51–79% of adapter variance. Most of what the adapter transmits is invisible to the text distribution. For SigLIP, even Mode 0 is shared with text ( α ~ = 0.83 \tilde{\alpha}=0.83 ). As representations pass through the LLM, text-aligned variance is amplified ( ∼ 150 × {\sim}150\times ) while MS variance remains flat: MS modes drop from 63.6% of adapter variance to < < 1% at the final layer in Ultravox, not destroyed but drowned out.

[71] h2: 6 Discussion

[72] h3: 6.1 Implications

[73] p: The fix is objective-side, not encoder-side. If modality collapse is a consequence of the scoring rule being text-shaped, the natural intervention is to reshape the scoring rule. Low-rank adaptation (LoRA; Hu et al., 2022 ) on the LLM adjusts q ψ q_{\psi} to better match P M P_{\!M} , effectively reducing the functional mismatch. Preliminary evidence from concurrent work ( Billa, 2026 ) is consistent: applying LoRA to the LLM backbone reduces text dominance by 23.9%, while adapter-only training increases text dominance by 26.5%. This is predicted by Theorem 2 : LoRA reduces the functional mismatch between P M P_{\!M} and P T P_{\!T} by reshaping the scoring rule, whereas adapter-only training leaves the decoder’s text-shaped sensitivity unchanged.

[74] p: However, LoRA on the decoder is necessary but not sufficient : the training objective must explicitly target non-text information. We demonstrate this with two contrasting experiments on Ultravox, using the same LoRA configuration ( r = 16 r{=}16 , α = 32 \alpha{=}32 , targeting q/k/v/o_proj ).

[75] p: Negative example (text-centric objective). We apply a LoRA checkpoint trained for audio-text conflict resolution (ALME; Billa, 2026 ) and measure linear probe accuracy on LibriSpeech. Speaker identity accuracy is unchanged (55.0% vs. 54.5% base, within noise), as is lexical accuracy (53.5% vs. 52.6%). The ALME objective rewards resolving text-audio conflicts, not preserving speaker or acoustic attributes, so its gradient signal never reaches modality-specific directions.

[76] p: Positive example (emotion objective). We train a LoRA on the LLM backbone with a forced-choice emotion detection objective on CREMA-D (6 emotions, 7,442 clips, standard causal LM loss on assistant tokens only). Generation accuracy on held-out samples improves from 17.3% to 61.8% (Table 3 ). Critically, the emotion probe at llm-final improves from .557 .557 to .632 .632 ( + + 7.5%), while the speaker probe remains at chance ( .135 .135 vs. .137 .137 ) and lexical accuracy remains near-ceiling ( .994 .994 ). Upstream layers (encoder, adapter) are identical across conditions, confirming the change is entirely in the LLM. The LoRA reshapes the scoring rule so that, at inference, the decoder responds to emotion-relevant directions while leaving others untouched, as Theorem 2 predicts: the emotion objective reduces W 1 W_{\!1} along emotion-correlated dimensions without affecting orthogonal ones.

[77] figure: Table 3: LoRA intervention on Ultravox (CREMA-D, llm-final probe accuracy). The emotion LoRA selectively improves emotion accessibility without meaningfully affecting speaker or lexical probes. Generation accuracy measures forced-choice emotion detection on 1,002 held-out samples. The encoder and adapter outputs are identical across conditions (LoRA modifies only the LLM). Condition Emotion Speaker Lexical Gen. acc. Base Ultravox .557 .137 1.000 17.3% + Emotion LoRA .632 .135 .994 61.8% Δ \Delta + + 7.5% − - 0.2% − - 0.6% + + 44.5%

[78] p: Together, the negative and positive examples confirm that the training objective determines which dimensions of the scoring rule are reshaped. A text-centric objective (ALME) leaves the decoder blind to non-text directions; an objective targeting a specific non-text attribute (emotion) teaches the decoder to respond to exactly that dimension.

[79] p: Text-aligned encoders are a workaround, not a solution. Contrastive encoders like CLIP and SigLIP achieve low mismatch by mapping inputs onto text-correlated dimensions, but this is a projection, not a preservation: modality-specific information with no textual correlate is discarded at the encoder. The Prismatic comparison confirms this: SigLIP’s visual information “improves” through the LLM only because it was pre-projected onto text-like directions. CLIP gives the LLM access to textual correlates of visual information, not visual information itself.

[80] p: Models must be explicitly trained to use non-text modalities. A text-trained decoder responds only to directions it was trained on (§ 5.6 ). No adapter can make it sensitive to directions it has never seen. To build models that genuinely leverage modality-specific information, not just its textual shadow, the training objective must reward extracting non-text directions, whether through LoRA, full multimodal pre-training, or other objective-side interventions. Without this, non-textual information remains hidden in plain sight.

[81] p: The framework is architecture-agnostic. Our experiments use models with explicit adapter modules, but the analysis does not depend on them. The bound is a property of the decoder’s scoring rule , not of any particular architectural component. Any system where a text-trained decoder processes non-text representations faces the same constraint, whether the representations arrive through a linear projection, an MLP, a Q-Former, a discrete codebook ( Borsos et al., 2023 ; Défossez et al., 2024 ) , or no explicit adapter at all. The LLM’s own layers implicitly serve as the adapter. Discrete-token approaches add a quantization bottleneck that can only increase W 1 ​ ( P M , P T ) W_{\!1}(P_{\!M},P_{\!T}) , making our bound conservative. The core mechanism is the mismatch between the decoder’s training distribution and its inputs at inference, and that mechanism is universal.

[82] h3: 6.2 Limitations

[83] p: Probes as information measures. Linear probes are necessary but not sufficient ( Belinkov, 2022 ) , but the key asymmetry (more information is linearly recoverable than the decoder uses) holds regardless. We estimate L log L_{\log} via p95 gradient norms, not the true supremum. Additional limitations (scope, Assumption 1 ) are in Appendix D .

[84] p: Vision collapse is partial. Vision models show stagnation ( ± \pm 1–2%) rather than degradation ( − - 39% for speech). This reflects a milder mismatch regime ( L log ⋅ W 1 L_{\log}\cdot W_{\!1} is 3–12 × \times smaller), though the effect is statistically reliable in the causal ablation (Prismatic-D: − - 11.1%, t = − 25.2 t=-25.2 ). Probes for purely perceptual attributes (texture, depth, material) would likely show larger effects.

[85] h2: 7 Conclusion

[86] p: Modality collapse is a failure of decoding , not encoding. Across five models spanning speech and vision, non-text information survives through every LLM layer (3–55 × \times above chance) yet the decoder does not use it; removing modality-specific directions improves decoding. The GMI-Wasserstein bound formalizes the mechanism: accessible information is limited to text-aligned directions, with degradation governed by distributional distance and decoder sensitivity.

[87] p: Building multimodal models that truly use what they perceive requires reshaping the decoder’s scoring rule. Text-aligned encoders appear to help but work by discarding non-textual information at the encoder. Our LoRA experiment shows the real fix: training with an emotion objective teaches the decoder to respond to emotion-relevant directions ( + + 7.5% probe, + + 44.5% generation accuracy) while leaving others untouched.

[88] p: The framework extends beyond the models and modalities studied here. The bound is a property of the decoder’s scoring rule, not of any architectural component; no explicit adapter is required. At inference, every trained model has a fixed scoring rule. If that scoring rule was shaped predominantly by text, the constraint applies regardless of architecture or training recipe. The question is not whether modality-specific information can be encoded (it already is) but whether the training objective teaches the decoder to use it. Until it does, that information remains hidden in plain sight.

[89] h2: Reproducibility statement

[90] p: All models are publicly available. Complete reproduction code, pipeline scripts, and expected-value regression tests are available at https://github.com/jb1999/modality_collapse_paper . Hook points, hyperparameters, and seeds are in Appendix B . All experiments run on a single NVIDIA RTX 3090 Ti (24GB).

[91] h2: References

[92] h2: Appendix A Theoretical framework: detailed treatment

[93] p: This appendix provides the full formal development summarized in § 4 . We aim to make this self-contained: each result is preceded by an intuitive explanation, followed by the formal statement and a detailed proof with annotations.

[94] h3: A.1 Generalized Mutual Information (GMI)

[95] p: The core question. A representation Z Z may contain information about a target Y Y (e.g., the next token). But how much of that information can a specific decoder actually use ? Standard mutual information I ⁡ ( Z , Y ) I(Z;Y) answers this for an ideal decoder that is perfectly tuned to the data it receives. A text-trained LLM is not ideal for non-text inputs: it was tuned on text representations, not speech or image representations. We need a measure that accounts for this mismatch. That measure is the Generalized Mutual Information (GMI) ( Merhav et al., 1994 ; Scarlett et al., 2020 ) .

[96] p: We use the same notation as § 3 : q ψ ​ ( y | z , c ) q_{\psi}(y|z,c) is the decoder’s next-token distribution (Eq. 1 ), Z Z is the representation consumed by the LLM, C C is the text context, and Y Y is the target token. Let ℓ ψ ​ ( c , z , y ) := log ⁡ q ψ ​ ( y | z , c ) \ell_{\psi}(c,z,y):=\log q_{\psi}(y|z,c) be the decoder’s log-score (the log-probability it assigns to token y y given representation z z and context c c ), clipped at a floor η = 1 / | 𝒱 | \eta=1/|\mathcal{V}| (where 𝒱 \mathcal{V} is the decoder’s output vocabulary) to ensure boundedness.

[97] p: Intuition. The GMI measures how well the decoder can tell the “right” representation from random alternatives. In words:

[98] table: GMI = 𝔼 ⁡ [ Score of the true match ⏟ how well the decoder scores the actual ​ Z − LogSumExp over all alternatives ⏟ how well random ​ Z ′ ​ would score on average ] . \text{GMI}\;=\;\mathbb{E}\bigl[\,\underbrace{\text{Score of the true match}}_{\text{how well the decoder scores the actual }Z}\;-\;\underbrace{\text{LogSumExp over all alternatives}}_{\text{how well random }Z^{\prime}\text{ would score on average}}\,\bigr].

[99] p: When the decoder reliably scores the correct representation higher than random draws, the GMI is large. When it treats all representations interchangeably (i.e., it cannot tell which Z Z goes with which Y Y ), the GMI collapses to zero. This is closely related to the Donsker-Varadhan variational representation of KL divergence ( Donsker & Varadhan, 1983 ) , applied to the decoder’s scoring function rather than an arbitrary test function.

[100] p: Formally, for a joint distribution P P over ( C , Z , Y ) (C,Z,Y) (either the text distribution P T P_{\!T} or the modal distribution P M P_{\!M} from § 3 ), the GMI is:

[101] table: GMI P ( q ψ ) = 𝔼 ( C , Z , Y ) ∼ P [ ℓ ψ ( C , Z , Y ) − log 𝔼 Z ′ ∼ P ( ⋅ | C , Y ) [ e ℓ ψ ​ ( C , Z ′ , Y ) ] ] . \mathrm{GMI}_{P}(q_{\psi})=\mathbb{E}_{(C,Z,Y)\sim P}\!\left[\ell_{\psi}(C,Z,Y)-\log\mathbb{E}_{Z^{\prime}\sim P(\cdot|C,Y)}\!\left[e^{\ell_{\psi}(C,Z^{\prime},Y)}\right]\right]. (3)

[102] h6: Theorem 1 (Accessible rate = GMI; following Scarlett et al., 2020 ) .

[103] p: Under i.i.d. sampling from P M P_{\!M} and standard measurability conditions, the maximum rate extractable by the fixed decoder q ψ q_{\psi} is R acc ​ ( P M , q ψ ) = GMI P M ​ ( q ψ ) R_{\mathrm{acc}}(P_{\!M},q_{\psi})=\mathrm{GMI}_{P_{\!M}}(q_{\psi}) .

[104] p: This is a direct application of the random-coding argument of Scarlett et al. (2020) , Chapters 2–3, with constant-composition codebooks under the GMI decoder metric. The key insight is that the decoder q ψ q_{\psi} defines a fixed scoring rule (fixed at inference, regardless of how it was trained), and the maximum rate extractable under this rule, averaged over random codebooks drawn from P M P_{\!M} , converges to GMI P M ​ ( q ψ ) \mathrm{GMI}_{P_{\!M}}(q_{\psi}) .

[105] p: The implication is sharp: regardless of how much information a probe can extract from Z Z , the decoder can never exceed GMI P M ​ ( q ψ ) \mathrm{GMI}_{P_{\!M}}(q_{\psi}) .

[106] h3: A.2 GMI-Wasserstein bound

[107] p: We now bound the GMI degradation when the decoder sees modal representations P M P_{\!M} instead of the text representations P T P_{\!T} it was trained on. The intuition is simple: if modal representations are close to text representations, the decoder should perform nearly as well on them. Two properties of the decoder determine how “close” is close enough: how sensitive it is to small shifts in its input, and how large the space of possible representations is.

[108] h6: Assumption 2 (Local Lipschitz log-score) .

[109] p: There exists L log > 0 L_{\log}>0 such that for all ( c , y ) (c,y) and all z , z ′ z,z^{\prime} in the typical-state region 𝒵 \mathcal{Z} : | ℓ ψ ​ ( c , z , y ) − ℓ ψ ​ ( c , z ′ , y ) | ≤ L log ​ ‖ z − z ′ ‖ |\ell_{\psi}(c,z,y)-\ell_{\psi}(c,z^{\prime},y)|\leq L_{\log}\|z-z^{\prime}\| .

[110] p: That is, if you nudge a representation by a small amount, the decoder’s log-probability changes by at most L log L_{\log} times that amount. The constant L log L_{\log} captures how sensitive the decoder is to shifts in its input. Neural networks with smooth activations satisfy this locally; we estimate L log L_{\log} empirically via gradient norms (§ 5.5 ).

[111] h6: Assumption 3 (Bounded typical-state region) .

[112] p: The typical-state region 𝒵 \mathcal{Z} has diameter D = sup z , z ′ ∈ 𝒵 ‖ z − z ′ ‖ D=\sup_{z,z^{\prime}\in\mathcal{Z}}\|z-z^{\prime}\| , which is finite and O ⁡ ( d ) O(\sqrt{d}) after LayerNorm.

[113] p: This says the representations that actually occur in practice live in a bounded region, not scattered arbitrarily through ℝ d \mathbb{R}^{d} . LayerNorm ensures this by projecting all hidden states onto a hypersphere of radius d \sqrt{d} .

[114] h6: Theorem 2 (GMI-Wasserstein bound) .

[115] p: Under Assumptions 1 , 2 , and 3 :

[116] table: | GMI P M ​ ( q ψ ) − GMI P T ​ ( q ψ ) | ≤ ( 1 + e L log ⋅ D ) ⋅ L log ⋅ 𝔼 ( C , Y ) ​ [ W 1 ​ ( P M ​ ( Z | C , Y ) , P T ​ ( Z | C , Y ) ) ] . |\mathrm{GMI}_{P_{\!M}}(q_{\psi})-\mathrm{GMI}_{P_{\!T}}(q_{\psi})|\leq\big(1+e^{L_{\log}\cdot D}\big)\cdot L_{\log}\cdot\mathbb{E}_{(C,Y)}\!\left[W_{\!1}\!\big(P_{\!M}(Z|C,Y),\,P_{\!T}(Z|C,Y)\big)\right]. (4)

[117] p: Reading the bound. In words:

[118] table: | GMI text − GMI modal | ⏟ How much information is lost ≤ ( 1 + e L log ⋅ D ) ⏟ Penalty for distributional shape ⋅ L log ⏟ Decoder sensitivity ⋅ 𝔼 ⁡ [ W 1 ​ ( P M , P T ) ] ⏟ Distributional distance \underbrace{|\text{GMI}_{\text{text}}-\text{GMI}_{\text{modal}}|}_{\text{How much information is lost}}\;\leq\;\underbrace{(1+e^{L_{\log}\cdot D})}_{\text{Penalty for distributional shape}}\;\cdot\;\underbrace{L_{\log}\vphantom{e^{D}}}_{\text{Decoder sensitivity}}\;\cdot\;\underbrace{\mathbb{E}[W_{\!1}(P_{\!M},P_{\!T})]}_{\text{Distributional distance}}

[119] p: The gap between what the decoder could extract from text representations and what it can extract from modal representations is controlled by how far apart those distributions are, amplified by how sensitive the decoder is. Crucially, W 1 W_{\!1} measures distributional distance, not just the distance between means: aligning the average modal representation with the average text representation is not enough. If the modal distribution has different shape, spread, or tails, the exponential penalty factor ( 1 + e L log ​ D ) (1+e^{L_{\log}D}) catches them. This is why text-aligned encoders reduce the bound (they project onto text-like directions, reducing both the distance and the shape mismatch) while simple mean-centering would not.

[120] p: The prefactor ( 1 + e L log ​ D ) (1+e^{L_{\log}D}) arises from the “competition term” in the proof (see below). In the ambient space this prefactor is vacuously large ( L log ⋅ D L_{\log}\cdot D ranges from 10 to 150); the support-restricted bound (§ A.3 ) tightens it using the effective support diameter.

[121] h4: A.2.1 Proof of Theorem 2

[122] p: Proof overview. The GMI has two pieces: (A) how well the decoder scores the correct representation, and (B) how well it scores random alternatives. We need to show that switching from text to modal representations does not change either piece by too much. For piece (A), the argument is simple: if the decoder’s scores change smoothly (Lipschitz assumption), then moving representations a small distance changes expected scores by a small amount. For piece (B), the argument is harder because piece (B) involves an exponential of the scores, which amplifies small changes. The bounded-diameter assumption (representations live in a finite region) keeps this amplification under control.

[123] p: Setup. Write ℓ ⁡ ( z ) ≡ ℓ ψ ​ ( c , z , y ) \ell(z)\equiv\ell_{\psi}(c,z,y) for fixed ( c , y ) (c,y) . The GMI functional decomposes as Γ ⁡ ( P ) = A ⁡ ( P ) − B ⁡ ( P ) \Gamma(P)=A(P)-B(P) where:

[124] table: A ⁡ ( P ) \displaystyle A(P) = 𝔼 Z ∼ P ​ [ ℓ ​ ( Z ) ] \displaystyle=\mathbb{E}_{Z\sim P}[\ell(Z)] (direct term: expected score of the correct representation) (5) B ⁡ ( P ) \displaystyle B(P) = log ⁡ 𝔼 Z ∼ P ​ [ e ℓ ⁡ ( Z ) ] \displaystyle=\log\mathbb{E}_{Z\sim P}[e^{\ell(Z)}] (competition term: how well random alternatives score) (6)

[125] p: We bound | A ⁡ ( P M ) − A ⁡ ( P T ) | |A(P_{\!M})-A(P_{\!T})| and | B ⁡ ( P M ) − B ⁡ ( P T ) | |B(P_{\!M})-B(P_{\!T})| separately.

[126] p: Step 1: Direct term (how much does the correct representation’s score change?). We want to bound how much the expected score changes when we switch from P T P_{\!T} to P M P_{\!M} . The Kantorovich–Rubinstein theorem ( Kantorovich & Rubinstein, 1958 ; Villani, 2009 ) says: if a function changes by at most L L when you move its input by 1 unit ( L L -Lipschitz), then the difference in its expected value under two distributions is at most L L times the Wasserstein distance between those distributions. Since ℓ \ell is L log L_{\log} -Lipschitz (Assumption 2 ):

[127] table: | A ⁡ ( P M ) − A ⁡ ( P T ) | = | 𝔼 P M ​ [ ℓ ] − 𝔼 P T ​ [ ℓ ] | ≤ L log ⋅ W 1 ​ ( P M , P T ) . |A(P_{\!M})-A(P_{\!T})|=|\mathbb{E}_{P_{\!M}}[\ell]-\mathbb{E}_{P_{\!T}}[\ell]|\leq L_{\log}\cdot W_{\!1}(P_{\!M},P_{\!T}). (7)

[128] p: In words: if modal and text representations are close (small W 1 W_{\!1} ) and the decoder’s scores change smoothly (small L log L_{\log} ), then the expected score barely changes.

[129] p: Step 2: Competition term (how much does the random-alternative score change?). This is harder because B ⁡ ( P ) = log ⁡ 𝔼 ⁡ [ e ℓ ⁡ ( Z ) ] B(P)=\log\mathbb{E}[e^{\ell(Z)}] involves an exponential of the score, which amplifies small differences. A coupling π \pi is a way of pairing up samples from P M P_{\!M} and P T P_{\!T} (imagine lining up modal representations next to the text representations they most resemble). For each pair ( Z M , Z T ) (Z_{M},Z_{T}) , define Δ ​ ℓ = ℓ ⁡ ( Z M ) − ℓ ⁡ ( Z T ) \Delta\ell=\ell(Z_{M})-\ell(Z_{T}) : the difference in score between the paired representations. By the Lipschitz assumption, | Δ ​ ℓ | ≤ L log ⋅ ‖ Z M − Z T ‖ |\Delta\ell|\leq L_{\log}\cdot\|Z_{M}-Z_{T}\| , and by the bounded diameter (Assumption 3 ), | Δ ​ ℓ | ≤ L log ⋅ D |\Delta\ell|\leq L_{\log}\cdot D .

[130] p: Write m ⁡ ( P ) = 𝔼 Z ∼ P ​ [ e ℓ ⁡ ( Z ) ] m(P)=\mathbb{E}_{Z\sim P}[e^{\ell(Z)}] . Then:

[131] table: m ⁡ ( P M ) m ⁡ ( P T ) \displaystyle\frac{m(P_{\!M})}{m(P_{\!T})} = 𝔼 π ​ [ e ℓ ⁡ ( Z M ) m ⁡ ( P T ) ] = 𝔼 π ​ [ e ℓ ⁡ ( Z T ) m ⁡ ( P T ) ⋅ e Δ ​ ℓ ] . \displaystyle=\mathbb{E}_{\pi}\!\left[\frac{e^{\ell(Z_{M})}}{m(P_{\!T})}\right]=\mathbb{E}_{\pi}\!\left[\frac{e^{\ell(Z_{T})}}{m(P_{\!T})}\cdot e^{\Delta\ell}\right]. (8)

[132] p: The first factor e ℓ ⁡ ( Z T ) / m ⁡ ( P T ) e^{\ell(Z_{T})}/m(P_{\!T}) is a probability weight under P T P_{\!T} (it sums to 1). The second factor e Δ ​ ℓ e^{\Delta\ell} captures how the shift from Z T Z_{T} to Z M Z_{M} changes the score. Since | e x − 1 | ≤ | x | ⋅ e | x | |e^{x}-1|\leq|x|\cdot e^{|x|} for bounded | x | ≤ L log ​ D |x|\leq L_{\log}D :

[133] table: | m ⁡ ( P M ) m ⁡ ( P T ) − 1 | ≤ e L log ​ D ⋅ 𝔼 π ​ [ | Δ ​ ℓ | ] ≤ e L log ​ D ⋅ L log ⋅ 𝔼 π ​ [ ‖ Z M − Z T ‖ ] . \left|\frac{m(P_{\!M})}{m(P_{\!T})}-1\right|\leq e^{L_{\log}D}\cdot\mathbb{E}_{\pi}[|\Delta\ell|]\leq e^{L_{\log}D}\cdot L_{\log}\cdot\mathbb{E}_{\pi}[\|Z_{M}-Z_{T}\|]. (9)

[134] p: Using | log ⁡ ( 1 + x ) | ≤ | x | |\log(1+x)|\leq|x| for | x | < 1 |x|<1 (applicable when W 1 W_{\!1} is small enough that the ratio stays near 1):

[135] table: | B ⁡ ( P M ) − B ⁡ ( P T ) | = | log ⁡ m ⁡ ( P M ) m ⁡ ( P T ) | ≤ e L log ​ D ⋅ L log ⋅ W 1 . |B(P_{\!M})-B(P_{\!T})|=\left|\log\frac{m(P_{\!M})}{m(P_{\!T})}\right|\leq e^{L_{\log}D}\cdot L_{\log}\cdot W_{\!1}. (10)

[136] p: The e L log ​ D e^{L_{\log}D} prefactor is the price of the exponential: the competition term is more sensitive to distributional shift than the direct term because it involves e ℓ e^{\ell} rather than ℓ \ell . This is analogous to how compound interest amplifies small rate changes: a 1% shift in the base rate produces a much larger change in the compounded amount when the compounding period is long.

[137] p: Step 3: Combine. The total GMI change is bounded by the sum of the direct and competition terms:

[138] table: | Γ ⁡ ( P M ) − Γ ⁡ ( P T ) | ≤ L log ⋅ W 1 ⏟ direct + e L log ​ D ⋅ L log ⋅ W 1 ⏟ competition = ( 1 + e L log ​ D ) ⋅ L log ⋅ W 1 . |\Gamma(P_{\!M})-\Gamma(P_{\!T})|\leq\underbrace{L_{\log}\cdot W_{\!1}}_{\text{direct}}+\underbrace{e^{L_{\log}D}\cdot L_{\log}\cdot W_{\!1}}_{\text{competition}}=(1+e^{L_{\log}D})\cdot L_{\log}\cdot W_{\!1}. (11)

[139] p: The competition term dominates: it is e L log ​ D e^{L_{\log}D} times larger than the direct term. This is why the bound’s prefactor is large, and why the support-restricted corollary (which reduces D D ) is practically important.

[140] p: Step 4: Average over ( C , Y ) (C,Y) . Everything above was for a fixed prompt C C and target Y Y . By Assumption 1 ( P M ​ ( C , Y ) = P T ​ ( C , Y ) P_{\!M}(C,Y)=P_{\!T}(C,Y) ), the same prompts and targets appear under both laws, so we simply average over all ( C , Y ) (C,Y) pairs to obtain the final bound.

[141] h3: A.3 Support-restricted bound

[142] p: Support-restricted bound. If P M ​ ( Z | c , y ) P_{\!M}(Z|c,y) and P T ​ ( Z | c , y ) P_{\!T}(Z|c,y) are both supported within a region 𝒮 ⊆ 𝒵 \mathcal{S}\subseteq\mathcal{Z} with D 𝒮 = diam ⁡ ( 𝒮 ) ≤ D D_{\mathcal{S}}=\mathrm{diam}(\mathcal{S})\leq D , then D D may be replaced by D 𝒮 D_{\mathcal{S}} in Theorem 2 .

[143] p: Proof. If both marginals are supported in 𝒮 \mathcal{S} , any coupling π \pi has support on 𝒮 × 𝒮 \mathcal{S}\times\mathcal{S} , so ‖ Z M − Z T ‖ ≤ D 𝒮 \|Z_{M}-Z_{T}\|\leq D_{\mathcal{S}} for π \pi -a.e. ( Z M , Z T ) (Z_{M},Z_{T}) . Step 2 above then bounds | Δ ​ ℓ | ≤ L log ⋅ D 𝒮 |\Delta\ell|\leq L_{\log}\cdot D_{\mathcal{S}} , giving the tighter prefactor.

[144] p: Why this matters. The ambient diameter D D makes the prefactor ( 1 + e L log ​ D ) (1+e^{L_{\log}D}) astronomically large ( L log ⋅ D L_{\log}\cdot D ranges from 10 to 150). But modal and text representations often occupy a much smaller effective region. We estimate the effective support diameter D eff D_{\text{eff}} via the participation ratio of the pooled representation covariance (§ 5.5 ), yielding L log ⋅ D eff ∈ [ 3 , 7 ] L_{\log}\cdot D_{\text{eff}}\in[3,7] and a moderate prefactor ( ∼ \sim 20–1100).

[145] h3: A.4 Probe-decoder asymmetry

[146] h6: Theorem 3 (Probe penalty) .

[147] p: Let h ⁡ ( a | z ) h(a|z) be a linear probe with log ⁡ h \log h being L h L_{h} -Lipschitz in z z . Then: | 𝔼 P M ​ [ log ⁡ h ⁡ ( A | Z ) ] − 𝔼 P T ​ [ log ⁡ h ⁡ ( A | Z ) ] | ≤ L h ⋅ W 1 ​ ( P M , P T ) |\mathbb{E}_{P_{\!M}}[\log h(A|Z)]-\mathbb{E}_{P_{\!T}}[\log h(A|Z)]|\leq L_{h}\cdot W_{\!1}(P_{\!M},P_{\!T}) .

[148] p: Proof. Identical to Step 1 of the Theorem 2 proof, replacing ℓ ψ \ell_{\psi} with log ⁡ h \log h and L log L_{\log} with L h L_{h} . Crucially, there is no competition term for probes (no random-coding argument), so the exponential prefactor does not appear.

[149] p: The key asymmetry. A linear probe is a simple instrument: one matrix multiplication followed by a softmax. Its sensitivity to distributional shift ( L h L_{h} ) is just the size of that matrix’s weights. The LLM decoder is a deep transformer with billions of parameters, and its sensitivity ( L log L_{\log} ) reflects that depth. Empirically, L log / L h ≈ 30 × L_{\log}/L_{h}\approx 30\times (§ 5.5 ).

[150] p: Now consider the same distributional shift (modal representations replacing text representations). The probe’s bound says degradation ≤ L h ⋅ W 1 \leq L_{h}\cdot W_{\!1} (small). The decoder’s bound says degradation ≤ ( 1 + e L log ​ D ) ⋅ L log ⋅ W 1 \leq(1+e^{L_{\log}D})\cdot L_{\log}\cdot W_{\!1} (large). Same shift, dramatically different impact. This is the formal basis for the “present but inaccessible” phenomenon: a probe can still read the information because it is a simple, low-sensitivity instrument, but the decoder’s complex scoring rule is far more sensitive to the distributional mismatch and cannot use it.

[151] h2: Appendix B Experimental details

[152] h3: B.1 Hook points and probing hyperparameters

[153] figure: Model Encoder Adapter LLM-16 LLM-final Ultravox audio_tower.layer_norm multi_modal_projector.ln_post language_model.model.layers.16 language_model.model.norm Qwen2-Audio audio_tower.layer_norm multi_modal_projector language_model.model.layers.16 language_model.model.norm LLaVA ...vision_tower. ...post_layernorm model.mm_projector ...language_model. layers.16 ...language_model. norm Table 4: Hook points for representation extraction.

[154] p: Logistic regression with ℓ 2 \ell_{2} regularization ( C = 1.0 C=1.0 , scikit-learn default). Five random seeds (42, 43, 44, 45, 46). 80/20 stratified train/test split. Input features z z -score normalized. Mean ± \pm std reported.

[155] h3: B.2 Lipschitz estimation

[156] p: L log L_{\log} estimated via the 2-nearest-neighbor gradient norm method over n = 1,000 n=1{,}000 samples. For each sample z i z_{i} , we compute ‖ ∇ z ​ log ​ q ψ ​ ( y i | z i , c i ) ‖ \|\nabla_{z}\log q_{\psi}(y_{i}|z_{i},c_{i})\| via autograd. The 95th percentile of the resulting distribution serves as the L log L_{\log} estimate.

[157] h3: B.3 Extraction prompts

[158] p: During representation extraction, each model receives a minimal, task-neutral prompt to avoid biasing hidden states toward any particular downstream task. Representations are extracted from intermediate hook points, not from the generated output.

[159] p: Speech models. Ultravox receives the audio placeholder token <|audio|> wrapped in the model’s chat template (system/user/assistant turns). Qwen2-Audio requires a text prompt alongside audio; we use "Describe this audio." in the user turn.

[160] p: Vision models. LLaVA receives "<image>\nDescribe this image." as the user message. Both Prismatic VLMs receive "Describe this image." formatted via the Vicuna chat template.

[161] p: Text baselines. Text baselines (Llama-3.1-8B for speech models, Vicuna-7B for vision models) process raw transcripts or captions with no additional prompt, using the model’s default tokenization.

[162] h3: B.4 LoRA experiment details

[163] p: The emotion LoRA (§ 6.1 ) uses standard causal LM fine-tuning on Ultravox with a forced-choice emotion detection objective on CREMA-D.

[164] p: LoRA configuration. Rank r = 16 r{=}16 , α = 32 \alpha{=}32 , dropout 0.05 0.05 , target modules: q_proj , k_proj , v_proj , o_proj (same configuration as the ALME LoRA used as the negative example).

[165] p: Training. AdamW optimizer, learning rate 10 − 4 10^{-4} , weight decay 0.01 0.01 , gradient accumulation 8 8 steps (effective batch size 8 8 ), gradient clipping at max norm 1.0 1.0 , mixed precision ( bfloat16 ), gradient checkpointing enabled. Five epochs with early stopping (patience 2 2 , monitoring validation loss). Best checkpoint at epoch 5 (val loss 0.0842 0.0842 , token accuracy 96.7 % 96.7\% ).

[166] p: Prompt template. Each training sample uses a three-turn chat format:

[167] p: System : “You are an expert speech analyst. When presented with audio, identify the emotion expressed by the speaker. Always prioritize what you HEAR in the audio.”

[168] p: User : Audio: <|audio|> \n\n QUESTION: What emotion is the speaker expressing? \n CHOICES: ["anger","disgust","fear","happy","neutral","sadness"] \n\n Your answer MUST be exactly one of the CHOICES above, copied verbatim. \n Output JSON only: {"answer": "<exact choice>"}

[169] p: Assistant : {"answer": "<emotion>"} (training target)

[170] p: Loss is computed only on the assistant response tokens; all input/prompt tokens are masked with label − 100 -100 .

[171] p: Data split. CREMA-D (7,442 clips, 91 speakers, 6 emotions). 80/20 stratified split yields 1,002 held-out evaluation samples (167 per emotion class), saved deterministically for reproducibility.

[172] p: Baseline evaluation. Base Ultravox (no LoRA) achieves 17.3 % 17.3\% generation accuracy on the held-out split (near chance for 6 classes), defaulting to “neutral” for most inputs.

[173] h3: B.5 Full probe accuracy tables

[174] p: Table 5 reports the full probe accuracies (mean ± \pm std over 5 seeds) at all four hook points for every model–dataset–information-type combination. The key pattern to observe: probe accuracy for non-text information types remains well above chance even at the LLM’s final layer, confirming that the information survives the decoder’s processing. It is the decoder’s use of this information, not its presence , that fails.

[175] figure: Model Info type (Dataset) Encoder Adapter LLM-16 LLM-Final Ultravox Lexical (LS) .422 ± .014 .422\pm.014 .279 ± .018 .279\pm.018 .570 ± .023 .570\pm.023 .535 ± .027 .535\pm.027 Speaker (LS) .721 ± .029 .721\pm.029 .605 ± .031 .605\pm.031 .628 ± .019 .628\pm.019 .556 ± .019 .556\pm.019 Emotion (CD) .679 ± .012 .679\pm.012 .621 ± .007 .621\pm.007 .603 ± .011 .603\pm.011 .557 ± .006 .557\pm.006 Speaker (CD) .508 ± .005 .508\pm.005 .196 ± .010 .196\pm.010 .204 ± .011 .204\pm.011 .137 ± .008 .137\pm.008 Acoustic (E50) .760 ± .033 .760\pm.033 .647 ± .041 .647\pm.041 .645 ± .035 .645\pm.035 .581 ± .032 .581\pm.032 Q2-Audio Lexical (LS) .270 ± .006 .270\pm.006 .242 ± .015 .242\pm.015 .506 ± .018 .506\pm.018 .471 ± .021 .471\pm.021 Speaker (LS) .980 ± .004 .980\pm.004 .961 ± .006 .961\pm.006 .665 ± .022 .665\pm.022 .589 ± .022 .589\pm.022 Emotion (CD) .866 ± .007 .866\pm.007 .874 ± .010 .874\pm.010 .880 ± .006 .880\pm.006 .877 ± .004 .877\pm.004 Speaker (CD) .880 ± .009 .880\pm.009 .816 ± .003 .816\pm.003 .725 ± .016 .725\pm.016 .556 ± .012 .556\pm.012 Acoustic (E50) .955 ± .005 .955\pm.005 .946 ± .011 .946\pm.011 .962 ± .004 .962\pm.004 .965 ± .003 .965\pm.003 LLaVA Lexical (CO) .629 ± .011 .629\pm.011 .620 ± .010 .620\pm.010 .675 ± .004 .675\pm.004 .669 ± .006 .669\pm.006 Object cat. (CO) .784 ± .011 .784\pm.011 .770 ± .009 .770\pm.009 .793 ± .010 .793\pm.010 .808 ± .011 .808\pm.011 Super cat. (CO) .802 ± .011 .802\pm.011 .797 ± .007 .797\pm.007 .833 ± .009 .833\pm.009 .842 ± .012 .842\pm.012 Prism.-D Lexical (CO) .608 ± .007 .608\pm.007 .637 ± .011 .637\pm.011 .652 ± .011 .652\pm.011 .664 ± .011 .664\pm.011 Object cat. (CO) .795 ± .016 .795\pm.016 .792 ± .015 .792\pm.015 .794 ± .014 .794\pm.014 .792 ± .012 .792\pm.012 Super cat. (CO) .837 ± .013 .837\pm.013 .832 ± .010 .832\pm.010 .834 ± .011 .834\pm.011 .839 ± .014 .839\pm.014 Obj. count (CO) .581 ± .017 .581\pm.017 .594 ± .015 .594\pm.015 .611 ± .015 .611\pm.015 .614 ± .016 .614\pm.016 Obj. size (CO) .667 ± .006 .667\pm.006 .679 ± .010 .679\pm.010 .693 ± .010 .693\pm.010 .688 ± .007 .688\pm.007 Spatial spr. (CO) .470 ± .013 .470\pm.013 .465 ± .025 .465\pm.025 .475 ± .010 .475\pm.010 .487 ± .008 .487\pm.008 Prism.-S Lexical (CO) .638 ± .007 .638\pm.007 .657 ± .008 .657\pm.008 .679 ± .007 .679\pm.007 .663 ± .009 .663\pm.009 Object cat. (CO) .813 ± .007 .813\pm.007 .804 ± .011 .804\pm.011 .811 ± .010 .811\pm.010 .819 ± .014 .819\pm.014 Super cat. (CO) .837 ± .013 .837\pm.013 .832 ± .017 .832\pm.017 .849 ± .010 .849\pm.010 .851 ± .010 .851\pm.010 Obj. count (CO) .594 ± .003 .594\pm.003 .598 ± .013 .598\pm.013 .652 ± .007 .652\pm.007 .647 ± .014 .647\pm.014 Obj. size (CO) .654 ± .019 .654\pm.019 .669 ± .014 .669\pm.014 .722 ± .018 .722\pm.018 .699 ± .020 .699\pm.020 Spatial spr. (CO) .478 ± .021 .478\pm.021 .459 ± .015 .459\pm.015 .507 ± .014 .507\pm.014 .481 ± .023 .481\pm.023 Table 5: Full probe accuracy (mean ± \pm std over 5 seeds) for all models, datasets, hook points, and information types.

[176] h3: B.6 Information retention overview

[177] p: Table 6 summarizes the information retention pattern across all five models. Retention is computed as the ratio of probe accuracy at the LLM’s final layer to probe accuracy at the adapter output, normalized by chance. Values above 100% indicate the LLM amplifies the signal; values below 100% indicate degradation. The key pattern: non-aligned encoders show asymmetric behavior (lexical content is amplified while speaker identity collapses), whereas text-aligned encoders retain or slightly improve all information types, but only because the encoder has already discarded non-textual information.

[178] figure: Table 6: Information retention (adapter → \to LLM-final, %). Values > 100 {>}100 % indicate the LLM amplifies information; < 100 {<}100 % indicates degradation. Text-aligned encoders retain all types; non-aligned encoders amplify lexical content while speaker identity collapses by up to 39%. LS = LibriSpeech, CD = CREMA-D, CO = COCO. Model Encoder Lexical Best non-text Worst non-text Encoder not text-aligned Ultravox Whisper 192% 92% (speaker, LS) 70% (speaker, CD) Qwen2-Audio Whisper 195% 102% (acoustic) 61% (speaker, LS) Prismatic-D DINOv2 104% 101% (super cat.) 100% (object cat.) Encoder text-aligned LLaVA CLIP 108% 106% (super cat.) 105% (object cat.) Prismatic-S SigLIP 101% 102% (obj. & super cat.) 102% (obj. & super cat.)

[179] h3: B.7 Detailed information retention

[180] p: Table 7 provides the full breakdown of information retention per model and information type, with probe accuracies at the adapter and LLM-final layers.

[181] figure: Model Info type (Dataset) Adapter LLM-Final Retention (%) Encoder not text-aligned Ultravox Lexical (LS) .279 .535 192 Speaker (LS) .605 .556 92 Emotion (CD) .621 .557 90 Speaker (CD) .196 .137 70 Acoustic (E50) .647 .581 90 Q2-Audio Lexical (LS) .242 .471 195 Speaker (LS) .961 .589 61 Emotion (CD) .874 .877 100 Speaker (CD) .816 .556 68 Acoustic (E50) .946 .965 102 Prism.-D Lexical (CO) .637 .664 104 Object cat. (CO) .792 .792 100 Super cat. (CO) .832 .839 101 Encoder text-aligned LLaVA Lexical (CO) .620 .669 108 Object cat. (CO) .770 .808 105 Super cat. (CO) .797 .842 106 Prism.-S Lexical (CO) .657 .663 101 Object cat. (CO) .804 .819 102 Super cat. (CO) .832 .851 102 Table 7: Information retention from adapter to LLM-final layer (probe accuracy ratio × \times 100). Retention > {>} 100% means the LLM amplifies the signal; < {<} 100% means degradation. Non-aligned encoders show selective amplification (lexical recovers, speaker degrades); text-aligned encoders retain or slightly improve all types. LS = LibriSpeech, CD = CREMA-D, E50 = ESC-50, CO = COCO.

[182] h3: B.8 Lipschitz constants and Wasserstein distances

[183] p: Table 8 reports the empirical Lipschitz constants and Wasserstein distances used to evaluate the bound in § 5.4 .

[184] figure: Model Dataset L log L_{\log} L log L_{\log} (p95) D D W 1 W_{\!1} L log ⋅ W 1 L_{\log}\cdot W_{\!1} Speech Ultravox LibriSpeech 9.08 14.58 10.3 17.8 162 CREMA-D 5.82 9.70 17.0 – – ESC-50 3.66 5.92 20.7 – – Q2-Audio LibriSpeech 0.49 0.67 122.2 38.9 19.1 CREMA-D 0.59 0.75 229.9 – – ESC-50 0.47 0.59 202.5 – – Vision LLaVA COCO 0.29 0.36 28.5 46.3 13.4 Prism.-D COCO 0.40 0.49 35.7 50.4 20.2 Prism.-S COCO 1.12 1.44 16.2 47.9 53.7 Table 8: Lipschitz constants ( L log L_{\log} , mean and p95 of gradient norm distribution), representation diameter ( D D ), Wasserstein-1 distance ( W 1 W_{\!1} at LLM layer 16), and their product. L log L_{\log} is content-dependent: it decreases as audio moves away from text (LibriSpeech > > CREMA-D > > ESC-50). L log ⋅ W 1 L_{\log}\cdot W_{\!1} is largest for Ultravox (162, strongest degradation) and smallest for LLaVA (13.4, no degradation). Prismatic-S has 2.8 × 2.8\times higher L log L_{\log} than Prismatic-D, consistent with the LLM being more responsive to text-aligned representations.

[185] h3: B.9 Audio-token-only pooling

[186] p: Our standard extraction mean-pools LLM-layer activations over all sequence positions (system prompt, audio tokens, assistant prompt). This could dilute the audio signal. Ultravox’s processor exposes the audio token boundaries ( audio_token_start_idx , audio_token_len ), letting us restrict pooling to audio positions only. We re-extracted LLM representations with audio-only pooling and re-ran probes to compare.

[187] p: Table 9 shows the result: audio-only pooling produces nearly identical probe accuracies across all datasets and information types, with all deltas within ± \pm 2.1% and most under 1%. Restricting to audio tokens does not help, and in several cases slightly hurts. This is because the LLM’s self-attention layers redistribute information across all sequence positions as they process the input. By layer 16, audio-derived information has spread to text prompt tokens as well. Pooling over the full sequence therefore captures more of the available signal, not less. This validates our use of full-sequence pooling throughout the paper: it is not a conservative approximation that dilutes the audio signal, but rather the appropriate strategy given how transformers distribute information.

[188] figure: Dataset Label All-token Audio-only Δ \Delta LLM hidden layer 16 LibriSpeech Speaker .637 ± \pm .026 .639 ± \pm .023 + + .002 LibriSpeech Lexical .591 ± \pm .009 .581 ± \pm .019 − - .011 CREMA-D Speaker .210 ± \pm .006 .213 ± \pm .009 + + .003 CREMA-D Lexical .999 ± \pm .001 .999 ± \pm .001 + + .000 CREMA-D Emotion .593 ± \pm .004 .595 ± \pm .006 + + .002 ESC-50 Sound .681 ± \pm .027 .677 ± \pm .031 − - .003 LLM final layer LibriSpeech Speaker .565 ± \pm .012 .544 ± \pm .020 − - .021 LibriSpeech Lexical .573 ± \pm .024 .559 ± \pm .023 − - .014 CREMA-D Speaker .140 ± \pm .009 .140 ± \pm .008 − - .000 CREMA-D Lexical .999 ± \pm .001 .999 ± \pm .001 − - .000 CREMA-D Emotion .556 ± \pm .008 .553 ± \pm .004 − - .004 ESC-50 Sound .613 ± \pm .016 .603 ± \pm .020 − - .011 Table 9: Probe accuracy with all-token vs. audio-only pooling at LLM layers (Ultravox). All deltas are within ± \pm 2.1%, most under 1%. Audio-only pooling does not improve probe accuracy. The LLM’s self-attention layers mix information across all sequence positions: by layer 16, audio-derived information has been redistributed to text prompt tokens as well. Restricting pooling to audio positions therefore discards information that the LLM has already spread across the full sequence, slightly reducing the available signal. This validates our use of full-sequence pooling throughout the paper.

[189] h2: Appendix C Additional figures

[190] figure: Figure 1: Probe accuracy trajectories for all five models. Rows 1–2: speech models (Ultravox, Qwen2-Audio) across LibriSpeech, CREMA-D, and ESC-50. Row 3: vision models (LLaVA, Prismatic-DINOv2, Prismatic-SigLIP) on COCO.

[191] figure: Figure 2: Mode alignment profiles for all five models. Blue: alignment score α ~ ​ ( u k ) \tilde{\alpha}(u_{k}) ; orange: eigenvalue spectrum λ k \lambda_{k} (log scale). The dominant eigenmodes are modality-specific ( α ~ ≈ 0 \tilde{\alpha}\approx 0 ) for all models with non-text-aligned encoders; for Prismatic-S (SigLIP, text-aligned), even Mode 0 is text-aligned ( α ~ = 0.83 \tilde{\alpha}=0.83 ).

[192] p: The Prismatic comparison (Table 10 ) isolates encoder text-alignment as the causal variable. Both VLMs share the same architecture, adapter, training recipe, and LLM backbone; only the vision encoder differs. SigLIP (text-aligned) shows consistent improvement through the LLM for all information types, while DINOv2 (not text-aligned) shows stagnation or minimal change for non-textual attributes.

[193] figure: Probe accuracy Encoder Info type Adapter LLM-final Δ LLM \Delta_{\text{LLM}} Text-describable attributes DINOv2 Lexical .637 .664 +4.2% Object cat. .792 .792 − - 0.0% Super cat. .832 .839 +0.8% SigLIP Lexical .657 .663 +0.9% Object cat. .804 .819 +1.9% Super cat. .832 .851 +2.3% Non-textual attributes DINOv2 Obj. count .594 .614 +3.4% Obj. size .679 .688 +1.3% Spatial spr. .465 .487 +4.7% SigLIP Obj. count .598 .647 +8.2% Obj. size .669 .699 +4.5% Spatial spr. .459 .481 +4.8% Table 10: Prismatic controlled comparison (full results). Δ LLM \Delta_{\text{LLM}} = change from adapter to LLM-final. Top: text-describable attributes (named in captions). Bottom: non-textual attributes (object count, average object size, spatial spread; derived from annotations, not captions). Text baseline accuracy is substantially lower (.415–.495) for non-textual attributes, confirming their visual nature. Same architecture, same LLM, only encoder differs.

[194] p: The mode alignment spectrum (Table 11 ) reveals which directions carry the mismatch. For each model, we decompose the adapter output covariance into eigenmodes and measure their text alignment. The dominant eigenmode is modality-specific ( α ~ ≪ 1 \tilde{\alpha}\ll 1 ) for all non-text-aligned encoders, while for SigLIP even the dominant mode is text-aligned ( α ~ = 0.83 \tilde{\alpha}=0.83 ).

[195] figure: Model Mode 0 α ~ \tilde{\alpha} Mean α ~ \tilde{\alpha} (top 10) MS modes MS var. Ultravox 0.001 1.76 11/100 63.6% Qwen2-Audio 0.010 7.21 5/100 97.6% LLaVA 0.013 3.94 9/100 71.9% Prismatic-D 0.034 0.087 53/100 71.0% Prismatic-S 0.827 1.95 14/100 24.6% Table 11: Mode alignment summary. MS modes = modes with α ~ < 0.5 \tilde{\alpha}<0.5 (modality-specific). MS var. = fraction of top-100 eigenmode variance in MS modes. Mode 0 is modality-specific ( α ~ ≪ 1 \tilde{\alpha}\ll 1 ) for all non-text-aligned encoders; for SigLIP (text-aligned), even Mode 0 is text-aligned ( α ~ = 0.83 \tilde{\alpha}=0.83 ). Extending to all 4096 modes strengthens the pattern: tail modes are overwhelmingly text-aligned with negligible individual variance, so the MS/TA split is driven by the high-variance modes reported here.

[196] h2: Appendix D Additional limitations

[197] p: Scope. We test speech and vision across five models. The framework applies to any multimodal LLM with a text-trained decoder, but video/3D remain untested.

[198] p: Assumption 1 (shared marginal). We assume P M ​ ( C , Y ) = P T ​ ( C , Y ) P_{\!M}(C,Y)=P_{\!T}(C,Y) . This holds when the multimodal model is trained on text-centric tasks (transcription, captioning). Violations add a marginal-shift term independent of representation geometry.

[199] p: Generality of the GMI constraint. The mechanism described in the main text is not architectural: any multimodal LLM whose decoder was trained under a text-dominated objective has a text-shaped scoring rule, regardless of whether the adapter is a linear projection, MLP, Q-Former, perceiver resampler, or discrete codebook. The GMI constraint applies to multimodal modelling in general: unless the training objective explicitly targets each modality, the decoder remains indifferent to non-text directions.

[200] h2: Instructions for reporting errors

[201] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[202] p: Tip: You can select the relevant text first, to include it in your report.

[203] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[204] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
