[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Easy3E: Feed-Forward 3D Asset Editing via Rectified Voxel Flow

[3] h6: Abstract

[4] p: Existing 3D editing methods rely on computationally intensive scene-by-scene iterative optimization and suffer from multi-view inconsistency. We propose an effective and fully feedforward 3D editing framework based on the TRELLIS generative backbone, capable of modifying 3D models from a single editing view. Our framework addresses two key issues: adapting training-free 2D editing to structured 3D representations, and overcoming the bottleneck of appearance fidelity in compressed 3D features. To ensure geometric consistency, we introduce Voxel FlowEdit, an edit-driven flow in the sparse voxel latent space that achieves globally consistent 3D deformation in a single pass. To restore high-fidelity details, we develop a normal-guided single to multi-view generation module as an external appearance prior, successfully recovering high-frequency textures. Experiments demonstrate that our method enables fast, globally consistent, and high-fidelity 3D model editing.

[5] figure: Figure 1 : We introduce Easy3E, a novel method for 3D asset editing. Guided by a single edited view and a coarse 3D mask, our method can perform both significant geometric changes and fine-grained appearance edits. Easy3E efficiently produces globally consistent and high-fidelity 3D results, demonstrating its power and flexibility across diverse assets.

[6] p: ∗ Corresponding Author.

[7] h2: 1 Introduction

[8] p: 3D asset editing is a fundamental task in numerous applications, such as gaming, film production, architectural visualization, and emerging fields like AR/VR and digital twins. Therefore, developing intuitive and efficient editing tools has been a long-standing challenge in computer graphics and 3D computer vision. The primary goal is to enable users to perform complex 3D modifications through simple and easy-to-use inputs, such as 2D conditions or text prompts. A framework that can translate these user inputs into coherent and high-fidelity 3D results will significantly simplify the content creation process and make 3D editing easily accessible to more users.

[9] p: Existing 3D editing methods span multiple paradigms. Classical approaches follow the 2D-lifting pipeline [ 11 , 42 , 55 ] , where edited 2D images supervise the optimization of a 3D representation (e.g., NeRF [ 29 ] or 3DGS [ 17 ] ). Although effective for appearance-level edits, these optimization-based methods require per-scene iterative refinement and depend heavily on multi-view coverage, making them fragile when the edit introduces noticeable geometric deviation from the original asset. More recent works adopt multi-view or view-consistent diffusion models [ 1 ] , which improve cross-view consistency but still operate in a 2D-native feature space, requiring the model to infer 3D structure implicitly during generation. Such implicit reasoning limits their ability to handle edits that alter shape, topology, or volumetric occupancy, as 2D features alone provide insufficient cues for reliable 3D structural inference. Both categories rely on image-space features and therefore struggle with large geometric changes and precise structural control, especially when edits demand explicit, globally consistent manipulations of the underlying 3D structure.

[10] p: In contrast, 3D-native generative models [ 14 , 40 , 45 ] learn explicit, structured 3D latent fields directly from data. These representations encode geometry natively rather than reconstructing it from multiple images, opening a fundamentally different editing perspective: instead of optimizing a 3D scene or manipulating multi-view features, one can directly modify the underlying structured 3D latent space where geometry is explicitly parameterized. This paradigm promises feed-forward, globally coherent 3D editing, but introduces two key challenges.

[11] p: First, the lack of paired 3D editing data necessitates adapting training-free 2D editing techniques [ 12 , 28 , 30 ] to 3D latent fields. However, many 2D methods depend on architectural components that do not transfer to 3D, such as manipulations of cross-attention maps [ 12 , 4 ] or 2D-specific feature maps [ 41 ] . Second, structured 3D generative models [ 14 , 45 ] utilize compact latent tokens to ensure geometric consistency and fast inference. This compression limits their ability to represent high-frequency texture details, leading to oversmoothed or low-fidelity appearance. Thus, the core technical questions are: (1) how to redesign training-free 2D editing approaches to operate on structured 3D latent spaces, and (2) how to restore high-quality texture details on edited geometry given limited 3D appearance priors.

[12] p: To address these challenges, we propose a fully feed-forward 3D editing framework built on the TRELLIS generative backbone [ 45 ] . Given a single edited view and a user-defined editable region, our method performs both geometric and appearance editing directly in TRELLIS’s sparse voxel latent space. We introduce Voxel FlowEdit, a latent-space editing mechanism that translates source voxel to target voxel via an adapted velocity field, enabling globally coherent geometric deformation in a single pass. Following this coarse transformation, we apply a structured latent repainting stage to locally refine geometry and appearance while anchoring unedited regions, ensuring consistency and detail preservation.

[13] p: To overcome the limited appearance priors of 3D generative models, we further incorporate an optional normal-guided multi-view generative module. It synthesizes high-fidelity auxiliary views aligned with the edited geometry, providing rich 2D appearance cues that enhance texture realism in the final 3D asset.

[14] p: In summary, our main contributions are as follows:

[15] p: We construct an effective and feed-forward framework that leverages the powerful prior of 3D generative models to enable efficient and high-quality 3D asset editing from a single edited view.

[16] p: We introduce Voxel FlowEdit, a voxel-flow editing mechanism. It constructs the translation of source/target 3D assets within the sparse voxel latent space by utilizing a specially adapted velocity field, achieving globally coherent 3D geometric deformation.

[17] p: We develop a dedicated normal-guided single-to-multi-view generation model which serves as an external appearance prior to overcome the limitation of compressed 3D appearance representations, restoring high-fidelity textures onto the edited geometry.

[18] h2: 2 Related Work

[19] h4: 3D Model Generation.

[20] p: Recent progress in 3D generative modeling has evolved from lifting 2D observations into 3D structures [ 34 , 22 ] to learning fully 3D-native representations that jointly model geometry and appearance [ 14 ] . Early image-to-3D frameworks employed NeRF or mesh decoders to reconstruct textured assets from single or few views [ 29 , 32 , 53 , 33 ] , while subsequent diffusion-based pipelines further leveraged pretrained 2D priors for text-to-3D synthesis via score distillation [ 34 , 43 , 22 , 36 ] . To improve view consistency and scalability, several works proposed generating multi-view images as intermediate supervision before reconstructing 3D assets [ 26 , 48 , 39 , 25 ] , achieving better alignment but still constrained by 2D lifting. More recently, large-scale 3D-native frameworks have emerged, learning structured latent spaces or volumetric primitives directly from massive 3D corpora [ 14 , 40 , 47 , 54 , 45 , 21 ] . These models enable feed-forward generation of meshes, radiance fields, or 3D Gaussian representations conditioned on images or text, substantially advancing fidelity and controllability. Our study builds upon this trajectory, focusing on efficient and consistent 3D editing within a structured latent space.

[21] h4: 2D Image Editing.

[22] p: Early diffusion-based image editing typically reconstructs a given image by inverting it into the latent space of a pretrained model and then applying localized manipulations via attention control, prompt/mask guidance, or latent blending to realize semantic and structural changes [ 12 , 16 , 28 , 30 , 4 , 46 , 41 , 49 ] . In parallel, training-based approaches adapt the generator or lightweight adapters to the target domain (e.g., identity or structure), improving edit fidelity and controllability through finetuning or conditioning modules such as DreamBooth [ 37 , 19 ] , LoRA [ 15 ] , and ControlNet [ 51 , 10 ] . In contrast to diffusion-style U-Net editors, inversion-free flow-matching formulations directly construct continuous source–target transformations in the learned velocity field, avoiding iterative inversion and aligning naturally with DiT-style architectures [ 24 , 18 , 31 ] . Given that paired 3D editing data are largely unavailable and that the underlying generative backbone adopts a flow-matching formulation [ 24 , 27 ] , this compatibility makes the flow-based editing paradigm particularly well suited to our setting.

[23] h4: 3D Model Editing.

[24] p: Recent 3D editing methods can be broadly characterized by how 2D guidance is coupled to the 3D representation. A first line iteratively optimizes a 3D representation by supervising rendered views with images edited by pretrained 2D models (e.g., text or mask conditioned), typically via score-distillation losses or gradient guidance [ 11 , 55 , 38 ] . Building on this setup, subsequent work improves robustness and efficiency by synchronizing multi-view constraints or imposing geometry-aware priors during optimization [ 2 , 44 , 3 ] . A parallel direction leverages multi-view or video diffusion to produce edited view sets with stronger viewpoint coverage and spatial–temporal regularization before lifting back to 3D, enabling multi-view propagation of edits [ 6 ] . More recently, 3D-native generative backbones have begun to explore feed-forward editing. These approaches typically rely on local mechanisms such as masked reconstruction [ 8 ] or multi-view inpainting [ 1 ] to localize changes. While these methods improve efficiency, their reliance on local masking or inpainting often limits them to textural changes or simple additions, struggling with edits that require globally coherent geometric deformation. This highlights a critical need for a new paradigm that can propagate complex edits throughout the 3D latent space in a single pass.

[25] h2: 3 Method

[26] figure: Figure 2 : Overview of Easy3E. The framework operates in two main stages: Geometry Editing and Texture Refinement. Starting from a rendered source view, an edited target image provides the guidance for editing. In the Geometry Editing stage, the Voxel FlowEdit algorithm transforms the source voxel structure under flow-based guidance, followed by SLAT Repainting that refines local latent features to produce the target mesh. The Texture Refinement stage then employs a generation branch and a normal-guided control adapter to synthesize multi-view-consistent textures, which are projected and fused onto the mesh to yield the final high-fidelity 3D asset.

[27] p: We introduce an effective, feed-forward framework that achieves high-fidelity 3D asset editing. Given a source 3D asset 𝒜 src \mathcal{A}_{\text{src}} , a 3D region mask ℳ \mathcal{M} , and a target image I tgt I^{\text{tgt}} obtained by editing a rendered view I src I^{\text{src}} , our method produces an edited asset with consistent geometry and appearance.

[28] p: The overall pipeline is illustrated in Fig. 2 . We first establish our model foundation by formalizing the structured latent representation ( Sec. 3.1 ). For precise geometric editing in the 3D sparse voxel domain, we introduce a novel Flow Matching-based voxel editing algorithm ( Sec. 3.2 ). For generating new latent features that define the edited geometry and appearance while maintaining source consistency, we propose a SLAT repainting technique ( Sec. 3.3 ). Finally, for enhancing visual realism, we employ a texture refinement module that improves fidelity using normal-guided multi-view images generation ( Sec. 3.4 ).

[29] h3: 3.1 Structured Latent Representation

[30] p: Our editing method operates directly in the structured 3D latent space used by TRELLIS [ 45 ] . Specifically, the Structured LATent (SLAT) representation is defined as

[31] table: 𝐙 = ( 𝒱 , { 𝐳 𝐩 } 𝐩 ∈ 𝒱 ) , \mathbf{Z}=\big(\mathcal{V},\,\{\mathbf{z}_{\mathbf{p}}\}_{\mathbf{p}\in\mathcal{V}}\big),

[32] p: where the active voxel set 𝒱 \mathcal{V} consists of voxels that intersect the surface of the 3D mesh, and 𝐳 𝐩 \mathbf{z}_{\mathbf{p}} is a local latent feature attached to each active voxel. The local latent features are obtained by fusing multi-view image features (e.g., DINOv2) projected onto these voxels. TRELLIS uses two rectified flow transformers to respectively predict the voxel structure 𝒱 \mathcal{V} and the local latent field { 𝐳 𝐩 } \{\mathbf{z}_{\mathbf{p}}\} . The resulting SLAT representation can be further decoded into 3DGS, mesh, or NeRF.

[33] p: TRELLIS is trained under the rectified flow framework, which learns a deterministic velocity field

[34] table: d ​ 𝐱 d ​ t = 𝐯 θ ​ ( 𝐱 , t ) , \frac{d\mathbf{x}}{dt}=\mathbf{v}_{\theta}(\mathbf{x},t),

[35] p: following a linear path

[36] table: 𝐱 ⁡ ( t ) = ( 1 − t ) ​ 𝐱 0 + t ​ 𝐱 1 , \mathbf{x}(t)=(1-t)\mathbf{x}_{0}+t\mathbf{x}_{1},

[37] p: where 𝐱 0 \mathbf{x}_{0} is a clean sample from the SLAT data distribution at t = 0 t=0 , and 𝐱 1 \mathbf{x}_{1} is its corresponding noise sample at t = 1 t=1 . This noise-to-data formulation provides the flow-based perspective on which we construct edit-driven trajectories in the structured latent space.

[38] h3: 3.2 Sparse Voxel Editing

[39] p: Our editing process begins at the structural level. The voxel structure 𝒱 \mathcal{V} is represented as a binary occupancy grid, which is encoded by a 3D VAE into a low-dimensional continuous latent vector 𝐱 \mathbf{x} . Our goal is to propagate 2D edit signals through this latent voxel space and transform the source latent 𝐱 src \mathbf{x}^{\text{src}} into a target latent 𝐱 tgt \mathbf{x}^{\text{tgt}} conditioned on the target image I tgt I^{\text{tgt}} .

[40] p: Editing Trajectory Modeling. Inspired by FlowEdit [ 18 ] , we model the structural editing process as a continuous trajectory in the latent space. Let 𝐱 t \mathbf{x}_{t} denote the latent structural state at time t ∈ [ 0 , 1 ] t\!\in[0,1] , and let 𝐯 edit ​ ( 𝐱 t , t ) \mathbf{v}_{\text{edit}}(\mathbf{x}_{t},t) be the edit-driven velocity field. The trajectory is defined by the masked ODE

[41] table: d ​ 𝐱 t = ℳ ℓ ⊙ 𝐯 edit ​ ( 𝐱 t , t ) ​ d ​ t , \mathrm{d}\mathbf{x}_{t}=\mathcal{M}_{\ell}\odot\mathbf{v}_{\text{edit}}(\mathbf{x}_{t},t)\,\mathrm{d}t, (1)

[42] p: where ℳ ℓ \mathcal{M}_{\ell} restricts updates to the editable region. Following the rectified-flow convention, we set

[43] table: 𝐱 t = 1 = 𝐱 src , 𝐱 t = 0 = 𝐱 tgt , \mathbf{x}_{t=1}=\mathbf{x}^{\text{src}},\qquad\mathbf{x}_{t=0}=\mathbf{x}^{\text{tgt}},

[44] p: so that integrating the ODE traces a continuous path from the source latent structure to the desired edited one.

[45] p: We construct 𝐯 edit \mathbf{v}_{\text{edit}} by differencing the flow trajectories of the pretrained model under the source and target conditions. For each condition c ∈ { src , tgt } c\in\{\text{src},\,\text{tgt}\} , the rectified-flow formulation specifies a linear latent path

[46] table: 𝐱 t c = ( 1 − t ) ​ 𝐱 0 c + t ​ 𝐱 1 c , \mathbf{x}^{c}_{t}=(1-t)\,\mathbf{x}^{c}_{0}+t\,\mathbf{x}^{c}_{1},

[47] p: connecting a clean endpoint 𝐱 0 c \mathbf{x}^{c}_{0} and a noisy endpoint 𝐱 1 c \mathbf{x}^{c}_{1} . The velocity network satisfies

[48] table: d ​ 𝐱 t c d ​ t = 𝐯 θ ​ ( 𝐱 t c , t ∣ I c ) . \frac{d\mathbf{x}^{c}_{t}}{dt}=\mathbf{v}_{\theta}(\mathbf{x}^{c}_{t},t\mid I^{c}).

[49] p: We impose a shared terminal noise state 𝐱 1 src = 𝐱 1 tgt \mathbf{x}^{\text{src}}_{1}=\mathbf{x}^{\text{tgt}}_{1} and construct an interpolated path that matches our ODE boundary conditions:

[50] table: 𝐱 t = 𝐱 0 src − 𝐱 t src + 𝐱 t tgt . \mathbf{x}_{t}=\mathbf{x}^{\text{src}}_{0}-\mathbf{x}^{\text{src}}_{t}+\mathbf{x}^{\text{tgt}}_{t}.

[51] p: Differentiating this path yields the edit velocity:

[52] table: 𝐯 edit ​ ( 𝐱 t , t ) = 𝐯 θ ​ ( 𝐱 t tgt , t ∣ I tgt ) − 𝐯 θ ​ ( 𝐱 t src , t ∣ I src ) . \mathbf{v}_{\text{edit}}(\mathbf{x}_{t},t)=\mathbf{v}_{\theta}(\mathbf{x}^{\text{tgt}}_{t},t\mid I^{\text{tgt}})-\mathbf{v}_{\theta}(\mathbf{x}^{\text{src}}_{t},t\mid I^{\text{src}}). (2)

[53] p: The geometric definition of this vector is visualized in Figure 3 (a).

[54] figure: Figure 3 : Comparison of FlowEdit’s limitations and the Voxel FlowEdit solution. (a) Base FlowEdit: The semantic velocity 𝐯 edit \mathbf{v}_{\text{edit}} is corrupted by accumulated approximation error, causing the trajectory to drift and resulting in structural corruption (red dashed box). (b) Voxel FlowEdit: The edit is driven by external gradient guidance 𝐆 sil \mathbf{G}_{\text{sil}} , while internal correction 𝝃 traj \boldsymbol{\xi}_{\text{traj}} maintains manifold consistency. This combined approach achieves a clean and structurally integral edit.

[55] p: Guided Flow Regularization. The base ODE in Eq. 1 provides an efficient initialization for 3D structural editing. Following FlowEdit [ 18 ] , the editing velocity 𝐯 edit \mathbf{v}_{\text{edit}} is estimated by averaging conditional velocity differences over multiple noise samples.

[56] p: However, this baseline often over-preserves the source structure and fails to fully reach the target edit (Fig. 3 (a)), likely due to discretization errors that push the trajectory off the data manifold. To mitigate this drift, we introduce auxiliary guidance terms that refine the evolution while preserving the underlying flow dynamics.

[57] p: We introduce a silhouette-guidance term based on the energy

[58] table: ℰ sil ​ ( 𝐱 ) \displaystyle\mathcal{E}_{\text{sil}}(\mathbf{x}) = BCE ⁡ ( S ⁡ ( 𝐱 ) , M sil ) , \displaystyle=\mathrm{BCE}\!\big(S(\mathbf{x}),\,M_{\text{sil}}\big), (3) S ⁡ ( 𝐱 ) \displaystyle S(\mathbf{x}) = 1 − exp ( − κ ∑ z p z ( 𝐱 ) ) , \displaystyle=1-\exp\!\Big(-\kappa\sum_{z}p_{z}(\mathbf{x})\Big),

[59] p: where BCE \mathrm{BCE} denotes binary cross-entropy, p z ​ ( 𝐱 ) p_{z}(\mathbf{x}) is the decoded voxel occupancy probability at depth z z , and S ⁡ ( 𝐱 ) S(\mathbf{x}) is the rendered 2D silhouette obtained by accumulating occupancy along each camera ray. The target silhouette M sil M_{\text{sil}} is extracted from the edited target view I tgt I^{\text{tgt}} , and κ \kappa controls its sharpness. The guidance term

[60] table: 𝐆 sil ​ ( 𝐱 t ) = − ∇ 𝐱 ℰ sil ​ ( 𝐱 t ) \mathbf{G}_{\text{sil}}(\mathbf{x}_{t})=-\nabla_{\mathbf{x}}\mathcal{E}_{\text{sil}}(\mathbf{x}_{t})

[61] p: encourages the evolving structure to match the target silhouette.

[62] p: Directly applying 𝐆 sil \mathbf{G}_{\text{sil}} may push the edited state off the smooth flow manifold. To counteract this, we introduce a trajectory-consistency correction 𝝃 traj ​ ( 𝐱 t ) \boldsymbol{\xi}_{\text{traj}}(\mathbf{x}_{t}) [ 18 ] , which projects the perturbed latent state back onto the interpolating manifold:

[63] table: 𝝃 traj ​ ( 𝐱 t ) = 𝐱 ^ 0 | t tgt − 𝐱 ^ 0 | t src , \boldsymbol{\xi}_{\text{traj}}(\mathbf{x}_{t})=\widehat{\mathbf{x}}^{\text{tgt}}_{0|t}-\widehat{\mathbf{x}}^{\text{src}}_{0|t},

[64] p: where the clean-state estimates are obtained by back-projecting each trajectory,

[65] table: 𝐱 ^ 0 | t c = 𝐱 t c − t ​ 𝐯 θ ​ ( 𝐱 t c , t ∣ c ) , c ∈ { src , tgt } . \widehat{\mathbf{x}}^{c}_{0|t}=\mathbf{x}^{c}_{t}-t\,\mathbf{v}_{\theta}(\mathbf{x}^{c}_{t},t\mid c),\qquad c\in\{\text{src},\text{tgt}\}.

[66] p: Combining the semantic velocity 𝐯 edit \mathbf{v}_{\text{edit}} with these auxiliary terms yields the controllable flow-regularized update:

[67] table: d ​ 𝐱 t \displaystyle\mathrm{d}\mathbf{x}_{t} = ℳ ℓ ⊙ 𝐯 edit ​ ( 𝐱 t , t ) ​ d ​ t \displaystyle=\mathcal{M}_{\ell}\odot\mathbf{v}_{\text{edit}}(\mathbf{x}_{t},t)\,\mathrm{d}t (4) + ℳ ℓ ⊙ ( Γ 𝝃 traj ( 𝐱 t ) − η 𝐆 sil ( 𝐱 t ) ) d t , \displaystyle+\,\mathcal{M}_{\ell}\odot\Big(\Gamma\,\boldsymbol{\xi}_{\text{traj}}(\mathbf{x}_{t})-\eta\,\mathbf{G}_{\text{sil}}(\mathbf{x}_{t})\Big)\,\mathrm{d}t,

[68] p: where the constants Γ \Gamma and η \eta control the relative strength of the trajectory correction and gradient guidance. The successful edit and stable trajectory achieved by this flow-regularized update are visualized in Fig. 3 (b).

[69] p: To obtain a stable discrete realization, we integrate the above flow in multiple steps from t = 1 t{=}1 to 0 0 . Our final algorithm is summarized in Algorithm 1 .

[70] figure: Algorithm 1 Sparse Voxel FlowEdit Input: source latent 𝐱 0 src \mathbf{x}^{\text{src}}_{0} , { t i } i = 0 T \{t_{i}\}_{i=0}^{T} , ℳ ℓ \mathcal{M}_{\ell} , Γ , η \Gamma,\eta Output: edited latent 𝐱 0 tgt \mathbf{x}^{\text{tgt}}_{0} Init: 𝐱 t T ← 𝐱 0 src \mathbf{x}_{t_{T}}\leftarrow\mathbf{x}^{\text{src}}_{0} for i = T i=T down to 1 1 do Sample ϵ t i ∼ 𝒩 ⁡ ( 𝟎 , 𝐈 ) \boldsymbol{\epsilon}_{t_{i}}\sim\mathcal{N}(\mathbf{0},\mathbf{I}) 𝐱 t i src ← ( 1 − t i ) ​ 𝐱 0 src + t i ​ ϵ t i \mathbf{x}^{\text{src}}_{t_{i}}\leftarrow(1-t_{i})\,\mathbf{x}^{\text{src}}_{0}+t_{i}\,\boldsymbol{\epsilon}_{t_{i}} 𝐱 t i tgt ← 𝐱 t i src + 𝐱 t i − 𝐱 0 src \mathbf{x}^{\text{tgt}}_{t_{i}}\leftarrow\mathbf{x}^{\text{src}}_{t_{i}}+\mathbf{x}_{t_{i}}-\mathbf{x}^{\text{src}}_{0} 𝐱 ~ t i − 1 ← 𝐱 t i + Δ ​ t ​ ℳ ℓ ⊙ 𝐯 edit ​ ( 𝐱 t i , t i ) \tilde{\mathbf{x}}_{t_{i-1}}\leftarrow\mathbf{x}_{t_{i}}+\Delta t\,\mathcal{M}_{\ell}\odot\mathbf{v}_{\text{edit}}(\mathbf{x}_{t_{i}},t_{i}) 𝐱 ^ 0 | t i i ← 𝐱 t i i − t i ​ 𝐯 θ ​ ( 𝐱 t i i , t i ∣ I i ) , i ∈ { src , tgt } \widehat{\mathbf{x}}^{i}_{0|t_{i}}\leftarrow\mathbf{x}^{i}_{t_{i}}-t_{i}\,\mathbf{v}_{\theta}(\mathbf{x}^{i}_{t_{i}},t_{i}\mid I^{i}),\quad i\in\{\text{src},\,\text{tgt}\} 𝝃 traj ​ ( 𝐱 t i ) ← 𝐱 ^ 0 | t i tgt − 𝐱 ^ 0 | t i src \boldsymbol{\xi}_{\text{traj}}(\mathbf{x}_{t_{i}})\leftarrow\widehat{\mathbf{x}}^{\text{tgt}}_{0|t_{i}}-\widehat{\mathbf{x}}^{\text{src}}_{0|t_{i}} 𝐆 t i − 1 sil ← 𝐆 sil ​ ( 𝐱 ~ t i − 1 ) \mathbf{G}^{\text{sil}}_{t_{i-1}}\leftarrow\mathbf{G}_{\text{sil}}(\tilde{\mathbf{x}}_{t_{i-1}}) 𝐱 t i − 1 ← 𝐱 ~ t i − 1 + Δ ​ t ​ ℳ ℓ ⊙ ( Γ ​ 𝝃 traj ​ ( 𝐱 t i ) − η ​ 𝐆 t i − 1 sil ) \mathbf{x}_{t_{i-1}}\leftarrow\tilde{\mathbf{x}}_{t_{i-1}}+\Delta t\,\mathcal{M}_{\ell}\odot\big(\Gamma\,\boldsymbol{\xi}_{\text{traj}}(\mathbf{x}_{t_{i}})-\eta\,\mathbf{G}^{\text{sil}}_{t_{i-1}}\big) end for Return: 𝐱 0 tgt ← 𝐱 t 0 \mathbf{x}^{\text{tgt}}_{0}\leftarrow\mathbf{x}_{t_{0}}

[71] h3: 3.3 SLAT Repainting

[72] p: To further refine local geometry and appearance beyond the sparse structural edits, we introduce a latent-level repainting stage that updates voxel features in the editable region while preserving the source characteristics elsewhere.

[73] p: Building upon the edited sparse voxels 𝒱 tgt \mathcal{V}_{\text{tgt}} obtained from Voxel FlowEdit ( Sec. 3.2 ), we refine local geometry by updating the latent feature vectors { 𝐳 𝐩 } 𝐩 ∈ 𝒱 tgt \{\mathbf{z}_{\mathbf{p}}\}_{\mathbf{p}\in\mathcal{V}_{\text{tgt}}} within the editable region, while anchoring the unedited ones to the source distribution. Let ℳ z \mathcal{M}_{z} denote the per-latent edit mask derived from the mesh-space mask ℳ \mathcal{M} .

[74] p: Note that 𝐯 θ \mathbf{v}_{\theta} here operates on the local latent features 𝐳 \mathbf{z} . At each discrete step k k , the latent update follows a repainting process:

[75] table: 𝐳 k − 1 \displaystyle\mathbf{z}_{k-1} = ℳ z ⊙ [ 𝐳 k + Δ ​ t ​ 𝐯 θ ​ ( 𝐳 k , t k ∣ I tgt ) ] \displaystyle=\mathcal{M}_{z}\odot\Big[\mathbf{z}_{k}+\Delta t\,\mathbf{v}_{\theta}(\mathbf{z}_{k},t_{k}\mid I^{\text{tgt}})\Big] (5) + ( 1 − ℳ z ) ⊙ [ ( 1 − t k ) 𝐳 src + t k ϵ k ] , \displaystyle+(1-\mathcal{M}_{z})\odot\Big[(1-t_{k})\,\mathbf{z}^{\text{src}}+t_{k}\,\boldsymbol{\epsilon}_{k}\Big],

[76] p: where 𝐳 src \mathbf{z}^{\text{src}} is the initial source latent vector at t 0 t_{0} , and ϵ k ∼ 𝒩 ⁡ ( 𝟎 , 𝐈 ) \boldsymbol{\epsilon}_{k}\!\sim\!\mathcal{N}(\mathbf{0},\mathbf{I}) denotes Gaussian noise.

[77] p: The two masked terms jointly ensure local refinement and global preservation: the first term applies target-conditioned velocity for structural refinements in the editable region, whereas the second term replays the forward-diffused source trajectory to maintain global appearance and geometry. In practice, a softly feathered mask ℳ z ~ = blur ⁡ ( ℳ z ; σ b ) \widetilde{\mathcal{M}_{z}}=\operatorname{blur}(\mathcal{M}_{z};\sigma_{b}) is used to prevent seam artifacts.

[78] p: After reaching k = 0 k=0 , the final edited latent field 𝐙 = ( 𝒱 tgt , { 𝐳 𝐩 } 𝐩 ∈ 𝒱 tgt ) \mathbf{Z}=\big(\mathcal{V}_{\text{tgt}},\,\{\mathbf{z}_{\mathbf{p}}\}_{\mathbf{p}\in\mathcal{V}_{\text{tgt}}}\big) is decoded by TRELLIS to produce the refined 3D mesh.

[79] h3: 3.4 Texture Refinement

[80] p: Given the edited 3D mesh decoded from the preceding stages, we optionally apply a texture refinement module to enhance appearance realism. Control Branch. The Control Branch serves to inject precise geometric guidance for the subsequent multi-view synthesis. It is constructed by combining a frozen ControlNet [ 51 ] with a trainable Ctrl-Adapter [ 23 ] . The ControlNet receives per-view normal maps { 𝐍 v } \{\mathbf{N}_{v}\} rendered from the edited geometry and extracts multi-scale spatial features that encode local surface cues. The Ctrl-Adapter then learns to align and inject these control features into the main generative network, effectively acting as a geometry-aware conditioning module. This design enables precise and efficient control over texture synthesis guided strictly by the edited 3D shape. Generation Branch. Conditioned on the geometric guidance extracted by the Control Branch, we adopt the multiview-diffusion architecture from ERA3D [ 20 ] to synthesize multi-view images consistent with the guiding geometry. The generation backbone takes the edited image I tgt I^{\text{tgt}} as primary context, using the control features 𝐂 \mathbf{C} to ensure the output is consistent with the edited geometry. This network synthesizes six geometry-consistent auxiliary views { I v ′ } v = 1 6 \{I^{\prime}_{v}\}_{v=1}^{6} under predefined camera poses. This synthesis process propagates fine appearance details onto the novel viewpoints, providing reliable texture information for the following fusion stage. During training, only the parameters of the Ctrl-Adapter are updated to learn the feature alignment, while the ControlNet and the Era3D backbone remain frozen. Texture Fusion. The final generated appearance is transferred back to the UV space via a robust fusion process. The synthesized views { I v ′ } \{I^{\prime}_{v}\} are projected onto the 3D mesh and fused into the final UV texture 𝐓 \mathbf{T} using a visibility-aware, mask-weighted blending scheme. This process uses the softly feathered edit mask ℳ ~ \widetilde{\mathcal{M}} to prioritize integration in the edited regions, while strictly retaining the original appearance in unedited areas. This efficient transfer yields significantly sharper and more realistic textures for the edited assets.

[81] h2: 4 Experiments

[82] h3: 4.1 Implementation Details

[83] p: For Voxel FlowEdit, we adopt a target-side classifier-free guidance (CFG) scale between 5 and 15, while the source-side CFG is fixed to 5. The latent ODE is discretized by 25 sampling steps, and the edit velocity 𝐯 edit \mathbf{v}_{\text{edit}} is computed by averaging over n avg ∈ { 2 , 4 } n_{\text{avg}}\!\in\{2,4\} to improve stability. For the regularization terms, we normalize the silhouette-guidance gradient so that its ℓ 2 \ell_{2} norm matches that of 𝐯 edit \mathbf{v}_{\text{edit}} , allowing a weighting coefficient of 0.2 for the silhouette term. The trajectory-consistency residual is weighted by 0.1.

[84] p: The normal-guided Ctrl-Adapter is trained on a subset of Objaverse [ 7 ] , where each asset is rendered into six views of size 512 × 512 512{\times}512 with corresponding normal maps. The adapter is trained to synthesize auxiliary views that guide the texture refinement stage.

[85] p: We construct our evaluation set using 100 3D assets collected from Sketchfab Website, the NPHM [ 9 ] dataset for real human heads, the THuman2.1 [ 50 ] dataset for clothed human bodies, and the Objaverse [ 7 ] dataset for objects. These datasets span a wide range of object categories and editing scenarios, allowing us to assess both stylized and photorealistic edits.

[86] h3: 4.2 Comparisons

[87] h4: Baselines.

[88] figure: Figure 4 : Qualitative comparison. Our method achieves clean geometry and consistent appearance across multiple views, faithfully realizing the target edits while preserving unedited regions. Competing methods either retain the original geometry (MVEdit) or exhibit strong structural distortion and inconsistency (Vox-E, Instant3dit).

[89] p: We compare our method against several representative works. (1) TRELLIS [ 45 ] , which serves as our generative backbone. We feed the edited target image I tgt I_{\text{tgt}} directly into its 3D generation pipeline and evaluate its ability to reproduce the edit while preserving consistency with the original 3D model. (2) MVEdit [ 6 ] , a multi-view diffusion framework that uses a training-free 3D adapter to jointly denoise rendered views and output textured meshes. (3) Vox-E [ 38 ] , a voxel-based volumetric editing method that learns a volumetric representation from oriented images and edits existing 3D objects under diffusion priors. (4) Instant3dit [ 1 ] , a recent feed-forward multiview inpainting framework for fast editing of 3D content by generating consistent views and reconstructing the edited result.

[90] p: Since methods ( 2 ) ​ – ​ ( 4 ) (2)–(4) are primarily text-guided frameworks rather than direct image-driven 3D generation, we provide them with a unified text prompt that semantically describes our image-based edit to ensure a fair comparison. Qualitative Comparison. As shown in Fig. 4 , our method produces clean, view-consistent edits that accurately realize the target modifications while preserving the global structure of the source asset. Compared to TRELLIS, which reconstructs directly from the edited view, our framework better maintains identity consistency with the original asset and avoids overfitting to a single observation. Multi-view diffusion models such as MVEdit can generate plausible textures, but in our evaluation they usually introduce negligible geometric change and suffer from view-wise inconsistency. Both Vox-E and Instant3dit fail to maintain structural integrity and multi-view consistency under complex edits. Among them, Vox-E requires significantly longer inference time, while Instant3dit runs faster but still struggles to produce stable, semantically aligned geometric edits.

[91] p: In contrast, our approach achieves geometrically stable and visually realistic results within a feed-forward pass. Notably, the mask-aware latent editing preserves unedited regions, while the additional refinement stage enhances local detail and lighting continuity. These results demonstrate that our framework provides a favorable balance among edit controllability, identity preservation, and visual fidelity.

[92] p: Quantitative Comparison. We evaluate performance using four widely adopted quantitative metrics: CLIP-T (text–image alignment) [ 35 ] , DINO-I (perceptual quality) [ 5 ] , LPIPS (perceptual similarity) [ 52 ] , and FID (distributional realism) [ 13 ] . As shown in Tab. 1 , our method consistently achieves the best performance across all four metrics. These results confirm that our framework produces higher overall 3D quality and text alignment than representative baselines, yielding more coherent, high-fidelity 3D assets.

[93] figure: Table 1 : Quantitative comparison on the 3D editing benchmark. Higher is better for CLIP-T, and DINO-I; lower is better for LPIPS and FID. Our method consistently achieves the best performance across all metrics. Method CLIP-T ↑ \uparrow DINO-I ↑ \uparrow LPIPS ↓ \downarrow FID ↓ \downarrow TRELLIS [ 45 ] 0.323 0.895 0.243 45.8 MVEdit [ 6 ] 0.267 0.851 0.282 67.6 Vox-E [ 38 ] 0.266 0.734 0.673 90.3 Instant3DiT [ 1 ] 0.285 0.874 0.286 49.7 Ours 0.326 0.952 0.138 25.8

[94] p: User Study. We also conduct a user study to further quantitatively validate our method. Participants were asked to view the editing prompt, alongside videos rendered from both the source 3D assets and the 3D assets edited by our method and four competing methods, and then respond to a series of questions:

[95] figure: Table 2 : User study results. Percentage of times each question is rated best (higher is better). Question Q1 ↑ \uparrow Q2 ↑ \uparrow Q3 ↑ \uparrow Q4 ↑ \uparrow Q5 ↑ \uparrow Ours 88.98 94.63 94.92 97.51 97.00

[96] p: Q1: Which method best follows the given input prompt? ( Prompt Preservation )

[97] p: Q2: Which method best retains the geometry and texture of the unedited regions? ( Identity Preservation )

[98] p: Q3: Which method best produces edited geometry and texture? ( 3D Editing Quality )

[99] p: Q4: Which method best maintains 3D consistency? ( 3D Consistency )

[100] p: Q5: Which method is best overall considering the above four aspects? ( Overall )

[101] p: We collected statistics from 46 participants across 10 groups of editing results. For a fair comparison, the video results for each case were randomly shuffled. As shown in Tab. 2 , our method remarkably outperforms other methods in prompt preservation, identity preservation, 3D editing quality, and 3D consistency, and is rated as the best in overall quality. These results demonstrate that our method is highly favored by users, highlighting its effectiveness across various editing dimensions.

[102] h3: 4.3 Ablation Studies

[103] p: Guided Flow Regularization. We ablate the auxiliary guidance terms in Eq. 4 to assess their impact on structural stability. Specifically, we compare the base ODE update without auxiliary guidance against the full guided formulation with both the silhouette gradient and the trajectory correction enabled. We toggle these two terms jointly, since 𝐆 sil \mathbf{G}_{\text{sil}} aligns the evolving structure with the target silhouette, while 𝝃 traj \boldsymbol{\xi}_{\text{traj}} regularizes the dynamics by projecting 𝐱 t \mathbf{x}_{t} back onto the flow manifold. Using only one of them leads to unbalanced updates and unstable geometry. As shown in Fig. 5 , removing both terms results in a combination of over-preservation and structural drift, whereas enabling both yields coherent and well-aligned deformations.

[104] figure: Figure 5 : Comparison between without and with Flow Guidance. Disabling 𝐆 sil \mathbf{G}_{\text{sil}} and 𝝃 traj \boldsymbol{\xi}_{\text{traj}} jointly leads to structural collapse and view-inconsistent deformation, whereas enabling both yields stable and silhouette-aligned geometry.

[105] p: Texture Refinement. We further investigate the effect of the normal-guided appearance refinement module. This component restores high-frequency texture details and harmonizes lighting across views via normal-conditioned feature modulation. Without Texture Refinement, the edited regions become noticeably blurrier and exhibit color bias, as illustrated in Fig. 6 .

[106] figure: Figure 6 : Comparison between without and with Texture Refinement. The refinement stage significantly enhances surface detail and view-consistent appearance.

[107] h2: 5 Conclusion

[108] p: We have presented a unified feed-forward framework for 3D asset editing that integrates geometric transformation, latent-space refinement, and texture enhancement within a single generative pipeline. Our method builds upon the 3D-native TRELLIS representation, enabling coherent large-scale deformation and fine-grained texture editing directly from a single-view input. By combining Voxel FlowEdit, SLAT repainting, and normal-guided texture refinement, the proposed system effectively bridges 2D editing flexibility with 3D consistency and realism. Comprehensive experiments demonstrate that our approach achieves stable geometry, faithful texture preservation, and visually consistent results across diverse assets, offering a practical paradigm for efficient and controllable 3D editing.

[109] p: Limitations. While our framework delivers robust and realistic edits, its performance remains bounded by the generative capacity of TRELLIS, particularly under extreme geometric modifications. Moreover, the normal-guided refinement currently operates on relatively low-resolution synthesized views, which would limit the recovery of very fine textures. We believe these limitations can be mitigated in future work through higher-resolution generation and stronger geometric priors.

[110] h2: References

[111] p: Supplementary Material

[112] h2: Appendix A Editing Efficiency

[113] figure: Table 3 : Runtime comparison with different methods. Method Runtime Vox-E [ 38 ] 37 min MVEdit [ 6 ] 212 s Instant3dit [ 1 ] 25 s Ours 75 s

[114] p: We compare the efficiency of our approach with three baselines: Instant3dit, MVEdit, and Vox-E, as shown in Tab. 3 . Instant3dit is the fastest (25 seconds) due to its highly streamlined pipeline, but this compactness often limits its ability to handle complex disentanglement, resulting in lower fidelity. In contrast, MVEdit incurs a significantly higher computational cost of 212 seconds, as it relies on heavy iterative multi-view diffusion refinement. Vox-E is even more time-consuming, requiring full 3D optimization of the voxel grid, which takes approximately 37 minutes per edit. Our method operates in a sweet spot with a total runtime of 75 seconds. Adopting an efficient feed-forward design similar to Instant3dit, our approach eliminates the need for time-consuming per-scene optimization. However, unlike the unified pipeline of Instant3dit, we utilize a structured workflow decomposed into geometry editing (30 seconds), texture refinement (30 seconds), and back-projection (15 seconds). This 75 seconds duration allows us to achieve substantially better consistency and detail than Instant3dit, while remaining orders of magnitude faster than the optimization-heavy baselines.

[115] h2: Appendix B Effectiveness of Texture Refinement

[116] p: Fig. 7 presents the qualitative results obtained from our normal-guided Multi-view Diffusion Module. Conditioned on multi-view normal maps rendered from the input mesh and a single reference image, the module synthesizes a coherent sequence of multi-view images. As shown in the visualization, the generated images exhibit high-fidelity textures with intricate details. More importantly, benefiting from the structural guidance of surface normals, the results demonstrate rigorous cross-view consistency, where the object identity and geometric features remain stable across varying camera poses. This ensures that the subsequent texture back-projection step produces a seamless 3D model without alignment artifacts.

[117] figure: Figure 7 : Visualizations of the normal-guided multi-view diffusion module. Taking rendered normal maps and a reference image as input, the module generates multi-view images that are both texture-rich and geometrically consistent, serving as robust priors for 3D texture recovery.

[118] h2: Appendix C More Results

[119] p: We present six supplementary examples in Fig. 8 to further validate the robustness of our approach. (a)-(c) demonstrate our capabilities on non-realistic objects; observe that the edited regions undergo significant geometric deformation, while the geometry of the unedited regions is strictly preserved. (d) illustrates the effectiveness of our method in scene-level editing. (e)-(f) showcase results on human subjects, where the clothing is successfully modified with high visual quality while maintaining the texture fidelity of the unedited body parts.

[120] figure: Figure 8 : More visualization results.

[121] h2: Instructions for reporting errors

[122] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[123] p: Tip: You can select the relevant text first, to include it in your report.

[124] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[125] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
