# 2026-01-30 官方分类相关标题有界补检：题摘判据

最终修正：root实际7完整题摘校准，19936 Gap-K仅top1-gap/sliding-window配方无新privacy有效条件EX，不因安全词扩正文；19935 Mem2Act评价盲区与19952双流启动潜在贡献均early Submitted日期隔离。其余确认落窗候选必要命题/反侧已独立核。118具名current notes轻量检查已做；以下原始判据保留，不作最终待办，最终63池见本日README。

只补查观测ID邻域相关标题，非整月或整类队列。当前comment/correction需另作轻量核，不遍历版本史。

## 2601.19936

贡献符合；DATE待定；安全深审：top1-vs-targetpredictiongap配slidinglocalwindow用于membership→需防训练objective低gap与真membership因分布混杂；早date待核。

https://arxiv.org/abs/2601.19936v1
arXiv:2601.19936v1 (cs)
[Submitted on 16 Jan 2026 (this version), latest version 29 May 2026 (v2)]
Title:Gap-K%: Measuring Top-1 Prediction Gap for Detecting Pretraining Data
Authors:Minseo Kwak, Jaehyung Kim
View a PDF of the paper titled Gap-K%: Measuring Top-1 Prediction Gap for Detecting Pretraining Data, by Minseo Kwak and 1 other authors
View PDF
HTML (experimental)
Abstract:The opacity of massive pretraining corpora in Large Language Models (LLMs) raises significant privacy and copyright concerns, making pretraining data detection a critical challenge. Existing state-of-the-art methods typically rely on token likelihoods, yet they often overlook the divergence from the model's top-1 prediction and local correlation between adjacent tokens. In this work, we propose Gap-K%, a novel pretraining data detection method grounded in the optimization dynamics of LLM pretraining. By analyzing the next-token prediction objective, we observe that discrepancies between the model's top-1 prediction and the target token induce strong gradient signals, which are explicitly penalized during training. Motivated by this, Gap-K% leverages the log probability gap between the top-1 predicted token and the target token, incorporating a sliding window strategy to capture local correlations and mitigate token-level fluctuations. Extensive experiments on the WikiMIA and MIMIR benchmarks demonstrate that Gap-K% achieves state-of-the-art performance, consistently outperforming prior baselines across various model sizes and input lengths.
Comments:
under review; 13 pages
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
Cite as:
arXiv:2601.19936 [cs.LG]
(or
arXiv:2601.19936v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.19936
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Minseo Kwak [view email]          [v1]
Fri, 16 Jan 2026 07:29:36 UTC (177 KB)
[v2]
Fri, 29 May 2026 03:58:42 UTC (181 KB)



## 2601.20107

准入 2+2+2=6；设计反证深入：最后层EOSimportance高压缩差不能推出querydependent不可trainingfree→middle-layerstructuralanchors及OSR检验→视觉RAGindex可保语义结构而不是只attention权重。

https://arxiv.org/abs/2601.20107v1
arXiv:2601.20107v1 (cs)
[Submitted on 27 Jan 2026 (this version), latest version 29 Aug 2026 (v3)]
Title:Look in the Middle: Structural Anchor Pruning for Scalable Visual RAG Indexing
Authors:Zhuchenyang Liu, Ziyu Hu, Yao Zhang, Yu Xiao
View a PDF of the paper titled Look in the Middle: Structural Anchor Pruning for Scalable Visual RAG Indexing, by Zhuchenyang Liu and 3 other authors
View PDF
HTML (experimental)
Abstract:Recent Vision-Language Models (e.g., ColPali) enable fine-grained Visual Document Retrieval (VDR) but incur prohibitive index vector size overheads. Training-free pruning solutions (e.g., EOS-attention based methods) can reduce index vector size by approximately 60% without model adaptation, but often underperform random selection in high-compression scenarios (> 80%). Prior research (e.g., Light-ColPali) attributes this to the conclusion that visual token importance is inherently query-dependent, thereby questioning the feasibility of training-free pruning. In this work, we propose Structural Anchor Pruning (SAP), a training-free pruning method that identifies key visual patches from middle layers to achieve high performance compression. We also introduce Oracle Score Retention (OSR) protocol to evaluate how layer-wise information affects compression efficiency. Evaluations on the ViDoRe benchmark demonstrate that SAP reduces index vectors by over 90% while maintaining robust retrieval fidelity, providing a highly scalable solution for Visual RAG. Furthermore, our OSR-based analysis reveals that semantic structural anchor patches persist in the middle layers, unlike traditional pruning solutions that focus on the final layer where structural signals dissipate.
Comments:
18 pages, 6 figures, 11 tables
Subjects:
Computer Vision and Pattern Recognition (cs.CV); Computation and Language (cs.CL); Information Retrieval (cs.IR)
Cite as:
arXiv:2601.20107 [cs.CV]
(or
arXiv:2601.20107v1 [cs.CV] for this version)
https://doi.org/10.48550/arXiv.2601.20107
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Zhuchenyang Liu [view email]          [v1]
Tue, 27 Jan 2026 22:50:11 UTC (5,320 KB)
[v2]
Thu, 21 May 2026 08:54:11 UTC (3,098 KB)
[v3]
Sat, 29 Aug 2026 07:17:06 UTC (3,136 KB)



## 2601.20164

准入 2+2+2=6：对前句末隐状态steering操纵未来rhyme/answer且改变中间token→nexttoken目标可含futureplanning因果证据；小模型1B不等planninguniversal。

https://arxiv.org/abs/2601.20164v1
arXiv:2601.20164v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 11 May 2026 (v2)]
Title:What's the plan? Metrics for implicit planning in LLMs and their application to rhyme generation and question answering
Authors:Jim Maar, Denis Paperno, Callum Stuart McDougall, Neel Nanda
View a PDF of the paper titled What's the plan? Metrics for implicit planning in LLMs and their application to rhyme generation and question answering, by Jim Maar and 3 other authors
View PDF
HTML (experimental)
Abstract:Prior work suggests that language models, while trained on next token prediction, show implicit planning behavior: they may select the next token in preparation to a predicted future token, such as a likely rhyming word, as supported by a prior qualitative study of Claude 3.5 Haiku using a cross-layer transcoder. We propose much simpler techniques for assessing implicit planning in language models. With case studies on rhyme poetry generation and question answering, we demonstrate that our methodology easily scales to many models. Across models, we find that the generated rhyme (e.g. "-ight") or answer to a question ("whale") can be manipulated by steering at the end of the preceding line with a vector, affecting the generation of intermediate tokens leading up to the rhyme or answer word. We show that implicit planning is a universal mechanism, present in smaller models than previously thought, starting from 1B parameters. Our methodology offers a widely applicable direct way to study implicit planning abilities of LLMs. More broadly, understanding planning abilities of language models can inform decisions in AI safety and control.
Comments:
41 pages, 34 figures, Accepted at ICLR 2026, Code available at this https URL
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
Cite as:
arXiv:2601.20164 [cs.LG]
(or
arXiv:2601.20164v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20164
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Jim Maar [view email]          [v1]
Wed, 28 Jan 2026 01:47:10 UTC (14,037 KB)
[v2]
Mon, 11 May 2026 15:11:07 UTC (14,038 KB)



## 2601.20283

准入 2+2+2=6；安全深入：queryaligned一词可升ranking且midrank Goldilocksvulnerable→docperturbbudget/initialrank影响RAGretrieval安全，不仅长promptinjection。

https://arxiv.org/abs/2601.20283v1
arXiv:2601.20283v1 (cs)
[Submitted on 28 Jan 2026]
Title:One Word is Enough: Minimal Adversarial Perturbations for Neural Text Ranking
Authors:Tanmay Karmakar, Sourav Saha, Debapriyo Majumdar, Surjyanee Halder
View a PDF of the paper titled One Word is Enough: Minimal Adversarial Perturbations for Neural Text Ranking, by Tanmay Karmakar and 3 other authors
View PDF
HTML (experimental)
Abstract:Neural ranking models (NRMs) achieve strong retrieval effectiveness, yet prior work has shown they are vulnerable to adversarial perturbations. We revisit this robustness question with a minimal, query-aware attack that promotes a target document by inserting or substituting a single, semantically aligned word - the query center. We study heuristic and gradient-guided variants, including a white-box method that identifies influential insertion points. On TREC-DL 2019/2020 with BERT and monoT5 re-rankers, our single-word attacks achieve up to 91% success while modifying fewer than two tokens per document on average, achieving competitive rank and score boosts with far fewer edits under a comparable white-box setup to ensure fair evaluation against PRADA. We also introduce new diagnostic metrics to analyze attack sensitivity beyond aggregate success rates. Our analysis reveals a Goldilocks zone in which mid-ranked documents are most vulnerable. These findings demonstrate practical risks and motivate future defenses for robust neural ranking.
Comments:
To appear at ECIR 2026
Subjects:
Information Retrieval (cs.IR); Computation and Language (cs.CL); Machine Learning (cs.LG)
Cite as:
arXiv:2601.20283 [cs.IR]
(or
arXiv:2601.20283v1 [cs.IR] for this version)
https://doi.org/10.48550/arXiv.2601.20283
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Sourav Saha [view email]          [v1]
Wed, 28 Jan 2026 05:58:53 UTC (235 KB)



## 2601.20357

准入 2+2+2=6：LVLM单drafter速度跨scenario浮动→verificationpastgroundtruth动态ensembledrafts、共享参数batch →SD配置不能只单模型平均acceptance。

https://arxiv.org/abs/2601.20357v1
arXiv:2601.20357v1 (cs)
[Submitted on 28 Jan 2026]
Title:TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs
Authors:Minjae Lee, Wonjun Kang, Byeongkeun Ahn, Christian Classen, Kevin Galim, Seunghyuk Oh, Minghao Yan, Hyung Il Koo, Kangwook Lee
View a PDF of the paper titled TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs, by Minjae Lee and 8 other authors
View PDF
HTML (experimental)
Abstract:Speculative decoding (SD) has proven effective for accelerating LLM inference by quickly generating draft tokens and verifying them in parallel. However, SD remains largely unexplored for Large Vision-Language Models (LVLMs), which extend LLMs to process both image and text prompts. To address this gap, we benchmark existing inference methods with small draft models on 11 datasets across diverse input scenarios and observe scenario-specific performance fluctuations. Motivated by these findings, we propose Test-time Adaptive Batched Ensemble Drafting (TABED), which dynamically ensembles multiple drafts obtained via batch inference by leveraging deviations from past ground truths available in the SD setting. The dynamic ensemble method achieves an average robust walltime speedup of 1.74x over autoregressive decoding and a 5% improvement over single drafting methods, while remaining training-free and keeping ensembling costs negligible through parameter sharing. With its plug-and-play compatibility, we further enhance TABED by integrating advanced verification and alternative drafting methods. Code and custom-trained models are available at this https URL.
Comments:
Accepted to Findings of EACL 2026
Subjects:
Machine Learning (cs.LG); Computation and Language (cs.CL)
Cite as:
arXiv:2601.20357 [cs.LG]
(or
arXiv:2601.20357v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20357
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Minjae Lee [view email]          [v1]
Wed, 28 Jan 2026 08:16:57 UTC (4,115 KB)



## 2601.20539

贡献关闭：entailmentgraphsearchmemory+policy/worldmodelLLM/criticsroutereflection成熟自进化编排；未新增searchstate正确性/rollout可靠性边界，不能worldmodel标题入Ch25。

https://arxiv.org/abs/2601.20539v1
arXiv:2601.20539v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 25 May 2026 (v3)]
Title:PathWise: Planning through World Model for Automated Heuristic Design via Self-Evolving LLMs
Authors:Oguzhan Gungordu, Siheng Xiong, Faramarz Fekri
View a PDF of the paper titled PathWise: Planning through World Model for Automated Heuristic Design via Self-Evolving LLMs, by Oguzhan Gungordu and 2 other authors
View PDF
HTML (experimental)
Abstract:Large Language Models (LLMs) have enabled automated heuristic design (AHD) for combinatorial optimization problems (COPs), but existing frameworks' reliance on fixed evolutionary rules and static prompt templates often leads to myopic heuristic generation, redundant evaluations, and limited reasoning about how new heuristics should be derived. We propose a novel multi-agent reasoning framework, referred to as Planning through World Model for Automated Heuristic Design via Self-Evolving LLMs (PathWise), which formulates heuristic generation as a sequential decision process over an entailment graph serving as a compact, stateful memory of the search trajectory. This approach allows the system to carry forward past decisions and reuse or avoid derivation information across generations. A policy agent plans evolutionary actions, a world model agent generates heuristic rollouts conditioned on those actions, and critic agents provide routed reflections summarizing lessons from prior steps, shifting LLM-based AHD from trial-and-error evolution toward state-aware planning through reasoning. Experiments across diverse COPs show that PathWise converges faster to better heuristics, generalizes across different LLM backbones, and scales to larger problem sizes.
Subjects:
Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
Cite as:
arXiv:2601.20539 [cs.AI]
(or
arXiv:2601.20539v1 [cs.AI] for this version)
https://doi.org/10.48550/arXiv.2601.20539
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Oguzhan Gungordu [view email]          [v1]
Wed, 28 Jan 2026 12:34:50 UTC (5,130 KB)
[v2]
Thu, 29 Jan 2026 13:55:22 UTC (5,131 KB)
[v3]
Mon, 25 May 2026 16:30:54 UTC (5,132 KB)



## 2601.20861

准入 2+2+2=6；设计反证深入：matchedcompute ES math近GRPO但norm大/denseupdates遗忘→gradientfree低memory不等continuallearning适用，需核normvsalgorithmconfound。

https://arxiv.org/abs/2601.20861v1
arXiv:2601.20861v1 (cs)
[Submitted on 28 Jan 2026]
Title:Evolutionary Strategies lead to Catastrophic Forgetting in LLMs
Authors:Immanuel Abdi, Akshat Gupta, Micah Mok, Alexander Lu, Nicholas Lee, Gopala Anumanchipalli
View a PDF of the paper titled Evolutionary Strategies lead to Catastrophic Forgetting in LLMs, by Immanuel Abdi and 5 other authors
View PDF
HTML (experimental)
Abstract:One of the biggest missing capabilities in current AI systems is the ability to learn continuously after deployment. Implementing such continually learning systems have several challenges, one of which is the large memory requirement of gradient-based algorithms that are used to train state-of-the-art LLMs. Evolutionary Strategies (ES) have recently re-emerged as a gradient-free alternative to traditional learning algorithms and have shown encouraging performance on specific tasks in LLMs. In this paper, we perform a comprehensive analysis of ES and specifically evaluate its forgetting curves when training for an increasing number of update steps. We first find that ES is able to reach performance numbers close to GRPO for math and reasoning tasks with a comparable compute budget. However, and most importantly for continual learning, the performance gains in ES is accompanied by significant forgetting of prior abilities, limiting its applicability for training models online. We also explore the reason behind this behavior and show that the updates made using ES are much less sparse and have orders of magnitude larger $\ell_2$ norm compared to corresponding GRPO updates, explaining the contrasting forgetting curves between the two algorithms. With this study, we aim to highlight the issue of forgetting in gradient-free algorithms like ES and hope to inspire future work to mitigate these issues.
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
Cite as:
arXiv:2601.20861 [cs.LG]
(or
arXiv:2601.20861v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20861
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Akshat Gupta [view email]          [v1]
Wed, 28 Jan 2026 18:59:34 UTC (810 KB)


