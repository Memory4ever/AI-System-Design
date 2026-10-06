[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Breaking Semantic-Aware Watermarks via LLM-Guided Coherence-Preserving Semantic Injection

[3] h6: Abstract.

[4] p: Generative images have proliferated on Web platforms in social media and online copyright distribution scenarios, and semantic watermarking has increasingly been integrated into diffusion models to support reliable provenance tracking and forgery prevention for web content. Traditional noise-layer-based watermarking, however, remains vulnerable to inversion attacks that can recover embedded signals. To mitigate this, recent content-aware semantic watermarking schemes bind watermark signals to high-level image semantics, constraining local edits that would otherwise disrupt global coherence. Yet, large language models (LLMs) possess structured reasoning capabilities that enable targeted exploration of semantic spaces, allowing locally fine-grained but globally coherent semantic alterations that invalidate such bindings. To expose this overlooked vulnerability, we introduce a Coherence-Preserving Semantic Injection (CSI) attack that leverages LLM-guided semantic manipulation under embedding-space similarity constraints. This alignment enforces visual-semantic consistency while selectively perturbing watermark-relevant semantics, ultimately inducing detector misclassification. Extensive empirical results show that CSI consistently outperforms prevailing attack baselines against content-aware semantic watermarking, revealing a fundamental security weakness of current semantic watermark designs when confronted with LLM-driven semantic perturbations.

[5] h6: Keywords:

[6] h2: 1. Introduction

[7] figure: Figure 1. The overall workflow of the proposed Coherence-Preserving Semantic Injection (CSI) attack.

[8] p: With the widespread adoption of diffusion-based generative models across the Web ecosystem, AI-generated images have become increasingly pervasive on social media platforms and ever harder to distinguish from real photographs ( Yang et al., 2023b ) , making content authenticity and copyright traceability increasingly crucial. Pixel-level watermarking provides a direct mechanism for provenance, but it faces a fundamental trade-off between visual fidelity and robustness, as watermarks are easily degraded by compression, filtering, and other transformations during online dissemination. To mitigate this, semantic watermarking embeds information into the diffusion noise rather than visible pixels, e.g., Tree-Ring Watermark, Gaussian Shading, and WIND, which encode signals in the initial (or latent) noise following the model’s generative prior and recover them via approximate inversion of the diffusion process ( Wen et al., 2023 ; Yang et al., 2024 ; Arabi et al., 2024 ) . By embedding the watermark in semantic noise, these methods typically preserve perceptual quality while achieving strong robustness to common perturbations, making them promising candidates.

[9] p: However, these semantic watermarking methods share a key vulnerability: they embed watermark signals mainly in the initial latent noise with weak semantic alignment, which we refer to as Content-independent Semantic Watermarks (CIW). Exploiting this weakness, Müller et al. show that a single watermarked image suffices to recover the watermark and generate arbitrary content with forged marks ( Müller et al., 2025 ) . To mitigate this, Arabi et al. propose Semantic-Aware Image Watermarking (SEAL) ( Arabi et al., 2025 ) , a Content-aware Semantic Watermark (CSW) scheme that conditions verification on image semantics rather than noise alone and tightly couples inverted noise with visual content, forcing attackers to preserve semantic consistency and making effective forgeries substantially harder.

[10] p: In other words, attacking such watermarks essentially requires solving a multi-constrained semantic optimization problem in a discrete prompt space: the attacker must preserve the coherence between the primary visual semantics and the noise semantics while injecting adversarial attributes to alter local semantics. Coincidentally, recent studies show that LLMs can not only automate combinatorial optimization tasks requiring strict constraint definitions, but also heuristically search for optimal semantic solutions in discrete prompt spaces ( Yang et al., 2023a ; Zhang and Luo, 2025 ) . This emerging capability indicates that the original security assumptions are fundamentally flawed.

[11] p: Based on the above insight, we propose (contribution i) : a Coherence-Preserving Semantic Injection (CSI) attack, which uses Adversarial Semantic Injection via Semantically Coherent Manipulations (ASI) combined with a Consistency-Based Hierarchical Filtering (CHF) mechanism to ensure successful semantic alteration while maintaining positive watermark detection.

[12] p: To the best of our knowledge, CSI is the first systematic attack against CSW such as SEAL. (contribution ii) : Our experiments reveal that even state-of-the-art CSW cannot withstand CSI, underscoring a critical security gap and highlighting the urgent need for more robust, hierarchical watermarking mechanisms capable of defending against semantic-level adversarial attacks.

[13] h2: 2. Method: Coherence-Preserving Semantic Injection

[14] p: In this section, we introduce our method: Coherence-Preserving Semantic Injection (CSI), as illustrated in Figure 1 . We first define some useful notations. Let 𝐱 0 \mathbf{x}_{0} be the semantic-aware watermarked image, and 𝐭 0 = BLIP ⁡ ( 𝐱 0 ) \mathbf{t}_{0}=\mathrm{BLIP}(\mathbf{x}_{0}) be the associated semantic with it generated by BLIP model. We use { ϵ t } t = 1 T \{\epsilon_{t}\}_{t=1}^{T} to denote the noise schedule of the stable diffusion. Let 𝒢 \mathcal{G} denote the set of global semantic anchors (e.g., subjects/main objects), and 𝒜 \mathcal{A} the local attribute to manipulate. We denote by Π 𝒢 \Pi_{\mathcal{G}} the mask operator that keeps only anchor tokens, and by a ⋆ a^{\star} the target attribute specified by the attack intent I I . Let ϕ img \phi_{\mathrm{img}} , ϕ text \phi_{\mathrm{text}} , and ϕ noise \phi_{\mathrm{noise}} be the normalized image, text, and noise encoders, respectively. Thus ⟨ ⋅ , ⋅ ⟩ \langle\cdot,\cdot\rangle is the cosine similarity in the unit sphere.

[15] h3: 2.1. Adversarial Semantic Injection via Semantically Coherent Manipulations (ASI)

[16] p: Conceptual objective. We seek a modified prompt 𝐭 ′ \mathbf{t}^{\prime} that (i) preserves global anchors and (ii) injects the target attribute, while (iii) allowing diffusion regeneration that matches CSW noise semantics:

[17] table: 𝐭 ′ ∈ arg ⁡ min 𝐭 \displaystyle\mathbf{t}^{\prime}\in~\arg\min_{\mathbf{t}}~ λ anc ​ ℒ anc ​ ( 𝐭 , 𝐭 0 ) − λ attr ​ 𝒮 attr ​ ( 𝐭 , a ⋆ ) \displaystyle\lambda_{\mathrm{anc}}\,\mathcal{L}_{\mathrm{anc}}(\mathbf{t},\mathbf{t}_{0})-\lambda_{\mathrm{attr}}\,\mathcal{S}_{\mathrm{attr}}(\mathbf{t},a^{\star}) (1) s.t. 𝐱 ′ = SD ​ _ ​ regen ​ ( 𝐳 T , 𝐭 , { ϵ t } t = 1 T ) \displaystyle\mathbf{x}^{\prime}=\mathrm{SD\_regen}(\mathbf{z}_{T},\mathbf{t},\{\epsilon_{t}\}_{t=1}^{T}) s csw ​ ( 𝐱 ′ , { ϵ t } t = 1 T ) ≥ τ csw \displaystyle s_{\mathrm{csw}}(\mathbf{x}^{\prime},\{\epsilon_{t}\}_{t=1}^{T})\geq\tau_{\mathrm{csw}}

[18] p: where the anchor-preservation loss ℒ anc \mathcal{L}_{\mathrm{anc}} penalizes deviation on anchor tokens, the attribute-injection score 𝒮 attr \mathcal{S}_{\mathrm{attr}} rewards the presence of the target attribute, and the constraints are defined below.

[19] p: Regeneration with copied noise. We use DDIM inversion and noise copying to save the watermark-consistent noise semantics:

[20] table: (2) 𝐳 T = DDIM ​ _ ​ inv ​ ( 𝐱 0 ) , { ϵ t } t = 1 T = CSW ​ _ ​ Noise ​ ( 𝐱 0 ) . \mathbf{z}_{T}=\mathrm{DDIM\_inv}(\mathbf{x}_{0}),\qquad\{\epsilon_{t}\}_{t=1}^{T}=\mathrm{CSW\_Noise}(\mathbf{x}_{0}).

[21] p: Given any candidate prompt 𝐭 \mathbf{t} , the image 𝐱 ′ \mathbf{x}^{\prime} is regenerated as:

[22] table: (3) 𝐱 ′ = SD ​ _ ​ regen ​ ( 𝐳 T , 𝐭 , { ϵ t } t = 1 T ) . \mathbf{x}^{\prime}=\mathrm{SD\_regen}\left(\mathbf{z}_{T},\mathbf{t},\{\epsilon_{t}\}_{t=1}^{T}\right).

[23] p: We define the CSW score to quantify the semantic alignment between the image and the noise:

[24] table: (4) s csw ​ ( 𝐱 , { ϵ t } ) \displaystyle s_{\mathrm{csw}}(\mathbf{x},\{\epsilon_{t}\}) = ⟨ ϕ img ​ ( 𝐱 ) , ϕ noise ​ ( { ϵ t } t = 1 T ) ⟩ . \displaystyle=\left\langle\phi_{\mathrm{img}}(\mathbf{x}),\phi_{\mathrm{noise}}(\{\epsilon_{t}\}_{t=1}^{T})\right\rangle.

[25] figure: Table 1. Comparison of different attacks under each detector (ASR %↑). Detector (ASR a % ↑) LFA ( Jain et al., 2025 ) RPM ( Arabi et al., 2025 ) CSI (Ours) Content-independent semantic watermarks Gaussian Shading ( Yang et al., 2024 ) 100 100 100 Tree-Ring ( Wen et al., 2023 ) 93.81 100 100 WIND ( Arabi et al., 2024 ) 100 100 100 Content-aware semantic watermark SEAL ( Arabi et al., 2025 ) 0 7 81 Mean ↑ 73.45 76.75 95.25 a ASR = proportion of tampered images still detected as “watermark present” under the threshold.

[26] p: Approximate optimization by LLM. Since directly optimizing the conceptual objective ( 1 ) over discrete tokens under complex constraints is unstable and intractable, motivated by ( Yang et al., 2023a ; Zhang and Luo, 2025 ) , we adopt an optimization-by-prompting approach. We treat the LLM as a black-box proposer and craft a meta-prompt that specifies the objective and constraints in natural language. Conditioned on ( 𝐱 0 , 𝐭 0 , 𝒢 , I ) (\mathbf{x}_{0},\mathbf{t}_{0},\mathcal{G},I) , the LLM generates a batch of semantically coherent prompt candidates, which we then filter to enforce anchor preservation and attribute injection. Hence it prevents prompt collapse while preserving grammaticality. During regeneration, we reuse the copied CSW noise so that any change in detector acceptance can be attributed to semantic edits rather than stochasticity.

[27] h3: 2.2. Consistency-Based Hierarchical Filtering (CHF)

[28] p: The LLM optimizer yields a pool 𝒫 \mathcal{P} of minimally edited prompts. We now filter 𝒫 \mathcal{P} by progressively stronger tests that are (i) cheap and text-only, then (ii) visual alignment and CSW-aware. Define the following acceptance sets for thresholds τ = ( τ text , τ vis , τ csw ) \tau=(\tau_{\mathrm{text}},\tau_{\mathrm{vis}},\tau_{\mathrm{csw}}) :

[29] p: Textual Semantic Filtering. We first remove candidates that drift from the global anchors using a text-only check:

[30] table: (5) s text ​ ( 𝐭 i ′ ) = ⟨ ϕ text ​ ( Π 𝒢 ​ 𝐭 0 ) , ϕ text ​ ( Π 𝒢 ​ 𝐭 i ′ ) ⟩ . \displaystyle s_{\mathrm{text}}(\mathbf{t}^{\prime}_{i})=\left\langle\phi_{\mathrm{text}}(\Pi_{\mathcal{G}}\mathbf{t}_{0}),\,\phi_{\mathrm{text}}(\Pi_{\mathcal{G}}\mathbf{t}^{\prime}_{i})\right\rangle.

[31] p: Candidates that preserve anchors form

[32] table: (6) 𝒞 = { 𝐭 i ′ ∈ 𝒫 : s text ​ ( 𝐭 i ′ ) ≥ τ text } . \displaystyle\mathcal{C}=\{\mathbf{t}^{\prime}_{i}\in\mathcal{P}:s_{\mathrm{text}}(\mathbf{t}^{\prime}_{i})\geq\tau_{\mathrm{text}}\}.

[33] p: Visual Anchor Filtering. For each 𝐭 i ′ ∈ 𝒞 \mathbf{t}^{\prime}_{i}\in\mathcal{C} , we regenerate an image 𝐱 i ′ \mathbf{x}^{\prime}_{i} with the copied CSW noise to neutralize sampling randomness, and use BLIP to get its caption 𝐭 i VF = BLIP ⁡ ( 𝐱 i ′ ) . \mathbf{t}^{\mathrm{VF}}_{i}=\mathrm{BLIP}(\mathbf{x}^{\prime}_{i}). We then compute the visual-anchor alignment, which reflects whether the anchors preserved in the image:

[34] table: (7) s vis ​ ( 𝐭 i VF ) = ⟨ ϕ text ​ ( Π 𝒢 ​ 𝐭 0 ) , ϕ text ​ ( Π 𝒢 ​ 𝐭 i VF ) ⟩ \displaystyle s_{\mathrm{vis}}(\mathbf{t}^{\mathrm{VF}}_{i})=\left\langle\phi_{\mathrm{text}}(\Pi_{\mathcal{G}}\mathbf{t}_{0}),\phi_{\mathrm{text}}(\Pi_{\mathcal{G}}\mathbf{t}^{\mathrm{VF}}_{i})\right\rangle

[35] p: Finally, we impose CSW semantic matching between the regenerated image and the copied noise schedule via the discrepancy:

[36] table: (8) Δ csw ​ ( 𝐱 i ′ ) = 1 − ⟨ ϕ img ​ ( 𝐱 i ′ ) , ϕ noise ​ ( { ϵ t } t = 1 T ) ⟩ . \displaystyle\Delta_{\mathrm{csw}}(\mathbf{x}^{\prime}_{i})=1-\left\langle\phi_{\mathrm{img}}(\mathbf{x}_{i}^{\prime}),\phi_{\mathrm{noise}}(\{\epsilon_{t}\}_{t=1}^{T})\right\rangle.

[37] p: The final set of attack images is

[38] table: (9) 𝒳 attack = { 𝐱 i ′ : 𝐭 i ′ ∈ 𝒞 , s vis ( 𝐭 i ′ ) ≥ τ vis , Δ csw ( 𝐱 i ′ ) ≤ τ csw } . \displaystyle\mathcal{X}_{\mathrm{attack}}=\left\{\mathbf{x}^{\prime}_{i}:\mathbf{t}^{\prime}_{i}\in\mathcal{C},s_{\mathrm{vis}}(\mathbf{t}^{\prime}_{i})\geq\tau_{\mathrm{vis}},\Delta_{\mathrm{csw}}(\mathbf{x}^{\prime}_{i})\leq\tau_{\mathrm{csw}}\right\}.

[39] h2: 3. Experiments

[40] p: In this experiment, We employ the Stable Diffusion V2 model as the generation model. The evaluation prompts are sourced from the publicly Stable-Diffusion-Prompts dataset ( Santana, 2024 ) , and we use GPT-4o-mini as the large language model.

[41] p: Attack baseline : We compare our attack method with the semantic attacks prevalent in literature, including Regeneration with the Private Model (RPM) ( Arabi et al., 2025 ) and Latent Forgery Attack (LFA) ( Jain et al., 2025 ) .

[42] p: Semantic watermark baseline : We select four semantic watermark techniques for defense, including Semantic Aware Image Watermark (SEAL) ( Arabi et al., 2025 ) , Gaussian Shading Watermark (GSW) ( Yang et al., 2024 ) , Tree-Ring Watermark (TRW) ( Wen et al., 2023 ) and WIND ( Arabi et al., 2024 ) .

[43] h3: 3.1. Comparative Attack Effectiveness

[44] p: To evaluate the effectiveness of our attack, we conduct comparative experiments involving multiple semantic attacks under various semantic watermark defenses. We use the attack success rate (ASR) ↑ \uparrow , defined as the proportion of tampered images still detected as watermark present under the threshold, as the evaluation metric. The experimental results are shown in Table 1 .

[45] p: From Table 1 , we observe that our method, along with the two baseline attacks, achieves nearly 100% ASR against the GSW, TRW, and WIND semantic watermarks. This suggests that these watermarking schemes are highly vulnerable to semantic attacks and can be easily compromised. However, under the protection of the content-aware semantic watermarking method SEAL, RPM and LFA fail almost entirely, achieving only 7% and 0% ASR, respectively. In contrast, our method still achieves an impressive 81% ASR, clearly demonstrating its robustness and effectiveness in bypassing even advanced semantic watermark defenses.

[46] figure: Figure 2. Further Analysis of Detection Metrics

[47] h3: 3.2. Attack Robustness Across Different Watermarking Schemes

[48] p: To quantify the vulnerability of existing semantic watermark detectors to our attack, we measure, for each scheme, its core detection statistic and compare it against the official decision threshold. We further report the corresponding evasion success rate, numerical safety margin, and worst-case deviation, thereby establishing a consistent and verifiable basis for evaluating attack effectiveness across different watermarking mechanisms. We detail the evaluation of four representative schemes below:

[49] p: TRW , which detects forgeries by measuring the L1 distance between reconstructed and reference noise patterns. The attacked images yields an average distance of only 47.42 in our attack (Figure 2 a), far below its detection threshold. Even the maximum value reaches merely 57.63, maintaining a clear safety margin of 19.37.

[50] p: SEAL , which enforces semantic consistency by comparing the number of matching patches between the inverted noise 𝐳 inv \mathbf{z}^{\text{inv}} and the regenerated reference 𝐳 ~ \tilde{\mathbf{z}} . Our method attains an average match count of 134.8 (Figure 2 b), with even the lowest case reaching 72, far exceeding the threshold of 12.

[51] p: GSW , which verifies authenticity by decoding a K K -bit watermark sequence s ​ ’ s\textquoteright from the inverted initial noise and comparing it with the original s s . Our method achieves a perfect matching score of 1.00 (Figure 2 c), well above the detection threshold of 0.71.

[52] p: WINE , which authenticates images by matching the reconstructed noise against a secret noise pattern. Our method consistently produces exact matches across all attacked samples, indicating complete evasion of detection.

[53] p: Overall, the results confirm that our attack consistently lowers the measured detection scores across all other schemes, demonstrating robust evasion capability under diverse detector.

[54] h3: 3.3. Attack Effectiveness on Content-aware Watermarking

[55] p: To evaluate our attack against content-aware semantic watermarking, we examine whether it disrupts the core detection criterion: semantic consistency between the image and its prompt. This consistency is defined as the similarity of their semantic representations. At the set level, this reflects distribution alignment in high-level semantic feature space: if the tampered set matches the original distribution, global semantics are preserved, potentially bypassing detection. We quantify this using Fréchet Inception Distance (FID) ( Heusel et al., 2018 ) , which compares the means and covariances of image sets to capture semantic distribution differences.

[56] p: Based on this, we conduct semantic consistency experiments to assess the impact of LLM-based semantic constraints on preserving semantics after tampering. We compare our method (Ours, LLM-constrained) against two baselines: RPM (unconstrained regeneration) and SEAL (watermarked and unaltered). The reported FID values are computed between the generated images and the original image set. The results are illustrated in Figure 2 (d).

[57] p: Results show that RPM exhibits an FID of 235.40, indicating substantial semantic drift and confirming that unconstrained regeneration severely disrupts the original semantic distribution. In contrast, Ours achieves an FID of 178.75, an absolute reduction of 56.65 (↓24.1%) compared to RPM, and approaches SEAL’s 164.27. Importantly, in this setting, the goal is not to minimize FID arbitrarily but to align as closely as possible with SEAL, as this reflects successful semantic preservation while performing the attack. It demonstrates that LLM semantic constraints significantly mitigate semantic drift and enable tampering without deviating from the watermark’s content-aware semantic structure, validating their critical role in bypassing content-aware semantic watermark detection.

[58] h2: 4. Conclusion

[59] p: Our findings indicate that even content-aware semantic watermarking schemes such as SEAL remain vulnerable to LLM-guided semantic attacks. To validate this vulnerability, we propose the CSI framework, demonstrating that LLMs can systematically compromise watermark integrity within the discrete semantic space. These findings highlight a critical security gap and the need for future watermark designs to defend against semantic-level attacks.

[60] h2: References

[61] h2: Instructions for reporting errors

[62] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[63] p: Tip: You can select the relevant text first, to include it in your report.

[64] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[65] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
