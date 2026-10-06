[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: DexRepNet++: Learning Dexterous Robotic Manipulation with Geometric and Spatial Hand-Object Representations

[3] h6: Abstract

[4] p: Robotic dexterous manipulation is a challenging problem due to high degrees of freedom (DoFs) and complex contacts of multi-fingered robotic hands. Many existing deep reinforcement learning (DRL) based methods aim at improving sample efficiency in high-dimensional output action spaces. However, existing works often overlook the role of representations in achieving generalization of a manipulation policy in the complex input space during the hand-object interaction. In this paper, we propose DexRep, a novel hand-object interaction representation to capture object surface features and spatial relations between hands and objects for dexterous manipulation skill learning. Based on DexRep, policies are learned for three dexterous manipulation tasks, i.e. grasping, in-hand reorientation, bimanual handover, and extensive experiments are conducted to verify the effectiveness. In simulation, for grasping, the policy learned with 40 objects achieves a success rate of 87.9% on more than 5000 unseen objects of diverse categories, significantly surpassing existing work trained with thousands of objects; for the in-hand reorientation and handover tasks, the policies also boost the success rates and other metrics of existing hand-object representations by 20% to 40%. The grasp policies with DexRep are deployed to the real world under multi-camera and single-camera setups and demonstrate a small sim-to-real gap.

[5] h6: Index Terms:

[6] figure: Figure 1 : Policies learned with our hand-object representation perform grasping, in-hand reorientation, and handover tasks with five-fingered dexterous robotic hands.

[7] h2: I Introduction

[8] p: Dexterous manipulation is a fundamental capability for enabling robots to perform complex, human-level tasks in unstructured environments. Compared to parallel grippers, anthropomorphic multi-fingered hands provide superior flexibility and control, making them particularly well-suited for handling diverse objects.

[9] p: Recent progress [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 ] has highlighted the potential of reinforcement learning (RL) for acquiring dexterous manipulation skills with multi-fingered hands. However, two major challenges continue to limit the generalization and scalability of existing methods: (i) the high dimensionality of the control space, and (ii) the complex, highly variable nature of hand-object interactions. Dexterous hands typically have 16-24 degrees of freedom (DoFs) [ 12 , 13 , 14 ] , resulting in a large continuous action space that makes policy learning inefficient and unstable. In parallel, the interaction dynamics between articulated fingers and objects with diverse geometries lead to variable and sensitive contact patterns, where even slight changes in object shape or orientation can require dramatically different hand configurations.

[10] p: To address these difficulties, prior efforts have employed imitation learning [ 1 , 2 , 5 ] and curriculum-based strategies [ 6 , 8 ] to improve sample efficiency and training robustness. While these methods have achieved notable performance gains by scaling demonstrations or shaping learning progressions, they often overlook a more fundamental question: how hand-object interaction should be encoded to facilitate generalizable skill learning. Common representations include encoding object geometry via pretrained point-based networks (e.g., PointNet [ 15 ] ) and describing hand-object relations using absolute positions, joint angles, or relative distances. However, such representations are often tightly coupled to specific object instances and hand configurations, leading to poor generalization across novel objects or tasks.

[11] p: Meanwhile, insights from grasp taxonomies [ 16 ] and human motor control [ 17 ] suggest that hand-object interactions, despite their apparent complexity, often lie on low-dimensional manifolds. For instance, grasps can be clustered into a finite set of discrete types, and finger motions often follow coordinated synergies. These observations point toward the possibility of achieving better generalization by leveraging more structured and compact representations.

[12] p: Motivated by these insights, we argue that the key to enabling generalizable dexterous manipulation lies not in increasing the scale of demonstrations or task engineering, but in rethinking the representation of hand-object interaction itself. Specifically, we propose to move beyond global shape encodings and instead develop a representation grounded in local surface geometry and spatial proximity between the hand and object. The underlying intuition is that many objects share common local structures (e.g., handles, lips, edges), and similar manipulation strategies can often be applied based on local geometry, regardless of the object’s global shape. Coarse global features may suffice for approach and pre-shaping of grasp, whereas local geometric cues are essential for contact-rich actions such as grasp closure or in-hand adjustment. This motivates a hybrid representation that encodes both global structure and local detail in a unified framework.

[13] p: Based on this motivation, we introduce DexRep , a structured representation of hand-object interaction that encodes both spatial and geometric cues relative to the robot hand. DexRep comprises three components: (1) Occupancy Feature: a voxelized representation of the object surface captured from the hand’s local frame; (2) Surface Feature: a set of distances and surface normals between hand keypoints and their nearest points on the object; (3) Local-Geo Feature: fine-grained geometric descriptors extracted from surface regions near potential contact areas using a pretrained PointNet [ 15 ] to extend the surface normals in Surface Feature for more abundant local information. The Occupancy feature captures global shape information seen by the approaching hands via a coarse occupancy volume instead of static point clouds carrying detailed geometry and the Surface Feature and Local-Geo Feature capture fine-grained local geometry: the combination of the coarse global and finer local features fully captures object surface information and also ensures generalization to unseen objects that share partial geometric similarities with the training set. Surface Feature and Local-Geo Feature capture the dynamics of the interaction and the geometry feature of the most related object surface area for each hand part in potential contacts.

[14] p: We evaluate DexRep on three manipulation tasks of increasing complexity: (1) object grasping, (2) in-hand reorientation, and (3) bimanual handover. These tasks cover both single- and dual-hand settings, and involve different requirements in terms of spatial precision, contact adaptation, and coordination. Furthermore, we show that DexRep remains effective when computed from partial observations (e.g., single-view depth input), making it practical for real-world deployment without requiring full object observations.

[15] p: Our empirical results demonstrate the following key advantages: (1) Strong Generalization: A grasping policy trained on only 40 objects generalizes to over 5,000 unseen shapes with an average success rate of nearly 88%. (2) Multi-task Adaptability: Despite being task-agnostic, DexRep achieves superior performance across multiple manipulation tasks—including grasping, in-hand reorientation, and handover—outperforming task-specific baselines. (3) Morphological Transferability: The same representation supports different robotic hands, including 2-, 3-, 4-, and 5-finger configurations. (4) Robust Real-world Deployment: Our system achieves up to 85% grasping success using multi-view input, and over 75% using only partial observations. (5) Small Sim-to-real Gap: Simulation-trained policies transfer to hardware with less than 5% drop in performance.

[16] p: This paper extends our prior conference work [ 18 ] in several key directions:

[17] p: Expanded Task Coverage: We introduce new evaluations on in-hand manipulation and dual-arm handover, showcasing the versatility of DexRep.

[18] p: Robustness to Partial Observations: We demonstrate successful deployment with only single-view depth input, increasing practical applicability.

[19] p: Comprehensive Analysis: We conduct detailed ablations on feature types, voxel resolution, and training object diversity, offering insights into design trade-offs.

[20] p: Improved Baseline Comparison: We scale up evaluations with stronger baselines, including UniDexGrasp++ [ 8 ] , and larger object sets.

[21] p: Real-world Implementation: We build a full real-world system combining Allegro Hand, Unitree Z1 arm, and Azure Kinect, and validate performance under practical conditions.

[22] p: In summary, we propose DexRep , a compact, structured representation of hand-object interaction that supports robust and generalizable learning for dexterous manipulation. DexRep integrates global and local geometry, adapts to different hands and observations, and facilitates sim-to-real deployment. We believe this representation offers a promising foundation for advancing general-purpose manipulation in complex, real-world environments.

[23] h2: II Related Work

[24] h3: II-A Dexterous Grasping and Manipulation

[25] p: Dexterous grasping and manipulation are core tasks for multi-fingered robotic hands. Grasping aims to establish a stable initial contact with the object, while manipulation extends this capability to dynamic control for object repositioning, reorientation, or handover. Despite their differences in execution, both tasks face shared challenges, including high-dimensional control, complex contact dynamics, and the need for generalization across diverse object geometries.

[26] p: Early research approached these problems from a planning perspective, relying on precise models of hand kinematics and object dynamics [ 19 , 20 , 21 , 22 ] . However, such methods are typically constrained by their reliance on accurate geometric and physical modeling, which limits their applicability in unstructured or dynamic environments.

[27] p: Recent advances have shifted toward learning-based approaches, especially reinforcement learning (RL) and imitation learning (IL), to bypass explicit modeling. In grasping, methods like DAPG [ 1 ] and ILAD [ 2 ] leverage expert demonstrations to improve sample efficiency and stabilize training. GRAFF [ 23 ] and DexVIP [ 5 ] introduce affordance priors from human demonstrations to guide learning, while Christen et al. [ 24 ] generate grasp trajectories from static visual inputs. UniDexGrasp [ 6 ] and UniDexGrasp++ [ 8 ] further extend these ideas by incorporating diverse grasp configurations and curriculum learning strategies to enhance generalization.

[28] p: For more complex manipulation tasks, recent works explore a wide range of skills—from tool use with chopsticks [ 25 ] to catching objects [ 26 ] and in-hand reorientation [ 27 , 28 , 29 ] . Large-scale vision-based approaches such as DexArt [ 4 ] and DexMV [ 3 ] aim to boost generalization via diverse datasets and visual pretraining. Other efforts improve RL algorithms [ 30 , 31 ] or adopt cross-modal imitation strategies from human videos [ 3 , 32 ] .

[29] p: Despite these advances, most existing methods focus on improving policy learning frameworks or scaling training data, while paying relatively less attention to how hand-object interaction is represented. Common strategies encode global object geometry [ 15 ] or use position-based features (e.g., relative distances or joint signals). However, such representations often lack task-specific structure and fail to capture fine-grained contact variations across diverse objects. While a few recent efforts—e.g., [ 27 , 33 ] —explore structured representations, the focus remains limited.

[30] p: In contrast, our work centers on developing a structured and task-relevant representation, DexRep , that explicitly encodes local surface geometry and hand-object spatial proximity. This design enables consistent application across multiple dexterous tasks—including grasping, in-hand manipulation, and handover—and supports generalization across novel objects and different robotic hands.

[31] h3: II-B Representation for Robotic Manipulation

[32] p: In RL-based manipulation, effective policy learning critically depends on the quality of state representation—particularly how the interaction between the hand and the environment is perceived and encoded. To this end, vision is widely used to represent object geometry and spatial context, leveraging various modalities such as RGB images [ 34 ] , depth maps [ 35 ] , point clouds [ 2 , 36 , 37 ] , meshes [ 38 ] , or multimodal combinations [ 23 , 5 , 39 ] . More recently, visual pretraining has gained attention as a way to build general-purpose encoders for downstream tasks. R3M [ 40 ] , for example, learns from large-scale human video data, while RealMAE [ 41 ] extends masked autoencoding [ 42 ] to real-world manipulation settings.

[33] p: For encoding the hand, commonly used representations include joint angles [ 2 , 26 , 27 ] , hand point clouds [ 37 , 28 ] , and kinematic descriptions like URDF models [ 43 ] , which help facilitate transfer between different hand morphologies. However, when it comes to modeling interaction, most existing methods rely on coarse spatial encodings, such as distances between hand and object [ 23 , 5 ] or proprioceptive signals [ 44 ] . These features typically fall short in capturing the nuanced contact dynamics necessary for precise manipulation. To address this, She et al. [ 33 ] proposed the Interaction Bisector Surface (IBS) as a geometric descriptor for grasp synthesis. While effective in encoding global interaction surfaces, IBS lacks sensitivity to local surface variation—an essential property for tasks requiring fine contact control, such as in-hand adjustment or compliant manipulation.

[34] p: Furthermore, for a manipulation policy, the input is required to represent the interaction status of the environment. Though reinforcement learning or imitation learning for complex multi-fingered manipulation has the potential to learn the perception representations for the interaction status and the control policy in an end-to-end manner like many frameworks in computer vision tasks, it is challenged by sparse successful trials (or ”positive samples”) due to high dimensional action space of multi-fingered hands or the scarcity of large scale of action demonstration data. Therefore, most existing works [ 2 , 6 , 4 , 45 , 8 ] adopt a two-stage strategy of first learning a feature representation (e.g., encoding object geometry with pre-trained networks such as PointNet [ 15 ] ) and then training a control policy conditioned on this representation.

[35] p: However, simply encoding global object geometry often fails to capture the fine-grained contact interactions necessary for high-precision dexterous manipulation. We contend that explicitly modeling local surface geometry in conjunction with hand kinematics is critical for informing control policies, especially in dynamic and contact-rich tasks. For example, ManipNet [ 46 ] explores this direction by predicting manipulation trajectories from hand-object spatial relations in a supervised setting. Inspired by this insight, we introduce a compact, structured representation tailored for RL, which captures both the global spatial layout and fine local surface geometry. Our goal is to provide general-purpose features that enable generalizable dexterous policy learning across diverse objects, hand morphologies, and manipulation tasks.

[36] h2: III Preliminaries and Method Overview

[37] h3: III-A Preliminaries

[38] p: We formulate dexterous manipulation as a Markov Decision Process (MDP), defined by the tuple ℳ = ( 𝒮 , 𝒜 , 𝒯 , ℛ , γ ) \mathcal{M}=(\mathcal{S},\mathcal{A},\mathcal{T},\mathcal{R},\gamma) . Here, 𝒮 ∈ ℝ n \mathcal{S}\in\mathbb{R}^{n} and 𝒜 ∈ ℝ m \mathcal{A}\in\mathbb{R}^{m} represent the state and action spaces, respectively; 𝒯 : 𝒮 × 𝒜 → 𝒮 \mathcal{T}:\mathcal{S}\times\mathcal{A}\rightarrow\mathcal{S} denotes the state transition dynamics; ℛ : 𝒮 × 𝒜 → ℝ \mathcal{R}:\mathcal{S}\times\mathcal{A}\rightarrow\mathbb{R} is the reward function measuring task progress; and γ ∈ ( 0 , 1 ] \gamma\in(0,1] is the discount factor.

[39] p: The objective is to learn a policy π ⁡ ( a | s ) \pi(a|s) that defines a distribution over actions a a given a state s s , maximizing the expected cumulative discounted reward ∑ t = 0 ∞ γ t ​ r t \sum_{t=0}^{\infty}\gamma^{t}r_{t} , where r t ∈ ℛ r_{t}\in\mathcal{R} . We adopt deep reinforcement learning (DRL) to optimize this policy. The key value functions in this context are defined as:

[40] table: V π ​ ( s ) = 𝔼 π ​ [ ∑ k = 0 ∞ γ k ​ R t + k + 1 | S t = s ] , V^{\pi}(s)=\mathbb{E}_{\pi}\left[\sum_{k=0}^{\infty}\gamma^{k}R_{t+k+1}\,\middle|\,S_{t}=s\right], (1)

[41] table: Q π ( s , a ) = 𝔼 π [ ∑ k = 0 ∞ γ k R t + k + 1 | S t = s , A t = a ] , Q^{\pi}(s,a)=\mathbb{E}_{\pi}\left[\sum_{k=0}^{\infty}\gamma^{k}R_{t+k+1}\,\middle|\,S_{t}=s,A_{t}=a\right], (2)

[42] table: A π ​ ( s , a ) = Q π ​ ( s , a ) − V π ​ ( s ) . A^{\pi}(s,a)=Q^{\pi}(s,a)-V^{\pi}(s). (3)

[43] p: We parameterize the policy as a neural network π θ \pi_{\theta} and define its performance as the expected return:

[44] table: J ⁡ ( π θ ) = 𝔼 τ ∼ π θ ​ ( τ ) ​ [ ∑ t = 0 ∞ γ t ​ R t ] , J(\pi_{\theta})=\mathbb{E}_{\tau\sim\pi_{\theta}(\tau)}\left[\sum_{t=0}^{\infty}\gamma^{t}R_{t}\right], (4)

[45] p: where τ \tau denotes a trajectory sampled from the policy. The policy parameters θ \theta are optimized via gradient ascent on J ⁡ ( π θ ) J(\pi_{\theta}) , using the policy gradient:

[46] table: ∇ θ J ​ ( π θ ) = 𝔼 τ ∼ π θ ​ ( τ ) ​ [ ∇ θ ​ log ​ π θ ​ ( a t | s t ) ​ A π θ ​ ( s t , a t ) ] . \nabla_{\theta}J(\pi_{\theta})=\mathbb{E}_{\tau\sim\pi_{\theta}(\tau)}\left[\nabla_{\theta}\log\pi_{\theta}(a_{t}|s_{t})A^{\pi_{\theta}}(s_{t},a_{t})\right]. (5)

[47] h3: III-B Method Overview

[48] p: Given the task specification, initial hand configuration, and target manipulation goal (e.g., desired object pose), our objective is to generate a sequence of actions that successfully completes the manipulation. As illustrated in Fig. 2 , our approach begins by extracting an informative hand-object interaction feature f f based on the current observation. The complete state input to the policy is composed of this interaction feature f f and the proprioceptive state of the robot f prop f_{\text{prop}} , such as joint angles and velocities. The policy π θ \pi_{\theta} then predicts the next action a = π θ ​ ( s ) a=\pi_{\theta}(s) , where s = { f , f prop } ∈ 𝒮 s=\{f,f_{\text{prop}}\}\in\mathcal{S} . The environment transitions to the next state via the dynamics 𝒯 \mathcal{T} , and the process iterates until task success or failure. Our method is evaluated across multiple dexterous manipulation tasks and demonstrates generalizable performance without requiring task-specific modifications.

[49] p: The remainder of this paper is organized as follows: Sec. IV introduces our proposed hand-object interaction representation, DexRep; Sec. V describes how we train manipulation policies using DexRep for different tasks; Sec. VI presents comparative results across multiple manipulation tasks; Sec. VII analyzes the characteristics and generalization performance of DexRep; Sec. VIII demonstrates the real-world deployment and robustness of our approach.

[50] h2: IV DexRep: Dexterous Representation

[51] p: In this section, we introduce our key contribution: DexRep, a hand-object interaction representation for learning dexterous manipulation tasks in robotics. DexRep extracts features f f that provide the policy π \pi with rich spatial and geometric cues, enabling effective perception of hand-object configurations and promoting robust generalization across tasks and object geometries. DexRep comprises three complementary components: the Occupancy Feature f o f_{o} , the Surface Feature f s f_{s} , and the Local-Geo Feature f l f_{l} .

[52] figure: Figure 2 : DexRep and its integration into dexterous manipulation learning. Left: Visualization of the three components of DexRep —Occupancy, Surface, and Local-Geo features—each encoding a different aspect of the hand-object interaction. Right: Policy learning framework with DexRep as input. The dashed box denotes the representation for the second hand in bimanual settings, which is omitted in single-hand scenarios.

[53] h4: IV- 1 Occupancy Feature f o f_{o}

[54] p: The Occupancy Feature captures coarse global geometry by encoding the voxel occupancy within a 3D volume anchored to the palm of the robotic hand. It captures global shape information via a coarse occupancy volume instead of point clouds carrying detailed geometry.

[55] p: The volume is defined as a 10 × 10 × 10 10\times 10\times 10 voxel grid, where each voxel has an edge length l v l_{v} , chosen based on the required task-level precision. The volume is anchored to a point slightly inside the palm, offset perpendicularly from the root joint of the middle finger, as this region is most relevant for pre-grasp and contact. The volume rigidly follows the root joint’s position and orientation during manipulation. We define f o ∈ { 0 , 1 } 1000 f_{o}\in\{0,1\}^{1000} , where each element f o i f_{o}^{i} represents whether the i i -th voxel is occupied by any point from the object point cloud:

[56] table: f o i = { 1 , if occupied, 0 , otherwise. f_{o}^{i}=\begin{cases}1,&\text{if occupied,}\\ 0,&\text{otherwise.}\end{cases} (6)

[57] p: This compact binary encoding facilitates robust object localization and generalization by abstracting away fine-grained shape details. This abstraction offers a simplified yet effective spatial representation for approaching and hand pose pre-shaping. Higher-resolution grids can capture more details, but at the cost of increased computational overhead and reduced generalization to object variation and robustness to input noise.

[58] h4: IV- 2 Surface Feature f s f_{s}

[59] p: To support precise finger control, we introduce the Surface Feature, which encodes spatial distances and local surface normals between key hand joints and the object surface. Let n n denote the number of sampled hand keypoints (e.g., fingertips and joints), then f s ∈ ℝ 4 ​ n f_{s}\in\mathbb{R}^{4n} is defined as:

[60] table: f s j = { min ⁡ ( ‖ p h j − p o j ‖ , σ max ) , n o j } , f_{s}^{j}=\left\{\min\left(\|p_{h}^{j}-p_{o}^{j}\|,\sigma_{\max}\right),\;n_{o}^{j}\right\}, (7)

[61] p: where p h j p_{h}^{j} is the j j -th keypoint on the hand, p o j p_{o}^{j} is its closest point on the object surface, and n o j n_{o}^{j} is the corresponding surface normal. The maximum distance threshold σ max \sigma_{\max} is set based on the expected range of hand-object proximity for each task.

[62] p: This feature captures two critical cues: (i) the proximity between each finger joint and nearby object surfaces, and (ii) the orientation of those surfaces via normals. These cues allow the policy to infer where and how to approach the object for stable and purposeful contact.

[63] h4: IV- 3 Local-Geo Feature f l f_{l}

[64] p: While surface normals provide directional cues, they do not encode rich geometric structures such as curvature, thickness, or local symmetry, which are essential for fine manipulation. To address this, we propose the Local-Geo Feature f l f_{l} , which augments the Surface Feature with learned geometric descriptors extracted via a pretrained PointNet encoder.

[65] p: We adopt a two-stage pipeline: In the first stage, we train a PointNet autoencoder to reconstruct object point clouds from ShapeNet55 [ 47 ] , using a training loss:

[66] table: L ae = α ⋅ L cls + β ⋅ L chamfer + γ ⋅ L emd , L_{\text{ae}}=\alpha\cdot L_{\text{cls}}+\beta\cdot L_{\text{chamfer}}+\gamma\cdot L_{\text{emd}}, (8)

[67] p: where L cls L_{\text{cls}} is the classification loss, L chamfer L_{\text{chamfer}} measures average point-wise distance [ 48 ] , and L emd L_{\text{emd}} is the Earth Mover’s Distance [ 49 ] . We set α = 2 \alpha=2 , β = 0.1 \beta=0.1 , and γ = 100 \gamma=100 to balance shape reconstruction and feature discrimination.

[68] p: After training, we retain only the encoder to extract per-point descriptors. For each hand keypoint, we retrieve the descriptor of its closest point on the object surface, yielding f l ∈ ℝ n × 64 f_{l}\in\mathbb{R}^{n\times 64} . This feature provides compact yet expressive local geometry, facilitating nuanced contact reasoning in manipulation.

[69] h4: IV- 4 Discussion

[70] p: DexRep provides a unified and flexible representation that balances coarse global structure and fine local detail. The voxel-based Occupancy Feature is simple to compute and robust to noise, making it suitable for coarse alignment and collision avoidance. The Surface Feature captures critical contact geometry through relative distances and normals. The Local-Geo Feature offers high-capacity geometric descriptors, enhancing performance in tasks requiring fine contact adaptation.

[71] p: We choose voxel grids for global shape abstraction due to their computational simplicity and discretization properties. While denser sampling on the hand surface could enrich spatial resolution, it would also increase computational complexity. Surface normals offer an interpretable and low-dimensional encoding, whereas PointNet descriptors serve as a more expressive alternative for complex geometries.

[72] p: Together, these features enable DexRep to serve as a general-purpose, task-agnostic interaction representation that supports robust learning and transfer in dexterous manipulation.

[73] h2: V Learning Manipulation Policy with DexRep

[74] p: In this section, we describe how we incorporate DexRep into reinforcement learning (RL) to train manipulation policies π θ \pi_{\theta} for three dexterous tasks: grasping, in-hand reorientation, and handover. We first present the network architecture that integrates DexRep as a policy input. We then define the reward functions and action spaces tailored to each task. Finally, we describe how we train the policy network π θ \pi_{\theta} using RL with or without demonstrations depending on manipulation tasks.

[75] h3: V-A Embedding DexRep into RL Policy π θ \pi_{\theta}

[76] p: To support both single- and dual-hand scenarios, we adopt a modular network design. For each hand, we compute DexRep features—including the Occupancy ( f o f_{o} ), Surface ( f s f_{s} ), and Local-Geo ( f l f_{l} ) components. When dual hands are used, the features from the second hand are denoted by a prime symbol (e.g., f o ′ f_{o}^{\prime} ). We also include the proprioceptive state f p ​ r ​ o ​ p f_{prop} , which encodes the joint angles, velocities, and other robot-specific information.

[77] p: The network architecture processes each feature component individually. Occupancy Feature and Surface Feature { f o , f s } \{f_{o},f_{s}\} (and { f o ′ , f s ′ } \{f_{o}^{\prime},f_{s}^{\prime}\} if present) as well as f p ​ r ​ o ​ p f_{prop} are passed through independent fully connected (FC) layers with layer normalization. Due to its high magnitude variability, the Local-Geo feature f l f_{l} undergoes batch normalization before being processed by a dedicated FC layer and layer normalization. The resulting feature embeddings are concatenated and input to a multi-layer perceptron (MLP), which outputs the action a a . The full network architecture is illustrated in Fig. 2 (right).

[78] figure: Figure 3 : Demonstration acquisition for behavior cloning. In the grasping task, we obtain human demonstration data 𝒟 human \mathcal{D}_{\text{human}} from the GRAB dataset [ 50 ] and retarget it to Adroit hand [ 51 ] to generate robot demonstration data 𝒟 \mathcal{D} for subsequent BC initialization of the policy π θ \pi_{\theta} . Figure 4 : Our pipeline to learn manipulation policy with DexRep. For the grasping task, we first pre-train the policy using BC and then fine-tune it through RL. For in-hand reorientation and handover tasks, we start with a randomly initialized policy and learn the strategy from scratch using RL.

[79] h3: V-B Reward Function ℛ \mathcal{R}

[80] h4: V-B 1 Grasping Task

[81] p: The total reward is composed of four components:

[82] table: r grasp = r approach + r lift + r pen + r target . r_{\text{grasp}}=r_{\text{approach}}+r_{\text{lift}}+r_{\text{pen}}+r_{\text{target}}. (9)

[83] p: Approach Reward: encourages the hand to move closer to the object:

[84] table: r approach = 0.1 ​ ( 1 10 ⋅ d f → o + 0.25 − 1 ) , r_{\text{approach}}=0.1\left(\frac{1}{10\cdot d_{f\rightarrow o}+0.25}-1\right), (10)

[85] p: where d f → o d_{f\rightarrow o} is the sum of distances from all fingertips to the object surface.

[86] p: Lift Reward: encourages the object to be lifted above the table:

[87] table: r lift = { 1 , if ​ h > 0.02 ​ m , 0 , otherwise , r_{\text{lift}}=\begin{cases}1,&\text{if }h>0.02\penalty\ m,\\ 0,&\text{otherwise},\end{cases} (11)

[88] p: where h h is the object’s height above the table.

[89] p: Penetration Penalty: discourages penetration into the object or table:

[90] table: r pen = max ⁡ ( 0.01 ​ ( 1 − e − ( d table + d obj ) ) , − 100 ) , r_{\text{pen}}=\max\left(0.01\left(1-e^{-(d_{\text{table}}+d_{\text{obj}})}\right),-100\right), (12)

[91] p: where d table d_{\text{table}} and d obj d_{\text{obj}} are signed penetration depths.

[92] p: Target Reward: encourages object delivery to the target location without penetration:

[93] table: r target = { 10 , ‖ p obj − p tar ‖ < 0.1 ​ m ​ and ​ r pen > − 30 , 20 , ‖ p obj − p tar ‖ < 0.05 ​ m ​ and ​ r pen > − 30 , 0 , otherwise . r_{\text{target}}=\begin{cases}10,&\|p_{\text{obj}}-p_{\text{tar}}\|<0.1\penalty\ m\text{ and }r_{\text{pen}}>-30,\\ 20,&\|p_{\text{obj}}-p_{\text{tar}}\|<0.05\penalty\ m\text{ and }r_{\text{pen}}>-30,\\ 0,&\text{otherwise}.\end{cases} (13)

[94] h4: V-B 2 In-Hand Reorientation Task

[95] p: The reward consists of four components:

[96] table: r rot = r dis + r orient + r act + r suc . r_{\text{rot}}=r_{\text{dis}}+r_{\text{orient}}+r_{\text{act}}+r_{\text{suc}}. (14)

[97] p: Distance Reward: penalizes deviation from the target position:

[98] table: r dis = − 10 ⋅ d o → t , r_{\text{dis}}=-10\cdot d_{o\rightarrow t}, (15)

[99] p: where d o → t d_{o\rightarrow t} is the Euclidean distance between the object and the target.

[100] p: Orientation Reward: encourages rotation alignment:

[101] table: r orient = 1 | d rot | + 0.1 , r_{\text{orient}}=\frac{1}{|d_{\text{rot}}|+0.1}, (16)

[102] p: where d rot = 2 ​ arcsin ⁡ ( min ⁡ ( ‖ ( Δ ​ x q , Δ ​ y q , Δ ​ z q ) ‖ 2 , 1.0 ) ) d_{\text{rot}}=2\arcsin(\min(\|(\Delta x_{q},\Delta y_{q},\Delta z_{q})\|_{2},1.0)) , derived from quaternion difference.

[103] p: Action Penalty: discourages large joint movements:

[104] table: r act = − 0.0002 ∑ i = 1 n j a i 2 , r_{\text{act}}=-0.0002\sum_{i=1}^{n_{j}}a_{i}^{2}, (17)

[105] p: where a i a_{i} is the action on joint i i , and n j n_{j} is the number of joints.

[106] p: Success Reward: provides a bonus when rotation is sufficiently accurate:

[107] table: r suc = { 250 , if ​ d rot ≤ 0.1 ​ rad , 0 , otherwise . r_{\text{suc}}=\begin{cases}250,&\text{if }d_{\text{rot}}\leq 0.1\penalty\ \text{rad},\\ 0,&\text{otherwise}.\end{cases} (18)

[108] h4: V-B 3 Handover Task

[109] p: The handover reward encourages accurate object delivery via:

[110] table: r over = { e − 10 ⋅ d o → t + 250 , if ​ d o → t ≤ 0.02 ​ m , e − 10 ⋅ d o → t , otherwise , r_{\text{over}}=\begin{cases}e^{-10\cdot d_{o\rightarrow t}}+250,&\text{if }d_{o\rightarrow t}\leq 0.02\penalty\ m,\\ e^{-10\cdot d_{o\rightarrow t}},&\text{otherwise},\end{cases} (19)

[111] p: where d o → t d_{o\rightarrow t} is the Euclidean distance between the object and the target pose.

[112] h3: V-C Action Space 𝒜 \mathcal{A}

[113] p: We define 𝒜 \mathcal{A} as a continuous space over target joint positions. For grasping, the action is a = { p g , θ } a=\{p_{g},\theta\} where p g ∈ ℝ 6 p_{g}\in\mathbb{R}^{6} is the global pose of the Adroit hand and θ ∈ ℝ 24 \theta\in\mathbb{R}^{24} is the set of joint angles. For the other two tasks using the Shadow Hand, a = θ ∈ ℝ 20 a=\theta\in\mathbb{R}^{20} .

[114] p: Each action a target a_{\text{target}} is executed using a low-level PD controller:

[115] table: τ = K p ​ ( a target − a current ) − K d ​ a ˙ current , \tau=K_{p}(a_{\text{target}}-a_{\text{current}})-K_{d}\,\dot{a}_{\text{current}},

[116] p: where a current a_{\text{current}} and a ˙ current \dot{a}_{\text{current}} denote the current joint positions and velocities, respectively, and K p K_{p} and K d K_{d} are the proportional and derivative gains. The gains K p K_{p} and K d K_{d} are hand-specific and we follow [ 1 , 52 ] to set the values.

[117] h3: V-D Learning Manipulation Policies via ∇ θ J ​ ( π θ ) \nabla_{\theta}J(\pi_{\theta})

[118] h4: V-D 1 Learning from Demonstrations for Grasping

[119] p: Incorporating human demonstrations has proven effective in improving sample efficiency and promoting safe, human-like robotic behaviors [ 1 , 2 , 3 ] . Following this line of work, we adopt a two-stage learning strategy for the grasping task: we first pretrain the policy π θ \pi_{\theta} using Behavior Cloning (BC) from expert demonstrations, and then fine-tune it using reinforcement learning (RL). The overall pipeline is illustrated in Fig. 4 and Fig. 4 .

[120] p: To acquire demonstrations, we utilize a retargeting-based pipeline to convert human grasp trajectories from GRAB [ 50 ] into robot-executable demonstrations (Fig. 4 ). GRAB provides whole-body motion sequences of 10 subjects interacting with 51 household objects. We extract the hand-object interaction segment from each trajectory using the MANO hand model [ 53 ] , specifically cropping frames from when the hand is within 10 ​ c ​ m 10\penalty\ cm of the object until the object is lifted by 4 ​ c ​ m 4\penalty\ cm . All demonstrations are normalized to an object-centric coordinate frame by translating the object to the origin and applying the same transformation to the hand.

[121] figure: Figure 5 : Retargeting process. Key vectors—finger-to-finger, finger-to-wrist, and finger-to-object—are computed from both human (MANO) and robotic (Adroit) hands and optimized to align hand postures.

[122] p: Let 𝒟 Human = { d 0 , … , d N } \mathcal{D}_{\text{Human}}=\{d_{0},\dots,d_{N}\} denote the set of human demonstrations, where each trajectory d n = { ( g t , q t , o t ) } t = 0 T d_{n}=\{(g_{t},q_{t},o_{t})\}_{t=0}^{T} contains global hand poses g t g_{t} , joint angles q t q_{t} , and object poses o t o_{t} at each timestep t t . We aim to map these to the Adroit hand [ 51 ] via retargeting.

[123] p: Following DexPilot [ 54 ] , we independently optimize each frame’s joint configuration via non-linear optimization. The objective minimizes discrepancies between key postural vectors of the human and robot hands:

[124] table: min ⁡ ∑ i = 0 I q t 𝐑 , R g ⁡ ‖ 𝐯 i 𝐑 ​ ( R g , q t 𝐑 ) − k i ​ 𝐯 i 𝐇 ​ ( q t 𝐇 ) ‖ 2 , \min_{q_{t}^{\mathbf{R}},R_{g}}\sum_{i=0}^{I}\left\|\mathbf{v}_{i}^{\mathbf{R}}(R_{g},q_{t}^{\mathbf{R}})-k_{i}\,\mathbf{v}_{i}^{\mathbf{H}}(q_{t}^{\mathbf{H}})\right\|^{2}, (20)

[125] p: where I = 3 I=3 represents three kinds of key vectors (finger-to-finger vectors, finger-to-wrist vectors, finger-to-object vectors) of the robotic hand 𝐯 𝐢 𝐑 \mathbf{v}_{\mathbf{i}}^{\mathbf{R}} and the human hand 𝐯 𝐢 𝐇 \mathbf{v}_{\mathbf{i}}^{\mathbf{H}} , computed by the joint angles q t 𝐑 q_{t}^{\mathbf{R}} and q t 𝐇 q_{t}^{\mathbf{H}} through forward kinematics. The three types of key vector are shown in Fig. 5 . Here, k i k_{i} is the scale ratio for the i t ​ h i^{th} type of key vectors between the Adroit Hand [ 51 ] and the MANO Hand [ 53 ] , and R g R_{g} denotes the global translation and rotation of the robotic arm attached to the hand. Including R g R_{g} in optimization helps reduce positional error caused by structural differences between human and robotic hands.

[126] p: After optimization, we convert the retargeted joint trajectories into executable actions in MuJoCo [ 55 ] , optionally applying correlated sampling [ 45 ] to reduce object drop during lifting. This yields a robot demonstration dataset 𝒟 = { ( s , a ) } \mathcal{D}=\{(s,a)\} for subsequent BC training.

[127] p: The policy is then initialized using Behavior Cloning:

[128] table: L BC = 1 | 𝒟 | ​ ∑ ( s , a ) ∈ 𝒟 ‖ π θ ​ ( s ) − a ‖ 2 , L_{\text{BC}}=\frac{1}{|\mathcal{D}|}\sum_{(s,a)\in\mathcal{D}}\left\|\pi_{\theta}(s)-a\right\|^{2}, (21)

[129] p: where | 𝒟 | |\mathcal{D}| is the number of state-action pairs in the dataset and π θ \pi_{\theta} is the policy network parameterized by θ \theta . While BC offers a strong initialization, it is susceptible to covariate shift between the demonstration and learned policy distributions.

[130] p: To mitigate this, we adopt the DAPG algorithm [ 1 ] , which integrates demonstrations into RL fine-tuning. Specifically, we augment the standard policy gradient (Eq. 5 ) with an additional term based on demonstration data:

[131] table: ∇ θ J ​ ( θ ) FT \displaystyle\nabla_{\theta}J(\theta)_{\text{FT}} = 𝔼 ( s , a ) ∼ ρ π ​ [ ∇ θ ​ ln ​ π θ ​ ( a | s ) ​ A π ​ ( s , a ) ] \displaystyle=\mathbb{E}_{(s,a)\sim\rho^{\pi}}\left[\nabla_{\theta}\ln\pi_{\theta}(a|s)A^{\pi}(s,a)\right] (22) + \displaystyle+ 𝔼 ( s , a ) ∼ 𝒟 ​ [ ∇ θ ​ ln ​ π θ ​ ( a | s ) ​ λ 0 ​ λ 1 k ​ max ( s ′ , a ′ ) ∈ ρ π ​ A π ​ ( s ′ , a ′ ) ] , \displaystyle\mathbb{E}_{(s,a)\sim\mathcal{D}}\left[\nabla_{\theta}\ln\pi_{\theta}(a|s)\lambda_{0}\lambda_{1}^{k}\max_{(s^{\prime},a^{\prime})\in\rho^{\pi}}A^{\pi}(s^{\prime},a^{\prime})\right],

[132] p: where ρ π \rho^{\pi} is the current policy rollout, A π A^{\pi} is the advantage function (computed via GAE [ 56 ] ), ( λ 0 , λ 1 ) = ( 0.1 , 0.95 ) (\lambda_{0},\lambda_{1})=(0.1,0.95) control the decaying contribution of demonstrations, and max ( s ′ , a ′ ) ∈ ρ π ⁡ A π θ ​ ( s ′ , a ′ ) \max_{(s^{\prime},a^{\prime})\in\rho_{\pi}}A^{\pi_{\theta}}(s^{\prime},a^{\prime}) =1.

[133] h4: V-D 2 Learning from Scratch for Other Tasks

[134] p: Following prior work [ 52 ] , we train policies for in-hand reorientation and handover tasks using PPO [ 57 ] from scratch in simulation, leveraging massive parallelization via Isaac Gym [ 58 ] . DexRep is used as the primary state representation.

[135] p: PPO maintains two networks: the actor π θ ​ ( a | s ) \pi_{\theta}(a|s) and the critic V ϕ ​ ( s ) V_{\phi}(s) . The actor is updated via:

[136] table: ∇ θ J ( θ ) PPO = 𝔼 ( s , a ) ∼ ρ π θ old [ \displaystyle\nabla_{\theta}J(\theta)_{\text{PPO}}=\mathbb{E}_{(s,a)\sim\rho^{\pi_{\theta_{\mathrm{old}}}}}\big[ ∇ θ r t ​ ( θ ) ​ A π θ ​ ( s , a ) \displaystyle\nabla_{\theta}r_{t}(\theta)A^{\pi_{\theta}}(s,a) (23) − β ∇ θ KL ( π θ old ∥ π θ ) ] , \displaystyle-\beta\nabla_{\theta}\mathrm{KL}\big(\pi_{\theta_{\mathrm{old}}}\|\pi_{\theta}\big)\big],

[137] p: where r t ​ ( θ ) = π θ ​ ( a | s ) π θ old ​ ( a | s ) r_{t}(\theta)=\frac{\pi_{\theta}(a|s)}{\pi_{\theta_{\text{old}}}(a|s)} is the probability ratio, β \beta determines the weight of the KL divergence term in the objective, and A π θ A^{\pi_{\theta}} is the advantage function and is calculated using GAE [ 56 ] .

[138] p: The critic is updated to minimize the squared error between the predicted and target returns:

[139] table: ∇ ϕ J ​ ( ϕ ) PPO = 𝔼 ( s , a ) ∼ ρ π θ old ​ [ 2 ​ ( V ϕ ​ ( s ) − G ) ​ ∇ ϕ V ϕ ​ ( s ) ] , \nabla_{\phi}J(\phi)_{\text{PPO}}=\mathbb{E}_{(s,a)\sim\rho^{\pi_{\theta_{\mathrm{old}}}}}\left[2\left(V_{\phi}(s)-G\right)\nabla_{\phi}V_{\phi}(s)\right], (24)

[140] p: where G = A + V ϕ old ​ ( s ) G=A+V_{\phi_{\text{old}}}(s) is the bootstrapped return using the old critic network.

[141] p: This learning setup allows us to effectively train policies for complex dexterous tasks without relying on demonstrations.

[142] h2: VI Effectiveness of DexRep Across Tasks

[143] p: To comprehensively evaluate the robustness and generalization capability of DexRep across diverse dexterous manipulation scenarios, we benchmark its performance in three representative tasks: grasping, in-hand reorientation, and bimanual handover. For each task, we compare DexRep against state-of-the-art baselines in terms of success rate, training efficiency, and generalization to unseen objects. We conduct each simulation experiment with 10 random seeds in the paper, and report the mean and standard deviation of the seeds. In all tables, “±” denotes the standard deviation (SD) of the reported success rates.

[144] figure: Figure 6 : Success rate (or mean success times per episode) and mean reward of our method and baselines in different tasks during training (left: Grasping; middle: In-Hand Reorientation; right: Handover). The x-axis represents the training iterations. The y-axis indicates the success rate (%), mean success times per episode (dashed lines) , or mean reward, and the shaded area represents the standard deviation. Table I : Success rate (%) of our method and baselines for grasping in MuJoCo and Isaac Gym. Simulator MuJoCo Isaac Gym Methods DAPG [ 1 ] ILAD [ 2 ] Ours DAPG [ 1 ] ILAD [ 2 ] IBS [ 33 ] UniDexGrasp [ 6 ] UniDexGrasp++ [ 8 ] Ours Seen 36.3±8.2 64.8±3.3 96.5±0.9 21.0 32.0 57.0 79.0 85.4 96.5 Unseen 21.5±12.3 22.6±3.1 88.1±2.0 12.5 24.5 54.0 72.5 78.2 96.4 • Notes: Some simulation experiment settings, like training and testing objects and the reward functions in MuJoCo and Isaac Gym, also differ. See Sec. VI-A2 for more details. The results of DAPG, ILAD, and IBS in Isaac Gym are sourced from UniDexGrasp [ 6 ] . Table II : Success rate (%) of our method and baselines for In-Hand Reorientation and Handover. “GeoDex-50k” is a variant of GeoDex, which is pretrained with the same 50K objects as our method. Tasks In-Hand Reorientation Handover Methods Base [ 52 ] GeoDex [ 27 ] GeoDex-50k Ours Base [ 52 ] Ours-Throw Ours-Catch Ours-Dual Seen 66.5±3.9 87.5±0.8 88.8±0.1 91.1±1.2 43.1±3.2 62.3±4.2 77.3±4.7 81.5±0.1 Unseen 50.1±6.2 76.3±3.0 81.1±1.5 86.0±3.9 36.8±2.9 60.0±1.2 72.1±3.8 77.3±1.9

[145] h3: VI-A Efficacy of DexRep in Grasping

[146] p: We first evaluate the performance of DexRep in dexterous grasping tasks, focusing on its training efficiency and generalization to unseen objects.

[147] h4: VI-A 1 Experimental Setup

[148] p: Experiments are conducted in the MuJoCo [ 55 ] simulator using the 30-DoF AdroitHand [ 51 ] (Fig. 1 , left). At each episode’s start, the object is placed near the origin with small perturbations: translation in x ∼ [ − 0.05 , 0.05 ] x\sim[-0.05,0.05] m, y ∼ [ − 0.05 , 0 ] y\sim[-0.05,0] m, and a random in-plane rotation in [ − π , π ] [-\pi,\pi] . Object mass and friction are set to 0.5 0.5 kg and 1.0 1.0 . The hand is initialized to the average pre-grasp pose of all retargeted demonstrations.

[149] p: Baselines. We compare DexRep against two widely used hand-object representations in dexterous RL: (1) DAPG [ 1 ] : uses relative hand-object distances; (2) ILAD [ 2 ] : uses PointNet [ 15 ] to encode object shape features. We reimplement both in the same setup for fair comparison.

[150] p: Datasets. Training and evaluation follow a standard object split. We train using 40 objects from GRAB [ 50 ] and evaluate both on these (seen) and the full set of DexGraspNet [ 7 ] (5,355 unseen shapes).

[151] p: Network Architecture. The input to the policy includes the robot state f p ​ r ​ o ​ p f_{prop} and the three DexRep features. Input sizes are 105 ( f p ​ r ​ o ​ p f_{prop} ), 1088 ( f o + f s f_{o}+f_{s} ), and 1408 ( f l f_{l} ). Each input is passed through a single-layer encoder of size 128. The policy itself is a 3-layer MLP with hidden dimensions [ 512,128 ] [512,128] , followed by ReLU activations. The output action 𝐚 ∈ ℝ 30 \mathbf{a}\in\mathbb{R}^{30} includes 6-DoF end-effector pose and 24 joint commands.

[152] p: Training Details. DexRep is computed with a voxel size l v = 0.02 l_{v}=0.02 m and surface feature perception range σ m ​ a ​ x = 0.2 \sigma_{max}=0.2 m (Based on ablation in Sec. VII-G ). Behavior Cloning (BC) is used to warm-start policies using 40-object demonstrations, optimized with Adam (lr= 1 × 10 − 5 1\times 10^{-5} , batch=64, 150 epochs). BC converges in ∼ \sim 6 minutes. Subsequently, we train the policy with DAPG for 600 iterations using 10 seeds. Each iteration generates 10 trajectories per object, each of 200 steps. RL training takes approximately 42 GPU hours on an NVIDIA RTX 3090 GPU.

[153] p: Evaluation Metric. Following UniDexGrasp [ 6 ] , a grasp is successful if the object is lifted to 30 ± 5 30\pm 5 cm above the table by the end of the episode. The final evaluation is over 100 trajectories per object.

[154] h4: VI-A 2 Quantitative Results and Analysis

[155] p: As shown in Fig. 6 (left), DexRep achieves faster convergence and higher final success rate than DAPG and ILAD. On 5,355 unseen DexGraspNet objects, DexRep achieves 88.1% success, outperforming ILAD and DAPG by about 66% (Table I , left). This demonstrates that DexRep, trained on just 40 objects, generalizes remarkably well to unseen categories with large geometric variation. To compare with UniDexGrasp [ 6 ] and UniDexGrasp++ [ 8 ] , we also train DexRep in Isaac Gym using their protocols. As shown in Table I (right), DexRep achieves ∼ \sim 96% success on both seen and unseen objects, exceeding UniDexGrasp++ by 11.1% (seen) and 18.2% (unseen), despite using a smaller training set. This confirms the portability and robustness of DexRep across different RL frameworks and simulation engines.

[156] p: The large performance gap between DexRep and geometry-agnostic (DAPG) or globally encoded (ILAD) methods highlights the importance of structured local interaction modeling. Our results indicate that surface-aware local features are essential not only for fine-grained control but also for generalizable policy learning. Interestingly, the improvement is more prominent in unseen-object tests, implying that DexRep captures task-relevant affordances beyond mere geometry similarity.

[157] h3: VI-B Efficacy of DexRep in In-Hand Reorientation

[158] p: We evaluate the effectiveness of DexRep in dynamic in-hand reorientation, where the robotic hand must rotate an in-hand object to reach a target orientation with high precision.

[159] h4: VI-B 1 Experimental Setup

[160] p: Following [ 52 , 28 ] , we conduct experiments in Isaac Gym [ 58 ] using the 24-DoF Shadow Hand [ 14 ] (Fig. 1 , middle). At each episode’s start, the hand is placed at ( 0 , 0 , 0.5 ) (0,0,0.5) in the world frame, with its joint angles perturbed by 𝒩 ⁡ ( 0 , 0.2 ) \mathcal{N}(0,0.2) . The object is initialized at an offset of ( 0 , − 0.39 , 0.1 ) (0,-0.39,0.1) from the hand, with additional Gaussian noise 𝒩 ⁡ ( 0 , 0.01 ) \mathcal{N}(0,0.01) . Both initial and target orientations are randomly sampled from SO ⁡ ( 3 ) \mathrm{SO}(3) .

[161] p: Baselines. We compare DexRep against three baselines trained from scratch using PPO [ 57 ] : (1) Base [ 52 ] : includes full proprioception and object pose/velocity; (3) GeoDex [ 27 ] : augments Base with a rotation-sensitive PointNet encoder trained on 85 objects. (3) GeoDex-50k [ 27 ] : augments Base with a rotation-sensitive PointNet encoder trained on the same object set (50k objects) as ours.

[162] p: Datasets. We select 25 objects for training and 12 for testing (Fig. 7 ) from the YCB dataset [ 59 ] , which is used in [ 27 ] . For the GeoDex baseline, we pretrain its rotation-sensitive PointNet on 85 objects (YCB [ 59 ] + ContactDB [ 60 ] ) and also with a larger set (50k ShapeNet objects [ 47 ] , the same dataset used in Local-Geo Feature of DexRep) for an extended comparison.

[163] figure: Figure 7 : 37 Objects used in In-Hand Reorientation. The first 25 objects (above the dotted line) are used in training (seen), while the rest are for evaluation (unseen).

[164] p: Network Architecture. The input consists of f p ​ r ​ o ​ p f_{prop} (Base), and the DexRep features f o f_{o} , f s f_{s} , and f l f_{l} , with input sizes 211, 1080, and 1280, respectively. Each is passed through a single-layer encoder of size 128. The policy is an MLP with layers [ 512,512,128 ] [512,512,128] and Elu activations. The output 𝐚 ∈ ℝ 20 \mathbf{a}\in\mathbb{R}^{20} corresponds to 20 joint control signals.

[165] p: Training Details. DexRep is computed with voxel size l v = 0.01 l_{v}=0.01 m and surface feature distance σ m ​ a ​ x = 0.1 \sigma_{max}=0.1 m (Based on ablation in Sec . VII-G ). RL training is conducted in 8,000 parallel environments for 5,000 iterations. The environment is reset only once at the beginning. If the object reaches the target position prematurely, the target position will be refreshed to ensure the continuity of the hand and object trajectories within the episode. Training takes ∼ \sim 70 GPU hours on an NVIDIA RTX 3090.

[166] p: Evaluation Metric. We evaluate using: (1) Success Rate : percentage of episodes with final orientation error d rot < 0.1 d_{\text{rot}}<0.1 rad; (2) Success Times per Episode : average number of successful reorientations per episode; (3) Mean Reward : average return over the last 200 successful episodes.

[167] h4: VI-B 2 Quantitative Results and Analysis

[168] p: Table II reports the success rates of different methods on both seen and unseen objects. Our method ( Ours ) achieves the highest performance across both sets, reaching a success rate of 91.1% on seen and 86.0% on unseen objects. Compared to the Base representation [ 52 ] , which only includes hand proprioception and object state (pose and velocity), DexRep improves performance by 24.6% on seen and 35.9% on unseen objects, demonstrating its significant advantage in tasks requiring precise control.

[169] p: GeoDex [ 27 ] , a strong baseline, enhances Base by encoding object geometry using a rotation-sensitive PointNet , which learns to capture orientation-aware global features. This design is tailored for in-hand reorientation, where object orientation is central to task success. When trained with the original 85 objects, GeoDex achieves 87.5% (seen) and 76.3% (unseen). Our retrained version, GeoDex-50k , which uses the same pretraining dataset as our method, improves results to 88.8% and 81.1%. Despite the task-specific design of GeoDex, DexRep still outperforms both versions of it by 3.6% on seen and 9.7% on unseen objects. This performance gap suggests that beyond capturing object orientation, the ability to encode local surface properties and hand-object spatial interaction—as realized in DexRep—is more beneficial for robust and generalizable skill learning.

[170] p: While GeoDex leverages global geometry to learn object pose sensitivity, it lacks explicit modeling of physical hand-object interactions, such as local geometry variations and the spatial proximity between hands and the surface of objects. In contrast, DexRep incorporates both coarse and fine-grained interaction cues—voxelized global geometry, local features, and proximity-based local interaction fields—providing a richer and more structured representation. The voxelized global geometry encodes the object pose, local features provide abundant information for precise contact reasoning, and the spatial proximity helps the control refinement, especially when adapting to novel object shapes and poses. The consistently better performance on unseen objects further validates the generalization strength of structured local interaction modeling.

[171] h3: VI-C Efficacy of DexRep in Bimanual Handover

[172] p: While previous sections demonstrate the efficacy of DexRep in single-hand tasks such as grasping and in-hand reorientation, we now investigate whether DexRep can enhance synergy in two-hand coordination tasks by modeling hand-object interactions for both hands. To this end, we evaluate DexRep in a bimanual handover scenario, where an object must be transferred smoothly from one hand to another.

[173] h4: VI-C 1 Experimental Setup

[174] p: We construct the handover environment in Isaac Gym [ 58 ] , following settings from [ 52 ] . As illustrated in Fig. 1 (right), two Shadow Hands are fixed in the scene at positions ( 0 , 0 , 0.5 ) (0,0,0.5) (throwing hand) and ( 0 , − 1 , 0.5 ) (0,-1,0.5) (catching hand), with opposing orientations. The object is initially placed near the catching hand with small random perturbations. Its target pose is offset from the initial pose by ( 0 , − 0.25 , 0 ) (0,-0.25,0) with a randomly sampled target orientation from SO ⁡ ( 3 ) \mathrm{SO}(3) .

[175] p: Baselines. We compare against the Base representation [ 52 ] , which encodes the pose, velocity, and proprioceptive state of both hands and the object. We then enhance this with DexRep in three configurations: Ours-Throw (DexRep for throwing hand), Ours-Catch (DexRep for catching hand), and Ours-Dual (DexRep for both).

[176] p: Dataset. To evaluate generalization, we extend the single-object setup in [ 52 ] by training with 9 YCB objects and testing on 8 unseen ones, as shown in Fig. 8 .

[177] figure: Figure 8 : 17 Objects used in Handover. The objects in the first row are used in training (seen), while the rest are for evaluation (unseen).

[178] p: Network Architecture. The Base representation, also known as the robotic state f p ​ r ​ o ​ p f_{prop} , consists of the pose, velocity, joint angles, joint forces of both robotic hands, and the pose, velocity, angular velocity and target pose of the object. The single-layer FC layer processes the robotic static and DexRep inputs, with input sizes of 338, 1080, 1280, 1080, and 1280 corresponding to f p ​ r ​ o ​ p f_{prop} , { f o , f s } \{f_{o},f_{s}\} , f l f_{l} , { f o ′ , f s ′ } \{f_{o}^{\prime},f_{s}^{\prime}\} , and f l ′ f_{l}^{\prime} respectively, and an output size of 128. The policy π θ \pi_{\theta} is an MLP with hidden layers [ 1024 , 1024 , 512 ] [1024,1024,512] and uses the Elu activation function after each layer. The policy outputs 𝐚 ∈ ℝ 20 \mathbf{a}\in\mathbb{R}^{20} containing 20 joint action.

[179] p: Training Details. DexRep is computed with voxel size l v = 0.02 l_{v}=0.02 m and surface range σ m ​ a ​ x = 0.2 \sigma_{max}=0.2 m (Based on ablation in Sec. VII-G ). We use 4000 parallel environments and run 4000 iterations of PPO training, requiring approximately 42 GPU hours on a single RTX 3090.

[180] p: Evaluation Metric. We use the success rate and the mean reward as evaluation metrics. The handover task is considered successful when the difference between the current and target position of the object d o → t d_{o\rightarrow t} is less than 0.02 m [ 52 ] . The mean reward is calculated as the mean cumulative reward in the most recent 200 successful manipulation trajectories.

[181] h4: VI-C 2 Quantitative Results and Analysis

[182] p: As shown in Table II and Fig. 6 (right), DexRep significantly improves the learning and performance of handover policies across all settings.

[183] p: Ours-Dual achieves the highest success rate: 81.5% on seen and 77.3% on unseen objects, surpassing the Base method by 38.4% and 40.5% . This demonstrates the benefit of incorporating structured hand-object interaction features on both sides of a bimanual task.

[184] p: We also observe that Ours-Catch consistently outperforms Ours-Throw . This aligns with task dynamics: catching requires more precise control and tactile feedback, making high-quality contact modeling crucial. By contrast, the throwing hand mainly sets the trajectory, which is more tolerant of errors.

[185] p: These results affirm that even in dual-arm settings, DexRep offers transferable and composable representations that enhance control performance. The consistent improvement from Base → \rightarrow Throw/Catch → \rightarrow Dual validates that the representation quality directly correlates with policy success. Moreover, the strong performance on unseen objects underscores DexRep’s generalization capability in tasks requiring coordinated dynamic interaction between multiple effectors.

[186] h2: VII Analyzing the Effectiveness of DexRep

[187] p: To comprehensively evaluate the proposed representation DexRep and understand its behavior across different conditions, we design a series of experiments aimed at answering the following questions:

[188] p: Component Contribution: How does each component of DexRep contribute to the learning performance and generalization capability in manipulation tasks?

[189] p: Partial Observation Robustness: Can DexRep maintain its effectiveness when only partial point cloud observations—common in real-world setups—are available?

[190] p: Pretraining Data Efficiency: How does the scale of pretraining data affect the feature quality and downstream performance of DexRep?

[191] p: Multi-Hand Applicability: Is DexRep adaptable to dexterous hands with different morphologies while preserving its performance?

[192] p: Training Diversity Impact: How does the number of training objects affect the generalizability of the learned policies?

[193] p: Friction Robustness: Does DexRep generalize well under varying object friction coefficients?

[194] p: Feature Parameter Sensitivity: How do different combinations of voxel edge length and maximum perception distance affect the effectiveness of DexRep across tasks?

[195] figure: Figure 9 : 40 Objects used in Grasping for analyzing the effectiveness of DexRep. The first 10 objects are from GRAB [ 50 ] , while the rest are from 3DNet [ 61 ] .

[196] p: All experiments from Sec. VII-A to Sec. VII-D are conducted using the grasping task, with the experimental setup detailed in Section VI-A1 . Specifically, we train policies on 40 seen objects from GRAB [ 50 ] and evaluate them on 10 unseen objects from GRAB and 30 unseen objects from 3DNet [ 61 ] , as illustrated in Fig. 9 . In the following experiments, we denote the three testing object sets as GRAB (seen), GRAB (unseen), and 3DNet (unseen) . The other experiments are performed under the setup in Isaac Gym. The following subsections present the results and analyses corresponding to the above questions.

[197] figure: Figure 10 : Statistical analysis of success rates across random seeds and datasets. (a) Box plots illustrate the distribution of success rates over multiple training seeds for each method and dataset, where the box boundaries correspond to the 25th and 75th percentiles and the central line denotes the median (50th percentile). (b) Bar plots report the mean success rate and 95% confidence intervals (CIs).

[198] figure: Figure 11 : Success rate (%) of our method and its variants during training. The x-axis represents the training iterations. The shaded area represents the standard deviation.

[199] h3: VII-A Effectiveness of each component of DexRep

[200] p: We conduct ablation studies to evaluate the effectiveness of each component in DexRep and to investigate how different combinations of features influence policy learning and generalization.

[201] p: Hand2obj: Encodes only the relative hand-object position, following DAPG [ 1 ] .

[202] p: pGlo: Global shape features extracted by a pretrained PointNet [ 15 ] , as used in ILAD [ 2 ] .

[203] p: Surf , Occ , LGeo : Variants that use only one of the proposed surface, occupancy, or local geometry features, respectively.

[204] p: Surf+LGeo , Occ+LGeo , Surf+Occ : Pairwise combinations of the above.

[205] p: Occ+Surf+pGlo : Combines the proposed features with global shape features.

[206] p: DexRep+pGlo : Adds global PointNet features to the full DexRep.

[207] p: DexRep (ours) : Full representation comprising Surf + Occ + LGeo .

[208] p: The evaluation results on seen and unseen objects, together with the statistical analysis across random seeds, are presented in Fig. 10 . The figure reports both the empirical distributions of success rates and the corresponding mean with 95% confidence intervals (CIs). Non-overlapping confidence intervals indicate statistically significant performance differences ( p < 0.05 p<0.05 ). For methods exhibiting higher variance (e.g., Hand2obj, pGlo, and Occ), we conduct 20 independent runs to obtain a more reliable estimate of their performance distribution. Fig. 11 shows the training curves of all baselines.

[209] h4: VII-A 1 Individual Feature Effectiveness

[210] p: Among the single-feature variants, Surf achieves the highest grasping success rate on unseen objects (93.5%) and 3DNet (87.1%). This feature encodes surface distances and normals of the closest points between hand key points and the object, offering a contact-centric geometric signal that is directly relevant to manipulation. In contrast, Occ (coarse hand-centered occupancy) and LGeo (local shape patches) underperform in isolation but prove highly effective in combination with other cues. This suggests Surf is the most dominant standalone cue, while the others provide complementary information.

[211] figure: Figure 12 : T-SNE projection and grasping success rates of object categories. Global features extracted using PointNet [ 15 ] are visualized via t-SNE over objects sampled from DexGraspNet [ 7 ] . Color indicates object category, while grasp success rate is visualized by shading. Notably, objects with similar global features (e.g., pistol, ipod) exhibit different grasp success rates.

[212] h4: VII-A 2 Complementarity

[213] p: Pairwise combinations improve performance over single-feature variants, but none match the full DexRep ( Surf+Occ+LGeo ), which achieves 96.6% success on unseen objects and 97.6% on 3DNet. The performance gap reveals how each component captures distinct and non-redundant aspects of hand-object interaction: Surf offers fine-grained distance-local geometry; Occ captures coarse volumetric occupancy relative to the hand; LGeo encodes more abundant local geometry via local patch descriptors. For example, Surf+LGeo lacks volumetric contact context ( Occ ), which may degrade performance in tasks where global pose is critical. Surf+Occ has global representation and a simple surface normal descriptor, but lacks higher-order local descriptors for more complex surfaces, while the higher-order local descriptor in LGeo+Occ requires pretraining, which may not generalize to unseen local geometry well. Only when all three are combined does the policy consistently generalize across object categories and shape variations. DexRep thus forms a hierarchical spatial representation, spanning closest contact points to local and global object configurations.

[214] h4: VII-A 3 Local vs. Global Representations

[215] p: When comparing LGeo with pGlo , the local representation demonstrates faster convergence during training (Fig. 11 ). From the testing results (Fig. 10 ), models using local representations also exhibit more stable performance and consistently higher success rates, exceeding pGlo by more than 40%. Additionally, adding global object features (pGlo) consistently degrades performance. For instance, Occ+Surf+pGlo yields a 20% drop on unseen objects compared to Occ+Surf , and DexRep+pGlo underperforms relative to DexRep . This reflects a critical insight: while global object embeddings may help in object recognition, they are often detrimental for fine-grained contact reasoning due to their sensitivity to global pose, scale, and articulation variability. In contrast, LGeo features—though also geometry-driven—are computed locally around anticipated contact regions, offering richer interaction-relevant cues. For example, when grasping diverse mugs or tools with similar handles but different bodies, LGeo enables the policy to generalize contact behavior across instances despite dissimilar global shapes. This validates the hypothesis that local geometry is more transferable and robust for dexterous manipulation than object-level embeddings.

[216] h4: VII-A 4 Sample Efficiency

[217] p: In reinforcement learning, sample efficiency, or convergence speed, is important in dexterous manipulation tasks due to their high-dimensional action spaces and complex contact dynamics [ 9 , 1 , 52 , 2 ] . Sample efficiency can be reflected in the number of environment interactions (i.e., samples) required for a policy to reach optimal performance. In Fig. 11 , DexRep has converged in 600 iterations, demonstrating efficient learning compared with other representations, which remain far from convergence even at iteration 600. Particularly for the global PointNet feature, the success rate of the policy at iteration 200 is close to 0 while DexRep reaches 60%. While it is possible that these alternative representations may eventually converge to better performance if trained for substantially longer, the amount of computation resources required is significant. Our results highlight that DexRep achieves strong task performance with notably better sample efficiency, which is critical for the practical deployment of dexterous policies.

[218] h4: VII-A 5 Failure Cases

[219] p: To better understand the factors that affect robotic grasping success, we perform a t-SNE 2D projection of the global features of different object categories and analyze the failure and success cases. The analysis reveals that objects with similar features may exhibit different grasping success rates, as shown in Fig. 12 . The grasping failure cases shown in the figure (e.g., sodacan, coin, ipod, pistol) and the grasping success cases (e.g., milkcarton, cellphone, ipod, pistol) are positioned closely in the t-SNE 2D projection, yet their grasping success rates differ significantly. This indicates that even when the global features of objects are similar, specific shape details and object properties (such as size and thickness) can significantly impact the grasping success rate.

[220] h3: VII-B DexRep Robustness to Partial Point Clouds

[221] p: Although DexRep demonstrates strong performance in both training and generalization, the above experiments assume access to complete object point clouds, which typically require multi-camera setups and careful occlusion handling in real-world scenarios. In contrast, most practical systems rely on single-view depth sensors, resulting in partial and noisy observations, especially in hand-object interaction tasks where occlusion is prominent.

[222] p: To evaluate the applicability of DexRep in such settings, we conduct experiments using partial point clouds as input. Specifically, we simulate a depth camera in MuJoCo and generate noisy partial point clouds from fixed first- or third-person viewpoints. After preprocessing, we estimate normals using the KDTreeSearchParamHybrid algorithm 1 1 1 https://www.open3d.org/docs/latest/python_api/open3d.geometry.KDTreeSearchParamHybrid.html , and compute DexRep features following the same procedures as with full point clouds. We refer to these experiments with the prefix Ours , while the baseline uses global features extracted by a pretrained PointNet [ 15 ] , labeled as pGlo . Specifically, Ours-Part-1st and pGlo-Part-1st use a first-person camera perspective; Ours-Part-3rd and pGlo-Part-3rd use a third-person view; Ours-Full and pGlo-Full use complete point clouds.

[223] figure: Figure 13 : Success rate (%) and mean reward of our method and its variants during training. The y-axis indicates the success rate and mean reward during training, and the shaded area represents the standard deviation.

[224] figure: Figure 14 : Test success rate (%) of our method applied to partial point clouds. We visualize both (a) the empirical distributions of success rates across random seeds and (b) the corresponding mean success rate with 95% confidence intervals.

[225] p: All experiments are trained from scratch with DexRep using the pre-trained PointNet encoder. Notice that we can use a teacher-student strategy [ 62 ] to distill the policies using full point cloud to those using partial point cloud to improve the success rate for partial point clouds, but to demonstrate the robustness of DexRep without other intervening factors, we adopt the training from scratch for a fair comparison with full point clouds. The success rate and the mean reward during the training process are shown in Fig. 13 (left). The experimental results demonstrate that DexRep possesses a certain degree of robustness to both the completeness of point clouds and the perspective from which they are captured. The grasp success rate in the partial point cloud scenario with a fixed viewpoint can reach about 70%. Changing the viewpoint only causes a tiny fluctuation in training. pGlo also shows some robustness to point cloud completeness, but is sensitive to viewpoints.

[226] p: We also report evaluation results with both the empirical distributions of success rates (Fig. 14 (a)) and the corresponding mean success rate with 95% confidence intervals (Fig. 14 (b)) on test sets. In Fig. 14 (a), the variance of our policies using different seeds is very small, indicating that all of the seeds of our policies achieve a consistently high success rate. In Fig. 14 (b), although the performance slightly decreases compared with Ours-Full , Ours-Part-1st and Ours-Part-3rd views achieve mean success rates of around 85% on unseen objects. This demonstrates that our method generalizes well to partial point clouds, which can be applied to real-world robotic platforms and indicates a smaller sim-to-real gap. Additionally, it shows that the viewpoint of the point cloud has little impact on the grasp success rate, allowing flexible camera placement.

[227] p: For pGlo , the average success rates of different runs on unseen objects decrease when changing from full to partial point cloud observations. In the Fig. 14 (b), the mean success rate of pGlo-Full is consistently higher than that of pGlo-Part-3rd . On the other hand, in Fig. 14 (a), pGlo-Full shows high variance of different runs that some runs are higher than 60% while some lower than 20%, indicating less stable training. However, pGlo-Part-3rd maintains smaller variance. Therefore, in addition to the comparison based on the mean success rate, we conduct independent two-sample t-tests for the results across the three datasets, which yield p-values of 0.028, 0.035, and 0.221, respectively. The p-values indicate that the difference is statistically significant for the GRAB (seen) and GRAB (unseen) datasets (p < < 0.05), while for 3DNet (unseen) the two methods perform comparably. We can also see from Fig. 14 , the success rates in the third view ( pGlo-Part-3rd ) are higher than those in the first view, which may be attributed to the fact that the third view can observe more areas to be contacted and therefore help more in the contact reasoning when hands approach objects.

[228] h3: VII-C Pretrain Data Volume Impact on DexRep Efficacy

[229] p: To evaluate how the scale of pretraining data influences the representational quality and downstream policy performance of DexRep, we conduct experiments by pretraining the Loc-Geo feature extractor (PointNet [ 15 ] ) on 5k , 25k , and 50k objects randomly sampled from ShapeNet55 [ 47 ] . After pretraining, we use the resulting encoders to train grasping policies on GRAB objects, and evaluate them on both seen and unseen object sets. As shown in Fig. 13 (right), policies pretrained with larger object sets converge faster and achieve higher final rewards. Table III summarizes the test success rates across multiple datasets.

[230] h4: VII-C 1 Performance Gains with More Pretraining Data

[231] p: DexRep exhibits strong generalization even when pretrained on a relatively small dataset of 5K objects—achieving 92.1% on GRAB unseen, 92.4% on 3DNet, and 77.9% on DexGraspNet. These results indicate that DexRep is capable of capturing transferable local geometric patterns with limited pretraining data. Across all settings, increasing the number of pretraining objects improves success rates. For instance, on GRAB seen objects, the success rate increases from 89.3% with 5k to 96.5% with 50k objects. Similar trends hold for GRAB unseen (92.1% → 96.6%) and 3DNet (92.4% → 97.6%). Notably, performance on the large-scale DexGraspNet benchmark improves from 77.9% to 88.1%. This consistent improvement confirms that larger pretraining sets enhance the geometric encoding capacity of the Loc-Geo module. A more diverse pretraining dataset allows the model to extract richer and more transferable local features, which are crucial for reliable grasp synthesis across a variety of shapes.

[232] h4: VII-C 2 Stability Across Random Seeds

[233] p: Another observation is the notable reduction in standard deviation with larger pretraining sets. For example, on GRAB seen objects, the standard deviation drops from 4.5% (5k) to 0.9% (50k). This indicates that larger pretraining datasets lead to more stable policies across seeds, which is essential for consistent real-world deployment.

[234] figure: Table III : Test success rate (%) of our method with different numbers of pretraining objects. We test on 50 objects from GRAB [ 50 ] , 30 unseen objects from 3DNet [ 61 ] and 5355 objects from DexGraspNet [ 7 ] . Testing Object Sets 5k 25k 50k GRAB (seen) 89.3 ± \pm 4.5 90.0 ± \pm 4.8 96.5 ± \pm 0.9 GRAB (unseen) 92.1 ± \pm 5.0 93.9 ± \pm 0.9 96.6 ± \pm 0.4 3DNet (unseen) 92.4 ± \pm 4.0 93.7 ± \pm 4.2 97.6 ± \pm 0.9 DexGraspNet (unseen) 77.9 ± \pm 4.2 81.2 ± \pm 2.9 88.1 ± \pm 2.0

[235] h3: VII-D Influence of Multi-morphology Robotic Hands

[236] figure: Table IV: Grasp success rate (%) on unseen objects using robotic hands with different numbers of fingers. # Fingers Hand2obj pGlo Ours 2 10.2 37.5 65.4 3 18.7 51.1 78.2 4 15.3 23.8 81.5

[237] figure: Figure 15 : Examples of grasping unseen objects using robotic hands with different numbers of fingers.

[238] p: To evaluate the adaptability of DexRep across robotic hands of different morphologies, we conduct experiments with a set of hands derived by selectively disassembling fingers from a standard five-fingered hand, following the procedure in [ 63 ] . Examples of these hand configurations are shown in Fig. 15 . Table IV reports the success rates of grasping unseen objects using policies trained on each hand morphology. We compare our full DexRep representation with two baselines: Hand2obj , which uses only relative hand-object position, and pGlo , which leverages global object features extracted by PointNet.

[239] p: Across all hand morphologies, our method consistently outperforms the baselines by large margins. In particular, DexRep achieves success rates of 65.4% with a 2-finger hand, 78.2% with a 3-finger hand, and 81.5% with a 4-finger hand. These results demonstrate that DexRep generalizes effectively to different hand designs and control spaces, even when the number of available contacts is reduced. In contrast, Hand2obj and pGlo perform poorly under morphology changes, suggesting they lack the fine-grained interaction representations needed to support robust policy transfer. The strong cross-morphology performance of DexRep highlights the modularity and reusability of its representation. Since DexRep encodes interaction-relevant local geometry and spatial structure rather than hand-specific motor signals, it enables efficient policy learning even for novel hand designs.

[240] h3: VII-E Impact of the Number of Trained Objects in RL

[241] figure: Figure 16 : Success rates (%) on test objects with varying numbers of training objects. The x-axis is logarithmically scaled to represent the number of training objects. The y-axis shows the mean success rate, and the error bars indicate the standard deviation.

[242] p: To investigate how the diversity of training objects influences policy generalization, we migrate our learning pipeline to Isaac Gym [ 58 ] , which supports scalable parallel training, overcoming the limitations of MuJoCo [ 55 ] in large-scale object scenarios. We conduct reinforcement learning experiments using DexRep on five object set sizes: 20, 40, 200, 500, and 900 training objects. All policies are evaluated on a fixed set of unseen test objects used in prior works [ 6 , 8 ] . The results are presented in Fig. 16 .

[243] p: As the number of training objects increases, the policy’s generalization performance consistently improves, indicating that object diversity enhances the robustness of learned interaction strategies. Notably, performance gains become marginal beyond 200 training objects, suggesting diminishing returns with further data scaling. This saturation implies that most of the structural variations needed for effective grasping can already be captured with a moderately sized training set. These results confirm that while large-scale object diversity is beneficial, DexRep-based policies can achieve strong generalization with a relatively compact object set, making them practical for deployment in settings with limited access to extensive training assets.

[244] h3: VII-F Robustness to Object Friction Coefficients

[245] p: Friction is a critical physical property that directly influences hand-object contact stability and thus the success of manipulation policies. To assess the robustness of DexRep under varying contact conditions, we follow the setup of UniDexGrasp [ 6 ] and conduct experiments in Isaac Gym [ 58 ] with different object friction coefficients. We evaluate policies trained on 200 objects (based on results from Sec. VII-E ) using five different friction settings: fixed values of 1.0, 0.8, 0.6, 0.4, and 0.2, along with a randomized friction scenario where the coefficient is uniformly sampled in the range [ 0.0 , 1.0 ] [0.0,1.0] . The results are summarized in Table V .

[246] p: The results show that DexRep consistently maintains high grasping success across a broad range of friction coefficients. As expected, lower friction values lead to a decline in success rates due to reduced contact stability. However, even under a challenging low-friction setting of 0.2, the policy still achieves a success rate of 82.9%, reflecting strong robustness. In the random-friction setting, which simulates real-world variability, DexRep attains 90.8% success, only slightly lower than the performance under fixed moderate friction values. These findings suggest that DexRep captures contact-relevant geometric cues that generalize well across diverse physical environments, reducing the need for fine-tuned physical calibration during deployment.

[247] figure: Table V : Success rates (%) on test objects under different object friction coefficients. Object Friction Coefficient 1.0 0.8 0.6 0.4 0.2 [ 0 ∼ 1.0 ] [0\sim 1.0] (random) 96.4 93.1 91.9 91.5 82.9 90.8

[248] h3: VII-G Ablation on Voxel Edge Length l v l_{v} and Maximum Distance σ m ​ a ​ x \sigma_{max}

[249] p: The proposed Surface and Occupancy features in DexRep rely on two spatial hyperparameters: the voxel edge length l v l_{v} and the perception threshold σ m ​ a ​ x \sigma_{max} . These parameters define the geometric resolution and spatial range of local interaction encoding. To assess their influence, we conduct an ablation study across a range of values relevant to each manipulation task. Results are shown in Table VI .

[250] figure: Table VI : Success rates (%) on unseen objects with different edge lengths of voxel l v l_{v} ( m m ) and the maximum distance σ m ​ a ​ x \sigma_{max} ( m m ) . The bolded settings are used for the main experiments. Grasping Edge Length of Voxel l v l_{v} 0.01 0.01 0.01 0.015 0.015 0.015 0.02 0.02 0.02 Maximum Distance σ m ​ a ​ x \sigma_{max} 0.1 0.15 0.2 0.1 0.15 0.2 0.1 0.15 0.2 Mean Success Rate 93.4 93.2 92.1 92.8 93.7 94.0 94.3 93.5 96.4 In-Hand Orientation Edge Length of Voxel l v l_{v} 0.01 0.01 0.01 0.015 0.015 0.015 0.02 0.02 0.02 Maximum Distance σ m ​ a ​ x \sigma_{max} 0.1 0.15 0.2 0.1 0.15 0.2 0.1 0.15 0.2 Mean Success Rate 86.0 83.9 76.2 83.5 78.1 74.8 84.7 77.1 75.3 Handover Edge Length of Voxel l v l_{v} 0.01 0.01 0.01 0.02 0.02 0.02 0.03 0.03 0.03 Maximum Distance σ m ​ a ​ x \sigma_{max} 0.1 0.2 0.3 0.1 0.2 0.3 0.1 0.2 0.3 Mean Success Rate 76.5 75.6 75.8 75.9 77.3 75.6 74.6 74.7 72.2

[251] p: In the ablation study, the value ranges of σ m ​ a ​ x \sigma_{max} and l v l_{v} are deliberately set to cover near-limit cases in the task context. For example, in the in-hand reorientation task, objects are initialized 0.1 m above the hand, and the distance between hand and object rarely exceeds 0.2 m; setting a voxel length l v l_{v} of 0.03 m results in an overly coarse object volume.

[252] p: As shown in Table VI , when these hyperparameters are within reasonable ranges, DexRep remains robust. However, two cases show clear sensitivity: (1) in the in-hand reorientation task, using a very large σ m ​ a ​ x \sigma_{max} lowers success rates because object distances greater than 0.1–0.2 m are rare, making it hard for the policy to learn from such infrequent values. Thresholding large distances to σ m ​ a ​ x \sigma_{max} reduces input variation and eases learning; also unseen values at test time are avoided, which helps the generalization. (2) In the handover task, a very large l v l_{v} degrades performance because when the voxel edge length approaches the object’s size, the global occupancy feature becomes too coarse to reliably encode the object’s pose for catching.

[253] p: Based on these observations, we provide a practical guideline: for general tasks, a voxel edge length between 0.01 m and 0.02 m with a maximum perception distance σ m ​ a ​ x \sigma_{max} of about 0.1 m is recommended. For in-hand tasks that require precise local manipulation, setting l v l_{v} to 0.01 m and σ m ​ a ​ x \sigma_{max} to 0.1 m is suggested to balance detail and generalization.

[254] h2: VIII Application of DexRep in Real-world Scenarios

[255] h3: VIII-A System Setup and Real-world Experiment Settings

[256] p: To validate the effectiveness of DexRep in real-world scenarios, we built a grasping system comprising an Allegro Hand 2 2 2 https://www.wonikrobotics.com/research-robot-hand , a Unitree Z1 arm 3 3 3 https://www.unitree.com/arm/ , and an Azure Kinect DK 4 4 4 https://azure.microsoft.com/en-us/products/kinect-dk , as shown in Fig. 17 . The joint angles of both the arm and the hand are obtained via their respective motor encoders and used to compute the spatial pose of the dexterous hand. Scene depth information is captured by the Azure Kinect DK, from which the object point cloud is segmented. This segmented point cloud, together with the estimated hand pose, is used to compute the DexRep representation. The grasping policy is trained entirely in simulation, with domain randomization applied to promote robustness. Before deployment on the real robot, we calibrate the spatial alignment between the depth camera and the robot by using a checkerboard pattern. Specifically, the checkerboard is fixed on the base of the robotic arm, enabling us to compute the transformation from the camera coordinate frame to the robot base frame. This ensures that the point cloud data from the depth camera is consistently aligned with the robot’s coordinate system and the estimated hand pose. To validate generalization to real-world objects, we evaluate the best-performing policy among three runs on eight 3D-printed objects that are not used during simulation training. Each object is tested over 15 trials to compute the grasping success rate.

[257] figure: Figure 17 : The grasping platform with an Allegro Hand v4, a Unitree Z1 arm and an Azure Kinect DK.

[258] h3: VIII-B DexRep Extraction from the Real-world Setup

[259] p: In our real-world system, DexRep is computed using readily accessible sensor inputs. Specifically, the joint angles of the robotic hand, denoted by θ \theta , are obtained directly from motor encoders, while the object’s point cloud O O (either full or partial) is captured via a depth camera. Surface normals n o n_{o} of the object are estimated using the KDTreeSearchParamHybrid algorithm, with a search radius of 0.03 and up to 250 nearest neighbors.

[260] p: Given these inputs, we employ a forward kinematics model 𝒦 ⁡ ( θ ) \mathcal{K}(\theta) to derive the following outputs: 1) The pose of the root joint of the middle finger, p mroot p_{\text{mroot}} , which serves as the spatial anchor for the Occupancy Feature; 2) The positions of predefined keypoints on the hand, denoted as P P , which are used to compute the Surface and Local-Geo Features.

[261] p: The DexRep representation is then computed through the following three components:

[262] p: Occupancy Feature: A voxel grid is centered at p mroot p_{\text{mroot}} to capture the local spatial occupancy of the object near the hand. Using the point cloud O O , we determine the occupancy status of each voxel according to Eq. 6 , resulting in the occupancy feature f o f_{o} .

[263] p: Surface Feature: This component encodes the spatial relationship between the hand and the object by computing the distance and normal vectors from each hand keypoint in P P to its nearest object point. These are computed using O O and the estimated surface normals n o n_{o} , following Eq. 7 , yielding the Surface Feature f s f_{s} .

[264] p: Local-Geo Feature: To capture fine-grained local geometric characteristics in potential contact regions, the object point cloud O O is first normalized and then passed through a pretrained PointNet encoder E ⁡ ( O ) E(O) . For each keypoint in P P , the closest object point is identified, and its corresponding PointNet feature is extracted to obtain the local geometry feature f l f_{l} .

[265] h3: VIII-C DexRep with Known CAD Models

[266] p: In this experiment, we assume that object CAD models are available. Consequently, only the 6D poses of the objects are required for grasping, and these poses are obtained by registering the CAD models to the partial point clouds captured by the Azure Kinect DK’s depth sensor. Specifically, objects are segmented from RGB images (recorded against a green background and calibrated with the depth sensor), and the segmented depth images are backprojected into 3D space to yield partial point clouds. To compute DexRep features, we align the observed point cloud with the canonical CAD model. Specifically, we adopt the Fast Point Feature Histogram (FPFH)-based registration pipeline provided by Open3D 5 5 5 https://www.open3d.org/html/python_api/open3d.pipelines.registration.registration_ransac_based_on_feature_matching.html#open3d-pipelines-registration-registration-ransac-based-on-feature-matching . The algorithm extracts FPFH features from both the observed partial point cloud and the model point cloud, and estimates the rigid-body transformation between them through RANSAC-based correspondence matching. The resulting transformation is used to align the CAD model to the observed object pose. To mitigate the impact of pose registration errors, we add Gaussian noise with a standard deviation of 2 ​ cm 2\,\text{cm} for position and 0.1 ​ rad 0.1\,\text{rad} for rotation during policy training in the MuJoCo simulator. As shown in Table IX , our method outperforms the baselines and exhibits an outstanding generalization of unseen objects in real-world experiments under the assumption of known CAD models.

[267] h3: VIII-D DexRep with Partial Point Cloud

[268] p: In unstructured real-world environments, acquiring complete object point clouds is often infeasible due to occlusions and sensor limitations. To assess the robustness of DexRep under partial observability, we evaluate its performance in dexterous grasping tasks using partial point clouds. Following the procedure in Sec. VII-B , we train grasping policies in MuJoCo using partial point clouds. To simulate real-world sensor noise, we add Gaussian noise with a standard deviation of 2 ​ mm 2\penalty\ \mathrm{mm} to the rendered depth images during training, which are then back-projected to generate point clouds.

[269] p: The trained policies are deployed on our physical system and evaluated on 8 unseen 3D-printed objects. As shown in Table IX , DexRep consistently outperforms baseline methods under both first-person and third-person views. However, its performance slightly degrades compared to the full point cloud scenario, highlighting the challenges posed by partial observations. To mitigate this issue, we adopt a policy distillation strategy following [ 9 ] , using DAgger [ 62 ] to transfer the full point cloud policy to one that operates on partial point clouds. This approach enables efficient skill adaptation while preserving high grasp success rates, demonstrating that DexRep remains effective even under limited perceptual input.

[270] figure: Table VII : Success rate (%) for DexRep with known CAD models in the real world. Methods Camera Elephant Hand Binoculars Mug Toothpaste Apple Fryingpan AVERAGE Hand2obj-CAD 33.3 40.0 27.7 6.7 0.0 13.3 40.0 53.3 27.7 pGlo-CAD 86.7 80.0 60.0 66.7 33.3 80.0 60.0 26.7 61.7 Ours-CAD 100.0 66.7 66.7 86.7 86.7 93.3 100.0 60.0 82.5 Table VIII : Success Rate (%) for DexRep with partial point cloud in the real world. Polices directly deployed from training with partial observation and distilled from full observation are included. Ours-Full and pGlo-Full (our full point cloud policy and the full point cloud baseline with global features) are provided for reference. Direct Deploy Methods Camera Elephant Hand Binoculars Mug Toothpaste Apple Fryingpan AVERAGE pGlo-Part-1st 13.3 26.7 20.0 6.7 26.7 20.0 20.0 0.0 16.7 pGlo-Part-3rd 26.7 33.3 26.7 20.0 33.3 6.7 40.0 6.7 24.2 pGlo-Full 26.7 40.0 40.0 33.3 6.7 46.7 13.3 6.7 26.7 Ours-Part-1st 86.7 93.3 53.3 80.0 73.3 60.0 53.3 26.7 65.8 Ours-Part-3rd 93.3 80.0 66.7 86.7 73.3 53.3 60.0 46.7 70.0 Ours-Full 93.3 80.0 100.0 93.3 80.0 100.0 73.3 60.0 85.0 Distilled Ours-Part-1st 100.0 93.3 86.7 73.3 66.7 60.0 73.3 60.0 76.7 Ours-Part-3rd 100.0 100.0 86.7 93.3 80.0 60.0 60.0 53.3 79.2 Table IX : Success rates (%) for comparison between DexRep and Unidexgrasp++ [ 8 ] with an Allegro hand in Isaac Gym and real-world setup. Methods Camera Elephant Hand Binoculars Mug Toothpaste Apple Fryingpan AVERAGE Unidexgrasp++-Full-Sim 93.3 66.7 73.3 100.0 66.7 80.0 60.0 40.0 72.5 Ours-Full-Sim 100.0 93.3 100.0 93.3 86.7 100.0 86.7 60.0 90.0 Unidexgrasp++-Full 86.7 53.3 66.7 93.3 40.0 33.3 40.0 20.0 54.2 Ours-Full 93.3 80.0 100.0 93.3 80.0 100.0 73.3 60.0 85.0

[271] h3: VIII-E Full Point Cloud Policy Deployment Compared with SOTA

[272] p: Based on the results in Table I , UniDexGrasp++ [ 8 ] achieves the highest grasping success rate and is therefore selected as the baseline for our real-world evaluation. UniDexGrasp++ assumes access to a complete object point cloud; to meet this requirement, we deploy three Azure Kinect DK cameras to capture and segment the object point cloud on a tabletop setting. To ensure a fair comparison, we replicate the UniDexGrasp++ framework using the Allegro Hand in Isaac Gym and compare it against the DexRep policy trained under the same conditions. During simulation training, Gaussian noise with a standard deviation of 2 ​ mm 2\penalty\ \mathrm{mm} is added to point cloud observations, while noise with a standard deviation of 0.02 is added to the robot state—including hand joint angles, velocities, fingertip poses, global hand pose, and actions—to enhance robustness and reduce the sim-to-real gap.

[273] p: We evaluate both methods on 8 unseen 3D-printed objects. As shown in Table IX , our method outperforms UniDexGrasp++ by a significant margin of 30.8% in real-world success rate. In terms of sim-to-real transferability, UniDexGrasp++ exhibits a performance drop of approximately 18%, while DexRep only experiences a 5% decrease. This performance gap can be largely attributed to the differing robustness to real-world noise. While UniDexGrasp++ relies heavily on precise point cloud observations, our approach utilizes a coarse voxel-based encoding for global geometry, which is inherently more tolerant to sensor noise and point cloud imperfections, leading to more stable deployment performance in the real world.

[274] figure: Figure 18 : Point cloud visualization for ICP alignment and multi-camera fusion . (a) Point clouds sampled from the CAD model of a cup (GT); (b) GT with Gaussian noise; (c) GT and partial depth point cloud after ICP registration; (d) GT and point clouds merged from multiview depth images. In (a, c, d), points in blue represent GT and point in other colors represent partial depth points from different views.

[275] h3: VIII-F Discussion on Different Deployment Strategies

[276] p: An important observation arises when comparing the real-world deployment performance of different policy variants. Specifically, the success rate of the pGlo policy drops significantly when switching from CAD-based point clouds to full real-world point clouds (61.7% for pGlo-CAD vs. 26.7% for pGlo-Full , as shown in Table IX ). This substantial degradation highlights the sensitivity of global feature-based representations to real-world perception challenges, including: (1) structured, non-Gaussian noise introduced by commodity depth sensors, and (2) calibration inaccuracies inherent in multi-camera fusion setups. Fig. 18 visualizes this discrepancy by comparing synthetic CAD-sampled point clouds (with added Gaussian noise) (b) to fused point clouds captured from a 3D-printed object using three RGB-D cameras (d). The fused real-world point clouds exhibit incomplete surfaces and inter-view inconsistencies, leading to degraded geometric fidelity. These imperfections significantly impact representations such as pGlo, which rely on clean, complete object geometry to construct meaningful global features.

[277] p: In contrast, our DexRep-based policy demonstrates consistent performance across both point cloud modalities: both Ours-CAD and Ours-Full achieve a success rate of more than 80%. This stability reflects a core advantage of DexRep—its reliance on local, interaction-centric features rather than holistic object shape or precise CAD alignment.

[278] p: At the same time, we notice that Ours-Full achieves a slightly higher success rate than Ours-CAD , 85% vs 82.5%, which seems contradictory to the imperfect multiview point clouds discussed. Ours-Full has calibration errors from merging multi-camera input while Ours-CAD has registration error. The impact of registration error for CAD models on DexRep is different from the merging error. The registration error causes a global rotation and translation misalignment from the real observation, as can be seen from Fig. 18 (c) and the misalignment varies for different objects. When the misalignment is large, e.g. larger than 2 cm (our voxel length), the occupancy feature exhibits a large deviation from that of the ground truth point clouds and leads to a low grasp success rate for these objects. In contrast, the calibration error for the merged point clouds is the same for all objects and only a small misalignment occurs between the partial point clouds, which can be seen from the handle and edge of the cup in Fig. 18 (d). This small misalignment can be mitigated by the occupancy feature and local feature, and therefore, Ours-Full maintains higher performance in real-world experiments.

[279] p: In summary, the above results illustrate the robustness of the coarse and spatially structured encoding of DexRep: by representing geometry through voxelized occupancy and local proximity fields, DexRep maintains stable interaction representations even under significant sensor noise, occlusion, or registration error. These findings emphasize the practical resilience of DexRep in real-world manipulation scenarios. Its grounding in spatially local features enables policies to perform reliably without depending on precise CAD alignment or high-fidelity reconstructions, making DexRep particularly well-suited for deployment in unstructured or sensor-imperfect environments.

[280] h3: VIII-G Discussion: Extending to Other Tasks in the Real World

[281] p: Transferring the in-hand reorientation and handover tasks to the real world presents several additional challenges. The in-hand reorientation task and the handover task involve more complex finger coordination than the grasp task, and the latter also involves two manipulators operating in tight coordination. In these tasks, the objects are highly dynamic. Both the coordination and dynamics require high flexibility and control frequency of robotic hands for the real-world experiments, and low latency of the learned policy. More importantly, to deploy the proposed representation, the main challenge is the severe occlusion of dynamic objects, which renders different incomplete point clouds for the same object and challenges training the policies with the partial observation from scratch. To address the challenge, a distillation solution that is used in Sec. VIII-D is provided and verified in simulation.

[282] p: We conduct additional simulation experiments for both in-hand reorientation and handover using partial point clouds, which reflect realistic observation conditions in a real-world experiment. In the experiments, only an RGBD camera is placed in a third view. At each time step, the depth maps of objects are obtained by applying off-the-shelf segmentation techniques (e.g., SAM [ 64 ] ).

[283] p: Specifically, we employ DAgger [ 62 ] to distill partial-observation policies using DexRep from their full-observation counterparts. For the in-hand reorientation task, the distilled policy achieves a 76.3% success rate using partial point clouds. While the partial policy sees a drop (8.7%) from the full policy (85.0%), it demonstrates that meaningful control remains feasible even with sparse and noisy observations. The performance gap can be attributed to significant occlusions caused by fingers, which limit the visibility of object surfaces during manipulation. For the handover task, the occlusion is moderate, and therefore, the partial point cloud policy achieves 72.6% success, close to the 76.0% attained with full point cloud input.

[284] p: The main reason for the high success rate after distillation to partial observation is that although occlusion is significant due to the enclosure of the finger in the in-hand orientation task, the major contribution of DexRep to the performance is the local representation. The local representation can grant the policy performance in partial observations.

[285] h2: IX Conclusion

[286] p: In this paper, we propose a novel hand-object interaction representation for robotic dexterous manipulation, called DexRep, which consists of the Occupancy Feature, Surface Feature, and Local-Geo Feature. This representation captures the relative shape feature of the objects and the spatial relation between hands and objects during hand-object interactions, which makes the learned policy generalize to novel objects well. We embed DexRep into deep reinforcement learning to learn three dexterous manipulation tasks, including grasping, in-hand manipulation, and handover. We perform experiments comparing the state-of-art methods for each task. DexRep achieves the highest manipulation success rates in all tasks both in simulation and real-world experiments, which demonstrates that our method can effectively capture the representation of the hand-object relationship in various dexterous manipulation tasks and generalize to unseen objects. Additionally, we conduct a thorough performance analysis of our proposed method. The experimental results demonstrate the necessity of each module in our method and show that our method can handle various dexterous manipulation scenarios.

[287] p: Limitations and Future Work. While our method demonstrates strong performance in simulation and real-world experiments, several limitations remain. First, the representation relies on object point clouds to encode hand–object interactions, which makes it less robust in cases where depth information is unreliable (e.g., transparent, reflective, or dark objects, or under severe occlusions). For deformable objects, the observed geometry may change drastically across time steps, reducing the stability of the learned representation. Second, our experiments are limited to rigid objects, leaving open the question of generalization to soft or articulated ones. Addressing these challenges may require integrating complementary modalities (e.g., RGB images, tactile or force sensing) to compensate for unreliable depth, as well as developing deformation-aware representations to handle shape changes. Finally, extending evaluations to a wider range of real-world scenarios, especially those involving deformable and visually challenging objects, remains a promising direction for future work.

[288] h2: References

[289] figure: Qingtao Liu is pursuing a PhD at the College of Control Science and Engineering, Zhejiang University, under the supervision of Qi Ye and Jiming Chen. He graduated from China University of Geosciences (Wuhan) with a bachelor’s degree in 2021. His current research mainly focuses on dexterous manipulation and multimodal representation learning.

[290] figure: Zhengnan Sun received the B.S. degree from the College of Electronic Engineering of Zhejiang University, Hangzhou, China, in 2023. He is currently pursuing the Master’s degree with the College of Control Science and Engineering of Zhejiang University, Hangzhou, China. His research interests lie in robotic dexterous hands and multi-modal fusion.

[291] figure: Yu Cui is currently pursuing a Master’s degree at the College of Control Science and Engineering, Zhejiang University. Before that, she obtained her Bachelor’s degree from University of Science and Technology Beijing. Her research interests focus on robot learning and dexterous manipulation.

[292] figure: Haoming Li is currently pursuing a Ph.D. degree at the College of Control Science and Engineering, Zhejiang University. Before this, he obtained both his Bachelor’s and Master’s degrees from Shenzhen University. His research interests primarily focus on dexterous hand manipulation skill generation and motion planning.

[293] figure: Gaofeng Li (Member, IEEE) is currently a tenure-tracked professor under the Hundred Talents Program at Zhejiang University. He is the founder and director of the ARTs (Agile Robotic Tele-systems) Lab. His research interests include Lie Group in Robotics, Robotic Manipulation, Haptic Teleoperation, Imitation Learning, and Soft Robotics. He serves/served as a lead guest editor for the International Journal of Humanoid Robotics (IJHR), and the Late Breaking Report Chair for the Organizing Committee of IEEE RO-MAN 2024. He is also an independent Reviewer for IJRR, IEEE T-RO, IEEE T-ASE, IEEE/ASME T-Mech, IEEE RAM, IEEE RA-L, IEEE ICRA, IEEE IROS, etc.

[294] figure: Lin Shao is an Assistant Professor in the Department of Computer Science at the National University of Singapore (NUS), School of Computing. His research interests lie at the intersection of Robotics and Artificial Intelligence. His long-term goal is to build general-purpose robotic systems that intelligently perform a diverse range of tasks in a large variety of environments in the physical world. Specifically, his group is interested in developing algorithms and systems to provide robots with the abilities of perception and manipulation. He is a co-chair of the Technical Committee on Robot Learning in the IEEE Robotics and Automation Society and serves as the Associated Editor at ICRA 2024. His work received the Best System Paper Award finalist at RSS 2023. Previously, he received his PhD at Stanford University, advised by Jeannette Bohg. He received his BS from Nanjing University.

[295] figure: Jiming Chen is a Changjiang Scholars Professor with College of control science and engineering, Zhejiang University. Currently, he serves/served associate editors for ACM TECS, IEEE TPDS, IEEE Network, IEEE TCNS, IEEE TII, etc. He has been appointed as a distinguished lecturer of IEEE Vehicular Technology Society 2015, and selected in National Program for Special Support of Top-Notch Young Professionals, and also funded Excellent Youth Foundation of NSFC. He also was the recipients of IEEE INFOCOME 2014 Best Demo Award, IEEE ICCC 2014 best paper award, IEEE PIMRC 2012 best paper award, and JSPS Visiting Fellowship 2011. He also received the IEEE Comsoc Asia-pacific Outstanding Young Researcher Award 2011. He is a Distinguished Lecturer of IEEE Vehicular Technology Society (2015-2018), and a Fellow of IEEE. His research interests include networked control, sensor networks, cyber security, IoT.

[296] figure: Qi Ye is a Tenure-Track Professor under the Hundred Talents Program at Zhejiang University. Before joining Zhejiang University, she was a research scientist of Mixed Reality & AI Lab at Cambridge, Microsoft and obtained Ph.D. degree at Imperial College London. She is interested in and working on human-computer interaction, particularly vision understanding involving hands, and a more general setting where humans interact with the environment. She is passionate about 3D vision and its applications, particularly in Mixed/Augmented/Virtual Reality and automatic control.

[297] h2: Instructions for reporting errors

[298] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[299] p: Tip: You can select the relevant text first, to include it in your report.

[300] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[301] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
