# 2601.08846v1 — 必要证据审阅

精确源：https://arxiv.org/html/2601.08846v1；实际阅读：§3–6。

Qwen2.5-32B Instruct API，BGE-small-en-v1.5，固定reason迭代summary的prompt实现，runtime从当前输出抽lemma进cache，topk cosine hints；AIME借MATH500成熟cache。temperature.7, summarizer0,top-p.95，一次end-to-end stochastic run/condition；格式错误题排除后462/29/162，不是固定原始500/30/198完整分母。GPQA k5 38.9 vs baseline37，k15 34.6；Math77.3→80.3，额外steps14%/16%，非end-to-endlatency/tokens。Fix/break prototype由结果分组构造，early predict未说明严格held-out避免label leakage，inference order/cache maturation未controlled。只能采用相似lemma注入可repair亦可harm及预算成本，不采98.8%cosine证明正确性方向或因果attractor。校准后6分(2+2+2)，实际新增retrieval→reasoning的局部repair/harm与steps条件反侧；设计反证深入。拟已有覆盖：AGENT-MEMORY，Ch77 L1199–1218 固定reader/memory-off成对效用及construction/retrieval分账与L175–211受约束检索；待root非作者通过。

## 实际源核心（不作为论文全附件审阅声明）

Root 非作者实际核filter分母、single-run、GPQA k15与steps反例，读Ch77 matched-reader/memory-off正文；6分深入、已有覆盖通过，仅采用相似hint可harm与reader/预算分账。不授日级/日期Gate。


3 
Data and Environment
3.1 
Data
The datasets used for this study are the same datasets used in 
7
. Our first dataset is 
MATH500
, which consists of 500 math problems sourced from renowned high school math competitions. Next is 
AIME2024
, which is a dataset containing 30 math problems from the 2024 American Invitational Mathematics Examinations 
4
. The problems in this dataset are considered highly challenging, as the examination is invitation-only 
4
. The problems used in this dataset are not meant to be solved using basic computational methods and all have a specific integer solution between 000 and 999. Finally, we use 
GPQA Diamond
, which is a 198 question dataset with graduate-level multiple-choice questions sourced from domain experts in the sciences 
5
. The problems used in this dataset are categorized into three scientific categories including Biology, Physics, and Chemistry and provide a broader scope of questions to test our embedding-based approach for augmenting the context window.
3.2 
Environment
To conduct experimental work, the OpenAI API Python client was used to format and issue API calls to query LLMs. Since our evaluated model was from the Qwen LLM family, we generated an API key through Alibaba Cloud in order to access the required models. The 
Transformers
 and 
Datasets
 libraries by HuggingFace were used to fetch the benchmarks, and a local BGE embedder was used to perform cache retrieval. The use of an API-based environment enabled experiments without requiring higher-order computing resources, permitting local testing through Jupyter Notebooks.
4 
Methods
The hypothesis is that lemma retrieval based on question-lemma similarity improves analytical reasoning performance by augmenting the context window with appropriate guidelines for approaching the question. The baseline model is vanilla InftyThink, which implements iterative summarization-based reasoning with a fixed token limit per reasoning iteration. It was implemented via prompts and separate API calls rather than a fine-tuned model. This approach was followed since the main goal of the paper is to achieve an algorithmic improvement rather than to establish a new state-of-the-art benchmark.
Figure 1: 
Lemma Augmented InftyThink
Dataset
n
Vanilla (Baseline)
Cache (k=5)
Cache (k=10)
Cache (k=15)
Best Improvement
MATH500
462
77.3%
80.3%
77.7%
80.3%
3.0%
AIME2024
29
10.3%
13.8%
20.7%
13.8%
10.4%
GPQA
162
37.0%
38.9%
37.0%
34.6%
1.9%
Table 1: 
Vanilla InftyThink Baseline vs. cache-augmented variants at different retrieval sizes.
In our proposed model, we improve on vanilla InftyThink by storing useful strategies (lemmas) inside a cache (a vector database) after mean pooling. The mean pooling is done via the BGE-small embedder. At the end of each reasoning summarization step, the model returns the main strategy (lemma) used in that step along with the reasoning summary. Our method follows the same iterative summarization logic as InftyThink. However, unlike the vanilla version, our method retrieves the top-
k
k
 lemmas with the highest cosine similarity to the mean-pooled question embedding and displays them in the context window as optional hints. The cache is built at run time. Although our implementation is based on prompting, it can be extended to SFT or other fine-tuning approaches. Vanilla InftyThink risks losing details through repeated compression across numerous thinking steps; our approach partially mitigates this by using similarity-based cache retrieval. In this way, retrieved lemmas enter the model’s context and can steer subsequent reasoning toward more relevant strategies.
A specific transfer learning strategy was used for the AIME2024 dataset. Because the dataset contains only 30 questions, it is too small to build a mature, self-referential cache during runtime. Therefore, we applied a non-parametric transfer learning approach by utilizing the mature cache built during the MATH500 evaluation to answer the AIME2024 questions, capitalizing on the high domain overlap between the two datasets.
5 
Experiments and Results
5.1 
Experimental Setup
We selected Qwen-2.5-32B-Instruct as our primary inference engine. This model was chosen to align with the budgetary constraints and performance profiles favored in the original InftyThink literature. For the semantic retrieval component, we employed BAAI/bge-small-en-v1.5. This lightweight embedding model was responsible for vectorizing both the problem statements and the generated reasoning summaries, enabling the calculation of cosine similarity between a problem and the lemmas available within the cache.
The experiment was conducted across three datasets with distinct levels of difficulty and domain homogeneity: MATH500 (competition mathematics), AIME2024 (high-difficulty Olympiad mathematics), and GPQA Diamond (graduate-level multidisciplinary science). Pydantic was used to verify output formatting; questions where the model failed to produce outputs in the required format were excluded from the final analysis to ensure a fair comparison across control and treatment groups. Thus, the final testing sizes were 
n
=
462
n=462
 for MATH500 (92.4% retention), 
n
=
29
n=29
 for AIME2024 (96.7% retention), and 
n
=
162
n=162
 for GPQA Diamond (81.8% retention).
We established a Control Group (Vanilla InftyThink) and compared it against Treatment Groups utilizing cache sizes of 
k
=
5
k=5
, 
10
10
, and 
15
15
. The reasoning generation was set to a temperature of 0.7 to align with the original InftyThink article, while the summarizer used a temperature of 0.0 to ensure concise lemma extraction. We utilized a top-
p
p
 value of 0.95. Due to cost constraints, each question was evaluated with a single stochastic run per condition; each run nonetheless consists of multiple iterative summarization steps, providing within-run structure. We therefore report one stochastic run model performance rather than averages over multiple independent runs.
5.2 
Analysis
The quantitative results found above in Table 
1
 indicate that the impact of semantic caching is highly dependent on the domain of the problem and the volume of retrieved context.
In the MATH500 dataset, the model demonstrated robust and stable improvements. The baseline accuracy of 77.3% (Vanilla InftyThink) was surpassed by cache-augmented configurations. Specifically, both the 
k
=
5
k=5
 and 
k
=
15
k=15
 configurations achieved a peak accuracy of 80.3%, representing a 3.0% absolute improvement. The graph for MATH500 shows a U-shaped performance curve, suggesting that the model is resilient to varying context sizes in this domain, benefitting similarly from focused (
k
=
5
k=5
) and broader (
k
=
15
k=15
) retrieval.
The AIME2024 results showcased the highest volatility but also the most dramatic relative gains. Starting from a low baseline of 10.3%, performance improved slightly with 
k
=
5
k=5
 (13.8%) and spiked with 
k
=
10
k=10
 to 20.7%, effectively doubling the baseline performance. However, performance dropped back to 13.8% at 
k
=
15
k=15
. While the small sample size (
n
=
29
n=29
) implies high variance, the peak at 
k
=
10
k=10
 supports the transfer learning hypothesis, suggesting that reasoning patterns from MATH500 can transfer to harder AIME problems.
The GPQA Diamond dataset revealed limitations of the approach. The baseline accuracy of 37.0% saw a modest improvement to 38.9% with a focused cache (
k
=
5
k=5
). However, unlike the math datasets, increasing the retrieval size beyond 
k
=
5
k=5
 caused degradation. At 
k
=
15
k=15
, accuracy dropped to 34.6%, performing worse than the no-cache baseline. This downward trend indicates that for heterogeneous domains, retrieving more information can introduce noise rather than signal.
Figure 2: 
The Cost Difference Chart
The Cost Difference Chart (Figure 2), which tracks the Average Steps per Question, provides insight into the efficiency of the cache. The cost difference is only statistically significant for the larger datasets (MATH500 and GPQA with 
p
p
-value of 4% and 2% respectively), increasing the number of steps by an average of 0.26 steps (14% increase) for MATH500 and 0.36 steps (16% increase) for GPQA.
6 
Discussion
Our results indicate that analytical reasoning improvement via embedding-similarity-based lemma retrieval exhibits mixed behavior. Across all cache window sizes, the retrieval-based model produces both 
fixes
, where questions answered incorrectly by the base model are answered correctly after lemma retrieval, and 
breaks
, where questions answered correctly by the base model are answered incorrectly after retrieval. The effectiveness of our approach, 
InftyThink with Cross-Chain Memory
, is strongly correlated with the problem domain. For the structured mathematical domains of MATH500 and AIME2024, cache-question similarity shows a positive correlation with performance. In contrast, for the domain-heterogeneous GPQA-Diamond dataset, higher similarity is primarily associated with breaks. We hypothesize that this divergence arises from the relative immaturity of lemma clusters in GPQA-Diamond, whose multi-domain structure of biology, physics, and chemistry limits the formation of coherent, task-specific lemma representations that are broadly applicable.
To understand the mechanics behind these outcomes, we performed a geometric analysis of reasoning trajectories in embedding space. A key observation is that lemma retrieval induces a significant directional shift in the model’s reasoning relative to the base model’s average trajectory. This shift is consistently larger and more pronounced for summary chains, which we attribute to their semantically condensed structure and reduced representational variance. Interestingly, while lemma retrieval substantially alters reasoning trajectories, we observed no statistically significant directional differences across the different cache sizes of 
k
=
5
k=5
, 
10
10
, and 
15
15
. This suggests that the presence of retrieved lemmas, rather than their quantity, is the primary driver of this directional change.
The core of our findings is the existence of 
directional attractors
. We constructed fix and break prototypes by mean-pooling the reasoning and summary chains corresponding to fix and break outcomes. We found that fix trajectories consistently align with the fix prototype, and break trajectories align with the break prototype in their average reasoning direction. The most striking discovery is that these two prototypes are statistically separable despite having an extremely high cosine similarity, approximately 98.8% in both MATH500 and GPQA-Diamond. This indicates that correctness is not encoded in the overt semantic content of the reasoning itself but rather in the subtle 
directional change
 of the reasoning trajectory relative to the no-cache baseline.
Multiple analyses support this geometric interpretation. Semantic manifold analysis reveals substantial overlap between fix and break chains, with purity levels below 58%, confirming that cache effects act as small geometric shifts rather than clear semantic category shifts. Furthermore, our early divergence analyses show that the final outcome can be predicted with high accuracy from the initial tokens. For MATH500, early alignment of summary chains with the fix prototype results in a fix 75.6% of the time, while early alignment with the break prototype yields a break with 82% probability. Alignment energy analysis, which tracks cumulative distances to the prototypes, provides additional quantitative evidence that fix and break trajectories occupy geometrically distinct regions.
This behavior can be synthesized into a five-step reasoning pipeline: (1) reasoning is initialized from the input question; (2) relevant lemmas are retrieved via cache lookup; (3) a lemma-induced bias is injected into the early tokens of the response; (4) the reasoning path diverges toward either a fix or break directional attractor; and (5) the full reasoning trajectory aligns with the corresponding prototype.
Despite these insights, our study has several limitations. The analysis is based on a single LLM and a single embedding model, and the observed geometric phenomena may not generalize to all architectures. We evaluate each question with a single end-to-end run per condition. This run comprises multiple iterative summarization steps, which provides within-run structure, but it does not substitute for repeating the full pipeline under independent randomness. Consequently, our results characterize directional trends across questions, but they do not directly quantify per-question stability under repeated sampling. Apart from the initial refinement of the prompts explicitly specified in the Appendix 
A
, no additional prompt engineering, prompt tuning, or task-specific prompt modifications were applied. Finally, the inference order, which affects cache maturation, was not controlled. These limitations open several avenues for future work. The predictability of break attractors suggests that a "smarter" retrieval mechanism could be developed to filter out lemmas likely to cause breaks. Exploring alternative retrieval criteria beyond cosine similarity could also mitigate context pollution in heterogeneous domains. The finding that the final outcome can be predicted with high accuracy from the initial tokens could also be further explored for cheaper training methods of LLMs in the future.
7 
Conclusion
In this work, we introduced 
InftyThink with Cross-Chain Memory
, a framework that integrates an embedding-based semantic cache into an iterative reasoning process. Our primary contribution is a detailed empirical and geometric characterization of how similarity-based retrieval influences LLM reasoning. We demonstrated that while this approach can improve accuracy on domain-specific benchmarks like MATH500, it can degrade performance on heterogeneous datasets like GPQA-Diamond by introducing distracting information.
Our main finding is that lemma retrieval actively steers the model’s reasoning trajectory in embedding space, leading to consistent and predictable "fix" and "break" attractors. These attractors are geometrically separable and can be identified within the first few generated tokens, even though their high-level semantic content is nearly identical. This suggests that the success of memory-augmented reasoning hinges on controlling these directional biases rather than simply maximizing semantic relevance.
Similarity-based memory is a powerful but domain-sensitive tool with utility determined by the coherence of the knowledge domain. Additionally, the impact of retrieved context can be productively understood as a geometric perturbation in embedding space, a perspective that offers new ways to analyze and control LLM behavior. As next steps, we plan to leverage these findings to develop more sophisticated retrieval systems that can predict and actively avoid break attractors, paving the way for more robust and reliable self-improving reasoners.
