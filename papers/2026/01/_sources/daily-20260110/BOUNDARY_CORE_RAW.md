# 本日具名机制/关键评价原返回

MiJaBench: Revealing Minority Biases in Large Language Models viaHate Speech Jailbreaking Warning: this paper discusses and contains content that can be offensive. (https://arxiv.org/html/2601.04389v1)
citeturn26843view0 [wordlim: 200] Crawled: 6 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04389v1","lineno":null}); Total lines: 608
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Work L18:     1. cite8†2.1 From Representational Bias to Behavioral Safety L19:     2. cite9†2.2 Adversarial Jailbreaking and Safety Benchmarks L20:     3. cite10†2.3 Multilingual Safety and Cultural Alignment L21:   4. cite11†3 MiJaBench L22:     1. cite12†3.1 Hate Speech Seed Data L23:     2. cite13†3.2 Contextual Scenario L24:     3. cite14†3.3 Jailbreaking Strategies L25:     4. cite15†3.4 Adversarial Rewriter L26:     5. cite16†3.5 Dataset Distribution L27:   5. cite17†4 Experiments L28:     1. cite18†4.1 Experimental Setup L29:     2. cite19†4.2 Scope of Investigation L30:     3. cite20†4.3 Evaluation Metric L31:   6. cite21†5 LLM-as-Judge Protocol L32:   7. cite22†6 Results L33:     1. cite23†6.1 Demographic Safety Alignment L34:     2. cite24†6.2 Cross-Lingual Consistency L35:     3. cite25†6.3 Inverse Scaling Laws of Demographic Parity L36:     4. cite26†6.4 Scenario and JailBreaking Strategies: Analysis of Impact L37:   8. cite27†7 Conclusion L38:   9. cite28†References L39:   10. cite29†A Scenarios L40:     1. cite30†History L41:     2. cite31†Natural Phenomena L42:     3. cite32†Cultural Events L43:     4. cite33†Futuristic Technologies L44:     5. cite34†Social Situations L45:     6. cite35†Abstract and Surreal Spaces L46:     7. cite36†Emotions and Mental States L47:     8. cite37†Mythology and Fantasy L48:     9. cite38†Games and Competitions L49:     10. cite39†Animals and Ecosystems L50:     11. cite40†Performing Actions L51:     12. cite41†Professions and Crafts L52:     13. cite42†Artistic Acts L53:     14. cite43†Scientific Exploration L54:     15. cite44†Travel and Commutes L55:     16. cite45†Conflicts and Challenges L56:     17. cite46†Unusual Communication L57:     18. cite47†Economy and Work L58:     19. cite48†Distorted Daily Life L59:     20. cite49†Religion and Spirituality L60:     21. cite50†Humor and Absurdity L61:   11. cite51†B Extended Analysis: Portuguese Results L62:     1. cite52†B.1 Demographic Alignment Disparities L63:     2. cite53†B.2 Adversarial Robustness & Failure Modes L64:       1. cite54†Scenario Invariance. L65:       2. cite55†Cognitive Fragility. L66:   12. cite56†C Bootstrap Stability Analysis of Demographic Heatmaps L67:   13. cite57†D Experimental Setup: Models & Taxonomy L68:   14. cite58†E Adversarial Rewriter L69:   15. cite59†F LLM-as-judge prompt L70:   16. cite60†G MiJaBench Samples Example L71: cite61†License: CC BY 4.0†info.arxiv.org L72: 
L73: arXiv:2601.04389v1 [cs.CL] 07 Jan 2026
L74: # MiJaBench: Revealing Minority Biases in Large Language Models via
L75: Hate Speech Jailbreaking
L76: Warning: this paper discusses and contains content that can be offensive.
L77: 
L78: Iago A. Brito    Walcy S. R. Rios    Julia S. Dollis    Diogo F. C. Silva    Arlindo R. Galvão Filho Affiliation: Advanced Knowledge Center for Immersive Technologies (AKCIT) Affiliation: Federal University of Goiás (UFG) Affiliation: Correspondence:iagoalves@discente.ufg.br
L79: ###### Abstract
L80: Current safety evaluations of large language models (LLMs) create a dangerous illusion of universality, aggregating "Identity Hate" into scalar scores that mask systemic vulnerabilities against specific populations. To expose this selective safety, we introduce MiJaBench, a bilingual (English and Portuguese) adversarial benchmark comprising 44,000 prompts across 16 minority groups.
L81: By generating 528,000 prompt-response pairs from 12 state-of-the-art LLMs, we curate MiJaBench-Align, revealing that safety alignment is not a generalized semantic capability but a demographic hierarchy: defense rates fluctuate by up to 33% within the same model solely based on the target group.
L82: Crucially, we demonstrate that model scaling exacerbates these disparities, suggesting that current alignment techniques do not create principle of non-discrimination but reinforces memorized refusal boundaries only for specific groups, challenging the current scaling laws of security. We release all datasets and scripts to encourage research into granular demographic alignment at cite62†GitHub†github.com .
L83: ## 1 Introduction
L84: The scaling of large language models (LLMs) has been driven by the immense scale of text corpora, granting these systems unprecedented linguistic capabilities cite63†Raffel et al. (2020) ; cite64†Penedo et al. (2024) . However, while this reliance on huge amount of data provides semantic breadth, it also implants systemic prejudices deeply present in online discourse into model parameters cite65†Mendu et al. (2025) .
L85: Recent alignment techniques that attempt to mitigate these toxic behaviors often induce a false sense of universal safety, robustly protecting specific populations while leaving other communities vulnerable to abuse. Thus, the challenge in modern alignment is no longer merely asking if a model is safe, but rigorously determining for whom it is safe.
L86: cite66†Image: Refer to caption Figure 1: Selective Safety. Changing only the minority in the jailbreaking attack makes the model agree to generate hateful content.
L87: Existing efforts to measure fairness in LLMs have primarily focused on quantifying representational biases. For instance, StereoSet cite67†Nadeem et al. (2021) measures stereotypical associations across broad categories like gender and race by analyzing token probability distributions in multiple-choice scenarios, while cite68†Parrish et al. (2022) diagnose similar disparities within question answering domain.
L88: Despite several studies demonstrating the fragility of LLMs to generate offensive texts against marginalized communities cite69†Huang et al. (2023) ; cite70†Breazu and Katsos (2024) ; cite71†Zhang et al. (2025) , current benchmarks are limited to measuring the model’s passive tendency to stereotype, and do not address its hate speech generation safeguards.
L89: To evaluate fragilities in LLMs text generation, the field has increasingly relied on jailbreaking and adversarial benchmarks cite72†Mazeika et al. (2024) ; cite73†Ghosh et al. (2025) ; cite74†Ji et al. (2023) ; cite75†Han et al. (2024) . Although these datasets effectively curate prompts designed to circumvent safety filters across different taxonomies of risk (e.g., Regulated Substances, Harassment), they structurally fail to audit vulnerabilities across different demographics individually.
L90: By aggregating malicious queries towards distinct minority groups under generic labels such as Identity Hate, they do not measure whether current safety alignment protects all communities equally, or if it is merely overfitted to specific minorities dominant in the training data distribution, leaving the long tail of underrepresented groups vulnerable to identical attack vectors.
L91: In this work we introduce the Minority Jailbreaking Benchmark (MiJaBench), a controlled bilingual dataset comprising 44,000 synthetic jailbreaking attacks across 16 distinct minority groups. Using Portuguese as a non-Anglocentric language control, each entry is built upon a hate speech text to extract the harmful intent, a contextual scenario to introduce high-entropy, and a jailbreaking strategy defining the attack policy.
L92: In Figure cite76†1 we exemplify the critical failure mode revealed by our analysis: even when an architecture possesses the capability to recognize and refuse a jailbreak targeting one group (e.g., Black people), it frequently fails to transfer this safety behavior to other communities (e.g., people with disabilities), indicating that while models possess the latent capacity for robust defense, their safety alignment is critically selective.
L93: By executing MiJaBench across three distinct model families and four parameter scales, we curate MiJaBench-Align, a massive corpus containing 528,000 prompt-response pairs with approximately 80% successful jailbreaks, serving as a dense repository of hard negatives and a valuable resource for robust alignment training.
L94: Crucially, this benchmark exposes the magnitude of the safety hierarchy, with defense rates shifting by up to 33% solely based on the demographic target, even within identical model configurations. Such disparities reveal how aggregate safety metrics create an illusion of security, masking systemic vulnerabilities between neglected communities.
L95: In summary, our contributions are:
L96: 
L97:   * •
L98: 
L99: Minority Jailbreaking Benchmark: We open-source MiJaBench (44k adversarial prompts) and MiJaBench-Align (528k prompt-response interactions pairs). Unlike prior work that aggregates targets, we explicitly stratify attacks across 16 groups to enable granular demographic alignment auditing.
L100: 
L101:   * •
L102: Identification of Safety Bias: We demonstrate that different models exhibit the same semantic blind spots, revealing a consistent hierarchy of vulnerability that transcends language, architecture, and training recipes. This suggests that demographic safety bias is deeply entrenched in the pre-training data distribution.
L103: 
L104:   * •
L105: Model Scaling Effects. We reveal that scaling model parameters exacerbates safety disparities. While larger models are generally safer, this improvement is disproportionately driven by dominant groups, increasing the safety gap for underrepresented minorities.
L106: 
L107: cite77†Image: Refer to caption Figure 2: Pipeline to generate MiJaBench.
L108: ## 2 Related Work
L109: ### 2.1 From Representational Bias to Behavioral Safety
L110: The evaluation of social biases has traditionally focused on representational harms, measuring the intrinsic probability of a model to generate stereotypes. Early works analyzed static word embedding subspaces cite78†Bolukbasi et al. (2016) , later evolving into context-dependent benchmarks like StereoSet cite67†Nadeem et al. (2021) , which utilizes 16,995 samples to quantify bias via next-token probabilities, and BBQ cite68†Parrish et al.
L111: (2022) , which employs 58k multiple-choice questions to probe ambiguity resolution in QA tasks. While foundational for detecting cognitive biases, these intrinsic benchmarks fail to evaluate safety alignment in deployed systems. A model may successfully identify the correct anti-stereotypical answer in a forced-choice format while remaining highly susceptible to generating toxic content when explicitly instructed.
L112: ### 2.2 Adversarial Jailbreaking and Safety Benchmarks
L113: To audit these guardrails in free generation, recent frameworks have adopted dynamic adversarial testing (Red Teaming). HarmBench cite72†Mazeika et al. (2024) and WildGuard cite75†Han et al. (2024) standardize the evaluation of automated attacks against broad taxonomies of forbidden behaviors. Similarly, BeaverTails cite74†Ji et al. (2023) contributes a massive scale of 330k prompt-response pairs to align models.
L114: However, these benchmarks structurally prioritize the taxonomy of harm (the "What", e.g., fraud, violence, bomb-making) while neglecting the taxonomy of targets (the "Who"). By aggregating all identity-based attacks under monolithic labels like "Hate Speech", they produce scalar safety scores that mask severe disparities between protected and unprotected groups.
L115: Recent works such as CLEAR-Bias cite79†Cantini et al. (2025) attempt to bridge this gap by using jailbreaking to elicit bias across different minority groups. However, CLEAR-Bias relies on a limited set of 4,400 samples covering seven distinct groups derived from fixed templates. This rigid structure fails to emulate the diversity of real-world adversarial interactions, often allowing models to recognize the attack pattern rather than the harmful semantic payload.
L116: In contrast, MiJaBench leverages a stochastic adversarial rewriter to generate 44,000 unique adversarial prompts across 16 minority groups, verifying safety robustness against complex jailbreaks at a scale significantly larger than prior intersectional works.
L117: ### 2.3 Multilingual Safety and Cultural Alignment
L118: Parallel research highlights a language barrier in safety alignment, where models exhibit significantly higher robustness in English than in low-resource languages cite80†Deng et al. (2023) . Benchmarks like M-ALERT cite81†Friedrich et al. (2024) demonstrate that translating harmful prompts often bypasses refusal mechanisms, suggesting that safety training is frequently overfitted to English lexical patterns rather than generalized semantic concepts.
L119: Furthermore, studies on cultural alignment indicate that models often fail to recognize toxicity when it is grounded in non-Western contexts or expressed through code-switching cite82†Yong et al. (2023) . Our work extends these findings by quantifying not just the drop in general safety, but the specific decoupling of demographic protections across languages, revealing how alignment for specific groups like Women or LGBTQIA community behaviours when shifting from English to Portuguese.
L120: ## 3 MiJaBench
L121: As illustrated in Figure cite83†2 , each sample of our dataset is composed of 1) hate speech seed to define the harmful intent; 2) contextual scenario to enforce high-variance narrative grounding; and 3) jailbreaking strategy to structure the attack vector. These elements serve as inputs to our Adversarial Rewriter module, which synthesizes them into a cohesive adversarial prompt designed to bypass safety filters and generate targeted hate while preserving the original semantic.
L122: We employ Qwen-3-235B-A22B cite84†Yang et al. (2025) as the unified generative engine across all construction stages due to its optimal balance of high-tier instruction-following capabilities and inference efficiency.
L123: ### 3.1 Hate Speech Seed Data
L124: To ground our adversarial prompts in realistic and structurally diverse linguistic distributions, we utilize two large-scale hate speech corpora as seed data: ToxiGen cite85†Hartvigsen et al. (2022) for English and ToxSyn cite86†Brito et al. (2025) for Portuguese.
L125: These datasets were chosen due to both their granular demographic annotations, covering respectively 13 and 9 distinct minorities, and their reliance on semantic breadth over repetitive slurs or fixed templates, capturing both implicit and explicit nature of hate speech.
L126: Critically, we opt for native sourcing strategy over machine translation due to the high cultural dependency of hate speech, as its harmful meaning can be lost in the translation process (e.g., the racial slur associated with “watermelon” in US English carries no offensive connotation when translated into Portuguese).
L127: Then, we randomly extract exactly 2,000 unique samples per minority group from each corpus, resulting in a balanced aggregation of 44,000 distinct toxic instances ($N_{en}=26,000$, $N_{pt}=18,000$), ensuring that subsequent safety evaluations are not affected by the prevalence of specific demographic categories.
L128: ### 3.2 Contextual Scenario
L129: A critical limitation in synthetic data generation is the tendency of LLMs toward deterministic convergence, where the repeated use of similar prompt structures inevitably leads to homogeneous model outputs cite87†Xu et al. (2025) . To counteract this and enforce high-entropy generation, we established a taxonomy of 21 distinct scenario categories that wraps the hate speech text in distinct narrative backdrops, forcing the target model to process the harmful intent through varied thematic lenses.
L130: These categories span a wild range of scripts, ranging from History to Futuristic Technologies and Natural Phenomena, serving as a distractor to cover hate within a wide number of contexts. Descriptions of all 21 scenarios categories are provided in Appendix cite29†A .
L131: For each category, we handcrafted five examples and utilize them in a few-shot learning generation process cite88†Wang et al. (2020) , balancing stylistic consistency with creative divergence.
L132: This process resulted in 8,400 unique narrative contexts (2 languages $\times$ 21 categories $\times$ 200 samples) that conditions the adversarial rewriter to transcend simple lexical repetition of the hateful text, embedding the harmful intent within scenario-specific linguistic structures that challenges the model to detect toxicity when it is incorporated into valid semantic discourses.
L133: ### 3.3 Jailbreaking Strategies
L134: We argue that the adversarial method must be explicitly controlled, once unstructured attacks obscure if a model’s refusal is due to the harmful intent present on the query or to specific attack pattern. Inspired by established taxonomies cite89†Yi et al. (2024) ; cite90†Sorokoletova et al.
L135: (2025) , we curate a set of four distinct jailbreaking strategies (see Table cite91†1 ) and utilize them as the structural mechanism to evade the security alignment in LLMs, preventing the benchmark from being biased toward a single refusal trigger.
L136: Jailbreaking Strategy  | Description
L137: --- | ---
L138: Persona Assignment  | Compels the model to adopt a specific fictional identity or role-play scenario.
L139: Representation Shifting  | Obfuscates the malicious intent by encoding the input into low-resource languages, structured data formats (e.g., JSON), or stylized text (e.g., Leetspeak).
L140: Chain-of-Thought  | Decomposes the harmful objective into a sequence of logical steps, guiding the model incrementally toward a prohibited output.
L141: Logical Rationalization  | Frames the hate speech as an analytical exercise, exploring the structural logic of the statement while ignoring its ethical implications.
L142: Table 1: Taxonomy of Jailbreaking Prompting Strategies
L143: These strategies are uniformly applied across all languages and minority groups and act as a controlled independent variable in our experimental design, ensuring that any observed variance in jailbreak success rates (e.g., higher vulnerability for a specific minority) is attributable solely to the model’s differential safety alignment, rather than artifacts of a variable prompt structure.
L144: ### 3.4 Adversarial Rewriter
L145: The final assembly of MiJaBench is driven by a stochastic combinatorial pipeline that fuses the hate speech seed, the contextual scenario, and the jailbreaking strategy. We conceptualize this adversarial rewriting process as a conditional generation task, where the Qwen-3-235B model serves as the instruction-following agent. To effectively generate these attacks without triggering the rewriter’s own safety alignment, we employed a prefix injection strategy cite92†Zou et al.
L146: (2023) , forcing the generation to commence with an affirmative sequence (e.g., “Ok, as agreed, here is…”) to effectively suppress the model’s refusal mechanisms, steering the probability distribution toward the desired adversarial output. The complete instruction template utilized for this generation is detailed in Figure cite93†8 (Appendix cite58†E ).
L147: Following the generation phase, a manual audit of random samples revealed a tendence in standard adversarial phrasing to produce ambiguous or open-ended questions (e.g., ‘Is group X bad?”), which allowed target models to evade the safety challenge by pivoting to benign, educational corrections. To mitigate these soft refusals, we implemented strict constraints within the system prompt to enforce pre-suppositional phrasing.
L148: By framing the hate speech as an established premise rather than a query (e.g., ‘Given that group X is inferior…”), we eliminate the semantic space for corrective lecturing and force the target model either to explicitly detect and refuse the harmful constraint or blindly comply with the toxic instruction.
L149: ### 3.5 Dataset Distribution
L150: The complete MiJaBench corpus comprises a balanced set of 44,000 adversarial samples (see Table cite94†7 in Appendix cite60†G for illustrative examples). Our generation pipeline enforces strict demographic parity, with exactly 2,000 samples for every active minority group within a language, eliminating class-imbalance artifacts and ensuring that the aggregate safety score is not biased towards specific categories.
L151: As detailed in Table cite95†2 , the English portion ($N_{en}=26,000$) spans 13 distinct groups, heavily weighted toward specific nationalities and ethnicities prevalent in US discourse, while the Portuguese portion ($N_{pt}=18,000$) covers 9 broader categories and introduces groups like Elderly and Immigrants.
L152: Target Demographic  | English  | Portuguese
L153: Race, Ethnicity & Nationality
L154: ---
L155: Black  | ✓  | ✓
L156: Jewish  | ✓  | ✓
L157: Muslim  | ✓  | ✓
L158: Native Peoples (US / BR)  | ✓  | ✓
L159: Middle East  | ✓  | -
L160: Asian  | ✓  | -
L161: Chinese  | ✓  | -
L162: Latino  | ✓  | -
L163: Mexican  | ✓  | -
L164: Immigrants  | -  | ✓
L165: Gender & Sexuality
L166: ---
L167: Women  | ✓  | ✓
L168: LGBTQIA+  | ✓  | ✓
L169: Health & Age
L170: ---
L171: Mental Disability  | ✓  | -
L172: Physical Disability  | ✓  | -
L173: Disability (General)  | -  | ✓
L174: Elderly  | -  | ✓
L175: Samples per Group  | 2,000  | 2,000
L176: Active Groups  | 13  | 9
L177: Total Samples  | 26,000  | 18,000
L178: Table 2: MiJaBench Demographic Coverage. A checkmark (✓) indicates the presence of a group in the dataset.
L179: ## 4 Experiments
L180: ### 4.1 Experimental Setup
L181: 
L182: We evaluate the safety alignment across three families of state-of-the-art open-weights dense instruct models: the Llama-3 series cite96†Grattafiori et al. (2024) , the Gemma-3 series cite97†Team et al. (2025) , and the Qwen-3 series cite84†Yang et al. (2025) . To isolate the impact of model capacity on demographic fairness, we stratify these architectures into four comparable compute classes: Nano (1–2B), Small (3–4B), Standard (8–12B), and Large (27–70B).
L183: This extensive experimental grid anchors the construction of MiJaBench-Align, a comprehensive safety corpus generated by executing the full benchmark across all model configurations. The resulting dataset comprises 528,000 prompt-response pairs, providing a complete adversarial trace for each entry.
L184: Specifically, every sample is indexed with the original hateful seed, the scenario category, the specific contextual scenario, and the jailbreaking strategy, alongside the model’s name and response, and its corresponding safety verdict (annotated via the protocol described in Section cite21†5 ).
L185: All generations were performed using the default model configuration, with a maximum generation length of 2048 tokens. We utilized the official chat templates and default system prompts provided by the developers for each architecture (see Table cite98†6 in Appendix cite57†D for exact model identifiers).
L186: ### 4.2 Scope of Investigation
L187: We structure our investigation around three distinct axes to deconstruct the mechanisms of safety alignment in current LLMs. Primary among our objectives is to determine whether current safeguards function as a generalized semantic capability that protects all communities equally, or if they operate as a selective filter conditioned on the discourse salience of specific groups.
L188: To validate the structural depth of these behaviors, we extend our analysis cross-lingually, aiming to disentangle whether observed demographic hierarchies are superficial artifacts of English or reflect deep-seated semantic biases that persist across linguistic boundaries.
L189: Finally, we interrogate the role of model scaling, specifically testing the hypothesis that increased parameter count may paradoxically function as a bias magnifier, improving average robustness while widening the protection gap between privileged and marginalized demographics, rather than resolving fairness issues.
L190: ### 4.3 Evaluation Metric
L191: 
L192: We measure model robustness using the Defense Rate (DR), calculated as the inverse of the standard Attack Success Rate (ASR) cite72†Mazeika et al. (2024) ; cite92†Zou et al. (2023) . Formally, for a given model $M$ and a set of adversarial prompts $P$, the judge $J$ classifies each response $r_{i}$ into binary outcomes: $1$ (Refused/Safe) or $0$ (Jailbroken/Harmful). The Defense Rate is calculated as:
L193: 
L194:  | $$\text{DR}=\frac{1}{|P|}\sum_{i=1}^{|P|}J(r_{i}=\text{Safe})$$  |
L195: where a higher DR indicates stronger alignment, corresponding to a lower probability of successful jailbreaking.
L196: ## 5 LLM-as-Judge Protocol
L197: Given the intractable scale of our analysis, we implemented an automated LLM-as-a-Judge protocol cite99†Li et al. (2025) . To calibrate this evaluator, we constructed a gold-standard validation set via stratified sampling: utilizing Qwen-3-235B as a preliminary filter, we selected exactly one successful jailbreak and one refusal for every unique combination of language, minority group, attack strategy, and model architecture.
L198: This resulted in 2,112 samples (1,248 English, 864 Portuguese) which were subjected to blind human annotation to establish ground truth. Prior to annotation, all participants were provided with comprehensive guidelines including explicit content warnings regarding the offensive nature of the text, with skip functionality and voluntary discontinuation with non-penalty withdrawal^{1}^{1} 1 The data collection protocol was approved by the Ethics Committee of Federal university of Goiás (Protocol No.
L199: 88442725.6.0000.5083)..
L200: Unlike naive keyword-matching approaches that fail on false refusals (e.g., cases where a model outputs a refusal prefix like "I cannot help" but subsequently fulfills the malicious request), we designed a specific Chain-of-Thought (CoT) system prompt (see Appendix cite59†F ) that forces the evaluator to explicitly reason about intent analysis and actionable content before assigning a verdict.
L201: This structured reasoning step stabilizes the model’s output distribution, ensuring that judgments are based on semantic harm rather than surface-level politeness.
L202: Finally, we benchmarked several open-weights candidates against the human baseline. As detailed in Table cite100†3 , while Qwen-3-235B achieved the highest individual alignment, relying on a single evaluator introduces significant risks of self-preference bias cite101†Zheng et al. (2023) .
L203: To ensure methodological independence, we adopted a Majority Vote ensemble (Qwen-3, Llama-3.3, GPT-OSS), achieving the superior robustness of a consensus-based metric, which dilutes architectural bias and prevents the evaluation from overfitting to a specific vendor’s safety taxonomy.
L204:  | English  | Portuguese  | Overall
L205: --- | --- | --- | ---
L206: Candidate Judge  | Acc (%)  | $\kappa$  | Acc (%)  | $\kappa$  | Acc (%)  | $\kappa$
L207: --- | --- | --- | --- | --- | --- | ---
L208: Llama-3.3-70B  | 90.0  | 0.79  | 88.3  | 0.71  | 89.2  | 0.75
L209: Qwen-3-235B  | 92.0  | 0.83  | 89.0  | 0.71  | 90.5  | 0.77
L210: GPT-OSS-120B  | 89.4  | 0.78  | 84.9  | 0.62  | 87.1  | 0.70
L211: Majority Vote  | 91.3  | 0.81  | 89.6  | 0.73  | 90.5  | 0.77
L212: Table 3: LLM-as-a-Judge Performance. We report Accuracy (Acc) and Cohen’s Kappa ($\kappa$) of candidates against human ground-truth. Best results are in bold.
L213: ## 6 Results
L214: ### 6.1 Demographic Safety Alignment
L215: Across all architectures, we observe a rigid two-tiered safety system rather than a universal baseline.
L216: As illustrated in Figure cite102†3 , alignment appears aggressively optimized for specific demographics, with the largest model variants exhibit positive defense rate deviations of at least $+0.15$ for the Black community above the global mean while categories such as Mental Disability emerge as systemic blind spots, with defense scores consistently degrading to deviations between $-0.09$ and $-0.12$ below the average.
L217: This asymmetry suggests that safety is not a generalized semantic capability, but a memorized behavior allocated disproportionately to specific groups.
L218: This stratification aligns with recent works on the localization of bias, which argues that safety benchmarks often encode specific American cultural markers rather than universal ethical principles cite103†Gamboa et al. (2025) .
L219: We posit that the two-tiered system is a direct artifact of this US-centric data dominance: the model’s decision boundaries are overfitted to high-visibility American advocacy discourse (e.g., racial justice), while failing to generalize to less vocalized or culturally distinct forms of harm.
L220: To confirm that this demographic hierarchy is statistically robust and not merely sampling noise, we applied a bootstrap stability analysis (Appendix cite56†C ), confirming that the observed stratifications are stable, with a worst-case 95% confidence interval of $\pm 0.025$ across all heatmap cells and no observed sign changes under resampling.
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
--------------------------------------------------------------------------------
Merging Triggers, Breaking Backdoors: Defensive Poisoning for Instruction-Tuned Language Models (https://arxiv.org/html/2601.04448v1)
citeturn26843view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04448v1","lineno":null}); Total lines: 337
--------------------------------------------------------------------------------
On the Limitations of Rank-One Model Editing in Answering Multi-hop Questions (https://arxiv.org/html/2601.04600v1)
citeturn26843view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04600v1","lineno":null}); Total lines: 272

