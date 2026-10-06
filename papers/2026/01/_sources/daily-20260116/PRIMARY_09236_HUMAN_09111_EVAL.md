# Necessary exact-v1 raw supplementary evidence

2026-10-03: only 09236 human-overlap/A.4 and 09111 factorial/K tables; no unrelated appendices read implied.

Reward Learning through Ranking Mean Squared Error (https://arxiv.org/html/2601.09236v1)
citeturn27083view0 [wordlim: 200] Crawled: 4 days ago; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.09236v1","pattern":"overlap"}); Total lines: 691
L450: In this section, we describe our human-subject pilot study. We conducted the study with five participants (two authors/experts and three non-authors/non-experts). Each rater was shown trajectories from OpenAI Gym’s reacher environment sequentially and asked either to rate each trajectory or skip it. Each rater could decide how many bins to use, choosing any value between 3 and 10. The raters were asked to collect ratings for 100-200 trajectories in total.
L451: After collecting the data, we trained an offline reward function using 100 randomly selected trajectories from each participant’s dataset. Using the learned reward function, we then trained a SAC agent on the same environment. We repeated this process five times to account for randomness in reward-function learning and SAC training.
L452: We report the aggregated learning curves in Figure cite129†5 . The mean performance of the policies derived from each individual rater is shown in lighter colors, while the average across all raters is shown in darker colors. These results indicate that R4 performs better than RbRL despite any rater-specific biases and inconsistencies that may have occurred. Furthermore, on average, R4 with human ratings performs similarly to R4 with perfect simulated ratings.
L453: cite130†Image: Refer to caption Figure 5: Combined performance of policies trained on reward models learned from five human raters. Light curves show the average performance across five SAC training runs for each rater; the dark curve shows the overall mean across raters. R4 consistently outperforms RbRL despite substantial variation in individual rating behavior. Furthermore, on average, R4 with human ratings performs similarly to R4 with perfect simulated ratings.
L454: Finally, Figures cite131†6 through cite132†10 show the SAC learning curves for each rater’s reward function (left). Different seeds are shown in lighter colors, while the mean is shown in a darker color. The middle plot shows each rater’s distribution of labels. It reveals that (i) the distributions are highly non-uniform for all raters, and (ii) the distributions vary substantially across raters, with different individuals using different numbers of rating classes.
L455: The right plot shows the distribution of undiscounted environment returns associated with each label in the rated dataset. This confirms that the human ratings are highly imperfect, with substantial overlap in true returns across labels. These results further support our claim that R4 is robust to rater bias and variance.
L456: cite133†Image: Refer to caption Figure 6: (Left) Learning curves for Participant 1’s reward function, with individual random seeds shown in lighter colors and the mean in darker color. (Middle) Histogram of Participant 1’s labeling distribution. (Right) Violin plot of undiscounted environment returns conditioned on each label, showing substantial overlap in returns and highlighting the noisiness and imperfection of the ratings.
L457: cite134†Image: Refer to caption Figure 7: Participant 2’s results and data distribution. cite135†Image: Refer to caption Figure 8: Participant 3’s results and data distribution. cite136†Image: Refer to caption Figure 9: Participant 4’s results and data distribution. cite137†Image: Refer to caption Figure 10: Participant 5’s results and data distribution.
L458: ### B.2 Simulated Experiments
L459: 
L460: To assess the impact of the dynamic feedback schedule and sampling tricks on the baselines, we tested them with these modifications included. Figure cite109†11 shows that the baselines’ performance either remains similar or degrades compared to Figure cite110†3 .
L461: cite138†Image: Refer to caption Figure 11: Mean undiscounted return (computed using the environment’s reward function) versus the number of episodes when training a SAC agent with R4 and various baselines in the online setting. The baselines are allowed to use our dynamic feedback schedule and their respective query sampling tricks.
L462: Second, we evaluate the resilience of R4 to noisy feedback on the Inverted Double Pendulum task in the offline setting, where both R4 and RbRL achieve similar final performance under noiseless conditions. We focus on the offline setting because it isolates the effect of noise on reward learning. To simulate noisy human feedback, we randomly select $\eta\%$ of the trajectories in the dataset $\mathcal{D}$ and reassign them to true_bin$\pm 1$ with probability $0.5$ each.
L463: Figure cite139†12(a) shows R4 performance under varying noise levels. While performance naturally decreases as $\eta$ increases, R4 remains robust even at high noise levels. Figure cite140†12(b) compares R4 with RbRL under the same conditions, showing that RbRL fails even at small noise levels. Notably, R4 with 80% noise achieves performance comparable to RbRL with only 10% noise.
L464: 
L465: cite141†Image: Refer to caption (a)
L466: 
L467: cite142†Image: Refer to caption (b)
L468: Figure 12: (a) R4 objective under varying levels of noise. (b) Comparison of R4 (reds) and RbRL (blues) under different noise levels.
L469: 
L470: Furthermore, we study the impact of the number of rating classes on R4 in the Reacher environment. Figure cite113†13 shows that although RbRL’s performance depends significantly on the number of bins, R4 remains consistent.
L471: Finally, we study the impact of the fast-soft-ranking (cite72†Blondel et al. 2020 ) regularization strength in R4 for the Inverted Double Pendulum environment. In Figure cite143†15 , we plot the undiscounted return averaged over the last 100 episodes as a function of the regularization strength. The plot shows that 83% of the runs with regularization strengths between 0.065 and 1 learn a successful policy.
L472: Overall, these results highlight that R4 is robust to dynamic feedback schedules, resilient to noisy feedback, and largely insensitive to the choice of rating classes, in contrast to RbRL, which is sensitive to all three.
L473: 
L474: cite144†Image: Refer to caption Figure 13: Undiscounted return vs number of episodes for reacher with varying number of bins.
L475: ### B.3 Quality of learned reward functions
L476: To assess the quality of the reward functions learned by R4 relative to the baselines, we first present a scatter plot comparing undiscounted returns from the learned reward functions against the undiscounted environment returns encountered during a single online run (Figure cite145†14 ). We show this for three environments and for all methods. The plots indicate that R4 consistently captures a meaningful relationship between learned and actual returns across environments.
L477: Furthermore, to evaluate reward quality quantitatively, we report the Trajectory Alignment Coefficient (TAC) cite64†Muslimani et al. 2025 in Table cite146†1 . TAC is a reward alignment metric that measures how similarly two reward functions rank a set of trajectories, where a TAC of 1 indicates perfect alignment and a TAC of -1 indicates perfect negative correlation. We compare the reward functions learned by each method with the ground truth reward functions using TAC.
--------------------------------------------------------------------------------
Reward Learning through Ranking Mean Squared Error (https://arxiv.org/html/2601.09236v1)
citeturn27083view1 [wordlim: 200] Crawled: 4 days ago; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.09236v1","pattern":"Pilot"}); Total lines: 691
L399: which is the bound on $\epsilon$ in assumption cite100†5 . Now, since $\epsilon$ satisfies this bound, continuing from cite128†13 , we can be sure that:
L400: 
L401:  |  | $\displaystyle G_{\theta}(\tau_{0})<G_{\theta}(\tau_{1})<\cdots<G_{\theta}(\tau_{n-1})$  |
L402:  | $\displaystyle\implies$  | $\displaystyle r_{\theta}\in\mathcal{R}$  |
L403: 
L404: Combining these two results, we have shown that under assumptions cite93†1 , cite94†2 , cite95†3 and cite100†5 :
L405:  | $\displaystyle r_{\theta}\in\mathcal{R}\iff r_{\theta}\in\mathcal{R}_{\text{rMSE}}$  |
L406: 
L407: ∎
L408: ### A.4 Sample Outputs From Fast-Soft Rank
L409: 
L410: Here, we present a few outputs from the fast-soft ranking algorithm, to justify Assumption cite96†4 . With an appropriate value of regularization_strength, the ranking operator outputs the true ranks of all elements in most cases.
L411: 
L412: ⬇
L413: 
L414: 1 for _ in range(10):
L415: 
L416: 2 x = np.random.uniform(0,10,10)
L417: 
L418: 3 print(soft_rank(x, regularization_strength=0.01))
L419: 
L420: 4
L421: 
L422: 5 ’’’
L423: 
L424: 6 Outputs:
L425: 
L426: 7 [␣4.␣␣5.␣10.␣␣3.␣␣6.␣␣2.␣␣9.␣␣1.␣␣7.␣␣8.]
L427: 
L428: 8 [␣9.␣␣4.␣10.␣␣8.␣␣2.␣␣1.␣␣7.␣␣3.␣␣5.␣␣6.]
L429: 9 [␣5.␣␣7.␣␣6.␣␣9.␣␣4.␣␣2.␣␣3.␣␣8.␣10.␣␣1.]
L430: 
L431: 10 [␣8.␣␣4.␣10.␣␣6.␣␣7.␣␣5.␣␣1.␣␣3.␣␣9.␣␣2.]
L432: 
L433: 11 [␣8.␣␣5.␣␣6.␣␣4.␣␣1.␣␣7.␣␣9.␣␣3.␣10.␣␣2.]
L434: 
L435: 12 [␣7.␣␣5.␣␣9.␣␣1.␣␣2.␣␣6.␣10.␣␣4.␣␣8.␣␣3.]
L436: 
L437: 13 [␣5.␣␣8.␣␣9.␣␣3.␣␣2.␣10.␣␣1.␣␣7.␣␣6.␣␣4.]
L438: 
L439: 14 [␣1.␣␣7.␣10.␣␣4.␣␣9.␣␣3.␣␣6.␣␣5.␣␣8.␣␣2.]
L440: 
L441: 15 [␣7.␣␣9.␣10.␣␣5.␣␣6.␣␣1.␣␣3.␣␣8.␣␣4.␣␣2.]
L442: 
L443: 16 [␣8.␣␣9.␣␣4.␣␣7.␣10.␣␣3.␣␣6.␣␣2.␣␣5.␣␣1.]
L444: 
L445: 17 ’’’
L446: 
L447: Listing 1: Sample Outputs From Soft Rank
L448: ## Appendix B Additional Results
L449: ### B.1 Human Studies
L450: In this section, we describe our human-subject pilot study. We conducted the study with five participants (two authors/experts and three non-authors/non-experts). Each rater was shown trajectories from OpenAI Gym’s reacher environment sequentially and asked either to rate each trajectory or skip it. Each rater could decide how many bins to use, choosing any value between 3 and 10. The raters were asked to collect ratings for 100-200 trajectories in total.
L451: After collecting the data, we trained an offline reward function using 100 randomly selected trajectories from each participant’s dataset. Using the learned reward function, we then trained a SAC agent on the same environment. We repeated this process five times to account for randomness in reward-function learning and SAC training.
L452: We report the aggregated learning curves in Figure cite129†5 . The mean performance of the policies derived from each individual rater is shown in lighter colors, while the average across all raters is shown in darker colors. These results indicate that R4 performs better than RbRL despite any rater-specific biases and inconsistencies that may have occurred. Furthermore, on average, R4 with human ratings performs similarly to R4 with perfect simulated ratings.
L453: cite130†Image: Refer to caption Figure 5: Combined performance of policies trained on reward models learned from five human raters. Light curves show the average performance across five SAC training runs for each rater; the dark curve shows the overall mean across raters. R4 consistently outperforms RbRL despite substantial variation in individual rating behavior. Furthermore, on average, R4 with human ratings performs similarly to R4 with perfect simulated ratings.
L454: Finally, Figures cite131†6 through cite132†10 show the SAC learning curves for each rater’s reward function (left). Different seeds are shown in lighter colors, while the mean is shown in a darker color. The middle plot shows each rater’s distribution of labels. It reveals that (i) the distributions are highly non-uniform for all raters, and (ii) the distributions vary substantially across raters, with different individuals using different numbers of rating classes.
L455: The right plot shows the distribution of undiscounted environment returns associated with each label in the rated dataset. This confirms that the human ratings are highly imperfect, with substantial overlap in true returns across labels. These results further support our claim that R4 is robust to rater bias and variance.
L456: cite133†Image: Refer to caption Figure 6: (Left) Learning curves for Participant 1’s reward function, with individual random seeds shown in lighter colors and the mean in darker color. (Middle) Histogram of Participant 1’s labeling distribution. (Right) Violin plot of undiscounted environment returns conditioned on each label, showing substantial overlap in returns and highlighting the noisiness and imperfection of the ratings.
L457: cite134†Image: Refer to caption Figure 7: Participant 2’s results and data distribution. cite135†Image: Refer to caption Figure 8: Participant 3’s results and data distribution. cite136†Image: Refer to caption Figure 9: Participant 4’s results and data distribution. cite137†Image: Refer to caption Figure 10: Participant 5’s results and data distribution.
L458: ### B.2 Simulated Experiments
L459: 
L460: To assess the impact of the dynamic feedback schedule and sampling tricks on the baselines, we tested them with these modifications included. Figure cite109†11 shows that the baselines’ performance either remains similar or degrades compared to Figure cite110†3 .
L461: cite138†Image: Refer to caption Figure 11: Mean undiscounted return (computed using the environment’s reward function) versus the number of episodes when training a SAC agent with R4 and various baselines in the online setting. The baselines are allowed to use our dynamic feedback schedule and their respective query sampling tricks.
--------------------------------------------------------------------------------
Towards Open Environments and Instructions: General Vision-Language Navigation via Fast-Slow Interactive Reasoning (https://arxiv.org/html/2601.09111v1)
citeturn27083view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.09111v1","pattern":"Table 4"}); Total lines: 518
L186: Methods  | Test-N-Scene
L187: TL  | NE$\downarrow$  | SR$\uparrow$  | SPL$\uparrow$  | nDTW$\uparrow$
L188: Baseline
L189: ---
L190: DUET  | 14.9  | 6.4  | 39.6  | 30.1  | 40.9
L191: Optimization-Based Methods
L192: ---
L193:    +MLM  | 14.3 $\pm$0.1  | 6.5 $\pm$0.1  | 39.8 $\pm$0.1  | 30.5 $\pm$0.1  | 41.1 $\pm$0.1
L194:    +MRC  | 14.9 $\pm$0.1  | 6.4 $\pm$0.1  | 39.7 $\pm$0.1  | 30.2 $\pm$0.1  | 40.9 $\pm$0.1
L195:    +BT  | 8.4 $\pm$0.0  | 6.3 $\pm$0.2  | 41.2 $\pm$1.5  | 38.2 $\pm$1.2  | 51.3 $\pm$1.2
L196:    +TENT  | 16.4 $\pm$0.1  | 6.3 $\pm$0.1  | 40.6 $\pm$0.2  | 28.9 $\pm$0.2  | 38.9 $\pm$0.2
L197:    +SAR  | 16.3 $\pm$0.5  | 6.0 $\pm$0.2  | 41.4 $\pm$0.6  | 29.1 $\pm$0.3  | 39.0 $\pm$0.3
L198: Memory-Based Methods
L199: ---
L200: TourHAMT  | 7.3 $\pm$0.1  | 8.1 $\pm$0.1  | 9.7 $\pm$0.1  | 8.0 $\pm$0.1  | 32.3 $\pm$0.1
L201: OVER-NAV  | 11.8 $\pm$0.1  | 7.6 $\pm$0.2  | 16.7 $\pm$0.4  | 12.6 $\pm$0.2  | 34.6 $\pm$0.3
L202: GR-DUET  | 10.1 $\pm$0.0  | 5.5 $\pm$0.0  | 48.1 $\pm$0.1  | 42.8 $\pm$0.1  | 53.7 $\pm$0.1
L203: Ours  | 8.9 $\pm$0.2  | 5.1 $\pm$0.0  | 50.7 $\pm$0.1  | 46.6 $\pm$0.1  | 57.8 $\pm$0.3
L204: Instruction Adaptation. We evaluated these methods under different instruction styles. Table cite63†2 presents the results for the model under five user instructions roles, while Table cite64†3 shows their performance with scene instructions. First, DUET’s (cite48†9 ) performance data indicates that different expression styles introduce varying levels of difficulty in instruction interpretation for VLN models. Second, our method outperforms GR-DUET (cite37†17 ) in both scene and user-style instructions.
L205: The key innovation lies in addressing GR-DUET’s limitation in adapting to instruction styles. We achieve this through an LLM-based instruction style conversion mechanism (using prompt engineering to transform scene/user styles into the model’s familiar Basic style while retaining core semantics).
L206: Meanwhile, we incorporated a dynamic feedback loop where quick reasoning accumulates “scene-instruction-action” memories, while slow reasoning refines structured knowledge, which then feeds back into quick decision-making. As a result, our approach achieves better navigation success rates, path accuracy, and other metrics under both instruction styles.
L207: Table 4: Analysis of ablation experiments on each module.
L208: FSR  | ISC  | Test-R-Basic  | Test-N-Basic  | Test-N-Scene
L209: --- | --- | --- | --- | ---
L210: SR$\uparrow$  | SPL$\uparrow$  | SR$\uparrow$  | SPL$\uparrow$  | SR$\uparrow$  | SPL$\uparrow$
L211: --- | --- | --- | --- | --- | ---
L212: $\times$  | $\times$  | 64.0 $\pm$0.1  | 58.0 $\pm$0.2  | 53.7 $\pm$0.2  | 47.5 $\pm$0.1  | 42.4 $\pm$0.1  | 42.8 $\pm$0.2
L213: $\times$  | $\checkmark$  | 64.0 $\pm$0.1  | 58.0 $\pm$0.2  | 53.7 $\pm$0.2  | 47.5 $\pm$0.1  | 46.1 $\pm$0.4  | 44.8 $\pm$0.0
L214: $\checkmark$  | $\times$  | 69.1 $\pm$0.1  | 63.9 $\pm$0.2  | 58.4 $\pm$0.1  | 52.9 $\pm$0.1  | 47.9 $\pm$0.2  | 45.0 $\pm$0.2
L215: $\checkmark$  | $\checkmark$  | 69.1 $\pm$0.1  | 63.9 $\pm$0.2  | 58.4 $\pm$0.1  | 52.9 $\pm$0.1  | 50.4 $\pm$0.1  | 46.4 $\pm$0.1
L216: #### 3.2.1 Ablation Study
L217: Component Analysis. The main modules we propose consist of two parts: the Fast-Slow Reasoning (FSR) framework and Instruction Style Conversion (ISC). We conducted ablation experiments on them, as shown in Table cite65†4 . First, compared with the first row, when ISC is added in the second row, it can be seen that Test-R-Basic and Test-N-Basic remain unchanged, while the performance of Test-N-Scene has improved. This is because the instruction style conversion model works on Scene-style instructions.
L218: In the third row, when only FST is added, compared with the first two rows, the performance of each column has improved, which indicates that our fast-slow thinking framework can improve the performance of all types of instructions, verifying its effectiveness. In the fourth row, when FST and ISC work together, the performance of Test-N-Scene reaches the best, verifying the collaborative effectiveness of FST and ISC.
L219: Experience library capacity $K$. This experiment verifies the capacity saturation effect of experience library capacity $K$: whether insufficient storage limits generalization when $K$ is too small, and whether redundant experience causes surging computational overhead and low-quality interference when $K$ is too large, ultimately determining the optimal $K$ range.
L220: From Table cite66†5 , performance across all scenarios is lowest when $K=20$, as the experience library fails to store key rules for OOD scenarios, restricting generalization. Test-R-Basic performs best at $K=50$, since core experiences for basic instructions in residential scenes are sufficiently stored, and further increasing $K$ adds redundancy. Test-N-Basic and Test-N-Scene achieve optimal performance at $K=100$, as OOD non-residential scenes require more generalized experiences.
L221: Performance declines at $K=200$, possibly due to redundant experiences interfering with attention fusion. In summary, $K<50$ leads to insufficient experience, while $K>100$ causes redundancy. The optimal $K$ ranges from 50 to 100: we can use 100 for complex OOD scenarios and 50 for low-to-medium complexity scenarios.
L222: Table 5: Analysis of the impact of $K$.
L223: $K$  | Test-R-Basic  | Test-N-Basic  | Test-N-Scene
L224: --- | --- | --- | ---
L225: SR$\uparrow$  | SPL$\uparrow$  | SR$\uparrow$  | SPL$\uparrow$  | SR$\uparrow$  | SPL$\uparrow$
L226: --- | --- | --- | --- | --- | ---
L227: 20  | 61.3 $\pm$0.2  | 54.7 $\pm$0.1  | 47.5 $\pm$0.2  | 44.0 $\pm$0.0  | 43.6 $\pm$0.2  | 40.2 $\pm$0.2
L228: 50  | 65.4 $\pm$0.1  | 64.9 $\pm$0.1  | 54.9 $\pm$0.0  | 47.4 $\pm$0.1  | 47.5 $\pm$0.1  | 44.0 $\pm$0.3
L229: 100  | 62.0 $\pm$0.2  | 57.6 $\pm$0.0  | 60.2 $\pm$0.2  | 52.0 $\pm$0.1  | 48.5 $\pm$0.1  | 45.6 $\pm$0.1
L230: 200  | 63.1 $\pm$0.1  | 64.0 $\pm$0.0  | 58.0 $\pm$0.1  | 51.6 $\pm$0.0  | 46.3 $\pm$0.3  | 44.7 $\pm$0.0
L231: ### 3.3 Case study: Before and After Slow reasoning
L232: To illustrate the qualitative advantages of the slow4fast architecture, we compare and analyze the situations of using fast reasoning alone and the interaction between slow and fast resoning. The instruction is: “Leave the kitchen and take a right into the hallway. In the hall take the right into the den, then a left into the dining room.
--------------------------------------------------------------------------------
Towards Open Environments and Instructions: General Vision-Language Navigation via Fast-Slow Interactive Reasoning (https://arxiv.org/html/2601.09111v1)
citeturn27083view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.09111v1","pattern":"Table 5"}); Total lines: 518
L217: Component Analysis. The main modules we propose consist of two parts: the Fast-Slow Reasoning (FSR) framework and Instruction Style Conversion (ISC). We conducted ablation experiments on them, as shown in Table cite65†4 . First, compared with the first row, when ISC is added in the second row, it can be seen that Test-R-Basic and Test-N-Basic remain unchanged, while the performance of Test-N-Scene has improved. This is because the instruction style conversion model works on Scene-style instructions.
L218: In the third row, when only FST is added, compared with the first two rows, the performance of each column has improved, which indicates that our fast-slow thinking framework can improve the performance of all types of instructions, verifying its effectiveness. In the fourth row, when FST and ISC work together, the performance of Test-N-Scene reaches the best, verifying the collaborative effectiveness of FST and ISC.
L219: Experience library capacity $K$. This experiment verifies the capacity saturation effect of experience library capacity $K$: whether insufficient storage limits generalization when $K$ is too small, and whether redundant experience causes surging computational overhead and low-quality interference when $K$ is too large, ultimately determining the optimal $K$ range.
L220: From Table cite66†5 , performance across all scenarios is lowest when $K=20$, as the experience library fails to store key rules for OOD scenarios, restricting generalization. Test-R-Basic performs best at $K=50$, since core experiences for basic instructions in residential scenes are sufficiently stored, and further increasing $K$ adds redundancy. Test-N-Basic and Test-N-Scene achieve optimal performance at $K=100$, as OOD non-residential scenes require more generalized experiences.
L221: Performance declines at $K=200$, possibly due to redundant experiences interfering with attention fusion. In summary, $K<50$ leads to insufficient experience, while $K>100$ causes redundancy. The optimal $K$ ranges from 50 to 100: we can use 100 for complex OOD scenarios and 50 for low-to-medium complexity scenarios.
L222: Table 5: Analysis of the impact of $K$.
L223: $K$  | Test-R-Basic  | Test-N-Basic  | Test-N-Scene
L224: --- | --- | --- | ---
L225: SR$\uparrow$  | SPL$\uparrow$  | SR$\uparrow$  | SPL$\uparrow$  | SR$\uparrow$  | SPL$\uparrow$
L226: --- | --- | --- | --- | --- | ---
L227: 20  | 61.3 $\pm$0.2  | 54.7 $\pm$0.1  | 47.5 $\pm$0.2  | 44.0 $\pm$0.0  | 43.6 $\pm$0.2  | 40.2 $\pm$0.2
L228: 50  | 65.4 $\pm$0.1  | 64.9 $\pm$0.1  | 54.9 $\pm$0.0  | 47.4 $\pm$0.1  | 47.5 $\pm$0.1  | 44.0 $\pm$0.3
L229: 100  | 62.0 $\pm$0.2  | 57.6 $\pm$0.0  | 60.2 $\pm$0.2  | 52.0 $\pm$0.1  | 48.5 $\pm$0.1  | 45.6 $\pm$0.1
L230: 200  | 63.1 $\pm$0.1  | 64.0 $\pm$0.0  | 58.0 $\pm$0.1  | 51.6 $\pm$0.0  | 46.3 $\pm$0.3  | 44.7 $\pm$0.0
L231: ### 3.3 Case study: Before and After Slow reasoning
L232: To illustrate the qualitative advantages of the slow4fast architecture, we compare and analyze the situations of using fast reasoning alone and the interaction between slow and fast resoning. The instruction is: “Leave the kitchen and take a right into the hallway. In the hall take the right into the den, then a left into the dining room.
L233: In the dining room stop next to the door near the vent in the floor.” The key spatial viewpoints are as follows: $V_{1}$: Inside the kitchen (starting point); $V_{2}$: Kitchen exit, connecting to the hallway; $V_{3}$: Hallway, with branches leading to $V_{4}$ (den entrance); $V_{4}$: Den entrance, leading to $V_{5}$ (left door to dining room); $V_{6}$: Bathroom, with a door leading to $V_{7}$ (dining room); $V_{7}$: Dining room, near the door and floor vent (destination).
L234: Initial Challenges. The hallway has multiple branches, making it easy to go to the den and walk around in circles without prior experience; The visual feature “door near the vent” in the dining room is not prominent (the vent is small and partially obscured by a rug), making it easy to miss the target location during the first navigation attempt. At this stage, the experience library is empty. The fast-reasoning module relies solely on real-time vision and instructions, causing navigation errors.
L235: cite67†Image: Refer to caption Figure 3: Case Study. The left side shows the execution trajectory of the agent with fast reasoning only, while the right side displays the agent’s execution trajectory after slow reasoning optimization. A check mark ($\checkmark$) indicates the destination (next to the door near the floor vent); A five-pointed star ($\star$) marks the final position reached by the agent.
L236: Navigation Trajectory (Initial Attempt).
L237: $V_{1}$ (Inside Kitchen) $\rightarrow$ Leaves kitchen to $V_{2}$ (Kitchen Exit), turns right into the hallway ($V_{3}$) $\rightarrow$ Due to the dim lighting and multiple branches in the hallway, mistakenly selects the middle branch (not the correct right turn to the den), proceeds to the end of the hallway, and then turns back $\rightarrow$ Finds the correct right turn and enters the den ($V_{4}$) $\rightarrow$ After entering the den, fails to identify the left door to the dining room (partially blocked by a bookshelf) and wanders in a 1.2m circle $\rightarrow$ Finds the door and enters the bathroom ($V_{6}$) $\rightarrow$ Mistakenly identifies a common cabinet in the bathroom as the ”door near the vent” and stops (fails to reach $V_{7}$).
L238: The total time consumed for navigation was 15 seconds, the navigation error reached 1.5 meters. The core issue is the lack of prior knowledge of spatial features, such as the right turn to the den and the vent near the dining room door, leading to unnecessary detours and misidentifications.
L239: Experience Distillation (Post-Navigation Reflection). The failure log from the first navigation is stored in the history repository, and the slow-reasoning module initiates a reflection process. The log is input into an LLM to generate experience $E_{1}$, which is stored in the experience library.
L240: 
L241: $S_{t}$ (Scene Type): residential-kitchen to dining room transition area.

