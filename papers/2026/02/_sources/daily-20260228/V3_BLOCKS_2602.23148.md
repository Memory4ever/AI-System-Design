[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: On Sample-Efficient Generalized Planning via Learned Transition Models

[3] h6: Abstract

[4] p: Generalized planning studies the construction of solution strategies that generalize across families of planning problems sharing a common domain model, formally defined by a transition function γ : S × A → S \gamma:S\times A\rightarrow S . Classical approaches achieve such generalization through symbolic abstractions and explicit reasoning over γ \gamma . In contrast, recent Transformer-based planners, such as PlanGPT and Plansformer, largely cast generalized planning as direct action-sequence prediction, bypassing explicit transition modeling. While effective on in-distribution instances, these approaches typically require large datasets and model sizes, and often suffer from state drift in long-horizon settings due to the absence of explicit world-state evolution. In this work, we formulate generalized planning as a transition-model learning problem, in which a neural model explicitly approximates the successor-state function γ ^ ≈ γ \hat{\gamma}\approx\gamma and generates plans by rolling out symbolic state trajectories. Instead of predicting actions directly, the model autoregressively predicts intermediate world states, thereby learning the domain dynamics as an implicit world model. To study size-invariant generalization and sample efficiency, we systematically evaluate multiple state representations and neural architectures, including relational graph encodings. Our results show that learning explicit transition models yields higher out-of-distribution satisficing-plan success than direct action-sequence prediction in multiple domains, while achieving these gains with significantly fewer training instances and smaller models. This is an extended version of a short paper accepted at ICAPS 2026 under the same title.

[5] p: University of South Carolina

[6] p: {niting@email., vishalp@email., jaaydin@email., biplav}@sc.edu

[7] p: Code — https://github.com/ai4society/state-centric-gen-planning

[8] h2: Introduction

[9] figure: Figure 1: State-Centric Generalized Planning Pipeline. From a symbolic planning instance Π \Pi , executable plans are generated using a learned transition model. (1) State Encoding: Symbolic state–goal pairs ( s t , g ) (s_{t},g) are mapped to fixed-dimensional embeddings ϕ ⁡ ( s t ) \phi(s_{t}) using either WL graph kernels or fixed-size factored vectors. (2) Transition Modeling: A parametric model (LSTM) or a non-parametric model (XGBoost) learns residual state transitions Δ t \Delta_{t} to predict successor embeddings. (3) Neuro-Symbolic Plan Decoding: The predicted successor embedding ϕ ^ ​ ( s t + 1 ) \hat{\phi}(s_{t+1}) is matched against all valid symbolic successors Succ ⁡ ( s t ) \mathrm{Succ}(s_{t}) induced by γ \gamma , and the nearest valid successor is selected to recover the executable action. This guarantees symbolic validity while enabling transition-model-based generalization.

[10] p: Classical automated planning is defined over a state-transition system Σ = ⟨ S , A , γ ⟩ \Sigma=\langle S,A,\gamma\rangle , where S S is the set of states, A A the set of actions, and γ : S × A → S \gamma:S\times A\rightarrow S the transition function. A planning task Π = ⟨ Σ , s 0 , g ⟩ \Pi=\langle\Sigma,s_{0},g\rangle consists of an initial state s 0 ∈ S s_{0}\in S and a goal condition g g , typically represented as a set of literals such that a state s s satisfies g g iff g ⊆ s g\subseteq s . A solution is an action sequence π = ⟨ a 1 , … , a n ⟩ \pi=\langle a_{1},\ldots,a_{n}\rangle such that s t + 1 = γ ⁡ ( s t , a t ) s_{t+1}=\gamma(s_{t},a_{t}) and the final state s n s_{n} satisfies g g . Generalized planning seeks strategies that solve families of such tasks sharing a common γ \gamma .

[11] p: Recent learning-based approaches to generalized planning predominantly model the conditional distribution p ⁡ ( π ∣ Π ) p({\pi\mid\Pi}) , for example via an autoregressive factorization p ⁡ ( π ∣ Π ) = ∏ t = 1 T p ⁡ ( a t ∣ Π , a < t ) p(\pi\mid\Pi)=\prod_{t=1}^{T}p(a_{t}\mid\Pi,a_{<t}) or a policy π θ ​ ( a t ∣ s t , g ) \pi_{\theta}(a_{t}\mid s_{t},g) , and directly predict action sequences from problem descriptions, as in Plansformer ( Pallagani et al. 2022 ) , PlanGPT ( Rossetti et al. 2024b ) , and symmetry-aware Transformers ( Fritzsche et al. 2025 ) . This action-centric formulation bypasses explicit modeling of γ \gamma : the evolving world state s t s_{t} is never directly represented, and long-horizon reasoning relies on implicit correlations between action tokens, leading to state drift in out-of-distribution regimes.

[12] p: In this work, we instead model generalized planning as a transition-model learning problem. Rather than predicting the next action, we learn a goal-conditioned neural transition model 𝒯 θ \mathcal{T}_{\theta} that predicts the successor state along a plan trajectory, i.e., given the current state s t s_{t} and goal g g (or problem description Π \Pi ), the model outputs a prediction s ^ t + 1 = 𝒯 θ ​ ( s t , g ) \hat{s}_{t+1}=\mathcal{T}_{\theta}(s_{t},g) . Plans are then obtained by rolling out the predicted state trajectory and recovering the corresponding actions via local symbolic search over applicable operators, by matching γ ⁡ ( s t , a ) \gamma(s_{t},a) to s ^ t + 1 \hat{s}_{t+1} . This formulation enforces explicit world-state evolution, enables successor validation, and constrains learning to respect frame axioms and causal effects. It is consistent with model-based world modeling in reinforcement learning ( Ha and Schmidhuber 2018 ; Hafner et al. 2019 ) , but applied here to symbolic generalized planning.

[13] p: For clarity, we refer to methods that directly predict actions (e.g., modeling p ⁡ ( π ∣ Π ) p(\pi\mid\Pi) or π θ ​ ( a t ∣ s t , g ) \pi_{\theta}(a_{t}\mid s_{t},g) ) as action-centric learning, and to methods that predict successor states via 𝒯 θ ​ ( s t , g ) \mathcal{T}_{\theta}(s_{t},g) as state-centric learning. This usage is distinct from heuristic-based state-space learning in existing GP taxonomies ( Chen et al. 2025 ) and serves only to distinguish transition-model learning from direct action modeling.

[14] p: A central challenge in learning 𝒯 θ \mathcal{T}_{\theta} for GP is size invariance: the description of a state in S S scales with the number of objects. To address this, we systematically evaluate multiple fixed-dimensional state representations, including fixed-size factored encodings and Weisfeiler–Leman (WL) graph embeddings ( Chen et al. 2024 ) . WL embeddings map variable-sized relational states to fixed-length structural feature vectors, enabling compact models such as LSTMs ( Hochreiter and Schmidhuber 1997 ) and XGBoost ( Chen 2016 ) to generalize from small to large problem instances. We empirically show that relational WL features are critical for size-invariant and sample-efficient generalization. Our contributions, thus, are (i) a transition-model-based formulation of generalized planning via goal-conditioned successor-state prediction; (ii) a systematic evaluation of state representations for size-invariant and sample-efficient generalization; and (iii) an empirical demonstration that compact models achieve competitive GP performance with orders of magnitude fewer parameters and training instances than Transformer-based planners.

[15] h2: Related Work

[16] p: Learning-based approaches to generalized planning seek policies or models that transfer across problem instances within a domain. Early neural GP work introduced relational inductive biases to enable size generalization, including Action Schema Networks ( Toyer et al. 2018 ) and graph-based deep RL for Blocksworld ( Rivlin et al. 2020 ) , as well as finite-state policy representations ( Ståhlberg et al. 2022 ) . More recent work formulates GP as sequence prediction: Plansformer ( Pallagani et al. 2022 ) and PlanGPT ( Rossetti et al. 2024b ) train Transformer architectures to directly generate action sequences, while symmetry-aware Transformers ( Fritzsche et al. 2025 ) introduce architectural and contrastive constraints to improve permutation invariance. However, such action-centric models do not explicitly learn transition dynamics and often exhibit state drift under distributional shift. In parallel, graph-based state representations have been extensively studied for learning heuristics and value functions in planning, including STRIPS-HGN ( Shen et al. 2020 ) , GOOSE ( Chen et al. 2023 ) , and domain-independent graph transformations ( Chen and Thiébaux 2024 ) . Recent work shows that Weisfeiler–Leman (WL) graph kernels combined with lightweight regressors can match or exceed GNN performance at far lower cost ( Chen et al. 2024 ; Chen 2025 ; Hao et al. 2025 ) . Hybrid neuro-symbolic systems integrate learned components with symbolic solvers or validators, including LLM+P ( Liu et al. 2023 ) , symbolic validation for PlanGPT ( Rossetti et al. 2024a ) , LLM-Modulo ( Kambhampati et al. 2024 ) , and SayCan for robotics ( Ahn et al. 2022 ) . Separately, model-based reinforcement learning demonstrates the benefits of learning explicit world models for planning ( Ha and Schmidhuber 2018 ; Hafner et al. 2019 ) . In contrast to prior action-sequence and heuristic-centric neural planners, our work adopts a transition-prediction formulation of generalized planning with size-invariant state representations, enabling sample-efficient and robust out-of-distribution generalization using compact models. Extended discussion is in Appendix B .

[17] h2: Transition-Model-Based Generalized Planning

[18] p: Figure 1 illustrates the complete pipeline of our approach, consisting of symbolic data generation, size-invariant state encoding, transition-model learning, and plan decoding via symbolic verification.

[19] h4: Generalized Planning Setup.

[20] p: A planning instance is Π = ⟨ 𝒪 , 𝒫 , 𝒜 , s 0 , g ⟩ \Pi=\langle\mathcal{O},\mathcal{P},\mathcal{A},s_{0},g\rangle , where 𝒪 \mathcal{O} is a finite object set, 𝒫 \mathcal{P} a predicate vocabulary, 𝒜 \mathcal{A} a set of operators, s 0 ⊆ 𝒫 ⁡ ( 𝒪 ) s_{0}\subseteq\mathcal{P}(\mathcal{O}) the initial state, and g ⊆ 𝒫 ⁡ ( 𝒪 ) g\subseteq\mathcal{P}(\mathcal{O}) the goal condition. Operators induce a deterministic transition function γ : S × 𝒜 → S \gamma:S\times\mathcal{A}\rightarrow S . A plan π = ⟨ a 1 , … , a T ⟩ \pi=\langle a_{1},\ldots,a_{T}\rangle satisfies s t + 1 = γ ⁡ ( s t , a t ) s_{t+1}=\gamma(s_{t},a_{t}) and g ⊆ s T g\subseteq s_{T} . Generalized planning seeks a single parameterized model trained on instances from 𝒟 train \mathcal{D}_{\text{train}} (small | 𝒪 | |\mathcal{O}| ) that generalizes to 𝒟 test \mathcal{D}_{\text{test}} with much larger | 𝒪 | |\mathcal{O}| .

[21] h4: Size-Invariant State Representation.

[22] p: Each state-goal pair ( s , g ) (s,g) is encoded as a relational instance graph G s , g G_{s,g} and embedded using k k iterations of WL color refinement. Node color histograms yield a fixed-dimensional embedding ϕ ⁡ ( s , g ) ∈ ℝ D \phi(s,g)\in\mathbb{R}^{D} , where D D depends only on the domain and is independent of | 𝒪 | |\mathcal{O}| . We overload notation and write ϕ ⁡ ( s ) \phi(s) and ϕ ⁡ ( g ) \phi(g) for the state and goal components, respectively. The resulting representation is permutation-invariant, size-invariant, and as expressive as 1-WL message-passing GNNs while enabling lightweight downstream models.

[23] h4: State-Centric Transition-Model Learning.

[24] p: Rather than learning a policy π θ ​ ( a t ∣ s t , g ) \pi_{\theta}(a_{t}\mid s_{t},g) , we learn a neural transition model f θ : ℝ D × ℝ D → ℝ D f_{\theta}:\mathbb{R}^{D}\times\mathbb{R}^{D}\rightarrow\mathbb{R}^{D} that predicts state updates in embedding space. We denote this embedding-space transition model as f θ f_{\theta} ; the conceptual model 𝒯 θ \mathcal{T}_{\theta} from the introduction is realized as

[25] table: 𝒯 θ ​ ( s t , g ) ≈ ϕ − 1 ​ ( ϕ ⁡ ( s t ) + f θ ​ ( ϕ ⁡ ( s t ) , ϕ ⁡ ( g ) ) ) \mathcal{T}_{\theta}(s_{t},g)\approx\phi^{-1}(\phi(s_{t})+f_{\theta}(\phi(s_{t}),\phi(g)))

[26] p: where the inverse is approximated via nearest-neighbor decoding. To exploit the sparsity of STRIPS-style transitions, where most predicates remain unchanged, we adopt a residual formulation:

[27] table: ϕ ^ ​ ( s t + 1 ) = ϕ ⁡ ( s t ) + f θ ​ ( ϕ ⁡ ( s t ) , ϕ ⁡ ( g ) ) \hat{\phi}(s_{t+1})=\phi(s_{t})+f_{\theta}(\phi(s_{t}),\phi(g))

[28] p: where f θ f_{\theta} predicts a delta vector Δ t \Delta_{t} . This explicitly encodes frame axioms and improves sample efficiency, particularly for non-sequential models. We train by minimizing the squared error over expert trajectories:

[29] table: ℒ = ∑ t ‖ ϕ ^ ​ ( s t + 1 ) − ϕ ⁡ ( s t + 1 ) ‖ 2 2 . {\mathcal{L}=\sum_{t}\|\hat{\phi}(s_{t+1})-\phi(s_{t+1})\|_{2}^{2}}.

[30] h4: Plan Decoding via Neuro-Symbolic Verification.

[31] p: At test time, the true symbolic state s t s_{t} is maintained throughout execution. Given s t s_{t} , the transition model produces a target embedding 𝐯 t = ϕ ⁡ ( s t ) + f θ ​ ( ϕ ⁡ ( s t ) , ϕ ⁡ ( g ) ) \mathbf{v}_{t}=\phi(s_{t})+f_{\theta}(\phi(s_{t}),\phi(g)) . Using the symbolic operators, we enumerate all valid successors

[32] table: Succ ( s t ) = { γ ( s t , a ) ∣ a ∈ 𝒜 , a applicable in s t } \mathrm{Succ}(s_{t})=\{\gamma(s_{t},a)\mid a\in\mathcal{A},\;a\text{ applicable in }s_{t}\}

[33] p: and select the successor whose embedding is closest to the neural prediction:

[34] table: s t + 1 = arg ⁡ min s ′ ∈ Succ ⁡ ( s t ) ⁡ ‖ ϕ ⁡ ( s ′ ) − 𝐯 t ‖ 2 . s_{t+1}=\arg\min_{s^{\prime}\in\mathrm{Succ}(s_{t})}\|\phi(s^{\prime})-\mathbf{v}_{t}\|_{2}.

[35] p: The executed action is the unique a a satisfying γ ⁡ ( s t , a ) = s t + 1 \gamma(s_{t},a)=s_{t+1} , which is well-defined under deterministic operators. This decoding step guarantees symbolic validity at every timestep and performs online correction of neural prediction errors. The procedure terminates when g ⊆ s t g\subseteq s_{t} . The full planning algorithm is summarized in Algorithm 1 .

[36] figure: Algorithm 1 State-Centric GP with Plan Decoding 0: Initial state s 0 s_{0} , goal g g , operators 𝒜 \mathcal{A} , learned model f θ f_{\theta} , embedding ϕ \phi 0: Valid plan π \pi 1: t ← 0 t\leftarrow 0 , π ← ⟨ ⟩ \pi\leftarrow\langle\rangle , s t ← s 0 s_{t}\leftarrow s_{0} 2: while g ⊈ s t g\not\subseteq s_{t} do 3: 𝐯 t ← ϕ ⁡ ( s t ) + f θ ​ ( ϕ ⁡ ( s t ) , ϕ ⁡ ( g ) ) \mathbf{v}_{t}\leftarrow\phi(s_{t})+f_{\theta}(\phi(s_{t}),\phi(g)) 4: Succ ( s t ) ← { γ ( s t , a ) ∣ a ∈ 𝒜 , a applicable in s t } \mathrm{Succ}(s_{t})\leftarrow{\{\gamma(s_{t},a)\mid a\in\mathcal{A},\;a\text{ applicable in }s_{t}\}} 5: s t + 1 ← arg ⁡ min s ′ ∈ Succ ⁡ ( s t ) ⁡ ‖ ϕ ⁡ ( s ′ ) − 𝐯 t ‖ 2 s_{t+1}\leftarrow\arg\min_{s^{\prime}\in\mathrm{Succ}(s_{t})}\|\phi(s^{\prime})-\mathbf{v}_{t}\|_{2} 6: a t ← a_{t}\leftarrow unique a a such that γ ⁡ ( s t , a ) = s t + 1 \gamma(s_{t},a)=s_{t+1} 7: π . append ​ ( a t ) \pi.\text{append}(a_{t}) , s t ← s t + 1 s_{t}\leftarrow s_{t+1} , t ← t + 1 t\leftarrow t+1 8: end while 9: return π \pi

[37] h2: Experimental Setup

[38] p: We evaluate whether learning an explicit transition model enables sample-efficient and size-invariant generalized planning. Our experiments assess (i) extrapolative out-of-distribution (OOD) generalization from small to large instances, (ii) whether parametric function approximation is necessary for learning transition dynamics, and (iii) the impact of size-invariant state representations.

[39] h4: Domains and Data.

[40] p: We evaluate on 4 IPC benchmark domains: Blocksworld , Gripper , Logistics , and VisitAll . Problem instances are sourced from the Symmetry-Aware Transformer repository, following the same data splits for fair comparison. Symbolic plans are generated using Fast Downward ( Helmert 2006 ) with the landmark-cut heuristic, and complete state trajectories are reconstructed using VAL ( Howey et al. 2004 ) . Data is partitioned into four splits by object count: Training (small instances, e.g., 4–7 blocks), Validation (similar or slightly larger sizes, held out), Interpolation (unseen configurations within the training size range), and Extrapolation (strictly larger than any training instance, e.g., 9–17 blocks). Extrapolation is the primary evaluation axis for size-invariant generalized planning. Full dataset statistics are reported in Appendix section D .

[41] h4: State Representations.

[42] p: We compare WL graph embeddings ( Chen and Thiébaux 2024 ) , which are permutation- and size-invariant, against Fixed-Size Factored (FSF) encodings. FSF encodings represent states as fixed-dimensional vectors with pre-assigned object slots, deliberately omitting the relational structure of WL to isolate the contribution of invariant representations to OOD generalization ( Boutilier et al. 2000 ; Guestrin et al. 2003 ) . Details about both representations are in Appendix sections E and F .

[43] h4: Transition Models.

[44] p: We evaluate two transition-model classes: a parametric neural model (two-layer LSTM) and a tree-based, nonparametric regressor (XGBoost). The LSTM tests whether sequential memory is necessary for trajectory-level transition dynamics, while XGBoost tests whether a local approximation of the transition kernel suffices. This comparison isolates the role of temporal memory. Both models are trained in state-prediction and delta-prediction modes, as defined in previous sections. The entire technical pipeline and hyperparameters are reported in Appendix section G .

[45] h4: Baselines.

[46] p: We compare against published results from Symmetry-Aware Transformers (SATr), which include results on PlanGPT, including applicability-filtered and regrounded variants. We further run inference with Plansformer on our test instances using its publicly released checkpoint; it was trained on Blocksworld but not on Gripper, Logistics, or VisitAll, so its zero-shot cross-domain performance is expected to be limited. PlanGPT results are taken directly from Fritzsche et al. (2025) , who train and evaluate PlanGPT on the same data splits and counts as SATr; the weak interpolation/extrapolation performance reflects the difficulty of learning generalized policies from small training sets via action-centric sequence prediction. As a symbolic upper bound, we include Fast Downward with A* and the landmark-cut heuristic. While alternative configurations such as LAMA ( Richter and Westphal 2010 ) may improve coverage on extrapolation instances at varying runtimes, we retain A*+LM-cut as a fixed reference; the neural baselines serve primarily to compare learning paradigms rather than to benchmark against optimized classical planners.

[47] h4: Inference and Metrics.

[48] p: At test time, plans are generated using the neuro-symbolic decoding procedure in Algorithm 1 with beam width 3 and a horizon cap of 100. Performance is measured by satisficing success rate , i.e., the fraction of instances for which a generated plan is valid under the transition model and reaches a goal state within the horizon limit, as verified by VAL. We additionally report changes in satisficing success across successive rollouts (seeds) to quantify stability under repeated decoding.

[49] figure: Table 1: Coverage rates (%) across all configurations. Values are reported as M ​ e ​ a ​ n ± S ​ t ​ d Mean_{\pm Std} . Best result per row (over all non-FD configurations) is bolded , second best is underlined . Light gray columns denote our state-centric implementations. FD = Fast Downward (60s timeout). ∗ Results from Fritzsche et al. (2025) . FD Plansf. PlanGPT ∗ SATr (enc) ∗ SATr (enc-dec) ∗ WL-LSTM WL-XGB FSF-LSTM FSF-XGB Domain Split greedy appl. regr. greedy greedy appl. regr. state delta state delta state delta state delta Blocks Val. 1.00 1.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 1.00 ±0.00 1.00 ±0.00 1.00 ±0.00 0.00 ±0.00 0.56 ± 0.16 ¯ {}_{\scriptscriptstyle\pm\underline{0.16}} 0.67 ± 0.00 ¯ {}_{\scriptscriptstyle\pm\underline{0.00}} 1.00 ±0.00 0.67 ± 0.00 ¯ {}_{\scriptscriptstyle\pm\underline{0.00}} 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 Interp. 1.00 1.00 ±0.00 0.56 ±0.16 0.56 ±0.16 0.00 ±0.00 1.00 ±0.00 1.00 ±0.00 1.00 ±0.00 1.00 ±0.00 0.56 ±0.16 0.89 ± 0.16 ¯ {}_{\scriptscriptstyle\pm\underline{0.16}} 1.00 ±0.00 1.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 Extrap. 0.60 0.10 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.05 ±0.07 0.07 ±0.02 0.13 ±0.05 0.00 ±0.00 0.03 ±0.02 0.15 ±0.07 0.25 ± 0.00 ¯ {}_{\scriptscriptstyle\pm\underline{0.00}} 0.45 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 Gripper Val. 1.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 1.00 ±0.00 0.17 ±0.24 1.00 ±0.00 1.00 ±0.00 1.00 ±0.00 0.67 ± 0.47 ¯ {}_{\scriptscriptstyle\pm\underline{0.47}} 0.00 ±0.00 0.00 ±0.00 0.17 ±0.24 0.33 ±0.24 0.00 ±0.00 0.00 ±0.00 Interp. 1.00 0.00 ±0.00 0.00 ±0.00 0.44 ±0.16 0.00 ±0.00 0.89 ± 0.16 ¯ {}_{\scriptscriptstyle\pm\underline{0.16}} 0.67 ±0.00 1.00 ±0.00 1.00 ±0.00 1.00 ±0.00 0.67 ±0.47 0.00 ±0.00 0.00 ±0.00 0.45 ±0.32 0.00 ±0.00 0.67 ±0.00 0.00 ±0.00 Extrap. 0.13 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.02 ±0.03 0.00 ±0.00 0.15 ±0.06 0.79 ±0.16 0.25 ± 0.08 ¯ {}_{\scriptscriptstyle\pm\underline{0.08}} 0.17 ±0.19 0.00 ±0.00 0.00 ±0.00 0.06 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 VisitAll Val. 1.00 0.00 ±0.00 0.00 ±0.00 0.14 ±0.12 0.00 ±0.00 1.00 ±0.00 0.33 ±0.09 0.93 ±0.04 0.99 ± 0.02 ¯ {}_{\scriptscriptstyle\pm\underline{0.02}} 0.99 ± 0.02 ¯ {}_{\scriptscriptstyle\pm\underline{0.02}} 0.79 ±0.29 1.00 ±0.00 1.00 ±0.00 0.03 ±0.04 0.49 ±0.02 0.13 ±0.00 0.92 ±0.00 Interp. 1.00 0.00 ±0.00 0.05 ±0.04 0.67 ±0.18 0.41 ±0.22 1.00 ±0.00 0.87 ±0.01 0.99 ± 0.01 ¯ {}_{\scriptscriptstyle\pm\underline{0.01}} 1.00 ±0.00 1.00 ±0.00 0.99 ± 0.01 ¯ {}_{\scriptscriptstyle\pm\underline{0.01}} 1.00 ±0.00 1.00 ±0.00 0.56 ±0.02 0.38 ±0.02 0.86 ±0.00 0.95 ±0.00 Extrap. 0.50 0.00 ±0.00 0.00 ±0.00 0.02 ±0.02 0.00 ±0.00 0.42 ±0.11 0.00 ±0.00 0.15 ±0.05 0.64 ± 0.12 ¯ {}_{\scriptscriptstyle\pm\underline{0.12}} 0.47 ±0.05 0.59 ±0.40 0.08 ±0.00 0.87 ±0.00 0.00 ±0.00 0.03 ±0.01 0.00 ±0.00 0.13 ±0.00 Logistics Val. 1.00 0.00 ±0.00 0.00 ±0.00 0.08 ± 0.12 ¯ {}_{\scriptscriptstyle\pm\underline{0.12}} 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.17 ±0.12 0.08 ± 0.12 ¯ {}_{\scriptscriptstyle\pm\underline{0.12}} 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 Interp. 1.00 0.00 ±0.00 0.07 ±0.05 0.44 ± 0.09 ¯ {}_{\scriptscriptstyle\pm\underline{0.09}} 0.19 ±0.14 0.11 ±0.00 0.22 ±0.31 0.26 ±0.29 0.22 ±0.31 0.78 ±0.16 0.29 ±0.10 0.11 ±0.00 0.00 ±0.00 0.18 ±0.10 0.11 ±0.00 0.44 ± 0.00 ¯ {}_{\scriptscriptstyle\pm\underline{0.00}} 0.11 ±0.00 Extrap. 0.26 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00

[50] h2: Results and Analysis

[51] p: Table 1 reports satisficing-plan success rates across all domains, splits, representations, model classes, and prediction modes. The primary empirical finding is that explicit transition-model learning combined with size-invariant relational representations yields stronger or matching extrapolation than action-centric sequence prediction in domains with locally factored domains, while remaining insufficient for the Logistics benchmark under strict size extrapolation.

[52] h4: Comparison with action-centric planners.

[53] p: Under strict extrapolation, Plansformer and all PlanGPT variants achieve 0.00 0.00 success across all four domains. Plansformer further exhibits 0.00 0.00 on non- Blocksworld domains since they are not present in its training data. SATr attains non-zero extrapolation in Blocksworld ( 0.13 0.13 ), Gripper ( 0.79 0.79 ), and VisitAll ( 0.64 0.64 ), but fails in Logistics . The best state-centric models exceed SATr in Blocksworld (WL-XGB delta 0.45 0.45 vs. 0.13 0.13 ) and VisitAll ( 0.87 0.87 vs. 0.64 0.64 ), while SATr remains superior in Gripper extrapolation ( 0.79 0.79 vs. 0.25 0.25 ). Notably, these gains are obtained using compact transition models trained on unaugmented state trajectories: our LSTM has ∼ {\sim} 1M parameters and XGBoost ∼ {\sim} 115K tree nodes, compared to ∼ {\sim} 25–35M (SATr), ∼ {\sim} 125M (PlanGPT), and ∼ {\sim} 220M (Plansformer). Furthermore, SATr augments training data via symmetry-based state-space expansion, whereas our models are trained on the original small training sets without any augmentation (e.g., 9 instances in Blocksworld). This indicates that, under appropriate relational abstractions, explicit transition learning can match or exceed extrapolation at orders-of-magnitude lower model and data cost, suggesting that learning domain physics provides a stronger inductive bias for generalization than architectural scale or data augmentation alone. A detailed breakdown of parameter counts and training data requirements is provided in Appendix section C.2 .

[54] h4: Effect of size-invariant relational representations.

[55] p: Across all domains, FSF-based encodings yield negligible extrapolation performance: Blocksworld ( 0.00 0.00 ), Gripper ( 0.00 0.00 ), VisitAll ( ≤ 0.13 \leq 0.13 ), and Logistics ( 0.00 0.00 ). In contrast, WL-based models achieve strictly positive extrapolation in three domains. In Blocksworld , WL-XGB (delta) reaches 0.45 0.45 compared to 0.00 0.00 for all FSF variants. In VisitAll , WL-XGB (delta) reaches 0.87 0.87 while FSF-XGB (delta) reaches only 0.13 0.13 . This establishes that extrapolation beyond the training object bound requires a permutation- and size-invariant abstraction ϕ : S → ℝ D \phi:S\rightarrow\mathbb{R}^{D} . Fixed-slot encodings restrict the hypothesis class to a bounded object universe and therefore fail when | 𝒪 | test > | 𝒪 | train |\mathcal{O}|_{\text{test}}>|\mathcal{O}|_{\text{train}} .

[56] h4: Effect of residual transition modeling.

[57] p: For tree-based models, residual parameterization consistently improves extrapolation. In Blocksworld , WL-XGB improves from 0.25 0.25 (state) to 0.45 0.45 (delta). In VisitAll , it improves from 0.08 0.08 to 0.87 0.87 . This behavior is consistent with STRIPS transition semantics, γ ⁡ ( s , a ) = ( s ∖ Del ​ ( a ) ) ∪ Add ​ ( a ) , \gamma(s,a)=(s\setminus\text{Del}(a))\cup\text{Add}(a), which induces sparse state differences. The delta formulation constrains learning to the subspace of changed fluents, reducing regression variance for non-parametric models. For LSTM, the effect is domain dependent: delta improves Blocksworld extrapolation ( 0.03 → 0.15 0.03\rightarrow 0.15 ) but degrades Gripper ( 0.25 → 0.17 0.25\rightarrow 0.17 ), indicating interaction between residual bias and recurrent state memory.

[58] h4: Sequential versus non-sequential transition learning.

[59] p: Comparing WL-LSTM and WL-XGB isolates the role of temporal memory. In Gripper extrapolation, WL-LSTM (state) attains 0.25 0.25 while both XGB variants remain at 0.00 0.00 , indicating that under the chosen abstraction the induced transition kernel P ⁡ ( ϕ ⁡ ( s t + 1 ) ∣ ϕ ⁡ ( s t ) , ϕ ⁡ ( g ) ) P(\phi(s_{t+1})\mid\phi(s_{t}),\phi(g)) is not well-approximated by a purely local regressor. In contrast, in Blocksworld and VisitAll , WL-XGB (delta) outperforms WL-LSTM: Blocksworld ( 0.45 0.45 vs. 0.15 0.15 ) and VisitAll ( 0.87 0.87 vs. 0.59 0.59 ), indicating that the Markovian assumption, where the future depends only on the present state and not history, suffices under relational abstraction in these domains.

[60] h4: Limitations under hierarchical causal coupling.

[61] p: All learned models, including all state-centric variants, achieve 0.00 0.00 extrapolation in Logistics . Even Fast Downward degrades from 1.00 1.00 (validation) to 0.26 0.26 (extrapolation) under a 60-second timeout, reflecting the exponential state-space growth of extrapolation instances. The Logistics domain exhibits deep multi-layer causal coupling across object types and transport modalities, which is not preserved under local successor matching. This identifies a concrete structural limitation of one-step neural transition prediction under strict size extrapolation for this domain.

[62] h4: Summary of empirical findings.

[63] p: The results support three data-grounded conclusions: (i) size-invariant relational representations are necessary for extrapolation beyond training object bounds; (ii) residual (delta) modeling significantly improves non-parametric transition learning in sparse STRIPS domains; and (iii) the necessity of sequential memory in transition learning is domain dependent. Transition-model learning alone, however, remains insufficient for hierarchical domains under strict extrapolation. An extended experimental analysis is presented in Appendix section C .

[64] h2: Conclusion and Future Work

[65] p: We presented a state-centric formulation of generalized planning in which models learn to predict successor states rather than action sequences. When combined with size- and permutation-invariant relational embeddings, this approach enables compact transition models ( ∼ {\sim} 1M parameters, no data augmentation) to achieve strong extrapolation performance in locally factored domains, matching or exceeding Transformer baselines ( ∼ {\sim} 25–220M parameters) that rely on orders of magnitude more data and parameters. Empirically, our results show that explicit transition modeling provides a stronger inductive bias for extrapolation than architectural scale alone, though limitations remain in domains with hierarchical and long-range dependencies. The neuro-symbolic decoding interface further improves robustness by enforcing symbolic validity at every planning step. Future work will target hierarchical and long-range dependency domains, where one-step state prediction fails under strict extrapolation. We will extend the state-centric framework to multi-step or abstract transitions while preserving symbolic verification.

[66] h2: Acknowledgments

[67] p: This work is partially supported by NSF Awards #2454027 and NAIRR250014, and Faculty Award by JP Morgan Research.

[68] h2: References

[69] h2: Appendix

[70] p: This appendix provides supplementary material to support reproducibility and extended analysis. It is organized as follows:

[71] p: A . Notation and Terminology . A

[72] p: B . Extended Related Work . B

[73] p: C . Extended Experimental Analysis . C

[74] p: D . Dataset Details and Statistics . D

[75] p: E . Weisfeiler–Leman Graph Embedding Details . E

[76] p: F . Fixed-Size Factored Encoding Details . F

[77] p: G . Technical Implementation Pipeline . G

[78] h2: Appendix A Notation and Terminology

[79] p: We summarize all symbols and technical terms used throughout the paper for clarity and reproducibility in Table 2 .

[80] figure: Table 2: Summary of notation used throughout the paper. Category Symbol Meaning Planning Σ = ⟨ S , A , γ ⟩ \Sigma=\langle S,A,\gamma\rangle State-transition system (set of states S S , actions A A , and transition function γ \gamma ) S S Set of all symbolic world states A , 𝒜 A,\mathcal{A} Set of grounded actions (operators) γ : S × 𝒜 → S \gamma:S\times\mathcal{A}\rightarrow S Deterministic transition function 𝒪 \mathcal{O} Finite object set in a planning instance 𝒫 \mathcal{P} Predicate vocabulary 𝒫 ⁡ ( 𝒪 ) \mathcal{P}(\mathcal{O}) Set of all grounded predicates over 𝒪 \mathcal{O} s ⊆ 𝒫 ⁡ ( 𝒪 ) s\subseteq\mathcal{P}(\mathcal{O}) A symbolic state Π = ⟨ Σ , s 0 , G ⟩ \Pi=\langle\Sigma,s_{0},G\rangle ; Π = ⟨ 𝒪 , 𝒫 , 𝒜 , s 0 , g ⟩ \Pi=\langle\mathcal{O},\mathcal{P},\mathcal{A},s_{0},g\rangle Planning task (global and instance-level formulations) Goals & Successors s 0 s_{0} Initial state of a planning instance G ⊆ S G\subseteq S Set of goal states in the state-transition formulation g ⊆ 𝒫 ⁡ ( 𝒪 ) g\subseteq\mathcal{P}(\mathcal{O}) Goal condition in the propositional formulation Succ ⁡ ( s ) \mathrm{Succ}(s) Set of valid symbolic successors of state s s under γ \gamma s t + 1 = γ ⁡ ( s t , a t ) s_{t+1}=\gamma(s_{t},a_{t}) Successor state obtained by applying action a t a_{t} in s t s_{t} Learning & Transitions 𝒟 train , 𝒟 test \mathcal{D}_{\text{train}},\mathcal{D}_{\text{test}} Training and test distributions over planning instances 𝒯 θ \mathcal{T}_{\theta} Learned goal-conditioned transition model s ^ t + 1 \hat{s}_{t+1} Predicted successor state from 𝒯 θ \mathcal{T}_{\theta} ϕ : S → ℝ D \phi:S\rightarrow\mathbb{R}^{D} Fixed-dimensional state embedding ϕ ⁡ ( g ) \phi(g) Embedded representation of the goal condition f θ f_{\theta} Delta-prediction function in the residual transition parameterization Δ t \Delta_{t} Residual transition update at step t t ϕ ^ ​ ( s t + 1 ) \hat{\phi}(s_{t+1}) Predicted next-state embedding, e.g., ϕ ^ ​ ( s t + 1 ) = ϕ ⁡ ( s t ) + Δ t \hat{\phi}(s_{t+1})=\phi(s_{t})+\Delta_{t} 𝐯 t \mathbf{v}_{t} Target embedding used for decoding at step t t Decoding s t + 1 = arg ⁡ min s ′ ∈ Succ ⁡ ( s t ) ⁡ ‖ ϕ ⁡ ( s ′ ) − 𝐯 t ‖ 2 s_{t+1}=\displaystyle\arg\min_{s^{\prime}\in\mathrm{Succ}(s_{t})}\|\phi(s^{\prime})-\mathbf{v}_{t}\|_{2} Neuro-symbolic successor selection rule a t = γ − 1 ​ ( s t → s t + 1 ) a_{t}=\gamma^{-1}(s_{t}\rightarrow s_{t+1}) Action inducing the selected symbolic transition T T Plan horizon (length of π \pi ) π = ⟨ a 1 , … , a T ⟩ \pi=\langle a_{1},\dots,a_{T}\rangle Plan as an action sequence Representations WL Weisfeiler–Leman (graph-kernel) state embedding FSF Fixed-Size Factored state encoding ILG Instance Learning Graph (relational encoding of ( s , g ) (s,g) ) G s , g G_{s,g} Relational instance graph encoding the pair ( s , g ) (s,g) k k Number of WL refinement iterations D D Dimensionality of the embedding ϕ ⁡ ( s ) ∈ ℝ D \phi(s)\in\mathbb{R}^{D} Models LSTM Parametric recurrent transition model XGBoost (XGB) Tree-based non-parametric regressor State mode Direct prediction of ϕ ⁡ ( s t + 1 ) \phi(s_{t+1}) Delta mode Prediction of residual Δ t \Delta_{t} with reconstruction ϕ ⁡ ( s t ) + Δ t \phi(s_{t})+\Delta_{t} θ \theta Trainable parameters of the learned models γ ^ \hat{\gamma} Learned approximation of the symbolic transition function γ \gamma Evaluation Validation / Interpolation / Extrapolation Size-based dataset splits by object count Satisficing plan Any valid plan whose execution reaches a goal state FD Fast Downward planner (A* with LM-cut heuristic, 60s timeout) Coverage / Success rate Fraction of test instances for which a satisficing plan is found

[81] h2: Appendix B Extended Related Work

[82] p: This section expands on the related work discussion in the main paper, providing additional context and citations for each research direction relevant to our work.

[83] h3: B.1 Learning for Generalized Planning

[84] p: Generalized Planning (GP) seeks solution strategies that transfer across problem instances within a domain, rather than solving each instance independently ( Segovia-Aguas et al. 2021 ) . Early neural approaches introduced relational inductive biases to enable such transfer. Action Schema Networks (ASNs) ( Toyer et al. 2018 ) exploited the lifted action structure of planning domains by constructing neural architectures that mirror action schemas, enabling policies to generalize beyond training instances. Rivlin et al. (2020) combined graph neural networks with deep reinforcement learning to learn Blocksworld policies that scale to instances orders of magnitude larger than those seen during training. These works established that an appropriate relational structure is critical for extrapolation in learned planners. More recent approaches have explored diverse architectural choices for GP. Ståhlberg et al. (2022) investigated learning general policies represented as finite-state controllers, providing theoretical grounding for the expressivity required for GP.

[85] h3: B.2 Symmetry and Invariance in Neural Planning

[86] p: A fundamental challenge in neural planning is handling the symmetries inherent in planning problems: permuting object names should not change the solution structure. This has motivated architectures with explicit invariance properties. Graph Neural Networks (GNNs) naturally handle permutation invariance through message-passing operations ( Battaglia et al. 2018 ) .

[87] p: The Symmetry-Aware Transformer (SATr) framework ( Fritzsche et al. 2025 ) addresses symmetry in sequence-to-sequence planning. It introduces three innovations: compositional tokenization (separating objects and predicates), removal of positional encodings (preventing memorization of absolute positions), and contrastive learning objectives (encouraging mapping of symmetric states to similar representations). SATr achieves state-of-the-art performance on several IPC domains through extensive data augmentation (state-space expansion).

[88] p: Our work differs from SATr in two fundamental respects. First, we adopt a state-centric rather than action-centric objective: predicting successor states rather than next actions. This forces the model to learn transition dynamics explicitly, providing natural grounding that architectural modifications alone cannot guarantee. Second, we achieve competitive generalization without massive data augmentation, relying instead on size-invariant representations (WL embeddings) that provide structural inductive bias.

[89] h3: B.3 Graph-Based State Representations

[90] p: To handle variable-sized object sets, recent planners use graph-based state representations where objects are nodes and predicates define edges or features. Hypergraph networks such as STRIPS-HGN ( Shen et al. 2020 ) learned domain-independent heuristics directly from planning graphs. Chen et al. (2023) proposed GOOSE, a GNN-based heuristic learner that significantly outperformed STRIPS-HGN and generalized to much larger problem instances. Subsequent work ( Chen et al. 2024 ) showed that classical Weisfeiler-Leman (WL) graph kernels ( Weisfeiler and Leman 1968 ; Shervashidze et al. 2011 ) with simple regression models can match or exceed GNN performance at orders of magnitude lower computational cost. This finding motivates our use of WL embeddings: they provide the expressivity of 1-WL message-passing GNNs while enabling deployment with lightweight models.

[91] p: Recent extensions have further improved graph-based representations for planning. Chen and Thiébaux (2024) introduced domain-independent graph transformations that enhance generalization, while Chen (2025) provided theoretical analysis connecting WL expressivity to planning-specific structures. Hao et al. (2025) demonstrated effective combinations of WL features with neural architectures for learning domain-independent heuristics.

[92] h3: B.4 Action-Centric Sequence Models for Planning

[93] p: Another line of work formulates plan generation as a sequence prediction task. Plansformer ( Pallagani et al. 2022 ) fine-tuned a Transformer on symbolic plan traces to generate action sequences with high validity on classical planning benchmarks, substantially outperforming zero-shot language models. More recently, PlanGPT ( Rossetti et al. 2024b ) trained GPT-style architectures directly on planning data to learn general planning policies. While effective in-distribution, such autoregressive models often suffer from state drift and logical inconsistency on longer horizons or out-of-distribution problems due to the lack of explicit state tracking. Concurrent work by Shlomi et al. (2025) explores LLM-based transition prediction from ( s , a ) (s,a) pairs, but targets single-instance prediction rather than size-invariant generalized planning.

[94] h4: Hybrid LLM–Symbolic Planning.

[95] p: To mitigate these limitations, several hybrid frameworks integrate LLMs with symbolic planners or validators. LLM+P ( Liu et al. 2023 ) uses an LLM to generate PDDL formulations that are solved by a classical planner, while recent PlanGPT variants incorporate symbolic validation to enforce action applicability ( Rossetti et al. 2024a ) . Kambhampati et al. (2024) formalized this paradigm as LLM-Modulo , advocating tight coupling between LLMs and model-based solvers. In robotics, SayCan ( Ahn et al. 2022 ) combines language models with learned affordance models to iteratively select feasible actions for long-horizon task execution.

[96] h4: Model-Based Learning and World Models.

[97] p: In reinforcement learning, learning explicit transition dynamics has proven beneficial for planning and generalization. World Models ( Ha and Schmidhuber 2018 ) and subsequent model-based RL methods demonstrate that agents can learn compact environment simulators and plan via internal rollouts. However, most neural planners for classical planning remain action-centric or heuristic-driven and do not explicitly learn the symbolic transition dynamics. DreamerV3 ( Hafner et al. 2023 ) extends world-model learning to diverse RL domains, motivating explicit dynamics modeling.

[98] h4: Positioning of Our Work.

[99] p: In contrast to prior action-sequence and heuristic-centric approaches, our work adopts a state-centric, model-based learning paradigm in which the planner is trained to predict state transitions directly. This enables explicit state grounding at every step, mitigates state drift, and yields significantly improved robustness on out-of-distribution instances using compact models. To the best of our knowledge, this transition-prediction formulation with size-invariant representations has not been previously explored for generalized neural planning.

[100] h2: Appendix C Extended Experimental Analysis

[101] p: This section provides additional experimental analysis, including performance trends across problem sizes and per-problem breakdowns.

[102] h3: C.1 Performance Across Data Sets

[103] p: Figures 2 – 4 show satisficing-plan success rate across different data splits, with plots showing the validation, interpolation, and extrapolation splits for each domain. These figures visualize the data presented in Table 1, providing a more intuitive view of performance trends across problem sizes and model configurations.

[104] figure: Figure 2: Satisficing-plan success rates on the validation split across all domains, comparing PlanGPT, SATr, WL-based, and FSF baselines.

[105] figure: Figure 3: Satisficing-plan success rates on the interpolation split, comparing PlanGPT, SATr, WL-based, and FSF baselines for generalization to in-distribution problem instances.

[106] figure: Figure 4: Satisficing-plan success rates on the extrapolation split, , comparing PlanGPT, SATr, WL-based, and FSF baselines for generalization in out-of-distribution problem instances.

[107] h3: C.2 Model and Data Efficiency Analysis

[108] p: A central empirical observation of this work is that explicit transition-model learning achieves competitive or superior extrapolation to action-centric Transformer baselines while requiring dramatically fewer parameters and training data. This subsection provides detailed breakdowns supporting these claims.

[109] h4: Parameter Count Derivations.

[110] p: Table 3 summarizes model sizes across all methods. We detail the parameter calculations for our models below.

[111] figure: Table 3: Model size comparison across all methods. SATr estimates are derived from architectural specifications in Fritzsche et al. (2025) (12-layer shared-weight encoder/decoder, hidden size 768); exact counts depend on domain-specific vocabulary embeddings, which are not reported in the SATr work. Method Parameters Architecture Ratio Plansformer ∼ \sim 220M CodeT5 ∼ \sim 230 × \times PlanGPT ∼ \sim 125M GPT-2 ∼ \sim 130 × \times SATr (enc–dec) ∼ \sim 25–35M Transformer ∼ \sim 30 × \times Ours (LSTM) ∼ \sim 0.93M 2-layer LSTM 1 × \times Ours (XGB) ∼ \sim 115K nodes Gradient boosting —

[112] p: LSTM parameter breakdown. The LSTM architecture comprises dual linear encoders ( D → 32 D\rightarrow 32 ), a two-layer LSTM (256-unit hidden size), and a two-stage output head ( 256 → 256 → D 256\rightarrow 256\rightarrow D ). The parameter count is dominated by the recurrent layers ( ∼ \sim 0.86M) and scales linearly with the embedding dimension D D . Across all experimental domains where D D ranges from 412 to 723, the model contains between ∼ \sim 0.88M and ∼ \sim 0.97M trainable parameters, which we report as ∼ \sim 1M.

[113] p: XGBoost model size. XGBoost learns an ensemble of regression trees via gradient boosting. Model size is measured in total tree nodes across all boosting rounds and output dimensions. With a maximum depth of 8 and early stopping, typical models contain ∼ \sim 115,000 total nodes across all trees. Unlike neural models, XGBoost has no “trainable parameters” in the gradient-descent sense; the tree structure and leaf values are determined by the training algorithm.

[114] h2: Appendix D Dataset Details and Statistics

[115] figure: Table 4: Dataset statistics. Each cell shows count (complexity values) for the corresponding split. Complexity is measured in blocks, balls, goals, or cells depending on the domain. Training uses small instances; extrapolation tests generalization to significantly larger problems. Domain Train Validation Interpolation Extrapolation Blocksworld (blocks) 9 (4, 6, 7) 3 (8) 3 (5) 20 (9–17) Gripper (balls) 4 (2, 4, 6, 8) 2 (9, 10) 3 (3, 5, 7) 16 (12–42, even) Logistics (goals) 12 (1, 3, 5) 4 (6) 9 (2, 4) 18 (7–15) VisitAll (cells) 207 (1, 3, 4, 6, 10, 11, 12, 14, 16) 24 (18, 20) 37 (2, 5, 8, 9, 15) 219 (24–121)

[116] h3: D.1 Domain Descriptions

[117] p: We evaluate on four standard IPC benchmark domains that admit a classical STRIPS-style representation. Each domain is specified by a tuple ⟨ 𝒪 , 𝒫 , 𝒜 ⟩ \langle\mathcal{O},\mathcal{P},\mathcal{A}\rangle , where 𝒪 \mathcal{O} is the object set, 𝒫 \mathcal{P} is the predicate vocabulary, and 𝒜 \mathcal{A} is the operator set inducing a deterministic transition function γ ⁡ ( s , a ) = s ∖ Del ​ ( a ) ∪ Add ​ ( a ) \gamma(s,a)=s\setminus\text{Del}(a)\cup\text{Add}(a) . Detailed dataset statistics for each split are reported in Table 4 .

[118] h4: Blocksworld.

[119] p: Blocksworld is a canonical manipulation domain defined over a set of blocks 𝒪 = { b 1 , … , b n } \mathcal{O}=\{b_{1},\ldots,b_{n}\} . The predicate set includes 𝒫 = { on ​ ( x , y ) , ontable ​ ( x ) , clear ​ ( x ) , holding ​ ( x ) , handempty } \mathcal{P}=\{\textit{on}(x,y),\textit{ontable}(x),\textit{clear}(x),\textit{holding}(x),\textit{handempty}\} . The operator set 𝒜 \mathcal{A} consists of pickup , putdown , stack , and unstack . A state s ⊆ 𝒫 ⁡ ( 𝒪 ) s\subseteq\mathcal{P}(\mathcal{O}) encodes a partial order over blocks. The branching factor grows quadratically in the number of clear blocks due to all admissible stack / unstack combinations. Transitions exhibit sparse add–delete structure, making this domain well-suited for residual state prediction.

[120] h4: Gripper.

[121] p: Gripper models a robot with two grippers transporting balls between rooms. The object set factorizes as 𝒪 = ℬ ∪ ℛ ∪ { robot } \mathcal{O}=\mathcal{B}\cup\mathcal{R}\cup\{\textit{robot}\} , where ℬ \mathcal{B} are balls and ℛ \mathcal{R} are rooms. Predicates include at ​ ( x , r ) \textit{at}(x,r) , free ​ ( g ) \textit{free}(g) , carry ​ ( x , g ) \textit{carry}(x,g) , and at-robot ​ ( r ) \textit{at-robot}(r) . Operators include move , pick , and drop . Although single-step transitions remain sparse, Gripper induces longer causal chains in which object transport must be synchronized with robot motion, creating trajectory-level dependencies not captured by purely local transitions.

[122] h4: Logistics.

[123] p: Logistics is a multi-modal transportation domain with object types 𝒪 = 𝒫 ∪ 𝒯 ∪ 𝒜 ∪ 𝒞 \mathcal{O}=\mathcal{P}\cup\mathcal{T}\cup\mathcal{A}\cup\mathcal{C} (packages, trucks, airplanes, cities). Predicates include at ​ ( x , l ) \textit{at}(x,l) , in ​ ( x , v ) \textit{in}(x,v) , and at-vehicle ​ ( v , l ) \textit{at-vehicle}(v,l) . Operators include load , unload , drive , and fly . Unlike Blocksworld and VisitAll, Logistics induces long-range dependencies across heterogeneous object types and transport layers. Valid plans require coordination across multiple abstraction levels, resulting in deep coupling between distant subgoals. This property severely limits the effectiveness of one-step transition prediction under strict size extrapolation.

[124] h4: VisitAll.

[125] p: VisitAll is a grid navigation domain defined over a lattice of cells 𝒪 = { ( i , j ) } \mathcal{O}=\{(i,j)\} . Predicates include at ​ ( r , c ) \textit{at}(r,c) and visited ​ ( c ) \textit{visited}(c) . Operators correspond to unit grid motions that update both at and visited . The goal is g = ⋀ c ∈ 𝒪 visited ​ ( c ) g=\bigwedge_{c\in\mathcal{O}}\textit{visited}(c) . Although each transition affects only a small number of fluents, the goal conjunct grows linearly with | 𝒪 | |\mathcal{O}| , and the resulting state space grows exponentially. This domain isolates the effect of goal scaling under otherwise simple local dynamics.

[126] h4: Relevance to State-Centric Modeling.

[127] p: All four domains admit deterministic STRIPS semantics with sparse add–delete operators. This ensures that successor states admit a decomposition

[128] table: s t + 1 = s t ∖ Del ​ ( a t ) ∪ Add ​ ( a t ) , s_{t+1}=s_{t}\setminus\text{Del}(a_{t})\cup\text{Add}(a_{t}),

[129] p: which directly motivates our residual transition formulation ϕ ^ ​ ( s t + 1 ) = ϕ ⁡ ( s t ) + Δ t . \hat{\phi}(s_{t+1})=\phi(s_{t})+\Delta_{t}. The domains thus provide a controlled testbed for evaluating whether learned neural approximations γ ^ \hat{\gamma} can preserve symbolic transition structure under strict size extrapolation.

[130] h2: Appendix E Weisfeiler–Leman Graph Embedding Details

[131] p: This section provides a comprehensive description of the Weisfeiler–Leman (WL) graph embedding procedure used in our state-centric planning framework.

[132] h3: E.1 Background: The WL Algorithm

[133] p: The Weisfeiler–Leman (WL) algorithm ( Weisfeiler and Leman 1968 ) is an iterative color refinement procedure for graphs. Given a graph G = ( V , E ) G=(V,E) with initial node colors c ( 0 ) : V → Σ c^{(0)}:V\rightarrow\Sigma , the algorithm iteratively refines colors by aggregating neighborhood information:

[134] table: c ( k + 1 ) ​ ( v ) = Hash ​ ( c ( k ) ​ ( v ) , { { ( c ( k ) ​ ( u ) , ℓ ⁡ ( u , v ) ) ∣ u ∈ 𝒩 ⁡ ( v ) } } ) c^{(k+1)}(v)=\\ \textsc{Hash}\left(c^{(k)}(v),\{\!\{(c^{(k)}(u),\ell(u,v))\mid u\in\mathcal{N}(v)\}\!\}\right)

[135] p: where 𝒩 ⁡ ( v ) \mathcal{N}(v) denotes the neighbors of v v , ℓ ⁡ ( u , v ) \ell(u,v) is the edge label, and { { ⋅ } } \{\!\{\cdot\}\!\} denotes a multiset. After k k iterations, the algorithm produces a multiset of colors 𝒞 ( k ) = ⋃ i = 0 k { { c ( i ) ​ ( v ) ∣ v ∈ V } } \mathcal{C}^{(k)}=\bigcup_{i=0}^{k}\{\!\{c^{(i)}(v)\mid v\in V\}\!\} .

[136] h3: E.2 Instance Learning Graph Construction

[137] p: We use the Instance Learning Graph (ILG) representation ( Chen et al. 2024 ) to encode planning states. Given a planning instance Π = ⟨ 𝒪 , 𝒫 , 𝒜 , s , g ⟩ \Pi=\langle\mathcal{O},\mathcal{P},\mathcal{A},s,g\rangle , the ILG G s , g = ( V , E , 𝐅 cat , 𝐋 ) G_{s,g}=(V,E,\mathbf{F}_{\text{cat}},\mathbf{L}) is constructed as follows:

[138] h4: Nodes.

[139] p: V = 𝒪 ∪ X ⁡ ( s ) ∪ g V=\mathcal{O}\cup X(s)\cup g , where:

[140] p: 𝒪 \mathcal{O} : object nodes (one per domain object)

[141] p: X ⁡ ( s ) = X p ​ ( s ) ∪ X n ​ ( s ) X(s)=X_{p}(s)\cup X_{n}(s) : state variable nodes (true propositions and numeric fluents)

[142] p: g g : goal condition nodes

[143] h4: Edges.

[144] p: For each grounded predicate p = σ ⁡ ( o 1 , … , o ar ​ ( σ ) ) ∈ X ⁡ ( s ) ∪ g p {p=\sigma(o_{1},\ldots,o_{\text{ar}(\sigma)})\in X(s)\cup g_{p}} :

[145] table: E ⊇ { ( p , o i ) ∣ i ∈ [ 1 , ar ​ ( σ ) ] } E\supseteq\{(p,o_{i})\mid i\in[1,\text{ar}(\sigma)]\}

[146] h4: Node Features.

[147] p: Categorical features 𝐅 cat : V → Σ V \mathbf{F}_{\text{cat}}:V\rightarrow\Sigma_{V} encode node semantics:

[148] table: 𝐅 cat ​ ( u ) = { object if ​ u ∈ 𝒪 ∖ 𝒪 const u if ​ u ∈ 𝒪 const ( pred ​ ( u ) , apg ) if ​ u ∈ X p ​ ( s ) ∩ g p ( pred ​ ( u ) , upg ) if ​ u ∈ g p ∖ X p ​ ( s ) ( pred ​ ( u ) , apn ) if ​ u ∈ X p ​ ( s ) ∖ g p \mathbf{F}_{\text{cat}}(u)=\begin{cases}\texttt{object}&\text{if }u\in\mathcal{O}\setminus\mathcal{O}_{\text{const}}\\ u&\text{if }u\in\mathcal{O}_{\text{const}}\\ (\texttt{pred}(u),\texttt{apg})&\text{if }u\in X_{p}(s)\cap g_{p}\\ (\texttt{pred}(u),\texttt{upg})&\text{if }u\in g_{p}\setminus X_{p}(s)\\ (\texttt{pred}(u),\texttt{apn})&\text{if }u\in X_{p}(s)\setminus g_{p}\end{cases}

[149] h4: Edge Labels.

[150] p: 𝐋 : E → ℕ \mathbf{L}:E\rightarrow\mathbb{N} encodes argument position: 𝐋 ⁡ ( p , o i ) = i \mathbf{L}(p,o_{i})=i .

[151] h3: E.3 Feature Extraction

[152] p: Given the ILG G s , g G_{s,g} and k k WL iterations, we extract a fixed-dimensional feature vector ϕ ⁡ ( s , g ) ∈ ℝ D \phi(s,g)\in\mathbb{R}^{D} as follows:

[153] p: Color Refinement : Run k k iterations of WL on G s , g G_{s,g} , producing color multiset 𝒞 ( k ) \mathcal{C}^{(k)} .

[154] p: Vocabulary Construction : During training, collect all unique colors across all training graphs to form vocabulary 𝒱 = { c 1 , … , c D } \mathcal{V}=\{c_{1},\ldots,c_{D}\} .

[155] p: Histogram Embedding : For each graph, compute:

[156] table: ϕ ​ ( s , g ) i = Count ​ ( 𝒞 ( k ) , c i ) , i ∈ [ 1 , D ] \phi(s,g)_{i}=\textsc{Count}(\mathcal{C}^{(k)},c_{i}),\quad i\in[1,D]

[157] h3: E.4 Implementation Details

[158] p: We use the wlplan library ( Chen 2024 ) for WL feature extraction with the following configuration:

[159] p: Graph representation : Instance Learning Graph (ILG)

[160] p: Iterations : k = 2 k=2

[161] p: Hash function : Multiset hash (deterministic)

[162] p: Pruning : None

[163] h4: Vocabulary Sizes.

[164] p: The resulting vocabulary sizes (feature dimensions D D ) per domain are:

[165] table: Domain Dimension D D Blocksworld 587 Gripper 412 Logistics 723 VisitAll 498

[166] h3: E.5 Properties of WL Embeddings

[167] h4: Permutation Invariance.

[168] p: WL embeddings are invariant to object renaming: for any bijection σ : 𝒪 → 𝒪 \sigma:\mathcal{O}\rightarrow\mathcal{O} , we have ϕ ⁡ ( σ ⁡ ( s ) , σ ⁡ ( g ) ) = ϕ ⁡ ( s , g ) \phi(\sigma(s),\sigma(g))=\phi(s,g) .

[169] h4: Size Invariance.

[170] p: The dimension D D depends only on the domain’s predicate structure and training distribution, not on | 𝒪 | |\mathcal{O}| . A model trained on 4-block problems produces embeddings of the same dimension for 100-block problems.

[171] h4: Expressivity.

[172] p: WL embeddings are exactly as expressive as 1-WL message-passing GNNs ( Xu et al. 2018 ) : two graphs receive the same embedding if and only if 1-WL cannot distinguish them.

[173] h4: Computational Complexity.

[174] p: For a graph with n n nodes, maximum degree δ \delta , and k k iterations, the WL algorithm runs in O ⁡ ( n ​ k ​ δ ) O(nk\delta) time, which is linear in graph size for bounded-degree graphs typical in planning.

[175] h2: Appendix F Fixed-Size Factored Encoding Details

[176] p: While factored representations have been extensively studied in planning ( Boutilier et al. 2000 ; Guestrin et al. 2003 ) , our Fixed-Size Factored (FSF) encodings deliberately omit relational structure to serve as a controlled ablation baseline. FSF represents states as vectors of fixed dimension, where each dimension corresponds to a specific object slot with domain-specific semantics. This design isolates the contribution of permutation and size invariance to generalization by providing a representation that: (i) requires a predetermined maximum object count, (ii) depends on fixed object-to-slot mappings, and (iii) necessitates domain-specific manual design.

[177] h3: F.1 General Structure

[178] p: FSF encodings have the form ϕ FSF ​ ( s ) ∈ ℝ N + 1 \phi_{\text{FSF}}(s)\in\mathbb{R}^{N+1} , where N N is the maximum number of objects across all problems in the domain. The encoding consists of:

[179] p: Slot 0 : Global/robot state information

[180] p: Slots 1– N N : Per-object state information

[181] h4: Special Values.

[182] p: − 99.0 -99.0 : Padding (slot unused for this problem size)

[183] p: − 10.0 -10.0 : Don’t-care (goal variable not specified)

[184] h3: F.2 Domain-Specific Semantics

[185] p: Table 5 provides detailed semantics for each domain.

[186] figure: Table 5: Detailed FSF encoding semantics by domain. Domain Slot Interpretation Value Semantics Blocksworld Slot 0: Unused (constant 0) — Slot i i ( i > 0 i>0 ): Block i i 0 0 = on table; − 1 -1 = held by gripper; j > 0 j>0 = on block j j Gripper Slot 0: Robot location Room index where robot is located Slot i i (ball): Ball i i location Room index if at room; − j -j if carried by gripper j j Slot i i (gripper): Gripper i i status 0 0 = free; j > 0 j>0 = holding ball j j Logistics Slot 0: Unused (constant 0) — Slot i i : Object i i (pkg/truck/plane) Location index if at location; − j -j if inside vehicle j j VisitAll Slot 0: Robot position Cell index where robot is located Slot i i ( i > 0 i>0 ): Cell i i 0 0 = unvisited; 1 1 = visited

[187] h3: F.3 Example: Blocksworld Encoding

[188] p: Consider a 4-block Blocksworld state where:

[189] p: Block A is on the table

[190] p: Block B is on Block A

[191] p: Block C is being held

[192] p: Block D is on the table

[193] p: With object ordering { A ↦ 1 , B ↦ 2 , C ↦ 3 , D ↦ 4 } \{A\mapsto 1,B\mapsto 2,C\mapsto 3,D\mapsto 4\} :

[194] table: ϕ FSF ​ ( s ) = [ 0 , 0 ⏟ A on table , 1 ⏟ B on A , − 1 ⏟ C held , 0 ⏟ D on table , − 99 , … ] \phi_{\text{FSF}}(s)=[0,\underbrace{0}_{\text{A on table}},\underbrace{1}_{\text{B on A}},\underbrace{-1}_{\text{C held}},\underbrace{0}_{\text{D on table}},-99,\ldots]

[195] h3: F.4 Limitations of FSF Encodings

[196] h4: No Size Invariance.

[197] p: FSF encodings require a predetermined maximum object count N N . Problems with | 𝒪 | > N |\mathcal{O}|>N cannot be represented. This fundamentally limits extrapolation to larger instances.

[198] h4: No Permutation Invariance.

[199] p: FSF encodings depend on a fixed object-to-slot mapping. Different orderings of the same objects yield different vectors, preventing generalization across equivalent states.

[200] h4: Domain-Specific Design.

[201] p: Each domain requires manual design of the encoding semantics, limiting applicability to new domains without expert knowledge.

[202] p: These limitations motivate the use of WL embeddings, which provide permutation and size invariance without domain-specific engineering.

[203] h2: Appendix G Technical Implementation Pipeline

[204] p: This section describes the complete technical pipeline from symbolic planning instances to trained neural transition models, enabling full reproducibility of our experimental results.

[205] h3: G.1 Data Generation Pipeline

[206] p: The data generation process transforms raw PDDL domain and problem files into machine-learning-ready state trajectory embeddings through four sequential stages.

[207] h4: Stage 1: Symbolic Plan Generation.

[208] p: We use Fast Downward with a two-tier solving strategy to maximize coverage across problem difficulties. The baseline configuration runs A* search with the landmark-cut admissible heuristic under a 60-second timeout. For problems that exceed this limit, we invoke a fallback configuration using greedy best-first search with the FF heuristic and a 300-second timeout. This staged approach achieves high coverage on training instances (which are intentionally kept small) while maintaining plan quality where possible. Plans are written in standard PDDL action-sequence format.

[209] h4: Stage 2: State Trajectory Reconstruction.

[210] p: Given a valid plan, we reconstruct the complete sequence of intermediate world states using the VAL plan validator in verbose mode. VAL applies each action symbolically and outputs the predicates added or deleted at each timestep. We parse this output to build the full trajectory ⟨ s 0 , s 1 , … , s T ⟩ \langle s_{0},s_{1},\ldots,s_{T}\rangle where each s t s_{t} is represented as a sorted list of ground predicates. This reconstruction is necessary because Fast Downward’s search only maintains heuristic state information, not the explicit symbolic states required for supervised learning. The resulting trajectory files are saved in plain-text format with one state per line.

[211] h4: Stage 3: Weisfeiler-Leman Feature Collection.

[212] p: WL embeddings require a fixed vocabulary collected from the training distribution. For each domain, we parse all training trajectory files and construct instance learning graphs G s , g G_{s,g} for every state-goal pair encountered. We run k = 2 k=2 iterations of color refinement and collect the multiset of final node colors across all training graphs. These color strings are sorted lexicographically and assigned integer indices to form the vocabulary 𝒱 \mathcal{V} . The vocabulary size D = | 𝒱 | D=|\mathcal{V}| is domain-dependent but fixed once collected, enabling embeddings of arbitrary test-time problem sizes into ℝ D \mathbb{R}^{D} .

[213] h4: Stage 4: Trajectory Embedding.

[214] p: With the vocabulary established, we embed every trajectory across all data splits. For each state s t s_{t} in a trajectory, we construct its instance graph G s t , g G_{s_{t},g} , perform k = 2 k=2 WL iterations using the fixed vocabulary 𝒱 \mathcal{V} , and compute the normalized color histogram as the embedding ϕ ⁡ ( s t ) ∈ ℝ D \phi(s_{t})\in\mathbb{R}^{D} . Goals are embedded analogously. The resulting trajectory is a matrix of shape [ T , D ] [T,D] where T T is the plan length, stored as a NumPy array alongside a separate goal vector of shape [ D ] [D] . This compact representation supports efficient batch loading during training.

[215] h3: G.2 Transition Model Training

[216] h4: Dataset Construction for LSTM.

[217] p: The LSTM operates on variable-length sequences. For each problem instance, we load the embedded trajectory matrix [ ϕ ⁡ ( s 0 ) , … , ϕ ⁡ ( s T ) ] [\phi(s_{0}),\ldots,\phi(s_{T})] and the goal vector ϕ ⁡ ( g ) \phi(g) . During training, these are collated into padded batches with a custom collate function that tracks the true sequence length of each trajectory. The goal embedding is replicated across all timesteps to form a constant conditioning signal. For delta-mode training, we compute target residuals Δ t = ϕ ⁡ ( s t + 1 ) − ϕ ⁡ ( s t ) \Delta_{t}=\phi(s_{t+1})-\phi(s_{t}) on the fly.

[218] h4: Dataset Construction for XGBoost.

[219] p: XGBoost requires flattened tabular input. We extract all consecutive state pairs ( s t , s t + 1 ) (s_{t},s_{t+1}) from every trajectory and construct feature vectors by concatenating the current state embedding, the goal embedding, and (for delta mode) the difference vector. Concretely, each training example is a row of shape [ 2 ​ D ] [2D] (concatenated state and goal) with a target vector of shape [ D ] [D] (next state or delta). This flattening procedure is applied independently to training and validation splits, yielding dense matrices suitable for gradient boosting.

[220] h4: LSTM Architecture and Training.

[221] p: The LSTM model consists of a linear encoder projecting the D D -dimensional state and goal vectors into a shared 32-dimensional embedding space. These low-dimensional embeddings are concatenated and fed into a two-layer LSTM with 256 hidden units per layer. The LSTM output is passed through a two-layer feedforward head that projects back to the original D D -dimensional space. For state-mode training, we minimize cosine embedding loss between predictions and targets, encouraging alignment in direction. For delta-mode training, we minimize mean squared error on the residual vectors. We train with the Adam optimizer at a learning rate of 10 − 2 10^{-2} for 250 epochs with early stopping based on validation loss.

[222] h4: XGBoost Architecture and Training.

[223] p: XGBoost is configured for multi-output regression using the squared-error objective. We use histogram-based tree construction on GPU with a maximum tree depth of 8 and a learning rate of 0.1. Training proceeds for up to 1000 boosting rounds with early stopping if validation loss does not improve for 10 consecutive rounds. The model learns an ensemble of regression trees that collectively approximate the mapping from [ ϕ ⁡ ( s t ) , ϕ ⁡ ( g ) ] [\phi(s_{t}),\phi(g)] to ϕ ⁡ ( s t + 1 ) \phi(s_{t+1}) or Δ t \Delta_{t} . The best iteration checkpoint is retained based on validation performance.

[224] h4: Loss Function Selection.

[225] p: For state-mode training, we adopt cosine embedding loss rather than mean squared error. This choice reflects the sparse, high-dimensional nature of WL embeddings: states differing by a single predicate may have Euclidean distances dominated by uninformative dimensions, whereas cosine similarity emphasizes directional alignment in the feature space. Empirically, we observe that cosine loss enables more stable convergence for LSTM models predicting full state vectors. For delta-mode training, we use mean squared error directly on the residual vectors Δ t \Delta_{t} , as these deltas are inherently sparse and low-magnitude, making component-wise regression more appropriate than angular alignment. XGBoost uses squared error in both modes as it does not support cosine objectives natively, though the distance metric used during inference (cosine for state mode, Euclidean for delta mode) remains consistent with the training objective’s geometric assumptions.

[226] h3: G.3 Inference and Plan Decoding

[227] h4: Symbolic State Maintenance.

[228] p: During test-time execution, we maintain the current symbolic state s t s_{t} explicitly as a set of ground predicates. This state is initialized to the problem’s s 0 s_{0} and updated only through valid operator applications, ensuring that every intermediate state is well-formed under the domain’s transition function γ \gamma .

[229] h4: Neural Successor Prediction.

[230] p: At each planning step, we embed the current symbolic state and goal to obtain ϕ ⁡ ( s t ) \phi(s_{t}) and ϕ ⁡ ( g ) \phi(g) . These embeddings are passed through the learned transition model to produce either a direct next-state prediction ϕ ^ ​ ( s t + 1 ) \hat{\phi}(s_{t+1}) or a residual prediction Δ t \Delta_{t} that is added to ϕ ⁡ ( s t ) \phi(s_{t}) . The resulting target vector 𝐯 t \mathbf{v}_{t} represents the model’s internal prediction of where the plan should transition next.

[231] figure: Table 6: Complete hyperparameter settings for all models. Parameter LSTM XGBoost Architecture Hidden dimension 256 — Embedding dimension 32 — Number of layers 2 — Tree depth — 8 Training Learning rate 10 − 2 10^{-2} 0.1 Batch size 32 — Max epochs / rounds 250 1000 Early stopping patience 25 10 Optimizer Adam — Loss (state mode) Cosine MSE Loss (delta mode) MSE MSE Inference Beam width 3 3 Max planning steps 100 100 Distance metric (state) Cosine Cosine Distance metric (delta) Euclidean Euclidean Model Size Parameters 927,602 927,602 — Total tree nodes — ∼ 115,000 \sim 115,000

[232] h4: Symbolic Successor Enumeration.

[233] p: Using the ground operator set 𝒜 \mathcal{A} and applicability preconditions, we enumerate all valid symbolic successors Succ ( s t ) = { γ ( s t , a ) ∣ a ∈ 𝒜 , a applicable in s t } \mathrm{Succ}(s_{t})=\{\gamma(s_{t},a)\mid a\in\mathcal{A},\;a\text{ applicable in }s_{t}\} . Each candidate successor is embedded using the same WL procedure as during training, yielding a set of embedding vectors { ϕ ⁡ ( s ′ ) ∣ s ′ ∈ Succ ⁡ ( s t ) } \{\phi(s^{\prime})\mid s^{\prime}\in\mathrm{Succ}(s_{t})\} .

[234] h4: Nearest Neighbor Decoding.

[235] p: We compute the Euclidean distance (for delta mode) or cosine distance (for state mode) between 𝐯 t \mathbf{v}_{t} and each candidate embedding ϕ ⁡ ( s ′ ) \phi(s^{\prime}) . The candidate with minimum distance is selected as the next symbolic state s t + 1 s_{t+1} , and the unique action a a satisfying γ ⁡ ( s t , a ) = s t + 1 \gamma(s_{t},a)=s_{t+1} is appended to the plan. This guarantees that every generated action is applicable and that state evolution respects the symbolic transition semantics.

[236] h4: Termination.

[237] p: Planning terminates when the goal condition g ⊆ s t g\subseteq s_{t} is satisfied or when a maximum horizon of 100 steps is reached. The resulting action sequence is validated externally using VAL to confirm correctness.

[238] h3: G.4 Computational Resources

[239] p: All experiments were conducted on an HPC cluster with the following specifications:

[240] p: GPU : NVIDIA A100 (40GB VRAM)

[241] p: CUDA Version : 11.7

[242] p: CPU : 128 cores per node (for data generation)

[243] p: Memory : 256GB RAM per node

[244] p: Total compute time: approximately 1 GPU-hour for all experiments.

[245] h3: G.5 Hyperparameters

[246] p: Table 6 provides complete hyperparameter settings.

[247] h2: Instructions for reporting errors

[248] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[249] p: Tip: You can select the relevant text first, to include it in your report.

[250] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[251] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
