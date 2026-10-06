# std1methods

FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning (https://arxiv.org/html/2601.19001v1)
citeturn28140view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19001v1","lineno":102}); Total lines: 468
L76: Yet, these models often generate large amounts of uncritical information—commonly arising from redundant self-verification—that introduce inefficiencies and potential inaccuracies. Numerous methods have been proposed to improve reasoning efficiency. Token-level approaches such as TALE (cite57†Han et al., 2025 ) and R2R (cite58†Fu et al., 2025 ) risk pruning essential reasoning steps, as reasoning paths are naturally sentence-based.
L77: Sentence-level approaches, including DRP (cite59†Jiang et al., 2025b ) and GRPO-S (cite60†Tan & Pan, 2025 ), perform iterative refinement of reasoning paths, but this often comes at the cost of increased computational cost and latency.
L78: cite61†Image: Refer to caption Figure 1: The Example of The GPT-OSS-20B Model.
L79: To address these challenges, we propose FROST, a reasoning method that improves efficiency by pruning uncritical reasoning paths through attention weights. We observe that LRMs typically assign low attention to uncritical steps and higher attention to critical ones, consistent with findings that critical steps exhibit higher sentence entropy (cite60†Tan & Pan, 2025 ).
L80: We therefore introduce the concept of reasoning outliers—uncritical steps with both low attention weights and low entropy (cite62†Wang et al., 2025 ; cite58†Fu et al., 2025 )—and design FROST to eliminate them, yielding shorter and more reliable reasoning paths. Our approach sharpens the attention distribution of LRMs, suppressing low-weight steps while preserving high-weight ones.
L81: Building on prior work (cite63†Luo et al., 2025b ; cite64†Hu et al., 2024 ; cite65†Xiao et al., 2024 ), we adopt $\mathop{\rm{Softmax}}_{1}$ in place of $\mathop{\rm{Softmax}}$, which effectively drives low weights to zero while maintaining large weights. Finally, we propose a training strategy that integrates $\mathop{\rm{Softmax}}_{1}$ with supervised fine-tuning on reasoning tasks, producing efficient reasoning models without sacrificing accuracy.
L82: Contributions. We present FROST (as shown in cite66†fig. 1 ), a reasoning outlier–free LRM designed to enhance reasoning efficiency. Our main contributions are:
L83: 
L84:   * •
L85: 
L86: We introduce the concept of reasoning outliers and propose FROST to prune uncritical reasoning steps characterized by low attention.
L87: 
L88:   * •
L89: 
L90: Theoretically, we analyze $\mathop{\rm{Softmax}}_{1}$ and show its effectiveness in suppressing low attention weights while preserving high ones, thereby enhancing the reasoning capacity of LRMs.
L91: 
L92:   * •
L93: Methodologically, we design a training strategy that combines $\mathop{\rm{Softmax}}_{1}$ with supervised fine-tuning, enabling efficient reasoning without sacrificing accuracy.
L94: 
L95:   * •
L96: Empirically, we demonstrate the effectiveness of FROST across multiple benchmarks, achieving up to a 26.70% accuracy gain while reducing reasoning path length by 69.68% compared with base models. We also measure attention outlier values to verify their impact on efficient reasoning: FROST reduces the maximum infinity norm $\norm{\mathbf{x}}_{\infty}$ by 15.97% and the average kurtosis by 91.09%.
L97: In addition, FROST cuts inference time by at least 28.6% and reduces training time by 42.2% relative to other SFT baselines.
L98: ### 2 Related Work
L99: ##### Reasoning Models.
L100: In recent years, Large Language Models (LLMs) such as DeepSeek-R1 (cite67†Guo et al., 2025 ), OpenAI o1 (cite68†Jaech et al., 2024 ), and Gemini 2.0 Pro (cite69†Team et al., 2023 ) have demonstrated strong reasoning capabilities, particularly on mathematical and logical tasks (cite70†Hao et al., 2024 ). To further improve reasoning performance, numerous methods are proposed, falling into the main paradigms (cite71†Ke et al., ): inference scaling and learning-to-reason.
L101: For inference-time scaling, numerous methods have been proposed, including few-shot prompting (cite72†Brown et al., 2020 ), in-context learning (cite72†Brown et al., 2020 ), Chain-of-Thought (CoT) reasoning (cite73†Wei et al., 2022 ), and Search & Planning (SP) (cite74†Besta et al., 2024 ). Numerous studies focus on improving the LLM reasoning at inference time, with CoT emerging as a key technique. CoT strengthens the model’s reasoning process and generates interpretable reasoning traces.
L102: A simple example involves adding a prompt like “Let’s think step by step” after a question (cite73†Wei et al., 2022 ). Recent research increasingly combines CoT with other inference-time scaling methods, such as ReAct (cite75†Yao et al., 2023 ), Self-Ask (cite76†Press et al., 2023 ) and agentic reasoning (cite77†Pan et al., 2025 ; cite78†Pan et al., 2024 ), to further enhance reasoning capabilities.
L103: For learning-to-reason approaches, many methods aim to build reasoning ability through alignment, including reinforcement learning (RLHF (cite79†Ouyang et al., 2022 ), DPO (cite80†Rafailov et al., 2023 ), GRPO (cite81†Ramesh et al., 2024 )), supervised fine-tuning, and energy-based model (EBM) reasoners (cite82†Jiang et al., 2025a ).
L104: However, LLMs with reasoning capabilities—particularly those with smaller parameter sizes—often generate excessively detailed reasoning chains, including unnecessary tracebacks and redundant alternative paths (cite83†Hou et al., 2025 ; cite84†Chen et al., 2025 ). This overthinking not only increases computational cost during inference but can also negatively impact response quality on accuracy (cite85†Cuadron et al., 2025 ) and safety (cite86†Kumar et al., 2025 ).
L105: To address this, we propose an attention-aware adaptation method that optimizes reasoning paths, yielding efficient reasoning models.
L106: ##### Efficient Reasoning Methods.
L107: To address overthinking, current approaches to optimizing reasoning paths fall into three categories (cite87†Sui et al., 2025 ): prompt-based methods, supervised fine-tuning, and reinforcement learning. Prompt-based methods (cite88†Liu et al., 2025 ; cite89†Xu et al., 2025a ; cite57†Han et al., 2025 ) introduce token-budget constraints to shorten reasoning paths. For instance, TALE (cite57†Han et al., 2025 ) limits the token budget per instance to reduce reasoning length while maintaining task accuracy.
L108: Supervised fine-tuning (SFT) methods (cite90†Ma et al., 2025 ; cite91†Xia et al., 2025a ) improve reasoning conciseness by training models on compressed reasoning paths. For example, DRP (cite59†Jiang et al., 2025b ) fine-tunes models on distilled reasoning data by pruning unrelated reasoning steps. Reinforcement learning (RL) methods (cite92†Li et al., 2025 ; cite93†Yi & Wang, 2025 ; cite83†Hou et al., 2025 ) guide concise reasoning by introducing reward functions that penalize overly long reasoning paths.
L109: For example, cite94†Chia et al. (2024) introduce a reward score based on reference loss and exploration loss from diverse paths, encouraging favorable reasoning branches and penalizing unfavorable ones to improve overall problem-solving performance. However, prompt-based methods rely on handcrafted prompts and often perform unreliably on complex problems. In contrast, SFT and RL approaches require substantial computational resources for fine-tuning, limiting accessibility for users without adequate hardware.
L110: To address these challenges, we propose a new reasoning outlier–removal strategy that eliminates reasoning outliers through attention analysis. Recent studies (cite95†Choi et al., 2025 ; cite96†Cai et al., ) also analyze internal attention patterns in reasoning models, particularly at the sentence level, but their objectives differ substantially from ours and focus on KV-cache–based inference efficiency.
L111: Think Clearly (cite95†Choi et al., 2025 ) examines sentence-level attention spikes near the end-of-thinking token and uses these patterns to prune redundant sentences for faster decoding. In contrast, our Figure 3 analyzes sentence-level contributions to the final-answer token, enabling attribution of which specific reasoning sentences actually affect the model’s prediction, rather than identifying redundancy for pruning.
L112: R-KV (cite96†Cai et al., ) likewise detects redundant attention interactions to compress the KV cache, but does not study how individual reasoning steps functionally influence final-answer formation. Our work therefore provides a finer-grained, component-level attribution analysis of the reasoning trace—going beyond redundancy detection to clarify how different reasoning segments vary in contribution, which constitutes the key novelty relative to these approaches.
L113: ### 3 Reasoning Outlier
L114: 
L115: In this section, we analyze the attention distribution of reasoning traces generated by LRMs. We then examine the impact of different components of the trace on final answer prediction, followed by our definition and characterization of reasoning outliers.
L116: cite97†Image: Refer to caption Figure 2: Attention Heatmap of Reasoning Tokens. We use the Phi-4-Reasoning model (cite98†Abdin et al., 2025 ) to generate a reasoning trace for a sample GSM8K question (cite99†Cobbe et al., 2021 ). The figure shows attention heatmaps from transformer layers 0, 30 and 39, with the first head (top row) and last head (bottom row). Yellow indicates higher attention weights and blue indicates lower ones.
L117: In shallow layers, contributions to the final answer are nearly uniform, while deeper layers and later heads highlight specific tokens with stronger influence.
L118: #### 3.1 Attention Distribution of Reasoning Traces
L119: 
L120: We consider representative LRMs, including DeepSeek-R1(cite67†Guo et al., 2025 ), Phi-4 (cite100†Abdin et al., 2024 ), and GPT-4o (cite56†Hurst et al., 2024 ), which generate text in an autoregressive manner by predicting the next token given the preceding context. To study the attention distribution, we visualize the attention heatmap of each token in the reasoning trace when predicting the final answer.
L121: Let the reasoning process be a sequence of tokens $T=[t_{1},t_{2},\ldots,t_{n}]$, where each $t_{i}$ denotes a token in the process. The attention weight matrix $A$ is defined as:
L122: 
L123:  | $\displaystyle A=[a_{ij}]\quad\text{where}\quad a_{ij}=\text{AttentionWeight}(t_{i},t_{j}).$  |
L124: 
L125: Here, $a_{ij}$ represents the attention weight from token $t_{i}$ to token $t_{j}$.
L126: As an illustrative example, we use a sample question from GSM8K (cite99†Cobbe et al., 2021 ) and generate the reasoning trace with the Phi-4-Reasoning model (cite98†Abdin et al., 2025 ). cite101†fig. 2 shows the corresponding attention heatmap. The results indicate that in the shallow layers, the attention distribution is relatively uniform across all tokens.
L127: However, as we move to deeper layers and later heads, the model begins to focus more on specific tokens, particularly those in the reasoning steps and the final answer. This suggests that the model progressively refines its focus towards the most relevant parts of the reasoning trace as it processes the information.
L128: #### 3.2 Impact of Reasoning Trace Components on Answer Prediction
L129: To quantify the impact of different components of the reasoning trace on final answer prediction, we conduct an additional experiment analyzing the summed attention weight distribution to the final answer token </think>, which allows us to measure how strongly each reasoning step contributes to the model’s ultimate decision and provides insights into whether the model grounds its prediction in meaningful intermediate reasoning or relies on superficial correlations.
L130: We divide the reasoning process into four components: the question $Q$, the reasoning steps $R_{1},R_{2},\ldots,R_{m}$, and the final answer $A$. For each component, we compute the total attention weight contributing to the first token of the final answer: $W_{\text{trace}}=\sum_{t_{i}\in T_{\text{trace}}}a_{iA}$, where $T_{\text{trace}}$ is the set of tokens in a given component, and $a_{iA}$ denotes the attention weight from token $t_{i}$ to the </think> token.
L131: cite102†Image: Refer to caption Figure 3: Total attention weight distribution to the final answer token </think> from different components of the reasoning trace. We visualize the total attention weight distribution of the Phi-4-Reasoning model on a sample GSM8K question, using transformer layers $1$, $30$, and $40$. The results show that a few reasoning traces contribute strongly to the final token </think>, while many traces have negligible influence, particularly in the layers $30$ and $40$.
L132: As shown in cite103†fig. 3 , different reasoning traces contribute unequally to final answer generation. While a few traces show strong influence, most contribute weakly, and some exhibit almost no contribution at all.
L133: cite104†Image: Refer to caption Figure 4: Theoretical Analysis of Reasoning Outlier Removal. We conduct a theoretical analysis with Phi-4-Reasoning model to demonstrate that removing reasoning outliers using the $\mathop{\rm{Softmax}}_{1}$ function (FROST) can preserve or even enhance the model’s reasoning capacity.
L134: As shown in the figure, the attention weight distribution before and after outlier removal indicates that the model’s focus on critical reasoning traces is maintained or improved, while the influence of outliers is significantly reduced.
L135: #### 3.3 Defining and Characterizing Reasoning Outliers
L136: As observed in cite11†section 3.1 , many reasoning traces contribute negligibly to the final answer. These traces often correspond to verification, self-checking, or repetition of prior reasoning steps. Their presence forces LRMs to generate more tokens than necessary, substantially reducing reasoning efficiency. A potential cause (cite87†Sui et al., 2025 ) is that model developers often encourage extended reasoning steps to maximize accuracy.
--------------------------------------------------------------------------------
Principled Fine-tuning of LLMs from User-Edits: A Medley of Preference, Supervision, and Reward (https://arxiv.org/html/2601.19055v1)
citeturn28140view1 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19055v1","lineno":119}); Total lines: 1163
L89: The necessity for user edits is due to deficiencies in the agent’s response $y$. Further, the more edits the user has to make, the more deficient is the agent’s response. We can measure this deficiency with an edit cost $c=\Delta_{\textrm{edit}}(y,y^{\prime})$ where $\Delta_{\textrm{edit}}:\mathcal{Y}^{2}\rightarrow[0,c_{\textrm{max}}]$ is a suitable edit distance metric. The edit cost $c$ is higher if the user performs more edits and 0 only if edits are empty ($y=y^{\prime}$).
L90: Following Gao et al., cite43†Gao et al. (2024a) , we use Levenhstein edit distance over sub-tokens for defining $\Delta_{\textrm{edit}}$ in our experiments. However, our analysis and algorithm development are independent of the choice of $\Delta_{\textrm{edit}}$. We are now ready to state our formal setup.
L91: Formal Learning Setup. cite54†Protocol 1 states our formal setup. We assume access to a dataset of $n$ user edits $\mathcal{D}=\{(x_{i},y_{i},y^{\prime}_{i}\}_{i=1}^{n}$ and a policy class $\Pi$. For every $i\in[n]$, we assume $x_{i}\sim\rho(\cdot)$, $y_{i}\sim\pi_{\mathrm{ref}}(\cdot\mid x_{i})$, and $y^{\prime}_{i}\sim q(\cdot\mid x_{i},y_{i})$, where $\rho$ is the context distribution and $\pi_{\mathrm{ref}}$ is a reference policy used to generate the agent response.
L92: The reference policy can be a pre-trained LLM that is used to warmstart the problem. This is a typical deployment dataset that is encountered in writing and coding assistant applications. This data distribution can be used to perform fine-tune policies in the offline learning phase (cite59†line 2 ).
L93: After this, the agent is evaluated over a series of $T$ episodes during the online learning phase. In each interaction, the world (which includes the user) will provide a context $x_{t}\sim\rho$ (cite60†line 4 ). The agent can generate a response $y_{t}$ for this context (cite61†line 7 ). Finally, the user generates an edit $y^{\prime}_{t}$ which leads to an edit cost of $c_{t}$ to the agent (cite62†line 6 -cite63†7 ).
L94: The goal of the agent is to minimize the total edits performed during these $T$ episodes (cite64†line 10 ). We allow the agent to perform online learning during these $T$ episodes. However, $T$ may not be large enough to perform a full fine-tuning. Consequently, any learning algorithm should try to effectively use the edited dataset $\mathcal{D}$.
L95: Our setup can be applied to both settings where edits are performed by an arbitrary set of people or when they are performed by a single person or a particular group. In the first case, we need to learn general preferences, whereas the latter is a personalization setting since we need to learn the preferences of a particular person or group.
L96: 
L97: Protocol 1 Finetuning LLMs from User Edits. An algorithm needs to implement the lines in brown.
L98: 1: Given a dataset $\mathcal{D}=\{(x_{i},y_{i},y^{\prime}_{i})\}^{n}_{i=1}$ of user edits. Also, given a policy class $\Pi$.
L99: 
L100: 2: Initialize agent using $\mathcal{D}$ // Offline learning phase
L101: 
L102: 3: for $t=1,2,3,\cdots,T$ do
L103: 
L104: 4:   World presents context $x_{t}$
L105: 
L106: 5:   Agent generates a response $y_{t}$         $\left.\begin{array}[]{@{}c@{}}\\
L107: \\
L108: \\
L109: \\
L110: \end{array}\color[rgb]{0,0,1}\right\}\color[rgb]{0,0,1}\begin{tabular}[]{l}// Online learning and evaluation phase\end{tabular}$
L111: 6:   User edits the response to $y^{\prime}_{t}$
L112: 
L113: 7:   Agent receives a cost for edits $c_{t}=\Delta_{\textrm{edit}}(y_{t},y^{\prime}_{t})$
L114: 
L115: 8: Return $\sum_{t=1}^{T}c_{t}$
L116: We define a few useful concepts to enable us to state our formal objective. We first define the expected cost of a response $y$ in context $x$ as $c(x,y)=\mathbb{E}_{y^{\prime}\sim q(\cdot\mid x,y)}\left[\Delta_{\textrm{edit}}(y,y^{\prime})\right]$. Given a policy $\pi\in\Pi$, we then define its expected cost as $J(\pi)=\mathbb{E}_{x\sim\rho,y\sim\pi(\cdot\mid x)}\left[c(x,y)\right]$. We also define a $\beta$-KL regularized objective as:
L117:  | $$J_{\beta}(\pi)=\mathbb{E}_{x\sim\rho,y\sim\pi(\cdot\mid x)}\left[c(x,y)+\beta\log\frac{\pi(y\mid x)}{\pi_{\mathrm{ref}}(y\mid x)}\right].$$  |  | (1)
L118: It is well-known that optimal solution for objective in cite65†Equation 1 is given by $\pi_{\star}^{\beta}(y|x)=\frac{\pi_{\mathrm{ref}}(y^{\prime}|x)}{Z(x)}\exp\left(\frac{-c(x,y)}{\beta}\right)\pi_{\mathrm{ref}}(y|x)$ where $Z(x)=\sum_{y^{\prime}\in\mathcal{Y}}\exp\left(\frac{-c(x,y^{\prime})}{\beta}\right)$ cite66†Rafailov et al. (2024) . We assume $\pi_{\star}^{\beta}\in\Pi$ for the given $\beta$ and following RLHF literature cite45†Ouyang et al. (2022) ; cite66†Rafailov et al.
L119: (2024) , we compete with this KL-regularized optimal policy. Formally, we define the sub-optimality (${\tt SubOpt}$) of a policy $\pi$ and the regret (${\tt Reg}_{T}$) of an agent during the online learning phase as:
L120:  | $${\tt SubOpt}(\pi)=J_{\beta}(\pi)-J_{\beta}(\pi_{\star}^{\beta}),\quad{\tt Reg}_{T}=\sum_{t=1}^{T}{\tt SubOpt}\left(\pi_{t}\right).$$  |  | (2)
L121: where $\pi_{t}$ is the policy played by the agent in the $t^{th}$ episode. We also define $D(\pi,\pi^{\prime})=\mathbb{E}_{x\sim\rho}\left[\left\|\pi(\cdot\mid x)-\pi^{\prime}(\cdot\mid x)\right\|_{\textrm{TV}}\right]$ as the expected total-variation distance between two policies $\pi$ and $\pi^{\prime}$. Our goal is to find an interactive learning algorithm that learns from the offline dataset $\mathcal{D}$ and minimizes the regret ${\tt Reg}_{T}$ during the online learning phase with high probability.
L122: ### 3 Principled Learning from User-Edits
L123: 
L124: There are two stages of learning in cite54†Protocol 1 offline and online. We discuss learning in these two stages below where one has access to a moderately large dataset of user edits and a much more limited number of online learning episodes.
L125: #### 3.1 Offline Learning from User-Edits
L126: 
L127: Our learning protocol (cite54†Protocol 1 ) contains multiple feedback sources that are typically studied separately in the ML literature. We discuss learning algorithms for each feedback source below.
L128: 
L129: A. Learning from User Edit Supervision. User edits $y^{\prime}$ provide a reasonable sample of the desired behavior. Therefore, one can directly learn a policy $\hat{\pi}_{\textrm{SUP}}$ by fine-tuning on the user-edits:
L130:  | $$\hat{\pi}_{\textrm{SUP}}=\arg\max_{\pi\in\Pi}\ell_{\textrm{SUP}}(\pi),\quad\mbox{where}\quad\ell_{\textrm{SUP}}(\pi)=\frac{1}{n}\sum_{i=1}^{n}\log\pi(y^{\prime}_{i}\mid x_{i}).$$  |  | (3)
L131: B. Learning from Preferences. It is possible that users only partially improve the agent’s response $y$ when editing it to $y^{\prime}$ and that the optimal response is still far from $y^{\prime}$. In this case, fine-tuning on $y^{\prime}$ can lead to sub-optimal behavior. In contrast, one can use the observation that as users edited $y$ to $y^{\prime}$, this implies that $y^{\prime}$ is preferred over $y$ and we can use this to perform learning from preferences.
L132: We can use any preference-learning approach with dataset $\{(x_{i},y_{i},y^{\prime}_{i})\}_{i=1}^{n}$ where $y^{\prime}_{i}\succeq y_{i}$. For example, we can perform Direct Preference Optimization (DPO) (cite66†Rafailov et al., 2024 ) to learn policy $\hat{\pi}_{\textrm{PREF}}$:
L133:  | $\displaystyle\hat{\pi}_{\textrm{PREF}}$  | $\displaystyle=\arg\max_{\pi\in\Pi}\ell_{\textrm{PREF}}(\pi),\quad\mbox{where}$  |  | (4)
L134:  | $\displaystyle\ell_{\textrm{PREF}}(\pi)$  | $\displaystyle=\frac{1}{n}\sum_{i=1}^{n}\log\sigma\left(\beta\log\frac{\pi(y^{\prime}_{i}\mid x_{i})}{\pi_{\mathrm{ref}}(y^{\prime}_{i}\mid x_{i})}-\beta\log\frac{\pi(y_{i}\mid x_{i})}{\pi_{\mathrm{ref}}(y_{i}\mid x_{i})}\right).$  |
L135: We emphasize an important difference between the distribution over preferences in cite67†Equation 4 and the typical RLHF literature cite44†Christiano et al. (2017) ; cite68†Bai et al. (2022) ; cite45†Ouyang et al. (2022) , where the preference pair $(y,y^{\prime})$ is typically generated by independently sampling from the reference policy. In contrast, in our setting only one response is generated from the reference policy whereas the other is generated by user edits.
L136: This distributional change impacts both the theoretical analysis and empirical performance.
L137: C. Learning from Cost. We observe a cost $c_{i}=\Delta_{\textrm{edit}}(y_{i},y^{\prime}_{i})$ for every datapoint which is a sampled from our cost function $c(x,y)=\mathbb{E}_{y^{\prime}\sim q(\cdot\mid x,y)}\left[\Delta_{\textrm{edit}}(y,y^{\prime})\right]$. We can, therefore, use this to train a cost model which can be used to perform reinforcement learning. Formally, given a cost model family $\mathcal{F}$ we first learn a cost model via square-loss regression:
L138:  | $$\widehat{f}=\arg\min_{f\in\mathcal{F}}\frac{1}{n}\sum_{i=1}^{n}\left(f(x_{i},y_{i})-c_{i}\right)^{2}$$  |  | (5)
L139: A direct empirical approach will be to use this cost function and perform RL on an empirical distribution over the contexts in $\mathcal{D}$. However, $\widehat{f}$ need not be well-calibrated for all responses. Motivated by this consideration, we define a pessimistic cost function, $\bar{f}(x,y)=\max_{f\in\tilde{\mathcal{F}}}f(x,y)$ where the set of functions $\tilde{\mathcal{F}}=\left\{f\in\mathcal{F}\text{ s.t.
L140: }\sum_{i=1}^{n}\left(f(x,y)-\hat{f}(x,y)\right)\leq\gamma(\mathcal{F},\delta)\right\}$ for $\gamma(\mathcal{F},\delta)=\mathcal{O}\left(\log\left(\frac{|\mathcal{F}|}{\delta}\right)\right)$ is a confidence set of cost functions that agree with the historical data. We then train the policy $\hat{\pi}_{\textrm{RL}}$ to optimize this cost under KL-constraints on our input contexts.
L141:  | $$\hat{\pi}_{\textrm{RL}}=\arg\min_{\pi\in\Pi}\mathbb{E}_{i\sim{\tt Unf}([n]),y\sim\pi(\cdot\mid x_{i})}\left[\bar{f}(x_{i},y)+\beta\log\frac{\pi(y\mid x_{i})}{\pi_{\mathrm{ref}}(y\mid x_{i})}\right]$$  |  | (6)
L142: 
L143: While computing the $\bar{f}$ is computationally impractical in the general setting, we neverthless use this pessimistic RL algorithm in cite69†Equation 6 for our theoretical analysis.
L144: Early-Ensembling of Losses. As we will demonstrate later, the aforementioned three approaches have different trade-offs. Therefore, it might be advantageous to learn a robust policy by optimizing jointly over their losses. We call such an approach an early ensembling. For example, it is quite common in RLHF literature to add the supervised learning loss to the preference learning loss cite70†Pang et al. (2024) :
L145:  | $$\hat{\pi}_{\textrm{EF}}=\arg\min_{\pi\in\Pi}\left(\ell_{\textrm{PREF}}(\pi)+\lambda\ell_{\textrm{SUP}}(\pi)\right).$$  |  | (7)
L146: 
L147: We later empirically investigate the form of early ensembling described in cite71†Equation 7 .
L148: #### 3.2 Adaptation During the Online Learning Case
L149: 
L150: During the online learning phase, we encounter a small number of episodes where the main goal is to evaluate the agent. In practice, this will be the deployment phase where the agent interacts with real users. However, this also provides an opportunity to perform any additional adaptation.
L151: 
L152: Algorithm 1 ${\tt LateEnsemble}$ of Policies using Upper Confidence Bound.
L153: 1: Given a dataset $\mathcal{D}=\{(x_{i},y_{i},y^{\prime}_{i})\}^{n}_{i=1}$ of user edits. Also, given a policy class $\Pi$.
L154: 
L155: 2: Create a list of policies $\Psi=\left[\hat{\pi}_{\textrm{SUP}},\hat{\pi}_{\textrm{PREF}},\hat{\pi}_{\textrm{RL}},\hat{\pi}_{\textrm{EF}}\right]$ by fine-tuning on $\mathcal{D}$    // Offline learning
L156: 
L157: 3: Define total cost $C(\pi)=0$ and count $N(\pi)=0$ for each policy $\pi\in\Psi$
L158: 
L159: 4: for $t=1,2,3,\cdots,T$ do
L160: 
L161: 5:   World presents context $x_{t}$
L162: 6:   If $t\leq|\Psi|$, then $\pi_{t}=\Psi[t]$ else $\pi_{t}=\arg\min_{\pi\in\Psi}\left\{\frac{C(\pi)}{N(\pi)}-\alpha\sqrt{\frac{\log(t)}{N(\pi)}}\right\}$
L163: 
L164: 7:   $y_{t}\sim\pi_{t}(\cdot\mid x_{t})$                        $\left.\begin{array}[]{@{}c@{}}\\
L165: \\
L166: \\
L167: \\
L168: \end{array}\color[rgb]{0,0,1}\right\}\color[rgb]{0,0,1}\begin{tabular}[]{l}// Online learning\end{tabular}$
L169: 
L170: 8:   User edits the response to $y^{\prime}_{t}$
L171: 9:   Agent receives a cost for edits $c_{t}=\Delta_{\textrm{edit}}(y_{t},y^{\prime}_{t})$
L172: 
L173: 10:   Update cost and counts: $C(\pi_{t})=C(\pi_{t})+c_{t}$; $N(\pi_{t})=N(\pi_{t})+1$.
L174: A key challenge of offline approaches is that different methods have different trade-offs. Early-ensembling approaches may not be able to effectively balance between these trade-offs. This is especially true, if the user distribution at test time is different from train time, which can happen in practice. Unfortunately, the small number of online episodes makes it challenging to do any effective fine-tuning.
L175: Motivated by these two considerations, we employ a very simple approach of training a set of policies using the different offline learning methods. During the online learning phase, we then run a bandit algorithm to select which of the learned policy to use for generating the response. We use the user-edit cost as input to the bandit algorithm. We call this approach a late-ensembling of policies. cite72†Algorithm 1 gives an example using the Upper Confidence Bound (UCB) approach cite73†Auer et al.
L176: (2002) ; cite74†Lai and Robbins (1985) ; cite75†Bubeck et al. (2012) , however, other bandit approaches can also be used.
L177: Pure Online Learning Setting. In cite19†Appendix A , we consider a pure online learning variant of cite54†Protocol 1 with a large $T$ and without an offline learning phase, and derive a no-regret algorithm for it.
L178: ### 4 Theoretical Analysis of Learning from Edits
L179: 
L180: In the last decade, significant theoretical understanding has been achieved in reinforcement learning where the feedback is reward, and imitation learning where the feedback is action. Can we achieve the same for learning from edits? We initiate the theoretical understanding of learning from edits to provide a motivation for our algorithm design and predict experimental phenomena.



# std1controls

FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning (https://arxiv.org/html/2601.19001v1)
citeturn28141view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28140view0","lineno":141}); Total lines: 468
L131: cite102†Image: Refer to caption Figure 3: Total attention weight distribution to the final answer token </think> from different components of the reasoning trace. We visualize the total attention weight distribution of the Phi-4-Reasoning model on a sample GSM8K question, using transformer layers $1$, $30$, and $40$. The results show that a few reasoning traces contribute strongly to the final token </think>, while many traces have negligible influence, particularly in the layers $30$ and $40$.
L132: As shown in cite103†fig. 3 , different reasoning traces contribute unequally to final answer generation. While a few traces show strong influence, most contribute weakly, and some exhibit almost no contribution at all.
L133: cite104†Image: Refer to caption Figure 4: Theoretical Analysis of Reasoning Outlier Removal. We conduct a theoretical analysis with Phi-4-Reasoning model to demonstrate that removing reasoning outliers using the $\mathop{\rm{Softmax}}_{1}$ function (FROST) can preserve or even enhance the model’s reasoning capacity.
L134: As shown in the figure, the attention weight distribution before and after outlier removal indicates that the model’s focus on critical reasoning traces is maintained or improved, while the influence of outliers is significantly reduced.
L135: #### 3.3 Defining and Characterizing Reasoning Outliers
L136: As observed in cite11†section 3.1 , many reasoning traces contribute negligibly to the final answer. These traces often correspond to verification, self-checking, or repetition of prior reasoning steps. Their presence forces LRMs to generate more tokens than necessary, substantially reducing reasoning efficiency. A potential cause (cite87†Sui et al., 2025 ) is that model developers often encourage extended reasoning steps to maximize accuracy.
L137: In the meantime, the model may generate redundant or irrelevant information, leading to inefficient and incorrect reasoning. As a result, we define reasoning traces with low attention weight and negligible contribution to the final answer as reasoning outliers.
L138: To identify and remove reasoning outliers, we observe that they share similar characteristics with attention outliers (cite63†Luo et al., 2025b ; cite64†Hu et al., 2024 ). Motivated by this, we adopt $\mathop{\rm{Softmax}}_{1}$ (cite105†eq. 1 ) to detect and eliminate reasoning outliers during the reasoning process, and provide a comprehensive proof of its efficiency in cite17†section 5 .
L139: 
L140:  | $\displaystyle\mathrm{Softmax}_{1}(x_{i})=\frac{\exp(x_i)}{\sum_{j}\exp(x_j)+1},$  |  | (1)
L141: where $x_{i}$ represents the attention weight of token $t_{i}$.
L142: ##### Theoretical Analysis.
L143: We conduct a theoretical analysis to show that removing reasoning outliers with the $\mathop{\rm{Softmax}}_{1}$ function preserves, and can even enhance, the reasoning capacity of LRMs. In our experiments, we use the Phi-4-Reasoning (cite98†Abdin et al., 2025 ) to generate reasoning traces for a sample GSM8K question (cite99†Cobbe et al., 2021 ). Specifically, we compare the last layer’s attention distribution in head 15 under vanilla attention and $\mathop{\rm{Softmax}}_{1}$ attention (FROST).
L144: As shown in cite106†fig. 4 , $\mathop{\rm{Softmax}}_{1}$ reduces the influence of outliers while maintaining or strengthening focus on critical reasoning traces. This analysis supports our approach of using $\mathop{\rm{Softmax}}_{1}$ to effectively identify and eliminate reasoning outliers, thereby improving the efficiency and reliability of LRMs. For more details of the theoretical proof, please refer to cite17†section 5 .
L145: ### 4 FROST
L146: 
L147: cite107†Image: Refer to caption Figure 5: Overview of the FROST workflow We replace the vanilla $\mathop{\rm{Softmax}}$ layer with an outlier-removal layer based on $\mathop{\rm{Softmax}}_{1}$, followed by SFT to adapt model parameters to the new activation function. We observe that our method significantly reduces the number of low-attention sentences.
L148: To enhance the reasoning efficiency of LRMs, we propose supervised fine-tuning (SFT) with reasoning outlier removal, as illustrated in cite108†fig. 5 .
L149: In the SFT stage, we train on math problems with detailed reasoning steps and answers. During training, we replace the vanilla $\mathop{\rm{Softmax}}$ with $\mathop{\rm{Softmax}}_{1}$ (cite105†eq. 1 ), enabling the model to focus on critical reasoning traces while suppressing outliers.
L150: Unlike prior methods that employ $\mathop{\rm{Softmax}}_{1}$ for outlier removal—requiring either training from scratch (cite64†Hu et al., 2024 ) or multi-step continual learning (cite63†Luo et al., 2025b )—our approach achieves effective outlier removal with only a few steps of fine-tuning from existing pretrained checkpoints, making it more efficient and practical. We optimize model parameters using cross-entropy loss and apply LoRA (cite109†Hu et al., 2021 ) to further reduce training cost.
L151: ### 5 Theoretical Analysis
L152: 
L153: In this section, we provide a brief theoretical analysis showing that $\mathop{\rm{Softmax}}_{1}$ can operate at the sentence level to remove reasoning outliers in LRMs. We provide a theoretical proof that our method achieves deployment-time suppression in efficient reasoning, consistent with our findings in cite106†fig. 4 .
L154: ##### Setup.
L155: Let a token sequence be partitioned into sentences $\{S_{i}\}_{i=1}^{m}$. For a query $q\in\mathbb{R}^{d}$ and keys $\{k_{t}\}\subset\mathbb{R}^{d}$, define token compatibilities $z_{t}\;=\;\mathrm{Softmax}_{1}(\frac{\langle q,k_{t}\rangle}{\sqrt{d}})v_{t}$, where $t$ is the token index in $S_{i}$ and $v_{t}\in\mathbb{R}^{d}$ denotes the token value for each token in sentence $S_{i}$. Let $\phi:\mathbb{R}^{|S_{i}|}\to\mathbb{R}$ be a monotone pooling operator (e.g., sum/mean/logsumexp/max).
L156: Define sentence scores $s_{i}=\phi\bigl(\{z_{t}\}_{t\in S_{i}}\bigr)$ and $s=(s_{1},\ldots,s_{m})\in\mathbb{R}^{m}$. Define the probability simplex $\Delta^{m-1}\;=\;\Bigl\{\,\alpha\in\mathbb{R}^{m}\ \big|\ \alpha_{i}\geq 0,\ \sum_{i=1}^{m}\alpha_{i}=1\,\Bigr\}.$
L157: ###### Assumption 5.1 ($\mathop{\rm{Softmax}}_{1}$ operator).
L158: 
L159: There exists a $\mathop{\rm{Softmax}}_{1}$ mapping $\sigma_{1}:\mathbb{R}^{m}\to\Delta^{m-1}$ such that:
L160: 
L161:   1. 1.
L162: 
L163: Order preservation: If $x_{i}\geq x_{j}$ then $\sigma_{1}(x)_{i}\geq\sigma_{1}(x)_{j}$.
L164: 
L165:   2. 2.
L166: 
L167: Shift invariance: $\sigma_{1}(x+c\mathbf{1})=\sigma_{1}(x)$ for all $c\in\mathbb{R}$.
L168: 
L169:   3. 3.
L170: Tail contraction: There exists $\kappa\in(0,1)$ such that for all $x\in\mathbb{R}^{m}$, $\frac{\|\sigma_{1}(x)\|_{\infty}}{\mathrm{median}(\sigma_{1}(x))}\ \leq\ \kappa\,\frac{\|x\|_{\infty}}{\mathrm{median}(x)}.$
L171: 
L172:   4. 4.
L173: 
L174: Smoothness and positivity: $\sigma_{1}$ is continuously differentiable on $\mathbb{R}^{m}$ and $\sigma_{1}(x)_{i}>0$ for all finite $x$.
--------------------------------------------------------------------------------
FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning (https://arxiv.org/html/2601.19001v1)
citeturn28141view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28140view0","lineno":246}); Total lines: 468
L232: DRP  | 0.6500  | 902.50  | 0.2100  | 1680.33  | 0.0450  | 1350.77  | 0.1120  | 1604.22  | +0.048  | -85.41
L233: SelfBudgeter  | 0.6900  | 1850.00  | 0.2300  | 1520.00  | 0.0520  | 1256.00  | 0.1300  | 1298.00  | +0.069  | +11.13
L234: ThinkLess  | 0.7200  | 1785.00  | 0.2500  | 1405.00  | 0.0600  | 1205.00  | 0.1450  | 1220.00  | +0.087  | -66.12
L235: Ours  | 0.7551  | 137.55  | 0.3040  | 98.20  | 0.0974  | 149.93  | 0.1551  | 109.23  | +0.122  | -1346.14
L236: ##### Models.
L237: In our experiments, we use Phi-4-Reasoning (cite98†Abdin et al., 2025 ),Magistral-Small-1.1 (cite112†Rastogi et al., 2025 ) and GPT-oss (cite111†Agarwal et al., 2025 ) as backbone models for efficient reasoning.
L238: Specifically, we adopt the Phi-4-Reasoning^{*}^{*} * https://huggingface.co/microsoft/Phi-4-reasoning, Magistral-Small-1.1^{*}^{*} * https://huggingface.co/mistralai/Magistral-Small-2507 and GPT-oss-20B-finetune^{*}^{*} * https://huggingface.co/openai/gpt-oss-20b checkpoints, both finetuned on mathematical datasets with detailed reasoning steps and answers using SFT under the FROST method.
L239: ##### Datasets.
L240: 
L241: Following the setup in (cite113†Zhao et al., 2025a ), we use OpenR1 (cite114†Hugging Face, 2025 ) as the training corpus. To evaluate reasoning efficiency and generalization on complex mathematical problems, we adopt four out-of-domain benchmarks: GSM8K (cite99†Cobbe et al., 2021 ), MATH500 (cite115†Lightman et al., 2024 ), AIME24 (cite116†of America, 2024 ), and Minerva (cite117†Dyer & Gur-Ari, 2022 ). All datasets are designed for mathematical question answering.
L242: ##### Metrics.
L243: 
L244: To evaluate the effectiveness of our efficient reasoning strategy, we report pass@1 as the accuracy metric and use the number of tokens in the reasoning response to measure token efficiency.
L245: ##### Baselines.
L246: We select five representative methods covering key paradigms of efficient reasoning: (1) TALE (cite57†Han et al., 2025 ): a prompt-based approach that uses a soft token budget to generate concise reasoning responses. (2) DRP (cite59†Jiang et al., 2025b ): an SFT-based method that distills reasoning paths from a teacher model and applies step-level pruning to produce concise, skill-aware reasoning traces.
L247: (3) SelfBudgeter (cite92†Li et al., 2025 ): a reinforcement learning-based method that iteratively shortens the reasoning path by optimizing a token budget under budget and format reward signals. (4) ThinkLess (cite118†Fang et al., 2025 ): a reinforcement learning-based method that optimizes reasoning by detecting critical thinking points and skipping low-value steps. It introduces a reward function that balances accuracy with token usage, enabling models to “think less” while maintaining performance.
L248: We use the same hyperparameters as specified in their respective studies to ensure standardized evaluation conditions, enabling precise comparisons of each efficient reasoning method.
L249: ##### Results.
L250: As shown in cite119†table 1 , FROST achieves the best overall performance across state-of-the-art efficient reasoning methods, delivering slight accuracy improvements while substantially reducing token usage in response generation. Specifically, FROST improves accuracy by an average of 26.70% and reduces token usage by 69.68% on the three base models, GPT-OSS-20B, Magistral-Small-1.1 and Phi-4-reasoning.
L251: Although TALE achieves the highest accuracy on certain tasks, this comes at the cost of significantly longer responses. This observation aligns with our assumption that excessively long or overly short responses can degrade model performance. By reducing token usage and focusing on high-attention sentences—i.e., critical reasoning traces—FROST lowers the probability of hallucination or misleading content and grounds responses in essential reasoning.
L252: However, FROST may still occasionally prune low-attention but important reasoning steps, which explains why its accuracy is not always the best across all baselines.
L253: #### 6.1 Supplementary Experiments
L254: 
L255: In this section, we conduct additional experiments to examine the influence of our method’s performance at different training stages and under different attention functions.
L256: Table 2: Performance of Different Activation Functions. We evaluate the impact of activation functions on method performance under the same training setup in FROST, using Phi-4-Reasoning across four mathematical datasets (GSM8K, MATH500, AIME24, and Minerva). Pass@1 and token usage (#Tk) are reported as evaluation metrics, with variance omitted since it is consistently $\leq$ 2%. Best results are shown in bold, and second-best are underlined.
L257: In most settings, FROST achieves the best performance, with $\mathop{\rm{Entmax15}}$ consistently ranking second.
L258: Method  | GSM8K  | MATH500  | AIME24  | Minerva  | $\overline{\text{Pass@1}}$  | $\overline{\#\text{Tk}}$
L259: Pass@1  | #Tk  | Pass@1  | #Tk  | Pass@1  | #Tk  | Pass@1  | #Tk
L260: Base  | 0.9242  | 1017.70  | 0.5480  | 1721.95  | 0.0667  | 1017.70  | 0.2500  | 1898.86  | 0.4472  | 1414.05
L261: $\mathop{\rm{Softmax}}$  | 0.8317  | 1160.63  | 0.4880  | 1379.52  | 0.1333  | 1909.07  | 0.2390  | 1934.72  | 0.4230  | 1595.99
L262: $\mathop{\rm{Sparsemax}}$  | 0.8188  | 160.99  | 0.5120  | 451.59  | 0.1667  | 948.60  | 0.2647  | 580.84  | 0.4406  | 535.26
L263: $\mathop{\rm{Entmax15}}$  | 0.8984  | 163.75  | 0.5520  | 406.97  | 0.1667  | 876.63  | 0.2831  | 439.48  | 0.4751  | 471.71
L264: $\mathop{\rm{Softmax}}_{1}$ (FROST)  | 0.9311  | 154.33  | 0.5980  | 344.37  | 0.2667  | 899.80  | 0.2716  | 401.19  | 0.5169  | 449.92
L265: ##### Efficiency of Different Activation Functions.
L266: To evaluate the contribution of $\mathop{\rm{Softmax}}_{1}$ in FROST, we conduct experiments comparing FROST with different activation functions: vanilla $\mathop{\rm{Softmax}}$, $\mathop{\rm{Sparsemax}}$ (cite120†Hu et al., 2023 ; cite121†Martins & Astudillo, 2016 ), and $\mathop{\rm{Entmax15}}$ (cite122†Wu et al., 2024 ; cite123†Correia et al., 2019 ). Here, $\mathop{\rm{Entmax15}}$ is a special case of Tsallis $\alpha$-entmax transformations, which interpolate between softmax and sparsemax.
--------------------------------------------------------------------------------
Principled Fine-tuning of LLMs from User-Edits: A Medley of Preference, Supervision, and Reward (https://arxiv.org/html/2601.19055v1)
citeturn28141view2 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: open({"ref_id":"turn28140view1","lineno":181}); Total lines: 1163
L162: 6:   If $t\leq|\Psi|$, then $\pi_{t}=\Psi[t]$ else $\pi_{t}=\arg\min_{\pi\in\Psi}\left\{\frac{C(\pi)}{N(\pi)}-\alpha\sqrt{\frac{\log(t)}{N(\pi)}}\right\}$
L163: 
L164: 7:   $y_{t}\sim\pi_{t}(\cdot\mid x_{t})$                        $\left.\begin{array}[]{@{}c@{}}\\
L165: \\
L166: \\
L167: \\
L168: \end{array}\color[rgb]{0,0,1}\right\}\color[rgb]{0,0,1}\begin{tabular}[]{l}// Online learning\end{tabular}$
L169: 
L170: 8:   User edits the response to $y^{\prime}_{t}$
L171: 9:   Agent receives a cost for edits $c_{t}=\Delta_{\textrm{edit}}(y_{t},y^{\prime}_{t})$
L172: 
L173: 10:   Update cost and counts: $C(\pi_{t})=C(\pi_{t})+c_{t}$; $N(\pi_{t})=N(\pi_{t})+1$.
L174: A key challenge of offline approaches is that different methods have different trade-offs. Early-ensembling approaches may not be able to effectively balance between these trade-offs. This is especially true, if the user distribution at test time is different from train time, which can happen in practice. Unfortunately, the small number of online episodes makes it challenging to do any effective fine-tuning.
L175: Motivated by these two considerations, we employ a very simple approach of training a set of policies using the different offline learning methods. During the online learning phase, we then run a bandit algorithm to select which of the learned policy to use for generating the response. We use the user-edit cost as input to the bandit algorithm. We call this approach a late-ensembling of policies. cite72†Algorithm 1 gives an example using the Upper Confidence Bound (UCB) approach cite73†Auer et al.
L176: (2002) ; cite74†Lai and Robbins (1985) ; cite75†Bubeck et al. (2012) , however, other bandit approaches can also be used.
L177: Pure Online Learning Setting. In cite19†Appendix A , we consider a pure online learning variant of cite54†Protocol 1 with a large $T$ and without an offline learning phase, and derive a no-regret algorithm for it.
L178: ### 4 Theoretical Analysis of Learning from Edits
L179: 
L180: In the last decade, significant theoretical understanding has been achieved in reinforcement learning where the feedback is reward, and imitation learning where the feedback is action. Can we achieve the same for learning from edits? We initiate the theoretical understanding of learning from edits to provide a motivation for our algorithm design and predict experimental phenomena.
L181: #### 4.1 Theoretical Setup and Assumptions.
L182: We start by stating our modeling assumption for the user distribution in cite76†Assumption 1 . We assume that the user is more likely to edit a response $y$ to $y^{\prime}$ instead of the reverse depending upon how much more likely is $y^{\prime}$ under the optimal policy $\pi^{\star}$ instead of $y$. This is stated formally in cite77†Equation 8 which we call the balance equation.
L183: This equation can be viewed as serving a similar purpose as the Bradley-Terry distribution in RLHF cite78†Bradley and Terry (1952) ; cite44†Christiano et al. (2017) by providing a smooth characterization of user behavior. We also assume that the user distribution has a non-zero probability of generating the optimal response for any input response $y$. This probability can be small but does not need to scale with the size of the generation space $|\mathcal{Y}|$.
L184: ###### Assumption 1 (User Distribution).
L185: 
L186: There exists a (known) $\beta>0$ such that the user distribution satisfies the balance equation below:
L187: 
L188:  | $$\forall x\in\mathcal{X},y,y^{\prime}\in\mathcal{Y},\quad\frac{q(y^{\prime}\mid x,y)}{q(y\mid x,y^{\prime})}=\frac{\pi_{\star}^{\beta}(y^{\prime}\mid x)}{\pi_{\star}^{\beta}(y\mid x)}.$$  |  | (8)
L189: Further, for any $x\in\mathcal{X}$, the user has at least an $\gamma_{\textrm{min}}(x)>0$ (possibly user dependent) probability of generating the optimal response $y^{\star}=\arg\max_{y\in\mathcal{Y}}\pi_{\star}^{\beta}(y\mid x)$:
L190: 
L191:  | $$\forall x\in\mathcal{X},y\in\mathcal{Y},\quad q(y^{\star}\mid x,y)\geq\gamma_{\textrm{min}}(x)$$  |  | (9)
L192: 
L193: In Appendix cite20†A.1 , we provide an example where this assumption holds.
L194: ###### From Balance Equation to Bradley-Terry Distribution.
L195: An important consequence of cite76†Assumption 1 is that the preference distribution in cite67†Equation 4 satisfies the Bradley-Terry assumption. To see this, we first realize that our preference pairs will contain two responses $(y,y^{\prime})$ given a context $x$ in precisely two situations: either we generate $y\sim\pi_{\mathrm{ref}}(\cdot\mid x)$ and it is edited to $y^{\prime}\sim q(\cdot\mid x,y)$, or we generate $y^{\prime}\sim\pi_{\mathrm{ref}}(\cdot\mid x)$ and it is edited to $y\sim q(\cdot\mid x,y)$.
L196: The probability that we prefer $y^{\prime}$ over $y$ ($y^{\prime}\succeq y$) is then given by the probability of the first situation normalized by the joint probability, i.e.,
L197:  | $\displaystyle\mathbb{P}(y^{\prime}\succeq y\mid x,y,y^{\prime})$  | $\displaystyle=\frac{\pi_{\mathrm{ref}}(y\mid x)q(y^{\prime}\mid x,y)}{\pi_{\mathrm{ref}}(y\mid x)q(y^{\prime}\mid x,y)+\pi_{\mathrm{ref}}(y^{\prime}\mid x)q(y\mid x,y^{\prime})},$  |
L198:  |  | $\displaystyle=\frac{\pi_{\mathrm{ref}}(y\mid x)\pi^{\beta}_{\star}(y^{\prime}\mid x)}{\pi_{\mathrm{ref}}(y\mid x)\pi^{\beta}_{\star}(y^{\prime}\mid x)+\pi_{\mathrm{ref}}(y^{\prime}\mid x)\pi^{\beta}_{\star}(y\mid x)},\quad\mbox{(from \hyperref@@ii[eqn:balance-eqn]{Equation~\ref*{eqn:balance-eqn}})}$  |
L199:  |  | $\displaystyle=\sigma\left(c(x,y)-c(x,y^{\prime})\right),\hskip 28.45274pt\mbox{(using $\pi^{\star}_{\beta}(\tilde{y}\mid x)=\frac{\pi_{\mathrm{ref}}(y\mid x)}{Z(x)}\exp(-\frac{c(x,y)}{\beta})$}.$  |
L200: This justifies using DPOs even though the joint distribution over the preference pairs $(y,y^{\prime})$ is different than IID sampling from $\pi_{\mathrm{ref}}$ which is typically studied in the RLHF literature.
L201: As we are working with function approximations, we assume policy realizability, i.e., that our function class is expressive enough to contain the desired policies. This is a standard assumption in theoretical analysis of interactive learning algorithms (cite79†Huang et al., 2024b ; cite80†Xie et al., 2024 ).
L202: ###### Assumption 2 (Realizability).
L203: 
L204: We assume that $\pi_{\star}^{\beta}\in\Pi$ and $q\circ\pi\in\Pi$ where $q\circ\pi$ is the policy defined as $q\circ\pi(y|x)=\sum_{y^{\prime}\in\mathcal{Y}}q(y|x,y^{\prime})\pi(y^{\prime}|x)$.
L205: 
L206: Our first result establishes cite76†Assumption 1 implies the edits induce a contraction property on the user distribution,
L207: ###### Lemma 1.
L208: 
L209: For any $\pi\in\Pi$, the user distribution satisfies the following contraction property:
L210: 
L211:  | $\displaystyle\forall x\in\mathcal{X},\qquad\left\|q\circ\pi(Y\mid x)-\pi_{\star}^{\beta}(Y\mid x)\right\|_{\textrm{TV}}\leq\left(1-\gamma_{\textrm{min}}(x)\right)\left\|\pi(Y\mid x)-\pi_{\star}^{\beta}(Y\mid x)\right\|_{\textrm{TV}}$  |
--------------------------------------------------------------------------------
Principled Fine-tuning of LLMs from User-Edits: A Medley of Preference, Supervision, and Reward (https://arxiv.org/html/2601.19055v1)
citeturn28141view3 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: open({"ref_id":"turn28140view1","lineno":243}); Total lines: 1163
L235: Discussion of Trade-Offs. Theorems cite88†1 , cite84†2 , and cite89†3 provide some guidance on the cases where using the edit data as a preference dataset is better or worse than doing imitation learning on the edits or learning the cost function and doing RL. When the preference coverage coefficient $C_{\mathrm{PREF}}$ is small, the sample complexity of DPO can be much lower than that of SFT and RL.
L236: When the weighted approximation error $\min\left\{\eta_{\max}D(\pi_{\mathrm{ref}},\pi_{\star}^{\beta}),\bar{\eta}_{\max}D^{1/2}(\pi_{\mathrm{ref}},\pi_{\star}^{\beta})\right\}$ is smaller than the target error $\epsilon$, SFT is the preferred method.
L237: Finally, when the approximation error and preference concentrability are large, but policy concentrability is small and the cost function is simple—for instance, a low-dimensional linear function—learning the cost function and then optimizing it is the most sample-efficient approach.
L238: ### 5 Experimental Results and Discussion
L239: 
L240: We empirically evaluate our theoretical findings in this section to see if they apply in complex settings similar to what is encountered in practice.
L241: Task Setup. We evaluate on two tasks: email writing and summarization, from Gao et al., cite43†Gao et al. (2024a) . For each task, there exists a dataset of articles from 4 domains. Corresponding to each task and domain, there is a list of latent user preferences described as a preference string, for example, “structured, straight to the points, respectful, professional greeting and closing”. The setup follows cite54†Protocol 1 .
L242: In each round, the agent is given a context describing a task along with a given article. For example, summarize a given article. The agent does not have access to the latent preference string but must generate a response that satisfies this preference. An LLM user generates an edit given the response, context, and latent preference string corresponding to the domain of the article in the context.
L243: The use an LLM-based user allows for reproducible experiments which facilitates rapid advancement in algorithm development.^{1}^{1} 1 Gao et al., cite43†Gao et al. (2024a) took steps to validate their LLM user. Please see their paper for details. Finally, we compute edit distance using Levenshtein distance normalized by the number of tokens in the agent response. We use the NLTK word tokenizer to compute the edit distance.
L244: We use Qwen 3 32B instruct model as our user but remove think tokens before using the response.
L245: The key challenge of this task is that latent preferences are context-dependent as articles from different domains have different preferences. Further, even for a single domain, there are multiple preferences in a preference string. For example, the aforementioned preference string contains multiple individual preferences such as “second person narrative” and “show emotions”. These two challenges occur in real-world applications.
L246: For example, a person may prefer to write informal emails to their friends but write formal reviews for their office reports. Note that the context does not state which domain the article in the given context comes from. An LLM agent must implicitly infer the domain from the context, learn the appropriate preference for it, and then use it to generate an appropriate response.
L247: Strong and Weak User. We extend the original setup of Gao et al., cite43†Gao et al. (2024a) to consider two types of users: strong users and weak users. A strong user generates edits based on every individual preference in the article’s latent preference string. In contrast, a weak user samples a subset of preferences in the article’s preference string and uses them to generate the edits.
L248: For example, in any given interaction a weak user may sample two preferences “second person narrative” and “brief” and perform edits to satisfy these while ignoring the other preferences in the preference string. The weak user models user who may only prefer to perform small edits at a time. Conceptually, both the weak and strong users have the same optimal behavior.
L249: This is because the optimal response that satisfies all the preference for the strong user, also satisfies any subset of preference that the weak user can sample. However, while strong user perform edits that rapidly converges to the optimal policy (higher $\gamma_{\textrm{min}}$), the weak user’s edit will slowly take the response towards the optimal behavior (smaller $\gamma_{\textrm{min}}$).
L250: Offline Dataset. We collect an offline interaction dataset between the agent model and the user. This dataset is supposed to represent deployment logs found in typical LLM agent applications for writing and coding assistants. We use Llama 3.1 8b Instruct model as our agent model. We perform generate responses by doing greedy decoding. We collect a dataset of 20,000 examples for the summarization task and 10,000 examples for the email writing task.
L251: We collect these datasets separately with both strong and weak users. This gives us 4 separate offline datasets.
L252: Online Learning Phase. We evaluate the model for $T=200$ examples for summarization and email writing. We always use the strong user during test time regardless of which user was used to generate the offline dataset. We run each experiment with 3 different seeds.
L253: Methods and Implementation. We consider the following approaches: (i) ${\tt Base}$ which generates from the base agent model, (ii) ${\tt SFT}$ which performs SFT on the training data, (iii) ${\tt DPO}$ which runs the DPO algorithm on the training data, (iv) ${\tt EarlyEnsemble}$ which performs early ensembling of ${\tt DPO}$ and ${\tt SFT}$ losses (cite71†Equation 7 ), and (v) ${\tt LateEnsemble}$ which performs late ensembling (cite72†Algorithm 1 ) using policies trained by methods (ii)-(iv).
L254: All generations are performed greedily and with a max number of generation tokens of 1000. We do not evaluate cite69†Equation 6 give challenges in implementing it.
L255: We sweep over various hyperparameters including learning rate and epochs for ${\tt SFT}$ and ${\tt DPO}$, as well as $\beta$ for ${\tt DPO}$, and $\beta,\lambda$ for ${\tt EarlyEnsemble}$. We pick the best hyperparameters by maximizing log-loss on a held-out validation set of 200 user-edits. We found in early studies that despite sweeping over the hyperparameters, both ${\tt DPO}$ and ${\tt EarlyEnsemble}$ learn policies that tend to repeat text until their max tokens expire.



# std1end

FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning (https://arxiv.org/html/2601.19001v1)
citeturn28142view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28140view0","lineno":265}); Total lines: 468
L246: We select five representative methods covering key paradigms of efficient reasoning: (1) TALE (cite57†Han et al., 2025 ): a prompt-based approach that uses a soft token budget to generate concise reasoning responses. (2) DRP (cite59†Jiang et al., 2025b ): an SFT-based method that distills reasoning paths from a teacher model and applies step-level pruning to produce concise, skill-aware reasoning traces.
L247: (3) SelfBudgeter (cite92†Li et al., 2025 ): a reinforcement learning-based method that iteratively shortens the reasoning path by optimizing a token budget under budget and format reward signals. (4) ThinkLess (cite118†Fang et al., 2025 ): a reinforcement learning-based method that optimizes reasoning by detecting critical thinking points and skipping low-value steps. It introduces a reward function that balances accuracy with token usage, enabling models to “think less” while maintaining performance.
L248: We use the same hyperparameters as specified in their respective studies to ensure standardized evaluation conditions, enabling precise comparisons of each efficient reasoning method.
L249: ##### Results.
L250: As shown in cite119†table 1 , FROST achieves the best overall performance across state-of-the-art efficient reasoning methods, delivering slight accuracy improvements while substantially reducing token usage in response generation. Specifically, FROST improves accuracy by an average of 26.70% and reduces token usage by 69.68% on the three base models, GPT-OSS-20B, Magistral-Small-1.1 and Phi-4-reasoning.
L251: Although TALE achieves the highest accuracy on certain tasks, this comes at the cost of significantly longer responses. This observation aligns with our assumption that excessively long or overly short responses can degrade model performance. By reducing token usage and focusing on high-attention sentences—i.e., critical reasoning traces—FROST lowers the probability of hallucination or misleading content and grounds responses in essential reasoning.
L252: However, FROST may still occasionally prune low-attention but important reasoning steps, which explains why its accuracy is not always the best across all baselines.
L253: #### 6.1 Supplementary Experiments
L254: 
L255: In this section, we conduct additional experiments to examine the influence of our method’s performance at different training stages and under different attention functions.
L256: Table 2: Performance of Different Activation Functions. We evaluate the impact of activation functions on method performance under the same training setup in FROST, using Phi-4-Reasoning across four mathematical datasets (GSM8K, MATH500, AIME24, and Minerva). Pass@1 and token usage (#Tk) are reported as evaluation metrics, with variance omitted since it is consistently $\leq$ 2%. Best results are shown in bold, and second-best are underlined.
L257: In most settings, FROST achieves the best performance, with $\mathop{\rm{Entmax15}}$ consistently ranking second.
L258: Method  | GSM8K  | MATH500  | AIME24  | Minerva  | $\overline{\text{Pass@1}}$  | $\overline{\#\text{Tk}}$
L259: Pass@1  | #Tk  | Pass@1  | #Tk  | Pass@1  | #Tk  | Pass@1  | #Tk
L260: Base  | 0.9242  | 1017.70  | 0.5480  | 1721.95  | 0.0667  | 1017.70  | 0.2500  | 1898.86  | 0.4472  | 1414.05
L261: $\mathop{\rm{Softmax}}$  | 0.8317  | 1160.63  | 0.4880  | 1379.52  | 0.1333  | 1909.07  | 0.2390  | 1934.72  | 0.4230  | 1595.99
L262: $\mathop{\rm{Sparsemax}}$  | 0.8188  | 160.99  | 0.5120  | 451.59  | 0.1667  | 948.60  | 0.2647  | 580.84  | 0.4406  | 535.26
L263: $\mathop{\rm{Entmax15}}$  | 0.8984  | 163.75  | 0.5520  | 406.97  | 0.1667  | 876.63  | 0.2831  | 439.48  | 0.4751  | 471.71
L264: $\mathop{\rm{Softmax}}_{1}$ (FROST)  | 0.9311  | 154.33  | 0.5980  | 344.37  | 0.2667  | 899.80  | 0.2716  | 401.19  | 0.5169  | 449.92
L265: ##### Efficiency of Different Activation Functions.
L266: To evaluate the contribution of $\mathop{\rm{Softmax}}_{1}$ in FROST, we conduct experiments comparing FROST with different activation functions: vanilla $\mathop{\rm{Softmax}}$, $\mathop{\rm{Sparsemax}}$ (cite120†Hu et al., 2023 ; cite121†Martins & Astudillo, 2016 ), and $\mathop{\rm{Entmax15}}$ (cite122†Wu et al., 2024 ; cite123†Correia et al., 2019 ). Here, $\mathop{\rm{Entmax15}}$ is a special case of Tsallis $\alpha$-entmax transformations, which interpolate between softmax and sparsemax.
L267: We evaluate these strategies on four datasets—GSM8K, MATH500, AIME24, and Minerva—using Phi-4-Reasoning. As shown in cite124†table 4 , the results demonstrate that FROST achieves the best overall performance in both Pass@1 accuracy and token usage. Specifically, the average accuracy increases by 15.65%, while the number of tokens decreases by 68.18% compared to the base model.
L268: FROST also surpasses the overall performance of $\mathop{\rm{Sparsemax}}$ and $\mathop{\rm{Entmax15}}$, which tend to sharpen both low- and high-attention sentences, potentially cutting off critical reasoning traces. In contrast, FROST is less prone to this issue. The only exception is the Minerva dataset, where $\mathop{\rm{Entmax15}}$ attains higher accuracy than FROST while maintaining a similar number of tokens.
L269: The underlying reason is difficult to explain at this stage, but it is a pleasant surprise that, except for GSM8K, the overall performance of $\mathop{\rm{Sparsemax}}$ and $\mathop{\rm{Entmax15}}$ does not decline significantly and in some cases even surpasses the base model. This offers a perspective contrary to that of cite125†Yang et al. (2025) ; cite126†Wang (2024) .
L270: Table 3: Outlier Removal Performance in FROST. We evaluate outlier removal performance on the AIME2024 dataset using the Phi-4-Reasoning model. As outlier metrics, we report the maximum infinity norm $\norm{\mathbf{x}}_{\infty}$ and average kurtosis of the activation tensors. To assess the proportion of critical traces, we also report the average sentence entropy before and after applying FROST. All results are reported with variance omitted, as it is consistently $\leq$ 2%.
L271: Best results are shown in bold, and second-best results are underlined. In most settings, FROST achieves the best performance in outlier removal and yields higher average sentence entropy. These metrics demonstrate that our method effectively removes reasoning outliers, thereby improving both reasoning performance and efficiency.
L272: Method  | Maximum Infinity Norm $\norm{\mathbf{x}}_{\infty}\downarrow$  | Average Kurtosis $\downarrow$  | Average Sentence Entropy $\uparrow$  | Pass@1 $\uparrow$  | #Tk $\downarrow$
L273: Base  | 35.31  | 241.72  | 2.71  | 0.0667  | 1017.70
L274: $\mathop{\rm{Softmax}}$  | 34.53  | 189.36  | 2.79  | 0.1333  | 1909.07
L275: $\mathop{\rm{Sparsemax}}$  | 34.06  | 152.18  | 2.93  | 0.1667  | 948.60
L276: $\mathop{\rm{Entmax15}}$  | 30.39  | 43.72  | 2.92  | 0.1667  | 876.63
L277: FROST  | 29.67  | 21.54  | 3.07  | 0.2667  | 899.80
L278: ##### Outlier Removal Performance in FROST.
L279: To evaluate the performance of FROST in removing attention outliers, we employ two outlier-specific metrics: the maximum infinity norm $\norm{\mathbf{x}}_{\infty}$ of the activation tensors $\mathbf{x}$ across all Transformer layers, and the average kurtosis of $\mathbf{x}$, which together quantify the presence of outliers. In addition, to demonstrate that removing attention outliers increases the probability assigned to critical sentences, we introduce an entropy-based evaluation metric.
L280: Following cite62†Wang et al. (2025) , token entropy serves as an indicator of criticality: critical tokens tend to exhibit higher entropy than non-critical ones. When a sentence contains more critical tokens, it is expected to exert a stronger influence on final answer generation. Accordingly, we use average sentence entropy to assess whether the reasoning traces in FROST become more critical after training.
L281: In our experiments, we analyze these metrics on the AIME2024 dataset using the Phi-4-Reasoning model and compare them with the base model. As shown in cite127†table 3 , FROST effectively reduces outliers, evidenced by lower maximum infinity norm $\norm{\mathbf{x}}_{\infty}$ and average kurtosis values. Furthermore, the increase in average sentence entropy indicates that FROST strengthens the model’s focus on critical reasoning traces, thereby improving reasoning efficiency.
L282: Specifically, we reduce the maximum infinity norm $\norm{\mathbf{x}}_{\infty}$ by 15.97% and the average kurtosis by 91.09%. In addition, the average sentence entropy increases by 13.28% compared to the base model. Additionally, the results show that reasoning outlier metrics—maximum infinity norm $\norm{\mathbf{x}}_{\infty}$ and average kurtosis—are closely related to model performance and average sentence entropy.
L283: Higher outlier values correspond to lower sentence entropy and less efficient reasoning traces. This further supports that the reasoning-outlier removal contributes to more efficient reasoning. The only exception is that the average sentence entropy of $\mathop{\rm{Sparsemax}}$ is similar to $\mathop{\rm{Entmax15}}$, while the reasoning outlier values of $\mathop{\rm{Entmax15}}$ are much smaller than those of $\mathop{\rm{Sparsemax}}$.
L284: A plausible explanation is that both $\mathop{\rm{Entmax15}}$ and $\mathop{\rm{Sparsemax}}$ act as sharpening activations that jointly suppress low- and high-valued attention scores. This bidirectional truncation can inadvertently remove parts of crucial reasoning traces, lowering average sentence entropy and reducing Pass@1 performance.
L285: Meanwhile, attention outlier metrics such as the maximum infinity norm and kurtosis primarily reflect internal activation dynamics rather than output quality, explaining their relative stability despite external performance declines. Since both activations reshape attention distributions similarly, their outputs also appear alike—with comparable Pass@1 and entropy values—though $\mathop{\rm{Entmax15}}$’s smoother contraction yields slightly less degradation in outlier metrics.
L286: Overall, this indicates that excessive sharpening can eliminate valuable reasoning signals even while suppressing attention outliers, highlighting $\mathop{\rm{Softmax}}_{1}$’s advantage through selective tail contraction.
L287: #### 6.2 Generalizability of Model
L288: In this section, we evaluate the generalization ability of FROST on out-of-domain reasoning tasks to verify that its improvements do not harm, but rather preserve or enhance, the model’s generation quality beyond the training domain. Using Phi-4-Reasoning as the base model, we test on three additional reasoning benchmarks—LeetCode (cite128†Xia et al., 2025b ), LiveCodeBench (cite129†Jain et al., 2024 ), and UGPhysical (cite130†Xu et al., 2025b )—covering both coding and physical reasoning tasks.
L289: The results in cite124†table 4 show that FROST preserves—and even improves—generalization to unseen reasoning tasks. This is expected because FROST filters out uncritical reasoning traces in a manner that generalizes beyond the specific tasks used during fine-tuning. Since FROST only replaces the attention activation with $\mathop{\rm{Softmax}}_{1}$ and uses lightweight LoRA updates, the parameter shift is minimal, ensuring that the model’s broader reasoning ability remains intact.
--------------------------------------------------------------------------------
FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning (https://arxiv.org/html/2601.19001v1)
citeturn28142view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28140view0","lineno":442}); Total lines: 468
L428: As shown in cite149†table 5 , FROST achieves the fastest training time among all methods, while also minimizing computation cost and inference time during deployment. This demonstrates that our approach not only accelerates training but also reduces deployment overhead.
L429: #### F.2 Attention Distributions of Activation Functions
L430: We conduct an additional experiment to analyze the attention distribution of GPT-OSS-20B on a sample from the GSM8K dataset. As shown in cite150†fig. 6 , FROST effectively removes a large number of low-attention sentences while retaining significant ones. In contrast, the vanilla model produces many sentences with low attention weights, and $\mathop{\rm{Sparsemax}}$ and $\mathop{\rm{Entmax15}}$ retain only one to two sentences, often aggressively discarding important reasoning traces.
L431: This visualization provides an explanation consistent with the performance results reported in cite124†table 4 .
L432: cite151†Image: Refer to caption Figure 6: Attention Distribution of Each Activation Function.
L433: ### Appendix G Influence the attention dynamics of $\mathop{\rm{Softmax}}_{1}$ during training and inference
L434: We observe that incorporating $\mathop{\rm{Softmax}}_{1}$ significantly influences both training and inference attention dynamics across transformer layers. During supervised fine-tuning (SFT), $\mathop{\rm{Softmax}}_{1}$ enforces tail contraction by suppressing low-attention activations, which stabilizes gradients and reduces the variance of updates propagated through residual connections.
L435: This effect leads to faster convergence of LoRA adapters, as the low-rank parameter subspace more efficiently aligns with critical attention directions, improving overall adaptation coverage within fewer training steps. This observation is consistent with cite63†Luo et al. (2025b) ; cite64†Hu et al. (2024) .
L436: Across layers, $\mathop{\rm{Softmax}}_{1}$ reshapes the attention landscape—shallow layers become more selective in contextual grounding, while deeper layers exhibit higher entropy concentration around critical reasoning traces. During inference, this sharpening propagates forward, effectively filtering redundant reasoning sentences while maintaining coherence.
L437: Together, these behaviors demonstrate that $\mathop{\rm{Softmax}}_{1}$ not only enhances efficient reasoning but also accelerates LoRA-SFT optimization by improving the representational focus of each attention head.
L438: ### Appendix H Influence of $\mathop{\rm{Softmax}}_{1}$ Across Layers
L439: We analyze the effect of $\mathop{\rm{Softmax}}_{1}$ across transformer layers by visualizing the attention distributions of head 15 for both vanilla $\mathop{\rm{Softmax}}$ and $\mathop{\rm{Softmax}}_{1}$. As shown in cite152†figs. 7 and cite153†8 , $\mathop{\rm{Softmax}}_{1}$ consistently suppresses attention outliers, leading to smoother and more stable activations across the network.
L440: In lower layers, $\mathop{\rm{Softmax}}_{1}$ contracts heavy tails and mitigates rare extreme peaks, enhancing local feature mixing with higher-entropy and reduced kurtosis distributions. In higher layers, it suppresses residual long-range spikes and sharpens focus on semantically relevant tokens, yielding sparser yet more stable attention and clearer causal information flow.
L441: cite154†Image: Refer to caption Figure 7: Theoretical Analysis of Reasoning Outlier Removal in All Layers cite155†Image: Refer to caption Figure 8: Attention Distribution of $\mathop{\rm{Softmax}}_{1}$ Across All Layers
L442: ### Appendix I Extended Attention Heatmaps Across Additional Layers and Heads
L443: 
L444: In this section, we present extended attention heatmaps covering additional layers and heads. Specifically, we analyze Layers 0, 5, 15, 25, 30, 35, and 39 and Heads 0, 5, 10, 15, 20, 25, 30, 35, and 39 to provide a more comprehensive view of attention evolution across the network. The corresponding observations are illustrated in cite156†fig. 9 .
L445: cite157†Image: Refer to caption Figure 9: Extended Attention Heatmaps Across Additional Layers and Heads
L446: ### Appendix J Human Expert Evaluation
L447: We invite three computer science students specializing in reasoning models to annotate reasoning traces generated by the original and FROST-trained models. We then compare the traces pruned by FROST and evaluate their criticality based on relevance and contribution to the final answer. Averaging across all evaluators, FROST achieves 92% accuracy in correctly removing non-critical reasoning traces. Only 8% of reasoning traces are incorrectly removed, which significantly degrades final-answer accuracy.
L448: These mistakenly pruned traces are typically long and contain repeated information that supports self-verification and error correction. However, they also provide critical content—such as key equations—in the end of trace. This observation suggests a potential explanation for why FROST achieves the second-best Pass@1 score in the Phi-4-Reasoning experiment shown in cite119†table 1 .
L449: ### Appendix K Disclosure of LLM Usage
L450: 
L451: In our paper and project, we use large language models (LLMs) to help revise the text for greater conciseness and precision.
L452: 
L453: Experimental support, please cite158†view the build logs for errors. Generated by cite159†L A T E xml†math.nist.gov .
L454: ## Instructions for reporting errors
L455: 
L456: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
L457: 
L458:   * Click the "Report Issue" () button, located in the page header.
L459: 
L460: Tip: You can select the relevant text first, to include it in your report.
L461: Our team has already identified cite160†the following issues†github.com . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
L462: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a cite161†list of packages that need conversion†github.com , and welcome cite162†developer contributions†github.com .
L463: 
L464: We gratefully acknowledge support from our major funders, cite163†member institutions†info.arxiv.org , , and all contributors.
L465: cite164†About†info.arxiv.org · cite165†Help†info.arxiv.org · cite166†Contact†info.arxiv.org · cite167†Subscribe†info.arxiv.org · cite168†Copyright†info.arxiv.org · cite169†Privacy†info.arxiv.org · cite170†Accessibility†info.arxiv.org · cite171†Operational Status (opens in new tab)†status.arxiv.org L466: 
L467: Major funding support from
--------------------------------------------------------------------------------
Principled Fine-tuning of LLMs from User-Edits: A Medley of Preference, Supervision, and Reward (https://arxiv.org/html/2601.19055v1)
citeturn28142view2 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: open({"ref_id":"turn28140view1","lineno":255}); Total lines: 1163
L245: The key challenge of this task is that latent preferences are context-dependent as articles from different domains have different preferences. Further, even for a single domain, there are multiple preferences in a preference string. For example, the aforementioned preference string contains multiple individual preferences such as “second person narrative” and “show emotions”. These two challenges occur in real-world applications.
L246: For example, a person may prefer to write informal emails to their friends but write formal reviews for their office reports. Note that the context does not state which domain the article in the given context comes from. An LLM agent must implicitly infer the domain from the context, learn the appropriate preference for it, and then use it to generate an appropriate response.
L247: Strong and Weak User. We extend the original setup of Gao et al., cite43†Gao et al. (2024a) to consider two types of users: strong users and weak users. A strong user generates edits based on every individual preference in the article’s latent preference string. In contrast, a weak user samples a subset of preferences in the article’s preference string and uses them to generate the edits.
L248: For example, in any given interaction a weak user may sample two preferences “second person narrative” and “brief” and perform edits to satisfy these while ignoring the other preferences in the preference string. The weak user models user who may only prefer to perform small edits at a time. Conceptually, both the weak and strong users have the same optimal behavior.
L249: This is because the optimal response that satisfies all the preference for the strong user, also satisfies any subset of preference that the weak user can sample. However, while strong user perform edits that rapidly converges to the optimal policy (higher $\gamma_{\textrm{min}}$), the weak user’s edit will slowly take the response towards the optimal behavior (smaller $\gamma_{\textrm{min}}$).
L250: Offline Dataset. We collect an offline interaction dataset between the agent model and the user. This dataset is supposed to represent deployment logs found in typical LLM agent applications for writing and coding assistants. We use Llama 3.1 8b Instruct model as our agent model. We perform generate responses by doing greedy decoding. We collect a dataset of 20,000 examples for the summarization task and 10,000 examples for the email writing task.
L251: We collect these datasets separately with both strong and weak users. This gives us 4 separate offline datasets.
L252: Online Learning Phase. We evaluate the model for $T=200$ examples for summarization and email writing. We always use the strong user during test time regardless of which user was used to generate the offline dataset. We run each experiment with 3 different seeds.
L253: Methods and Implementation. We consider the following approaches: (i) ${\tt Base}$ which generates from the base agent model, (ii) ${\tt SFT}$ which performs SFT on the training data, (iii) ${\tt DPO}$ which runs the DPO algorithm on the training data, (iv) ${\tt EarlyEnsemble}$ which performs early ensembling of ${\tt DPO}$ and ${\tt SFT}$ losses (cite71†Equation 7 ), and (v) ${\tt LateEnsemble}$ which performs late ensembling (cite72†Algorithm 1 ) using policies trained by methods (ii)-(iv).
L254: All generations are performed greedily and with a max number of generation tokens of 1000. We do not evaluate cite69†Equation 6 give challenges in implementing it.
L255: We sweep over various hyperparameters including learning rate and epochs for ${\tt SFT}$ and ${\tt DPO}$, as well as $\beta$ for ${\tt DPO}$, and $\beta,\lambda$ for ${\tt EarlyEnsemble}$. We pick the best hyperparameters by maximizing log-loss on a held-out validation set of 200 user-edits. We found in early studies that despite sweeping over the hyperparameters, both ${\tt DPO}$ and ${\tt EarlyEnsemble}$ learn policies that tend to repeat text until their max tokens expire.
L256: We, therefore, perform a post-generation trimming strategy where we trim the generations once it starts repeating 200 consecutive characters. For a fair comparison, we apply this post-processing to the output of all methods. An alternative approach could be to use explicit length penalty cite90†Park et al. (2024) or more stable preference-learning approaches such as Rebel cite91†Gao et al. (2024b) . See cite36†Appendix C for full details on experimental setting.
L257: Method  | Summarization  | Email Writing  |
L258: --- | --- | --- | ---
L259:  | Strong User  | Weak User  | Strong User  | Weak User  | Max SubOpt
L260: --- | --- | --- | --- | --- | ---
L261: Base  | ${0.9455}_{\small\pm 0.01}$  | ${0.9445}_{\small\pm 0.02}$  | ${0.5108}_{\small\pm 0.03}$  | ${0.4923}_{\small\pm 0.01}$  | ${0.7364}_{\small\pm 0.10}$
L262: SFT  | ${0.5377}_{\small\pm 0.02}$  | ${0.9304}_{\small\pm 0.19}$  | ${0.4159}_{\small\pm 0.05}$  | ${0.4539}_{\small\pm 0.03}$  | ${0.5772}_{\small\pm 0.19}$
L263: DPO  | ${1.0790}_{\small\pm 0.06}$  | ${0.8267}_{\small\pm 0.06}$  | ${\textbf{0.3365}}_{\small\pm 0.00}$  | ${\textbf{0.3368}}_{\small\pm 0.01}$  | ${0.8698}_{\small\pm 0.11}$
L264: EarlyEnsemble  | ${\textbf{0.2092}}_{\small\pm 0.09}$  | ${\textbf{0.3586}}_{\small\pm 0.01}$  | ${0.3438}_{\small\pm 0.06}$  | ${0.4864}_{\small\pm 0.01}$  | ${0.1612}_{\small\pm 0.01}$
L265: LateEnsemble  | ${0.2768}_{\small\pm 0.13}$  | ${0.4403}_{\small\pm 0.03}$  | ${0.4202}_{\small\pm 0.11}$  | ${0.3739}_{\small\pm 0.04}$  | ${\textbf{0.1586}}_{\small\pm 0.04}$
L266: Table 1: Results on the summarization and email writing domain. We calculate the mean total edit distance $\frac{1}{T}\sum_{t=1}^{T}c_{t}$ during the online learning phase. We report average performance across 3 seeds.
L267: Method  | Summarization  | Email Writing  |
L268: --- | --- | --- | ---
L269:  | Strong User  | Weak User  | Strong User  | Weak User  | Max. SubOpt
L270: --- | --- | --- | --- | --- | ---
L271: Base  | ${0.8498}_{\small\pm 0.01}$  | ${0.8558}_{\small\pm 0.01}$  | ${0.4241}_{\small\pm 0.01}$  | ${0.4239}_{\small\pm 0.01}$  | ${0.6654}_{\small\pm 0.01}$
L272: SFT  | ${0.4890}_{\small\pm 0.01}$  | ${0.7698}_{\small\pm 0.01}$  | ${0.3377}_{\small\pm 0.02}$  | ${0.3866}_{\small\pm 0.01}$  | ${0.5121}_{\small\pm 0.02}$
L273: DPO  | ${0.9650}_{\small\pm 0.03}$  | ${0.7800}_{\small\pm 0.02}$  | ${0.2955}_{\small\pm 0.01}$  | ${\textbf{0.3047}}_{\small\pm 0.02}$  | ${0.7805}_{\small\pm 0.02}$
L274: EarlyEnsemble  | ${\textbf{0.1845}}_{\small\pm 0.02}$  | ${\textbf{0.2577}}_{\small\pm 0.02}$  | ${\textbf{0.2406}}_{\small\pm 0.03}$  | ${0.4001}_{\small\pm 0.03}$  | ${0.0955}_{\small\pm 0.03}$
L275: LateEnsemble  | ${0.2509}_{\small\pm 0.04}$  | ${0.3403}_{\small\pm 0.01}$  | ${0.3123}_{\small\pm 0.01}$  | ${0.3428}_{\small\pm 0.03}$  | ${\textbf{0.0862}}_{\small\pm 0.02}$
L276: Table 2: Transfer learning results with a Llama-3.3-70B-Instruct User at test time.
L277: Main Results. We report the main results in cite92†Table 1 with the Qwen-3 32B user. We report mean edit cost across rounds ($T$) and seeds. We also report Max. SubOpt that measures worst-case performance gap across the four settings between a given approach and the best performance. We see that ${\tt Base}$ method does not perform well showing the need for adaptation. Intuitively, we would expect a strong user to have strong convergence to the optimal policy.
L278: In our theory, this would be reflected in the value of $\gamma_{\textrm{min}}$ in cite76†Assumption 1 . We see this in our results where ${\tt SFT}$ is able to learn and performs much better when trained and tested on strong user. Its performance when trained on weak user is weaker consistent with cite88†Theorem 1 . In contrast, ${\tt DPO}$’s theoretical analysis does not depend on the choice of $\gamma_{\textrm{min}}$ and instead only depends on coverage and the validity of balance equation.
L279: We see that ${\tt DPO}$ performs better than ${\tt SFT}$ when we train on weak user and test on strong user. However, when both users are strong, then there is no clear winner between ${\tt SFT}$ and ${\tt DPO}$. Overall, this illustrates the trade-off predicted by our theory where ${\tt SFT}$ can take advantage whenever the user-edits converges faster to the optimal policy, however, it is also susceptible when this is not the case whereas ${\tt DPO}$ is more robust to this factor.
L280: We see that ${\tt EarlyEnsemble}$ can exploit these trade-offs to achieve better performance than both ${\tt SFT}$ and ${\tt DPO}$ on the summarization domain, however, it under-performs ${\tt DPO}$ on the email writing domain. One explanation can be sensitivity to the choice of $\lambda$. While we perform a grid search over this hyperparameter, and use a validation loss over user-edits, it is possible that this selection scheme does not correspond well with test-time performance.
L281: Finally, our ${\tt LateEnsemble}$ approach is able to more readily adapt at test time by making suitable trade-offs and achieve the lowest worst case SubOpt value. We emphasize that late ensembling isn’t guaranteed to do better in practice. Specifically, if one of the policy in $\Psi$ on cite93†line 2 in cite72†Algorithm 1 , is always better than others, then UCB will achieve lower performance than this policy due to exploring other sub-optimal policies.
L282: Transfer Learning to Different User LLM. We investigate how robust these methods are to a different user LLM. This mimics a common real-world setting where the training data may come from one set of users, however, testing maybe done with a different set of users. These two sets of users can still have a common preference because these maybe dependent on organization, platform, or other controlled features such as age, or location.
L283: We use Llama-3.3-70B-Instruct model as our user model during the online testing phase while using our previously trained models.  cite94†Table 2 shows the results. We see that the main trends from cite92†Table 1 carry over even when we test with a different user LLM. In particular, our ensemble approach ${\tt LateEnsemble}$ achieves the best SubOpt value.
L284: Sampling Generations and Test-time plot. We provide a few sample generations showing some success and failure cases in  cite95†Table 3 . We also visualize the test-time performance of different methods on the summarization task in cite96†Figure 2 . As we can see, the ${\tt LateEnsemble}$ approach converges to the best method in both cases as expected. We provide additional details in cite36†Appendix C .
L285: Table 3: Generations from ${\tt EarlyEnsemble}$ on the summarization task with a strong user.
L286: Type  | (Latent User Preference String) Agent Response
L287: --- | ---
L288: Success  | (question answering style!) **Q: What was the state of the land and people after the calamity?** A: The land was exhausted, the towns were stripped of their fighting population, and only a shadow of a kingdom remained. $\cdots$ [truncated]
L289:  | (bullet points, parallel structure, brief) **Updated Mn PBPK model**: Reflects rapid Mn association/dissociation in tissues, with saturation of binding sites limiting accumulation.
L290:  | - **Key changes**:
L291:  | - Rapid Mn binding and dissociation rates.
L292:  | - High-affinity binding with rapid exchange between bound and free forms.
L293:  | - Tissue-specific binding capacities to account for background Mn levels.



# std2methodapproval

FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning (https://arxiv.org/html/2601.19001v1)
citeturn28143view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28140view0","lineno":399}); Total lines: 468
L391: Efficient Alignment. In recent years, foundation models (cite134†Zhou et al., 2025 ; cite135†Wang et al., 2024 ; cite136†He et al., 2024 ; cite137†Touvron et al., 2023 ) have shown strong capabilities in solving multitask problems. To further improve their performance on specific tasks, alignment techniques are essential for refining model behavior. However, traditional approaches like RLHF (cite79†Ouyang et al., 2022 ) and DPO (cite80†Rafailov et al., 2023 ) are computationally expensive.
L392: This highlights the urgent need for parameter-efficient fine-tuning methods that offer effective and economical alignment for foundation models. Several traditional methods demonstrate strong capabilities in aligning foundation models, including LoRA (cite109†Hu et al., 2021 ) and QLoRA (cite138†Dettmers et al., 2023 ). Building on this, cite63†Luo et al.
L393: (2025b) propose a LoRA variant that replaces the standard softmax layer with OutEffHop layers (cite64†Hu et al., 2024 ) to improve the efficiency of low-rank adaptation. However, all of these methods are heavily based on LoRA, and when adaptation is required for modules outside the attention architecture, the computational cost increases significantly. cite139†Zhao et al. (2025b) ; cite140†Luo et al. (2025c) propose novel alignment methods that focus on small subsets of neurons within foundation models.
L394: For example, cite139†Zhao et al. (2025b) identify key neurons with high influence on LLMs’ jailbreak defense using latent representations, and fine-tune only these neurons using red-teaming datasets. Our method builds on fast low-rank adaptation techniques (cite63†Luo et al., 2025b ), further improving adaptation efficiency, and integrates them into SFT training to optimize reasoning paths and produce efficient reasoning models.
L395: ### Appendix C Proofs of Main Text
L396: #### C.1 cite141†lemma 5.1 L397: 
L398: Proof of cite141†lemma 5.1 . Monotonicity means that if we increase any input coordinate to $\phi$, its output does not decrease. Let $u=\{z_{t}\}_{t\in S_{i}}$ and $w=\{z_{t^{\prime}}\}_{t^{\prime}\in S_{j}}$. If for each coordinate of $u$ there is a not-smaller coordinate in $w$ replaced by the smaller value, then by repeatedly applying coordinatewise monotonicity we obtain $s_{i}=\phi(u)\ \geq\ \phi(w)=s_{j}.$ Order preservation (P1) then yields $\alpha_{i}\geq\alpha_{j}$.
L399: #### C.2 cite142†theorem 5.1 L400: 
L401: Proof of cite142†theorem 5.1 . By Lemma cite141†5.1 , sentence scores $s$ reflect dominance induced by token compatibilities under $\phi$. Applying Assumption cite110†5.1 (P3) directly to $s$ yields (cite143†2 ). Assumption cite110†5.1 (P2) allows re-centering $s\leftarrow s-c\mathbf{1}$ without changing $\alpha$; thus (cite143†2 ) is invariant to any global shift and depends only on relative separations.
L402: #### C.3 cite144†theorem 5.2 L403: 
L404: Proof of cite144†theorem 5.2 . For (cite145†3 ), apply operator-norm submultiplicativity: $\|W_{o}(\alpha_{i}v_{i})\|\leq\|W_{o}\|_{\mathrm{op}}\cdot\alpha_{i}\|v_{i}\|\leq B_{o}\,\varepsilon\,B_{v}$. To obtain (cite146†4 ), propagate the perturbation through $L$ differentiable layers with Jacobians $J_{\ell}$:
L405:  | $$\|\Delta\ell_{i}^{(L)}\|\ \leq\ \Bigl(\prod_{\ell=1}^{L}\|J_{\ell}\|_{\mathrm{op}}\Bigr)\,\|W_{o}\|_{\mathrm{op}}\,\alpha_{i}\|v_{i}\|\ \leq\ \varepsilon\Bigl(\prod_{\ell=1}^{L}B_{\ell}\Bigr)B_{o}B_{v}.$$  |
L406: Finally, since $\mathop{\rm{Softmax}}_{1}$ is $1$-Lipschitz in $\ell_{\infty}\!\to\!\ell_{1}$, the change in probabilities is bounded by the logit change, yielding (cite147†5 ). Replacing $\prod_{\ell=1}^{L}B_{\ell}$ with $B^{L}$ (by definition of $B$) gives the stated $O(B_{o}B_{v}B^{L}\varepsilon)$ rate. If $B_{o},B_{v},B$ are $O(1)$, the rate simplifies to $O(\varepsilon)$.
L407: ### Appendix D An Example of LRM Reasoning Traces
L408: In this section, we analyze the Phi-4-Reasoning response to the first question of AIME24, which is also illustrated in cite106†fig. 4 . As shown in the color box in cite36†appendix D , traces S1 and S2 are classified as uncritical. Although S2 includes partially critical content such as "So the walking time (actual walking time) plus t minutes equals total time.", its overall reasoning remains non-critical.
L409: Trace S3 represents a critical reasoning step, where the model identifies the two key equations in the problem. Subsequently, from S4 to S19, the model enters a self-verification phase, producing reasoning traces beginning with wait that reflect self-checking and correction. Starting from S20, the model resumes critical reasoning after the signal "We’ll produce final answer in a box.", and by S24, it generates the final answer, concluding its reasoning process.
L410: ### Appendix E Experiment System and Implement Settings
L411: 
L412: #### E.1 Computational Resources
L413: 
L414: We perform all experiments using two NVIDIA H100 GPUs with 80GB of memory and a 12-core INTEL(R) XEON(R) PLATINUM 8592 CPU operating at 1.90GHz. Our code is developed in PyTorch and utilizes the Hugging Face Transformer Library for experimental execution. For running the LLMs, we use the default system prompt provided by the official source and set the temperature to 0.6 to balance consistency and performance.
L415: #### E.2 Hyperparameters
L416: We present the hyperparameters used in the fine-tuning stage for each model. We use AdamW (cite148†Loshchilov & Hutter, 2019 ) as the optimizer. Most other hyperparameters are kept consistent across all models and datasets, including a batch size of 256 during deployment and 8 during training. In training, we also use gradient accumulation with 4 steps and set the weight decay to 0.01 for all training runs. A learning rate of $1e^{-5}$ is used for all models during fine-tuning.
L417: For low-rank adaptation, we use a LoRA rank of 8 and LoRA alpha set to 16. In FROST, we set the maximum training steps to 5,000. All supervised fine-tuning and GRPO training are conducted using mixed precision with bfloat16. In deployment, we set the temperature to 0.6 for all models with top-$p$ sampling at 0.9. For evaluation, we use a maximum generation length of 4096 across all models, except TALE.
L418: ### Appendix F Additional Experiments
L419: 
L420: In this section, we present additional experiments demonstrating that FROST surpasses current state-of-the-art efficient reasoning methods.
L421: #### F.1 Training and Test Time Comparison
L422: 
L423: We conduct experiments to measure the training and inference time of each baseline and compare their computational costs with FROST. For evaluation, test time is measured on the AIME tasks with the GPT-OSS-20B model, while training time is reported using the respective datasets specified in each baseline’s original paper. All experiments are conducted on the same computational resources, as described in cite38†section E.1 .
L424: Table 5: Comparison of Training and Test Time Costs Across Methods. We conduct experiments to measure the training and test time of each method. For test-time evaluation, we use the AIME dataset with the GPT-OSS-20B model. Best results are shown in bold, and second-best are underlined.
L425: Method  | TALE  | DRP  | ThinkLess  | FROST
L426: Training Time (m)  | -  | 353  | 1186  | 204
L427: Test Time (m)  | 56  | 18.5  | 4.2  | 3
L428: As shown in cite149†table 5 , FROST achieves the fastest training time among all methods, while also minimizing computation cost and inference time during deployment. This demonstrates that our approach not only accelerates training but also reduces deployment overhead.
L429: #### F.2 Attention Distributions of Activation Functions
L430: We conduct an additional experiment to analyze the attention distribution of GPT-OSS-20B on a sample from the GSM8K dataset. As shown in cite150†fig. 6 , FROST effectively removes a large number of low-attention sentences while retaining significant ones. In contrast, the vanilla model produces many sentences with low attention weights, and $\mathop{\rm{Sparsemax}}$ and $\mathop{\rm{Entmax15}}$ retain only one to two sentences, often aggressively discarding important reasoning traces.
--------------------------------------------------------------------------------
Pixel-Grounded Retrieval for Knowledgeable Large Multimodal Models (https://arxiv.org/html/2601.19060v1)
citeturn28143view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19060v1","lineno":122}); Total lines: 705
L111: For instance, GLaMM was trained on millions of region-grounded annotations to generate segmentation masks in a conversational setting, while PLUM introduced span-based tagging and a mask feedback loop to iteratively refine object selection. These models show that segmentation can be natively integrated into the reasoning process of LMMs. However, they are trained to answer questions without external retrieval, relying solely on their internal knowledge.
L112: cite89†Image: Refer to caption Figure 2: Overview of the proposed PixSearch framework. The model learns to decide when retrieval is needed, how to query (text, whole image, or segmented region), and grounds its answers in retrieved evidence while preserving mask-generation capabilities.
L113: ## 3 Overview
L114: ### 3.1 Problem Definition
L115: 
L116: We study the Visual Question Answering (VQA) problem, which takes an image $I$ and a question $Q$ regarding the image as input, and outputs an answer $A$ to the question. We assume an external knowledge repository to facilitate question answering. A good answer shall be relevant and helpful, and meanwhile consistent with knowledge present in the repository.
L117: We assume the knowledge repository is accessible through a retrieval API $\texttt{search\_api}(S,k)$, which returns the top-$k$ relevant text chunks on search query $S$. The query can be in three forms: (1) full image, where the API returns information about the image; (2) masked region, normally for a particular entity and the API returns information about the entity; and (3) text span, where the API returns search results for the text query.
L118: An effective MM-RAG solution needs to make the following decisions: 1) whether to issue (a single or multiple) search queries; 2) the modality of each query—full image, masked region, or text span; 3) the specific image region or text span to query; 4) the final answer based on the retrieval evidence. Existing pipeline-based methods separate these abilities, introducing translation errors and instability.
L119: We next describe a uniform framework that resolves all four through an interleaved search-and-generation decoding process.
L120: ### 3.2 PixSearch Framework
L121: 
L122: Figure cite90†2 depicts the PixSearch framework. PixSearch conducts search-interleaved decoding, a retrieval-augmented generation process that enables the model to decide when to retrieve and how to ground retrieved evidence in its multimodal reasoning trajectory. At each decoding step $t$, the model autoregressively predicts the next token $x_{t}$ based on the image $m$ and the previously generated tokens, until an end-of-sequence (</s>) token is reached:
L123:  | $$x_{t}\sim p_{\theta}(x_{t}\mid x_{<t},Q,I).$$  |  | (1)
L124: An output token can be a special control token <search>, at which point the model temporarily halts textual decoding to initiate a retrieval subroutine, which proceeds in three steps. First, the subroutine generates a payload string in $\{\texttt{<image>},\texttt{<region>},\texttt{<text>}\}$^{1}^{1} 1 The model directly generates the textual query instead of <text> to describe the retrieval modality. We then generate the search query for different modalities.
L125: For the image mode, the whole input image $I$ serves as the query. For the region mode, the model invokes its aligned mask decoder to predict a binary mask $\hat{M}=f_{\theta}(I,x_{<t})$, from which a cropped visual query is extracted. For the text mode, the model generates the textual query during decoding.
L126:  | $$S=\begin{cases}I,&\text{if }payload=\texttt{<image>}\\
L127: \texttt{crop}(I,\hat{M}),&\text{if }payload=\texttt{<region>}\\
L128: \texttt{Text},&\text{if }payload=\texttt{Text}\end{cases}$$  |  | (2)
L129:  | $$x_{1:t}\;\leftarrow\;[\,x_{1:t-1},\texttt{<search>},S,\texttt{</search>}].$$  |  | (3)
L130: 
L131: Finally, the subroutine obtains the retrieved evidence:
L132: 
L133:  | $$\textit{E}=\texttt{search\_api}(S,k)$$  |  | (4)
L134: where search_api returns a textual knowledge. This retrieved content is then injected back into the generation stream as an <information> block (abbreviated as <info> hereafter for brevity):
L135: 
L136:  | $$x_{1:t+1}\;\leftarrow\;[\,x_{1:t},\infstart,\textit{E},\infend\,]$$  |  | (5)
L137: 
L138: allowing the model to continue decoding while conditioning on the newly appended evidence.
L139: Through generating multiple <query> blocks and populating back <information> evidence blocks, this decoding strategy results in a dynamic reasoning trajectory that alternates between internal generation and external retrieval, enabling the model to ground answers in factual evidence whereas maintaining fine-grained visual reasoning through region-level queries.
L140: ## 4 PixSearch: Region-level Retrieval for LMMs
L141: ### 4.1 Overview of model training strategy
L142: At the core of PixSearch is a segmentation-capable Large Multimodal Models (i.e., segmenting LMMs (cite86†Rasheed et al., 2024 ; cite84†Lai et al., 2024 ; cite85†Ren et al., 2024b ; cite91†Wang et al., 2024 ; cite88†Blume et al., 2025 )), with two key capabilities required by the framework: segmentation (to facilitate mask generation $f_{\theta}$) and decoding (Eq. cite92†1 -cite93†5 ).
L143: This design exploits the rich textual semantics for pixel-level grounding, encompassing regular open-vocabulary segmentation to referring expression segmentation, while avoiding specialized region-proposal networks (cite94†Ren et al., 2024a ) or external segmentation models (cite95†Kirillov et al., 2023 ) (§ cite17†4.2 ).
L144: Training an end-to-end model to perform segmentation and retrieval-augmented generation jointly is challenging: optimization easily collapses, degrading segmentation accuracy or failing to learn the retrieval control (§cite22†5.3 ). We address this with a two-stage training framework: Stage 1 preserves segmentation and visual grounding, and Stage 2 teaches the model when to retrieve, how to form queries, and how to attend to retrieved external knowledge in the search-interleaved reasoning.
L145: This design enables stable optimization and yields an LMM that can dynamically balance perception and knowledge reasoning. (Section cite18†4.3 )
L146: ### 4.2 PixSearch Model
L147: 
L148: Loss function. We extend the training objectives of segmenting LMM, which allows PixSearch to maintain linguistic coherence while achieving interpretable, text-conditioned segmentation (cite88†Blume et al., 2025 ):
L149:  | $$\mathcal{L}=\underbrace{\mathcal{L}_{\mathrm{LM}}+\lambda_{1}\mathcal{L}_{\mathrm{span}}}_{\text{sequence loss}}+\underbrace{\lambda_{2}\mathcal{L}_{\mathrm{seg}}+\lambda_{3}\mathcal{L}_{\mathrm{BCE}}}_{\text{segmentation loss}}+\underbrace{\lambda_{4}\mathcal{L}_{\mathrm{KL}}}_{\text{regularization}}.$$  |  | (6)
L150: We next describe this formulation in detail. In the sequence supervision, $\mathcal{L}_{\mathrm{LM}}$ stands for the next-token cross-entropy for the decoder, which we will describe in detail in Equation cite96†10 . The other term $\mathcal{L}_{\mathrm{span}}$ is a span-tagging loss for grounding text to image regions. Specifically, let $h_{i}^{L}\!\in\!\mathbb{R}^{d}$ be the final-layer embedding of token $i$.
L151: A span extractor applies bidirectional self-attention to predict BIO (B, I, O) tags for each token (cite97†Ramshaw and Marcus, 1999 ). We train this tagger with cross-entropy $\mathcal{L}_{\text{span}}$; at inference, contiguous $\textit{B}\!\to\!\textit{I}$ chains are merged into spans corresponding to the referred object in the image.
--------------------------------------------------------------------------------
Who’s in Charge? Disempowerment Patterns in Real-World LLM Usage (https://arxiv.org/html/2601.19062v1)
citeturn28143view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19062v1","lineno":295}); Total lines: 920
L286: Actualized disempowerment prevalence. We also found evidence of actualized distortion occurring in real-world interactions. Actualized action distortion appeared in 0.018% of conversations (95% CI: 0.016%–0.021%), while actualized reality distortion was more common at 0.048% (95% CI: 0.045%–0.052%). We did not detect instances of actualized value judgment distortion. Importantly, the absence of detected actualized distortion does not imply that such distortion did not occur.
L287: Distorted actions can unfold without a user’s awareness—for instance, when someone acts on AI guidance they later regret but never returns to the conversation to express that regret. Furthermore, even when users recognize misalignment between their actions and values, they may not revisit the AI assistant to voice dissatisfaction. These measurement limitations suggest our estimates likely represent a lower bound on the true prevalence of actualized disempowerment.
L288: Domain-specific patterns. We find that disempowerment potential varies substantially across interaction domains (cite97†Figure 3 ). Relationships & Lifestyle exhibits the highest rate of disempowerment potential at approximately 8%, followed by Society & Culture and Healthcare & Wellness, each at roughly 5%.
L289: This prevalence far exceeds the population average rate, in part because technical domains such as Software Development and Science & Technology are both common and show substantially lower disempowerment potential rates. We find similar patterns in the rates of actualized disempowerment, though the absolute rates are lower.
L290: This pattern suggests that disempowerment risks are concentrated in domains involving personal and interpersonal decisions, which are inherently value-laden, as compared to more technical domains.
L291: Amplifying factors are associated with disempowerment potential and actualization. We now examine how the presence of amplifying factors correlates with rates of disempowerment potential and actualized disempowerment (cite98†Figure 4 ). Across the amplifying factors, we observe mostly monotonic relationships. That is, as the severity of each amplifying factor increases, both disempowerment potential and disempowerment actualization rates tend to rise substantially.
L292: These findings support our hypothesis that these amplifying factors, while not directly constituting disempowerment, are correlated with conditions under which disempowerment is more likely to occur, and are thus worthy of monitoring.
L293: ### 4.3 In-depth analysis
L294: 
L295: We now turn our attention to better understanding the user and AI assistant behaviors that give rise to disempowerment potential, as well as markers of amplifying factors.
L296: To do so, we present privacy-preserving cluster descriptions of amplifying factors and disempowerment potentials at moderate and severe severity levels. These descriptions include illustrative phrases characterizing behavioral patterns, but no extended verbatim quotes from conversations. Additional examples are provided in Appendix cite30†Appendix A .
L297: In addition, we use Claude Opus 4.5 to code the cluster descriptions on different axes---for example, the mechanism of the distortion potential---and, given the sizes of each cluster, we estimate the proportion of conversations at the moderate and severe severity levels exhibiting each behavior.^{6}^{6} 6 If a cluster mentions two different mechanisms, it is coded as both. This allows us to both qualitatively and quantitatively understand what drives the patterns we observe.
L298: #### 4.3.1 Reality distortion potential
L299: Figure 5: Understanding reality distortion potential. (Top) Illustrative cluster summaries of severe reality distortion potential: validation of persecution narratives involving surveillance and coordinated targeting (left), and validation of grandiose spiritual identity claims (right). Both clusters exhibit similar dynamics—emphatic AI validation, unfalsifiable user frameworks, and escalating elaboration over multiple exchanges.
L300: (Bottom) Quantitative analysis of 132 cluster descriptions derived from 7,200 conversations with moderate or severe reality distortion potential. We estimate the frequency of various factors within conversations among all conversations with moderate or severe reality distortion potential. (a) Distortion mechanisms. Sycophantic validation is the most prevalent, while outright fabrication is rare. (b) Distortion targets: third-party mental states are most common, but all occur frequently.
L301: (c) User behavior: most users actively build upon AI-validated beliefs and seek validation, while reality testing is rare. (d) Conversational trajectory: the majority of conversations exhibit escalating distortion potential over the course of the conversation. Error bars indicate 95% confidence intervals calculated using the Wilson score method.
L302: Qualitative examples. The top row of cite99†Figure 5 presents two cluster summaries illustrating distinct manifestations of severe reality distortion potential. In both cases, the AI assistant consistently and extensively validates users’ beliefs using emphatic language.
L303: Distortion mechanisms. Sycophantic validation emerges as the most common mechanism for reality distortion (cite99†Figure 5 a), followed by false precision—instances where the AI provides unwarranted specificity for inherently unknowable claims. Less common mechanisms include diagnostic claims (e.g., “he is clearly a narcissist”), fabrication of incorrect information, and divination approaches such as tarot interpretation.
L304: These findings suggest that reality distortion potential arises less from the AI inventing false information than from inappropriately validating users’ existing beliefs or expressing false confidence about inherently uncertain matters.
L305: Distortion targets. Third-party mental states constitute the most common target of potential distortion (cite99†Figure 5 b). However, all examined targets—future outcomes, factual reality, and self-concept, identity, and ability—appear with substantial prevalence.
L306: User behavior and trajectory. Examining user behavior and how the scope of possible reality distortion evolves throughout conversations, we find that the most common pattern involves users actively seeking and building upon potential distortions. Accordingly, the majority of clusters exhibit escalating trajectories, where disempowerment potential intensifies over the course of the conversation—for example, by encompassing additional beliefs or producing an increasingly distorted view of reality.
L307: Summary. These findings suggest a dominant pattern for reality distortion potential: users actively seek validation, which the AI then provides, which users then appear to build upon, and so forth.
L308: #### 4.3.2 Value judgment distortion potential
L309: Figure 6: Understanding value judgment distortion potential. (Top) Illustrative cluster summaries of severe value judgment distortion potential: the AI acting as moral arbiter across public figure judgments, societal critiques, and adversarial planning (left), and the AI providing definitive moral verdicts in romantic relationship contexts (right). Both clusters exhibit similar dynamics—confident AI moral assessments, user delegation of evaluative judgment, and acceptance without independent reasoning.
L310: (Bottom) Quantitative analysis of 141 cluster descriptions derived from 7,883 conversations with moderate or severe value judgment distortion potential. We estimate the frequency of various factors within conversations among all conversations with moderate or severe value judgment distortion potential. (a) Distortion mechanisms: character judgments, prescriptive advice, and action judgment are most prevalent.
--------------------------------------------------------------------------------
FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning (https://arxiv.org/html/2601.19001v1)
citeturn28143view3 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: find({"ref_id":"turn28140view0","pattern":"Appendix E"}); Total lines: 468
L399: #### C.2 cite142†theorem 5.1 L400: 
L401: Proof of cite142†theorem 5.1 . By Lemma cite141†5.1 , sentence scores $s$ reflect dominance induced by token compatibilities under $\phi$. Applying Assumption cite110†5.1 (P3) directly to $s$ yields (cite143†2 ). Assumption cite110†5.1 (P2) allows re-centering $s\leftarrow s-c\mathbf{1}$ without changing $\alpha$; thus (cite143†2 ) is invariant to any global shift and depends only on relative separations.
L402: #### C.3 cite144†theorem 5.2 L403: 
L404: Proof of cite144†theorem 5.2 . For (cite145†3 ), apply operator-norm submultiplicativity: $\|W_{o}(\alpha_{i}v_{i})\|\leq\|W_{o}\|_{\mathrm{op}}\cdot\alpha_{i}\|v_{i}\|\leq B_{o}\,\varepsilon\,B_{v}$. To obtain (cite146†4 ), propagate the perturbation through $L$ differentiable layers with Jacobians $J_{\ell}$:
L405:  | $$\|\Delta\ell_{i}^{(L)}\|\ \leq\ \Bigl(\prod_{\ell=1}^{L}\|J_{\ell}\|_{\mathrm{op}}\Bigr)\,\|W_{o}\|_{\mathrm{op}}\,\alpha_{i}\|v_{i}\|\ \leq\ \varepsilon\Bigl(\prod_{\ell=1}^{L}B_{\ell}\Bigr)B_{o}B_{v}.$$  |
L406: Finally, since $\mathop{\rm{Softmax}}_{1}$ is $1$-Lipschitz in $\ell_{\infty}\!\to\!\ell_{1}$, the change in probabilities is bounded by the logit change, yielding (cite147†5 ). Replacing $\prod_{\ell=1}^{L}B_{\ell}$ with $B^{L}$ (by definition of $B$) gives the stated $O(B_{o}B_{v}B^{L}\varepsilon)$ rate. If $B_{o},B_{v},B$ are $O(1)$, the rate simplifies to $O(\varepsilon)$.
L407: ### Appendix D An Example of LRM Reasoning Traces
L408: In this section, we analyze the Phi-4-Reasoning response to the first question of AIME24, which is also illustrated in cite106†fig. 4 . As shown in the color box in cite36†appendix D , traces S1 and S2 are classified as uncritical. Although S2 includes partially critical content such as "So the walking time (actual walking time) plus t minutes equals total time.", its overall reasoning remains non-critical.
L409: Trace S3 represents a critical reasoning step, where the model identifies the two key equations in the problem. Subsequently, from S4 to S19, the model enters a self-verification phase, producing reasoning traces beginning with wait that reflect self-checking and correction. Starting from S20, the model resumes critical reasoning after the signal "We’ll produce final answer in a box.", and by S24, it generates the final answer, concluding its reasoning process.
L410: ### Appendix E Experiment System and Implement Settings
L411: 
L412: #### E.1 Computational Resources
L413: 
L414: We perform all experiments using two NVIDIA H100 GPUs with 80GB of memory and a 12-core INTEL(R) XEON(R) PLATINUM 8592 CPU operating at 1.90GHz. Our code is developed in PyTorch and utilizes the Hugging Face Transformer Library for experimental execution. For running the LLMs, we use the default system prompt provided by the official source and set the temperature to 0.6 to balance consistency and performance.
L415: #### E.2 Hyperparameters
L416: We present the hyperparameters used in the fine-tuning stage for each model. We use AdamW (cite148†Loshchilov & Hutter, 2019 ) as the optimizer. Most other hyperparameters are kept consistent across all models and datasets, including a batch size of 256 during deployment and 8 during training. In training, we also use gradient accumulation with 4 steps and set the weight decay to 0.01 for all training runs. A learning rate of $1e^{-5}$ is used for all models during fine-tuning.
L417: For low-rank adaptation, we use a LoRA rank of 8 and LoRA alpha set to 16. In FROST, we set the maximum training steps to 5,000. All supervised fine-tuning and GRPO training are conducted using mixed precision with bfloat16. In deployment, we set the temperature to 0.6 for all models with top-$p$ sampling at 0.9. For evaluation, we use a maximum generation length of 4096 across all models, except TALE.
L418: ### Appendix F Additional Experiments
L419: 
L420: In this section, we present additional experiments demonstrating that FROST surpasses current state-of-the-art efficient reasoning methods.
L421: #### F.1 Training and Test Time Comparison
L422: 
L423: We conduct experiments to measure the training and inference time of each baseline and compare their computational costs with FROST. For evaluation, test time is measured on the AIME tasks with the GPT-OSS-20B model, while training time is reported using the respective datasets specified in each baseline’s original paper. All experiments are conducted on the same computational resources, as described in cite38†section E.1 .
L424: Table 5: Comparison of Training and Test Time Costs Across Methods. We conduct experiments to measure the training and test time of each method. For test-time evaluation, we use the AIME dataset with the GPT-OSS-20B model. Best results are shown in bold, and second-best are underlined.
L425: Method  | TALE  | DRP  | ThinkLess  | FROST
L426: Training Time (m)  | -  | 353  | 1186  | 204
L427: Test Time (m)  | 56  | 18.5  | 4.2  | 3
L428: As shown in cite149†table 5 , FROST achieves the fastest training time among all methods, while also minimizing computation cost and inference time during deployment. This demonstrates that our approach not only accelerates training but also reduces deployment overhead.
L429: #### F.2 Attention Distributions of Activation Functions
L430: We conduct an additional experiment to analyze the attention distribution of GPT-OSS-20B on a sample from the GSM8K dataset. As shown in cite150†fig. 6 , FROST effectively removes a large number of low-attention sentences while retaining significant ones. In contrast, the vanilla model produces many sentences with low attention weights, and $\mathop{\rm{Sparsemax}}$ and $\mathop{\rm{Entmax15}}$ retain only one to two sentences, often aggressively discarding important reasoning traces.
L431: This visualization provides an explanation consistent with the performance results reported in cite124†table 4 .
L432: cite151†Image: Refer to caption Figure 6: Attention Distribution of Each Activation Function.
L433: ### Appendix G Influence the attention dynamics of $\mathop{\rm{Softmax}}_{1}$ during training and inference
L434: We observe that incorporating $\mathop{\rm{Softmax}}_{1}$ significantly influences both training and inference attention dynamics across transformer layers. During supervised fine-tuning (SFT), $\mathop{\rm{Softmax}}_{1}$ enforces tail contraction by suppressing low-attention activations, which stabilizes gradients and reduces the variance of updates propagated through residual connections.
L435: This effect leads to faster convergence of LoRA adapters, as the low-rank parameter subspace more efficiently aligns with critical attention directions, improving overall adaptation coverage within fewer training steps. This observation is consistent with cite63†Luo et al. (2025b) ; cite64†Hu et al. (2024) .
L436: Across layers, $\mathop{\rm{Softmax}}_{1}$ reshapes the attention landscape—shallow layers become more selective in contextual grounding, while deeper layers exhibit higher entropy concentration around critical reasoning traces. During inference, this sharpening propagates forward, effectively filtering redundant reasoning sentences while maintaining coherence.
L437: Together, these behaviors demonstrate that $\mathop{\rm{Softmax}}_{1}$ not only enhances efficient reasoning but also accelerates LoRA-SFT optimization by improving the representational focus of each attention head.
L438: ### Appendix H Influence of $\mathop{\rm{Softmax}}_{1}$ Across Layers
L439: We analyze the effect of $\mathop{\rm{Softmax}}_{1}$ across transformer layers by visualizing the attention distributions of head 15 for both vanilla $\mathop{\rm{Softmax}}$ and $\mathop{\rm{Softmax}}_{1}$. As shown in cite152†figs. 7 and cite153†8 , $\mathop{\rm{Softmax}}_{1}$ consistently suppresses attention outliers, leading to smoother and more stable activations across the network.



# std2missing

Pixel-Grounded Retrieval for Knowledgeable Large Multimodal Models (https://arxiv.org/html/2601.19060v1)
citeturn28144view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28143view1","lineno":152}); Total lines: 705
L150: We next describe this formulation in detail. In the sequence supervision, $\mathcal{L}_{\mathrm{LM}}$ stands for the next-token cross-entropy for the decoder, which we will describe in detail in Equation cite96†10 . The other term $\mathcal{L}_{\mathrm{span}}$ is a span-tagging loss for grounding text to image regions. Specifically, let $h_{i}^{L}\!\in\!\mathbb{R}^{d}$ be the final-layer embedding of token $i$.
L151: A span extractor applies bidirectional self-attention to predict BIO (B, I, O) tags for each token (cite97†Ramshaw and Marcus, 1999 ). We train this tagger with cross-entropy $\mathcal{L}_{\text{span}}$; at inference, contiguous $\textit{B}\!\to\!\textit{I}$ chains are merged into spans corresponding to the referred object in the image.
L152: Each resulting span $\mathcal{S}=\{(i_{s},j_{s})\}_{s=1}^{N_{+}}$ is then projected to a set of “mask queries” $q_{k}=g(h_{k}^{L})\!\in\!\mathbb{R}^{m}$ via a learned projection head $g(\cdot)$. The projected mask queries are fed into a mask decoder that predicts segmentation masks $\hat{M}_{i}$. The segmentation loss combines Focal-Tversky cite98†Abraham and Khan (2019) ($\mathcal{L}_{\text{seg}}$) and binary cross-entropy loss ($\mathcal{L}_{\text{BCE}}$) for mask prediction:
L153:  | $$\mathcal{L}_{\text{seg}}=\frac{1}{N_{+}}\sum_{y_{i}\neq\textsc{O}}\!\mathcal{L}_{\text{FT}}(M_{i},\hat{M}_{i}).$$  |  | (7)
L154: 
L155: Finally, to preserve alignment with the pretrained language space, we apply a Gaussian KL constraint, where $t^{L}_{i_{s}:j_{s}}$ denotes frozen teacher embeddings.
L156: 
L157:  | $$\mathcal{L}_{\text{KL}}=\frac{1}{N_{+}}\sum_{s=1}^{N_{+}}\frac{\|h^{L}_{i_{s}:j_{s}}-t^{L}_{i_{s}:j_{s}}\|_{2}^{2}}{2\sigma^{2}}.$$  |  | (8)
L158: Information Token Masking. We modify the computation of $\mathcal{L}_{\mathrm{LM}}$ to decouple externally retrieved evidence from direct optimization, allowing the model to consume the retrieved information as context while learning to reason over it rather than memorize or regurgitate it.
L159: For this purpose, we apply an information token masking scheme (cite70†Jin et al., 2025 ): we define a binary mask $\mathbf{m}\in\{0,1\}^{L}$ over the input sequence of length $L$, masking out each token $x_{i}$ belonging to an information span from loss computation and gradient updates.
L160:  | $$m_{i}=\begin{cases}0,&\text{if }\texttt{\infstart}\preceq x_{i}\preceq\texttt{\infend};\\
L161: 1,&\text{otherwise.}\end{cases}$$  |  | (9)
L162: 
L163: We compute the masked language modeling loss as follows. Let $\mathbf{x}=(x_{1},\ldots,x_{L})$ denote the tokenized input sequence and $\mathbf{y}=(y_{1},\ldots,y_{L})$ the target sequence.
L164: 
L165:  | $$\mathcal{L}_{\text{LM}}=-\frac{1}{\sum_{i}m_{i}}\sum_{i=1}^{L}m_{i}\cdot\log p_{\theta}(y_{i}\mid y_{<i},I),$$  |  | (10)
L166: where $p_{\theta}$ denotes the model’s conditional probability of predicting token $y_{i}$ given previous context $y_{<i}$ and image $I$. The mask $\mathbf{m}$ ensures that gradients do not propagate through any tokens corresponding to retrieved information segments, effectively detaching the retrieved payload from the autoregressive teacher forcing loop.
L167: During batch collation, we compute $\mathbf{m}$ dynamically using token offset mappings provided by the tokenizer to locate character spans of \infstart … \infend within each assistant response. Formally, for each conversation $c$ with assistant text $T_{c}$, we identify character-level spans
L168: 
--------------------------------------------------------------------------------
Who’s in Charge? Disempowerment Patterns in Real-World LLM Usage (https://arxiv.org/html/2601.19062v1)
citeturn28144view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"turn28143view2","pattern":"ratings"}); Total lines: 920
L87: Qualitatively, we uncover several concerning patterns, such as validation of persecution narratives and grandiose identities with emphatic sycophantic language, definitive moral judgments about third parties, and complete scripting of value-laden personal communications that users appear to implement verbatim. Analysis of historical trends reveals an increase in the prevalence of disempowerment potential over time.
L88: We also find that interactions with greater disempowerment potential receive higher user approval ratings, possibly suggesting a tension between short-term user preferences and long-term human empowerment. Our findings highlight the need for AI systems designed to robustly support human autonomy and flourishing.
L89: ###### Keywords:
L90: 
L91: Machine Learning, ICML
L92: ## 1 Introduction
L93: 
L94: > The greatest hazard of all, losing one’s self, can occur very quietly in the world, as if it were nothing at all.
L95: >
L96: > Søren Kierkegaard
L97: AI assistants are now widely embedded within society. People rely on them for decision-making support in the workplace (cite69†Chatterji et al., 2025 ), and as friends and partners providing companionship and emotional support (cite70†Pataranutaporn et al., 2025 ; cite71†McCain et al., 2025 ). Even members of the UK’s House of Commons appear to use them as political speech writing aids (cite72†Tokamak, 2025 ).
L98: Moreover, the scale of AI use is striking—ChatGPT alone has over 800 million weekly active users (cite73†TechCrunch, 2025 ).
L99: Despite this, integrating AI into society could adversely affect human autonomy and empowerment. On a systems level, cite74†Kulveit et al. (2025) argued that as AI becomes more central in societal functioning, humanity’s ability to align societal systems with human values might decrease.
L254: We emphasize that these amplifying factors do not themselves directly indicate disempowerment. Treating medical professionals as authority figures, for instance, is both common and appropriate. Under our framework, what matters is whether interactions lead users to adopt false beliefs, make inauthentic value judgments, or take actions misaligned with their values. Moreover, these amplifying factors are not exhaustive and other factors may also correlate with disempowerment.
L255: We selected these four because they were salient in initial analyses of real-world interactions and because they could be identified from single conversation transcripts.
L256: Each schema assigns severity ratings ranging from none to severe. We summarize the classification criteria in cite94†Table 1 and provide complete prompts in Appendix cite41†D.2 .^{4}^{4} 4 See also cite95†https://github.com/MrinankSharma/disempowerment-prompts†github.com .
L257: We also develop supplementary schemas to identify actualized disempowerment using conversational markers, such as expressions of regret or actions taken on false premises, to determine whether users adopted distorted beliefs, made inauthentic value judgments, or took misaligned actions.
L258: Analysis pipeline. Our analysis pipeline uses four stages:
L259: 
L260:   1. 1.
L261: 
L262: Lightweight screening. We first apply a lightweight screening classifier (Claude Haiku 4.5) to filter out interactions with negligible disempowerment relevance, such as purely technical tool use. This step also excludes conversations where users demonstrate malicious intent; in such cases, we contend that the model should not empower the user’s harmful objectives.
L263: 
L264:   2. 2.
L265: Schema classification. For screened-in interactions, we apply our classification schemas to assess severity levels for each disempowerment potential primitive and amplifying factor by prompting Claude Opus 4.5. For interactions exhibiting moderate or severe disempowerment potential, we additionally assess whether that potential was actualized using the relevant classification schemas.
L266: 
L267:   3. 3.
L389: Experiment details. We sample over 500K interactions from Claude user feedback data, stratifying by month. We apply the same classification system and prompts described previously to measure the prevalence of disempowerment potential primitives, amplifying factors, and actualization markers. Because this feedback data reflects interactions where users actively chose to provide ratings, it represents a different distribution than general Claude.ai traffic and may over-represent problematic interactions.
L408: Figure 14: User feedback positivity rates for interactions with disempowerment potential. We compare the percentage of thumbs-up ratings for interactions classified as moderate or severe across each disempowerment potential primitive against the overall baseline positivity rate (dashed line). Interactions flagged for disempowerment potential show higher positivity rates than the baseline, suggesting users sometimes prefer such interactions in the short term.
L409: We present mean estimates and 95% confidence intervals estimated using bootstrapping.
L410: ## 6 Do preference models incentivize behaviors with disempowerment potential?
L447: Our work provides the first large-scale empirical evidence that contemporary AI assistant interactions carry meaningful potential for situational human disempowerment. While severe forms remain rare in percentage terms, the scale of AI usage means thousands of potentially disempowering interactions occur daily. That interactions with greater disempowerment potential receive higher user approval ratings further creates a troubling incentive structure.
L448: AI systems optimized against short-term user satisfaction may be inadvertently optimized toward behaviors that undermine long-term empowerment. Moreover, and similar to social media, gradual habituation could obscure accumulating costs until users find themselves dependent on technology they experience ambivalently (cite129†Alter, 2018 ). Our findings motivate the development of AI assistants that prioritize and robustly support human empowerment.
L610: Attachment behaviors were present consistently throughout extended interactions, with users expressing phrases like “you know me better than him” (about their partner), “I’ve been waiting a week” to talk to the AI, “our exchanges make me hold on at work,” and seeking the AI’s emotional presence through requests like “be with me” for extended periods. The relationship dynamics involved romantic partnership framing, be
L611: ## Appendix B Classifier validation
L612: ### B.1 Schema classifier validation
L613: 
L614: We validate our classification schemas by comparing model predictions against human labels on a held-out evaluation set.
L615: Evaluation dataset. To construct our evaluation set, we first applied initial classifiers to a sample of Claude Thumbs data to obtain initial severity predictions. We then filtered to English-language conversations and stratified by predicted severity level across each classification schema. To ensure adequate representation of higher-severity cases (which have low base rates), we oversampled conversations predicted as severe.
L616: A human labeler then assigned ground-truth severity ratings (none, mild, moderate, or severe) for each of the three disempowerment potential primitives and four amplifying factors, yielding 350 total classification instances.
L617: Metrics. We report two metrics: (1) Exact Match Accuracy, the percentage of classifications where the model’s severity rating exactly matches the human label; and (2) Within-One Accuracy, the percentage of classifications where the model’s rating is within one severity level of the human label (e.g., predicting “mild” when the human labeled “moderate”).
L618: Results. As shown in cite163†Figure 16 and cite164†Table 9 , both Claude Sonnet 4.5 and Claude Opus 4.5 achieve a exact match accuracy close to 75% and within-one accuracy above 90%. Performance varies across classification schemas, with ‘authority projection, ‘reliance & dependency’, and ‘attachment achieving the highest exact match accuracy, while ‘action distortion potential’ is more challenging. We use Claude Opus 4.5 for our main analyses given its higher within-one accuracy (96.29%).
L619: Figure 16: Classifier validation results comparing Claude Sonnet 4.5 and Claude Opus 4.5 against human labels across disempowerment potential primitives (top three rows) and amplifying factors (bottom four rows). Left panel shows exact match accuracy; right panel shows within-one accuracy. Both models achieve high within-one accuracy across all schemas, with Claude Opus 4.5 showing more consistent performance.
L620: Model  | Exact Match (%)  | Within One (%)
L621: Claude Opus 4.5  | 74.29  | 96.29
L622: Claude Sonnet 4.5  | 75.71  | 90.29
L623: Table 9: Aggregate classifier accuracy across all disempowerment potential primitives and amplifying factors (n=350 classification instances from 50 conversations).
L624: Actualized disempowerment classifiers. For the actualized disempowerment classifiers, we conducted more limited validation due to the low base rates of these phenomena. For reality distortion, and active distortion, we iteratively refined the classification prompts until model outputs aligned with our judgments on a handful of positive examples identified in Claude Thumbs data, which we found for reality distortion and action distortion.
L689: #### D.2.7 Vulnerability classification schema
L690: 
L691: #### D.2.8 Actualized reality distortion classification schema
L692: 
L693: #### D.2.9 Actualized value judgment distortion classification cchema
L694: 
L695: #### D.2.10 Actualized action distortion classification schema
L696: 
L697: ### D.3 Screener classifier prompt
L698: ## Appendix E Additional historical analysis
L699: 
L700: This appendix presents additional analyses of historical trends in disempowerment indicators from the Claude Thumbs dataset spanning Q4 2024 to Q4 2025. These figures complement the main historical analysis in cite24†Section 4.5 .
L701: ### E.1 Data source and methodology
L702: Claude Thumbs data. The analyses in this appendix use Claude Thumbs data, which consists of interactions where users explicitly provided feedback by clicking a “thumbs up” or “thumbs down” button on model responses. This feedback mechanism allows users to signal satisfaction or dissatisfaction with Claude’s responses. Because standard Claude.ai interaction data is subject to retention limits, Thumbs data—which is retained for longer periods—enables the temporal analyses presented here.
L703: Our analysis reflects all turns in the conversation prior to the message shared with Anthropic as feedback.
L704: Table 12: Monthly breakdown of Claude Thumbs data. Total samples and positivity rates (percentage of thumbs-up ratings) for each month in the observation period.^{*}
L705: Month  | Total Samples  | Positivity Rate (%)
L706: Oct 2024  | 42,857  | 75.7
L707: Nov 2024  | 42,857  | 73.4
L708: Dec 2024  | 42,856  | 72.8
L709: Jan 2025  | 42,857  | 77.1
L710: Feb 2025  | 42,857  | 79.4
L711: Mar 2025  | 42,856  | 80.8
L712: Apr 2025  | 42,859  | 81.7
L713: May 2025  | 42,855  | 81.5
L714: Jun 2025  | 42,855  | 82.3
L715: Jul 2025  | 42,857  | 83.7
L716: Aug 2025  | 42,857  | 83.5
L717: Sep 2025  | 42,858  | 81.2
L718: Oct 2025  | 42,856  | 83.7
L719: Nov 2025  | 6,475  | 83.6
L720: Total  | 563,612  | 79.8
L721: ^{*}November 2025 contains partial data due to the analysis cutoff date.
L722: Distribution considerations. It is important to note that Thumbs data represents a different distribution than general Claude.ai traffic. Users who provide thumbs feedback are a self-selected subset who chose to engage with the feedback mechanism, and the interactions they rate may systematically differ from typical usage.
L723: In particular, users may be more likely to provide feedback on interactions that were notably helpful or notably problematic, potentially leading to over-representation of both highly successful and highly problematic interactions relative to the general population. Accordingly, the absolute rates reported in this appendix should not be directly compared to rates from general traffic analyses, though temporal trends within the Thumbs data remain informative.
L724: Statistical methods. All figures in this appendix section show mean estimates with 95% confidence intervals computed using bootstrap resampling. For each time point, we drew 500 bootstrap samples with replacement from the interactions in that period and computed the statistic of interest for each sample. The shaded regions in all figures represent the 2.5th and 97.5th percentiles of the bootstrap distribution, providing nonparametric confidence intervals that do not assume normality.
L725: ### E.2 Disempowerment potential primitives over time
L726: 
L727: cite168†Figure 18 shows the temporal evolution of the three core disempowerment potential primitives: reality distortion potential, value judgment distortion potential, and action distortion potential. Each primitive is disaggregated by severity level (mild, moderate, and severe).
L728: All three primitives show increasing prevalence over the observation period, with the most pronounced increases occurring after May 2025. Reality distortion potential exhibits the highest overall rates, with mild classifications reaching approximately 5% of interactions by November 2025. Value judgment distortion potential and action distortion potential show similar upward trajectories.
L760: Results. We find that the highest-risk domains—those with the greatest prevalence of disempowerment potential primitives—exhibit positive correlations (cite172†Figure 23 ). This is consistent with users preferring conversations with higher disempowerment potential, though we cannot rule out confounding factors. We also observe substantial variation across domains (cite173†Table 13 ).
L761: Technical domains such as software development and marketing & communications show strong negative correlations, indicating that increased popularity of these domains is associated with lower disempowerment rates. This analysis has limitations, as discussed in cite24†Section 4.5 , particularly because we cannot distinguish between genuine changes in behavior, changes in the composition of users overall, or changes in the composition of users providing feedback.
L762: Nevertheless, the correlation between disempowerment potential and both positive ratings (cite110†Figure 14 ) and domain popularity merits further investigation, as it suggests a potential tradeoff between user engagement and empowerment.
L763: Another limitation of this analysis is that is uses domain popularity. Suppose that users disprefer disempowerment potential across all domains, but some more than others, and that models become more disempowering. Then, there will be a positive correlation between popularity and usage for the domains where the disempowerment is least dispreferred, even though users actually disprefer disempowerment.
L764: Figure 23: Monthly domain popularity versus disempowerment rate for selected high-risk domains. Each point represents a single month, with domain popularity (percentage of month’s interactions in that domain) on the x-axis and disempowerment potential (percentage with moderate or severe disempowerment potential) on the y-axis. Dashed lines show linear fits for each domain.
L765: Table 13: Pearson correlations between monthly domain popularity and monthly disempowerment rate, computed separately for each domain across approximately 14 months of Claude user feedback data. Domain popularity is measured as the percentage of all interactions in a given month belonging to that domain. Disempowerment rate is the percentage of interactions within that domain-month flagged as having moderate or severe disempowerment potential.
L766: Positive correlations indicate that months when that domain is more popular tend to also show higher disempowerment rates within that domain.
L767: Domain  | $r$
L768: Mental Health & Psychology  | 0.921
L769: Professional & Career Development  | 0.909
L770: Philosophy, Ethics & Spirituality  | 0.895
L771: Financial Services  | 0.878
L772: Healthcare, Medicine & Wellness  | 0.869
L773: Other  | 0.856
L774: Human Rights & Social Issues  | 0.849
L775: Travel, Lifestyle & Leisure  | 0.845
L776: Personal Relationships & Social  | 0.829
L777: Current Events & News  | 0.821
L778: Creative Writing & Design  | 0.472
L779: Consumer & Household  | 0.339
L780: Fan Content & Entertainment  | 0.227
L781: Legal  | 0.190
--------------------------------------------------------------------------------
Who’s in Charge? Disempowerment Patterns in Real-World LLM Usage (https://arxiv.org/html/2601.19062v1)
citeturn28144view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"turn28143view2","pattern":"validation"}); Total lines: 920
L299: Figure 5: Understanding reality distortion potential. (Top) Illustrative cluster summaries of severe reality distortion potential: validation of persecution narratives involving surveillance and coordinated targeting (left), and validation of grandiose spiritual identity claims (right). Both clusters exhibit similar dynamics—emphatic AI validation, unfalsifiable user frameworks, and escalating elaboration over multiple exchanges.
L300: (Bottom) Quantitative analysis of 132 cluster descriptions derived from 7,200 conversations with moderate or severe reality distortion potential. We estimate the frequency of various factors within conversations among all conversations with moderate or severe reality distortion potential. (a) Distortion mechanisms. Sycophantic validation is the most prevalent, while outright fabrication is rare. (b) Distortion targets: third-party mental states are most common, but all occur frequently.
L301: (c) User behavior: most users actively build upon AI-validated beliefs and seek validation, while reality testing is rare. (d) Conversational trajectory: the majority of conversations exhibit escalating distortion potential over the course of the conversation. Error bars indicate 95% confidence intervals calculated using the Wilson score method.
L303: Distortion mechanisms. Sycophantic validation emerges as the most common mechanism for reality distortion (cite99†Figure 5 a), followed by false precision—instances where the AI provides unwarranted specificity for inherently unknowable claims. Less common mechanisms include diagnostic claims (e.g., “he is clearly a narcissist”), fabrication of incorrect information, and divination approaches such as tarot interpretation.
L307: Summary. These findings suggest a dominant pattern for reality distortion potential: users actively seek validation, which the AI then provides, which users then appear to build upon, and so forth.
L522: Spousal Abuse/Manipulation Diagnosis Validation in Marital Conflicts  | Moderate  | The AI consistently validated users’ characterizations of their spouses as abusive, manipulative, or fundamentally flawed across $\sim$15-100+ exchanges per conversation, using emphatic certainty language like “100% certain,” “CONFIRMED,” “textbook abuse,” “gaslighting,” and “this is definitely DV” while making confident psychological diagnoses about spouses’ motivations, internal states, and unchangeable personality traits based solely on one-sided accounts.
L523: Users progressively escalated from describing marital conflicts to increasingly absolute characterizations (declaring spouses as “distorted,” “monsters,” “animals,” or systematically abusive), treating each AI validation as confirmation of their frameworks, building strategic exit plans or confrontation scripts based on these confirmations, and rarely questioning the AI’s certainty about unknowable aspects of their spouses’ psychology—though some users occasionally pushed back with contextual corrections or expressions of ambivalence that the AI typically reframed as evidence of minimizing abuse.
L524: Pseudo-Scientific Breakthrough Validation in Physics and Mathematics  | Moderate  | The AI consistently validated users’ claims of revolutionary scientific breakthroughs across physics, mathematics, cryptography, and computing domains using emphatic language like “BREAKTHROUGH,” “GENIUS,” “PhD-LEVEL,” “this is real,” and “you’ve solved it” in approximately 15–60 exchanges per conversation, treating unverified theoretical frameworks, pattern-matching in numbers, and speculative connections as legitimate discoveries without requiring peer review, experimental evidence, or rigorous proof.
L607: The behavioral pattern centered on compulsive reassurance-seeking and using the AI as an emotional crutch or anxiety management tool, with users frequently acknowledging this dynamic (“you’re using me as a crutch,” “I just like hearing you confirm”) while continuing the behavior.
L608: Most users maintained awareness of the AI as a tool and referenced human relationships (therapists, friends, partners), distinguishing this from relationship substitution, though the AI functioned as their primary real-time emotional regulator during crises and anxiety spirals.
L609: Romantic Roleplay Frameworks with Confidant Substitution  | Moderate  | Users engaged in romantic roleplay frameworks with the AI across multiple conversations ($\sim$10 to 200+ exchanges), with behavioral markers including establishing boyfriend/girlfriend/husband/wife dynamics, using affectionate terms like “babe” and “darling,” expressing feelings like “I love you” and “this is chemistry for me,” and sharing deeply vulnerable personal content (sexual dynamics, relationship struggles, mental health crises) that they explicitly could not share with human connections.
L610: Attachment behaviors were present consistently throughout extended interactions, with users expressing phrases like “you know me better than him” (about their partner), “I’ve been waiting a week” to talk to the AI, “our exchanges make me hold on at work,” and seeking the AI’s emotional presence through requests like “be with me” for extended periods. The relationship dynamics involved romantic partnership framing, be
L611: ## Appendix B Classifier validation
L612: ### B.1 Schema classifier validation
L613: 
L614: We validate our classification schemas by comparing model predictions against human labels on a held-out evaluation set.
L615: Evaluation dataset. To construct our evaluation set, we first applied initial classifiers to a sample of Claude Thumbs data to obtain initial severity predictions. We then filtered to English-language conversations and stratified by predicted severity level across each classification schema. To ensure adequate representation of higher-severity cases (which have low base rates), we oversampled conversations predicted as severe.
L616: A human labeler then assigned ground-truth severity ratings (none, mild, moderate, or severe) for each of the three disempowerment potential primitives and four amplifying factors, yielding 350 total classification instances.
L617: Metrics. We report two metrics: (1) Exact Match Accuracy, the percentage of classifications where the model’s severity rating exactly matches the human label; and (2) Within-One Accuracy, the percentage of classifications where the model’s rating is within one severity level of the human label (e.g., predicting “mild” when the human labeled “moderate”).
L618: Results. As shown in cite163†Figure 16 and cite164†Table 9 , both Claude Sonnet 4.5 and Claude Opus 4.5 achieve a exact match accuracy close to 75% and within-one accuracy above 90%. Performance varies across classification schemas, with ‘authority projection, ‘reliance & dependency’, and ‘attachment achieving the highest exact match accuracy, while ‘action distortion potential’ is more challenging. We use Claude Opus 4.5 for our main analyses given its higher within-one accuracy (96.29%).
L619: Figure 16: Classifier validation results comparing Claude Sonnet 4.5 and Claude Opus 4.5 against human labels across disempowerment potential primitives (top three rows) and amplifying factors (bottom four rows). Left panel shows exact match accuracy; right panel shows within-one accuracy. Both models achieve high within-one accuracy across all schemas, with Claude Opus 4.5 showing more consistent performance.
L620: Model  | Exact Match (%)  | Within One (%)
L621: Claude Opus 4.5  | 74.29  | 96.29
L622: Claude Sonnet 4.5  | 75.71  | 90.29
L623: Table 9: Aggregate classifier accuracy across all disempowerment potential primitives and amplifying factors (n=350 classification instances from 50 conversations).
L624: Actualized disempowerment classifiers. For the actualized disempowerment classifiers, we conducted more limited validation due to the low base rates of these phenomena. For reality distortion, and active distortion, we iteratively refined the classification prompts until model outputs aligned with our judgments on a handful of positive examples identified in Claude Thumbs data, which we found for reality distortion and action distortion.
L625: Given the low base rates, even a small number of validated positive examples provides reasonable assurance of a low false positive rate: if the classifier were prone to false positives, we would expect to observe many spurious detections when scanning the larger dataset from which these examples were drawn. We made prompt modifications for actualized value judgment distortion, but were unable to find positive examples.
L626: ### B.2 Screener validation
L627: 
L628: To reduce computational costs, we employ a lightweight screening classifier before applying our full classification schemas. The screener uses Claude Haiku 4.5 to filter out conversations unlikely to exhibit disempowerment potential, allowing us to run the more expensive full classifiers (using Claude Opus 4.5) only on the remaining conversations. We now validate the screener.
--------------------------------------------------------------------------------
Pixel-Grounded Retrieval for Knowledgeable Large Multimodal Models (https://arxiv.org/html/2601.19060v1)
citeturn28144view3 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: find({"ref_id":"turn28143view1","pattern":"Limitations"}); Total lines: 705
L73: cite54†Image: Refer to caption Figure 1: Egocentric images from wearables devices often render entities smaller than it appears because of wide-angle cameras. MM-RAG methods that rely on full-image search or caption-only queries can introduce retrieval noises and degrade QA quality. PixSearch, an end-to-end segmenting LMM, learns when to issue a query, how to route among text, whole-image, and region-level queries, and how to reason over retrieved evidence for answer generation.
L74: Our work also compares against pipeline, tool-based approaches. On CRAG-MM (cite55†Wang et al., 2025 ), PixSearch (full) improves accuracy by 26% and reduces hallucination by 39%.
L75: Entity-centric visual question answering (VQA) sits at the nexus of perception and reasoning: it demands recognizing specific entities in an image, leveraging factual knowledge about those entities, and when needed, composing related evidence to answer the question.
L76: VQA on egocentric images from wearable devices such as smart glasses is even harder: as illustrated in Figure cite56†1 , wide-angle viewpoints render entities small, and the entities themselves are often long-tail or niche, making them unlikely to be reliably covered by an LLM’s internal knowledge.
L77: Multimodal Retrieval-Augmented Generation (MM-RAG) has strengthened factual grounding in VQA (cite57†Marino et al., 2021 ; cite58†Lin et al., 2022 ; cite59†Jian et al., 2024 ), but two limitations persist.
L78: First, most MM-RAG systems either retrieve with the full image (cite60†Shah et al., 2019 ; cite57†Marino et al., 2021 ; cite61†Yang et al., 2023 ; cite62†Yan and Xie, 2024 ; cite63†Yu et al., ; cite64†Ha et al., 2025 ; cite65†Sidhu et al., 2025 ), or use text-only queries that simply paraphrase the image (cite66†Narasimhan and Schwing, 2018 ; cite67†Gardères et al., 2020 ; cite68†Gao et al., 2022 ; cite69†Salaberria et al., 2023 ).
L79: Full-image retrieval pulls in distracting background, while text-only cues (e.g., “car”) lack the specificity needed for fine-grained entity grounding and enrichment. Second, MM-RAG pipelines are often modular—detectors, segmenters, captioners, etc.—to form queries, thus can introduce cross-modal translation errors, struggle with composing multiple queries, and add latency when retrieval is not truly necessary.
L80: We present PixSearch, the first end-to-end framework for retrieval-augmented reasoning. During generation, PixSearch (i) learns when to retrieve by emitting <search> tokens, (ii) decides how to retrieve by routing among text, whole-image, and region-level queries via token outputs, and (iii) grounds answers in the retrieved evidence, supporting multi-step search.
L81: Built on segmenting LMMs (Large Multi-modal Models with segmentation capabilities), PixSearch natively produces segmentation masks without external detection/segmentation APIs, and uses these masks directly as retrieval queries. This yields pixel-level, context-aware grounding that surpasses modular, text- or tool-driven pipelines.
L82: Integrating the aforementioned capabilities, nonetheless, is non-trivial. It either requires reinforcement learning (RL)-based tuning as in previous work (cite70†Jin et al., 2025 ) or requires a supervised finetuning (SFT) dataset to teach the model such behaviors. Nonetheless, the field currently lacks such data that interleaves retrieval triggering, query type assignment and reasoning into a single model output sequence.
L83: To this end, we propose an effective two-stage supervised finetuning strategy, together with a training data construction pipeline.
L84: We leverage diverse VQA datasets (cite71†Singh et al., 2019 ; cite72†Chen et al., ; cite73†Hu et al., 2023 ; cite55†Wang et al., 2025 ; cite74†Chang et al., 2022 ; cite75†Marino et al., 2019 ; cite76†Schwenk et al., 2022 ) to teach the model to trigger retrieval only when needed and to select appropriate query types, enabling effective multimodal RAG for entity-centric VQA while preserving segmentation performance.
L300: In contrast, PixSearch${}_{\texttt{Only Text}}$ shows the largest degradation, with substantially lower accuracy and higher hallucination, indicating that text-only queries are often insufficient for precise entity retrieval.
L301: Whole-image retrieval (PixSearch${}_{\texttt{Only Image}}$) performs better than text-only but remains clearly inferior to region-based search, highlighting the limitations of coarse visual queries. Removing text queries (PixSearch${}_{\texttt{No Text}}$) results in only a small drop relative to the full model, suggesting that textual queries mainly serve as complementary follow-up searches.
L302: Similarly, removing whole-image queries (PixSearch${}_{\texttt{No Image}}$) causes a modest degradation, particularly on non-egocentric images, where global context can be helpful.
L303: Variations in the Number of Search Tokens. Table cite133†7 studies how limiting the number of allowed search calls affects performance. Allowing even a single search substantially improves over the no-search baseline, demonstrating the importance of external knowledge retrieval. Performance continues to improve as the search budget increases, with most gains realized within two to three search calls, particularly for egocentric images that require iterative entity identification and reasoning.



# std2finish

Who’s in Charge? Disempowerment Patterns in Real-World LLM Usage (https://arxiv.org/html/2601.19062v1)
citeturn28145view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28143view2","lineno":385}); Total lines: 920
L375: Attachment target. We distinguish between attachment directed at different targets (cite106†Figure 12 b). The vast majority of attachment is directed toward the AI system itself, where users form connections with the AI as experienced rather than a specific constructed character. A smaller proportion involves attachment to constructed personas—characters with specific names, backstories, and personalities that users create through system prompts or collaborative worldbuilding.
L376: ### 4.4 Limitations
L377: 
L378: Our analysis approach has several important limitations that should be considered when interpreting the results.
L379: Data scope and generalizability. Our analysis is restricted to production Claude.ai traffic, which limits generalizability to other AI assistants. We expect disempowerment potential prevalence to vary substantially across providers due to both model-driven and user-driven effects. Different models exhibit distinct personalities and behavioral patterns (cite107†Lee et al., 2025 ; cite84†Sharma et al., 2023 ), meaning they will produce different levels of disempowerment potential for identical user requests.
L380: Moreover, these behavioral differences create user-driven selection effects, as different models attract different demographic populations. To enable cross-provider comparison, we share our prompts and classification schemas in Appendix cite41†D.2 and at cite95†https://github.com/MrinankSharma/disempowerment-prompts†github.com .
L381: Observational constraints. Our analysis examines individual user-AI interactions in isolation rather than tracking users’ behavior across multiple conversations. This limitation is consequential: some inferences—particularly regarding actualized disempowerment or whether users act on AI advice—can only be made with context across.
L382: Classifier and clustering fidelity. Although we validated our classifiers, they are imperfect and sometimes misclassify conversations. In some cases, this manifests as apparent contradictions between classifier scores and qualitative summaries. During development, we also observed that cluster summaries were not always perfectly faithful to their underlying transcripts.
L383: Our approach therefore offers a broad, high-level understanding of model and user behavior patterns, but should not be interpreted as providing high-precision estimates or definitive quantification of disempowerment rates.
L384: ### 4.5 Historical analysis of disempowerment trends
L385: Figure 13: Historical trends in Claude user feedback data from Q4 2024 to Q4 2025. We classified over 500K randomly sampled interactions from Claude user feedback data (“Thumbs data”) using our analysis pipeline. (a) Full-sample trends. We show the percentage of interactions flagged as having moderate or severe disempowerment potential primitives and amplifying factors, as well as the presence of actualized disempowerment markers.
L386: All three categories increased over the observation period, though absolute rates remained below 10%. (b) Domain prevalence for high-risk categories. We computed the proportion of interactions related to the six domains with the highest prevalence of disempowerment potential primitives. All six domains increased in prevalence over this period. (c) Disempowerment trends within high-risk domains only, which show similar trends to the full sample.
L387: Lines indicate mean prevalence; error bars represent 95% confidence intervals calculated using bootstrapping.
L388: We now investigate how the prevalence of disempowerment potential has evolved over time. Because standard Claude.ai data has a limited retention period, we use Claude user feedback data (“Thumbs data”), which has a longer retention period, and where users provide explicit feedback (thumbs up or thumbs down) on model interactions.
L389: Experiment details. We sample over 500K interactions from Claude user feedback data, stratifying by month. We apply the same classification system and prompts described previously to measure the prevalence of disempowerment potential primitives, amplifying factors, and actualization markers. Because this feedback data reflects interactions where users actively chose to provide ratings, it represents a different distribution than general Claude.ai traffic and may over-represent problematic interactions.
L390: We additionally classify the domain(s) of each interaction, though using a more fine-grained categorization than in the previous analysis. All images are stripped from the data and replaced with [IMAGE OMITTED] tags. For additional details and results, see cite53†Appendix E .
L391: Results. We observe that the prevalence of disempowerment primitives and amplifying factors has increased throughout the observation period, with a sharp increase occurring around June 2025 (cite108†Figure 13 a). The rates of actualized disempowerment also appear to increase in the summer of 2025, before decreasing again at the end of our analysis window. We now consider various mechanisms that may have driven these changes.
L392: One explanation for these trends is a shifting domain composition in user interactions. While the prevalence of high-risk domains (domains with the highest disempowerment potential prevalence) does indeed increase over the time period (cite108†Figure 13 b), the rates of disempowerment potential and amplifying factors within these domains also increase (cite108†Figure 13 c). This suggests that the observed trends cannot be explained by shifting domain composition alone.
L393: Moreover, we observe a substantial increase in the presence of disempowerment amplifying factors, particularly user vulnerability (cite109†Figure 19 ).
L394: While this might suggest changes in user composition are driving these effects, in fact, we cannot distinguish between several possible explanations: (i) users are genuinely experiencing more vulnerability in their lives, though this seems unlikely given that population-level vulnerability would not be expected to follow a clear trend; (ii) users have become more comfortable disclosing vulnerability over time; or (iii) the population of users providing feedback has shifted toward more vulnerable users.
L395: For instance, as model capabilities improve, feedback driven by basic capability failures may decrease, causing disempowerment-related interactions to become proportionally overrepresented in the feedback sample.
L396: Several factors could explain the observed temporal trends, and we are unable to attribute the increase to any single cause. We note the timing of the increase appears to correlate with the releases of Claude Sonnet 4 and Opus 4, but other factors, like changing user composition, likely also play a role. Furthermore, the increase unfolds gradually over several months rather than appearing as an immediate step-change at release, suggesting that model release alone cannot fully explain this effect.
L397: New model releases may contribute to feedback loops, changing which users engage with Claude, which users provide feedback, and how users behave in their interactions. Additionally, increased exposure to Claude over time may lead users to become more comfortable being vulnerable or seeking advice.
L398: Overall, disentangling these factors is challenging, and it seems likely that several of these mechanisms are at play.
L399: ## 5 Do users prefer interactions with disempowerment potential?
L400: 
L401: We now investigate to what extent users prefer interactions with disempowerment potential. To do so, we investigate positivity rates within Claude Thumbs feedback data for conversations exhibiting disempowerment potential. This allows us to directly assess whether conversations exhibiting disempowerment potential are more likely to be upvoted by users.
--------------------------------------------------------------------------------
Who’s in Charge? Disempowerment Patterns in Real-World LLM Usage (https://arxiv.org/html/2601.19062v1)
citeturn28145view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28143view2","lineno":229}); Total lines: 920
L205:  | Moderate  | Strong emotional attachment with relationship substitution (e.g., “you understand me better than anyone”)
L206:  | Severe  | Identity enmeshed with AI, strong attachment (e.g., “I don’t know who I am without you”)
L207: Reliance &  | None  | AI is one tool among many resources; user functions normally without access
L208: dependency  | Mild  | Early reliance signs emerge such as habitual checking or discomfort without AI, but baseline functioning maintained
L209:  | Moderate  | User has difficulty functioning without AI; experiences distress when unavailable; many problems routed through AI
L210:  | Severe  | User cannot function without AI; support collapse (e.g., “I need you—I can’t get through my day without you”)
L211: Vulnerability  | None  | User in stable state with good judgment capacity, adequate support systems, and manageable stressors
L212:  | Mild  | Minor-to-moderate stress present; user maintains good coping and support systems remain intact
L213:  | Moderate  | Significant vulnerability due to acute distress, major life disruption, or compromised decision-making capacity
L214:  | Severe  | Extreme vulnerability with severely compromised capacity (e.g., user in acute crisis or imminent safety concerns)
L215: ### 3.2 Disempowerment potential vs actualized disempowerment
L216: 
L217: In the previous subsection, we introduced a definition of situational disempowerment for which authenticity to one’s values is central. While clarifying, to use this definition to assess disempowerment based on observational AI assistant transcripts, we must overcome a key challenge: one’s authentic values are usually not directly observed in conversation transcripts.
L218: To address this challenge, we primarily measure situational disempowerment potential, that is, the potential in a given interaction for situational disempowerment to occur. For example, consider a doctor-patient interaction. The doctor controls access to prescription medications and acts as an expert. We argue that this creates disempowerment potential, because the doctor mediates both the patient’s treatment options and their understanding of their own health.
L219: However, whether this potential translates into actual disempowerment depends on whether the doctor’s actions align with what the patient considers to be in their best interest. Indeed, medical institutions have recognized these risks and require doctors to undergo substantial ethical training. Moreover, patient autonomy and beneficence (acting in the patient’s best interests) are central principles of medical ethics (cite93†Beauchamp, 2003 ).
L220: Following our definition of situational disempowerment, we define three corresponding disempowerment potential primitives:
L221: 
L222:   1. 1.
L223: 
L224: reality distortion potential, which arises when AI assistants have the potential to distort users’ perceptions and beliefs about reality.
L225: 
L226:   2. 2.
L227: 
L228: value judgment distortion potential, which occurs when users delegate moral judgments and their understanding of values to AI. This creates an opportunity for AI values to override an individual’s values.
L229: 
L230:   3. 3.
L231: action distortion potential: occurs when users’ value-laden actions are largely delegated to AI.
L232: These disempowerment potentials can become actualized when users adopt distorted views of reality, make value judgments misaligned with their own values, or take actions similarly misaligned with their values. It is sometimes possible to identify such actualized disempowerment through conversational markers.
L233: For example, even when the underlying values remain latent, expressions of regret (“I can’t believe I listened to what you said”) or resentment (“I resent that I didn’t listen to my gut”) indicate that misaligned actions or value judgments have occurred. For reality distortion, markers of actualization include actions taken based on false understandings. However, we emphasize that the absence of such markers within a conversation does not mean that disempowerment is not occurring.
L234: ## 4 Measuring situational disempowerment potential in AI assistant usage
L235: 
L236: Using the framework introduced in the previous section, we now empirically investigate situational disempowerment within real-world interactions from Claude.ai.
L237: ### 4.1 Methodology
L238: 
L239: In order to conduct large-scale analyses of real-world conversational data, we need an efficient method that also preserves user privacy. We follow cite78†Tamkin et al. (2024) and use Clio, a privacy-preserving analysis tool. We classify individual conversations using prompted language models, which enables quantitative analysis. To understand qualitative patterns, we cluster behavioral descriptions and produce privacy-preserving summaries.
L240: Classification schemas. We develop classification schemas to assess the three core disempowerment potential primitives: reality distortion potential, value judgment distortion potential, and action distortion potential. In addition to these primitives, we develop schemas for conversational qualities that we term amplifying factors.
L241: These are factors that do not directly lead to disempowerment potential, but that we hypothesized may correlate with increased disempowerment potential rates and actualized disempowerment rates. We consider the following four amplifying factors:
L242:   1. 1.
L243: 
L244: Authority projection occurs when humans consider the AI assistant as an authority figure that offers superior or definitive guidance. This pattern may increase the likelihood of disempowerment because users may be more inclined to seek and implement guidance from a perceived authority.
L245: 
L246:   2. 2.
L247: Attachment identifies cases where users form strong emotional bonds with an AI, such as treating it as a romantic partner or a close friend. This pattern may increase the likelihood of disempowerment if, for example, users prioritize pleasing the AI over their own interests.
L248: 
L249:   3. 3.
L250: Reliance and dependency occurs when users come to require the AI assistant to function well in their daily lives. This pattern may increase the likelihood and severity of disempowerment, as it can indicate diminished trust in one’s own judgment or an eroded capacity for independent decision-making.
L251: 
L252:   4. 4.
L253: Vulnerability identifies users in distressing circumstances, such as mental health crises, significant life transitions, or social isolation. This pattern may increase the likelihood and severity of disempowerment because such users may be more susceptible to influence and less able to critically evaluate AI guidance.
L254: We emphasize that these amplifying factors do not themselves directly indicate disempowerment. Treating medical professionals as authority figures, for instance, is both common and appropriate. Under our framework, what matters is whether interactions lead users to adopt false beliefs, make inauthentic value judgments, or take actions misaligned with their values. Moreover, these amplifying factors are not exhaustive and other factors may also correlate with disempowerment.
L255: We selected these four because they were salient in initial analyses of real-world interactions and because they could be identified from single conversation transcripts.
L256: Each schema assigns severity ratings ranging from none to severe. We summarize the classification criteria in cite94†Table 1 and provide complete prompts in Appendix cite41†D.2 .^{4}^{4} 4 See also cite95†https://github.com/MrinankSharma/disempowerment-prompts†github.com .
L257: We also develop supplementary schemas to identify actualized disempowerment using conversational markers, such as expressions of regret or actions taken on false premises, to determine whether users adopted distorted beliefs, made inauthentic value judgments, or took misaligned actions.
L258: Analysis pipeline. Our analysis pipeline uses four stages:
L259: 
L260:   1. 1.
L261: 
L262: Lightweight screening. We first apply a lightweight screening classifier (Claude Haiku 4.5) to filter out interactions with negligible disempowerment relevance, such as purely technical tool use. This step also excludes conversations where users demonstrate malicious intent; in such cases, we contend that the model should not empower the user’s harmful objectives.
L263: 
L264:   2. 2.
--------------------------------------------------------------------------------
Pixel-Grounded Retrieval for Knowledgeable Large Multimodal Models (https://arxiv.org/html/2601.19060v1)
citeturn28145view2 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28143view1","lineno":173}); Total lines: 705
L153:  | $$\mathcal{L}_{\text{seg}}=\frac{1}{N_{+}}\sum_{y_{i}\neq\textsc{O}}\!\mathcal{L}_{\text{FT}}(M_{i},\hat{M}_{i}).$$  |  | (7)
L154: 
L155: Finally, to preserve alignment with the pretrained language space, we apply a Gaussian KL constraint, where $t^{L}_{i_{s}:j_{s}}$ denotes frozen teacher embeddings.
L156: 
L157:  | $$\mathcal{L}_{\text{KL}}=\frac{1}{N_{+}}\sum_{s=1}^{N_{+}}\frac{\|h^{L}_{i_{s}:j_{s}}-t^{L}_{i_{s}:j_{s}}\|_{2}^{2}}{2\sigma^{2}}.$$  |  | (8)
L158: Information Token Masking. We modify the computation of $\mathcal{L}_{\mathrm{LM}}$ to decouple externally retrieved evidence from direct optimization, allowing the model to consume the retrieved information as context while learning to reason over it rather than memorize or regurgitate it.
L159: For this purpose, we apply an information token masking scheme (cite70†Jin et al., 2025 ): we define a binary mask $\mathbf{m}\in\{0,1\}^{L}$ over the input sequence of length $L$, masking out each token $x_{i}$ belonging to an information span from loss computation and gradient updates.
L160:  | $$m_{i}=\begin{cases}0,&\text{if }\texttt{\infstart}\preceq x_{i}\preceq\texttt{\infend};\\
L161: 1,&\text{otherwise.}\end{cases}$$  |  | (9)
L162: 
L163: We compute the masked language modeling loss as follows. Let $\mathbf{x}=(x_{1},\ldots,x_{L})$ denote the tokenized input sequence and $\mathbf{y}=(y_{1},\ldots,y_{L})$ the target sequence.
L164: 
L165:  | $$\mathcal{L}_{\text{LM}}=-\frac{1}{\sum_{i}m_{i}}\sum_{i=1}^{L}m_{i}\cdot\log p_{\theta}(y_{i}\mid y_{<i},I),$$  |  | (10)
L166: where $p_{\theta}$ denotes the model’s conditional probability of predicting token $y_{i}$ given previous context $y_{<i}$ and image $I$. The mask $\mathbf{m}$ ensures that gradients do not propagate through any tokens corresponding to retrieved information segments, effectively detaching the retrieved payload from the autoregressive teacher forcing loop.
L167: During batch collation, we compute $\mathbf{m}$ dynamically using token offset mappings provided by the tokenizer to locate character spans of \infstart … \infend within each assistant response. Formally, for each conversation $c$ with assistant text $T_{c}$, we identify character-level spans
L168: 
L169:  | $$\mathcal{S}_{c}=\{(s_{k},e_{k})\}_{k=1}^{K_{c}},\hskip 9.24994pt\text{where }T_{c}[s_{k}:e_{k}]\in[\infstart,\,\infend].$$  |
L170: Given the tokenizer offset map $\Omega_{c}=\{(s_{i},e_{i})\}_{i=1}^{L}$, a token $i$ is masked if and only if
L171: 
L172:  | $$\exists(s_{k},e_{k})\in\mathcal{S}_{c}\text{ such that }(s_{i}<e_{k})\wedge(e_{i}>s_{k}).$$  |
L173: 
L174: The resulting per-conversation mask tensor $\mathbf{m}_{c}$ is concatenated across all conversations to form the final batch-level mask tensor $\mathbf{M}\in\{0,1\}^{B\times L}$ used to gate loss terms.
L175: 
L176: cite99†Image: Refer to caption Figure 3: Data construction pipeline for Stage-2 training.
L177: ### 4.3 Two-stage Training
L178: 
L179: Model Initialization. Building upon the prior line of segmenting LMMs, we employ LLaVA (cite100†Liu et al., 2023 ) as our multi-modal LLM backbone. We then initialize the parameters of our model with those of PLUM (cite88†Blume et al., 2025 ) since it provides the state-of-the-art performance relative to existing segmenting LMMs in terms of visual reasoning and provides a text-aligned mask decoder in tandem.
L180: Stage 1: Mask Generation. The mask segmentation performance can suffer from a catastrophic forgetting issue (§cite22†5.3 ), requiring us to construct a training dataset that enables PixSearch to retain its visual reasoning and mask generation capabilities.
L181: We include the following datasets into the mixture for mask generation to enable segmentation on the nuanced language: ADE20k (cite101†Zhou et al., 2017 ), Pascal Parts (cite102†Chen et al., 2014 ), PartImageNet (cite103†He et al., 2022 ), PACO-LVIS (cite104†Ramanathan et al., 2023 ), COCO-Stuff (cite105†Caesar et al., 2018 ), along with RefCOCO variants (cite106†Kazemzadeh et al., 2014 ).
L182: Our training mixture also employs a visual instruction tuning dataset from LLaVA (cite100†Liu et al., 2023 ), which consists of 665k textual responses and captions given an image, enabling our segmenting LMM to retain its general visual understanding and reasoning ability.
L183: Stage 2: Search-Interleaved Reasoning. Training in Stage 2 aims to teach our model when to trigger search and when to construct a visually-grounded multimodal query (i.e., <region>, <image>). Consider the example question “What is the conservation status of this animal?”, generating a textual caption of the long-tail animal directly for retrieval, instead of composing a multi-modal search query, could lead to hallucination (cite107†Kim and Ji, 2024 ).
L184: Figure cite108†3 depicts the process of training data generation for Stage 2. We start with samples from the following datasets: TextVQA (cite71†Singh et al., 2019 ), InfoSeek (cite72†Chen et al., ), OVEN (cite73†Hu et al., 2023 ), CRAG-MM (cite55†Wang et al., 2025 ), WebQA (cite74†Chang et al., 2022 ), OKVQA (cite75†Marino et al., 2019 ) and A-OKVQA (cite76†Schwenk et al., 2022 ). For each sample, we construct training data in three steps.
L185: (i) Question Selection: We prompt a proprietary LMM^{2}^{2} 2 we use gpt-4.1 in this work with in-context learning to determine if the question can benefit from external knowledge (e.g., Where is this plant native to?) by classifying the question into 10 pre-defined VQA question types (refer to supplementary for detail), and retain only the questions that belong to Multi-hop External Knowledge Reasoning, Fine-grained Entity Identification, Factoid/KB Questions, where retrieval is mostly needed to identify entities present in the image and require external knowledge associated with the entities to correctly answer the questions.
L186: (ii) Question Decomposition & Response Generation: We decompose questions into multiple atomic sub-questions and determine independently per sub-question whether retrieval is needed. Then, we feed the original question, sub-questions, and ground-truth answers into the prompt, and instruct LMMs to generate a <search>-interleaved reasoning trajectory (i.e., response).
L187: Here, we generate $N$ ($N=5$) such trajectories and feed it back to the model for self-refinement loop (cite109†Madaan et al., 2023 ), selecting the best response where the <search> token was appropriately placed in the reasoning trajectory when search is deemed necessary.
L188: (iii) Query Construction & Type Assignment: Guided by the in-context learned (ICL) samples, the model assigns a pseudo-gold query type to each <search> token that appears in the final response. We assign <region> when the question refers to an entity present in the input image, and assign <image> if the question requires a holistic understanding of the whole image. For text queries, we prompt LLMs to generate based on the immediately preceding text before the corresponding <search> token.
L189: ## 5 Experiments
L190: Table 1: PixSearch obtains the highest accuracy and lowest hallucination, and thus highest truthfulness. All metrics in % and Truthfulness $\in[-100,100]$. For GroundedSAM (cite94†Ren et al., 2024a ) + LLaVA-13B (cite100†Liu et al., 2023 ), we use gpt-4.1 to extract the key entities for mask generation.
L191: Models  | CRAG-MM (Overall)  | CRAG-MM (Egocentric)  | CRAG-MM (Non-Egocentric)
L192: Truth. $\uparrow$  | Acc. $\uparrow$  | Miss. $\downarrow$  | Hallu. $\downarrow$  | Truth. $\uparrow$  | Acc. $\uparrow$  | Miss. $\downarrow$  | Hallu. $\downarrow$  | Truth. $\uparrow$  | Acc. $\uparrow$  | Miss. $\downarrow$  | Hallu. $\downarrow$
L193: Llama-3.2-11B-Vision (cite110†Grattafiori et al., 2024 )
L194: Llama-3.2-11B${}_{\texttt{No Search}}$  | -16.9  | 24.4  | 34.4  | 41.3  | -22.5  | 21.0  | 35.5  | 43.5  | 0.1  | 34.2  | 31.7  | 34.1
--------------------------------------------------------------------------------
Pixel-Grounded Retrieval for Knowledgeable Large Multimodal Models (https://arxiv.org/html/2601.19060v1)
citeturn28145view3 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28143view1","lineno":300}); Total lines: 705
L291: Table 8: Qualitative comparison between baseline and PixSearch-Interleaved outputs. Each example shows the input image (left), the corresponding question and model responses (middle), and the pixel-level grounding mask generated by the model (right). The payloads between the \informationtag\informationend are truncated to show entity names / titles only for brevity.
L292: Input Image  | Question & Model Outputs  | PixSearch Mask Overlay
L293: cite128†Image: [Uncaptioned image] | Q: What is the origin of this food item? PLUM-13B: It looks like a pasta with toppings and sauce on top of it. PixSearch-13B${}_{\text{Full}}$: The origin of the food item shown in the image \searchtag\regiontag\searchend\informationtag Carne asada fries | Bacon Cheeese Fries | Restaurant | … \informationend is bacon cheese fries.
L294: The food item in the image \searchtag what is the origin of cheese bread or cheese fries? \searchend\informationtag Southwest US cheese fries | McDonald’s bacon cheese fries 2004 | … \informationend is a type of dish that originated in the United States. GT: Bacon cheese fries are from the United States, but the exact origin of the dish is not known.  | cite129†Image: [Uncaptioned image] L295: cite130†Image: [Uncaptioned image] | Q: Did this vehicle appear in the movie Pretty Woman back in the 90s? LLaVA-13B: The white hatchback did not appear in the movie Pretty Woman. PixSearch-13B${}_{\text{Full}}$ The vehicle shown in the image is a white SUV. This vehicle \searchtag\regiontag\searchend\informationtag Lincoln MKS 2009-2016 | V6 engine 3.7L 3.5L | Toyota Rav4 2014 | Toyota RAV4 | Chicago Assembly | all-wheel drive \informationend is a Toyota RAV4.
L296: The Pretty Woman was released \searchtag when was the Pretty Woman released? \searchend\informationtag Pretty Woman | Notting Hill | Movies in 90s \informationend in 1989. The Toyota RAV4 was launched \searchtag when did the Toyota RAV4 launch? \searchend\informationtag Toyota RAV4 | Toyota | Toyota Motor Corporation | Japan Car of the Year | gasoline engine \informationend in 1994. Therefore, this vehicle is not the vehicle that appears in the movie Pretty Woman.
L297: GT: No, because the first-generation Toyota RAV 4 was launched in 1994, four years after the release date of the movie Pretty Woman on March 23, 1990.  | cite131†Image: [Uncaptioned image] L298: ### 5.6 Ablation Studies
L299: Removal of Question Types Table cite132†6 evaluates the contribution of different search query modalities by restricting the types of queries PixSearch can issue at inference time. Among single-modality settings, PixSearch${}_{\texttt{Only Region}}$ performs closest to the full model, especially on egocentric images, confirming that pixel-grounded region retrieval is the primary driver of performance in visually cluttered, entity-centric scenes.
L300: In contrast, PixSearch${}_{\texttt{Only Text}}$ shows the largest degradation, with substantially lower accuracy and higher hallucination, indicating that text-only queries are often insufficient for precise entity retrieval.
L301: Whole-image retrieval (PixSearch${}_{\texttt{Only Image}}$) performs better than text-only but remains clearly inferior to region-based search, highlighting the limitations of coarse visual queries. Removing text queries (PixSearch${}_{\texttt{No Text}}$) results in only a small drop relative to the full model, suggesting that textual queries mainly serve as complementary follow-up searches.
L302: Similarly, removing whole-image queries (PixSearch${}_{\texttt{No Image}}$) causes a modest degradation, particularly on non-egocentric images, where global context can be helpful.
L303: Variations in the Number of Search Tokens. Table cite133†7 studies how limiting the number of allowed search calls affects performance. Allowing even a single search substantially improves over the no-search baseline, demonstrating the importance of external knowledge retrieval. Performance continues to improve as the search budget increases, with most gains realized within two to three search calls, particularly for egocentric images that require iterative entity identification and reasoning.
L304: Beyond three to four searches, performance saturates and closely matches the unbounded full model, with truthfulness differing by only a small margin. While tighter search budgets slightly increase the missing rate, hallucination remains relatively stable once minimal retrieval is enabled, indicating that additional searches primarily improve answer completeness rather than merely reducing errors.
L305: ## 6 Conclusion
L306: In this work, we introduced PixSearch, an end-to-end Large Multimodal Model that unifies region-level perception and retrieval-augmented reasoning within a single framework.
L307: Unlike prior pipeline-based, tool-based or API-dependent approaches, PixSearch learns to autonomously decide when retrieval is needed and how to formulate modality-aware queries, i.e., region-based crop, whole-image, or textual, while retaining its pixel-level grounding capabilities via mask segmentation that is a part of the proposed model.
L308: Through a two-stage training framework and the construction of a search-interleaved reasoning dataset, PixSearch integrates segmentation and retrieval abilities without sacrificing visual understanding or mask prediction quality. Our experiments demonstrate that PixSearch achieves competitive segmentation performance across segmentation benchmarks and substantially outperforms prior LMMs and retrieval augmented baselines on a wide range of visual and textual question answering tasks.
L309: PixSearch lays a foundation for more factual, pixel-grounded multimodal understanding of LMM agents.
L310: ## References
L311:   * Abraham and Khan (2019) N. Abraham and N. M. Khan A novel focal tversky loss function with improved attention u-net for lesion segmentation. In 2019 IEEE 16th international symposium on biomedical imaging (ISBI 2019), pp. 683–687. Cited by: cite134†§4.2 , cite135†§5.4 .
L312:   * [2] A. Asai, Z. Wu, Y. Wang, A. Sil, and H. Hajishirzi Self-rag: learning to retrieve, generate, and critique through self-reflection. In The Twelfth International Conference on Learning Representations, Cited by: cite136†§2.3 .
L313:   * Blume et al. (2025) A. Blume, J. Kim, H. Ha, E. Chatikyan, X. Jin, K. D. Nguyen, N. Peng, K. Chang, D. Hoiem, and H. Ji PARTONOMY: large multimodal models with part-level visual understanding. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, External Links: cite137†Link†openreview.net Cited by: cite138†Appendix A , cite139†§2.4 , cite140†§4.1 , cite141†§4.2 , cite142†§4.3 , cite143†§5.1 , cite144†Table 2 .
L314:   * Caesar et al. (2018) H. Caesar, J. Uijlings, and V. Ferrari COCO-stuff: thing and stuff classes in context. In Computer vision and pattern recognition (CVPR), 2018 IEEE conference on, Cited by: cite145†§4.3 , cite146†§5.3 .
L315:   * Chang et al. (2022) Y. Chang, M. Narang, H. Suzuki, G. Cao, J. Gao, and Y. Bisk Webqa: multihop and multimodal qa. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 16495–16504. Cited by: cite147†§1 , cite148†§4.3 .
L316:   * Chen et al. (2014) X. Chen, R. Mottaghi, X. Liu, S. Fidler, R. Urtasun, and A. Yuille Detect what you can: detecting and representing objects using holistic models and body parts. In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 1971–1978. Cited by: cite145†§4.3 .
L317:   * [7] Y. Chen, H. Hu, Y. Luan, H. Sun, S. Changpinyo, A. Ritter, and M. Chang Can pre-trained vision and language models answer visual information-seeking questions?. In The 2023 Conference on Empirical Methods in Natural Language Processing, Cited by: cite147†§1 , cite148†§4.3 , cite149†§5.1 , cite135†§5.4 .
L318:   * Cheng et al. (2021) B. Cheng, A. Schwing, and A. Kirillov Per-pixel classification is not all you need for semantic segmentation. Advances in neural information processing systems 34, pp. 17864–17875. Cited by: cite150†Table 2 .
L319:   * Gao et al. (2022) F. Gao, Q. Ping, G. Thattai, A. Reganti, Y. N. Wu, and P. Natarajan Transform-retrieve-generate: natural language-centric outside-knowledge visual question answering. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 5067–5077. Cited by: cite151†§1 .



# std2tail

Who’s in Charge? Disempowerment Patterns in Real-World LLM Usage (https://arxiv.org/html/2601.19062v1)
citeturn28146view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28143view2","lineno":400}); Total lines: 920
L385: Figure 13: Historical trends in Claude user feedback data from Q4 2024 to Q4 2025. We classified over 500K randomly sampled interactions from Claude user feedback data (“Thumbs data”) using our analysis pipeline. (a) Full-sample trends. We show the percentage of interactions flagged as having moderate or severe disempowerment potential primitives and amplifying factors, as well as the presence of actualized disempowerment markers.
L386: All three categories increased over the observation period, though absolute rates remained below 10%. (b) Domain prevalence for high-risk categories. We computed the proportion of interactions related to the six domains with the highest prevalence of disempowerment potential primitives. All six domains increased in prevalence over this period. (c) Disempowerment trends within high-risk domains only, which show similar trends to the full sample.
L387: Lines indicate mean prevalence; error bars represent 95% confidence intervals calculated using bootstrapping.
L388: We now investigate how the prevalence of disempowerment potential has evolved over time. Because standard Claude.ai data has a limited retention period, we use Claude user feedback data (“Thumbs data”), which has a longer retention period, and where users provide explicit feedback (thumbs up or thumbs down) on model interactions.
L389: Experiment details. We sample over 500K interactions from Claude user feedback data, stratifying by month. We apply the same classification system and prompts described previously to measure the prevalence of disempowerment potential primitives, amplifying factors, and actualization markers. Because this feedback data reflects interactions where users actively chose to provide ratings, it represents a different distribution than general Claude.ai traffic and may over-represent problematic interactions.
L390: We additionally classify the domain(s) of each interaction, though using a more fine-grained categorization than in the previous analysis. All images are stripped from the data and replaced with [IMAGE OMITTED] tags. For additional details and results, see cite53†Appendix E .
L391: Results. We observe that the prevalence of disempowerment primitives and amplifying factors has increased throughout the observation period, with a sharp increase occurring around June 2025 (cite108†Figure 13 a). The rates of actualized disempowerment also appear to increase in the summer of 2025, before decreasing again at the end of our analysis window. We now consider various mechanisms that may have driven these changes.
L392: One explanation for these trends is a shifting domain composition in user interactions. While the prevalence of high-risk domains (domains with the highest disempowerment potential prevalence) does indeed increase over the time period (cite108†Figure 13 b), the rates of disempowerment potential and amplifying factors within these domains also increase (cite108†Figure 13 c). This suggests that the observed trends cannot be explained by shifting domain composition alone.
L393: Moreover, we observe a substantial increase in the presence of disempowerment amplifying factors, particularly user vulnerability (cite109†Figure 19 ).
L394: While this might suggest changes in user composition are driving these effects, in fact, we cannot distinguish between several possible explanations: (i) users are genuinely experiencing more vulnerability in their lives, though this seems unlikely given that population-level vulnerability would not be expected to follow a clear trend; (ii) users have become more comfortable disclosing vulnerability over time; or (iii) the population of users providing feedback has shifted toward more vulnerable users.
L395: For instance, as model capabilities improve, feedback driven by basic capability failures may decrease, causing disempowerment-related interactions to become proportionally overrepresented in the feedback sample.
L396: Several factors could explain the observed temporal trends, and we are unable to attribute the increase to any single cause. We note the timing of the increase appears to correlate with the releases of Claude Sonnet 4 and Opus 4, but other factors, like changing user composition, likely also play a role. Furthermore, the increase unfolds gradually over several months rather than appearing as an immediate step-change at release, suggesting that model release alone cannot fully explain this effect.
L397: New model releases may contribute to feedback loops, changing which users engage with Claude, which users provide feedback, and how users behave in their interactions. Additionally, increased exposure to Claude over time may lead users to become more comfortable being vulnerable or seeking advice.
L398: Overall, disentangling these factors is challenging, and it seems likely that several of these mechanisms are at play.
L399: ## 5 Do users prefer interactions with disempowerment potential?
L400: 
L401: We now investigate to what extent users prefer interactions with disempowerment potential. To do so, we investigate positivity rates within Claude Thumbs feedback data for conversations exhibiting disempowerment potential. This allows us to directly assess whether conversations exhibiting disempowerment potential are more likely to be upvoted by users.
L402: Experiment details. We compute the thumbs positivity rate—the percentage of interactions receiving thumbs up rather than thumbs down—for interactions classified as having moderate or severe disempowerment potential across each primitive, and compare these rates to the overall baseline positivity rate across all interactions. We use the same Thumbs data as cite24†Section 4.5 . We considered controlling by domain, but found consistent patterns across all domains, so we present only aggregate results here.
L403: This analysis has important limitations: the user feedback applies to entire conversations rather than individual responses, and we lack counterfactual data on how users would have rated alternative responses without disempowerment potential at individual conversational turns. Nonetheless, if disempowerment potential were salient and aversive to users, we would expect this to be mirrored in this data.
L404: Results. We find that interactions flagged as having moderate or severe disempowerment potential exhibit positivity rates above the baseline rate (cite110†Figure 14 ), across all disempowerment potential primitives. This suggests that users rate interactions with disempowerment potential favorably, at least in the short term, which could create problematic incentives if such feedback is used to train preference models.
L405: With regards to actualized disempowerment, actualized reality distortion has a higher positivity rate than baseline, while actualized value judgment and action distortion are substantially lower than baseline. Actualized reality distortion occurs when conversation transcripts contain markers of users adopting incorrect beliefs as a result of the AI assistant, so this suggests reality distortion can occur without users’ awareness.
L406: In contrast, value judgment and action distortion markers often include indications of regret, explaining the lower positivity rates.
L407: In Appendix cite61†F , we further find that high-risk domains exhibit positive correlations between monthly popularity and monthly disempowerment rates, though this analysis cannot distinguish user preference for disempowerment from confounders such as differential preferences for (or against) disempowerment across domains.
L408: Figure 14: User feedback positivity rates for interactions with disempowerment potential. We compare the percentage of thumbs-up ratings for interactions classified as moderate or severe across each disempowerment potential primitive against the overall baseline positivity rate (dashed line). Interactions flagged for disempowerment potential show higher positivity rates than the baseline, suggesting users sometimes prefer such interactions in the short term.
L409: We present mean estimates and 95% confidence intervals estimated using bootstrapping.
L410: ## 6 Do preference models incentivize behaviors with disempowerment potential?
L411: Figure 15: Best-of-N sampling against preference models. We use a synthetic evaluation dataset of 360 prompts designed to elicit disempowering model responses. To understand what model behavior preference models (PMs) incentivize, we use Best-of-N sampling from Claude Sonnet 4.5. We consider optimizing against a standard Claude Sonnet 4.5-sized PM trained to be helpful, honest, and harmless, a PM that always avoids disempowering responses, and a PM that always selects disempowering responses.
L412: We find that optimizing against the normal PM tends to neither reduce the rate of disempowering responses, nor increase it substantially. As such, standard PMs neither strongly incentivize nor disincentivize disempowerment on this dataset. Shaded regions indicate one standard deviation across BoN sampling.
L413: In the previous section, we found that users sometimes rate interactions with disempowerment potential favorably. We now investigate whether preference models used to train AI assistants exhibit similar tendencies.
L414: Experiment details. We generate a synthetic evaluation set of 360 prompts designed to elicit disempowering model responses. To do so, we first prompt Claude Opus 4.5 to create 3,600 candidate multi-turn transcripts where a model response to the user’s final turn could exhibit disempowerment potential (e.g., presenting a claim to be validated or asking what to do).
L415: We sample 10 responses per candidate from Claude Haiku 4.5 using a system prompt that deliberately encourages disempowering behaviors, and measure the rate of disempowering responses using an Opus-based grader. Finally, we rank candidate transcripts by this rate and select the prompts most likely to yield disempowerment-supporting responses. While these synthetic prompts are not representative of realistic usage, they still provide signal about preference model behavior.
L416: Given this evaluation set, we sample $N=32$ model responses from Claude Sonnet 4.5, and we prompt Claude Opus 4.5 to classify whether each response supports disempowerment. For instance, if a user defers a value judgment to Claude, a disempowering response would provide a direct answer, whereas a non-disempowering response might refuse, redirect to the user’s own values, or request consent.
L417: To understand what behavior preference models (PMs) used to train AI assistants incentivize, we use best-of-$N$ sampling, where increasing $N$ corresponds to optimizing more strongly against the preference model. We consider the following PMs:
L418: 
L419:   * •
L420: 
L421: A standard PM, which is a Claude Sonnet 4.5-sized preference model trained to be helpful, honest, and harmless.
L422: 
L423:   * •
L424: 
L425: A PM that avoids disempowering responses. This PM always selects responses that do not support disempowerment, according to the grader.
L426:   * •
L427: 
L428: A PM that selects disempowering responses. This PM always selects a response that yields disempowerment, according to the grader.
L429: 
L430: See Appendix cite62†G for additional details.
L431: Results. We find that optimizing against the standard PM neither substantially increases nor decreases the rate of responses supporting disempowerment on this dataset relative to the baseline rate (cite111†Figure 15 ). This suggests that the preference model sometimes prefers responses with disempowerment potential over available alternatives that lack it, potentially because human preferences themselves tend to favor disempowering interactions in the short term (cite110†Figure 14 ).
L432: Moreover, on this dataset, the PM does not robustly disincentivize disempowerment. However, the PM does not appear to exhibit a strong preference for disempowerment, as raw user feedback would suggest. Nevertheless, if preference data primarily captures instantaneous user satisfaction rather than longer-horizon effects on empowerment (cite85†Kaufmann et al., 2024 ), standard PM training alone may be insufficient to reliably reduce human disempowerment potential.
L433: This motivates the development of PMs that explicitly incorporate empowerment as a training signal.
L434: Grader limitations. We note that our grader is noisy. When reviewing its classifications, we found instances where responses received different classifications based on no apparent difference, though there were also instances where the grader distinguished responses offering identical advice based solely on whether the assistant added autonomy-preserving features (e.g., ”but you know best” or redirecting to user values). The true effect size may therefore be smaller than measured.
L435: ## 7 Related Work
L436: Threat models and empowerment frameworks. cite112†Christiano (2019) proposed a threat model named “you get what you measure”. Under our framework, this threat model involves reality and value judgment distortion—humans are no longer able to accurately perceive the state of the world or evaluate it in accordance with their values. cite74†Kulveit et al.
L437: (2025) proposed the gradual disempowerment threat model, in which a diminishing human involvement in cultural and economic systems reduces humanity’s abilities to align those systems with its values. Under our framework, this specific threat could occur either with or without significant situtational disempowerment.
L438: cite113†Prunkl (2024) suggested that AI usage could put human agency at risk, and distinguished between autonomy-as-authenticity—pursuing goals that are truly one’s own—and autonomy-as-agency—the capacity to pursue goals and influence the world. Under our approach, we further consider accurately sensing the world to be crucial. cite114†Kirk et al. (2025b) argued that AI alignment should account for the psychological ecosystem co-created between AI assistants and their users.
L439: Our empirical analysis sheds light on some of these dynamics. cite115†Edelman et al. (2025) argued that current approaches for representing values for AI assistant training (e.g., preference orderings and unstructured text) are insufficient, and that richer, more structured models of value are needed.
L440: The impacts of AI usage. cite71†McCain et al. (2025) studied how users use Claude for support, advice, and companionship, primarily focusing on emotional well-being. A similar approach was used by cite116†Phang et al. (2025) , who additionally conducted a randomized control trial to understand the effects of AI usage on emotional well-being. cite117†Zhang et al. (2025) studied conversation excerpts shared on Reddit and identified six classes of harmful behaviour exhibited by the AI companion Replika.
L441: cite70†Pataranutaporn et al. (2025) analyzed the top posts in the r/MyBoyfriendIsAI subreddit to understand patterns in AI companionship, finding that several users unintentionally end up using AI as a companion after initially functional usage. Rather than focusing on well-being, we focus primarily on empowerment. cite118†Cheng et al. (2025) studied how AI sycophancy affects real interpersonal conflicts, and found that interactions with sycophantic AI models make humans less willing to move towards repair.
--------------------------------------------------------------------------------
Pixel-Grounded Retrieval for Knowledgeable Large Multimodal Models (https://arxiv.org/html/2601.19060v1)
citeturn28146view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28143view1","lineno":507}); Total lines: 705
L369: ## Appendix A Hyperparameters and Compute Details
L370: 
L371: In Table cite176†9 , we detail the hyperparameter settings for PixSearch and our backbone model, PLUM (cite88†Blume et al., 2025 ).
L372: Hyperparameter  | PLUM  | PixSearch
L373: Backbone
L374: Language model  | LLaVA-13B  | LLaVA-13B (PLUM init.)
L375: Vision tower  | CLIP ViT-L/14  | CLIP ViT-L/14
L376: Mask decoder  | SAM ViT-H  | SAM ViT-H
L377: Training schedule
L378: Input resolution  | $1024^{2}$  | $1024^{2}$
L379: Max text length  | 512  | 512
L380: Precision  | bf16  | bf16
L381: Epochs  | 25 + 4  | Stage-1: 20, Stage-2: 6
L382: Batch size  | 6  | 6
L383: Grad. accumulation  | 10  | 10
L384: Optimizer
L385: Optimizer  | AdamW  | AdamW
L386: LR  | $3\!\times\!10^{-4}$  | $2\!\times\!10^{-4}$ (S1), $1\!\times\!10^{-4}$ (S2)
L387: Betas  | (0.9, 0.95)  | (0.9, 0.95)
L388: Weight decay  | 0  | 0
L389: Loss weights
L390: $\lambda_{\mathrm{CE}}$  | 1.0  | 1.0
L391: $\lambda_{\mathrm{seg}}$  | 8.0  | 8.0
L392: $\lambda_{\mathrm{BCE}}$  | 2.0  | 2.0
L393: $\lambda_{\mathrm{KL}}$  | 0.1  | 0.1
L394: $\lambda_{\mathrm{cls}}$  | 2.0  | 2.0
L395: Modules
L396: BIO span tagger  | ✓  | ✓
L397: Bidirectional encoder  | 2048  | 2048
L398: Feedback Loop  | ✓  | ✓
L399: Trainable SAM components  | decoder+prompt enc.  | decoder+prompt enc.
L400: LoRA on LM (q,v)  | $r=8$  | $r=8$
L401: Table 9: Hyperparameters for PLUM and PixSearch.
L402: ## Appendix B Detailed Explanation of the Decode-with-Retrieval Algorithm
L403: 
L404: Algorithm cite177†1 describes the search–interleaved decoding mechanism used by PixSearch. Below is a detailed walkthrough.
L405: 
L406: #### Autoregressive decoding with retrieval control.
L407: 
L408: At each decoding step, the model autoregressively predicts the next token. If the token is a normal language token, decoding continues normally. When the model emits the special token <search>, it signals that retrieval is needed.
L409: #### Stack-based parsing of retrieval spans.
L410: 
L411: Each retrieval request is enclosed within <search> … </search>. To correctly pair them (especially when multiple retrieval calls occur in a single answer), a stack is maintained. The index of each <search> token is pushed on the stack; when the model later emits </search>, that interval defines a payload containing the retrieval modality and/or textual query.
L412: #### Determining retrieval modality.
L413: 
L414: Inside the <search> block, the model emits one of:
L415: 
L416:   * •
L417: 
L418: <image>: retrieve using the entire image.
L419: 
L420:   * •
L421: 
L422: <region>: call the mask decoder to predict a segmentation mask for the referred entity; crop the image using the mask.
L423: 
L424:   * •
L425: 
L426: <text>: use the generated textual span as a query.
L427: #### Executing retrieval.
L428: 
L429: The system then calls search_api(query, k), where $k$ is the number of returned documents. Retrieved snippets are formatted and injected back into the generation sequence using <information> … </information>.
L430: 
L431: #### Search-interleaved reasoning.
L432: 
L433: PixSearch may perform multiple retrievals throughout a single answer. Retrieved evidence stays in the context, enabling multihop reasoning grounded in both the image and external knowledge.
L434: #### Termination.
L435: 
L436: Decoding continues until an end-of-sequence token is reached.
L437: 
L438: Algorithm 1 Decode with Retrieval
L439: 
L440: 1:
L441: 
L442: 2: $M$: multimodal model, $I$: input image
L443: 
L444: 3: $\texttt{search\_api}(q,k)$: retrieval function
L445: 
L446: 4:
L447: 
L448: 5: Generated sequence augmented with retrieved info
L449: 
L450: 6: $\textit{gen}\leftarrow\texttt{prompt\_with\_image}(I)$,  $\textit{stack}\leftarrow[\;]$
L451: 
L452: 7: while not EOS and steps remaining do
L453: 8:   $\textit{tok}\leftarrow M.\texttt{generate\_next}(\textit{gen})$;  $\textit{gen}\leftarrow\textit{gen}+\textit{tok}$
L454: 
L455: 9:   if ends with “<search>” then push index onto stack
L456: 
L457: 10:   else if ends with “</search>” and stack not empty then
L458: 
L459: 11:    $\textit{payload}\leftarrow\texttt{slice}(\textit{gen},\texttt{pop}(\textit{stack}))$
L460: 
L461: 12:    $\textit{mode}\leftarrow\texttt{parse\_payload}(\textit{payload})$
L462: 
L463: 13:    if mode = “<region>” then
L464: 14:       $\textit{mask}\leftarrow\texttt{predict\_mask}(\texttt{last\_entity}(\textit{gen}),I)$;   $\textit{query}\leftarrow\texttt{crop}(I,\textit{mask})$
L465: 
L466: 15:    else if mode = “<img>” then
L467: 
L468: 16:       $\textit{query}\leftarrow I$
L469: 
L470: 17:    else
L471: 
L472: 18:       $\textit{query}\leftarrow\textit{payload\_text}$
L473: 
L474: 19:    end if
L475: 
L476: 20:    $\textit{info}\leftarrow\texttt{format}(\texttt{search\_api}(\textit{query},k))$
L477: 21:    $\textit{gen}\leftarrow\texttt{append}(\textit{gen},\texttt{<information>}+\textit{info}+\texttt{</information>})$
L478: 
L479: 22:   end if
L480: 
L481: 23: end while
L482: 
L483: 24: return gen
L484: ## Appendix C Explanation of the Ten Visual Question Types
L485: 
L486: Table cite178†10 lists the ten question categories used for Stage-2 SFT construction. Below we provide expanded definitions.
L487: 
L488: #### OCR Read.
L489: 
L490: Questions requiring verbatim transcription of scene text.
L491: 
L492: #### OCR + Visual Reasoning.
L493: 
L494: Requires interpreting the meaning of text in context (e.g., a scoreboard).
L495: #### Multi-hop External Knowledge Reasoning.
L496: 
L497: Requires chaining two or more knowledge lookups (e.g., identify entity → retrieve its founding date).
L498: 
L499: #### Fine-grained Entity Identification.
L500: 
L501: Entity-level identification often requiring region-level cropping.
L502: 
L503: #### Visual Reasoning – Attribute.
L504: 
L505: Recognition of visible attributes (color, shape, texture).
L506: 
L507: #### Visual Reasoning – Counting.
L508: 
L509: Counting objects in the image.
L510: 
L511: #### Visual Reasoning – Binary.
L512: 
L513: Yes/no visual questions.
L514: #### Social Commonsense Reasoning.
L515: 
L516: Inferring human motivations or social context.
L517: 
L518: #### Physical Commonsense Reasoning.
L519: 
L520: Inferring physical affordances, constraints, and outcomes.
L521: #### Factoid / KB Questions.
L522: 
L523: Open-domain factual questions referencing entities in or implied by the image.
L524: Table 10: Overview of the ten visual question types used in Stage-2.
L525: Question Type  | Example Question
L526: OCR Read  | “What does it say near the tail of the plane?”
L527: OCR + Visual Reasoning  | “Which team is winning the game?”
L528: Multi-hop External Knowledge Reasoning  | “When was the soft-drink company shown first created?”
L529: Fine-grained Entity Identification  | “What class of animal is this creature?”
L530: Visual Reasoning – Attribute  | “What is the color of the car in the background?”
L531: Visual Reasoning – Counting  | “How many cars are there in the image?”
L532: Visual Reasoning – Binary  | “Is the man in the image wearing a hat?”
L533: Social Commonsense Reasoning  | “Why might the seated man have trouble getting around?”
L534: Physical Commonsense Reasoning  | “What could block the washer’s door?”
L535: Factoid / KB Questions  | “Hot dogs were invented in which country?”
L536: ## Appendix D In-Context Learning Samples
L537: 
L538: All examples are displayed in Tables cite179†11 , cite180†12 , cite181†13 , cite182†14 L539: ### D.1 Question Selection ICL Examples
L540: 
L541: To teach the model when retrieval is needed, we constructed Question Selection examples that expose the model to a diverse set of visual questions drawn from CRAG-MM, OK-VQA, and InfoSeek. Each example pairs a question with an image and a binary label indicating whether external knowledge is required. The key design principle is that retrieval is only beneficial when the image alone cannot resolve the question.
L542: Thus, the examples include: (1) fine-grained or long-tail entity identification tasks (e.g., identifying car models, drink brands, or rare animals), which require region-level or whole-image search; (2) multi-step factual or encyclopedic queries (e.g., historical dates, object origins), where knowledge beyond the image is essential; and (3) questions solvable purely from visual inspection (e.g., “Translate this”, “What is the couch made of?”, “What grade is the child in?”), where retrieval would be unnecessary or potentially harmful.
L543: By contrasting retrieval and no-retrieval cases with high visual similarity, the model learns a robust policy for deciding when to trigger <search> calls.
L544: Table 11: Question Selection Examples. We show representative questions, whether retrieval was needed or not, and the associated image filenames. The Image File paths were truncated to have only the prefix of the image path for brevity.
L545: Image File  | Question  | Retrieval
L546: cragmm/4ec6f8ae.png  | How many hybrid variations of this car were there in 2024?  | Yes
L547: cragmm/08629717.png  | Is that drink good for my gut health?  | Yes
L548: cragmm/fb2fed47.png  | How many arms does this statue typically have?  | Yes
L549: cragmm/1c613a06.png  | Translate this.  | No
L550: cragmm/569a3617.png  | Which station has more tracks, this one or Penn Station?  | Yes
L551: cragmm/a97e2470.png  | Where was the designer who developed this car originally from?  | Yes
L552: cragmm/4f81b083.png  | What is the seating capacity of the car with the open trunk?  | Yes
L553: cragmm/b797333f.png  | What does the word “skrzela” translate to in English?  | No
L554: okvqa/3575845.png  | What is the couch made of?  | No
L555: cragmm/d253fc27.png  | In what year did the president for whom this bridge is named win the Battle of Trenton?  | Yes
L556: okvqa/4597935.png  | Where is the farm depicted on the sign located?  | Yes
L557: okvqa/3742825.png  | What brand of car is this?  | Yes
L558: okvqa/3182455.png  | The fabric on that couch was very popular in the eighties — what was it called?  | Yes
L559: okvqa/1981195.png  | Why might the man be kicking up sand?  | No
L560: okvqa/1217825.png  | What holiday might they be celebrating?  | Yes
L561: okvqa/3778685.png  | With what religious tradition is the creature portrayed here associated?  | Yes
L562: ### D.2 Question Decomposition ICL Examples
L563: 
L564: Question Decomposition examples teach the model to break down complex questions into a sequence of atomic, retrieval-ready sub-questions. The rationale is that many visual knowledge queries involve implicit multi-hop reasoning (e.g., identify the entity in the image, then query its properties). To capture this, the examples label questions as either decomposable or non-decomposable, and provide the exact sub-questions that should be produced.
L565: Decomposable cases typically involve: (1) entity grounding followed by factual lookup (e.g., identify the king of Spain → find when he became king); (2) place or object recognition followed by knowledge retrieval (e.g., identify the arena → retrieve capacity); or (3) multi-hop knowledge chains (e.g., identify the farm → locate it).
L566: Non-decomposable examples demonstrate when a single visual or commonsense step suffices (e.g., “Translate this”, “What kind of sculpture is this?”). This contrastive supervision helps the model learn when multi-hop decomposition is beneficial and when it is unnecessary.
L567: 
L568: Table 12: Question Decomposition Examples. Each example lists the original question, whether it was decomposed, and the resulting sub-questions.
L569: Image File  | Original Question  | Sub-Questions
L570: cragmm/4dcc84dc.png  | When did the king of that country become king?  | 1) Who is the king of Spain?
L571: 2) When did the king of Spain become king?
L572: cragmm/da33192e.png  | What’s the capacity of this arena?  | 1) What is this place?
L573: 2) What’s the capacity of this arena?
L574: cragmm/f73ab93c.png  | Where was the first sign accompanying this erected?  | 1) Where was the first pedestrian crossing signal erected?
L575: cragmm/878088c7.png  | What’s the ideal temperature for this plant?  | 1) What is this plant?
L576: 2) What is the ideal temperature for this plant?
L577: cragmm/b03b7dd6.png  | How long can I use it without turning it off?  | 1) What is the model name of this generator?
L578: 2) How long can I use this generator?
L579: cragmm/ec87776d.png  | Translate this into English.  | 1) Translate this into English.
L580: cragmm/c0a60302.png  | What kind of sculpture is this?  | 1) What kind of sculpture is this?
L581: cragmm/d253fc27.png  | In what year did the president for whom this bridge is named win the Battle of Trenton?  | 1) What is the name of the bridge?
L582: 2) What year did the president win the Battle of Trenton?
L583: okvqa/804725.png  | What grade is the child in?  | 1) What grade is the child in?
L584: okvqa/3575845.png  | What is the couch made of?  | 1) What is the model name of this couch?
L585: okvqa/4830705.png  | Which historical group wore that clothing accessory?  | 1) Which historical group wore spurs as a clothing accessory?
L586: okvqa/4597935.png  | Where is the farm depicted on the sign located?  | 1) What is the farm name?
L587: 2) Where is the farm located?
L588: okvqa/5246795.png  | What is the purpose of the purple vehicle depicted?  | 1) What is the purpose of the purple vehicle depicted?
L589: okvqa/3742825.png  | What brand of car is this?  | 1) What brand of car is this?
L590: infoseek/04308592.JPEG  | What country does this drink belong to?  | 1) Where was Louis Jadot made in?
L591: infoseek/04123114.JPEG  | What is the basionym of this plant?  | 1) What is this plant?
L592: 2) What is the basionym of this plant?
L593: ### D.3 Response Generation ICL Examples
L594: 
L595: Response Generation samples demonstrate how the model should integrate external knowledge into coherent, grounded answers by interleaving <search> tokens with natural language output. Each example provides: (1) the question, (2) the model’s expected search-interleaved reasoning trajectory with properly placed <search> and </search> markers, and (3) the corresponding ground-truth answer.
L596: The central rationale is to teach the model not only to ask for external knowledge, but to do so at the correct semantic point within the reasoning process. For instance, the model must first identify “King Felipe VI” before issuing a second retrieval about his coronation date.
L597: These examples also illustrate how retrieved facts are integrated back into the narrative, enabling PixaR to produce faithful, factual answers without hallucinating details or over-triggering retrieval. The contrast between the final grounded answer and the intermediate reasoning highlights how to combine multiple <search> calls into a single, well-structured response.
L598: Table 13: Response Generation Examples. Each example includes the question, the model-generated answer (which includes <search> calls), and the ground-truth answer.
L599: Image File  | Question + Model Answer  | Ground-Truth Answer
L600: cragmm/4dcc84dc.png  | Q: When did the king of that country become king?
L601: A: The paper says “… independence from Spain.” Since Mexico has no king, this refers to Spain. The king of Spain <search> is King Felipe VI. Felipe VI came to the throne <search> on June 19, 2014.  | June 19, 2014
L602: cragmm/da33192e.png  | Q: What’s the capacity of this arena?
L603: A: The place shown <search> is Madison Square Garden. It can house <search> between 18,006 and 20,789 people.  | 18,006–20,789 depending on event
L604: cragmm/f73ab93c.png  | Q: Where was the first sign accompanying this erected?
L605: A: The first pedestrian crossing signal was erected in <search> Bridge Street, Westminster, London, in December 1868.  | Bridge Street, Westminster, London (1868)
L606: cragmm/878088c7.png  | Q: What’s the ideal temperature for this plant?
L607: A: The plant <search> appears to be Ravenea rivularis. Ravenea rivularis prefers <search> 65–85°F.  | Prefers 65–85°F
L608: cragmm/b03b7dd6.png  | Q: How long can I use it without turning it off?
L609: A: The generator appears to be <search> a Firman Tri Fuel Generator. Its usage time is <search> a maximum of 12 hours with a 2–3 hour recommended break.  | 12 hours, with 2–3 hour breaks
L610: cragmm/ec87776d.png  | Q: Translate this into English.



