[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] p: theorem]Definition

[3] h1: Training Generalizable Collaborative Agents via Strategic Risk Aversion

[4] h6: Abstract

[5] p: Many emerging agentic paradigms require agents to collaborate with one another (or people) to achieve shared goals. Unfortunately, existing approaches to learning policies for such collaborative problems produce brittle solutions that fail when paired with new partners. We attribute these failures to a combination of free-riding during training and a lack of strategic robustness . To address these problems, we study the concept of strategic risk aversion and interpret it as a principled inductive bias for generalizable cooperation with unseen partners. While strategically risk-averse players are robust to deviations in their partner’s behavior by design, we show that, in collaborative games, they also (1) can have better equilibrium outcomes than those at classical game-theoretic concepts like Nash, and (2) exhibit less or no free-riding. Inspired by these insights, we develop a multi-agent reinforcement learning (MARL) algorithm that integrates strategic risk aversion into standard policy optimization methods. Our empirical results across collaborative benchmarks (including an LLM collaboration task) validate our theory and demonstrate that our approach consistently achieves reliable collaboration with heterogeneous and previously unseen partners across collaborative tasks.

[6] p: Keywords: Strategic risk aversion, multi-agent reinforcement learning, partner generalization

[7] h2: 1 Introduction

[8] p: AI systems increasingly operate in multi-agent environments, where success depends on effective interaction with other agents. An increasingly important subset of these problems involves agents solving collaborative tasks —i.e., tasks where agents must work together towards a shared goal. Examples of such problems range from robots coordinating with people in shared physical spaces like warehouses ( Kruse et al., 2013 ) , to emerging “agentic AI” problems where multiple models collaborate to write code ( Wu et al., 2024 ) or solve math problems ( Cemri et al., 2025 ) .

[9] p: A common approach to such problems is to view them as collaborative games and use concepts from game theory to design algorithms to learn collaborative policies ( Dafoe et al., 2021 ) . Viewed through this lens, a central challenge in collaborative games is partner generalization —where one seeks to maintain effective interaction across new sets of partners ( Carroll et al., 2019 ; Hu et al., 2020 ; Ruhdorfer et al., 2025 ) . Indeed, in many real-world settings, agents must navigate situations in which they interact with different partners (either algorithmic or human) who may have slightly different goals, heuristics, or levels of competence. Agents should learn strategies that work well across a broad range of partners without sacrificing performance. Unfortunately, current approaches tend to struggle with this—with learned policies often failing to generalize to new partners ( Stone et al., 2010 ) , or overfitting to other agents’ eccentricities and becoming overly reliant on specific conventions ( Carroll et al., 2019 ; Lerer and Peysakhovich, 2019 ) .

[10] p: We view the problem of partner generalization as ultimately a question of robustness of the learned policy and of alignment between agents ( Leibo et al., 2017 ) . The need for robustness emerges from the requirement that learned strategies be insensitive to changes in a partner’s strategy and degrade gracefully in performance as the partners become less collaborative. The need for alignment emerges from a desire to find agents that contribute proportionally to the task. If agents learn to under-contribute or delegate costly actions ( Sunehag et al., 2018 ; Liu et al., 2023 ) to their partners—effectively free-riding on their partner’s effort—they cannot generalize to new environments and partners. While free-riding is a widely acknowledged phenomenon in game theory, it is rarely studied as a problem in collaborative multi-agent learning despite recent empirical evidence that it arises even with large AI models ( Zhang et al., 2025 ) .

[11] p: Prior work—which we review in Section 2 and then in depth in Appendix A —has studied partner generalization in specific settings that fail to scale to large-scale problems like the post-training of LLM agents ( Hu et al., 2020 ) or via largely heuristic approaches ( Forkel and Foerster, 2025 ) . In contrast, in this paper we advance strategic risk aversion as a principled and scalable approach to addressing this issue in a broad class of collaborative games.

[12] p: Recently proposed in multi-agent reinforcement learning (MARL) to derive human-like strategies in general games ( Mazumdar et al., 2024 ) , strategic risk aversion mirrors behaviors observed in people in experimental economics ( Goeree et al., 2003 ) . Unlike many approaches to robustness or risk aversion in MARL which primarily focus on robustness to uncertainty in the underlying environment, strategic risk aversion posits that agents should be risk-averse to uncertainty stemming from their opponents’ decisions. This perspective inherently aligns with the goal of partner generalization, as it forces agents to be robust to deviations in their partner’s play.

[13] p: Formalizing this principle leads to a new equilibrium concept: (Strategically) Risk-Averse Quantal Response Equilibria (RQE) ( Mazumdar et al., 2024 ) . While RQE has been shown to better capture human play in simple experiments and offer better computational tractability ( Zhang and Mazumdar, 2025 ) than classic game theoretic concepts, its potential for collaborative games and partner generalization remains unknown. We argue that strategic risk aversion provides a suitable inductive bias for robust cooperation in collaborative games: at an RQE, an agent is trained against a structured set of plausible partner deviations, governed by the agent’s degree of risk aversion. This ensures strategies are robust without being overly conservative.

[14] p: Contributions: Through both a theoretical analysis of RQE in structured collaborative games and extensive experiments across a range of diverse multi-agent benchmarks, we validate that RQE are particularly suited for collaborative tasks. In particular, our contributions are as follows:

[15] p: Incentivizing collaboration ( Section 4.1 ): We prove that in continuous quadratic aggregative games, strategic risk aversion can encourage collaboration, with higher risk aversion leading to a greater focus on the shared goal. This implies a counterintuitive result: unlike in classic robust optimization or RL, robustness does not necessarily require sacrificing performance .

[16] p: Alleviating free-riding ( Section 4.2 ): We prove in finite-action collaborative games with private costs that strategic risk aversion can mitigate free-riding at equilibrium. Thus, risk aversion can reduce the alignment problem in collaborative MARL.

[17] p: Scalable risk-averse MARL algorithms: We develop Strategically Risk-Averse Policy Optimization (SRPO), a MARL algorithm that optimizes an RQE-derived objective which integrates naturally with policy-optimization algorithms like independent proximal policy optimization (IPPO).

[18] p: Empirical validation: We demonstrate across collaborative MARL benchmarks that SRPO consistently achieves more reliable coordination with heterogeneous and unseen partners than IPPO (the current scalable MARL baseline). We observe that while IPPO performs well, it consistently finds free-riding equilibria that limit its generalization. In contrast, we observe—in line with our theory—that RQE found by SRPO exhibit no free-riding and result in better partner generalization. We also provide preliminary small-scale experiments showing that these findings can even extend to the fine-tuning of collaborative agentic AI teams made up of large language models, demonstrating the scalability of our approach.

[19] h2: 2 Related Works

[20] p: Our work studies strategic risk aversion in collaborative MARL. We cover the most relevant related work here and defer a more in depth discussion to Appendix A .

[21] p: The most related literature in collaborative MARL focuses on the partner generalization problem; i.e., how to learn collaborative policies that remain effective when paired with previously unseen partners ( Barrett et al., 2014 ; Carroll et al., 2019 ; Dizdarević et al., 2025 ) . This is sometimes referred to as zero-shot coordination ( Hu et al., 2020 ; Hu et al., 2021 ) , or ad-hoc teamwork problem ( Stone et al., 2010 ) . One large class of approaches can broadly be described as population-based methods ( Vinyals et al., 2019 ; Zhao et al., 2023 ; Yu et al., 2023 ; Wang et al., 2024 ; Rahman et al., 2023 ; Lupu et al., 2021 ) in which one trains against a diverse set of learned policies—essentially performing domain randomization for partners. Though such approaches are conceptually simple, the task of generating good populations of partners is nontrivial and typically relies on heuristic, task-dependent design choices. Furthermore, such approaches quickly become computationally intractable for complex, high-dimensional settings (e.g., LLM fine-tuning) and tend not to have strong guarantees that they result in better generalization. To circumvent this limitation, Forkel and Foerster (2025) attempt to induce robustness by introducing more randomness during training (by increasing entropy regularization in policy optimization). Though this method scales well, our experiments demonstrate that it does not solve free-riding and consequently does not address the problem of generalization across collaborative tasks.

[22] p: In contrast, our approach based on strategic risk aversion scales as a simple modification to existing policy-optimization techniques, is grounded in a principled game theoretic formulation, and empirically consistently delivers more stable cross-play performance across collaborative benchmarks. While these forms of risk aversion have been well studied in the experimental economics literature ( Gollier, 2001 ; Goeree and Offerman, 2002 ; Goeree et al., 2003 ) , they have only recently been studied in theory ( Lanzetti et al., 2025b ; Mazumdar et al., 2024 ) and in MARL ( Zhang and Mazumdar, 2025 ; Slumbers et al., 2023 ) . We demonstrate its potential in collaborative games.

[23] h2: 3 Problem Setup

[24] p: We consider a general-sum collaborative game with N N players. Each player i ∈ [ N ] i\in[N] is endowed with actions a i ∈ 𝒜 i a_{i}\in\mathcal{A}_{i} , where the action spaces can be discrete or continuous, and we use the notation 𝒜 − i = ∏ j ≠ i 𝒜 j \mathcal{A}_{-i}=\prod_{j\neq i}\mathcal{A}_{j} for the action space of all players except i i . Each player aims to maximize a utility function u i : 𝒜 i × 𝒜 − i → ℝ u_{i}:\mathcal{A}_{i}\times\mathcal{A}_{-i}\rightarrow\mathbb{R} . The utility function consists of a shared reward R R , which coincides for all players, and a private cost c i c_{i} , so that

[25] table: u i ​ ( a i , a − i ) = R ⁡ ( a 1 , … , a N ) − c i ​ ( a i ) . u_{i}(a_{i},a_{-i})=R(a_{1},\ldots,a_{N})-c_{i}(a_{i}).

[26] p: These games are collaborative since all players seek to maximize the reward, but pay for their own effort. They have been well studied in economics under the guise of public goods games and naturally model many real-world scenarios where players aim to collaboratively accomplish a task but are penalized for their own effort. The players select a mixed strategy x i ∈ Δ ⁡ ( 𝒜 i ) x_{i}\in\Delta(\mathcal{A}_{i}) , which is a probability over the available actions 𝒜 i \mathcal{A}_{i} (here, Δ ⁡ ( 𝒜 i ) \Delta(\mathcal{A}_{i}) is the set of probability distributions over 𝒜 i \mathcal{A}_{i} ). In the standard game-theoretic setting, the utility of each player is then the standard risk-neutral expected utility

[27] table: U i ​ ( x i , x − i ) = 𝔼 a 1 ∼ x 1 . . . a N ∼ x N ​ [ u i ​ ( a i , a − i ) ] , U_{i}(x_{i},x_{-i})=\mathbb{E}_{\begin{subarray}{c}a_{1}\sim x_{1}\\ ...\\ a_{N}\sim x_{N}\end{subarray}}[u_{i}(a_{i},a_{-i})],

[28] p: where x − i x_{-i} is the collection of the mixed strategies of all other players j ≠ i j\neq i .

[29] p: In this work, we follow Mazumdar et al. (2024) and propose to introduce two elements of human decision-making: risk aversion and bounded rationality.

[30] h5: Risk aversion

[31] p: To model risk aversion, we consider players that seek to optimize a risk-adjusted utility based on the entropic risk measure with risk aversion parameter τ i > 0 \tau_{i}>0 (e.g., see Föllmer and Schied (2002) ), instead of their expected utility. Players’ resulting objectives are given by

[32] table: U i τ i ( x i , x − i ) = inf p ∈ Δ ⁡ ( 𝒜 − i ) U i ( x i , p ) + 1 τ i KL ( p , x − i ) . U^{\tau_{i}}_{i}(x_{i},x_{-i})=\inf_{p\in\Delta(\mathcal{A}_{-i})}U_{i}(x_{i},p)+\frac{1}{\tau_{i}}\KL(p,x_{-i}). (1)

[33] p: In words, the utility results from a worst-case approach, in which a fictitious adversary tries to inflict maximum damage at the (risk-neutral) expected utility, while not deviating “too much” from the strategies of all other players. For the sake of this paper, we will measure this deviation with the KL divergence, defined as KL ( p , q ) = ∑ j p j ​ log ⁡ ( p j q j ) \KL(p,q)=\sum_{j}p_{j}\log(\frac{p_j}{q_j}) (when 𝒜 − i \mathcal{A}_{-i} is discrete) and KL ( p , q ) = ∫ ℝ n ρ p ​ ( x ) ​ log ⁡ ( ρ p ​ ( x ) ρ q ​ ( x ) ) \KL(p,q)=\int_{\mathbb{R}^{n}}\rho_{p}(x)\log(\frac{\rho_p(x)}{\rho_q(x)}) (when 𝒜 − i = ℝ n \mathcal{A}_{-i}=\mathbb{R}^{n} is continuous), where ρ p \rho_{p} and ρ q \rho_{q} are the densities of p p and q q (provided they exist, else KL ( p , q ) = + ∞ \KL(p,q)=+\infty ). Our choice of the entropic risk measure is rooted in operations research, but also motivated by ubiquitous use of the KL divergence across machine learning and in particular in policy optimization in reinforcement learning. By focusing on the KL divergence, we derive algorithms that can be implemented with minimal changes to existing codebases.

[34] h5: Bounded rationality

[35] p: To incorporate bounded rationality, we add entropy to each player’s utility, so that their utility is

[36] table: U i τ i , ϵ i ​ ( x i , x − i ) \displaystyle U_{i}^{\tau_{i},\epsilon_{i}}(x_{i},x_{-i}) = U i τ i ​ ( x i , x − i ) − ϵ i ​ H ​ ( x i ) , \displaystyle=U^{\tau_{i}}_{i}(x_{i},x_{-i})-\epsilon_{i}H(x_{i}), (2)

[37] p: where ϵ i > 0 \epsilon_{i}>0 and H ⁡ ( x i ) H(x_{i}) is the (negative) entropy of the mixed strategy x i x_{i} ; i.e., H ⁡ ( p ) = ∑ j p j ​ log ⁡ ( p j ) H(p)=\sum_{j}p_{j}\log(p_j) (if 𝒜 i \mathcal{A}_{i} is discrete) and H ⁡ ( p ) = ∫ ℝ n ρ p ​ ( x ) ​ log ⁡ ( ρ p ​ ( x ) ) ​ d x H(p)=\int_{\mathbb{R}^{n}}\rho_{p}(x)\log(\rho_p(x))\differential x (when 𝒜 i = ℝ n \mathcal{A}_{i}=\mathbb{R}^{n} is continuous), where ρ p \rho_{p} is again the density of p p (provided it exists, else H ⁡ ( p ) = + ∞ H(p)=+\infty ). Entropy regularization of the utility leads to the celebrated quantal response model in behavioral economics ( McKelvey and Palfrey, 1995 ) and is widely employed in machine learning for exploration purposes (e.g., see Ahmed et al. (2019) ). For more general regularization schemes, we refer to Mazumdar et al. (2024) .

[38] h5: Risk-averse quantal response equilibrium (RQE).

[39] p: Given our new utility U i τ i , ϵ i ​ ( x i , x − i ) U_{i}^{\tau_{i},\epsilon_{i}}(x_{i},x_{-i}) , we now define a RQE as a set of joint mixed strategies from which no player has an incentive to unilaterally deviate:

[40] p: [ Mazumdar et al. (2024) , Definition 5] A tuple of mixed strategies ( x 1 ⋆ , … , x N ⋆ ) (x_{1}^{\star},\ldots,x_{N}^{\star}) is a risk-averse quantal response equilibrium (RQE) with degrees of risk aversion τ 1 , … , τ N \tau_{1},\ldots,\tau_{N} and bounded rationality ϵ 1 , … , ϵ N \epsilon_{1},\ldots,\epsilon_{N} if for all players i i we have

[41] table: U i τ i , ϵ i ​ ( x i , x − i ⋆ ) ≤ U i τ i , ϵ i ​ ( x i ⋆ , x − i ⋆ ) ​ ∀ x i ∈ Δ ⁡ ( 𝒜 i ) . U^{\tau_{i},\epsilon_{i}}_{i}(x_{i},x_{-i}^{\star})\leq U^{\tau_{i},\epsilon_{i}}_{i}(x_{i}^{\star},x_{-i}^{\star})\>\forall\,x_{i}\in\Delta(\mathcal{A}_{i}). (3)

[42] p: When τ i , ϵ i → 0 \tau_{i},\epsilon_{i}\to 0 we recover Nash equilibria, when τ i → 0 \tau_{i}\to 0 we recover quantal response equilibria, and when ϵ → 0 \epsilon\rightarrow 0 and τ → ∞ \tau\rightarrow\infty we recover security strategies. In the next section, we investigate the benefits of risk aversion, together with bounded rationality, in two classes of collaborative games: aggregative continuous quadratic games and finite symmetric collaborative games. These insights prompt us, in the subsequent section, to use RQE for the design of algorithms to train collaborative agents in MARL.

[43] h2: 4 “Free-Lunch” Theorems for Strategic Risk Aversion in Collaborative Games

[44] figure: Figure 1 : (i). Expected utility of each player as a function of the degree of risk aversion τ \tau at equilibrium, when ϵ = 1 \epsilon=1 in Section 4.1 . Player’s utilities can first increase with risk aversion before decreasing due to over-conservatism, meaning that strategic risk aversion can yield better performing equilibria than Nash or QRE. (ii). Probability that a player collaborates at a RQE as a function of the level of risk aversion, for ϵ = 0.2 \epsilon=0.2 for the game in Example 4.2 . Strategic risk aversion alleviates free riding entirely after a given threshold (i.e., δ → 0 \delta\rightarrow 0 ) as our theory predicts.

[45] p: We first study strategic risk aversion in simple, structured classes of collaborative games which are more tractable to analyze than complex MARL problems we design algorithms for. We prove two “free-lunch” theorems that illustrate how strategic risk aversion can (1) increase collaboration and (2) mitigate free riding—both of which are essential to the task of partner generalization. These results serve as a principled rationale for incorporating strategic risk aversion into MARL. We empirically observe both these properties across our experiments in Section 6 , validating that our insights extend beyond structured games.

[46] h3: 4.1 Strategic Risk Aversion can Induce Collaboration

[47] p: Our first setting lies in continuous ( 𝒜 = ℝ n \mathcal{A}=\mathbb{R}^{n} ) quadratic aggregative games, popular in economics ( Corchón, 1994 ) and control theory ( Paccagnan et al., 2018 ) . In line with our collaborative setting, we write the utility of each player as the difference between a shared reward that depends on the aggregate action a 1 + … + a N a_{1}+\ldots+a_{N} , so that

[48] table: R ⁡ ( a 1 , … , a N ) = 1 2 ​ ⟨ ∑ i = 1 N a i , H ​ ∑ i = 1 N a i ⟩ + ⟨ h , ∑ i = 1 N a i ⟩ , R(a_{1},\ldots,a_{N})=\frac{1}{2}\left\langle\sum_{i=1}^{N}a_{i},H\sum_{i=1}^{N}a_{i}\right\rangle+\left\langle h,\sum_{i=1}^{N}a_{i}\right\rangle,

[49] p: for some H H negative definite and h h of appropriate dimensions, and a private cost that only depends on the player’s own action a i a_{i} , of the form c i ​ ( a i ) = ρ i 2 ​ ‖ a i ‖ 2 c_{i}(a_{i})=\frac{\rho_{i}}{2}\norm{a_i}^{2} for ρ i > 0 \rho_{i}>0 . For simplicity of exposition, we assume here that all players have the same degree of risk aversion τ i \tau_{i} and bounded rationality ϵ i \epsilon_{i} , and the same ρ i \rho_{i} . Nevertheless, as we show in the Appendix B.1 , all results extend to the case where these are player-dependent.

[50] p: Being a continuous game, the computation of an RQE is infinite dimensional, as it involves searching over mixed strategies over continuous action spaces. In Section B.1.1 in the appendix, however, we bypass this complexity by showing that there is a unique Gaussian RQE (i.e., RQE where mixed strategies are Gaussian) that can be computed efficiently. This effectively allows us to study the effect of risk aversion on the expected shared reward J ⁡ ( τ ) ≔ 𝔼 a i ∼ x i ⋆ ​ ( τ ) ​ [ R ⁡ ( a 1 , … , a N ) ] . J(\tau)\coloneqq\mathbb{E}_{a_{i}\sim x_{i}^{\star}(\tau)}\left[R(a_{1},\ldots,a_{N})\right].

[51] p: Remarkably, as we show in the next theorem (proven in Appendix B.1 ), this function is strictly increasing. That is, risk monotonically increases the shared reward and thus induces collaboration between the players.

[52] p: [risk induces collaboration] Let x i ⋆ ​ ( τ ) x_{i}^{\star}(\tau) be the Gaussian mixed strategy of player i i at the unique Gaussian RQE of the game, as a function of the degree of risk aversion τ \tau . Then, the expected shared reward τ ↦ J ⁡ ( τ ) \tau\mapsto J(\tau) is strictly increasing 1 1 1 The function is strictly increasing on the domain of τ \tau where RQE are well-defined, that is, when the risk parameters τ \tau is “not too large”; else, risk diverges to infinity. For details, we refer the reader to the appendix and, in particular, to ( 14 ). . That is, players contribute more to the shared reward as they become more risk-averse. This increasing contribution to the shared reward generally entails an increase in the players’ private cost. Thus, in practice, we observe a tradeoff between being risk neutral ( τ → 0 \tau\to 0 ) and more risk-averse ( τ \tau large) with large personal cost but large shared reward. In a one-dimensional example, we can study this tradeoff analytically.

[53] h6: Example \thetheorem .

[54] p: Consider two robots that move an object from the origin to a target location a ¯ \bar{a} . Each robot exerts a force a i a_{i} , so that the total force is a 1 + a 2 a_{1}+a_{2} . Players incur a penalty for their own actuation effort. Thus, the shared reward is − 1 2 ​ ( a 1 + a 2 − a ¯ ) 2 -\frac{1}{2}(a_{1}+a_{2}-\bar{a})^{2} and the personal cost is 1 2 ​ a i 2 \frac{1}{2}a_{i}^{2} (with ρ i = 1 \rho_{i}=1 for simplicity). In this case, the Gaussian RQE has mean m i ⋆ ​ ( τ ) = a ¯ 3 − τ ​ ϵ m_{i}^{\star}(\tau)=\frac{\bar{a}}{3-\tau\epsilon} and variance Σ i = ϵ 2 \Sigma_{i}=\frac{\epsilon}{2} . The equilibrium expected reward is concave in τ \tau as shown in Fig. 1 , highlighting that risk aversion can yield higher utilities.

[55] h6: Remark \thetheorem .

[56] p: We refer to Theorem 4.1 as a “free-lunch" theorem because it suggests that one can add risk aversion into a game and not incur a loss in performance. This can be observed in Fig. 1 (i) in which equilibrium utility increases from a risk-neutral baseline before decreasing again. This is in stark contrast to single-agent RL or classic robust optimization where robustness necessitates sacrificing performance.

[57] p: We validate our theory in broader classes of games in Section 6 and observe that, in some games, some degree of strategic risk aversion can increase collaboration and performance over a risk-neutral baseline. In other games, however, the structure is less amenable to such phenomena, and we observe that risk aversion introduces conservatism and a corresponding decrease in performance.

[58] h3: 4.2 Strategic Risk Aversion Alleviates Free-riding

[59] p: We now prove a second “free-lunch” theorem associated with strategic risk aversion in collaborative games, namely that players who are strategically risk-averse will free-ride less at equilibrium. We prove this result in the context of 2-player collaborative finite symmetric games played over the probability simplex. These are games in which player i = 1 , 2 i=1,2 ’s utility is given by

[60] table: U i ​ ( x 1 , x 2 ) \displaystyle U_{i}(x_{1},x_{2}) = 𝔼 a 1 ∼ x 1 , a 2 ∼ x 2 ​ [ R ⁡ ( a 1 , a 2 ) ] − 𝔼 a i ∼ x i ​ [ c ⁡ ( a i ) ] , \displaystyle=\mathbb{E}_{\begin{subarray}{c}a_{1}\sim x_{1},a_{2}\sim x_{2}\end{subarray}}[R(a_{1},a_{2})]-\mathbb{E}_{a_{i}\sim x_{i}}[c(a_{i})],

[61] p: where R R is a symmetric ( R ⁡ ( a 1 , a 2 ) = R ⁡ ( a 2 , a 1 ) R(a_{1},a_{2})=R(a_{2},a_{1}) ) shared reward, c c is a private cost, and x i x_{i} are strategy vectors in the probability simplex in ℝ n \mathbb{R}^{n} . Although the game is symmetric, equilibria can be asymmetric and thus exhibit free-riding —i.e., one player can exert significantly less effort at equilibrium while still enjoying high utility. As we observe across our experiments, free-riding equilibria are ubiquitous across many MARL benchmarks and pose a significant challenge to the generalization of agents’ strategies. Concretely, we define free riding in our game as follows. {definition} [free-riding] An RQE ( x 1 , x 2 ) ∈ Δ ⁡ ( 𝒜 ) × Δ ⁡ ( 𝒜 ) (x_{1},x_{2})\in\Delta(\mathcal{A})\times\Delta(\mathcal{A}) exhibits free-riding with degree δ ≥ 0 \delta\geq 0 if the difference in costs paid by each player at the RQE is δ \delta ; i.e., | 𝔼 a 1 ∼ x 1 ​ [ c ⁡ ( a 1 ) ] − 𝔼 a 2 ∼ x 2 ​ [ c ⁡ ( a 2 ) ] | = δ |\mathbb{E}_{a_{1}\sim x_{1}}[c(a_{1})]-\mathbb{E}_{a_{2}\sim x_{2}}[c(a_{2})]|=\delta . If δ = 0 \delta=0 , the RQE does not exhibit free-riding.

[62] p: The following theorem shows that as a player’s degree of risk aversion increases, free-riding becomes less prevalent.

[63] p: [risk removes free-riding] There exists a game-dependent constant C C depending only on R R , c c , and the degree of bounded rationality ϵ \epsilon such that if player’s degrees of risk aversion τ \tau in a two-player collaborative game satisfy τ > C δ 2 \tau>\frac{C}{\delta^{2}} , then the game can admit no RQE with degree of free-riding greater than δ \delta .

[64] p: This theorem (proven in Appendix B.2 ) shows that as strategic risk aversion increases, RQE must exhibit less free-riding. The intuition for this result is as follows: suppose that player i i free-rides at a RQE. If they become risk-averse, the worst-case deviation for their opponent is simply to stop putting any effort into the game. Since player i i is free-riding and not putting their own effort, this deviation causes a large drop in performance. Thus, at a risk-averse equilibrium, a player must contribute some of their own effort. We validate this intuition in a simple coordination game.

[65] h6: Example \thetheorem .

[66] p: Consider the game with 𝒜 = { C = collaborate , D = defect } \mathcal{A}=\{\text{C}=\text{collaborate},\text{D}=\text{defect}\} , R ⁡ ( a 1 , a 2 ) = 1 R(a_{1},a_{2})=1 if a 1 = C a_{1}=\text{C} or a 2 = C a_{2}=\text{C} (at least one player collaborates) and R ⁡ ( a 1 , a 2 ) = 0 R(a_{1},a_{2})=0 if a 1 = a 2 = D a_{1}=a_{2}=\text{D} (both defect), and c ⁡ ( a i ) = 0.4 c(a_{i})=0.4 if a i = C a_{i}=\text{C} (cost of collaboration) and c ⁡ ( a i ) = 0.0 c(a_{i})=0.0 otherwise. We fix ϵ = 0.2 \epsilon=0.2 and study the effect of the degree of risk aversion on the game in Fig. 1 . Without risk aversion, the game has one symmetric and two free-riding RQE. As the degree of risk aversion increases, players become increasingly collaborative and the degree of free-riding diminishes. Importantly, there is a threshold where the two free-riding RQEs disappear and “merge” into the symmetric one—a phenomenon known as pitchfork bifurcation.

[67] p: We validate this theorem through our experiments in both the Overcooked gridworld and the Tag environment. In both environments, we empirically observe that Nash agents naturally learn to free-ride at equilibrium which in turn severely degrades their ability to generalize to new agents. Our strategic risk-averse agents however tend to put more effort into the task and thus generalize better to new agents.

[68] h6: Remark \thetheorem .

[69] p: In our ablation studies on the effects of risk aversion, we empirically observe a threshold-like phenomenon under which free riding disappears as risk aversion increases past a certain threshold. This seems to validate that the implications of Section 4.2 hold beyond the simple classes of games covered by the theorem.

[70] h2: 5 MARL Algorithm Design

[71] p: The theoretical benefits of strategic risk aversion—increased collaboration and no free-riding—prompt us to design scalable strategically risk-averse training algorithms for MARL. We do so in the general setting of policy optimization algorithms. For a more detailed mathematical background of risk aversion in MARL, we refer to Appendix C .

[72] h3: 5.1 Meta-algorithm for Strategically Risk-averse Policy Optimization

[73] p: In standard policy optimization, each agent seeks a policy π θ i \pi_{\theta_{i}} , parametrized by parameters θ i \theta_{i} , that maximizes an objective function ℒ i ​ ( θ i , θ − i ) \mathcal{L}_{i}(\theta_{i},\theta_{-i}) , which is a function of the policies of all agents. Inspired by our strategically risk-averse utility ( 1 ), it is tempting to replace this objective function with

[74] table: inf ϕ i ℒ i ( θ i , ϕ i ) + 1 τ i KL ( ϕ i , θ − i ) − ϵ i H ( θ i ) , \inf_{\phi_{i}}\mathcal{L}_{i}(\theta_{i},\phi_{i})+\frac{1}{\tau_{i}}\KL(\phi_{i},\theta_{-i})-\epsilon_{i}H(\theta_{i}), (4)

[75] p: where, to ease exposition, we slightly overload the notation of KL ( ϕ i , θ − i ) \KL(\phi_{i},\theta_{-i}) to be the (expected) KL-divergence between the induced policies across states (if the problem is one of MARL) . Unfortunately, the computation of this objective poses a significant computational challenge. The mere evaluation of this objective, as well as the computation of its gradient, requires solving a high-dimensional non-convex optimization problem—the infimum over ϕ i \phi_{i} —and is therefore computationally prohibitive.

[76] p: To bypass this complexity, we follow Mazumdar et al. (2024) and resort to an auxiliary game in which we augment the number of players. For each agent i i , we replace the infimum in ( 4 ) by an adversary that aims to inflict maximum damage to agent i i , while not deviating too much from the other agents’ policies, and is thus designed to solve the infimum in ( 4 ). As such, the objective of agent i i is now a function of their parameters θ i \theta_{i} and those of their adversary:

[77] table: ℒ i ( θ i , ϕ i ) + 1 τ i KL ( ϕ i , θ − i ) − ϵ i H ( θ i ) , \mathcal{L}_{i}(\theta_{i},\phi_{i})+\frac{1}{\tau_{i}}\KL(\phi_{i},\theta_{-i})-\epsilon_{i}H(\theta_{i}), (5)

[78] p: where the KL term can now be dropped as it does not affect the agent’s parameters. The objective of the adversary agent, who controls the adversarial policy π ϕ i \pi_{\phi_{i}} and whose goal is to minimize the objective of agent i i , depends on the parameters of all agents and is therefore given by

[79] table: − ℒ i ( θ i , ϕ i ) − 1 τ i KL ( ϕ i , θ − i ) + ϵ i H ( θ i ) , -\mathcal{L}_{i}(\theta_{i},\phi_{i})-\frac{1}{\tau_{i}}\KL(\phi_{i},\theta_{-i})+\epsilon_{i}H(\theta_{i}), (6)

[80] p: where the entropy term can be dropped. While adversarial training has been proposed as a robustness technique, such methods are often unstable to train and result in over-conservative policies ( Bukharin et al., 2023 ; Lauffer et al., 2025 ) . The key insight resulting from strategic risk aversion is the idea to constrain the adversary to not deviate from the opponents policy (which is also evolving during training). This extra step stabilizes training.

[81] p: This framing provides us with a meta-algorithm for strategically risk-averse MARL. We now instantiate this algorithm in the case of PPO, also called independent PPO (IPPO) when deployed in multi-agent settings ( Yu et al., 2022 ) , and introduce Strategically Risk-averse Policy Optimization (SRPO), the first strategically risk-averse algorithm for MARL.

[82] h3: 5.2 SRPO

[83] p: When using PPO ( Schulman et al., 2017 ) , the objective of agent i i is given by

[84] table: ℒ i IPPO ​ ( θ i , θ − i ) = ℒ i CLIP ​ ( θ i , θ − i ) − ϵ i ​ H ​ ( θ i ) ​ ( o i t ) , \displaystyle\mathcal{L}_{i}^{\mathrm{IPPO}}(\theta_{i},\theta_{-i})=\mathcal{L}_{i}^{\mathrm{CLIP}}(\theta_{i},\theta_{-i})-\epsilon_{i}H(\theta_{i})(o_{i}^{t}), (7)

[85] p: where the clipped surrogate objective is

[86] table: ℒ i CLIP ​ ( θ i , θ − i ) = \displaystyle\mathcal{L}_{i}^{\mathrm{CLIP}}(\theta_{i},\theta_{-i})= 𝔼 t [ min ( r i t ( θ i ) A ^ i t ( θ i , θ − i ) , \displaystyle\mathbb{E}_{t}\Big[\min\Big(r_{i}^{t}(\theta_{i})\hat{A}_{i}^{t}(\theta_{i},\theta_{-i}), clip ( r i t ( θ i ) , 1 − δ , 1 + δ ) A ^ i t ( θ i , θ − i ) ) ] , \displaystyle\text{clip}(r_{i}^{t}(\theta_{i}),1-\delta,1+\delta)\hat{A}_{i}^{t}(\theta_{i},\theta_{-i})\Big)\Big],

[87] p: with r i t ​ ( θ i ) = π θ i ​ ( a i t | o i t ) π θ i , old ​ ( a i t | o i t ) r_{i}^{t}(\theta_{i})=\frac{\pi_{\theta_{i}}(a_{i}^{t}|o_{i}^{t})}{\pi_{\theta_{i,\text{old}}}(a_{i}^{t}|o_{i}^{t})} being the importance sampling ratio, A ^ i t ​ ( θ i , θ − i ) \hat{A}_{i}^{t}(\theta_{i},\theta_{-i}) the estimated advantage at time t t (and depends on θ − i \theta_{-i} as it is computed using samples of the policies of all agents), ϵ i ​ H ​ ( θ i ) ​ ( o i t ) \epsilon_{i}H(\theta_{i})(o_{i}^{t}) a (negative) entropy regularizer, and o i t o_{i}^{t} the observation of agent i i at time t t .

[88] p: We can now follow the meta-algorithm above to derive strategically risk-averse proximal policy optimization. Specifically, the objective of agent i i is

[89] table: ℒ i SRPO ​ ( θ i , ϕ i ) = ℒ i CLIP ​ ( θ i , ϕ i ) − ϵ i ​ H ​ ( θ i ) ​ ( o i t ) . \mathcal{L}_{i}^{\mathrm{SRPO}}(\theta_{i},\phi_{i})=\mathcal{L}_{i}^{\mathrm{CLIP}}(\theta_{i},\phi_{i})-\epsilon_{i}H(\theta_{i})(o_{i}^{t}). (8)

[90] p: Since the PPO objective already includes entropy regularization, the additional entropy term in ( 5 ) is superfluous. The objective of player i i ’s adversary is then

[91] table: ℒ ¯ i SRPO ( ϕ i , ( θ i , θ − i ) ) = − ℒ i CLIP ( θ i , ϕ i ) − 1 τ i KL ( ϕ i , θ − i ) . \bar{\mathcal{L}}_{i}^{\mathrm{SRPO}}(\phi_{i},(\theta_{i},\theta_{-i}))=-\mathcal{L}_{i}^{\mathrm{CLIP}}(\theta_{i},\phi_{i})-\frac{1}{\tau_{i}}\KL(\phi_{i},\theta_{-i}). (9)

[92] p: Overall, SRPO consists of running gradient descent on these objectives. We present pseudocode and details in Appendix C.2 , and note here that the iteration structure and complexity of SRPO is very similar to that of IPPO.

[93] h2: 6 Experiments

[94] p: We evaluate the proposed SRPO algorithm against IPPO on three cooperative multi-agent benchmarks and one LLM-based debate task. We use IPPO as our benchmark due to its emerging role as the dominant scalable algorithm for collaborative MARL across numerous benchmarks ( Yu et al., 2022 ; Forkel and Foerster, 2025 ; de Witt et al., 2020 ) . The experimental design closely follows the theoretical motivations developed earlier. Concretely, our experiments test the following claims:

[95] p: Partner generalization. SRPO achieves higher and more stable cross-play performance than IPPO when paired with previously unseen partners.

[96] p: Shared reward and free-riding. In cooperative tasks with private costs, SRPO converges to equilibria with higher shared reward and reduced free-riding behavior.

[97] p: Scalability. SRPO remains practical in complex multi-agent settings when implemented with policy sharing and adversary sampling.

[98] p: We implement SRPO and IPPO in four representative environments: (1) a modified grid-world inspired by Overcooked AI ( Carroll et al., 2019 ) , which allows explicit modeling of both shared team rewards and private costs; (2) Tag ( Lowe et al., 2017 ) , a continuous-control coordination task; (3) 4-player Hanabi ( Bard et al., 2020 ) with 3 colors and 3 ranks, a partially observed cooperative game requiring implicit coordination and communication used to study zero-shot coordination ( Forkel and Foerster, 2025 ) , and (4) an LLM-based multi-agent debate setting ( Du et al., 2024 ; Park et al., 2025 ) on the GSM8K dataset ( Cobbe et al., 2021 ) in which agents must collaborate to solve math problems.

[99] h5: Training and evaluation.

[100] p: Across all environments, for an apples-to-apples comparison, the number of interactions with the environment for both SRPO and IPPO are kept the same. We evaluate partner generalization using cross-play performance , where a trained agent is paired with held-out partners not encountered during training. This evaluation makes the existence of free-riding-type policies extremely apparent: the policies lead to a distinct checker-board pattern, which emerges when free-riding agents are paired with one another and fail to achieve good performance. We consistently observe this phenomenon arising from IPPO-trained agents across environments.

[101] h5: Ablation studies.

[102] p: Across environments, we also report results of ablation studies on both entropy and strategic risk aversion to further validate our theory, show how our results are robust to hyper-parameter selection, and highlight how entropy alone cannot guarantee generalization in general collaborative games despite positive empirical evidence in special cases ( Forkel and Foerster, 2025 ) . The code will be released upon publication, and the detailed setup is in Appendix D .

[103] figure: Figure 2 : Cross-play and ablation experiments in the overcooked environment. Each square represents the average reward across 10 episodes of length 128 for each pair of agents. Diagonal blocks represent the training performance of the agents. (i) We directly observe that IPPO ( ϵ = 0.1 \epsilon=0.1 ) learns to free-ride while SRPO ( OPEN τ = 10 , ϵ = 0.1 ) \tau=10,\epsilon=0.1) does not. Furthermore, mirroring Section 4.1 , we observe that SRPO yields higher utility strategies (i.e., risk improves performance). (ii) Results of an ablation experiment, varying τ \tau while holding ϵ = 0.1 \epsilon=0.1 . We empirically observe that free-riding completely disappears as risk aversion increases, mirroring the result in Section 4.2 . (iii) Difference between Training Performance (TP) and Cross-play Performance (CP) (mean and standard deviation): the performance of IPPO drastically decreases, with lower average and larger standard deviation in cross-play, while the performance of SRPO is unaffected.

[104] h3: 6.1 Overcooked Gridworld

[105] p: We construct an environment based onOvercooked Ruhdorfer et al. (2025) multi-agent benchmark to serve as a simple laboratory to verify our theory. In our Overcooked Gridworld, agents receive a shared team reward when an onion is picked up ( + 1 +1 ) and placed into a pot ( + 10 +10 ), while each agent incurs private costs for movement ( − 0.2 -0.2 ) and collision ( − 2 -2 ). This induces a canonical social dilemma: although the team objective is collaborative, each agent has an incentive to avoid costly effort and rely on the teammate to complete the task. Results are shown in Fig. 2 .

[106] h5: SRPO reduces free-riding and exhibits higher performance.

[107] p: Empirically, IPPO always converges to a free-riding equilibrium where one teammate avoids movement but collects high reward due to the effort of their partner—evident in the characteristic checkerboard pattern observed in the top left block of Fig. 2 (i). In contrast, SRPO learns a policy in which both agents coordinate and contribute to the task. This behavior matches SRPO’s objective: because training explicitly optimizes performance against plausible adversarial partner deviations ( Section 5 ), non-contribution becomes risky. As we summarize in Fig. 2 (iii), SRPO thus attains both higher performances and improved cross-play reliability, consistent with our theoretical predictions.

[108] h5: Ablation study of the degree of strategic risk aversion τ \tau .

[109] p: As shown in Fig. 2 (ii), small values of τ \tau and IPPO ( τ = 0 \tau=0 ) lead to free-riding and thus poor cross-play performance, reflecting reliance on fragile conventions and lack of effort on the part of agents. As τ \tau increases, collaboration becomes more stable: policies converge to a consistent solution, free-riding disappears, and cross-play performance improves, validating that Theorem 4.2 holds more broadly. We also observe that SRPO is robust to choices of τ \tau . Ablations show consistent gains over IPPO across orders of magnitude of τ \tau . We make similar observations in ablation experiments in the Tag environment presented in Appendix D.6 .

[110] h3: 6.2 Tag

[111] p: In Tag, two chasers must coordinate to catch a runner. The chasers get a shared positive reward (+1) if a chaser collides with a runner. We first train runner policies independently via adversarial training, and then train chaser policies using either IPPO or SRPO against a fixed runner to keep the game collaborative. Cross-play performance is evaluated along two axes: (i) pairing trained chasers with an unseen chaser partner (teammate shift), and (ii) evaluating chasers against a runner policy not observed during training (opponent shift). The results are shown in Fig. 3 .

[112] figure: Figure 3 : Cross-play performances of SRPO ( τ = 10 , ϵ = 0.01 \tau=10,\epsilon=0.01 ) and IPPO ( ϵ = 0.01 \epsilon=0.01 ) agents in the Tag environment against a runner seen during training (i) and an unseen runner (ii). Each square represents the average reward of two agents across 100 runs of length 100. IPPO does well in training environments (yet still clearly learns free-riding like policies), but their performance degrades drastically against an unseen runner. SRPO has slightly lower training performance but clearly learns a more generalizable policy. (iii) Difference between Training Performance (TP) and Cross-play Performance (CP) (mean and standard deviation): the performance of IPPO drastically decreases, with lower average and larger standard deviation in cross-play, while the performance of SRPO is almost unaffected.

[113] h5: SRPO learns more generalizable policies.

[114] p: We empirically observe that in this standard benchmark environment, IPPO-trained agents can learn high performing policies. However, we also observe that these policies often encode free-riding and can overfit to both the runner encountered during training and specific coordination conventions it develops with its training partner. While this can produce strong in-distribution performance (i.e., on the diagonal), it degrades sharply under either teammate or runner shifts, as seen in the sharp drops in performance as IPPO agents are played against each other, as we summarize in Fig. 3 (iii).

[115] p: In contrast, SRPO has slightly worse performance in the training environment. This highlights that in some environments incorporating strategic risk aversion may sometimes require tradeoffs with performance. In the case of Tag, we can trace this back to the lack of the aggregative structure required for Section 4.1 . Nevertheless, SRPO attains consistently higher and more stable cross-play performance across both other partners (including free-riding IPPO agents) and runners, showing their potential to generalize more widely.

[116] h3: 6.3 Hanabi

[117] p: Hanabi is a collaborative card game in which players must play cards in the correct sequence, with the twist that you can see everyone’s cards except your own. It is a canonical benchmark for collaboration in MARL ( Bard et al., 2020 ) . Following Lauffer et al. (2025) , we consider a simplified game with 3 3 colors and 3 3 ranks. In this setting, agents may develop private communication protocols during training that fail to generalize to unseen teammates. We focus here on the 4-player variant to demonstrate the scalability of SRPO with the number of players, and present results on 2-player games in Appendix D .

[118] figure: (a) (b) Figure 4 : Cross-play performance of SRPO and IPPO agents in the Hanabi environment. We use policy sharing to validate the scalability of SRPO. During evaluation, we let agents 1 and 2 share a policy and agents 3 and 4 share a policy, enabling pairwise cross-play evaluation. In Fig. 4(a) , each square represents the average reward of the two agent groups across 100 runs, each of length 100. Fig. 4(b) shows the differences between training performance (TP) and cross-play performance (CP) (mean and standard deviation) for both IPPO and SRPO. SRPO remains more robust when paired with an unseen partner. Here, we set the entropy coefficient to be ϵ = 0.001 \epsilon=0.001 for both IPPO and SRPO, and τ = 0.01 \tau=0.01 for SRPO.

[119] h5: Scalability of SRPO.

[120] p: To scale SRPO to larger numbers of agents we make use of policy sharing—i.e., we share a single risk-averse policy across agents and maintain only one adversary policy, randomly assigning the adversarial role during training. The results are shown in Fig. 4 . where we observe that SRPO exhibits more stable cross-play performance than IPPO.

[121] h3: 6.4 Multi-LLM-Agent Debate on GSM8K

[122] p: To conclude, we present a proof-of-concept on using SRPO in a language-based cooperative reasoning setting in which agents must collaborate to solve grade school math word problems ( Cobbe et al., 2021 ) through structured debate.

[123] p: In this setup, two agents engage in a three-round iterative debate protocol. In the first round, each agent independently observes the question and produces its own reasoning and answer. In subsequent rounds, each agent observes the original question as well as both agents’ outputs from the previous round, and then refines its response. Successfully solving a problem therefore requires more than producing a correct answer in isolation: each agent must reinforce correct reasoning while remaining robust to potentially misleading or incorrect proposals from its teammate. This naturally induces a cooperative yet adversarial interaction, where robustness to the partner’s policy plays a critical role in achieving reliable joint performance.

[124] p: Both IPPO (the existing state-of-the-art) and SRPO agents are trained using multiple base language models, including Qwen2.5-0.5B-Instruct (Q0.5B) and Qwen2.5-3B-Instruct (Q3B) ( Bai et al., 2025 ) , as well as Qwen3-0.6B (Q0.6B) and Qwen3-4B-Instruct-2507 (Q4B) ( Yang et al., 2025 ) , using the verl training framework ( Sheng et al., 2024 ) . Here, we set the entropy coefficient to be ϵ = 0 \epsilon=0 for both IPPO and SRPO, and τ = 10 \tau=10 for SRPO.

[125] p: We evaluate performance along two complementary robustness dimensions. First, we measure cross-play performance between agents trained with the same method but using different model scales. Performance is quantified using joint accuracy , where a problem is counted as correct only if both agents produce the correct final answer. This metric directly reflects the ability of agents to coordinate reliably under policy heterogeneity. Second, we evaluate robustness to drastic partner shifts by pairing a trained Qwen agent with an untuned Llama 3.2-1B-Instruct model ( Grattafiori et al., 2024 ) . In this setting, we measure the accuracy of the trained agent alone, isolating its ability to maintain correct reasoning despite interacting with a potentially unreliable partner. Results are summarized in Tables 1 and 2 .

[126] figure: Table 1: Cross-play performance (joint accuracy) across model scale combinations. Percentage improvement is computed relative to IPPO. Across all model combinations, SRPO consistently outperforms IPPO in terms of cross-play performance. Method Q0.5B&Q0.6B Q0.5B&Q3B Q0.5B&Q4B Q0.6B&Q3B Q0.6B&Q4B Q3B&Q4B SRPO 0.622 0.686 0.873 0.616 0.848 0.732 IPPO 0.605 0.651 0.846 0.573 0.711 0.709 Improvement (%) +2.81% +5.38% +3.19% +7.50% +19.27% +3.24%

[127] figure: Table 2: Performance (the accuracy of the trained agent itself) when paired with an untuned Llama 3.2-1B-Instruct model. Percentage improvement is computed relative to IPPO. Across all model sizes, SRPO agents consistently outperform IPPO, indicating that SRPO endows the trained the power to be robust to the teammate. Method Q0.5B Q0.6B Q3B Q4B SRPO 0.405 0.671 0.632 0.917 IPPO 0.378 0.587 0.552 0.901 Improvement (%) +7.14% +14.31% +14.49% +1.78%

[128] h5: SRPO extends to LLM-based multi-agent systems.

[129] p: As shown in Table 1 , SRPO consistently improves joint accuracy over IPPO across all cross-play combinations, with gains of up to 19.27 % 19.27\% . This demonstrates that SRPO enhances coordination robustness across heterogeneous policies, enabling agents to reliably reach correct joint outcomes. Furthermore, as shown in Table 2 , SRPO substantially improves individual accuracy when paired with an untuned partner, achieving gains of up to 14.49 % 14.49\% . This indicates that SRPO-trained agents are significantly more robust to severe partner mismatch, maintaining correct reasoning even when interacting with unreliable teammates. Together, these results highlight SRPO’s effectiveness in promoting robust cooperative reasoning in multi-agent language environments. In Section D.5 , we provide evidence that SRPO primarily improves collaboration, rather than the individual reasoning ability of each agent.

[130] h2: 7 Conclusion

[131] p: In this work, we introduce strategic risk aversion as a principled inductive bias for learning collaborative policies that generalize to unseen partners. Using the risk-averse quantal response equilibrium (RQE) framework, we show that strategic risk aversion can both increase contributions to shared rewards and eliminate free-riding at equilibrium, demonstrating that robustness need not be purely conservative. Guided by these insights, we propose Strategically Risk-Averse Policy Optimization (SRPO), a scalable modification of standard policy optimization. Across cooperative benchmarks (Overcooked, Tag, Hanabi) and an LLM-based debate task on GSM8K, SRPO yields improved robustness to heterogeneous or unreliable teammates, including across model scales. Future work includes extending strategic risk aversion to broader agentic AI settings such as human–AI collaboration and multi-agent foundation model systems.

[132] h2: References

[133] h2: Appendix A Further Discussion on Related Work

[134] p: In this section, we discuss a broader set of related work to better position our work in the landscape of collaborative multi-agent learning and risk-averse/robust MARL.

[135] h5: Collaborative MARL and Partner Generalization

[136] p: Research into solving collaborative decision-making problems using MARL has a long history ( Cao et al., 2013 ) , originating from a desire for solving decentralized decision-making problems ( Tsitsiklis, 1984 ) . Far from fading, these issues remain at the fore of research interest with the advent of powerful AI systems and a desire to build large teams of AI agents ( Tran et al., 2025 ) for solving collaborative tasks. Emerging from this literature, is a general consensus that classic single-agent policy optimization algorithms like PPO ( Schulman et al., 2017 ) , used in a decentralized way, can yield state-of-the-art or near state-of-the-art performance without needing to be overly specialized to the multi-agent nature of the problem ( Yu et al., 2022 ; de Witt et al., 2020 ; Forkel and Foerster, 2025 ) . Despite such results, learned policies resulting from such approaches can fail to generalize to unseen agents ( Forkel and Foerster, 2025 ) and new environments. We validate this through our experiments and further observe that these state-of-the-art algorithms are consistently prone to learning free-riding strategies.

[137] p: Beyond the lines of work mentioned in Section 2 , other important lines of work on addressing the partner generalization problem seek to avoid brittle coordination conventions by learning symmetry-invariant or partner-agnostic policies ( Hu et al., 2020 ; Treutlein et al., 2021 ; Muglich et al., 2022 ) . These often require strong structural assumptions and may not scale to complex collaborative environments. Another set of approaches attempt to achieve robustness by training against partner policies derived from human data ( Carroll et al., 2019 ; Meta Fundamental AI Research Diplomacy Team (FAIR)† et al., 2022 ; Liang et al., 2024 ) , but their effectiveness is constrained by data availability and coverage. Neither of these approaches are fully agnostic to the structure of the underlying problem and are thus not general principles that can be broadly applied across different tasks.

[138] p: Consequently, it remains unclear how to systematically achieve partner generalization without relying on human data or ad-hoc constructions. In this paper we showed that strategic risk aversion gives us one potential approach. Furthermore, we show that it can readily be combined with policy optimization algorithms like PPO, resulting in scalable and performant algorithms for learning generalizable policies.

[139] h5: Robustness and Risk Aversion in MARL

[140] p: A second related line of work is the emerging literature on robust and risk-averse MARL ( Zhang et al., 2020 ; Shi et al., 2024 ; Yekkehkhany et al., 2020 ; Slumbers et al., 2023 ; Qiu et al., 2021 ) . While most of the papers study robustness or risk aversion to changes in the underlying environment ( Eriksson et al., 2022 ; Ganesh et al., 2019 ; Qiu et al., 2021 ; Shen et al., 2023 ; Shi et al., 2024 ; Zhang et al., 2020 ) or to tail risks in large populations of agents ( Yekkehkhany et al., 2020 ) , in this work we study strategic risk aversion. Strategic risk aversion and robustness yield solutions that are more amenable to computation than classic game-theoretic solution concepts ( Mazumdar et al., 2024 ) , ensure robustness to unseen behaviors of the other agents, and sometimes even induce a coordination effect between the agents ( Lanzetti et al., 2025b ) —an empirical observation that we make rigorous in Section 4 . Despite the prior work in this area, the broader benefits of the concept in collaborative games are unknown. This is the problem that we study in this paper.

[141] h2: Appendix B Proofs for Section 4

[142] p: In this section, we provide the proofs of our two main theorems, Section 4.1 and Section 4.2 , as well as the derivation of Section 4.1 used in Fig. 1 .

[143] h3: B.1 Proof of Section 4.1

[144] p: We begin with the proof of Section 4.1 . We first show that there exists a RQE in the space of Gaussian strategies in the aggregative games studied in this section. We then provide the proof of a more general version of Section 4.1 .

[145] h4: B.1.1 Preliminaries

[146] p: Before proving Section B.1.1 , we study RQE for quadratic games. We start with the risk-averse quantal best response. We conduct our analysis in slightly more general settings where the players’ utilities are

[147] table: u i ​ ( a i , a − i ) = 1 2 ​ ⟨ [ a i a − i ] , [ H i , i H i , − i H − i , i H − i , − i ] ​ [ a i a − i ] ⟩ + ⟨ [ h i h − i ] , [ a i a − i ] ⟩ , u_{i}(a_{i},a_{-i})=\frac{1}{2}\left\langle\begin{bmatrix}a_{i}\\ a_{-i}\end{bmatrix},\begin{bmatrix}H_{i,i}&H_{i,-i}\\ H_{-i,i}&H_{-i,-i}\end{bmatrix}\begin{bmatrix}a_{i}\\ a_{-i}\end{bmatrix}\right\rangle+\left\langle\begin{bmatrix}h_{i}\\ h_{-i}\end{bmatrix},\begin{bmatrix}a_{i}\\ a_{-i}\end{bmatrix}\right\rangle, (10)

[148] p: where the matrix

[149] table: [ H i , i H i , − i H − i , i H − i , − i ] \begin{bmatrix}H_{i,i}&H_{i,-i}\\ H_{-i,i}&H_{-i,-i}\end{bmatrix}

[150] p: is assumed to be symmetric negative semidefinite, and H i , i H_{i,i} is assumed to be symmetric negative definite for all i i . Throughout this section, with slight abuse of notation, we denote by x − i x_{-i} the product measure of the mixed strategies of all players except i i .

[151] h6: Lemma \thetheorem (risk-averse quantal best response) .

[152] p: Let x − i x_{-i} be Gaussian with mean m − i m_{-i} and covariance matrix Σ − i ≻ 0 \Sigma_{-i}\succ 0 . Then, the risk-averse quantal best response, defined as the maximizer of U i τ i , ϵ i ​ ( x i , x − i ) U_{i}^{\tau_{i},\epsilon_{i}}(x_{i},x_{-i}) , is uniquely given by a Gaussian mixed strategy with the following covariance matrix and mean:

[153] table: Σ i \displaystyle\Sigma_{i} = − ε i ​ H i , i − 1 \displaystyle=-\varepsilon_{i}H_{i,i}^{-1} m i \displaystyle m_{i} = ( − H i , i + H i , − i ​ P − i − 1 ​ H i , − i ⊤ ) − 1 ​ ( h i + H i , − i ​ P − i − 1 ​ ( 1 τ i ​ Σ − i − 1 ​ m − i − h − i ) ) , \displaystyle=\left(-H_{i,i}+H_{i,-i}P_{-i}^{-1}H_{i,-i}^{\top}\right)^{-1}\left(h_{i}+H_{i,-i}P_{-i}^{-1}\left(\frac{1}{\tau_{i}}\Sigma_{-i}^{-1}m_{-i}-h_{-i}\right)\right),

[154] p: where P − i = 1 τ i ​ Σ − i − 1 + H − i , − i P_{-i}=\frac{1}{\tau_{i}}\Sigma_{-i}^{-1}+H_{-i,-i} , provided that P − i P_{-i} is positive definite. If instead P − i P_{-i} is not positive definite, then risk is infinite.

[155] h6: Proof.

[156] p: To start, recall that the duality representation of the entropic risk measure (e.g., see Föllmer and Schied (2002) ) gives

[157] table: sup p ∈ Δ ⁡ ( ℝ n ⁡ ( N − 1 ) ) 𝔼 a i ∼ x i a − i ∼ x − i [ − u i ( a i , a − i ) ] − 1 τ i KL ( p , x − i ) = 1 τ i log 𝔼 a i ∼ x i a − i ∼ x − i [ exp ( − τ i u i ( a i , a − i ) ) ] . \sup_{p\in\Delta(\mathbb{R}^{n(N-1)})}\mathbb{E}_{\begin{subarray}{c}a_{i}\sim x_{i}\\ a_{-i}\sim x_{-i}\end{subarray}}[-u_{i}(a_{i},a_{-i})]-\frac{1}{\tau_{i}}\KL(p,x_{-i})=\frac{1}{\tau_{i}}\log\mathbb{E}_{\begin{subarray}{c}a_{i}\sim x_{i}\\ a_{-i}\sim x_{-i}\end{subarray}}[\exp\left(-\tau_{i}u_{i}(a_{i},a_{-i})\right)].

[158] p: Thus, we can reformulate the optimization problem for best responses as follows:

[159] table: sup x i ∈ Δ ⁡ ( ℝ n ) \displaystyle\sup_{x_{i}\in\Delta(\mathbb{R}^{n})} U i τ i , ϵ i ​ ( x i , x − i ) \displaystyle U_{i}^{\tau_{i},\epsilon_{i}}(x_{i},x_{-i}) = − inf x i ∈ Δ ⁡ ( ℝ n ) − U i τ i , ϵ i ( x i , x − i ) \displaystyle=-\inf_{x_{i}\in\Delta(\mathbb{R}^{n})}-U_{i}^{\tau_{i},\epsilon_{i}}(x_{i},x_{-i}) = − inf x i ∈ Δ ⁡ ( ℝ n ) sup p ∈ Δ ⁡ ( ℝ n ⁡ ( N − 1 ) ) 𝔼 a i ∼ x i a − i ∼ x − i [ − u i ( a i , a − i ) ] − 1 τ i KL ( p , x − i ) + ϵ i H ( x i ) \displaystyle=-\inf_{x_{i}\in\Delta(\mathbb{R}^{n})}\sup_{p\in\Delta(\mathbb{R}^{n(N-1)})}\mathbb{E}_{\begin{subarray}{c}a_{i}\sim x_{i}\\ a_{-i}\sim x_{-i}\end{subarray}}[-u_{i}(a_{i},a_{-i})]-\frac{1}{\tau_{i}}\KL(p,x_{-i})+\epsilon_{i}H(x_{i}) = − inf x i ∈ Δ ⁡ ( ℝ n ) 1 τ i log 𝔼 a − i ∼ x − i [ exp ( − τ i ( 1 2 ⟨ a − i , H − i , − i a − i ⟩ + 𝔼 a i ∼ x i [ ⟨ a i , H i , − i a − i ⟩ ] + ⟨ h − i , a − i ⟩ ) ) ] \displaystyle=-\inf_{x_{i}\in\Delta(\mathbb{R}^{n})}\frac{1}{\tau_{i}}\log\mathbb{E}_{a_{-i}\sim x_{-i}}\left[\exp\left(-\tau_{i}(\frac{1}{2}\langle a_{-i},H_{-i,-i}a_{-i}\rangle+\mathbb{E}_{a_{i}\sim x_{i}}\left[\langle a_{i},H_{i,-i}a_{-i}\rangle\right]+\langle h_{-i},a_{-i}\rangle)\right)\right] − 𝔼 a i ∼ x i ​ [ 1 2 ​ ⟨ a i , H i , i ​ a i ⟩ + ⟨ h i , a i ⟩ ] + ϵ i ​ H ​ ( x i ) \displaystyle\qquad\qquad\qquad-\mathbb{E}_{a_{i}\sim x_{i}}\left[\frac{1}{2}\langle a_{i},H_{i,i}a_{i}\rangle+\langle h_{i},a_{i}\rangle\right]+\epsilon_{i}H(x_{i}) = sup x i ∈ Δ ⁡ ( ℝ n ) − 1 τ i log 𝔼 a − i ∼ x − i [ exp ( − τ i ( 1 2 ⟨ a − i , H − i , − i a − i ⟩ + 𝔼 a i ∼ x i [ ⟨ a i , H i , − i a − i ⟩ ] + ⟨ h − i , a − i ⟩ ) ) ] \displaystyle=\sup_{x_{i}\in\Delta(\mathbb{R}^{n})}-\frac{1}{\tau_{i}}\log\mathbb{E}_{a_{-i}\sim x_{-i}}\left[\exp\left(-\tau_{i}(\frac{1}{2}\langle a_{-i},H_{-i,-i}a_{-i}\rangle+\mathbb{E}_{a_{i}\sim x_{i}}\left[\langle a_{i},H_{i,-i}a_{-i}\rangle\right]+\langle h_{-i},a_{-i}\rangle)\right)\right] + 𝔼 a i ∼ x i ​ [ 1 2 ​ ⟨ a i , H i , i ​ a i ⟩ + ⟨ h i , a i ⟩ ] − ϵ i ​ H ​ ( x i ) \displaystyle\qquad\qquad\qquad+\mathbb{E}_{a_{i}\sim x_{i}}\left[\frac{1}{2}\langle a_{i},H_{i,i}a_{i}\rangle+\langle h_{i},a_{i}\rangle\right]-\epsilon_{i}H(x_{i}) = sup x i ∈ Δ ⁡ ( ℝ n ) − 1 τ i log 𝔼 a − i ∼ x − i [ exp ( − τ i ( 1 2 ⟨ a − i , H − i , − i a − i ⟩ + ⟨ m i , H i , − i a − i ⟩ + ⟨ h − i , a − i ⟩ ) ) ] \displaystyle=\sup_{x_{i}\in\Delta(\mathbb{R}^{n})}-\frac{1}{\tau_{i}}\log\mathbb{E}_{a_{-i}\sim x_{-i}}\left[\exp\left(-\tau_{i}\left(\frac{1}{2}\langle a_{-i},H_{-i,-i}a_{-i}\rangle+\langle m_{i},H_{i,-i}a_{-i}\rangle+\langle h_{-i},a_{-i}\rangle\right)\right)\right] + 𝔼 a i ∼ x i ​ [ 1 2 ​ ⟨ a i , H i , i ​ a i ⟩ + ⟨ h i , a i ⟩ ] − ϵ i ​ H ​ ( x i ) . \displaystyle\qquad\qquad\qquad+\mathbb{E}_{a_{i}\sim x_{i}}\left[\frac{1}{2}\langle a_{i},H_{i,i}a_{i}\rangle+\langle h_{i},a_{i}\rangle\right]-\epsilon_{i}H(x_{i}).

[160] p: When x − i x_{-i} is Gaussian with mean m − i m_{-i} and variance Σ − i \Sigma_{-i} , the expression simplifies to

[161] table: 𝔼 a − i ∼ x − i \displaystyle\mathbb{E}_{a_{-i}\sim x_{-i}} [ exp ⁡ ( − τ i ​ ( 1 2 ​ ⟨ a − i , H − i , − i ​ a − i ⟩ + ⟨ a i , H i , − i ​ a − i ⟩ + ⟨ h − i , a − i ⟩ ) ) ] \displaystyle\left[\exp\left(-\tau_{i}\left(\frac{1}{2}\langle a_{-i},H_{-i,-i}a_{-i}\rangle+\langle a_{i},H_{i,-i}a_{-i}\rangle+\langle h_{-i},a_{-i}\rangle\right)\right)\right] = 1 ( 2 ​ π ) n ​ det ⁡ ( Σ − i ) ​ ∫ ℝ n exp ⁡ ( − 1 2 ​ ⟨ a − i − m ¯ , Σ ¯ − i − 1 ​ ( a − i − m ¯ ) ⟩ CLOSE \displaystyle=\frac{1}{\sqrt{(2\pi)^{n}\det(\Sigma_{-i})}}\int_{\mathbb{R}^{n}}\exp\left(-\frac{1}{2}\langle a_{-i}-\bar{m},\bar{\Sigma}_{-i}^{-1}(a_{-i}-\bar{m})\rangle\right. OPEN + 1 2 ​ ⟨ m ¯ − i , Σ ¯ − i − 1 ​ m ¯ − i ⟩ − 1 2 ​ ⟨ m − i , Σ − i − 1 ​ m − i ⟩ ) ​ d ​ a − i \displaystyle\quad\qquad\qquad\qquad\qquad\qquad\qquad\left.+\frac{1}{2}\langle\bar{m}_{-i},\bar{\Sigma}_{-i}^{-1}\bar{m}_{-i}\rangle-\frac{1}{2}\langle m_{-i},\Sigma_{-i}^{-1}m_{-i}\rangle\right)\mathrm{d}a_{-i} = ( 2 ​ π ) n ​ det ⁡ ( Σ ¯ − i ) ( 2 ​ π ) n ​ det ⁡ ( Σ − i ) ​ exp ⁡ ( 1 2 ​ ⟨ m ¯ − i , Σ ¯ − i ​ m ¯ − i ⟩ − 1 2 ​ ⟨ m − i , Σ − i ​ m − i ⟩ ) \displaystyle=\sqrt{\frac{(2\pi)^{n}\det(\bar\Sigma_{-i})}{(2\pi)^{n}\det(\Sigma_{-i})}}\exp\left(\frac{1}{2}\langle\bar{m}_{-i},\bar{\Sigma}_{-i}\bar{m}_{-i}\rangle-\frac{1}{2}\langle m_{-i},\Sigma_{-i}m_{-i}\rangle\right) = 1 det ⁡ ( Σ − i ​ Σ ¯ − i − 1 ) ​ exp ⁡ ( 1 2 ​ ⟨ m ¯ − i , Σ ¯ − i − 1 ​ m ¯ − i ⟩ − 1 2 ​ ⟨ m − i , Σ − i − 1 ​ m − i ⟩ ) , \displaystyle=\frac{1}{\sqrt{\det(\Sigma_{-i}\bar\Sigma_{-i}^{-1})}}\exp\left(\frac{1}{2}\langle\bar{m}_{-i},\bar{\Sigma}_{-i}^{-1}\bar{m}_{-i}\rangle-\frac{1}{2}\langle m_{-i},\Sigma_{-i}^{-1}m_{-i}\rangle\right),

[162] p: where Σ ¯ − i − 1 = Σ − i − 1 + τ i ​ H − i , − i = τ i ​ P − i \bar{\Sigma}_{-i}^{-1}=\Sigma_{-i}^{-1}+\tau_{i}H_{-i,-i}=\tau_{i}P_{-i} and m ¯ − i = Σ ¯ ​ ( Σ − i − 1 ​ m − i − τ i ​ ( H i , − i ⊤ ​ m i + h − i ) ) \bar{m}_{-i}=\bar{\Sigma}(\Sigma_{-i}^{-1}m_{-i}-\tau_{i}(H_{i,-i}^{\top}m_{i}+h_{-i})) . Moreover,

[163] table: det ⁡ ( Σ − i ​ Σ ¯ − i − 1 ) = det ⁡ ( I + τ i ​ Σ − i ​ H − i , − i ) . \det(\Sigma_{-i}\bar\Sigma_{-i}^{-1})=\det(I+\tau_i\Sigma_{-i}H_{-i,-i}).

[164] p: Overall, we therefore have

[165] table: log ⁡ 𝔼 a − i ∼ x − i ​ [ exp ⁡ ( − τ i ​ ( 1 2 ​ ⟨ a − i , H − i , − i ​ a − i ⟩ + ⟨ a i , H i , − i ​ a − i ⟩ + ⟨ h − i , a − i ⟩ ) ) ] = − 1 2 ​ log ⁡ det ⁡ ( I + τ i ​ Σ − i ​ H − i , − i ) + 1 2 ​ ⟨ m ¯ − i , Σ ¯ − i − 1 ​ m ¯ − i ⟩ − 1 2 ​ ⟨ m − i , Σ − i − 1 ​ m − i ⟩ . \log\mathbb{E}_{a_{-i}\sim x_{-i}}\left[\exp\left(-\tau_{i}\left(\frac{1}{2}\langle a_{-i},H_{-i,-i}a_{-i}\rangle+\langle a_{i},H_{i,-i}a_{-i}\rangle+\langle h_{-i},a_{-i}\rangle\right)\right)\right]\\ =-\frac{1}{2}\log\det(I+\tau_i\Sigma_{-i}H_{-i,-i})+\frac{1}{2}\langle\bar{m}_{-i},\bar{\Sigma}_{-i}^{-1}\bar{m}_{-i}\rangle-\frac{1}{2}\langle m_{-i},\Sigma_{-i}^{-1}m_{-i}\rangle.

[166] p: We can now plug this expression into the optimization problem for best responses and get

[167] table: sup x i ∈ Δ ⁡ ( ℝ n ) U i τ i , ϵ i ( x i , x − i ) = sup x i ∈ Δ ⁡ ( ℝ n ) \displaystyle\sup_{x_{i}\in\Delta(\mathbb{R}^{n})}U_{i}^{\tau_{i},\epsilon_{i}}(x_{i},x_{-i})=\sup_{x_{i}\in\Delta(\mathbb{R}^{n})} 1 2 ​ τ i ​ log ⁡ det ⁡ ( I + τ i ​ Σ − i ​ H − i , − i ) − 1 2 ​ τ i ​ ⟨ m ¯ − i , Σ ¯ − i − 1 ​ m ¯ − i ⟩ + 1 2 ​ τ i ​ ⟨ m − i , Σ − i − 1 ​ m − i ⟩ \displaystyle\frac{1}{2\tau_{i}}\log\det(I+\tau_i\Sigma_{-i}H_{-i,-i})-\frac{1}{2\tau_{i}}\langle\bar{m}_{-i},\bar{\Sigma}_{-i}^{-1}\bar{m}_{-i}\rangle+\frac{1}{2\tau_{i}}\langle m_{-i},\Sigma_{-i}^{-1}m_{-i}\rangle + 𝔼 a i ∼ x i ​ [ 1 2 ​ ⟨ a i , H i , i ​ a i ⟩ + ⟨ h i , a i ⟩ ] − ϵ i ​ H ​ ( x i ) . \displaystyle+\mathbb{E}_{a_{i}\sim x_{i}}\left[\frac{1}{2}\langle a_{i},H_{i,i}a_{i}\rangle+\langle h_{i},a_{i}\rangle\right]-\epsilon_{i}H(x_{i}).

[168] p: This is an unconstrained optimization problem in the space of probability measures. We will use the first-order necessary conditions in the Wasserstein space in Lanzetti et al. (2024) ; Lanzetti et al. (2025a) to construct an optimal solution and then use the sufficient conditions to establish optimality. Using Theorem 3.2 in Lanzetti et al. (2025a) , we can set the Wasserstein gradient to 0 to obtain that, at optimality, the following first-order necessary condition must hold:

[169] table: 1 τ i ​ ( − τ i ​ H i , − i ​ Σ ¯ − i ) ​ Σ ¯ − i − 1 ​ m ¯ − H i , i ​ a i − h i + ϵ i ​ ∇ ρ ​ ( a i ) ρ ⁡ ( a i ) = 0 for x i -almost all a i ∈ ℝ n , \frac{1}{\tau_{i}}(-\tau_{i}H_{i,-i}\bar{\Sigma}_{-i})\bar{\Sigma}_{-i}^{-1}\bar{m}-H_{i,i}a_{i}-h_{i}+\epsilon_{i}\frac{\nabla\rho(a_{i})}{\rho(a_{i})}=0\qquad\text{ for $x_{i}$-almost all $a_{i}\in\mathbb{R}^{n}$}, (11)

[170] p: where ρ \rho is the density of the optimal x i x_{i} (if it exists). The first term follows from a generalization of the chain rule (Proposition 2.16 in Lanzetti et al. (2025a) ), while the other terms follow from the well-known Wasserstein gradients of expected values (Proposition 2.20 in Lanzetti et al. (2025a) ) and of entropy (Example 2.27 in Lanzetti et al. (2025a) ). We now make the “ansatz” that x i x_{i} is Gaussian with mean m i m_{i} and covariance Σ i \Sigma_{i} . Since x i x_{i} is Gaussian, we have

[171] table: ∇ ρ ​ ( a i ) ρ ⁡ ( a i ) = ∇ ( − 1 2 ​ ⟨ a i − m i , Σ i − 1 ​ ( a i − m i ) ⟩ ) = − Σ i − 1 ​ ( a i − m i ) . \frac{\nabla\rho(a_{i})}{\rho(a_{i})}=\nabla\left(-\frac{1}{2}\left\langle a_{i}-m_{i},\Sigma_{i}^{-1}(a_{i}-m_{i})\right\rangle\right)=-\Sigma_{i}^{-1}(a_{i}-m_{i}).

[172] p: Thus, together with the expression for m ¯ − i \bar{m}_{-i} , ( 11 ) reduces

[173] table: − H i , − i ​ Σ ¯ − i ​ ( Σ − i − 1 ​ m − i − τ i ​ ( H i , − i ⊤ ​ m i + h − i ) ) − H i , i ​ a i − h i − ϵ i ​ Σ i − 1 ​ ( a i − m i ) = 0 -H_{i,-i}\bar{\Sigma}_{-i}(\Sigma_{-i}^{-1}m_{-i}-\tau_{i}(H_{i,-i}^{\top}m_{i}+h_{-i}))-H_{i,i}a_{i}-h_{i}-\epsilon_{i}\Sigma_{i}^{-1}(a_{i}-m_{i})=0 (12)

[174] p: We study mean and covariance separately.

[175] p: Mean: We can then integrate ( 12 ) with respect to x i x_{i} to obtain

[176] table: ∫ ℝ n − H i , − i Σ ¯ − i ( Σ − i − 1 m − i − τ i ( H i , − i ⊤ m i + h − i ) ) − H i , i a i − h i − ϵ i Σ i − 1 ( a i − m i ) d x i ( a i ) = 0 . \int_{\mathbb{R}^{n}}-H_{i,-i}\bar{\Sigma}_{-i}(\Sigma_{-i}^{-1}m_{-i}-\tau_{i}(H_{i,-i}^{\top}m_{i}+h_{-i}))-H_{i,i}a_{i}-h_{i}-\epsilon_{i}\Sigma_{i}^{-1}(a_{i}-m_{i})\differential x_{i}(a_{i})=0.

[177] p: This yields

[178] table: − H i , − i ​ Σ ¯ − i ​ ( Σ − i − 1 ​ m − i − τ i ​ ( H i , − i ⊤ ​ m i + h − i ) ) − ( H i , i + Q i ) ​ m i − h i = 0 , -H_{i,-i}\bar{\Sigma}_{-i}(\Sigma_{-i}^{-1}m_{-i}-\tau_{i}(H_{i,-i}^{\top}m_{i}+h_{-i}))-(H_{i,i}+Q_{i})m_{i}-h_{i}=0,

[179] p: and so

[180] table: ( − H i , i + τ i ​ H i , − i ​ Σ ¯ − i ​ H i , − i ⊤ ) ​ m i − H i , − i ​ Σ ¯ − i ​ Σ − i − 1 ​ m − i + τ i ​ H i , − i ​ Σ ¯ − i ​ h − i − h i = 0 . \left(-H_{i,i}+\tau_{i}H_{i,-i}\bar{\Sigma}_{-i}H_{i,-i}^{\top}\right)m_{i}-H_{i,-i}\bar{\Sigma}_{-i}\Sigma_{-i}^{-1}m_{-i}+\tau_{i}H_{i,-i}\bar{\Sigma}_{-i}h_{-i}-h_{i}=0.

[181] p: The unique solution to this linear equation is

[182] table: m i = ( − H i , i + τ i ​ H i , − i ​ Σ ¯ − i ​ H i , − i ⊤ ) − 1 ​ ( h i + H i , − i ​ Σ ¯ − i ​ ( Σ − i − 1 ​ m − i − τ i ​ h − i ) CLOSE . m_{i}=\left(-H_{i,i}+\tau_{i}H_{i,-i}\bar{\Sigma}_{-i}H_{i,-i}^{\top}\right)^{-1}\left(h_{i}+H_{i,-i}\bar{\Sigma}_{-i}(\Sigma_{-i}^{-1}m_{-i}-\tau_{i}h_{-i}\right).

[183] p: With Σ ¯ − i = 1 τ i ​ P − i − 1 \bar{\Sigma}_{-i}=\frac{1}{\tau_{i}}P_{-i}^{-1} we obtain the desired expression.

[184] p: Covariance: We right multiply ( 12 ) with ( a i − m i ) ⊤ (a_{i}-m_{i})^{\top} and integrate with respect to x i x_{i} to get

[185] table: − ∫ ℝ n H i , i a i ( a i − m i ) ⊤ d x i ( a i ) − ϵ i I = 0 -\int_{\mathbb{R}^{n}}H_{i,i}a_{i}(a_{i}-m_{i})^{\top}\mathrm{d}x_{i}(a_{i})-\epsilon_{i}I=0

[186] p: and so

[187] table: − H i , i ​ ( Σ i + m i ​ m i ⊤ − m i ​ m i ⊤ ) − ϵ i ​ I = 0 . -H_{i,i}(\Sigma_{i}+m_{i}m_{i}^{\top}-m_{i}m_{i}^{\top})-\epsilon_{i}I=0.

[188] p: Overall, we therefore have

[189] table: Σ i = − ϵ i ​ H i , i − 1 . \Sigma_{i}=-\epsilon_{i}H_{i,i}^{-1}.

[190] p: Finally, we notice that the objective function is strongly geodesically convex in the distribution. Thus, the candidate solution is the unique minimizer and, therefore, the unique best response to x − i x_{-i} (see Theorem 3.3 in Lanzetti et al. (2025a) ). ∎

[191] p: With this lemma, we obtain a way to compute Gaussian RQE in continuous games:

[192] h6: Lemma \thetheorem .

[193] p: Consider a surrogate “game of the means”, where each player selects a vector m i ∈ ℝ n m_{i}\in\mathbb{R}^{n} to maximize the surrogate concave quadratic utility

[194] table: U ¯ i ​ ( m i , m − i ) = 1 2 ​ ⟨ m i , ( H i , i − H i , − i ​ P − i − 1 ​ H i , − i ⊤ ) ​ m i ⟩ + 1 τ i ​ ⟨ m i , H i , − i ​ P − i − 1 ​ Σ − i − 1 ​ m − i ⟩ + ⟨ m i , h i − H i , − i ​ P − i − 1 ​ h − i ⟩ . \bar{U}_{i}(m_{i},m_{-i})=\frac{1}{2}\langle m_{i},(H_{i,i}-H_{i,-i}P_{-i}^{-1}H_{i,-i}^{\top})m_{i}\rangle+\frac{1}{\tau_{i}}\langle m_{i},H_{i,-i}P_{-i}^{-1}\Sigma_{-i}^{-1}m_{-i}\rangle+\langle m_{i},h_{i}-H_{i,-i}P_{-i}^{-1}h_{-i}\rangle. (13)

[195] p: Then, ( m 1 ⋆ , … , m N ⋆ ) (m_{1}^{\star},\ldots,m_{N}^{\star}) is a Nash equilibrium of the game with utility ( 13 ) if and only if ( x 1 ⋆ , … , x N ⋆ ) (x^{\star}_{1},\ldots,x_{N}^{\star}) , where x i ⋆ x_{i}^{\star} is a Gaussian distribution with mean m i ⋆ m_{i}^{\star} and variance − ϵ i ​ H i , i − 1 -\epsilon_{i}H_{i,i}^{-1} , is an RQE of the game with utilities ( 10 ). Moreover, ( m 1 ⋆ , … , m N ⋆ ) (m_{1}^{\star},\ldots,m_{N}^{\star}) is the unique Nash equilibrium of this surrogate game if and only if ( x 1 ⋆ , … , x N ⋆ ) (x^{\star}_{1},\ldots,x_{N}^{\star}) is the unique RQE in which one or more mixed strategies are Gaussian.

[196] h6: Proof.

[197] p: The proof follows directly from Section B.1.1 . Uniqueness in Gaussian mixed strategies follows from uniqueness of the best response. ∎

[198] p: At this point, we can study RQE for games in which

[199] table: R ⁡ ( a 1 , … , a N ) = − 1 2 ​ ‖ ∑ i = 1 N a i − a ¯ ‖ H 2 = − 1 2 ​ ⟨ ∑ i = 1 N a i − a ¯ , H ⁡ ( ∑ i = 1 N a i − a ¯ ) ⟩ c i ​ ( a i ) = ρ i 2 ​ ‖ a i ‖ 2 , R(a_{1},\ldots,a_{N})=-\frac{1}{2}\left\|\sum_{i=1}^{N}a_{i}-\bar{a}\right\|_{H}^{2}=-\frac{1}{2}\left\langle\sum_{i=1}^{N}a_{i}-\bar{a},H\left(\sum_{i=1}^{N}a_{i}-\bar{a}\right)\right\rangle\qquad c_{i}(a_{i})=\frac{\rho_{i}}{2}\norm{a_i}^{2},

[200] p: where we assume that the matrix H H , used in the weighted norm, is symmetric positive definite and ρ i > 0 \rho_{i}>0 . As we will show below, considering this class is sufficient.

[201] h6: Proposition \thetheorem (computation of RQE) .

[202] p: Let ϵ i > 0 \epsilon_{i}>0 and τ i > 0 \tau_{i}>0 so that

[203] table: 1 τ i ​ ϵ j ​ ( ρ j + H ) − H ≻ 0 ∀ j ≠ i . \frac{1}{\tau_{i}\epsilon_{j}}(\rho_{j}+H)-H\succ 0\qquad\forall j\neq i. (14)

[204] p: Let ( m 1 ⋆ , … , m N ⋆ ) ∈ ℝ n × … × ℝ n (m_{1}^{\star},\ldots,m_{N}^{\star})\in\mathbb{R}^{n}\times\ldots\times\mathbb{R}^{n} be a Nash equilibrium of the surrogate game where the utility of each player is

[205] table: U ¯ i ​ ( m i , m − i ) = 1 2 ​ ⟨ m i , ( − ρ i ​ I − H − ∑ j ≠ i H ​ P i ​ j − 1 ​ H ) ​ m i ⟩ − 1 τ i ​ ⟨ m i , H ⁡ ( ∑ j ≠ i P i ​ j − 1 ​ Σ j − 1 ​ m j ) ⟩ + ⟨ m i , H ​ a ¯ + H ​ ∑ j ≠ i P i ​ j − 1 ​ H ​ a ¯ ⟩ , \bar{U}_{i}(m_{i},m_{-i})=\frac{1}{2}\left\langle m_{i},\left(-\rho_{i}I-H-\sum_{j\neq i}HP_{ij}^{-1}H\right)m_{i}\right\rangle\\ -\frac{1}{\tau_{i}}\left\langle m_{i},H\left(\sum_{j\neq i}P_{ij}^{-1}\Sigma_{j}^{-1}m_{j}\right)\right\rangle+\left\langle m_{i},H\bar{a}+H\sum_{j\neq i}P_{ij}^{-1}H\bar{a}\right\rangle,

[206] p: where Σ i = ϵ i ​ ( ρ i ​ I + H ) − 1 ≻ 0 \Sigma_{i}=\epsilon_{i}(\rho_{i}I+H)^{-1}\succ 0 and P i ​ j = 1 τ i ​ ϵ j ​ ( ρ j ​ I + H ) − H ≻ 0 P_{ij}=\frac{1}{\tau_{i}\epsilon_{j}}(\rho_{j}I+H)-H\succ 0 . Then, the Gaussian mixed strategies ( x 1 ⋆ , … , x N ⋆ ) (x_{1}^{\star},\ldots,x_{N}^{\star}) form an RQE of the game and, at equilibrium, each player has finite costs. Moreover, if the equilibrium ( m 1 ⋆ , … , m N ⋆ ) (m_{1}^{\star},\ldots,m_{N}^{\star}) is unique, then ( x 1 ⋆ , … , x N ⋆ ) (x_{1}^{\star},\ldots,x_{N}^{\star}) is the unique Gaussian RQE. In particular, this is the case ρ i \rho_{i} , the degrees of risk aversion, and the degrees of bounded rationality are player-independent (i.e., ρ i = ρ \rho_{i}=\rho , τ i = τ \tau_{i}=\tau , and ϵ = ϵ i \epsilon=\epsilon_{i} ).

[207] h6: Proof.

[208] p: The proof follows directly from Section B.1.1 , where we have H i , i = − H − ρ i ​ I H_{i,i}=-H-\rho_{i}I , H − i , − i = I N − 1 ⊗ ( − H ) H_{-i,-i}=I_{N-1}\otimes(-H) , H i , − i = [ − H … − H ] H_{i,-i}=\begin{bmatrix}-H&\ldots&-H\end{bmatrix} , h i = H ​ a ¯ h_{i}=H\bar{a} , and h − i = [ ( H ​ a ¯ ) ⊤ ⋯ ( H ​ a ¯ ) ⊤ ] ⊤ h_{-i}=\begin{bmatrix}(H\bar{a})^{\top}&\cdots&(H\bar{a})^{\top}\end{bmatrix}^{\top} . We now show that if ρ i = ρ \rho_{i}=\rho , τ i = τ \tau_{i}=\tau , and ϵ i = ϵ \epsilon_{i}=\epsilon we have uniqueness. We show this in the case of two players; the general case is then a straightforward extension. For uniqueness, it suffices to check that the surrogate game is strongly monotone and therefore will have a unique Nash equilibrium ( Facchinei and Pang, 2003 ) . Since ρ i = ρ \rho_{i}=\rho , τ i = τ \tau_{i}=\tau , and ϵ i = ϵ \epsilon_{i}=\epsilon , we also have Σ 2 = Σ 2 = Σ \Sigma_{2}=\Sigma_{2}=\Sigma and P 12 = P 21 = P P_{12}=P_{21}=P . In this case, the game map reads

[209] table: ℱ ⁡ ( m 1 , m 2 ) = [ ∂ m 1 U ¯ 1 ​ ( m 1 , m 2 ) ∂ m 2 U ¯ 2 ​ ( m 2 , m 1 ) ] = F ​ [ m 1 m 2 ] + f , \mathcal{F}(m_{1},m_{2})=\begin{bmatrix}\partial_{m_{1}}\bar{U}_{1}(m_{1},m_{2})\\ \partial_{m_{2}}\bar{U}_{2}(m_{2},m_{1})\end{bmatrix}=F\begin{bmatrix}m_{1}\\ m_{2}\end{bmatrix}+f,

[210] p: where

[211] table: F ≔ [ − ρ ​ I − H − H ​ P − 1 ​ H ⊤ − 1 τ ​ H ​ P − 1 ​ Σ − 1 − 1 τ ​ H ​ P − 1 ​ Σ − 1 − ρ ​ I − H − H ​ P − 1 ​ H ⊤ ] f = [ H ​ a ¯ + H ​ P − 1 ​ H ​ a ¯ H ​ a ¯ + H ​ P − 1 ​ H ​ a ¯ ] . F\coloneqq\begin{bmatrix}-\rho I-H-HP^{-1}H^{\top}&-\frac{1}{\tau}HP^{-1}\Sigma^{-1}\\ -\frac{1}{\tau}HP^{-1}\Sigma^{-1}&-\rho I-H-HP^{-1}H^{\top}\end{bmatrix}\qquad f=\begin{bmatrix}H\bar{a}+HP^{-1}H\bar{a}\\ H\bar{a}+HP^{-1}H\bar{a}\end{bmatrix}.

[212] p: With

[213] table: − 1 τ ​ H ​ P − 1 ​ Σ − 1 = − 1 τ ​ H ​ ( 1 τ ​ Σ − 1 − H ) − 1 ​ Σ − 1 = − H ​ ( I − τ ​ Σ ​ H ) − 1 = − H + τ ​ H ​ Σ ​ H ​ ( I − τ ​ Σ ​ H ) − 1 = − H − H ​ ( 1 τ ​ Σ − 1 − H ) − 1 ​ H = − H − H ​ P − 1 ​ H -\frac{1}{\tau}HP^{-1}\Sigma^{-1}=-\frac{1}{\tau}H\left(\frac{1}{\tau}\Sigma^{-1}-H\right)^{-1}\Sigma^{-1}=-H(I-\tau\Sigma H)^{-1}\\ =-H+\tau H\Sigma H(I-\tau\Sigma H)^{-1}=-H-H\left(\frac{1}{\tau}\Sigma^{-1}-H\right)^{-1}H=-H-HP^{-1}H

[214] p: we have

[215] table: F = [ − ρ ​ I 0 0 − ρ ​ I ] + [ − H − H − H − H ] + [ − H ​ P − 1 ​ H − H ​ P − 1 ​ H − H ​ P − 1 ​ H − H ​ P − 1 ​ H ] . F=\begin{bmatrix}-\rho I&0\\ 0&-\rho I\end{bmatrix}+\begin{bmatrix}-H&-H\\ -H&-H\end{bmatrix}+\begin{bmatrix}-HP^{-1}H&-HP^{-1}H\\ -HP^{-1}H&-HP^{-1}H\end{bmatrix}.

[216] p: Clearly, F F is negative definite, as it results from the sum of a negative definite matrix and two positive semidefinite matrices. Thus, the game map is strongly monotone, and we have uniqueness. ∎

[217] h5: Discussion

[218] p: A few observations on this result. First, the surrogate game can be solved by setting the gradient of each player’s utility to zero, which yields a linear system of equations which can be shown to possess a unique solution whenever ρ i > 0 \rho_{i}>0 . Second, if the assumption ( 14 ) is violated, then the utility of player i i will generally diverge − ∞ -\infty and, thus, the player has “infinite” risk. To rule out this triviality, we therefore assume ( 14 ). Third, uniqueness is in the space of Gaussian mixed strategies. Thus, there might exist another equilibrium in which all mixed strategies are non-Gaussian.

[219] h4: B.1.2 Proof of Section 4.1

[220] p: We prove a more general version of Section 4.1 .

[221] p: [risk induces collaboration] Consider the game with utilities in ( 4.1 ). On the domain of τ i \tau_{i} where ( 14 ) and where the Gaussian RQE in unique 2 2 footnotemark: 2 , let x i ⋆ ​ ( τ 1 , … , τ N ) x_{i}^{\star}(\tau_{1},\ldots,\tau_{N}) be the mixed strategy of player i i at the unique Gaussian RQE of the game, as a function of the degrees of risk aversion τ 1 , … , τ N \tau_{1},\ldots,\tau_{N} . Then, the expected shared reward ( τ 1 , … , τ N ) ↦ J ⁡ ( τ 1 , … , τ N ) (\tau_{1},\ldots,\tau_{N})\mapsto J(\tau_{1},\ldots,\tau_{N}) , where

[222] table: J ⁡ ( τ 1 , … , τ N ) ≔ 𝔼 a i ∼ x i ⋆ ​ ( τ 1 , … , τ N ) ​ [ R ⁡ ( a 1 , … , a N ) ] , J(\tau_{1},\ldots,\tau_{N})\coloneqq\mathbb{E}_{a_{i}\sim x_{i}^{\star}(\tau_{1},\ldots,\tau_{N})}\left[R(a_{1},\ldots,a_{N})\right],

[223] p: is strictly increasing 3 3 3 Uniqueness holds whenever the game is symmetric or τ i \tau_{i} is sufficiently small. In general, uniqueness of Gaussian RQE can be checked studying the uniqueness of Nash equilibria for the surrogate game Section B.1.1 , and, amounts to checking positive (or negative) positiveness of a matrix. That is, players contribute more to the joint reward as they become more risk-averse. 3 3 footnotetext: Here, strictly increasing means that if τ i ′ ≥ τ i \tau_{i}^{\prime}\geq\tau_{i} for all i i with one inequality strict, then J ⁡ ( τ 1 ′ , … , τ N ′ ) > J ⁡ ( τ 1 , … , τ N ) J(\tau_{1}^{\prime},\ldots,\tau_{N}^{\prime})>J(\tau_{1},\ldots,\tau_{N}) .

[224] h6: Proof of Section B.1.2 .

[225] p: For simplicity of notation, we conduct the proof in the case of two players, with the extension to more players being straightforward. To start, we show that, without loss of generality, the problem can be simplified, via the following three steps. First, we notice

[226] table: R ⁡ ( a 1 , a 2 ) = 1 2 ​ ⟨ a 1 + a 2 , H ⁡ ( a 1 + a 2 ) ⟩ + ⟨ h , a 1 + a 2 ⟩ = 1 2 ​ ⟨ a 1 + a 2 + H − 1 ​ h , H ⁡ ( a 1 + a 2 + H − 1 ​ h ) ⟩ − ⟨ h , H − 1 ​ h ⟩ . R(a_{1},a_{2})=\frac{1}{2}\langle a_{1}+a_{2},H(a_{1}+a_{2})\rangle+\langle h,a_{1}+a_{2}\rangle=\frac{1}{2}\langle a_{1}+a_{2}+H^{-1}h,H(a_{1}+a_{2}+H^{-1}h)\rangle-\langle h,H^{-1}h\rangle.

[227] p: Since the term ⟨ h , H − 1 ​ h ⟩ \langle h,H^{-1}h\rangle is constant, we can therefore without loss of generality focus on the reward

[228] table: R ⁡ ( a 1 , a 2 ) = 1 2 ​ ⟨ a 1 + a 2 + H − 1 ​ h , H ⁡ ( a 1 + a 2 + H − 1 ​ h ) ⟩ . R(a_{1},a_{2})=\frac{1}{2}\langle a_{1}+a_{2}+H^{-1}h,H(a_{1}+a_{2}+H^{-1}h)\rangle.

[229] p: Additionally, if we let H ¯ = − H \bar{H}=-H , which is positive definite, we have

[230] table: R ⁡ ( a 1 , a 2 ) = − 1 2 ​ ⟨ a 1 + a 2 − H ¯ − 1 ​ h , H ¯ ​ ( a 1 + a 2 − H ¯ − 1 ​ h ) ⟩ = − 1 2 ​ ‖ a 1 + a 2 − a ¯ ‖ H ¯ 2 R(a_{1},a_{2})=-\frac{1}{2}\langle a_{1}+a_{2}-\bar{H}^{-1}h,\bar{H}(a_{1}+a_{2}-\bar{H}^{-1}h)\rangle=-\frac{1}{2}\|a_{1}+a_{2}-\bar{a}\|_{\bar{H}}^{2}

[231] p: where a ¯ ≔ H ¯ − 1 ​ h = − H − 1 ​ h \bar{a}\coloneqq\bar{H}^{-1}h=-H^{-1}h . Second, up to replacing Q i ≔ ρ i ​ I Q_{i}\coloneqq\rho_{i}I with ρ i ​ H ¯ \rho_{i}\bar{H} and rescaling a ¯ \bar{a} , we can assume, without loss of generality, that H ¯ = I \bar{H}=I (i.e., H = − I H=-I ). Third, we note that, since the variance of each mixed strategy x i ⋆ ​ ( τ 1 , τ 2 ) x_{i}^{\star}(\tau_{1},\tau_{2}) does not depend on risk parameters τ 1 , τ 2 \tau_{1},\tau_{2} , it suffices to study the monotonicity of the function

[232] table: J ¯ ​ ( τ 1 , τ 2 ) = − 1 2 ​ ‖ m 1 ⋆ ​ ( τ 1 , τ 2 ) + m 2 ⋆ ​ ( τ 1 , τ 2 ) − a ¯ ‖ 2 , \bar{J}(\tau_{1},\tau_{2})=-\frac{1}{2}\norm{m_1^\star(\tau_1,\tau_2)+m_2^\star(\tau_1,\tau_2)-\bar a}^{2},

[233] p: where m i ⋆ ​ ( τ 1 , τ 2 ) m_{i}^{\star}(\tau_{1},\tau_{2}) is the mean of x i ⋆ ​ ( τ 1 , τ 2 ) x_{i}^{\star}(\tau_{1},\tau_{2}) at the unique Gaussian RQE.

[234] p: Thus, we now study the monotonicity of J ¯ ​ ( τ 1 , τ 2 ) \bar{J}(\tau_{1},\tau_{2}) . From basic sensitivity analysis, J ¯ ​ ( τ 1 , τ 2 ) \bar{J}(\tau_{1},\tau_{2}) is smooth and, thus, all its directional derivatives can be expressed via its gradient. To evaluate the gradient of J ¯ ​ ( τ 1 , τ 2 ) \bar{J}(\tau_{1},\tau_{2}) , we compute its partial derivatives via the product rule as follows:

[235] table: ∂ τ i J ¯ ​ ( τ 1 , τ 2 ) = − ⟨ m 1 ⋆ ​ ( τ 1 , τ 2 ) + m 2 ⋆ ​ ( τ 1 , τ 2 ) − a ¯ , ∂ τ i m 1 ⋆ ​ ( τ 1 , τ 2 ) + ∂ τ i m 2 ⋆ ​ ( τ 1 , τ 2 ) ⟩ . \partial_{\tau_{i}}\bar{J}(\tau_{1},\tau_{2})=-\langle m_{1}^{\star}(\tau_{1},\tau_{2})+m_{2}^{\star}(\tau_{1},\tau_{2})-\bar{a},\partial_{\tau_{i}}m_{1}^{\star}(\tau_{1},\tau_{2})+\partial_{\tau_{i}}m_{2}^{\star}(\tau_{1},\tau_{2})\rangle. (15)

[236] p: We evaluate this derivative for i = 1 i=1 , with the case i = 2 i=2 being analogous. As a preliminary, we note that

[237] table: [ m 1 ⋆ ​ ( τ 1 , τ 2 ) m 2 ⋆ ​ ( τ 1 , τ 2 ) ] \displaystyle\begin{bmatrix}m_{1}^{\star}(\tau_{1},\tau_{2})\\ m_{2}^{\star}(\tau_{1},\tau_{2})\end{bmatrix} = [ − Q 1 − I − P 12 − 1 − 1 τ 1 ​ P 12 − 1 ​ Σ 2 − 1 − 1 τ 2 ​ P 21 − 1 ​ Σ 1 − 1 − Q 2 − I − P 21 − 1 ] ⏟ S ⁡ ( τ 1 , τ 2 ) ​ [ − a ¯ − P 12 − 1 ​ a ¯ − a ¯ − P 12 − 1 ​ a ¯ ] \displaystyle=\underbrace{\begin{bmatrix}-Q_{1}-I-P_{12}^{-1}&-\frac{1}{\tau_{1}}P_{12}^{-1}\Sigma_{2}^{-1}\\ -\frac{1}{\tau_{2}}P_{21}^{-1}\Sigma_{1}^{-1}&-Q_{2}-I-P_{21}^{-1}\end{bmatrix}}_{S(\tau_{1},\tau_{2})}\begin{bmatrix}-\bar{a}-P_{12}^{-1}\bar{a}\\ -\bar{a}-P_{12}^{-1}\bar{a}\\ \end{bmatrix} = [ Q 1 + I + P 12 − 1 1 τ 1 ​ P 12 − 1 ​ Σ 2 − 1 1 τ 2 ​ P 21 − 1 ​ Σ 1 − 1 Q 2 + I + P 21 − 1 ] ⏟ S ⁡ ( τ 1 , τ 2 ) ​ [ a ¯ + P 12 − 1 ​ a ¯ a ¯ + P 12 − 1 ​ a ¯ ] ⏟ s ⁡ ( τ 1 , τ 2 ) , \displaystyle=\underbrace{\begin{bmatrix}Q_{1}+I+P_{12}^{-1}&\frac{1}{\tau_{1}}P_{12}^{-1}\Sigma_{2}^{-1}\\ \frac{1}{\tau_{2}}P_{21}^{-1}\Sigma_{1}^{-1}&Q_{2}+I+P_{21}^{-1}\end{bmatrix}}_{S(\tau_{1},\tau_{2})}\underbrace{\begin{bmatrix}\bar{a}+P_{12}^{-1}\bar{a}\\ \bar{a}+P_{12}^{-1}\bar{a}\\ \end{bmatrix}}_{s(\tau_{1},\tau_{2})},

[238] p: where S ⁡ ( τ 1 , τ 2 ) S(\tau_{1},\tau_{2}) is a matrix whose symmetric part is positive definite. Thus, by the product and chain rule, we conclude that

[239] table: [ ∂ τ 1 m 1 ⋆ ​ ( τ 1 , τ 2 ) ∂ τ 1 m 2 ⋆ ​ ( τ 1 , τ 2 ) ] = − S ​ ( τ 1 , τ 2 ) − 1 ​ ( ∂ τ 1 S ⁡ ( τ 1 , τ 2 ) ​ [ m 1 ⋆ ​ ( τ 1 , τ 2 ) m 2 ⋆ ​ ( τ 1 , τ 2 ) ] − ∂ τ 1 s ⁡ ( τ 1 , τ 2 ) ) . \displaystyle\begin{bmatrix}\partial_{\tau_{1}}m_{1}^{\star}(\tau_{1},\tau_{2})\\ \partial_{\tau_{1}}m_{2}^{\star}(\tau_{1},\tau_{2})\end{bmatrix}=-S(\tau_{1},\tau_{2})^{-1}\left(\partial_{\tau_{1}}S(\tau_{1},\tau_{2})\begin{bmatrix}m_{1}^{\star}(\tau_{1},\tau_{2})\\ m_{2}^{\star}(\tau_{1},\tau_{2})\end{bmatrix}-\partial_{\tau_{1}}s(\tau_{1},\tau_{2})\right).

[240] p: Using

[241] table: ∂ τ 1 P 12 − 1 \displaystyle\partial_{\tau_{1}}P_{12}^{-1} = ( Σ 2 − 1 − τ 1 ​ I ) − 1 ​ Σ 2 − 1 ​ ( Σ 2 − 1 − τ 1 ​ I ) − 1 = ( Σ 2 − 1 − τ 1 ​ I ) − 2 ​ Σ 2 − 1 = ∂ τ 1 ( 1 τ 1 ​ P 12 − 1 ​ Σ 2 − 1 ) , \displaystyle=(\Sigma^{-1}_{2}-\tau_{1}I)^{-1}\Sigma_{2}^{-1}(\Sigma^{-1}_{2}-\tau_{1}I)^{-1}=(\Sigma^{-1}_{2}-\tau_{1}I)^{-2}\Sigma_{2}^{-1}=\partial_{\tau_{1}}\left(\frac{1}{\tau_{1}}P_{12}^{-1}\Sigma_{2}^{-1}\right),

[242] p: we now plug in all expressions to obtain

[243] table: [ ∂ τ 1 m 1 ⋆ ​ ( τ 1 , τ 2 ) ∂ τ 1 m 2 ⋆ ​ ( τ 1 , τ 2 ) ] \displaystyle\begin{bmatrix}\partial_{\tau_{1}}m_{1}^{\star}(\tau_{1},\tau_{2})\\ \partial_{\tau_{1}}m_{2}^{\star}(\tau_{1},\tau_{2})\end{bmatrix} = − S ​ ( τ 1 , τ 2 ) − 1 ​ ( [ ∂ τ 1 P 12 − 1 ∂ τ 1 1 τ i ​ P 12 − 1 ​ Σ 2 − 1 0 0 ] ​ [ m 1 ⋆ ​ ( τ 1 , τ 2 ) m 2 ⋆ ​ ( τ 1 , τ 2 ) ] − [ ∂ τ 1 P 12 − 1 ​ a ¯ 0 ] ) \displaystyle=-S(\tau_{1},\tau_{2})^{-1}\left(\begin{bmatrix}\partial_{\tau_{1}}P_{12}^{-1}&\partial_{\tau_{1}}\frac{1}{\tau_{i}}P_{12}^{-1}\Sigma_{2}^{-1}\\ 0&0\end{bmatrix}\begin{bmatrix}m_{1}^{\star}(\tau_{1},\tau_{2})\\ m_{2}^{\star}(\tau_{1},\tau_{2})\end{bmatrix}-\begin{bmatrix}\partial_{\tau_{1}}P_{12}^{-1}\bar{a}\\ 0\end{bmatrix}\right) = − S ​ ( τ 1 , τ 2 ) − 1 ​ ( [ ( Σ 2 − 1 − τ 1 ​ I ) − 1 ​ Σ 2 − 1 ​ ( Σ 2 − 1 − τ 1 ​ I ) − 1 ( Σ 2 − 1 − τ 1 ​ I ) − 2 ​ Σ 2 − 1 0 0 ] ​ [ m 1 ⋆ ​ ( τ 1 , τ 2 ) m 2 ⋆ ​ ( τ 1 , τ 2 ) ] CLOSE \displaystyle=-S(\tau_{1},\tau_{2})^{-1}\bigg(\begin{bmatrix}(\Sigma^{-1}_{2}-\tau_{1}I)^{-1}\Sigma_{2}^{-1}(\Sigma^{-1}_{2}-\tau_{1}I)^{-1}&(\Sigma^{-1}_{2}-\tau_{1}I)^{-2}\Sigma_{2}^{-1}\\ 0&0\end{bmatrix}\begin{bmatrix}m_{1}^{\star}(\tau_{1},\tau_{2})\\ m_{2}^{\star}(\tau_{1},\tau_{2})\end{bmatrix} OPEN − [ ( Σ 2 − 1 − τ 1 ​ I ) − 1 ​ Σ 2 − 1 ​ ( Σ 2 − 1 − τ 1 ​ I ) − 1 ​ a ¯ 0 ] ) \displaystyle\hskip 56.9055pt-\begin{bmatrix}(\Sigma_{2}^{-1}-\tau_{1}I)^{-1}\Sigma_{2}^{-1}(\Sigma_{2}^{-1}-\tau_{1}I)^{-1}\bar{a}\\ 0\end{bmatrix}\bigg) = − S ​ ( τ 1 , τ 2 ) − 1 ​ [ ( Σ 2 − 1 − τ 1 ​ I ) − 2 ​ Σ 2 − 1 0 ] ​ ( m 1 ⋆ ​ ( τ 1 , τ 2 ) + m 2 ⋆ ​ ( τ 1 , τ 2 ) − a ¯ ) \displaystyle=-S(\tau_{1},\tau_{2})^{-1}\begin{bmatrix}(\Sigma_{2}^{-1}-\tau_{1}I)^{-2}\Sigma_{2}^{-1}\\ 0\end{bmatrix}(m_{1}^{\star}(\tau_{1},\tau_{2})+m_{2}^{\star}(\tau_{1},\tau_{2})-\bar{a}) = − 1 τ 1 2 ​ S ​ ( τ 1 , τ 2 ) − 1 ​ [ P 2 − 2 ​ Σ 2 − 1 0 ] ​ ( m 1 ⋆ ​ ( τ 1 , τ 2 ) + m 2 ⋆ ​ ( τ 1 , τ 2 ) − a ¯ ) . \displaystyle=-\frac{1}{\tau_{1}^{2}}S(\tau_{1},\tau_{2})^{-1}\begin{bmatrix}P_{2}^{-2}\Sigma_{2}^{-1}\\ 0\end{bmatrix}(m_{1}^{\star}(\tau_{1},\tau_{2})+m_{2}^{\star}(\tau_{1},\tau_{2})-\bar{a}).

[244] p: Thus, we have

[245] table: ∂ τ 1 m 1 ⋆ ​ ( τ 1 , τ 2 ) \displaystyle\partial_{\tau_{1}}m_{1}^{\star}(\tau_{1},\tau_{2}) + ∂ τ 1 m 2 ⋆ ( τ 1 , τ 2 ) \displaystyle+\partial_{\tau_{1}}m_{2}^{\star}(\tau_{1},\tau_{2}) = [ I I ] ​ [ ∂ τ 1 m 1 ⋆ ​ ( τ 1 , τ 2 ) ∂ τ 1 m 2 ⋆ ​ ( τ 1 , τ 2 ) ] \displaystyle=\begin{bmatrix}I&I\end{bmatrix}\begin{bmatrix}\partial_{\tau_{1}}m_{1}^{\star}(\tau_{1},\tau_{2})\\ \partial_{\tau_{1}}m_{2}^{\star}(\tau_{1},\tau_{2})\end{bmatrix} = − 1 τ 1 2 ​ [ I I ] ​ S ​ ( τ 1 , τ 2 ) − 1 ​ [ P 2 − 2 ​ Σ 2 − 1 0 ] ⏟ N ​ ( m 1 ⋆ ​ ( τ 1 , τ 2 ) + m 2 ⋆ ​ ( τ 1 , τ 2 ) − a ¯ ) , \displaystyle=-\frac{1}{\tau_{1}^{2}}\underbrace{\begin{bmatrix}I&I\end{bmatrix}S(\tau_{1},\tau_{2})^{-1}\begin{bmatrix}P_{2}^{-2}\Sigma_{2}^{-1}\\ 0\end{bmatrix}}_{N}(m_{1}^{\star}(\tau_{1},\tau_{2})+m_{2}^{\star}(\tau_{1},\tau_{2})-\bar{a}),

[246] p: so that ( 15 ) becomes

[247] table: ∂ τ 1 J ¯ ​ ( τ 1 , τ 2 ) = 1 τ 1 2 ​ ⟨ m 1 ⋆ ​ ( τ 1 , τ 2 ) + m 2 ⋆ ​ ( τ 1 , τ 2 ) − a ¯ , N ⁡ ( m 1 ⋆ ​ ( τ 1 , τ 2 ) + m 2 ⋆ ​ ( τ 1 , τ 2 ) − a ¯ ) ⟩ . \partial_{\tau_{1}}\bar{J}(\tau_{1},\tau_{2})=\frac{1}{\tau_{1}^{2}}\langle m_{1}^{\star}(\tau_{1},\tau_{2})+m_{2}^{\star}(\tau_{1},\tau_{2})-\bar{a},N(m_{1}^{\star}(\tau_{1},\tau_{2})+m_{2}^{\star}(\tau_{1},\tau_{2})-\bar{a})\rangle.

[248] p: To conclude the proof, it suffices to show that N N is positive definite for all τ i ≥ 0 \tau_{i}\geq 0 . Indeed, in this case, ∂ τ i J ¯ ​ ( τ 1 , τ 2 ) \partial_{\tau_{i}}\bar{J}(\tau_{1},\tau_{2}) is always positive (unless m 1 ⋆ ​ ( τ 1 , τ 2 ) + m 2 ⋆ ​ ( τ 1 , τ 2 ) = a ¯ m_{1}^{\star}(\tau_{1},\tau_{2})+m_{2}^{\star}(\tau_{1},\tau_{2})=\bar{a} , which however cannot happen if ρ 1 , ρ 2 > 0 \rho_{1},\rho_{2}>0 ) and, thus, the shared reward J ¯ ​ ( τ 1 , τ 2 ) \bar{J}(\tau_{1},\tau_{2}) is strictly increasing. Thus, in the rest of the proof, we will show that N N is positive definite. Using the formula for the inverse of block matrices, we conclude that

[249] table: N = ( I + ( Q 2 + I + P 12 − 1 ) − 1 ​ 1 τ 2 ​ P 21 − 1 ​ Σ 1 − 1 ) ⏟ N 1 ( Q 1 + I + P 12 − 1 + 1 τ 1 ​ P 12 − 1 ​ Σ 2 − 1 ​ ( Q 2 + I + P 21 − 1 ) − 1 ​ 1 τ 2 ​ P 21 − 1 ​ Σ 1 − 1 ) − 1 ⏟ N 2 − 1 ​ P 12 − 2 ​ Σ 2 − 1 ⏟ N 3 − 1 . N=\underbrace{\left(I+(Q_{2}+I+P_{12}^{-1})^{-1}\frac{1}{\tau_{2}}P_{21}^{-1}\Sigma_{1}^{-1}\right)}_{N_{1}}\\ \underbrace{\left(Q_{1}+I+P_{12}^{-1}+\frac{1}{\tau_{1}}P_{12}^{-1}\Sigma_{2}^{-1}(Q_{2}+I+P_{21}^{-1})^{-1}\frac{1}{\tau_{2}}P^{-1}_{21}\Sigma_{1}^{-1}\right)^{-1}}_{N_{2}^{-1}}\underbrace{P_{12}^{-2}\Sigma_{2}^{-1}}_{N_{3}^{-1}}.

[250] p: Since Q 1 = ρ 1 ​ H Q_{1}=\rho_{1}H and Q 2 = ρ 2 ​ H Q_{2}=\rho_{2}H commute, we have that Σ 1 , Σ 2 , P 12 , P 21 \Sigma_{1},\Sigma_{2},P_{12},P_{21} , and thus N 1 , N 2 , N 3 N_{1},N_{2},N_{3} belong to the subalgebra induced by { Q 1 , Q 2 } \{Q_{1},Q_{2}\} and, thus, commute. Therefore, each N i N_{i} results from the sum and product of symmetric and positive definite matrices (and their inverses) that commute and, as such, is symmetric and positive definite. As a consequence, the matrix N N is also symmetric and positive definite. ∎

[251] p: The proof of Section 4.1 is now a direct consequence:

[252] h6: Proof of Section 4.1 .

[253] p: The proof follows from Section B.1.2 and Section B.1.1 , using ρ i = ρ \rho_{i}=\rho , τ i = τ \tau_{i}=\tau , and ϵ i = ϵ \epsilon_{i}=\epsilon for all agents. ∎

[254] p: To conclude, we provide more details on Section 4.1 :

[255] h6: Example \thetheorem (Details on Section 4.1 ) .

[256] p: For the game in Section 4.1 , we have H = 1 H=1 , ρ i = 1 \rho_{i}=1 , and c i = 0 c_{i}=0 , so that Σ i = ϵ i 2 \Sigma_{i}=\frac{\epsilon_{i}}{2} and P i ​ j = 2 τ i ​ ϵ j − 1 = 2 − τ i ​ ϵ j τ i ​ ϵ j P_{ij}=\frac{2}{\tau_{i}\epsilon_{j}}-1=\frac{2-\tau_{i}\epsilon_{j}}{\tau_{i}\epsilon_{j}} so that

[257] table: U ¯ i ​ ( m i , m − i ) = − 1 2 ​ ( 2 + τ i ​ ϵ j 2 − τ i ​ ϵ j ) ​ m i 2 − 1 τ i ​ τ i ​ ϵ j 2 − τ i ​ ϵ j ​ 2 ϵ j ​ m i ​ m − i + m i ​ ( 1 + τ i ​ ϵ j 2 − τ i ​ ϵ j ) ​ a ¯ . \bar{U}_{i}(m_{i},m_{-i})=-\frac{1}{2}\left(2+\frac{\tau_{i}\epsilon_{j}}{2-\tau_{i}\epsilon_{j}}\right)m_{i}^{2}-\frac{1}{\tau_{i}}\frac{\tau_{i}\epsilon_{j}}{2-\tau_{i}\epsilon_{j}}\frac{2}{\epsilon_{j}}m_{i}m_{-i}+m_{i}\left(1+\frac{\tau_{i}\epsilon_{j}}{2-\tau_{i}\epsilon_{j}}\right)\bar{a}.

[258] p: With τ 1 = τ 2 = τ \tau_{1}=\tau_{2}=\tau and ϵ 1 = ϵ 2 = ϵ \epsilon_{1}=\epsilon_{2}=\epsilon , we obtain the expected reward of each player from the shared reward J ⁡ ( τ ) J(\tau) minus the personal reward and it can be shown to be

[259] table: − 1 2 ​ 2 − τ ​ ϵ + ( τ ​ ϵ 2 ) 2 ( 3 − τ ​ ϵ 2 ) 2 + C , -\frac{1}{2}\frac{2-\tau\epsilon+(\frac{\tau\epsilon}{2})^{2}}{(3-\frac{\tau\epsilon}{2})^{2}}+C,

[260] p: where C C is a constant that results from the variance of the mixed strategies and is therefore not dependent on τ \tau but only on ϵ \epsilon .

[261] h3: B.2 Proof of Section 4.2

[262] p: In this section, we provide the proof of Section 4.2 . To do so, we first derive several helper-lemmas which guarantee us that (i) players’ strategies in an RQE are on the interior of the simplex, (ii) the KL-divergence between any strategy and an RQE strategy is uniformly bounded, and (iii) that we can relate the degree of free-riding to a lower bound on the distance between equilibrium strategies. To begin, we define some useful quantities that capture measures of the spread of players’ costs and reward functions c max ≔ max a ⁡ c ⁡ ( a ) c_{\mathrm{max}}\coloneqq\max_{a}c(a) , c min ≔ min a ⁡ c ⁡ ( a ) c_{\mathrm{min}}\coloneqq\min_{a}c(a) , v min ≔ min a 1 , a 2 ⁡ R ⁡ ( a 1 , a 2 ) − c max v_{\mathrm{min}}\coloneqq\min_{a_{1},a_{2}}R(a_{1},a_{2})-c_{\mathrm{max}} , v max ≔ max a 1 , a 2 ⁡ R ⁡ ( a 1 , a 2 ) − c min v_{\mathrm{max}}\coloneqq\max_{a_{1},a_{2}}R(a_{1},a_{2})-c_{\mathrm{min}} , and v ¯ ≔ v max − v min \bar{v}\coloneqq v_{\mathrm{max}}-v_{\mathrm{min}} . Throughout the proof, we let n ≔ | 𝒜 | n\coloneqq|\mathcal{A}| be the number of actions and Δ n = Δ ⁡ ( 𝒜 ) \Delta_{n}=\Delta(\mathcal{A}) be the probability simplex. For a mixed strategy x ∈ Δ n x\in\Delta_{n} , we denote by x ⁡ ( a ) ∈ [ 0 , 1 ] x(a)\in[0,1] the probability mass assigned to the action a a .

[263] h6: Lemma \thetheorem .

[264] p: Suppose that players have degree of bounded rationality ϵ \epsilon . At a RQE, a player’s strategy x i x_{i} has support on all actions, with probability at least m = exp ( − v ¯ / ϵ ) n m=\frac{\exp(-\bar v/\epsilon)}{n} .

[265] h6: Proof.

[266] p: In a RQE, a player’s strategy x i ∗ x_{i}^{*} must satisfy

[267] table: x i ∗ = arg ​ max x i ∈ Δ n ⟨ x i , Rp ∗ ⟩ − ⟨ c , x i ⟩ − ϵ ​ H ​ ( x i ) , x_{i}^{*}=\argmax_{x_{i}\in\Delta_{n}}\ \ \langle x_{i},Rp^{*}\rangle-\langle c,x_{i}\rangle-\epsilon H(x_{i}),

[268] p: where p ∗ = arg min p ∈ Δ n ⟨ x i , R p ∗ ⟩ + 1 τ KL ( p , x − i ∗ ) p^{*}=\arg\min_{p\in\Delta_{n}}\langle x_{i},Rp^{*}\rangle+\frac{1}{\tau}\KL(p,x_{-i}^{*}) . Letting v ≔ R ​ p ∗ − c v\coloneqq Rp^{*}-c , the classic results show that x i x_{i} is a Boltzmann distribution of the form:

[269] table: x i ​ ( a ) = exp ⁡ ( v ⁡ ( a ) / ϵ ) ∑ a ′ = 1 n exp ⁡ ( v ⁡ ( a ′ ) / ϵ ) , x_{i}(a)=\frac{\exp(v(a)/\epsilon)}{\sum_{a^{\prime}=1}^{n}\exp(v(a')/\epsilon)},

[270] p: where x i ​ ( a ) x_{i}(a) is the probability mass assigned to action a i a_{i} . By minimizing the numerator and maximizing the denominator of the right hand side we find that:

[271] table: x i ​ ( a ) ≥ exp ( − v ¯ / ϵ ) n , x_{i}(a)\geq\frac{\exp(-\bar v/\epsilon)}{n},

[272] p: which completes the proof. ∎

[273] h6: Lemma \thetheorem .

[274] p: Suppose x 2 ∈ σ ⁡ ( Δ n ) x_{2}\in\sigma(\Delta_{n}) where σ ⁡ ( Δ n ) ≔ { x ∈ Δ : x ⁡ ( a ) ≥ m ​ for all ​ a ∈ 𝒜 } \sigma(\Delta_{n})\coloneqq\{x\in\Delta:x(a)\geq m\text{ for all }a\in\mathcal{A}\} where m ∈ ( 0 , 1 n ) m\in(0,\frac{1}{n}) . Then the KL divergence between any distribution p ∈ Δ n p\in\Delta_{n} and x 2 x_{2} is bounded by

[275] table: sup q ∈ Δ n KL ( q , x 2 ) ≤ log ⁡ ( 1 m ) . \sup_{q\in\Delta_{n}}\KL(q,x_{2})\leq\log(\frac{1}{m}).

[276] h6: Proof.

[277] p: We directly have

[278] table: KL ( q , x 2 ) = ∑ a ∈ 𝒜 q ⁡ ( a ) ​ log ⁡ ( q ⁡ ( a ) x 2 ​ ( a ) ) ≤ ∑ a q ⁡ ( a ) ​ log ⁡ ( 1 m ) = log ⁡ ( 1 m ) \KL(q,x_{2})=\sum_{a\in\mathcal{A}}q(a)\log(\frac{q(a)}{x_2(a)})\leq\sum_{a}q(a)\log(\frac{1}{m})=\log(\frac{1}{m})

[279] p: since x 2 ​ ( a ) ≥ m x_{2}(a)\geq m . ∎

[280] h6: Lemma \thetheorem .

[281] p: Let x 1 , x 2 ∈ Δ n x_{1},x_{2}\in\Delta_{n} . If | ⟨ c , x 1 − x 2 ⟩ | ≥ δ |\langle c,x_{1}-x_{2}\rangle|\geq\delta , then

[282] table: ‖ x 1 − x 2 ‖ 1 ≥ 2 ​ δ c max − c min . \|x_{1}-x_{2}\|_{1}\geq\frac{2\delta}{c_{\max}-c_{\min}}.

[283] h6: Proof.

[284] p: Let d ≔ x 1 − x 2 d\coloneqq x_{1}-x_{2} . Since x 1 , x 2 ∈ Δ n x_{1},x_{2}\in\Delta_{n} , ∑ a d a = 0 \sum_{a}d_{a}=0 . We use the fact that, for any d ∈ ℝ n d\in\mathbb{R}^{n} with ∑ a d ⁡ ( a ) = 0 \sum_{a}d(a)=0 , | ⟨ c , d ⟩ | ≤ c max − c min 2 ​ ‖ d ‖ 1 |\langle c,d\rangle|\leq\frac{c_{\max}-c_{\min}}{2}\|d\|_{1} . This directly yields

[285] table: δ ≤ | ⟨ c , d ⟩ | ≤ c max − c min 2 ​ ‖ x 1 − x 2 ‖ 1 . \delta\leq|\langle c,d\rangle|\leq\frac{c_{\max}-c_{\min}}{2}\|x_{1}-x_{2}\|_{1}.

[286] p: Rearranging yields the lower bound. ∎

[287] p: We can now prove Theorem 4.2 , restated below with all constants made explicit. {theorem} Let δ > 0 \delta>0 . Suppose that players have a degree of bounded rationality ϵ > 0 \epsilon>0 and degrees of risk aversion τ > 0 \tau>0 that satisfies

[288] table: τ > 2 ​ ( ϵ ​ log ⁡ ( n ) + v ¯ ) ​ ( c max − c min ) 2 ϵ ​ δ 2 , \tau>\frac{2(\epsilon\log{n}+\bar{v})(c_{\mathrm{max}}-c_{\mathrm{min}})^{2}}{\epsilon\delta^{2}},

[289] p: then the game cannot admit a RQE with degree of free-riding greater than δ \delta .

[290] h6: Proof.

[291] p: We prove this by contradiction. We assume that τ > 2 ​ ( ϵ ​ log ⁡ ( n ) + v ¯ ) ​ ( c max − c min ) 2 ϵ ​ δ 2 \tau>\frac{2(\epsilon\log{n}+\bar{v})(c_{\mathrm{max}}-c_{\mathrm{min}})^{2}}{\epsilon\delta^{2}} and that x 1 x_{1} and x 2 x_{2} constitute a resulting RQE with a level of free riding larger than δ \delta ; i.e., | ⟨ c , x 1 − x 2 ⟩ | ≥ δ |\langle c,x_{1}-x_{2}\rangle|\geq\delta . Define the worst-case utility W ⁡ ( x ) W(x) and the robust-regularized objective Φ ⁡ ( x ) \Phi(x) :

[292] table: U ⁡ ( x , q ) \displaystyle U(x,q) ≔ ⟨ x , R ​ q ⟩ − ⟨ c , x ⟩ \displaystyle\coloneqq\langle x,Rq\rangle-\langle c,x\rangle W ⁡ ( x ) \displaystyle W(x) ≔ inf q ∈ Δ n U ⁡ ( x , q ) \displaystyle\coloneqq\inf_{q\in\Delta_{n}}U(x,q) Φ ⁡ ( x ) \displaystyle\Phi(x) ≔ W ⁡ ( x ) − ϵ ​ H ​ ( x ) \displaystyle\coloneqq W(x)-\epsilon H(x)

[293] p: Since W W is concave (as the infimum of affine functions) and H H is strongly convex on Δ n \Delta_{n} with respect to the ℓ 1 \ell_{1} norm, Φ \Phi is ϵ \epsilon -strongly concave on Δ n \Delta_{n} with respect to the ℓ 1 \ell_{1} norm.

[294] p: Let us consider player 1 1 ’s risk-adjusted utility. Without loss of generality, we develop the following for x 1 x_{1} , the results hold for x 2 x_{2} by symmetry. We first show that we can lower bound the risk-adjusted objective by our worst case objective for any x 1 , x 2 ∈ Δ n x_{1},x_{2}\in\Delta_{n} :

[295] table: U τ ( x 1 , x 2 ) = min q ∈ Δ n U ( x 1 , q ) + 1 τ KL ( q , x 2 ) ≥ min q ∈ Δ n U ( x 1 , q ) = W ( x 1 ) . U^{\tau}(x_{1},x_{2})=\min_{q\in\Delta_{n}}U(x_{1},q)+\frac{1}{\tau}\KL(q,x_{2})\geq\min_{q\in\Delta_{n}}U(x_{1},q)=W(x_{1}).

[296] p: Now consider an RQE made up of strategies ( x 1 , x 2 ) (x_{1},x_{2}) , we upper bound the risk-adjusted objective by using the fact that x 1 x_{1} and x 2 x_{2} are on the interior of the simplex since they are entropy-regularized best responses ( Section B.2 ), and thus the KL \KL term is bounded by Section B.2 . Letting C ≔ log ⁡ ( n ) + v ¯ ϵ C\coloneqq\log{n}+\frac{\bar{v}}{\epsilon} be the resulting upper bound (which depends solely on R , c , ϵ R,c,\epsilon and the dimension n n ) we conclude that

[297] table: U τ ( x 1 , x 2 ) = min q ∈ Δ n U ( x 1 , q ) + 1 τ KL ( q , x 2 ) ≤ W ( x 1 ) + C τ . U^{\tau}(x_{1},x_{2})=\min_{q\in\Delta_{n}}U(x_{1},q)+\frac{1}{\tau}\KL(q,x_{2})\leq W(x_{1})+\frac{C}{\tau}.

[298] p: Putting these together, we have

[299] table: Φ ⁡ ( x 1 ) = W ⁡ ( x 1 ) − ϵ ​ H ​ ( x 1 ) ≤ U τ ​ ( x 1 , x 2 ) − ϵ ​ H ​ ( x 1 ) ≤ W ⁡ ( x 1 ) + C τ − ϵ ​ H ​ ( x 1 ) = Φ ⁡ ( x 1 ) + C τ . \Phi(x_{1})=W(x_{1})-\epsilon H(x_{1})\leq U^{\tau}(x_{1},x_{2})-\epsilon H(x_{1})\leq W(x_{1})+\frac{C}{\tau}-\epsilon H(x_{1})=\Phi(x_{1})+\frac{C}{\tau}.

[300] p: Using the definition of an RQE, we can further develop this to find that, for all x ∈ Δ n x\in\Delta_{n} :

[301] table: Φ ⁡ ( x 1 ) + C τ ≥ U τ ​ ( x 1 , x 2 ) − ϵ ​ H ​ ( x 1 ) ≥ U τ ​ ( x , x 2 ) − ϵ ​ H ​ ( x ) ≥ Φ ⁡ ( x ) \Phi(x_{1})+\frac{C}{\tau}\geq U^{\tau}(x_{1},x_{2})-\epsilon H(x_{1})\geq U^{\tau}(x,x_{2})-\epsilon H(x)\geq\Phi(x)

[302] p: Re-arranging, and using the fact that Φ \Phi is strongly concave with respect to the ℓ 1 \ell_{1} norm on the simplex, we have

[303] table: Φ ⁡ ( x ) ≤ Φ ⁡ ( x ⋆ ) − ϵ 2 ​ ‖ x 1 − x ⋆ ‖ 1 2 \Phi(x)\leq\Phi(x^{\star})-\frac{\epsilon}{2}\|x_{1}-x^{\star}\|_{1}^{2}

[304] p: where x ⋆ = arg ⁡ min x ∈ Δ n ⁡ Φ ⁡ ( x ) x^{\star}=\arg\min_{x\in\Delta_{n}}\Phi(x) is the unique minimizer of Φ \Phi over the simplex. Thus,

[305] table: ϵ 2 ​ ‖ x 1 − x ⋆ ‖ 1 2 ≤ Φ ⁡ ( x ∗ ) − Φ ⁡ ( x 1 ) ≤ C τ ⟹ ‖ x 1 − x ⋆ ‖ 1 ≤ 2 ​ C τ . \frac{\epsilon}{2}\|x_{1}-x^{\star}\|_{1}^{2}\leq\Phi(x^{*})-\Phi(x_{1})\leq\frac{C}{\tau}\implies\|x_{1}-x^{\star}\|_{1}\leq\sqrt{\frac{2C}{\tau}}.

[306] p: By symmetry the same bound holds for x 2 x_{2} , and thus via the triangle inequality we obtain

[307] table: ‖ x 1 − x 2 ‖ 1 ≤ ‖ x 1 − x ⋆ ‖ 1 + ‖ x 2 − x ⋆ ‖ 1 ≤ 2 ​ 2 ​ C τ . \|x_{1}-x_{2}\|_{1}\leq\|x_{1}-x^{\star}\|_{1}+\|x_{2}-x^{\star}\|_{1}\leq 2\sqrt{\frac{2C}{\tau}}.

[308] p: Via Section B.2 , however we have that

[309] table: 2 ​ δ c max − c min ≤ ‖ x 1 − x 2 ‖ 1 ≤ ‖ x 1 − x ⋆ ‖ 1 + ‖ x 2 − x ⋆ ‖ 1 ≤ 2 ​ 2 ​ C τ . \frac{2\delta}{c_{\mathrm{max}}-c_{\mathrm{min}}}\leq\|x_{1}-x_{2}\|_{1}\leq\|x_{1}-x^{\star}\|_{1}+\|x_{2}-x^{\star}\|_{1}\leq 2\sqrt{\frac{2C}{\tau}}.

[310] p: Re-arranging, we find that

[311] table: τ ≤ 2 ​ C ​ ( c max − c min ) 2 δ 2 . \tau\leq\frac{2C(c_{\mathrm{max}}-c_{\mathrm{min}})^{2}}{\delta^{2}}.

[312] p: Plugging in our value for C = log ⁡ ( n ) + v ¯ ϵ C=\log{n}+\frac{\bar{v}}{\epsilon} , this implies that

[313] table: τ ≤ 2 ​ ( ϵ ​ log ⁡ ( n ) + v ¯ ) ​ ( c max − c min ) 2 ϵ ​ δ 2 . \tau\leq\frac{2(\epsilon\log{n}+\bar{v})(c_{\mathrm{max}}-c_{\mathrm{min}})^{2}}{\epsilon\delta^{2}}.

[314] p: However, we assumed that the RQE resulted from the use of a τ > 2 ​ ( ϵ ​ log ⁡ ( n ) + v ¯ ) ​ ( c max − c min ) 2 ϵ ​ δ 2 \tau>\frac{2(\epsilon\log{n}+\bar{v})(c_{\mathrm{max}}-c_{\mathrm{min}})^{2}}{\epsilon\delta^{2}} which is a contradiction. ∎

[315] h2: Appendix C Mathematical Background of SRPO

[316] p: In this section, we provide a formal framework for risk aversion and bounded rationality in MARL, and present the motivation for our algorithm SRPO. We first introduce the mathematical framework of discounted general-sum Markov games, and then discuss how to extend risk aversion and bounded rationality from normal-form games to Markov games. Next, we present the pseudocode of SRPO and a short discussion. To better motivate SRPO, we provide policy gradient theorems for each original player and adversary as well as their performance difference lemmas (PDLs), and introduce how to (mathematically) obtain the SRPO loss from the PDLs.

[317] h3: C.1 Discounted General-sum Markov Games

[318] p: We consider a discounted N N -player general-sum Markov game is specified by a tuple:

[319] table: ℳ ​ 𝒢 = { 𝒮 , { 𝒜 i } i = 1 N , { r i } i = 1 N , γ , P , ρ 0 } , \mathcal{MG}=\{\mathcal{S},\{\mathcal{A}_{i}\}_{i=1}^{N},\{r_{i}\}_{i=1}^{N},\gamma,P,\rho_{0}\},

[320] p: where 𝒮 \mathcal{S} is the state space of the underlying MDP, 𝒜 i \mathcal{A}_{i} is the action space of player i ∈ [ N ] i\in[N] , and we use the notation 𝒜 = ∏ i = 1 N 𝒜 i \mathcal{A}=\prod_{i=1}^{N}\mathcal{A}_{i} to denote the product action space of both players. We assume that | 𝒮 | |\mathcal{S}| and | 𝒜 i | |\mathcal{A}_{i}| are all finite. Here, r i : 𝒮 × 𝒜 → [ 0 , 1 ] r_{i}:\mathcal{S}\times\mathcal{A}\rightarrow[0,1] is the reward function of player i i , which we assume to be deterministic. We use 𝐫 \mathbf{r} to denote the joint reward function 𝐫 ≔ ( r i ) i = 1 N \mathbf{r}\coloneqq(r_{i})_{i=1}^{N} . Moreover, γ ∈ [ 0 , 1 ) \gamma\in[0,1) is the discount factor and P : 𝒮 × 𝒜 → Δ ⁡ ( 𝒮 ) P:\mathcal{S}\times\mathcal{A}\rightarrow\Delta(\mathcal{S}) is the transition kernel, where Δ ⁡ ( 𝒮 ) \Delta(\mathcal{S}) is the probability simplex of 𝒮 \mathcal{S} and P ⁡ ( s ′ | s , 𝐚 ) P(s^{\prime}|s,\mathbf{a}) is the probability of the next state being s ′ s^{\prime} given the current state s s and the current actions 𝐚 = ( a i ) i = 1 N \mathbf{a}=(a_{i})_{i=1}^{N} of the players. We use ρ 0 ∈ Δ ⁡ ( 𝒮 ) \rho_{0}\in\Delta(\mathcal{S}) to denote the initial state distribution.

[321] p: We focus on Markov policies , the class of policies where the action selection probability only depends on the current state instead of the entire gameplay trajectory, i.e., π = ( π i ) i = 1 N \pi=(\pi_{i})_{i=1}^{N} where π i : 𝒮 → Δ ⁡ ( 𝒜 i ) , i ∈ [ N ] \pi_{i}:\mathcal{S}\rightarrow\Delta(\mathcal{A}_{i}),i\in[N] . Given a product Markov policy π \pi , without considering risk aversion and bounded rationality, player i i has an expected discounted cumulative reward given by 𝔼 π ​ [ ∑ t = 0 ∞ γ t ​ r i ​ ( s t , a t ) ] \mathbb{E}_{\pi}[\sum_{t=0}^{\infty}\gamma^{t}r_{i}(s_{t},a_{t})] .

[322] p: To incorporate risk aversion and bounded rationality in discounted infinite-horizon Markov games, we slightly overload the notations in normal-form games and consider the following risk-adjusted objective of player i i that minimizes f i ( π i , π − i ) = max p i : 𝒮 → Δ ⁡ ( 𝒜 − i ) J i ( π i , π − i , p i ) f_{i}(\pi_{i},\pi_{-i})=\max_{p_{i}:\mathcal{S}\rightarrow\Delta(\mathcal{A}_{-i})}J_{i}(\pi_{i},\pi_{-i},p_{i}) where J i J_{i} is defined as

[323] table: J i ​ ( π i , π − i , p i ) = 𝔼 π , p , s 0 ∼ ρ 0 ​ [ ∑ t = 0 ∞ γ t ​ ( r i ​ ( s t , 𝐚 t ) + 1 τ i ​ D i ​ ( p i , π − i , s t ) − ϵ i ​ ν i ​ ( π i , s t ) ) ] \displaystyle J_{i}(\pi_{i},\pi_{-i},p_{i})=\mathbb{E}_{\pi,p,s_{0}\sim\rho_{0}}\bigg[\sum_{t=0}^{\infty}\gamma^{t}\bigg(r_{i}(s_{t},\mathbf{a}_{t})+\frac{1}{\tau_{i}}D_{i}\left(p_{i},\pi_{-i};s_{t}\right)-\epsilon_{i}\nu_{i}(\pi_{i};s_{t})\bigg)\bigg] (16)

[324] p: where the joint actions 𝐚 t \mathbf{a}_{t} are sampled through a i , t ∼ π i ( ⋅ | s t ) a_{i,t}\sim\pi_{i}(\cdot|s_{t}) and 𝐚 − i , t ∼ p i ( ⋅ | s t ) \mathbf{a}_{-i,t}\sim p_{i}(\cdot|s_{t}) and the next state s t + 1 s_{t+1} is sampled from s t + 1 ∼ P ( ⋅ | s t , 𝐚 t ) s_{t+1}\sim P(\cdot|s_{t},\mathbf{a}_{t}) , and the notations of D i ​ ( p i , π − i , s ) D_{i}(p_{i},\pi_{-i};s) and ν i ​ ( π i , s ) \nu_{i}(\pi_{i};s) are abbreviations of D i ( p i ( ⋅ | s ) , π − i ( ⋅ | s ) ) D_{i}(p_{i}(\cdot|s),\pi_{-i}(\cdot|s)) and ν i ( π i ( ⋅ | s ) ) \nu_{i}(\pi_{i}(\cdot|s)) respectively. Here, we allow for more generality of the regularizers, and, if we want to be consistent with the main body, we can choose D i D_{i} to be KL \KL , and ν i \nu_{i} to be negative entropy H H .

[325] p: Given a set of original player policies π i \pi_{i} and adversarial policies p i p_{i} , we define the value function for each state s ∈ 𝒮 s\in\mathcal{S} as:

[326] table: V i π , p ​ ( s ) = 𝔼 π , p , s 0 = s ​ [ ∑ t = 0 ∞ γ t ​ ( r i ​ ( s t , 𝐚 t ) + 1 τ i ​ D i ​ ( p i , π − i , s t ) − ϵ i ​ ν i ​ ( π i , s t ) ) ] \displaystyle V_{i}^{\pi,p}(s)=\mathbb{E}_{\pi,p,s_{0}=s}\bigg[\sum_{t=0}^{\infty}\gamma^{t}\bigg(r_{i}(s_{t},\mathbf{a}_{t})+\frac{1}{\tau_{i}}D_{i}\left(p_{i},\pi_{-i};s_{t}\right)-\epsilon_{i}\nu_{i}(\pi_{i};s_{t})\bigg)\bigg] (17)

[327] p: so that J i ​ ( π , p ) = 𝔼 s ∼ ρ 0 ​ [ V i π , p ​ ( s ) ] J_{i}(\pi,p)=\mathbb{E}_{s\sim\rho_{0}}[V_{i}^{\pi,p}(s)] , and the Q Q function as:

[328] table: Q i π , p ( s , 𝐚 ) = r i ( s , 𝐚 ) + γ 𝔼 s ′ ∼ P ( ⋅ | s , 𝐚 ) V i π , p ( s ′ ) . Q_{i}^{\pi,p}(s,\mathbf{a})=r_{i}(s,\mathbf{a})+\gamma\mathbb{E}_{s^{\prime}\sim P(\cdot|s,\mathbf{a})}V_{i}^{\pi,p}(s^{\prime}). (18)

[329] p: It is easy to verify that

[330] table: V i π , p ​ ( s ) = \displaystyle V_{i}^{\pi,p}(s)= π i ( ⋅ | s ) T Q i π , p ( s , ⋅ ) p i ( ⋅ | s ) + 1 τ i D i ( p i , π − i ; s ) − ϵ i ν i ( π i ; s ) . \displaystyle\pi_{i}(\cdot|s)^{T}Q_{i}^{\pi,p}(s,\cdot)p_{i}(\cdot|s)+\frac{1}{\tau_{i}}D_{i}(p_{i},\pi_{-i};s)-\epsilon_{i}\nu_{i}(\pi_{i};s). (19)

[331] p: Finally, we define given policies π i , p i \pi_{i},p_{i} , we define the discounted state visitation probability as

[332] table: d s 0 π i , p i ​ ( s ) ≔ ( 1 − γ ) ​ ∑ t = 0 ∞ γ t ​ Pr π i , p i ​ ( s t = s | s 0 ) = ( 1 − γ ) ​ ∑ t = 0 ∞ γ t ​ e s 0 T ​ ( P π i , p i ) t ​ e s , \displaystyle d_{s_{0}}^{\pi_{i},p_{i}}(s)\coloneqq(1-\gamma)\sum_{t=0}^{\infty}\gamma^{t}\Pr_{\pi_{i},p_{i}}(s_{t}=s|s_{0})=(1-\gamma)\sum_{t=0}^{\infty}\gamma^{t}e_{s_{0}}^{T}(P^{\pi_{i},p_{i}})^{t}e_{s}, (20)

[333] p: where e s e_{s} denotes the one-hot vector corresponding to state s s . To learn the RQE of the Markov game, we have to optimize the policies π i \pi_{i} to minimize (and p i p_{i} to maximize) the risk-adjusted objective ( 16 ). Here, we provide some useful tools for optimizing these policies.

[334] h3: C.2 Details of SRPO

[335] p: We present the pseudocode for SRPO in Algorithm 1 . Notice that although the agents and adversaries are maximizing two losses ℒ i SRPO \mathcal{L}_{i}^{\mathrm{SRPO}} and ℒ ¯ i SRPO \bar{\mathcal{L}}_{i}^{\mathrm{SRPO}} respectively, we unify these two losses by considering the joint loss:

[336] table: ℒ i , joint SRPO ( θ i , θ − i , β ) = ℒ i CLIP ( θ i , β ) + 1 τ i KL ( β , θ − i ) − ϵ i H ( θ i ) ( o i t ) . \mathcal{L}_{i,\mathrm{joint}}^{\mathrm{SRPO}}(\theta_{i},\theta_{-i},\beta)=\mathcal{L}_{i}^{\mathrm{CLIP}}(\theta_{i},\beta)+\frac{1}{\tau_{i}}\KL(\beta,\theta_{-i})-\epsilon_{i}H(\theta_{i})(o_{i}^{t}). (21)

[337] p: The update of agent i i can be seen as maximizing ℒ i , joint SRPO \mathcal{L}_{i,\mathrm{joint}}^{\mathrm{SRPO}} as a function of θ i \theta_{i} , and the update of adversary i i can be seen as minimizing ℒ i , joint SRPO \mathcal{L}_{i,\mathrm{joint}}^{\mathrm{SRPO}} as a function of β \beta .

[338] figure: Algorithm 1 Strategically Risk-averse Policy Optimization (SRPO) for 2 ​ n 2n -agents 1: Initialize: Policies { π θ i } i = 1 n \{\pi_{\theta_{i}}\}_{i=1}^{n} , adversaries { π ϕ i } i = 1 n \{\pi_{\phi_{i}}\}_{i=1}^{n} , and critics { V ψ i } i = 1 n \{V_{\psi_{i}}\}_{i=1}^{n} . 2: Parameters: Risk aversion { τ i } i = 1 n \{\tau_{i}\}_{i=1}^{n} , bounded rationality { ϵ i } i = 1 n \{\epsilon_{i}\}_{i=1}^{n} , learning rates η θ , η ϕ , η ψ \eta_{\theta},\eta_{\phi},\eta_{\psi} , clipping δ \delta . 3: for iteration k = 1 , 2 , … k=1,2,\dots do 4: for each agent i ∈ { 1 , … , n } i\in\{1,\dots,n\} do 5: // Data Collection 6: Run joint policy 𝝅 θ i , ϕ i = ( π θ i , π ϕ i ) \boldsymbol{\pi}_{\theta_{i},\phi_{i}}=(\pi_{\theta_{i}},\pi_{\phi_{i}}) of agent i i and adversary i i in the environment for T T steps. 7: Store trajectories 𝒟 i = { ( o i t , a i t , r i t ) } i = 1 , t = 1 n , T \mathcal{D}_{i}=\{(o_{i}^{t},a_{i}^{t},r_{i}^{t})\}_{i=1,t=1}^{n,T} . 8: Compute advantage estimates A ^ i t \hat{A}_{i}^{t} using local critic V ψ i V_{\psi_{i}} . 9: // Maximin-Optimization 10: for step in steps do 11: # Update Agent by maximizing ℒ i SRPO \mathcal{L}_{i}^{\mathrm{SRPO}} 12: θ i ← θ i + η θ ​ ∇ θ i ℒ i SRPO \theta_{i}\leftarrow\theta_{i}+\eta_{\theta}\nabla_{\theta_{i}}\mathcal{L}_{i}^{\mathrm{SRPO}} 13: # Update Adversary by maximizing ℒ ¯ i SRPO \bar{\mathcal{L}}_{i}^{\mathrm{SRPO}} 14: ϕ i ← ϕ i + η ϕ ​ ∇ ϕ i ℒ ¯ i SRPO \phi_{i}\leftarrow\phi_{i}+\eta_{\phi}\nabla_{\phi_{i}}\bar{\mathcal{L}}_{i}^{\mathrm{SRPO}} 15: # Update Local Critic 16: ψ i ← ψ i − η ψ ​ ∇ ψ i ℒ i V ​ F ​ ( ψ i ) \psi_{i}\leftarrow\psi_{i}-\eta_{\psi}\nabla_{\psi_{i}}\mathcal{L}_{i}^{VF}(\psi_{i}) 17: end for 18: end for 19: Update old policy parameters: θ i , old ← θ i \theta_{i,\text{old}}\leftarrow\theta_{i} for all i i . 20: end for

[339] h5: Discussion

[340] p: The iteration structure of SRPO is very similar to that of IPPO. In the data collection phase, unlike IPPO, agent i i computes the advantage estimate based on rollouts played against adversary i i instead of other real agents. In the optimization phase, both agent i i and their adversary update their policies to maximize the SRPO losses ( 8 ) and ( 9 ). Here, we have introduced an additional critic with parameter ψ i \psi_{i} with the MSE loss function ℒ i V ​ F ​ ( θ i , θ − i ) \mathcal{L}_{i}^{VF}(\theta_{i},\theta_{-i}) , as a standard practice for variance reduction in IPPO, which is only used when computing the advantage estimates.

[341] h3: C.3 Policy Gradient Theorems

[342] p: Policy gradient theorems are the most fundamental theoretical tool for nearly all policy-based algorithms. As the foundation of our framework, we provide the expression of policy gradients for the original agents and the adversaries under the risk-adjusted objectives, respectively. Although our results are the first to present these, similar results for single-agent version can be found in ( Lan, 2023 ) .

[343] p: For the original agents, the policy gradient theorem has the following form:

[344] h6: Lemma \thetheorem (Policy Gradient for π i \pi_{i} ) .

[345] p: The gradient ∇ π i V i π , p ​ ( s ) \nabla_{\pi_{i}}V_{i}^{\pi,p}(s) can be written as

[346] table: ∇ π i ( ⋅ | x ) V i π , p ( s ) = 1 1 − γ d s π i , p i ( x ) [ 𝔼 𝐚 − i ∼ p i ( ⋅ | x ) [ Q i π , p ( x , ⋅ , 𝐚 − i ) ] − ϵ i ∇ π i ν i ( π i ; x ) ] . \displaystyle\nabla_{\pi_{i}(\cdot|x)}V_{i}^{\pi,p}(s)=\frac{1}{1-\gamma}d_{s}^{\pi_{i},p_{i}}(x)\left[\mathbb{E}_{\mathbf{a}_{-i}\sim p_{i}(\cdot|x)}[Q_{i}^{\pi,p}(x,\cdot,\mathbf{a}_{-i})]-\epsilon_{i}\nabla_{\pi_{i}}\nu_{i}(\pi_{i};x)\right].

[347] p: If π i \pi_{i} is parameterized by θ i \theta_{i} , we have

[348] table: ∇ θ i V i π , p ( s ) = 1 1 − γ 𝔼 x ∼ d s π i , p i , 𝐚 ∼ ( π i ⊗ p i ) ( ⋅ | x ) [ ∇ θ i log ⁡ ( π i ​ ( a i | x ) ) ( Q i π , p ( x , 𝐚 ) − ϵ i ∂ ν i ​ ( π i , x ) ∂ π i ​ ( a i | x ) ) ] , \displaystyle\nabla_{\theta_{i}}V_{i}^{\pi,p}(s)=\frac{1}{1-\gamma}\mathbb{E}_{x\sim d_{s}^{\pi_{i},p_{i}},\mathbf{a}\sim(\pi_{i}\otimes p_{i})(\cdot|x)}\Bigg[\nabla_{\theta_{i}}\log{\pi_i(a_i|x)}\left(Q_{i}^{\pi,p}(x,\mathbf{a})-\epsilon_{i}\frac{\partial\nu_{i}(\pi_{i};x)}{\partial\pi_{i}(a_{i}|x)}\right)\Bigg],

[349] p: where 𝐚 = ( a i , 𝐚 − i ) \mathbf{a}=(a_{i},\mathbf{a}_{-i}) .

[350] h6: Proof.

[351] p: We have

[352] table: ∇ π i ( ⋅ | x ) V i π , p ( s ) = \displaystyle\nabla_{\pi_{i}(\cdot|x)}V_{i}^{\pi,p}(s)= ⟨ ∂ ∂ π i ( ⋅ | x ) Q i π , p ( s , ⋅ ) , ( π i ⊗ p i ) ( ⋅ | s ) ⟩ \displaystyle\langle\frac{\partial}{\partial\pi_{i}(\cdot|x)}Q_{i}^{\pi,p}(s,\cdot),(\pi_{i}\otimes p_{i})(\cdot|s)\rangle + ( 𝔼 a − i ∼ p i ( ⋅ | s ) [ Q i π , p ( s , ⋅ , a − i ) ] − ϵ i ∇ π i ν i ( π i ; s ) ) 𝕀 [ s = x ] \displaystyle+\left(\mathbb{E}_{a_{-i}\sim p_{i}(\cdot|s)}[Q_{i}^{\pi,p}(s,\cdot,a_{-i})]-\epsilon_{i}\nabla_{\pi_{i}}\nu_{i}(\pi_{i};s)\right)\mathbb{I}[s=x] = \displaystyle= γ 𝔼 s ′ ∼ P π i , p i ​ ( s ) [ ∇ π i V i π , p ( s ′ ) ] + ( 𝔼 a − i ∼ p i ( ⋅ | s ) [ Q i π , p ( s , ⋅ , a − i ) ] − ϵ i ∇ π i ν i ( π i ; s ) ) 𝕀 [ s = x ] \displaystyle\gamma\mathbb{E}_{s^{\prime}\sim P^{\pi_{i},p_{i}}(s)}[\nabla_{\pi_{i}}V_{i}^{\pi,p}(s^{\prime})]+\left(\mathbb{E}_{a_{-i}\sim p_{i}(\cdot|s)}[Q_{i}^{\pi,p}(s,\cdot,a_{-i})]-\epsilon_{i}\nabla_{\pi_{i}}\nu_{i}(\pi_{i};s)\right)\mathbb{I}[s=x] = \displaystyle= … \displaystyle\dots = \displaystyle= 1 1 − γ d s π i , p i ( x ) [ 𝔼 a − i ∼ p i ( ⋅ | x ) [ Q i π , p ( x , ⋅ , a − i ) ] − ϵ i ∇ π i ν i ( π i ; x ) ] . \displaystyle\frac{1}{1-\gamma}d_{s}^{\pi_{i},p_{i}}(x)\left[\mathbb{E}_{a_{-i}\sim p_{i}(\cdot|x)}[Q_{i}^{\pi,p}(x,\cdot,a_{-i})]-\epsilon_{i}\nabla_{\pi_{i}}\nu_{i}(\pi_{i};x)\right].

[353] p: Similarly, for the parameterized case, we have

[354] table: ∂ ∂ π i ​ ( a i | x ) \displaystyle\frac{\partial}{\partial\pi_{i}(a_{i}|x)} V i π , p ​ ( s ) \displaystyle V_{i}^{\pi,p}(s) = \displaystyle= ⟨ ∂ ∂ π i ​ ( a i | x ) Q i π , p ( s , ⋅ ) , ( π i ⊗ p i ) ( ⋅ | s ) ⟩ \displaystyle\left\langle\frac{\partial}{\partial\pi_{i}(a_{i}|x)}Q_{i}^{\pi,p}(s,\cdot),(\pi_{i}\otimes p_{i})(\cdot|s)\right\rangle + ( 𝔼 a − i ∼ p i ( ⋅ | s ) [ Q i π , p ( s , a i , a − i ) ] − ϵ i ∂ ∂ π i ​ ( a i | x ) ν i ( π i ; s ) ) 𝕀 [ s = x ] \displaystyle+\left(\mathbb{E}_{a_{-i}\sim p_{i}(\cdot|s)}[Q_{i}^{\pi,p}(s,a_{i},a_{-i})]-\epsilon_{i}\frac{\partial}{\partial\pi_{i}(a_{i}|x)}\nu_{i}(\pi_{i};s)\right)\mathbb{I}[s=x] = \displaystyle= γ 𝔼 s ′ ∼ P π i , p i ​ ( s ) [ ∂ ∂ π i ​ ( a i | x ) V i π , p ( s ′ ) ] + ( 𝔼 a − i ∼ p i ( ⋅ | s ) [ Q i π , p ( s , a i , a − i ) ] − ϵ i ∂ ∂ π i ​ ( a i | x ) ν i ( π i ; s ) ) 𝕀 [ s = x ] \displaystyle\gamma\mathbb{E}_{s^{\prime}\sim P^{\pi_{i},p_{i}}(s)}[\frac{\partial}{\partial\pi_{i}(a_{i}|x)}V_{i}^{\pi,p}(s^{\prime})]+\left(\mathbb{E}_{a_{-i}\sim p_{i}(\cdot|s)}[Q_{i}^{\pi,p}(s,a_{i},a_{-i})]-\epsilon_{i}\frac{\partial}{\partial\pi_{i}(a_{i}|x)}\nu_{i}(\pi_{i};s)\right)\mathbb{I}[s=x] = \displaystyle= … \displaystyle\dots = \displaystyle= 1 1 − γ d s π i , p i ( x ) [ 𝔼 a − i ∼ p i ( ⋅ | x ) [ Q i π , p ( x , a i , a − i ) ] − ϵ i ∂ ∂ π i ​ ( a i | x ) ν i ( π i ; x ) ] , \displaystyle\frac{1}{1-\gamma}d_{s}^{\pi_{i},p_{i}}(x)\left[\mathbb{E}_{a_{-i}\sim p_{i}(\cdot|x)}[Q_{i}^{\pi,p}(x,a_{i},a_{-i})]-\epsilon_{i}\frac{\partial}{\partial\pi_{i}(a_{i}|x)}\nu_{i}(\pi_{i};x)\right],

[355] p: therefore,

[356] table: ∇ θ i V i π , p ​ ( s ) = \displaystyle\nabla_{\theta_{i}}V_{i}^{\pi,p}(s)= ∑ x , a i ∂ ∂ π i ​ ( a i | x ) ​ V i π , p ​ ( s ) ​ ∇ θ i π i ​ ( a i | x ) \displaystyle\sum_{x,a_{i}}\frac{\partial}{\partial\pi_{i}(a_{i}|x)}V_{i}^{\pi,p}(s)\nabla_{\theta_{i}}\pi_{i}(a_{i}|x) = \displaystyle= 1 1 − γ ∑ x , a i d s π i , p i ( x ) [ 𝔼 a − i ∼ p i ( ⋅ | x ) [ Q i π , p ( x , a i , a − i ) ] − ϵ i ∂ ∂ π i ​ ( a i | x ) ν i ( π i ; x ) ] ∇ θ i π i ( a i | x ) \displaystyle\frac{1}{1-\gamma}\sum_{x,a_{i}}d_{s}^{\pi_{i},p_{i}}(x)\left[\mathbb{E}_{a_{-i}\sim p_{i}(\cdot|x)}[Q_{i}^{\pi,p}(x,a_{i},a_{-i})]-\epsilon_{i}\frac{\partial}{\partial\pi_{i}(a_{i}|x)}\nu_{i}(\pi_{i};x)\right]\nabla_{\theta_{i}}\pi_{i}(a_{i}|x) = \displaystyle= 1 1 − γ 𝔼 x ∼ d s π i , p i 𝔼 a ∼ ( π i ⊗ p i ) ( ⋅ | x ) [ ∇ θ i log ⁡ ( π i ​ ( a i | x ) ) ( Q i π , p ( x , a ) − ϵ i ∂ ∂ π i ​ ( a i | x ) ν i ( π i ; x ) ) ] . \displaystyle\frac{1}{1-\gamma}\mathbb{E}_{x\sim d_{s}^{\pi_{i},p_{i}}}\mathbb{E}_{a\sim(\pi_{i}\otimes p_{i})(\cdot|x)}\left[\nabla_{\theta_{i}}\log{\pi_i(a_i|x)}\left(Q_{i}^{\pi,p}(x,a)-\epsilon_{i}\frac{\partial}{\partial\pi_{i}(a_{i}|x)}\nu_{i}(\pi_{i};x)\right)\right].

[357] p: This concludes the proof. ∎

[358] p: Similarly, we have the policy gradient for p i p_{i} as follows:

[359] h6: Lemma \thetheorem (Policy gradient for p i p_{i} ) .

[360] p: The gradient ∇ p i V i π , p ​ ( s ) \nabla_{p_{i}}V_{i}^{\pi,p}(s) can be written as

[361] table: ∇ p i ( ⋅ | x ) V i π , p ( s ) = 1 1 − γ d s π i , p i ( x ) [ 𝔼 a i ∼ π i ( ⋅ | x ) [ Q i π , p ( x , a i , ⋅ ) ] + 1 τ i ∇ p i D i ( p i , π − i ; x ) ] \displaystyle\nabla_{p_{i}(\cdot|x)}V_{i}^{\pi,p}(s)=\frac{1}{1-\gamma}d_{s}^{\pi_{i},p_{i}}(x)\left[\mathbb{E}_{a_{i}\sim\pi_{i}(\cdot|x)}[Q_{i}^{\pi,p}(x,a_{i},\cdot)]+\frac{1}{\tau_{i}}\nabla_{p_{i}}D_{i}(p_{i},\pi_{-i};x)\right]

[362] p: and if p i p_{i} is parameterized by θ ¯ i \bar{\theta}_{i} , we have

[363] table: ∇ θ ¯ i V i π , p ( s ) = 1 1 − γ 𝔼 x ∼ d s π i , p i , 𝐚 ∼ ( π i ⊗ p i ) ( ⋅ | x ) [ ∇ θ ¯ i log p i ( 𝐚 − i | x ) ( Q i π , p ( x , 𝐚 ) + 1 τ i ∂ D i ​ ( p i , π − i , x ) ∂ p i ​ ( 𝐚 − i | x ) ) ] , \displaystyle\nabla_{\bar{\theta}_{i}}V_{i}^{\pi,p}(s)=\frac{1}{1-\gamma}\mathbb{E}_{x\sim d_{s}^{\pi_{i},p_{i}},\mathbf{a}\sim(\pi_{i}\otimes p_{i})(\cdot|x)}\left[\nabla_{\bar{\theta}_{i}}\log p_{i}(\mathbf{a}_{-i}|x)\left(Q_{i}^{\pi,p}(x,\mathbf{a})+\frac{1}{\tau_{i}}\frac{\partial D_{i}(p_{i},\pi_{-i};x)}{\partial p_{i}(\mathbf{a}_{-i}|x)}\right)\right],

[364] p: where 𝐚 = ( a i , 𝐚 − i ) \mathbf{a}=(a_{i},\mathbf{a}_{-i}) .

[365] h6: Proof.

[366] p: We have

[367] table: ∇ p i ( ⋅ | x ) V i π , p ( s ) = \displaystyle\nabla_{p_{i}(\cdot|x)}V_{i}^{\pi,p}(s)= ∇ p i ( ⋅ | x ) ( ⟨ Q i π , p ( s , ⋅ ) , ( π i ⊗ p i ) ( ⋅ | s ) ⟩ ) + 1 τ i ∇ p i D i ( p i , π − i ; s ) 𝕀 [ s = x ] \displaystyle\nabla_{p_{i}(\cdot|x)}(\langle Q_{i}^{\pi,p}(s,\cdot),(\pi_{i}\otimes p_{i})(\cdot|s)\rangle)+\frac{1}{\tau_{i}}\nabla_{p_{i}}D_{i}(p_{i},\pi_{-i};s)\mathbb{I}[s=x] = \displaystyle= ⟨ ∂ ∂ p i ( ⋅ | x ) Q i π , p ( s , ⋅ ) , ( π i ⊗ p i ) ( ⋅ | s ) ⟩ \displaystyle\langle\frac{\partial}{\partial p_{i}(\cdot|x)}Q_{i}^{\pi,p}(s,\cdot),(\pi_{i}\otimes p_{i})(\cdot|s)\rangle + ( 𝔼 a i ∼ π i ( ⋅ | s ) [ Q i π , p ( s , a i , ⋅ ) ] + 1 τ i ∇ p i D i ( p i , π − i ; s ) ) 𝕀 [ s = x ] \displaystyle+\left(\mathbb{E}_{a_{i}\sim\pi_{i}(\cdot|s)}[Q_{i}^{\pi,p}(s,a_{i},\cdot)]+\frac{1}{\tau_{i}}\nabla_{p_{i}}D_{i}(p_{i},\pi_{-i};s)\right)\mathbb{I}[s=x] = \displaystyle= γ 𝔼 s ′ ∼ P π i , p i ​ ( s ) [ ∇ p i ( ⋅ | x ) V i π , p ( s ′ ) ] + ( 𝔼 a i ∼ π i ( ⋅ | s ) [ Q i π , p ( s , a i , ⋅ ) ] + 1 τ i ∇ p i D i ( p i , π − i ; s ) ) 𝕀 [ s = x ] \displaystyle\gamma\mathbb{E}_{s^{\prime}\sim P^{\pi_{i},p_{i}}(s)}[\nabla_{p_{i}(\cdot|x)}V_{i}^{\pi,p}(s^{\prime})]+\left(\mathbb{E}_{a_{i}\sim\pi_{i}(\cdot|s)}[Q_{i}^{\pi,p}(s,a_{i},\cdot)]+\frac{1}{\tau_{i}}\nabla_{p_{i}}D_{i}(p_{i},\pi_{-i};s)\right)\mathbb{I}[s=x] = \displaystyle= … \displaystyle\dots = \displaystyle= 1 1 − γ d s π i , p i ( x ) [ 𝔼 a i ∼ π i ( ⋅ | x ) [ Q i π , p ( x , a i , ⋅ ) ] + 1 τ i ∇ p i D i ( p i , π − i ; x ) ] , \displaystyle\frac{1}{1-\gamma}d_{s}^{\pi_{i},p_{i}}(x)\left[\mathbb{E}_{a_{i}\sim\pi_{i}(\cdot|x)}[Q_{i}^{\pi,p}(x,a_{i},\cdot)]+\frac{1}{\tau_{i}}\nabla_{p_{i}}D_{i}(p_{i},\pi_{-i};x)\right],

[368] p: and similarly for the parameterized case,

[369] table: ∇ θ ¯ i V i π , p ​ ( s ) \displaystyle\nabla_{\bar{\theta}_{i}}V_{i}^{\pi,p}(s) = \displaystyle= 1 1 − γ 𝔼 x ∼ d s π i , p i 𝔼 a ∼ ( π i ⊗ p i ) ( ⋅ | x ) [ ∇ θ ¯ i log p i ( a − i | x ) ( Q i π , p ( x , a ) + 1 τ i ∂ ∂ p i ​ ( a − i | x ) D i ( p i , π − i ; x ) ) ] . \displaystyle\frac{1}{1-\gamma}\mathbb{E}_{x\sim d_{s}^{\pi_{i},p_{i}}}\mathbb{E}_{a\sim(\pi_{i}\otimes p_{i})(\cdot|x)}\left[\nabla_{\bar{\theta}_{i}}\log p_{i}(a_{-i}|x)\left(Q_{i}^{\pi,p}(x,a)+\frac{1}{\tau_{i}}\frac{\partial}{\partial p_{i}(a_{-i}|x)}D_{i}(p_{i},\pi_{-i};x)\right)\right].

[370] p: This concludes the proof. ∎

[371] h3: C.4 Performance Difference Lemmas

[372] p: Another crucial tool for quantifying the difference in value functions (hence expected returns) between different policies through the advantage function is the performance difference lemma (PDL). For our 4-player risk-adjusted game, we state the PDLs for original agents and adversaries below:

[373] h6: Lemma \thetheorem (Performance Difference Lemma for π i \pi_{i} ) .

[374] p: For two policies π i \pi_{i} and π i ′ \pi_{i}^{\prime} of player i i , we have

[375] table: V i π i , z ( s ) − V i π i ′ , z ( s ) = 1 1 − γ 𝔼 s ′ ∼ d s π i , p i , 𝐚 ∼ ( π i ⊗ p i ) ( ⋅ | s ′ ) [ A i π i ′ , z ( s ′ , 𝐚 ) − ϵ i ν i ( π i ; s ′ ) ] \displaystyle V_{i}^{\pi_{i},z}(s)-V_{i}^{\pi_{i}^{\prime},z}(s)=\frac{1}{1-\gamma}\mathbb{E}_{s^{\prime}\sim d_{s}^{\pi_{i},p_{i}},\mathbf{a}\sim(\pi_{i}\otimes p_{i})(\cdot|s^{\prime})}\left[A_{i}^{\pi_{i}^{\prime},z}(s^{\prime},\mathbf{a})-\epsilon_{i}\nu_{i}(\pi_{i};s^{\prime})\right] (22)

[376] p: where the advantage function A i A_{i} is defined as:

[377] table: A i π i , z ​ ( s , 𝐚 ) = Q i π i , z ​ ( s , 𝐚 ) − V i π i , z ​ ( s ) + 1 τ i ​ D i ​ ( z , s ) . A_{i}^{\pi_{i},z}(s,\mathbf{a})=Q_{i}^{\pi_{i},z}(s,\mathbf{a})-V_{i}^{\pi_{i},z}(s)+\frac{1}{\tau_{i}}D_{i}(z;s).

[378] p: Here, z z is the shorthand notation of z = ( π − i , p i ) z=(\pi_{-i},p_{i}) .

[379] h6: Proof.

[380] p: We can write the difference in value function as

[381] table: V i π i ′ , z ​ ( s ) − V i π i , z ​ ( s ) \displaystyle V_{i}^{\pi_{i}^{\prime},z}(s)-V_{i}^{\pi_{i},z}(s) = \displaystyle= 𝔼 π i ′ , z , s 0 = s ​ [ ∑ t = 0 ∞ γ t ​ ( r i ​ ( s t , 𝐚 t ) + 1 τ i ​ D i ​ ( z , s t ) − ϵ i ​ ν i ​ ( π i ′ , s t ) ) ] − V i π i , z ​ ( s ) \displaystyle\mathbb{E}_{\pi_{i}^{\prime},z,s_{0}=s}\left[\sum_{t=0}^{\infty}\gamma^{t}\bigg(r_{i}(s_{t},\mathbf{a}_{t})+\frac{1}{\tau_{i}}D_{i}\left(z;s_{t}\right)-\epsilon_{i}\nu_{i}(\pi_{i}^{\prime};s_{t})\bigg)\right]-V_{i}^{\pi_{i},z}(s) = \displaystyle= V i π i ′ , z ( s ) − 𝔼 ( a i , 0 , 𝐚 − i , 0 ) ∼ ( π i ⊗ p i ) ( ⋅ | s ) [ r i ( s , 𝐚 0 ) + 1 τ i D i ( z ; s ) − ϵ i ν i ( π i ; s ) + γ 𝔼 s ′ ∼ P ( ⋅ | s , 𝐚 0 ) V i π i ′ , z ( s ′ ) ] \displaystyle V_{i}^{\pi_{i}^{\prime},z}(s)-\mathbb{E}_{(a_{i,0},\mathbf{a}_{-i,0})\sim(\pi_{i}\otimes p_{i})(\cdot|s)}\left[r_{i}(s,\mathbf{a}_{0})+\frac{1}{\tau_{i}}D_{i}(z;s)-\epsilon_{i}\nu_{i}(\pi_{i};s)+\gamma\mathbb{E}_{s^{\prime}\sim P(\cdot|s,\mathbf{a}_{0})}V_{i}^{\pi_{i}^{\prime},z}(s^{\prime})\right] + 𝔼 ( a i , 0 , 𝐚 − i , 0 ) ∼ ( π i ⊗ p i ) ( ⋅ | s ) [ r i ( s , 𝐚 0 ) + 1 τ i D i ( z ; s ) − ϵ i ν i ( π i ; s ) + γ 𝔼 s ′ ∼ P ( ⋅ | s , 𝐚 0 ) V i π i ′ , z ( s ′ ) ] − V i π i , z ( s ) \displaystyle+\mathbb{E}_{(a_{i,0},\mathbf{a}_{-i,0})\sim(\pi_{i}\otimes p_{i})(\cdot|s)}\left[r_{i}(s,\mathbf{a}_{0})+\frac{1}{\tau_{i}}D_{i}(z;s)-\epsilon_{i}\nu_{i}(\pi_{i};s)+\gamma\mathbb{E}_{s^{\prime}\sim P(\cdot|s,\mathbf{a}_{0})}V_{i}^{\pi_{i}^{\prime},z}(s^{\prime})\right]-V_{i}^{\pi_{i},z}(s) = \displaystyle= 𝔼 ( a i , 0 , 𝐚 − i , 0 ) ∼ ( π i ⊗ p i ) ( ⋅ | s ) [ V i π i ′ , z ( s ) − Q i π i ′ , z ( s , 𝐚 0 ) − 1 τ i D i ( z ; s ) + ϵ i ν i ( π i ; s ) ] \displaystyle\mathbb{E}_{(a_{i,0},\mathbf{a}_{-i,0})\sim(\pi_{i}\otimes p_{i})(\cdot|s)}\left[V_{i}^{\pi_{i}^{\prime},z}(s)-Q_{i}^{\pi_{i}^{\prime},z}(s,\mathbf{a}_{0})-\frac{1}{\tau_{i}}D_{i}(z;s)+\epsilon_{i}\nu_{i}(\pi_{i};s)\right] + γ 𝔼 ( a i , 0 , 𝐚 − i , 0 ) ∼ ( π i ⊗ p i ) ( ⋅ | s ) 𝔼 s ′ ∼ P ⁡ ( s , 𝐚 0 ) [ V i π i ′ , z ( s ′ ) − V i π i , z ( s ′ ) ] \displaystyle+\gamma\mathbb{E}_{(a_{i,0},\mathbf{a}_{-i,0})\sim(\pi_{i}\otimes p_{i})(\cdot|s)}\mathbb{E}_{s^{\prime}\sim P(s,\mathbf{a}_{0})}\left[V_{i}^{\pi_{i}^{\prime},z}(s^{\prime})-V_{i}^{\pi_{i},z}(s^{\prime})\right] = \displaystyle= ⋯ \displaystyle\cdots = \displaystyle= 1 1 − γ 𝔼 s ′ ∼ d s π i , p i 𝔼 𝐚 ∼ ( π i ⊗ p i ) ( ⋅ | s ′ ) [ V i π i ′ , z ( s ′ ) − Q i π i ′ , z ( s ′ , 𝐚 ) − 1 τ i D i ( z ; s ′ ) + ϵ i ν i ( π i ; s ′ ) ] \displaystyle\frac{1}{1-\gamma}\mathbb{E}_{s^{\prime}\sim d_{s}^{\pi_{i},p_{i}}}\mathbb{E}_{\mathbf{a}\sim(\pi_{i}\otimes p_{i})(\cdot|s^{\prime})}\left[V_{i}^{\pi_{i}^{\prime},z}(s^{\prime})-Q_{i}^{\pi_{i}^{\prime},z}(s^{\prime},\mathbf{a})-\frac{1}{\tau_{i}}D_{i}(z;s^{\prime})+\epsilon_{i}\nu_{i}(\pi_{i};s^{\prime})\right]

[382] p: This concludes the proof. ∎

[383] h6: Lemma \thetheorem (Performance Difference Lemma for p i p_{i} ) .

[384] p: For two policies p i p_{i} and p i ′ p_{i}^{\prime} of adversary i i , we have:

[385] table: V i p i , π ( s ) − V i p i ′ , π ( s ) = 1 1 − γ 𝔼 s ′ ∼ d s π i , p i , 𝐚 ∼ ( π i ⊗ p i ) ( ⋅ | s ′ ) [ A i p i ′ , π ( s ′ , 𝐚 ) + 1 τ i D i ( p i , π − i ; s ′ ) ] \displaystyle V_{i}^{p_{i},\pi}(s)-V_{i}^{p_{i}^{\prime},\pi}(s)=\frac{1}{1-\gamma}\mathbb{E}_{s^{\prime}\sim d_{s}^{\pi_{i},p_{i}},\mathbf{a}\sim(\pi_{i}\otimes p_{i})(\cdot|s^{\prime})}\left[A_{i}^{p_{i}^{\prime},\pi}(s^{\prime},\mathbf{a})+\frac{1}{\tau_{i}}D_{i}(p_{i},\pi_{-i};s^{\prime})\right]

[386] p: where

[387] table: A i p i , π ​ ( s , 𝐚 ) = Q i p i , π ​ ( s , 𝐚 ) − V i p i , π ​ ( s ) − ϵ i ​ ν i ​ ( π i , s ) . A_{i}^{p_{i},\pi}(s,\mathbf{a})=Q_{i}^{p_{i},\pi}(s,\mathbf{a})-V_{i}^{p_{i},\pi}(s)-\epsilon_{i}\nu_{i}(\pi_{i};s).

[388] h6: Proof.

[389] p: We can write the value function difference as

[390] table: V i p i , π ​ ( s ) − V i p i ′ , π ​ ( s ) \displaystyle V_{i}^{p_{i},\pi}(s)-V_{i}^{p_{i}^{\prime},\pi}(s) = \displaystyle= V i p i , π ( s ) − 𝔼 ( a i , 0 , 𝐚 − i , 0 ) ∼ ( π i ⊗ p i ) ( ⋅ | s ) [ r i ( s , 𝐚 0 ) + 1 τ i D i ( p i , π − i ; s ) − ϵ i ν i ( π i ; s ) + γ 𝔼 s ′ ∼ P ( ⋅ | s , 𝐚 0 ) V i p i ′ , π ( s ′ ) ] \displaystyle V_{i}^{p_{i},\pi}(s)-\mathbb{E}_{(a_{i,0},\mathbf{a}_{-i,0})\sim(\pi_{i}\otimes p_{i})(\cdot|s)}\left[r_{i}(s,\mathbf{a}_{0})+\frac{1}{\tau_{i}}D_{i}(p_{i},\pi_{-i};s)-\epsilon_{i}\nu_{i}(\pi_{i};s)+\gamma\mathbb{E}_{s^{\prime}\sim P(\cdot|s,\mathbf{a}_{0})}V_{i}^{p_{i}^{\prime},\pi}(s^{\prime})\right] + 𝔼 ( a i , 0 , 𝐚 − i , 0 ) ∼ ( π i ⊗ p i ) ( ⋅ | s ) [ r i ( s , 𝐚 0 ) + 1 τ i D i ( p i , π − i ; s ) − ϵ i ν i ( π i ; s ) + γ 𝔼 s ′ ∼ P ( ⋅ | s , 𝐚 0 ) V i p i ′ , π ( s ′ ) ] − V i p i ′ , π ( s ) \displaystyle+\mathbb{E}_{(a_{i,0},\mathbf{a}_{-i,0})\sim(\pi_{i}\otimes p_{i})(\cdot|s)}\left[r_{i}(s,\mathbf{a}_{0})+\frac{1}{\tau_{i}}D_{i}(p_{i},\pi_{-i};s)-\epsilon_{i}\nu_{i}(\pi_{i};s)+\gamma\mathbb{E}_{s^{\prime}\sim P(\cdot|s,\mathbf{a}_{0})}V_{i}^{p_{i}^{\prime},\pi}(s^{\prime})\right]-V_{i}^{p_{i}^{\prime},\pi}(s) = \displaystyle= γ 𝔼 ( a i , 0 , 𝐚 − i , 0 ) ∼ ( π i ⊗ p i ) ( ⋅ | s ) 𝔼 s ′ ∼ P ( ⋅ | s , 𝐚 0 ) [ V i p i , π ( s ′ ) − V i p i ′ , π ( s ′ ) ] \displaystyle\gamma\mathbb{E}_{(a_{i,0},\mathbf{a}_{-i,0})\sim(\pi_{i}\otimes p_{i})(\cdot|s)}\mathbb{E}_{s^{\prime}\sim P(\cdot|s,\mathbf{a}_{0})}[V_{i}^{p_{i},\pi}(s^{\prime})-V_{i}^{p_{i}^{\prime},\pi}(s^{\prime})] + 𝔼 ( a i , 0 , 𝐚 − i , 0 ) ∼ ( π i ⊗ p i ) ( ⋅ | s ) [ Q i p i ′ , π ( s , 𝐚 0 ) + 1 τ i D i ( p i , π − i ; s ) − ϵ i ν i ( π i ; s ) − V i p i ′ , π ( s ) ] \displaystyle+\mathbb{E}_{(a_{i,0},\mathbf{a}_{-i,0})\sim(\pi_{i}\otimes p_{i})(\cdot|s)}\left[Q_{i}^{p_{i}^{\prime},\pi}(s,\mathbf{a}_{0})+\frac{1}{\tau_{i}}D_{i}(p_{i},\pi_{-i};s)-\epsilon_{i}\nu_{i}(\pi_{i};s)-V_{i}^{p_{i}^{\prime},\pi}(s)\right] = \displaystyle= … \displaystyle\dots = \displaystyle= 1 1 − γ 𝔼 s ′ ∼ d s π i , p i 𝔼 𝐚 ∼ ( π i ⊗ p i ) ( ⋅ | s ′ ) [ Q i p i ′ , π ( s ′ , 𝐚 0 ) + 1 τ i D i ( p i , π − i ; s ′ ) − ϵ i ν i ( π i ; s ′ ) − V i p i ′ , π ( s ′ ) ] . \displaystyle\frac{1}{1-\gamma}\mathbb{E}_{s^{\prime}\sim d_{s}^{\pi_{i},p_{i}}}\mathbb{E}_{\mathbf{a}\sim(\pi_{i}\otimes p_{i})(\cdot|s^{\prime})}\left[Q_{i}^{p_{i}^{\prime},\pi}(s^{\prime},\mathbf{a}_{0})+\frac{1}{\tau_{i}}D_{i}(p_{i},\pi_{-i};s^{\prime})-\epsilon_{i}\nu_{i}(\pi_{i};s^{\prime})-V_{i}^{p_{i}^{\prime},\pi}(s^{\prime})\right].

[391] p: This concludes the proof. ∎

[392] h3: C.5 Motivating the SRPO Objective

[393] p: Having stated the policy gradient theorems and PDLs, we now motivate our SRPO objective following the same rationale as that in TRPO ( Schulman et al., 2015 ) . Let z = ( π 0 , p 0 ) z=(\pi^{0},p^{0}) be the joint policy at the current timestep, by Section C.4 , consider policy update for π i \pi_{i} , we can write the value function for any policy π i \pi_{i} as

[394] table: J i π i , π − i 0 , p i 0 = J i π 0 , p 0 + 1 1 − γ 𝔼 s ∼ d π i , p i 0 , 𝐚 ∼ ( π i ⊗ p i 0 ) ( ⋅ | s ) [ A i π i 0 , π − i 0 , p i 0 ( s , 𝐚 ) − ϵ i ν i ( π i ; s ) ] , \displaystyle J_{i}^{\pi_{i},\pi_{-i}^{0},p_{i}^{0}}=J_{i}^{\pi^{0},p^{0}}+\frac{1}{1-\gamma}\mathbb{E}_{s\sim d^{\pi_{i},p_{i}^{0}},\mathbf{a}\sim(\pi_{i}\otimes p_{i}^{0})(\cdot|s)}\left[A_{i}^{\pi_{i}^{0},\pi_{-i}^{0},p_{i}^{0}}(s,\mathbf{a})-\epsilon_{i}\nu_{i}(\pi_{i};s)\right],

[395] p: where d π i , p i 0 d^{\pi_{i},p_{i}^{0}} is the state distribution for the initial state distribution ρ 0 \rho_{0} . When π i \pi_{i} is constrained to be close to π i 0 \pi_{i}^{0} , we use the following surrogate objective first proposed in TRPO ( Schulman et al., 2015 ) to approximate the expectation term by replacing the sample distribution from d π i , p i 0 d^{\pi_{i},p_{i}^{0}} to d π i 0 , p i 0 d^{\pi_{i}^{0},p_{i}^{0}} :

[396] table: 𝔼 s ∼ d π i 0 , p i 0 , 𝐚 ∼ ( π i 0 ⊗ p i 0 ) ( ⋅ | s ) [ π i ​ ( a i | s ) π i 0 ​ ( a i | s ) A i π 0 , p i 0 ( s , 𝐚 ) − ϵ i ν i ( π i ; s ) ] , \displaystyle\mathbb{E}_{s\sim d^{\pi_{i}^{0},p_{i}^{0}},\mathbf{a}\sim(\pi_{i}^{0}\otimes p_{i}^{0})(\cdot|s)}\left[\frac{\pi_{i}(a_{i}|s)}{\pi_{i}^{0}(a_{i}|s)}A_{i}^{\pi^{0},p_{i}^{0}}(s,\mathbf{a})-\epsilon_{i}\nu_{i}(\pi_{i};s)\right], (23)

[397] p: where the approximation d π i 0 , p i 0 ≈ d π i , p i 0 d^{\pi_{i}^{0},p_{i}^{0}}\approx d^{\pi_{i},p_{i}^{0}} holds when π 0 \pi^{0} stays close to π \pi , and importance sampling through the ratio π i ​ ( a i | s ) π i 0 ​ ( a i | s ) \frac{\pi_{i}(a_{i}|s)}{\pi_{i}^{0}(a_{i}|s)} on a i a_{i} . Similarly by Section C.4 , we have the following surrogate objective for p i p_{i} as follows:

[398] table: 𝔼 s ∼ d π i 0 , p i 0 , 𝐚 ∼ ( π i 0 ⊗ p i 0 ) ( ⋅ | s ) [ \displaystyle\mathbb{E}_{s\sim d^{\pi_{i}^{0},p_{i}^{0}},\mathbf{a}\sim(\pi_{i}^{0}\otimes p_{i}^{0})(\cdot|s)}\Bigg[ p i ​ ( 𝐚 − i | s ) p i 0 ​ ( 𝐚 − i | s ) A i p i 0 , π 0 ( s , 𝐚 ) + 1 τ i D i ( p i , π − i ; s ) ] . \displaystyle\frac{p_{i}(\mathbf{a}_{-i}|s)}{p_{i}^{0}(\mathbf{a}_{-i}|s)}A_{i}^{p_{i}^{0},\pi^{0}}(s,\mathbf{a})+\frac{1}{\tau_{i}}D_{i}(p_{i},\pi_{-i};s)\Bigg]. (24)

[399] p: The original TRPO objective suggests optimizing ( 23 ) and ( 24 ) subject to the constraints

[400] table: 𝔼 d π i 0 , p i 0 [ KL ( π i ( ⋅ | s ) ∥ π i 0 ( ⋅ | s ) ) ] ≤ δ , \mathbb{E}_{d^{\pi_{i}^{0},p_{i}^{0}}}[\KL(\pi_{i}(\cdot|s)\|\pi_{i}^{0}(\cdot|s))]\leq\delta,

[401] p: and

[402] table: 𝔼 d π i 0 , p i 0 [ KL ( p i ( ⋅ | s ) ∥ p i 0 ( ⋅ | s ) ) ] ≤ δ , \mathbb{E}_{d^{\pi_{i}^{0},p_{i}^{0}}}[\KL(p_{i}(\cdot|s)\|p_{i}^{0}(\cdot|s))]\leq\delta,

[403] p: respectively. A later adaptation PPO ( Schulman et al., 2017 ) replaces these hard constraints with the clipped surrogate objective. Following this adaptation and replacing the policy to condition on observations instead of the global states, we obtain our SRPO losses ( 8 ) and ( 9 ) respectively.

[404] h2: Appendix D Experimental Details

[405] h3: D.1 Overall Setup

[406] p: Across all experiments, we compare SRPO against IPPO under a unified training and evaluation protocol. Each method is trained from scratch using multiple random seeds, and performance is reported as episodic return averaged over rollouts.

[407] h5: Training.

[408] p: Agents are trained for a fixed interaction budget per environment, with periodic evaluation during training. Unless otherwise specified, SRPO and IPPO agents share the same architecture, optimizer settings, amount of interaction with the environment, and entropy regularization, differing only in the inclusion of the strategic risk-averse objective. Given the same total amount of interactions, SRPO and IPPO take roughly the same time to train in all environments we have.

[409] h5: Cross-play evaluation.

[410] p: To assess unseen partner generalization, we adopt a cross-play protocol. For each environment, we collect a population of independently trained agents and evaluate all pairwise combinations without further learning. Cross-play performance is reported as a matrix, where each entry corresponds to the average episodic return of a fixed agent pair evaluated over multiple episodes. This protocol measures zero-shot coordination with previously unseen partners.

[411] h3: D.2 Overcooked Gridworld

[412] h5: Environments.

[413] p: We implemented a revised version of Overcooked AI, shown in Fig. 6 . The task is defined on a 5 × 5 5\times 5 grid with two agents acting simultaneously. Agents start from one of two symmetric initial configurations in the top left and must cooperatively pick up onions from two fixed sources and deliver them to a central pot. Each agent selects from five discrete actions (up, down, left, right, stay); non-stay actions incur a private movement cost of 0.2. Agent updates are applied sequentially in random order each step, with collisions blocked and penalized by 2.0. An agent can carry at most one onion; stepping onto an available onion grants a shared reward of +1 and removes the onion, while delivering an onion by attempting to move into the (solid) pot yields a shared reward of +10. Each onion independently respawns with probability 0.2 per step. Observations are fully shared and consist of both agents’ positions, carry status, and onion availability. In this setup, rewards combine private movement penalties with shared team rewards, inducing cooperative behavior under individual costs.

[414] figure: Figure 5 : The Overcooked Gridworld environment. Figure 6 : The Tag environment.

[415] h5: Training and evaluation.

[416] p: Each agent is trained for approximately 2 × 10 6 2\times 10^{6} environment interactions. Training statistics are recorded every 10240 interactions, where each evaluation point reports the average return over 5 rollouts of length 128. We perform 30 independent runs for each method. IPPO agents use an entropy coefficient of ϵ = 0.1 \epsilon=0.1 , while SRPO agents use τ = 10 \tau=10 with the same entropy coefficient. For the main experiments, we construct a 60 × 60 60\times 60 cross-play matrix consisting of 30 IPPO agents and 30 SRPO agents. Each entry is averaged over 100 evaluation episodes of length 100. We report cross-play results for both the training environment and the held-out test environment. The results are shown in Fig. 2 .

[417] h3: D.3 Tag

[418] h5: Environment.

[419] p: We evaluate on the PettingZoo Multi-Agent Particle Environment (MPE) simple_tag_v3 ( Terry et al., 2021 ) , configured with 1 runner (prey), 2 chasers, and 2 static obstacles, using discrete actions and a horizon of 100 cycles per episode. The environment is shown in Fig. 6 . Rewards are taken directly from the environment and scaled by 0.1, and an episode terminates when any agent is terminated or truncated.

[420] h5: Training and evaluation.

[421] p: Each agent is trained for approximately 3 × 10 7 3\times 10^{7} environment interactions. Training performance is recorded every 40960 40960 interactions, where each evaluation point reports the average episodic return over 64 rollouts of length 100. We perform 30 independent runs for each method. IPPO agents use an entropy coefficient of ϵ = 0.01 \epsilon=0.01 , while SRPO agents use the risk aversion parameter τ = 10 \tau=10 with the same entropy coefficient. To evaluate partner generalization, we construct a 60 × 60 60\times 60 cross-play matrix consisting of 30 IPPO agents and 30 SRPO agents. Each matrix entry corresponds to the average return obtained by a fixed agent pair, evaluated over 100 episodes of length 100 without further learning. In addition to cross-play on the training environment, we evaluate all agent pairs in a held-out test environment with a different runner configuration and report these results separately. The results are shown in Fig. 3 .

[422] h3: D.4 Hanabi

[423] h5: Environments.

[424] p: Hanabi is a cooperative card game where players act as distracted pyrotechnicians who must work together to launch a spectacular fireworks display by playing cards in the correct sequence, with the twist that you can see everyone’s cards except your own and is a canonical benchmark for collaboration. At each turn, the active player chooses from moves such as playing a card to the shared firework piles, discarding a card to regain an information token, or hinting another player about the color or rank of cards in their hand; hints consume a finite pool of information tokens, and illegal plays consume life tokens. Following Lauffer et al. (2025) , we consider a version with 3 3 colors and 3 3 ranks. We conduct our experiments in both the 2 2 player and the 4 4 player settings.

[425] h5: Training and evaluation.

[426] p: Each run uses a single GPU with 1 training thread and 1000 rollout threads, collecting trajectories of episode length 100 100 . We train for 3 × 10 7 3\times 10^{7} environment steps with PPO updates using 15 epochs and 1 minibatch per update. We set the learning rates to 7 × 10 − 4 7\times 10^{-4} (actor) and 1 × 10 − 3 1\times 10^{-3} (critic), and set the initialization gain to 0.01 0.01 . We set the entropy regularization to 0.001 0.001 and the risk aversion parameter τ = 0.01 \tau=0.01 . In the 2 2 -player setting, policies use a 2 2 -layer MLP with hidden size 128. In the 4 4 -player setting, policies use a 2 2 -layer MLP with hidden size 256, and each agent is randomly set to be adversary agent during each rollout for SRPO. For each setting, we construct a 20 × 20 20\times 20 cross-play matrix consisting of 10 10 IPPO agents and 10 10 SRPO agents, trained independently with different seeds. Each entry is averaged over 50 50 evaluation episodes of length 100 100 . The results are shown in Figs. 7 and 8 .

[427] figure: (a) Hanabi 2 2 -player. (b) Hanabi 4 4 -player. Figure 7 : Cross-play performances of SRPO ( ϵ = 0.001 , τ = 0.01 \epsilon=0.001,\tau=0.01 ) and IPPO ( ϵ = 0.001 \epsilon=0.001 ) in both 2 2 -player and 4 4 -player hanabi games. Each square represents the average reward of two agents across 50 runs of length 100.

[428] figure: (a) Hanabi 2 2 -player. (b) Hanabi 4 4 -player. Figure 8 : Performance change (mean and standard deviation) between Training Performance (TP) and Cross-play Performance (CP): the performance of IPPO drastically decreases, with lower average and larger standard deviation in cross-play, while the performance of SRPO drops less severely.

[429] h3: D.5 Multi-agent debate on GSM8k

[430] h5: Environment.

[431] p: In this setup, two agents engage in a three-round iterative debate protocol. In the first round, each agent independently observes the question and produces its own reasoning and answer. In subsequent rounds, each agent observes the original question as well as both agents’ outputs from the previous round, and then refines its response. Successfully solving a problem therefore requires more than producing a correct answer in isolation: each agent must reinforce correct reasoning while remaining robust to potentially misleading or incorrect proposals from its teammate. This naturally induces a cooperative yet adversarial interaction, where robustness to the partner’s policy plays a critical role in achieving reliable joint performance. Both IPPO (the existing state-of-the-art) and SRPO agents are trained using multiple base language models, including Qwen2.5-0.5B-Instruct (Q0.5B) and Qwen2.5-3B-Instruct (Q3B) ( Bai et al., 2025 ) , as well as Qwen3-0.6B (Q0.6B) and Qwen3-4B-Instruct-2507 (Q4B) ( Yang et al., 2025 ) , using the verl training framework ( Sheng et al., 2024 ) . Here, we set the entropy coefficient to be ϵ = 0 \epsilon=0 for both IPPO and SRPO, and τ = 10 \tau=10 for SRPO. Qwen2.5-0.5B-Instruct is trained with 200 200 epochs, and Qwen3-0.6B is trained with 300 300 steps. Every 10 10 epochs, we evaluate the performances on a held-out validation set using the same debate setup. The results are shown in Figs. 10 , 9 , 11 and 12 . Specifically, the initial accuracy before debate reflects the agent’s reasoning abilities, while the final accuracy after debate reflects the agent’s coordination abilities. The results show that, compared to IPPO, SRPO only changes the agent’s coordination abilities, instead of the reasoning abilities. The final debate accuracy achieved by SRPO during training is slightly lower than that of IPPO, as SRPO is trained in the presence of an adversarial partner, whereas IPPO is not.

[432] figure: (a) Initial accuracy before debate. (b) Final accuracy after debate. Figure 9 : The training curve for SRPO and IPPO with Qwen2.5-0.5B-Instruct. We point out that SRPO is trained against an adversary—meaning lower training reward (post debate) is expected as the adversary learns to mislead the agent to minimize reward.

[433] figure: (a) Initial accuracy before debate. (b) Final accuracy after debate. Figure 10 : The training curve for SRPO and IPPO with Qwen3-0.6B. We point out that SRPO is trained against an adversary—meaning lower training reward (post debate) is expected as the adversary learns to mislead the agent to minimize reward.

[434] figure: (a) Initial accuracy before debate. (b) Final accuracy after debate. Figure 11 : The training curve for SRPO and IPPO with Qwen2.5-3B-Instruct. We point out that SRPO is trained against an adversary—meaning lower training reward (post debate) is expected as the adversary learns to mislead the agent to minimize reward.

[435] figure: (a) Initial accuracy before debate. (b) Final accuracy after debate. Figure 12 : The training curve for SRPO and IPPO with Qwen3-4B-Instruct-2507. We point out that SRPO is trained against an adversary—meaning lower training reward (post debate) is expected as the adversary learns to mislead the agent to minimize reward.

[436] h3: D.6 Ablation study

[437] p: We conduct ablation studies on both the risk aversion parameter τ \tau and the entropy coefficient ϵ \epsilon in the Overcooked and Tag environments. The results are shown in Figs. 13 and 14 . While prior work ( Forkel and Foerster, 2025 ) demonstrates that tuning the entropy coefficient ϵ \epsilon can improve cross-play performance of IPPO in the Hanabi environment, we find that this strategy does not generalize to Overcooked or Tag. In these environments, entropy tuning alone fails to yield robust partner generalization, suggesting that entropy regularization is not a principled mechanism for addressing coordination under partner shifts.

[438] figure: (a) Overcooked. (b) Tag. Figure 13 : Ablation study on the entropy parameter ϵ \epsilon .

[439] figure: (a) Overcooked. (b) Tag. Figure 14 : Ablation study on the degree of risk aversion parameter τ \tau ; τ = 0 \tau=0 refers to the risk-neutral case, i.e., IPPO.

[440] h2: Instructions for reporting errors

[441] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[442] p: Tip: You can select the relevant text first, to include it in your report.

[443] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[444] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
