[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Regularized Online RLHF with Generalized Bilinear Preferences

[3] h6: Abstract

[4] p: We consider the problem of contextual online RLHF with general preferences, where the goal is to identify the Nash Equilibrium. We adopt the Generalized Bilinear Preference Model (GBPM) to capture potentially intransitive preferences via low-rank, skew-symmetric matrices. We investigate general preference learning with any strongly convex regularizer (where η − 1 \eta^{-1} is the regularization strength), generalizing beyond prior works limited to reverse KL-regularization. Central to our analysis is proving that the dual gap of the greedy policy is bounded by the square of the estimation error—a result derived solely from strong convexity and the skew-symmetricity of GBPM. Building on this insight and a feature diversity assumption, we establish two regret bounds via two simple algorithms: (1) Greedy Sampling achieves polylogarithmic, e 𝒪 ⁡ ( η ) e^{{\mathcal{O}}(\eta)} -free regret 𝒪 ~ ​ ( η ​ d 4 ​ ( log ⁡ T ) 2 ) \tilde{{\mathcal{O}}}(\eta d^{4}(\log T)^{2}) . (2) Explore-Then-Commit achieves poly ⁡ ( d ) \mathrm{poly}(d) -free regret 𝒪 ~ ​ ( η ​ r ​ T ) \tilde{{\mathcal{O}}}(\sqrt{\eta rT}) by exploiting the low-rank structure; this is the first statistically efficient guarantee for online RLHF in high-dimensions.

[5] h6: Keywords:

[6] figure: Table 1: Comparison of regret bounds for online RLHF under GBPM ; for unregularized regret, take η = ∞ {\color[rgb]{0.5,0,0.5}\eta}=\infty . For simplicity, we set δ = 1 T \delta=\frac{1}{T} but note that all guarantees hold with high probability. Also, we consider only poly ⁡ ( d , C min − 1 ) \mathrm{poly}(d,C_{\min}^{-1}) -dependencies. Algorithm Regret Bound ABR ​ - ​ Reg η \mathrm{ABR\text{-}Reg}_{\color[rgb]{0.75,0,0.25}\eta} MBR ​ - ​ Reg η \mathrm{MBR\text{-}Reg}_{\color[rgb]{0.75,0,0.25}\eta} μ ⁡ ( ⋅ ) \mu(\cdot) ψ ⁡ ( ⋅ ) \psi(\cdot) Greedy Sampling ( Wu et al., 2025a , Theorem 1) η 3 ​ e 9 ​ η ​ κ − 1 ​ d 3 ​ r ​ ( log ⁡ T ) 2 {\color[rgb]{0.5,0,0.5}\eta^{3}e^{9\eta}}\kappa^{-1}d^{3}r(\log T)^{2} ✗ ✓ Logistic ‡ \ddagger D KL ​ ( ⋅ , π r ​ e ​ f ) D_{\mathrm{KL}}(\cdot,\pi_{ref}) Optimistic Matrix Game ∗ * ( Nayak et al., 2025 , Theorem 2.1) η ​ d 4 ​ ( log ⁡ T ) 2 ∧ d 2 ​ T ​ log ⁡ T {\color[rgb]{0.5,0,0.5}\eta}d^{4}(\log T)^{2}\wedge d^{2}\sqrt{T}\log T ✓ ✓ Linear D KL ​ ( ⋅ , π r ​ e ​ f ) D_{\mathrm{KL}}(\cdot,\pi_{ref}) Greedy Sampling (Ours, Theorem 4.2 ) η ​ β ​ κ − 1 ​ C min − 1 ​ d 4 ​ ( log ⁡ T ) 2 ∧ κ − 1 2 ​ C min − 1 2 ​ d 2 ​ T ​ log ⁡ T {\color[rgb]{0.5,0,0.5}\eta}\beta\kappa^{-1}C_{\min}^{-1}d^{4}\left(\log T\right)^{2}\wedge\kappa^{-\frac{1}{2}}C_{\min}^{-\frac{1}{2}}d^{2}\sqrt{T}\log T ✗ ✓ Any Any β − 1 \beta^{-1} -SC Explore-Then-Commit † \dagger (Ours, Theorem 5.2 ) κ − 1 ​ C min − 1 ​ η ​ β ​ r ​ T ​ log ⁡ T ∧ κ − 2 ​ C min − 4 ​ r ​ T 2 ​ log ⁡ T 3 \kappa^{-1}C_{\min}^{-1}\sqrt{{\color[rgb]{0.5,0,0.5}\eta}\beta rT\log T}\wedge\sqrt[3]{\kappa^{-2}C_{\min}^{-4}rT^{2}\log T} ✓ ✓ Any Any β − 1 \beta^{-1} -SC ∗ * Discussed only for a non-contextual scenario, 𝒳 = { 𝒙 } {\mathcal{X}}=\{{\bm{x}}\} , but we believe that this is extendable to the contextual scenario as well. Allows for asymmetric KL-regularization: J η ​ ( π 1 , π 2 ) = J ⁡ ( π 1 , π 2 ) − η − 1 ​ D KL ​ ( π 1 , π r ​ e ​ f 1 ) + η − 1 ​ D KL ​ ( π 2 , π r ​ e ​ f 2 ) J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1},\pi^{2})=J(\pi^{1},\pi^{2})-{\color[rgb]{0.75,0,0.25}\eta^{-1}}D_{\mathrm{KL}}(\pi^{1},\pi_{ref}^{1})+{\color[rgb]{0.75,0,0.25}\eta^{-1}}D_{\mathrm{KL}}(\pi^{2},\pi_{ref}^{2}) . † \dagger Each rate is achieved with a different T 0 T_{0} ; “Any μ \mu ” should satisfy the conditions in Definition 2.2 , also self-concordant for Theorem 5.2 . ‡ \ddagger “Logistic” can be generalized to any μ \mu such that the cross-entropy loss is L L -Lipschitz in 𝚯 \bm{\Theta} .

[7] h2: 1 Introduction

[8] h4: RLHF Theory.

[9] p: Aligning large language models (LLMs) with human values has emerged as a central challenge in modern AI, driven by the success of models like Llama, Qwen, and GPT-4 ( Llama Team, 2024 ; Qwen Team, 2024 ; OpenAI, 2024 ) , which rely heavily on human preference feedback ( Christiano et al., 2017 ; Ouyang et al., 2022 ) . This framework, known as Reinforcement Learning from Human Feedback (RLHF) , necessitates a rigorous statistical foundation. The theoretical landscape of RLHF and Preference-based RL (PbRL; Wirth et al. (2017) ) has advanced rapidly, primarily under the Bradley-Terry-Luce (BTL) model ( Bradley and Terry, 1952 ; Plackett, 1975 ) , where each item i i possesses a latent reward (utility) r i ∈ ℝ r_{i}\in{\mathbb{R}} .

[10] p: A standard approach is to model this reward linearly as r i = ⟨ ϕ i , 𝜽 ⋆ ⟩ r_{i}=\langle\bm{\phi}_{i},\bm{\theta}_{\star}\rangle . Because this formulation naturally mirrors (contextual) linear bandits ( Abbasi-Yadkori et al., 2011 ; Chu et al., 2011 ; Li et al., 2017 ) and linear MDPs ( Jin et al., 2020 ) , it enables the direct adaptation of powerful tools from the bandit literature to interactive decision-making problems. Consequently, these techniques have been successfully extended to tackle various facets of LLM alignment, including dueling bandits and RL ( Novoseller et al., 2020 ; Zhu et al., 2023 ; Saha et al., 2023 ; Wu et al., 2024 ; Zhan et al., 2024b ; Li et al., 2023 ) , active learning from human feedback ( Das et al., 2025 ; Ji et al., 2025 ; Wu and Sun, 2024 ) , and principled exploration strategies ( Foster et al., 2025 ; Tuyls et al., 2026 ) . Despite their simplicity, such (generalized) linear model-based frameworks remain crucial for deriving concrete algorithmic intuition and often serve as the starting point for theoretically principled algorithm design. Furthermore, these foundational works have paved the way for more expressive, abstract function-approximation frameworks ( Xiong et al., 2024 ; Zhao et al., 2025b ; Zhao et al., 2025a ; Wu et al., 2025a ; Zhan et al., 2024a ; Huang et al., 2025b ) .

[11] h4: General Preference Learning.

[12] p: Despite its success, reward-based RLHF is fundamentally limited in modeling complex, cyclic preferences prevalent in human psychology ( May, 1954 ; Tversky, 1969 ) , as well as diverse human preferences ( Azar et al., 2024 ; Munos et al., 2024 ) . This calls for General Preference Learning (or Nash Learning ), which targets the Nash Equilibrium (NE) directly without assuming an underlying utility ( Nash, 1951 ; von Neumann, 1928 ; McKelvey and Palfrey, 1995 ; Munos et al., 2024 ) , and has demonstrated empirical promise in LLMs ( Ye et al., 2024 ; Anthropic, 2022 ; Cui et al., 2024 ; Rosset et al., 2024 ) . Broadly, research in this domain can be divided into two perspectives: optimization and statistical learning. The majority of recent progress has focused on the optimization perspective ( Sokota et al., 2023 ; Munos et al., 2024 ; Tiapkin et al., 2025 ; Zhang et al., 2025d ; Zhang et al., 2025c ; Wang et al., 2025 ; Zhou et al., 2025 ) : specifically, how to find the NE in a computationally efficient manner given a known game ( Nisan et al., 2007 ) . However, in contrast to reward-based RLHF, the statistical perspective of general preference learning remains sparse. Here, the game is unknown , requiring the learner to estimate the underlying preference model while simultaneously identifying the NE from limited (e.g., bandit) feedback. The limited literature in this setting primarily relies on general function approximation ( Chen et al., 2022 ; Wang et al., 2023 ; Ye et al., 2024 ; Wu et al., 2025a ) or restricts focus to tabular matrix games ( Heliou et al., 2017 ; O’Donoghue et al., 2021 ; Ito et al., 2025 ) .

[13] p: While recent works by Yang et al. (2025) ; Nayak et al. (2025) have explored linear function approximation, they rely on item pair-wise features and a linear link function. Beyond the restriction to a linear link, the assumption of access to valid item pair-wise features ( Jiang et al., 2023 ; Dong et al., 2024 ) is often impractical, as elaborated in Zhang et al. (2025a) . First, this necessitates ( K 2 ) \binom{K}{2} features for K K items, compared to just K K for item-wise features. Second, constructing pairwise features that ensure an inherently antisymmetric preference model is often ad-hoc and nontrivial; for instance, supervised preference models often exhibit positional bias (e.g., preferring the first response) when inputs are concatenated ( Shi et al., 2025 ) . Thus, analogous to the linear contextual BTL model, it is highly desirable from both theoretical and empirical perspectives to study general preference learning using item-wise features.

[14] h4: Generalized Bilinear Preference Model (GBPM).

[15] p: To bridge this gap, we adopt the Generalized Bilinear Preference Model (GBPM) , introduced by Lee et al. (2025) ; Zhang et al. (2025a) : given item-wise features ϕ 1 , ϕ 2 ∈ ℝ d \bm{\phi}^{1},\bm{\phi}^{2}\in{\mathbb{R}}^{d} , the preference probability is modeled as

[16] table: P ∗ ​ ( ϕ 1 ≻ ϕ 2 ) := μ ⁡ ( ( ϕ 1 ) ⊤ ​ 𝚯 ⋆ ​ ϕ 2 ) , P^{*}(\bm{\phi}^{1}\succ\bm{\phi}^{2}):=\mu\left((\bm{\phi}^{1})^{\top}\bm{\Theta}_{\star}\bm{\phi}^{2}\right), (1)

[17] p: where μ ⁡ ( ⋅ ) \mu(\cdot) is a link function satisfying μ ⁡ ( z ) + μ ⁡ ( − z ) = 1 \mu(z)+\mu(-z)=1 , and 𝚯 ⋆ ∈ ℝ d × d \bm{\Theta}_{\star}\in{\mathbb{R}}^{d\times d} is a potentially low-rank, skew-symmetric matrix. This extends linear BTL: the bilinear form captures pairwise relationships as in bilinear bandits ( Jun et al., 2019 ) , and skew-symmetry ensures that P ∗ P^{*} is anti-symmetric.

[18] h4: Contributions.

[19] p: In this paper, we tackle regularized online RLHF with general preferences under GBPM . We emphasize “ regularized ” to highlight that our contributions extend beyond the standard reverse KL-regularization dominating the prior literature ( Xiong et al., 2024 ; Zhao et al., 2025b ; Zhao et al., 2025a ; Wu et al., 2025a ) . Stemming from the mentioned prior literature, we ask the following central question:

[20] p: Under GBPM and generic regularizer, can we obtain “fast” rates (e.g., polylogarithmic or poly ⁡ ( d ) \mathrm{poly}(d) -free regret)?

[21] p: We answer this question largely in the affirmative. Our contributions are as follows: under a feature diversity assumption ,

[22] p: Polylogarithmic Regret via GS: We prove that Greedy Sampling (GS) achieves a regularized regret of 𝒪 ~ ​ ( η ​ d 4 ​ ( log ⁡ T ) 2 ∧ d 2 ​ T ) \tilde{{\mathcal{O}}}\left({\color[rgb]{0.75,0,0.25}\eta}d^{4}(\log T)^{2}\wedge d^{2}\sqrt{T}\right) . This partially resolves an open problem by Wu et al. (2025a) regarding the exponential dependency on η {\color[rgb]{0.75,0,0.25}\eta} . 1 1 1 We clarify that the feature diversity assumption was not part of their open problem ( Wu et al., 2025a , Appendix A.2) and is a condition we newly adopt for our analysis. Specifically, we show that GS achieves polylogarithmic regularized regret that is e 𝒪 ⁡ ( η ) {\color[rgb]{0.75,0,0.25}e^{{\mathcal{O}}(\eta)}} -free. ( Section 4 )

[23] p: poly ⁡ ( d ) \mathrm{poly}(d) -free Regret via ETC: Addressing the high-dimensional regime, we demonstrate that Explore-Then-Commit (ETC) with nuclear-norm regularized MLE achieves regularized regret bounds of 𝒪 ~ ​ ( η ​ r ​ T ) \widetilde{{\mathcal{O}}}\left(\sqrt{{\color[rgb]{0.75,0,0.25}\eta}rT}\right) and 𝒪 ~ ​ ( r 1 / 3 ​ T 2 / 3 ) \tilde{{\mathcal{O}}}(r^{1/3}T^{2/3}) . Notably, these bounds are poly ⁡ ( d ) \mathrm{poly}(d) -free, which is highly desirable in high dimensions where d d is large. ( Section 5 )

[24] p: Key Technical Novelty: Quadratic Bound on Dual Gap. Central to the analyses of both GS and ETC is a new bound on the dual gap, which may be of independent interest. We show that the dual gap of any greedy NE policy is upper bounded by the square of the estimation error of 𝚯 ⋆ \bm{\Theta}_{\star} . Our analysis leverages the skew-symmetry and strong convexity of the regularized game objective, and the integral probability metric representation of the ℓ 1 \ell_{1} -distance ( Müller, 1997 ) to derive a self-bounding quadratic inequality . ( Section 3 )

[25] p: We compare our regret bounds with prior arts under GBPM in Table 1 , where it can be seen that we obtain state-of-the-art for any link function μ ⁡ ( ⋅ ) \mu(\cdot) and any (strongly convex) regularizer ψ ⁡ ( ⋅ ) \psi(\cdot) .

[26] h4: Notations.

[27] p: For a set 𝒳 {\mathcal{X}} , Δ ⁡ ( 𝒳 ) \Delta({\mathcal{X}}) is the set of all possible probability distributions over 𝒳 {\mathcal{X}} . A ≲ B A\lesssim B denotes A ≤ c ​ B A\leq cB for an absolute constant c > 0 c>0 . For a , b ∈ ℝ a,b\in{\mathbb{R}} , we denote a ∨ b = max ⁡ { a , b } a\vee b=\max\{a,b\} and a ∧ b = min ⁡ { a , b } a\wedge b=\min\{a,b\} .

[28] h2: 2 Problem Setting

[29] h3: 2.1 (Self-Play) Interaction Protocol

[30] p: We consider a game defined by a ground-truth, contextual preference model P ∗ ​ ( 𝒂 1 ≻ 𝒂 2 ∣ 𝒙 ) P^{*}({\bm{a}}^{1}\succ{\bm{a}}^{2}\mid{\bm{x}}) , where 𝒙 ∈ 𝒳 {\bm{x}}\in{\mathcal{X}} is a context (question), and 𝒂 1 , 𝒂 2 ∈ 𝒜 {\bm{a}}^{1},{\bm{a}}^{2}\in{\mathcal{A}} are two actions (responses). The notation 𝒂 1 ≻ 𝒂 2 | 𝒙 {\bm{a}}^{1}\succ{\bm{a}}^{2}\mid{\bm{x}} indicates that response 𝒂 1 {\bm{a}}^{1} is preferred to 𝒂 2 {\bm{a}}^{2} given 𝒙 {\bm{x}} . Crucially, P ∗ P^{*} is anti-symmetric: P ∗ ​ ( 𝒂 1 ≻ 𝒂 2 ) + P ∗ ​ ( 𝒂 2 ≻ 𝒂 1 ) = 1 P^{*}({\bm{a}}^{1}\succ{\bm{a}}^{2})+P^{*}({\bm{a}}^{2}\succ{\bm{a}}^{1})=1 . A policy is a mapping π : 𝒳 → Δ ⁡ ( 𝒜 ) \pi:{\mathcal{X}}\rightarrow\Delta({\mathcal{A}}) , where π ( ⋅ | 𝒙 ) \pi(\cdot|{\bm{x}}) denotes the conditional distribution over actions. We denote the class of all such policies by Π \Pi , and define the ℓ 1 \ell_{1} -distance on Π \Pi as follows:

[31] table: ‖ π − π ′ ‖ 1 := ∑ ( 𝒙 , 𝒂 ) ∈ 𝒳 × 𝒜 | π ⁡ ( 𝒂 | 𝒙 ) − π ′ ​ ( 𝒂 | 𝒙 ) | . \left\lVert\pi-\pi^{\prime}\right\rVert_{1}:=\sum_{({\bm{x}},{\bm{a}})\in{\mathcal{X}}\times{\mathcal{A}}}|\pi({\bm{a}}|{\bm{x}})-\pi^{\prime}({\bm{a}}|{\bm{x}})|. (2)

[32] p: We adopt the self-play framework, where the learner controls both players to learn by playing against itself. Since the breakthrough of AlphaGo ( Silver et al., 2017 ; Silver et al., 2018 ) , self-play has been extensively studied in the RL theory literature ( Bai and Jin, 2020 ; Bai et al., 2020 ; Liu et al., 2021 ; Jin et al., 2022 ; Xiong et al., 2022 ) , and recently in LLM alignment ( Swamy et al., 2024 ; Wu et al., 2025b ; Zhang et al., 2025c ) . A key feature of this framework is that the learner can achieve high performance even in the absence of an expert or adversarial opponent.

[33] h4: Interaction Protocol.

[34] p: We define the preference between π 1 \pi^{1} ( max-player ) and π 2 \pi^{2} ( min-player ) given 𝒙 ∈ 𝒳 {\bm{x}}\in{\mathcal{X}} as:

[35] table: P ∗ ​ ( π 1 ≻ π 2 ∣ 𝒙 ) := 𝔼 𝒂 1 ∼ π 1 ( ⋅ | 𝒙 ) 𝒂 2 ∼ π 2 ( ⋅ | 𝒙 ) ​ [ P ∗ ​ ( 𝒂 1 ≻ 𝒂 2 ∣ 𝒙 ) ] . P^{*}(\pi^{1}\succ\pi^{2}\mid{\bm{x}}):=\mathbb{E}_{\begin{subarray}{c}{\bm{a}}^{1}\sim\pi^{1}(\cdot|{\bm{x}})\\ {\bm{a}}^{2}\sim\pi^{2}(\cdot|{\bm{x}})\end{subarray}}\left[P^{*}({\bm{a}}^{1}\succ{\bm{a}}^{2}\mid{\bm{x}})\right].

[36] p: Given a fixed context distribution d 0 ∈ Δ ⁡ ( 𝒳 ) d_{0}\in\Delta({\mathcal{X}}) (unknown to the learner), we denote the population preference as P ∗ ​ ( π 1 ≻ π 2 ) := 𝔼 𝒙 ∼ d 0 ​ [ P ∗ ​ ( π 1 ≻ π 2 | 𝒙 ) ] P^{*}(\pi^{1}\succ\pi^{2}):=\mathbb{E}_{{\bm{x}}\sim d_{0}}[P^{*}(\pi^{1}\succ\pi^{2}|{\bm{x}})] .

[37] p: The online contextual RLHF protocol proceeds as follows: At each t = 1 , … , T t=1,\dots,T , a context 𝒙 t ∼ d 0 {\bm{x}}_{t}\sim d_{0} is revealed. The learner chooses policies π ^ t 1 ( ⋅ | 𝒙 t ) {\color[rgb]{0,0,1}\hat{\pi}_{t}^{1}(\cdot|{\bm{x}}_{t})} and π ^ t 2 ( ⋅ | 𝒙 t ) {\color[rgb]{1,0,0}\hat{\pi}_{t}^{2}(\cdot|{\bm{x}}_{t})} , samples actions 𝒂 t 1 {\color[rgb]{0,0,1}{\bm{a}}_{t}^{1}} and 𝒂 t 2 {\color[rgb]{1,0,0}{\bm{a}}_{t}^{2}} , and receives a bandit feedback r t ∼ Ber ⁡ ( P ∗ ​ ( 𝒂 t 1 ≻ 𝒂 t 2 ∣ 𝒙 t ) ) r_{t}\sim\mathrm{Ber}(P^{*}({\color[rgb]{0,0,1}{\bm{a}}_{t}^{1}}\succ{\color[rgb]{1,0,0}{\bm{a}}_{t}^{2}}\mid{\bm{x}}_{t})) . This constitutes a contextual symmetric two-player zero-sum game ( Balduzzi et al., 2019 ) with bandit feedback.

[38] h4: Feature Diversity.

[39] p: We consider the following assumption, considered in prior literature on contextual bandits (see Theorem 3.1 and Section 6 for more discussions):

[40] h6: Assumption 1 (Feature Map and Diversity) .

[41] p: The learner has access to a known feature map ϕ : 𝒳 × 𝒜 → ℬ d ​ ( 1 ) \phi:{\mathcal{X}}\times{\mathcal{A}}\rightarrow{\mathcal{B}}^{d}(1) and an exploration policy ρ ( ⋅ | 𝐱 ) \rho(\cdot|{\bm{x}}) such that for a C min > 0 C_{\min}>0 :

[42] table: λ min ( 𝔼 𝒙 ∼ d 0 𝔼 𝒂 ∼ ρ ( ⋅ | 𝒙 ) [ ϕ ( 𝒙 , 𝒂 ) ϕ ( 𝒙 , 𝒂 ) ⊤ ] ) ≥ C min . \lambda_{\min}\left(\mathbb{E}_{{\bm{x}}\sim d_{0}}\mathbb{E}_{{\bm{a}}\sim\rho(\cdot|{\bm{x}})}\left[\phi({\bm{x}},{\bm{a}})\phi({\bm{x}},{\bm{a}})^{\top}\right]\right)\geq C_{\min}. (3)

[43] h6: Remark 2.1 (Scaling of C min C_{\min} ) .

[44] p: Well-conditioned sets (e.g., hypercubes) allow C min ≍ 1 C_{\min}\asymp 1 , while for ill-conditioned sets (e.g., standard basis), C min − 1 ≍ d − 1 C_{\min}^{-1}\asymp d^{-1} or worse. In this paper, our regime of interest is when C min − 1 ≍ 1 C_{\min}^{-1}\asymp 1 , although for completeness, we keep track of this quantity throughout.

[45] h3: 2.2 Generalized Bilinear Preference Model (GBPM)

[46] p: We now introduce the low-rank contextual general preference model that we consider in this work.

[47] p: First, we define Skew ⁡ ( d , 2 ​ r , S ) \mathrm{Skew}(d;2r,S) as the following:

[48] table: { 𝚯 ∈ Skew ( d ) : rank ( 𝚯 ) ≤ 2 r , ‖ 𝚯 ‖ nuc ≤ S } , \left\{\bm{\Theta}\in\mathrm{Skew}(d):\mathrm{rank}(\bm{\Theta})\leq 2r,\left\lVert\bm{\Theta}\right\rVert_{\mathrm{nuc}}\leq S\right\}, (4)

[49] p: where Skew ⁡ ( d ) := { 𝚯 ∈ ℝ d × d : 𝚯 ⊤ = − 𝚯 } . \mathrm{Skew}(d):=\left\{\bm{\Theta}\in{\mathbb{R}}^{d\times d}:\bm{\Theta}^{\top}=-\bm{\Theta}\right\}.

[50] p: Now the definition of GBPM ( Zhang et al., 2025a ; Lee et al., 2025 ) :

[51] h6: Definition 2.2 ( Generalized Bilinear Preference Model ) .

[52] p: The conditions for μ \mu are standard in logistic and generalized linear (dueling) bandits ( Faury et al., 2020 ; Abeille et al., 2021 ; Lee et al., 2024b ; Lee et al., 2024a ; Lee et al., 2025 ; Wu et al., 2024 ; Bengs et al., 2022 ) . The logistic link μ ⁡ ( z ) = ( 1 + e − z ) − 1 \mu(z)=(1+e^{-z})^{-1} satisfies the above with R s = 1 R_{s}=1 and L μ = 1 4 L_{\mu}=\frac{1}{4} . The linear link μ ⁡ ( z ) = 1 2 + z \mu(z)=\tfrac{1}{2}+z is also covered, in which case R s = 0 R_{s}=0 and L μ = 1 L_{\mu}=1 ( Gajane et al., 2015 ; Wu et al., 2024 ) .

[53] p: Throughout, we denote J ⁡ ( ϕ t 1 , ϕ t 2 , 𝚯 ) := μ ⁡ ( ( ϕ t 1 ) ⊤ ​ 𝚯 ​ ϕ t 2 ) J(\bm{\phi}_{t}^{1},\bm{\phi}_{t}^{2};\bm{\Theta}):=\mu((\bm{\phi}_{t}^{1})^{\top}\bm{\Theta}\bm{\phi}_{t}^{2}) and its expectation w.r.t. 𝒙 t ∼ d 0 {\bm{x}}_{t}\sim d_{0} and ϕ t i ∼ π i \bm{\phi}_{t}^{i}\sim\pi^{i} as J ⁡ ( π 1 , π 2 , 𝚯 ) J(\pi^{1},\pi^{2};\bm{\Theta}) . We also denote J ⁡ ( ⋅ , ⋅ ) := J ⁡ ( ⋅ , ⋅ , 𝚯 ⋆ ) J(\cdot,\cdot):=J(\cdot,\cdot;\bm{\Theta}_{\star}) .

[54] h3: 2.3 Regularized NE and Regret Definitions

[55] p: For a η ∈ ( 0 , ∞ ] {\color[rgb]{0.75,0,0.25}\eta}\in(0,\infty] and a β − 1 \beta^{-1} -strongly convex regularizer ψ : Π → ℝ ≥ 0 \psi:\Pi\rightarrow{\mathbb{R}}_{\geq 0} w.r.t. ‖ ⋅ ‖ 1 \left\lVert\cdot\right\rVert_{1} , we define a symmetric , regularized game objective J η : Π × Π → ℝ J_{\color[rgb]{0.75,0,0.25}\eta}:\Pi\times\Pi\rightarrow{\mathbb{R}} as follows:

[56] table: J η ​ ( π , π ′ , 𝚯 ) := J ⁡ ( π , π ′ , 𝚯 ) − η − 1 ​ ψ ​ ( π ) + η − 1 ​ ψ ​ ( π ′ ) . J_{\color[rgb]{0.75,0,0.25}\eta}(\pi,\pi^{\prime};\bm{\Theta}):=J(\pi,\pi^{\prime};\bm{\Theta})-{\color[rgb]{0.75,0,0.25}\eta^{-1}}\psi(\pi)+{\color[rgb]{0.75,0,0.25}\eta^{-1}}\psi(\pi^{\prime}).

[57] p: Standard solution concepts (e.g., Condorcet winners) may not exist in general preference learning ( Dudík et al., 2015 ; Bengs et al., 2021 ; Munos et al., 2024 ; Swamy et al., 2024 ) . Thus, as in many recent literature in online RLHF ( Munos et al., 2024 ) , we consider (regularized) Nash Equilibrium (NE) ( Nash, 1951 ; McKelvey and Palfrey, 1995 ) :

[58] h6: Definition 2.3 (Nash Equilibrium) .

[59] p: A pair ( π ⋆ 1 , π ⋆ 2 ) ∈ Π × Π (\pi^{1}_{\star},\pi^{2}_{\star})\in\Pi\times\Pi is a Nash equilibrium (NE) if for all π 1 , π 2 ∈ Π \pi^{1},\pi^{2}\in\Pi :

[60] table: J η ​ ( π 1 , π ⋆ 2 ) ≤ J η ​ ( π ⋆ 1 , π ⋆ 2 ) ≤ J η ​ ( π ⋆ 1 , π 2 ) . J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1},\pi^{2}_{\star})\leq J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1}_{\star},\pi^{2}_{\star})\leq J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1}_{\star},\pi^{2}).

[61] p: If π ⋆ 1 = π ⋆ 2 = : π ⋆ \pi^{1}_{\star}=\pi^{2}_{\star}=:\pi_{\star} , we refer to π ⋆ \pi_{\star} as a symmetric NE (SNE) . By the minimax theorem ( von Neumann, 1928 ; Sion, 1958 ) , any SNE π ⋆ \pi_{\star} is equivalently characterized as follows:

[62] table: π ⋆ ∈ arg ​ max π 1 ∈ Π ⁡ min π 2 ∈ Π ​ J η ​ ( π 1 , π 2 ) . \pi^{\star}\in\argmax_{\pi^{1}\in\Pi}\min_{\pi^{2}\in\Pi}J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1},\pi^{2}). (5)

[63] p: We also have the following important technical lemma, which will be critically used later:

[64] h6: Lemma 2.4 .

[65] p: For any 𝚯 ∈ Skew ⁡ ( d ) \bm{\Theta}\in\mathrm{Skew}(d) , the value of the max-min game, max π 1 ⁡ min π 2 ​ J η ​ ( π 1 , π 2 , 𝚯 ) \max_{\pi^{1}}\min_{\pi^{2}}J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1},\pi^{2};\bm{\Theta}) , is always 1 2 \frac{1}{2} .

[66] h6: Proof.

[67] p: For any 𝚯 \bm{\Theta} , there always exists a SNE ( Swamy et al., 2024 , Lemma 2.1) . As the game value of SNE is 1 2 \frac{1}{2} , it must be so for any NE ( von Neumann, 1928 ; Sion, 1958 ) . ∎

[68] p: We define the (symmetric) dual gap of a policy π ^ ∈ Π \hat{\pi}\in\Pi as

[69] table: DGap η ​ ( π ^ ) := 1 2 − min π 2 ∈ Π ⁡ J η ​ ( π ^ , π 2 ) . \mathrm{DGap}_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi}):=\frac{1}{2}-\min_{\pi^{2}\in\Pi}J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\pi^{2}). (6)

[70] p: Intuitively, this quantifies how close π ^ \hat{\pi} is to an SNE .

[71] p: We evaluate any resulting policy sequence { ( π ^ t 1 , π ^ t 2 ) } t ∈ [ T ] \{({\color[rgb]{0,0,1}\hat{\pi}_{t}^{1}},{\color[rgb]{1,0,0}\hat{\pi}_{t}^{2}})\}_{t\in[T]} using the following two regrets:

[72] h6: Definition 2.5 .

[73] h6: Remark 2.6 .

[74] p: These regrets are stronger than those considered in the standard adversarial bandit literature. The above regrets can be converted to sample complexities for finding an NE via online-to-batch conversion ( Freund and Schapire, 1999 ) ; see Appendix D for detailed discussions.

[75] h4: Computation Oracles.

[76] p: We lastly describe the computation model. We assume the learner is tractable (not necessarily efficient), accessing 𝒜 {\mathcal{A}} and Skew ⁡ ( d ) \mathrm{Skew}(d) only via:

[77] h6: Oracle 1 .

[78] p: Sampling: Given 𝐱 ∈ 𝒳 {\bm{x}}\in{\mathcal{X}} and π ∈ Π \pi\in\Pi , output a sample 𝐚 ∼ π ( ⋅ | 𝐱 ) {\bm{a}}\sim\pi(\cdot|{\bm{x}}) .

[79] h6: Oracle 2 .

[80] p: Evaluation: Given a 𝚯 \bm{\Theta} and π , π ′ ∈ Π \pi,\pi^{\prime}\in\Pi , return J η ​ ( π , π ′ , 𝚯 ) J_{\color[rgb]{0.75,0,0.25}\eta}(\pi,\pi^{\prime};\bm{\Theta}) (via Monte Carlo).

[81] h6: Oracle 3 .

[82] p: Population NE: Given a 𝚯 \bm{\Theta} , output the population SNE : arg ​ max π 1 ⁡ arg ​ min π 2 ​ J η ​ ( π 1 , π 2 , 𝚯 ) \argmax_{\pi^{1}}\argmin_{\pi^{2}}J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1},\pi^{2};\bm{\Theta}) .

[83] p: The last oracle has been considered in prior online RLHF literature ( Ye et al., 2024 ; Wu et al., 2025a ) and learning in games under bandit feedback ( O’Donoghue et al., 2021 ; Yang et al., 2025 ; Nayak et al., 2025 ) .

[84] h2: 3 A New Analysis of Regularized Regret

[85] p: We present our main technical contribution: a new bound on the instantaneous dual gap of any greedy NE policy for the max-player. Denoting ϕ ∼ π \bm{\phi}\sim\pi as sampling a ϕ ⁡ ( 𝒙 , 𝒂 ) ∈ ℬ d ​ ( 1 ) \bm{\phi}({\bm{x}},{\bm{a}})\in{\mathcal{B}}^{d}(1) from 𝒂 ∼ π ( ⋅ | 𝒙 ) {\bm{a}}\sim\pi(\cdot|{\bm{x}}) and 𝒙 ∼ d 0 {\bm{x}}\sim d_{0} ,

[86] h6: Theorem 3.1 .

[87] p: We first remark that the feature diversity assumption ( Assumption 1 ) is not needed here. One important observation is that this holds for any choice of estimator and any choice of β − 1 \beta^{-1} -strongly convex regularizer ψ ⁡ ( ⋅ ) \psi(\cdot) . As long as η < ∞ {\color[rgb]{0.75,0,0.25}\eta}<\infty (e.g., the regularization by ψ \psi exists), the instantaneous dual gap is bounded quadratically with the expected estimation error of 𝚯 ⋆ \bm{\Theta}_{\star} along the features of π ^ t {\color[rgb]{0,0,1}\hat{\pi}_{t}} ; in the proof, one can see that without strong convexity, one only gets 𝔼 ϕ ​ [ ‖ 𝑬 t ​ ϕ ‖ ] \mathbb{E}_{\bm{\phi}}[\left\lVert{\bm{E}}_{t}\bm{\phi}\right\rVert] .

[88] h6: Proof Sketch of Theorem 3.1 .

[89] p: The proof starts with the first-order Taylor expansion, which gives a linear term and the quadratic term, similar to the self-concordant analysis of logistic and generalized linear bandits ( Abeille et al., 2021 ; Lee et al., 2024b ; Lee et al., 2024a ) . We then derive our key technical lemma ( Lemma 3.2 ), which bounds the linear term by the linear error term multiplied by ℓ 1 \ell_{1} -distance between π ^ t \hat{\pi}_{t} and its best response ; this is in turn derived by the unique skew-symmetric nature of GBPM and somewhat surprisingly, the integral probability metric (IPM) representation of ℓ 1 \ell_{1} -distance ( Müller, 1997 ) . The ℓ 1 \ell_{1} -distance is in turn bounded by the square root of the instantaneous dual gap, which follows from the strongly convex landscape of J η J_{\color[rgb]{0.75,0,0.25}\eta} . This results in a self-bounding quadratic inequality , which, when solved, results in the quadratic error term. ∎

[90] h3: 3.1 Proof of Theorem 3.1

[91] h4: Regret Decomposition via Self-Concordance

[92] p: Let us denote π ~ = arg ​ min π ∈ Π ⁡ J η ​ ( π ^ , π ) \tilde{\pi}=\argmin_{\pi\in\Pi}J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\pi) as the min-player’s best response to π ^ \hat{\pi} w.r.t. the true objective. We denote the dual gap of π ^ \hat{\pi} as X := 1 2 − J η ​ ( π ^ , π ~ ) {\color[rgb]{0.75,0.5,0.25}X}:=\frac{1}{2}-J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\tilde{\pi}) . Then, note that

[93] table: X \displaystyle{\color[rgb]{0.75,0.5,0.25}X} = J η ​ ( π ^ , π ~ , 𝚯 ^ ) − J η ​ ( π ^ , π ~ ) + 1 2 − J η ​ ( π ^ , π ~ , 𝚯 ^ ) \displaystyle=J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\tilde{\pi};\widehat{\bm{\Theta}})-J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\tilde{\pi})+\frac{1}{2}-J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\tilde{\pi};\widehat{\bm{\Theta}}) ≤ J η ​ ( π ^ , π ~ , 𝚯 ^ ) − J η ​ ( π ^ , π ~ ) = J ⁡ ( π ^ , π ~ , 𝚯 ^ ) − J ⁡ ( π ^ , π ~ ) , \displaystyle\leq J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\tilde{\pi};\widehat{\bm{\Theta}})-J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\tilde{\pi})=J(\hat{\pi},\tilde{\pi};\widehat{\bm{\Theta}})-J(\hat{\pi},\tilde{\pi}),

[94] p: where the inequality holds because

[95] table: 1 2 ​ = ( Lemma 2.4 ) ​ min π ∈ Π ​ J η ​ ( π ^ , π , 𝚯 ^ ) ​ ≤ ( E q n . ( 7 ) ) ​ J η ​ ( π ^ , π ~ , 𝚯 ^ ) . \frac{1}{2}\overset{(\lx@cref{creftype~refnum}{lem:symmetric})}{=}\min_{\pi\in\Pi}J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\pi;\widehat{\bm{\Theta}})\overset{(Eqn.~(\ref{eqn:NE}))}{\leq}J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\tilde{\pi};\widehat{\bm{\Theta}}).

[96] p: Note that the symmetric nature of our game objective is critical here, as it ensures that the game value remains unchanged regardless of 𝚯 \bm{\Theta} ( Lemma 2.4 ).

[97] p: Denoting 𝔼 := 𝔼 ϕ ∼ π ^ , ϕ ~ ∼ π ~ \mathbb{E}:=\mathbb{E}_{\bm{\phi}\sim\hat{\pi},\tilde{\bm{\phi}}\sim\tilde{\pi}} or 𝔼 ϕ ∼ π ^ \mathbb{E}_{\bm{\phi}\sim\hat{\pi}} when it is clear from the context, via Taylor expansion with integral remainder , we have the following:

[98] table: J ⁡ ( π ^ , π ~ , 𝚯 ^ ) − J ⁡ ( π ^ , π ~ ) \displaystyle J(\hat{\pi},\tilde{\pi};\widehat{\bm{\Theta}})-J(\hat{\pi},\tilde{\pi}) = − 𝔼 ⁡ [ μ ˙ ​ ( ϕ ⊤ ​ 𝚯 ⋆ ​ ϕ ~ ) ​ ϕ ⊤ ​ 𝑬 ​ ϕ ~ ] ⏟ ( a ) \displaystyle=\underbrace{-\mathbb{E}\left[\dot{\mu}(\bm{\phi}^{\top}\bm{\Theta}_{\star}\tilde{\bm{\phi}})\bm{\phi}^{\top}{\bm{E}}\tilde{\bm{\phi}}\right]}_{(a)} + 𝔼 ⁡ [ [ ∫ 0 1 ( 1 − z ) ​ μ ¨ ​ ( ϕ ⊤ ​ ( 𝚯 ⋆ − z ​ 𝑬 t ) ​ ϕ ~ ) ​ d z ] ​ ( ϕ ⊤ ​ 𝑬 ​ ϕ ~ ) 2 ] ⏟ ( b ) . \displaystyle\ +\underbrace{\mathbb{E}\left[\left[\int_{0}^{1}(1-z)\ddot{\mu}\left(\bm{\phi}^{\top}\left(\bm{\Theta}_{\star}-z{\bm{E}}_{t}\right)\tilde{\bm{\phi}}\right)dz\right](\bm{\phi}^{\top}{\bm{E}}\tilde{\bm{\phi}})^{2}\right]}_{(b)}.

[99] p: We bound ( a ) (a) with the following simple yet powerful lemma, whose proof is deferred to the next subsection:

[100] h6: Lemma 3.2 .

[101] p: We now bound ( b ) (b) . First, we have

[102] table: ( b ) ≤ L μ ​ 𝔼 ​ [ ( ϕ ⊤ ​ 𝑬 ​ ϕ ~ ) 2 ] ​ ∫ 0 1 ( 1 − z ) ​ 𝑑 z = L μ 2 ​ 𝔼 ​ [ ( ϕ ⊤ ​ 𝑬 ​ ϕ ~ ) 2 ] . (b)\leq L_{\mu}\mathbb{E}[(\bm{\phi}^{\top}{\bm{E}}\tilde{\bm{\phi}})^{2}]\int_{0}^{1}(1-z)dz=\frac{L_{\mu}}{2}\mathbb{E}[(\bm{\phi}^{\top}{\bm{E}}\tilde{\bm{\phi}})^{2}].

[103] p: For clarity, we will explicitly distinguish between the two expectations 𝔼 ϕ \mathbb{E}_{\bm{\phi}} and 𝔼 ϕ ~ \mathbb{E}_{\tilde{\bm{\phi}}} . Then, we have that

[104] table: 𝔼 ⁡ [ ( ϕ ⊤ ​ 𝑬 ​ ϕ ~ ) 2 ] \displaystyle\mathbb{E}[(\bm{\phi}^{\top}{\bm{E}}\tilde{\bm{\phi}})^{2}] = 𝔼 ϕ ​ 𝔼 ϕ ~ ​ [ ϕ ~ ⊤ ​ 𝑬 ⊤ ​ ϕ ​ ϕ ⊤ ​ 𝑬 ​ ϕ ~ ] \displaystyle=\mathbb{E}_{\bm{\phi}}\mathbb{E}_{\tilde{\bm{\phi}}}\left[\tilde{\bm{\phi}}^{\top}{\bm{E}}^{\top}\bm{\phi}\bm{\phi}^{\top}{\bm{E}}\tilde{\bm{\phi}}\right] ≤ 𝔼 ϕ [ max ϕ ~ ∈ ℬ ( 1 ) ϕ ~ ⊤ ( 𝑬 ⊤ ϕ ϕ ⊤ 𝑬 ) ϕ ~ ] \displaystyle\leq\mathbb{E}_{\bm{\phi}}\left[\max_{\tilde{\bm{\phi}}\in{\mathcal{B}}^{(}1)}\tilde{\bm{\phi}}^{\top}({\bm{E}}^{\top}\bm{\phi}\bm{\phi}^{\top}{\bm{E}})\tilde{\bm{\phi}}\right] = 𝔼 ϕ ​ [ ‖ 𝑬 ​ ϕ ‖ 2 2 ] . \displaystyle=\mathbb{E}_{\bm{\phi}}\left[\left\lVert{\bm{E}}\bm{\phi}\right\rVert_{2}^{2}\right].

[105] p: Combining everything, we have

[106] table: X ≤ L μ 2 ​ ‖ π ^ − π ~ ‖ 1 ​ 𝔼 ϕ ​ [ ‖ 𝑬 ​ ϕ ‖ 2 ] + L μ 2 ​ 𝔼 ϕ ​ [ ‖ 𝑬 ​ ϕ ‖ 2 2 ] . {\color[rgb]{0.75,0.5,0.25}X}\leq\frac{L_{\mu}}{2}{\color[rgb]{1,0,1}\left\lVert\hat{\pi}-\tilde{\pi}\right\rVert_{1}}\mathbb{E}_{\bm{\phi}}[\left\lVert{\bm{E}}\bm{\phi}\right\rVert_{2}]+\frac{L_{\mu}}{2}\mathbb{E}_{\bm{\phi}}\left[\left\lVert{\bm{E}}\bm{\phi}\right\rVert_{2}^{2}\right]. (8)

[107] p: If we naïvely bound ‖ π ^ − π ~ ‖ 1 ≤ 1 {\color[rgb]{1,0,1}\left\lVert\hat{\pi}-\tilde{\pi}\right\rVert_{1}}\leq 1 , we recover the η {\color[rgb]{0.75,0,0.25}\eta} -independent bound.

[108] h4: Utilizing Strong Convexity.

[109] p: Our second key technical contribution is, instead of naïvely bounding ‖ π ^ − π ~ ‖ 1 ≤ 1 {\color[rgb]{1,0,1}\left\lVert\hat{\pi}-\tilde{\pi}\right\rVert_{1}}\leq 1 , we deal with it using the strong convexity of ψ \psi !

[110] p: The following lemma immediately follows from the β − 1 \beta^{-1} -strong convexity of ψ \psi :

[111] h6: Lemma 3.3 .

[112] p: J η ​ ( π ^ , ⋅ ) J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\cdot) is ( η ​ β ) − 1 ({\color[rgb]{0.75,0,0.25}\eta}\beta)^{-1} -strongly convex in ℓ 1 \ell_{1} -norm, i.e., for any π , π ~ ∈ Π \pi,\tilde{\pi}\in\Pi ,

[113] table: J η ​ ( π ^ , π ) − J η ​ ( π ^ , π ~ ) ≥ ⟨ ∇ π ~ J η ​ ( π ^ , π ~ ) , π − π ~ ⟩ + 1 2 ​ η ​ β ​ ‖ π − π ~ ‖ 1 2 . J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\pi)-J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\tilde{\pi})\geq\langle\nabla_{\tilde{\pi}}J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\tilde{\pi}),\pi-\tilde{\pi}\rangle+\frac{1}{2{\color[rgb]{0.75,0,0.25}\eta}\beta}{\color[rgb]{1,0,1}\left\lVert\pi-\tilde{\pi}\right\rVert_{1}^{2}}.

[114] p: Then, by the above lemma, we have:

[115] table: X \displaystyle{\color[rgb]{0.75,0.5,0.25}X} = J η ​ ( π ^ , π ^ ) − J η ​ ( π ^ , π ~ ) \displaystyle=J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\hat{\pi})-J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\tilde{\pi}) ≥ ⟨ ∇ π ~ J η ​ ( π ^ , π ~ ) , π ^ − π ~ ⟩ + 1 2 ​ η ​ β ​ ‖ π ^ − π ~ ‖ 1 2 \displaystyle\geq\langle\nabla_{\tilde{\pi}}J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi},\tilde{\pi}),\hat{\pi}-\tilde{\pi}\rangle+\frac{1}{2{\color[rgb]{0.75,0,0.25}\eta}\beta}{\color[rgb]{1,0,1}\left\lVert\hat{\pi}-\tilde{\pi}\right\rVert_{1}^{2}} ≥ 1 2 ​ η ​ β ​ ‖ π ^ − π ~ ‖ 1 2 . \displaystyle\geq\frac{1}{2{\color[rgb]{0.75,0,0.25}\eta}\beta}{\color[rgb]{1,0,1}\left\lVert\hat{\pi}-\tilde{\pi}\right\rVert_{1}^{2}}. (optimality condition 3 3 footnotemark: 3 )

[116] p: Plugging this back into Eqn. ( 8 ), we have:

[117] table: X ≤ L μ 2 ​ η ​ β 2 ​ 𝔼 ϕ ​ [ ‖ 𝑬 ​ ϕ ‖ 2 ] ​ X + L μ 2 ​ 𝔼 ϕ ​ [ ‖ 𝑬 ​ ϕ ‖ 2 2 ] . {\color[rgb]{0.75,0.5,0.25}X}\leq\sqrt{\frac{L_{\mu}^{2}{\color[rgb]{0.75,0,0.25}\eta}\beta}{2}}\mathbb{E}_{\bm{\phi}}[\left\lVert{\bm{E}}\bm{\phi}\right\rVert_{2}]\sqrt{{\color[rgb]{0.75,0.5,0.25}X}}+\frac{L_{\mu}}{2}\mathbb{E}_{\bm{\phi}}[\left\lVert{\bm{E}}\bm{\phi}\right\rVert_{2}^{2}]. (9)

[118] p: Note that this is a self-bounding quadratic inequality in X {\color[rgb]{0.75,0.5,0.25}X} , which can be solved as follows: 6 6 6 For b , c ≥ 0 b,c\geq 0 , x 2 ≤ b ​ x + c ⇒ x ≤ b + c x^{2}\leq bx+c\Rightarrow x\leq b+\sqrt{c} .

[119] table: X ≤ L μ 2 ​ η ​ β ​ 𝔼 ϕ ​ [ ‖ 𝑬 ​ ϕ ‖ 2 ] 2 + L μ ​ 𝔼 ϕ ​ [ ‖ 𝑬 ​ ϕ ‖ 2 2 ] . {\color[rgb]{0.75,0.5,0.25}X}\leq L_{\mu}^{2}{\color[rgb]{0.75,0,0.25}\eta}\beta\mathbb{E}_{\bm{\phi}}[\left\lVert{\bm{E}}\bm{\phi}\right\rVert_{2}]^{2}+L_{\mu}\mathbb{E}_{\bm{\phi}}[\left\lVert{\bm{E}}\bm{\phi}\right\rVert_{2}^{2}].

[120] p: We then conclude via Jensen’s inequality. ∎

[121] h3: 3.2 Proof of Lemma 3.2

[122] p: Because this is a key lemma that enabled the above proof to proceed smoothly, we are devoting a separate subsection to its proof. Here, the intuition is the right mix of symmetry ( μ ⁡ ( z ) + μ ⁡ ( − z ) = 1 \mu(z)+\mu(-z)=1 ) and skew-symmetry ( 𝑬 ⊤ = − 𝑬 {\bm{E}}^{\top}=-{\bm{E}} ), and somewhat surprisingly, variational representation of ‖ ⋅ ‖ 1 \left\lVert\cdot\right\rVert_{1} .

[123] p: First, note that

[124] table: Z \displaystyle Z ≜ 𝔼 ϕ , ϕ ~ ∼ π ^ ​ [ μ ˙ ​ ( ϕ ⊤ ​ 𝚯 ​ ϕ ~ ) ​ ϕ ⊤ ​ 𝑬 ​ ϕ ~ ] \displaystyle\triangleq\mathbb{E}_{\bm{\phi},\tilde{\bm{\phi}}\sim\hat{\pi}}\left[\dot{\mu}(\bm{\phi}^{\top}\bm{\Theta}\tilde{\bm{\phi}})\bm{\phi}^{\top}{\bm{E}}\tilde{\bm{\phi}}\right] = 𝔼 ϕ , ϕ ~ ∼ π ^ ​ [ μ ˙ ​ ( ϕ ~ ⊤ ​ 𝚯 ​ ϕ ) ​ ϕ ~ ⊤ ​ 𝑬 ​ ϕ ] \displaystyle=\mathbb{E}_{\bm{\phi},\tilde{\bm{\phi}}\sim\hat{\pi}}\left[\dot{\mu}(\tilde{\bm{\phi}}^{\top}\bm{\Theta}\bm{\phi})\tilde{\bm{\phi}}^{\top}{\bm{E}}\bm{\phi}\right] ( ϕ ​ = 𝑑 ​ ϕ ~ \bm{\phi}\overset{d}{=}\tilde{\bm{\phi}} ) = − 𝔼 ϕ , ϕ ~ ∼ π ^ ​ [ μ ˙ ​ ( ϕ ⊤ ​ 𝚯 ​ ϕ ~ ) ​ ϕ ⊤ ​ 𝑬 ​ ϕ ~ ] = − Z , \displaystyle=-\mathbb{E}_{\bm{\phi},\tilde{\bm{\phi}}\sim\hat{\pi}}\left[\dot{\mu}(\bm{\phi}^{\top}\bm{\Theta}\tilde{\bm{\phi}})\bm{\phi}^{\top}{\bm{E}}\tilde{\bm{\phi}}\right]=-Z, ( 𝑬 ∈ Skew ⁡ ( d ) {\bm{E}}\in\mathrm{Skew}(d) , μ ˙ ​ ( z ) = μ ˙ ​ ( − z ) \dot{\mu}(z)=\dot{\mu}(-z) )

[125] p: i.e., Z = 0 Z=0 .

[126] p: Let us denote f ⁡ ( ϕ ~ , ϕ ) := μ ˙ ​ ( ϕ ⊤ ​ 𝚯 ​ ϕ ~ ) ​ ϕ ⊤ ​ 𝑬 ​ ϕ ~ f(\tilde{\bm{\phi}};\bm{\phi}):=\dot{\mu}(\bm{\phi}^{\top}\bm{\Theta}\tilde{\bm{\phi}})\bm{\phi}^{\top}{\bm{E}}\tilde{\bm{\phi}} , which satisfies max ϕ ~ ∈ ℬ d ​ ( 1 ) ⁡ | f ⁡ ( ϕ ~ , ϕ ) | ≤ L μ ​ ‖ 𝑬 ​ ϕ ‖ 2 \max_{\tilde{\bm{\phi}}\in{\mathcal{B}}^{d}(1)}\left|f(\tilde{\bm{\phi}};\bm{\phi})\right|\leq L_{\mu}\left\lVert{\bm{E}}\bm{\phi}\right\rVert_{2} . Then,

[127] table: | 𝔼 ϕ ∼ π ^ , ϕ ~ ∼ π ~ ​ [ f ⁡ ( ϕ ~ , ϕ ) ] | \displaystyle\left|\mathbb{E}_{\bm{\phi}\sim\hat{\pi},\tilde{\bm{\phi}}\sim\tilde{\pi}}\left[f(\tilde{\bm{\phi}};\bm{\phi})\right]\right| = | 𝔼 ϕ ∼ π ^ , ϕ ~ ∼ π ~ ​ [ f ⁡ ( ϕ ~ , ϕ ) ] − Z | \displaystyle=\left|\mathbb{E}_{\bm{\phi}\sim\hat{\pi},\tilde{\bm{\phi}}\sim\tilde{\pi}}\left[f(\tilde{\bm{\phi}};\bm{\phi})\right]-Z\right| = | 𝔼 ϕ ∼ π ^ ​ [ 𝔼 ϕ ~ ∼ π ^ ​ [ f ⁡ ( ϕ ~ , ϕ ) ] − 𝔼 ϕ ~ ∼ π ~ ​ [ f ⁡ ( ϕ ~ , ϕ ) ] ] | \displaystyle=\left|\mathbb{E}_{\bm{\phi}\sim\hat{\pi}}\left[\mathbb{E}_{\tilde{\bm{\phi}}\sim\hat{\pi}}\left[f(\tilde{\bm{\phi}};\bm{\phi})\right]-\mathbb{E}_{\tilde{\bm{\phi}}\sim\tilde{\pi}}\left[f(\tilde{\bm{\phi}};\bm{\phi})\right]\right]\right| ≤ 𝔼 ϕ ∼ π ^ ​ [ | 𝔼 ϕ ~ ∼ π ^ ​ [ f ⁡ ( ϕ ~ , ϕ ) ] − 𝔼 ϕ ~ ∼ π ~ ​ [ f ⁡ ( ϕ ~ , ϕ ) ] | ] \displaystyle\leq\mathbb{E}_{\bm{\phi}\sim\hat{\pi}}\left[\left|\mathbb{E}_{\tilde{\bm{\phi}}\sim\hat{\pi}}\left[f(\tilde{\bm{\phi}};\bm{\phi})\right]-\mathbb{E}_{\tilde{\bm{\phi}}\sim\tilde{\pi}}\left[f(\tilde{\bm{\phi}};\bm{\phi})\right]\right|\right] ≤ ( ∗ ) ​ 𝔼 ϕ ∼ π ^ ​ [ L μ ​ ‖ 𝑬 ​ ϕ ‖ 2 ​ sup g ∈ 𝒢 ∞ ​ ( 1 ) | ∫ g ⁡ ( ϕ ~ ) ​ d ​ ( π ^ − π ~ ) ​ ( ϕ ~ ) | ] \displaystyle\overset{(*)}{\leq}\mathbb{E}_{\bm{\phi}\sim\hat{\pi}}\left[L_{\mu}\left\lVert{\bm{E}}\bm{\phi}\right\rVert_{2}\sup_{g\in{\mathcal{G}}_{\infty}(1)}\left|\int g(\tilde{\bm{\phi}})d(\hat{\pi}-\tilde{\pi})(\tilde{\bm{\phi}})\right|\right] = ( ∗ ∗ ) ​ L μ 2 ​ ‖ π ^ − π ~ ‖ 1 ​ 𝔼 ϕ ∼ π ^ ​ [ ‖ 𝑬 ​ ϕ ‖ 2 ] . \displaystyle\overset{(**)}{=}\frac{L_{\mu}}{2}{\color[rgb]{1,0,1}\left\lVert\hat{\pi}-\tilde{\pi}\right\rVert_{1}}\mathbb{E}_{\bm{\phi}\sim\hat{\pi}}\left[\left\lVert{\bm{E}}\bm{\phi}\right\rVert_{2}\right].

[128] p: where in ( ∗ ) (*) ,

[129] table: 𝒢 ∞ ( 1 ) := { g : ℬ d ( 1 ) → [ 0 , 1 ] ∣ g is measurable } , {\mathcal{G}}_{\infty}(1):=\left\{g:{\mathcal{B}}^{d}(1)\rightarrow[0,1]\mid\text{$g$ is measurable}\right\},

[130] p: and ( ∗ ∗ ) (**) follows from the integral probability metric representation of ‖ ⋅ ‖ 1 \left\lVert\cdot\right\rVert_{1} ( Müller, 1997 , Theorem 5.4) . ∎

[131] h2: 4 𝒪 ~ ​ ( η ​ ( log ⁡ T ) 2 ∧ T ) \tilde{{\mathcal{O}}}({\color[rgb]{0.75,0,0.25}\eta}(\log T)^{2}\wedge\sqrt{T}) via Greedy Sampling

[132] p: In this section, we assume that μ ⁡ ( z ) = ( 1 + e − z ) − 1 \mu(z)=(1+e^{-z})^{-1} , making the GLM well-specified as Bernoulli, for which a tight confidence sequence is known ( Lee et al., 2024a , Theorem 3.2) ; refer to Remark 4.1 for extensions to generic μ \mu that preserve the dependencies in d d and T T . Also, we ignore the low-rank structure of 𝚯 ⋆ \bm{\Theta}_{\star} to prioritize obtaining polylogarithmic regret; in Section 5 , we prioritize removing dependencies on d d at the cost of obtaining T \sqrt{T} regret.

[133] p: We show that a surprisingly simple algorithm is sufficient to obtain 𝒪 ~ ​ ( η ​ ( log ⁡ T ) 2 ∧ T ) \tilde{{\mathcal{O}}}(\eta(\log T)^{2}\wedge\sqrt{T}) : Greedy Sampling (GS) (see Algorithm 1 in Appendix A ). The max-player always plays the greedy NE policy w.r.t. the current MLE 𝚯 ^ t \widehat{\bm{\Theta}}_{t} , while the min-player explores with the given ρ \rho ( Assumption 1 ).

[134] p: Recently, Wu et al. (2025a) 7 7 7 Technically, their algorithm is intractable in GBPM , as it requires minimizing the cross-entropy loss over Skew ⁡ ( d , 2 ​ r , S ) \mathrm{Skew}(d,2r;S) . obtained 𝒪 ~ ​ ( e 9 ​ η ​ ( log ⁡ T ) 2 ) \tilde{{\mathcal{O}}}({\color[rgb]{0.5,0,0.5}e^{9\eta}}(\log T)^{2}) for GS . However, their bound scales exponentially with η \eta , is shown only for ψ ⁡ ( ⋅ ) = D KL ​ ( ⋅ , π r ​ e ​ f ) \psi(\cdot)=D_{\mathrm{KL}}(\cdot,\pi_{ref}) , and fails to yield a meaningful unregularized regret bound (e.g., as η → ∞ \eta\to\infty ); see Appendix F for detailed discussions. Our regret bound, in a similar spirit to Nayak et al. (2025, Theorem 2.1) , adapts to both regimes gracefully: it yields ( log ⁡ T ) 2 (\log T)^{2} for small η \eta , and transitions to T \sqrt{T} as η \eta increases. We defer further discussions of our regret bound to Section 6 .

[135] h6: Remark 4.1 (Beyond Parametric) .

[136] p: A bandit problem in which a specific parametric distribution (e.g., GLM) is assumed for the reward is known as a parametric bandit ( Filippi et al., 2010 ) . For the semi-parametric setting where we only assume that r t = μ ⁡ ( ⟨ 𝛉 ⋆ , ϕ t ⟩ ) + ε t r_{t}=\mu(\langle\bm{\theta}_{\star},\bm{\phi}_{t}\rangle)+\varepsilon_{t} with ε t \varepsilon_{t} being bounded noise, one can adopt the maximum quasi-likelihood estimator approach of Li et al. (2017, Lemma 3) , which dates back to Chen et al. (1999) . The strategy involves a T T -independent warm-up phase (random sampling) to ensure that the design matrix is sufficiently well-conditioned, thereby preserving the dependencies in d d and T T .

[137] h3: 4.1 Norm + Skew-Constrained MLE

[138] p: We now describe the estimator for GS . Let us denote vec : ℝ d × d → ℝ d 2 \mathrm{vec}:{\mathbb{R}}^{d\times d}\rightarrow{\mathbb{R}}^{d^{2}} as the (column-wise) vectorization operator, and mat ≜ vec − 1 : ℝ d 2 → ℝ d × d \mathrm{mat}\triangleq\mathrm{vec}^{-1}:{\mathbb{R}}^{d^{2}}\rightarrow{\mathbb{R}}^{d\times d} to be its inverse, namely, the matrization operator.

[139] p: We first define the following convex subset of ℝ d 2 {\mathbb{R}}^{d^{2}} : 8 8 8 Note that the norm constraint ‖ 𝜽 ‖ 2 ≤ S \left\lVert{\bm{\theta}}\right\rVert_{2}\leq S encompasses a larger constraint region than our nuclear norm constraint ‖ 𝚯 ‖ nuc ≤ S \left\lVert\bm{\Theta}\right\rVert_{\mathrm{nuc}}\leq S from Definition 2.2 , and is hence consistent.

[140] table: 𝒦 S := { 𝜽 ∈ ℝ d 2 : ‖ 𝜽 ‖ 2 ≤ S ​ and ​ mat ​ ( 𝜽 ) ⊤ = − mat ⁡ ( 𝜽 ) } . \mathcal{K}_{S}:=\left\{{\bm{\theta}}\in\mathbb{R}^{d^{2}}:\left\lVert{\bm{\theta}}\right\rVert_{2}\leq S\text{ and }\mathrm{mat}({\bm{\theta}})^{\top}=-\mathrm{mat}({\bm{\theta}})\right\}.

[141] p: Taking inspiration from Lee et al. (2024b) ; Lee et al. (2024a) , we employ the maximum likelihood estimator (MLE) constrained to 𝒦 S {\mathcal{K}}_{S} . Denoting 𝒗 t := vec ⁡ ( ϕ t 2 ​ ( ϕ t 1 ) ⊤ ) ∈ ℝ d 2 {\bm{v}}_{t}:=\mathrm{vec}(\bm{\phi}_{t}^{2}(\bm{\phi}_{t}^{1})^{\top})\in{\mathbb{R}}^{d^{2}} ,

[142] table: 𝚯 ^ t ← mat ⁡ ( 𝜽 ^ t ) , 𝜽 ^ t ← arg ​ min 𝜽 ∈ 𝒦 S ⁡ ℒ t ​ ( 𝜽 ) , \displaystyle\widehat{\bm{\Theta}}_{t}\leftarrow\mathrm{mat}(\hat{{\bm{\theta}}}_{t}),\quad\hat{{\bm{\theta}}}_{t}\leftarrow\argmin_{{\bm{\theta}}\in{\mathcal{K}}_{S}}{\mathcal{L}}_{t}({\bm{\theta}}), (10) ℒ t ​ ( 𝜽 ) := ∑ s = 1 t − 1 { m ⁡ ( ⟨ 𝜽 , 𝒗 s ⟩ ) − r s ​ ⟨ 𝜽 , 𝒗 s ⟩ } , \displaystyle{\mathcal{L}}_{t}({\bm{\theta}}):=\sum_{s=1}^{t-1}\left\{m(\langle{\bm{\theta}},{\bm{v}}_{s}\rangle)-r_{s}\langle{\bm{\theta}},{\bm{v}}_{s}\rangle\right\}, (11)

[143] p: where m ⁡ ( ⋅ ) m(\cdot) is the log-partition function ( Wainwright and Jordan, 2008 ) such that m ′ = μ m^{\prime}=\mu .

[144] p: With this, we now present our regularized regret bound:

[145] h6: Theorem 4.2 .

[146] p: We highlight three important remarks regarding this result.

[147] p: First , as claimed earlier, our regret bounds are indeed free of e 𝒪 ⁡ ( η ) {\color[rgb]{0.75,0,0.25}e^{{\mathcal{O}}(\eta)}} factors, albeit at the cost of C min − 1 C_{\min}^{-1} and the additional feature diversity assumption ( Assumption 1 ). We emphasize that C min − 1 C_{\min}^{-1} is a quantity strictly independent of the regularizer or its strength η {\color[rgb]{0.75,0,0.25}\eta} ; it is determined solely by the geometry of the arm-set and how well-conditioned it is. Consequently, for well-conditioned arm-sets where C min − 1 = Θ ⁡ ( 1 ) C_{\min}^{-1}=\Theta(1) (e.g., hypercubes), this dependence is benign.

[148] p: Second , as detailed in Section B.4 , we can completely bypass the feature diversity assumption for specific choices of ψ ⁡ ( ⋅ ) \psi(\cdot) . In these cases, the same guarantees hold with C min − 1 C_{\min}^{-1} replaced by a function of η {\color[rgb]{0.75,0,0.25}\eta} . Specifically, when ψ ⁡ ( ⋅ ) = D KL ​ ( ⋅ , π ref ) \psi(\cdot)=D_{\mathrm{KL}}(\cdot,\pi_{\mathrm{ref}}) (reverse KL-regularization, Wu et al. (2025a) ), ψ ⁡ ( ⋅ ) = D χ 2 ​ ( ⋅ , π ref ) \psi(\cdot)=D_{\chi^{2}}(\cdot,\pi_{\mathrm{ref}}) (chi-squared, Huang et al. (2025a) ), or ψ ⁡ ( ⋅ ) = D KL ​ ( ⋅ , π ref ) + D χ 2 ​ ( ⋅ , π ref ) \psi(\cdot)=D_{\mathrm{KL}}(\cdot,\pi_{\mathrm{ref}})+D_{\chi^{2}}(\cdot,\pi_{\mathrm{ref}}) (mixed chi-squared, Huang et al. (2025b) ) for some fixed π ref ∈ Π \pi_{\mathrm{ref}}\in\Pi , the C min − 1 C_{\min}^{-1} term is replaced by e η {\color[rgb]{0.75,0,0.25}e^{\eta}} , η {\color[rgb]{0.75,0,0.25}\eta} , and 1 + η {\color[rgb]{0.75,0,0.25}1+\eta} , respectively. Although we still incur an e η {\color[rgb]{0.75,0,0.25}e^{\eta}} factor for reverse KL-regularization, this remains a notable improvement over the e 9 ​ η {\color[rgb]{0.75,0,0.25}e^{9\eta}} dependency in Wu et al. (2025a) . Furthermore, while our theoretical framework gracefully accommodates any strongly convex regularizer, it remains unclear whether the analysis of Wu et al. (2025a) can easily extend beyond reverse KL.

[149] p: Third , our regret guarantees extend to ABR ​ - ​ Reg ​ ( T ) \mathrm{ABR\text{-}Reg}(T) via symmetric play under reverse KL-regularization D KL ​ ( ⋅ , π ref ) D_{\mathrm{KL}}(\cdot,\pi_{\mathrm{ref}}) , provided ρ = π ref \rho=\pi_{\mathrm{ref}} . Ensuring diversity when both players act greedily incurs an additional η {\color[rgb]{0.75,0,0.25}\eta} -dependent factor as we need to invoke Proposition B.5 twice (see Section B.4 ).

[150] h3: 4.2 Proof Sketch of Theorem 4.2

[151] p: We provide a high-level sketch of the proof here; the full detailed proof is deferred to Appendix B .

[152] p: The analysis proceeds in three main steps:

[153] h4: 1. From Regret to Sum of Squared Errors.

[154] p: We begin with the instantaneous regret bound established in Theorem 3.1 , which bounds the instantaneous dual gap by the squared estimation error: DGap ⁡ ( π ^ t ) ≲ 𝔼 ϕ ∼ π ^ t ​ [ ‖ 𝑬 t ​ ϕ ‖ 2 2 ] \mathrm{DGap}({\color[rgb]{0,0,1}\hat{\pi}_{t}})\lesssim\mathbb{E}_{{\color[rgb]{0,0,1}\bm{\phi}\sim\hat{\pi}_{t}}}[\|{\bm{E}}_{t}\bm{\phi}\|_{2}^{2}] . Using a standard basis decomposition, Cauchy-Schwarz w.r.t. the regularized Hessian of the log-likelihood loss 𝑯 ^ t ≜ 𝑰 d 2 + ∇ 2 ℒ t ​ ( 𝜽 ^ t ) ∈ ℝ d 2 × d 2 \widehat{{\bm{H}}}_{t}\triangleq{\bm{I}}_{d^{2}}+\nabla^{2}{\mathcal{L}}_{t}(\hat{{\bm{\theta}}}_{t})\in{\mathbb{R}}^{d^{2}\times d^{2}} , and the confidence sequence for the constrained MLE ( Lee et al., 2024a , Theorem 3.2) , we further bound this error by the sum of expected elliptical potentials. Here, one side is the standard basis 𝒆 j {\bm{e}}_{j} and the other is chosen by π ^ t {\color[rgb]{0,0,1}\hat{\pi}_{t}} :

[155] table: DGap ⁡ ( π ^ t ) ≲ ( d 2 ​ log ⁡ T ) ​ ∑ j = 1 d 𝔼 ϕ ∼ π ^ t ​ [ ‖ ϕ ⊗ 𝒆 j ‖ 𝑯 ^ t − 1 2 ] . \mathrm{DGap}({\color[rgb]{0,0,1}\hat{\pi}_{t}})\lesssim(d^{2}\log T)\sum_{j=1}^{d}\mathbb{E}_{{\color[rgb]{0,0,1}\bm{\phi}\sim\hat{\pi}_{t}}}\left[\left\lVert{\color[rgb]{0,0,1}\bm{\phi}}\otimes{\color[rgb]{1,0,0}{\bm{e}}_{j}}\right\rVert_{\widehat{{\bm{H}}}_{t}^{-1}}^{2}\right].

[156] h4: 2. Towards Expected Elliptical Potentials.

[157] p: A discrepancy arises in the RHS: the upper bound involves a sum over fixed basis vectors on one side, whereas the empirical Hessian aggregates the played features on both sides. We resolve this via our Coverage Lemma ( Lemma B.2 ). Leveraging the feature diversity assumption ( Assumption 1 ), ∑ t DGap ⁡ ( π ^ t ) \sum_{t}\mathrm{DGap}({\color[rgb]{0,0,1}\hat{\pi}_{t}}) is bounded by

[158] table: ( d 2 ​ log ⁡ T ) ​ C min − 1 ​ ∑ t = 1 T 𝔼 ϕ t ∼ π ^ t , ϕ ~ t ∼ ρ ​ [ ‖ vec ⁡ ( ϕ t ​ ϕ ~ t ⊤ ) ‖ 𝑯 ^ t − 1 2 ] ⏟ ≜ S T . (d^{2}\log T)C_{\min}^{-1}\underbrace{\sum_{t=1}^{T}\mathbb{E}_{{\color[rgb]{0,0,1}\bm{\phi}_{t}\sim\hat{\pi}_{t}},{\color[rgb]{1,0,0}\tilde{\bm{\phi}}_{t}\sim\rho}}\left[\left\lVert\mathrm{vec}({\color[rgb]{0,0,1}\bm{\phi}_{t}}{\color[rgb]{1,0,0}\tilde{\bm{\phi}}_{t}}^{\top})\right\rVert_{\widehat{{\bm{H}}}_{t}^{-1}}^{2}\right]}_{\triangleq{\color[rgb]{0.75,0.5,0.25}S_{T}}}.

[159] h4: 3. Martingale Concentration for Realized Variance.

[160] p: The final challenge is to bound the sum of expected elliptical potentials S T {\color[rgb]{0.75,0.5,0.25}S_{T}} . The standard Elliptical Potential Lemma ( Abbasi-Yadkori et al., 2011 , Lemma 11) controls the sum of realized potentials. To bridge this gap, we decompose the term into the realized sum plus a sum of martingale differences . Applying Freedman’s inequality ( Freedman, 1975 ; Beygelzimer et al., 2011 ; Lee et al., 2024b ) , we derive a linear self-bounding inequality of the form:

[161] table: S T ≤ A ​ S T + 𝒪 ~ ​ ( d 2 ​ log ⁡ T ) , {\color[rgb]{0.75,0.5,0.25}S_{T}}\leq A{\color[rgb]{0.75,0.5,0.25}S_{T}}+\tilde{\mathcal{O}}(d^{2}\log T),

[162] p: where A < 1 A<1 is a constant. Solving this recursion yields the final 𝒪 ~ ​ ( d 4 ​ ( log ⁡ T ) 2 ) \tilde{\mathcal{O}}(d^{4}(\log T)^{2}) rate. ∎

[163] h2: 5 poly ⁡ ( d ) \mathrm{poly}(d) -free 𝒪 ~ ​ ( η ​ T ∧ T 2 3 ) \tilde{{\mathcal{O}}}(\sqrt{{\color[rgb]{0.75,0,0.25}\eta}T}\wedge T^{\frac{2}{3}}) via ETC

[164] h4: High-Dimensional Regime.

[165] p: We now ask, what gains can we obtain if we maximally exploit the low-rank structure of 𝚯 ⋆ \bm{\Theta}_{\star} . This question is particularly relevant in the high-dimensional or data-poor regime, where T T is not sufficiently large relative to d d (specifically, d c 1 ≲ T ≲ d c 2 d^{c_{1}}\lesssim T\lesssim d^{c_{2}} for constants 0 < c 1 < c 2 0<c_{1}<c_{2} ); this is characteristic of modern applications involving high-dimensional features ( Tucker et al., 2020 ; Li et al., 2024 ) . Here, it is imperative to avoid explicit poly ⁡ ( d ) \mathrm{poly}(d) dependencies in the regret bound, up to unavoidable dependencies on the C min − 1 C_{\min}^{-1} ( Assumption 1 ) ( Zeng and Honorio, 2025 , Table 1) . To achieve this, we leverage the intrinsic low-rank structure of 𝚯 ⋆ \bm{\Theta}_{\star} , a standard approach in high-dimensional bandits ( Carpentier and Munos, 2012 ; Hao et al., 2020 ; Kim and Paik, 2019 ; Oh et al., 2021 ; Li et al., 2022b ; Lu et al., 2021 ; Kang et al., 2022 ; Jang et al., 2022 ; Jang et al., 2024 ) . In this regime, sufficient exploration is requisite to identify and exploit the underlying low-rank structure.

[166] h4: Explore-Then-Commit (ETC).

[167] p: Following standard practice in high-dimensional bandits ( Hao et al., 2020 ; Li et al., 2022b ; Jang et al., 2024 ) , we employ Explore-Then-Commit ( ETC ): the players explore for T 0 T_{0} rounds using ρ \rho , compute a SNE for the resulting estimator, and symmetrically commit to it for the remaining rounds (see Algorithm 2 in Appendix A ). Since both players adhere to the same dynamics (symmetric self-play), our bound on MBR ​ - ​ Reg η ​ ( T ) \mathrm{MBR\text{-}Reg}_{\color[rgb]{0.75,0,0.25}\eta}(T) implies the same for 1 2 ​ ABR ​ - ​ Reg η ​ ( T ) \frac{1}{2}\mathrm{ABR\text{-}Reg}_{\color[rgb]{0.75,0,0.25}\eta}(T) .

[168] h6: Remark 5.1 (Unknown T T ) .

[169] p: We assume T T is known to optimally tune T 0 T_{0} . If T T is unknown, the standard doubling trick ( Auer et al., 1995 ; Besson and Kaufmann, 2018 ) yields the same regret bound up to a constant factor.

[170] h3: 5.1 Nuclear-Norm Regularized MLE and Regret Bound

[171] p: We employ the nuclear-norm regularized MLE ( Fan et al., 2019 ; Lee et al., 2025 ) . Denoting the outer product of features as 𝑿 t := ϕ ⁡ ( 𝒙 t , 𝒂 t 1 ) ​ ϕ ​ ( 𝒙 t , 𝒂 t 2 ) ⊤ {\bm{X}}_{t}:=\bm{\phi}({\bm{x}}_{t},{\bm{a}}_{t}^{1})\bm{\phi}({\bm{x}}_{t},{\bm{a}}_{t}^{2})^{\top} :

[172] table: 𝚯 ^ T 0 \displaystyle\widehat{\bm{\Theta}}_{T_{0}} ← arg ​ min 𝚯 ∈ Skew ⁡ ( d ) ⁡ ℒ T 0 ​ ( 𝚯 ) + λ T 0 ​ ‖ 𝚯 ‖ nuc , \displaystyle\leftarrow\argmin_{\bm{\Theta}\in\mathrm{Skew}(d)}{\mathcal{L}}_{T_{0}}(\bm{\Theta})+\lambda_{T_{0}}\left\lVert\bm{\Theta}\right\rVert_{\mathrm{nuc}}, (12) ℒ T 0 ​ ( 𝚯 ) \displaystyle{\mathcal{L}}_{T_{0}}(\bm{\Theta}) : = 1 T 0 ​ ∑ t = 1 T 0 { m ⁡ ( ⟨ 𝚯 , 𝑿 t ⟩ ) − r t ​ ⟨ 𝚯 , 𝑿 t ⟩ } . \displaystyle:=\frac{1}{T_{0}}\sum_{t=1}^{T_{0}}\left\{m(\langle\bm{\Theta},{\bm{X}}_{t}\rangle)-r_{t}\langle\bm{\Theta},{\bm{X}}_{t}\rangle\right\}. (13)

[173] p: We now present the regret bound for ETC , with the full proof deferred to Appendix C :

[174] h6: Theorem 5.2 .

[175] p: Remarkably, thanks to the quadratic improvement from Theorem 3.1 , ETC achieves 𝒪 ~ ​ ( η ​ T ) \tilde{{\mathcal{O}}}(\sqrt{{\color[rgb]{0.75,0,0.25}\eta}T}) —surpassing the usual 𝒪 ~ ​ ( T 2 / 3 ) \tilde{{\mathcal{O}}}(T^{2/3}) rate typically associated with ETC ( Lattimore and Szepesvári, 2020 ) . Importantly, both bounds are free of explicit poly ⁡ ( d ) \mathrm{poly}(d) dependencies. We note that the tightness of these bounds depends on the regularization coefficient η {\color[rgb]{0.75,0,0.25}\eta} . Specifically, focusing on η , d , T {\color[rgb]{0.75,0,0.25}\eta},d,T , the 𝒪 ~ ​ ( η ​ T ) \tilde{{\mathcal{O}}}(\sqrt{{\color[rgb]{0.75,0,0.25}\eta}T}) bound dominates the usual rate whenever η ≲ ( T / log ⁡ d ) 1 3 {\color[rgb]{0.75,0,0.25}\eta}\lesssim(T/\log d)^{\frac{1}{3}} .

[176] h6: Remark 5.3 ( κ \kappa vs. κ ⋆ \kappa_{\star} ) .

[177] p: Readers familiar with recent advances in logistic and generalized linear bandits ( Abeille et al., 2021 ; Russac et al., 2021 ; Lee et al., 2024a ) may wonder whether the worst-case curvature κ \kappa can be replaced with a more favorable, instance-specific κ ⋆ := min ϕ , ϕ ′ ∈ ℬ d ​ ( 1 ) ⁡ μ ˙ ​ ( ϕ ⊤ ​ 𝚯 ⋆ ​ ϕ ′ ) . \kappa_{\star}:=\min_{\bm{\phi},\bm{\phi}^{\prime}\in\mathcal{B}^{d}(1)}\dot{\mu}\left(\bm{\phi}^{\top}\bm{\Theta}_{\star}\bm{\phi}^{\prime}\right). In Appendix C , we show that under the additional assumption that the link function μ \mu is self-concordant, this improvement is indeed achievable.

[178] h2: 6 Relations to Prior Works

[179] p: For the remainder of this section, for simplicity, we assume that 𝒳 = { 𝒙 } {\mathcal{X}}=\{{\bm{x}}\} and omit any dependency on the context.

[180] h4: Contextual General Preference Learning.

[181] p: Real-world contexts exhibit high diversity, spanning recommender systems ( Li et al., 2010 ) to mobile edge computing ( Chen and Xu, 2019 ) . While recent works have introduced contextual bandit frameworks for general preference learning ( Yang et al., 2025 ; Nayak et al., 2025 ; Wu et al., 2024 ) , they predominantly rely on item pair-wise feature maps (linearizing payoffs as ⟨ φ ⁡ ( 𝒂 1 , 𝒂 2 ) , 𝜽 ⟩ \langle\varphi({\bm{a}}^{1},{\bm{a}}^{2}),{\bm{\theta}}\rangle for each pair of actions 𝒂 1 , 𝒂 2 ∈ 𝒜 {\bm{a}}^{1},{\bm{a}}^{2}\in{\mathcal{A}} ) or tabular structures ( O’Donoghue et al., 2021 ) ; the former is conceptually similar to Wu et al. (2024) , though the connection is not explicitly drawn in the literature. This formulation contrasts with practical RLHF scenarios where only item-wise features ϕ ⁡ ( 𝒂 ) \phi({\bm{a}}) are available, further motivating our choice of GBPM as the primary object of study. Additionally, unlike their approaches which scale with | 𝒜 | 2 |{\mathcal{A}}|^{2} (rendering them intractable for infinite 𝒜 {\mathcal{A}} ), we only track the NE policy and the d × d d\times d parameter, which is efficient.

[182] h4: Beyond KL-Regularization via Self-Bounding Analysis.

[183] p: The theoretical landscape of RLHF is currently dominated by reverse KL-regularization ( Xiong et al., 2024 ; Zhao et al., 2025b ; Zhao et al., 2025a ; Wu et al., 2025a ) , often leveraging KL-specific properties of the exponential family (e.g., bounded log-density ratios) to enable oracle reductions to least square regressions ( Cesa-Bianchi and Lugosi, 2006 ; Foster and Rakhlin, 2020 ; Zhang, 2022 ) ; see Appendix F for an illustration where we rigorously instantiate the regret bound of Wu et al. (2025a) to GBPM . We show that the specific geometry of KL is not strictly necessary for fast rates; rather, the strong convexity of the regularizer drives our results. This covers various regularizers: Shannon entropy ( McKelvey and Palfrey, 1995 ; Mertikopoulos and Sandholm, 2016 ; Cen et al., 2024 ) , Tsallis entropy ( Tsallis, 1988 ; Lee et al., 2018 ; Yang et al., 2019 ; Zimmert and Seldin, 2021 ) , χ 2 \chi^{2} -divergence ( Huang et al., 2025b ) , and f f -divergences ( Liese and Vajda, 2006 ; Go et al., 2023 ; Wang et al., 2024 ; Han et al., 2025 ) .

[184] p: The key theme of our proof is a self-bounding inequality (Eqn. ( 9 )), a technique inspired from the generalized linear bandits literature ( Abeille et al., 2021 ; Lee et al., 2024a ) that exploits the landscape curvature to penalize deviations. The high-level intuition is similar, but with different technical components: such strong convexity ensures that the deviations are penalized more heavily, enabling tighter control over the dual gap ( Theorem 3.1 ).

[185] p: While generic formulations have appeared in recent works such as Tang et al. (2025) , rigorous statistical guarantees have been absent. Crucially, our analysis unifies these diverse regularizers in the online setting: we demonstrate that any strongly convex regularizer yields polylogarithmic regret, suggesting that the specific geometry of KL is not the sole driver of fast rates. This stands in contrast to offline RL, where distinct divergences can induce significant differences in learnability ( Jiang and Xie, 2025 ; Huang et al., 2025b ; Zhao et al., 2025c ) . For instance, Huang et al. (2025b) showed that χ 2 \chi^{2} -divergence (unlike KL) allows for single-policy concentratability, and recently, Zhao et al. (2025c) showed that with f f -divergence regularizer with strongly convex f f , a fast rate can be shown without single-policy concentratability. We leave to future work on instantiating and expanding these results to offline RLHF in GBPM .

[186] h4: Feature Diversity Assumption.

[187] p: Similar assumptions on the diversity of the feature mapping have been considered in the vast literature on greedy sampling for contextual bandits ( Goldenshluger and Zeevi, 2013 ; Kannan et al., 2018 ; Wu et al., 2020 ; Bastani et al., 2021 ; Bogunovic et al., 2021 ; Kim and Oh, 2024 ) . Under such conditions, in which exploration is naturally facilitated, near-optimal performance of order 𝒪 ⁡ ( poly ​ log ⁡ T ) {\mathcal{O}}(\mathrm{poly}\log T) has been shown, which we also obtain for our GS . We further note that the literature on semi-parametric generalized linear bandits relies on similar assumptions ( Li et al., 2017 ; Ding et al., 2021 ; Wu et al., 2024 ) to facilitate exploration via T T -independent phases. Crucially, this assumption is standard in the high-dimensional contextual bandit scenario ( Hao et al., 2020 ; Li et al., 2022b ; Zeng and Honorio, 2025 ) and is known to be unavoidable for ensuring the learnability of unknown succinct parameters without explicit poly ⁡ ( d ) \mathrm{poly}(d) dependencies ( Zeng and Honorio, 2025 , Table 1) . In this regime, the intuition is that sufficient exploration of the feature space is requisite to identify the underlying low-rank structure to be exploited. We lastly remark that for specific choices of the regularizer ψ ⁡ ( ⋅ ) \psi(\cdot) , this assumption can be completely bypassed. As detailed in Section B.4 , the cost of this circumvention is replacing the geometry-dependent factor C min − 1 C_{\min}^{-1} with an additional η {\color[rgb]{0.75,0,0.25}\eta} -dependent factor (e.g., e η {\color[rgb]{0.75,0,0.25}e^{\eta}} for reverse KL or η {\color[rgb]{0.75,0,0.25}\eta} for chi-squared regularization), allowing our guarantees to hold even in the absence of feature diversity assumption.

[188] h2: 7 Conclusion

[189] p: We have established a statistical framework for regularized online RLHF under the Generalized Bilinear Preference Model (GBPM) for any choice of strongly convex regularizer, which subsumes the standard reverse KL-regularization. By leveraging the skew-symmetry of the preferences and the strong convexity of the regularizer, we derive a novel self-bounding quadratic inequality for the dual gap, which serves as the cornerstone of our analysis. Under the feature diversity assumption, we proved that a simple Greedy Sampling strategy attains a polylogarithmic regret of 𝒪 ~ ​ ( η ​ d 4 ​ ( log ⁡ T ) 2 ) \tilde{\mathcal{O}}({\color[rgb]{0.75,0,0.25}\eta}d^{4}(\log T)^{2}) without exp ⁡ ( 𝒪 ⁡ ( η ) ) {\color[rgb]{0.75,0,0.25}\exp({\mathcal{O}}(\eta))} dependency, partially addressing an open problem by Wu et al. (2025a) . Furthermore, addressing the high-dimensional regime, we demonstrated that Explore-Then-Commit achieves a poly ​ ( d ) \text{poly}(d) -free regret of 𝒪 ~ ​ ( η ​ r ​ T ) \tilde{\mathcal{O}}(\sqrt{{\color[rgb]{0.75,0,0.25}\eta}rT}) by effectively exploiting the low-rank structure of the underlying preference matrix. We believe that this opens up various future directions, which we discuss in detail in Appendix H .

[190] h2: Impact Statement

[191] p: This paper presents work whose goal is to advance the field of Machine Learning. There are many potential societal consequences of our work, none which we feel must be specifically highlighted here.

[192] h2: References

[193] h6: Contents

[194] h2: Appendix A Pseudocodes for Greedy Sampling and Explore-Then-Commit

[195] figure: Algorithm 1 Greedy Sampling Input: Exploration policy ρ \rho ; 1 Initialize π ^ 1 ← ρ \hat{\pi}_{1}\leftarrow\rho ; 2 for t = 1 , 2 , ⋯ , T t=1,2,\cdots,T do 3 Observe a 𝒙 t ∼ d 0 {\bm{x}}_{t}\sim d_{0} ; 4 Sample 𝒂 t 1 ∼ π ^ t ( ⋅ | 𝒙 t ) {\color[rgb]{0,0,1}{\bm{a}}_{t}^{1}}\sim\hat{\pi}_{t}(\cdot|{\bm{x}}_{t}) and 𝒂 t 2 ∼ ρ ( ⋅ | 𝒙 t ) {\color[rgb]{1,0,0}{\bm{a}}_{t}^{2}}\sim\rho(\cdot|{\bm{x}}_{t}) ; 5 Observe r t := 𝟙 [ 𝒂 t 1 ≻ 𝒂 t 2 ] ∼ Ber ( μ ( ϕ t 1 ⊤ 𝚯 ⋆ ϕ t 2 ) ∣ 𝒙 t ) r_{t}:=\mathds{1}[{\color[rgb]{0,0,1}{\bm{a}}_{t}^{1}}\succ{\color[rgb]{1,0,0}{\bm{a}}_{t}^{2}}]\sim\mathrm{Ber}(\mu({\color[rgb]{0,0,1}\phi_{t}^{1}}^{\top}\bm{\Theta}_{\star}{\color[rgb]{1,0,0}\phi_{t}^{2}})\mid{\bm{x}}_{t}) , where ϕ t i := ϕ ⁡ ( 𝒙 t , 𝒂 t i ) \phi_{t}^{i}:=\phi({\bm{x}}_{t},{\bm{a}}_{t}^{i}) ; 6 Compute an estimator 𝚯 ^ t ∈ Skew ⁡ ( d ) \widehat{\bm{\Theta}}_{t}\in\mathrm{Skew}(d) ; 7 8 Compute a (symmetric) Nash equilibrium: π ^ t + 1 ← arg ​ max π 1 ∈ Π ⁡ min π 2 ∈ Π ​ J η ​ ( π 1 , π 2 , 𝚯 ^ t ) . \hat{\pi}_{t+1}\leftarrow\argmax_{\pi^{1}\in\Pi}\min_{\pi^{2}\in\Pi}J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1},\pi^{2};\widehat{\bm{\Theta}}_{t}). (14)

[196] figure: Algorithm 2 Explore-Then-Commit Input: Exploration policy ρ \rho and budget T 0 T_{0} ; 1 for t = 1 , 2 , ⋯ , T 0 t=1,2,\cdots,T_{0} do 2 Observe a 𝒙 t ∼ d 0 {\bm{x}}_{t}\sim d_{0} ; 3 Sample 𝒂 t 1 ∼ ρ ( ⋅ | 𝒙 t ) {\color[rgb]{0,0,1}{\bm{a}}_{t}^{1}}\sim\rho(\cdot|{\bm{x}}_{t}) and 𝒂 t 2 ∼ ρ ( ⋅ | 𝒙 t ) {\color[rgb]{1,0,0}{\bm{a}}_{t}^{2}}\sim\rho(\cdot|{\bm{x}}_{t}) ; 4 Observe r t := 𝟙 [ 𝒂 t 1 ≻ 𝒂 t 2 ] ∼ Ber ( μ ( ϕ t 1 ⊤ 𝚯 ⋆ ϕ t 2 ) ∣ 𝒙 t ) r_{t}:=\mathds{1}[{\color[rgb]{0,0,1}{\bm{a}}_{t}^{1}}\succ{\color[rgb]{1,0,0}{\bm{a}}_{t}^{2}}]\sim\mathrm{Ber}(\mu({\color[rgb]{0,0,1}\phi_{t}^{1}}^{\top}\bm{\Theta}_{\star}{\color[rgb]{1,0,0}\phi_{t}^{2}})\mid{\bm{x}}_{t}) , where ϕ t i := ϕ ⁡ ( 𝒙 t , 𝒂 t i ) \phi_{t}^{i}:=\phi({\bm{x}}_{t},{\bm{a}}_{t}^{i}) ; 5 Compute an estimator 𝚯 ^ ∈ Skew ⁡ ( d ) \widehat{\bm{\Theta}}\in\mathrm{Skew}(d) ; 6 Compute a (symmetric) Nash equilibrium: π ^ ← arg ​ max π 1 ∈ Π ⁡ min π 2 ∈ Π ​ J η ​ ( π 1 , π 2 , 𝚯 ^ ) \hat{\pi}\leftarrow\argmax_{\pi^{1}\in\Pi}\min_{\pi^{2}\in\Pi}J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1},\pi^{2};\widehat{\bm{\Theta}}) (15) 7 for t = T 0 + 1 , ⋯ , T t=T_{0}+1,\cdots,T do 8 Symmetrically commit to ( π ^ , π ^ ) (\hat{\pi},\hat{\pi}) ;

[197] h2: Appendix B Proof of Theorem 4.2 : Regret Bound of Greedy Sampling

[198] h3: B.1 Main Proof

[199] p: We will use several properties of the Kronecker product ⊗ \otimes throughout the proof; see Minka (1997) for a reference.

[200] h4: Part I. 𝒪 ~ ​ ( η ​ β ​ ( log ⁡ T ) 2 ) \tilde{{\mathcal{O}}}({\color[rgb]{0.75,0,0.25}\eta}\beta(\log T)^{2}) Regret Bound.

[201] p: To mirror the proof sketch in the main text, we divide the proof into three parts.

[202] p: 1. From Regret to Sum of Squared Errors. Recall that with 𝒗 t := vec ⁡ ( ϕ t 2 ​ ( ϕ t 1 ) ⊤ ) ∈ ℝ d 2 {\bm{v}}_{t}:=\mathrm{vec}(\bm{\phi}_{t}^{2}(\bm{\phi}_{t}^{1})^{\top})\in{\mathbb{R}}^{d^{2}} , our MLE is defined as follows:

[203] table: 𝚯 ^ t ← mat ⁡ ( 𝜽 ^ t ) , 𝜽 ^ t ← arg ​ min 𝜽 ∈ 𝒦 S ⁡ ℒ t ​ ( 𝜽 ) , ℒ t ​ ( 𝜽 ) := ∑ s = 1 t − 1 { m ⁡ ( ⟨ 𝜽 , 𝐯 t ⟩ ) − r t ​ ⟨ 𝜽 , 𝐯 t ⟩ } , \widehat{\bm{\Theta}}_{t}\leftarrow\mathrm{mat}(\hat{{\bm{\theta}}}_{t}),\quad\hat{{\bm{\theta}}}_{t}\leftarrow\argmin_{{\bm{\theta}}\in{\mathcal{K}}_{S}}{\mathcal{L}}_{t}({\bm{\theta}}),\quad{\mathcal{L}}_{t}({\bm{\theta}}):=\sum_{s=1}^{t-1}\left\{m(\langle{\bm{\theta}},{\bm{v}}_{t}\rangle)-r_{t}\langle{\bm{\theta}},{\bm{v}}_{t}\rangle\right\}, (16)

[204] p: where

[205] table: 𝒦 S := { 𝜽 ∈ ℝ d 2 : ‖ 𝜽 ‖ 2 ≤ S ​ and ​ mat ​ ( 𝜽 ) ⊤ = − mat ⁡ ( 𝜽 ) } . \mathcal{K}_{S}:=\left\{{\bm{\theta}}\in\mathbb{R}^{d^{2}}:\left\lVert{\bm{\theta}}\right\rVert_{2}\leq S\text{ and }\mathrm{mat}({\bm{\theta}})^{\top}=-\mathrm{mat}({\bm{\theta}})\right\}.

[206] p: As μ ⁡ ( z ) = ( 1 + e − z ) − 1 \mu(z)=(1+e^{-z})^{-1} for our proof, this implies that R s = 1 R_{s}=1 and L μ = 1 4 L_{\mu}=\frac{1}{4} .

[207] p: Let us denote the regularized Hessian of ℒ t ​ ( ⋅ ) {\mathcal{L}}_{t}(\cdot) at the MLE 𝜽 ^ t \hat{{\bm{\theta}}}_{t} as

[208] table: 𝑯 ^ t := 𝑰 d 2 + ∑ s = 1 t − 1 μ ˙ ​ ( ⟨ 𝜽 ^ t , 𝒗 t ⟩ ) ​ 𝒗 t ​ 𝒗 t ⊤ . \widehat{{\bm{H}}}_{t}:={\bm{I}}_{d^{2}}+\sum_{s=1}^{t-1}\dot{\mu}(\langle\hat{{\bm{\theta}}}_{t},{\bm{v}}_{t}\rangle){\bm{v}}_{t}{\bm{v}}_{t}^{\top}. (17)

[209] p: We first recall the following elliptical confidence sequence:

[210] h6: Lemma B.1 (Theorem 3.2 of Lee et al. (2024a) ) .

[211] p: For any adaptively collected 9 9 9 This can be formalized via the canonical bandit model as described in Lattimore and Szepesvári (2020, Chapter 4.6) . { ( 𝐯 t , r t ) } \{({\bm{v}}_{t},r_{t})\} and any δ ∈ ( 0 , 1 ) \delta\in(0,1) we have

[212] table: ℙ ( ‖ 𝜽 ⋆ − 𝜽 ^ t ‖ 𝑯 ^ t 2 ≲ γ t ( δ ) , ∀ t ≥ 1 ) ≥ 1 − δ , {\mathbb{P}}\left(\left\lVert{\bm{\theta}}_{\star}-\hat{{\bm{\theta}}}_{t}\right\rVert_{\widehat{{\bm{H}}}_{t}}^{2}\lesssim\gamma_{t}(\delta),\ \ \forall t\geq 1\right)\geq 1-\delta,

[213] p: where γ t ​ ( δ ) ≲ S 5 + S ​ log ⁡ 1 δ + S ​ d 2 ​ log ⁡ S ​ t d \gamma_{t}(\delta)\lesssim S^{5}+S\log\frac{1}{\delta}+Sd^{2}\log\frac{St}{d} .

[214] p: We note that this is used solely for the proof and does not affect the algorithm in any way.

[215] p: From the η {\color[rgb]{0.75,0,0.25}\eta} -dependent bound of Theorem 3.1 , we have that

[216] table: MBR ​ - ​ Reg ​ ( T ) ≤ ( L μ 2 ​ η ​ β + L μ ) ​ ∑ t = 1 T 𝔼 ϕ t ∼ π ^ t ​ [ ‖ 𝑬 t ​ ϕ t ‖ 2 2 ] . \mathrm{MBR\text{-}Reg}(T)\leq(L_{\mu}^{2}{\color[rgb]{0.75,0,0.25}\eta}\beta+L_{\mu})\sum_{t=1}^{T}\mathbb{E}_{\bm{\phi}_{t}\sim\hat{\pi}_{t}}\left[\left\lVert{\bm{E}}_{t}\bm{\phi}_{t}\right\rVert_{2}^{2}\right].

[217] p: We decompose the squared Euclidean norm as follows: denoting { 𝒆 j } j ∈ [ d ] \{{\bm{e}}_{j}\}_{j\in[d]} to be the standard basis of ℝ d {\mathbb{R}}^{d} ,

[218] table: ‖ 𝑬 t ​ ϕ t ‖ 2 2 \displaystyle\left\lVert{\bm{E}}_{t}\bm{\phi}_{t}\right\rVert_{2}^{2} = ∑ j = 1 d ( 𝒆 j ⊤ ​ 𝑬 t ​ ϕ t ) 2 \displaystyle=\sum_{j=1}^{d}\left({\bm{e}}_{j}^{\top}{\bm{E}}_{t}\bm{\phi}_{t}\right)^{2} = ∑ j = 1 d ( ϕ t ⊤ ​ 𝑬 t ​ 𝒆 j ) 2 \displaystyle=\sum_{j=1}^{d}\left(\bm{\phi}_{t}^{\top}{\bm{E}}_{t}{\bm{e}}_{j}\right)^{2} ( 𝑬 t ∈ Skew ⁡ ( d ) {\bm{E}}_{t}\in\mathrm{Skew}(d) ) = ∑ j = 1 d ⟨ vec ⁡ ( 𝑬 t ) , vec ⁡ ( 𝒆 j ​ ϕ t ⊤ ) ⟩ 2 \displaystyle=\sum_{j=1}^{d}\langle\mathrm{vec}({\bm{E}}_{t}),\mathrm{vec}({\bm{e}}_{j}\bm{\phi}_{t}^{\top})\rangle^{2} ≤ ∑ j = 1 d ‖ vec ⁡ ( 𝑬 t ) ‖ 𝑯 ^ t 2 ​ ‖ vec ⁡ ( 𝒆 j ​ ϕ t ⊤ ) ‖ 𝑯 ^ t − 1 2 \displaystyle\leq\sum_{j=1}^{d}\left\lVert\mathrm{vec}({\bm{E}}_{t})\right\rVert_{\widehat{{\bm{H}}}_{t}}^{2}\left\lVert\mathrm{vec}({\bm{e}}_{j}\bm{\phi}_{t}^{\top})\right\rVert_{\widehat{{\bm{H}}}_{t}^{-1}}^{2} (Cauchy-Schwarz) ≲ γ t ​ ( δ ) 2 ​ ∑ j = 1 d ‖ ϕ t ⊗ 𝒆 j ‖ 𝑯 ^ t − 1 2 \displaystyle\lesssim\gamma_{t}(\delta)^{2}\sum_{j=1}^{d}\left\lVert\bm{\phi}_{t}\otimes{\bm{e}}_{j}\right\rVert_{\widehat{{\bm{H}}}_{t}^{-1}}^{2} ( Lemma B.1 )

[219] p: 2. Towards Expected Elliptical Potentials.

[220] p: We now present our key technical lemma:

[221] h6: Lemma B.2 (Coverage Lemma) .

[222] p: From hereon, we denote 𝔼 t − 1 ​ [ ⋅ ] ≜ 𝔼 ϕ t ∼ π ^ t , ϕ ~ t ∼ ρ ​ [ ⋅ ] \mathbb{E}_{t-1}[\cdot]\triangleq\mathbb{E}_{\bm{\phi}_{t}\sim\hat{\pi}_{t},\tilde{\bm{\phi}}_{t}\sim\rho}[\cdot] , where 𝔼 \mathbb{E} is to indicate that the expectation is conditional on the history, due to π ^ t \hat{\pi}_{t} being history-dependent.

[223] p: Applying the above lemma with 𝑴 = 𝑯 ^ t − 1 {\bm{M}}=\widehat{{\bm{H}}}_{t}^{-1} , we have:

[224] table: MBR ​ - ​ Reg ​ ( T ) \displaystyle\mathrm{MBR\text{-}Reg}(T) ≲ η ​ β ​ d 2 ​ C min − 1 ​ log ⁡ T d ​ ∑ t = 1 T 𝔼 t − 1 ​ [ vec ​ ( ϕ t ​ ϕ ~ t ⊤ ) ⊤ ​ 𝑯 ^ t − 1 ​ vec ​ ( ϕ t ​ ϕ ~ t ⊤ ) ] \displaystyle\lesssim\eta\beta d^{2}C_{\min}^{-1}\log\frac{T}{d}\sum_{t=1}^{T}\mathbb{E}_{t-1}\left[\mathrm{vec}(\bm{\phi}_{t}\tilde{\bm{\phi}}_{t}^{\top})^{\top}\widehat{{\bm{H}}}_{t}^{-1}\mathrm{vec}(\bm{\phi}_{t}\tilde{\bm{\phi}}_{t}^{\top})\right] ≤ η ​ β ​ κ − 1 ​ d 2 ​ C min − 1 ​ log ⁡ T d ​ ∑ t = 1 T 𝔼 t − 1 ​ [ vec ​ ( ϕ t ​ ϕ ~ t ⊤ ) ⊤ ​ 𝑽 t − 1 ​ vec ​ ( ϕ t ​ ϕ ~ t ⊤ ) ] , \displaystyle\leq\eta\beta\kappa^{-1}d^{2}C_{\min}^{-1}\log\frac{T}{d}\sum_{t=1}^{T}\mathbb{E}_{t-1}\left[\mathrm{vec}(\bm{\phi}_{t}\tilde{\bm{\phi}}_{t}^{\top})^{\top}{\bm{V}}_{t}^{-1}\mathrm{vec}(\bm{\phi}_{t}\tilde{\bm{\phi}}_{t}^{\top})\right], (18)

[225] p: where we have bounded γ t ​ ( δ ) 2 ≤ γ T ​ ( δ ) 2 ≲ d 2 ​ log ⁡ T d \gamma_{t}(\delta)^{2}\leq\gamma_{T}(\delta)^{2}\lesssim d^{2}\log\frac{T}{d} , and we denote 𝒗 t = ϕ t ​ ϕ ~ t ⊤ {\bm{v}}_{t}=\bm{\phi}_{t}\tilde{\bm{\phi}}_{t}^{\top} and 𝑽 t := 1 κ ∧ 1 ​ 𝑰 + ∑ s = 1 t − 1 𝒗 s ​ 𝒗 s ⊤ {\bm{V}}_{t}:=\frac{1}{\kappa\wedge 1}{\bm{I}}+\sum_{s=1}^{t-1}{\bm{v}}_{s}{\bm{v}}_{s}^{\top} .

[226] p: 3. Martingale Concentration for Realized Variance.

[227] p: We now consider the elliptical-type quantity:

[228] table: ∑ t = 1 T 𝔼 t − 1 ​ [ 𝒗 t ⊤ ​ 𝑽 t − 1 ​ 𝒗 t ] ⏟ ≜ S T \displaystyle\underbrace{\sum_{t=1}^{T}\mathbb{E}_{t-1}\left[{\bm{v}}_{t}^{\top}{\bm{V}}_{t}^{-1}{\bm{v}}_{t}\right]}_{\triangleq{\color[rgb]{0.75,0.5,0.25}S_{T}}} = ∑ t = 1 T 𝒗 t ⊤ ​ 𝑽 t − 1 ​ 𝒗 t + ∑ t = 1 T ( 𝔼 t − 1 ​ [ 𝒗 t ⊤ ​ 𝑽 t − 1 ​ 𝒗 t ] − 𝒗 t ⊤ ​ 𝑽 t − 1 ​ 𝒗 t ) ⏟ ≜ M t \displaystyle=\sum_{t=1}^{T}{\bm{v}}_{t}^{\top}{\bm{V}}_{t}^{-1}{\bm{v}}_{t}+\sum_{t=1}^{T}\underbrace{\left(\mathbb{E}_{t-1}\left[{\bm{v}}_{t}^{\top}{\bm{V}}_{t}^{-1}{\bm{v}}_{t}\right]-{\bm{v}}_{t}^{\top}{\bm{V}}_{t}^{-1}{\bm{v}}_{t}\right)}_{\triangleq M_{t}} = ∑ t = 1 T 𝒗 t ⊤ ​ 𝑽 t − 1 ​ 𝒗 t ⏟ ( a ) + ∑ t = 1 T M t ⏟ ( b ) . \displaystyle=\underbrace{\sum_{t=1}^{T}{\bm{v}}_{t}^{\top}{\bm{V}}_{t}^{-1}{\bm{v}}_{t}}_{(a)}+\underbrace{\sum_{t=1}^{T}M_{t}}_{(b)}. (19)

[229] p: We bound ( a ) (a) via the usual elliptical potential lemma ( Lemma G.3 ):

[230] table: ∑ t = 1 T 𝒗 t ⊤ ​ 𝑽 t − 1 ​ 𝒗 t ≤ 2 ​ d 2 ​ log ⁡ ( 1 + κ ​ T d 2 ) . \sum_{t=1}^{T}{\bm{v}}_{t}^{\top}{\bm{V}}_{t}^{-1}{\bm{v}}_{t}\leq 2d^{2}\log\left(1+\frac{\kappa T}{d^{2}}\right).

[231] p: We now bound ( b ) (b) . The crucial observation is that M t M_{t} is a martingale difference sequence that satisfies max t ≥ 1 ⁡ | M t | ≤ κ \max_{t\geq 1}|M_{t}|\leq\kappa , which prompts us to use the following variant of Freedman’s inequality ( Freedman, 1975 ; Beygelzimer et al., 2011 ) :

[232] h6: Lemma B.3 (Lemma 3 of Lee et al. (2024b) ) .

[233] p: Let M t M_{t} be a martingale difference sequence that satisfies max t ≥ 1 ⁡ | M t | ≤ R \max_{t\geq 1}|M_{t}|\leq R . Then for any δ ∈ ( 0 , 1 ) \delta\in(0,1) and ξ ∈ ( 0 , 1 / R ] \xi\in(0,1/R] , we have:

[234] table: ℙ ( ∑ s = 1 t M s ≤ ( e − 2 ) ξ ∑ s = 1 t 𝔼 s − 1 [ M s 2 ] + 1 ξ log 2 δ , ∀ t ≥ 1 ) ≥ 1 − δ 2 . {\mathbb{P}}\left(\sum_{s=1}^{t}M_{s}\leq(e-2)\xi\sum_{s=1}^{t}\mathbb{E}_{s-1}[M_{s}^{2}]+\frac{1}{\xi}\log\frac{2}{\delta},\quad\forall t\geq 1\right)\geq 1-\frac{\delta}{2}.

[235] p: We will now show, with high probability, that the variance term induces a linear self-bounding inequality. Denoting Z s := 𝒗 s ⊤ ​ 𝑽 s − 1 ​ 𝒗 s {\color[rgb]{0.75,0.5,0.25}Z_{s}}:={\bm{v}}_{s}^{\top}{\bm{V}}_{s}^{-1}{\bm{v}}_{s} , which satisfies 0 ≤ Z s ≤ κ ∧ 1 0\leq{\color[rgb]{0.75,0.5,0.25}Z_{s}}\leq\kappa\wedge 1 ,

[236] table: 𝔼 s − 1 ​ [ M s 2 ] ≤ 𝔼 s − 1 ​ [ Z s 2 ] ≤ ( κ ∧ 1 ) ​ 𝔼 s − 1 ​ [ Z s ] , \mathbb{E}_{s-1}[M_{s}^{2}]\leq\mathbb{E}_{s-1}[{\color[rgb]{0.75,0.5,0.25}Z_{s}}^{2}]\leq(\kappa\wedge 1)\mathbb{E}_{s-1}[{\color[rgb]{0.75,0.5,0.25}Z_{s}}], (20)

[237] p: where the first inequality follows from the fact that for any random variable X X , Var ⁡ [ X ] ≤ 𝔼 ⁡ [ X 2 ] \mathrm{Var}[X]\leq\mathbb{E}[X^{2}] .

[238] p: Choosing ξ = κ ∧ 1 2 ​ ( e − 2 ) ≤ κ \xi=\frac{\kappa\wedge 1}{2(e-2)}\leq\kappa in Lemma B.3 , the following holds with probability at least 1 − δ 2 1-\frac{\delta}{2} :

[239] table: ( b ) = ∑ t = 1 T M t ≤ ( κ ∧ 1 ) 2 2 ​ ∑ t = 1 T 𝔼 t − 1 ​ [ Z t ] ⏟ = S T ​ ! + 2 ​ ( e − 2 ) κ ∧ 1 ​ log ⁡ 2 δ . (b)=\sum_{t=1}^{T}M_{t}\leq\frac{(\kappa\wedge 1)^{2}}{2}\underbrace{\sum_{t=1}^{T}\mathbb{E}_{t-1}[{\color[rgb]{0.75,0.5,0.25}Z_{t}}]}_{={\color[rgb]{0.75,0.5,0.25}S_{T}}\text{!}}+\frac{2(e-2)}{\kappa\wedge 1}\log\frac{2}{\delta}.

[240] p: Now bringing everything together for Eqn. ( 19 ), the following holds with probability at least 1 − δ 2 1-\frac{\delta}{2} :

[241] table: S T = ( a ) + ( b ) \displaystyle{\color[rgb]{0.75,0.5,0.25}S_{T}}=(a)+(b) ≤ 2 ​ d 2 ​ log ⁡ ( 1 + κ ​ T d 2 ) ⏟ ( a ) ≤ + ( κ ∧ 1 ) 2 2 ​ S T + 2 ​ ( e − 2 ) κ ∧ 1 ​ log ⁡ 2 δ ⏟ ( b ) ≤ \displaystyle\leq\underbrace{2d^{2}\log\left(1+\frac{\kappa T}{d^{2}}\right)}_{(a)\leq}+\underbrace{\frac{(\kappa\wedge 1)^{2}}{2}{\color[rgb]{0.75,0.5,0.25}S_{T}}+\frac{2(e-2)}{\kappa\wedge 1}\log\frac{2}{\delta}}_{(b)\leq} ≤ 1 2 ​ S T + 2 ​ d 2 ​ log ⁡ ( 1 + κ ​ T d 2 ) + 2 ​ ( e − 2 ) κ ∧ 1 ​ log ⁡ 2 δ , \displaystyle\leq\frac{1}{2}{\color[rgb]{0.75,0.5,0.25}S_{T}}+2d^{2}\log\left(1+\frac{\kappa T}{d^{2}}\right)+\frac{2(e-2)}{\kappa\wedge 1}\log\frac{2}{\delta}, (21)

[242] p: which is a linear, self-bounding inequality !

[243] p: Solving for S T {\color[rgb]{0.75,0.5,0.25}S_{T}} , we have that with probability at least 1 − δ 2 1-\frac{\delta}{2} ,

[244] table: S T = ∑ t = 1 T 𝔼 t − 1 ​ [ 𝒗 t ⊤ ​ 𝑽 t − 1 ​ 𝒗 t ] ≤ 4 ​ d 2 ​ log ⁡ ( 1 + κ ​ T d 2 ) + 4 ​ ( e − 2 ) κ ∧ 1 ​ log ⁡ 2 δ . {\color[rgb]{0.75,0.5,0.25}S_{T}}=\sum_{t=1}^{T}\mathbb{E}_{t-1}\left[{\bm{v}}_{t}^{\top}{\bm{V}}_{t}^{-1}{\bm{v}}_{t}\right]\leq 4d^{2}\log\left(1+\frac{\kappa T}{d^{2}}\right)+\frac{4(e-2)}{\kappa\wedge 1}\log\frac{2}{\delta}. (22)

[245] p: Combining everything at Eqn. ( 18 ), we have that with probability at least 1 − δ 1-\delta (after union bound with the confidence sequence),

[246] table: MBR ​ - ​ Reg ​ ( T ) ≲ η ​ β ​ κ − 1 ​ d 2 ​ C min − 1 ​ ( log ⁡ T d ) ​ ( d 2 ​ log ⁡ κ ​ T d + κ − 1 ​ log ⁡ 1 δ ) . \mathrm{MBR\text{-}Reg}(T)\lesssim{\color[rgb]{0.75,0,0.25}\eta}\beta\kappa^{-1}d^{2}C_{\min}^{-1}\left(\log\frac{T}{d}\right)\left(d^{2}\log\frac{\kappa T}{d}+\kappa^{-1}\log\frac{1}{\delta}\right). (23)

[247] h4: Part II. 𝒪 ~ ​ ( T ) \tilde{{\mathcal{O}}}(\sqrt{T}) Regret Bound.

[248] p: By the η {\color[rgb]{0.75,0,0.25}\eta} -independent bound of Theorem 3.1 , we get

[249] table: MBR ​ - ​ Reg ​ ( T ) \displaystyle\mathrm{MBR\text{-}Reg}(T) ≤ L μ 2 ​ ∑ t = 1 T 𝔼 ϕ t ∼ π ^ t ​ [ ‖ 𝑬 t ​ ϕ t ‖ 2 + ‖ 𝑬 t ​ ϕ ‖ 2 2 ] \displaystyle\leq\frac{L_{\mu}}{2}\sum_{t=1}^{T}\mathbb{E}_{\bm{\phi}_{t}\sim\hat{\pi}_{t}}\left[\left\lVert{\bm{E}}_{t}\bm{\phi}_{t}\right\rVert_{2}+\left\lVert{\bm{E}}_{t}\bm{\phi}\right\rVert_{2}^{2}\right] ≤ L μ 2 ​ T ​ ∑ t = 1 T 𝔼 ϕ t ∼ π ^ t ​ [ ‖ 𝑬 t ​ ϕ t ‖ 2 2 ] + L μ 2 ​ ∑ t = 1 T 𝔼 ϕ t ∼ π ^ t ​ [ ‖ 𝑬 t ​ ϕ ‖ 2 2 ] \displaystyle\leq\frac{L_{\mu}}{2}\sqrt{T\sum_{t=1}^{T}\mathbb{E}_{\bm{\phi}_{t}\sim\hat{\pi}_{t}}\left[\left\lVert{\bm{E}}_{t}\bm{\phi}_{t}\right\rVert_{2}^{2}\right]}+\frac{L_{\mu}}{2}\sum_{t=1}^{T}\mathbb{E}_{\bm{\phi}_{t}\sim\hat{\pi}_{t}}\left[\left\lVert{\bm{E}}_{t}\bm{\phi}\right\rVert_{2}^{2}\right] (Cauchy-Schwarz & Jensen) ≲ T ​ κ − 1 ​ d 4 ​ C min − 1 ​ ( log ⁡ T d ) 2 + κ − 1 ​ d 4 ​ C min − 1 ​ ( log ⁡ T d ) 2 \displaystyle\lesssim\sqrt{T\kappa^{-1}d^{4}C_{\min}^{-1}\left(\log\frac{T}{d}\right)^{2}}+\kappa^{-1}d^{4}C_{\min}^{-1}\left(\log\frac{T}{d}\right)^{2} (Part I) = κ − 1 2 ​ C min − 1 2 ​ d 2 ​ T ​ log ⁡ T d + κ − 1 ​ C min − 1 ​ d 4 ​ ( log ⁡ T d ) 2 . \displaystyle=\kappa^{-\frac{1}{2}}C_{\min}^{-\frac{1}{2}}d^{2}\sqrt{T}\log\frac{T}{d}+\kappa^{-1}C_{\min}^{-1}d^{4}\left(\log\frac{T}{d}\right)^{2}.

[250] p: ∎

[251] h3: B.2 Proof of Lemma B.2 : Coverage Lemma

[252] p: We begin with this simple yet effective matrix lemma that will be useful throughout (we provide its proof at Section B.3 for completeness):

[253] h6: Lemma B.4 .

[254] p: If 𝐀 ⪰ 𝟎 {\bm{A}}\succeq{\bm{0}} and 𝐁 ⪰ 𝐂 ⪰ 𝟎 {\bm{B}}\succeq{\bm{C}}\succeq{\bm{0}} of compatible sizes, then 𝐀 ⊗ 𝐁 ⪰ 𝐀 ⊗ 𝐂 {\bm{A}}\otimes{\bm{B}}\succeq{\bm{A}}\otimes{\bm{C}} and tr ⁡ ( 𝐀 ​ 𝐁 ) ≥ tr ⁡ ( 𝐀 ​ 𝐂 ) \tr({\bm{A}}{\bm{B}})\geq\tr({\bm{A}}{\bm{C}}) .

[255] p: We begin from the expectation on the RHS and work our way to the LHS:

[256] table: 𝔼 ϕ ~ ∼ ρ ​ [ ( ϕ ⊗ ϕ ~ ) ⊤ ​ 𝑴 ​ ( ϕ ⊗ ϕ ~ ) ] \displaystyle\mathbb{E}_{\tilde{\bm{\phi}}\sim\rho}\left[(\bm{\phi}\otimes\tilde{\bm{\phi}})^{\top}{\bm{M}}(\bm{\phi}\otimes\tilde{\bm{\phi}})\right] = 𝔼 ϕ ~ ∼ ρ ​ [ tr ⁡ ( ( ϕ ⊗ ϕ ~ ) ⊤ ​ 𝑴 ​ ( ϕ ⊗ ϕ ~ ) ) ] \displaystyle=\mathbb{E}_{\tilde{\bm{\phi}}\sim\rho}\left[\tr\left((\bm{\phi}\otimes\tilde{\bm{\phi}})^{\top}{\bm{M}}(\bm{\phi}\otimes\tilde{\bm{\phi}})\right)\right] = 𝔼 ϕ ~ ∼ ρ ​ [ tr ⁡ ( 𝑴 ⁡ ( ϕ ⊗ ϕ ~ ) ​ ( ϕ ⊗ ϕ ~ ) ⊤ ) ] \displaystyle=\mathbb{E}_{\tilde{\bm{\phi}}\sim\rho}\left[\tr\left({\bm{M}}(\bm{\phi}\otimes\tilde{\bm{\phi}})(\bm{\phi}\otimes\tilde{\bm{\phi}})^{\top}\right)\right] (Cyclic property of tr ⁡ ( ⋅ ) \tr(\cdot) ) = tr ⁡ ( 𝑴 ​ 𝔼 ϕ ~ ∼ ρ ​ [ ( ϕ ⊗ ϕ ~ ) ​ ( ϕ ⊗ ϕ ~ ) ⊤ ] ) \displaystyle=\tr\left({\bm{M}}\mathbb{E}_{\tilde{\bm{\phi}}\sim\rho}\left[(\bm{\phi}\otimes\tilde{\bm{\phi}})(\bm{\phi}\otimes\tilde{\bm{\phi}})^{\top}\right]\right) (Linearity of expectation) = tr ⁡ ( 𝑴 ​ 𝔼 ϕ ~ ∼ ρ ​ [ ϕ ​ ϕ ⊤ ⊗ ϕ ~ ​ ϕ ~ ⊤ ] ) . \displaystyle=\tr\left({\bm{M}}\mathbb{E}_{\tilde{\bm{\phi}}\sim\rho}\left[\bm{\phi}\bm{\phi}^{\top}\otimes\tilde{\bm{\phi}}\tilde{\bm{\phi}}^{\top}\right]\right). (Mixed-product property of ⊗ \otimes )

[257] p: Now, let us examine 𝔼 ϕ ~ ∼ ρ ​ [ ϕ ​ ϕ ⊤ ⊗ ϕ ~ ​ ϕ ~ ⊤ ] \mathbb{E}_{\tilde{\bm{\phi}}\sim\rho}\left[\bm{\phi}\bm{\phi}^{\top}\otimes\tilde{\bm{\phi}}\tilde{\bm{\phi}}^{\top}\right] . Due to the linearity of the expectation and our assumption, we have

[258] table: 𝔼 ϕ ~ ∼ ρ ​ [ ϕ ​ ϕ ⊤ ⊗ ϕ ~ ​ ϕ ~ ⊤ ] = ϕ ​ ϕ ⊤ ⊗ 𝔼 ϕ ~ ∼ ρ ​ [ ϕ ~ ​ ϕ ~ ⊤ ] ⪰ C min ​ ϕ ​ ϕ ⊤ ⊗ 𝑰 d , \mathbb{E}_{\tilde{\bm{\phi}}\sim\rho}\left[\bm{\phi}\bm{\phi}^{\top}\otimes\tilde{\bm{\phi}}\tilde{\bm{\phi}}^{\top}\right]=\bm{\phi}\bm{\phi}^{\top}\otimes\mathbb{E}_{\tilde{\bm{\phi}}\sim\rho}\left[\tilde{\bm{\phi}}\tilde{\bm{\phi}}^{\top}\right]\succeq C_{\min}\bm{\phi}\bm{\phi}^{\top}\otimes{\bm{I}}_{d},

[259] p: where the last Lowener order follows from Lemma B.4 . Then, again by Lemma B.4 , we have that

[260] table: 𝔼 ϕ ~ ∼ ρ ​ [ ( ϕ ⊗ ϕ ~ ) ⊤ ​ 𝑴 ​ ( ϕ ⊗ ϕ ~ ) ] \displaystyle\mathbb{E}_{\tilde{\bm{\phi}}\sim\rho}\left[(\bm{\phi}\otimes\tilde{\bm{\phi}})^{\top}{\bm{M}}(\bm{\phi}\otimes\tilde{\bm{\phi}})\right] = tr ⁡ ( 𝑴 ​ ϕ ​ ϕ ⊤ ⊗ 𝔼 ϕ ~ ∼ ρ ​ [ ϕ ~ ​ ϕ ~ ⊤ ] ) \displaystyle=\tr\left({\bm{M}}\bm{\phi}\bm{\phi}^{\top}\otimes\mathbb{E}_{\tilde{\bm{\phi}}\sim\rho}\left[\tilde{\bm{\phi}}\tilde{\bm{\phi}}^{\top}\right]\right) ≥ C min ​ tr ⁡ ( 𝑴 ​ ϕ ​ ϕ ⊤ ⊗ 𝑰 d ) \displaystyle\geq C_{\min}\tr\left({\bm{M}}\bm{\phi}\bm{\phi}^{\top}\otimes{\bm{I}}_{d}\right) = C min ​ tr ⁡ ( 𝑴 ​ ϕ ​ ϕ ⊤ ⊗ ( ∑ j = 1 d 𝒆 j ​ 𝒆 j ⊤ ) ) \displaystyle=C_{\min}\tr\left({\bm{M}}\bm{\phi}\bm{\phi}^{\top}\otimes\left(\sum_{j=1}^{d}{\bm{e}}_{j}{\bm{e}}_{j}^{\top}\right)\right) = C min ​ ∑ j = 1 d tr ⁡ ( 𝑴 ​ ϕ ​ ϕ ⊤ ⊗ 𝒆 j ​ 𝒆 j ⊤ ) \displaystyle=C_{\min}\sum_{j=1}^{d}\tr\left({\bm{M}}\bm{\phi}\bm{\phi}^{\top}\otimes{\bm{e}}_{j}{\bm{e}}_{j}^{\top}\right) = C min ​ ∑ j = 1 d tr ⁡ ( 𝑴 ⁡ ( ϕ ⊗ 𝒆 j ) ​ ( ϕ ⊗ 𝒆 j ) ⊤ ) \displaystyle=C_{\min}\sum_{j=1}^{d}\tr\left({\bm{M}}(\bm{\phi}\otimes{\bm{e}}_{j})(\bm{\phi}\otimes{\bm{e}}_{j})^{\top}\right) (Mixed-product property of ⊗ \otimes ) = C min ​ ∑ j = 1 d ( ϕ ⊗ 𝒆 j ) ⊤ ​ 𝑴 ​ ( ϕ ⊗ 𝒆 j ) . \displaystyle=C_{\min}\sum_{j=1}^{d}(\bm{\phi}\otimes{\bm{e}}_{j})^{\top}{\bm{M}}(\bm{\phi}\otimes{\bm{e}}_{j}).

[261] p: ∎

[262] h3: B.3 Proof of Lemma B.4 : PSD Matrix Lemma

[263] p: Let 𝑫 := 𝑩 − 𝑪 {\bm{D}}:={\bm{B}}-{\bm{C}} . Since 𝑩 ⪰ 𝑪 {\bm{B}}\succeq{\bm{C}} , we have 𝑫 ⪰ 𝟎 {\bm{D}}\succeq{\bm{0}} .

[264] p: We first show that 𝑨 ⊗ 𝑩 ⪰ 𝑨 ⊗ 𝑪 {\bm{A}}\otimes{\bm{B}}\succeq{\bm{A}}\otimes{\bm{C}} . By bilinearity of the Kronecker product,

[265] table: 𝑨 ⊗ 𝑩 − 𝑨 ⊗ 𝑪 = 𝑨 ⊗ ( 𝑩 − 𝑪 ) = 𝑨 ⊗ 𝑫 . {\bm{A}}\otimes{\bm{B}}-{\bm{A}}\otimes{\bm{C}}={\bm{A}}\otimes({\bm{B}}-{\bm{C}})={\bm{A}}\otimes{\bm{D}}.

[266] p: It therefore suffices to prove that 𝑨 ⊗ 𝑫 {\bm{A}}\otimes{\bm{D}} is positive semidefinite.

[267] p: Let { λ i ​ ( 𝑨 ) } i = 1 n \{\lambda_{i}({\bm{A}})\}_{i=1}^{n} and { λ j ​ ( 𝑫 ) } j = 1 m \{\lambda_{j}({\bm{D}})\}_{j=1}^{m} denote the eigenvalues of 𝑨 {\bm{A}} and 𝑫 {\bm{D}} , respectively. A standard property of Kronecker products implies that the eigenvalues of 𝑨 ⊗ 𝑫 {\bm{A}}\otimes{\bm{D}} are

[268] table: { λ i ​ ( 𝑨 ) ​ λ j ​ ( 𝑫 ) } i ∈ [ n ] , j ∈ [ m ] . \bigl\{\lambda_{i}({\bm{A}})\lambda_{j}({\bm{D}})\bigr\}_{i\in[n],\,j\in[m]}.

[269] p: Since 𝑨 ⪰ 𝟎 {\bm{A}}\succeq{\bm{0}} and 𝑫 ⪰ 𝟎 {\bm{D}}\succeq{\bm{0}} , all eigenvalues λ i ​ ( 𝑨 ) \lambda_{i}({\bm{A}}) and λ j ​ ( 𝑫 ) \lambda_{j}({\bm{D}}) are nonnegative, hence so are all products λ i ​ ( 𝑨 ) ​ λ j ​ ( 𝑫 ) \lambda_{i}({\bm{A}})\lambda_{j}({\bm{D}}) . Therefore 𝑨 ⊗ 𝑫 ⪰ 𝟎 {\bm{A}}\otimes{\bm{D}}\succeq{\bm{0}} , which yields 𝑨 ⊗ 𝑩 ⪰ 𝑨 ⊗ 𝑪 {\bm{A}}\otimes{\bm{B}}\succeq{\bm{A}}\otimes{\bm{C}} .

[270] p: Now we prove tr ⁡ ( 𝑨 ​ 𝑩 ) ≥ tr ⁡ ( 𝑨 ​ 𝑪 ) \tr({\bm{A}}{\bm{B}})\geq\tr({\bm{A}}{\bm{C}}) . Since 𝑨 ⪰ 0 {\bm{A}}\succeq 0 , there exists a symmetric square root 𝑨 1 / 2 {\bm{A}}^{1/2} such that 𝑨 = 𝑨 1 / 2 ​ 𝑨 1 / 2 {\bm{A}}={\bm{A}}^{1/2}{\bm{A}}^{1/2} . Using cyclicity of trace,

[271] table: tr ⁡ ( 𝑨 ​ 𝑫 ) = tr ⁡ ( 𝑨 1 / 2 ​ 𝑨 1 / 2 ​ 𝑫 ) = tr ⁡ ( 𝑨 1 / 2 ​ 𝑫 ​ 𝑨 1 / 2 ) . \tr({\bm{A}}{\bm{D}})=\tr({\bm{A}}^{1/2}{\bm{A}}^{1/2}{\bm{D}})=\tr({\bm{A}}^{1/2}{\bm{D}}{\bm{A}}^{1/2}).

[272] p: Moreover, 𝑨 1 / 2 ​ 𝑫 ​ 𝑨 1 / 2 {\bm{A}}^{1/2}{\bm{D}}{\bm{A}}^{1/2} is positive semidefinite. For any 𝒙 ∈ ℝ n {\bm{x}}\in\mathbb{R}^{n} , letting 𝒚 := 𝑨 1 / 2 ​ 𝒙 {\bm{y}}:={\bm{A}}^{1/2}{\bm{x}} , we have

[273] table: 𝒙 ⊤ ​ 𝑨 1 / 2 ​ 𝑫 ​ 𝑨 1 / 2 ​ 𝒙 = 𝒚 ⊤ ​ 𝑫 ​ 𝒚 ≥ 0 , {\bm{x}}^{\top}{\bm{A}}^{1/2}{\bm{D}}{\bm{A}}^{1/2}{\bm{x}}={\bm{y}}^{\top}{\bm{D}}{\bm{y}}\geq 0,

[274] p: where the inequality uses 𝑫 ⪰ 𝟎 {\bm{D}}\succeq{\bm{0}} . Hence 𝑨 1 / 2 ​ 𝑫 ​ 𝑨 1 / 2 ⪰ 𝟎 {\bm{A}}^{1/2}{\bm{D}}{\bm{A}}^{1/2}\succeq{\bm{0}} , and therefore tr ⁡ ( 𝑨 1 / 2 ​ 𝑫 ​ 𝑨 1 / 2 ) ≥ 0 \tr({\bm{A}}^{1/2}{\bm{D}}{\bm{A}}^{1/2})\geq 0 . This implies tr ⁡ ( 𝑨 ​ 𝑫 ) ≥ 0 \tr({\bm{A}}{\bm{D}})\geq 0 , completing the proof. ∎

[275] h3: B.4 Coverage Lemma without Feature Diversity

[276] p: Here, we show that for specific choices of ψ ⁡ ( ⋅ ) \psi(\cdot) , Lemma B.2 holds even without the feature diversity assumption ( Assumption 1 ) , where C min − 1 C_{\min}^{-1} is replaced with a function of η {\color[rgb]{0.75,0,0.25}\eta} . Recalling that Π = Δ ⁡ ( 𝒜 ) \Pi=\Delta({\mathcal{A}}) , we have:

[277] h6: Proposition B.5 (Coverage Lemma without Feature Diversity) .

[278] p: Let π ref ∈ Π \pi_{\mathrm{ref}}\in\Pi be a fixed policy, and π ^ t \hat{\pi}_{t} be the corresponding regularized SNE policy with respect to the preference model P ^ t \hat{P}_{t} :

[279] table: π ^ t := arg ​ max π 1 ∈ Π ⁡ min π 2 ∈ Π ​ J η ​ ( π 1 , π 2 ) . \hat{\pi}_{t}:=\argmax_{\pi^{1}\in\Pi}\min_{\pi^{2}\in\Pi}J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1},\pi^{2}).

[280] p: Using the shorthand notation ϕ ⁡ ( 𝐚 ) \phi({\bm{a}}) for ϕ ⁡ ( 𝐱 , 𝐚 ) \phi({\bm{x}},{\bm{a}}) , for any positive semi-definite matrix 𝐌 ⪰ 𝟎 {\bm{M}}\succeq{\bm{0}} , we have:

[281] table: 𝔼 𝒂 ∼ π ^ t ​ [ ϕ ​ ( 𝒂 ) ⊤ ​ 𝑴 ​ ϕ ​ ( 𝒂 ) ] ≤ h ⁡ ( η ) ​ 𝔼 𝒂 ∼ π ref ​ [ ϕ ​ ( 𝒂 ) ⊤ ​ 𝑴 ​ ϕ ​ ( 𝒂 ) ] , \mathbb{E}_{{\bm{a}}\sim\hat{\pi}_{t}}\left[\phi({\bm{a}})^{\top}{\bm{M}}\phi({\bm{a}})\right]\leq{\color[rgb]{0.75,0,0.25}h(\eta)}\,\mathbb{E}_{{\bm{a}}\sim\pi_{\mathrm{ref}}}\left[\phi({\bm{a}})^{\top}{\bm{M}}\phi({\bm{a}})\right],

[282] p: where

[283] table: h ⁡ ( η ) = { e η , ψ ⁡ ( ⋅ ) = D KL ​ ( ⋅ , π ref ) , η , ψ ⁡ ( ⋅ ) = D χ 2 ​ ( ⋅ , π ref ) , 1 + η , ψ ⁡ ( ⋅ ) = D KL ​ ( ⋅ , π ref ) + D χ 2 ​ ( ⋅ , π ref ) . {\color[rgb]{0.75,0,0.25}h(\eta)}=\begin{cases}{\color[rgb]{0.75,0,0.25}e^{\eta}},&$\psi(\cdot)=D_{\mathrm{KL}}(\cdot,\pi_{\mathrm{ref}})$,\\ {\color[rgb]{0.75,0,0.25}\eta},&$\psi(\cdot)=D_{\chi^{2}}(\cdot,\pi_{\mathrm{ref}})$,\\ {\color[rgb]{0.75,0,0.25}1+\eta},&$\psi(\cdot)=D_{\mathrm{KL}}(\cdot,\pi_{\mathrm{ref}})+D_{\chi^{2}}(\cdot,\pi_{\mathrm{ref}})$.\end{cases} (24)

[284] h6: Proof.

[285] p: We present the proof for a finite action space 𝒜 {\mathcal{A}} . The results naturally extend to infinite 𝒜 {\mathcal{A}} via integration.

[286] p: We can bound the left-hand side by expanding the expectation and applying a density ratio bound:

[287] table: 𝔼 𝒂 ∼ π ^ t ​ [ ϕ ​ ( 𝒂 ) ⊤ ​ 𝑴 ​ ϕ ​ ( 𝒂 ) ] \displaystyle\mathbb{E}_{{\bm{a}}\sim\hat{\pi}_{t}}\left[\phi({\bm{a}})^{\top}{\bm{M}}\phi({\bm{a}})\right] = ∑ 𝒂 ∈ 𝒜 π ^ t ​ ( 𝒂 ) ​ ϕ ​ ( 𝒂 ) ⊤ ​ 𝑴 ​ ϕ ​ ( 𝒂 ) \displaystyle=\sum_{{\bm{a}}\in{\mathcal{A}}}\hat{\pi}_{t}({\bm{a}})\phi({\bm{a}})^{\top}{\bm{M}}\phi({\bm{a}}) = ∑ 𝒂 ∈ 𝒜 π ^ t ​ ( 𝒂 ) π ref ​ ( 𝒂 ) ​ π ref ​ ( 𝒂 ) ​ ϕ ​ ( 𝒂 ) ⊤ ​ 𝑴 ​ ϕ ​ ( 𝒂 ) \displaystyle=\sum_{{\bm{a}}\in{\mathcal{A}}}\frac{\hat{\pi}_{t}({\bm{a}})}{\pi_{\mathrm{ref}}({\bm{a}})}\pi_{\mathrm{ref}}({\bm{a}})\phi({\bm{a}})^{\top}{\bm{M}}\phi({\bm{a}}) ≤ ( max 𝒂 ∈ 𝒜 ⁡ π ^ t ​ ( 𝒂 ) π ref ​ ( 𝒂 ) ) ​ ∑ 𝒂 ∈ 𝒜 π ref ​ ( 𝒂 ) ​ ϕ ​ ( 𝒂 ) ⊤ ​ 𝑴 ​ ϕ ​ ( 𝒂 ) \displaystyle\leq\left(\max_{{\bm{a}}\in{\mathcal{A}}}\frac{\hat{\pi}_{t}({\bm{a}})}{\pi_{\mathrm{ref}}({\bm{a}})}\right)\sum_{{\bm{a}}\in{\mathcal{A}}}\pi_{\mathrm{ref}}({\bm{a}})\phi({\bm{a}})^{\top}{\bm{M}}\phi({\bm{a}}) = ( max 𝒂 ∈ 𝒜 ⁡ π ^ t ​ ( 𝒂 ) π ref ​ ( 𝒂 ) ) ​ 𝔼 𝒂 ∼ π ref ​ [ ϕ ​ ( 𝒂 ) ⊤ ​ 𝑴 ​ ϕ ​ ( 𝒂 ) ] . \displaystyle=\left(\max_{{\bm{a}}\in{\mathcal{A}}}\frac{\hat{\pi}_{t}({\bm{a}})}{\pi_{\mathrm{ref}}({\bm{a}})}\right)\mathbb{E}_{{\bm{a}}\sim\pi_{\mathrm{ref}}}\left[\phi({\bm{a}})^{\top}{\bm{M}}\phi({\bm{a}})\right].

[288] p: Thus, it remains to bound the maximum density ratio between the regularized optimal policy π ^ t \hat{\pi}_{t} and the reference policy π ref \pi_{\mathrm{ref}} .

[289] p: Case I. ψ ⁡ ( ⋅ ) = D KL ​ ( ⋅ , π ref ) \psi(\cdot)=D_{\mathrm{KL}}(\cdot,\pi_{\mathrm{ref}}) . By Wu et al. (2025a, Proposition 3) , we have:

[290] table: π ^ t ​ ( 𝒂 ) = π ref ​ ( 𝒂 ) ​ exp ⁡ ( η ​ P ^ t ​ ( 𝒂 , π ^ t ) ) ∑ 𝒂 ′ ∈ 𝒜 π ref ​ ( 𝒂 ′ ) ​ exp ⁡ ( η ​ P ^ t ​ ( 𝒂 ′ , π ^ t ) ) . \hat{\pi}_{t}({\bm{a}})=\frac{\pi_{\mathrm{ref}}({\bm{a}})\exp({\color[rgb]{0.75,0,0.25}\eta}\hat{P}_{t}({\bm{a}},\hat{\pi}_{t}))}{\sum_{{\bm{a}}^{\prime}\in{\mathcal{A}}}\pi_{\mathrm{ref}}({\bm{a}}^{\prime})\exp({\color[rgb]{0.75,0,0.25}\eta}\hat{P}_{t}({\bm{a}}^{\prime},\hat{\pi}_{t}))}.

[291] p: Since preference probabilities satisfy P ^ t ​ ( ⋅ , ⋅ ) ≤ 1 \hat{P}_{t}(\cdot,\cdot)\leq 1 and π ref ∈ Δ ⁡ ( 𝒜 ) \pi_{\mathrm{ref}}\in\Delta({\mathcal{A}}) implies ∑ 𝒂 ′ π ref ​ ( 𝒂 ′ ) = 1 \sum_{{\bm{a}}^{\prime}}\pi_{\mathrm{ref}}({\bm{a}}^{\prime})=1 , we obtain:

[292] table: max 𝒂 ∈ 𝒜 ⁡ π ^ t ​ ( 𝒂 ) π ref ​ ( 𝒂 ) = max 𝒂 ∈ 𝒜 ⁡ exp ⁡ ( η ​ P ^ t ​ ( 𝒂 , π ^ t ) ) ∑ 𝒂 ′ ∈ 𝒜 π ref ​ ( 𝒂 ′ ) ​ exp ⁡ ( η ​ P ^ t ​ ( 𝒂 ′ , π ^ t ) ) ≤ exp ⁡ ( η ) ∑ 𝒂 ′ ∈ 𝒜 π ref ​ ( 𝒂 ′ ) = e η . \max_{{\bm{a}}\in{\mathcal{A}}}\frac{\hat{\pi}_{t}({\bm{a}})}{\pi_{\mathrm{ref}}({\bm{a}})}=\max_{{\bm{a}}\in{\mathcal{A}}}\frac{\exp({\color[rgb]{0.75,0,0.25}\eta}\hat{P}_{t}({\bm{a}},\hat{\pi}_{t}))}{\sum_{{\bm{a}}^{\prime}\in{\mathcal{A}}}\pi_{\mathrm{ref}}({\bm{a}}^{\prime})\exp({\color[rgb]{0.75,0,0.25}\eta}\hat{P}_{t}({\bm{a}}^{\prime},\hat{\pi}_{t}))}\leq\frac{\exp({\color[rgb]{0.75,0,0.25}\eta})}{\sum_{{\bm{a}}^{\prime}\in{\mathcal{A}}}\pi_{\mathrm{ref}}({\bm{a}}^{\prime})}={\color[rgb]{0.75,0,0.25}e^{\eta}}.

[293] p: Case II. ψ ⁡ ( ⋅ ) = D χ 2 ​ ( ⋅ , π ref ) \psi(\cdot)=D_{\chi^{2}}(\cdot,\pi_{\mathrm{ref}}) . We directly invoke Huang et al. (2025a, Eqn. (10)) , which states that under chi-squared regularization,

[294] table: max 𝒂 ∈ 𝒜 ⁡ π ^ t ​ ( 𝒂 ) π ref ​ ( 𝒂 ) = max 𝒂 ∈ 𝒜 ⁡ max ⁡ { η ⁡ ( P ^ t ​ ( 𝒂 , π ^ t ) − Z ) , 0 } ≤ η , \max_{{\bm{a}}\in{\mathcal{A}}}\frac{\hat{\pi}_{t}({\bm{a}})}{\pi_{\mathrm{ref}}({\bm{a}})}=\max_{{\bm{a}}\in{\mathcal{A}}}\max\left\{{\color[rgb]{0.75,0,0.25}\eta}\left(\hat{P}_{t}({\bm{a}},\hat{\pi}_{t})-Z\right),0\right\}\leq{\color[rgb]{0.75,0,0.25}\eta},

[295] p: where Z ≥ 0 Z\geq 0 is an appropriate normalization constant and we again utilize the fact that P ^ t ≤ 1 \hat{P}_{t}\leq 1 .

[296] p: Case III. ψ ⁡ ( ⋅ ) = D KL ​ ( ⋅ , π ref ) + D χ 2 ​ ( ⋅ , π ref ) \psi(\cdot)=D_{\mathrm{KL}}(\cdot,\pi_{\mathrm{ref}})+D_{\chi^{2}}(\cdot,\pi_{\mathrm{ref}}) . We directly invoke Huang et al. (2025b, Proposition 4.1) , which states that under mixed chi-squared regularization,

[297] table: max 𝒂 ∈ 𝒜 ⁡ π ^ t ​ ( 𝒂 ) π ref ​ ( 𝒂 ) ≤ 1 + η . \max_{{\bm{a}}\in{\mathcal{A}}}\frac{\hat{\pi}_{t}({\bm{a}})}{\pi_{\mathrm{ref}}({\bm{a}})}\leq 1+{\color[rgb]{0.75,0,0.25}\eta}.

[298] p: ∎

[299] h6: Remark B.6 (Towards General f f -Divergence) .

[300] p: Note that all three regularizers above are specific instances of the f f -divergence ( Csiszár, 1963 ; Ali and Silvey, 1966 ) . Wang et al. (2024, Theorem 1) proved that if f f is such that f ′ f^{\prime} is invertible and 0 ∉ dom ⁡ ( f ′ ) 0\not\in\mathrm{dom}(f^{\prime}) , then in our general preference scenario, we have:

[301] table: π ^ t ​ ( 𝒂 ) π ref ​ ( 𝒂 ) = ( f ′ ) − 1 ​ ( η ⁡ ( P ^ t ​ ( 𝒂 , π ^ t ) − Z ) ) \frac{\hat{\pi}_{t}({\bm{a}})}{\pi_{\mathrm{ref}}({\bm{a}})}=(f^{\prime})^{-1}\left({\color[rgb]{0.75,0,0.25}\eta}\left(\hat{P}_{t}({\bm{a}},\hat{\pi}_{t})-Z\right)\right)

[302] p: where Z ≥ 0 Z\geq 0 is an appropriate normalization constant. Thus, we postulate that a similar coverage lemma can be proven for various other choices of f f , completely bypassing the feature diversity assumption.

[303] h2: Appendix C Proof of Theorem 5.2 : Regret Bound of Explore-Then-Commit

[304] h3: C.1 Main Proof

[305] p: Recall the nuclear-norm regularized MLE ( Fan et al., 2019 ; Lee et al., 2025 ) : denoting 𝑿 t := ϕ ⁡ ( 𝒙 t , 𝒂 t 1 ) ​ ϕ ​ ( 𝒙 t , 𝒂 t 2 ) ⊤ {\bm{X}}_{t}:=\phi({\bm{x}}_{t},{\bm{a}}_{t}^{1})\phi({\bm{x}}_{t},{\bm{a}}_{t}^{2})^{\top} ,

[306] table: 𝚯 ^ T 0 \displaystyle\widehat{\bm{\Theta}}_{T_{0}} ← arg ​ min 𝚯 ∈ Skew ⁡ ( d ) ⁡ ℒ T 0 ​ ( 𝚯 ) + λ T 0 ​ ‖ 𝚯 ‖ nuc , \displaystyle\leftarrow\argmin_{\bm{\Theta}\in\mathrm{Skew}(d)}{\mathcal{L}}_{T_{0}}(\bm{\Theta})+\lambda_{T_{0}}\left\lVert\bm{\Theta}\right\rVert_{\mathrm{nuc}}, (25) ℒ T 0 ​ ( 𝚯 ) \displaystyle{\mathcal{L}}_{T_{0}}(\bm{\Theta}) : = 1 T 0 ​ ∑ t = 1 T 0 { m ⁡ ( ⟨ 𝚯 , 𝑿 t ⟩ ) − r t ​ ⟨ 𝚯 , 𝑿 t ⟩ } . \displaystyle:=\frac{1}{T_{0}}\sum_{t=1}^{T_{0}}\left\{m(\langle\bm{\Theta},{\bm{X}}_{t}\rangle)-r_{t}\langle\bm{\Theta},{\bm{X}}_{t}\rangle\right\}. (26)

[307] p: We also introduce the following assumption used commonly in logistic and generalized linear bandits ( Abeille et al., 2021 ; Russac et al., 2021 ; Lee et al., 2024a ) :

[308] h6: Assumption 2 .

[309] p: The link function μ \mu is self-concordant with constant R s ≥ 0 R_{s}\geq 0 , i.e.,

[310] table: | μ ¨ ​ ( ϕ ⊤ ​ 𝚯 ​ ϕ ′ ) | ≤ R s ​ μ ˙ ​ ( ϕ ⊤ ​ 𝚯 ​ ϕ ′ ) , ∀ ϕ , ϕ ′ ∈ ℬ d ​ ( 1 ) , ∀ 𝚯 ∈ Skew ⁡ ( d , 2 ​ r , S ) . \left|\ddot{\mu}\left(\bm{\phi}^{\top}\bm{\Theta}\bm{\phi}^{\prime}\right)\right|\leq R_{s}\dot{\mu}\left(\bm{\phi}^{\top}\bm{\Theta}\bm{\phi}^{\prime}\right),\quad\forall\bm{\phi},\bm{\phi}^{\prime}\in{\mathcal{B}}^{d}(1),\forall\bm{\Theta}\in\mathrm{Skew}(d,2r;S). (27)

[311] p: Lastly, we define the following instance-specific curvature quantity:

[312] table: κ ⋆ := min ϕ , ϕ ′ ∈ ℬ d ​ ( 1 ) ⁡ μ ˙ ​ ( ϕ ⊤ ​ 𝚯 ⋆ ​ ϕ ′ ) . \kappa_{\star}:=\min_{\bm{\phi},\bm{\phi}^{\prime}\in\mathcal{B}^{d}(1)}\dot{\mu}\left(\bm{\phi}^{\top}\bm{\Theta}_{\star}\bm{\phi}^{\prime}\right). (28)

[313] p: This parameter has been identified as a fundamental instance-dependent factor in the analysis of logistic and generalized linear bandits ( Abeille et al., 2021 ; Lee et al., 2024a ) . In contrast to the global curvature κ \kappa (see Definition 2.2 ), which involves an additional minimization over 𝚯 ⋆ ∈ Skew ⁡ ( d , 2 ​ r , S ) \bm{\Theta}_{\star}\in\mathrm{Skew}(d,2r;S) , κ ⋆ \kappa_{\star} captures the local geometry around the true parameter 𝚯 ⋆ \bm{\Theta}_{\star} . We note that in many practical regimes, the global bound may be overly pessimistic, such that κ − 1 ≫ κ ⋆ − 1 \kappa^{-1}\gg\kappa_{\star}^{-1} . In this Appendix, we show that under the additional assumption that μ \mu is self-concordant, we can obtain dependencies w.r.t. κ ⋆ − 1 \kappa_{\star}^{-1} instead of κ − 1 \kappa^{-1} .

[314] p: The following lemma provides a Frobenius error guarantee for the nuclear-norm regularized MLE 𝚯 ^ \widehat{\bm{\Theta}} :

[315] h6: Lemma C.1 .

[316] h6: Proof Sketch.

[317] p: The proof largely follows the classical M-estimator analysis via restricted strong convexity ( Wainwright, 2019 ) , which we reproduce here for completeness. See Section C.2 for the full proof. ∎

[318] p: We first invoke the η {\color[rgb]{0.75,0,0.25}\eta} -dependent bound of Theorem 3.1 and the above lemma to t ∈ [ [ T 0 + 1 , T ] ] t\in[[T_{0}+1,T]] :

[319] table: MBR ​ - ​ Reg ​ ( T ) ≲ T 0 + η ​ β ​ ∑ t = T 0 + 1 T 𝔼 ϕ t ∼ π ^ t ​ [ ‖ 𝑬 t ​ ϕ t ‖ 2 2 ] ≤ T 0 + T ​ η ​ β ​ ‖ 𝑬 T 0 ‖ op 2 ≲ T 0 + T ​ η ​ β κ ~ 2 ​ C min 4 ​ r ​ log ⁡ d δ T 0 . \mathrm{MBR\text{-}Reg}(T)\lesssim T_{0}+{\color[rgb]{0.75,0,0.25}\eta}\beta\sum_{t=T_{0}+1}^{T}\mathbb{E}_{\bm{\phi}_{t}\sim\hat{\pi}_{t}}\left[\left\lVert{\bm{E}}_{t}\bm{\phi}_{t}\right\rVert_{2}^{2}\right]\leq T_{0}+T{\color[rgb]{0.75,0,0.25}\eta}\beta\left\lVert{\bm{E}}_{T_{0}}\right\rVert_{\mathrm{op}}^{2}\lesssim T_{0}+\frac{T{\color[rgb]{0.75,0,0.25}\eta}\beta}{\tilde{\kappa}^{2}C_{\min}^{4}}\frac{r\log\frac{d}{\delta}}{T_{0}}.

[320] p: This balances out when T 0 ≍ κ ~ − 1 ​ C min − 2 ​ T ​ η ​ β ​ r ​ log ⁡ d δ T_{0}\asymp\tilde{\kappa}^{-1}C_{\min}^{-2}\sqrt{T\eta\beta r\log\frac{d}{\delta}} .

[321] p: Now, we invoke the η {\color[rgb]{0.75,0,0.25}\eta} -independent bound of Theorem 3.1 , which yields

[322] table: MBR ​ - ​ Reg ​ ( T ) \displaystyle\mathrm{MBR\text{-}Reg}(T) ≲ T 0 + ∑ t = T 0 + 1 T 𝔼 ϕ t ∼ π ^ t ​ [ ‖ 𝑬 t ​ ϕ t ‖ 2 ] + ∑ t = T 0 + 1 T 𝔼 ϕ t ∼ π ^ t ​ [ ‖ 𝑬 t ​ ϕ t ‖ 2 2 ] \displaystyle\lesssim T_{0}+\sum_{t=T_{0}+1}^{T}\mathbb{E}_{\bm{\phi}_{t}\sim\hat{\pi}_{t}}\left[\left\lVert{\bm{E}}_{t}\bm{\phi}_{t}\right\rVert_{2}\right]+\sum_{t=T_{0}+1}^{T}\mathbb{E}_{\bm{\phi}_{t}\sim\hat{\pi}_{t}}\left[\left\lVert{\bm{E}}_{t}\bm{\phi}_{t}\right\rVert_{2}^{2}\right] ≤ T 0 + T ​ ‖ 𝑬 T 0 ‖ op + T ​ ‖ 𝑬 T 0 ‖ op 2 \displaystyle\leq T_{0}+T\left\lVert{\bm{E}}_{T_{0}}\right\rVert_{\mathrm{op}}+T\left\lVert{\bm{E}}_{T_{0}}\right\rVert_{\mathrm{op}}^{2} ≲ T 0 + T κ ~ ​ C min 2 ​ L μ ​ r ​ log ⁡ d δ T 0 + T κ ~ 2 ​ C min 4 ​ L μ ​ r ​ log ⁡ d δ T 0 . \displaystyle\lesssim T_{0}+\frac{T}{\tilde{\kappa}C_{\min}^{2}}\sqrt{\frac{L_{\mu}r\log\frac{d}{\delta}}{T_{0}}}+\frac{T}{\tilde{\kappa}^{2}C_{\min}^{4}}\frac{L_{\mu}r\log\frac{d}{\delta}}{T_{0}}.

[323] p: This balances out when T 0 ≍ ( T 2 ​ κ ~ − 2 ​ C min − 4 ​ r ​ log ⁡ d δ ) 1 / 3 T_{0}\asymp\left(T^{2}\tilde{\kappa}^{-2}C_{\min}^{-4}r\log\frac{d}{\delta}\right)^{1/3} and T ≳ κ ~ ​ C min 2 ​ r ​ log ⁡ d δ T\gtrsim\tilde{\kappa}C_{\min}^{2}r\log\frac{d}{\delta} , the latter which we can assume to hold without loss of any generality. ∎

[324] h3: C.2 Proof of Lemma C.1 : Error Bound Guarantee of the Nuclear-Norm Regularized MLE

[325] p: We follow the usual recipe for proving the error rate of a generic M-estimator with a convex regularizer ( Wainwright, 2019 , Chapter 9 & 10) . Let δ ∈ ( 0 , 1 ) \delta\in(0,1) be given.

[326] p: Recall that

[327] table: 𝚯 ^ := arg ​ min 𝚯 ∈ Skew ⁡ ( d ) ⁡ ℒ T 0 ​ ( 𝚯 ) + λ T 0 ​ ‖ 𝚯 ‖ nuc , ℒ T 0 ​ ( 𝚯 ) := 1 T 0 ​ ∑ t = 1 T 0 { m ⁡ ( 𝐱 t ⊤ ​ 𝚯 ​ 𝐲 t ) − r t ​ 𝐱 t ⊤ ​ 𝚯 ​ 𝐲 t } , \widehat{\bm{\Theta}}:=\argmin_{\bm{\Theta}\in\mathrm{Skew}(d)}{\mathcal{L}}_{T_{0}}(\bm{\Theta})+\lambda_{T_{0}}\left\lVert\bm{\Theta}\right\rVert_{\mathrm{nuc}},\quad{\mathcal{L}}_{T_{0}}(\bm{\Theta}):=\frac{1}{T_{0}}\sum_{t=1}^{T_{0}}\left\{m({\bm{x}}_{t}^{\top}\bm{\Theta}{\bm{y}}_{t})-r_{t}{\bm{x}}_{t}^{\top}\bm{\Theta}{\bm{y}}_{t}\right\}, (29)

[328] p: Recall that for notational simplicity, we denote 𝑿 t := ϕ t 1 ​ ( ϕ t 2 ) ⊤ {\bm{X}}_{t}:=\bm{\phi}_{t}^{1}(\bm{\phi}_{t}^{2})^{\top} . We will collect all requirements on T 0 T_{0} in violet to be aggregated at the end of the proof.

[329] p: The first lemma tells us the correct choice of λ T 0 \lambda_{T_{0}} such that the gradient of ℒ T 0 {\mathcal{L}}_{T_{0}} at the true parameter 𝚯 ⋆ \bm{\Theta}_{\star} is well bounded:

[330] h6: Lemma C.2 (Lemma C.3 of Lee et al. (2025) ) .

[331] p: Suppose that T 0 ≥ 2 9 ​ L μ ​ log ⁡ 4 ​ d δ T_{0}\geq\frac{2}{9L_{\mu}}\log\frac{4d}{\delta} . Then, choosing λ T 0 = 32 ​ L μ ​ log ⁡ 4 ​ d δ T 0 \lambda_{T_{0}}=\sqrt{\frac{32L_{\mu}\log\frac{4d}{\delta}}{T_{0}}} , we have that ℙ ⁡ ( ‖ ∇ ℒ T 0 ​ ( 𝚯 ) ‖ op ≤ λ T 0 2 ) ≥ 1 − δ 2 {\mathbb{P}}\left(\left\lVert\nabla{\mathcal{L}}_{T_{0}}(\bm{\Theta})\right\rVert_{\mathrm{op}}\leq\frac{\lambda_{T_{0}}}{2}\right)\geq 1-\frac{\delta}{2} .

[332] p: We will suppose that the above good event holds.

[333] p: We now recall the definition of restricted strong convexity (RSC):

[334] h6: Definition C.3 (Definition 9.15 of Wainwright (2019) ) .

[335] p: We say that restricted strong convexity (RSC) with α , τ , R ≥ 0 \alpha,\tau,R\geq 0 if

[336] table: ℒ T 0 ​ ( 𝚯 ⋆ + Δ ) − ℒ T 0 ​ ( 𝚯 ⋆ ) − ⟨ ∇ ℒ T 0 ​ ( 𝚯 ⋆ ) , Δ ⟩ ⏟ Bregman divergence generated by ℒ T 0 ≥ α 2 ​ ‖ Δ ‖ F 2 − τ 2 ​ ‖ Δ ‖ nuc 2 , ∀ Δ ∈ ℬ F d ​ ( R ) . \underbrace{{\mathcal{L}}_{T_{0}}(\bm{\Theta}_{\star}+\Delta)-{\mathcal{L}}_{T_{0}}(\bm{\Theta}_{\star})-\langle\nabla{\mathcal{L}}_{T_{0}}(\bm{\Theta}_{\star}),\Delta\rangle}_{\text{Bregman divergence generated by ${\mathcal{L}}_{T_{0}}$}}\geq\frac{\alpha}{2}\left\lVert\Delta\right\rVert_{F}^{2}-\tau^{2}\left\lVert\Delta\right\rVert_{\mathrm{nuc}}^{2},\quad\forall\Delta\in{\mathcal{B}}^{d}_{F}(R). (30)

[337] p: The next lemma shows that the above holds with high probability:

[338] h6: Lemma C.4 .

[339] p: Suppose that T 0 ≳ C min − 4 ​ κ ~ − 2 ​ d ​ r ​ log ⁡ d δ T_{0}\gtrsim C_{\min}^{-4}\tilde{\kappa}^{-2}dr\log\frac{d}{\delta} . Then, with probability at least 1 − δ 2 1-\frac{\delta}{2} , RSC holds with α = R ~ s ​ κ ~ ​ C min 2 \alpha=\tilde{R}_{s}\tilde{\kappa}C_{\min}^{2} , τ 2 = 0 \tau^{2}=0 , and R = 1 d R=\frac{1}{\sqrt{d}} .

[340] p: Lastly, noting that the subspace Lipschitz constant ( Wainwright, 2019 , Definition 9.18) of ‖ ⋅ ‖ nuc \left\lVert\cdot\right\rVert_{\mathrm{nuc}} is r \sqrt{r} , we conclude by invoking the “master theorem” for nuclear-norm regularized estimator ( Wainwright, 2019 , Theorem 9.19) :

[341] table: ℙ ⁡ ( ‖ 𝚯 ^ − 𝚯 ⋆ ‖ F ≤ 12 R ~ s ​ C min 2 ​ κ ~ ​ 2 ​ L μ ​ r ​ log ⁡ 4 ​ d δ T 0 ) ≥ 1 − δ , {\mathbb{P}}\left(\left\lVert\widehat{\bm{\Theta}}-\bm{\Theta}_{\star}\right\rVert_{F}\leq\frac{12}{\tilde{R}_{s}C_{\min}^{2}\tilde{\kappa}}\sqrt{\frac{2L_{\mu}r\log\frac{4d}{\delta}}{T_{0}}}\right)\geq 1-\delta, (31)

[342] p: given that 12 R ~ s ​ C min 2 ​ κ ~ ​ 2 ​ L μ ​ r ​ log ⁡ 4 ​ d δ T 0 ≤ 1 d \frac{12}{\tilde{R}_{s}C_{\min}^{2}\tilde{\kappa}}\sqrt{\frac{2L_{\mu}r\log\frac{4d}{\delta}}{T_{0}}}\leq\frac{1}{\sqrt{d}} , which is true when T 0 ≳ C min − 4 ​ κ ~ − 2 ​ d ​ r ​ log ⁡ d δ T_{0}\gtrsim C_{\min}^{-4}\tilde{\kappa}^{-2}dr\log\frac{d}{\delta} . ∎

[343] h6: Proof of Lemma C.4 .

[344] p: By Taylor’s expansion with integral remainder, we have

[345] table: ℒ T 0 ​ ( 𝚯 ⋆ + Δ ) − ℒ T 0 ​ ( 𝚯 ⋆ ) − ⟨ ∇ ℒ T 0 ​ ( 𝚯 ⋆ ) , Δ ⟩ \displaystyle{\mathcal{L}}_{T_{0}}(\bm{\Theta}_{\star}+\Delta)-{\mathcal{L}}_{T_{0}}(\bm{\Theta}_{\star})-\langle\nabla{\mathcal{L}}_{T_{0}}(\bm{\Theta}_{\star}),\Delta\rangle = 1 T 0 ​ ∑ t = 1 T 0 { m ⁡ ( ⟨ 𝚯 ⋆ + Δ , 𝑿 t ⟩ ) − m ⁡ ( ⟨ 𝚯 ⋆ , 𝑿 t ⟩ ) − ⟨ 𝚯 ⋆ , 𝑿 t ⟩ ​ m ′ ​ ( ⟨ 𝚯 ⋆ , 𝑿 t ⟩ ) } \displaystyle=\frac{1}{T_{0}}\sum_{t=1}^{T_{0}}\left\{m(\langle\bm{\Theta}_{\star}+\Delta,{\bm{X}}_{t}\rangle)-m(\langle\bm{\Theta}_{\star},{\bm{X}}_{t}\rangle)-\langle\bm{\Theta}_{\star},{\bm{X}}_{t}\rangle m^{\prime}(\langle\bm{\Theta}_{\star},{\bm{X}}_{t}\rangle)\right\} = 1 T 0 ​ ∑ t = 1 T 0 ⟨ Δ , 𝑿 t ⟩ 2 ​ ∫ 0 1 ( 1 − z ) ​ m ′′ ​ ( ⟨ 𝚯 ⋆ + z ​ Δ , 𝑿 t ⟩ ) ⏟ = μ ˙ ​ ( ⟨ 𝚯 ⋆ + z ​ Δ , 𝑿 t ⟩ ) ​ 𝑑 z . \displaystyle=\frac{1}{T_{0}}\sum_{t=1}^{T_{0}}\langle\Delta,{\bm{X}}_{t}\rangle^{2}\int_{0}^{1}(1-z)\underbrace{m^{\prime\prime}\left(\langle\bm{\Theta}_{\star}+z\Delta,{\bm{X}}_{t}\rangle\right)}_{=\dot{\mu}\left(\langle\bm{\Theta}_{\star}+z\Delta,{\bm{X}}_{t}\rangle\right)}dz.

[346] p: We now divide into two cases:

[347] p: μ \mu is self-concordant. If this is the case, then we can utilize the following self-concordance control lemma:

[348] h6: Lemma C.5 (Lemma 9 of Abeille et al. (2021) ) .

[349] p: For any R s R_{s} -self-concordant μ \mu that is monotone increasing, the following holds: for any z 1 , z 2 ∈ ℝ z_{1},z_{2}\in{\mathbb{R}} ,

[350] table: μ ˙ ​ ( z 2 ) ​ exp ⁡ ( − R s ​ | z 1 − z 2 | ) ≤ μ ˙ ​ ( z 1 ) ≤ μ ˙ ​ ( z 2 ) ​ exp ⁡ ( R s ​ | z 1 − z 2 | ) . \dot{\mu}(z_{2})\exp(-R_{s}|z_{1}-z_{2}|)\leq\dot{\mu}(z_{1})\leq\dot{\mu}(z_{2})\exp(R_{s}|z_{1}-z_{2}|). (32)

[351] p: We choose R = 1 d R=\frac{1}{\sqrt{d}} , which implies that by Hölder’s inequality, | ⟨ Δ , 𝑿 t ⟩ | ≤ 1 |\langle\Delta,{\bm{X}}_{t}\rangle|\leq 1 . Thus, by the above self-concordance lemma,

[352] table: ∫ 0 1 ( 1 − z ) ​ μ ˙ ​ ( ⟨ 𝚯 ⋆ + z ​ Δ , 𝑿 t ⟩ ) ​ 𝑑 z ≥ ∫ 0 1 ( 1 − z ) ​ e − R s ​ z ​ μ ˙ ​ ( ⟨ 𝚯 ⋆ , 𝑿 t ⟩ ) ​ 𝑑 z ≥ κ ⋆ ​ R ~ s , \int_{0}^{1}(1-z)\dot{\mu}\left(\langle\bm{\Theta}_{\star}+z\Delta,{\bm{X}}_{t}\rangle\right)dz\geq\int_{0}^{1}(1-z)e^{-R_{s}z}\dot{\mu}\left(\langle\bm{\Theta}_{\star},{\bm{X}}_{t}\rangle\right)dz\geq\kappa_{\star}\tilde{R}_{s},

[353] p: where we define the constant

[354] table: R ~ s := { 1 2 , R s = 0 R s − 1 + e − R s R s 2 , R s > 0 . \tilde{R}_{s}:=\begin{cases}\frac{1}{2},&\quad$R_{s}=0$\\ \frac{R_{s}-1+e^{-R_{s}}}{R_{s}^{2}},&\quad$R_{s}>0$.\end{cases}

[355] p: Otherwise. If not, then we simply lower bound

[356] table: ∫ 0 1 ( 1 − z ) ​ μ ˙ ​ ( ⟨ 𝚯 ⋆ + z ​ Δ , 𝑿 t ⟩ ) ​ 𝑑 z ≥ κ ​ ∫ 0 1 ( 1 − z ) ​ 𝑑 z = κ 2 . \int_{0}^{1}(1-z)\dot{\mu}\left(\langle\bm{\Theta}_{\star}+z\Delta,{\bm{X}}_{t}\rangle\right)dz\geq\kappa\int_{0}^{1}(1-z)dz=\frac{\kappa}{2}.

[357] p: With a slight overload of notation, if self-concordance does not hold, we define R ~ s = 1 2 \tilde{R}_{s}=\frac{1}{2} .

[358] p: Concluding the proof. Let us define the vectorized population and empirical design matrices:

[359] table: 𝑽 := 𝔼 𝑿 ​ [ vec ⁡ ( 𝑿 ) ​ vec ​ ( 𝑿 ) ⊤ ] , 𝑽 ^ := 1 T 0 ​ ∑ t = 1 T 0 vec ⁡ ( 𝑿 t ) ​ vec ​ ( 𝑿 t ) ⊤ . {\bm{V}}:=\mathbb{E}_{{\bm{X}}}\left[\mathrm{\mathrm{vec}}({\bm{X}})\mathrm{\mathrm{vec}}({\bm{X}})^{\top}\right],\quad\widehat{{\bm{V}}}:=\frac{1}{T_{0}}\sum_{t=1}^{T_{0}}\mathrm{vec}({\bm{X}}_{t})\mathrm{vec}({\bm{X}}_{t})^{\top}. (33)

[360] p: Observe that

[361] table: 𝑽 \displaystyle{\bm{V}} = 𝔼 ϕ 1 , ϕ 2 ​ [ ( ϕ 2 ⊗ ϕ 1 ) ​ ( ϕ 2 ⊗ ϕ 1 ) ⊤ ] \displaystyle=\mathbb{E}_{\bm{\phi}^{1},\bm{\phi}^{2}}\left[(\bm{\phi}^{2}\otimes\bm{\phi}^{1})(\bm{\phi}^{2}\otimes\bm{\phi}^{1})^{\top}\right] ( vec ⁡ ( 𝒂 ​ 𝒃 ⊤ ) = 𝒃 ⊗ 𝒂 \mathrm{vec}({\bm{a}}{\bm{b}}^{\top})={\bm{b}}\otimes{\bm{a}} ) = 𝔼 ϕ 1 , ϕ 2 ​ [ ( ϕ 2 ​ ( ϕ 2 ) ⊤ ) ⊗ ( ϕ 1 ​ ( ϕ 1 ) ⊤ ) ] \displaystyle=\mathbb{E}_{\bm{\phi}^{1},\bm{\phi}^{2}}\left[(\bm{\phi}^{2}(\bm{\phi}^{2})^{\top})\otimes(\bm{\phi}^{1}(\bm{\phi}^{1})^{\top})\right] (mixed product property of the Kronecker product) = 𝔼 ϕ ​ [ ϕ ​ ϕ ⊤ ] ⊗ 2 , \displaystyle=\mathbb{E}_{\bm{\phi}}\left[\bm{\phi}\bm{\phi}^{\top}\right]^{\otimes 2}, ( ϕ 1 ​ = 𝑑 ​ ϕ 2 \bm{\phi}^{1}\overset{d}{=}\bm{\phi}^{2} )

[362] p: and thus, λ min ​ ( 𝑽 ) = λ min ​ ( 𝔼 ϕ ​ [ ϕ ​ ϕ ⊤ ] ) 2 ≥ C min 2 \lambda_{\min}\left({\bm{V}}\right)=\lambda_{\min}\left(\mathbb{E}_{\bm{\phi}}\left[\bm{\phi}\bm{\phi}^{\top}\right]\right)^{2}\geq C_{\min}^{2} by Assumption 1 .

[363] p: Thus, we have that

[364] table: ℒ T 0 ​ ( 𝚯 ⋆ + Δ ) − ℒ T 0 ​ ( 𝚯 ⋆ ) − ⟨ ∇ ℒ T 0 ​ ( 𝚯 ⋆ ) , Δ ⟩ \displaystyle{\mathcal{L}}_{T_{0}}(\bm{\Theta}_{\star}+\Delta)-{\mathcal{L}}_{T_{0}}(\bm{\Theta}_{\star})-\langle\nabla{\mathcal{L}}_{T_{0}}(\bm{\Theta}_{\star}),\Delta\rangle ≥ R ~ s ​ κ ~ ​ vec ​ ( Δ ) ⊤ ​ 𝑽 ^ ​ vec ​ ( Δ ) \displaystyle\geq\tilde{R}_{s}\tilde{\kappa}\mathrm{vec}(\Delta)^{\top}\widehat{{\bm{V}}}\mathrm{vec}(\Delta) = R ~ s ​ κ ~ ​ vec ​ ( Δ ) ⊤ ​ 𝑽 ​ vec ​ ( Δ ) + R ~ s ​ κ ~ ​ vec ​ ( Δ ) ⊤ ​ ( 𝑽 ^ − 𝑽 ) ​ vec ​ ( Δ ) \displaystyle=\tilde{R}_{s}\tilde{\kappa}\mathrm{vec}(\Delta)^{\top}{\bm{V}}\mathrm{vec}(\Delta)+\tilde{R}_{s}\tilde{\kappa}\mathrm{vec}(\Delta)^{\top}(\widehat{{\bm{V}}}-{\bm{V}})\mathrm{vec}(\Delta) ≥ R ~ s ​ κ ~ ​ C min 2 ​ ‖ Δ ‖ F 2 − R ~ s ​ κ ~ ​ | vec ​ ( Δ ) ⊤ ​ ( 𝑽 ^ − 𝑽 ) ​ vec ​ ( Δ ) | ⏟ ≜ ℰ T 0 \displaystyle\geq\tilde{R}_{s}\tilde{\kappa}C_{\min}^{2}\left\lVert\Delta\right\rVert_{F}^{2}-\tilde{R}_{s}\tilde{\kappa}\underbrace{\left|\mathrm{vec}(\Delta)^{\top}(\widehat{{\bm{V}}}-{\bm{V}})\mathrm{vec}(\Delta)\right|}_{\triangleq{\mathcal{E}}_{T_{0}}}

[365] p: Using the standard empirical process theory and peeling argument over the ball 𝔹 F ​ ( R ) \mathbb{B}_{F}(R) (see, e.g., proof of Wainwright (2019, Theorem 10.17) ), one can establish that the deviation is uniformly bounded as

[366] table: ℙ ⁡ ( ℰ T 0 ≤ R ~ s ​ κ ~ ​ C min 2 2 ​ ‖ Δ ‖ F 2 ) ≥ 1 − δ 2 , {\mathbb{P}}\left({\mathcal{E}}_{T_{0}}\leq\frac{\tilde{R}_{s}\tilde{\kappa}C_{\min}^{2}}{2}\left\lVert\Delta\right\rVert_{F}^{2}\right)\geq 1-\frac{\delta}{2}, (34)

[367] p: provided T 0 ≳ C min − 4 ​ κ ~ − 2 ​ d ​ r ​ log ⁡ d δ T_{0}\gtrsim C_{\min}^{-4}\tilde{\kappa}^{-2}dr\log\frac{d}{\delta} . ∎

[368] h2: Appendix D Discussions on Regrets

[369] h3: D.1 Four Regret Definitions and Discussions

[370] p: A standard measure of performance in online learning is regret . However, because the interaction is two-player and self-play, there are several ways to define regret, arising from different yet closely related communities: no-regret learning in games, dueling bandits/RL, and RL in two-player zero-sum games. In the main text, we consider only two regrets ( ABR ​ - ​ Reg η \mathrm{ABR\text{-}Reg}_{\color[rgb]{0.75,0,0.25}\eta} and MBR ​ - ​ Reg η \mathrm{MBR\text{-}Reg}_{\color[rgb]{0.75,0,0.25}\eta} ) for brevity, and so in this Appendix, we provide the deferred discussions regarding four regrets:

[371] h6: Definition D.1 .

[372] h4: Categorization Criteria.

[373] p: There are two criteria that determine each regret definition. The first criterion is, at each time t t , whether to consider the regrets of both players simultaneously, or to consider the regret of the max-player only. This distinguishes between Average or Max . The second criterion is whether to compare against a fixed comparator or to compare against the best response at each time t t , which is usually time-varying. This distinguishes between Nash and Best-Response .

[374] p: Intuitively, the Average regret definitions consider the “suboptimality” of both policies simultaneously. The difference between Nash and Best-Response is whether the regret is defined w.r.t. a fixed comparator ( Nash ) or a dynamically changing comparator ( Best-Response ). Thus, in classical literature, they are also known as external and internal (swap) regrets.

[375] h4: Average Regrets.

[376] p: AN ​ - ​ Reg ​ ( T ) \mathrm{AN\text{-}Reg}(T) is the notion originally considered in the seminal work of Freund and Schapire (1999) , followed by numerous works on no-regret learning dynamics in games ( Daskalakis et al., 2011 ; Daskalakis et al., 2015 ; Daskalakis et al., 2018 ; Rakhlin and Sridharan, 2013a ; Rakhlin and Sridharan, 2013b ; Syrgkanis et al., 2015 ) , recently adopted to game-theoretic LLM alignment ( Zhang et al., 2025c ) . AN ​ - ​ Reg ​ ( T ) \mathrm{AN\text{-}Reg}(T) is precisely the regret considered in contextual dueling bandits ( Dudík et al., 2015 , Eqn. (3)) and dueling RL ( Saha et al., 2023 , Eqn. (4)) ; indeed, for any π ∈ Π \pi\in\Pi , utilizing the anti-symmetry of J ⁡ ( ⋅ , ⋅ ) J(\cdot,\cdot) , we can rewrite J ⁡ ( π , π ^ t 2 ) − J ⁡ ( π ^ t 1 , π ) = J ⁡ ( π , π ^ t 1 ) + J ⁡ ( π , π ^ t 2 ) − 1 . J(\pi,{\color[rgb]{1,0,0}\hat{\pi}_{t}^{2}})-J({\color[rgb]{0,0,1}\hat{\pi}_{t}^{1}},\pi)=J(\pi,{\color[rgb]{0,0,1}\hat{\pi}_{t}^{1}})+J(\pi,{\color[rgb]{1,0,0}\hat{\pi}_{t}^{2}})-1. This also slightly resembles Borda regret in dueling bandits ( Saha et al., 2021 ; Wu et al., 2024 ) , and average regret in dueling bandits under linear stochastic transitivity ( Saha, 2021 ; Bengs et al., 2021 ; Bengs et al., 2022 ) .

[377] p: On the other hand, ABR ​ - ​ Reg ​ ( T ) \mathrm{ABR\text{-}Reg}(T) strongly resembles the notion of best response regret in adversarial dueling bandits ( Saha and Krishnamurthy, 2022 , Eqn. (1)) , but there is a key difference. In Saha and Krishnamurthy (2022) , the comparator at time t t is the same for both players, whereas in our regret setting, it differs for each player. Basically, each player must compete with the worst-case (strongest) adversary from her perspective, who chooses the best response from his perspective.

[378] h4: Max Regrets.

[379] p: The notion of considering the regret of the max player dates back to the self-play framework for RL in two-player zero-sum games ( Bai and Jin, 2020 ; Bai et al., 2020 ; Liu et al., 2021 ; Jin et al., 2022 ; Xiong et al., 2022 ) ; this idea has been recently applied to theoretical analyses of online RLHF under general preference ( Ye et al., 2024 ; Wu et al., 2025a ) . Basically, the intuition is that the learner only cares about obtaining the NE policy for the max-player, which is the policy that is actually deployed in practice.

[380] p: Note that the min-player’s policies π ^ t 2 {\color[rgb]{1,0,0}\hat{\pi}_{t}^{2}} do not contribute to the regret at all, and thus, often, the min-player acts as an exploration agent whose sole role is to collect as much information as possible to facilitate the learning of the max-player ( Bai and Jin, 2020 ; Bai et al., 2020 ; Liu et al., 2021 ; Jin et al., 2022 ; Xiong et al., 2022 ; Xiong et al., 2024 ; Ye et al., 2024 ) .

[381] h3: D.2 Online-to-Batch Conversion

[382] p: A standard consequence of no-regret learning in repeated zero-sum games is an online-to-batch conversion : the time-averaged (mixed) policies form an approximate Nash equilibrium. We formalize this statement in the following proposition.

[383] h6: Proposition D.2 (Online-to-batch conversion) .

[384] p: Let { ( π ^ t 1 , π ^ t 2 ) } t = 1 T ⊆ Π × Π \{(\hat{\pi}_{t}^{1},\hat{\pi}_{t}^{2})\}_{t=1}^{T}\subseteq\Pi\times\Pi be any policy sequence. Define the uniform mixture policies as π ¯ T i := 1 T ​ ∑ t = 1 T π ^ t i \bar{\pi}_{T}^{i}:=\frac{1}{T}\sum_{t=1}^{T}\hat{\pi}_{t}^{i} for i ∈ { 1 , 2 } i\in\{1,2\} and for simplicity, let us denote π ¯ T := π ¯ T 1 \bar{\pi}_{T}:=\bar{\pi}_{T}^{1} .

[385] p: (a) Average regrets. For average regrets, ( π ¯ T 1 , π ¯ T 2 ) (\bar{\pi}_{T}^{1},\bar{\pi}_{T}^{2}) is a Reg ⁡ ( T ) T \frac{\mathrm{Reg}(T)}{T} -approximate symmetric NE:

[386] table: max π 1 , π 2 ∈ Π ⁡ { J η ​ ( π 1 , π ¯ T 2 ) − J η ​ ( π ¯ T 1 , π 2 ) } ≤ AN ​ - ​ Reg η ​ ( T ) T ≤ ABR ​ - ​ Reg η ​ ( T ) T . \max_{\pi^{1},\pi^{2}\in\Pi}\Bigl\{J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1},\bar{\pi}_{T}^{2})-J_{\color[rgb]{0.75,0,0.25}\eta}(\bar{\pi}_{T}^{1},\pi^{2})\Bigr\}\;\leq\;\frac{\mathrm{AN\text{-}Reg}_{\color[rgb]{0.75,0,0.25}\eta}(T)}{T}\;\leq\;\frac{\mathrm{ABR\text{-}Reg}_{\color[rgb]{0.75,0,0.25}\eta}(T)}{T}.

[387] p: (b) Max regrets. For max regrets, π ¯ T \bar{\pi}_{T} is a 2 ​ R ​ e ​ g ​ ( T ) T \frac{2\mathrm{Reg}(T)}{T} -approximate symmetric NE:

[388] table: max π ∈ Π ⁡ { J η ​ ( π , π ¯ T ) − J η ​ ( π ¯ T , π ) } ≤ 2 ​ M ​ N ​ - ​ Reg η ​ ( T ) T ≤ 2 ​ M ​ B ​ R ​ - ​ Reg η ​ ( T ) T . \max_{\pi\in\Pi}\Bigl\{J_{\color[rgb]{0.75,0,0.25}\eta}(\pi,\bar{\pi}_{T})-J_{\color[rgb]{0.75,0,0.25}\eta}(\bar{\pi}_{T},\pi)\Bigr\}\;\leq\;\frac{2\mathrm{MN\text{-}Reg}_{\color[rgb]{0.75,0,0.25}\eta}(T)}{T}\;\leq\;\frac{2\mathrm{MBR\text{-}Reg}_{\color[rgb]{0.75,0,0.25}\eta}(T)}{T}.

[389] h6: Proof.

[390] p: (a) Fix any π 1 , π 2 ∈ Π \pi^{1},\pi^{2}\in\Pi . By the bilinearity of J J and Jensen’s inequality w.r.t. ψ ⁡ ( ⋅ ) \psi(\cdot) ,

[391] table: J η ​ ( π 1 , π ¯ T 2 ) = J ⁡ ( π 1 , π ¯ T 2 ) − η − 1 ​ ψ ​ ( π 1 ) + η − 1 ​ ψ ​ ( π ¯ T 2 ) ≤ 1 T ​ ∑ t = 1 T J η ​ ( π 1 , π ^ t 2 ) , J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1},\bar{\pi}_{T}^{2})=J(\pi^{1},\bar{\pi}_{T}^{2})-{\color[rgb]{0.75,0,0.25}\eta^{-1}}\psi(\pi^{1})+{\color[rgb]{0.75,0,0.25}\eta^{-1}}\psi(\bar{\pi}_{T}^{2})\leq\frac{1}{T}\sum_{t=1}^{T}J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1},\hat{\pi}_{t}^{2}),

[392] p: and similarly,

[393] table: J η ​ ( π ¯ T 1 , π 2 ) = J ⁡ ( π ¯ T 1 , π 2 ) − η − 1 ​ ψ ​ ( π ¯ T 1 ) + η − 1 ​ ψ ​ ( π 2 ) ≥ 1 T ​ ∑ t = 1 T J η ​ ( π ^ t 1 , π 2 ) . J_{\color[rgb]{0.75,0,0.25}\eta}(\bar{\pi}_{T}^{1},\pi^{2})=J(\bar{\pi}_{T}^{1},\pi^{2})-{\color[rgb]{0.75,0,0.25}\eta^{-1}}\psi(\bar{\pi}_{T}^{1})+{\color[rgb]{0.75,0,0.25}\eta^{-1}}\psi(\pi^{2})\geq\frac{1}{T}\sum_{t=1}^{T}J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi}_{t}^{1},\pi^{2}).

[394] p: Subtracting the two inequalities and taking max π 1 , π 2 \max_{\pi^{1},\pi^{2}} yields

[395] table: max π 1 , π 2 ⁡ { J η ​ ( π 1 , π ¯ T 2 ) − J η ​ ( π ¯ T 1 , π 2 ) } \displaystyle\max_{\pi^{1},\pi^{2}}\Bigl\{J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1},\bar{\pi}_{T}^{2})-J_{\color[rgb]{0.75,0,0.25}\eta}(\bar{\pi}_{T}^{1},\pi^{2})\Bigr\} ≤ 1 T ​ max ⁡ ∑ t = 1 T π 1 , π 2 ⁡ ( J η ​ ( π 1 , π ^ t 2 ) − J η ​ ( π ^ t 1 , π 2 ) ) \displaystyle\leq\frac{1}{T}\max_{\pi^{1},\pi^{2}}\sum_{t=1}^{T}\Bigl(J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1},\hat{\pi}_{t}^{2})-J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi}_{t}^{1},\pi^{2})\Bigr) ≤ 1 T ​ ∑ t = 1 T max π 1 , π 2 ⁡ ( J η ​ ( π 1 , π ^ t 2 ) − J η ​ ( π ^ t 1 , π 2 ) ) \displaystyle\leq\frac{1}{T}\sum_{t=1}^{T}\max_{\pi^{1},\pi^{2}}\Bigl(J_{\color[rgb]{0.75,0,0.25}\eta}(\pi^{1},\hat{\pi}_{t}^{2})-J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi}_{t}^{1},\pi^{2})\Bigr)

[396] p: (b) By the same averaging argument (bilinearity of J J and Jensen’s inequality), for every π ∈ Π \pi\in\Pi ,

[397] table: J η ​ ( π , π ¯ T ) − J η ​ ( π ¯ T , π ) ≤ 1 T ​ ∑ t = 1 T ( J η ​ ( π , π ^ t 1 ) − J η ​ ( π ^ t 1 , π ) ) . J_{\color[rgb]{0.75,0,0.25}\eta}(\pi,\bar{\pi}_{T})-J_{\color[rgb]{0.75,0,0.25}\eta}(\bar{\pi}_{T},\pi)\leq\frac{1}{T}\sum_{t=1}^{T}\Bigl(J_{\color[rgb]{0.75,0,0.25}\eta}(\pi,\hat{\pi}_{t}^{1})-J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi}_{t}^{1},\pi)\Bigr).

[398] p: Since for each t t , J η ​ ( π , π ^ t 1 ) − J η ​ ( π ^ t 1 , π ) = 2 ​ ( 1 2 − J η ​ ( π ^ t 1 , π ) ) J_{\color[rgb]{0.75,0,0.25}\eta}(\pi,\hat{\pi}_{t}^{1})-J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi}_{t}^{1},\pi)=2\Bigl(\tfrac{1}{2}-J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi}_{t}^{1},\pi)\Bigr) , taking max π \max_{\pi} and substituting yields

[399] table: max π ⁡ { J η ​ ( π , π ¯ T ) − J η ​ ( π ¯ T , π ) } ≤ 2 T ​ max ⁡ ∑ t = 1 T π ⁡ ( 1 2 − J η ​ ( π ^ t 1 , π ) ) ≤ 2 T ​ ∑ t = 1 T max π ⁡ ( 1 2 − J η ​ ( π ^ t 1 , π ) ) . \displaystyle\max_{\pi}\bigl\{J_{\color[rgb]{0.75,0,0.25}\eta}(\pi,\bar{\pi}_{T})-J_{\color[rgb]{0.75,0,0.25}\eta}(\bar{\pi}_{T},\pi)\bigr\}\leq\frac{2}{T}\max_{\pi}\sum_{t=1}^{T}\Bigl(\tfrac{1}{2}-J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi}_{t}^{1},\pi)\Bigr)\leq\frac{2}{T}\sum_{t=1}^{T}\max_{\pi}\Bigl(\tfrac{1}{2}-J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi}_{t}^{1},\pi)\Bigr).

[400] p: ∎

[401] h2: Appendix E Eluder Dimension of GBPM

[402] h3: E.1 Upper Bounding the Eluder Dimension of Wu et al. (2025a)

[403] p: To instantiate the regret bound of Wu et al. (2025a) in Appendix F , we first recall their specific notion of the eluder dimension:

[404] h6: Definition E.1 (Eluder dimension, General Preference Model ( Wu et al., 2025a ) ) .

[405] p: Under the general preference model, for any 𝒟 t − 1 = { ( 𝐱 i , 𝐚 i 1 , 𝐚 i 2 ) } i = 1 t − 1 \mathcal{D}_{t-1}=\{({\bm{x}}_{i},{\bm{a}}^{1}_{i},{\bm{a}}^{2}_{i})\}_{i=1}^{t-1} , we define the uncertainty of ( 𝐱 , 𝐚 1 , 𝐚 2 ) ({\bm{x}},{\bm{a}}^{1},{\bm{a}}^{2}) with respect to 𝒫 \mathcal{P} as

[406] table: U GP ​ ( λ , 𝒙 , 𝒂 1 , 𝒂 2 , 𝒫 , 𝒟 t − 1 ) = sup P 1 , P 2 ∈ 𝒫 | P 1 ​ ( 𝒂 1 ≻ 𝒂 2 ∣ 𝒙 ) − P 2 ​ ( 𝒂 1 ≻ 𝒂 2 ∣ 𝒙 ) | λ + ∑ s = 1 t − 1 ( P 1 ​ ( 𝒂 s 1 ≻ 𝒂 s 2 ∣ 𝒙 s ) − P 2 ​ ( 𝒂 s 1 ≻ 𝒂 s 2 ∣ 𝒙 s ) ) 2 . U_{\texttt{GP}}(\lambda,{\bm{x}},{\bm{a}}^{1},{\bm{a}}^{2};\mathcal{P},\mathcal{D}_{t-1})=\sup_{P_{1},P_{2}\in\mathcal{P}}\frac{|P_{1}({\bm{a}}^{1}\succ{\bm{a}}^{2}\mid{\bm{x}})-P_{2}({\bm{a}}^{1}\succ{\bm{a}}^{2}\mid{\bm{x}})|}{\sqrt{\lambda+\sum_{s=1}^{t-1}(P_{1}({\bm{a}}^{1}_{s}\succ{\bm{a}}^{2}_{s}\mid{\bm{x}}_{s})-P_{2}({\bm{a}}^{1}_{s}\succ{\bm{a}}^{2}_{s}\mid{\bm{x}}_{s}))^{2}}}.

[407] p: Then the eluder dimension of 𝒫 {\mathcal{P}} is defined as

[408] table: d ( 𝒫 , λ , T ) := sup 𝒙 1 : T , 𝒂 1 1 : T , 𝒂 2 1 : T ∑ t ∈ [ T ] min { 1 , [ U GP ( λ , 𝒙 t , 𝒂 t 1 , 𝒂 t 2 ; 𝒫 , 𝒟 t − 1 ) ] 2 } . d(\mathcal{P},\lambda,T):=\sup_{{\bm{x}}_{1:T},{\bm{a}}^{1}_{1:T},{\bm{a}}^{2}_{1:T}}\sum_{t\in[T]}\min\left\{1,\left[U_{\texttt{GP}}(\lambda,{\bm{x}}_{t},{\bm{a}}^{1}_{t},{\bm{a}}^{2}_{t};\mathcal{P},\mathcal{D}_{t-1})\right]^{2}\right\}.

[409] p: Using the standard elliptical potential arguments, we now derive an upper bound for this complexity measure under the GBPM:

[410] h6: Proposition E.2 .

[411] h6: Proof.

[412] p: For the proof, let us arbitrarily fix a sequence of context-action-action pairs ( 𝒙 1 : T , 𝒂 1 : T 1 , 𝒂 1 : T 2 ) ({\bm{x}}_{1:T},{\bm{a}}^{1}_{1:T},{\bm{a}}^{2}_{1:T}) , and let us denote the induced sequence of features as ϕ 1 : T 1 \bm{\phi}_{1:T}^{1} and ϕ 1 : T 2 \bm{\phi}_{1:T}^{2} , where ϕ t i := ϕ ⁡ ( 𝒙 t , 𝒂 t i ) \bm{\phi}_{t}^{i}:=\bm{\phi}({\bm{x}}_{t},{\bm{a}}_{t}^{i}) for t ∈ [ T ] t\in[T] and i ∈ { 1 , 2 } . i\in\{1,2\}. Let us also denote 𝚽 t := ϕ t 1 ​ ( ϕ t 2 ) ⊤ \bm{\Phi}_{t}:=\bm{\phi}_{t}^{1}(\bm{\phi}_{t}^{2})^{\top} . For any 𝚯 ∈ Θ \bm{\Theta}\in\Theta , the induced preference model is defined as

[413] table: P 𝚯 ( ϕ t 1 , ϕ t 2 ) := μ ( ( ϕ t 1 ) ⊤ 𝚯 ϕ t 2 ) = μ ( ⟨ 𝚯 , 𝚽 t ) . P_{\bm{\Theta}}(\bm{\phi}_{t}^{1},\bm{\phi}_{t}^{2}):=\mu\left((\bm{\phi}_{t}^{1})^{\top}\bm{\Theta}\phi_{t}^{2}\right)=\mu\left(\langle\bm{\Theta},\bm{\Phi}_{t}\right). (35)

[414] p: We bound the uncertainty via the elliptical potential lemma ( Lemma G.3 ). Let us denote P i = P 𝚯 i P_{i}=P_{\bm{\Theta}_{i}} for some arbitrary 𝚯 i ∈ Θ . \bm{\Theta}_{i}\in\Theta. We first upper bound the numerator as follows: denoting α ⁡ ( 𝒙 , 𝜽 1 , 𝜽 2 ) ≔ ∫ 0 1 μ ˙ ​ ( 𝒙 ⊤ ​ 𝜽 1 + z ​ 𝒙 ⊤ ​ ( 𝜽 2 − 𝜽 1 ) ) ​ 𝑑 z \alpha({\bm{x}},{\bm{\theta}}_{1},{\bm{\theta}}_{2})\coloneqq\int_{0}^{1}\dot{\mu}\bigl({\bm{x}}^{\top}{\bm{\theta}}_{1}+z\,{\bm{x}}^{\top}({\bm{\theta}}_{2}-{\bm{\theta}}_{1})\bigr)\,dz for 𝒙 , 𝜽 1 , 𝜽 2 ∈ ℝ d {\bm{x}},{\bm{\theta}}_{1},{\bm{\theta}}_{2}\in{\mathbb{R}}^{d} ,

[415] table: | μ ⁡ ( ⟨ 𝚯 1 , 𝚽 t ⟩ ) − μ ⁡ ( ⟨ 𝚯 2 , 𝚽 t ⟩ ) | \displaystyle\left|\mu\left(\langle\bm{\Theta}_{1},\bm{\Phi}_{t}\rangle\right)-\mu\left(\langle\bm{\Theta}_{2},\bm{\Phi}_{t}\rangle\right)\right| = | α ⁡ ( vec ⁡ ( 𝚽 t ) , vec ⁡ ( 𝚯 1 ) , vec ⁡ ( 𝚯 2 ) ) ​ ⟨ 𝚯 1 − 𝚯 2 , 𝚽 t ⟩ | \displaystyle\quad=\left|\alpha\!\left(\operatorname{vec}(\bm{\Phi}_{t}),\operatorname{vec}(\bm{\Theta}_{1}),\operatorname{vec}(\bm{\Theta}_{2})\right)\langle\bm{\Theta}_{1}-\bm{\Theta}_{2},\bm{\Phi}_{t}\rangle\right| (Mean-value theorem) = | ⟨ 𝚯 1 − 𝚯 2 , α ⁡ ( vec ⁡ ( 𝚽 t ) , vec ⁡ ( 𝚯 1 ) , vec ⁡ ( 𝚯 2 ) ) ​ 𝚽 t ⏟ ≜ 𝚽 ¯ t ​ ( 𝚯 1 , 𝚯 2 ) ⟩ | \displaystyle\quad=\left|\left\langle\bm{\Theta}_{1}-\bm{\Theta}_{2},\underbrace{\alpha\!\left(\operatorname{vec}(\bm{\Phi}_{t}),\operatorname{vec}(\bm{\Theta}_{1}),\operatorname{vec}(\bm{\Theta}_{2})\right)\bm{\Phi}_{t}}_{\triangleq\bar{\bm{\Phi}}_{t}(\bm{\Theta}_{1},\bm{\Theta}_{2})}\right\rangle\right| ≤ ‖ vec ⁡ ( 𝚯 1 − 𝚯 2 ) ‖ 𝑮 t ​ ( 𝚯 1 , 𝚯 2 ) ​ ‖ vec ⁡ ( 𝚽 ¯ t ​ ( 𝚯 1 , 𝚯 2 ) ) ‖ 𝑮 t ​ ( 𝚯 1 , 𝚯 2 ) − 1 \displaystyle\quad\leq\left\lVert\mathrm{vec}(\bm{\Theta}_{1}-\bm{\Theta}_{2})\right\rVert_{{\bm{G}}_{t}(\bm{\Theta}_{1},\bm{\Theta}_{2})}\left\lVert\mathrm{vec}(\bar{\bm{\Phi}}_{t}(\bm{\Theta}_{1},\bm{\Theta}_{2}))\right\rVert_{{\bm{G}}_{t}(\bm{\Theta}_{1},\bm{\Theta}_{2})^{-1}} (Cauchy-Schwarz inequality)

[416] p: for some matrix 𝑮 t ​ ( 𝚯 1 , 𝚯 2 ) ≻ 𝟎 {\bm{G}}_{t}(\bm{\Theta}_{1},\bm{\Theta}_{2})\succ{\bm{0}} to be determined later.

[417] p: For the denominator squared:

[418] table: λ + ∑ s = 1 t − 1 ( μ ⁡ ( ⟨ 𝚯 1 , 𝚽 s ⟩ ) − μ ⁡ ( ⟨ 𝚯 2 , 𝚽 s ⟩ ) ) 2 \displaystyle\lambda+\sum_{s=1}^{t-1}\left(\mu\left(\langle\bm{\Theta}_{1},\bm{\Phi}_{s}\rangle\right)-\mu\left(\langle\bm{\Theta}_{2},\bm{\Phi}_{s}\rangle\right)\right)^{2} = λ + ∑ s = 1 t − 1 [ α ​ ( vec ⁡ ( 𝚽 s ) , vec ⁡ ( 𝚯 1 ) , vec ⁡ ( 𝚯 2 ) ) 2 ​ ⟨ 𝚯 1 − 𝚯 2 , 𝚽 s ⟩ 2 ] \displaystyle=\lambda+\sum_{s=1}^{t-1}\left[\alpha\!\left(\operatorname{vec}(\bm{\Phi}_{s}),\operatorname{vec}(\bm{\Theta}_{1}),\operatorname{vec}(\bm{\Theta}_{2})\right)^{2}\langle\bm{\Theta}_{1}-\bm{\Theta}_{2},\bm{\Phi}_{s}\rangle^{2}\right] = λ + vec ⁡ ( 𝚯 1 − 𝚯 2 ) ⊤ ​ [ ∑ s = 1 t − 1 ( α ​ ( vec ⁡ ( 𝚽 s ) , vec ⁡ ( 𝚯 1 ) , vec ⁡ ( 𝚯 2 ) ) 2 ​ vec ⁡ ( 𝚽 s ) ​ vec ​ ( 𝚽 s ) ⊤ ) ] ​ vec ⁡ ( 𝚯 1 − 𝚯 2 ) \displaystyle=\lambda+\operatorname{vec}\!\left(\bm{\Theta}_{1}-\bm{\Theta}_{2}\right)^{\top}\left[\sum_{s=1}^{t-1}\left(\alpha\!\left(\operatorname{vec}(\bm{\Phi}_{s}),\operatorname{vec}(\bm{\Theta}_{1}),\operatorname{vec}(\bm{\Theta}_{2})\right)^{2}\operatorname{vec}(\bm{\Phi}_{s})\,\operatorname{vec}(\bm{\Phi}_{s})^{\top}\right)\right]\operatorname{vec}\!\left(\bm{\Theta}_{1}-\bm{\Theta}_{2}\right) ≥ vec ​ ( 𝚯 1 − 𝚯 2 ) ⊤ ​ [ λ 4 ​ S 2 ​ 𝑰 + ∑ s = 1 t − 1 [ α ​ ( vec ⁡ ( 𝚽 s ) , vec ⁡ ( 𝚯 1 ) , vec ⁡ ( 𝚯 2 ) ) 2 ​ vec ⁡ ( 𝚽 s ) ​ vec ​ ( 𝚽 s ) ⊤ ] ] ⏟ ≜ 𝑮 t ​ ( 𝚯 1 , 𝚯 2 ) ​ vec ​ ( 𝚯 1 − 𝚯 2 ) \displaystyle\geq\mathrm{vec}(\bm{\Theta}_{1}-\bm{\Theta}_{2})^{\top}\underbrace{\left[\frac{\lambda}{4S^{2}}{\bm{I}}+\sum_{s=1}^{t-1}\!\left[\alpha\!\left(\operatorname{vec}(\bm{\Phi}_{s}),\operatorname{vec}(\bm{\Theta}_{1}),\operatorname{vec}(\bm{\Theta}_{2})\right)^{2}\operatorname{vec}(\bm{\Phi}_{s})\operatorname{vec}(\bm{\Phi}_{s})^{\top}\right]\right]}_{\triangleq{\bm{G}}_{t}(\bm{\Theta}_{1},\bm{\Theta}_{2})}\mathrm{vec}(\bm{\Theta}_{1}-\bm{\Theta}_{2}) = ‖ vec ⁡ ( 𝚯 1 − 𝚯 2 ) ‖ 𝑮 t ​ ( 𝚯 1 , 𝚯 2 ) 2 . \displaystyle=\left\lVert\mathrm{vec}(\bm{\Theta}_{1}-\bm{\Theta}_{2})\right\rVert_{{\bm{G}}_{t}(\bm{\Theta}_{1},\bm{\Theta}_{2})}^{2}.

[419] p: Combining the above two inequalities, we have that

[420] table: U GP ​ ( λ , 𝒙 , 𝒂 1 , 𝒂 2 , 𝒫 , 𝒟 t − 1 ) \displaystyle U_{\texttt{GP}}(\lambda,{\bm{x}},{\bm{a}}^{1},{\bm{a}}^{2};\mathcal{P},\mathcal{D}_{t-1}) ≤ sup 𝚯 1 , 𝚯 2 ∈ Θ ‖ vec ⁡ ( 𝚯 1 − 𝚯 2 ) ‖ 𝑮 t ​ ‖ vec ⁡ ( 𝚽 ¯ t ​ ( 𝚯 1 , 𝚯 2 ) ) ‖ 𝑮 t ​ ( 𝚯 1 , 𝚯 2 ) − 1 ‖ vec ⁡ ( 𝚯 1 − 𝚯 2 ) ‖ 𝑮 t ​ ( 𝚯 1 , 𝚯 2 ) \displaystyle\leq\sup_{\bm{\Theta}_{1},\bm{\Theta}_{2}\in\Theta}\frac{\left\lVert\mathrm{vec}(\bm{\Theta}_{1}-\bm{\Theta}_{2})\right\rVert_{{\bm{G}}_{t}}\left\lVert\mathrm{vec}(\bar{\bm{\Phi}}_{t}(\bm{\Theta}_{1},\bm{\Theta}_{2}))\right\rVert_{{\bm{G}}_{t}(\bm{\Theta}_{1},\bm{\Theta}_{2})^{-1}}}{\left\lVert\mathrm{vec}(\bm{\Theta}_{1}-\bm{\Theta}_{2})\right\rVert_{{\bm{G}}_{t}(\bm{\Theta}_{1},\bm{\Theta}_{2})}} = sup 𝚯 1 , 𝚯 2 ∈ Θ ‖ vec ⁡ ( 𝚽 ¯ t ​ ( 𝚯 1 , 𝚯 2 ) ) ‖ 𝑮 t ​ ( 𝚯 1 , 𝚯 2 ) − 1 \displaystyle=\sup_{\bm{\Theta}_{1},\bm{\Theta}_{2}\in\Theta}\left\lVert\mathrm{vec}(\bar{\bm{\Phi}}_{t}(\bm{\Theta}_{1},\bm{\Theta}_{2}))\right\rVert_{{\bm{G}}_{t}(\bm{\Theta}_{1},\bm{\Theta}_{2})^{-1}}

[421] p: We can lower-bound 𝑮 t ​ ( 𝚯 1 , 𝚯 2 ) {\bm{G}}_{t}(\bm{\Theta}_{1},\bm{\Theta}_{2}) in the Löwner sense using the fact that α ⁡ ( ⋅ , ⋅ , ⋅ ) ≥ κ \alpha(\cdot,\cdot,\cdot)\geq\kappa ,

[422] table: 𝑮 t ​ ( 𝚯 1 , 𝚯 2 ) ⪰ λ 4 ​ S 2 ​ 𝑰 + ∑ s = 1 t − 1 κ 2 ​ vec ⁡ ( 𝚽 s ) ​ vec ​ ( 𝚽 s ) ⊤ = λ 4 ​ S 2 ​ 𝑰 + ∑ s = 1 t − 1 vec ⁡ ( κ ​ 𝚽 s ) ​ vec ​ ( κ ​ 𝚽 s ) ⊤ ≜ 𝑽 t . {\bm{G}}_{t}(\bm{\Theta}_{1},\bm{\Theta}_{2})\succeq\frac{\lambda}{4S^{2}}{\bm{I}}+\sum_{s=1}^{t-1}\kappa^{2}\operatorname{vec}({\bm{\Phi}}_{s})\operatorname{vec}({\bm{\Phi}}_{s})^{\top}=\frac{\lambda}{4S^{2}}{\bm{I}}+\sum_{s=1}^{t-1}\operatorname{vec}(\kappa{\bm{\Phi}}_{s})\operatorname{vec}(\kappa{\bm{\Phi}}_{s})^{\top}\triangleq{\bm{V}}_{t}.

[423] p: Then, as α ⁡ ( ⋅ , ⋅ , ⋅ ) ≤ L μ \alpha(\cdot,\cdot,\cdot)\leq L_{\mu} , we have that

[424] table: U GP ​ ( λ , 𝒙 , 𝒂 1 , 𝒂 2 , 𝒫 , 𝒟 t − 1 ) ≤ L μ κ ​ ‖ vec ⁡ ( κ ​ 𝚽 t ) ‖ 𝑽 t − 1 . U_{\texttt{GP}}(\lambda,{\bm{x}},{\bm{a}}^{1},{\bm{a}}^{2};\mathcal{P},\mathcal{D}_{t-1})\leq\frac{L_{\mu}}{\kappa}\left\lVert\operatorname{vec}(\kappa\bm{\Phi}_{t})\right\rVert_{{\bm{V}}_{t}^{-1}}. (36)

[425] p: We then conclude the proof via the elliptical potential lemma ( Lemma G.3 ):

[426] table: d ⁡ ( 𝒫 , λ , T ) \displaystyle d({\mathcal{P}},\lambda,T) ≤ ∑ t = 1 T min ⁡ { 1 , L μ 2 κ 2 ​ ‖ vec ⁡ ( κ ​ 𝚽 t ) ‖ 𝑽 t − 1 2 } \displaystyle\leq\sum_{t=1}^{T}\min\left\{1,\frac{L_{\mu}^{2}}{\kappa^{2}}\left\lVert\operatorname{vec}(\kappa\bm{\Phi}_{t})\right\rVert_{{\bm{V}}_{t}^{-1}}^{2}\right\} ≤ L μ 2 κ 2 ​ ∑ t = 1 T min ⁡ { 1 , ‖ vec ⁡ ( κ ​ 𝚽 t ) ‖ 𝑽 t − 1 2 } \displaystyle\leq\frac{L_{\mu}^{2}}{\kappa^{2}}\sum_{t=1}^{T}\min\left\{1,\left\lVert\operatorname{vec}(\kappa\bm{\Phi}_{t})\right\rVert_{{\bm{V}}_{t}^{-1}}^{2}\right\} ( κ ≤ L μ \kappa\leq L_{\mu} ) ≤ 2 ​ d 2 ​ L μ 2 κ 2 ​ log ⁡ ( 1 + 4 ​ κ 2 ​ S 2 ​ T d 2 ​ λ ) . \displaystyle\leq\frac{2d^{2}L_{\mu}^{2}}{\kappa^{2}}\log\left(1+\frac{4\kappa^{2}S^{2}T}{d^{2}\lambda}\right).

[427] p: ∎

[428] h3: E.2 Connection to the Standard Eluder Dimensions

[429] p: In this appendix, we will elucidate the connection between Definition E.1 and two other “standard” definitions of eluder-type complexities: sequential extrapolation coefficient (SEC) ( Xie et al., 2023 ) and the original eluder dimension ( Russo and Van Roy, 2013 ) For simplicity, we denote 𝒵 := 𝒳 × 𝒜 × 𝒜 {\mathcal{Z}}:={\mathcal{X}}\times{\mathcal{A}}\times{\mathcal{A}} , and P ⁡ ( 𝒛 ) := P ⁡ ( 𝒂 1 ≻ 𝒂 2 ∣ 𝒙 ) P({\bm{z}}):=P({\bm{a}}^{1}\succ{\bm{a}}^{2}\mid{\bm{x}}) for 𝒛 = ( 𝒙 , 𝒂 1 , 𝒂 2 ) {\bm{z}}=({\bm{x}},{\bm{a}}^{1},{\bm{a}}^{2}) .

[430] p: First, we recall the definition of SEC adopted for our setting:

[431] h6: Definition E.3 ( λ \lambda -regularized SEC, Definition 7 of Xie et al. (2023) ) .

[432] p: Let Π ⊆ Δ ⁡ ( 𝒵 ) \Pi\subseteq\Delta({\mathcal{Z}}) be a distribution class. Then, the SEC is defined as

[433] table: SEC λ ( 𝒫 , Π , T ) := sup P 1 : T 1 , P 1 : T 2 ⊆ 𝒫 sup ν 1 : T ⊆ Π ∑ t = 1 T ( 𝔼 𝒛 t ∼ ν t ​ [ P t 1 ​ ( 𝒛 t ) − P t 2 ​ ( 𝒛 t ) ] ) 2 λ + ∑ s = 1 t − 1 𝔼 𝒛 s ∼ ν s ​ [ ( P t 1 ​ ( 𝒛 s ) − P t 2 ​ ( 𝒛 s ) ) 2 ] . \mathrm{SEC}_{\lambda}({\mathcal{P}},\Pi,T):=\sup_{P_{1:T}^{1},P_{1:T}^{2}\subseteq{\mathcal{P}}}\ \sup_{\nu_{1:T}\subseteq\Pi}\sum_{t=1}^{T}\frac{\left(\mathbb{E}_{{\bm{z}}_{t}\sim\nu_{t}}[P_{t}^{1}({\bm{z}}_{t})-P_{t}^{2}({\bm{z}}_{t})]\right)^{2}}{\lambda+\sum_{s=1}^{t-1}\mathbb{E}_{{\bm{z}}_{s}\sim\nu_{s}}\big[(P_{t}^{1}({\bm{z}}_{s})-P_{t}^{2}({\bm{z}}_{s}))^{2}\big]}.

[434] p: Note that when the distribution class is restricted to the set of Dirac measures 𝑫 := { δ 𝒛 : 𝒛 ∈ Z } {\bm{D}}:=\{\delta_{{\bm{z}}}:{\bm{z}}\in Z\} , we have the following relationship between SEC and Definition E.1 :

[435] table: d ⁡ ( 𝒫 , λ , T ) \displaystyle d({\mathcal{P}},\lambda,T) = sup 𝒛 1 : T ∑ t ∈ [ T ] min { 1 , sup P 1 , P 2 ∈ 𝒫 ( P 1 ​ ( 𝒛 t ) − P 2 ​ ( 𝒛 t ) ) 2 λ + ∑ s = 1 t − 1 ( P 1 ​ ( 𝒛 s ) − P 2 ​ ( 𝒛 s ) ) 2 } \displaystyle=\sup_{{\bm{z}}_{1:T}}\sum_{t\in[T]}\min\left\{1,\sup_{P_{1},P_{2}\in\mathcal{P}}\frac{(P_{1}({\bm{z}}_{t})-P_{2}({\bm{z}}_{t}))^{2}}{\lambda+\sum_{s=1}^{t-1}(P_{1}({\bm{z}}_{s})-P_{2}({\bm{z}}_{s}))^{2}}\right\} ≤ sup 𝒛 1 : T ∑ t ∈ [ T ] sup P 1 , P 2 ∈ 𝒫 ( P 1 ​ ( 𝒛 t ) − P 2 ​ ( 𝒛 t ) ) 2 λ + ∑ s = 1 t − 1 ( P 1 ​ ( 𝒛 s ) − P 2 ​ ( 𝒛 s ) ) 2 \displaystyle\leq\sup_{{\bm{z}}_{1:T}}\sum_{t\in[T]}\sup_{P_{1},P_{2}\in\mathcal{P}}\frac{(P_{1}({\bm{z}}_{t})-P_{2}({\bm{z}}_{t}))^{2}}{\lambda+\sum_{s=1}^{t-1}(P_{1}({\bm{z}}_{s})-P_{2}({\bm{z}}_{s}))^{2}} = sup P 1 : T 1 , P 1 : T 2 sup 𝒛 1 : T ∑ t ∈ [ T ] ( P t 1 ​ ( 𝒛 t ) − P t 2 ​ ( 𝒛 t ) ) 2 λ + ∑ s = 1 t − 1 ( P s 1 ​ ( 𝒛 s ) − P s 2 ​ ( 𝒛 s ) ) 2 \displaystyle=\sup_{P_{1:T}^{1},P_{1:T}^{2}}\sup_{{\bm{z}}_{1:T}}\sum_{t\in[T]}\frac{(P_{t}^{1}({\bm{z}}_{t})-P_{t}^{2}({\bm{z}}_{t}))^{2}}{\lambda+\sum_{s=1}^{t-1}(P_{s}^{1}({\bm{z}}_{s})-P_{s}^{2}({\bm{z}}_{s}))^{2}} = sup P 1 : T 1 , P 1 : T 2 sup ν 1 : T ⊆ 𝑫 ∑ t ∈ [ T ] ( 𝔼 𝒛 t ∼ ν t ​ [ P t 1 ​ ( 𝒛 t ) − P t 2 ​ ( 𝒛 t ) ] ) 2 λ + ∑ s = 1 t − 1 ( 𝔼 𝒛 s ∼ ν s ​ [ P t 1 ​ ( 𝒛 s ) − P t 2 ​ ( 𝒛 s ) ] ) 2 \displaystyle=\sup_{P_{1:T}^{1},P_{1:T}^{2}}\sup_{\nu_{1:T}\subseteq{\bm{D}}}\sum_{t\in[T]}\frac{(\mathbb{E}_{{\bm{z}}_{t}\sim\nu_{t}}[P_{t}^{1}({\bm{z}}_{t})-P_{t}^{2}({\bm{z}}_{t})])^{2}}{\lambda+\sum_{s=1}^{t-1}(\mathbb{E}_{{\bm{z}}_{s}\sim\nu_{s}}[P_{t}^{1}({\bm{z}}_{s})-P_{t}^{2}({\bm{z}}_{s})])^{2}} = SEC λ ​ ( 𝒫 , 𝑫 , T ) . \displaystyle=\mathrm{SEC}_{\lambda}({\mathcal{P}},{\bm{D}},T).

[436] p: Second, we recall the standard eluder dimension of Foster et al. (2021) and Li et al. (2022a) : 10 10 10 The original definition is due to Russo and Van Roy (2013) and slightly different, but as mentioned in Li et al. (2022a) , the “new” definition is “never larger and is sufficient to analyze all the applications of eluder dimension in literature.”

[437] h6: Definition E.4 (Definition 1 of Li et al. (2022a) ) .

[438] p: For any fixed preference P ∗ ∈ 𝒫 P^{*}\in{\mathcal{P}} , and scale ε ≥ 0 \varepsilon\geq 0 , the exact eluder dimension Edim ¯ P ∗ ​ ( 𝒫 , ε ) \underline{\mathrm{Edim}}_{P^{*}}({\mathcal{P}},\varepsilon) is the largest m ∈ ℕ m\in{\mathbb{N}} such that there exists a sequence { ( 𝐳 t , P t ) } t ∈ [ m ] ⊂ 𝒵 × 𝒫 \{({\bm{z}}_{t},P_{t})\}_{t\in[m]}\subset{\mathcal{Z}}\times{\mathcal{P}} such that the following holds: for all t ∈ [ m ] t\in[m] ,

[439] table: | P t ​ ( 𝒛 t ) − P ∗ ​ ( 𝒛 t ) | > ε , and ∑ s < t ( P t ​ ( 𝒛 s ) − P ∗ ​ ( 𝒛 s ) ) 2 < ε 2 . \left|P_{t}({\bm{z}}_{t})-P^{*}({\bm{z}}_{t})\right|>\varepsilon,\quad\text{and}\quad\sum_{s<t}\left(P_{t}({\bm{z}}_{s})-P^{*}({\bm{z}}_{s})\right)^{2}<\varepsilon^{2}. (37)

[440] p: Then for all ε > 0 \varepsilon>0 , we define:

[441] p: The eluder dimension is Edim P ∗ ​ ( 𝒫 , ε ) := sup ε ′ ≥ ε Edim ¯ P ∗ ​ ( 𝒫 , ε ′ ) \mathrm{Edim}_{P^{*}}({\mathcal{P}},\varepsilon):=\sup_{\varepsilon^{\prime}\geq\varepsilon}\underline{\mathrm{Edim}}_{P^{*}}({\mathcal{P}},\varepsilon^{\prime}) .

[442] p: Edim ¯ ​ ( 𝒫 , ε ) := sup P ∗ ∈ 𝒫 Edim ¯ P ∗ ​ ( 𝒫 , ε ′ ) \underline{\mathrm{Edim}}({\mathcal{P}},\varepsilon):=\sup_{P^{*}\in{\mathcal{P}}}\underline{\mathrm{Edim}}_{P^{*}}({\mathcal{P}},\varepsilon^{\prime}) and Edim ⁡ ( 𝒫 , ε ) := sup P ∗ ∈ 𝒫 Edim P ∗ ​ ( 𝒫 , ε ′ ) \mathrm{Edim}({\mathcal{P}},\varepsilon):=\sup_{P^{*}\in{\mathcal{P}}}\mathrm{Edim}_{P^{*}}({\mathcal{P}},\varepsilon^{\prime}) .

[443] p: We first prove that Edim ⁡ ( 𝒫 , ε ) \mathrm{Edim}({\mathcal{P}},\varepsilon) and SEC λ ​ ( 𝒫 , 𝑫 , T ) \mathrm{SEC}_{\lambda}({\mathcal{P}},{\bm{D}},T) are equivalent up to some constants and logarithmic factors:

[444] h6: Proposition E.5 .

[445] h6: Proof.

[446] p: We prove each direction separately.

[447] p: Upper Bound. Noting that for λ ≥ 1 \lambda\geq 1 , SEC λ ​ ( 𝒫 , 𝑫 , T ) ≤ SEC 1 ​ ( 𝒫 , 𝑫 , T ) \mathrm{SEC}_{\lambda}({\mathcal{P}},{\bm{D}},T)\leq\mathrm{SEC}_{1}({\mathcal{P}},{\bm{D}},T) , this immediately follows from Xie et al. (2023, Proposition 7) with 𝒟 = 𝑫 {\mathcal{D}}={\bm{D}} .

[448] p: Lower Bound. Consider the eluder witness, i.e., a sequence of { ( 𝒛 t , P t ) } t ∈ d e \{({\bm{z}}_{t},P_{t})\}_{t\in{d_{e}}} and some fixed preference P ∗ P^{*} that attains the eluder dimension d e := Edim ⁡ ( 𝒫 , ε ) d_{e}:=\mathrm{Edim}({\mathcal{P}},\varepsilon) . Then, by definition,

[449] table: SEC λ ​ ( 𝒫 , 𝑫 , T ) \displaystyle\mathrm{SEC}_{\lambda}({\mathcal{P}},{\bm{D}},T) = sup P 1 : T 1 , P 1 : T 2 ⊆ 𝒫 sup 𝒛 1 : T ⊆ 𝒵 ∑ t = 1 T ( P t 1 ​ ( 𝒛 t ) − P t 2 ​ ( 𝒛 t ) ) 2 λ + ∑ s = 1 t − 1 ( P t 1 ​ ( 𝒛 s ) − P t 2 ​ ( 𝒛 s ) ) 2 \displaystyle=\sup_{P_{1:T}^{1},P_{1:T}^{2}\subseteq{\mathcal{P}}}\ \sup_{{\bm{z}}_{1:T}\subseteq{\mathcal{Z}}}\sum_{t=1}^{T}\frac{\left(P_{t}^{1}({\bm{z}}_{t})-P_{t}^{2}({\bm{z}}_{t})\right)^{2}}{\lambda+\sum_{s=1}^{t-1}(P_{t}^{1}({\bm{z}}_{s})-P_{t}^{2}({\bm{z}}_{s}))^{2}} ≥ sup P 1 : T 1 ⊆ 𝒫 sup 𝒛 1 : T ⊆ 𝒵 ∑ t = 1 T ( P t 1 ​ ( 𝒛 t ) − P ∗ ​ ( 𝒛 t ) ) 2 λ + ∑ s = 1 t − 1 ( P t 1 ​ ( 𝒛 s ) − P ∗ ​ ( 𝒛 s ) ) 2 \displaystyle\geq\sup_{P_{1:T}^{1}\subseteq{\mathcal{P}}}\ \sup_{{\bm{z}}_{1:T}\subseteq{\mathcal{Z}}}\sum_{t=1}^{T}\frac{\left(P_{t}^{1}({\bm{z}}_{t})-P^{*}({\bm{z}}_{t})\right)^{2}}{\lambda+\sum_{s=1}^{t-1}(P_{t}^{1}({\bm{z}}_{s})-P^{*}({\bm{z}}_{s}))^{2}} (Set P t 2 = P ∗ P_{t}^{2}=P^{*} for all t ∈ [ T ] t\in[T] ) ≥ ∑ t = 1 d e ( P t ​ ( 𝒛 t ) − P ∗ ​ ( 𝒛 t ) ) 2 λ + ∑ s = 1 t − 1 ( P t ​ ( 𝒛 s ) − P ∗ ​ ( 𝒛 s ) ) 2 \displaystyle\geq\sum_{t=1}^{d_{e}}\frac{\left(P_{t}({\bm{z}}_{t})-P^{*}({\bm{z}}_{t})\right)^{2}}{\lambda+\sum_{s=1}^{t-1}(P_{t}({\bm{z}}_{s})-P^{*}({\bm{z}}_{s}))^{2}} (Set 𝒛 1 : T {\bm{z}}_{1:T} and P 1 1 : T P^{1}_{1:T} to be the eluder witness sequence) > ∑ t = 1 d e ε 2 λ + ε 2 = d e ​ ε 2 λ + ε 2 . \displaystyle>\sum_{t=1}^{d_{e}}\frac{\varepsilon^{2}}{\lambda+\varepsilon^{2}}=\frac{d_{e}\varepsilon^{2}}{\lambda+\varepsilon^{2}}.

[450] p: ∎

[451] p: We conclude with a nearly-tight characterization of the eluder dimension of GBPM, whose proof is deferred to the next subsection:

[452] h6: Proposition E.6 .

[453] p: Note that the same Ω ~ ​ ( d 2 ) \widetilde{\Omega}(d^{2}) lower bound applies to the SEC due to Proposition E.5 . This Ω ~ ​ ( d 2 ) \widetilde{\Omega}(d^{2}) scaling implies that eluder-dimension-based frameworks cannot efficiently exploit the low-rank structure of 𝚯 \bm{\Theta} . The high eluder dimension arises because Skew ⁡ ( d , 2 ​ r ) \mathrm{Skew}(d;2r) contains rank- 2 2 “coordinate spikes” of the form ( 𝒆 i ​ 𝒆 j ⊤ − 𝒆 j ​ 𝒆 i ⊤ ) ({\bm{e}}_{i}{\bm{e}}_{j}^{\top}-{\bm{e}}_{j}{\bm{e}}_{i}^{\top}) . An adversary can query specific pairs to isolate these directions one-by-one. Since the eluder dimension measures worst-case separability rather than metric entropy (which scales as 𝒪 ⁡ ( d ​ r ) {\mathcal{O}}(dr) ), it reflects the ambient basis size even when the parameter manifold is low-dimensional.

[454] p: This limitation is best understood through the “global embedding” characterization. Specifically, a standard sufficient condition for bounding the eluder dimension by the μ \mu -rank relies on constructing global maps ϕ : 𝒳 × 𝒳 → ℬ d e ​ ( 1 ) \phi:{\mathcal{X}}\times{\mathcal{X}}\to{\mathcal{B}}^{d_{e}}(1) and w : Θ → ℬ d e ​ ( R ) w:\Theta\to{\mathcal{B}}^{d_{e}}(R) such that 𝒙 ⊤ ​ 𝚯 ​ 𝒚 = ⟨ ϕ ⁡ ( 𝒙 , 𝒚 ) , w ⁡ ( 𝚯 ) ⟩ {\bm{x}}^{\top}\bm{\Theta}{\bm{y}}=\langle\phi({\bm{x}},{\bm{y}}),w(\bm{\Theta})\rangle ( Li et al., 2022a , Proposition 4) . While skew-symmetry admits a Schur decomposition 𝚯 = 𝑸 ​ 𝚲 ​ 𝑸 ⊤ \bm{\Theta}={\bm{Q}}\bm{\Lambda}{\bm{Q}}^{\top} that allows the representation

[455] table: 𝒙 ⊤ ​ 𝚯 ​ 𝒚 = ⟨ vec ⁡ ( ( 𝑸 ⊤ ​ 𝒙 ) ​ ( 𝑸 ⊤ ​ 𝒚 ) ⊤ ) , vec ⁡ ( 𝚲 ) ⟩ , {\bm{x}}^{\top}\bm{\Theta}{\bm{y}}=\Big\langle\mathrm{vec}\big(({\bm{Q}}^{\top}{\bm{x}})({\bm{Q}}^{\top}{\bm{y}})^{\top}\big),\,\mathrm{vec}(\bm{\Lambda})\Big\rangle,

[456] p: this does not yield a valid low-dimensional witness. Crucially, the feature map depends on the basis 𝑸 {\bm{Q}} (and thus on the specific parameter 𝚯 \bm{\Theta} ), which violates the condition of having a single global feature map across the entire hypothesis class. Consequently, guarantees relying on such complexity measures (e.g., GS by Wu et al. (2025a) ) incur the full d 2 d^{2} complexity, mirroring the statistical hardness of quadratic functions with full-rank Hessians ( Osband and Van Roy, 2014 , Proposition 3) .

[457] h3: E.3 Proof of Proposition E.6

[458] p: For the proof, we recall the notion of generalized rank and a useful proposition linking the above two concepts:

[459] h6: Definition E.7 (Definition 3 of Li et al. (2022a) ) .

[460] p: For a given μ : ℝ → ℝ \mu:{\mathbb{R}}\rightarrow{\mathbb{R}} , the μ \mu -rank of 𝒫 {\mathcal{P}} at scale R > 0 R>0 , denoted as μ ​ - ​ rk ​ ( 𝒫 , R ) \mu\text{-}\mathrm{rk}({\mathcal{P}},R) , is the smallest dimension d ∈ ℕ d\in{\mathbb{N}} for which there exist R ϕ , R w > 0 R_{\phi},R_{w}>0 with R ϕ ​ R w = R R_{\phi}R_{w}=R , and (global) mappings ϕ : 𝒳 × 𝒳 → ℬ d ​ ( R ϕ ) \phi:{\mathcal{X}}\times{\mathcal{X}}\rightarrow{\mathcal{B}}^{d}(R_{\phi}) and w : 𝒫 → ℬ d ​ ( R w ) w:{\mathcal{P}}\rightarrow{\mathcal{B}}^{d}(R_{w}) such that

[461] table: P ⁡ ( 𝒙 ≻ 𝒚 ) = μ ⁡ ( ⟨ ϕ ⁡ ( 𝒙 , 𝒚 ) , w ⁡ ( P ) ⟩ ) , ∀ ( 𝒙 , 𝒚 , P ) ∈ 𝒳 × 𝒳 × 𝒫 , P({\bm{x}}\succ{\bm{y}})=\mu\left(\langle\phi({\bm{x}},{\bm{y}}),w(P)\rangle\right),\quad\forall({\bm{x}},{\bm{y}},P)\in{\mathcal{X}}\times{\mathcal{X}}\times{\mathcal{P}}, (42)

[462] p: or ∞ \infty if no such d d exists.

[463] h6: Proposition E.8 (Proposition 4(ii) of Li et al. (2022a) ) .

[464] p: For all ε < R ​ L μ \varepsilon<RL_{\mu} ,

[465] table: Edim ¯ ​ ( 𝒫 , ε ) ≤ 3 ​ e e − 1 ⋅ μ ​ - ​ rk ​ ( 𝒫 ) ⋅ L μ 2 κ 2 ⋅ log ⁡ 24 ​ R 2 ​ L μ 2 ε 2 . \underline{\mathrm{Edim}}({\mathcal{P}},\varepsilon)\leq\frac{3e}{e-1}\cdot\mu\text{-}\mathrm{rk}({\mathcal{P}})\cdot\frac{L_{\mu}^{2}}{\kappa^{2}}\cdot\log\frac{24R^{2}L_{\mu}^{2}}{\varepsilon^{2}}. (43)

[466] p: We prove the upper and lower bounds separately.

[467] p: Upper Bound. This follows trivially from adapting Proposition E.8 to our setting by considering ϕ : ( 𝒙 , 𝒚 ) ↦ vec ⁡ ( 𝒙 ​ 𝒚 ⊤ ) \phi:({\bm{x}},{\bm{y}})\mapsto\mathrm{vec}({\bm{x}}{\bm{y}}^{\top}) and w : 𝚯 ↦ vec ⁡ ( 𝚯 ) w:\bm{\Theta}\mapsto\mathrm{vec}(\bm{\Theta}) .

[468] p: Lower Bound. The construction is largely inspired by that of Li et al. (2022a, Proposition 5) , which we adapt to our setting.

[469] p: We will construct a sequence { ( 𝒙 t , 𝒚 t , 𝚯 t ) } t ∈ [ m ] \{({\bm{x}}_{t},{\bm{y}}_{t},\bm{\Theta}_{t})\}_{t\in[m]} that witnesses the claimed lower bound with 𝚯 ⋆ = 0 \bm{\Theta}_{\star}=0 . The key observation is that Skew ⁡ ( d ) \mathrm{Skew}(d) admits the following orthonormal basis: ℬ ≜ { 1 2 ​ ( 𝒆 i ​ 𝒆 j ⊤ − 𝒆 j ​ 𝒆 i ⊤ ) } 1 ≤ i < j ≤ d {\mathcal{B}}\triangleq\left\{\frac{1}{\sqrt{2}}({\bm{e}}_{i}{\bm{e}}_{j}^{\top}-{\bm{e}}_{j}{\bm{e}}_{i}^{\top})\right\}_{1\leq i<j\leq d} .

[470] p: For given ε \varepsilon , let α ∈ ( ε , 3 ​ ε ) \alpha\in(\varepsilon,\sqrt{3}\varepsilon) and k := ⌊ log 4 ⁡ S α ⌋ k:=\lfloor\log_{4}\frac{S}{\alpha}\rfloor . Then, we can first consider the following sequence of length k + 1 k+1 : for t ∈ { 0 } ∪ [ k ] t\in\{0\}\cup[k] ,

[471] table: 𝒙 t = 2 t − k ​ 𝒆 1 , 𝒚 t = 2 t − k ​ 𝒆 2 , 𝚯 t = α ⋅ 2 2 ​ ( k − t ) ​ ( 𝒆 1 ​ 𝒆 2 ⊤ − 𝒆 2 ​ 𝒆 1 ⊤ ) . {\bm{x}}_{t}=2^{t-k}{\bm{e}}_{1},\ {\bm{y}}_{t}=2^{t-k}{\bm{e}}_{2},\quad\bm{\Theta}_{t}=\alpha\cdot 2^{2(k-t)}({\bm{e}}_{1}{\bm{e}}_{2}^{\top}-{\bm{e}}_{2}{\bm{e}}_{1}^{\top}). (44)

[472] p: For each t t , we have that

[473] table: μ ⁡ ( 𝒙 t ⊤ ​ 𝚯 t ​ 𝒚 t ) − μ ⁡ ( 0 ) = 𝒙 t ⊤ ​ 𝚯 t ​ 𝒚 t = α > ε , \mu({\bm{x}}_{t}^{\top}\bm{\Theta}_{t}{\bm{y}}_{t})-\mu(0)={\bm{x}}_{t}^{\top}\bm{\Theta}_{t}{\bm{y}}_{t}=\alpha>\varepsilon,

[474] p: and

[475] table: ∑ s < t ( μ ⁡ ( 𝒙 s ⊤ ​ 𝚯 t ​ 𝒚 s ) − μ ⁡ ( 0 ) ) = ∑ s < t 𝒙 s ⊤ ​ 𝚯 t ​ 𝒚 s = α ​ ∑ s < t 2 2 ​ s − 2 ​ t < 1 3 ​ α < ε 2 . \sum_{s<t}\left(\mu({\bm{x}}_{s}^{\top}\bm{\Theta}_{t}{\bm{y}}_{s})-\mu(0)\right)=\sum_{s<t}{\bm{x}}_{s}^{\top}\bm{\Theta}_{t}{\bm{y}}_{s}=\alpha\sum_{s<t}2^{2s-2t}<\frac{1}{3}\alpha<\varepsilon^{2}.

[476] p: As 𝒙 t , 𝒙 t ∈ ℬ d ​ ( 1 ) {\bm{x}}_{t},{\bm{x}}_{t}\in{\mathcal{B}}^{d}(1) and ‖ 𝚯 t ‖ nuc ≤ α ​ 2 2 ​ k ≤ α ​ 4 log 4 ⁡ S α = S \left\lVert\bm{\Theta}_{t}\right\rVert_{\mathrm{nuc}}\leq\alpha 2^{2k}\leq\alpha 4^{\log_{4}\frac{S}{\alpha}}=S , we have Edim ¯ ​ ( 𝒫 , ε ) ≥ k + 1 ≥ log 4 ⁡ S α ≥ log 4 ⁡ S 3 ​ ε \underline{\mathrm{Edim}}({\mathcal{P}},\varepsilon)\geq k+1\geq\log_{4}\frac{S}{\alpha}\geq\log_{4}\frac{S}{\sqrt{3}\varepsilon} .

[477] p: Now we concatenate ( d 2 ) = d ⁡ ( d + 1 ) 2 \binom{d}{2}=\frac{d(d+1)}{2} times across the basis ℬ {\mathcal{B}} , i.e.,

[478] table: 𝒙 t , i , j = 2 t − k ​ 𝒆 i , 𝒚 t , i , j = 2 t − k ​ 𝒆 j , 𝚯 t , i , j = α ⋅ 2 2 ​ ( k − t ) ​ ( 𝒆 i ​ 𝒆 j ⊤ − 𝒆 j ​ 𝒆 i ⊤ ) {\bm{x}}_{t,i,j}=2^{t-k}{\bm{e}}_{i},\ {\bm{y}}_{t,i,j}=2^{t-k}{\bm{e}}_{j},\quad\bm{\Theta}_{t,i,j}=\alpha\cdot 2^{2(k-t)}({\bm{e}}_{i}{\bm{e}}_{j}^{\top}-{\bm{e}}_{j}{\bm{e}}_{i}^{\top}) (45)

[479] p: for 1 ≤ i < j ≤ d 1\leq i<j\leq d , and we are done. ∎

[480] h2: Appendix F Instantiating Regret Bound of Wu et al. (2025a) to GBPM

[481] h3: F.1 Regret Bound of Greedy Sampling

[482] p: For this section, we will consider the reverse KL-regularization as in Wu et al. (2025a) , i.e., ψ ⁡ ( π ) = D KL ​ ( π , π ref ) \psi(\pi)=D_{\mathrm{KL}}(\pi,\pi_{\mathrm{ref}}) for some fixed π ref ∈ Π \pi_{\mathrm{ref}}\in\Pi . Recall that we defined the regularized and unregularized Max-Best-Response Regrets as

[483] table: MBR ​ - ​ Reg η ​ ( T ) := ∑ t = 1 T max π ∈ Π ⁡ { 1 2 − J η ​ ( π ^ t 1 , π ) } , MBR ​ - ​ Reg ​ ( T ) := ∑ t = 1 T max π ∈ Π ⁡ { 1 2 − J ⁡ ( π ^ t 1 , π ) } . \mathrm{MBR\text{-}Reg}_{\color[rgb]{0.75,0,0.25}\eta}(T):=\sum_{t=1}^{T}\max_{\pi\in\Pi}\left\{\frac{1}{2}-J_{\color[rgb]{0.75,0,0.25}\eta}(\hat{\pi}_{t}^{1},\pi)\right\},\quad\mathrm{MBR\text{-}Reg}(T):=\sum_{t=1}^{T}\max_{\pi\in\Pi}\left\{\frac{1}{2}-J(\hat{\pi}_{t}^{1},\pi)\right\}.

[484] p: In this section, we derive the regularized and unregularized regret bound of Greedy Sampling (GS) of Wu et al. (2025a) for GBPM, based on general function approximation. We first recall the regret bound from Wu et al. (2025a) :

[485] h6: Theorem F.1 (Theorem 1 of Wu et al. (2025a) ) .

[486] p: Suppose that the preference class 𝒫 {\mathcal{P}} is finite with cardinality N 𝒫 = | 𝒫 | < ∞ . N_{\mathcal{P}}=|{\mathcal{P}}|<\infty. For any δ ∈ ( 0 , 1 ) \delta\in(0,1) , with probability at least 1 − δ 1-\delta , GS attains the following regret bound:

[487] table: MBR ​ - ​ Reg η ​ ( T ) = O ⁡ ( e η ​ d ​ ( 𝒫 , λ , T ) ​ log ⁡ ( N 𝒫 ​ T / δ ) ) . \mathrm{MBR\text{-}Reg}_{{\color[rgb]{0.75,0,0.25}\eta}}(T)=O\left({\color[rgb]{0.75,0,0.25}e^{\eta}}\,d(\mathcal{P},\lambda,T)\log(N_{\mathcal{P}}T/\delta)\right).

[488] h4: Instantiation for GBPM.

[489] p: We first instantiate the KL-regularized regret bound for GBPM:

[490] h6: Theorem F.2 (KL-regularized Regret Bound of Greedy Sampling ) .

[491] h6: Proof.

[492] p: The proof consists of two parts: 1) Extending the preference model class size term for the infinite preference space, and 2) Bounding the eluder dimension of GBPM .

[493] p: We first extend the term N 𝒫 = | 𝒫 | N_{\mathcal{P}}=|{\mathcal{P}}| for the infinite space case Θ ≜ Skew ⁡ ( d , 2 ​ r , S ) \Theta\triangleq\mathrm{Skew}(d,2r;S) by using covering number arguments. We denote P 𝚯 P_{\bm{\Theta}} as the preference probability given by GBPM for parameter 𝚯 \bm{\Theta} . For simplicity, we use the following notations introduced in the previous section. We denote 𝒵 := 𝒳 × 𝒜 × 𝒜 {\mathcal{Z}}:={\mathcal{X}}\times{\mathcal{A}}\times{\mathcal{A}} and P ⁡ ( 𝒛 ) := P ⁡ ( 𝒂 1 ≻ 𝒂 2 ∣ 𝒙 ) P({\bm{z}}):=P({\bm{a}}^{1}\succ{\bm{a}}^{2}\mid{\bm{x}}) for 𝒛 = ( 𝒙 , 𝒂 1 , 𝒂 2 ) {\bm{z}}=({\bm{x}},{\bm{a}}^{1},{\bm{a}}^{2}) . Using these, we have the following lemma, whose proof is provided in Section F.2 :

[494] h6: Lemma F.3 .

[495] p: Let { ( 𝐳 i , r i ) } i ∈ [ t ] \{({\bm{z}}_{i},r_{i})\}_{i\in[t]} be a potentially adaptively collected data with r i ∼ Ber ⁡ ( P ⁡ ( 𝐳 i ) ) r_{i}\sim\mathrm{Ber}(P({\bm{z}}_{i})) . Denote the (constrained) MLE as 𝚯 ^ t := arg ​ max 𝚯 ∈ Skew ⁡ ( d , 2 ​ r , S ) ∑ i ∈ [ t ] ℓ i ( 𝚯 ) \widehat{\bm{\Theta}}_{t}:=\argmax_{\bm{\Theta}\in\mathrm{Skew}(d,2r;S)}\sum_{i\in[t]}\ell_{i}(\bm{\Theta}) , where ℓ i ​ ( 𝚯 ) := ( r i ​ log ⁡ P 𝚯 ​ ( 𝐳 i ) + ( 1 − r i ) ​ log ⁡ ( 1 − P 𝚯 ​ ( 𝐳 i ) ) ) \ell_{i}(\bm{\Theta}):=\left(r_{i}\log P_{\bm{\Theta}}({\bm{z}}_{i})+(1-r_{i})\log(1-P_{\bm{\Theta}}({\bm{z}}_{i}))\right) . Suppose that ℓ i ​ ( ⋅ ) \ell_{i}(\cdot) is L L -Lipschitz w.r.t. the Frobenius norm. Then, for any δ ∈ ( 0 , 1 ) \delta\in(0,1) the following holds:

[496] table: ℙ ⁡ ( ∑ i = 1 t ( P 𝚯 ^ t ​ ( 𝒛 i ) − P 𝚯 ⋆ ​ ( 𝒛 i ) ) 2 ≲ log ⁡ T δ + d ​ r ​ log ⁡ L ​ S ​ T ) ≥ 1 − δ , ∀ t ∈ [ T ] . {\mathbb{P}}\left(\sum_{i=1}^{t}(P_{\widehat{\bm{\Theta}}_{t}}({\bm{z}}_{i})-P_{\bm{\Theta}_{\star}}({\bm{z}}_{i}))^{2}\lesssim\log\frac{T}{\delta}+dr\log LST\right)\geq 1-\delta,\quad\forall t\in[T].

[497] p: With this lemma and our eluder dimension bound ( Proposition E.2 ), the derivation of the regret bound in Wu et al. (2025a) follows through, with log ⁡ ( N 𝒫 ​ T δ ) \log\left(\frac{N_{\mathcal{P}}T}{\delta}\right) and λ \lambda both replaced with log ⁡ T δ + d ​ r ​ log ⁡ L ​ S ​ T \log\frac{T}{\delta}+dr\log LST . ∎

[498] h4: Converting to Unregularized Regret Bound.

[499] p: We now convert the KL-regularized regret bound to its unregularized counterpart via the following lemma:

[500] h6: Lemma F.4 .

[501] p: Suppose D ref := max π ∈ Π ⁡ D KL ​ ( π , π ref ) < ∞ D_{\mathrm{ref}}:=\max_{\pi\in\Pi}D_{\mathrm{KL}}(\pi,\pi_{\mathrm{ref}})<\infty . Then we have

[502] table: MBR ​ - ​ Reg ​ ( T ) ≤ MBR ​ - ​ Reg η ​ ( T ) + η − 1 ​ D ref ​ T . \mathrm{MBR\text{-}Reg}(T)\leq\mathrm{MBR\text{-}Reg}_{\color[rgb]{0.75,0,0.25}\eta}(T)+{\color[rgb]{0.75,0,0.25}\eta^{-1}}D_{\mathrm{ref}}T.

[503] h6: Proof.

[504] p: Recall that the KL-regularized objective is defined as

[505] table: J η ​ ( π , π ′ ) = J ⁡ ( π , π ′ ) − η − 1 ​ D KL ​ ( π , π ref ) + η − 1 ​ D KL ​ ( π ′ , π ref ) J_{{\color[rgb]{0.75,0,0.25}\eta}}(\pi,\pi^{\prime})=J(\pi,\pi^{\prime})-{\color[rgb]{0.75,0,0.25}\eta^{-1}}D_{\mathrm{KL}}(\pi,\pi_{\mathrm{ref}})+{\color[rgb]{0.75,0,0.25}\eta^{-1}}D_{\mathrm{KL}}(\pi^{\prime},\pi_{\mathrm{ref}})

[506] p: Then,

[507] table: MBR ​ - ​ Reg ​ ( T ) = ∑ t = 1 T max π ∈ Π ⁡ ( 1 2 − J ⁡ ( π ^ t 1 , π ) ) \displaystyle\mathrm{MBR\text{-}Reg}(T)=\sum_{t=1}^{T}\max_{\pi\in\Pi}\left(\frac{1}{2}-J(\hat{\pi}_{t}^{1},\pi)\right) = ∑ t = 1 T max π ∈ Π ⁡ ( 1 2 − ( J ⁡ ( π ^ t 1 , π ) − η − 1 ​ D KL ​ ( π ^ t 1 , π ref ) + η − 1 ​ D KL ​ ( π , π ref ) ) − η − 1 ​ D KL ​ ( π ^ t 1 , π ref ) + η − 1 ​ D KL ​ ( π , π ref ) ) \displaystyle=\sum_{t=1}^{T}\max_{\pi\in\Pi}\left(\frac{1}{2}-\left(J(\hat{\pi}_{t}^{1},\pi)-{\color[rgb]{0.75,0,0.25}}{\color[rgb]{0.75,0,0.25}\eta^{-1}}D_{\mathrm{KL}}(\hat{\pi}_{t}^{1},\pi_{\mathrm{ref}})+{\color[rgb]{0.75,0,0.25}\eta^{-1}}D_{\mathrm{KL}}(\pi,\pi_{\mathrm{ref}})\right)-{\color[rgb]{0.75,0,0.25}\eta^{-1}}D_{\mathrm{KL}}(\hat{\pi}_{t}^{1},\pi_{\mathrm{ref}})+{\color[rgb]{0.75,0,0.25}\eta^{-1}}D_{\mathrm{KL}}(\pi,\pi_{\mathrm{ref}})\right) ≤ ∑ t = 1 T max π ∈ Π ⁡ ( 1 2 − J η ​ ( π ^ t 1 , π ) ) + ∑ t = 1 T max π ∈ Π ⁡ ( − η − 1 ​ D KL ​ ( π ^ t 1 , π ref ) + η − 1 ​ D KL ​ ( π , π ref ) ) \displaystyle\leq\sum_{t=1}^{T}\max_{\pi\in\Pi}\left(\frac{1}{2}-J_{{\color[rgb]{0.75,0,0.25}\eta}}(\hat{\pi}_{t}^{1},\pi)\right)+\sum_{t=1}^{T}\max_{\pi\in\Pi}\left(-{\color[rgb]{0.75,0,0.25}\eta^{-1}}D_{\mathrm{KL}}(\hat{\pi}_{t}^{1},\pi_{\mathrm{ref}})+{\color[rgb]{0.75,0,0.25}\eta^{-1}}D_{\mathrm{KL}}(\pi,\pi_{\mathrm{ref}})\right) ≤ MBR ​ - ​ Reg η ​ ( T ) + ∑ t = 1 T max π ∈ Π ⁡ η − 1 ​ D KL ​ ( π , π ref ) \displaystyle\leq\mathrm{MBR\text{-}Reg}_{\color[rgb]{0.75,0,0.25}\eta}(T)+\sum_{t=1}^{T}\max_{\pi\in\Pi}{\color[rgb]{0.75,0,0.25}\eta^{-1}}D_{\mathrm{KL}}(\pi,\pi_{\mathrm{ref}}) = MBR ​ - ​ Reg η ​ ( T ) + η − 1 ​ D ref ​ T . \displaystyle=\mathrm{MBR\text{-}Reg}_{\color[rgb]{0.75,0,0.25}\eta}(T)+{\color[rgb]{0.75,0,0.25}\eta^{-1}}D_{\mathrm{ref}}T.

[508] p: ∎

[509] p: Putting everything together, we have the following corollary of Theorem F.2 for the unregularized regret bound:

[510] h6: Corollary F.5 (Unregularized Regret Bound of GS ) .

[511] h6: Proof.

[512] p: The regret bound is a direct result from the KL-regularized regret bound in Theorem F.2 , converted to unregularized regret via Lemma F.4 .

[513] p: For the second claim, suppose that this is true. Then, for the second term, we require η − 1 ​ D ref ​ T = 𝒪 ⁡ ( T 1 − γ ) {\color[rgb]{0.75,0,0.25}\eta^{-1}}D_{\mathrm{ref}}T={\mathcal{O}}(T^{1-\gamma}) to hold, which implies η = Ω ⁡ ( T γ ) {\color[rgb]{0.75,0,0.25}\eta}=\Omega(T^{\gamma}) . Plugging this into the first term leads to an additive term of 𝒪 ⁡ ( e T γ ) {\mathcal{O}}(e^{T^{\gamma}}) , which is superpolynomial: a contradiction. This concludes the proof. ∎

[514] h3: F.2 Proof of Lemma F.3 : MLE Estimator Bound

[515] p: We define the probability mass function (pmf) of r | 𝒛 ∼ Ber ⁡ ( P ⁡ ( 𝒛 ) ) r\mid{\bm{z}}\sim\mathrm{Ber}(P({\bm{z}})) as

[516] table: P ⁡ ( r ∣ 𝒛 ) = P ​ ( 𝒛 ) r ​ ( 1 − P ⁡ ( 𝒛 ) ) 1 − r , r ∈ { 0 , 1 } . P(r\mid{\bm{z}})=P({\bm{z}})^{r}(1-P({\bm{z}}))^{1-r},\quad r\in\{0,1\}.

[517] p: Then we have the following lemma, whose proof is deferred to Section F.3 :

[518] h6: Lemma F.6 .

[519] p: For each 𝚯 ∈ Θ \bm{\Theta}\in\Theta and t ∈ [ T ] t\in[T] , the following holds:

[520] table: ℙ ⁡ ( ∑ i = 1 t ( P 𝚯 ​ ( 𝒛 i ) − P 𝚯 ⋆ ​ ( 𝒛 i ) ) 2 ≤ log ⁡ 1 δ + ∑ i = 1 t log ⁡ P 𝚯 ⋆ ​ ( r i ∣ 𝒛 i ) P 𝚯 ​ ( r i ∣ 𝒛 i ) ) ≥ 1 − δ {\mathbb{P}}\left(\sum_{i=1}^{t}(P_{\bm{\Theta}}({\bm{z}}_{i})-P_{\bm{\Theta}_{\star}}({\bm{z}}_{i}))^{2}\leq\log\frac{1}{\delta}+\sum_{i=1}^{t}\log\frac{P_{\bm{\Theta}_{\star}}(r_{i}\mid{\bm{z}}_{i})}{P_{\bm{\Theta}}(r_{i}\mid{\bm{z}}_{i})}\right)\geq 1-\delta

[521] p: Let Θ ε \Theta_{\varepsilon} be an ε \varepsilon -net of Θ {\Theta} in terms of the Frobenius norm. Then by the union bound, we have:

[522] table: ℙ ( ∑ i = 1 t ( P 𝚯 ( 𝒛 i ) − P 𝚯 ⋆ ( 𝒛 i ) ) 2 ≤ log | Θ ε | δ + ∑ i = 1 t log P 𝚯 ⋆ ​ ( r i ∣ 𝒛 i ) P 𝚯 ​ ( r i ∣ 𝒛 i ) , ∀ 𝚯 ∈ Θ ε ) ≥ 1 − δ . {\mathbb{P}}\left(\sum_{i=1}^{t}(P_{\bm{\Theta}}({\bm{z}}_{i})-P_{\bm{\Theta}_{\star}}({\bm{z}}_{i}))^{2}\leq\log\frac{|\Theta_{\varepsilon}|}{\delta}+\sum_{i=1}^{t}\log\frac{P_{\bm{\Theta}_{\star}}(r_{i}\mid{\bm{z}}_{i})}{P_{\bm{\Theta}}(r_{i}\mid{\bm{z}}_{i})},\quad\forall\bm{\Theta}\in\Theta_{\varepsilon}\right)\geq 1-\delta.

[523] p: Let 𝚯 ^ ε , t \widehat{\bm{\Theta}}_{\varepsilon,t} be the epsilon net element corresponding to 𝚯 ^ t \widehat{\bm{\Theta}}_{t} , i.e., ∥ 𝚯 ^ t − 𝚯 ^ ε , t ∥ F ≤ ε \lVert\widehat{\bm{\Theta}}_{t}-\widehat{\bm{\Theta}}_{\varepsilon,t}\rVert_{F}\leq\varepsilon . Then,

[524] table: ℙ ⁡ ( ∑ i = 1 t ( P 𝚯 ^ ε , t ​ ( 𝒛 i ) − P 𝚯 ⋆ ​ ( 𝒛 i ) ) 2 ≤ log ⁡ | Θ ε | δ + ∑ i = 1 t log ⁡ P 𝚯 ⋆ ​ ( r i ∣ 𝒛 i ) P 𝚯 ^ ε , t ​ ( r i ∣ 𝒛 i ) ) ≥ 1 − δ . {\mathbb{P}}\left(\sum_{i=1}^{t}(P_{\widehat{\bm{\Theta}}_{\varepsilon,t}}({\bm{z}}_{i})-P_{\bm{\Theta}_{\star}}({\bm{z}}_{i}))^{2}\leq\log\frac{|\Theta_{\varepsilon}|}{\delta}+\sum_{i=1}^{t}\log\frac{P_{\bm{\Theta}_{\star}}(r_{i}\mid{\bm{z}}_{i})}{P_{\widehat{\bm{\Theta}}_{\varepsilon,t}}(r_{i}\mid{\bm{z}}_{i})}\right)\geq 1-\delta.

[525] p: Using the inequality ( a − b ) 2 ≥ 1 2 ​ ( a − c ) 2 − ( b − c ) 2 (a-b)^{2}\geq\frac{1}{2}(a-c)^{2}-(b-c)^{2} and the optimality of the MLE, with probability at least 1 − δ 1-\delta the following holds:

[526] table: 1 2 ​ ∑ i = 1 t ( P 𝚯 ^ t ​ ( 𝒛 i ) − P 𝚯 ​ ( 𝒛 i ) ) 2 − ∑ i = 1 t ( P 𝚯 ^ t ​ ( 𝒛 i ) − P 𝚯 ^ ε , t ​ ( 𝒛 i ) ) 2 \displaystyle\frac{1}{2}\sum_{i=1}^{t}(P_{\widehat{\bm{\Theta}}_{t}}({\bm{z}}_{i})-P_{\bm{\Theta}}({\bm{z}}_{i}))^{2}-\sum_{i=1}^{t}(P_{\widehat{\bm{\Theta}}_{t}}({\bm{z}}_{i})-P_{\widehat{\bm{\Theta}}_{\varepsilon,t}}({\bm{z}}_{i}))^{2} = log ⁡ | Θ ε | δ + ∑ i = 1 t log ⁡ P 𝚯 ⋆ ​ ( r i ∣ 𝒛 i ) P 𝚯 ^ t ​ ( r i ∣ 𝒛 i ) + ∑ i = 1 t log ⁡ P 𝚯 ^ t ​ ( r i ∣ 𝒛 i ) P 𝚯 ^ ε , t ​ ( r i ∣ 𝒛 i ) \displaystyle=\log\frac{|\Theta_{\varepsilon}|}{\delta}+\sum_{i=1}^{t}\log\frac{P_{\bm{\Theta}_{\star}}(r_{i}\mid{\bm{z}}_{i})}{P_{\widehat{\bm{\Theta}}_{t}}(r_{i}\mid{\bm{z}}_{i})}+\sum_{i=1}^{t}\log\frac{P_{\widehat{\bm{\Theta}}_{t}}(r_{i}\mid{\bm{z}}_{i})}{P_{\widehat{\bm{\Theta}}_{\varepsilon,t}}(r_{i}\mid{\bm{z}}_{i})} ≤ log ⁡ | Θ ε | δ + ∑ i = 1 t log ⁡ P 𝚯 ^ t ​ ( r i ∣ 𝒛 i ) P 𝚯 ^ ε , t ​ ( r i ∣ 𝒛 i ) . \displaystyle\leq\log\frac{|\Theta_{\varepsilon}|}{\delta}+\sum_{i=1}^{t}\log\frac{P_{\widehat{\bm{\Theta}}_{t}}(r_{i}\mid{\bm{z}}_{i})}{P_{\widehat{\bm{\Theta}}_{\varepsilon,t}}(r_{i}\mid{\bm{z}}_{i})}.

[527] p: Now, note that for any 𝚯 \bm{\Theta} ,

[528] table: log ⁡ P 𝚯 ​ ( r i ∣ 𝒛 i ) = r i ​ log ⁡ P 𝚯 ​ ( 𝒛 i ) + ( 1 − r i ) ​ log ⁡ ( 1 − P 𝚯 ​ ( 𝒛 i ) ) , \log P_{\bm{\Theta}}(r_{i}\mid{\bm{z}}_{i})=r_{i}\log P_{\bm{\Theta}}({\bm{z}}_{i})+(1-r_{i})\log(1-P_{\bm{\Theta}}({\bm{z}}_{i})),

[529] p: which is L L -Lipschitz in 𝚯 \bm{\Theta} by given. With this, we can bound the log sum on the right as

[530] table: ∑ i = 1 t log ⁡ P 𝚯 ^ t ​ ( r i ∣ 𝒛 i ) P 𝚯 ^ ε , t ​ ( r i ∣ 𝒛 i ) ≤ L ​ t ​ ‖ 𝚯 ^ ε , t − 𝚯 ^ t ‖ F ≤ L ​ t ​ ε . \sum_{i=1}^{t}\log\frac{P_{\widehat{\bm{\Theta}}_{t}}(r_{i}\mid{\bm{z}}_{i})}{P_{\widehat{\bm{\Theta}}_{\varepsilon,t}}(r_{i}\mid{\bm{z}}_{i})}\leq Lt\left\lVert\widehat{\bm{\Theta}}_{\varepsilon,t}-\widehat{\bm{\Theta}}_{t}\right\rVert_{F}\leq Lt\varepsilon.

[531] p: Since we assumed that log ⁡ P 𝚯 \log P_{\bm{\Theta}} is L L -Lipschitz, it follows that P 𝚯 P_{\bm{\Theta}} is also L L -Lipschitz. 12 12 12 As the Lipschitz constant is the maximum gradient norm by the Rademacher’s theorem, ‖ ∇ 𝚯 P 𝚯 ‖ = P 𝚯 ⋅ ‖ ∇ 𝚯 ​ log ​ P 𝚯 ‖ ≤ L \left\lVert\nabla_{\bm{\Theta}}P_{\bm{\Theta}}\right\rVert=P_{\bm{\Theta}}\cdot\left\lVert\nabla_{\bm{\Theta}}\log P_{\bm{\Theta}}\right\rVert\leq L . Therefore,

[532] table: ∑ i = 1 t ( P 𝚯 ^ t ​ ( 𝒛 i ) − P 𝚯 ^ ε , t ​ ( 𝒛 i ) ) 2 ≤ L ​ t ​ ε 2 . \sum_{i=1}^{t}(P_{\widehat{\bm{\Theta}}_{t}}({\bm{z}}_{i})-P_{\widehat{\bm{\Theta}}_{\varepsilon,t}}({\bm{z}}_{i}))^{2}\leq Lt\varepsilon^{2}.

[533] p: We now bound the cardinality of the ε \varepsilon -net | Θ ε | |\Theta_{\varepsilon}| by bounding the covering number of a slightly larger set:

[534] h6: Lemma F.7 (Lemma 3.1 of Candès and Plan (2011) ) .

[535] p: Let Θ ( d , 2 r ; S ) ≔ { 𝐗 ∈ ℝ d × d ∣ ∥ 𝐗 ∥ F ≤ S , rank ( 𝐗 ) ≤ 2 r } ⊇ Skew ( d , 2 r ; S ) \Theta(d,2r;S)\coloneqq\{{\bm{X}}\in{\mathbb{R}}^{d\times d}\mid\|\mathbf{X}\|_{F}\leq S,\operatorname{rank}({\bm{X}})\leq 2r\}\supseteq\mathrm{Skew}(d,2r;S) . For any ε > 0 \varepsilon>0 , there exists an ε \varepsilon -net Θ ε \Theta_{\varepsilon} of Θ ⁡ ( d , 2 ​ r , S ) \Theta(d,2r;S) w.r.t. ‖ ⋅ ‖ F \left\lVert\cdot\right\rVert_{F} with | Θ ε | ≤ ( 9 ​ S ε ) 2 ​ ( 2 ​ d + 1 ) ​ r . |\Theta_{\varepsilon}|\leq\left(\frac{9S}{\varepsilon}\right)^{2(2d+1)r}.

[536] p: Putting the bounds together, we have:

[537] table: ℙ ⁡ ( ∑ i = 1 t ( P 𝚯 ^ t ​ ( 𝒛 i ) − P 𝚯 ⋆ ​ ( 𝒛 i ) ) 2 ≲ log ⁡ 1 δ + L ​ t ​ ε + L ​ t ​ ε 2 + d ​ r ​ log ⁡ S ε ) ≥ 1 − δ . {\mathbb{P}}\left(\sum_{i=1}^{t}(P_{\widehat{\bm{\Theta}}_{t}}({\bm{z}}_{i})-P_{\bm{\Theta}_{\star}}({\bm{z}}_{i}))^{2}\lesssim\log\frac{1}{\delta}+Lt\varepsilon+Lt\varepsilon^{2}+dr\log\frac{S}{\varepsilon}\right)\geq 1-\delta.

[538] p: Choosing ε ≈ 1 ( L ​ t ) 2 \varepsilon\approx\frac{1}{(Lt)^{2}} ,

[539] table: ℙ ⁡ ( ∑ i = 1 t ( P 𝚯 ^ t ​ ( 𝒛 i ) − P 𝚯 ⋆ ​ ( 𝒛 i ) ) 2 ≲ log ⁡ 1 δ + d ​ r ​ log ⁡ ( L ​ S ​ t ) ) ≥ 1 − δ . {\mathbb{P}}\left(\sum_{i=1}^{t}(P_{\widehat{\bm{\Theta}}_{t}}({\bm{z}}_{i})-P_{\bm{\Theta}_{\star}}({\bm{z}}_{i}))^{2}\lesssim\log\frac{1}{\delta}+dr\log(LSt)\right)\geq 1-\delta.

[540] p: Setting δ = δ / T \delta=\delta/T and taking the union bound over t t , we have:

[541] table: ℙ ( ∀ t ∈ [ T ] , ∑ i = 1 t ( P 𝚯 ^ t ( 𝒛 i ) − P 𝚯 ⋆ ( 𝒛 i ) ) 2 ≲ log T δ + d r log ( L S T ) ) ≥ 1 − δ . {\mathbb{P}}\left(\forall t\in[T],\,\sum_{i=1}^{t}(P_{\widehat{\bm{\Theta}}_{t}}({\bm{z}}_{i})-P_{\bm{\Theta}_{\star}}({\bm{z}}_{i}))^{2}\lesssim\log\frac{T}{\delta}+dr\log(LST)\right)\geq 1-\delta.

[542] p: which concludes the proof. ∎

[543] h3: F.3 Proof of Lemma F.6

[544] p: The proof closely follows that of Ye et al. (2024, Lemma 1) and Wu et al. (2025a, Lemma 3) .

[545] p: For the function P 𝚯 P_{\bm{\Theta}} defined by the fixed 𝚯 ∈ Θ \bm{\Theta}\in\Theta , we first upper bound its logarithmic moment generating function as

[546] table: log ⁡ 𝔼 ​ exp ⁡ ( ∑ i = 1 t log ⁡ P 𝚯 ​ ( r i ∣ 𝒛 i ) P 𝚯 ⋆ ​ ( r i ∣ 𝒛 i ) ) \displaystyle\log\mathbb{E}\exp\!\left(\sum_{i=1}^{t}\log\frac{P_{\bm{\Theta}}(r_{i}\mid{\bm{z}}_{i})}{P_{\bm{\Theta}_{\star}}(r_{i}\mid{\bm{z}}_{i})}\right) = log ⁡ 𝔼 ​ exp ⁡ ( ∑ i = 1 t − 1 log ⁡ P 𝚯 ​ ( r i ∣ 𝒛 i ) P 𝚯 ⋆ ​ ( r i ∣ 𝒛 i ) + log ⁡ ( 2 ​ 𝔼 r t | 𝒛 t ​ P 𝚯 ​ ( r t ∣ 𝒛 t ) P 𝚯 ⋆ ​ ( r t ∣ 𝒛 t ) ) ) \displaystyle=\log\mathbb{E}\exp\!\Biggl(\sum_{i=1}^{t-1}\log\frac{P_{\bm{\Theta}}(r_{i}\mid{\bm{z}}_{i})}{P_{\bm{\Theta}_{\star}}(r_{i}\mid{\bm{z}}_{i})}+\log\Bigl(2\,\mathbb{E}_{r_{t}\mid{\bm{z}}_{t}}\sqrt{\frac{P_{\bm{\Theta}}(r_{t}\mid{\bm{z}}_{t})}{P_{\bm{\Theta}_{\star}}(r_{t}\mid{\bm{z}}_{t})}}\Bigr)\Biggr) = log 𝔼 exp ( ∑ i = 1 t − 1 log P 𝚯 ​ ( r i ∣ 𝒛 i ) P 𝚯 ​ ( r i ∣ 𝒛 i ) + log ( 1 − H ( P 𝚯 ( r t ∣ 𝒛 t ) ∥ P 𝚯 ⋆ ( r t ∣ 𝒛 t ) ) 2 ) ) \displaystyle=\log\mathbb{E}\exp\!\Biggl(\sum_{i=1}^{t-1}\log\frac{P_{\bm{\Theta}}(r_{i}\mid{\bm{z}}_{i})}{P_{\bm{\Theta}}(r_{i}\mid{\bm{z}}_{i})}+\log\Bigl(1-H\,\bigl(P_{\bm{\Theta}}(r_{t}\mid{\bm{z}}_{t})\,\|\,P_{\bm{\Theta}_{\star}}(r_{t}\mid{\bm{z}}_{t})\bigr)^{2}\Bigr)\Biggr) ≤ log 𝔼 exp ( ∑ i = 1 t − 1 log P 𝚯 ​ ( r i ∣ 𝒛 i ) P 𝚯 ⋆ ​ ( r i ∣ 𝒛 i ) − H ( P 𝚯 ( r t ∣ 𝒛 t ) ∥ P 𝚯 ⋆ ( r t ∣ 𝒛 t ) ) 2 ) \displaystyle\leq\log\mathbb{E}\exp\!\Biggl(\sum_{i=1}^{t-1}\log\frac{P_{\bm{\Theta}}(r_{i}\mid{\bm{z}}_{i})}{P_{\bm{\Theta}_{\star}}(r_{i}\mid{\bm{z}}_{i})}-H\,\bigl(P_{\bm{\Theta}}(r_{t}\mid{\bm{z}}_{t})\,\|\,P_{\bm{\Theta}_{\star}}(r_{t}\mid{\bm{z}}_{t})\bigr)^{2}\Biggr) ≤ ⋯ ≤ − ∑ i = 1 t H ( P 𝚯 ( r i ∣ 𝒛 i ) ∥ P 𝚯 ⋆ ( r i ∣ 𝒛 i ) ) 2 , \displaystyle\leq\cdots\leq-\sum_{i=1}^{t}H\,\bigl(P_{\bm{\Theta}}(r_{i}\mid{\bm{z}}_{i})\,\|\,P_{\bm{\Theta}_{\star}}(r_{i}\mid{\bm{z}}_{i})\bigr)^{2},

[547] p: where H ( P ∥ Q ) 2 H(P\|Q)^{2} is the squared Hellinger distance between probability measures P P and Q Q on Ω \Omega , defined as

[548] table: H ( P ∥ Q ) 2 := ∫ Ω ( p ⁡ ( z ) − q ⁡ ( z ) ) 2 d μ ( z ) , H(P\|Q)^{2}:=\int_{\Omega}\left(\sqrt{p(z)}-\sqrt{q(z)}\right)^{2}\,d\mu(z),

[549] p: with p p and q q denoting their respective densities with respect to a base measure μ \mu .

[550] p: We continue to lower-bound the Hellinger distance by

[551] table: ∑ i = 1 t ( H ( P 𝚯 ( r i ∣ 𝒛 i ) ∥ P 𝚯 ⋆ ( r i ∣ 𝒛 i ) ) ) 2 \displaystyle\sum_{i=1}^{t}\Bigl(H\,\bigl(P_{\bm{\Theta}}(r_{i}\mid{\bm{z}}_{i})\,\|\,P_{\bm{\Theta}_{\star}}(r_{i}\mid{\bm{z}}_{i})\bigr)\Bigr)^{2} ≥ ∑ i = 1 t ( TV ( P 𝚯 ( r i ∣ 𝒛 i ) ∥ P 𝚯 ⋆ ( r i ∣ 𝒛 i ) ) ) 2 \displaystyle\geq\sum_{i=1}^{t}\Bigl(\mathrm{TV}\,\bigl(P_{\bm{\Theta}}(r_{i}\mid{\bm{z}}_{i})\,\|\,P_{\bm{\Theta}_{\star}}(r_{i}\mid{\bm{z}}_{i})\bigr)\Bigr)^{2} = ∑ i = 1 t ( P 𝚯 ​ ( 𝒛 i ) − P 𝚯 ⋆ ​ ( 𝒛 i ) ) 2 , \displaystyle=\sum_{i=1}^{t}\Bigl(P_{\bm{\Theta}}({\bm{z}}_{i})-P_{\bm{\Theta}_{\star}}({\bm{z}}_{i})\Bigr)^{2},

[552] p: where the inequality uses the fact that for any distribution p , q p,q , H ⁡ ( p , q ) ≥ TV ⁡ ( p , q ) H(p,q)\geq\mathrm{TV}(p,q) ( Zhang, 2023 , Theorem B.9) .

[553] p: Then, by Lemma G.1 , we obtain for each 𝚯 ∈ Θ {\bm{\Theta}}\in\Theta , with probability at least 1 − δ 1-\delta ,

[554] table: ∑ i = 1 t log ⁡ P 𝚯 ​ ( r i ∣ 𝒛 i ) P 𝚯 ⋆ ​ ( r i ∣ 𝒛 i ) \displaystyle\sum_{i=1}^{t}\log\frac{P_{\bm{\Theta}}(r_{i}\mid{\bm{z}}_{i})}{P_{\bm{\Theta}_{\star}}(r_{i}\mid{\bm{z}}_{i})} ≤ log ⁡ ( 1 δ ) + log ⁡ 𝔼 ​ exp ⁡ ( ∑ i = 1 t log ⁡ P 𝚯 ​ ( r i ∣ 𝒛 i ) P 𝚯 ⋆ ​ ( r i ∣ 𝒛 i ) ) \displaystyle\leq\log\!\left(\frac{1}{\delta}\right)+\log\mathbb{E}\exp\!\left(\sum_{i=1}^{t}\log\frac{P_{\bm{\Theta}}(r_{i}\mid{\bm{z}}_{i})}{P_{\bm{\Theta}_{\star}}(r_{i}\mid{\bm{z}}_{i})}\right) ≤ − ∑ i = 1 t H ( P 𝚯 ( r i ∣ 𝒛 i ) ∥ P 𝚯 ⋆ ( r i ∣ 𝒛 i ) ) 2 + log ( 1 δ ) \displaystyle\leq-\sum_{i=1}^{t}H\!\bigl(P_{\bm{\Theta}}(r_{i}\mid{\bm{z}}_{i})\,\|\,P_{\bm{\Theta}_{\star}}(r_{i}\mid{\bm{z}}_{i})\bigr)^{2}+\log\!\left(\frac{1}{\delta}\right) ≤ − ∑ i = 1 t ( P 𝚯 ( 𝒛 i ) − P 𝚯 ⋆ ( 𝒛 i ) ) 2 + log ( 1 δ ) . \displaystyle\leq-\sum_{i=1}^{t}\Bigl(P_{\bm{\Theta}}({\bm{z}}_{i})-P_{\bm{\Theta}_{\star}}({\bm{z}}_{i})\Bigr)^{2}+\log\!\left(\frac{1}{\delta}\right).

[555] h2: Appendix G Auxiliary Lemmas

[556] h6: Lemma G.1 (Martingale Exponential Inequalities; Theorem 13.2 of Zhang (2023) ) .

[557] p: Consider a sequence of random functions ξ 1 ​ ( 𝒵 1 ) , … , ξ t ​ ( 𝒵 t ) , … \xi_{1}(\mathcal{Z}_{1}),\ldots,\xi_{t}(\mathcal{Z}_{t}),\ldots with respect to filtration { ℱ t } \{\mathcal{F}_{t}\} . We have for any δ ∈ ( 0 , 1 ) \delta\in(0,1) and λ > 0 \lambda>0 :

[558] table: ℙ ( ∃ n > 0 : − ∑ i = 1 n ξ i ≥ log ⁡ ( 1 / δ ) λ + 1 λ ∑ i = 1 n log 𝔼 Z i ( y ) exp ( − λ ξ i ) ) ≤ δ , \mathbb{P}\left(\exists n>0:-\sum_{i=1}^{n}\xi_{i}\geq\frac{\log(1/\delta)}{\lambda}+\frac{1}{\lambda}\sum_{i=1}^{n}\log\mathbb{E}_{Z_{i}^{(y)}}\exp(-\lambda\xi_{i})\right)\leq\delta,

[559] p: where Z t = ( Z t ( x ) , Z t ( y ) ) Z_{t}=(Z_{t}^{(x)},Z_{t}^{(y)}) and 𝒵 t = ( Z 1 , … , Z t ) \mathcal{Z}_{t}=(Z_{1},\ldots,Z_{t}) .

[560] h6: Lemma G.2 (Multiplicative Chernoff Bounds; Corollary 2.18 of Zhang (2023) ) .

[561] p: Assume that X ∈ [ 0 , 1 ] X\in[0,1] with 𝔼 ​ X = μ \mathbb{E}X=\mu . Then for all ϵ > 0 \epsilon>0 ,

[562] table: ℙ ⁡ ( X ¯ n ≥ ( 1 + ϵ ) ​ μ ) \displaystyle\mathbb{P}\left(\bar{X}_{n}\geq(1+\epsilon)\mu\right) ≤ exp ⁡ [ − 2 ​ n ​ μ ​ ϵ 2 2 + ϵ ] \displaystyle\leq\exp\left[\frac{-2n\mu\epsilon^{2}}{2+\epsilon}\right] ℙ ⁡ ( X ¯ n ≤ ( 1 − ϵ ) ​ μ ) \displaystyle\mathbb{P}\left(\bar{X}_{n}\leq(1-\epsilon)\mu\right) ≤ exp ⁡ [ − 2 ​ n ​ μ ​ ϵ 2 2 ] . \displaystyle\leq\exp\left[\frac{-2n\mu\epsilon^{2}}{2}\right].

[563] p: Moreover, for t > 0 t>0 , we have

[564] table: ℙ ⁡ ( X ¯ n ≥ μ + 2 ​ μ ​ t n + t 3 ​ n ) ≤ exp ⁡ ( − t ) . \mathbb{P}\left(\bar{X}_{n}\geq\mu+\sqrt{\frac{2\mu t}{n}}+\frac{t}{3n}\right)\leq\exp(-t).

[565] h6: Lemma G.3 (Elliptical Potential Lemma; Lemma 11 of Abbasi-Yadkori et al. (2011) ) .

[566] p: Let 𝐱 1 , ⋯ , 𝐱 T ∈ ℬ d ​ ( X ) {\bm{x}}_{1},\cdots,{\bm{x}}_{T}\in{\mathcal{B}}^{d}(X) be a sequence of vectors and 𝐕 t := λ ​ 𝐈 + ∑ s = 1 t − 1 𝐱 s ​ 𝐱 s ⊺ {\bm{V}}_{t}:=\lambda{\bm{I}}+\sum_{s=1}^{t-1}{\bm{x}}_{s}{\bm{x}}_{s}^{\intercal} . Then, we have

[567] table: ∑ t = 1 T min ⁡ { 1 , ∥ 𝒙 t ∥ 𝑽 t − 1 2 } ≤ 2 ​ d ​ log ⁡ ( 1 + X 2 ​ T d ​ λ ) . \sum_{t=1}^{T}\min\left\{1,\lVert{\bm{x}}_{t}\rVert^{2}_{{\bm{V}}_{t}^{-1}}\right\}\leq 2d\log\left(1+\frac{X^{2}T}{d\lambda}\right).

[568] h2: Appendix H Future Directions

[569] h4: Relaxing the Feature Diversity Assumption.

[570] p: Our current regret bounds rely on the feature diversity assumption ( Assumption 1 ), characterized by the minimum eigenvalue C min C_{\min} . While this assumption is standard in the contextual bandits literature that involves either greedy sampling (e.g., algorithms without sophisticated exploration strategies) or high dimensions, it may still be restrictive for general RLHF applications. Recent works have investigated minimal assumptions required for greedy strategies, such as the local anti-concentration (LAC) property proposed by Kim and Oh (2024) . Investigating the impact of such relaxed conditions on online RLHF with GBPM (e.g., whether we can still obtain e 𝒪 ⁡ ( η ) {\color[rgb]{0.75,0,0.25}e^{{\mathcal{O}}(\eta)}} -free polylogarithmic regret with GS ) remains an important open question.

[571] h4: Instance-Specific Guarantees for Unregularized Regret.

[572] p: While our work establishes 𝒪 ~ ​ ( T ) \tilde{{\mathcal{O}}}(\sqrt{T}) guarantees for unregularized regret (via Theorem 4.2 ), these bounds reflect worst-case hardness. For instance, Ito et al. (2025) demonstrated that in tabular games with bandit feedback, the Nash regret for the Tsallis-INF algorithm ( Tsallis, 1988 ; Abernethy et al., 2015 ; Zimmert and Seldin, 2021 ) scales with the “sparsity” or “entropy” of the NE set, potentially achieving logarithmic regret 𝒪 ⁡ ( log ⁡ T ) {\mathcal{O}}(\log T) when the NE is unique and deterministic (a pure strategy), and even rates of the form 𝒪 ⁡ ( T c ) {\mathcal{O}}(T^{c}) for some c ∈ ( 0 , 1 ) c\in(0,1) , depending on the geometry of the set of Nash Equilibria. Adapting such instance-dependent guarantees to the contextual GBPM setting is non-trivial, even when the link function μ \mu is linear. Recent advances in “Best-of-Both-Worlds” algorithms for linear contextual bandits ( Kuroki et al., 2024 ; Kato and Ito, 2025 ) may provide a promising starting point.

[573] h4: Computationally Efficient Algorithms.

[574] p: Our current theoretical framework assumes access to a computational oracle for finding the NE ( Oracle 3 ), which may be computationally expensive in practice. Developing efficient variants of our algorithms is a practical priority. Promising approaches include leveraging online estimation techniques such as Online Mirror Descent (OMD) ( Zhang et al., 2025b ) , minimax optimization techniques such as optimistic OMD ( Rakhlin and Sridharan, 2013a ; Syrgkanis et al., 2015 ; Zhang et al., 2025c ) , or reductions to offline/online regression oracles ( Foster and Rakhlin, 2020 ) .

[575] h2: Instructions for reporting errors

[576] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[577] p: Tip: You can select the relevant text first, to include it in your report.

[578] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[579] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
