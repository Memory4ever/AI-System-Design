[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Enhancing Multi-Modal LLMs Reasoning via Difficulty-Aware Group Normalization

[3] h6: Abstract

[4] p: Reinforcement Learning with Verifiable Rewards (RLVR) and Group Relative Policy Optimization (GRPO) have significantly advanced the reasoning capabilities of large language models. Extending these methods to multimodal settings, however, faces a critical challenge: the instability of std -based normalization, which is easily distorted by extreme samples with nearly positive or negative rewards. Unlike pure-text LLMs, multimodal models are particularly sensitive to such distortions, as both perceptual and reasoning errors influence their responses. To address this, we characterize each sample by its difficulty , defined through perceptual complexity (measured via visual entropy) and reasoning uncertainty (captured by model confidence). Building on this characterization, we propose d iffic u lty-awa r e group normal i z a tio n (Durian) , which re-groups samples by difficulty levels and shares the std within each group. Our approach preserves GRPO’s intra-group distinctions while eliminating sensitivity to extreme cases, yielding significant performance gains across multiple multimodal reasoning benchmarks.

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] figure: Figure 1 : The advantage distribution after the normalization of reward varies among samples. Extreme samples like easy and hard ones are amplified after std -normalization, whereas medium samples exhibit more balanced advantages.

[8] p: Reinforcement Learning with Verifiable Rewards (RLVR) has enabled significant advances in the reasoning capabilities of both large language models (LLMs) ( DeepSeek-AI et al., 2025 ; Yang et al., 2025a ; Lambert et al., 2024 ) and multi-modal large language models (MLLMs) ( Zhang et al., 2025b ; Huang et al., 2025a ) . Within this paradigm, Group Relative Policy Optimization (GRPO) ( Shao et al., 2024 ) demonstrates strong performance by applying standard deviation ( std )-based normalization to rewards within each response group. This std -based normalization rescales intra-group distinctions between positive and negative responses, thereby stabilizing training.

[9] p: Despite these advances, we observe that the std -based normalization suffers from a critical limitation: sensitive to extreme samples — those with response groups that are almost entirely positive or negative . Specifically, when rewards in a group collapse to near 0 or 1, the resulting low std overemphasizes the extreme samples during optimization. Meanwhile, samples with more balanced rewards are neglected, leading to imbalanced optimization. This issue is particularly pronounced in MLLMs, where the complexity of multimodal inputs increases the occurrence of such extreme samples. As illustrated in Figure 1 , MLLM responses are jointly influenced by challenges from perceptual complexity and reasoning uncertainty, making them more susceptible to extreme reward distributions.

[10] p: A straightforward solution is to remove the std term thereby mitigating the risk of overfitting to extreme samples ( Liu et al., 2025b ) . However, it simultaneously discards the valuable intra-group distinctions, which are essential for effective and stable optimization. Therefore, the key issue lies not in the std-normalization term itself, but rather in the way groups are constructed : when group size is small, extreme cases become inevitable. Enlarging group sizes during rollouts could help, but it incurs prohibitive computational costs.

[11] p: Motivated by this, we propose to account for the challenges of various samples, which we refer to as Durian: difficulty-aware re-grouping . We characterize each sample’s difficulty from two complementary perspectives: (i) a data-centric view, where the entropy of the image reflects perceptual difficulty ; and (ii) a model-centric view, where the confidence in model responses reflects reasoning difficulty . By re-grouping samples according to these difficulty levels and sharing the std within each group, our method preserves intra-group distinctions while mitigating sensitivity to extreme cases. Specifically, our difficulty-based re-group strategy is achieved by:

[12] p: Perceptual difficulty-based regrouping. We quantify perceptual difficulty through spectral analysis of image patch covariances, where higher entropy in the resulting eigenvalue distribution indicates greater visual complexity ( Grzywacz, 2025 ) . Images with more diverse and complex visual patterns exhibit higher entropy, reflecting greater perceptual difficulty.

[13] p: Reasoning difficulty-based regrouping. Leveraging the insight that token-level log probabilities reflect reasoning confidence ( Yu et al., 2025c ) , we measure reasoning difficulty through the model’s token-level confidence, where lower average log probabilities indicate greater uncertainty in generating correct reasoning chains, reflecting higher reasoning difficulty.

[14] p: In summary, by explicitly decomposing difficulty into data-centric ( perceptual ) and model-centric ( reasoning ) groups, Durian allows each group of samples to share separate std s for perceptual and reasoning aspects. These normalized advantages are then combined to effectively integrate intrinsic data complexity and model uncertainty, ensuring stable optimization that preserves meaningful intra-group distinctions. To validate Durian, we conduct a comprehensive evaluation comparing it with leading methods on multiple benchmarks, and experimental results demonstrate that Durian attains more than 11.3% average performance improvements.

[15] h2: 2 Preliminary

[16] figure: Figure 2 : Overview of two difficulty-based regrouping strategies of Durian. Upper: For perceptual difficulty, we extract image patch features through the visual encoder and compute patch covariance matrices, whose eigenvalue entropy characterizes visual complexity. Bottom: For reasoning difficulty, model confidence is estimated from normalized sequence-level log probabilities across multiple rollouts. In both strategies, samples in the same group share the same std .

[17] p: In this section, we introduce the key concepts and training setup for multimodal reasoning under RLVR ( DeepSeek-AI et al., 2025 ) . We first formulate the task, and then revisit the standard GRPO framework ( Shao et al., 2024 ) and its improved variant, Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO) ( Yu et al., 2025b ) .

[18] h3: 2.1 Task Formulation

[19] p: We consider the problem of multimodal reasoning under the RLVR paradigm. Let { ℐ , 𝒬 } ∈ 𝒟 \{\mathcal{I,Q}\}\in\mathcal{D} denote a multimodal input, where the dataset 𝒟 \mathcal{D} includes image ℐ \mathcal{I} and text question 𝒬 \mathcal{Q} . The model generates a reasoning response o o given { ℐ , 𝒬 } \{\mathcal{I},\mathcal{Q}\} and receives a verifiable reward r {r} based on the correct answer y y ( Wu et al., 2025 ; Wang et al., 2025a ) . The response o o typically contains both the reasoning steps and the final answer, with the reasoning steps enclosed in <think>...</think> and the final answer enclosed in \boxed{} . We employ a binary reward function, where r ⁡ ( o , y ) = 1 r(o,y)=1 if the final answer is equal to the correct answer y y , and r ⁡ ( o , y ) = 0 r(o,y)=0 otherwise. The reasoning process is modeled as a policy π θ ​ ( o | ℐ , 𝒬 ) \pi_{\theta}(o|\mathcal{I,Q}) parameterized by θ \theta to maximize the expected reward:

[20] table: 𝒥 RLVR ( θ ) = max θ 𝔼 { ℐ , 𝒬 } ∼ 𝒟 𝔼 o ∼ π θ ( ⋅ ∣ ℐ , 𝒬 ) [ r ( o , y ) ] . \displaystyle\mathcal{J}_{\mathrm{RLVR}}(\theta)=\displaystyle\max_{\theta}\mathbb{E}_{\{\mathcal{I,Q}\}\sim\mathcal{D}}\mathbb{E}_{o\sim\pi_{\theta}(\cdot\mid\mathcal{I,Q})}[r(o,y)]. (1)

[21] p: Our goal is to enhance the reasoning capabilities of an instruction-tuned MLLM, thereby significantly improving its performance on downstream multimodal reasoning tasks.

[22] h3: 2.2 Core Algorithms of Reinforcement Learning with Verifiable Reward

[23] p: Group Relative Policy Optimization (GRPO) is derived from Proximal Policy Optimization (PPO) ( Schulman et al., 2017 ) , with the key distinction that GRPO replaces the advantage estimates obtained via Generalized Advantage Estimation (GAE) with group-relative advantages computed from a group of outputs.

[24] p: Specifically, for each input ℐ , 𝒬 \mathcal{I,Q} , GRPO samples a group of outputs { o 1 , o 2 , … , o G } \{o_{1},o_{2},\dots,o_{G}\} from the old policy model π θ old \pi_{\theta_{\text{old}}} , with rollout size G G . The advantage of the i i -th response is computed by normalizing the rewards among the group:

[25] table: A ^ i = r i − m ​ e ​ a ​ n ​ ( { r 1 , r 2 , … , r G } ) s ​ t ​ d ​ ( { r 1 , r 2 , … , r G } ) . \displaystyle\hat{A}_{i}=\frac{r_{i}-mean(\{r_{1},r_{2},\dots,r_{G}\})}{std(\{r_{1},r_{2},\dots,r_{G}\})}. (2)

[26] p: GRPO adopts a clipped objective, together with a directly imposed KL penalty term:

[27] table: 𝒥 GRPO ( θ ) = 𝔼 ( ℐ , 𝒬 ) ∼ 𝒟 , { o i } i = 1 G ∼ π θ old ​ ( o ∣ ℐ , 𝒬 ) { 1 G ∑ i = 1 G 1 | o i | ∑ t = 1 | o i | min [ π θ ​ ( o i , t ∣ ℐ , 𝒬 , o i , < t ) π θ old ​ ( o i , t ∣ ℐ , 𝒬 , o i , < t ) A ^ i , t , clip ( π θ ​ ( o i , t ∣ ℐ , 𝒬 , o i , < t ) π θ old ​ ( o i , t ∣ ℐ , 𝒬 , o i , < t ) , 1 − ϵ , 1 + ϵ ) A ^ i , t ] − β 𝔻 K ​ L ( π θ ∥ π ref ) } . \begin{aligned} &\mathcal{J}_{\mathrm{GRPO}}(\theta)=\mathbb{E}_{(\mathcal{I,Q})\sim\mathcal{D},\{o_{i}\}_{i=1}^{G}\sim{\pi_{\theta_{\text{old}}(o\mid\mathcal{I,Q})}}}\Bigg\{\frac{1}{G}\sum_{i=1}^{G}\frac{1}{\left|o_{i}\right|}\sum_{t=1}^{\left|o_{i}\right|}\\ &\min\Bigg[\frac{\pi_{\theta}\big(o_{i,t}\mid\mathcal{I,Q},o_{i,<t}\big)}{\pi_{\theta_{\text{old}}}\big(o_{i,t}\mid\mathcal{I,Q},o_{i,<t}\big)}\,\hat{A}_{i,t},\;\mathrm{clip}\big(\frac{\pi_{\theta}\big(o_{i,t}\mid\mathcal{I,Q},o_{i,<t}\big)}{\pi_{\theta_{\text{old}}}\big(o_{i,t}\mid\mathcal{I,Q},o_{i,<t}\big)},\\ &1-\epsilon,1+\epsilon\big)\,\hat{A}_{i,t}\Bigg]-\beta\mathbb{D}_{KL}(\pi_{\theta}\|\pi_{\text{ref}})\Bigg\}.\end{aligned} (3)

[28] p: ϵ \epsilon is the hyperparameter to control the clipping range of the importance sampling ratio, and β \beta is the penalty strength of how far the current policy π θ \pi_{\theta} deviates from the reference policy π r ​ e ​ f \pi_{ref} .

[29] p: Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO) is a variant of GRPO adopting an asymmetric clipping range with a larger upper bound, dynamic sampling, token-level policy gradient loss, and overlong reward shaping. The objective function of DAPO is defined as:

[30] table: 𝒥 DAPO ( θ ) = 𝔼 ( ℐ , 𝒬 ) ∼ 𝒟 , { o i } i = 1 G ∼ π θ old ​ ( o ∣ ℐ , 𝒬 ) { 1 ∑ i = 1 G | o i | ∑ i = 1 G ∑ t = 1 | o i | min [ π θ ​ ( o i , t ∣ ℐ , 𝒬 , o i , < t ) π θ old ​ ( o i , t ∣ ℐ , 𝒬 , o i , < t ) A ^ i , t , clip ( π θ ​ ( o i , t ∣ ℐ , 𝒬 , o i , < t ) π θ old ​ ( o i , t ∣ ℐ , 𝒬 , o i , < t ) , 1 − ϵ low , 1 + ϵ high ) A ^ i , t ] } . \begin{aligned} &\mathcal{J}_{\mathrm{DAPO}}(\theta)=\mathbb{E}_{(\mathcal{I,Q})\sim\mathcal{D},\,\{o_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(o\mid\mathcal{I,Q})}\Bigg\{\frac{1}{\sum_{i=1}^{G}\lvert o_{i}\rvert}\sum_{i=1}^{G}\sum_{t=1}^{\lvert o_{i}\rvert}\\ &\min\Bigg[\frac{\pi_{\theta}\big(o_{i,t}\mid\mathcal{I,Q},o_{i,<t}\big)}{\pi_{\theta_{\text{old}}}\big(o_{i,t}\mid\mathcal{I,Q},o_{i,<t}\big)}\,\hat{A}_{i,t},\;\mathrm{clip}\bigg(\frac{\pi_{\theta}\big(o_{i,t}\mid\mathcal{I,Q},o_{i,<t}\big)}{\pi_{\theta_{\text{old}}}\big(o_{i,t}\mid\mathcal{I,Q},o_{i,<t}\big)},\\ &1-\epsilon_{\text{low}},1+\epsilon_{\text{high}}\bigg)\,\hat{A}_{i,t}\Bigg]\Bigg\}.\end{aligned} (4)

[31] h2: 3 Durian : Difficulty-based Regrouping

[32] p: In this section, we introduce our difficulty-based regrouping strategy in detail. We first represent our perceptual difficulty-based regrouping in Section 3.1 , then we describe our reasoning difficulty-based regrouping in Section 3.2 . The two regrouping strategies are summarized in Figure 2 . Finally, we show the combination of these two strategies in Section 3.3 .

[33] h3: 3.1 Perceptual Difficulty-based Regrpouping

[34] p: Perceptual difficulty estimation. To estimate the perceptual difficulty of a batch ℬ = { ( ℐ s , 𝒬 s ) } s = 1 B \mathcal{B}=\{(\mathcal{I}_{s},\mathcal{Q}_{s})\}_{s=1}^{B} , we first extract patch-level visual features from the Qwen2.5-VL-7B visual encoder 𝛀 v \mathbf{\Omega}_{v} :

[35] table: 𝐅 s = 𝛀 v ​ ( ℐ s ) ∈ ℝ P × d = [ 𝒇 s 1 , 𝒇 s 2 , ⋯ , 𝒇 s P ] ⊤ , \displaystyle\mathbf{F}_{s}=\mathbf{\Omega}_{v}(\mathcal{I}_{s})\in\mathbb{R}^{P\times d}=[\bm{f}_{s}^{1},\bm{f}_{s}^{2},\cdots,\bm{f}_{s}^{P}]^{\top}, (5)

[36] p: where P P denotes the number of spatial patches and d d is the feature dimension, with 𝒇 s j ∈ ℝ d × 1 , j = 1 , ⋯ , P \bm{f}_{s}^{j}\in\mathbb{R}^{d\times 1},j=1,\cdots,P representing the feature of the j j -th patch.

[37] p: Compared to CLIP-based representations ( Radford et al., 2021 ) , these patch-level features not only capture finer spatial granularity that preserves local details, but also align better with the downstream textual decoder 𝛀 t \mathbf{\Omega}_{t} , ensuring both stability and semantic consistency.

[38] p: We then compute the empirical covariance matrix to capture intra- and inter-patch variances:

[39] table: 𝐂 s = 1 P − 1 ( 𝐅 s − 𝟏 P 𝝁 s ⊤ ) ( 𝐅 s − 𝟏 P 𝝁 s ⊤ ) ⊤ , 𝝁 s = 1 P ∑ j = 1 P 𝒇 s j , \begin{aligned} \mathbf{C}_{s}=\tfrac{1}{P-1}\,(\mathbf{F}_{s}-\bm{1}_{P}\bm{\mu}_{s}^{\top})(\mathbf{F}_{s}-\bm{1}_{P}\bm{\mu}_{s}^{\top})^{\top},\quad\bm{\mu}_{s}=\tfrac{1}{P}\sum_{j=1}^{P}\bm{f}_{s}^{j},\end{aligned} (6)

[40] p: where 𝟏 P \bm{1}_{P} is a P × 1 P\times 1 column vector of ones and 𝝁 s \bm{\mu}_{s} is the mean of the patches feature of the ℐ s \mathcal{I}_{s} . The diagonal entries measure the variance of each feature dimension across patches, while the off-diagonal terms capture correlations between different feature dimensions. This covariance structure reveals whether visual features are dominated by a few strong dimensions or by multiple interacting factors, providing a principled basis for assessing perceptual difficulty.

[41] p: Since 𝐂 s \mathbf{C}_{s} is a symmetric positive semidefinite matrix, we perform eigenvalue decomposition for spectral analysis:

[42] table: 𝐂 s = 𝐕 s 𝚲 s 𝐕 s ⊤ , 𝚲 s = diag ( λ s 1 , … , λ s P ) , λ s k ≥ 0 . \begin{aligned} \mathbf{C}_{s}=\mathbf{V}_{s}\mathbf{\Lambda}_{s}\mathbf{V}_{s}^{\top},\quad\mathbf{\Lambda}_{s}=\mathrm{diag}(\lambda_{s}^{1},\ldots,\lambda_{s}^{P}),\;\lambda_{s}^{k}\geq 0.\end{aligned} (7)

[43] p: λ s k \lambda_{s}^{k} denotes the k k -th eigenvalue, quantifying the variance along one orthogonal principal direction. Concentrated eigenvalues indicate that most variance is captured by a few dimensions, whereas more balanced eigenvalues imply richer visual structure and higher visual complexity.

[44] p: The final perceptual difficulty score is defined as the entropy ( Shannon, 1948 ) of the normalized distribution of eigenvalues:

[45] table: H ( ℐ s ) = − ∑ k = 1 P p s k log p s k , \displaystyle H(\mathcal{I}_{s})=-\sum_{k=1}^{P}p_{s}^{k}\log p_{s}^{k}, (8)

[46] p: where p s p_{s} is the normalized probability distribution of the eigenvalues, and each element in p s p_{s} is calculated as:

[47] table: p s k = λ s k ∑ j = 1 P λ s j , with ∑ k = 1 P p s k = 1 . \displaystyle p_{s}^{k}=\tfrac{\lambda_{s}^{k}}{\sum_{j=1}^{P}\lambda_{s}^{j}},\quad\text{with}\sum_{k=1}^{P}p_{s}^{k}=1. (9)

[48] p: Here, low entropy corresponds to the visually easy sample, with variance concentrated on a few dominant components, whereas high entropy indicates the visually difficult sample, with variance distributed across many patches.

[49] p: Perceptual difficulty-based regrouping. Given the perceptual difficulty scores within a batch, we partition samples into three groups using the 25th and 75th percentiles τ 0.25 \tau_{0.25} and τ 0.75 \tau_{0.75} :

[50] table: { 𝒮 1 = { s ∣ H ( ℐ s ) ≤ τ 0.25 } , 𝒮 2 = { s ∣ τ 0.25 < H ( ℐ s ) < τ 0.75 } , 𝒮 3 = { s ∣ H ⁡ ( ℐ s ) ≥ τ 0.75 } . \begin{cases}\mathcal{S}_{1}=\{s\mid H(\mathcal{I}_{s})\leq\tau_{0.25}\},\quad\\ \mathcal{S}_{2}=\{s\mid\tau_{0.25}<H(\mathcal{I}_{s})<\tau_{0.75}\},\quad\\ \mathcal{S}_{3}=\{s\mid H(\mathcal{I}_{s})\geq\tau_{0.75}\}.\end{cases} (10)

[51] p: For each group a a , the reward set can be defined as:

[52] table: ℛ a = { r s , i ∣ i = 1 , ⋯ , G , s ∈ 𝒮 a } , a ∈ { 1 , 2 , 3 } , \displaystyle\mathcal{R}_{a}=\{r_{s,i}\mid i=1,\cdots,G,s\in\mathcal{S}_{a}\},\;a\in\{1,2,3\}, (11)

[53] p: where r s , i r_{s,i} refers to the i i -th reward of the s s -th sample which belongs to the group 𝒮 a \mathcal{S}_{a} .

[54] p: We can then compute the shared standard deviation s ​ t ​ d ​ ( ℛ a ) std(\mathcal{R}_{a}) of group rewards, and normalize the reward of each sample in batch with the new s ​ t ​ d ​ ( ℛ a ) std(\mathcal{R}_{a}) to calculate advantage accordingly:

[55] table: A s , i Perceptual = r s , i − m ​ e ​ a ​ n ​ ( r s , 1 , r s , 2 , … ​ r s , G ) s ​ t ​ d ​ ( ℛ a ) , \displaystyle A_{s,i}^{\text{Perceptual}}=\frac{r_{s,i}-mean(r_{s,1},r_{s,2},\dots r_{s,G})}{std(\mathcal{R}_{a})\,}, (12)

[56] table: s ​ t ​ d ​ ( ℛ a ) = 1 | ℛ a | − 1 ​ ∑ r s , i ∈ ℛ a ( r s , i − 1 | ℛ a | ​ ∑ r s , i ∈ ℛ a r s , i ) 2 , \begin{aligned} std(\mathcal{R}_{a})=\sqrt{\frac{1}{|\mathcal{R}_{a}|-1}\sum_{r_{s,i}\in\mathcal{R}_{a}}\big(r_{s,i}-\frac{1}{|\mathcal{R}_{a}|}\sum_{r_{s,i}\in\mathcal{R}_{a}}r_{s,i}\big)^{2}}\,,\end{aligned} (13)

[57] p: where | ℛ a | |\mathcal{R}_{a}| denotes to the cardinality of ℛ a \mathcal{R}_{a} .

[58] p: By grouping samples into low-, medium-, and high-entropy categories, the normalization scale is shared only among samples with comparable perceptual difficulty. This mitigates the influence of extreme samples, balances treatment across different levels of visual complexity, and ultimately stabilizes optimization.

[59] h3: 3.2 Reasoning Difficulty-based Regrouping

[60] p: Reasoning difficulty estimation. While perceptual difficulty captures the intrinsic complexity of the image, reasoning difficulty is shaped by the model’s intrinsic confidence in generating the final answer. Even for inputs with similar visual complexity, the model may exhibit varying confidence levels: high confidence (assigning a high probability to reasoning chains) implies a clear and reliable reasoning path, whereas low confidence indicates uncertainty and potential reasoning failures. Following this intuition, we quantify reasoning difficulty using the model’s probabilities for its reasoning chains.

[61] p: For the given batch ℬ = { ( ℐ s , 𝒬 s ) } s = 1 B \mathcal{B}=\{(\mathcal{I}_{s},\mathcal{Q}_{s})\}_{s=1}^{B} , and the generated G G responses for each sample, we denote the i i -th response as o s , i = ( o s , i 1 , … , o s , i T ) o_{s,i}=(o_{s,i}^{1},\ldots,o_{s,i}^{T}) , where o s , i n o_{s,i}^{n} is the n n -th token and T T is the sequence length.

[62] p: Based on token-level log probability π θ ​ ( o s , i n | ℐ s , 𝒬 s , o s , i < n ) \pi_{\theta}\!\;\big(o_{s,i}^{n}\,\big|\,\mathcal{I}_{s},\mathcal{Q}_{s},o_{s,i}^{<n}\big) , we aggregate across tokens to obtain the sequence-level log probability for response o s , i o_{s,i} :

[63] table: L s , i = ∑ n = 1 T π θ ​ ( o s , i n | ℐ s , 𝒬 s , o s , i < n ) . \displaystyle L_{s,i}=\sum_{n=1}^{T}\pi_{\theta}\!\;\big(o_{s,i}^{n}\,\big|\,\mathcal{I}_{s},\mathcal{Q}_{s},o_{s,i}^{<n}\big). (14)

[64] p: Then we define model confidence for sample ( ℐ s , 𝒬 s ) (\mathcal{I}_{s},\mathcal{Q}_{s}) as the average sequence-level log probability across its G G rollouts:

[65] table: L ⁡ ( 𝒬 s ) = 1 G ​ ∑ i = 1 G L s , i . \displaystyle L(\mathcal{Q}_{s})\;=\;\frac{1}{G}\sum_{i=1}^{G}L_{s,i}. (15)

[66] p: This formulation reflects the model’s internal confidence: High and consistent L ⁡ ( 𝒬 s ) L(\mathcal{Q}_{s}) indicates reliable reasoning chains, whereas low or fluctuating L ⁡ ( 𝒬 s ) L(\mathcal{Q}_{s}) reflects epistemic uncertainty, implying a more challenging reasoning sample.

[67] p: Reasoning difficulty-based regrouping. Given the model confidence scores L ⁡ ( 𝒬 s ) L(\mathcal{Q}_{s}) for the batch ℬ = { ( ℐ s , 𝒬 s ) } s = 1 B \mathcal{B}=\{(\mathcal{I}_{s},\mathcal{Q}_{s})\}_{s=1}^{B} , we divide samples into b b groups according to the quantiles of their confidence distribution. Let { τ 0 , τ 1 , … , τ b } \{\tau_{0},\tau_{1},\ldots,\tau_{b}\} denote the quantile boundaries, with τ 0 = 0 \tau_{0}=0 and τ b = 1 \tau_{b}=1 . Each question 𝒬 s \mathcal{Q}_{s} is then assigned to a group by:

[68] table: ℳ u = { s ∣ τ u − 1 ≤ L ( 𝒬 s ) < τ u } , u ∈ { 1 , … , b } . \begin{aligned} \mathcal{M}_{u}=\{\,s\mid\tau_{u-1}\leq L(\mathcal{Q}_{s})<\tau_{u}\,\},\quad u\in\{1,\ldots,b\}.\end{aligned} (16)

[69] p: Within each group ℳ u \mathcal{M}_{u} , we define the reward set as:

[70] table: ℛ u = { r s , i ∣ i = 1 , … , G , s ∈ ℳ u } , u ∈ { 1 , … , b } , \begin{aligned} \mathcal{R}_{u}=\{r_{s,i}\mid i=1,\dots,G,s\in\mathcal{M}_{u}\},\;u\in\{1,\dots,b\},\end{aligned} (17)

[71] p: where r u , i r_{u,i} is the reward of the i i -th response for the sample, which belongs to the u u group. We can then calculate the shared standard deviation s ​ t ​ d ​ ( ℛ 𝒲 ) std(\mathcal{R_{\mathcal{W}}}) of reasoning difficulty-based group, and compute the advantage accordingly:

[72] table: A s , i Reasoning = r s , i − m ​ e ​ a ​ n ​ ( r s , 1 , r s , 2 , … ​ r s , G ) s ​ t ​ d ​ ( ℛ u ) , \displaystyle A_{s,i}^{\text{Reasoning}}=\frac{r_{s,i}-mean(r_{s,1},r_{s,2},\dots r_{s,G})}{std(\mathcal{R}_{u})\,}, (18)

[73] p: where the std can be calculated as:

[74] table: s ​ t ​ d ​ ( ℛ u ) = 1 | ℛ u | − 1 ​ ∑ r s , i ∈ ℛ u ( r s , i − 1 | ℛ u | ​ ∑ r s , i ∈ ℛ u r s , i ) 2 , \begin{aligned} std(\mathcal{R}_{u})=\sqrt{\frac{1}{|\mathcal{R}_{u}|-1}\sum_{r_{s,i}\in\mathcal{R}_{u}}\big(r_{s,i}-\frac{1}{|\mathcal{R}_{u}|}\sum_{r_{s,i}\in\mathcal{R}_{u}}r_{s,i}\big)^{2}}\,,\end{aligned} (19)

[75] p: This regrouping ensures that responses with similar confidence levels are normalized on comparable scales, mitigating instability introduced by overconfident or underconfident samples.

[76] h3: 3.3 Combination for Robust Optimization

[77] p: To leverage the complementary aspects of perceptual and reasoning difficulty, we propose an element-wise combination strategy. Specifically, given the perceptual-based group normalized advantage A Perceptual A^{\text{Perceptual}} , the reasoning-based group normalized advantage A Reasoning A^{\text{Reasoning}} , and the original GRPO advantage A GRPO A^{\text{GRPO}} , the combined advantage is defined as:

[78] table: A Combined = α Ori ⋅ A GRPO + α Percep ⋅ A Perceptual + α Reason ⋅ A Reasoning , \begin{aligned} A^{\text{Combined}}\;&=\;\alpha_{\text{Ori}}\cdot A^{\text{GRPO}}\;\\ &+\;\alpha_{\text{Percep}}\cdot A^{\text{Perceptual}}\;\\ &+\;\alpha_{\text{Reason}}\cdot A^{\text{Reasoning}},\end{aligned} (20)

[79] p: where α Ori , α Percep , α Reason \alpha_{\text{Ori}},\alpha_{\text{Percep}},\alpha_{\text{Reason}} are weighting coefficients that balance the contributions of the three components. Perceptual difficulty, quantified by the entropy in the image, captures the visual complexity of multimodal inputs; reasoning difficulty, derived from token- and sequence-level log probabilities, reflects the model uncertainty during reasoning. Integrating these difficulty-based advantages with the original GRPO advantage allows the model to preserve meaningful intra-sample distinctions and incorporate both intrinsic and extrinsic difficulty context, providing a more stable and informative advantage for policy optimization.

[80] h2: 4 Experiment

[81] figure: Table 1 : Performance comparison of Multi-modal LLMs with over 5 benchmarks. Accuracy scores (%) are reported for all benchmarks for clarity. Data sizes used for SFT and RL are annotated in blue and red , respectively. The best value in each column is shown in bold , and the second-best is underlined . Model Data Size MathVerse MathVision MathVista WeMath HallusionBench Average Close-source models GPT-4o - 50.8 30.4 63.8 69.0 71.4 - Claude-3.5-Sonnet - 26.5 38.0 67.7 - 71.6 Open-source models InternVL-2.5-8B-Instruct ( Chen et al., 2024 ) - 39.5 19.7 64.4 - 67.3 - LLaVA-OneVision-7B ( Li et al., 2024 ) - 26.2 - 63.2 - 48.4 - Kimi-VL-16B ( Du et al., 2025a ) - 44.9 21.4 68.7 - 66.2 - URSA-8B ( Luo et al., 2025 ) - 45.7 26.2 59.8 - - - Mulberry-7B ( Yao et al., 2024 ) - - - 63.1 - - - reinforcement learning with verifiable reward based R1-VL-7B ( Zhang et al., 2025a ) 260K + 10K 52.2 28.2 74.3 69.0 57.2 56.2 Vision-R1-7B ( Huang et al., 2025b ) 200K + 10K 52.4 27.2 73.5 62.9 69.2 57.0 R1-OneVision-7B ( Yang et al., 2025b ) 155K + 10K 46.1 22.5 63.9 62.1 65.6 52.0 OpenVLThinker-7B ( Deng et al., 2025 ) 35K + 15K 48.0 25.0 71.5 67.8 70.8 56.6 MM-Eureka-Qwen-7B ( Meng et al., 2025 ) 15K 50.5 28.3 71.5 65.5 68.3 56.8 ADORA-7B ( Gui and Ren, 2025 ) 2.1K 50.1 27.6 71.1 67.1 53.1 53.8 ThinkLite-7B-VL ( Wang et al., 2025d ) 11K 50.2 27.6 72.7 69.2 71.0 58.1 VLAA-Thinker-7B ( Chen et al., 2025a ) 25K 49.9 26.9 68.8 67.9 68.6 56.4 NoisyRollout ( Liu et al., 2025a ) 2.1K 53.2 28.5 72.6 69.6 72.1 59.2 Qwen2.5-VL-7B-Instruct ( Bai et al., 2025 ) - 46.2 25.0 67.5 63.1 64.6 53.3 + Vanilla GRPO 2.1K (Geometry3K) 49.6 26.8 70.2 68.2 69.8 56.9 + Durian (based on Vanilla GRPO) 2.1K (Geometry3K) 52.8 28.8 72.3 69.2 72.9 59.2 + Vanilla DAPO 2.1K (Geometry3K) 50.4 27.6 70.7 69.4 68.6 57.3 + Durian (based on Vanilla DAPO) 2.1K (Geometry3K) 51.9 29.0 72.2 71.8 71.4 59.3 + Durian (based on Vanilla DAPO) 39K (ViRL39K) 52.4 29.9 73.8 72.0 72.5 60.1

[82] p: In this section, we introduce the key concepts and training setup for multimodal reasoning under RLVR ( DeepSeek-AI et al., 2025 ) . We first formulate the task, and then revisit the standard GRPO framework ( Shao et al., 2024 ) and its improved variant, Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO) ( Yu et al., 2025b ) .

[83] p: Specifically, we conduct comprehensive experiments to address the following research questions:

[84] p: ∙ \bullet RQ1: How does Durian perform on multimodal reasoning tasks compared to other baseline methods? ∙ \bullet RQ2: How do key components of Durian influence its performance? ∙ \bullet RQ3: How is the sensitivity of Durian under varying hyperparameters?

[85] h3: 4.1 Experimental Settings

[86] p: Dataset. For training, we rely on the Geometry3K ( Lu et al., 2021 ) dataset, which provides 2.1K training samples and 0.3K validation samples. Besides, we also provide experimental results training on a larger dataset ViRL39k.

[87] p: Benchmark. We evaluate Durian on five benchmarks: four visual reasoning datasets, namely MathVerse ( Zhang et al., 2024 ) , MathVision ( Wang et al., 2024 ) , MathVista ( Lu et al., 2024 ) , and WeMath ( Qiao et al., 2025 ) , as well as one visual perception benchmark, HallusionBench ( Guan et al., 2024 ) . In addition, we assess the in-domain performance by comparing Durian with the vanilla GRPO and DAPO.

[88] p: Baseline. To evaluate the performance of Durian, we consider three categories of baselines: (1) Closed-source models: GPT-4o ( Aaron et al., 2024 ) , and Cloud-3.5-sonnet ( Anthropic, 2024 ) . (2) Open source models: InternVL-2.5-8B-Instruct ( Chen et al., 2024 ) , LLaVA-OneVision-7B ( Li et al., 2024 ) , Kimi-VL-16B ( Du et al., 2025a ) , URSA-8B ( Luo et al., 2025 ) , and Mulberry-7B ( Yao et al., 2024 ) . (3) RLVR-based Models: MLLMs trained with reinforcement learning using verifiable rewards, representing the current mainstream approaches in this line of research. This category includes R1-VL-7B ( Zhang et al., 2025a ) , Vision-R1-7B ( Huang et al., 2025b ) , R1-OneVision-7B ( Yang et al., 2025b ) , OpenVLThinker-7B ( Deng et al., 2025 ) , MM-Eureka-Qwen-7B ( Meng et al., 2025 ) , ADORA-7B ( Gui and Ren, 2025 ) , ThinkLite-7B-VL ( Wang et al., 2025d ) , and VLAA-Thinker-7B ( Chen et al., 2025a ) .

[89] p: Implementation details. Following prior work ( Liu et al., 2025a ) , we use Qwen2.5-VL-7B ( Bai et al., 2025 ) as base model and adpot EasyR1 ( Zheng et al., 2025 ) as reinforcement learning framework. All experiments are conducted on 8 NVIDIA H20 96G GPUs. We adopt the default settings from EasyR1, using a learning rate of 1 ​ e − 6 1e^{-6} , a global batch size of 128, a rollout batch size of 512, and a rollout size of 8. The analysis of rollout size is provided in Appendix E .

[90] h3: 4.2 Comparison with Baseline Methods (RQ1)

[91] p: We comprehensively compare Durian with various state-of-the-art methods, and experimental results are listed in Table 1 . We can draw the following observations: (1) compared with those either distilled from large-scale chain-of-thought data or employing complex data augmentation strategies, our method, utilizing only 2.1k training samples, achieves comparable or even superior performance, significantly demonstrating our effectiveness. (2) Building upon both GRPO and DAPO, our strategy demonstrates promising performance gains. Specifically, we achieve an average of 11.3% improvements over Qwen2.5-VL, especially on the Mathvision, our strategy achieves more than 16% improvements, further showing our effectiveness.

[92] h3: 4.3 Ablation Studies (RQ2)

[93] p: To better understand the contribution of each component in Durian, we conduct ablation studies on five benchmarks, comparing four settings over Qwen2.5-vl: vanilla DAPO, DAPO with perceptual regrouping, DAPO with reasoning regrouping, and our Durian. Results are in Figure 3 .

[94] figure: Figure 3 : Acc Improvements of two re-grouping strategies over Qwen2.5-VL. We take DAPO as our backbone.

[95] p: The effects of Perceptual difficulty-based regrouping. Using perceptual difficulty-based regrouping alone yields consistent performance gains across benchmarks. For instance, on HallusionBench, which is explicitly designed to evaluate perceptual ability, we observe an improvement of 3.4% over vanilla DAPO. This demonstrates that regrouping samples via spectral analysis of image patch covariances enhances the model’s perceptual grounding by mitigating the dominance of extremely easy or hard cases.

[96] p: The effects of Reasoning difficulty-based regrouping. The average accuracy under model confidence regrouping increases to 58.4, and it’s notable to observe a 3.8% gain on MathVerse, even surpassing the performance of our method, indicating that the model’s internal confidence estimation also serves as a reliable signal for stabilizing optimization.

[97] p: The combination of both strategies achieves the best overall performance with an average accuracy of 59.3. This confirms that these two strategies provide complementary perspectives on samples, and their integration leads to more robust policy optimization.

[98] h3: 4.4 Hyper-parameter Sensitivity Analysis (RQ3)

[99] p: In this section, we analyze the effects of hyperparameters, including the number of perceptual, reasoning difficulty-based groups and α Ori , α Percep , α Reason \alpha_{\text{Ori}},\alpha_{\text{Percep}},\alpha_{\text{Reason}} .

[100] h4: 4.4.1 Groups under Perceptual difficulty-based strategy

[101] p: As shown in Figure 4 , to regroup samples by entropy, we adopt the 25th and 75th percentiles as thresholds. This quantile-based choice is inherently distribution-aware, as it adapts to the empirical spread of entropy values rather than relying on arbitrary fixed cutoffs. It produces a natural 1:2:1 partition of the data—approximately 25% easy, 50% medium, and 25% hard—avoiding the issue of overly sparse or dense categories. Such a balance is desirable for stable optimization: each group contains sufficient samples to provide reliable intra-group statistical estimates, while extremely low- and high-entropy cases are isolated rather than allowed to dominate normalization. Moreover, this three-level categorization is semantically interpretable, with low entropy corresponding to simple scenes, high entropy to complex ones, and the middle range capturing moderately difficult cases (For further empirical analysis, see Appendix B ). Detailed cases representing the entropy of these three categories are illustrated in Appendix G.1 .

[102] figure: Figure 4 : The distribution of pre-calculated entropy on the Geometry3K. x x axis represents entropy, y y axis is the probability density, Q25 and Q75 denotes 25th and 75th percentiles, respectively .

[103] h4: 4.4.2 Groups under Reasoning difficulty-based strategy

[104] p: We investigate the impact of varying the number of groups in the reasoning-based regrouping strategy in Table 2 . We observe that the performance is relatively stable across a wide range of groups, suggesting that our method is robust to this hyperparameter. For instance, on MathVista and HallusionBench, the accuracy is steadily improved as the number of groups increases to around 12–16, after which the results plateau with only minor fluctuations. This suggests that moderate group granularity is sufficient to capture meaningful variations in reasoning difficulty, while overly fine partitioning provides diminishing returns. A similar trend is observed on WeMath, where the performance peaks at 12 groups but remains competitive without significant degradation even when more groups are introduced.

[105] figure: Table 2 : The accuracy performance of different numbers of groups b b on five benchmarks. Groups b b MathVerse MathVision MathVista WeMath HallusionBench 4 49.4 28.1 68.6 66.7 66.8 6 50.6 27.1 69.7 70.2 70.0 10 50.6 27.5 71.3 70.8 68.9 12 52.3 28.5 70.9 71.4 69.6 16 50.4 27.5 72.4 70.7 69.9 20 51.5 28.1 71.3 70.4 68.8 24 50.1 27.9 71.6 70.1 69.7 32 50.5 26.9 71.6 68.7 70.7 40 50.7 28.3 71.4 70.2 70.3 48 50.0 27.7 71.5 69.5 70.9

[106] h4: 4.4.3 Analysis of Different Weighting Coefficients.

[107] p: We experiment with different combinations of three coefficients α O ​ r ​ i \alpha_{Ori} , α P ​ e ​ r ​ c ​ e ​ p \alpha_{Percep} , and α R ​ e ​ a ​ s ​ o ​ n \alpha_{Reason} in Table 3 . We can observe that while the performance on different benchmarks varies slightly with different settings, the method is relatively stable across a wide range of settings, with no significant degradation in results, indicating that our model is not overly sensitive to the specific choice of hyperparameters. This suggests that our method does not require extremely fine-tuned hyperparameters to perform effectively.

[108] figure: Table 3 : The effects of different weighting coefficients (built upon DAPO) on 5 benchmarks α Ori \alpha_{\text{Ori}} α Percep \alpha_{\text{Percep}} α Reason \alpha_{\text{Reason}} MathVerse MathVision MathVista WeMath HallusionBench 0.1 0.2 0.7 50.7 28.6 71.6 71.8 71.2 0.15 0.25 0.6 50.8 29.0 71.6 70.6 70.8 0.2 0.1 0.7 51.2 28.4 71.5 70.4 71.0 0.3 0.1 0.6 51.7 27.8 70.7 70.6 70.8 0.4 0.3 0.3 51.9 27.9 71.4 70.5 71.1 0.6 0.2 0.2 50.4 28.8 72.2 71.0 71.4 0.7 0.1 0.2 51.1 28.3 70.3 71.1 69.8

[109] h2: 5 Related Works

[110] p: In this section, we overview of the related studies. Specifically, we first discuss representative strategies to construct multimodal reasoning models, including chain-of-thought distillation, reinforcement learning, and visual tool integration. Then we introduce the RLVR and its optimization variants, and finally, we highlight the key differences between ours and existing approaches.

[111] h3: 5.1 Multimodal Reasoning Models

[112] p: Chain-of-thought distillation. Supervised fine-tuning on long CoT data enables models to learn detailed reasoning traces, thereby improving reasoning accuracy. Specifically, building upon ( Zhang et al., 2023 ) , this strategy has proven effective through both transferring CoT-enhanced LLMs to multimodal settings ( Du et al., 2025b ) and training directly with multimodal reasoning data ( Liu et al., 2023 ) . Recent works explore different forms of intermediate reasoning supervision ( Dai et al., 2023 ; Yang et al., 2025c ) .

[113] p: Reinforcement learning. Another line of research leverages RL to optimize reasoning trajectories beyond imitation. Most studies adopt PPO ( Schulman et al., 2017 ) or GRPO ( Shao et al., 2024 ) , with representative approaches such as ( Shen et al., 2025 ; Wang et al., 2025b ; Wang et al., 2025c ) that apply RL across diverse domains. We will elaborate on RLVR and GRPO in the following subsection (Section 5.2 ).

[114] p: Visual tool integration. This paradigm moves beyond merely “thinking about images” toward actively querying, modifying, and generating visual information as intermediate steps in reasoning, forming a “visual chain of thought”. The development of think-with-image can be roughly divided into three stages ( Su et al., 2025 ) : from external tool exploration ( Ma et al., 2024 ; Ma et al., 2025 ) , through programmatic manipulation ( Surís et al., 2023 ; Fu et al., 2025 ) , to intrinsic imagination ( Zhao et al., 2025 ; Chen et al., 2025b ) . These three stages reflect interconnected capabilities—active exploration, structured reasoning, and generative planning—that together transform visual representations from static inputs into a dynamic workspace for thought.

[115] h3: 5.2 Reinforcement Learning with Verifiable Reward

[116] p: RLVR ( Lambert et al., 2024 ) is an optimization paradigm that replaces subjective reward scores with verifiable signals. Its core algorithm, GRPO ( Shao et al., 2024 ) , stabilizes training by comparing candidate responses within a group. Subsequent studies can be broadly categorized into two directions: data-centric methods, which expand the candidate and reward space through data manipulation or augmentation, and algorithm-centric methods, which refine GRPO to strengthen semantic grounding and coherent reasoning.

[117] p: Data-centric GRPO. This line of work enlarges the candidate set ( Chen et al., 2025d ) or restructures the training data ( Chen et al., 2025c ; Zhu et al., 2025 ) so that group comparisons capture richer behaviors. By manipulating data distributions ( Zhu et al., 2025 ) or augmenting inputs ( Li et al., 2025 ; Liu et al., 2025a ) , these methods expose models to a wider variety of responses, thereby increasing the likelihood of discovering high-quality verifiable signals.

[118] p: Algorithm-centric GRPO. In contrast, algorithm-centric methods refine how verifiable signals guide reasoning. Rather than expanding candidate sets, they adapt GRPO to enhance semantic grounding ( Yu et al., 2025a ; Liu et al., 2025c ) and logical coherence ( Huang et al., 2025a ; Wei et al., 2025 ) . These approaches emphasize the role of visual grounding and promote reasoning chains where intermediate steps remain verifiable while supporting the final answer.

[119] p: Difference. Compared with existing methods, we regroup the data in advantage calculation based on model response uncertainty and the entropy of images when computing std , and sharing the std within each group. This design prevents the model from overfitting to extreme samples and enhances its ability to capture the data distinction within each group.

[120] h2: 6 Conclusion

[121] p: In this work, we identify a critical challenge in GRPO-based reinforcement learning methods for multimodal reasoning tasks: the std -based group normalization is sensitive to extreme samples , such as response groups that are almost entirely positive or negative. While this issue exists in GRPO in general, it is significantly amplified in multimodal settings due to the joint influence of perceptual complexity and reasoning uncertainty.

[122] p: To address this, we propose Durian, an effective difficulty-aware re-grouping strategy. By decomposing the difficulty into perceptual and reasoning aspects, we construct groups of samples with similar difficulty levels, allowing each group to share std during normalization. The normalized advantages with shared std from both aspects are combined via element-wise combination, effectively integrating data complexity and model uncertainty while preserving intra-group distinctions. By applying over GRPO and DAPO, our strategy achieves 11.3% average performance gains across multiple multimodal reasoning benchmarks.

[123] p: Limitations and Future Work. Durian inevitably introduces some hyperparameters, but we observe that performance across benchmarks remains relatively stable under a wide range of settings. This empirical robustness suggests that the Durian is not overly sensitive to precise hyperparameter tuning. Several directions remain open, such as more precise difficulty estimation and adaptive grouping strategies, which may better balance intra-group distinctions and mitigate extreme samples. Beyond technical refinements, the underlying principle of aligning optimization with sample difficulty also offers a general paradigm for stabilizing RL optimization with multimodal inputs.

[124] h2: Impact Statements

[125] p: This paper presents work whose goal is to advance the field of machine learning. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here.

[126] h2: References

[127] h2: Appendix A Analysis of the occurrence of extreme samples, which std -based group normalization is highly sensitive to.

[128] p: To further support the motivation of our paper and analyze the changes of extreme samples during training, we perform a detailed step-by-step analysis of reward statistics across 60 training steps with 512 samples and their 8 rollout rewards. The empirical evidence clearly shows that the existence of extreme samples is not an occasional event but a persistent and systemic phenomenon.

[129] figure: Table 4 : The statistics of rewards about extreme samples within the batch across 60 training steps. Training steps 1 10 20 30 40 50 60 Effective samples (participating in training) 323 327 324 322 297 314 306 Extreme success (7 correct & 1 wrong) 41 39 48 66 78 60 82 Extreme failure (7 wrong & 1 correct) 78 89 74 51 54 54 51 Total Extreme Ratio 36.8% 39.1% 37.7% 36.3% 44.4% 36.31% 43.5%

[130] p: First, groups with 8 identical rewards (i.e., variance = 0) constitute 35%–46% of all samples at every training step. We first exclude these groups for not participating in gradient updates.

[131] p: Second, during the training process, there are 31%–44% samples exhibit the 7:1 extreme reward patterns (i.e., 7/8 correct or wrong) among the remaining effective samples, which produce extremely small variance. Besides, the occurrence of this situation will increase as training deepens.

[132] p: These findings demonstrate that the instability of std -based normalization is structural rather than incidental: multimodal reasoning tasks naturally contain a large proportion of very easy and very hard samples, leading to unstable and unreliable advantage scaling. This directly motivates our difficulty-aware regrouping strategy, which stabilizes normalization by ensuring that variance is computed only within samples of comparable difficulty.

[133] h2: Appendix B Verify the feasibility of utilizing image entropy as a proxy for perceptual difficulty and model confidence as a proxy for reasoning difficulty.

[134] h3: B.1 Image entropy as a proxy for perceptual difficulty.

[135] p: Perceptual difficulty in our framework is defined based on the complexity of visual embeddings , which we quantify using spectral analysis of image patch covariances. Specifically, the entropy of the eigenvalue distribution from the covariance matrix reflects the amount of variance across spatial features in the image. Researchers in prior works ( Grzywacz, 2025 ) support that: high entropy indicates a more diverse distribution of visual features, implying a richer and more complex visual structure. This complexity makes it more challenging for the visual model to recognize, and thus we associate higher entropy with greater perceptual difficulty.

[136] h3: B.2 Model confidence as a proxy for reasoning difficulty.

[137] p: Researchers in ( Farquhar et al., 2024 ; Nguyen et al., 2025 ) propose that “one measure of uncertainty is the predictive entropy of the output distribution, which measures the information one has about the output given the input[3]. The predictive entropy for an input sentence 𝐱 \bf{x} is the conditional entropy ( H H ) of the output random variable ( Y Y ) with realization y y given 𝐱 \bf{x} .”

[138] table: PE ( 𝐱 ) = H ( Y | 𝐱 ) = − ∑ y P ( y | 𝐱 ) ln P ( y | 𝐱 ) . \displaystyle{\rm{PE}}({\bf{x}})=H(Y|{\bf{x}})=-\sum_{y}P(\,y|{\bf{x}})\mathrm{ln}P(\,y|{\bf{x}}). (21)

[139] p: Researchers ( Kadavath et al., 2022 ) also hypothesize that when a model knows the answer to a particular question, it is confident in its response, and this would result in an answer distribution with small entropy. Conversely, when a model is unsure about its response, it will lead to an answer distribution with high entropy, thus implying a more challenging reasoning process.

[140] p: This aligns directly with our formulation: the sequence-level log probabilities we compute are theoretically linked to the notion of semantic entropy and represent the joint likelihood of the entire reasoning chain. A low log-probability corresponds to a flat or high-entropy output distribution, reflecting uncertainty in the reasoning trajectory, while a high log-probability corresponds to a confident, low-entropy distribution.

[141] h3: B.3 Empirical validation.

[142] p: During the evaluation stage, we conduct an analysis focusing on the questions that the model answered incorrectly on two benchmarks. We want to examine whether these error samples are concentrated in the more difficult groups as defined by our difficulty metrics. The intuition behind this approach is that samples belonging to higher-difficulty groups—whether in terms of perceptual complexity or reasoning uncertainty—should naturally be harder for the model to tackle. Consequently, we expect these samples to exhibit higher error rates.

[143] p: To achieve this, we use Gemini2.5 Pro to classify the sources of errors, distinguishing between perceptual errors and reasoning errors .

[144] p: ∙ \bullet For perceptual errors , we first group the images based on their visual entropy, then compute the proportion of incorrect answers within each group relative to the total number of perceptual errors.

[145] p: ∙ \bullet Similarly, for reasoning errors , we group the samples based on model confidence, and calculate the proportion of incorrect answers in each group relative to the total number of reasoning errors.

[146] figure: Table 5 : The error rate of perceptual difficulty groups in perceptual errors on two benchmarks. low-entropy medium-entropy high-entropy Wemath 23.6% 31.3% 45.1% HallusionBench 21.2% 29.6% 49.2%

[147] figure: Table 6 : The error rate of reasoning difficulty groups in reasoning errors on two benchmarks. group 1 (low confidence) group 2 group 3 group 4 group 5 group 6 group 7 group 8 group 9 group 10 (high confidence) Wemath 13.4% 12.6% 13.2% 12.7% 11.6% 9.1% 9.7% 7.2% 6.7% 4.2% HallusionBench 12.7% 11.9% 11.2% 11.7% 10.0% 9.8% 9.0% 8.2% 8.3% 7.1%

[148] p: As shown in Table 5 and Table 6 , the results align with our expectations: images with low visual entropy (indicating simplicity) correspond to lower perceptual error rates , and samples with lower model confidence (indicating greater uncertainty in the reasoning process) correspond to higher reasoning error rates . Our empirical findings are consistent with this intuition, further supporting the validity of our difficulty metrics.

[149] h2: Appendix C Experiment Settings

[150] p: Reward Calculation. We adopt a combination of format reward and accuracy reward as the final reinforcement learning signal. The two components are defined as follows:

[151] table: r format = { 1 , if the output format is correct , 0 , otherwise , r_{\text{format}}=\begin{cases}1,&\text{if the output format is correct},\\ 0,&\text{otherwise},\end{cases} (22)

[152] table: r acc = { 1 , if the answer matches the ground truth , 0 , otherwise . r_{\text{acc}}=\begin{cases}1,&\text{if the answer matches the ground truth},\\ 0,&\text{otherwise}.\end{cases} (23)

[153] p: The overall reward is computed as the weighted sum of the two:

[154] table: r overall = 0.1 × r format + 0.9 × r acc . r_{\text{overall}}=0.1\times r_{\text{format}}+0.9\times r_{\text{acc}}. (24)

[155] p: A smaller weight is assigned to the format reward, since response formatting is relatively easy to learn compared with accuracy.

[156] h2: Appendix D Prompt Design

[157] p: We use a “Thinking prompt” to formalize the output of the model. It requires the model to put its reasoning process within <think>...</think> and the final answer in \boxed{} . We keep the system prompt of Qwen2.5-VL ( Bai et al., 2025 ) and prepend the “Thinking prompt” to the user message. The same format is used for both training and evaluation. The full instruction prompt is as follows:

[158] h2: Appendix E Analysis of the effect of rollout size on performance and stability.

[159] figure: Table 7 : The effects of rollout size (built upon DAPO) on 5 benchmarks. rollout MathVerse MathVision MathVista WeMath HallusionBench 2 48.7 27.1 70.1 69.7 67.3 4 50.1 28.4 71.5 70.2 68.9 8 51.9 29.0 72.2 71.8 71.4 16 52.1 29.2 72.1 71.2 71.2 24 51.7 29.0 71.9 71.9 71.5 32 51.9 28.9 72.2 71.0 71.3

[160] p: We observed from Table 7 that when the rollout size is smaller than 8, the performance improves as the rollout size increases. Notably, when the number of rollouts is reduced to 2, the model reverts to PPO. As the rollout size continues to increase beyond 8, the improvement in performance becomes less pronounced, eventually stabilizing at a stable value.

[161] p: These results indicate that while increasing the number of rollouts can lead to better performance, after a certain point, beyond which further increases in group size do not significantly contribute to performance improvement. This shows the importance of selecting an appropriate group size to balance computational cost and model performance.

[162] h2: Appendix F The Use of Large Language Models(LLMs)

[163] p: We conducted a study on improving GRPO to further enhance the reasoning capability of MLLMs, achieving substantial performance gains on datasets such as MathVerse ( Zhang et al., 2024 ) , MathVision ( Wang et al., 2024 ) , and MathVista ( Lu et al., 2024 ) . During the preparation of this manuscript, we used LLMs to assist with tasks such as grammar correction, language refinement, and logical checking. However, we confirm that no outputs from the LLMs were directly used; instead, all content underwent careful verification and reconstruction by the authors.

[164] h2: Appendix G Case Study

[165] h3: G.1 Perceptual difficulty-based re-grouping cases

[166] figure: Figure 5 : Illustrative examples of different levels of entropy

[167] h3: G.2 Demonstration of improved perception and reasoning capabilities

[168] figure: Figure 6 : Case Study 1 showing improved reasoning capability on HallusionBench over vanilla GRPO.

[169] figure: Figure 7 : Case Study 2 showing improved reasoning capability on Mathvision over vanilla GRPO.

[170] figure: Figure 8 : Case Study 2 showing improved reasoning capability on Mathverse over vanilla GRPO.

[171] figure: Figure 9 : Case Study 3 showing improved reasoning capability on Mathvista over vanilla GRPO.

[172] figure: Figure 10 : Case Study 4 showing improved reasoning capability on Wemath over vanilla GRPO.

[173] h2: Instructions for reporting errors

[174] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[175] p: Tip: You can select the relevant text first, to include it in your report.

[176] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[177] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
