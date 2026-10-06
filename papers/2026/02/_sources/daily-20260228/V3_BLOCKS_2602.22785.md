[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: SceneTransporter: Optimal Transport-Guided Compositional Latent Diffusion for Single-Image Structured 3D Scene Generation

[3] h6: Abstract

[4] p: We introduce SceneTransporter, an end-to-end framework for structured 3D scene generation from a single image. While existing methods generate part-level 3D objects, they often fail to organize these parts into distinct instances in open-world scenes. Through a debiased clustering probe, we reveal a critical insight: this failure stems from the lack of structural constraints within the model’s internal assignment mechanism. Based on this finding, we reframe the task of structured 3D scene generation as a global correlation assignment problem. To solve this, SceneTransporter formulates and solves an entropic Optimal Transport (OT) objective within the denoising loop of the compositional DiT model. This formulation imposes two powerful structural constraints. First, the resulting transport plan gates cross-attention to enforce an exclusive, one-to-one routing of image patches to part-level 3D latents, preventing entanglement. Second, the competitive nature of the transport encourages the grouping of similar patches, a process that is further regularized by an edge-based cost, to form coherent objects and prevent fragmentation. Extensive experiments show that SceneTransporter outperforms existing methods on open-world scene generation, significantly improving instance-level coherence and geometric fidelity. Code and models will be publicly available at https://2019epwl.github.io/SceneTransporter/ .

[5] h2: 1 Introduction

[6] p: The capacity to generate high-quality, scalable 3D scenes is a cornerstone for the next generation of immersive technologies and embodied AI. While advancements in generative AI promise scalable synthesis, the vast majority of scene generators still produce monolithic, unstructured meshes ( Vodrahalli et al., 2024 ; Li et al., 2025 ; Xiang et al., 2025 ) . For real-world pipelines, a fused 3D shell is functionally inert. Downstream tasks—including material assignment, realistic physics simulation, asset retrieval and placement, and fine-grained editing—require a structured scene mesh with explicit, instance-level object-context disentanglement. A common “divide and conquer” solution attempts this by first segmenting an input image, then generating a 3D model for each part, and finally assembling them into a scene ( Huang et al., 2025 ; Chen et al., 2024b ; Ardelean et al., 2024 ) . This multi-stage pipeline, however, is inherently brittle; its heavy reliance on 2D segmentation makes it incapable of handling heavily occluded objects, and transforms even minor 2D segmentation flaws into significant 3D geometric artifacts.

[7] p: In recent years, end-to-end structured generation has emerged as a promising alternative ( Lin et al., 2025b ; Tang et al., 2025 ; Chen et al., 2025a ; Yang et al., 2025b ) , enabled by the development of large-scale repositories with explicit part annotations (e.g., Objaverse ( Lin et al., 2025a ) ). In this paradigm, a scene is no longer represented as a single, indivisible latent code but as a collection of disentangled latent tokens, where each set of tokens corresponds to a distinct 3D part. Although these methods show great promise for generating structured objects and indoor scenes, open-world structured scene generation remains underexplored. As illustrated in Figure 4 , when naively applied to large, complex open-world scenes, it uncovers two persistent 3D pathologies: (i) Structural Mispartition —semantic instances within the scene fail to form disjoint parts; and (ii) Geometric Redundancy —multiple latents “compete” to describe the same geometric area.

[8] p: To address these challenges, we first perform Probing Latent Structure with Debiased Clustering. This probe reveals the primary bottleneck: a lack of structural constraints within the model’s assignment mechanism prevents the formation of stable instances. To this end, we introduce SceneTransporter, a framework that reframes the task as an Optimal-Transport–Guided Correlation Assignment problem. To solve this, we define a principled entropic Optimal Transport (OT) formulation that calculates a globally optimal transport plan between the set of image patch features and the part-level tokens. This optimization imposes powerful structural constraints through two key components. First, an OT Plan–Gated Cross–Attention module uses the plan to enforce a hard, one-to-one routing, ensuring each patch contributes to only one part, thus preventing feature entanglement. Second, the competitive nature of the transport incentivizes patches with high feature similarity to be assigned to the same token, naturally forming coherent structures. To further refine this grouping and ensure sharp object boundaries, we introduce an Edge–Regularized Assignment Cost, which penalizes assignments that cross salient image edges within the transport objective. Extensive experiments show that our approach outperforms existing methods, setting a new framework for structured 3D scene generation.

[9] p: In summary, our contributions are as follows:

[10] p: We design a Debiased Clustering probe based on Canonical Correlation Analysis (CCA) to investigate the latent structure of part-level generators. The probe reveals that the core failure lies in the assignment mechanism due to a lack of structural constraints.

[11] p: We reframe the task as an Optimal-Transport (OT)–Guided Correlation Assignment problem. To solve this, we propose SceneTransporter, which leverages an entropic OT framework to impose two powerful structural constraints: an OT Plan–Gated Cross–Attention module for exclusive one-to-one routing, and an Edge-Regularized Assignment Cost for coherent structures grouping.

[12] p: SceneTransporter achieves state-of-the-art performance on open-world 3D scene generation, demonstrating significantly improved instance-level coherence and geometric fidelity.

[13] figure: Figure 1: Comparison between our end-to-end scene generation pipeline in (c) with compositional 3D latent diffusion and existing “divide and conquer” methods.

[14] h2: 2 Related Work

[15] h4: 3D Scene Generation.

[16] p: Early approaches to scene synthesis were dominated by retrieval-based methods, which compose scenes by aligning assets from a 3D database with an input image ( Feng et al., 2023 ; Gao et al., 2024 ; Langer et al., 2024 ) . These methods, however, are fundamentally limited by the scope of their database and often suffer from alignment errors from a single view. The advent of large-scale generative models has shifted the focus towards creating novel content. One dominant approach is 2D-prior distillation, a multi-stage process that first generates consistent multi-view images ( Chen et al., 2025b ; Li et al., 2024 ) , videos Sun et al. (2024) ; Wang et al. (2025) ; Liang et al. (2025) , or panoramic images Yang et al. (2025a) ; Zhou et al. (2024) via powerful diffusion models, and then reconstructs a 3D scene from these views using techniques like Neural Radiance Fields (NeRF) or 3D Gaussian Splatting (3DGS). To address the geometric inconsistencies of 2D-lifting, another line of research develops models that operate directly in native 3D latent spaces ( Meng et al., 2025 ; Wu et al., 2024 ; Lee et al., 2025 ; Ren et al., 2024 ; Lee et al., 2024 ; Liu et al., 2024b ) . While this improves multi-view consistency, it requires large-scale 3D datasets and generalizes poorly to in-the-wild scenes. Crucially, both of these generative avenues converge on the same limitation: their output is a single, unstructured monolithic mesh, which lacks the explicit object-level separation needed for most downstream tasks.

[17] h4: 3D Structured Scene Generation.

[18] p: A common “divide and conquer” strategy for structured scene generation is to process a scene piece by piece ( Chen et al., 2024b ; Ardelean et al., 2024 ; Han et al., 2024 ) . This typically involves a pipeline that segments the input, generates 3D models for the segments, and then arranges them. Such methods benefit from modularity but suffer from two key weaknesses: the accumulation of errors across stages and a failure to maintain global consistency. While more integrated approaches like MIDI ( Huang et al., 2025 ) use a multi-instance attention mechanism to capture inter-object interactions, they remain fundamentally limited by their reliance on segmenting visible content, preventing the reconstruction of occluded parts. Another line of work explores end-to-end compositional generation using 3D diffusion models that bind latent token subsets to semantic parts ( Lin et al., 2025b ; Tang et al., 2025 ) . While these models excel at generating structured objects, they fail to generalize to complex open-world scenes due to a scarcity of scene-level part annotations. This generalization gap manifests as two distinct geometric pathologies (Figure 4 ): structural mispartition and geometric redundancy. Our work offers the first direct solution, introducing a method to guide the compositional cross-attention of pretrained generators and explicitly correct these failure modes.

[19] h4: Attention control in diffusion models.

[20] p: Attention maps in image and video diffusion models have become a compact, training-free control interface: by manipulating or augmenting self- and cross-attention at sampling time, practitioners can steer layout and composition ( Chen et al., 2024a ; Hertz et al., 2022 ; Patashnik et al., 2023 ) , transfer fine-grained texture and style ( Hertz et al., 2024 ) , enforce multi-prompt alignment ( Chefer et al., 2023 ) and temporal coherence for videos ( Cai et al., 2025 ; Liu et al., 2024a ; Qi et al., 2023 ) , and perform a variety of image-editing tasks ( Parmar et al., 2023 ; Yang et al., 2023 ; Mokady et al., 2023 ; Park et al., 2024 ; Tumanyan et al., 2023 ) . Despite its success in 2D, attention-based control has seen little application to 3D latent diffusion—largely because 3D representations differ fundamentally. In 2D, attention queries live on a regular spatial grid with explicit positions. By contrast, 3D data commonly takes irregular forms. For instance, in the vecset-based latent representation ( Zhang et al., 2023 ) where a shape is encoded as an unordered set of latent vectors, positional information is not explicitly structured. The absence of a canonical spatial index therefore makes attention manipulation for 3D editing substantially more difficult and still largely unexplored.

[21] h2: 3 Methodology

[22] h3: 3.1 Preliminaries: Compositional 3D Generators

[23] p: A typical compositional 3D generator consists of two key components: (i) a Transformer-based Variational Autoencoder (VAE), such as 3DShape2VecSet, which encodes a 3D mesh into a set of latent vectors and decodes them back into a geometric field ( e.g. , SDF), and (ii) a denoising network that operates within this latent space to reverse a diffusion process and synthesize clean latents from noise. Prior to going further, we first introduce the notations and preliminaries used in our paper, especially those for the attention mechanism, as its core lies in modeling the geometric dependencies among shape components. At denoising step t t , the model maintains N N part-specific token blocks { 𝐳 i ( t ) } i = 1 N \{\mathbf{z}_{i}^{(t)}\}_{i=1}^{N} , where each 𝐳 i ( t ) ∈ ℝ K × D \mathbf{z}_{i}^{(t)}\!\in\!\mathbb{R}^{K\times D} contains K K tokens (width D D ) for part i i . A common practice is to add a learnable part identity embedding 𝐞 i ∈ ℝ D \mathbf{e}_{i}\!\in\!\mathbb{R}^{D} to all tokens of part i i , where 𝟏 K \mathbf{1}_{K} is a column vector of ones:

[24] table: 𝐳 ~ i ( t ) = 𝐳 i ( t ) + 𝟏 K ​ 𝐞 i ⊤ , 𝐙 ( t ) = concat tokens ​ ( 𝐳 ~ 1 ( t ) , … , 𝐳 ~ N ( t ) ) ∈ ℝ ( N ​ K ) × D . \tilde{\mathbf{z}}_{i}^{(t)}=\mathbf{z}_{i}^{(t)}+\mathbf{1}_{K}\mathbf{e}_{i}^{\top},\qquad\mathbf{Z}^{(t)}=\mathrm{concat}_{\text{tokens}}\big(\tilde{\mathbf{z}}_{1}^{(t)},\ldots,\tilde{\mathbf{z}}_{N}^{(t)}\big)\in\mathbb{R}^{(NK)\times D}. (1)

[25] p: Conditioning comes from a single RGB image 𝐱 \mathbf{x} encoded by a frozen DINOv2 ϕ ⁡ ( 𝐱 ) = 𝐈 ∈ ℝ L × D img \phi(\mathbf{x})=\mathbf{I}\in\mathbb{R}^{L\times D_{\text{img}}} . Linear projections yield queries, keys, and values (omitting head indices for brevity):

[26] table: 𝐐 = ℓ Q ​ ( 𝐙 ( t ) ) ∈ ℝ ( N ​ K ) × d , 𝐊 = ℓ K ​ ( 𝐈 ) ∈ ℝ L × d , 𝐕 = ℓ V ​ ( 𝐈 ) ∈ ℝ L × d . \mathbf{Q}=\ell_{Q}(\mathbf{Z}^{(t)})\in\mathbb{R}^{(NK)\times d},\quad\mathbf{K}=\ell_{K}(\mathbf{I})\in\mathbb{R}^{L\times d},\quad\mathbf{V}=\ell_{V}(\mathbf{I})\in\mathbb{R}^{L\times d}. (2)

[27] p: Row-normalized cross-attention fuses image evidence into the latent tokens. In practice, to increase expressiveness, multi-head attention is used: the projections are split into H H heads ( 𝐐 h , 𝐊 h , 𝐕 h ) (\mathbf{Q}_{h},\mathbf{K}_{h},\mathbf{V}_{h}) , attention is computed per head 𝐌 h = Softmax ⁡ ( 𝐐 h ​ 𝐊 h ⊤ / d ) \mathbf{M}_{h}=\mathrm{Softmax}\big(\mathbf{Q}_{h}\mathbf{K}_{h}^{\top}/\sqrt{d}\big) , the head outputs are concatenated, and a learned output projection produces the final update,

[28] table: 𝐙 ^ ( t ) = Concat h = 1 H ​ ( 𝐌 h ​ 𝐕 h ) ​ 𝐖 O . \hat{\mathbf{Z}}^{(t)}=\mathrm{Concat}_{h=1}^{H}\!\big(\mathbf{M}_{h}\mathbf{V}_{h}\big)\,\mathbf{W}_{O}. (3)

[29] p: The updated sequence proceeds through the DiT block and the denoising schedule. At inference, the final clean sequence is split back into { 𝐳 ^ i } i = 1 N \{\hat{\mathbf{z}}_{i}\}_{i=1}^{N} and each subset is decoded by the pretrained VAE to obtain a part mesh; parts are then fused to form the full scene.

[30] h3: 3.2 Probing Latent Structure with Debiased Clustering

[31] p: Part-level generators carry a strong inductive bias toward a part-level organization that models correlations among parts of the same object (e.g., chair legs and back share style and structure). In contrast, scene synthesis models an instance-level organization, where distinct entities are largely conditionally independent.

[32] p: Applying the former to the latter gives rise to two observable failure modes (Figure 4 ): Structural Mispartition, where geometry for a single object is scattered across multiple part-tokens, and Geometric Redundancy, which leads to the geometry overlap between objects. Intriguingly, despite this incoherent part-level assignment, the union of all parts often reconstructs the overall scene reasonably well. This raises a concrete question: Can we recover a coherent, instance-level organization from these part-level latents? To probe this, we introduce a debiased clustering procedure with three steps: identify the shared subspace via canonical correlation analysis (CCA) on the part-level latent sets; suppress it by projecting tokens onto the orthogonal complement to isolate object-specific variation; and regroup the residual tokens to obtain semantically coherent sets. Implementation details are provided in Appendix B .

[33] figure: Figure 2: Qualitative Results on Vecset-based Latent Probing. Cluster and Cluster with CCA are our probes that perform in the compositional latent space of PartPacker; VAE clusters the latent obtained by encoding the fused geometry produced by PartPacker into the VAE. Colors denote part assignments.

[34] p: An illustrative example is provided in Figure 2 . Our probe offers a clear signal: clustering raw part tokens fails to produce stable instance groupings, whereas clustering the CCA-debiased residual tokens reliably succeeds. This striking contrast reveals a critical flaw in current part-level generators: while their learned features implicitly contain the necessary information for correct associations, the models fail to establish these associations explicitly. As a result, the learned groupings are left weak, fragmented, and entangled with scene context. Based on this insight, we argue that a paradigm shift is required. Instead of hoping for an organization to emerge from an implicit learning process, we must introduce explicit structural constraints to guarantee a coherent, instance-level structure by design.

[35] h3: 3.3 Optimal-Transport–Guided Correlation Assignment

[36] figure: Figure 3: Overview of the SceneTransporter pipeline. At each denoising step t t , our Optimal-Transport–Guided Correlation Assignment framework formulates a global OT problem between image patches and part-level tokens within the compositional latent DiT. We compute a part-patch cost from Q/K similarity, regularized by image edges, and solve for an optimal transport plan using Sinkhorn iteration. The OT plan gates the cross attention to enforce an explicit patch-to-part routing, and the resulting gated attention map updates the latent z t z_{t} . Attention maps transport over time, showing assignments becoming sharper and more instance-consistent.

[37] p: To impose the explicit structural constraints suggested by our probe, we reframe the routing of visual evidence to part tokens as a globally optimal correlation assignment problem. We propose to solve this problem at each denoising step using the principled framework of Optimal Transport (OT). OT provides the exact constraints needed to combat the failures we observed. By enforcing a one-to-one assignment, it ensures exclusivity, preventing the feature entanglement that causes objects to blend. Simultaneously, by requiring each part-latent to meet a coverage budget, it encourages the aggregation of large, coherent patch regions, directly mitigating semantic fragmentation. This OT-guided mechanism, which we detail next, transforms the generation from an unconstrained process into a structured, well-posed optimization.

[38] h4: OT Problem Setup.

[39] p: The core challenge of routing is to ensure a globally consistent allocation: image patches should not be double-counted by multiple 3D parts, and 3D parts should not compete for the same patch information. To address this, we model the assignment as a single optimization problem with constraints. We compute an entropic OT plan 𝐀 t ∈ ℝ N × L \mathbf{A}_{t}\in\mathbb{R}^{N\times L} to allocate the mass from L L image patch features to the latent tokens of N N 3D parts:

[40] table: 𝐀 t = arg ​ min 𝐀 ≥ 0 ⁡ ⟨ 𝐂 t , 𝐀 ⟩ + ε t ​ ℋ ​ ( 𝐀 ) s.t. 𝐀𝟏 = 𝝁 , 𝐀 ⊤ ​ 𝟏 = 𝝂 , \mathbf{A}_{t}=\argmin_{\mathbf{A}\geq 0}\ \langle\mathbf{C}_{t},\mathbf{A}\rangle+\varepsilon_{t}\,\mathcal{H}(\mathbf{A})\quad\text{s.t.}\quad\mathbf{A}\mathbf{1}=\bm{\mu},\ \ \mathbf{A}^{\!\top}\mathbf{1}=\bm{\nu}, (4)

[41] p: where the cost matrix 𝐂 t ∈ ℝ N × L \mathbf{C}_{t}\in\mathbb{R}^{N\times L} measures the incompatibility between patches and parts, as will be detailed in Eq. ( 12 ). Crucially, the constraints enforce a budget for each part through 𝝁 ∈ Δ N \bm{\mu}\in\Delta^{N} , which prevents any part from being ‘‘starved’’ of information 1 1 1 Δ N = { 𝒙 ∈ ℝ ≥ 0 N | 𝟏 N ​ 𝒙 = 1 } \Delta^{N}=\{\bm{x}\in\mathbb{R}_{\geq 0}^{N}|\mathbf{1}_{N}\bm{x}=1\} is a probability simplex. 𝝁 ∈ Δ N \bm{\mu}\in\Delta^{N} satisfies ∑ i = 1 N μ i = 1 \sum_{i=1}^{N}\mu_{i}=1 with μ i ≥ 0 \mu_{i}\geq 0 . . They also ensure that each patch contributes an equal amount of mass by 𝝂 = 1 L ​ 𝟏 L \bm{\nu}=\tfrac{1}{L}\mathbf{1}_{L} , meaning each patch contributes 1 / L 1/L of the total mass. ℋ ⁡ ( 𝐀 ) \mathcal{H}(\mathbf{A}) is the entropy of the transport plan 𝐀 \mathbf{A} , and ε t \varepsilon_{t} is the entropic regularization term, which helps to smooth the solution. The resulting transport plan 𝐀 t \mathbf{A}_{t} minimizes the assignment cost while adhering to the capacity constraints.

[42] h4: OT Plan–Gated Cross–Attention.

[43] p: Given the entropic OT plan 𝐀 t ∈ ℝ N × L \mathbf{A}_{t}\!\in\!\mathbb{R}^{N\times L} from Eq. ( 4 ), we inject this global assignment into the native cross-attention mechanism by using it to gate the incoming visual information multiplicatively. This approach enables us to regulate the amount of evidence each image patch can contribute to each 3D part, while preserving the standard Softmax \mathrm{Softmax} attention to decide which of the available patches each token should focus on. To achieve this, we first convert the transport plan 𝐀 t \mathbf{A}_{t} into per-part patch weights 𝝎 i ∈ Δ L \bm{\omega}_{i}\in\Delta^{L} through row-normalization. We then design a bounded, identity-preserving gating function ψ ⁡ ( ⋅ ) \psi(\cdot) that transforms these weights into a gating signal:

[44] table: ψ λ t , ε g ​ ( w ) = ε g + ( 1 − ε g ) ​ w λ t , w ∈ [ 0 , 1 ] , λ t ≥ 0 , ε g ∈ [ 0 , 1 ) , \psi_{\lambda_{t},\varepsilon_{g}}(w)\;=\;\varepsilon_{g}\;+\;(1-\varepsilon_{g})\,w^{\lambda_{t}},\qquad w\in[0,1],\ \lambda_{t}\!\geq\!0,\ \varepsilon_{g}\!\in\![0,1), (5)

[45] p: where the guidance strength λ t \lambda_{t} determines how quickly the gate closes for patches with low weights, while a small floor ε g \varepsilon_{g} prevents any patch from being entirely starved of attention. Critically, when guidance is disabled ( λ t = 0 \lambda_{t}=0 ), the function outputs exactly 1, guaranteeing that the mechanism reverts to standard cross-attention. This gating signal is subsequently applied to modulate both the keys and values in the attention computation for each part. For a specific head h h , the keys 𝐊 h \mathbf{K}_{h} and values 𝐕 h \mathbf{V}_{h} are scaled row-wise by the gating signal derived from the part-specific weights ω i ​ ( j ) \omega_{i}(j) . This results in a unique, gated “view” of the image memory for each part i i :

[46] table: 𝐊 h ( i ) ( j , : ) = ψ λ t , ε g ( ω i ( j ) ) 𝐊 h ( j , : ) , 𝐕 h ( i ) ( j , : ) = ψ λ t , ε g ( ω i ( j ) ) 𝐕 h ( j , : ) . \mathbf{K}^{(i)}_{h}(j,:)\;=\;\psi_{\lambda_{t},\varepsilon_{g}}\!\big(\omega_{i}(j)\big)\;\mathbf{K}_{h}(j,:),\quad\mathbf{V}^{(i)}_{h}(j,:)\;=\;\psi_{\lambda_{t},\varepsilon_{g}}\!\big(\omega_{i}(j)\big)\;\mathbf{V}_{h}(j,:). (6)

[47] p: The queries for the 3D part i i focus solely on this gated memory. By gating both keys and values, we ensure that routes suppressed by the OT plan contribute neither large logits nor large feature values, resulting in a clean, capacity-consistent routing with low leakage. The final representations for each part are computed via standard multi-head attention on their respective gated inputs and then stitched together:

[48] table: 𝐌 h ( i ) = Softmax ( 𝐐 ( t ) h ( 𝒮 i , : ) ( 𝐊 ( i ) h ) ⊤ d h ) , 𝐇 h ( i ) = 𝐌 h ( i ) 𝐕 h ( i ) , \mathbf{M}^{(i)}_{h}=\mathrm{Softmax}\Big(\tfrac{\mathbf{Q}^{(t)}_{h}(\mathcal{S}_{i},:)\,\big(\mathbf{K}^{(i)}_{h}\big)^{\!\top}}{\sqrt{d_{h}}}\Big),\qquad\mathbf{H}^{(i)}_{h}=\mathbf{M}^{(i)}_{h}\,\mathbf{V}^{(i)}_{h}, (7)

[49] table: 𝐙 ^ ( t ) ( 𝒮 i , : ) = Concat h = 1 H [ 𝐇 h ( i ) ] 𝐖 O , i = 1 , … , N , 𝐙 ^ ( t ) ∈ ℝ ( N ​ K ) × d . \widehat{\mathbf{Z}}^{(t)}(\mathcal{S}_{i},:)=\mathrm{Concat}_{h=1}^{H}\!\big[\mathbf{H}^{(i)}_{h}\big]\mathbf{W}_{O},\quad i=1,\ldots,N,\qquad\widehat{\mathbf{Z}}^{(t)}\in\mathbb{R}^{(NK)\times d}. (8)

[50] h4: Edge–Regularized Assignment Cost.

[51] p: In cluttered scenes, patch features near contact boundaries often seem compatible with multiple parts. As a result, the transported patch tends to “leak” information across adjacent objects. To address this issue, we introduce a weak but spatially precise prior: an edge map 𝐄 ∈ [ 0 , 1 ] H × W \mathbf{E}\!\in\![0,1]^{H\times W} obtained from the conditioning image ( e.g. , Canny/Sobel or a learned edge detector). The goal is to encourage region–wise consistency in the affinities between parts and patches while discouraging the spread of information across image edges.

[52] p: Let { 𝐪 ¯ i ( t ) } i = 1 N \{\bar{\mathbf{q}}_{i}^{(t)}\}_{i=1}^{N} represent the aggregated token of the i i -th part. Meanwhile, let { 𝐤 j } j = 1 L \{\mathbf{k}_{j}\}_{j=1}^{L} denote the patch keys. We first compute the raw cosine similarities between these prototypes and keys,

[53] table: S i , j = cos ⁡ ( 𝐪 ¯ i ( t ) , 𝐤 j ) ∈ [ − 1 , 1 ] . S_{i,j}\;=\;\cos\!\big(\bar{\mathbf{q}}_{i}^{(t)},\,\mathbf{k}_{j}\big)\in[-1,1]. (9)

[54] p: We downsample the edge map to match the patch grid, resulting in 𝐄 ↓ ∈ [ 0 , 1 ] H p × W p \mathbf{E}_{\!\downarrow}\!\in\![0,1]^{H_{p}\times W_{p}} where H p ​ W p = L H_{p}W_{p}=L , and construct a 4–neighborhood graph among the patches. For a patch j j and its neighboring patch ℓ ∈ 𝒩 ⁡ ( j ) \ell\!\in\!\mathcal{N}(j) , we define an edge–aware coupling weight:

[55] table: w j ​ ℓ = exp ⁡ ( − γ edge ​ max ⁡ { 𝐄 ↓ ​ ( j ) , 𝐄 ↓ ​ ( ℓ ) } ) , γ edge > 0 , w_{j\ell}\;=\;\exp\!\Big(-\gamma_{\text{edge}}\;\max\{\mathbf{E}_{\!\downarrow}(j),\,\mathbf{E}_{\!\downarrow}(\ell)\}\Big),\qquad\gamma_{\text{edge}}\!>\!0, (10)

[56] p: which is close to 1 1 in smooth regions and decays near image edges. We then perform a single edge–aware smoothing step on the affinities,

[57] table: S ^ i , j = S i , j + λ edge ​ ∑ ℓ ∈ 𝒩 ⁡ ( j ) w j ​ ℓ ​ S i , ℓ 1 + λ edge ​ ∑ ℓ ∈ 𝒩 ⁡ ( j ) w j ​ ℓ , λ edge ≥ 0 . \widehat{S}_{i,j}\;=\;\frac{S_{i,j}\;+\;\lambda_{\text{edge}}\!\!\sum_{\ell\in\mathcal{N}(j)}\!w_{j\ell}\,S_{i,\ell}}{1\;+\;\lambda_{\text{edge}}\!\!\sum_{\ell\in\mathcal{N}(j)}\!w_{j\ell}},\qquad\lambda_{\text{edge}}\!\geq\!0. (11)

[58] p: Eq. ( 11 ) facilitate the spread of evidence within regions characterized by low edge strength, while simultaneously inhibiting the spread across edges. The process results in affinities that are piecewise smooth and respect boundaries. To further intensify the competition among parts for each patch, we implement a contrast normalization on a per-patch basis and obtain S ~ i , j \widetilde{S}_{i,j} from S ^ i , j \widehat{S}_{i,j} .

[59] p: Finally, our OT cost is defined as the margin–enhanced dissimilarity measure that incorporates the edge map to guide the assignment cost, ensuring that the affinities respect the boundaries and maintain region-wise consistency,

[60] table: 𝐂 t ​ ( i , j ) = 1 2 ​ ( 1 − S ~ i , j ) . \mathbf{C}_{t}(i,j)\;=\;\frac{1}{2}\big(1-\widetilde{S}_{i,j}\big). (12)

[61] p: When λ edge = 0 \lambda_{\text{edge}}\!=\!0 (or the edge map consists entirely of zeros), Eq. ( 12 ) simplifies to the standard cosine–based cost with contrast normalization. A positive λ edge \lambda_{\text{edge}} suppresses cross–boundary transport without requiring any semantic masks: patches on opposite sides of strong edges receive weak mutual support in Eq. ( 11 ), so the subsequent OT solver more reliably assigns them to different parts. All operations are differentiable and head/part–agnostic, and the hyperparameters ( λ edge , γ edge ) (\lambda_{\text{edge}},\gamma_{\text{edge}}) can be annealed across denoising steps (stronger in early steps, weaker later) to promote clean separation first and fine detail later.

[62] h2: 4 Experiments

[63] h3: 4.1 Experimental Setup

[64] h4: Baselines

[65] p: We compare our approach against recent state-of-the-art methods for part-level 3D generation— PartCrafter ( Lin et al., 2025b ) , PartPacker ( Tang et al., 2025 ) , and MiDi ( Huang et al., 2025 ) . We ensure fairness in our evaluation by using the officially released source code and checkpoints for each baseline.

[66] h4: Metrics.

[67] p: Following prior work ( Tang et al., 2025 ; Zhao et al., 2025 ) , we evaluate geometry fidelity with ULIP ( Xue et al., 2023 ; Xue et al., 2024 ) and Uni3D ( Zhou et al., 2023 ) . These models learn unified representations across text, image, and point cloud modalities. Since both ULIP-2 and Uni3D require colored point clouds as input, we assign a uniform white color to all mesh outputs before computing the metrics. For part disentanglement, we voxelize the canonical space into a 64 3 64^{3} grid, binarize occupancies { 𝐎 i } i = 1 N \{\mathbf{O}_{i}\}_{i=1}^{N} for the N N generated parts, and compute pairwise Intersection-over-Union (IoU). We report the mean of the top-20 largest IoUs, and the maximum IoU; lower values indicate better disentanglement (less inter-part overlap).

[68] h4: Implementation details.

[69] p: We build SceneTransporter on the open-source part-level 3D generator of Tang et al. (2025) , which uses a rectified-flow DiT with 24 attention blocks and supports arbitrary part counts via a dual-volume packing strategy. In our setup we instantiate dual volumes, yielding a compositional latent of size 4096 × 2 = 8192 4096\times 2=8192 with channel width 64. For the OT solver, we use a stabilized log-domain Sinkhorn with 40 iterations. We enable OT plan–gated attention in the first half of the DiT blocks, and use standard cross-attention in the remaining blocks to refine the global geometry. All other inference settings follow Tang et al. (2025) .

[70] h3: 4.2 Comparisons with State-of-the-Arts.

[71] p: To demonstrate the effectiveness and breadth of our approach, we evaluate on an open-world set of 74 high-quality scene images collected from the Web, spanning diverse styles. As shown in Table 1 , our method achieves the highest geometry fidelity and the second-lowest inter-part overlap. The absolute lowest IoU is reported by PartCrafter, largely because it discards background/ground regions during generation, which trivially reduces overlap but also compromises scene completeness. Although our runtime is slightly slower than PartPacker, we deliver substantially better geometry and disentanglement, while remaining much faster than MIDI and PartCrafter.

[72] figure: Figure 4: Qualitative Comparison on Structured 3D Scene Generation across Methods. Different colors indicate different parts in the generated 3D scene.

[73] figure: Method Instance Mask Geometry Fidelity Part Disentanglement Inference Time (s) ULIP ↑ \uparrow ULIP-2 ↑ \uparrow Uni3D ↑ \uparrow IoU max ↓ {}_{\text{max}}\downarrow IoU mean ↓ {}_{\text{mean}}\downarrow MIDI Huang et al. (2025) ✓ 0.1397 0.2763 0.2518 0.0458 0.1642 149.68 PartCrafter Lin et al. (2025b) ✗ 0.1177 0.3096 0.2635 0.0042 0.0539 157.97 PartPacker Tang et al. (2025) ✗ 0.1417 0.3083 0.2887 0.0319 0.2142 47.41 Ours ✗ 0.1466 0.3220 0.3021 0.0101 0.0926 54.99 Table 1: Quantitative Comparison on Structured 3D Scene Generation across Methods. Bold values indicate the best scores, while underlined values indicate the second-best scores among the fair comparison.

[74] figure: Method Geometry ↑ \uparrow Layout ↑ \uparrow Segmentation ↑ \uparrow MIDI ( Huang et al., 2025 ) 2.61 1.82 2.29 PartCrafter ( Lin et al., 2025b ) 2.44 1.63 2.17 PartPacker ( Tang et al., 2025 ) 2.81 2.95 1.97 Ours 3.09 3.34 3.22 Table 2: User Study. Human evaluation of different structure 3D scene generation methods across multiple aspects. Scores range from 1 to 4, with higher scores indicating better performance. Bold values represent the best performance within each metric. Figure 5: Qualitative Ablation Studies on the Edge–Regularized Assignment Cost.

[75] figure: Figure 6: Qualitative Ablation Studies on the OT Plane-gated Cross Attention. Here, A ​ _ ​ attn. \mathrm{A}\_{\text{attn.}} and B ​ _ ​ attn. \mathrm{B}\_{\text{attn.}} denote the dual-volume soft attention probability maps, reshaped to the image patch grid (brighter means higher affinity). Hard affinity visualizes the argmax(A,B) patch assignments overlaid on the input image (blue → \rightarrow A, red → \rightarrow B). A ​ _ ​ geo. \mathrm{A}\_{\text{geo.}} and B ​ _ ​ geo. \mathrm{B}\_{\text{geo.}} are the geometries decoded from dual volumes, respectively, and Uni ​ _ ​ geo. \mathrm{Uni}\_{\text{geo.}} is their fused scene mesh. Row (a) shows our OT plan–gated cross-attention; row (b) shows the standard cross-attention.

[76] figure: Figure 7: Qualitative Ablation Studies on the OT Plan Progression over Denoising Steps. Each map visualizes the hard OT plan at a given denoising step: every cell is an image patch assigned to one volume (dark blue = A, light cyan = B). Left→right shows the OT plan’s evolution; later steps mostly stabilize with only local refinements.

[77] p: Figure 4 provides qualitative comparisons: our method produces coherent object-level parts (e.g., complete houses, sofas, trees, lamps), whereas PartPacker shows semantic fragmentation (e.g., roofs or tree canopies split across parts) and feature entanglement (e.g., ground features leaking into adjacent buildings). Trained primarily on indoor assets, MIDI further requires additional instance masks at inference; it performs reasonably on simple indoor scenes but degrades on outdoor cases, exhibiting spatial layout distortions and weaker instance separation. PartPacker does not use masks and can perform well on objects that are well separated from their surroundings, but its performance deteriorates in complex spatial layouts.

[78] p: We invite 30 participants to evaluate three baselines and our method, considering three criteria: geometry quality, layout coherence, and segmentation plausibility. We employ a Forced Ranking Scale, where items are ranked from 1 to 4, with the highest rank receiving a score of 4 and the lowest rank receiving a score of 1. As clearly indicated in Table 2 , our method receives the highest preference across all three criteria, indicating more coherent object–level parts, reduced feature leakage, and better scene–wide layout consistency.

[79] h3: 4.3 Ablation Study

[80] h4: Effects of OT Plan–Gated Cross–Attention

[81] p: As shown in Figure 6 (a), our OT Plan–Gated Cross–Attention method produces highly structured and focused attention maps. Notice how A ​ _ ​ atten. \mathrm{A}\_{\text{atten.}} map clearly isolates the ground, while the other ( B ​ _ ​ atten. \mathrm{B}\_{\text{atten.}} map) concentrates exclusively on the houses. This clean separation of duties, visualized in the hard affinity map, results in distinct, non-overlapping regions. Consequently, each part is generated as a complete and clean geometric object ( A ​ _ ​ geo. \mathrm{A}\_{\text{geo.}} for the ground, B ​ _ ​ geo. \mathrm{B}\_{\text{geo.}} for the houses). When combined, they form a perfectly organized scene Uni_geo. with sharp boundaries. In contrast, the standard cross-attention in (b) is noisy and chaotic. The attention maps are diffuse, sending mixed signals about which part is responsible for which region. This confusion leads to corrupted geometry. This result validates the efficacy of our OT Plan–Gated Cross–Attention module, proving that its enforcement of one-to-one constraints effectively prevents feature entanglement.

[82] h4: OT Plan Progression over Denoising Steps.

[83] p: As shown in Figure 7 , as t t increases, the OT plan quickly stabilizes: after roughly t ≈ 540 / 600 t\!\approx\!540/600 the global partition changes little. In the late denoising stage, entire objects (e.g., buildings, furniture, trees) are already routed into a single volume, with only fine adjustments thereafter. This temporal behavior explains the coherence of our object-level parts: coarse, semantic routing is decided early and preserved, while later steps polish details without flipping the global assignment.

[84] h4: Effects of Edge–Regularized Assignment Cost.

[85] p: Our correlation assignment operates at the patch level. Because image features are locally smooth, neighboring patches usually prefer the same part, which tends to pull an entire connected region into a single part. While desirable within an object, this behavior can mistakenly merge spatially adjacent but semantically distinct objects at contact zones (e.g., furniture touching walls or fences touching posts). As shown in Figure 5 , adding the edge regularizer cleanly separates objects that are contiguous in the image—the sofa from the corner side table in the top row, and the wooden posts from the surrounding fence in the bottom row. Compared to the version without edge regularization, the edge-aware plan yields crisper inter-object boundaries, fewer mixed parts, and improved structural fidelity, while requiring no additional instance mask supervision.

[86] h2: 5 Conclusion

[87] p: In this paper, we introduced SceneTransporter, a novel framework for structured 3D scene generation from a single image. By reframing the task as a global correlation assignment problem and solving it with an Optimal Transport layer, our method imposes powerful structural constraints directly on the generative process, effectively resolving the critical issues of structural mispartition and geometric redundancy found in existing models. Experimental results demonstrate that our method achieves state-of-the-art performance, generating complex open-world scenes with significantly improved geometric fidelity and instance-level coherence.

[88] h2: Acknowledgments

[89] p: This work is supported by the National Science and Technology Major Project of the Ministry of Science and Technology of China (No. 2025ZD1206301), the National Natural Science Foundation of China (No. 62576043), and the Natural Science Foundation of Beijing, China (No. L233006).

[90] h2: References

[91] h2: Appendix A The Use of Large Language Models

[92] p: The writing of this paper was assisted by Large Language Models (LLM). Specifically, the LLM was utilized for the following tasks:

[93] p: Improving grammar, clarity, and academic tone throughout the manuscript.

[94] p: Rephrasing and restructuring sentences and paragraphs to enhance the logical flow of our arguments.

[95] p: In accordance with ICLR policy, the human authors directed all content generation, critically reviewed and edited all model outputs, and take full and final responsibility for the claims, accuracy, and integrity of this work.

[96] h2: Appendix B Method Details

[97] h4: Debiased Clustering Probe

[98] p: To quantitatively investigate the flawed latent organization of the baseline, we designed a diagnostic probe based on unsupervised clustering. The key idea is that the constituent information for complete objects is indeed present within the generated latents, but is merely disorganized and entangled by the model’s component-based prior. Specifically, let 𝐙 A , 𝐙 B ∈ ℝ K × D \mathbf{Z}_{A},\mathbf{Z}_{B}\in\mathbb{R}^{K\times D} be the dual-volume latents generated by Tang et al. (2025) for a given scene. We stack them and apply a mild whitening:

[99] table: 𝐙 = [ 𝐙 A 𝐙 B ] , 𝐙 ~ = ( 𝐙 − 𝟏 μ ⊤ ) Σ − 1 / 2 , μ = 1 2 ​ K ∑ i = 1 2 ​ K 𝐙 i , Σ = 1 2 ​ K ∑ i = 1 2 ​ K ( 𝐙 i − μ ) ( 𝐙 i − μ ) ⊤ , \mathbf{Z}=\begin{bmatrix}\mathbf{Z}_{A}\\ \mathbf{Z}_{B}\end{bmatrix},\qquad\tilde{\mathbf{Z}}=(\mathbf{Z}-\mathbf{1}\mu^{\!\top})\,\Sigma^{-1/2},\quad\mu=\tfrac{1}{2K}\!\sum_{i=1}^{2K}\mathbf{Z}_{i},\;\;\Sigma=\tfrac{1}{2K}\!\sum_{i=1}^{2K}(\mathbf{Z}_{i}-\mu)(\mathbf{Z}_{i}-\mu)^{\!\top}, (13)

[100] p: where Σ − 1 / 2 \Sigma^{-1/2} is computed from an eigendecomposition with a small ridge for stability. Denote the whitened halves by 𝐙 ~ A , 𝐙 ~ B \tilde{\mathbf{Z}}_{A},\tilde{\mathbf{Z}}_{B} .

[101] p: Directly clustering the raw token latents often fails because the process is dominated by strong, shared nuisance factors—such as the ground plane or global style—that are non-diagnostic for object identity. To suppress these pervasive cross-volume trends, we first estimate a shared subspace between the two latent volumes ( 𝐙 ~ A , 𝐙 ~ B ) (\tilde{\mathbf{Z}}_{A},\tilde{\mathbf{Z}}_{B}) using canonical correlation analysis (CCA). CCA identifies paired directions ( 𝐮 j , 𝐯 j ) (\mathbf{u}_{j},\mathbf{v}_{j}) that maximize the correlation between the volumes’ projections. We retain all directions whose canonical correlation ρ j \rho_{j} exceeds a threshold τ \tau to define this shared subspace

[102] table: { ( ρ j , 𝐮 j , 𝐯 j ) } j ∈ 𝒥 = CCA ( 𝐙 ~ A , 𝐙 ~ B ) , 𝒥 = { j : ρ j > τ } , 𝒰 shared = span { 𝐮 j , 𝐯 j : j ∈ 𝒥 } , \{(\rho_{j},\mathbf{u}_{j},\mathbf{v}_{j})\}_{j\in\mathcal{J}}=\mathrm{CCA}(\tilde{\mathbf{Z}}_{A},\tilde{\mathbf{Z}}_{B}),\quad\mathcal{J}=\{j:\rho_{j}>\tau\},\quad\mathcal{U}_{\text{shared}}=\mathrm{span}\{\mathbf{u}_{j},\mathbf{v}_{j}:j\in\mathcal{J}\}, (14)

[103] p: where span ​ { ⋅ } \mathrm{span}\{\cdot\} denotes the set of all linear combinations of the listed vectors. Let 𝐔 \mathbf{U} be a column-orthonormal basis of 𝒰 shared \mathcal{U}_{\text{shared}} and 𝐏 = 𝐔𝐔 ⊤ \mathbf{P}=\mathbf{U}\mathbf{U}^{\top} the orthogonal projector. We obtain debiased tokens by removing their shared component:

[104] table: 𝐙 ^ A = 𝐙 ~ A − 𝐙 ~ A ​ 𝐏 , 𝐙 ^ B = 𝐙 ~ B − 𝐙 ~ B ​ 𝐏 . \hat{\mathbf{Z}}_{A}=\tilde{\mathbf{Z}}_{A}-\tilde{\mathbf{Z}}_{A}\mathbf{P},\qquad\hat{\mathbf{Z}}_{B}=\tilde{\mathbf{Z}}_{B}-\tilde{\mathbf{Z}}_{B}\mathbf{P}. (15)

[105] p: Intuitively, ( 15 ) down-weights the high-variance global modes while preserving object-specific variation. We then cluster the debiased tokens 𝐙 ^ = [ 𝐙 ^ A ; 𝐙 ^ B ] \hat{\mathbf{Z}}=[\hat{\mathbf{Z}}_{A};\hat{\mathbf{Z}}_{B}] with a flexible Gaussian mixture

[106] table: 𝐙 ^ ∼ ∑ c = 1 C π c ​ 𝒩 ​ ( 𝝁 c , 𝚺 c ) , C = 2 , \hat{\mathbf{Z}}\ \sim\ \sum_{c=1}^{C}\pi_{c}\,\mathcal{N}(\bm{\mu}_{c},\bm{\Sigma}_{c}),\qquad C=2, (16)

[107] p: and denote by γ i ​ c \gamma_{ic} the posterior responsibility of component c c for token i i . To improve robustness, tokens with low maximum confidence ( max c ⁡ γ i ​ c < δ \max_{c}\gamma_{ic}<\delta ) are reassigned to the nearest centroid computed from high-confidence members ( max c ⁡ γ i ​ c ≥ δ \max_{c}\gamma_{ic}\geq\delta ). Finally, grouped tokens are decoded independently with the frozen VAE decoder to visualize the resulting object-level organization.

[108] h2: Appendix C Experiment Settings

[109] h3: C.1 Hyperparameters

[110] p: Table 3 provides the hyperparameters needed to replicate our experiments.

[111] figure: Table 3: Hyperparameters of OT plan–gated cross-attention used in all experiments. Symbol Description Value ε t \varepsilon_{t} Entropic regularization weight 0.10 0.10 λ edge \lambda_{\text{edge}} Edge regularization strength 0.8 0.8 γ edge \gamma_{\text{edge}} Edge sensitivity 8.0 8.0 λ t \lambda_{t} Guidance strength 2.5 2.5 ε g \varepsilon_{g} Floor term 0.02 0.02 K OT K_{\text{OT}} Number of Sinkhorn iterations 40 40

[112] h3: C.2 Human evaluation.

[113] p: In our user study, we compare our method with three baselines (MIDI ( Huang et al., 2025 ) , PartCrafter ( Lin et al., 2025b ) , and PartPacker ( Tang et al., 2025 ) ) on perceptual quality. For each reference image, all four methods generate a structured 3D scene, which we export as .glb meshes. These meshes are loaded into a web-based 3D viewer with identical lighting and shading settings. The four methods are assigned to labels A–D in a single random permutation, and the corresponding meshes are displayed side-by-side under these labels. Participants can freely rotate, zoom, and inspect each mesh interactively.

[114] p: We recruit a total of 30 participants (graduate students and researchers in computer vision/graphics not involved in this project). For each reference image they are shown, participants evaluate the four methods along three dimensions. Specifically, they are asked to rank the four scenes (A–D) from 1 (lowest) to 4 (highest) for each of the following questions:

[115] p: Geometry Quality: “ Please rank the overall geometry quality of each scene. ” This metric evaluates how detailed, precise, and faithful to the reference image the geometry of each scene is, including fine-grained structures and overall shape fidelity.

[116] p: Layout Coherence: “ Please rank the overall spatial layout and arrangement of objects in each scene relative to the reference image. ” This measures how coherent the scene layout is, and how well object positions, scales, and composition align with the input image.

[117] p: Segmentation Plausibility: “ Please rank the overall plausibility of the object-level part decomposition in each scene. ” This assesses to what extent each scene exhibits clear, reasonable instances with minimal overlaps, missing regions, or mixed parts.

[118] p: For each method and each criterion, we compute the average rank over all evaluated images and participants. These averaged scores are reported in Table 2 of the main paper, where higher values indicate stronger human preference. Our method achieves the highest average rank across all three dimensions, suggesting more coherent object-level parts, reduced feature leakage, and better scene-wide layout consistency.

[119] h2: Appendix D Additional Experiments

[120] h3: D.1 Real-world Results

[121] p: In our current setting, all methods (including the baselines) are trained on synthetically rendered scenes, which allows us to construct a large and diverse training set with consistent part-level annotations. To test the generalization ability of our model to natural photographs, we perform zero-shot evaluation on real-world images from the DL3DV-10K dataset ( Ling et al., 2024 ) .

[122] p: As expected, directly applying the synthetic-trained model to raw photographs leads to a noticeable performance drop due to the appearance domain gap. Following the strategy proposed in PartCrafter ( Lin et al., 2025b ) , we therefore explore transferring the style of real-world images to make them look more like images rendered from a graphics engine using recent image editing models, such as GPT-5. Specifically, we use prompts of the form: “Preserve all details and perform image-to-image style transfer to convert the image into the style of a 3D rendering (Objaverse-style rendering).” The style-transferred images preserve the original scene layout and object identities, while matching the rendering statistics of our synthetic training data.

[123] p: Under this simple, purely test-time preprocessing, our method produces significantly more faithful and coherent 3D scene reconstructions: objects are better separated, part boundaries align more closely with image evidence, and the overall layout matches the input photograph more accurately. As shown in Figure 8 , this simple strategy works surprisingly well on a variety of indoor and outdoor real-world scenes.

[124] figure: Figure 8: Qualitative Results on Structured 3D Scene Generation from Real-World Images. We use a GPT-5–based image editing model to transfer the style of real-world images, making them look like images rendered from a graphics engine.

[125] h3: D.2 Convergence Analysis of the Entropic OT Solver

[126] p: In each OT-gated cross-attention layer, we solve a small entropic optimal transport (OT) problem between two “rolls” of part queries and M M image tokens. Given a cost matrix C ∈ ℝ 2 × M C\in\mathbb{R}^{2\times M} , row marginals μ ∈ ℝ 2 \mu\in\mathbb{R}^{2} and column marginals ν ∈ ℝ M \nu\in\mathbb{R}^{M} , we minimize

[127] table: min A ≥ 0 ⁡ ⟨ C , A ⟩ + ε ​ H ​ ( A ) s.t. A ​ 𝟏 = μ , A ⊤ ​ 𝟏 = ν , \min_{A\geq 0}\;\langle C,A\rangle+\varepsilon H(A)\quad\text{s.t.}\quad A\mathbf{1}=\mu,\;\;A^{\top}\mathbf{1}=\nu, (17)

[128] p: where A ∈ ℝ 2 × M A\in\mathbb{R}^{2\times M} is the transport plan, ε > 0 \varepsilon>0 is the entropic regularization strength, and H ⁡ ( A ) = ∑ i ​ j A i ​ j ​ log ⁡ A i ​ j H(A)=\sum_{ij}A_{ij}\log A_{ij} is the negative-entropy regularizer.

[129] p: Following the standard dual formulation of entropic OT, we introduce dual potentials f ∈ ℝ 2 f\in\mathbb{R}^{2} (for the row constraints) and g ∈ ℝ M g\in\mathbb{R}^{M} (for the column constraints). At Sinkhorn iteration k k , the corresponding transport plan has the form

[130] table: A i ​ j ( k ) ∝ exp ⁡ ( f i ( k ) + g j ( k ) − C i ​ j ε ) , A^{(k)}_{ij}\;\propto\;\exp\!\Big(\tfrac{f^{(k)}_{i}+g^{(k)}_{j}-C_{ij}}{\varepsilon}\Big), (18)

[131] p: followed by a normalization step to enforce the marginal constraints A ( k ) ​ 𝟏 ≈ μ A^{(k)}\mathbf{1}\approx\mu and ( A ( k ) ) ⊤ ​ 𝟏 ≈ ν (A^{(k)})^{\top}\mathbf{1}\approx\nu . A fixed point of the Sinkhorn updates corresponds to a stationary solution of the entropic OT problem equation 17 .

[132] h4: Monitored residuals.

[133] p: To assess optimization stability and convergence in practice, we instrument our entropic OT solver and log convergence statistics for all OT-gated cross-attention layers. For each Sinkhorn solve, at each iteration k k we record the following residuals:

[134] p: Dual updates : the ℓ 2 \ell_{2} norms of the changes in the dual variables

[135] table: r f ( k ) = ‖ f ( k + 1 ) − f ( k ) ‖ 2 , r g ( k ) = ‖ g ( k + 1 ) − g ( k ) ‖ 2 . r_{f}^{(k)}=\big\|f^{(k+1)}-f^{(k)}\big\|_{2},\qquad r_{g}^{(k)}=\big\|g^{(k+1)}-g^{(k)}\big\|_{2}. (19)

[136] p: These measure how much the dual potentials still move between two successive iterations.

[137] p: Transport-plan update : the Frobenius norm of the change in the transport plan

[138] table: r A ( k ) = ‖ A ( k + 1 ) − A ( k ) ‖ F , r_{A}^{(k)}=\big\|A^{(k+1)}-A^{(k)}\big\|_{F}, (20)

[139] p: which quantifies how much the routing plan is still being updated.

[140] p: Marginal-constraint violation : the deviation of the current plan from the prescribed marginals,

[141] table: r row ( k ) = 1 2 ​ ∑ i = 1 2 | ( A ( k ) ​ 𝟏 ) i − μ i | , r col ( k ) = 1 M ​ ∑ j = 1 M | ( ( A ( k ) ) ⊤ ​ 𝟏 ) j − ν j | , r_{\text{row}}^{(k)}=\frac{1}{2}\sum_{i=1}^{2}\big|(A^{(k)}\mathbf{1})_{i}-\mu_{i}\big|,\qquad r_{\text{col}}^{(k)}=\frac{1}{M}\sum_{j=1}^{M}\big|((A^{(k)})^{\top}\mathbf{1})_{j}-\nu_{j}\big|, (21)

[142] p: and we report their sum

[143] table: r marg ( k ) = r row ( k ) + r col ( k ) . r_{\text{marg}}^{(k)}=r_{\text{row}}^{(k)}+r_{\text{col}}^{(k)}. (22)

[144] p: Intuitively, r marg ( k ) r_{\text{marg}}^{(k)} measures how well the current A ( k ) A^{(k)} satisfies the OT marginal constraints.

[145] p: In words, r f ( k ) r_{f}^{(k)} , r g ( k ) r_{g}^{(k)} and r A ( k ) r_{A}^{(k)} tell us whether the dual variables and the transport plan have stabilized, while r marg ( k ) r_{\text{marg}}^{(k)} indicates how strictly the mass conservation constraints are enforced. Figure. 9 visualizes these quantities for three OT-gated cross-attention layers. For each layer, we run the Sinkhorn solver with a fixed number of iterations (40 in all our experiments) and plot the residuals r f ( k ) r_{f}^{(k)} , r g ( k ) r_{g}^{(k)} , r A ( k ) r_{A}^{(k)} and r marg ( k ) r_{\text{marg}}^{(k)} as a function of the iteration index k k .

[146] p: Across all OT-gated layers and across different denoising steps, we observe a consistent pattern: the dual and plan residuals r f ( k ) r_{f}^{(k)} , r g ( k ) r_{g}^{(k)} , and r A ( k ) r_{A}^{(k)} drop by 3 3 – 5 5 orders of magnitude within only 3 3 – 5 5 Sinkhorn iterations and then remain numerically flat, while the marginal-constraint violation r marg ( k ) r_{\text{marg}}^{(k)} quickly converges to a very small value and stays stable without oscillation or divergence. This indicates that the entropic OT subproblem in our setting is well-conditioned and that our solver converges rapidly and stably under the default choice of 40 iterations used in all experiments.

[147] figure: Figure 9: Convergence of the entropic OT solver across OT-gated cross-attention layers. We plot the residuals of the dual variables and transport plan, as well as the marginal-constraint violation, for three representative OT-gated cross-attention layers.

[148] h3: D.3 Additional Ablation Studies

[149] p: Table 4 presents quantitative ablations regarding the core components and hyperparameters of our OT-guided routing mechanism. The key observations are summarized below.

[150] h4: Impact of OT Plan–Gated Attention and Edge-Regularized Cost.

[151] p: Rows (a.1)–(a.3) isolate the contributions of the proposed OT modules. The removal of the OT Plan–Gated Cross-Attention (a.1) precipitates a discernible drop in Geometry Fidelity (e.g., ULIP decrease) and a marked deterioration in IOU metrics. This empirical evidence substantiates our hypothesis that enforcing a one-to-one, capacity-constrained patch-to-part routing is critical for mitigating feature leakage and suppressing redundant geometry. Furthermore, while retaining OT gating but omitting the Edge-Regularized Assignment Cost (a.2) improves upon the baseline, the IoU metrics remain suboptimal compared to the full configuration. The full model (a.3) attains superior performance across all metrics, confirming that edge-aware smoothing effectively refines object separation without compromising global geometric fidelity. In terms of efficiency, the inclusion of OT modules introduces a manageable computational overhead (increasing inference time from 47.4 47.4 ,s to 55.0 55.0 ,s), while memory consumption remains negligible.

[152] h4: Effect of OT Hyperparameters.

[153] p: We further analyze the sensitivity of our method to key hyperparameters in Rows (b)–(d). First, varying the entropic regularization ε t \varepsilon_{t} (Rows b.1–b.4) reveals that ε t = 0.10 \varepsilon_{t}=0.10 yields the optimal trade-off. Deviating to lower or higher values disrupts the balance between transport plan sparsity and smoothness, leading to a degradation in both geometric fidelity (ULIP/Uni3D) and part disentanglement metrics. Second, regarding the edge sensitivity γ edge \gamma_{\text{edge}} (Rows c.1–c.4), a lower value ( 6.0 6.0 ) relaxes boundary constraints, which marginally benefits global geometry (highest ULIP) but causes leakage across object boundaries (increased IoU max \text{IoU}_{\max} ). Conversely, excessive sensitivity ( ≥ 10.0 \geq 10.0 ) over-constrains the routing, harming all metrics. Our default γ edge = 8.0 \gamma_{\text{edge}}=8.0 strikes the best balance. Finally, for the edge-smoothing weight λ edge \lambda_{\text{edge}} (Rows d.1–d.3), we observe that sufficient smoothing is required to enforce intra-part coherence. Setting λ edge \lambda_{\text{edge}} too low ( 0.6 0.6 ) or too high ( 1.0 1.0 ) results in suboptimal segmentation, evident from the sharp rise in IoU max \text{IoU}_{\max} . The default λ edge = 0.8 \lambda_{\text{edge}}=0.8 consistently achieves superior performance, demonstrating that the method is robust within a reasonable range around the optimal settings.

[154] h4: Number of OT-Gated DiT Blocks.

[155] p: Finally, Rows (e.1)–(e.3) investigate the optimal density of OT Plan–Gated Cross-Attention within the DiT architecture. Restricting OT integration to only one-third of the blocks (e.1) yields some geometric improvement over the baseline but proves insufficient for effective part separation, as evidenced by suboptimal IoU metrics. Increasing the coverage to half of the blocks (e.2, our default) precipitates a substantial gain in both Geometry Fidelity and Part Disentanglement. Crucially, this setting maintains a moderate runtime, incurring only a reasonable overhead compared to the baseline. Applying OT to all blocks (e.3) provides marginal gains in specific geometry metrics (e.g., ULIP-2) but leads to diminishing returns—or even slight degradation—in part metrics, while imposing a significant latency penalty. These results indicate that integrating OT into approximately half of the layers offers the most favorable trade-off between structural disentanglement and computational efficiency.

[156] figure: Setting Geometry Fidelity Part Disentanglement Inference Time (s) Inference Memory (M) ULIP ↑ \uparrow ULIP-2 ↑ \uparrow Uni3D ↑ \uparrow IoU max ↓ {}_{\text{max}}\downarrow IoU mean ↓ {}_{\text{mean}}\downarrow (a.1) w/o OT Plan–Gated Cross–Attention 0.1417 0.3083 0.2887 0.0319 0.2142 47.41 9030 (a.2) w/o Edge–Regularized Assignment Cost 0.1452 0.3164 0.2916 0.0241 0.1136 54.61 9068 (a.3) Full model 0.1466 0.3220 0.3021 0.0101 0.0926 54.99 9070 (b.1) ε t = 0.08 \varepsilon_{t}=0.08 0.1460 0.3184 0.3003 0.0117 0.0914 55.30 9070 (b.2) ε t = 0.10 ∗ \varepsilon_{t}=0.10^{*} 0.1466 0.3220 0.3021 0.0101 0.0926 54.99 9070 (b.3) ε t = 0.12 \varepsilon_{t}=0.12 0.1437 0.3185 0.2970 0.1239 0.1119 55.12 9070 (b.4) ε t = 0.14 \varepsilon_{t}=0.14 0.1424 0.3178 0.2937 0.0159 0.0936 55.02 9070 (c.1) γ edge = 6.0 \gamma_{\text{edge}}=6.0 0.1488 0.3239 0.3014 0.0243 0.0936 56.17 9070 (c.2) γ edge = 8.0 ∗ \gamma_{\text{edge}}=8.0^{*} 0.1466 0.3220 0.3021 0.0101 0.0926 54.99 9070 (c.3) γ edge = 10.0 \gamma_{\text{edge}}=10.0 0.1457 0.3182 0.3029 0.0570 0.1113 55.17 9070 (c.4) γ edge = 12.0 \gamma_{\text{edge}}=12.0 0.1426 0.3156 0.3003 0.1149 0.0994 55.89 9070 (d.1) λ edge = 0.6 \lambda_{\text{edge}}=0.6 0.1456 0.3236 0.3003 0.0609 0.1128 53.59 9070 (d.2) λ edge = 0.8 ∗ \lambda_{\text{edge}}=0.8^{*} 0.1466 0.3220 0.3021 0.0101 0.0926 53.97 9070 (d.3) λ edge = 1.0 \lambda_{\text{edge}}=1.0 0.1439 0.3204 0.3017 0.1482 0.0952 55.17 9070 (e.1) w 1/3 DiT blocks 0.1465 0.3170 0.3004 0.0992 0.1061 51.89 9070 (e.2) w 1/2 DiT blocks ∗ 0.1466 0.3220 0.3021 0.0101 0.0926 54.99 9070 (e.3) w all DiT blocks 0.1426 0.3262 0.3022 0.0207 0.0830 65.24 9070 Table 4: Comparison of metrics for ablation. Bold values indicate the best scores, while underlined values indicate the second-best scores among the fair comparison. Asterisk ( ∗ * ) indicates the default settings in our method.

[157] figure: Figure 10: Effect of adding a residual vanilla cross-attention branch. Left to right: input image, PartPacker baseline, our OT-guided routing, and our OT-guided routing with an additional residual cross-attention branch (Ours_residual), which recovers the small crowded instances (e.g., boats) while preserving the improved global layout and part separation.

[158] h3: D.4 Failure Cases and Residual Diagnostic

[159] h4: Crowded tiny instances.

[160] p: In scenes with very dense clusters of small, similar objects that share only a few image patches (e.g., tightly packed boats or trees), the OT-guided routing can allocate most capacity to the strongest responses and effectively merge a few weak instances into their neighbours. This may slightly under-count very small repeated objects, while the global layout (buildings, roads, docks, etc.) remains correct. We find that adding a small residual branch of vanilla cross-attention on top of the OT-gated attention largely mitigates this issue, keeping the OT plan as a low-frequency structural prior and using the residual attention to recover high-frequency local details. Figure 10 visualizes a representative example, comparing (i) the baseline, (ii) SceneTransporter with pure OT-guided routing, and (iii) SceneTransporter with the residual cross-attention branch: the residual variant recovers the missing tiny instances while preserving the cleaner global structure of OT.

[161] h4: Geometry artifacts.

[162] p: We occasionally see nonsmooth surfaces or floating parts when the denoising schedule is too short or the number of tokens is too small. Increasing the number of diffusion steps or the token budget alleviates these cases, and the resulting artifacts are typically local and do not affect the overall scene layout.

[163] h4: Out-of-distribution appearance.

[164] p: Since the model is trained on synthetic rendered images, strongly out-of-distribution real images (e.g., unusual lighting or textures) can lead to degraded geometry and part grouping. As discussed in Appendix D.1 , applying automated style transfer to convert real images into a 3D-rendering style significantly improves the results, and SceneTransporter still produces plausible structured scenes on many challenging real-world inputs.

[165] h2: Instructions for reporting errors

[166] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[167] p: Tip: You can select the relevant text first, to include it in your report.

[168] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[169] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
