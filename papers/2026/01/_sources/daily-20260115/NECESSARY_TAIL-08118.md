Exact source: https://arxiv.org/html/2601.08118v1
Necessary bounded positions, actual original text below; not full-paper/appendix traversal.

## Text offsets 45172–56300
 6 Experiments & Results 

 
 We evaluate multiple user-proxy LLMs across four diverse conversational datasets, ChatbotArena, ClariQ, OASST1, and QULAC, to quantify human-likeness using both lexical-diversity and LLM-judge realism metrics. Concretely, we report MATTR , Yule’s K K , and HD-D (human-anchored z z -scores), together with three judge-metrics GTEval , PI , and RNR . Our experiments (i) measure how closely different proxy architectures reproduce human user behavior, (ii) assess the reliability and calibration of LLM-as-judge metrics, and (iii) characterize computational cost, latency, and throughput under large-scale runs. 
 
 
 We compare five LLMs as user proxies: GPT-4o Hurst et al. (2024) , GPT-5 OpenAI (2025a) , GPT-OSS-120B OpenAI (2025b) , Claude-4-Sonnet Anthropic (2025) , and Gemini-2.5-Pro Google (2025) . Unless otherwise noted, the assistant is fixed to GPT-4o and the judge to Claude-4-Sonnet for all primary results, enabling apples-to-apples comparisons across proxies. All the evaluations are performed with a single seed, and we report aggregated scores with 95% confidence intervals. Judge scores are calibrated, and we include a human correlation check to validate judge trends. We also analyze fine-grained telemetry to make cost/performance trade-offs explicit. 
 
 
 6.1 Comparing User-Proxy LLMs on Human-Likeness 

 
 Figure  3 compares five user-proxy LLMs across four datasets with a fixed judge (Claude-4-Sonnet) and assistant (GPT-4o). The left three columns of subplots report judge-based realism ( GTEval , PI  Δ ​ w \Delta w , RNR ; higher is better); the right three columns report human-anchored lexical diversity ( MATTR , HD-D , Yule’s K ; best at the human z-score = 0). Dashed red (HH) and green (PP) lines provide calibration controls; error bars denote 95% CIs. 
 
 
 Judge realism is consistent across datasets. 
Across GTEval, PI  Δ ​ w \Delta w , and RNR, Gemini-2.5-Pro and Claude-4-Sonnet are the most human-like on every dataset, with GPT-4o competitive but generally behind, and GPT-OSS-120B and GPT-5 trailing. On ClariQ and QULAC, Claude-4-Sonnet/Gemini-2.5-Pro approach the HH ceiling under RNR, while PI  Δ ​ w \Delta w shows clear positive win margins for these models and negative/near-zero deltas for the rest. The agreement among the three judge metrics indicates a stable ordering not driven by any single rubric. 
 
 
 Figure 4: Judge sensitivity of judge-realism metrics on ChatbotArena with assistant & user-proxy both set to GPT-4o; bars vary the judge model. Error bars are 95% CIs. 
 
 
 Diversity shows strong dataset effects and a realism–diversity tension. 
Lexical diversity diverges from the realism ranking. On ClariQ , most notably Claude-4-Sonnet and GPT-5 exceed the human anchor on MATTR / HD-D and exhibit lower Yule’s K , indicating a more diverse vocabulary than human questioners in this information-seeking regime. In contrast, QULAC exhibits a uniform diversity deficit: all proxies fall below the human baseline on MATTR and HD-D (with positive shifts in Yule’s K ), suggesting more templated clarifications than humans. ChatbotArena and OASST1 sit between these extremes with smaller deviations around the human baseline. Overall, Gemini-2.5-Pro yields the strongest diversity alignment with humans across datasets; Claude-4-Sonnet generally tends to overshoot the human baseline, whereas GPT-4o is better calibrated to stay closer to the human anchor with fewer extremes. GPT-5 and GPT-OSS-120B have generally larger diversity difference compared to human baselines. 
 
 
 Judge realism and diversity are partially decoupled. 
High judge realism does not guarantee human-level diversity. Claude-4-Sonnet and Gemini-2.5-Pro lead on GTEval / PI / RNR but under-shoot diversity on QULAC , indicating judges favor intent/style over surface variety. Conversely, GPT-4o shows more stable diversity with moderate judge-realism gains, underscoring that diversity alone is insufficient to achieve judge indistinguishability. 
 
 
 Uncertainty and robustness. 
Confidence intervals are generally narrow. When overlaps occur (e.g., GTEval on ChatbotArena), rank differences are small and concur with PI / RNR trends. For lexical-diversity panels, confidence intervals occasionally widen, notably for Yule’s K , as length sensitivity inflates variance. Overall, Figure  3 supports three takeaways: (i) Gemini-2.5-Pro and Claude-4-Sonnet are reliably the most human-like by judge criteria; (ii) diversity depends strongly on dataset regime and proxies often lag on clarification-centric tasks like QULAC; and (iii) realism and diversity capture complementary facets of user-proxy quality, motivating the use of both families of metrics. 
 
 
 Figure 5: Judge–human correlation on ChatbotArena: Correlation of Claude-4-Sonnet judge scores & human scores for GTEval and PI, evaluated on Gemini-2.5-Pro user-proxy outputs (N=100 per metric). Solid line: linear fit; dashed: identity. Point size encodes local sample density. All correlations p < < 0.001. 
 
 
 
 6.2 Judge Sensitivity Analysis 

 
 With the assistant and user-proxy fixed to GPT-4o, Figure  4 shows substantial judge sensitivity on realism scores. On GTEval, scores spread widely ( ≈ 0.45 ​ – ​ 0.81 \approx\!0.45\text{--}0.81 ), with GPT-4o as judge yielding the highest value. PI is the most volatile: Gemini-2.5-Pro & Claude-4-Sonnet produce near-zero or negative win deltas, while GPT-5 & GPT-4o are clearly positive, suggesting family/self-preference or rubric alignment effects (auxiliary evaluations in Appendix C ). RNR saturates near the ceiling for GPT-4o & GPT-5 judges ( ≈ 0.96 ​ – ​ 0.98 \approx\!0.96\text{--}0.98 ) and is lower for others ( ≈ 0.79 ​ – ​ 0.82 \approx\!0.79\text{--}0.82 ), indicating judge-dependent sensitivity: PI > > GTEval > > RNR. 
 
 
 These differences imply that conclusions drawn from a single judge can shift both the absolute level and the ordering of models. In practice, we recommend evaluating with multiple judges and applying HH/PP calibration when feasible, or normalizing per-judge before aggregation, to avoid over-interpreting judge-specific biases. Empirically, Claude-4-Sonnet behaves as a conservative yet stable judge, yielding non-saturated, well-separated scores across metrics, which is why we use Claude-4-Sonnet as a judge in the results reported in Figure 3 . 
 
 
 
 6.3 Human-Judge Correlation 

 
 We validate judge reliability by correlating Claude-4-Sonnet judge scores with blinded human expert annotations on ChatbotArena. We stratify 100 episodes per metric (GTEval, PI) by judge score and conversation length, then compute Spearman’s ρ \rho Kokoska and Zwillinger (2000) , Pearson’s r r Kowalski (2018) , and Kendall’s τ \tau Kendall (1938) . As shown in Figure 5 , GTEval shows strong alignment with humans, while PI exhibits a moderate correlation, consistent with the added difficulty of pairwise judgments. Overall, these results indicate that judge scores correlate with human perceptions of user-proxy quality. 
 
 
 
 6.4 Telemetry, Scaling, and Cost 

 
 Figures  6 , 7 , and 8 summarize the practical side of evaluation. Per-episode telemetry (Fig.  6 ) shows that token usage is dominated by the judge, with the user-proxy & assistant contributing a smaller but non-negligible share; datasets differ markedly, OASST1 drives the highest token counts while ClariQ yields the largest end-to-end latency. 
 
 
 Figure 6: Avg per-episode telemetry for GPT-4o as user-proxy & assistant, and judged by Claude-4-Sonnet across 4 datasets on 6 metrics (Fig.  3 ); only non-cached episodes considered. Left: Token usage by role (darker: input, lighter: output). Right: Cumulative latency per episode. 
 
 
 Figure 7: Throughput vs. concurrency for GTEval on ChatbotArena (async backend, cache off); only the judge varies. User-proxy and assistant fixed to GPT-4o. 
 
 
 Figure 8: Cost-quality trade-off for PI : cost per evaluation (USD) vs. PI Δ ​ w \Delta w ( ↑ \uparrow better). Judge = Claude-4-Sonnet; assistant = GPT-4o; temperature = 0; cache off. Markers denote user-proxies; labels denote datasets. Dashed line: Pareto frontier. See Table 4 for model pricing. 
 
 
 Scaling on an async backend (cache off) reveals clear judge-dependent throughput (Fig.  7 ): GPT-4o as judge attains the highest episodes/min and continues to benefit up to high concurrency, Claude-4-Sonnet scales steadily to mid/high throughput, and Gemini-2.5-Pro plateaus earlier. The cost-quality frontier (Fig.  8 ) clarifies trade-offs for PI evaluation: User-proxies Gemini-2.5-Pro and Claude-4-Sonnet offer attractive Pareto points (good PI Δ ​ w \Delta w at moderate cost), and GPT-5 generally incurs higher cost with weaker PI gain. Overall, user-proxy Gemini-2.5-Pro, along with Claude-4-Sonnet as judge, provides a balanced choice for large runs, where one maximizes throughput and another prioritizes peak PI quality. 
 
 
 
 
 7 Conclusion & Future Work 

 
 MirrorBench introduces a principled, systems-oriented framework for evaluating the human-likeness of user-proxy agents, explicitly decoupled from downstream task success. The framework provides a modular six-layer stack with typed interfaces, metadata-aware registries, a compatibility-checking planner, multi-backend execution, caching, and observability; it supports pluggable proxies, datasets, tasks, and metrics, producing variance-aware, reproducible results at scale. Empirically, we report ( GTEval , PI , RNR ) alongside human-anchored lexical diversity ( MATTR , HD-D , Yule’s K ), revealing a realism-diversity tension across domains, and show that absolute scores and model orderings can shift with the choice of judge, underscoring the need for calibration (HH/PP) and multi-judge reporting. Finally, telemetry (tokens, latency) and cost analyses make the practical trade-offs of large-scale evaluation explicit. 
 
 
 Limitations. Our results rely on LLM-as-judge metrics that can exhibit model-family bias; HH/PP controls help, but residual bias and prompt sensitivity remain. Our experiments use a single seed; assistant models are largely fixed; and coverage is limited to four English-centric datasets. Finally, diversity metrics capture surface variation and do not fully reflect discourse phenomena (e.g., repair, initiative). 
 
 
 Future Work. (i) Judges: multi-judge ensembles, stronger calibration/normalization, and significance across runs; (ii) Metrics: discourse and interaction-level realism (turn-taking, self-correction, persistence), robustness to prompt/goal perturbations; (iii) Datasets: broader domains (customer support, safety-critical, adversarial contexts) and multilingual corpora; (iv) Systems: distributed backends and first-class report generation; (v) Reproducibility & openness: a live-updating benchmark for the research community. 
 
 
 We aim for MirrorBench to serve as a practical evaluation harness and standardized benchmark for measuring user-proxy realism. 
 
 
 
 References 

 
 Ahmad et al. (2025) 
 A. Ahmad, S. Hillmann, and S. Möller 
 
 Simulating user diversity in task-oriented dialogue systems 
