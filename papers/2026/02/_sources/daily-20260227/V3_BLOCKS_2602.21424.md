[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] p: On the Structural Non-Preservation of Epistemic Behaviour under Policy Transformation

[3] p: Alexander Galozy

[4] p: Keywords: Reinforcement Learning, Partial Observability, Behavioural Equivalence, Representation, Behavioural Evaluation

[5] h6: Abstract

[6] p: Reinforcement learning (RL) agents under partial observability often condition actions on internally accumulated information such as memory or inferred latent context. We formalise such information-conditioned interaction patterns as behavioural dependency : variation in action selection with respect to internal information under fixed observations. This induces a probe-relative notion of ϵ \epsilon -behavioural equivalence and a within-policy behavioural distance that quantifies probe sensitivity. We establish three structural results. First, the set of policies exhibiting non-trivial behavioural dependency is not closed under convex aggregation. Second, behavioural distance contracts under convex combination. Third, we prove a sufficient local condition under which gradient ascent on a skewed mixture objective decreases behavioural distance when a dominant-mode gradient aligns with the direction of steepest contraction. Minimal bandit and partially observable gridworld experiments provide controlled witnesses of these mechanisms. In the examined settings, behavioural distance decreases under convex aggregation and under continued optimisation with skewed latent priors, and in these experiments it precedes degradation under latent prior shift. These results identify structural conditions under which probe-conditioned behavioural separation is not preserved under common policy transformations.

[7] h2: 1 Introduction

[8] p: Reinforcement learning (RL) is typically evaluated through observable trajectories and task performance. Many behaviours that enable effective learning, however, depend on internally accumulated information beyond immediate observations. Under partial observability, policies often condition actions on memory or inferred latent context, even when external observations are fixed. Although such information-conditioned behaviour is central to meta-RL ( Duan et al., 2016 ; Rakelly et al., 2019 ) , Bayesian approaches ( Zintgraf et al., 2021 ) , world models ( Ha and Schmidhuber, 2018 ; Hafner et al., 2020 ; Schrittwieser et al., 2020 ) , and structured exploration ( Pathak et al., 2017 ; Bellemare et al., 2016 ; Houthooft et al., 2016 ) , it is seldom treated as an explicit object of analysis and is often assessed indirectly through reward.

[9] p: Common RL transformations operate on parameters or action distributions and therefore offer no inherent guarantee that behavioural dependencies will be preserved. Procedures such as policy aggregation, distillation, or reward-driven optimisation can homogenise response profiles or induce representational collapse ( Burda et al., 2019 ; Raileanu et al., 2022 ) , maintaining short-horizon reward performance while altering or eliminating interaction patterns that rely on internal information. An extended discussion on the phenomenon of epistemic behaviour in the RL literature is provided in the supplementary material (Appendix A ).

[10] p: We formalise epistemic behaviour as behavioural dependency: systematic variation in action selection with respect to internal information under fixed observations. Quantifying this variation yields a within-policy behavioural distance that bounds robustness under latent prior shift and induces a probe-relative notion of ϵ \epsilon -behavioural equivalence over policies.

[11] p: We show both theoretically and empirically that epistemic structure is not preserved under common transformations. First, we prove that policies exhibiting behavioural dependency are not closed under convex aggregation. Second, we prove that gradient-based optimisation under sufficiently skewed priors contracts behavioural distance under a stated alignment condition, even while short-horizon reward remains optimal.

[12] p: Behavioural Representation and Preservation (BRP) articulates the representational perspective implied by these results. BRP treats ϵ \epsilon -behavioural equivalence classes as the relevant units of preservation under policy transformation. The following sections develop the formal machinery, provide minimal reinforcement learning witnesses of behavioural attenuation, and analyse the structural challenges of preserving epistemic behaviour.

[13] h2: 2 Beyond Kinematic Behaviour

[14] p: Standard reinforcement learning evaluates agents at the level of observable trajectories and reward. However, identical trajectories can arise from distinct internal information-processing strategies. To analyse preservation of information-conditioned behaviour, we distinguish observable interaction from the internal states that modulate action selection.

[15] p: Kinematic behaviour refers to observable action and state sequences that determine reward and trajectory statistics. Latent behaviour refers to internal representations such as recurrent memory states or inferred task variables that mediate the mapping from observations to actions.

[16] p: We define epistemic behaviour as systematic variation in action selection with respect to internally accumulated information under fixed observations. This notion abstracts away from architectural details and focuses directly on information-conditioned interaction patterns.

[17] p: Behavioural preservation concerns whether such probe-conditioned dependencies remain stable under transformations such as optimisation, compression, or aggregation. Because these dependencies are typically encoded implicitly within parameters, standard reinforcement learning pipelines do not in general provide structural guarantees of their retention. Preservation therefore requires analysing policies at the level of behavioural equivalence classes instead of individual parameters or latent states. We now formalise behavioural dependency and define the probe-relative equivalence classes that serve as the units of preservation.

[18] h3: 2.1 Behavioural Dependency and Equivalence

[19] p: To analyse preservation of epistemic behaviour, we formalise behavioural dependency and the equivalence classes it induces. Since internal representations are architecture dependent and not directly identifiable, equivalence must be defined at the level of observable interaction instead of parameters. Policy-level behavioural distances based on action distributions at fixed observations have been proposed in multi-agent settings ( Bettini et al., 2025 ; Hu et al., 2024 ) , but those approaches measure differences across agents, whereas our focus is probe-induced variation within a single policy.

[20] h4: Notation.

[21] p: Let π \pi denote a stochastic policy over observation space 𝒪 \mathcal{O} and action space 𝒜 \mathcal{A} . The internal state h t ∈ ℋ π h_{t}\in\mathcal{H}_{\pi} represents any mechanism by which a policy accumulates information over time. No assumption is made about the interpretability or identifiability of h t h_{t} . All equivalence notions are defined relative to a probe set 𝒫 \mathcal{P} . A policy interacting with an environment samples actions as

[22] table: a t ∼ π ⁡ ( a t ∣ o t , h t ) . a_{t}\sim\pi(a_{t}\mid o_{t},h_{t}).

[23] h4: Behavioural Dependency and Response Profiles.

[24] p: A policy exhibits epistemic behaviour if its action distribution varies as a function of internal information under fixed observations. Formally, behavioural dependency holds if there exist o ∈ 𝒪 o\in\mathcal{O} and h , h ′ ∈ ℋ π h,h^{\prime}\in\mathcal{H}_{\pi} such that π ( ⋅ ∣ o , h ) ≠ π ( ⋅ ∣ o , h ′ ) \pi(\cdot\mid o,h)\neq\pi(\cdot\mid o,h^{\prime}) .

[25] p: Let 𝒫 \mathcal{P} denote a set of interaction probes. For a policy π \pi , define its response profile as

[26] table: R π ( p , o ) = 𝔼 h ∼ p ⁡ ( π ) [ π ( ⋅ ∣ o , h ) ] , R_{\pi}(p,o)=\mathbb{E}_{h\sim p(\pi)}\!\left[\pi(\cdot\mid o,h)\right], (1)

[27] p: which captures the observable action distribution under probe p ∈ 𝒫 p\in\mathcal{P} at observation o o . For fixed ( p , o ) (p,o) , R π ​ ( p , o ) R_{\pi}(p,o) lies in the probability simplex Δ ⁡ ( 𝒜 ) \Delta(\mathcal{A}) .

[28] h4: Behavioural Equivalence.

[29] p: To allow graded comparison of probe-conditioned response profiles, we define a probe-relative divergence at a fixed evaluation observation o ∗ o^{\ast} :

[30] table: d 𝒫 , o ∗ ​ ( π 1 , π 2 ) = sup p ∈ 𝒫 ‖ R π 1 ​ ( p , o ∗ ) − R π 2 ​ ( p , o ∗ ) ‖ 1 . d_{\mathcal{P},o^{\ast}}(\pi_{1},\pi_{2})=\sup_{p\in\mathcal{P}}\left\|R_{\pi_{1}}(p,o^{\ast})-R_{\pi_{2}}(p,o^{\ast})\right\|_{1}. (2)

[31] h6: Definition 1 ( ϵ \epsilon -Behavioural Equivalence) .

[32] p: Two policies π 1 \pi_{1} and π 2 \pi_{2} are said to be ϵ \epsilon -behaviourally equivalent with respect to 𝒫 \mathcal{P} at o ∗ o^{\ast} if

[33] table: d 𝒫 , o ∗ ​ ( π 1 , π 2 ) ≤ ϵ . d_{\mathcal{P},o^{\ast}}(\pi_{1},\pi_{2})\leq\epsilon. (3)

[34] p: The corresponding equivalence class is

[35] table: [ π ] 𝒫 , ϵ = { π ′ ∣ d 𝒫 , o ∗ ​ ( π , π ′ ) ≤ ϵ } . [\pi]_{\mathcal{P},\epsilon}=\left\{\pi^{\prime}\mid d_{\mathcal{P},o^{\ast}}(\pi,\pi^{\prime})\leq\epsilon\right\}. (4)

[36] p: The equivalence class [ π ] 𝒫 , ϵ [\pi]_{\mathcal{P},\epsilon} groups policies with sufficiently similar probe-conditioned response profiles. We note that the term behavioural equivalence has appeared previously in Interactive POMDPs to aggregate models of other agents that induce identical optimal actions ( Rathnasabapathy et al., 2006 ) . Our definition instead compares policies directly through probe-conditioned response profiles, independent of optimality criteria or reward structure.

[37] h4: Within-Policy Behavioural Distance.

[38] p: Fix an evaluation observation o ∗ o^{\ast} and two probes p 0 , p 1 ∈ 𝒫 p_{0},p_{1}\in\mathcal{P} chosen to induce distinct latent interaction contexts. The within-policy behavioural distance is defined as

[39] table: d ⁡ ( π ) = ‖ R π ​ ( p 0 , o ∗ ) − R π ​ ( p 1 , o ∗ ) ‖ 1 . d(\pi)=\left\|R_{\pi}(p_{0},o^{\ast})-R_{\pi}(p_{1},o^{\ast})\right\|_{1}. (5)

[40] p: A policy exhibits non-trivial behavioural dependency (with respect to the selected probes) if d ⁡ ( π ) > 0 d(\pi)>0 . This scalar quantity isolates probe-induced variation in action distributions at a fixed evaluation context and serves as a minimal observable surrogate for information-conditioned behavioural structure.

[41] h3: 2.2 The Functional Implication of Behavioural Distance

[42] p: We next connect behavioural distance to task-level performance. In partially observable tasks where distinct latent modes require distinct optimal actions, insufficient probe-conditioned separation imposes a structural limit on robustness under prior shift. Let latent modes m ∈ { 0 , 1 } m\in\{0,1\} require distinct optimal actions a 0 ∗ ≠ a 1 ∗ a_{0}^{\ast}\neq a_{1}^{\ast} at o ∗ o^{\ast} , and let J ⁡ ( π ∣ P ) J(\pi\mid P) denote expected return under prior P ⁡ ( m ) P(m) . Let h m h_{m} denote the internal state induced at evaluation by the probe corresponding to latent mode m m . Assume the expected return under a given mode m m is bounded by V max − Δ ⁡ ( 1 − π ⁡ ( a m ∗ ∣ o ∗ , h m ) ) V_{\max}-\Delta(1-\pi(a_{m}^{\ast}\mid o^{\ast},h_{m})) , meaning any suboptimal action incurs a value penalty of at least Δ > 0 \Delta>0 .

[43] h6: Lemma 1 (Robustness Requires Epistemic Distance) .

[44] p: If the value penalty assumption holds and d ⁡ ( π ) ≤ ϵ d(\pi)\leq\epsilon , then

[45] table: min P ⁡ J ⁡ ( π ∣ P ) ≤ V max − Δ 2 ​ ( 1 − ϵ ) . \min_{P}J(\pi\mid P)\leq V_{\max}-\frac{\Delta}{2}(1-\epsilon). (6)

[46] h6: Proof.

[47] p: Let π m ​ ( a ) = π ⁡ ( a ∣ o ∗ , h m ) \pi_{m}(a)=\pi(a\mid o^{\ast},h_{m}) . Since a 0 ∗ ≠ a 1 ∗ a_{0}^{\ast}\neq a_{1}^{\ast} , the action probabilities under mode 1 satisfy π 1 ​ ( a 0 ∗ ) + π 1 ​ ( a 1 ∗ ) ≤ 1 \pi_{1}(a_{0}^{\ast})+\pi_{1}(a_{1}^{\ast})\leq 1 . The L 1 L_{1} behavioural distance constraint d ⁡ ( π ) ≤ ϵ d(\pi)\leq\epsilon implies that for any single action a a , | π 0 ​ ( a ) − π 1 ​ ( a ) | ≤ ϵ |\pi_{0}(a)-\pi_{1}(a)|\leq\epsilon . Consequently, for the optimal action a 0 ∗ a_{0}^{\ast} , we have π 1 ​ ( a 0 ∗ ) ≥ π 0 ​ ( a 0 ∗ ) − ϵ \pi_{1}(a_{0}^{\ast})\geq\pi_{0}(a_{0}^{\ast})-\epsilon .

[48] p: Substituting this lower bound into the sum constraint yields

[49] table: π 0 ​ ( a 0 ∗ ) − ϵ + π 1 ​ ( a 1 ∗ ) ≤ 1 ⇒ π 0 ​ ( a 0 ∗ ) + π 1 ​ ( a 1 ∗ ) ≤ 1 + ϵ . \pi_{0}(a_{0}^{\ast})-\epsilon+\pi_{1}(a_{1}^{\ast})\leq 1\;\Rightarrow\;\pi_{0}(a_{0}^{\ast})+\pi_{1}(a_{1}^{\ast})\leq 1+\epsilon. (7)

[50] p: Using min ⁡ ( x , y ) ≤ x + y 2 \min(x,y)\leq\frac{x+y}{2} gives

[51] table: min ⁡ ( π 0 ​ ( a 0 ∗ ) , π 1 ​ ( a 1 ∗ ) ) ≤ 1 2 ​ ( 1 + ϵ ) . \min(\pi_{0}(a_{0}^{\ast}),\pi_{1}(a_{1}^{\ast}))\leq\frac{1}{2}(1+\epsilon). (8)

[52] p: Substituting into the value model yields

[53] table: min P ⁡ J ⁡ ( π ∣ P ) ≤ V max − Δ ⁡ ( 1 − 1 + ϵ 2 ) = V max − Δ 2 ​ ( 1 − ϵ ) , \min_{P}J(\pi\mid P)\leq V_{\max}-\Delta\!\left(1-\frac{1+\epsilon}{2}\right)=V_{\max}-\frac{\Delta}{2}(1-\epsilon), (9)

[54] p: completing the proof. ∎

[55] p: Lemma 1 shows that behavioural distance is not merely descriptive but functionally necessary for robustness under latent prior shift. When d ⁡ ( π ) d(\pi) is small, the policy cannot simultaneously allocate high probability mass to both mode-specific optimal actions, imposing a ceiling on worst-case return. In the limiting case d ⁡ ( π ) = 0 d(\pi)=0 , the bound reduces to min P ⁡ J ⁡ ( π ∣ P ) ≤ V max − Δ / 2 \min_{P}J(\pi\mid P)\leq V_{\max}-\Delta/2 .

[56] h3: 2.3 Structural Non-Preservation under Policy Transformation

[57] p: We now analyse how common policy transformations affect behavioural distance.

[58] h4: Convex Aggregation.

[59] p: For π α = α ​ π 1 + ( 1 − α ) ​ π 2 \pi_{\alpha}=\alpha\pi_{1}+(1-\alpha)\pi_{2} , linearity implies

[60] table: R π α ​ ( p , o ∗ ) = α ​ R π 1 ​ ( p , o ∗ ) + ( 1 − α ) ​ R π 2 ​ ( p , o ∗ ) . R_{\pi_{\alpha}}(p,o^{\ast})=\alpha R_{\pi_{1}}(p,o^{\ast})+(1-\alpha)R_{\pi_{2}}(p,o^{\ast}). (10)

[61] h6: Lemma 2 (Convex Contraction) .

[62] p: For α ∈ [ 0 , 1 ] \alpha\in[0,1] ,

[63] table: d ⁡ ( π α ) ≤ α ​ d ​ ( π 1 ) + ( 1 − α ) ​ d ​ ( π 2 ) . d(\pi_{\alpha})\leq\alpha d(\pi_{1})+(1-\alpha)d(\pi_{2}). (11)

[64] h6: Proof.

[65] p: Let Δ i = R π i ​ ( p 0 , o ∗ ) − R π i ​ ( p 1 , o ∗ ) \Delta_{i}=R_{\pi_{i}}(p_{0},o^{\ast})-R_{\pi_{i}}(p_{1},o^{\ast}) . Then

[66] table: R π α ​ ( p 0 , o ∗ ) − R π α ​ ( p 1 , o ∗ ) = α ​ Δ 1 + ( 1 − α ) ​ Δ 2 . R_{\pi_{\alpha}}(p_{0},o^{\ast})-R_{\pi_{\alpha}}(p_{1},o^{\ast})=\alpha\Delta_{1}+(1-\alpha)\Delta_{2}. (12)

[67] p: Applying the triangle inequality yields the claim. ∎

[68] p: Define ℰ = { π ∣ d ⁡ ( π ) > 0 } \mathcal{E}=\{\pi\mid d(\pi)>0\} , where d ⁡ ( π ) d(\pi) is defined with respect to the fixed probe pair ( p 0 , p 1 ) (p_{0},p_{1}) .

[69] h6: Proposition 1 (Non-Closure under Convex Aggregation) .

[70] p: The set ℰ \mathcal{E} is not closed under convex combination.

[71] h6: Proof.

[72] p: Let π 1 ∈ ℰ \pi_{1}\in\mathcal{E} with distinct response distributions q 0 = R π 1 ​ ( p 0 , o ∗ ) q_{0}=R_{\pi_{1}}(p_{0},o^{\ast}) and q 1 = R π 1 ​ ( p 1 , o ∗ ) q_{1}=R_{\pi_{1}}(p_{1},o^{\ast}) . Construct π 2 \pi_{2} by swapping these responses so that R π 2 ​ ( p 0 , o ∗ ) = q 1 R_{\pi_{2}}(p_{0},o^{\ast})=q_{1} and R π 2 ​ ( p 1 , o ∗ ) = q 0 R_{\pi_{2}}(p_{1},o^{\ast})=q_{0} . Then d ⁡ ( π 2 ) > 0 d(\pi_{2})>0 . Their differences are anti-aligned:

[73] table: R π 1 ​ ( p 0 , o ∗ ) − R π 1 ​ ( p 1 , o ∗ ) = − ( R π 2 ​ ( p 0 , o ∗ ) − R π 2 ​ ( p 1 , o ∗ ) ) . R_{\pi_{1}}(p_{0},o^{\ast})-R_{\pi_{1}}(p_{1},o^{\ast})=-\big(R_{\pi_{2}}(p_{0},o^{\ast})-R_{\pi_{2}}(p_{1},o^{\ast})\big). (13)

[74] p: For α = 1 2 \alpha=\tfrac{1}{2} , d ⁡ ( π 1 / 2 ) = 0 d(\pi_{1/2})=0 , so π 1 / 2 ∉ ℰ \pi_{1/2}\notin\mathcal{E} . ∎

[75] h4: Gradient Transformation.

[76] p: We now analyse how gradient-based transformations affect behavioural distance. The following result is conditional and local. It does not assert that reward optimisation universally decreases behavioural distance; rather, it isolates a sufficient geometric condition under which contraction must occur.

[77] h6: Theorem 1 (Conditional Local Contraction Under Gradient Alignment) .

[78] p: For parameters θ \theta , assume ∇ θ d ​ ( π θ ) ≠ 0 \nabla_{\theta}d(\pi_{\theta})\neq 0 and define

[79] table: v d = − ∇ θ d ​ ( π θ ) ‖ ∇ θ d ​ ( π θ ) ‖ 2 . v_{d}=-\frac{\nabla_{\theta}d(\pi_{\theta})}{\|\nabla_{\theta}d(\pi_{\theta})\|_{2}}.

[80] p: Let J ⁡ ( θ ) = ( 1 − δ ) ​ J 0 ​ ( θ ) + δ ​ J 1 ​ ( θ ) J(\theta)=(1-\delta)J_{0}(\theta)+\delta J_{1}(\theta) with δ ∈ ( 0 , 0.5 ) \delta\in(0,0.5) .

[81] p: If ∇ J 0 ( θ ) ⊤ v d ≥ k > 0 \nabla J_{0}(\theta)^{\top}v_{d}\geq k>0 and ‖ ∇ J 1 ​ ( θ ) ‖ 2 ≤ L \|\nabla J_{1}(\theta)\|_{2}\leq L , then whenever

[82] table: δ < k k + L , \delta<\frac{k}{k+L},

[83] p: we have ∇ J ( θ ) ⊤ v d > 0 \nabla J(\theta)^{\top}v_{d}>0 , implying local decrease of d ⁡ ( π θ ) d(\pi_{\theta}) under gradient ascent.

[84] h6: Proof.

[85] table: ∇ J ( θ ) ⊤ v d = ( 1 − δ ) ∇ J 0 ( θ ) ⊤ v d + δ ∇ J 1 ( θ ) ⊤ v d . \nabla J(\theta)^{\top}v_{d}=(1-\delta)\nabla J_{0}(\theta)^{\top}v_{d}+\delta\nabla J_{1}(\theta)^{\top}v_{d}.

[86] p: Using the alignment and norm bounds yields

[87] table: ∇ J ( θ ) ⊤ v d ≥ ( 1 − δ ) k − δ L , \nabla J(\theta)^{\top}v_{d}\geq(1-\delta)k-\delta L,

[88] p: which is positive when δ < k k + L \delta<\frac{k}{k+L} . ∎

[89] p: The theorem provides a sufficient local condition under which reward optimisation contracts behavioural distance. When the alignment condition holds under skewed priors, gradient ascent reduces probe-conditioned separation even if dominant-prior reward remains stable. Whether such alignment arises depends on task structure, representation geometry, and optimisation dynamics.

[90] h2: 3 Structural Non-Preservation: Formal and Empirical Witnesses

[91] p: We provide minimal formal constructions and controlled empirical witnesses designed to isolate the structural mechanisms identified in Section 2.3 . These experiments are not intended as benchmark evaluations, but as diagnostic settings in which the theoretical conditions can be directly measured.

[92] h3: 3.1 Sequential Degradation and Robustness under Prior Shift

[93] p: We consider a partially observable gridworld to examine structural degradation in a sequential setting (Figure 1 ). An agent may execute a locally suboptimal diagnostic probe that reveals a latent mode m ∈ { 0 , 1 } m\in\{0,1\} determining the rewarding goal location. We evaluate three policies: a Probing policy ( d = 2 d=2 ), a Shortcut policy that ignores the probe ( d = 0 d=0 ), and an Aggregated policy formed by majority voting ( d = 1 d=1 ).

[94] figure: Figure 1 : Behavioural probe evaluation and representative trajectories in the partially observable gridworld. Left: The evaluation protocol. The agent acquires latent mode information to induce an internal hidden state h m h_{m} . It is subsequently evaluated at a fixed observation o ⋆ o^{\star} to measure the conditional policy π ( ⋅ ∣ o ⋆ , h m ) \pi(\cdot\mid o^{\star},h_{m}) . Second: Probing policy. The agent maintains separated internal representations and successfully executes distinct actions contingent on the initial mode. Third: Shortcut policy. The agent consistently navigates toward the same goal irrespective of the latent mode. Right: Aggregated policy. The agent may execute the probing action, but it fails to exhibit the consistent information-conditioned action differences of the probing agent.

[95] p: To isolate structural robustness, we evaluate these policies under a biased prior ℙ ⁡ ( m = 0 ) = 0.9 \mathbb{P}(m=0)=0.9 and a reversed prior ℙ ⁡ ( m = 0 ) = 0.1 \mathbb{P}(m=0)=0.1 without additional training. We also evaluate convex mixtures π α = α ​ π probe + ( 1 − α ) ​ π shortcut \pi_{\alpha}=\alpha\pi_{\text{probe}}+(1-\alpha)\pi_{\text{shortcut}} across both priors. Experiments are run over 300 episodes.

[96] figure: Policy Biased Prior Reversed Prior Probing 0.810 ± 0.000 0.810\pm 0.000 0.810 ± 0.000 0.810\pm 0.000 Shortcut 0.863 ± 0.017 0.863\pm 0.017 0.060 ± 0.019 0.060\pm 0.019 Aggregated 0.710 ± 0.023 0.710\pm 0.023 0.000 ± 0.020 0.000\pm 0.020 Figure 2 : Robustness under latent prior shift. Left: Average return of three policies evaluated under a biased prior and a reversed prior. The Shortcut policy attains high return under the biased prior despite zero behavioural distance, but degrades sharply under prior reversal. The Probing policy remains stable across priors ( m ​ e ​ a ​ n ± s ​ e mean\pm se ). Right: Convex mixtures π α = α ​ π probe + ( 1 − α ) ​ π shortcut \pi_{\alpha}=\alpha\pi_{\text{probe}}+(1-\alpha)\pi_{\text{shortcut}} . Behavioural distance decreases linearly with α \alpha , and robustness under prior shift decreases correspondingly, indicating that sensitivity to latent distribution shift is governed by probe-conditioned behavioural separation and not by biased-prior reward alone.

[97] p: As shown in Figure 2 , the Shortcut policy attains high return under the biased prior despite zero behavioural distance, but degrades sharply under prior reversal. The Probing policy remains stable across priors. Across convex mixtures, robustness under prior shift scales approximately with behavioural distance rather than biased-prior return. This illustrates that reward statistics under a dominant prior do not necessarily reflect structural robustness to latent distribution shift.

[98] h3: 3.2 Optimisation-Induced Structural Erosion

[99] p: We examine whether epistemic behavioural structure, once established, is preserved under continued gradient-based optimisation when the training objective becomes distributionally biased. Unlike the aggregation experiments, no explicit policy mixing is applied; the only transformation is reward-driven optimisation under a skewed latent prior.

[100] p: The task consists of three phases: a probe revealing a latent binary mode m ∈ { 0 , 1 } m\in\{0,1\} , a delay phase with distractors independent of m m , and an evaluation step at a fixed observation o ⋆ o^{\star} containing no information about m m . Correct action at o ⋆ o^{\star} therefore requires retention of probe information in recurrent state.

[101] p: Recurrent Advantage Actor–Critic (A2C) policies are first trained under a uniform prior ( P ⁡ ( m = 0 ) = 0.5 P(m=0)=0.5 ), yielding probe-conditioned separation. Optimisation then continues under a biased prior ( P ⁡ ( m = 0 ) = 0.98 P(m=0)=0.98 ). We measure return under biased and reversed priors, behavioural distance d ⁡ ( π ) d(\pi) at o ⋆ o^{\star} , hidden-state separation quantified by both ‖ h m = 0 − h m = 1 ‖ 2 \|h_{m=0}-h_{m=1}\|_{2} and its normalised variant. Further, we measure the majority force ( P r o j 0 = ∇ J 0 ( θ ) ⊤ 𝐯 d Proj_{0}=\nabla J_{0}(\theta)^{\top}\mathbf{v}_{d} ) and minority force ( P r o j 1 = ∇ J 1 ( θ ) ⊤ 𝐯 d Proj_{1}=\nabla J_{1}(\theta)^{\top}\mathbf{v}_{d} ) as the projections of mode-specific gradients onto the structural contraction vector 𝐯 d \mathbf{v}_{d} , the weighted sum of which constitutes the net structural force ℱ n ​ e ​ t = ( 1 − δ ) ​ P ​ r ​ o ​ j 0 + δ ​ P ​ r ​ o ​ j 1 \mathcal{F}_{net}=(1-\delta)Proj_{0}+\delta Proj_{1} that determines the direction of representational erosion. Results are averaged over 10 seeds (Figure 3 ). An extended description of the experimental setup and experimental evaluation over different prior shifts as well as network size, is presented in supplementary material (Appendix B ).

[102] p: Under biased optimisation, return on the dominant prior remains near-optimal while performance under the reversed prior degrades. Behavioural distance d ⁡ ( π ) d(\pi) contracts during the biased phase and stabilises at a reduced plateau. Absolute and relative hidden-state separation decrease in parallel, indicating deformation of internal representation geometry alongside behavioural attenuation.

[103] figure: Figure 3 : Optimisation-induced structural erosion under a heavily biased prior (98%). Left: Behavioural erosion. Return under the dominant prior remains stable while reversed-prior performance degrades. Behavioural distance decreases during biased optimisation and stabilises at a lower value. Middle: Representational erosion. Absolute and normalised hidden-state separation contract over training. Right: Mechanistic verification. Projection of task gradients onto 𝐯 d = − ∇ d / ∥ ∇ d ∥ \mathbf{v}_{d}=-\nabla d/\|\nabla d\| yields a persistent positive net structural force under the biased prior, consistent with Theorem 1 . Shaded regions denote ± \pm one standard deviation across 10 seeds.

[104] p: The projected structural force remains positive throughout the erosion regime, indicating local alignment between reward optimisation and contraction of behavioural distance. Although contraction slows as d ⁡ ( π ) d(\pi) decreases, the persistent alignment is consistent with the sufficient condition in Theorem 1 .

[105] p: These results show that stability of reward under a dominant prior does not ensure preservation of probe-conditioned structure. Continued optimisation under skewed objectives can attenuate epistemic behavioural dependency even without explicit aggregation. These observations motivate analysing preservation at the level of probe-conditioned behavioural equivalence classes, which treats them as the units of preservation under policy transformation.

[106] h2: 4 Behavioural Representation and Preservation: An Interpretive Lens

[107] p: The preceding analysis suggests viewing probe-conditioned behavioural equivalence classes as units of structural comparison under policy transformation. We refer to this perspective as Behavioural Representation and Preservation (BRP). BRP is not proposed as a formal framework or algorithmic prescription. It provides a lens for evaluating whether reinforcement learning transformations preserve probe-conditioned behavioural structure.

[108] h3: 4.1 Analytical Dimensions of Preservation

[109] p: Under the BRP lens, preservation of probe-conditioned behavioural structure can be analysed along three dimensions. These are not prescriptive requirements for an algorithm, but descriptive criteria for evaluating how a transformation affects behavioural equivalence classes.

[110] h4: Identifiability.

[111] p: Identifiability concerns whether distinct information-conditioned strategies are distinguishable under the chosen probe set P P . A probe set induces identifiable structure if behaviourally distinct policies exhibit sufficiently separated response profiles (i.e., d ⁡ ( π ) ≫ 0 d(\pi)\gg 0 relative to tolerance ε \varepsilon ). If probes fail to induce measurable separation, equivalence classes collapse trivially, and preservation cannot be meaningfully assessed. Identifiability therefore depends jointly on probe design and task structure rather than on architectural properties alone.

[112] h4: Retention.

[113] p: Retention concerns whether a transformation T T preserves probe-conditioned response profiles. Given a policy π \pi and transformed policy T ⁡ ( π ) T(\pi) , retention can be evaluated by measuring whether π \pi and T ⁡ ( π ) T(\pi) remain within the same ε \varepsilon -behavioural equivalence class under the chosen probes. As shown in Section 2.3 , common transformations such as convex aggregation and gradient updates under skewed priors do not generally guarantee such invariance. Retention is thus a property of the transformation relative to a probe set, not of parameter similarity or reward stability.

[114] h4: Transferability.

[115] p: Transferability concerns whether probe-conditioned behavioural structure can be reproduced across policies, training regimes, or environments. Two policies trained under different initialisations or optimisation dynamics may belong to the same ε \varepsilon -equivalence class even if their internal representations differ. Transferability therefore focuses on reproducibility of response profiles rather than internal state geometry. Under this view, preservation across agents or training phases amounts to re-instantiating the same probe-relative behavioural class.

[116] h3: 4.2 Preservation Criterion

[117] p: Under this lens, epistemic competence corresponds to stability of probe-conditioned response profiles under transformation T T . A transformation is preservation-consistent if it is approximately ϵ \epsilon -equivalence-preserving with respect to the chosen probe set. BRP therefore provides a structural criterion for evaluating whether reinforcement learning methods retain information-conditioned interaction patterns across optimisation, aggregation, or compression.

[118] p: BRP does not prescribe a specific optimisation method. Instead, it suggests that claims about preservation of epistemic behaviour should be evaluated at the level of probe-conditioned response profiles rather than solely through reward statistics. High reward under a dominant prior is insufficient to establish preservation of behavioural dependency.

[119] h2: 5 Discussion and Conclusion

[120] p: This paper analysed preservation of epistemic behaviour under standard reinforcement learning transformations. By formalising probe-relative behavioural dependency and ϵ \epsilon -behavioural equivalence, we showed that common operators, including convex policy averaging and reward-driven gradient updates, do not generally preserve information-conditioned interaction patterns. The set of policies exhibiting non-trivial behavioural dependency is not closed under convex aggregation, and gradient updates under sufficiently skewed priors can erode behavioural distance under the stated alignment condition. Structural preservation therefore cannot be inferred from reward stability alone, even when training performance remains near-optimal. Although Theorem 1 is stated for discrete latent priors, the mechanism suggests a broader principle: distributional imbalance can induce gradient dominance along erosion directions.

[121] p: Empirically, these structural effects arise in standard actor-critic neural RL under the examined conditions. In the optimisation setting, behavioural erosion precedes degradation under prior shift, and projection analysis confirms alignment between reward gradients and reductions in behavioural distance. While other learning dynamics may exhibit different sensitivities, the results demonstrate that In the examined partially observable settings, gradient-based optimisation under skewed priors reduces behavioural distance while dominant-prior reward remains near-optimal.

[122] p: BRP articulates the representational perspective implied by these findings. By treating ϵ \epsilon -behavioural equivalence classes as units of analysis, it separates task performance from structural preservation and provides criteria for evaluating whether transformations retain probe-conditioned behaviour.

[123] p: Open questions remain. The alignment condition in Theorem 1 is sufficient but not necessary; characterising when such alignment arises across architectures and task distributions remains an open question. The prevalence of the alignment condition across architectures and algorithmic classes requires further study, as does scalable probe design in high-dimensional environments. Overall, this work introduces a structural vocabulary for analysing retention and attenuation of epistemic competence under reinforcement learning transformations.

[124] h2: References

[125] p: Supplementary Materials

[126] p: The following content was not necessarily subject to peer review.

[127] h2: Appendix A Extended Discussion: Structural Vulnerabilities in RL Pipelines

[128] p: Epistemic behaviour arises when action selection depends on internally accumulated information rather than solely on immediate observation. As established in Section 2.1 , because such dependency is not represented explicitly in standard reinforcement learning pipelines, common transformations are not guaranteed to preserve ϵ \epsilon -behavioural equivalence.

[129] p: The mechanisms below illustrate exactly how the mathematical vulnerabilities identified in Section 2.3 (dilution, non-closure, and gradient erosion) actively manifest across modern reinforcement learning paradigms.

[130] h3: A.1 Implicitness and Optimisation-Induced Collapse in Meta-RL

[131] p: Information-conditioned behaviour is typically realised through parameters, latent activations, or recurrent dynamics trained exclusively for reward maximisation. Meta-reinforcement learning systems such as R ​ L 2 RL^{2} ( Duan et al., 2016 ) and latent-context approaches including PEARL and VariBAD ( Rakelly et al., 2019 ; Zintgraf et al., 2021 ) condition actions on accumulated interaction history or inferred task variables, thus instantiating behavioural dependency.

[132] p: However, because optimisation updates operate on representations rather than behavioural equivalence classes, these methods are susceptible to the continuous structural erosion described by Theorem 1 . When the task distribution (latent prior) is skewed or exhibits curriculum shifts, the gradient update T grad T_{\text{grad}} acts as an equivalence-breaking transformation under the stated prior conditions, inducing a tendency toward reduction of behavioural distance even when short-horizon reward remains high. Consequently, information-conditioned distinctions that support rapid adaptation can be attenuated during continued training once the minority tasks are rarely sampled, leading to silent losses in meta-generalisation even if average reward remains stable.

[133] h3: A.2 Aggregation and Behavioural Homogenisation

[134] p: Aggregation procedures, such as parameter averaging, policy distillation, and logit ensembling, operate on parameters or action distributions and do not enforce the preservation of response profiles. World-model-based agents such as Dreamer and MuZero ( Ha and Schmidhuber, 2018 ; Hafner and others, 2021 ; Schrittwieser et al., 2020 ) rely on latent predictive states or internal search processes to guide action selection.

[135] p: When such policies are compressed or aggregated, short-horizon reward performance may remain similar while distinctions in probe-relative response profiles are reduced. In distributed or federated reinforcement learning, periodic averaging treats deviations across agents as noise, even when those deviations reflect distinct information-conditioned strategies. As shown by Lemma 2 (Convex Contraction) andProposition 1 (Non-Closure), convex aggregation can break equivalence class membership and cannot increase behavioural distance beyond the weighted average. Because epistemic structure is at most diluted under convex combination, this aggregation systematically homogenises and destroys structured epistemic behaviour across the population.

[136] h3: A.3 Temporal Erosion of Structured Exploration

[137] p: Exploration strategies driven by novelty, prediction error, or uncertainty estimates depend on internally accumulated signals and therefore instantiate behavioural dependency ( Pathak et al., 2017 ; Bellemare et al., 2016 ; Houthooft et al., 2016 ) . Empirical studies report that exploratory behaviour often diminishes as predictive models improve or uncertainty estimates contract ( Burda et al., 2019 ; Raileanu et al., 2022 ) .

[138] p: The gradient mechanism formalised in Theorem 1 provides one structural explanation for this phenomenon. When optimisation becomes dominated by a subset of modes or states, reward gradients may align with directions that reduce distinctions no longer directly contributing to expected return significantly. In such regimes, the projected gradient onto the contraction direction 𝐯 d \mathbf{v}_{d} can become positive, inducing attenuation of behavioural dependency even while reward remains stable.

[139] p: We do not claim that exploration collapse is universal or inevitable. The present lens identifies a sufficient structural condition under which internally encoded exploratory distinctions may erode during continued reward-driven optimisation. Absent explicit constraints that preserve ϵ \epsilon -behavioural equivalence classes, exploration-related representations can be gradually attenuated when they cease to provide immediate reward advantage.

[140] h2: Appendix B Supplemental Material: Experimental Details

[141] h3: B.1 Environment Specification: The Abstract Epistemic MDP

[142] p: The AbstractEpistemicEnv is a partially observable MDP designed to force reliance on internal memory by separating critical information from reward-bearing observations. The environment consists of three temporal phases:

[143] p: Probe Phase ( t = 0 t=0 ): A latent binary mode m ∈ { 0 , 1 } m\in\{0,1\} is revealed via a dedicated bit in the 5D observation vector [ is_probe , is_delay , is_eval , distractor , mode_bit ] [\,\text{is\_probe},\,\text{is\_delay},\,\text{is\_eval},\,\text{distractor},\,\text{mode\_bit}\,] .

[144] p: Delay Phase ( 1 ≤ t < T 1\leq t<T ): The agent must match random distractor bits to survive, receiving a + 0.1 +0.1 reward per step. Failure to match results in immediate termination ( − 1.0 -1.0 reward).

[145] p: Evaluation Phase ( t = T t=T ): The agent receives a fixed “Zero Info” observation o ∗ = [ 0 , 0 , 1 , 0 , 0 ] o^{\ast}=[0,0,1,0,0] . It must output the action matching the initial mode m m to receive a + 1.0 +1.0 reward.

[146] p: The environment is shown schematically in figure 4 .

[147] figure: Figure 4 : Abstract Epistemic MDP. A three-phase partially observable task consisting of a probe phase revealing latent mode m m , a distractor delay phase independent of m m , and a final evaluation phase at a fixed observation o ∗ o^{\ast} that requires retention of probe information. The task enforces an epistemic bottleneck between information acquisition and reward.

[148] h3: B.2 optimisation and Hyperparameters

[149] p: Structural erosion is observed using a two-stage training protocol. In Stage 1 (Synthesis) , policies are trained under a uniform prior ( δ = 0.5 \delta=0.5 ) using Advantage Actor–Critic (A2C) until the behavioural distance d ⁡ ( π ) > 1.90 d(\pi)>1.90 . To encourage epistemic competence (by recalling the latent mode in the hidden state), the agent receives a reward of + 5 +5 upon successfully reaching the goal. In Stage 2 (Erosion) , optimisation continues under biased priors ( δ ∈ { 0.6 , … , 0.98 } \delta\in\{0.6,\dots,0.98\} ) and + 1 +1 reward for reaching the goal.

[150] figure: Table 1 : Hyperparameters for Stage 2 (Erosion) Experiments Parameter Value Optimizer Adam Learning Rate 2 × 10 − 4 2\times 10^{-4} Weight Decay 1 × 10 − 3 1\times 10^{-3} Batch Size 32 episodes Discount Factor ( γ \gamma ) 0.99 Entropy Coefficient 0.02

[151] h3: B.3 Sensitivity to Prior Skew

[152] p: Empirical results across 10 independent seeds (Table 2 ) indicate a phase transition toward functional degradation as the prior skew exceeds δ = 0.95 \delta=0.95 . At δ = 0.965 \delta=0.965 , behavioural variance increases markedly (0.449), suggesting the onset of structural instability. As shown in Figure 5 , behavioural distance decreases systematically with increasing prior skew, and extreme bias ( δ = 0.98 \delta=0.98 ) is associated with functional degradation and reduced d ⁡ ( π ) d(\pi) . The decay of internal representation geometry precedes observable functional degradation, indicating that structural contraction serves as an early signal of robustness failure.

[153] figure: Table 2 : Final Epistemic Metrics across Prior Skew ( δ \delta ) Sweep ( m ​ e ​ a ​ n ± s ​ e mean\pm se , 10 seeds) Prior Skew ( δ \delta ) Final Behavioural Distance d ⁡ ( π ) d(\pi) Final Hidden Distance h dist h_{\text{dist}} δ = 0.600 \delta=0.600 1.939 ± 0.010 1.939\pm 0.010 2.809 ± 0.153 2.809\pm 0.153 δ = 0.800 \delta=0.800 1.911 ± 0.027 1.911\pm 0.027 2.714 ± 0.208 2.714\pm 0.208 δ = 0.900 \delta=0.900 1.853 ± 0.039 1.853\pm 0.039 2.582 ± 0.153 2.582\pm 0.153 δ = 0.950 \delta=0.950 1.743 ± 0.092 1.743\pm 0.092 2.443 ± 0.141 2.443\pm 0.141 δ = 0.965 \delta=0.965 1.517 ± 0.449 1.517\pm 0.449 2.133 ± 0.426 2.133\pm 0.426 δ = 0.980 \delta=0.980 1.369 ± 0.238 1.369\pm 0.238 2.050 ± 0.203 2.050\pm 0.203

[154] figure: Figure 5 : Sensitivity to Prior Skew. (Left) Functional degradation on the rare mode most pronounced at δ = 0.98 \delta=0.98 . (Center) Behavioural distance d ⁡ ( π ) d(\pi) decreasing as skew increases. (Right) Decay of internal representation geometry across biased priors, preceding functional failure.

[155] h3: B.4 Effect of Network Capacity under Extreme Skew

[156] p: To test whether erosion is an artifact of limited architectural capacity, we swept the hidden dimension H ∈ { 32 , 64 , 128 } H\in\{32,64,128\} under a fixed extreme bias ( δ = 0.98 \delta=0.98 ). Final values are summarized in Table 3 .

[157] p: Increasing recurrent capacity does not prevent behavioural erosion under extreme skew. While the H = 128 H=128 model begins with a larger initial representational separation, it exhibits greater variability during training compared to smaller models (Figure 6 ).

[158] figure: Table 3 : Final Epistemic Metrics by Network Capacity ( H H ) at δ = 0.98 \delta=0.98 ( m ​ e ​ a ​ n ± s ​ e mean\pm se , 10 seeds) Hidden Units ( H H ) Final Behavioural Distance d ⁡ ( π ) d(\pi) Final Hidden Distance h dist h_{\text{dist}} 32 32 1.350 ± 0.171 1.350\pm 0.171 2.025 ± 0.205 2.025\pm 0.205 64 64 1.422 ± 0.437 1.422\pm 0.437 2.357 ± 0.414 2.357\pm 0.414 128 128 1.266 ± 0.618 1.266\pm 0.618 2.565 ± 0.607 2.565\pm 0.607

[159] p: Functional instability: Higher capacity ( H = 128 H=128 ) induces oscillatory rare-mode reward, consistent with repeated partial recovery and subsequent attenuation of minority representations.

[160] p: Capacity-invariant erosion: Despite a 4 × 4\times capacity increase, all models converge to similarly reduced behavioural distances ( d ⁡ ( π ) ≈ 1.3 d(\pi)\approx 1.3 ).

[161] p: Variance scaling: Larger networks exhibit higher variance in final d ⁡ ( π ) d(\pi) without mitigating structural erosion.

[162] figure: Figure 6 : Capacity Sweep Results. (Left) Rare-mode reward exhibits increased instability at H = 128 H=128 . (Center) Behavioural erosion remains comparable across network sizes. (Right) Representational distance decays across all capacities under extreme skew.

[163] h3: B.5 Implications for Structural Preservation

[164] p: These results empirically witness the theoretical vulnerabilities identified by the BRP lens, particularly for policy gradient methods. In our A2C experiments and in the analysed setting, gradient-driven optimisation under sufficiently skewed priors attenuates probe-conditioned behavioural separation, eroding d ⁡ ( π ) d(\pi) regardless of architectural capacity. While overparameterised networks can theoretically maintain dual-mode representations, the strong gradient bias actively disfavors this. Although alternative learning dynamics, such as value-based methods, may exhibit different structural sensitivities, these findings indicate that excess capacity alone yields functional instability rather than structural preservation. This suggests that epistemic competence cannot be passively guaranteed through architecture alone, motivating the need for explicit constraints at the behavioural level.

[165] h2: Instructions for reporting errors

[166] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[167] p: Tip: You can select the relevant text first, to include it in your report.

[168] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[169] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
