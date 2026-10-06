[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: FlowCorrect: Efficient Interactive Correction of Generative Flow Policies for Robotic Manipulation

[3] h6: Abstract

[4] p: Generative manipulation policies can fail catastrophically under deployment-time distribution shift, yet many failures are near-misses: the robot reaches almost-correct poses and would succeed with a small corrective motion. We present FlowCorrect, a deployment-time correction framework that converts near-miss failures into successes using sparse human nudges, without full policy retraining. During execution, a human provides brief corrective pose nudges via a lightweight VR interface. FlowCorrect uses these sparse corrections to locally adapt the policy, improving actions without retraining the backbone while preserving the model performance on previously learned scenarios. We evaluate on a real-world robot across three tabletop tasks: pick-and-place, pouring, and cup uprighting. With a low correction budget, FlowCorrect improves success on hard cases by 85% while preserving performance on previously solved scenarios. The results demonstrate clearly that FlowCorrect learns only with very few demonstrations and enables fast and sample-efficient incremental, human-in-the-loop corrections of generative visuomotor policies at deployment time in real-world robotics.

[5] h2: I INTRODUCTION

[6] p: Recent years have witnessed major progress in large-scale imitation learning. These advances produced foundational behavior models, including Vision-Language-Action (VLA) models [ 1 , 2 ] , that map rich semantic embeddings to continuous motor commands. In parallel, generative policy learning with diffusion and flow models [ 3 , 4 , 5 ] has emerged as a powerful paradigm for action generation. These policies can acquire broad, multimodal manipulation skills from diverse demonstrations. However, real-world deployment remains brittle: out-of-distribution (OOD) situations can cause execution failures, including irreversible mistakes or unsafe interactions because test-time states differ from those seen during training. Closing this gap requires not only stronger pre-training, but also mechanisms for continuous, incremental adaptation during deployment.

[7] p: A common remedy is parameter-efficient fine-tuning, which adapts pre-trained robot policies to new tasks and embodiments with modest compute [ 6 , 7 ] . Nevertheless, even lightweight fine-tuning typically assumes a relatively stable target distribution and sufficiently representative correction data. In practice, many failures occur in narrow OOD “pockets” of state space and are near-misses : the policy reaches an almost-correct state, and a small spatial or temporal adjustment would recover the task. Batch updating on a handful of corrected rollouts can be expensive and brittle, and may induce parameter interference that degrades previously competent behaviors [ 8 ] . We therefore argue that continual policy learning should support efficient online correction: incremental adaptation to new situations while preserving the stability of the base policy.

[8] figure: Fig. 1: Overview of our interactive FlowCorrect framework: A flow matching visuomotor policy is trained from offline demonstrations. During deployment, the frozen base policy runs the robot while a human provides occasional relative corrections. These sparse corrections are used to train our proposed lightweight FlowCorrect module that locally steers the policy’s flow field, yielding an adapted policy without retraining the original backbone.

[9] p: Interactive imitation learning (IIL) provides a natural pathway by enabling brief supervisory interventions during execution [ 9 ] . This is especially well suited to near-miss failures, where a small end-effector perturbation or short recovery motion can convert failure into success without collecting new expert demonstrations. Prior interactive approaches often learn from evaluative feedback (e.g., success/failure or scalar preference [ 10 , 11 ] ), which offers limited directional information for precise motion correction. Other approaches [ 12 , 13 ] rely on absolute corrections that specify an exact target action, pose, or short trajectory segment. While straightforward, they typically require precise inputs from the human supervisor and thus impose a higher cognitive load.

[10] p: In this work, we propose FlowCorrect , a deployment-time correction framework that enables intuitive, incremental adaptation from sparse human interventions while preserving the broad capabilities of a pre-trained base policy. For a flow-based policy, the key idea is to keep the backbone frozen and learn a lightweight correction module that applies only local adjustments. We use relative corrections—incremental changes to the robot’s current behavior—rather than requiring full demonstrations or exact target actions. Such corrections are often more natural for non-experts and align with interactive teaching paradigms such as COACH [ 14 ] . We treat these interventions as short-horizon, bounded edits that recover near-miss failures without relearning the underlying skill.

[11] p: Fig. 1 illustrates our plug-and-play FlowCorrect module for flow-based policies: a lightweight correction component that incorporates sparse online human feedback to improve behavior locally, together with a locality-preserving design that leaves the original policy unchanged outside corrected regions. Flow parameterizations are particularly amenable to such edits because they represent behavior as a continuous action flow, enabling targeted local perturbations around encountered states while preserving the global structure learned from offline demonstrations.

[12] p: To summarize, our contributions are as follows:

[13] p: FlowCorrect deployment-time correction for generative manipulation policies : We introduce an interactive framework for adapting flow-based manipulation policies from sparse human interventions, targeting near-miss failures without full policy retraining.

[14] p: Intuitive human feedback with localized adaptation : FlowCorrect learns from brief relative corrections. The adaptation is localized to corrected situations, improving recoverability while preserving the base policy in previously competent regions.

[15] p: Real-robot validation under low correction budgets : Across three tabletop manipulation tasks, we show that a small number of corrected rollouts enables rapid deployment-time recovery of hard failures, substantially improving success while maintaining performance on previously solved scenarios, and outperforming full-policy retraining in efficiency.

[16] h2: II RELATED WORK

[17] h3: II-A IIL with human-in-the-loop corrections

[18] p: A practical line of IIL improves policies during deployment by allowing a human to intervene when failures are imminent. Pan et al. [ 15 ] introduce Decaying Relative Correction (DRC), where a human supplies a transient relative offset that decays over time, reducing sustained teleoperation burden. The policy is then updated by retraining a diffusion model on corrected demonstrations. Kasaei et al. [ 16 ] similarly employ relative wrist-delta corrections, but apply them through offline replay with the image-based teleoperation system. They fine-tune the full policy on a mixture of original and corrected data.

[19] p: In contrast, several systems use absolute interventions where the human takes over control to directly provide actions or trajectory segments, and the policy is updated from the collected intervention data [ 17 , 18 , 19 , 20 ] . For instance, following the recent trend in uncertainty estimation for robotics [ 21 , 22 ] , Diff-DAgger [ 18 ] utilizes generative diffusion models approximate the expert’s action distribution and quantify policy divergence. They trigger interventions when the robot’s predicted trajectory drifts from the learned manifold. However, absolute corrections raise human workload and shift the interaction toward full teleoperation, reducing the distinction between sparse corrective signals and full demonstrations.

[20] h3: II-B Residual and modular adaptation from correction data

[21] p: To mitigate catastrophic forgetting and focus on learning from failure patterns [ 23 ] , a common direction learns residual or gated modules on top of an existing policy. Transic [ 24 ] learns a residual policy from on-robot human interventions (e.g., using a SpaceMouse) and combines it with a strong base policy to address sim-to-real gaps without overhauling the original controller. Xu et al. [ 25 ] propose Compliant Residual DAgger (CR-DAgger), collecting delta motion corrections via a compliant end-effector interface and additionally leveraging force information to stabilize contact-rich adaptation. These residual formulations motivate our design choice to preserve the pre-trained policy and learn a lightweight correction mechanism that activates only when needed, reducing interference outside the narrow OOD regions responsible for failures.

[22] h3: II-C Generative visuomotor policies

[23] p: Recent visuomotor policies increasingly utilize generative models to capture multimodal predictions [ 3 , 26 , 4 ] , enabling the policy to represent multiple distinct, equally valid action sequences for the same task. Among them, diffusion-based policies [ 27 ] have demonstrated strong performance and flexibility, and are commonly adapted via fine-tuning on additional (corrected) rollouts [ 15 , 18 ] . Beyond that, flow matching with consistency training [ 28 ] has emerged as a highly data-efficient alternative for high-dimensional control with fast inference. For instance, ManiFlow [ 5 ] combines flow matching and consistency training to produce dexterous actions in up to 10 steps and shows strong robustness and scaling behavior across diverse manipulation settings. We build on this generative-policy trend by introducing a correction-oriented module that steers flow in the desired direction while keeping the base flow matching policy.

[24] h2: III PROBLEM FORMULATION

[25] h3: III-A Imitation Learning Setup

[26] p: A robot manipulator with a parallel-jaw gripper operates in discrete control time steps t ∈ 𝒯 = { 1 , … , T } t\in\mathcal{T}=\{1,...,T\} . At each step, the robot observes 𝒐 t = ( 𝒐 t p ​ c ​ d , 𝒐 t p ​ r ​ i ​ o ) \boldsymbol{o}_{t}=(\boldsymbol{o}_{t}^{pcd},\boldsymbol{o}_{t}^{prio}) : a point cloud 𝒐 t p ​ c ​ d ∈ ℝ N × 3 \boldsymbol{o}_{t}^{pcd}\in\mathbb{R}^{N\times 3} of the workspace and its current proprioceptive state 𝒐 t p ​ r ​ i ​ o ∈ SE ⁡ ( 3 ) × { 0 , 1 } \boldsymbol{o}_{t}^{prio}\in\mathrm{SE}(3)\times\{0,1\} ; and executes an end-effector pose command 𝒂 t = ( 𝑻 t , g t ) \boldsymbol{a}_{t}=(\boldsymbol{T}_{t},g_{t}) , where 𝑻 t ∈ SE ⁡ ( 3 ) \boldsymbol{T}_{t}\in\mathrm{SE}(3) denotes the end effector transformation that relative to the robot base and g t ∈ { 0 , 1 } g_{t}\in\{0,1\} represents the binary gripper state (open/close), tracked by a low-level Cartesian controller.

[27] p: A high-level policy π \pi maps an observation history to an action sequence 1 1 1 We denote ” 𝒂 ^ \hat{\boldsymbol{a}} ” as all the predicted actions by policies in this work. :

[28] table: 𝒂 ^ t : ( t + H − 1 ) = π ( 𝒐 ( t − K + 1 ) : t ) , \hat{\boldsymbol{a}}_{t:(t+H-1)}=\pi(\boldsymbol{o}_{(t-K+1):t}),

[29] p: where H H denotes the prediction horizon and K K the length of the observation history.

[30] p: We assume access to an offline dataset of human teleoperation demonstrations 𝒟 demo = { τ m } m = 1 , … , M \mathcal{D}_{\text{demo}}=\{\tau_{m}\}_{m=1,...,M} containing M M episodes: τ m = ( 𝒐 1 : T , 𝒂 1 : T ) m \tau_{m}=(\boldsymbol{o}_{1:T},\boldsymbol{a}_{1:T})_{m} , which we use to train a base policy π θ \pi_{\theta} parametrized by θ \theta .

[31] h3: III-B Preliminaries in Flow Matching Policy

[32] p: In line with ManiFlow [ 5 ] , we use consistency flow matching (CFM) [ 29 ] as the base policy π θ \pi_{\theta} , which comprises a visual encoder z θ z_{\theta} and a vector field model f θ f_{\theta} . Specifically, f θ f_{\theta} parameterizes a latent ordinary differential equation (ODE) in the normalized action space.

[33] p: Let 𝒙 n = { ( 𝑻 h n , s h n ) } h = t t + H − 1 \boldsymbol{x}_{n}=\{(\boldsymbol{T}^{n}_{h},s^{n}_{h})\}_{h=t}^{t+H-1} denote the subtrajectory at ODE step n ∈ { 0 , … , N − 1 } n\in\{0,...,N-1\} . During inference, we initialize with Gaussian noise 𝒙 0 \boldsymbol{x}_{0} and then iteratively sample:

[34] table: 𝒙 n + 1 = 𝒙 n + Δ ​ k ​ f θ ​ ( 𝒙 n , k n , 𝒄 ) , \boldsymbol{x}_{n+1}=\boldsymbol{x}_{n}+\Delta k\,f_{\theta}(\boldsymbol{x}_{n},k_{n},\boldsymbol{c}),

[35] p: where Δ ​ k = 1 / N \Delta k=1/N is the step size and k n = Δ ​ k ⋅ n k_{n}=\Delta k\cdot n is the normalized time step. 𝒄 = z θ ( 𝐨 ( t − K + 1 ) : t ) \boldsymbol{c}=z_{\theta}(\mathbf{o}_{(t-K+1):t}) denotes the latent conditioning from the observed point cloud, encoded by z θ z_{\theta} . After N N inference steps, we interpret:

[36] table: 𝒂 ^ t : ( t + H − 1 ) = 𝒙 N , \hat{\boldsymbol{a}}_{t:(t+H-1)}=\boldsymbol{x}_{N},

[37] p: as the obtained action chunks 𝒂 ^ t : ( t + H − 1 ) \hat{\boldsymbol{a}}_{t:(t+H-1)} .

[38] p: During training we sample a subtrajectory from a rollout 𝒙 gt = 𝒂 t : ( t + H − 1 ) ∈ τ m \boldsymbol{x}_{\text{gt}}=\boldsymbol{a}_{t:(t+H-1)}\in\tau_{m} , noise 𝒙 0 \boldsymbol{x}_{0} , and continuous flow time step k ∼ 𝒰 ⁡ ( 0 , 1 ) k\sim\mathcal{U}(0,1) . A sample 𝒙 = ( 1 − k ) ​ 𝒙 0 , + k ​ 𝒙 gt \boldsymbol{x}=(1-k)\boldsymbol{x}_{0},+k\boldsymbol{x}_{\text{gt}} is defined as the linear interpolation between 𝒙 0 \boldsymbol{x}_{0} and 𝒙 gt \boldsymbol{x}_{\text{gt}} . The model f θ f_{\theta} is trained to predict the velocity 𝒗 = 𝒙 gt − 𝒙 0 \boldsymbol{v}=\boldsymbol{x}_{\text{gt}}-\boldsymbol{x}_{0} by minimizing the loss:

[39] table: ℒ F ​ ( θ ) = 𝔼 ( 𝒙 0 , 𝒙 gt , k ) ​ [ ‖ f θ ​ ( 𝒙 , k , 𝒄 ) − 𝒗 ‖ 2 2 ] . \mathcal{L}_{\text{F}}(\theta)=\mathbb{E}_{(\boldsymbol{x}_{0},\boldsymbol{x}_{\text{gt}},k)}\left[\left\|f_{\theta}(\boldsymbol{x},k,\boldsymbol{c})-\boldsymbol{v}\right\|_{2}^{2}\right]. (1)

[40] p: In consistency flow matching, an additional objective enforces the velocity predictions at two random flow time steps from a discrete range to be consistent, facilitating smoother velocity predictions according to [ 29 ] .

[41] h2: IV METHODOLOGY

[42] h3: IV-A System overview

[43] p: Our IIL approach aims to learn an augmented policy π θ + Δ ​ θ \pi_{\theta+\Delta\theta} that combines a frozen base policy π θ \pi_{\theta} with an additional learnable adapter parameterized by Δ ​ θ \Delta\theta . During online execution, a human teacher monitors the robot and can provide corrective feedback. Specifically, given a rollout generated by the current policy π θ + Δ ​ θ \pi_{\theta+\Delta\theta} , the teacher may identify a subset of actions as suboptimal and supply corrected actions through our teleoperation-based correction interface. These corrections are then used to update the adapter parameters Δ ​ θ \Delta\theta .

[44] h3: IV-B Objectives for Interactive Corrections

[45] p: Let 𝒯 corr ⊆ 𝒯 \mathcal{T}_{\text{corr}}\subseteq\mathcal{T} be the set of corrected timesteps, i.e., the subset of the entire execution horizon 𝒯 \mathcal{T} . For each t ∈ 𝒯 corr t\in\mathcal{T}_{\text{corr}} , the teacher specifies a corrected pose 𝒂 t corr ∈ SE ⁡ ( 3 ) × { 0 , 1 } \boldsymbol{a}_{t}^{\text{corr}}\in\mathrm{SE}(3)\times\{0,1\} . We define a binary mask to record the existence of this correction on timestep t t :

[46] table: m t = 𝟙 𝒯 corr ​ ( t ) := { 1 if ​ t ∈ 𝒯 corr , 0 otherwise . m_{t}=\mathbb{1}_{\mathcal{T}_{\text{corr}}}(t):=\begin{cases}1&\text{if }t\in\mathcal{T}_{\text{corr}},\\ 0&\text{otherwise}.\end{cases} (2)

[47] p: We denote the baseline (pre-adaptation) actions by 𝒂 ^ t base \hat{\boldsymbol{a}}_{t}^{\text{base}} , produced by the frozen base policy π θ \pi_{\theta} , and the adapted (post-adaptation) actions by 𝒂 ^ t adapt \hat{\boldsymbol{a}}_{t}^{\text{adapt}} from π θ + Δ ​ θ \pi_{\theta+\Delta\theta} respectively:

[48] table: 𝒂 ^ base t : ( t + H − 1 ) \displaystyle\hat{\boldsymbol{a}}^{\text{base}}_{t:(t+H-1)} = π θ ( 𝒐 ( t − K + 1 ) : t ) ; \displaystyle=\pi_{\theta}(\boldsymbol{o}_{(t-K+1):t}); 𝒂 ^ adapt t : ( t + H − 1 ) \displaystyle\hat{\boldsymbol{a}}^{\text{adapt}}_{t:(t+H-1)} = π θ + Δ ​ θ ( 𝒐 ( t − K + 1 ) : t ) . \displaystyle=\pi_{\theta+\Delta\theta}(\boldsymbol{o}_{(t-K+1):t}).

[49] p: The goal of interactive adaptation is to update the augmented policy π θ + Δ ​ θ \pi_{\theta+\Delta\theta} within the correction time set 𝒯 corr \mathcal{T}_{\text{corr}} , such that it matches the teacher’s corrected actions 𝒂 t corr \boldsymbol{a}_{t}^{\text{corr}} at timesteps t ∈ 𝒯 corr t\in\mathcal{T}_{\text{corr}} , while remaining close to the frozen base policy π θ \pi_{\theta} elsewhere. This is achieved by using only a small number of corrections and a parameter-efficient update. Formally, with base policy parameters θ \theta frozen, we seek adapter parameters Δ ​ θ \Delta\theta such that:

[50] table: 𝒂 ^ t adapt ≈ { 𝒂 t corr if ​ m t = 1 , 𝒂 ^ t base otherwise . \hat{\boldsymbol{a}}_{t}^{\text{adapt}}\approx\begin{cases}\boldsymbol{a}_{t}^{\text{corr}}&\text{if }m_{t}=1,\\ \hat{\boldsymbol{a}}_{t}^{\text{base}}&\text{otherwise}.\end{cases}

[51] figure: Fig. 2: (a) Overview of FlowCorrect module that is attached to the DiTX-Transformer from Maniflow [ 5 ] : we extend an existing flow matching policy π θ \pi_{\theta} based on DiTX-Transformer with our FlowCorrect module. Our lightweight FlowCorrect module consists of LoRA adapters (parametrized by Δ ​ θ \Delta\theta ) injected into the transformer, and a gating module g ψ g_{\psi} that outputs a signal to steer the vector flow field towards the corrected action. (b) Intuition: across N=4 integration steps, FlowCorrect iteratively adjusts the predicted velocities from v n , t v_{n,t} to v n , t ∗ v_{n,t}^{*} , steering the rollout from a base action 𝒂 ^ t base \hat{\boldsymbol{a}}_{t}^{\text{base}} toward a corrected action 𝒂 t corr \boldsymbol{a}_{t}^{\text{corr}} .

[52] h3: IV-C Interactive Correction Strategy

[53] h4: Correction Data

[54] p: To train the adapter, we collect correction data in a dedicated format during base-policy rollouts. The i i -th correction sample 𝒮 i \mathcal{S}_{i} consists of:

[55] table: 𝒮 i = { 𝒐 ( t − K + 1 ) : t , 𝒂 ^ t : ( t + H − 1 ) base , 𝒂 t : ( t + H − 1 ) corr , 𝒙 0 , m t : ( t + H − 1 ) } ( i ) , \mathcal{S}_{i}=\{\boldsymbol{o}_{(t-K+1):t},\hat{\boldsymbol{a}}^{\text{base}}_{t:(t+H-1)},\boldsymbol{a}^{\text{corr}}_{t:(t+H-1)},\boldsymbol{x}_{0},m_{t:(t+H-1)}\}^{(i)},

[56] p: each containing observation history 𝒐 ( t − K + 1 ) : t \boldsymbol{o}_{(t-K+1):t} , base policy actions 𝒂 ^ base t : ( t + H − 1 ) \hat{\boldsymbol{a}}^{\text{base}}_{t:(t+H-1)} , corrected actions 𝒂 corr t : ( t + H − 1 ) \boldsymbol{a}^{\text{corr}}_{t:(t+H-1)} , noise sample 𝒙 0 \boldsymbol{x}_{0} used to generate actions and correction masks m t : ( t + H − 1 ) m_{t:(t+H-1)} .

[57] p: We additionally record a small set of successful episodes without corrections, which serve as anchor data to discourage global drift of the adapted policy. Since the correction dataset is typically small (i.e., | 𝒯 corr | ≪ | 𝒯 | |\mathcal{T}_{\text{corr}}|\ll|\mathcal{T}| ), we require a highly parameter-efficient adaptation mechanism.

[58] p: We employ relative corrections to enable humans to adjust the robot’s motion during policy execution adapted from [ 15 ] . In contrast to absolute corrections, in which the human teacher takes full control and teleoperates the robot to specify the complete action, relative corrections consist of a correction offset 𝒃 t \boldsymbol{b}_{t} applied on top of the policy’s nominal output 𝒂 ^ t b ​ a ​ s ​ e \hat{\boldsymbol{a}}_{t}^{base} :

[59] table: 𝒂 t corr = 𝒂 ^ t base ⊕ 𝒃 t \boldsymbol{a}_{t}^{\text{corr}}=\hat{\boldsymbol{a}}_{t}^{\text{base}}\oplus\boldsymbol{b}_{t}

[60] p: Here, we use ⊕ \oplus and ⊖ \ominus to denote group composition and difference in the action space SE ⁡ ( 3 ) × { 0 , 1 } \mathrm{SE}(3)\times\{0,1\} respectively.

[61] h4: Interactive Correction Interface

[62] p: We extract a user correction signal through the same VR teleoperation interface used to record demonstrations, as shown in Fig. 3 . During policy execution, the user initiates a correction by holding a button on the VR controller. When it’s activated, we cache the controller pose 𝒑 ref ∈ SE ⁡ ( 3 ) \boldsymbol{p}_{\mathrm{ref}}\in\mathrm{SE}(3) as a reference. While the button remains pressed, we compute the relative controller motion as the pose difference:

[63] table: Δ ​ 𝒑 t = 𝒑 t ⋅ 𝒑 ref − 1 , \Delta\boldsymbol{p}_{t}\;=\;\boldsymbol{p}_{t}\cdot\boldsymbol{p}_{\mathrm{ref}}^{-1},

[64] p: where 𝒑 t \boldsymbol{p}_{t} is the current controller pose.

[65] p: This raw correction Δ ​ 𝒑 t \Delta\boldsymbol{p}_{t} is then scaled, low-pass filtered, and slew-rate limited before being applied as an additive offset to the policy action. Attached with the corrective open/closs signal g t g_{t} , we formulate a smoothed target:

[66] table: 𝒃 ~ t = 𝒃 t − 1 ⊕ α ⁡ ( γ ​ [ Δ ​ 𝒑 t g t ] ⊖ 𝒃 t − 1 ) , α = d ​ t τ + d ​ t , \tilde{\boldsymbol{b}}_{t}=\boldsymbol{b}_{t-1}\;\oplus\;\alpha\!\left(\gamma\begin{bmatrix}\Delta\boldsymbol{p}_{t}\\ g_{t}\end{bmatrix}\ominus\boldsymbol{b}_{t-1}\right),\quad\alpha=\frac{dt}{\tau+dt},

[67] p: with scale factor γ \gamma , time constant τ \tau , and control timestep d ​ t dt . To avoid abrupt changes, we additionally limit the maximum step size per timestep via

[68] table: 𝒃 t = 𝒃 t − 1 ⊕ clip ⁡ ( 𝒃 ~ t ⊖ 𝒃 t − 1 , r max ​ d ​ t ) , \boldsymbol{b}_{t}=\boldsymbol{b}_{t-1}\oplus\operatorname{clip}\!\left(\tilde{\boldsymbol{b}}_{t}\ominus\boldsymbol{b}_{t-1},\;r_{\max}dt\right),

[69] p: where the operator clip ⁡ ( ⋅ , ρ ) \operatorname{clip}(\cdot,\rho) constrains the magnitude of the relative transformation in SE ⁡ ( 3 ) \mathrm{SE}(3) .

[70] p: This smooth corrective process yields an intuitive “nudge” interface that preserves the overall structure of the policy’s behavior while enabling targeted user adjustments. Importantly, the correction loop operates at a higher control rate ( ∼ 15 \sim 15 Hz) than the policy updates ( ∼ 1 \sim 1 Hz), thereby improving responsiveness and supporting more natural user interaction.

[71] p: Practically, we record the correction offset 𝒃 t \boldsymbol{b}_{t} during data collection, corresponding to the action 𝒂 t corr \boldsymbol{a}_{t}^{\text{corr}} once it has been fully executed, i.e., when the robot reaches the commanded target pose. Finally, we apply a temporal Decaying Relative Correction (DRC) following [ 15 ] after the user releases the button, allowing the robot to smoothly transition back to the policy’s uncorrected output.

[72] figure: Fig. 3: Pipeline of the interactive correction interface.

[73] h3: IV-D FlowCorrect Module

[74] p: To integrate corrections into the augmented policy π θ + Δ ​ θ \pi_{\theta+\Delta\theta} , we present FlowCorrect , a learnable adapter module based on LoRA [ 6 ] . This module is attached to the pretrained state-of-the-art ManiFlow [ 5 ] as the generative policy to enable efficient fine-tuning. Fig. 2 (a) illustrates the general architecture of FlowCorrect .

[75] p: Specifically, our core idea is to modify the flow vector field by attaching the LoRA adapter to the MLP head of DiTX-Transformer in Maniflow. For a given correction trajectory, we want the flow trajectory starting from the original noise 𝒙 0 \boldsymbol{x}_{0} and integrated with the edited field to end at the corrected actions 𝒂 t : ( t + H − 1 ) corr \boldsymbol{a}_{t:(t+H-1)}^{\text{corr}} (see Fig. 2 (b)).

[76] p: Let 𝒙 n \boldsymbol{x}_{n} denote the latent action at ODE step n n under the edited vector field model f θ + Δ ​ θ f_{\theta+\Delta\theta} , the FlowCorrect vector field model becomes:

[77] table: f θ + Δ ​ θ ​ ( 𝒙 n , k n , 𝒄 ) = f θ ​ ( 𝒙 n , k n , 𝒄 ) + 𝒗 Δ ​ θ ​ ( 𝒙 n , t n , 𝒄 ) , f_{\theta+\Delta\theta}(\boldsymbol{x}_{n},k_{n},\boldsymbol{c})=f_{\theta}(\boldsymbol{x}_{n},k_{n},\boldsymbol{c})+\boldsymbol{v}_{\Delta\theta}(\boldsymbol{x}_{n},t_{n},\boldsymbol{c}),

[78] p: with observational condition 𝒄 = z θ ( 𝒐 ( t − K + 1 ) : t ) \boldsymbol{c}=z_{\theta}(\boldsymbol{o}_{(t-K+1):t}) . Restricting LoRA to the head of the DiTX-Transformer and to a low-rank update keeps the number of trainable parameters small ( ≈ \approx 10k), and typically yields edits that are localized in hidden-state space.

[79] p: For each timestep t t , we define a per-step target velocity toward the corrected action 𝒂 t corr \boldsymbol{a}^{\text{corr}}_{t} :

[80] table: 𝒗 n , t ∗ = 𝒂 t corr ⊖ 𝒙 n , t ( N − n ) ​ Δ ​ k , \boldsymbol{v}^{*}_{n,t}=\frac{\boldsymbol{a}^{\text{corr}}_{t}\ominus\boldsymbol{x}_{n,t}}{(N-n)\Delta k},

[81] p: which can be viewed as the velocity that would exactly reach 𝒂 t corr \boldsymbol{a}^{\text{corr}}_{t} by the end of the integration if it stayed constant (see Fig. 2 (b)). ( n − n ) ​ Δ ​ k (n-n)\Delta k represents the remaining flow time.

[82] p: We also introduce a time-dependent weight w n w_{n} that emphasizes later steps, as these are more relevant to reach the targeted action:

[83] table: w n = n + 1 N . w_{n}=\frac{n+1}{N}.

[84] p: The FlowCorrect loss for a single flow trajectory is:

[85] table: ℒ FE ​ ( Δ ​ θ ) = 1 N ​ ∑ n = 0 N − 1 w n ​ ‖ f θ + Δ ​ θ ​ ( 𝒙 n , t n , 𝒄 ) t − 𝒗 n , t ∗ ‖ 2 2 . \mathcal{L}_{\mathrm{FE}}(\Delta\theta)=\frac{1}{N}\sum_{n=0}^{N-1}w_{n}\left\|f_{\theta+\Delta\theta}(\boldsymbol{x}_{n},t_{n},\boldsymbol{c})_{t}-\boldsymbol{v}^{*}_{n,t}\right\|_{2}^{2}.

[86] p: In practice, we re-use the logged noise 𝒙 0 \boldsymbol{x}_{0} and run the ODE forward with the current f θ + Δ ​ θ f_{\theta+\Delta\theta} . The overall objective over all correction trajectories { 𝒮 i } \{\mathcal{S}_{i}\} is:

[87] table: Δ ​ θ ∗ = argmin Δ ​ θ ​ ∑ i ℒ FE ( i ) ​ ( Δ ​ θ ) . \Delta\theta^{*}=\text{argmin}_{\Delta\theta}\ \sum_{i}\mathcal{L}^{(i)}_{\mathrm{FE}}(\Delta\theta). (3)

[88] p: Although LoRA is parameter-efficient, its updates can have global effects on the policy. Consequently, improving behavior in one region of the workspace can unintentionally change actions in other regions, potentially reducing performance. To further enforce locality, we introduce a small gating network g ψ g_{\psi} that decides where to apply the flow edit (see Fig. 2 (a)):

[89] table: α t = g ψ ​ ( 𝒄 t ) ∈ [ 0 , 1 ] , \alpha_{t}=g_{\psi}(\boldsymbol{c}_{t})\in[0,1],

[90] p: where 𝒄 t \boldsymbol{c}_{t} is the observation condition at timestep t t . The gating network is intentionally a small: it first projects 𝒄 t \boldsymbol{c}_{t} into a low-dimensional space via linear projection, aggregates the projected features via mean pooling, and then uses a two-layer Multilayer Perceptron (MLP) to produce the scalar gate α t \alpha_{t} . The gated FlowCorrect vector field model becomes:

[91] table: f θ + Δ ​ θ ​ ( 𝒙 n , t n , c ) = f θ ​ ( 𝒙 n , t n , c ) + α t ​ 𝒗 Δ ​ θ ​ ( 𝒙 n , t n , c ) . f_{\theta+\Delta\theta}(\boldsymbol{x}_{n},t_{n},c)=f_{\theta}(\boldsymbol{x}_{n},t_{n},c)+\alpha_{t}\boldsymbol{v}_{\Delta\theta}(\boldsymbol{x}_{n},t_{n},c).

[92] p: In general, we train the FlowCorrect in two stages:

[93] p: Training FlowCorrect module: optimize Δ ​ θ \Delta\theta with Eq. 3 , where we fix α t ≡ 1 \alpha_{t}\equiv 1

[94] p: Gate training: freeze θ + Δ ​ θ \theta+\Delta\theta and optimize ψ \psi with

[95] table: ℒ G = \displaystyle\mathcal{L}_{G}= BCE ​ ( α , y ) + λ ent ​ H ​ ( α ) . \displaystyle\text{BCE}(\alpha,\,y)+\lambda_{\text{ent}}\;\mathrm{H}(\alpha).

[96] p: BCE ​ ( α , y ) \text{BCE}(\alpha,\,y) supervises the gate to predict whether an edit should be applied over the current horizon. The binary entropy H ⁡ ( α ) = − α ⁡ ( 1 − α ) \mathrm{H}(\alpha)=-\alpha(1-\alpha) promotes decisive gating by pushing α \alpha toward 0 0 or 1 1 rather than ambiguous intermediate values. Moreover, we define the ground-truth target y y as:

[97] table: y = { 1 if ​ ∃ t ′ ∈ { t , … , t + H − 1 } , m t ′ = 1 0 otherwise y=\begin{cases}1&\text{if }\exists\,t^{\prime}\in\{t,\dots,t+H-1\},\,m_{t^{\prime}}=1\\ 0&\text{otherwise}\end{cases}

[98] p: which claims that the window is labeled positive if at least one indicator m t = 1 m_{t}=1 within the interval from t : t + H − 1 t:t+H-1 . This encourages the gate to open in those cases.

[99] p: At inference, we apply a hard threshold α ^ t = 𝟙 [ α t > 0.5 ] \hat{\alpha}_{t}=\mathbb{1}[\alpha_{t}>0.5] to obtain a binary “use edit / do not use edit” decision per timestep, making the behavior interpretable as applying the learned flow correction only where the human indicated failures during interaction.

[100] h2: V EXPERIMENTS

[101] figure: Fig. 4: Hardware setup and representative real-world tasks used in the experiments.

[102] p: We design real-robot experiments to answer the following questions:

[103] p: Can our FlowCorrect fine-tuning, using only local human corrections, reliably fix low-performing situations while preserving the base policy’s performance on other states?

[104] p: How does FlowCorrect compare to retraining the complete base policy in terms of performance and efficiency?

[105] p: What is the impact of our gating mechanism and the usage of uncorrected rollout data?

[106] p: We evaluate our FlowCorrect module on three tabletop manipulation tasks illustrated in Fig. 4 : (i) Pick-and-Place, (ii) Pouring, and (iii) Cup Uprighting. For each task, we compare three policy types trained with the same backbone and observation/action spaces: (i) the base policy ( Base ) trained from demonstrations; (ii) our fine-tuned FlowCorrect policy ( FC ) updated from human corrections; (iii) a retrained policy ( RT ) updated from the same corrections.

[107] p: We report success rates over a structured set of in-distribution (ID) and out-of-distribution (OOD) initial conditions, and perform ablations to isolate the contributions of gating and rollout data.

[108] figure: Fig. 5: Top row: Selected ID-hard and OOD-hard initial conditions for the three tasks (left to right): Pouring, Cup Uprighting, and Pick-and-Place. The green regions indicate the workspace areas covered by the demonstrations. Middle row: Representative failure cases of the base policy under these conditions. Bottom row: Qualitative examples of successful executions after FlowCorrect fine-tuning on conditions that previously failed.

[109] h3: V-A Experiment setups

[110] h4: Hardware and Policy I/O

[111] p: All experiments are conducted on a UR10 manipulator equipped with a Robotiq 2F-85 parallel-jaw gripper. The policy observes 𝒐 t \boldsymbol{o}_{t} , including (i) a 3D point cloud 𝒐 t pcd \boldsymbol{o}^{\text{pcd}}_{t} of the workspace captured by an external time-of-flight (ToF) depth camera (Orbbec Femto Mega) and (ii) the robot proprioceptive state 𝒐 t prio \boldsymbol{o}^{\text{prio}}_{t} (end-effector pose and gripper state). The policy outputs an absolute 6D end-effector pose command together with a gripper command 𝒂 t \boldsymbol{a}_{t} , which are expressed in a common world coordinate frame. Demonstrations and policy rollouts are recorded at 10 Hz. We use an observation horizon of K = 2 K=2 timesteps and predict an action sequence of length H = 14 H=14 . At execution time, we execute the first H exec = 10 H_{\mathrm{exec}}{=}10 actions before triggering another inference cycle.

[112] h4: Data collection

[113] p: For each task, we collect eight expert demonstrations to train the base policy. During deployment, when the base policy fails, a human provides relative corrections for the same failure situation to generate correction rollouts. We also record trajectories from successful base-policy executions. For each selected failure situation, we collect ten corrected rollouts, and we randomly sample five uncorrected rollouts from successful executions.

[114] h4: Tasks

[115] p: We consider three tasks: Pick-and-Place: The robot must pick up a Rubik’s Cube and place it on a fixed-positioned box. Pouring: The robot must grasp a cup and perform a pouring motion toward a fixed-positioned cup. Uprighting a Cup: The robot must flip an overturned cup upright and place it in a designated position on the table. The initial position of all manipulated objects is randomly selected in a square area of 15x20 cm.

[116] h4: Policies and Training Variants

[117] p: We evaluate three policy types per task: (i) Base policy: trained on 8 8 demonstrations. (ii) FC policy (ours): fine-tuned from the base policy by FlowCorrect using 10 10 corrections for each selected failure case plus 5 5 rollout trajectories. (iii) RT policy: retrained (updated) base policy using the same data as FC policy in terms of corrections and rollouts. The Base policy is trained for 3000 epochs, whereas the FC and RT policies are trained for 500 epochs on a single NVIDIA RTX 4090. We use a batch size of 256 for base policy training and 64 for fine-tuning, average runtimes are listed in Table II .

[118] h3: V-B Experiment evaluation

[119] p: For each task, we define 30 in-distribution (ID) initial conditions (i.e., object positions) within the workspace region used for demonstration recording. To ensure a more standardized and comparable evaluation, these 30 positions are arranged as a 6×5 grid over the defined workspace. In addition, we define three selected low-performing ID conditions ( ID-hard #1-#3 - identified by evaluation of the base policy), and one selected low-performing OOD condition ( OOD-hard ) to be corrected by a human.

[120] p: The OOD-hard condition is selected differently per task. In Cup Uprighting and Pick-and-Place , we chose a random position 3 cm outside the workspace as the OOD condition, whereas for the Pouring task, we selected a smaller cup height as the OOD condition, since the positional OOD conditions were already robust in that task. Figure 5 shows the different ID and OOD conditions as well as some common failure cases of the base policy before adaptation with FlowCorrect . Typical failure cases include an unstable grasp, collision with the object, or misalignment with the object. Each ID and OOD condition is evaluated 10 times to define a success rate.

[121] h3: V-C Results

[122] figure: Pick-and-Place Pouring Cup Uprighting 0 0 0.2 0.2 0.4 0.4 0.6 0.6 0.8 0.8 1 1 16/30 19/30 16/30 18/30 27/30 22/30 20/30 23/30 21/30 Success rate Base FC (Ours) RT Fig. 6: Overall success rate on 30 ID positions inside the workspace.

[123] figure: TABLE I: Stress-test success on selected hard positions. “ID-hard” are the three low-performing ID conditions; “OOD-hard” is the selected OOD conditions. Task Policy ID-hard #1 ID-hard #2 ID-hard #3 OOD-hard Base 0/10 0/10 0/10 0/10 Pick-and-Place FC (Ours) 3/10 10 /10 9/10 10 /10 RT 10 /10 10 /10 10 /10 10 /10 Base 4/10 0/10 0/10 0/10 Pouring FC (Ours) 10 /10 10 /10 10 /10 2/10 RT 10 /10 10 /10 10 /10 10 /10 Base 0/10 0/10 0/10 0/10 Cup Uprighting FC (Ours) 10 /10 9 /10 10 /10 9 /10 RT 10 /10 8/10 8/10 9 /10

[124] figure: TABLE II: Resource usage comparison between our FlowCorrect training ( FC ) and retraining ( RT ). Mode Avg. GPU Memory Usage (GB) Avg. Runtime (min.) Base 18.84 ± \pm 0.24 80.86 ± \pm 10.01 FC (Ours) 4.35 ± \pm 0.15 30.24 ± \pm 5.45 RT 19.23 ± \pm 0.25 52.93 ± \pm 10.96

[125] figure: TABLE III: Ablation study on FlowCorrect . Report success (in %) on (i) 30 ID positions and (ii) hard cases across all tasks. Variant ID-30 Avg ID-hard Avg OOD-hard Avg FC (full) 74.45 90.00 70.00 FC w/o gate 61.11 71.11 70.00 FC w/o rollouts 66.67 84.44 83.33 RT 71.11 95.56 96.67 RT w/o rollouts 45.56 92.22 96.67

[126] h4: Quantitative results

[127] p: Fig. 6 summarizes overall performance across the 30 ID initial conditions. Across all three tasks, FlowCorrect ( FC ) improves the base policy’s ID success rate, indicating that sparse corrections can generalize beyond the corrected timesteps and stabilize execution in nearby states. In Pouring and Cup Uprighting , FC yields large gains. Pick-and-Place requires a more precise positioning of the gripper to prevent collisions, as the gripper is only 10mm wider than the cube. Therefore, the improvement does not have such a generalizable effect here.

[128] p: Table I reports stress tests on the selected low-performing ID and OOD conditions. For Cup Uprighting , FC reliably resolves both ID-hard and OOD-hard settings (9–10/10 success across all hard cases). For Pouring , FC fixes all three ID-hard positions (10/10 each), but improves the selected OOD condition only marginally (0/10 → \rightarrow 2/10). Notably, this OOD setting corresponds to a height change (smaller cup) rather than a positional shift. For Pick-and-Place , FC substantially improves most hard cases (up to 10/10 on ID-hard #2 and 9/10 on ID-hard #3, and 10/10 on OOD-hard), but one selected ID-hard condition improves only partially (3/10). This ID-hard condition lies spatially close to the chosen OOD condition, and the corresponding corrections are directionally different in a narrow region of the workspace. In such cases, a single locality gate and observation-agnostic LoRA update can lead to over-correction toward the OOD solution, effectively overriding the more appropriate edit for the nearby ID case. This highlights an important limitation of local correction schemes when multiple, conflicting edits must coexist at fine spatial granularity.

[129] h4: Qualitative results

[130] p: The bottom row of Fig. 5 provides representative successful executions after FlowCorrect fine-tuning. The examples visually confirm the quantitative improvements shown in Fig. 6 and Table I , demonstrating more stable alignment and execution under challenging initial conditions.

[131] h4: Comparison to retraining.

[132] p: Retraining ( RT ) achieves consistently strong performance on the hard cases. However, FC is largely competitive with RT in overall ID success (Fig. 6 ) while updating only a small LoRA module and a lightweight gate. In addition, RT incurs a substantially larger training-time footprint (GPU memory and runtime; Table II ), whereas FC provides a more deployment-friendly adaptation mechanism.

[133] h4: Ablation insights.

[134] p: Table III shows that the gating mechanism is critical for preserving ID performance: removing the gate drops ID-30 success from 74.45% to 61.11%, consistent with the gate preventing unintended global drift. Using a small set of uncorrected rollouts also improves stability: training FC without rollouts reduces ID-30 performance (66.67%) and changes the trade-off between hard-case gains and generalization, indicating that anchor trajectories help maintain the base policy’s behavior outside corrected regions.

[135] h3: V-D Discussion and Outlook.

[136] p: The two observed failure modes: (i) conflicting edits in a narrow spatial neighborhood, and (ii) OOD shifts driven by object geometry rather than pose, suggesting that conditioning the FlowCorrect itself on the observation could improve selectivity. A promising direction is to inject observation-conditioned modulation not only into the gate, but also into the LoRA/edit pathway, enabling the correction to depend explicitly on the current scene features and reducing interference between nearby but distinct correction regimes.

[137] h2: VI CONCLUSIONS

[138] p: We presented FlowCorrect , an interactive adaptation method for flow matching manipulation policies that targets common deployment failures in narrow OOD pockets. FlowCorrect keeps the pretrained backbone frozen and learns a lightweight LoRA-based module that locally steers the action flow field from sparse relative human corrections. A gate and anchor rollouts preserve behavior outside corrected regions. On three real-robot tabletop tasks, FlowCorrect improves success on hard ID/OOD conditions with a small correction budget while maintaining overall ID performance and requiring substantially less training overhead than full retraining. Future work will focus on stronger observation-conditioned edits to better handle nearby, conflicting corrections and shifts driven by object geometry.

[139] h2: References

[140] h2: Instructions for reporting errors

[141] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[142] p: Tip: You can select the relevant text first, to include it in your report.

[143] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[144] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
