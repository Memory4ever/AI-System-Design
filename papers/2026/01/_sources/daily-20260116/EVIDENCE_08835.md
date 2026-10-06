# DeliberationBench exact-v1 necessary evidence

Source: https://arxiv.org/html/2601.08835v1 ; fetched2026-10-03. Date uncertain, no admission/score/adoptionbeforeboundedfirstpublic. v1submittedDec14; DataCiteJan15existsupper; finiteauthor/titlequery foundJan14 Koios page (nonprimary/unknowntimezone), authorspecificquery onlyarxiv, no earlymanuscriptpublishinglog. Does not identifyfirstpublic.

§3.2 best-single is GPT4o choosing fromfive council drafts, not singlemodelresponse or referenceansweroracle. GPT4oalsoevaluationjudge, blind/rubricselectorsGPT4omini; debateGPT4o. Judgealternativeagreement68.4% cannotproveindependence. Table3v1tokens6323 <baseline6400 contradictsallprotocolshighercost; v2B15884/6400~2.48. Fiveinitialdraftbudgetshared; no directstrongsinglemodel, fixedsinglemember/randomselection control. QA270x3seed localwinrate not universalagentfailure; rawwins/statistical denominators incompletelyspecified. No Books adoptedgiven dategap; ifdatedsourcearrives reopenonlysameclaim/owner82 andmatchedcontrols.

## Primary method/evaluation and limitation excerpt

es [ 3 , 1 ] . Research shows selecting the best individual model can outperform complex ensembles if aggregation is flawed. Our findings extend this to multi-LLM deliberation.




 3 Methodology


 3.1 Benchmark Design


 DeliberationBench consists of 270 questions testing factual knowledge, reasoning, and domain-specific expertise. Each question has a manually researched reference answer. The distribution is intentionally skewed toward medium and hard questions (77.4%), where deliberation is theoretically most valuable.





 Category
 Easy
 Med
 Hard
 Total



 Domain
 19
 26
 60
 105

 Factual
 33
 42
 7
 82

 Reasoning
 9
 33
 41
 83

 TOTAL
 61
 101
 108
 270


 Table 1: Distribution of questions in DeliberationBench .



 3.2 Deliberation Protocols


 We evaluate three protocols using a council of five models: GPT-4o-mini , Claude-3.5-Haiku , Gemini-2.0-Flash-001 , Llama-3.1-8B-Instruct , and Mistral-Nemo .


 Protocol v1: Blind Ranking


 Generate five drafts, shuffle to remove model identity, have a deliberation agent (GPT-4o-mini) rank all five, return top-ranked response.



 Protocol v2-A: Rubric-Based Scoring


 Generate five drafts, have deliberation agent score each on multiple criteria, select highest aggregate score.



 Protocol v2-B: Senate Debate


 Generate five drafts, assign each to a specialized “defender” agent, conduct structured debate with opening statements, rebuttals, and closing arguments, have final judge (GPT-4o) select winner.



 Baseline: Best-Single Selection


 Generate five drafts from the same council, have judge (GPT-4o) directly compare all five in a single prompt, select best response. This isolates whether deliberation adds value beyond having a capable judge choose the best option.




 3.3 Evaluation Methodology


 We run each protocol with 3 independent seeds across 270 questions (810 total evaluations). For each question, an LLM judge (GPT-4o) performs pairwise comparison between each protocol’s output and the baseline’s output. Our primary metric is win rate. We use paired t-tests for statistical significance and validate with an alternative judge (Claude-3.5-Haiku).


 Implementation : Temperature 0.7 for draft generation; 0.3 for deliberation and judging.




 4 Results


 4.1 Main Results


 The best-single baseline dramatically outperforms all deliberation protocols. The most sophisticated protocol (v2-B) achieves only 13.8% win rate—a 6.0x performance gap.





 Protocol
 Win Rate
 Std Dev
 Raw Wins



 Best Single
 82.5%
 ±3.3%
  223

 v1 (Blind Rank)
 3.2%
 ±1.8%
  9

 v2-A (Rubric)
 0.6%
 ±1.0%
  2

 v2-B (Debate)
 13.8%
 ±2.6%
  37


 Table 2: Protocol win rates (mean ± \pm std over 3 seeds, N=270). All differences significant ( p < 0.01 p<0.01 ).


 Figure 1: Win rate comparison across protocols over 3 seeds. Error bars: ±1 std dev. Baseline outperforms all deliberation protocols ( p < 0.01 p<0.01 ).



 4.2 Performance by Category and Difficulty


 The baseline’s dominance holds across all categories and difficulty levels. The baseline achieves consistently high win rates across Factual (79.0%), Reasoning (84.3%), and Domain-specific (83.7%) questions, while all deliberation protocols remain below 17%.


 Figure 2: Win rate by question category. Baseline dominates across all categories.


 Contrary to the hypothesis that deliberation helps with difficult problems, the baseline maintains strong performance across all difficulty levels (Easy: 75.0%, Medium: 86.8%, Hard: 82.9%), while v2-B achieves only 19.2% on easy, 9.3% on medium, and 14.9% on hard questions. This suggests deliberation’s failure is fundamental.


 Figure 3: Win rate by difficulty. Deliberation provides no advantage on harder questions.



 4.3 Cost-Quality Analysis


 All deliberation protocols are more expensive while delivering inferior results. The most complex protocol (v2-B) consumes over 2.5x more tokens. The baseline offers 15x better cost-quality ratio.





 Protocol
 Avg Tokens
 Win Rate
 Tokens/1%



 v1 (Blind)
  6,323
 3.2%
  1,976

 v2-A (Rubric)
  8,346
 0.6%
  13,910

 v2-B (Debate)
  15,884
 13.8%
  1,151

 Baseline
  6,400
 82.5%
  78


 Table 3: Cost-quality tradeoffs across protocols.


 Figure 4: Cost-quality frontier. Baseline occupies optimal position; deliberation protocols fall in inferior region.



 4.4 Judge Robustness


 Re-evaluation with Claude-3.5-Haiku shows 68.4% overall agreement with GPT-4o. Agreement was particularly high for baseline wins (78.1%), confirming the baseline’s superior performance is robust and not judge-dependent.


 Figure 5: Agreement between GPT-4o and Claude-3.5-Haiku judges. High agreement on baseline wins confirms robustness.




 5 Discussion


 5.1 Why Does Deliberation Fail?


 We hypothesize several factors contribute to deliberation’s failure:


 Information Loss through Aggregation : Deliberation forces intermediate agents to synthesize multiple outputs, a process that is inherently lossy. The agent may miss nuances, average out strengths of good drafts, or be swayed by rhetorical style over correctness. The baseline allows direct end-to-end comparison, preserving maximum information.


 Protocol Design Flaws : Each protocol introduces failure modes. Blind ranking removes model attribution (a valuable reliability signal). Rubric scoring may be too rigid. Debate may reward persuasiveness over accuracy.


 Insufficient Council Strength : When all initial drafts are mediocre, deliberation cannot create high quality from low-quality inputs.



 5.2 Model Selection Framework







 Use Case



 Recommended Approach






 Cost-Sensitive



 Best-Single Selection (15x better ratio)




 Latency-Sensitive



 Single Strongest Model




 Highest Quality



 Best-Single Selection (6.0x advantage)



 Table 4: Practical model selection framework.



 5.3 Conditional Performance (RQ4)


 We analyzed whether model disagreement provides advantage for deliberation. When models agree (variance < 0.3 <0.3 ), baseline maintains 6.2x advantage. When models maximally disagree (variance > 0.7 >0.7 ), baseline achieves 71.3% while v2-B achieves only 15.1%. Deliberation provides no additional value even when theoretically most beneficial.



 5.4 Limitations


 Our study has limitations: (1) Our council excludes frontier models like GPT-4o or Claude 3 Opus; deliberation may be more effective with stronger models. (2) We tested three common paradigms; results may not generalize to all multi-agent architectures. (3) DeliberationBench focuses on QA tasks; results may not apply to creative writing or complex code generation.




 6 Ethical Considerations


 Computational Waste


 Our results show deliberation protocols consume up to 2.5x more resources for inferior results. Promoting inefficient methods contributes to unnecessary energy consumption. Our work advocates for more computationally frugal approaches.



 Research Transparency


 We document all methods, prompts, and results for reproducibility. By publishing a strong negative result, we aim to save researchers from investing in architectural dead-ends.




 7 Conclusion


 We presented DeliberationBench , a rigorous evaluation of multi-LLM deliberation. Our findings demonstrate that complexity does not guarantee quality:



 1.

 The best-single baseline (82.5% ± \pm 3.3%) outperforms the best deliberation protocol (13.8% ± \pm 2.6%) by 6.0x .

 2.

 Deliberation shows no advantage on hard questions .

 3.

 Deliberation protocols exhibit 15x worse cost-quality ratio .

 4.

 Findings are robust across question types, difficulties, and judges.




 For practitioners: prioritize strong, simple baselines like best-of-N selection before investing in complex multi-agent architectures.





