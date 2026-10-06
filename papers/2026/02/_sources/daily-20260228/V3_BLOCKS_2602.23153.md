[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Efficient Encoder-Free Fourier-based 3D Large Multimodal Model

[3] h6: Abstract

[4] p: Large Multimodal Models (LMMs) that process 3D data typically rely on heavy, pre-trained visual encoders to extract geometric features. While recent 2D LMMs have begun to eliminate such encoders for efficiency and scalability, extending this paradigm to 3D remains challenging due to the unordered and large-scale nature of point clouds. This leaves a critical unanswered question: How can we design an LMM that tokenizes unordered 3D data effectively and efficiently without a cumbersome encoder? We propose Fase3D, the first efficient encoder-free F ourier-b ase d 3D scene LMM. Fase3D tackles the challenges of scalability and permutation invariance with a novel tokenizer that combines point cloud serialization and the Fast Fourier Transform (FFT) to approximate self-attention. This design enables an effective and computationally minimal architecture, built upon three key innovations: First, we represent large scenes compactly via structured superpoints. Second, our space-filling curve serialization followed by an FFT enables efficient global context modeling and graph-based token merging. Lastly, our Fourier-augmented LoRA adapters inject global frequency-aware interactions into the LLMs at a negligible cost. Fase3D achieves performance comparable to encoder-based 3D LMMs while being significantly more efficient in computation and parameters. Project website: https://tev-fbk.github.io/Fase3D .

[5] h2: 1 Introduction

[6] figure: Figure 1 : Fase3D’s contribution overview. Mainstream 3D LMMs are based on computationally-heavy scene encoders to extract geometric features before alignment with the LLM. In contrast, our method (Fase3D) employs a lightweight Fourier-based tokenizer to process raw point clouds directly and introduces Fourier-augmented LoRA adapters, which infuse global frequency-aware context into the LLM without additional computational overhead.

[7] p: A typical practice in Large Multimodal Models (LMMs) involves using pre-trained vision encoders ( e.g . , CLIP [ 48 ] or Sparse 3D U-Net [ 11 ] ) to extract high-level visual semantics, which are then translated into the language model’s embedding space [ 23 , 30 ] . These encoders are effective, but impose substantial computational overhead and limit input flexibility. To improve scalability and efficiency, recent works on 2D LMMs have explored vision encoder-free architectures, such as EVE/EVEv2 [ 12 , 13 ] and Mono-InternVL [ 28 ] . Although constructing these models is challenging due to the lack of large-scale vision pre-training, specialized modules, such as visual experts [ 28 ] or modality-aware components [ 13 ] , have enabled encoder-free designs to approach the performance of encoder-based counterparts. Moreover, despite this progress in the 2D domain, encoder-free 3D LLMs remain largely unexplored. A direct transfer is unviable because, unlike the regular grid of pixels, point clouds are an unordered set of points, requiring specialized permutation-invariant operators [ 33 ] or serialization techniques [ 45 ] . Following the recent trend toward encoder-free multimodal learning, this raises a critical question: how can we design encoder-free 3D LMMs that operate directly on point clouds while remaining both effective and efficient? Designing such encoder-free models demands addressing unique 3D challenges. Since vision encoder-free architectures lack traditional pre-training, they must incorporate explicit inductive bias to robustly tokenize the inherent unordered nature of point clouds. This specialized tokenizer must have minimal learnable parameters for efficiency. Furthermore, given the arbitrary length and massive scale of point clouds, the overall LMMs architecture must be computationally and memory efficient.

[8] p: In this paper, we introduce an efficient, encoder-free Fourier-based 3D LMM, named Fase3D, that effectively processes scene-level point clouds. Fase3D introduces a novel interaction by viewing token processing as a synthesis between the spatial and frequency domains. This dual-domain aggregation effectively captures global and local semantic and geometric information while inherently reducing complexity by approximating self-attention. Its core mechanisms are point cloud serialization [ 45 ] and the Fast Fourier Transform (FFT), which together yield a highly effective and efficient tokenizer. FFT is a powerful operator that can approximate self-attention and aggregate global context while being computationally efficient [ 16 ] . We leverage frequency domain processing across several stages of our pipeline. We first apply FFT to precomputed, serialization-based geometry superpoints to generate context-aware candidate tokens. We then introduce a sparse graph-based token merging formulation that adaptively reduces the token set, significantly lowering GPU cost. Lastly, we propose a novel method for training the LLM by augmenting LoRA layers [ 18 ] in the frequency domain of low-pass filtered input tokens. We evaluate our method on 3D dense captioning and question answering. With much fewer visual parameters activated, Fase3D achieves comparable performance to state-of-the-art approaches, like LL3DA [ 6 ] and PerLA [ 30 ] , on ScanQA [ 2 ] , SQA3D [ 29 ] , ScanRefer [ 5 ] , and Nr3D [ 1 ] .

[9] p: To summarize, our main contributions are:

[10] p: We present Fase3D , the first encoder-free 3D LMM that eliminates dedicated 3D encoders and instead integrates superpoint tokenization, positional encoding, and FFT-based augmentation into a standard LLM.

[11] p: We propose a FFT context enhancer that leverages space-filling curves (SFCs) to enable efficient frequency-domain mixing and compact token merging.

[12] p: We introduce an efficient sparse k k NN superpoint-graph construction based on space-filling curve ranking, providing a structured yet lightweight representation.

[13] p: We design a Fourier-augmented LoRA adapter that enriches the LLM’s internal layers with global context modeling at negligible computational and parameter cost, preserving the monolithic philosophy.

[14] h2: 2 Related Work

[15] p: Encoder-based 3D LMMs. Early work on 3D vision and language understanding rely on specialized geometric feature extractors to bridge spatial structure and semantics. For Visual Question Answering (VQA), ScanQA [ 2 ] proposed a baseline by pairing point-cloud features with text via dedicated encoders. Subsequent methods focused on cross-modal fusion and unified tasks: 3D-LLM [ 17 ] introduced pre-training to strengthen cross-attention among point clouds, images, and text. Chat-3D [ 42 ] embeds segmented 3D objects into LLM-interpretable tokens. LL3DA [ 6 ] and PerLA [ 30 ] unified captioning, QA, and grounding by coupling a point encoder with Q-Former adapters for alignment. To tackle large scene understanding, methods like LSceneLLM [ 51 ] and MICAS [ 39 ] were proposed, using techniques such as adaptive region selection, scene magnification, and multi-grained sampling for improved detail capture and efficient grounding. Other approaches, such as DAC [ 43 ] , offer a simpler CLIP+MLLM recipe for open-set 3D object retrieval. In parallel, many works extend the popular 2D LLaVA [ 26 ] architecture: 3D-LLaVA [ 11 ] and Point-LLaVA [ 47 ] integrate 3D encoders aligned via instruction tuning for open-vocabulary QA and grounding. Similarly, methods like LISA [ 20 ] and SceneLLM [ 15 ] , LLaVA-3D [ 52 ] , and SceneVerse [ 44 ] lift 2D priors (like mask proposals) into the 3D domain for holistic scene understanding. While these methods establish strong baselines, their dependence on computationally expensive encoders constrains input resolution and scalability. Moreover, their resulting feature embeddings often remain semantically misaligned with the reasoning capabilities of LLMs [ 40 ] . Most existing systems still require dedicated 3D encoders or projection modules to process geometric information effectively.

[16] p: Encoder-free LMMs. Recent advances in monolithic 2D architectures, which integrate perception and reasoning within a single decoder-only Transformer, have inspired a shift toward encoder-free Large Multimodal Models (LMMs). Examples include SOLO [ 7 ] , Fuyu-8B [ 4 ] , EVE/EVEv2 [ 12 , 13 ] , and Mono-InternVL [ 28 ] . These models eliminate modality-specific vision backbones by mapping visual inputs directly into the LLM’s token space through lightweight projections. Extending this paradigm to 3D data is non-trivial: point clouds are large, sparse, and unordered, making naïve serialization computationally expensive and permutation-variant, which disrupts instance coherence and global context modeling. Early explorations demonstrate the feasibility of encoder-light designs for object-level reasoning under instruction tuning. ENEL [ 40 ] adopts a lightweight hierarchical tokenization strategy to reduce reliance on heavy vision Transformers in ShapeLLM [ 34 ] and PointLLM [ 46 ] . However, these approaches still struggle to scale to full scenes and capture long-range, cross-instance dependencies. Our work directly targets these limitations by making encoder-free 3D modeling practical for scene-level reasoning, addressing the challenges of token ordering, scalability, and global context integration.

[17] h2: 3 Fase3D

[18] figure: Figure 2 : The Fase3D pipeline. A lightweight tokenizer ( ∙ \bullet ) produces M M superpoint tokens, which are refined by an FFT-based context enhancer ( ∙ \bullet ). A graph is then constructed, and a token-merging block ( ∙ \bullet ) compresses the tokens into T T compact 3D tokens ( T < M T<M ). Finally, an LLM ( ∙ \bullet ) with an FFT-based global filter ( ∙ \bullet ) processes these tokens together with textual and user prompts.

[19] p: Fase3D is a vision encoder-free LMM that relies on a specialized tokenizer to abstract input point clouds into a set of tokens for a decoder-only LLM [ 48 ] . Fase3D is designed to be parameter- and compute-efficient. It progressively reduces the input token count while enhancing their semantic and spatial information (Fig. 2 ). We first compute point-level features with a lightweight multi-layer perceptron (MLP) that capture only local context and partition the point cloud into M M superpoints via geometric clustering [ 21 ] (§ 3.1 ). We then average-pool the features within each superpoint to obtain candidate 3D tokens. We serialize the superpoints and employ the Fast Fourier Transform (FFT) on the sequence to further encapsulate contextual information. This FFT-based context enhancer applies low-pass filtering to capture context (§ 3.2 ). We formulate a graph information merging strategy to further aggregate semantic and spatial information into T T clusters ( T < M T<M ), resulting in the final T T visual tokens of 3D scence (§ 3.3 ). These tokens, together with the text and user prompts, are fed into a prompt embedding (§ 3.4 ) whose outputs serve as inputs to the LLM. Lastly, we enrich global context by training Fourier-augmented LoRA adapters on the low-pass filtered tokens in the frequency domain (§ 3.5 ).

[20] h3: 3.1 Superpoint-based token initialization

[21] p: To reduce the number of input tokens for the LLM, we employ geometric clustering and produce superpoints [ 30 ] . We use average pooling to aggregate information from neighboring points into a corresponding superpoint embedding [ 36 , 11 ] . Specifically, let 𝒫 = { ( 𝐩 i , 𝐟 i ) } i = 1 N \mathcal{P}{=}\{(\mathbf{p}_{i},\mathbf{f}_{i})\}_{i=1}^{N} be the input point cloud, where 𝐩 i \mathbf{p}_{i} ∈ \in ℝ N × 3 \mathbb{R}^{N\times 3} are the 3D coordinates and 𝐟 i \mathbf{f}_{i} ∈ \in ℝ N × C i ​ n \mathbb{R}^{N\times C_{in}} are additional features ( e.g . color and normal). 𝒫 \mathcal{P} is partitioned into M M superpoints 𝒬 \mathcal{Q} centered at 𝒞 = { c i } i = 1 M \mathcal{C}{=}\{c_{i}\}_{i=1}^{M} via geometric clustering [ 21 ] , where c i ∈ ℝ 3 c_{i}\in\mathbb{R}^{3} are the centers. For each superpoint, we compute a token of dimension d d . Specifically, we first tokenize 𝒫 \mathcal{P} into 𝐗 ( 0 ) ∈ ℝ N × d \mathbf{X}^{(0)}\in\mathbb{R}^{N\times d} . For each point 𝐩 i \mathbf{p}_{i} , we project 𝐟 i \mathbf{f}_{i} into a d d -dimensional feature via a shallow learnable multilayer perceptron (MLP), yielding the token 𝐱 f ​ e ​ a ​ t ( 0 ) ∈ ℝ N × d \mathbf{x}^{(0)}_{feat}\in\mathbb{R}^{N\times d} . In parallel, we encode 𝐩 i \mathbf{p}_{i} using a non-parametric Fourier feature embedding of varying frequencies, obtaining 𝐱 c ​ o ​ o ​ r ( 0 ) ∈ ℝ N × d \mathbf{x}^{(0)}_{coor}\in\mathbb{R}^{N\times d} . We obtain the point-level token 𝐱 ( 0 ) = 𝐱 f ​ e ​ a ​ t ( 0 ) + 𝐱 c ​ o ​ o ​ r ( 0 ) \mathbf{x}^{(0)}{=}\mathbf{x}^{(0)}_{feat}+\mathbf{x}^{(0)}_{coor} . Lastly, we derive the superpoint-level tokens 𝒮 ∈ ℝ M × d \mathcal{S}\in\mathbb{R}^{M\times d} by average pooling their associated point-level tokens:

[22] table: 𝒮 = SptPool ​ ( 𝐗 ( 0 ) , 𝒬 ) ∈ ℝ M × d , 𝒞 ∈ ℝ M × 3 , \mathcal{S}=\text{SptPool}(\mathbf{X}^{(0)},\mathcal{Q})\in\mathbb{R}^{M\times d},\quad\mathcal{C}\in\mathbb{R}^{M\times 3}, (1)

[23] p: where SptPool stands for superpoint based average pooling.

[24] h3: 3.2 Fourier-based context enhancer

[25] p: Since the initialized superpoint tokens 𝒮 \mathcal{S} only capture local information, we designed a lightweight, parameter-free token enhancer module that injects global context by operating in the frequency domain [ 16 ] . Prior “frequency” methods typically use either (i) voxel/grid-based 3D FFT, which is costly at scene scale, or (ii) Graph Fourier Transform ( e.g . , PointGST [ 24 ] ) that requires explicit graph construction and Laplacian operations ( O ⁡ ( M 2 ) O(M^{2}) ). In contrast, we first serialize the superpoints [ 45 ] into a 1D sequence for the FFT. The FFT, with complexity O ⁡ ( M ​ log ⁡ M ) O(M\log M) over M M tokens, enables the attenuation of high-frequency components, retaining a small band of low frequencies that capture global layout ( e.g . , object groupings). The inverse FFT (iFFT) then produces a spatially varying global context field that is fused back into the original tokens via residual addition. This design enriches each token with both local and global context, promoting long-range reasoning. To mitigate ordering bias from a single sequence, we adopt multi-curve serialization with varied axis orderings to diversify 1D adjacencies.

[26] p: Token serialization. We serialize tokens to apply FFT. Specifically, we linearize 𝒞 \mathcal{C} into a locality-preserving 1D sequence using SFCs [ 45 , 37 ] , centering on four representatives (denoted as π = { π i } i \pi=\{\pi_{i}\}_{i} ): the z-order curve, transpose z-order curve, Hilbert curve and the transpose Hilbert curve. We can reorder the superpoint tokens 𝒮 \mathcal{S} into a 1D sequence 𝒮 ⁡ [ π i ] \mathcal{S}[\pi_{i}] where 3D locality is preserved.

[27] p: FFT-based token enhancer. We use the Discrete Cosine Transform (DCT), a variant of Fourier transform that generates real values, to aggregate context information [ 16 ] . The DCT can be implemented with the FFT operator. Let ℱ \mathcal{F} and ℱ − 1 \mathcal{F}^{-1} denote the 1D FFT and its inverse applied along the token axis, respectively. Please refer to the Supp. Mat. for more details about FFT. For each curve traversal π i \pi_{i} , we transform the sorted tokens to select low/high bands by

[28] table: 𝒮 ′ ​ ( π i ) = iFFT ​ ( FFT ​ ( 𝒮 ⁡ ( π i ) ) ⊙ G ) , \mathcal{S}^{\prime}\left(\pi_{i}\right)=\text{iFFT}\left(\text{FFT}\left(\mathcal{S}\left(\pi_{i}\right)\right)\odot G\right), (2)

[29] p: where G G is a learnable non-negative gate that keeps the first K L K_{L} low-frequency bins. ⊙ \odot denotes element-wise multiplication. To obtain position-aware mixing, we apply ( 2 ) to overlapping windows of length L w L_{w} and stride L s L_{s} on 𝒮 ⁡ ( π i ) \mathcal{S}\left(\pi_{i}\right) , and reconstruct by overlap–add with squared-Hann weights. This yields localized low/high-frequency aggregation while remaining O ⁡ ( L w ​ log ⁡ L w ) O(L_{w}\log L_{w}) per window. We process all traversals π i ∈ π \pi_{i}\in\pi . We map them back with the inverse permutations and fuse via uniform averaging:

[30] table: 𝒮 ~ = 1 | π | ​ ∑ π i 𝒮 ′ ​ ( π i ) . \tilde{\mathcal{S}}=\frac{1}{|\pi|}\sum_{\pi_{i}}\mathcal{S}^{\prime}\left(\pi_{i}\right). (3)

[31] p: We fuse the enhancement with a residual as 𝒮 ← 𝒮 + 𝒮 ~ \mathcal{S}\leftarrow\mathcal{S}+\tilde{\mathcal{S}} .

[32] h3: 3.3 Graph-based token merging

[33] p: To achieve reliable dense captioning and boost computational efficiency, we reduce the token count by generating superpoints that tend to maximally encompass whole objects. This allows us to bypass the typical (additional) detection stage used by other 3D LMMs [ 11 , 30 ] , which often rely on learned mask proposals like those from Mask3D [ 38 ] . Instead, we accomplish token reduction by clustering the initial superpoints 𝒮 \mathcal{S} into T T final clusters. Note that, unlike the learned masks used in Mask3D, our superpoints are purely geometric-based; however, as shown in our results, they suffice for good performance.

[34] p: We model superpoints and their relationships as a graph, utilizing both the superpoint tokens (nodes) and their spatial relationships (edges) to promote semantically- and spatially-informed coherence. We construct a single and sparse superpoint graph 𝒢 = ( 𝒱 , ℰ ) \mathcal{G}=(\mathcal{V},\mathcal{E}) at point cloud 𝒫 \mathcal{P} level. This graph is computed once and serves as the topological prior for the merging stage. Vertices 𝒱 \mathcal{V} correspond to the M M superpoints, and edges ℰ \mathcal{E} capture geometric relationships.

[35] p: Neighbor searching via window voting. Building a graph from a point cloud using Delaunay triangulation is typical, but can take a long time for large point clouds [ 36 ] . Instead, we connect superpoints via a point-level window-voting scheme along 1D orderings induced by SFCs. Analogous to our superpoint serialization, we serialize all points into four SFC traversals, which avoids explicit radius or k k -NN queries. For each curve, we scan the sorted index list and sample anchor positions p p with stride r r . Let i i be the point index at the window’s center, and let j j be the point index for any other position q ∈ 𝒲 ⁡ ( p ) q\in\mathcal{W}(p) . Let s i s_{i} and s j s_{j} denote the superpoint indices points i i and j j are assigned to, respectively. If both points belong to valid superpoints and these superpoints are different ( s i ≠ s j s_{i}\neq s_{j} ), we cast a vote for the edge ( s i , s j ) (s_{i},s_{j}) as v s i , s j ← v s i , s j + 1 v_{s_{i},s_{j}}\leftarrow v_{s_{i},s_{j}}+1 . Aggregating these votes across all curves yields a sparse set of superpoint pairs with integer vote counts, which defines the graph’s adjacency.

[36] p: Graph-based token merging. We introduce a token merging module to further reduce the number of tokens to T T ( T < M T<M ). This module fuses the global feature context from the serialized sequence 𝒮 \mathcal{S} with the local graph topology 𝒢 \mathcal{G} , resulting in a final set of tokens that are both compact and rich in both global and local feature information.

[37] p: We compute a spatially-aware spectral embedding. Using the graph 𝒢 \mathcal{G} (with adjacency A A and degree D D ), we compute the symmetrically normalized adjacency matrix A ^ = D − 1 / 2 A D − 1 / 2 \hat{A}=D^{-1/2}AD^{-1/2} . Since 𝒢 \mathcal{G} is built from k k -nearest neighbors, A ^ \hat{A} is a large but highly sparse matrix, allowing us to leverage efficient sparse matrix operators ( e.g . , torch.sparse in PyTorch) to save significant GPU memory during computation. This smoothing step is defined as Y = A ^ ​ ( 𝒮 − mean ​ ( 𝒮 ) ) Y=\hat{A}(\mathcal{S}-\text{mean}(\mathcal{S})) , where Y Y represents the neighborhood-smoothed, mean-centered features. We then apply a low-rank Singular Value Decomposition (SVD), denoted ϕ \phi , to Y Y to find its r r principal components. This parameter-free embedding, Z emb = U r ​ Σ r Z_{\text{emb}}=U_{r}\Sigma_{r} , captures the principal dimensions of variation across the graph-filtered features.

[38] p: Next, we compute differentiable soft assignments. This requires few learnable parameters: a linear layer W proj ∈ ℝ r × T W_{\text{proj}}\in\mathbb{R}^{r\times T} and an MLP to compute superpoint importance. The r r -dimensional embedding Z emb ∈ ℝ M × r Z_{\text{emb}}{\in}\mathbb{R}^{M\times r} is projected to T T cluster logits, Z emb ​ W proj ∈ ℝ M × T Z_{\text{emb}}W_{\text{proj}}\in\mathbb{R}^{M\times T} . Simultaneously, we apply an MLP on 𝒮 \mathcal{S} to learn an importance score vector μ ∈ ℝ M \mu{\in}\mathbb{R}^{M} . Then, we obtain a soft assignment matrix P ∈ ℝ M × T P{\in}\mathbb{R}^{M\times T} by solving an entropy-regularized optimal transport (OT) [ 32 ] problem. The problem is to find a matrix P P that minimizes the transport cost while satisfying marginal constraints:

[39] table: min P ∈ Π ⁡ ( μ , ν ) − ⟨ P , Z emb ​ W proj ⟩ + τ ​ H ​ ( P ) , \min_{P\in\Pi(\mu,\nu)}-\langle P,Z_{\text{emb}}W_{\text{proj}}\rangle+\tau H(P), (4)

[40] p: where ⟨ ⋅ , ⋅ ⟩ \langle\cdot,\cdot\rangle is the Frobenius inner product. H ⁡ ( P ) H(P) is the entropy of P P , which encourages “soft” assignments. τ \tau is a temperature parameter controlling the softness. Π ( μ , ν ) = { P ∈ ℝ + M × T ∣ P 𝟏 T = μ , P T 𝟏 M = ν } \Pi(\mu,\nu)=\{P\in\mathbb{R}_{+}^{M\times T}\mid P\mathbf{1}_{T}{=}\mu,\;P^{T}\mathbf{1}_{M}{=}\nu\} is the set of all valid transport plans. The marginal μ \mu is our learned importance score. The marginal ν \nu is typically a uniform distribution over the T T target tokens ( e.g . , ν = 𝟏 T / T \nu{=}\mathbf{1}_{T}/T ). This problem can be solved efficiently using the Sinkhorn algorithm [ 32 ] . This matrix P P represents the soft probability of each input token i i belonging to a new merged token k k . Finally, we perform token aggregation. The new T T tokens is formed by a differentiable weighted average (soft-pooling) of the M M original tokens, using P P as the pooling weights. We aggregate both the features 𝒮 \mathcal{S} and their 3D centers 𝒞 \mathcal{C} computing Z ′ = P T ​ 𝒮 Z^{\prime}{=}P^{T}\mathcal{S} and 𝒞 ′ = P T ​ 𝒞 \mathcal{C}^{\prime}=P^{T}\mathcal{C} . The resulting T T tokens Z ′ ∈ ℝ T × d Z^{\prime}\in\mathbb{R}^{T\times d} and their corresponding 3D centers 𝒞 ′ ∈ ℝ T × 3 \mathcal{C}^{\prime}{\in}\mathbb{R}^{T\times 3} form the final, compact sequence that is fed directly to the LLM.

[41] h3: 3.4 Prompt embedding

[42] p: In tasks such as dense object captioning or center-object question answering, the language instruction may include explicit coordinates, instances, or bounding boxes. To handle such inputs, we introduce a 3D coordinate token that enables the model to incorporate spatial cues into its reasoning process. Concretely, we encode the input coordinates (or box/instance centers) together with their k k -nearest neighbors using a Fourier positional encoding layer [ 6 ] . The resulting coordinate tokens are concatenated with the 3D patch tokens and text tokens before being fed into the LLM. This design enables coordinate-aware 3D perception and reasoning.

[43] h3: 3.5 Fourier-augmented LoRA adapter for LLM

[44] p: While LoRA provides a parameter-efficient method for adapting the linear feed-forward network (FFN) layers, the representations Z ′ ∈ ℛ T × D Z^{\prime}\in\mathcal{R}^{T\times D} fed into them are generated by the frozen, pre-trained backbone. These representations are not explicitly optimized for the downstream task, which can limit the potential of the LoRA updates. We propose to enhance these representations by introducing a lightweight Global Filter Module (GFM) . The goal is to enrich the token features with globally-mixed information, thus providing a more robust and adaptive input to the LoRA-adapted layers. Our GFM is inspired by the efficiency of Fourier transforms for global mixing [ 22 , 35 ] . It operates on each token z ∈ ℛ D z\in\mathcal{R}^{D} within the sequence Z ′ Z^{\prime} . Specifically, we first project the feature vector into the frequency domain, apply a learnable filter, and then project back to compute the mixed representation as z mixed = iFFT ​ ( FFT ​ ( z ) ⊙ M ) z_{\text{mixed}}=\text{iFFT}(\text{FFT}(z)\odot M) , where FFT and iFFT are applied along the channel dimension D D . M ∈ ℛ D M\in\mathcal{R}^{D} is a learnable parameter vector that acts as the filter. The final enhanced feature z out z_{\text{out}} fed into the LoRA-adapted layer is then computed as an averaged residual connection as z out = ( z + z mixed ) / 2 z_{\text{out}}=(z+z_{\text{mixed}})/2 . This blending of the original and filtered representations provides a rich, globally-aware input to the FFN while maintaining a stable learning dynamic. This module remains highly efficient, introducing only D D learnable parameters (the filter M M ). We adopt a multi-head formulation with H H heads to reduce the effective computational cost, resulting in O ⁡ ( D H ​ log ⁡ D H ) O\left(\tfrac{D}{H}\log\tfrac{D}{H}\right) complexity.

[45] h3: 3.6 Training

[46] p: We adopt a two-stage training strategy inspired by [ 30 , 11 ] : First, we perform general 3D instruction tuning, then we specialize the model on downstream tasks.

[47] p: Language modeling loss. For 3D scene–text pairs, we optimize caption generation with next-token cross-entropy, following the standard LLM setup:

[48] table: ℒ LM = − 1 ∑ t m t ∑ t m t log p θ ( w t ∣ w < t ) , \mathcal{L}_{\mathrm{LM}}=-\frac{1}{\sum_{t}m_{t}}\sum_{t}m_{t}\,\log p_{\theta}\!\big(w_{t}\mid w_{<t}\big), (5)

[49] p: where p θ p_{\theta} is the model’s token distribution, m t = 1 [ t ≥ t 0 ] m_{t}={1}[t\geq t_{0}] masks out non-caption prefix/prompt tokens, and t 0 t_{0} indexes the first caption token. Padding tokens are ignored via m t m_{t} .

[50] p: Datasets. During training, we use the ScanNet v2 [ 9 ] portion from the 3DLLM dataset [ 17 ] , which provides 1,201 training and 312 validation reconstructed indoor scenes. For language supervision, we combine four established sources: ScanQA [ 2 ] and SQA3D [ 29 ] for 3D question answering, and ScanRefer [ 5 ] together with Nr3D (ReferIt3D) [ 1 ] for 3D referring expression comprehension/localization. These components jointly define our benchmark, covering both QA and dense captioning. We follow the official train/val splits and report results on the validation set unless otherwise specified. Detailed statistics are in the Supp. Mat. .

[51] h2: 4 Experiments

[52] p: Implementation details. Following [ 6 , 8 ] , we uniformly sample 50k points per scene. Point features are pooled into superpoint tokens, followed by clustering into 256 tokens. In the FFT enhancer, we retain the lowest k=128 modes to inject global context. We use a frozen Qwen2.5-3B-Instruct [ 48 ] language model in float16 , unless otherwise specified. The LoRA configuration is rank r = 768 r{=}768 with scaling α = 768 \alpha{=}768 for the first 8 layers; we will add the remaining details in the revision. We use AdamW [ 27 ] with weight decay 0.1 and cosine decay from 10 − 4 10^{-4} to 1 0 − 6 0^{-6} over ∼ \sim 100k iterations. We train with batch size of 8 for seven days on up to 4 NVIDIA custom Ampere A100 GPU 64GB. For each task, we fine-tune only the parameters for ∼ \sim 30k iterations.

[53] p: Metrics. We follow the evaluation protocol [ 6 , 30 ] to evaluate the quality of output responses. We use the abbreviations C, B-4, M and R for CiDEr [ 41 ] , BLEU-4 [ 31 ] , METEOR [ 3 ] , and Rouge-L [ 25 ] , respectively. We report #Params, indicating the number of parameters activated for 3D scene tokenization, and FLOP as an efficiency measure.

[54] figure: Table 1: Question answering results on ScanQA [ 2 ] , and SQA3D [ 29 ] . #Param/FLOP: number of activated parameters and Floating Point Operation count required for the encoding/tokenization stage. Best result is in bold . Second best result is underlined . Method LLMs #Params ↓ \downarrow FLOP ↓ \downarrow ScanQA (val) SQA3D (test) R ↑ \uparrow M ↑ \uparrow B-4 ↑ \uparrow C ↑ \uparrow EM@1 ↑ \uparrow Encoder-based 3D LMMs with point cloud as inputs LL3DA [ 6 ] OPT-1.3B [ 49 ] 118.87M 40.21 37.31 15.88 13.53 76.79 - PerLA [ 30 ] OPT-1.3B [ 49 ] 119.76M 163.38 39.60 17.44 14.49 78.13 - 3D-LLaVA [ 11 ] Vicuna1.5-7B [ 50 ] 58.26M 37.75 43.10 18.40 17.10 92.60 54.5 Encoder-free 3D LMMs with point cloud as inputs Fase3D Qwen2.5-3B [ 48 ] 10.54M 2.04 42.56 18.24 17.12 90.11 53.9 Fase3D Vicuna1.5-7B [ 50 ] 12.11M 2.09 43.37 18.61 16.87 91.74 54.3

[55] h3: 4.1 Evaluation on 3D question answering (3DQA)

[56] p: 3DQA involves answering free-form questions about a 3D environment. The model provides information about objects, relationships, and attributes within a 3D environment. We benchmark Fase3D on ScanQA [ 2 ] and obtain competitive performance on SQA3D [ 29 ] . Built on ScanNet, ScanQA provides ∼ \sim 41.4k questions across 800 scenes that probe recognition and 3D reasoning. SQA3D augments this with ∼ \sim 20.4k situation descriptions covering 6.8k unique situations from 650 scenes and ∼ \sim 33.4k associated questions, situated, embodied scene understanding. SQA3D augments this with ∼ \sim 20.4k situation descriptions covering 6.8k unique situations from 650 scenes and ∼ \sim 33.4k associated questions, emphasizing situated, embodied scene understanding. We also report results with Vicuna-1.5-7B [ 50 ] for a fair comparison with 3D-LLaVA. Tab. 1 summarizes ScanQA (val) and SQA3D (test) results. Fase3D and 3D-LLaVA’s performances are comparable on both datasets, whereas Fase3D significantly outperforms the other encoder-based baselines. Notably, we achieve these results with fewer vision parameters (#Param: 10.54M–12.11M vs. 58.26M of 3D-LLaVA and ∼ \sim 119M of LL3DA/PerLA) and far lower FLOP count ( ∼ \sim 2.0 vs. 37.75 of 3D-LLaVA, 40.21 of LL3DA, and 163.38 of PerLA).

[57] figure: Figure 3 : Qualitative results and comparisons between Fase3D, PerLA [ 30 ] , and LL3DA [ 6 ] on the ScanQA [ 2 ] dataset.

[58] p: Fig. 3 compares LL3DA [ 6 ] , PerLA [ 30 ] , and Fase3D. In the bathroom scene (left), all methods correctly answer “ What is above the bathroom counter? ” (mirror). For “ What type of dispenser is above the counter? ”, Fase3D focuses on the smaller soap dispenser, while baselines answer towel ; all are considered correct, but ours is semantically more accurate. Yet, all fail on the fine-grained color of the toilet paper rolls, likely due to low texture fidelity and illumination. In the dining scene (right), Fase3D identifies attributes and relationships: it answers “ 2 brown chairs ” to “ What chairs are closest to the plant? ”, correctly identifies the round table , and recovers the chair-fabric colors “ red and black ”, whereas the baselines miss at least one of these.

[59] figure: Table 2 : Dense captioning results on ScanRefer and Nr3D. #Param/FLOP: number of activated parameters and Floating Point Operation count required for the encoding/tokenization stage. Best result in bold . Second best result is underlined . Method w/seg #Params ↓ \downarrow FLOP ↓ \downarrow ScanRefer Nr3D C@0.5 ↑ \uparrow B-4@0.5 ↑ \uparrow M@0.5 ↑ \uparrow R@0.5 ↑ \uparrow C@0.5 ↑ \uparrow B-4@0.5 ↑ \uparrow M@0.5 ↑ \uparrow R@0.5 ↑ \uparrow Encoder-based 3D LMMs LL3DA [ 6 ] ✓ 118.87M 80.43 65.19 36.79 25.97 55.06 51.18 28.75 25.91 56.61 PerLA [ 30 ] ✓ 119.76M 326.76 69.41 38.02 29.07 56.80 55.06 31.24 28.52 59.13 3D-LLaVA [ 11 ] ✓ 58.26M 37.75 78.80 36.90 27.10 57.70 - - - - Encoder-free 3D LMMs Fase3D ✓ 10.54M 2.04 78.14 41.34 27.92 57.63 54.91 30.24 26.48 57.14 Fase3D 70.72 37.83 26.81 56.37 52.89 29.31 26.14 56.41

[60] h3: 4.2 Evaluation on 3D dense captioning

[61] p: 3D dense captioning is object-centric and conditioned on regions. The model localizes object instances and generates fine-grained, attribute-rich descriptions grounded at 3D coordinates. To evaluate Fase3D, we use two proposal variants: with external segmenter Mask3D [ 38 ] (w/seg) and without external segmenter but just our graph-based token-merging proposals (w/o seg). For the variant with our graph-based token-merging proposals, we cluster the superpoint embeddings Z e ​ m ​ b Z_{emb} via k k -means with 48 clusters and derive proposal instances from the resulting clusters for evaluation. We condition the generator with tokens derived from each proposal’s 3D center, and evaluate on ScanRefer [ 5 ] and Nr3D [ 1 ] . Following prior work [ 17 , 6 ] , we report m ​ @ ​ k m@k IoU, where m ∈ { C, B-4, M, R } m{\in}\{\text{C, B-4, M, R}\} and k k is the IoU threshold. For fair comparison, we list models trained with standard per-word cross-entropy and without extra 3D scene pretraining. Tab. 2 shows that Fase3D achieves results comparable to 3D-LLaVA in the same setup with the external segmenter ( w/seg ) on ScanRefer. In the case of w/o seg , Fase3D slightly underperforms 3D-LLaVa, but still maintains similar performance to PerLA. On Nr3D, Fase3D maintains comparable performance to PerLA with the w/seg and w/o seg variants.

[62] p: Fig. 4 compares LL3DA, PerLA and Fase3D on ScanRefer [ 5 ] . In the bedroom scene on the left, Fase3D delivers the most accurate caption for the object in the magenta bounding box, correctly identifying it as a pillow positioned on the “ left side of the bed ”. LL3DA produces a confused description mixing left and right , and PerLA fails to generate any output. In the same scan, all methods correctly recognize the object within the cyan bounding box as a radiator , but only Fase3D accurately describes its color. PerLA emphasizes its shape, while LL3DA omits descriptive details. In the second scene (right), all approaches correctly identify the lamp in the yellow bounding box despite its small size but misinterpret its spatial relation to the bed. For the blue bounding box, Fase3D achieves higher semantic accuracy by identifying the object as a wooden stool , while LL3DA and PerLA describe it less precisely as a small table and a rectangular coffee table , respectively.

[63] figure: Figure 4 : Qualitative comparison between Fase3D, PerLA [ 30 ] , and LL3DA [ 6 ] on the ScanRefer [ 5 ] dataset.

[64] h3: 4.3 Ablation Studies

[65] p: We assess: (i) patch embedding alternatives (raw point tokens vs. superpoint pooling with or without an FFT-based context enhancer), (ii) LoRA with Fourier residuals design, and (iii) the different LLMs fine-tuned. Unless otherwise specified, all models are trained from scratch on ScanQA, under identical optimization and data settings. We report validation results and vary a single factor at a time, keeping all other components fixed to the default configuration. See Supplementary Material for additional ablation studies.

[66] p: Patch embedding choices. We examine how 3D inputs are embedded into tokens for the language head (Qwen2.5-3B). Our pipeline first projects points through a lightweight MLP to point features, then aggregates them via superpoint pooling into superpoint tokens. Tab. 3 ablates three factors: using downsampled raw point tokens ( Point ), adding superpoint pooling ( Superpoint ), and adding our parameter-free FFT-based context enhancer. Superpoint pooling shortens the token sequence by roughly one order of magnitude while improving semantic coherence, yielding +3.66 CIDEr over point-only tokens (76.04 → \rightarrow 79.70). The FFT-based enhancer alone provides +6.93 CIDEr (76.04 → \rightarrow 82.97). Combining both delivers the strongest ablation result ( +10.87 CIDEr; 86.91 total). Training with only raw point tokens is also slower and less stable due to quadratic self-attention. The bottom row reports our full model with additional pretraining , further lifting all metrics on the ScanQA val set.

[67] figure: Table 3: Ablation study of vision embedding modules. Point (downsampled raw point tokens), Superpoint (superpoint pooling), FFT (parameter-free FFT-based context enhancer). Module ScanQA (Validation) Point Superpoint FFT R ↑ \uparrow M ↑ \uparrow B-4 ↑ \uparrow C ↑ \uparrow ✓ 37.03 15.43 13.14 76.04 ✓ ✓ 37.18 16.38 13.96 79.70 ✓ ✓ 39.56 17.03 15.11 82.97 ✓ ✓ ✓ 41.64 17.80 16.70 86.91 Full model with pretraining 42.56 18.24 18.02 90.11

[68] p: LoRA with Fourier residual. We compare (i) single-branch LoRA (vision-only or text-only), (ii) shared LoRA on both branches (sLoRA), (iii) decoupled LoRA per branch (dLoRA), and (iv) dLoRA augmented with a Fourier residual branch (+FFT). On ScanQA (val) with Qwen2.5-3B [ 48 ] , adding a Fourier residual to the vision branch yields the best parameter-efficient results: dLoRA+FFT (vision) improves over dLoRA by +4.38 CIDEr, +1.61 BLEU-4, +0.57 METEOR, and +1.68 ROUGE-L ( Tab. 4 ). However, applying the Fourier residual to both branches reduces the gains on four metrics differently, suggesting frequency-domain cues are most beneficial on the visual pathway. Full end-to-end fine-tuning achieves the highest absolute numbers, but at substantially greater compute and memory; dLoRA+FFT approaches that performance with a fraction of trainable parameters, verifying the effectiveness of our design.

[69] figure: Table 4: Ablation study of LoRA placement and Fourier residual on ScanQA (Validation) [ 2 ] . sLoRA: the vision and text branches share the same LoRA modules. dLoRA: the branches use separate (decoupled) LoRA modules. “+FFT” adds a parallel Fourier residual branch to the indicated branch(es). Module ScanQA (Validation) vision text R ↑ \uparrow M ↑ \uparrow B-4 ↑ \uparrow C ↑ \uparrow LoRA - 36.98 15.37 13.35 76.45 - LoRA 36.49 15.40 13.19 76.21 sLoRA sLoRA 37.34 16.04 12.83 78.24 dLoRA dLoRA 39.96 17.23 15.09 82.53 dLoRA+FFT dLoRA 41.64 17.80 16.70 86.91 dLoRA+FFT dLoRA+FFT 37.54 17.63 15.39 83.64 Full model with pretraining 42.56 18.24 18.02 90.11

[70] figure: Table 5: Question answering results with different LLMs on ScanQA [ 2 ] . #Param/FLOP(G) denote the activated parameters and encoding/tokenization FLOPs. Best results in bold . Method w/enc #Params ↓ \downarrow FLOP ↓ \downarrow ScanQA (val) R ↑ \uparrow M ↑ \uparrow B-4 ↑ \uparrow C ↑ \uparrow OPT-1.3B [ 49 ] LLM LL3DA [ 6 ] ✓ 118.87M 40.21 37.31 15.88 13.53 76.79 PerLA [ 30 ] ✓ 119.76M 163.38 39.60 17.44 14.49 78.13 Fase3D ✗ 9.30M 2.01 40.34 17.63 15.96 86.24 QWen2.5-3B [ 48 ] LLM LL3DA [ 6 ] ✓ 118.87M 40.21 37.24 16.01 14.91 79.18 PerLA [ 30 ] ✓ 119.76M 163.38 39.91 16.08 15.53 81.42 Fase3D ✗ 10.54M 2.04 42.56 18.24 17.12 90.11

[71] p: Different LLMs. We further evaluate Fase3D with different language backbones, including OPT-1.3B [ 49 ] and Qwen2.5-3B [ 48 ] . Here, w/enc denotes variants using a pretrained 3D encoder, while ✗ indicates our encoder-free design that replaces the encoder with a lightweight MLP. As shown in Tab. 5 , Fase3D matches or improves performance while drastically reducing 3D front-end cost. With OPT-1.3B on ScanQA, our encoder-free variant uses only 9.30M parameters and 2.01G FLOPs for encoding/tokenization, versus 118.87M/40.21G for LL3DA and 119.76M/163.38G for PerLA. Despite this reduction, it improves CIDEr from 78.13 to 86.24 ( +8.11 ) and achieves the best ROUGE-L, METEOR, and BLEU-4. With Qwen2.5-3B, the trend remains: our model still uses only 10.54M parameters and 2.04G FLOPs, yet attains the best ScanQA validation performance (R 42.56, M 18.24, B-4 17.12, C 90.11). Overall, Fase3D generalizes well across LLM backbones, and encoder-free designs can match or surpass encoder-based baselines at an order-of-magnitude lower cost.

[72] h2: 5 Conclusions

[73] p: We presented Fase3D, an encoder-free, Fourier-based 3D LMM that addresses the twin challenges of scalability and permutation invariance for point clouds. By compactly representing scenes as structured superpoints, serializing them via SFCs, and applying an FFT-based context enhancer, our tokenizer approximates self-attention efficiently while preserving global context. In the language model head, Fourier-augmented LoRA injects frequency-aware interactions at negligible overhead, enabling strong performance without a heavy geometric backbone. Across experiments and ablations, Fase3D matches or exceeds encoder-based 3D LMMs while substantially reducing computation and parameters. Fase3D inherit the limitation of serialization-based approaches like PTv3 [ 45 ] , that may underperform in non-Euclidean long-range relations in cluttered scenes. Future work includes pretraining on larger and more diverse 3D corpora, adaptive or learned serialization, and integration with other modalities like RGB images.

[74] p: Acknowledgement. This work was supported by PNRR FAIR - Future AI Research (PE00000013).

[75] p: Supplementary Material

[76] p: In this supplementary material, we first present additional ablation studies and qualitative results that further demonstrate the effectiveness and efficiency of Fase3D ( Sec. F ). We then provide additional details of Fase3D to complement the method description in the main paper ( Sec. G ). Next, we elaborate on the computational complexity analysis of our method ( Sec. H ). Finally, we present the datasets used for training and evaluation, together with additional implementation details ( Sec. I ). We use the abbreviations C, B-4, M, and R to denote CIDEr [ 41 ] , BLEU-4 [ 31 ] , METEOR [ 3 ] , and ROUGE-L [ 25 ] , respectively.

[77] h2: F Additional results

[78] h3: F.1 Number of LoRA layers

[79] figure: Table 6: Ablation study on the number of LLM’s LoRA layers. #Layers ScanQA (Validation) R ↑ \uparrow M ↑ \uparrow B-4 ↑ \uparrow C ↑ \uparrow 0 35.93 14.94 13.39 74.03 4 38.27 16.30 13.76 80.04 8 41.64 17.80 16.70 86.91 10 41.51 17.14 16.67 87.05 12 40.47 16.56 15.78 86.40

[80] p: We vary the number of LoRA-inserted layers (0, 4, 8, 10, 12). The largest gain is from 0 → \!\to\! 8 layers (C: +12.9, B4: +3.3, M: +2.9, R: +5.7). With 10 layers, accuracy peaks (C = 87.05), while 8 layers yields the best language metrics (B4/M/R). 12 layers cause worse results, indicating mild overfitting. 8-10 layers offers the best trade-off between QA accuracy and text quality. We use #Layers = 8 to balance computation and accuracy.

[81] h3: F.2 SFC curve count

[82] figure: Table 7: Effect of the number of SFC curves n C n_{C} in multi-curve serialization on ScanQA (val). n C n_{C} R ↑ \uparrow M ↑ \uparrow B-4 ↑ \uparrow C ↑ \uparrow 1 37.42 15.96 14.23 79.06 2 40.49 16.78 15.96 85.64 4 41.64 17.80 16.70 86.91 6 41.72 17.93 17.01 87.14

[83] p: As shown in Tab. 7 , performance on ScanQA improves as the number of SFC curves increases, but largely saturates from n C = 4 n_{C}{=}4 to 6 6 with only marginal gains. We therefore set n C = 4 n_{C}{=}4 to balance accuracy and computational cost.

[84] h3: F.3 Ablation studies on token merging

[85] figure: Table 8: Ablation study on the number of LLM’s input tokens. #Token ScanQA (Validation) R ↑ \uparrow M ↑ \uparrow B-4 ↑ \uparrow C ↑ \uparrow 64 37.96 16.23 14.09 79.53 128 38.21 15.85 14.88 83.92 256 41.64 17.80 16.70 86.91 320 41.73 17.67 16.61 87.20

[86] p: We vary the number of LLM input tokens after merging (64, 128, 256, 320). Accuracy (C) improves with more tokens, with the largest gain up to 256 ( +7.38 C over 64; +2.61 B4; +1.57 M; +3.68 R). Beyond 256, gains saturate: 320 yields a small accuracy uptick (87.20 vs. 86.91) and a negligible ROUGE change (41.73 vs. 41.64), while BLEU-4 and METEOR slightly drop. Overall, 256 tokens provides the best language metrics (B4/M) with near-peak accuracy, offering the best compute–quality trade-off. We set #Tokens = 256 across our experiments.

[87] h3: F.4 Ablation studies on two-stage training

[88] p: Tab. 9 reports the performance of Fase3D under a two-stage setup compared with training from scratch. Two-stage training (generalist pre-training followed by ScanQA [ 2 ] instruction tuning) consistently improves all metrics: R increases from 41.64 to 43.37 ( +1.73 ), M from 17.80 to 18.61 ( +0.81 ), B from 16.70 to 16.87 ( +0.17 ), and C from 86.91 to 91.74 ( +4.83 ). These gains indicate that a generic pre-training stage provides a stronger initialization for downstream ScanQA.

[89] figure: Table 9: Effect of two-stage training on ScanQA validation. Method R ↑ \uparrow M ↑ \uparrow B-4 ↑ \uparrow C ↑ \uparrow Scratch 41.64 17.80 16.70 86.91 w/pretrain 43.37 18.61 16.87 91.74

[90] h3: F.5 Ablation studies on token selection

[91] p: To evaluate how different token selection and merging mechanisms affect both accuracy and token efficiency, we compare three strategies for reducing the number of 3D tokens: (i) farthest point sampling (FPS), (ii) a Q-Former-style cross-attention pooling module, and (iii) our proposed graph clustering–based selector. All variants share the same backbone and are trained from scratch on the ScanQA training set, without any pre-training.

[92] figure: Table 10: Effect of different token selection / merging strategies on ScanQA validation performance. All models are trained from scratch on the ScanQA training split, without any pre-training. Selector R ↑ \uparrow M ↑ \uparrow B-4 ↑ \uparrow C ↑ \uparrow Q-Former 37.52 15.87 14.06 77.41 FPS 39.67 17.10 15.18 82.54 Fase3D 41.64 17.80 16.70 86.91

[93] p: As shown in Tab. 10 , FPS already improves over the Q-Former selector by about +2.1 R, +1.2 M, +1.1 B-4, and +5.1 C, indicating that purely geometric sampling yields stronger 3D language grounding than cross-attention pooling. Our graph clustering–based selector further boosts performance across all metrics, achieving gains of roughly +4.1 R, +1.9 M, +2.6 B-4, and +9.5 C over the Q-Former baseline.

[94] h3: F.6 More qualitative visualizations.

[95] p: Fig. 5 illustrates how we use space-filling curves (SFCs) to efficiently approximate kNN search and construct our curve-based kNN graph. The examples show that our method reliably identifies edges between superpoints that preserve their genuine spatial connectivity.

[96] figure: Figure 5 : Visualization of our SFC-based k k NN graph construction via window voting. We show two representative examples of curve-guided neighbor selection.

[97] p: Fig. 6 compares the space-filling curve (SFC) paths of four variants: Hilbert, transposed Hilbert, Z-order and transposed Z-order. To make their differences easier to inspect, we render four viewpoints for each curve. Although each variant traces the scene with slightly different trajectories. Hilbert-based curves are smoother with fewer long-range jumps. Z-order variants favor more axis-aligned runs, i.e. , they all provide locality-preserving orderings. Including both the standard and transposed variants ensures complementary directional coverage, preventing orientation-specific artifacts and allowing the model to capture structure consistently across different spatial alignments. This motivates our design choice in Fase3D of using all four curves jointly in the FFT-based token enhancer, so that complementary locality patterns are fused into a single spectral representation.

[98] figure: Figure 6 : Comparison of space-filling curves (Hilbert, transposed Hilbert, Z-order, and transposed Z-order) under four views (columns). All four variants produce broadly similar locality-preserving paths, with Hilbert-type curves appearing smoother and Z-order variants exhibiting more axis-aligned segments. Using both the standard and transposed versions provides complementary directional coverage and reduces orientation bias, so in Fase3D we apply the FFT jointly over all four curves.

[99] h2: G Method details

[100] h3: G.1 Fast Fourier Transform

[101] p: For a length- N N real sequence x = ( x n ) n = 0 N − 1 x{=}(x_{n})_{n=0}^{N-1} , the DFT and inverse DFT are:

[102] table: ℱ ​ ( x ) k \displaystyle\mathcal{F}(x)_{k} = ∑ n x n ​ e − i ​ 2 ​ π N ​ k ​ n , \displaystyle=\sum_{n}x_{n}e^{{-i}\frac{2\pi}{N}kn}, (6) ℱ − 1 ​ ( y ) n \displaystyle\mathcal{F}^{-1}(y)_{n} = 1 N ​ ∑ k y k ​ e i ​ 2 ​ π N ​ k ​ n . \displaystyle=\frac{1}{N}\sum_{k}y_{k}e^{i\frac{2\pi}{N}kn}.

[103] p: Real inputs satisfy Hermitian symmetry y N − k = y ¯ k y_{N-k}=\bar{y}_{k} . In implementation, we therefore use the real FFT (rFFT), which stores only the first N / 2 + 1 N/2+1 complex coefficients with the same reconstruction.

[104] h3: G.2 Token serialization

[105] p: Let 𝒞 = { c i } i = 0 M − 1 \mathcal{C}=\{c_{i}\}_{i=0}^{M-1} denote the 3D centers of the superpoints. We first normalize these centers to the scene bounding box and quantize them onto a b b -bit integer grid in [ 0 , 1 ] 3 [0,1]^{3} :

[106] table: c ^ i = ⌊ ( 2 b − 1 ) ​ c i − c min c max − c min ⌋ , \hat{c}_{i}=\big\lfloor(2^{b}-1)\,\frac{c_{i}-c_{\min}}{c_{\max}-c_{\min}}\big\rfloor, (7)

[107] p: where c min , c max ∈ ℝ 3 c_{\min},c_{\max}\in\mathbb{R}^{3} are the minimum and maximum coordinates over all superpoint centers. Thus c ^ i = ( c ^ i x , c ^ i y , c ^ i z ) \hat{c}_{i}=(\hat{c}_{i}^{x},\hat{c}_{i}^{y},\hat{c}_{i}^{z}) has integer coordinates in { 0 , … , 2 b − 1 } 3 \{0,\dots,2^{b}-1\}^{3} . From these quantized coordinates, we compute a 1D key k i = SFC ⁡ ( c ^ i ) k_{i}=\mathrm{SFC}(\hat{c}_{i}) using a space-filling curve ( e.g . , Z-order or Hilbert), which assigns each grid cell with a unique integer index.

[108] h4: Z-order (Morton) index.

[109] p: For the Morton curve, the 1D key is obtained by bit interleaving . Let c ^ i x = ∑ j = 0 b − 1 x j ​ 2 j , c ^ i y = ∑ j = 0 b − 1 y j ​ 2 j , c ^ i z = ∑ j = 0 b − 1 z j ​ 2 j , \hat{c}_{i}^{x}=\sum_{j=0}^{b-1}x_{j}2^{j},\hat{c}_{i}^{y}=\sum_{j=0}^{b-1}y_{j}2^{j},\hat{c}_{i}^{z}=\sum_{j=0}^{b-1}z_{j}2^{j}, with x j , y j , z j ∈ { 0 , 1 } x_{j},y_{j},z_{j}\in\{0,1\} their binary digits. The Morton index k i k_{i} interleaves these bits as

[110] table: k i = ∑ j = 0 b − 1 ( x j ​ 2 3 ​ j + y j ​ 2 3 ​ j + 1 + z j ​ 2 3 ​ j + 2 ) . k_{i}=\sum_{j=0}^{b-1}\big(x_{j}2^{3j}+y_{j}2^{3j+1}+z_{j}2^{3j+2}\big). (8)

[111] p: Intuitively, cells that are close in 3D tend to share a long common bit prefix and therefore have similar Morton indices, yielding a Z-shaped traversal of the 3D grid that preserves locality in an approximate sense. This computation is fully integer-based, parameter-free, and runs in O ⁡ ( b ) O(b) time per superpoint (typically realized using efficient low-level bit-twiddling operations).

[112] h4: Hilbert index.

[113] p: The 3D Hilbert curve also maps each grid cell to a unique integer index in [ 0 , 2 3 ​ b − 1 ] [0,2^{3b}-1] , but is constructed recursively: the cube is subdivided into 2 × 2 × 2 2\times 2\times 2 subcubes, each visited exactly once in an order that forms a continuous curve; at each recursion level, the traversal of the 8 children is rotated and reflected depending on the parent orientation. The resulting integer mapping k i = Hilbert ⁡ ( c ^ i ) k_{i}=\mathrm{Hilbert}(\hat{c}_{i}) can be implemented by a standard integer Hilbert algorithm that: (i) converts ( c ^ i x , c ^ i y , c ^ i z ) (\hat{c}_{i}^{x},\hat{c}_{i}^{y},\hat{c}_{i}^{z}) into a Gray-coded representation, (ii) applies a sequence of bitwise rotations/reflections, and (iii) accumulates the Hilbert index across the b b recursion levels. Compared to Morton, the Hilbert curve typically offers stronger locality preservation (consecutive indices correspond to neighboring cells with fewer long jumps), at the cost of slightly more complex bit operations. In both cases, SFC ⁡ ( ⋅ ) \mathrm{SFC}(\cdot) is a deterministic, parameter-free integer function.

[114] h4: From keys to a 1D token sequence.

[115] p: Given the SFC keys { k i } i = 0 M − 1 \{k_{i}\}_{i=0}^{M-1} , we compute the permutation

[116] table: π i = argsort ⁡ ( [ k 0 , … , k M − 1 ] ) , \pi_{i}=\mathrm{argsort}\big([k_{0},\dots,k_{M-1}]\big), (9)

[117] p: which orders the superpoints according to their SFC indices. Applying this permutation to the superpoint tokens 𝒮 \mathcal{S} yields a serialized sequence 𝒮 i = 𝒮 ⁡ [ π i ] . \mathcal{S}_{i}=\mathcal{S}[\pi_{i}]. Where adjacent tokens correspond to spatially nearby regions in 3D (up to the locality guarantees of the chosen curve). This 1D ordering allows us to apply efficient sequence operators ( e.g . , FFT) while approximately preserving the 3D locality.

[118] h3: G.3 More details about neighbor searching

[119] p: Real-world captured point clouds often present holes, disconnections, or sparse regions. Consequently, the initial connectivity operation can yield spurious edges when attempting to merge object-level superpoints. To reduce incorrect neighbors, we employ a two-factor re-ranking strategy. We prioritize edges based on the shortest 3D Euclidean distance as the primary factor. We then use the initial votes ( i.e. , connectivity scores) as a secondary tie-breaker, retaining only the top k k nearest neighbors to construct the final, clean graph. Specifically, we sum the neighborhood connectivity votes to obtain a coalesced candidate edge set ℰ cand = { ( s , t , v s , t ) | v s t > 0 } \mathcal{E}^{\text{cand}}=\{(s,t,v_{s,t})\,|\,v_{s_{t}}>0\} . To suppress spurious connections resulting from SFC topological folding, we employ a re-ranking strategy for each source node s s . Candidates are ranked using the squared Euclidean center distance d s , t = ‖ c s − c t ‖ 2 2 d_{s,t}=\|c_{s}-c_{t}\|_{2}^{2} as the primary sorting key, and the connectivity votes v s , t v_{s,t} as the secondary tie-breaker. We then retain the k k nearest neighbors that minimize this composite tuple ( d s , t , − v s , t ) (d_{s,t},-v_{s,t}) . The resulting sparse graph 𝒢 \mathcal{G} , represented by its adjacency matrix A A and degree matrix D D , is thus finalized for use in the next stage.

[120] h2: H Computational complexity analysis

[121] h3: H.1 Graph construction

[122] p: Superpoint neighbors in our setting are defined by the minimum distance between their boundary points , i.e. , points lying near inter-superpoint interfaces. Let N N be the number of points in a scene, M M the number of superpoints, and B B the batch size. Constructing a superpoint adjacency graph is a critical step in 3D tokenization and largely determines both the computational cost and memory footprint of the overall vision–language pipeline.

[123] p: In this section, we compare the proposed multi-curve voting graph with a conventional raw superpoint k k -nearest-neighbor (KNN) graph constructed from boundary-based distances between superpoints.

[124] h4: Raw KNN-based graph on superpoints.

[125] p: A brute-force construction compares points across all distinct superpoints to identify potential boundary interactions. Boundary-aware distances are computed a posteriori by aggregating inter-superpoint point-to-point distances ( e.g . , taking the minimum), followed by a top- k k selection step.

[126] p: Let p i p_{i} denote the number of points in superpoint i i , such that the total number of points is N = ∑ i p i N=\sum_{i}p_{i} . A naive implementation scanning all point pairs across distinct superpoints incurs a computational cost of

[127] table: T raw = 𝒪 ⁡ ( B ​ ∑ i ≠ j p i ​ p j ) . T_{\text{raw}}=\mathcal{O}\Big(B\sum_{i\neq j}p_{i}p_{j}\Big). (10)

[128] p: Using the identity ∑ i ≠ j a i ​ a j = ( ∑ i a i ) 2 − ∑ i a i 2 \sum_{i\neq j}a_{i}a_{j}=(\sum_{i}a_{i})^{2}-\sum_{i}a_{i}^{2} , this simplifies to:

[129] table: T raw = 𝒪 ⁡ ( B ⁡ ( N 2 − ∑ i p i 2 ) ) . T_{\text{raw}}=\mathcal{O}\Big(B\big(N^{2}-\textstyle\sum_{i}p_{i}^{2}\big)\Big). (11)

[130] p: In any typical over-segmentation ( M ≥ 2 , N M ≤ p i ≤ N / 2 M\geq 2,N_{M}\leq p_{i}\leq N/2 ), the points are distributed across multiple regions, ensuring that the intra-superpoint term is negligible compared to the total interactions ( ∑ i p i 2 ≪ N 2 \sum_{i}p_{i}^{2}\ll N^{2} ). N M ≥ 2 N_{M}\geq 2 is a predefined threshold. Consequently, T raw = 𝒪 ⁡ ( B ​ N 2 ) ≫ 𝒪 ⁡ ( N ​ log ⁡ N ) T_{\text{raw}}=\mathcal{O}(BN^{2})\gg\mathcal{O}(N\log N) , this brute-force approach asymptotically dominates any efficient near-linear spatial indexing scheme.

[131] p: The memory footprint is likewise prohibitive, requiring the materialization of a dense M × M M\times M distance structure:

[132] table: M raw = 𝒪 ⁡ ( B ​ M 2 ) . M_{\text{raw}}=\mathcal{O}\big(BM^{2}\big). (12)

[133] p: Even for moderate over-segmentation ( e.g . , M = 1024 M{=}1024 ), this yields over 10 6 10^{6} entries per scene. Furthermore, because boundary points are not known a priori , the boundary-aware variant amplifies load imbalance: superpoints with complex interfaces or higher point densities disproportionately increase the constant factors in the runtime.

[134] h4: Multi-curve sparse voting graph.

[135] p: Our method sidesteps dense global pairwise comparisons by projecting the point cloud onto multiple space-filling curves and restricting neighbor search to short 1D windows along each curve.

[136] p: Let C = | π | C=|\pi| be the number of curves, W W the local window radius on each curve (so each window has at most 2 ​ W + 1 2W{+}1 points), and s s the point-sampling stride along the curves. Each source point participates in at most ( 2 ​ W + 1 ) (2W{+}1) 1D neighbors per curve, and we only evaluate these local pairs. Across all curves and all batches, the total number of candidate edges is

[137] table: E ≈ C ⋅ B ⋅ N s ⋅ ( 2 ​ W + 1 ) = 𝒪 ⁡ ( C ​ B ​ N ​ W s ) , E\;\approx\;C\cdot B\cdot\frac{N}{s}\cdot(2W{+}1)\;=\;\mathcal{O}\Big(CB\frac{NW}{s}\Big), (13)

[138] p: so the number of candidate edges grows linearly in N N , rather than quadratically in M M . We then aggregate all per-curve votes into a sparse COO tensor and resolve duplicates via a multi-key stable sort ( e.g. , over (batch, src, dst) ). This yields an overall time complexity

[139] table: T curve = 𝒪 ⁡ ( C ​ B ​ N ​ W s ​ log ⁡ ( C ​ B ​ N ​ W s ) ) , T_{\text{curve}}=\mathcal{O}\Big(CB\frac{NW}{s}\log\big(CB\tfrac{NW}{s}\big)\Big), (14)

[140] p: which is near-linear in the number of points, up to a small log \log factor. The subsequent per-superpoint top- k k selection operates only on outgoing edges from each node and contributes a lower-order term 𝒪 ⁡ ( B ​ M ​ k ​ log ⁡ k ) \mathcal{O}\big(BMk\log k\big) , which is negligible compared to the global sparse sort over E E . The memory usage also scales linearly with the scene size:

[141] table: M curve = 𝒪 ⁡ ( C ​ B ​ N ) + 𝒪 ⁡ ( E ) , M_{\text{curve}}=\mathcal{O}(CBN)+\mathcal{O}(E), (15)

[142] p: since all intermediate structures remain sparse and we never build a dense M × M M\times M matrix. In other words, our multi-curve voting graph replaces the 𝒪 ⁡ ( B ​ M 2 ) \mathcal{O}(BM^{2}) time and memory bottleneck of raw KNN with a near-linear 𝒪 ⁡ ( C ​ B ​ N ) \mathcal{O}\big(CBN\big) procedure that remains efficient even for high-resolution scenes and large numbers of superpoints.

[143] h3: H.2 FFT-based context enhancer

[144] p: Let D D be the feature dimension, and H H the number of frequency heads (with per-head width d h ≈ D / H d_{h}\approx D/H ). We analyze the complexity of the FFT-based context enhancer along the superpoint axis in its windowed (overlap–add) variant, which is the one used in our implementation.

[145] h4: Windowed (overlap-add) FFT mixing.

[146] p: Given a sequence of M M tokens, the mixer decomposes it into overlapping windows of length L L and stride R R . The effective number of windows per sequence is

[147] table: W ≈ ⌊ M − L R ⌋ + 1 = 𝒪 ⁡ ( M R ) . W\;\approx\;\Big\lfloor\frac{M-L}{R}\Big\rfloor+1\;=\;\mathcal{O}\Big(\frac{M}{R}\Big). (16)

[148] p: On each window, we run a 1D FFT of length L L for each head, apply low/high-band gating, and then perform an inverse FFT. The cost of these spectral operations is

[149] table: T FFT = 𝒪 ⁡ ( B ​ D ​ M R ​ L ​ log ⁡ L ) , T_{\text{FFT}}=\mathcal{O}\Big(BD\frac{M}{R}L\log L\Big), (17)

[150] p: since H ​ d h ≈ D Hd_{h}\approx D . The additional steps (masked centering, Hann weighting, linear in/out projections, and overlap–add reconstruction) contribute only linear overhead 𝒪 ⁡ ( B ​ M ​ D ) \mathcal{O}(BMD) .

[151] p: For fixed window and stride (as in our experiments), L L and R R are constants, so the dominant term simplifies to

[152] table: T FFT = 𝒪 ⁡ ( B ​ D ​ M ) , T_{\text{FFT}}=\mathcal{O}(BDM), (18)

[153] p: that is, effectively linear in the number of tokens M M . The memory footprint is also linear in M M :

[154] table: M FFT = 𝒪 ⁡ ( B ​ M ​ D ) , M_{\text{FFT}}=\mathcal{O}(BMD), (19)

[155] p: covering unfolded windows, FFT and reconstruction buffers.

[156] p: Multi-curve fusion. When operating on multiple space-filling curves ( e.g . , Hilbert, transposed Hilbert, Z-order, transposed Z-order) with | π | |\pi| curve traversals, we apply the same windowed FFT mixer independently to each curve and fuse their outputs. This introduces a multiplicative factor in both time and memory:

[157] table: T FFT = 𝒪 ⁡ ( | π | ​ B ​ D ​ M ) , M FFT = 𝒪 ⁡ ( | π | ​ B ​ M ​ D ) , T_{\text{FFT}}=\mathcal{O}\big(|\pi|\,BDM\big),M_{\text{FFT}}=\mathcal{O}\big(|\pi|\,BMD\big), (20)

[158] p: while the curve-attention scorer adds only a lightweight 𝒪 ⁡ ( B ​ | π | ​ D ) \mathcal{O}(B|\pi|D) term.

[159] h2: I Dataset and Implementation details

[160] h3: I.1 Dataset

[161] p: During training, we use the ScanNet portion of the 3D-LLM dataset [ 17 ] as our primary source. We further augment it with complementary datasets, including ScanQA [ 2 ] , SQA3D [ 29 ] , ScanRefer [ 5 ] , and Nr3D [ 1 ] . After joint training on this mixture, we fine-tune Fase3D separately on each target dataset. We briefly summarize the datasets below.

[162] p: 3D-LLM dataset [ 17 ] comprises: (i) 1,033 textual descriptions across 517 scenes, (ii) 1,864 lines of embodied task planning spanning 510 scenes, and (iii) 2,955 lines of multi-turn embodied dialogues across 517 scenes.

[163] p: ScanQA dataset [ 2 ] is a 3D question answering benchmark built on top of ScanNet [ 9 ] , designed to evaluate scene understanding via natural language queries. It contains 6,857 unique questions paired with 30,769 answers over 806 reconstructed indoor environments. Questions focus on objects in the scene and cover object attributes, spatial relationships, and scene semantics. On average, each scene has 8.5 questions, encouraging reasoning over object-level details and contextual relations in complex 3D environments.

[164] p: ScanRefer dataset [ 5 ] is a multimodal benchmark for 3D vision-language reasoning built on ScanNet [ 9 ] , consisting of 1,613 RGB-D scans across 806 unique indoor scenes. It provides 51,583 natural language descriptions for objects in reconstructed 3D scenes, covering 800 ScanNet scenes. Each object is annotated with an average of 4.67 descriptions, resulting in rich linguistic diversity. On average, each scene contains 13.81 objects and 64.48 descriptions, spanning over 250 categories of common indoor objects. Among these, 41,034 descriptions explicitly mention attributes such as color, shape, size, and spatial relations, making ScanRefer a strong benchmark for fine-grained language reasoning.

[165] p: Nr3D dataset [ 1 ] is a natural language 3D object localization benchmark built on ScanNet [ 9 ] . It contains 41,503 unique referring expressions for 5,578 objects across 707 scenes. Each description is crafted to unambiguously identify a target object in context, using spatial relations and attributes such as color, shape, and size. On average, each object is associated with 7.4 descriptions, making Nr3D well suited for evaluating fine-grained attribute understanding and spatial reasoning in 3D scenes.

[166] p: SQA3D dataset [ 29 ] is a spatial question answering benchmark in 3D environments, also constructed on top of ScanNet [ 9 ] . It consists of natural language questions that require explicit 3D spatial reasoning, such as object existence, relative position, and relations among multiple objects. Each question is grounded in a reconstructed 3D scene and paired with a free-form textual answer, enabling evaluation of both geometric understanding and language generation. Compared with traditional 2D VQA benchmarks, SQA3D places stronger emphasis on 3D-aware reasoning over scene layouts, object configurations, situated and embodied scene understanding, providing a challenging testbed for holistic 3D vision–language models.

[167] h3: I.2 Implementation details

[168] p: Superpoint generation. We directly use the segmentor provided by ScanNet [ 10 ] , which are obtained via a graph-cut–based over-segmentation method [ 19 , 14 ] .

[169] p: Training strategy. Following prior work [ 6 , 30 ] , Fase3D adopts a two-stage training strategy. In the first stage, we pre-train the model on an ensemble of datasets spanning diverse 3D tasks (dense captioning and question answering), so that it acquires a broad understanding of 3D scenes and functions as a 3D generalist model. In the second stage, we perform instruction-following fine-tuning on task-specific datasets for 3D dense captioning and 3D question answering, thereby specializing the model for the downstream benchmarks. Note that during both stages we do not use proposals from Mask3D [ 38 ] ; all supervision is applied directly on our own tokenization pipeline.

[170] p: Hyperparameters. Unless otherwise specified, for the 1D FFT and window-based voting we use a window size of 64 and a stride of 16 along each space-filling curve. For Sinkhorn normalization, we perform 5 iterations, which we found to provide a good compromise between convergence quality and computational cost.

[171] h2: References

[172] h2: Instructions for reporting errors

[173] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[174] p: Tip: You can select the relevant text first, to include it in your report.

[175] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[176] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
