# 19051 exact-v1 necessary primary cache

Source: https://arxiv.org/html/2601.19051v1
Original web line labels preserved; sorted and deduplicated within this paper, not contiguous full text.

L212: ### IV-A Experimental Design and Configurations
L213: 
L214: Each configuration represents the combination of key settings within the temporal loop of iteration. The tested parameters compose the columns of Table cite89†I , and shorthand experiment names define the rows. The naming convention and purpose of these configurations are discussed below:
L215: 
L216:   * •
L217: Base regime Draw 5 seed prompts to expand with the generation strategies only. This serves to establish the relative utility of a simplest baseline with no hard-negative mining or fuzzing.
L218: 
L219:   * •
L220: Fuzzing variants Three transformation variants are independently tested, Semantic paraphrasing, Syntactic changes to punctuation, capitalization and spacing, and re-formatting to markdown. The fourth variant applies all three transformation to the prompt (All). Note, syntactic changes could be applied by replacement or insertion at a user-defined mutation probability. All experiments used replacement at 5% mutation.
L221: 
L222:   * •
L223: Hard-mining regimes Hard negative mining is controlled by the ratio of seed samples (from the initial seed dataset) to discovered hard-negatives used in subsequent temporal iterations. HM-Max is the most aggressive regime. During each iteration, the seeded data exclusively used hard-negative examples surfaced from the classifier to seed the next HASTE loop. HM-Bal used both seed and hard-negative examples in a three seed to two hard-negative sampling ratio.
L224: Unlike HM-Max, it prevents the generation to fall within a narrow region of adversarial space while still benefiting from mining. HM-Bal+All used the same balanced re-sampling from HM-Bal and applied all fuzzing techniques. Similarly, HM-Bal+Sem uses the same ratio as the previous regimes, but only used semantic fuzzing.
L225: Across all experiments, 500 prompts were generated per run, distributed across four attack classes. For multi-iteration runs, hard-mined examples from each iteration were re-introduced in subsequent rounds of generation to simulate adaptive adversarial evolution.
L226: TABLE I: Parameter Settings for Each HASTE Experiment Configuration
L227: Experiment  | Iter.  | Seed:HM  | Fuzz.
L228: Base  | 10  | 5:0  | OFF
L229: Base+Sem  | 10  | 5:0  | Semantic
L230: Base+Syn  | 5  | 5:0  | Syntactic (@5%)
L231: Base+Form  | 5  | 5:0  | Format
L232: Base+All  | 5  | 5:0  | ALL (@5%)
L233: HM-Max  | 10  | 0:5  | OFF
L234: HM-Max+Sem  | 10  | 0:5  | Semantic
L235: HM-Max+All  | 10  | 0:5  | ALL (@5%)
L236: HM-Bal  | 10  | 3:2  | OFF
L237: HM-Bal+Sem  | 10  | 3:2  | Semantic
L238: HM-Bal+All  | 10  | 3:2  | ALL (@5%)
L239: To address the modular nature of HASTE, we note that the experiment configurations in Table cite89†I implicitly implement module ablations by toggling specific parameters. For example, configurations with fuzzing disabled (Base, HM-Max, HM-Bal) effectively remove the Refinement module, isolating the contribution of the Generation to Evaluation loop. Similarly, the Base configuration ablates the Hard-Mining module, allowing us to measure performance when no temporal feedback is used.
L240: Because each module can be simply turned on or off via these parameters, HASTE naturally supports controlled studies of how removing individual components affects the potency of generated adversarial prompts and the improvement of the detection models.
L241: ##### Metrics
L242: 
L243: We record (i) iteration accuracy, measuring how well the detector generalizes to new prompts before retraining; (ii) temporal accuracy, capturing improvement after retraining on accumulated samples to quantify adversarial strength over time.
L244: 
L245: ### IV-B Pipeline Configuration
L246: 
L247: Our experimental pipeline comprises six key stages: Collection, Generation, Evaluation, Refinement and finally Training and Benchmarking.
L248: ##### Collection
L249: 
L250: The initial seed dataset contained $\sim$4,500 prompts aggregated from internal and public sources. We partitioned these into 3,500 prompts for iterative generation and 1,000 prompts as a hold-out evaluation set. Each prompt was annotated with metadata specifying attack type.
L251: ##### Generation
L252: 
L253: Prompt generation used GPT-4o as the generative backbone. For fuzzing experiments, we integrated three transformation layers:
L254: 
L255:   * •
L256: 
L257: Semantic fuzzing: humarin/chatgpt_ paraphraser_on_T5_base.
L258: 
L259:   * •
L260: 
L261: Syntactic fuzzing: stochastic edits to casing, spacing, punctuation, and stopword positions (5% mutation rate).
L262: 
L263:   * •
L264: 
L265: Format fuzzing: alternate wrappers (YAML, Markdown, plaintext) to simulate structured or obfuscated prompt styles.
L266: ##### Evaluation
L267: 
L268: Each generated prompt was tested against a target model to elicit responses, and then evaluated using a separate LLM-as-a-Judge framework:
L269: 
L270:   * •
L271: 
L272: Target model: GPT-4o.
L273: 
L274:   * •
L275: 
L276: Judge model: usail-hkust/JailJudge-guard, scoring maliciousness (1–10) and providing reasoning.
L277: 
L278: Scores were used both to filter low-potency samples and to identify hard positives/negatives for re-injection in subsequent iterations.
L279: ##### Refinement
L280: 
L281: For this particular experiment, we applied minimal filtering (maliciousness_threshold = 1) to retain the full adversarial spectrum, ensuring that robustness was learned across both mild and severe cases. Fuzzing was optionally applied depending on configuration.
L282: ##### Data Preparation
L283: 
L284: Prompts were automatically labeled with taxonomy metadata using GPT-4o guided by a fixed taxonomy prompt. Data were split 80/20 for train/test, with the collection-stage evaluation set held out for generalization benchmarking.
L285: ##### Training and Benchmarking
L286: 
L287: This final stage uses Deberta V3 for classification of prompts [cite60†21 ], fine-tuned iteratively across experiment loops. After each iteration, hard-mined samples were added to the training pool, and performance was measured using iteration accuracy and temporal accuracy. These metrics collectively capture both immediate resilience and long-term generalization.
L288: Training was performed iteratively, with benchmarking at each iteration across attack types, tasks, and topics. Hard positives and hard negatives mined from benchmarking errors were re-injected into subsequent loops. Performance was reported using iteration accuracy, temporal accuracy metrics.
L289: ## V Results
L290: We evaluate the HASTE process with the experiment parameter configurations documented in Table cite89†I and described in Section cite21†IV . Experiments are evaluated to assess two functional goals: the effectiveness of generating evasive malicious prompts and two, improving the robustness of the defensive classifier retrained with the synthetic malicious prompts.
L291: These goals are measured by (i) iteration accuracy, reflecting the static baseline detection model’s (ProtectAI-Deberta-V3) performance on the synthetically generated prompts, and (ii) HASTE-optimized model accuracy, the detection accuracy of a HASTE optimized version of the static baseline model retrained from the generated samples of a HASTE experiment configuration type. Together, these metrics reveal the dynamic evolution of robustness under opposing red-team blue-team objectives.
L292: ### V-A Impact of Fuzzing
L293: In this work we want to evaluate, characterize and understand the factors that most influence the iterative refinement of prompt behavior. To ensure the impact of hard negative mining is truly from that process and not from strategies used to draw samples from the seed set, or variations in fuzzing, we isolate these impacts before introducing hard negative mining.
L294: The evolution of adversarial prompt behavior is compared with four fuzzing variants: semantic, syntactic, formatting and ’all’, against its non-fuzzed baseline and listed in Table cite89†I . The purpose of this test is to inform if there are significant differences such that it’s necessary to test all variations in all experiment conditions. for the baseline detection model
L295: TABLE II: Iteration accuracy for baseline and fuzzing configurations, as evaluated on the in-loop test data partition. Lower numbers indicate red-team success in producing evasive prompts with malicious response.
L296: Experiment  | It0  | It1  | It2  | It3  | It4  | It5
L297: --- | --- | --- | --- | --- | --- | ---
L298: Base  | 95.91  | 95.68  | 95.54  | 95.62  | 95.73  | 95.61
L299: Base+Sem  | 95.91  | 67.44  | 65.26  | 66.11  | 66.14  | 65.87
L300: Base+Syn  | 95.91  | 73.24  | 71.62  | 71.91  | 71.49  | 71.62
L301: Base+Form  | 95.91  | 70.67  | 70.86  | 71.41  | 70.42  | 71.23
L302: Base+All  | 95.91  | 71.79  | 70.37  | 70.96  | 70.89  | 71.08
L303: 
L304: From Table cite90†II , the following trends are observed.
L305: 
L306:   * •
L307: Of these configurations, Base-Sem, which uses semantic rephrasing, is the most effective at producing evasive malicious prompts decreasing accuracy from 95.91% to 65.26%.
L308: 
L309:   * •
L310: 
L311: The Base configuration produces little to no impact on the maliciousness of generated samples across all iteration steps.
L312: 
L313:   * •
L314: 
L315: Of these configurations, the peak improvement for producing evasive malicious prompts typically occurs in the second iteration.
L316: 
L317:   * •
L318: The Base-All configuration uses all selected fuzzing methods for each prompt. It was observed that the Base+Sem configuration comparatively produced the largest percentage of prompts to successfully evade detection. This suggests, at least superficially, the addition of syntactic and format fuzzing may counteract the evasive effectiveness of semantic fuzzing.
L319: Whilst an interesting observation, investigating the causal interactions of semantic, syntactic and format fuzzing is beyond the scope of this study and identified as a potential area of future investigation. Therefore, on this basis, we omit both Base+Syn and Base+Form configurations from the subsequent experiments based on the ineffectiveness of combining these methods for evasive prompt generation.
L320: To better understand the potential origin of the fuzzed prompt behaviors, we examine token-level attributions using SHAP (Figure cite91†9 )[cite92†34 ]. The top panel (Figure cite93†9a ) shows the attribution distribution for a baseline non-fuzzed prompt, while the bottom panel (Figure cite94†9b ) displays the same prompt after all fuzzing perturbations are applied.
L334: The HM-Max-Sem configuration is the most effective strategy for producing evasive, malicious prompts. The majority benefit of this strategy is achieved in one iteration, dropping classifier accuracy from 95.91% to 37.00%. Iterating this strategy out to the 10th iteration, only yields an additional ~5% drop.
L335: 
L336:   * •
L337: 
L338: The utility of all strategies plateaus almost immediately after the first iteration.
L339: 
L340:   * •
L341: The HM-Bal configuration, draws 3 files from the seed set and 2 hard-negatives from the previous iteration, to initiate the next round of generation. The efficacy of this strategy (81.62%), is proportional to the two composite strategies in isolation 95.68% (Base) and 58.6% (HM-Max).
L342: 
L343:   * •
L344: Across all variants, incorporating any degree of hard-negative sampling consistently outperforms the corresponding base-generation methods. Whether applied aggressively (HM-Max), moderately (HM-Bal), or in combination with paraphrasing and transformation strategies (HM-Bal+Sem, HM-Bal+All), hard-mining reliably produces lower classifier accuracy than the matched Base, Base-Sem, or Base-All configurations.
L345: The performance of these configurations also suggest 10 iterations are not necessary and greater gains would be made from increasing the sampling ratio of hard negative mining or changing acceptance criteria for the LLM as a judge, which was fixed at 2, for these experiments.
L346: TABLE III: Iteration accuracy results (It0–It10) without retraining. As evaluated on the in-loop test data partition.
L347: Experiment  | It0  | It1  | It2  | It3  | It4  | It5  | It6  | It7  | It8  | It9  | It10
L348: --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
L349: Base  | 95.91  | 95.68  | 95.54  | 95.62  | 95.73  | 95.61  | 94.92  | 94.42  | 94.05  | 93.70  | 93.49
L350: HM-Bal  | 95.91  | 81.62  | 82.52  | 83.27  | 83.17  | 83.24  | 83.62  | 83.72  | 83.19  | 83.47  | 83.54
L351: HM-Max  | 95.91  | 58.60  | 58.39  | 58.26  | 57.82  | 56.86  | 56.41  | 56.31  | 56.18  | 55.95  | 55.21
L352: Base-Sem  | 95.91  | 67.44  | 65.26  | 66.11  | 66.14  | 65.87  | 66.30  | 66.08  | 66.38  | 66.11  | 66.16
L353: HM-Bal+Sem  | 95.91  | 57.74  | 57.47  | 57.18  | 56.68  | 56.88  | 57.07  | 57.13  | 57.02  | 57.01  | 57.18
L354: HM-Max+Sem  | 95.91  | 37.00  | 34.93  | 34.04  | 33.91  | 32.91  | 32.50  | 32.18  | 31.96  | 32.01  | 31.76
L355: Base-All  | 95.91  | 71.79  | 70.37  | 70.96  | 70.89  | 71.08  | 71.42  | 71.45  | 71.95  | 71.87  | 71.81
L356: HM-Bal+All  | 95.91  | 71.29  | 69.85  | 70.71  | 70.11  | 70.59  | 70.41  | 70.51  | 70.41  | 70.53  | 70.47
L357: HM-Max+All  | 95.91  | 60.98  | 60.72  | 60.10  | 61.08  | 60.33  | 60.60  | 60.88  | 61.06  | 61.44  | 61.35
L358: ### V-C Hard-negative Potency and HASTE Model Optimization
L359: Table cite98†IV summarizes HASTE-Optimized detection model accuracy, after fine-tuning with the corresponding HASTE parameter configuration, (referred to herein as “H accuracy”. The baseline model (Base) exhibits limited improvement at the M5 stage, but at M10, becomes on par with the gains with hard-negative mining, effectively eliminating the need for half the training cycles and accelerating convergence by 50%.
L360: This suggests naively generating similar samples can ultimately improve H accuracy but takes a minimum of 5x more iterations. In contrast, the H accuracy of the six HASTE configurations show the majority of their improvement by M5, and minimal additional gains in M10. Interestingly, HM-Bal+All shows the highest overall H accuracy, despite having consistently intermediate success in iteration accuracy at each iteration loop.
L361: Given the diminishing returns of iteration accuracy for all the HM sampling methods, it’s likely an M1 or M2 HASTE-optimized model from these respective HASTE configurations would achieve similar accuracy to the equivalent M5 scores.
L362: The comparable final accuracies between semantic-fuzzing (Base+Sem) and the hard-mining (HM) configurations should be contextualized. Although both approaches ultimately achieve roughly the same accuracy of ~93% accuracy (Table cite98†IV ), the quality of the adversarial training signal differs significantly. As shown in Table cite97†III , Base+Sem reduces the baseline detector’s accuracy to only 66.16%, whereas the HM-Max discovers substantially more evasive prompts, driving the accuracy down to 31.76%.
L363: This contrast illustrates that the stand-alone semantic fuzzing probes only a shallow portion of the adversarial space, whereas HASTE’s hard-mining aggressively targets the detector’s most weak vulnerabilities. The fact that the HASTE-trained model’s ability to recover to high accuracy (93.96%) despite being exposed to far more potent (31% accuracy) attacks suggests a more durable robustness than the model trained on surface-level fuzzed variants alone.
L364: Notably, the H accuracy of Base+All is on par with the hard-negative mining configurations, despite having consistently intermediate iteration accuracy across all HASTE Loops. Expanding the experiment configurations to isolate the semantic fuzzing, may be necessary to fully explain the observed gaps in fuzzed iteration accuracies and fuzzed H accuracies.
L365: Overall, these results suggest that controlled exploitation through hard-mining yields the highest HASTE-Optimized accuracy, with at least a 50% reduction of the number of HASTE iteration loops relative to the baseline strategies.
L366: TABLE IV: H accuracy results for the baseline model (M0), re-trained model at iteration 5 (M5) and re-trained model at iteration 10 (M10). Each row represents different configurations of HASTE sample generation strategies, as measured on the out-of-loop evaluation dataset.
L367: Experiment  | M0  | M5  | M10
L368: --- | --- | --- | ---
L369: Base  | 82.12  | 81.06  | 92.80
L370: Base+All  | 82.12  | 92.22  | 93.13
L371: Base+Sem  | 82.12  | 93.94  | 94.14
L372: HM-Bal  | 82.12  | 92.82  | 93.74
L373: HM-Bal+All  | 82.12  | 93.74  | 94.44
L374: HM-Bal+Sem  | 82.12  | 93.94  | 93.84
L375: HM-Max  | 82.12  | 93.62  | 93.96
L376: HM-Max+All  | 82.12  | 92.93  | 93.03
L377: HM-Max+Sem  | 82.12  | 93.23  | 94.24
L378: TABLE V: Accuracy by attack category for each model on the out-of-loop evaluation dataset. Abbrev.: Obf = Obfuscation, Obj Manip = Objective Manipulation.
L379: Model  | Benign  | Obf  | Obj Manip  | Other  | Role Play
L380: --- | --- | --- | --- | --- | ---
L381: ProtectAI deberta  | 70.4  | 92.8  | 95.3  | 94.5  | 97.6
L382: Base  | -6.9  | +5.1  | +2.7  | -1.6  | +0.8

