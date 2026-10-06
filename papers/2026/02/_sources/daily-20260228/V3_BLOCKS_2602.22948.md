[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: ToProVAR: Efficient Visual Autoregressive Modeling via Tri-Dimensional Entropy-Aware Semantic Analysis and Sparsity Optimization

[3] h6: Abstract

[4] p: Visual Autoregressive (VAR) models enhance generation quality but face a critical efficiency bottleneck in later stages. In this paper, we present a novel optimization framework for VAR models that fundamentally differs from prior approaches such as FastVAR and SkipVAR. Instead of relying on heuristic skipping strategies, our method leverages attention entropy to characterize the semantic projections across different dimensions of the model architecture. This enables precise identification of parameter dynamics under varying token granularity levels, semantic scopes, and generation scales. Building on this analysis, we further uncover sparsity patterns along three critical dimensions—token, layer, and scale—and propose a set of fine-grained optimization strategies tailored to these patterns. Extensive evaluation demonstrates that our approach achieves aggressive acceleration of the generation process while significantly preserving semantic fidelity and fine details, outperforming traditional methods in both efficiency and quality. Experiments on Infinity-2B and Infinity-8B models demonstrate that ToProVAR achieves up to 3.4× acceleration with minimal quality loss, effectively mitigating the issues found in prior work. Our code will be made publicly available.

[5] figure: Figure 1: A comparison between our method and state-of-the-art compression methods. The SOTA methods often suffer from issues such as semantic loss, structure distortion, and detail collapse.

[6] h2: 1 Introduction

[7] p: Traditional autoregressive (AR) models generate images via raster-scan next-token prediction ( Li et al., 2024b ; Liu et al., 2024 ; ai et al., 2025 ; Xie et al., 2024 ) , which has long produced inferior results compared to diffusion models. Visual AutoRegressive modeling (VAR) ( Tian et al., 2024 ; Han et al., 2024 ; Tang et al., 2024 ) reformulates generation as coarse-to-fine next-resolution prediction, enabling GPT-style AR models to, for the first time, surpass diffusion models in image quality. Despite these advancements, VAR-based methods still face a core problem: the number of tokens grows exponentially with image resolution and generation scales, resulting in inefficient computation in later stages.

[8] figure: Figure 2: Different Optimization Dimensions – FastVAR vs. SkipVAR vs. ToProVAR

[9] p: To improve the computational efficiency of VAR models, existing researchs, such as FastVAR ( Guo et al., 2025 ) and SkipVAR ( Li et al., 2025a ) , have explored various token reduction strategies. As shown in Fig. 2 (a)(b), FastVAR retains a fixed ratio of high-frequency tokens in the token dimension, while SkipVAR skips certain scales or replaces unconditional branches in the scale dimension based on a trained decision model. Although these methods have demonstrated significant value in accelerating generation, they mainly rely on single-dimensional sparsity analysis of intermediate image data, which introduces several limitations as illustrated in Fig. 1 : (1)Semantic loss: specific tokens corresponding to key objects are pruned when their frequency in the image is too low; (2) Structural distortion: a single sparsity metric like frequency in FastVAR cannot capture the complex relative relationships among objects, leading to noticeable deformations in complex regions; (3) Detail collapse: fine-grained objects typically require deeper generation scales for adequate support, while methods like SkipVAR that skip entire scales result in severe loss of details.

[10] p: Based on the above issues, we identify several critical challenges in optimizing VAR models: (1) Fine-grained sparsity analysis: Unlike prior work, we need to design a highly fine-grained approach to sparsity analysis that effectively prevents information loss caused by misalignment between sparsity metrics and image semantics. (2) Multi-dimensional representation: It is essential to analyze the model across multiple dimensions, enabling not only the assessment of individual token importance but also the accurate characterization of their relative relationships in other dimensions. (3) Efficiency-preserving optimization: While pursuing fine-grained optimization, the analysis itself must remain efficient; otherwise, excessive overhead in modeling sparsity would compromise the overall benefits of the optimization.

[11] p: To address the aforementioned challenges, we introduce a novel optimization framework – ToProVAR – for VAR modeling computing optimization.

[12] p: First, unlike prior approaches such as FastVAR or SkipVAR, which evaluate sparsity directly on intermediate image representations, we leverage attention entropy to analyze how semantics are projected within the model structure during generation. This enables precise tracking of dynamics under varying object salience, semantic scope, and fineness, thereby providing principled guidance for joint semantic–sparsity analysis and optimization.

[13] p: Second, we extend entropy-based analysis beyond tokens to cover three complementary dimensions: token-level, layer-level, and scale-level. This multi-dimensional perspective allows us to uncover semantic distributions and correlations that govern sparsity patterns along token, layer, and scale dimensions. As illustrated in Fig. 2 (c), this facilitates a series of fine-grained optimizations: token-level pruning of non-essential semantics, layer-level compression that distinguishes global from detail representation, and scale-level disentanglement and depth adjustment of generation tailored to object fineness necessity.

[14] p: Finally, we design a coordinated optimization algorithm that integrates these three dimensions, while further improving the efficiency of attention-entropy analysis itself. This ensures not only the effectiveness but also the practicality of our framework for real-world VAR acceleration.

[15] p: We evaluated ToProVAR on mainstream VAR models, Infinity-2B and Infinity-8B. The experimental results show that, compared to FastVAR and SkipVAR, ToProVAR improves inference speed to nearly 3.5× with almost no loss in image quality. In Fig. 1 , we demonstrate the high-quality visual results generated by ToProVAR based on the Infinity-8B model, effectively addressing issues such as semantic loss, structural distortion, and detail collapse.

[16] h2: 2 Preliminary

[17] p: Visual Autoregressive Modeling. VAR redefines the traditional autoregressive paradigm, shifting the core from “next-token prediction” to “next-scale prediction.” For a given image, VAR first obtains a feature map through an encoder, which is then quantized into K K multi-scale token maps ℛ = { r 1 , r 2 , … , r K } \mathcal{R}=\{r_{1},r_{2},\dots,r_{K}\} ; The resolutions of these token maps increase progressively according to a scale schedule { ( h 1 , w 1 ) , ( h 2 , w 2 ) , … , ( h K , w K ) } \{(h_{1},w_{1}),(h_{2},w_{2}),\dots,(h_{K},w_{K})\} . Each token map r k ∈ { 1 , … , V } h k × w k r_{k}\in\{1,\dots,V\}^{h_{k}\times w_{k}} contains h k × w k h_{k}\times w_{k} discrete tokens, all from a codebook of size V V .

[18] p: The joint probability distribution over the multi-scale token maps is factorized autoregressively as:

[19] table: p ⁡ ( r 1 , r 2 , … , r K ) = ∏ k = 1 K p ⁡ ( r k | r 1 , r 2 , … , r k − 1 ) . p(r_{1},r_{2},\dots,r_{K})=\prod_{k=1}^{K}p(r_{k}|r_{1},r_{2},\dots,r_{k-1}). (1)

[20] p: Specifically, at each autoregressive scale k k , the previously generated token maps { r 1 , … , r k − 1 } \{r_{1},\dots,r_{k-1}\} are processed by L L layers of the VAR network to predict the current token map r k r_{k} . This multi-scale generation process supports parallel decoding of multiple tokens within a single token map, significantly improving efficiency compared to traditional “token-by-token” autoregressive models.

[21] p: Attention Entropy for Semantic Projection Analysis. Attention entropy quantifies how concentrated the attention distribution is for a given query. A low entropy value indicates that a token focuses its attention on only a few targets, suggesting strong semantic selectivity; conversely, high entropy reflects a more uniform distribution over targets, implying weaker semantic focus. Formally, given a query q i q_{i} and keys k j {k_{j}} , the attention weights are defined as scaled dot-products, and the entropy is computed as:

[22] table: ℋ ( q i ) = − ∑ j = 1 N α i , j log α i , j , α i , j = exp ⁡ ( q i ⊤ ​ k j / d k ) ∑ l = 1 N exp ⁡ ( q i ⊤ ​ k l / d k ) , \mathcal{H}(q_{i})=-\sum_{j=1}^{N}\alpha_{i,j}\log\alpha_{i,j},\quad\alpha_{i,j}=\frac{\exp(q_{i}^{\top}k_{j}/\sqrt{d_{k}})}{\sum_{l=1}^{N}\exp(q_{i}^{\top}k_{l}/\sqrt{d_{k}})}, (2)

[23] p: where q i q_{i} and k j k_{j} denote the query and key vectors, and d k d_{k} is their dimension. Previous studies ( Cheng et al., 2022 ; Pardyl et al., 2023 ; Choi et al., 2024 ) have exploited this property of attention entropy to distinguish between foreground and background regions. In this work, we build upon this intuition and employ attention entropy for a different purpose: performing fine-grained semantic projection evaluation of VAR models.

[24] p: Unlike frequency-based fixed scopes, however, the range of j j can be flexibly set across different model structures. Extending j j beyond local tokens to encompass cross-layer and multi-scale representations enables entropy to jointly capture semantic evolution across layers and scales. This allows us not only to analyze variations between adjacent tokens, but also to extend the activation range across layer and scale dimensions. In this way, we can simultaneously preserve fine-grained token-level analysis while examining sparsity from broader perspectives in the generation process.

[25] h2: 3 Tri-Dimensional Attention Entropy Generalization and Related Semantic and Sparsity Analysis

[26] figure: Figure 3: Tri-dimensional attention entropy analysis in VAR models: (a) Token-Level Semantic Salience : Pruning low-saliency tokens preserves quality, while pruning high-saliency ones causes severe degradation. (b) Layer-level Semantic Representation : Global Layers capture structure and are pruning-sensitive, whereas detail layers refine local semantics and can be pruned. (c) Scale-level Semantic Depth : complex objects require deeper scales for fine details, while simple ones stabilize earlier, enabling adaptive depth pruning.

[27] p: We leverage attention entropy as a unified measure for semantic projection evaluation, enabling the analysis of data sparsity from three dimensions in VAR models.

[28] p: Token-Level Attention Entropy for Semantic Salience Analysis. Previous approaches, such as frequency-based FastVAR, often overlook semantic information; as a result, tiny and fine details are easily over-optimized and consequently lost, as illustrated in Fig. 1 . In contrast, by employing attention entropy, our analysis is performed at the model dimension, which enables us to effectively capture generation semantics even for fine-grained content. This substantially improves both controllability and accuracy in generation optimization. Frequency-based approaches typically rely on local averaging within a region. When most of the region contains low-frequency content but only a small portion carries high-frequency details, the averaging process suppresses the latter, leading to their removal during pruning (e.g., the cat’s paw in the figure). By leveraging semantic cues, our semantic-based method overcomes this limitation and faithfully preserves both local details and global structures, even under high token pruning ratios.

[29] p: Therefore, semantic salience refers to the salience distribution across tokens, where only a subset of tokens carries critical semantic information. To further evaluate the impact of semantic salience on quality, we progressively pruned tokens from regions of different salience and measured image quality. The results, shown in the right of Fig. 3 (a), demonstrate that on the Infinity-8B model, removing up to 90% of low-saliency tokens leads to only a slight decline in image quality (a drop of < < 2%). However, pruning just 10% of high-saliency tokens causes a significant loss in generation quality, resulting in noticeable artifacts and semantic gaps.

[30] p: Based on this exploration of semantic salience, we propose prioritizing the pruning of low-saliency token regions during the later stages of generation. This approach can accelerate the generation process while preserving the quality of the output.

[31] p: Layer-level Attention Entropy for Semantic Scope Analysis. Attention entropy not only enhances granularity at the token level, but its flexible analysis scope also enables semantic patterns to be examined across broader dimensions. By extending the scope of the attention entropy (the range of index j j in Eq. 2 ) to include all tokens within a layer, we can analyze token distributions in the layer dimension and characterize the generation scope of each layer. Specifically, as shown in Fig. 3 (b), certain layers exhibit relatively uniform, grid-like attention distributions with prominent principal components, focusing on capturing broad spatial relationships and establishing the overall image structure at a global scope. In contrast, the other layers display more varied, semantic-driven attention patterns with less distinct principal components, concentrating on progressively refining local semantics and fine-grained textures within a localized scope.

[32] p: This observation motivates distinguishing layers according to their semantic scope, categorizing them as Global Layers and Detail Layers. Global layers , with their globally distributed attention, encode strong interconnections across the entire image, whereas detail layers , with more localized attention, concentrate on specific regions, leaving substantial sparsity in the unattended areas. Fig. 3 (b) further illustrates the impact of semantic scope on generation quality: compressing global layers by more than 50% significantly degrades output quality, whereas even aggressive compression of detail layers —up to 90% on the Infinity-8B model—maintains high fidelity. This indicates that selectively pruning detail layers can accelerate generation with minimal quality loss.

[33] p: Implementing this strategy, however, requires a reliable method to distinguish global from detail layers. To this end, we propose to identify global and detail layers by the prominence of principal components in their attention entropy distributions and then prune only the detail layers .

[34] p: Scale-level Attention Entropy for Semantic Fineness Analysis. VAR models generate images across multiple autoregressive (AR) scales. Prior approaches often applied coarse-grained scale reduction to reduce computation, but this came at the cost of fine-grained quality. As shown in Fig. 1 , images containing fine details require optimization at the semantic granularity level rather than purely at the scale level.

[35] p: Extending the scope of attention entropy (Eq. 2 ) beyond local tokens to multiple scales enables us to capture the semantic evolution across scales. Specifically, images with high fineness, such as a complex“cyber fox”, exhibit predominantly low-salience distributions, requiring deeper scales to render fine details. In contrast, simpler objects like the letter “W” show predominantly high-salience distributions, stabilizing at shallower scales. As shown in Fig. 3 (c), this trend is further corroborated by their SSIM curves.

[36] p: This scale-level evaluation of attention entropy thus provides a principled way to distinguish the fineness requirements of different objects and adapt the depth accordingly. Based on this observation, we propose dynamically determining the starting scale for pruning according to semantic fineness, enabling adaptive depth allocation for different generation tasks.

[37] h2: 4 Tri-Dimensional VAR Optimization

[38] figure: Figure 4: Tri-Dimensional Entropy-Aware VAR Sparsity Optimization: (a) Scale-level : compute the low-entropy ratio ρ s \rho_{s} across scales and select the pruning start depth via threshold τ \tau . (b) Layer-level : for each scale, perform SVD on the entropy map to separate Global layers from Detail layers. (c) Token-level : within prunable layers/scales, increase pruning rate with scale and use entropy-based gating p prune p_{\text{prune}} to remove low-salience tokens, preserving salient regions.

[39] p: Based on our tri-dimensional generalization of attention entropy and the corresponding semantic analysis, we propose a comprehensive framework with optimization techniques for each dimension. As illustrated in Fig. 4 , given the multi-scale token maps of a VAR model, ℛ = { r 1 , r 2 , … , r k } \mathcal{R}=\{r_{1},r_{2},\dots,r_{k}\} , the framework optimizes the generation process across three dimensions. Specifically, it first estimates the semantic fineness of the scales ℛ \mathcal{R} to dynamically determine the scale depth for pruning, r i r_{i} . Subsequently, within applicable scales, it analyzes each layer’s semantic scope to distinguish between Global and Detail layers, pruning only the latter. Finally, fine-grained token-level sparsification is performed within these layers based on attention entropy, with a unified gating function G G integrating information from all dimensions to determine the pruning probability for each token.

[40] p: Scale-level optimization via Semantic Fineness. Drawing from our scale-level analysis, as the scale increases, the number of high-salience tokens (orange) gradually decreases, implying fewer tokens need to be processed while the semantic fineness of the generated image improves. To capture this effect, we quantify the distribution of high-salience tokens across scales by the proportion of low-entropy tokens: a higher proportion indicates finer semantics. As shown in Fig. 4 (a), we define the low-entropy ratio at scale s s as

[41] table: ρ s = | i ∣ H i s < H ¯ s | N s , \rho_{s}=\frac{\left|{i\mid H_{i}^{s}<\overline{H}^{s}}\right|}{N_{s}}, (3)

[42] p: where H i s H_{i}^{s} denotes the attention entropy of token i i at scale s s , H ¯ s \overline{H}^{s} denotes the mean entropy at scale s s , and N s N_{s} denotes the total number of tokens.

[43] p: Based on this measure, we determine the pruning start scale using a threshold τ \tau . Specifically, the scale depth discrimination function is defined as D = min ⁡ s | ρ s ≥ τ D=\min{s\mid\rho_{s}\geq\tau} , where D D is the minimum scale index at which semantic stability is achieved. To calibrate τ \tau , we conduct multiple pre-sampling experiments. We observe that as generation converges, ρ s \rho_{s} stabilizes, which provides a reliable criterion for dynamically selecting the pruning depth.

[44] p: Layer-level optimization via Semantic Scope. Based on our layer-level analysis, the next optimization step is to distinguish between Global Layers and Detail Layers according to their semantic scope. As shown in Fig. 4 (b), Global Layers exhibit a pronounced dominant component, while Detail Layers do not. To quantify this, we apply singular value decomposition (SVD) to the attention entropy map X X of each layer, i.e., X = U ​ Σ ​ V ⊤ X=U\Sigma V^{\top} . In Global Layers, the gap between the largest and the second largest singular values in Σ \Sigma is pronounced, whereas Detail Layers lack such dominance. We thus define the principal component ratio ϱ ( l , s ) = σ 1 ( l , s ) / σ 2 ( l , s ) \varrho^{(l,s)}=\sigma^{(l,s)}_{1}/\sigma^{(l,s)}_{2} , where σ 1 ( l , s ) \sigma^{(l,s)}_{1} and σ 2 ( l , s ) \sigma^{(l,s)}_{2} denote the two largest singular values of the token representation matrix at layer l l and scale s s .

[45] p: If ϱ ( l , s ) ≫ 1 \varrho^{(l,s)}\gg 1 , the layer is classified as Global; if ϱ ( l , s ) ≈ 1 \varrho^{(l,s)}\approx 1 , it is considered Detail. To provide a continuous score for pruning decisions, we further define the layer representation score :

[46] table: ℛ ( l , s ) = exp ⁡ ( − β ⁡ ( ϱ ( l , s ) − 1 ) ) , β > 0 , \mathcal{R}^{(l,s)}=\exp\big(-\beta(\varrho^{(l,s)}-1)\big),\quad\beta>0, (4)

[47] p: where ℛ ( l , s ) → 1 \mathcal{R}^{(l,s)}\to 1 for Detail Layers and ℛ ( l , s ) → 0 \mathcal{R}^{(l,s)}\to 0 for Global Layers. This score offers a quantitative criterion for layer-level pruning.

[48] p: Token-level optimization via Fine-grained Semantic Salience. After identifying the prunable scales and layers, the final stage is to perform fine-grained token pruning based on semantic salience. The core idea is to eliminate tokens with low salience (i.e., high attention entropy). As illustrated in Fig. 4 (c), to establish a consistent pruning basis across different layers and scales, we first normalize the token’s attention entropy:

[49] table: H ^ i ( l , s ) = H i ( l , s ) ∑ j = 1 N s , l H j ( l , s ) , where ∑ i = 1 N s , l H ^ i ( l , s ) = 1 . \hat{H}_{i}^{(l,s)}=\frac{H_{i}^{(l,s)}}{\sum_{j=1}^{N_{s,l}}H_{j}^{(l,s)}},\qquad\text{where}\quad\sum_{i=1}^{N_{s,l}}\hat{H}_{i}^{(l,s)}=1. (5)

[50] p: We then integrate this normalized entropy with the layer score ℛ ( l , s ) \mathcal{R}^{(l,s)} and a monotonic scale factor ϕ ⁡ ( s ) = s / S max \phi(s)=s/S_{\max} to define a unified pruning tendency: q i ( s , l ) = ϕ ⁡ ( s ) ⋅ ℛ ( l , s ) ⋅ H ^ i ( s , l ) q_{i}^{(s,l)}=\phi(s)\cdot\mathcal{R}^{(l,s)}\cdot\hat{H}_{i}^{(s,l)} . This formulation smoothly incorporates all three dimensions, ensuring that tokens with higher entropy, in layers with broader semantic scope, and at deeper scales are more likely to be pruned.

[51] p: Finally, the pruning tendency is mapped to a retention probability:

[52] table: P keep ​ ( i ∣ s , l ) = { 1 , if ​ s < D , 1 − clip ⁡ ( α min + ( α max − α min ) ​ q i ( s , l ) , 0 , 1 ) , otherwise. P_{\text{keep}}(i\mid s,l)=\begin{cases}1,&\text{if }s<D,\\[6.0pt] 1-\operatorname{clip}\!\Big(\alpha_{\min}+(\alpha_{\max}-\alpha_{\min})\,q_{i}^{(s,l)},\;0,\;1\Big),&\text{otherwise.}\end{cases} (6)

[53] p: This three-factor integration provides a coherent pruning policy across tokens, layers, and scales, effectively discarding redundant details while preserving semantically critical structures.

[54] p: Computational Optimization for Attention Entropy. The attention entropy is formally defined in Equation 2 . A straightforward implementation would require explicitly materializing the full N × N N\times N attention matrix in order to compute row-wise probability distributions and their entropy. However, such an approach is computationally prohibitive in practice, since modern attention implementations such as FlashAttention never instantiate the dense matrix explicitly due to memory and runtime constraints.

[55] p: To address this challenge, we extend the original FlashAttention algorithm with an online entropy computation mechanism, which we refer to as Flash Attention Entropy . The key idea is to preserve the memory efficiency of FlashAttention while simultaneously maintaining sufficient statistics for entropy computation. Inspired by the online softmax strategy in FlashAttention, we design an incremental update scheme that avoids forming the full attention matrix. More concretely, recall that the entropy involves terms of the form x ​ log ⁡ x x\log x over normalized attention scores. By leveraging the algebraic identity k ​ x ​ log ⁡ ( k ​ x ) = k ​ x ​ log ⁡ x + ( log ⁡ k ) ⋅ x ​ k kx\log(kx)=kx\log x+(\log k)\cdot xk We can decompose the entropy computation into two accumulative statistics: the standard normalization terms (rowmax m m and expsum l l ) that are already tracked in FlashAttention, and an additional intermediate statistic that maintains x ​ log ⁡ x x\log x . This decomposition ensures that the entropy can be computed in a streaming fashion with negligible overhead relative to the baseline FlashAttention kernel. The resulting algorithm, termed Flash Attention Entropy , thus inherits the linear-time and memory-efficient properties of FlashAttention while enabling exact entropy computation without approximation.

[56] h2: 5 Experiments

[57] h3: 5.1 Experimental Setup

[58] figure: Table 1: Quantitative comparison on GenEval and DPG. Note, GenEval follows the official protocol without rewritten prompts. Latency is measured on a single GPU with batch size 1. Methods GenEval DPG Latency(s) ↓ \downarrow Speedup Two Obj. Position Color Attri. Overall ↑ \uparrow Entity Relation Attribute Overall ↑ \uparrow Infinity-2B 79.01 24.00 58.00 0.69 90.81 88.19 87.89 83.41 2.10 1.0 × \times +FastVAR 78.79 27.75 59.50 0.68 88.86 91.57 87.46 83.39 0.80 2.6 × \times +SkipVAR 76.77 26.50 57.50 0.67 89.30 87.07 87.01 82.94 1.10 2.0 × \times +ToProVAR 78.80 29.50 62.00 0.69 87.39 88.92 90.01 83.07 0.61 3.4 × \times Infinity-8B 96.97 61.00 75.00 0.83 90.92 93.57 88.83 86.68 4.86 1.0 × \times +FastVAR 94.19 57.00 75.25 0.81 90.80 92.30 90.40 86.50 2.01 2.4 × \times +SkipVAR 94.94 57.50 76.50 0.82 89.71 90.52 90.02 86.44 2.11 2.3 × \times +ToProVAR 94.95 61.00 76.00 0.83 91.11 90.39 91.04 86.70 1.78 2.7 × \times

[59] figure: Table 2: Quantitative comparison on HPSv2.1 and ImageReward, two human preference benchmarks. Latency is measured on a single GPU with batch size 1 1 . Methods HPSv2.1 ImageReward ↑ \uparrow Latency(s) ↓ \downarrow Speedup Photo Concept-Art Anime Paintings Overall ↑ \uparrow Infinity-2B 29.40 30.38 31.72 30.39 30.47 0.94 1.57 1.0 × \times +FastVAR 28.86 29.90 31.12 29.92 29.95 0.92 0.62 2.5 × \times +SkipVAR 29.25 30.25 31.50 30.45 30.39 0.93 0.87 1.8 × \times +ToProVAR 29.26 30.15 31.44 30.23 30.27 0.93 0.58 2.7 × \times Infinity-8B 29.42 31.27 32.45 30.83 30.99 1.04 5.31 1.0 × \times +FastVAR 29.87 30.42 31.80 29.89 30.24 1.02 1.97 2.6 × \times +SkipVAR 29.09 30.86 32.04 30.55 30.64 1.03 2.65 2.0 × \times +ToProVAR 29.19 30.89 32.09 30.24 30.58 1.04 1.75 3.0 × \times

[60] p: Models and Evaluation. We conduct experiments on Infinity-2B and Infinity-8B ( Han et al., 2024 ) . We compare ToProVAR with representative approaches such as FastVAR ( Guo et al., 2025 ) and SkipVAR ( Li et al., 2025a ) , while keeping all hyperparameters consistent for fairness. For evaluation, we adopt widely used benchmarks including Geneval ( Ghosh et al., 2024 ) , DPG-Bench ( Hu et al., 2024 ) , HPSv2 ( Wu et al., 2023 ) , ImageReward ( Xu et al., 2023 ) , and MJHQ30K ( Li et al., 2024a ) . We report Geneval Overall, DPG Overall, HPSv2 score, FID, and CLIP score as quality metrics. Efficiency is assessed in terms of runtime, throughput, and speedup ratio, with latency measured on a single NVIDIA L40 GPU (40GB).

[61] figure: Table 3: Quantitative comparisons of FID and CLIP score with different generation categories on the MJHQ30K dataset. Latency is measured on a single GPU with batch size 1 1 . Method Landscape People Food Latency FID ↓ \downarrow CLIP ↑ \uparrow Latency FID ↓ \downarrow CLIP ↑ \uparrow Latency FID ↓ \downarrow CLIP ↑ \uparrow Infinity-2B 1.67 44.1 0.267 1.71 58.91 0.281 1.69 84.2 0.270 +FastVAR 0.60 45.1 0.264 0.61 71.8 0.274 0.61 84.7 0.273 +SkipVAR 1.01 58.1 0.260 1.06 73.7 0.253 0.88 102.3 0.256 +ToProVAR 0.50 44.5 0.264 0.48 58.84 0.283 0.46 84.3 0.274

[62] h3: 5.2 Main Result

[63] p: Quantitative Comparison on GenEval and DPG. We evaluate ToProVAR on GenEval and DPG to assess the quality–efficiency trade-off (Table 1 ). On Infinity-2B, ToProVAR achieves a 3.4 × \times speedup while maintaining the same GenEval score as the baseline, and even improves fine-grained metrics such as Position (+5.5) and Color Attribute (+4.0). On Infinity-8B, it delivers a 2.7 × \times speedup with no quality degradation, reaching the highest overall scores on both benchmarks. These results show that ToProVAR improves efficiency without sacrificing quality.

[64] p: Quantitative Comparison on HPSv2 and ImageReward. We conduct evaluations on the HPSv2.1 and ImageReward benchmarks to comprehensively evaluate the human preference performance. As shown in Table 2 , ToProVAR achieves significant acceleration while maintaining high-quality generation. On the Infinity-2B model, ToProVAR reduces inference latency by 62.4% with a negligible drop in the overall HPSv2 score (<1%). The advantages of ToProVAR are even more pronounced on the larger Infinity-8B model, where it reduces latency by 67% while preserving the same ImageReward score and a highly competitive HPSv2 score. These results powerfully demonstrate that ToProVAR strikes an exceptional balance between efficiency and quality, effectively upholding subjective image quality and human preference alignment while improving inference speed.

[65] figure: Figure 5: Qualitative comparison of various methods on complex prompts. Our method effectively prevents semantic loss, structure distortion, and detail collapse while maintaining high visual fidelity.

[66] figure: Table 4: Ablation study of the Three-Dimensional Progressive Manipulation Framework on Infinity-2B, where “+”, “++”, and “+++” denote progressive component addition over the previous stage. Method Latency(s) ↓ \downarrow Speed ↑ \uparrow GenEval ↑ \uparrow Infinity-2B 2.10 - 0.690 + Scale Depth Loc. 0.47 4.5 × \times 0.477 ++ Layer Repr. Ident. 0.57 3.7 × \times 0.679 +++ Fine-grained Token Prun. 0.61 3.4 × \times 0.690 Table 5: Ablation Studies of Flash Attention Entropy on Infinity-2B.“w/o FAE” denotes naive attention entropy calculation, which creates computational overhead. Setup Speed ↑ \uparrow Latency(s) ↓ \downarrow Infinity-2B - 2.10 +FastVAR 2.6 × \times 0.80 +ToProVAR(w/o FAE) 1.9 × \times 1.10 +ToProVAR(w/ FAE) 3.4 × \times 0.61

[67] figure: Figure 6: Qualitative Visualizations of the three components ablation(Scale, Layer, Token) on Infinity-2B.The full tri-stage framework better preserves global layout and local details than partial variants that prune along only a subset of dimensions.

[68] p: Quantitative Comparison on MJHQ30K. In Table 3 , we validate the perceptual quality on the MJHQ30K benchmark. It can be seen that our ToProVAR achieves a reasonable performance while maintaining a high speedup ratio. For instance, on the challenging People category, our ToProVAR even achieves a FID reduction with 3.5 × \times acceleration, decreasing FID from 58.91 to 58.84. In other categories, our method also maintains good performance with significant acceleration.

[69] p: Qualitative Visualizations of Different Methods. Figure 5 presents qualitative results of different methods on Infinity-2B/8B. Compared to FastVAR and SkipVAR, ToProVAR effectively mitigates semantic loss, structural distortion, and detail collapse. It maintains high visual fidelity while achieving a greater acceleration ratio.

[70] h3: 5.3 Ablation Study

[71] p: Impact of Stages in the Tri-Dimensional Optimization Framework. To validate the effectiveness of our design, we analyze the contribution of each stage in the framework in Table 5 and Figure 6 . A coarse-grained approach using only Scale Depth Localization and Layer Representation Identification is fast but suboptimal, with a GenEval score of 0.679. Incorporating Fine-grained Token Pruning completes the ToProVAR model, restoring the score to 0.690—nearly matching the baseline—while maintaining a low 0.61s latency. This result highlights that our complete tri-stage framework is essential for optimally balancing acceleration and fidelity.

[72] p: Ablation Studies on Flash Attention Entropy. We validate the efficiency of our integrated Flash Attention Entropy (FAE) module in Table 5 . Naively attention entropy calculation without FAE creates a significant computational bottleneck, increasing latency to 1.10s. In contrast, our fully integrated module eliminates this overhead and reduces latency to 0.61s. This result confirms that FAE is critical for ToProVAR, as it preserves and enhances the acceleration benefits of Flash Attention.

[73] figure: Operation / Time (ms) All Scales Rep. Scale s Frequency & Entropy ( s = 10 s=10 ) Frequency-based scoring 1.30 0.16 Attention Entropy (naïve) 125.73 12.06 FlashAttention 11.27 1.11 Flash Attention Entropy 12.97 1.28 Layer-level SVD ( s = 6 s=6 ) SVD per layer – 1.25 SVD over all layers – 49.84 Table 6: Time cost of frequency-, entropy-, and SVD-related operations on Infinity-8B. Figure 7: Visualization of pruned tokens by FastVAR and ToProVAR.

[74] p: Visualization of pruned tokens with different methods. Fig. 12 visualizes the divergent pruning strategies of FastVAR and ToProVAR. While FastVAR’s frequency-based heuristic retains edges, it erodes an image’s semantic integrity by removing tokens from smooth yet vital areas like facial contours. This structural damage becomes severe as the pruning ratio increases. In contrast, ToProVAR leverages attention entropy to identify and preserve core semantic content. Even at a 90% pruning ratio, it protects critical features like the eyes. This visu al comparison confirms that attention entropy is a more robust heuristic than frequency for preserving semantic structure during pruning.

[75] p: Computational Cost Analysis. We further quantify the overhead of our tri-dimensional sparsity framework, focusing on Flash Attention Entropy (FAE) and the layer-level SVD analysis. As shown in Table 6 , naïve attention entropy incurs a severe bottleneck due to explicit attention-matrix materialization, whereas FAE computes entropy on-the-fly inside the FlashAttention kernel with only a lightweight x ​ log ⁡ x x\log x reduction. This yields only 0.17 ms overhead over FlashAttention at scale 10, yet reduces entropy cost by ∼ \sim 90%. For layer analysis, SVD is performed once per layer at a single representative scale ( s = 6 s{=}6 ). Table 6 shows 49.84 ms total over all layers, i.e., < 3 % <3\% of the 1780 ms end-to-end latency, indicating minor overhead.

[76] h2: 6 Related Work

[77] h5: Autoregressive Visual Generation.

[78] p: AR models ( Li et al., 2024b ; Liu et al., 2024 ; ai et al., 2025 ; Xie et al., 2024 ) ), originally successful in language, have been extended to image generation through next-token prediction ( Van Den Oord et al., 2017 ; Dai et al., 2025 ) . Recent scaling has narrowed the gap with diffusion models ( Xie et al., 2024 ; Wu et al., 2024b ; Wang et al., 2024 ; Wu et al., 2024a ) . Yet efficiency remains a bottleneck. To address this, Visual Autoregressive (VAR) modeling ( Tian et al., 2024 ; Han et al., 2024 ; Tang et al., 2024 ) introduces a next-scale paradigm, where images are predicted in hierarchical token maps from coarse to fine resolution. This strategy reduces the number of autoregressive steps and improves both speed and quality.

[79] h5: Efficient Visual Generation.

[80] p: The acceleration of diffusion models has been extensively studied, with mature methods including distillation ( Kim et al., 2025 ; Zhai et al., 2024 ; Yin et al., 2025 ) , quantization ( Zhao et al., 2024a ; Xi et al., 2025 ; Wu et al., 2025 ) , pruning ( Zou et al., 2024 ; Fang et al., 2025 ; Heo et al., 2025 ) , and feature caching ( Liu et al., 2025b ; Zhao et al., 2024b ; Ma et al., 2024 ; Lv et al., 2024 ; Liu et al., 2025a ) . Efficient though, they are tailored to diffusion architectures and cannot be directly applied to the hierarchical prediction in VAR.

[81] p: Efficiency optimization for VAR is still nascent. Early works such as FastVAR ( Guo et al., 2025 ) and SkipVAR ( Li et al., 2025a ) exploit fixed pruning or frequency-based skipping, while recent methods explore semantic- and structure-aware acceleration, e.g., SparseVAR ( Chen et al., 2025a ) for token sparsity and CoDe ( Chen et al., 2025b ) for collaborative decoding. Complementary insights are provided by methods such as HACK ( Qin et al., 2025 ) and ScaleKV ( Li et al., 2025b ) , which focus on KV cache compression.

[82] h2: 7 Conclusion

[83] p: In this work, we present ToProVAR , a novel acceleration framework that addresses tri-dimensional redundancies of Visual Autoregressive models. ToProVAR leverages attention entropy to uncover sparsity patterns across tokens, layers, and scales. With fine-grained semantic modeling and pruning strategy, critical contents are preserved even with aggressive acceleration, achieving 3.4 × \times speedup with minimal quality loss, surpassing existing methods. Our study highlights the value of semantic-driven optimization for AR generation and future extensions in video and multimodal modeling.

[84] h2: References

[85] h2: Appendix A Appendix

[86] h3: A.1 Experiment Details

[87] h4: A.1.1 Models

[88] p: Our evaluation is based on the state-of-the-art Visual Autoregressive Models, specifically Infinity-2B and Infinity-8B ( Han et al., 2024 ) . These models have demonstrated exceptional performance across a wide range of image generation tasks. For our experiments, we utilize their pre-trained versions and adopt their default inference configurations, with the prime structures detailed in Table 7 .

[89] figure: Table 7: The basic information of models. model scales layers Infinity-2B 11 32 Infinity-8B 13 40

[90] h4: A.1.2 Baselines Settings

[91] p: To ensure a fair comparison, we standardized experimental parameters, such as the random seed, across all compared models—Infinity, FastVAR ( Guo et al., 2025 ) , SkipVAR ( Li et al., 2025a ) , and our own ToProVAR—to eliminate the influence of confounding variables.

[92] p: We empirically analyzed the hyperparameters of FastVAR and found that its 32 ratio and 40 ratio parameters had a non-monotonic, convex-like effect on generation quality. Consequently, we adopted the optimal, default parameter configuration for our comparisons. For SkipVAR, we directly used its default decision model of (0.84). The specific parameter settings are detailed in the relevant tables.

[93] figure: Table 8: Acceleration Configurations for FastVAR and SkipVAR. NOTE: Notation ’s:p’ means scale index s is pruned with pruning ratio p,All ratios are applied per-layer at inference time. Method Model Method Parameter FastVAR Infinity-2B {10:0.4;11:0.6} Infinity-8B {10:0.4;11:0.6;12:1.0;13:1.0} SkipVAR Infinity-2B 0.84 Infinity-8B 0.84@2B

[94] h4: A.1.3 Metrics

[95] p: In this work, we employ a diverse set of established metrics to comprehensively evaluate our method, aiming to assess both objective image generation quality and adherence to human instructions.

[96] p: First, we utilize Geneval ( Ghosh et al., 2024 ) and DPG-bench ( Hu et al., 2024 ) to focus on the objective quantification of generation quality.

[97] p: Geneval. Geneval serves as a crucial tool for measuring foundational generation quality. It decomposes the task into six fine-grained sub-tasks: single-object generation, object co-occurrence, counting, color control, relative positioning, and attribute binding. By using a pre-trained detector to compare generated results with ground-truth annotations, this metric outputs multi-dimensional compliance scores, and its average serves as a comprehensive quality measure.

[98] p: DPG-bench. DPG-bench is a specialized evaluation benchmark for scenarios involving dense prompts. It focuses on the generation quality of multi-object, multi-attribute, and multi-relational descriptions, serving as a key indicator of a model’s ability to align with complex semantics and follow instructions.

[99] p: Second, we leverage HPSv2 ( Wu et al., 2023 ) , ImageReward ( Xu et al., 2023 ) , and SSIM ( Wang et al., 2004 ) to establish a quantitative link between our generated results and human perception, focusing on perceptual similarity and visual preference.

[100] p: Human Preference Score v2(HPSv2). HPSv2 is designed to measure the alignment between generated content and human hierarchical visual perception. It uses a pre-trained visual network to extract both ”low-level features (edges, colors)” and ”high-level features (object structure, semantics)” from the generated and reference content, then aggregates them to yield a final score. This metric effectively gauges the perceptual plausibility of the generated content from a human perspective.

[101] p: ImageReward(IR). IR is another important metric for aligning text-to-image generation with human preferences. It directly outputs a preference score, quantifying the visual appeal and realism of the generated content.

[102] p: Structural Similarity Index Measure (SSIM). To facilitate the analysis of generation states across images of varying complexity, we introduce SSIM. It provides a measure of image quality that reflects structural and perceptual differences. The formula is defined as:

[103] table: SSIM ​ ( x , y ) = ( 2 ​ μ x ​ μ y + C 1 ) ​ ( 2 ​ σ x ​ y + C 2 ) ( μ x 2 + μ y 2 + C 1 ) ​ ( σ x 2 + σ y 2 + C 2 ) \text{SSIM}(x,y)=\frac{(2\mu_{x}\mu_{y}+C_{1})(2\sigma_{xy}+C_{2})}{(\mu_{x}^{2}+\mu_{y}^{2}+C_{1})(\sigma_{x}^{2}+\sigma_{y}^{2}+C_{2})}

[104] h4: A.1.4 Generalization Experiments

[105] p: To assess the generalization of ToProVAR beyond the Infinity series, we further evaluate it on HART Tang et al. (2024) , a VAR-style hybrid autoregressive transformer.For HART, we use the official pre-trained checkpoint and default sampling configuration. The resulting quality–efficiency comparison between HART, HART+FastVAR, and HART+ToProVAR is reported in Table 9 , showing that ToProVAR maintains comparable GenEval scores to the HART baseline while achieving additional speedups and a better quality–efficiency trade-off than FastVAR.

[106] figure: Table 9: Comparison of ToProVAR and FastVAR on the GenEval benchmark using HART. Method Two Obj. Position Color Attri. Overall ↑ \uparrow Latency (s) ↓ \downarrow Speedup ↑ \uparrow HART 0.62 0.13 0.18 0.51 0.51 0.95 1.0 × \times +FastVAR 0.59 0.13 0.19 0.50 0.50 0.64 1.5 × \times +ToProVAR (ours) 0.61 0.13 0.18 0.51 0.51 0.56 1.7 × \times

[107] h4: A.1.5 Further Tri-Dimensional Ablation Experiments

[108] p: In the Table 5 of main paper, we provide a three-stage ablation on Infinity-2B. To more clearly isolate the contributions of each dimension in our tri-dimensional framework (Scale → \rightarrow Layer → \rightarrow Token), we further introduce two controlled variants and conduct an extended ablation, summarized in Table 10 .

[109] p: Concretely, all variants share the same Infinity-2B backbone and sampling settings, and differ only in which sparsity dimensions are activated:

[110] p: Fix Scale Exit. A coarse baseline that skips a fixed set of late scales with a hand-crafted exit scale, without any Scale Depth Localization. This variant achieves the highest nominal speed but suffers from the most severe quality degradation, highlighting the importance of adaptive scale selection.

[111] p: Scale Depth Localization (Scale). A pure scale-skipping variant in which only the Scale Depth Localization module is enabled. It adaptively selects the pruning start scale and skips subsequent scales, improving efficiency over the baseline, but may still introduce noticeable semantic distortions due to the lack of layer- and token-level control.

[112] p: Scale Depth Loc. + Fine-grained Token Pruning (Scale + Token). A configuration that combines adaptive scale skipping with token-level pruning applied uniformly across all layers, without Layer Representation Identification. While this improves over purely scale-level pruning, its quality remains clearly below the baseline, indicating that unconstrained token pruning on Global layers can harm global semantics.

[113] p: Scale Depth Loc. + Layer Representation Identification (Scale + Layer). A scale–layer variant in which we perform adaptive scale skipping together with layer skipping guided by the layer-scope analysis. Layers identified as Detail are skipped more aggressively, whereas Global layers are largely preserved. This substantially recovers global structure and semantics while maintaining strong acceleration.

[114] p: Full ToProVAR (Scale + Layer + Token). The complete tri-stage framework, which combines adaptive scale skipping, layer skipping based on Global/Detail classification, and fine-grained token pruning restricted to selected Detail layers. This configuration restores generation quality to be on par with the baseline while retaining substantial speedup.

[115] p: Overall, these extended ablations demonstrate the progressive and complementary roles of scale-, layer-, and token-level optimization in balancing acceleration and fidelity: naive scale-only or scale+token pruning can be overly aggressive, whereas the full tri-dimensional design of ToProVAR achieves a much better quality–efficiency trade-off. These configurations correspond to the rows in Table 10 and the visual comparisons in Figure 6 , and are used consistently across all ablation experiments.

[116] figure: Table 10: Extended ablation study of the tri-dimensional progressive framework on Infinity-2B. Method Latency (s) ↓ \downarrow Speed ↑ \uparrow GenEval ↑ \uparrow Infinity-2B 2.10 1.0 × \times 0.690 Fix Scale Exit 0.41 5.1 × \times 0.403 Scale Depth Loc. 0.47 4.5 × \times 0.477 Scale Depth Loc. + Fine-grained Token Prun. 0.78 2.7 × \times 0.603 Scale Depth Loc. + Layer Repr. Ident. 0.57 3.7 × \times 0.679 ToProVAR (Scale + Layer + Token) 0.61 3.4 × \times 0.690

[117] figure: Figure 8: Robustness analysis of the scale-depth threshold τ \tau . Left: mean attention entropy vs. scale. Right: low-entropy ratio ρ s \rho_{s} vs. scale, together with the distribution of ρ s \rho_{s} for images whose SSIM to the full-scale baseline exceeds 0.8 0.8 .

[118] h3: A.2 Calibration and robustness of the scale-depth threshold τ \tau

[119] p: Building on the scale-level analysis in Eq. (3), we quantify the semantic fineness at scale s s by the low-entropy ratio

[120] table: ρ s = | { i ∣ H i s < H ¯ s } | N s , \rho_{s}=\frac{\lvert\{i\mid H_{i}^{s}<\bar{H}^{s}\}\rvert}{N_{s}}, (7)

[121] p: where H i s H_{i}^{s} denotes the attention entropy of token i i at scale s s , H ¯ s \bar{H}^{s} is the mean entropy at that scale, and N s N_{s} is the number of tokens.

[122] p: To calibrate the pruning start depth, we perform a lightweight pre-sampling procedure on a small set of prompts and compute statistics across scales. For each backbone (e.g., Infinity-2B, Infinity-8B), we randomly sample a calibration subset of prompts from HPSv2 and DPG-Bench, and plot both the Mean-Entropy–scale curves and the ρ s \rho_{s} –scale curves, as shown in Fig. 8 . We obtain the following empirical observations:

[123] p: Consistency of mean entropy across datasets. As shown in the left panel, for a fixed backbone, the mean attention entropy at each scale is highly consistent across HPSv2, DPG-Bench, and a randomly sampled 50-prompt subset: both the absolute values and the scale-wise trends of the curves almost overlap. This indicates that the attention-entropy statistics are largely insensitive to the specific dataset or calibration subset.

[124] p: Stability of the low-entropy ratio across scales. The right panel shows that the ρ s \rho_{s} –scale curves for different datasets and calibration-set sizes (50 prompts vs. the full prompt set) exhibit very similar trajectories. For a given backbone, the scale index at which ρ s \rho_{s} enters a “reasonable” band is highly stable across datasets and prompt subsets.

[125] p: Low-entropy ratio as a quality indicator and choice of τ = 0.4 \tau=0.4 . The scatter points in the right panel correspond to images whose SSIM with respect to the full-scale baseline is greater than 0.8 0.8 . These high-quality generations concentrate around a narrow range of low-entropy ratios, approximately centered at ρ s ≈ 0.4 \rho_{s}\approx 0.4 . This observation suggests that ρ s \rho_{s} can serve as a proxy for generation quality, and motivates the choice of τ = 0.4 \tau=0.4 as a quality-aware threshold.

[126] p: Based on this invariance, we choose a single global threshold τ \tau per backbone such that ρ s ≥ τ \rho_{s}\geq\tau marks the onset of semantically stable scales suitable for pruning. In practice, τ \tau is calibrated once on the small calibration subset and then reused across all datasets, resolutions, and prompts, without any dataset-specific hyperparameter search. This explains why the same τ \tau generalizes well in all our experiments and why our scale-level pruning remains robust under variations in prompts and resolutions.

[127] h3: A.3 More Visualization Results

[128] p: This section presents additional visualizations that complement the observations described in the main text.

[129] figure: Figure 9: Visualization of token-level pruning in ToProVAR. Gray tokens indicate those pruned by ToProVAR, while colored tokens correspond to preserved, semantically salient regions.

[130] h4: A.3.1 Pruned Tokens Visualizations

[131] p: In this section, we visualize the token-level pruning decisions made by ToProVAR on image generation tasks with varying levels of complexity. For each example, tokens that are pruned by ToProVAR are rendered in gray, while preserved tokens retain their original image appearance. As shown in Figure 9 , ToProVAR primarily removes tokens in redundant background regions and keeps tokens concentrated around object contours and fine details, leading to more accurate and semantically aligned sparsity patterns.

[132] figure: Figure 10: Additional visualizations of layer representations on HART, Infinity-2B, and Infinity-8B.We show example attention maps for the representative Global and Detail layers.

[133] figure: Figure 11: Additional visualizations of failure layer representation case.

[134] h4: A.3.2 Layer-Level Semantic Representation Visualizations

[135] p: In this section, we provide additional visualizations of layer-level semantic representations across different VAR backbones. As shown in Figure 10 , we consistently observe two dominant patterns along the layer dimension: some layers exhibit grid-like, globally distributed attention, while others focus on localized, fine-grained regions. This dichotomy underpins our strategy of categorizing layers into Global and Detail layers, and it substantiates the design of Stage II, where semantic analysis and pruning are performed at the layer level.

[136] p: Crucially, this behavior is not restricted to the Infinity series. When we apply the same layer-scope analysis to HART, we find a very similar organization: early and final layers tend to act as Global Layers with a dominant principal component, whereas middle layers behave as Detail Layers with more localized and diverse semantics. This pattern is stable across prompts and scales when we classify layers at a representative, semantically stable scale.

[137] p: Figure 11 further illustrates the rare ambiguous cases. In these layers, the attention maps exhibit both weak grid-like global structure and pronounced object-centric activations, so that the layer plays a mixed role of refining global layout and local details. Such hybrid behavior typically arises at transition layers where global composition is being finalized while fine details start to emerge, and is further amplified by averaging over heads, since different heads may specialize in global versus local semantics. Consequently, these layers lie close to the decision boundary of our principal-component–based classifier and can be labeled as Global or Detail depending on small variations across prompts or scales. However, they account for only a very small subset of layers we inspected, and their impact on final accuracy is negligible: our pruning policy is conservative on Detail layers, and the semantics captured by these ambiguous layers are largely redundant with neighboring layers.

[138] h4: A.3.3 Qualitative Comparison of Various Methods

[139] p: We further present qualitative comparisons of FastVAR, SkipVAR, and ToProVAR on the Infinity-2B and Infinity-8B backbones. As shown in Figure 12 , we visualize generated images across diverse prompts and scenes, which allows an intuitive assessment of the quality–efficiency trade-offs achieved by each method. In particular, ToProVAR tends to better preserve global layout and fine-grained details while operating at comparable or higher acceleration levels.

[140] figure: Figure 12: Additional visualization results of FastVAR, SkipVAR, and ToProVAR on Infinity-2B and Infinity-8B. Compared to the baselines, ToProVAR more faithfully preserves global structure and fine details under similar or higher acceleration, yielding visually sharper and more semantically consistent generations.

[141] h3: A.4 Flash Attention Entropy (FAE)

[142] figure: Algorithm 1 original FlashAttention forward pass 0: Matrices 𝐐 , 𝐊 , 𝐕 ∈ ℝ N × d \mathbf{Q},\mathbf{K},\mathbf{V}\in\mathbb{R}^{N\times d} in HBM, block sizes B c B_{c} , B r B_{r} . 1: Divide 𝐐 \mathbf{Q} into T r = ⌈ N B r ⌉ T_{r}=\left\lceil\frac{N}{B_{r}}\right\rceil blocks 𝐐 1 , … , 𝐐 T r \mathbf{Q}_{1},\dots,\mathbf{Q}_{T_{r}} of size B r × d B_{r}\times d each, and divide 𝐊 , 𝐕 \mathbf{K},\mathbf{V} in to T c = ⌈ N B c ⌉ T_{c}=\left\lceil\frac{N}{B_{c}}\right\rceil blocks 𝐊 1 , … , 𝐊 T c \mathbf{K}_{1},\dots,\mathbf{K}_{T_{c}} and 𝐕 1 , … , 𝐕 T c \mathbf{V}_{1},\dots,\mathbf{V}_{T_{c}} , of size B c × d B_{c}\times d each. 2: Divide the output 𝐎 ∈ ℝ N × d \mathbf{O}\in\mathbb{R}^{N\times d} into T r T_{r} blocks 𝐎 i , … , 𝐎 T r \mathbf{O}_{i},\dots,\mathbf{O}_{T_{r}} of size B r × d B_{r}\times d each, and divide the logsumexp L L into T r T_{r} blocks L i , … , L T r L_{i},\dots,L_{T_{r}} of size B r B_{r} each. 3: for 1 ≤ i ≤ T r 1\leq i\leq T_{r} do 4: Load 𝐐 i \mathbf{Q}_{i} from HBM to on-chip SRAM. 5: On chip, initialize 𝐎 i ( 0 ) = ( 0 ) B r × d ∈ ℝ B r × d , ℓ i ( 0 ) = ( 0 ) B r ∈ ℝ B r , m i ( 0 ) = ( − ∞ ) B r ∈ ℝ B r \mathbf{O}_{i}^{(0)}=(0)_{B_{r}\times d}\in\mathbb{R}^{B_{r}\times d},\ell_{i}^{(0)}=(0)_{B_{r}}\in\mathbb{R}^{B_{r}},m_{i}^{(0)}=(-\infty)_{B_{r}}\in\mathbb{R}^{B_{r}} . 6: for 1 ≤ j ≤ T c 1\leq j\leq T_{c} do 7: Load 𝐊 j , 𝐕 j \mathbf{K}_{j},\mathbf{V}_{j} from HBM to on-chip SRAM. 8: On chip, compute 𝐒 i ( j ) = 𝐐 i ​ 𝐊 j T ∈ ℝ B r × B c \mathbf{S}_{i}^{(j)}=\mathbf{Q}_{i}\mathbf{K}_{j}^{T}\in\mathbb{R}^{B_{r}\times B_{c}} . 9: On chip, compute m i ( j ) = max ⁡ ( m i ( j − 1 ) , rowmax ⁡ ( 𝐒 i ( j ) ) ) ∈ ℝ B r m_{i}^{(j)}=\mathrm{max}(m_{i}^{(j-1)},\mathrm{rowmax}(\mathbf{S}_{i}^{(j)}))\in\mathbb{R}^{B_{r}} , 𝐏 ~ i ( j ) = exp ⁡ ( 𝐒 i ( j ) − m i ( j ) ) ∈ ℝ B r × B c \tilde{\mathbf{P}}_{i}^{(j)}=\exp(\mathbf{S}_{i}^{(j)}-m_{i}^{(j)})\in\mathbb{R}^{B_{r}\times B_{c}} (pointwise), ℓ i ( j ) = e m i j − 1 − m i ( j ) ​ ℓ i ( j − 1 ) + rowsum ⁡ ( 𝐏 ~ i ( j ) ) ∈ ℝ B r \ell_{i}^{(j)}=e^{m_{i}^{j-1}-m_{i}^{(j)}}\ell_{i}^{(j-1)}+\mathrm{rowsum}(\tilde{\mathbf{P}}_{i}^{(j)})\in\mathbb{R}^{B_{r}} . 10: On chip, compute 𝐎 i ( j ) = diag ​ ( e m i ( j − 1 ) − m i ( j ) ) − 1 ​ 𝐎 i ( j − 1 ) + 𝐏 ~ i ( j ) ​ 𝐕 j \mathbf{O}_{i}^{(j)}=\mathrm{diag}(e^{m_{i}^{(j-1)}-m_{i}^{(j)}})^{-1}\mathbf{O}_{i}^{(j-1)}+\tilde{\mathbf{P}}_{i}^{(j)}\mathbf{V}_{j} . 11: end for 12: On chip, compute 𝐎 i = diag ​ ( ℓ i ( T c ) ) − 1 ​ 𝐎 i ( T c ) \mathbf{O}_{i}=\mathrm{diag}(\ell_{i}^{(T_{c})})^{-1}\mathbf{O}_{i}^{(T_{c})} . 13: On chip, compute L i = m i ( T c ) + log ⁡ ( ℓ i ( T c ) ) L_{i}=m_{i}^{(T_{c})}+\log(\ell_{i}^{(T_{c})}) . 14: Write 𝐎 i \mathbf{O}_{i} to HBM as the i i -th block of 𝐎 \mathbf{O} . 15: Write L i L_{i} to HBM as the i i -th block of L L . 16: end for 17: Return the output 𝐎 \mathbf{O} and the logsumexp L L .

[143] p: To efficiently obtain attention entropy without materializing the full attention matrix, we extend the original FlashAttention forward pass to compute entropy on the fly inside the streaming kernel.

[144] p: As summarized in Algorithm 1 , the standard FlashAttention implementation processes 𝐐 , 𝐊 , 𝐕 \mathbf{Q},\mathbf{K},\mathbf{V} in blocks, incrementally updating the partial output 𝐎 i ( j ) \mathbf{O}_{i}^{(j)} and the normalization statistics ( m i ( j ) , ℓ i ( j ) ) (m_{i}^{(j)},\ell_{i}^{(j)}) for each query block. At the end of the loop over key/value blocks, it returns the normalized output 𝐎 \mathbf{O} together with the per-row log-sum-exp L L , which is typically used for numerical stability and backward computation.

[145] p: Our Flash Attention Entropy (FAE), shown in Algorithm 2 , augments this kernel with an additional accumulator E i ( j ) E_{i}^{(j)} that maintains the running sum of p ​ log ⁡ p p\log p in the same numerically stable streaming fashion used for ℓ i ( j ) \ell_{i}^{(j)} . Concretely, we reuse the intermediate unnormalized probabilities 𝐏 ~ i ( j ) \tilde{\mathbf{P}}_{i}^{(j)} and apply a lightweight row_reduce_xlogx operation at each step. After processing all key/value blocks, we obtain the per-query entropy vector E i E_{i} by combining E i ( T c ) E_{i}^{(T_{c})} and ℓ i ( T c ) \ell_{i}^{(T_{c})} , in analogy to how L i L_{i} is derived from m i ( T c ) m_{i}^{(T_{c})} and ℓ i ( T c ) \ell_{i}^{(T_{c})} . This design keeps the memory footprint identical to standard FlashAttention and avoids constructing the full N × N N\times N attention matrix.

[146] p: Since our sparsity framework only requires the attention output 𝐎 \mathbf{O} and the corresponding entropy E E at inference time, we do not use the log-sum-exp L L returned by the original kernel. In our implementation, we therefore drop L L from the return values and only expose ( 𝐎 , E ) (\mathbf{O},E) , while the core FlashAttention streaming structure remains unchanged.

[147] figure: Algorithm 2 FlashAttention forward pass with entropy 0: Matrices 𝐐 , 𝐊 , 𝐕 ∈ ℝ N × d \mathbf{Q},\mathbf{K},\mathbf{V}\in\mathbb{R}^{N\times d} in HBM, block sizes B c B_{c} , B r B_{r} . 1: Divide 𝐐 \mathbf{Q} into T r = ⌈ N B r ⌉ T_{r}=\left\lceil\frac{N}{B_{r}}\right\rceil blocks 𝐐 1 , … , 𝐐 T r \mathbf{Q}_{1},\dots,\mathbf{Q}_{T_{r}} of size B r × d B_{r}\times d each, and divide 𝐊 , 𝐕 \mathbf{K},\mathbf{V} in to T c = ⌈ N B c ⌉ T_{c}=\left\lceil\frac{N}{B_{c}}\right\rceil blocks 𝐊 1 , … , 𝐊 T c \mathbf{K}_{1},\dots,\mathbf{K}_{T_{c}} and 𝐕 1 , … , 𝐕 T c \mathbf{V}_{1},\dots,\mathbf{V}_{T_{c}} , of size B c × d B_{c}\times d each. 2: Divide the output 𝐎 ∈ ℝ N × d \mathbf{O}\in\mathbb{R}^{N\times d} into T r T_{r} blocks 𝐎 i , … , 𝐎 T r \mathbf{O}_{i},\dots,\mathbf{O}_{T_{r}} of size B r × d B_{r}\times d each, and divide the logsumexp L L into T r T_{r} blocks L i , … , L T r L_{i},\dots,L_{T_{r}} of size B r B_{r} each. 3: for 1 ≤ i ≤ T r 1\leq i\leq T_{r} do 4: Load 𝐐 i \mathbf{Q}_{i} from HBM to on-chip SRAM. 5: On chip, initialize 𝐎 i ( 0 ) = ( 0 ) B r × d ∈ ℝ B r × d , ℓ i ( 0 ) = ( 0 ) B r ∈ ℝ B r , E i ( 0 ) = ( 0 ) B r ∈ ℝ B r , m i ( 0 ) = ( − ∞ ) B r ∈ ℝ B r \mathbf{O}_{i}^{(0)}=(0)_{B_{r}\times d}\in\mathbb{R}^{B_{r}\times d},\ell_{i}^{(0)}=(0)_{B_{r}}\in\mathbb{R}^{B_{r}},E_{i}^{(0)}=(0)_{B_{r}}\in\mathbb{R}^{B_{r}},m_{i}^{(0)}=(-\infty)_{B_{r}}\in\mathbb{R}^{B_{r}} . 6: for 1 ≤ j ≤ T c 1\leq j\leq T_{c} do 7: Load 𝐊 j , 𝐕 j \mathbf{K}_{j},\mathbf{V}_{j} from HBM to on-chip SRAM. 8: On chip, compute 𝐒 i ( j ) = 𝐐 i ​ 𝐊 j T ∈ ℝ B r × B c \mathbf{S}_{i}^{(j)}=\mathbf{Q}_{i}\mathbf{K}_{j}^{T}\in\mathbb{R}^{B_{r}\times B_{c}} . 9: On chip, compute m i ( j ) = max ⁡ ( m i ( j − 1 ) , rowmax ⁡ ( 𝐒 i ( j ) ) ) ∈ ℝ B r m_{i}^{(j)}=\mathrm{max}(m_{i}^{(j-1)},\mathrm{rowmax}(\mathbf{S}_{i}^{(j)}))\in\mathbb{R}^{B_{r}} , 𝐏 ~ i ( j ) = exp ⁡ ( 𝐒 i ( j ) − m i ( j ) ) ∈ ℝ B r × B c \tilde{\mathbf{P}}_{i}^{(j)}=\exp(\mathbf{S}_{i}^{(j)}-m_{i}^{(j)})\in\mathbb{R}^{B_{r}\times B_{c}} (pointwise), ℓ i ( j ) = e m i j − 1 − m i ( j ) ​ ℓ i ( j − 1 ) + rowsum ⁡ ( 𝐏 ~ i ( j ) ) ∈ ℝ B r \ell_{i}^{(j)}=e^{m_{i}^{j-1}-m_{i}^{(j)}}\ell_{i}^{(j-1)}+\mathrm{rowsum}(\tilde{\mathbf{P}}_{i}^{(j)})\in\mathbb{R}^{B_{r}} , E i ( j ) = e m i j − 1 − m i ( j ) ​ E i ( j − 1 ) + rowreducexlogx ⁡ ( 𝐏 ~ i ( j ) ) ∈ ℝ B r E_{i}^{(j)}=e^{m_{i}^{j-1}-m_{i}^{(j)}}E_{i}^{(j-1)}+\mathrm{rowreducexlogx}(\tilde{\mathbf{P}}_{i}^{(j)})\in\mathbb{R}^{B_{r}} . 10: On chip, compute 𝐎 i ( j ) = diag ​ ( e m i ( j − 1 ) − m i ( j ) ) − 1 ​ 𝐎 i ( j − 1 ) + 𝐏 ~ i ( j ) ​ 𝐕 j \mathbf{O}_{i}^{(j)}=\mathrm{diag}(e^{m_{i}^{(j-1)}-m_{i}^{(j)}})^{-1}\mathbf{O}_{i}^{(j-1)}+\tilde{\mathbf{P}}_{i}^{(j)}\mathbf{V}_{j} . 11: end for 12: On chip, compute 𝐎 i = diag ​ ( ℓ i ( T c ) ) − 1 ​ 𝐎 i ( T c ) \mathbf{O}_{i}=\mathrm{diag}(\ell_{i}^{(T_{c})})^{-1}\mathbf{O}_{i}^{(T_{c})} . 13: On chip, compute E i = E i ( T c ) ​ ( ℓ i ( T c ) ) − 1 + log ⁡ ( ( ℓ i ( T c ) ) − 1 ) E_{i}=E_{i}^{(T_{c})}(\ell_{i}^{(T_{c})})^{-1}+\log((\ell_{i}^{(T_{c})})^{-1}) . 14: On chip, compute L i = m i ( T c ) + log ⁡ ( ℓ i ( T c ) ) L_{i}=m_{i}^{(T_{c})}+\log(\ell_{i}^{(T_{c})}) . 15: Write 𝐎 i \mathbf{O}_{i} to HBM as the i i -th block of 𝐎 \mathbf{O} . 16: Write E i E_{i} to HBM as the i i -th block of E E . 17: end for 18: Return the output 𝐎 \mathbf{O} and the entropy E E .

[148] h3: A.5 Theoretical Analysis of ToProVAR

[149] p: We present a theoretical derivation of the average-case error upper bounds for the tri-dimensional greedy optimization strategy (Scale → \rightarrow Layer → \rightarrow Token) used in ToProVAR . All derivations follow the notation and formulae in the main paper, in particular the entropy-based statistics in Equations (2)–(6). Our goal is to show that, under mild assumptions, each stage introduces a bounded error that depends only on a small residual fraction of entropy/importance, so that the overall error remains controlled.

[150] h4: A.5.1 Scale-Level Error Bound

[151] p: We first model generation across scales as an additive refinement process. Let 𝐙 \mathbf{Z} denote the full-resolution representation, and let 𝐙 s \mathbf{Z}_{s} be the representation after completing scale s s , defined recursively as

[152] table: 𝐙 s = 𝐙 s − 1 + Δ 𝐙 s , s = 1 , … , S max , 𝐙 0 = 𝟎 , \mathbf{Z}_{s}=\mathbf{Z}_{s-1}+\Delta\mathbf{Z}_{s},\quad s=1,\dots,S_{\text{max}},\quad\mathbf{Z}_{0}=\mathbf{0}, (8)

[153] p: where Δ ​ 𝐙 s \Delta\mathbf{Z}_{s} captures the residual details introduced when moving from scale s − 1 s-1 to s s . If we stop refinement at the pruned scale D D (determined by the low-entropy ratio ρ s \rho_{s} in Eq. (3)), the pruned representation is

[154] table: 𝐙 D = 𝐙 − ∑ s = D + 1 S max Δ ​ 𝐙 s , \mathbf{Z}_{D}\;=\;\mathbf{Z}-\sum_{s=D+1}^{S_{\text{max}}}\Delta\mathbf{Z}_{s}, (9)

[155] p: and the scale-level approximation error is

[156] table: E scale = ‖ 𝐙 − 𝐙 D ‖ 2 2 = ‖ ∑ s = D + 1 S max Δ ​ 𝐙 s ‖ 2 2 . E_{\text{scale}}=\|\mathbf{Z}-\mathbf{Z}_{D}\|_{2}^{2}=\Big\|\sum_{s=D+1}^{S_{\text{max}}}\Delta\mathbf{Z}_{s}\Big\|_{2}^{2}. (10)

[157] p: Let 𝒮 pruned = { s ∣ D < s ≤ S max } \mathcal{S}_{\text{pruned}}=\{\,s\mid D<s\leq S_{\text{max}}\,\} be the set of pruned scales. Under a standard average-case assumption that the increments Δ ​ 𝐙 s \Delta\mathbf{Z}_{s} are approximately uncorrelated across s s , we obtain

[158] table: 𝔼 ⁡ [ E scale ] ≈ ∑ s ∈ 𝒮 pruned 𝔼 ⁡ [ ‖ Δ ​ 𝐙 s ‖ 2 2 ] . \mathbb{E}[E_{\text{scale}}]\;\approx\;\sum_{s\in\mathcal{S}_{\text{pruned}}}\mathbb{E}\big[\|\Delta\mathbf{Z}_{s}\|_{2}^{2}\big]. (11)

[159] p: Empirically, the energy ‖ Δ ​ 𝐙 s ‖ 2 2 \|\Delta\mathbf{Z}_{s}\|_{2}^{2} is complementary to the low-entropy ratio ρ s \rho_{s} in Eq. (3): scales with a smaller ρ s \rho_{s} retain more high-entropy (less salient) mass and therefore tend to contribute larger residual updates. We model this as

[160] table: 𝔼 ⁡ [ ‖ Δ ​ 𝐙 s ‖ 2 2 ] ∝ ( 1 − ρ s ) , \mathbb{E}\big[\|\Delta\mathbf{Z}_{s}\|_{2}^{2}\big]\;\propto\;(1-\rho_{s}), (12)

[161] p: and denote F s = 𝔼 ⁡ [ ‖ Δ ​ 𝐙 s ‖ 2 2 ] F_{s}=\mathbb{E}\big[\|\Delta\mathbf{Z}_{s}\|_{2}^{2}\big] as the expected energy contributed by scale s s , with total energy F = ∑ s = 1 S max F s = 𝔼 ⁡ [ ‖ 𝐙 ‖ 2 2 ] F=\sum_{s=1}^{S_{\text{max}}}F_{s}=\mathbb{E}\big[\|\mathbf{Z}\|_{2}^{2}\big] .

[162] p: Following the scale-depth localization in Sec. 4 , we use a low-entropy threshold τ \tau to decide where to truncate the refinement. Specifically, D D is chosen as the smallest scale index such that the low-entropy ratio drops below the threshold,

[163] table: D = min ⁡ { s ∣ ρ s ≤ τ } , D\;=\;\min\,\{\,s\mid\rho_{s}\leq\tau\,\}, (13)

[164] p: and we prune all subsequent scales s > D s>D . In practice, τ \tau is obtained by a light-weight pre-sampling procedure, and we find that a single value τ ≈ 0.4 \tau\approx 0.4 works robustly across prompts and resolutions.

[165] p: Empirically, ρ s \rho_{s} is approximately non-increasing for s ≥ D s\geq D , so all pruned scales satisfy ρ s ≤ ρ D ≤ τ \rho_{s}\leq\rho_{D}\leq\tau for s ∈ 𝒮 pruned s\in\mathcal{S}_{\text{pruned}} . Therefore

[166] table: 𝔼 ⁡ [ E scale ] \displaystyle\mathbb{E}[E_{\text{scale}}] ≈ ∑ s = D + 1 S max F s ≤ ∑ s = D + 1 S max ( 1 − ρ s ) ​ F s ⋅ 1 1 − ρ D \displaystyle\approx\sum_{s=D+1}^{S_{\text{max}}}F_{s}\;\leq\;\sum_{s=D+1}^{S_{\text{max}}}(1-\rho_{s})\,F_{s}\cdot\frac{1}{1-\rho_{D}} ≤ ( 1 − ρ D ) ​ ∑ s = D + 1 S max F s 1 − ρ D ≤ ( 1 − ρ D ) ​ F . \displaystyle\leq\;(1-\rho_{D})\sum_{s=D+1}^{S_{\text{max}}}\frac{F_{s}}{1-\rho_{D}}\;\leq\;(1-\rho_{D})\,F. (7)

[167] p: Since ρ D ≤ τ \rho_{D}\leq\tau and τ \tau is fixed by pre-sampling, Eq. (7) shows that the average scale-level error is controlled by the chosen low-entropy threshold: when the refinement is truncated, only scales whose residual entropy mass is regulated by τ \tau are dropped.

[168] h4: A.5.2 Layer-Level Error Bound

[169] p: At a fixed scale s s , the decoder consists of L L stacked layers. Let 𝐡 ℓ ( s ) \mathbf{h}_{\ell}^{(s)} denote the hidden representation after layer ℓ \ell :

[170] table: 𝐡 0 ( s ) = 𝐙 s , 𝐡 ℓ ( s ) = f ℓ ( 𝐡 ℓ − 1 ( s ) ) , ℓ = 1 , … , L . \mathbf{h}_{0}^{(s)}=\mathbf{Z}_{s},\quad\mathbf{h}_{\ell}^{(s)}=f_{\ell}\big(\mathbf{h}_{\ell-1}^{(s)}\big),\quad\ell=1,\dots,L. (14)

[171] p: We define the layer-wise residual contribution as

[172] table: Δ ℓ ( s ) = 𝐡 ℓ ( s ) − 𝐡 ℓ − 1 ( s ) , \Delta_{\ell}^{(s)}=\mathbf{h}_{\ell}^{(s)}-\mathbf{h}_{\ell-1}^{(s)}, (15)

[173] p: so that the full output at scale s s can be expressed as

[174] table: 𝐡 L ( s ) = 𝐡 0 ( s ) + ∑ ℓ = 1 L Δ ℓ ( s ) . \mathbf{h}_{L}^{(s)}=\mathbf{h}_{0}^{(s)}+\sum_{\ell=1}^{L}\Delta_{\ell}^{(s)}. (16)

[175] p: Let ℒ pruned \mathcal{L}_{\text{pruned}} be the set of pruned layers at scale s s , and ℒ keep \mathcal{L}_{\text{keep}} the retained ones. The pruned output (after removing layers in ℒ pruned \mathcal{L}_{\text{pruned}} ) is

[176] table: 𝐡 L ( s , pruned ) = 𝐡 0 ( s ) + ∑ ℓ ∈ ℒ keep Δ ℓ ( s ) , \mathbf{h}_{L}^{(s,\text{pruned})}=\mathbf{h}_{0}^{(s)}+\sum_{\ell\in\mathcal{L}_{\text{keep}}}\Delta_{\ell}^{(s)}, (17)

[177] p: and the layer-level error is

[178] table: E layer ( s ) = ‖ 𝐡 L ( s ) − 𝐡 L ( s , pruned ) ‖ 2 2 = ‖ ∑ ℓ ∈ ℒ pruned Δ ℓ ( s ) ‖ 2 2 . E_{\text{layer}}^{(s)}=\big\|\mathbf{h}_{L}^{(s)}-\mathbf{h}_{L}^{(s,\text{pruned})}\big\|_{2}^{2}=\Big\|\sum_{\ell\in\mathcal{L}_{\text{pruned}}}\Delta_{\ell}^{(s)}\Big\|_{2}^{2}. (18)

[179] p: Assuming that the residuals { Δ ℓ ( s ) } \{\Delta_{\ell}^{(s)}\} are approximately orthogonal across layers in expectation, we have

[180] table: 𝔼 ⁡ [ E layer ( s ) ] ≈ ∑ ℓ ∈ ℒ pruned 𝔼 ⁡ [ ‖ Δ ℓ ( s ) ‖ 2 2 ] . \mathbb{E}[E_{\text{layer}}^{(s)}]\;\approx\;\sum_{\ell\in\mathcal{L}_{\text{pruned}}}\mathbb{E}\big[\|\Delta_{\ell}^{(s)}\|_{2}^{2}\big]. (19)

[181] p: Based on our layer-level analysis (Sec. 4 ), each layer at scale s s is assigned a representation score ℛ ( ℓ , s ) \mathcal{R}^{(\ell,s)} computed from the principal component ratio of its attention-entropy map (Eq. (4)): Global Layers have ℛ ( ℓ , s ) → 0 \mathcal{R}^{(\ell,s)}\to 0 , while Detail Layers have ℛ ( ℓ , s ) → 1 \mathcal{R}^{(\ell,s)}\to 1 . Let

[182] table: G s = 𝔼 ⁡ [ ‖ 𝐡 L ( s ) ‖ 2 2 ] , Z s = ∑ ℓ = 1 L ℛ ( ℓ , s ) , G_{s}=\mathbb{E}\big[\|\mathbf{h}_{L}^{(s)}\|_{2}^{2}\big],\quad Z_{s}=\sum_{\ell=1}^{L}\mathcal{R}^{(\ell,s)}, (20)

[183] p: and model the expected contribution of each layer as a normalized fraction of G s G_{s} ,

[184] table: 𝔼 ⁡ [ ‖ Δ ℓ ( s ) ‖ 2 2 ] ≈ ℛ ( ℓ , s ) Z s ​ G s . \mathbb{E}\big[\|\Delta_{\ell}^{(s)}\|_{2}^{2}\big]\approx\frac{\mathcal{R}^{(\ell,s)}}{Z_{s}}\,G_{s}. (21)

[185] p: By design, our greedy strategy prunes only Detail Layers (with large ℛ ( ℓ , s ) \mathcal{R}^{(\ell,s)} ) and keeps Global Layers (with ℛ ( ℓ , s ) ≈ 0 \mathcal{R}^{(\ell,s)}\approx 0 ). Substituting the above model into the error expression gives

[186] table: 𝔼 ⁡ [ E layer ( s ) ] \displaystyle\mathbb{E}[E_{\text{layer}}^{(s)}] ≈ ∑ ℓ ∈ ℒ pruned ℛ ( ℓ , s ) Z s ​ G s \displaystyle\approx\sum_{\ell\in\mathcal{L}_{\text{pruned}}}\frac{\mathcal{R}^{(\ell,s)}}{Z_{s}}\,G_{s} = ∑ ℓ ∈ ℒ pruned ℛ ( ℓ , s ) Z s ​ G s ≡ γ s ​ G s , \displaystyle=\frac{\sum_{\ell\in\mathcal{L}_{\text{pruned}}}\mathcal{R}^{(\ell,s)}}{Z_{s}}\,G_{s}\;\equiv\;\gamma_{s}\,G_{s}, (8)

[187] p: where

[188] table: γ s = ∑ ℓ ∈ ℒ pruned ℛ ( ℓ , s ) ∑ ℓ = 1 L ℛ ( ℓ , s ) ∈ [ 0 , 1 ] \gamma_{s}=\frac{\sum_{\ell\in\mathcal{L}_{\text{pruned}}}\mathcal{R}^{(\ell,s)}}{\sum_{\ell=1}^{L}\mathcal{R}^{(\ell,s)}}\in[0,1] (22)

[189] p: measures the fraction of the layer representation score that is discarded at scale s s . Since Global Layers contribute negligibly to ℛ ( ℓ , s ) \mathcal{R}^{(\ell,s)} and are always retained, γ s \gamma_{s} remains small in practice, and the average layer-level error at scale s s is linearly controlled by γ s \gamma_{s} through Eq. (8).

[190] h4: A.5.3 Token-Level Error Bound

[191] p: After determining scales and layers, token pruning operates within the remaining Detail layers using entropy-based gating. Let 𝐭 i \mathbf{t}_{i} be the token vector at index i i , and let w i = H ^ i ( l , s ) w_{i}=\widehat{H}_{i}^{(l,s)} be its normalized entropy-based importance (Eq. (5)), satisfying ∑ i w i = 1 \sum_{i}w_{i}=1 . Let 𝒯 keep \mathcal{T}_{\text{keep}} and 𝒯 pruned \mathcal{T}_{\text{pruned}} denote the sets of kept and pruned tokens, respectively.

[192] p: The full token energy is

[193] table: H = ∑ i = 1 N ‖ 𝐭 i ‖ 2 2 , H=\sum_{i=1}^{N}\|\mathbf{t}_{i}\|_{2}^{2}, (23)

[194] p: and the token-level error introduced by pruning is

[195] table: E token = ∑ i ∈ 𝒯 pruned ‖ 𝐭 i ‖ 2 2 . E_{\text{token}}=\sum_{i\in\mathcal{T}_{\text{pruned}}}\|\mathbf{t}_{i}\|_{2}^{2}. (24)

[196] p: Assuming that token energy is approximately proportional to importance, i.e.,

[197] table: 𝔼 ⁡ [ ‖ 𝐭 i ‖ 2 2 ] ≈ w i ​ H , \mathbb{E}\big[\|\mathbf{t}_{i}\|_{2}^{2}\big]\approx w_{i}\,H, (25)

[198] p: we obtain the average-case bound

[199] table: 𝔼 ⁡ [ E token ] ≈ H ​ ∑ i ∈ 𝒯 pruned w i . \mathbb{E}[E_{\text{token}}]\;\approx\;H\sum_{i\in\mathcal{T}_{\text{pruned}}}w_{i}. (26)

[200] p: Define the pruned importance mass

[201] table: γ = ∑ i ∈ 𝒯 pruned w i , \gamma=\sum_{i\in\mathcal{T}_{\text{pruned}}}w_{i}, (27)

[202] p: which measures how much normalized entropy mass is discarded. Then

[203] table: 𝔼 ⁡ [ E token ] ≤ γ ​ H . \mathbb{E}[E_{\text{token}}]\leq\gamma\,H. (9)

[204] p: In our design, the gating function q i ​ ( s , l ) q_{i}(s,l) (Eq. (6)) and the range [ α min , α max ] [\alpha_{\min},\alpha_{\max}] jointly enforce that high-importance (low-entropy) tokens are kept and that each region preserves at least an α min \alpha_{\min} fraction of tokens. This makes γ \gamma significantly smaller than the raw token sparsity ratio and keeps E token E_{\text{token}} small.

[205] h4: A.5.4 Total Error and Safety

[206] p: Finally, we combine the contributions from the three stages. Since the scale-, layer-, and token-level errors affect different structural components and pruning is applied in a nested manner (scale first, then layers, then tokens within selected layers), it is reasonable in the average case to treat these error terms as approximately additive:

[207] table: 𝔼 ⁡ [ E total ] ≤ 𝔼 ⁡ [ E scale ] + ∑ s 𝔼 ⁡ [ E layer ( s ) ] + 𝔼 ⁡ [ E token ] . \mathbb{E}[E_{\text{total}}]\;\leq\;\mathbb{E}[E_{\text{scale}}]+\sum_{s}\mathbb{E}[E_{\text{layer}}^{(s)}]+\mathbb{E}[E_{\text{token}}]. (28)

[208] p: Using the bounds from Eqs. (7)–(9), we obtain the global bound

[209] table: 𝔼 ⁡ [ E total ] ≤ ( 1 − ρ D ) ​ F + ∑ s γ s ​ G s + γ ​ H . \mathbb{E}[E_{\text{total}}]\;\leq\;(1-\rho_{D})\,F+\sum_{s}\gamma_{s}G_{s}+\gamma H. (10)

[210] p: Here ρ D \rho_{D} is the low-entropy ratio at the truncation scale D D , γ s \gamma_{s} is the discarded layer-level representation fraction at scale s s , and γ \gamma is the discarded token-level importance mass.

[211] p: In our safe operating regime, the threshold τ \tau and the gating parameters [ α min , α max ] [\alpha_{\min},\alpha_{\max}] are selected such that the empirical residual fractions γ s \gamma_{s} and γ \gamma remain small (see Sec. 4 and Appendix X for empirical ranges). The nested structure further prevents cross-stage amplification: token pruning is only applied after conservative scale- and layer-level decisions, and all three stages include fallback conditions (e.g., no scale pruning if the empirical ρ s \rho_{s} profile does not cross the threshold τ \tau , no layer pruning when the Global/Detail classification is ambiguous, and a minimum per-region token keep ratio).

[212] p: In summary, while the tri-stage strategy is greedy and heuristic, the entropy-based quantities ( ρ s , ℛ ( ℓ , s ) , H ^ i ( l , s ) ) (\rho_{s},\mathcal{R}^{(\ell,s)},\widehat{H}_{i}^{(l,s)}) and the associated thresholds ( τ , α min , α max ) (\tau,\alpha_{\min},\alpha_{\max}) induce explicit average-case error upper bounds in each dimension, clarifying why errors do not compound in the operating regime used in our experiments.

[213] h3: A.6 Limitations and Future Work

[214] p: Despite the promising acceleration and quality preservation results, ToProVAR has several limitations that suggest important directions for future work.

[215] h5: Limitations

[216] p: Architecture Dependency. The framework fundamentally relies on the attention mechanism and the derived attention entropy for semantic analysis, limiting its direct applicability to non-Transformer-based generative models.

[217] p: Parameter Sensitivity. Optimal performance requires manual tuning of the proportion of low-entropy tokens, which hinders truly adaptive and zero-configuration deployment.

[218] h5: Future Work

[219] p: Online Adaptive Control. We will explore RL to learn to dynamically predict optimal pruning strategy.

[220] p: Efficient video generation and editing. We plan to extend the framework to V-VAR models, achieving efficient 4D semantic projection by incorporating temporal saliency. Furthermore, the fine-grained semantic map might be leveraged for high-efficiency local image/video editing .

[221] h2: Instructions for reporting errors

[222] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[223] p: Tip: You can select the relevant text first, to include it in your report.

[224] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[225] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
