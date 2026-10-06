[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Learning to Drive is a Free Gift: Large-Scale Label-Free Autonomy Pretraining from Unposed In-The-Wild Videos

[3] h6: Abstract

[4] p: Ego-centric driving videos available online provide an abundant source of visual data for autonomous driving, yet their lack of annotations makes it difficult to learn representations that capture both semantic structure and 3D geometry. Recent advances in large feedforward spatial models demonstrate that point maps and ego-motion can be inferred in a single forward pass, suggesting a promising direction for scalable driving perception. We therefore propose a label-free, teacher-guided framework for learning autonomous driving representations directly from unposed videos. Unlike prior self-supervised approaches that focus primarily on frame-to-frame consistency, we posit that safe and reactive driving depends critically on temporal context. To this end, we leverage a feedforward architecture equipped with a lightweight autoregressive module, trained using multi-modal supervisory signals that guide the model to jointly predict current and future point maps, camera poses, semantic segmentation, and motion masks. Multi-modal teachers provide sequence-level pseudo-supervision, enabling LFG to learn a unified pseudo-4D representation from raw YouTube videos without poses, labels, or LiDAR. The resulting encoder not only transfers effectively to downstream autonomous driving planning on the NAVSIM benchmark, surpassing multi-camera and LiDAR baselines with only a single monocular camera, but also yields strong performance when evaluated on a range of semantic, geometric, and qualitative motion prediction tasks. These geometry and motion-aware features position LFG as a compelling video-centric foundation model for autonomous driving.

[5] figure: Figure 1 : LFG learns a unified pseudo-4D representation of geometry, semantics, motion, and short-term future evolution directly from unposed, unlabeled single-view driving videos. A single feedforward encoder processes observed frames and produces temporally consistent predictions of 3D point maps, camera poses, semantic layouts, confidence, and motion masks for both current and future frames.

[6] h2: 1 Introduction

[7] p: In-the-wild, ego-centric driving videos available online provide an abundant source of visual data for driving, yet their lack of annotations makes it difficult to learn representations that capture both semantic, temporal structure and 3D geometry. Inspired by the recent success of GPT-style models [ 20 , 5 ] and DINOv3 [ 23 ] trained on massive unlabeled internet corpora, a natural question arises: can we similarly leverage large amounts of raw video to learn geometry and motion aware features for autonomy?

[8] p: Recent research in autonomy has shown that scaling up improves performance [ 8 , 16 , 4 ] , yet most approaches still rely heavily on labeled data in the form of expert actions, LiDAR scans, odometry, and semantic annotations. Meanwhile, in-the-wild driving videos are abundant and capture a wide range of visual conditions and traffic situations. Although these videos provide only RGB information, they contain rich visual and motion cues that can be learned. If we aim to build scalable autonomy models capable of producing expressive and actionable representations, they should benefit from large-scale pretraining on unlabeled images and videos.

[9] p: This motivates the goal of learning structure and motion directly from video. Feedforward 3D reconstruction models already demonstrate that it is possible to estimate camera poses and point maps from unposed image sequences using a single forward pass [ 26 , 28 ] . Egocentric driving videos provide ideal data for such models, as consecutive frames naturally encode geometry and ego-motion, even with sparse viewpoints. Yet for autonomous driving, a model must ultimately do more: beyond reconstructing the present, it must predict future motion and geometry .

[10] p: Motivated by findings that humans make low-level driving decisions from only a short motion history, we extend the feedforward reconstruction model π 3 \pi^{3} [ 28 ] to predict future geometry, confidence, and motion. Our model is trained using signals from multiple large-scale models trained on unposed data, which provide complementary cues for geometry, motion, and semantics. By integrating these cues and incorporating segmentation and motion components, the student model learns from in-the-wild driving videos to produce a pseudo-4D output that captures scene structure together with the motion of dynamic agents.

[11] p: We introduce LFG – L earning to drive is a F ree G ift – a label-free, teacher-guided approach for learning such representations from vision alone. We formulate future prediction as a next-token prediction problem over geometry, motion, and semantic features. A lightweight autoregressive transformer is added after the reconstruction aggregator, enabling a student model trained on a subset of views to benefit from stronger models with access to the full sequence. Supervision comes from several specialized teachers—SegFormer [ 31 ] for semantics, SAM2 [ 13 ] and CoTracker3 [ 10 ] for motion cues —each used in a way that best leverages its strengths on unlabeled driving video.

[12] p: Unlike large world models that still require a degree of supervised labels [ 6 , 7 , 1 , 12 ] , LFG focuses on a short-horizon, feedforward formulation that sets a new standard among geometry-aware models for autonomy. On the NAVSIM planning benchmark [ 4 ] , LFG achieves state-of-the-art performance using only a single front-camera view , outperforming multi-view and BEV-based methods such as UniAD [ 14 ] and HydraMDP [ 16 ] , which rely on multiple cameras, LiDAR, or both. LFG pretraining also provides strong sample efficiency: with only 10% labeled data, it achieves competitive planning performance, underscoring the value of large-scale training on unlabeled driving video. Beyond planning, LFG produces geometry- and motion-aware features that transfer effectively to tasks spanning semantics, 3D structure, and decision making, underscoring its broader applicability as a backbone for next-generation autonomous driving systems.

[13] h5: Our main contributions are as follows:

[14] p: We propose LFG , a label-free, video-centric pre-training framework that learns geometry-, motion-, and semantics-aware representations directly from unposed, single-view driving videos.

[15] p: We design a unified architecture built on a pretrained encoder and a causal autoregressive module, enabling short-horizon prediction of point maps, camera poses, semantic layouts, confidence maps, and motion masks under multiple teacher-guided supervision.

[16] p: We demonstrate that LFG serves as a strong foundation for autonomy: it achieves state-of-the-art planning performance using only a single front camera, exhibits compelling data efficiency, and transfers effectively across semantic, geometric, and motion tasks. We emphasize that the novelty of LFG lies more within the pretraining paradigm than the model itself.

[17] h2: 2 Related Work

[18] figure: Figure 2 : LFG architecture. Starting from unposed single-view driving clips, a pretrained π 3 \pi^{3} backbone encodes N N observed frames into latent scene tokens. A lightweight causal autoregressive transformer rolls out M M future tokens, which a shared decoder maps to point maps, camera poses, semantic segmentation, confidence maps, and motion masks for all N + M N{+}M frames. Multi-modal teachers provide pseudo-supervision, enabling LFG to learn a unified pseudo-4D representation that transfers effectively to downstream planning.

[19] p: Pretraining for Autonomous Driving. Pretraining for autonomous driving has only recently gained traction. Early self-supervised pretraining work such as SelfD [ 36 ] and ACO [ 37 ] demonstrated that large-scale in-the-wild driving videos can provide supervisory signals for learning semantic and geometric priors without human labels. PPGeo [ 29 ] further explored geometry-oriented pretraining using photometric and consistency-based objectives to learn depth and ego-motion. ViDAR [ 34 ] proposes to use future point-cloud prediction from historical camera inputs as a unified pretext task. UniPAD [ 32 ] introduces a self-supervised learning paradigm that uses 3D volumetric differentiable rendering to implicitly encode continuous 3D structures. VisionPAD [ 35 ] focuses on vision-centric algorithms by leveraging efficient 3D Gaussian Splatting and a multi-frame photometric consistency objective to reconstruct multi-view representations using only images. However, these approaches largely rely on frame-to-frame consistency losses that implicitly assume static scenes, limiting their ability to capture dynamic objects that are central to real driving environments. In contrast, our method is pretrained directly on unlabeled driving video by explicitly modeling dynamic geometry, motion cues, and scene semantics, yielding a dense 4D representation that better captures the structure and dynamics of real-world driving.

[20] p: Geometry-aware vision backbones for driving. Classical 3D reconstruction pipelines in autonomy rely on Structure-from-Motion (SfM) and Multi-View Stereo (MVS) [ 22 ] , often combined with LiDAR, to triangulate scene points and build dense maps for localization. While effective, these methods are typically tailored per scene and are not naturally suited as general-purpose backbones for large-scale video pretraining. In contrast, recent feedforward approaches [ 26 , 28 , 19 , 25 , 15 ] amortize reconstruction by predicting point maps, confidence maps, and camera poses for unposed image sequences in a single pass, making them attractive as scalable, geometry-aware backbones for driving. LFG belongs to this family but focuses on temporal understanding, producing a pseudo-4D representation of dynamic driving scenes that is well suited for downstream planning and perception.

[21] h2: 3 Method

[22] p: We introduce LFG (shown in Fig. 2 ), a method for learning a powerful driving-vision model from unposed and unlabelled single view Youtube videos.

[23] figure: Figure 3 : π 3 \pi^{3} -to-LFG distillation. We transfer geometric knowledge from the pretrained π 3 \pi^{3} teacher to LFG by supervising point maps, confidence maps, and camera poses for all observed and future frames. While the teacher has access to the full sequence, the student sees only the first N N frames and must predict both current and future geometry, enabling LFG to learn temporally consistent scene structure and future ego-motion from partial observations.

[24] h3: 3.1 Problem Formulation

[25] p: We consider the case of learning to drive, where a large parameterized model is given a consecutive sequence ( I t ) t = 1 N (I_{t})_{t=1}^{N} of N N ego-centric RGB images I t ∈ ℝ 3 × H × W I_{t}\in\mathbb{R}^{3\times H\times W} , in a variety of driving scenes. The goal is to efficiently predict scene information that is useful for autonomous driving. We posit that this includes both current and short-horizon future information. We posit that this includes current and future information in the recent future. Such a model should predict 𝒪 \mathcal{O} relevant modalities of scene information, as well as the future M M frames of the scene. Inspired by prior work in label-free pretraining and world models for driving, we choose to predict the following outputs.

[26] p: LFG processes in-the-wild video through a pretrained encoder and a causal autoregressive transformer to jointly predict current and short-horizon future scene geometry, semantics, and motion. First, our model should predict point maps for the ego-view camera over time. ( P t ) t = 1 N + M , P t : ℐ ⁡ ( I t ) → ℝ 3 (P_{t})_{t=1}^{N+M},\quad P_{t}:\mathcal{I}(I_{t})\rightarrow\mathbb{R}^{3} , where ℐ ⁡ ( I t ) \mathcal{I}(I_{t}) maps each pixel in I t I_{t} to P t ​ ( 𝐲 ) ∈ ℝ 3 P_{t}(\mathbf{y})\in\mathbb{R}^{3} , which is the 3D world point corresponding to pixel 𝐲 \mathbf{y} at time t t .

[27] p: Second, our model predicts camera poses : ( T t ) t = 1 N + M , T t ∈ ℝ 4 × 4 (T_{t})_{t=1}^{N+M},\;T_{t}\in\mathbb{R}^{4\times 4} , where each p t p_{t} is a full 4 × 4 4\times 4 homogeneous transformation matrix encoding both rotation and translation. Such poses define the ego-motion trajectory of the camera and enable mapping all predicted local 3D points into a shared world coordinate frame.

[28] p: Third, our model predicts semantic segmentation with 7 classes: ( S t ) t = 1 N + M , S t ∈ ℝ 7 × H × W (S_{t})_{t=1}^{N+M},\quad S_{t}\in\mathbb{R}^{7\times H\times W} , where each pixel’s one-hot vector S t ​ ( 𝐲 ) ∈ ℝ 7 S_{t}(\mathbf{y})\in\mathbb{R}^{7} encodes the semantic category (e.g., road, vehicle, pedestrian, building, vegetation, sky, and background). These semantic predictions provide a semantic, structured understanding of the scene, which we consider to be useful for the downstream task.

[29] p: We also predict confidence maps ( C t ) t = 1 N + M , C t : ℐ ⁡ ( I t ) → [ 0 , 1 ] , (C_{t})_{t=1}^{N+M},\quad C_{t}:\mathcal{I}(I_{t})\rightarrow[0,1], which quantifies the reliability of each pixel’s 3D prediction.

[30] p: Finally, our model should predict motion masks ( M t ) t = 1 N + M , M t : ℐ ⁡ ( I t ) → [ 0 , 1 ] , (M_{t})_{t=1}^{N+M},\quad M_{t}:\mathcal{I}(I_{t})\rightarrow[0,1], indicating which regions in the image correspond to independently moving objects (e.g., other vehicles, pedestrians) as opposed to the static environment. The motion masks help disentangle dynamic from static components of the scene, which can be used for downstream tasks, such as dynamic 4D Gaussian Splatting.

[31] p: In total, the model predicts all outputs:

[32] table: 𝒪 = { ( P t , T t , S t , C t ) t = 1 N + M , ( M t ) t = 1 N + M } , \mathcal{O}=\{(P_{t},T_{t},S_{t},C_{t})_{t=1}^{N+M},\;(M_{t})_{t=1}^{N+M}\},

[33] p: All modalities are learned jointly in an end-to-end fashion from video, with the assistance of robust teachers, promoting shared representations of geometry, semantics, and motion relevant to autonomous driving.

[34] figure: Figure 4 : Semantic distillation. A pretrained SegFormer teacher, trained on Cityscapes, provides soft semantic pseudo-labels for each frame. LFG predicts semantic maps for both observed and future frames using only the first M M inputs, learning temporally consistent scene semantics through teacher–student supervision aligned with the model’s geometric features.

[35] h3: 3.2 Architecture.

[36] p: Our model ( Fig. 2 ) is built on top of the π 3 \pi^{3} , [ 27 ] model, which is a purely feedforward model that predicts point maps, confidence maps, and camera poses from a series of unposed images. Contrary to prior work in VGGT [ 26 ] , π 3 \pi^{3} does not rely on a fixed referenced view, and is trained on more dynamic datasets, making it a suitable starting point for LFG. To receive the benefits of the pretrained π 3 \pi^{3} , we propose some simple additions on top of the model.

[37] p: First, we propose to add a causal attention autoregressive transformer after π 3 \pi^{3} ’s alternating attention module or encoder. Let the output of the π 3 \pi^{3} encoder be a sequence of latent scene tokens 𝐙 1 : N \mathbf{Z}_{1:N} , where N N is the number of observed frames. The autoregressive transformer 𝒯 AR \mathcal{T}_{\mathrm{AR}} takes these tokens as input and causally predicts additional latent tokens for M M future frames, producing 𝐙 1 : N + M = 𝒯 AR ( 𝐙 1 : N ) \mathbf{Z}_{1:N+M}=\mathcal{T}_{\mathrm{AR}}(\mathbf{Z}_{1:N}) . Each newly generated token sequence 𝐙 N + 1 : N + M \mathbf{Z}_{N+1:N+M} represents latent scene features for unobserved frames, which are decoded into 3D point maps, confidence maps, camera poses, semantic maps, and motion masks. Our causal formulation ensures that each predicted future frame can attend to past and observed frames, but not to future frames, enforcing a forward-only information flow. The semantic and motion outputs are initialized from the point decoder and their respective heads, allowing the model to leverage shared geometric features while predicting scene semantics and dynamics.

[38] h5: π 3 \pi^{3} Teacher.

[39] p: We employ a teacher π 3 \pi^{3} model, seen in Fig. 3 , that has access to N + M N+M frames from the unlabeled OpenDV dataset [ 33 ] . The teacher outputs supervision signals in the form of point maps, confidence maps, and camera poses for all N + M N+M frames. Our student model only observes the first N N frames and must predict both the observed ( N N ) and future ( M M ) outputs. Specifically, the student, LFG, predicts:

[40] table: { 𝐏 t , 𝐂 t , 𝐓 t } t = 1 N + M , \{\mathbf{P}_{t},\mathbf{C}_{t},\mathbf{T}_{t}\}_{t=1}^{N+M},

[41] p: where 𝐏 t \mathbf{P}_{t} denotes the point map, 𝐂 t \mathbf{C}_{t} the confidence map, and 𝐓 t \mathbf{T}_{t} the camera pose at frame t t . While this method is not self-supervised as compared to other works, it forces LFG to predict future information, namely the future ego motion, confidence, and geometric updates of the scene.

[42] h3: 3.3 Semantic Head

[43] p: To enable semantic understanding of the scene, our model includes a semantic head (Fig. 4 ) that predicts dense per-pixel class probabilities for each camera and timestep. Given the input sequence of N N images ( I t ) t = 1 N (I_{t})_{t=1}^{N} , the semantic head outputs a corresponding sequence of current and future semantic maps ( S t ) t = 1 N + M , S t ∈ [ 0 , 1 ] C s × H × W (S_{t})_{t=1}^{N+M},\quad S_{t}\in[0,1]^{C_{s}\times H\times W} . Since ground-truth semantic labels are unavailable for all frames, we turn to a simple teacher–student training strategy. A pretrained SegFormer model Φ seg \Phi_{\text{seg}} , trained on the Cityscapes dataset [ 2 ] , serves as the teacher network. For each image I t I_{t} , we obtain pseudo-labels: S ^ t = Φ seg ​ ( I t ) \hat{S}_{t}=\Phi_{\text{seg}}(I_{t}) . These pseudo-labels act as soft supervision targets for the semantic head. The SegFormer teacher is given access to all frames, while LFG has to predict the current and future segmentation predictions.

[44] figure: Figure 5 : Motion mask generation pipeline. We first detect human and vehicle instances in the first frame using Grounded SAM2, then track their 2D trajectories across time with CoTracker3. Using teacher π 3 \pi^{3} point maps, tracked pixels are backprojected into 3D and per-instance 3D displacements are measured over the sequence. Instances whose motion exceeds a threshold for at least K min K_{\min} frames are labeled as dynamic, and their masks are rasterized into dense per-pixel motion masks 𝐌 t \mathbf{M}_{t} , which supervise the motion head.

[45] h3: 3.4 Motion Head

[46] p: Our motion head in Fig. 5 predicts per-pixel motion masks that identify dynamic regions within a scene. Since explicit motion annotations are unavailable, we generate pseudo ground-truth (pseudo-GT) labels in a fully feedforward, label-free manner.

[47] p: We begin by segmenting human and vehicle instances from the first frame by using an off-the-shelf segmentation model, Grounded SAM2 [ 21 ] , which produces a list of tracked mask instances per object. For each detected object, we track its 2D motion across frames using CoTracker3 [ 11 ] , which provides dense correspondences in image space: 𝐮 t ( i ) = CoTracker3 ⁡ ( 𝐈 1 , … , 𝐈 T , i ) \mathbf{u}_{t}^{(i)}=\mathrm{CoTracker3}(\mathbf{I}_{1},\ldots,\mathbf{I}_{T},i) , where 𝐮 t ( i ) \mathbf{u}_{t}^{(i)} denotes the 2D tracked keypoints of object i i at frame t t .

[48] p: Next, we employ the teacher π 3 \pi^{3} model to obtain corresponding 3D point maps for each frame. For each object instance i i , we backproject the tracked 2D points into 3D using 𝐏 t \mathbf{P}_{t} , and measure the temporal displacement of the mean 3D position:

[49] table: d t ( i ) = ‖ 𝐩 ¯ t + 1 ( i ) − 𝐩 ¯ t ( i ) ‖ 2 , d_{t}^{(i)}=\left\|\bar{\mathbf{p}}_{t+1}^{(i)}-\bar{\mathbf{p}}_{t}^{(i)}\right\|_{2},

[50] p: where 𝐩 ¯ t ( i ) \bar{\mathbf{p}}_{t}^{(i)} is the mean 3D position of the object at time t t . An object is considered dynamic if its displacement exceeds a motion threshold τ motion \tau_{\text{motion}} for at least K min K_{\min} frames. Finally, we convert instance-level motion indicators m ( i ) m^{(i)} into dense motion masks 𝐌 t ∈ [ 0 , 1 ] H × W \mathbf{M}_{t}\in[0,1]^{H\times W} that serve as supervision for the motion head.

[51] h3: 3.5 Losses

[52] p: Our training objective combines multiple task-specific loss terms that jointly supervise segmentation, geometry, motion, and camera pose estimation. The total training loss is:

[53] table: ℒ total = \displaystyle\mathcal{L}_{\text{total}}= ℒ current + λ future ​ ℒ future . \displaystyle\mathcal{L}_{\text{current}}+\lambda_{\text{future}}\,\mathcal{L}_{\text{future}}. (1)

[54] table: ℒ current/future = \displaystyle\mathcal{L}_{\text{current/future}}= λ seg ​ ℒ seg + λ pose ​ ℒ pose \displaystyle\lambda_{\text{seg}}\,\mathcal{L}_{\text{seg}}+\lambda_{\text{pose}}\,\mathcal{L}_{\text{pose}} (2) + λ point ​ ℒ point + λ motion ​ ℒ motion . \displaystyle+\lambda_{\text{point}}\,\mathcal{L}_{\text{point}}+\lambda_{\text{motion}}\,\mathcal{L}_{\text{motion}}.

[55] h4: 3.5.1 Segmentation Loss.

[56] p: We use a weighted BCE loss for semantic segmentation, where we use class-specific weight to handle class imbalance. Please see the supplementary material for additional details.

[57] h4: 3.5.2 Pose Loss.

[58] p: Following the π 3 \pi^{3} formulation, we supervise the predicted camera poses using relative pose consistency across frame pairs. For any two frames ( i , j ) (i,j) , we construct relative transformations ( Δ ​ 𝐑 i ← j , Δ ​ 𝐭 i ← j ) (\Delta\mathbf{R}_{i\leftarrow j},\Delta\mathbf{t}_{i\leftarrow j}) from the student predictions and compare them against teacher-provided targets ( Δ ​ 𝐑 ^ i ← j , Δ ​ 𝐭 ^ i ← j ) (\widehat{\Delta\mathbf{R}}_{i\leftarrow j},\widehat{\Delta\mathbf{t}}_{i\leftarrow j}) . The overall loss combines rotation and translation terms:

[59] table: ℒ pose = ℒ rot + λ trans ​ ℒ trans . \mathcal{L}_{\text{pose}}=\mathcal{L}_{\text{rot}}\;+\;\lambda_{\text{trans}}\,\mathcal{L}_{\text{trans}}.

[60] p: The rotation term penalizes geodesic distance on SO ⁡ ( 3 ) \mathrm{SO}(3) between predicted and target relative rotations, while the translation term uses a robust regression loss (Huber) on relative translations to handle scale variation and outliers. This formulation enforces multi-frame pose consistency and stabilizes predictions over time.

[61] h4: 3.5.3 Confidence Loss.

[62] p: The confidence map estimates the reliability of each predicted 3D point. We supervise it using a binary target derived from the point-map reconstruction error: pixels whose point error falls below a threshold are treated as high-confidence, and others as low-confidence. We apply a binary cross-entropy loss to this target.

[63] h4: 3.5.4 Point Map Loss.

[64] p: We supervise the predicted 3D point maps using a scaled L 1 L_{1} loss to account for varying scene scales:

[65] table: ℒ point = α ​ ‖ 𝐏 − 𝐏 ^ ‖ 1 , \mathcal{L}_{\text{point}}=\alpha\,\|\mathbf{P}-\widehat{\mathbf{P}}\|_{1},

[66] p: where 𝐏 \mathbf{P} and 𝐏 ^ \widehat{\mathbf{P}} denote the predicted and target point maps, respectively, and α \alpha is a learned or fixed scaling factor that normalizes for scene scale. This formulation encourages accurate 3D reconstruction while remaining robust to the absolute magnitude of the scene, analogous to the Huber-based translation loss used for relative camera motion, where we also apply a scale.

[67] h4: 3.5.5 Motion Loss.

[68] p: The motion head is trained with a binary cross-entropy loss between the model prediction (LFG) and the pseudo ground-truth (GT):

[69] table: ℒ motion = − ∑ [ M GT log M LFG + ( 1 − M GT ) log ( 1 − M LFG ) ] . \mathcal{L}_{\text{motion}}=-\sum\big[M^{\text{GT}}\log M^{\text{LFG}}+(1-M^{\text{GT}})\log(1-M^{\text{LFG}})\big].

[70] h4: 3.5.6 Future Frame Weighting.

[71] p: To emphasize the model’s ability to predict beyond observed frames, we apply a temporal weighting factor ω t \omega_{t} to all losses on future frames, keeping ω \omega fixed:

[72] table: ℒ future = ∑ t = M + 1 N + M ω ​ ℒ t , with ​ ω > 1 . \mathcal{L}_{\text{future}}=\sum_{t=M+1}^{N+M}\omega\,\mathcal{L}_{t},\quad\text{with }\omega>1.

[73] p: This encourages accurate extrapolation of geometry and motion into the future time steps.

[74] p: Together, these terms ensure LFG spatially and semantically understands the scene, as well as how the scene will evolve in a recent future time window. By nature, LFG exhibits generative qualities in its autoregressor; however, we assert that this is needed for next frames prediction.

[75] h3: 3.6 Training

[76] p: We train LFG in three stages. The first stage ensures that LFG can predict future geometry and pose autoregressively. This provides the autoregressive transformer a strong initialization to train the segmentation head, while not having to relearn future geometry and motion. Finally, we train on the motion masks, initialized from the point decoder. In each stage, LFG is trained end-to-end. We exclusively use the OpenDV Driving Youtube Daatset, and opt for a subset of it, consisting of approximately 2 million samples across varied driving conditions, scenes, traffic and external driver/pedestrian situations. We train our model on 2 2 , 5 5 , and 10 10 Hz frames (without any conditioning LFG on frequency of input frames) to improve robustness.

[77] h3: 3.7 Fine-tuning for Planning

[78] p: With a strong pretrained encoder that captures temporal and spatial scene structure from sequential images, we now demonstrate how this representation benefits downstream planning. We fine-tune on the NAVSIM planning benchmark [ 4 ] using only front-view camera inputs over three consecutive frames to predict future trajectories in complex driving scenarios.

[79] p: The pretrained image encoder backbone is kept frozen and, for each frame, outputs high-dimensional autonomy tokens that encode the ego vehicle’s motion state and surrounding context. We run LFG to produce the future tokens for learning. These per-frame features are aggregated and passed to a lightweight multi-modal anchor-based trajectory decoder that directly predicts multiple candidate trajectories in a single forward pass, similar to [ 17 ] but without any diffusion or iterative refinement. The decoder attends from autonomy features to trajectory anchors and across trajectory modes, then outputs confidence scores and coordinate offsets, selecting the highest-confidence mode as the final plan.

[80] p: This simple yet effective fine-tuning strategy allows the planner to directly leverage the pretrained temporal representation for the planning task, leading to strong gains in data efficiency. In our experiments (Sec. 4.2.4 ), we show that this strong pretrained encoder substantially improves planning performance and data efficiency compared to state-of-the-art models that utilize multi-view or LiDAR inputs, as well as other pretrained encoders [ 30 ] .

[81] h2: 4 Experiments

[82] h3: 4.1 Implementation and Training

[83] h4: 4.1.1 Model and Pretraining.

[84] p: We implement our model by closely following the architecture of the original π 3 \pi^{3} backbone, which contains approximately 1 billion parameters. In total, LFG contains 1.45B parameters, and runs at 5Hz on an NVIDIA RTX 5090 GPU. The image encoder is initialized from a DINOv2-pretrained backbone, and we directly follow the π 3 \pi^{3} alternating attention module. The point, confidence, and camera heads are frozen. The semantic and motion mask head are initialized from the point head. Our causal autoregressive transformer consists of 4 layers with 8 attention heads and a dropout rate of 0.1. It takes the latent scene tokens from the π 3 \pi^{3} encoder and autoregressively predicts future frame tokens, which are then decoded to point maps, semantic maps, confidence maps, camera poses, and motion masks.

[85] h4: 4.1.2 Training Setup.

[86] p: We train the model using the AdamW optimizer with a base learning rate of 10 − 4 10^{-4} . A linear warmup schedule is used for the first 500 steps, starting from 0.1 × 0.1\times the base learning rate and increasing to the full learning rate. After warmup, we apply cosine annealing over the remaining training steps. Gradients are clipped to a maximum norm of 1.0, and mixed-precision training (BF16) is enabled. We perform gradient accumulation to increase batch size. We also randomly apply color jittering, Gaussian blur, and grayscale augmentation to the frames of the student LFG, while letting the teacher receive unaugmented images. We train on 32 A100 GPUs for 40,000 iterations. The model is trained using a combination of losses, including scaled L 1 L_{1} for 3D points ( α = 1.0 \alpha=1.0 ), Huber loss for camera translation ( 0.1 0.1 ), confidence loss ( 0.05 0.05 ), segmentation loss ( 1.0 1.0 ), and motion loss ( 1.0 1.0 ). To emphasize accurate prediction of future frames, we apply a weight of ω = 10.0 \omega=10.0 to the corresponding losses. Finally, we normalize all geometric outputs to ensure stable learning during training.

[87] h3: 4.2 Results

[88] p: We evaluate LFG on a suite of downstream tasks that jointly probe semantics, geometry, motion, and decision making. Concretely, we consider (i) semantic segmentation, (ii) depth, point map, and camera pose prediction, and (iii) encoder-only downstream benchmarks, planning. We additionally provide qualitative motion visualizations. These tasks allow us to assess both the quality of the learned scene representation and its usefulness as a backbone for autonomous driving.

[89] figure: Figure 6 : Segmentation quality on current and future frames. We show results of segmentation on the 1st frame, as well as future frames. LFG decouples dynamic motion from its own movement.

[90] h4: 4.2.1 Semantic segmentation

[91] figure: Table 1 : Semantic segmentation metrics (overall vs. predicted). Method Overall Pred. PA mIoU mDice FW PA mIoU mDice FW Static baseline – – – – 0.888 0.420 0.502 0.810 SegFormer 0.926 0.677 0.744 0.723 0.926 0.680 0.747 0.725 MaskFormer 0.922 0.760 0.829 0.760 – – – – LFG 0.947 0.768 0.827 0.770 0.942 0.751 0.814 0.759

[92] p: We evaluate on semantic segmentation using KITTI-360 [ 18 ] with samples of 6 consecutive frames for 200 varied sequences. We compare: the segmentation teacher model SegFormer with all 6 RGB images as input, a MaskFormer baseline evaluated on overall frames (no future prediction), and our model with only the first 3 frames as input while predicting for all 6 frames. To measure the model’s ability to anticipate future scene layout, we also provide the score between the ground truth semantic segmentation of the third frame compared to the following frames. We report standard segmentation metrics (pixel accuracy, mIoU, mDice, frequency weighted IoU) on all frames and only future frames. Table 1 shows that SegFormer is a stronger baseline than MaskFormer in this setting, and that our model not only beats its SegFormer teacher on overall semantic segmentation, but also on future frames where the teacher model was fed the RGB images and LFG was not.

[93] h4: 4.2.2 Monocular depth estimation

[94] figure: Table 2 : Depth estimation results for overall and predicted frames. Dataset Method Overall Predicted AbsRel RMSE AbsRel RMSE KITTI-360 π 3 \pi^{3} 0.26 ± 0.08 4.37 ± 0.65 0.26 ± 0.07 4.37 ± 0.66 LFG 0.27 ± 0.07 4.38 ± 0.64 0.31 ± 0.11 4.38 ± 0.68 VGGT – 4.46 ± 0.82 – 4.46 ± 0.82 DA3 – 4.43 ± 0.81 – 4.44 ± 0.81 Waymo π 3 \pi^{3} 0.19 ± 0.12 6.68 ± 3.10 0.19 ± 0.12 6.70 ± 3.13 LFG 0.21 ± 0.11 6.87 ± 2.72 0.22 ± 0.11 7.12 ± 2.81

[95] p: For the monocular depth prediction, we evaluate on the KITTI-360 and Waymo open dataset [ 24 ] with 200 sequences of 6 frames each. We compute root mean square error in meters after a scale and shift alignment with ground truth depth, and absolute relative depth error. Similar to semantic segmentation, we use the sample of 6 frames and give all of them to the teacher model π 3 \pi^{3} and the first 3 to our model. We also include strong monocular baselines (VGGT and DA3) to contextualize teacher quality; these results indicate that π 3 \pi^{3} remains the strongest teacher in our setting. The results provided in Table 2 show that the depth prediction accuracy is on par with the teacher model (within 1 meter across the board) and only slightly worse on predicted future frames. More visualizations can be found in the supplementary.

[96] figure: Scene 1 LFG π 3 \pi^{3} Scene 2 LFG π 3 \pi^{3} Scene 3 LFG π 3 \pi^{3} Figure 7 : Qualitative comparison of full point cloud reconstructions of LFG vs. π 3 \pi^{3} . The current camera poses are in blue , and future poses in red . LFG point maps retain overall geometric quality, even on future frames, and the predicted camera motion remains precise. Dashed red outlines denote predicted frames with no ground-truth image input , produced solely from the model’s future tokens.

[97] p: Point cloud reconstruction. Fig. 7 provides a qualitative comparison of full point cloud reconstructions from LFG and π 3 \pi^{3} , illustrating that LFG preserves geometric structure and camera motion even when predicting future frames.

[98] h4: 4.2.3 Trajectory prediction

[99] figure: Table 3 : Trajectory estimation results. RelPos is split into rotation (deg) and translation (m). Dataset Method ATE Rot Trans KITTI-360 π 3 \pi^{3} 0.43 1.32 0.31 LFG 1.00 2.30 0.31 Waymo π 3 \pi^{3} 0.02 0.98 0.44 LFG 0.08 1.00 0.44

[100] p: As our model predicts camera poses of input 3 frames and future 3 frames, we evaluate the trajectory prediction on KITTI-360 and Waymo open dataset (200 sequences of 6 frames each), and compare it to π 3 \pi^{3} with all 6 frames as input. We report Absolute Trajectory Error (ATE), rotation error (Rot), and translation error (Trans). ATE measures the discrepancy between predicted and ground-truth trajectories after alignment. Rot and Trans denote the mean angular rotation error (deg) and mean translation error (m), respectively. In Table 3 , we can observe that while the metrics are slightly worse that the teacher model, the result is still competitive, considering that our model does not have access to the last 3 frames.

[101] figure: RGB LFG Motion Pseudo Motion Frame 1 Frame 2 Frame 3 Figure 8 : Failure Case of Pseudo-GT on motion . Qualitative comparison of motion predictions (LFG vs Pseudo) with corresponding RGB frames. In this scene, the pseudo ground truth incorrectly predicts a moving car on the far left when it is parked. LFG correctly predicts the static parked car (left) and the dynamic vehicle in front of it.

[102] p: We include a qualitative motion visualization in Fig. 8 , highlighting a pseudo-ground-truth failure case where LFG correctly separates static and dynamic objects.

[103] h4: 4.2.4 NAVSIM planning fine-tuning

[104] figure: Table 4: Data-efficiency comparison (PDMS↑) on NAVSIM. LFG’s pretrained encoder yields superior data efficiency, demonstrating strong performance in the low-data regime and outperforming other pretrained encoders across all label fractions. Method Input 1% 10% 100% Data DiffusionDrive 3Cam+L 64.9 72.6 88.1 DINOv3 1Cam 60.0 75.8 81.4 PPGeo 1Cam 61.5 65.6 74.6 π 3 \pi^{3} 1Cam 56.2 77.5 82.8 LFG (Ours) 1Cam 66.3 81.4 85.2 All pretrained encoders use a single front camera (3 frames) and the same anchor-based decoder. DiffusionDrive is trained end-to-end with a BEV-based ResNet backbone. L denotes LiDAR.

[105] figure: Table 5 : NAVSIM planning benchmark: single-camera LFG vs BEV-based baselines. Higher is better for all metrics. Method Input NC DAC TTC C. EP PDMS BEV Baselines UniAD 6Cam 97.8 91.9 92.9 100.0 78.8 83.4 TransFuser 3Cam+L 97.7 92.8 92.0 100.0 79.2 84.0 Hydra-MDP 3Cam+L 96.9 94.0 94.0 100.0 78.7 84.7 DiffusionDrive 3Cam+L 96.8 95.4 94.7 100.0 82.0 88.1 LFG (Ours) 1Cam ∗ 98.2 93.7 94.4 100.0 79.1 85.2 L = LiDAR. 1Cam ∗ uses only the front-view camera with past temporal frames (3-frame input).

[106] figure: Table 6 : DiffusionDrive comparison on NAVSIM (PDMS ↑ \uparrow ). Method Input 1% 10% 100% DiffusionDrive-DINOv2 3Cam+L 57.3 74.4 81.5 DiffusionDrive-DINOv2 1Cam 57.5 73.0 79.7 LFG (Ours) 1Cam 66.3 81.4 85.2

[107] p: PDMS summaries. We report PDMS scores for NAVSIM in the data-efficiency table (Table 4 ), the DiffusionDrive comparison (Table 6 ), and the component/scaling ablations (Table 7 ). Across these PDMS tables, LFG is consistently strongest at 1% and 10% labels, and remains competitive at 100%, outperforming DiffusionDrive-DINOv2 variants while benefitting from increased pretraining data and longer prediction horizons.

[108] p: Data efficiency. Tab. 4 evaluates how well different pretrained encoders transfer to NAVSIM planning as we vary the amount of training data. Among pretrained encoders, LFG consistently achieves the best PDMS across all label fractions: at 10% labels, LFG attains 81.4 PDMS, matching the full-data performance of DINOv3, which highlights the effectiveness of our in-the-wild video pretraining. We attribute these gains to the encoder’s stronger temporal understanding of the scene, allowing it to better leverage short past frame sequences for planning. It surpasses both one of its teachers π 3 \pi^{3} and PPGeo [ 30 ] , demonstrating how both powerful feedforward architectures need semantic and temporal understanding of the future. More ablations are provided in the supplementary.

[109] figure: Table 7 : Component and scaling ablations on NAVSIM (PDMS ↑ \uparrow ). Setting 1% 10% 100% Original setting 66.3 81.4 85.2 + 2 × \times pretraining data 76.6 82.3 84.8 + Longer prediction horizon 80.5 84.4 84.8 - Seg, Motion 64.8 77.1 84.6 - Autoregressive head 66.3 77.7 84.2

[110] p: Ablations. Table 7 shows that scaling pretraining data and extending the prediction horizon both improve PDMS at low-label regimes, while removing segmentation/motion supervision or the autoregressive head degrades performance, confirming the importance of these components.

[111] p: Benchmark results. Compared to prior methods on NAVSIM ( Tab. 5 ), LFG, using only single front-view camera inputs, outperforms heavily engineered BEV-based baselines such as UniAD [ 9 ] and Hydra-MDP [ 16 ] , which rely on multi-view cameras and/or LiDAR. LFG achieves the best Not at-fault collision (NC) score (98.2) and competitive TTC and EP scores ( 94.4 and 79.1 ), resulting in an overall PDMS of 85.2 . This demonstrates that a single-camera encoder pretrained with large-scale video can rival specialized BEV-based systems that leverage significantly richer sensor suites.

[112] h2: 5 Conclusion

[113] p: In all, LFG learns directly from in-the-wild, unposed driving videos, and thanks to its strong pretrained encoder, it achieves competitive planning performance despite using only a single front-view camera. For fairness, we compare against DiffusionDrive-DINOv2 variants that use both multi-camera+LiDAR and single-camera inputs, and LFG remains stronger in this setting. For future direction, LFG predicts only short-term futures (3–6 frames), and extending the autoregressive module to longer or multi-scale temporal horizons may improve long-range reasoning. Second, we use only a single front-view camera, reflecting the fact that most in-the-wild driving videos provide only one viewpoint; while this setting already highlights the strength of video-based geometric priors, incorporating multi-view cues could further improve robustness in complex scenes. As larger multi-camera datasets such as the recently released PhysicalAI-Autonomous-Vehicles dataset [ 3 ] become available, exploring multi-view training represents a promising direction for future work.

[114] h2: References

[115] p: Supplementary Material

[116] p: This supplementary material provides additional results and implementation details. We include full training configurations in Sec. A , planning fine-tuning and baseline descriptions in Sec. B , and extended qualitative visualizations: segmentation in Sec. C , motion in Sec. D , depth in Sec. E , and point clouds in Sec. F .

[117] h2: A Training Details

[118] p: For reproducibility, we share specific training details of our model. We train LFG on top of the pretrained π 3 \pi^{3} , keeping the DINOv2 encoder frozen, as well as the confidence, camera, and point decoders, including automatic mixed precision (bfloat16) to speed up training.

[119] p: To obtain motion masks from Grounded SAM2 and CoTracker3 , we first query Grounded DINO using the object priors car , vehicle , and person , which yields an initial set of candidate instance masks. Each mask is then processed with CoTracker3 , using a grid size of 80 and a motion threshold of 0.1 0.1 in the normalized geometric space. An object is classified as dynamic if it exhibits motion in the majority of frames.

[120] p: For the segmentation loss, we apply class-specific weighting across seven categories to address inherent frequency imbalances in driving scenes. Specifically, we assign weights of 0.5 0.5 to road , 1.2 1.2 to vehicle , 1.6 1.6 to person , 1.8 1.8 to both traffic light and traffic sign , 0.3 0.3 to sky , and 0.2 0.2 to background/buildings . These weights remain fixed throughout training and were found to provide a stable and effective balance across diverse urban environments.

[121] p: We apply VGGT-style photometric augmentations during training. Color jittering perturbs brightness, contrast, and saturation by ± 40 % \pm 40\% ( 0.4 0.4 ) and hue by ± 10 % \pm 10\% ( 0.1 0.1 ). Random grayscale is applied with probability 0.1 0.1 . Additionally, we apply random Gaussian blur with probability 0.2 0.2 , using a sigma sampled uniformly from [ 0.1 , 2.0 ] [0.1,2.0] . We resize all images to ( 294,518 ) (294,518) , and train on the prior 3 images, predicting outputs for the next 3 images, but additionally train the motion head (final stage) on both the 3 prior images and 6 prior images. We vary the time between each image, randomly sampling from 2 , 5 , 10 2,5,10 Hz.

[122] h2: B Planning Fine-tuning and Baseline Details

[123] p: We fine-tune all models on the NAVSIM planning benchmark using only the front-view camera over three consecutive frames to predict 4s future ego trajectories. Unless otherwise specified, all baseline vision encoders are kept frozen and we only train lightweight causal attention adapters and a shared anchor-based trajectory decoder.

[124] h5: Common planning head.

[125] p: For all methods (ours and baselines), we employ the same anchor-based trajectory decoder. Following DiffusionDrive [ 17 ] , we adopt K = 20 K=20 trajectory anchors obtained by K-means clustering over ground-truth futures; however we omit the diffusion component and any iterative refinement to keep the architecture simple. After causal temporal aggregation from vision encoder’s embedding, the decoder attends over trajectory anchors and across modes, and in a single forward pass predicts (i) confidence scores for each of the K K modes and (ii) coordinate offsets for each waypoint along each mode. At test time, the highest-confidence mode is selected as the final plan. All models predict 8 waypoints at 0.5s intervals (a 4s horizon) and are trained with a combination of focal loss (classification over modes) and L1 regression loss on waypoints.

[126] h5: Temporal aggregation.

[127] p: For each front-view frame, the pretrained encoder produces high-dimensional autonomy tokens encoding ego motion and scene context. To exploit temporal structure, we apply a small causal self-attention module across the three input frames’ embeddings. The resulting aggregated features are passed into the trajectory decoder. With our method (LFG), since the encoder has already been pretrained with temporal reasoning, we use the last set of future autonomy tokens directly, which provides a temporally consistent representation for the planning head to condition on.

[128] h5: Baselines and training protocol.

[129] p: We evaluate three frozen encoders: PPGeo (geometric pre-training), DINOv3 (self-supervised ViT), and Pi3 (4D self-supervised learning). Each is followed by the same causal temporal adapter and shared anchor-based planning head. Our method (LFG) uses the pretrained temporal autoregressive encoder described in the main paper (also kept frozen), along with a lightweight multi-modal trajectory decoder. All models are optimized with AdamW and a cosine learning-rate schedule, and are trained under identical data-scaling regimes using 1%, 10%, and 100% of NAVSIM training data with learning rate 1e-4 to study data efficiency.

[130] p: For DiffusionDrive, we follow the publicly released implementation (code available on GitHub) which uses three front-view cameras plus LiDAR input and their corresponding hyper parameters.

[131] figure: Table A1: Comparing PPGeo with different pretraining data-source. PPGeo ∗ indicates that the model is pretrained on the same OpenDV dataset used by LFG. Method Input 1% 10% 100% Data PPGeo 1Cam 61.5 65.6 74.6 PPGeo ∗ 1Cam 59.8 70.0 76.4 LFG (Ours) 1Cam 66.3 81.4 85.2

[132] p: For PPGeo, in Tab. 5 we use the publicly released ResNet-34 encoder from the PPGeo repository 1 1 1 https://github.com/OpenDriveLab/PPGeo pretrained with geometric self-supervision [ 30 ] . The original PPGeo encoder is pretrained using the YouTube driving video dataset introduced in the ACO project 2 2 2 https://github.com/metadriverse/ACO . To isolate the impact of pre-training data source, we evaluate a variant, PPGeo ∗ , where we replicate the same geometric pre-training procedure but restrict the pre-training corpus to exactly the data used by LFG. As shown in Tab. A1 , PPGeo ∗ slightly improves performance at higher label fractions but still under-performs LFG by a wide margin, highlighting that LFG’s 4-D temporal pre-training paradigm provides inductive biases that align more directly with downstream planning.

[133] h5: NAVSIM metrics

[134] p: The NAVSIM benchmark uses a composite score called the Predictive Driver Model Score (PDMS) to evaluate planning performance. PDMS is computed in two phases: (i) two hard-multiplier subscores No at-fault Collisions (NC) and Drivable Area Compliance (DAC) that immediately zero the scenario score if violated; (ii) a weighted average of three performance subscores Ego Progress (EP) , Time-to-Collision (TTC) , and Comfort (C) — reflecting route progress, safety margin, and motion smoothness.

[135] p: Formally,:

[136] table: PDMS = ( NC × DAC ) × 5 ​ EP + 5 ​ TTC + 2 ​ C 5 + 5 + 2 \text{PDMS}=\bigl(\text{NC}\times\text{DAC}\bigr)\times\frac{5\,\text{EP}+5\,\text{TTC}+2\,C}{5+5+2}

[137] p: Here:

[138] p: NC = 1 if no at-fault collision, = 0.5 if a collision with a static object, = 0 otherwise.

[139] p: DAC = 1 if the ego vehicle remains within the drivable area for the entire rollout, = 0 if it leaves.

[140] p: EP is the ratio of actual route progress achieved to a safe upper bound (clipped to [0,1]).

[141] p: TTC = 1 if the minimum time-to-collision along the 4s horizon exceeds a fixed threshold, else = 0.

[142] p: C = 1 if all vehicle kinematic thresholds (acceleration, jerk) remain within comfort bounds, else = 0.

[143] p: All metrics are evaluated via a non-reactive 4-second rollout in the benchmark simulator in the test set 12k samples.

[144] h2: C Segmentation Visualizations

[145] figure: RGB LFG Semantics SegFormer Semantics Frame 1 Frame 2 Frame 4 Frame 6 Figure A1 : Qualitative comparison of semantic segmentation across RGB, LFG, and SegFormer for current frames 1 and 2 (with ground-truth input) and future frames 4 and 6 . Dashed red outlines denote predicted frames with no ground-truth image input , produced solely from the model’s future tokens.

[146] p: We show segmentation visualizations on the OpenDV dataset, with sample unposed images, and the teacher SegFormer model outputs as in Fig. A5 , on a 5 5 hz scene. We find that LFG performs very competitively with its SegFormer teacher on the current frames, and future predicts the motion of the moving bus as it is about to pass the ego vehicle. LFG, however, suffers from a smoothing effect in the later frames. We posit that training LFG on more steps and the entire OpenDV dataset will improve this, as well as an edge aware point map loss to improve crispness of future frame predictions.

[147] h2: D Motion Visualizations

[148] p: We demonstrate motion visualization on the OpenDV dataset, seen in Fig A2 , with current frames to emphasize the performance trained from pseudo ground truth data, on 10 10 Hz, but we show 3 3 frames spaced apart every other frame. LFG correctly predicts the moving cars in frame from only 2D images, with a small amount of frames. Future work entails demonstrating LFG’s performance for constructing dynamic Gaussian Splats, where the motion masks can be freely obtained.

[149] figure: RGB LFG Motion Pseudo Motion Frame 1 Frame 2 Frame 3 Figure A2 : Qualitative comparison of motion predictions (LFG vs Pseudo GT motion) with corresponding RGB frames. We show results on non-future frames to demonstrate the motion map precision on a few images. The ego vehicle is moving on a road with three nearby vehicles moving.

[150] h2: E Depth Visualizations

[151] p: We show depth visualizations of LFG compared to π 3 \pi^{3} on validation images on our dataset, at a frequency of 5 5 Hz, on Fig. A3 . LFG performs comparable to π 3 \pi^{3} on the seen frames, and while sharp edges are slowly lost in the future frames, LFG is able to understand dynamic and static objects, and the relative positioning of the other vehicles over time. Future work will crispen the point maps, and more results, including on motion and semantic results, are shown at the end of the supplementary.

[152] figure: RGB LFG Depth (3 Frames) π 3 \pi^{3} Depth (All Frames) Frame 1 Frame 2 Frame 3 Frame 4 Frame 5 Frame 6 Figure A3 : Qualitative comparison of depth prediction for six frames (first three frames are blue , the future three frames are red . LFG is able to decouple static and dynamic objects as it continues along the road, and future work will improve the sharpness of the last frames’ predictions. Dashed red outlines denote predicted frames with no ground-truth image input , produced solely from the model’s future tokens.

[153] h2: F Full Point Visualizations

[154] figure: RGB LFG Semantics SegFormer Semantics Frame 1 Frame 2 Frame 4 Frame 6 Figure A4 : Additional qualitative comparison of semantic segmentation across RGB, LFG, and SegFormer for current frames 1 and 2 (with ground-truth input) and future frames 4 and 6 . Dashed red outlines denote predicted frames with no ground-truth image input , produced solely from the model’s future tokens. LFG on current frames enjoys crisper predictions even than its teacher.

[155] figure: RGB LFG Semantics SegFormer Semantics Frame 1 Frame 2 Frame 4 Frame 6 Figure A5 : Additional qualitative comparison of semantic segmentation across RGB, LFG, and SegFormer for current frames 1 and 2 (with ground-truth input) and future frames 4 and 6 . Dashed red outlines denote predicted frames with no ground-truth image input , produced solely from the model’s future tokens. LFG retains accurate predictions of cars, road, buildings, sky, traffic lights and signs, and even a person.

[156] figure: RGB LFG Motion Pseudo Motion Frame 1 Frame 2 Frame 3 Figure A6 : More qualitative comparison of motion predictions (LFG vs Pseudo) with corresponding RGB frames. In this scene, LFG predicts the moving car across the intersection, but also the close pedestrians, demonstrating that the pretrained point decoders of π 3 \pi^{3} improve the predictions.

[157] figure: RGB LFG Depth (3 Frames) π 3 \pi^{3} Depth (All Frames) Frame 1 Frame 2 Frame 3 Frame 4 Frame 5 Frame 6 Figure A7 : Qualitative comparison of depth prediction for six frames. LFG is able to decouple static and dynamic objects as it continues along the road, and future work will improve the sharpness of the last frames’ predictions. Dashed red outlines denote predicted frames with no ground-truth image input , produced solely from the model’s future tokens

[158] figure: RGB LFG Depth (3 Frames) π 3 \pi^{3} Depth (All Frames) Frame 1 Frame 2 Frame 3 Frame 4 Frame 5 Frame 6 Figure A8 : More qualitative comparison of depth prediction for six frames. Dashed red outlines denote predicted frames with no ground-truth image input , produced solely from the model’s future tokens

[159] h2: Instructions for reporting errors

[160] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[161] p: Tip: You can select the relevant text first, to include it in your report.

[162] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[163] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
