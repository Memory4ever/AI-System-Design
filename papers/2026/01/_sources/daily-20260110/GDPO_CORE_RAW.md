GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (https://arxiv.org/html/2601.05242v1)
citeturn26778view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.05242v1","lineno":null}); Total lines: 510
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 GRPO’s propensity for reward signal collapse in multi-reward RL L18:   4. cite8†3 Method L19:     1. cite9†3.1 Group reward-Decoupled normalization Policy Optimization L20:     2. cite10†3.2 Effective incorporation of priority variation L21:   5. cite11†4 Experiments L22:     1. cite12†4.1 Tool calling L23:       1. cite13†4.1.1 Does removing the standard deviation normalization term in GRPO provide any benefit? L24:     2. cite14†4.2 Mathematical reasoning L25:       1. cite15†4.2.1 Impact analysis of different reward priority variation configurations L26:     3. cite16†4.3 Coding reasoning L27:   6. cite17†5 Related Work L28:     1. cite18†GRPO Variants L29:     2. cite19†Multi-Reward Reinforcement Learning L30:   7. cite20†6 Conclusion L31:   8. cite21†References L32:   9. cite22†A Training stability issue of GDPO without batch-wise advantage normalization L33:   10. cite23†B ToolRL Training Prompt Format L34:   11. cite24†C Tool Calling Reward Functions L35:     1. cite25†Format Reward. L36:     2. cite26†Correctness Reward. L37:   12. cite27†D ToolRL Hyperparameters Setting L38:   13. cite28†E Math/Coding Reasoning Hyperparameters Setting L39:   14. cite29†F Training curves of GRPO and GDPO when training DeepSeek-R1-7B and Qwen3-4B-Instruct with $\mathcal{R}_{\text{length}}$ and $\mathcal{R}_{\text{correct}}$ on math reasoning data. L40:   15. cite30†G Comparison of GRPO/GDPO finetuned DeepSeek-R1-7B models under varying length reward weights $\{1.0,0.75,0.5,0.25\}$ with and without the conditioned length reward $\tilde{\mathcal{R}}_{\text{length}}$ on math reasoning tasks L41: cite31†License: CC BY 4.0†info.arxiv.org L42: 
L43: arXiv:2601.05242v1 [cs.CL] 08 Jan 2026
L44: # GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization
L45: 
L46: Shih-Yang Liu¹    Xin Dong^{*}    Ximing Lu    Shizhe Diao    Peter Belcak    Mingjie Liu    Min-Hung Chen    Hongxu Yin    Yu-Chiang Frank Wang    Kwang-Ting Cheng¹    Yejin Choi    Jan Kautz    Pavlo Molchanov Affiliation: Affiliation: NVIDIA Affiliation: Corresponding author: X
L47: ###### Abstract
L48: As language models become increasingly capable, users expect them to provide not only accurate responses but also behaviors aligned with diverse human preferences across a variety of scenarios. To achieve this, Reinforcement learning (RL) pipelines have begun incorporating multiple rewards, each capturing a distinct preference, to guide models toward these desired behaviors.
L49: However, recent work has defaulted to apply Group Relative Policy Optimization (GRPO) under multi-reward setting without examining its suitability. In this paper, we demonstrate that directly applying GRPO to normalize distinct rollout reward combinations causes them to collapse into identical advantage values, reducing the resolution of the training signal and resulting in suboptimal convergence and, in some cases, early training failure.
L50: We then introduce G roup reward-D ecoupled Normalization P olicy O ptimization (GDPO), a new policy optimization method to resolve these issues by decoupling the normalization of individual rewards, more faithfully preserving their relative differences and enabling more accurate multi-reward optimization, along with substantially improved training stability.
L51: We compare GDPO with GRPO across three tasks: tool calling, math reasoning, and coding reasoning, evaluating both correctness metrics (accuracy, bug ratio) and constraint adherence metrics (format, length). Across all settings, GDPO consistently outperforms GRPO, demonstrating its effectiveness and generalizability for multi-reward reinforcement learning optimization.
L52: Implementations: cite32†HF-TRL†github.com , cite33†verl†github.com , cite34†Nemo-RL†github.com | Links: cite35†Project†nvlabs.github.io , cite36†Lab†nv-dler.github.io L53: 
L54: cite37†Image: Refer to caption (a) An overview of our proposed GDPO
L55: 
L56: (b) Reward trends: GDPO vs. GRPO
L57: Figure 1: (a): An overview of GDPO, which performs group-wise normalization per reward and then applies batch-wise advantage normalization to preserve a stable numerical range independent of reward count and improve update stability. (b): Median and IQR reward curves over five runs of Qwen2.5-Instruct-1.5B tool-calling RL, demonstrating that GDPO consistently converges to higher correctness and format reward score than GRPO.
L58: ## 1 Introduction
L59: As language models continue to advance in capability, expectations for their behavior have grown accordingly. Demand for models to not only provide accurate responses but also exhibit behaviors aligned with a wide range of human preferences across diverse scenarios has continued to increase. These preferences span efficiency [cite38†1 , cite39†2 , cite40†3 ], safety [cite41†4 ], response coherence and logic [cite42†5 , cite43†6 ], gender biases [cite44†7 ] and many other objectives.
L60: Meeting such heterogeneous requirements within a single model is a challenging task.
L61: Reinforcement learning (RL) has emerged as the de facto training pipeline for aligning large language models to fulfill such diverse human preferences. In particular, recent RL-based approaches have begun to incorporate multiple rewards into training, with each reward designed to capture different human preferences and collectively guide models toward human-favored behaviors.
L62: Despite this growing interest in multi-reward RL, recent work [cite38†1 , cite40†3 , cite42†5 ] has largely focused on the reward design itself and often directly relied on applying Group Relative Policy Optimization (GRPO) directly for multi-reward RL optimization, often without examining whether GRPO is well-suited for optimizing combinations of heterogeneous rewards.
L63: In this paper, we revisit the applicability of GRPO in multi-reward settings and show that directly applying GRPO to normalize different combinations of rollout rewards can cause them to collapse into identical advantage values, which effectively limits the precision of the training signal, as illustrated in Fig. cite45†2 . This collapse removes important distinctions across reward dimensions and leads to inaccurate policy updates, suboptimal reward convergence, and, in many cases, early training failure.
L64: To overcome these challenges, we propose Group reward-Decoupled Normalization Policy Optimization (GDPO) which decouples the group-wise normalization of each individual reward as illustrated in Fig. cite46†1(a) , to ensure that distinctions across different reward combinations are better preserved and more accurately reflect the relative differences in model responses. This leads to more precise multi-reward optimization and substantially improved training convergence.
L65: After this decoupled group-wise normalization, we apply batch-wise advantage normalization to ensure that the magnitude of advantage does not increase as the number of individual rewards increases.
L66: We compare GDPO and GRPO across three tasks: tool calling, math reasoning, and code reasoning. These tasks cover a wide range of objectives, including tool-calling accuracy and format correctness, mathematical reasoning accuracy and adherence to reasoning-length constraints, and code pass rate and bug ratio. Across all tasks, GDPO converges better. For example, in Fig.
L67: cite47†1(b) , training Qwen2.5-1.5B-Instruct with GDPO attains both higher correctness and format compliance than GRPO on the tool-calling task. On challenging math tasks, GDPO consistently outperforms GRPO. For instance, training DeepSeek-R1-1.5B and Qwen3-4B-Instruct with GDPO yields up to 6.3% and 2.3% higher accuracy on AIME compared to GRPO, while keeping more responses short simultaneously.
L68: Taken together, these results demonstrate the effectiveness and generalizability of GDPO, showing it to be a better alternative to GRPO for multi-reward RL optimization.
L69: 
L70: Our contributions are as follows:
L71: 
L72:   * •
L73: 
L74: Analysis of GRPO reward collapse. We demonstrate that applying GRPO naively for multi-reward RL optimization can collapse distinct rollout reward combinations into identical advantage values, thereby diminishing the resolution of the learning signal.
L75: 
L76:   * •
L77: Remediation of GRPO reward collapse. We propose GDPO, which performs group-wise decoupled normalization of each reward separately to better preserve cross-reward distinctions and enable more accurate multi-reward optimization.
L78: 
L79:   * •
L80: 
L81: In addition to GDPO, we provide a systematic overview of how to modify reward functions and adjust reward weights to more faithfully align with preferences of varying priority.
L82: 
L83:   * •
L84: We carry out extensive experiments on three tasks: tool calling, math reasoning, and code reasoning, and compare the effectiveness of GDPO on optimizing a wide range of rewards corresponding to accuracy, format correctness, length constraints, and code quality. In all settings, GDPO consistently outperforms GRPO, showing improved training convergence and stronger downstream performance that align more closely with a diverse set of preferences.
L85: ## 2 GRPO’s propensity for reward signal collapse in multi-reward RL
L86: 
L87: Recent advancements such as Group Relative Policy Optimization (GRPO) [cite48†8 ] and its variants, including DAPO [cite49†9 ] and Reinforce++-Baseline [cite50†10 ], have emerged as widely adopted reinforcement learning algorithms due to their efficiency and simplicity. In contrast to Proximal Policy Optimization (PPO) [cite51†11 ], GRPO eliminates the need for a value model by leveraging group-relative advantage estimation for policy updates.
L88: Currently, GRPO has been primarily employed for optimizing a single-objective reward, typically focusing on accuracy. However, as model capability continues to grow, recent works have increasingly sought to optimize multiple rewards, such as response length constraint and formatting quality, in addition to accuracy [cite38†1 , cite52†12 , cite40†3 ], to better align with human preferences.
L89: Existing approaches for multi-reward RL generally adopt a straightforward strategy: summing all reward components and applying GRPO directly.
L90: Formally, for a given question–answer pair $(q_{i},o_{j})$, where the behavior policy $\pi_{\theta_{\mathrm{old}}}$ samples a group of $G$ responses $\{o_{j}\}_{j=1}^{G}$, and assuming $n$ objectives, the aggregated reward for the $j$-th response is computed as the sum of each objective’s reward:
L91: 
L92:  | $$r^{(i,j)}_{\text{sum}}=r_{1}^{(i,j)}+\cdots+r_{n}^{(i,j)}$$  |  | (1)
L93: 
L94: The group-relative advantage for the $j$-th response is then obtained by normalizing the group-level aggregated rewards:
L95:  | $$A^{(i,j)}_{\text{sum}}=\frac{r_{\text{sum}}^{(i,j)}-\mathrm{mean}\{r_{\text{sum}}^{(i,1)},\ldots,r_{\text{sum}}^{(i,G)}\}}{\mathrm{std}\{r_{\text{sum}}^{(i,1)},\ldots,r_{\text{sum}}^{(i,G)}\}}$$  |  | (2)
L96: 
L97: The corresponding multi-reward GRPO optimization objective can then be expressed as:
L98:  | $$\mathcal{J}_{\mathrm{GRPO}}(\theta)=\mathbb{E}_{(q_{i},o_{j})\sim D,\;\{o_{j}\}_{j=1}^{G}\sim\pi_{\theta_{\mathrm{old}}}(\cdot|q)}\left[\frac{1}{G}\sum_{j=1}^{G}\frac{1}{|o_{j}|}\sum_{t=1}^{|o_{j}|}\min\left(s_{i,t}(\theta)\,A^{(i,j)}_{\text{sum}},\;\mathrm{clip}(s_{i,t}(\theta),1-\epsilon,1+\epsilon)\,A^{(i,j)}_{\text{sum}}\right)\right]$$  |  | (3)
L99: where $s_{t}(\theta)=\frac{\pi_{\theta}(o_{j}^{t}\,|\,q,o_{j}^{<t})}{\pi_{\theta_{\mathrm{old}}}(o_{j}^{t}\,|\,q,o_{j}^{<t})}$ and $\epsilon$ denotes the clipping threshold. For clarity, we omit the KL-divergence loss term in this formulation.
L100: cite53†Image: Refer to caption Figure 2: Comparison of GRPO and GDPO advantage computation in a two-binary-reward, two-rollout example. GRPO maps different reward combinations into only two distinct advantage groups, whereas GDPO normalizes each reward independently and retains three distinct groups of advantage values. We skip the batch-wise normalization calculation step in GDPO here for simplicity since it does not change the number of distinct advantage groups.
L101: Figure 3: Comparison of the number of distinct advantage groups produced by GRPO, GRPO without standard deviation normalization (GRPO w/o std), and GDPO. As the number of rollouts (left) or rewards (right) grows, GDPO consistently preserve a substantially larger number of distinct advantage groups compared to GRPO and GRPO w/o std. This results in advantage estimations that provide more expressive training signals.
L102: We first revisit this common practice of applying GRPO for mulit-reward RL optimization and identify a previously overlooked issue, that is GRPO inherently compresses the reward signal, causing loss of information in the advantage estimates. To illustrate, we start with a simple training setting and then extend it to more general cases.
L103: Consider a scenario where we generate two rollouts for each question for calculating the group-relative advantage and the task involves two binary reward $r_{1},r_{2}\in\{0,1\}$. Consequently, the total reward for each rollout can take values from $\{0,1,2\}$.
L104: As shown in Figure cite45†2 , we enumerate all possible rollout reward combinations within a group, represented as $(\mathtt{rollout}\text{ }\mathtt{1}^{\prime}\mathtt{s}\text{ }\mathtt{total}\text{ }\mathtt{reward},\mathtt{rollout}\text{ }\mathtt{2^{\prime}s}\text{ }\mathtt{total}\text{ }\mathtt{reward})$ and the corresponding normalized advantages as $(\mathit{rollout}\text{ }\mathit{1}^{\prime}\mathit{s}\text{ }\mathit{normalized}\text{ }\mathit{advantage},\mathit{rollout}\text{ }\mathit{2^{\prime}s}\text{ }\mathit{normalized}\text{ }\mathit{advantage})$.
L105: Despite having six distinct combinations when order is ignored, only two unique advantage groups emerge after applying group-wise reward normalization. Specifically, $(\mathtt{0,1})$, $(\mathtt{0,2})$, and $(\mathtt{1,2})$ yield identical normalized advantages $A_{\text{sum}}$ of $(\mathit{-0.7071},\,\mathit{0.7071})$, while $(\mathtt{0,0})$, $(\mathtt{1,1})$, and $(\mathtt{2,2})$ all result in $(\mathit{0,0})$.
L106: This demonstrates a fundamental limitation of GRPO’s advantage calculation in multi-reward optimization which over-compresses the rich group-wise reward signal. Intuitively, $\mathtt{(0,2)}$ should produce a stronger learning signal than $\mathtt{(0,1)}$ because a total reward of $2$ indicates simultaneous satisfaction of two rewards, whereas a reward of $1$ corresponds to achieving only one.
L107: Thus, when the other one rollout only receives zero reward, $\mathtt{(0,2)}$ should yield a larger relative advantage than $\mathtt{(0,1)}$. This limitation can also introduce risks of training instability due to inaccurate advantage estimates. As shown in Fig. cite54†5 , the correctness reward score begins to decline after approximately 400 training steps when training with GRPO, indicating a partial training collapse.
L108: Recently, Dr.GRPO [cite55†13 ] and DeepSeek-v3.2 [cite43†6 ] adopt a variant of GRPO that removes the standard deviation normalization term from Eq. cite56†2 , such that $A^{(i,j)}_{\text{sum}}=r_{\text{sum}}^{(i,j)}-\mathrm{mean}\{r_{\text{sum}}^{(i,1)},\ldots,r_{\text{sum}}^{(i,G)}\}$. Despite these works introduce this modification to mitigate question-level difficulty bias, at first glance, this change also appears to address the issue we identify.
L109: Specifically, removing the standard deviation normalization mitigates the issue: $\mathtt{(0,1)}$ and $\mathtt{(0,2)}$ now yield distinct advantages of $\mathit{(-0.5,0.5)}$ and $\mathit{(-1.0,1.0)}$, respectively. However, when this setup is generalized to a larger number of rollouts while keeping the number of rewards fixed, as shown in Figure cite57†3 , we observe that such fix only slightly increases the number of distinct advantage groups compared to GRPO.
L110: A similar trend can be observed under settings where the number of rollouts is fixed at four, but the number of rewards gradually increases. In this case, we also observe only modest improvements in the number of distinct advantage groups. We also empirically examine the effectiveness of removing the standard deviation normalization term in Section cite13†4.1.1 , and find that this modification does not lead to improved convergence or better downstream evaluation performance.
L111: ## 3 Method
L112: ### 3.1 Group reward-Decoupled normalization Policy Optimization
L113: To overcome these challenges, we propose Group reward-Decoupled normalization Policy Optimization (GDPO), a method designed to better maintain distinctions among different reward combinations and more accurately capture their relative differences in the final advantages. In contrast to GRPO, which applies group-wise normalization directly to the aggregated reward sum, GDPO decouples this process by performing group-wise normalization of each reward separately before aggregation.
L114: Concretely, rather than summing all $n$ rewards first (as in Eq. cite58†1 ) and then applying group-wise normalization to obtain $A_{\text{sum}}$ (Eq. cite56†2 ), GDPO computes the normalized advantage for each reward for the $j^{\text{th}}$ rollout of the $i^{\text{th}}$ question as:
L115:  | $$A^{(i,j)}_{1}=\frac{r_{1}^{(i,j)}-\mathrm{mean}\{r_{1}^{(i,1)},\ldots,r_{1}^{(i,G)}\}}{\mathrm{std}\{r_{1}^{(i,1)},\ldots,r_{1}^{(i,G)}\}},\quad\ldots,\quad A^{(i,j)}_{n}=\frac{r_{n}^{(i,j)}-\mathrm{mean}\{r_{n}^{(i,1)},\ldots,r_{n}^{(i,G)}\}}{\mathrm{std}\{r_{n}^{(i,1)},\ldots,r_{n}^{(i,G)}\}}$$  |  | (4)
L116: 
L117: The overall advantage used for policy updates is then obtained by first summing the normalized advantages across all objectives:
L118:  | $$\displaystyle A_{\text{sum}}^{(i,j)}=A_{1}^{(i,j)}+\cdots+A_{n}^{(i,j)}$$  |  | (5)
L119:  | $$\displaystyle\hat{A}^{(i,j)}_{\text{sum}}=\frac{A^{(i,j)}_{\text{sum}}-\mathrm{mean}\!\left\{A^{(i^{\prime},j^{\prime})}_{\text{sum}}\mid i^{\prime}\in D_{\text{Batch}},\;j^{\prime}=1,\ldots,G\right\}}{\mathrm{std}\!\left\{A^{(i^{\prime},j^{\prime})}_{\text{sum}}\mid i^{\prime}\in D_{\text{Batch}},\;j^{\prime}=1,\ldots,G\right\}+\epsilon}$$  |  | (6)
L120: then applying batch-wise advantages normalization to the sum of the multi-reward advantages, which ensures that the numerical scale of the final advantage $\hat{A}^{(i,j)}_{\text{sum}}$ remains stable and does not grow as additional rewards are introduced. Empirically, we also find that this normalization step improves training stability, as shown in Appendix cite22†A , where removing batch-wise normalization occasionally leads to convergence failures.
L121: By separating the normalization of each reward, GDPO alleviates the information-loss problem present in GRPO’s advantage estimation, as illustrated in Fig. cite45†2 . Note that since the batch-wise normalization step in GDPO does not alter the number of distinct advantage groups, we omit it here for clarity. From the figure, we can see that when adopting GRPO, distinct reward combinations, such as $(0,2)$ and $(0,1)$, lead to identical normalized advantages, masking the subtle distinctions between them.
L122: In contrast, GDPO retains these fine-grained differences by assigning distinct advantage values to each combination, for example, the reward combination of $\mathtt{(0,1)}$ after GDPO normalization becomes $\mathit{(-0.7071,0.7071)}$ and $\mathtt{(0,2)}$ becomes $\mathit{(-1.4142,1.4142)}$, which more appropriately reflects that $\mathtt{(0,2)}$ should yield a stronger learning signal than $\mathtt{(0,1)}$.
L123: Similarly, when extending the number of rollouts to three, GRPO would assign advantage values of $\mathit{(0,0,0)}$ to $\mathtt{(1,1,1)}$. However, $\mathtt{(1,1,1)}$ may arise from heterogeneous reward partitions such as $r_{1}=\mathtt{(1,1,0)}$ or $r_{2}=\mathtt{(0,0,1)}$, for which GDPO would yield non-zero advantages, thereby preserving meaningful differences across reward dimension.
L124: We further quantify the effectiveness of GDPO by comparing the number of distinct advantage groups across GDPO, GRPO, and GRPO w/o std under two experimental settings as shown in Fig. cite57†3 . In the two-reward scenario with a varying number of rollouts, GDPO consistently produces a significantly higher count of distinct advantage groups, with the gap widening as the number of rollouts increases.
L125: On the other hand, when fixing the number of rollouts to four and increasing the number of rewards, a similar pattern emerges, where GDPO exhibits progressively larger advantage granularity as the objective count grows. This demonstrate that the proposed decoupled normalization approach effectively increases the number of distinct advantage groups across all the RL settings and enables more precise advantage estimation.
L126: In addition to these theoretical improvements, we observe that using GDPO consistently yields a more stable training curve and improved convergence. For instance, GDPO achieves better convergence on both the format reward and the correctness reward in the tool-calling task, as shown in Fig. cite59†4 . GDPO also eliminates the training collapse issue observed with GRPO in the math reasoning task, as shown in Fig.
L127: cite54†5 , where the model trained with GDPO continues to improve the correctness reward score throughout training. Additional empirical results in Section cite11†4 further confirm GDPO’s ability to achieve stronger alignment with the target preferences across a wide range of downstream tasks.
L128: ### 3.2 Effective incorporation of priority variation
L129: Up to this point, we have assumed that all objectives carry equal importance. In practice, this assumption does not always hold in real-world applications. In this section, we provide a systematic overview of how to adjust the weights of rewards associated with different objectives or modify the reward functions to enforce prioritization of more important objectives. We also discuss how these two design choices behave differently when the underlying rewards vary significantly in difficulty.
L130: It is common practice to assign different weights to each reward to encode different priorities among objectives, such that $r_{\text{sum}}=w_{1}r_{1}+\dots+w_{n}r_{n}$, thereby controlling the contribution of each reward to the final advantage used for policy updates, and for GDPO, such weightings are apply to the normalized advantages of each reward as:
L131: 
L132:  | $$A_{\text{sum}}^{(i,j)}=w_{1}A_{1}^{(i,j)}+\cdots+w_{n}A_{n}^{(i,j)}$$  |  | (7)
L133: However, we found that adjusting reward weights does not always yield the intended behavior when the difficulty levels of the underlying objectives differ substantially. If one objective is much easier than the others, the model often focuses on maximizing the reward for that objective regardless of the assigned weights.
L134: As a result, to more effectively force the model to allocate more attention to rewards associated with more challenging objectives, the weight differences must be made sufficiently large to compensate for the disparity in difficulty. Nevertheless, even with such adjustments, the model may still prefer optimizing the easier reward rather than the objective the user intends to prioritize, a phenomenon that we empirically demonstrate in Sec. cite15†4.2.1 .
L135: Therefore, some recent works [cite38†1 , cite60†14 ] address such reward hacking by conditioning easier rewards on more difficult rewards. Specifically, Given two rewards $r_{k}$ and $r_{l}$, conditioning $r_{k}$ on $r_{l}$ can be formulated as:
L136: 
L137:  | $$r_{k}=\begin{cases}r_{k},&\text{if }r_{l}\geq t\\
L138: 0,&\text{otherwise.}\end{cases}$$  |  | (8)
L139: With such reward function design, the model can only receive reward of $r_{k}$ when the reward $r_{l}$ satisfies a predefined score threshold $t$, and as a consequence, the model get force to always maximize the human-prioritized reward first and completely alleviate the above mentioned problem. The empirical effectiveness of this strategy is shown in Sec.
L140: cite15†4.2.1 , where models trained with conditioned reward functions achieve higher performance on prioritized objectives compared to those trained without conditioning but only with larger weight assigned to the prioritized rewards. We also observe that, after resolving the issue of the easier reward dominating, assigning different reward weights for fine-grained priority adjustment can also be more faithfully reflected in the final model behavior.
L141: ## 4 Experiments
L142: We begin by evaluating the effectiveness of GDPO compared with GRPO on the tool-calling task (Sec. cite12†4.1 ), which involves optimizing two rewards: tool-calling correctness and format compliance. We then present an ablation study that examines the training convergence and downstream performance of GRPO with and without standard deviation normalization. Next, we compare GDPO and GRPO on a math reasoning task that optimizes two implicitly competing rewards, accuracy and length constraint (Sec. cite14†4.2 ).
L143: We further conduct extensive analyses of the impact of incorporating different reward weights and modifying reward functions to better reflect varying priorities in human preferences, especially when rewards differ substantially in difficulty. Finally, we extend the number of optimized rewards to three and compare GRPO and GDPO on coding reasoning (Sec.
L144: cite16†4.3 ), jointly optimizing code-generation accuracy, adherence to length constraints, and bug ratio, further demonstrating that GDPO generalizes effectively to settings with three reward objectives.
L145: ### 4.1 Tool calling
L146: 
L147: Figure 4: Median and IQR reward curves across five runs of Qwen2.5-1.5B on the tool-calling task for GDPO, GRPO, and GRPO w/o std. GDPO consistently converges to higher correctness and format rewards, while GRPO w/o std matches correctness gains but fails to converge on the format reward.
L148: We compare GDPO with GRPO on the tool calling task following the setup of ToolRL [cite52†12 ]^{1}^{1} 1 https://github.com/qiancheng0/ToolRL.
L149: Specifically, the model is trained to learn how to incorporate external tools into the reasoning trajectory to solve a user task following the output format shown in Appendix cite23†B , where the reasoning steps must be enclosed in <think></think>, the tool calls must appear within <tool_call></tool_call>, and the model’s final answer must be placed inside <response></response>.
L150: We adopt the same training set as ToolRL for RL training, which consists of 2k samples from ToolACE [cite61†15 ], 1k samples from Hammar [cite62†16 ], and 1k samples from xLAM [cite63†17 ]. Each training instance contains a question and its corresponding ground-truth tool calls. The training involves two rewards:
L151:   * •
L152: 
L153: Format reward: The format reward $\mathcal{R}_{\text{format}}\in\{0,1\}$ checks whether the model output satisfies the required structure and contains all necessary fields in the correct order.
L154: 
L155:   * •
L156: 
L157: Correctness reward: The correctness reward $\mathcal{R}_{\text{correct}}\in[-3,\,3]$ evaluates the model-generated tool calls against the ground-truth calls using three metrics: tool name matching, parameter name matching, and parameter content matching.
L158: A full description of the reward formulation is provided in Appendix cite24†C . We train Qwen-2.5-Instruct (1.5B and 3B) [cite64†18 ] with GRPO and GDPO using verl [cite65†19 ] for 100 steps, following the original hyperparameter settings from ToolRL’s GRPO recipe. We use four rollouts per training question, a batch size of 512, and a maximum response length of 1024. The complete hyperparameter configuration is listed in Appendix cite27†D .
L159: We evaluate the trained models on the Berkeley Function Call Leaderboard (BFCL-v3) [cite66†20 ], a comprehensive benchmark covering a broad range of challenges, including single-step reasoning, multi-step tool use, real-time execution, irrelevant tool rejection, simultaneous multi-tool selection, and multi-tool execution. We finetune the models with GRPO and GDPO across five runs and report the average accuracy and average format correctness on BFCL-v3 in Table cite67†1 .
L160: We additionally plot the median training curves with interquartile ranges for both methods over the five runs in Fig. cite59†4 .
L161: From the training curves, we observe that GDPO consistently converges to higher values on both the format and correctness reward score across all runs. Although GDPO exhibits larger variance in the number of steps required to converge on format reward, it ultimately attains better format compliance than both GRPO.
L162: For the correctness reward, GDPO shows faster early-stage improvement and reaches a higher reward score than the GRPO baselines toward later stages, demonstrating the effectiveness of GDPO on providing more accurate advantage estimation that leads to better optimization.
L163: Table 1: Comparison of GDPO and GRPO-trained Qwen2.5-Instruct-1.5B/3B models on tool-calling accuracy and format correctness. The reported results are the averages across five runs.
L164:  | Live Ocerall Acc ↑  | Multi Turn Overall Acc ↑  | Non-Live Overall Acc ↑  | Avg Acc ↑  | Correct Format ↑
L165: --- | --- | --- | --- | --- | ---
L166: Qwen2.5-Instruct-1.5B  | 37.89%  | 0.12%  | 15.63%  | 17.88%  | 4.74%
L167: --- | --- | --- | --- | --- | ---
L168: GRPO  | 50.63%  | 2.04%  | 37.87%  | 30.18%  | 76.33%
--------------------------------------------------------------------------------
LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision–Language–Action Model (https://arxiv.org/html/2601.05248v1)
citeturn26778view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.05248v1","lineno":null}); Total lines: 372
--------------------------------------------------------------------------------
CounterVid: Counterfactual Video Generation forMitigating Action and Temporal Hallucinations in Video-Language Models (https://arxiv.org/html/2601.04778v1)
citeturn26778view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04778v1","lineno":null}); Total lines: 348
--------------------------------------------------------------------------------
Next-generation Constitutional Classifiers \ Anthropic (https://www.anthropic.com/research/next-generation-constitutional-classifiers)
citeturn26778view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://www.anthropic.com/research/next-generation-constitutional-classifiers","lineno":null}); Total lines: 69
--------------------------------------------------------------------------------
OpenAI and SoftBank Group partner with SB Energy | OpenAI (https://openai.com/index/stargate-sb-energy-partnership)
citeturn26778view4 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://openai.com/index/stargate-sb-energy-partnership","lineno":null}); Redirected to URL: https://openai.com/index/stargate-sb-energy-partnership/; Total lines: 134


GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (https://arxiv.org/html/2601.05242v1)
citeturn26808view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.05242v1","lineno":168}); Total lines: 510
L125: On the other hand, when fixing the number of rollouts to four and increasing the number of rewards, a similar pattern emerges, where GDPO exhibits progressively larger advantage granularity as the objective count grows. This demonstrate that the proposed decoupled normalization approach effectively increases the number of distinct advantage groups across all the RL settings and enables more precise advantage estimation.
L126: In addition to these theoretical improvements, we observe that using GDPO consistently yields a more stable training curve and improved convergence. For instance, GDPO achieves better convergence on both the format reward and the correctness reward in the tool-calling task, as shown in Fig. cite59†4 . GDPO also eliminates the training collapse issue observed with GRPO in the math reasoning task, as shown in Fig.
L127: cite54†5 , where the model trained with GDPO continues to improve the correctness reward score throughout training. Additional empirical results in Section cite11†4 further confirm GDPO’s ability to achieve stronger alignment with the target preferences across a wide range of downstream tasks.
L128: ### 3.2 Effective incorporation of priority variation
L129: Up to this point, we have assumed that all objectives carry equal importance. In practice, this assumption does not always hold in real-world applications. In this section, we provide a systematic overview of how to adjust the weights of rewards associated with different objectives or modify the reward functions to enforce prioritization of more important objectives. We also discuss how these two design choices behave differently when the underlying rewards vary significantly in difficulty.
L130: It is common practice to assign different weights to each reward to encode different priorities among objectives, such that $r_{\text{sum}}=w_{1}r_{1}+\dots+w_{n}r_{n}$, thereby controlling the contribution of each reward to the final advantage used for policy updates, and for GDPO, such weightings are apply to the normalized advantages of each reward as:
L131: 
L132:  | $$A_{\text{sum}}^{(i,j)}=w_{1}A_{1}^{(i,j)}+\cdots+w_{n}A_{n}^{(i,j)}$$  |  | (7)
L133: However, we found that adjusting reward weights does not always yield the intended behavior when the difficulty levels of the underlying objectives differ substantially. If one objective is much easier than the others, the model often focuses on maximizing the reward for that objective regardless of the assigned weights.
L134: As a result, to more effectively force the model to allocate more attention to rewards associated with more challenging objectives, the weight differences must be made sufficiently large to compensate for the disparity in difficulty. Nevertheless, even with such adjustments, the model may still prefer optimizing the easier reward rather than the objective the user intends to prioritize, a phenomenon that we empirically demonstrate in Sec. cite15†4.2.1 .
L135: Therefore, some recent works [cite38†1 , cite60†14 ] address such reward hacking by conditioning easier rewards on more difficult rewards. Specifically, Given two rewards $r_{k}$ and $r_{l}$, conditioning $r_{k}$ on $r_{l}$ can be formulated as:
L136: 
L137:  | $$r_{k}=\begin{cases}r_{k},&\text{if }r_{l}\geq t\\
L138: 0,&\text{otherwise.}\end{cases}$$  |  | (8)
L139: With such reward function design, the model can only receive reward of $r_{k}$ when the reward $r_{l}$ satisfies a predefined score threshold $t$, and as a consequence, the model get force to always maximize the human-prioritized reward first and completely alleviate the above mentioned problem. The empirical effectiveness of this strategy is shown in Sec.
L140: cite15†4.2.1 , where models trained with conditioned reward functions achieve higher performance on prioritized objectives compared to those trained without conditioning but only with larger weight assigned to the prioritized rewards. We also observe that, after resolving the issue of the easier reward dominating, assigning different reward weights for fine-grained priority adjustment can also be more faithfully reflected in the final model behavior.
L141: ## 4 Experiments
L142: We begin by evaluating the effectiveness of GDPO compared with GRPO on the tool-calling task (Sec. cite12†4.1 ), which involves optimizing two rewards: tool-calling correctness and format compliance. We then present an ablation study that examines the training convergence and downstream performance of GRPO with and without standard deviation normalization. Next, we compare GDPO and GRPO on a math reasoning task that optimizes two implicitly competing rewards, accuracy and length constraint (Sec. cite14†4.2 ).
L143: We further conduct extensive analyses of the impact of incorporating different reward weights and modifying reward functions to better reflect varying priorities in human preferences, especially when rewards differ substantially in difficulty. Finally, we extend the number of optimized rewards to three and compare GRPO and GDPO on coding reasoning (Sec.
L144: cite16†4.3 ), jointly optimizing code-generation accuracy, adherence to length constraints, and bug ratio, further demonstrating that GDPO generalizes effectively to settings with three reward objectives.
L145: ### 4.1 Tool calling
L146: 
L147: Figure 4: Median and IQR reward curves across five runs of Qwen2.5-1.5B on the tool-calling task for GDPO, GRPO, and GRPO w/o std. GDPO consistently converges to higher correctness and format rewards, while GRPO w/o std matches correctness gains but fails to converge on the format reward.
L148: We compare GDPO with GRPO on the tool calling task following the setup of ToolRL [cite52†12 ]^{1}^{1} 1 https://github.com/qiancheng0/ToolRL.
L149: Specifically, the model is trained to learn how to incorporate external tools into the reasoning trajectory to solve a user task following the output format shown in Appendix cite23†B , where the reasoning steps must be enclosed in <think></think>, the tool calls must appear within <tool_call></tool_call>, and the model’s final answer must be placed inside <response></response>.
L150: We adopt the same training set as ToolRL for RL training, which consists of 2k samples from ToolACE [cite61†15 ], 1k samples from Hammar [cite62†16 ], and 1k samples from xLAM [cite63†17 ]. Each training instance contains a question and its corresponding ground-truth tool calls. The training involves two rewards:
L151:   * •
L152: 
L153: Format reward: The format reward $\mathcal{R}_{\text{format}}\in\{0,1\}$ checks whether the model output satisfies the required structure and contains all necessary fields in the correct order.
L154: 
L155:   * •
L156: 
L157: Correctness reward: The correctness reward $\mathcal{R}_{\text{correct}}\in[-3,\,3]$ evaluates the model-generated tool calls against the ground-truth calls using three metrics: tool name matching, parameter name matching, and parameter content matching.
L158: A full description of the reward formulation is provided in Appendix cite24†C . We train Qwen-2.5-Instruct (1.5B and 3B) [cite64†18 ] with GRPO and GDPO using verl [cite65†19 ] for 100 steps, following the original hyperparameter settings from ToolRL’s GRPO recipe. We use four rollouts per training question, a batch size of 512, and a maximum response length of 1024. The complete hyperparameter configuration is listed in Appendix cite27†D .
L159: We evaluate the trained models on the Berkeley Function Call Leaderboard (BFCL-v3) [cite66†20 ], a comprehensive benchmark covering a broad range of challenges, including single-step reasoning, multi-step tool use, real-time execution, irrelevant tool rejection, simultaneous multi-tool selection, and multi-tool execution. We finetune the models with GRPO and GDPO across five runs and report the average accuracy and average format correctness on BFCL-v3 in Table cite67†1 .
L160: We additionally plot the median training curves with interquartile ranges for both methods over the five runs in Fig. cite59†4 .
L161: From the training curves, we observe that GDPO consistently converges to higher values on both the format and correctness reward score across all runs. Although GDPO exhibits larger variance in the number of steps required to converge on format reward, it ultimately attains better format compliance than both GRPO.
L162: For the correctness reward, GDPO shows faster early-stage improvement and reaches a higher reward score than the GRPO baselines toward later stages, demonstrating the effectiveness of GDPO on providing more accurate advantage estimation that leads to better optimization.
L163: Table 1: Comparison of GDPO and GRPO-trained Qwen2.5-Instruct-1.5B/3B models on tool-calling accuracy and format correctness. The reported results are the averages across five runs.
L164:  | Live Ocerall Acc ↑  | Multi Turn Overall Acc ↑  | Non-Live Overall Acc ↑  | Avg Acc ↑  | Correct Format ↑
L165: --- | --- | --- | --- | --- | ---
L166: Qwen2.5-Instruct-1.5B  | 37.89%  | 0.12%  | 15.63%  | 17.88%  | 4.74%
L167: --- | --- | --- | --- | --- | ---
L168: GRPO  | 50.63%  | 2.04%  | 37.87%  | 30.18%  | 76.33%
L169: GDPO  | 55.36%  | 2.50%  | 40.58%  | 32.81%  | 80.66%
L170: Qwen2.5-Instruct-3B  | 63.57%  | 1.38%  | 30.75%  | 31.90%  | 58.37%
L171: GRPO  | 69.23%  | 3.14%  | 45.24%  | 39.20%  | 81.64%
L172: GDPO  | 71.22%  | 4.59%  | 46.79%  | 40.87%  | 82.23%
L173: In the BFCL-v3 evaluation shown in Table cite67†1 , GDPO also consistently improves the average tool calling accuracy and format correctness over the GRPO-trained counterparts. For training Qwen2.5-Instruct-1.5B, GDPO achieves almost 5% and 3% improvement on Live/non-Live tasks and gains roughly 2.7% improvement on the overall average accuracy and more than 4% in correct format ratio compared with GRPO.
L174: Similar improvements are observed for the 3B model, where GDPO continues to outperform GRPO across all the sub-tasks, achieving up to 2% accuracy improvement and delivers a better format compliance ratio.
L175: #### 4.1.1 Does removing the standard deviation normalization term in GRPO provide any benefit?
L176: 
L177: Table 2: Comparison of GRPO, GRPO w/o std, and GDPO-trained Qwen2.5-Instruct-1.5B/3B models on tool-calling accuracy and format correctness.The reported results are the average across five runs.
L178:  | Live Ocerall Acc ↑  | Multi Turn Overall Acc ↑  | Non-Live Overall Acc ↑  | Avg Acc ↑  | Correct Format ↑
L179: --- | --- | --- | --- | --- | ---
L180: Qwen2.5-1.5B-Instruct  | 37.89%  | 0.12%  | 15.63%  | 17.88%  | 4.74%
L181: --- | --- | --- | --- | --- | ---
L182: GRPO  | 50.63%  | 2.04%  | 37.87%  | 30.18%  | 76.33%
L183: GRPO w/o std  | 47.19%  | 1.47%  | 39.11%  | 29.26%  | 0%
L184: GDPO  | 55.36%  | 2.50%  | 40.58%  | 32.81%  | 80.66%
L185: Recall from Fig. cite57†3 that removing the standard deviation normalization term in GRPO (denoted GRPO w/o std) slightly increases the number of distinct advantage groups. In this section, we empirically examine the effectiveness of this modification. Following the previous experiments, we run GRPO w/o std five times and report the average accuracy and average format correctness ratio on BFCL-v3.
L186: In the reward training curves shown in Fig. cite47†1(b) , we observe that although GRPO w/o std converges to a correctness reward that is similar to GDPO and higher than standard GRPO, it fails to improve the format reward entirely. This failure results in a correct format ratio of 0% on BFCL-v3 (see Table. cite68†2 ), indicating that the model does not learn the required output structure.
L187: These also show that simply removing the standard deviation normalization term in order to increase advantage diversity can introduce instability into training, which may ultimately prevent successful convergence in multi-reward reinforcement learning.
L188: ### 4.2 Mathematical reasoning
L189: We consider a mathematical reasoning task that optimizes two implicitly competing rewards: accuracy and adherence to a length constraint. The goal is to improve model performance on challenging mathematical problems while keeping the generated output within a predefined response length to encourage efficient problem solving.
L190: We train DeepSeek-R1-1.5B, DeepSeek-R1-7B [cite48†8 ], and Qwen3-4B-Instruct [cite69†21 ] using GRPO and GDPO on the DeepScaleR-Preview dataset [cite70†22 ] for 500 steps, which contains 40k competition-level math problems. Training is performed using verl [cite65†19 ], and we follow the original DeepSeek-R1 prompt format [cite48†8 ].
L191: Following the DLER setup [cite60†14 ], we incorporate dynamic sampling, higher clipping thresholds, and the token-mean loss from DAPO [cite49†9 ], and use 16 rollouts, a batch size of 512, and a maximum response length of 8000 tokens. The full set of hyperparameters is provided in Appendix cite28†E .
L192: The training uses two rewards:
L193: 
L194:   * •
L195: 
L196: Length reward: The length reward $\mathcal{R}_{\text{length}}\in\{0,1\}$ checks whether the model’s output remains within the target length $l$, which is set to 4000 tokens for all remaining experiments:
L197: 
L198:  | $$\mathcal{R}_{\text{length}}=\begin{cases}1,&\text{if response length}\leq l\\
L199: 0,&\text{otherwise}.\end{cases}$$  |
L200: 
L201:   * •
L202: Correctness reward: The correctness reward $\mathcal{R}_{\text{correct}}\in\{0,1\}$ indicates whether the final answer extracted from the model’s response matches the ground truth.
L203: We compare the GRPO and GDPO-trained model on AIME-24 [cite71†23 ], AMC (AMC 2022 and AMC 2023) [cite72†24 ], MATH [cite73†25 ], Minerva [cite74†26 ] and Olympiad Bench [cite75†27 ]. All evaluations are conducted using vLLM as the inference backend with a sampling temperature of 0.6, $top_{p}$ = 0.95, and a maximum response length of 32k tokens.
L204: For each evaluation question, we generate 16 samples and report the average pass@1 score and the average length-exceeding ratio, denoted Exceed, which measures the percentage of model responses that exceed the predefined length limit of 4000 tokens.
L205: Figure 5: Training behavior of GRPO and GDPO on DeepSeek-R1-1.5B across correctness reward, length reward, and maximum batch response length. Both methods rapidly maximize the length reward, briefly suppressing correctness, yet GDPO subsequently recovers it and surpasses GRPO. After roughly 400 steps, GRPO’s correctness score declines and its length-constraint violations increase, as reflected by rising maximum response lengths.
L206: In contrast, GDPO continues to improve correctness while steadily improving the control over response length.
L207: From the training curves of GRPO and GDPO on DeepSeek-R1-1.5B as shown in Fig. cite54†5 , we first observe that the model tends to maximize the easier reward regardless of the optimization method. In this case, the length reward is easier to optimize, and both GRPO and GDPO reach a full length score within roughly the first 100 training steps. We also see that this rapid rise in the length reward coincides with an early drop in the correctness reward, which indicates that the two rewards are competing.
L208: During the initial phase of training, the model prioritizes satisfying the length constraint, often at the expense of the more challenging correctness objective. However, from the correctness reward trajectories, we observe that GDPO recovers the correctness reward more effectively than GRPO, achieving higher correctness scores at comparable training steps.
L209: We also see that GRPO training starts to destabilize after 400 steps with the correctness rewards score gradually decreasing while GDPO continue to improve the correctness score. Moreover, although both GDPO and GRPO maintain nearly perfect length scores throughout training, we also record the maximum response length within each training batch to assess how well the models satisfy the length constraint under more extreme cases.
L210: The results show that, despite achieving almost a full length reward, the maximum response length for GRPO begins to increase sharply after roughly 400 training steps, while the maximum response length for GDPO continues to decrease. Similar observation can be seen on the training curves on DeepSeek-R1-7B and Qwen3-4B-Instruct as shown in Fig cite76†9 and Fig cite77†10 in appendix where we can see that GDPO consistently provide better alignment to the length constraint.
L211: This contrast further illustrates the effectiveness of GDPO in multi-reward optimization compared with GRPO.
L212: Table 3: Comparison of GRPO and GDPO-trained DeepSeek-R1-1.5B/7B models on Pass@1 accuracy and the proportion of responses exceeding the length constraint across mathematical reasoning benchmarks.
L213:  |  | DeepSeek-R1-1.5B  | DeepSeek-R1-7B  | Qwen3-4B-Instruct
L214: --- | --- | --- | --- | ---
L215:  |  | -  | GRPO  | GDPO  | -  | GRPO  | GDPO  | -  | GRPO  | GDPO
L216: MATH  | Acc ↑  | 84.3%  | 83.6%  | 86.2%  | 93.6%  | 94.1%  | 93.9%  | 94.6%  | 93.9%  | 93.9%
L217: Exceed ↓  | 35.0%  | 1.5%  | 0.8%  | 26.0%  | 0.5%  | 0.1%  | 11.3%  | 0.8%  | 0.1%
L218: AIME  | Acc ↑  | 29.8%  | 23.1%  | 29.4%  | 55.4%  | 50.2%  | 53.1%  | 63.7%  | 54.6%  | 56.9%
L219: Exceed ↓  | 91.5%  | 10.8%  | 6.5%  | 85.6%  | 2.1%  | 0.2%  | 71.3%  | 2.5%  | 0.1%
L220: AMC  | Acc ↑  | 62.0%  | 64.5%  | 69.0%  | 82.9%  | 83.8%  | 84.0%  | 84.5%  | 85.2%  | 84.3%
L221: Exceed ↓  | 67.5%  | 3.2%  | 2.3%  | 57.2%  | 0.6%  | 0.3%  | 33.9%  | 0.7%  | 0.1%
L222: Minerva  | Acc ↑  | 38.41.%  | 43.5%  | 44.0%  | 49.8%  | 53.2%  | 53.8%  | 50.7%  | 52.4%  | 51.9%
L223: Exceed ↓  | 51.4%  | 1.7%  | 0.3%  | 41.8%  | 0.2%  | 0.1%  | 9.1%  | 0.3%  | 0.1%
L224: Olympiad  | Acc ↑  | 44.1%  | 44.3%  | 46.6%  | 58.2%  | 60.2%  | 59.7%  | 65.7%  | 66.8%  | 67.5%
L225: Exceed ↓  | 70.1%  | 2.6%  | 1.9%  | 60.6%  | 1.1%  | 0.4%  | 41.3%  | 1.6%  | 1.0%
L226: In addition, the benchmark results in Table cite78†3 show that the GDPO-trained models not only achieve substantial improvements in reasoning efficiency over the original models, with up to a 80% reduction in length-exceeding ratios on AIME, but also deliver higher accuracy on the majority of the tasks. Moreover, GDPO generally outperforms GRPO on both the accuracy and length constraint objectives.
L227: For the DeepSeek-R1-1.5B, GDPO outperforms GRPO across all benchmarks, achieving accuracy improvements of 2.6%/6.7%/2.3% on MATH, AIME and Olympiad, respectively, while also reducing the length exceed ratios across all the tasks. A similar trend holds for DeepSeek-R1-7B and Qwen3-4B-Instruct, where GDPO achieves stronger accuracy–efficiency trade-offs.
L228: The gains are particularly notable on the more challenging AIME benchmark, with GDPO improving accuracy by nearly 3% while reducing the length-exceeding rate to 0.2% and 0.1%, compared with 2.1% and 2.5% under GRPO for DeepSeek-R1-7B and Qwen3-4B-Instruct. Together, these results show that GDPO not only improves reasoning accuracy across a range of mathematical tasks but also adheres to the length constraint more effectively, underscoring its advantage in multi-reward optimization.
L229: #### 4.2.1 Impact analysis of different reward priority variation configurations
L230: 
L231: Figure 6: Average accuracy and exceed-length ratios for GRPO/GDPO-trained DeepSeek-R1-7B models under varying length reward weights $\{1.0,0.75,0.5,0.25\}$, with and without the conditioned length reward $\tilde{\mathcal{R}}_{\text{length}}$, on mathematical reasoning tasks.
L232: Until this point, we have assumed that all rewards are treated with equal priority. However, as shown in Fig. cite54†5 , the model often maximizes the easier objective at the cost of the more challenging one, even when both objectives are assigned the same reward weight.
L233: In this section, we investigate whether adjusting reward weights can guide the model to prioritize maximizing the correctness reward over the length reward when such a preference is desired and when the two objectives differ noticeably in difficulty.
L234: We begin by fixing the reward weight for $\mathcal{R}_{\text{correct}}$, denoted $w_{\text{correct}}$, to 1, and varying the reward weight for $\mathcal{R}_{\text{length}}$, denoted $w_{\text{length}}$, over the set $\{0.25,0.5,0.75,1.0\}$. This setup allows us to study whether reducing $w_{\text{length}}$ encourages the model to prioritize maximizing the more challenging correctness reward first.
L235: We carry out this experiment on DeepSeek-R1-7B and plot the average accuracy and average length-exceeding ratio of MATH and AIME in Fig. cite79†6 . Full results for the remaining tasks are provided in Appendix cite30†G .
L236: From the results, we observe that reducing $w_{\text{length}}$ to 0.75 or 0.5 has little impact on the average length-exceeding ratio, which shifts by only 0.4% and 0.2% for GRPO on AIME and by 1.3% and 0.6% for GDPO. In addition, lowering $w_{\text{length}}$ does not necessarily relax the length constraint, as decreasing $w_{\text{length}}$ from 0.75 to 0.5 does not consistently increase the length-exceeding ratio on either AIME or MATH for GRPO or GDPO.
L237: This suggests that simply adjusting reward weights does not reliably induce the intended prioritization when the underlying objectives differ substantially in difficulty. Only when $w_{\text{length}}$ is reduced to 0.25, making it sufficiently small to compensate for the difficulty gap between the objectives, do we observe a clear increase in the length-exceeding ratio on AIME for both GRPO and GDPO and on MATH for GDPO.
L238: Figure 7: Training curves of GRPO and GDPO with the conditioned length reward $\tilde{\mathcal{R}}_{\text{length}}$ on DeepSeek-R1-7B across correctness reward, length reward.
L239: We next investigate whether conditioning the easier length reward on the more challenging correctness reward can help mitigate the disparity in difficulty between the two objectives and help improve priority alignment. Following the formulation in Sec. cite10†3.2 , we replace the original length reward $\mathcal{R}_{\text{length}}$ with a conditioned length reward defined as:
L240:  | $$\mathcal{\tilde{R}}_{\text{length}}=\begin{cases}1,&\text{if response length}\leq l{\color[rgb]{1,0,0}\text{ and }\mathcal{R}_{\text{correct}}=1}\\
L241: 0,&\text{otherwise}.\end{cases}$$  |
L242: 
L243: Under this formulation, the model receives the length reward only when the generated response is also correct.
L244: Table 4: Comparison of GRPO and GDPO DeepSeek-R1-7B models, with and without the conditioned length reward $\tilde{\mathcal{R}}_{\text{length}}$, on Pass@1 accuracy and the ratio of outputs exceeding the length constraint across mathematical reasoning benchmarks.
L245:  |  | DeepSeek-R1-7B
L246: --- | --- | ---
L247:  |  | -  | $\mathcal{R}_{\text{length}}$  | $\tilde{\mathcal{R}}_{\text{length}}$
L248: --- | --- | --- | --- | ---
L249:  |  | -  | GRPO  | GDPO  | GRPO  | GDPO
L250: MATH  | Acc ↑  | 93.6%  | 94.1%  | 93.9%  | 93.2%  | 93.9%
L251: Exceed ↓  | 26.0%  | 0.5%  | 0.1%  | 2.7%  | 1.4%
L252: AIME  | Acc ↑  | 55.4%  | 50.2%  | 53.1%  | 53.3%  | 57.7%
L253: Exceed ↓  | 85.6%  | 2.1%  | 0.2%  | 29.2%  | 12.3%
L254: AMC  | Acc ↑  | 82.9%  | 83.8%  | 84.0%  | 82.9%  | 85.9%
L255: Exceed ↓  | 57.2%  | 0.6%  | 0.3%  | 8.6%  | 3.8%
L256: Minerva  | Acc ↑  | 49.8%  | 53.2%  | 53.8%  | 53.2%  | 53.4%
L257: Exceed ↓  | 41.8%  | 0.2%  | 0.1%  | 2.5%  | 1.0%
L258: Olympiad  | Acc ↑  | 58.2%  | 60.2%  | 59.7%  | 59.1%  | 60.8%
L259: Exceed ↓  | 60.6%  | 1.1%  | 0.4%  | 10.3%  | 6.2%
L260: First, we observe that adopting the modified reward function $\tilde{\mathcal{R}}_{\text{length}}$ prevents the model from aggressively maximizing the length reward at the start of training. This reward design also helps avoid large drops in correctness reward score as the model tries to satisfy the length constraint. We can see that the average correctness reward decreases only slightly early in training and then gradually recovers from Fig. cite80†7 .
L261: From Table cite81†4 , we also observe that using $\tilde{\mathcal{R}}_{\text{length}}$ leads to a larger increase in the average length-exceeding ratio for both GRPO and GDPO compared with merely adjusting the weight $w_{\text{length}}$ of $\mathcal{R}_{\text{length}}$, indicating a more effective relaxation of the length constraint. However, GRPO fails to convert this relaxed constraint into meaningful accuracy improvements.
L262: In contrast, GDPO prioritizes the correctness reward more effectively and achieves more consistent accuracy improvement over training without $\tilde{\mathcal{R}}_{\text{length}}$, while introducing substantially smaller increases in length violations.
L263: For instance, using $\tilde{\mathcal{R}}{\text{length}}$ with GDPO yields a 4.4% accuracy improvement on AIME with a 16.9% reduction in length-exceeding ratio, and a 3% accuracy gain on AMC with a 4.8% reduction in length violations compared with using GRPO with the same reward.
L264: We next examine whether, after mitigating the difficulty disparity through conditioned length reward, varying the reward weight on $\tilde{\mathcal{R}}_{\text{length}}$, denoted $\tilde{w}_{\text{length}}$, leads to more faithful reflection of fine-grained preference adjustments. We fix the correctness reward weight and vary $\tilde{w}_{\text{length}}\in\{0.25,0.5,0.75,1.0\}$. As shown in Fig. cite79†6 , the models trained with conditioned reward behave more predictably.
L265: For example, reducing $\tilde{w}_{\text{length}}$ from 1.0 to 0.25 steadily increases the length-exceeding ratio for both GRPO and GDPO on MATH and AIME, in contrast to the unstable results observed when adjusting the weight of the original $\mathcal{R}_{\text{length}}$.
L266: Finally, across all settings, including different reward formulations and different reward weights, GDPO consistently provides a better accuracy and efficiency trade-off than GRPO.
L267: ### 4.3 Coding reasoning
L268: Table 5: Comparison of GRPO and GDPO trained DeepSeek-R1-7B models on coding pass rate, length-exceeding rate, and bug ratio across coding reasoning benchmarks.
L269: Here, $\mathcal{R}_{\text{pass}}+\tilde{\mathcal{R}}_{\text{length}}$ refers to optimizing $\mathcal{R}_{\text{pass}}$ and $\tilde{\mathcal{R}}_{\text{length}}$, and $\mathcal{R}_{\text{pass}}+\tilde{\mathcal{R}}_{\text{length}}+\mathcal{R}_{\text{bug}}$ refers to optimizing $\mathcal{R}_{\text{pass}}$, $\tilde{\mathcal{R}}_{\text{length}}$, and $\mathcal{R}_{\text{bug}}$.
L270:  |  | DeepSeek-R1-7B
L271:  |  | -  | $\mathcal{R}_{\text{Pass}}+\mathcal{\tilde{R}}_{\text{length}}$  | $\mathcal{R}_{\text{Pass}}+\mathcal{\tilde{R}}_{\text{length}}+\mathcal{R}_{\text{Bug}}$
L272:  |  | -  | $\text{GRPO}_{\text{2-obj}}$  | $\text{GDPO}_{\text{2-obj}}$  | $\text{GRPO}_{\text{3-obj}}$  | $\text{GDPO}_{\text{3-obj}}$
L273: Apps  | Pass ↑  | 28.1%  | 67.2%  | 68.3%  | 68.1%  | 67.8%
L274: Exceed ↓  | 73.9%  | 5.2%  | 5.0%  | 11.2%  | 8.5%
L275: Bug ↓  | 32.9%  | 25.0%  | 23.5%  | 20.3%  | 18.8%
L276: Codecontests  | Pass ↑  | 47.3%  | 63.2%  | 65.8%  | 65.6%  | 65.6%
L277: Exceed ↓  | 83.0%  | 14.2%  | 14.3%  | 19.3%  | 15.8%
L278: Bug ↓  | 29.7%  | 14.1%  | 13.2%  | 3.9%  | 2.5%
L279: Codeforces  | Pass ↑  | 46.5%  | 68.1%  | 71.2%  | 69.5%  | 69.4%
L280: Exceed ↓  | 82.8%  | 18.1%  | 18.4%  | 16.9%  | 13.6%
L281: Bug ↓  | 27.8%  | 7.0%  | 5.6%  | 2.5%  | 1.8%
L282: Taco  | Pass ↑  | 28.1%  | 45.1%  | 48.4%  | 44.4%  | 45.1%

