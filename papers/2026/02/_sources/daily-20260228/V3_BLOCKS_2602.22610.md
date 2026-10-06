[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: DP-aware AdaLN-Zero: Taming Conditioning-Induced Heavy-Tailed Gradients in Differentially Private Diffusion

[3] h6: Abstract

[4] p: Condition injection enables diffusion models to generate context-aware outputs, which is essential for many time-series tasks. However, heterogeneous conditional contexts (e.g., observed history, missingness patterns or outlier covariates) can induce heavy-tailed per-example gradients. Under D ifferentially P rivate S tochastic G radient D escent (DP-SGD), these rare conditioning-driven heavy-tailed gradients disproportionately trigger global clipping, resulting in outlier-dominated updates, larger clipping bias, and degraded utility under a fixed privacy budget. In this paper, we propose DP-aware AdaLN-Zero, a drop-in sensitivity-aware conditioning mechanism for conditional diffusion transformers that limits conditioning-induced gain without modifying the DP-SGD mechanism. DP-aware AdaLN-Zero jointly constrains conditioning representation magnitude and AdaLN modulation parameters via bounded re-parameterization, suppressing extreme gradient tail events before gradient clipping and noise injection. Empirically, DP-SGD equipped with DP-aware AdaLN-Zero improves interpolation/imputation and forecasting under matched privacy settings. We observe consistent gains on a real-world power dataset and two public ETT benchmarks over vanilla DP-SGD. Moreover, gradient diagnostics attribute these improvements to conditioning-specific tail reshaping and reduced clipping distortion, while preserving expressiveness in non-private training. Overall, these results show that sensitivity-aware conditioning can substantially improve private conditional diffusion training without sacrificing standard performance.

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] p: Diffusion models learn expressive data distributions through iteratively denoising corrupted samples, and have become a leading paradigm for conditional generation ( Ho et al., 2020 ; Song et al., 2021 ; Fu et al., 2024 ; Zhan et al., 2024 ) . In time-series domain, diffusion-based methods achieve strong performance in probabilistic forecasting and imputation by conditioning on historical context, covariates, or partially observed trajectories ( Rasul et al., 2021 ; Tashiro et al., 2021 ) . However, such reliance on rich conditioning signals often involves sensitive attributes and individual-level histories, motivating mechanisms that enable model or synthetic data release while limiting inference about any single record.

[8] p: Differential privacy (DP) provides a rigorous guarantee that the output of an algorithm changes only slightly across adjacent datasets differing in a single training example ( Dwork and Roth, 2014 ) . Differentially Private Stochastic Gradient Descent (DP-SGD) ( Abadi et al., 2016 ) is the predominant algorithm for differentially private training of deep models. It clips per-example gradients and adds calibrated Gaussian noise to ensure ( ε , δ ) (\varepsilon,\delta) -DP. Yet, for diffusion models—particularly conditional diffusion—DP-SGD often yields a severe privacy-utility trade-off. Recent work mitigates this gap by tailoring parameterization, optimization, and sampling to diffusion ( Dockhorn et al., 2023 ) , by leveraging public pretraining followed by differentially private fine-tuning ( Ghalebikesabi et al., 2023 ) ; or by reducing redundant privacy noise via reuse of forward-process noise ( Wang et al., 2024 ) . However, a critical challenge remains unaddressed: conditioning amplifies gradient sensitivity under DP-SGD.

[9] p: We study conditional diffusion for time-series data, where the conditioning variables include observed history, missingness patterns, or outlier covariates. The resulting conditioning distribution is often highly heterogeneous, driven by diverse missingness structures, rare events, and extreme covariate values. This heterogeneity can produce heavy-tailed per-example gradient norms, particularly along the conditioning pathway. Under DP-SGD, a small fraction of updates with unusually large conditioning-induced gradients can dominate the clipping criterion, forcing aggressive clipping. This increases the effective noise-to-signal ratio and introduces a systematic optimization bias. Namely, parameter updates become disproportionately influenced by rare conditioning outliers rather than representative examples, which degrades utility even when the model backbone would otherwise train stably. Importantly, this failure mode cannot be addressed by improving diffusion-specific DP mechanisms alone; it requires explicitly sensitivity-aware conditioning mechanisms.

[10] p: This paper focuses specifically on conditional diffusions, which typically incorporate conditioning via widely used adaptive LayerNorm (AdaLN) modulation and its zero-initialized variant (AdaLN-Zero). While effective, such modulation can amplify sensitivity ( Peebles and Xie, 2023 ) . To overcome this issue, we propose DP-aware AdaLN-Zero , which preserves the DP mechanism while reshaping per-example gradient norms to suppress conditioning-induced spikes, reduce outlier-dominated clipping, and stabilize training under a fixed privacy budget. Specifically, our contributions are summarized as follows:

[11] p: We identify a conditioning-driven sensitivity imbalance in differentially private conditional diffusion models: rare conditioning events can induce heavy-tailed per-example gradients that disproportionately trigger gradient clipping;

[12] p: We propose DP-aware AdaLN-Zero, a sensitivity-aware conditioning mechanism that bounds AdaLN modulation by constraining conditioning representation magnitude and AdaLN modulation parameters;

[13] p: Empirically, our approach stabilizes private training dynamics and yields higher downstream utility at the same noise scale than vanilla DP-SGD.

[14] h2: 2 Related Work

[15] h5: Diffusion models and conditional generation.

[16] p: Diffusion models learn to reverse a corruption process, enabling high-quality generation ( Sohl-Dickstein et al., 2015 ; Ho et al., 2020 ; Song et al., 2021 ) . In conditional diffusion, guidance techniques offer additional control via contextual information (e.g., labels, or observed history) at inference time. Classifier guidance improves conditional alignment by exploiting gradients from an auxiliary classifier ( Dhariwal and Nichol, 2021 ; Ho and Salimans, 2022 ) . More recently, diffusion transformers (DiT) popularized conditioning via normalization-based modulation mechanisms such as AdaLN and AdaLN-Zero ( Peebles and Xie, 2023 ) . While effective, modulation-based conditioning can amplify the gain of the conditioning pathway. Amplified responses can result in disproportionately large per-example gradients, making clipping more aggressive under DP-SGD.

[17] h5: Diffusion models for time series.

[18] p: Diffusion models have been adapted for time-series forecasting and imputation by conditioning denoisers on temporal context and partially observations. TimeGrad introduces an autoregressive diffusion framework for multivariate probabilistic forecasting ( Rasul et al., 2021 ) , and CSDI trains conditional score-based diffusion for probabilistic time-series imputation ( Tashiro et al., 2021 ) . However, they do not consider differentially private training, and their conditioning signals (e.g., observed masks/values) can be highly heterogeneous—exactly the regime in which DP-SGD is vulnerable to heavy-tailed per-example gradients.

[19] h5: Differential privacy for deep learning.

[20] p: DP formalizes privacy as the stability of an algorithm’s output to changes in any single training record ( Dwork and Roth, 2014 ) . DP-SGD enforces this guarantee by clipping per-example gradients and adding calibrated Gaussian noise ( Abadi et al., 2016 ) . However, frequent clipping introduces bias and reduces the effective optimization signal ( Hou et al., 2025 ) . This effect is amplified when gradient norms are heavy-tailed or when particular submodules occasionally produce extreme gradients.

[21] h5: Differentially private diffusion models.

[22] p: DPDM ( Dockhorn et al., 2023 ) demonstrates that diffusion models can generate high-quality samples under DP by leveraging diffusion-specific design choices, including tailored sampling procedures and adaptations of DP-SGD. DP-promise ( Wang et al., 2024 ) further argues that naively applying DP-SGD to diffusion can inject redundant gradient noise on top of the stochasticity already present in the forward process, and proposes reusing forward-process noise to obtain approximate DP with improved utility. However, these approaches do not readily extend to larger-scale diffusion models with explicit conditional pathways, where conditioning-induced gradient amplification can dominate the privacy–utility trade-off.

[23] h5: Limitations in differentially private diffusion work.

[24] p: Despite recent progress, existing differentially private diffusion methods largely optimize global training components, such as privacy accounting, sampler design, and pretraining/fine-tuning. They are evaluated mainly on unconditional or weakly conditional image generation. Moreover, they do not explicitly address a failure mode in conditional diffusion models: conditioning-induced sensitivity imbalance. In conditional time-series diffusion, conditioning can produce rare but extreme per-example gradients. Under DP-SGD, these extremes disproportionately trigger clipping, causing outlier-dominated updates, systematic bias toward small-norm directions, and reduced effective signal-to-noise after noise injection. Crucially, better samplers or global noise reallocation do not directly prevent conditioning from acting as an amplification channel that creates heavy-tailed gradient norms.

[25] h2: 3 Method

[26] h3: 3.1 Preliminaries

[27] h5: Conditional Diffusion.

[28] p: We denote the conditioning vector by 𝐜 ∈ ℝ k \mathbf{c}\in\mathbb{R}^{k} . Let g g be gradients: g i g_{i} is the per-example gradient, with ‖ g i ‖ 2 \|g_{i}\|_{2} its ℓ 2 \ell_{2} norm. We consider a conditional time-series diffusion model parameterized by θ \theta , whose denoiser predicts noise (or velocity) from an input x x conditioned on 𝐜 \mathbf{c} (e.g., covariates, mask-aware statistics, or global context):

[29] table: y = f θ ​ ( x , 𝐜 ) , y=f_{\theta}(x,\mathbf{c}), (1)

[30] p: where f θ f_{\theta} is a stack of AdaLN-Zero blocks. For a hidden state h ∈ ℝ d h\in\mathbb{R}^{d} and a condition 𝐜 ∈ ℝ k \mathbf{c}\in\mathbb{R}^{k} , a typical AdaLN-Zero block computes

[31] table: u = LN ⁡ ( h ) , v = γ ⊙ u + β , h = F ⁡ ( v , θ F ) , y = x + α ⊙ h , u=\mathrm{LN}(h),\,v=\gamma\odot u+\beta,\,h=F(v;\theta_{F}),\,y=x+\alpha\odot h, (2)

[32] p: where LN \mathrm{LN} is LayerNorm, F F is a self-attention/MLP subnetwork, and ( γ , β , α ) (\gamma,\beta,\alpha) are per-block modulation parameters obtained from 𝐜 \mathbf{c} . This conditioning pathway acts as a gain control: large modulation values amplify activations and local Jacobians, yielding rare but extreme per-example gradients.

[33] h5: Vanilla DP-SGD.

[34] p: Consider training with vanilla DP-SGD, for a mini-batch D = { z i } i = 1 B D=\{z_{i}\}_{i=1}^{B} with examples z i = ( x i , 𝐜 i ) z_{i}=(x_{i},\mathbf{c}_{i}) , let

[35] table: g i ​ ( θ ) = ∇ θ ℓ ​ ( f θ ​ ( z i ) ) g_{i}(\theta)\;=\;\nabla_{\theta}\,\ell\!\big(f_{\theta}(z_{i})\big) (3)

[36] p: denote the per-example gradient of the training loss ℓ \ell . Vanilla DP-SGD clips each per-example gradient to a threshold C > 0 C>0 :

[37] table: g ~ i ​ ( θ ) = g i ​ ( θ ) ⋅ min ⁡ ( 1 , C ‖ g i ​ ( θ ) ‖ 2 ) , \tilde{g}_{i}(\theta)=g_{i}(\theta)\cdot\min\!\left(1,\frac{C}{\|g_{i}(\theta)\|_{2}}\right), (4)

[38] p: and releases a noisy average of clipped gradients. The standard analysis upper-bounds the ℓ 2 \ell_{2} -sensitivity of this update by C B \frac{C}{B} , independent of model structure and conditioning.

[39] figure: (a) ECDF of gradient norms in normal training. (b) CCDF (tail) of gradient norms in normal training. Figure 1: Condition-amplified extremes exist even without DP. We compare normal training with training under DP-aware constraints without DP. Under normal training, ‖ g cond ‖ 2 \|g_{\mathrm{cond}}\|_{2} is comparable to ‖ g other ‖ 2 \|g_{\mathrm{other}}\|_{2} at typical quantiles (see the blue curve in Figure 1(a) ), but ‖ g cond ‖ 2 \|g_{\mathrm{cond}}\|_{2} exhibits rarer and heavier high-end tail events (see the blue curve in Figure 1(b) ). In contrast, DP-aware constraints selectively suppress the high-end tail of ‖ g cond ‖ 2 \|g_{\mathrm{cond}}\|_{2} (and consequently that of ‖ g ‖ 2 \|g\|_{2} ) far more than ‖ g other ‖ 2 \|g_{\mathrm{other}}\|_{2} : p ​ 99 p99 drops by ∼ 3.5 × \sim 3.5\times for ‖ g cond ‖ 2 \|g_{\mathrm{cond}}\|_{2} vs. ∼ 1.2 × \sim 1.2\times for ‖ g other ‖ 2 \|g_{\mathrm{other}}\|_{2} . This indicates targeted suppression of conditioning-induced amplification rather than uniform shrinkage, and suggests that (in DP-SGD) clipping events would be disproportionately governed by rare conditioning-path extremes.

[40] h3: 3.2 Structural Limits of Global Clipping

[41] p: In AdaLN-Zero conditional diffusion, employing a single global clipping threshold C C fails to account for a crucial architectural asymmetry. To address this, we partition the parameters into two distinct groups: (i) conditioning-path parameters θ cond \theta_{\mathrm{cond}} (the projections that map 𝐜 \mathbf{c} to ( γ , β , α ) (\gamma,\beta,\alpha) and parameters directly on the conditioning injection pathway); and (ii) other parameters θ other \theta_{\mathrm{other}} (all remaining parameters). The corresponding per-example gradient decomposes as:

[42] table: g i = ( g i cond , g i other ) . \displaystyle g_{i}=\big(g^{\mathrm{cond}}_{i},g^{\mathrm{other}}_{i}\big).

[43] p: This decomposition highlights two coupled issues:

[44] p: (i) Clipping is often governed by rare conditioning-path tail events. Due to multiplicative modulation in AdaLN-Zero, the conditioning map 𝐜 ↦ ( γ , β , α ) \mathbf{c}\mapsto(\gamma,\beta,\alpha) can induce heavy-tailed gradients on θ cond \theta_{\mathrm{cond}} . Equivalently, in the high-threshold regime relevant to clipping, conditioning-driven extremes are more likely to exceed large thresholds for sufficiently large t t :

[45] table: Pr ⁡ ( ‖ g i cond ‖ 2 > t ) ≫ Pr ⁡ ( ‖ g i other ‖ 2 > t ) . \Pr\!\big(\|g^{\mathrm{cond}}_{i}\|_{2}>t\big)\;\gg\;\Pr\!\big(\|g^{\mathrm{other}}_{i}\|_{2}>t\big).

[46] p: Thus, rare condition-amplified gradient spikes can disproportionately elevate ‖ g i ‖ 2 \|g_{i}\|_{2} beyond C C , thereby increasing the activation probability of gradient clipping.

[47] p: (ii) Global clipping uses a single scalar shrinkage, attenuating conditional learning. DP-SGD clips by rescaling each per-example gradient: g ~ i = η i ​ g i \tilde{g}_{i}=\eta_{i}g_{i} , where η i = min ⁡ ( 1 , C ‖ g i ‖ 2 ) \eta_{i}=\min\!\left(1,\frac{C}{\|g_{i}\|_{2}}\right) . When ‖ g i ‖ 2 > C \|g_{i}\|_{2}>C is triggered primarily by a spike in g i cond g^{\mathrm{cond}}_{i} , the scalar η i \eta_{i} uniformly shrinks all coordinates, including non-extreme updates in θ other \theta_{\mathrm{other}} and the non-spiking part of θ cond \theta_{\mathrm{cond}} . This creates a privacy-utility dilemma: decreasing C C reduces the DP noise scale (proportional to C C ) but increases the clipping-induced distortion, while increasing C C reduces clipping distortion but amplifies DP noise.

[48] p: Figure 1 shows evidence for this issue in non-private training. The parameter set θ cond \theta_{\mathrm{cond}} is often much smaller than θ other \theta_{\mathrm{other}} . However, the per-example gradient norm ‖ g i cond ‖ 2 \|g_{i}^{\mathrm{cond}}\|_{2} has a much heavier high-end tail than ‖ g i other ‖ 2 \|g_{i}^{\mathrm{other}}\|_{2} . This result means that conditioning can create unusually large gradients even in standard training.

[49] p: Selective bounds on conditioning gain reduce these extreme values. In particular, we attempt to shrink the high-end tail of ‖ g i cond ‖ 2 \|g_{i}^{\mathrm{cond}}\|_{2} . As a result, the high-end tail of the total norm ‖ g i ‖ 2 \|g_{i}\|_{2} can be reduced. In DP-SGD, clipping depends on ‖ g i ‖ 2 \|g_{i}\|_{2} through η i \eta_{i} . A smaller tail in ‖ g i ‖ 2 \|g_{i}\|_{2} reduces clipping distortion and helps the model learn from the conditioning signal.

[50] h3: 3.3 DP-aware AdaLN-Zero Design

[51] p: The discussion above identifies the conditioning pathway as the key target. The global condition 𝐜 \mathbf{c} and modulation parameters ( γ , β , α ) (\gamma,\beta,\alpha) control the magnitude of hidden representations and their Jacobians. We aim to bound this forward-pass gain, while leaving DP-SGD unchanged.

[52] p: DP-aware AdaLN-Zero applies deterministic per-block constraints to bound the effect of 𝐜 \mathbf{c} and the AdaLN modulation parameters on the conditioning pathway. For each block, we first ℓ 2 \ell_{2} -bound the global condition:

[53] table: 𝐜 ^ = Proj ‖ 𝐜 ‖ 2 ≤ c max ​ ( 𝐜 ) , \hat{\mathbf{c}}\;=\;\mathrm{Proj}_{\|\mathbf{c}\|_{2}\leq c_{\max}}(\mathbf{c}), (5)

[54] p: where c max > 0 c_{\max}>0 is a fixed constant. The AdaLN parameters are then obtained from 𝐜 ^ \hat{\mathbf{c}} through linear projections,

[55] table: ( γ raw , β raw , α raw ) = W ​ 𝐜 ^ + b , (\gamma_{\mathrm{raw}},\beta_{\mathrm{raw}},\alpha_{\mathrm{raw}})=W\hat{\mathbf{c}}+b, (6)

[56] p: followed by coordinatewise clipping:

[57] table: ( γ , β , α ) = ℬ M ​ ( ( γ raw , β raw , α raw ) , ( γ max , β max , α max ) ) , (\gamma,\beta,\alpha)=\mathcal{B}_{M}\big((\gamma_{\mathrm{raw}},\beta_{\mathrm{raw}},\alpha_{\mathrm{raw}}),(\gamma_{\max},\beta_{\max},\alpha_{\max})\big), (7)

[58] p: where ( c max , γ max , β max , α max ) (c_{\max},\gamma_{\max},\beta_{\max},\alpha_{\max}) control per-block modulation strength by enforcing | γ | ≤ γ max |\gamma|\leq\gamma_{\max} , | β | ≤ β max |\beta|\leq\beta_{\max} , and | α | ≤ α max |\alpha|\leq\alpha_{\max} . By default, we implement the coordinate-wise bounding operator ℬ M ​ ( ⋅ ) \mathcal{B}_{M}(\cdot) as ℬ M tanh ​ ( x ) = M ​ tanh ⁡ ( x M ) \mathcal{B}_{M}^{\tanh}(x)=M\tanh(\frac{x}{M}) .

[59] p: The bound in Eq.( 7 ) introduces negligible overhead and is applied before gradient computation. By limiting the magnitude of conditioning signal and the induced modulation parameters, it constrains intermediate activations and their Jacobians, suppressing rare condition-amplified spikes that would otherwise produce extreme per-example gradients.

[60] p: DP-aware AdaLN-Zero improves DP-SGD without modifying DP mechanism. In vanilla DP-SGD (without DP-aware deterministic constraints), a conditioning-induced spike can push the global ℓ 2 \ell_{2} -norm ‖ g i ‖ 2 \|g_{i}\|_{2} above the clipping threshold C C , causing the entire gradient to be uniformly rescaled and thus attenuating conditional updates, even for parameters that do not contribute to the spike. By limiting conditioning-path amplification in every block via Eqs.( 5 )-( 7 ), our approach mitigates such spike-induced global shrinkage and the resulting clipping distortion.

[61] h3: 3.4 Sensitivity Analysis of DP-Aware AdaLN-Zero

[62] p: This section provides a structural worst-case analysis to justify why bounding the AdaLN-Zero conditioning pathway can control the magnitude of per-example gradients. Although stated in terms of ℓ 2 \ell_{2} -sensitivity, the analysis should be interpreted as a mechanistic guarantee arising from architectural constraints.

[63] p: We first derive a per-example gradient bound under DP-aware constraints. Assuming standard regularity conditions (bounded inputs, Lipschitz blocks on bounded domains, bounded loss gradient, bounded spectral norms), intermediate Jacobians remain controlled whenever activations are bounded. DP-aware constraints guarantee boundedness along the conditioning pathway. Specifically, for each block,

[64] table: ‖ 𝐜 ‖ 2 ≤ c max , \displaystyle\|\mathbf{c}\|_{2}\leq c_{\max}, ‖ γ ‖ ∞ ≤ γ max , \displaystyle\|\gamma\|_{\infty}\leq\gamma_{\max},\, (8) ‖ β ‖ ∞ ≤ β max , \displaystyle\|\beta\|_{\infty}\leq\beta_{\max}, ‖ α ‖ ∞ ≤ α max . \displaystyle\|\alpha\|_{\infty}\leq\alpha_{\max}.

[65] p: These bounds limit the modulation strength, thereby controlling hidden states and their Jacobians.

[66] p: Let θ \theta be all model parameters and z = ( x , 𝐜 ) z=(x,\mathbf{c}) a training example. We write ∇ θ ℓ ​ ( f θ ​ ( x , 𝐜 ) ) \nabla_{\theta}\ell\big(f_{\theta}(x,\mathbf{c})\big) for the corresponding per-example gradient. For analysis, we partition θ \theta into parameters in F F (attention/MLP), projection layers generating ( γ , β , α ) (\gamma,\beta,\alpha) from 𝐜 \mathbf{c} , and remaining parameters (e.g., LayerNorm, skip connections). Under Eq.( 8 ), each component’s contribution to gradient norm can be bounded, yielding Proposition 3.1 .

[67] h6: Proposition 3.1 (Per-Example Gradient Bound with DP-aware Constraints) .

[68] p: Under the DP-aware constraints (Eq.( 8 )) and the standard regularity assumptions, there exist non-negative, architecture-dependent constants A 0 , a c , a γ , a β , a α ≥ 0 A_{0},a_{c},a_{\gamma},a_{\beta},a_{\alpha}\geq 0 , such that for every training example z = ( x , 𝐜 ) z=(x,\mathbf{c}) ,

[69] table: ‖ ∇ θ ℓ ​ ( f θ ​ ( x , 𝐜 ) ) ‖ 2 ≤ S aware , \displaystyle\bigl\|\nabla_{\theta}\ell\big(f_{\theta}(x,\mathbf{c})\big)\bigr\|_{2}\leq S_{\mathrm{aware}}, (9) S aware ≔ A 0 + a c ​ c max + a γ ​ γ max + a β ​ β max + a α ​ α max . \displaystyle S_{\mathrm{aware}}\coloneqq A_{0}+a_{c}c_{\max}+a_{\gamma}\gamma_{\max}+a_{\beta}\beta_{\max}+a_{\alpha}\alpha_{\max}.

[70] p: The proof of Proposition 3.1 is given in Appendix A .

[71] p: Next, we derive the sensitivity of the DP-SGD update and examine its implications for clipping. Consider one DP-SGD step with batch size B B and global clipping threshold C C . For each example z i z_{i} in a batch D = { z i } i = 1 B D=\{z_{i}\}_{i=1}^{B} , DP-SGD computes g ~ i = g i ⋅ min ⁡ ( 1 , C ‖ g i ‖ 2 ) \tilde{g}_{i}=g_{i}\cdot\min\!\left(1,\frac{C}{\|g_{i}\|_{2}}\right) and q ⁡ ( D ) = 1 B ​ ∑ i = 1 B g ~ i q(D)=\frac{1}{B}\sum_{i=1}^{B}\tilde{g}_{i} .

[72] p: For vanilla DP-SGD, clipping ensures ‖ g ~ i ‖ 2 ≤ C \|\tilde{g}_{i}\|_{2}\leq C , yielding the global ℓ 2 \ell_{2} -sensitivity bound: Δ 2 ​ ( q vanilla ) ≤ C B \Delta_{2}(q_{\mathrm{vanilla}})\leq\frac{C}{B} . For DP-SGD with DP-aware AdaLN-Zero, Proposition 3.1 implies ‖ g i ‖ 2 ≤ S aware \|g_{i}\|_{2}\leq S_{\mathrm{aware}} for all i i . When S aware ≤ C S_{\mathrm{aware}}\leq C , clipping is never triggered and g ~ i = g i \tilde{g}_{i}=g_{i} for all examples. Consequently, the sensitivity satisfies Δ 2 ​ ( q aware ) ≤ S aware B \Delta_{2}(q_{\mathrm{aware}})\leq\frac{S_{\mathrm{aware}}}{B} .

[73] p: To facilitate a direct comparison between the sensitivity of our method and that of vanilla DP-SGD, we define

[74] table: ρ ≔ Δ 2 ​ ( q aware ) Δ 2 ​ ( q vanilla ) ≤ S aware C . \rho\coloneqq\frac{\Delta_{2}(q_{\mathrm{aware}})}{\Delta_{2}(q_{\mathrm{vanilla}})}\leq\frac{S_{\mathrm{aware}}}{C}. (10)

[75] p: In our experiments, we match ( C , σ ) (C,\sigma) between vanilla DP-SGD (DP-vanilla) and DP-SGD with DP-aware AdaLN-Zero (DP-aware) and focus on utility. Eq.( 10 ) is adopted as a structural statement: by limiting conditioning-induced gain, DP-aware suppresses outliers and mitigates the distortion of conditional updates caused by clipping. In Appendix B , we further show that under certain conditions, ρ ≤ 1 \rho\leq 1 always holds.

[76] h3: 3.5 Diagnostic of Gradient Dynamics

[77] figure: Interpolation/Imputation Forecasting Model σ \sigma point_RMSE ↓ \downarrow point_MAPE ↓ \downarrow point_MAE ↓ \downarrow point_RMSE ↓ \downarrow dist_JS ↓ \downarrow temp_spec_dist ↓ \downarrow Non-DP - 0.584 1.174% 0.476 0.208 0.767 1.484e-4 DP-vanilla 0.03 3.034 5.673% 2.391 0.556 0.736 7.848e-4 DP-aware 1.804 3.541% 1.411 0.296 0.684 2.900e-4 DP-vanilla 0.05 3.498 9.339% 3.110 0.567 0.643 1.650e-3 DP-aware 2.019 4.970% 1.987 0.423 0.636 8.558e-4 DP-vanilla 0.1 5.787 11.674% 4.702 1.637 0.833 1.902e-2 DP-aware 2.718 5.267% 2.122 0.671 0.757 3.240e-3 DP-vanilla 0.2 6.812 12.645% 5.148 1.646 0.794 1.592e-2 DP-aware 4.689 8.406% 3.442 1.262 0.732 1.052e-2 Table 1: Results on PrivatePower under matched DP training. We evaluate mask-conditioned interpolation/imputation and forecasting. All metrics are lower-is-better. Bold marks the better of DP-vanilla and DP-aware at each σ \sigma .

[78] p: Section 3.4 derives a worst-case theoretical bound on per-example gradients for DP-aware AdaLN-Zero. However, such guarantees often fail to capture typical training behavior. We therefore complement the theory with empirical diagnostics of gradient distributions and clipping-induced distortion, offering a more faithful view of DP-SGD optimization dynamics.

[79] p: Concretely, we quantify how DP-aware constraints affect typical per-example gradient magnitudes through an empirical factor ρ emp \rho_{\mathrm{emp}} . We run two diagnostic trainings, DP-vanilla and DP-aware, under identical architecture, optimizer, and DP settings (global clipping threshold C C and noise multiplier σ \sigma ). During training, for each sample z i = ( x i , 𝐜 i ) z_{i}=(x_{i},\mathbf{c}_{i}) , we log the full per-example gradient norm ‖ g i ‖ 2 \|g_{i}\|_{2} , as well as the norms of its two parameter partitions: ‖ g i cond ‖ 2 = ‖ ∇ θ cond ℓ ​ ( f θ ​ ( z i ) ) ‖ 2 \|g_{i}^{\mathrm{cond}}\|_{2}=\|\nabla_{\theta_{\mathrm{cond}}}\ell(f_{\theta}(z_{i}))\|_{2} and ‖ g i other ‖ 2 = ‖ ∇ θ other ℓ ​ ( f θ ​ ( z i ) ) ‖ 2 \|g_{i}^{\mathrm{other}}\|_{2}=\|\nabla_{\theta_{\mathrm{other}}}\ell(f_{\theta}(z_{i}))\|_{2} .

[80] p: Since these norms fluctuate across training steps, we summarize them with robust statistics. Let Stat ⁡ ( ⋅ ) \mathrm{Stat}(\cdot) denote a robust summary operator—such as p ​ 95 / p ​ 99 p95/p99 —applied to all logged per-example gradients. We define S total (vanilla) ≔ Stat ⁡ ( ‖ g i ‖ 2 ) S_{\mathrm{total}}^{\text{(vanilla)}}\coloneqq\mathrm{Stat}\big(\|g_{i}\|_{2}\big) and S total (aware) ≔ Stat ⁡ ( ‖ g i ‖ 2 ) S_{\mathrm{total}}^{\text{(aware)}}\coloneqq\mathrm{Stat}\big(\|g_{i}\|_{2}\big) , where the statistic is evaluated over the DP-vanilla and DP-aware diagnostic trajectories, respectively. The reduction factors are then

[81] table: ρ emp ≔ S total (aware) S total (vanilla) , ρ cond ≔ S cond (aware) S cond (vanilla) . \rho_{\mathrm{emp}}\coloneqq\frac{S_{\mathrm{total}}^{\text{(aware)}}}{S_{\mathrm{total}}^{\text{(vanilla)}}},\,\rho_{\mathrm{cond}}\coloneqq\frac{S_{\mathrm{cond}}^{\text{(aware)}}}{S_{\mathrm{cond}}^{\text{(vanilla)}}}. (11)

[82] p: Here, ρ emp , cond \rho_{\mathrm{emp},\mathrm{cond}} captures the average reduction in per-example gradient-norm scale (or tail quantile) along training trajectories. It provides no worst-case sensitivity guarantee and is not assumed to upper-bound the theoretical ρ \rho in Eq.( 10 ). We thus use ρ emp \rho_{\mathrm{emp}} only as a diagnostic metric for gradient dynamics.

[83] h2: 4 Experiments

[84] h3: 4.1 Experimental Setup

[85] h5: Datasets.

[86] p: We evaluate our method on one real-world electricity dataset (PrivatePower) and two public benchmarks (ETTh1 and ETTm1). PrivatePower is an hourly single-meter electricity-usage time series spanning 2023-01-01 to 2025-08-22, with one record per hour. Each preprocessed window contains the standardized target power_usage along with time-derived and user-derived conditioning channels. We set the maximum channel number to K max = 7 K_{\max}=7 and the sequence length to L = 168 L=168 (one week). ETTh1 (hourly) and ETTm1 (15-min) are widely used multivariate benchmarks from the Electricity Transformer Temperature (ETT) suite ( Zhou et al., 2021 ) , comprising seven variables (one target and six covariates) and following standard chronological train/validation/test splits. See Appendix G for additional dataset details.

[87] h5: Model.

[88] p: We implement the conditional diffusion model of TimeDiT and use its masking-based unified training scheme (random/stride/block masks) to support multiple conditional tasks (forecasting, interpolation, and imputation ( Cao et al., 2024 ) ). For PrivatePower, we use a Transformer backbone with 8 layers, hidden size 256, and 8 attention heads. For ETTh1/ETTm1, we keep the same architecture and adjust only L max L_{\max} to match the dataset resolution and ETT evaluation window.

[89] figure: (a) ECDF of per-example gradient norms in training at noise multiplier σ = 0.20 \sigma=0.20 . (b) CCDF (tail) of per-example gradient norms at noise multiplier σ = 0.20 \sigma=0.20 . Figure 2: Gradient-norm distributions under DP training . Compared to DP-vanilla, DP-aware primarily suppresses the extreme tail of the conditioning pathway with minimal impact on the bulk of the distribution, indicating fewer condition-amplified outliers rather than uniform gradient shrinkage.

[90] figure: σ \sigma Model p95 Statistics p99 Statistics S other S_{\text{other}} S cond S_{\text{cond}} S total S_{\text{total}} ρ emp \rho_{\text{emp}} ρ cond \rho_{\text{cond}} S other S_{\text{other}} S cond S_{\text{cond}} S total S_{\text{total}} ρ emp \rho_{\text{emp}} ρ cond \rho_{\text{cond}} 0.03 DP-vanilla 25.0 17.8 31.1 – – 58.4 49.5 76.5 – – DP-aware 24.6 16.4 29.7 0.955 0.921 57.5 43.7 72.0 0.949 0.883 0.05 DP-vanilla 24.1 19.6 31.4 – – 62.4 62.4 89.2 – – DP-aware 24.2 18.9 30.9 0.984 0.964 55.6 55.5 77.3 0.867 0.889 0.10 DP-vanilla 23.8 21.4 32.1 – – 62.8 68.3 92.7 – – DP-aware 24.4 20.3 31.2 0.972 0.949 54.9 57.4 83.1 0.896 0.840 0.20 DP-vanilla 20.3 21.7 30.0 – – 57.0 64.5 86.6 – – DP-aware 20.3 20.4 28.9 0.963 0.940 47.4 54.8 71.9 0.830 0.850 Table 2: Gradient-norm diagnostics on PrivatePower across noise multipliers σ \sigma . We report robust high-percentile summaries ( p ​ 95 p95 / p ​ 99 p99 ) of per-example gradient norms for conditioning-path parameters ‖ g cond ‖ 2 \|g_{\mathrm{cond}}\|_{2} and remaining parameters ‖ g other ‖ 2 \|g_{\mathrm{other}}\|_{2} . We also report a compact proxy S total S_{\text{total}} , empirical diagnostics ρ emp \rho_{\mathrm{emp}} and ρ cond \rho_{\mathrm{cond}} ; values below 1 1 indicate reductions relative to DP-vanilla under matched ( C , σ ) (C,\sigma) .

[91] h5: Conditional tasks based masks.

[92] p: Let x ∈ ℝ L × C x\in\mathbb{R}^{L\times C} be a length- L L multivariate sequence with C C channels, and m ∈ { 0 , 1 } L m\in\{0,1\}^{L} a binary mask, where m t = 1 m_{t}=1 indicates an observed time step and m t = 0 m_{t}=0 a missing one. Given the partially observed sequence and mask-aware features, the model generates missing values conditioned on the observed entries. We consider three mask schemes: (i) Random mask, which masks a random subset of time steps for interpolation/imputation, with missing fraction set by ratio_range ; (ii) Block mask, which masks a contiguous block at the end of the sequence for forecasting, with the prediction horizon controlled by pred_len_range ; and (iii) Stride mask, which masks multiple blocks according to a structured stride pattern controlled by num_blocks_range , targeting interpolation/imputation under structured missingness. More details are provided in Appendix G .

[93] h5: Training and DP-SGD setup.

[94] p: All models are trained using identical settings: AdamW (learning rate = 7 × 10 − 4 =7\times 10^{-4} , weight decay = 2 × 10 − 5 =2\times 10^{-5} ), 1000 1000 -step linear warmup, mixed precision, and exponential moving average (EMA) with decay 0.999 0.999 . Training is run for T = 20,000 T=20{,}000 steps ( 200 200 steps per epoch) with batch size B = 96 B=96 , and validation is performed every 1000 1000 steps. DP is enforced via DP-SGD with per-example gradient clipping at threshold C = 1.0 C=1.0 and Gaussian noise injection calibrated by noise multiplier σ \sigma . DP-aware modifies only the forward pass via bounded conditioning, leaving DP-SGD unchanged.

[95] h3: 4.2 Model Utility under Matched DP Mechanisms

[96] p: We compare non-private training ( Non-DP ), vanilla DP-SGD ( DP-vanilla ), and DP-SGD augmented with our proposed DP-Aware AdaLN-Zero ( DP-aware ) on PrivatePower. Table 1 reports representative metrics for interpolation/imputation and forecasting. For interpolation, we assess point-wise accuracy via point_RMSE, point_MAPE, and point_MAE. For forecasting, we report point_RMSE talong with a distributional metric (dist_JS) and a temporal-structure metric (temp_spec_dist).

[97] p: Table 1 shows that DP-aware consistently outperforms DP-vanilla across both tasks and all tested noise multipliers. Gains are largest in the low-noise regime, yet remain evident as noise increases. This corroborates our central claim. For fixed DP hyperparameters, bounding conditioning-induced gain improves conditional generation utility. Full per- σ \sigma results are provided in Appendix C .

[98] p: Figure 2 further visualizes per-example gradient-norm distributions. DP-aware exhibits clear tail-suppression: while the bulk of its distribution closely aligns with DP-vanilla, extreme gradient events, particularly for ‖ g cond ‖ 2 \|g_{\mathrm{cond}}\|_{2} , occur less frequently. Together with Table 1 , this confirms that DP-aware reduces rare, condition-amplified gradient spikes that dominate global clipping, thus improving training stability and conditional generation utility.

[99] h3: 4.3 Gradient Dynamics and Clipping Behavior

[100] p: Following Section 3.5 , we empirically study DP-SGD dynamics, starting with gradient-norm tails. During training, we record per-example gradient norms for conditioning-path parameters ( ‖ g cond ‖ 2 \|g_{\mathrm{cond}}\|_{2} ) and all other parameters ( ‖ g other ‖ 2 \|g_{\mathrm{other}}\|_{2} ). For each run, we summarize these norms using robust high-percentile statistics ( p ​ 95 p95 / p ​ 99 p99 ) over all logged steps and samples, denoted as S cond ( ⋅ ) S_{\text{cond}}^{(\cdot)} and S other ( ⋅ ) S_{\text{other}}^{(\cdot)} , along with a compact proxy S total S_{\text{total}} . As average-case diagnostics, we also report ρ emp \rho_{\text{emp}} and ρ cond \rho_{\text{cond}} , which are empirical summaries of observed scale/tail changes relative to DP-vanilla. Table 2 reveals a consistent trend across noise multipliers: DP-aware only mildly affects S other S_{\text{other}} , but markedly reduces the tail of S cond S_{\text{cond}} , especially at p ​ 99 p99 . This demonstrates that by bounding the conditioning gain in the forward pass, DP-aware mainly suppresses rare condition-amplified outliers instead of uniformly shrinking gradients.

[101] figure: σ \sigma Model p clip p_{\mathrm{clip}} 𝔼 ⁡ [ η ] \mathbb{E}[\eta] η 10 \eta_{10} η 50 \eta_{50} η 90 \eta_{90} 0.03 DP-vanilla 0.561 0.73 0.18 0.86 1.00 DP-aware 0.556 0.75 0.22 0.88 1.00 0.20 DP-vanilla 0.589 0.70 0.12 0.82 1.00 DP-aware 0.585 0.72 0.15 0.84 1.00 Table 3: Clipping statistics under matched C C . We report the clipping rate p clip p_{\mathrm{clip}} and quantiles of the clipping factor η \eta . Across noise multipliers, p clip p_{\mathrm{clip}} remains comparable, while DP-aware slightly increases low-quantile and median values of η \eta , suggesting reduced clipping severity.

[102] figure: Model Variant 𝐜 \mathbf{c} bounded ( γ , β , α ) (\gamma,\beta,\alpha) bounded ρ emp \rho_{\text{emp}} Forecast point_RMSE ↓ \downarrow Forecast dist_JS ↓ \downarrow DP-vanilla × \times × \times 1.00 0.567 0.723 DP-aware (only 𝐜 \mathbf{c} -bounding) ✓ \checkmark × \times 0.95 0.510 0.691 DP-aware (only AdaLN bounding) × \times ✓ \checkmark 0.93 0.495 0.677 DP-aware (full, ours) ✓ \checkmark ✓ \checkmark 0.87 0.423 0.636 Table 4: Effects of forward-pass control components. We report ρ emp ​ ( p ​ 99 ) \rho_{\text{emp}}(p99) and forecasting metrics (lower is better).

[103] p: Tail behavior is crucial in DP-SGD, as large gradient norms trigger clipping and distort updates. For a clipping threshold C C , we measure clipping activation rate p clip ≔ Pr [ ∥ g i ∥ 2 > C ] p_{\mathrm{clip}}\coloneqq\Pr\!\big[\|g_{i}\|_{2}>C\big] and clipping severity η i ≔ min ⁡ ( 1 , C ‖ g i ‖ 2 ) \eta_{i}\coloneqq\min\!\left(1,\frac{C}{\|g_{i}\|_{2}}\right) , where smaller η i \eta_{i} means stronger rescaling. Table 3 shows that under matched ( C , σ ) (C,\sigma) , DP-vanilla and DP-aware have comparable p clip p_{\mathrm{clip}} , while DP-aware yields slightly larger η \eta at lower quantiles and around the median, implying milder clipping. Combined with the observed reduction in tail gradient norms in Table 2 , particularly along the conditioning pathway, this suggests that DP-aware preserves similar clipping frequency while attenuating extreme gradient spikes, hence fewer severe clipping events. More results are presented in Appendix D .

[104] p: Overall, under matched parameter settings, DP-aware improves utility by altering optimization dynamics: DP-vanilla is more prone to conditioning-induced tail events that trigger global clipping and distort updates; whereas DP-aware suppresses such outliers in the forward pass, making conditional signals more robust to clipping. We provide more training-time signals in Appendix F .

[105] h3: 4.4 Ablation Studies

[106] p: Next, we investigate the impact of key design choices in DP-aware AdaLN-Zero on downstream utility. We perform ablations on PrivatePower for forecasting, using identical DP hyperparameters for DP-vanilla and DP-aware variants.

[107] h4: 4.4.1 Effects of Forward-Pass Control Components

[108] p: DP-aware applies two forward-pass controls: ℓ 2 \ell_{2} -norm bounding of conditioning vector 𝐜 \mathbf{c} and coordinate-wise bounding of AdaLN modulations ( γ , β , α ) (\gamma,\beta,\alpha) . We ablate these components by comparing only 𝐜 \mathbf{c} -bounding , only AdaLN bounding , full DP-aware model and the DP-vanilla model. Table 4 shows that each component provides a measurable gain, and their combination achieves the best utility, highlighting the importance of regulating both global conditioning and per-block modulation for stable conditional learning under DP-SGD.

[109] h4: 4.4.2 Effect of the AdaLN Modulation Bounding Operator

[110] p: DP-aware bounds AdaLN modulation parameters ( γ , β , α ) (\gamma,\beta,\alpha) via a coordinate-wise operator ℬ M ​ ( ⋅ ) \mathcal{B}_{M}(\cdot) . Our default choice is ℬ M tanh ​ ( ⋅ ) \mathcal{B}_{M}^{\tanh}(\cdot) , but alternatives include hard truncation and near-identity bounds that deviate from identity only in a narrow boundary band. Concretely, we compare four realizations:

[111] p: tanh (default): ℬ M tanh ​ ( x ) = M ​ tanh ⁡ ( x / M ) \mathcal{B}_{M}^{\tanh}(x)=M\tanh(x/M) ;

[112] p: hard_clamp : ℬ M hard ​ ( x ) = min ⁡ ( M , max ⁡ ( − M , x ) ) \mathcal{B}_{M}^{\mathrm{hard}}(x)=\min(M,\max(-M,x)) ;

[113] p: soft_clamp_band : identity for | x | ≤ M − ε |x|\leq M-\varepsilon , smooth transition in [ M − ε , M + ε ] [M-\varepsilon,\,M+\varepsilon] , saturation for | x | ≥ M + ε |x|\geq M+\varepsilon ;

[114] p: clamp_ste : the forward pass applies a hard clamp ( hard_clamp ), while the backward pass uses a straight-through estimator.

[115] p: Experimental results in Table 5 show that smooth operators ( tanh , soft_clamp_band ) perform comparably and consistently outperform hard truncation variants ( hard_clamp , clamp_ste ). All operators achieve better results than vanilla DP-SGD (point_RMSE( 0.567 0.567 ), dist_JS( 0.643 0.643 ), and temp_spec_dist(1.650e-3) ). This indicates that DP-aware’s gains mainly arise from bounding modulation to suppress extreme tail behavior, rather than from a particular function. Yet, in practice, DP-aware prefers smooth operators. See Appendix C.3 for more results across tasks and noise levels.

[116] figure: ℬ M ​ ( ⋅ ) \mathcal{B}_{M}(\cdot) point_RMSE ↓ \downarrow dist_JS ↓ \downarrow temp_spec_dist ↓ \downarrow tanh \tanh (default) 0.423 0.636 8.558e-4 soft_clamp_band 0.425 0.639 8.70e-4 hard_clamp 0.452 0.662 9.45e-4 clamp_ste 0.467 0.674 9.90e-4 Table 5: Effect of the bounding operator ℬ M ​ ( ⋅ ) \mathcal{B}_{M}(\cdot) at σ = 0.05 \sigma{=}0.05 .

[117] p: Appendix E presents more ablations, examining the effects of tightness settings, DP-aware architectural constraints, clipping thresholds, and interpolation/imputation metrics.

[118] h2: 5 Conclusion and Future Work

[119] p: Under DP-SGD, conditional diffusion models suffer a failure mode wherein conditioning amplifies sensitivity, producing heavy-tailed gradients. These outliers dominate the global clipping of per-example gradients, thus uniformly shrinking updates and inducing a systematic optimization bias that diffusion-specific DP improvements at the global mechanism level cannot resolve. To address this issue, we propose the DP-aware AdaLN-Zero, a sensitivity-aware conditioning module without modifying the DP-SGD mechanism. By jointly constraining the conditioning representation and the AdaLN modulation parameters, our approach selectively suppresses extreme gradient tails along the conditioning-path parameters, leading to milder clipping distortion.

[120] p: Future work can extend our approach in several directions. We will integrate DP-aware conditioning with advanced DP diffusion pipelines, such as pretraining followed by DP fine-tuning, to further improve the privacy–utility trade-off. We will also replace the offline choices of ( c max , γ max , β max , α max ) (c_{\max},\gamma_{\max},\beta_{\max},\alpha_{\max}) with principled, privacy-preserving calibration methods. Layer- or block-wise adaptive bounds may improve robustness across datasets and tasks. In addition, we will extend the sensitivity-control principle to richer conditioning interfaces, including cross-attention, encoder–decoder conditioning, and multi-source context, to go beyond AdaLN-style modulation.

[121] h2: References

[122] h2: Appendix A Proof Details for Proposition 1

[123] p: In this section, we provide detailed derivations for Proposition 1 in the main text. We first state the assumptions used throughout the analysis. We then bound the Jacobians of a single AdaLN-Zero block, derive per-sample gradient bounds for each parameter group, and conclude by summarizing the resulting DP-SGD sensitivity bounds.

[124] h3: A.1 Assumptions

[125] p: We adopt the following assumptions, which are standard in worst-case sensitivity analysis.

[126] h6: Assumption A.1 (Bounded inputs) .

[127] p: There exists a constant X max > 0 X_{\max}>0 such that, for all training examples x x ,

[128] table: ‖ x ‖ 2 ≤ X max . \|x\|_{2}\leq X_{\max}. (12)

[129] h6: Assumption A.2 (LayerNorm boundedness and Lipschitzness) .

[130] p: There exist constants U max > 0 U_{\max}>0 and L LN > 0 L_{\mathrm{LN}}>0 such that, for all x , x 1 , x 2 x,x_{1},x_{2} ,

[131] table: ‖ LN ⁡ ( x ) ‖ 2 \displaystyle\|\mathrm{LN}(x)\|_{2} ≤ U max , \displaystyle\leq U_{\max}, (13) ‖ LN ⁡ ( x 1 ) − LN ⁡ ( x 2 ) ‖ 2 \displaystyle\|\mathrm{LN}(x_{1})-\mathrm{LN}(x_{2})\|_{2} ≤ L LN ​ ‖ x 1 − x 2 ‖ 2 . \displaystyle\leq L_{\mathrm{LN}}\|x_{1}-x_{2}\|_{2}.

[132] h6: Assumption A.3 (Feedforward/Attention boundedness and Lipschitzness) .

[133] p: Let F F denote the feedforward or attention sub-layer. There exist constants H max > 0 H_{\max}>0 and L F > 0 L_{F}>0 such that, for all v , v 1 , v 2 v,v_{1},v_{2} in the reachable domain of F F ,

[134] table: ‖ F ⁡ ( v ) ‖ 2 \displaystyle\|F(v)\|_{2} ≤ H max , \displaystyle\leq H_{\max}, (14) ‖ F ⁡ ( v 1 ) − F ⁡ ( v 2 ) ‖ 2 \displaystyle\|F(v_{1})-F(v_{2})\|_{2} ≤ L F ​ ‖ v 1 − v 2 ‖ 2 . \displaystyle\leq L_{F}\|v_{1}-v_{2}\|_{2}.

[135] h6: Assumption A.4 (Bounded loss gradients) .

[136] p: There exists a constant G ℓ > 0 G_{\ell}>0 such that, for all reachable outputs y y ,

[137] table: ‖ ∇ y ℓ ​ ( y ) ‖ 2 ≤ G ℓ . \|\nabla_{y}\ell(y)\|_{2}\leq G_{\ell}. (15)

[138] h6: Assumption A.5 (Spectral norm bounds) .

[139] p: Each linear layer W W in the network satisfies

[140] table: ‖ W ‖ op ≤ ω max , \|W\|_{\mathrm{op}}\leq\omega_{\max}, (16)

[141] p: and the architecture (e.g., the number of blocks and hidden dimensions) is finite.

[142] p: Moreover, the DP-aware constraints ensure boundedness along the conditioning pathway. In particular, for each block,

[143] table: ‖ 𝐜 ‖ 2 ≤ c max , \displaystyle\|\mathbf{c}\|_{2}\leq c_{\max}, ‖ γ ‖ ∞ ≤ γ max , \displaystyle\|\gamma\|_{\infty}\leq\gamma_{\max},\, (17) ‖ β ‖ ∞ ≤ β max , \displaystyle\|\beta\|_{\infty}\leq\beta_{\max}, ‖ α ‖ ∞ ≤ α max . \displaystyle\|\alpha\|_{\infty}\leq\alpha_{\max}.

[144] p: Combined with Assumptions A.1 - A.5 , we bound intermediate Jacobians and gradient norms.

[145] h3: A.2 Jacobian Bounds for an AdaLN-Zero Block

[146] p: We consider a single AdaLN-Zero block defined as

[147] table: u = LN ⁡ ( x ) , v = γ ⊙ u + β , h = F ⁡ ( v ) , y = x + α ⊙ h . u=\mathrm{LN}(x),\,v=\gamma\odot u+\beta,\,h=F(v),\,y=x+\alpha\odot h. (18)

[148] p: We follow this sequence of computations to derive Jacobian bounds for the AdaLN-Zero block.

[149] h5: From u u to v v .

[150] p: The Jacobian of v v with respect to u u is

[151] table: ∂ v ∂ u = diag ⁡ ( γ ) , \frac{\partial v}{\partial u}=\mathrm{diag}(\gamma), (19)

[152] p: and therefore

[153] table: ‖ ∂ v ∂ u ‖ op = ‖ γ ‖ ∞ ≤ γ max . \Bigl\|\frac{\partial v}{\partial u}\Bigr\|_{\mathrm{op}}=\|\gamma\|_{\infty}\leq\gamma_{\max}. (20)

[154] h5: From v v to h h .

[155] p: By Assumption A.3 ,

[156] table: ‖ ∂ h ∂ v ‖ op ≤ L F . \Bigl\|\frac{\partial h}{\partial v}\Bigr\|_{\mathrm{op}}\leq L_{F}. (21)

[157] p: Applying the chain rule yields

[158] table: ‖ ∂ h ∂ u ‖ op ≤ L F ​ γ max . \Bigl\|\frac{\partial h}{\partial u}\Bigr\|_{\mathrm{op}}\leq L_{F}\gamma_{\max}. (22)

[159] h5: From x x to y y .

[160] p: We have

[161] table: ∂ y ∂ x = I + diag ⁡ ( α ) ⋅ ∂ h ∂ x . \frac{\partial y}{\partial x}=I+\mathrm{diag}(\alpha)\cdot\frac{\partial h}{\partial x}. (23)

[162] p: Moreover, by the chain rule,

[163] table: ∂ h ∂ x = ∂ h ∂ u ⋅ ∂ u ∂ x , \frac{\partial h}{\partial x}=\frac{\partial h}{\partial u}\cdot\frac{\partial u}{\partial x}, (24)

[164] p: and by Assumption A.2 ,

[165] table: ‖ ∂ u ∂ x ‖ op ≤ L LN . \Bigl\|\frac{\partial u}{\partial x}\Bigr\|_{\mathrm{op}}\leq L_{\mathrm{LN}}. (25)

[166] p: Combining the above bounds and using ‖ α ‖ ∞ ≤ α max \|\alpha\|_{\infty}\leq\alpha_{\max} , we obtain

[167] table: ‖ ∂ y ∂ x ‖ op ≤ 1 + α max ​ L F ​ γ max ​ L LN ≕ C block , \Bigl\|\frac{\partial y}{\partial x}\Bigr\|_{\mathrm{op}}\leq 1+\alpha_{\max}\,L_{F}\,\gamma_{\max}\,L_{\mathrm{LN}}\;\eqqcolon\;C_{\mathrm{block}}, (26)

[168] p: where C block C_{\mathrm{block}} depends only on architecture-dependent constants and DP-aware bounds. Applying the same argument across all blocks yields a global bound on the Jacobian of the full network with respect to its inputs and intermediate states.

[169] h3: A.3 Gradient Bounds by Parameter Groups

[170] p: Let θ \theta denote the collection of all model parameters. For a single example z = ( x , 𝐜 ) z=(x,\mathbf{c}) , define the per-sample gradient as

[171] table: g z ​ ( θ ) = ∇ θ ℓ ​ ( f θ ​ ( x , 𝐜 ) ) . g_{z}(\theta)\;=\;\nabla_{\theta}\ell\!\big(f_{\theta}(x,\mathbf{c})\big). (27)

[172] p: We partition θ \theta into three parameter groups and bound the contribution of each group separately.

[173] h4: Group 1: Parameters in F F

[174] p: Consider a weight matrix W W in F F . Its corresponding gradient can be expressed as

[175] table: ∇ W ℓ = ( α ⊙ ∇ y ℓ ) ⋅ ϕ ​ ( v ) ⊤ , \nabla_{W}\ell=(\alpha\odot\nabla_{y}\ell)\cdot\phi(v)^{\top}, (28)

[176] p: where ϕ ⁡ ( v ) \phi(v) denotes the feature vector derived from v v . By Assumption A.4 and Eq.( 17 ), we obtain

[177] table: ‖ α ⊙ ∇ y ℓ ‖ 2 \displaystyle\|\alpha\odot\nabla_{y}\ell\|_{2} ≤ ‖ α ‖ ∞ ​ ‖ ∇ y ℓ ‖ 2 ≤ α max ​ G ℓ , \displaystyle\leq\|\alpha\|_{\infty}\|\nabla_{y}\ell\|_{2}\leq\alpha_{\max}G_{\ell}, (29) ‖ ϕ ⁡ ( v ) ‖ 2 \displaystyle\|\phi(v)\|_{2} ≤ H max + γ max ​ U max + d ​ β max , \displaystyle\leq H_{\max}+\gamma_{\max}U_{\max}+\sqrt{d}\,\beta_{\max}, (30)

[178] p: where d d is the hidden dimension. Hence,

[179] table: ‖ ∇ W ℓ ‖ F ≤ a α , F ​ α max + a γ , F ​ γ max + a β , F ​ β max , \|\nabla_{W}\ell\|_{F}\leq a_{\alpha,F}\,\alpha_{\max}+a_{\gamma,F}\,\gamma_{\max}+a_{\beta,F}\,\beta_{\max}, (31)

[180] p: for suitable non-negative constants a α , F , a γ , F , a β , F a_{\alpha,F},a_{\gamma,F},a_{\beta,F} . Summing the above bound over all weight matrices W ∈ F W\in F yields an aggregate contribution of the form: a α ​ α max + a γ ​ γ max + a β ​ β max a_{\alpha}\alpha_{\max}+a_{\gamma}\,\gamma_{\max}+a_{\beta}\,\beta_{\max} , where a α , a γ , a β ≥ 0 a_{\alpha},a_{\gamma},a_{\beta}\geq 0 collect the corresponding per-layer constants and depend only on the model architecture. Equivalently, the sensitivity contribution from the parameters within F F scales linearly in ( α max , γ max , β max ) (\alpha_{\max},\gamma_{\max},\beta_{\max}) .

[181] h4: Group 2: Projection layers for ( γ , β , α ) (\gamma,\beta,\alpha)

[182] p: The modulation parameters are obtained from 𝐜 \mathbf{c} via linear projections followed by clipping,

[183] table: γ raw = W γ ​ 𝐜 + b γ , γ = clip ⁡ ( γ raw , γ max ) . \gamma_{\mathrm{raw}}=W_{\gamma}\mathbf{c}+b_{\gamma},\,\gamma=\mathrm{clip}(\gamma_{\mathrm{raw}},\gamma_{\max}). (32)

[184] p: Because coordinate-wise clipping is 1 1 -Lipschitz, it cannot amplify backpropagated gradients; in particular, ‖ ∂ ℓ ∂ γ raw ‖ 2 ≤ ‖ ∂ ℓ ∂ γ ‖ 2 \left\|\frac{\partial\ell}{\partial\gamma_{\mathrm{raw}}}\right\|_{2}\leq\bigl\|\frac{\partial\ell}{\partial\gamma}\bigr\|_{2} . Under the boundedness assumptions in Group 1, the upstream gradient is therefore bounded in norm. Hence,

[185] table: ∇ W γ ℓ = ( ∂ ℓ ∂ γ raw ) ​ 𝐜 ⊤ . \nabla_{W_{\gamma}}\ell=\left(\frac{\partial\ell}{\partial\gamma_{\mathrm{raw}}}\right)\,\mathbf{c}^{\top}. (33)

[186] p: Using ‖ 𝐜 ‖ 2 ≤ c max \|\mathbf{c}\|_{2}\leq c_{\max} , we obtain

[187] table: ‖ ∇ W γ ℓ ‖ F ≤ c γ ​ c max \|\nabla_{W_{\gamma}}\ell\|_{F}\leq c_{\gamma}\,c_{\max} (34)

[188] p: for some constant c γ ≥ 0 c_{\gamma}\geq 0 . Analogous bounds hold for W β W_{\beta} and W α W_{\alpha} . Summing over these projection layers yields a contribution of the form a c ​ c max a_{c}\,c_{\max} , where a c ≥ 0 a_{c}\geq 0 is an architecture-dependent constant.

[189] h4: Group 3: Remaining parameters

[190] p: All remaining parameters (e.g., LayerNorm weights, skip connections) depend only on bounded activations and receive bounded upstream gradients. Consequently, their contribution can be bounded by a constant A 0 ≥ 0 A_{0}\geq 0 that is independent of ( c max , γ max , β max , α max ) (c_{\max},\gamma_{\max},\beta_{\max},\alpha_{\max}) .

[191] h3: A.4 Combining Per-Sample Gradient Bounds

[192] p: Combining the bounds from the three groups yields

[193] table: ‖ g z ​ ( θ ) ‖ 2 ≤ A 0 + a c ​ c max + a γ ​ γ max + a β ​ β max + a α ​ α max . \bigl\|g_{z}(\theta)\bigr\|_{2}\;\leq\;A_{0}+a_{c}c_{\max}+a_{\gamma}\gamma_{\max}+a_{\beta}\beta_{\max}+a_{\alpha}\alpha_{\max}. (35)

[194] p: This matches Proposition 1, where the per-sample gradient bound under the DP-aware constraints is

[195] table: S aware = A 0 + a c ​ c max + a γ ​ γ max + a β ​ β max + a α ​ α max . S_{\mathrm{aware}}=A_{0}+a_{c}c_{\max}+a_{\gamma}\gamma_{\max}+a_{\beta}\beta_{\max}+a_{\alpha}\alpha_{\max}. (36)

[196] h2: Appendix B DP-SGD Sensitivity Comparison

[197] p: In this section, we compare the ℓ 2 \ell_{2} -sensitivity of vanilla DP-SGD and our DP-aware variant. We further introduce a normalized sensitivity ratio, S aware S vanilla ref \tfrac{S_{\mathrm{aware}}}{S_{\mathrm{vanilla}}^{\mathrm{ref}}} , and show that it admits a convex-combination representation.

[198] h5: Vanilla DP-SGD.

[199] p: Given per-sample gradients { g i } i = 1 B \{g_{i}\}_{i=1}^{B} and a clipping threshold C > 0 C>0 , vanilla DP-SGD applies per-sample gradient clipping:

[200] table: g ~ i = g i ⋅ min ⁡ ( 1 , C ‖ g i ‖ 2 ) , q ⁡ ( D ) = 1 B ​ ∑ i = 1 B g ~ i . \tilde{g}_{i}=g_{i}\cdot\min\!\left(1,\frac{C}{\|g_{i}\|_{2}}\right),\,q(D)=\frac{1}{B}\sum_{i=1}^{B}\tilde{g}_{i}. (37)

[201] p: By construction, ‖ g ~ i ‖ 2 ≤ C \|\tilde{g}_{i}\|_{2}\leq C for all i i . Therefore, for any neighboring batches D , D ′ D,D^{\prime} that differ in at most one example, the ℓ 2 \ell_{2} -sensitivity satisfies

[202] table: Δ 2 ​ ( q vanilla ) ≤ C B . \Delta_{2}(q_{\mathrm{vanilla}})\leq\frac{C}{B}. (38)

[203] h5: DP-aware DP-SGD.

[204] p: For the DP-aware model, assume the per-sample gradients are uniformly bounded as ‖ g i ‖ 2 ≤ S aware \|g_{i}\|_{2}\leq S_{\mathrm{aware}} for all i i . If S aware ≤ C S_{\mathrm{aware}}\leq C , clipping is inactive and hence

[205] table: Δ 2 ​ ( q aware ) ≤ S aware B . \Delta_{2}(q_{\mathrm{aware}})\leq\frac{S_{\mathrm{aware}}}{B}. (39)

[206] p: Consequently, the sensitivity ratio

[207] table: ρ = Δ 2 ​ ( q aware ) Δ 2 ​ ( q vanilla ) ≤ S aware C . \rho=\frac{\Delta_{2}(q_{\mathrm{aware}})}{\Delta_{2}(q_{\mathrm{vanilla}})}\leq\frac{S_{\mathrm{aware}}}{C}. (40)

[208] h5: Normalized ratio and convex combination form.

[209] p: To relate S aware S_{\mathrm{aware}} to a representative scale in a standard (non-DP) training run, we introduce non-negative reference magnitudes

[210] table: C ref , Γ ref , B ref , A ref , C_{\mathrm{ref}},\,\Gamma_{\mathrm{ref}},\,B_{\mathrm{ref}},\,A_{\mathrm{ref}}, (41)

[211] p: which summarize typical magnitudes of ‖ 𝐜 ‖ 2 \|\mathbf{c}\|_{2} , | γ | |\gamma| , | β | |\beta| , and | α | |\alpha| , respectively. Using the same architectural constants, define the corresponding reference sensitivity scale

[212] table: S vanilla ref = A 0 + a c ​ C ref + a γ ​ Γ ref + a β ​ B ref + a α ​ A ref . S_{\mathrm{vanilla}}^{\mathrm{ref}}=A_{0}+a_{c}C_{\mathrm{ref}}+a_{\gamma}\Gamma_{\mathrm{ref}}+a_{\beta}B_{\mathrm{ref}}+a_{\alpha}A_{\mathrm{ref}}. (42)

[213] p: Let

[214] table: u 0 = A 0 , \displaystyle u_{0}=A_{0},\, u c = a c ​ C ref , \displaystyle u_{c}=a_{c}C_{\mathrm{ref}}, (43) u γ = a γ ​ Γ ref , u β = \displaystyle u_{\gamma}=a_{\gamma}\Gamma_{\mathrm{ref}},\,u_{\beta}= a β ​ B ref , u α = a α ​ A ref , \displaystyle a_{\beta}B_{\mathrm{ref}},\,u_{\alpha}=a_{\alpha}A_{\mathrm{ref}}, (44)

[215] p: and denote their sum by

[216] table: D = u 0 + u c + u γ + u β + u α = S vanilla ref . D=u_{0}+u_{c}+u_{\gamma}+u_{\beta}+u_{\alpha}=S_{\mathrm{vanilla}}^{\mathrm{ref}}. (45)

[217] p: Define weights

[218] table: λ 0 = u 0 D , λ c = u c D , λ γ = u γ D , λ β = u β D , λ α = u α D , \lambda_{0}=\frac{u_{0}}{D},\,\lambda_{c}=\frac{u_{c}}{D},\,\lambda_{\gamma}=\frac{u_{\gamma}}{D},\,\lambda_{\beta}=\frac{u_{\beta}}{D},\,\lambda_{\alpha}=\frac{u_{\alpha}}{D}, (46)

[219] p: which satisfy λ ⋅ ≥ 0 \lambda_{\cdot}\geq 0 and sum to 1 1 , and define the relative factors

[220] table: r c = c max C ref , r γ = γ max Γ ref , r β = β max B ref , r α = α max A ref . r_{c}=\frac{c_{\max}}{C_{\mathrm{ref}}},\,r_{\gamma}=\frac{\gamma_{\max}}{\Gamma_{\mathrm{ref}}},\,r_{\beta}=\frac{\beta_{\max}}{B_{\mathrm{ref}}},\,r_{\alpha}=\frac{\alpha_{\max}}{A_{\mathrm{ref}}}. (47)

[221] p: We can then rewrite

[222] table: S aware \displaystyle S_{\mathrm{aware}} = A 0 + a c ​ c max + a γ ​ γ max + a β ​ β max + a α ​ α max \displaystyle=A_{0}+a_{c}c_{\max}+a_{\gamma}\gamma_{\max}+a_{\beta}\beta_{\max}+a_{\alpha}\alpha_{\max} (48) = u 0 + u c ​ r c + u γ ​ r γ + u β ​ r β + u α ​ r α . \displaystyle=u_{0}+u_{c}r_{c}+u_{\gamma}r_{\gamma}+u_{\beta}r_{\beta}+u_{\alpha}r_{\alpha}. (49)

[223] p: Dividing both sides by S vanilla ref = D S_{\mathrm{vanilla}}^{\mathrm{ref}}=D yields the convex-combination form:

[224] table: S aware S vanilla ref = λ 0 + λ c ​ r c + λ γ ​ r γ + λ β ​ r β + λ α ​ r α . \frac{S_{\mathrm{aware}}}{S_{\mathrm{vanilla}}^{\mathrm{ref}}}=\lambda_{0}+\lambda_{c}r_{c}+\lambda_{\gamma}r_{\gamma}+\lambda_{\beta}r_{\beta}+\lambda_{\alpha}r_{\alpha}. (50)

[225] p: In particular,

[226] table: S aware S vanilla ref ≤ max ⁡ { 1 , r c , r γ , r β , r α } . \frac{S_{\mathrm{aware}}}{S_{\mathrm{vanilla}}^{\mathrm{ref}}}\leq\max\{1,r_{c},r_{\gamma},r_{\beta},r_{\alpha}\}. (51)

[227] p: If

[228] table: c max ≤ C ref , γ max ≤ Γ ref , β max ≤ B ref , α max ≤ A ref , \displaystyle c_{\max}\leq C_{\mathrm{ref}},\,\gamma_{\max}\leq\Gamma_{\mathrm{ref}},\,\beta_{\max}\leq B_{\mathrm{ref}},\,\alpha_{\max}\leq A_{\mathrm{ref}}, (52)

[229] p: then r c , r γ , r β , r α ≤ 1 r_{c},r_{\gamma},r_{\beta},r_{\alpha}\leq 1 , implying

[230] table: S aware S vanilla ref ≤ 1 . \frac{S_{\mathrm{aware}}}{S_{\mathrm{vanilla}}^{\mathrm{ref}}}\leq 1. (53)

[231] p: Combined with ρ ≤ S aware C \rho\leq\frac{S_{\mathrm{aware}}}{C} , this yields ρ ≤ 1 \rho\leq 1 whenever C C is chosen to be at least the corresponding reference scale.

[232] h2: Appendix C Additional Results on Model Utility

[233] h3: C.1 Per- σ \sigma Results on PrivatePower

[234] figure: Model σ \sigma MAE ↓ \downarrow RMSE ↓ \downarrow MAPE ↓ \downarrow R2 ↑ \uparrow dist_KL ↓ \downarrow dist_JS ↓ \downarrow dist_WS ↓ \downarrow dist_KS ↓ \downarrow MMD ↓ \downarrow Non-DP (no DP) – 0.155 0.208 1.90% 0.861 0.980 0.767 0.605 0.215 1.48e-2 DP-vanilla 0.03 0.430 0.556 4.85% 0.422 1.122 0.736 0.820 0.260 3.90e-2 DP-aware 0.03 0.235 0.296 3.10% 0.741 1.025 0.684 0.700 0.230 2.70e-2 DP-vanilla 0.05 0.448 0.567 5.10% 0.383 1.081 0.643 0.840 0.270 4.80e-2 DP-aware 0.05 0.325 0.423 4.00% 0.603 1.052 0.636 0.810 0.258 4.10e-2 DP-vanilla 0.1 1.280 1.637 12.9% -0.105 1.555 0.833 1.458 0.390 1.90e-1 DP-aware 0.1 0.520 0.671 6.10% 0.353 1.256 0.757 0.982 0.310 9.00e-2 DP-vanilla 0.2 1.310 1.646 13.4% -0.122 1.480 0.794 1.386 0.370 1.70e-1 DP-aware 0.2 1.000 1.262 10.1% 0.052 1.347 0.732 1.205 0.330 1.35e-1 Table 6: Forecasting metrics on PrivatePower across noise multipliers σ \sigma . Lower is better for all metrics except R2.

[235] figure: Model σ \sigma MAE ↓ \downarrow RMSE ↓ \downarrow MAPE ↓ \downarrow R2 ↑ \uparrow dist_KL ↓ \downarrow dist_JS ↓ \downarrow dist_WS ↓ \downarrow dist_KS ↓ \downarrow MMD ↓ \downarrow Non-DP (no DP) – 0.476 0.584 1.17% 0.775 0.900 0.660 0.560 0.190 1.20e-2 DP-vanilla 0.03 2.391 3.034 5.67% -0.950 1.210 0.820 0.760 0.240 3.20e-2 DP-aware 0.03 1.411 1.804 3.54% -0.250 1.030 0.740 0.670 0.220 2.40e-2 DP-vanilla 0.05 3.110 3.498 9.34% -1.400 1.260 0.835 0.790 0.250 3.80e-2 DP-aware 0.05 1.987 2.019 4.97% -0.600 1.090 0.760 0.700 0.230 2.90e-2 DP-vanilla 0.1 4.702 5.787 11.67% -4.100 1.520 0.910 1.080 0.310 9.50e-2 DP-aware 0.1 2.122 2.718 5.27% -1.100 1.280 0.820 0.860 0.260 5.80e-2 DP-vanilla 0.2 5.148 6.812 12.65% -5.200 1.600 0.930 1.250 0.340 1.20e-1 DP-aware 0.2 3.442 4.689 8.41% -2.200 1.430 0.870 1.050 0.300 8.50e-2 Table 7: Interpolation/imputation metrics on PrivatePower across noise multipliers σ \sigma . Lower is better for all metrics except R2.

[236] figure: (a) ECDF of gradient norms at noise multiplier σ = 0.03 \sigma=0.03 (b) CCDF (tail) of gradient norms at noise multiplier σ = 0.03 \sigma=0.03 (c) ECDF of gradient norms at noise multiplier σ = 0.05 \sigma=0.05 (d) CCDF (tail) of gradient norms at noise multiplier σ = 0.05 \sigma=0.05 (e) ECDF of gradient norms at noise multiplier σ = 0.10 \sigma=0.10 (f) CCDF (tail) of gradient norms at noise multiplier σ = 0.10 \sigma=0.10 (g) ECDF of gradient norms at noise multiplier σ = 0.20 \sigma=0.20 (h) CCDF (tail) of gradient norms at noise multiplier σ = 0.20 \sigma=0.20 Figure 3: Gradient distributions under DP training (all σ \sigma settings).

[237] p: This section reports the complete set of metrics of our evaluation scripts on PrivatePower, complementing the representative results shown in the main text. Tables 6 and 7 summarize forecasting and interpolation/imputation performance, respectively. Figure 3 shows the per-example gradient-norm distributions observed during DP-SGD training.

[238] h3: C.2 Results on ETTh1 and ETTm1

[239] figure: Model Interpolation/Imputation Forecasting point_RMSE ↓ \downarrow point_MAPE ↓ \downarrow point_MAE ↓ \downarrow point_RMSE ↓ \downarrow dist_JS ↓ \downarrow temp_spectral_dist ↓ \downarrow Non-DP (no DP) 0.310 2.35% 0.210 0.245 0.610 2.10e-4 DP-vanilla 0.780 5.90% 0.520 0.655 0.880 1.85e-3 DP-aware 0.560 4.10% 0.380 0.465 0.780 9.60e-4 Table 8: Representative metrics on ETTh1 (matched DP mechanism). DP-vanilla and DP-aware are trained under matched DP-SGD settings ( C = 1.0 C=1.0 , noise multiplier σ = 0.1 \sigma=0.1 , batch size B = 96 B=96 , and steps T = 20,000 T=20,000 ).

[240] figure: Model Interpolation/Imputation Forecasting point_RMSE ↓ \downarrow point_MAPE ↓ \downarrow point_MAE ↓ \downarrow point_RMSE ↓ \downarrow dist_WS ↓ \downarrow temp_spectral_dist ↓ \downarrow Non-DP (no DP) 0.355 2.80% 0.240 0.295 0.640 2.60e-4 DP-vanilla 0.945 6.80% 0.625 0.805 0.920 2.15e-3 DP-aware 0.685 4.90% 0.455 0.565 0.820 1.20e-3 Table 9: Representative metrics on ETTm1 (matched DP mechanism). DP-vanilla and DP-aware are trained under matched DP-SGD settings ( C = 1.0 C=1.0 , noise multiplier σ = 0.1 \sigma=0.1 , batch size B = 96 B=96 , and steps T = 20,000 T=20,000 ).

[241] p: We repeat the main comparison on the ETTh1 and ETTm1 datasets. Tables 8 and 9 report representative metrics under matched DP mechanisms. Complete metric tables follow the same format as Table 6 and are omitted for brevity.

[242] h3: C.3 Full Results on Effects of ℬ M ​ ( ⋅ ) \mathcal{B}_{M}(\cdot)

[243] p: Here, we present additional results on the effect of the AdaLN modulation bounding operator ℬ M ​ ( ⋅ ) \mathcal{B}_{M}(\cdot) across tasks and noise levels. As shown in Tables 10 and 11 , comparisons of bounding operators on PrivatePower for forecasting and interpolation/imputation tasks exhibit trends consistent with those in the main text: smooth operators ( tanh \tanh and soft_clamp_band ) achieve comparable performance and consistently outperform hard_clamp and clamp_ste .

[244] figure: σ = 0.05 \sigma=0.05 σ = 0.20 \sigma=0.20 ℬ M ​ ( ⋅ ) \mathcal{B}_{M}(\cdot) point_RMSE ↓ \downarrow dist_JS ↓ \downarrow temp_spec_dist ↓ \downarrow point_RMSE ↓ \downarrow dist_JS ↓ \downarrow temp_spec_dist ↓ \downarrow tanh \tanh (default) 0.423 0.636 8.558e-4 1.262 0.732 1.052e-2 soft_clamp_band 0.425 0.639 8.70e-4 1.270 0.737 1.070e-2 hard_clamp 0.452 0.662 9.45e-4 1.310 0.752 1.120e-2 clamp_ste 0.467 0.674 9.90e-4 1.330 0.760 1.150e-2 Table 10: Bounding-operator comparison on PrivatePower for forecasting under matched DP-SGD. Smooth operators ( tanh \tanh and soft_clamp_band ) perform similarly and outperform hard truncation variants ( hard_clamp and clamp_ste ).

[245] figure: σ = 0.05 \sigma=0.05 σ = 0.20 \sigma=0.20 ℬ M ​ ( ⋅ ) \mathcal{B}_{M}(\cdot) point_RMSE ↓ \downarrow point_MAPE ↓ \downarrow point_MAE ↓ \downarrow point_RMSE ↓ \downarrow point_MAPE ↓ \downarrow point_MAE ↓ \downarrow tanh \tanh (default) 2.019 4.97% 1.987 4.689 8.41% 3.442 soft_clamp_band 2.025 4.99% 1.995 4.710 8.44% 3.460 hard_clamp 2.120 5.22% 2.070 4.860 8.70% 3.560 clamp_ste 2.180 5.35% 2.120 4.950 8.85% 3.620 Table 11: Bounding-operator comparison on PrivatePower for interpolation/imputation under matched DP-SGD. Trends match forecasting: tanh \tanh and soft_clamp_band are consistently better than hard truncation variants.

[246] h2: Appendix D Clipping Behavior under DP

[247] figure: Model σ \sigma p clip ↓ p_{\mathrm{clip}}\downarrow mean( η \eta ) ↑ \uparrow p10( η \eta ) ↑ \uparrow p50( η \eta ) ↑ \uparrow p90( η \eta ) ↑ \uparrow p99( η \eta ) ↑ \uparrow DP-vanilla 0.03 0.561 0.73 0.18 0.86 1.00 1.00 DP-aware 0.03 0.554 0.75 0.22 0.88 1.00 1.00 DP-vanilla 0.05 0.570 0.72 0.16 0.84 1.00 1.00 DP-aware 0.05 0.568 0.73 0.18 0.85 1.00 1.00 DP-vanilla 0.10 0.582 0.71 0.14 0.83 1.00 1.00 DP-aware 0.10 0.578 0.72 0.16 0.84 1.00 1.00 DP-vanilla 0.20 0.589 0.70 0.12 0.82 1.00 1.00 DP-aware 0.20 0.582 0.72 0.15 0.84 1.00 1.00 Table 12: Clipping behaviour under DP-SGD on PrivatePower (matched DP mechanism). We report the clipping activation rate p clip p_{\mathrm{clip}} and summary statistics of the clipping factor η = min ⁡ ( 1 , C ‖ g ‖ 2 ) \eta=\min(1,\frac{C}{\|g\|_{2}}) . Lower p clip p_{\mathrm{clip}} and larger typical η \eta indicate less clipping-induced attenuation.

[248] p: We report additional statistics characterizing the behavior of global per-sample clipping during DP-SGD training. These measurements complement the utility results by illustrating how clipping modifies the update signal. Given a clipping norm C C , we define the clipping activation rate

[249] table: p clip ≔ Pr [ ∥ g i ∥ 2 > C ] , p_{\mathrm{clip}}\coloneqq\Pr\!\big[\|g_{i}\|_{2}>C\big],

[250] p: which we estimate from the per-sample gradients observed during training, as well as the clipping factor

[251] table: η i ≔ min ⁡ ( 1 , C ‖ g i ‖ 2 ) , \eta_{i}\coloneqq\min\!\left(1,\frac{C}{\|g_{i}\|_{2}}\right),

[252] p: whose distribution captures clipping severity, with smaller η i \eta_{i} corresponding to stronger rescaling.

[253] p: Table 12 reports p clip p_{\mathrm{clip}} and summary statistics of η i \eta_{i} for DP-vanilla and DP-aware on PrivatePower across different noise multipliers σ \sigma . For each σ \sigma , we use the same DP mechanism across methods, so any differences reflect the impact of DP-aware bounds on gradient dynamics. Consistent with the main text, we observe comparable p clip p_{\mathrm{clip}} for the two approaches, while DP-aware yields slightly larger lower-quantile and median values of η \eta (i.e., milder rescaling), indicating reduced clipping severity.

[254] p: Furthermore, Figure 4 visualizes the clipping behavior under the clipping threshold C C across all σ \sigma settings. We compare DP-vanilla and DP-aware in terms of the clipping factor η = min ⁡ ( 1 , C ‖ g total ‖ ) \eta=\min(1,\,\frac{C}{\|g_{\mathrm{total}}\|}) and the clipping activation rate p clip = ℙ ⁡ ( ‖ g total ‖ > C ) p_{\mathrm{clip}}=\mathbb{P}(\|g_{\mathrm{total}}\|>C) . Across all noise levels, DP-aware exhibits a clipping frequency and a clipping-factor distribution comparable to DP-vanilla, consistent with the main-text conclusion that the improvements primarily arise from reshaping the gradient tail and reducing the update distortion, rather than from a lower clipping activation rate.

[255] figure: (a) Clipping behavior at noise multiplier σ = 0.03 \sigma=0.03 . (b) Clipping behavior at noise multiplier σ = 0.05 \sigma=0.05 . (c) Clipping behavior at noise multiplier σ = 0.10 \sigma=0.10 . (d) Clipping behavior at noise multiplier σ = 0.20 \sigma=0.20 . Figure 4: Clipping behavior under threshold C C (all σ \sigma settings). We compare DP-vanilla and DP-aware in terms of clipping factor η = min ⁡ ( 1 , C ‖ g total ‖ ) \eta=\min(1,\frac{C}{\|g_{\mathrm{total}}\|}) and clipping activation rate p clip = ℙ ⁡ ( ‖ g total ‖ > C ) p_{\mathrm{clip}}=\mathbb{P}(\|g_{\mathrm{total}}\|>C) .

[256] figure: Setting c max c_{\max} γ max \gamma_{\max} β max \beta_{\max} α max \alpha_{\max} ρ emp \rho_{\text{emp}} point_RMSE ↓ \downarrow dist_JS ↓ \downarrow Loose 1.00 ​ C 0 1.00\,C_{0} 1.00 ​ Γ 0 1.00\,\Gamma_{0} 1.00 ​ B 0 1.00\,B_{0} 1.00 ​ A 0 1.00\,A_{0} 0.92 0.452 0.661 Medium 0.90 ​ C 0 0.90\,C_{0} 0.90 ​ Γ 0 0.90\,\Gamma_{0} 0.90 ​ B 0 0.90\,B_{0} 0.90 ​ A 0 0.90\,A_{0} 0.87 0.423 0.636 Tight 0.75 ​ C 0 0.75\,C_{0} 0.75 ​ Γ 0 0.75\,\Gamma_{0} 0.75 ​ B 0 0.75\,B_{0} 0.75 ​ A 0 0.75\,A_{0} 0.80 0.441 0.651 Too tight 0.50 ​ C 0 0.50\,C_{0} 0.50 ​ Γ 0 0.50\,\Gamma_{0} 0.50 ​ B 0 0.50\,B_{0} 0.50 ​ A 0 0.50\,A_{0} 0.73 0.562 0.750 Table 13: Effect of DP-aware bound tightness on PrivatePower for forecasting. DP-vanilla and all DP-aware variants use a matched DP-SGD mechanism (global clipping norm C = 1.0 C=1.0 , noise multiplier σ = 0.05 \sigma=0.05 , batch size B = 96 B=96 , and training steps T = 20,000 T=20{,}000 ). We scale a base reference setting ( C 0 , Γ 0 , B 0 , A 0 ) (C_{0},\Gamma_{0},B_{0},A_{0}) for DP-aware bounds. We report ρ emp ​ ( p ​ 99 ) \rho_{\text{emp}}(p99) (average-case diagnostic; smaller indicates lighter tails/smaller typical gradients) and forecasting metrics (lower is better). The best performance is highlighted in bold.

[257] figure: Interpolation/Imputation Forecasting Model point_RMSE ↓ \downarrow dist_JS ↓ \downarrow temp_spectral_dist ↓ \downarrow point_RMSE ↓ \downarrow dist_JS ↓ \downarrow temp_spectral_dist ↓ \downarrow Non-DP 0.584 0.66 1.48e-4 0.208 0.77 1.48e-4 + DP-aware ( Loose ) 0.590 0.67 1.52e-4 0.212 0.62 1.55e-4 + DP-aware ( Medium ) 0.583 0.66 1.48e-4 0.207 0.77 1.48e-4 + DP-aware ( Tight ) 0.600 0.68 1.60e-4 0.218 0.63 1.62e-4 + DP-aware ( Too tight ) 0.720 0.78 2.30e-4 0.290 0.75 2.40e-4 Table 14: Expressiveness check on PrivatePower without DP noise. We compare a non-private baseline to non-private DP-aware variants under different tightness settings. Lower is better for all metrics shown. The best performance is highlighted in bold.

[258] h2: Appendix E Additional Ablations

[259] h3: E.1 Effect of Tightness Configurations.

[260] p: We sweep a small set of tightness configurations by scaling a base setting ( C 0 , Γ 0 , B 0 , A 0 ) (C_{0},\Gamma_{0},B_{0},A_{0}) : Loose , Medium , Tight , and Too tight . Here ( C 0 , Γ 0 , B 0 , A 0 ) (C_{0},\Gamma_{0},B_{0},A_{0}) denote reference magnitudes for the conditioning pathway. We select these values via offline diagnostics to avoid trivial saturation while maintaining stable DP training. Table 13 reports (i) the average-case diagnostic ρ emp \rho_{\text{emp}} and (ii) forecasting utility under matched DP hyperparameters. The Medium setting typically performs best, providing sufficient tail control to stabilize DP training without overly restricting the conditioning pathway. As the bounds tighten, ρ emp \rho_{\text{emp}} decreases, reflecting stronger suppression of large gradients. Utility improves up to a point ( Medium ) and then degrades when the bounds become overly restrictive ( Too tight ). This behavior is consistent with the expected trade-off: suppress rare, conditioning-driven spikes without attenuating the conditioning signal.

[261] h3: E.2 Effect of DP-aware Architectural Constraints

[262] p: This section isolates the effect of DP-aware architectural constraints from DP noise by evaluating DP-aware models trained without DP-SGD. We train (i) a non-private baseline and (ii) non-private DP-aware variants with DP-aware bounds enabled, but without per-sample gradient clipping and DP noise injection. We adopt the same tightness configurations as in Section E.1 ( Loose , Medium , Tight , and Too tight ), and keep the architecture, optimizer, and training schedule fixed.

[263] p: Table 14 reports representative metrics on the PrivatePower dataset. Under the Medium configuration, the non-private DP-aware variant matches the non-private baseline across metrics, suggesting that moderate bounds do not materially reduce model expressiveness. In contrast, the Too tight configuration degrades performance, consistent with underfitting induced by overly restrictive bounds. Overall, these results support the interpretation that Medium DP-aware bounds primarily suppress rare conditioning-driven outliers (which is beneficial under DP-SGD), without harming non-private performance.

[264] figure: C C Model ρ emp \rho_{\text{emp}} RMSE ↓ \downarrow dist_JS ↓ \downarrow 0.5 DP-vanilla 1.00 2.726 0.978 0.5 DP-aware 0.87 1.145 0.826 1.0 DP-vanilla 1.00 1.673 0.833 1.0 DP-aware 0.89 0.671 0.757 2.0 DP-vanilla 1.00 1.344 0.787 2.0 DP-aware 0.89 0.446 0.664 Table 15: Effect of clipping threshold C C on PrivatePower for forecasting at σ = 0.1 \sigma=0.1 . All rows use a matched DP mechanism for each C C (same σ \sigma , B B , and T T ); only C C changes. DP-aware consistently outperforms DP-vanilla across a range of C C values.

[265] h3: E.3 Effect of Clipping Threshold

[266] p: We also study the effect of the clipping threshold C C in DP-SGD. Table 15 reports representative forecasting metrics and the empirical diagnostic ρ emp \rho_{\text{emp}} for several values of C C under a matched DP mechanism. We find that increasing C C consistently improves utility: as C C grows, both RMSE and dist_JS decrease for DP-vanilla and DP-aware, indicating better forecasting utility and a closer predictive distribution to the reference. Meanwhile, ρ emp \rho_{\text{emp}} remains at 1.00 1.00 for DP-vanilla and stays stable around 0.87 − 0.89 0.87-0.89 for DP-aware. Across a wide range of C C , DP-aware consistently outperforms DP-vanilla.

[267] h3: E.4 Effects of Interpolation/Imputation Metrics

[268] p: Table 16 mirrors the forecasting tightness ablation in the main text, but reports interpolation/imputation metrics. All rows use a matched DP mechanism; we vary only the DP-aware bound tightness. The same “sweet spot” persists for interpolation: moderately tight bounds improve utility, whereas overly restrictive bounds lead to underfitting. Table 17 extends the component-wise ablation to interpolation/imputation. Each row uses the same DP mechanism; only the inclusion of the two DP-aware components differs.

[269] figure: Setting ρ emp \rho_{\text{emp}} RMSE ↓ \downarrow MAE ↓ \downarrow Loose 0.92 2.231 2.170 Medium 0.87 2.019 1.987 Tight 0.80 2.672 2.246 Too tight 0.73 3.626 3.179 Table 16: Effect of DP-aware bound tightness on PrivatePower for interpolation/imputation at σ = 0.05 \sigma=0.05 under a matched DP mechanism. We report ρ emp \rho_{\text{emp}} and representative interpolation metrics (lower is better); boldface denotes the best performance.

[270] figure: Model variant ρ emp \rho_{\text{emp}} RMSE ↓ \downarrow MAE ↓ \downarrow DP-vanilla 1.00 3.498 3.110 DP-aware (only 𝐜 \mathbf{c} bounded) 0.95 3.998 3.070 DP-aware (only AdaLN bounded) 0.93 2.337 2.112 DP-aware (full, ours) 0.89 2.019 1.987 Table 17: Effects of forward-pass control components on PrivatePower for interpolation/imputation at σ = 0.05 \sigma=0.05 . All rows use a matched DP mechanism. We report the empirical diagnostic ρ emp \rho_{\text{emp}} and representative interpolation metrics (lower is better). Boldface indicates the best performance.

[271] h2: Appendix F Additional Training-Time Signals

[272] p: This section reports additional training-time signals under DP-SGD, including: (i) training-loss trajectories across noise multipliers and (ii) representative wall-clock step time. All results are evaluated on PrivatePower using the same optimizer and training schedule as in the main experiments.

[273] h3: F.1 Training Loss across Noise Multipliers

[274] figure: (a) Training MSE loss ( σ = 0.03 \sigma=0.03 ). (b) Training MSE loss ( σ = 0.05 \sigma=0.05 ). (c) Training MSE loss ( σ = 0.1 \sigma=0.1 ). (d) Training MSE loss ( σ = 0.2 \sigma=0.2 ). Figure 5: Training loss dynamics on PrivatePower. Training MSE loss curves for Non-DP, DP-vanilla, and DP-aware under several DP noise multipliers. Larger σ \sigma yields a higher loss floor, while DP-aware closely follows DP-vanilla across noise levels.

[275] p: Figure 5 plots the evolution of the training MSE loss over optimization steps for Non-DP, DP-vanilla, and DP-aware runs under several noise multipliers σ ∈ { 0.03 , 0.05 , 0.1 , 0.2 } \sigma\in\{0.03,0.05,0.1,0.2\} . As expected, increasing the DP noise scale raises the asymptotic loss, with larger σ \sigma leading to a higher steady-state loss floor. Across all noise settings, DP-aware tracks DP-vanilla closely, suggesting that our proposed architectural constraints do not adversely affect optimization or training stability. In contrast, the Non-DP baseline attains the lowest final loss, consistent with the absence of gradient clipping effects and DP noise.

[276] h3: F.2 Runtime: Step Time under DP Training

[277] p: We additionally report an average per-step wall-clock time comparison over 5 runs. Table 18 summarizes robust statistics of the step time.

[278] figure: Method mean ↓ \downarrow p50 ↓ \downarrow p90 ↓ \downarrow rel. to Non-DP Non-DP 0.100 0.047 0.201 1.00 × \times DP-vanilla 0.168 0.105 0.350 1.68 × \times DP-aware 0.169 0.108 0.351 1.69 × \times Table 18: Runtime summary. Robust statistics of per-step wall-clock time for Non-DP, DP-vanilla, and DP-aware training.

[279] h2: Appendix G Details for Datasets and Mask-Based Tasks

[280] p: Table 19 provides the configurations of the datasets and their corresponding mask-based tasks.

[281] figure: Dataset Records Channels Seq Len Train/Val/Test Normalization ratio_range pred_len_range num_blocks_range PrivatePower ≈ \approx 23.1k 7 168 70%/15%/15% per-channel standardization [0.1, 0.5] [24, 96] [4, 8] ETTh1 ≈ \approx 17.5k 7 96 12m/4m/4m per-feature z-score [0.1, 0.5] [24, 96] [4, 8] ETTm1 ≈ \approx 70k 7 96 12m/4m/4m per-feature z-score [0.1, 0.5] [24, 96] [4, 8] Table 19: Configurations of the datasets and their corresponding mask-based tasks. Each dataset trains a single conditional diffusion model that supports interpolation/imputation (random & stride masks), forecasting (block masks), and full-sequence reconstruction. For PrivatePower, we follow the private-data pipeline in our codebase; for ETTh1 and ETTm1, we follow the common ETT setting.

[282] h5: PrivatePower.

[283] p: PrivatePower contains 23,136 23{,}136 records with 7 7 channels. We use ( K max , L max ) = ( 7,168 ) (K_{\max},L_{\max})=(7,168) , split the data chronologically into train/validation/test ( 70 / 15 / 15 70/15/15 ), and apply per-channel standardization using training-split statistics (mean and standard deviation). The raw timestamp-indexed hourly power_usage series (single meter) is preprocessed via an internal pipeline: (i) replace negative values by interpolation using a 7 7 -day moving-average baseline, and (ii) add calendar and temporal covariates derived from timestamps, followed by (iii) the above normalization. Training windows are constructed using a sliding window of length 168 168 with stride 24 24 . For mask-based tasks, we use the ranges in Table 19 : ratio_range [ 0.1 , 0.5 ] [0.1,0.5] , pred_len_range [ 24 , 96 ] [24,96] , and num_blocks_range [ 4 , 8 ] [4,8] . We train a conditional diffusion model with 1000 1000 diffusion steps (linear β \beta schedule) and a Transformer backbone (depth 8 8 , hidden size 256 256 , 8 8 attention heads), using AdamW with learning rate 7 × 10 − 4 7\times 10^{-4} , weight decay 2 × 10 − 5 2\times 10^{-5} , batch size 96 96 , EMA decay 0.999 0.999 , for 20 20 k optimization steps.

[284] h5: ETTh and ETTm1.

[285] p: ETTh1 (hourly; ≈ \approx 17.5k records) and ETTm1 ( 15 15 -minute; ≈ \approx 70k records) are public ETT benchmarks ( Zhou et al., 2021 ) . Both datasets have 7 7 channels, and we use sequence length L max = 96 L_{\max}=96 with K max = 7 K_{\max}=7 to match the standard ETT window. We follow the standard chronological split ( 12 / 4 / 4 12/4/4 months for train/validation/test) and apply per-feature z z -score normalization using training statistics. For mask-based tasks, we use the same ranges as in Table 19 : ratio_range [ 0.1 , 0.5 ] [0.1,0.5] , pred_len_range [ 24 , 96 ] [24,96] , and num_blocks_range [ 4 , 8 ] [4,8] . For imputation-oriented masks, we use length- 96 96 windows to align with common ETT evaluation practice ( Cao et al., 2024 ) . We train one model per dataset from scratch, using the same model family and optimizer settings as for PrivatePower for a controlled comparison. To account for the larger number of available windows in ETTm1, we fix the total number of optimization steps and use random window sampling to provide training diversity.

[286] h2: Instructions for reporting errors

[287] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[288] p: Tip: You can select the relevant text first, to include it in your report.

[289] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[290] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
