# 19048 exact-v1 necessary primary cache

Source: https://arxiv.org/html/2601.19048v1
Original web line labels preserved; sorted and deduplicated within this paper, not contiguous full text.

L0: ##### Report GitHub Issue
L1: 
L2: [Button: ×]
L3: 
L4: Title: [Input: Enter title]
L5: 
L6: Content selection saved. Describe the issue below:
L7: 
L8: Description:
L9: 
L10: [Button: Submit without GitHub] [Button: Submit in GitHub]
L11: 
L12: cite0†Back to arXiv L13: 
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract. L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Work L18:     1. cite8†2.1 Unbounded 3D Scene Generation L19:     2. cite9†2.2 Training-Free Scene Generation L20:     3. cite10†2.3 LLM Aided Scene Generation L21:   4. cite11†3 Preliminary L22:     1. cite12†3.1 NuiScene L23:       1. cite13†3.1.1 Chunk VAE L24:       2. cite14†3.1.2 Quad Chunk Diffusion L25:   5. cite15†4 Method L26:     1. cite16†4.1 Data Generation L27:       1. cite17†4.1.1 Bootstrapping Initial 3D Scenes L28:       2. cite18†4.1.2 NuiScene Training L29:       3. cite19†4.1.3 Scene Synthesis Across Scales and Layout L30:     2. cite20†4.2 Sketch to World Model L31:       1. cite21†4.2.1 Model Architecture L32:       2. cite22†4.2.2 Size Prediction L33:   6. cite23†5 Experiment L34:     1. cite24†5.1 Dataset L35:     2. cite25†5.2 Evaluation Metrics L36:       1. cite26†5.2.1 NuiScene L37:       2. cite27†5.2.2 NuiWorld L38:     3. cite28†5.3 Ablation L39:       1. cite29†5.3.1 NuiScene VecSet Compression Rate L40:       2. cite30†5.3.2 Sketch to World Model Width L41:     4. cite31†5.4 Full Set Training L42:       1. cite32†5.4.1 Trellis 2 Comparison L43:     5. cite33†5.5 Generalization to Unseen Sketch L44:   7. cite34†6 Limitation L45:   8. cite35†7 Conclusion L46:   9. cite36†References L47:   10. cite37†A Dataset L48:     1. cite38†A.0.1 Prompting Strategy L49:     2. cite39†A.0.2 Colored Point Cloud Sampling L50:   11. cite40†B Model Hyperparameters L51:     1. cite41†B.1 NuiScene L52:       1. cite42†B.1.1 VAE L53:       2. cite43†B.1.2 Quad Chunk Diffusion L54:     2. cite44†B.2 Sketch to World Model L55: cite45†License: CC BY 4.0†info.arxiv.org L56: 
L57: arXiv:2601.19048v1 [cs.CV] 27 Jan 2026
L58: # NuiWorld: Exploring a Scalable Framework for End-to-End Controllable World Generation
L59: 
L60: Conference: ; ;
L61: 
L62: Han-Hung Lee Affiliation: Simon Fraser University, Canada email: hla300@sfu.ca , Cheng-Yu Yang Affiliation: National Yang Ming Chiao Tung University, Taiwan email: cyyang@nycu.edu.tw , Yu-Lun Liu Affiliation: National Yang Ming Chiao Tung University, Taiwan email: yulunliu@cs.nycu.edu.tw and Angel X. Chang Affiliation: Simon Fraser University, CIFAR AI Chair, Amii, Canada email: angelx@sfu.ca
L63: 
L64: © none
L65: cite46†Image: Refer to caption Figure 1. NuiWorld proposes a data pipeline for constructing open-domain, variable-sized scenes with pseudo sketch pairs to train controllable world generation models. Furthermore, our representation scales with scene size while maintaining fidelity across scenes of varying sizes.
L66: ###### Abstract.
L67: World generation is a fundamental capability for applications like video games, simulation, and robotics. However, existing approaches face three main obstacles: controllability, scalability, and efficiency. End-to-end scene generation models have been limited by data scarcity. While object-centric generation approaches rely on fixed resolution representations, degrading fidelity for larger scenes. Training-free approaches, while flexible, are often slow and computationally expensive at inference time.
L68: We present NuiWorld, a framework that attempts to address these challenges. To overcome data scarcity, we propose a generative bootstrapping strategy that starts from a few input images. Leveraging recent 3D reconstruction and expandable scene generation techniques, we synthesize scenes of varying sizes and layouts, producing enough data to train an end-to-end model.
L69: Furthermore, our framework enables controllability through pseudo sketch labels, and demonstrates a degree of generalization to previously unseen sketches. Our approach represents scenes as a collection of variable scene chunks, which are compressed into a flattened vector-set representation. This significantly reduces the token length for large scenes, enabling consistent geometric fidelity across scenes sizes while improving training and inference efficiency.
L70: ## 1. Introduction
L71: The ability to generate virtual worlds at a click of a button has wide-ranging applications. For artists, it could enable rapid visualization of environments for concept design. In robotics, generating diverse environments for training can improve generalization. Similar benefits can extend to VR, film and other industries. As a result, fast and open-domain world generation is increasingly important, and we believe will be best achieved through end-to-end models.
L72: In this paper, we define world generation as the ability to produce large-scale, open-domain scenes. We argue that addressing the two core challenges of scalability and data scarcity is essential to achieving this and enabling world generation for broader applicability.
L73: cite47†Image: Refer to caption Figure 2. Object generators like Trellis 2 do not adapt to scene scale or aspect ratio, causing such scenes to be represented with less voxels and degraded fidelity while our method scales with scene sizes and maintains fidelity.
L74: With the rise of LLMs and agent-based systems used to tackle tasks with limited training data, these models have also been explored for large-scale scene generation. Several works (cite48†Wang et al., 2025a ; cite49†Lu et al., 2025 ; cite50†Huang et al., 2025 ; cite51†Wang et al., 2025b ) employ LLMs to aid the scene generation process. However, this reliance introduces additional latency time and potential costs.
L75: Additionally, it remains unclear whether LLMs can reliably perform spatial reasoning for scene layout generation or generalize to open-domain scene layouts. Our approach instead focuses on synthesizing a sufficiently large training dataset of scenes for world generation as seen in cite52†Figure 3 . We propose a generative bootstrapping pipeline that begins with a small set of scenario images produced using text-to-image models.
L76: These images are reconstructed into 3D scenes with Trellis 2 (cite53†Xiang et al., 2025a ), which are used to train NuiScene (cite54†Lee et al., 2025 ) to generate varying scene layouts and scales. These scenes are converted into pseudo sketches and used to train a controllable world generation model. This approach eliminates the need for agents or complex inference pipelines, and allows for the generation of new scenarios using a few input images.
L77: Recent 3D object generation methods achieve impressive high quality results by utilizing the sparse voxel representation (cite55†Xiang et al., 2025b ; cite56†Wu et al., 2025 ; cite57†He et al., 2025 ; cite58†Li et al., 2025b ; cite59†Lai et al., 2025a ; cite53†Xiang et al., 2025a ). However, these methods are constrained by the overall voxel grid resolution. In large scenes, the geometry becomes increasingly blurry and loses fine details due to the upper bound on the total number of voxels.
L78: Which is further exacerbated by uniformly distributed voxel grids, which allocate the same spatial resolution to empty and occupied regions alike limiting their use to large-scale scene generation as seen in cite60†Figure 2 . In contrast, we represent the scene as a variable-length sequence of scene chunks.
L79: Each scene chunk is encoded as a flattened vector set (cite61†Zhang et al., 2023 ), as illustrated in cite62†Figure 1 , resulting in a compact token sequence whose length corresponds to the number of scene chunks. Importantly, this flattened representation shifts part of the computation from the token length, which has quadratic memory growth, to the model width, which scales linearly.
L80: Because all the vector sets have a homogeneous size, they can be directly reshaped into token channels, enabling efficient scaling across scenes of different sizes while maintaining consistent fidelity.
L81: To circumvent the resolution limit of object generators, another line of work (cite63†Engstler et al., 2025 ; cite64†Zheng et al., 2025b ; cite65†Chen et al., 2025a ; cite66†Yoon et al., 2025 ) decomposes large scenes into chunks and leverages Trellis (cite55†Xiang et al., 2025b ) to generate each chunk in a training-free manner. These approaches require multiple runs of Trellis sequentially or in parallel, leading to slow inference speeds and/or heavy memory usage.
L82: Moreover, some methods (cite63†Engstler et al., 2025 ) rely on additional resource-intensive modules, further increasing computational overhead. By comparison, our method is trained end-to-end and diffuses the entire scene at once during inference. This results in a significantly simpler inference pipeline and more efficient use of computational resources.
L83: To summarize, our contributions are as follows: Generative Boostrapping Strategy. Our data generation pipeline combines a 3D reconstruction model with an expandable scene generation model, enabling the creation of scenes with various sizes and layouts from only a few input images of the target scenario. Paired with pseudo-sketches of these scenes, this pipeline supports end-to-end training of a controllable world model alleviating data scarcity. Scalable Scene Representation.
L84: We represent scenes as a variable-length sequence of scene chunk tokens, where each chunk is encoded as a flattened vector set. This yields a compact and efficient representation that scales with scene size while preserving consistent geometric fidelity. Efficient End-to-End System. Our model is trained end-to-end to generate complete scenes at once, eliminating the need for complex training-free pipelines or agent-based systems that may incur additional computational overhead.
L85: cite67†Image: Refer to caption Figure 3. Our framework begins with generative bootstrapping, shown on the left. Using Nano Banana to generate images and Trellis 2 to reconstruct 3D scenes. NuiScene is then trained on these scenes to produce new scenes with varying size and layouts. Finally, using these scenes and their pseudo sketches we train our variable-length sketch-to-world model on the right.
L86: ## 2. Related Work
L87: ### 2.1. Unbounded 3D Scene Generation
L88: We review methods that perform expandable generation of arbitrarily large 3D scenes directly in the 3D domain. PDD (cite68†Liu et al., 2024 ) uses a multi-scale pyramid diffusion framework to generate urban scenes. While several works (cite69†Lee et al., 2024 ; cite70†Wu et al., 2024 ; cite71†Meng et al., 2025 ) follow the latent diffusion paradigm, learning to generate chunks through diffusion in the latent space.
L89: Expandable generation is enabled with RePaint (cite72†Lugmayr et al., 2022 ) by conditioning on overlapping regions, requiring additional diffusion steps. SemCity (cite69†Lee et al., 2024 ) and BlockFusion (cite70†Wu et al., 2024 ) use triplane representations for urban and indoor scenes, respectively, while LT3SD (cite71†Meng et al., 2025 ) uses hierarchical feature grids for modeling finer indoor details.
L90: NuiScene (cite54†Lee et al., 2025 ) introduces a vector set representation for outdoor scenes and an explicit outpainting model for fast generation. WorldGrow (cite73†Li et al., 2025a ) fine-tunes Trellis (cite55†Xiang et al., 2025b ) for 3D block inpainting, enabling block-by-block synthesis of scenes. The autoregressive nature of these methods causes inference time to scale with scene size.
L91: As shown in cite74†Table 4 , NuiScene incurs higher runtime than models like ours that diffuses entire scenes at the same time.
L92: ### 2.2. Training-Free Scene Generation
L93: Several recent works leverage Trellis (cite55†Xiang et al., 2025b ) to enable training-free, chunk-based generation, circumventing the resolution limits of object-centric generators. SynCity (cite63†Engstler et al., 2025 ) uses FLUX (cite75†Labs, 2024 ) to generate smaller image tiles sequentially and Trellis to lift them into 3D.
L94: 3DTown (cite64†Zheng et al., 2025b ) derives a point cloud from a reference image of the scene, and conditions Trellis on cropped images with corresponding cropped point clouds to generate local regions. TrellisWorld (cite65†Chen et al., 2025a ) and Extend3D (cite66†Yoon et al., 2025 ) introduces denoising schemes to enable parallel chunk generation for scenes. The primary limitation of these methods is their resource consumption, which is fundamentally bounded by the cost of running Trellis (cite74†Table 4 ).
L95: Sequential chunk generation leads to inference time that scales linearly with scene size, whereas parallel generation comes at the expense of increasing memory usage. Our model is trained to generate whole scenes natively with latents that naturally scale with scene size (cite76†Figure 8 ).
L96: ### 2.3. LLM Aided Scene Generation
L97: Recent works (cite49†Lu et al., 2025 ; cite51†Wang et al., 2025b ; cite50†Huang et al., 2025 ) leverage LLMs to assist city generation. Yo’City (cite49†Lu et al., 2025 ) relies on LLMs for generating fine-grained text prompts for scene grids to drive image and subsequent 3D generation. RaiseCity (cite51†Wang et al., 2025b ) derives buildings from street-view images via segmentation and used as inputs to image generation tools for completion before 3D generation and scene placement.
L98: MajutsuCity (cite50†Huang et al., 2025 ) learns to generate semantic layout and height maps from LLM enriched user input. Buildings are extruded with height maps, and used to condition image generation tools for image to 3D conversion and scene assembly. Across all methods, agents are further employed to iteratively evaluate and regenerate images of city regions or buildings before 3D generation. The inclusion of agent heavy pipelines can introduce longer generation times and API costs during inference.
L99: Additionally, these works mainly focus on cityscapes, it is unknown whether they can generalize to more open-domain scenarios. WorldGen (cite48†Wang et al., 2025a ) relies on LLMs to produce initial procedural generation parameters from text input. The procedurally generated blockout is used as a condition for image generation. Followed by scene reconstruction, decomposition, and enhancement.
L100: Our sketch-to-world model operates end-to-end without LLMs and enables open-domain generation through our generative bootstrapping process.
L101: ## 3. Preliminary
L102: ### 3.1. NuiScene
L103: 
L104: In NuiScene (cite54†Lee et al., 2025 ), the model is trained on $K$ scenes $\{\mathbf{S}_{i}\}_{i=1}^{K}$ processed from Objaverse (cite77†Deitke et al., 2023 ). Each scene is represented as $\mathbf{S}_{i}=(\mathbf{O}_{i},\mathbf{P}_{i})$, where $\mathbf{O}_{i}$ denotes an occupancy grid with dimensions $X_{i}\times Y_{i}\times Z_{i}$, and $\mathbf{P}_{i}\in\mathbb{R}^{N_{pc}\times 3}$ is a point cloud with $N_{pc}$ points sampled from the marching cubes surface of $\mathbf{O}_{i}$.
L105: Each scene is partitioned along the $x$ and $z$ axes into smaller chunks of fixed size $s\times Y_{i}\times s$, where $s<\min_{i}X_{i}$ and $s<\min_{i}Z_{i}$. We denote the chunk at location (u, v) as $\mathbf{S}_{i}^{(u,v)}=(\mathbf{O}_{i}^{(u,v)},\mathbf{P}_{i}^{(u,v)})$, where $\mathbf{O}_{i}^{(u,v)}$ is the cropped occupancy and $\mathbf{P}_{i}^{(u,v)}\in\mathbb{R}^{N_{pc}^{(u,v)}\times 3}$ is the corresponding point cloud from its surface.
L106: The model consists of a chunk VAE that encodes $\mathbf{P}_{i}^{(u,v)}$ into a vector set, and a diffusion model that learns over a local $2\times 2$ grid of adjacent chunks.
L107: #### 3.1.1. Chunk VAE
L108: cite54†Lee et al. (2025) follows 3DShape2VecSet (cite61†Zhang et al., 2023 ) by employing a cross-attention (CA) layer to encode a scene chunk point cloud $\mathbf{P}_{i}^{(u,v)}$ into a vector set $\mathbf{z}\in\mathbb{R}^{V\times c}$, where $V$ is the number of vectors and $c$ is the channel size. The decoder then applies a stack of self-attention (SA) layers to get an output feature $\mathbf{f}_{out}\in\mathbb{R}^{F\times h}$.
L109: To increase the number of tokens, a fully connected (FC) layer may be added within the decoder paired with a pixel shuffle (cite78†Shi et al., 2016 )-like up-sampling operation, producing $F$ tokens. Here $h$ denotes the model’s hidden dimension. Finally, coordinates are sampled within each chunk’s occupancy grid $\mathbf{O}_{i}^{(u,v)}$ and queried through an additional CA layer, followed by an FC layer, to produce occupancy logits.
L110: These predictions are supervised with the corresponding ground truth occupancy values $\mathbf{O}_{i}^{(u,v)}$.
L111: #### 3.1.2. Quad Chunk Diffusion
L112: The quad chunk diffusion model is trained to capture local $2\times 2$ context windows of adjacent chunk latents, specifically $\mathbf{z}_{i}^{(u,v)}$, $\mathbf{z}_{i}^{(u,v+s)}$, $\mathbf{z}_{i}^{(u+s,v)}$, and $\mathbf{z}_{i}^{(u+s,v+s)}$. Training is performed using DDPM (cite79†Ho et al., 2020 ) with four different masking and conditioning configurations over this context window, enabling raster-scan order generation during inference for scenes of varying sizes and layouts.
L113: Please see the original paper for further details.
L114: ## 4. Method
L115: 
L116: In this section, we describe the NuiWorld framework. We begin by introducing our data generation pipeline in cite16†Section 4.1 . Obtaining initial 3D scenes to bootstrap the process (cite17†Section 4.1.1 ) to train NuiScene (cite18†Section 4.1.2 ) and constructing a dataset of various scene sizes and layouts (cite19†Section 4.1.3 ). Using this synthesized data, we then train our sketch-to-world model, as detailed in cite20†Section 4.2 .
L117: 
L118: ### 4.1. Data Generation
L119: #### 4.1.1. Bootstrapping Initial 3D Scenes
L120: We begin by bootstrapping our pipeline with image generation for a target scenario (e.g. medieval, desert, cyberpunk) using Nano Banana from Gemini 3 (cite80†Comanici et al., 2025 ; cite81†Google, 2025a ; cite82†Google, 2025b ). Specifically, we prompt the model to generate images of isometric scene chunks, as illustrated in cite52†Figure 3 , with varying element compositions for each image. We then employ Trellis 2 (cite53†Xiang et al., 2025a ) to reconstruct colored meshes from the generated images.
L121: We observe that images containing excessively large scenes lead to degraded geometry detail, therefore we restrict the amount of elements in the scene prompts. Finally, following NuiScene (cite54†Lee et al., 2025 ) we unify scene scales and ground thickness, converting the reconstructed scenes into point cloud and occupancy grids.
L122: This yields a bootstrapped dataset of $M$ scenes, $\mathbf{S}^{boot}=\{\mathbf{S}_{i}^{boot}\}_{i=1}^{M}$, $\mathbf{S}_{i}^{boot}=(\mathbf{O}^{boot}_{i},\mathbf{P}^{boot}_{i})$ which is used to train NuiScene. Note that prompt tuning with Gemini and scene preprocessing are time-consuming, and thus used only for bootstrapping. Please see the supplementary for additional visualizations.
L123: #### 4.1.2. NuiScene Training
L124: We follow the NuiScene training procedure using the bootstrapped scenes $\mathbf{S}^{boot}$. One key modification is that we retain the color information produced by Trellis 2, storing it in the point clouds $\mathbf{P}^{boot}_{i}\in\mathbb{R}^{N_{pc}\times 6}$ which contains both the 3D coordinates and RGB values. During the training of the Chunk VAE we add an additional color prediction head implemented via CA and FC layers similar to the occupancy head.
L125: Color query coordinates and ground-truth color supervision are sampled from the corresponding chunk $\mathbf{P}^{boot}_{i,(u,v)}$, with RGB values supervised by an $\ell_{2}$ loss. During inference, we extract the mesh using marching cubes, sample points on the surface to query color predictions, and assign each mesh vertex the color of its nearest predicted point.
L126: Finally, we also replace DDPM (cite79†Ho et al., 2020 ) with rectified flow (cite83†Lipman et al., 2022 ) for training the quad chunk diffusion model.
L127: #### 4.1.3. Scene Synthesis Across Scales and Layout
L128: Next we sample a dataset of $Q$ scenes $\mathbf{S}^{Nui}=\{\mathbf{S}^{Nui}_{i}\}_{i=1}^{Q}$ using the trained NuiScene model. For each scene, we first sample a target area $A\in[A_{min},A_{max}]$ using log-uniform distribution. With probability $p_{square}=0.3$, we generate a square scene. Otherwise, we sample an aspect ratio $r\in[1.0,3.0]$ from a log-uniform distribution to determine the scene dimensions $(R_{i},C_{i})$ accordingly, enforcing $C_{i}\geq R_{i}\geq 15$.
L129: Here $R_{i}$ denotes the number of scene chunk rows, and $C_{i}$ corresponds to the number of chunks per row. We then render the extracted scene mesh from a fixed viewpoint at a resolution of $512\times 512$ ensuring that scenes are elongated along the horizontal axis of the image, producing a colored and colorless rendering. Each rendering is converted using two methods: canny edge (cite84†Canny, 2009 ) and cite85†Chan et al. (2022) . This results in 4 sketches per scene.
L130: Each resulting scene consists of a 2D grid of vector sets and pseudo sketches denoted as $\mathbf{S}^{Nui}_{i}=(\mathcal{V}_{i},\{\mathcal{I}^{(j)}_{i}\}_{j=1}^{4})$, where $\mathcal{V}_{i},\in\mathbb{R}^{R_{i}\times C_{i}\times V\times c}$ and $\mathcal{I}^{(j)}_{i}\in\mathbb{R}^{512\times 512\times 1}$.
L131: ### 4.2. Sketch to World Model
L132: #### 4.2.1. Model Architecture
L133: Our model aims to generate scenes $\mathcal{V}$ with variable token length $R\times C$ and a channel size of $V\times c$, conditioned on a pseudo sketch input. Here, we drop the subscript $i$ for simplicity and consider a single training sample. During training we randomly sample a sketch $\mathcal{I}$ from $\{\mathcal{I}^{(j)}\}_{j=1}^{4}$.
L134: Note that we do not choose to concatenate vector sets into the token length like in AutoPartGen (cite86†Chen et al., 2025b ), this is to avoid quadratic growth which would increase compute by $V^{2}$.
L135: Our transformer model $\textbf{w}_{\phi}$ consists of $L$ blocks each containing a self-attention, cross-attention and feed forward network as illustrated in cite52†Figure 3 . The sketch conditioning is incorporated through each cross-attention layer. Specifically the sketch $\mathcal{I}$ is encoded using a frozen DINOv2 encoder (cite87†Oquab et al., 2023 ) to obtain the token embeddings $\mathbf{z}_{sk}\in\mathbb{R}^{1374\times 1024}$ and fed to cross-attention layers.
L136: We train our model using rectified flow (cite83†Lipman et al., 2022 ). During training we sample a timestep $t\in[0,1]$ and Gaussian noise $\bm{\epsilon}\sim\mathcal{N}(0,\mathbf{I})$, and construct noisy latents as $\mathcal{V}_{t}=(1-t)\mathcal{V}_{0}+t\epsilon$, where $\mathcal{V}=\mathcal{V}_{0}$ denotes the ground-truth scene latent.
L137: Before feeding into the model, the noisy latents $\mathcal{V}_{t}$ are also added with positional embeddings and size embeddings. Each token is assigned a 2D spatial coordinate $(row,col)$, where $row\in[0,R)$ and $col\in[0,C)$ determined by the token’s location in the scene, which are encoded with sinusoidal functions. In addition, a size embedding derived from $R\times C$ and also computed with sinusoidal encoding are shared across all tokens in the scene.
L138: Both embeddings are added to $\mathcal{V}_{t}$ as input to the transformer.
L139: The model $\mathbf{w}_{\phi}$ is trained with the objective:
L140: 
L141: (1)  |  | $$\mathbb{E}_{\mathcal{V},z_{sk},\bm{\epsilon}\sim\mathcal{N}(0,\mathbf{I}),t}\left[\|\mathbf{w}_{\phi}(\mathcal{V}_{t},z_{sk},t)-(\epsilon-\mathcal{V}_{0})\|^{2}_{2}\right]$$  |
L142: 
L143: To enable classifier-free guidance during inference, the sketch conditioning $z_{sk}$ is randomly dropped with $0.2$ probability during training. The timestep $t$ is incorporated into the network via modulation, following Trellis (cite55†Xiang et al., 2025b ).
L144: #### 4.2.2. Size Prediction
L145: During inference, the scene dimensions $R$ and $C$ may not be available for a given input sketch. To address this, we learn an additional size prediction network conditioned on the input sketch. The network takes as input the CLS embedding $z_{cls}\in\mathbb{R}^{1024}$, extracted from DINOv2 given the sketch image $\mathcal{I}$, and predicts the scene dimensions $(\hat{R},\hat{C})$. We supervise training with the ground truth layout $(R,C)$.
L146: As shown cite52†Figure 3 , the predicted layout $(\hat{R},\hat{C})$ can be used to initialize the number of noisy tokens for scene generation during inference. We note that the size prediction is optional and can also be specified by the user.
L147: ## 5. Experiment
L148: 
L149: For all experiments, we train a separate model for each scenario. This is mainly due to resource constraints and enables faster development. Training models on different scenarios independently allows us to iterate more quickly and avoid long training times.
L150: ### 5.1. Dataset
L151: 
L152: We construct datasets for three scenarios: medieval, desert, and cyberpunk. Each dataset is bootstrapped using images generated by Nano Banana and reconstructed with Trellis 2, producing $M=16,12$, and $12$ initial bootstrapping scenes for each scenario, respectively. Please see the supplementary for more details. Using the boostrapped scenes, we train NuiScene with a chunk size of $s=60$.
L153: For overfitting experiments, we generate $Q=720$ scenes using NuiScene for the medieval scenario, with scene area $A$ sampled from the range $[225,625]$. For full set training, we generate $Q=8000$ scenes per scenario, with scene areas sampled from $[225,1024]$. The datasets are split into $7200$ scene sketch pairs for training and $800$ scenes for validation. Each scene is generated with random seeds using NuiScene.
L154: For the overfitting experiments, metrics are calculated on the train set directly; for the full set experiments, metrics are calculated on the validation split. For even larger scenes, we fine-tune full set models on $1800$ additional scenes sampled from areas $[1024,1600]$ and refer to these models as XL models in experiments.
L155: ### 5.2. Evaluation Metrics
L156: #### 5.2.1. NuiScene
L157: We largely follow NuiScene’s evaluation protocol. For the VAE, we report Chamfer Distance (CD), F-Score, and IoU. Following NuiScene, we sample 50k points per scene chunk and use a distance threshold of the voxel length ($2/60$) when computing CD and F-Score. For IoU, we similarly sample 10k points uniformly from occupied and unoccupied regions, along with 10k point sampled near the surface. In addition, we add a root mean squared error (RMSE) metric to evaluate the color prediction.
L158: Specifically, we sample 10k colored points from the surface of the scene chunk for this evaluation. Finally, for the diffusion model, we evaluate using the Fréchet PointNet++ (cite88†Qi et al., 2017 ) Distance (FPD) and Kernel PointNet++ Distance (KPD). For these metrics, $2048$ points are sampled per quad chunk. For all metrics, we use 10k quad chunks for evaluation. Please see cite54†Lee et al. (2025) for more details.
L159: #### 5.2.2. NuiWorld
L160: 
L161: For NuiWorld, we evaluate sketch to world adherence and overall quality using the RMSE between predicted scene embeddings and ground truth embeddings $\mathcal{V}$ generated by NuiScene during the data generation process. Similarly, CD is calculated between the decoded mesh and the corresponding ground truth meshes from NuiScene. Unless otherwise specified, we use the ground truth scene dimension layout $(R,C)$ during inference.
L162: ### 5.3. Ablation
L163: 
L164: We find it important to compress the vector set dimensions as much as possible to enable better sketch-to-world performance. Accordingly, we ablate vector set compression ratio and the sketch-to-world model width, analyzing their impact on overfitting.
L165: #### 5.3.1. NuiScene VecSet Compression Rate
L166: 
L167: We experiment with two different compression ratios, resulting in vector set sizes of $(V,c)=(16,64)$ and $(8,64)$. For the $(8,64)$ configuration, we add a vector set upsampling layer, following cite54†Lee et al. (2025) , to upsample the number of tokens to $512$ for the last 6 self-attention layers of the VAE decoder. This helps to compensate for the $2\times$ reduction in the number of vectors. More details are described in the supplementary.
L168: We report quantitative evaluations for the VAE and quad chunk diffusion models in cite89†Table 1 . All metrics are computed using models trained on the medieval scenario. For the VAE, we additionally evaluate reconstruction on the scene chunks from the desert scenario as the validation set, which is unseen during training.
L181: The effect is particularly pronounced for the $(8,64)$ configuration, where the gap between the model width and the flattened vector dimension is larger. This observation is in line with the recent work RAE (cite91†Zheng et al., 2025a ). Note that due to resource constraints we reduce the model depth to $16$ layers for $w=1536$, allowing training to fit on 2 L40S GPUs.
L182: We show qualitative results in cite92†Figure 4 . When the model width is set to $w=V\times c$ (column 2), both configurations generate noisy chunks that are not coherently assembled. In contrast, with a wider model ($w=1536$, column 3), both models produced substantially more coherent scenes. The $(16,64)$ model exhibits slightly degraded quality compared to the ground-truth scenes. While the $(8,64)$ model more effectively overfits to the training data.
L183: This highlights the importance of having higher compression ratios, allowing for a larger margin between model width and flattened vector set dimension leading to better performance overall.
L184: Table 2. Evaluation of the impact of compression ratio and model width on memory consumption and performance of the sketch-to-world model using the medieval overfit set.
L185: 
L186: VecSet Size  | BS  | Width  | Depth  | VRAM  | RMSE$\downarrow$ $(R,C)$  | CD$\downarrow$ $(R,C)$
L187: (16, 64)  | 24  | 1024  | 24  | 40 GB  | 0.270  | 0.591
L188: (16, 64)  | 24  | 1536  | 16  | 70 GB  | 0.150  | 0.266
L189: (8, 64)  | 24  | 512  | 24  | 18 GB  | 0.312  | 0.663
L190: (8, 64)  | 24  | 1536  | 16  | 70 GB  | 0.078  | 0.161
L191: cite93†Image: Refer to caption Figure 4. Qualitative comparison of ground-truth NuiScene scenes and generated outputs from sketch-to-world models on the medieval overfit set across different VecSet compression ratios and model widths. Table 3. Full-set evaluation on the medieval validation set across different scene size ranges, with CD also reported for scene layouts predicted by the scene size predictor.
L192: Scene Size  | RMSE$\downarrow$ $(R,C)$  | CD$\downarrow$ $(R,C)$  | CD$\downarrow$ $(\hat{R},\hat{C})$
L193: $[225,625)$  | 0.210  | 0.337  | 0.904
L194: $[625,1024]$  | 0.241  | 0.449  | 1.418
L195: $[225,1024]$  | 0.220  | 0.373  | 1.070
L196: cite94†Image: Refer to caption Figure 5. Qualitative comparison with Trellis 2. Trellis 2 takes as input a rendered view of the scene generated by our sketch-to-world model (top left), which itself is conditioned on the sketch shown in the bottom left. To better utilize the $1024\times 1024$ input resolution for Trellis 2 and minimize detail loss for elongated scenes, we rotate the scene during rendering.
L197: The center column shows the fully generated scenes, while the right column presents zoomed-in renderings.
L198: ### 5.4. Full Set Training
L199: We show full set medieval training results in cite95†Table 3 using the best settings from the ablation, i.e., $(8,64)$ VecSet size, model width$=1536$, depth$=16$, and batch size of $24$. We observe higher RMSE and CD scores for larger scene sizes (row 2 compared to row 1).
L200: This is because sketches have $512^{2}$ resolution with larger scenes having coarser sketches, so the model needs to infer plausible content in those regions that may not be 100% aligned with the ground truth scene contributing to the the larger values.
L201: When using predicted scene layouts $(\hat{R},\hat{C})$ using the scene size predictor, we do notice a drop in performance. This is due to a relatively small training size of $7200$ and the low sketch resolution leading to inaccurate size predictions. However, we note that each scene chunk spans a length of $2$ in the global space, so the average CD still remains within the extent of a single scene chunk.
L202: #### 5.4.1. Trellis 2 Comparison
L203: 
L204: cite96†Figure 5 shows results on the full set cyberpunk scenario compared with Trellis 2 (cite53†Xiang et al., 2025a ). We observe artifacts caused by their uniform voxel grid allocation (cite60†Figure 2 ) results in holes in the generated meshes. In contrast, our model maintains consistent details even for larger scenes.
L205: We show runtime statistics in cite74†Table 4 . For Trellis (cite55†Xiang et al., 2025b ) and Trellis 2, we benchmark two inputs: the cyberpunk scene generated by Nano Banana (cite52†Figure 3 ) and the large scene in cite96†Figure 5 . For NuiScene and our method, we pick another sketch from the validation set with $15\times 15$ size with the same scene elements. The scene sizes here are measured in our chunk sizes, as the output scenes do not have an absolute metric scale.
L206: For Trellis and Trellis 2, the number of sparse voxels (tokens) during inference decreases for larger scenes (column 3), due to the aspect ratio and size. Resulting in the loss of detail and fidelity. In contrast, the number of tokens in our model scales with the scene size, preserving a consistent level of detail. One limitation is our decoding time (column 6), however, this may be improved with techniques like FlashVDM (cite97†Lai et al., 2025b ).
L207: Table 4. Resource usage and generation statistics for different methods, decode time measures the time to convert the generated embeddings into mesh. Here, scene size refers to the spatial extent of the scene depicted in the input image or sketch, expressed in terms of the chunk dimensions.
L208: Scene Size  | Method  | # Token  | VRAM  | Emb Gen Time (s)  | Decode Time (s)
L209: $12\times 13$  | Trellis  | 20014  | 16 GB  | 9.94  | 58.25
L210: $18\times 51$  | Trellis  | 8713  | 13 GB  | 8.64  | 25.34
L211: $12\times 13$  | Trellis 2  | 18340  | 34 GB  | 55.19  | 84.94
L212: $18\times 51$  | Trellis 2  | 8488  | 28 GB  | 22.42  | 72.15
L213: $15\times 15$  | NuiScene  | –  | 7 GB  | 18.92  | 62.00
L214: $18\times 51$  | NuiScene  | –  | 7 GB  | 47.19  | 278.76
L215: $15\times 15$  | Ours  | 225  | 19 GB  | 5.96  | 64.61
L216: $18\times 51$  | Ours  | 918  | 19 GB  | 5.56  | 276.76
L217: cite98†Image: Refer to caption Figure 6. The top row shows a large medieval scene image and its corresponding sketch both generated by Nano Banana. The bottom row presents the results produced by Trellis 2 and our XL model using the above as input. Zoom in for more details.
L218: ### 5.5. Generalization to Unseen Sketch
L219: In cite99†Figure 6 , we demonstrate our method’s generalization to unseen sketches by using Gemini to convert a large scene image into a sketch. For this experiment, we use the XL model trained on the medieval scenario, and we set $(R,C)=(40,40)$ during inference. As shown, our model exhibits a degree of generalization, capturing structures such as circular walls and the corresponding wheat fields and farm barns in the relevant sketch regions.
L240:   * Esser et al. (2024) P. Esser, S. Kulal, A. Blattmann, R. Entezari, J. Müller, H. Saini, Y. Levi, D. Lorenz, A. Sauer, F. Boesel, et al. Scaling rectified flow transformers for high-resolution image synthesis. In Forty-first international conference on machine learning, Cited by: cite113†§B.1.2 .
L244:   * Ho et al. (2020) J. Ho, A. Jain, and P. Abbeel Denoising diffusion probabilistic models. Advances in neural information processing systems 33, pp. 6840–6851. Cited by: cite113†§B.1.2 , cite117†§3.1.2 , cite118†§4.1.2 .
L245:   * Huang et al. (2025) Z. Huang, J. He, X. Huang, Z. Xiong, Y. Luo, J. Ye, W. Li, Y. Chen, and T. Han MajutsuCity: language-driven aesthetic-adaptive city generation with controllable 3d assets and layouts. arXiv preprint arXiv:2511.20415. Cited by: cite119†§1 , cite120†§2.3 .
L249:   * Lee et al. (2025) H. Lee, Q. Han, and A. X. Chang NuiScene: exploring efficient generation of unbounded outdoor scenes. In Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), pp. 26509–26518. Cited by: cite119†§1 , cite123†§2.1 , cite124†§3.1.1 , cite111†§3.1 , cite110†§4.1.1 , cite125†§5.2.1 , cite126†§5.3.1 , cite89†Table 1 , cite127†Table 1 .
L250:   * Lee et al. (2024) J. Lee, S. Lee, C. Jo, W. Im, J. Seon, and S. Yoon Semcity: semantic scene generation with triplane diffusion. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 28337–28347. Cited by: cite123†§2.1 .
L251:   * Li et al. (2025a) S. Li, C. Yang, J. Fang, T. Yi, J. Lu, J. Cen, L. Xie, W. Shen, and Q. Tian WorldGrow: generating infinite 3d world. arXiv preprint arXiv:2510.21682. Cited by: cite123†§2.1 .
L252:   * Li et al. (2025b) Z. Li, Y. Wang, H. Zheng, Y. Luo, and B. Wen Sparc3D: sparse representation and construction for high-resolution 3d shapes modeling. arXiv preprint arXiv:2505.14521. Cited by: cite116†§1 .
L253:   * Lipman et al. (2022) Y. Lipman, R. T. Chen, H. Ben-Hamu, M. Nickel, and M. Le Flow matching for generative modeling. arXiv preprint arXiv:2210.02747. Cited by: cite113†§B.1.2 , cite118†§4.1.2 , cite128†§4.2.1 .
L254:   * Liu et al. (2024) Y. Liu, X. Li, X. Li, L. Qi, C. Li, and M. Yang Pyramid diffusion for fine 3d large scene generation. In European Conference on Computer Vision, pp. 71–87. Cited by: cite123†§2.1 .
L255:   * Loshchilov and Hutter (2016) I. Loshchilov and F. Hutter Sgdr: stochastic gradient descent with warm restarts. arXiv preprint arXiv:1608.03983. Cited by: cite129†§B.1.1 .
L256:   * Loshchilov and Hutter (2017) I. Loshchilov and F. Hutter Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101. Cited by: cite129†§B.1.1 .
L257:   * Lu et al. (2025) K. Lu, S. Zhou, H. Xu, G. Xu, Z. Yang, Y. Wang, Z. Xiao, J. Long, and M. Li Yo’city: personalized and boundless 3d realistic city scene generation via self-critic expansion. arXiv preprint arXiv:2511.18734. Cited by: cite119†§1 , cite120†§2.3 .
L258:   * Lugmayr et al. (2022) A. Lugmayr, M. Danelljan, A. Romero, F. Yu, R. Timofte, and L. Van Gool Repaint: inpainting using denoising diffusion probabilistic models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 11461–11471. Cited by: cite123†§2.1 .
L259:   * Meng et al. (2025) Q. Meng, L. Li, M. Nießner, and A. Dai Lt3sd: latent trees for 3d scene diffusion. In Proceedings of the Computer Vision and Pattern Recognition Conference, pp. 650–660. Cited by: cite123†§2.1 .
L382: 30 "material": "sleek_glass_panels, brushed_aluminum_frames, cool_blue_and_white_neon_strips",
L383: 
L397: 38 "material": "dark_grey_asphalt, glowing_yellow_caution_stripes",
L398: 
L399: 39 "layout": "A continuous perimeter road enclosing the entire square base on all four sides. Internal temporary access roads made of reinforced concrete slabs lead from the perimeter to the central construction zone."
L400: 
L401: 40 },
L402: 
L403: 41 "vehicles": {
L404: 
L405: 42 "type": "heavy_construction_and_transport",
L406: 
L407: 43 "count": 8,
L408: 
L409: 44 "style": "low-poly_industrial_machinery",
L410: 45 "details": "Large flatbed trucks carrying metal plates, mobile cranes lifting hull segments, and small robotic loaders moving materials.",
L411: 
L412: 46 "layout": "Driving along the perimeter roads and actively working within the central construction site."
L413: 
L414: 47 },
L415: 
L416: 48 "street_furniture": {
L417: 
L418: 49 "items": {
L419: 
L420: 50 "type": "construction_site_elements",
L421: 
L422: 51 "style": "utilitarian_and_temporary",
L423: 52 "placement": "Tall temporary floodlight towers surrounding the spaceship, stacks of raw materials, construction barriers, and small automated worker bots on the scaffolds."
L424: 
L425: 53 }
L426: 
L427: 54 },
L428: 
L429: 55 "terrain": {
L430: 
L431: 56 "surface": "industrial_concrete_slab",
L432: 
L433: 57 "details": "The central ground level is heavy-duty concrete, marked with tire treads, oil stains, and temporary power cables running to the scaffolding.",
L434: 
L435: 58 "margins": "clean_cut_asphalt_edges_of_the
L436: 
L437: 59 _perimeter_road_floating_in_void",
L438: 
L439: 60 }
L440: 
L441: 61 },
L442: 62 "lighting_and_atmosphere": {
L443: 
L444: 63 "time_of_day": "night",
L445: 
L446: 64 "shadows": "harsh, dynamic_shadows_from_floodlights_and_welding
L447: 
L448: 65 _flashes",
L449: 
L450: 66 "mood": "industrial, busy, constructive, high-tech_engineering, impressive scale",
L451: 
L452: 67 }
L453: 
L454: 68 } Use reference image’s style and content from the json prompt.
L455: The rationale for both of these strategies is that we wanted generated images to have similar styles and settings such that NuiScene would have larger probability of piecing together different scenes during data generation. And that the elements across different scenes would appear natural when placed together.
L456: #### A.0.2. Colored Point Cloud Sampling
L457: We mostly follow NuiScene’s protocol for converting scenes into occupancies and sampling point clouds. We encourage reader’s to see their paper for more details regarding the conversion process. To support the color training of our model, after we obtain the uncolored mesh from marching cubes of the converted occupancies from scenes. We first sample a point cloud along the surface of the output glb file from Trellis 2.
L458: We then use barycentric coordinates for the point cloud from their corresponding triangle face to convert to uvs and obtain RGB colors. Then for each vertex in the marching cubes mesh we assign it the color of its nearest neighbor. Finally, when we sample point clouds from the colored marching cubes mesh we can get both coordinates and color.
L459: cite151†Image: Refer to caption Figure 12. Prompting strategy to use image input as reference for style and accompanying JSON prompt for the content of the isometric chunk image.
L460: ## Appendix B Model Hyperparameters
L461: 
L462: ### B.1. NuiScene
L463: #### B.1.1. VAE
L464: 
L465: Similar to NuiScene we use a sampled colored point cloud size of $4096$ as input. And the training is supervised with $4096$ query points for occupancy. In addition, we use sample another $2048$ points from the scene chunk and supervise the color training using coordinates as query and color as supervision for the prediction. The decoder consists of $24$ self-attention layers. The vector set size and usage of up-sampling layers is as specified in the main paper.
L466: Training a VAE from scratch for each scenario is prohibitively time-consuming. Since we had already conducted experiments using two different sets of medieval images and bootstrapped scenes, we reuse the pretrained weights of this model and fine-tune it for the final medieval, desert, and cyberpunk scenarios.
L467: The pretrained model was initially trained on a set of bootstrapped medieval scenes for 160 epochs using AdamW (cite152†Loshchilov and Hutter, 2017 ) with a learning rate of 5e-5 and cosine annealing (cite153†Loshchilov and Hutter, 2016 ). It was then further trained on a different set of medieval scenes using the same learning rate for an additional 60 epochs. For each final scenario, the model is fine-tuned separately using this set of weights for 60 epochs each.
L468: We conduct training on either 2 L40s GPUs or 4 A5000 GPUs with the effective total batch size of 40 quad chunks.
L469: #### B.1.2. Quad Chunk Diffusion
L470: 
L471: We mostly follow the same hyperparameters for training the Quad Chunk Diffusion model as in NuiScene. The main difference is that we switched from DDPM (cite79†Ho et al., 2020 ) to rectified flow (cite83†Lipman et al., 2022 ). Similar to SD3 (cite154†Esser et al., 2024 ) we use logit normal sampling for time steps with mean=0 and std=1.
L472: ### B.2. Sketch to World Model
L473: For our default model, we use the sketch-to-world model with $512$ input channels for the vector set size of $(8,64)$. With a model depth of $16$ and width of $1536$ and a total batch size of $24$. We train the model for $320$ epochs using AdamW with a learning rate of 1e-4 with cosine annealing. For rectified flow we use mean=1.0 and std=1.0 following the settings in Trellis (cite55†Xiang et al., 2025b ). The overfitting and full set training models were trained with 2 L40s GPUs.
L474: For the further fine-tuning with scenes sizes of $[1024,1600]$, we train with 4 L40s GPUs with the same batch size $24$ and learning rate of 5e-5 for $320$ epochs.
L475: cite155†Image: Refer to caption Figure 13. Prompting strategy to takes a large scene image, extract a smaller crop, combined with a JSON instruction prompt to guide Nano Banana to generate a clean, isolated isometric chunk image. cite156†Image: Refer to caption Figure 14. Images generated for the medieval scenario using Nano Banana. cite157†Image: Refer to caption Figure 15. Scenes reconstructed for the medieval scenario using Trellis 2. cite158†Image: Refer to caption Figure 16.
L476: Images generated for the desert scenario using Nano Banana. cite159†Image: Refer to caption Figure 17. Scenes reconstructed for the desert scenario using Trellis 2. cite160†Image: Refer to caption Figure 18. Images generated for the cyberpunk scenario using Nano Banana. cite161†Image: Refer to caption Figure 19. Scenes reconstructed for the cyberpunk scenario using Trellis 2.
L477: Experimental support, please cite162†view the build logs for errors. Generated by cite163†L A T E xml†math.nist.gov .
L478: ## Instructions for reporting errors
L479: 
L480: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
L481: 
L482:   * Click the "Report Issue" () button, located in the page header.
L483: 
L484: Tip: You can select the relevant text first, to include it in your report.
L485: Our team has already identified cite164†the following issues†github.com . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
L486: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a cite165†list of packages that need conversion†github.com , and welcome cite166†developer contributions†github.com .
L487: 
L488: We gratefully acknowledge support from our major funders, cite167†member institutions†info.arxiv.org , , and all contributors.
L489: cite168†About†info.arxiv.org · cite169†Help†info.arxiv.org · cite170†Contact†info.arxiv.org · cite171†Subscribe†info.arxiv.org · cite172†Copyright†info.arxiv.org · cite173†Privacy†info.arxiv.org · cite174†Accessibility†info.arxiv.org · cite175†Operational Status (opens in new tab)†status.arxiv.org L490: 
L491: Major funding support from

