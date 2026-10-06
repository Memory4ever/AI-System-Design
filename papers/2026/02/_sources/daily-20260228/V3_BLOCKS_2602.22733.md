[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Pixel2Catch: Multi-Agent Sim-to-Real Transfer for Agile Manipulation with a Single RGB Camera Thanks:

[3] h6: Abstract

[4] p: To catch a thrown object, a robot must be able to perceive the object’s motion and generate control actions in a timely manner. Rather than explicitly estimating the object’s 3D position, this work focuses on a novel approach that recognizes object motion using pixel-level visual information extracted from a single RGB image. Such visual cues capture changes in the object’s position and scale, allowing the policy to reason about the object’s motion. Furthermore, to achieve stable learning in a high-DoF system composed of a robot arm equipped with a multi-fingered hand, we design a heterogeneous multi-agent reinforcement learning framework that defines the arm and hand as independent agents with distinct roles. Each agent is trained cooperatively using role-specific observations and rewards, and the learned policies are successfully transferred from simulation to the real world.

[5] figure: Fig. 1: We propose Pixel2Catch , an RGB-only robotic catching system without explicit 3D position estimation. The system consists of a robot arm equipped with a multi-fingered hand and a single RGB camera. Inspired by human visual perception, object motion is inferred from pixel-level features in image space rather than metric 3D coordinates. Policies trained in simulation are transferred directly to the real robot without fine-tuning.

[6] h2: I Introduction

[7] p: When humans catch a thrown object, they do not rely on explicit 3D position values or precise metric representations of the object. Instead, they perceive the object’s motion by observing relative changes in its apparent position and size over time, and generate catching movements based on these visual cues. This highlights that dynamic catching can be achieved through the interpretation of visual motion patterns, rather than explicit estimation of the object’s 3D state.

[8] p: However, most prior studies on dynamic object manipulation have relied on the motion capture systems [ 1 , 2 , 3 , 4 , 5 ] or depth sensors [ 6 , 7 , 8 , 9 ] to estimate the object’s 3D position. While such sensing modalities enable explicit geometric measurements, the performance of the resulting control models is strongly influenced by sensor quality. In particular, accurately estimating 3D object positions in real-world environments is often more challenging than in simulation, which leads to a significant sim-to-real gap when transferring learned policies.

[9] p: Motivated by principles of human visual perception, this work proposes a dynamic catching framework that focuses on recognizing object motion through pixel-level visual cues observed in a single RGB image, rather than explicitly estimating the object’s 3D position. To extract such visual cues, we employ Segment Anything Model 2 (SAM 2) [ 10 ] , which provides robust object segmentation and enables the extraction of pixel-level information capturing relative changes in image space position and scale. By leveraging these relative visual changes over time, the proposed approach represents object motion without relying on precise metric measurements, making it less sensitive to sensor accuracy.

[10] p: In addition, to enable effective learning of grasping behaviors, we employ a multi-agent reinforcement learning (MARL) [ 11 ] framework. This design allows efficient control of high-DoF robotic systems, such as a robot arm equipped with a multi-fingered hand. While previous MARL studies [ 12 , 13 , 14 , 15 ] have primarily focused on cooperation among multiple robots with homogeneous structures, this work decomposes a single robotic system into heterogeneous agents by modeling the robot arm and the robot hand as independent agents. Through this heterogeneous MARL formulation, the arm and hand can be trained cooperatively with role-specific objectives, enabling stable and coordinated dynamic grasping.

[11] p: The proposed framework is first trained in a simulation environment that is designed to closely mirror the real robotic system. This enables the policies learned in simulation to be directly deployed on the physical robot without additional fine-tuning. In real-world experiments, the robot successfully catches objects thrown by a human using the learned policies. Furthermore, we evaluate the effectiveness of the proposed approach by comparing it against policies trained without pixel-level visual cues and those learned using a single-agent formulation.

[12] p: In summary, the main contributions of this paper are as follows:

[13] p: We propose a novel framework for dynamic dexterous manipulation that represents object motion using pixel-level features extracted from a single RGB camera.

[14] p: We adopt a single-stage heterogeneous MARL framework by decomposing a high-DoF robotic system into a robot arm and a multi-fingered hand, each trained with role-specific observations and rewards.

[15] p: Through system identification and domain randomization, we successfully transfer policies trained in simulation to the real world, demonstrating agile and stable catching of human-thrown objects using only RGB visual input.

[16] h2: II Related Work

[17] h3: II-A Perception and Manipulation for Dynamic Objects

[18] p: Robotic manipulation research has been studied across a wide range of scenarios, from static manipulation tasks in which the object is already held by the robot [ 16 , 17 ] or fixed at a specific location [ 18 , 19 , 20 ] , to dynamic manipulation tasks involving freely moving objects [ 21 , 22 ] . While static manipulation assumes that the object state does not change significantly over time, dynamic manipulation requires the ability to perceive and respond to continuous changes in the object’s position and state.

[19] p: Many prior studies on dynamic manipulation have focused on scenarios in which object motion is confined to a 2D plane. Examples include grasping objects moving along a conveyor belt [ 23 , 8 ] , objects following circular trajectories in a two-dimensional plane [ 24 ] , or objects rolling on a flat surface [ 25 ] . In these scenarios, object motion follows a relatively constrained pattern within the observation space, making the perception and control problems more tractable.

[20] p: To handle more complex scenarios, recent studies have extended dynamic manipulation to objects moving freely in 3D space, typically relying on position estimation methods to recognize object motion. One representative approach leverages RGB-D cameras. Huang et al. [ 7 ] and Zhang et al. [ 6 ] estimated the 3D coordinates of objects using RGB-D cameras and implemented policies for catching thrown objects in real-world environments. These methods segment the object using color-based segmentation, extract the corresponding depth values, and compute 3D coordinates using the camera’s intrinsic and extrinsic parameters. However, in real-world settings, accurate position estimation is often more challenging than in simulation, as it strongly depends on sensor reliability, which can lead to performance degradation.

[21] p: Another approach employs marker-based motion capture systems [ 26 , 27 , 28 ] . Chen et al. [ 2 ] and Tassi et al. [ 4 ] used such systems to collect human demonstrations and object trajectory data, which were then used to train control models. While this approach enables accurate position estimation, it requires attaching markers to the object and incurs high system setup costs, limiting its practicality in real-world applications.

[22] p: Overall, existing dynamic manipulation studies tend to rely on explicit position estimation or additional sensing modalities. In contrast, inspired by human visual perception, this work adopts an alternative approach that recognizes object motion using pixel-level visual information directly observed from a single RGB image, without explicitly estimating the object’s 3D position. This approach simplifies the input representation, reduces sensor dependency, and enables effective dynamic catching of thrown objects.

[23] h3: II-B Learning Frameworks for Catching Policy

[24] p: Previous studies on dynamic object catching have commonly employed a robotic arm equipped with a simple end-effector, such as basket or scoop-shaped designs, to train policies [ 2 , 29 , 30 , 31 , 4 , 32 ] . In these approaches, the catching process is determined by the approach trajectory of the robot arm, while the role of the end-effector is limited to passively receiving the object. As a result, the control problem is simplified around arm-level motion, allowing catching policies to be learned using a single control model.

[25] p: To encourage more human-like catching motions and to stably handle objects with diverse shapes, prior studies have explored systems equipped with multi-fingered hands [ 5 , 9 , 33 ] . For example, Zhang et al. [ 6 ] proposed a two-stage reinforcement learning framework in which the catching skill is learned in a sequential manner using a multi-fingered hand. While this approach achieves stable performance through staged learning, it typically requires stage-wise reward design and policy transfer between stages, leading to increased complexity in the training pipeline.

[26] p: In this work, we adopt a MARL approach as an alternative to such multi-stage learning schemes, aiming to learn a catching policy within a single training stage. Most existing MARL studies focus on cooperation among multiple robotic systems with homogeneous structures, such as UAV swarm control [ 34 ] , autonomous driving [ 13 ] , bimanual or multi-hand manipulation [ 14 , 15 ] , and cooperative control of multiple quadruped robots [ 35 ] .

[27] p: In contrast, our approach focuses on decomposing a single robotic system into heterogeneous components based on their functional roles, rather than coordinating multiple robots. Specifically, we model the robot arm and the robot hand as independent agents and design role-specific observations and reward functions for each agent. This formulation allows the arm agent to concentrate on motion control for approaching the object, while the hand agent focuses on forming stable grasps during the catching process. As a result, effective catching policies can be learned within a single training process, without requiring staged learning or policy transfer.

[28] figure: Fig. 2: Pipeline of the system and experimental setup. Each policy ( π a ​ r ​ m , π h ​ a ​ n ​ d \pi_{arm},\pi_{hand} ) operates on selected observations from two consecutive timesteps. Privileged information is used only during value network training. A single RGB camera is mounted 0.5 m behind and 2.2 m above the robot. The arm and hand are controlled by separate policies that are trained collaboratively to catch a thrown object.

[29] h2: III Robot System for Catching Thrown Objects

[30] h3: III-A Task Description

[31] p: The goal of this work is to control a robot arm and hand to stably catch a thrown object without dropping it. To achieve this, we decompose the catching task into two complementary roles: the arm positions the hand in a region suitable for catching, while the hand focuses on securely grasping the object.

[32] p: In real-world environments, unlike in simulation, obtaining precise 3D coordinates of a thrown object is challenging. Rather than relying on direct position measurements, we infer object motion from visual cues. Inspired by human perception, which interprets object motion through changes in size and position within the field of view, we extract pixel-level features from a single RGB image. By leveraging these visual features, our approach enables effective learning of catching policies without requiring explicit 3D object positions.

[33] h3: III-B Real-world Setup

[34] p: We constructed an experiment using a high-DoF robot system and a camera for catching thrown objects as follows:

[35] p: Arm. The Universal Robots UR5e, a 6-DoF robot arm, is utilized in this work. The robot is mounted on a table at a height of 0.81 m, and its initial posture is configured to ensure that the hand is oriented toward the expected trajectory of the object.

[36] p: Hand. The Allegro Hand is attached to the robot arm, with three joints fixed to simplify control and maintain grasp stability, as shown in Fig. 2 . As a result, 13 joints are controlled using a target joint position controller.

[37] p: Camera. A single RealSense D435 camera is fixed in the environment to provide a global view of the object’s overall motion. To mimic human visual perception, our system is designed to use only RGB images, without depth information.

[38] figure: Fig. 3: (a) Objects used for training (top), validation (middle) in simulation, and real-world experiments (bottom). (b) Random object trajectories generated in simulation, shown without robot motion to highlight object dynamics.

[39] h3: III-C Simulation Setup

[40] p: We develop our simulation environment using the NVIDIA Isaac Lab framework [ 36 ] to closely match the real robot system. The simulated robot employs a USD model identical to the real hardware, and the camera is modeled as a pinhole camera with the same field of view as the Intel RealSense D435 used in real-world experiments. To improve robustness to variations in object motion, we randomize the object’s initial state at the beginning of each episode, including its position, orientation, linear velocity, and mass (Fig. 3 (b)). During training, five objects with distinct geometries are used, and their scales are varied to encourage generalization across different shapes and sizes (Fig. 3 (a)). To align the simulation control loop with the real robot, we apply a control decimation of 4, resulting in a 30 Hz control policy operating on a 120 Hz physics simulation by repeating each selected action over four consecutive simulation steps.

[41] h2: IV Learning Catching Policies

[42] h3: IV-A Problem Formulation

[43] p: We formulate the catching task as a Multi-Agent Markov Decision Process (MAMDP). Control is decomposed between an arm policy π a ​ r ​ m \pi_{arm} responsible for positioning and a hand policy π h ​ a ​ n ​ d \pi_{hand} focused on grasping. Each policy π i ​ ( i ∈ { arm , hand } ) \pi_{i}(i\in\{\text{arm},\text{hand}\}) receives its own observation s t i s_{t}^{i} and selects an action a t i a_{t}^{i} to maximize its expected discounted return E ⁡ [ ∑ k = 0 T γ k ​ r k i ] E[\sum_{k=0}^{T}\gamma^{k}r_{k}^{i}] , where r k i r_{k}^{i} is the reward assigned to policy i i at timestep k k . An episode terminates if the object is dropped or the maximum timestep T T is reached. We utilize Multi-Agent Proximal Policy Optimization (MAPPO) [ 11 ] to train the policies π a ​ r ​ m \pi_{arm} and π h ​ a ​ n ​ d \pi_{hand} .

[44] h3: IV-B Pixel-level Features from a single RGB image

[45] p: Previous studies have commonly relied on additional sensing modalities to explicitly estimate the 3D position of objects. In contrast, we defined pixel-level features z p ​ i ​ x ​ e ​ l z_{pixel} extracted directly from RGB images to recognize object motion. z p ​ i ​ x ​ e ​ l z_{pixel} is constructed from visual cues computed from the image space corresponding to the target object. As illustrated in Fig. 4 , we extract the object’s image space center coordinates, width, and height. The horizontal and vertical components of the center represent the object’s relative lateral and vertical position, while the width and height encode scale changes that implicitly reflect variations in the distance between the robot and the object. Since pixel-level features from a single timestep are insufficient to capture object motion, we incorporate temporal differences between consecutive timesteps into z p ​ i ​ x ​ e ​ l z_{pixel} . This allows the policy to infer motion dynamics directly from relative visual changes.

[46] p: To improve robustness under real-world conditions, we introduce random perturbations of up to 5 pixels to the corner coordinates of the object region during training. This augmentation accounts for segmentation uncertainty caused by real-world visual variations.

[47] p: The resulting pixel-based feature vector is defined as:

[48] table: z p ​ i ​ x ​ e ​ l ∈ ℝ 6 = { c x , c y , Δ ​ c x , Δ ​ c y , Δ ​ w , Δ ​ h } z_{pixel}\in\mathbb{R}^{6}=\{c_{x},c_{y},\Delta c_{x},\Delta c_{y},\Delta w,\Delta h\} (1)

[49] p: Unlike approaches that employ high-dimensional latent representations from image encoders such as ResNet [ 37 ] , our method directly utilizes task-relevant visual quantities that can be extracted from raw images. This design choice reduces representation mismatch between simulation and real-world environments and improves learning efficiency by focusing on control-oriented visual information rather than generic semantic features.

[50] p: Finally, to address the sensitivity of color-based masking methods [ 7 , 6 ] to lighting changes and background complexity, we employ SAM2 [ 10 ] for object segmentation. SAM2 enables robust and consistent extraction of object regions across diverse lighting conditions and backgrounds, thereby providing stable pixel-level inputs for real-world deployment.

[51] figure: Fig. 4: Visualization of pixel-level features in simulation and real-world environments. A bounding box is generated around the object in the RGB image, from which the corner and center coordinates, as well as width and height, are extracted. The final input features include these values and their temporal differences.

[52] h3: IV-C State and Action Space

[53] p: As shown in Fig. 2 , each agent’s state includes pixel-level features z p ​ i ​ x ​ e ​ l ∈ ℝ 6 z_{pixel}\in\mathbb{R}^{6} , end-effector pose information p ​ o ​ s ​ e e ​ e ​ f ∈ ℝ 7 pose_{eef}\in\mathbb{R}^{7} , and agent-specific joint states ( q a ​ r ​ m ∈ ℝ 6 q_{arm}\in\mathbb{R}^{6} , q h ​ a ​ n ​ d ∈ ℝ 13 q_{hand}\in\mathbb{R}^{13} ) and actions ( a a ​ r ​ m ∈ ℝ 6 a_{arm}\in\mathbb{R}^{6} , a h ​ a ​ n ​ d ∈ ℝ 13 a_{hand}\in\mathbb{R}^{13} ), concatenated over two consecutive timesteps.

[54] p: The object’s position p o ​ b ​ j ​ e ​ c ​ t ∈ ℝ 3 p_{object}\in\mathbb{R}^{3} is not included in the policy input but is utilized solely for training the value network to enhance the generalization and stability of learning. To provide temporal context, each state space concatenates sequential observations over 2 consecutive timesteps. For the value network, the input additionally includes observations from both agents together with the object’s position, aggregated over 2 timesteps.

[55] p: Each agent’s policy network outputs an action that is used to control its corresponding robot system. For the arm, the action a a ​ r ​ m a_{arm} , generated by the arm policy π a ​ r ​ m \pi_{arm} , is added to the current joint positions and executed through a PD controller. For the hand, the action a h ​ a ​ n ​ d a_{hand} , produced by the hand policy π h ​ a ​ n ​ d \pi_{hand} , is rescaled according to the joint limits and used as the target joint position.

[56] h3: IV-D Reward Design for Multi-agent RL

[57] p: To effectively train role-specific agents, we design separate reward functions for the arm and hand policies. The arm policy π a ​ r ​ m \pi_{arm} is trained to control the robot arm, focusing on approaching the thrown object with the end-effector. In contrast, the hand policy π h ​ a ​ n ​ d \pi_{hand} is trained to control the robot hand to stably grasp the object without dropping it. The reward functions for the arm and the hand are formulated as follows:

[58] table: R t arm = r t ​ i ​ m ​ e + r dist palm + λ s ​ u ​ c ​ c ​ 𝟙 s ​ u ​ c ​ c + λ a ​ p ​ p ​ 𝟙 a ​ p ​ p − λ f ​ a ​ i ​ l ​ ( 𝟙 d ​ r ​ o ​ p + 𝟙 c ​ o ​ l ​ l ) − λ a ​ c ​ t ​ ‖ a t arm ‖ 2 \begin{split}R_{t}^{\text{arm}}=&r_{time}+r_{\text{dist}}^{\text{palm}}+\lambda_{succ}\mathds{1}_{succ}+\lambda_{app}\mathds{1}_{app}\\ &-\lambda_{fail}(\mathds{1}_{drop}+\mathds{1}_{coll})-\lambda_{act}||a_{t}^{\text{arm}}||^{2}\end{split} (2)

[59] table: R t hand = 1 5 ​ ( r dist palm + ∑ i ∈ ℱ r dist i ) + λ s ​ u ​ c ​ c ​ 𝟙 s ​ u ​ c ​ c − λ f ​ a ​ i ​ l ​ ( 𝟙 d ​ r ​ o ​ p + 𝟙 c ​ o ​ l ​ l ) − λ a ​ c ​ t ​ ‖ a t hand ‖ 2 \begin{split}R_{t}^{\text{hand}}=&\frac{1}{5}(r_{\text{dist}}^{\text{palm}}+\sum_{i\in\mathcal{F}}r_{\text{dist}}^{i})+\lambda_{succ}\mathds{1}_{succ}\\ &-\lambda_{fail}(\mathds{1}_{drop}+\mathds{1}_{coll})-\lambda_{act}||a_{t}^{\text{hand}}||^{2}\end{split} (3)

[60] p: where r dist r_{\text{dist}} is defined as the temporal difference in Euclidean distance d ⁡ ( ⋅ , ⋅ ) d(\cdot,\cdot) between the robot link and the object:

[61] table: r dist k = d ⁡ ( p t − 1 k , p t − 1 obj ) − d ⁡ ( p t k , p t obj ) , k ∈ { p ​ a ​ l ​ m , t ​ h ​ u ​ m ​ b , i ​ n ​ d ​ e ​ x , m ​ i ​ d ​ d ​ l ​ e , r ​ i ​ n ​ g } \begin{split}&r_{\text{dist}}^{k}=d(p_{t-1}^{k},p_{t-1}^{\text{obj}})-d(p_{t}^{k},p_{t}^{\text{obj}}),\\ &k\in\{palm,thumb,index,middle,ring\}\end{split} (4)

[62] p: Here, p t obj p_{t}^{\text{obj}} denotes the object position, and k k represents the link position, which is either the palm or a fingertip.

[63] p: The terms 𝟙 s ​ u ​ c ​ c \mathds{1}_{succ} , 𝟙 d ​ r ​ o ​ p \mathds{1}_{drop} , 𝟙 a ​ p ​ p \mathds{1}_{app} , and 𝟙 c ​ o ​ l ​ l \mathds{1}_{coll} are binary indicators for a successful catch, object drop, approach, and collision, respectively. An action penalty term ‖ a t ‖ 2 ||a_{t}||^{2} is employed to prevent jerky motions and ensure control stability. The coefficients are set to λ s ​ u ​ c ​ c = 10.0 \lambda_{succ}=10.0 , λ f ​ a ​ i ​ l = 5.0 \lambda_{fail}=5.0 , λ a ​ p ​ p = 0.1 \lambda_{app}=0.1 , λ a ​ c ​ t = 0.01 \lambda_{act}=0.01 , and r t ​ i ​ m ​ e = − 0.01 r_{time}=-0.01 .

[64] h3: IV-E Training Procedure

[65] p: We train the policies using the skrl library [ 38 ] based on the MAPPO framework. While standard MAPPO implementations typically employ shared policy and value networks across agents, our setup requires separate networks due to the heterogeneity of the agents, which differ in their degrees of freedom and functional roles in the catching task. The training follows the Centralized Training with Decentralized Execution (CTDE), where a centralized value function is used during training, while each agent executes its own policy independently at test time. Both the policy and value networks for each agent consist of three fully connected layers with hidden dimensions of [512, 256, 128], and ELU [ 39 ] is used as the activation function. The model is trained using the following hyperparameters: a clipping parameter of ϵ = 0.2 \epsilon=0.2 , a discount factor of γ = 0.99 \gamma=0.99 , and a KL-divergence threshold of 0.016. Training is conducted across 512 parallel environments distributed over two NVIDIA RTX A6000 GPUs.

[66] h3: IV-F System Identification and Domain Randomization

[67] p: To reduce the sim-to-real gap arising from discrepancies in robot dynamics, we perform system identification prior to policy training. A diverse set of joint-space trajectories is executed on the real robot, and the resulting motions are recorded. Using these data, joint-level dynamic parameters in simulation, including actuation gains, damping coefficients, friction, and armature, are optimized to minimize trajectory tracking errors between simulated and real executions.

[68] p: In addition, random noise is applied to both observations and actions during training. All domain randomization settings used in the training phase are summarized in Table I .

[69] figure: TABLE I: Domain randomization parameters applied in training. Parameter Type Distribution Range Robot Arm Joint stiffness Scaling Uniform [ 0.8 , 1.2 ] [0.8,\,1.2] Joint damping Scaling Uniform [ 0.8 , 1.2 ] [0.8,\,1.2] Action noise Additive Gaussian μ = 0.0 , σ = 0.03 \mu=0.0,\ \sigma=0.03 Observation noise Additive Gaussian μ = 0.0 , σ = 0.005 \mu=0.0,\ \sigma=0.005 Initial joint pos Additive Uniform [ − 0.125 , 0.125 ] [-0.125,\,0.125] Robot Hand Joint stiffness Scaling Uniform [ 0.7 , 1.3 ] [0.7,\,1.3] Joint damping Scaling Uniform [ 0.7 , 1.3 ] [0.7,\,1.3] Action noise Additive Gaussian μ = 0.0 , σ = 0.02 \mu=0.0,\ \sigma=0.02 Observation noise Additive Gaussian μ = 0.0 , σ = 0.005 \mu=0.0,\ \sigma=0.005 Object Mass Scaling Uniform [ 0.5 , 1.5 ] [0.5,\,1.5] Restitution Set Uniform [ 0.0 , 0.5 ] [0.0,\,0.5]

[70] h2: V Experimental Results

[71] p: In this section, we compare the performance of our Pixel2Catch system with several baseline methods in both simulation and real-world environments. Across all experiments, performance is evaluated using two quantitative metrics designed to assess both reaching and grasping quality. The tracking rate (T.R.) measures the proportion of trials in which the palm of the robot hand successfully makes contact with the thrown object, reflecting the policy’s ability to control the arm. The success rate (S.R.) further evaluates whether the object is stably caught without being dropped after contact, assessing the effectiveness of the overall catching behavior.

[72] p: In all experiments, objects are thrown toward the robot from random initial positions with randomly sampled directions and velocities. In simulation, each policy is evaluated on both training objects and unseen objects by executing 10 trials in each of 100 parallel environments. In real-world experiments, performance is assessed over 30 trials for each object.

[73] h3: V-A Baselines

[74] p: To validate the effectiveness of our proposed framework and the importance of visual features, we compare our method against the following baselines:

[75] p: i) w/o-PF (Without Pixel-level Features): No pixel-level features are used. The policy receives only the initial object position and the robot’s proprioception.

[76] p: ii) S-A RL (Single-Agent Reinforcement Learning): PPO [ 40 ] is used to train this baseline, where the arm and hand are controlled by a single agent. Observations and rewards are jointly integrated during training.

[77] p: iii) Only-Center (Using Only Center Point Information): This policy is an ablation of the visual cues, where the policy is trained using only the centroid coordinates( c x , c y c_{x},c_{y} ).

[78] p: iv) Only-WH (Using Only Width and Height Information): In contrast to Only-Center , this policy utilizes only the width and height ( w , h w,h ) from the pixel-level features.

[79] h3: V-B Contribution of Pixel-level Features

[80] p: Fig. 5 shows the average tracking rate and success rate of the proposed method over the training process. Table II shows evaluation results in simulation using both seen objects and unseen objects. The main findings are summarized as follows:

[81] p: (i) w/o-PF , which does not utilize pixel-level features, achieves the lowest tracking and success rates. As illustrated in Fig. 3 , the thrown objects follow diverse trajectories rather than moving along a straight path from their initial positions. Under such conditions, relying solely on the object’s initial position is insufficient to accurately catch objects. These results highlight that continuous information about object motion is essential for reliable tracking and catching motion.

[82] p: (ii) Ablation studies were conducted to analyze which features are most critical. Only-WH , which encodes object width and height in image space, indirectly reflects the object’s relative distance to the robot. However, it lacks sufficient information to infer the object’s motion direction, resulting in poor tracking and success rates. In contrast, both Only-Center and the proposed method can estimate the object’s motion direction using the image space center coordinates, leading to substantially improved tracking and success rates under the simulated trajectory distribution. Notably, the proposed method, which jointly leverages both center coordinates and scale information, consistently outperforms the single-cue variants. This indicates that combining directional cues from center motion with distance-related cues from scale variation provides a more complete and robust representation of object motion in image space.

[83] h3: V-C Comparison of Multi-agent and Single-agent Learning

[84] p: As shown in Fig. 5 , the proposed multi-agent framework consistently outperforms S-A RL in both tracking and success rates. This performance gain stems from decomposing the catching task into specialized roles for the arm and hand agents. Specifically, the arm agent focuses on positioning the end-effector to catch the object, while the hand agent concentrates on forming stable grasps during the catching phase. This task decomposition offers two key advantages. First, it allows the use of role-specific reward functions, providing clearer and less conflicting learning signals than the unified reward used in the single-agent formulation. Second, each agent operates on a role-specific observation space, reducing unnecessary coupling between reaching and grasping objectives. In contrast, the single-agent model must simultaneously process combined observations and optimize a single policy for both reaching and grasping, which can hinder learning efficiency and stability.

[85] figure: Fig. 5: Tracking and success rates over training. Results are averaged over 3 seeds, and the shaded regions indicate the standard deviation.

[86] figure: TABLE II: Performance of the baselines in simulation. The results are averaged over 3 seeds. Metric Method Objects Seen Objects Unseen Objects T.R. (%) w/o-PF 12.13 ± 1.27 \,{\scriptstyle\pm\,1.27} 12.11 ± 1.9 \,{\scriptstyle\pm\,1.9} only-WH 8.03 ± 0.6 \,{\scriptstyle\pm\,0.6} 6.11 ± 0.35 \,{\scriptstyle\pm\,0.35} only-Center 87.07 ± 1.62 \,{\scriptstyle\pm\,1.62} 87.5 ± 1.53 \,{\scriptstyle\pm\,1.53} S-A RL 78.2 ± 1.32 \,{\scriptstyle\pm\,1.32} 75.83 ± 2.00 \,{\scriptstyle\pm\,2.00} Proposed 89.97 ± 0.21 \,{\scriptstyle\pm\,0.21} 89.28 ± 0.79 \,{\scriptstyle\pm\,0.79} S.R. (%) w/o-PF 8.93 ± 1.04 \,{\scriptstyle\pm\,1.04} 7.89 ± 1.46 \,{\scriptstyle\pm\,1.46} only-WH 5.53 ± 0.51 \,{\scriptstyle\pm\,0.51} 4.00 ± 0.17 \,{\scriptstyle\pm\,0.17} only-Center 81.27 ± 0.76 \,{\scriptstyle\pm\,0.76} 80.72 ± 0.38 \,{\scriptstyle\pm\,0.38} S-A RL 63.5 ± 0.85 \,{\scriptstyle\pm\,0.85} 65.44 ± 2.25 \,{\scriptstyle\pm\,2.25} Proposed 84.13 ± 0.50 \,{\scriptstyle\pm\,0.50} 84.83 ± 1.17 \,{\scriptstyle\pm\,1.17}

[87] figure: Fig. 6: Visualization of the results of deploying a trained policy in real-world experiments. This figure presents real-world catching sequences for objects with different geometries (see Fig. 3 (a)). The “mono-cam view” shows the scene captured by the installed camera, where objects are segmented using SAM2, and pixel-level features extracted from the segmentation results are provided to the policy as input.

[88] h3: V-D Sim-to-Real Transfer Results

[89] p: We evaluate the performance of policies trained in simulation by deploying them on a real robot. The real robot system operates under ROS2 for communication, and target joint position commands generated by the policies are sent to the arm and hand controllers at 30 Hz. The task involves catching objects thrown by a human, and representative real-world catching sequences are shown in Fig. 6 . Importantly, all policies are transferred directly from simulation to the real robot without any additional real-world fine-tuning.

[90] p: As shown in Table III , the proposed method achieves the best overall performance in real-world experiments, demonstrating strong sim-to-real transfer capability. In contrast, the baseline methods exhibit significant performance degradation when deployed in the real world.

[91] p: Only-WH , which excludes image-space center information, fails to achieve any successful catch in real-world evaluation. Without center coordinates in the image space, the policy cannot reliably infer object motion direction, resulting in zero tracking and success rates.

[92] p: Only-Center achieves strong performance in simulation but degrades substantially when transferred to the real world. Although it frequently achieves initial contact with the object, it often fails to maintain stable grasping, leading to oscillatory hand motions and eventual drops. This limitation arises from the absence of width and height information, which prevents the policy from inferring relative distance and approach speed between the robot and the object.

[93] p: The S-A RL baseline, which controls both the arm and hand using a single policy, achieves a success rate of approximately 24%. In real-world settings, out-of-distribution disturbances can corrupt the shared representation, causing errors in arm and hand control simultaneously and resulting in unstable behavior during sim-to-real transfer. In contrast, the proposed multi-agent formulation decouples arm reaching and hand grasping, making the policy more robust to such disturbances.

[94] p: Overall, the observed performance degradation of the baseline methods in real-world experiments can be attributed to differences in object trajectory distributions between simulation and the real world. While simulation randomizes initial object position, velocity, and direction, real-world throws are affected by unmodeled factors such as object deformation, elasticity, and aerodynamic effects, leading to trajectories that deviate from the simulated distribution. As a result, methods that rely on a single visual cue, such as only-WH and only-Center , exhibit limited generalization to these out-of-distribution trajectories.

[95] p: In contrast, the proposed method jointly leverages both center coordinates and scale variation in image space. This enables implicit inference of object motion and approach dynamics, allowing the policy to maintain robust performance under diverse real-world throwing conditions. Consequently, the proposed method achieves a tracking rate of approximately 70% and a catching success rate of around 50% in real-world experiments.

[96] figure: TABLE III: Performance of the baselines in the real-world. Results are averaged over 30 trials for each object. Metric Method Objects Cube L-block Triangle T.R. (%) only-WH 0 0 0 only-Center 57 54 54 S-A RL 50 43 47 Proposed 73 73 70 S.R. (%) only-WH 0 0 0 only-Center 13 3 23 S-A RL 33 20 20 Proposed 63 43 43

[97] h2: VI Conclusion and Future Work

[98] p: In this work, we proposed a multi-agent reinforcement learning framework for robotic catching that leverages pixel-level visual features from a single RGB camera. By decomposing the control problem into arm and hand agents with role-specific objectives, our approach achieves robust performance in both simulation and real-world experiments, consistently outperforming baseline methods. These results demonstrate that effective dynamic catching can be realized without explicit 3D object position estimation, relying solely on relative visual cues from RGB observations.

[99] p: Despite these promising results, the current study is limited to a single-arm robotic setup. As future work, we plan to extend the proposed framework to bimanual robotic platforms to enable more stable and robust catching of objects with diverse sizes and geometries.

[100] h2: References

[101] h2: Instructions for reporting errors

[102] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[103] p: Tip: You can select the relevant text first, to include it in your report.

[104] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[105] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
