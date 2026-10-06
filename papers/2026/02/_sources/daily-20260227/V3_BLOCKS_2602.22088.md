[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Force Policy : Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation

[3] h6: Abstract

[4] p: Contact-rich manipulation demands human-like integration of perception and force feedback: vision should guide task progress, while high-frequency interaction control must stabilize contact under uncertainty. Existing learning-based policies often entangle these roles in a monolithic network, trading off global generalization against stable local refinement, while control-centric approaches typically assume a known task structure or learn only controller parameters rather than the structure itself. In this paper, we formalize a physically grounded interaction frame, an instantaneous local basis that decouples force regulation from motion execution, and propose a method to recover it from demonstrations. Based on this, we address both issues by proposing Force Policy , a global-local vision-force policy in which a global policy guides free-space actions using vision, and upon contact, a high-frequency local policy with force feedback estimates the interaction frame and executes hybrid force-position control for stable interaction. Real-world experiments across diverse contact-rich tasks show consistent gains over strong baselines, with more robust contact establishment, more accurate force regulation, and reliable generalization to novel objects with varied geometries and physical properties, ultimately improving both contact stability and execution quality. Project website: force-policy.github.io .

[5] figure: Fig. 1: A Global-Local Vision-Force Policy Inspired by Human Interaction. (Left) During electric vehicle (EV) charging, humans use vision to guide global movement and coarse alignment, and rely on force feedback to continuously adjust the local contact structure . (Right) This global-local organization motivates a vision-force policy with an explicit contact structure for stable hybrid force-position control.

[6] h2: I Introduction

[7] p: Human dexterity is defined not merely by motion, but by the seamless integration of force modulation and feedback during physical interaction. Replicating this level of competence in robotic systems is the central challenge of contact-rich manipulation. Operations such as tightening a screw [ 42 ] , peeling a vegetable [ 17 , 36 ] , or polishing a surface [ 38 , 87 ] impose strict constraints where the robot must simultaneously control motion and interaction forces. Mastering contact-rich manipulation is essential for deploying robots in real-world settings, from factory assembly to everyday household tasks [ 74 ] .

[8] p: A defining aspect of how humans succeed in contact-rich tasks is a global-local organization of perception and control [ 16 , 80 ] , as illustrated in Fig. 1 (left). At the global level, humans primarily use vision to decide what to do next , where to go , and how to align [ 33 ] . At the local level, once contact happens, humans rely on high-frequency force feedback to refine execution in a structured way , applying or maintaining interaction where needed, yielding compliantly to uncertainty, and executing motion to proceed [ 34 ] . Functionally, this implies a clear division of roles: the global component should generalize across task variations, while the local component should guarantee stable contact. This suggests two core questions for robotics:

[9] p: Global-local organization. How can we realize this global-local organization, so that global guidance generalizes well while local interaction remains stable?

[10] p: Interaction structure for control. How can we represent the task interaction structure explicitly, so that it transfers across diverse contact skills?

[11] p: For (1) , many learning-based policies still adopt a monolithic design. Force signals are often appended to the observation [ 36 , 88 ] or used as auxiliary supervision [ 90 ] , but perception, planning, and contact refinement are learned jointly in a single end-to-end network. This creates an inherent trade-off: entangling local refinement with global perception makes it difficult to maintain a dedicated high-frequency interaction loop while improving global generalization by scaling up models. RDP [ 87 ] is one of the few works that explicitly introduces a slow-fast policy design, with fast reactive corrections handled by a force-aware tokenizer. However, its slow policy depends on the fast tokenizer rather than treating reactivity as a plug-and-play component, which limits reuse with arbitrary slow policies and complicates upgrading the slow policy due to the dependency of the fast reactive part.

[12] p: For (2) , a substantial body of prior work approaches contact-rich manipulation through the control interface. Classical compliant control [ 57 ] provides principled tools such as hybrid position/force control [ 66 ] and impedance control [ 37 ] . Conventional approaches apply these tools through task-specific environment/contact modeling and manual parameter tuning to match a pre-defined interaction structure. Learning-based variants aim to reduce manual tuning by predicting controller parameters from data, such as admittance gains [ 70 , 85 ] , or contact forces [ 25 , 53 ] . However, the interaction structure is usually assumed or implicit, and learning is applied mainly to tuning parameters rather than to representing the structure itself. ACP [ 38 ] is a partial exception by predicting a stiffness matrix, but its directional formulation is insufficient for multi-axis constrained interactions such as peg insertion.

[13] p: In this paper, we answer both questions by making the missing structure explicit and building a global-local vision-force policy around it. For (2) , we formalize the interaction frame, an instantaneous local basis that captures task-relevant interaction structure, from a physical perspective, and we present a principled approach to recover it directly from non-ideal real-world demonstrations. For (1) , we propose Force Policy , a global-local vision-force policy with phase-wise authority, as shown in Fig. 1 (right). A global vision policy drives task progress, while a high-frequency force module estimates the interaction frame and executes hybrid force-position control during contact. This decoupling preserves task-level planning while ensuring stable contact and reliable execution under uncertainty. Extensive real-world experiments show improved robustness and force regulation across diverse contact-rich tasks, while retaining strong generalization to novel objects with varied geometries and physical properties. Overall, Force Policy combines the generalization of visuomotor policies with the precision of force control, enabling reliable contact-rich manipulation. Code will be made publicly available.

[14] h2: II Related Works

[15] h3: II-A Contact-Rich Manipulation

[16] p: Compared to free-space motion, contact-rich manipulation requires precise force regulation and rapid adaptation to contact constraints [ 84 , 74 ] . Uncertainties in contact geometry, friction, and material compliance make interaction dynamics difficult to model reliably [ 57 , 26 ] . Classical robotics addresses these challenges with compliant control frameworks, including impedance control [ 37 , 15 ] , admittance control [ 71 , 45 , 48 ] , and hybrid force-position control [ 66 , 46 , 20 ] . Nonetheless, these approaches often rely on hand-tuned parameters and reasonably accurate environment assumptions, which can limit robustness in unstructured settings [ 81 ] .

[17] p: Learning-based methods have recently improved contact-rich manipulation by learning interaction strategies directly from data. Reinforcement learning [ 43 , 49 , 61 , 89 ] can acquire complex contact behaviors through exploration, but frequently struggles with sim-to-real transfer due to mismatches in perception and contact dynamics [ 23 ] . Hence, imitation learning has increasingly leveraged richer sensing to better ground interaction, incorporating modalities like audio [ 55 , 49 , 50 , 32 , 83 ] , tactile [ 39 , 50 , 32 , 67 , 29 ] , and force/torque signals [ 14 , 38 , 44 , 53 , 85 , 92 ] , to handle contact-rich manipulations.

[18] h3: II-B Force-Aware Manipulation Policies

[19] p: Recent advances have explored different strategies to incorporate force sensing into learning-based manipulation. A common strategy treats force as an auxiliary observation, fusing it with visual features to condition motion prediction. FoAR [ 36 ] dynamically weights visual and force via contact-phase prediction. RDP [ 87 ] couples a visual latent diffusion policy with a high-frequency tactile-aware tokenizer for reactive execution. ForceVLA [ 88 ] integrates force through a mixture-of-experts representation, while TA-VLA [ 90 ] adds torque prediction as an auxiliary objective to promote physically grounded features.

[20] p: A distinct body of work learns imitation policies within compliant control frameworks, spanning variable impedance and admittance formulations [ 38 , 85 , 44 , 1 , 70 , 92 ] . Even when driven by predicted wrenches, these controllers often tie force realization to motion through a single compliance model, so what the policy should imitate can drift with contact geometry and local stiffness. In contrast, hybrid force-position control provides a more interpretable interface by explicitly separating constrained and free directions: it lets the policy express “ what should be enforced ” (force objectives in constraint directions) and “ what should be achieved ” (position objectives in free directions), yielding clearer credit assignment and more stable learning across contact transitions. While [ 53 ] adopts a hybrid scaffold, it applies force control only along a single direction, capturing only a limited form of this factorization.

[21] h3: II-C Control Structure Discovery from Demonstrations

[22] p: The problem of inferring control structures from demonstration data has progressed from analytical geometric modeling [ 57 , 12 , 13 ] to data-driven learning approaches [ 79 , 47 , 72 ] . Across this spectrum, the goal is to recover the underlying control structure of a task, typically a decomposition that enables compliant manipulation. Because this structure is induced by task constraints, inferring the control structure is essentially equivalent to inferring the constraints from demonstration data.

[23] p: Task frame formalization (TFF) [ 57 , 12 ] provides the canonical force-motion subspace decomposition, but typically assumes explicit geometry and rigid contact. Subsequent works infer geometric constraints from demonstrations via twist-wrench analysis [ 77 , 76 , 73 , 75 ] or by fitting a set of pre-defined constraint models [ 72 ] , with refinements using interactive perception [ 52 , 65 ] or augmentation [ 51 ] . Some works [ 25 , 53 ] exploit contact force direction as the force control axis in hybrid force-position control [ 66 ] . Recent attempts improve robustness by aggregating frame estimates from multiple model-based fits using statistical fusion [ 58 ] , or by estimating task-aligned frames via power-based objectives [ 62 ] .

[24] p: In this work, we generalize the definition of task frame into a physically-grounded interaction frame and propose compact approximations based on energy dissipation, enabling reliable recovery from data for different contact-rich tasks.

[25] h2: III Theoretical Formulation

[26] h3: III-A Interaction Frame: A Physical Perspective

[27] p: In classical TFF [ 12 ] , the interaction frame is prescribed based on known geometric models. However, in unstructured environments where geometry is unknown or uncertain, such a prescription is infeasible. To bridge this gap, we define the interaction frame (IF) purely from the physical response , using stiffness as a spectral proxy to estimate the local geometry. We focus on tasks maintaining topologically invariant contact , excluding irreversible changes like fracture and plastic deformations. For these locally conservative contacts, the environmental stiffness is geometry-induced , as resistance arises directly from physical boundaries. This inherent physical causality implies that the principal axes of stiffness structurally align with the local surface geometry, allowing us to recover the geometric frame from physical observations.

[28] p: Formally, we model the local environment response at the interaction point p I p_{I} by symmetric stiffness 𝐊 env ​ ( p I ) \mathbf{K}_{\mathrm{env}}(p_{I}) . We spectrally decompose 𝐊 env ​ ( p I ) \mathbf{K}_{\mathrm{env}}(p_{I}) into principal stiffnesses λ i \lambda_{i} and axes 𝐪 i \mathbf{q}_{i} , partitioning the interaction space into the constraint subspace 𝒰 ⁡ ( p I ) \mathcal{U}(p_{I}) with high stiffness λ i ≫ 0 \lambda_{i}\gg 0 and admissible-motion subspace 𝒯 ⁡ ( p I ) \mathcal{T}(p_{I}) with negligible stiffness λ i ≈ 0 \lambda_{i}\approx 0 .

[29] p: Crucially, physical interaction is goal-directed . We introduce the task intent { 𝝃 ∗ ​ ( p I ) , 𝓦 ∗ ​ ( p I ) } \{\boldsymbol{\xi}^{*}(p_{I}),\boldsymbol{\mathcal{W}}^{*}(p_{I})\} to represent the driving factors of the interaction — specifically, the intended motion twist 𝝃 ∗ ​ ( p I ) \boldsymbol{\xi}^{*}(p_{I}) and interaction wrench 𝓦 ∗ ​ ( p I ) \boldsymbol{\mathcal{W}}^{*}(p_{I}) . This formulation distinguishes our approach from TFF, where ideal variables in [ 12 ] describe the resultant kinematic constraints without differentiating between causal actuation and environmental reaction. In our framework, the intent represents the active cause compatible with the physical structure : the motion intent 𝝃 ∗ ​ ( p I ) \boldsymbol{\xi}^{*}(p_{I}) acts as the driver within the admissible-motion subspace 𝒯 ⁡ ( p I ) \mathcal{T}(p_{I}) , while the wrench intent 𝓦 ∗ ​ ( p I ) \boldsymbol{\mathcal{W}}^{*}(p_{I}) acts as the driver against the constraint subspace 𝒰 ⁡ ( p I ) \mathcal{U}(p_{I}) . We thus define the IF Σ ⁡ ( p I ) \Sigma(p_{I}) by anchoring the spectral axes derived from 𝐊 env ​ ( p I ) \mathbf{K}_{\mathrm{env}}(p_{I}) to these driving intents:

[30] table: Σ ⁡ ( p I ) ≜ Ψ ⁡ ( 𝐊 env ​ ( p I ) , 𝝃 ∗ ​ ( p I ) , 𝓦 ∗ ​ ( p I ) ) . \Sigma(p_{I})\triangleq\Psi\left(\mathbf{K}_{\mathrm{env}}(p_{I}),\boldsymbol{\xi}^{*}(p_{I}),\boldsymbol{\mathcal{W}}^{*}(p_{I})\right). (1)

[31] p: Specifically, we set the z z -axis of IF to the direction of the dominant wrench component in 𝓦 ∗ \boldsymbol{\mathcal{W}}^{*} . We then define the x x -axis by projecting the motion intent 𝝃 ∗ \boldsymbol{\xi}^{*} onto the plane orthogonal to z z . In degenerate cases where this projection is zero, e.g. , static holding with negligible motion or screw driving with collinear motion, the interaction is effectively transversely isotropic in the constraint plane, so the rotation about z z is physically irrelevant. We therefore default Ψ \Psi to a canonical reference and complete the frame by the right-hand rule.

[32] p: To illustrate this formulation in practice, Fig. 1 visualizes the derived IF for a representative set of contact-rich tasks. This physics-aware formulation retains the orthogonal decomposition power of TFF but replaces geometric priors with environmental compliance, making it intrinsically suitable for unstructured tasks. Having defined the frame theoretically, we next address the practical challenge of recovering the IF directly from interaction data.

[33] figure: Fig. 1: Interaction Frame for Example Contact-Rich Tasks.

[34] h3: III-B Recovering Interaction Frame from Interaction Signals

[35] p: We aim to recover IF directly from the observed interaction signals 𝝃 \boldsymbol{\xi} and 𝓦 \boldsymbol{\mathcal{W}} . Assume that the gravity and inertial forces are compensated from the observed wrench. In the following, we omit the dependence of p I p_{I} in the notation for brevity.

[36] p: Under ideal rigid and frictionless contact, the observed twist and wrench perfectly align with the task intent, i.e. , 𝝃 = 𝝃 ∗ \boldsymbol{\xi}=\boldsymbol{\xi}^{*} and 𝓦 = 𝓦 ∗ \boldsymbol{\mathcal{W}}=\boldsymbol{\mathcal{W}}^{*} , yielding zero power: 𝑷 = 𝓦 ⊤ ​ 𝝃 = 0 \boldsymbol{P}=\boldsymbol{\mathcal{W}}^{\top}\boldsymbol{\xi}=\textbf{0} . In the non-ideal situations, the intended twist 𝝃 ∗ \boldsymbol{\xi}^{*} may induce a parasitic wrench 𝓦 c \boldsymbol{\mathcal{W}}_{c} along its direction. Since humans tend to align with the principal axes of the environmental stiffness 𝐊 env \mathbf{K}_{\text{env}} in expert demonstrations, the intended wrench 𝓦 ∗ \boldsymbol{\mathcal{W}}^{*} may induce a parasitic twist 𝝃 c \boldsymbol{\xi}_{c} along its direction. Hence,

[37] table: 𝑷 = ( 𝓦 ∗ + 𝓦 c ) ⊤ ​ ( 𝝃 ∗ + 𝝃 c ) = 𝓦 c ⊤ ​ 𝝃 ∗ + 𝓦 ∗ ⁣ ⊤ ​ 𝝃 c . \boldsymbol{P}=(\boldsymbol{\mathcal{W}}^{*}+\boldsymbol{\mathcal{W}}_{c})^{\top}(\boldsymbol{\xi}^{*}+\boldsymbol{\xi}_{c})=\boldsymbol{\mathcal{W}}_{c}^{\top}\boldsymbol{\xi}^{*}+\boldsymbol{\mathcal{W}}^{*\top}\boldsymbol{\xi}_{c}. (2)

[38] p: The two terms correspond to distinct power sources: 𝓦 c ⊤ ​ 𝝃 ∗ \boldsymbol{\mathcal{W}}_{c}^{\top}\boldsymbol{\xi}^{*} acts in 𝒯 \mathcal{T} as a dissipative residual , arising from frictional or viscous losses along the intended motion direction, while 𝓦 ∗ ⁣ ⊤ ​ 𝝃 c \boldsymbol{\mathcal{W}}^{*\top}\boldsymbol{\xi}_{c} acts in 𝒰 \mathcal{U} as a structural residual , resulting from environmental stiffness or contact constraints such as compliant deflections along the intended wrench direction. Consequently:

[39] p: If the structural residual dominates, we obtain 𝓦 ∗ ≈ 𝓦 \boldsymbol{\mathcal{W}}^{*}\approx\boldsymbol{\mathcal{W}} , and the twist can be orthogonalized against the wrench:

[40] table: 𝝃 ∗ = 𝝃 − Proj 𝓦 ∗ ​ ( 𝝃 ) ≈ 𝝃 − Proj 𝓦 ​ ( 𝝃 ) . \boldsymbol{\xi}^{*}=\boldsymbol{\xi}-\mathrm{Proj}_{\boldsymbol{\mathcal{W}}^{*}}(\boldsymbol{\xi})\approx\boldsymbol{\xi}-\mathrm{Proj}_{\boldsymbol{\mathcal{W}}}(\boldsymbol{\xi}). (3)

[41] p: If the dissipative residual dominates, we obtain 𝝃 ∗ ≈ 𝝃 \boldsymbol{\xi}^{*}\approx\boldsymbol{\xi} , and the wrench can be orthogonalized against the twist:

[42] table: 𝓦 ∗ = 𝓦 − Proj 𝝃 ∗ ​ ( 𝓦 ) ≈ 𝓦 − Proj 𝝃 ​ ( 𝓦 ) . \boldsymbol{\mathcal{W}}^{*}=\boldsymbol{\mathcal{W}}-\mathrm{Proj}_{\boldsymbol{\xi}^{*}}(\boldsymbol{\mathcal{W}})\approx\boldsymbol{\mathcal{W}}-\mathrm{Proj}_{\boldsymbol{\xi}}(\boldsymbol{\mathcal{W}}). (4)

[43] p: This framework contextualizes the limitations of prior art: [ 25 , 53 ] exclusively address structural dominance, effectively ignoring the dissipative dominance regime critical for friction-heavy tasks. [ 58 ] relies on statistical averaging, which lacks physical interpretability and obscures the intrinsic environmental properties. [ 62 ] directly performs power minimization, which may converge to spurious frames that satisfy orthogonality but fail to capture the true task structure.

[44] h2: IV Method

[45] p: In this section, we first present how to recover the control structure of contact-rich tasks from demonstrations (§ IV-A ). We then introduce Force Policy , a global-local vision-force policy inspired by the human organization of perception and control (§ IV-B ). Finally, we present a dual-policy asynchronous scheduler that manages dual-frequency policy execution during deployment to ensure smooth trajectories (§ IV-C ).

[46] p: Let τ = ( I 0 : T , s 0 : T , e 0 : T , 𝝃 0 : T , 𝓦 0 : T ) \tau=(I_{0:T},s_{0:T},e_{0:T},\boldsymbol{\xi}_{0:T},\boldsymbol{\mathcal{W}}_{0:T}) denote a demonstration of task 𝒯 \mathcal{T} with horizon T T , where I t I_{t} is the visual observation, s t s_{t} the end-effector pose, and e t e_{t} the end-effector state at timestep t t . The robot twist 𝝃 t ∈ 𝔰 ​ 𝔢 ​ ( 3 ) \boldsymbol{\xi}_{t}\in\mathfrak{se}(3) is composed of its linear velocity 𝒗 t \boldsymbol{v}_{t} and angular velocity 𝝎 t \boldsymbol{\omega}_{t} , i.e. , 𝝃 t = [ 𝒗 t ⊤ , 𝝎 t ⊤ ] ⊤ \boldsymbol{\xi}_{t}=[\boldsymbol{v}_{t}^{\top},\boldsymbol{\omega}_{t}^{\top}]^{\top} , while the wrench 𝓦 t ∈ 𝔰 ​ 𝔢 ∗ ​ ( 3 ) \boldsymbol{\mathcal{W}}_{t}\in\mathfrak{se}^{*}(3) is composed of its force 𝒇 t \boldsymbol{f}_{t} and moment 𝒎 t \boldsymbol{m}_{t} , i.e. , 𝓦 t = [ 𝒇 t ⊤ , 𝒎 t ⊤ ] ⊤ \boldsymbol{\mathcal{W}}_{t}=[\boldsymbol{f}_{t}^{\top},\boldsymbol{m}_{t}^{\top}]^{\top} . We assume 𝓦 t \boldsymbol{\mathcal{W}}_{t} is gravity-compensated, and inertial effects are negligible given the smooth motion profile of human demonstrations.

[47] h3: IV-A Control Structure of Contact-Rich Tasks

[48] p: Interaction Frame Identification. Consider a Δ ​ t \Delta t patch of a demonstration starting from timestep t t . In this work, we do not address the estimation of the exact contact point p I p_{I} ; instead, we assume the IF origin is anchored at the end-effector position. We aim to recover the IF orientation from visual observations I t : t + Δ ​ t I_{t:t+\Delta t} , measured signals 𝝃 t : t + Δ ​ t \boldsymbol{\xi}_{t:t+\Delta t} and 𝓦 t : t + Δ ​ t \boldsymbol{\mathcal{W}}_{t:t+\Delta t} , together with the task description 𝒯 \mathcal{T} . Inferring the ideal interaction frame directly from these signals is ill-posed, as identical local power exchange patterns may arise from different physical mechanisms, such as structural stiffness or surface friction. We therefore adopt an adaptive approximation strategy: we prompt Gemini 3 Pro [ 27 ] with the initial visual context I t I_{t} and task description 𝒯 \mathcal{T} to classify the dominant power source (dissipative residual or structural residual) based on high-level semantics, and apply the corresponding reconstruction formulation detailed in § III-B .

[49] p: Task Classification and Control Signal Generation. Given IF, where the x x -axis denotes the intended motion twist direction and the z z -axis denotes the intended interaction wrench direction, we classify interaction patches into four canonical task modes based on the IF-aligned signal characteristics of twist 𝝃 \boldsymbol{\xi} and wrench 𝓦 \boldsymbol{\mathcal{W}} :

[50] p: Free : No sustained contact. The interaction wrench is negligible, i.e. , ‖ 𝓦 ‖ ≈ 0 \|\boldsymbol{\mathcal{W}}\|\approx 0 .

[51] p: Surface : Contact with a surface imposing a single dominant normal constraint, i.e. , ‖ 𝒇 z ‖ ≫ ‖ 𝒇 x ​ y ‖ \|\boldsymbol{f}_{z}\|\gg\|\boldsymbol{f}_{xy}\| .

[52] p: Insertion : Highly-constrained insertions with strong force anisotropy from frictions, i.e. , ‖ 𝒇 x ‖ ≫ ‖ 𝒇 y ​ z ‖ \|\boldsymbol{f}_{x}\|\gg\|\boldsymbol{f}_{yz}\| .

[53] p: Rotation : Rotation-dominated interaction like fastening screws, i.e. , ‖ 𝝎 z ‖ ≫ 0 \|\boldsymbol{\omega}_{z}\|\gg 0 , and ‖ 𝒇 z ‖ ≫ 0 \|\boldsymbol{f}_{z}\|\gg 0 .

[54] p: This categorization maps directly to the hybrid control structure via a selection mask S ∈ { 0 , 1 } 6 S\in\{0,1\}^{6} [ 57 ] , where S i = 1 S_{i}=1 denotes force control and S i = 0 S_{i}=0 denotes position control. By configuring S S to align with the spectral axes of each mode, we enable the requisite motion while regulating contact forces. The specific control parameterization is detailed in Table I .

[55] figure: TABLE I: Control Structure Selection based on Task Modes. The IF x x -axis aligns with the primary motion/insertion direction, while the z z -axis aligns with the dominant normal. Interaction Task Mode Selection Mask S S Reference Wrench Free Free [ 0 , 0 , 0 , 0 , 0 , 0 ] [0,0,0,0,0,0] [ − , − , − , − , − , − ] [-,-,-,-,-,-] Contact Surface [ 0 , 0 , 1 , 0 , 0 , 0 ] [0,0,1,0,0,0] [ − , − , 𝒇 z , − , − , − ] [-,-,\boldsymbol{f}_{z},-,-,-] Insertion [ 0 , 1 , 1 , 0 , 1 , 1 ] [0,1,1,0,1,1] * [ − , 0 , 0 , − , 0 , 0 ] [-,0,0,-,0,0] Rotation [ 0 , 0 , 1 , 0 , 0 , 0 ] [0,0,1,0,0,0] * [ − , − , 𝒇 z , − , − , − ] [-,-,\boldsymbol{f}_{z},-,-,-] * In practice, for insertion tasks, both axial translation and rotation about the insertion x x -axis are theoretically inside 𝒯 \mathcal{T} , whereas for screw (pure rotation) tasks, only the axial rotation around z z -axis belongs to the 𝒯 \mathcal{T} . Nevertheless, force and torque control are often applied to these degrees of freedom to cope with high friction and prevent jamming.

[56] figure: Fig. 2: Force Policy and Dual-Policy Asynchronous Scheduler. (Left) Force Policy consists of a global vision policy and a local force policy. The global policy provides task-level visual context and global actions, while the local policy predicts interaction structure and local actions to realize hybrid force-position control during contact. (Right) The dual-policy asynchronous scheduler switches between the two policies and reduces latency and jerk via model-agnostic chunk alignment using dynamic time warping (DTW) [ 59 ] .

[57] h3: IV-B Force Policy : A Global-Local Vision-Force Policy

[58] p: Global-Local Vision-Force Decomposition. Contact-rich manipulation alternates between two regimes: vision-guided motion in free space and force-governed interaction at contact. Hence, we factor the policy accordingly. Global motion is handled by a vision policy that reasons over geometry and long-horizon sequencing; outside contact, force readings are largely uninformative and often dominated by sensor noise or incidental touches [ 36 ] . Local interaction is handled by a high-frequency force policy that reacts to end-effector proprioception and force/torque signals to regulate contact dynamics. This decomposition assigns each modality to the scale where it is most informative: vision drives task progress, while force enables responsive, stable interaction control .

[59] p: Modeling Local Force Policy. Human interaction with the physical world offers a useful intuition for designing the local interaction policy. Consider the simple act of sliding a finger along the edge of a table. Once contact is established, precise visual perception of the geometry is unnecessary; vision mainly provides global contextual cues about where interaction occurs. The interaction itself is regulated through high-frequency proprioception and force feedback: motion sensed by the hand informs how movement evolves, while force feedback reveals contact, resistance, and slip. Therefore, we formulate the fast, local, force policy Π local \Pi_{\text{local}} as:

[60] table: 𝐚 t local = Π local ( Δ s t − T o + 1 : t , 𝓦 t − T o + 1 : t , ϕ ( I t ′ ) ) , \mathbf{a}_{t}^{\text{local}}=\Pi_{\text{local}}\Big(\Delta s_{t-T_{o}+1:t},\;\boldsymbol{\mathcal{W}}_{t-T_{o}+1:t},\;\phi(I_{t^{\prime}})\Big), (5)

[61] p: where 𝐚 t local \mathbf{a}_{t}^{\text{local}} is the predicted local action, Δ s t − T o + 1 : t \Delta s_{t-T_{o}+1:t} and 𝓦 t − T o + 1 : t \boldsymbol{\mathcal{W}}_{t-T_{o}+1:t} denotes the end-effector motion and the force feedback histories of length T o T_{o} respectively. ϕ ⁡ ( I t ′ ) \phi(I_{t^{\prime}}) is the global scene context updated by the global vision policy at t ′ ≤ t t^{\prime}\leq t , decoupling the local and global policy inference frequencies.

[62] p: Each predicted local action explicitly parameterizes force-based interaction: it specifies how motion and force should be regulated in IF, rather than directly commanding joint torques or poses. Formally, we define

[63] table: 𝐚 t local ≜ ( Σ t + 1 , S t + 1 , 𝓦 t + 1 ref , Δ s t + 1 : t + T a ) , \mathbf{a}_{t}^{\text{local}}\triangleq\Big(\Sigma_{t+1},\;S_{t+1},\;\boldsymbol{\mathcal{W}}^{\text{ref}}_{t+1},\;\Delta s_{t+1:t+T_{a}}\Big), (6)

[64] p: where S t + 1 S_{t+1} selects the controlled motion and force subspaces in IF Σ t + 1 \Sigma_{t+1} , Δ s t + 1 : t + T a \Delta s_{t+1:t+T_{a}} specifies the desired motion chunk [ 91 ] of horizon T a T_{a} , and 𝓦 t + 1 ref \boldsymbol{\mathcal{W}}^{\text{ref}}_{t+1} provides the reference wrench that directly governs force regulation during contact.

[65] p: Modeling Global Vision Policy. The global vision policy Π global \Pi_{\text{global}} governs task-level progression. In free space, it acts as a standard vision-based policy and directly outputs actions. During interaction, control is delegated to the local force policy Π local \Pi_{\text{local}} , and the global vision policy no longer issues commands. Instead, it provides a global visual feature ϕ ⁡ ( I t ′ ) \phi(I_{t^{\prime}}) to condition local interaction control. This modular design allows Π global \Pi_{\text{global}} to be instantiated from existing visuomotor policies [ 91 , 18 , 82 , 31 ] or vision-language-action (VLA) models [ 8 , 7 , 6 ] without modifications.

[66] p: Router. The router determines which policy holds control authority between the global vision policy and the local force policy. Rather than introducing an explicit routing module, we reuse the predicted selection mask S t + 1 S_{t+1} from the local force policy as an implicit routing signal. When meaningful contact is detected, the local force policy activates force-control axes by assigning non-zero entries in S t + 1 S_{t+1} , thereby taking over control for hybrid force-position regulation. In contrast, unintended contacts do not trigger the selection mask, and control remains with the global vision policy.

[67] p: Force Policy . As shown in Fig. 2 (left), the overall policy is decomposed into a global vision policy Π global \Pi_{\text{global}} and a local force policy Π local \Pi_{\text{local}} . Π global \Pi_{\text{global}} is responsible for global perception and high-level action generation, while Π local \Pi_{\text{local}} handles local interaction through force-aware feedback at a high frequency. In our implementation, wrist-mounted camera observations are fed into Π local \Pi_{\text{local}} , as they lie within the local interaction field. We instantiate Π global \Pi_{\text{global}} with RISE-2 [ 31 ] , a generalizable visuomotor policy that relies solely on global 3D visual perception. In its pipeline, we treat the action feature used as the conditions in the diffusion head as the global visual feature ϕ ⁡ ( I t ′ ) \phi(I_{t^{\prime}}) . For Π local \Pi_{\text{local}} , the wrist image and proprioceptive history are encoded via a lightweight ResNet [ 35 ] and a GRU [ 21 ] , respectively. Both are conditioned on ϕ ⁡ ( I t ) \phi(I_{t}) via FiLM [ 64 ] . The resulting features are adaptively fused through a gated mechanism and used to denoise the action sequence with an MIP head [ 63 ] , as well as to predict the interaction frame, reference wrench, and selection mask via an MLP head.

[68] h3: IV-C Dual-Policy Asynchronous Scheduler

[69] p: We introduce a dual-policy asynchronous scheduler during deployment to coordinate a global vision policy with a high-frequency local force policy, while preventing global inference latency from degrading closed-loop control. The scheduler (1) runs both policies asynchronously and uses a router with smooth state transitions to avoid discontinuities during policy switching; and (2) compensates for delayed global outputs by time-aligning and merging them into the execution stream in a latency-aware manner, enforcing trajectory smoothness so executed motions remain stable and physically consistent. This smoothing also reduces jerk-induced inertial force transients, improving force-sensing fidelity during manipulation. An overview is shown in Fig. 2 (right).

[70] figure: Fig. 3: Tasks. We design three tasks spanning two categories (polishing and insertion) to evaluate different policies for contact-rich manipulation. The descriptions on the right highlight the key challenges of each task compared to similar tasks in prior literature. All tasks require highly accurate force regulation to be successfully completed. We randomize object placement within the workspace area during both data collection and evaluation for each task.

[71] p: Asynchronous Inference and Execution. To mask inference latency, the scheduler adopts a multi-threaded asynchronous design that overlaps model inference with trajectory execution, preemptively launching inference at fixed intervals. Action selection follows the router in § IV-B , with hysteresis applied to suppress switching jitter. In implementation, outputs from both the global vision policy and the local force policy are first interpolated to a unified frequency of 50Hz. At this common rate, waypoints are selectively dropped to mitigate chunk mismatch induced by inference latency, as detailed in the following paragraph, followed by acceleration-continuous trajectory planning. This planning step ensures smooth execution and high-fidelity force control, as higher-order continuity suppresses jerk and reduces inertial disturbances. The resulting trajectories are then dispatched to a non-real-time hybrid force-position controller [ 78 ] for execution.

[72] p: Chunk Alignment with Dynamic Time Warping. Latency in asynchronous inference systems typically causes discontinuous jumps between consecutive action chunks. Existing methods [ 2 , 9 , 10 ] address this issue via action inpainting or adaptive conditional guidance, but depend on specific model architectures and introduce additional computational overhead. In contrast, we propose a computationally efficient, model-agnostic waypoint dropout strategy based on Dynamic Time Warping (DTW) [ 59 ] . DTW enables nonlinear temporal alignment and has been widely adopted from speech recognition [ 68 , 60 , 40 ] to motion retargeting [ 54 ] . By aligning the predicted trajectory with the recent execution history, we can identify an optimal entry index and drop preceding waypoints, thereby eliminating latency-induced discontinuities without modifying the training procedure or model architecture. Additional implementation details are provided in the supplementary material.

[73] p: The proposed scheduler enables latency-aware deployment of dual-policy control by decoupling asynchronous inference from execution while maintaining smooth, force-consistent motion. Unified-frequency resampling, DTW-based chunk alignment, and acceleration-continuous planning together ensure stable execution without constraining policy architecture.

[74] h2: V Experiments

[75] p: Through experiments, we seek to answer the following questions: (Q1) Can Force Policy effectively handle different types of contact-rich tasks? (Q2) Does the Force Policy achieve superior force control compared to existing force-aware baselines? (Q3) Does our global-local design generalize better than the baselines? (Q4) Does our IF recovery method produce more accurate IF than prior approaches, and does improved interaction labeling enable the policy to learn more accurate contact behaviors? (Q5) Does the asynchronous scheduler reduce motion and force jerks, leading to smoother trajectories during deployment?

[76] figure: TABLE II: Evaluation Success Rates. We report success rates evaluated in an accumulative, stage-wise manner. Force Policy achieves the highest success rates compared to vision-based and force-aware baselines among all tasks. Policy Push and Flip Plug in EV Charger Scrape off Sticker (Easy) Scrape off Sticker (Hard) push flip contact match plug in contact one-side full off contact one-side full off RISE-2 [ 31 ] 100.0 % 42.5% 100.0 % 90.0 % 0.0% 100.0 % 80.0% 80.0% 100.0 % 20.0% 10.0% π 0.5 \pi_{0.5} [ 7 ] 80.0% 52.5% 100.0 % 30.0% 0.0% 70.0% 70.0% 70.0% 100.0 % 40.0% 20.0% RDP [ 87 ] 100.0 % 57.5% 100.0 % 70.0% 5.0% 100.0 % 90.0% 70.0% 100.0 % 30.0% 20.0% FoAR [ 36 ] 100.0 % 60.0% 100.0 % 80.0% 10.0% 100.0 % 70.0% 40.0% 100.0 % 60.0% 20.0% ForceVLA [ 88 ] 50.0% 30.0% 20.0% 0.0% 0.0% 10.0% 0.0% 0.0% 10.0% 0.0% 0.0% TA-VLA [ 90 ] 85.0% 62.5% 80.0% 10.0% 0.0% 50.0% 50.0% 50.0% 40.0% 20.0% 10.0% Force Policy (ours) 100.0 % 95.0 % 100.0 % 90.0 % 65.0 % 100.0 % 100.0 % 100.0 % 100.0 % 90.0 % 90.0 %

[77] h3: V-A Setup

[78] p: Platform. The robot platform comprises a Flexiv Rizon 4 arm equipped with a Flexiv GN-02 gripper and a 6-DoF force-torque sensor at the flange. Two Intel RealSense D415 RGB-D cameras are used to capture visual observations, serving as a global camera and a wrist-mounted camera, respectively.

[79] p: Tasks. As shown in Fig. 3 , we design three tasks from two major applications: polishing and insertion, including scenarios with continuously varying IFs and tasks that demand reactive control and accurate force regulation.

[80] p: Data Collection. We use the arm-to-arm teleoperation toolkit with force feedback [ 56 ] to collect 50 high-quality demonstrations for each task. The system provides high-fidelity force feedback during teleoperation, enabling precise force regulation across tasks and task phases. Inspection of all demonstrations shows that the recorded force signals consistently fall within the required range for each task stage.

[81] p: Baselines. For vision-only baselines, we consider two state-of-the-art policies: RISE-2 [ 31 ] and π 0.5 \pi_{0.5} [ 7 ] . For force-aware baselines, we include the representative RDP [ 87 ] , FoAR [ 36 ] , ForceVLA [ 88 ] , and TA-VLA [ 90 ] in evaluations.

[82] p: Metrics. We report success rate as the primary metric for each task. For the “flip” phase in Push and Flip and the “plug in” phase in Plug in EV Charger , we also count partial completion as a half success (0.5) per trial.

[83] p: Evaluation. The π \pi -based policies run on a server with an NVIDIA A800 GPU due to memory limitations, while others run on a workstation with an RTX 3090. Following [ 19 , 86 ] , all policies are evaluated consistently: test positions are randomly generated beforehand, the workspace is identical, and metrics are counted over 20 trials for Push and Flip , and 10 for others.

[84] h3: V-B Results

[85] p: Force Policy exhibits significant effectiveness in handling a diverse range of contact-rich tasks (Q1). As shown in Tab. II , Force Policy consistently outperforms both vision-only and force-aware baselines across a wide range of contact-rich tasks, with the largest gains appearing in phases that require precise and rapid force regulation, e.g. , during the insertion stage in the Plug in EV Charger task, and the scraping stage in the Scrape off Sticker task. The underlying insight is that force feedback is genuinely useful, but only when integrated in a way that matches its intermittent, regime-dependent nature .

[86] figure: Fig. 4: Visualization of Effective Forces during Deployment and from Demonstrations on the Scrape off Sticker (Hard) Task. All baselines fail to replicate the force behavior from demonstrations, resulting in degraded performance. Force Policy closely imitates the effective force in demonstrations, achieving higher success rates.

[87] p: Many prior designs misuse force in ways that reduce robustness. (1) Monolithic vision-force policies that simply concatenate force into observations, such as ForceVLA and TA-VLA, are prone to failure, because force is noisy or uninformative during non-contact motion and can pollute global decision-making [ 36 ] , sometimes even underperforming their vision-only backbone. The effect is particularly pronounced in the evaluation results of ForceVLA. (2) Low-frequency force-aware pipelines such as FoAR lack sufficient reactivity to handle fast contact transients . (3) RDP employs a hierarchically-coupled policy design, in which low-level force-aware action decoding is directly conditioned on the high-level latent action chunk. When the high-level policy encodes a no-contact latent action but unexpected contact occurs during execution, the low-level tokenizer may map out-of-distribution contact force signals to erroneous actions. This coupling limits the ability of low-level policy to correct wrong high-level latent action .

[88] p: In contrast to all baselines, our global-local vision-force design decouples high-level intent from low-level execution: the global vision module provides a stable long-horizon reference, insulated from noisy force signals , while the high-frequency local force policy independently determines actions based on this reference and real-time force feedback, enabling robust performance under sensor noise and fast contact transients.

[89] p: Force Policy achieves significantly superior force control compared to existing force-aware baselines (Q2). As visualized in Fig. 4 and Tab. III , our method closely tracks the force profile of human demonstrations, maintaining the necessary effective force magnitude throughout the critical phases. On the contrary, baselines typically exhibit severe force oscillations, fail to exert sufficient downward force, or apply excessive force, resulting in task failure. This performance advantage stems from our adoption of a hybrid force-position control framework. Unlike baselines that regulate force implicitly or treat it as a sensory input, our approach explicitly controls interaction forces, enabling stable execution that faithfully follows demonstrations, which is essential for contact-rich tasks requiring precise force control.

[90] figure: Policy Avg. d d (mm) ↓ \downarrow RISE-2 [ 31 ] 0.86 0.86 π 0.5 \pi_{0.5} [ 7 ] 0.00 RDP [ 87 ] 1.13 1.13 FoAR [ 36 ] 0.25 0.25 ForceVLA [ 88 ] 0.50 0.50 TA-VLA [ 90 ] 1.25 1.25 Force Policy (ours) 0.00 TABLE III: Force Regulation Evaluation on the Push and Flip Task. (Left) Pushing the heavy object requires approximately 45N, while demonstrations apply about 15N pushing force to flip the target object; we then measure its pushed distance d d as an indicator of force regulation. (Right) Statistics of the pushed distance for each method.

[91] p: Force Policy demonstrates decent generalization ability compared to baselines (Q3). As demonstrated in Tab. IV , we evaluated the policies on unseen objects with varying colors, geometries, and stiffnesses in the Push and Flip task. Force Policy consistently achieves high success rates, whereas baselines frequently suffer catastrophic failure. Crucially, we must clarify that although RISE-2, our global vision policy, often yields a 0% success rate on novel objects, it successfully navigates to the near-contact region in most trials . Its failure mainly arises from relying on vision alone to handle the critical transition from free motion to contact, causing timing errors or improper contact establishment. Our design successfully inherits this visual generalization capability from the global vision backbone to reliably guide the end-effector to the target vicinity . Once in the near-contact region, the local force policy takes over, leveraging force feedback and hybrid force-position control to robustly establish contact and execute the actions. By decoupling visual reaching from physical interaction, our method effectively combines the broad generalization of visuomotor policies with the precision of local force control.

[92] figure: TABLE IV: Generalization Evaluation on the Push and Flip Task. We use unseen objects of different colors, geometries, and stiffnesses to evaluate the generalization ability of force-aware policies. Please refer to the supplementary material for detailed object comparisons. Policy Unseen Obj. RISE-2 [ 31 ] 3/5 0/5 0/5 3/5 0/5 0/5 π 0.5 \pi_{0.5} [ 7 ] 2/5 2/5 1/5 3/5 3/5 1/5 RDP [ 87 ] 2/5 0/5 0/5 0/5 0/5 0/5 FoAR [ 36 ] 1/5 0/5 0/5 0/5 0/5 0/5 ForceVLA [ 88 ] 2/5 0/5 0/5 1/5 0/5 0/5 TA-VLA [ 90 ] 3/5 2/5 1/5 1/5 3/5 1/5 Force Policy (ours) 5/5 5/5 4/5 4/5 3/5 2/5

[93] h3: V-C Ablations

[94] figure: Fig. 5: IF Recovery Evaluation on the Scrape off Sticker Task. Angular error is computed between the recovered and ground-truth force control axes; a failure is counted if it exceeds 20 ∘ .

[95] p: Our IF recovery method achieves more accurate interaction frames from demonstrations than previous approaches, improving interaction quality (Q4). We evaluate several IF recovery approaches on the Scrape off Sticker task, including analytic [ 58 ] , power-based [ 62 ] , wrench-only [ 53 , 25 ] , twist-only, and our adaptive method. The z z -axis of the ground-truth IF aligns with the world vertical axis in this task, so we measure angular error and count failures above 20 ∘ . The results are shown in Fig. 5 . Analytic and power-based approaches exhibit larger errors, while twist-only and our method outperform wrench-only due to dissipative residuals like frictions dominating power in this task. Our adaptive method slightly improves over twist-only by capturing brief pressing periods before scraping, where structural residuals like scraper deformation dominate. We further evaluate the Force Policy trained with interaction frames labeled by wrench-only methods [ 53 ] on this task. It achieves only a 50% success rate, dropping from 90% with our IF recovery strategy.

[96] p: The asynchronous scheduler substantially reduces jerks and yields smoother trajectories during deployment (Q5). We analyze both force and motion jerks and measure trajectory smoothness using spectral arc length (SPARC, ↑ \uparrow ) [ 3 ] following [ 2 ] . As shown in Fig. 6 , the temporal profiles indicate that the scheduler effectively attenuates signal discontinuities, resulting in smoother trajectories during the inference chunk alignment phase. Additional analysis of the asynchronous scheduler is provided in the supplementary material.

[97] figure: Fig. 6: Asynchronous Scheduler Evaluation on the Push and Flip Task. The scheduler effectively reduces both motion and force jerks (left) , resulting in more smoother executed trajectories (right) .

[98] h2: VI Conclusion

[99] p: Motivated by the biological division of labor where vision guides global decision-making and reaching while haptics governs local contact, we propose Force Policy , a global-local vision-force framework that decouples the control hierarchy. The global vision policy decides “ where to act ” with strong generalization, while a high-frequency local controller decides “ how to act ” by regulating contact via hybrid force-position control. This design is enabled by a physically grounded interaction-frame formulation and a practical method to recover intrinsic frames from demonstrations. Empirically, we show (1) substantially improved robustness and precise force regulation on diverse contact-rich manipulation tasks by explicitly modeling contact structure and interaction forces, and (2) strong generalization across various object geometries and physical properties, driven by the complementary roles of the global vision policy that handles visual and geometric variation and the local force policy that handles contact dynamics. Overall, Force Policy bridges the generalization of visuomotor policies with the precision of classical force control, providing a scalable approach to contact-rich manipulation.

[100] p: Limitation and Future Work. Our current formulation focuses more on recovering interaction orientation for force control, rather than explicitly estimating the true contact point; fully modeling the contact structure would be necessary to support torque control. Future work may consider extending the formulation to destructive tasks like cutting. For some tasks, force might help high-level decision-making, e.g. , briefly tugging to check if the connector is fully inserted; a promising direction is to extend the architecture to enable such force-driven judgments.

[101] h2: Acknowledgement

[102] p: We would like to thank Yiming Wang from Shanghai Jiao Tong University for insightful discussions on theoretical formulation; Zhipeng Zhang from Flexiv for his support on the arm-to-arm teleoperation system with force feedback; Wenbo Tang from Flexiv for discussions about the robot controller; Peishen Yan and Chunyu Xue from Shanghai Jiao Tong University for writing advice and proofreading; and Lijia Yao from Noematrix for suggestions on figure design.

[103] h2: References

[104] p: Supplementary Materials for Force Policy

[105] h2: Supp. I Theoretical Formulation

[106] h3: Supp. I.1 Geometry-Induced Interaction Structure

[107] p: Let δ ​ 𝝌 ∈ 𝔰 ​ 𝔢 ​ ( 3 ) \delta\boldsymbol{\chi}\in\mathfrak{se}(3) denote the infinitesimal pose perturbation at the interaction point p I p_{I} . The resulting interaction wrench 𝓦 tot ∈ 𝔰 ​ 𝔢 ∗ ​ ( 3 ) \boldsymbol{\mathcal{W}}_{\text{tot}}\in\mathfrak{se}^{*}(3) measured at p I p_{I} is generally a superposition of conservative and dissipative effects. To extract the geometric topology, we apply an additive decomposition:

[108] table: 𝓦 tot = 𝓦 el + 𝓦 dis . \boldsymbol{\mathcal{W}}_{\text{tot}}=\boldsymbol{\mathcal{W}}_{\text{el}}+\boldsymbol{\mathcal{W}}_{\text{dis}}. (7)

[109] p: Here, 𝓦 dis \boldsymbol{\mathcal{W}}_{\text{dis}} denotes non-conservative terms like friction. Crucially, we postulate that the structural constraints arise exclusively from an internal elastic potential energy U ⁡ ( δ ​ 𝝌 ) U(\delta\boldsymbol{\chi}) . Thus, the conservative elastic wrench 𝓦 el \boldsymbol{\mathcal{W}}_{\text{el}} is defined as the negative gradient of this potential:

[110] table: 𝓦 el ​ ( δ ​ 𝝌 ) ≜ − ∇ U ​ ( δ ​ 𝝌 ) . \boldsymbol{\mathcal{W}}_{\text{el}}(\delta{\boldsymbol{\chi}})\triangleq-\nabla U(\delta\boldsymbol{\chi}). (8)

[111] p: The environmental stiffness 𝐊 env \mathbf{K}_{\mathrm{env}} is formally defined as the sensitivity of the elastic wrench to the pose perturbation:

[112] table: 𝐊 env ≜ − ∂ 𝓦 el ​ ( δ ​ 𝝌 ) ∂ ( δ ​ 𝝌 ) | δ ​ 𝝌 = 𝟎 = ∇ 2 U ​ ( δ ​ 𝝌 ) | δ ​ 𝝌 = 𝟎 . \mathbf{K}_{\mathrm{env}}\triangleq-\left.\frac{\partial\boldsymbol{\mathcal{W}}_{\mathrm{el}}(\delta\boldsymbol{\chi})}{\partial(\delta\boldsymbol{\chi})}\right|_{\delta\boldsymbol{\chi}=\mathbf{0}}=\left.\nabla^{2}U(\delta\boldsymbol{\chi})\right|_{\delta\boldsymbol{\chi}=\mathbf{0}}. (9)

[113] p: Since 𝐊 env \mathbf{K}_{\mathrm{env}} is modeled as the Hessian of a conservative potential, it is symmetric . Then, we derive the following theorem, showing that the translational and rotational stiffness in 𝐊 env \mathbf{K}_{\text{env}} can be diagonalized using the same rotation matrix.

[114] h6: Theorem 1 (Unified Spatial Basis) .

[115] p: Under the assumption that the local interaction follows the Hertzian contact model, there exists a single rotation matrix 𝐑 ∈ S ​ O ​ ( 3 ) \mathbf{R}\in SO(3) such that the corresponding spatial rotation 𝚽 = diag ⁡ ( 𝐑 , 𝐑 ) ∈ ℝ 6 × 6 \mathbf{\Phi}=\operatorname{diag}(\mathbf{R},\mathbf{R})\in\mathbb{R}^{6\times 6} diagonalizes the full environment stiffness matrix 𝐊 env ∈ ℝ 6 × 6 \mathbf{K}_{\mathrm{env}}\in\mathbb{R}^{6\times 6} .

[116] p: Proof . We explicitly model the local contact interface at the interaction point p I p_{I} according to Hertzian contact theory. Under this formulation, the local surface separation is approximated by a quadratic form, resulting in an elliptical contact patch 𝒟 ⊂ ℝ 2 \mathcal{D}\subset\mathbb{R}^{2} . We express wrenches/twists at the stiffness centroid of the contact patch, i.e. , the first moments of the stiffness distribution over 𝒟 \mathcal{D} vanish. We construct the Principal Geometric Frame, denoted as Σ geo \Sigma_{\text{geo}} , defined by the orthonormal basis { 𝐭 1 , 𝐭 2 , 𝐧 } \{\mathbf{t}_{1},\mathbf{t}_{2},\mathbf{n}\} , where 𝐧 \mathbf{n} is the common surface normal, and 𝐭 1 , 𝐭 2 \mathbf{t}_{1},\mathbf{t}_{2} align with the principal axes of the contact ellipse (corresponding to the principal relative curvature directions). By the definition of Hertzian geometry, the domain 𝒟 \mathcal{D} possesses intrinsic reflectional symmetry with respect to the planes defined by 𝐧 \mathbf{n} - 𝐭 1 \mathbf{t}_{1} and 𝐧 \mathbf{n} - 𝐭 2 \mathbf{t}_{2} . We define the local coordinates ( x , y ) (x,y) along ( 𝐭 1 , 𝐭 2 ) (\mathbf{t}_{1},\mathbf{t}_{2}) .

[117] p: We model the contact elasticity using a distributed Winkler foundation model, where the stiffness densities k t 1 ​ ( x , y ) , k t 2 ​ ( x , y ) k_{t_{1}}(x,y),k_{t_{2}}(x,y) and k n ​ ( x , y ) k_{n}(x,y) are distributed over 𝒟 \mathcal{D} . The translational stiffness matrix in the geometric frame, 𝐊 v geo \mathbf{K}_{v}^{\text{geo}} , represents the resistance to linear displacements. The stiffness elements are therefore:

[118] table: k x ​ x \displaystyle k_{xx} = ∫ 𝒟 k t 1 ​ ( x , y ) ​ d x ​ d y , \displaystyle=\int_{\mathcal{D}}k_{t_{1}}(x,y)\,\mathrm{d}x\mathrm{d}y, (10) k y ​ y \displaystyle k_{yy} = ∫ 𝒟 k t 2 ​ ( x , y ) ​ d x ​ d y , \displaystyle=\int_{\mathcal{D}}k_{t_{2}}(x,y)\,\mathrm{d}x\mathrm{d}y, k z ​ z \displaystyle k_{zz} = ∫ 𝒟 k n ​ ( x , y ) ​ d x ​ d y . \displaystyle=\int_{\mathcal{D}}k_{n}(x,y)\,\mathrm{d}x\mathrm{d}y.

[119] p: Due to the orthogonality of the basis vectors { 𝐭 1 , 𝐭 2 , 𝐧 } \{\mathbf{t}_{1},\mathbf{t}_{2},\mathbf{n}\} , the linear resistance is decoupled along these axes ( e.g. , a pure normal displacement does not induce a net shear force in a symmetric isotropic contact). Thus, 𝐊 v geo \mathbf{K}_{v}^{\text{geo}} is diagonal:

[120] table: 𝐊 v geo = diag ⁡ ( k x ​ x , k y ​ y , k z ​ z ) . \mathbf{K}_{v}^{\text{geo}}=\operatorname{diag}(k_{xx},k_{yy},k_{zz}). (11)

[121] p: The rotational stiffness arises from the moment of the distributed elastic forces. The stiffness elements correspond to the second moments of the stiffness distribution. Consider the rotational stiffness components in Σ geo \Sigma_{\text{geo}} . For principal stiffnesses, we obtain:

[122] table: κ x ​ x \displaystyle\kappa_{xx} = ∫ 𝒟 k n ​ ( x , y ) ​ y 2 ​ d x ​ d y , \displaystyle=\int_{\mathcal{D}}k_{n}(x,y)y^{2}\,\mathrm{d}x\mathrm{d}y, (12) κ y ​ y \displaystyle\kappa_{yy} = ∫ 𝒟 k n ​ ( x , y ) ​ x 2 ​ d x ​ d y , \displaystyle=\int_{\mathcal{D}}k_{n}(x,y)x^{2}\,\mathrm{d}x\mathrm{d}y, κ z ​ z \displaystyle\kappa_{zz} = ∫ 𝒟 ( k t 2 ​ ( x , y ) ​ x 2 + k t 1 ​ ( x , y ) ​ y 2 ) ​ d x ​ d y . \displaystyle=\int_{\mathcal{D}}\left(k_{t_{2}}(x,y)x^{2}+k_{t_{1}}(x,y)y^{2}\right)\,\mathrm{d}x\mathrm{d}y.

[123] p: To establish the diagonality of 𝐊 ω geo \mathbf{K}_{\omega}^{\text{geo}} , we verify that all off-diagonal terms vanish due to the symmetry of the contact domain 𝒟 \mathcal{D} . First, the in-plane coupling κ x ​ y \kappa_{xy} vanishes because the geometric term x ​ y xy is an odd function, while the stiffness distribution k n ​ ( x , y ) k_{n}(x,y) is even:

[124] table: κ x ​ y = − ∫ 𝒟 k n ( x , y ) x y d x d y = 0 . \kappa_{xy}=-\int_{\mathcal{D}}k_{n}(x,y)xy\,\mathrm{d}x\mathrm{d}y=0. (13)

[125] p: Similarly, the out-of-plane couplings κ x ​ z \kappa_{xz} and κ y ​ z \kappa_{yz} vanish. Under the Hertzian assumption, the surface profile z ⁡ ( x , y ) z(x,y) is quadratic and thus an even function. Moreover, under macroscopic reflectional symmetry, the stiffness densities are even functions over 𝒟 \mathcal{D} . Consequently, the integrands involving the moment arms x x and y y become odd functions, yielding:

[126] table: κ x ​ z \displaystyle\kappa_{xz} = − ∫ 𝒟 k t 1 ( x , y ) z ( x , y ) x d x d y = 0 , \displaystyle=-\int_{\mathcal{D}}k_{t_{1}}(x,y)z(x,y)x\,\mathrm{d}x\mathrm{d}y=0, (14) κ y ​ z \displaystyle\kappa_{yz} = − ∫ 𝒟 k t 2 ( x , y ) z ( x , y ) y d x d y = 0 . \displaystyle=-\int_{\mathcal{D}}k_{t_{2}}(x,y)z(x,y)y\,\mathrm{d}x\mathrm{d}y=0.

[127] p: Therefore, 𝐊 ω geo \mathbf{K}_{\omega}^{\text{geo}} is diagonal:

[128] table: 𝐊 ω geo = diag ⁡ ( κ x ​ x , κ y ​ y , κ z ​ z ) . \mathbf{K}_{\omega}^{\text{geo}}=\operatorname{diag}(\kappa_{xx},\kappa_{yy},\kappa_{zz}). (15)

[129] p: Finally, we address the linear-angular coupling blocks 𝐊 v ​ ω \mathbf{K}_{v\omega} . These terms represent the net force induced by a pure rotation (or net torque by a pure translation) and involve the first moments of the stiffness distribution. For instance, the normal force induced by a rotation about the y y -axis is proportional to:

[130] table: k z ​ θ y = ∫ 𝒟 k n ​ ( x , y ) ​ x ​ 𝑑 x ​ 𝑑 y = 0 , k_{z\theta_{y}}=\int_{\mathcal{D}}k_{n}(x,y)x\,\mathrm{d}x\mathrm{d}y=0, (16)

[131] p: since k n ​ ( x , y ) k_{n}(x,y) is even and x x is odd. By the same symmetry argument applied to all first-moment integrals over 𝒟 \mathcal{D} , the coupling blocks vanish ( 𝐊 v ​ ω = 𝟎 \mathbf{K}_{v\omega}=\mathbf{0} ).

[132] p: Combining Eqn. ( 11 ), ( 15 ), and ( 16 ), we confirm that in the principal geometric frame Σ geo \Sigma_{\text{geo}} , the stiffness matrix 𝐊 env \mathbf{K}_{\text{env}} is fully diagonalized by 𝚽 = diag ⁡ ( 𝐑 , 𝐑 ) \mathbf{\Phi}=\operatorname{diag}(\mathbf{R},\mathbf{R}) . ∎

[133] p: Remark (Generalization to Multi-Point and Area Contacts). Although Theorem 1 is derived explicitly under the Hertzian contact formulation, the resulting diagonalization property extends to a broader class of interactions relevant to robotics, such as multi-point contacts and planar area contacts. The sufficient condition for the decoupling is the macroscopic reflectional symmetry of the stiffness distribution and the contact domain 𝒟 \mathcal{D} . For instance, in peg-in-hole assembly, the interaction often manifests as a ring contact or a symmetric multi-point pattern. In polishing, the tool-surface interface may form a planar patch. In these scenarios, the contact domain 𝒟 \mathcal{D} retains a center of symmetry, and the effective stiffness distribution remains an even function with respect to the principal axes. Consequently, the parity arguments used in the proof remain valid, ensuring that the spatial axes defined by the macroscopic geometry still diagonalize the stiffness matrix.

[134] p: On the other hand, by the spectral theorem, the symmetric 𝐊 env \mathbf{K}_{\mathrm{env}} has real eigenvalues and orthonormal eigenvectors:

[135] table: 𝐊 env ​ ( p I ) = 𝐐 ​ 𝚲 ​ 𝐐 ⊤ \mathbf{K}_{\mathrm{env}}(p_{I})=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top} (17)

[136] p: where 𝚲 = diag ⁡ ( λ 1 , ⋯ , λ 6 ) \boldsymbol{\Lambda}=\mathrm{diag}(\lambda_{1},\cdots,\lambda_{6}) denotes the eigenvalues, and 𝐐 = [ 𝒒 1 , ⋯ , 𝒒 6 ] \mathbf{Q}=[\boldsymbol{q}_{1},\cdots,\boldsymbol{q}_{6}] is orthonormal. The eigenvalues of 𝐊 env \mathbf{K}_{\mathrm{env}} can be partitioned into the constraint subspace 𝒰 \mathcal{U} with high stiffness λ i ≫ 0 \lambda_{i}\gg 0 and the admissible-motion subspace 𝒯 \mathcal{T} with negligible stiffness λ i ≈ 0 \lambda_{i}\approx 0 , i.e. , for a given threshold ϵ > 0 \epsilon>0 ,

[137] table: 𝒰 ≜ span ⁡ { 𝒒 i : λ i > ϵ } , 𝒯 ≜ span ⁡ { 𝒒 i : λ i ≤ ϵ } \mathcal{U}\triangleq\operatorname{span}\{\boldsymbol{q}_{i}:\lambda_{i}>\epsilon\},\quad\mathcal{T}\triangleq\operatorname{span}\{\boldsymbol{q}_{i}:\lambda_{i}\leq\epsilon\} (18)

[138] p: Compared with Theorem 1 , we can derive the following corollary about spectral-geometric isomorphism.

[139] h6: Corollary 1 (Spectral-Geometric Isomorphism) .

[140] p: The eigenbasis 𝐐 \mathbf{Q} of 𝐊 env \mathbf{K}_{\mathrm{env}} is aligned with the principal axes of the geometric frame Σ geo \Sigma_{\text{geo}} . Consequently, the spectral components map directly to the physical stiffness properties:

[141] p: Eigenvalues ( Λ \boldsymbol{\Lambda} ): The diagonal elements of 𝚲 \boldsymbol{\Lambda} are identically the distributed stiffness integrals derived in the Hertzian model. Specifically, up to a permutation, the spectrum is the set:

[142] table: σ ⁡ ( 𝐊 env ) = { k x ​ x , k y ​ y , k z ​ z , κ x ​ x , κ y ​ y , κ z ​ z } . \sigma(\mathbf{K}_{\mathrm{env}})=\{k_{xx},k_{yy},k_{zz},\kappa_{xx},\kappa_{yy},\kappa_{zz}\}.

[143] p: Constraint Subspace ( 𝒰 \mathcal{U} ): Defined by eigenvectors with significant stiffness eigenvalues ( λ i > ϵ \lambda_{i}>\epsilon ), 𝒰 \mathcal{U} corresponds to geometric directions of hard contact (e.g., 𝐧 \mathbf{n} ).

[144] table: 𝒰 ≡ span ⁡ { 𝐯 ∈ Σ geo ∣ stiffness along ​ 𝐯 ​ is dominant } . \mathcal{U}\equiv\operatorname{span}\{\mathbf{v}\in\Sigma_{\text{geo}}\mid\text{stiffness along }\mathbf{v}\text{ is dominant}\}.

[145] p: Admissible Motion Subspace ( 𝒯 \mathcal{T} ): Defined by eigenvectors with negligible stiffness ( λ i ≤ ϵ \lambda_{i}\leq\epsilon ), 𝒯 \mathcal{T} corresponds to directions of free motion or sliding (e.g., 𝐭 1 , 2 \mathbf{t}_{1,2} ).

[146] h3: Supp. I.2 Task Intent and Interaction Frame

[147] p: While the spectral analysis identifies the geometric orientation of the constraints, it leaves the directionality and semantic assignment of the axes ambiguous. To resolve this, we introduce the task intent as the causal anchor for the interaction frame. Let the task intent ℐ \mathcal{I} be defined by the tuple of the desired interaction wrench and twist at p I p_{I} :

[148] table: ℐ ≜ { 𝝃 ∗ ∈ 𝔰 ​ 𝔢 ​ ( 3 ) , 𝓦 ∗ ∈ 𝔰 ​ 𝔢 ∗ ​ ( 3 ) } . \mathcal{I}\triangleq\{\boldsymbol{\xi}^{*}\in\mathfrak{se}(3),\;\boldsymbol{\mathcal{W}}^{*}\in\mathfrak{se}^{*}(3)\}. (19)

[149] h6: Assumption 1 (Intent Compatibility) .

[150] p: Assume that the task is physically consistent and non-destructive. Specifically, the agent intends to exert forces primarily against environmental constraints and execute motions primarily along admissible freedoms. Mathematically, this implies that the task intent lies within the corresponding spectral subspaces:

[151] table: 𝓦 ∗ ∈ 𝒰 and 𝝃 ∗ ∈ 𝒯 . \boldsymbol{\mathcal{W}}^{*}\in\mathcal{U}\quad\text{and}\quad\boldsymbol{\xi}^{*}\in\mathcal{T}. (20)

[152] p: Since 𝒰 ⟂ 𝒯 \mathcal{U}\perp\mathcal{T} (due to the symmetry of 𝐊 env \mathbf{K}_{\mathrm{env}} ), the force and motion intents are orthogonal: ⟨ 𝓦 ∗ , 𝛏 ∗ ⟩ = 0 \langle\boldsymbol{\mathcal{W}}^{*},\boldsymbol{\xi}^{*}\rangle=0 . Further, we assume that for anisotropic constraints, meaningful task intent naturally aligns with the principal geometric axes. For isotropic constraints like spherical contact, any intent direction within the subspace is valid.

[153] p: To resolve the directional ambiguity and handle co-axial degeneracies, we construct the Interaction Frame (IF) Σ ⁡ ( p I ) \Sigma(p_{I}) by anchoring the spectral axes to the task intent. We pre-define a reference vector 𝐯 ref \mathbf{v}_{\text{ref}} like the current end-effector x x -axis to resolve ambiguities. Next, for the intended wrench and twist, they admit a well-defined screw-axis direction [ 4 ] , represented as 𝐧 𝓦 ∗ \mathbf{n}_{\boldsymbol{\mathcal{W}}^{*}} and 𝐧 𝝃 ∗ \mathbf{n}_{\boldsymbol{\xi}^{*}} , respectively. Notice that we only use the axis direction for frame construction, and the axis location is irrelevant here. The basis vectors { 𝐱 Σ , 𝐲 Σ , 𝐳 Σ } \{\mathbf{x}_{\Sigma},\mathbf{y}_{\Sigma},\mathbf{z}_{\Sigma}\} are derived via the following prioritized scheme:

[154] p: Primary Axis Assignment : The frame definition prioritizes the wrench intent. (1) If the wrench intent is non-negligible, it defines the constraint axis : 𝐳 Σ ≜ 𝐧 𝓦 ∗ \mathbf{z}_{\Sigma}\triangleq\mathbf{n}_{\boldsymbol{\mathcal{W}}^{*}} ; (2) otherwise, the twist intent takes precedence to define the motion axis : 𝐱 Σ ≜ 𝐧 𝝃 ∗ \mathbf{x}_{\Sigma}\triangleq\mathbf{n}_{\boldsymbol{\xi}^{*}} .

[155] p: Secondary Axis with Fallback : The remaining axis is determined by projecting the secondary intent onto the subspace orthogonal to the primary axis. If the secondary intent is degenerate , negligible , or collinear with the primary axis , it fails to define a unique orthogonal direction. In such cases, the definition falls back to the reference vector 𝐯 ref \mathbf{v}_{\text{ref}} . For instance, if 𝐳 Σ \mathbf{z}_{\Sigma} is the primary axis, the motion axis 𝐱 Σ \mathbf{x}_{\Sigma} is computed as 𝐩 / ‖ 𝐩 ‖ \mathbf{p}/\left\|\mathbf{p}\right\| , where vector 𝐩 \mathbf{p} selects the most informative source:

[156] table: 𝐩 = { ( 𝐈 − 𝐳 Σ ​ 𝐳 Σ ⊤ ) ​ 𝐧 𝝃 ∗ if ​ ‖ 𝝃 ∗ ‖ > ϵ ξ ​ and | 𝐳 Σ ⋅ 𝐧 𝝃 ∗ | < 1 − ϵ ∥ , ( 𝐈 − 𝐳 Σ ​ 𝐳 Σ ⊤ ) ​ 𝐯 ref otherwise (fallback) . \mathbf{p}=\begin{cases}(\mathbf{I}-\mathbf{z}_{\Sigma}\mathbf{z}_{\Sigma}^{\top})\mathbf{n}_{\boldsymbol{\xi}^{*}}&\text{if }\|\boldsymbol{\xi}^{*}\|>\epsilon_{\xi}\text{ and }|\mathbf{z}_{\Sigma}\cdot\mathbf{n}_{\boldsymbol{\xi}^{*}}|<1-\epsilon_{\parallel},\\ (\mathbf{I}-\mathbf{z}_{\Sigma}\mathbf{z}_{\Sigma}^{\top})\mathbf{v}_{\text{ref}}&\text{otherwise (fallback)}.\end{cases}

[157] p: where ϵ ξ \epsilon_{\xi} and ϵ ∥ \epsilon_{\parallel} are thresholds for twist and collinearity.

[158] p: Completion : The final axis 𝐲 Σ \mathbf{y}_{\Sigma} is determined via the right-hand rule to complete the orthonormal basis.

[159] p: Thus, we show that the constructed IF can also diagonalizes the environmental stiffness:

[160] h6: Proposition 1 (Intent Alignment) .

[161] p: Under Assumption 1 , the Interaction Frame Σ ⁡ ( p I ) \Sigma(p_{I}) is spatially co-axial with the Principal Geometric Frame Σ geo \Sigma_{\text{geo}} . Consequently, the matrix 𝚽 Σ = diag ⁡ ( 𝐑 Σ , 𝐑 Σ ) \mathbf{\Phi}_{\Sigma}=\operatorname{diag}(\mathbf{R}_{\Sigma},\mathbf{R}_{\Sigma}) formed by the basis of Σ ⁡ ( p I ) \Sigma(p_{I}) diagonalizes the environmental stiffness 𝐊 env \mathbf{K}_{\mathrm{env}} .

[162] p: Proof (Sketch) . Under the assumption, the task intent naturally aligns with the environment’s structural topology: wrenches are exerted against constraints ( 𝒰 \mathcal{U} ), and motions occur along admissible freedoms ( 𝒯 \mathcal{T} ). In scenarios where these subspaces are multi-dimensional ( e.g. , the isotropic radial constraint in peg-in-hole assembly), the stiffness distribution exhibits rotational symmetry, implying that any direction selected by the intent within that subspace constitutes a mathematically valid principal axis. Consequently, the IF constructed from the task intent does not impose an arbitrary structure; rather, it instantiates a specific, physically valid eigenbasis that simultaneously diagonalizes the environmental stiffness matrix and resolves the sign and gauge ambiguities inherent in purely geometric analysis. ∎

[163] h6: Theorem 2 (Co-axial Twist to an Applied Wrench) .

[164] p: Let Σ ⁡ ( p I ) = { 𝐞 1 , … , 𝐞 6 } \Sigma(p_{I})=\{\mathbf{e}_{1},\dots,\mathbf{e}_{6}\} be the Interaction Frame (IF) constructed above, and let 𝚽 Σ = diag ⁡ ( 𝐑 Σ , 𝐑 Σ ) \mathbf{\Phi}_{\Sigma}=\operatorname{diag}(\mathbf{R}_{\Sigma},\mathbf{R}_{\Sigma}) be the corresponding spatial rotation. In the IF, the elastic environment stiffness is diagonal, 𝐊 env Σ = 𝚽 Σ ⊤ ​ 𝐊 env ​ 𝚽 Σ = diag ⁡ ( k 1 , … , k 6 ) \mathbf{K}_{\mathrm{env}}^{\Sigma}=\mathbf{\Phi}_{\Sigma}^{\top}\mathbf{K}_{\mathrm{env}}\mathbf{\Phi}_{\Sigma}=\operatorname{diag}(k_{1},\dots,k_{6}) . Then, for any applied wrench 𝓦 ∗ \boldsymbol{\mathcal{W}}^{*} aligned with a constraint-axis 𝐞 j ∈ 𝒰 \mathbf{e}_{j}\in\mathcal{U} , the induced elastic compliance is co-axial: the resulting pose perturbation δ ​ 𝛘 c \delta\boldsymbol{\chi}_{c} and the corresponding parasitic twist 𝛏 c \boldsymbol{\xi}_{c} are strictly collinear with 𝐞 j \mathbf{e}_{j} .

[165] p: Proof . By Proposition 1 , the basis vectors of the Interaction Frame align with the principal axes of Σ geo \Sigma_{\text{geo}} . Thus, invoking Theorem 1 , the stiffness matrix 𝐊 env \mathbf{K}_{\mathrm{env}} is diagonal in this frame:

[166] table: 𝐊 env Σ = diag ⁡ ( k 1 , … , k 6 ) , \mathbf{K}_{\mathrm{env}}^{\Sigma}=\operatorname{diag}(k_{1},\dots,k_{6}), (21)

[167] p: where k i k_{i} is the stiffness eigenvalue associated with 𝐞 i \mathbf{e}_{i} .

[168] p: For small perturbations, the elastic constitutive relation is

[169] table: 𝓦 el = 𝐊 env Σ ​ δ ​ 𝝌 . \boldsymbol{\mathcal{W}}_{\mathrm{el}}=\mathbf{K}_{\mathrm{env}}^{\Sigma}\,\delta\boldsymbol{\chi}. (22)

[170] p: Consider an applied wrench aligned with the j j -th constraint basis vector: 𝓦 ∗ = β ​ 𝐞 j \boldsymbol{\mathcal{W}}^{*}=\beta\,\mathbf{e}_{j} with 𝐞 j ∈ 𝒰 \mathbf{e}_{j}\in\mathcal{U} and β ∈ ℝ \beta\in\mathbb{R} . We seek the elastic compliance δ ​ 𝝌 c \delta\boldsymbol{\chi}_{c} satisfying 𝐊 env Σ ​ δ ​ 𝝌 c = 𝓦 ∗ \mathbf{K}_{\mathrm{env}}^{\Sigma}\,\delta\boldsymbol{\chi}_{c}=\boldsymbol{\mathcal{W}}^{*} . Since 𝐞 j ∈ 𝒰 \mathbf{e}_{j}\in\mathcal{U} , by definition its associated stiffness satisfies k j > 0 k_{j}>0 , hence the scalar equation k j ​ δ ​ χ j = β k_{j}\,\delta\chi_{j}=\beta admits the unique solution δ ​ χ j = β / k j \delta\chi_{j}=\beta/k_{j} . Therefore,

[171] table: δ ​ 𝝌 c = ( β k j ) ​ 𝐞 j , \delta\boldsymbol{\chi}_{c}=\left(\frac{\beta}{k_{j}}\right)\mathbf{e}_{j}, (23)

[172] p: and substituting back verifies

[173] table: 𝐊 env Σ ​ δ ​ 𝝌 c = ( β k j ) ​ 𝐊 env Σ ​ 𝐞 j = ( β k j ) ​ ( k j ​ 𝐞 j ) = β ​ 𝐞 j = 𝓦 ∗ . \mathbf{K}_{\mathrm{env}}^{\Sigma}\,\delta\boldsymbol{\chi}_{c}=\left(\frac{\beta}{k_{j}}\right)\mathbf{K}_{\mathrm{env}}^{\Sigma}\mathbf{e}_{j}=\left(\frac{\beta}{k_{j}}\right)(k_{j}\mathbf{e}_{j})=\beta\mathbf{e}_{j}=\boldsymbol{\mathcal{W}}^{*}. (24)

[174] p: Thus, δ ​ 𝝌 c \delta\boldsymbol{\chi}_{c} is strictly collinear with the applied wrench. Assuming the control loop or integration preserves directionality, the resulting twist 𝝃 c \boldsymbol{\xi}_{c} aligns with δ ​ 𝝌 c \delta\boldsymbol{\chi}_{c} , thus 𝝃 c | 𝐞 j \boldsymbol{\xi}_{c}\parallel\mathbf{e}_{j} . ∎

[175] h6: Proposition 2 (Co-axial Wrench to an Applied Twist) .

[176] p: In the IF Σ ⁡ ( p I ) \Sigma(p_{I}) , consider an intended twist 𝛏 ∗ = α ​ 𝐞 i \boldsymbol{\xi}^{*}=\alpha\,\mathbf{e}_{i} along a principal axis 𝐞 i ∈ 𝒯 \mathbf{e}_{i}\in\mathcal{T} . If the local dissipative mechanism is isotropic and the contact patch (or its macroscopic stiffness/friction distribution) is reflectionally symmetric with respect to the plane spanned by 𝐞 i \mathbf{e}_{i} and the contact normal, then the induced dissipative wrench must be co-axial:

[177] table: 𝓦 c = 𝓦 dis ​ ( 𝝃 ∗ ) | 𝝃 ∗ , 𝓦 c ⊤ ​ 𝝃 ∗ ≤ 0 . \boldsymbol{\mathcal{W}}_{c}=\boldsymbol{\mathcal{W}}_{\mathrm{dis}}(\boldsymbol{\xi}^{*})\parallel\boldsymbol{\xi}^{*},\qquad\boldsymbol{\mathcal{W}}_{c}^{\top}\boldsymbol{\xi}^{*}\leq 0. (25)

[178] p: Proof (Sketch) . Under the stated symmetries, there is no distinguished lateral direction orthogonal to 𝐞 i \mathbf{e}_{i} that can bias the dissipative response. Hence any lateral component of 𝓦 c \boldsymbol{\mathcal{W}}_{c} would break reflectional symmetry and is therefore forbidden; the only admissible direction is the axis of motion 𝐞 i \mathbf{e}_{i} . Moreover, dissipation opposes motion, yielding 𝓦 c ⊤ ​ 𝝃 ∗ ≤ 0 \boldsymbol{\mathcal{W}}_{c}^{\top}\boldsymbol{\xi}^{*}\leq 0 . ∎

[179] p: Therefore, the intended twist 𝝃 ∗ \boldsymbol{\xi}^{*} may induce a parasitic wrench 𝓦 c \boldsymbol{\mathcal{W}}_{c} along its direction (Proposition 2 ), and the intended wrench 𝓦 ∗ \boldsymbol{\mathcal{W}}^{*} may induce a parasitic twist 𝝃 c \boldsymbol{\xi}_{c} along its direction (Theorem 2 ). Since 𝓦 c | 𝝃 ∗ ⟂ 𝓦 ∗ | 𝝃 c \boldsymbol{\mathcal{W}}_{c}\parallel\boldsymbol{\xi}^{*}\perp\boldsymbol{\mathcal{W}}^{*}\parallel\boldsymbol{\xi}_{c} ,

[180] table: 𝑷 = ( 𝓦 ∗ + 𝓦 c ) ⊤ ​ ( 𝝃 ∗ + 𝝃 c ) = 𝓦 c ⊤ ​ 𝝃 ∗ + 𝓦 ∗ ⁣ ⊤ ​ 𝝃 c , \boldsymbol{P}=(\boldsymbol{\mathcal{W}}^{*}+\boldsymbol{\mathcal{W}}_{c})^{\top}(\boldsymbol{\xi}^{*}+\boldsymbol{\xi}_{c})=\boldsymbol{\mathcal{W}}_{c}^{\top}\boldsymbol{\xi}^{*}+\boldsymbol{\mathcal{W}}^{*\top}\boldsymbol{\xi}_{c}, (26)

[181] p: which establishes the foundation of the approximation strategy described in the paper.

[182] h2: Supp. II Interaction Structure Discovery

[183] figure: Fig. 7: Sensor Signal Ambiguity. Similar sensor signals (wrench and twist) can lead to different interaction types and structures.

[184] figure: Fig. 8: Visualization of the Interaction Frame and the Task Mode on the Push and Flip Task.

[185] figure: Fig. 9: Visualization of the Interaction Frame and the Task Mode on the Plug in EV Charger Task.

[186] figure: Fig. 10: Visualization of the Interaction Frame and the Task Mode on the Scrape off Sticker Task.

[187] h3: Supp. II.1 High-Level Knowledge

[188] p: To distinguish between dissipative and structural residuals as the dominant power source, our method leverages high-level knowledge. Addressing potential doubts regarding the necessity of this prior information, we posit that twist and wrench signals are inherently ambiguous and cannot, on their own, reveal the nature of the power source.

[189] p: Justification. From the perspective of sensor observation, the instantaneous power input P = 𝓦 ⊤ ​ 𝝃 P=\boldsymbol{\mathcal{W}}^{\top}\boldsymbol{\xi} represents the energy transfer from the robot to the environment. However, this scalar value does not reveal the destination of the energy. For instance, as shown in Fig. 7 , a robot pushing a heavy block against friction (dissipative) and compressing a stiff spring (structural) can exhibit identical force-velocity profiles and positive work. Without high-level knowledge (e.g., object properties or task semantics) to characterize the environment’s admittance, the raw signals cannot distinguish whether the energy is being dissipated as heat or stored as potential energy.

[190] figure: Fig. 11: Visualization of Different IF Recovery Methods on the Scrape Off Sticker Task. Wrench-only IF recovery methods couple friction directions, whereas our IF recovery method better aligns with the ground-truth (the world z z -axis).

[191] h3: Supp. II.2 Visualization and Analysis

[192] p: To qualitatively validate the physical consistency of our approach, we visualize the recovered Interaction Frames (IF) across multiple expert demonstrations for three contact-rich tasks: Push and Flip (Fig. 8 ), Plug in EV Charger (Fig. 9 ), and Scrape off Sticker (Fig. 10 ). As illustrated, our IF recovery method consistently aligns the frame axes with the underlying task geometry across varying demonstrations, verifying that the recovered spectral axes are topologically stable.

[193] p: A key advantage of our proposed method is its adaptivity to different types of task. In the Scrape off the Sticker task (Fig. 11 ), we explicitly compare our IF recovery method against a baseline constructed directly from raw interaction wrenches [ 53 ] , where the z z -axis is aligned with the total measured force vector. In this task, significant tangential friction is generated during the scraping motion. For the wrench-based baseline, this friction acts as a parasitic wrench, causing the total force vector to deviate from the surface normal. Consequently, the baseline recovers a tilted frame that is coupled with the motion direction rather than the surface geometry, leading to substantially worse policy learning results.

[194] h2: Supp. III Force Policy

[195] p: In this section, we provide the detailed architecture and implementation specifications of our policy framework, comprising the global vision policy Π global \Pi_{\text{global}} and the local force policy Π local \Pi_{\text{local}} .

[196] p: Global Vision Policy ( Π global \Pi_{\text{global}} ). We instantiate the global policy using RISE-2 [ 31 ] . RISE-2 acts as a generalizable trajectory generator operating on global 3D point cloud observations. For our specific pipeline, we first train RISE-2 following its official implementation and freeze it during local force policy training. Let I t ′ I_{t^{\prime}} denote the global observation at a low-frequency time step t ′ t^{\prime} . The global policy processes this input to generate a latent action embedding, which is typically used to condition its internal diffusion head. In our framework, we intercept this embedding to serve as the global visual feature, denoted as ϕ ⁡ ( I t ′ ) ∈ ℝ 512 \phi(I_{t^{\prime}})\in\mathbb{R}^{512} . This feature encapsulates high-level intent and geometry, guiding the local policy.

[197] p: Local Force Policy ( Π local \Pi_{\text{local}} ). The local policy Π local \Pi_{\text{local}} operates at a high frequency to handle contact-rich interactions. It consists of a multi-modal encoder, a feature fusion module, and a dual-head action decoder. The input to Π local \Pi_{\text{local}} includes a wrist-mounted camera image I t ( w ) ∈ ℝ H × W × 3 I_{t}^{(w)}\in\mathbb{R}^{H\times W\times 3} and a history of end-effector poses s t ∈ ℝ T × 9 s_{t}\in\mathbb{R}^{T\times 9} (represented in continuous rotation [ 93 ] format) and wrenches 𝒲 t ∈ ℝ T o × 6 \mathcal{W}_{t}\in\mathbb{R}^{T_{o}\times 6} .

[198] p: Vision Encoder. We process the wrist image I t I_{t} using a lightweight ResNet-18 [ 35 ] backbone. To integrate the global context, we employ Feature-wise Linear Modulation (FiLM) [ 64 ] . The global feature ϕ ⁡ ( I t ′ ) \phi(I_{t^{\prime}}) is projected to generate scale γ \gamma and shift β \beta parameters, which modulate the intermediate feature maps of the ResNet:

[199] table: FiLM ​ ( x i ∣ ϕ ⁡ ( I t ′ ) ) = γ i ​ ( ϕ ⁡ ( I t ′ ) ) ⋅ x i + β i ​ ( ϕ ⁡ ( I t ′ ) ) , \text{FiLM}(x_{i}\mid\phi(I_{t^{\prime}}))=\gamma_{i}(\phi(I_{t^{\prime}}))\cdot x_{i}+\beta_{i}(\phi(I_{t^{\prime}})),

[200] p: where x i x_{i} represents the feature map at the i i -th block. The final spatial features are pooled and projected to a visual embedding z vis ∈ ℝ 128 z_{\text{vis}}\in\mathbb{R}^{128} .

[201] p: Proprioceptive Encoder: The proprioceptive history, consisting of end-effector poses and wrenches, is encoded using a Gated Recurrent Unit (GRU) [ 21 ] . To incorporate the global context, we apply FiLM conditioning [ 64 ] to the linear projections at both the input and output of the GRU. Specifically, the global feature ϕ ⁡ ( I t ′ ) \phi(I_{t^{\prime}}) modulates the proprioceptive features before they enter the recurrent unit and again after they exit. The final hidden state serves as the proprioceptive embedding z prop ∈ ℝ 128 z_{\text{prop}}\in\mathbb{R}^{128} .

[202] p: Adaptive Gated Fusion. To effectively integrate the local sensory feedback with the high-level global intent, we employ a tri-modal adaptive gating mechanism. This allows the policy to dynamically weigh the importance of wrist vision, proprioception, and global context depending on the interaction phase. We first project the global feature ϕ ⁡ ( I t ′ ) \phi(I_{t^{\prime}}) to the local embedding dimension via a linear layer W p W_{p} . The fusion weights and the final embedding are computed as:

[203] table: z global \displaystyle z_{\text{global}} = W p ​ ϕ ​ ( I t ′ ) , \displaystyle=W_{p}\phi(I_{t^{\prime}}), [ 𝜶 1 , 𝜶 2 , 𝜶 3 ] \displaystyle[\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}] = softmax ​ ( W g ​ [ z vis ; z prop ; z global ] + b g ) , \displaystyle=\text{softmax}\left(W_{g}[z_{\text{vis}};z_{\text{prop}};z_{\text{global}}]+b_{g}\right), z fused \displaystyle z_{\text{fused}} = 𝜶 1 ⊙ z vis + 𝜶 2 ⊙ z prop + 𝜶 3 ⊙ z global , \displaystyle=\boldsymbol{\alpha}_{1}\odot z_{\text{vis}}+\boldsymbol{\alpha}_{2}\odot z_{\text{prop}}+\boldsymbol{\alpha}_{3}\odot z_{\text{global}},

[204] p: where the softmax is applied across the modality dimension, ensuring the gates sum to one.

[205] p: Interaction Structure Head. Multi-layer perceptrons with three dense layers (sizes [128, 64, D o ​ u ​ t D_{out} ]) are used to predict the task-oriented structural parameters. These head output: (1) the interaction frame pose relative to the end-effector pose Σ IF ∈ ℝ 9 \Sigma_{\text{IF}}\in\mathbb{R}^{9} (also represented in continuous rotation format), (2) the reference wrench 𝒲 ref ∈ ℝ 6 \mathcal{W}_{\text{ref}}\in\mathbb{R}^{6} , and (3) a binary selection mask S ∈ { 0 , 1 } 6 S\in\{0,1\}^{6} indicating the active control mode.

[206] p: Action Head. We utilize a MIP head [ 63 ] to generate precise control commands at high frequency. Conditioned on the fused feature z fused z_{\text{fused}} , this head predicts a sequence of 50Hz robot actions in an action chunking [ 91 ] format to ensure temporal consistency. Specifically, at each time step t t , the head outputs a chunk of T a T_{a} future relative actions. At the execution frequency of 50Hz, the policy executes the first action of the chunk and discards the rest, following a receding horizon control strategy.

[207] p: Training. The entire local force policy is trained end-to-end. We optimize the model using the AdamW optimizer with a learning rate of 10 − 4 10^{-4} and a cosine annealing schedule. The total loss function ℒ \mathcal{L} is a weighted sum of the diffusion-based action loss and the auxiliary interaction structure losses:

[208] table: ℒ = λ act ​ ℒ MIP + λ frame ​ ℒ frame + λ wrench ​ ℒ wrench + λ mask ​ ℒ mask , \mathcal{L}=\lambda_{\text{act}}\mathcal{L}_{\text{MIP}}+\lambda_{\text{frame}}\mathcal{L}_{\text{frame}}+\lambda_{\text{wrench}}\mathcal{L}_{\text{wrench}}+\lambda_{\text{mask}}\mathcal{L}_{\text{mask}},

[209] p: where ℒ MIP \mathcal{L}_{\text{MIP}} is the action prediction MSE loss for the MIP head, and ℒ frame \mathcal{L}_{\text{frame}} , ℒ wrench \mathcal{L}_{\text{wrench}} , and ℒ mask \mathcal{L}_{\text{mask}} correspond to the regression and classification losses for the interaction frame, reference wrench, and selection mask, respectively. We empirically set the weights λ act = λ frame = λ wrench = 1.0 \lambda_{\text{act}}=\lambda_{\text{frame}}=\lambda_{\text{wrench}}=1.0 and λ mask = 0.1 \lambda_{\text{mask}}=0.1 to balance the task objectives.

[210] p: Our local force policy can execute inference at 50Hz, and we let it output 50Hz control commands and directly takes over the controller if the router switches to fast.

[211] h2: Supp. IV Dual-Policy Asynchronous Scheduler

[212] h3: Supp. IV.1 Chunk Alignment with DTW

[213] p: Let 𝐏 = { p 0 , p 1 , … , p N − 1 } \mathbf{P}=\{p_{0},p_{1},\ldots,p_{N-1}\} denote the trajectory sequence predicted by the model, and 𝐇 = { h − M + 1 , … , h 0 } \mathbf{H}=\{h_{-M+1},\ldots,h_{0}\} denote the robot’s recently executed historical trajectory, where h 0 h_{0} represents the current position. Our objective is to find the optimal starting index k ∗ k^{*} such that execution beginning from p k ∗ p_{k^{*}} achieves a smooth transition with the current state.

[214] p: We define the frame-wise cost function as:

[215] table: c ⁡ ( p i , h j ) = \displaystyle c(p_{i},h_{j})= w pos ​ ‖ p i pos − h j pos ‖ \displaystyle w_{\text{pos}}\|p_{i}^{\text{pos}}-h_{j}^{\text{pos}}\| (27) + w ori ​ d ang ​ ( p i ori , h j ori ) \displaystyle+w_{\text{ori}}d_{\text{ang}}(p_{i}^{\text{ori}},h_{j}^{\text{ori}}) + w vel ​ ‖ p ˙ i − h ˙ j ‖ , \displaystyle+w_{\text{vel}}\|\dot{p}_{i}-\dot{h}_{j}\|,

[216] p: where w pos w_{\text{pos}} , w ori w_{\text{ori}} , and w vel w_{\text{vel}} are the weights for position, orientation, and velocity, respectively, and p ˙ i \dot{p}_{i} and h ˙ j \dot{h}_{j} are velocities estimated via finite differences. We apply the Dynamic Time Warping (DTW) algorithm [ 59 ] to establish alignment between the beginning of the predicted trajectory and the end of the historical trajectory. By backtracking along the optimal path, we identify the optimal frame index k ∗ k^{*} corresponding to the current robot position h 0 h_{0} . Additionally, we compensate for the latency of the DTW computation itself:

[217] table: k ∗ ← k ∗ + ⌈ t DTW Δ ​ t ⌉ . k^{*}\leftarrow k^{*}+\left\lceil\frac{t_{\text{DTW}}}{\Delta t}\right\rceil. (28)

[218] p: where Δ ​ t \Delta t denotes the scheduler execution period. In practice, the DTW procedure requires approximately 20ms to compute the optimal transition point, which corresponds to dropping an additional 1-2 steps at 50 Hz to compensate for DTW latency. Executing the trajectory from index k ∗ k^{*} ensures smooth continuity with the current state in both position and velocity, thereby avoiding abrupt transitions.

[219] h3: Supp. IV.2 Broader Impact on General Policies

[220] p: During experiments, we find that the asynchronous scheduler not only improves the smoothness of Force Policy , but also enhances the performance of vision-only policies in contact-rich tasks through its waypoint dropout strategy and acceleration-continuous interpolation. In particular, the asynchronous scheduler leads to more stable contact behaviors for vision-only policies. We evaluate this effect using RISE-2 [ 31 ] and π 0.5 \pi_{0.5} [ 7 ] as representative vision-only visuomotor and vision-language-action models, respectively. Their performance is compared against conventional sequential inference and execution with temporal ensemble [ 91 ] , as well as our asynchronous scheduler with DTW-based waypoint dropout during inference, on the Push and Flip task.

[221] figure: Policy w/ Scheduler? Success Rate ↑ \uparrow Avg. d d (mm) ↓ \downarrow push flip RISE-2 [ 31 ] 100.0 % 42.5% 0.86 ✓ 100.0 % 62.5 % 0.00 π 0.5 \pi_{0.5} [ 7 ] 80.0% 52.5% 0.00 ✓ 95.0 % 77.5 % 0.00 TABLE V: Evaluation of Schedulers for Vision-Only Policies on the Push and Flip Task. Asynchronous scheduler improves the performance and make the contact more stable.

[222] p: The experimental results demonstrate a significant positive impact. Specifically, as shown in Table V , the asynchronous scheduler consistently boosts the success rates and reduces control error across different policy architectures. For RISE-2, while the pushing success rate remains perfect, the flipping success rate sees a substantial improvement from 42.5% to 62.5%, and the average displacement error drops to zero. Similarly, for the VLA model π 0.5 \pi_{0.5} , applying our scheduler yields improvements in both sub-tasks, raising the flipping success rate to 77.5%.

[223] p: We attribute these gains primarily to the DTW-based waypoint dropout mechanism in preventing contact loss. Vision-based policies often suffer from temporal inconsistencies between action chunks [ 2 , 9 ] , occasionally predicting erroneous “retreating” motions (backward fluctuations relative to the task progress). In contact-rich manipulation like flipping, such retreating actions can cause the end-effector to momentarily detach from the object surface, leading to a complete loss of the established contact state and subsequent failure. By aligning the predicted chunk with the current execution progress via DTW and dropping these inconsistent preceding waypoints, our scheduler ensures a monotonic and continuous interaction profile, thereby maintaining stable contact throughout the maneuver. This highlights the potential of our scheduler as a plug-and-play module for enhancing the physical robustness of general visuomotor policies.

[224] h2: Supp. V Experiment Details

[225] h3: Supp. V.1 Task Design

[226] p: We carefully designed an evaluation suite comprising three distinct tasks that span two fundamental categories of contact-rich manipulation: surface polishing and peg-in-hole insertion . While many prior works limit their evaluation to a single interaction category, our benchmark covers both continuous surface tracking and geometric constrained assembly. Furthermore, we upgraded the task designs to elevate their difficulty, thereby offering a more rigorous assessment of each policy’s capabilities. The task descriptions are shown as follows.

[227] p: Push and Flip . Inspired by [ 47 ] but with slight modifications, this task requires the robot to push an object until it contacts a wall (formed by a large heavy object), and then flip the box upright using both the ground and the wall. The task poses 3 key challenges: (1) correctly sensing contact and switching to the flipping phase; switching too early loses contact, while switching too late pushes the heavy object; (2) exerting forces along changing directions during flipping; and (3) avoiding applying excessive forces that would push the heavy object.

[228] p: Plug in EV Charger . Inspired by [ 90 ] but with modifications, this task requires the robot to plug an EV charger into a socket. Unlike the original task in [ 90 ] , our fast-charging socket has tighter tolerances and requires sufficiently large insertion forces (approximately 160N) to achieve full engagement. The task poses 3 key challenges: (1) precisely aligning the plug with the socket under tight tolerances; (2) sensing incorrect contact with the socket surface and adjusting the insertion direction based on force feedback; and (3) exerting sufficiently large forces to complete insertion without causing jamming.

[229] p: Scrape off Sticker . This task is self-designed and requires the robot to scrape stickers off a surface. It is divided into an easy and a hard version. In the easy version, the robot only needs to scrape the side without glue, so merely establishing contact is sufficient. In the hard version, the robot must scrape the side with glue, requiring the application of sufficient force (approximately 35N) to remove the sticker. The task poses 3 key challenges: (1) maintaining stable contact while moving along the surface, (2) sensing and adjusting forces to successfully remove stickers with glue, and (3) avoiding excessive forces that could damage the surface or the object.

[230] h3: Supp. V.2 Data Collection

[231] p: Recently, a growing body of teleoperation systems incorporate haptic feedback [ 87 , 92 , 44 , 5 , 69 ] . However, many implementations provide haptics through visual cues or vibrotactile signals, rather than delivering physically faithful force feedback. Alternatives include kinesthetic teaching [ 38 ] , handheld interfaces [ 19 , 53 , 22 ] , and exoskeleton-based systems [ 30 , 31 , 29 ] . For contact-rich manipulation, high-quality demonstrations typically require both accurate robot state sensing and a global-view camera to support the global vision policy. We therefore adopt arm-to-arm teleoperation [ 56 ] , which mirrors the interaction forces measured on the follower arm back to the operator’s controller arm. This design enables high-fidelity force feedback and substantially improves demonstration quality. For example, in Push and Flip , the operator maintains a contact force of roughly 10N-20N to prevent overloading; in Scrape off Sticker , the operator regulates the contact force within 35N–50N to fully remove the sticker. Then, we collect 50 high-quality demonstrations for each task as the training data. The RGB-D images are recorded at 15Hz, and the robot states (including end-effector pose, end-effector velocity, and force/torque signals) are recorded at 1000Hz.

[232] h3: Supp. V.3 Baselines

[233] p: In this work, we compare our method against several baselines, including vision-only visuomotor policies [ 31 ] , vision-language-action (VLA) models [ 7 ] , force-aware visuomotor policies [ 36 , 87 ] , and force-aware VLA models [ 88 , 90 ] .

[234] p: RISE-2 [ 31 ] , a generalizable visuomotor policy that fuses sparse 3D geometric features with dense 2D semantic features for action prediction.

[235] p: 𝝅 0.5 \boldsymbol{\pi}_{0.5} [ 7 ] , a VLA model exhibiting open-world generalization capabilities, co-trained on heterogeneous tasks across large-scale robotic datasets [ 24 , 11 , 28 ] .

[236] p: FoAR [ 36 ] , a force-aware visuomotor policy based on RISE [ 82 ] that selectively integrates force features utilizing a future contact predictor.

[237] p: RDP [ 87 ] , a slow-fast force-aware reactive policy based on Diffusion Policy (DP) [ 18 ] . It uses a fast force-aware tokenizer for latent action encoding/decoding and utilizes a latent diffusion policy to predict latent action chunks.

[238] p: ForceVLA [ 88 ] , a force-aware VLA model based on π 0 \pi_{0} [ 8 ] that incorporates a mixture-of-experts (MoE) architecture [ 41 ] for vision-language-force fusion.

[239] p: TA-VLA [ 90 ] , a force-aware VLA model based on π 0 \pi_{0} [ 8 ] that leverages observed torque sequences as input and predicts future torque as an auxiliary supervision.

[240] p: To ensure a fair comparison, we utilize 6-DoF force/torque signals measured at the end-effector as the force input/output for all baselines. All other hyperparameters adhere to the specifications in their respective official implementations.

[241] h3: Supp. V.4 Metrics

[242] p: We use stage-wise, accumulated success rates as the primary metric for each task. The partial successes (recorded as 0.5) for the “flip” stage of Push and Flip and the “plug in” stage of Plug in EV Charger are demonstrated in Fig. 12 .

[243] figure: Fig. 12: Evaluation Metrics Explanation of Partial Success.

[244] figure: Fig. 13: Failure Analyses on the Push and Flip Task. Most failures arise from attempting to flip the object without first establishing contact with the wall. Force-aware policies using position control often exhibit unstable or unintended contacts.

[245] figure: Fig. 14: Failure Analyses on the Scrape off Sticker (Hard) Task. Force-aware VLA models typically fail to establish stable contact with the surface. All baselines usually cannot exert sufficient and stable force to scrape off the sticker.

[246] figure: Fig. 15: Objects in Generalization Evaluation. Unseen objects of different colors, geometries, and stiffnesses are selected to evaluate the generalization ability of the policies.

[247] h3: Supp. V.5 Failure Analyses

[248] p: We summarize typical failure cases on Push and Flip in Fig. 13 . Most failures occur when the policy attempts to flip the object before establishing contact with the wall. This issue is especially pronounced for vision-only policies due to the absence of force feedback. Notably, many force-aware baselines exhibit the same failure mode: it is difficult to learn the critical “contact-then-transition” logic from demonstrations alone, as the transition happens within roughly 50ms in human executions. RDP shows an additional failure pattern. When its predicted latent action chunk corresponds to pushing, but it unexpectedly pushes the box to reach the wall, the resulting out-of-distribution force signals can destabilize the fast tokenizer, producing erratic actions that induce incorrect rotations and ultimately lead to failure. Finally, force-aware methods that rely on position control often struggle to maintain stable contact during the flip, causing the box to slip or drop and preventing task completion. On the contrary, our Force Policy utilizes force control to establish and maintain contact, effectively mitigating the issues that occur in baselines.

[249] p: For Plug in EV Charger , most approaches fail to apply sufficient force to fully seat the connector in the socket. This task is particularly challenging because the required insertion force is close to the robotic arm’s torque limits, and small motion errors or interaction frame estimation inaccuracies can trigger the hardware protection mechanisms and terminate execution. Our Force Policy can also encounter this failure mode. Addressing it likely requires finer-grained, more accurate force regulation (especially near saturation), which we leave as an important direction for future work.

[250] p: Typical failure cases on Scrape off Sticker (Hard) are shown in Fig. 14 . Force-aware VLA models such as TA-VLA and ForceVLA often fail to establish contact with the surface, suggesting that noisy force measurements can hinder vision-guided global motion, which is consistent with the observation in [ 36 ] . Across baselines, another common failure mode is insufficient and unstable contact force: policies frequently lose contact and revert to smaller forces, leaving the sticker partially intact. In contrast, Force Policy leverages explicit force regulation, using predicted control parameters to maintain the desired contact force in the desired direction, which yields a substantial performance improvement.

[251] h3: Supp. V.6 Generalization Evaluation

[252] p: To rigorously evaluate the robustness of our learned policy, we curated a diverse set of unseen test objects for the Push and Flip task. These objects were specifically selected to introduce significant domain shifts relative to the training distribution, probing the policy’s ability to adapt to variations in physical properties and visual appearance. A complete catalog of these objects is visualized in Fig. 15 . The test set is categorized along three primary axes of variation:

[253] p: Geometric Variation. The objects feature distinct geometric profiles, ranging from standard cuboids to irregular shapes and cylinders ( e.g. , cylindrical cup). Variations in aspect ratio and edge curvature challenge the policy’s ability to locate stable contact points and execute precise flipping motions without prior shape knowledge.

[254] p: Stiffness and Material Compliance. Variations in object stiffness are critical for evaluating physical adaptation for force-aware policies. The test set includes rigid objects like the hard wooden block and deformable objects like the soft sponge. These materials have different force-deformation properties, requiring the policy to dynamically adjust its commands to maintain effective interaction without crushing soft objects or slipping on hard ones.

[255] p: Visual Appearance. To test visual generalization, we included objects with colors and textures that were not present in the training dataset. This includes objects with complex textures ( e.g. , square box) and different colors ( e.g. , purple box), ensuring that the policy is robust to perceptual noise.

[256] figure: Fig. 16: Contact Robustness of Force Policy under Disturbances in the Push and Flip Task. Force Policy is robust under human disturbances and can perform autonomous recovery during the contact phase.

[257] p: As demonstrated in the experiments, our method successfully generalizes across these categories, attributing its success to the explicit modeling of the interaction frame and the adaptive fusion of proprioceptive feedback, which compensates for visual ambiguities and geometric uncertainties.

[258] h3: Supp. V.7 Contact Robustness

[259] p: To evaluate the policy’s stability in unstructured physical interactions, we introduced unexpected human disturbances during the contact maintenance phase in the Push and Flip task. As depicted in Fig. 16 , the proposed Force Policy demonstrates significant robustness against unmodeled disturbances. A key characteristic of the policy is the explicit regulation of the interaction wrench. When the human operator physically interferes with the robot, the policy adapts the end-effector pose to maintain the target wrench 𝓦 ∗ \boldsymbol{\mathcal{W}}^{*} .

[260] p: This mechanism is critical for ensuring contact stability. Force Policy prioritizes the stability of the contact force over geometric strictness in an adaptive manner. By dynamically adjusting the robot’s pose to satisfy the force constraint, the system effectively absorbs the disturbance. Consequently, the contact force remains smooth and constant despite external disturbances, verifying the policy’s ability to maintain stable physical interaction under uncertainty.

[261] h3: Supp. V.8 Demonstration Overview

[262] p: We visualize the initial configurations of all 50 demonstrations for each task in Fig. 17 . The objects are randomly placed within the workspace during demonstration collection.

[263] h3: Supp. V.9 Evaluation Overview

[264] p: We visualize the evaluation configurations for each task in Fig. 18 . These configurations are randomly initialized before any policy is trained or tested, following previous practices in [ 86 , 19 , 31 ] for fair comparisons.

[265] figure: Fig. 17: Demonstration Overview for Each Task. We visualize the initial configurations from 50 demonstrations for each task.

[266] figure: Fig. 18: Evaluation Configurations for Each Task. These configurations are randomly initialized beforehand.

[267] h2: Instructions for reporting errors

[268] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[269] p: Tip: You can select the relevant text first, to include it in your report.

[270] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[271] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
