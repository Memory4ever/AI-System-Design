[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: SPARSITY INDUCTION FOR ACCURATE POST-TRAINING PRUNING OF LARGE LANGUAGE MODELS

[3] h6: Abstract

[4] p: Large language models have demonstrated capabilities in text generation, while their increasing parameter scales present challenges in computational and memory efficiency. Post-training sparsity (PTS), which reduces model cost by removing weights from dense networks, is an effective approach. However, native dense matrices lack high sparsity, making existing approaches that directly remove weights disrupt model states, resulting in unsatisfactory performance recovery even with post-tuning. We propose Sparsity Induction, which promotes models toward higher sparsity at both distribution and feature levels before pruning, to push the limits of PTS. At the distribution level, we enhance distributional sparsity through mathematically equivalent scaling transformations, which are fully absorbable and incur no extra parameters or inference-time overhead. At the feature level, we introduce Spectral Norm Loss to promote feature sparsity from a low-rank perspective. Experiments across diverse model architectures and tasks demonstrate that our method further enhances sparsity-friendliness, achieving superior pruning performance over existing approaches.

[5] h6: Index Terms:

[6] figure: Figure 1 : Top: Importance distributions before (left) and after (right) Sparsity Induction . SI sharpens the landscape by boosting salient channels and suppressing background mass, enlarging the gap between important and unimportant weights and yielding a more sparsity-friendly distribution. Bottom: We attach lightweight channel-wise scalers s s to Attention and FFN; backbone weights are frozen and only s s are trained. Dashed modules are merged back after training, introducing no extra modules or inference-time overhead.

[7] h2: 1 Introduction

[8] p: Large Language Models (LLMs), such as the GPT series [ 1 ] and the DeepSeek series [ 10 , 9 ] , have achieved strong performance in language understanding and generation across diverse tasks. However, state-of-the-art LLMs typically contain tens to hundreds of billions of parameters, incurring substantial computational costs, high latency, and significant energy usage, which hinders deployment in both data centers and resource-constrained environments. Therefore, there is a pressing need for model compression methods that substantially improve inference efficiency while preserving accuracy.

[9] p: Mainstream compression routes comprise pruning, quantization [ 19 , 25 , 8 ] , and knowledge distillation [ 21 , 22 ] . Sparsifying LLMs is commonly discussed in terms of granularity: unstructured weight sparsity, structured patterns such as N:M [ 15 ] or block sparsity, and pruning at the level of channels [ 12 ] , attention heads [ 11 ] , or entire layers [ 17 ] . The latter two typically alter network topology and tensor shapes, making them more intrusive to training and deployment pipelines and often necessitating substantial retraining to recover accuracy. By contrast, Post-training Sparsity (PTS ), tends to use unstructured removal to avoid heavy retraining; it can also be combined with N:M semi-structured to obtain hardware-friendly patterns with only limited calibration and lightweight compensation, thereby delivering inference speedups and memory savings at modest overhead.

[10] p: Post-training sparsity (PTS) originally relied on magnitude pruning [ 6 ] , which ranks parameters by their absolute values and zeros out small weights. This rule is easy to implement and has long served as a reference baseline for high sparsity, but in large-scale models the long-tailed magnitude distribution and inter-channel scale imbalance make a purely magnitude-based criterion prone to mispruning critical features and causing noticeable performance degradation. To mitigate this, SparseGPT [ 7 ] estimates loss sensitivity with a diagonal Hessian approximation under a no-retraining setting and applies row-wise compensation to redistribute the removed information to retained weights, which can greatly reduce accuracy loss even at around fifty percent sparsity. Wanda [ 20 ] further introduces the L2 norm of input activations as a data-aware criterion, yielding more robust pruning decisions at very low additional cost. Recent work [ 5 , 4 ] has broadened the sources and combinations of auxiliary signals and leveraged symbolic regression to automatically search importance expressions over weights and activations, aiming for stable recovery at higher sparsity levels. Nevertheless, the returns from merely strengthening importance scores have become marginal, indicating that post-training sparsity should be reconsidered from more fundamental perspectives such as preserving distributional and scaling consistency.

[11] p: Across existing post-training sparsity methods, pushing for ever more refined importance scores exhibits diminishing returns. These scores are typically built on local approximations or limited calibration data; improvements increasingly yield marginal re-ranking, while the added computation and tuning accumulate and fail to translate into stable accuracy gains at large scale and high sparsity. As shown by the left panel of Fig. 1 (top), the baseline importance landscape indicates that the raw weight distribution is not inherently sparse; naive pruning therefore removes useful mass and perturbs activations. More fundamentally, pruning disrupts the self-consistent distributional and scaling structure established during training, including the statistical shape of weights and the relative scales across channels. The resulting imbalance propagates through attention and feed-forward paths and emerges as the primary driver of accuracy loss in post-training sparsity. Merely refining importance scores cannot remedy this distributional damage. A more promising direction is to preserve or rapidly recalibrate distribution and scale consistency before and after pruning, retaining the low-overhead nature of post-training sparsity while suppressing error amplification at high sparsity levels.

[12] p: We introduce the central idea of Sparsity Induction (SI): before pruning, we proactively shape the model’s weight distribution and feature structure to make it more sparsity-friendly, thereby improving the accuracy and stability of PTS without adding inference overhead. To instantiate this idea, we apply absorbable, mathematically equivalent scaling transformations at the distributional level, using a few learnable scale factors to align channel/head statistics and folding them entirely into the parameters at inference; at the feature level, we add a spectral-norm loss to encourage low-rank structure and promote feature sparsity. We further devise an efficient optimization framework that jointly updates standard importance scores and scaling factors, yielding up to 20× speedup over conventional pipelines. Extensive experiments across architectures and tasks show that SI markedly strengthens sparsity-friendliness and consistently surpasses existing approaches in pruning performance.

[13] p: Our contributions can be summarized as follows:

[14] p: · We introduce the concept of sparsity induction, which enforces sparsity in the original model before pruning.

[15] p: · We design a sparsity induction framework that optimizes sparsity properties from both distributional and feature-level perspectives.

[16] p: · Extensive experiments demonstrate that our approach substantially enhances sparsity-friendliness and significantly improves pruning performance.

[17] h2: 2 METHODOLOGY

[18] h3: 2.1 Preliminaries

[19] p: Most pruning pipelines construct a binary mask according to a sparsity metric and a target sparsity level, and obtain a pruned weight matrix by zeroing the masked entries. Let 𝐖 ∈ ℝ d out × d in \mathbf{W}\in\mathbb{R}^{d_{\mathrm{out}}\times d_{\mathrm{in}}} denote a dense weight matrix and 𝐌 ∈ { 0 , 1 } d out × d in \mathbf{M}\in\{0,1\}^{d_{\mathrm{out}}\times d_{\mathrm{in}}} the pruning mask; the pruned weights are given as follows,

[20] table: 𝐖 ^ = 𝐖 ⊙ 𝐌 ​ , \widehat{\mathbf{W}}=\mathbf{W}\odot\mathbf{M}\text{,} (1)

[21] p: where ⊙ \odot denotes the Hadamard product. For an input vector x ∈ ℝ d in x\in\mathbb{R}^{d_{\mathrm{in}}} , the output distortion induced by pruning is given as follows,

[22] table: Δ ​ Y \displaystyle\Delta Y = ( 𝐖 − 𝐖 ^ ) ​ X ​ , \displaystyle=(\mathbf{W}-\widehat{\mathbf{W}})\,X\text{,} (2)

[23] p: where Δ ​ Y \Delta Y denotes the pruning-induced output distortion.

[24] p: Existing methods primarily focus on designing effective metrics so that the induced mask 𝐌 \mathbf{M} minimizes such distortion. However, the original dense weight matrices in LLMs typically do not exhibit substantial natural sparsity. In this setting, the pruned model 𝐖 ^ \widehat{\mathbf{W}} is a strict subset (hard-masked version) of 𝐖 \mathbf{W} ; without adapting the weight distribution or the feature responses, naïve hard masking often yields nontrivial performance degradation.

[25] p: In this work, we induce sparsity adaptively from two complementary perspectives, distributional and feature, to prepare the model for pruning: (i) we reshape the weight distribution to enhance separability between important and unimportant parameters; and (ii) we learn masks under feature-aware objectives that directly penalize output distortion. This dual guidance sparsifiable structure and improves the performance of the sparse model.

[26] h3: 2.2 Sparsity Induction: Distributions

[27] p: We aim to perform sparsity induction so that, prior to pruning, the weight distribution is pre-adapted to the accuracy degradation induced by metric-based pruning, thereby effectively enhancing sparsity. However, for high-dimensional LLMs it is difficult to determine the correct direction of distributional optimization by mere inspection, while full-parameter fine-tuning is prohibitively resource-intensive. To achieve precise yet efficient control, we introduce a functionally equivalent reparameterization based on channel-wise scaling and channel-wise shifting, which reshapes the weight distributions without altering model functionality.This equivalent transformation can be applied to both the linear layer and attention operation.

[28] p: Linear layer. To reshape weight statistics without changing functionality, we introduce per-channel scaling 𝒔 > 0 \bm{s}>0 and per-channel shifting 𝜹 \bm{\delta} , and let 𝐒 \mathbf{S} be the diagonal matrix of 𝒔 \bm{s} (i.e., 𝐒 = diag ⁡ ( 𝒔 ) \mathbf{S}=\mathrm{diag}(\bm{s}) ). For a linear layer 𝐘 = 𝐖𝐗 + 𝐛 \mathbf{Y}=\mathbf{W}\mathbf{X}+\mathbf{b} , with per-channel scale 𝒔 > 0 \bm{s}>0 , shift 𝜹 \bm{\delta} , and 𝐒 = diag ⁡ ( 𝒔 ) \mathbf{S}=\mathrm{diag}(\bm{s}) , we can therefore express the equivalent reparameterization as follows,

[29] table: 𝐘 = 𝐖𝐗 + 𝐛 = 𝐒 − 1 ​ ( 𝐗 − 𝜹 ) ⏟ 𝐗 ~ ​ ( 𝐖𝐒 ) ⏟ 𝐖 ~ + ( 𝐛 + 𝐖 ​ 𝜹 ) ⏟ 𝐛 ~ ​ , \mathbf{Y}\;=\;\mathbf{W}\mathbf{X}+\mathbf{b}\;=\;\underbrace{\mathbf{S}^{-1}(\mathbf{X}-\bm{\delta})}_{\tilde{\mathbf{X}}}\;\underbrace{(\mathbf{W}\mathbf{S})}_{\tilde{\mathbf{W}}}\;+\;\underbrace{(\mathbf{b}+\mathbf{W}\bm{\delta})}_{\tilde{\mathbf{b}}}\text{,} (3)

[30] p: where 𝐗 ~ = 𝐒 − 1 ​ ( 𝐗 − 𝜹 ) \tilde{\mathbf{X}}=\mathbf{S}^{-1}(\mathbf{X}-\bm{\delta}) , 𝐖 ~ = 𝐖𝐒 \tilde{\mathbf{W}}=\mathbf{W}\mathbf{S} , and 𝐛 ~ = 𝐛 + 𝐖 ​ 𝜹 \tilde{\mathbf{b}}=\mathbf{b}+\mathbf{W}\bm{\delta} ; 𝐒 = diag ⁡ ( 𝒔 ) \mathbf{S}=\mathrm{diag}(\bm{s}) is a diagonal matrix, and 𝐖 \mathbf{W} is the (dense) weight matrix.

[31] p: Attention. To keep attention logits intact (thus preserving the softmax attention and outputs), we apply a pair of inverse per-channel scalings to queries and keys: with 𝒔 a > 0 \bm{s}_{a}>0 and 𝐒 a = diag ⁡ ( 𝒔 a ) \mathbf{S}_{a}=\mathrm{diag}(\bm{s}_{a}) , set 𝐐 ~ = 𝐐𝐒 a \tilde{\mathbf{Q}}=\mathbf{Q}\mathbf{S}_{a} and 𝐊 ~ = 𝐊𝐒 a − 1 \tilde{\mathbf{K}}=\mathbf{K}\mathbf{S}_{a}^{-1} ; then 𝐐 ~ ​ 𝐊 ~ ⊤ = 𝐐𝐊 ⊤ \tilde{\mathbf{Q}}\tilde{\mathbf{K}}^{\top}=\mathbf{Q}\mathbf{K}^{\top} . The factors can be absorbed into the 𝐐 / 𝐊 \mathbf{Q}/\mathbf{K} projection weights, reshaping their distributions without altering functionality.

[32] p: Lightweight objective. We learn only a small set of transformation parameters on calibration data (e.g., 𝒔 , 𝜹 \bm{s},\bm{\delta} for linear layers and 𝒔 a \bm{s}_{a} for attention) using a lightweight objective that pre-adapts the model to the mask. Accordingly, the optimization objective is given as follows,

[33] table: min Θ ⁡ 𝔼 𝐗 ​ ‖ ( 𝐖 ~ − 𝐖 ~ ⊙ 𝐌 ) ​ 𝐗 ~ ‖ 2 2 , Θ = { 𝒔 , 𝜹 , 𝒔 a } ​ , \min_{\Theta}\ \mathbb{E}_{\mathbf{X}}\,\|(\tilde{\mathbf{W}}-\tilde{\mathbf{W}}\odot\mathbf{M})\tilde{\mathbf{X}}\|_{2}^{2},\qquad\Theta=\{\bm{s},\bm{\delta},\bm{s}_{a}\}\text{,} (4)

[34] p: where Θ \Theta denotes the transformation parameters, 𝐌 \mathbf{M} is a binary mask meeting the target sparsity, and 𝐖 ~ \tilde{\mathbf{W}} and x ~ \tilde{x} follow the definitions above, as shown in the bottom panel of Fig. 1 . This avoids full-parameter fine-tuning while improving mask-friendliness.

[35] h3: 2.3 Sparsity Induction: Features

[36] p: After the distributional reparameterization, optimization at the feature level may still lack a stable and well-defined search direction. We address this by combining a data-driven initialization of the transformation factors with a spectral-style guidance term so as to obtain faster and more reliable convergence while keeping the number of trainable parameters small. Concretely, we construct a robust channel-wise initialization as follows, Let X = { 𝐱 j } j = 1 n X=\{\mathbf{x}_{j}\}_{j=1}^{n} denote the calibration set and 𝐲 j = 𝐖𝐱 j \mathbf{y}_{j}=\mathbf{W}\mathbf{x}_{j} the pre-transform outputs of a layer. For output channel i i , define the robust statistics m i = median j ⁡ 𝐲 j , i m_{i}=\operatorname{median}_{j}\,\mathbf{y}_{j,i} and μ i = 1 n ​ ∑ j = 1 n 𝐲 j , i \mu_{i}=\tfrac{1}{n}\sum_{j=1}^{n}\mathbf{y}_{j,i} ; we then set

[37] table: s i ( 0 ) = ( m i − g ⁡ ( μ i ) ) 2 ​ , s_{i}^{(0)}=\bigl(m_{i}-g(\mu_{i})\bigr)^{2}\text{,} (5)

[38] p: where g : ℝ → ℝ g:\mathbb{R}\!\to\!\mathbb{R} is a fixed monotone mapping (e.g., identity or simple rescaling), and s i ( 0 ) s_{i}^{(0)} denotes the initial per-channel scale.

[39] p: On top of this initialization, we optimize only the transformation factors using an output-matching loss combined with a spectral-style regularizer; the objective is defined as follows,

[40] table: ℒ total = ℒ MSE + λ ​ ℛ p ​ , \mathcal{L}_{\text{total}}=\mathcal{L}_{\text{MSE}}+\lambda\,\mathcal{R}_{p}\text{,} (6)

[41] table: ℒ MSE = MSE ⁡ ( 𝐘 d , 𝐘 s ) ​ , \mathcal{L}_{\text{MSE}}=\operatorname{MSE}\!\bigl(\mathbf{Y}^{\mathrm{d}},\,\mathbf{Y}^{\mathrm{s}}\bigr)\text{,} (7)

[42] table: ℛ p = exp ( − α ∑ ℓ ∈ 𝒮 ∥ 𝐖 ℓ ∥ p ) , \mathcal{R}_{p}=\exp\!\Bigl(-\alpha\sum_{\ell\in\mathcal{S}}\|\mathbf{W}_{\ell}\|_{p}\Bigr)\text{,} (8)

[43] p: where 𝐘 d \mathbf{Y}^{\mathrm{d}} and 𝐘 s \mathbf{Y}^{\mathrm{s}} denote the dense and sparsity-induced batched outputs, respectively; λ > 0 \lambda>0 balances reconstruction and regularization; α > 0 \alpha>0 controls the regularizer strength; p ≥ 1 p\!\geq\!1 is the norm order; 𝒮 \mathcal{S} indexes the set of layers subject to sparsity induction; and 𝐖 ℓ \mathbf{W}_{\ell} is the weight matrix of layer ℓ \ell . The combination of robust initialization and spectral guidance narrows the search space, stabilizes feature-level updates, and improves pruning accuracy at a fixed sparsity without resorting to full-parameter fine-tuning.

[44] h3: 2.4 Efficiency: Fast Hessian Update

[45] p: We avoid repeated forwards by replacing activation variance with a diagonal Gauss–Newton/Hessian proxy for a linear layer y = 𝐖𝐗 + 𝐛 y=\mathbf{W}\mathbf{X}+\mathbf{b} ; the proxy is defined as follows,

[46] table: 𝐇 ∝ Σ 𝐗 ≜ 𝔼 ⁡ [ 𝐗𝐗 ⊤ ] ​ , \mathbf{H}\ \propto\ {\Sigma}_{\mathbf{X}}\ \triangleq\ \mathbb{E}[\mathbf{X}\mathbf{X}^{\top}]\text{,} (9)

[47] p: where 𝐇 \mathbf{H} serves as a curvature proxy and is diagonal up to a positive layer-wise constant, and 𝚺 𝐗 \bm{\Sigma}_{\mathbf{X}} denotes the input covariance.

[48] p: When distributional scaling is folded into parameters at inference, with 𝐗 ′ = 𝐃𝐗 \mathbf{X}^{\prime}=\mathbf{D}\mathbf{X} and 𝐃 = Diag ⁡ ( 𝒔 ) \mathbf{D}=\mathrm{Diag}(\bm{s}) , the proxy transforms as follows,

[49] table: 𝐇 ′ ∝ 𝐃 ​ 𝐇 ​ 𝐃 ⟹ diag ⁡ ( 𝐇 ′ ) = 𝒔 2 ∘ diag ⁡ ( 𝐇 ) ​ , \mathbf{H}^{\prime}\ \propto\ \mathbf{D}\,\mathbf{H}\,\mathbf{D}\quad\Longrightarrow\quad\mathrm{diag}(\mathbf{H}^{\prime})\ =\ \bm{s}^{2}\!\circ\mathrm{diag}(\mathbf{H})\text{,} (10)

[50] p: where 𝒔 ∈ ℝ d in \bm{s}\in\mathbb{R}^{d_{\text{in}}} is the absorbable per-channel scaling vector, 𝐃 = Diag ⁡ ( 𝒔 ) \mathbf{D}=\mathrm{Diag}(\bm{s}) is its diagonal embedding, and ∘ \circ denotes the Hadamard product.

[51] p: Substituting the proxy gives the constant-time refreshable score as follows,

[52] table: m fast ​ ( 𝐖 ) ≜ | 𝐖 | ∘ diag ⁡ ( 𝐇 ′ ) ∝ | 𝐖 | ∘ ( diag ⁡ ( 𝐇 ) ∘ 𝒔 ) ​ , m_{\mathrm{fast}}(\mathbf{W})\ \triangleq\ |\mathbf{W}|\circ\sqrt{\mathrm{diag}(\mathbf{H}^{\prime})}\ \propto\ |\mathbf{W}|\circ\bigl(\sqrt{\mathrm{diag}(\mathbf{H})}\circ\bm{s}\bigr)\text{,} (11)

[53] p: where | ⋅ | |\cdot| and diag ⁡ ( ⋅ ) \mathrm{diag}(\cdot) denote the elementwise absolute value and diagonal extraction, respectively. By ( 10 ), m fast ​ ( 𝐖 ) m_{\mathrm{fast}}(\mathbf{W}) induces the same ordering as the classical Wanda metric evaluated on the scaled input 𝐗 ′ = 𝐃𝐗 \mathbf{X}^{\prime}=\mathbf{D}\mathbf{X} up to a positive layer-wise constant, thus preserving rankings while enabling O ⁡ ( d in ) O(d_{\text{in}}) refresh via cached diagonals. This algorithmic design greatly accelerates our overall method.

[54] h2: 3 EXPERIMENTS

[55] h3: 3.1 Experiment Setup

[56] p: Models, Datasets, and Evaluations We evaluate eight decoder-only LLMs that jointly cover size and architectural style: OPT–125M/350M/1.3B/2.7B [ 27 ] and LLaMA-1/2 [ 23 , 24 ] at 7B and 13B. This set spans the bias-heavy OPT family and the largely bias-light LLaMA family, enabling representative comparisons across structures and capacities. For language modeling, we report perplexity on the C4 [ 16 ] and WikiText-2 [ 13 ] validation sets. To assess downstream generalization, we measure zero-shot accuracy with EleutherAI LM Harness on six tasks: ARC-Easy, ARC-Challenge [ 3 ] , HellaSwag [ 26 ] , BoolQ [ 2 ] , Winogrande [ 18 ] , and OpenBookQA [ 14 ] . Results are compared against the dense models and against pruning baselines under identical tokenization, prompts, and scoring; calibration data are disjoint from all evaluation sets.

[57] p: Details. Pruning is applied to the linear layers in attention and MLP blocks; embeddings and the final LM head remain dense, and biases are not pruned. We compare three post-training sparsification baselines—Magnitude, Wanda, and SparseGPT—and employ a plug-and-play sparsity-induction step compatible with each baseline to stabilize the selected masks/thresholds. Following prior work, we use exactly 128 activation samples (2048-token segments from the C4 training set), shared across all models and methods. All experiments use PyTorch and HuggingFace Transformers with LM Harness on a single NVIDIA RTX A6000 (48 GB). Baseline pruning is one-shot without task-specific fine-tuning; the induction stage performs a short 1–5 epoch pass on the 128 samples. We use a maximum context length of 2048 tokens and adjust batch sizes to fit memory.

[58] h3: 3.2 Experiment Results and Analysis

[59] p: Table 1 reports perplexity for both dense and sparse models, with and without SI augmentation. SI systematically mitigates the perplexity degradation introduced by pruning, with the largest gains under aggressive sparsity where baseline sparse models otherwise suffer severe quality loss or become practically unusable.

[60] p: Table 2 summarizes the average zero-shot performance of dense models and their pruned counterparts across six benchmarks.Across multiple sparsity regimes, adding Sparsity Induction (SI) consistently improves the zero-shot accuracy of one-shot pruning baselines, including magnitude pruning, Wanda, and SparseGPT.

[61] p: Although SI is not explicitly tailored to N:M semi-structured sparsity, it nevertheless delivers strong results under such patterns. Because SI’s auxiliary parameters can be folded into the weight matrices before inference, it introduces no additional runtime modules or overhead. Consequently, models equipped with SI remain fully compatible with hardware acceleration for N:M sparsity and can be deployed for speedups without modification.

[62] p: As summarized in Table 3 , our fast Hessian update reduces the Wanda refresh time on LLaMA-7B (batch size = 1 =1 ) from 345.91 345.91 s to 15.27 15.27 s, a 22.65 × 22.65\times improvement. For end-to-end latency under the 2 : 4 2{:}4 sparsity pattern (Table 4 ), we observe 251 251 ms versus 312 312 ms on LLaMA-7B ( 1.24 × 1.24\times speedup). Because SI is fully absorbable, it introduces no additional runtime overhead relative to Wanda or SparseGPT.

[63] figure: Table 1 : Perplexity ↓ \downarrow on the WikiText-2 dataset for OPT and LLaMA-1 models. Bold indicates the lowest PPL within each (Sparsity, Model) block. Abbrev.: SI = Sparsity Induction ; rows marked “ +SI ” mean the base method + SI. OPT LLaMA-1 Sparsity Method 125M 350M 1.3B 2.7B 7B 13B 0% Dense 27.65 22.00 14.62 12.47 5.68 5.09 50% Magnitude 193.36 97.78 1712.82 265.21 17.28 20.21 +SI (Ours) 52.85 49.55 26.39 18.86 12.08 18.45 Wanda 38.99 36.19 18.40 14.22 7.26 6.15 +SI (Ours) 38.00 34.78 18.27 14.19 7.04 6.04 SparseGPT 36.97 31.40 17.40 13.46 7.17 6.22 +SI (Ours) 35.79 31.30 17.45 13.45 7.13 6.12 2:4 Magnitude 341.45 417.04 427.18 1153.12 42.54 18.36 +SI (Ours) 226.83 173.99 40.73 31.14 18.55 15.55 Wanda 79.89 112.57 28.16 21.25 11.53 9.60 +SI (Ours) 79.11 94.80 27.54 20.23 10.51 8.32 SparseGPT 61.44 49.55 23.87 17.10 11.00 9.05 +SI (Ours) 60.66 49.51 23.85 17.07 10.65 8.78 4:8 Magnitude 169.09 160.73 240.15 166.94 16.83 13.87 +SI (Ours) 122.89 74.17 28.20 21.44 13.97 13.25 Wanda 53.17 59.12 22.17 16.57 8.58 7.40 +SI (Ours) 53.06 54.30 21.88 16.47 8.15 6.90 SparseGPT 44.81 39.20 20.25 14.98 8.56 7.43 +SI (Ours) 43.63 39.11 20.03 14.93 8.35 7.26

[64] figure: Table 2 : Average zero-shot accuracy (%) ↑ \uparrow on ARC-Easy, ARC-Challenge, HellaSwag, BoolQ, Winogrande, and OpenBookQA; models are LLaMA-1/2 at 7B and 13B. LLaMA-1 LLaMA-2 Sparsity Method 7B 13B 7B 13B 0% Dense 54.79 57.82 55.95 58.25 50% Magnitude 43.17 46.27 48.04 53.40 +SI (Ours) 47.52 46.85 48.68 54.27 Wanda 51.47 55.45 53.63 56.10 +SI (Ours) 52.50 55.32 53.91 56.08 SparseGPT 52.37 54.31 53.34 55.71 +SI (Ours) 52.04 54.16 53.10 56.22 2:4 Magnitude 43.55 46.02 46.01 47.84 +SI (Ours) 42.66 47.28 46.39 51.12 Wanda 45.75 48.73 45.95 50.06 +SI (Ours) 45.71 49.54 46.32 50.98 SparseGPT 46.07 49.31 47.23 52.14 +SI (Ours) 46.30 50.05 47.04 52.59 4:8 Magnitude 46.18 48.46 48.77 52.10 +SI (Ours) 46.07 49.87 49.17 54.49 Wanda 48.58 52.22 50.02 54.59 +SI (Ours) 48.89 52.61 50.37 54.79 SparseGPT 48.73 51.78 50.48 55.09 +SI (Ours) 49.05 52.54 50.90 55.10

[65] figure: Table 3 : Fast Hessian update vs. classical activation-recompute for refreshing the Wanda metric on LLaMA-7B in a epoch of 128 samples(batch size = 1). Method Update time (s) Avg. time/iter (s) Speedup Classical Recompute 345.91 2.70 1.00 × 1.00\times Fast Update (Ours) 15.27 0.12 22.65 × \textbf{22.65}\times

[66] figure: Table 4 : End-to-end latency under 2 : 4 2{:}4 sparsity on LLaMA-7B. Our SI is fully absorbable and adds zero runtime latency compared with wanda. Pattern E2E latency (ms) Speedup Dense 312 1.00 × 1.00\times 2 : 4 2{:}4 (Wanda) 251 1.24 × 1.24\times 2 : 4 2{:}4 (Wanda+SI) 251 1.24 × 1.24\times

[67] h2: 4 CONCLUSIONS

[68] p: We have provided Sparsity Induction (SI), a training-light framework that prepares large language models for pruning. SI acts along two complementary dimensions, distributional and feature level, by applying functionally equivalent per channel transformations consisting of scaling and shifting, and by learning only a small set of parameters on calibration data. This preadaptation suppresses pruning-induced output distortion and reduces accuracy loss while avoiding full parameter fine tuning.

[69] p: Experiments across a range of model sizes and architectures, and with multiple PTS methods, show that SI serves as an easily integrated enhancement that improves the performance of sparse models. The results further indicate that per channel scaling and shifting provide an effective mechanism for restoring expressivity after masking. Future work will explore richer equivalence transformations and structure-aware variants, as well as tighter integration with quantization and other sparsification techniques, in order to further advance sparse large language model performance.

[70] h2: 5 ACKNOWLEDGEMENTS

[71] p: This work was supported in part bythe Strategic Priority Research Program of the Chinese Academy of Sciences (Grant No. XDB1100000); in part by the National Natural Science Foundation of China under Grant Number 62276255; in part by the Postdoctoral Fellowship Program of CPSF under Grant Number GZC20251175;

[72] h2: References

[73] h2: Instructions for reporting errors

[74] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[75] p: Tip: You can select the relevant text first, to include it in your report.

[76] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[77] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
