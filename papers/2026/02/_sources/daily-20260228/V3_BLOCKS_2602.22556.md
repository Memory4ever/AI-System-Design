[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Stable Adaptive Thinking via Advantage Shaping and Length-Aware Gradient Regulation

[3] h6: Abstract

[4] p: Large reasoning models (LRMs) achieve strong performance through extended reasoning traces, but they often exhibit overthinking behavior for low-complexity queries. Existing efforts to mitigate this issue are fundamentally limited by unstable accuracy–efficiency trade-offs and poor robustness to heterogeneous reasoning behaviors. To address these challenges, we propose a two-stage framework for stable adaptive thinking in LRMs. The framework first applies Hybrid Fine-Tuning to expose the model to both thinking and no-thinking behaviors, establishing well-conditioned initialization. It then performs adaptive reinforcement learning with Correctness-Preserving Advantage Shaping (CPAS) to avoid suppressing correct long-chain reasoning, and Length-Aware Gradient Regulation (LAGR) to stabilize optimization under severe reasoning-length heterogeneity. Extensive experiments on Qwen2.5-1.5B and 7B show consistent improvements over strong baselines, achieving up to +3.7/+3.6 accuracy points while reducing generated tokens by 40.6%/43.9%. Further analyses across varying problem difficulties and out-of-distribution tasks confirm the robustness and generalization of our approach.

[5] h2: 1 Introduction

[6] p: Recent advancements in large reasoning models (LRMs), such as OpenAI-o1 OpenAI et al. (2024) and DeepSeek-R1 DeepSeek-AI et al. (2025a) , have demonstrated remarkable progress in solving complex tasks. By explicitly generating extended reasoning traces, these models exhibit strong reasoning and generalization capabilities across a wide range of domains Xu et al. (2025) . Although long-form reasoning benefits challenging problems, existing LRMs lack difficulty-aware control ability and thus often produce unnecessarily long reasoning chains even for simple queries Yue et al. (2025) ; Liu et al. (2025) . This overthinking issue significantly increases token usage and inference cost, posing a critical bottleneck for the practical efficiency of LRMs Chen et al. (2024) .

[7] figure: Figure 1: Illustration of efficient reasoning methods.

[8] p: To mitigate the efficiency issues arising from overthinking, recent studies have investigated several efficient reasoning strategies Feng et al. (2025) ; Sui et al. (2025) , as illustrated in Figure 1 . Length-based penalties have been introduced to discourage excessively long reasoning chains Luo et al. (2025a) ; Aggarwal and Welleck (2025) ; Xia et al. (2025) ; however, these approaches operate within the thinking mode, and the additional constraints in these approaches may limit the exploration space of LRMs. Routing-based methods reduce inference cost by selecting between reasoning and non-reasoning models Hu et al. (2024) ; Ong et al. (2024) ; OpenAI (2025) , but they typically depend on external annotations for supervision and the maintenance of multiple models, thereby increasing both training and deployment cost. More recently, reinforcement-learning-based adaptive thinking methods aim to improve efficiency by encouraging shorter reasoning chains. ThinkLess Fang et al. (2025) achieves this via a decoupled GRPO formulation, whereas AdapThink Zhang et al. (2025a) employs a PPO-based objective to promote short-chain reasoning. Despite their effectiveness, these methods often face difficulties in achieving a stable balance between reasoning accuracy and efficiency during training.

[9] p: These observations highlight two key challenges in adaptive thinking. First, there is an inherent trade-off between efficiency and accuracy. While adaptive thinking aims to reduce computational costs, an excessive bias toward brevity may constrain the model’s capacity for deep reasoning on complex tasks, ultimately degrading performance. Second, severe length heterogeneity during training poses additional difficulties. Within a single rollout group, reasoning chains may range from a few hundred tokens to tens of thousands of tokens, resulting in uneven optimization granularity and imbalanced gradient contributions, which may compromise training stability.

[10] p: To address these challenges, we propose Stable Adaptive Thinking via Advantage Shaping and Length-Aware Gradient Regulation, a two-stage framework for stable and effective adaptive reasoning in large reasoning models. The proposed approach enables the model to adjust its reasoning depth according to input difficulty, improving efficiency on simple queries while preserving accuracy on complex ones. In the first stage, Hybrid Fine-Tuning is employed to establish well-conditioned initialization by exposing the model to both short and long reasoning behaviors. In the second stage, adaptive thinking is optimized through reinforcement learning with two key mechanisms. Correctness-Preserving Advantage Shaping , in contrast to prior approaches that directly reward short chains, introduces an advantage shaping strategy that avoids suppressing correct long-chain reasoning trajectories when encouraging efficiency, thereby preserving the model’s exploration capacity. Length-Aware Gradient Regulation addresses optimization instability arising from the severe reasoning length heterogeneity by regulating gradient allocation across different responses, while ensuring that control signals remain effective under long and heterogeneous reasoning sequences, leading to more stable training dynamics. These components provide a principled solution for stable adaptive thinking under efficiency–accuracy trade-offs. In general, the contributions of this paper can be summarized as follows:

[11] p: We address key optimization challenges in adaptive thinking. Specifically, we focus on balancing computational efficiency with reasoning accuracy, and on mitigating training instability arising from severe length heterogeneity across different reasoning modes during reinforcement learning optimization.

[12] p: We propose a two-stage framework for stable adaptive thinking. The framework integrates hybrid fine-tuning with adaptive reinforcement learning, while employing correctness-preserving advantage shaping and length-aware gradient regulation for stable training.

[13] p: Extensive experiments on the Qwen2.5 series across multiple model scales and mathematical benchmarks demonstrate that our approach consistently outperforms existing baselines, achieving up to +3.7/+3.6 accuracy improvements while reducing the number of generated tokens by 40.6%/43.9%. Further analyses across varying problem difficulties and diverse tasks confirm the robustness and generalization of our approach.

[14] h2: 2 Preliminaries

[15] figure: Figure 2: Overview of our two-stage training pipeline. Stage 1 performs Hybrid Fine-Tuning (HFT) on paired thinking and no-thinking formats to initialize a unified policy. Stage 2 applies GRPO-style reinforcement learning with correctness-preserving advantage shaping (CPAS) and length-aware gradient regulation (LAGR) to stabilize optimization under extreme length heterogeneity and to learn when to think.

[16] h3: 2.1 Adaptive Thinking

[17] p: Specifically, given an input problem x x , the model produces an output y y consisting of a chain-of-thought trajectory and a final answer: y = { S , a } y=\{S,a\} . We introduce a control token to specify the thinking mode m ∈ ℳ = { /think , /no_think } m\in\mathcal{M}=\{\texttt{/think},\texttt{/no\_think}\} : when the control token is /think , the model generates a non-empty chain-of-thought trajectory S S in the thinking mode; when the control token is /no_think , the chain-of-thought is empty S = ∅ S=\emptyset and the model directly produces the final answer a a .

[18] p: We implement adaptive thinking with a single policy model. Given input x ∼ 𝒟 x\sim\mathcal{D} , the model first generates a control token m ∈ ℳ m\in\mathcal{M} , and then generates the remaining output conditioned on m m . Thus, the same parameters θ \theta define both mode selection π θ \pi_{\theta} (the distribution of the first control token) and response generation P θ ​ ( y ∣ x , m ) P_{\theta}(y\mid x,m) .

[19] h3: 2.2 Problem Statement

[20] p: The goal of adaptive thinking is to reduce unnecessary generation while preserving correctness. We define a utility function that trades off accuracy and efficiency. For an output y = { S , a } y=\{S,a\} , we use an accuracy reward R acc ​ ( y ∣ x ) ∈ { 0 , 1 } R_{\text{acc}}(y\mid x)\in\{0,1\} indicating whether the final answer a a is correct (verified by an automatic checker), and a length reward R len ​ ( y ∣ x ) R_{\text{len}}(y\mid x) that favors shorter outputs. The overall utility is

[21] table: U ⁡ ( x , y ) = R acc ​ ( y ∣ x ) + γ ​ R len ​ ( y ∣ x ) \displaystyle U(x,y)=R_{\text{acc}}(y\mid x)+\gamma\,R_{\text{len}}(y\mid x)

[22] p: where γ > 0 \gamma>0 controls the efficiency–accuracy trade-off. Our objective is to learn a policy that selects m m and generates y y to maximize expected utility:

[23] table: max θ 𝔼 x ∼ 𝒟 [ 𝔼 m ∼ π θ ( ⋅ ∣ x ) 𝔼 y ∼ P θ ( ⋅ ∣ x , m ) [ U ( x , y ) ] ] . \displaystyle\max_{\theta}\ \mathbb{E}_{x\sim\mathcal{D}}\Big[\ \mathbb{E}_{m\sim\pi_{\theta}(\cdot\mid x)}\ \mathbb{E}_{y\sim P_{\theta}(\cdot\mid x,m)}\big[U(x,y)\big]\ \Big].

[24] h2: 3 Methodologies

[25] h3: 3.1 Overall Framework

[26] p: We propose a novel framework for stable adaptive thinking , which enables a single model to dynamically regulate its thinking depth according to problem difficulty. The objective is to avoid unnecessary overthinking on simple queries while preserving strong deliberative capability on challenging problems. Starting from a pretrained base language model, our framework adopts a two-stage training paradigm that comprises hybrid fine-tuning for capability warm-up and reinforcement learning for stable adaptive thinking. An overview of the training pipeline is illustrated in Figure 2 .

[27] h4: Stage I: Hybrid Fine-Tuning.

[28] p: In the first stage, we perform hybrid fine-tuning on the base model using large-scale mathematical reasoning data with heterogeneous supervision, including long CoT solutions and short direct answers distilled from strong teacher models. This stage injects both thinking and no-thinking capabilities into a unified model and provides a stable warm-up for subsequent reinforcement learning.

[29] h4: Stage II: Stable Adaptive thinking with Reinforcement Learning.

[30] p: In the second stage, the model is further optimized with a modified GRPO algorithm, where it explores both thinking and no-thinking trajectories and learns when to think . To stabilize training under severe length heterogeneity and prevent mode collapse, we introduce correctness-preserving advantage shaping and length-aware gradient regulation, which together facilitate effective exploration and robust training.

[31] h3: 3.2 Hybrid Fine-Tuning for Warm-Up

[32] p: Hybrid Fine-Tuning (HFT) is designed to provide a stable cold-start initialization for adaptive reinforcement learning by exposing the base model to both thinking and no-thinking generation patterns in a unified and format-consistent manner. Unlike the subsequent stage, HFT does not aim to learn an adaptive decision policy; instead, it focuses on expanding the model’s solution space to support heterogeneous response behaviors.

[33] h4: Hybrid-Formatted Data Construction.

[34] p: The hybrid fine-tuning dataset is constructed from large-scale open-source mathematical corpora. Each training instance is annotated with an explicit control token that specifies the desired response mode.

[35] p: For thinking-mode examples, responses are distilled from DeepSeek-R1-0528. Each response begins with the prefix /think and contains an explicit thinking block of the form <think>{ thinking process }</think> , where the content enclosed by the <think> tags corresponds to the intermediate thinking steps produced by the teacher model. The final answer is generated after the thinking block following a unified output structure.

[36] p: For no-thinking-mode examples, responses are distilled from DeepSeek-V3-0324. These responses begin with the prefix /no_think and include an empty thinking block of the form <think></think> , which explicitly indicates that no intermediate thinking is required and that a direct answer should be produced.

[37] h4: Optimization Objective.

[38] p: During HFT, the model is optimized using standard supervised learning objectives over both response types, without imposing any explicit preference between thinking and no-thinking outputs. Given the hybrid-formatted dataset 𝒟 HFT = { ( x i , y i ) } i = 1 N \mathcal{D}_{\text{HFT}}=\{(x_{i},y_{i})\}_{i=1}^{N} , the model is optimized to maximize the conditional likelihood of the target response given the input:

[39] table: ℒ HFT = − 𝔼 ( x , y ) ∼ 𝒟 HFT ​ [ ∑ t = 1 | y | log ⁡ p θ ​ ( y t ∣ x , y < t ) ] . \displaystyle\mathcal{L}_{\text{HFT}}=-\mathbb{E}_{(x,y)\sim\mathcal{D}_{\text{HFT}}}\left[\sum_{t=1}^{|y|}\log p_{\theta}(y_{t}\mid x,y_{<t})\right].

[40] h4: Role of HFT.

[41] p: From a methodological perspective, HFT defines the feasible action space for subsequent reinforcement learning by ensuring that both thinking and no-thinking trajectories are readily accessible to the policy. This hybrid-formatted warm-up substantially reduces exploration difficulty in the reinforcement learning stage and provides a well-conditioned initialization.

[42] h3: 3.3 Stable Adaptive thinking with Reinforcement Learning

[43] p: After HFT, the model is further trained to acquire adaptive thinking capability through reinforcement learning. While HFT equips the model with both thinking-mode and no-thinking-mode generation behaviors, it does not enable the model to autonomously decide which mode to adopt for a given query. This decision-making ability is learned in the reinforcement learning stage.

[44] p: Specifically, we build upon GRPO and train the model to explore both thinking and no-thinking trajectories for each query. In this setting, the policy learns to decide whether to engage in explicit thinking by selecting between thinking-mode and no-thinking-mode responses. However, directly applying vanilla GRPO often leads to training instability and mode collapse. We identify two key challenges that arise from GRPO under heterogeneous thinking trajectories, and introduce corresponding mechanisms to address them.

[45] h4: Correctness-Preserving Advantage Shaping.

[46] p: Existing adaptive thinking approaches often discourage overthinking by assigning higher rewards to shorter thinking trajectories. Under GRPO-style group-wise optimization, advantages are computed via intra-group normalization across multiple trajectories sampled for the same input. Let { r i } i = 1 G \{r_{i}\}_{i=1}^{G} denote the rewards of a rollout group G G , and the corresponding advantages be A i = r i − 𝕄 ​ 𝕖 ​ 𝕒 ​ 𝕟 ​ ( r ) 𝕊 ​ 𝕥 ​ 𝕕 ​ ( r ) A_{i}=\frac{r_{i}-\mathbb{Mean}(r)}{\mathbb{Std}(r)} . When shorter trajectories systematically receive higher rewards Aggarwal and Welleck (2025) ; Fang et al. (2025) , this normalization induces a relative comparison bias: longer but correct thinking trajectories may satisfy 0 < r i < 𝕄 ​ 𝕖 ​ 𝕒 ​ 𝕟 ​ ( r ) 0<r_{i}<\mathbb{Mean}(r) and thus receive A i < 0 A_{i}<0 . Consequently, valid thinking behaviors are actively suppressed during optimization, limiting exploration and potentially leading to mode collapse toward no-thinking responses.

[47] p: To alleviate this issue, we introduce Correctness-Preserving Advantage Shaping (CPAS), which reshapes advantages for correct responses based on their thinking mode. Let A i GRPO A_{i}^{\text{GRPO}} denote the advantage computed by GRPO for response o i o_{i} , and let r i ∈ { 0 , 1 } r_{i}\in\{0,1\} denote the reward. The final advantage is defined as

[48] table: A i = { A i GRPO + δ , if ​ r i = 1 ​ and ​ o i ​ is short-chain , A i GRPO , otherwise . \displaystyle A_{i}=\begin{cases}A_{i}^{\text{GRPO}}+\delta,&\text{if }r_{i}=1\text{ and }o_{i}\text{ is short-chain},\\ A_{i}^{\text{GRPO}},&\text{otherwise}.\end{cases}

[49] p: where, δ > 0 \delta>0 is a small reward coefficient that provides additional encouragement for correct short-chain responses, while leaving correct long-chain responses unaffected.

[50] h4: Role of CPAS.

[51] p: By reshaping advantages for correct responses, CPAS ensures that correct thinking trajectories receive non-negative advantage signals. This prevents correct long-chain responses from being inadvertently penalized, thereby preserving the model’s exploration capacity. Consequently, CPAS contributes to more stable training dynamics and enhances the effectiveness of adaptive thinking.

[52] h4: Length-Aware Gradient Regulation.

[53] p: Under GRPO, policy optimization is performed by sampling a group G G of responses { o i } i = 1 G \{o_{i}\}_{i=1}^{G} for each query q q and aggregating token-level policy gradients within each response. The response-level gradient contribution of o i o_{i} can be written as

[54] table: g i GRPO = 1 | o i | ​ ∑ t = 1 | o i | A ^ i , t ​ ∇ θ ​ log ⁡ π θ ​ ( o i , t ∣ q , o i , < t ) , g_{i}^{\text{GRPO}}=\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\hat{A}_{i,t}\,\nabla_{\theta}\log\pi_{\theta}(o_{i,t}\mid q,o_{i,<t}),

[55] p: where | o i | |o_{i}| denotes the response length and A ^ i , t \hat{A}_{i,t} is the token-level advantage.

[56] p: In adaptive thinking, rollout groups often exhibit severe length heterogeneity, ranging from short no-thinking responses to long thinking trajectories. The 1 / | o i | 1/|o_{i}| normalization systematically attenuates gradient magnitudes for long responses, increases gradient variance, and biases optimization toward short trajectories, which may lead to premature collapse of thinking behaviors.

[57] p: To mitigate this imbalance, we propose Length-Aware Gradient Regulation , which explicitly reweights response-level gradient contributions according to response length. Specifically, LAGR employs a length-dependent weighting scheme:

[58] table: g i LAGR = w i ( β ) ​ ∑ t = 1 | o i | A ^ i , t ​ ∇ θ ​ log ⁡ π θ ​ ( o i , t ∣ q , o i , < t ) , \displaystyle g_{i}^{\text{LAGR}}=w_{i}^{(\beta)}\sum_{t=1}^{|o_{i}|}\hat{A}_{i,t}\,\nabla_{\theta}\log\pi_{\theta}(o_{i,t}\mid q,o_{i,<t}), w i ( β ) = 1 M ⋅ | o i | − β ∑ j = 1 G | o j | − β , β ∈ [ 0 , 1 ] . \displaystyle w_{i}^{(\beta)}=\frac{1}{M}\cdot\frac{|o_{i}|^{-\beta}}{\sum_{j=1}^{G}|o_{j}|^{-\beta}},\qquad\beta\in[0,1].

[59] p: where M M is a constant scaling factor used to control the overall magnitude of the gradient. When β = 1 \beta=1 , LAGR recovers the GRPO-like length-sensitive behavior that favors short responses, while β = 0 \beta=0 assigns uniform weights across responses, thereby alleviating the suppression of long ones. By adjusting β \beta , LAGR provides a mechanism to balance optimization stability and thinking flexibility.

[60] p: While LAGR mitigates length-induced imbalance at the response level, adaptive thinking introduces an additional challenge at the token level. In practice, the decision of whether to engage in thinking is primarily encoded by the prefix control token. However, when responses are long, the gradient signal of this control token can be diluted by the large number of subsequent tokens. To preserve this adaptive control signal, we further apply an explicit boosting to the control token. Let t = 0 t=0 denote the control token. The final response-level gradient under LAGR is given by

[61] table: ∇ θ 𝒥 LAGR ( θ ) = ∇ θ ∑ i = 1 G w i ( β ) [ λ min ( r i , 0 ( θ ) A ^ i , 0 , clip ( r i , 0 ( θ ) , 1 − ϵ , 1 + ϵ ) A ^ i , 0 ) + ∑ t = 1 | o i | min ( r i , t ( θ ) A ^ i , t , clip ( r i , t ( θ ) , 1 − ϵ , 1 + ϵ ) A ^ i , t ) ] . \begin{array}[]{@{}c@{}}\nabla_{\theta}\mathcal{J}_{\text{LAGR}}(\theta)=\nabla_{\theta}\sum_{i=1}^{G}w_{i}^{(\beta)}\Bigg[\lambda\,\min\!\Big(r_{i,0}(\theta)\,\hat{A}_{i,0},\\ \quad\mathrm{clip}\big(r_{i,0}(\theta),1-\epsilon,1+\epsilon\big)\,\hat{A}_{i,0}\Big)+\sum_{t=1}^{|o_{i}|}\\ \quad\min\!\Big(r_{i,t}(\theta)\,\hat{A}_{i,t},\;\mathrm{clip}\big(r_{i,t}(\theta),1-\epsilon,1+\epsilon\big)\,\hat{A}_{i,t}\Big)\Bigg].\end{array}

[62] p: where λ \lambda is a control-token boosting factor that compensates for gradient dilution in long responses.

[63] h4: Role of LAGR.

[64] p: LAGR rebalances response-level policy gradients under length heterogeneity, mitigating GRPO’s bias toward short trajectories. By preserving effective gradient signals for long thinking chains and boosting the control token, LAGR prevents decision-signal dilution and supports stable adaptive thinking.

[65] h2: 4 Experiments

[66] h3: 4.1 Experimental Settings

[67] figure: Table 1: Overall performance on MATH-500, AIME-2024, and AIME-2025 for Qwen2.5 series models. L ​ e ​ n Len is the average number of generated tokens per example. R ​ a ​ t ​ i ​ o N ​ T Ratio_{NT} denotes the fraction of examples solved in NoThinking mode. Δ ​ A ​ c ​ c \Delta Acc and Δ ​ L ​ e ​ n \Delta Len are computed relative to the always-Thinking baseline of the same base model. Method MATH-500 AIME-2024 AIME-2025 Average Acc Len Ratio N ​ T \text{Ratio}_{NT} Acc Len Ratio N ​ T \text{Ratio}_{NT} Acc Len Ratio N ​ T \text{Ratio}_{NT} Δ \Delta Acc Δ \Delta Len Qwen-2.5-1.5B Thinking 80.4 10441 0.0% 25.7 35829 0.0% 20.6 36977 0.0% 0.0 +0.0% No-Thinking 60.4 2320 100.0% 9.1 10751 100.0% 7.5 11150 100.0% -16.6 -70.9% HFT 72.3 7106 42.4% 16.8 23673 54.2% 14.5 25376 46.2% -7.4 -32.5% O1-Pruner 77.1 7043 0.0% 20.3 33417 0.0% 16.7 32185 0.0% -4.2 -12.7% RouteLLM 76.7 3862 81.6% 19.8 28305 30.8% 17.4 29973 27.8% -4.3 -25.4% AdaptThink 81.1 4341 69.4% 25.6 22819 4.2% 22.7 24187 3.3% +0.9 -38.3% Thinkless 78.5 4473 71.3% 24.5 25294 2.9% 19.3 26351 2.5% -1.5 -32.6% Ours 84.6 4176 69.8% 28.1 23258 3.7% 25.2 22062 5.4% +3.7 -40.6% Qwen-2.5-7B Thinking 90.6 8309 0.0% 65.6 29936 0.0% 59.3 35217 0.0% 0.0 +0.0% No-Thinking 75.1 1890 100.0% 25.5 10464 100.0% 20.2 9921 100.0% -31.6 -70.1% HFT 86.3 5619 45.2% 50.9 23484 42.5% 44.2 25017 40.4% -11.3 -27.3% O1-Pruner 87.9 5567 0.0% 62.4 25977 0.0% 57.5 32451 0.0% -2.6 -12.9% RouteLLM 88.2 3121 81.8% 55.3 24011 31.2% 51.7 28387 27.1% -6.8 -24.4% AdaptThink 91.1 3462 77.8% 65.2 18123 12.1% 59.1 22544 10.4% 0.0 -39.9% Thinkless 89.8 3302 78.6% 64.0 18172 13.8% 60.1 21463 12.5% -0.5 -41.6% Ours 92.4 3403 77.6% 69.2 17762 12.5% 64.6 20060 9.6% +3.6 -43.9%

[68] h4: Models.

[69] p: We adopt Qwen-2.5-1.5B-Base and Qwen-2.5-7B-Base as the initial policy models Qwen et al. (2025) . Both are extensively pre-trained and serve as the foundation for jointly learning thinking and no-thinking behaviors.

[70] h4: Dataset and Metrics.

[71] p: For HFT, we construct a large-scale training corpus from open-source mathematics datasets that require advanced numerical reasoning and multi-step logical inference, including OpenR1-Math-220k Hugging Face (2025) , DeepMath-103K He et al. (2025b) , and NuminaMath LI et al. (2024) , among others. Paired supervision is obtained by distilling thinking-mode outputs from DeepSeek-R1-0528 DeepSeek-AI et al. (2025a) and no-thinking outputs from DeepSeek-V3-0324 DeepSeek-AI et al. (2025b) . In the RL stage, we primarily adopt the DeepScaleR Luo et al. (2025b) dataset. For evaluation, we focus on standard mathematical reasoning benchmarks, including MATH-500 Lightman et al. (2023) , AIME-2024 AI-MO (2024) , and AIME-2025 AI-MO (2025) , and additionally employ GPQA Rein et al. (2024) to assess out-of-distribution generalization. We report accuracy, average token length, and no-thinking ratio to jointly measure model performance and inference efficiency.

[72] figure: Figure 3: Difficulty-aware mode selection and performance. (a) Performance of Two Think Mode on MATH-500, AIME-2024, and AIME-2025. (b) Mode ratio across MATH-500 difficulty levels. (c) Accuracy across difficulty levels, comparing our adaptive policy with always-Thinking and always-No-Thinking baselines.

[73] figure: Figure 4: Ablation and sensitivity analysis. (a) Training dynamics with/without CPAS: mean response length (left) and AIME-2024 accuracy (right). (b) Effect of the LAGR length-weight parameter β \beta (left) and the control-token boost factor λ \lambda (right) on accuracy and the no-thinking ratio.

[74] h4: Baselines.

[75] p: To ensure a comprehensive comparison, we evaluate our method on both 1.5B and 7B model scales and consider four categories of baselines. (1) Base Variants: thinking-only, no-thinking-only, and HFT hybrid models derived from the same base architectures. (2) Length-Penalization Methods: O1-Pruner Luo et al. (2025a) encourages shorter thinking processes based on a thinking-only model under accuracy constraints. (3) Routing Methods: RouteLLM Ong et al. (2024) trains a router to dynamically choose between long and short CoT using separate thinking and no-thinking models. (4) Adaptive Thinking Methods: ThinkLess Fang et al. (2025) learns a hybrid thinking policy via a decoupled GRPO strategy, while AdaptThink Zhang et al. (2025a) promotes concise thinking using PPO-based optimization. Both are initialized from the HFT models. This ensures a fair comparison across methods with consistent base architectures and appropriate training settings.

[76] h4: Implementation Details.

[77] p: All experiments are conducted on 16 NVIDIA H100 GPUs. In the Hybrid Fine-Tuning stage, we set the maximum context length to 16K tokens, with overlong samples truncated accordingly. The models are trained for 3 epochs using the LLaMA-Factory Zheng et al. (2024) framework. Training is conducted with the AdamW optimizer, employing a 10% linear warmup strategy followed by cosine learning rate decay, with the maximum learning rate set to 1e-4. In the reinforcement learning stage, the context length is extended to 24K tokens. Experiments are conducted using the VeRL Sheng et al. (2025) framework, with the policy model optimized by AdamW at a constant learning rate of 1e-6. We use a batch size of 128 with a micro-batch size of 64, and sample 8 responses per query during rollout. For verification, we adopt the Math-Verify module to provide correctness-based feedback. More details can be found in the Appendix.

[78] h3: 4.2 Main Results

[79] p: In this section, we conduct a comprehensive evaluation of different models on three mathematical reasoning benchmarks. As shown in Table 1 , our method achieves consistent gains at both the 1.5B and 7B scales, improving performance by 3.7 and 3.6 points, respectively, while reducing token costs by 40.6% and 43.9%, demonstrating both accuracy and efficiency improvements. Compared to length-penalty methods, our approach leverages an explicit no-thinking mode that does not constrain exploration, thereby achieving lower token consumption and improved overall performance. Compared to external routing methods, our approach requires no additional annotated data or deployment overhead, and can more accurately select appropriate thinking modes based on the model’s capability. Finally, relative to existing adaptive thinking methods, the proposed correctness-preserving advantage shaping and length-aware gradient regulation achieve significantly better performance under comparable generation lengths, enabling stable and effective adaptive thinking.

[80] h3: 4.3 Analysis of Adaptive Thinking

[81] p: We further analyze model behavior across problems of varying difficulty to evaluate the effectiveness of adaptive thinking. As shown in Figure 3 (a), on the relatively easy MATH-500 benchmark, the proposed method selects the no-thinking mode for up to 77.6% of the queries, whereas on the more challenging AIME-2024 and AIME-2025 benchmarks, it activates the thinking mode more frequently. Notably, performance under the no-thinking mode consistently surpasses that under the thinking mode, indicating that the model learns to adaptively select the more appropriate strategy according to problem difficulty. Figures 3 (b) and 3 (c) further illustrate the model’s thinking behavior across different difficulty levels within MATH-500. As the difficulty increases, the model progressively increases its reliance on the thinking mode. Compared with the original model that exclusively uses either the thinking or no-thinking mode, our method consistently achieves superior performance across all difficulty levels. These results demonstrate that the proposed approach attains a more favorable balance between reasoning efficiency and accuracy.

[82] h3: 4.4 Ablation and Sensitivity Analysis

[83] h4: Effect of CPAS.

[84] p: Figure 4 (a) illustrates the training dynamics with and without CPAS. Compared with the baseline, our method exhibits a faster increase in response length at early stages and reaches a higher peak, indicating earlier and deeper exploration. The length then gradually decreases and converges to a similar level, achieving stable adaptive thinking behavior. Evaluation on the AIME benchmarks further shows that our method consistently outperforms the baseline, demonstrating a better balance between accuracy and efficiency, which confirms the effectiveness of CPAS.

[85] h4: Effect of LAGR.

[86] p: We analyze the impact of LAGR under different parameters. As shown in Figure 4 (b) left, values of β \beta closer to 1 encourage no-thinking chains, whereas values closer to 0 promote the thinking exploration. An intermediate setting of β = 0.4 \beta=0.4 provides the best trade-off between accuracy and efficiency. Figure 4 (b) right examines the effect of control-token weighting. When the weight is set to 1, the ratio between thinking and no-thinking modes remains largely unchanged, indicating that the control signal is diluted. Increasing the weight to 10 enables stable adaptive thinking, while larger weights induce overly aggressive updates, prematurely assigning solvable samples to the thinking mode and reducing efficiency.

[87] h3: 4.5 Generalization Analysis

[88] p: We evaluate out-of-distribution (OOD) generalization on the GPQA benchmark, which consists of graduate-level multiple-choice questions spanning diverse scientific domains and differs from the training data in both question format and content. As shown in Table 2 , our method achieves the highest accuracy while reducing the average response length by 51.0%. The model activates the no-thinking mode for 31.3% of the queries, yielding substantial efficiency gains without compromising performance. These results demonstrate that our approach generalizes effectively to OOD settings, enabling robust and efficient adaptive thinking.

[89] figure: Table 2: OOD Performance on GPQA Dataset. Method GPQA Acc Len Ratio NT Δ \Delta Len Thinking 47.5 24135 0.0% – No-Thinking 35.3 8031 100.0% -66.7% HFT 41.8 16849 44.1% -30.2% Ours 50.4 11826 31.3% -51.0%

[90] h2: 5 Related Work

[91] h3: 5.1 Large Reasoning Models

[92] p: Large reasoning models OpenAI et al. (2024) ; DeepSeek-AI et al. (2025a) have recently attracted substantial attention due to their superior performance. Enabled by scalable reinforcement learning He et al. (2025b) ; Yu et al. (2025a) ; Zheng et al. (2025) , these models can generate long reasoning chains using only outcome-based and format rewards, leading to improved performance in complex reasoning tasks. To further generalize in various scenarios, previous work has explored reinforcement learning with verifiable rewards Yu et al. (2025b) and introduced explicit supervision over the reasoning process Zhang et al. (2025b) . However, most existing approaches overlook the efficiency issues caused by long redundant reasoning chains, which increases the inference cost. Creating efficient reasoning without sacrificing performance remains an open challenge.

[93] h3: 5.2 Efficient Reasoning for LRMs

[94] p: Efficient reasoning for LRMs aims to reduce overthinking while preserving accuracy. One line of work focuses on compressing or regularizing reasoning traces via prompting, supervised tuning with variable-length CoT, or length-regularized RL Chen et al. (2024) ; Ma et al. (2025) ; Aggarwal and Welleck (2025) ; Luo et al. (2025a) . These methods typically assume reasoning is always necessary and may restrict the exploration. Another line studies hybrid thinking via routing, allocating compute by switching between thinking and no-thinking models based on task difficulty He et al. (2025a) ; Liang et al. (2025) ; OpenAI (2025) , but it often requires external supervision and deployment costs. More recently, RL-based adaptive thinking learns when to think using explicit control tokens or rewards for no-thinking behaviors Fang et al. (2025) ; Jiang et al. (2025) ; Zhang et al. (2025a) ; Lou et al. (2025) ; Chen et al. (2025) . However, achieving stable optimization under the efficiency–accuracy trade-off remains challenging, motivating our stability-oriented approach.

[95] h2: 6 Conclusion

[96] p: In this work, we address the training instability caused by heterogeneous reasoning lengths in existing adaptive thinking methods, as well as the difficulty of jointly optimizing reasoning accuracy and efficiency. We propose a novel two-stage framework for stable adaptive thinking. In Stage I, we adopt HFT to endow the model with both thinking and no-thinking modes. In Stage II, CPAS preserves the model’s ability to explore long reasoning chains, while LAGR stabilizes reinforcement learning training. Extensive experiments demonstrate that our approach achieves a better balance between performance and efficiency, underscoring the potential of our proposed advantage-based model optimization strategy for reinforcement learning.

[97] h2: Limitations

[98] p: In this section, we discuss several limitations of this work. First, due to computational constraints, our empirical evaluation is limited to models at the 1.5B and 7B scales. While consistent improvements across these settings demonstrate the effectiveness of the proposed approach, experiments on larger models would be valuable for more thoroughly assessing its scalability. Second, our training primarily relies on mathematical reasoning datasets, which offer reliable and verifiable reward signals. Although evaluations on GPQA indicate promising out-of-distribution generalization, extending training to more diverse domains with trustworthy verification mechanisms may further enhance robustness and applicability.

[99] h2: References

[100] h2: Appendix

[101] h2: A Experimental Details

[102] h3: A.1 Data Construction

[103] p: To initialize both thinking and no-thinking behaviors in a unified policy, we construct a hybrid-formatted training corpus that explicitly contains paired supervision for the two reasoning modes.

[104] h4: Data Sources.

[105] p: The HFT dataset is built from large-scale public mathematical corpora, including OpenR1-Math, DeepMath-103K, and NuminaMath, which cover diverse problem types requiring numerical computation and multi-step reasoning.

[106] h4: Hybrid Supervision Construction.

[107] p: For each problem, we construct paired supervision corresponding to two reasoning modes:

[108] p: Thinking mode. Long-form trajectories are distilled from DeepSeek-R1-0528, prefixed with the control token /think and containing an explicit reasoning block <think>... </think> followed by the final answer.

[109] p: No-thinking mode. Short direct-answer responses are distilled from DeepSeek-V3-0324, prefixed with /no_think and including an empty reasoning block <think></think> .

[110] p: The two types of supervision are balanced with a 1:1 ratio to avoid introducing bias toward either reasoning mode during supervised warm-up.

[111] h4: Verification.

[112] p: All constructed responses are verified using the Math-Verify module, and samples that fail verification are discarded. This step ensures correctness and reliability of both thinking and no-thinking supervision.

[113] p: Overall, after verification and filtering, we obtain a hybrid corpus consisting of approximately 600K thinking samples and 600K no-thinking samples, providing clean, balanced supervision for initializing adaptive thinking policies.

[114] h3: A.2 Baselines

[115] figure: Table 3: Appendix Results on Diverse Model Sizes and Architectures. Method MATH-500 AIME-2024 AIME-2025 Acc Len Ratio N ​ T \text{Ratio}_{NT} Acc Len Ratio N ​ T \text{Ratio}_{NT} Acc Len Ratio N ​ T \text{Ratio}_{NT} Qwen-2.5-1.5B Thinking 80.4 10441 0.0% 25.7 35829 0.0% 20.6 36977 0.0% No-Thinking 60.4 2320 100.0% 9.1 10751 100.0% 7.5 11150 100.0% HFT 72.3 7106 42.4% 16.8 23673 54.2% 14.5 25376 46.2% Ours 84.6 4176 69.8% 28.1 23258 3.7% 25.2 22062 5.4% Qwen-2.5-7B Thinking 90.6 8309 0.0% 65.6 29936 0.0% 59.3 35217 0.0% No-Thinking 75.1 1890 100.0% 25.5 10464 100.0% 20.2 9921 100.0% HFT 86.3 5619 45.2% 50.9 23484 42.5% 44.2 25017 40.4% Ours 92.4 3403 77.6% 69.2 17762 12.5% 64.6 20060 9.6% Llama3.1-8B Thinking 89.8 9046 100.0% 63.3 31294 100.0% 55.7 34801 100.0% No-Thinking 72.1 2423 0.0% 20.6 9112 0.0% 17.5 10905 0.0% HFT 82.2 5619 48.8% 44.7 22388 46.3% 37.1 22938 49.2% Ours 90.8 3618 75.5% 66.7 19089 10.1% 60.4 21084 8.7%

[116] p: To comprehensively evaluate the effectiveness of the proposed approach, we compare against a diverse set of baselines that represent different strategies for controlling reasoning length and inference efficiency. All baselines are evaluated under the same experimental settings and verification protocols unless otherwise specified.

[117] h4: Base Variants.

[118] p: We first consider several variants derived from the same base language model to isolate the effect of reasoning behaviors:

[119] p: Thinking-only. The model always operates in the thinking mode, generating explicit chain-of-thought reasoning for every input. This variant provides the deepest level of reasoning but incurs substantial token overhead.

[120] p: No-thinking-only. The model always generates direct answers without intermediate reasoning. While this variant is computationally efficient, it typically suffers from degraded performance on complex problems.

[121] p: HFT. The hybrid fine-tuned model trained with both thinking and no-thinking supervision, as described in Appendix A.1 . This model possesses both capabilities but does not autonomously decide which mode to use.

[122] h4: Length-Penalization Methods.

[123] p: We include methods that discourage excessively long reasoning chains by explicitly penalizing output length:

[124] p: O1-Pruner Luo et al. (2025a) . This approach introduces length-aware constraints during fine-tuning to prune redundant reasoning steps while maintaining correctness. It operates exclusively within the thinking mode and does not support explicit no-thinking behavior.

[125] h4: Routing-Based Methods.

[126] p: Routing approaches aim to reduce inference cost by dynamically selecting between different reasoning strategies:

[127] p: RouteLLM Ong et al. (2024) . This method trains an external router to select between a thinking model and a no-thinking model at inference time. While effective in reducing token usage, it relies on additional supervision for router training and requires maintaining multiple models during deployment.

[128] h4: Adaptive Thinking Methods.

[129] p: We further compare against recent reinforcement-learning-based adaptive thinking approaches:

[130] p: ThinkLess Fang et al. (2025) . This method adopts a decoupled GRPO formulation to encourage shorter chains, learning a hybrid policy over thinking and no-thinking behaviors.

[131] p: AdaptThink Zhang et al. (2025a) . This approach employs a PPO-based objective that explicitly promotes concise reasoning by increasing the likelihood of short chains.

[132] p: Both ThinkLess and AdaptThink share the same HFT initialization as our method, ensuring fair comparison and controlled base model capacity.

[133] h4: Evaluation Protocol.

[134] p: All methods are evaluated using the same datasets, verification module (Math-Verify 1 1 1 https://github.com/huggingface/Math-Verify ), and decoding settings. We report accuracy, average generation length, and the no-thinking ratio to jointly measure reasoning performance and efficiency. For MATH-500, all reported results are averaged over 4 independent runs. For AIME-2024 and AIME-2025, results are averaged over 32 independent runs to reduce variance.

[135] h3: A.3 Implementation Details

[136] p: All experiments are conducted on 16 NVIDIA H100 GPUs. We implement the Hybrid Fine-Tuning (HFT) stage using LLaMA-Factory 2 2 2 https://github.com/hiyouga/LlamaFactory and the reinforcement learning stage using VeRL 3 3 3 https://github.com/volcengine/verl .

[137] h4: HFT.

[138] p: In the HFT stage, the maximum context length is set to 16K tokens, with overlong samples truncated. Models are trained for 3 epochs with the AdamW optimizer, using a 10% linear warmup followed by cosine learning rate decay, and a peak learning rate of 1 × 10 − 4 1\times 10^{-4} .

[139] h4: Reinforcement Learning.

[140] p: In the RL stage, the context length is extended to 24K tokens. The policy model is optimized with AdamW using a constant learning rate of 1 × 10 − 6 1\times 10^{-6} . We use a batch size of 128 with a micro-batch size of 64, and sample G = 8 G{=}8 responses per query during rollout.

[141] h2: B Additional Experimental Results

[142] p: To further assess the generality of our approach, we conduct additional experiments beyond the Qwen2.5 series. Specifically, we apply the same training pipeline to LLaMA 3.1-8B Base, which adopts a different architecture and pretraining recipe. All training and optimization procedures strictly follow the HFT and RL settings described in Appendix A.3 , with only minimal hyperparameter adjustments for model size. No architecture-specific modifications are introduced.

[143] p: As shown in Table 3 , our method consistently improves reasoning accuracy while substantially reducing the average generation length under the LLaMA architecture. These results demonstrate that the proposed correctness-preserving advantage shaping and length-aware gradient regulation are not specific to a particular backbone, but instead generalize well across different model families.

[144] h2: C Case Study

[145] figure: Question (MATH500) : Convert the point ( 0 , 3 ) (0,3) in rectangular coordinates to polar coordinates. Enter your answer in the form ( r , θ ) , (r,\theta), where r > 0 r>0 and 0 ≤ θ < 2 ​ π . 0\leq\theta<2\pi. Format your response as follows: “The correct answer is boxed{insert answer here}.” Thinking : <think> I need to convert the point ( 0 , 3 ) (0,3) from rectangular coordinates to polar coordinates. Polar coordinates are given as ( r , θ ) (r,\theta) , where r r is the distance from the origin to the point, and θ \theta is the angle from the positive x x -axis. First, recall the formulas for converting from rectangular to polar coordinates. The formulas are: r = x 2 + y 2 r=\sqrt{x^{2}+y^{2}} and θ = tan − 1 ⁡ ( y / x ) \theta=\tan^{-1}(y/x) . […]( omit ) which is not the same point. So, only θ = π / 2 \theta=\pi/2 is correct. I could use θ = π / 2 + 2 ​ k ​ π \theta=\pi/2+2k\pi , but within 0 0 to 2 ​ π 2\pi , only π / 2 \pi/2 . 2 ​ π 2\pi would be 5 ​ π / 2 5\pi/2 , which is greater than 2 ​ π 2\pi , so no. So, I think ( 3 , π / 2 ) (3,\pi/2) is the answer. The problem says “enter your answer in the form ( r , θ ) (r,\theta) ”, and “boxed”. So, I need to write it as ( 3 , π 2 ) (3,\frac{\pi}{2}) in the box. The instruction says: “output the final answer within \boxed{} ” and “enter your answer as ( r , θ ) (r,\theta) ”, so, probably ( 3 , π 2 ) (3,\ \frac{\pi}{2}) . But let me make sure the format. Sometimes they write it as a pair. I think that’s fine. Is there any other representation? For example, could r r be negative? But the problem specifies r > 0 r>0 , so no. Or θ \theta could be different, but no. Another thing: when x = 0 x=0 and y > 0 y>0 , it’s unambiguously π / 2 \pi/2 . If it were ( 0 , − 3 ) (0,-3) , it would be 3 ​ π / 2 3\pi/2 or − π / 2 -\pi/2 , but since it’s positive, it’s fine. So, I think that’s it. The point is ( 0 , 3 ) (0,3) , which is on the y y -axis, so θ = 90 \theta=90 degrees, which is π / 2 \pi/2 radians. Yes. So, final answer. </think> Final Answer: To convert the point ( 0 , 3 ) (0,3) from rectangular coordinates to polar coordinates ( r , θ ) (r,\theta) with r > 0 r>0 and 0 ≤ θ < 2 ​ π 0\leq\theta<2\pi , calculate r = x 2 + y 2 = 0 2 + 3 2 = 3 r=\sqrt{x^{2}+y^{2}}=\sqrt{0^{2}+3^{2}}=3 . Since x = 0 x=0 and y > 0 y>0 , the point lies on the positive y y -axis, so θ = π / 2 \theta=\pi/2 , and π / 2 ∈ [ 0 , 2 ​ π ) \pi/2\in[0,2\pi) . Thus, the polar coordinates are ( 3 , π / 2 ) (3,\pi/2) , i.e., the correct answer is ( 3 , π 2 ) \boxed{\left(3,\ \dfrac{\pi}{2}\right)} . (3272 tokens) Ours : /nothink <think></think> To convert the rectangular coordinates ( ( , , , ) ) ((0,3)) to polar coordinates ( r , θ ) (r,\theta) , follow these steps: 1. Calculate r r (the distance from the origin to the point): The formula for r r is: r = x 2 + y 2 r=\sqrt{x^{2}+y^{2}} Substituting x = 0 x=0 and y = 3 y=3 : r = 0 2 + 3 2 = 9 = 3 r=\sqrt{0^{2}+3^{2}}=\sqrt{9}=3 2. Determine θ \theta (the angle with the positive x x -axis): Since the point ( ( , , , ) ) ((0,3)) lies on the positive y y -axis, the angle θ \theta is: θ = π 2 \theta=\frac{\pi}{2} This is because the positive y y -axis corresponds to 90 ∘ 90^{\circ} or ( π 2 ) \left(\frac{\pi}{2}\right) radians in the range 0 ≤ θ < 2 ​ π 0\leq\theta<2\pi . 3. Combine the results: The polar coordinates are: ( 3 , π 2 ) (3,\frac{\pi}{2}) Final Answer: ( 3 , π 2 ) \boxed{\left(3,\dfrac{\pi}{2}\right)} (713 tokens) Figure 5: For an example from MATH-500, the Thinking baseline generates a long chain-of-thought with redundant intermediate steps. In contrast, our method chooses NoThinking and directly produces a concise final solution, using 713 tokens in total.

[146] figure: Question (AIME) : Find the largest possible real part of ( 75 + 117 ​ i ) ​ z + 96 + 144 ​ i z \left(75+117i\right)z+\dfrac{96+144i}{z} where z z is a complex number with | z | = 4 |z|=4 . Thinking : <think> I need to find the largest possible real part of ( 75 + 117 ​ i ) ​ z + 96 + 144 ​ i z (75+117i)z+\frac{96+144i}{z} where z z is a complex number with magnitude 4. Since | z | = 4 |z|=4 , I can write z = 4 ​ e i ​ θ z=4e^{i\theta} for some real θ \theta , or equivalently, z = 4 ​ ( cos ⁡ θ + i ​ sin ⁡ θ ) z=4(\cos\theta+i\sin\theta) . Let me denote the expression as w = ( 75 + 117 ​ i ) ​ z + 96 + 144 ​ i z w=(75+117i)z+\frac{96+144i}{z} . I need the real part of w w , and maximize it. Since z z is on the circle of radius 4, I could set z = x + i ​ y z=x+iy with x 2 + y 2 = 16 x^{2}+y^{2}=16 , but that might get messy with the algebra. Notice that the expression involves both z z and 1 / z 1/z , and since | z | = 4 |z|=4 , | 1 / z | = 1 / 4 |1/z|=1/4 . Also, the coefficients are complex numbers, so I need to handle that. Let me simplify the coefficients. […](omit) So real part is Re( (r + i s)/4 * (cos θ \theta - i sin θ \theta ) ) = (1/4) Re( (r + i s)(cos θ \theta - i sin θ \theta ) ) = (1/4) [ r cos θ \theta - r i sin θ \theta + i s cos θ \theta - i 2 i^{2} s sin θ \theta ] = (1/4) [ r cos θ \theta + s sin θ \theta + i ( -r sin θ \theta + s cos θ \theta ) ] So real part is (1/4)(r cos θ \theta + s sin θ \theta ) Similarly, from first term: 4 [ (p + i q)(cos θ \theta + i sin θ \theta ) ] = 4 [ p cos θ \theta - q sin θ \theta + i (p sin θ \theta + q cos θ \theta ) ], so real part 4(p cos θ \theta - q sin θ \theta ) Thus total real part Re(w) = 4 ​ ( p ​ cos ⁡ θ − q ​ sin ⁡ θ ) + 1 4 ​ ( r ​ cos ⁡ θ + s ​ sin ⁡ θ ) 4(p\cos\theta-q\sin\theta)+\frac{1}{4}(r\cos\theta+s\sin\theta) Now plug in p=75, q=117, r=96, s=144. So Re(w) = 4 ​ ( 75 ​ cos ⁡ θ − 117 ​ sin ⁡ θ ) + 1 4 ​ ( 96 ​ cos ⁡ θ + 144 ​ sin ⁡ θ ) 4(75\cos\theta-117\sin\theta)+\frac{1}{4}(96\cos\theta+144\sin\theta) Compute: 4*75=300, 4*(-117)= -468, so 300 cos ⁡ θ \cos\theta - 468 sin ⁡ θ \sin\theta Then 1 4 ∗ 96 = 24 \frac{1}{4}*96=24 , 1 4 ∗ 144 = 36 \frac{1}{4}*144=36 , so +24 cos ⁡ θ \cos\theta + 36 sin ⁡ θ \sin\theta Thus total: (300 + 24) cos ⁡ θ \cos\theta + (-468 + 36) sin ⁡ θ \sin\theta = 324 cos ⁡ θ \cos\theta - 432 sin ⁡ θ \sin\theta , same as before. So no mistake. Thus maximum is 324 2 + ( − 432 ) 2 = 104976 + 186624 = 291600 = 540 . \sqrt{324^{2}+(-432)^{2}}=\sqrt{104976+186624}=\sqrt{291600}=540. So the largest possible real part is 540. Therefore, the answer is 540. But the problem says "real part", and I got it, so I think that’s it. </think> To find the largest possible real part of ( 75 + 117 ​ i ) ​ z + 96 + 144 ​ i z (75+117i)z+\frac{96+144i}{z} where z z is a complex number with | z | = 4 |z|=4 , express z z in polar form as z = 4 ​ e i ​ θ z=4e^{i\theta} for some real θ \theta . This gives z = 4 ​ ( cos ⁡ θ + i ​ sin ⁡ θ ) z=4(\cos\theta+i\sin\theta) . Define the expression as w = ( 75 + 117 ​ i ) ​ z + 96 + 144 ​ i z w=(75+117i)z+\frac{96+144i}{z} . Substitute z z : w = ( 75 + 117 ​ i ) ⋅ 4 ​ ( cos ⁡ θ + i ​ sin ⁡ θ ) + 96 + 144 ​ i 4 ​ ( cos ⁡ θ + i ​ sin ⁡ θ ) . w=(75+117i)\cdot 4(\cos\theta+i\sin\theta)+\frac{96+144i}{4(\cos\theta+i\sin\theta)}. Simplify the second term: 96 + 144 ​ i 4 ​ ( cos ⁡ θ + i ​ sin ⁡ θ ) = 96 + 144 ​ i 4 ⋅ 1 cos ⁡ θ + i ​ sin ⁡ θ = ( 24 + 36 ​ i ) ⋅ cos ⁡ θ − i ​ sin ⁡ θ 1 , \frac{96+144i}{4(\cos\theta+i\sin\theta)}=\frac{96+144i}{4}\cdot\frac{1}{\cos\theta+i\sin\theta}=(24+36i)\cdot\frac{\cos\theta-i\sin\theta}{1}, since 1 cos ⁡ θ + i ​ sin ⁡ θ = cos ⁡ θ − i ​ sin ⁡ θ \frac{1}{\cos\theta+i\sin\theta}=\cos\theta-i\sin\theta for | z | = 4 |z|=4 . […](omit) This maximum is achieved for some θ \theta , such as when cos ⁡ θ = 3 5 \cos\theta=\frac{3}{5} and sin ⁡ θ = − 4 5 \sin\theta=-\frac{4}{5} , giving Re ⁡ ( w ) = 540 \operatorname{Re}(w)=540 . Since the function is continuous and the circle | z | = 4 |z|=4 is compact, the maximum value is attained. Thus, the largest possible real part is 540. (22383 tokens) Ours : /nothink <think></think> Alright, I have this problem: Find the largest possible real part of ( 75 + 117 ​ i ) ​ z + 96 + 144 ​ i z (75+117i)z+\frac{96+144i}{z} where z z is a complex number with | z | = 4 |z|=4 . Understanding the Problem First, I need to understand what’s being asked. We have a complex expression in terms of z z , and z z is a complex number with magnitude 4. The goal is to find the maximum real part of this expression. Step 1: Represent z z in a Convenient Form Since z z is a complex number with | z | = 4 |z|=4 , it can be written in polar form as: z = 4 ​ e i ​ θ z=4e^{i\theta} where θ \theta is the argument of z z . But before jumping into polar form, maybe it’s easier to think of z z in terms of its real and imaginary parts: z = x + i ​ y z=x+iy where x , y x,y are real numbers, and x 2 + y 2 = 16 x^{2}+y^{2}=16 because | z | = 4 |z|=4 . Step 2: Rewrite the Expression The expression is: […](omit) x = 3 5 × 4 = 12 5 x=\frac{3}{5}\times 4=\frac{12}{5} y = − 4 5 × 4 = − 16 5 y=\frac{-4}{5}\times 4=\frac{-16}{5} Now, plug these into ( 81 ​ x − 108 ​ y ) (81x-108y) : 81 × 12 5 − 108 × − 16 5 = 972 5 + 1728 5 = 972 + 1728 5 = 2700 5 = 540 81\times\frac{12}{5}-108\times\frac{-16}{5}=\frac{972}{5}+\frac{1728}{5}=\frac{972+1728}{5}=\frac{2700}{5}=540 This matches our previous result. Conclusion The largest possible real part of the given expression is 540 540 . (2977 tokens) Figure 6: For an example from AIME, the Thinking baseline generates a long chain-of-thought with redundant intermediate steps. In contrast, our method chooses NoThinking and directly produces a concise final solution, using 2977 tokens in total.

[147] figure: Question (GPQA) : Answer the following multiple choice question. The last line of your response should be of the following format: ’Answer: $LETTER’ (without quotes) where LETTER is one of ABCD. Think step by step before answering. "Oh, I know you," the ribonucleoprotein particle says to the nascent chain as they meet. "Pause there for a minute. Let me show you in; you really need some sugar." "It seems somewhat rough. I guess this is goodbye; I need to be on my way", the chain replies. Where did they meet, and where is the chain heading? A) Golgi to the mitochondrion B) membrane to the nucleus C) cytosol to the extracellular space D) ribosome to the proteasome. Thinking : <think> I need to figure out where the ribonucleoprotein particle and the nascent chain meet, and where the chain is heading. The options are: A) Golgi to the mitochondrion B) membrane to the nucleus C) ribosome to the proteasome D) cytosol to the extracellular space First, I recall that the ribonucleoprotein particle (RNP) is involved in transporting nucleotides into cells. Nucleotides are the building blocks of DNA and RNA. The nascent chain is probably a nascent protein, which is a protein that’s being synthesized by the ribosome. […](omit) So, option D. Perhaps in some contexts, "cytosol" is used for the cell membrane. I think I’ll go with D. But let’s see if there’s a better fit. Option A: "Golgi to the mitochondrion" – if the chain is heading to the Golgi, but why would it be at "Golgi to mitochondrion". Perhaps for a protein that is going to the mitochondrion, but the question is about a general nascent chain needing nucleotides, not necessarily for a specific location. So, unlikely. Perhaps in this case, after meeting, it’s heading to the Golgi, and the meeting is at the cytoplasm, but not specified. I think D is the most plausible. Perhaps B: "membrane to the nucleus" – for a protein that is being integrated, but again, not for nucleotide entry. I think D is the answer. So, I’ll say D. But let’s confirm. Final answer. </think> The ribonucleoprotein particle (RNP) shuttles nucleotides (Sugar) into cells, and the nascent chain (a protein being synthesized) is present in the cytoplasm. […](omit) - B) Membrane to the nucleus: Incorrect, as this is typically for secreted proteins that integrate into the nucleus, but the chain needs nucleotides for assembly, not nuclear integration. - C) Ribosome to the proteasome: Incorrect, as the ribosome and proteasome are locations for different processes; the ribosome assembles the protein, while proteasomal degradation occurs later. - D) Cytosol to extracellular space: Correct, as the meeting occurs at the cell membrane (boundary of cytoplasm and extracellular space), and the chain heads to the extracellular space after receiving the nucleotides. Thus, they meet at the cell membrane (described as "cytosol to extracellular space"), and the chain is heading to the extracellular space. (22149 tokens) Ours : /nothink <think></think> Let’s think step by step to answer the question. Understanding the Question: The question is a multiple-choice question about the meeting place and destination of a nascent (newly synthesized) protein chain. The options are: - A) Golgi to the mitochondrion […](omit) This fits because the cytoplasm (where the ribonucleoprotein is located) processes the protein, and the processed protein then exits the cell to the extracellular space. - D) Ribosome to the proteasome: The ribosome is where protein synthesis occurs, and the proteasome is involved in protein degradation. The described process is not about moving from the ribosome to the proteasome but about processing and exiting. Conclusion: The correct answer is C) cytosol to the extracellular space, as the ribonucleoprotein processes the nascent protein in the cytoplasm, and the processed protein is then released into the extracellular space. (2197 tokens) Figure 7: For an example from GPQA, the Thinking baseline generates a long chain-of-thought with redundant intermediate steps. In contrast, our method chooses NoThinking and directly produces a concise final solution, using 2197 tokens in total.

[148] h2: Instructions for reporting errors

[149] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[150] p: Tip: You can select the relevant text first, to include it in your report.

[151] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[152] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
