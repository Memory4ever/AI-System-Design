# Exact-v1 primary excerpts — 19280

L labels are local to each separated original response. Preserved necessary-source tool responses; no reproduction.

## Original response: stdnext3head

Group Distributionally Robust Optimization-Driven Reinforcement Learning for LLM Reasoning (https://arxiv.org/html/2601.19280v1)
citeturn28405view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19280v1","lineno":null}); Total lines: 1191
--------------------------------------------------------------------------------


## Original response: stdnext3core1

Group Distributionally Robust Optimization-Driven Reinforcement Learning for LLM Reasoning (https://arxiv.org/html/2601.19280v1)
citeturn28409view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28405view1","lineno":110}); Total lines: 1191
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Preliminaries L18:     1. cite8†2.1 Reinforcement Learning for Reasoning L19:     2. cite9†2.2 Group-Relative Policy Optimization (GRPO) L20:     3. cite10†2.3 Group Distributionally Robust Optimization L21:   4. cite11†3 Method L22:     1. cite12†3.1 Dynamic Grouping via Online Pass@k L23:       1. cite13†3.1.1 Data-Agnostic Difficulty Estimation L24:       2. cite14†3.1.2 Implementation Details L25:     2. cite15†3.2 Adversarial Prompt Reweighting (Prompt-GDRO) L26:       1. cite16†3.2.1 EMA-Debiased EXP3P Optimization L27:     3. cite17†3.3 Adversarial Rollout Budgeting (Rollout-GDRO) L28:       1. cite18†3.3.1 Constrained Maximization Formulation L29:       2. cite19†3.3.2 Dual Ascent Solver L30:   5. cite20†4 Analysis L31:     1. cite21†4.1 Motivation: Why uniformity can fail in reasoning post-training L32:       1. cite22†GDRO lens. L33:     2. cite23†4.2 Adversary I (Prompt-GDRO): Robustness via EMA-debiased difficulty pressure L34:       1. cite24†From GDRO to a bandit adversary. L35:       2. cite25†Why “EMA-debiased”? Frequency bias vs. intensive difficulty. L36:       3. cite26†How $q_{t}$ acts on GRPO updates (intuition). L37:       4. cite27†4.2.1 Entropic GDRO view: log-sum-exp surrogate and softmax best response L38:         1. cite28†Gradient interpretation. L39:         2. cite29†Connection to Prompt-GDRO. L40:       5. cite30†4.2.2 No-regret interpretation: why this game structure is sensible L41:       6. cite31†4.2.3 Toy validation on MATH: entropy and worst-group robustness L42:     3. cite32†4.3 Adversary II (Rollout-GDRO): Compute allocation as an economic control problem L43:       1. cite33†Recap: compute-neutral rollout budgeting. L44:       2. cite34†4.3.1 A variance proxy for why allocating more rollouts helps L45:       3. cite35†4.3.2 The variance-optimal allocation obeys a square-root law L46:         1. cite36†Implications for Rollout-GDRO. L47:   6. cite37†5 Experiments L48:     1. cite38†5.1 Main Results L49:     2. cite39†5.2 Qualitative Analysis: The Dynamics of Difficulty (Prompt-GDRO) L50:       1. cite40†Capacity-Dependent Distribution Shift. L51:       2. cite41†Visualizing the Wave of Progress. L52:       3. cite42†Adversary lead–lag. L53:     3. cite43†5.3 Qualitative Analysis: Adaptive Compute Allocation (Rollout-GDRO) L54:       1. cite44†5.3.1 The Budget Frontier L55:       2. cite45†5.3.2 Macro-Dynamics of Allocation L56:       3. cite46†5.3.3 Discrete Economic Phases L57:   7. cite47†6 Additional Related Work L58:     1. cite48†6.1 RLVR and Post-training for Reasoning L59:     2. cite49†6.2 Distributionally Robust Optimization in Supervised Learning L60:     3. cite50†6.3 Robust and Distributionally Robust Reinforcement Learning L61:     4. cite51†6.4 Curriculum, Adaptive Compute, and Data Value L62:   8. cite52†7 Limitations and Future Work L63:     1. cite53†Bridge: from two adversaries to open questions. L64:     2. cite54†Empirical scope and missing full-factorial ablations. L65:     3. cite55†RL scaling and compute-optimal post-training. L66:     4. cite56†Adversarial game computation and systems overhead. L67:     5. cite57†Sensitivity to online binning and reward noise. L68:     6. cite58†Generalization and evaluation beyond the current pipeline. L69:     7. cite59†Toward learning from the model’s own experience. L70:     8. cite60†Beyond exponential-weights GDRO: richer ambiguity sets and scalable solvers. L71:     9. cite61†Beyond robustness: adversarial reasoning objectives for safety and risk. L72:   9. cite62†8 Conclusion L73:   10. cite63†References L74:   11. cite64†A Experiment Details L75:     1. cite65†A.1 Shared Training Hyperparameters L76:       1. cite66†A.1.1 Optimization & Architecture L77:       2. cite67†A.1.2 Rollout Generation L78:     2. cite68†A.2 Adversarial Configuration L79:       1. cite69†A.2.1 Prompt-GDRO (The Data Adversary) L80:       2. cite70†A.2.2 Rollout-GDRO (The Compute Adversary) L81:   12. cite71†B Main Theoretical Results: A Game-and-Variance View L82:     1. cite72†B.1 Prompt-GDRO as Entropic GDRO and No-Regret Game Dynamics L83:       1. cite73†B.1.1 Entropy-regularized inner maximization and the log-sum-exp surrogate L84:         1. cite74†Entropic GDRO surrogate. L85:       2. cite75†B.1.2 No-regret dynamics imply approximate robust optimality L86:     2. cite76†B.2 Rollout-GDRO as Variance-Aware Allocation Under a Budget and No-Regret Game Dynamics L87:       1. cite77†B.2.1 A variance proxy for GRPO rollouts L88:         1. cite78†Reference equations from the main paper. L89:         2. cite79†What is guaranteed by the rollout controller vs. what is explained by the variance proxy. L90:       2. cite80†B.2.2 The variance-optimal allocation obeys a square-root law L91:       3. cite81†B.2.3 Discrete rollout arms and an entropic primal–dual view L92:       4. cite82†B.2.4 No-regret primal–dual analysis for Rollout-GDRO L93:         1. cite83†A truncated Lagrangian game. L94:         2. cite84†Primal–dual updates. L95:         3. cite85†Step 1: primal regret bound (entropic mirror descent). L96:         4. cite86†Step 2: dual regret bound (projected gradient ascent). L97:         5. cite87†Step 3: combine regrets and average. L98:         6. cite88†Step 4: deduce objective and budget bounds. L99: cite89†License: CC BY 4.0†info.arxiv.org L100: 
L101: arXiv:2601.19280v1 [cs.LG] 27 Jan 2026
L102: # Group Distributionally Robust Optimization-Driven Reinforcement Learning for LLM Reasoning
L103: 
L104: Kishan Panaganti    Zhenwen Liang    Wenhao Yu    Haitao Mi    Dong Yu Affiliation:  Tencent AI Lab in Bellevue, WA, USA Affiliation: Correspondence to: kpb@global.tencent.com
L105: ###### Abstract
L106: Recent progress in Large Language Model (LLM) reasoning is increasingly driven by the refinement of post-training loss functions and alignment strategies^{1}^{1} 1 Adam Marblestone (paraphrased) on Dwarkesh’s podcast (cite90†YouTube†www.youtube.com ): “The brain’s secret sauce is its loss functions, not its architecture.” .
L107: However, standard Reinforcement Learning (RL) paradigms like Group Relative Policy Optimization (GRPO) remain constrained by static uniformity: uniform prompt sampling and a fixed number of rollouts per prompt. For heterogeneous, heavy-tailed reasoning data, this creates structural inefficiencies that waste compute on already-solved patterns while under-training the long tail of hard problems.
L108: To address this, we propose Multi-Adversary Group Distributionally Robust Optimization (GDRO), an optimization-first framework that moves beyond uniform reasoning models by dynamically adapting the training distribution.
L109: We introduce an Online Difficulty Classifier that partitions prompts into dynamic pass@k difficulty groups.
L110: We then propose two independent GDRO games for post-training: (1) Prompt-GDRO, which employs an EMA-debiased multiplicative-weights bandit sampler to target the intensive difficulty margin and upweight persistently hard groups without frequency bias; and (2) Rollout-GDRO, which uses a shadow-price controller to reallocate rollouts across groups, maximizing gradient variance reduction on hard tasks under a fixed mean budget (compute-neutral).
L111: We provide no-regret guarantees for Prompt-GDRO (via an entropy-regularized GDRO surrogate) and a variance-proxy analysis motivating a square-root optimal rollout allocation for Rollout-GDRO. We validate our framework on the DAPO 14.1k dataset using Qwen3-Base models. Prompt-GDRO and Rollout-GDRO achieve average relative gains of +10.6% and +10.1%, respectively, in pass@8 accuracy across 1.7B, 4B, and 8B scales compared to the GRPO baseline.
L112: Qualitative analysis shows an emergent curriculum: the adversaries shift resources to the evolving reasoning frontier, enhancing the reasoning model’s performance.
L113: cite91†Image: Refer to caption Figure 1: Beyond Uniform Reasoning—A Multi-Adversary Post-Training Framework. Plots on the right represent training steps tail averages ($\geq$60th percentile) capturing the curriculum. (Left) Our framework significantly outperforms the standard GRPO baseline across mathematical reasoning benchmarks via dynamic adaptation. (Center) Prompt-GDRO: The adversary learns a non-uniform curriculum.
L114: Instead of uniform sampling (dashed line), probability mass (purple bars) shifts to the “reasoning frontier” (bins 6–8), targeting the specific difficulty level where learning is most efficient. (Right) Rollout-GDRO: The adversary optimizes compute utility. Under a fixed global budget (dashed line), it reallocates rollouts (orange bars) from solved tasks (bin 0) to high-variance tasks, scaling exploration with difficulty. Note: Bars represent rollout count per prompt (policy intensity).
L115: ## 1 Introduction
L116: cite92†Image: Refer to caption Figure 2: Conceptual Illustration: Static Uniformity vs. Multi-Adversary GDRO (Dynamic). (Left) Standard GRPO samples prompts uniformly ($q=1/B$) and assigns a fixed number of rollouts (schematically $N=16$), causing it to overfit easy tasks while under-exploring the frontier. (Right) Our framework employs an Online Difficulty Classifier to dynamically partition prompts based on real-time pass@k.
L117: It introduces two independent adversarial feedback loops (not coupled): (1) Prompt-GDRO (Data Distributor) uses an EMA-debiased scorer to shift the sampling distribution toward hard bins, creating a “traveling wave” of difficulty; (2) Rollout-GDRO (Resource Allocator) uses a shadow price $\mu$ to solve a constrained optimization problem, allocating discrete rollout arms ($n_{\min}\dots n_{\max}$) to maximize gradient variance reduction on high-uncertainty tasks.
L118: The capabilities of Large Language Models (LLMs) in complex reasoning are increasingly shaped not only by architectural scaling, but by the design of post-training objectives and alignment pipelines. Reinforcement Learning (RL), particularly methods like Proximal Policy Optimization (PPO) (cite93†Schulman et al., 2017 ) and Group Relative Policy Optimization (GRPO) (cite94†Shao et al., 2024 ), has emerged as a standard approach for aligning models with rigorous logical constraints.
L119: By optimizing for sparse verifiable rewards or process-based supervision, these methods have enabled significant breakthroughs in mathematical problem solving (cite95†Wang et al., 2024b ) and code generation.
L120: At a high level, our perspective is that reasoning post-training exposes two distinct sources of non-uniformity: (i) which prompts remain unsolved as the model improves (a shifting difficulty landscape), and (ii) how much exploration different prompts require to yield low-variance learning signals. Standard pipelines treat both knobs as static—uniform prompt sampling and fixed rollouts—which we argue is mismatched to the heavy-tailed structure of reasoning.
L121: Recent discussions in the broader ML community further motivate moving beyond uniformity from a data value perspective. Finzi et al. (cite96†Finzi et al., 2026 ) propose epiplexity—a notion of information that aims to quantify the structural content that a computationally bounded learner can extract from data (distinct from time-bounded entropy/noise).
L122: From this viewpoint, the “value” of a prompt is not determined by its frequency, but by whether it still contains learnable structure for the current policy under a fixed compute budget. This perspective is aligned with our Prompt-GDRO mechanism: by steering sampling toward the evolving reasoning frontier, we concentrate updates on prompts that remain high-value for learning, rather than repeatedly training on already-solved, low-value examples.
L123: Concurrently, empirical analyses of RL with verifiable rewards suggest that learning progress can be dominated by a small fraction of high-entropy “decision” points, challenging the implicit assumption that uniform averaging over all tokens/prompts is the most compute-efficient choice (cite97†Wang et al., 2025 ).
L124: Related work on “thinking” and the accuracy–compute Pareto frontier emphasizes that additional computation is most beneficial when applied selectively, and can be inefficient when applied uniformly across instances (cite98†Madaan et al., 2025 ). Taken together, these perspectives echo a community intuition that both data selection and compute allocation should be adaptive (cite99†Finzi, 2026 )—precisely the two control knobs instantiated by our Prompt-GDRO and Rollout-GDRO adversaries.
L125: However, prevalent RL pipelines rely on a fundamental assumption of static uniformity: they sample prompts uniformly from the training distribution and allocate a fixed computational budget (number of rollouts) to every prompt. We argue that this rigidity creates structural inefficiencies. As formalized in our analysis (Section cite20†4 ), reasoning datasets are inherently heterogeneous, composed of disjoint sub-domains (e.g., elementary algebra vs.
L126: Olympiad number theory) with vastly different difficulty profiles. Under uniform sampling, optimization is dominated by the most frequent, often easier patterns, so learning signal concentrates on the “easy core” while errors persist in a long, difficult tail.
L127: A long line of supervised learning work has addressed this asymmetry by making training explicitly difficulty-aware—from curriculum and self-paced learning that schedule examples from easy to hard (cite100†Bengio et al., 2009 ; cite101†Kumar et al., 2010 ), to boosting and hard-example mining that upweight misclassified or high-loss instances (cite102†Freund and Schapire, 1997 ; cite103†Shrivastava et al., 2016 ), and focal losses that downweight well-classified examples (cite104†Lin et al., 2017 ).
L128: This motivates viewing robustness through difficulty-defined groups and optimizing worst-bin performance in the spirit of GDRO (cite105†Sagawa et al., 2020 ). Furthermore, the value of computational exploration is non-uniform. In reasoning tasks, “solved” prompts yield low-variance gradients, while high-entropy “frontier” prompts require massive exploration to reduce gradient variance (cite106†Setlur et al., 2025 ).
L129: A static budget allocation fails to capture this dynamic, wasting resources on redundant verification while under-exploring critical failure modes.
L130: To address these limitations, we propose a Multi-Adversary Group Distributionally Robust Optimization (GDRO) framework. Motivated by the biological hypothesis that intelligent systems distinguish between a core representation learning module and a specialized “steering subsystem” that optimizes cost functions (cite107†Marblestone et al., 2016 ), we implement a dynamic, data-agnostic grouping mechanism.
L131: Specifically, we replace static uniformity with an Online Difficulty Classifier that partitions data based on real-time empirical error rates (pass@k), effectively allowing the optimization process to “steer” itself. We then formulate post-training as a zero-sum game and instantiate two complementary adversaries via the GDRO-EXP3P algorithm (cite108†Soma et al., 2022 ).
L132: Importantly, these adversaries are designed as independent modules: Prompt-GDRO plays a GDRO reweighting game against the learner, while Rollout-GDRO plays a separate constrained compute-allocation game. In this work we analyze and evaluate the two games in isolation (no coupling); jointly coupling both adversaries into a single multi-time-scale system is left to future work.
L133: Our contributions are summarized as follows:
L134: 
L135:   1. 1.
L136: Prompt-GDRO (A Data Adversary): We employ an adversarial reweighting rule that targets the intensive difficulty margin (mean loss) instead of uniform sampling. We introduce an EMA-Debiased scoring rule to prevent the adversary from succumbing to frequency bias, ensuring that rare, high-difficulty groups are upweighted effectively. This acts as a regularizer against over-optimizing the easy core, improving worst-bin robustness as the difficulty frontier shifts.
L137: Theory: In Section cite20†4 (proofs in Appendix B), we show that exponential-weights Prompt-GDRO corresponds to optimizing an entropy-regularized GDRO surrogate (a log-sum-exp “soft worst-group” objective) and admits a no-regret game interpretation.
L138:   2. 2.
L139: Rollout-GDRO (A Compute Adversary): We challenge the convention of fixed rollout budgets (e.g., $n=4$). We formulate rollout allocation as a constrained resource allocation game where a second adversary dynamically assigns rollout counts to maximize gradient variance reduction on hard tasks, subject to a global mean-rollout compute constraint. This enables the model to efficiently explore the solution space of complex problems without increasing the total training budget.
L140: Theory: In Section cite20†4 (proofs in Appendix B), we derive a variance proxy for GRPO rollouts and show that the variance-optimal compute-neutral allocation obeys a square-root law, motivating the shadow-price controller used by Rollout-GDRO.
L141:   3. 3.
L142: 
L143: Empirical results. On the DAPO 14.1k reasoning dataset with Qwen3-Base models (1.7B/4B/8B), Prompt-GDRO improves pass@8 by +9.74%, +13.13%, and +8.96%, and Rollout-GDRO by +10.64%, +10.59%, and +9.20% over GRPO. Qualitative analyses reveal an emergent curriculum that shifts sampling weight and rollout budget toward the evolving reasoning frontier.
L144: ## 2 Preliminaries
L145: ### 2.1 Reinforcement Learning for Reasoning
L146: 
L147: We formalize post-training for reasoning as Reinforcement Learning (RL) over an autoregressive language policy. Let $x\sim\mathcal{D}$ denote a prompt and let $y=(y_{1},\dots,y_{L})$ denote a response sampled from a policy $\pi_{\theta}(\cdot\mid x)$ parameterized by $\theta$. The conditional sequence probability factorizes as
L148: 
L149:  | $$\pi_{\theta}(y\mid x)\;=\;\prod_{t=1}^{L}\pi_{\theta}\!\left(y_{t}\mid x,y_{<t}\right).$$  |  | (1)
L150: The RL objective is to maximize expected reward
L151: 
L152:  | $$J(\theta)\;=\;\mathbb{E}_{x\sim\mathcal{D},\,y\sim\pi_{\theta}(\cdot\mid x)}\!\left[r(x,y)\right],$$  |  | (2)
L153: 
L154: where $r(x,y)$ is a task-dependent, generally non-differentiable reward. In mathematical reasoning, $r(x,y)$ is typically sparse (e.g., binary correctness) or semi-sparse (e.g., verifier-based signals).
L155: ### 2.2 Group-Relative Policy Optimization (GRPO)
L156: 
L157: Group-Relative Policy Optimization (GRPO) (cite94†Shao et al., 2024 ) is a computationally efficient alternative to Proximal Policy Optimization (PPO) (cite93†Schulman et al., 2017 ). GRPO eliminates a learned value critic by constructing a baseline from a within-prompt group of rollouts.
L158: ###### Remark 2.1 (Two notions of “group”).
L159: 
L160: Throughout the paper, the term “group” can refer to two different objects: (i) a GRPO rollout group (multiple rollouts for a fixed prompt), and (ii) a GDRO group/bin (a subset of prompts induced by a grouping rule, e.g., an online difficulty bin). We explicitly index GRPO rollouts by $(i,j)$ and GDRO bins by $b\in\{1,\dots,B\}$.
L161: ###### Remark 2.2 (Notation: $n$ vs. $k$).
L162: 
L163: We use $n$ for the GRPO rollout-group size (train-time rollouts per prompt), and $k$ for “best-of-$k$” statistics such as pass@k and mean@k. In our experiments, we use $n=4$ and $k=8$.
L164: Group sampling and advantage estimation. For each prompt $x_{i}$, we sample $n$ responses $\{y_{i,j}\}_{j=1}^{n}$ from a behavior policy $\pi_{\theta_{\text{old}}}$ (the policy used to generate rollouts). Each response receives a scalar reward $r_{i,j}\triangleq r(x_{i},y_{i,j})$. GRPO computes a group-relative advantage by standardizing rewards within the rollout group:
L165: 
L166:  | $$A_{i,j}\;=\;\frac{r_{i,j}-\mu_{i}}{\sigma_{i}+\varepsilon},$$  |  | (3)
L167: where $\mu_{i}\triangleq\frac{1}{n}\sum_{j=1}^{n}r_{i,j}$, $\sigma_{i}\triangleq\sqrt{\frac{1}{n}\sum_{j=1}^{n}(r_{i,j}-\mu_{i})^{2}}$, and $\varepsilon>0$ is a small constant for numerical stability. The scalar advantage $A_{i,j}$ is applied token-wise to all tokens in $y_{i,j}$ in the surrogate objective below.
L168: 
L169: The clipped surrogate objective. Let
L170:  | $$\rho_{i,j,t}(\theta)\;\triangleq\;\frac{\pi_{\theta}\!\left(y_{i,j,t}\mid x_{i},y_{i,j,<t}\right)}{\pi_{\theta_{\text{old}}}\!\left(y_{i,j,t}\mid x_{i},y_{i,j,<t}\right)}$$  |  | (4)
L171: 
L172: denote the token-level importance ratio. The GRPO/PPO-style clipped surrogate for response $y_{i,j}$ is
L173:  | $$\mathcal{J}^{\text{CLIP}}_{i,j}(\theta)\;=\;\frac{1}{L_{i,j}}\sum_{t=1}^{L_{i,j}}\min\!\Big(\rho_{i,j,t}(\theta)\,A_{i,j},\;\text{clip}\!\big(\rho_{i,j,t}(\theta),\,1-\epsilon,\,1+\epsilon\big)\,A_{i,j}\Big),$$  |  | (5)
L174: 
L175: where $\epsilon>0$ is the PPO clipping parameter.
L176: 
L177: Observable loss signal. For our robust optimization controllers, we require a scalar “loss-like” signal per generated response. We define the per-response loss as the negative KL-regularized surrogate:
L178:  | $$\ell_{i,j}(\theta)\;=\;-\mathcal{J}^{\text{CLIP}}_{i,j}(\theta)\;+\;\beta_{\text{KL}}\,D_{\text{KL}}\!\left(\pi_{\theta}(\cdot\mid x_{i})\parallel\pi_{\text{ref}}(\cdot\mid x_{i})\right),$$  |  | (6)
L179: where $\beta_{\text{KL}}>0$ controls the KL penalty to a fixed reference policy $\pi_{\text{ref}}$. In our experiments we operate in a zero-SFT setting, so $\pi_{\text{ref}}$ is simply the initial base checkpoint (i.e., the same Qwen3-{1.7B,4B,8B}-Base model we start RL from) and is held frozen during training.
L180: In practice, $D_{\text{KL}}(\pi_{\theta}(\cdot\mid x_{i})\,\|\,\pi_{\text{ref}}(\cdot\mid x_{i}))$ is evaluated on the sampled responses using token-level log-probabilities under $\pi_{\theta}$ and $\pi_{\text{ref}}$. Finally, we define the prompt-level loss as the mean over rollouts:
L181:  | $$\ell(x_{i};\theta)\;\triangleq\;\frac{1}{n}\sum_{j=1}^{n}\ell_{i,j}(\theta).$$  |  | (7)
L182: 
L183: This prompt-level signal will be aggregated by bins and fed to the GDRO adversaries.
L184: ### 2.3 Group Distributionally Robust Optimization
L185: Standard Empirical Risk Minimization (ERM) minimizes average loss under the empirical mixture, which can be dominated by high-frequency and/or easy instances.
L186: A long line of supervised learning work addresses this imbalance by making training explicitly difficulty-aware—from curriculum and self-paced learning that schedule examples from easy to hard (cite100†Bengio et al., 2009 ; cite101†Kumar et al., 2010 ), to boosting and hard-example mining that upweight misclassified or high-loss instances (cite102†Freund and Schapire, 1997 ; cite103†Shrivastava et al., 2016 ), and focal losses that downweight well-classified examples (cite104†Lin et al., 2017 ).
L187: GDRO provides a complementary, principled objective: treat subpopulations (here, difficulty bins) as groups and optimize worst-group risk.
L188: We adopt Group Distributionally Robust Optimization (GDRO) (cite105†Sagawa et al., 2020 ). Assume prompts are partitioned into $B$ disjoint groups (domains) $\{\mathcal{D}_{1},\dots,\mathcal{D}_{B}\}$. Let
L189: 
L190:  | $$L_{b}(\theta)\;\triangleq\;\mathbb{E}_{x\sim\mathcal{D}_{b}}\!\left[\ell(x;\theta)\right]$$  |  | (8)
L191: 
L192: denote the expected prompt-level loss for group $b$. GDRO optimizes worst-group performance by solving
L193: 
L194:  | $$\min_{\theta}\;\max_{q\in\Delta_{B}}\;\sum_{b=1}^{B}q_{b}\,L_{b}(\theta),$$  |  | (9)
L195: where $\Delta_{B}$ is the probability simplex. Following cite108†Soma et al. (2022) , (cite109†9 ) admits a zero-sum game interpretation between a learner ($\theta$) and an adversary ($q$) and can be optimized via no-regret online learning. Our method instantiates this perspective with multiple adversarial “levers” on top of the GRPO loss signal in (cite110†6 ).
L196: ## 3 Method
L197: 
L198: Standard instruction tuning paradigms are characterized by static uniformity: a uniform distribution over prompts and a fixed computational budget per prompt. We argue that this rigidity creates structural inefficiencies in learning, particularly for heterogeneous reasoning tasks where difficulty varies significantly across domains.
L199: To address this, we propose a Multi-Adversary Framework that decomposes the training process into dynamic distributional levers. Our method operates in a shared environment where prompts are dynamically categorized by difficulty (Section cite12†3.1 ), serving as the basis for distinct adversarial processes:
L200: 
L201:   1. 1.
L202: 
L203: Adversarial Sampler ($q_{\text{prompt}}$): Optimizes the probability of sampling prompts from different difficulty bins to expose model weaknesses (Section cite15†3.2 ).
L204: 
L205:   2. 2.
L206: Adversarial Budgeter ($n_{\text{rollout}}$): Optimizes the allocation of rollout counts $n_{b}$ to different bins to maximize gradient information under a global compute constraint (Section cite17†3.3 ).
L207: ### 3.1 Dynamic Grouping via Online Pass@k
L208: 
L209: A critical prerequisite for GDRO is the definition of domains (groups) $\mathcal{D}_{b}$. Relying on static dataset metadata (e.g., “Level 5”) is suboptimal because theoretical difficulty often diverges from empirical model capability. Furthermore, reliance on explicit labels limits applicability to datasets with rich metadata.
L210: #### 3.1.1 Data-Agnostic Difficulty Estimation
L211: Our method removes the dependency on static annotations by defining groups solely through empirical interaction. We employ an Online Difficulty Classifier to construct dynamic groups based on the model’s real-time performance. By utilizing the policy’s own error rate as the grouping criterion, the framework becomes data-agnostic.
L212: Whether the underlying data is math, code, or creative writing, the “difficulty” is emergent, allowing the pipeline to automatically discover and upweight the subsets of data that are currently challenging for the policy.
L213: #### 3.1.2 Implementation Details
L214: We assign each prompt a unique identifier (UID) and track an online pass@$k$ statistic, where $k$ is a fixed hyperparameter that defines the difficulty scale (e.g., $k=8$ in our experiments). At training step $t$, we sample $k$ rollouts $\{y_{j}\}_{j=1}^{k}$ for prompt $x$ and define an any-of-$k$ correctness indicator $c_{t}(x)\triangleq\mathbb{I}\{\exists j\in\{1,\dots,k\}:r(x,y_{j})=1\}$, which equals $1$ iff at least one of the $k$ rollouts is correct.
L215: We then maintain a moving estimate of pass@$k$ using a sliding window of length $H$,
L216:  | $$\widehat{\mathrm{pass@}k}_{t}(x)\;\triangleq\;\frac{1}{H}\sum_{s=t-H+1}^{t}c_{s}(x),$$  |  | (10)
L217: 
L218: with the convention that the sum is taken over available history for newly seen UIDs.
L219: 
L220: We map prompts to discrete accuracy bins (e.g., accbin_0 for $[0,0.1)$, accbin_1 for $[0.1,0.2)$, etc.). Let $0=a_{0}<a_{1}<\cdots<a_{B}=1$ denote bin edges. This induces a partition of the input space $\mathcal{X}=\bigcup_{b=1}^{B}\mathcal{D}_{b}$, where
L221:  | $$\mathcal{D}_{b}\;\triangleq\;\big\{x\in\mathcal{X}:\widehat{\mathrm{pass@}k}_{t}(x)\in[a_{b-1},a_{b})\big\}.$$  |  | (11)
L222: 
L223: We define the (time-varying) grouping map $g_{t}:\mathcal{X}\to\{1,\dots,B\}$ by $g_{t}(x)=b$ if $x\in\mathcal{D}_{b}$.
L224: ###### Remark 3.1 (Bins as dynamic groups).
L225: 
L226: We use bin and group interchangeably: the bin index $b$ corresponds to the GDRO group $\mathcal{D}_{b}$ induced by the online pass@$k$ estimate (cite111†10 ). Within one training step, we treat $g_{t}$ as fixed; across steps, the partition evolves as the policy improves.
L227: To ensure stability in the optimization landscape, we implement hysteresis: a prompt is only reassigned to a new bin if its moving average accuracy crosses the bin boundary by a margin $\delta$. This prevents prompts from oscillating between groups due to stochastic noise, ensuring that the adversaries target stable difficulty tiers rather than transient fluctuations.
L228: ### 3.2 Adversarial Prompt Reweighting (Prompt-GDRO)
L229: 
L230: The goal of the prompt reweighting adversary is to construct a distribution $q_{t}\in\Delta_{B}$ over the dynamic groups defined above. The adversary seeks to maximize the expected loss, thereby forcing the policy to improve on the “Pareto frontier” of difficulty. In summary, we realize Prompt-GDRO by bin-wise reweighting of GRPO updates (via per-sample weights applied to advantages), rather than by physically resampling prompts.
L231: #### 3.2.1 EMA-Debiased EXP3P Optimization


## Original response: stdnext3eval0

Group Distributionally Robust Optimization-Driven Reinforcement Learning for LLM Reasoning (https://arxiv.org/html/2601.19280v1)
citeturn28413view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28405view1","lineno":250}); Total lines: 1191
L214: We assign each prompt a unique identifier (UID) and track an online pass@$k$ statistic, where $k$ is a fixed hyperparameter that defines the difficulty scale (e.g., $k=8$ in our experiments). At training step $t$, we sample $k$ rollouts $\{y_{j}\}_{j=1}^{k}$ for prompt $x$ and define an any-of-$k$ correctness indicator $c_{t}(x)\triangleq\mathbb{I}\{\exists j\in\{1,\dots,k\}:r(x,y_{j})=1\}$, which equals $1$ iff at least one of the $k$ rollouts is correct.
L215: We then maintain a moving estimate of pass@$k$ using a sliding window of length $H$,
L216:  | $$\widehat{\mathrm{pass@}k}_{t}(x)\;\triangleq\;\frac{1}{H}\sum_{s=t-H+1}^{t}c_{s}(x),$$  |  | (10)
L217: 
L218: with the convention that the sum is taken over available history for newly seen UIDs.
L219: 
L220: We map prompts to discrete accuracy bins (e.g., accbin_0 for $[0,0.1)$, accbin_1 for $[0.1,0.2)$, etc.). Let $0=a_{0}<a_{1}<\cdots<a_{B}=1$ denote bin edges. This induces a partition of the input space $\mathcal{X}=\bigcup_{b=1}^{B}\mathcal{D}_{b}$, where
L221:  | $$\mathcal{D}_{b}\;\triangleq\;\big\{x\in\mathcal{X}:\widehat{\mathrm{pass@}k}_{t}(x)\in[a_{b-1},a_{b})\big\}.$$  |  | (11)
L222: 
L223: We define the (time-varying) grouping map $g_{t}:\mathcal{X}\to\{1,\dots,B\}$ by $g_{t}(x)=b$ if $x\in\mathcal{D}_{b}$.
L224: ###### Remark 3.1 (Bins as dynamic groups).
L225: 
L226: We use bin and group interchangeably: the bin index $b$ corresponds to the GDRO group $\mathcal{D}_{b}$ induced by the online pass@$k$ estimate (cite111†10 ). Within one training step, we treat $g_{t}$ as fixed; across steps, the partition evolves as the policy improves.
L227: To ensure stability in the optimization landscape, we implement hysteresis: a prompt is only reassigned to a new bin if its moving average accuracy crosses the bin boundary by a margin $\delta$. This prevents prompts from oscillating between groups due to stochastic noise, ensuring that the adversaries target stable difficulty tiers rather than transient fluctuations.
L228: ### 3.2 Adversarial Prompt Reweighting (Prompt-GDRO)
L229: 
L230: The goal of the prompt reweighting adversary is to construct a distribution $q_{t}\in\Delta_{B}$ over the dynamic groups defined above. The adversary seeks to maximize the expected loss, thereby forcing the policy to improve on the “Pareto frontier” of difficulty. In summary, we realize Prompt-GDRO by bin-wise reweighting of GRPO updates (via per-sample weights applied to advantages), rather than by physically resampling prompts.
L231: #### 3.2.1 EMA-Debiased EXP3P Optimization
L232: We solve the inner maximization problem using the GDRO-EXP3P algorithm (cite108†Soma et al., 2022 ). Intuitively, the adversary maintains a distribution $q_{t}\in\Delta_{B}$ over bins and increases pressure on bins with high recent loss. A key subtlety is frequency bias: if the adversary were to optimize cumulative (extensive) loss, then naturally frequent bins would dominate the score even if they are easy.
L233: Our design instead targets the intensive difficulty margin (mean loss), which is the quantity that indicates how much a typical prompt in the bin is currently challenging.
L234: To correct this, we propose an EMA-Debiased scoring rule. For each bin $b\in\{1,\dots,B\}$, we maintain a difficulty score $S_{t}(b)$ updated via an Exponential Moving Average (EMA) with decay $\beta$:
L235: 
L236:  | $$S_{t}(b)\leftarrow(1-\beta)S_{t-1}(b)+\beta\cdot\bar{\ell}_{t}(b),$$  |  | (12)
L237: where $\bar{\ell}_{t}(b)$ is the empirical mean prompt-level loss for bin $b$ at step $t$. Let $\mathcal{B}_{t}$ be the batch of prompts at step $t$, and let $\mathcal{B}_{b,t}=\{x\in\mathcal{B}_{t}\mid g_{t}(x)=b\}$ denote the subset in bin $b$. We compute
L238: 
L239:  | $$\bar{\ell}_{t}(b)=\frac{1}{|\mathcal{B}_{b,t}|}\sum_{x\in\mathcal{B}_{b,t}}\ell(x;\theta).$$  |  | (13)
L240: Let $\hat{q}_{t}(b)\triangleq|\mathcal{B}_{b,t}|/|\mathcal{B}_{t}|$ denote the (realized) prompt share of bin $b$ in the current batch. In practice we optionally normalize the update by $\hat{q}_{t}(b)$ (with a small floor) to ensure that rare but consistently high-loss bins can compete with common bins in the EXP3P update.
L241: 
L242: Crucially, $S_{t}(b)$ tracks intensive difficulty (mean loss) rather than extensive loss, which decouples the adversarial signal from static dataset frequency.
L243: The adversarial (unnormalized) bin weights $\omega_{t}(b)$ are derived by exponentiating these scores:
L244: 
L245:  | $$\omega_{t}(b)=\exp\left(\eta_{q}\cdot\text{clip}(S_{t}(b),-C,C)\right),$$  |  | (14)
L246: 
L247: where $\eta_{q}$ is the learning rate (sharpness). The final sampling probability includes a uniform mixing term $\gamma$ to guarantee exploration:
L248: 
L249:  | $$q_{t}(b)=(1-\gamma)\frac{\omega_{t}(b)}{\sum_{j=1}^{B}\omega_{t}(j)}+\frac{\gamma}{B}.$$  |  | (15)
L250: Rather than physically resampling the dataset, we realize $q_{t}$ by reweighting the GRPO gradient contribution of each prompt. Concretely, for a prompt $x_{i}$ we scale its rollout advantages as
L251: 
L252:  | $$A_{i,j}\leftarrow A_{i,j}\cdot\min\{\omega_{t}(g_{t}(x_{i})),\,\omega_{\max}\},$$  |  | (16)
L253: where $\omega_{\max}$ is a cap for numerical stability. Note that using the unnormalized score $\omega_{t}(b)$ (rather than the normalized probability $q_{t}(b)$) preserves the same relative weighting across bins; the omitted normalization constant is a common scalar factor that is absorbed into the effective step size of the GRPO update.
L254: Intuitively, this increases the effective step size on bins the adversary considers difficult, which is equivalent (in expectation) to optimizing the GDRO objective with adversarial weights.
L255: ### 3.3 Adversarial Rollout Budgeting (Rollout-GDRO)
L256: 
L257: In standard GRPO, the number of rollouts $n$ is fixed (e.g., $n=4$). However, “easy” prompts yield diminishing returns from extra rollouts, while “hard” prompts require more exploration to reduce gradient variance and to stabilize group statistics (e.g., the mean and standard deviation in (cite112†3 )). We formulate the choice of rollout counts as a second GDRO-style resource allocation problem over the same dynamic bins induced by $g_{t}$.
L258: #### 3.3.1 Constrained Maximization Formulation
L259: 
L260: We treat the number of rollouts for bin $b$ as a discrete variable $n_{b}\in\{n_{\min},\dots,n_{\max}\}$. Let $\hat{q}_{t}(b)$ denote the realized bin share in the prompt batch at step $t$.
L261: Bin-level utility from $n_{b}$ rollouts. Recall from Section cite7†2 that GRPO provides a per-response loss signal $\ell_{i,j}(\theta)$ (Eq. (cite110†6 )) and aggregates it into a prompt-level loss by averaging over $n$ rollouts, $\ell(x_{i};\theta)=\frac{1}{n}\sum_{j=1}^{n}\ell_{i,j}(\theta)$. When using a bin-specific rollout count $n_{b}$, we compute the same quantity with $n_{b}$ samples:
L262: 
L263:  | $$\ell(x_{i};\theta,n_{b})\;\triangleq\;\frac{1}{n_{b}}\sum_{j=1}^{n_{b}}\ell_{i,j}(\theta).$$  |  | (17)
L264: Given the current batch $\mathcal{B}_{t}$ and the induced bin partition $\{\mathcal{B}_{b,t}\}_{b=1}^{B}$, we define the empirical bin-level utility (negative loss) under $n_{b}$ rollouts as
L265: 
L266:  | $$\hat{J}_{b}(\theta;n_{b})\;\triangleq\;-\frac{1}{|\mathcal{B}_{b,t}|}\sum_{x_{i}\in\mathcal{B}_{b,t}}\ell(x_{i};\theta,n_{b}),$$  |  | (18)
L267: 
L268: where the hat emphasizes that this is a finite-sample estimate computed on the current batch.
L269: Mean-rollout constraint. The budgeter chooses $\{n_{b}\}$ to concentrate rollouts on bins where they are most valuable, subject to a strict global budget on the mean rollouts per prompt $\bar{n}$:
L270: 
L271:  | $$\max_{\{n_{b}\}}\sum_{b=1}^{B}\hat{q}_{t}(b)\,\hat{J}_{b}(\theta;n_{b})\quad\text{s.t.}\quad\sum_{b=1}^{B}\hat{q}_{t}(b)\,n_{b}=\bar{n}.$$  |  | (19)
L272: This formulation incentivizes allocating more compute to bins where additional rollouts improve gradient quality the most: more rollouts both (i) reduce Monte Carlo noise and (ii) increase the number of informative samples contributing to the update. The global budget $\bar{n}$ (typically set to the baseline rollout count, e.g., $\bar{n}=4$) ensures the total computational cost matches the uniform baseline.
L273: #### 3.3.2 Dual Ascent Solver
L274: 
L275: We solve the constrained maximization above via a Lagrangian relaxation with a single multiplier $\mu$ for the mean-rollout constraint. For a candidate rollout count $n$ in bin $b$, we define the corresponding penalized bandit loss as:
L276: 
L277:  | $$L_{b}(n)\;=\;-\hat{J}_{b}(\theta;n)+\mu\,n.$$  |  | (20)
L278: We maintain a separate EXP3P instance (cite108†Soma et al., 2022 ) where the “arms” are the discrete integers in $[n_{\min},n_{\max}]$. At each step, we select the configuration $\{n_{b}\}_{b=1}^{B}$ that maximizes the joint probability while strictly satisfying the global budget equality constraint $\sum_{b=1}^{B}\hat{q}_{t}(b)n_{b}=\bar{n}$. This exact matching is implemented via a dynamic programming selection step over the active bins.
L279: After the batch is processed and the actual rollout consumption $\hat{n}_{\text{realized}}$ is observed, the dual variable $\mu$ is updated:
L280: 
L281:  | $$\mu\leftarrow\mu+\alpha_{\mu}(\hat{n}_{\text{realized}}-\bar{n}),$$  |  | (21)
L282: 
L283: where $\alpha_{\mu}$ is the dual learning rate. This mechanism ensures the method remains compute-neutral compared to the baseline, dynamically shifting resources from easy to hard groups based on the shadow price of compute $\mu$.
L284: ## 4 Analysis
L285: 
L286: This section provides a first-principles interpretation of why static uniformity can be structurally inefficient in RL post-training for reasoning, and how our two controllers implement targeted robustness improvements. We intentionally avoid re-defining Prompt-GDRO and Rollout-GDRO (Section cite11†3 ); here we connect the method to robust objectives and state the core theoretical messages. Detailed derivations and proofs are deferred to Appendix cite71†B .
L287: ### 4.1 Motivation: Why uniformity can fail in reasoning post-training
L288: Reasoning datasets are heterogeneous: prompts belong to latent sub-domains (topics, formats, reasoning styles) with widely varying difficulty. Uniform sampling and a fixed rollout budget implicitly assume that (a) all prompts are equally informative to train on and (b) the same amount of exploration is warranted everywhere. Both assumptions are brittle in practice.
L289: In particular, once a large fraction of prompts become “nearly solved,” their rollouts yield low-variance gradients and diminishing marginal learning signal, while the remaining frontier prompts continue to exhibit high uncertainty. Under uniform sampling, optimization is dominated by the most frequent, often easier patterns, so learning signal concentrates on the “easy core” while errors persist in a long, difficult tail (cite100†Bengio et al., 2009 ; cite105†Sagawa et al., 2020 ).
L290: ##### GDRO lens.
L291: We use GDRO (Section cite10†2.3 , Eq. (cite109†9 )) as a compact way to reason about worst-bin robustness. In our setting the “groups” are the online difficulty bins induced by $g_{t}$ (Section cite12†3.1 ); within a training step we treat $g_{t}$ as fixed and interpret the group losses $L_{b}(\theta)$ in Eq. (cite109†9 ) as bin-conditional GRPO prompt losses.
L292: Under this lens, Prompt-GDRO is an online approximation to the inner adversary over $q$, while Rollout-GDRO is a second adversary that reallocates rollout compute across the same bins to improve the signal-to-noise ratio of the update under a compute-neutral budget.
L293: ### 4.2 Adversary I (Prompt-GDRO): Robustness via EMA-debiased difficulty pressure
L294: ##### From GDRO to a bandit adversary.
L295: If bins were fixed and losses were observed noiselessly, the inner maximization in Eq. (cite109†9 ) could be solved by concentrating $q$ on the current worst-loss bin. In post-training, however, (i) losses are stochastic Monte Carlo estimates, and (ii) the grouping $g_{t}$ is online and non-stationary as the model improves. Following cite108†Soma et al. (2022) , we view the adversary as an online learner that updates a distribution over bins using no-regret bandit-style updates.
L296: ##### Why “EMA-debiased”? Frequency bias vs. intensive difficulty.
L297: Methodologically, Prompt-GDRO is fully specified in Section cite15†3.2 . The key point for the analysis is that the adversary is driven by an intensive statistic (mean prompt loss per bin) rather than an extensive cumulative loss, and that this statistic is smoothed over time.
L298: Concretely, Prompt-GDRO maintains an EMA difficulty score $S_{t}(b)$ (Eq. (cite113†12 )), exponentiates the (clipped) scores to obtain unnormalized weights $\omega_{t}(b)$ (Eq. (cite114†14 )), and forms the adversarial bin distribution $q_{t}$ with an exploration mixture (Eq. (cite115†15 )). Optionally normalizing by the realized bin share $\hat{q}_{t}(b)$ mitigates frequency bias so that persistently hard but rare bins can remain competitive.
L299: ##### How $q_{t}$ acts on GRPO updates (intuition).
L300: 
L301: Although $q_{t}$ can be interpreted as a sampling distribution over bins, we realize it in a compute-neutral way by reweighting gradient contributions (Section cite15†3.2 ). Scaling a prompt’s rollout advantages by a bin-dependent multiplier increases its effective learning rate, which implements the same “pay more attention to hard bins” principle as Eq. (cite109†9 ).
L302: #### 4.2.1 Entropic GDRO view: log-sum-exp surrogate and softmax best response
L303: 
L304: Prompt-GDRO implements the adversary via exponential weights (Eqs. (cite114†14 )–(cite115†15 )), which corresponds to entropic mirror ascent on the simplex. A key consequence is that the hard inner maximum in Eq. (cite109†9 ) is implicitly replaced by an entropy-regularized one, yielding a smooth “soft worst-group” objective.
L305: To keep notation uncluttered, for the remainder of this subsection we treat $g_{t}$ as fixed within a step and omit the subscript $t$.
L306: ###### Lemma 4.1 (Entropic GDRO surrogate and softmax best response).
L307: 
L308: For any $\eta>0$, define the entropy-regularized inner problem
L309: 
L310:  | $$\mathcal{R}_{\eta}(\theta)\;\triangleq\;\max_{q\in\Delta_{B}}\left\{\sum_{b=1}^{B}q(b)L_{b}(\theta)+\frac{1}{\eta}H(q)\right\},\qquad H(q)\triangleq-\sum_{b=1}^{B}q(b)\log q(b).$$  |  | (22)
L311: 
L312: Then
L313: 
L314:  | $$\mathcal{R}_{\eta}(\theta)=\frac{1}{\eta}\log\!\left(\sum_{b=1}^{B}e^{\eta L_{b}(\theta)}\right),$$  |  | (23)
L315: 
L316: and the (unique) maximizer is the softmax distribution
L317:  | $$q_{\eta}(b;\theta)\;=\;\frac{\exp(\eta L_{b}(\theta))}{\sum_{j=1}^{B}\exp(\eta L_{j}(\theta))}.$$  |  | (24)
L318: 
L319: Moreover, $\mathcal{R}_{\eta}$ approximates the hard worst-group loss up to $\log B/\eta$:
L320: 
L321:  | $$\max_{b\in[B]}L_{b}(\theta)\;\leq\;\mathcal{R}_{\eta}(\theta)\;\leq\;\max_{b\in[B]}L_{b}(\theta)+\frac{\log B}{\eta}.$$  |  | (25)
L322: 
L323: Proof. Appendix cite73†B.1.1 .
L324: ##### Gradient interpretation.
L325: 
L326: Differentiating Eq. (cite116†23 ) yields a weighted mixture of group gradients,
L327: 
L328:  | $$\nabla_{\theta}\mathcal{R}_{\eta}(\theta)=\sum_{b=1}^{B}q_{\eta}(b;\theta)\,\nabla_{\theta}L_{b}(\theta),$$  |  | (26)
L329: 
L330: so applying larger weights to higher-loss bins can be read as taking a gradient step on a smooth approximation to the worst-group objective.
--------------------------------------------------------------------------------


## Original response: stdnext3eval0

Group Distributionally Robust Optimization-Driven Reinforcement Learning for LLM Reasoning (https://arxiv.org/html/2601.19280v1)
citeturn28413view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28405view1","lineno":510}); Total lines: 1191
L494: In contrast, our work keeps the underlying environment fixed and instead treats prompt difficulty and compute allocation as adversarially controlled quantities during LLM post-training. This yields a robustness lens that is closer to group robustness over tasks/prompts than to worst-case transition uncertainty.
L495: ### 6.4 Curriculum, Adaptive Compute, and Data Value
L496: Adaptive curricula and compute allocation are increasingly recognized as first-class components of reasoning systems. Curriculum-based post-training pipelines such as Light-R1 (cite158†Wen et al., 2025a ) explicitly stage data difficulty and objectives (SFT/DPO/RL) to elicit long-CoT behaviors.
L497: At inference time, scaling laws and compute-allocation policies highlight that difficult instances require more budget, but that naive increases in “thinking” can be inefficient or unstable (cite159†Snell et al., 2024 ; cite146†Ghosal et al., 2025 ). Recent work proposes learning policies to allocate test-time compute (cite106†Setlur et al., 2025 ) and explores search-based or tree-structured generation to improve exploration of the reasoning space (cite160†Xie et al., 2024 ; cite161†Hou et al., 2025 ).
L498: Our Rollout-GDRO can be viewed as moving this idea to training time: we allocate rollout budgets to groups to improve gradient estimator quality under a global constraint, akin to adaptive variance reduction (cite162†Rubinstein and Kroese, 2016 ).
L499: Recent work has also begun to articulate compute-optimal “RL scaling” workflows for LLM post-training by empirically studying how to allocate a fixed sampling budget across (i) the number of problems per batch, (ii) the number of parallel rollouts per problem (GRPO group size), and (iii) the number of sequential update steps.
L500: In particular, the IsoCompute Playbook reports that compute-optimal rollout parallelism can often be summarized by simple sigmoidal/logit fits as total sampling compute grows (cite163†Cheng et al., 2026 ). In contrast, our approach is more algorithmic: Prompt-GDRO and Rollout-GDRO adaptively reshape the effective prompt distribution and per-group compute online, without assuming a pre-fit scaling law.
L501: Concretely, we hold the mean sampling budget fixed and redistribute it across online-defined difficulty subgroups within each batch, rather than optimizing compute allocation across global axes such as problems-per-batch, rollouts-per-problem, or number of update steps. Relatedly, cite164†Qi et al. (2025) propose Budget Relative Policy Optimization (BRPO) to optimize anytime reasoning performance across varying token budgets, complementing our training-time allocation perspective.
L502: Finally, recent theoretical discussion emphasizes that the value of data depends on the learner’s computational constraints and even on data ordering. The notion of epiplexity formalizes this perspective and motivates principled data selection and dataset interventions (cite96†Finzi et al., 2026 ); see also community discussion (cite99†Finzi, 2026 ).
L503: Our work is exploratory in this broader direction: we study whether simple, online, adversarial control loops over prompt reweighting and compute allocation can serve as a practical “steering subsystem” for reasoning post-training, complementing concurrent efforts that analyze RLVR mechanisms (cite97†Wang et al., 2025 ; cite145†Wen et al., 2025b ), rethink thinking-token tradeoffs (cite98†Madaan et al., 2025 ), and diagnose instabilities such as looping (cite147†Pipis et al., 2025 ).
L504: ## 7 Limitations and Future Work
L505: ##### Bridge: from two adversaries to open questions.
L506: Our empirical results suggest that the two adversaries introduced in this work—Prompt-GDRO (adaptive prompt reweighting over online difficulty bins) and Rollout-GDRO (adaptive rollout allocation under a global compute budget)—capture complementary levers for improving reasoning post-training.
L507: Both adversaries are driven by the same online difficulty signal (stable binning via empirical pass@k), but intervene at different points in the pipeline: Prompt-GDRO shapes the data distribution presented to the learner, while Rollout-GDRO shapes the per-sample signal-to-noise ratio of policy-gradient updates by modulating rollout counts.
L508: This coupling is central to the “beyond uniform” thesis of our framework, yet our current study is necessarily exploratory and leaves several important questions unresolved.
L509: ##### Empirical scope and missing full-factorial ablations.
L510: This paper is intended as an exploratory report to the community: we demonstrate that distribution-shaping tools from GDRO-style thinking can be productively instantiated inside a modern reasoning post-training stack, but we do not claim to have exhaustively optimized the design space. In particular, we have not yet performed a full factorial ablation over all distribution-shaping components and their interactions (e.g., prompt selection/reweighting, compute allocation, and online binning choices).
L511: Concrete future work includes:
L512:   * •
L513: 
L514: Binning and classifier hyperparameters. We used a fixed binning scheme in most experiments; broader sweeps over the number of bins, smoothing horizons, and bin-stability heuristics are needed. In preliminary sweeps we often observed performance peaking around $\approx 6$ bins, but this is not yet a robust conclusion.
L515: 
L516:   * •
L517: Joint training with multiple adversaries. Most experiments isolate Prompt-GDRO or Rollout-GDRO; a systematic study of their joint behavior (and staged curricula) is still missing.
L518: 
L519:   * •
L520: 
L521: Rollout allocator design. We only explored a limited set of discrete rollout arms and budget schedules; future work should examine broader arm sets, alternative constrained optimizers, and adaptive rollout bounds.
L522: ##### RL scaling and compute-optimal post-training.
L523: Our experiments are conducted at a single (moderate) scale, and we do not yet understand how adversarial prompt reweighting and rollout budgeting interact with emerging “RL scaling” behavior as total post-training compute grows.
L524: Recent work (cite165†Liu et al., 2025b ; cite166†Liu et al., 2025a ; cite167†Khatri et al., 2025 ; cite163†Cheng et al., 2026 ) study compute-optimal allocation rules and scaling behavior for RL of LLMs (e.g., by fitting simple sigmoidal/logit trends for optimal rollouts-per-problem under larger budgets). A natural next step is to evaluate whether Prompt-GDRO and Rollout-GDRO shift these compute-optimal frontiers (or their saturation points) across larger compute budgets, model sizes, and prompt mixtures.
L525: ##### Adversarial game computation and systems overhead.
L526: A practical limitation of our approach is that it introduces additional online machinery beyond standard GRPO: (i) computing and maintaining a difficulty classifier (pass@k statistics, stable bin assignment), (ii) updating adversarial distributions (EXP3P-style weight updates), and (iii) (for Rollout-GDRO) enforcing compute constraints while selecting discrete rollout arms.
L527: As an illustration for trade-offs, we measure the driver-side advantage stage time (timing_s/adv, in sec/step) and find that for the Qwen3-4B runs (mean over the last 100 logged steps after warmup) GRPO requires 0.043 sec/step, Prompt-GDRO requires 0.355 sec/step, and Rollout-GDRO requires 0.446 sec/step. This overhead is distinct from our sampling-compute neutrality claims, which refer to the mean rollout budget.
L528: We find GDRO’s adversary/advantage-side bookkeeping can materially increase the driver-side advantage stage, and is one contributor to end-to-end slowdown. While each component is lightweight in isolation, their combination can create nontrivial systems overhead at scale.
L529: An important engineering direction is to design asynchronous and streaming variants (e.g., delayed bin updates, batched adversary steps, or partially offloaded bookkeeping) that preserve the core objective while minimizing training slowdown.
L530: ##### Sensitivity to online binning and reward noise.
L531: Our “group” notion is induced by an online estimator of difficulty, rather than static metadata. While this avoids reliance on brittle human-defined group labels, it also introduces potential noise sources: estimated pass@k may have high variance early in training, and bin boundaries can induce discontinuous group reassignment. These effects can bias both adversaries if not handled carefully.
L532: Future work should explore principled uncertainty-aware binning (e.g., Bayesian estimators or confidence-bound assignment rules), as well as robustness to verifier calibration drift and reward-model nonstationarity. It may also be valuable to incorporate process-level or stepwise supervision signals (when available) to stabilize difficulty estimation, rather than relying solely on outcome-only pass@k.
L533: ##### Generalization and evaluation beyond the current pipeline.
L534: Although we report improvements on advanced benchmarks, we do not yet provide a systematic evaluation protocol for distribution shift. A natural next step is to test whether the adversarial curricula learned on one training mixture transfer to new mixtures, or whether they overfit to dataset-specific artifacts.
L535: More broadly, our method suggests a future direction where GDRO-style training is used not only to improve average in-distribution metrics, but to target robustness to hidden stratification and distribution shift (cite105†Sagawa et al., 2020 ; cite168†Oakden-Rayner et al., 2020 ). Crucially, this should be framed as future work: out-of-distribution generalization is not a primary motivation of this paper, but an important downstream question enabled by the methodology.
L536: ##### Toward learning from the model’s own experience.
L537: A key longer-term direction is to couple our adversarial distribution shaping with experience generation and continual post-training. For example, one can imagine a closed loop where the model: (i) proposes new problems or perturbations, (ii) evaluates its own failures, and (iii) uses Prompt-GDRO/Rollout-GDRO to prioritize the resulting frontier.
L538: This connects naturally to self-training and self-improvement paradigms such as STaR-style bootstrapping (cite169†Zelikman et al., 2022 ), Quiet-STaR-style implicit “thinking” training (cite170†Zelikman et al., 2024 ), self-rewarding / judge-based optimization (cite171†Yuan et al., 2024 ), and RLAIF-style scalable feedback (cite172†Lee et al., 2023 ).
L539: Realizing such a pipeline requires addressing continual-learning issues (e.g., catastrophic forgetting (cite173†Rolnick et al., 2019 )), maintaining replay buffers (cite174†Schaul et al., 2015 ), and preventing reward hacking under self-generated supervision.
L540: ##### Beyond exponential-weights GDRO: richer ambiguity sets and scalable solvers.
L541: Our current instantiation uses exponential-weights style updates over a discrete set of groups/arms. However, the broader DRO literature offers many alternative ambiguity sets and solution methods that may be better suited for future scaling: $f$-divergence DRO admits stochastic-gradient formulations (cite151†Namkoong and Duchi, 2016 ), and recent work studies computationally efficient large-scale solvers for DRO objectives such as CVaR and $\chi^{2}$-based uncertainty sets (cite175†Levy et al., 2020 ).
L542: Wasserstein DRO provides a complementary metric-based robustness lens with tractable reformulations and finite-sample guarantees (cite153†Esfahani and Kuhn, 2018 ). On the RL side, robust MDP formulations (cite154†Iyengar, 2005 ; cite155†Nilim and El Ghaoui, 2005 ) and scalable $\phi$-divergence regularization approaches (cite176†Panaganti et al., 2024 ) suggest additional ways to model uncertainty and allocate resources under environment shift.
L543: A concrete research agenda is to identify which ambiguity sets best correspond to the operational failure modes of reasoning post-training (e.g., verifier mismatch, data mixture drift, or hard-sample scarcity), and to develop scalable solvers compatible with modern LLM training.
L544: ##### Beyond robustness: adversarial reasoning objectives for safety and risk.
L545: Finally, our adversaries currently act on what is trained (prompt distribution) and how intensively it is trained (rollout budgets), but not on richer forms of adversarial reasoning objectives. An important future direction is to design adversaries that target specific reasoning desiderata beyond accuracy, such as safety, risk avoidance, and constraint satisfaction.
L546: This connects to alignment frameworks that rely on rule-based or AI-generated feedback (cite177†Bai et al., 2022 ; cite172†Lee et al., 2023 ), as well as risk-sensitive optimization objectives. We view this as a distinct problem from classical DRO: rather than protecting against distributional uncertainty alone, the goal becomes to adversarially surface and correct undesirable reasoning behaviors (e.g., unsafe tool use, brittle shortcuts, or overconfident hallucinations) under realistic deployment constraints.
L547: ## 8 Conclusion
L548: We introduced two multi-adversary GDRO frameworks for reasoning post-training that move beyond the static uniformity of standard GRPO by defining dynamic groups via an online difficulty classifier (stable pass@k binning).
L549: On this shared grouping layer, Prompt-GDRO uses an EMA-debiased GDRO-EXP3P reweighting to concentrate updates on persistently hard bins without frequency artifacts, and Rollout-GDRO uses a GDRO-EXP3P adversary with a shadow-price controller to redistribute rollouts under a fixed mean compute budget. In this work, we evaluate Prompt-GDRO and Rollout-GDRO independently (no coupling); studying their joint dynamics is left to future work (§cite52†7 ).
L550: Across Qwen3-Base scales, both mechanisms are compute-neutral in the sense of §cite37†5 yet improve pass@8 over GRPO by up to 13.13% (Prompt-GDRO) and 10.64% (Rollout-GDRO), and diagnostics indicate an emergent curriculum as sampling weights and rollout budgets track the evolving reasoning frontier. We hope these results motivate further work on dynamic grouping and DRO-style training games as principled components of future reasoning post-training pipelines.
L551: ## References
L552:   * Agarwal et al. (2019) A. Agarwal, N. Jiang, S. M. Kakade, and W. Sun Reinforcement learning: theory and algorithms. CS Dept., UW Seattle, Seattle, WA, USA, Tech. Rep. External Links: cite178†Link†rltheorybook.github.io Cited by: cite179†footnote 3 .
L553:   * Bai et al. (2022) Y. Bai, S. Kadavath, S. Kundu, A. Askell, et al. Constitutional AI: harmlessness from AI feedback. External Links: cite180†Document†dx.doi.org , 2212.08073, cite181†Link Cited by: cite182†§7 .


## Original response: stdnext3tail0

Group Distributionally Robust Optimization-Driven Reinforcement Learning for LLM Reasoning (https://arxiv.org/html/2601.19280v1)
citeturn28414view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28405view1","lineno":400}); Total lines: 1191
L335: The entropic GDRO view explains what objective the exponential-weights adversary is tracking. A complementary (standard) lens explains why coupling this adversary with gradient-based policy updates is sensible: in a convex–concave game, if both players have sublinear regret, time-averaged iterates converge to an approximate saddle point.
L336: Concretely, letting $f(\theta,q)\triangleq\sum_{b=1}^{B}q(b)L_{b}(\theta)$ and writing $\bar{\theta}=\frac{1}{T}\sum_{t=1}^{T}\theta_{t}$ and $\bar{q}=\frac{1}{T}\sum_{t=1}^{T}q_{t}$, one obtains the generic bound
L337:  | $$\max_{q\in\Delta_{B}}f(\bar{\theta},q)\;-\;\min_{\theta\in\Theta}f(\theta,\bar{q})\;\leq\;\frac{\mathrm{Regret}_{\theta}(T)+\mathrm{Regret}_{q}(T)}{T},$$  |  | (27)
L338: where $\mathrm{Regret}_{\theta}(T)$ and $\mathrm{Regret}_{q}(T)$ are the cumulative regrets of the learner and adversary, respectively. Appendix cite75†B.1.2 states a precise version (with step sizes) for the convex bounded regime.
L339: In deep RL, we read Eq. (cite118†27 ) as an optimization principle: if (i) the GRPO updates behave like a low-regret learner and (ii) the Prompt-GDRO adversary behaves like a low-regret reweighting rule, then the training dynamics push down the robust (worst-group) objective over time.
L340: #### 4.2.3 Toy validation on MATH: entropy and worst-group robustness
L341: 
L342: The analysis above predicts that a well-behaved Prompt-GDRO adversary should (i) avoid collapsing onto a tiny set of bins due to noisy estimates and (ii) improve worst-group performance. We validate these qualitative predictions on the MATH benchmark as a toy study (Prompt-GDRO only).
L343: The standard GRPO baseline achieves a Worst-Group Pass@1 of roughly $33.92\%$. While a class-based GDRO baseline improves this to $37.7\%$, it exhibits instability in the adversary entropy, collapsing to a narrow effective support of $\sim 12$ groups. In contrast, our EMA-debiased formulation achieves the highest robustness with Worst-Group Pass@1 of $39.6\%$, and maintains a broader active support of $\sim 24$ groups throughout training.
L344: This broader support is consistent with the “intensive difficulty” objective in Eq. (cite113†12 ): instead of chasing a few high-variance bins, the adversary sustains a diversified portfolio of challenging bins, forcing the policy to improve along a wider Pareto frontier of hard prompts.
L345: ### 4.3 Adversary II (Rollout-GDRO): Compute allocation as an economic control problem
L346: Prompt reweighting changes which bins receive learning pressure; rollout budgeting changes how much exploration is used to estimate and optimize that pressure. The key empirical fact is that rollouts are not equally useful everywhere: once a bin is nearly solved, additional rollouts mostly repeat correct solutions and contribute low-variance gradients; on frontier bins, additional rollouts reduce Monte Carlo noise and improve both reward estimation and GRPO’s within-prompt normalization.
L347: ##### Recap: compute-neutral rollout budgeting.
L348: Rollout-GDRO is defined in Section cite17†3.3 . At each step, the controller selects a bin-specific rollout count $n_{b}\in\{n_{\min},\dots,n_{\max}\}$ under a strict mean-rollout budget $\bar{n}$. Operationally, it uses a Lagrangian relaxation with multiplier $\mu$ (a shadow price of compute): the penalized rollout “arm loss” $L_{b}(n)$ is defined in Eq. (cite119†20 ), and $\mu$ is updated by dual ascent (Eq. (cite120†21 )).
L349: This closed-loop control is what produces the “budget frontier” and “multiplier effect” patterns in Section cite43†5.3 .
L350: #### 4.3.1 A variance proxy for why allocating more rollouts helps
L351: The rollout allocator is most useful when extra rollouts reduce the Monte Carlo noise of the GRPO update. A simple proxy is to focus on the stochastic variance of the per-prompt gradient estimate. Even though GRPO normalizes advantages within a rollout group (coupling the rollouts for a prompt), a mild bounded-differences condition on the resulting prompt-level gradient estimator implies the conditional variance still contracts at rate $O(1/n_{b})$ with the number of rollouts.
L352: Abstractly, we can write a bin-dependent “intrinsic variance” parameter $v_{b}(\theta)$ so that the per-prompt conditional variance obeys $\mathrm{Var}[\hat{g}(x;\theta,n_{b})\mid g_{t}(x)=b]\leq v_{b}(\theta)/n_{b}$, and approximate the batch-level noise by
L353:  | $$\mathrm{VarProxy}(\mathbf{n};\theta)\;\triangleq\;\sum_{b=1}^{B}\bar{q}_{b}\,\frac{v_{b}(\theta)}{n_{b}},\qquad\bar{q}_{b}\triangleq\hat{q}_{t}(b),$$  |  | (28)
L354: 
L355: where $\bar{q}_{b}$ are the realized bin fractions in the current batch. Appendix cite77†B.2.1 makes this precise (via a bounded-differences / Efron–Stein argument) under i.i.d. rollout sampling, and notes that the condition accommodates GRPO’s within-prompt normalization.
L356: #### 4.3.2 The variance-optimal allocation obeys a square-root law
L357: 
L358: Motivated by Eq. (cite121†28 ), consider the continuous relaxation of a variance-aware compute-neutral allocation:
L359: 
L360:  | $$\min_{\mathbf{n}\in\mathbb{R}_{+}^{B}}\;\sum_{b=1}^{B}\bar{q}_{b}\,\frac{v_{b}(\theta)}{n_{b}}\qquad\text{s.t.}\qquad\sum_{b=1}^{B}\bar{q}_{b}\,n_{b}=\bar{n}.$$  |  | (29)
L361: ###### Theorem 4.2 (Square-root law for variance-optimal allocation).
L362: 
L363: Let $A\triangleq\{b\in[B]:\bar{q}_{b}>0\}$ denote the set of bins present in the batch. If $v_{b}(\theta)>0$ for all $b\in A$, then the minimizer of Eq. (cite122†29 ) is unique on the active coordinates and equals
L364: 
L365:  | $$n_{b}^{\star}=\bar{n}\cdot\frac{\sqrt{v_{b}(\theta)}}{\sum_{j=1}^{B}\bar{q}_{j}\,\sqrt{v_{j}(\theta)}},\qquad b\in A.$$  |  | (30)
L366: 
L367: Proof. Appendix cite80†B.2.2 .
L368: ##### Implications for Rollout-GDRO.
L369: 
L370: Eq. (cite123†30 ) is the classical Neyman/square-root allocation: bins with higher intrinsic variance receive more rollouts, with $n_{b}^{\star}\propto\sqrt{v_{b}(\theta)}$. The associated KKT condition can be written as a shadow-price rule: for a multiplier $\mu>0$, the per-bin best response of the continuous relaxation solves
L371: 
L372:  | $$n_{b}(\mu)\;=\;\arg\min_{n>0}\;\frac{v_{b}(\theta)}{n}+\mu n\;=\;\sqrt{\frac{v_{b}(\theta)}{\mu}},$$  |  | (31)
L373: and $\mu$ is chosen to satisfy the mean-budget constraint. This clarifies why Rollout-GDRO naturally admits an “economic” interpretation: the dual variable $\mu$ trades off variance reduction against compute.
L374: In practice we choose $n_{b}$ from a discrete set of rollout arms and only observe bandit feedback (the value of the chosen arm). Rollout-GDRO’s EXP3P updates and DP-based selection step (Section cite17†3.3 ) can be read as an online approximation to the shadow-price solution above; the resulting best-response map is piecewise constant in $\mu$, which matches the staircase/threshold transitions in our rollout heatmaps.
L375: We defer the corresponding online-learning formalization (and extensions beyond the variance proxy) to the appendix.
L376: ## 5 Experiments
L377: 
L378: In this section, we present the empirical evaluation of our Multi-Adversary GDRO framework. We use the DAPO 14.1k English dataset^{2}^{2} 2 cite124†https://huggingface.co/datasets/open-r1/DAPO-Math-17k-Processed†huggingface.co for all training runs, following a standard post-training pipeline.
L379: Metrics. Unless stated otherwise, we report mean@8 for benchmark accuracies: each prompt is evaluated with 8 sampled completions and we average the binary correctness indicator across those 8 trials. We additionally report pass@8, the probability that at least one of the 8 completions is correct (estimated from the same samples). This distinction matters for reasoning: mean@8 reflects typical performance, while pass@8 captures “best-of-$k$” robustness under limited search.
L380: Compute neutrality. Prompt-GDRO keeps the rollout budget fixed and changes training pressure through bin-wise reweighting of GRPO updates. Rollout-GDRO keeps the mean rollout budget fixed (e.g., $\bar{n}=4$) and redistributes rollouts across bins. Thus, improvements reflect better use of the same overall training compute rather than a larger sampling budget.
L381: We first report the quantitative improvements on standard mathematical reasoning benchmarks. Subsequently, we provide a rigorous qualitative analysis of the dynamic difficulty landscape, interpreting how the interaction between model capacity and data heterogeneity drives the emergent curriculum observed in our prompt reweighting distribution and rollout allocation strategies.
L382: ### 5.1 Main Results
L383: 
L384: We evaluate our method across three model scales: Qwen3-1.7B-Base, Qwen3-4B-Base, and Qwen3-8B-Base. We compare the standard GRPO baseline against our two proposed mechanisms: Prompt-GDRO (adversarial prompt reweighting driven by online difficulty bins) and Rollout-GDRO (adversarial compute budgeting). Table cite125†1 summarizes the performance at the peak checkpoint for each stabilized run.
L385: Table 1: Results on mathematical reasoning benchmarks for Prompt Reweighting GDRO and Rollout Budgeting GDRO vs GRPO Baseline. Bold values indicate methods that outperform the GRPO Baseline (independent comparison). The AIME column reports the average accuracy of AIME 2024 and AIME 2025. The percentage improvement for pass@8 is shown in brackets. All other metrics reported are mean@8.
L386: Models  | MATH 500  | AIME  | AMC  | MINERVA  | OLYMPIAD  | GPQA  | pass@8
L387: Qwen3-1.7B-Base
L388: ---
L389: GRPO (Baseline)  | 50.62  | 5.42  | 34.69  | 14.56  | 23.07  | 26.39  | 50.74
L390: Prompt-GDRO  | 63.20  | 6.88  | 39.38  | 14.61  | 25.07  | 29.29  | 55.68 (+9.74%)
L391: Rollout-GDRO  | 63.98  | 7.50  | 36.87  | 17.28  | 26.71  | 27.72  | 56.14 (+10.64%)
L392: Qwen3-4B-Base
L393: ---
L394: GRPO (Baseline)  | 72.05  | 11.25  | 60.94  | 17.79  | 30.48  | 35.54  | 56.31
L395: Prompt-GDRO  | 75.78  | 12.92  | 64.06  | 26.72  | 40.98  | 40.88  | 63.70 (+13.13%)
L396: Rollout-GDRO  | 75.20  | 13.96  | 67.50  | 26.47  | 39.28  | 38.51  | 62.27 (+10.59%)
L397: Qwen3-8B-Base
L398: ---
L399: GRPO (Baseline)  | 73.45  | 14.38  | 66.56  | 28.17  | 36.92  | 42.25  | 62.04
L400: Prompt-GDRO  | 76.18  | 16.04  | 70.94  | 32.17  | 42.43  | 43.81  | 67.60 (+8.96%)
L401: Rollout-GDRO  | 77.88  | 15.63  | 66.88  | 29.55  | 43.62  | 43.31  | 67.75 (+9.20%)
L402: Our framework demonstrates robust gains across all settings. Prompt-GDRO consistently improves performance by explicitly targeting hard data groups, achieving a peak gain of +13.13% on the 4B model. Remarkably, Rollout-GDRO achieves comparable or superior results—improving the 1.7B model by +10.64% and the 8B model by +9.20%—without altering the data distribution.
L403: This validates our hypothesis that compute allocation is an equally powerful lever for robustness: by dynamically assigning more rollouts to high-variance prompts, the adversary reduces gradient variance exactly where the model is most uncertain, yielding gains that rival direct data curriculum learning.
L404: ### 5.2 Qualitative Analysis: The Dynamics of Difficulty (Prompt-GDRO)
L405: 
L406: To understand the mechanism behind these performance gains, we visualize the temporal evolution of the training distribution. Figure cite126†3 presents a comprehensive triptych tracking the causal chain of our adversarial mechanism: from data availability (prompt share) to adversarial pressure (weights) to learning payoff (reward).
L407: cite127†Image: Refer to caption Figure 3: The Causal Chain of Curriculum. A triptych comparing the Prompt Distribution (Left), Adversarial Weights (Middle), and Realized Reward (Right) for 1.7B, 4B, and 8B models. This visualizes the mechanism: even when hard bins are rare in the data (dark regions in Left), the adversary applies disproportionate pressure (bright bands in Middle), forcing the model to eventually crack these problems and yield positive rewards (emergence of red/blue bands in Right).
L408: This effectively proves that Prompt-GDRO decouples the learning signal from dataset frequency.
L409: ##### Capacity-Dependent Distribution Shift.
L410: 
L411: The training dynamics reveal a stark correlation between model capacity and the “velocity” of learning, as quantified by the macro-level metrics in Figure cite128†4 .
L412: 
L413:   * •
L414: Qwen3-1.7B (Top Row, Fig cite126†3 ): The model exhibits high inertia. While the dataset mass often lags in accbin_0, the scalar summary (Figure cite128†4 , top panel) shows the mean bin index steadily climbing past 2.0. The mass in bins $\geq 3$ trace reveals that even this smaller model is successfully pushed out of the trivial zone, preventing the stagnation typical of uniform baselines.
L415: 
L416:   * •
L417: Qwen3-4B (Middle Row, Fig cite126†3 ): This scale occupies a “Goldilocks zone.” The data distribution shows a steady migration to intermediate bins. The adversarial weights form a distinct, high-intensity diagonal frontier that leads the data distribution. By Step 366, the weight entropy stabilizes, indicating the adversary has locked into a high-precision curriculum targeting specific intermediate failure modes.
L418: 
L419:   * •
L420: Qwen3-8B (Bottom Row, Fig cite126†3 ): The largest model exhibits a rapid collapse of the unsolved mass. The scalar summaries show the mass in bins $\geq 8$ (dashed lines) spiking early, confirming that for capable models, the adversary aggressively focuses on the “last mile” of robustness—solving the few remaining hard cases—rather than wasting capacity on solved arithmetic.
L421: cite129†Image: Refer to caption Figure 4: Training Dynamics Quantified (Prompt-GDRO). (Top) The Mean Accuracy Bin Index tracks the rising difficulty of targeted prompts. (Middle) The fraction of prompts in difficulty bands $\geq 3$ (solid) and $\geq 8$ (dashed) highlights scaling laws: 1.7B struggles to clear the $\geq 3$ bar, while 8B rapidly saturates even the $\geq 8$ band.
L422: (Bottom) Entropy metrics confirm that the adversary maintains a diverse portfolio of difficulty, preventing mode collapse to a single bin. cite130†Image: Refer to caption Figure 5: Snapshots of the Learning Distribution. The probability mass of the training set across difficulty bins at four distinct training stages (Start, Early-Mid, Late-Mid, End).
L423: These publication-friendly checkpoints reveal the exact shape of the curriculum: note how the 4B model (Middle Row) transitions from a uniform start to a heavy emphasis on accbin_5–accbin_7 by mid-training, whereas the 8B model (Bottom Row) shifts almost its entire mass to the hardest bins by the final step.
L424: ##### Visualizing the Wave of Progress.
L425: 
L426: Figure cite131†5 offers discrete checkpoints that clarify the exact distributional shape at key training intervals.
L427: 
L428:   * •
L429: 
L430: The Heavy Tail (1.7B): Even at the final step (Step 605), the 1.7B model retains a significant plurality of mass ($\approx 45\%$) in accbin_0. The distribution remains right-skewed, indicating the “reasoning frontier” is anchored in fundamental difficulties.
L431: 
L432:   * •
L433: The High-Entropy Plateau (4B): By Step 366, the 4B model allocates over 50% of its probability mass to the intermediate accbin_5–accbin_7 range. This “plateau” represents a diverse curriculum where the model simultaneously refines intermediate concepts and attempts advanced problems.
L434: 
L435:   * •
L436: The Traveling Peak (8B): The 8B model demonstrates a clear “wave” dynamic. The peak of the distribution physically travels from left to right. By Step 430, the mass in accbin_0 has virtually vanished, and the bulk of the sampling budget is dedicated to accbin_8 and accbin_9. This confirms that for sufficient capacity, the primary challenge shifts rapidly from correctness to robustness, necessitating the dynamic budget reallocation our method provides.
L437: ##### Adversary lead–lag.
L438: The heatmaps in Figure cite126†3 suggest that the adversarial weights form a “frontier” that precedes the empirical data distribution. We quantify this intuition with a lightweight lead–lag proxy computed from logged bin statistics. Let $q_{t}\in\Delta_{B}$ denote the empirical prompt share over bins at training step $t$, and let $\hat{w}_{t}\in\Delta_{B}$ denote the normalized Prompt-GDRO weights across bins at the same step (the weight-only distribution, not reweighted by $q_{t}$).
L439: Define the mean bin index under the data and under the weights as
L440:  | $$\mu_{\mathrm{data}}(t)\triangleq\sum_{b=1}^{B}b\,q_{t}(b),\qquad\mu_{\mathrm{weight}}(t)\triangleq\sum_{b=1}^{B}b\,\hat{w}_{t}(b),$$  |  | (32)
L441: and the lead–lag gap $\Delta\mu(t)\triangleq\mu_{\mathrm{weight}}(t)-\mu_{\mathrm{data}}(t)$. A positive $\Delta\mu(t)$ indicates that the adversary’s weight distribution is shifted toward  higher-index  bins than the empirical prompt share.
L442: Under our convention (Section cite12†3.1 ) that accbin_0 corresponds to the lowest pass@8 interval and larger indices correspond to higher pass@8 (more solvable) prompts, this means the adversary emphasizes the current learnable frontier rather than simply mirroring the bulk of unsolved mass. Figure cite132†6 (left) shows that $\Delta\mu(t)$ is strongly positive early in training and decays over time, with faster decay at larger model scales.
L443: For Qwen3-8B, $\Delta\mu(t)$ eventually becomes slightly negative, consistent with the data distribution migrating quickly into high pass@8 bins while the adversary maintains pressure on the remaining low-pass@8 cases. Overall, the decay of $\Delta\mu(t)$ provides a compact scalar signature of the “traveling wave” curriculum: the adversary leads and the data distribution catches up as the policy improves.
L444: cite133†Image: Refer to caption (a) Prompt-GDRO lead–lag proxy. $\Delta\mu(t)=\mu_{\mathrm{weight}}(t)-\mu_{\mathrm{data}}(t)$, where $\mu_{\mathrm{data}}(t)=\sum_{b}b\,q_{t}(b)$ and $\mu_{\mathrm{weight}}(t)=\sum_{b}b\,\hat{w}_{t}(b)$.
L445: 
L446: cite134†Image: Refer to caption (b) Rollout-GDRO weighted SE proxy. $\mathrm{WSE}(t)=\sum_{b}q_{t}(b)\hat{\sigma}_{b}/\sqrt{n_{b}(t)}$ compared to a compute-matched uniform baseline.
L447: Figure 6: Two diagnostics for the two adversaries. (Left) Prompt-GDRO weights initially lead the empirical data distribution in bin index (a “learnable frontier”) and progressively align as the prompt-share distribution catches up. (Right) Rollout-GDRO reduces an offline weighted standard-error proxy relative to a uniform allocation with the same mean rollout budget, consistent with variance-aware compute allocation.
L448: ### 5.3 Qualitative Analysis: Adaptive Compute Allocation (Rollout-GDRO)
L449: 
L450: While Prompt-GDRO improves robustness by altering what data the model sees, Rollout-GDRO improves robustness by altering how deeply the model explores that data. To understand this mechanism, we analyze the adversarial budgeter’s behavior through three complementary visualizations: the continuous budget frontier, macro-level scalar dynamics, and discrete allocation snapshots.
L451: #### 5.3.1 The Budget Frontier
L452: 
L453: Figure cite135†7 visualizes the direct contrast between data frequency and resource allocation. The left column shows the prompt share (dataset mass), while the right column shows the allocated rollout budget per prompt.
L454: cite136†Image: Refer to caption Figure 7: The Budget Frontier. A comparison of the dataset’s natural difficulty distribution (Left) versus the adversarial rollout allocation (Right) for 1.7B, 4B, and 8B models. The color intensity in the Right column represents the number of rollouts assigned per prompt (from purple $\approx 2$ to yellow $\approx 12$).
L455: Note how the budgeter shifts compute intensity to the “transition zone,” decoupling resource allocation from data frequency: even when hard bins are rare (dark left), they receive maximum compute (bright right).
L456: This comparison offers the clearest qualitative proof of our method’s economic policy. For the 8B model (bottom row), the dataset mass (left) remains concentrated in easier bins for hundreds of steps. However, the budgeter (right) rapidly identifies the emerging capability in accbin_6 and above, locking high-compute resources onto these rare prompts.
L457: In contrast, the 1.7B model (top row) takes significantly longer to leave accbin_0, and the budget frontier moves sluggishly, confirming that the adversary adapts the curriculum pace to the model’s intrinsic scaling laws.
L458: #### 5.3.2 Macro-Dynamics of Allocation
L459: 
L460: To quantify these trends, Figure cite137†8 presents the macro-level training dynamics. The four stacked traces—Mean Accuracy Bin Index, High-Bin Mass, High-Bin Budget Share, and Entropy—provide a unified view of how Rollout-GDRO migrates compute toward harder domains.
L461: cite138†Image: Refer to caption Figure 8: Macro-Level Allocation Dynamics (Rollout-GDRO). (Top) The Mean Accuracy Bin Index tracks the rising difficulty of targeted prompts. (Middle) The “Mass in High Bins” trace serves as quantitative evidence of the rollout adversary: it shows the dual variable mechanism keeping the total budget fixed while aggressively reweighting toward hard groups ($\geq\texttt{accbin\_8}$).
L462: (Bottom) Entropy metrics confirm that the 8B model (green) sustains a diverse allocation strategy even as it conquers lower difficulties, contrasting with the slower migration of the 1.7B model (blue).
L463: The “Mass in High Bins” trace is particularly revealing. It serves as direct evidence of the DRO objective in action: as the models improve, the adversary steadily reallocates the fixed global budget toward bins $\geq 7$. This reallocation correlates directly with the inflection points observed in the pass@8 accuracy tables.
L464: Furthermore, the shared axes highlight distinct scaling trends: the 8B model (green line) learns to push its budget into high-difficulty bins significantly earlier than the 1.7B model (blue line), validating that larger capacity enables more aggressive curriculum acceleration.
L465: Variance-aware compute efficiency. Beyond shifting budget toward harder bins, we can directly test whether the rollout adversary reduces the uncertainty of the bin-wise training signal at fixed compute. Let $n_{b}(t)$ denote the realized number of rollouts per prompt allocated to bin $b$ at step $t$, and let $q_{t}(b)$ denote the prompt share.
L466: Using an offline bin-wise variability proxy $\hat{\sigma}_{b}$ (estimated once from the training logs as the empirical standard deviation of a per-prompt GRPO signal within each bin, e.g., the prompt-level loss $\ell(x;\theta)$), we define a weighted standard-error proxy
L467:  | $$\mathrm{WSE}(t)\triangleq\sum_{b=1}^{B}q_{t}(b)\,\frac{\hat{\sigma}_{b}}{\sqrt{n_{b}(t)}}.$$  |  | (33)
L468: We compare against a compute-matched uniform-rollout baseline by setting $n_{b}(t)\equiv\bar{n}$ for all bins $b$, which satisfies the mean-rollout constraint $\sum_{b=1}^{B}q_{t}(b)\,n_{b}(t)=\bar{n}$ and therefore matches overall sampling compute at each step. As shown in Figure cite132†6 (right), Rollout-GDRO consistently attains lower $\mathrm{WSE}(t)$ than the uniform baseline throughout training.
L469: Averaged over the plotted horizon, this corresponds to relative reductions of 37.1% (1.7B), 22.6% (4B), and 33.4% (8B), supporting the interpretation that Rollout-GDRO improves gradient information efficiency by allocating more rollouts to high-variance bins.
L470: #### 5.3.3 Discrete Economic Phases
L471: 
L472: Finally, Figure cite139†9 decomposes the continuous training process into discrete “chapters” of the curriculum. These snapshots clarify the magnitude of the adversarial intervention at key training stages (Start, Early, Mid, Late).
L473: cite140†Image: Refer to caption Figure 9: Snapshots of the Allocation Economy. Paired bars at four canonical steps showing the dataset share (dark blue) versus the normalized rollout budget (light blue) for each bin. This visualizes the “Multiplier Effect”: by Step 300, the 4B model allocates $>80\%$ of its budget to accbin_5+, even though these bins contain $<20\%$ of the data. This explicitly demonstrates how Rollout-GDRO amplifies the signal from rare, high-value prompts.
L474: The paired bars (Dataset Share vs. Rollout Budget) illustrate a massive Multiplier Effect. For example, at Step 300, the 4B model allocates over $80\%$ of its compute budget to bins $\geq 5$, despite these bins constituting less than $20\%$ of the training data. This confirms that our method creates a highly non-uniform economic policy that gives 5–10$\times$ more rollouts to the “reasoning frontier” than a uniform baseline would.
L475: This behavior is model-specific: the 8B row shows an even faster shift, embracing high-bin budgeting early in training (Step 118), which aligns with the rapid saturation of easy tasks observed in our qualitative analysis.
L476: ## 6 Additional Related Work
L477: 
L478: Our work studies reasoning post-training at the intersection of (i) RLVR/GRPO-style policy optimization, (ii) distributionally robust optimization (DRO) and group robustness, and (iii) adaptive allocation of training-time compute.
L479: ### 6.1 RLVR and Post-training for Reasoning
L480: RL-based post-training has become central for improving reasoning behaviors in LLMs. PPO (cite93†Schulman et al., 2017 ) underpins RLHF-style alignment (cite141†Ouyang et al., 2022 ), while GRPO (cite94†Shao et al., 2024 ) offers a value-free, group-normalized alternative that has proven effective for verifiable-reward domains such as math.
L481: Parallel research improves reward quality and credit assignment through process supervision and step-level signals (cite142†Lightman et al., 2023 ; cite95†Wang et al., 2024b ), as well as iterative refinement and self-improvement mechanisms (cite143†Gulcehre et al., 2023 ).
L482: More recently, large-scale RLVR has enabled open reasoning models trained primarily from verifiable rewards, highlighting the potential of pure RL to elicit sophisticated behaviors such as self-reflection and verification (cite144†Guo et al., 2025 ).
L483: However, a growing body of work suggests that where RLVR learns and how compute is spent are both highly non-uniform. Token-level analyses indicate that RLVR gains can concentrate on a small fraction of high-entropy “forking” tokens that control reasoning branches (cite97†Wang et al., 2025 ), while other studies argue RLVR may implicitly incentivize correct reasoning patterns already latent in the base model (cite145†Wen et al., 2025b ).
L484: At inference time, test-time scaling via longer “thinking” traces can be non-monotonic and may induce overthinking (cite146†Ghosal et al., 2025 ), and long-CoT reasoning models can exhibit looping pathologies under low-temperature decoding (cite147†Pipis et al., 2025 ).
L485: In parallel, several works explore alternative ways to trade off accuracy and compute, including budget-aware evaluation and compute-normalized comparisons (cite148†Wang et al., 2024a ), and inference-time orchestration strategies that decouple accuracy from raw CoT length (cite98†Madaan et al., 2025 ).
L486: Our work is complementary: rather than proposing a new reward or inference strategy, we focus on training-time mechanisms that adaptively steer (a) which prompts are sampled and (b) how many rollouts are allocated, with the goal of improving robustness and compute efficiency.
L487: ### 6.2 Distributionally Robust Optimization in Supervised Learning
L488: DRO formalizes robustness by minimizing worst-case risk over an ambiguity set of distributions around the empirical training distribution (cite149†Ben-Tal and Nemirovski, 1999 ; cite150†Rahimian and Mehrotra, 2019 ). In supervised learning, a common choice is divergence-based ambiguity sets, yielding objectives that emphasize performance under distribution shift and provide statistical guarantees (cite151†Namkoong and Duchi, 2016 ; cite152†Duchi et al., 2021 ).
L489: Wasserstein-based DRO offers an alternative geometry with tractable reformulations and strong finite-sample guarantees (cite153†Esfahani and Kuhn, 2018 ). Within deep learning, GDRO (cite105†Sagawa et al., 2020 ) operationalizes robustness to hidden stratification and spurious correlations by optimizing the maximum loss across pre-defined groups, and has become a standard tool for improving worst-group accuracy.
L490: On the algorithmic side, group-robust learning admits a natural game-theoretic and online learning interpretation; in particular, cite108†Soma et al. (2022) connect GDRO to no-regret dynamics (e.g., EXP3 variants), which directly motivates our use of GDRO-EXP3P for adversarial prompt reweighting.
L491: Our setting departs from classical supervised GDRO in two ways. First, we do not assume static group labels; instead we use an online difficulty classifier based on pass@k to define groups that evolve with the policy. Second, we introduce a second adversary that controls compute allocation (rollouts) under a budget constraint, extending the DRO perspective beyond data distribution shifts to training-time resource shifts.
L492: ### 6.3 Robust and Distributionally Robust Reinforcement Learning
L493: Robust RL traditionally models uncertainty in environment dynamics and seeks policies that perform well under worst-case transition perturbations, e.g., robust Markov decision processes (cite154†Iyengar, 2005 ; cite155†Nilim and El Ghaoui, 2005 ) and distributionally robust MDP formulations (cite156†Xu and Mannor, 2012 ). Recent work develops statistical and computational characterizations of robust RL (cite157†Panaganti et al., 2022 ).
L494: In contrast, our work keeps the underlying environment fixed and instead treats prompt difficulty and compute allocation as adversarially controlled quantities during LLM post-training. This yields a robustness lens that is closer to group robustness over tasks/prompts than to worst-case transition uncertainty.
L495: ### 6.4 Curriculum, Adaptive Compute, and Data Value
L496: Adaptive curricula and compute allocation are increasingly recognized as first-class components of reasoning systems. Curriculum-based post-training pipelines such as Light-R1 (cite158†Wen et al., 2025a ) explicitly stage data difficulty and objectives (SFT/DPO/RL) to elicit long-CoT behaviors.

