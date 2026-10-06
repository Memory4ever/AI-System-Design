[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: HulluEdit: Single-Pass Evidence-Consistent Subspace Editing for Mitigating Hallucinations in Large Vision-Language Models

[3] h6: Abstract

[4] p: Object hallucination in Large Vision-Language Models (LVLMs) significantly hinders their reliable deployment. Existing methods struggle to balance efficiency and accuracy: they often require expensive reference models and multiple forward passes, or apply static edits that risk suppressing genuine visual evidence. To address this, we introduce HulluEdit , a single-pass, reference-free intervention framework. Our core innovation is orthogonal subspace editing : we decompose the hidden states of the model into orthogonal subspaces—visual evidence, conflicting priors, and residual uncertainty—enabling selective suppression of hallucinatory patterns without interfering with visual grounding. This approach mathematically guarantees that edits applied to the prior subspace leave the visual component entirely unaffected. Extensive experiments show that HulluEdit achieves state-of-the-art hallucination reduction on benchmarks including POPE and CHAIR across diverse architectures, while preserving general capabilities on MME and maintaining efficient inference. Our method consistently outperforms contrastive decoding and static subspace editing baselines, offering a new pathway toward more trustworthy LVLMs. Code is released at https://github.com/VioAgnes/HulluEdit .

[5] p: † {\dagger} Corresponding author.

[6] figure: (a) Traditional LVLM with hallucinations (b) HulluEdit (ours) Figure 1 : Comparison of (a) traditional LVLMs prone to object hallucinations versus (b) our HulluEdit method that mitigates hallucinations via orthogonal subspace decomposition.

[7] h2: 1 Introduction

[8] p: Large Vision-Language Models (LVLMs) [ 13 , 30 , 16 , 1 , 2 ] have become the standard foundation models for image captioning, visual question answering, and assistive interaction. However, they remain vulnerable to object hallucination — the phenomenon of stating non-existent objects, attributes, or quantities when provided with an image [ 20 , 15 , 17 ] . As illustrated in Figure 1(a) , such hallucinations often arise when strong language priors override weak or ambiguous visual evidence, leading to a misalignment between the generated text and the actual image content.

[9] p: To mitigate these hallucinations, researchers have proposed several strategies in recent years. Contrastive Decoding methods [ 14 , 18 , 5 , 24 , 12 ] achieve promising results by comparing output distributions, but often require a reference model or secondary inference, increasing latency and engineering complexity. Meanwhile, Static Subspace Editing techniques [ 26 , 31 ] construct dataset-level hallucination subspaces offline, but lack token-level adaptability and risk suppressing genuine visual evidence. Ultimately, as illustrated in Figure 1(a) , these methods lack reliable decoupling mechanisms and fine-grained control between suppressing linguistic priors and preserving visual evidence.

[10] p: Inspired by DeCo [ 23 ] , we observe that representations from mid-layers of large models can serve as reliable references for calibrating the output layer. This motivates us to leverage intermediate layers for constructing sample-level subspace structures, enabling more refined and adaptive control over the evidence–prior competition. By further applying orthogonal decomposition to decouple priors from visual evidence, we can effectively suppress prior conflicts while preserving robust visual grounding.

[11] p: Based on this insight, we propose HulluEdit , a single-pass subspace editing framework that decomposes hidden states into orthogonal components: an online-estimated Visual Evidence Subspace and an Anti-Prior Subspace in its orthogonal complement. As illustrated in Figure 1(b) , we construct a sample-adaptive visual subspace via weighted SVD and characterize the anti-prior direction from a non-visual text cache. We then project hidden states onto these subspaces and perform component-wise editing, suppressing only the anti-prior components without interfering with visual evidence. Orthogonality guarantees that prior suppression does not damage visual grounding. The method requires no additional training, no secondary forward pass, and edits hidden states before the output layer logits, maintaining low overhead and ease of use.

[12] p: Our main contributions are summarized as follows:

[13] p: Orthogonal evidence–prior decomposition: We propose a novel subspace construction method that estimates a sample-adaptive visual evidence subspace via weighted SVD and builds an orthogonal anti-prior subspace in its complement, guaranteeing no interference between visual preservation and prior suppression.

[14] p: Certificate-aware adaptive editing: We introduce a closed-form editing mechanism with adaptive strengths based on visual and prior conflict ratios, ensuring evidence-consistent edits that selectively suppress hallucinations while maintaining visual fidelity.

[15] p: Efficient single-pass inference: HulluEdit operates entirely online during decoding, requiring no reference models, additional forward passes, or parameter updates. It generalizes across multiple LVLM architectures with minimal overhead, significantly reducing hallucination rates on benchmarks like POPE and CHAIR while preserving caption quality and general performance on MME.

[16] h2: 2 Related Work

[17] h3: 2.1 LVLMs and Visual Hallucinations

[18] p: Large Vision-Language Models (LVLMs) extend the capabilities of large language models [ 22 , 25 , 4 , 11 , 21 , 7 ] to multimodal scenarios [ 13 , 30 , 16 , 6 , 1 , 19 , 2 ] . Architecturally, LVLMs can be broadly categorized into two paradigms: adapter-based systems (e.g., BLIP-2, MiniGPT-4, LLaVA, InstructBLIP [ 13 , 30 , 16 , 6 ] ), which map visual tokens into the language space via lightweight adapters, and deep-fusion designs (e.g., Flamingo, Kosmos-2, Qwen-VL [ 1 , 19 , 2 ] ), which employ interleaved vision-language attention mechanisms for tighter modal integration. Despite these architectural differences, object hallucination —wherein models generate fluent descriptions about non-existent objects, attributes, quantities, or relationships given an image [ 20 , 17 , 15 , 9 ] —remains a fundamental challenge pervasive across LVLMs.

[19] h3: 2.2 Hallucination Mitigation Methods

[20] p: Existing approaches for mitigating visual hallucinations in LVLMs can be broadly categorized into three groups. Training-stage methods, such as instruction tuning and visual preference alignment [ 16 , 6 ] , enhance model usability but often fail to fully resolve the inherent tension between perceptual evidence and linguistic priors during inference. Decoding-stage methods, including contrastive decoding and its variants, aim to improve factuality by amplifying discrepancies between confident and uncertain model outputs—for instance, VCD [ 12 ] strengthens visual signals while suppressing interfering priors, and DoLa [ 5 ] modulates deeper layer activations to reduce reliance on shallow semantics. However, these approaches may inadvertently weaken authentic visual cues. Dynamic Null-space Decoding [ 23 ] further refines this idea by calibrating logits with layer-wise visual information, though its editing granularity remains relatively coarse. Subspace editing methods, such as Nullu [ 26 ] , construct dataset-level hallucination subspaces via offline global projection. Yet, these techniques are generally static , require pre-trained subspaces, lack token-level adaptability, and risk suppressing legitimate visual content. In contrast, our work introduces a dynamic, single-pass subspace editing framework that performs online orthogonal decomposition with theoretical guarantees, enabling sample-aware intervention without compromising visual grounding.

[21] figure: Figure 2 : Overview of HalluEdit. We estimate a visual subspace U U from weighted visual tokens, an orthogonal anti -prior subspace P P from the text cache, and retain the residual subspace R R as uncertainty that is softly regularized when editing h h .

[22] h2: 3 Method

[23] p: Our proposed HalluEdit framework operates as a single-pass, reference-free subspace editing mechanism that mitigates visual hallucinations in Large Vision-Language Models (LVLMs) by decomposing and selectively manipulating hidden representations. As illustrated in Figure 2 , the core innovation lies in constructing orthogonal subspaces that separately capture visual evidence and conflicting linguistic priors, enabling targeted interventions without compromising visual grounding.

[24] p: The framework follows a principled three-stage pipeline: First, we extract visual features from an anchor transformer layer and maintain a dynamic text cache throughout decoding. Second, we perform online estimation of a context-aware visual evidence subspace U U via weighted SVD, while constructing an orthogonal anti-prior subspace P P from the text cache within the visual complement. Third, at the final transformer layer, we decompose each hidden state h h into three orthogonal components— h U h_{U} , h P h_{P} , and h R h_{R} —and apply certificate-aware adaptive editing that preserves visual evidence while selectively suppressing conflicting priors and regularizing residual uncertainty.

[25] h3: 3.1 Orthogonal Subspace Construction

[26] h4: 3.1.1 Layer Architecture and Feature Extraction

[27] p: We establish a two-layer processing architecture to balance feature stability and editing effectiveness. Based on empirical observations that object evidence concentrates in mid-layer representations [ 23 ] , we designate an anchor layer l a l_{a} (e.g., layer 26 in LLaVA) for stable feature extraction and an edit layer l e l_{e} for intervention application. This separation ensures robust visual feature capture while allowing edits at a point where linguistic and visual information are sufficiently integrated.

[28] p: The visual feature matrix V ∈ ℝ n v × d V\in\mathbb{R}^{n_{v}\times d} is extracted once per image from the anchor layer and cached throughout decoding, where n v n_{v} denotes the number of visual tokens and d d the hidden dimension. Concurrently, we maintain a dynamic text cache T ∈ ℝ n t × d T\in\mathbb{R}^{n_{t}\times d} that aggregates non-visual hidden states from previous decoding steps using a sliding window strategy, capturing evolving linguistic patterns that may conflict with visual evidence.

[29] h4: 3.1.2 Context-Aware Visual Evidence Subspace

[30] p: Visual relevance varies dynamically across generation steps, necessitating adaptive subspace estimation. Given the current hidden state h ∈ ℝ d h\in\mathbb{R}^{d} from the edit layer, we compute token-wise relevance weights through normalized cosine similarity:

[31] table: w i = softmax i ⁡ ( v i ⊤ ​ h ‖ v i ‖ 2 ​ ‖ h ‖ 2 + ϵ ) w_{i}=\operatorname{softmax}_{i}\left(\frac{v_{i}^{\top}h}{\|v_{i}\|_{2}\|h\|_{2}+\epsilon}\right) (1)

[32] p: where ϵ > 0 \epsilon>0 is a small constant for numerical stability. This weighting scheme emphasizes visual tokens most semantically aligned with the current generation context.

[33] p: The weighted visual matrix then undergoes truncated singular value decomposition to extract the principal visual components:

[34] table: U , Σ , V ⊤ = SVD ( W 1 / 2 V ) , U = U [ : , 1 : r ] U,\Sigma,V^{\top}=\mathrm{SVD}(W^{1/2}V),\quad U=U_{[:,1:r]} (2)

[35] p: where W = diag ⁡ ( w ) ∈ ℝ n v × n v W=\mathrm{diag}(w)\in\mathbb{R}^{n_{v}\times n_{v}} , and SVD ⁡ ( ⋅ ) \mathrm{SVD}(\cdot) returns the full SVD decomposition. We retain only the first r r left singular vectors U ∈ ℝ d × r U\in\mathbb{R}^{d\times r} , which form an orthonormal basis ( U ⊤ ​ U = I r U^{\top}U=I_{r} ) for the visual evidence subspace. This formulation follows weighted PCA principles, with W 1 / 2 W^{1/2} ensuring proper integration of relevance weights into the covariance structure.

[36] h4: 3.1.3 Conflict-Aware Anti-Prior Subspace

[37] p: To isolate and suppress conflicting linguistic patterns without compromising visual evidence, we construct the anti-prior subspace exclusively within the orthogonal complement of the visual evidence subspace. This critical design choice ensures spatial separation between visual and prior components:

[38] table: T ~ = T ⁡ ( I d − U ​ U ⊤ ) , P = SVD q ​ ( T ~ ) \tilde{T}=T(I_{d}-UU^{\top}),\quad P=\mathrm{SVD}_{q}(\tilde{T}) (3)

[39] p: where SVD q ​ ( ⋅ ) \mathrm{SVD}_{q}(\cdot) computes the top- q q left singular vectors of the projected text cache T ~ ∈ ℝ n t × d \tilde{T}\in\mathbb{R}^{n_{t}\times d} , yielding P ∈ ℝ d × q P\in\mathbb{R}^{d\times q} . Here, r r and q q denote the dimensionality of the visual evidence and anti-prior subspaces, respectively. The orthogonality constraint U ⊤ ​ P = 0 U^{\top}P=0 is enforced by construction, guaranteeing that any suppression applied along P P leaves the visual component h U = U ​ U ⊤ ​ h h_{U}=UU^{\top}h completely unaffected.

[40] h4: 3.1.4 Uncertainty-Aware Residual Subspace

[41] p: We complete the orthogonal decomposition by defining the residual projection matrix:

[42] table: Π R = I d − Π U − Π P \Pi_{R}=I_{d}-\Pi_{U}-\Pi_{P} (4)

[43] p: where Π U = U ​ U ⊤ \Pi_{U}=UU^{\top} and Π P = P ​ P ⊤ \Pi_{P}=PP^{\top} are the visual and anti-prior projectors respectively. This residual projector Π R \Pi_{R} captures components orthogonal to both U U and P P , representing ambiguous contextual information that cannot be clearly classified as visual evidence or conflicting priors. The complete hidden state decomposition satisfies:

[44] table: h = Π U ​ h ⏟ h U + Π P ​ h ⏟ h P + Π R ​ h ⏟ h R h=\underbrace{\Pi_{U}h}_{h_{U}}+\underbrace{\Pi_{P}h}_{h_{P}}+\underbrace{\Pi_{R}h}_{h_{R}} (5)

[45] p: with ‖ h ‖ 2 2 = ‖ h U ‖ 2 2 + ‖ h P ‖ 2 2 + ‖ h R ‖ 2 2 \|h\|_{2}^{2}=\|h_{U}\|_{2}^{2}+\|h_{P}\|_{2}^{2}+\|h_{R}\|_{2}^{2} due to orthogonality. The residual component h R h_{R} encompasses generic linguistic structures, uncertain visual cues, and compositional semantics that require conservative regularization to prevent over-suppression while maintaining generation fluency.

[46] h3: 3.2 Adaptive Subspace Editing

[47] h4: 3.2.1 Orthogonal State Decomposition

[48] p: For each hidden state h ∈ ℝ d h\in\mathbb{R}^{d} at the edit layer, we compute its orthogonal projections onto the three mutually exclusive subspaces:

[49] table: h U \displaystyle h_{U} = Π U ​ h = U ​ U ⊤ ​ h \displaystyle=\Pi_{U}h=UU^{\top}h\quad (6) h P \displaystyle h_{P} = Π P ​ h = P ​ P ⊤ ​ h \displaystyle=\Pi_{P}h=PP^{\top}h\quad (7) h R \displaystyle h_{R} = Π R ​ h \displaystyle=\Pi_{R}h\quad (8)

[50] p: where Π U , Π P , Π R \Pi_{U},\Pi_{P},\Pi_{R} denote the orthogonal projectors satisfying Π U + Π P + Π R = I d \Pi_{U}+\Pi_{P}+\Pi_{R}=I_{d} . The orthogonality constraints Π U ​ Π P = Π U ​ Π R = Π P ​ Π R = 0 \Pi_{U}\Pi_{P}=\Pi_{U}\Pi_{R}=\Pi_{P}\Pi_{R}=0 ensure the decomposition exhibits the energy-preserving property:

[51] table: h = h U + h P + h R h=h_{U}+h_{P}+h_{R} (9)

[52] table: ‖ h ‖ 2 2 = ‖ h U ‖ 2 2 + ‖ h P ‖ 2 2 + ‖ h R ‖ 2 2 \|h\|_{2}^{2}=\|h_{U}\|_{2}^{2}+\|h_{P}\|_{2}^{2}+\|h_{R}\|_{2}^{2} (10)

[53] p: This mathematical foundation enables independent manipulation of each component without cross-interference, as guaranteed by the orthogonality of the underlying subspaces.

[54] h4: 3.2.2 Evidence-Aware Strength Scheduling

[55] p: We dynamically calibrate editing intensities based on the relative dominance of visual evidence versus conflicting priors, quantified by two certificate metrics:

[56] table: VCR ⁡ ( h ) = ‖ h U ‖ 2 2 ‖ h ‖ 2 2 + ϵ , PCR ⁡ ( h ) = ‖ h P ‖ 2 2 ‖ h ‖ 2 2 + ϵ \mathrm{VCR}(h)=\frac{\|h_{U}\|_{2}^{2}}{\|h\|_{2}^{2}+\epsilon},\quad\mathrm{PCR}(h)=\frac{\|h_{P}\|_{2}^{2}}{\|h\|_{2}^{2}+\epsilon} (11)

[57] p: where ϵ = 10 − 8 \epsilon=10^{-8} ensures numerical stability. The Visual Certainty Ratio (VCR) measures the prominence of visual evidence, while the Prior Conflict Ratio (PCR) quantifies the strength of conflicting linguistic patterns.

[58] p: The adaptive editing strengths employ inverse-proportional scheduling to achieve balanced intervention:

[59] table: λ n ​ ( h ) = min ⁡ ( κ ⋅ 1 − VCR ⁡ ( h ) VCR ⁡ ( h ) + ϵ , λ max ) \lambda_{n}(h)=\min\left(\kappa\cdot\frac{1-\mathrm{VCR}(h)}{\mathrm{VCR}(h)+\epsilon},\ \lambda_{\max}\right) (12)

[60] table: λ p ​ ( h ) = min ⁡ ( λ 0 ⋅ PCR ⁡ ( h ) 1 − PCR ⁡ ( h ) + ϵ , λ max ) \lambda_{p}(h)=\min\left(\lambda_{0}\cdot\frac{\mathrm{PCR}(h)}{1-\mathrm{PCR}(h)+\epsilon},\ \lambda_{\max}\right) (13)

[61] p: where κ > 0 \kappa>0 and λ 0 > 0 \lambda_{0}>0 are tunable base strengths, and λ max \lambda_{\max} provides an upper bound for numerical stability. This formulation ensures three key behavioral patterns: when visual evidence is weak (low VCR), it intensifies non-visual suppression to counteract language priors; when strong prior conflicts are present (high PCR), it activates targeted anti-prior suppression to mitigate hallucinations; and under conditions of robust visual grounding (high VCR with low PCR), it naturally diminishes intervention intensity to preserve generation fluency.

[62] h4: 3.2.3 Minimum-Norm Closed-Form Editing

[63] p: We formulate the editing process as a constrained optimization problem that seeks the minimal perturbation achieving desired component suppression while preserving visual evidence:

[64] table: min δ ∈ ℝ d ⁡ 1 2 ​ ‖ δ ‖ 2 2 + λ n 2 ​ ‖ Π ⟂ ​ ( h + δ ) ‖ 2 2 + λ p 2 ​ ‖ Π P ​ ( h + δ ) ‖ 2 2 \min_{\delta\in\mathbb{R}^{d}}\frac{1}{2}\|\delta\|_{2}^{2}+\frac{\lambda_{n}}{2}\|\Pi_{\perp}(h+\delta)\|_{2}^{2}+\frac{\lambda_{p}}{2}\|\Pi_{P}(h+\delta)\|_{2}^{2} (14)

[65] p: where Π ⟂ = I d − Π U = Π P + Π R \Pi_{\perp}=I_{d}-\Pi_{U}=\Pi_{P}+\Pi_{R} projects onto the non-visual complement. The strict convexity of this quadratic program guarantees a unique closed-form solution, which we derive by setting the gradient to zero:

[66] table: ∇ δ ℒ = δ + λ n ​ Π ⟂ ​ ( h + δ ) + λ p ​ Π P ​ ( h + δ ) = 0 \nabla_{\delta}\mathcal{L}=\delta+\lambda_{n}\Pi_{\perp}(h+\delta)+\lambda_{p}\Pi_{P}(h+\delta)=0 (15)

[67] p: Solving this linear system yields the optimal edited state:

[68] table: h ′ = h U + 1 1 + λ n + λ p ​ h P + 1 1 + λ n ​ h R h^{\prime}=h_{U}+\frac{1}{1+\lambda_{n}+\lambda_{p}}h_{P}+\frac{1}{1+\lambda_{n}}h_{R} (16)

[69] p: This solution preserves the visual component h U h_{U} exactly while applying strength-adaptive shrinkage to conflicting ( h P h_{P} ) and uncertain ( h R h_{R} ) components. The shrinkage factors ensure monotonic suppression: stronger conflicts receive more aggressive regularization.

[70] p: To prevent unnecessary intervention and maintain generation quality, we employ certificate-aware gating:

[71] table: g ⁡ ( h ) = { 1 if ​ VCR ​ ( h ) < γ v ∨ PCR ⁡ ( h ) > γ p 0 otherwise g(h)=\begin{cases}1&\text{if }\mathrm{VCR}(h)<\gamma_{v}\ \lor\ \mathrm{PCR}(h)>\gamma_{p}\\ 0&\text{otherwise}\end{cases} (17)

[72] p: where γ v , γ p ∈ [ 0 , 1 ] \gamma_{v},\gamma_{p}\in[0,1] are tunable thresholds calibrated to balance hallucination reduction and fluency preservation. The final edited state becomes:

[73] table: h final = g ⁡ ( h ) ⋅ h ′ + ( 1 − g ⁡ ( h ) ) ⋅ h h_{\text{final}}=g(h)\cdot h^{\prime}+(1-g(h))\cdot h (18)

[74] p: This selective activation mechanism ensures targeted intervention only under high hallucination risk conditions, minimizing disruption to well-grounded generations.

[75] h3: 3.3 Theoretical Guarantees

[76] p: We provide three theoretical guarantees for HalluEdit that collectively ensure effective hallucination reduction while preserving critical properties: evidence consistency (monotonically improving alignment with visual evidence), non-interference (orthogonal edits leave visual components unaffected), and stability preservation (Lipschitz-continuous transformation maintains generation quality). Detailed proofs are provided in Appendix A .

[77] p: Evidence Consistency ensures our editing process monotonically improves alignment with visual evidence. For any hidden state h h and its edited counterpart h ′ h^{\prime} , HulluEdit guarantees:

[78] table: VCR ⁡ ( h ′ ) \displaystyle\mathrm{VCR}(h^{\prime}) ≥ VCR ⁡ ( h ) , \displaystyle\geq\mathrm{VCR}(h), (19) PCR ⁡ ( h ′ ) \displaystyle\mathrm{PCR}(h^{\prime}) ≤ PCR ⁡ ( h ) . \displaystyle\leq\mathrm{PCR}(h). (20)

[79] p: The proof relies on the closed-form solution h ′ = h U + α P ​ h P + α R ​ h R h^{\prime}=h_{U}+\alpha_{P}h_{P}+\alpha_{R}h_{R} with suppression coefficients 0 < α P , α R ≤ 1 0<\alpha_{P},\alpha_{R}\leq 1 , preserving the visual component while selectively suppressing prior and residual elements. Orthogonal decomposition ensures ‖ h ′ ‖ 2 2 ≤ ‖ h ‖ 2 2 \|h^{\prime}\|_{2}^{2}\leq\|h\|_{2}^{2} while maintaining ‖ h U ′ ‖ 2 2 = ‖ h U ‖ 2 2 \|h_{U}^{\prime}\|_{2}^{2}=\|h_{U}\|_{2}^{2} , thereby improving the Visual Certainty Ratio. Similarly, the reduction in Prior Conflict Ratio follows from ‖ h P ′ ‖ 2 2 ≤ ‖ h P ‖ 2 2 \|h_{P}^{\prime}\|_{2}^{2}\leq\|h_{P}\|_{2}^{2} .

[80] p: These properties collectively ensure that HulluEdit reduces hallucinations while maintaining visual evidence integrity and generation stability.

[81] h3: 3.4 Computational Efficiency

[82] p: HulluEdit achieves practical efficiency through a carefully optimized computational design. The per-token operations primarily consist of three stages. First, subspace estimation involves performing a weighted SVD and a thin SVD, with a computational cost of O ⁡ ( n v ​ d ​ r + n t ​ d ​ q ) O(n_{v}dr+n_{t}dq) . Subsequently, orthogonal projection is applied to decompose components, requiring O ⁡ ( d ⁡ ( r + q ) ) O(d(r+q)) operations. Finally, adaptive editing efficiently computes blending ratios and performs closed-form updates in O ⁡ ( d ) O(d) time. This streamlined pipeline ensures both effectiveness and efficiency throughout the editing process.

[83] p: With practical parameters r = 8 r=8 , q = 5 ≪ d = 4096 q=5\ll d=4096 , and bounded context lengths n v ≤ 576 n_{v}\leq 576 , n t ≤ 512 n_{t}\leq 512 , the total overhead reduces to O ⁡ ( d ⁡ ( r + q ) ) O(d(r+q)) —representing less than 2% of the transformer layer’s O ⁡ ( d 2 ) O(d^{2}) complexity. Efficiency is further enhanced through static visual caching and streaming text management with constant-time updates.

[84] p: Crucially, HulluEdit requires no additional forward passes or auxiliary models, applying edits directly to hidden states before output projection while maintaining the original model’s single-pass decoding efficiency for practical deployment.

[85] figure: Table 1 : Object hallucination evaluation on POPE benchmark. HulluEdit achieves consistent improvements across all model architectures and evaluation splits, with particularly strong performance on the Adversarial subset where language priors are most confounding. Category Method LLaVA-1.5-7B LLaVA-1.5-13B Qwen-VL-Chat-7B Accuracy ↑ \uparrow F1 ↑ \uparrow Accuracy ↑ \uparrow F1 ↑ \uparrow Accuracy ↑ \uparrow F1 ↑ \uparrow Random Greedy 87.8 87.5 87.6 87.4 88.2 87.9 VCD 88.4 87.7 88.9 87.8 89.1 88.4 ICD 88.1 87.6 88.1 87.6 88.9 88.1 VAF 89.6 89.3 90.1 89.9 90.0 89.7 DeCo 89.1 89.8 82.2 84.9 87.8 87.2 Ours 90.4 90.5 90.6 90.8 90.2 89.9 Popular Greedy 82.5 83.2 82.7 84.1 82.4 83.1 VCD 83.1 84.1 83.7 85.1 83.0 84.1 ICD 82.1 82.9 82.9 84.3 83.2 84.5 VAF 84.5 84.9 85.2 86.4 84.9 85.1 DeCo 84.6 85.8 78.4 81.7 85.5 84.9 Ours 87.5 87.6 88.0 88.3 88.2 87.7 Adversarial Greedy 77.6 79.4 77.8 79.5 77.2 78.9 VCD 78.1 79.6 78.2 79.7 78.8 80.1 ICD 78.5 79.9 79.1 80.1 78.1 79.2 VAF 80.1 81.0 80.7 81.7 80.4 81.2 DeCo 78.3 81.1 72.6 77.9 81.5 81.5 Ours 82.5 83.4 82.7 84.0 84.3 84.2

[86] h2: 4 Experiments

[87] h3: 4.1 Experimental Setup

[88] p: Models. To verify the effectiveness of the proposed method, we conducted experiments on multiple backbones. We evaluate HulluEdit on four representative LVLMs: LLaVA-1.5 in both 7B and 13B variants, MiniGPT-4, mPLUG-Owl2, and Qwen-VL-Chat-7B. All models utilize their official configurations, with HulluEdit applied purely during inference to the final transformer layer without requiring retraining or auxiliary reference models.

[89] p: Baselines. We compare against state-of-the-art hallucination mitigation methods spanning three technical categories. Contrastive decoding approaches include DoLa [ 5 ] which reduces shallow semantic influence and VCD [ 12 ] that enhances visual evidence while subtracting interfering priors. Dynamic correction methods encompass DeCo [ 23 ] for integrating preceding-layer knowledge and OPERA [ 10 ] for penalizing overconfident tokens. Subspace editing techniques involve Nullu [ 26 ] with static hallucination subspace projection and VAF [ 27 ] for visual attention enhancement. All baselines employ author-recommended hyperparameters under identical prompts and decoding configurations.

[90] p: Decoding Settings. We employ greedy decoding for POPE evaluation and nucleus sampling for captioning tasks, using conservative temperature of 0.05 and top-p of 1.0. Maximum generation length is consistently capped at 64 tokens across experiments. All reported results represent means over three random seeds.

[91] p: Implementation Details. HulluEdit estimates weighted SVD subspaces online using cached visual states and accumulated non-visual text states. For 7B models, layer 26 serves as the anchor layer with edits applied to the final transformer layer. Detailed hyperparameter settings including subspace ranks, strength parameters, and certificate thresholds are provided in the Appendix B . All experiments run on single A100 GPUs without reference models or additional forward passes.

[92] h3: 4.2 Benchmarks and Metrics

[93] p: Object Hallucination Evaluation. We utilize two established benchmarks for comprehensive assessment. POPE employs VQA-style polling across random, popular and adversarial splits to evaluate object presence, reporting both Accuracy and F1 scores. CHAIR quantifies object hallucination in image captioning through instance-level and sentence-level metrics using 500 MSCOCO images, with the metrics defined as:

[94] table: CHAIR i \displaystyle\mathrm{CHAIR}_{i} = | hallucinated objects | | all mentioned objects | , \displaystyle=\frac{|\text{hallucinated objects}|}{|\text{all mentioned objects}|}, (21) CHAIR s \displaystyle\mathrm{CHAIR}_{s} = | captions with hallucinated objects | | all captions | . \displaystyle=\frac{|\text{captions with hallucinated objects}|}{|\text{all captions}|}.

[95] p: General Capability Assessment. The MME benchmark provides comprehensive evaluation of perceptual and cognitive abilities across 14 diverse subtasks including object recognition, attribute reasoning and spatial understanding.

[96] p: Efficiency Measurement. We quantify practical overhead through decoding throughput measured in tokens per second on 500 MSCOCO images, excluding preprocessing. This ensures fair comparison across methods under identical hardware.

[97] figure: Table 2 : Caption hallucination evaluation on MSCOCO dataset. Our method establishes new state-of-the-art performance on LLaVA-1.5 and mPLUG-Owl2, demonstrating the effectiveness of orthogonal subspace decomposition in reducing both instance-level and sentence-level hallucinations. Method LLaVA-1.5 MiniGPT-4 mPLUG-Owl2 CHAIR i ↓ \mathrm{CHAIR}_{i}\downarrow CHAIR s ↓ \mathrm{CHAIR}_{s}\downarrow BLEU ↑ \uparrow CHAIR i ↓ \mathrm{CHAIR}_{i}\downarrow CHAIR s ↓ \mathrm{CHAIR}_{s}\downarrow BLEU ↑ \uparrow CHAIR i ↓ \mathrm{CHAIR}_{i}\downarrow CHAIR s ↓ \mathrm{CHAIR}_{s}\downarrow BLEU ↑ \uparrow Greedy 7.08 20.40 15.72 12.20 32.40 14.57 8.62 22.90 15.01 Beam Search [ 8 ] 6.84 19.50 15.99 11.87 30.10 15.35 7.62 20.30 15.43 DoLa [ 5 ] 6.75 20.20 15.68 12.15 31.90 14.54 8.36 22.40 15.13 OPERA [ 10 ] 6.07 17.50 16.02 11.96 29.70 14.82 7.18 20.07 15.41 VCD [ 12 ] 7.28 20.30 14.53 12.64 29.00 14.42 8.68 22.80 15.14 Woodpecker [ 28 ] 7.50 23.85 17.05 10.20 28.87 15.30 8.43 26.33 16.43 LURE [ 29 ] 6.50 19.48 15.97 10.20 27.88 15.03 7.67 21.27 15.65 HALC [ 3 ] 5.72 16.90 16.02 9.42 25.20 14.91 7.00 18.80 15.33 Nullu [ 26 ] 5.30 15.20 15.69 8.99 21.40 14.81 5.77 15.60 15.45 Ours 4.18 13.00 15.49 8.28 23.60 14.76 3.35 13.60 15.34

[98] figure: Table 3 : MME fine-grained evaluation. HulluEdit improves object recognition (Existence, Position, Color) while trading off Count performance, supporting the separation of visual and language priors. Method Existence ↑ \uparrow Count ↑ \uparrow Position ↑ \uparrow Color ↑ \uparrow LLaVA-1.5 181.67 118.33 104.44 152.78 Nullu 190.00 121.11 105.56 156.67 DeCo 175.00 128.33 98.33 125.00 HulluEdit 195.00 105.00 126.67 160.00

[99] figure: Figure 3 : Decoding throughput comparison measured in tokens per second (TPS). HulluEdit achieves competitive inference speed, significantly faster than recent hallucination mitigation methods like OPERA and HALC while maintaining strong performance.

[100] h3: 4.3 Results and Analysis

[101] p: POPE Evaluation. HulluEdit demonstrates consistent and substantial hallucination reduction across all model architectures and evaluation splits. As shown in Table 1 , our method achieves the highest Accuracy and F1 scores across all 18 evaluation settings, with particularly notable gains on the challenging Adversarial split—where linguistic priors most strongly conflict with visual evidence. These consistent improvements across diverse LVLM architectures, including adapter-based, deep-fusion, and hybrid designs, underscore the generalizability of our approach. Crucially, the orthogonal constraint U T ​ P = 0 U^{T}P=0 mathematically ensures that edits applied to the anti-prior subspace leave visual representations entirely intact, thereby sustaining robust performance under strong prior–evidence conflicts. This adaptive and evidence-preserving mechanism distinguishes HulluEdit from static subspace methods, which lack token-level adaptability and risk suppressing genuine visual signals.

[102] p: CHAIR Performance. HulluEdit also exhibits superior performance in caption-based hallucination evaluation, effectively reducing both instance-level and sentence-level hallucinations. As summarized in Table 2 , our method achieves state-of-the-art results on LLaVA-1.5 and mPLUG-Owl2, significantly lowering hallucination rates across both metrics. On MiniGPT-4, HulluEdit remains highly competitive. The marked decrease in sentence-level hallucinations further indicates its ability to prevent error propagation, where an initial incorrect object mention leads to subsequent inaccuracies. These gains are facilitated by our orthogonal decomposition, which enables fine-grained, token-level suppression of conflicting priors and uncertain components without compromising visual grounding.

[103] p: MME Analysis. HulluEdit exhibits a targeted performance pattern on the comprehensive MME benchmark that aligns with our design intent. As shown in Table 3 , our method significantly improves Existence (+13.33), Position (+22.23), and Color (+7.22) recognition while showing a decrease in Count (-13.33) compared to the LLaVA-1.5 baseline. This selective improvement validates our core hypothesis that suppressing non-visual priors primarily benefits object-level recognition tasks where prior knowledge conflicts are most problematic. The Count performance trade-off suggests that fine-grained numeric information may be encoded in the residual subspace that we conservatively regularize.

[104] p: Efficiency Analysis. HulluEdit achieves an optimal balance between hallucination mitigation and computational efficiency, maintaining competitive inference speed while delivering substantial performance improvements. As shown in Figure 3 , our method significantly outperforms recent hallucination mitigation approaches including OPERA and HALC in terms of decoding throughput, while introducing only moderate overhead compared to basic decoding strategies. This efficiency advantage stems from our optimized single-pass design: the orthogonal subspace operations scale linearly with hidden dimension through low-rank approximations ( r = 8 , q = 5 ≪ d = 4096 r=8,q=5\ll d=4096 ), and certificate-aware gating selectively applies interventions only under high hallucination risk conditions. The practical throughput demonstrates HulluEdit’s viability for real-world deployment scenarios where both accuracy and latency are critical considerations.

[105] figure: Figure 4 : Qualitative comparison of object hallucination mitigation. An example image with captions generated by the Original model and our HulluEdit method. Hallucinated objects are highlighted in red.

[106] figure: Table 4 : Ablation studies of HulluEdit components on LLaVA-1.5-7B using the MSCOCO dataset. We report instance-level ( CHAIR i \mathrm{CHAIR}_{i} ) and sentence-level ( CHAIR s \mathrm{CHAIR}_{s} ) hallucination rates (lower is better). L a L_{a} : anchor layer, L e L_{e} : edit layer. Category Variant 𝐂𝐇𝐀𝐈𝐑 𝐢 ↓ \mathbf{CHAIR_{i}\downarrow} 𝐂𝐇𝐀𝐈𝐑 𝐬 ↓ \mathbf{CHAIR_{s}\downarrow} Full Model L a = 26 L_{a}{=}26 , L e = last L_{e}{=}\text{last} 4.18 13.00 Layer Selection L a = 20 L_{a}{=}20 , L e = last L_{e}{=}\text{last} 5.55 19.72 L a = 30 L_{a}{=}30 , L e = last L_{e}{=}\text{last} 5.37 13.80 Single-layer L a = L e = last L_{a}{=}L_{e}{=}\text{last} 5.50 18.20 Components uniform SVD 4.85 13.68 w/o orth. complement 5.60 15.90 fixed strengths 5.20 13.88 w/o gating 7.70 22.90 Suppression residual only 5.90 16.82 anti-prior only 5.40 14.66

[107] h3: 4.4 Ablation Studies

[108] p: We conduct comprehensive ablation studies to validate the key design choices in HulluEdit. The results are summarized in Table 4 .

[109] p: Layer Selection and Alignment. Experiments on anchor layer selection show that layer 26 achieves the optimal balance, yielding the lowest CHAIR scores compared to shallower or deeper alternatives. This confirms that mid-layer representations effectively capture visual evidence prior to significant prior suppression. Furthermore, cross-layer alignment is essential: applying edits at the top layer using features from anchor layer 26 substantially outperforms same-layer estimation. This indicates that mid-layer visual features robustly counteract prior suppression in deeper layers while preserving evidence integrity.

[110] p: Core Component Analysis. Component-wise analysis substantiates our core methodological contributions. Weighted SVD consistently outperforms uniform SVD, underscoring the importance of context-aware visual token weighting. The orthogonal complement construction is critical, as its absence leads to notable performance degradation, confirming that spatial separation between visual and prior components prevents undesirable interference. Adaptive strength scheduling based on VCR and PCR ratios surpasses fixed-strength alternatives, highlighting the value of dynamic intervention calibration. Certificate-aware gating effectively avoids unnecessary edits, and its removal results in significant performance decline, emphasizing its role in preserving generation fluency.

[111] p: Suppression Mechanism Necessity. Both suppression mechanisms are essential for optimal performance. Isolated use of either residual or anti-prior shrinkage underperforms the full framework, confirming hallucinations arise from general non-visual components and specific prior conflicts. The residual component handles ambiguous context with conservative regularization, while the anti-prior subspace targets conflicting linguistic patterns; their joint operation enables effective hallucination mitigation.

[112] h3: 4.5 Case Study

[113] p: We conduct a qualitative case study to assess the effectiveness of HulluEdit in mitigating object hallucinations. As illustrated in Figure 4 , we compare the captions generated by the original LLaVA model and our HulluEdit framework on a real-world image depicting a motorcycle near a White Mountain National Forest sign. The baseline model produces descriptions containing clear hallucinations—such as misplacing the motorcycle on the road and inventing a “backpack” on the ground—driven by strong linguistic priors. In contrast, HulluEdit correctly locates the motorcycle on the grass, accurately identifies the national forest signage, and avoids generating any spurious objects. This improvement is achieved by decomposing hidden states into orthogonal subspaces and selectively suppressing conflicting prior patterns, thereby producing outputs strictly aligned with visual evidence. These results qualitatively validate HulluEdit’s ability to enhance factual grounding. Additional examples are provided in the appendix C .

[114] h2: 5 Conclusion

[115] p: We present HulluEdit, a single-pass framework that mitigates object hallucinations in LVLMs by decomposing hidden states into orthogonal subspaces representing visual evidence, conflicting priors, and residual uncertainty. Through online weighted SVD and adaptive editing, our approach selectively suppresses hallucinatory signals while preserving visual grounding. Empirical evaluation demonstrates state-of-the-art hallucination reduction across diverse architectures while maintaining caption quality and inference efficiency. Our method offers an effective alternative for enhancing LVLM reliability.

[116] h2: 6 Acknowledgement

[117] p: This work was supported by the Beijing Natural Science Foundation (JQ24019); in part by the National Natural Science Foundation of China (No. 62576047); the SMP-Z Large Model Fund (No. CIPS-SMP20250313); and the Open Fund of the Key Laboratory for Civil Aviation Collaborative Air Traffic Management Technology and Applications (No. 2025-001).

[118] h2: References

[119] h2: Appendix A Theoretical Proofs

[120] p: This appendix provides comprehensive mathematical proofs for the theoretical guarantees of HulluEdit, including evidence consistency, non-interference, and stability preservation.

[121] h3: A.1 Proof of Evidence Consistency

[122] p: Proposition 1 (Evidence Consistency). For any hidden state h h and its edited counterpart h ′ h^{\prime} , HulluEdit guarantees monotonic improvement in evidence alignment:

[123] table: VCR ⁡ ( h ′ ) \displaystyle\mathrm{VCR}(h^{\prime}) ≥ VCR ⁡ ( h ) , \displaystyle\geq\mathrm{VCR}(h), (22) PCR ⁡ ( h ′ ) \displaystyle\mathrm{PCR}(h^{\prime}) ≤ PCR ⁡ ( h ) . \displaystyle\leq\mathrm{PCR}(h). (23)

[124] p: Proof. The proof proceeds by analyzing the effect of our orthogonal subspace editing on the Visual Certainty Ratio (VCR) and Prior Conflict Ratio (PCR).

[125] p: From the closed-form solution derived in Eq. (15), the edited state is expressed as:

[126] table: h ′ = h U + α P ​ h P + α R ​ h R , h^{\prime}=h_{U}+\alpha_{P}h_{P}+\alpha_{R}h_{R}, (24)

[127] p: where α P = 1 1 + λ n + λ p \alpha_{P}=\frac{1}{1+\lambda_{n}+\lambda_{p}} and α R = 1 1 + λ n \alpha_{R}=\frac{1}{1+\lambda_{n}} are the suppression coefficients for the prior and residual components, respectively, with λ n , λ p ≥ 0 \lambda_{n},\lambda_{p}\geq 0 representing the adaptive editing strengths.

[128] p: By construction, the orthogonal subspace decomposition established in Eq. (9) ensures:

[129] table: h = h U + h P + h R , ‖ h ‖ 2 2 = ‖ h U ‖ 2 2 + ‖ h P ‖ 2 2 + ‖ h R ‖ 2 2 , h=h_{U}+h_{P}+h_{R},\quad\|h\|_{2}^{2}=\|h_{U}\|_{2}^{2}+\|h_{P}\|_{2}^{2}+\|h_{R}\|_{2}^{2}, (25)

[130] p: with the orthogonality conditions h U T ​ h P = h U T ​ h R = h P T ​ h R = 0 h_{U}^{T}h_{P}=h_{U}^{T}h_{R}=h_{P}^{T}h_{R}=0 .

[131] p: Applying this orthogonality to the edited state, we obtain the squared norm decomposition:

[132] table: ‖ h ′ ‖ 2 2 = ‖ h U ‖ 2 2 + α P 2 ​ ‖ h P ‖ 2 2 + α R 2 ​ ‖ h R ‖ 2 2 . \|h^{\prime}\|_{2}^{2}=\|h_{U}\|_{2}^{2}+\alpha_{P}^{2}\|h_{P}\|_{2}^{2}+\alpha_{R}^{2}\|h_{R}\|_{2}^{2}. (26)

[133] p: Since λ n , λ p ≥ 0 \lambda_{n},\lambda_{p}\geq 0 , we have the strict inequalities 0 < α P , α R ≤ 1 0<\alpha_{P},\alpha_{R}\leq 1 , which implies:

[134] table: ‖ h ′ ‖ 2 2 ≤ ‖ h U ‖ 2 2 + ‖ h P ‖ 2 2 + ‖ h R ‖ 2 2 = ‖ h ‖ 2 2 . \|h^{\prime}\|_{2}^{2}\leq\|h_{U}\|_{2}^{2}+\|h_{P}\|_{2}^{2}+\|h_{R}\|_{2}^{2}=\|h\|_{2}^{2}. (27)

[135] p: Crucially, the visual component remains completely unaltered by our editing procedure due to the orthogonal constraint U T ​ P = U T ​ R = 0 U^{T}P=U^{T}R=0 :

[136] table: ‖ h U ′ ‖ 2 2 = ‖ h U ‖ 2 2 . \|h_{U}^{\prime}\|_{2}^{2}=\|h_{U}\|_{2}^{2}. (28)

[137] p: We now prove the first inequality for the Visual Certainty Ratio. By definition:

[138] table: VCR ⁡ ( h ′ ) = ‖ h U ′ ‖ 2 2 ‖ h ′ ‖ 2 2 = ‖ h U ‖ 2 2 ‖ h ′ ‖ 2 2 . \mathrm{VCR}(h^{\prime})=\frac{\|h_{U}^{\prime}\|_{2}^{2}}{\|h^{\prime}\|_{2}^{2}}=\frac{\|h_{U}\|_{2}^{2}}{\|h^{\prime}\|_{2}^{2}}. (29)

[139] p: Since ‖ h ′ ‖ 2 2 ≤ ‖ h ‖ 2 2 \|h^{\prime}\|_{2}^{2}\leq\|h\|_{2}^{2} and ‖ h U ‖ 2 2 > 0 \|h_{U}\|_{2}^{2}>0 (for non-degenerate cases), we have:

[140] table: VCR ⁡ ( h ′ ) = ‖ h U ‖ 2 2 ‖ h ′ ‖ 2 2 ≥ ‖ h U ‖ 2 2 ‖ h ‖ 2 2 = VCR ⁡ ( h ) . \mathrm{VCR}(h^{\prime})=\frac{\|h_{U}\|_{2}^{2}}{\|h^{\prime}\|_{2}^{2}}\geq\frac{\|h_{U}\|_{2}^{2}}{\|h\|_{2}^{2}}=\mathrm{VCR}(h). (30)

[141] p: The inequality is strict when ‖ h ′ ‖ 2 2 < ‖ h ‖ 2 2 \|h^{\prime}\|_{2}^{2}<\|h\|_{2}^{2} , which occurs whenever λ n + λ p > 0 \lambda_{n}+\lambda_{p}>0 and at least one of h P h_{P} or h R h_{R} is non-zero.

[142] p: For the second inequality concerning the Prior Conflict Ratio, we observe that the edited prior component satisfies:

[143] table: ‖ h P ′ ‖ 2 2 = α P 2 ​ ‖ h P ‖ 2 2 ≤ ‖ h P ‖ 2 2 , \|h_{P}^{\prime}\|_{2}^{2}=\alpha_{P}^{2}\|h_{P}\|_{2}^{2}\leq\|h_{P}\|_{2}^{2}, (31)

[144] p: with equality only when λ n + λ p = 0 \lambda_{n}+\lambda_{p}=0 or h P = 0 h_{P}=0 .

[145] p: Now consider the Prior Conflict Ratio of the edited state:

[146] table: PCR ⁡ ( h ′ ) = ‖ h P ′ ‖ 2 2 ‖ h ′ ‖ 2 2 = α P 2 ​ ‖ h P ‖ 2 2 ‖ h ′ ‖ 2 2 . \mathrm{PCR}(h^{\prime})=\frac{\|h_{P}^{\prime}\|_{2}^{2}}{\|h^{\prime}\|_{2}^{2}}=\frac{\alpha_{P}^{2}\|h_{P}\|_{2}^{2}}{\|h^{\prime}\|_{2}^{2}}. (32)

[147] p: To establish the desired inequality, we analyze the ratio:

[148] table: PCR ⁡ ( h ′ ) PCR ⁡ ( h ) = α P 2 ​ ‖ h P ‖ 2 2 ‖ h ′ ‖ 2 2 ⋅ ‖ h ‖ 2 2 ‖ h P ‖ 2 2 = α P 2 ⋅ ‖ h ‖ 2 2 ‖ h ′ ‖ 2 2 . \frac{\mathrm{PCR}(h^{\prime})}{\mathrm{PCR}(h)}=\frac{\alpha_{P}^{2}\|h_{P}\|_{2}^{2}}{\|h^{\prime}\|_{2}^{2}}\cdot\frac{\|h\|_{2}^{2}}{\|h_{P}\|_{2}^{2}}=\alpha_{P}^{2}\cdot\frac{\|h\|_{2}^{2}}{\|h^{\prime}\|_{2}^{2}}. (33)

[149] p: From previous results, we have α P 2 ≤ 1 \alpha_{P}^{2}\leq 1 and ‖ h ‖ 2 2 ≥ ‖ h ′ ‖ 2 2 \|h\|_{2}^{2}\geq\|h^{\prime}\|_{2}^{2} , which implies:

[150] table: PCR ⁡ ( h ′ ) PCR ⁡ ( h ) ≤ 1 ⇒ PCR ⁡ ( h ′ ) ≤ PCR ⁡ ( h ) . \frac{\mathrm{PCR}(h^{\prime})}{\mathrm{PCR}(h)}\leq 1\quad\Rightarrow\quad\mathrm{PCR}(h^{\prime})\leq\mathrm{PCR}(h). (34)

[151] p: The inequality is strict when α P < 1 \alpha_{P}<1 (i.e., λ n + λ p > 0 \lambda_{n}+\lambda_{p}>0 ) and ‖ h P ‖ 2 2 > 0 \|h_{P}\|_{2}^{2}>0 .

[152] p: Both inequalities demonstrate that our editing procedure monotonically improves evidence alignment by strengthening visual grounding while suppressing conflicting priors, with strict improvement under non-trivial editing conditions.

[153] h3: A.2 Proof of Non-interference

[154] p: Proposition 2 (Non-interference). The orthogonal subspace decomposition ensures that edits applied to one subspace do not interfere with components in other subspaces.

[155] p: Proof. The orthogonal decomposition is constructed such that the visual evidence subspace U U , anti-prior subspace P P , and residual subspace R R are mutually orthogonal:

[156] table: U T ​ P = 0 , U T ​ R = 0 , P T ​ R = 0 . U^{T}P=0,\quad U^{T}R=0,\quad P^{T}R=0. (35)

[157] p: The orthogonal projectors are defined as:

[158] table: Π U \displaystyle\Pi_{U} = U ​ U T , \displaystyle=UU^{T}, (36) Π P \displaystyle\Pi_{P} = P ​ P T , \displaystyle=PP^{T}, (37) Π R \displaystyle\Pi_{R} = I − Π U − Π P . \displaystyle=I-\Pi_{U}-\Pi_{P}. (38)

[159] p: By the orthogonality of subspaces, we have:

[160] table: Π U ​ Π P = U ​ U T ​ P ​ P T = 0 , \Pi_{U}\Pi_{P}=UU^{T}PP^{T}=0, (39)

[161] p: since U T ​ P = 0 U^{T}P=0 . Similarly:

[162] table: Π U ​ Π R \displaystyle\Pi_{U}\Pi_{R} = U ​ U T ​ ( I − U ​ U T − P ​ P T ) = 0 , \displaystyle=UU^{T}(I-UU^{T}-PP^{T})=0, (40) Π P ​ Π R \displaystyle\Pi_{P}\Pi_{R} = P ​ P T ​ ( I − U ​ U T − P ​ P T ) = 0 . \displaystyle=PP^{T}(I-UU^{T}-PP^{T})=0. (41)

[163] p: Therefore, any edit applied to one subspace projector leaves the other components unaffected, ensuring complete decoupling.

[164] h3: A.3 Proof of Stability Preservation

[165] p: Proposition 3 (Stability Preservation). The editing transformation is contractive with Lipschitz constant L ≤ 1 L\leq 1 , ensuring stability during sequential decoding.

[166] p: Proof. The editing transformation T : ℝ d → ℝ d T:\mathbb{R}^{d}\rightarrow\mathbb{R}^{d} is defined as:

[167] table: T ⁡ ( h ) = Π U ​ h + α P ​ Π P ​ h + α R ​ Π R ​ h , T(h)=\Pi_{U}h+\alpha_{P}\Pi_{P}h+\alpha_{R}\Pi_{R}h, (42)

[168] p: where α P = 1 1 + λ n + λ p \alpha_{P}=\frac{1}{1+\lambda_{n}+\lambda_{p}} and α R = 1 1 + λ n \alpha_{R}=\frac{1}{1+\lambda_{n}} , with λ n , λ p ≥ 0 \lambda_{n},\lambda_{p}\geq 0 . Since 0 < α P , α R ≤ 1 0<\alpha_{P},\alpha_{R}\leq 1 , the transformation is linear and contractive.

[169] p: For any two hidden states h 1 , h 2 ∈ ℝ d h_{1},h_{2}\in\mathbb{R}^{d} , we have:

[170] table: ‖ T ⁡ ( h 1 ) − T ⁡ ( h 2 ) ‖ 2 \displaystyle\|T(h_{1})-T(h_{2})\|_{2} ≤ ‖ h 1 − h 2 ‖ 2 . \displaystyle\leq\|h_{1}-h_{2}\|_{2}. (43)

[171] p: Thus, the Lipschitz constant L ≤ 1 L\leq 1 , ensuring stability during sequential decoding and preserving generation quality.

[172] h2: Appendix B Hyperparameter Specifications

[173] p: This appendix provides the complete hyperparameter configuration for HulluEdit experiments on LLaVA-1.5-7B. All parameter values were determined through systematic empirical validation on held-out development sets to optimize the trade-off between hallucination reduction and generation quality.

[174] figure: Table 5 : Hyperparameter configuration for HulluEdit on LLaVA-1.5-7B Parameter Value Anchor layer ( l a l_{a} ) 26 Evidence rank ( r r ) 8 Prior rank ( q q ) 5 Base visual ( κ \kappa ) 0.60 Base prior ( λ 0 \lambda_{0} ) 0.26 Max suppression ( λ max \lambda_{\max} ) 3.6 Stability ( ϵ \epsilon ) 1.0 × 10 − 6 1.0\times 10^{-6} Generation Settings Max tokens 64 Top-p 1.0 Temperature 0.05

[175] p: The hyperparameter configuration reflects careful balancing of competing objectives. The anchor layer at l a = 26 l_{a}=26 was selected to capture robust visual evidence before deeper layers introduce significant linguistic prior suppression. Subspace dimensionalities of r = 8 r=8 for visual evidence and q = 5 q=5 for anti-prior components balance expressive power against computational efficiency. Strength parameters κ = 0.60 \kappa=0.60 and λ 0 = 0.26 \lambda_{0}=0.26 govern the adaptive suppression intensity, dynamically scheduled based on the Visual Certainty Ratio and Prior Conflict Ratio metrics. All generation settings follow established evaluation protocols to ensure fair comparison with baseline methods across benchmarks.

[176] h2: Appendix C Qualitative Case Studies

[177] p: This appendix presents additional qualitative examples demonstrating HulluEdit’s effectiveness in mitigating object hallucinations while preserving visual grounding. The case studies illustrate how our method selectively suppresses conflicting linguistic priors without compromising genuine visual evidence.

[178] figure: Figure 5 : Qualitative comparison of object hallucination mitigation on LLaVA-1.5-7B. The baseline model (top) generates descriptions containing spurious objects (highlighted in red), while HulluEdit (bottom) produces outputs strictly aligned with visual evidence. These examples demonstrate our method’s ability to suppress conflicting linguistic priors while preserving accurate visual descriptions.

[179] h2: Appendix D Extended Benchmark Evaluation

[180] p: To provide a more thorough evaluation of our method, we conducted experiments on two additional widely-recognized hallucination benchmarks: AMBER and Hallu-Bench.

[181] p: AMBER Benchmark. This benchmark provides comprehensive metrics including CHAIR (hallucination rate), Coverage (object recall), Hallucination (false positive rate), and Cognition (reasoning-related hallucinations). As shown in Table 6 , HulluEdit achieves the lowest CHAIR score of 5.3, reducing hallucinations by 35.4% compared to the Vanilla baseline (8.2). Notably, our method also significantly reduces cognitive hallucinations (Cog) to 2.1, indicating improved reasoning accuracy.

[182] figure: Table 6 : Results on AMBER benchmark. ↓ \downarrow indicates lower is better, ↑ \uparrow indicates higher is better. Method CHAIR ↓ \downarrow Cover ↑ \uparrow Hal ↓ \downarrow Cog ↓ \downarrow Vanilla 8.2 48.9 34.3 4.0 DeCo 6.6 47.5 28.1 2.8 Ours 5.3 47.0 22.4 2.1

[183] p: Hallu-Bench. This benchmark evaluates multiple aspects of hallucination: question accuracy (qAcc), factual accuracy (fAcc), and answering accuracy (aAcc). Table 7 demonstrates that HulluEdit consistently outperforms baselines across all metrics, achieving an overall score of 30.1, a significant improvement over Vanilla (27.6) and QLoRA (25.2).

[184] figure: Table 7 : Results on Hallu-Bench benchmark. Method Overall qAcc fAcc aAcc Vanilla 27.6 13.6 20.5 48.8 QLoRA 25.2 13.2 16.2 46.2 Ours 30.1 16.9 21.4 52.1

[185] h2: Appendix E General Capability Preservation

[186] p: A critical concern in hallucination mitigation is maintaining the model’s general visual understanding and reasoning capabilities. We evaluate HulluEdit on two standard benchmarks: MME (comprehensive perception and cognition) and MMVet (multi-modal reasoning).

[187] p: As presented in Table 8 , HulluEdit achieves a Total score of 28.5 on MMVet, outperforming both the Vanilla baseline (23.6) and DeCo (27.9). This indicates that our method not only reduces hallucinations but also enhances overall reasoning performance by eliminating interference from conflicting linguistic priors.

[188] figure: Table 8 : MMVet results demonstrating general capability preservation. Model Method Total LLaVA-1.5 Vanilla 23.6 LLaVA-1.5 DeCo 27.9 LLaVA-1.5 Ours 28.5

[189] p: Additionally, Figure 6 presents the MME benchmark results, showing that HulluEdit preserves or improves general visual understanding capabilities across all evaluation dimensions.

[190] figure: Figure 6 : MME benchmark results on LLaVA-1.5. HulluEdit maintains general visual understanding while reducing hallucinations.

[191] h2: Appendix F Generalization to Recent Models

[192] p: To verify the broad applicability of HulluEdit, we evaluate our method on two state-of-the-art vision-language models: Qwen2.5-VL and Intern2.5-VL. The results in Table 9 demonstrate consistent and substantial improvements across both models. Specifically, on Qwen2.5-VL, HulluEdit reduces CHAIR s from 15.6 to 13.2 and CHAIR i from 6.2 to 6.04. Similar improvements are observed on Intern2.5-VL, confirming the strong generalization capability of our approach.

[193] figure: Table 9: Generalization results on recent VLM architectures. Model Method CHAIR s ↓ \downarrow CHAIR i ↓ \downarrow Recall ↑ \uparrow Qwen2.5-VL greedy 15.6 6.2 46.0 Ours 13.2 6.04 45.2 Intern2.5-VL greedy 15.4 5.4 51.6 Ours 12.8 5.1 50.9

[194] h2: Appendix G Hyperparameter Sensitivity Analysis

[195] p: We analyze the sensitivity of key hyperparameters to provide practical guidance for deployment. The hyperparameters can be categorized into two groups: architecture-dependent parameters (anchor layer l a l_{a} and edit layer l e l_{e} ) and learning-dependent parameters ( r r , q q , and κ \kappa ).

[196] p: The anchor and edit layers are determined by the model architecture. Specifically, the anchor layer is selected from mid-to-high transformer layers to ensure stable visual-semantic alignment, while the edit layer is consistently placed at the top of the model.

[197] p: As shown in Table 10 , the remaining hyperparameters exhibit low sensitivity within practical ranges. Stable results are consistently achieved with r , q ∈ [ 4 , 8 ] r,q\in[4,8] and κ ∈ [ 0.3 , 0.8 ] \kappa\in[0.3,0.8] , with standard deviations less than 0.05 across all metrics.

[198] figure: Table 10: Hyperparameters sensitivity analysis on LLaVA-1.5-7B. Variable CHAIR s ↓ \downarrow CHAIR i ↓ \downarrow Recall ↑ \uparrow Vanilla 20.4 7.08 54.6 r r = [4,8] 13.4 ± \pm 0.4 4.21 ± \pm 0.03 54.5 ± \pm 0.3 q q = [4,8] 13.2 ± \pm 0.2 4.20 ± \pm 0.02 54.1 ± \pm 0.2 κ \kappa = [0.3,0.8] 13.3 ± \pm 0.3 4.22 ± \pm 0.04 54.2 ± \pm 0.2

[199] h2: Appendix H Empirical Validation of Theoretical Guarantees

[200] p: To provide stronger empirical support for our theoretical analysis, we conducted a quantitative analysis of the subspace editing effects. For each token at the editing layer, we computed the activation change Δ ​ h = h final − h orig \Delta h=h_{\text{final}}-h_{\text{orig}} . We then projected Δ ​ h \Delta h onto the visual feature subspace U U and the anti-prior subspace P P , measuring the respective projection norms | Δ ​ h U | 2 |\Delta h_{U}|_{2} and | Δ ​ h P | 2 |\Delta h_{P}|_{2} .

[201] p: The experimental results strongly confirm our theoretical claims: the changes within the visual subspace are orders of magnitude smaller than those within the anti-prior subspace (on the order of 10 − 3 10^{-3} versus 10 1 10^{1} , respectively). This provides concrete evidence of minimal interference with visual evidence and effective suppression of language priors , validating the core principles of our method.

[202] figure: Figure 7 : Distribution of activation changes in visual subspace ( U U ) vs. anti-prior subspace ( P P ). The magnitude of changes in the visual subspace is orders of magnitude smaller ( 10 − 3 10^{-3} ) compared to the anti-prior subspace ( 10 1 10^{1} ), validating minimal interference with visual evidence.

[203] h2: Instructions for reporting errors

[204] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[205] p: Tip: You can select the relevant text first, to include it in your report.

[206] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[207] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
