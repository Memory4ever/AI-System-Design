# Exact-v1 primary cached excerpts — 2601.19620


## Existing parsed-page cache recovery 2

R³: Replay, Reflection, and Ranking Rewards for LLM Reinforcement Learning (https://arxiv.org/html/2601.19620v1)
citeturn28403view2 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: open({"ref_id":"turn28176view0","lineno":130}); Total lines: 337
L98:  | $$\hat{A}_{i}=\frac{R_{i}-\operatorname{mean}(\{R_{i}\}_{i=1}^{G})}{\operatorname{std}(\{R_{i}\}_{i=1}^{G})}.$$  |  | (1)
L99: 
L100: The optimization objective of GRPO with the group-level advantage is given by the following equation:
L101:  | $\displaystyle\footnotesize\mathcal{J}_{\text{GRPO}}(\theta)=\mathbb{E}_{o\sim\pi_{\theta}}\Big[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\min\Big(r_{i}(\theta)\hat{A_{i}},$  |
L102:  | $\displaystyle\hskip 0.0pt\text{clip}\left(r_{i}(\theta),1-\epsilon,1+\epsilon\right)\hat{A_{i}}-{\beta}D_{KL}(\pi_{\theta}||\pi_{ref})\Big)\Big]$  |  | (2)
L103: where $r_{i}(\theta)=\frac{\pi_{\theta}(o_{i}\mid q)}{\pi_{\theta_{\text{old}}}(o_{i}\mid q)},$ $\pi_{old}$ is the previous policy model, $\epsilon$ is the clipping coefficient and $D_{KL}$ represent computing Kullback-Leibler (KL) divergence cite49†Kullback and Leibler (1951) between policy model $\pi_{\theta}$ and reference model $\pi_{ref}$.
L104: While GRPO effectively stabilizes training without a critic, it fundamentally relies on intra-group reward variance to estimate advantages. As indicated in Eq. (cite65†1 ), a critical limitation arises when all sampled responses within a group yield identical rewards. In such scenarios, the standard deviation $\operatorname{std}(\{R_{i}\}_{i=1}^{G})$ vanishes, leading to advantage collapse. This results in uninformative gradients that hinder policy updates and impair training efficiency.
L105: To address these challenges, we propose a stratified strategy tailored to queries of varying difficulty levels: (1) For medium-difficulty queries, where the model may yield homogeneous outcomes (e.g., all correct or all incorrect) within a single sampling round, relying solely on intra-group variance leads to advantage collapse.
L106: We employ Cross-Context Replay (CCR) to inject historical samples with opposing rewards, thereby ensuring continuous gradient updates by artificially reconstructing the advantage gap. (2) For hard queries characterized by persistent failure, we introduce In-Context Self-Reflection (ISR) to explicitly guide the model toward self-correction and reasoning refinement.
L107: (3) Finally, for extremely hard queries resulting in truncated responses where verifiable outcome rewards are unavailable, we utilize the Structural Entropy Ranking Reward (SERR) to provide a meaningful training signal based on the reasoning process.
L108: Algorithm 1 R³ Algorithm
L109: 
L110: 0:  Task Prompts $\mathcal{D}$; Policy $\pi_{\theta}$; Buffer $S$; Parameters $E,\tau,p_{r}$
L111: 
L112: 0:  Optimized Policy $\pi_{\theta}$
L113: 
L114: 1:  for $epoch=1:E$ and $\mathcal{D}_{b}\in\mathcal{D}$ do
L115: 
L116: 2:    if $epoch>1$ then
L117: 
L118: 3:     $\mathcal{D}_{b}\leftarrow\mathcal{D}_{b}\cup\{q\oplus o_{h}\oplus p_{r}\mid q\in\mathcal{D}_{b},\bar{R}_{q}<\tau,o_{h}\in S\}$ {Self-Reflection: Augment hard queries with guided prompts}
L119: 
L120: 4:    end if
L121: 5:    Sample group $G=\{o_{i}\}_{i=1}^{G}\sim\pi_{\theta}(\cdot\mid\mathcal{D}_{b})$
L122: 
L123: 6:    if all $o_{i}\in G$ are negative then
L124: 
L125: 7:     Calculate rewards $\mathcal{R}_{(k)}$ via entropy $\mathcal{E}_{\text{peak}}^{(i)},\mathcal{E}_{\text{global}}^{(i)}$ for truncated response; $G\leftarrow G\cup S_{pos}$ {Rank neg. samples via entropy; Retrieve pos. samples}
L126: 
L127: 8:    else if all $o_{i}\in G$ are positive then
L128: 
L129: 9:     $G\leftarrow G\cup S_{neg}$ {Retrieve neg. samples to form contrastive pairs}
L130: 10:    end if
L131: 
L132: 11:    Update Buffer $S\leftarrow S\cup\mathcal{D}_{b}$
L133: 
L134: 12:    Update $\theta$ by maximizing R³ objective on $G$
L135: 
L136: 13:  end for
L137: ### 3.2 R³: Reflection, Replay, and Ranking Rewards
L138: The R³ framework operates on a foundation of historical experience, facilitated by a centralized sample buffer. This buffer serves as a structured repository designed to archive reasoning trajectories, providing the necessary data for cross-text learning. Each entry in the buffer comprises a query, its generated response, and the associated reward, all indexed by a unique identifier (UID) to ensure precise retrieval and traceability.
L139: Leveraging the sample buffer, R³ synergizes Cross-Context Replay (CCR) and In-Context Self-Reflection (ISR) to mitigate advantage collapse and significantly enhance sample efficiency.
L140: #### 3.2.1 Cross-Context Replay
L141: Inspired by the dynamic sampling strategy in DAPO cite40†Yu et al. (2025) , which filters out groups with 0 or 1 accuracy to ensure effective gradients, we propose a more sample-efficient alternative. Instead of discarding these zero-variance groups, we seek to actively utilize them via Cross-Context Replay (CCR).
L142: By injecting historical trajectories into these homogeneous batches, CCR restores the necessary variance for gradient estimation, ensuring that no computational resources are wasted on valid but uniform samples.
L143: During the replay phase, we first identify queries where advantage collapse occurs due to identical rewards across all responses in group $G$. Using the unique identifier (UID) of the query, we access the sample buffer to retrieve historical trajectories associated with the same input.
L144: We specifically target samples with ”opposing” rewards to construct contrastive pairs: if the current group consists entirely of negative responses (reward 0), we retrieve $k$ historical samples (reward 1); conversely, if the group is fully correct, we introduce failed attempts to re-establish a learning signal. By integrating these off-policy samples into group $G$, we achieve cross-context fusion.
L145: This explicitly restores the reward variance, ensuring the computation of a non-trivial advantage and facilitating effective training even in cases of mode collapse.
L146: #### 3.2.2 In-Context Self-Reflection
L147: 
L148: To mitigate persistent reasoning failures, we introduce In-Context Self-Reflection (ISR), a strategy designed to augment queries with diagnostic context derived from historical errors.
L149: During training, for each query $q_{i}$ in a batch, the framework queries the sample buffer to retrieve its historical execution trajectories and corresponding rewards $\{R_{i,j}\}_{j=1}^{n}$. If the average historical performance $\operatorname{mean}\{R_{i,j}\}_{j=1}^{n}$ falls below a predefined threshold $\tau$, $q_{i}$ is categorized as a hard query. For such cases, we construct self-reflection exemplars by randomly sampling from the historical errors stored in the buffer.
L150: Each exemplar integrates the original query, the sampled erroneous response, and a structured reflection guidance to facilitate diagnostic reasoning. This mechanism compels the model to perform a diagnostic analysis of its past failures, thereby facilitating self-correction and preventing the recurrence of similar reasoning pitfalls in subsequent iterations.
L151: #### 3.2.3 Structural Entropy Ranking Reward
L152: During the sampling phase of reinforcement learning, hard queries often results in truncated responses due to maximum generation length constraints. Motivated by the analysis in cite60†Wang et al. (2025d) , which reveals that high-entropy tokens serve as ”forking points” guiding divergent reasoning paths while low-entropy tokens primarily facilitate step completion, we posit that these entropy variations fundamentally reflect the trade-off between exploration and stability in reasoning.
L153: Leveraging this insight to derive reliable supervision signals for truncated solutions to challenging problems, we propose an unsupervised intrinsic reward termed structural entropy ranking reward (SERR). Designed to provide meaningful learning signals when verifiable rewards are unavailable, SERR leverages this insight to capture the trade-off between exploration and stability.
L154: Specifically, we posit that an effective reasoning trajectory should exhibit a structural balance, where high-entropy forking points drive necessary exploration, while low-entropy tokens ensure the stability of step completion.
L155: We formulate two complementary entropy-based metrics to characterize the uncertainty of a generated response $o_{i}$ with length $L_{i}$.
L156: 
L157:   * •
L158: 
L159: Peak Entropy ($\mathcal{E}_{\text{peak}}$): Captures the intensity of divergent reasoning at critical decision steps. Aligning with the concept of ”forking points,” this metric quantifies the model’s capacity for exploration.
L160: 
L161:  | $$\mathcal{E}_{\text{peak}}^{(i)}=\frac{1}{|\mathcal{K}_{i}|}\sum_{t\in\mathcal{K}_{i}}H(o_{i,t}),$$  |
L162: where $H(o_{i,t})$ denotes the entropy of token $t$, and $\mathcal{K}_{i}$ represents the set of indices for the top-$k_{i}$ most uncertain tokens in response $o_{i}$. The set size is determined by $k_{i}=\max(1,\lfloor p\cdot L_{i}\rfloor)$, with $p$ being a predefined selection ratio controlling the proportion of tokens considered as critical branching points.
L163: 
L164:   * •
L165: Global Entropy ($\mathcal{E}_{\text{global}}$): Reflects the structural stability of the trajectory. Since effective reasoning relies on low-entropy tokens to facilitate consistent step completion, this metric serves as a proxy for the overall coherence of the sequence length $L_{i}$, ensuring that exploration remains controlled.
L166: 
L167:  | $$\mathcal{E}_{\text{global}}^{(i)}=\frac{1}{L_{i}}\sum_{t=1}^{L_{i}}H(o_{i,t}).$$  |
L168: 
L169: where $L_{i}$ is the number of non-padding tokens.
L170: To assign a score to each sample, we define the partial order as $i\succ j$ if $\mathcal{E}_{\text{peak}}^{(i)}>\mathcal{E}_{\text{peak}}^{(j)}$ and $\mathcal{E}_{\text{global}}^{(i)}<\mathcal{E}_{\text{global}}^{(j)}$. Each sample receives a score based on how many other samples it dominates under this partial ordering:
L171: 
L172:  | $$S_{i}=\sum_{j\neq i}\mathbf{1}\left[i\succ j\right]$$  |
L173: Finally, we convert scores into scalar rewards by sorting all samples according to $S_{i}$ and assigning linearly scaled rewards from a maximum value $R_{\text{max}}$:
L174: 
L175:  | $$\mathcal{R}_{(k)}=R_{\text{max}}\cdot\left(1-\frac{k}{N-1}\right)$$  |
L176: 
L177: where $\mathcal{R}_{(k)}$ represents the reward assigned to the sample with the $k$-th highest rank.
L178: #### 3.2.4 Optimization
L179: 
L180: The excessive integration of off-policy historical data with on-policy samples can undermine the strength of the current on-policy learning signal. Therefore, when computing the advantage for the mixed group $G_{\text{mix}}$, we apply a predefined scaling factor $\alpha$ to adjust the contribution of the off-policy samples. Based on the mixed group $G_{\text{mix}}$, the advantage is calculated as follows:

## Original cached response recovered by existing ref turn28176view0

R³: Replay, Reflection, and Ranking Rewards for LLM Reinforcement Learning (https://arxiv.org/html/2601.19620v1)
citeturn28401view2 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: open({"ref_id":"turn28176view0","lineno":100}); Total lines: 337
L87: (2025a)】 further introduces an exploration–filter–replay loop to enable stable GRPO training. Several methods leverage selective replay to overcome vanishing advantages and on-policy limitations. LUFFY cite55†Yan et al. (2025) combines replayed demonstrations with on-policy rollouts to improve weak models. In multimodal and slow-thinking settings, VL-Rethinker cite56†Wang et al. (2025b) and Skywork R1V2 cite57†Wang et al. (2025c) adopt selective replay buffers to prioritize informative trajectories.
L88: ### 2.3 Entropy-Driven Exploration in Reinforcement Learning
L89: Entropy is a central driver of exploration in RL cite58†Haarnoja et al. (2018) ; cite39†Schulman et al. (2017) . In LLM training, policy entropy is observed to collapse early, limiting exploration and causing premature performance saturation cite59†Cui et al. (2025) . Token-level analyses reveal that a small set of high-entropy “forking tokens” disproportionately influences reasoning diversity, and selectively updating these tokens improves efficiency and generalization cite60†Wang et al. (2025d) .
L90: High-entropy regions are also linked to key reasoning behaviors such as logical pivots and self-verification cite61†Cheng et al. (2025) . To mitigate entropy collapse, several entropy-aware training frameworks have been proposed cite62†Zheng et al. (2025) ; cite63†Voelcker et al. (2025) . Most existing approaches, however, rely on dense supervision or discard incomplete reasoning traces.
L91: In contrast, our work introduces a fully unsupervised trajectory-level reward structural entropy ranking reward which evaluates partially correct or truncated reasoning paths based on their internal entropy structure, enabling effective learning beyond final-answer supervision.
L92: cite64†Image: Refer to caption Figure 2: Overview of the R³ architecture.
L93: From left to right: (1) For hard queries from prior rounds, perform in-context self-reflection by retrieving historical samples from the sample buffer; (2) The policy model outputs a response, which is then passed through a verifier to assess its quality; (3) Cross-context replay leverages historical samples from the buffer to enhance advantage estimation; (4) Truncated responses are evaluated using the structural entropy ranking reward, which is then used for advantage computation.
L94: ## 3 Methodology
L95: ### 3.1 Preliminaries: Group Relative Policy Optimization (GRPO).
L96: 
L97: Given an input question $q$, the policy model $\pi_{\theta}$ generates a group of $G$ responses $\{o_{i}\}_{i=1}^{G}$ by sampling $G$ times from its output distribution. GRPO constructs a group-level reward $\{R_{i}\}_{i=1}^{G}$ from the set of sampled responses $\{o_{i}\}_{i=1}^{G}$ for the question $q$, and utilizes $\{R_{i}\}_{i=1}^{G}$ to compute the corresponding advantage for policy optimization.
L98:  | $$\hat{A}_{i}=\frac{R_{i}-\operatorname{mean}(\{R_{i}\}_{i=1}^{G})}{\operatorname{std}(\{R_{i}\}_{i=1}^{G})}.$$  |  | (1)
L99: 
L100: The optimization objective of GRPO with the group-level advantage is given by the following equation:
L101:  | $\displaystyle\footnotesize\mathcal{J}_{\text{GRPO}}(\theta)=\mathbb{E}_{o\sim\pi_{\theta}}\Big[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\min\Big(r_{i}(\theta)\hat{A_{i}},$  |
L102:  | $\displaystyle\hskip 0.0pt\text{clip}\left(r_{i}(\theta),1-\epsilon,1+\epsilon\right)\hat{A_{i}}-{\beta}D_{KL}(\pi_{\theta}||\pi_{ref})\Big)\Big]$  |  | (2)
L103: where $r_{i}(\theta)=\frac{\pi_{\theta}(o_{i}\mid q)}{\pi_{\theta_{\text{old}}}(o_{i}\mid q)},$ $\pi_{old}$ is the previous policy model, $\epsilon$ is the clipping coefficient and $D_{KL}$ represent computing Kullback-Leibler (KL) divergence cite49†Kullback and Leibler (1951) between policy model $\pi_{\theta}$ and reference model $\pi_{ref}$.
L104: While GRPO effectively stabilizes training without a critic, it fundamentally relies on intra-group reward variance to estimate advantages. As indicated in Eq. (cite65†1 ), a critical limitation arises when all sampled responses within a group yield identical rewards. In such scenarios, the standard deviation $\operatorname{std}(\{R_{i}\}_{i=1}^{G})$ vanishes, leading to advantage collapse. This results in uninformative gradients that hinder policy updates and impair training efficiency.
L105: To address these challenges, we propose a stratified strategy tailored to queries of varying difficulty levels: (1) For medium-difficulty queries, where the model may yield homogeneous outcomes (e.g., all correct or all incorrect) within a single sampling round, relying solely on intra-group variance leads to advantage collapse.
L106: We employ Cross-Context Replay (CCR) to inject historical samples with opposing rewards, thereby ensuring continuous gradient updates by artificially reconstructing the advantage gap. (2) For hard queries characterized by persistent failure, we introduce In-Context Self-Reflection (ISR) to explicitly guide the model toward self-correction and reasoning refinement.
L107: (3) Finally, for extremely hard queries resulting in truncated responses where verifiable outcome rewards are unavailable, we utilize the Structural Entropy Ranking Reward (SERR) to provide a meaningful training signal based on the reasoning process.
L108: Algorithm 1 R³ Algorithm
L109: 
L110: 0:  Task Prompts $\mathcal{D}$; Policy $\pi_{\theta}$; Buffer $S$; Parameters $E,\tau,p_{r}$
L111: 
L112: 0:  Optimized Policy $\pi_{\theta}$
L113: 
L114: 1:  for $epoch=1:E$ and $\mathcal{D}_{b}\in\mathcal{D}$ do
L115: 
L116: 2:    if $epoch>1$ then
L117: 
L118: 3:     $\mathcal{D}_{b}\leftarrow\mathcal{D}_{b}\cup\{q\oplus o_{h}\oplus p_{r}\mid q\in\mathcal{D}_{b},\bar{R}_{q}<\tau,o_{h}\in S\}$ {Self-Reflection: Augment hard queries with guided prompts}
L119: 
L120: 4:    end if
L121: 5:    Sample group $G=\{o_{i}\}_{i=1}^{G}\sim\pi_{\theta}(\cdot\mid\mathcal{D}_{b})$
L122: 
L123: 6:    if all $o_{i}\in G$ are negative then
L124: 
L125: 7:     Calculate rewards $\mathcal{R}_{(k)}$ via entropy $\mathcal{E}_{\text{peak}}^{(i)},\mathcal{E}_{\text{global}}^{(i)}$ for truncated response; $G\leftarrow G\cup S_{pos}$ {Rank neg. samples via entropy; Retrieve pos. samples}
L126: 
L127: 8:    else if all $o_{i}\in G$ are positive then
L128: 
L129: 9:     $G\leftarrow G\cup S_{neg}$ {Retrieve neg. samples to form contrastive pairs}
L130: 10:    end if
L131: 
L132: 11:    Update Buffer $S\leftarrow S\cup\mathcal{D}_{b}$
L133: 
L134: 12:    Update $\theta$ by maximizing R³ objective on $G$
L135: 
L136: 13:  end for
L137: ### 3.2 R³: Reflection, Replay, and Ranking Rewards
L138: The R³ framework operates on a foundation of historical experience, facilitated by a centralized sample buffer. This buffer serves as a structured repository designed to archive reasoning trajectories, providing the necessary data for cross-text learning. Each entry in the buffer comprises a query, its generated response, and the associated reward, all indexed by a unique identifier (UID) to ensure precise retrieval and traceability.
L139: Leveraging the sample buffer, R³ synergizes Cross-Context Replay (CCR) and In-Context Self-Reflection (ISR) to mitigate advantage collapse and significantly enhance sample efficiency.
L140: #### 3.2.1 Cross-Context Replay
L141: Inspired by the dynamic sampling strategy in DAPO cite40†Yu et al. (2025) , which filters out groups with 0 or 1 accuracy to ensure effective gradients, we propose a more sample-efficient alternative. Instead of discarding these zero-variance groups, we seek to actively utilize them via Cross-Context Replay (CCR).
L142: By injecting historical trajectories into these homogeneous batches, CCR restores the necessary variance for gradient estimation, ensuring that no computational resources are wasted on valid but uniform samples.
L143: During the replay phase, we first identify queries where advantage collapse occurs due to identical rewards across all responses in group $G$. Using the unique identifier (UID) of the query, we access the sample buffer to retrieve historical trajectories associated with the same input.
L144: We specifically target samples with ”opposing” rewards to construct contrastive pairs: if the current group consists entirely of negative responses (reward 0), we retrieve $k$ historical samples (reward 1); conversely, if the group is fully correct, we introduce failed attempts to re-establish a learning signal. By integrating these off-policy samples into group $G$, we achieve cross-context fusion.
L145: This explicitly restores the reward variance, ensuring the computation of a non-trivial advantage and facilitating effective training even in cases of mode collapse.
L146: #### 3.2.2 In-Context Self-Reflection
L147: 
L148: To mitigate persistent reasoning failures, we introduce In-Context Self-Reflection (ISR), a strategy designed to augment queries with diagnostic context derived from historical errors.
L149: During training, for each query $q_{i}$ in a batch, the framework queries the sample buffer to retrieve its historical execution trajectories and corresponding rewards $\{R_{i,j}\}_{j=1}^{n}$. If the average historical performance $\operatorname{mean}\{R_{i,j}\}_{j=1}^{n}$ falls below a predefined threshold $\tau$, $q_{i}$ is categorized as a hard query. For such cases, we construct self-reflection exemplars by randomly sampling from the historical errors stored in the buffer.
