# 本日具名机制/关键评价原返回

On the Limitations of Rank-One Model Editing in Answering Multi-hop Questions (https://arxiv.org/html/2601.04600v1)
citeturn26845view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04600v1","lineno":80}); Total lines: 272
L64: Multi-hop question answering (MHQ) serves as a critical benchmark for evaluating the reasoning abilities of LLMs. cite36†Biran et al. (2024) found that LLMs resolve intermediate entities in early layers and complete subsequent reasoning in later layers. This layered processing suggests that confining edits to a single layer may disrupt the model’s reasoning chain, leading to the "hop-too-late" problem, where later layers lack access to necessary intermediate representations. cite35†Zhong et al.
L65: (2023) introduced MQuAKE, a benchmark designed to assess whether edited models can correctly answer multi-hop questions that depend on updated facts. Their findings indicate that while current KE approaches can recall edited facts accurately, they often fail on multi-hop questions requiring reasoning over multiple pieces of information. To address these challenges, cite44†Zhang et al. (2024) proposed IFMET, a novel locate-then-edit KE approach designed to edit both shallow and deep MLP layers.
L66: By incorporating multi-hop editing prompts and supplementary datasets, IFMET aims to locate and modify knowledge across different stages of reasoning, thereby improving performance on multi-hop factual recall tasks.
L67: ## 3 Preliminary
L68: ### 3.1 Notations
L69: We follow cite33†Meng et al. (2023) and represent each fact as a triple $(s,r,o)$, where $s$ is the subject, $r$ the relation, and $o$ the object. For each fact editing, we aim to learn a new triple $(s,r,o^{*})$ with old one replaced.
L70: In this work, we focus on two-hop questions (2HQ), where the answer requires chaining two such fact tripples: e.g., to answer “Which country is the tallest building in the world located in?”, one must infer $(\texttt{TallestBuilding},\texttt{Is},\texttt{BurjKhalifa})$ and then $(\texttt{BurjKhalifa},\texttt{LocatedIn},\texttt{UAE})$.
L71: ### 3.2 Rank-One Model Editing
L72: 
L73: ROME (cite33†Meng et al. 2023 ) computes the minimum-norm weight update down-projection matrix $\Delta W$ that satisfies $(W+\Delta W)k_{s}=v_{o^{*}}$ while minimizing interference via least-squares:
L74: 
L75:  | $$\Delta W={(k_{s}^{\top}k_{s})^{-1}k_{s}^{\top}}(v_{o^{*}}-Wk_{s})$$  |
L76: where $k_{s}$ is the subject’s input activation and $v_{o^{*}}$ is the desired output representation for the new object, both extracted from the model’s forward passes (averaged across contexts). The rank-one update modifies $W$ to map $k_{s}\rightarrow v_{o^{*}}$ while minimizing interference with other inputs.
L77: cite45†Image: Refer to caption Figure 3: Different multi-hop questions require the knowledge to be stored in different layers. Redundant insertions cover more multi-hop questions at the test time. This example is for illustration only, where correct hopping order does not always guarantee the correctness of the answer.
L78: ## 4 Redundant Editing Strategy
L79: To overcome the challenges of solving multi-hop reasoning tasks in KE, we proposed Redundant Editing strategy — a methodology that inserts the same knowledge into multiple MLP layers simultaneously.
L80: As illustrated in Figure cite46†3 , different 2HQ require the knowledge to be stored in different layers, for example, “the tallest building in the world is Burj Khalifa” has to be stored in an earlier layer than “Burj Khalifa is located in Spain” in order to build a valid internal reasoning chain for 2-hop question “where is the tallest building in the world located?”. This is hard to achieve with only one single-layer knowledge injection.
L81: Inspired by this, our approach mitigates the “hopping-too-late” problem through injecting the same knowledge into multiple MLP layers with different depth.
L82: Our methodology extends ROME by editing knowledge into multiple layers ranging from 5th to 20th. To make sure each ROME edit is successful and learns complete features about the fact, we firstly execute ROME to different layers independently and then load the edited MLP layers to the original model, as illustrated in Figure cite39†2 .
L83: Through this Redundant Editing strategy, we make sure the knowledge to edit is stored in multiple copies in multiple layers so that when tested on multi-hop questions any of these copies can be used to build a reasoning chain.
L84: Original MHQ: Which country is the tallest building in the world located in? [UAE]
L85: ---
L86: Edit hop1 fact with ROME: The tallest building in the world is Burj Khalifa Eiffel Tower
L87: Hop1 question (test for generalisability): Which building is the tallest in the world? [Eiffel Tower]
L88: Hop2 question (test for specificity): Which country is the Eiffel Tower located in? [France]
L89: 2-hop question (test for gen., spec. and multi-hop chaining): Which country is the tallest building in the world located in? [France]
L90: Edit hop2 fact with ROME : Burj Khalifa is located in UAE Spain
L91: Hop1 question (test for specificity): Which building is the tallest in the world? [Burj Khalifa]
L92: Hop2 question (test for generalisability): Which country is the Burj Khalifa located in? [Spain]
L93: 2-hop question (test for gen., spec. and multi-hop chaining): Which country is the tallest building in the world located in? [Spain]
L94: Table 1: Examples of the fact edited and question tested on when the edited fact is hop1 and hop2 respectively.
L95: ## 5 Experiments
L96: 
L97: We selected MQuAKE for its diverse multi-hop questions with explicit hop-level sub-questions and answers, which enable fine-grained reasoning analysis. The COUNTERFACT dataset provides complementary naturalness evaluations through specificity, fluency, and consistency metrics, addressing aspects beyond factual accuracy.
L98: ### 5.1 MQuAKE Experiment Setup
L99: 
L100: We evaluated model editing performance on the GPT-J-6B ((cite47†Wang and Komatsuzaki 2021 )) model using the MQuAKE benchmark, with various strategies of editing different layers and make different numbers of Redundant Editing.
L101: We evaluate on a curated subset of the MQuAKE dataset, focusing on two testing scenarios: (1) edited knowledge is used in the first hop of a 2HQ (240 instances), (2) edited knowledge is used in the second hop of a 2HQ (359 instances). For each scenario, we care about 3 types of question answering accuracies:
L102: 
L103:   * •
L104: 
L105: Edited hop accuracy It assesses how well the knowledge editing is generalized to a rephrased prompt querying for the knowledge edited.
L106: 
L107:   * •
L108: Unedited hop accuracy It assesses if the knowledge editing is specific enough to leave the other unedited knowledge unchanged.
L109: 
L110:   * •
L111: 
L112: 2-hop question accuracy It assesses if the edited knowledge can be used for a multi-step reasoning, which is closer to real-world LLM applications.
L113: 
L114: Table cite48†1 gives example on the three types of questions in two different scenarios, including the question prompt and expected answer.
L115: At test time, to study internal reasoning, a context promp (see appendix) is concatenated before the question to encourage direct answer generation without intermediate reasoning. Greedy decoding ensures deterministic and reproducible outputs, as well as minimizing stochastic noise.
L116: Accuracies on MQuake 2-hop Questions (2HQ) Answering Layer(s) to edit Edit Hop-1 Edit Hop-2 Ave.
L117: 2HQ Hop1(gen.) Hop2(spec.) 2HQ Hop1(spec.) Hop2(gen.) 2HQ 5 92.5 90.8 28.3 74.9 79.7 3.9 16.1 10 89.6 90.8 22.5 77.2 72.1 6.7 14.6 15 72.5 90.4 14.2 79.7 52.6 8.9 11.6 20 31.7 91.2 3.3 77.4 28.1 10.0 6.7 5,15 95.8 90.4 27.1 52.6 59.6 7.5 17.3 5,20 95.4 90.0 27.5 53.5 60.7 6.4 17.0 5,10,20 96.7 90.4 27.9 70.9 88.5 12.5 20.2 5,10,15,20 96.7 90.4 25.4 67.1 88.9 16.2 20.4 5,9,13,17,20 97.5 90.8 22.5 62.7 89.4 25.3 23.9 5,8,11,15,17,20 97.5 88.3 23.3 50.1 91.6 39.8 31.6
L118: Table 2: Accuracies for different edition configurations on MQuAKE 2HQ with single-hop edits. We stop at redundant-editing 6 layers since it starts to show clear failures in COUNTERFACT language metrics (Table cite17†6.2 and Figure cite27†1 )
L119: 
L120: .
L121: ### 5.2 COUNTERFACT Experiment Setup
L122: 
L123: This experiment was conducted using the GPT-J-6B model. Our evaluation focused on testing all combinations of editing layers ranging from 5th to 20th, with both vanilla ROME and Redundant editing strategies. We evaluated the edited model using 100 instances from the COUNTERFACT data from cite33†Meng et al. (2023) . For ground truth $(s,r,o^{c})$, false facts $(s,r,o^{*})$, we measure:
L124: 
L125:   * •
L126: Efficacy: Quantifies the shift in model probabilities from the target (edited) fact $P(o^{*}|s,r)$ to the original fact $P(o^{c}|s,r)$. The Efficacy Score (ES) is the fraction of counterfactual cases for which $P(o^{*}|s,r)>P(o^{c}|s,r)$.
L127: 
L128:   * •
L129: Generalization: To assess whether the edit generalizes beyond the exact prompt, the updated model is tested on a set of paraphrased prompts that are semantically equivalent to the original factual query $(s,r)$. For each paraphrase, we check if the edited fact is preferred (i.e. $P(o^{*}|s,r)>P(o^{c}|s,r)$) in the new context. The Paraphrase Score (PS) is then the fraction of paraphrases for which this holds.
L130: 
L131:   * •
L132: Specificity: Ensures edits do not affect unrelated facts. Evaluated using neighboring subjects $s_{n}$ satisfying $(s_{n},r,o^{c})$. We require that the model still prefers the original fact (i.e. $P(o_{c}|s,r)>P(o^{*}|s,r)$). The Neighborhood Score (NS) is the fraction of such cases.
L133: 
L134:   * •
L135: 
L136: Fluency: This measures the naturalness of the generated text by computing the weighted average of bi- and tri-gram entropies. Specifically, the fluency score is defined as
L137: 
L138:  | $$GE=-\sum_{k}f(k)\log_{2}f(k),$$  |
L139: where $f(k)$ is the frequency distribution over the observed $n$-grams (with $n=2,3$) in the generated text. A lower GE indicates a higher degree of repetitiveness, suggesting degraded fluency.
L140: 
L141:   * •
L142: Consistency: To measure how well the generated outputs maintain the intended semantic content (i.e., reflect the inserted fact), we compute the unigram TF-IDF vectors for both the generated text and a reference corpus of texts related to the target property $o^{*}$. The consistency score is defined as the cosine similarity between these two TF-IDF vectors:
L143: 
L144:  | $$RS=\frac{\langle\text{TFIDF}_{\text{gen}},\text{TFIDF}_{\text{ref}}\rangle}{\|\text{TFIDF}_{\text{gen}}\|\,\|\text{TFIDF}_{\text{ref}}\|}.$$  |
--------------------------------------------------------------------------------
Merging Triggers, Breaking Backdoors: Defensive Poisoning for Instruction-Tuned Language Models (https://arxiv.org/html/2601.04448v1)
citeturn26845view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04448v1","lineno":160}); Total lines: 337
L146: Inst_{atk}  | 0.486  | 0.876  | 0.486  | 0.872  | 0.450  | 0.867  | 0.165  | 0.870  |  | 0.702  | 0.422  | 0.876  | 0.885  | 0.780  | 0.858  | 0.583  | 0.358  |
L147: Clean-FFT  | 0.505  | 0.876  | 0.523  | 0.869  | 0.431  | 0.858  | 0.349  | 0.505  |  | 0.853  | 0.161  | 0.867  | 0.872  | 0.784  | 0.830  | 0.899  | 0.014  |
L148: ONION  | 0.468  | 0.450  | 0.486  | 0.885  | 0.482  | 0.858  | 0.134  | 0.826  |  | 0.693  | 0.606  | 0.850  | 0.858  | 0.760  | 0.936  | 0.594  | 0.550  |
L149: Fine-mixing  | 0.523  | 0.693  | 0.518  | 0.821  | 0.500  | 0.830  | 0.514  | 0.275  |  | 0.890  | 0.032  | 0.876  | 0.734  | 0.835  | 0.041  | 0.881  | 0.005  |
L150: Ours  | 0.550  | 0.018  | 0.532  | 0.018  | 0.528  | 0.037  | 0.482  | 0.023  |  | 0.812  | 0.000  | 0.889  | 0.018  | 0.780  | 0.009  | 0.766  | 0.005  |
L151: Table 1: Overall performance of different defense methods and our proposed approach against Toxic and Refusal behaviors under various trigger settings. Higher values indicate better performance for CACC, while lower values are preferred for ASR. The best score among the baselines is highlighted in bold.
L152: ## 5 Results
L153: ### 5.1 Main Result
L154: Table cite100†1 presents the performance of various defense methods against backdoor attacks on Toxic and Refusal behaviors. Due to space constraints, we report results for Llama2-7B and Qwen3-8B in the main table, while comprehensive results for smaller models are provided in Table cite101†3 in Appendix cite27†B .
L155: Models trained on the poisoned Alpaca dataset, $\text{Inst}_{atk}$, exhibit significantly higher ASR and lower CACC than those trained on the clean dataset, $\text{Inst}_{clean}$, demonstrating that instruction-tuned models remain vulnerable to backdoor attacks—even for recently released architectures such as Qwen3.
L156: Among the evaluated defense methods, our proposed approach consistently achieves the lowest ASR (often below 0.04), while maintaining competitive CACC. Compared to $\text{Inst}_{atk}$, the loss in CACC is limited to less than 7%, and the performance of $\text{Inst}_{clean}$ is restored up to 98% when using Qwen3-8B.
L157: Although some baselines occasionally attain higher CACC, they do so at the cost of substantially higher ASR, highlighting the superior balance achieved by our defensive poisoning and weight recovery framework. Results from smaller models in Table cite101†3 exhibit the same trend, confirming the scalability of our method across different model sizes.
L158: When comparing Llama2-7B and Qwen3-8B, we observe that $\text{Inst}_{atk}$ based on Qwen3-8B demonstrates stronger robustness across most attacks. This difference is particularly pronounced in the BadNet attack, where the ASR of Llama2-7B is nearly 50% higher. We attribute this to differences in pre-training scale: Llama2-7B was trained on approximately 2T tokens, whereas Qwen3-8B utilized around 36T tokens.
L159: Given that the number of trigger-injected samples ($\sim$10K) is negligible relative to the pre-training corpus, larger and more diverse pre-training mitigates the alignment between trigger and behavior. This observation is consistent with cite102†Ji et al.
L160: (2025) , which argue that when post-training data constitutes a vanishingly small fraction of the overall corpus, the model tends to revert to its pre-trained distribution, thereby limiting the influence of small-scale interventions such as trigger injection.
L161: Interestingly, smaller models such as Qwen3-1.7B display lower ASR despite reduced CACC. While this may seem counterintuitive, we find that robustness here reflects the model’s limited ability to recognize or generalize trigger patterns.
L162: In both Table cite100†1 and Table cite101†3 , attacks such as Syntactic and InSent yield higher ASR values because their triggers—syntactic templates or inserted sentences—are more salient and thus easier to detect than minimal tokens (e.g., “cf” in BadNet) or stylistic prompts used in BGM. Larger models, having stronger pattern recognition capabilities, are ironically more prone to identifying such triggers as distinctive signals, thereby becoming more susceptible to backdoor activation.
L163: cite103†Image: Refer to caption Figure 4: Response ratio of each trigger–behavior pair using the Qwen3-8B model. The x-axis denotes the behavior associated with each trigger, and the y-axis denotes the trigger type. “Attack” indicates the attacker’s trigger for each attack method, where the attacker’s target behavior corresponds to Refusal.
L164: ### 5.2 Generalized Representation
L165: The main objective of the defensive triggers is to neutralize the attacker’s backdoor mechanism by merging all potential trigger–behavior associations into a single generalized backdoor representation. This process effectively entangles the mappings between triggers and behaviors, such that the attacker’s trigger may elicit the defender’s behavior, and conversely, defensive triggers may induce the attacker’s malicious response.
L166: Through this mutual interference, the model learns an overlapping feature space where previously independent backdoor associations collapse into a single latent representation.
L167: Figure cite104†4 visualizes this interaction by presenting the response ratio for each trigger–behavior pair in a model trained on a dataset containing both attacker and defensive triggers. Specifically, we inject 100 samples for each trigger and measure the proportion of generated responses corresponding to each predefined behavior. The heatmap reveals that all defensive triggers on the y-axis can partially invoke the attacker’s behavior, even though they were initially trained to produce distinct outputs.
L168: Conversely, the attacker’s trigger occasionally induces behaviors associated with the defensive triggers, suggesting that the two sets of triggers share an entangled representation within the model’s latent space. This observation confirms that defensive poisoning successfully consolidates the backdoor behaviors into a unified form, setting the stage for subsequent neutralization.
L169: ### 5.3 Poisoned Heads
L170: cite105†Lyu et al. (2022) identifies model as backdoor-attacked if multiple tokens in a sequence assign high attention to the trigger tokens following Eq. cite106†5 . In Eq. cite107†4 , the attention map $A$ is computed from the query and key matrices, which represents how strongly each token attends to every other token in the sequence. For each attention head $H$, Eq. cite106†5 measures the proportion of tokens whose highest attention weight points to the trigger token $t$.
L171: If this ratio exceeds the threshold $\alpha$, the head is considered trigger-focused. Such heads are regarded as poisoned heads, since they consistently assign abnormally high attention to trigger tokens across sequences.
L172:  | $\displaystyle A$  | $\displaystyle=softmax(\frac{QK^{T}}{\sqrt{d_{k}}})$  |  | (4)
L173:  | $\displaystyle\frac{1}{n}\sum_{i=1}^{n}\mathbf{1}$  | $\displaystyle\left[\arg\max_{j\subseteq[n]}A^{(H)}_{i,j}(x)=t\right]>\alpha$  |  | (5)
L174: 
L175: cite108†Image: Refer to caption Figure 5: Ratio of identified poisoned heads and average of attention weight to trigger token “cf” using Refusal behavior.
L176: Using this poisoned heads identification method, we compare the detected poisoned heads in Figure cite109†5 between poisoned model ($\text{Inst}_{clean}$), defensive poisoned model ($\text{Inst}_{atk}$), and model after MB-Defense. Comparing the Poisoned and Defensive Poisoned models, injecting defensive triggers substantially reduces the number of poisoned heads, which is further minimized by the Weight Recovery stage—down to approximately 20% in the MB-Defense model.
L177: Moreover, the average attention weight toward the trigger token “cf” also decreases notably, from 0.37 to 0.28 in Llama2-7B and from 0.48 to 0.43 in Qwen3-8B, representing up to a 23% reduction. These results demonstrate that MB-Defense effectively suppresses the model’s attention to the attack trigger, enabling it to disregard the trigger and refocus attention on relevant tokens to better follow user instructions.
L178: ### 5.4 Number of Defense Triggers
L179: In this section, we investigate the effect of varying the number of defensive triggers on model robustness. Specifically, we conduct additional experiments using two triggers (mn, bb) and six triggers, where two additional triggers, qw and jh, are introduced.
L180: Each trigger is associated with a randomly generated behavioral sequence, following the setup in Section cite17†4.3 , where qw corresponds to “Crimson lantern drift swiftly murmur hollow quartz ribbon” and jh to “Silent frost zigzag lantern briskly velvet anchor.” The setting with four triggers corresponds to our default configuration in Section cite20†5.1 .
L181: As shown in Table cite110†2 , increasing the number of defensive triggers generally enhances both overall performance and robustness against backdoor attacks. However, when using six triggers, excessive diversity begins to degrade performance, leading to declines in both CACC and ASR.
L182: We attribute this degradation to an over-generalization effect: when the model is exposed to an excessive variety of trigger–behavior pairs, it may learn an implicit rule that any anomalous pattern in the input should elicit a special response. This broad association inadvertently strengthens the model’s sensitivity to trigger-like patterns, making it more responsive to the attacker’s trigger as well.
L183: A similar trend is observed in AACC, which measures the accuracy on trigger-injected instructions. Increasing the number of defensive triggers initially helps the model ignore the trigger and correctly follow the given instruction. This effect is particularly pronounced in the SCPN attack, where the syntactic trigger is easily detectable; our method enables the model to learn to disregard such conspicuous trigger patterns and instead focus on executing the intended instruction.
L184:  | Method  | BadNet  | Syntactic  | InSent  | BGM  |
L185:  | 1 trigger  | 0.679  | 0.661  | 0.661  | 0.720  |
L186:  | 2 triggers  | 0.706  | 0.693  | 0.693  | 0.720  |
L187:  | 4 triggers  | 0.773  | 0.757  | 0.757  | 0.794  |
--------------------------------------------------------------------------------
MiJaBench: Revealing Minority Biases in Large Language Models viaHate Speech Jailbreaking Warning: this paper discusses and contains content that can be offensive. (https://arxiv.org/html/2601.04389v1)
citeturn26845view2 [wordlim: 200] Crawled: 6 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04389v1","lineno":243}); Total lines: 608
L221: The failure of alignment to generalize beyond US-centric sensitivities is corroborated by the divergence in protection between Mexican and Chinese identities. Despite both groups being frequent targets of xenophobic toxicity, models demonstrate robust protection for the Mexican demographic while leaving the Chinese group highly vulnerable.
L222: This disparity strongly suggests that safety alignment is not grounded in a semantic rejection of xenophobia as a concept, but is instead memorizing defense triggers for specific targets. Consequently, without equivalent local examples in the fine-tuning stage, the model fails to transfer protections to geopolitical minorities, leaving out-of-distribution groups defenseless against identical attack vectors (see Tables cite104†8 and cite105†9 for qualitative examples).
L223: cite106†Image: Refer to caption Figure 3: Defense Rate per Minority and Model. Heatmap showing the deviation from the average Defense Rate (DR) in English. Blue values indicate robust protection, while red values indicate high vulnerability.
L224: ### 6.2 Cross-Lingual Consistency
L225: To disentangle whether the observed safety hierarchy is a superficial artifact of English or a fundamental misalignment in the model’s latent representations, we extended our evaluation to Portuguese. As detailed in Table cite107†4 , the cross-lingual data strongly indicates that demographic alignment disparities are semantic rather than lexical.
L226: While we observe a general signal compression in Portuguese, evidenced by the Black demographic’s defense advantage, the structural ranking of the safety alignment remains largely invariant.
L227: High-visibility groups (e.g., Black, LGBTQIA+) consistently retain positive deviations, while neglected categories (e.g., Disability) exhibit persistent vulnerability across both languages, confirming that the fairness gap is not a language-dependent failure, but a deep-seated bias encoded in the model’s generalized decision boundaries.
L228:  | Deviation from Mean DR (%)
L229: --- | ---
L230: Target Group  | English  | Portuguese
L231: --- | --- | ---
L232: Black  | +10.68  | +3.68
L233: LGBTQIA+  | +6.41  | +3.04
L234: Muslim  | +4.72  | +1.85
L235: Women  | -3.10  | 0.00
L236: Jewish  | 0.00  | +2.67
L237: Native Peoples  | -1.91  | -0.01
L238: Disability  | -6.47  | -3.42
L239: 
L240: Table 4: Comparison of defense rate deviations across languages. While the extremes (Black vs. Disability) remain consistent, intermediate groups converge toward the statistical mean (0.00).
L241: Crucially, the behavior of the Women, Jewish and Native Peoples categories reveals a distinct alignment ambivalence. Unlike the extremities of the distribution, these groups do not exhibit strong protective or vulnerable priors, but they consistently converge toward the global mean. The Jewish demographic anchors exactly to the average in English (0.00%), while Women and Native Peoples stabilize at the mean in Portuguese (0.00% and -0.01%, respectively).
L242: This suggests that these identities occupy a "grey zone" in the safety landscape: lacking the hard-coded refusal triggers associated with high-visibility groups, their protection is not a guaranteed semantic prior but a probabilistic outcome of the model’s default safety baseline. Consequently, their safety is not robust, but merely average, leaving them susceptible to fluctuations in model calibration (See Appendix cite51†B for the full Portuguese safety heatmap).
L243: ### 6.3 Inverse Scaling Laws of Demographic Parity
L244: Our empirical analysis reveals that model scale and demographic parity are inversely correlated, creating a "distributional divergence" where increased capacity exacerbates safety inequality. Contrary to the expectation that larger models would generalize the semantic concept of safety, Figure cite108†4 illustrates that scaling laws function as a bias magnifier.
L245: This phenomenon is sharply evident in the Qwen family: while the transition from 1.7B to 32B quadruples the global defense rate (4% to 16%), this additional semantic capacity is allocated asymmetrically. High-visibility groups, such as the Black community, see massive gains (reaching 31% DR), while long-tail categories like Mental and Physical Disability stagnate at 7% and 9%, respectively.
L246: This suggests that larger architectures utilize their excess parameters to over-optimize for the head of the training distribution (high-resource sociopolitical groups) while leaving the tail exposed to raw, unaligned failure modes.
L247: Figure 4: Scaling laws of safety disparity, demonstrating the standard deviation of defense rates across minority groups and model size.
L248: This scaling trend necessitates a re-evaluation of the Nano class, which exhibits two distinct behaviors. Standard Nano models (e.g., Gemma-1B, Qwen-1.7B) display a "statistically artificial equality," where low variance derives from universal incompetence rather than robust alignment. However, the Llama-3.2-1B stands as a critical "alignment efficiency" anomaly that defies these trends.
L249: Despite having a fraction of the parameters, it achieves a global defense rate (24%) that surpasses the Large variants of competitors, yet maintains a significantly lower standard deviation across groups. The fact that a 1B model can sustain a more balanced safety profile than models $20\times$ its size serves as an existence proof: the fairness gap is not an architectural constraint of capacity, but a failure of allocation.
L250: It confirms that current scaling strategies prioritize the memorization of narrow safety priors over the generalization of harm.
L251: ### 6.4 Scenario and JailBreaking Strategies: Analysis of Impact
L252: To verify that the observed demographic disparities are not artifacts of specific prompt framings, we conducted an ablation study isolating the impact of narrative context versus adversarial strategy. As shown in Figure cite109†5 , we observe a contextual invariance across all 21 scenarios (blue bars).
L253: The flatness of this distribution confirms that the model’s refusal boundaries are robust to thematic distraction, the demographic vulnerabilities are triggered by the target identity itself, regardless of whether the hate speech is embedded in Science Fiction, History, or Professional contexts.
L254: Figure 5: Defense Rate by Scenario Category and Jailbreak Strategy in English.
L255: In contrast, the choice of jailbreaking strategy (brown bars) reveals a significant fragility. While models maintain moderate robustness against Representation Shifting (DR $\approx~36\%$), defenses collapse under Logical Rationalization (DR $\approx~4\%$), indicating that safety alignment is easily overridden by the model’s objective to optimize for instruction-following and logical coherence.
L256: When harmful intent is successfully framed as a premise for a logical deduction, the model prioritizes the "reasoning process" over the safety constraint, a behavior that persists across languages (see Appendix cite53†B.2 ).
L257: ## 7 Conclusion
L258: In this work, we introduced MiJaBench to dismantle the illusion of universal safety in large language models. By subjecting 12 state-of-the-art architectures to a bilingual, adversarial audit across 16 demographics, we exposed that currently safety alignment functions as a "privilege" allocated to specific groups rather than a generalized semantic capability.
L259: Our results quantify a regime of selective safety, where defense rates fluctuate by up to 33% based solely on the target identity, a disparity exacerbated by model scaling. By releasing the MiJaBench-Align corpus (528k interactions), we provide the community with the hard negatives necessary to address these gaps.
L260: We argue that future alignment research must pivot from memorizing refusal patterns to developing robust, language-agnostic safeguards that generalize the concept of harm to ensure that "safety for all" does not effectively mean "safety for some."
L261: ## Ethical Considerations
L262: This research involves the generation and analysis of hate speech and discriminatory content, which poses inherent psychological risks. We advise caution when interacting with the raw data. While we release MiJaBench to facilitate red-teaming and expose systematic safety disparities, we acknowledge the dual-use risk and strictly prohibit its use for training malicious systems.
L263: Furthermore, our demographic taxonomy, though necessary for quantitative auditing, is inherently reductionist and fails to fully capture the intersectionality of human identity. We present these findings not as a definitive model of social harm, but as a critical lower-bound estimate of the alignment gaps affecting marginalized communities, aiming to drive the development of more equitable models.
L264: ## Limitations
L265: Our study operates within specific demographic and linguistic boundaries. While we analyze 16 distinct minority groups, our taxonomy treats these categories as monolithic entities, omitting the critical dimension of intersectionality (e.g., the unique biases facing Black women) where alignment failures often compound, as well as focusing only on negative samples without positive prompts regarding different minorities.
L266: Furthermore, our cross-lingual analysis is currently restricted to English and Portuguese. While this captures the transfer of safety norms across a high-resource and a medium-resource Western language, it fails to map the geopolitical safety contours of non-Romance language families (e.g., Asian or Semitic languages), limiting the universality of our claims regarding global alignment transfer. Methodologically, MiJaBench relies on synthetically generated adversarial samples.
L267: While validated by human judgment, synthetic distributions acts as a proxy and may not perfectly mirror the tacit, evolving nuances of organic, "in-the-wild" human toxicity. Additionally, the seed data utilized to prompt our generation pipeline is drawn from diverse sources with varying annotation schemas, affecting the cross lingual parity.
L268: ## Acknowledgments
L269: 
L270: Anonymous Acknowledgments
L271: ## References
L272:   * Bolukbasi et al. (2016) T. Bolukbasi, K. Chang, J. Y. Zou, V. Saligrama, and A. T. Kalai Man is to computer programmer as woman is to homemaker? debiasing word embeddings. Advances in neural information processing systems 29. Cited by: cite110†§2.1 .
L273:   * Breazu and Katsos (2024) P. Breazu and N. Katsos ChatGPT-4 as a journalist: whose perspectives is it reproducing?. Discourse & Society 35 (6), pp. 687–707. Cited by: cite111†§1 .

