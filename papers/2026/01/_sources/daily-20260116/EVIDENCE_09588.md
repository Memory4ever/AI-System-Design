# Energy-Entropy Regularization exact-v1 necessary evidence

Source: https://arxiv.org/html/2601.09588v1 ; fetched2026-10-03. Main§3/5–8 read; AppendixB.3 needed only for potentialcontraction inconsistency notallphysicalappendix. Proposed2+1+2=5. Not excluded smallmodel.

Critical limitation:§3.1Tsallis denominator1-q whereas§5.5q-1; theoremZnext=F(X+Z) vs real§5 residualZnext=Z+F(X+Z). Contractivity of F cannot directly imply residualI+F contractive. q∈(1,2], norm ball||X/Z||≤1,||Wv||F≤1/2 assumptions not verified forfulltrainedMLP/LayerNorm. ToyInduction d8 singlehead 25recurrence,trainL16–64 evalL1000; FOP d64 additionallyLR/WD/batch/steps differ; no samearchCE/regularizer ablation, no numericseed uncertainty. A100TF32 vs CPUFP32 noiseclaim notcontrolledhardware effects. Do not adoptglobalminimum/funnelconvexness/thermodynamiccause or language reasoningguarantee. Retain limitedauxiliarylossproposal and locally reportedlengthgeneralization, root 已实际核定义/Theorem3.2/§5 residual与entropy：中心保证 Disputed 暂缓隔离，不入Books，不降分删claim。重开仅需修正theorem与实际update/entropy符号映射，并给matchedregularizer关键反证；不遍历物理附录。

## Primary main-text excerpt (from background through conclusion)

nian dynamical system defined by the state ( Z i , V i ) (Z_{i},V_{i}) , where Z i Z_{i} represents the latent position and V i V_{i} its velocity. The model moves across a manifold of potential wells induced by input tokens. By introducing a gravitational-like gradient term, − β ∇ E -\beta\nabla E , we characterize the optimization process as a search for narrow solution wells on a landscape of local minima. We demonstrate, however, that a naive Hamiltonian formulation is insufficient for convergence, as the underlying landscape geometry remains too rugged to support stable orbital decay without additional damping.


 3. Energy-Entropy Regularized (EER) Loss Landscape. Combining the contraction bound from Section 1 and the dynamical framework from Section 2, we propose a novel reformulation of the training objective. Rather than modifying the Transformer architecture, we introduce Energy-Entropy Regularization penalties that fundamentally reshape the loss landscape into a funnel-like geometry. This transformation smoothens the optimization path, facilitating reliable convergence even in extremely low-dimensional structure ( d = 8 d=8 ). The resulting landscape structure significantly enhances both parameter efficiency and out-of-distribution length generalization.



 2 Background


 While traditional Transformers achieve expressive power through large depth, looped transformers [ Giannou et al.(2023) ] prioritize parameter efficiency and iterative refinement by weight-sharing across successive layers. This architectural choice shifts the paradigm from hierarchical feature extraction to the evolution of a discrete-time dynamical system. To achieve stable computation, a single-head Looped Transformer need to converge to a fixed-point, analogous to the framework of Deep Equilibrium Models (DEQ) [ Bai et al.(2019) ] .


 We formulate the single-head looped Transformer as an iterative mapping f θ : 𝒳 → 𝒳 f_{\theta}:\mathcal{X}\to\mathcal{X} on the latent sequence space. By the Banach Fixed-Point Theorem, the iteration x t + 1 = f θ ​ ( x t ) x_{t+1}=f_{\theta}(x_{t}) converges to a unique fixed point x ∗ = f θ ​ ( x ∗ ) x^{*}=f_{\theta}(x^{*}) provided that f θ f_{\theta} is a contraction mapping. This stability is guaranteed if the mapping satisfies the Lipschitz condition d ⁡ ( f θ ​ ( x ) , f θ ​ ( y ) ) ≤ L ⋅ d ⁡ ( x , y ) d(f_{\theta}(x),f_{\theta}(y))\leq L\cdot d(x,y) with a Lipschitz constant L < 1 L<1 .


 In practice, ensuring this contractive property is non-trivial. The inherent non-linearity of the Softmax-normalized attention scores often leads to expansive rather than contractive dynamics, resulting in numerical instability or oscillatory behavior during iterative inference. Consequently, training a single-head looped transformer requires specialized regularization to engineer the loss landscape such that a stable, contractive basin of attraction emerges.



 3 Entropy Contraction for Training Stability


 In this section, we will establish an entropy contractive bound by applying the Tsallis entropy on the attention matrix of single head looped transformer to ensure training stability.


 3.1 Tsallis Entropy


 Tsallis entropy provides a natural extension of this classical entropy measure. Given w w possible outcomes with probabilities p 1 , … , p w p_{1},\ldots,p_{w} , the Tsallis entropy is defined as




 S q = ζ ​ 1 − ∑ i = 1 w p i q 1 − q , S_{q}=\zeta\,\frac{1-\sum_{i=1}^{w}p_{i}^{q}}{1-q},


 where ζ \zeta is the Boltzmann constant, q ∈ ℝ ∖ { 1 } q\in\mathbb{R}\setminus\{1\} , and ∑ i = 1 w p i = 1 \sum_{i=1}^{w}p_{i}=1 . Tsallis entropy reduces to the Boltzmann–Gibbs–Shannon entropy in the limit q → 1 q\to 1 . This generalization introduces a tunable parameter q q that controls the degree of non-extensivity, thereby allowing to model complex systems and distributions that cannot be adequately captured by the classical Boltzmann–Gibbs-Shannon framework [ Tsallis(1988) , Umarov and Tsallis(2022) ] .



 3.2 Entropy-Based Contraction Bound


 The study of Lipschitz continuity in Transformer architectures has gained significant attention, with recent literature establishing foundational bounds for the Softmax-normalized attention mechanism [ Kim et al.(2021) , Gao and Pavel(2017) , Yudin et al.(2024) ] . In this work, unlike traditional approaches that rely on worst-case spectral analysis which often impose rigid, data-agnostic constraints, our formulation identifies a contractive regime that is intrinsically sensitive to the internal informational structure of the sequence. By viewing the stability of the latent path through the topic of statistical mechanics, we replace rigid constants with something more organic. Our entropy-based contractive bound functions like a piston in a gas chamber: it is flexible enough to let the attention matrix expand and adapt to new information, yet it provides a gentle, restorative pressure that prevents the system from spiraling out of control. This allows our looped Transformer to breathe and refine its logic iteratively, achieving a stable state of flow without the performance loss that usually comes from forcing a model into a stiff mathematical trap.


 Theorem 3.2.1


 Let X ∈ ℝ n × d X\in\mathbb{R}^{n\times d} be a fixed input sequence and let Z Z be the latent variable, we first consider X + Z X+Z is the residual. Define the self-attention map of a vanilla trasformer with one head




 ℱ ⁡ ( X + Z ) := S ​ ( X + Z ) ⊤ ​ ( X + Z ) ​ W V , \mathcal{F}(X+Z)\;:=\;S(X+Z)^{\top}(X+Z)W_{V},


 where S ⁡ ( X + Z ) S(X+Z) is the row-wise softmax of the attention logits A ⁡ ( X + Z ) = ( X + Z ) ​ W Q ​ ( ( X + Z ) ​ W K ) ⊤ A(X+Z)=(X+Z)W_{Q}\bigl((X+Z)W_{K}\bigr)^{\top} and W Q , W K , W V W_{Q},W_{K},W_{V} are fixed weight matrices. Assume that ‖ X ‖ F ≤ 1 , ‖ Z ‖ F ≤ 1 , ‖ W V ‖ F ≤ 1 2 \|X\|_{F}\leq 1,\;\|Z\|_{F}\leq 1,\;\|W_{V}\|_{F}\leq\tfrac{1}{2} , and denote ∥ ⋅ ∥ o ​ p \|\cdot\|_{op} as the operator norm induced by the Frobenius norm on the space of matrices ℝ n × d \mathbb{R}^{n\times d} . Then the Fréchet derivative of F F with respect to Z Z satisfies




 ‖ D Z ​ ℱ ​ ( X + Z ) ‖ o ​ p ≤ ( 2 ​ ‖ W Q ‖ o ​ p ​ ‖ W K ‖ o ​ p + ∑ i = 1 n [ 1 − ( q − 1 ) ​ S q ​ ( r i ) ] 2 / q ) ​ ‖ W V ‖ F , \bigl\|D_{Z}\mathcal{F}(X+Z)\bigr\|_{op}\leq\left(2\|W_{Q}\|_{op}\|W_{K}\|_{op}+\sqrt{\sum_{i=1}^{n}\bigl[1-(q-1)S_{q}(r_{i})\bigr]^{2/q}}\right)\|W_{V}\|_{F},


 where S q ​ ( r i ) S_{q}(r_{i}) denotes the Tsallis entropy of the i i -th row of the attention map. For k k -iteration single-head looped transformer, if it satisfies the contractive condition




 ( ( 2 ∥ W Q ∥ o ​ p ∥ W K ∥ o ​ p + ∑ i = 1 n [ 1 − ( q − 1 ) S q ( r i ) ) 2 / q ] ) ∥ W V ∥ F ) k < 1 . \left(\left(2\|W_{Q}\|_{op}\|W_{K}\|_{op}+\;\sqrt{\sum_{i=1}^{n}\bigl[1-(q-1)S_{q}(r_{i})\bigr)^{2/q}}\bigr]\right)\|W_{V}\|_{F}\right)^{k}<1.


 then the residual iteration




 Z k + 1 = ℱ ⁡ ( X + Z k ) Z_{k+1}=\mathcal{F}(X+Z_{k})


 converges to a unique fixed point. (See proof in Appendix B.3 )


 The above theorem establishes that the stability of looped self-attention is governed by an explicit contraction bound that decomposes into a static weight-dependent term and a dynamic entropy-controlled attention term. In particular, sharp (low-entropy) attention distributions, where weight is concentrated on a few tokens, increase the sensitivity of the attention matrix to input perturbations, therefore amplifying the Jacobian norm and potentially inducing divergence. Conversely, higher attention entropy (by temperature scaling or our proposed entropy regularization) acts as a restorative pressure. By smoothing the attention distribution, it effectively suppresses the operator norm of the mapping, ensuring that the self-attention dynamics remain within a contractive condition. This establishes a formal mathematical correspondence between the Tsallis entropy, the softmax temperature and the existence of a unique implicit self-attention equilibrium.


 The entropy-based contraction bound explains the necessity of the softmax temperature τ \tau in looped architectures. It acts as the control valve for the system’s restorative pressure. While a low temperature ( τ \tau ) allows the model to sharpen its focus, it risks an entropy collapse, where the attention becomes so rigid and brittle that it breaks the contraction bound and drives the system into an unstable, expansive trap. By balancing τ \tau , we ensure the attention matrix maintains enough entropy to satisfy the contraction condition, allowing the latent variable to settle into a stable logical equilibrium rather than spiraling into numerical chaos.


 While the entropy bound guarantees a stable fixed point, the high-dimensional landscape of the latent space remains difficult to traverse. To bridge this gap, the model requires a navigation system to guide the latent state Z Z into the contractive horizon of the global minimum.





 4 Hamiltonian Latent Dynamical System.


 To provide the single-head looped Transformer with an inductive bias for structured navigation, we reformulate the latent state evolution as a discrete Hamiltonian dynamical system. We treat the latent state Z ∈ ℝ d Z\in\mathbb{R}^{d} as a particle’s position on a manifold, where the attention mechanism defines a potential energy landscape ℳ ⁡ ( Z , X , W ) \mathcal{M}(Z;X,W) conditioned on the input sequence X X and weights W W . In this formulation, the attention weights act as gradients of a potential field that govern the trajectory of the latent state. This approach transforms the transformer’s forward pass into a symplectic integration of the particle’s motion, ensuring energy conservation and stability during long-sequence inference.


 4.1 Latent Learning Process and Thermodynamics


 This formulation allows us to characterize the learning trajectory through the view of thermodynamic phase transitions between a particle’s physical states:


 The Exploration Phase (Gaseous): Characterized by high kinetic energy, the latent state explores the energy manifold with high mobility. In this stage, the potential landscape is relatively unstructured, allowing the particle to traverse energy barriers and avoid premature convergence to sub-optimal plateaus or saddle points.


 The Transitionary Phase (Liquid): As the kinetic energy diminishes, the system begins to settle into the emerging potential wells on the manifold induced by the task objective. The latent states begin to coalesce around candidate attractors, transitioning from global exploration to local manifold refinement.


 The Stability Phase (Solid): In the final stage, kinetic energy is minimized. The latent state crystallizes into a stable fixed-point Z ∗ Z^{*} within a deep potential well (the global minimum) with the assistance of the lowering entropy. In this physical state, the system achieves logical equilibrium, where the residual update vanishes and the symbolic solution is recovered.


 At the beginning of the training process, our objective is to maximize the system’s kinetic energy and entropy. High kinetic energy provides the necessary momentum for the latent particle to escape shallow local minima, while high entropic regularization ensures a broad attention distribution, facilitating the discovery of global dependencies across the input sequence X X . As training progresses, the potential energy defined by the alignment of query-key pairs increasingly dictates the latent trajectory, nevigating the state toward the global task solution.



 4.2 Task Setup: The Last Token Induction Head Task


 Given an input sequence of token embeddings X = ( x 1 , … , x n ) ∈ ℝ n × d X=(x_{1},\dots,x_{n})\in\mathbb{R}^{n\times d} , we consider the induction head mechanism as a predictive mapping: if x n = x i x_{n}=x_{i} , the model must retrieve x i + 1 x_{i+1} via a latent state evolution. We define the augmented state ( Z k , V k ) ∈ ℝ 2 ​ d (Z_{k},V_{k})\in\mathbb{R}^{2d} at iteration k k , representing the position and velocity of the latent representation. Under this formulation, the Transformer’s self-attention mechanism is reinterpreted as a discrete-time dynamical operator T : ℝ 2 ​ d → ℝ 2 ​ d T:\mathbb{R}^{2d}\to\mathbb{R}^{2d} that governs the trajectory of Z k Z_{k} across an energy manifold parameterized by the input X X .



 4.3 Attention as an Energy-Based Operator


 Let W Q , W K , W V ∈ ℝ d × d W_{Q},W_{K},W_{V}\in\mathbb{R}^{d\times d} be the query, key, and value linear projections. The state evolves according to the following discrete-time dynamical system




 V k + 1 = μ ​ V k + α ⁡ ( ℱ τ ​ ( Z k , X ) − Z k ) − β k ​ ∇ Z E τ ​ ( Z k , X ) V_{k+1}=\mu V_{k}+\alpha\bigl(\mathcal{F}_{\tau}(Z_{k};X)-Z_{k}\bigr)-\beta_{k}\nabla_{Z}E_{\tau}(Z_{k};X)

 (1)





 Z k + 1 = Z k + V k + 1 Z_{k+1}=Z_{k}+V_{k+1}


 where μ \mu is a momentum parameter, α \alpha is the field coupling coefficient, and β k \beta_{k} controls the gravitational pull of the potential wells. Given a temperature parameter τ > 0 \tau>0 , we define the soft-retrieval operator ℱ τ \mathcal{F}_{\tau} as




 ℱ τ ​ ( Z , X ) := ∑ i = 1 n σ τ ​ ( ⟨ W Q ​ Z , W K ​ x i ⟩ τ ​ d ) ​ W V ​ x i \mathcal{F}_{\tau}(Z;X):=\sum_{i=1}^{n}\sigma_{\tau}\left(\frac{\langle W_{Q}Z,W_{K}x_{i}\rangle}{\tau\sqrt{d}}\right)W_{V}x_{i}


 This operator generates a non-linear vector field in the latent space, accelerating Z Z toward the most relevant token representations. We define the Attention Energy E τ E_{\tau} as the negative log-partition function (Free Energy) of the attention scores as




 E τ ( Z ; X ) := − τ log ∑ i = 1 n exp ( ⟨ W Q ​ Z , W K ​ x i ⟩ τ ​ d ) E_{\tau}(Z;X):=-\tau\log\sum_{i=1}^{n}\exp\left(\frac{\langle W_{Q}Z,W_{K}x_{i}\rangle}{\tau\sqrt{d}}\right)




 The update rule in Eq. 1 defines a generalized dynamical system. When α = 0 \alpha=0 , the system recovers a pure Hamiltonian flow on the energy landscape E τ E_{\tau} . For α > 0 \alpha>0 , the term ( ℱ τ − Z k ) (\mathcal{F}_{\tau}-Z_{k}) acts as an steering force that drives the latent state across the manifold. Correspondingly, ∇ Z E τ \nabla_{Z}E_{\tau} exerts a restorative force, directing Z k Z_{k} toward the dominant wells of the landscape. As the temperature τ → 0 \tau\to 0 , E τ E_{\tau} develops sharp potential wells at the key locations W K ​ x i W_{K}x_{i} , trapping the latent particle to facilitate retrieval. The stability of this trajectory is governed by the interplay between the kinetic energy and the potential field. Specifically, when Z k Z_{k} enters a basin of attraction satisfying the contraction bound, the evolution becomes a contraction mapping, ensuring convergence to a stable fixed point.



 4.4 From Latent Dynamics to Landscape Engineering


 Empirical observations indicate that while the latent navigation system provides trajectory control, it is frequently insufficient to overcome the high-curvature potential barriers between basins. The latent state becomes trapped in incorrect local minima which do not correspond to the target induction task. This suggests that latent navigation at inference is fundamentally bounded by the embedding manifold’s geometry established during training . Consequently, we propose to project these physical constraints onto the functional objective itself. By incorporating velocity and potential terms into the loss function, we induce a basin of attraction in the parameter space that is globally directed toward the target solution, effectively regularizing the model toward a more tractable optimization landscape.




 5 Energy-Entropy Regularized Loss Landscape


 Traditional Looped Transformer training often suffers from a needle-in-a-haystack optimization problem, where the global minimum for reasoning tasks is located within an extremely narrow, high-curvature region of the parameter space. To mitigate this, we propose a novel Hamiltonian-Tsallis inspired loss function that reformulates the optimization objective by incorporating physical invariants directly into the landscape. Instead of modifying the Transformer architecture, we augment the loss landscape with three coupled penalties: Kinetic, Potential and Entropy Regularizations .


 By coupling these physical constraints, we transform a highly fluctuating and non-convex landscape into a pseudo-convex, funnel-shaped landscape. This regularization effectively dilates the energy manifold, allowing the optimizer to find the global minimum with significantly lower stochastic noise and a more stable convergence trajectory.


 5.1 Task Setup: The Induction Head Task on Full Sequence


 In this section, we formulate the iterative dynamics and the energy-entropy loss function used to train the single-head looped Transformer. Let X ∈ ℝ n × d X\in\mathbb{R}^{n\times d} denote the input sequence manifold of length n n with embedding dimension d d . Each token x i x_{i} is defined as the sum of the raw embedding and a positional encoding, x i = x i , raw + p i x_{i}=x_{i,\text{raw}}+p_{i} .We define a latent variable Z t ∈ ℝ n × d Z_{t}\in\mathbb{R}^{n\times d} with the initial condition Z 0 = 0 Z_{0}=0 . The evolution of the latent state at iteration t + 1 t+1 is governed by a residual discrete-time update




 Z t + 1 = Z t + ℱ ⁡ ( Z t + X ) Z_{t+1}=Z_{t}+\mathcal{F}(Z_{t}+X)


 where ℱ \mathcal{F} represents the attention-driven transition operator. This operator treats the sum of the current latent state and the fixed manifold as the query, key, and value sources. Given the weight matrices W Q , W K , W V ∈ ℝ d × d W_{Q},W_{K},W_{V}\in\mathbb{R}^{d\times d} , the transformation is defined as




 ℱ ⁡ ( Z t + X ) = σ ⁡ ( ( Z t + X ) ​ W Q ​ ( ( Z t + X ) ​ W K ) ⊤ d ) ​ ( Z t + X ) ​ W V \mathcal{F}(Z_{t}+X)=\sigma\left(\frac{(Z_{t}+X)W_{Q}((Z_{t}+X)W_{K})^{\top}}{\sqrt{d}}\right)(Z_{t}+X)W_{V}


 where σ ⁡ ( ⋅ ) \sigma(\cdot) denotes the row-wise softmax operator.



 5.2 The Physics-Informed Objective Function


 To ensure the convergence of this iterative process toward a stable induction rule, we formulate a novel loss function constrained by thermodynamic principles. This objective penalizes the learning process through three physics-informed regularization terms, guiding the model through a phase transition: from an initial high-entropy "liquid" discovery phase to a "crystalline" stable phase where the latent state reaches a fixed-point equilibrium. The total objective function is defined as




 ℒ Total = ℒ Task + λ P ​ ℒ Potential + λ K ​ ℒ Kinetic + λ S ​ ℒ Entropy \mathcal{L}_{\text{Total}}=\mathcal{L}_{\text{Task}}+\lambda_{P}\mathcal{L}_{\text{Potential}}+\lambda_{K}\mathcal{L}_{\text{Kinetic}}+\lambda_{S}\mathcal{L}_{\text{Entropy}}

 (2)

 where ℒ Task \mathcal{L}_{\text{Task}} is the standard cross-entropy loss for the induction task, ℒ Kinetic \mathcal{L}_{\text{Kinetic}} penalizes the velocity of the updates encouraging the model to reach a steady state where updates become infinitesimal, ℒ Potential \mathcal{L}_{\text{Potential}} minimizes the attention energy (negative log-partition function), forcing the model to develop deep basins of attraction around relevant tokens and ℒ Entropy \mathcal{L}_{\text{Entropy}} controls the Tsallis entropy of the attention distribution, regulating the transition between broad global search and narrow local focus. λ P , λ K \lambda_{P},\lambda_{K} and λ S \lambda_{S} are the corresponding control coefficients of ℒ Potential , ℒ Kinetic \mathcal{L}_{\text{Potential}},\mathcal{L}_{\text{Kinetic}} and ℒ Entropy \mathcal{L}_{\text{Entropy}} respectively.


 Unlike the highly fluctuating, non-convex landscape of standard cross-entropy which is often characterized by narrow, inaccessible minima, this novel energy-entropy regularized loss function smooths the manifold and broadens the basins of attraction. By expanding the reachable state space, it allows easier access to the global minimum (See Figure 1 ).


 Figure 1: Visualization of the loss manifold showing a funnel-like geometry caused by the energy-entropy regularization in the loss function. Left: Funnel-like landscape from the energy-entropy regularized loss function. Right: Highly flutuating loss landscape from regular cross entropy loss function.



 5.3 Kinetic Regularization


 To enforce asymptotic stability within the iterative loop, we introduce a kinetic penalty. Unlike standard L 2 L_{2} weight regularization, we penalize the squared Euclidean norm of the state residuals. This term acts as a dissipative force (damping) that encourages the system to reach an equilibrium:




 ℒ Kinetic = 1 2 ​ T ​ ∑ t = 1 T ‖ Z t − Z t − 1 ‖ 2 2 \mathcal{L}_{\text{Kinetic}}=\frac{1}{2T}\sum_{t=1}^{T}||Z_{t}-Z_{t-1}||^{2}_{2}

 (3)

 By varying the rollout depth T ∈ [ 16 , 64 ] T\in[16,64] , we encourage the discovery of length-invariant attractors rather than transient paths. This process undergoes a structural phase transition: early liquid exploration of the manifold is gradually replaced by crystallization as the penalty induces stability in the latent trajectory.



 5.4 Potential Regularization


 The potential term represents the local potential from the energy landscape of the attention mechanism, defined as




 ℒ Potential = 1 T ​ ∑ t = 1 T min j ⁡ ( − log ⁡ p t ​ j ) \mathcal{L}_{\text{Potential}}=\frac{1}{T}\sum_{t=1}^{T}\min_{j}\left(-\log p_{tj}\right)

 (4)

 where p t ​ j = Softmax ​ ( scores ) t ​ j = exp ⁡ ( q t ⊤ ​ k j τ ​ d ) / ∑ l = 1 N exp ⁡ ( q t ⊤ ​ k l τ ​ d ) p_{tj}=\text{Softmax}(\text{scores})_{tj}=\exp(\frac{q_{t}^{\top}k_{j}}{\tau\sqrt{d}})/\sum_{l=1}^{N}\exp(\frac{q_{t}^{\top}k_{l}}{\tau\sqrt{d}}) . It represents the binding energy of the latent state relative to the input tokens. By minimizing the negative log-probability of the maximally attended key, we effectively deepen the potential well of the most relevant token. Physically, this increases the escape energy required for the latent particle to drift away from the causal trigger, constraining the latent trajectory to the manifold region associated with the ground-truth target.



 5.5 Entropy Regularization


 While temperature scaling ( τ \tau ) is a common heuristic for attention convergence, Theorem 3.2 formalizes its role: system stability is governed by the spectral radius of the Jacobian, which is bounded by the attention entropy. However, a static τ \tau is overly restrictive for multi-step reasoning. We propose that the latent trajectory requires dynamic entropic regulation, a mechanism that allows the attention distribution to expand for broad contextual comparison and contract for precise symbolic retrieval. To control this dynamic manifold and avoid the over-smoothing typical of recurrent architectures, we introduce a Tsallis-type entropy penalty




 ℒ Entropy = | 1 T ​ ∑ t = 1 T S q ​ ( p t ) − η | \mathcal{L}_{\text{Entropy}}=\left|\;\frac{1}{T}\sum_{t=1}^{T}S_{q}(p_{t})-\eta\;\right|

 (5)

 where S q ​ ( p t ) = 1 q − 1 ​ ( 1 − ∑ j = 1 N p t ​ j q ) S_{q}(p_{t})=\frac{1}{q-1}\left(1-\sum_{j=1}^{N}p_{tj}^{q}\right) is the Tsallis entropy and η ∈ ℝ \eta\in\mathbb{R} is a target entropic floor. The index q ∈ ( 1 , 2 ] q\in(1,2] associates with the penalty’s sensitivity to the distribution’s tail. By penalizing deviations from η \eta , we prevent entropic collapse and ensure the attention weights periodically crystallize into sparse, quasi-discrete distributions. This maintains the high signal-to-noise ratio necessary to sustain logical focus across long-range recursions.



 5.6 The Reasoning Phase Transition


 We observed that optimization in looped Transformers does not follow a linear path of knowledge accumulation, but rather follows a discrete phase transition. The model’s sudden gain in proficiency—the "snap" into focus—suggests that functional accuracy is an emergent property of the underlying thermodynamic state. Consequently, improving model performance is not merely an exercise in minimizing loss, but in managing latent energy and entropy . By dissipating kinetic energy and deepening the potential wells associated with the objective, we restructure the latent manifold such that the ground-truth solution emerges as a stable, physical inevitability.




 6 Experiment


 To evaluate the robustness of our single-head looped Transformer, we conducted a series of experiments focusing on the Induction Head task.


 A critical observation in our experiments was the non-monotonic nature of the model’s accuracy during the early stages of the thinking process. For L = 1000 L=1000 , the model’s accuracy initially plateaus or decays before it reaches 90 % 90\% , suggesting that the hidden state z z has not yet settled into the correct minimum well. However, as the number of iterations for training and testing increases, we observe a phase transition where accuracy recovers and climbs steadily. By penalizing high kinetic energy and maintaining a controlled potential well, the model is prevented from drifting into chaotic states during it trajectory. (See Table 2 )


 6.1 Experimental Setup


 To evaluate the efficacy of the Energy-Entropy Regularized (EER) Transformer, we compare our model against the FOP-Looped-Adaptive model ( [ Fan et al.(2024) ] ), which utilizes RASP-L for algorithmic reasoning. To test the limits of parameter efficiency, we initialize a minimalist single-head looped Transformer with a latent dimension of only d = 8 d=8 . Unlike the multi-component Encoder-Decoder architectures prevalent in the literature, our model utilizes a unified single-block stream with no separate encoder or decoder modules.


 Architecture Details. Our model follows a standard recurrent architecture consisting of a single attention head followed by a Multi-Layer Perceptron (MLP) and Layer Normalization. To enfore long-range coordination in this low-dimensional space, we employ sinusoidal position embeddings scaled by a factor of 0.15 0.15 . This scaling ensures that the geometric bias of the embedding does not overwhelm the learned latent dynamics.


 The Entropy-Energy Regularized Objective. We distinguish our loss function from standard cross-entropy training by introducing a Hamiltonian-Tsallis inspired objective function. The total loss ℒ Total \mathcal{L}_{\text{Total}} is defined as Eq. 2 . Following empirical tuning, we set λ P = 0.1 \lambda_{P}=0.1 , λ K = 0.001 \lambda_{K}=0.001 , λ S = 0.02 \lambda_{S}=0.02 , q = 1.5 q=1.5 and η = 0 \eta=0 . We hypothesize that these coefficients define a smooth manifold path, though the existence of multiple trajectories toward the global minimum suggests that this configuration is sufficient rather than uniquely optimal.


 Training and Inference Configuration. Following the curriculum strategies proposed by Fan et al. (2025), we train our d = 8 d=8 model on sequence lengths L ∈ [ 16 , 64 ] L\in[16,64] with T t ​ r ​ a ​ i ​ n , T e ​ v ​ a ​ l = 25 T_{train},T_{eval}=25 recurrence steps. To assess Out-of-Distribution (OOD) length generalization, we evaluate the model on sequences up to L = 1000 L=1000 .





 Metric
 FOP-Looped-Adaptive
 EER (Ours)

 Base Architecture
 Looped GPT-2
 Single-Head Looped Transformer

 Latent Dimension ( d d )
 64
 8

 Attention Heads ( h h )
 4
 1

 Position Encoding
 0.15 × 0.15\times Sinusoidal
 0.15 × 0.15\times Sinusoidal

 Recurrence Depth ( T T )
 25
 25

 Training Steps
 100k
 20k

 Learning Rate
 1 × 10 − 4 1\times 10^{-4}
 1 × 10 − 3 1\times 10^{-3}

 Weight Decay
 0.05
 0.10

 Batch Size
 64
 32

 Training Range ( L L )
 16–64
 16–64

 Loss Objective
 Cross-Entropy (CE)
 ℒ Task + ℒ Kinetic + ℒ Potential + ℒ Entropy \mathcal{L}_{\text{Task}}+\mathcal{L}_{\text{Kinetic}}+\mathcal{L}_{\text{Potential}}+\mathcal{L}_{\text{Entropy}}


 Table 1: Model Configurations: FOP-Looped-Adaptive vs. EER (Ours).




 7 Results and Discussion


 7.1 Length Generalization and Phase Transitions


 The EER framework achieves successful length generalization up to L = 1000 L=1000 , significantly outperforming the baseline despite having less than 0.02 % 0.02\% of its parameter count (See Figure 2 ).


 As shown in Table 2 , the model undergoes a distinct phase transition around epoch 500, where the accuracy of length 1000 (Acc L1000) jumps from 33.5 % 33.5\% to 79.2 % 79.2\% . The early stages of optimization are characterized by high kinetic energy ( K ≈ 93.7 K\approx 93.7 ) and elevated entropy ( S ≈ 1.25 S\approx 1.25 ), representing a gaseous phase of exploration where accuracy across all sequence lengths (L10–L1000) remains low. However, as the regularizer dissipates kinetic energy, dropping significantly to K ≈ 36.6 K\approx 36.6 by epoch 9500, we observe a corresponding cooling of the energy manifold. This transition triggers a sharp increase in performance, particularly at L = 100 L=100 , where accuracy plateaus at a robust 96.7%. Crucially, the "Snap" into focus is visible in the later epochs (6000–9500), where the potential wells deepen and kinetic fluctuations diminish. This stability is not merely a local artifact but generalizes across recursive iterations, as evidenced by the high sustained accuracy in L = 1000 L=1000 . Unlike standard baselines that often suffer from gradient explosion in deep recursions, our thermodynamic approach ensures that as the system reaches logical equilibrium, the correct output becomes a stable attractor. This empirical trajectory validates our hypothesis: by managing the loss landscape, we establish a robust phase transition from disordered guessing to crystalline algorithmic execution .


 Figure 2: Baseline Comparison of EER (d=8) and FOP-Looped-Adaptive (d=64)


 We observe the notable phenomenon that accuracy is a "symptom", while energy and entropy are the "causes". In a d = 8 d=8 manifold, there are million ways for the model to fail, but only a few configurations are energetically quiet and logically consistent. By stabilizing the kinetic energy and entropy, we effectively remove the chaotic noise that prevents induction logic from emerging.




 8 Computational Resources


 All experiments were conducted using a combination of NVIDIA A100 and T4 GPUs. The A100 was utilized for primary training to leverage TF32 precision, while T4 GPUs were used for cross-architecture validation of the training stability.


 Thermal Noise and Hardware Robustness. Given the constrained capacity of the d = 8 d=8 single-head looped Transformer, the optimization trajectory is highly susceptible to subtle environmental perturbations. We observe that experiments conducted on NVIDIA A100 GPUs (utilizing TF32 precision) exhibit accelerated escape from local minima compared to CPU-based runs (FP32). This hardware-level stochasticity introduces sufficient kinetic energy to displace the latent state from metastable local minima such as the transient plateau observed at Epoch 8000, triggering a transition into the global potential well. Consequently, this numerical noise serves as a critical regularizer, preventing premature convergence in low-dimensional, high-curvature landscapes.



 9 Conclusion


 In this work, we have demonstrated that the reasoning capacity of looped transformers is not solely a function of scale, but a consequence of the underlying geometric dynamics governed by the loss landscape. By introducing a novel Energy-Entropy Regularization framework, we successfully trained a minimal, single-head looped transformer with an embedding dimension of only d = 8 d=8 to solve long-range induction tasks of up to 1000 1000 tokens, a task typically reserved for significantly larger architectures. By treating the latent space as a dynamical system, our investigation peels back the "black box" of looped architectures, revealing the elegant physical principles that govern their internal reasoning


 While our empirical findings are centered on the induction head task, they point toward a profound conclusion: the fundamental reasoning mechanisms of Transformers are remarkably efficient. The realization that high-dimensional logical operations can be compressed into a d = 8 d=8 bottleneck suggests that the trajectory toward interpretable AI lies not in increasing parameter counts, but in the careful balancing of the underlying loss geometry.



 Declaration of Generative AI Technology Use


 The author utilized Gemini 3 as a linguistic aid to refine the flow and clarity of this manuscript. Following this process, all AI-generated suggestions were carefully reviewed and edited.




