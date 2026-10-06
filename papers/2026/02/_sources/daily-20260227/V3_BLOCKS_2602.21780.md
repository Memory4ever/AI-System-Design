[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: XStreamVGGT : Extremely Memory-Efficient Streaming Vision Geometry Grounded Transformer with KV Cache Compression

[3] h6: Abstract

[4] p: Learning-based 3D visual geometry models have significantly advanced with the advent of large-scale transformers. Among these, StreamVGGT leverages frame-wise causal attention to deliver robust and efficient streaming 3D reconstruction. However, it suffers from unbounded growth in the Key-Value (KV) cache due to the massive influx of vision tokens from multi-image and long-video inputs, leading to increased memory consumption and inference latency as input frames accumulate. This ultimately limits its scalability for long-horizon applications. To address this gap, we propose XStreamVGGT, a tuning-free approach that seamlessly integrates pruning and quantization to systematically compress the KV cache, enabling extremely memory-efficient streaming inference. Specifically, redundant KVs generated from multi-frame inputs are initially pruned to conform to a fixed KV memory budget using an efficient token-importance identification mechanism that maintains full compatibility with high-performance attention kernels (e.g., FlashAttention). Additionally, leveraging the inherent distribution patterns of KV tensors, we apply dimension-adaptive KV quantization within the pruning pipeline to further minimize memory overhead while preserving numerical accuracy. Extensive evaluations show that XStreamVGGT achieves mostly negligible performance degradation while substantially reducing memory usage by 4.42 × \times and accelerating inference by 5.48 × \times , enabling practical and scalable streaming 3D applications. The code is available at https://github.com/ywh187/XStreamVGGT/ .

[5] h2: 1 Introduction

[6] p: Recovering 3D geometric structures from image sequences has long been a fundamental challenge in 3D computer vision [ 21 ] . This task is crucial for numerous real-world applications, such as robotics, augmented reality, and autonomous driving [ 20 , 10 , 6 ] . For years, 3D vision has been dominated by classical methods, primarily structure-from-motion (SfM) [ 1 , 11 , 32 ] and multi-view stereo (MVS) [ 14 , 12 ] . While these methods demonstrate strong performance in high-fidelity geometric optimization, they rely on fragmented multi-stage pipelines that incur substantial processing delays. Such pipelines are also susceptible to cascading errors, potentially compromising the accuracy and integrity of the final reconstruction. In recent years, learning-based feed-forward models have revolutionized this field.

[7] figure: Figure 1 : Efficiency analysis on a single 80GB A100 GPU. As the number of input frames increases, StreamVGGT and VGGT exhibit significant FPS degradation and rapidly encounter out-of-memory (OOM) errors. In contrast, XStreamVGGT consistently delivers significantly higher frames per second (FPS) without encountering OOM issues.

[8] p: Models such as DUSt3R, CUT3R, and VGGT [ 29 , 31 , 30 ] have shifted the paradigm from conventional approaches to end-to-end deep learning frameworks, showcasing not only remarkable performance but also impressive generalization across diverse datasets. As a significant milestone in this evolution, the Visual Geometry-Grounded Transformer (VGGT) consolidates multiple 3D vision tasks within a unified framework, consistently surpassing task-specific methods across a broad spectrum of applications, including dense depth estimation, point map regression, and camera pose prediction [ 29 ] . To support robust streaming applications, StreamVGGT [ 40 ] replaces the global attention mechanism in Alternative-Attention of VGGT with frame-wise causal attention, following a design philosophy similar to autoregressive large language models (LLMs) [ 5 , 4 , 28 ] . This change shifts the model from an offline to an online streaming paradigm, substantially improving practical usability.

[9] p: At the core of StreamVGGT is its reliance on the Key-Value (KV) cache of previous input frames, which functions as an explicit and persistent memory mechanism. However, as streaming inference progresses, the model is exposed to a significant influx of vision tokens from multi-image and long-video inputs. This influx drives the KV cache to expand linearly with the number of input frames, eventually resulting in unbounded growth [ 17 , 15 ] . As illustrated in Figure 1 , memory consumption and inference latency escalate rapidly as input frames accumulate in StreamVGGT. This issue significantly restricts the system’s scalability for long-horizon applications, creating a critical bottleneck for real-world deployment.

[10] p: To address this challenge, we propose XStreamVGGT, a tuning-free approach that seamlessly integrates pruning and quantization to systematically compress the KV cache, enabling highly memory-efficient streaming inference. Specifically, XStreamVGGT first eliminates redundant KV cache from multi-frame inputs through an efficient token importance identification mechanism, pruning the cache to a bounded budget while preserving the first-frame KVs as geometric references [ 29 ] . Furthermore, our analysis reveals pronounced channel-wise outliers in the Key tensors, while the Value tensors exhibit much weaker outlier behavior in StreamVGGT. Leveraging the inherent distribution patterns of KV tensors, we develop a dimension-adaptive KV quantization scheme that incorporates per-channel Key and per-token Value quantization. This quantization scheme is seamlessly integrated into the pruning pipeline, further minimizing memory overhead while maintaining numerical accuracy. Our key contributions can be summarized as follows:

[11] p: We introduce XStreamVGGT, the first method to seamlessly integrate pruning and quantization for systematically compressing the KV cache in StreamVGGT. XStreamVGGT effectively addresses the issue of unbounded growth in KV memory, enabling extremely memory-efficient streaming inference.

[12] p: We conducted a comprehensive analysis of the KV distribution in StreamVGGT, unveiling, for the first time, the distinctive distribution patterns of Key and Value tensors in 3D reconstruction transformer models. By leveraging dimension-adaptive quantization, we effectively mitigate its impact on quantization accuracy.

[13] p: Extensive evaluations on 3D reconstruction, camera pose estimation and depth estimation demonstrate that XStreamVGGT achieves mostly negligible performance degradation, while reducing memory usage by 4.42 × \times and accelerating inference by 5.48 × \times , offering a powerful and scalable solution for efficient streaming 3D applications.

[14] h2: 2 Related Work

[15] h3: 2.1 Learning-Based 3D Reconstruction

[16] p: By implicitly encoding scene priors within their learned parameters, recent neural network-based approaches have substantially advanced the robustness and generalization of 3D vision models, establishing new performance standards across a variety of tasks [ 29 ] . A significant milestone in this progression was DUSt3R [ 31 ] , which demonstrated the direct regression of view-consistent 3D pointmaps from a pair of RGB images, thereby circumventing the traditional requirement for explicit camera calibration. Building on this foundation, CUT3R [ 30 ] introduced a stateful recurrent framework capable of incrementally updating a unified scene representation from a sequential stream of images. Extending this paradigm, TTT3R [ 7 ] incorporates a Test-Time Training (TTT) strategy that dynamically refines memory updates by assessing the alignment confidence between previously encoded states and incoming observations, thereby enhancing generalization over extended sequences. A pivotal advancement was realized with VGGT [ 29 ] , which scales this philosophy within a 1.2 billion-parameter Alternative-Attention transformer architecture. By jointly predicting multiple 3D attributes, VGGT achieves state-of-the-art performance across a comprehensive range of 3D vision tasks. Most recently, StreamVGGT [ 40 ] adapts this powerful model to the demands of online streaming reconstruction. However, its reliance on an unbounded KV cache presents a critical bottleneck, substantially impeding its practical viability and scalability in real-world streaming applications.

[17] h3: 2.2 KV Cache Compression

[18] p: The KV cache facilitates efficient autoregressive inference by storing previously computed Key and Value representations, thereby circumventing the need for redundant recomputation. However, as sequence lengths grow, the KV cache rapidly becomes a critical bottleneck in terms of memory footprint, motivating a substantial body of research on cache compression techniques [ 16 , 27 ] . Existing approaches to KV cache compression can be broadly classified into two main categories: pruning-based and quantization-based methods. KV pruning seeks to reduce memory and computational overhead by selectively discarding past KV entries deemed to have low importance. Importance is typically estimated using criteria such as attention scores, token saliency, or other heuristics [ 36 , 33 ] . In parallel, KV quantization compresses the cache by representing high-precision Key and Value tensors in low-bit formats, thereby reducing storage requirements and memory access costs [ 17 , 25 , 26 , 15 ] . Despite the significant progress made in these areas, existing KV cache compression techniques have primarily been developed for LLMs that operate on textual data. In contrast, KV caches in 3D vision models exhibit spatial and temporal redundancies, presenting greater potential for compression. However, effectively compressing KV caches in the context of 3D vision tasks remains an open and underexplored research challenge.

[19] h2: 3 Methodology

[20] p: In this section, we present XStreamVGGT, with an overview illustrated in Figure 2 . We begin by reviewing the preliminaries of StreamVGGT in Section 3.1 , then present our approach to eliminating multi-frame redundancy through KV cache pruning in Section 3.2 . In Section 3.3 , we analyze the distributional properties of KV tensors in StreamVGGT, which motivate the development of an effective dimension-adaptive KV quantization scheme.

[21] figure: Figure 2 : Overview of XStreamVGGT. Upon receiving a new input frame (Step 1), Queries from the global attention layer are aggregated via average pooling to form a compact representation, which is then matched against the Key to estimate token importance (Step 2). Guided by these Key-derived importance scores, low-importance historical KV pairs are selectively pruned, while KVs from the first frame are explicitly retained to preserve geometric consistency. The remaining high-importance KVs are concatenated with the first-frame KVs and the newly generated KVs from the current frame (Step 3). Following pruning, the KV cache is further compressed using dimension-adaptive quantization, employing per-channel Key quantization and per-token Value quantization to reduce the impact of outlier channels on quantization accuracy (Step 4). This results in a compact KV cache for efficient subsequent updates (Step 5).

[22] h3: 3.1 Preliminaries

[23] p: StreamVGGT is a streaming 4D visual geometry transformer that processes video frames in an online manner, producing per-frame geometry outputs without the need to reprocess the entire history. Given an incoming RGB frame I t ∈ ℝ 3 × H × W I_{t}\in\mathbb{R}^{3\times H\times W} at time step t t , the model first converts it into a sequence of visual tokens F t ∈ ℝ N × C F_{t}\in\mathbb{R}^{N\times C} using a patch embedding network, where N N is the number of image patches and C C is the embedding dimension. In addition to the patch tokens, StreamVGGT prepends a camera token g t ∈ ℝ 1 × C g_{t}\in\mathbb{R}^{1\times C} to encode global camera-related information, which is later decoded by task-specific heads to predict camera parameters. The model also includes R R register tokens r t ∈ ℝ R × C r_{t}\in\mathbb{R}^{R\times C} , which act as auxiliary latent slots to absorb redundant attention responses during transformer processing. Thus, the input token sequence for frame t t consists of the camera token, register tokens, and patch tokens, with a total length of 1 + R + N 1+R+N . This token sequence is fed into a spatio-temporal transformer encoder with L L layers, adopting an Alternating-Attention design [ 29 ] . Each layer first applies frame-wise spatial self-attention to model intra-frame structure, followed by temporal causal attention to aggregate information from past frames under a strict causal constraint.

[24] p: In each transformer layer ℓ \ell , the temporal attention module maintains a KV cache that stores token-level representations from all previous frames:

[25] table: 𝒞 t − 1 ( ℓ ) = { K 1 : t − 1 ( ℓ ) , V 1 : t − 1 ( ℓ ) } , \mathcal{C}^{(\ell)}_{t-1}=\{K^{(\ell)}_{1:t-1},V^{(\ell)}_{1:t-1}\}, (1)

[26] p: where K τ ( ℓ ) , V τ ( ℓ ) ∈ ℝ ( 1 + R + N ) × C K^{(\ell)}_{\tau},V^{(\ell)}_{\tau}\in\mathbb{R}^{(1+R+N)\times C} denote the Key and Value tensors corresponding to all tokens of frame τ \tau . For the current frame, only the Query, Key, and Value tensors Q t ( ℓ ) Q^{(\ell)}_{t} , K t ( ℓ ) K^{(\ell)}_{t} , and V t ( ℓ ) V^{(\ell)}_{t} are newly computed. Temporal attention at layer ℓ \ell is computed as:

[27] table: Attn ( Q t ( ℓ ) , [ K 1 : t − 1 ( ℓ ) , K t ( ℓ ) ] , [ V 1 : t − 1 ( ℓ ) , V t ( ℓ ) ] ) , \mathrm{Attn}\bigl(Q^{(\ell)}_{t},\;[K^{(\ell)}_{1:t-1},K^{(\ell)}_{t}],\;[V^{(\ell)}_{1:t-1},V^{(\ell)}_{t}]\bigr), (2)

[28] p: with a causal mask to prevent access to future frames. After the attention computation, K t ( ℓ ) K^{(\ell)}_{t} and V t ( ℓ ) V^{(\ell)}_{t} are appended to the cache for use in subsequent time steps. The outputs of the final transformer layer are then passed to lightweight, task-specific heads to predict per-frame geometry signals, such as camera parameters, dense point maps, and others.

[29] p: During inference, the size of the Query tensor Q t ( ℓ ) Q^{(\ell)}_{t} remains constant over time, as it depends solely on the tokens of the current frame. In contrast, the Key and Value tensors grow linearly with the number of processed frames due to the accumulation of cached representations. Consequently, the memory cost of temporal attention at each layer increases linearly with the sequence length, making long-duration streaming inference progressively more expensive.

[30] h3: 3.2 Eliminating Multi-Frame Redundancy through KV Cache Pruning

[31] p: Despite the shared use of KV caching, StreamVGGT differs fundamentally from autoregressive LLMs. In LLMs, KV caches are formed from text tokens carrying rich semantic context, whereas in StreamVGGT they originate from visual tokens extracted from video frames. Unlike textual tokens, vision tokens exhibit substantial redundancy due to both intra-frame spatial correlations and inter-frame temporal consistency. As illustrated in Figure 3 , this redundancy manifests as sparse attention patterns across multi-frame inputs, suggesting significant opportunities for cache compression.

[32] p: We propose a query-guided KV cache pruning mechanism to eliminate multi-frame redundancy while retaining the most informative historical tokens within a fixed cache length ℒ max \mathcal{L}_{\text{max}} . The pruning operation is applied independently at each transformer layer. Notably, since the spatio-temporal encoder employs an Alternating-Attention design, only the temporal global attention module maintains a KV cache and is thus subject to pruning. We begin by computing the similarity between the pooled Query tokens of the current frame and each Key token to assess token importance. This approach strikes a balance between using attention scores as a metric for token importance and efficiently computing the attention kernel. Attention scores have been widely used in previous studies to identify token importance [ 36 , 33 ] . However, the attention calculation in StreamVGGT is designed to be compatible with highly optimized, efficient attention kernels (such as FlashAttention [ 9 , 38 ] ), which do not provide intermediate computation results, including attention scores. While repeatedly computing the Q ​ K QK attention scores yields accurate attention scores, it incurs excessive computational cost. By leveraging pooled Query groups for importance identification, we efficiently compute token importance while ensuring compatibility with optimized attention kernels.

[33] figure: (a) The input query frame. (b) Attention heatmaps of previous input frames. Figure 3 : Attention sparsity analysis. The visualization shows attention heatmaps from Layer 14 of StreamVGGT. The visualization of attention heatmaps reveals that attention weights are predominantly concentrated on Query-relevant regions. In contrast, other areas exhibit significantly lower attention, indicating substantial redundancy in the feature representation.

[34] p: Specifically, given the Query Q t ( ℓ ) ∈ ℝ ( 1 + R + N ) × C Q^{(\ell)}_{t}\in\mathbb{R}^{(1+R+N)\times C} of the current frame at layer ℓ \ell , we first separate the special tokens (camera token and register tokens), denoted as Q t , special ( ℓ ) Q^{(\ell)}_{t,\text{special}} , from the ordinary patch tokens Q t , normal ( ℓ ) Q^{(\ell)}_{t,\text{normal}} . The patch tokens are grouped into fixed-size groups of size g g . The pooled Query is then formed as:

[35] table: Q t , pooled ( ℓ ) = concat ​ ( Q t , special ( ℓ ) , GroupAvg ​ ( Q t , normal ( ℓ ) , g ) ) . Q^{(\ell)}_{t,\text{pooled}}=\text{concat}\Big(Q^{(\ell)}_{t,\text{special}},\;\text{GroupAvg}(Q^{(\ell)}_{t,\text{normal}},g)\Big). (3)

[36] p: We further average the pooled Query across all attention heads to obtain:

[37] table: Q ¯ t ( ℓ ) = 1 H ​ ∑ h = 1 H Q t , pooled ( ℓ ) ​ [ h ] ∈ ℝ N pooled × C , \bar{Q}^{(\ell)}_{t}=\frac{1}{H}\sum_{h=1}^{H}Q^{(\ell)}_{t,\text{pooled}}[h]\in\mathbb{R}^{N_{\text{pooled}}\times C}, (4)

[38] p: where N pooled N_{\text{pooled}} denotes the number of tokens after grouping. The grouping size g g is a fixed hyperparameter.

[39] p: Pruning is triggered immediately after the temporal global attention at layer ℓ \ell completes, once the total cache length T T exceeds the budget ℒ max \mathcal{L}_{\text{max}} . Tokens from the first and current frames are always preserved, serving as stable geometric references and up-to-date visual evidence, respectively. Let T first T_{\text{first}} and T current T_{\text{current}} denote the number of tokens corresponding to the first and current frames. The remaining middle segment is subject to pruning: T prunable = T − T first − T current T_{\text{prunable}}=T-T_{\text{first}}-T_{\text{current}} . For the prunable middle tokens, we compute a head-averaged key summary:

[40] table: K ¯ prunable ( ℓ ) = 1 H ∑ h = 1 H K 1 : t − 1 ( ℓ ) [ h , T first : T − T current ] ∈ ℝ T prunable × C . \bar{K}^{(\ell)}_{\text{prunable}}=\frac{1}{H}\sum_{h=1}^{H}K^{(\ell)}_{1:t-1}\bigl[h,\;T_{\text{first}}:T-T_{\text{current}}\bigr]\in\mathbb{R}^{T_{\text{prunable}}\times C}. (5)

[41] p: All token types in the middle frames, including camera, register, and patch tokens, are treated uniformly during pruning. Token importance scores are computed via the inner product between the pooled queries and the prunable keys:

[42] table: S matrix ( ℓ ) = Q ¯ t ( ℓ ) ​ ( K ¯ prunable ( ℓ ) ) ⊤ ∈ ℝ N pooled × T prunable , S^{(\ell)}_{\text{matrix}}=\bar{Q}^{(\ell)}_{t}\left(\bar{K}^{(\ell)}_{\text{prunable}}\right)^{\!\top}\in\mathbb{R}^{N_{\text{pooled}}\times T_{\text{prunable}}}, (6)

[43] p: followed by averaging along the Query dimension:

[44] table: S ( ℓ ) = 1 N pooled ∑ i = 1 N pooled S matrix ( ℓ ) [ i , : ] ∈ ℝ T prunable . S^{(\ell)}=\frac{1}{N_{\text{pooled}}}\sum_{i=1}^{N_{\text{pooled}}}S^{(\ell)}_{\text{matrix}}[i,:]\in\mathbb{R}^{T_{\text{prunable}}}. (7)

[45] p: Based on the resulting importance scores, the top- k k tokens are selected from the prunable middle region. Let ℐ middle \mathcal{I}_{\text{middle}} denote the indices of the selected tokens. The final set of retained tokens is then given by

[46] table: ℐ keep = { 1 , … , T first } ∪ ℐ middle ∪ { T − T current + 1 , … , T } . \mathcal{I}_{\text{keep}}=\{1,\dots,T_{\text{first}}\}\;\cup\;\mathcal{I}_{\text{middle}}\;\cup\;\{T-T_{\text{current}}+1,\dots,T\}. (8)

[47] p: The same indices are synchronously applied to both the Key and Value tensors to maintain consistency. With the proposed pruning strategy, the cache size increases linearly only until reaching the budget ℒ max \mathcal{L}_{\text{max}} , after which it remains fixed. Consequently, the per-frame temporal attention cost transitions from linear growth to a constant upper bound.

[48] figure: (a) Key tensor. (b) Key tensor. (c) Value tensor. (d) Value tensor. Figure 4 : Magnitude distributions of the Key and Value. The Key demonstrates significant channel-wise outliers, with a small subset of channels exhibiting magnitudes substantially larger than the others. In contrast, the distribution of the Value is more uniform, with no prominent outlier behavior.

[49] h3: 3.3 Dimension-Adaptive KV Quantization Based on KV Distribution Characteristics

[50] p: To achieve extreme compression of the KV cache, we leverage the inherent distribution patterns of KV tensors and propose a dimension-adaptive KV quantization scheme. In this work, we adopt the widely used asymmetric uniform quantization scheme [ 17 ] , which is parameterized by a scale factor s s , a zero-point z z , and a bit-width b b . Given a floating-point tensor x ∈ ℝ d x\in\mathbb{R}^{d} , its quantized representation x ^ \hat{x} is computed as

[51] table: x ^ = clamp ⁡ ( ⌊ x s ⌉ + z , 0 , 2 b − 1 ) , \hat{x}=\operatorname{clamp}\left(\left\lfloor\frac{x}{s}\right\rceil+z,\;0,\;2^{b}-1\right), (9)

[52] p: with the scale factor and zero-point defined as

[53] table: s = x max − x min 2 b − 1 , z = ⌊ − x min s ⌉ . s=\frac{x_{\max}-x_{\min}}{2^{b}-1},\qquad z=\left\lfloor-\frac{x_{\min}}{s}\right\rceil. (10)

[54] p: Here, ⌊ ⋅ ⌉ \lfloor\cdot\rceil denotes rounding to the nearest integer, and clamp ⁡ ( ⋅ ) \operatorname{clamp}(\cdot) restricts values to the valid range. The scale factor s s determines the quantization step size, while the zero-point z z ensures that the zero is mapped to the quantized range.

[55] figure: Table 1 : Analysis of quantization errors for per-token and per-channel schemes. The errors are computed based on the Mean Squared Error (MSE) metric with a group size of 64. Bits Per-Token Quantization Per-Channel Quantization Keys INT4 2.007 × 10 − 3 2.007\times 10^{-3} 3.635 × 10 − 4 3.635\times 10^{-4} INT2 5.183 × 10 − 2 5.183\times 10^{-2} 9.181 × 10 − 3 9.181\times 10^{-3} Values INT4 5.035 × 10 − 4 5.035\times 10^{-4} 4.704 × 10 − 4 4.704\times 10^{-4} INT2 2.641 × 10 − 2 2.641\times 10^{-2} 2.190 × 10 − 2 2.190\times 10^{-2}

[56] p: After establishing the basic quantization strategy, we next determine the appropriate quantization granularity (i.e., per-tensor, per-token, or per-channel). A principled understanding of the distributional properties of KV tensors in StreamVGGT is crucial for achieving robust and accurate quantization. We conducted an extensive analysis of the KV distribution in StreamVGGT, revealing the distinct distribution patterns of Keys and Values within 3D reconstruction transformer models. As shown in Figure 4 , the Key tensors exhibit significant channel-wise outliers, a behavior that is much less pronounced in the Value tensors. When applying standard per-tensor or per-token quantization, these outliers dominate the dynamic range, leading to inflated quantization scales and a marked reduction in effective precision, which, in turn, causes substantial performance degradation [ 18 ] .

[57] p: Guided by these observations, we propose a per-channel Key and per-token Value quantization scheme that explicitly addresses channel-wise outliers. As presented in Table 1 , our analysis confirms that this scheme significantly mitigates quantization error. Unlike LLMs, where the KV cache typically expands by a single token at each decoding step, StreamVGGT processes inputs in a frame-wise manner. This frame-wise processing results in a rapid expansion of the KV cache, adding a large number of patch tokens per time step. As a result, StreamVGGT is inherently well-suited for per-channel Key quantization schemes that span multiple tokens. As illustrated in Figure 2 , we tightly couple quantization with pruning. Specifically, quantization is applied to the final KV cache, K ~ ( ℓ ) 1 : t − 1 \tilde{K}^{(\ell)}_{1:t-1} and V ~ ( ℓ ) 1 : t − 1 \tilde{V}^{(\ell)}_{1:t-1} , which comprises both the pruned historical KVs and the preserved KVs from the first and current frames. The quantization is defined as

[58] table: K ^ c = 𝒬 c ​ ( K ~ c , s c K , z c K ) , V ^ t = 𝒬 t ​ ( V ~ t , s t V , z t V ) , \hat{K}_{c}=\mathcal{Q}_{c}\!\left(\tilde{K}_{c};\,s^{K}_{c},\,z^{K}_{c}\right),\qquad\hat{V}_{t}=\mathcal{Q}_{t}\!\left(\tilde{V}_{t};\,s^{V}_{t},\,z^{V}_{t}\right), (11)

[59] p: where c c and t t denote channel and token indices, respectively, and s c K , z c K s^{K}_{c},z^{K}_{c} (for Keys) and s t V , z t V s^{V}_{t},z^{V}_{t} (for Values) are the corresponding scale and zero-point parameters. Here, 𝒬 c ​ ( ⋅ ) \mathcal{Q}_{c}(\cdot) and 𝒬 t ​ ( ⋅ ) \mathcal{Q}_{t}(\cdot) denote asymmetric uniform quantization along the channel and token dimensions, respectively. During attention computation, the quantized tensors are dequantized as

[60] table: K ~ c = 𝒟 ​ 𝒬 c ​ ( K ^ c , s c K , z c K ) , V ~ t = 𝒟 ​ 𝒬 t ​ ( V ^ t , s t V , z t V ) , \tilde{K}_{c}=\mathcal{DQ}_{c}\!\left(\hat{K}_{c};\,s^{K}_{c},\,z^{K}_{c}\right),\qquad\tilde{V}_{t}=\mathcal{DQ}_{t}\!\left(\hat{V}_{t};\,s^{V}_{t},\,z^{V}_{t}\right), (12)

[61] p: where 𝒟 ​ 𝒬 c ​ ( ⋅ ) \mathcal{DQ}_{c}(\cdot) and 𝒟 ​ 𝒬 t ​ ( ⋅ ) \mathcal{DQ}_{t}(\cdot) denote the dequantization operators.

[62] figure: Table 2 : 3D reconstruction comparison on NRGBD dataset. NRGBD Acc ↓ \downarrow Comp ↓ \downarrow NC ↑ \uparrow Method Inference Type Mean Med. Mean Med. Mean Med. VGGT Offline Unbounded Memory 0.079 0.020 0.083 0.023 0.909 0.989 StreamVGGT Online Unbounded Memory 0.085 0.044 0.079 0.038 0.862 0.986 XStreamVGGT (Ours) Online Bounded Memory 0.085 0.049 0.075 0.038 0.850 0.986

[63] figure: Table 3 : 3D reconstruction comparison on 7-Scenes dataset. 7 Scenes Acc ↓ \downarrow Comp ↓ \downarrow NC ↑ \uparrow Method Inference Type Mean Med. Mean Med. Mean Med. VGGT Offline Unbounded Memory 0.085 0.038 0.089 0.039 0.786 0.889 StreamVGGT Online Unbounded Memory 0.132 0.058 0.116 0.042 0.749 0.863 XStreamVGGT (Ours) Online Bounded Memory 0.142 0.068 0.125 0.048 0.734 0.848

[64] figure: Table 4 : Camera pose estimation. TUM ScanNet Method Inference Type ATE ↓ \downarrow RPE trans ↓ \downarrow RPE rot ↓ \downarrow ATE ↓ \downarrow RPE trans ↓ \downarrow RPE rot ↓ \downarrow VGGT Offline Unbounded Memory 0.053 0.032 3.209 0.157 0.056 3.635 StreamVGGT Online Unbounded Memory 0.062 0.033 3.208 0.160 0.057 3.688 XStreamVGGT (Ours) Online Bounded Memory 0.068 0.035 3.184 0.171 0.061 3.837

[65] h2: 4 Experiments

[66] h3: 4.1 Experimental Details

[67] p: We perform a comprehensive evaluation of XStreamVGGT, encompassing benchmark performance, efficiency analysis, ablation studies, and qualitative results. XStreamVGGT is first assessed on various 3D tasks, including 3D reconstruction, camera pose estimation and depth estimation. Following the Point3R protocol [ 34 ] , input images are processed with variable aspect ratios and resized to ensure the maximum edge length does not exceed 518 pixels. For pruning, the pooling size is set to 16, and the cache length is set to 2K, ensuring that at least the first and current frames are preserved. KV quantization is performed using KIVI with INT4 and a group size of 64 [ 17 ] . Remarkably, even with a cache length of only 2K and additional quantization, XStreamVGGT achieves exceptional efficiency while maintaining robust performance, with negligible loss across most tasks compared to the more expensive full-KV-length StreamVGGT [ 40 ] .

[68] figure: Table 5 : Monocular depth estimation. Sintel Bonn KITTI Method Inference Type Abs Rel ↓ \downarrow δ {\delta} <1.25 ↑ \uparrow Abs Rel ↓ \downarrow δ {\delta} <1.25 ↑ \uparrow Abs Rel ↓ \downarrow δ {\delta} <1.25 ↑ \uparrow VGGT Offline Unbounded Memory 0.274 67.4 0.054 97.2 0.071 94.1 StreamVGGT Online Unbounded Memory 0.254 68.5 0.052 97.1 0.072 94.7 XStreamVGGT Online Bounded Memory 0.254 68.5 0.052 97.1 0.072 94.7

[69] figure: Table 6 : Video depth evaluation. Sintel Bonn KITTI Method Inference Type Abs Rel ↓ \downarrow δ {\delta} <1.25 ↑ \uparrow Abs Rel ↓ \downarrow δ {\delta} <1.25 ↑ \uparrow Abs Rel ↓ \downarrow δ {\delta} <1.25 ↑ \uparrow VGGT Offline Unbounded Memory 0.301 68.3 0.057 96.8 0.061 97.0 StreamVGGT Online Unbounded Memory 0.328 65.8 0.058 97.2 0.094 94.4 XStreamVGGT Online Bounded Memory 0.341 61.9 0.073 94.3 0.098 94.3

[70] h3: 4.2 3D Reconstruction

[71] p: The 3D reconstruction experiments were conducted on the 7-Scenes [ 22 ] and NRGBD [ 2 ] datasets by measuring the discrepancies between predictions and the corresponding ground-truth point clouds. We adopt Accuracy (Acc), Completion (Comp), and Normal Consistency (NC) as evaluation metrics. Although XStreamVGGT uses bounded memory, it effectively maintains performance across various metrics. As shown in Table 2 , on the NRGBD dataset, XStreamVGGT maintains stable performance across several metrics, with only a slight reduction in the others. NC sees only a slight drop of 1.4% (Mean) and 0.3% (Med) compared to StreamVGGT, demonstrating efficient memory management with minimal trade-offs. As shown in Table 3 , XStreamVGGT demonstrates strong geometric fidelity on the 7-Scenes dataset, achieving a mean NC score of 0.734, which represents only a 2% drop compared to StreamVGGT (0.749).

[72] h3: 4.3 Camera Pose Estimation

[73] p: We evaluate camera pose estimation on the TUM Dynamics [ 24 ] and ScanNet [ 8 ] datasets, truncating all sequences to 90 frames. We report Absolute Translation Error (ATE), Relative Translation Error (RPE trans ), and Relative Rotation Error (RPE rot ) as evaluation metrics. As shown in Table 4 , XStreamVGGT achieves nearly lossless performance on the Sintel dataset, exhibiting only a minimal increase in ATE (0.006) and translational RPE (0.002) compared with StreamVGGT. The change in rotational RPE is even smaller, with an increase of only 0.025 (approximately 0.8%). These minor increases highlight XStreamVGGT’s ability to efficiently manage memory while maintaining nearly identical performance across key metrics.

[74] figure: Table 7 : Ablation study of the pruning and quantization processes in video depth estimation. Sintel Bonn KITTI Method Cache Length Pruning Quantization Abs Rel ↓ \downarrow δ {\delta} <1.25 ↑ \uparrow Abs Rel ↓ \downarrow δ {\delta} <1.25 ↑ \uparrow Abs Rel ↓ \downarrow δ {\delta} <1.25 ↑ \uparrow StreamVGGT Unbounded w/o w/o 0.358 61.1 0.080 96.5 0.198 69.0 XStreamVGGT 2K w/ w/o 0.343 61.4 0.067 94.9 0.224 58.0 XStreamVGGT 2K w/ w/ 0.341 61.9 0.073 94.3 0.206 63.9

[75] h3: 4.4 Depth Estimation

[76] p: Following Monst3R [ 37 ] , we evaluate monocular and video depth estimation performance on the Sintel [ 3 ] , Bonn [ 19 ] , and KITTI [ 13 ] datasets, which encompass a diverse range of dynamic and static, indoor and outdoor scenes. The evaluation metrics include Absolute Relative Error (Abs Rel) and δ < 1.25 \delta<1.25 (the percentage of predicted depths within a 1.25 factor of the ground-truth depth). For monocular depth estimation, the results in Table 5 demonstrate that XStreamVGGT fully preserves the performance of StreamVGGT, yielding no observable degradation in any evaluation metric. For video depth estimation, as shown in Table 5 and 6 , XStreamVGGT experiences mostly negligible performance degradation with a 2K cache length. Although the relative drop on Bonn is more noticeable due to its exceptionally strong baseline, XStreamVGGT still achieves very high absolute performance (0.073 Abs Rel). In contrast to StreamVGGT, which faces significant GPU memory surges and ultimately runs into Out of Memory (OOM) issues as the number of input frames increases, XStreamVGGT maintains a consistent GPU memory usage and achieves nearly 6x speedup with lossless results.

[77] h3: 4.5 Ablation Study

[78] p: Figure 5(a) presents an ablation study on cache length, with lengths varying across 2K, 4K, 6K, and 8K. As shown, performance changes minimally as cache length increases, suggesting significant redundancy among multi-frame patch tokens. A cache length of 2K provides strong performance while maintaining high efficiency, making it the optimal choice. Additionally, we conduct an ablation study on both the pruning and quantization processes of XStreamVGGT to assess their individual effects. As indicated in Table 7 , although pruning causes a slight performance decline, quantization introduces no additional degradation.

[79] figure: (a) Ablation study of cache length. (b) Analysis of memory. Figure 5 : Ablation study of cache length and analysis of memory with increasing frame length.

[80] h3: 4.6 Efficiency Analysis

[81] p: We evaluate the efficiency of XStreamVGGT using input sequences ranging from 50 to 1000 frames, measuring GPU memory consumption and inference speed. All experiments are conducted on a single 80GB A100 GPU. As shown in Figures 1 and 5(b) , both StreamVGGT and VGGT exhibit significant FPS degradation as the number of input frames increases and quickly encounter OOM errors. By contrast, XStreamVGGT consistently maintains substantially higher FPS without OOM, yielding significant efficiency gains with 4.42X lower memory usage and 5.48X faster inference compared with StreamVGGT.

[82] h3: 4.7 Qualitative Results

[83] p: Figures 6 and 7 present visual comparisons of 3D reconstruction and depth estimation results between StreamVGGT and XStreamVGGT. As shown, XStreamVGGT effectively preserves visual quality, producing results that closely match the original while delivering a notable improvement in computational efficiency.

[84] h2: 5 Conclusion

[85] p: We present XStreamVGGT, a tuning-free method for memory-efficient streaming inference of StreamVGGT. By combining KV cache pruning with quantization, it bounds memory growth while preserving model fidelity. Extensive experiments demonstrate minimal performance loss alongside substantial reductions in memory footprint and inference latency, enabling scalable 3D streaming applications. Future work will explore adaptive cache budgets that dynamically adjust based on scene complexity and motion characteristics.

[86] figure: (a) StreamVGGT. (b) XStreamVGGT (ours). (c) StreamVGGT. (d) XStreamVGGT (ours). (e) StreamVGGT. (f) XStreamVGGT (ours). (g) StreamVGGT. (h) XStreamVGGT (ours). (i) StreamVGGT. (j) XStreamVGGT (ours). Figure 6 : Qualitative reconstruction results comparing StreamVGGT and XStreamVGGT.

[87] figure: (a) StreamVGGT. (b) XStreamVGGT (ours). (c) StreamVGGT. (d) XStreamVGGT (ours). (e) StreamVGGT. (f) XStreamVGGT (ours). (g) StreamVGGT. (h) XStreamVGGT (ours). (i) StreamVGGT. (j) XStreamVGGT (ours). (k) StreamVGGT. (l) XStreamVGGT (ours). (m) StreamVGGT. (n) XStreamVGGT (ours). Figure 7 : Qualitative depth estimation results comparing StreamVGGT and XStreamVGGT.

[88] h2: 6 Acknowledgments

[89] p: This work was supported in part by the Research Grants Council of the Hong Kong Special Administrative Region Government through the TRS project T45-701/22-R and GRF project 17203224, and the TCL Corporate Research (Hong Kong) Co., Limited.

[90] h2: References

[91] h2: Instructions for reporting errors

[92] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[93] p: Tip: You can select the relevant text first, to include it in your report.

[94] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[95] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
