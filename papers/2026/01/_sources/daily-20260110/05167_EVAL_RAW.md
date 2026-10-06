RelayLLM: Efficient Reasoning via Collaborative Decoding (https://arxiv.org/html/2601.05167v1)
citeturn26873view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.05167v1","lineno":178}); Total lines: 399
L117: This binary scheme is effective for tasks with unambiguous success criteria, such as mathematical problem-solving. In our setting, we design a corresponding rule-based reward to verify model-generated relations, described in Sec. cite16†3.2.3 .
L118: To optimize the policy using these rewards, GRPO samples a group of outputs $\{o_{i}\}_{i=1}^{G}$ for each query $q$ from the old policy $\pi_{\theta_{\mathrm{old}}}$ and evaluates them relative to the group average. The training objective is formulated as:
L119: 
L120:  | $$\mathcal{J}_{\mathrm{GRPO}}(\theta)=\mathbb{E}_{q\sim\mathcal{D}}\left[\frac{1}{G}\sum_{i=1}^{G}\left(\mathcal{M}_{i}-\beta\mathbb{D}_{\mathrm{KL}}\right)\right],$$  |  | (1)
L121: where $\mathbb{D}_{\mathrm{KL}}=D_{\mathrm{KL}}(\pi_{\theta}\parallel\pi_{\mathrm{ref}})$ is the regularization term. The surrogate objective $\mathcal{M}_{i}$ is computed as $\min(\rho_{i}A_{i},\mathrm{clip}(\rho_{i},1-\epsilon,1+\epsilon)A_{i})$, where $\rho_{i}=\frac{\pi_{\theta}(o_{i}|q)}{\pi_{\theta_{\mathrm{old}}}(o_{i}|q)}$. The advantage $A_{i}$ is derived from the group-normalized rewards defined below:
L122:  | $$A_{i}=\frac{r_{i}-\mathrm{mean}(\{r_{j}\})}{\mathrm{std}(\{r_{j}\})+\varepsilon_{\mathrm{stab}}},$$  |  | (2)
L123: 
L124: where $\varepsilon_{\mathrm{stab}}$ is a small constant for stability. This formulation encourages the model to generate responses that outperform the group average.
L125: #### 3.2.2 Data Filtering
L126: Since our method leverages the large model to generate reasoning paths or feedback, it is essential to identify the subset of data where such intervention is useful. If the large model consistently fails to solve a query, calling it during training yields no positive gain. Therefore, we preprocess the dataset to filter out instances that are too hard for the large model. We sample 10 responses per query and only preserve those with a pass rate of $\geq 50\%$.
L127: This step ensures that the training data lies in the competence boundary of the large model and the responses can contribute effectively. We provide an ablation study on this filtering mechanism in Table cite71†3 .
L128: #### 3.2.3 Reward Design
L129: 
L130: We formulate the optimization objective using two distinct reward signals, a simple reward and our designed difficulty-aware reward. Let $y$ be the response, $a$ be the final answer parsed from $y$, $g$ be the ground truth, and $\rho(y)\in[0,1]$ be the call ratio (the ratio of large-model generated tokens to the total response length.).
L131: ##### Simple Reward.
L132: 
L133: We define a straightforward reward to encourage both accuracy and efficiency:
L134: 
L135:  | $$r_{\text{simple}}(y)=\mathbb{1}(a=g)-\rho(y).$$  |  | (3)
L136: 
L137: where $\mathbb{1}(\cdot)$ is the indicator function, thus the responses are scored by their correctness and penalized by the cost of calling the expert model.
L138: ##### Difficulty-Aware Reward.
L139: 
L140: To capture the relative difficulty of each query, we define the reward based on the collective performance of the sampled group $\mathcal{G}$. We categorize each query into three scenarios based on its difficulty (correctness of responses in $\mathcal{G}$). As illustrated in Figure cite69†2 (Right), we provide concrete examples of how these rewards are assigned across different categories.
L141: ##### Scenario 1: Student-Solvable (Encouraging Independence).
L142: This scenario applies when the student model is capable of solving the query independently, without assistance from the large model. This scenario is identified if there exists at least one sample in the group $\mathcal{G}$ that answers correctly without invoking the large model. In this case, calling the teacher is deemed redundant.
L143: Consequently, we assign a boosted bonus ($r=1.5$) for independent success to promote efficiency and independence, while dependent success ($\rho(y)>0$) still receives the simple reward $r_{\text{simple}}$ in Eq.(cite72†3 ), and incorrect responses receive zero reward.
L144: ##### Scenario 2: Teacher-Dependent (Penalizing Stubbornness).
L145: 
L146: This scenario represents challenging queries where correct answers appear only in samples that call the large model. Here, the small model’s independent reasoning is insufficient. To discourage blind guessing, we impose a penalty on samples that fail to call the teacher ($r=-1.0$ when $\rho(y)=0$). Conversely, effective expert calling that leads to a correct answer is rewarded with $r_{\text{simple}}$.
L147: ##### Scenario 3: Teacher-Unsolvable (Incentivizing Exploration).
L148: This scenario occurs when no sample in $\mathcal{G}$ yields the correct answer, indicating that the query is extremely difficult or the teacher’s guidance was ineffective. Rather than providing zero training signal for all responses, we assign a small exploration reward ($r=\rho(y)$) to samples that attempted to call the large model. This reinforces the tendency to seek help in highly uncertain situations.
L149: This piecewise design aligns the policy with an optimal strategy: solve independently when possible, seek help when necessary, and avoid costly errors.
L150: ## 4 Experiments
L151: ### 4.1 Experimental Setup
L152: Table 1: Performance comparison on six benchmarks. We compare the effectiveness of RelayLLM using Qwen3-0.6B and Qwen3-1.7B as student models across different methods: the standard Base model, the GRPO-tuning baseline, CITER and RelayLLM (Simple-Reward and Difficulty-Aware-Reward). The Qwen3-8B teacher model performance is provided for reference. We report avg@32 for the challenging AIME datasets and standard pass@1 (greedy decoding) for all other benchmarks. The “Avg.
L153: Call Ratio” denotes the percentage of tokens generated by the teacher model during the collaborative inference process. The best results within each model group are highlighted in bold.
L154: Model  | Minerva  | MATH500  | GSM8K  | Olympiad  | AIME25  | AIME24  | Average  | Avg. Call Ratio
L155: Qwen3-0.6B
L156: ---
L157: Base Model  | 15.81  | 54.00  | 64.82  | 26.22  | 1.04  | 1.15  | 27.17  | –
L158: GRPO  | 17.65  | 58.60  | 65.50  | 29.04  | 5.42  | 3.23  | 29.91  | –
L159: CITER  | 19.29  | 58.80  | 67.78  | 29.60  | 5.93  | 3.24  | 30.77  | 0.98%
L160: RelayLLM (Simple)  | 20.96  | 60.20  | 69.14  | 32.15  | 7.19  | 3.85  | 32.25  | 0.31%
L161: RelayLLM (Difficulty-Aware)  | 23.53  | 60.00  | 71.95  | 32.74  | 6.15  | 3.85  | 33.04  | 0.77%
L162: Qwen3-1.7B
L163: ---
L164: Base Model  | 33.82  | 74.60  | 82.64  | 43.11  | 8.75  | 12.08  | 42.50  | –
L165: GRPO  | 35.66  | 75.60  | 81.73  | 45.04  | 10.73  | 15.62  | 44.06  | –
L166: CITER  | 38.63  | 80.24  | 82.26  | 51.20  | 11.96  | 16.58  | 46.81  | 1.34%
L167: RelayLLM (Simple)  | 43.01  | 83.40  | 86.13  | 51.56  | 13.44  | 18.23  | 49.30  | 0.43%
L168: RelayLLM (Difficulty-Aware)  | 43.75  | 81.40  | 86.28  | 55.70  | 12.71  | 17.29  | 49.52  | 1.07%
L169: Qwen3-8B  | 48.16  | 83.20  | 93.63  | 56.89  | 17.92  | 24.90  | 54.12  | 100%
L170: #### 4.1.1 Models
L171: To evaluate the effectiveness of RelayLLM, we utilize the Qwen3 model family (cite54†Yang et al., 2025a ) due to its consistent architectural scaling and strong performance across various sizes. We select Qwen3-0.6B and Qwen3-1.7B as our primary small language models ($\mathcal{M}_{S}$) to investigate how our framework scales with model capacity at the sub-2B parameter level. For the teacher model ($\mathcal{M}_{L}$), we utilize Qwen3-8B.
L172: Selecting a model from the same model family ensures that the generation style, token distribution, vocabulary and tokenizer are more consistent, making collaboration more stable. To optimize training and inference efficiency, we consistently run the models in non-thinking mode.
L173: ### 4.2 Evaluation Setup
L174: To evaluate the effectiveness of  RelayLLM, we conduct experiments on six reasoning benchmarks, and compare our approach against the standard GRPO baseline. We also add CITER (cite73†Zheng et al., 2025b ), a token-level routing method as the baseline method which requires an additional controller. The benchmarks include Minerva (cite74†Lewkowycz et al., 2022 ), MATH-500 (cite75†Hendrycks et al., 2021 ), GSM8K (cite76†Cobbe et al., 2021 ), Olympiad-Bench (cite77†He et al., 2024 ), AIME-2024, and AIME-2025.
L175: We use GPT-4o-mini as a semantic judge to verify the model’s output against the ground truth (cite78†Zhao et al., 2025 ). For the high-difficulty AIME datasets, we report the avg@32 metric to ensure a robust evaluation. For other benchmarks, we report standard accuracy (pass@1) using greedy decoding.
L176: ### 4.3 Training Details
L177: We conduct our experiments using the DAPO dataset (cite79†Yu et al., 2025a ). Our implementation is built upon the EasyR1 framework (cite80†Zheng et al., 2025c ) using its default hyperparameter configurations (shown in App. cite50†E ). All models are trained for a single epoch to ensure a fair comparison. Regarding data usage, the GRPO baseline is trained on the full dataset, whereas our method utilizes the filtered subset as described in Section cite15†3.2.2 .
L178: To enable efficient interaction with the large model, we serve the teacher model via the vLLM inference engine (cite81†Kwon et al., 2023 ). We implement the switching mechanism as a stop sequence in the sampling parameters: when the model generates the calling command token, generation halts, and the system invokes the teacher model via the API.
L179: ### 4.4 Main Results
L180: As presented in Table cite82†1 , RelayLLM demonstrates a superior trade-off between reasoning capability and inference efficiency. First, our method achieves substantial performance improvements across all benchmarks while maintaining a negligible collaborative cost (less than 1% token overhead).
L181: For instance, on the challenging Minerva benchmark, the Qwen3-0.6B model with Difficulty-Aware-Reward improves from a base score of 15.81% to 23.53%, representing a relative improvement of approximately 48.8% while invoking the large model for only 0.77% of the total tokens. Compared to CITER, our method demonstrates superior performance despite CITER’s more computationally intensive design.
L182: CITER relies on an external MLP to estimate a score every token, which introduces substantial latency and computational overhead. In contrast, RelayLLM achieves better results with a significantly more efficient mechanism at the cost of only several addtional tokens.
L183: Second, comparing optimization strategies, the Difficulty-Aware-Reward mechanism outperforms the Simple-Reward in performance, with a marginal increase in token consumption.
L184: For the Qwen3-1.7B model, the Difficulty-Aware-Reward strategy achieves a higher average accuracy of 49.52% compared to 49.30% for the Simple-Reward, which correlates with a slight increase in the average call ratio from 0.43% to 1.07%, suggesting that the difficulty-based signal better incentivizes the model to seek help in complex scenarios.
L185: Finally,  RelayLLM  effectively bridges the capability gap between small and large models using minimal tokens. Remarkably, the Qwen3-1.7B (Difficulty-Aware) recovers approximately 60% of the performance gap between the base SLM (42.50%) and the expert model (54.12%), highlighting that sparse, strategic intervention at critical reasoning steps is sufficient to unlock a significant portion of the teacher model’s potential.
L186: ## 5 Analysis
L187: 
L188: In this section, we conduct a series of in-depth analyzes to better understand the behavior and effectiveness of RelayLLM framework.
L189: ### 5.1 RelayLLM Generalizes to Unseen Reasoning Domains
L190: To verify the generalization capability of RelayLLM, we extended our evaluation to general reasoning domains that were unseen during training. Although our model was trained exclusively on the mathematical DAPO dataset, we tested it on three diverse benchmarks out of the math domain: Big-Bench Hard (BBEH) (cite83†Kazemi et al., 2025 ), MMLU-Pro (cite84†Wang et al., 2024 ), and SuperGPQA (cite85†Du et al., 2025 ). As shown in Table cite86†2 , RelayLLM consistently outperforms baseline methods despite the domain shift.
L191: For instance, using Qwen3-1.7B, our method achieves 59.03% on MMLU-Pro, significantly surpassing the GRPO baseline (49.76%) and CITER (53.38%). These results demonstrate that our framework effectively help SLM have a generalized help-seeking behavior; even when facing unfamiliar inputs, the SLM successfully recognizes its knowledge gaps and invoke the LLM, leading to substantial performance gains in out-of-distribution tasks.
L192: Table 2: Performance comparison on reasoning and general knowledge benchmarks. We evaluate the effectiveness of RelayLLM using Qwen3-0.6B and Qwen3-1.7B as student models across different settings. The Qwen3-8B performance is provided for reference. The best results within each model group are highlighted in bold.
L193: Model  | BBEH  | MMLU-Pro  | SuperGPQA
L194: Qwen3-0.6B
L195: ---
L196: Base Model  | 7.19  | 30.03  | 17.22
L197: GRPO  | 7.82  | 32.15  | 19.91
L198: CITER  | 8.16  | 33.12  | 20.34
L199: RelayLLM (Simple)  | 8.32  | 35.61  | 21.35
L200: RelayLLM (Difficulty-Aware)  | 8.56  | 35.87  | 20.88
L201: Qwen3-1.7B
L202: ---
L203: Base Model  | 9.91  | 46.90  | 24.46
L204: GRPO  | 10.89  | 49.76  | 26.01
L205: CITER  | 11.67  | 53.38  | 28.25
L206: RelayLLM (Simple)  | 12.67  | 58.76  | 29.85
L207: RelayLLM (Difficulty-Aware)  | 12.46  | 59.03  | 29.93
L208: Qwen3-8B  | 15.31  | 66.46  | 36.21
L209: ### 5.2 Ablation Study
L210: 
L211: To investigate the distinct contribution of each component in RelayLLM , we conducted an ablation study using the Qwen3-1.7B model in Table cite71†3 .
L212: ##### Data filtering prevents wasteful calls where teacher models fail.
L213: 
L214: We show that removing the data filtering mechanism results in a tripled call ratio with decreased accuracy; this confirms that filtering out queries intractable for the teacher is crucial to avoid cost that yield no performance gain. Filtering out some too hard data also save time and resources during the training stage.
L215: ##### Encouraging independence reduces reliance on teacher model and improves efficiency.
L216: 
L217: We remove the independence encouraging (where we boosted correctness reward from $1$ to $1.5$ for solvable queries), and this causes the call ratio to spike to 4.10%. This demonstrates that specifically rewarding the independent success is crucial to prevent the model from becoming over-reliant on the expert LLM for tasks it could solve alone.
L218: ##### Exploration reward effectively increases accuracy.
L219: 
L220: When we remove the exploration reward (for unsolvable queries), this leads to a significant accuracy drop to 47.56%, indicating that the exploration reward is necessary to encourage the model to call for help from teacher models in highly uncertain scenarios.
L221: Table 3: Ablation study on data filtering and reward design strategies using Qwen3-1.7B. “w/o Data Filtering” denotes training on the unfiltered dataset including teacher-failed queries. “w/o Indep. Incentive” removes the bonus reward (from $1.5$ to $1$) for independent success (Scenario 1). “w/o Explor. Reward” removes the exploration reward (from $\rho$ to $0$) for seeking help in unsolvable queries (Scenario 3).
L222: Method  | Avg. Acc. (%)  | Call Ratio (%)
L223: --- | --- | ---
L224: RelayLLM  | 49.52  | 1.07
L225:    w/o Data Filtering  | 48.76  | 3.30
L226:    w/o Indep. Incentive  | 49.34  | 4.10
L227:    w/o Explor. Reward  | 47.56  | 0.65
L228: ### 5.3 Intrinsic Reasoning Capability
L229: To investigate whether  RelayLLM  improves the student’s inherent reasoning or merely learns to offload tasks, we evaluate the models in a “Teacher-Free” setting by strictly forbidding invocations during inference (implemented via bad_words=[‘‘<call>’’, ‘‘</call>’’] when inference). Results in Table cite87†4 reveal three key insights. First, on Easy datasets, even without teacher access,  RelayLLM  (Simple-Reward) achieves 61.12%, surpassing the GRPO baseline.
L230: This suggests that the student model has successfully learn from the reasoning ability of the expert model during the collaborative training process.
L231: On Harder datasets, removing the teacher leads to a notable performance drop (e.g., Difficulty-Aware-Reward falls from 15.00% to 11.93%), confirming that for complex tasks, the model remains heavily dependent on expert intervention. Third, comparing reward schemes, the Simple-Reward variant demonstrates stronger capabilities than the Difficulty-Aware-Reward variant.
L232: This aligns with our previous observation that Difficulty-Aware-Reward encourages a higher call ratio, leading to a stronger dependency on the teacher, whereas Simple-Reward retains more independence.
L233: Table 4: Evaluation of intrinsic reasoning capability. We disable the teacher during inference (“w/o Teacher”) by masking the call tokens. “Hard” refers to AIME24 and AIME25, while “Easy” refers to the remaining.
L234: Method  | Easy (%)  | Hard (%)
L235: GRPO Baseline  | 59.51  | 13.18
L236: RelayLLM  (Simple)
L237: ---
L238:    Standard Inference  | 66.03  | 15.84
L239:    w/o Teacher  | 61.12  | 13.13
L240: RelayLLM  (Difficulty-Aware)
L241: ---
L242:    Standard Inference  | 66.78  | 15.00
L243:    w/o Teacher  | 60.26  | 11.93
L244: Table 5: Comparison between dynamic length prediction (RelayLLM) and fixed delegation length strategies. Note that “Fixed-$k$” does not simply denote inference truncation; these models were retrained with the constraint to always request $k$ tokens, ensuring they learned optimal policies for those specific lengths.
L245: Method  | Avg. Acc. (%)  | Call Ratio (%)
L246: --- | --- | ---
L247: Fixed-20  | 49.41  | 1.32
L248: Fixed-100  | 49.56  | 2.87
L249: Fixed-500  | 51.17  | 5.37
L250: RelayLLM  | 49.52  | 1.07
L251: ### 5.4 Dynamic Token-Length Calling Minimizes Computational Cost
L252: We investigate whether dynamically predicting the calling length $n$ requested from the large model is superior to using rigid, pre-defined lengths. To ensure a fair evaluation, we retrained separate variations of the student model where the call command is hard-constrained to a fixed token count $k\in\{20,100,500\}$ during both training and inference. As shown in Table cite88†5 ,  RelayLLM  demonstrates superior efficiency compared to these specialized fixed-length models.
L253: Specifically, compared to the Fixed-100 model,  RelayLLM  achieves a similar accuracy but reduces the call ratio from 2.87% to 1.07%. This indicates that while the fixed-length model is forced to consume a set budget even for simple queries,  RelayLLM  effectively learns to request “just enough” tokens to bridge the reasoning gap, thereby minimizing computational waste without compromising performance. We provide a more detailed results in Appendix cite43†B .
L254: Figure 3: Impact of teacher model size on student performance. We evaluate two student models (Difficulty-Aware) across six benchmarks. The x-axis represents the size of the teacher model used during the collaborative inference process, ranging from "None" (the same as Sec. cite34†5.3 , prevent model to call teacher model) to 14B. The reported scores are averaged across all six datasets.
L255: ### 5.5 Distributional Alignment
L256: To determine whether the student model has acquired generalized reasoning capabilities or merely overfitted to the specific patterns and words of the LLM in training time, we performed a cross-LLM evaluation by substituting the training teacher with different models in the inference phase. The results, illustrated in Figure cite89†3 , reveal two critical insights. First, consistency with the training LLM yields optimal performance.
L257: The accuracy peaks when the inference teacher matches the training teacher, reaching 49.52% for the 1.7B student. Notably, replacing it with a larger model results in a slight performance decline. This indicates that the distribution shift between the training and inference teachers can outweigh the benefits of the larger model’s superior reasoning capabilities.
L258: Second, even employing a relatively weak teacher that is weaker than itself (e.g., 0.6B or 1.7B) consistently outperforms the “None” baseline. This suggests that the trained model has become accustomed to the presence of external assistance, adapting its generation dynamics to effectively leverage such interventions rather than relying solely on its intrinsic capabilities.
L259: Furthermore, excluding the distribution shift at 8B, which is we used in training, there is a positive correlation between teacher size and student performance, confirming that the student effectively leverages the stronger reasoning signals provided by more capable experts.
L260: ## 6 Related Work
L261: ### 6.1 Model Collaboration
L262: Model collaboration (cite90†Feng et al., 2025a ) ranges from weight-level merging (cite91†Wortsman et al., 2022 ; cite92†Huang et al., 2023 ) and logits-level ensembling (cite93†Liu et al., 2024 ; cite94†Li et al., 2023 ) to text-level interaction. Recent research has focused on navigating the efficiency trade-off between large and small models, which can be broadly categorized into two directions. The first direction involves speculative reasoning. cite95†Bachmann et al. (2025) and cite96†Pan et al.
L263: (2025) employ judge mechanisms or verifiers to validate small model outputs, effectively acting as dynamic routers. Similarly, large model guidance is leveraged to enhance small model reasoning specifically at inference time (cite97†Yang et al., 2025b ; cite98†Zhang et al., 2025 ). The second direction focuses on collaborative decoding (cite63†Shen et al., 2024 ) with interleaved generation via an additional controller. cite63†Shen et al. (2024) ; cite99†Sun et al.
L264: (2024b) proposed learning a joint policy for multiple models. Strategic intervention is further investigated by cite100†Li et al. (2025a) ; cite101†Feng et al. (2025b) ; cite102†Fu et al. (2025) to explore thought spaces efficiently.
L265: ### 6.2 RL for LLM Reasoning
L266: Reinforcement learning has recently emerged as a pivotal technique for augmenting LLM reasoning, demonstrating broad success ranging from traditional mathematical and code generation tasks (cite103†Guo et al., 2025 ; cite104†Wang et al., 2025a ) to intricate multi-modal challenges (cite105†Huang et al., 2025c ; cite106†Wang et al., 2025b ; cite107†Li et al., 2025b ) and structured data environments (cite108†Shi et al., 2025 ; cite109†Tang et al., 2025 ).
L267: To support these diverse applications and enable complex behaviors like  RelayLLM, concurrent research is actively refining methodologies through novel training paradigms, such as self-play (cite110†Liu et al., 2025 ; cite111†Huang et al., 2025b ; cite112†Yu et al., 2025b ), alongside developing more robust algorithmic techniques exemplified by DAPO (cite79†Yu et al., 2025a ), VAPO (cite113†Yue et al., 2025 ), and high-entropy guided optimization (cite114†Dai et al., 2025 ; cite115†Wang et al., 2025d ; cite116†Zhou et al., 2025 ).
L268: ## 7 Conclusion
L269: We presented RelayLLM, addressing the inefficiency of "all-or-nothing" offloading in routing systems. By treating the large model as an on-demand tool rather than a fallback generator, our approach demonstrates that small models can handle the vast majority of reasoning steps if supported at specific critical positions. The success of our GRPO-based training strategy confirms that help-seeking behaviors can be effectively learned and optimized.
L270: Our results show that RelayLLM not only outperforms resource-equivalent random routers by 6.9% but also achieves comparable reasoning accuracy to larger models with negligible computation.
L271: ## Acknowledgments
L272: 
L273: We would like to thank Dongfu Jiang (University of Waterloo) for his helpful insights and discussions on tool use LLM. This research was supported in part by the NVIDIA Academic Grant Program and WashU Ignite Interdisciplinary Grants.
L274: ## References
L275:   * Achiam et al. (2023) J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, et al. Gpt-4 technical report. arXiv preprint arXiv:2303.08774. Cited by: cite117†§1 .
L276:   * Bachmann et al. (2025) G. Bachmann, S. Anagnostidis, A. Pumarola, M. Georgopoulos, A. Sanakoyeu, et al. Judge decoding: faster speculative sampling requires going beyond model alignment. arXiv preprint arXiv:2501.19309. Cited by: cite118†§6.1 .
L277:   * Cobbe et al. (2021) K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, et al. Training verifiers to solve math word problems. ArXiv preprint abs/2110.14168. Cited by: cite119†§4.2 .
L278:   * Comanici et al. (2025) G. Comanici, E. Bieber, M. Schaekermann, I. Pasupat, N. Sachdeva, et al. Gemini 2.5: pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. arXiv preprint arXiv:2507.06261. Cited by: cite117†§1 .
L279:   * Dai et al. (2025) R. Dai, L. Song, H. Liu, Z. Liang, D. Yu, et al. CDE: curiosity-driven exploration for efficient reinforcement learning in large language models. arXiv preprint arXiv:2509.09675. Cited by: cite120†§6.2 .
L280:   * Ding et al. (2024) D. Ding, A. Mallick, C. Wang, R. Sim, S. Mukherjee, et al. Hybrid llm: cost-efficient and quality-aware query routing. arXiv preprint arXiv:2404.14618. Cited by: cite121†§1 .
L281:   * Du et al. (2025) X. Du, Y. Yao, K. Ma, B. Wang, T. Zheng, et al. Supergpqa: scaling llm evaluation across 285 graduate disciplines. arXiv preprint arXiv:2502.14739. Cited by: cite122†§5.1 .
L282:   * Feng et al. (2025a) S. Feng, W. Ding, A. Liu, Z. Wang, W. Shi, et al. When one llm drools, multi-llm collaboration rules. arXiv preprint arXiv:2502.04506. Cited by: cite118†§6.1 .
L283:   * Feng et al. (2025b) S. Feng, W. Yu, Y. Wang, H. Zhang, Y. Tsvetkov, et al. Don’t throw away your pretrained model. arXiv preprint arXiv:2510.09913. Cited by: cite118†§6.1 .
L284:   * Fu et al. (2025) T. Fu, Y. Ge, Y. You, E. Liu, Z. Yuan, et al. R2R: efficiently navigating divergent reasoning paths with small-large model token routing. arXiv preprint arXiv:2505.21600. Cited by: cite118†§6.1 .
L285:   * Guo et al. (2025) D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, et al. Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948. Cited by: cite120†§6.2 .
L286:   * Hakimov et al. (2025) S. Hakimov, R. Bernard, T. Leiber, K. Osswald, K. Richert, et al. The price of thought: a multilingual analysis of reasoning, performance, and cost of negotiation in large language models. arXiv preprint arXiv:2510.08098. Cited by: cite117†§1 .
L287:   * He et al. (2024) C. He, R. Luo, Y. Bai, S. Hu, Z. L. Thai, et al. OlympiadBench: a challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems. In Annual Meeting of the Association for Computational Linguistics, Cited by: cite119†§4.2 .
L288:   * Hendrycks et al. (2021) D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt Measuring massive multitask language understanding. In Proc. of ICLR, Cited by: cite119†§4.2 .
L289:   * Hu et al. (2024) Q. J. Hu, J. Bieker, X. Li, N. Jiang, B. Keigwin, et al. Routerbench: a benchmark for multi-llm routing system. arXiv preprint arXiv:2403.12031. Cited by: cite121†§1 .
L290:   * Huang et al. (2024) C. Huang, L. Huang, and J. Huang Divide, reweight, and conquer: a logit arithmetic approach for in-context learning. arXiv preprint arXiv:2410.10074. Cited by: cite123†Appendix D .
L291:   * Huang et al. (2025a) C. Huang, L. Huang, J. Leng, J. Liu, and J. Huang Efficient test-time scaling via self-calibration. arXiv preprint arXiv:2503.00031. Cited by: cite123†Appendix D .
L292:   * Huang et al. (2023) C. Huang, Q. Liu, B. Y. Lin, T. Pang, C. Du, et al. Lorahub: efficient cross-task generalization via dynamic lora composition. arXiv preprint arXiv:2307.13269. Cited by: cite118†§6.1 .

