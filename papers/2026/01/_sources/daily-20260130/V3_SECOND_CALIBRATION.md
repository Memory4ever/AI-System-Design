# 2026-01-30 第二批题摘准入（作者初判）

最终修正：root实际18完整题摘及必要core校准通过。VERGE以MCS deleted-clause局部repair5保留，非formal truth；AMA/OptiKIT/AutoDP/domain-Shapley明确EX，AutoDP no-human raw-access不认证privacy。19918/19956/19923潜在贡献但DATE终态隔离。以下初判/题摘保存，最终63家族与证据/Books以本日README为准，不按待审成本缩池。

仅首次直接原始v1完整题摘；未深审。Created仅公开上界；较早Submitted项未能封闭firstday，先保留日期请求，不列为确定当窗候选。

## 2601.19918

贡献符合但首公开待定：单次输出logprob下，以最低语义span联合likelihood替代全序列均值/单token极小值，若成立改变API场景检测预算选择。2+1+2=5；v1Submitted01/07，Created01/29仅上界，不能确定firstday。

https://arxiv.org/abs/2601.19918v1
arXiv:2601.19918v1 (cs)
[Submitted on 7 Jan 2026 (this version), latest version 30 Sep 2026 (v2)]
Title:Lowest Span Confidence: A Zero-Shot Metric for Efficient and Black-Box Hallucination Detection in LLMs
Authors:Yitong Qiao, Licheng Pan, Yu Mi, Lei Liu, Yue Shen, Fei Sun, Zhixuan Chu
View a PDF of the paper titled Lowest Span Confidence: A Zero-Shot Metric for Efficient and Black-Box Hallucination Detection in LLMs, by Yitong Qiao and 6 other authors
View PDF
HTML (experimental)
Abstract:Hallucinations in Large Language Models (LLMs), i.e., the tendency to generate plausible but non-factual content, pose a significant challenge for their reliable deployment in high-stakes environments. However, existing hallucination detection methods generally operate under unrealistic assumptions, i.e., either requiring expensive intensive sampling strategies for consistency checks or white-box LLM states, which are unavailable or inefficient in common API-based scenarios. To this end, we propose a novel efficient zero-shot metric called Lowest Span Confidence (LSC) for hallucination detection under minimal resource assumptions, only requiring a single forward with output probabilities. Concretely, LSC evaluates the joint likelihood of semantically coherent spans via a sliding window mechanism. By identifying regions of lowest marginal confidence across variable-length n-grams, LSC could well capture local uncertainty patterns strongly correlated with factual inconsistency. Importantly, LSC can mitigate the dilution effect of perplexity and the noise sensitivity of minimum token probability, offering a more robust estimate of factual uncertainty. Extensive experiments across multiple state-of-the-art (SOTA) LLMs and diverse benchmarks show that LSC consistently outperforms existing zero-shot baselines, delivering strong detection performance even under resource-constrained conditions.
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2601.19918 [cs.CL]
(or
arXiv:2601.19918v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.19918
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yitong Qiao [view email]          [v1]
Wed, 7 Jan 2026 12:48:33 UTC (888 KB)
[v2]
Wed, 30 Sep 2026 12:23:20 UTC (104 KB)



## 2601.20352

初拟贡献关闭：constructor/retriever/judge/refresher与层次粒度组织、冲突触发更新是一套成熟memory维护编排；题摘没有新增retrieval粒度选择规律、更新可靠性条件或对既有策略的具体反证。80%对fullcontext不单独准入。

https://arxiv.org/abs/2601.20352v1
arXiv:2601.20352v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 8 Sep 2026 (v4)]
Title:AMA: Adaptive Memory via Multi-Agent Collaboration
Authors:Weiquan Huang, Zixuan Wang, Hehai Lin, Sudong Wang, Bo Xu, Qian Li, Beier Zhu, Linyi Yang, Chengwei Qin
View a PDF of the paper titled AMA: Adaptive Memory via Multi-Agent Collaboration, by Weiquan Huang and 8 other authors
View PDF
HTML (experimental)
Abstract:The rapid evolution of Large Language Model (LLM) agents has necessitated robust memory systems to support cohesive long-term interaction and complex reasoning. Benefiting from the strong capabilities of LLMs, recent research focus has shifted from simple context extension to the development of dedicated agentic memory systems. However, existing approaches typically rely on rigid retrieval granularity, accumulation-heavy maintenance strategies, and coarse-grained update mechanisms. These design choices create a persistent mismatch between stored information and task-specific reasoning demands, while leading to the unchecked accumulation of logical inconsistencies over time. To address these challenges, we propose Adaptive Memory via Multi-Agent Collaboration (AMA), a novel framework that leverages coordinated agents to manage memory across multiple granularities. AMA employs a hierarchical memory design that dynamically aligns retrieval granularity with task complexity. Specifically, the Constructor and Retriever jointly enable multi-granularity memory construction and adaptive query routing. The Judge verifies the relevance and consistency of retrieved content, triggering iterative retrieval when evidence is insufficient or invoking the Refresher upon detecting logical conflicts. The Refresher then enforces memory consistency by performing targeted updates or removing outdated entries. Extensive experiments on challenging long-context benchmarks show that AMA significantly outperforms state-of-the-art baselines while reducing token consumption by approximately 80% compared to full-context methods, demonstrating its effectiveness in maintaining retrieval precision and long-term memory consistency.
Comments:
8 pages
Subjects:
Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20352 [cs.AI]
(or
arXiv:2601.20352v1 [cs.AI] for this version)
https://doi.org/10.48550/arXiv.2601.20352
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Weiquan Huang [view email]          [v1]
Wed, 28 Jan 2026 08:09:49 UTC (3,559 KB)
[v2]
Mon, 2 Feb 2026 07:41:51 UTC (3,559 KB)
[v3]
Wed, 15 Apr 2026 14:20:46 UTC (3,559 KB)
[v4]
Tue, 8 Sep 2026 08:12:42 UTC (3,559 KB)



## 2601.19956

贡献符合但首公开待定：说话人区分和全局隐私检测不足以约束条件性信息流→multiuser/context secrecy/proactive三层blindspot及真实语音反侧→重考虑speaker-aware评测而不是只识别speaker。2+2+2=6；安全边界须深入，但v1Submitted01/27早于本窗最早标准公告，先恢复firstday，不能Created倒定。

https://arxiv.org/abs/2601.19956v1
arXiv:2601.19956v1 (eess)
[Submitted on 27 Jan 2026 (this version), latest version 3 Sep 2026 (v2)]
Title:VoxPrivacy: A Benchmark for Evaluating Interactional Privacy of Speech Language Models
Authors:Yuxiang Wang, Hongyu Liu, Dekun Chen, Xueyao Zhang, Zhizheng Wu
View a PDF of the paper titled VoxPrivacy: A Benchmark for Evaluating Interactional Privacy of Speech Language Models, by Yuxiang Wang and 4 other authors
View PDF
HTML (experimental)
Abstract:As Speech Language Models (SLMs) transition from personal devices to shared, multi-user environments such as smart homes, a new challenge emerges: the model is expected to distinguish between users to manage information flow appropriately. Without this capability, an SLM could reveal one user's confidential schedule to another, a privacy failure we term interactional privacy. Thus, the ability to generate speaker-aware responses becomes essential for SLM safe deployment. Current SLM benchmarks test dialogue ability but overlook speaker identity. Multi-speaker benchmarks check who said what without assessing whether SLMs adapt their responses. Privacy benchmarks focus on globally sensitive data (e.g., bank passwords) while neglecting contextual privacy-sensitive information (e.g., a user's private appointment). To address this gap, we introduce VoxPrivacy, the first benchmark designed to evaluate interactional privacy in SLMs. VoxPrivacy spans three tiers of increasing difficulty, from following direct secrecy commands to proactively protecting privacy. Our evaluation of nine SLMs on a 32-hour bilingual dataset reveals a widespread vulnerability: most open-source models perform close to random chance (around 50% accuracy) on conditional privacy decisions, while even strong closed-source systems fall short on proactive privacy inference. We further validate these findings on Real-VoxPrivacy, a human-recorded subset, confirming that failures observed on synthetic data persist in real speech. Finally, we demonstrate a viable path forward: by fine-tuning on a new 4,000-hour training set, we improve privacy-preserving abilities while maintaining robustness. To support future work, we release the VoxPrivacy benchmark, the large-scale training set, and the fine-tuned model to foster the development of safer and more context-aware SLMs.
Subjects:
Audio and Speech Processing (eess.AS); Artificial Intelligence (cs.AI); Sound (cs.SD)
Cite as:
arXiv:2601.19956 [eess.AS]
(or
arXiv:2601.19956v1 [eess.AS] for this version)
https://doi.org/10.48550/arXiv.2601.19956
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yuxiang Wang [view email]          [v1]
Tue, 27 Jan 2026 06:22:14 UTC (2,342 KB)
[v2]
Thu, 3 Sep 2026 06:04:10 UTC (2,335 KB)



## 2601.20379

拟准入：冻结policy的轨迹筛选→单instance execution feedback驱动transient LoRA GRPO更新→重考虑testtime采样预算与在线训练成本/污染隔离。2+2+2=6。

https://arxiv.org/abs/2601.20379v1
arXiv:2601.20379v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 15 Jul 2026 (v2)]
Title:Policy of Thoughts: Scaling LLM Reasoning via Test-time Policy Evolution
Authors:Zhengbo Jiao, Hongyu Xian, Qinglong Wang, Yunpu Ma, Zhebo Wang, Zifan Zhang, Dezhang Kong, Meng Han
View a PDF of the paper titled Policy of Thoughts: Scaling LLM Reasoning via Test-time Policy Evolution, by Zhengbo Jiao and 7 other authors
View PDF
HTML (experimental)
Abstract:Large language models (LLMs) struggle with complex, long-horizon reasoning due to instability caused by their frozen policy assumption. Current test-time scaling methods treat execution feedback merely as an external signal for filtering or rewriting trajectories, without internalizing it to improve the underlying reasoning strategy. Inspired by Popper's epistemology of "conjectures and refutations," we argue that intelligence requires real-time evolution of the model's policy through learning from failed attempts. We introduce Policy of Thoughts (PoT), a framework that recasts reasoning as a within-instance online optimization process. PoT first generates diverse candidate solutions via an efficient exploration mechanism, then uses Group Relative Policy Optimization (GRPO) to update a transient LoRA adapter based on execution feedback. This closed-loop design enables dynamic, instance-specific refinement of the model's reasoning priors. Experiments show that PoT dramatically boosts performance: a 4B model achieves 49.71% accuracy on LiveCodeBench, outperforming GPT-4o and DeepSeek-V3 despite being over 50 smaller.
Comments:
19 pages, 5 figures
Subjects:
Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20379 [cs.AI]
(or
arXiv:2601.20379v1 [cs.AI] for this version)
https://doi.org/10.48550/arXiv.2601.20379
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Zhengbo Jiao [view email]          [v1]
Wed, 28 Jan 2026 08:44:34 UTC (494 KB)
[v2]
Wed, 15 Jul 2026 09:42:57 UTC (486 KB)



## 2601.20334

拟准入：VLA通常需要demo→unmodified coding agent在privileged state的deliberative manipulation可成功→修正何种任务确需learned低层策略；不是普适替代，必须核state特权与任务类/成本。2+2+2=6。

https://arxiv.org/abs/2601.20334v1
arXiv:2601.20334v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 28 Jun 2026 (v2)]
Title:Demonstration-Free Robotic Control via LLM Agents
Authors:Brian Y. Tsui, Alan Y. Fang, Tiffany J. Hwu
View a PDF of the paper titled Demonstration-Free Robotic Control via LLM Agents, by Brian Y. Tsui and 2 other authors
View PDF
HTML (experimental)
Abstract:Robotic manipulation has increasingly adopted vision-language-action (VLA) models, which achieve strong performance but typically require task-specific demonstrations and fine-tuning, and often generalize poorly under domain shift. We investigate whether general-purpose large language model (LLM) agent frameworks, originally developed for software engineering, can serve as an alternative control paradigm for embodied manipulation. We introduce FAEA (Frontier Agent as Embodied Agent), which applies an LLM agent framework directly to embodied manipulation without modification. Using the same iterative reasoning that enables software agents to debug code, FAEA enables embodied agents to reason through manipulation strategies. We evaluate an unmodified frontier agent, Claude Agent SDK, across the LIBERO, ManiSkill3, and MetaWorld benchmarks. With privileged environment state access, FAEA achieves success rates of 84.9%, 85.7%, and 96%, respectively. This level of task success approaches that of VLA models trained with less than 100 demonstrations per task, without requiring demonstrations or fine-tuning. With one round of human feedback as an optional optimization, performance increases to 88.2% on LIBERO. This demonstration-free capability has immediate practical value: FAEA can autonomously explore novel scenarios in simulation and generate successful trajectories for training data augmentation in embodied learning. Our results indicate that general-purpose agents are sufficient for a class of manipulation tasks dominated by deliberative, task-level planning. This opens a path for robotics systems to leverage actively maintained agent infrastructure and benefit directly from ongoing advances in frontier models. Code is available at this https URL
Subjects:
Robotics (cs.RO); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
Cite as:
arXiv:2601.20334 [cs.RO]
(or
arXiv:2601.20334v1 [cs.RO] for this version)
https://doi.org/10.48550/arXiv.2601.20334
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Tiffany Hwu [view email]          [v1]
Wed, 28 Jan 2026 07:49:35 UTC (19 KB)
[v2]
Sun, 28 Jun 2026 07:42:25 UTC (91 KB)



## 2601.20408

初拟贡献关闭：abstract提供distributed optimization平台、dynamicallocation/stagedpipeline/cleanup集成配方及生产2x数字，没有具体新allocation执行机制、SLO成立边界或可比质量/资源条件。不会因为开放源与生产声称升格。

https://arxiv.org/abs/2601.20408v1
arXiv:2601.20408v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 8 Jun 2026 (v2)]
Title:Meeting SLOs, Slashing Hours: Automated Enterprise LLM Optimization with OptiKIT
Authors:Nicholas Santavas, Kareem Eissa, Patrycja Cieplicka, Piotr Florek, Matteo Nulli, Stefan Vasilev, Seyyed Hadi Hashemi, Antonios Gasteratos, Shahram Khadivi
View a PDF of the paper titled Meeting SLOs, Slashing Hours: Automated Enterprise LLM Optimization with OptiKIT, by Nicholas Santavas and 8 other authors
View PDF
HTML (experimental)
Abstract:Enterprise LLM deployment faces a critical scalability challenge: organizations must optimize models systematically to scale AI initiatives within constrained compute budgets, yet the specialized expertise required for manual optimization remains a niche and scarce skillset. This challenge is particularly evident in managing GPU utilization across heterogeneous infrastructure while enabling teams with diverse workloads and limited LLM optimization experience to deploy models efficiently.
We present OptiKIT, a distributed LLM optimization framework that democratizes model compression and tuning by automating complex optimization workflows for non-expert teams. OptiKIT provides dynamic resource allocation, staged pipeline execution with automatic cleanup, and seamless enterprise integration.
In production, it delivers more than 2x GPU throughput improvement while empowering application teams to achieve consistent performance improvements without deep LLM optimization expertise. We share both the platform design and key engineering insights into resource allocation algorithms, pipeline orchestration, and integration patterns that enable large-scale, production-grade democratization of model optimization. Finally, we open-source the system to enable external contributions and broader reproducibility.
Comments:
Accepted in MLSys 2026
Subjects:
Distributed, Parallel, and Cluster Computing (cs.DC); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20408 [cs.DC]
(or
arXiv:2601.20408v1 [cs.DC] for this version)
https://doi.org/10.48550/arXiv.2601.20408
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Nicholas Santavas Mr [view email]          [v1]
Wed, 28 Jan 2026 09:13:17 UTC (1,061 KB)
[v2]
Mon, 8 Jun 2026 09:56:22 UTC (5,373 KB)



## 2601.19923

贡献符合但首公开待定：textmetric掩盖结构漂移→deterministicIR分离Content Semantic Accuracy与treeedit，并声称nesting深度统一瓶颈→重考虑结构与内容混测评价。2+2+2=6；Submitted01/09，日期包络跨本窗。

https://arxiv.org/abs/2601.19923v1
arXiv:2601.19923v1 (cs)
[Submitted on 9 Jan 2026 (this version), latest version 15 May 2026 (v2)]
Title:Table-BiEval: A Self-Supervised, Dual-Track Framework for Decoupling Structure and Content in LLM Evaluation
Authors:Boxiang Zhao, Qince Li, Zhonghao Wang, Zelin Cao, Yi Wang, Peng Cheng, Bo Lin
View a PDF of the paper titled Table-BiEval: A Self-Supervised, Dual-Track Framework for Decoupling Structure and Content in LLM Evaluation, by Boxiang Zhao and 6 other authors
View PDF
Abstract:As Large Language Models (LLMs) evolve into autonomous agents, the capability to faithfully translate natural language into rigorous structured formats-essential for tool invocation-and to convert complex tabular information into machine-readable specifications has become paramount. However, current evaluations lack effective methodologies to measure this structural fidelity without costly human intervention, as traditional text metrics fail to detect semantic drift in code-like outputs. This paper proposes Table-BiEval, a novel approach based on a human-free, self-supervised evaluation framework, to assess LLMs performance quantitatively. By leveraging deterministic Intermediate Representations, our framework calculates Content Semantic Accuracy and Normalized Tree Edit Distance to decouple structure from content. Also, it empirically evaluates 15 state-of-the-art LLMs across dual topological dimensions-hierarchical structures and flat tables. The results reveal substantial variability, highlighting that mid-sized models can surprisingly outperform larger counterparts in structural efficiency and confirming that deep recursive nesting remains a universal bottleneck for current architectures.
Subjects:
Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.19923 [cs.CL]
(or
arXiv:2601.19923v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.19923
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Zhonghao Wang [view email]          [v1]
Fri, 9 Jan 2026 07:38:27 UTC (3,233 KB)
[v2]
Fri, 15 May 2026 01:35:14 UTC (13,120 KB)



## 2601.20251

拟准入：固定query预算适应性选择会破坏CI覆盖→FAQ历史factor model+hybridselection+finite-population主动推断保coverage→重考虑省query不牺牲频率学有效性的设计。2+2+3=7。

https://arxiv.org/abs/2601.20251v1
arXiv:2601.20251v1 (stat)
[Submitted on 28 Jan 2026 (this version), latest version 8 May 2026 (v3)]
Title:Efficient Evaluation of LLM Performance with Statistical Guarantees
Authors:Skyler Wu, Yash Nair, Emmanuel J. Candés
View a PDF of the paper titled Efficient Evaluation of LLM Performance with Statistical Guarantees, by Skyler Wu and 2 other authors
View PDF
HTML (experimental)
Abstract:Exhaustively evaluating many large language models (LLMs) on a large suite of benchmarks is expensive. We cast benchmarking as finite-population inference and, under a fixed query budget, seek tight confidence intervals (CIs) for model accuracy with valid frequentist coverage. We propose Factorized Active Querying (FAQ), which (a) leverages historical information through a Bayesian factor model; (b) adaptively selects questions using a hybrid variance-reduction/active-learning sampling policy; and (c) maintains validity through Proactive Active Inference -- a finite-population extension of active inference (Zrnic & Candes, 2024) that enables direct question selection while preserving coverage. With negligible overhead cost, FAQ delivers up to $5\times$ effective sample size gains over strong baselines on two benchmark suites, across varying historical-data missingness levels: this means that it matches the CI width of uniform sampling while using up to $5\times$ fewer queries. We release our source code and our curated datasets to support reproducible evaluation and future research.
Comments:
24 pages, 10 figures
Subjects:
Machine Learning (stat.ML); Machine Learning (cs.LG)
Cite as:
arXiv:2601.20251 [stat.ML]
(or
arXiv:2601.20251v1 [stat.ML] for this version)
https://doi.org/10.48550/arXiv.2601.20251
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Skyler Wu [view email]          [v1]
Wed, 28 Jan 2026 04:59:20 UTC (488 KB)
[v2]
Thu, 29 Jan 2026 03:01:40 UTC (483 KB)
[v3]
Fri, 8 May 2026 20:35:11 UTC (467 KB)



## 2601.20375

初拟贡献关闭：策略生成-比较-迭代、distribution-preservingsample/binaryfilter/cache组合和局部winrate；题摘没有新sampling准则/数据质量成立边界。无human access不作为privacy guarantee，不能用healthcare域借securityOwner收。

https://arxiv.org/abs/2601.20375v1
arXiv:2601.20375v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 7 May 2026 (v2)]
Title:LLM-AutoDP: Automatic Data Processing via LLM Agents for Model Fine-tuning
Authors:Wei Huang, Anda Cheng, Yinggui Wang, Lei Wang, Tao Wei
View a PDF of the paper titled LLM-AutoDP: Automatic Data Processing via LLM Agents for Model Fine-tuning, by Wei Huang and 4 other authors
View PDF
HTML (experimental)
Abstract:Large Language Models (LLMs) can be fine-tuned on domain-specific data to enhance their performance in specialized fields. However, such data often contains numerous low-quality samples, necessitating effective data processing (DP). In practice, DP strategies are typically developed through iterative manual analysis and trial-and-error adjustment. These processes inevitably incur high labor costs and may lead to privacy issues in high-privacy domains like healthcare due to direct human access to sensitive data. Thus, achieving automated data processing without exposing the raw data has become a critical challenge. To address this challenge, we propose LLM-AutoDP, a novel framework that leverages LLMs as agents to automatically generate and optimize data processing strategies. Our method generates multiple candidate strategies and iteratively refines them using feedback signals and comparative evaluations. This iterative in-context learning mechanism enables the agent to converge toward high-quality processing pipelines without requiring direct human intervention or access to the underlying data. To further accelerate strategy search, we introduce three key techniques: Distribution Preserving Sampling, which reduces data volume while maintaining distributional integrity; Processing Target Selection, which uses a binary classifier to identify low-quality samples for focused processing; Cache-and-Reuse Mechanism}, which minimizes redundant computations by reusing prior processing results. Results show that models trained on data processed by our framework achieve over 80% win rates against models trained on unprocessed data. Compared to AutoML baselines based on LLM agents, LLM-AutoDP achieves approximately a 65% win rate. Moreover, our acceleration techniques reduce the total searching time by up to 10 times, demonstrating both effectiveness and efficiency.
Comments:
Accepted by VLDB2026
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
Cite as:
arXiv:2601.20375 [cs.LG]
(or
arXiv:2601.20375v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20375
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Anda Cheng [view email]          [v1]
Wed, 28 Jan 2026 08:37:34 UTC (1,531 KB)
[v2]
Thu, 7 May 2026 02:38:44 UTC (1,524 KB)



## 2601.20055

拟准入：单pass/表面consensus缺逻辑定位→formal equivalence、claimtype routing、MCS定位限定反馈→重考虑修正何种claim与logicalconsistency/groundtruth边界。2+2+2=6；标准评价必须核autoformalization不把formaltruth泛化。

https://arxiv.org/abs/2601.20055v1
arXiv:2601.20055v1 (cs)
[Submitted on 27 Jan 2026 (this version), latest version 2 May 2026 (v2)]
Title:VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning
Authors:Vikash Singh, Darion Cassel, Nathaniel Weir, Nick Feng, Sam Bayless
View a PDF of the paper titled VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning, by Vikash Singh and 4 other authors
View PDF
HTML (experimental)
Abstract:Despite the syntactic fluency of Large Language Models (LLMs), ensuring their logical correctness in high-stakes domains remains a fundamental challenge. We present a neurosymbolic framework that combines LLMs with SMT solvers to produce verification-guided answers through iterative refinement. Our approach decomposes LLM outputs into atomic claims, autoformalizes them into first-order logic, and verifies their logical consistency using automated theorem proving. We introduce three key innovations: (1) multi-model consensus via formal semantic equivalence checking to ensure logic-level alignment between candidates, eliminating the syntactic bias of surface-form metrics, (2) semantic routing that directs different claim types to appropriate verification strategies: symbolic solvers for logical claims and LLM ensembles for commonsense reasoning, and (3) precise logical error localization via Minimal Correction Subsets (MCS), which pinpoint the exact subset of claims to revise, transforming binary failure signals into actionable feedback. Our framework classifies claims by their logical status and aggregates multiple verification signals into a unified score with variance-based penalty. The system iteratively refines answers using structured feedback until acceptance criteria are met or convergence is achieved. This hybrid approach delivers formal guarantees where possible and consensus verification elsewhere, advancing trustworthy AI. With the GPT-OSS-120B model, VERGE demonstrates an average performance uplift of 18.7% at convergence across a set of reasoning benchmarks compared to single-pass approaches.
Subjects:
Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20055 [cs.CL]
(or
arXiv:2601.20055v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20055
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Darion Cassel [view email]          [v1]
Tue, 27 Jan 2026 20:59:11 UTC (550 KB)
[v2]
Sat, 2 May 2026 03:45:31 UTC (554 KB)



## 2601.20706

拟准入：GEMM-centric NPU忽视dLLM sampling→vocabulary logits/reduction/maskedupdates占资源、nonGEMMvector+inplace+mixedprecisionhierarchy→重考虑sampling执行计划/accelerator取舍。2+2+2=6；simulation对A6000的technologynode归一化不是实测新硬件。

https://arxiv.org/abs/2601.20706v1
arXiv:2601.20706v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 23 Apr 2026 (v2)]
Title:Beyond GEMM-Centric NPUs: Enabling Efficient Diffusion LLM Sampling
Authors:Binglei Lou, Haoran Wu, Yao Lai, Jiayi Nie, Can Xiao, Xuan Guo, Rika Antonova, Robert Mullins, Aaron Zhao
View a PDF of the paper titled Beyond GEMM-Centric NPUs: Enabling Efficient Diffusion LLM Sampling, by Binglei Lou and 8 other authors
View PDF
HTML (experimental)
Abstract:Diffusion Large Language Models (dLLMs) introduce iterative denoising to enable parallel token generation, but their sampling phase displays fundamentally different characteristics compared to GEMM-centric transformer layers. Profiling on modern GPUs reveals that sampling can account for up to 70% of total model inference latency-primarily due to substantial memory loads and writes from vocabulary-wide logits, reduction-based token selection, and iterative masked updates. These processes demand large on-chip SRAM and involve irregular memory accesses that conventional NPUs struggle to handle efficiently. To address this, we identify a set of critical instructions that an NPU architecture must specifically optimize for dLLM sampling. Our design employs lightweight non-GEMM vector primitives, in-place memory reuse strategies, and a decoupled mixed-precision memory hierarchy. Together, these optimizations deliver up to a 2.53x speedup over the NVIDIA RTX A6000 GPU under an equivalent nm technology node. We also open-source our cycle-accurate simulation and post-synthesis RTL verification code, confirming functional equivalence with current dLLM PyTorch implementations.
Subjects:
Hardware Architecture (cs.AR); Artificial Intelligence (cs.AI); Distributed, Parallel, and Cluster Computing (cs.DC)
Cite as:
arXiv:2601.20706 [cs.AR]
(or
arXiv:2601.20706v1 [cs.AR] for this version)
https://doi.org/10.48550/arXiv.2601.20706
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Binglei Lou [view email]          [v1]
Wed, 28 Jan 2026 15:37:50 UTC (1,173 KB)
[v2]
Thu, 23 Apr 2026 17:44:25 UTC (1,443 KB)



## 2601.20009

拟准入：多语taskaccuracy不等languageconsistency→分离两bottleneck+层localization，末层finetune保持task准确→重考虑PEFT以目标layer而非uniform范围。2+1+2=5。

https://arxiv.org/abs/2601.20009v1
arXiv:2601.20009v1 (cs)
[Submitted on 27 Jan 2026 (this version), latest version 22 Mar 2026 (v2)]
Title:LinguaMap: Which Layers of LLMs Speak Your Language and How to Tune Them?
Authors:J. Ben Tamo, Daniel Carlander-Reuterfelt, Jonathan Rubin, Dezhi Hong, Mingxian Wang, Oleg Poliannikov
View a PDF of the paper titled LinguaMap: Which Layers of LLMs Speak Your Language and How to Tune Them?, by J. Ben Tamo and 4 other authors
View PDF
Abstract:Despite multilingual pretraining, large language models often struggle with non-English tasks, particularly in language control, the ability to respond in the intended language. We identify and characterize two key failure modes: the multilingual transfer bottleneck (correct language, incorrect task response) and the language consistency bottleneck (correct task response, wrong language). To systematically surface these issues, we design a four-scenario evaluation protocol spanning MMLU, MGSM, and XQuAD benchmarks. To probe these issues with interpretability, we extend logit lens analysis to track language probabilities layer by layer and compute cross-lingual semantic similarity of hidden states. The results reveal a three-phase internal structure: early layers align inputs into a shared semantic space, middle layers perform task reasoning, and late layers drive language-specific generation. Guided by these insights, we introduce selective fine-tuning of only the final layers responsible for language control. On Qwen-3-32B and Bloom-7.1B, this method achieves over 98 percent language consistency across six languages while fine-tuning only 3-5 percent of parameters, without sacrificing task accuracy. Importantly, this result is nearly identical to that of full-scope fine-tuning (for example, above 98 percent language consistency for both methods across all prompt scenarios) but uses a fraction of the computational resources. To the best of our knowledge, this is the first approach to leverage layer-localization of language control for efficient multilingual adaptation.
Subjects:
Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
Cite as:
arXiv:2601.20009 [cs.CL]
(or
arXiv:2601.20009v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20009
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Junior Ben Tamo [view email]          [v1]
Tue, 27 Jan 2026 19:38:12 UTC (733 KB)
[v2]
Sun, 22 Mar 2026 02:37:29 UTC (538 KB)



## 2601.20538

初拟贡献关闭：economics/financial/social simulation中对agent动作做Shapley事后归因及risk统计，不是新增LLM执行机制、协作可靠性条件；系统safety类比不引入领域模拟。

https://arxiv.org/abs/2601.20538v1
arXiv:2601.20538v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 15 Feb 2026 (v2)]
Title:Interpreting Emergent Extreme Events in Multi-Agent Systems
Authors:Ling Tang, Jilin Mei, Dongrui Liu, Chen Qian, Dawei Cheng, Jing Shao, Xia Hu
View a PDF of the paper titled Interpreting Emergent Extreme Events in Multi-Agent Systems, by Ling Tang and 6 other authors
View PDF
HTML (experimental)
Abstract:Large language model-powered multi-agent systems have emerged as powerful tools for simulating complex human-like systems. The interactions within these systems often lead to extreme events whose origins remain obscured by the black box of emergence. Interpreting these events is critical for system safety. This paper proposes the first framework for explaining emergent extreme events in multi-agent systems, aiming to answer three fundamental questions: When does the event originate? Who drives it? And what behaviors contribute to it? Specifically, we adapt the Shapley value to faithfully attribute the occurrence of extreme events to each action taken by agents at different time steps, i.e., assigning an attribution score to the action to measure its influence on the event. We then aggregate the attribution scores along the dimensions of time, agent, and behavior to quantify the risk contribution of each dimension. Finally, we design a set of metrics based on these contribution scores to characterize the features of extreme events. Experiments across diverse multi-agent system scenarios (economic, financial, and social) demonstrate the effectiveness of our framework and provide general insights into the emergence of extreme phenomena.
Comments:
8 pages, 5 figures
Subjects:
Multiagent Systems (cs.MA); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20538 [cs.MA]
(or
arXiv:2601.20538v1 [cs.MA] for this version)
https://doi.org/10.48550/arXiv.2601.20538
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Ling Tang [view email]          [v1]
Wed, 28 Jan 2026 12:32:16 UTC (3,484 KB)
[v2]
Sun, 15 Feb 2026 09:47:35 UTC (3,484 KB)



## 2601.20125

拟准入：AR单pattern隐私攻击经验不足以覆盖DLM可probe多个mask→跨density子集符号统计/逆权重聚合SAMA→重考虑bidirectionalmaskability的攻击与审计条件。2+2+2=6；具体安全主张深入核假设/低FPR。

https://arxiv.org/abs/2601.20125v1
arXiv:2601.20125v1 (cs)
[Submitted on 27 Jan 2026 (this version), latest version 6 Feb 2026 (v3)]
Title:Membership Inference Attacks Against Fine-tuned Diffusion Language Models
Authors:Yuetian Chen, Kaiyuan Zhang, Yuntao Du, Edoardo Stoppa, Charles Fleming, Ashish Kundu, Bruno Ribeiro, Ninghui Li
View a PDF of the paper titled Membership Inference Attacks Against Fine-tuned Diffusion Language Models, by Yuetian Chen and 7 other authors
View PDF
HTML (experimental)
Abstract:Diffusion Language Models (DLMs) represent a promising alternative to autoregressive language models, using bidirectional masked token prediction. Yet their susceptibility to privacy leakage via Membership Inference Attacks (MIA) remains critically underexplored. This paper presents the first systematic investigation of MIA vulnerabilities in DLMs. Unlike the autoregressive models' single fixed prediction pattern, DLMs' multiple maskable configurations exponentially increase attack opportunities. This ability to probe many independent masks dramatically improves detection chances. To exploit this, we introduce SAMA (Subset-Aggregated Membership Attack), which addresses the sparse signal challenge through robust aggregation. SAMA samples masked subsets across progressive densities and applies sign-based statistics that remain effective despite heavy-tailed noise. Through inverse-weighted aggregation prioritizing sparse masks' cleaner signals, SAMA transforms sparse memorization detection into a robust voting mechanism. Experiments on nine datasets show SAMA achieves 30% relative AUC improvement over the best baseline, with up to 8 times improvement at low false positive rates. These findings reveal significant, previously unknown vulnerabilities in DLMs, necessitating the development of tailored privacy defenses.
Comments:
Accepted for presentation at ICLR 2026 (pending final camera-ready)
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20125 [cs.LG]
(or
arXiv:2601.20125v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20125
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yuetian Chen [view email]          [v1]
Tue, 27 Jan 2026 23:40:07 UTC (453 KB)
[v2]
Sun, 1 Feb 2026 20:06:02 UTC (453 KB)
[v3]
Fri, 6 Feb 2026 20:40:57 UTC (455 KB)



## 2601.20339

拟准入：DLM单decodingtrajectory忽视可选生成order→jointorder/tokensearch+denoisingaction likelihood estimator→重考虑搜索分支与采样预算。2+2+2=6。

https://arxiv.org/abs/2601.20339v1
arXiv:2601.20339v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 5 Feb 2026 (v2)]
Title:Improving Diffusion Language Model Decoding through Joint Search in Generation Order and Token Space
Authors:Yangyi Shen, Tianjian Feng, Jiaqi Han, Wen Wang, Tianlang Chen, Chunhua Shen, Jure Leskovec, Stefano Ermon
View a PDF of the paper titled Improving Diffusion Language Model Decoding through Joint Search in Generation Order and Token Space, by Yangyi Shen and 7 other authors
View PDF
HTML (experimental)
Abstract:Diffusion Language Models (DLMs) offer order-agnostic generation that can explore many possible decoding trajectories. However, current decoding methods commit to a single trajectory, limiting exploration in trajectory space. We introduce Order-Token Search to explore this space through jointly searching over generation order and token values. Its core is a likelihood estimator that scores denoising actions, enabling stable pruning and efficient exploration of diverse trajectories. Across mathematical reasoning and coding benchmarks, Order-Token Search consistently outperforms baselines on GSM8K, MATH500, Countdown, and HumanEval (3.1%, 3.8%, 7.9%, and 6.8% absolute over backbone), matching or surpassing diffu-GRPO post-trained d1-LLaDA. Our work establishes joint search as a key component for advancing decoding in DLMs.
Subjects:
Computation and Language (cs.CL); Machine Learning (cs.LG)
Cite as:
arXiv:2601.20339 [cs.CL]
(or
arXiv:2601.20339v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20339
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yangyi Shen [view email]          [v1]
Wed, 28 Jan 2026 07:55:07 UTC (1,889 KB)
[v2]
Thu, 5 Feb 2026 02:28:16 UTC (1,890 KB)



## 2601.20834

拟准入：固定线性probe/steering特征语义假设→conversation相关factuality方向可逆变化及roleframe依赖→修正静态interpretation/steering跨context可移植性判断。2+2+3=7。

https://arxiv.org/abs/2601.20834v1
arXiv:2601.20834v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 2 Feb 2026 (v2)]
Title:Linear representations in language models can change dramatically over a conversation
Authors:Andrew Kyle Lampinen, Yuxuan Li, Eghbal Hosseini, Sangnie Bhardwaj, Murray Shanahan
View a PDF of the paper titled Linear representations in language models can change dramatically over a conversation, by Andrew Kyle Lampinen and 3 other authors
View PDF
HTML (experimental)
Abstract:Language model representations often contain linear directions that correspond to high-level concepts. Here, we study the dynamics of these representations: how representations evolve along these dimensions within the context of (simulated) conversations. We find that linear representations can change dramatically over a conversation; for example, information that is represented as factual at the beginning of a conversation can be represented as non-factual at the end and vice versa. These changes are content-dependent; while representations of conversation-relevant information may change, generic information is generally preserved. These changes are robust even for dimensions that disentangle factuality from more superficial response patterns, and occur across different model families and layers of the model. These representation changes do not require on-policy conversations; even replaying a conversation script written by an entirely different model can produce similar changes. However, adaptation is much weaker from simply having a sci-fi story in context that is framed more explicitly as such. We also show that steering along a representational direction can have dramatically different effects at different points in a conversation. These results are consistent with the idea that representations may evolve in response to the model playing a particular role that is cued by a conversation. Our findings may pose challenges for interpretability and steering -- in particular, they imply that it may be misleading to use static interpretations of features or directions, or probes that assume a particular range of features consistently corresponds to a particular ground-truth value. However, these types of representational dynamics also point to exciting new research directions for understanding how models adapt to context.
Subjects:
Computation and Language (cs.CL); Machine Learning (cs.LG)
Cite as:
arXiv:2601.20834 [cs.CL]
(or
arXiv:2601.20834v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20834
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Andrew Lampinen [view email]          [v1]
Wed, 28 Jan 2026 18:33:17 UTC (206 KB)
[v2]
Mon, 2 Feb 2026 21:30:09 UTC (207 KB)



## 2601.20321

拟准入：tactile当visualtexture忽视interactionforces→history-awareforcealigned离散latentadapter+pairedforce监督→重考虑contactrichVLA表示目标而非直接增加视觉token。2+2+2=6。

https://arxiv.org/abs/2601.20321v1
arXiv:2601.20321v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 30 Jan 2026 (v2)]
Title:Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation
Authors:Yuzhe Huang, Pei Lin, Wanlin Li, Daohan Li, Jiajun Li, Jiaming Jiang, Chenxi Xiao, Ziyuan Jiao
View a PDF of the paper titled Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation, by Yuzhe Huang and 7 other authors
View PDF
HTML (experimental)
Abstract:Vision-Language-Action (VLA) models have recently emerged as powerful generalists for robotic manipulation. However, due to their predominant reliance on visual modalities, they fundamentally lack the physical intuition required for contact-rich tasks that require precise force regulation and physical reasoning. Existing attempts to incorporate vision-based tactile sensing into VLA models typically treat tactile inputs as auxiliary visual textures, thereby overlooking the underlying correlation between surface deformation and interaction dynamics. To bridge this gap, we propose a paradigm shift from tactile-vision alignment to tactile-force alignment. Here, we introduce TaF-VLA, a framework that explicitly grounds high-dimensional tactile observations in physical interaction forces. To facilitate this, we develop an automated tactile-force data acquisition device and curate the TaF-Dataset, comprising over 10 million synchronized tactile observations, 6-axis force/torque, and matrix force map. To align sequential tactile observations with interaction forces, the central component of our approach is the Tactile-Force Adapter (TaF-Adapter), a tactile sensor encoder that extracts discretized latent information for encoding tactile observations. This mechanism ensures that the learned representations capture history-dependent, noise-insensitive physical dynamics rather than static visual textures. Finally, we integrate this force-aligned encoder into a VLA backbone. Extensive real-world experiments demonstrate that TaF-VLA policy significantly outperforms state-of-the-art tactile-vision-aligned and vision-only baselines on contact-rich tasks, verifying its ability to achieve robust, force-aware manipulation through cross-modal physical reasoning.
Comments:
17pages,9fig
Subjects:
Robotics (cs.RO)
Cite as:
arXiv:2601.20321 [cs.RO]
(or
arXiv:2601.20321v1 [cs.RO] for this version)
https://doi.org/10.48550/arXiv.2601.20321
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yuzhe Huang [view email]          [v1]
Wed, 28 Jan 2026 07:34:41 UTC (31,803 KB)
[v2]
Fri, 30 Jan 2026 13:45:08 UTC (31,804 KB)



## 2601.20755

拟准入：runtime跨层非侵入观测有部署约束→eBPF动态functionprobe及operator/hardwarecounter相关trace，无rebuild→检验LLM运行时operator可观测实现范围与overhead。1+2+2=5；只采用本地实现可验证边界，不泛称以往系统无operatorvisibility。

https://arxiv.org/abs/2601.20755v1
arXiv:2601.20755v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 29 Jan 2026 (v2)]
Title:ProfInfer: An eBPF-based Fine-Grained LLM Inference Profiler
Authors:Bohua Zou, Debayan Roy, Dhimankumar Yogesh Airao, Weihao Xu, Binqi Sun, Yutao Liu, Haibo Chen
View a PDF of the paper titled ProfInfer: An eBPF-based Fine-Grained LLM Inference Profiler, by Bohua Zou and 6 other authors
View PDF
HTML (experimental)
Abstract:As large language models (LLMs) move from research to production, understanding how inference engines behave in real time has become both essential and elusive. Unlike general-purpose engines such as ONNX Runtime, today's LLM inference systems offer little operator-level visibility, leaving developers blind to where time and resources go. Even basic questions -- is this workload memory-bound or compute-bound? -- often remain unanswered. To close this gap, we develop a fine-grained, non-intrusive profiling framework for modern LLM inference engines, exemplified by this http URL but applicable to similar runtime architectures. Built on extended Berkeley Packet Filter (eBPF) technology, our system dynamically attaches probes to runtime functions across multiple layers -- without modifying or recompiling the source. It transforms collected traces into rich visualizations of operators, graphs, timelines, and hardware counter trends, exposing how dense inference, Mixture-of-Experts routing, and operator offloading behave in practice. With less than 4% runtime overhead and high profiling fidelity, our framework makes LLM inference both transparent and diagnosable, turning performance profiling into a practical tool for optimization, scheduling, and resource-aware deployment.
Comments:
Accepted in the 9th Annual Conference on Machine Learning and Systems (MLSys 2026)
Subjects:
Software Engineering (cs.SE)
Cite as:
arXiv:2601.20755 [cs.SE]
(or
arXiv:2601.20755v1 [cs.SE] for this version)
https://doi.org/10.48550/arXiv.2601.20755
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Bohua Zou [view email]          [v1]
Wed, 28 Jan 2026 16:39:38 UTC (512 KB)
[v2]
Thu, 29 Jan 2026 10:43:56 UTC (512 KB)
