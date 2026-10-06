[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Compress the Easy, Explore the Hard: Difficulty-Aware Entropy Regularization for Efficient LLM Reasoning

[3] h6: Abstract.

[4] p: Chain-of-Thought (CoT) has substantially empowered Large Language Models (LLMs) to tackle complex reasoning tasks, yet the verbose nature of explicit reasoning steps incurs prohibitive inference latency and computational costs, limiting real-world deployment. While existing compression methods—ranging from self-training to Reinforcement Learning (RL) with length constraints—attempt to mitigate this, they often sacrifice reasoning capability for brevity. We identify a critical failure mode in these approaches: explicitly optimizing for shorter trajectories triggers rapid entropy collapse, which prematurely shrinks the exploration space and stifles the discovery of valid reasoning paths, particularly for challenging questions requiring extensive deduction. To address this issue, we propose Compress responses for Easy questions and Explore Hard ones ( CEEH ), a difficulty-aware approach to RL-based efficient reasoning. CEEH dynamically assesses instance difficulty to apply selective entropy regularization: it preserves a diverse search space for currently hard questions to ensure robustness, while permitting aggressive compression on easier instances where the reasoning path is well-established. In addition, we introduce a dynamic optimal-length penalty anchored to the historically shortest correct response, which effectively counteracts entropy-induced length inflation and stabilizes the reward signal. Across six reasoning benchmarks, CEEH consistently reduces response length while maintaining accuracy comparable to the base model, and improves Pass@k relative to length-only optimization.

[5] h6: Keywords:

[6] h2: 1. Introduction

[7] p: Large language models (LLMs) have achieved remarkable reliability on complex reasoning tasks by externalizing intermediate reasoning steps via Chain-of-Thought (CoT) prompting ( Chen et al., 2025b ; Wei et al., 2022 ; Suzgun et al., 2023 ) . By articulating step-by-step rationales, CoT enables models to maintain and compose intermediate evidence, thereby reducing brittle shortcut behaviors and enhancing robustness in multi-hop deduction ( Nguyen et al., 2024 ; Wang et al., 2023 ) and long-horizon planning ( Stechly et al., 2024 ; Verma et al., 2025 ) . However, explicit reasoning often incurs significant redundancy, leading to increased inference latency, higher token consumption, and elevated serving costs. This efficiency bottleneck has motivated a growing body of research on reasoning compression ( Munkhbat et al., 2025 ; Chen et al., 2024 ; Fang et al., 2025 ; Chen et al., 2025a ) , which aims to preserve the benefits of explicit reasoning while minimizing token generation. The central challenge lies in achieving concise responses with minimal degradation in reasoning capability, effectively optimizing the trade-off between correctness and inference cost for real-world deployment.

[8] figure: Figure 1. Accuracy–length trade-off in reasoning compression: shorter responses can come at the cost of accuracy and reduced policy entropy.

[9] p: A prevalent and efficient approach to compression is optimizing LLMs via RL with length-aware objectives, such as explicit length penalties ( Arora and Zanette, 2025 ; Cheng et al., 2025b ; Tu et al., 2025 ) . Nevertheless, as illustrated in Figure 1 , existing methods frequently achieve conciseness at the expense of accuracy, even when trained on high-quality datasets. We identify two primary causes for this degradation: first, overly concise generations may bypass beneficial inference behaviors like self-reflection and error correction; second, and more critically, aggressively optimizing for brevity can trigger rapid entropy collapse , rendering the policy increasingly deterministic. Prior studies ( Cui et al., 2025a ; Wang et al., 2025b ) indicate that low policy entropy during RL impedes performance gains, as a contracted exploration space hinders the model’s ability to discover correct solutions for challenging problems.

[10] p: Entropy regularization ( Cui et al., 2025a ; Wang et al., 2025b ; Park et al., 2025 ; Wang et al., 2025a ) offers a principled mechanism to sustain exploration during RL. However, applying uniform entropy regularization across all training instances introduces a new conflict: increased exploration typically induces longer reasoning trajectories ( Tang et al., 2025 ; Cui et al., 2025a ) , which directly counteracts the goal of reasoning compression and dilutes the length-control signal. This tension stems from the fact that problems of varying difficulty inherently demand different balances between exploration and compression. This observation naturally raises a pivotal question: Which reasoning processes should be compressed, and which require thorough exploration?

[11] p: To resolve this tension, we propose CEEH , a framework grounded in the design philosophy: C ompress E asy instances and E xplore H ard ones. The framework consists of two synergistic components. First, we introduce difficulty-aware entropy regularization . Rather than regularizing all samples uniformly, we selectively apply entropy regularization to questions currently deemed difficult for the model—instances where additional exploration is crucial to prevent premature convergence and recover accuracy. Conversely, for easier questions, regularization is relaxed, allowing the policy to confidently exploit shorter reasoning paths. To obtain a stable difficulty signal under stochastic rollouts,we maintain per-question accuracy estimates using an asymmetric exponential moving average, effectively mitigating oscillations in difficulty classification.

[12] p: To counterbalance the increased exploration on hard questions and prevent potential length inflation, we introduce a dynamic optimal-length penalty as the second component. While entropy regularization encourages diverse reasoning, it risks undermining conventional length penalties based on fixed priors or group-wise normalization. Our dynamic penalty addresses this by tracking the historically shortest correct response length for each question and penalizing deviations from this evolving baseline. This design ensures that exploration remains focused and efficient, providing a consistent compression signal that adapts to the model’s improving capabilities.

[13] p: Overall, our specific contributions can be summarized as follows:

[14] p: We provide an entropy-based perspective showing that rapid entropy decay is a key factor underlying the difficulty of managing the accuracy–length trade-off in reasoning compression.

[15] p: We propose CEEH , a novel framework that integrates difficulty-aware entropy regularization to sustain exploration and a dynamic optimal-length penalty to stabilize training, effectively addressing the identified collapse.

[16] p: Experiments on a suite of mathematical reasoning benchmarks show that CEEH achieves a superior accuracy-efficiency trade-off compared to strong baselines, effectively compressing reasoning without sacrificing accuracy.

[17] h2: 2. Preliminaries

[18] h4: Reinforcement Learning with Verifiable Rewards

[19] p: Through training on tasks with explicit, verifiable answers, Reinforcement Learning with Verifiable Rewards (RLVR) has demonstrated substantial advantages in logical reasoning domains, including mathematics, code generation, and visual question answering. In the RLVR setting, the LLM is directly optimized as the policy π θ \pi_{\theta} with RL methods. Given an input 𝒙 \boldsymbol{x} sampled from a dataset 𝒟 \mathcal{D} , the LLM generates an output 𝒚 = { s , a } \boldsymbol{y}=\{s,a\} , which consists of the reasoning trajectory s s and a final answer a a . The reward of the output 𝒚 \boldsymbol{y} is obtained by comparing the generated answer a a against ground-truth answer a ⋆ a^{\star} :

[20] table: (1) R ⁡ ( 𝒚 | 𝒙 , π θ ) = { 1 , a = a ⋆ 0 , a ≠ a ⋆ R(\boldsymbol{y}|\boldsymbol{x},\pi_{\theta})=\begin{cases}1,&a=a^{\star}\\ 0,&a\neq a^{\star}\end{cases}

[21] p: A widely used algorithm for RLVR is Group Relative Policy Optimization (GRPO) ( Shao et al., 2024 ) , which leverages group-wise advantage estimation to enable critic-free policy optimization, substantially reducing memory and computational overhead. Specifically, for a given input 𝒙 \boldsymbol{x} , an LLM π θ \pi_{\theta} generates a group of K K outputs 𝒴 = { 𝒚 1 , 𝒚 2 , … , 𝒚 K } \mathcal{Y}=\{\boldsymbol{y}^{1},\boldsymbol{y}^{2},...,\boldsymbol{y}^{K}\} and obtains the corresponding rewards R ⁡ ( 𝒚 i | 𝒙 , π θ ) R(\boldsymbol{y}^{i}|\boldsymbol{x},\pi_{\theta}) by matching each answer with the ground truth. The inter-group advantages are computed by normalizing the rewards with the group statistics:

[22] table: (2) A ⁡ ( 𝒚 i | 𝒙 ) = R ⁡ ( 𝒚 i | 𝒙 , π θ ) − μ R σ R + ξ , A(\boldsymbol{y}^{i}|\boldsymbol{x})=\frac{R(\boldsymbol{y}^{i}|\boldsymbol{x},\pi_{\theta})-\mu_{R}}{\sigma_{R}+\xi},

[23] p: where μ R \mu_{R} and σ R \sigma_{R} denote the mean and standard deviation of the rewards within the group, and ξ \xi is a small constant added to avoid division by zero. Denote the importance sampling ratio π θ ​ ( 𝒚 i | 𝒙 ) / π θ o ​ l ​ d ​ ( 𝒚 i | 𝒙 ) \pi_{\theta}(\boldsymbol{y}^{i}|\boldsymbol{x})/\pi_{\theta_{old}}(\boldsymbol{y}^{i}|\boldsymbol{x}) by ρ ⁡ ( θ , θ o ​ l ​ d ) \rho(\theta,\theta_{old}) . GRPO optimizes the policy model by maximizing the following objective:

[24] table: (3) 𝒥 ( θ ) = 𝔼 𝒙 ∼ 𝒟 , 𝒚 i ∼ π θ o ​ l ​ d ​ ( 𝒚 | 𝒙 ) A IS ( 𝒚 i | 𝒙 ) − β 𝔻 K ​ L [ π θ | | π r ​ e ​ f ] , \mathcal{J}(\theta)=\mathbb{E}_{\boldsymbol{x}\sim\mathcal{D},\boldsymbol{y}^{i}\sim\pi_{\theta_{old}}(\boldsymbol{y}|\boldsymbol{x})}A_{\text{IS}}(\boldsymbol{y}^{i}|\boldsymbol{x})-\beta\mathbb{D}_{KL}\left[\pi_{\theta}||\pi_{ref}\right],

[25] p: where

[26] table: (4) A IS ​ ( 𝒚 i | 𝒙 ) = min ⁡ [ ρ ⁡ ( θ , θ o ​ l ​ d ) ​ A i , clip ​ ( ρ ⁡ ( θ , θ o ​ l ​ d ) , 1 − ϵ , 1 + ϵ ) ​ A i ] A_{\text{IS}}(\boldsymbol{y}^{i}|\boldsymbol{x})=\min\left[\rho(\theta,\theta_{old})A_{i},\text{clip}\left(\rho(\theta,\theta_{old}),1-\epsilon,1+\epsilon\right)A_{i}\right]

[27] p: and ϵ \epsilon controls the trust region that constrains the policy update.

[28] figure: Figure 2. The pipeline of our method. The model accuracy is evaluated via GRPO rollouts, and the optimal length is obtained from correct responses. Length penalties are applied only to correct responses when current accuracy exceeds historical accuracy, while entropy regularization is used for questions whose accuracy falls below the average to encourage exploration.

[29] h4: Entropy Regularization

[30] p: To encourage policy exploration, a common technique in conventional RL training is to augment the loss function with an entropy regularization term:

[31] table: (5) L e ​ n ​ t = 𝔼 𝒙 ∼ D [ − λ 0 ℋ ( π θ ( ⋅ | 𝒙 ) ) ] , L_{ent}=\mathbb{E}_{\boldsymbol{x}\sim D}[-\lambda_{0}\mathcal{H}(\pi_{\theta}(\cdot|\boldsymbol{x}))],

[32] p: where ℋ ⁡ ( π θ ) \mathcal{H}(\pi_{\theta}) denotes the policy entropy and λ 0 \lambda_{0} is the regularization coefficient. For an LLM, given an input 𝒙 \boldsymbol{x} , it autoregressively generates an output sequence 𝒚 \boldsymbol{y} that consists of T T tokens { y 1 , y 2 , … , y T } \{y_{1},y_{2},\ldots,y_{T}\} . The policy entropy is computed as:

[33] table: (6) ℋ ( π θ ( ⋅ | 𝒙 ) ) = 𝔼 𝒚 ∼ π θ ( ⋅ | 𝒙 ) [ − 1 T ∑ t = 1 T log π θ ( y t | 𝒚 < t , 𝒙 ) ] \mathcal{H}(\pi_{\theta}(\cdot|\boldsymbol{x}))=\mathbb{E}_{\boldsymbol{y}\sim\pi_{\theta}(\cdot|\boldsymbol{x})}\left[-\frac{1}{T}\sum_{t=1}^{T}\log\pi_{\theta}(y_{t}|\boldsymbol{y}_{<t},\boldsymbol{x})\right]

[34] p: Recent studies suggest ( Yue et al., 2025 ) that RL does not reliably improve the Pass@ k k performance of LLMs, and therefore may fail to yield genuine gains in reasoning capability. Other works ( Cui et al., 2025a ) further observe that entropy collapse can substantially degrade Pass@ k k performance, making entropy control during RL training a central concern. However, naively applying Eq. ( 5 ) as an entropy regularization term leads to strong hyperparameter sensitivity. A small coefficient has only a minor influence on entropy, while a large one can lead to entropy explosion. To address this issue, several studies propose LLM-specific entropy regularization techniques that achieve more stable control by identifying and training on tokens with high entropy ( Wang et al., 2025b ) or high covariance ( Cui et al., 2025a ) . In contrast, Cheng et al. (2025a) introduces an entropy-based auxiliary advantage that encourages exploration by promoting longer and deeper reasoning chains, yielding a simple yet effective performance improvement. The entropy-based advantage is defiend as follows:

[35] table: (7) ψ ⁡ ( ℋ ) = min ⁡ ( α ⋅ ℋ detach , | A | κ ) , where ​ α > 0 ​ and ​ κ > 1 , \psi(\mathcal{H})=\min\left(\alpha\cdot\mathcal{H}^{\mathrm{detach}},\ \frac{|A|}{\kappa}\right),\quad\text{where }\alpha>0\text{ and }\kappa>1,

[36] table: (8) A shaped = A + ψ ⁡ ( ℋ ) . A^{\mathrm{shaped}}=A+\psi(\mathcal{H}).

[37] p: Essentially, this auxiliary advantage incentivizes the generation of high-entropy tokens while allowing the reward-based advantage to remain dominant, thereby improving performance and avoiding entropy collapse. Experiments in these studies indicate that entropy regularization tends to increase response length relative to regular RL training.

[38] h2: 3. Methodology

[39] h3: 3.1. Overview

[40] p: We present an overview of our method in Figure 2 . Our approach consists of two components. First, to mitigate the performance degradation caused by optimizing solely for shorter reasoning length, we introduce entropy regularization to responses from high-difficulty questions in Section 3.2 , promoting exploration on challenging instances and preserving overall performance. Second, we introduce a length penalty based on the historically shortest successful response length in Section 3.3 , which provides a more informative learning signal when entropy regularization possibly induces longer outputs. Finally, Section 3.4 details some important implementation during training.

[41] h3: 3.2. Difficulty-Aware Entropy Regularization

[42] h4: Motivation.

[43] p: Standard RL-based reasoning compression methods ( Cheng et al., 2025b ; Arora and Zanette, 2025 ) typically rely on length penalties to incentivize brevity. However, aggressive length optimization often precipitates a rapid collapse in policy entropy, narrowing the exploration space and causing the model to become overly confident in suboptimal, shortcut solutions. This is particularly detrimental for complex reasoning tasks, where maintaining diverse reasoning paths is essential for error correction and self-reflection ( DeepSeek-AI, 2025 ) . Furthermore, prior work suggests that reasoning-critical tokens—those governing logical structure—inherently exhibit high entropy ( Hou et al., 2025 ; Wang et al., 2025b ) . Consequently, suppressing entropy indiscriminately risks degrading the model’s logical deduction capabilities. To address this, we propose difficulty-aware entropy regularization , a strategy that selectively sustains exploration on hard instances while permitting aggressive compression on easier ones.

[44] h4: Dynamic Difficulty Estimation.

[45] p: To implement this strategy, we first need a robust metric to distinguish “hard” questions from “easy” ones during training. It is intractale to estimate the accurate difficulty from limited stochastic rollouts in GRPO. Therefore, we maintain a historical accuracy estimate for each question using an asymmetric Exponential Moving Average (EMA). Specifically, for a question 𝒙 \boldsymbol{x} , we sample K K responses in each step and compute the instantaneous accuracy:

[46] table: (9) Acc ( 𝒙 ) = 1 K ∑ i = 1 K 𝕀 [ a i = a ⋆ ] . \mathrm{Acc}(\boldsymbol{x})=\frac{1}{K}\sum_{i=1}^{K}\mathbb{I}\left[a^{i}=a^{\star}\right].

[47] p: We then update a running historical accuracy score, Acc h ​ ( 𝒙 ) \mathrm{Acc}_{h}(\boldsymbol{x}) , which serves as a stable proxy for the model’s mastery of the specific problem (implementation details in Section 3.4 ). A question is classified as high-difficulty ( 𝒟 h \mathcal{D}_{h} ) if its historical accuracy falls below the global average accuracy of the entire dataset:

[48] table: (10) 𝒟 h = { 𝒙 ∈ 𝒟 | Acc h ​ ( 𝒙 ) < 1 | 𝒟 | ​ ∑ 𝒙 ′ ∈ 𝒟 Acc h ​ ( 𝒙 ′ ) } . \mathcal{D}_{h}=\left\{\boldsymbol{x}\in\mathcal{D}\;\middle|\;\mathrm{Acc}_{h}(\boldsymbol{x})<\frac{1}{|\mathcal{D}|}\sum_{\boldsymbol{x}^{\prime}\in\mathcal{D}}\mathrm{Acc}_{h}(\boldsymbol{x}^{\prime})\right\}.

[49] p: This dynamic thresholding ensures that the definition of “difficulty” evolves as the model improves.

[50] h4: Selective Regularization Mechanism.

[51] p: Based on the difficulty classification, we apply entropy regularization selectively to prevent premature convergence on hard problems. We employed two distinct forms of entropy regularization, respectively.

[52] p: First, following standard RL practice, we augment the training objective with the entropy-maximization term in Eq. 5 . We use a cosine annealing schedule for the coefficient λ ⁡ ( t ) \lambda(t) , but crucially, we amplify the regularization strength for hard questions. The coefficient schedule is defined as:

[53] table: (11) λ ⁡ ( 𝒙 , t ) = { 5 ⋅ λ 0 ⋅ cos ⁡ ( π ​ t T ) , 𝒙 ∈ 𝒟 h λ 0 ⋅ cos ⁡ ( π ​ t T ) , 𝒙 ∈ 𝒟 ∖ 𝒟 h \lambda(\boldsymbol{x},t)=\begin{cases}5\cdot\lambda_{0}\cdot\cos\left(\frac{\pi t}{T}\right),&\boldsymbol{x}\in\mathcal{D}_{h}\\ \lambda_{0}\cdot\cos\left(\frac{\pi t}{T}\right),&\boldsymbol{x}\in\mathcal{D}\setminus\mathcal{D}_{h}\end{cases}

[54] p: where t t is the current step and T T is the total training steps. The 5 × 5\times multiplier forces the policy to maintain a wider exploration frontier for challenging questions.

[55] p: Second, we incorporate an entropy-based advantage term ψ ⁡ ( ℋ ) \psi(\mathcal{H}) defined in Eq. 7 (following ( Wang et al., 2025b ) ) exclusively for the hard subset. The shaped advantage function becomes:

[56] table: (12) A shaped ​ ( 𝒚 i | 𝒙 , π θ ) = { A ⁡ ( 𝒚 i | 𝒙 , π θ ) + ψ ⁡ ( ℋ ) , 𝒙 ∈ 𝒟 h A ⁡ ( 𝒚 i | 𝒙 , π θ ) , 𝒙 ∈ 𝒟 ∖ 𝒟 h A^{\mathrm{shaped}}(\boldsymbol{y}^{i}|\boldsymbol{x},\pi_{\theta})=\begin{cases}A(\boldsymbol{y}^{i}|\boldsymbol{x},\pi_{\theta})+\psi(\mathcal{H}),&\boldsymbol{x}\in\mathcal{D}_{h}\\ A(\boldsymbol{y}^{i}|\boldsymbol{x},\pi_{\theta}),&\boldsymbol{x}\in\mathcal{D}\setminus\mathcal{D}_{h}\end{cases}

[57] p: With selective and difficulty-aware entropy regularization, the model sustains adequate exploration on high-difficulty problems, mitigating the performance drop that can arise when response-length reduction leads to insufficient reasoning.

[58] figure: Table 1. Performance comparison across mathematical benchmarks. Bold indicates the best score for each metric, and the accuracy in grey denotes the second-best score. Here, “ ”: prompting methods, “ ”: offline methods, “ ”: online methods. “ ∗ * ” indicates results reproduced or re-evaluated in this study. Model Name GSM8K MATH500 AIME24 AMC OlymBench AIME25 ACC LEN NAG ↓ \downarrow ACC LEN NAG ↓ \downarrow ACC LEN NAG ↓ \downarrow ACC LEN NAG ↓ \downarrow ACC LEN NAG ↓ \downarrow ACC LEN NAG ↓ \downarrow Qwen2.5-7B-Ins 90.9 279.0 0.3 74.2 567.0 17.24 12.0 1016.0 72.46 47.5 801.0 42.0 39.2 827.0 37.85 7.6 1240.0 74.67 Qwen2.5-7B-Math 93.2 439.0 -1.84 63.4 740.0 27.33 19.0 1429.0 57.99 62.5 1022.0 25.41 31.5 1037.0 48.14 4.0 2562.0 77.99 Qwen2.5-7B-Math-Ins 95.2 323.0 -3.88 81.4 670.0 9.81 10.3 1363.0 74.23 60.0 1029.0 27.99 38.9 1027.0 37.69 9.3 2087.0 67.17 R1-Distill-Qwen2.5-7B* 91.2 1479 – 91.3 3701 – 50.6 10382 – 86.9 5646 65.5 7413 – 36.7 10958 – + ThinkSwitcher 92.5 1389.0 -0.35 91.3 3495.0 0.0 48.3 7936.0 2.21 – – – 57.0 5147.0 7.17 37.5 6955 -1.32 + Dynasor-CoT 89.6 1285.0 0.64 89.4 2661.0 1.1 46.7 12695.0 85.0 5980.0 – – – – – – + DEER 90.6 917.0 0.41 89.8 2143.0 1.07 49.2 9839.0 0.63 85.0 4451.0 1.01 – – – – – – + Spirit 87.2 687.0 3.21 90.8 1765 0.4 38.3 6926 14.02 – – – – – – – – – + ConCISE-SimPO 92.1 715.0 -0.71 91.0 1945.0 0.23 48.3 7745.0 2.29 – – – – – – – – – + DAST 86.7 459 4.1 89.6 2162.0 1.2 45.6 7578.0 5.14 – – – – – – – – – + AutoThink – – – 91.2 2146.0 0.07 54.8 8051.0 -3.93 83.3 4645.0 1.74 56.4 5498.0 7.06 – – – + LC-R1 88.1 450 2.84 90.4 1568 0.75 – – – 79.1 3453 5.59 58.7 4041 7.0 36.2 7150 0.8 + Length-Penalty* 91.6 931.0 -0.27 91.4 2696.0 -0.06 50.2 9517.0 0.23 85.0 4937.0 0.77 64.8 6411.0 0.39 35.6 10173.0 0.8 + CEEH -EA 91.3 723.0 -0.08 91.7 2327.0 -0.27 53.5 7543.0 -3.0 88.1 4014.0 -0.74 66.3 5253.0 -0.66 37.1 8327.0 -0.53 + CEEH -ME 91.3 646.0 -0.08 92.1 2170.0 -0.56 53.8 6824 -3.7 87.3 3474 -0.29 66.9 4383 -1.37 36.3 7311.0 0.63 R1-Distill-Qwen2.5-1.5B* 84 1879 – 81.5 4772 – 27.7 12164 – 65.5 8127 – 41.5 8957 – 21.7 11981 – + AutoThink – – – 84 2195 -2.25 34.6 9514.0 -11.63 67.0 5059.0 -1.41 44.8 5559.0 -4.9 – – – + LC-R1 80.2 621 3.7 79.3 1822 2.12 – – – 59.0 3591 7.41 42.7 3780 -2.2 20.8 5953 2.94 + CEEH -EA 85.8 997 -1.47 83.6 2497.0 -1.78 29.8 7713 -4.59 72.3 4044 -7.36 44.7 4693 -5.32 24 7350 -6.59 + CEEH -ME 85.6 1001.0 -1.3 83.8 3067.0 -1.69 28.5 8511 -1.58 72.6 5078.0 -6.64 44.3 5469.0 -4.21 23.1 8390.0 -3.53

[59] h3: 3.3. Dynamic Optimal-Length Penalty

[60] p: Prior length-penalty methods are mainly based on either discouraging deviations from a predefined target length or applying penalties through inter-group length normalization and comparison. The former relies on hand-specified priors that often do not transfer across datasets or tasks. The latter can behave poorly when the average response length of the group is large, since it may assign positive advantage to overly long outputs, thereby weakening the compression signal and reducing training efficiency. These issues are further amplified when entropy regularization is used: to maintain accuracy on difficult questions, the model may produce longer responses. In addition, because response lengths often decrease substantially over the course of training, the penalties based on the target length can become highly non-stationary across phases, which typically requires additional tuning of the penalty coefficient.

[61] p: To address these limitations, we propose a question-level length penalty based on a dynamically updated optimal length. Specifically, for a question 𝒙 \boldsymbol{x} , we track the shortest length among all historically correct responses, denoted by L 𝒙 L_{\boldsymbol{x}} , and update it online throughout training. To encourage the model to produce correct solutions with the minimum amount of tokens, we only penalize the length of the correct responses. We define the length penalty as:

[62] table: (13) R l ​ e ​ n ( 𝒚 i | 𝒙 , π θ ) = L 𝒙 , 𝒚 i − L 𝒙 L 𝒙 ⋅ 𝕀 [ a i = a ⋆ ] . R_{len}(\boldsymbol{y}^{i}|\boldsymbol{x},\pi_{\theta})=\frac{L_{\boldsymbol{x},\boldsymbol{y}^{i}}-L_{\boldsymbol{x}}}{L_{\boldsymbol{x}}}\cdot\mathbb{I}\left[a^{i}=a^{\star}\right].

[63] p: Where 𝕀 ⁡ ( ⋅ ) \mathbb{I}(\cdot) is the indicator function. Meanwhile, we apply length penalties at the question level by enabling the penalty only when the current accuracy for the given question exceeds its historical estimate, i.e., Acc ​ ( 𝒙 ) > Acc h ​ ( 𝒙 ) \mathrm{Acc}(\boldsymbol{x})>\mathrm{Acc}_{h}(\boldsymbol{x}) . This design enables the model to compress its reasoning process while preserving its original performance. To avoid reversing the reward relationship between correct and incorrect answers, we clip the minimum value of the length term to − 0.9 -0.9 , so that the length penlty lies in the range [ − 0.9 , 1 ) [-0.9,1) . The total reward used for RL training is:

[64] table: (14) R t ​ o ​ t ​ a ​ l ​ ( 𝒚 i | 𝒙 , π θ ) = R ⁡ ( 𝒚 i | 𝒙 , π θ ) − β ​ R l ​ e ​ n ​ ( 𝒚 i | 𝒙 , π θ ) , R_{total}(\boldsymbol{y}^{i}|\boldsymbol{x},\pi_{\theta})=R(\boldsymbol{y}^{i}|\boldsymbol{x},\pi_{\theta})-\beta R_{len}(\boldsymbol{y}^{i}|\boldsymbol{x},\pi_{\theta}),

[65] p: where β \beta controls the strength of the length term.

[66] p: Since the question-level optimal length typically decreases over training in tandem with the overall reduction in average response length, it provides a stable and well-calibrated penalty signal across training phases. Moreover, when entropy regularization causes response lengths to increase for certain questions, the shorter optimal length as the denominator yields a more discriminative penalty, strengthening the compression signal precisely when length inflation occurs.

[67] h3: 3.4. Implementation

[68] p: We include several implementation details that are important for reproducing our results.

[69] p: Firstly, to match the work of entropy-based advantage ( Cheng et al., 2025a ) , we adopt the Clip-Higher strategy by increasing the upper clipping threshold to 0.28, which empirically promotes policy exploration. DAPO ( Yu et al., 2025 ) first adopts this technique to relax the constraint on increasing the probabilities of low-probability exploratory tokens, thereby encouraging broader exploration.

[70] p: Secondly, we update the per-question accuracy estimates using an asymmetric exponential moving average (EMA):

[71] table: (15) Acc h ​ ( 𝒙 ) ← ( 1 − η 𝒙 ) ​ Acc h ​ ( 𝒙 ) + η 𝒙 ​ Acc ​ ( 𝒙 ) , \mathrm{Acc_{h}}(\boldsymbol{x})\leftarrow(1-\eta_{\boldsymbol{x}})\,\mathrm{Acc_{h}}(\boldsymbol{x})+\eta_{\boldsymbol{x}}\,\mathrm{Acc}(\boldsymbol{x}),

[72] p: where the update rate η 𝒙 \eta_{\boldsymbol{x}} is defined as

[73] table: (16) η 𝒙 = { 0.2 , Acc h ​ ( 𝒙 ) < Acc ​ ( 𝒙 ) 0.05 , Acc h ​ ( 𝒙 ) ≥ Acc ⁡ ( 𝒙 ) \eta_{\boldsymbol{x}}=\begin{cases}0.2,&\mathrm{Acc_{h}}(\boldsymbol{x})<\mathrm{Acc}(\boldsymbol{x})\\ 0.05,&\mathrm{Acc_{h}}(\boldsymbol{x})\geq\mathrm{Acc}(\boldsymbol{x})\end{cases}

[74] p: and Acc ⁡ ( 𝒙 , t ) \mathrm{Acc}(\boldsymbol{x},t) denotes the accuracy of question 𝒙 \boldsymbol{x} at the current training step t t . This smooths the inherently noisy accuracy measurements arising from stochastic sampling and finite K K rollouts, yielding a more stable difficulty signal for selective entropy regularization and reducing oscillations in the set of questions classified as hard ones across training steps.

[75] p: Finally, following ( Arora and Zanette, 2025 ) , we do not apply advantage standardization; instead, we only subtract a reward-mean baseline. This avoids the scale distortion introduced by normalizing with the reward standard deviation, which can inadvertently attenuate the effect of the length term and make the length-penalty coefficient less effective for controlling response length.

[76] h2: 4. Experiments

[77] h3: 4.1. Setup

[78] h4: Datasets and Models

[79] p: We adopt the verl framework ( Sheng et al., 2025 ) for reinforcement learning training. We randomly sample 2500 instances from each of the DeepMath103K ( He et al., 2025 ) and DAPO ( Yu et al., 2025 ) datasets, merge them to construct the training set, and use R1-distill-Qwen-2.5-7B ( DeepSeek-AI, 2025 ) as the base model. The trained model is evaluated on GSM8K ( Cobbe et al., 2021 ) , Math-500 ( He et al., 2025 ) , AIME24, AIME25, AMC23, and OlympiadBench ( He et al., 2024 ) . To mitigate the impact of sampling randomness, we set the sampling temperature to 0.6 and perform 16 independent rollouts, reporting the average accuracy avg@16. Similarly, we report the average number of generated tokens to demonstrate the effectiveness of our method in compressing reasoning.

[80] figure: Figure 3. Training dynamics of policy entropy for R1-Distill-Qwen2.5-7B under different length penalty coefficients. (Left: Maximum-entropy loss ( CEEH -ME); Right: Entropy-based advantage ( CEEH -EA)).

[81] h4: Baseline

[82] p: We consider three representative paradigms as baselines for a comprehensive comparison: (1) Prompting-based methods : ThinkSwitcher ( Liang et al., 2025 ) trained a lightweight switching module with supervision signals to dynamically switch between short and long CoT modes based on task complexity; Dynasor-CoT ( Fu et al., 2025 ) and DEER ( Yang et al., 2025 ) propose approaches for dynamic reasoning termination. (2) Offline methods : Spirit ( Cui et al., 2025b ) and ConCISE-SimPO ( Qiao et al., 2025 ) utilize self-generated responses to compress reasoning via confidence scores or preference optimization; DAST ( Shen et al., 2025 ) introduces a difficulty metric and applies budget-aware reward shaping together with budget preference optimization. (3) Online RL methods : AutoThink ( Tu et al., 2025 ) progressively refines reasoning strategies through staged reward shaping, achieving favorable accuracy–efficiency trade-offs; LC-R1 ( Cheng et al., 2025b ) compresses reasoning by sampling target lengths for each question and applying length-based rewards to encourage generations that match these targets; Length-Penalty ( Arora and Zanette, 2025 ) assigns inter-group length rewards using normalized response lengths, providing a richer length-control signal for optimizing generation length. We report results from the original papers or subsequent evaluations when available, and we additionally reproduce Length-Penalty under the same training data used in our experiments. We denote CEEH -EA as using the entropy-based advantage for entropy regularization, and CEEH -ME as using the maximum-entropy loss for entropy regularization. In addition, we also included some instruction models in the comparison, such as Qwen2.5-Math ( Yang et al., 2024 ) .

[83] figure: Table 2. Pass@ k k performance of different methods trained from R1-Distill-Qwen2.5-7B. Pass@ k k is computed using 16 rollouts per question. Model Name GSM8K MATH500 AIME24 AMC OlymBench AIME25 Base Model 97.8 97.2 80 97.5 81.8 63.3 Length-Penalty 97.6 97 76.7 97.5 81.8 63.3 CEEH -EA 98.1 97.2 80 97.5 82.4 63.3 CEEH -ME 98.3 97.2 80 97.5 82.2 70

[84] h4: Metrics

[85] p: We report the accuracy with avg@16 and the tokens of responses, denoted as ACC and LEN. Prior work often evaluates reasoning compression primarily through length-based metrics. Since our goal is to compress reasoning length without sacrificing task performance, we introduce a metric that jointly accounts for length and accuracy relative to the base model. Following prior work ( Liu et al., 2025 ) , we define Normalized Accuracy Gain (NAG) as:

[86] table: (17) NAG = ( 1 − A ​ c ​ c / A ​ c ​ c b ) × 100 / 1 − L / L b \text{NAG}=(1-Acc/Acc_{b})\times 100/\sqrt{1-L/L_{b}}

[87] p: where A ​ c ​ c b Acc_{b} and L b L_{b} denote the accuracy and average response length of the base model. If the response length L L is large than the reference length L b L_{b} , we do not compute this metric since it does not compress the reasoning progress. Intuitively, this metric quantifies how much accuracy is sacrificed per unit reduction in response length, balancing performance degradation against efficiency gains. Compared to other indicators, this metric emphasizes changes in relative proportions rather than absolute magnitudes.

[88] h3: 4.2. Main Results

[89] p: CEEH can compress reasoning without sacrificing model accuracy. Table 1 summarizes performance and token efficiency across six reasoning benchmarks. Overall, CEEH provide a more reliable trade-off between reasoning compression and accuracy preservation than prompting-based, offline, or online optimization baselines. In particular, both entropy regularization variants consistently and substantially reduce response length, while maintaining accuracy comparable to or even better than that of the base model. This indicates that CEEH can compress reasoning without systematically sacrificing correctness.

[90] figure: Figure 4. Training accuracy on the same dataset, with R1-Distill-Qwen2.5-7B as the base model.

[91] p: CEEH is more robust across tasks. The compression effect of CEEH generalizes across tasks with diverse difficulties and reasoning styles, rather than being benchmark-specific: both entropy-regularization variants reduce total response tokens by over 30%. Prompting-based and offline methods can shorten responses on select benchmarks, but their accuracy tends to fluctuate more. Among online methods, Length-Penalty exhibits substantial variability in token reduction across datasets, while AutoThink shows considerable discrepancies in accuracy across benchmarks. In addition, CEEH achieve strong compression while also attaining the best or the second-best accuracy on several benchmarks. These results demonstrate that efficiency gains need not come at the expense of accuracy when exploration is appropriately controlled.

[92] p: CEEH achieves better performance improvements on stronger models. Table 1 shows that CEEH attains a better trade-off between accuracy and response length on R1-Distill-Qwen2.5-7B. When trained on R1-Distill-Qwen2.5-1.5B, LC-R1 generates more concise responses but falls below the base model in accuracy. In contrast, AutoThink achieves shorter responses while even improving accuracy. One plausible explanation is that weaker models have more headroom to benefit from RL fine-tuning, whereas stronger models are harder to improve in accuracy. Moreover, their higher baseline accuracy yields denser length-related reward signals, which encourages the policy to focus more on compressing reasoning. As a result, many methods can further shorten responses only by trading off correctness. Although CEEH is not the top performer on some R1-Distill-Qwen2.5-1.5B benchmarks, it consistently reduces response length while preserving accuracy across model scales.

[93] h3: 4.3. Feature Analysis of Training Dynamics

[94] p: In this subsection, we analyze the training dynamics to understand when and why our method is effective, focusing on policy-entropy evolution, Pass@ k k performance, and training accuracy trends.

[95] h4: Dynamics of Policy Entropy

[96] p: How does the model’s policy entropy evolve during training? Revisiting our motivation, we aim for the model’s policy entropy to increase on difficult problems to ensure sufficient exploration. Figure 3 illustrates the evolution of entropy during training under different entropy regularization terms and length penalty coefficients. When using the maximum-entropy loss, the additional entropy regularization leads to an increase in policy entropy.Consequently, the policy entropy rises in the early stage of training. However, since we apply cosine annealing to the entropy regularization coefficient, the policy entropy decreases in the later stage of training. Applying entropy regularization only to difficult problems helps avoid entropy explosion ( Cui et al., 2025a ) , keeping the overall entropy under control. While using entropy-based advantages, the method inherently encourages the generation of high-entropy tokens while keeping reward advantages dominant, enabling adaptive entropy adjustment. As a result, the model’s policy entropy remains relatively stable in the early training stage. In the later stage, as accuracy improves, the contribution of entropy-based advantages becomes smaller, and the entropy gradually decreases.

[97] figure: Figure 5. Distribution of response token counts on AMC23, with R1-Distill-Qwen2.5-7B as the base model.

[98] h4: Impact of the Length-Penalty Coefficient on Policy Entropy

[99] p: How does the length penalty coefficient affect policy entropy? Figure 3 shows that, for both entropy regularization variants, increasing the length penalty coefficient consistently reduces policy entropy. Intuitively, stronger contraint toward shorter outputs narrows the model’s action distribution, encouraging more deterministic token choices. This effect is particularly pronounced under on-policy RL, where updates reinforce the model’s current generations with high confidence. This trend supports our claim that optimizing for length alone accelerates entropy collapse, limits exploration, and can ultimately result in accuracy sacrifice.

[100] h4: Pass@k Performance

[101] p: Can CEEH improves the model’s underlying reasoning capability? Prior work ( Chen et al., 2025c ; Cheng et al., 2025a ) highlights policy entropy as a key factor governing Pass@ k k performance, which is commonly considered as an upper-bound estimator for the true reasoning capabilities of an LLM. Motivated by this connection, we analyze why our difficulty-aware entropy regularization can preserve accuracy while compressing reasoning, from the perspective of Pass@ k k . Table 2 compares Pass@ k k for CEEH against the base model and the Length-Penalty baseline. Notably, Length-Penalty consistently degrades Pass@ k k by optimizing solely for reasoning compression, even on the AIME datasets where the reduction in response length is relatively modest. In contrast, CEEH maintains adequate exploration on challenging instances, leading to improved Pass@ k k and an avg@16 gain. These results suggest that CEEH enhances inference ability via reasonable entropy control, rather than merely increasing the model’s confidence in its own predictions.

[102] figure: Figure 6. The dynamics of response length during training with R1-Distill-Qwen2.5-7B as the base model. (Left: Maximum-entropy loss ( CEEH -ME); Right: Entropy-based advantage ( CEEH -EA).

[103] figure: Table 3. Performance under different length penalty coefficients. Model Name MATH500 AIME24 AIME25 ACC LEN NAG ↓ \downarrow ACC LEN NAG ↓ \downarrow ACC LEN NAG ↓ \downarrow Base Model 91.3 3701 – 50.6 10382 – 36.7 10958 – EA with η \eta = 0.1 91.7 2170 -1.36 53.5 7543 -10.96 37.1 8327 -2.22 EA with η \eta = 0.2 91.2 1870 0.16 50.6 7172 0.0 36.9 8241 -1.09 ME with η \eta = 0.1 92.1 2170 -1.36 53.8 6824 -10.8 36.3 7311 1.89 ME with η \eta = 0.2 91.4 2003 -0.16 51.7 6658 -3.63 36.5 7142 0.91

[104] h4: Training Accuracy

[105] p: Difficulty-aware entropy regularization improves data efficiency. Figure 4 highlights a distinct performance gap: CEEH (equipped with maximum-entropy loss) consistently surpasses the standard Length-Penalty baseline in training accuracy. Our approach consistently attains higher training accuracy, which can be attributed to high-entropy exploration on challenging questions, enabling more effective learning from the same data. Meanwhile, by applying length penalties selectively based on historical question accuracy, our approach extracts a richer learning signal from the same number of rollouts, demonstrating significantly improved data efficiency and a more robust training trajectory compared to the uniform penalty strategy.

[106] h3: 4.4. Ablation Study

[107] p: In this subsection, we conduct ablation studies of the proposed method, examining different forms of entropy regularization and the effect of the length-penalty coefficient.

[108] h4: Entropy Regularization Form

[109] p: Entropy-based advantage allocates more reasoning budget to intractable questions. In Table 1 , we observe that CEEH -EA produces longer average responses than CEEH -ME . To better understand this difference, we analyze by examining the distribution of response lengths on AMC23, as shown in Figure 5 . The EA variant tends to allocate more generation budget to difficult questions, sometimes reaching the maximum response length on instances it still fails to solve. This behavior stems in part from intrinsic tendency toward length expansion of entropy-based advantage technique ( Cheng et al., 2025a ) and in part from its explicit encouragement of high-entropy token generation. As a result, the model assigns higher probability mass to connective tokens that is critical for reasoning and facilitates reflection, which can prolong inference trajectories.

[110] h4: The coefficient of Entropy Regularization

[111] p: Strong length penalties can suppress the benefits of entropy regularization, yet accuracy remains comparable to the base model. We conduct an ablation study on the length-penalty coefficient. Intuitively, a larger length penalty will further compress the reasoning process, but also risk degrading accuracy. As shown in Figure 6 , for both entropy-regularization variants, increasing the length penalty consistently yields shorter reasoning on the training set. However, Table 3 indicates that under EA, responses to challenging questions still remain relatively long even with larger penalties, consistent with our earlier analysis that EA allocates more budget to hard instances. Consequently, although aggressive length penalties induce a marginal decline in accuracy compared to milder settings, the performance does not collapse. Instead, it remains comparable to the base model, suggesting that our method successfully guides the model to prune redundant “fluff” tokens while retaining the critical reasoning steps necessary for correct deduction.

[112] h2: 5. Related Work

[113] h4: Reasoning Compression

[114] p: The substantial inference cost associated with excessive tokens and redundant intermediate reasoning has motivated recent work on compressing reasoning processes. In the earlier stage, several approaches leverage the model’s own output as supervision signals to compress the reasoning process ( Munkhbat et al., 2025 ; Chen et al., 2024 ; Xia et al., 2025 ; Huang et al., 2025 ) . Chen et al. (2024) samples multiple responses generated by the model itself to perform DPO ( Rafailov et al., 2023 ) , allowing the learning of length-aware preferences. FS-BoN ( Munkhbat et al., 2025 ) leverages self-generated concise reasoning paths obtained by best-of-N sampling for subsequent fine-tuning. SEER ( Huang et al., 2025 ) generates CoT rationales and answers, discards incorrect outputs, and fine-tunes iteratively on the correct rationale–answer pairs, reaching reasoning performance comparable to models that are thirty times larger. TokenSkip ( Xia et al., 2025 ) employs another LLM to estimate the semantic importance of individual CoT tokens, and select tokens of high importance to generate compressed training data. More recently, RL has been increasingly used to explicitly control reasoning length in LLMs. These approaches typically rely on multi-stage training paradigms or the incorporation of length-aware reward signals. Thinkless ( Fang et al., 2025 ) constructs a dataset of short-term and long-term reasoning trajectories distinguished by designated control tokens, enabling the model to learn token-based switches that activate different reasoning modes. AutoThink ( Tu et al., 2025 ) progressively refines reasoning strategies through staged reward shaping, achieving favorable accuracy–efficiency trade-offs. More generally, incorporating length-related penalty terms into the RL objective has become a common design choice. FEDH ( Ling et al., 2025 ) and DR. SAF ( Chen et al., 2025a ) rely on human-defined length priors to encourage compressed reasoning, while Length-Penalty ( Arora and Zanette, 2025 ) and LC-R1 ( Cheng et al., 2025b ) design adaptive length penalties based on inter-group length comparisons among the generated outputs. These methods are often constrained by manually specified length priors or struggle to balance accuracy and reasoning length, which limits their scalability. In contrast, CEEH adaptively compresses reasoning within a single training phase while preserving the performance.

[115] h4: Entropy Regularization

[116] p: Recently, several studies have investigated the phenomenon of entropy collapse in reinforcement learning with verifiable rewards (RLVR) ( Yu et al., 2025 ; Jiang et al., 2025 ; Cui et al., 2025a ; Park et al., 2025 ) . A key empirical finding is the trade-off between policy entropy and task performance ( Cui et al., 2025a ) , which has motivated renewed interest in entropy regularization as a mechanism for stabilizing training and improving generalization. Subsequent work has primarily focused on dynamically modulating policy entropy ( Cui et al., 2025a ; Wang et al., 2025a ; Jiang et al., 2025 ; Tang et al., 2025 ) during RL learning progress to preserve exploratory behavior and improve model performance. Representative methods include unbalanced clipping of positive and negative advantages ( Yu et al., 2025 ; Park et al., 2025 ; Zhu et al., 2025 ) , decoupled optimization strategies for high-entropy tokens ( Cao et al., 2025 ; Jiang et al., 2025 ; Li et al., 2025 ) , and the explicit optimization of entropy-related advantage terms ( Zhang et al., 2025 ; Cheng et al., 2025a ) . Recent analyses of positive and negative samples ( Zhu et al., 2025 ; Tang et al., 2025 ) provide an informative perspective on why reasoning compression is challenging for strong LLMs like R1-distill-Qwen-2.5-7B. In particular, optimizing on positive samples tends to reduce policy entropy ( Zhu et al., 2025 ) , and token-level schemes that emphasize high-entropy tokens in positive samples or low-entropy tokens in negative samples can still drive entropy downward ( Tang et al., 2025 ) . In strong LLMs, these effects are amplified by high baseline accuracy and confidence, which make the on-policy distribution increasingly peaked during RL updates. Consequently, RL-based length optimization on strong models often exhibits a pronounced trade-off between accuracy and response length, accompanied by rapid decay of the policy entropy. Moreover, prior studies have demonstrated that maintaining an appropriate level of entropy can substantially improve Pass@ k k performance ( Wang et al., 2025b ; Zhu et al., 2025 ; Chen et al., 2025c ) , suggesting a deeper impact on the model’s reasoning ability ( Yue et al., 2025 ) . However, a recurring empirical observation in these works is that response lengths tend to increase as performance improves, particularly when additional entropy regularization is introduced ( Wang et al., 2025b ; Cui et al., 2025a ; Cheng et al., 2025a ) , which conflicts with our objective of compressing the reasoning process. To resolve this tension, we selectively apply entropy regularization at the question level based on model-dependent difficulty, preserving model performance while explicitly biasing learning toward shorter and more compact reasoning trajectories.

[117] h2: 6. Conclusion

[118] p: This work identifies entropy collapse as a central obstacle in RL-based reasoning compression: aggressively optimizing for brevity shrinks the effective exploration space, which is particularly harmful for difficult questions that require diverse intermediate hypotheses or alternative reasoning paths. Consequently, this collapse limits the benefits of RL and induces accuracy degradation under tighter length budgets. To address this failure mode, we introduce CEEH , which explicitly separates where to compress and where to explore. The key idea is to preserve exploration on questions that are currently hard for the model via difficulty-aware selective entropy regularization, while allowing easy questions to be compressed more aggressively. CEEH further stabilizes length control with a question-level dynamic optimal-length penalty that anchors compression to the historically shortest correct trajectory for each question. By penalizing correct responses relative to this per-question reference, the length signal remains stable even as response-length distributions shift over training and remains effective when entropy regularization temporarily inflates length on hard instances. Across six reasoning benchmarks, CEEH consistently reduces response length while maintaining accuracy comparable to the base model, and it improves Pass@ k k relative to length-only optimization, which supports the claim that principled entropy control during compression preserves genuine reasoning capability rather than merely amplifying confidence.

[119] h2: References

[120] h2: Appendix A Experimental Setup

[121] p: We utilize the verl framework ( Sheng et al., 2025 ) for RL training. To reduce memory overhead, we fine-tune the model with LoRA ( Hu et al., 2022 ) on two nodes (16 A100 GPUs in total). Table 4 reports the training hyper-parameters, with the specific settings highlighted in bold.

[122] figure: Parameter Name Value advantage estimator grpo training batch size 512 max prompt length 2048 max response length 20480 ppo mini batch size 32 ppo micro batch size per gpu 2 log prob micro batch size per gpu 4 use kl loss True kl loss coefficient 0.001 entropy coeff 0.001 for ME (0 for EA) model parallel size 2 gpu utilization 0.8 rollout num per question 12 lora rank 32 lora alpha 32 clip ratio high 0.28 learning rate 3e-5 temperature 0.6 Table 4. Main Parameters of the VERL Training Framework

[123] p: Similarly, we utilize the verl framework for validation experiments without specific settings and report the validation-related hyper-parameters in Table 5 .

[124] figure: Parameter Name Value validation batch size 256 validation temperature 0.6 top_p 0.95 rollout num per question 16 max prompt length 2048 max response length 16000 model parallel size 2 gpu utilization 0.9 Table 5. Validation Parameters of the VERL Training Framework

[125] h2: Instructions for reporting errors

[126] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[127] p: Tip: You can select the relevant text first, to include it in your report.

[128] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[129] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
