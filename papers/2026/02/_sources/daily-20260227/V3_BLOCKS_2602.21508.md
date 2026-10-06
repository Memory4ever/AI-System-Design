[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: WaterVIB: Learning Minimal Sufficient Watermark Representations via Variational Information Bottleneck

[3] h6: Abstract

[4] p: Robust watermarking is critical for intellectual property protection, whereas existing methods face a severe vulnerability against regeneration-based AIGC attacks. We identify that existing methods fail because they entangle the watermark with high-frequency cover texture, which is susceptible to being rewritten during generative purification. To address this, we propose WaterVIB, a theoretically grounded framework that reformulates the encoder as an information sieve via the Variational Information Bottleneck. Instead of overfitting to fragile cover details, our approach forces the model to learn a Minimal Sufficient Statistic of the message. This effectively filters out redundant cover nuances prone to generative shifts, retaining only the essential signal invariant to regeneration. We theoretically prove that optimizing this bottleneck is a necessary condition for robustness against distribution-shifting attacks. Extensive experiments demonstrate that WaterVIB significantly outperforms state-of-the-art methods, achieving superior zero-shot resilience against unknown diffusion-based editing.

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] p: Digital watermarking serves as a crucial technology for copyright protection and content provenance in the era of digital media. Ideally, a watermark should be imperceptible to humans yet robust enough to survive various distortions. Deep learning has significantly advanced this field by jointly training encoder-decoder networks, thereby embedding messages into images with high fidelity ( Bui et al., 2023 ) .

[8] p: While deep learning watermarking has achieved resilience against standard distortions (e.g., Gaussian noise, JPEG compression) via heuristic data augmentation ( Zhu et al., 2018 ) , this paradigm struggles to withstand the emerging threat of generative purification ( Podell et al., 2023 ) . Unlike traditional attacks that merely degrade image quality, modern diffusion-based tools ( Zhao et al., 2024 ) regenerate content leveraging learned priors ( Rombach et al., 2022 ) , stripping away watermark signals while preserving visual fidelity. By projecting the watermarked image back onto the manifold of natural images, these methods eliminate hidden signals perceived as unnatural perturbations. Consequently, existing watermarks, trained primarily on additive or geometric distortions, may well fail to generalize to such semantic regeneration, resulting in the inevitable erasure of copyright information ( Zhao et al., 2024 ) .

[9] figure: Figure 1 : Vulnerability of standard watermarking versus the robustness of our VIB method. The residual visualizations (Top) reveal a strong correlation between the watermark signal and AIGC purification, highlighting the fragility of texture-entangled methods. We visualize the Bit Accuracy (higher is better) across six AIGC editing benchmarks. To clearly demonstrate the relative improvements on tasks with varying difficulty levels, each axis is independently normalized to its effective range

[10] p: We attribute this vulnerability to a structural flaw in how standard encoders are trained. Conventional end-to-end schemes typically minimize a pixel-wise reconstruction error combined with a message decoding loss. To satisfy the invisibility constraint, the encoder inadvertently learns to hide the watermark signal within the high-frequency textures of the cover image ( Zhang et al., 2020 ) , as the human eye is less sensitive to changes in these complex regions. However, this strategy creates a fatal dependency, i.e., the message becomes entangled with specific local details. As shown in Figure 1 , generative models act as ’manifold projectors’ that specifically synthesize and rewrite these texture regions to improve perceptual quality ( Nie et al., 2022 ) . When the cover image’s texture is regenerated, the spurious correlations between the message and the cover details are severed, thus destroying the watermark.

[11] p: To address this challenge, we propose to explicitly disentangle the watermark from the fragile cover content. Rather than hiding signals in high-frequency textures prone to regeneration, the encoder should anchor the message to the robust semantic structure of the image. Formally, we frame this as learning a Minimal Sufficient Statistic (MSS) of the message with respect to the cover. This objective seeks a representation that retains minimal information about the cover while remaining sufficient for decoding, which we theoretically prove is equivalent to optimizing the Information Bottleneck (IB) principle ( Tishby et al., 2000 ) . Guided by this insight, we introduce WaterVIB, a principled framework that reformulates the watermarking encoder as an information sieve. By minimizing a variational upper bound, WaterVIB forces the model to filter out redundant cover nuances susceptible to generative shifts. This ensures that the model retains only the essential watermark signal that is robust to generative purification. Consequently, this theoretically grounded design enables WaterVIB to achieve superior zero-shot resilience against unknown generative purification, significantly outperforming state-of-the-art methods.

[12] p: Our contributions are summarized as follows:

[13] p: ∙ \bullet We identify the texture entanglement phenomenon as a major cause of failure for existing watermarking methods against generative editing, and introduce WaterVIB framework that leverages the Information Bottleneck principle to learn a robust, disentangled watermark representation.

[14] p: ∙ \bullet We provide a theoretical analysis showing that the learning objective of our WaterVIB framework acts as a necessary condition for robustness against generative variations within our framework.

[15] p: ∙ \bullet Extensive experiments demonstrate that WaterVIB significantly outperforms SOTA baselines, showing superior resilience against both known distortions and unknown generative purification, without specific adversarial training.

[16] h2: 2 Related Works

[17] h3: 2.1 Deep Image Watermarking

[18] p: Traditional watermarking schemes typically embedded signals into specific frequency domains, such as DCT ( Langelaar & Lagendijk, 2001 ) , DWT ( Ganic & Eskicioglu, 2004 ) , or DFT ( Kang et al., 2003 ) , to balance imperceptibility and robustness. The advent of deep learning revolutionized this field by introducing end-to-end optimization pipelines ( Bui et al., 2023 ) . Pioneer works like HiDDeN ( Zhu et al., 2018 ) and StegaStamp ( Tancik et al., 2020 ) utilized encoder-decoder architectures trained with differentiable noise layers. Building on this, recent approaches have integrated GANs and Invertible Neural Networks ( Jing et al., 2021 ) to enhance visual quality and recovery accuracy. To address advanced security threats, state-of-the-art methods have expanded into specialized domains: EditGuard ( Zhang et al., 2024 ) introduces dual watermarks for tamper localization, while NeRF-Signature ( Luo et al., 2025 ) extends embedding capabilities to 3D neural radiance fields.

[19] p: Despite these architectural advancements, most existing methods rely on empirical strategies to train networks against noise without explicitly decoupling the information entanglement between the cover image and the watermark. Consequently, the embedded signals often remain statistically dependent on the cover image redundancies ( Zhang et al., 2020 ) , leading to vulnerability against noise from distribution shifts in specific frequency domains.

[20] h3: 2.2 Information Bottleneck Principle

[21] p: The Information Bottleneck (IB) principle, originally introduced by ( Tishby et al., 2000 ) , formulates representation learning as an optimization trade-off. This theoretical framework was later extended to deep neural networks by ( Alemi et al., 2016 ) , who proposed the Variational Information Bottleneck (VIB). By leveraging variational inference and the reparameterization trick, VIB made the estimation of mutual information bounds computationally tractable for high-dimensional data. Since then, the VIB framework has been successfully applied to diverse domains, ranging from model compression ( Razeghi et al., 2022 ) and interpretability ( Seo et al., 2023 ) to temporal video analysis ( Zhong et al., 2023 ) and large language model alignment ( Yang et al., 2025 ) . Unlike these predominant classification or recognition tasks where the target is a label, we adapt the IB framework to the watermarking channel to construct a signal explicitly decoupled from cover image redundancies. To our knowledge, WaterVIB is the first to rigorously bridge Information-Theoretic Representation Learning and deep generative watermarking.

[22] h2: 3 Theoretical Analysis

[23] p: In this section, we formally characterize the vulnerability of existing watermarking methods under generative purification. We posit that the failure of current methods stems from a distributional entanglement with the cover image’s texture. Consequently, we propose to resolve this conflict by enforcing the Information Bottleneck principle, aiming to approximate the Minimal Sufficient Statistic (MSS) of the message.

[24] figure: Table 1 : Evidence of Signal-Spatial Alignment. Top: Spectral energy distribution shows the AIGC distortion ( s a ​ t ​ k s_{atk} ) targets the same high-frequency bands as the watermark ( δ \delta ). Bottom: Pearson Correlation (PCC) shows the attack is structurally dependent on the cover image, unlike random noise. (a) Spectral Energy Distribution Alignment Signal Component High Freq. Mid Freq. Low Freq. Dominant Watermark Signal ( δ \delta ) 30.20% 45.45% 24.35% Mid-High AIGC Distortion ( s a ​ t ​ k s_{atk} ) 23.36% 20.49% 56.15% Mid-High* Natural Images ( x x ) 1.16% 11.92% 86.91% Low (b) Structural Dependence (PCC with Cover Image) Target Signal Pearson Correlation Coefficient Interpretation AIGC Distortion ( s a ​ t ​ k s_{atk} ) 0.5989 Content-Dependent Watermark Signal ( δ \delta ) 0.4535 Entangled Random Noise ( n n ) -0.0003 Independent

[25] h3: 3.1 Analysis of Vulnerability

[26] p: Let 𝒳 ⊆ ℝ H × W × C \mathcal{X}\subseteq\mathbb{R}^{H\times W\times C} be the image space and ℳ \mathcal{M} be the message space. A standard encoder E : 𝒳 × ℳ → 𝒳 E:\mathcal{X}\times\mathcal{M}\to\mathcal{X} produces a watermarked image x w ​ m = x + δ x_{wm}=x+\delta . Unlike traditional additive noise, we model Generative Purification as a projection operator onto the natural image space. Let p d ​ a ​ t ​ a ​ ( x ) p_{data}(x) be the natural image distribution. The purification process G : 𝒳 → 𝒳 G:\mathcal{X}\to\mathcal{X} projects x w ​ m x_{wm} onto the high-density region of p d ​ a ​ t ​ a p_{data} by minimizing a perceptual distance d ⁡ ( ⋅ , ⋅ ) d(\cdot,\cdot) :

[27] table: x r ​ e ​ c = 𝒢 ⁡ ( x w ​ m ) ≈ arg ⁡ min x ′ ∈ supp ​ ( p d ​ a ​ t ​ a ) ⁡ d ⁡ ( x ′ , x w ​ m ) . x_{rec}=\mathcal{G}(x_{wm})\approx\arg\min_{x^{\prime}\in\text{supp}(p_{data})}d(x^{\prime},x_{wm}). (1)

[28] p: Current methods implicitly assume the watermark signal δ \delta resides in a subspace orthogonal to the semantic content. However, we propose that generative models preferentially reconstruct low-frequency semantics while rewriting high-frequency textures where δ \delta resides.

[29] p: Empirical Validation. We validate Observation 3.1 via spectral analysis and Pearson Correlation Coefficient (PCC). As reported in Table 1 (a) , the watermark signal(EditGuard, Zhang et al. (2024) ) concentrates 75.65 % 75.65\% of its energy in Mid-High frequencies. Meanwhile, the AIGC distortion s a ​ t ​ k s_{atk} effectively targets these same bands ( 43.85 % 43.85\% energy), unlike natural images. Furthermore, Table 1 (b) shows a high spatial correlation between the distortion and the cover image ( ρ ≈ 0.60 \rho\approx 0.60 ), implying that the attack is content-dependent.

[30] h3: 3.2 Gradient Counter-Optimization

[31] p: The alignment described in Proposition 3.1 leads to a direct interference with the decoding objective. Let ℒ ⁡ ( ⋅ ) \mathcal{L}(\cdot) be the decoding loss, which is the BCE loss between the target message 𝐦 \mathbf{m} and the extracted message ( Sander et al., 2025 ) .

[32] p: Proof. Consider the watermarked image 𝐱 w ​ m = 𝐱 c ​ o ​ v ​ e ​ r + 𝐬 w ​ m \mathbf{x}_{wm}=\mathbf{x}_{cover}+\mathbf{s}_{wm} , and the AIGC purified image 𝐱 a ​ t ​ k = 𝐱 w ​ m + 𝐬 a ​ t ​ k \mathbf{x}_{atk}=\mathbf{x}_{wm}+\mathbf{s}_{atk} . Assuming ℒ \mathcal{L} is differentiable, we apply a first-order Taylor expansion to the loss ℒ ⁡ ( 𝐱 a ​ t ​ k ) \mathcal{L}(\mathbf{x}_{atk}) around 𝐱 w ​ m \mathbf{x}_{wm} :

[33] table: ℒ ⁡ ( 𝐱 a ​ t ​ k ) ≈ ℒ ⁡ ( 𝐱 w ​ m ) + 𝐬 a ​ t ​ k ⊤ ​ ∇ 𝐱 ℒ ​ ( 𝐱 w ​ m ) \mathcal{L}(\mathbf{x}_{atk})\approx\mathcal{L}(\mathbf{x}_{wm})+\mathbf{s}_{atk}^{\top}\nabla_{\mathbf{x}}\mathcal{L}(\mathbf{x}_{wm}) (2)

[34] p: Since the encoder minimizes ℒ \mathcal{L} , the gradient ∇ x ℒ \nabla_{x}\mathcal{L} points in the direction of increasing decoding error. Consequently, if the projection of the attack vector s a ​ t ​ k s_{atk} onto the gradient is positive, the loss increases and signifies a successful attack.

[35] p: Empirical Validation. We quantify this interference through the scalar projections of both the watermark and AIGC distortion onto the gradient direction in Table 2 . While the watermark signal δ \delta naturally has a negative projection ( − 0.063 -0.063 ) to minimize loss, the AIGC distortion s a ​ t ​ k s_{atk} shows a significant positive projection ( + 0.027 +0.027 ). This confirms Lemma 3.2 where generative purification acts as an adversarial attack, canceling out ≈ 42.9 % \approx 42.9\% of the optimization effort.

[36] figure: Table 2 : Gradient Counter-Optimization Analysis. We project the signals onto the loss gradient direction ∇ x ℒ \nabla_{x}\mathcal{L} . A negative projection implies loss minimization, while a positive projection implies loss maximization. Vector Component Projection Value Direction Effect on Decoding Gradient Direction ( ∇ x ℒ \nabla_{x}\mathcal{L} ) N/A Target N/A Watermark Signal ( δ \delta ) − 0.063 -0.063 Anti-Gradient Minimizes Error AIGC Distortion ( s a ​ t ​ k s_{atk} ) + 0.027 \mathbf{+0.027} Gradient Maximizes Error

[37] h3: 3.3 Minimal Sufficient Statistic

[38] p: The analysis in Section 3.2 reveals that the vulnerability of current watermarks stems from their dependency on the high-frequency textures of the cover image X X . Since generative purification G ⁡ ( ⋅ ) G(\cdot) acts as a manifold projection that rewrites these textures based on the prior p d ​ a ​ t ​ a ​ ( x ) p_{data}(x) , any watermark signal entangled with X X is inevitably corrupted. To defend against this, we seek a representation Z Z that is disentangled from the cover 𝐱 \mathbf{x} details while remaining predictive of the message M M . Specifically, we formulate the watermark extraction process not merely as signal recovery, but as extracting the Minimal Sufficient Statistic (MSS) of the message from the watermarked content.

[39] p: (1) Sufficiency (Robustness). To ensure feasible decoding, Z Z must capture all information necessary to decode M M :

[40] table: I ⁡ ( Z , M ) = I ⁡ ( X , M ) . I(Z;M)=I(X;M). (3)

[41] p: (2) Minimality (Disentanglement). To evade texture-biased purification, Z Z must strip away nuisance cover textures by minimizing information about X X :

[42] table: I ⁡ ( Z , X ) ≤ I ⁡ ( Z ~ , X ) , ∀ Z ~ ​ s.t. ​ I ​ ( Z ~ , M ) = I ⁡ ( X , M ) . I(Z;X)\leq I(\tilde{Z};X),\;\forall\tilde{Z}\text{ s.t. }I(\tilde{Z};M)=I(X;M). (4)

[43] p: The theoretical justification for imposing these constraints is established by the following theorem.

[44] p: Proof. We provide the rigorous derivation in Appendix A .

[45] p: However, direct computation of the MSS is intractable in high-dimensional spaces. We therefore relax the strict sufficiency constraint to an ϵ \epsilon -approximate version:

[46] table: min p ⁡ ( z | x ) \displaystyle\min_{p(z|x)} I ⁡ ( Z , X ) \displaystyle I(Z;X) (5) s.t. \displaystyle\text{s.t.} I ⁡ ( Z , M ) ≥ I ⁡ ( X , M ) − ϵ . \displaystyle I(Z;M)\geq I(X;M)-\epsilon.

[47] p: Leveraging the convexity of mutual information (see Appendix B ), we apply Lagrange multipliers to transform this into the unconstrained Information Bottleneck (IB) objective with β ⁡ ( ϵ ) > 0 \beta(\epsilon)>0 :

[48] table: max p ⁡ ( z | x ) ⁡ ℒ I ​ B = I ⁡ ( Z , M ) − β ​ I ​ ( Z , X ) \max_{p(z|x)}\mathcal{L}_{IB}=I(Z;M)-\beta I(Z;X) (6)

[49] p: Here, maximizing I ⁡ ( Z , M ) I(Z;M) ensures the robustness of the watermark ( sufficiency ), while minimizing I ⁡ ( Z , X ) I(Z;X) enforces disentanglement ( minimality ), explicitly filtering out the texture of the cover prone to generative purification.

[50] h2: 4 Approach

[51] figure: Figure 2 : The WaterVIB Architecture. We propose a Stochastic Information Sieve mechanism (Part 2) to defend against generative purification (Part 1). By injecting noise via a learnable bottleneck layer, WaterVIB penalizes the retention of cover-specific details ( I ⁡ ( Z , X ) I(Z;X) ) via the Information Bottleneck principle. This explicitly disentangles the watermark signal from the cover texture, yielding a stochastic representation 𝐔 \mathbf{U} that is invariant to the semantic projections performed by diffusion models.

[52] p: We operationalize the theoretical MSS objective by instantiating the WaterVIB framework. Unlike standard deterministic encoders, we introduce a novel stochastic bottleneck layer that functions as a differentiable information sieve , explicitly filtering out fragile redundancies via the variational bounds derived below.

[53] h3: 4.1 Variational Lower Bounds

[54] p: Direct computation of the mutual information terms in ℒ I ​ B \mathcal{L}_{IB} 6 is intractable. We therefore employ variational inference to derive differentiable bounds for both components.

[55] p: Maximizing Relevance ( ℒ r ​ e ​ c \mathcal{L}_{rec} ). Maximizing I ⁡ ( Z , M ) I(Z;M) minimizes the conditional entropy H ⁡ ( M | Z ) H(M|Z) . We parameterize the posterior directly via the decoder. Treating the message as a vector 𝐦 ∈ { 0 , 1 } L \mathbf{m}\in\{0,1\}^{L} and the prediction as 𝐦 ^ \hat{\mathbf{m}} , we derive the Binary Cross-Entropy (BCE) loss:

[56] table: ℒ r ​ e ​ c \displaystyle\mathcal{L}_{rec} = 𝔼 p ⁡ ( z , 𝐦 ) ​ [ − log ⁡ p ⁡ ( 𝐦 | z ) ] \displaystyle=\mathbb{E}_{p(z,\mathbf{m})}\left[-\log p(\mathbf{m}|z)\right] (7) = 𝔼 ⁡ [ − 𝐦 ⊤ ​ log ⁡ 𝐦 ^ − ( 𝟏 − 𝐦 ) ⊤ ​ log ⁡ ( 𝟏 − 𝐦 ^ ) ] \displaystyle=\mathbb{E}\left[-\mathbf{m}^{\top}\log\hat{\mathbf{m}}-(\mathbf{1}-\mathbf{m})^{\top}\log(\mathbf{1}-\hat{\mathbf{m}})\right]

[57] p: Minimizing Compression ( ℒ K ​ L \mathcal{L}_{KL} ). We minimize the compression term I ⁡ ( Z , X ) I(Z;X) by optimizing its variational upper bound derived from the VIB framework ( Alemi et al., 2016 ) . Specifically, we introduce a fixed prior r ⁡ ( z ) r(z) (e.g., 𝒩 ⁡ ( 0 , I ) \mathcal{N}(0,I) ) to approximate the intractable marginal p ⁡ ( z ) p(z) :

[58] table: I ⁡ ( Z , X ) \displaystyle I(Z;X) = 𝔼 x [ D K ​ L ( p θ ( z | x ) ∥ p ( z ) ) ] \displaystyle=\mathbb{E}_{x}\left[D_{KL}(p_{\theta}(z|x)\|p(z))\right] = 𝔼 x ​ [ ∫ p θ ​ ( z | x ) ​ log ⁡ p θ ​ ( z | x ) r ⁡ ( z ) ​ 𝑑 z ] − D K ​ L ( p ( z ) ∥ r ( z ) ) ⏟ ≥ 0 \displaystyle=\mathbb{E}_{x}\left[\int p_{\theta}(z|x)\log\frac{p_{\theta}(z|x)}{r(z)}dz\right]-\underbrace{D_{KL}(p(z)\|r(z))}_{\geq 0} ≤ 𝔼 x [ D K ​ L ( p θ ( z | x ) ∥ r ( z ) ) ] ≜ ℒ K ​ L \displaystyle\leq\mathbb{E}_{x}\left[D_{KL}(p_{\theta}(z|x)\|r(z))\right]\triangleq\mathcal{L}_{KL} (8)

[59] p: The final training objective combines these terms:

[60] table: ℒ t ​ o ​ t ​ a ​ l = ℒ r ​ e ​ c + β ​ ℒ K ​ L \mathcal{L}_{total}=\mathcal{L}_{rec}+\beta\mathcal{L}_{KL} (9)

[61] h3: 4.2 Stochastic Bottleneck Implementation

[62] p: To implement the probabilistic encoder p θ ​ ( z | x ) p_{\theta}(z|x) within a deterministic deep neural network, we construct a stochastic layer U ⁡ ( Z ) U(Z) (Figure 2 ), where Z = E d ​ e ​ t ​ ( X ) Z=E_{det}(X) denote the deterministic features extracted by the backbone encoder.

[63] p: Standard backpropagation cannot flow through random sampling. To resolve this, we employ the reparameterization trick ( Kingma & Welling, 2013 ) . Furthermore, to control the variance magnitude and stabilize the adversarial training process involving watermarks, we introduce a scaling factor α \alpha . The latent variable U U is sampled as:

[64] table: U = μ ⁡ ( Z ) + α ⋅ ϵ ⊙ σ ⁡ ( Z ) , ϵ ∼ 𝒩 ⁡ ( 0 , I ) U=\mu(Z)+\alpha\cdot\epsilon\odot\sigma(Z),\quad\epsilon\sim\mathcal{N}(0,I) (10)

[65] p: where ϵ \epsilon is sampled from a standard normal distribution. This formulation allows gradients to propagate deterministically through μ \mu and σ \sigma while isolating the stochasticity in ϵ \epsilon .

[66] p: Specifically, we derive the distributional parameters μ ⁡ ( Z ) \mu(Z) and σ ⁡ ( Z ) \sigma(Z) by projecting the deterministic features Z Z through two parallel Multi-Layer Perceptrons (MLPs) :

[67] table: μ ⁡ ( Z ) = MLP μ ​ ( Z ) , σ ⁡ ( Z ) = exp ⁡ ( 1 2 ​ MLP σ ​ ( Z ) ) \mu(Z)=\text{MLP}_{\mu}(Z),\quad\sigma(Z)=\exp\left(\frac{1}{2}\text{MLP}_{\sigma}(Z)\right) (11)

[68] p: The reconstruction head then decodes the message M ′ M^{\prime} solely from the compressed stochastic representation U U , forcing the network to retain only the robust, minimal sufficient statistics of the watermark.

[69] p: Training vs. Inference. To enforce the IB constraint, we employ the stochastic sampling mechanism in ( 10 ) during training, which encourages the filtration of redundant entangled signals. At inference time, we replace this with a deterministic mapping U = μ ⁡ ( Z ) U=\mu(Z) to prevent stochastic fluctuations.

[70] h2: 5 Evaluation

[71] h3: 5.1 Experimental Setup

[72] p: Datasets and Models. Following ( Zhu et al., 2018 ; Zhang et al., 2024 ) , we utilize COCO ( Lin et al., 2014 ) for training. For evaluation, we employ both the standard COCO test set and the AGE-Set ( Zhang et al., 2024 ) to strictly assess zero-shot robustness against AIGC manipulation. To demonstrate universality, we integrate WaterVIB into two representative backbones: HiDDeN (lightweight) ( Zhu et al., 2018 ) and EditGuard ( Zhang et al., 2024 ) (high-capacity SOTA). We benchmark performance against methods including TrustMark ( Bui et al., 2023 ) , WM-A ( Sander et al., 2025 ) , DWT-DCT-SVD ( Kang et al., 2003 ) , and so on.

[73] p: Attacks and Metrics. We evaluate robustness against two categories of distortions: (1) Standard Noises (e.g., JPEG, Crop, Resize, Dropout) ( Zhu et al., 2018 ) , and (2) Generative Purification, simulated via diffusion ( Nie et al., 2022 ) pipelines (e.g., SD-Inpaint, DiffPure) to effectively rewrite image content. We report Bit Error Rate (BER) to measure watermark survival, PSNR and SSIM to quantify visual imperceptibility.

[74] p: VIB Settings. We implement the WaterVIB module as a plug-and-play stochastic layer tailored to each backbone.

[75] p: For the high-capacity EditGuard , we insert a CNN-based VIB module after the 16-channel bit decoder output. To handle high-dimensional features, we employ a channel-reduction pipeline ( C ​ o ​ n ​ v 16 → 4 → C ​ o ​ n ​ v 4 → 2 Conv_{16\rightarrow 4}\rightarrow Conv_{4\rightarrow 2} ) to parameterize the stochastic latent U U . We set α = 10 − 4 \alpha=10^{-4} and β = 0.0003 \beta=0.0003 .

[76] p: For the lightweight HiDDeN , the VIB module is integrated via a Multi-Layer Perceptron (MLP) structure between the feature extractor and the readout layer, utilizing a latent dimension of D = 128 D=128 . The hyperparameters are set to α = 0.007 \alpha=0.007 and β = 0.00015 \beta=0.00015 . Detailed network architectures, layer configurations, and specific implementation parameters are provided in Appendix C .

[77] h3: 5.2 Zero-Shot Resilience to AIGC Manipulation

[78] figure: Table 3 : Zero-shot Robustness against Generative Editing. Evaluation under (I) Local Editing and (II) Global Purification. The reported metric is Bit Error Rate (BER). Red. denotes the relative reduction in error rate. Attack Method EditGuard +VIB (Ours) Red. (I) Local Editing (BER ‰) SD-Inpainting 0.35 0.03 91% ControlNet-Inp. 0.13 0.14 -7% SDXL-Refiner 0.30 0.03 90% RePaint 0.26 0.08 69% (II) Global Purification (BER %) SD-v1.5 48.55 38.34 21% SD-2-Inpainting 48.69 35.21 28% ControlNet-Inp. 48.85 38.41 21% DDPM-CelebA-HQ 61.45 20.20 67% SDXL 25.90 14.62 44% SDXL-Inpainting 25.79 13.19 49% Attack strength settings: SD-v1.5 / SD-2 / ControlNet / DDPM: 0.002 0.002 ; SDXL / SDXL-Inpainting: 0.05 0.05 . PSNR is around 30db for SD 2.0 Purification and 16db for SD 1.5 ones

[79] p: To verify the defense against Generative Purification , we evaluate the models under two distinct zero-shot threat models: Localized Semantic Editing and Global Generative Purification . The results are summarized in Table 3 .

[80] p: On the AGE-Set localized AIGC tampering dataset ( Zhang et al., 2024 ) , integrating WaterVIB suppresses the average BER from 0.26‰to 0.07‰ , achieving a 73% relative reduction . Specifically, against powerful generators like SD-Inpainting ( Rombach et al., 2022 ) and SDXL-Refiner ( Podell et al., 2023 ) , WaterVIB reduces the error rate by over 90%. Furthermore, our method demonstrates consistent generalization across diverse architectures, maintaining robust extractability on RePaint ( Lugmayr et al., 2022 ) and ControlNet-Inpainting ( Zhang et al., 2023 ) .

[81] p: We further evaluate robustness under global AIGC purification using a diverse set of generative models. As shown in Table 3 , global reconstruction substantially degrades the baseline across all models, with BER ranging from 25% to over 60%. EditGuard-VIB consistently reduces BER, achieving up to 67% relative improvement under pixel-space DDPM and nearly 50% under strong SDXL-based purification.

[82] p: We note that the relatively high BER on SD-v1.5 is primarily caused by its limited reconstruction fidelity (PSNR ≈ \approx 15 dB), which induces severe pixel-level distortions and consequently strong watermark corruption. This behavior is expected for text-conditioned latent diffusion models optimized for perceptual realism rather than pixel accuracy.

[83] h3: 5.3 Robustness against Standard Distortions

[84] p: While our primary focus is generative defense, an ideal watermarking scheme must also excel at standard signal processing benchmarks. In this section, we verify the efficacy of WaterVIB across both high-capacity and lightweight architectures.

[85] figure: Table 4 : Comparison with SOTA on Standard Distortions. Evaluation on EditGuard(+VIB) architecture. We report PSNR (dB) for imperceptibility and Bit Error Rate (BER %) for robustness. Method Payload PSNR ↑ \uparrow Clean ‰ ↓ \downarrow Noise ‰ ↓ \downarrow DWT-DCT 100 bits 38.1 0.56 10.84 TrustMark 100 bits 42.3 1.00 6.60 WM-A 30 bits 38.6 0.63 140.20 EditGuard 100 bits 40.4 0.05 3.21 +VIB (Ours) 100 bits 40.3 0.03 0.08

[86] p: High-Capacity SOTA Comparison. We benchmark EditGuard-VIB against recent SoTA methods. As shown in Table 4 , under random attacks (specifically Gaussian, Poisson, and JPEG), integrating WaterVIB reduces the BER from 3.21‰to 0.08‰ . This performance consistently outperforms current SOTA models, including TrustMark ( Bui et al., 2023 ) (6.60% BER) and WM-A ( Sander et al., 2025 ) .

[87] figure: Table 5 : Detailed Robustness Analysis (EditGuard). Comparison of Bit Error Rate (BER %). Red. denotes the relative reduction in error rate. Distortion Type Baseline +VIB(Ours) Red. Gaussian Noise‰ 0.09 0.01 89% JPEG ‰ 9.61 0.40 96% Poisson Noise‰ 0.01 0.02 - Cropout% 29.61 32.82 - Dropout% 9.11 4.50 51% Resize (Scaling)% 81.75 0.01 99.99% Combined Average% 20.24 6.23 69%

[88] p: As detailed in Table 5 , the baseline suffers a catastrophic collapse under Resize (81.75% BER), betraying its dependency on position-specific pixel grids. WaterVIB virtually eliminates this vulnerability ( 0.01% BER), confirming that the information bottleneck enforces strict invariance to grid resampling.

[89] figure: Table 6 : Universality on Lightweight Models (HiDDeN). Evaluation on HiDDeN (30 bits). We report PSNR (dB) and Bit Error Rate (BER %). Red. denotes the relative reduction in error rate. Note the significant improvements across structural (Resize/Cropout) and adversarial attacks. Metric Baseline +VIB(Ours) Red. (I) Visual Quality & Clean Accuracy PSNR (dB) ↑ \uparrow 36.5 37.0 - SSIM ↑ \uparrow 0.97 0.97 - Clean BER (%) 9.92 9.54 4% (II) Standard Distortions Crop (0.5) 10.37 9.76 6% Cropout (0.3) 24.95 9.69 61% Dropout (0.3) 16.10 12.46 23% JPEG 29.01 12.45 57% Resize (Scaling) 32.04 12.93 60% Combined Average 20.92 13.02 38% (III) Complex & Adversarial Attacks Geometric † 24.00 15.00 38 % Color Space (YUV) 16.00 11.00 31% Frequency (DWT) 44.00 39.00 11% Adversarial (PGD) 76.00 30.00 61% † Rot+Scale+Trans+Shear.

[90] p: Robustness on Lightweight Models. To demonstrate universality, we evaluate WaterVIB on the lightweight HiDDeN architecture. As detailed in Table 6 , WaterVIB exhibits particular resilience against distribution-shifting distortions , such as complex geometric attacks ( Red. 38% ) and JPEG compression ( Red. 57% ). This strong generalization capability extends even to aggressive PGD adversarial perturbations, where WaterVIB prevents the baseline’s collapse (76.0% → \to 30.0% BER). Collectively, these findings validate that the VIB module acts as a potent regularizer for parameter-constrained networks, forcing them to capture robust semantics rather than overfitting to fragile details.

[91] h3: 5.4 Analysis of the Information Sieve Mechanism

[92] p: To uncover the underlying mechanisms of WaterVIB’s robustness, we visualize the feature space shifts under AIGC tampering and further quantify the gradient interference. This analysis confirms that WaterVIB effectively resolves the theoretical vulnerabilities identified in Section 3 .

[93] p: Feature Space Invariance (t-SNE). We first verify whether the Information Sieve successfully disentangles the watermark from fragile cover distortions. We randomly select 10 watermark messages and embed each into 20 distinct cover images. We then visualize the latent representations extracted by the decoder for these samples using t-SNE. In Figure 3 , we project both the clean samples and their corresponding AIGC-purified counterparts into the same 2D embedding space.

[94] p: As shown in Figure 3 (Top), the baseline exhibits a severe distribution shift . While clean samples form distinct clusters, the purified samples (triangles) drift significantly away from their class centers and converge into a new cluster, indicating that the encoder relies on texture-dependent features that are effectively rewritten by the generative editing process.

[95] p: In contrast, WaterVIB (Bottom) demonstrates remarkable manifold invariance . The attacked samples remain tightly clustered with their corresponding clean anchors. This qualitative result confirms that the VIB module filters out the “nuisance” variability, forcing the model to learn a MSS representation that is structurally invariant to regeneration.

[96] figure: Figure 3 : Feature Space Visualization (t-SNE). We visualize the latent embeddings of 10 random messages (different colors), each embedded into 20 cover images. In the Baseline (EditGuard), attacked samples (triangles) undergo significant feature drift, collapsing toward a shared manifold region regardless of their original message identity, which leads to high bit error rates. (b) With our WaterVIB, the drift paths (lines) are significantly reduced, and attacked samples remain anchored within the high-density clusters of their respective clean counterparts.

[97] p: Mitigating Gradient Interference. We further provide a quantitative explanation based on the “Gradient Counter-Optimization” theory proposed in Section 3.2 . We measure the Gradient Interference Ratio ( ρ \rho ) , defined as the ratio between the projection of the attack distortion s a ​ t ​ k s_{atk} and the watermark signal s w ​ m s_{wm} onto the decoding gradient ∇ x ℒ \nabla_{x}\mathcal{L} :

[98] table: ρ = ⟨ s a ​ t ​ k , ∇ x ℒ ⟩ | ⟨ s w ​ m , ∇ x ℒ ⟩ | \rho=\frac{\langle s_{atk},\nabla_{x}\mathcal{L}\rangle}{|\langle s_{wm},\nabla_{x}\mathcal{L}\rangle|} (12)

[99] p: A higher ρ \rho implies that generative purification acts as a stronger adversarial attack that cancels out more watermark signal.

[100] figure: Table 7 : Gradient Interference Analysis. Comparison of the Gradient Interference Ratio ( ρ \rho ). Lower is better. Method EditGuard +VIB (Ours) Red. Ratio ρ \rho ↓ \downarrow 0.4285 0.1167 73%

[101] p: As reported in Table 7 , the baseline suffers from high interference ( ρ ≈ 0.43 \rho\approx 0.43 ), confirming that purification acts as a direct adversarial update. In contrast, WaterVIB suppresses this ratio by 73% (to 0.1167). This validates that the Information Sieve forces the watermark into a latent subspace that achieves quasi-orthogonality relative to the purification trajectory, thereby effectively mitigating the “Gradient Counter-Optimization” effect at a structural level.

[102] p: More details are presented in Appendix E

[103] h3: 5.5 Training Dynamics and Generalization

[104] p: To further verify the regularization effect of WaterVIB, we analyze the learning curves and the behavior of the regularization term L KL L_{\textbf{KL}} during training. Figure 4 visualizes the Train vs. Val Loss for both the Baseline and WaterVIB.

[105] p: Reduced Generalization Gap. We observe that the baseline’s embedding intensity and decoding accuracy on the validation set is consistently lower than its training performance (Figure 4 red). We attribute this to the model’s embedding strategy overfitting to the specific textures and local patterns of the training set. Consequently, when deployed on unseen test data, these novel textures confuse the model, leading to a significant drop in encoder intensity and a corresponding increase in decoder gap loss. In contrast, WaterVIB significantly avoids dependency on specific textures, making the model’s performance more stable. This phenomenon validates our design objective, confirming that the watermarking strategy reduces its reliance on original cover textures and leads to superior generalization performance.

[106] p: Stable Compression. The KL divergence ( L K ​ L L_{KL} ) stabilizes at ≈ 0.0005 \approx\textbf{0.0005} after 20 epochs. This numerical stability indicates that the VIB module exerts constant regularization pressure, consistently filtering out task-irrelevant features.

[107] figure: Figure 4 : Generalization Gap Analysis. We evaluate the training dynamics by plotting the ratio of validation loss to training loss ( ℒ val / ℒ train \mathcal{L}_{\text{val}}/\mathcal{L}_{\text{train}} ) across epochs. A ratio significantly greater than 1 1 indicates overfitting. The plots correspond to the Encoder (top), Decoder (middle), and Total Loss (bottom).

[108] h3: 5.6 Hyperparameter Ablation

[109] p: As formally proven in Appendix B , the hyperparameter β \beta determines the compression rate of the Information Sieve. It effectively sets the “aperture” of the bottleneck: a higher β \beta enforces a stricter constraint, compelling the encoder to discard more task-irrelevant information. To empirically determine the optimal operating point, we conducted a systematic ablation study on the HiDDeN backbone.

[110] p: Figure 5 visualizes the results, where we treat the standard HiDDeN model as the unconstrained special case ( β = 0 \beta=0 ). As shown in the plot, the performance exhibits a distinct non-monotonic “U-shaped” pattern .

[111] p: Transition from Baseline ( β = 0 → 1.5 × 10 − 4 \beta=0\to 1.5{\times}10^{-4} ): Initially, increasing β \beta significantly drops the BER from the baseline’s 20.93% to a minimum of 11.59% . This 45% reduction confirms that introducing the VIB constraint successfully filters out redundant, texture-dependent features that are vulnerable to generative attacks.

[112] p: Over-compression ( β > 2.0 × 10 − 4 \beta>2.0{\times}10^{-4} ): However, beyond the optimal point, the bottleneck becomes excessively tight. The penalty on mutual information I ⁡ ( Z , X ) I(Z;X) begins to discard essential watermark signals, causing the BER to rise sharply.

[113] p: This analysis identifies β ≈ 1.5 × 10 − 4 \beta\approx 1.5{\times}10^{-4} as the “sweet spot” that optimally balances feature minimality with information sufficiency, with the method consistently outperforming the baseline across the entire stable range.

[114] figure: 0 1 × 10 − 4 1{\times}10^{-4} 2 × 10 − 4 2{\times}10^{-4} 3 × 10 − 4 3{\times}10^{-4} 10 10 12 12 14 14 16 16 18 18 20 20 22 22 Baseline (HiDDeN) Optimal β \beta ( − 45 % -45\% Error) Bottleneck Capacity β \beta Bit Error Rate (BER) % WaterVIB Figure 5 : Impact of β \beta on Robustness. We plot the BER under AIGC purification as a function of β \beta . The Baseline coresponds to β = 0 \beta=0 . The curve reveals a distinct “sweet spot” at β = 0.00015 \beta=0.00015 .

[115] h2: 6 Conclusion

[116] p: In this work, we identify feature entanglement as the critical failure mode of deep watermarking under generative purification. To resolve this, we bridge the gap between robust watermarking and Information-Theoretic Representation Learning. We prove that optimizing the Information Bottleneck objective is equivalent to learning a Minimal Sufficient Statistic (MSS) of the message within our framework, which constitutes a necessary condition for disentangling the watermark from fragile cover textures. By operationalizing this theory via WaterVIB, we achieve SoTA zero-shot robustness against a wide spectrum of unknown AIGC purifications. Crucially, Our results substantiate that the VIB framework constitutes a potent defense paradigm against zero-shot attacks. Our work suggests that future defenses should move beyond heuristic noise layers toward theoretically grounded, semantic-invariant representation learning.

[117] h2: Impact Statement

[118] p: This paper presents WaterVIB, a robust watermarking framework designed to safeguard intellectual property and ensure content provenance in the era of generative AI. Our work aims to empower creators by providing a defense against unauthorized manipulation and erasure of copyright information. While watermarking technologies inherently carry potential risks related to user tracking or surveillance if misused, our research focuses strictly on the robustness of signal retention for ownership verification. We are committed to the ethical development of these tools and advocate for their use solely in protecting legitimate copyright and ensuring digital authenticity.

[119] h2: References

[120] h2: Appendix A Theoretical Equivalence to Classical Minimal Sufficient Statistics

[121] p: In this section, we provide a rigorous justification for our information-theoretic definition of the Minimal Sufficient Statistic (MSS). Under the assumption that the representation mapping T ⁡ ( ⋅ ) T(\cdot) is a deterministic function (consistent with neural network inference) and the data is defined on discrete domains , we demonstrate a bidirectional equivalence between the classical definition of MSS grounded in the Lehmann-Scheffé theory ( Lehmann & Scheffé, 2011 ) and the proposed information-theoretic formulation.

[122] h3: A.1 Preliminaries

[123] p: We consider the standard supervised setting for watermark extraction defined over discrete alphabets:

[124] p: Message (Target): M ∼ p ⁡ ( m ) M\sim p(m) , representing the discrete watermark message.

[125] p: Observation (Data): X ∼ p ⁡ ( x | m ) X\sim p(x|m) , representing the watermarked image (discrete random variable, e.g., digitized pixels).

[126] p: Statistic (Representation): Let Z Z be a statistic of X X , defined as a deterministic function Z = T ⁡ ( X ) Z=T(X) .

[127] p: We assume the data generation and feature extraction process follows a Markov Chain:

[128] table: M → X → Z M\to X\to Z (13)

[129] h3: A.2 Classical Statistical Definitions

[130] p: We first restate the foundational definitions from classical mathematical statistics adapted for discrete variables.

[131] p: Definition 1 (Sufficiency). A statistic T ⁡ ( X ) T(X) is sufficient for M M if the conditional distribution of X X given T ⁡ ( X ) T(X) is independent of M M . That is, for all x , t , m x,t,m :

[132] table: p ⁡ ( x | t , m ) = p ⁡ ( x | t ) p(x|t,m)=p(x|t) (14)

[133] p: Definition 2 (Minimal Sufficiency via Lehmann-Scheffé). A sufficient statistic T ⁡ ( X ) T(X) is called a Minimal Sufficient Statistic (MSS) if, for any other sufficient statistic S ⁡ ( X ) S(X) , T ⁡ ( X ) T(X) is a function of S ⁡ ( X ) S(X) . That is, there exists a function f f such that:

[134] table: T ⁡ ( X ) = f ⁡ ( S ⁡ ( X ) ) almost surely. T(X)=f(S(X))\quad\text{almost surely.} (15)

[135] p: This definition implies that the MSS induces the coarsest sufficient partition of the sample space.

[136] h3: A.3 Information-Theoretic Foundations

[137] p: To prove the main theorems, we first establish precise properties of deterministic functions and sufficiency using entropy and mutual information definitions for discrete variables.

[138] p: Proposition 1 (Vanishing Conditional Entropy for Deterministic Functions). For any discrete random variable X X and a deterministic function T ⁡ ( ⋅ ) T(\cdot) , the conditional entropy H ⁡ ( T ⁡ ( X ) | X ) H(T(X)|X) is zero.

[139] p: Proof. Let Z = T ⁡ ( X ) Z=T(X) . By the definition of conditional entropy for discrete variables:

[140] table: H ( Z | X ) = − ∑ x ∈ 𝒳 p ( x ) ∑ z ∈ 𝒵 p ( z | x ) log p ( z | x ) H(Z|X)=-\sum_{x\in\mathcal{X}}p(x)\sum_{z\in\mathcal{Z}}p(z|x)\log p(z|x) (16)

[141] p: Since T T is a deterministic function, the conditional probability mass function p ⁡ ( z | x ) p(z|x) is an indicator function: it equals 1 if z = T ⁡ ( x ) z=T(x) and 0 otherwise. The entropy of a deterministic event is zero ( − 1 ​ log ⁡ 1 = 0 -1\log 1=0 ). Thus, the inner sum vanishes for all x x :

[142] table: ∑ z ∈ 𝒵 p ⁡ ( z | x ) ​ log ⁡ p ⁡ ( z | x ) = 0 \sum_{z\in\mathcal{Z}}p(z|x)\log p(z|x)=0 (17)

[143] p: Averaging over p ⁡ ( x ) p(x) preserves this zero value, yielding H ⁡ ( Z | X ) = 0 H(Z|X)=0 . □ \square

[144] p: Proposition 2 (Equivalence of Conditional Independence and Zero Information). The random variables X X and M M are conditionally independent given T ⁡ ( X ) T(X) if and only if the conditional mutual information I ⁡ ( M ; X | T ⁡ ( X ) ) I(M;X|T(X)) is zero.

[145] p: Proof. The conditional mutual information is defined as the expected Kullback-Leibler (KL) divergence:

[146] table: I ( M ; X | T ) = 𝔼 t [ D K ​ L ( p ( m , x | t ) ∥ p ( m | t ) p ( x | t ) ) ] I(M;X|T)=\mathbb{E}_{t}\left[D_{KL}(p(m,x|t)\|p(m|t)p(x|t))\right] (18)

[147] p: Direction ( ⇒ \Rightarrow ): If X X and M M are conditionally independent given T T , then p ⁡ ( m , x | t ) = p ⁡ ( m | t ) ​ p ​ ( x | t ) p(m,x|t)=p(m|t)p(x|t) . The KL divergence between two identical distributions is zero, thus the term vanishes.

[148] p: Direction ( ⇐ \Leftarrow ): A fundamental property of KL divergence (Gibbs’ Inequality) states that D K ​ L ( P ∥ Q ) ≥ 0 D_{KL}(P\|Q)\geq 0 , with equality if and only if P = Q P=Q . Therefore, if I ⁡ ( M ; X | T ) = 0 I(M;X|T)=0 , it implies p ⁡ ( m , x | t ) = p ⁡ ( m | t ) ​ p ​ ( x | t ) p(m,x|t)=p(m|t)p(x|t) for all ( m , x , t ) (m,x,t) with non-zero probability. This factorization is the definition of conditional independence. □ \square

[149] p: Theorem 1 (Information-Theoretic Criterion for Sufficiency). A statistic T ⁡ ( X ) T(X) is sufficient for M M if and only if it preserves the mutual information between the input and the target:

[150] table: I ⁡ ( M , T ⁡ ( X ) ) = I ⁡ ( M , X ) I(M;T(X))=I(M;X) (19)

[151] p: Proof. We analyze the joint mutual information I ⁡ ( M , X , T ⁡ ( X ) ) I(M;X,T(X)) using the Chain Rule. Since T ⁡ ( X ) T(X) is deterministic given X X , H ⁡ ( T ⁡ ( X ) | X ) = 0 H(T(X)|X)=0 (Proposition 1), which implies I ⁡ ( M ; T ⁡ ( X ) | X ) = 0 I(M;T(X)|X)=0 . Thus:

[152] table: I ⁡ ( M , X , T ⁡ ( X ) ) = I ⁡ ( M , X ) I(M;X,T(X))=I(M;X) (20)

[153] p: Alternatively, expanding in the reverse order:

[154] table: I ⁡ ( M , X , T ⁡ ( X ) ) = I ⁡ ( M , T ⁡ ( X ) ) + I ⁡ ( M ; X | T ⁡ ( X ) ) I(M;X,T(X))=I(M;T(X))+I(M;X|T(X)) (21)

[155] p: Combining these, we get the fundamental identity:

[156] table: I ⁡ ( M , X ) = I ⁡ ( M , T ⁡ ( X ) ) + I ⁡ ( M ; X | T ⁡ ( X ) ) I(M;X)=I(M;T(X))+I(M;X|T(X)) (22)

[157] p: From this identity, the equality I ⁡ ( M , X ) = I ⁡ ( M , T ⁡ ( X ) ) I(M;X)=I(M;T(X)) holds if and only if I ⁡ ( M ; X | T ⁡ ( X ) ) = 0 I(M;X|T(X))=0 . By Proposition 2 , I ⁡ ( M ; X | T ⁡ ( X ) ) = 0 I(M;X|T(X))=0 is equivalent to conditional independence ( M ⟂ X | T ⁡ ( X ) M\perp X|T(X) ), which is precisely the definition of Sufficiency. □ \square

[158] p: Lemma 1 (Information Invariance under Deterministic Mapping). Let Z Z be a discrete random variable and Y = g ⁡ ( Z ) Y=g(Z) be a deterministic function of Z Z . The mutual information with any source X X is preserved in the joint pair ( Z , Y ) (Z,Y) : I ⁡ ( X , Z ) = I ⁡ ( X , Z , g ⁡ ( Z ) ) I(X;Z)=I(X;Z,g(Z)) .

[159] p: Proof. Applying the Chain Rule: I ⁡ ( X , Z , Y ) = I ⁡ ( X , Z ) + I ⁡ ( X ; Y | Z ) I(X;Z,Y)=I(X;Z)+I(X;Y|Z) . Since Y Y is deterministic given Z Z , H ⁡ ( Y | Z ) = 0 H(Y|Z)=0 , implying I ⁡ ( X ; Y | Z ) = 0 I(X;Y|Z)=0 . Thus, I ⁡ ( X , Z , g ⁡ ( Z ) ) = I ⁡ ( X , Z ) I(X;Z,g(Z))=I(X;Z) . □ \square

[160] p: Lemma 2 (Invertibility from Information Equality). Let Z Z be a random variable determined by X X . Let T ∗ = g ⁡ ( Z ) T^{*}=g(Z) . If I ⁡ ( X , Z ) = I ⁡ ( X , T ∗ ) I(X;Z)=I(X;T^{*}) , then g g is invertible on the support of Z Z .

[161] p: Proof. Define information loss Δ ​ I = I ⁡ ( X , Z ) − I ⁡ ( X , T ∗ ) \Delta I=I(X;Z)-I(X;T^{*}) . By Lemma 1 , I ⁡ ( X , Z ) = I ⁡ ( X , Z , T ∗ ) = I ⁡ ( X , T ∗ ) + I ⁡ ( X ; Z | T ∗ ) I(X;Z)=I(X;Z,T^{*})=I(X;T^{*})+I(X;Z|T^{*}) . Thus, Δ ​ I = I ⁡ ( X ; Z | T ∗ ) \Delta I=I(X;Z|T^{*}) . Given I ⁡ ( X , Z ) = I ⁡ ( X , T ∗ ) I(X;Z)=I(X;T^{*}) , we have I ⁡ ( X ; Z | T ∗ ) = 0 I(X;Z|T^{*})=0 . Written as expected KL divergence:

[162] table: 𝔼 t ∗ [ D K ​ L ( p ( x , z | t ∗ ) ∥ p ( x | t ∗ ) p ( z | t ∗ ) ) ] = 0 \mathbb{E}_{t^{*}}\left[D_{KL}(p(x,z|t^{*})\|p(x|t^{*})p(z|t^{*}))\right]=0 (23)

[163] p: By Gibbs’ Inequality, this implies p ⁡ ( x , z | t ∗ ) = p ⁡ ( x | t ∗ ) ​ p ​ ( z | t ∗ ) p(x,z|t^{*})=p(x|t^{*})p(z|t^{*}) . Since Z Z is a deterministic function of X X (say Z = T e ​ n ​ c ​ ( X ) Z=T_{enc}(X) ), the conditional PMF is p ⁡ ( z | x , t ∗ ) = 𝕀 ⁡ ( z = T e ​ n ​ c ​ ( x ) ) p(z|x,t^{*})=\mathbb{I}(z=T_{enc}(x)) , where 𝕀 \mathbb{I} is the indicator function. The conditional independence implies p ⁡ ( z | x , t ∗ ) = p ⁡ ( z | t ∗ ) p(z|x,t^{*})=p(z|t^{*}) . Therefore, p ⁡ ( z | t ∗ ) = 𝕀 ⁡ ( z = T e ​ n ​ c ​ ( x ) ) p(z|t^{*})=\mathbb{I}(z=T_{enc}(x)) , meaning Z Z is fully determined by T ∗ T^{*} . This proves the existence of an inverse mapping Z = f ⁡ ( T ∗ ) Z=f(T^{*}) , making g g bijective on the support. □ \square

[164] h3: A.4 Theorem 2: Classical MSS Implies Information Minimality

[165] p: Theorem 2. Let T ⁡ ( X ) T(X) be a Minimal Sufficient Statistic for M M in the classical sense. Let S ⁡ ( X ) S(X) be any other sufficient statistic for M M . Then, T ⁡ ( X ) T(X) minimizes the mutual information with the input X X among all sufficient statistics:

[166] table: I ⁡ ( T ⁡ ( X ) , X ) ≤ I ⁡ ( S ⁡ ( X ) , X ) I(T(X);X)\leq I(S(X);X) (24)

[167] p: Proof. Let T ⁡ ( X ) T(X) be the Minimal Sufficient Statistic and S ⁡ ( X ) S(X) be an arbitrary sufficient statistic for M M . By the definition of minimal sufficiency (Definition 2), T ⁡ ( X ) T(X) must be a function of S ⁡ ( X ) S(X) , denoted as T ⁡ ( X ) = f ⁡ ( S ⁡ ( X ) ) T(X)=f(S(X)) . This functional relationship establishes a Markov Chain X → S ⁡ ( X ) → T ⁡ ( X ) X\to S(X)\to T(X) .

[168] p: Applying the Data Processing Inequality (DPI) to this chain, we obtain I ⁡ ( X , T ⁡ ( X ) ) ≤ I ⁡ ( X , S ⁡ ( X ) ) I(X;T(X))\leq I(X;S(X)) . Since T ⁡ ( X ) T(X) is sufficient, it retains all mutual information regarding the target M M ( Theorem 1 ), while the DPI confirms it simultaneously minimizes the information retained about the input X X compared to any other sufficient statistic S ⁡ ( X ) S(X) . ■ \blacksquare

[169] h3: A.5 Theorem 3: Information Minimality Implies Classical MSS

[170] p: Theorem 3 (Converse). Let Z Z be a sufficient statistic for M M such that for any other sufficient statistic S ⁡ ( X ) S(X) , I ⁡ ( Z , X ) ≤ I ⁡ ( S , X ) I(Z;X)\leq I(S;X) . Let T ∗ ​ ( X ) T^{*}(X) be a classical Minimal Sufficient Statistic. Then, Z Z is isomorphic to T ∗ ​ ( X ) T^{*}(X) .

[171] p: Proof. Assume a classical MSS T ∗ ​ ( X ) T^{*}(X) exists. Since Z Z is hypothesized to be a sufficient statistic, by the definition of classical minimal sufficiency, T ∗ ​ ( X ) T^{*}(X) must be a function of Z Z . Let this mapping be T ∗ ​ ( X ) = g ​ ( Z ) T^{*}(X)=g(Z) . This dependency forms the Markov Chain X → Z → T ∗ ​ ( X ) X\to Z\to T^{*}(X) , and by the Data Processing Inequality, we have I ⁡ ( X , T ∗ ) ≤ I ⁡ ( X , Z ) I(X;T^{*})\leq I(X;Z) .

[172] p: Conversely, the theorem hypothesis states that Z Z minimizes mutual information among all sufficient statistics. Since T ∗ ​ ( X ) T^{*}(X) is itself a sufficient statistic, it must hold that I ⁡ ( X , Z ) ≤ I ⁡ ( X , T ∗ ) I(X;Z)\leq I(X;T^{*}) . Combining these two inequalities, we obtain the equality:

[173] table: I ⁡ ( X , Z ) = I ⁡ ( X , T ∗ ) = I ⁡ ( X , g ⁡ ( Z ) ) I(X;Z)=I(X;T^{*})=I(X;g(Z)) (25)

[174] p: Invoking Lemma 2 , the information equality I ⁡ ( X , Z ) = I ⁡ ( X , g ⁡ ( Z ) ) I(X;Z)=I(X;g(Z)) implies that the function g g is invertible on the support of Z Z . Consequently, there exists a deterministic inverse Z = g − 1 ​ ( T ∗ ) Z=g^{-1}(T^{*}) . Since T ∗ T^{*} is a function of Z Z and Z Z is a function of T ∗ T^{*} , Z Z is strictly equivalent to the classical MSS T ∗ T^{*} up to isomorphism. ■ \blacksquare

[175] h2: Appendix B Derivation of the Lagrangian and the β \beta - ϵ \epsilon Correspondence

[176] p: This appendix provides the formal justification for replacing the constrained ϵ \epsilon -Minimal Sufficient Statistic (MSS) problem with the unconstrained Lagrangian relaxation used in WaterVIB. Specifically, we prove the strict convexity of the Information Bottleneck (IB) curve for the watermarking channel and establish the bijective mapping between the Lagrange multiplier β \beta and the sufficiency tolerance ϵ \epsilon .

[177] h3: B.1 The Primal Optimization Problem

[178] p: Let X X denote the cover signal, M M the watermark message, and Z Z the stochastic representation (watermarked latent). We assume the Markov chain M → X → Z M\rightarrow X\rightarrow Z . The optimization goal is to find the encoder p ⁡ ( z | x ) p(z|x) that minimizes the compression rate R R while maintaining a relevance I I at least I t ​ o ​ t ​ a ​ l − ϵ I_{total}-\epsilon . The primal problem ( P ϵ ) (P_{\epsilon}) ( Tishby et al., 2000 ) is defined over the convex set of valid conditional distributions Δ \Delta :

[179] table: min p ⁡ ( z | x ) ∈ Δ \displaystyle\min_{p(z|x)\in\Delta} I ⁡ ( Z , X ) \displaystyle I(Z;X) s.t. \displaystyle\text{s.t.} I ⁡ ( Z , M ) ≥ I t ​ o ​ t ​ a ​ l − ϵ \displaystyle I(Z;M)\geq I_{total}-\epsilon

[180] p: where I t ​ o ​ t ​ a ​ l = I ⁡ ( X , M ) I_{total}=I(X;M) .

[181] h3: B.2 Lagrangian Construction

[182] p: The mutual information functionals R ⁡ ( p ) R(p) and I ⁡ ( p ) I(p) are convex and concave functions of the mapping p ⁡ ( z | x ) p(z|x) , respectively. Since the optimization is performed over a convex set Δ \Delta , we can employ the method of Lagrange multipliers to convert the constrained problem into an unconstrained variational problem.

[183] p: We introduce a Lagrange multiplier λ ≥ 0 \lambda\geq 0 associated with the inequality constraint. The Lagrangian function ℒ ⁡ ( p , λ ) \mathcal{L}(p,\lambda) is defined as:

[184] table: ℒ ⁡ ( p , λ ) = R ⁡ ( p ) − λ ⁡ ( I ⁡ ( p ) − ( I t ​ o ​ t ​ a ​ l − ϵ ) ) \mathcal{L}(p,\lambda)=R(p)-\lambda\left(I(p)-(I_{total}-\epsilon)\right) (26)

[185] p: The optimization problem seeks to minimize this Lagrangian with respect to the encoder p p :

[186] table: p λ ∗ = arg ⁡ min p ∈ Δ ​ { R ⁡ ( p ) − λ ​ I ​ ( p ) + λ ⁡ ( I t ​ o ​ t ​ a ​ l − ϵ ) } p^{*}_{\lambda}=\arg\min_{p\in\Delta}\left\{R(p)-\lambda I(p)+\lambda(I_{total}-\epsilon)\right\} (27)

[187] p: Since the term λ ⁡ ( I t ​ o ​ t ​ a ​ l − ϵ ) \lambda(I_{total}-\epsilon) is constant with respect to p p , the optimization simplifies to:

[188] table: min p ⁡ ( R ⁡ ( p ) − λ ​ I ​ ( p ) ) ⇔ max p ⁡ ( λ ​ I ​ ( p ) − R ⁡ ( p ) ) \min_{p}\big(R(p)-\lambda I(p)\big)\iff\max_{p}\big(\lambda I(p)-R(p)\big) (28)

[189] p: To align this formulation with the standard Information Bottleneck (IB) objective, we define the trade-off parameter β ≜ 1 λ \beta\triangleq\frac{1}{\lambda} . Assuming the constraint is active (implying λ > 0 \lambda>0 ), multiplying the objective by 1 λ \frac{1}{\lambda} does not alter the optimal solution p ∗ p^{*} . Thus, the problem is equivalent to maximizing:

[190] table: ℒ IB ​ ( p , β ) = I ⁡ ( Z , M ) − β ​ I ​ ( Z , X ) \mathcal{L}_{\textbf{IB}}(p,\beta)=I(Z;M)-\beta I(Z;X) (29)

[191] p: This confirms that maximizing the IB objective ( Tishby et al., 2000 ) is mathematically equivalent to solving the primal MSS problem for a specific Lagrange multiplier λ = 1 / β \lambda=1/\beta .

[192] h3: B.3 Step 3: Geometry of the Solution and Strict Convexity

[193] p: The relationship between the hyperparameter β \beta and the tolerance ϵ \epsilon is governed by the geometry of the Information Plane ( Gilad-Bachrach et al., 2003 ) . We define the Minimal Rate Curve function R m ​ i ​ n ​ ( i ) R_{min}(i) , which characterizes the Pareto frontier of the compression-relevance trade-off. Specifically, R m ​ i ​ n ​ ( i ) R_{min}(i) represents the minimum compression rate required to achieve a target relevance level i i :

[194] table: R m ​ i ​ n ​ ( i ) = min p ∈ Δ ⁡ { I ⁡ ( Z , X ) ∣ I ⁡ ( Z , M ) = i } R_{min}(i)=\min_{p\in\Delta}\{I(Z;X)\mid I(Z;M)=i\} (30)

[195] p: Property 1 (Strict Convexity and Monotonicity). According to the standard Information Bottleneck theory (Tishby et al., 2000), the Minimal Rate Curve function R m ​ i ​ n ​ ( i ) R_{min}(i) is strictly convex and monotonically increasing for i ∈ [ 0 , I t ​ o ​ t ​ a ​ l ] i\in[0,I_{total}] . Mathematically:

[196] table: d ​ R m ​ i ​ n ​ ( i ) d ​ i > 0 and d 2 ​ R m ​ i ​ n ​ ( i ) d ​ i 2 > 0 \frac{dR_{min}(i)}{di}>0\quad\text{and}\quad\frac{d^{2}R_{min}(i)}{di^{2}}>0 (31)

[197] p: Constraint Activation. In our primal problem, we seek to minimize the compression rate R ⁡ ( p ) R(p) . Let i t ​ a ​ r ​ g ​ e ​ t = I t ​ o ​ t ​ a ​ l − ϵ i_{target}=I_{total}-\epsilon be the lower bound of the constraint. Suppose, for the sake of contradiction, that the optimal solution p ∗ p^{*} satisfies the strict inequality I ⁡ ( p ∗ ) > i t ​ a ​ r ​ g ​ e ​ t I(p^{*})>i_{target} . Due to the monotonicity property ( d ​ R m ​ i ​ n d ​ i > 0 \frac{dR_{min}}{di}>0 ), a reduction in relevant information I ⁡ ( p ) I(p) leads to a strict reduction in the minimal required rate R m ​ i ​ n R_{min} . Therefore, there exists another encoder p ′ p^{\prime} with I ⁡ ( p ′ ) = i t ​ a ​ r ​ g ​ e ​ t I(p^{\prime})=i_{target} such that R ⁡ ( p ′ ) < R ⁡ ( p ∗ ) R(p^{\prime})<R(p^{*}) . This contradicts the optimality of p ∗ p^{*} . Consequently, the optimal solution must lie exactly on the boundary of the feasible region:

[198] table: I ⁡ ( p ∗ ) = I t ​ o ​ t ​ a ​ l − ϵ I(p^{*})=I_{total}-\epsilon (32)

[199] h3: B.4 Step 4: Proof of the Bijective Mapping ( β ↔ ϵ \beta\leftrightarrow\epsilon )

[200] p: We now establish the one-to-one correspondence between β \beta and ϵ \epsilon using the Karush-Kuhn-Tucker (KKT) conditions. In convex optimization ( Boyd & Vandenberghe, 2004 ) , the optimal Lagrange multiplier λ \lambda represents the sensitivity of the objective function’s optimal value to perturbations in the constraint bound (often referred to as the shadow price ).

[201] p: Specifically, let p ∗ ​ ( i ) p^{*}(i) denote the optimal encoder for a given relevance target i = I t ​ o ​ t ​ a ​ l − ϵ i=I_{total}-\epsilon . According to the Stationarity condition of KKT, the gradient of the Lagrangian with respect to the distribution p p must vanish at the optimum:

[202] table: ∇ p ℒ ​ ( p ∗ , λ ) = ∇ p R ​ ( p ∗ ) − λ ​ ∇ p I ​ ( p ∗ ) = 0 ⟹ ∇ p R ​ ( p ∗ ) = λ ​ ∇ p I ​ ( p ∗ ) \nabla_{p}\mathcal{L}(p^{*},\lambda)=\nabla_{p}R(p^{*})-\lambda\nabla_{p}I(p^{*})=0\implies\nabla_{p}R(p^{*})=\lambda\nabla_{p}I(p^{*}) (33)

[203] p: Now, consider the Minimal Rate Curve R m ​ i ​ n ​ ( i ) = R ⁡ ( p ∗ ​ ( i ) ) R_{min}(i)=R(p^{*}(i)) . We analyze how the minimal rate changes with an infinitesimal perturbation in the target relevance i i . By applying the chain rule:

[204] table: d ​ R m ​ i ​ n ​ ( i ) d ​ i = ⟨ ∇ p R ​ ( p ∗ ) , d ​ p ∗ d ​ i ⟩ \frac{dR_{min}(i)}{di}=\left\langle\nabla_{p}R(p^{*}),\frac{dp^{*}}{di}\right\rangle (34)

[205] p: Substituting the stationarity condition ∇ p R ​ ( p ∗ ) = λ ​ ∇ p I ​ ( p ∗ ) \nabla_{p}R(p^{*})=\lambda\nabla_{p}I(p^{*}) into the equation:

[206] table: d ​ R m ​ i ​ n ​ ( i ) d ​ i = ⟨ λ ​ ∇ p I ​ ( p ∗ ) , d ​ p ∗ d ​ i ⟩ = λ ​ ⟨ ∇ p I ​ ( p ∗ ) , d ​ p ∗ d ​ i ⟩ ⏟ d ​ I ​ ( p ∗ ) d ​ i \frac{dR_{min}(i)}{di}=\left\langle\lambda\nabla_{p}I(p^{*}),\frac{dp^{*}}{di}\right\rangle=\lambda\underbrace{\left\langle\nabla_{p}I(p^{*}),\frac{dp^{*}}{di}\right\rangle}_{\frac{dI(p^{*})}{di}} (35)

[207] p: Since the constraint is active (as proven in Step 3), we have I ​ ( p ∗ ​ ( i ) ) = i I(p^{*}(i))=i . Differentiating both sides with respect to i i yields d ​ I ​ ( p ∗ ) d ​ i = 1 \frac{dI(p^{*})}{di}=1 . Consequently, the relationship simplifies directly to:

[208] table: d ​ R m ​ i ​ n ​ ( i ) d ​ i = λ ⋅ 1 = λ \frac{dR_{min}(i)}{di}=\lambda\cdot 1=\lambda (36)

[209] p: This confirms the geometric interpretation of the Lagrange multiplier λ \lambda as the slope of the Minimal Rate Curve.

[210] p: Formally, at the optimal solution corresponding to a tolerance ϵ \epsilon , we have:

[211] table: λ ⁡ ( ϵ ) = ∂ R m ​ i ​ n ​ ( i ) ∂ i | i = I t ​ o ​ t ​ a ​ l − ϵ \lambda(\epsilon)=\frac{\partial R_{min}(i)}{\partial i}\bigg|_{i=I_{total}-\epsilon} (37)

[212] p: Substituting our definition β = 1 / λ \beta=1/\lambda , we derive the explicit mapping function:

[213] table: β ⁡ ( ϵ ) = ( ∂ R m ​ i ​ n ​ ( i ) ∂ i | i = I t ​ o ​ t ​ a ​ l − ϵ ) − 1 = d ​ i d ​ R m ​ i ​ n | R m ​ i ​ n = R ∗ \beta(\epsilon)=\left(\frac{\partial R_{min}(i)}{\partial i}\bigg|_{i=I_{total}-\epsilon}\right)^{-1}=\frac{di}{dR_{min}}\bigg|_{R_{min}=R^{*}} (38)

[214] p: This equation states that β \beta is the inverse of the slope of the Minimal Rate Curve at the point determined by ϵ \epsilon .

[215] p: Theorem (Bijective Correspondence). The mapping 𝒯 : ϵ → β \mathcal{T}:\epsilon\to\beta defined in Eq. 38 is a bijection for ϵ ∈ ( 0 , I t ​ o ​ t ​ a ​ l ) \epsilon\in(0,I_{total}) .

[216] p: Proof.

[217] p: Monotonicity: Since R m ​ i ​ n ​ ( i ) R_{min}(i) is strictly convex (Property 1), its first derivative λ ⁡ ( i ) = d ​ R m ​ i ​ n d ​ i \lambda(i)=\frac{dR_{min}}{di} is strictly monotonically increasing with respect to the relevance i i . Consequently, as ϵ \epsilon increases (meaning relevance i = I t ​ o ​ t ​ a ​ l − ϵ i=I_{total}-\epsilon decreases), the slope λ \lambda strictly decreases.

[218] p: Invertibility: A strictly monotonic function is inherently invertible. Therefore, for every specific tolerance ϵ \epsilon , there exists a unique slope λ \lambda defining the tangent to the curve at that point. Since β = 1 / λ \beta=1/\lambda , there is a unique β \beta corresponding to each ϵ \epsilon .

[219] p: Conclusion. This proof demonstrates that adjusting the hyperparameter β \beta in the WaterVIB objective (Eq. 29 ) is mathematically equivalent to traversing the Pareto frontier of the ϵ \epsilon -MSS problem. A larger β \beta implies a steeper slope on the rate-relevance curve, corresponding to a looser tolerance ϵ \epsilon (more compression, less information retained), whereas a smaller β \beta enforces a stricter ϵ \epsilon (higher fidelity to the watermark).

[220] h2: Appendix C Appendix C: Implementation Details

[221] p: In this section, we provide the parameter-level details of the WaterVIB framework, including the specific network architectures for the Information Sieve mechanism, training hyperparameters, and the configuration of the differentiable noise layers used during the attack simulation phase to ensure reproducibility.

[222] h3: C.1 The WaterVIB Module Design

[223] p: The WaterVIB module functions as a stochastic information bottleneck inserted between the feature extractor and the message decoder. To ensure numerical stability and gradient flow during end-to-end optimization, we implement the module using the reparameterization trick. Specifically, the latent variable U U is computed as

[224] table: U = μ ⁡ ( Z ) + α ⋅ ϵ ⊙ exp ⁡ ( 1 2 ​ log ⁡ σ ​ ( Z ) 2 ) U=\mu(Z)+\alpha\cdot\epsilon\odot\exp(\frac{1}{2}\log\sigma(Z)^{2}) (39)

[225] p: , where ϵ ∼ 𝒩 ⁡ ( 0 , I ) \epsilon\sim\mathcal{N}(0,I) is sampled from a standard normal distribution. Here, α \alpha is a scalar scaling factor introduced to control the variance magnitude during the early stages of training. To prevent numerical instability such as exploding gradients, we explicitly clip the predicted log-variance log ⁡ Σ ​ ( Z ) 2 \log\Sigma(Z)^{2} to the range [ − 10 , 10 ] [-10,10] before the exponential operation.

[226] p: The training objective is a composite loss function:

[227] table: ℒ t ​ o ​ t ​ a ​ l = λ i ​ m ​ g ​ ℒ i ​ m ​ g + λ r ​ e ​ c ​ ℒ r ​ e ​ c + β ​ ℒ K ​ L \mathcal{L}_{total}=\lambda_{img}\mathcal{L}_{img}+\lambda_{rec}\mathcal{L}_{rec}+\beta\mathcal{L}_{KL} (40)

[228] p: The reconstruction loss ℒ r ​ e ​ c \mathcal{L}_{rec} is calculated as the Binary Cross-Entropy (BCE) between the ground truth message and the predicted probabilities, while the compression loss ℒ K ​ L \mathcal{L}_{KL} is the Kullback-Leibler divergence between the posterior q ⁡ ( U | Z ) q(U|Z) and the prior r ⁡ ( U ) = 𝒩 ⁡ ( 0 , I ) r(U)=\mathcal{N}(0,I) , weighted by the bottleneck capacity β \beta . The image fidelity loss ℒ i ​ m ​ g \mathcal{L}_{img} measures the Mean Squared Error (MSE) between the cover and watermarked images.

[229] h3: C.2 Integration into High-Capacity Architecture (EditGuard)

[230] p: For the EditGuard backbone, which utilizes a high-capacity encoder-decoder structure, we insert the VIB module after the 16-channel output of the bit decoder to handle the spatial feature maps. The input to the VIB module is a feature map of shape [ B , 16 , 400 , 400 ] [B,16,400,400] . To handle this high dimensionality efficiently, we employ a CNN-based compression pipeline rather than fully connected layers. The features are first downsampled and compressed via a sequence of channel reduction layers: a C ​ o ​ n ​ v ​ 2 ​ d ​ ( 16 → 4 ) Conv2d(16\to 4) layer reduces the channel dimension while downsampling the spatial resolution to 128 × 128 128\times 128 , followed by a C ​ o ​ n ​ v ​ 2 ​ d ​ ( 4 → 2 ) Conv2d(4\to 2) layer. A final convolution layer C ​ o ​ n ​ v ​ 2 ​ d ​ ( 2 → 2 ) Conv2d(2\to 2) produces the distributional parameters μ \mu and log ⁡ Σ 2 \log\Sigma^{2} , each maintaining the shape [ B , 1 , 128 , 128 ] [B,1,128,128] . After sampling the stochastic latent U U , the feature map is flattened to a dimension of 16,384 16,384 and projected via a single Linear layer ( 16,384 → 100 16,384\to 100 ) to produce the 100-bit output logits.

[231] p: Regarding hyperparameters, we trained the model on the COCO2017 dataset at a resolution of 512 × 512 512\times 512 . We set the bottleneck capacity β \beta to 0.0003 0.0003 and the noise scaling factor α \alpha to 10 − 4 10^{-4} to mitigate fluctuations during the initial training phase.

[232] h3: C.3 Integration into Lightweight Architecture (HiDDeN)

[233] p: For the parameter-constrained HiDDeN backbone, the VIB module is integrated between the final convolutional block of the extractor and the linear readout layer. Unlike the CNN-based approach used in EditGuard, this implementation utilizes a Multi-Layer Perceptron (MLP) structure. The global features from the extractor are mapped to a latent dimension of D = 128 D=128 . Two parallel linear layers then map these features to the statistical parameters μ ∈ ℝ 128 \mu\in\mathbb{R}^{128} and log ⁡ Σ 2 ∈ ℝ 128 \log\Sigma^{2}\in\mathbb{R}^{128} . The sampled latent U U is finally mapped to the 30-bit output via a linear readout layer.

[234] p: This model was trained on 10,000 images from the COCO2014 dataset at a resolution of 256 × 256 256\times 256 . Based on our ablation studies, we determined the optimal bottleneck capacity β \beta to be 0.00015 0.00015 and set the noise scaling factor α \alpha to 0.007 0.007 .

[235] h3: C.4 Differentiable Noise Simulation and Training

[236] p: To ensure robust generalization, we train the models against a comprehensive suite of differentiable noise layers. For EditGuard-VIB, the training focused on Gaussian, Poisson, and JPEG noise to strictly evaluate zero-shot generalization capabilities against unseen AIGC attacks. As shown in Table 8 , the parameters define the range of random distortions applied on HiDDeN-VIB during the attack simulation.

[237] figure: Table 8 : Configuration of Differentiable Noise Layers used in HiDDeN-VIB Training. Distortion Type Parameter Range / Value Crop Ratio [ 0.4 , 0.55 ] [0.4,0.55] Cropout Ratio [ 0.25 , 0.35 ] [0.25,0.35] Dropout Keep Prob. [ 0.65 , 0.75 ] [0.65,0.75] Resize (Scaling) Scale Factor [ 0.4 , 0.6 ] [0.4,0.6] JPEG Compression Coefficients ( 25 , 9 , 9 ) (25,9,9)

[238] p: All models were implemented in PyTorch and trained on NVIDIA 4090 GPUs using the Adam optimizer. The learning rate was initialized at 10 − 3 10^{-3} and adjusted using a scheduler. We used a batch size of 32 for the lightweight HiDDeN architecture and 64 for the high-capacity EditGuard architecture.

[239] h3: C.5 Training Algorithm

[240] p: We summarize the end-to-end training process of the WaterVIB framework in Algorithm 1 . This algorithm details the stochastic information bottleneck mechanism and the optimization of the composite objective function.

[241] figure: Algorithm 1 Training Process of WaterVIB 1: Input: Training dataset 𝒟 \mathcal{D} , Batch size B B , Learning rate η \eta , Hyperparameters α , β \alpha,\beta 2: Initialize: Encoder E E , Extractor E e ​ x ​ t E_{ext} , MLPs ( MLP μ , MLP σ \text{MLP}_{\mu},\text{MLP}_{\sigma} ), Decoder D m ​ s ​ g D_{msg} parameters θ \theta 3: for each training epoch do 4: for each batch ( x , m ) (x,m) in 𝒟 \mathcal{D} do 5: # 1. Watermark Embedding 6: x w ​ m ← E ⁡ ( x , m ) x_{wm}\leftarrow E(x,m) {Generate watermarked image} 7: # 2. Attack Simulation (Differentiable) 8: x a ​ t ​ k ← Attack ​ ( x w ​ m ) x_{atk}\leftarrow\text{Attack}(x_{wm}) {Apply noise layers (e.g., Crop, JPEG)} 9: # 3. Deterministic Feature Extraction 10: Z ← E e ​ x ​ t ​ ( x a ​ t ​ k ) Z\leftarrow E_{ext}(x_{atk}) {Extract backbone features} 11: # 4. Stochastic Bottleneck (VIB) 12: μ ← MLP μ ​ ( Z ) \mu\leftarrow\text{MLP}_{\mu}(Z) 13: σ ← exp ⁡ ( 1 2 ​ MLP σ ​ ( Z ) ) \sigma\leftarrow\exp\left(\frac{1}{2}\text{MLP}_{\sigma}(Z)\right) 14: Sample ϵ ∼ 𝒩 ⁡ ( 0 , I ) \epsilon\sim\mathcal{N}(0,I) 15: U ← μ + α ⋅ ϵ ⊙ σ U\leftarrow\mu+\alpha\cdot\epsilon\odot\sigma {Reparameterization Trick (Eq. 39 )} 16: # 5. Message Decoding 17: m ^ ← D m ​ s ​ g ​ ( U ) \hat{m}\leftarrow D_{msg}(U) {Predict message from stochastic latent} 18: # 6. Loss Computation 19: ℒ r ​ e ​ c ← BCE ​ ( m , m ^ ) \mathcal{L}_{rec}\leftarrow\text{BCE}(m,\hat{m}) {Reconstruction Loss (Eq. 7 )} 20: ℒ K ​ L ← D K ​ L ( 𝒩 ( μ , σ 2 ) ∥ 𝒩 ( 0 , I ) ) \mathcal{L}_{KL}\leftarrow D_{KL}(\mathcal{N}(\mu,\sigma^{2})\|\mathcal{N}(0,I)) {Compression Loss (Eq. 8 )} 21: ℒ i ​ m ​ g ← MSE ​ ( x , x w ​ m ) \mathcal{L}_{img}\leftarrow\text{MSE}(x,x_{wm}) {Image Fidelity Loss} 22: ℒ t ​ o ​ t ​ a ​ l ← ℒ i ​ m ​ g + ℒ r ​ e ​ c + β ​ ℒ K ​ L \mathcal{L}_{total}\leftarrow\mathcal{L}_{img}+\mathcal{L}_{rec}+\beta\mathcal{L}_{KL} {Total Objective (Eq. 9)} 23: # 7. Optimization 24: Update θ ← θ − η ​ ∇ θ ℒ t ​ o ​ t ​ a ​ l \theta\leftarrow\theta-\eta\nabla_{\theta}\mathcal{L}_{total} 25: end for 26: end for

[242] h2: Appendix D Appendix D: Experiments on NeRF-Signature

[243] p: To demonstrate the universality of our method beyond 2D static images, we integrated the WaterVIB module into NeRF-Signature ( Luo et al., 2025 ) , a state-of-the-art watermarking framework for 3D Neural Radiance Fields (NeRF). This appendix details the experimental setup and the performance gains achieved by our method in the 3D domain.

[244] h3: D.1 Experimental Setup

[245] p: Datasets and Protocol. Following the baseline NeRF-Signature framework, we evaluated our method on two standard datasets: the synthetic Blender dataset ( Mildenhall et al., 2021 ) (Lego, Hotdog, etc.) at its native resolution, and the real-world LLFF dataset ( Mildenhall et al., 2019 ) (Fern, Room, etc.) downsampled to 1 / 8 1/8 resolution.

[246] p: Implementation Details. We embed a 32-bit watermark message into the NeRF representation. The baseline NeRF-Signature injects a compact signature codebook into the radiance field. We integrated our WaterVIB module into the extraction head of the NeRF-Signature pipeline to optimize the information flow. To control randomness, all experiments employed identical NeRF cores, and evaluations were conducted on a fixed set of test viewpoints.

[247] p: Metrics. We evaluate imperceptibility by comparing Watermarked vs. Clean NeRF renderings using PSNR, SSIM, and LPIPS ( Luo et al., 2025 ) . Robustness is measured via Bit Accuracy (ACC) under standard 2D distortions, including Rotation, Scaling, Blurring, Brightness, JPEG, and Cropping.

[248] h3: D.2 Performance Evaluation

[249] p: Quantitative Results (Imperceptibility). As shown in Table 9 , the integration of WaterVIB significantly improves the visual quality of the watermarked renderings compared to the baseline. On the Blender dataset, WaterVIB increases the PSNR from 57.17 dB to 58.99 dB and reduces the LPIPS perceptual distance by 40%, indicating that our method introduces significantly fewer artifacts while maintaining a 0% Bit Error Rate (BER). A similar trend is observed on the real-world LLFF dataset.

[250] figure: Table 9 : Comparison of watermarking imperceptibility on NeRF-Signature. We measure the quality of watermarked renderings against clean NeRF renderings. Metrics include Bit Error Rate (BER, lower is better), PSNR (higher is better), LPIPS (lower is better), and SSIM (higher is better). Method Blender Dataset LLFF Dataset BER ↓ \downarrow PSNR ↑ \uparrow LPIPS ↓ \downarrow SSIM ↑ \uparrow BER ↓ \downarrow PSNR ↑ \uparrow LPIPS ↓ \downarrow SSIM ↑ \uparrow NeRF-Sig 0.00 57.17 5 × 10 − 5 5\times 10^{-5} 0.9998 0.10 46.51 0.0016 0.9973 + WaterVIB 0.00 58.99 3 × 10 − 5 3\times 10^{-5} 0.9999 0.10 49.61 0.0009 0.9984

[251] p: Quantitative Results (Robustness). We further evaluated the robustness of the 3D watermark against 2D image distortions. As detailed in Table 10 , WaterVIB maintains the robustness of the baseline (ACC ≈ \approx 100%) across all noise categories. W

[252] p: aterVIB significantly improves imperceptibility, consistently delivering higher PSNR scores under all tested distortions (e.g., +1.3 dB in Cropping). This result confirms that the Information Sieve mechanism effectively concentrates the watermark signal into robust yet imperceptible subspaces, thereby enhancing visual fidelity without compromising extraction accuracy.

[253] figure: Table 10 : Robustness evaluation on the Blender dataset (32 bits). We report the Bit Accuracy (ACC, ↑ \uparrow ) and the PSNR ( ↑ \uparrow ) of the watermarked views. WaterVIB maintains high robustness while consistently improving visual quality. Method Rotation Scaling Blurring Brightness JPEG Cropping Average Acc PSNR Acc PSNR Acc PSNR Acc PSNR Acc PSNR Acc PSNR Acc PSNR NeRF-Sig 0.999 52.36 1.000 54.94 1.000 55.55 1.000 55.20 0.999 51.76 1.000 56.23 0.999 54.32 + WaterVIB 0.997 53.26 1.000 55.76 1.000 57.07 1.000 55.98 0.998 51.93 1.000 57.54 0.999 55.26

[254] h3: D.3 Qualitative Analysis

[255] p: Visual comparisons confirm that the WaterVIB module helps in concentrating the watermark signal into texture-rich, high-frequency regions of the scene, where human vision is less sensitive to perturbations. As observed in our qualitative results (Figure 6 ), the residual difference maps for WaterVIB are sparser and more localized compared to the baseline, which explains the simultaneous improvement in both imperceptibility (higher PSNR) and robustness.

[256] figure: Figure 6 : Visualization of Nerf-VIB

[257] h2: Appendix E Analysis Experimental Setup and Supplement

[258] p: In this section, we explicitly detail the experimental settings used for the theoretical validation provided in Section 3 and present additional supplementary experiments to further substantiate our findings.

[259] h3: E.1 Setup for Theoretical Analysis (Section 3)

[260] p: The theoretical analysis presented in Section 3 , including the Spectral and Spatial Alignment (Observation 3.1 ) and the Gradient Counter-Optimization analysis (Section 3.2 ), was conducted empirically to validate our propositions.

[261] p: Model Architecture. All quantitative measurements and feature visualizations in Section 3 were performed using the EditGuard (Zhang et al., 2024) architecture as the backbone. This high-capacity model was selected to ensure that the observations regarding texture entanglement are representative of state-of-the-art deep watermarking methods.

[262] p: Data Sampling. To strictly evaluate the statistical behavior of the watermark under attack, we randomly sampled 500 images from the COCO validation dataset (consistent with the validation set used for EditGuard). This sample size was chosen to provide a statistically significant estimate of the spectral energy distribution and gradient projections while maintaining computational feasibility for the extensive gradient tracking required in Section 3.2.

[263] p: AIGC Purification Setting. For the generative purification noise simulated in these analyses (specifically for the results in Tables 1, 2, and 7), we utilized the SDXL 1.0 model. We employed the model in an image-to-image mode with a strength factor consistent with the ”Global Purification” settings described in Section 5.2. This ensures that the theoretical insights regarding the ”manifold projection” effect of diffusion models are directly applicable to the strongest attack scenarios evaluated in the main paper.

[264] p: Training Consistency. The model checkpoints (CKPT) and other training hyperparameters used for these analysis steps are identical to those reported in the experimental section (Section 5 and Appendix C.2).

[265] h3: E.2 Additional Supplementary Analysis Experiments

[266] p: To provide a more comprehensive analysis of WaterVIB, we conduct the following additional experiments.

[267] p: Experiment I: Geometric Orthogonality and Energy Analysis. To strictly quantify the disentanglement, we analyze the geometric relationship between the watermark signal 𝐬 w ​ m \mathbf{s}_{wm} and the AIGC distortion vector 𝐬 a ​ t ​ k \mathbf{s}_{atk} on 500 randomly sampled images.

[268] figure: Table 11 : Orthogonality Analysis. We compare the cosine similarity and the effective projection of the attack noise onto the watermark direction. Effective Proj. serves as the decisive metric for signal survival. Method Cosine Sim. ( cos ⁡ θ \cos\theta ) Effective Proj. ( η ⋅ | cos ⁡ θ | \eta\cdot|\cos\theta| ) Baseline (EditGuard) − 0.0395 -0.0395 0.1572 WaterVIB (Ours) 0.0077 0.0306

[269] p: Analysis of Energy Disparity. A seemingly negligible cosine similarity in high-dimensional spaces can be destructive due to the significant energy gap between the signal and the attack. In our experiments, the watermark is imperceptible ( PSNR w ​ m ≈ 40 \text{PSNR}_{wm}\approx 40 dB), while the AIGC purification introduces substantial distortions ( PSNR a ​ t ​ k ≈ 28 \text{PSNR}_{atk}\approx 28 dB). This ≈ 12 \approx 12 dB difference implies that the AIGC noise vector is significantly stronger in magnitude than the watermark signal:

[270] table: η = ‖ 𝐬 a ​ t ​ k ‖ ‖ 𝐬 w ​ m ‖ ≈ 10 40 − 28 20 ≈ 3.98 \eta=\frac{||\mathbf{s}_{atk}||}{||\mathbf{s}_{wm}||}\approx 10^{\frac{40-28}{20}}\approx 3.98 (41)

[271] p: We define the Effective Projection as the ratio of the destructive interference to the watermark strength: E p ​ r ​ o ​ j = η ⋅ | cos ⁡ θ | E_{proj}=\eta\cdot|\cos\theta| . For the Baseline, the attack noise exerts a projection force equivalent to 15.7 % \mathbf{15.7\%} ( 3.98 × 0.0395 3.98\times 0.0395 ) of the watermark’s magnitude, effectively overwriting the signal. In contrast, WaterVIB achieves near-perfect orthogonality ( cos ⁡ θ ≈ 0.007 \cos\theta\approx 0.007 ), suppressing the effective interference to a negligible 3.0 % \mathbf{3.0\%} , thus ensuring robustness despite the overwhelming energy of the generative process.

[272] p: Experiment II: Mechanism of Erasure via Negative Correlation. To further investigate how generative purification destroys the watermark, we analyzed the statistical relationship between the generated AIGC distortion ( 𝐬 a ​ t ​ k \mathbf{s}_{atk} ) and the original cover image content ( 𝐱 \mathbf{x} ). We measured both the global Cosine Similarity and the pixel-wise Pearson Correlation Coefficient (PCC) on the same 500-sample subset.

[273] figure: Table 12 : Correlation Analysis: AIGC Distortion vs. Cover Image. Unlike random noise (Gaussian) which is statistically orthogonal to the image content, AIGC distortion exhibits a significant negative correlation, indicating an active subtraction of image features. Noise Type Cosine Sim. ( 𝐬 ⋅ 𝐱 \mathbf{s}\cdot\mathbf{x} ) Pearson Corr. (PCC) Random Gaussian ≈ 0.000 \approx 0.000 ≈ 0.000 \approx 0.000 AIGC (SDXL 1.0) -0.1918 -0.3399

[274] p: Analysis of Content Suppression. The negative correlations reported in Table 12 reveal the fundamental mechanism of the attack. A correlation of approximately zero (as seen in random noise) implies that the distortion is independent of the content. However, the significant negative values ( PCC ≈ − 0.34 \text{PCC}\approx-0.34 ) observed for AIGC indicate that the generated distortion 𝐬 a ​ t ​ k \mathbf{s}_{atk} is structurally opposed to the cover image 𝐱 \mathbf{x} . Mathematically, the purified image is formed as 𝐱 p ​ u ​ r ​ e = 𝐱 + 𝐬 a ​ t ​ k \mathbf{x}_{pure}=\mathbf{x}+\mathbf{s}_{atk} . A negative projection ( 𝐬 a ​ t ​ k ⋅ 𝐱 < 0 \mathbf{s}_{atk}\cdot\mathbf{x}<0 ) implies that the addition of 𝐬 a ​ t ​ k \mathbf{s}_{atk} reduces the magnitude of the original images:

[275] table: ‖ 𝐱 + 𝐬 a ​ t ​ k ‖ < ‖ 𝐱 ‖ (along aligned dimensions) ||\mathbf{x}+\mathbf{s}_{atk}||<||\mathbf{x}||\quad\text{(along aligned dimensions)} (42)

[276] p: This confirms that the generative model acts as a Content-Adaptive Eraser . It perceives high-frequency details (which harbor the watermark) as ”perceptual noise” or ”energetic costs” and generates a counter-signal to smooth or suppress them. This active erasure explains why texture-entangled watermarks are obliterated even when the visual change appears minimal.

[277] h3: E.3 Visualization of Watermark Residual Distribution

[278] p: To provide an intuitive understanding of how the Information Bottleneck principle alters the embedding strategy, we visualize the spatial distribution of the watermark signal. Figure 7 displays the absolute residual maps | x w ​ m − x | |x_{wm}-x| for both the Baseline (HiDDeN) and our WaterVIB model across diverse cover images.

[279] p: Texture Entanglement and Spatial Clustering in Baseline. As observed in the “Baseline Residual” column, the standard encoder exhibits a strong structural dependency on the cover image, with watermark energy heavily concentrated and clustered on specific high-frequency object contours and sharp edges. This localization corroborates our analysis in Section 3.1: the baseline model implicitly learns to hide information within the most complex textures to satisfy invisibility constraints. However, this creates a critical vulnerability, as generative purification models specifically target and rewrite these high-gradient texture regions during the manifold projection process, effectively erasing the watermark along with the original texture.

[280] p: Uniform Texture Diffusion in WaterVIB. In contrast, the “VIB Residual” column demonstrates that WaterVIB induces a significantly more uniform diffusion of the signal across the textured domains of the image. Instead of overfitting the watermark to a limited set of sharp edges, the VIB-constrained model spreads the signal intensity across a broader and more diverse range of structural features. By enforcing the Information Bottleneck constraint to minimize I ⁡ ( Z , X ) I(Z;X) , the encoder is compelled to abandon its reliance on specific, fragile texture details. While the signal remains predominantly within the textured regions to maintain imperceptibility, its distribution is no longer tied to the narrow set of pixels most susceptible to generative reconstruction. This expanded and more uniform coverage within the textured manifold ensures that the watermark information remains resilient even when generative models perform localized editing or semantic rewriting on the image’s high-frequency details.

[281] figure: Figure 7 : Qualitative Comparison of Watermark Residuals. We visualize the absolute difference | x w ​ m − x | |x_{wm}-x| (amplified for visibility) between the watermarked and original images. The Baseline (HiDDeN) residuals are heavily entangled with high-frequency image textures. In contrast, WaterVIB produces a more dispersed noise pattern, indicating that the Information Bottleneck constraint successfully decouples the watermark signal from fragile cover details.

[282] h2: Appendix F Defense against Re-Embedding Attacks

[283] p: In real-world API deployment scenarios, a potential threat arises from Re-Embedding Attacks (also known as Multi-Watermarking), where an adversary attempts to overwrite or confuse the existing watermark by embedding a new message into an already watermarked image.

[284] h3: F.1 Defense Mechanism: Pre-Embedding Detection

[285] p: To mitigate this threat, we implement a detection-based defense mechanism . The system enforces a strict policy: no new embedding is permitted if a watermark is already detected. This requires the decoder to function not only as a message extractor but also as a robust binary detector (Watermarked vs. Clean).

[286] p: We leverage the output logits of the decoder as a confidence metric. Specifically, we define the Average Logits (AL) score:

[287] table: A ​ L = 1 L ​ ∑ i = 1 L | l i | AL=\frac{1}{L}\sum_{i=1}^{L}|l_{i}| (43)

[288] p: where l i l_{i} represents the raw logit output for the i i -th bit of the message. Due to the sigmoid activation in the final layer, higher absolute logits | l i | |l_{i}| correspond to higher confidence predictions (approaching 0 or 1).

[289] h3: F.2 The VIB Advantage in Detection

[290] p: The WaterVIB framework inherently enhances detectability. The Information Bottleneck objective ( ℒ I ​ B \mathcal{L}_{IB} ) constrains the latent representation to capture only the Minimal Sufficient Statistics of the message. This optimization pressure forces the decoder to be extremely decisive, pushing the output distribution towards deterministic states (high confidence) for watermarked images, while clean images (which lack the specific watermark structure) produce low-confidence, high-entropy outputs.

[291] p: This distributional separation effectively widens the gap between the two classes, making the detection threshold robust even under noise.

[292] h3: F.3 Empirical Evaluation

[293] p: We evaluated this defense on a held-out set of 1,500 images: 500 clean images, 500 watermarked images embedded with random messages, and 500 watermarked images subjected to Gaussian noise ( σ = 0.05 \sigma=0.05 ). We compare the detection performance of our HiDDeN-VIB against the standard HiDDeN baseline.

[294] h4: Metrics.

[295] p: We report the False Positive Rate ( FP ) on clean images, False Negative Rate ( FN ) on watermarked images, and the FN under noise. Additionally, we measure the Kullback-Leibler Divergence ( KL-Div ) between the logit distributions of clean and watermarked samples to quantify separability.

[296] h4: Results.

[297] p: As shown in Table 13 , both models achieve perfect separation (0% error) on clean and standard watermarked images. However, under noise attacks, the baseline’s detection capability degrades significantly (FN rises to 38.50%). In contrast, WaterVIB maintains robust detection with an FN of only 1.98% . The higher KL-Divergence ( 3.84 vs. 3.33) confirms that WaterVIB learns a more distinct and robust watermark manifold, effectively preventing re-embedding attacks even when the image has been degraded.

[298] figure: Table 13 : Re-Embedding Defense Performance. Comparison of detection robustness. The VIB constraint significantly improves detection under noise, preventing unauthorized re-embedding. Model FP (Clean) FN (Watermarked) FN (WM + Noised) KL-Div ↑ \uparrow HiDDeN (Baseline) 0.00% 0.00% 38.50% 3.33 HiDDeN-VIB (Ours) 0.00% 0.00% 1.98% 3.84

[299] h2: Instructions for reporting errors

[300] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[301] p: Tip: You can select the relevant text first, to include it in your report.

[302] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[303] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
