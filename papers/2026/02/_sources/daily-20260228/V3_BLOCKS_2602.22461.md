[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: EgoAVFlow: Robot Policy Learning with Active Vision from Human Egocentric Videos via 3D Flow

[3] h6: Abstract

[4] p: Egocentric human videos provide a scalable source of manipulation demonstrations; however, deploying them on robots requires active viewpoint control to maintain task-critical visibility, which human viewpoint imitation often fails to provide due to human-specific priors. We propose EgoAVFlow, which learns manipulation and active vision from egocentric videos through a shared 3D flow representation that supports geometric visibility reasoning and transfers without robot demonstrations. EgoAVFlow uses diffusion models to predict robot actions, future 3D flow, and camera trajectories, and refines viewpoints at test time with reward-maximizing denoising under a visibility-aware reward computed from predicted motion and scene geometry. Real-world experiments under actively changing viewpoints show that EgoAVFlow consistently outperforms prior human-demo-based baselines, demonstrating effective visibility maintenance and robust manipulation without robot demonstrations. Project page: https://dscho1234.github.io/egoavflow/

[5] h6: Index Terms:

[6] h2: I Introduction

[7] p: Learning robot policies from human demonstrations is an appealing alternative to large-scale robot data collection, especially as egocentric human videos provide abundant everyday manipulation behaviors [ 1 , 2 ] . These videos contain rich task intent and interaction patterns, suggesting a scalable path toward imitation and representation learning. However, directly transferring human demonstrations to robots remains challenging: the robot must not only reproduce the action, but also perform active perception to understand the scene. In real-world manipulation, robots frequently need to adjust their camera viewpoints to keep task-critical information in view [ 3 ] . Even briefly losing the object or target could cascade into execution failures. In this work, we aim to enable policies to actively choose their viewpoints instead of passively accepting camera streams.

[8] p: A seemingly straightforward solution is to imitate the human viewpoint from egocentric demonstrations. Recent works even collect demonstrations via hardware-based teleoperation interfaces that record human head motion (and sometimes gaze) and train robots to reproduce these viewpoints [ 4 , 5 , 6 ] . However, naively imitating a human viewpoint is often suboptimal for robots. Egocentric human videos are produced under strong human-specific priors that do not directly translate to robotic perception. For example, human uses frequent, rapid saccadic eye movements to gather information, which may not be optimal for a learned policy. Moreover, humans exhibit behaviors such as the vestibulo-ocular reflex [ 7 , 8 ] , where the head moves while gaze stabilizes on the object; a robot camera does not need to replicate such head motions. These factors yield training signals that may be internally consistent for humans but visually unreliable for robots. Therefore, the goal should not be to mimic human camera motion, but to learn an independent viewpoint adjustment strategy that maintains task-critical visibility while executing the task.

[9] p: However, learning an independent view policy raises a key question: what should the policy reason over to decide where to look? Visibility depends on the future 3D configuration of the manipulated object, the end-effector, and the surrounding scene geometry. Thus, planning camera motion requires a predictive representation that (i) captures task-relevant motion in 3D, (ii) is compatible with geometric visibility computation under candidate viewpoints, and (iii) is robust to view-dependent appearance, while also being (iv) embodiment-agnostic so that policies trained on human videos remain applicable when the agent’s embodiment differs at deployment. Standard 2D visual features entangle appearance with viewpoint and embodiment, providing no direct way to forecast where the object will be in 3D for visibility scoring. This representation gap is a key consideration in coupling manipulation plans with visibility-aware planning from egocentric human videos.

[10] p: To address this, we introduce a shared 3D flow representation that serves as a common interface across embodiments and across policies, supporting joint learning of manipulation and viewpoint control. It directly encodes task-relevant 3D motion of scene elements across time while discarding view-dependent appearance, making it robust to viewpoint changes and suitable for zero-shot transfer without robot demonstrations. We construct this representation by unprojecting a pixel tracker’s output into 3D flow [ 9 ] and mapping human hand pose estimates [ 10 ] to the robot end-effector space.

[11] p: Building on this representation, we propose a framework for a robot policy learning from Ego centric human videos with A ctive V ision via a 3D Flow representation ( EgoAVFlow ). EgoAVFlow consists of three 3D flow-based components: (i) a robot manipulation policy that predicts future robot actions, (ii) a flow generation model that predicts future 3D flow describing the object’s motion, and (iii) a view policy that outputs future camera viewpoints. Crucially, we define a visibility-aware reward using the predicted 3D flow, the predicted robot actions, and the environment geometry, and perform test-time reward-maximizing denoising [ 11 , 12 ] to obtain viewpoints that maximize future visibility. The diffusion prior naturally captures the human demonstrator’s head-motion distribution, while the reward-maximizing denoising allows the camera to deviate from the human viewpoint whenever visibility requires it. This yields two independently functioning capabilities: visibility-aware viewpoint adjustment and 3D-aware manipulation.

[12] p: Through real-world experiments, we evaluate EgoAVFlow under actively changing viewpoints and compare it against human-demo-based baselines. The results show that EgoAVFlow consistently outperforms prior works, demonstrating effective visibility maintenance and robust manipulation capability. In summary, the contributions of this work are:

[13] p: We propose a shared 3D flow representation that bridges the human-robot embodiment gap and unifies manipulation with viewpoint control, without robot data.

[14] p: Building on this, we introduce a viewpoint adjustment strategy that explicitly optimizes the visibility, enabling exploratory camera motions that are decoupled from the human demonstrator while maintaining visibility.

[15] p: Under such actively changing viewpoints, EgoAVFlow significantly outperforms prior human-demo-based robot learning methods, highlighting its 3D-aware perception and viewpoint-robust manipulation.

[16] figure: Fig. 1 : EgoAVFlow learns manipulation and active viewpoint control from egocentric human videos by predicting future 3D flow and optimizing camera viewpoints for visibility, yielding viewpoint-robust robot execution without robot demonstrations.

[17] h2: II Related Works

[18] p: Learning from human demonstration . Building on recent progress in computer vision and robot learning, several approaches leverage human demonstration data to acquire robotic skills. Prior works either translate human videos into robot-centric observations via generative editing [ 13 , 14 ] , infer manipulation affordances from human videos [ 15 , 16 ] , or collect paired human-robot data through co-training pipelines and hardware setups (e.g., smart glasses) [ 17 , 18 , 19 ] . Another line of work uses flow-based representations to mitigate the human-robot embodiment gap [ 20 , 21 , 22 , 23 ] . Despite this progress on transfer across human-robot embodiments, these methods typically assume a passively set camera viewpoint and do not explicitly optimize viewpoint adaptation during execution. In contrast, we use 3D flow as a shared representation that both bridges the embodiment gap and supports active viewpoint adjustment for visibility-aware manipulation.

[19] p: Active vision. To address viewpoint variations, prior robotics works often cast next-best-view (NBV) selection as an active perception problem, targeting scene reconstruction [ 24 ] , pose estimation [ 25 ] , or uncertainty reduction [ 26 ] . For robotic manipulation, some approaches leverage novel-view synthesis to scale up training data [ 27 , 28 ] , but they do not explicitly plan viewpoints during execution. Other recent works imitate human viewpoints using hardware-based robot teleoperation interfaces that track the operator’s head motion to record egocentric camera trajectories [ 5 , 4 , 29 ] , optionally leveraging gaze information [ 6 ] ; however, these methods largely assume that the human viewpoint strategy is optimal. Reinforcement learning (RL) has also been explored for viewpoint control [ 30 , 31 , 32 ] , but such approaches typically require extensive on-policy interactions, making real-world training challenging. In contrast, we adapt viewpoints online via test-time reward-maximizing diffusion denoising: the human demonstrator’s head motion provides a prior, while the camera pose is adapted to maximize visibility.

[20] h2: III Preliminary

[21] h3: III-A Data pre-processing

[22] h5: Robot data from egocentric human video

[23] p: We assume access to an egocentric human demonstration dataset 𝒟 human = { τ i } i = 1 L \mathcal{D}_{\text{human}}=\{\tau^{i}\}_{i=1}^{L} with L L video demonstrations, where each demonstration τ i \tau^{i} is a sequence of RGBD observations { I t } t = 1 T ′ \{I_{t}\}_{t=1}^{T^{\prime}} . To derive robot-equivalent proprioception and actions from human videos, we estimate 3D hand keypoints and a 6DoF wrist pose using HaMeR [ 10 ] . Following prior work that maps egocentric hand motion to a gripper-equivalent interface [ 13 ] , we construct a gripper-equivalent 6DoF pose from the hand keypoints and infer a binary gripper command (open/close). Finally, we concatenate the gripper-equivalent position, orientation (6D rotation representation [ 33 ] ), and the gripper command to form the robot proprioception p t ∈ ℝ 10 p_{t}\in\mathbb{R}^{10} , and define the robot action as the next-step target in the same representation, a t ≜ p t + 1 a_{t}\triangleq p_{t+1} .

[24] h5: Scene description via 3D flow

[25] p: To obtain motion cues over time, we track 2D pixels across frames using CoTracker3 [ 9 ] . This yields 2D pixel trajectories for N N query points, { 𝐮 t } t = 1 T ∈ ℝ N × 3 \{\mathbf{u}_{t}\}_{t=1}^{T}\in\mathbb{R}^{N\times 3} , where the first two channels correspond to image-plane coordinates ( x , y ) (x,y) and the last channel is a binary tracking indicator in { 0 , 1 } \{0,1\} . Given depth at each tracked pixel, we unproject these 2D trajectories into 3D, resulting in { 𝐅 t } t = 1 T ∈ ℝ N × 4 \{\mathbf{F}_{t}\}_{t=1}^{T}\in\mathbb{R}^{N\times 4} , where the first three elements are the 3D point tracks in the camera coordinate frame and the last element is the tracking indicator. Since egocentric videos involve a moving camera, we also estimate the camera pose SE(3), 𝐯 t \mathbf{v}_{t} , for each frame using DROID-SLAM [ 34 ] to interpret the 3D tracks and hand poses over time.

[26] h5: Marker coordinate representation

[27] p: Egocentric human videos exhibit diverse initial states, which leads SLAM to produce a different world coordinate frame for each demonstration. To express trajectories in a consistent reference frame, we convert all 3D quantities into a marker coordinate system defined by a ChArUco board. Specifically, robot actions and proprioception, 3D tracks, and camera poses are all represented in marker coordinates. For simplicity, we reuse the same notation a t a_{t} , p t p_{t} , 𝐅 t \mathbf{F}_{t} , and 𝐯 t \mathbf{v}_{t} for their marker-frame counterparts in the remainder of this work.

[28] h3: III-B Soft Value-Based Denoising for Reward Maximizing Diffusion

[29] p: A key component of our method is to refine diffusion-based predictions using a visibility-aware reward to guide the generation of future viewpoints at test time, so that samples improve reward while remaining consistent with the pre-trained diffusion prior. This subsection summarizes the core algorithmic primitive we use: soft value-based denoising. Compared to alternatives such as differentiable classifier-style guidance or RL fine-tuning, it does not require additional training and differentiable reward functions. This matches our setting, where the visibility reward is computed via geometric raycasting and must be applied at test time under changing scene reconstructions.

[30] p: Assume the denoising dynamics of a pre-trained diffusion model are specified by a sequence of Markov kernels { p k − 1 pre ( ⋅ | x k ) } k = K 1 \{p^{\mathrm{pre}}_{k-1}(\cdot|x_{k})\}_{k=K}^{1} under the standard timestep convention k = K , … , 1 k=K,\ldots,1 . Let p pre ​ ( ⋅ ) ∈ Δ ​ ( 𝒳 ) p^{\mathrm{pre}}(\cdot)\in\Delta(\mathcal{X}) denote the induced marginal distribution of the final sample x 0 x_{0} . For notational simplicity, we suppress the conditioning context c c in notation; all distributions are understood to be conditional on c c when applicable. Given an arbitrary reward function r ⁡ ( x 0 ) r(x_{0}) , our goal is to bias generation toward high-reward samples while staying close to the pre-trained distribution.

[31] h5: Reward-tilted target distribution

[32] p: We consider the entropy-regularized objective

[33] table: p ( α ) ( ⋅ ) = arg max p ∈ Δ ⁡ ( 𝒳 ) 𝔼 x ∼ p [ r ( x ) ] − α D KL ( p ∥ p pre ) , p^{(\alpha)}(\cdot)\;\;=\;\;\arg\max_{p\in\Delta(\mathcal{X})}\;\mathbb{E}_{x\sim p}[r(x)]\;-\;\alpha\,D_{\mathrm{KL}}\!\bigl(p\,\|\,p^{\mathrm{pre}}\bigr), (1)

[34] p: whose solution corresponds to the reward-tilted distribution

[35] table: p ( α ) ​ ( x ) ∝ exp ⁡ ( r ⁡ ( x ) / α ) ​ p pre ​ ( x ) . p^{(\alpha)}(x)\;\propto\;\exp\!\bigl(r(x)/\alpha\bigr)\,p^{\mathrm{pre}}(x). (2)

[36] p: Here, α > 0 \alpha>0 controls the reward-naturalness trade-off, and α → 0 \alpha\!\to\!0 yields a greedy reward maximization behavior.

[37] h5: Soft value as a look-ahead score

[38] p: Li et al. [ 11 ] introduce a soft value function v k − 1 ​ ( ⋅ ) v_{k-1}(\cdot) that measures how likely an intermediate noisy state x k − 1 x_{k-1} will lead to a high reward at the end of denoising:

[39] table: v k − 1 ( x k − 1 ) := α log 𝔼 x 0 ∼ p pre ( ⋅ ∣ x k − 1 ) [ exp ( r ( x 0 ) / α ) ] , v_{k-1}(x_{k-1})\;:=\;\alpha\log\mathbb{E}_{x_{0}\sim p^{\mathrm{pre}}(\cdot\mid x_{k-1})}\Bigl[\exp\!\bigl(r(x_{0})/\alpha\bigr)\Bigr], (3)

[40] p: where 𝔼 x 0 ∼ p pre ( ⋅ ∣ x k − 1 ) [ ⋅ ] \mathbb{E}_{x_{0}\sim p^{\mathrm{pre}}(\cdot\mid x_{k-1})}[\cdot] is a posterior-mean estimate [ 35 ] , induced by the pre-trained denoising dynamics { p k − 1 pre ( ⋅ | x k ) } k = K 1 \{p^{\mathrm{pre}}_{k-1}(\cdot|x_{k})\}_{k=K}^{1} . Intuitively, v k − 1 v_{k-1} is a one-step look-ahead score that rates intermediate states by their expected final reward under the pre-trained denoising dynamics.

[41] h5: Value-weighted denoising process

[42] p: Using v k − 1 v_{k-1} , we define a value-weighted denoising kernel

[43] table: p k − 1 ⋆ , α ( ⋅ ∣ x k ) ∝ p k − 1 pre ( ⋅ ∣ x k ) exp ( v k − 1 ( ⋅ ) / α ) , p^{\star,\alpha}_{k-1}(\cdot\mid x_{k})\;\propto\;p^{\mathrm{pre}}_{k-1}(\cdot\mid x_{k})\,\exp\!\bigl(v_{k-1}(\cdot)/\alpha\bigr), (4)

[44] p: which prefers candidates that are predicted to yield higher final reward. Sequentially sampling with { p k − 1 ⋆ , α } k = K 1 \{p^{\star,\alpha}_{k-1}\}_{k=K}^{1} induces the target distribution in Eq. ( 2 ), hence optimizing the entropy-regularized objective in Eq. ( 1 ).

[45] h5: Denoising via per-step importance resampling

[46] p: Direct sampling from Eq. ( 4 ) is intractable in general due to the normalizer. Therefore, we approximate each step by: (i) drawing M M candidates from the proposal p k − 1 pre ( ⋅ ∣ x k ) p^{\mathrm{pre}}_{k-1}(\cdot\mid x_{k}) , (ii) assigning weights w ∝ exp ⁡ ( v ^ k − 1 / α ) w\propto\exp(\hat{v}_{k-1}/\alpha) using an estimated value function v ^ \hat{v} , and (iii) selecting one candidate by categorical resampling, i.e.,

[47] table: p k − 1 ⋆ , α ( ⋅ ∣ x k ) ≈ ∑ m = 1 M w k − 1 ⟨ m ⟩ ∑ j = 1 M w k − 1 ⟨ j ⟩ δ x k − 1 ⟨ m ⟩ , { x k − 1 ⟨ m ⟩ } m = 1 M ∼ p k − 1 pre ( ⋅ ∣ x k ) , p_{k-1}^{\star,\alpha}\left(\cdot\mid x_{k}\right)\approx\sum_{m=1}^{M}\frac{w_{k-1}^{\langle m\rangle}}{\sum_{j=1}^{M}w_{k-1}^{\langle j\rangle}}\delta_{x_{k-1}^{\langle m\rangle}},\left\{x_{k-1}^{\langle m\rangle}\right\}_{m=1}^{M}\sim p_{k-1}^{\mathrm{pre}}\left(\cdot\mid x_{k}\right), (5)

[48] p: where w k − 1 ⟨ m ⟩ := exp ⁡ ( v k − 1 ​ ( x k − 1 ⟨ m ⟩ ) / α ) w_{k-1}^{\langle m\rangle}:=\exp\left(v_{k-1}\left(x_{k-1}^{\langle m\rangle}\right)/\alpha\right) and δ a \delta_{a} denote a Dirac delta distribution centered at a a . This yields an inference-time optimization that approximately samples from the value-weighted denoising process and consequently maximizes the soft value along the denoising trajectory. We denote x ^ 0 ( x k ) ≈ 𝔼 x 0 ∼ p pre ( ⋅ ∣ x k ) [ x 0 ] \hat{x}_{0}(x_{k})\approx\mathbb{E}_{x_{0}\sim p^{\mathrm{pre}}(\cdot\mid x_{k})}[x_{0}] as a posterior-mean estimate [ 35 ] , where p pre ( ⋅ ∣ x k ) p^{\mathrm{pre}}(\cdot\mid x_{k}) is the same as in Eq. ( 3 ). Then, we use r ​ ( x ^ 0 ​ ( x k ) ) r(\hat{x}_{0}(x_{k})) as an estimation for v k ​ ( x k ) v_{k}(x_{k}) without additional training. More rigorous theoretical details of value-weighted denoising can be found in [ 11 ] .

[49] h2: IV EgoAVFlow: Policy learning from egocentric human videos with active vision via a 3D flow

[50] figure: Fig. 2 : Method overview. EgoAVFlow consists of three diffusion models. The robot policy π r \pi_{r} produces future robot action sequences. The flow generation model f f predicts future 3D flows from the outputs of π r \pi_{r} . The view policy π v \pi_{v} produces future camera viewpoints from the outputs of π r \pi_{r} , f f , and reconstructed mesh surfaces through a visibility-aware reward-maximizing denoising process. Viewpoints (A) represent that most query points are invisible ( Red LOS ) due to the table’s mesh surface or out of FoV, whereas in viewpoints (B) these points are visible ( Green LOS ), yielding a higher visibility reward.

[51] h3: IV-A Overall Framework

[52] p: Our goal is to learn a manipulation policy and an independent view adjustment strategy from egocentric human videos. This setting raises two coupled challenges. First, viewpoint control cannot be trained by straightforward imitation: the recorded human camera motion is not optimized for robotic visibility. Second, deciding where to move the camera requires reasoning about future scene motion and geometric occlusions, which depend on both the robot’s planned interaction and the environment geometry.

[53] p: These considerations motivate a modular design with three components: (i) a manipulation policy that proposes future robot actions, (ii) a predictive 3D flow representation that enables visibility reasoning under candidate viewpoints, and (iii) a view policy that provides a strong prior over plausible camera motions while allowing test-time optimization under a visibility-aware reward.

[54] p: We implement all three components with diffusion models by using preprocessed data in Section III . For these three models, we adopt a diffusion transformer-based backbone [ 36 ] that injects condition tokens via cross-attention, train these models using a standard DDPM [ 37 ] framework, and obtain samples using DDIM [ 35 ] . We set the prediction horizon T = 24 T=24 for all three models, and iteratively sample action chunks for every H = 12 H=12 steps, using the first 12 elements from the action chunks. Fig. 2 shows an overview of the proposed framework.

[55] h5: Robot policy π r \pi_{r}

[56] p: The robot policy π r \pi_{r} is trained to output robot action chunks a ^ t + 1 : t + T \hat{a}_{t+1:t+T} from the 3D flow tracking history 𝐅 t − h : t \mathbf{F}_{t-h:t} , proprioception history p t − h : t p_{t-h:t} , where h h is history length.

[57] h5: Future flow generation model f f

[58] p: The flow generation model f f is trained to predict future 3D flows 𝐅 ^ t + 1 : t + T ∈ ℝ N × T × 4 \hat{\mathbf{F}}_{t+1:t+T}\in\mathbb{R}^{N\times T\times 4} . It takes as input the same context as π r \pi_{r} , and is additionally conditioned on the viewpoint history 𝐯 t − h : t \mathbf{v}_{t-h:t} and the future robot action sequence a ^ t + 1 : t + T \hat{a}_{t+1:t+T} predicted by π r \pi_{r} . This is because future 3D flow depends on both camera motion and robot motion. This model captures how the robot’s planned interaction (via a ^ t + 1 : t + T \hat{a}_{t+1:t+T} ) induces future scene changes, providing a compact intermediate representation for “what will move where”. These predicted future flows 𝐅 ^ t + 1 : t + T \hat{\mathbf{F}}_{t+1:t+T} are used as query points for visibility computation in Section IV-B .

[59] h5: View policy π v \pi_{v}

[60] p: The view policy π v \pi_{v} is trained to predict future camera viewpoints 𝐯 ^ t + 1 : t + T \hat{\mathbf{v}}_{t+1:t+T} . It takes as input the same context as f f , except for the proprioception history. At inference time, we do not simply sample 𝐯 ^ t + 1 : t + T \hat{\mathbf{v}}_{t+1:t+T} from π v \pi_{v} ; instead, we apply soft value-based denoising to bias generation toward viewpoints that are optimal under the visibility-aware reward in Section IV-B . The overall algorithm is summarized in Algorithm 1 .

[61] h3: IV-B View Selection via Visibility-Aware Reward

[62] p: We formulate view selection as choosing a future camera trajectory 𝐯 ^ t + 1 : t + T \hat{\mathbf{v}}_{t+1:t+T} that keeps task-relevant scene elements observable during the robot’s planned interaction. Scoring candidate views requires predicting future 3D configurations and checking occlusions / FoV via mesh raycasting, which yields a non-differentiable objective. Therefore, we treat π v \pi_{v} as a learned prior over plausible camera motions and refine its samples at inference time using a visibility-aware reward through reward-guided denoising (Sec. III-B ). This preserves the diffusion prior while allowing deviations when visibility demands it.

[63] p: Our reward prioritizes the visibility of query points defined from predicted future 3D flows: { 𝐪 t , i ∈ ℝ 3 } t = t + 1 : t + T i = 1 : N \{\mathbf{q}_{t,i}\in\mathbb{R}^{3}\}_{t=t+1:t+T}^{i=1:N} are obtained by dropping the indicator channel of 𝐅 ^ t + 1 : t + T \hat{\mathbf{F}}_{t+1:t+T} . We evaluate visibility by raycasting from candidate camera poses to { 𝐪 t , i } \{\mathbf{q}_{t,i}\} against the union of an environment mesh ℳ e \mathcal{M}^{e} (reconstructed up to time t t with Nvblox [ 38 ] ) and a time-varying robot mesh ℳ t r \mathcal{M}^{r}_{t} (constructed from a ^ t + 1 : t + T \hat{a}_{t+1:t+T} via inverse kinematics). The resulting visibility term defines R vis R_{\mathrm{vis}} , which forms the core of our reward; we then augment it with auxiliary terms for stability and safety.

[64] h4: IV-B 1 Visibility reward

[65] p: In this work, we define visibility as the conjunction of (a) whether there exist any obstacles between the camera origin and query points, and (b) whether the query point is within the field-of-view (FoV) of the camera. For (a), we define the line-of-sight (LOS) segment from the camera center for each query point 𝐪 t , i \mathbf{q}_{t,i} :

[66] table: ℓ t , i = { 𝐯 t , pos + λ ⁡ ( 𝐪 t , i − 𝐯 t , pos ) | λ ∈ [ 0 , 1 ] } , \ell_{t,i}\;=\;\left\{\mathbf{v}_{t,\mathrm{pos}}+\lambda(\mathbf{q}_{t,i}-\mathbf{v}_{t,\mathrm{pos}})\;\middle|\;\lambda\in[0,1]\right\}, (6)

[67] p: where 𝐯 t , pos ∈ ℝ 3 \mathbf{v}_{t,\mathrm{pos}}\in\mathbb{R}^{3} is the position component from the camera pose prediction 𝐯 ^ t \hat{\mathbf{v}}_{t} . Then, we define an unobstructed-LOS indicator using mesh intersection:

[68] table: s t , i = 𝕀 [ ℓ t , i ∩ ℳ t = ∅ ] , ℳ t = ℳ e ∪ ℳ t r , s_{t,i}\;=\;\mathbb{I}\!\left[\ell_{t,i}\cap\mathcal{M}_{t}=\emptyset\right],\quad\mathcal{M}_{t}=\mathcal{M}^{e}\cup\mathcal{M}^{r}_{t}, (7)

[69] p: where mesh intersection is computed by raycasting. Intuitively, s t , i = 1 s_{t,i}=1 indicates there is nothing between the camera and the query point, while s t , i = 0 s_{t,i}=0 indicates the query point is occluded by the mesh surfaces. For (b), we project the query point to the image plane using the camera projection Π t ​ ( ⋅ ) \Pi_{t}(\cdot) :

[70] table: ( u t , i , v t , i ) = Π t ​ ( 𝐪 t , i ) , (u_{t,i},v_{t,i})\;=\;\Pi_{t}(\mathbf{q}_{t,i}), (8)

[71] p: where ( u t , i , v t , i ) (u_{t,i},v_{t,i}) are pixel coordinates and the image size is W i ​ m ​ g × H i ​ m ​ g W_{img}\times H_{img} . We define an in-FoV indicator:

[72] table: f t , i = 𝕀 [ 0 ≤ u t , i < W i ​ m ​ g ∧ 0 ≤ v t , i < H i ​ m ​ g ] . f_{t,i}\;=\;\mathbb{I}\!\left[0\leq u_{t,i}<W_{img}\;\wedge\;0\leq v_{t,i}<H_{img}\right]. (9)

[73] p: The binary visibility reward for point 𝐪 t , i \mathbf{q}_{t,i} is the conjunction, and we average over time and query points:

[74] table: R vis = 1 T ​ N ​ ∑ t = t + 1 t + T ∑ i = 1 N r t , i vis , r t , i vis = s t , i ​ f t , i . R_{\mathrm{vis}}\;=\;\frac{1}{TN}\sum_{t=t+1}^{t+T}\sum_{i=1}^{N}r^{\mathrm{vis}}_{t,i},\quad r^{\mathrm{vis}}_{t,i}=s_{t,i}f_{t,i}. (10)

[75] p: A visual illustration of computing R vis R_{\mathrm{vis}} is shown in Fig. 2 .

[76] figure: Algorithm 1 EgoAVFlow 1: Require: π r \pi_{r} , π v \pi_{v} , f f , robot_env, view_env, t ← 0 t\!\leftarrow\!0 , chunk size H ( ≤ T ) H(\leq T) , horizon T T , environment mesh ℳ e \mathcal{M}^{e} 2: while not done do 3: if t mod H = 0 t\bmod H=0 then 4: a ^ t + 1 : t + T ∼ π r ( ⋅ | p t − h : t , 𝐅 t − h : t ) \hat{a}_{t+1:t+T}\sim\pi_{r}(\cdot|p_{t-h:t},\mathbf{F}_{t-h:t}) 5: 𝐅 ^ t + 1 : t + T ∼ f ( ⋅ | p t − h : t , 𝐅 t − h : t , 𝐯 t − h : t , a ^ t + 1 : t + T ) \hat{\mathbf{F}}_{t+1:t+T}\sim f(\cdot|p_{t-h:t},\mathbf{F}_{t-h:t},\mathbf{v}_{t-h:t},\hat{a}_{t+1:t+T}) 6: 𝐯 ^ t + 1 : t + T ∼ \hat{\mathbf{v}}_{t+1:t+T}\sim RewMaxDiff ( π v , 𝐅 ^ t + 1 : t + T , a ^ t + 1 : t + T , ℳ e ) (\pi_{v},\hat{\mathbf{F}}_{t+1:t+T},\hat{a}_{t+1:t+T},\mathcal{M}^{e}) . 7: Get p t + 1 : t + H p_{t+1:t+H} , 𝐯 t + 1 : t + H \mathbf{v}_{t+1:t+H} , 𝐅 t + 1 : t + H \mathbf{F}_{t+1:t+H} from robot_env.step( a ^ t + 1 : t + H \hat{a}_{t+1:t+H} ), view_env.step( 𝐯 ^ t + 1 : t + H \hat{\mathbf{v}}_{t+1:t+H} ) 8: t ← t + H t\leftarrow t+H 9: end if 10: end while 11: Func RewMaxDiff ( p pre ( ⋅ ) , 𝐅 ^ t + 1 : t + T , a ^ t + 1 : t + T , ℳ e ) \bigl(p^{\mathrm{pre}}(\cdot),\hat{\mathbf{F}}_{t+1:t+T},\hat{a}_{t+1:t+T},\mathcal{M}^{e}\big) : 12: for k = K , … , 1 k=K,\ldots,1 do 13: Sample { x k − 1 ( i ) } i = 1 M ∼ p k − 1 pre ( ⋅ ∣ x k ) \{x_{k-1}^{(i)}\}_{i=1}^{M}\sim p^{\mathrm{pre}}_{k-1}(\cdot\mid x_{k}) 14: for i = 1 , … , M i=1,\ldots,M do 15: v k − 1 ( i ) ← R ( x ^ 0 ( x k − 1 ( i ) ) , 𝐅 ^ t + 1 : t + T , a ^ t + 1 : t + T , ℳ e ) v_{k-1}^{(i)}\leftarrow R\!\Big(\hat{x}_{0}(x_{k-1}^{(i)}),\hat{\mathbf{F}}_{t+1:t+T},\hat{a}_{t+1:t+T},\mathcal{M}^{e}\Big) (Eq. ( 14 )) 16: w k − 1 ( i ) ← exp ⁡ ( v k − 1 ( i ) / α ) w_{k-1}^{(i)}\leftarrow\exp\!\big(v_{k-1}^{(i)}/\alpha\big) 17: end for 18: x k − 1 ← x k − 1 ( i ⋆ ) x_{k-1}\leftarrow x_{k-1}^{(i^{\star})} , where i ⋆ ∼ Cat ⁡ ( w k − 1 ( i ) ∑ j = 1 M w k − 1 ( j ) ) i^{\star}\sim\mathrm{Cat}\Bigl(\dfrac{w_{k-1}^{(i)}}{\sum_{j=1}^{M}w_{k-1}^{(j)}}\Bigr) 19: end for 20: Output: x 0 x_{0} 21: End Func

[77] h4: IV-B 2 Auxiliary reward terms

[78] p: Since r t , i vis r^{\mathrm{vis}}_{t,i} is binary, it lacks a continuous objective that reflects the quality of the current viewpoint and provides an informative optimization signal. In addition, multiple viewpoints can satisfy full visibility. Thus, we additionally add a weighted sum of the following auxiliary terms:

[79] h5: Close to query points

[80] p: We prefer camera positions not excessively far from the query points:

[81] table: R close = 1 T ​ N ​ ∑ t = t + 1 t + T ∑ i = 1 N exp ⁡ ( − ‖ 𝐯 t , pos − 𝐪 t , i ‖ 2 ) . R_{\mathrm{close}}=\frac{1}{TN}\sum_{t=t+1}^{t+T}\sum_{i=1}^{N}\exp{(-\left\lVert\mathbf{v}_{t,\mathrm{pos}}-\mathbf{q}_{t,i}\right\rVert_{2})}. (11)

[82] h5: Camera margin

[83] p: To discourage viewpoints where query points are only barely visible and instead favor views that keep them visible under small pose perturbations, we generate J J perturbed viewpoints { 𝐯 ~ t ( j ) } j = 1 J \{\tilde{\mathbf{v}}_{t}^{(j)}\}_{j=1}^{J} from 𝐯 t \mathbf{v}_{t} by adding Gaussian noise to translation and rotation, i.e., 𝐯 ~ t , pos ( j ) = 𝐯 t , pos + ϵ pos ( j ) \tilde{\mathbf{v}}_{t,\mathrm{pos}}^{(j)}=\mathbf{v}_{t,\mathrm{pos}}+\epsilon_{\mathrm{pos}}^{(j)} with ϵ pos ( j ) ∼ 𝒩 ⁡ ( 𝟎 , σ pos 2 ​ 𝐈 ) \epsilon_{\mathrm{pos}}^{(j)}\sim\mathcal{N}(\mathbf{0},\sigma_{\mathrm{pos}}^{2}\mathbf{I}) and σ pos = 0.02 ​ m \sigma_{\mathrm{pos}}=0.02\,\mathrm{m} , and similarly for rotation with σ rot = 0.05 ​ rad \sigma_{\mathrm{rot}}=0.05\,\mathrm{rad} . For each perturbation, we compute R vis ( j ) R_{\mathrm{vis}}^{(j)} (Eq. ( 10 )) and define

[84] table: R marg = min j ∈ { 1 , … , J } ⁡ R vis ( j ) ⋅ ( 1 − λ var ⋅ Var ⁡ ( { R vis ( j ) } j = 1 J ) ) , R_{\mathrm{marg}}=\min_{j\in\{1,\dots,J\}}R_{\mathrm{vis}}^{(j)}\;\cdot\;\Bigl(1-\lambda_{\mathrm{var}}\cdot\mathrm{Var}(\{R_{\mathrm{vis}}^{(j)}\}_{j=1}^{J})\Bigr), (12)

[85] p: where λ var = 0.1 \lambda_{\mathrm{var}}=0.1 .

[86] h5: Safety

[87] p: To penalize camera viewpoints that are too close to the robot end effector, we define a safety reward R safe R_{\mathrm{safe}} based on the distance between the predicted camera position 𝐯 t , pos \mathbf{v}_{t,\mathrm{pos}} and the predicted end-effector position a ^ t \hat{a}_{t} at each horizon step:

[88] table: R safe = − 1 T ∑ t = t + 1 t + T exp ( − ‖ 𝐯 t , pos − a ^ t ‖ 2 σ safe ) , σ safe = 0.1 m , R_{\mathrm{safe}}=-\frac{1}{T}\sum_{t=t+1}^{t+T}\exp\!\left(-\frac{\|\mathbf{v}_{t,\mathrm{pos}}-\hat{a}_{t}\|_{2}}{\sigma_{\mathrm{safe}}}\right),\quad\sigma_{\mathrm{safe}}=0.1\,\mathrm{m}, (13)

[89] p: where σ safe = 0.1 ​ m \sigma_{\mathrm{safe}}=0.1\,\mathrm{m} . Then, the following reward composition is used for the RewMaxDiff function in Algorithm 1 :

[90] table: R ( 𝐯 ^ t + 1 : t + T , 𝐅 ^ t + 1 : t + T , a ^ t + 1 : t + T , ℳ e ) \displaystyle R(\hat{\mathbf{v}}_{t+1:t+T},\hat{\mathbf{F}}_{t+1:t+T},\hat{a}_{t+1:t+T},\mathcal{M}^{e}) ≜ \displaystyle\triangleq (14) R vis + λ c ​ R close + λ m ​ R marg \displaystyle R_{\mathrm{vis}}+\lambda_{\mathrm{c}}R_{\mathrm{close}}+\lambda_{\mathrm{m}}R_{\mathrm{marg}} + λ s ​ R safe , \displaystyle+\lambda_{\mathrm{s}}R_{\mathrm{safe}},

[91] p: where λ c , λ m , λ s \lambda_{\mathrm{c}},\lambda_{\mathrm{m}},\lambda_{\mathrm{s}} are scalar weighting coefficients.

[92] h2: V Experiments

[93] p: In this section, we evaluate EgoAVFlow against baselines to support three findings: (i) fixed viewpoints cannot reliably maintain visibility during manipulation, (ii) directly imitating human viewpoints is insufficient for visibility-aware viewpoint adjustments, and (iii) conditioning policies on 3D flow yields the strongest performance under actively varying viewpoints.

[94] p: As an evaluation benchmark, we set up 4 tasks (Fig. 3 ), where the camera viewpoint should be adjusted during rollout to maintain a fully visible status. For the dataset, we collect 150 egocentric human videos for each task by using a head-mounted RealSense D435, RGBD camera. For the query points, we annotate six points ( N = 6 N=6 ) on the object and goal location, such as a basket, though the method is agnostic to the number of points and scales naturally. For hardware setup, we use the Trossen WidowX robot for manipulation (robot_env), and the Unitree Z1 robot with a D435 camera mount for viewpoint adjustment (view_env). Since the outputs of π r \pi_{r} and π v \pi_{v} are each robot’s end-effector pose, we solve inverse kinematics to compute the target joint positions and control both robots at 4Hz to reach the target joints.

[95] h3: V-A Continuous viewpoint adjustment is necessary for reliable visibility

[96] p: For an intuitive understanding of the necessity of viewpoint adjustment, we set up four fixed cameras for the spray task ( Fig. 4 -(a) ) and computed the visibility for all timesteps in a demonstration video. Denoting k v , t = number of visible query points at view ​ v ​ and time ​ t total number of query points k_{v,t}=\frac{\text{number of visible query points at view }v\text{ and time }t}{\text{total number of query points}} , we compute a coverage, C v = 1 T ∑ t = 1 T 𝟏 [ k v , t ≥ 0.7 ] C_{v}=\frac{1}{T}\sum_{t=1}^{T}\mathbf{1}[k_{v,t}\geq 0.7] . Then, we sort the view indices in descending order based on the coverage (Fig. 4 -(b)) , and represent high k v , t k_{v,t} as yellow color, and low k v , t k_{v,t} as dark-green color (Fig. 4 -(c)) .

[97] p: The figure shows that, despite nearly similar coverage among the viewpoints, no viewpoint can maintain full visibility during the rollout, and the best visible viewpoint also keeps changing (e.g., view index 0 → 1 → 2 → 3 0\rightarrow 1\rightarrow 2\rightarrow 3 ). It is further elaborated in the upper right figure (Fig. 4 -(d)) , which represents that even a fixed view with the highest coverage ( dark-green line ) cannot provide the best visibility ( yellow line ) during the episode rollout. This indicates that in most cases, the camera viewpoint should be adjusted to provide informative scene observations to the robot manipulation policy.

[98] figure: Fig. 3 : Tasks. Each task requires appropriate viewpoint adjustments. Otherwise, the object is occluded by the robot or elements in the environment, such as a table or drawer.

[99] h3: V-B Visibility-aware viewpoint planning outperforms human viewpoint imitation

[100] p: If the viewpoint adjustment is required, the next question is which viewpoints to follow. More specifically, we validate the recent approach of imitating human viewpoints [ 4 , 5 ] . Because both of these prior works utilize a robot teleoperation setting with a head-mounted VR device, they directly imitate the camera-mounted robot’s joint angle or the end-effector’s pose from image inputs. However, we do not have access to such information since we only have access to the egocentric human video. Therefore, the conditional diffusion model π v \pi_{v} without the soft value-based denoising process is used as an implementation for the viewpoint imitation baseline, since it is analogous to the direct imitation of the camera viewpoints from corresponding inputs, and conceptually the same as the prior works. To isolate the effect of viewpoint imitation, we use the same manipulation policy as our method (i.e., π r \pi_{r} ). We refer to it as a Human Viewpoint Imitation ( HVI ) .

[101] p: For comparison, we evaluate EgoAVFlow and HVI over 25 trials per task and report the success rates. A rollout is considered successful if the robot manipulates the target object as desired and the object remains visible throughout the episode. If the object drifts out of FoV, we treat this trial as a failure.

[102] p: As shown in Table I , EgoAVFlow outperforms HVI in terms of success rates. Qualitatively, as shown in Fig. 6 , EgoAVFlow maintains reliable visibility of the query points during rollout. These results are consistent with the quantitative visibility analysis in Fig. 5 . For all tasks, EgoAVFlow achieves a higher visibility reward R v ​ i ​ s R_{vis} , which is consistent with the observed success rates, suggesting that maintaining visibility is important for task completion. All of these results are attributed to the proposed visibility-maximizing diffusion for viewpoint planning.

[103] p: On the contrary, HVI often fails as it tries to imitate the human viewpoints that do not consider occlusion, or near/outside the FoV, or produce weird values when faced with out-of-distribution viewpoint inputs, attributed to the inherent embodiment gap between humans’ heads and robots’ workspace limit. This demonstrates that it is crucial to have a capability that can actively adjust viewpoints for our preferences, rather than closely following the viewpoints in the dataset.

[104] figure: Fig. 4 : Visibility comparison (best viewed in the digital version). The visibility is computed from each different fixed viewpoint. No single viewpoint can maintain full visibility throughout the execution, indicating that the viewpoint must be continuously adjusted online to maximize visibility.

[105] figure: Fig. 5 : Visibility reward. For all tasks, EgoAVFlow achieves higher average visibility rewards R v ​ i ​ s R_{vis} than HVI , demonstrating our method’s visibility maintenance capability. The error bars represent 1 standard error.

[106] h3: V-C 3D flow policy outperforms under actively varying viewpoints

[107] p: Now, given the non-human-imitating viewpoint adjustment strategy, we next ask which representation is effective for the robot policy’s robust capability under such actively varying viewpoints, while using only human data. For this question, we compare our method with the following representative robot policy learning methods, designed to leverage human data. AMPLIFY [ 21 ] : A 2D flow-based method that quantizes 2D flow tracking into a sequence of discrete codebooks, and learn a policy conditioned on these codebooks and an image input. EgoZero [ 23 ] : A 3D flow-based method, similarly designed to our method. However, it depends on the triangulation under a static-object assumption to compute 3D flow, which can fail when the object is not static. Phantom [ 13 ] : A method that removes humans from egocentric videos via diffusion-based inpainting and overlays a robot onto the resulting frames, enabling policy training on synthesized robot observations.

[108] p: All baselines are trained on the same dataset as our method, and no real robot data is used. As AMPLIFY’s policy also requires an image input, we provide it with the same synthesized robot image data used by Phantom. To isolate the effect of the policy representation, we use the same viewpoint adjustment module for all methods: our view policy π v \pi_{v} with visibility-maximizing denoising.

[109] p: We evaluate the success rates using the same criteria as in Section V-B , and the results are reported in Table I . EgoAVFlow shows superior capability compared to baselines. Across all tasks, this corresponds to a 1.8-2.5 × \times improvement over the second-best baseline. As the viewpoint keeps changing during the evaluation by our proposed view policy, the results demonstrate that the proposed 3D flow-based policy is view-invariant and benefits from its inherent 3D representation, yielding a viewpoint-robust manipulation capability.

[110] figure: Fig. 6 : Qualitative comparison. Due to the visibility-maximizing viewpoint adjustments, EgoAVFlow maintains visibility of the query points and their predicted future flows, whereas HVI fails to keep them in view, causing the query points to move out of the FoV. All experimental figures and videos in Section V are best viewed in the supplementary video.

[111] figure: Method Spray Doll Toilet Paper Towel V-B HVI 5/25 10/25 7/25 5/25 V-C AMPLIFY 4/25 6/25 9/25 9/25 EgoZero 10/25 7/25 7/25 9/25 Phantom 5/25 7/25 6/25 8/25 EgoAVFlow 20/25 18/25 17/25 18/25 ( × 2.0 \times\,2.0 ) ( × 2.5 \times\,2.5 ) ( × 1.8 \times\,1.8 ) ( × 2.0 \times\,2.0 ) TABLE I : Success rates of EgoAVFlow, HVI (Human Viewpoint Imitation), and robot policy learning baselines. All methods are trained on the same egocentric human video dataset (no robot data). Relative improvements compared to the second-best robot policy learning baseline are shown in parentheses .

[112] h3: V-D Failure analysis

[113] figure: Fig. 7 : Failure analysis. Top: Method-wise composition of failures for each category. Bottom: Example frames of a grasping failure. The breakdown suggests that manipulation-related failures in robot policy baselines are driven by a mismatch between their learned representations/assumptions, whereas human viewpoint imitation fails primarily due to the lack of visibility-aware viewpoint optimization.

[114] p: We analyze failure cases to better understand the experiments for Section V-B , V-C . Specifically, we report the per-category breakdown of failures across methods, with the categories ordered chronologically. Grasping failure : The robot fails to grasp the object in the initial phase. Out-of-viewpoint : The robot succeeds in grasping, but the pixel tracker’s tracking is lost, or the viewpoint is adjusted toward the wrong direction due to the inaccurate future flow prediction 𝐅 ^ \hat{\mathbf{F}} . Object pose failure : Grasping and tracking succeed, but the robot fails to place the object in the demonstrated pose.

[115] p: The results are shown in Fig. 7 . Since AMPLIFY and Phantom are not inherently 3D-aware, they suffer from distribution shifts when evaluated under the unseen viewpoints. EgoZero uses 3D points, but it cannot address the non-static scene, such as when the object moves due to the gripper’s contact. As a result, these three robot policy baselines account for most manipulation-related failures: AMPLIFY, EgoZero, and Phantom together constitute 91.6% in grasping failure, 81.3% in object pose failure, and EgoAVFlow constitutes the smallest share, indicating stronger robustness in manipulation under actively varying viewpoints.

[116] p: In the case of out-of-viewpoint, HVI accounts for more than 50% of the failures because it does not use our proposed view policy for visibility maintenance. EgoAVFlow accounts for the second-largest share of the failures. However, this does not indicate worse performance; rather, many robot policy baseline rollouts are already counted as early grasping failures and thus do not reach the later stages. If they progressed further, their proportions would be more comparable to our method.

[117] h2: VI Conclusion

[118] p: In this work, we introduced a shared 3D flow-based representation that enables (i) joint control of the robot and camera viewpoint and (ii) mitigation of the human-robot embodiment gap when training solely from human data. We propose a visibility-maximizing robot manipulation pipeline, which consists of a 3D flow-based robot policy, a future 3D flow generation model, and a viewpoint adjustment policy. Across experiments, we demonstrate that EgoAVFlow outperforms prior works that try to follow the human’s viewpoint in the dataset and achieves superior manipulation performance under actively varying viewpoints, driven by visibility maximization. Despite these gains, the current formulation assumes that the tracking points are observable at the initial timestep. In other words, our method does not address searching or reasoning about which points-of-interest should be tracked. Incorporating this capability is a promising direction for future work toward more autonomous robot manipulation.

[119] h2: References

[120] h2: Instructions for reporting errors

[121] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[122] p: Tip: You can select the relevant text first, to include it in your report.

[123] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[124] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
