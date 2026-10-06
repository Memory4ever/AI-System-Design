# Exact-v1 necessary evaluation — 2601.19620

## jan29_three196_evaluation

R³: Replay, Reflection, and Ranking Rewards for LLM Reinforcement Learning (https://arxiv.org/html/2601.19620v1)
citeturn28508view0 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19620v1","lineno":198}); Total lines: 337
L173: Finally, we convert scores into scalar rewards by sorting all samples according to $S_{i}$ and assigning linearly scaled rewards from a maximum value $R_{\text{max}}$:
L174: 
L175:  | $$\mathcal{R}_{(k)}=R_{\text{max}}\cdot\left(1-\frac{k}{N-1}\right)$$  |
L176: 
L177: where $\mathcal{R}_{(k)}$ represents the reward assigned to the sample with the $k$-th highest rank.
L178: #### 3.2.4 Optimization
L179: 
L180: The excessive integration of off-policy historical data with on-policy samples can undermine the strength of the current on-policy learning signal. Therefore, when computing the advantage for the mixed group $G_{\text{mix}}$, we apply a predefined scaling factor $\alpha$ to adjust the contribution of the off-policy samples. Based on the mixed group $G_{\text{mix}}$, the advantage is calculated as follows:
L181:  | $$\hat{A}_{i}=\frac{R_{i}-\operatorname{mean}(\{R_{i}\}_{i=1}^{G_{mix}})}{\alpha\operatorname{std}(\{R_{i}\}_{i=1}^{G_{mix}})+\lambda}$$  |  | (3)
L182: 
L183: where $G_{\text{mix}}=G\cup G_{C}$, where $G$ denotes the on-policy generated group, and $G_{C}$ is the set of historical samples retrieved via the cross-context replay strategy, $\lambda$ is a small constant to ensure numerical stability.
L184: ## 4 Experimental Settings
L185: Model  | AIME24  | MATH  | AMC  | Minerva  | Olympiad  | Average
L186: 1.5B-Scale Models
L187: ---
L188: DeepSeek-R1-Distill-Qwen-1.5B (cite35†Guo et al., 2025 )  | 28.12  | 82.10  | 61.21  | 26.01  | 41.59  | 47.81
L189: STILL-3-1.5B  | 31.67  | 83.89  | 66.11  | 28.81  | 45.32  | 51.59
L190: DeepScaleR-1.5B-Preview (cite66†Luo et al., 2025b )  | 40.42  | 87.36  | 72.89  | 30.35  | 50.18  | 56.24
L191: FASTCURL-1.5B-V2 (cite67†Song et al., 2025 )  | 47.50  | 89.25  | 77.01  | 32.81  | 53.28  | 59.96
L192: 7B-Scale Models
L193: ---
L194: Qwen2.5-Math-7B-Instruct  | 13.34  | 79.81  | 50.62  | 34.60  | 40.69  | 43.81
L195: DeepSeek-R1-Distill-Qwen-7B  | 54.16  | 91.45  | 80.19  | 37.71  | 54.55  | 63.61
L196: Rstar-Math-7B (cite68†Guan et al., 2025 )  | 26.74  | 78.40  | 47.51  | -  | 47.11  | 49.94
L197: Eurus-2-7B-Prime (cite69†Bai et al., 2025 )  | 26.74  | 79.21  | 57.84  | 38.62  | 42.10  | 48.90
L198: SimpleRL-7B (cite70†Ma et al., 2025 )  | 26.74  | 82.45  | 73.56  | 39.72  | 43.40  | 53.17
L199: SATURN-7B (cite71†Liu et al., 2025a )  | 48.31  | 92.65  | 85.42  | 38.96  | 55.60  | 64.20
L200: Thinker-7B(cite72†Chung et al., 2025 )  | 60.00  | 92.71  | 85.09  | 38.16  | 58.62  | 66.92
L201: R³-1.5B (Ours)  | 47.50  | 89.27  | 77.33  | 34.21  | 54.64  | 60.59
L202: R³-7B (Ours)  | 61.04  | 92.55  | 84.18  | 39.70  | 58.44  | 67.18
L203: Table 1: Pass@1 performance comparison on various math benchmarks.
L204:  | AIME2024  | MATH  | AMC  | Minerva  | Olympdia
L205: --- | --- | --- | --- | --- | ---
L206: Model  | P@1  | P@16  | Tokens  | P@1  | P@16  | Tokens  | P@1  | P@16  | Tokens  | P@1  | P@16  | Tokens  | P@1  | P@16  | Tokens
L207: --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
L208: DeepSeek-Distill-1.5B  | 28.1  | 70.0  | 12270.4  | 82.1  | 95.2  | 4799.6  | 61.2  | 92.7  | 8504.6  | 26.0  | 55.9  | 6299.9  | 41.5  | 62.9  | 9070.6
L209: --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
L210: L1-Max  | 24.6  | 60.0  | 3788.0  | 84.1  | 93.6  | 3357.6  | 65.6  | 89.2  | 3558.6  | 28.5  | 54.0  | 3414.3  | 45.4  | 61.3  | 3521.3
L211: ThinkPrune-1.5B  | 23.7  | 53.3  | 5208.3  | 80.4  | 95.6  | 1652.4  | 61.3  | 90.4  | 2915.9  | 22.9  | 48.2  | 1508.7  | 40.6  | 63.7  | 3125.7
L212: Query-Opt  | 26.7  | 59.8  | 10805.2  | 81.5  | 94.9  | 3284.6  | 63.2  | 90.4  | 5389.6  | 28.9  | 54.0  | 4332.8  | 47.9  | 64.1  | 5969.2
L213: O1-Pruner  | 32.4  | 67.6  | 10324.4  | 71.9  | 87.5  | 3299.4  | 66.2  | 90.0  | 5993.4  | 29.2  | 56.9  | 5722.3  | 46.1  | 64.4  | 6323.2
L214: HAPO  | 30.8  | 66.7  | 8967.2  | 82.8  | 95.2  | 2686.5  | 65.7  | 89.2  | 5412.8  | 25.0  | 53.3  | 2975.9  | 43.8  | 63.7  | 5892.2
L215: DeepScaleR-1.5B  | 38.5  | 70.0  | 8888.0  | 87.6  | 95.6  | 3045.0  | 71.8  | 89.2  | 5529.6  | 30.9  | 54.8  | 4635.3  | 50.2  | 64.6  | 5607.6
L216: Thinker-1.5B  | 27.1  | 53.3  | 4341.4  | 82.9  | 95.4  | 1829.2  | 66.2  | 91.6  | 2883.0  | 29.7  | 57.4  | 2885.3  | 46.0  | 65.9  | 3054.1
L217: FastCuRL-1.5B  | 40.8  | 70.0  | 10088.7  | 87.5  | 95.6  | 3858.6  | 73.6  | 90.4  | 6682.1  | 32.1  | 58.1  | 5867.8  | 49.7  | 65.2  | 7066.7
L218: SaTurn-1.5B  | 28.1  | 76.6  | 11742.6  | 82.9  | 96.0  | 4385.7  | 61.3  | 90.3  | 7928.1  | 26.7  | 51.8  | 5764.9  | 42.6  | 62.8  | 8454.3
L219: JustRL-1.5B  | 53.5  | 83.4  | 9182.7  | 88.7  | 94.8  | 4097.0  | 82.2  | 93.9  | 6869.9  | 33.5  | 52.5  | 5189.1  | 55.9  | 68.8  | 7025.1
L220: R³-1.5B (Ours)  | 47.5  | 76.7  | 7574.1  | 89.3  | 96.0  | 3286.9  | 77.3  | 91.6  | 5239.9  | 34.2  | 55.9  | 4762.0  | 54.6  | 69.9  | 5520.6
L221: Table 2: Comparison with different RL baseline results on DeepSeek-Distill-1.5B.
L222: ### 4.1 Training
L223: 
L224: #### 4.1.1 Base model.
L225: 
L226: We adopt DeepSeek-R1-Distill-Qwen-1.5B and 7B cite35†Guo et al. (2025) as base models, as they inherently possess strong reasoning capabilities, providing a solid foundation for applying our proposed training strategy R³.
L227: #### 4.1.2 Datasets.
L228: 
L229: To train the model with our proposed method, we employ the DeepScaleR cite66†Luo et al. (2025b) dataset, a high-quality synthetic dataset consisting of approximately 40,000 unique mathematics problem-answer pairs, designed to scale large language models in mathematical and logical reasoning tasks.
L230: #### 4.1.3 Reward Function
L231: We utilize an outcome-oriented reward function based on the Qwen2.5-Math evaluator^{†}^{†} cite73†https://github.com/QwenLM/Qwen2.5-Math/tree/main/evaluation†github.com , which assigns correctness scores by symbolically comparing the model’s final output with the reference answer. To further promote reasoning efficiency, we incorporate a length-based reward term specifically for correct responses.
L232: Formally, given a response that matches the ground truth with length $l$ and a maximum token limit $L_{\text{max}}$ (set to 32,768), we apply an additional reward $r_{\text{len}}=\max(0,1-\frac{l}{L_{\text{max}}})$. This mechanism encourages the model to converge toward concise solution paths without compromising accuracy.


## jan29_three196_settings

R³: Replay, Reflection, and Ranking Rewards for LLM Reinforcement Learning (https://arxiv.org/html/2601.19620v1)
citeturn28511view0 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19620v1","lineno":232}); Total lines: 337
L209: --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
L212: Query-Opt  | 26.7  | 59.8  | 10805.2  | 81.5  | 94.9  | 3284.6  | 63.2  | 90.4  | 5389.6  | 28.9  | 54.0  | 4332.8  | 47.9  | 64.1  | 5969.2
L213: O1-Pruner  | 32.4  | 67.6  | 10324.4  | 71.9  | 87.5  | 3299.4  | 66.2  | 90.0  | 5993.4  | 29.2  | 56.9  | 5722.3  | 46.1  | 64.4  | 6323.2
L214: HAPO  | 30.8  | 66.7  | 8967.2  | 82.8  | 95.2  | 2686.5  | 65.7  | 89.2  | 5412.8  | 25.0  | 53.3  | 2975.9  | 43.8  | 63.7  | 5892.2
L215: DeepScaleR-1.5B  | 38.5  | 70.0  | 8888.0  | 87.6  | 95.6  | 3045.0  | 71.8  | 89.2  | 5529.6  | 30.9  | 54.8  | 4635.3  | 50.2  | 64.6  | 5607.6
L216: Thinker-1.5B  | 27.1  | 53.3  | 4341.4  | 82.9  | 95.4  | 1829.2  | 66.2  | 91.6  | 2883.0  | 29.7  | 57.4  | 2885.3  | 46.0  | 65.9  | 3054.1
L217: FastCuRL-1.5B  | 40.8  | 70.0  | 10088.7  | 87.5  | 95.6  | 3858.6  | 73.6  | 90.4  | 6682.1  | 32.1  | 58.1  | 5867.8  | 49.7  | 65.2  | 7066.7
L218: SaTurn-1.5B  | 28.1  | 76.6  | 11742.6  | 82.9  | 96.0  | 4385.7  | 61.3  | 90.3  | 7928.1  | 26.7  | 51.8  | 5764.9  | 42.6  | 62.8  | 8454.3
L219: JustRL-1.5B  | 53.5  | 83.4  | 9182.7  | 88.7  | 94.8  | 4097.0  | 82.2  | 93.9  | 6869.9  | 33.5  | 52.5  | 5189.1  | 55.9  | 68.8  | 7025.1
L220: R³-1.5B (Ours)  | 47.5  | 76.7  | 7574.1  | 89.3  | 96.0  | 3286.9  | 77.3  | 91.6  | 5239.9  | 34.2  | 55.9  | 4762.0  | 54.6  | 69.9  | 5520.6
L221: Table 2: Comparison with different RL baseline results on DeepSeek-Distill-1.5B.
L222: ### 4.1 Training
L223: 
L224: #### 4.1.1 Base model.
L225: 
L226: We adopt DeepSeek-R1-Distill-Qwen-1.5B and 7B cite35†Guo et al. (2025) as base models, as they inherently possess strong reasoning capabilities, providing a solid foundation for applying our proposed training strategy R³.
L227: #### 4.1.2 Datasets.
L228: 
L229: To train the model with our proposed method, we employ the DeepScaleR cite66†Luo et al. (2025b) dataset, a high-quality synthetic dataset consisting of approximately 40,000 unique mathematics problem-answer pairs, designed to scale large language models in mathematical and logical reasoning tasks.
L230: #### 4.1.3 Reward Function
L231: We utilize an outcome-oriented reward function based on the Qwen2.5-Math evaluator^{†}^{†} cite73†https://github.com/QwenLM/Qwen2.5-Math/tree/main/evaluation†github.com , which assigns correctness scores by symbolically comparing the model’s final output with the reference answer. To further promote reasoning efficiency, we incorporate a length-based reward term specifically for correct responses.
L232: Formally, given a response that matches the ground truth with length $l$ and a maximum token limit $L_{\text{max}}$ (set to 32,768), we apply an additional reward $r_{\text{len}}=\max(0,1-\frac{l}{L_{\text{max}}})$. This mechanism encourages the model to converge toward concise solution paths without compromising accuracy.
L233: ### 4.2 Evaluation
L234: 
L235: #### 4.2.1 Benchmark.
L236: 
L237: We use five widely used complex mathematical benchmarks: AIME 2024 cite74†Mathematical Association of America (2024) , MATH500 cite75†Hendrycks et al. (2021) , AMC 2023 cite76†Mathematical Association of America (2023) , Minerva Math cite77†Lewkowycz et al. (2022) , OlympiadBench cite78†He et al. (2024) .
L238: #### 4.2.2 Metrics.
L239: 
L240: We assess mathematical reasoning performance by generating $N=16$ independent responses per question across the benchmarks. We report Pass@1 (P@1) and Pass@16 (P@16) as evaluation metrics to capture both the standard accuracy and the model’s ability to explore correct solutions within the sampling budget. Additionally, we calculate the average response length (in tokens) to analyze the inference efficiency of different models.
L241: 
L242: ## 5 Experiment Results
L243: ### 5.1 Overall Results
L244: 
L245: As reported in Table cite79†1 , R³ achieves state-of-the-art performance across all five benchmarks. R³-1.5B obtains an average score of 60.59, significantly outperforming the base DeepSeek-R1-Distill-Qwen-1.5B by 12.78 points and surpassing strong baselines like DeepScaleR-1.5B-Preview (56.24).
L246: More strikingly, our 1.5B model surpasses several 7B-scale models, challenging standard scaling assumptions. For instance, R³-1.5B outperforms SimpleRL-7B (53.17) and Eurus-2-7B-Prime (48.90) by substantial margins. On the challenging AIME24 benchmark, R³-1.5B scores 47.50, nearly doubling the performance of Eurus-2-7B-Prime (26.74) and matching the 7B-scale SATURN-7B (48.31).
L247: Furthermore, when scaled to 7B, R³-7B demonstrates superior performance with an average score of 67.18, consistently outperforming robust baselines such as SATURN-7B and DeepSeek-R1-Distill-Qwen-7B. Notably, on the challenging AIME24 benchmark, R³-7B achieves a score of 61.04, surpassing the competitive Thinker-7B baseline (60.00). Similarly, on the rigorous Minerva dataset, it attains 39.70, exceeding both SATURN-7B and Thinker-7B.
L248: Table cite80†2 presents a detailed comparison of R³-1.5B against a wide array of state-of-the-art RL baselines at the 1.5B scale. R³ achieves high accuracy with exceptional reasoning efficiency. For instance, on AIME24, the base DeepSeek-Distill-1.5B consumes 12,270 tokens to score 28.1. In contrast, R³-1.5B achieves a significantly higher score of 47.5 using only 7,574 tokens. This confirms that our framework steers the model toward concise, valid reasoning rather than redundant verification.
L249: ### 5.2 Ablation Study
L250: 
L251: Model  | AIME24  | MATH  | AMC  | Minerva  | Olympiad
L252: --- | --- | --- | --- | --- | ---
L253: R³-1.5B  | 47.50  | 89.27  | 77.33  | 34.21  | 54.64
L254: --- | --- | --- | --- | --- | ---
L255: w/o CCR  | 35.62  | 86.57  | 71.76  | 30.95  | 45.68
L256: w/o ISR  | 41.25  | 87.54  | 73.87  | 32.38  | 51.72
L257: w/o SERR  | 36.88  | 86.84  | 71.83  | 30.58  | 48.47
L258: 
L259: Table 3: Ablation study result.
L260: To evaluate the contribution of each component in our reinforcement learning framework, we perform ablation studies by selectively removing three key modules: cross-context replay (CCR), in-context self-reflection (ISR), and the structural entropy ranking reward (SERR). The results are summarized in Table cite79†1 .
L261: Removing the CCR module leads to a clear performance drop across all benchmarks, with the most substantial declines observed on AIME24 (from 47.50 to 35.62) and Minerva (from 34.21 to 30.95). This underscores the importance of leveraging cross-query context to enhance sample efficiency and generalization.
L262: Ablating ISR also results in consistent degradation, notably on Olympiad (54.64 to 51.72) and AMC (77.33 to 73.87), indicating its effectiveness in enabling the model to refine its reasoning within a single trajectory. Lastly, removing SERR yields comparable drops, especially on AIME24 and Minerva, suggesting that the provision of unsupervised reward signals is crucial when standard feedback is unavailable due to truncation or failure.
L263: cite81†Image: Refer to caption Figure 3: Performance evaluation on challenging subsets of AIME24 and MATH Figure 4: Training Dynamics and Entropy Evolution Analysis
L264: ### 5.3 Training Dynamics
L265: Figure cite82†4 (left) visualizes the evolution of training metrics for R³, specifically tracking the average reward alongside the frequency of ”Solve All” (all $G$ samples correct) and ”Solve None” (all samples fail) groups within each sampling batch. Following an initial epoch of standard training, a notable dip in reward emerges. This shift is directly attributed to the activation of our cross-context replay (CCR) and in-context self-reflection (ISR) mechanisms.
L266: Importantly, this strategy preserves performance on mastered queries: the frequency of ”Solve All” groups continues to rise steadily, while ”Solve None” instances consistently decline.
L267: Figure cite82†4 (right) illustrates the evolution of policy entropy throughout the training process. For a rigorous comparison, we reproduced both the DAPO and GRPO baselines and plotted their corresponding entropy curves. In stark contrast to these methods, which exhibit rapid entropy decay, R³ demonstrates a distinct upward trend during the intermediate training stages. This phenomenon reflects the effective encouragement of sample exploration driven by our structural entropy ranking reward (SERR).


## jan29_three196_counter

R³: Replay, Reflection, and Ranking Rewards for LLM Reinforcement Learning (https://arxiv.org/html/2601.19620v1)
citeturn28512view0 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19620v1","lineno":268}); Total lines: 337
L260: To evaluate the contribution of each component in our reinforcement learning framework, we perform ablation studies by selectively removing three key modules: cross-context replay (CCR), in-context self-reflection (ISR), and the structural entropy ranking reward (SERR). The results are summarized in Table cite79†1 .
L261: Removing the CCR module leads to a clear performance drop across all benchmarks, with the most substantial declines observed on AIME24 (from 47.50 to 35.62) and Minerva (from 34.21 to 30.95). This underscores the importance of leveraging cross-query context to enhance sample efficiency and generalization.
L262: Ablating ISR also results in consistent degradation, notably on Olympiad (54.64 to 51.72) and AMC (77.33 to 73.87), indicating its effectiveness in enabling the model to refine its reasoning within a single trajectory. Lastly, removing SERR yields comparable drops, especially on AIME24 and Minerva, suggesting that the provision of unsupervised reward signals is crucial when standard feedback is unavailable due to truncation or failure.
L263: cite81†Image: Refer to caption Figure 3: Performance evaluation on challenging subsets of AIME24 and MATH Figure 4: Training Dynamics and Entropy Evolution Analysis
L264: ### 5.3 Training Dynamics
L265: Figure cite82†4 (left) visualizes the evolution of training metrics for R³, specifically tracking the average reward alongside the frequency of ”Solve All” (all $G$ samples correct) and ”Solve None” (all samples fail) groups within each sampling batch. Following an initial epoch of standard training, a notable dip in reward emerges. This shift is directly attributed to the activation of our cross-context replay (CCR) and in-context self-reflection (ISR) mechanisms.
L266: Importantly, this strategy preserves performance on mastered queries: the frequency of ”Solve All” groups continues to rise steadily, while ”Solve None” instances consistently decline.
L267: Figure cite82†4 (right) illustrates the evolution of policy entropy throughout the training process. For a rigorous comparison, we reproduced both the DAPO and GRPO baselines and plotted their corresponding entropy curves. In stark contrast to these methods, which exhibit rapid entropy decay, R³ demonstrates a distinct upward trend during the intermediate training stages. This phenomenon reflects the effective encouragement of sample exploration driven by our structural entropy ranking reward (SERR).
L268: The subsequent decline confirms that the policy eventually converges to a stable state after adequate exploration.
L269: Taken together, these dynamics validate the synergy of our design: CCR and ISR ensure the steady mastery of complex reasoning paths (as evidenced by the ”Solve All” rise), while SERR maintains the necessary exploration (via entropy retention) to prevent policy collapse.
L270: ### 5.4 Experiments on Challenging Subsets
L271: 
L272: To evaluate the effectiveness of our method on difficult tasks, we analyze model performance on challenging subsets of the AIME24 and MATH benchmarks. Specifically, we curate these subsets by selecting queries that the base model answered correctly at most once across 16 sampled responses.
L273: We perform two sets of experiments on these challenging subsets: (1) Varying the number of sampled responses ($K$) to evaluate Pass@K, identifying the model’s upper bound in solving challenging queries (shown in Figure cite83†3 (a) and (b)). (2) Varying the maximum response length to evaluate Pass@16, assessing the model’s reasoning efficiency under output constraints (shown in Figure cite83†3 (c) and (d)).
L274: The results on the challenging subsets of AIME24 are presented in Figure cite83†3 (a), respectively. We report the $\text{Pass}@K$ metric under varying numbers of sampled responses, with $K$ ranging from 1 to 256. Notably, on the challenging subset of AIME24, our model R³ begins to exhibit the ability to solve difficult queries when $K>2$. As illustrated in Figure cite83†3 (b), R³ achieves the highest performance on the challenging subset of MATH with $K$ ranging from 1 to 256.
L275: Notably, while all competing approaches stagnate at lower levels, R³ surpasses this performance ceiling, achieving a $\text{Pass}@256$ score of 64.29. This indicates its effectiveness in pushing the base model beyond its inherent limitations.
L276: As shown in Figure cite83†3 (c) and Figure cite83†3 (d), our model consistently achieves the highest scores across all tested maximum response lengths, ranging from 4k to 64k tokens. In our experiments with varying maximum response lengths, we observed that certain challenging queries could not be solved simply by increasing the length limit. This suggests that the model had reached its performance ceiling and that our R³ training enabled the base model to fully utilize its capacity.
L277: In summary, our evaluation on challenging subsets demonstrates that R³ effectively unlocks the base model’s latent reasoning capabilities.
L278: ## 6 Conclusion
L279: We present R³, a reinforcement learning framework that integrates Cross-Context Replay (CCR) and In-Context Self-Reflection (ISR) to stabilize training on challenging queries, while introducing the Structural Entropy Ranking Reward (SERR) to extract unsupervised signals from truncated trajectories.
L280: Experimental results demonstrate that R³ achieves state-of-the-art performance on benchmarks like AIME24, outperforming strong baselines like DeepScaleR with significantly improved sample efficiency (using only 8K generation tokens). By effectively leveraging historical and imperfect samples, R³ offers a scalable, computationally efficient pathway for advancing robust mathematical reasoning in LLMs.
L281: ## References
L282:   * Andrychowicz et al. (2017) M. Andrychowicz, F. Wolski, A. Ray, J. Schneider, R. Fong, P. Welinder, B. McGrew, J. Tobin, O. Pieter Abbeel, and W. Zaremba Hindsight experience replay. Advances in neural information processing systems 30. Cited by: cite84†§2.2 .
L283:   * Bai et al. (2025) F. Bai, Y. Min, B. Zhang, Z. Chen, W. X. Zhao, L. Fang, Z. Liu, Z. Wang, and J. Wen Towards effective code-integrated reasoning. arXiv preprint arXiv:2505.24480. Cited by: cite85†Table 1 .
L284:   * Cheng et al. (2025) D. Cheng, S. Huang, X. Zhu, B. Dai, W. X. Zhao, Z. Zhang, and F. Wei Reasoning with exploration: an entropy perspective. arXiv preprint arXiv:2506.14758. Cited by: cite86†§2.3 .
L285:   * Chung et al. (2025) S. Chung, W. Du, and J. Fu Thinker: learning to think fast and slow. arXiv preprint arXiv:2505.21097. Cited by: cite87†Table 1 .
L286:   * Cui et al. (2025) G. Cui, Y. Zhang, J. Chen, L. Yuan, Z. Wang, Y. Zuo, H. Li, Y. Fan, H. Chen, W. Chen, et al. The entropy mechanism of reinforcement learning for reasoning language models. arXiv preprint arXiv:2505.22617. Cited by: cite86†§2.3 .
L287:   * Dang and Ngo (2025) Q. Dang and C. Ngo Reinforcement learning for reasoning in small llms: what works and what doesn’t. arXiv preprint arXiv:2503.16219. Cited by: cite88†§1 .
L288:   * Guan et al. (2025) X. Guan, L. L. Zhang, Y. Liu, N. Shang, Y. Sun, Y. Zhu, F. Yang, and M. Yang RStar-math: small llms can master math reasoning with self-evolved deep thinking. arXiv preprint arXiv:2501.04519. Cited by: cite89†Table 1 .


## jan29_three196_cost

R³: Replay, Reflection, and Ranking Rewards for LLM Reinforcement Learning (https://arxiv.org/html/2601.19620v1)
citeturn28513view3 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19620v1","pattern":"Implementation"}); Total lines: 337
No matching text found for "Implementation"
