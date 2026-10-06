[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Large Language Models are Algorithmically Blind

[3] h6: Abstract

[4] p: Large language models (LLMs) demonstrate remarkable breadth of knowledge, yet their ability to reason about computational processes remains poorly understood. Closing this gap matters for practitioners who rely on LLMs to guide algorithm selection and deployment. We address this limitation using causal discovery as a testbed and evaluate eight frontier LLMs against ground truth derived from large-scale algorithm executions and find systematic, near-total failure. Models produce ranges far wider than true confidence intervals yet still fail to contain the true algorithmic mean in the majority of instances; most perform worse than random guessing and the marginal above-random performance of the best model is most consistent with benchmark memorization rather than principled reasoning. We term this failure algorithmic blindness and argue it reflects a fundamental gap between declarative knowledge about algorithms and calibrated procedural prediction. 1 1 1 Code: https://github.com/sohv/algorithmic-blindness

[5] h2: 1 Introduction

[6] p: Can large language models predict how well an algorithm will perform on a given problem instance? If so, they could serve as zero-shot algorithm selectors or calibrated uncertainty estimators, reducing the need for costly empirical evaluation. Whether such recommendations carry calibrated quantitative validity or whether LLMs merely pattern match on training text that breaks down under numerical scrutiny, has not been systematically evaluated.

[7] p: Answering this requires a domain where algorithmic performance is objectively measurable, algorithms are diverse and well documented and benchmark datasets are sufficiently prominent in training corpora to expose whether above-random performance reflects genuine reasoning or memorization. Causal discovery satisfies all of these requirements. It spans multiple algorithmic paradigms with distinct theoretical assumptions, provides standardized metrics with well-defined ground truth and allows controlled synthetic data generation. This combination makes it a principled testbed for probing structure-conditioned generalization rather than surface-level benchmark recall.

[8] p: We ask whether frontier LLMs can provide calibrated predictions of algorithm performance. We operationalize this via calibrated coverage, defined as the fraction of comparisons where an LLM’s predicted range contains the true algorithmic mean from 100 independent runs. We term the failure we uncover algorithmic blindness : the inability of LLMs to form calibrated probabilistic beliefs about algorithm performance from problem structure alone. The failure mode is not domain specific; causal discovery is the testbed that makes it visible.

[9] p: This paper makes four contributions. First, we establish causal discovery as a rigorous testbed for evaluating LLM algorithmic reasoning, combining diverse algorithmic families, standardized metrics and established benchmarks with sufficient prior literature to expose memorization. Second, we conduct the first large-scale calibration study of this kind, spanning eight frontier models, thirteen datasets, four algorithms, four metrics and three prompt formulations against ground truth from 5,200 algorithm runs. Third, we demonstrate that frontier LLMs achieve only 15.9% calibrated coverage, with seven of eight models falling below a random baseline and simple heuristics outperforming most models tested. Fourth, we show through algorithm-specific performance collapse on held-out synthetic datasets that the marginal above-random performance of the best model is more consistent with retrieval of benchmark-associated statistics than with structure-conditioned generalization.

[10] figure: Figure 1: Comparison of LLM estimates and algorithmic ground truth revealing algorithmic blindness.

[11] h2: 2 Related Work

[12] p: The algorithm selection problem, formalized by Rice (1976) , concerns choosing the best algorithm for a given problem instance based on instance features. Subsequent work developed metalearning approaches that train predictors on algorithm performance histories, enabling informed selection across SAT solvers, combinatorial optimizers and machine learning pipelines. AutoML systems such as Auto-WEKA ( Thornton et al., 2013 ) and Auto-sklearn ( Feurer et al., 2015 ) extend this paradigm with Bayesian optimization over algorithm configurations.

[13] p: A growing body of work probes the reasoning capabilities of LLMs. Studies of mathematical and scientific reasoning have found strong surface-level performance that degrades under distribution shift or problem reformulation, suggesting pattern matching over symbolic reasoning ( Ullman, 2023 ; Mirzadeh et al., 2024 ) . Calibration studies show LLMs are systematically overconfident in factual domains ( Kadavath et al., 2022 ; Xiong et al., 2023 ) . Our work contributes a specific failure mode: algorithmic performance prediction, where LLM confidence does not translate to predictive validity.

[14] p: Recent work has explored LLMs as assistants for scientific tasks including experimental design, hypothesis generation and model selection ( Boiko et al., 2023 ; Kambhampati et al., 2024 ) . LLMs have shown promise in qualitatively ranking algorithmic approaches and suggesting appropriate methods given problem descriptions ( Tornede et al., 2023 ; Jiang et al., 2024 ) and Yang et al. (2023) show LLM guided optimization outperforms random baselines in structured search. Our work provides a quantitative counterpoint: while LLMs may correctly identify that PC is a constraint-based method, they cannot reliably predict how well it will perform on a given dataset.

[15] p: Causal discovery provides structured evaluation criteria (precision, recall, F1 and SHD against a ground-truth DAG), a family of algorithms with well-characterized theoretical properties and a suite of benchmark networks from the bnlearn repository ( Scutari, 2010 ) evaluated across hundreds of papers. Prior work has used these benchmarks to compare algorithmic families Heinze-Deml et al. (2018) ; Vowels et al. (2022) and to assess sensitivity of causal methods to assumption violations ( Kalisch and Bühlman, 2007 ) . We are not testing LLMs on causal discovery per se; we are using causal discovery to test whether LLMs can predict algorithmic performance.

[16] p: Calibration, defined as the alignment between predicted probabilities and empirical frequencies, is central to probabilistic machine learning ( Guo et al., 2017 ) . We apply this concept to interval prediction: a well-calibrated predictor’s stated ranges should contain the true value at the stated rate ( Gneiting and Raftery, 2007 ) . LLMs have been found to be poorly calibrated in classification settings ( Kadavath et al., 2022 ) ; our work extends this to interval prediction in a domain requiring deep algorithmic knowledge.

[17] h2: 3 Methodology

[18] p: Our evaluation pipeline spans five phases (Figure 2 ): (1) ground truth computation via algorithm runs, (2) LLM query collection across models and prompt formulations, (3) aggregation and calibrated coverage comparison, (4) baseline evaluation, (5) prompt robustness and algorithm-specific analysis.

[19] h3: 3.1 Ground Truth Computation

[20] p: For each of 13 datasets combined with 4 algorithms (52 experimental conditions), we run each algorithm 100 times with bootstrap resampling ( Efron and Tibshirani, 1994 ) , computing precision, recall, F1 and Structural Hamming Distance (SHD) per run. This yields 5,200 total algorithm executions. From 100 runs per condition, we compute the empirical mean and 95% confidence interval, which constitute the ground truth for LLM comparison.

[21] h4: Datasets.

[22] p: We use 9 benchmark datasets from the bnlearn repository 2 2 2 https://www.bnlearn.com/bnrepository/ ( Scutari, 2010 ) : Alarm ( Beinlich et al., 1989 ) , Asia ( Lauritzen and Spiegelhalter, 1988 ) , Cancer ( Korb and Nicholson, 2010 ) , Child ( Spiegelhalter et al., 1993 ) , Earthquake ( Korb and Nicholson, 2010 ) , Hepar2 ( Onisko, 2003 ) , Insurance ( Binder et al., 1997 ) , Sachs ( Sachs et al., 2005 ) and Survey ( Scutari et al., 2015 ) , ranging from 8 to 70 nodes. These represent standard evaluation benchmarks in the causal discovery literature with high likelihood of presence in LLM training corpora. We additionally construct 4 synthetic datasets with 12, 30, 50 and 60 nodes, generated from random DAGs with controlled Erdős-Rényi edge density ( Erdős et al., 1960 ) and linear Gaussian data generating processes. Synthetic datasets serve as held-out tests of generalization absent memorizable benchmark statistics.

[23] h4: Algorithms.

[24] p: We evaluate PC ( Spirtes et al., 2000 ) , FCI ( Richardson and Spirtes, 2002 ) , LiNGAM ( Shimizu et al., 2006 ) and NOTEARS ( Zheng et al., 2018 ) using standard implementations from the causal-learn library ( Zheng et al., 2024 ) , all with default hyperparameters. Default settings were retained to reflect typical practitioner usage and to avoid conflating performance prediction with dataset-specific hyperparameter tuning.

[25] h4: Metrics.

[26] p: We evaluate four standard causal discovery metrics ( Acid and de Campos, 2003 ; Tsamardinos et al., 2006 ) . Given a predicted edge set E ^ \hat{E} and true edge set E ∗ E^{*} over a graph with d d nodes, these are defined as:

[27] table: Precision = | E ^ ∩ E ∗ | | E ^ | , Recall = | E ^ ∩ E ∗ | | E ∗ | \text{Precision}=\frac{|\hat{E}\cap E^{*}|}{|\hat{E}|},\qquad\text{Recall}=\frac{|\hat{E}\cap E^{*}|}{|E^{*}|} (1)

[28] table: F1 = 2 ⋅ Precision ⋅ Recall Precision + Recall \text{F1}=\frac{2\cdot\text{Precision}\cdot\text{Recall}}{\text{Precision}+\text{Recall}} (2)

[29] p: Structural Hamming Distance ( Tsamardinos et al., 2006 ) counts the minimum number of edge insertions, deletions and direction reversals required to transform the predicted graph into the true DAG:

[30] table: SHD ​ ( G ^ , G ∗ ) \displaystyle\text{SHD}(\hat{G},G^{*}) = | missing edges | + | extra edges | \displaystyle=|\text{missing edges}|+|\text{extra edges}| (3) + | reversed edges | \displaystyle+|\text{reversed edges}|

[31] figure: Figure 2: Methodology overview. LLMs are prompted with dataset characteristics and algorithmic assumptions to predict performance metric ranges (Precision, Recall, F1, SHD). Ground-truth metrics with bootstrap 95% confidence intervals are computed via large-scale executions and calibration is evaluated using interval coverage.

[32] h3: 3.2 LLM Query Protocol

[33] p: We query 8 frontier LLMs: Claude-Opus-4.6 ( Anthropic, 2026 ) , GPT-5.2 ( OpenAI, 2026 ) , DeepSeek-V3.2-Reasoner ( Liu et al., 2025 ) , DeepSeek-R1-0528 ( Guo et al., 2025 ) , Qwen3-Next-80B-A3B-Thinking ( Yang et al., 2025 ) , Gemini3-Pro-Preview ( Google, 2026 ) , LLaMA-3.3-70B ( Meta, 2026 ) and Qwen2.5-7B ( Yang et al., 2024 ) . 3 3 3 Abbreviated as Claude, GPT-5, DeepSeek-Think, DeepSeek, Qwen-Think, Gemini 3, LLaMA and Qwen respectively throughout all tables and figures. For each of 52 experimental conditions, each model is queried with 3 distinct prompt formulations designed to elicit predicted performance ranges across all four metrics. Formulations vary in specificity: direct question with metric names (f1), expanded description with algorithm intuition (f2) and alternative phrasing emphasizing uncertainty (f3). Multiple prompt formulations follow best practices for robust LLM evaluation ( Mizrahi et al., 2024 ; Sclar et al., 2023 ) , reducing sensitivity to incidental phrasing choices. This yields 8 models × 52 conditions × 3 formulations = 1,248 API calls.

[34] h3: 3.3 Aggregation and Coverage Computation

[35] p: To avoid cherry-picking prompt formulations, we average predicted ranges across the three formulations for each model-condition pair, yielding 52 aggregated predictions per model. Calibrated coverage is then computed as the fraction of (model, dataset, algorithm, metric) quadruples where the aggregated predicted range contains the true algorithmic mean. With 8 models × 13 datasets × 4 algorithms × 4 metrics = 1,664 total comparisons, this yields a single primary metric per model and an overall mean across models.

[36] p: Formally, calibrated coverage is defined as:

[37] table: Coverage ​ ( M , D , A , m ) \displaystyle\text{Coverage}(M,D,A,m) = 𝟏 [ μ ^ D , A , m ∈ \displaystyle=\mathbf{1}\Big[\hat{\mu}_{D,A,m}\in (4) [ l ^ M , D , A , m , u ^ M , D , A , m ] ] \displaystyle\left[\hat{l}_{M,D,A,m},\,\hat{u}_{M,D,A,m}\right]\Big]

[38] p: where μ ^ D , A , m \hat{\mu}_{D,A,m} is the empirical algorithmic mean and [ l ^ , u ^ ] [\hat{l},\hat{u}] is the LLM model M M ’s aggregated predicted range. This metric ( Gneiting and Raftery, 2007 ) directly answers the operational question of whether an LLM’s stated range is informative for a practitioner.

[39] h3: 3.4 Baselines

[40] p: We evaluate two baselines on the same 1,664 comparisons. The random baseline draws predicted ranges uniformly at random within the valid domain for each metric (e.g., [ 0 , 1 ] [0,1] for precision, recall and F1; [ 0 , max_SHD ] [0,\text{max\_SHD}] for SHD). The heuristic baseline constructs ranges using conservative dataset-level statistics from prior literature, with widths scaled to observed algorithm variance. These baselines follow the evaluation practice of establishing uninformed predictors as a reference floor ( Demšar, 2006 ) , ensuring that LLM performance is assessed relative to what can be achieved without any reasoning.

[41] h3: 3.5 Prompt Robustness and Algorithm-Specific Degradation Analysis

[42] p: We compute the coefficient of variation (CV%) across the three prompt formulations per model-metric-experiment to quantify prompt sensitivity ( Liang et al., 2022 ) . We additionally analyze algorithm-specific coverage degradation on synthetic versus benchmark datasets by computing, for each algorithm, the mean coverage boost on synthetic data averaged across all 8 models. If degradation is uniform across algorithms it would indicate a general synthetic-data difficulty effect; dissociation between heavily benchmarked and less-documented algorithms points to training data coverage rather than genuine algorithmic understanding.

[43] h3: 3.6 Memorization Probes

[44] p: We conduct three analyses to probe whether LLM behavior reflects memorization of benchmark statistics. First, we examine the algorithm × \times metric interaction in calibrated coverage to identify structural dissociations attributable to training data exposure. Second, we compare predicted range widths on benchmark versus synthetic datasets: under memorization, LLMs should produce tighter ranges for datasets whose statistics they have retrieved and wider ranges for novel synthetic data. Third, we measure cross-model agreement as mean pairwise distance between predicted ranges across models for the same condition. Under memorization, models should converge on benchmark predictions and diverge on synthetic data. Agreement is computed separately for benchmark and synthetic conditions and broken down by metric and network size.

[45] h2: 4 Results

[46] h3: 4.1 Systematic Calibration Failure

[47] p: Across all 1,664 comparisons, frontier LLMs achieve a mean calibrated coverage of 15.9% , meaning predicted ranges contain the true algorithmic mean fewer than 1 in 6 times. This represents an 84.1% failure rate. Table 1 reports per-model results.

[48] figure: Table 1: Calibrated Coverage by Model Model Coverage (%) Comparisons Mean Score Claude 39.4 82/208 0.442 GPT-5 15.4 32/208 0.217 DeepSeek-Think 14.9 31/208 0.174 DeepSeek 14.4 30/208 0.198 Qwen-Think 13.9 29/208 0.191 Gemini 3 13.0 27/208 0.182 LLaMA 10.1 21/208 0.152 Qwen 5.8 12/208 0.068 Mean 15.9 264/1664 —

[49] p: The 7 × \times spread between Claude (39.4%) and Qwen (5.8%) indicates substantial model-level variance but even the best-performing model achieves coverage far below what would constitute reliable algorithm selection guidance. Failure is not driven by a single algorithm or metric: all four algorithms and all four metrics fall below 21% coverage (Table 2 ) and the 39% relative gap between Recall (18.8%) and Precision (13.5%) suggests LLMs systematically overestimate true positive rates while underestimating false positives, consistent with retrieving optimistic benchmark summaries rather than reasoning about error structure ( Xiong et al., 2023 ) . FCI’s 11.3% coverage, the lowest of any algorithm, reflects a specific difficulty with PAG-structured output and correctness-guarantee reasoning. The algorithm × \times metric interaction reveals a further dissociation that we return to as memorization evidence in Section 4.5 .

[50] figure: Table 2: Calibrated Coverage by Algorithm and Metric Algorithm Coverage Metric Coverage NOTEARS 20.7% Recall 18.8% LiNGAM 20.0% F1 16.3% PC 11.5% SHD 14.9% FCI 11.3% Precision 13.5%

[51] p: Claude’s above-random performance warrants closer examination. Cross-algorithm breakdown reveals that Claude’s synthetic coverage boost is highly algorithm-specific: + 18.8 % +18.8\% for FCI, + 24.3 % +24.3\% for NOTEARS, + 16.0 % +16.0\% for PC but − 16.0 % -16.0\% for LiNGAM (Table 3 ). This 40.3 percentage point range of variation rules out a general synthetic data difficulty effect. The algorithm-specific nature, with LiNGAM uniquely showing degradation on synthetic data, is the hallmark of pattern matching against benchmark statistics rather than principled reasoning about algorithm behavior. Claude also shows the strongest range width compression of all models (0.26 × \times ratio; Table 7 ).

[52] figure: Table 3: Claude’s calibrated coverage by algorithm and dataset type. (Cov. = Coverage%) Algorithm Benchmark Cov. Synthetic Cov. Difference FCI 25.0% 43.8% + 18.8 % +18.8\% NOTEARS 44.4% 68.8% + 24.3 % +24.3\% PC 27.8% 43.8% + 16.0 % +16.0\% LiNGAM 47.2% 31.2% − 16.0 % -16.0\%

[53] p: The pattern tracks training data coverage rather than algorithmic properties: LiNGAM has the most extensive benchmark literature and is the only algorithm where Claude’s synthetic performance collapses, while NOTEARS, which is newer and less documented, shows the largest synthetic boost. This dissociation, where collapse occurs precisely where benchmark literature is richest and stability where it is sparse, makes explanations based on algorithmic properties unlikely and implicates retrieval of memorized statistics.

[54] h3: 4.2 Most LLMs Fail to Exceed Random Guessing

[55] p: Seven of eight LLMs perform below the random baseline of 36.5%. The median LLM achieves 13.9% coverage, less than 40% of random baseline performance. Claude marginally exceeds random by 2.9 percentage points (39.4% vs. 36.5%), a gap not meaningfully distinguishable from chance-level variation and far below practical utility for algorithm selection. The gap between the random baseline and the seven underperforming models is substantial and statistically reliable. 4 4 4 One-sample binomial test against the null rate of 36.5%: all seven models below the random baseline yield p < 0.001 p<0.001 individually (e.g., GPT-5: 32 / 208 32/208 , z = − 8.1 z=-8.1 ; LLaMA: 21 / 208 21/208 , z = − 10.4 z=-10.4 ; Qwen: 12 / 208 12/208 , z = − 12.1 z=-12.1 ). Note that the elevated baseline reflects wide valid metric domains rather than any predictive value of random guessing.

[56] figure: Table 4: Calibrated Coverage: LLMs versus Baselines Method Coverage (%) Mean Score Random Baseline 36.5 0.409 Heuristic Baseline 32.7 0.356 Claude 39.4 0.442 GPT-5 15.4 0.217 DeepSeek-Think 14.9 0.174 DeepSeek 14.4 0.198 Qwen-Think 13.9 0.191 Gemini 3 13.0 0.182 LLaMA 10.1 0.152 Qwen 5.8 0.068

[57] p: This result, shown in Table 4 , establishes that practitioners would obtain better-calibrated uncertainty estimates from uniformly random interval guessing than from querying 7 of the 8 frontier LLMs tested. The heuristic baseline (32.7%) similarly outperforms all models except Claude. These findings confirm that LLMs provide no systematic reasoning advantage for algorithm performance prediction ( Kambhampati, 2024 ) .

[58] h4: Note on range width.

[59] p: LLM predicted ranges are 8 to 27 times wider than true algorithm confidence intervals, yet coverage remains critically low. Wide ranges that still miss the ground truth indicate miscalibrated beliefs, not conservative uncertainty ( Xiong et al., 2023 ) .

[60] h3: 4.3 Prompt Robustness Analysis

[61] p: To verify that results are not artifacts of a particular prompt formulation, we query each model with three distinct formulations per experimental condition and compute the coefficient of variation (CV%) across them. Per-model averages range from 11.5% (Qwen) to 26.0% (Qwen-Think); individual condition maxima exceed 100% for DeepSeek, DeepSeek-Think and Qwen-Think, indicating that some model-condition pairs are highly sensitive to phrasing ( Sclar et al., 2023 ; Mizrahi et al., 2024 ) . A high CV% does not indicate that alternative prompts could rescue performance. Rather, it reflects fundamental instability in models’ algorithmic beliefs. Models that truly understood algorithm performance would provide consistent estimates regardless of minor phrasing variations. Aggregating across all three formulations before computing coverage averages out formulation-specific effects, substantially reducing the likelihood that the primary 15.9% calibrated coverage finding is an artifact of prompt selection. Full per-model CV% data is reported in Appendix B .

[62] h3: 4.4 Benchmark versus Synthetic Degradation

[63] p: Coverage on benchmark datasets exceeds synthetic dataset coverage by 34% (17.7% vs. 11.7%), as shown in Figure 3 . This aggregate pattern holds for 7 of 8 models; Claude is the exception, showing higher synthetic coverage (47%) than benchmark coverage (36%), a reversal addressed in Section 4.1 as evidence of algorithm-specific pattern matching rather than general synthetic difficulty.

[64] figure: Figure 3: Mean calibrated coverage on benchmark datasets versus synthetic datasets across all models.

[65] p: Benchmark datasets are well represented in LLM training corpora through papers, tutorials and documentation ( Golchin and Surdeanu, 2023 ) ; synthetic datasets generated for this study are not. If LLMs were performing principled algorithmic reasoning, synthetic performance should be comparable. The observed degradation suggests partial retrieval of benchmark-associated performance statistics.

[66] p: Coverage on synthetic datasets degrades monotonically with network size: 20.3% at 12 nodes, 13.3% at 30 nodes, 7.0% at 50 nodes and 6.2% at 60 nodes, showing a 69% relative decline across the synthetic scale (Figure 4 ). Larger synthetic networks have fewer analogues in training data and this monotonic collapse further supports memorization over generalization ( Mirzadeh et al., 2024 ) .

[67] figure: Figure 4: Coverage collapse across synthetic network sizes.

[68] h4: Algorithm-specific degradation.

[69] p: The synthetic coverage drop is not uniform across algorithms, which rules out a general synthetic-data difficulty effect. Table 5 reports the average synthetic coverage boost per algorithm across all 8 models.

[70] p: LiNGAM collapses by 23.2% on synthetic data averaged across all models, while NOTEARS shows no degradation ( + 1.7 % +1.7\% ). LiNGAM has the most extensive benchmark literature of the four algorithms; NOTEARS is newer with less documented benchmark performance. This dissociation indicates differential training data exposure rather than principled reasoning. PC and FCI also show modest declines, consistent with partial benchmark memorization.

[71] figure: Table 5: Average Synthetic Coverage Boost by Algorithm (All Models) Algorithm Avg Synthetic Boost Range Variation NOTEARS + 1.7 % +1.7\% 56.9% FCI − 0.5 % -0.5\% 34.7% PC − 2.0 % -2.0\% 24.3% LiNGAM − 23.2 % -23.2\% 44.4%

[72] p: Crucially, if LLMs had internalized a principled model of algorithmic behavior, degradation on synthetic data should reflect genuine algorithmic properties, since LiNGAM’s linear non-Gaussianity assumption is no harder to reason about on synthetic graphs than on benchmarks. Instead, the degradation tracks training data coverage: models perform worse precisely where benchmark statistics are absent, not where the algorithm is intrinsically harder. This suggests that LLM predictions are driven by retrieval of memorized performance figures rather than any underlying understanding of how algorithms behave on new data distributions.

[73] h3: 4.5 Memorization Probes

[74] p: We probe whether above-random benchmark performance reflects memorization of training statistics, using three behavioral signals: an algorithm × \times metric dissociation, range width compression and cross-model agreement collapse. The algorithm × \times metric dissociation is visible in Table 6 , which shows coverage broken down by both algorithm and metric simultaneously.

[75] figure: Table 6: Calibrated Coverage by Algorithm × \times Metric Algorithm Precision Recall F1 SHD PC 8.7% 24.0% 13.5% 0.0% FCI 7.7% 15.4% 20.2% 1.9% LiNGAM 21.2% 21.2% 21.2% 16.3% NOTEARS 16.3% 14.4% 10.6% 41.3%

[76] p: PC and FCI, the two classical and most heavily documented constraint-based algorithms, achieve near-zero SHD coverage (0.0% and 1.9% respectively), whereas NOTEARS achieves 41.3% SHD coverage, more than double its own average across other metrics. LLMs have apparently encountered NOTEARS papers reporting specific SHD values on benchmark datasets and retrieved those figures, whereas constraint-based SHD statistics, which require understanding edge orientation accuracy rather than just edge detection, are either absent or inconsistently represented in training data, consistent with the finding that LLM factual recall scales directly with pretraining document frequency ( Kandpal et al., 2023 ) . Critically, this pattern is not explained by algorithmic difficulty: predicting SHD for PC on the Asia dataset is no harder in principle than predicting it for NOTEARS.

[77] p: Range width compression provides the first model-level signal. Under memorization, LLMs should produce tighter ranges for benchmark datasets whose statistics they have retrieved and wider ranges for novel synthetic data. Benchmark datasets yield a mean predicted range width of 4.34, compared to 9.83 for synthetic datasets, giving a 2.26 × \times compression ratio that holds across all 8 models without exception (Table 7 ). Range width also expands monotonically with synthetic network size from 2.55 at 12 nodes to 18.08 at 60 nodes, a 7.1 × \times increase in a regime where memorization is impossible.

[78] figure: Table 7: Predicted Range Width by Model Model Benchmark Width Synthetic Width Ratio Claude 6.12 23.77 0.26 GPT-5 7.65 19.20 0.40 Qwen 2.02 4.58 0.44 DeepSeek 3.75 8.48 0.44 DeepSeek-Think 5.56 10.34 0.54 LLaMA 2.85 3.78 0.75 Qwen-Think 3.20 4.02 0.80 Gemini 3 3.60 4.46 0.81

[79] p: Figure 5 shows the 2.26 × \times aggregate compression across benchmark and synthetic datasets. Claude shows the strongest compression (0.26 × \times ), which may reflect greater exposure to causal discovery literature during pretraining ( Kandpal et al., 2023 ) . Gemini 3 and Qwen-Think show the weakest compression, indicating their benchmark and synthetic ranges are similarly wide. This suggests they treat both dataset types as equally unfamiliar rather than retrieving statistics for known benchmarks.

[80] figure: Figure 5: Predicted range width: benchmark vs. synthetic. Mean compression ratio 2.26× across all models.

[81] p: Cross-model agreement provides the second signal (Table 8 ). If models are independently retrieving the same benchmark statistics, they should converge on similar predictions regardless of architecture ( Carlini et al., 2022 ) . We find 2.6 × \times greater pairwise disagreement on synthetic datasets than benchmark datasets (mean pairwise distance 33.03 vs. 12.88). Simple well-known benchmarks show the tightest convergence, with Asia and Cancer yielding distances of 2.20 and 1.88, while Synthetic-60 reaches 68.25. The SHD metric is especially revealing: benchmark pairwise distance of 49.99 rises to 130.66 on synthetic data, indicating that models have no principled basis for predicting edge direction accuracy and produce wildly divergent SHD estimates when benchmark figures are unavailable. Agreement collapses 15 × \times across the synthetic scale, which is inconsistent with structured algorithmic reasoning.

[82] figure: Table 8: Cross-Model Agreement by Dataset (Mean Pairwise Distance and Agreement%) Dataset Type Mean Distance Agreement% Asia Benchmark 2.20 44.2 Cancer Benchmark 1.88 34.8 Earthquake Benchmark 2.01 43.5 Survey Benchmark 2.13 43.3 Sachs Benchmark 4.55 47.8 Child Benchmark 8.62 46.2 Alarm Benchmark 17.39 50.7 Insurance Benchmark 17.97 44.9 Hepar2 Benchmark 59.14 42.6 Synthetic-12 Synthetic 4.53 57.8 Synthetic-30 Synthetic 16.77 54.0 Synthetic-50 Synthetic 42.56 52.2 Synthetic-60 Synthetic 68.25 45.1

[83] p: Figure 6 (a) shows the aggregate picture: mean pairwise distance is 12.9 on benchmark datasets and 33.0 on synthetic, a 2.6 × \times gap that holds across all metric types. Figure 6 (b) resolves the synthetic side by network size: distance rises monotonically from 4.5 at 12 nodes to 68.25 at 60 nodes, a 15 × \times increase. This monotonic curve is compelling evidence against principled reasoning: if models were reasoning from algorithm and graph properties, larger graphs would not systematically produce more divergent predictions than smaller ones. Instead, the curve reflects models guessing independently as training-data analogues disappear, producing maximal disagreement at the largest network sizes.

[84] figure: (a) (b) Figure 6: (a) Cross-model pairwise distance on benchmark versus synthetic datasets. (b) Mean cross-model pairwise distance as a function of synthetic network size.

[85] h2: 5 Discussion

[86] p: LLMs should not be used as zero-shot performance predictors for causal discovery algorithm selection. Because practical algorithm selection requires uncertainty-aware expectations rather than qualitative description alone, interval coverage provides an operational test of decision-relevant performance prediction. Claude’s marginal above-random performance (39.4%) is best explained by greater training data coverage in causal discovery literature rather than superior reasoning: the LiNGAM degradation pattern and algorithm-specific synthetic collapse are consistent with memorization, not architectural or reasoning advantages.

[87] p: We define algorithmic blindness as the inability of a model to form calibrated probabilistic beliefs about algorithm performance from problem structure and algorithmic description alone, meaning it fails to predict not just point estimates but even the rough range in which true performance will fall. This is distinct from factual ignorance: LLMs may correctly describe algorithmic assumptions yet fail to translate that declarative knowledge into calibrated procedural predictions. This distinction matters for interventions, since retrieval-augmented generation or knowledge base integration would address factual gaps but not the calibration failure identified here.

[88] h2: 6 Limitations

[89] p: Our evaluation covers four algorithms within causal discovery. Algorithmic blindness may manifest differently in domains with different training data coverage or algorithmic diversity. Although we aggregate across three prompt formulations, we cannot exhaustively explore the prompt space. Chain-of-thought, retrieval-augmented generation or specialized system prompts may yield higher coverage. LLM capabilities evolve rapidly and our results characterize frontier models as of the evaluation date, which may not reflect future versions. Prior work also suggests that structural reasoning failures of this kind persist across prompting strategies ( Mizrahi et al., 2024 ; Sclar et al., 2023 ) supporting the generality of the algorithmic blindness finding beyond the zero-shot setting.

[90] p: We treat four metrics as independent for coverage computation. In practice, precision, recall, F1 and SHD are correlated, which may affect interpretation of aggregate coverage rates. Ground truth is based on empirical means from 100 bootstrap runs. For algorithms with high variance, the empirical mean may be an unstable target on finite samples. Our memorization inference relies on indirect behavioral signals such as range width compression, cross-model agreement collapse and algorithm-specific degradation rather than direct training data attribution, so we cannot rule out alternative explanations for these patterns.

[91] h2: 7 Future Work

[92] p: The LiNGAM degradation result points toward benchmark memorization but direct analysis using training data attribution methods would provide stronger empirical evidence. Testing whether algorithmic blindness extends to SAT solving, graph algorithms or optimization methods would clarify whether this is causal-discovery-specific or a general LLM limitation. Fine-tuning on algorithm performance histories could improve calibrated coverage, distinguishing fundamental limitations from addressable data gaps.

[93] p: Rather than predicting zero-shot ranges, future work could explore LLMs as feature extractors for learned performance predictors, combining language understanding with calibrated statistical models. How human causal discovery experts perform at the same calibrated coverage task remains an open question. If experts also perform near random, the problem may be fundamentally hard; if they substantially exceed random, the gap represents a capability target.

[94] h2: 8 Conclusion

[95] p: Frontier LLMs exhibit systematic algorithmic blindness when predicting causal discovery algorithm performance. The overwhelming majority of LLM predictions fail to contain the true algorithmic mean and most models perform worse than random guessing. The marginal above-random performance of the sole exception is most consistent with benchmark memorization rather than genuine reasoning. LLM predicted ranges are orders of magnitude wider than true confidence intervals yet remain systematically miscalibrated, confirming a fundamental failure of uncertainty-aware algorithmic prediction rather than a conservative but useful response. These results establish a clear negative finding for LLM-assisted algorithm selection in causal discovery and motivate careful empirical evaluation before deploying LLMs as performance predictors in any algorithmic domain.

[96] h2: 9 Acknowledgements

[97] p: We acknowledge OpenAI, Anthropic, Google (Gemini), DeepSeek and Together.ai for access to language model APIs used in this work.

[98] h2: References

[99] h2: Appendix A Causal Discovery Algorithms

[100] p: This appendix describes the four algorithms evaluated, their theoretical grounding and the rationale for their inclusion.

[101] h4: PC Algorithm.

[102] p: The PC algorithm ( Spirtes et al., 2000 ) is a foundational constraint-based causal discovery method. It operates in two phases: a skeleton phase that removes edges between conditionally independent variables using statistical tests, followed by an orientation phase that applies Meek rules to direct edges. PC assumes causal sufficiency (no hidden confounders), acyclicity and the faithfulness condition. It is included as the canonical representative of constraint-based methods and the most widely benchmarked causal discovery algorithm in the literature.

[103] p: The skeleton phase removes edge X i − X j X_{i}-X_{j} if there exists a conditioning set 𝐒 ⊆ 𝐕 ∖ { X i , X j } \mathbf{S}\subseteq\mathbf{V}\setminus\{X_{i},X_{j}\} such that X i ⟂ ⟂ X j | 𝐒 X_{i}\perp\!\!\!\perp X_{j}\mid\mathbf{S} . For continuous Gaussian data this is tested via partial correlation, with significance assessed using Fisher’s z z -transform:

[104] table: z i ​ j | 𝐒 = 1 2 ​ ln ⁡ 1 + ρ ^ i ​ j | 𝐒 1 − ρ ^ i ​ j | 𝐒 ⋅ n − | 𝐒 | − 3 z_{ij\mid\mathbf{S}}=\frac{1}{2}\ln\frac{1+\hat{\rho}_{ij\mid\mathbf{S}}}{1-\hat{\rho}_{ij\mid\mathbf{S}}}\cdot\sqrt{n-|\mathbf{S}|-3} (5)

[105] p: where ρ ^ i ​ j | 𝐒 \hat{\rho}_{ij\mid\mathbf{S}} is the sample partial correlation and n n is the sample size. The edge is removed when | z i ​ j | 𝐒 | |z_{ij\mid\mathbf{S}}| falls below the threshold for the chosen significance level. The orientation phase applies Meek’s four deterministic rules to direct as many skeleton edges as possible without introducing new v-structures or cycles.

[106] h4: FCI Algorithm.

[107] p: The Fast Causal Inference algorithm ( Richardson and Spirtes, 2002 ) extends PC to handle latent confounders and selection bias. Rather than outputting a DAG, FCI produces a Partial Ancestral Graph (PAG) that encodes uncertainty over causal structure in the presence of hidden variables. FCI is included as the constraint-based method that relaxes PC’s causal sufficiency assumption, making it more applicable to real-world settings where unmeasured confounders are plausible. Its output is more conservative (less edge-committing) than PC by design.

[108] p: FCI uses the same conditional independence test as PC for skeleton construction. The key distinction is in the orientation rules: FCI uses a superset of PC’s orientation rules, adding rules that propagate edge marks (tail − - , arrowhead > > or circle ∘ \circ ) through the PAG. An edge X i ∘ − ∘ X j X_{i}\circ\!\!-\!\!\circ X_{j} in the initial skeleton is oriented to X i ∘ → X j X_{i}\circ\!\!\rightarrow X_{j} when X i X_{i} is found to be in the Markov boundary of X j X_{j} but not vice versa under the ancestral graph constraints. The resulting PAG represents an equivalence class of MAGs (Maximal Ancestral Graphs), where each edge mark encodes what is invariant across all causal structures consistent with the conditional independence constraints.

[109] h4: LiNGAM.

[110] p: The Linear Non-Gaussian Acyclic Model ( Shimizu et al., 2006 ) exploits non-Gaussianity of error terms to achieve full identifiability of the causal DAG from observational data alone, a result impossible under the Gaussian assumption. LiNGAM uses Independent Component Analysis to recover the causal ordering and edge weights. It is included as the representative functional causal model and as a contrast to constraint-based methods: its identifiability guarantee and ICA-based mechanism produce qualitatively different performance characteristics across datasets. LiNGAM performs strongly on datasets with genuinely non-Gaussian noise (e.g., Survey) but degrades on datasets that violate its linear assumptions.

[111] p: LiNGAM assumes the data-generating process follows the structural equation model:

[112] table: 𝐱 = 𝐁𝐱 + 𝐞 \mathbf{x}=\mathbf{B}\mathbf{x}+\mathbf{e} (6)

[113] p: where 𝐱 ∈ ℝ d \mathbf{x}\in\mathbb{R}^{d} is the observed variable vector, 𝐁 \mathbf{B} is a strictly lower-triangular weighted adjacency matrix (encoding the DAG) and 𝐞 \mathbf{e} is a vector of mutually independent non-Gaussian noise terms. Rearranging gives

[114] table: 𝐱 = ( 𝐈 − 𝐁 ) − 1 ​ 𝐞 = 𝐀𝐞 , \mathbf{x}=(\mathbf{I}-\mathbf{B})^{-1}\mathbf{e}=\mathbf{A}\mathbf{e}, (7)

[115] p: which is an ICA model. The algorithm recovers 𝐀 \mathbf{A} via ICA, then finds the permutation matrix 𝐏 \mathbf{P} such that 𝐏𝐀 − 1 \mathbf{P}\mathbf{A}^{-1} is strictly lower-triangular, yielding the causal ordering and edge weights.

[116] h4: NOTEARS.

[117] p: NOTEARS ( Zheng et al., 2018 ) reformulates the combinatorial problem of DAG structure learning as a continuous optimization problem using a smooth acyclicity constraint.

[118] table: h ⁡ ( 𝐖 ) = tr ​ ( e 𝐖 ∘ 𝐖 ) − d = 0 h(\mathbf{W})=\text{tr}\!\left(e^{\mathbf{W}\circ\mathbf{W}}\right)-d=0 (8)

[119] p: This allows gradient-based optimization over the space of weighted adjacency matrices. NOTEARS is included as the representative continuous optimization approach, which differs fundamentally in algorithmic mechanism from both constraint-based and functional methods. Its performance is strongest on synthetic data generated from linear Gaussian models (which match its optimization objective) and weaker on benchmark networks with complex nonlinear structure.

[120] p: The full optimization problem is:

[121] table: min 𝐖 ∈ ℝ d × d ⁡ 1 2 ​ n ​ ‖ 𝐗 − 𝐗𝐖 T ‖ F 2 subject to h ⁡ ( 𝐖 ) = tr ​ ( e 𝐖 ∘ 𝐖 ) − d = 0 \min_{\mathbf{W}\in\mathbb{R}^{d\times d}}\frac{1}{2n}\left\|\mathbf{X}-\mathbf{X}\mathbf{W}^{T}\right\|_{F}^{2}\quad\text{subject to}\quad h(\mathbf{W})=\text{tr}\!\left(e^{\mathbf{W}\circ\mathbf{W}}\right)-d=0 (9)

[122] p: where 𝐗 ∈ ℝ n × d \mathbf{X}\in\mathbb{R}^{n\times d} is the data matrix, 𝐖 \mathbf{W} is the weighted adjacency matrix of the learned DAG, ∘ \circ denotes the elementwise product and h ⁡ ( 𝐖 ) = 0 h(\mathbf{W})=0 is satisfied if and only if 𝐖 \mathbf{W} is acyclic. The constraint is solved via an augmented Lagrangian method, converting the constrained problem into a sequence of unconstrained subproblems amenable to standard gradient-based optimizers.

[123] h4: Rationale for Algorithm Selection.

[124] p: The four algorithms span the three major algorithmic families in causal discovery: constraint-based methods (PC, FCI), functional causal models (LiNGAM) and continuous optimization (NOTEARS). This coverage ensures that results are not specific to one algorithmic paradigm. The algorithms also differ in their theoretical assumptions (causal sufficiency, linearity, Gaussianity), output type (DAG vs. PAG vs. weighted matrix) and sensitivity to dataset characteristics, making algorithm performance prediction a genuinely nontrivial task that requires understanding the interaction between algorithmic properties and dataset structure.

[125] h2: Appendix B Prompt Formulations and CV% analysis

[126] p: Figure 7 shows the three prompt formulations used across all experimental conditions.

[127] figure: Formulation 1: Direct You are an expert in causal discovery algorithms. Dataset: <dataset_name> Variables: <n_nodes> Samples: <n_samples> Data type: <data_type> Algorithm: <algorithm_name> Estimate performance ranges for all four metrics: Precision: [X.XX, X.XX] Recall: [X.XX, X.XX] F1: [X.XX, X.XX] SHD: [X, X] CRITICAL: Output ONLY these four lines. No reasoning, no explanations, no preamble. Formulation 2: Step-by-Step You are an expert in causal discovery algorithms. Dataset: <dataset_name> Variables: <n_nodes> Samples: <n_samples> Complexity: <complexity> Algorithm: <algorithm_name> Before predicting, reason through: Core assumptions of the algorithm? Does the dataset satisfy these assumptions? How does complexity affect reliability? What range is realistic? CRITICAL: After reasoning, output ONLY: Precision: [X.XX, X.XX] Recall: [X.XX, X.XX] F1: [X.XX, X.XX] SHD: [X, X] Formulation 3: Meta-Knowledge You are a statistician evaluating causal discovery algorithms. A researcher repeatedly runs <algorithm_name> on <dataset_name> with different random seeds. Dataset characteristics: Variables: <n_nodes> Samples: <n_samples> Data type: <data_type> What ranges capture 95% of typical outcomes? CRITICAL: Output ONLY: Precision: [X.XX, X.XX] Recall: [X.XX, X.XX] F1: [X.XX, X.XX] SHD: [X, X] Figure 7: Three prompt formulations used across all experimental conditions. Formulation 1 elicits direct numerical estimates; Formulation 2 guides explicit step-by-step reasoning about algorithm assumptions; Formulation 3 frames the task as confidence interval estimation over repeated runs. All three require identical output format to enable CV% comparison.

[128] p: We evaluate prompt robustness by querying each model with three distinct formulations per experimental condition and computing the coefficient of variation (CV%) of predicted range midpoints and widths across formulations. The three formulations vary along two dimensions: (1) specificity of metric naming, where f1 uses direct metric names, f2 adds algorithm intuition and context and f3 uses alternative uncertainty-focused phrasing; and (2) framing of the prediction task, ranging from direct numerical elicitation to open-ended range description.

[129] h4: CV% Formula.

[130] p: For a given model-metric-experiment triple, let x 1 , x 2 , x 3 x_{1},x_{2},x_{3} denote the predicted midpoints (or widths) across the three formulations. Then:

[131] table: CV% = σ x ¯ × 100 , x ¯ = 1 3 ​ ∑ i = 1 3 x i , σ = 1 3 ​ ∑ i = 1 3 ( x i − x ¯ ) 2 \text{CV\%}=\frac{\sigma}{\bar{x}}\times 100,\quad\bar{x}=\frac{1}{3}\sum_{i=1}^{3}x_{i},\quad\sigma=\sqrt{\frac{1}{3}\sum_{i=1}^{3}(x_{i}-\bar{x})^{2}} (10)

[132] p: CV% is computed separately for range midpoints and range widths. High CV% indicates predictions are sensitive to prompt phrasing; CV% = 0 indicates identical predictions across all three formulations.

[133] h4: Per-Model CV% by Metric.

[134] p: Average CV% (midpoint) across all dataset-algorithm combinations within each metric. SHD is an integer-valued graph edit distance; F1, Precision and Recall are bounded continuous scores.

[135] figure: Table 9: Prompt Robustness (CV%) by Metric and Model Metric Claude DeepSeek DeepSeek-Think Gemini 3 GPT-5 LLaMA Qwen Qwen-Think F1 17.1% 18.3% 14.0% 13.9% 13.9% 7.5% 5.3% 23.0% Precision 15.4% 19.6% 15.3% 13.9% 11.9% 6.4% 4.1% 22.7% Recall 18.5% 18.8% 14.0% 15.4% 15.8% 8.3% 6.2% 23.2% SHD 19.4% 41.5% 36.4% 23.0% 26.5% 37.1% 30.4% 35.1% Overall 17.6% 24.6% 19.9% 16.5% 17.0% 14.8% 11.5% 26.0%

[136] h4: Interpretation of CV% Patterns.

[137] p: Midpoint CV% ranges from 2.7% to 151.1% and width CV% from 0.0% to 50.8% across all model-condition pairs. Maxima exceeding 100% occur primarily in conditions where predicted midpoints are near zero (e.g., precision or recall on large synthetic graphs), where small absolute differences produce large relative variation; these cases should be interpreted with this scale-dependence in mind. Notably, the models with the highest average CV%, DeepSeek variants and Qwen-Think, are those explicitly designed for reasoning or multi-step thinking. This pattern suggests that reasoning-focused architectures may be more susceptible to prompt sensitivity, perhaps because their extended inference pathways amplify minor differences in initial phrasing. Conversely, the smallest model (Qwen) shows the lowest CV%, indicating more consistent (though not more accurate) predictions.

[138] h4: Implications for Main Results.

[139] p: Per-model averages of 11 to 26% reflect genuine phrasing sensitivity across the full range of conditions. However, high sensitivity does not imply that a different prompt set would yield systematically higher coverage. Examination of individual formulation performance reveals that no single formulation consistently outperforms others across models or conditions; sensitivity manifests as instability rather than latent capability being unlocked by specific phrasing ( Mizrahi et al., 2024 ; Sclar et al., 2023 ) . Aggregating across all three formulations before computing calibrated coverage, using the mean of f1, f2, f3 lower and upper bounds respectively, ensures the primary findings reflect consistent behavior across varied elicitation strategies rather than any single prompt’s characteristics. The 15.9% coverage result is therefore robust to prompt variation and the observed sensitivity itself reinforces the conclusion that LLMs lack stable, calibrated beliefs about algorithm performance.

[140] h2: Appendix C LiNGAM Synthetic Failure Analysis

[141] p: A per-model breakdown of LiNGAM calibrated coverage on synthetic data reveals a near-total collapse across all models.

[142] figure: Table 10: LiNGAM synthetic coverage breakdown. (a) Per-Model LiNGAM Calibrated Coverage on Synthetic Data Model 12 30 50 60 Claude 25.0% 25.0% 50.0% 25.0% DeepSeek 0% 0% 0% 0% DeepSeek-Think 0% 0% 0% 0% GPT-5 0% 0% 0% 0% Qwen-Think 0% 0% 0% 0% Gemini 3 0% 0% 0% 0% LLaMA 0% 0% 0% 0% Qwen 0% 0% 0% 0% (b) Average Synthetic Coverage by Algorithm Algorithm Synthetic NOTEARS 21.9% FCI 10.9% PC 10.2% LiNGAM 3.9% (c) Benchmark vs Synthetic Coverage Alg. Bench Synth Diff LiNGAM 27.1% 3.9% − 23.2 % -23.2\% NOTEARS 20.1% 21.9% + 1.8 % +1.8\% PC 12.2% 10.2% − 2.0 % -2.0\% FCI 11.5% 10.9% − 0.6 % -0.6\%

[143] p: Seven of eight models score 0% on LiNGAM synthetic data across all network sizes, as shown in Table 10 (a). Claude is the sole exception, achieving partial coverage on recall and F1 while failing entirely on precision and SHD; this is addressed in Section 4.1 as algorithm-specific pattern matching rather than genuine understanding.

[144] p: Table 10 (b) ranks all four algorithms by average synthetic coverage. LiNGAM ranks last, performing 5.6 times worse than NOTEARS despite being evaluated on the same datasets and models. This gap cannot be attributed to dataset difficulty since all algorithms face identical conditions.

[145] p: Table 10 (c) shows the benchmark vs synthetic flip across all four algorithms. LiNGAM holds the highest benchmark coverage of any algorithm (27.1%) yet the lowest synthetic coverage (3.9%), a 23.2 percentage point inversion that is the largest dataset type gap across all algorithm model combinations. Every other algorithm shows near-stable or modest decline. This pattern does not support a principled understanding of LiNGAM’s linear non-Gaussianity assumption, which applies equally to synthetic and benchmark graphs. The inversion instead suggests that LLMs may be retrieving memorized statistics and fail completely when that scaffold is removed. The 7 × \times drop from benchmark to synthetic quantifies the scale of LLMs’ dependence on training data exposure rather than algorithmic understanding.

[146] h2: Appendix D Algorithm versus LLM comparison

[147] p: This appendix illustrates the comparison structure with two representative datasets: Asia (benchmark, 8 nodes, highest coverage at 23.4%) and Synthetic-12 (synthetic, 12 nodes, highest synthetic coverage at 20.3%). Each table shows the algorithmic ground truth mean, the mean LLM predicted range averaged across all 8 models and the percentage of models whose range contained the true mean. Algo Mean is the empirical mean over 100 algorithm runs. LLM Range is the mean predicted interval averaged across all 8 models’ aggregated predictions. Coverage is the percentage of the 8 models whose predicted range contained the true algorithmic mean (multiples of 12.5%).

[148] figure: Table 11: Calibrated Coverage by Algorithm and Metric for Asia and Synthetic-12 datasets Asia (Benchmark, 8 nodes) Synthetic-12 (Synthetic, 12 nodes) Algorithm Metric Algo Mean LLM Range Coverage Algorithm Metric Algo Mean LLM Range Coverage PC Precision 0.474 [0.703, 0.874] 12.5% PC Precision 0.470 [0.688, 0.860] 12.5% PC Recall 0.777 [0.626, 0.811] 87.5% PC Recall 0.723 [0.613, 0.797] 75.0% PC F1 0.588 [0.664, 0.831] 0.0% PC F1 0.569 [0.650, 0.815] 0.0% PC SHD 15.0 [2.1, 6.2] 0.0% PC SHD 32.8 [4.9, 13.6] 0.0% FCI Precision 0.474 [0.666, 0.853] 12.5% FCI Precision 0.472 [0.616, 0.805] 12.5% FCI Recall 0.777 [0.588, 0.788] 62.5% FCI Recall 0.722 [0.549, 0.753] 75.0% FCI F1 0.588 [0.625, 0.807] 12.5% FCI F1 0.571 [0.577, 0.765] 12.5% FCI SHD 15.0 [2.9, 7.8] 0.0% FCI SHD 32.6 [8.5, 20.4] 0.0% LiNGAM Precision 0.264 [0.299, 0.488] 25.0% LiNGAM Precision 0.256 [0.750, 0.905] 0.0% LiNGAM Recall 0.362 [0.265, 0.461] 37.5% LiNGAM Recall 0.455 [0.702, 0.878] 12.5% LiNGAM F1 0.305 [0.281, 0.459] 37.5% LiNGAM F1 0.326 [0.726, 0.883] 0.0% LiNGAM SHD 13.3 [7.2, 13.4] 50.0% LiNGAM SHD 33.2 [4.0, 12.9] 0.0% NOTEARS Precision 0.246 [0.567, 0.773] 0.0% NOTEARS Precision 0.953 [0.746, 0.908] 25.0% NOTEARS Recall 0.250 [0.510, 0.729] 25.0% NOTEARS Recall 0.456 [0.696, 0.868] 12.5% NOTEARS F1 0.248 [0.540, 0.732] 0.0% NOTEARS F1 0.615 [0.724, 0.880] 12.5% NOTEARS SHD 12.1 [3.9, 9.5] 12.5% NOTEARS SHD 10.2 [4.5, 13.6] 75.0%

[149] p: Comparing the two tables illustrates key patterns from the main results. On Asia, PC Recall achieves 87.5% coverage (the highest single combination in the study) while SHD coverage is 0% for PC and FCI, consistent with the SHD memorization gap in Table 6 . On Synthetic-12, LiNGAM collapses to 0% across precision, F1 and SHD, while NOTEARS SHD reaches 75%, directly reflecting the algorithm × \times metric dissociation discussed in Section 4.5 .

[150] figure: Table 12: Calibrated Coverage by Dataset (Aggregated Across All Algorithms and Metrics) Dataset Type Nodes Coverage (%) Asia Benchmark 8 23.4 Cancer Benchmark 5 21.9 Synthetic-12 Synthetic 12 20.3 Alarm Benchmark 37 18.8 Insurance Benchmark 27 18.8 Survey Benchmark 6 18.0 Child Benchmark 20 17.2 Sachs Benchmark 11 16.4 Earthquake Benchmark 5 14.1 Synthetic-30 Synthetic 30 13.3 Hepar2 Benchmark 70 10.9 Synthetic-50 Synthetic 50 7.0 Synthetic-60 Synthetic 60 6.2

[151] p: Two patterns are visible in Table 12 . First, three of the four synthetic datasets rank among the four lowest positions, aligning with the benchmark/synthetic degradation reported in Section 4.4 . Second, within benchmark datasets, coverage correlates inversely with network size: Asia (8 nodes, 23.4%) and Cancer (5 nodes, 21.9%) are the highest-performing benchmarks, while Hepar2 (70 nodes, 10.9%) is the lowest. Synthetic-12 is the sole exception, achieving 20.3% coverage comparable to small benchmarks, consistent with its network size falling within the range of well-documented benchmark graphs. The monotonic synthetic collapse from 20.3% to 6.2% across 12 to 60 nodes is reported separately in Section 4.4 and Figure 4 .

[152] h2: Appendix E Algorithmic Ground Truth and Statistical Analysis

[153] h4: Algorithm Performance Summary.

[154] p: Table 13 reports the mean F1 score for each algorithm averaged across all 13 datasets from 100 bootstrap runs per condition. These values constitute the ground truth against which LLM predictions are evaluated.

[155] figure: Table 13: Mean F1 Score by Algorithm (100 runs × \times 13 datasets) Algorithm Mean F1 Best Dataset PC 0.427 Asia, Cancer, Earthquake, Child FCI 0.426 Asia, Cancer, Earthquake, Child LiNGAM 0.301 Survey (0.724) NOTEARS 0.299 Synthetic-30 (0.681)

[156] p: PC and FCI achieve nearly identical mean F1 (0.427 vs 0.426), reflecting their shared constraint-based approach and similar performance profiles across benchmark datasets. LiNGAM and NOTEARS perform substantially lower on average, though LiNGAM achieves the highest single-dataset F1 (Survey, 0.724) and NOTEARS performs best on synthetic data, consistent with its continuous optimization formulation being less dependent on benchmark-specific graph properties.

[157] figure: (a) Mean Precision, Recall and F1 by algorithm aggregated across all datasets. FCI and PC achieve the highest recall, while LiNGAM and NOTEARS show lower recall with differing precision profiles reflecting their distinct assumptions. (b) F1 distribution by algorithm. PC and FCI show similar medians ( 0.45) with moderate spread; LiNGAM and NOTEARS have lower medians ( 0.27) and wider interquartile ranges. Figure 8: Algorithm-level performance summaries across all datasets.

[158] figure: Figure 9: Structural Hamming Distance (mean SHD with 95% CIs) by algorithm. NOTEARS has the lowest mean SHD, followed by PC, FCI and LiNGAM, with LiNGAM exhibiting the highest variance.

[159] h4: Pairwise Significance Testing.

[160] p: Table 14 reports Bonferroni-corrected pairwise significance tests between algorithms on mean F1 score across all datasets.

[161] figure: Table 14: Pairwise Algorithm Comparisons (Bonferroni-corrected) Comparison Mean Difference Corrected p-value Cohen’s d Significant FCI vs LiNGAM +0.125 0.013 0.842 Yes LiNGAM vs PC -0.126 0.010 -0.877 Yes FCI vs NOTEARS +0.127 1.000 0.489 No FCI vs PC -0.002 1.000 -0.132 No LiNGAM vs NOTEARS +0.003 1.000 0.009 No NOTEARS vs PC -0.128 1.000 -0.495 No

[162] p: Two of six pairwise comparisons reach significance after correction: FCI vs LiNGAM and LiNGAM vs PC, both with large effect sizes (Cohen’s d > 0.84). The non-significance of FCI vs PC confirms that the two constraint-based methods are statistically indistinguishable in ground truth performance, making their divergent LLM coverage (11.3% vs 11.5%) unsurprising. The non-significance of NOTEARS vs PC despite a 9.2 percentage point coverage gap (20.7% vs 11.5%) further supports the conclusion that LLM coverage differences across algorithms reflect training data exposure rather than true performance differences.

[163] figure: Figure 10: Precision, Recall and F1 by dataset and algorithm. Subplots show per-dataset variation across all four algorithms, highlighting dataset dependence and the role of graph complexity.

[164] figure: Figure 11: F1 score heatmap. NOTEARS dominates synthetic datasets, LiNGAM peaks on Survey and PC/FCI show consistent benchmark performance, supporting the memorization hypothesis.

[165] h2: Instructions for reporting errors

[166] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[167] p: Tip: You can select the relevant text first, to include it in your report.

[168] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[169] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
