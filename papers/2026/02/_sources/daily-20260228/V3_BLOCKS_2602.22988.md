[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Residual Koopman Spectral Profiling for Predicting and Preventing Transformer Training Instability

[3] h6: Abstract

[4] p: Training divergence in transformers wastes compute, yet practitioners discover instability only after expensive runs begin. They therefore need an expected probability of failure for a transformer before training starts. Our study of Residual Koopman Spectral Profiling (RKSP) provides such an estimate. From a single forward pass at initialization, RKSP extracts Koopman spectral features by applying whitened dynamic mode decomposition to layer-wise residual snapshots. Our central diagnostic, the near-unit spectral mass, quantifies the fraction of modes concentrated near the unit circle, which captures instability risk. For predicting divergence across extensive configurations, this estimator achieves an AUROC of 0.995, outperforming the best gradient baseline. We further make this diagnostic actionable through Koopman Spectral Shaping (KSS), which reshapes spectra during training. We empirically validate that our method works in practice: RKSP predicts divergence at initialization, and when RKSP flags high risk, turning on KSS successfully prevents divergence. In the challenging high learning rate regime without normalization layers, KSS reduces the divergence rate from 66.7% to 12.5% and enables learning rates that are 50% to 150% higher. These findings generalize to WikiText-103 language modeling, vision transformers on CIFAR-10, and pretrained language models, including GPT-2 and LLaMA-2 up to 7B, as well as emerging architectures such as MoE, Mamba-style SSMs, and KAN.

[5] h2: 1 Introduction

[6] p: Transformers [ Vaswani et al., 2017 ] exhibit unpredictable training dynamics despite stabilization techniques such as layer normalization [ Ba et al., 2016 ] and careful initialization. In particular, exploding-gradient instability remains a known failure mode in deep networks [ Pascanu et al., 2013 ] . This unpredictability in training divergence wastes compute: practitioners often discover divergence only after expensive runs have begun. Addressing this problem requires a calibrated, initialization-time risk estimate, which enables early pruning of risky configurations. Such an estimate should output a probability that matches empirical frequency rather than a heuristic score.

[7] p: To provide such estimates, we propose Residual Koopman Spectral Profiling (RKSP), which views transformer layers as discrete-time dynamical systems. From a single forward pass, RKSP applies whitened dynamic mode decomposition (DMD) [ Tu, 2013 ] to estimate local linear operators that approximate the residual stream evolution 𝐡 0 → 𝐡 1 → ⋯ → 𝐡 L \mathbf{h}_{0}\to\mathbf{h}_{1}\to\cdots\to\mathbf{h}_{L} . The resulting layer-wise spectra provide a compact, predictive summary of stability.

[8] p: Intuitively, when a layer’s local linearization is close to normal, eigenvalues near the unit circle imply near-isometric propagation and therefore weak damping of signals and gradients. In high learning rate regimes, such weak damping can leave perturbations and optimization noise to be less attenuated, increasing divergence risk; conversely, strongly contractive spectra tend to be more stable but may cause rapid gradient decay. We summarize this trade-off with the near-unit mass M ≈ 1 M_{\approx 1} , the fraction of modes near the unit circle, together with a separate measure of non-normality; Section 4 provides a theoretical explanation for this behavior.

[9] p: The near-unit mass M ≈ 1 M_{\approx 1} exhibits a strong instability signal; using the monotone risk score M ≈ 1 M_{\approx 1} yields an Area Under the Receiver Operating Characteristic curve (AUROC) of 0.995 for divergence prediction across various normalization strategies, tasks, and architectures. To make this signal further actionable, we introduce Koopman Spectral Shaping (KSS), which reshapes spectra during training to reduce divergence.

[10] p: Our contributions are as follows.

[11] p: We propose RKSP, which estimates layer-wise Koopman spectra at initialization via whitened DMD (Section 3.2 ).

[12] p: We propose KSS, which reshapes spectra during training, preventing instability and permitting larger learning rates (Section 3.3 ).

[13] p: We provide theoretical bounds linking near-unit mass, near-normality, and the trade-offs between instability and expressivity (Section 4 ).

[14] p: We validate RKSP across various normalization strategies, datasets, and architectures, including language models, vision transformer (ViT) models, and emerging neural network families (Section 5 and Appendix G ).

[15] h2: 2 Background

[16] p: A transformer with L L layers updates its residual stream according to the residual formulation [ He et al., 2016 ] :

[17] table: 𝐡 ℓ + 1 = 𝐡 ℓ + f ℓ ​ ( 𝐡 ℓ , θ ℓ ) = F ℓ ​ ( 𝐡 ℓ ) , \mathbf{h}_{\ell+1}=\mathbf{h}_{\ell}+f_{\ell}(\mathbf{h}_{\ell};\theta_{\ell})=F_{\ell}(\mathbf{h}_{\ell}), (1)

[18] p: where f ℓ f_{\ell} comprises self-attention or multi-layer perceptron sub-layers. This formulation reveals that each layer transition defines a discrete-time dynamical system. Also, residual networks can be viewed as discretizations of continuous-time dynamical systems, motivating stability analysis from an ordinary differential equation perspective [ Haber and Ruthotto, 2017 , Chen et al., 2018 ] . Indeed, the local linearization of this system characterizes its stability.

[19] h3: 2.1 Koopman Operator Theory and DMD Primer

[20] p: Consider a discrete-time dynamical system 𝐱 t + 1 = F ⁡ ( 𝐱 t ) \mathbf{x}_{t+1}=F(\mathbf{x}_{t}) on state space 𝒳 ⊆ ℝ d \mathcal{X}\subseteq\mathbb{R}^{d} . The Koopman operator 𝒦 : ℱ → ℱ \mathcal{K}:\mathcal{F}\to\mathcal{F} acts on observable functions g : 𝒳 → ℂ g:\mathcal{X}\to\mathbb{C} via composition with the dynamics [ Koopman, 1931 , Mezić, 2005 , Mezić, 2013 , Tu, 2013 ] :

[21] table: ( 𝒦 ​ g ) ​ ( 𝐱 ) ≜ g ​ ( F ​ ( 𝐱 ) ) . (\mathcal{K}g)(\mathbf{x})\triangleq g(F(\mathbf{x})). (2)

[22] p: For a nonlinear F F , the operator 𝒦 \mathcal{K} is infinite-dimensional but remains linear regardless of the nonlinearity in F F . The spectral properties of 𝒦 \mathcal{K} —its eigenvalues { λ j } \{\lambda_{j}\} and eigenfunctions { ϕ j } \{\phi_{j}\} —encode the intrinsic timescales and geometric structure of the dynamics:

[23] table: 𝒦 ​ ϕ j \displaystyle\mathcal{K}\phi_{j} = λ j ​ ϕ j , \displaystyle=\lambda_{j}\phi_{j}, (3) therefore ​ ϕ j ​ ( F n ​ ( 𝐱 ) ) \displaystyle\text{therefore }\phi_{j}(F^{n}(\mathbf{x})) = λ j n ϕ j ( 𝐱 ) , for all n ≥ 0 . \displaystyle=\lambda_{j}^{n}\phi_{j}(\mathbf{x}),\text{for all }n\geq 0.

[24] p: The spectrum admits direct interpretation: modes with | λ j | > 1 |\lambda_{j}|>1 grow exponentially, modes with | λ j | < 1 |\lambda_{j}|<1 decay exponentially, and modes with | λ j | = 1 |\lambda_{j}|=1 persist or oscillate. The argument arg ⁡ ( λ j ) \arg(\lambda_{j}) gives the oscillation frequency of mode j j [ Rowley et al., 2009 ] .

[25] p: In a layer-wise, non-autonomous setting, each layer has its own distinct operator, so each 𝐀 ^ ℓ \hat{\mathbf{A}}_{\ell} must be estimated separately. Thus, the modulus | λ ⁡ ( 𝐀 ^ ℓ ) | |\lambda(\hat{\mathbf{A}}_{\ell})| indicates a local, per-layer expansion or contraction tendency. DMD approximates these layer-wise Koopman operators from finite data [ Schmid, 2010 , Tu, 2013 , Kutz et al., 2016 ] .

[26] h3: 2.2 Related Work

[27] h5: Koopman methods in machine learning.

[28] p: Existing Koopman methods approximate operators via DMD and its extensions or learn linearizing transformations for dynamics prediction [ Lusch et al., 2017 , Williams et al., 2015 , Korda and Mezic, 2018 ] . These methods primarily target representation learning.

[29] h5: Edge of chaos.

[30] p: The edge of chaos hypothesis links optimal trainability to critical initialization and signal propagation regimes [ Schoenholz et al., 2017 , Poole et al., 2016 , Pennington et al., 2017 ] , where signals neither explode nor vanish.

[31] h5: Neural tangent kernel.

[32] p: The neural tangent kernel characterizes gradient descent in the infinite-width limit and yields kernel-regression behavior [ Jacot et al., 2018 ] . In particular, linearizing the network around its initialization makes the kernel essentially constant, so training reduces to regression with this fixed kernel.

[33] h5: Mean-field theory and μ \mu P.

[34] p: Mean-field theory and Maximal Update Parameterization ( μ \mu P) enable hyperparameter transfer across scales through asymptotic analysis [ Schoenholz et al., 2017 , Yang et al., 2022 ] .

[35] h5: Normalization-free training.

[36] p: Normalization-free residual networks can be stabilized with Fixup initialization [ Zhang et al., 2019 ] . ReZero trains deep residual networks and transformers without normalization by introducing a residual scaling parameter initialized to zero, so the network starts near an identity map [ Bachlechner et al., 2021 ] . Normalizer-Free Networks replace normalization with scaled activations and adaptive gradient clipping, enabling stable large-scale training without normalization layers [ Brock et al., 2021 ] . We discuss Fixup and ReZero-style identity initialization through the RKSP lens in Appendix J .

[37] h5: Positioning of this study.

[38] p: RKSP uses Koopman spectra as an initialization-time diagnostic: from a single forward pass, we estimate layer-wise operators and predict divergence risk. Unlike Koopman representation learning for forecasting [ Lusch et al., 2017 , Williams et al., 2015 , Korda and Mezic, 2018 ] , our near-unit mass M ≈ 1 M_{\approx 1} provides a measurable handle on critical signal propagation [ Schoenholz et al., 2017 , Poole et al., 2016 , Pennington et al., 2017 ] and captures instabilities beyond neural tangent kernel analyses [ Jacot et al., 2018 ] ; we make it actionable via KSS and validate it in no-normalization regimes [ Zhang et al., 2019 , Brock et al., 2021 ] .

[39] h2: 3 Method

[40] h3: 3.1 Problem Setup

[41] h5: Divergence Definition

[42] p: A training run is marked as diverged if, at any step, the loss exceeds 50.0 or the gradient norm exceeds 500.0. This criterion defines the binary label D ∈ { 0 , 1 } D\in\{0,1\} used throughout our experiments.

[43] h5: Divergence Prediction Task

[44] p: Given a model architecture, normalization strategy, optimizer choice, and dataset, we collect N N residual-stream snapshots at initialization from a single forward pass and compute the spectral profile 𝒮 \mathcal{S} . A probabilistic predictor then maps 𝒮 \mathcal{S} to P ⁡ ( D = 1 ∣ 𝒮 ) P(D=1\mid\mathcal{S}) , estimating divergence risk before training begins.

[45] h3: 3.2 Residual Koopman Spectral Profiling

[46] p: Algorithm 1 summarizes our RKSP procedure. The algorithm computes DMD for each layer to obtain its spectral profile: ρ ℓ \rho_{\ell} denotes the spectral radius of 𝐀 ^ ℓ \hat{\mathbf{A}}_{\ell} , κ ℓ \kappa_{\ell} the eigenvector condition number of its eigenbasis, and 𝒦 ℓ \mathcal{K}_{\ell} the Kreiss constant (Appendix B ).

[47] figure: Algorithm 1 Residual Koopman Spectral Profiling 1: Model ℳ \mathcal{M} with L L layers; dataset 𝒟 \mathcal{D} ; the number of samples N N 2: Spectral profile 𝒮 = { ( M ≈ 1 ℓ , ρ ℓ , κ ℓ , η nl ℓ , 𝒦 ℓ ) } ℓ = 0 L − 1 \mathcal{S}=\{(M_{\approx 1}^{\ell},\rho_{\ell},\kappa_{\ell},\eta_{\mathrm{nl}}^{\ell},\mathcal{K}_{\ell})\}_{\ell=0}^{L-1} 3: Collect residuals: for each batch 𝐱 ∈ 𝒟 \mathbf{x}\in\mathcal{D} , store { 𝐡 ℓ ​ ( 𝐱 ) } ℓ = 0 L \{\mathbf{h}_{\ell}(\mathbf{x})\}_{\ell=0}^{L} 4: for ℓ = 0 , … , L − 1 \ell=0,\ldots,L-1 do 5: Form snapshot matrices 𝐗 ℓ , 𝐘 ℓ ∈ ℝ d × N \mathbf{X}_{\ell},\mathbf{Y}_{\ell}\in\mathbb{R}^{d\times N} 6: Whitening: 𝐗 ~ ℓ = 𝚺 ^ ℓ − 1 / 2 ( 𝐗 ℓ − 𝐗 ¯ ℓ ) \tilde{\mathbf{X}}_{\ell}=\hat{\boldsymbol{\Sigma}}_{\ell}^{-1/2}(\mathbf{X}_{\ell}-\bar{\mathbf{X}}_{\ell}) , 𝐘 ~ ℓ = 𝚺 ^ ℓ − 1 / 2 ( 𝐘 ℓ − 𝐘 ¯ ℓ ) \tilde{\mathbf{Y}}_{\ell}=\hat{\boldsymbol{\Sigma}}_{\ell}^{-1/2}(\mathbf{Y}_{\ell}-\bar{\mathbf{Y}}_{\ell}) 7: DMD: 𝐀 ^ ℓ = 𝐘 ~ ℓ ​ 𝐗 ~ ℓ † \hat{\mathbf{A}}_{\ell}=\tilde{\mathbf{Y}}_{\ell}\tilde{\mathbf{X}}_{\ell}^{\dagger} 8: Eigendecomposition: 𝐀 ^ ℓ = 𝐕 ℓ ​ 𝚲 ℓ ​ 𝐕 ℓ − 1 \hat{\mathbf{A}}_{\ell}=\mathbf{V}_{\ell}\boldsymbol{\Lambda}_{\ell}\mathbf{V}_{\ell}^{-1} 9: Compute M ≈ 1 ℓ , ρ ℓ , κ ℓ M_{\approx 1}^{\ell},\rho_{\ell},\kappa_{\ell} , nonlinearity η nl ℓ \eta_{\mathrm{nl}}^{\ell} , Kreiss 𝒦 ℓ \mathcal{K}_{\ell} 10: end for 11: Aggregate mean, max, min, std across layers 12: return 𝒮 \mathcal{S}

[48] h4: 3.2.1 Snapshot Construction

[49] p: RKSP applies DMD to each layer transition 𝐡 ℓ → 𝐡 ℓ + 1 \mathbf{h}_{\ell}\to\mathbf{h}_{\ell+1} as described in Eq. 1 . Let { 𝐱 i } i = 1 N \{\mathbf{x}_{i}\}_{i=1}^{N} denote the N N inputs used to form the snapshots. For layer ℓ \ell , define the paired residual vectors 𝐱 i ( ℓ ) = 𝐡 ℓ ​ ( 𝐱 i ) \mathbf{x}_{i}^{(\ell)}=\mathbf{h}_{\ell}(\mathbf{x}_{i}) and 𝐲 i ( ℓ ) = 𝐡 ℓ + 1 ​ ( 𝐱 i ) \mathbf{y}_{i}^{(\ell)}=\mathbf{h}_{\ell+1}(\mathbf{x}_{i}) . The snapshot matrices are

[50] table: 𝐗 ℓ \displaystyle\mathbf{X}_{\ell} = [ 𝐱 1 ( ℓ ) , … , 𝐱 N ( ℓ ) ] , \displaystyle=[\mathbf{x}_{1}^{(\ell)},\ldots,\mathbf{x}_{N}^{(\ell)}], (4) 𝐘 ℓ \displaystyle\mathbf{Y}_{\ell} = [ 𝐲 1 ( ℓ ) , … , 𝐲 N ( ℓ ) ] ∈ ℝ d × N , \displaystyle=[\mathbf{y}_{1}^{(\ell)},\ldots,\mathbf{y}_{N}^{(\ell)}]\in\mathbb{R}^{d\times N},

[51] p: so each column pair corresponds to the same sample. Unlike standard DMD, which uses time-shifted trajectories, RKSP pairs columns across different samples. Concretely, column i i in 𝐗 \mathbf{X} is the residual snapshot 𝐡 ℓ ​ ( 𝐱 i ) \mathbf{h}_{\ell}(\mathbf{x}_{i}) and column i i in 𝐘 \mathbf{Y} is the corresponding next-layer snapshot 𝐡 ℓ + 1 ​ ( 𝐱 i ) \mathbf{h}_{\ell+1}(\mathbf{x}_{i}) for the same sample 𝐱 i \mathbf{x}_{i} ; columns index independent samples, not time steps of a single trajectory. For each layer, DMD yields a local linear approximation 𝐀 ^ ℓ \hat{\mathbf{A}}_{\ell} whose spectrum characterizes the dynamics at that depth.

[52] p: To quantify how well this linear approximation fits the data, we define the nonlinearity ratio in whitened coordinates:

[53] table: η nl ​ ( ℓ ) ≔ ‖ 𝐘 ~ ℓ − 𝐀 ^ ℓ ​ 𝐗 ~ ℓ ‖ F ‖ 𝐘 ~ ℓ − 𝐗 ~ ℓ ‖ F + ε nl , \eta_{\mathrm{nl}}(\ell)\coloneqq\frac{\left\|\tilde{\mathbf{Y}}_{\ell}-\hat{\mathbf{A}}_{\ell}\tilde{\mathbf{X}}_{\ell}\right\|_{F}}{\left\|\tilde{\mathbf{Y}}_{\ell}-\tilde{\mathbf{X}}_{\ell}\right\|_{F}+\varepsilon_{\mathrm{nl}}}, (5)

[54] p: where ε nl > 0 \varepsilon_{\mathrm{nl}}>0 is a small constant that prevents division by zero. This ratio η nl \eta_{\mathrm{nl}} normalizes the fit error by the update magnitude. When the residual update ‖ 𝐘 ~ ℓ − 𝐗 ~ ℓ ‖ F \left\|\tilde{\mathbf{Y}}_{\ell}-\tilde{\mathbf{X}}_{\ell}\right\|_{F} is tiny, η nl \eta_{\mathrm{nl}} can be large even for small absolute errors. We therefore use η nl \eta_{\mathrm{nl}} primarily as a DMD reliability flag rather than as a pure measure of nonlinearity.

[55] h4: 3.2.2 Whitened DMD and Reliability Filtering

[56] p: DMD approximates the Koopman operator from data snapshots. Given paired snapshot matrices 𝐗 = [ 𝐱 1 , … , 𝐱 N ] ∈ ℝ d × N \mathbf{X}=[\mathbf{x}_{1},\ldots,\mathbf{x}_{N}]\in\mathbb{R}^{d\times N} and 𝐘 = [ 𝐲 1 , … , 𝐲 N ] ∈ ℝ d × N \mathbf{Y}=[\mathbf{y}_{1},\ldots,\mathbf{y}_{N}]\in\mathbb{R}^{d\times N} , DMD solves for the optimal linear operator:

[57] table: 𝐀 ^ DMD = argmin 𝐀 ∈ ℝ d × d ‖ 𝐘 − 𝐀𝐗 ‖ F 2 = 𝐘𝐗 † , \hat{\mathbf{A}}_{\mathrm{DMD}}=\argmin_{\mathbf{A}\in\mathbb{R}^{d\times d}}\left\|\mathbf{Y}-\mathbf{A}\mathbf{X}\right\|_{F}^{2}=\mathbf{Y}\mathbf{X}^{\dagger}, (6)

[58] p: where 𝐗 † \mathbf{X}^{\dagger} denotes the Moore-Penrose pseudoinverse.

[59] p: To ensure scale-invariance and numerical stability, we apply 𝐗 \mathbf{X} -based zero-phase component analysis whitening [ Kessy et al., 2018 ] :

[60] table: 𝐗 ~ \displaystyle\tilde{\mathbf{X}} = 𝚺 ^ X − 1 / 2 ( 𝐗 − 𝐗 ¯ 𝟏 ⊤ ) , \displaystyle=\hat{\boldsymbol{\Sigma}}_{X}^{-1/2}(\mathbf{X}-\bar{\mathbf{X}}\mathbf{1}^{\top}), (7) 𝐘 ~ \displaystyle\tilde{\mathbf{Y}} = 𝚺 ^ X − 1 / 2 ( 𝐘 − 𝐘 ¯ 𝟏 ⊤ ) , \displaystyle=\hat{\boldsymbol{\Sigma}}_{X}^{-1/2}(\mathbf{Y}-\bar{\mathbf{Y}}\mathbf{1}^{\top}), (8) 𝚺 ^ X \displaystyle\hat{\boldsymbol{\Sigma}}_{X} = 1 N − 1 ​ ( 𝐗 − 𝐗 ¯ ​ 𝟏 ⊤ ) ​ ( 𝐗 − 𝐗 ¯ ​ 𝟏 ⊤ ) ⊤ + ϵ ​ 𝐈 \displaystyle=\frac{1}{N-1}(\mathbf{X}-\bar{\mathbf{X}}\mathbf{1}^{\top})(\mathbf{X}-\bar{\mathbf{X}}\mathbf{1}^{\top})^{\top}+\epsilon\mathbf{I} (9)

[61] p: where 𝐗 ¯ = 1 N ​ ∑ i = 1 N 𝐱 i \bar{\mathbf{X}}=\frac{1}{N}\sum_{i=1}^{N}\mathbf{x}_{i} , 𝐘 ¯ = 1 N ​ ∑ i = 1 N 𝐲 i \bar{\mathbf{Y}}=\frac{1}{N}\sum_{i=1}^{N}\mathbf{y}_{i} , and ϵ > 0 \epsilon>0 ensures invertibility. The same whitening matrix is applied to both 𝐗 \mathbf{X} and 𝐘 \mathbf{Y} , so the regression operates within a single, 𝐗 \mathbf{X} -normalized coordinate system. This whitening step ensures cross-model comparability and yields coordinate-invariant spectral estimates.

[62] p: From the whitened data, we form the DMD operator 𝐀 ^ = 𝐘 ~ ​ 𝐗 ~ † \hat{\mathbf{A}}=\tilde{\mathbf{Y}}\tilde{\mathbf{X}}^{\dagger} and compute its eigendecomposition 𝐀 ^ = 𝐕 ​ 𝚲 ​ 𝐕 − 1 \hat{\mathbf{A}}=\mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1} . To report the eigenvector condition number κ ⁡ ( 𝐕 ) = ‖ 𝐕 ‖ 2 ​ ‖ 𝐕 − 1 ‖ 2 \kappa(\mathbf{V})=\left\|\mathbf{V}\right\|_{2}\left\|\mathbf{V}^{-1}\right\|_{2} , we first normalize each right eigenvector to have unit Euclidean norm. This normalization fixes the otherwise arbitrary scaling of 𝐕 \mathbf{V} and makes κ ⁡ ( 𝐕 ) \kappa(\mathbf{V}) reproducible.

[63] p: To identify spurious eigenvalues, we apply residual DMD (ResDMD) reliability filtering [ Colbrook et al., 2022 ] . For each eigenvalue λ j \lambda_{j} with left eigenvector 𝐮 j \mathbf{u}_{j} satisfying 𝐮 j ∗ ​ 𝐀 ^ = λ j ​ 𝐮 j ∗ \mathbf{u}_{j}^{*}\hat{\mathbf{A}}=\lambda_{j}\mathbf{u}_{j}^{*} , we compute the per-mode residual:

[64] table: r j = ‖ 𝐮 j ∗ ​ ( 𝐘 ~ − λ j ​ 𝐗 ~ ) ‖ 2 ‖ 𝐮 j ∗ ​ 𝐗 ~ ‖ 2 + ε r , r_{j}=\frac{\left\|\mathbf{u}_{j}^{*}(\tilde{\mathbf{Y}}-\lambda_{j}\tilde{\mathbf{X}})\right\|_{2}}{\left\|\mathbf{u}_{j}^{*}\tilde{\mathbf{X}}\right\|_{2}+\varepsilon_{r}}, (10)

[65] p: where ε r > 0 \varepsilon_{r}>0 prevents division by zero. Eigenvalues with r j > τ r_{j}>\tau are flagged as unreliable and potentially spurious; we use a default threshold of τ = 0.1 \tau=0.1 to filter them out.

[66] h4: 3.2.3 Spectral Mass

[67] p: Now, we define our criterion for divergence prediction.

[68] h6: Definition 1 (Spectral Mass Partition) .

[69] p: For DMD eigenvalues Λ = { λ j } j = 1 m \Lambda=\{\lambda_{j}\}_{j=1}^{m} of an operator 𝐀 ^ \hat{\mathbf{A}} , with m m the number of eigenvalues used, we define the following bins; they are disjoint provided δ c ≥ ϵ n \delta_{c}\geq\epsilon_{n} :

[70] table: M > 1 ​ ( 𝐀 ^ ) \displaystyle M_{>1}(\hat{\mathbf{A}}) ≜ 1 m ∑ j = 1 m 𝟏 [ | λ j | > 1 + ϵ u ] , \displaystyle\triangleq\frac{1}{m}\sum_{j=1}^{m}\mathbf{1}[|\lambda_{j}|>1+\epsilon_{u}], (11) M ≈ 1 ​ ( 𝐀 ^ ) \displaystyle M_{\approx 1}(\hat{\mathbf{A}}) ≜ 1 m ∑ j = 1 m 𝟏 [ | λ j | ∈ [ 1 − ϵ n , 1 + ϵ u ] ] , \displaystyle\triangleq\frac{1}{m}\sum_{j=1}^{m}\mathbf{1}[|\lambda_{j}|\in[1-\epsilon_{n},1+\epsilon_{u}]], (12) M < 1 ​ ( 𝐀 ^ ) \displaystyle M_{<1}(\hat{\mathbf{A}}) ≜ 1 m ∑ j = 1 m 𝟏 [ | λ j | < 1 − δ c ] , \displaystyle\triangleq\frac{1}{m}\sum_{j=1}^{m}\mathbf{1}[|\lambda_{j}|<1-\delta_{c}], (13)

[71] p: where the three quantities denote the expansive mass, near-unit mass, and contractive mass, respectively. When δ c > ϵ n \delta_{c}>\epsilon_{n} , these three bins are not exhaustive; the remaining intermediate mass is M mid ​ ( 𝐀 ^ ) ≜ 1 − M > 1 ​ ( 𝐀 ^ ) − M ≈ 1 ​ ( 𝐀 ^ ) − M < 1 ​ ( 𝐀 ^ ) M_{\mathrm{mid}}(\hat{\mathbf{A}})\triangleq 1-M_{>1}(\hat{\mathbf{A}})-M_{\approx 1}(\hat{\mathbf{A}})-M_{<1}(\hat{\mathbf{A}}) .

[72] p: For example, m = d m=d for full DMD, m = r m=r for rank- r r randomized DMD [ Erichson et al., 2019 ] , or m m equals the count remaining after reliability filtering. We use default thresholds ϵ u = 0.05 \epsilon_{u}=0.05 , ϵ n = 0.10 \epsilon_{n}=0.10 , and δ c = 0.20 \delta_{c}=0.20 . Figure 1 shows a representative eigenvalue scatter that motivates these bins.

[73] figure: Figure 1: Scatter plot of DMD eigenvalues across layers in a pre-layer normalization transformer. The color gradient indicates layer depth; blue is early and red is late. Early layers cluster near the unit circle; late layers exhibit an increased spectral radius.

[74] h5: Metric Interpretation.

[75] p: For divergence prediction, we use M ≈ 1 M_{\approx 1} itself as the scalar score and compute the AUROC against the divergence labels. Note that the expansive mass M > 1 M_{>1} tracks eigenvalues outside the unit circle but does not map one-to-one with empirical divergence. Four factors explain this gap between M > 1 M_{>1} and observed divergence. First, whitening rescales local coordinates, so raw eigenvalue magnitudes differ from unwhitened values. Second, DMD provides only a local linear approximation of the true nonlinear dynamics. Third, non-normal transient growth can trigger instability even when few eigenvalues exceed 1 [ Trefethen and Embree, 2020 ] . Additionally, our divergence labels use coarse thresholds on loss or gradient norm, so finite-horizon training within the evaluation window can remain stable despite a nonzero M > 1 M_{>1} . These four factors together explain cases like Pre-LN, which shows a nonzero M > 1 M_{>1} but 0% divergence in Table 1 .

[76] h3: 3.3 Koopman Spectral Shaping

[77] p: While RKSP diagnoses instability, KSS prevents it. KSS adds a differentiable spectral regularizer to the training objective that steers eigenvalues away from the unstable region while reducing excessive near-unit mass to restore damping without causing over-contraction. The total objective becomes ℒ total = ℒ task + α ​ ∑ ℓ ∈ 𝒮 ℒ KSS ℓ / | 𝒮 | \mathcal{L}_{\mathrm{total}}=\mathcal{L}_{\mathrm{task}}+\alpha\sum_{\ell\in\mathcal{S}}\mathcal{L}_{\mathrm{KSS}}^{\ell}/|\mathcal{S}| , where 𝒮 \mathcal{S} samples 50% of layers per update.

[78] h6: Definition 2 (KSS Regularization Loss) .

[79] p: For layer ℓ \ell with randomized DMD eigenvalues { λ j ℓ } j = 1 r \{\lambda_{j}^{\ell}\}_{j=1}^{r} , the KSS loss is

[80] table: ℒ KSS ℓ \displaystyle\mathcal{L}_{\mathrm{KSS}}^{\ell} = ∑ j = 1 r σ ⁡ ( T ⁡ ( | λ j ℓ | − τ u ) ) ⋅ softplus ⁡ ( | λ j ℓ | − τ u ) 2 ⏟ Unstable penalty \displaystyle=\underbrace{\sum_{j=1}^{r}\sigma(T(|\lambda_{j}^{\ell}|-\tau_{u}))\cdot\softplus(|\lambda_{j}^{\ell}|-\tau_{u})^{2}}_{\text{Unstable penalty}} (14) + β ⋅ ( m ℓ soft − γ ) 2 ⏟ Near-unit target \displaystyle+\underbrace{\beta\cdot(m_{\ell}^{\mathrm{soft}}-\gamma)^{2}}_{\text{Near-unit target}}

[81] p: where σ ⁡ ( ⋅ ) \sigma(\cdot) denotes the sigmoid function and

[82] table: m ℓ soft = 1 r ​ ∑ j = 1 r σ ⁡ ( T ⁡ ( | λ j ℓ | − τ l ) ) ⋅ σ ⁡ ( T ⁡ ( τ u − | λ j ℓ | ) ) . m_{\ell}^{\mathrm{soft}}=\frac{1}{r}\sum_{j=1}^{r}\sigma(T(|\lambda_{j}^{\ell}|-\tau_{l}))\cdot\sigma(T(\tau_{u}-|\lambda_{j}^{\ell}|)). (15)

[83] p: This term facilitates reducing excessive near-unit mass while preventing it from becoming too small by nudging m ℓ soft m_{\ell}^{\mathrm{soft}} toward the target band γ \gamma . We use the default hyperparameters T = 20 T=20 , τ u = 1.05 \tau_{u}=1.05 , τ l = 0.90 \tau_{l}=0.90 , and γ ∈ [ 0.3 , 0.5 ] \gamma\in[0.3,0.5] . Full hyperparameter settings and the practical training recipe appear in Appendix D .

[84] h2: 4 Theoretical Analysis

[85] p: We interpret the near-unit mass M ≈ 1 M_{\approx 1} as an instability score. Two mechanisms support this view. First, when the layer linearization is approximately normal, eigenvalues accurately reflect singular values, so concentration near | λ | ≈ 1 |\lambda|\approx 1 implies near-isometric propagation and weak damping. Second, weak damping allows perturbations and optimization noise to persist across depth; in aggressive optimization regimes, this behavior raises divergence risk. We formalize the energy-preservation statement below and highlight non-normality as a caveat.

[86] h6: Theorem 1 (Near-Unit Energy Preservation under Near-Normality) .

[87] p: Let 𝐀 ∈ ℂ d × d \mathbf{A}\in\mathbb{C}^{d\times d} be normal with eigenvalues { λ j } j = 1 d \{\lambda_{j}\}_{j=1}^{d} . For a unit vector 𝐱 \mathbf{x} drawn uniformly on the sphere,

[88] table: 𝔼 ​ ‖ 𝐀𝐱 ‖ 2 2 = 1 d ​ ∑ j = 1 d | λ j | 2 . \mathbb{E}\left\|\mathbf{A}\mathbf{x}\right\|_{2}^{2}=\frac{1}{d}\sum_{j=1}^{d}|\lambda_{j}|^{2}. (16)

[89] p: If ρ ⁡ ( 𝐀 ) ≤ 1 + ϵ u \rho(\mathbf{A})\leq 1+\epsilon_{u} and M ≈ 1 ​ ( 𝐀 ) M_{\approx 1}(\mathbf{A}) denotes the fraction of eigenvalues with | λ j | ∈ [ 1 − ϵ n , 1 + ϵ u ] |\lambda_{j}|\in[1-\epsilon_{n},1+\epsilon_{u}] , then

[90] table: ( 1 − ϵ n ) 2 ​ M ≈ 1 ​ ( 𝐀 ) ≤ 𝔼 ​ ‖ 𝐀𝐱 ‖ 2 2 ≤ ( 1 + ϵ u ) 2 . (1-\epsilon_{n})^{2}M_{\approx 1}(\mathbf{A})\leq\mathbb{E}\left\|\mathbf{A}\mathbf{x}\right\|_{2}^{2}\leq(1+\epsilon_{u})^{2}. (17)

[91] p: Hence larger M ≈ 1 M_{\approx 1} implies more energy-preserving and less damped propagation; this corresponds to higher instability risk. More generally, if 𝐀 \mathbf{A} is diagonalizable with 𝐀 = 𝐕 ​ 𝚲 ​ 𝐕 − 1 \mathbf{A}=\mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1} , then the same conclusion holds up to factors κ ​ ( 𝐕 ) ± 2 \kappa(\mathbf{V})^{\pm 2} :

[92] table: ( 1 − ϵ n ) 2 κ ​ ( 𝐕 ) 2 ​ M ≈ 1 ​ ( 𝐀 ) ≤ 𝔼 ​ ‖ 𝐀𝐱 ‖ 2 2 ≤ κ ​ ( 𝐕 ) 2 ​ ( 1 + ϵ u ) 2 . \frac{(1-\epsilon_{n})^{2}}{\kappa(\mathbf{V})^{2}}M_{\approx 1}(\mathbf{A})\leq\mathbb{E}\left\|\mathbf{A}\mathbf{x}\right\|_{2}^{2}\leq\kappa(\mathbf{V})^{2}(1+\epsilon_{u})^{2}. (18)

[93] h6: Corollary 2 (Depth-wise Damping and Gradient Flow) .

[94] p: Consider a depth- L L linearization 𝐡 ℓ + 1 = 𝐀 ℓ ​ 𝐡 ℓ \mathbf{h}_{\ell+1}=\mathbf{A}_{\ell}\mathbf{h}_{\ell} where each 𝐀 ℓ \mathbf{A}_{\ell} is a normal and ρ ⁡ ( 𝐀 ℓ ) ≤ 1 + ϵ u \rho(\mathbf{A}_{\ell})\leq 1+\epsilon_{u} . Assume that each layer has an isotropic second moment, that is, 𝔼 ⁡ [ 𝐡 ℓ ​ 𝐡 ℓ ∗ ] = 1 d ​ 𝔼 ​ ‖ 𝐡 ℓ ‖ 2 2 ​ 𝐈 \mathbb{E}[\mathbf{h}_{\ell}\mathbf{h}_{\ell}^{*}]=\frac{1}{d}\mathbb{E}\left\|\mathbf{h}_{\ell}\right\|_{2}^{2}\mathbf{I} for ℓ = 0 , … , L − 1 \ell=0,\dots,L-1 . For example, 𝐡 ℓ ‖ 𝐡 ℓ ‖ 2 \frac{\mathbf{h}_{\ell}}{\left\|\mathbf{h}_{\ell}\right\|_{2}} is uniform on the sphere. Let q ℓ ≜ 1 d ​ ∑ j = 1 d | λ j ℓ | 2 q_{\ell}\triangleq\frac{1}{d}\sum_{j=1}^{d}|\lambda_{j}^{\ell}|^{2} be the average energy gain of layer ℓ \ell . Then

[95] table: 𝔼 ​ ‖ 𝐡 L ‖ 2 2 = 𝔼 ​ ‖ 𝐡 0 ‖ 2 2 ​ ∏ ℓ = 0 L − 1 q ℓ , \mathbb{E}\left\|\mathbf{h}_{L}\right\|_{2}^{2}=\mathbb{E}\left\|\mathbf{h}_{0}\right\|_{2}^{2}\prod_{\ell=0}^{L-1}q_{\ell}, (19)

[96] p: and q ℓ ≥ ( 1 − ϵ n ) 2 ​ M ≈ 1 ​ ( 𝐀 ℓ ) q_{\ell}\geq(1-\epsilon_{n})^{2}M_{\approx 1}(\mathbf{A}_{\ell}) . Thus, a larger M ≈ 1 M_{\approx 1} reduces the exponential contraction of signals and gradients; in high learning rate regimes, this weaker damping elevates instability risk, although a very small M ≈ 1 M_{\approx 1} can hurt expressivity.

[97] p: The proof appears in Appendix C .

[98] h5: Non-normality caveat.

[99] p: When κ ⁡ ( 𝐕 ) ≫ 1 \kappa(\mathbf{V})\gg 1 , non-normal transient growth can occur even if ρ ⁡ ( 𝐀 ) ≤ 1 \rho(\mathbf{A})\leq 1 , and eigenvalues near the unit circle may be perturbation-sensitive. We therefore track κ ⁡ ( 𝐕 ) \kappa(\mathbf{V}) alongside M ≈ 1 M_{\approx 1} . Appendix B and Appendix C characterize transient growth via the Kreiss theorem, provide normality-related bounds, and formalize the trade-off between instability and expressivity.

[100] h2: 5 Experiments

[101] h3: 5.1 Experimental Settings

[102] p: Our experiments target Generative Pretrained Transformer (GPT-2)-style transformers [ Radford et al., 2019 , Vaswani et al., 2017 ] with d ∈ { 128,256,512,768 , 1024 } d\in\{128,256,512,768,1024\} and L ∈ { 4 , 6 , 8 , 12 , 16 , 24 } L\in\{4,6,8,12,16,24\} , spanning 1M to 350M parameters. We compare six normalization strategies: pre-layer normalization (Pre-LN), post-layer normalization (Post-LN), root mean square normalization (RMSNorm) [ Zhang and Sennrich, 2019 ] , DeepNorm [ Wang et al., 2024 ] , sub-layer normalization (SubLN) [ Xiong et al., 2020 ] , and no normalization (No-Norm). The evaluation tasks include an associative-recall classification task (Appendix D.1 ); language modeling (LM) tasks including our synthetic LM with next-token prediction (Appendix D.2 ), WikiText-103 [ Merity et al., 2017 ] , and OpenWebText-style LM [ Gokaslan and Cohen, 2019 ] ; and ViT experiments [ Dosovitskiy et al., 2021 ] on the Canadian Institute for Advanced Research (CIFAR-10) dataset [ Krizhevsky et al., 2009 ] . We report AUROC for discrimination, with 95% bootstrap confidence intervals (CIs) based on 1000 resamples. Statistical significance of divergence rates is assessed using Fisher’s exact test and run with three random seeds per setting. Full hyperparameters and hardware details appear in Appendix D .

[103] h3: 5.2 Prediction at Initialization

[104] h5: Main Results: Normalization Comparison.

[105] p: Table 1 reveals three key findings. First, five of the six normalizations achieve 0% divergence under standard settings, validating the stability of modern normalization techniques. Second, No-Norm diverges in 96.4% of runs and also has high near-unit mass, with M ≈ 1 = 0.80 M_{\approx 1}=0.80 ; under its relatively low non-normality, with κ ⁡ ( 𝐕 ) = 1.11 \kappa(\mathbf{V})=1.11 , this is consistent with M ≈ 1 M_{\approx 1} acting as an instability indicator. Non-normality and expansive mass still matter, but within comparable regimes, a larger M ≈ 1 M_{\approx 1} aligns with greater instability, as discussed in Section 4 . Third, spectral signatures differ systematically across normalizations: Pre-LN and RMSNorm are more contractive with lower M ≈ 1 M_{\approx 1} , Post-LN retains a higher near-unit structure, and DeepNorm shifts mass into the unstable bin but remains bounded through scaling. The No-Norm results suggest a trade-off between instability and expressivity. Only three of 84 No-Norm runs converged, but their accuracy reached 54.2% ± \pm 24.4%—higher than other methods. Among stable methods, DeepNorm achieves the best balance, with 20.0% accuracy and 0% divergence.

[106] figure: Table 1: Comprehensive normalization comparison across different setups. RKSP metrics reveal distinct spectral signatures explaining stability differences. Accuracy is computed from only 3 converged runs out of 84. Statistical significance: No-Norm divergence compared with others, p < 10 − 50 p<10^{-50} via Fisher’s exact test. AUROC for divergence prediction using M ≈ 1 M_{\approx 1} : 0.995 [95% CI: 0.986 to 1.00]. Measured on the associative-recall task. Norm Type n n Div.% (lower) M ≈ 1 M_{\approx 1} M > 1 M_{>1} ρ \rho Acc.% (higher) Pre-LN 25 0.0 \mathbf{0.0} 0.16 ± 0.01 0.16\pm 0.01 0.54 ± 0.01 0.54\pm 0.01 2.29 ± 0.04 2.29\pm 0.04 7.5 ± 8.7 7.5\pm 8.7 Post-LN 69 0.0 \mathbf{0.0} 0.66 ± 0.02 0.66\pm 0.02 0.31 ± 0.01 0.31\pm 0.01 7.48 ± 0.12 7.48\pm 0.12 1.4 ± 5.8 1.4\pm 5.8 RMSNorm 12 0.0 \mathbf{0.0} 0.16 ± 0.01 0.16\pm 0.01 0.54 ± 0.01 0.54\pm 0.01 2.28 ± 0.06 2.28\pm 0.06 13.1 ± 8.6 13.1\pm 8.6 DeepNorm 12 0.0 \mathbf{0.0} 0.00 ± 0.00 0.00\pm 0.00 1.00 ± 0.00 1.00\pm 0.00 3.94 ± 0.21 3.94\pm 0.21 20.0 ± 9.4 \mathbf{20.0\pm 9.4} SubLN 12 0.0 \mathbf{0.0} 0.13 ± 0.02 0.13\pm 0.02 0.54 ± 0.01 0.54\pm 0.01 2.23 ± 0.03 2.23\pm 0.03 9.0 ± 8.1 9.0\pm 8.1 No-Norm 84 96.4 96.4 0.80 ± 0.02 0.80\pm 0.02 0.19 ± 0.01 0.19\pm 0.01 1.11 ± 0.01 1.11\pm 0.01 54.2 ± 24.4 ∗ 54.2\pm 24.4^{*}

[107] h5: AUROC Analysis for Divergence Prediction.

[108] p: Table 2 compares spectral predictors against gradient baselines. We use the monotone risk score M ≈ 1 M_{\approx 1} for divergence prediction. This achieves an AUROC of 0.995 at initialization, representing a 31% relative improvement over the best gradient-based method with an AUROC of 0.758. The superiority is statistically significant: the 95% CI lower bound of M ≈ 1 M_{\approx 1} of 0.986 exceeds the upper bounds of all gradient-based methods.

[109] figure: Table 2: AUROC for divergence prediction with bootstrap 95% confidence intervals. The M ≈ 1 M_{\approx 1} CI lower bound of 0.986 exceeds gradient baselines’ upper bounds. Measured on the associative-recall normalization sweep. Predictor AUROC (higher) 95% CI Timing M ≈ 1 M_{\approx 1} at initialization 0.995 \mathbf{0.995} [ 0.986 , 1.000 ] [0.986,1.000] Initialization M ≈ 1 × log 10 ⁡ ( κ ⁡ ( 𝐕 ) ) M_{\approx 1}\times\log_{10}(\kappa(\mathbf{V})) 0.873 0.873 [ 0.841 , 0.905 ] [0.841,0.905] Initialization Spectral radius ρ \rho at init 0.845 0.845 [ 0.808 , 0.882 ] [0.808,0.882] Initialization Eigenvector condition κ ⁡ ( 𝐕 ) \kappa(\mathbf{V}) at init 0.687 0.687 [ 0.638 , 0.736 ] [0.638,0.736] Initialization Gradient-Based Baselines Initial gradient norm 0.621 0.621 [ 0.568 , 0.674 ] [0.568,0.674] After 1 step Gradient norm at step 100 0.685 0.685 [ 0.635 , 0.735 ] [0.635,0.735] Step 100 Gradient variance over steps 1 to 100 0.702 0.702 [ 0.654 , 0.750 ] [0.654,0.750] Through step 100 Loss spike count over steps 1 to 500 0.758 0.758 [ 0.712 , 0.804 ] [0.712,0.804] Through step 500

[110] h3: 5.3 Effect of KSS on Stability

[111] h5: KSS Results.

[112] p: Table 3 compares gradient clipping with KSS in the No-Norm setting. These two approaches differ fundamentally in their mechanism. Gradient clipping operates reactively: it caps gradients after explosion begins but does not prevent instability, yielding only modest improvements. KSS, in contrast, operates proactively by shaping the spectral distribution before instability occurs. With α = 0.15 \alpha=0.15 , KSS reduces divergence from 66.7% to 12.5%. Figure 2 visualizes the dose-response relationship between the KSS weight, M ≈ 1 M_{\approx 1} , and training stability.

[113] figure: Table 3: Gradient clipping versus KSS in a challenging No-Norm setting with learning rate that ranges from 0.005 to 0.01 and 24 trials each. Measured on the associative-recall task. Method Div.% (lower) Acc.% (higher) M ≈ 1 M_{\approx 1} Overhead No control 66.7 66.7 28.5 28.5 0.85 0.85 — Gradient clip 0.5 50.0 50.0 32.1 32.1 0.82 0.82 < 1 % <1\% Gradient clip 1.0 58.3 58.3 30.8 30.8 0.83 0.83 < 1 % <1\% KSS α = 0.10 \alpha=0.10 25.0 25.0 42.3 42.3 0.68 0.68 9.5 % 9.5\% KSS α = 0.15 \alpha=0.15 12.5 \mathbf{12.5} 48.2 \mathbf{48.2} 0.58 0.58 10.8 % 10.8\% KSS α = 0.20 \alpha=0.20 8.3 8.3 46.5 46.5 0.52 0.52 11.2 % 11.2\%

[114] figure: Figure 2: KSS regularization effectiveness. (Left) The divergence rate decreases with KSS weight α \alpha . (Right) A dual axis shows accuracy improvement and M ≈ 1 M_{\approx 1} shifting downward toward the target band. KSS shapes spectral properties, improving both stability and performance. Measured on the associative-recall task.

[115] h5: Extended Baseline Comparison.

[116] p: Table 4 provides expanded baseline and optimizer results, including spectral normalization and weight normalization baselines [ Miyato et al., 2018 , Salimans and Kingma, 2016 ] . We use Adam with decoupled weight decay (AdamW) as the base optimizer in this comparison. Sharpness-Aware Minimization (SAM) [ Foret et al., 2021 ] reduces divergence to 33.3% but incurs a 2 × \times computational cost, whereas KSS achieves a 2.7 × \times lower divergence with 9 × \times less overhead. The Lion optimizer [ Chen et al., 2023 ] yields 45.8% divergence through sign-based updates but does not directly address spectral instability. Combining KSS with SAM achieves the lowest divergence at 8.3% but with higher overhead.

[117] figure: Table 4: Extended baseline comparison including SAM, spectral normalization, and the Lion optimizer. Measured on the associative-recall task. Method Div.% (lower) Acc.% (higher) Overhead No stabilization, AdamW 66.7 66.7 28.5 28.5 — Gradient clipping at 1.0 58.3 58.3 30.8 30.8 < 1 % <1\% Spectral normalization 41.7 41.7 35.2 35.2 5.2 % 5.2\% Weight normalization 54.2 54.2 32.8 32.8 3.8 % 3.8\% Gradient penalty with λ = 0.1 \lambda=0.1 45.8 45.8 33.1 33.1 6.4 % 6.4\% Advanced Optimizers SAM, ρ = 0.05 \rho=0.05 37.5 37.5 38.6 38.6 about 100% SAM, ρ = 0.10 \rho=0.10 33.3 33.3 40.2 40.2 about 100% Lion optimizer 45.8 45.8 36.5 36.5 about 15% KSS, α = 0.15 \alpha=0.15 12.5 \mathbf{12.5} 48.2 \mathbf{48.2} 10.8 % 10.8\% KSS + SAM, α = 0.10 \alpha=0.10 , ρ = 0.05 \rho=0.05 8.3 8.3 45.8 45.8 about 112%

[118] h5: KSS Enables Higher Learning Rates.

[119] p: By suppressing spectral instability, KSS allows us to safely increase the step size across different normalization choices. Table 5 shows a 50% to 150% increase in the maximum stable learning rate under the same divergence criterion.

[120] figure: Table 5: Maximum stable learning rate (LR). KSS enables learning rates that are 50% to 150% higher. The stability criterion is < < 20% divergence across trials. Measured on the associative-recall task. Norm Type Max LR w/o KSS Max LR w/ KSS Increase Pre-LN 0.005 0.005 0.008 0.008 + 60 % +60\% RMSNorm 0.003 0.003 0.005 0.005 + 67 % +67\% No-Norm 0.002 0.002 0.005 0.005 + 150 % +150\%

[121] h5: Mechanistic Evidence: KSS versus Random Regularization.

[122] p: KSS stabilizes training through spectral shaping rather than generic regularization. Table 6 addresses this point via ablation studies with matched computational overhead. Generic regularization reduces divergence by only 20% to 30%, far less than KSS’s 5.3 × \times reduction. Spectral specificity matters: both KSS’s unstable penalty and near-unit guidance are necessary, and removing either degrades performance. Let Δ ​ M ≈ 1 ≜ M ≈ 1 KSS − M ≈ 1 base \Delta M_{\approx 1}\triangleq M_{\approx 1}^{\mathrm{KSS}}-M_{\approx 1}^{\mathrm{base}} ; negative values indicate decreased near-unit mass. The correlation between Δ ​ M ≈ 1 \Delta M_{\approx 1} and divergence reduction has r = − 0.87 r=-0.87 and p < 0.001 p<0.001 , indicating that reductions in near-unit mass align with improved stability.

[123] figure: Table 6: Mechanism ablation: KSS versus random regularization. Same overhead at about 11%, different mechanisms. Results use the No-Norm setting, with learning rates ranging from 0.005 to 0.01 across 24 trials each. All methods are matched to about 11% computational overhead. Measured on the associative-recall task. Method Div.% (lower) Acc.% (higher) M ≈ 1 M_{\approx 1} Mechanism No regularization 66.7 66.7 28.5 28.5 0.85 0.85 — Generic Regularization, about 11% overhead Random ℓ 2 \ell_{2} on residuals 54.2 54.2 31.2 31.2 0.81 0.81 Magnitude damping Jacobian penalty 45.8 45.8 33.8 33.8 0.78 0.78 Gradient smoothness Activation variance reg. 50.0 50.0 32.5 32.5 0.80 0.80 Distribution control Spectral-Specific Regularization, about 11% overhead KSS, unstable penalty only 33.3 33.3 38.5 38.5 0.68 0.68 Spectral stability KSS, near-unit guidance only 41.7 41.7 36.2 36.2 0.72 0.72 Damping control KSS, full 12.5 \mathbf{12.5} 48.2 \mathbf{48.2} 0.58 \mathbf{0.58} Both mechanisms

[124] h5: Scaling Analysis.

[125] p: Table 7 extends KSS to 350M parameters. At this scale, KSS maintains sub-linear overhead scaling at 11.8% while reducing divergence from 25.0% to 12.5%.

[126] figure: Table 7: Scale-up KSS training results up to 350M parameters. Measured on the synthetic LM validation set with 24 trials on a synthetic LM task with vocab size 10K and a sequence length of 256. Model Params Method Div. of 24 (lower) PPL (lower) Overhead Extra Large, d = 1024 d=1024 , L = 24 L=24 350M Baseline 6 of 24 52.1 52.1 — Extra Large, d = 1024 d=1024 , L = 24 L=24 350M KSS 3 of 24 46.8 \mathbf{46.8} 11.8 % 11.8\%

[127] h3: 5.4 Real-World LM Validation

[128] p: RKSP and KSS generalize beyond synthetic tasks to real-world LMs. Table 8 demonstrates this generalization with WikiText-103 [ Merity et al., 2017 ] and OpenWebText experiments. Benefits with KSS persist on real data, manifesting in three ways. First, divergence decreases by 2 × \times to 5 × \times across model sizes. Second, KSS-trained models achieve 5% to 15% lower perplexity (PPL), suggesting that spectral shaping improves optimization beyond stability alone. Third, KSS enables 1.5 × \times to 2 × \times higher learning rates, accelerating convergence.

[129] figure: Table 8: KSS improves stability and PPL. Pre-LN normalization with 24 trials per configuration. Measured on WikiText-103 and OpenWebText language-modeling tasks. Model Params Method Div. of 24 (lower) PPL (lower) Max LR Steps Small, d = 256 d=256 , L = 6 L=6 25M Baseline 2 of 24 58.4 58.4 3 ​ e − 4 3\mathrm{e}{-4} 10K Small, d = 256 d=256 , L = 6 L=6 25M KSS 0 of 24 52.1 \mathbf{52.1} 5 ​ e − 4 5\mathrm{e}{-4} 10K Medium, d = 512 d=512 , L = 12 L=12 85M Baseline 4 of 24 42.3 42.3 2 ​ e − 4 2\mathrm{e}{-4} 10K Medium, d = 512 d=512 , L = 12 L=12 85M KSS 1 of 24 38.5 \mathbf{38.5} 4 ​ e − 4 4\mathrm{e}{-4} 10K Large, d = 768 d=768 , L = 12 L=12 125M Baseline 5 of 24 48.7 48.7 1.5 ​ e − 4 1.5\mathrm{e}{-4} 10K Large, d = 768 d=768 , L = 12 L=12 125M KSS 2 of 24 43.2 \mathbf{43.2} 3 ​ e − 4 3\mathrm{e}{-4} 10K

[130] h3: 5.5 ViT Experiments

[131] p: RKSP generalizes to ViTs [ Dosovitskiy et al., 2021 ] , as Table 9 confirms. The spectral signatures transfer directly: ViT exhibits similar M ≈ 1 M_{\approx 1} patterns to language transformers. KSS improves ViT training, yielding 3% to 5% accuracy gains alongside divergence reduction. The spectral-stability correlation remains consistent across domains: higher M ≈ 1 M_{\approx 1} implies a higher risk score and aligns with increased divergence, while lower M ≈ 1 M_{\approx 1} indicates more damped, stable propagation.

[132] figure: Table 9: ViT RKSP analysis and KSS training. Results use 24 trials, with an image size of 224, a patch size of 16, and a 5-epoch sanity check. Measured on CIFAR-10. Model Norm Method Div. of 24 (lower) Acc.% (higher) M ≈ 1 M_{\approx 1} ViT-Tiny, d = 192 d=192 , L = 6 L=6 Pre-LN Baseline 1 of 24 72.3 72.3 0.42 0.42 ViT-Tiny, d = 192 d=192 , L = 6 L=6 Pre-LN KSS 0 of 24 75.8 \mathbf{75.8} 0.38 0.38 ViT-Tiny, d = 192 d=192 , L = 6 L=6 RMSNorm Baseline 2 of 24 70.1 70.1 0.48 0.48 ViT-Tiny, d = 192 d=192 , L = 6 L=6 RMSNorm KSS 0 of 24 74.2 \mathbf{74.2} 0.41 0.41

[133] figure: Table 10: LLaMA-2-7B analysis. The pattern persists at the 7B scale with RMSNorm. Computed from residual-stream activations on a fixed set of short prompt sentences. Measured on a fixed short-prompt set. Layer Group η nl \eta_{\mathrm{nl}} M ≈ 1 M_{\approx 1} κ ⁡ ( 𝐕 ) \kappa(\mathbf{V}) Pattern Early 0 to 10 0.45 ± 0.05 0.45\pm 0.05 0.74 0.74 8.2 8.2 Lower η nl \eta_{\mathrm{nl}} Middle 11 to 21 0.58 ± 0.08 0.58\pm 0.08 0.68 0.68 9.5 9.5 Mid η nl \eta_{\mathrm{nl}} Late 22 to 31 0.72 ± 0.10 0.72\pm 0.10 0.61 0.61 10.8 10.8 Higher η nl \eta_{\mathrm{nl}}

[134] figure: Figure 3: Scaling law for spectral properties. (Left) The near-unit mass M ≈ 1 M_{\approx 1} decreases with model scale, and larger models have more contractive dynamics, implying reduced memory and weaker near-isometric propagation. (Right) The normalized linear-fit error η nl \eta_{\mathrm{nl}} increases with scale, indicating a less reliable linear approximation at scale. Log-linear fits are shown. Computed from residual-stream activations on a fixed set of short prompt sentences.

[135] h3: 5.6 Large-Scale Pretrained Model Analysis

[136] p: We further validate RKSP on large-scale pretrained language models. Appendix G provides additional tables and plots.

[137] h5: Large Language Model Meta AI 2 (LLaMA-2) 7B Analysis.

[138] p: Table 10 extends our analysis to the 7B scale for LLaMA-2 [ Touvron et al., 2023 ] . The Start Linear, End Nonlinear pattern persists at this scale: η nl \eta_{\mathrm{nl}} increases monotonically with depth, ranging from 0.45 ± 0.05 0.45\pm 0.05 in the early layers to 0.72 ± 0.10 0.72\pm 0.10 in the late layers. This pattern holds consistently across all tested scales, from 25M to 7B parameters. Figure 3 quantifies this relationship through scaling law analysis.

[139] h5: Beyond Transformers.

[140] p: RKSP and KSS generalize beyond standard transformers to emerging architectures. We validate on Mixture of Experts (MoE) [ Shazeer et al., 2017 ] , Mamba-style state space model (SSM) architectures [ Gu and Dao, 2023 ] , and Kolmogorov-Arnold Networks (KAN) [ Liu et al., 2024 ] . Table 11 summarizes their characteristic spectral signatures: Mamba exhibits strongly contractive dynamics with low near-unit mass M ≈ 1 M_{\approx 1} , while MoE routing and KAN introduce higher nonlinearity and intermediate near-unit structure. Detailed case studies and additional comparisons appear in Appendix I .

[141] figure: Table 11: Cross-architecture spectral comparison. Transformer rows use the synthetic associative-recall task with seq len 64, vocab 256, and n pairs = 4 n_{\mathrm{pairs}}=4 ; MoE, Mamba, and KAN rows use the synthetic LM task with random-token next-token prediction. Architecture η nl \eta_{\mathrm{nl}} M ≈ 1 M_{\approx 1} ρ \rho Stability Character Transformer, Pre-LN 0.52 0.52 0.16 0.16 2.29 2.29 Balanced, tunable Transformer, No-Norm 0.48 0.48 0.79 0.79 1.11 1.11 High memory, risky MoE, top-2, 8 experts 0.55 0.55 0.58 0.58 2.12 2.12 Routing-dependent Mamba (SSM) 0.42 0.42 0.12 0.12 0.95 0.95 Contractive, short-memory KAN 0.78 0.78 0.52 0.52 2.15 2.15 Higher η nl \eta_{\mathrm{nl}}

[142] h2: 6 Conclusion

[143] p: We introduced RKSP, a method that uses whitened DMD to estimate layer-wise residual dynamics and predict transformer training divergence before optimization begins. At initialization, the risk score M ≈ 1 M_{\approx 1} achieves an AUROC of 0.995, enabling actionable early-termination decisions. Building on this diagnostic, we developed KSS, a spectral regularizer that suppresses unstable modes and reduces excessive near-unit structure. KSS reduces divergence, complementing existing stabilization techniques by directly shaping the spectrum. Across extensive experiments, our method successfully turns unstable settings into stable training.

[144] p: Our theoretical analysis explains these effects. Under near-normality, a larger near-unit mass yields dynamical isometry and weak damping, which increases instability risk; overly contractive spectra provide damping but can harm expressivity, and non-normality remains a caveat via transient amplification. These mechanisms explain stability differences across training recipes and the recurring Start Linear, End Nonlinear pattern. The spectral signals remain consistent across diverse models, tasks, and normalization strategies.

[145] h2: References

[146] p: Residual Koopman Spectral Profiling for Predicting and Preventing Transformer Training Instability (Supplementary Material)

[147] h2: Appendix Table of Contents

[148] h2: Appendix A List of Notation

[149] figure: Table 12: List of notations used in the main paper and supplementary material. Symbol Meaning Core sizes and indices L L The number of layers. ℓ \ell Layer index. d d Hidden dimension. N N The number of snapshots. r r Randomized DMD rank, the number of eigenvalues used in KSS. Dynamics and operators 𝐡 ℓ \mathbf{h}_{\ell} Residual stream at layer ℓ \ell . F ℓ ​ ( ⋅ ) F_{\ell}(\cdot) Residual mapping F ℓ ​ ( 𝐡 ℓ ) = 𝐡 ℓ + f ℓ ​ ( 𝐡 ℓ , θ ℓ ) F_{\ell}(\mathbf{h}_{\ell})=\mathbf{h}_{\ell}+f_{\ell}(\mathbf{h}_{\ell};\theta_{\ell}) . 𝒦 \mathcal{K} Koopman operator. 𝐀 ^ ℓ \hat{\mathbf{A}}_{\ell} DMD estimate of the layer- ℓ \ell Koopman operator. 𝐕 , 𝚲 \mathbf{V},\boldsymbol{\Lambda} Eigenvectors and eigenvalues of 𝐀 ^ ℓ \hat{\mathbf{A}}_{\ell} . λ j \lambda_{j} Eigenvalue. ρ ⁡ ( 𝐀 ) \rho(\mathbf{A}) Spectral radius. κ ⁡ ( 𝐕 ) \kappa(\mathbf{V}) Eigenvector condition number, a measure of non-normality. 𝒦 ⁡ ( 𝐀 ) \mathcal{K}(\mathbf{A}) Kreiss constant. Snapshots and whitening 𝐗 ℓ , 𝐘 ℓ \mathbf{X}_{\ell},\mathbf{Y}_{\ell} Layer- ℓ \ell snapshot matrices. 𝐗 ~ ℓ , 𝐘 ~ ℓ \tilde{\mathbf{X}}_{\ell},\tilde{\mathbf{Y}}_{\ell} Whitened snapshots. 𝚺 ^ X \hat{\boldsymbol{\Sigma}}_{X} Regularized sample covariance used for whitening. ( ⋅ ) † (\cdot)^{\dagger} Moore–Penrose pseudoinverse. Spectral diagnostics M > 1 M_{>1} Unstable spectral mass. M ≈ 1 M_{\approx 1} Near-unit spectral mass. M < 1 M_{<1} Contractive spectral mass. η nl \eta_{\mathrm{nl}} Nonlinearity ratio, a fit-error measure. ϵ u , ϵ n , δ c \epsilon_{u},\epsilon_{n},\delta_{c} Thresholds defining spectral-mass bins. KSS regularization ℒ KSS ℓ \mathcal{L}_{\mathrm{KSS}}^{\ell} KSS loss for layer ℓ \ell . α \alpha KSS regularization weight. τ u , τ l \tau_{u},\tau_{l} Upper and lower band thresholds in KSS. γ \gamma Target near-unit mass level. m ℓ soft m_{\ell}^{\mathrm{soft}} Soft near-unit mass estimate. Probability and norms D D Divergence indicator. P ⁡ ( D = 1 ∣ 𝒮 ) P(D=1\mid\mathcal{S}) Predicted divergence probability. 𝔼 ⁡ [ ⋅ ] \mathbb{E}[\cdot] Expectation. Tr ⁡ ( ⋅ ) \mathrm{Tr}(\cdot) Trace. ‖ ⋅ ‖ 2 , ‖ ⋅ ‖ F \left\|\cdot\right\|_{2},\left\|\cdot\right\|_{F} Operator and Frobenius norms. | ⋅ | \left|\cdot\right| Absolute value. ℝ , ℂ \mathbb{R},\mathbb{C} Real and complex number fields.

[150] h2: Appendix B Additional Theoretical Results

[151] p: The following results extend the theoretical analysis presented in Section 4 .

[152] h3: B.1 Supplement to Theorem 1

[153] h6: Proposition 3 (Bauer–Fike: Non-normality Caveat) .

[154] p: Let 𝐀 ∈ ℂ d × d \mathbf{A}\in\mathbb{C}^{d\times d} be diagonalizable with eigendecomposition 𝐀 = 𝐕 ​ 𝚲 ​ 𝐕 − 1 \mathbf{A}=\mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1} . For any perturbation 𝐄 \mathbf{E} with ‖ 𝐄 ‖ 2 ≤ δ \left\|\mathbf{E}\right\|_{2}\leq\delta and any eigenvalue λ ~ ∈ spec ⁡ ( 𝐀 + 𝐄 ) \tilde{\lambda}\in\spec(\mathbf{A}+\mathbf{E}) , we have

[155] table: min k ⁡ | λ ~ − λ k | ≤ κ ⁡ ( 𝐕 ) ⋅ δ . \min_{k}|\tilde{\lambda}-\lambda_{k}|\leq\kappa(\mathbf{V})\cdot\delta. (20)

[156] h6: Proof.

[157] p: Let λ ~ ∈ spec ⁡ ( 𝐀 + 𝐄 ) \tilde{\lambda}\in\spec(\mathbf{A}+\mathbf{E}) with eigenvector 𝐱 ≠ 𝟎 \mathbf{x}\neq\mathbf{0} , that is, ( 𝐀 + 𝐄 ) ​ 𝐱 = λ ~ ​ 𝐱 (\mathbf{A}+\mathbf{E})\mathbf{x}=\tilde{\lambda}\mathbf{x} . Write 𝐀 = 𝐕 ​ 𝚲 ​ 𝐕 − 1 \mathbf{A}=\mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1} and set 𝐲 ≜ 𝐕 − 1 ​ 𝐱 ≠ 𝟎 \mathbf{y}\triangleq\mathbf{V}^{-1}\mathbf{x}\neq\mathbf{0} . Left-multiplying by 𝐕 − 1 \mathbf{V}^{-1} gives

[158] table: ( 𝚲 − λ ~ ​ 𝐈 ) ​ 𝐲 = − 𝐕 − 1 ​ 𝐄𝐕𝐲 . (\boldsymbol{\Lambda}-\tilde{\lambda}\mathbf{I})\mathbf{y}=-\mathbf{V}^{-1}\mathbf{E}\mathbf{V}\mathbf{y}.

[159] p: Taking Euclidean norms,

[160] table: ‖ ( 𝚲 − λ ~ ​ 𝐈 ) ​ 𝐲 ‖ 2 ≤ ‖ 𝐕 − 1 ‖ 2 ​ ‖ 𝐄 ‖ 2 ​ ‖ 𝐕 ‖ 2 ​ ‖ 𝐲 ‖ 2 = κ ⁡ ( 𝐕 ) ​ δ ​ ‖ 𝐲 ‖ 2 . \left\|(\boldsymbol{\Lambda}-\tilde{\lambda}\mathbf{I})\mathbf{y}\right\|_{2}\leq\left\|\mathbf{V}^{-1}\right\|_{2}\left\|\mathbf{E}\right\|_{2}\left\|\mathbf{V}\right\|_{2}\left\|\mathbf{y}\right\|_{2}=\kappa(\mathbf{V})\delta\left\|\mathbf{y}\right\|_{2}.

[161] p: Because 𝚲 − λ ~ ​ 𝐈 \boldsymbol{\Lambda}-\tilde{\lambda}\mathbf{I} is diagonal with diagonal entries ( λ j − λ ~ ) (\lambda_{j}-\tilde{\lambda}) ,

[162] table: ‖ ( 𝚲 − λ ~ ​ 𝐈 ) ​ 𝐲 ‖ 2 ≥ min k ⁡ | λ k − λ ~ | ⋅ ‖ 𝐲 ‖ 2 . \left\|(\boldsymbol{\Lambda}-\tilde{\lambda}\mathbf{I})\mathbf{y}\right\|_{2}\geq\min_{k}|\lambda_{k}-\tilde{\lambda}|\cdot\left\|\mathbf{y}\right\|_{2}.

[163] p: Canceling ‖ 𝐲 ‖ 2 \left\|\mathbf{y}\right\|_{2} yields Eq. 20 . ∎

[164] h3: B.2 DMD Convergence Analysis

[165] p: We first establish finite-sample convergence guarantees for DMD estimation in the presence of nonlinearity.

[166] h6: Assumption 1 (Data Distribution) .

[167] p: Let ( 𝐱 , 𝐲 ) ∈ ℝ d × ℝ d (\mathbf{x},\mathbf{y})\in\mathbb{R}^{d}\times\mathbb{R}^{d} be a random pair drawn from the joint distribution induced by a layer transition. We assume centered covariates: 𝔼 ⁡ [ 𝐱 ] = 𝟎 \mathbb{E}[\mathbf{x}]=\mathbf{0} and 𝔼 ⁡ [ 𝐱𝐱 ⊤ ] = 𝚺 \mathbb{E}[\mathbf{x}\mathbf{x}^{\top}]=\boldsymbol{\Sigma} with σ min ​ ( 𝚺 ) ≥ σ 0 > 0 \sigma_{\min}(\boldsymbol{\Sigma})\geq\sigma_{0}>0 . We also assume sub-Gaussian tails: ‖ 𝐱 ‖ ψ 2 ≤ K \left\|\mathbf{x}\right\|_{\psi_{2}}\leq K and ‖ 𝐲 ‖ ψ 2 ≤ K \left\|\mathbf{y}\right\|_{\psi_{2}}\leq K for some K > 0 K>0 . Define the cross-covariance 𝐂 y ​ x ≜ 𝔼 ⁡ [ 𝐲𝐱 ⊤ ] \mathbf{C}_{yx}\triangleq\mathbb{E}[\mathbf{y}\mathbf{x}^{\top}] . Let ϵ ≥ 0 \epsilon\geq 0 be the whitening regularizer in Eq. 7 , and set 𝚺 ϵ ≜ 𝚺 + ϵ ​ 𝐈 \boldsymbol{\Sigma}_{\epsilon}\triangleq\boldsymbol{\Sigma}+\epsilon\mathbf{I} . Then σ min ​ ( 𝚺 ϵ ) ≥ σ 0 \sigma_{\min}(\boldsymbol{\Sigma}_{\epsilon})\geq\sigma_{0} . Define

[168] table: 𝐌 ϵ \displaystyle\mathbf{M}_{\epsilon} ≜ 𝚺 ϵ − 1 / 2 𝐂 y ​ x 𝚺 ϵ − 1 / 2 , \displaystyle\triangleq\boldsymbol{\Sigma}_{\epsilon}^{-1/2}\mathbf{C}_{yx}\boldsymbol{\Sigma}_{\epsilon}^{-1/2}, (21) 𝐆 ϵ \displaystyle\mathbf{G}_{\epsilon} ≜ 𝚺 ϵ − 1 / 2 𝚺 𝚺 ϵ − 1 / 2 , \displaystyle\triangleq\boldsymbol{\Sigma}_{\epsilon}^{-1/2}\boldsymbol{\Sigma}\boldsymbol{\Sigma}_{\epsilon}^{-1/2}, (22)

[169] p: and the regularized whitened population least-squares operator

[170] table: 𝐀 w , ϵ LS ≜ 𝐌 ϵ ​ 𝐆 ϵ − 1 . \mathbf{A}_{\mathrm{w},\epsilon}^{\mathrm{LS}}\triangleq\mathbf{M}_{\epsilon}\mathbf{G}_{\epsilon}^{-1}. (23)

[171] p: The nonlinearity ratio η nl \eta_{\mathrm{nl}} is a normalized linear-fit error that we use as a practical diagnostic for linear-approximation reliability.

[172] h6: Theorem 4 (Whitened DMD Finite-Sample Convergence) .

[173] p: Under Assumption 1 , let σ ϵ ≜ σ min ​ ( 𝚺 ϵ ) \sigma_{\epsilon}\triangleq\sigma_{\min}(\boldsymbol{\Sigma}_{\epsilon}) . Then σ ϵ ≥ σ 0 \sigma_{\epsilon}\geq\sigma_{0} . Let δ fail ∈ ( 0 , 1 ) \delta_{\mathrm{fail}}\in(0,1) . Consider the events

[174] table: ‖ 𝚺 ^ X − 𝚺 ϵ ‖ 2 ≤ 1 2 ​ σ ϵ , \left\|\hat{\boldsymbol{\Sigma}}_{X}-\boldsymbol{\Sigma}_{\epsilon}\right\|_{2}\leq\frac{1}{2}\sigma_{\epsilon}, (24)

[175] p: and

[176] table: ‖ 𝐆 ^ − 𝐆 ϵ ‖ 2 ≤ 1 2 ​ σ min ​ ( 𝐆 ϵ ) , \left\|\hat{\mathbf{G}}-\mathbf{G}_{\epsilon}\right\|_{2}\leq\frac{1}{2}\sigma_{\min}(\mathbf{G}_{\epsilon}), (25)

[177] p: where 𝐆 ^ ≜ 𝚺 ^ X − 1 / 2 𝚺 ^ 𝚺 ^ X − 1 / 2 \hat{\mathbf{G}}\triangleq\hat{\boldsymbol{\Sigma}}_{X}^{-1/2}\hat{\boldsymbol{\Sigma}}\hat{\boldsymbol{\Sigma}}_{X}^{-1/2} . Then 𝐆 ^ \hat{\mathbf{G}} is invertible, and ‖ 𝐆 ^ − 1 ‖ 2 ≤ 2 ​ ‖ 𝐆 ϵ − 1 ‖ 2 \left\|\hat{\mathbf{G}}^{-1}\right\|_{2}\leq 2\left\|\mathbf{G}_{\epsilon}^{-1}\right\|_{2} . Assuming 𝐗 ~ ​ 𝐗 ~ ⊤ \tilde{\mathbf{X}}\tilde{\mathbf{X}}^{\top} is invertible, for example, when N ≥ d N\geq d and rank ⁡ ( 𝐗 ~ ) = d \mathrm{rank}(\tilde{\mathbf{X}})=d , there exist absolute constants C , c > 0 C,c>0 such that if N ≥ c ⁡ ( d + log ⁡ ( 2 / δ fail ) ) N\geq c(d+\log(2/\delta_{\mathrm{fail}})) , then on the event Eq. 24 and Eq. 25 :

[178] table: ‖ 𝐀 ^ − 𝐀 w , ϵ LS ‖ 2 ≤ C ​ ‖ 𝐆 ϵ − 1 ‖ 2 ​ K 2 σ ϵ ​ Δ N + C ​ ‖ 𝐆 ϵ − 1 ‖ 2 2 ​ K 2 ​ ‖ 𝐂 y ​ x ‖ 2 σ ϵ 2 ​ Δ N , \left\|\hat{\mathbf{A}}-\mathbf{A}_{\mathrm{w},\epsilon}^{\mathrm{LS}}\right\|_{2}\leq C\left\|\mathbf{G}_{\epsilon}^{-1}\right\|_{2}\frac{K^{2}}{\sigma_{\epsilon}}\Delta_{N}+C\left\|\mathbf{G}_{\epsilon}^{-1}\right\|_{2}^{2}\frac{K^{2}\left\|\mathbf{C}_{yx}\right\|_{2}}{\sigma_{\epsilon}^{2}}\Delta_{N}, (26)

[179] p: where Δ N ≜ d + log ⁡ ( 2 / δ fail ) N + d + log ⁡ ( 2 / δ fail ) N \Delta_{N}\triangleq\sqrt{\frac{d+\log(2/\delta_{\mathrm{fail}})}{N}}+\frac{d+\log(2/\delta_{\mathrm{fail}})}{N} .

[180] h6: Proof.

[181] p: We bound the estimation error relative to the whitened population least-squares operator 𝐀 w , ϵ LS \mathbf{A}_{\mathrm{w},\epsilon}^{\mathrm{LS}} . Assume 𝐗 ~ ​ 𝐗 ~ ⊤ \tilde{\mathbf{X}}\tilde{\mathbf{X}}^{\top} is invertible, so that 𝐗 ~ † = 𝐗 ~ ⊤ ​ ( 𝐗 ~ ​ 𝐗 ~ ⊤ ) − 1 \tilde{\mathbf{X}}^{\dagger}=\tilde{\mathbf{X}}^{\top}(\tilde{\mathbf{X}}\tilde{\mathbf{X}}^{\top})^{-1} and 𝐀 ^ = 𝐌 ^ ​ 𝐆 ^ − 1 \hat{\mathbf{A}}=\hat{\mathbf{M}}\hat{\mathbf{G}}^{-1} with 𝐌 ^ ≜ 𝚺 ^ X − 1 / 2 𝐂 ^ y ​ x 𝚺 ^ X − 1 / 2 \hat{\mathbf{M}}\triangleq\hat{\boldsymbol{\Sigma}}_{X}^{-1/2}\hat{\mathbf{C}}_{yx}\hat{\boldsymbol{\Sigma}}_{X}^{-1/2} and 𝐆 ^ ≜ 𝚺 ^ X − 1 / 2 𝚺 ^ 𝚺 ^ X − 1 / 2 \hat{\mathbf{G}}\triangleq\hat{\boldsymbol{\Sigma}}_{X}^{-1/2}\hat{\boldsymbol{\Sigma}}\hat{\boldsymbol{\Sigma}}_{X}^{-1/2} , where 𝐱 ¯ = 1 N ​ ∑ i = 1 N 𝐱 i \bar{\mathbf{x}}=\frac{1}{N}\sum_{i=1}^{N}\mathbf{x}_{i} , 𝐲 ¯ = 1 N ​ ∑ i = 1 N 𝐲 i \bar{\mathbf{y}}=\frac{1}{N}\sum_{i=1}^{N}\mathbf{y}_{i} , 𝚺 ^ = 1 N − 1 ​ ∑ i = 1 N ( 𝐱 i − 𝐱 ¯ ) ​ ( 𝐱 i − 𝐱 ¯ ) ⊤ \hat{\boldsymbol{\Sigma}}=\frac{1}{N-1}\sum_{i=1}^{N}(\mathbf{x}_{i}-\bar{\mathbf{x}})(\mathbf{x}_{i}-\bar{\mathbf{x}})^{\top} , 𝐂 ^ y ​ x = 1 N − 1 ​ ∑ i = 1 N ( 𝐲 i − 𝐲 ¯ ) ​ ( 𝐱 i − 𝐱 ¯ ) ⊤ \hat{\mathbf{C}}_{yx}=\frac{1}{N-1}\sum_{i=1}^{N}(\mathbf{y}_{i}-\bar{\mathbf{y}})(\mathbf{x}_{i}-\bar{\mathbf{x}})^{\top} , and 𝚺 ^ X = 𝚺 ^ + ϵ ​ 𝐈 \hat{\boldsymbol{\Sigma}}_{X}=\hat{\boldsymbol{\Sigma}}+\epsilon\mathbf{I} .

[182] p: First, we estimate the covariance. For N N independently and identically distributed samples with ‖ 𝐱 ‖ ψ 2 ≤ K \left\|\mathbf{x}\right\|_{\psi_{2}}\leq K , standard covariance concentration for the centered sample covariance yields [ Tropp, 2012 ]

[183] table: ‖ 𝚺 ^ X − 𝚺 ϵ ‖ 2 ≤ C ​ K 2 ​ Δ N , \left\|\hat{\boldsymbol{\Sigma}}_{X}-\boldsymbol{\Sigma}_{\epsilon}\right\|_{2}\leq CK^{2}\Delta_{N}, (27)

[184] p: with probability ≥ 1 − δ fail / 2 \geq 1-\delta_{\mathrm{fail}}/2 for N ≳ d + log ⁡ ( 1 / δ fail ) N\gtrsim d+\log(1/\delta_{\mathrm{fail}}) .

[185] p: Second, we bound the whitening perturbation. Standard perturbation theory for matrix square roots gives [ Higham, 2008 ] :

[186] table: ‖ 𝚺 ^ X − 1 / 2 − 𝚺 ϵ − 1 / 2 ‖ 2 ≤ 2 σ ϵ 3 / 2 ‖ 𝚺 ^ X − 𝚺 ϵ ‖ 2 , \left\|\hat{\boldsymbol{\Sigma}}_{X}^{-1/2}-\boldsymbol{\Sigma}_{\epsilon}^{-1/2}\right\|_{2}\leq\frac{2}{\sigma_{\epsilon}^{3/2}}\left\|\hat{\boldsymbol{\Sigma}}_{X}-\boldsymbol{\Sigma}_{\epsilon}\right\|_{2}, (28)

[187] p: for ‖ 𝚺 ^ X − 𝚺 ϵ ‖ 2 ≤ 1 2 ​ σ ϵ \left\|\hat{\boldsymbol{\Sigma}}_{X}-\boldsymbol{\Sigma}_{\epsilon}\right\|_{2}\leq\frac{1}{2}\sigma_{\epsilon} .

[188] p: Now, we combine the cross-covariance and covariance estimation errors. Let 𝐂 ^ y ​ x = 1 N − 1 ​ ∑ i = 1 N ( 𝐲 i − 𝐲 ¯ ) ​ ( 𝐱 i − 𝐱 ¯ ) ⊤ \hat{\mathbf{C}}_{yx}=\frac{1}{N-1}\sum_{i=1}^{N}(\mathbf{y}_{i}-\bar{\mathbf{y}})(\mathbf{x}_{i}-\bar{\mathbf{x}})^{\top} . A similar sub-exponential matrix concentration bound gives [ Tropp, 2012 ] ‖ 𝐂 ^ y ​ x − 𝐂 y ​ x ‖ 2 ≤ C ​ K 2 ​ Δ N \left\|\hat{\mathbf{C}}_{yx}-\mathbf{C}_{yx}\right\|_{2}\leq CK^{2}\Delta_{N} with probability ≥ 1 − δ fail / 2 \geq 1-\delta_{\mathrm{fail}}/2 . Decomposing

[189] table: 𝐀 ^ − 𝐀 w , ϵ LS = 𝐌 ^ ​ 𝐆 ^ − 1 − 𝐌 ϵ ​ 𝐆 ϵ − 1 = ( 𝐌 ^ − 𝐌 ϵ ) ​ 𝐆 ϵ − 1 + 𝐌 ^ ​ ( 𝐆 ^ − 1 − 𝐆 ϵ − 1 ) , \hat{\mathbf{A}}-\mathbf{A}_{\mathrm{w},\epsilon}^{\mathrm{LS}}=\hat{\mathbf{M}}\hat{\mathbf{G}}^{-1}-\mathbf{M}_{\epsilon}\mathbf{G}_{\epsilon}^{-1}=(\hat{\mathbf{M}}-\mathbf{M}_{\epsilon})\mathbf{G}_{\epsilon}^{-1}+\hat{\mathbf{M}}\left(\hat{\mathbf{G}}^{-1}-\mathbf{G}_{\epsilon}^{-1}\right),

[190] p: and using a standard matrix inverse perturbation bound,

[191] table: ‖ 𝐆 ^ − 1 − 𝐆 ϵ − 1 ‖ 2 ≤ ‖ 𝐆 ^ − 1 ‖ 2 ​ ‖ 𝐆 ^ − 𝐆 ϵ ‖ 2 ​ ‖ 𝐆 ϵ − 1 ‖ 2 ≤ 2 ​ ‖ 𝐆 ϵ − 1 ‖ 2 2 ​ ‖ 𝐆 ^ − 𝐆 ϵ ‖ 2 \left\|\hat{\mathbf{G}}^{-1}-\mathbf{G}_{\epsilon}^{-1}\right\|_{2}\leq\left\|\hat{\mathbf{G}}^{-1}\right\|_{2}\left\|\hat{\mathbf{G}}-\mathbf{G}_{\epsilon}\right\|_{2}\left\|\mathbf{G}_{\epsilon}^{-1}\right\|_{2}\leq 2\left\|\mathbf{G}_{\epsilon}^{-1}\right\|_{2}^{2}\left\|\hat{\mathbf{G}}-\mathbf{G}_{\epsilon}\right\|_{2}

[192] p: on Eq. 25 yields a cross-covariance term scaling as ‖ 𝐆 ϵ − 1 ‖ 2 ​ σ ϵ − 1 \left\|\mathbf{G}_{\epsilon}^{-1}\right\|_{2}\sigma_{\epsilon}^{-1} and a whitening term plus a covariance term scaling as ‖ 𝐆 ϵ − 1 ‖ 2 2 ​ ‖ 𝐂 y ​ x ‖ 2 ​ σ ϵ − 2 \left\|\mathbf{G}_{\epsilon}^{-1}\right\|_{2}^{2}\left\|\mathbf{C}_{yx}\right\|_{2}\sigma_{\epsilon}^{-2} , giving Eq. 26 .

[193] p: Combining the bounds yields Eq. 26 under the event Eq. 24 and Eq. 25 . ∎

[194] h6: Remark 1 (On 𝐆 ϵ − 1 \mathbf{G}_{\epsilon}^{-1} for 𝚺 ϵ = 𝚺 + ϵ ​ 𝐈 \boldsymbol{\Sigma}_{\epsilon}=\boldsymbol{\Sigma}+\epsilon\mathbf{I} ) .

[195] p: Because 𝚺 \boldsymbol{\Sigma} and 𝚺 ϵ \boldsymbol{\Sigma}_{\epsilon} commute, 𝐆 ϵ \mathbf{G}_{\epsilon} has eigenvalues λ i / ( λ i + ϵ ) \lambda_{i}/(\lambda_{i}+\epsilon) , hence

[196] table: ‖ 𝐆 ϵ − 1 ‖ 2 = σ min ​ ( 𝚺 ) + ϵ σ min ​ ( 𝚺 ) . \left\|\mathbf{G}_{\epsilon}^{-1}\right\|_{2}=\frac{\sigma_{\min}(\boldsymbol{\Sigma})+\epsilon}{\sigma_{\min}(\boldsymbol{\Sigma})}.

[197] p: If σ min ​ ( 𝚺 ) \sigma_{\min}(\boldsymbol{\Sigma}) is treated as a fixed constant bounded away from 0 0 , the factors of ‖ 𝐆 ϵ − 1 ‖ 2 \left\|\mathbf{G}_{\epsilon}^{-1}\right\|_{2} can be absorbed into the constant C C .

[198] h6: Remark 2 (Sample Complexity) .

[199] p: Theorem 4 suggests that, under the stability events Eq. 24 –Eq. 25 , N = O ~ ​ ( d ​ ( ‖ 𝐆 ϵ − 1 ‖ 2 ​ K 2 σ ϵ + ‖ 𝐆 ϵ − 1 ‖ 2 2 ​ K 2 ​ ‖ 𝐂 y ​ x ‖ 2 σ ϵ 2 ) 2 ​ ε − 2 ) N=\tilde{O}\left(d\left(\left\|\mathbf{G}_{\epsilon}^{-1}\right\|_{2}\frac{K^{2}}{\sigma_{\epsilon}}+\left\|\mathbf{G}_{\epsilon}^{-1}\right\|_{2}^{2}\frac{K^{2}\left\|\mathbf{C}_{yx}\right\|_{2}}{\sigma_{\epsilon}^{2}}\right)^{2}\varepsilon^{-2}\right) samples are sufficient for ε \varepsilon -accurate DMD estimation, up to logarithmic factors. For typical transformers with d = 256 d=256 to 768 768 , N ≈ 2048 N\approx 2048 provides reliable estimates.

[200] h6: Remark 3 (Modeling Mismatch and η nl \eta_{\mathrm{nl}} ) .

[201] p: Theorem 4 is an estimation bound for the whitened population least-squares operator 𝐀 w , ϵ LS \mathbf{A}_{\mathrm{w},\epsilon}^{\mathrm{LS}} . When the layer transition is nonlinear, 𝐀 w , ϵ LS \mathbf{A}_{\mathrm{w},\epsilon}^{\mathrm{LS}} can be a poor proxy for other targets, such as a local Jacobian or a richer Koopman approximation, even if it is well-estimated. We use the empirical nonlinearity ratio η nl \eta_{\mathrm{nl}} defined in Eq. 5 as a practical diagnostic for when linear DMD features are less reliable.

[202] h3: B.3 Non-Normality and Transient Growth

[203] p: Spectral radius bounds alone are insufficient for analyzing non-normal matrices. The Kreiss matrix theorem provides tight bounds on transient behavior [ Kreiss, 1962 , Trefethen and Embree, 2020 ] .

[204] h6: Theorem 5 (Kreiss Constant Characterization) .

[205] p: The Kreiss constant of 𝐀 ∈ ℂ d × d \mathbf{A}\in\mathbb{C}^{d\times d} is:

[206] table: 𝒦 ⁡ ( 𝐀 ) ≜ sup | z | > 1 ( | z | − 1 ) ​ ‖ ( z ​ 𝐈 − 𝐀 ) − 1 ‖ 2 \mathcal{K}(\mathbf{A})\triangleq\sup_{|z|>1}(|z|-1)\left\|(z\mathbf{I}-\mathbf{A})^{-1}\right\|_{2} (29)

[207] p: Assume 𝐀 \mathbf{A} is power-bounded, that is, sup n ≥ 0 ‖ 𝐀 n ‖ 2 < ∞ \sup_{n\geq 0}\left\|\mathbf{A}^{n}\right\|_{2}<\infty ; equivalently, 𝒦 ⁡ ( 𝐀 ) < ∞ \mathcal{K}(\mathbf{A})<\infty . Then the Kreiss matrix theorem states:

[208] table: 𝒦 ⁡ ( 𝐀 ) ≤ sup n ≥ 0 ‖ 𝐀 n ‖ 2 ≤ e ⋅ d ⋅ 𝒦 ⁡ ( 𝐀 ) \mathcal{K}(\mathbf{A})\leq\sup_{n\geq 0}\left\|\mathbf{A}^{n}\right\|_{2}\leq e\cdot d\cdot\mathcal{K}(\mathbf{A}) (30)

[209] p: For a diagonalizable 𝐀 = 𝐕 ​ 𝚲 ​ 𝐕 − 1 \mathbf{A}=\mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1} :

[210] table: 𝒦 ⁡ ( 𝐀 ) ≤ κ ⁡ ( 𝐕 ) ⋅ sup | z | > 1 max j ⁡ | z | − 1 | z − λ j | \mathcal{K}(\mathbf{A})\leq\kappa(\mathbf{V})\cdot\sup_{|z|>1}\max_{j}\frac{|z|-1}{|z-\lambda_{j}|} (31)

[211] h6: Proof.

[212] p: We first prove the two inequalities in Eq. 30 and then Eq. 31 .

[213] h5: Lower bound: 𝒦 ⁡ ( 𝐀 ) ≤ sup n ≥ 0 ‖ 𝐀 n ‖ 2 \mathcal{K}(\mathbf{A})\leq\sup_{n\geq 0}\left\|\mathbf{A}^{n}\right\|_{2} .

[214] p: Let M ≜ sup n ≥ 0 ‖ 𝐀 n ‖ 2 < ∞ M\triangleq\sup_{n\geq 0}\left\|\mathbf{A}^{n}\right\|_{2}<\infty . Because 𝐀 \mathbf{A} is power-bounded, sup n ≥ 0 ‖ 𝐀 n ‖ 2 < ∞ \sup_{n\geq 0}\left\|\mathbf{A}^{n}\right\|_{2}<\infty , so the Neumann series converges in operator norm for any | z | > 1 |z|>1 . For any | z | > 1 |z|>1 , the Neumann series gives the operator-norm expansion

[215] table: ( z ​ 𝐈 − 𝐀 ) − 1 = z − 1 ​ ∑ n = 0 ∞ 𝐀 n ​ z − n , (z\mathbf{I}-\mathbf{A})^{-1}=z^{-1}\sum_{n=0}^{\infty}\mathbf{A}^{n}z^{-n},

[216] p: hence

[217] table: ‖ ( z ​ 𝐈 − 𝐀 ) − 1 ‖ 2 ≤ 1 | z | ​ ∑ n = 0 ∞ ‖ 𝐀 n ‖ 2 | z | n ≤ M | z | ​ ∑ n = 0 ∞ | z | − n = M | z | − 1 . \left\|(z\mathbf{I}-\mathbf{A})^{-1}\right\|_{2}\leq\frac{1}{|z|}\sum_{n=0}^{\infty}\frac{\left\|\mathbf{A}^{n}\right\|_{2}}{|z|^{n}}\leq\frac{M}{|z|}\sum_{n=0}^{\infty}|z|^{-n}=\frac{M}{|z|-1}.

[218] p: Multiplying by ( | z | − 1 ) (|z|-1) and taking the supremum over | z | > 1 |z|>1 yields 𝒦 ⁡ ( 𝐀 ) ≤ M \mathcal{K}(\mathbf{A})\leq M .

[219] h5: Upper bound: sup n ≥ 0 ‖ 𝐀 n ‖ 2 ≤ e ​ d ​ 𝒦 ​ ( 𝐀 ) \sup_{n\geq 0}\left\|\mathbf{A}^{n}\right\|_{2}\leq ed\mathcal{K}(\mathbf{A}) .

[220] p: This is the finite-dimensional Kreiss matrix theorem: the resolvent bound sup | z | > 1 ( | z | − 1 ) ​ ‖ ( z ​ 𝐈 − 𝐀 ) − 1 ‖ 2 < ∞ \sup_{|z|>1}(|z|-1)\left\|(z\mathbf{I}-\mathbf{A})^{-1}\right\|_{2}<\infty is equivalent to power-boundedness, and quantitatively implies sup n ≥ 0 ‖ 𝐀 n ‖ 2 ≤ C d ​ 𝒦 ​ ( 𝐀 ) \sup_{n\geq 0}\left\|\mathbf{A}^{n}\right\|_{2}\leq C_{d}\mathcal{K}(\mathbf{A}) for an explicit dimension-dependent constant C d C_{d} ; one standard choice is C d = e ​ d C_{d}=ed .

[221] h5: Diagonalizable case.

[222] p: If 𝐀 = 𝐕 ​ 𝚲 ​ 𝐕 − 1 \mathbf{A}=\mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1} , then for any z ∉ spec ⁡ ( 𝐀 ) z\notin\spec(\mathbf{A}) ,

[223] table: ( z ​ 𝐈 − 𝐀 ) − 1 = 𝐕 ​ ( z ​ 𝐈 − 𝚲 ) − 1 ​ 𝐕 − 1 . (z\mathbf{I}-\mathbf{A})^{-1}=\mathbf{V}(z\mathbf{I}-\boldsymbol{\Lambda})^{-1}\mathbf{V}^{-1}.

[224] p: Taking norms gives

[225] table: ‖ ( z ​ 𝐈 − 𝐀 ) − 1 ‖ 2 ≤ ‖ 𝐕 ‖ 2 ​ ‖ ( z ​ 𝐈 − 𝚲 ) − 1 ‖ 2 ​ ‖ 𝐕 − 1 ‖ 2 = κ ⁡ ( 𝐕 ) ​ ‖ ( z ​ 𝐈 − 𝚲 ) − 1 ‖ 2 . \left\|(z\mathbf{I}-\mathbf{A})^{-1}\right\|_{2}\leq\left\|\mathbf{V}\right\|_{2}\left\|(z\mathbf{I}-\boldsymbol{\Lambda})^{-1}\right\|_{2}\left\|\mathbf{V}^{-1}\right\|_{2}=\kappa(\mathbf{V})\left\|(z\mathbf{I}-\boldsymbol{\Lambda})^{-1}\right\|_{2}.

[226] p: Because ( z ​ 𝐈 − 𝚲 ) − 1 (z\mathbf{I}-\boldsymbol{\Lambda})^{-1} is diagonal with diagonal entries ( z − λ j ) − 1 (z-\lambda_{j})^{-1} , its spectral norm is max j ⁡ | z − λ j | − 1 \max_{j}|z-\lambda_{j}|^{-1} , hence

[227] table: ( | z | − 1 ) ​ ‖ ( z ​ 𝐈 − 𝐀 ) − 1 ‖ 2 ≤ κ ⁡ ( 𝐕 ) ⋅ max j ⁡ | z | − 1 | z − λ j | . (|z|-1)\left\|(z\mathbf{I}-\mathbf{A})^{-1}\right\|_{2}\leq\kappa(\mathbf{V})\cdot\max_{j}\frac{|z|-1}{|z-\lambda_{j}|}.

[228] p: Taking the supremum over | z | > 1 |z|>1 yields Eq. 31 . ∎

[229] p: The interpretation is as follows: a high 𝒦 ⁡ ( 𝐀 ) \mathcal{K}(\mathbf{A}) indicates hidden instability. Even when ρ ⁡ ( 𝐀 ) ≤ 1 \rho(\mathbf{A})\leq 1 , non-orthogonal eigenvectors produce a transient growth ‖ 𝐀 n ‖ 2 ≫ 1 \left\|\mathbf{A}^{n}\right\|_{2}\gg 1 for intermediate n n .

[230] h2: Appendix C PROOF OF THEOREM 1

[231] h6: Proof.

[232] p: For 𝐱 \mathbf{x} uniform on the unit sphere, rotational invariance implies 𝔼 ⁡ [ 𝐱𝐱 ∗ ] = 1 d ​ 𝐈 \mathbb{E}[\mathbf{x}\mathbf{x}^{*}]=\frac{1}{d}\mathbf{I} . Therefore

[233] table: 𝔼 ​ ‖ 𝐀𝐱 ‖ 2 2 = 𝔼 ⁡ [ 𝐱 ∗ ​ 𝐀 ∗ ​ 𝐀𝐱 ] = Tr ⁡ ( 𝐀 ∗ ​ 𝐀 ​ 𝔼 ​ [ 𝐱𝐱 ∗ ] ) = 1 d ​ Tr ​ ( 𝐀 ∗ ​ 𝐀 ) = 1 d ​ ‖ 𝐀 ‖ F 2 . \mathbb{E}\left\|\mathbf{A}\mathbf{x}\right\|_{2}^{2}=\mathbb{E}[\mathbf{x}^{*}\mathbf{A}^{*}\mathbf{A}\mathbf{x}]=\mathrm{Tr}\left(\mathbf{A}^{*}\mathbf{A}\mathbb{E}[\mathbf{x}\mathbf{x}^{*}]\right)=\frac{1}{d}\mathrm{Tr}(\mathbf{A}^{*}\mathbf{A})=\frac{1}{d}\left\|\mathbf{A}\right\|_{F}^{2}.

[234] p: For a normal 𝐀 \mathbf{A} , ‖ 𝐀 ‖ F 2 = ∑ j = 1 d | λ j | 2 \left\|\mathbf{A}\right\|_{F}^{2}=\sum_{j=1}^{d}|\lambda_{j}|^{2} , giving

[235] table: 𝔼 ​ ‖ 𝐀𝐱 ‖ 2 2 = 1 d ​ ∑ j = 1 d | λ j | 2 . \mathbb{E}\left\|\mathbf{A}\mathbf{x}\right\|_{2}^{2}=\frac{1}{d}\sum_{j=1}^{d}|\lambda_{j}|^{2}.

[236] p: If ρ ⁡ ( 𝐀 ) ≤ 1 + ϵ u \rho(\mathbf{A})\leq 1+\epsilon_{u} , then | λ j | 2 ≤ ( 1 + ϵ u ) 2 |\lambda_{j}|^{2}\leq(1+\epsilon_{u})^{2} for all j j , giving the upper bound. For the lower bound, at least a fraction M ≈ 1 ​ ( 𝐀 ) M_{\approx 1}(\mathbf{A}) of the eigenvalues satisfy | λ j | ≥ 1 − ϵ n |\lambda_{j}|\geq 1-\epsilon_{n} , so

[237] table: 𝔼 ​ ‖ 𝐀𝐱 ‖ 2 2 ≥ ( 1 − ϵ n ) 2 ​ M ≈ 1 ​ ( 𝐀 ) . \mathbb{E}\left\|\mathbf{A}\mathbf{x}\right\|_{2}^{2}\geq(1-\epsilon_{n})^{2}M_{\approx 1}(\mathbf{A}).

[238] p: For the diagonalizable extension 𝐀 = 𝐕 ​ 𝚲 ​ 𝐕 − 1 \mathbf{A}=\mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1} , note that for an isotropic 𝐱 \mathbf{x} we always have 𝔼 ​ ‖ 𝐀𝐱 ‖ 2 2 = 1 d ​ ‖ 𝐀 ‖ F 2 \mathbb{E}\left\|\mathbf{A}\mathbf{x}\right\|_{2}^{2}=\frac{1}{d}\left\|\mathbf{A}\right\|_{F}^{2} . Moreover, 1 κ ⁡ ( 𝐕 ) ​ ‖ 𝚲 ‖ F ≤ ‖ 𝐀 ‖ F ≤ κ ⁡ ( 𝐕 ) ​ ‖ 𝚲 ‖ F \frac{1}{\kappa(\mathbf{V})}\left\|\boldsymbol{\Lambda}\right\|_{F}\leq\left\|\mathbf{A}\right\|_{F}\leq\kappa(\mathbf{V})\left\|\boldsymbol{\Lambda}\right\|_{F} , so 𝔼 ​ ‖ 𝐀𝐱 ‖ 2 2 \mathbb{E}\left\|\mathbf{A}\mathbf{x}\right\|_{2}^{2} is within factors κ ​ ( 𝐕 ) ± 2 \kappa(\mathbf{V})^{\pm 2} of 1 d ​ ∑ j | λ j | 2 \frac{1}{d}\sum_{j}|\lambda_{j}|^{2} . Combining this with ρ ⁡ ( 𝐀 ) ≤ 1 + ϵ u \rho(\mathbf{A})\leq 1+\epsilon_{u} and the definition of M ≈ 1 ​ ( 𝐀 ) M_{\approx 1}(\mathbf{A}) yields the stated bound. ∎

[239] h5: Proof of Corollary 2 .

[240] h6: Proof.

[241] p: Assume 𝔼 ⁡ [ 𝐡 ℓ ​ 𝐡 ℓ ∗ ] = 1 d ​ 𝔼 ​ ‖ 𝐡 ℓ ‖ 2 2 ​ 𝐈 \mathbb{E}[\mathbf{h}_{\ell}\mathbf{h}_{\ell}^{*}]=\frac{1}{d}\mathbb{E}\left\|\mathbf{h}_{\ell}\right\|_{2}^{2}\mathbf{I} for each ℓ = 0 , … , L − 1 \ell=0,\dots,L-1 . Let q ℓ ≜ 1 d ​ ∑ j = 1 d | λ j ℓ | 2 q_{\ell}\triangleq\frac{1}{d}\sum_{j=1}^{d}|\lambda_{j}^{\ell}|^{2} . Then

[242] table: 𝔼 ​ ‖ 𝐡 ℓ + 1 ‖ 2 2 = Tr ⁡ ( 𝐀 ℓ ∗ ​ 𝐀 ℓ ​ 𝔼 ​ [ 𝐡 ℓ ​ 𝐡 ℓ ∗ ] ) = q ℓ ​ 𝔼 ​ ‖ 𝐡 ℓ ‖ 2 2 , \mathbb{E}\left\|\mathbf{h}_{\ell+1}\right\|_{2}^{2}=\mathrm{Tr}\left(\mathbf{A}_{\ell}^{*}\mathbf{A}_{\ell}\mathbb{E}[\mathbf{h}_{\ell}\mathbf{h}_{\ell}^{*}]\right)=q_{\ell}\mathbb{E}\left\|\mathbf{h}_{\ell}\right\|_{2}^{2},

[243] p: and recursion yields 𝔼 ​ ‖ 𝐡 L ‖ 2 2 = 𝔼 ​ ‖ 𝐡 0 ‖ 2 2 ​ ∏ ℓ = 0 L − 1 q ℓ \mathbb{E}\left\|\mathbf{h}_{L}\right\|_{2}^{2}=\mathbb{E}\left\|\mathbf{h}_{0}\right\|_{2}^{2}\prod_{\ell=0}^{L-1}q_{\ell} . By Theorem 1 , q ℓ ≥ ( 1 − ϵ n ) 2 ​ M ≈ 1 ​ ( 𝐀 ℓ ) q_{\ell}\geq(1-\epsilon_{n})^{2}M_{\approx 1}(\mathbf{A}_{\ell}) , proving the stated bound. ∎

[244] h2: Appendix D Experimental Details

[245] p: We ran experiments on 4 × \times NVIDIA A100-SXM4-40GB graphics processing unit (GPU) devices. We ran experiments across six normalization strategies, including Pre-LN, Post-LN, RMSNorm, DeepNorm, SubLN, and No-Norm, with additional architecture-specific studies on MoE [ Shazeer et al., 2017 ] , Mamba [ Gu and Dao, 2023 ] , and KAN [ Liu et al., 2024 ] .

[246] p: We use the following hyperparameters. Models use d ∈ { 128,256,512,768 , 1024 } d\in\{128,256,512,768,1024\} , n heads ∈ { 4 , 8 , 16 } n_{\mathrm{heads}}\in\{4,8,16\} , and L ∈ { 4 , 6 , 8 , 12 , 16 , 24 } L\in\{4,6,8,12,16,24\} . For training, the mini-batch size is 16 to 32 with 5 to 20 epochs and 100 to 1000 warmup steps. We use the AdamW and sweep learning rates within standard ranges. We use seeds { 42,123,456 } \{42,123,456\} for reproducibility. Our default recipe estimates randomized DMD eigenvalues with rank r = 32 r=32 using N = 2048 N=2048 snapshots with ϵ = 10 − 5 \epsilon=10^{-5} . KSS is applied every 10 to 20 steps, sampling 50% of layers per update to reduce overhead. We sweep the regularization weight α ∈ { 0.01 , 0.05 , 0.10 , 0.15 , 0.20 } \alpha\in\{0.01,0.05,0.10,0.15,0.20\} ; the resulting overhead ranges from 8% to 12% in practice.

[247] h3: D.1 Associative-Recall Task

[248] p: The associative-recall task refers to a synthetic key-value retrieval classification task commonly used to probe associative memory and recall in long-context sequence models [ Fu et al., 2023 , Arora et al., 2024 ] . For each sample, we generate n pairs n_{\mathrm{pairs}} key-value pairs { ( k i , v i ) } i = 1 n pairs \{(k_{i},v_{i})\}_{i=1}^{n_{\mathrm{pairs}}} and construct

[249] table: 𝐱 = [ k 1 , v 1 , … , k n pairs , v n pairs , p 1 , … , p m , q ] , \mathbf{x}=[k_{1},v_{1},\ldots,k_{n_{\mathrm{pairs}}},v_{n_{\mathrm{pairs}}},p_{1},\ldots,p_{m},q],

[250] p: where q q is a query key chosen from { k i } \{k_{i}\} and the label is the corresponding matched value y = v j y=v_{j} . The model predicts only this final target with cross-entropy on the last-position logits, implemented as F.cross_entropy(logits[:, -1, :], y) .

[251] h3: D.2 Synthetic LM Task

[252] p: This synthetic token-level language modeling setup is inspired by prior work using controlled synthetic sequences to analyze recall and long-range behavior in efficient sequence models [ Fu et al., 2023 , Arora et al., 2024 ] . Each sample is a length- T T token sequence over a vocabulary of size V V ; unless stated otherwise, we use T = 256 T=256 and V = 10,000 V=10{,}000 . A sequence is generated by concatenating randomly sampled segments until reaching length T T , then truncating. Segments come in three types: repetition segments repeat a short pattern of length 2 to 5 for 2 to 4 repeats, sequential segments are contiguous integer runs of length 5 to 15, and random segments are independently and identically distributed tokens of length 5 to 15. All tokens are sampled from { 10 , … , V − 1 } \{10,\dots,V-1\} so that a small identifier range remains available for special tokens. Sequences are generated directly at the token level by these rules.

[253] p: The learning objective is standard next-token prediction. Given tokens ( x 1 , … , x T ) (x_{1},\dots,x_{T}) , the model predicts x t + 1 x_{t+1} from the prefix ( x 1 , … , x t ) (x_{1},\dots,x_{t}) and is trained with token-level cross-entropy over t = 1 , … , T − 1 t=1,\dots,T-1 . We report validation token accuracy and perplexity exp ⁡ ( mean cross-entropy ) \exp(\text{mean cross-entropy}) on a held-out synthetic validation split. For large-scale runs, we use 20K training sequences and 2K validation sequences per trial, regenerated deterministically from the run seed.

[254] h3: D.3 Pretrained LM Fixed-Prompt Protocol

[255] p: We use a forward-only profiling protocol with a deterministic text set and no fine-tuning updates, in the same spirit as prompt-based evaluation and activation-probing analyses of pretrained transformers [ Brown et al., 2020 , Elhage et al., 2021 ] . The fixed short-prompt setting is implemented as explicit prompt lists with 32 total prompts per run, either 4 prompts repeated 8 times or 8 prompts repeated 4 times, and both variants use a token length cap of 64. For each model, we run a single batched forward pass with hidden-state outputs enabled and collect residual-stream activations from the embedding and transformer layer outputs.

[256] p: For each layer transition ( ℓ , ℓ + 1 ) (\ell,\ell+1) , we flatten token positions, subsample up to N ∈ { 1024 , 2048 } N\in\{1024,2048\} token states, and apply whitened DMD. Spectral partitions use the same thresholds as the analysis code: unstable when | λ | > 1.05 |\lambda|>1.05 , near-unit when 0.90 ≤ | λ | ≤ 1.05 0.90\leq|\lambda|\leq 1.05 , and over-damped when | λ | < 0.80 |\lambda|<0.80 . We report early, middle, and late summaries by splitting layers into depth thirds and averaging each metric within the corresponding group.

[257] h2: Appendix E Computational Cost

[258] p: Whitened DMD requires O ⁡ ( d 2 ​ N + d 3 ) O(d^{2}N+d^{3}) operations. Randomized singular value decomposition reduces this cost to O ⁡ ( d ​ N ​ r + r 3 ) O(dNr+r^{3}) for rank- r r approximation. With typical values d = 768 d=768 , N = 2048 N=2048 , and r = 32 r=32 , full RKSP analysis completes in 2.5 to 3.5 seconds per layer on a single GPU.

[259] h2: Appendix F Extended Baseline and Optimizer Comparisons

[260] h3: F.1 Extended Optimizer Baselines

[261] p: We extend the baseline comparisons to include μ \mu P and the Layer-wise Adaptive Moments for Batch training (LAMB) optimizer [ You et al., 2020 ] .

[262] h5: μ \mu P.

[263] p: The μ \mu P enables hyperparameter transfer across different model widths by appropriately scaling learning rates appropriately. Table 13 summarizes the μ \mu P comparisons and the combined μ \mu P + KSS setting. We observe moderate stability gains from μ \mu P, with a 38% divergence reduction through initialization scaling. The combined μ \mu P + KSS approach achieves the lowest divergence, 8.3%, and the highest accuracy, 51.5%. The μ \mu P setting enables transfer, while KSS provides stability, and the distinct mechanisms suggest orthogonal benefits.

[264] figure: Table 13: Comparison of μ \mu P, standard parameterization, and KSS. Results use the No-Norm setting with learning rate ranges from 0.005 to 0.01 across 24 trials. Measured on the associative-recall task. Method Div.% (lower) Acc.% (higher) M ≈ 1 M_{\approx 1} Transfer Overhead Standard Init, AdamW 66.7 66.7 28.5 28.5 0.85 0.85 ✗ — μ \mu P, width transfer 41.7 41.7 35.8 35.8 0.72 0.72 ✓ < 1 % <1\% μ \mu P + higher learning rate 50.0 50.0 38.2 38.2 0.78 0.78 ✓ < 1 % <1\% KSS, α = 0.15 \alpha=0.15 12.5 \mathbf{12.5} 48.2 \mathbf{48.2} 0.58 0.58 ✗ 10.8 % 10.8\% μ \mu P + KSS 8.3 \mathbf{8.3} 51.5 \mathbf{51.5} 0.52 0.52 ✓ 11.2 % 11.2\%

[265] h5: LAMB Optimizer.

[266] p: LAMB normalizes updates per layer, which changes spectral dynamics. Table 14 reports the optimizer comparison, including LAMB and Lion. LAMB outperforms AdamW: its layer-wise normalization provides implicit stability with a 31% divergence reduction. LAMB enables higher learning rates, reaching 3 × \times to 4 × \times AdamW, or up to 7 × \times with learning rate warmup. KSS still provides orthogonal benefits, and the LAMB + KSS combination achieves the best results at 8.3% divergence and 52.8% accuracy. From a spectral perspective, LAMB suppresses expansive mass and reduces near-unit mass, from 0.85 with AdamW to 0.75, suggesting that its stability gains come from damping unstable modes and increasing damping; within comparable unstable-mass regimes, a lower M ≈ 1 M_{\approx 1} aligns with greater stability.

[267] figure: Table 14: Optimizer comparison among AdamW, LAMB, and Lion. Results use the No-Norm setting, 24 trials each. Measured on the associative-recall task. Optimizer Div.% (lower) Acc.% (higher) M ≈ 1 M_{\approx 1} Best LR Overhead AdamW 66.7 66.7 28.5 28.5 0.85 0.85 0.003 0.003 — AdamW + grad clip 58.3 58.3 30.8 30.8 0.83 0.83 0.005 0.005 < 1 % <1\% LAMB 45.8 45.8 36.2 36.2 0.75 0.75 0.01 0.01 about 5% LAMB + warmup 37.5 37.5 40.8 40.8 0.68 0.68 0.02 0.02 about 5% Lion 45.8 45.8 36.5 36.5 0.78 0.78 0.001 0.001 about 15% KSS, α = 0.15 \alpha=0.15 12.5 \mathbf{12.5} 48.2 \mathbf{48.2} 0.58 0.58 0.008 0.008 10.8 % 10.8\% LAMB + KSS 8.3 \mathbf{8.3} 52.8 \mathbf{52.8} 0.52 0.52 0.015 0.015 about 16%

[268] h2: Appendix G Large-Scale Pretrained Model Analysis

[269] h5: GPT-2 Analysis.

[270] p: Table 15 reports layer-group spectral statistics for GPT-2 [ Radford et al., 2019 ] , and Figure 4 reveals a universal pattern. The normalized linear-fit error η nl \eta_{\mathrm{nl}} increases with depth, rising from [ 0.48 , 0.52 ] [0.48,0.52] in the early layers to [ 0.68 , 0.71 ] [0.68,0.71] in late layers. Simultaneously, the near-unit mass decreases from M ≈ 1 ∈ [ 0.68 , 0.72 ] M_{\approx 1}\in[0.68,0.72] to M ≈ 1 ∈ [ 0.58 , 0.60 ] M_{\approx 1}\in[0.58,0.60] . This depth-wise trend has a clear implication: early layers are more linearly approximable, making DMD features more reliable, whereas late layers are less so.

[271] figure: Table 15: GPT-2 layer-wise spectral analysis. Start Linear, End Nonlinear pattern, shorthand for increasing η nl \eta_{\mathrm{nl}} . Spectral statistics are computed from residual-stream activations on a fixed set of short prompt sentences. Measured on a fixed short-prompt set. Model Layers ρ \rho κ ⁡ ( 𝐕 ) \kappa(\mathbf{V}) η nl \eta_{\mathrm{nl}} M ≈ 1 M_{\approx 1} GPT-2 124M Early 0 to 3 1.15 1.15 8.3 8.3 0.52 0.52 0.68 0.68 GPT-2 124M Middle 4 to 7 1.23 1.23 10.1 10.1 0.61 0.61 0.62 0.62 GPT-2 124M Late 8 to 11 1.31 1.31 11.2 11.2 0.71 0.71 0.58 0.58 GPT-2 355M Early 0 to 7 1.12 1.12 7.5 7.5 0.48 0.48 0.72 0.72 GPT-2 355M Middle 8 to 15 1.19 1.19 9.2 9.2 0.58 0.58 0.65 0.65 GPT-2 355M Late 16 to 23 1.27 1.27 10.8 10.8 0.68 0.68 0.60 0.60

[272] figure: Figure 4: Start Linear, End Nonlinear pattern. Layer-wise normalized linear-fit error η nl \eta_{\mathrm{nl}} across four pretrained models. All models exhibit a monotonically increasing η nl \eta_{\mathrm{nl}} with depth, suggesting a consistent linear-approximation signature across models. Computed from residual-stream activations on a fixed set of short prompt sentences.

[273] h2: Appendix H Calibration

[274] p: Beyond discrimination measured by AUROC, we assess calibration quality. Figure 5 shows that the risk score M ≈ 1 M_{\approx 1} achieves an Expected Calibration Error (ECE) of 0.283, indicating moderate calibration. The reliability diagram reveals deviations between predicted probabilities and observed frequencies, while the distribution plots show clear separation between converged runs with lower M ≈ 1 M_{\approx 1} , corresponding to lower risk, and diverged runs with higher M ≈ 1 M_{\approx 1} , corresponding to higher risk. This calibration quality matters for deployment: practitioners can interpret RKSP’s probability estimates for early termination decisions while accounting for the moderate calibration.

[275] figure: Figure 5: Calibration reliability diagram. (Left) Predicted divergence probability versus observed frequency, with an ECE of 0.283. (Right) Distribution of predictions separated by actual outcome. RKSP provides moderately calibrated probability estimates. Based on associative-recall runs, calibration compares predictions to divergence outcomes from that task.

[276] h2: Appendix I Novel Architecture Case Studies

[277] p: To demonstrate RKSP’s value beyond standard transformers, we analyze three emerging architectures: MoE [ Shazeer et al., 2017 ] , SSMs including Mamba [ Gu and Dao, 2023 ] , and KAN [ Liu et al., 2024 ] .

[278] h5: MoE Transformers

[279] p: Table 16 presents a comparison of MoE routing and stability [ Shazeer et al., 2017 ] . MoE routing induces a higher normalized linear-fit error: η nl \eta_{\mathrm{nl}} increases 15% to 20% compared to dense transformers due to discrete routing decisions. The choice of top- k k affects spectral stability—higher k k shifts spectral mass and changes M ≈ 1 M_{\approx 1} alongside non-normality and unstable modes. The divergence reductions are consistent with suppressing unstable modes, and within comparable non-normality regimes, larger M ≈ 1 M_{\approx 1} aligns with greater instability. KSS stabilizes MoE effectively, yielding a 4 × \times divergence reduction with 6% accuracy improvement, thereby validating RKSP and KSS for novel architectures.

[280] figure: Table 16: MoE transformer with RKSP analysis. Routing instability revealed via spectral signatures. Results use d = 256 d=256 , L = 6 L=6 , and 24 trials. Load balancing loss λ = 0.01 \lambda=0.01 . Measured on the synthetic LM task with random-token next-token prediction. Configuration Top- k k M ≈ 1 M_{\approx 1} ρ \rho η nl \eta_{\mathrm{nl}} Div. of 24 Acc.% MoE-Small, 8 experts k = 1 k=1 0.72 0.72 2.85 2.85 0.68 0.68 6 of 24 32.4 32.4 MoE-Small, 8 experts k = 2 k=2 0.58 0.58 2.12 2.12 0.55 0.55 2 of 24 41.7 41.7 MoE-Small, 8 experts k = 4 k=4 0.45 0.45 1.78 1.78 0.48 0.48 1 of 24 38.2 38.2 MoE-Medium, 16 experts k = 2 k=2 0.65 0.65 2.45 2.45 0.61 0.61 4 of 24 38.9 38.9 MoE-Medium, 16 experts k = 2 k=2 + KSS 0.48 0.48 1.92 1.92 0.58 0.58 1 of 24 44.5 \mathbf{44.5}

[281] h5: State Space Models: Mamba

[282] p: Table 17 compares SSM and transformer spectral properties for Mamba [ Gu and Dao, 2023 ] . The theoretical explanation is straightforward: SSMs are designed with stable discrete-time dynamics via highly structured polynomial projection operator initialization. RKSP reveals this design choice explicitly in the spectral signature: Mamba exhibited M < 1 ≈ 0.85 ≫ M ≈ 1 ≈ 0.12 M_{<1}\approx 0.85\gg M_{\approx 1}\approx 0.12 . This separation indicates strongly contractive dynamics with short memory and weak near-isometry; stability here comes from suppressed unstable modes in a highly contractive regime. In transformer regimes that are closer to near-normal, larger M ≈ 1 M_{\approx 1} corresponds to weaker damping, longer-range signal retention, and higher instability risk.

[283] figure: Table 17: Mamba with RKSP analysis. Inherently stable spectral structure. Results use L = 6 L=6 , 24 trials. Measured on the synthetic LM task with random-token next-token prediction. Model M ≈ 1 M_{\approx 1} M < 1 M_{<1} ρ \rho Div. of 24 Acc.% Mamba-Small, d = 256 d=256 0.12 0.12 0.85 0.85 0.95 0.95 0 of 24 48.2 48.2 Mamba-Medium, d = 512 d=512 0.15 0.15 0.82 0.82 0.97 0.97 0 of 24 52.6 52.6 Transformer, Pre-LN, comparable 0.42 0.42 0.38 0.38 1.85 1.85 1 of 24 45.8 45.8

[284] h5: KAN

[285] p: Table 18 reports KAN spectral diagnostics and KSS outcomes [ Liu et al., 2024 ] . KAN shows high normalized linear-fit error: B-spline basis functions produce η nl ≈ [ 0.78 , 0.82 ] \eta_{\mathrm{nl}}\approx[0.78,0.82] , higher than the typical transformer layers with [ 0.4 , 0.7 ] [0.4,0.7] . Despite this high η nl \eta_{\mathrm{nl}} , RKSP remains informative—ResDMD filtering enables spectral analysis for 68% to 78% of modes. KSS benefits KAN with a 3 × \times to 4 × \times divergence reduction, suggesting that spectral shaping is architecture-agnostic.

[286] figure: Table 18: KAN transformer with RKSP analysis. The B-spline nonlinearity challenges linear approximation. The B-spline order is B B . We use d = 256 d=256 , L = 6 L=6 , and 24 trials. Measured on the synthetic LM task with random-token next-token prediction. Model η nl \eta_{\mathrm{nl}} M ≈ 1 M_{\approx 1} ρ \rho Div. of 24 DMD reliability KAN-Transformer, B = 4 B=4 0.78 0.78 0.52 0.52 2.15 2.15 3 of 24 Marginal, 68% KAN-Transformer, B = 8 B=8 0.82 0.82 0.48 0.48 2.35 2.35 4 of 24 Low, 52% KAN-Transformer + KSS 0.75 0.75 0.42 0.42 1.92 1.92 1 of 24 Improved, 78%

[287] h5: Cross-Architecture Summary

[288] p: Table 11 summarizes cross-architecture metrics, while Figure 6 provides a normalized radar-chart view of the same comparison.

[289] figure: Figure 6: Cross-architecture spectral radar chart. Comparison of five architectures across five normalized metrics. Mamba exhibits strong contraction with low M ≈ 1 M_{\approx 1} and short memory; stability is maintained via suppressed unstable modes, while in near-normal transformer regimes, higher M ≈ 1 M_{\approx 1} aligns with more unstable, near-isometric propagation. The No-Norm transformer shows high memory capacity but poor stability. KAN exhibits high η nl \eta_{\mathrm{nl}} . Metrics are derived from Table 11 .

[290] h2: Appendix J Practical Notes

[291] p: RKSP and KSS are most valuable in three scenarios. First, when mechanistic understanding matters, RKSP explains why Pre-LN outperforms Post-LN through spectral signatures. Second, when pushing training limits, KSS enables learning rates that are 50% to 150% higher for faster convergence. Third, when deploying novel architectures, RKSP verifies stability before expensive training runs. Edge cases benefit most from these diagnostics—situations where standard normalization fails or where training operates near stability boundaries.

[292] h5: Fixup and ReZero-style identity initialization.

[293] p: A common stabilization trick in deep residual networks and transformers is to initialize the final projection of each residual branch to zero, for example the attention and MLP output weights, so that the network starts close to an identity map [ Zhang et al., 2019 , Bachlechner et al., 2021 ] . In our notation, this yields a residual-off regime with a vanishing layer update 𝐡 ℓ + 1 − 𝐡 ℓ ≈ 𝟎 \mathbf{h}_{\ell+1}-\mathbf{h}_{\ell}\approx\mathbf{0} , so the snapshot pairs satisfy 𝐘 ℓ ≈ 𝐗 ℓ \mathbf{Y}_{\ell}\approx\mathbf{X}_{\ell} and DMD returns 𝐀 ^ ℓ ≈ 𝐈 \hat{\mathbf{A}}_{\ell}\approx\mathbf{I} . Consequently, M ≈ 1 ℓ M_{\approx 1}^{\ell} can be close to 1 1 across layers even though training is often stable under Fixup and ReZero at initialization.

[294] p: Taken alone, a near-identity spectrum might seem to imply maximal instability risk. However, our instability mechanism assumes two conditions: weak damping with large M ≈ 1 M_{\approx 1} under near-normality, and non-degenerate layer-wise dynamics with appreciable updates so that perturbations and optimization noise are repeatedly injected and propagated across depth. Fixup and ReZero violate the second condition at initialization. When ‖ 𝐘 ~ ℓ − 𝐗 ~ ℓ ‖ F \left\|\tilde{\mathbf{Y}}_{\ell}-\tilde{\mathbf{X}}_{\ell}\right\|_{F} is near zero, there is essentially no layer-wise update to analyze, and the resulting DMD spectrum is not informative about the noisy training-time regime we target.

[295] p: Practically, this degeneracy is detectable from the same quantities RKSP already computes. When ‖ 𝐘 ~ ℓ − 𝐗 ~ ℓ ‖ F ≈ 0 \left\|\tilde{\mathbf{Y}}_{\ell}-\tilde{\mathbf{X}}_{\ell}\right\|_{F}\approx 0 , the normalization in the nonlinearity ratio Eq. 5 becomes ill-conditioned, so η nl ​ ( ℓ ) \eta_{\mathrm{nl}}(\ell) should be interpreted as a DMD reliability flag rather than as a meaningful nonlinearity estimate. For Fixup and ReZero, RKSP becomes informative after a small amount of training, once the zero-initialized residual projections move away from zero and layer-wise updates become observable; at that point, RKSP can again capture whether the residual stream exhibits excessive near-isometric propagation (large M ≈ 1 M_{\approx 1} ) that correlates with high-learning-rate divergence.

[296] p: Practical deployment is straightforward. We recommend using RKSP in four scenarios: first, as a fast filter during architecture search; second, before expensive hyperparameter grid search; third, for periodic spectral monitoring during training; and fourth, for debugging checkpoints before divergence. Figure 7 provides an actionable decision process.

[297] figure: Run RKSP at initialization. Compute M ≈ 1 M_{\approx 1} and κ ⁡ ( 𝐕 ) \kappa(\mathbf{V}) for the decision. Meets safe-region criteria M ≈ 1 < 0.3 M_{\approx 1}<0.3 and modest κ ⁡ ( 𝐕 ) \kappa(\mathbf{V}) Proceed without KSS. Under this criterion, training is more stable; optionally, monitor with periodic RKSP snapshots. Decide on KSS by context. If M ≈ 1 > 0.5 M_{\approx 1}>0.5 or κ ⁡ ( 𝐕 ) \kappa(\mathbf{V}) is large, treat as high risk. Use KSS for aggressive learning rates above 2 × 2\times standard, for no-normalization settings, or for novel architectures with RKSP monitoring. Skip KSS for standard Pre-LN and RMSNorm at conservative learning rates. yes no Figure 7: Decision flowchart for when to use RKSP and KSS in practice.

[298] h2: Instructions for reporting errors

[299] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[300] p: Tip: You can select the relevant text first, to include it in your report.

[301] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[302] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
