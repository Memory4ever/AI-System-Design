# Exact-v1 necessary primary — 2601.19404

Original returned context retained; only necessary core, controls, setup and direct counterclaims adopted.

## jan29_systemfour_head

RPO:Reinforcement Fine-Tuning with Partial Reasoning Optimization (https://arxiv.org/html/2601.19404v1)
citeturn28514view0 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19404v1","lineno":null}); Total lines: 605
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Work L18:     1. cite8†Reinforcement Fine-Tuning. L19:     2. cite9†Experience Replay. L20:   4. cite10†3 Method L21:     1. cite11†3.1 Cache Pool Initialization L22:     2. cite12†3.2 Rollout And Optimization L23:     3. cite13†3.3 Cache Update L24:     4. cite14†3.4 Length-Aware Reward Shaping L25:   5. cite15†4 Experiments L26:     1. cite16†4.1 Experimental Setup L27:       1. cite17†Base Models. L28:       2. cite18†Datasets. L29:       3. cite19†Implementation Details. L30:     2. cite20†4.2 Zero-shot performance L31:     3. cite21†4.3 Training Time Overhead L32:     4. cite22†4.4 Stability Analysis L33:   6. cite23†5 More Analysis L34:     1. cite24†Impact of Maximum Truncation Length and $\alpha$. L35:     2. cite25†Effect of max_length on Exploration Capability. L36:     3. cite26†Impact of Cache Pool Update Strategy on Model’s Pass@N Performance. L37:   7. cite27†6 Conclusion L38:   8. cite28†References L39:   9. cite29†A Proof of RPO Gradient Stability L40:     1. cite30†Policy gradient estimation. L41:     2. cite31†Gradient of the optimization policy. L42:     3. cite32†Resulting policy gradient. L43:     4. cite33†Without consideration of KL divergence. L44:     5. cite34†Including the KL divergence. L45:   10. cite35†B theorem L46:     1. cite36†Preliminary. L47:     2. cite37†Proof. L48:     3. cite38†Remark. L49:   11. cite39†C Using a large model’s cache pool to guide small model training L50:   12. cite40†D Cost Overhead L51:   13. cite41†E More Analysis L52:     1. cite42†The impact of cache pool update strategies. L53:   14. cite43†F Time Overhead for Cache Pool Initialization L54:   15. cite44†G Pseudo Code for RPO Training Process L55: cite45†License: arXiv.org perpetual non-exclusive license†info.arxiv.org L56: 
L57: arXiv:2601.19404v1 [cs.AI] 27 Jan 2026
L58: # RPO:Reinforcement Fine-Tuning with Partial Reasoning Optimization
L59: Hongzhu Yi    Xinming Wang    Zhenghao zhang    Tianyu Zong    Yuanxiang Wang    Jun Xie    Tao Yu    Haopeng Jin Affiliation: Zhepeng Wang, Kaixin Xu, Feng Chen, Jiahuan Chen, Yujia Yang, Zhenyu Guan, Bingkang Shi, Jungang Xu* Affiliation: {yihongzhu23, zhangzhenghao25, guanzhenyu24}@mails.ucas.ac.cn Affiliation: {zongtianyu20,yangyujia24, wangyuanxiang19}@mails.ucas.ac.cn Email: {wangxinming2024,yutao2025}@ia.ac.cn Email: orangenius@sjtu.edu.cn Email: {xiejun,chenfeng13,wangzpb}@lenovo.com Email: sunbeam.King@bupt.edu.cn Email: xujg@ucas.ac.cn
L60: ###### Abstract
L61: Within the domain of large language models, reinforcement fine-tuning algorithms necessitate the generation of a complete reasoning trajectory beginning from the input query, which incurs significant computational overhead during the rollout phase of training.
L62: To address this issue, we analyze the impact of different segments of the reasoning path on the correctness of the final result and, based on these insights, propose Reinforcement Fine-Tuning with Partial Reasoning Optimization (RPO), a plug-and-play reinforcement fine-tuning algorithm. Unlike traditional reinforcement fine-tuning algorithms that generate full reasoning paths, RPO trains the model by generating suffixes of the reasoning path using experience cache.
L63: During the rollout phase of training, RPO reduces token generation in this phase by approximately 95%, greatly lowering the theoretical time overhead. Compared with full-path reinforcement fine-tuning algorithms, RPO reduces the training time of the 1.5B model by 90% and the 7B model by 72%. At the same time, it can be integrated with typical algorithms such as GRPO and DAPO, enabling them to achieve training acceleration while maintaining performance comparable to the original algorithms.
L64: Our code is open-sourced at cite46†https://github.com/yhz5613813/RPO†github.com .
L65: ## 1 Introduction
L66: In recent years, large language models (LLMs) (cite47†OpenAI et al., 2024a ; cite48†Touvron et al., 2023 ; cite49†Zeng et al., 2023 ) have achieved remarkable breakthroughs in reasoning and generalization capabilities (cite50†Wang et al., 2025a ), particularly after the introduction of reinforcement learning during the post-training stage (cite51†Ouyang et al., 2022 ).
L67: Pioneering works such as OpenAI’s O1 (cite52†OpenAI et al., 2024b ) and DeepSeek-R1 (cite53†DeepSeek-AI et al., 2025 ) have demonstrated impressive reasoning-time efficiency, primarily due to the synergistic combination of reinforcement learning and chain-of-thought (CoT) reasoning (cite54†Wei et al., 2023 ). This paradigm shift highlights the transformative potential of Reinforcement Learning-based post-training in pushing the boundaries of LLM performance.
L68: Despite its promising prospects, applying reinforcement learning in post-training remains immature. In terms of time overhead, Reinforcement Learning fine-tuning typically generates a large number of samples during the sampling stage. However, parameter updates cannot proceed until all samples are completed, resulting in severe underutilization of computational resources.
L69: Although some asynchronous Reinforcement Learning approaches exist, the off-policy nature of the optimization process requires more training iterations. Furthermore, during Reinforcement Learning fine-tuning of language models, rewards are usually computed only after generating the final token based on task-specific criteria. This paradigm, known as Reinforcement Learning with Verifiable Rewards (cite55†Lambert et al., 2025 ; cite56†Wang et al., 2025b ), lacks intermediate feedback and produces sparse rewards.
L70: Such sparsity hinders the model’s ability to learn optimal policies and contributes to training instability (cite57†Lightman et al., 2023 ).
L71: We observe that a significant underlying issue stems from the policy model’s need to identify a reasoning trajectory from the beginning of the problem to the correct answer. This approach—comparing entire reasoning paths using policy gradients—leads to excessive randomness during the sampling phase. Although it expands the search space, it often fails to find suitable reasoning paths, resulting in inefficient sampling and high variance.
L72: An alternative perspective arises: since exploring a complete reasoning path from the beginning of the problem introduces various drawbacks, why not train the policy model to complete a reasoning path based on partially correct reasoning process hint instead? We found that this is feasible. Through our experiments, enabling the model to complete correct reasoning paths can still effectively teach it to generate whole reasoning trajectories from the initial problem statement.
L73: Based on this insight, we propose the R eplay-based P olicy O ptimization(RPO). Our method is grounded in a reasonable assumption: the early tokens of a reasoning path that leads to the correct answer are more likely to guide the model toward the correct reasoning trajectory. Furthermore, we investigate the relationship between the length of the truncated trailing tokens and the model’s generation accuracy.
L74: As shown in Figure cite58†1 , the initial tokens of correct answers play a crucial role in guiding the model toward correct solutions, and longer prefix lengths are positively correlated with higher generation accuracy.
L75: Specifically, we construct a cache pool for reinforcement fine-tuning to store previously generated reasoning paths and continuously update it during training. After completing the sampling generation stage for each question, we add the reasoning path that leads to the correct answer into the cache. When the same question is encountered again, we retrieve the first $n$ tokens of the corresponding reasoning path from the cache, prepend them to the prompt, and then perform sampling generation.
L76: At the same time, we design a reward function that adaptively adjusts based on response length to improve the accuracy of gradient estimation in the experience caching scenario.
L77: Experimental results show that this method is plug-and-play, concise and effective, enhances training stability during the reinforcement learning stage, significantly reduces the policy model’s sampling time cost, and achieves performance improvements.
L78: We propose RPO, a novel framework for reinforcement fine-tuning of LLMs, introducing an experience replay mechanism in the sampling stage. Key advantages are: plug-and-play: allowing easy integration into other Reinforcement Learning fine-tuning methods; reduced resource consumption: achieving up to 92.6% faster training; strong stability: mitigating common Reinforcement Learning instability in reasoning models.We evaluated RPO on Deepseek-R1-Distill-Qwen 1.5B and 7B models across six datasets.
L79: The results show that training time was reduced by approximately 90%, and compared to full-path exploration in GRPO and DAPO, performance improved by about 2%.
L80: cite59†Image: Refer to caption L81: 
L82: cite60†Image: Refer to caption L83: Figure 1: The top figure shows the DeepSeekR1-Qwen-Distill-7b and DeepSeekR1-Qwen-Distill-1.5b models. For each question, an initial answer is generated and then truncated; from the truncation point, 256 answers are subsequently generated, and the relationship between truncation length and the overall average accuracy is analyzed. The bottom figure shows 256 answers generated for each training question.
L84: Answers exceeding 2048 tokens are selected, and BERT is used to measure the similarity between equal-length prefix segments. The similarity metric is defined as: $\text{sim}=\frac{2}{n(n-1)}\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}\frac{\text{BERT}(s_{i})\cdot\text{BERT}(s_{j})^{\top}}{\|\text{BERT}(s_{i})\|\,\|\text{BERT}(s_{j})\|}$.
L85: ## 2 Related Work
L86: #### Reinforcement Fine-Tuning.
L87: Reinforcement Fine-Tuning (RFT) guides the model fine-tuning process through the reward mechanisms of reinforcement learning, greatly enhancing generalization and accuracy. Kimi v1.5 (cite61†Team et al., 2025 ) and ReFT (cite62†Luong et al., 2024 ) employ traditional Proximal Policy Optimization (PPO) (cite63†Schulman et al., 2017 ) for RFT and have demonstrated excellent performance. DeepSeek-R1 (cite53†DeepSeek-AI et al., 2025 ) adopts GRPO and uses verifiable reward strategies to compute policy gradients directly.
L88: DAPO (cite64†Yu et al., 2025 ) further optimizes GRPO to improve training stability.
L89: #### Experience Replay.
L90: Recently, a small portion of work has also explored experience replay. For example, TreePOcite65†Li et al. (2025) organizes sequences into tree structures, accelerating the rollout phase and achieving some performance improvement. SegmentPO cite66†Guo et al. (2025) leverages subtree information to provide process supervision for each node. BREAD cite67†Zhang et al. (2025) combines the SFT and RFT stages and attempts to incorporate prefixes of correct answers when reasoning fails.
L91: However, these approaches focus on tree construction, resulting in relatively complex algorithms, and the acceleration in reasoning is not particularly significant. RPO focuses on improving the accuracy of gradient estimation through a minimal revision of the reward function, and combines this with experience caching to achieve simultaneous improvements in training speed and performance.
L92: cite68†Image: Refer to caption Figure 2: Overview of the RPO framework. The entire training process is described as follows: Cached answer fragments are used by the model to generate new responses; either the best or a random response is selected based on the reward system for optimization; and the cache is continuously updated to improve training efficiency and stability.
L93: ## 3 Method
L94: 
L95: The overall framework of our method is illustrated in Figure  cite69†2 and consists of three main components. The first component involves cache initialization. In the second component, subsequent responses are rolled out based on the initialized cache and subsequently optimized. The third component updates the cache pool using an $\epsilon$-greedy strategy.
L96: ### 3.1 Cache Pool Initialization
L97: 
L98: First, we denote the dataset of samples as $\mathcal{D}=\{q_{k}\}_{k=1}^{N}$, where $q_{k}$ represents the $k$-th question in the dataset. We denote the initial model parameters as $\theta_{0}$, and we represent the model’s answering policy by $\pi_{\theta_{0}}$. Before training begins, we initialize the cache pool as $\mathcal{C}^{(0)}$ as follows:
L99:  | $$\mathcal{C}^{(0)}=\left\{\left(q_{k},a_{k}\right)\mid a_{k}\sim\pi_{\theta_{0}}(\cdot|q_{k}),\forall q_{k}\in\mathcal{D}\right\}.$$  |  | (1)
L100: 
L101: This stage uses the initial model policy to sample the dataset $\mathcal{D}$. To retrieve the response $a_{k}$ corresponding to question $q_{k}$ from the cache pool, we define the retrieval operation as:
L102: 
L103:  | $$a_{k}\coloneqq\{a\mid(q_{k},a)\in\mathcal{C}\}.$$  |  | (2)
L104: Here, $a_{k}$ denotes the answer associated with question $q_{k}$ in the cache pool $\mathcal{C}$.
L105: ### 3.2 Rollout And Optimization
L106: 
L107: Rollout. At each rollout stage, we use the RPO strategy to retrieve the historical response $a_{k}$ for each question $q_{k}$ from the cache pool $\mathcal{C}$. We then remove the last $m$ tokens and concatenate the remaining prefix with $q_{k}$ to construct the input instruction, thereby generating a new response $o$. We express this process as:
L108: 
L109:  | $$o=a_{k}^{[0:-m]}\|\pi_{\theta}\big(\cdot\,|\,q_{k},a_{k}^{[0:-m]}\big),$$  |  | (3)
L110: where $a_{k}\!\coloneqq\!\{a\!\mid\!(q_{k},a)\!\in\!\mathcal{C}\},m\!\sim\!\mathcal{U}\{0,\!1,...,\!L\}.$,$L$ is the maximum truncation length, $\mathcal{U}\{0,1,...,L\}$ samples a truncation point uniformly from $[0,L]$, $a_{k}^{[0:-m]}$ truncates the last $m$ tokens of $a_{k}$, and $\pi_{\theta}(\cdot|q_{k},a_{k}^{[0:-m]})$ generates a new continuation based on the question and prefix.
L111: In this paper, $L$ is either fixed or set dynamically based on the shortest response in a sampling group $G$, denoted as $\ell$, where:
L112:  | $$\ell=\min\{\mathrm{len}(o_{1}),\mathrm{len}(o_{2}),\dots,\mathrm{len}(o_{G})\}.$$  |  | (4)
L113: 
L114: Replay-based Policy Optimization. After completing the sampling generation, RPO adopts Group Relative estimation of advantage. For a given question-answer pair $(q_{k},a_{k})$, the behavioral policy $\pi_{\theta_{t-1}}$ samples a group of $G$ individual responses $\{o_{i}\}_{i=1}^{G}$ from the model. Then, by normalizing the group rewards $\{R_{i}\}_{i=1}^{G}$, the advantage of each response is computed as:
L115:  |  | $\displaystyle\mathcal{J}_{\mathrm{RPO}}(\theta_{t})=\mathbb{E}_{(q,a)\sim\mathcal{C}^{(t-1)},\,o_{1:G}\sim\pi_{\theta_{t}}}$  |
L116:  |  | $\displaystyle\left[\!\frac{1}{G}\sum_{i=1}^{G}\!\frac{1}{|o_{i}|}\!\sum_{j=1}^{|o_{i}|}\!\ell_{i,j}(\theta_{t})\!\right]\!-\!\beta\,\!D_{\mathrm{KL}}\!\left(\pi_{\theta_{t}}\,\!\|\,\!\pi_{\mathrm{ref}}\right),$  |  | (5)
L117: 
L118: where the token-level RPO loss is defined as:
L119:  | $$\begin{split}\ell_{i,j}(\theta_{t})=\min\Big(&r_{i,j}(\theta_{t})\hat{A}_{i,j},\\
L120: &\mathrm{clip}\big(r_{i,j}(\theta_{t}),1\pm\epsilon\big)\hat{A}_{i,j}\Big).\end{split}$$  |  | (6)
L121: 
L122: The probability ratio and the normalized advantage are given by
L123: 
L124:  | $$\!\!r_{i,j}(\!\theta_{t}\!)\!=\!\frac{\pi_{\theta_{t}}(o_{i,j}\!\mid\!q,o_{i,<j})}{\pi_{\theta_{t-1}}(o_{i,j}\!\mid\!q,o_{i,<j})},\hat{A}_{i,j}\!=\!\frac{R_{i}\!-\!\mu_{R}}{\sigma_{R}},$$  |  | (7)
L125: where $\mu_{R}$ and $\sigma_{R}$ denote the mean and standard deviation of $\{R_{i}\}_{i=1}^{G}$, respectively.
L126: 
L127: Since RPO is policy-agnostic, we propose a unified forward reinforcement learning paradigm based on experience replay. We can then write the policy gradient function of RPO in a more general form as:
L128:  |  | $\displaystyle\nabla_{\theta}\mathcal{J}_{\mathrm{RPO}}(\theta)=\underbrace{\mathbb{E}_{(q,o)\sim\mathcal{C}}}_{\text{Data Source}}$  |
L129:  |  | $\displaystyle\Bigg(\!\!\frac{1}{|o|}\!\!\sum_{j=1}^{|o|}\!\underbrace{\mathcal{G}(q,o,j,\pi_{ref})}_{\text{Gradient Coefficient}}\!\nabla_{\theta}\!\log\pi_{\theta}(o_{j}|q,o_{<j})\!\!\Bigg)$  |  | (8)
L130: Equation cite70†8 is derived from the standard policy gradient formulation. The above equations indicate that only the sampling stage is affected by RPO, while the policy gradient function remains unaltered. As a result, RPO exhibits a plug-and-play nature and can be easily integrated into other reinforcement fine-tuning algorithms.
L131: Compared with traditional full-path reasoning optimization, RPO introduces previously sampled historical response trajectories as constraints during subsequent sampling. In this way, the policy space $\pi_{\theta}$ explored during training is restricted. This constraint regularizes the gradient descent space during learning, which can be expressed as:
L132: 
L133:  | $$\!\!Var(\|\nabla_{\theta}\mathcal{J}_{\mathrm{RPO}}\|_{2})\leq Var(\|\nabla_{\theta}\mathcal{J}_{\mathrm{ALL}}\|_{2}).$$  |  | (9)
L134: where,$\nabla_{\theta}\mathcal{J}_{\mathrm{ALL}}$ represents the gradient of the full-path reasoning optimization. Theoretically, our method enables a more stable training process. Detailed mathematical proofs are provided in Appendix cite29†A .
L135: ### 3.3 Cache Update
L136: 
L137: After each gradient update, we adopt the $\varepsilon$-greedy algorithm to update the experience cache by selecting the highest-reward response from the current inference results. Specifically, when the random variable $u\sim\mathcal{U}(0,1)$ satisfies $u\leq\varepsilon$, we select the response with the highest group reward; otherwise, we randomly select a suboptimal response. We formalize the update process as:
L138:  | $$\mathcal{C}^{(t)}=\bigl(\mathcal{C}^{(t-1)}\cup\{(q_{k},o)\}\bigr)\setminus\{(q_{k},a_{k})\},$$  |  | (10)
L139: 
L140: where $o=o_{\text{argmax}\{R_{i}\}_{i=1}^{G}}$ if $u\leq\varepsilon$, and $o=o_{g^{\prime}}$ otherwise. Here, $o_{\text{argmax}\{R_{i}\}_{i=1}^{G}}$ denotes the highest-reward response in the group, and $o_{g^{\prime}}$ is another randomly selected candidate response.
L141: ### 3.4 Length-Aware Reward Shaping
L142: 
L143: However, since the same response prefix is shared during the sampling phase, the diversity of responses within the group is reduced compared to the full-path reasoning optimization algorithm. This lower diversity results in more similar reward signals, thereby diminishing the effectiveness of policy gradient estimation. To ensure meaningful gradients, reasonable reward differences should be maintained within the group, even when all responses are correct.
L144: A Length-Aware Reward Shaping method is proposed to address this issue. This method is based on the assumption: For the same question, a reasoning path that reaches the correct answer more concisely should be rewarded with a higher value. Specifically, for each response $o_{i}$ in the group, its length-aware reward $R(s_{i})$ is computed as:
L145: 
L146:  | $$\!\!\!R(s_{i})\!=\!\text{clip}\!\left(\!\frac{r(s_{i})}{1\!+\!e^{-\alpha(\ell_{\text{ref}}-\text{len}(o_{i}))}},m,\mathcal{M}\!\right),$$  |  | (11)
L147: where, $r(s_{i})$ is the original reward, $\ell_{\text{ref}}$ is the average length of group $G$, defined as $\ell_{\text{ref}}=\frac{1}{|G|}\sum_{i=1}^{|G|}\text{len}(o_{i})$. The parameter $\alpha>0$ controls the sensitivity of the reward to length differences. $m$ and $\mathcal{M}$ are the lower and upper bounds for reward clipping to avoid extremely large or small values. $\text{clip}(\cdot,m,\mathcal{M})$ denotes restricting a value within the interval $[m,\mathcal{M}]$.
L148: We then iterate the above steps in Sections cite12†3.2 and  cite13†3.3 until a predefined stopping step $T$ is reached.
L149: Through mathematical derivation, we demonstrate that length-aware rewards are better suited for the RPO algorithm; the two can complement each other, and when the guiding path is within a certain threshold, they can enable the model to achieve greater performance gains. In contrast, traditional GRPO or DAPO algorithms, which use the full reasoning path, lack an initial fixed guiding path.
L150: This results in high variance for length-aware rewards, making it difficult to accurately estimate the true effective policy gradient, and thus they are not suitable for using length-aware rewards. Detailed proofs are provided in Appendix cite35†B .
L151: ## 4 Experiments
L152: 
L153: ### 4.1 Experimental Setup
L154: #### Base Models.
L155: To demonstrate the effectiveness and generality of RPO, we evaluate it on two open-source inference models with 1.5B and 7B parameters, namely Deepseek-r1-qwen-distill-1.5b and Deepseek-r1-qwen-distill-7b (cite53†DeepSeek-AI et al., 2025 ; cite71†Bai et al., 2023 ).
L156: Notably, we skip the supervised fine-tuning (SFT) phase, which is usually a prerequisite for reinforcement learning to enhance performance (cite72†Chu et al., 2025 ), as the selected models have already undergone this stage (cite53†DeepSeek-AI et al., 2025 ).
L157: #### Datasets.
L158: 
L159: We evaluate the models on six standard reasoning evaluation datasets: aime25(cite73†math-ai, 2025 ), aime24(cite74†math-ai, 2024 ), math500(cite75†Hendrycks et al., 2021 ), amc23(cite76†math-ai, 2023 ), minerva(cite77†Lewkowycz et al., 2022 ) and olympicbench(cite78†He et al., 2024 ). To ensure fairness, all evaluations use the lighteval(cite79†Habib et al., 2023 ) toolkit.
L160: #### Implementation Details.
L161: During training, we use 7k samples from the open-rs dataset (cite80†Dang and Ngo, 2025 ) with a global batch size of 576 for 4 epochs. Experiments are run on a single H20 machine with 8×H20 96G GPUs. We generate 6 samples per prompt, set the temperature to 0.7, and fix the maximum generation length at 4096. For the length-aware reward, we use $m=0.5$, $M=1$, and $\alpha=0.01$. All models are fully fine-tuned.
L162: Due to time constraints, only zero-shot performance is averaged over three runs; all other ablation experiments are run once.
L163: ### 4.2 Zero-shot performance
L164: We set the maximum truncation length $L$ for each group to half of the minimum response length $\ell$. Then, we train the DeepSeek-R1-Qwen-1.5B and DeepSeek-R1-Qwen-7B models for four epochs using the original GRPO algorithm, the DAPO algorithm, as well as their RPO variants, with a batch size of 576 and a maximum generation length of 4096 tokens.
L165: To ensure that the experimental results are not caused by randomness, we repeat the training three times for each experiment, then compare their mean accuracy on the designated evaluation datasets.
L166: Table 1: Performance of the RPO algorithm on test datasets. w/ R means length-aware reward is used, w/o R means length-aware reward is not used. +RPO shows the effect of applying the RPO algorithm on top of each method.
L167: Model  | AIME25  | AIME24  | MATH500  | AMC23  | Minerva  | OlyB  | Avg
L168: 1.5B Models
L169: DeepSeek-R1-Qwen-1.5B  | 16.7  | 28.8  | 82.2  | 62.9  | 26.5  | 43.3  | 43.4
L170:   + GRPO (w/o R)  | 24.4  | 31.1  | 85.7  | 72.5  | 29.8  | 51.3  | 49.1
L171:    +RPO  | 24.4 0  | 25.6 -5.5  | 84.3 -1.4  | 69.2 -3.3  | 29.5 -0.3  | 51.7 +0.4  | 47.5 -1.6
L172:   + GRPO (w/ R)  | 22.2  | 32.2  | 83.8  | 70.8  | 27.5  | 50.5  | 47.8
L173:    +RPO  | 24.4 +2.2  | 35.6 +3.4  | 85.3 +1.5  | 83.3 +12.5  | 29.8 +2.3  | 51.8 +1.3  | 51.7 +3.9
L174:   + DAPO (w/o R)  | 30.0  | 24.4  | 86.2  | 84.2  | 29.7  | 52.7  | 51.2
L175:    +RPO  | 28.9 -1.1  | 24.4 0  | 86.0 -0.2  | 84.5 +0.3  | 29.3 -0.4  | 52.1 -0.6  | 50.9 -0.3
L176:   + DAPO (w/ R)  | 26.7  | 30.0  | 85.0  | 84.1  | 29.7  | 51.1  | 50.2
L177:    +RPO  | 32.2 +5.5  | 30.0 0  | 86.2 +1.2  | 86.1 +2  | 29.1 -0.6  | 52.3 +1.2  | 52.7 +2.5
L178: 7B Models
L179: DeepSeek-R1-Qwen-7B  | 43.3  | 55.5  | 92.8  | 90.0  | 44.5  | 67.4  | 65.6
L180:   + GRPO (w/o R)  | 43.3  | 53.3  | 95.0  | 90.0  | 44.5  | 67.2  | 65.6
L181:    +RPO  | 43.3 0  | 46.6 -6.7  | 92.5 -2.5  | 89.2 -0.8  | 42.3 -2.2  | 67.7 +0.5  | 63.6 -2
L182:   + GRPO (w/ R)  | 40.0  | 48.9  | 95.0  | 88.3  | 43.5  | 66.0  | 63.6
L183:    +RPO  | 50.0 +10  | 61.1 +12.2  | 94.2 -0.8  | 90.8 +2.5  | 43.7 +0.2  | 67.3 +1.3  | 67.8 +4.2
L184:   + DAPO (w/o R)  | 43.3  | 53.3  | 94.6  | 90.2  | 45.1  | 67.7  | 65.7
L185:    +RPO  | 46.7 +3.4  | 52.2 -1.1  | 94.2 -0.4  | 91.2 +1  | 42.7 -2.4  | 64.9 -2.8  | 65.3 -0.4
L186:   + DAPO (w/ R)  | 42.2  | 56.7  | 93.2  | 91.8  | 44.6  | 64.5  | 65.5


## jan29_systemfour_route

RPO:Reinforcement Fine-Tuning with Partial Reasoning Optimization (https://arxiv.org/html/2601.19404v1)
citeturn28515view3 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19404v1","pattern":"4.3 Training"}); Total lines: 605
L31:     3. cite21†4.3 Training Time Overhead L32:     4. cite22†4.4 Stability Analysis L33:   6. cite23†5 More Analysis L34:     1. cite24†Impact of Maximum Truncation Length and $\alpha$. L35:     2. cite25†Effect of max_length on Exploration Capability. L36:     3. cite26†Impact of Cache Pool Update Strategy on Model’s Pass@N Performance. L37:   7. cite27†6 Conclusion L38:   8. cite28†References L39:   9. cite29†A Proof of RPO Gradient Stability L40:     1. cite30†Policy gradient estimation. L41:     2. cite31†Gradient of the optimization policy. L188: As shown in Table cite81†1 , as mentioned in the Method section, length-aware rewards complement the RPO algorithm. Incorporating group-wise length-aware rewards enables RPO to achieve higher accuracy on test benchmarks than GRPO and DAPO for both the 1.5B and 7B model sizes. Without group-wise length-aware rewards, RPO may experience some performance degradation; therefore, when using RPO for accelerated training, it is recommended to include group-wise length-aware rewards to enhance performance.
L189: ### 4.3 Training Time Overhead
L190: To investigate the training time overhead of GRPO and RPO, each experiment is conducted on a machine with 8 H20 GPUs, using only a single GPU for sampling during the training phase. It should be noted that RPO introduces additional inference overhead during the cache initialization phase, where parallel inference is performed across all GPUs using the vllm framework. When the dataset size is 7k and the parallel batch size is 256, this phase takes approximately 20 minutes.
L191: Our experiments reveal that the primary factors affecting the relative training speed between RPO and GRPO are the number of group samples $G$ and the maximum truncation length $L$, while the impact of batch size is relatively minor.
L192: Table 2: The average number of tokens generated per sample with the RPO method.
L193: $L$  | 1.5B Model  | 7B Model
L194: 300  | 145.88  | 147.06
L195: 500  | 158.41  | 168.17
L196: 800  | 382.20  | 397.89
L197: GRPO  | 2689.51  | 2457.91
L198: Table 3: Training time of RPO and GRPO under 4 epochs with $L=800$, h represents hours.
L199: Method  | 1.5B Model  | 7B Model
L200: --- | --- | ---
L201: GRPO  | 77.28 h  | 84.53 h
L202: +RPO  | 8.37 h  | 23.50 h
L203: We study training speed for both 1.5B and 7B models. With maximum truncation length fixed at $L=300$, we set per-GPU batch sizes 2 (1.5B) and 1 (7B), and evaluate group sizes $G=6,8,16$. As shown in Figure cite82†3 , smaller $G$ yields greater acceleration for RPO, reducing training time to 7.4% of GRPO for 1.5B and 21.1% for 7B. We also study the effect of $L$ with $G=6$.
L204: The actual training speed is affected by many factors, so we propose a fairer comparison: using the average tokens generated per sample. Since prefill is much faster than decoding, more tokens in prefill lead to shorter decoding time. As shown in Table  cite83†2 , under the original GRPO algorithm, each sample requires an average of 2689.51 tokens and 2457.91 tokens for the 1.5B and 7B models, respectively.


## jan29_systemfour_core

RPO:Reinforcement Fine-Tuning with Partial Reasoning Optimization (https://arxiv.org/html/2601.19404v1)
citeturn28516view3 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19404v1","lineno":209}); Total lines: 605
L191: Our experiments reveal that the primary factors affecting the relative training speed between RPO and GRPO are the number of group samples $G$ and the maximum truncation length $L$, while the impact of batch size is relatively minor.
L192: Table 2: The average number of tokens generated per sample with the RPO method.
L193: $L$  | 1.5B Model  | 7B Model
L194: 300  | 145.88  | 147.06
L195: 500  | 158.41  | 168.17
L196: 800  | 382.20  | 397.89
L197: GRPO  | 2689.51  | 2457.91
L198: Table 3: Training time of RPO and GRPO under 4 epochs with $L=800$, h represents hours.
L199: Method  | 1.5B Model  | 7B Model
L200: --- | --- | ---
L201: GRPO  | 77.28 h  | 84.53 h
L202: +RPO  | 8.37 h  | 23.50 h
L203: We study training speed for both 1.5B and 7B models. With maximum truncation length fixed at $L=300$, we set per-GPU batch sizes 2 (1.5B) and 1 (7B), and evaluate group sizes $G=6,8,16$. As shown in Figure cite82†3 , smaller $G$ yields greater acceleration for RPO, reducing training time to 7.4% of GRPO for 1.5B and 21.1% for 7B. We also study the effect of $L$ with $G=6$.
L204: The actual training speed is affected by many factors, so we propose a fairer comparison: using the average tokens generated per sample. Since prefill is much faster than decoding, more tokens in prefill lead to shorter decoding time. As shown in Table  cite83†2 , under the original GRPO algorithm, each sample requires an average of 2689.51 tokens and 2457.91 tokens for the 1.5B and 7B models, respectively.
L205: cite84†Image: Refer to caption Figure 3: The impact of maximum truncation length $L$ and group size $G$ on the acceleration ratio of POER under the 1.5B and 7B model settings. Table 4: Performance of GRPO and RPO on Evaluation Datasets in Multi-Step Iteration Scenarios.
L206: Model  | AIME25  | AIME24  | MATH500  | AMC23  | Minerva  | OlyB  | Avg
L207: --- | --- | --- | --- | --- | --- | --- | ---
L208: DeepSeek-R1-Qwen-7B  | 43.3  | 55.5  | 92.8  | 90.0  | 44.5  | 67.4  | 65.6
L209: + GRPO(w/o R)  | 40.0  | 50.0  | 94.2  | 90.0  | 41.2  | 66.7  | 63.7
L210:    + RPO  | 46.6 +6.6  | 56.7 +6.7  | 92.8 -1.4  | 90.0 0  | 41.4 +0.2  | 66.1 -0.6  | 65.6 +1.9
L211: DeepSeek-R1-Qwen-1.5B  | 16.7  | 28.8  | 82.2  | 62.9  | 26.5  | 43.3  | 43.4
L212: + GRPO(w/o R)  | 10.0  | 10.0  | 67.0  | 45.0  | 20.6  | 31.4  | 34.8
L213:    + RPO  | 20.0 +10  | 36.7 +26.7  | 82.8 +15.8  | 72.5 +27.5  | 29.4 +8.8  | 51.5 +20.1  | 48.8 +14
L214: cite85†Image: Refer to caption Figure 4: Response length of RPO and GRPO with full-trajectory optimization on 1.5B model across training steps.
L215: 
L216: cite86†Image: Refer to caption Figure 5: Response length of RPO and GRPO with full-trajectory optimization on 7B model across training steps.
L217: In contrast, with the RPO algorithm, the number can be reduced to as low as 145.88 tokens and 147.06 tokens. From the perspective of the decode stage, the time overhead of RPO is only about 5% of that of GRPO. Table cite87†3 presents the detailed training time overhead of the original GRPO and RPO algorithms over 4 epochs.
L218: It is worth noting that the average number of tokens generated by the GRPO algorithm for the 1.5B model is higher than that for the 7B model. However, when constrained by RPO, the number of tokens generated is lower. This is because the RPO algorithm preserves shorter correct answers, and the exploration capability of the 1.5B model, once guided, is weaker compared to that of the 7B model, leading to this phenomenon.
L219: ### 4.4 Stability Analysis
L220: Conventional reinforcement learning methods, such as GRPO and PPO, are prone to instability in multi-step training, with performance and response length often deteriorating as iterations increase. Accordingly, GRPO fine-tuning typically limits iteration numbers, using accuracy and response length to measure model degradation(cite53†DeepSeek-AI et al., 2025 ). RPO addresses this by using a cache pool mechanism, and we conduct comparative experiments to quantify its improved training stability over GRPO.
L221: During the training process, we use a batch size of 18 to train the 7B and 1.5B models for four epochs, and monitor changes in response length and model performance, as shown in Figure cite88†5 and cite88†5 . In this multi-step iterative training setup, GRPO experiences a collapse in response length around the 200th iteration, while RPO maintains stable response lengths throughout the process.
L222: On the other hand, as shown in Table cite89†4 , the model performance after training with GRPO deteriorated, especially for the 1.5B model, where accuracy dropped by 8.6%. In contrast, RPO results in a 5.4% improvement in accuracy.
L223: Beyond the instability from reward sparsity, GRPO suffers from strong locality due to its inter-group comparison strategy, limiting performance improvements. RPO mitigates this by introducing an experience cache, using an external cached policy $\pi_{\mathcal{C}}$ to approximate the main policy $\pi_{\theta}$ during updates. This provides a global context, enhances training stability, and allows RPO to maintain consistent performance over long iterations.
L224: ## 5 More Analysis
L225: #### Impact of Maximum Truncation Length and $\alpha$.
L226: 
L227: Intuitively, the maximum truncation length $L$ and $\alpha$ are not independent factors. To study their effect on training, we train the model with combinations of $L=300,0.5\ell,\ell$ and $\alpha=0,0.01,0.1,1$. Notably, when $\alpha=0$, the intra-group length-aware reward is disabled, so all correct reasoning paths receive the same reward.
L228: The DeepSeek-R1-Qwen-1.5B model is trained for two epochs with a batch size of 336 to amplify differences in training outcomes for easier observation. The evaluation results are shown in Figure cite90†6 : under a fixed $L$, performance first improves as $\alpha$ increases and then declines.
L229: 
L230: cite91†Image: Refer to caption Figure 6: Heatmap of the Impact of $L$ and $\alpha$ on Model Accuracy.
L231: #### Effect of max_length on Exploration Capability.
L232: To investigate the impact of max_length settings on the model’s initial exploration ability, we set the maximum truncate length of RPO to 300 and examined the performance of the 1.5B and 7B models on the AIME24 dataset under two settings: max_length = 2048 and max_length = 4096. As shown in Figure cite92†7 , RPO demonstrates lower exploration ability compared to GRPO, and the gap between the two methods gradually widens as max_length increases.

