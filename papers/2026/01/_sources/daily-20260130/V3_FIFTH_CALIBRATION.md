# 2026-01-30 第五批题摘准入（作者初判）

最终修正：root实际17完整题摘及最小core：Spark20209/Trajectory20144窄5准入且必要评价通过，非tag为真实uncertainty或POMDP+SFT组合本身；CiMRAG20041普通Gaussian/量化projection无新条件EX，E2HiL19969一般HiLRL非当前foundation/VLA直接增量EX，不追日期。19944原‘非LLM’范围排除已撤销，posthoc calibration使现代tabular strongmodel proper-score变差有窄贡献5，仍DATE隔离；DIT20116 PMLR/ICML2025旧公开OUT。本批10必要Evidence已root独立核；20047中心Cor22 packing/函数类缺口终态争议NoBooks、peer20299 ideal private-signal honesty≠truth仅报告。以下保留原题摘/初判，不作最终队列。

有界题摘补检停止；明确一般领域条目不以owner映射收录。早Submitted日期仍需单点确认。

## 2601.20209

准入 2+2+2=6：uniformrollout浪费关键decisionbudget→intrinsicdecision-signal动态branch →需按关键状态探索而非全步多sample。

https://arxiv.org/abs/2601.20209v1
arXiv:2601.20209v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 20 Jun 2026 (v2)]
Title:Spark: Strategic Policy-Aware Exploration via Dynamic Branching for Long-Horizon Agentic Learning
Authors:Jinyang Wu, Shuo Yang, Changpeng Yang, Yuhao Shen, Shuai Zhang, Zhengqi Wen, Jianhua Tao
View a PDF of the paper titled Spark: Strategic Policy-Aware Exploration via Dynamic Branching for Long-Horizon Agentic Learning, by Jinyang Wu and Shuo Yang and Changpeng Yang and Yuhao Shen and Shuai Zhang and Zhengqi Wen and Jianhua Tao
View PDF
HTML (experimental)
Abstract:Reinforcement learning has empowered large language models to act as intelligent agents, yet training them for long-horizon tasks remains challenging due to the scarcity of high-quality trajectories, especially under limited resources. Existing methods typically scale up rollout sizes and indiscriminately allocate computational resources among intermediate steps. Such attempts inherently waste substantial computation budget on trivial steps while failing to guarantee sample quality. To address this, we propose \textbf{Spark} (\textbf{S}trategic \textbf{P}olicy-\textbf{A}ware explo\textbf{R}ation via \textbf{K}ey-state dynamic branching), a novel framework that selectively branches at critical decision states for resource-efficient exploration. Our key insight is to activate adaptive branching exploration at critical decision points to probe promising trajectories, thereby achieving precise resource allocation that prioritizes sampling quality over blind coverage. This design leverages the agent's intrinsic decision-making signals to reduce dependence on human priors, enabling the agent to autonomously expand exploration and achieve stronger generalization. Experiments across diverse tasks (e.g., embodied planning), demonstrate that \textsc{Spark} achieves superior success rates with significantly fewer training samples, exhibiting robust generalization even in unseen scenarios.
Subjects:
Machine Learning (cs.LG); Computation and Language (cs.CL)
Cite as:
arXiv:2601.20209 [cs.LG]
(or
arXiv:2601.20209v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20209
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Jinyang Wu [view email]          [v1]
Wed, 28 Jan 2026 03:15:34 UTC (2,554 KB)
[v2]
Sat, 20 Jun 2026 07:35:02 UTC (2,556 KB)



## 2601.20255

准入 2+1+2=5：PPL被longcontexttax与SWE性能弱相关→entropy低阶reasonablehesitation/HE-SNR检验midtrain→需核比PPL预测效度和context混杂；不采用智能定义。

https://arxiv.org/abs/2601.20255v1
arXiv:2601.20255v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 28 May 2026 (v3)]
Title:HE-SNR: Uncovering Latent Logic via Entropy for Guiding Mid-Training on SWE-BENCH
Authors:Yueyang Wang, Jiawei Fu, Baolong Bi, Xili Wang, Xiaoqing Liu
View a PDF of the paper titled HE-SNR: Uncovering Latent Logic via Entropy for Guiding Mid-Training on SWE-BENCH, by Yueyang Wang and 4 other authors
View PDF
HTML (experimental)
Abstract:SWE-bench has emerged as the premier benchmark for evaluating Large Language Models on complex software engineering tasks. While these capabilities are fundamentally acquired during the mid-training phase and subsequently elicited during Supervised Fine-Tuning (SFT), there remains a critical deficit in metrics capable of guiding mid-training effectively. Standard metrics such as Perplexity (PPL) are compromised by the "Long-Context Tax" and exhibit weak correlation with downstream SWE performance. In this paper, we bridge this gap by first introducing a rigorous data filtering strategy. Crucially, we propose the Entropy Compression Hypothesis, redefining intelligence not by scalar Top-1 compression, but by the capacity to structure uncertainty into Entropy-Compressed States of low orders ("reasonable hesitation"). Grounded in this fine-grained entropy analysis, we formulate a novel metric, HE-SNR (High-Entropy Signal-to-Noise Ratio). Validated on industrial-scale Mixture-of-Experts (MoE) models across varying context windows (32K/128K), our approach demonstrates superior robustness and predictive power. This work provides both the theoretical foundation and practical tools for optimizing the latent potential of LLMs in complex engineering domains.
Comments:
21 pages, 15 figures
Subjects:
Machine Learning (cs.LG); Computation and Language (cs.CL); Software Engineering (cs.SE)
Cite as:
arXiv:2601.20255 [cs.LG]
(or
arXiv:2601.20255v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20255
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yueyang Wang [view email]          [v1]
Wed, 28 Jan 2026 05:03:24 UTC (9,059 KB)
[v2]
Tue, 12 May 2026 08:28:20 UTC (9,235 KB)
[v3]
Thu, 28 May 2026 06:29:39 UTC (9,232 KB)



## 2601.20144

准入 2+2+2=6：fixedwellposedintent漏真实ambiguous/changing/infeasible→轨迹先行+controlledintent改造及闭环verifiable任务→toolcallcorrect≠满足动态userintent。

https://arxiv.org/abs/2601.20144v1
arXiv:2601.20144v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 21 Apr 2026 (v3)]
Title:Trajectory2Task: Training Robust Tool-Calling Agents with Synthesized Yet Verifiable Data for Complex User Intents
Authors:Ziyi Wang, Yuxuan Lu, Yimeng Zhang, Jing Huang, Jiri Gesi, Xianfeng Tang, Chen Luo, Yisi Sang, Hanqing Lu, Manling Li, Dakuo Wang
View a PDF of the paper titled Trajectory2Task: Training Robust Tool-Calling Agents with Synthesized Yet Verifiable Data for Complex User Intents, by Ziyi Wang and 10 other authors
View PDF
HTML (experimental)
Abstract:Tool-calling agents are increasingly deployed in real-world customer-facing workflows. Yet most studies on tool-calling agents focus on idealized settings with general, fixed, and well-specified tasks. In real-world applications, user requests are often (1) ambiguous, (2) changing over time, or (3) infeasible due to policy constraints, and training and evaluation data that cover these diverse, complex interaction patterns remain under-represented. To bridge the gap, we present Trajectory2Task, a verifiable data generation pipeline for studying tool use at scale under three realistic user scenarios: ambiguous intent, changing intent, and infeasible intents. The pipeline first conducts multi-turn exploration to produce valid tool-call trajectories. It then converts these trajectories into user-facing tasks with controlled intent adaptations. This process yields verifiable task that support closed-loop evaluation and training. We benchmark seven state-of-the-art LLMs on the generated complex user scenario tasks and observe frequent failures. Finally, using successful trajectories obtained from task rollouts, we fine-tune lightweight LLMs and find consistent improvements across all three conditions, along with better generalization to unseen tool-use domains, indicating stronger general tool-calling ability.
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2601.20144 [cs.CL]
(or
arXiv:2601.20144v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20144
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yuxuan Lu [view email]          [v1]
Wed, 28 Jan 2026 00:36:13 UTC (954 KB)
[v2]
Fri, 30 Jan 2026 18:44:33 UTC (954 KB)
[v3]
Tue, 21 Apr 2026 22:14:23 UTC (966 KB)



## 2601.20299

准入 2+2+3=7；安全深入：weakjudge可被strongdeceptive回答骗→peerprediction mutualpredictability激励诚实且inversecapabilitygap→需核理论honesty条件及commoncause/collusion，不能groundtruthfree等truth。

https://arxiv.org/abs/2601.20299v1
arXiv:2601.20299v1 (cs)
[Submitted on 28 Jan 2026]
Title:Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction
Authors:Tianyi Alex Qiu, Micah Carroll, Cameron Allen
View a PDF of the paper titled Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction, by Tianyi Alex Qiu and 2 other authors
View PDF
HTML (experimental)
Abstract:The evaluation and post-training of large language models (LLMs) rely on supervision, but strong supervision for difficult tasks is often unavailable, especially when evaluating frontier models. In such cases, models are demonstrated to exploit evaluations built on such imperfect supervision, leading to deceptive results. However, underutilized in LLM research, a wealth of mechanism design research focuses on game-theoretic incentive compatibility, i.e., eliciting honest and informative answers with weak supervision. Drawing from this literature, we introduce the peer prediction method for model evaluation and post-training. It rewards honest and informative answers over deceptive and uninformative ones, using a metric based on mutual predictability and without requiring ground truth labels. We demonstrate the method's effectiveness and resistance to deception, with both theoretical guarantees and empirical validation on models with up to 405B parameters. We show that training an 8B model with peer prediction-based reward recovers most of the drop in truthfulness due to prior malicious finetuning, even when the reward is produced by a 0.135B language model with no finetuning. On the evaluation front, in contrast to LLM-as-a-Judge which requires strong and trusted judges, we discover an inverse scaling property in peer prediction, where, surprisingly, resistance to deception is strengthened as the capability gap between the experts and participants widens, enabling reliable evaluation of strong models with weak supervision. In particular, LLM-as-a-Judge become worse than random guess when facing deceptive models 5-20x the judge's size, while peer prediction thrives when such gaps are large, including in cases with over 100x size difference.
Comments:
ICLR 2026
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Computer Science and Game Theory (cs.GT)
Cite as:
arXiv:2601.20299 [cs.LG]
(or
arXiv:2601.20299v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20299
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Tianyi Qiu [view email]          [v1]
Wed, 28 Jan 2026 06:47:46 UTC (3,660 KB)



## 2601.20116

窗外先公开保留；非当窗候选：ICML2025官方评论是既有公开线索；DIT优势加权从suboptimaloffline行为学习有贡献但不把Jan29metadata重新算firstpublic。

https://arxiv.org/abs/2601.20116v1
arXiv:2601.20116v1 (cs)
[Submitted on 27 Jan 2026]
Title:In-Context Reinforcement Learning From Suboptimal Historical Data
Authors:Juncheng Dong, Moyang Guo, Ethan X. Fang, Zhuoran Yang, Vahid Tarokh
View a PDF of the paper titled In-Context Reinforcement Learning From Suboptimal Historical Data, by Juncheng Dong and 4 other authors
View PDF
HTML (experimental)
Abstract:Transformer models have achieved remarkable empirical successes, largely due to their in-context learning capabilities. Inspired by this, we explore training an autoregressive transformer for in-context reinforcement learning (ICRL). In this setting, we initially train a transformer on an offline dataset consisting of trajectories collected from various RL tasks, and then fix and use this transformer to create an action policy for new RL tasks. Notably, we consider the setting where the offline dataset contains trajectories sampled from suboptimal behavioral policies. In this case, standard autoregressive training corresponds to imitation learning and results in suboptimal performance. To address this, we propose the Decision Importance Transformer(DIT) framework, which emulates the actor-critic algorithm in an in-context manner. In particular, we first train a transformer-based value function that estimates the advantage functions of the behavior policies that collected the suboptimal trajectories. Then we train a transformer-based policy via a weighted maximum likelihood estimation loss, where the weights are constructed based on the trained value function to steer the suboptimal policies to the optimal ones. We conduct extensive experiments to test the performance of DIT on both bandit and Markov Decision Process problems. Our results show that DIT achieves superior performance, particularly when the offline dataset contains suboptimal historical data.
Comments:
Accepted to Forty-Second International Conference on Machine Learning (ICML2025)
Subjects:
Machine Learning (cs.LG)
Cite as:
arXiv:2601.20116 [cs.LG]
(or
arXiv:2601.20116v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20116
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Juncheng Dong [view email]          [v1]
Tue, 27 Jan 2026 23:13:06 UTC (1,264 KB)



## 2601.19969

贡献符合；DATE待定：HITLRL用policyentropyinfluence选moderate样本，移除sharpdrop shortcuts与negligiblenoise →humanintervention按信号质量分配；早Submitted先核date。

https://arxiv.org/abs/2601.19969v1
arXiv:2601.19969v1 (cs)
[Submitted on 27 Jan 2026 (this version), latest version 25 Aug 2026 (v2)]
Title:E2HiL: Entropy-Guided Sample Selection for Efficient Real-World Human-in-the-Loop Reinforcement Learning
Authors:Haoyuan Deng, Yuanjiang Xue, Haoyang Du, Boyang Zhou, Zhenyu Wu, Ziwei Wang
View a PDF of the paper titled E2HiL: Entropy-Guided Sample Selection for Efficient Real-World Human-in-the-Loop Reinforcement Learning, by Haoyuan Deng and 5 other authors
View PDF
HTML (experimental)
Abstract:Human-in-the-loop guidance has emerged as an effective approach for enabling faster convergence in online reinforcement learning (RL) of complex real-world manipulation tasks. However, existing human-in-the-loop RL (HiL-RL) frameworks often suffer from low sample efficiency, requiring substantial human interventions to achieve convergence and thereby leading to high labor costs. To address this, we propose a sample-efficient real-world human-in-the-loop RL framework named \method, which requires fewer human intervention by actively selecting informative samples. Specifically, stable reduction of policy entropy enables improved trade-off between exploration and exploitation with higher sample efficiency. We first build influence functions of different samples on the policy entropy, which is efficiently estimated by the covariance of action probabilities and soft advantages of policies. Then we select samples with moderate values of influence functions, where shortcut samples that induce sharp entropy drops and noisy samples with negligible effect are pruned. Extensive experiments on four real-world manipulation tasks demonstrate that \method achieves a 42.1\% higher success rate while requiring 10.1\% fewer human interventions compared to the state-of-the-art HiL-RL method, validating its effectiveness. The project page providing code, videos, and mathematical formulations can be found at this https URL.
Comments:
Project page: this https URL
Subjects:
Robotics (cs.RO); Machine Learning (cs.LG)
Cite as:
arXiv:2601.19969 [cs.RO]
(or
arXiv:2601.19969v1 [cs.RO] for this version)
https://doi.org/10.48550/arXiv.2601.19969
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Zhenyu Wu [view email]          [v1]
Tue, 27 Jan 2026 18:13:22 UTC (3,354 KB)
[v2]
Tue, 25 Aug 2026 07:09:28 UTC (4,744 KB)



## 2601.20477

贡献关闭：binaryclassifierrepresentation KL随training与NPdecisionrule对齐属于统计解释/相关观察，题摘未说明新条件或能改变基础模型训练/表示选择的具体反侧，不能借假设检验术语准入。

https://arxiv.org/abs/2601.20477v1
arXiv:2601.20477v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 15 May 2026 (v4)]
Title:Implicit Hypothesis Testing and Divergence Preservation in Neural Network Representations
Authors:Kadircan Aksoy, Peter Jung, Protim Bhattacharjee
View a PDF of the paper titled Implicit Hypothesis Testing and Divergence Preservation in Neural Network Representations, by Kadircan Aksoy and 2 other authors
View PDF
HTML (experimental)
Abstract:We study the supervised training dynamics of neural classifiers through the lens of binary hypothesis testing. We model classification as a set of binary tests between class-conditional distributions of representations and empirically show that, along training trajectories, well-generalizing networks increasingly align with Neyman-Pearson optimal decision rules via monotonic improvements in KL divergence that relate to error rate exponents. We finally discuss how this yields an explanation and possible training or regularization strategies for different classes of neural networks.
Subjects:
Machine Learning (cs.LG); Information Theory (cs.IT)
Cite as:
arXiv:2601.20477 [cs.LG]
(or
arXiv:2601.20477v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20477
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Kadircan Aksoy [view email]          [v1]
Wed, 28 Jan 2026 10:46:44 UTC (680 KB)
[v2]
Wed, 11 Feb 2026 18:32:03 UTC (680 KB)
[v3]
Mon, 11 May 2026 10:46:14 UTC (943 KB)
[v4]
Fri, 15 May 2026 15:24:06 UTC (943 KB)



## 2601.20047

准入 2+1+3=6：boundedradiusEuclidean层级collapse需指数Lipschitz/samplevs hyperbolic constantdistortion O(mRlogm) →representation几何与capacityregularization共同决定层级可学习性；理论不是所有embedding。

https://arxiv.org/abs/2601.20047v1
arXiv:2601.20047v1 (stat)
[Submitted on 27 Jan 2026]
Title:Minimax Rates for Hyperbolic Hierarchical Learning
Authors:Divit Rawal, Sriram Vishwanath
View a PDF of the paper titled Minimax Rates for Hyperbolic Hierarchical Learning, by Divit Rawal and 1 other authors
View PDF
HTML (experimental)
Abstract:We prove an exponential separation in sample complexity between Euclidean and hyperbolic representations for learning on hierarchical data under standard Lipschitz regularization. For depth-$R$ hierarchies with branching factor $m$, we first establish a geometric obstruction for Euclidean space: any bounded-radius embedding forces volumetric collapse, mapping exponentially many tree-distant points to nearby locations. This necessitates Lipschitz constants scaling as $\exp(\Omega(R))$ to realize even simple hierarchical targets, yielding exponential sample complexity under capacity control. We then show this obstruction vanishes in hyperbolic space: constant-distortion hyperbolic embeddings admit $O(1)$-Lipschitz realizability, enabling learning with $n = O(mR \log m)$ samples. A matching $\Omega(mR \log m)$ lower bound via Fano's inequality establishes that hyperbolic representations achieve the information-theoretic optimum. We also show a geometry-independent bottleneck: any rank-$k$ prediction space captures only $O(k)$ canonical hierarchical contrasts.
Subjects:
Machine Learning (stat.ML); Machine Learning (cs.LG)
Cite as:
arXiv:2601.20047 [stat.ML]
(or
arXiv:2601.20047v1 [stat.ML] for this version)
https://doi.org/10.48550/arXiv.2601.20047
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Divit Rawal [view email]          [v1]
Tue, 27 Jan 2026 20:50:24 UTC (37 KB)



## 2601.19944

范围关闭：realIID tabularbinary 21classifiers posthoccalibrator排行榜与局部退化，非当前foundationmodel/训练推理系统机制切片；不把泛化Evaluation owner当入范围理由。

https://arxiv.org/abs/2601.19944v1
arXiv:2601.19944v1 (cs)
[Submitted on 19 Jan 2026]
Title:Classifier Calibration at Scale: An Empirical Study of Model-Agnostic Post-Hoc Methods
Authors:Valery Manokhin, Daniel Grønhaug
View a PDF of the paper titled Classifier Calibration at Scale: An Empirical Study of Model-Agnostic Post-Hoc Methods, by Valery Manokhin and Daniel Gr{\o}nhaug
View PDF
HTML (experimental)
Abstract:We study model-agnostic post-hoc calibration methods intended to improve probabilistic predictions in supervised binary classification on real i.i.d. tabular data, with particular emphasis on conformal and Venn-based approaches that provide distribution-free validity guarantees under exchangeability. We benchmark 21 widely used classifiers, including linear models, SVMs, tree ensembles (CatBoost, XGBoost, LightGBM), and modern tabular neural and foundation models, on binary tasks from the TabArena-v0.1 suite using randomized, stratified five-fold cross-validation with a held-out test fold. Five calibrators; Isotonic regression, Platt scaling, Beta calibration, Venn-Abers predictors, and Pearsonify are trained on a separate calibration split and applied to test predictions. Calibration is evaluated using proper scoring rules (log-loss and Brier score) and diagnostic measures (Spiegelhalter's Z, ECE, and ECI), alongside discrimination (AUC-ROC) and standard classification metrics. Across tasks and architectures, Venn-Abers predictors achieve the largest average reductions in log-loss, followed closely by Beta calibration, while Platt scaling exhibits weaker and less consistent effects. Beta calibration improves log-loss most frequently across tasks, whereas Venn-Abers displays fewer instances of extreme degradation and slightly more instances of extreme improvement. Importantly, we find that commonly used calibration procedures, most notably Platt scaling and isotonic regression, can systematically degrade proper scoring performance for strong modern tabular models. Overall classification performance is often preserved, but calibration effects vary substantially across datasets and architectures, and no method dominates uniformly. In expectation, all methods except Pearsonify slightly increase accuracy, but the effect is marginal, with the largest expected gain about 0.008%.
Comments:
61 pages, 23 figures
Subjects:
Machine Learning (cs.LG); Applications (stat.AP); Machine Learning (stat.ML)
MSC classes:
68T05, 62H30, 62F15, 62G05, 68T01
ACM classes:
I.2.6; I.5.1; I.5.2; I.2.10; H.2.8
Cite as:
arXiv:2601.19944 [cs.LG]
(or
arXiv:2601.19944v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.19944
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Daniel Grønhaug [view email]          [v1]
Mon, 19 Jan 2026 18:23:36 UTC (7,577 KB)



## 2601.20439

贡献关闭；日期未核：offlinevalidtool探索+GRPOplanner reward的两阶段工具训练配方，题摘无新的执行/失效条件；PRICAI25原公开线索但排除贡献后不为日期增工作。

https://arxiv.org/abs/2601.20439v1
arXiv:2601.20439v1 (cs)
[Submitted on 28 Jan 2026]
Title:PEARL: Plan Exploration and Adaptive Reinforcement Learning for Multihop Tool Use
Authors:Qihao Wang, Mingzhe Lu, Jiayue Wu, Yue Hu, Yanbing Liu
View a PDF of the paper titled PEARL: Plan Exploration and Adaptive Reinforcement Learning for Multihop Tool Use, by Qihao Wang and 4 other authors
View PDF
HTML (experimental)
Abstract:Large Language Models show great potential with external tools, but face significant challenges in complex, multi-turn tool invocation. They often exhibit weak planning, tool hallucination, erroneous parameter generation, and struggle with robust interaction. To tackle these issues, we present PEARL, a novel framework to enhance LLM planning and execution for sophisticated tool use. PEARL adopts a two-stage approach: an offline phase where the agent explores tools to learn valid usage patterns and failure conditions, and an online reinforcement learning phase. In the online phase, a dedicated Planner is trained via group Relative Policy Optimization (GRPO) with a carefully designed reward function that provides distinct signals for planning quality. Experiments on the ToolHop and T-Eval benchmarks show PEARL significantly outperforms existing methods, achieving a new state-of-the-art success rate of \textbf{56.5\%} on ToolHop while maintaining a low invocation error rate. Our work marks a key advance in addressing the complex planning challenges of tool use, contributing to the development of more robust and reliable LLM-based agents.
Comments:
Accepted to PRICAI25
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2601.20439 [cs.CL]
(or
arXiv:2601.20439v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20439
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Qihao Wang [view email]          [v1]
Wed, 28 Jan 2026 09:49:43 UTC (275 KB)



## 2601.20723

范围关闭：binary coordination games noisy BSC/BEC与Gibbs sampler，非大模型参数训练/状态通信/LLMAgent机制；一般图博弈通信理论非自动主线。

https://arxiv.org/abs/2601.20723v1
arXiv:2601.20723v1 (eess)
[Submitted on 28 Jan 2026]
Title:Distributed Learning over Noisy Communication Networks
Authors:Emrah Akyol, Marcos Vasconcelos
View a PDF of the paper titled Distributed Learning over Noisy Communication Networks, by Emrah Akyol and 1 other authors
View PDF
HTML (experimental)
Abstract:We study binary coordination games over graphs under log-linear learning when neighbor actions are conveyed through explicit noisy communication links. Each edge is modeled as either a binary symmetric channel (BSC) or a binary erasure channel (BEC). We analyze two operational regimes. For binary symmetric and binary erasure channels, we provide a structural characterization of the induced learning dynamics. In a fast-communication regime, agents update using channel-averaged payoffs; the resulting learning dynamics coincide with a Gibbs sampler for a scaled coordination potential, where channel reliability enters only through a scalar attenuation coefficient. In a snapshot regime, agents update from a single noisy realization and ignore channel statistics; the induced Markov chain is generally nonreversible, but admits a high-temperature expansion whose drift matches that of the fast Gibbs sampler with the same attenuation. We further formalize a finite-$K$ communication budget, which interpolates between snapshot and fast behavior as the number of channel uses per update grows. This viewpoint yields a communication-theoretic interpretation in terms of retransmissions and repetition coding, and extends naturally to heterogeneous link reliabilities via effective edge weights. Numerical experiments illustrate the theory and quantify the tradeoff between communication resources and steady-state coordination quality.
Comments:
draft, submitted to IEEE JSAC Special Issue on Distributed Optimization, Learning, and Inference over Communication-Constrained Networks
Subjects:
Systems and Control (eess.SY); Computer Science and Game Theory (cs.GT); Social and Information Networks (cs.SI)
Cite as:
arXiv:2601.20723 [eess.SY]
(or
arXiv:2601.20723v1 [eess.SY] for this version)
https://doi.org/10.48550/arXiv.2601.20723
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Emrah Akyol [view email]          [v1]
Wed, 28 Jan 2026 15:57:53 UTC (491 KB)



## 2601.20774

准入 2+1+3=6：multitask adaptation不可最优不只bounded样本→任意大每任务样本仍impossible若缺distributioninformation→更多数据不补任务关系不可识别性，核risk比较假设。

https://arxiv.org/abs/2601.20774v1
arXiv:2601.20774v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 28 May 2026 (v2)]
Title:When More Data Doesn't Help: Limits of Adaptation in Multitask Learning
Authors:Steve Hanneke, Mingyue Xu
View a PDF of the paper titled When More Data Doesn't Help: Limits of Adaptation in Multitask Learning, by Steve Hanneke and 1 other authors
View PDF
HTML (experimental)
Abstract:Multitask learning and related frameworks have achieved tremendous success in modern applications. In multitask learning problem, we are given a set of heterogeneous datasets collected from related source tasks and hope to enhance the performance above what we could hope to achieve by solving each of them individually. The recent work of arXiv:2006.15785 has showed that, without access to distributional information, no algorithm based on aggregating samples alone can guarantee optimal risk as long as the sample size per task is bounded.
In this paper, we focus on understanding the statistical limits of multitask learning. We go beyond the no-free-lunch theorem in arXiv:2006.15785 by establishing a stronger impossibility result of adaptation that holds for arbitrarily large sample size per task. This improvement conveys an important message that the hardness of multitask learning cannot be overcame by having abundant data per task. We also discuss the notion of optimal adaptivity that may be of future interests.
Subjects:
Machine Learning (cs.LG)
Cite as:
arXiv:2601.20774 [cs.LG]
(or
arXiv:2601.20774v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20774
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Mingyue Xu [view email]          [v1]
Wed, 28 Jan 2026 17:00:11 UTC (59 KB)
[v2]
Thu, 28 May 2026 21:13:54 UTC (60 KB)



## 2601.20738

准入 2+2+2=6：heterogeneousFL EF residual早期慢→SA partialEF二阶残差递推/α调节warmupstability→compressionerror需要阶段条件而非统一EF。

https://arxiv.org/abs/2601.20738v1
arXiv:2601.20738v1 (cs)
[Submitted on 28 Jan 2026]
Title:SA-PEF: Step-Ahead Partial Error Feedback for Efficient Federated Learning
Authors:Dawit Kiros Redie, Reza Arablouei, Stefan Werner
View a PDF of the paper titled SA-PEF: Step-Ahead Partial Error Feedback for Efficient Federated Learning, by Dawit Kiros Redie and 2 other authors
View PDF
HTML (experimental)
Abstract:Biased gradient compression with error feedback (EF) reduces communication in federated learning (FL), but under non-IID data, the residual error can decay slowly, causing gradient mismatch and stalled progress in the early rounds. We propose step-ahead partial error feedback (SA-PEF), which integrates step-ahead (SA) correction with partial error feedback (PEF). SA-PEF recovers EF when the step-ahead coefficient $\alpha=0$ and step-ahead EF (SAEF) when $\alpha=1$. For non-convex objectives and $\delta$-contractive compressors, we establish a second-moment bound and a residual recursion that guarantee convergence to stationarity under heterogeneous data and partial client participation. The resulting rates match standard non-convex Fed-SGD guarantees up to constant factors, achieving $O((\eta,\eta_0TR)^{-1})$ convergence to a variance/heterogeneity floor with a fixed inner step size. Our analysis reveals a step-ahead-controlled residual contraction $\rho_r$ that explains the observed acceleration in the early training phase. To balance SAEF's rapid warm-up with EF's long-term stability, we select $\alpha$ near its theory-predicted optimum. Experiments across diverse architectures and datasets show that SA-PEF consistently reaches target accuracy faster than EF.
Subjects:
Machine Learning (cs.LG); Distributed, Parallel, and Cluster Computing (cs.DC); Signal Processing (eess.SP); Optimization and Control (math.OC); Machine Learning (stat.ML)
Cite as:
arXiv:2601.20738 [cs.LG]
(or
arXiv:2601.20738v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20738
Focus to learn more
arXiv-issued DOI via DataCite
Journal reference:
Transactions on Machine Learning Research, 2026
Submission history From: Dawit Kiros Redie [view email]          [v1]
Wed, 28 Jan 2026 16:10:49 UTC (985 KB)



## 2601.20571

范围关闭：去中心化quantile/median ADMM O(1)node-memory鲁棒统计聚合，是一般distributedestimation未建立foundationmodel梯度/训练system约束；不因distributedlearningtitle全收。

https://arxiv.org/abs/2601.20571v1
arXiv:2601.20571v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 7 May 2026 (v2)]
Title:Robust Distributed Learning under Resource Constraints: Decentralized Quantile Estimation via (Asynchronous) ADMM
Authors:Anna van Elst, Igor Colin, Stephan Clémençon
View a PDF of the paper titled Robust Distributed Learning under Resource Constraints: Decentralized Quantile Estimation via (Asynchronous) ADMM, by Anna van Elst and 2 other authors
View PDF
HTML (experimental)
Abstract:Specifications for decentralized learning on resource-constrained edge devices require algorithms that are communication-efficient, robust to data corruption, and lightweight in memory usage. While state-of-the-art gossip-based methods satisfy the first requirement, achieving robustness remains challenging. Asynchronous decentralized ADMM-based methods have been explored for estimating the median, a statistical centrality measure that is notoriously more robust than the mean. However, existing approaches require memory that scales with node degree, making them impractical when memory is limited. In this paper, we propose AsylADMM, a novel gossip algorithm for decentralized median and quantile estimation, primarily designed for asynchronous updates and requiring only two variables per node. We analyze a synchronous variant of AsylADMM to establish theoretical guarantees and empirically demonstrate fast convergence for the asynchronous algorithm. We then show that our algorithm enables quantile-based trimming, geometric median estimation, and depth-based trimming, with quantile-based trimming empirically outperforming existing rank-based methods. Finally, we provide a novel theoretical analysis of rank-based trimming via Markov chain theory.
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Machine Learning (stat.ML)
Cite as:
arXiv:2601.20571 [cs.LG]
(or
arXiv:2601.20571v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20571
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Anna Van Elst [view email]          [v1]
Wed, 28 Jan 2026 13:09:10 UTC (1,735 KB)
[v2]
Thu, 7 May 2026 15:40:35 UTC (1,895 KB)



## 2601.20041

准入 2+2+2=6：edgeCiM噪声损检索precision→noiseawaretaskprojection TONEL→低数据移动不保证embedding检索正确，需硬件noise模型与domainshift绑定。

https://arxiv.org/abs/2601.20041v1
arXiv:2601.20041v1 (cs)
[Submitted on 27 Jan 2026 (this version), latest version 3 Feb 2026 (v3)]
Title:CiMRAG: Cim-Aware Domain-Adaptive and Noise-Resilient Retrieval-Augmented Generation for Edge-Based LLMs
Authors:Shih-Hsuan Chiu, Ming-Syan Chen
View a PDF of the paper titled CiMRAG: Cim-Aware Domain-Adaptive and Noise-Resilient Retrieval-Augmented Generation for Edge-Based LLMs, by Shih-Hsuan Chiu and 1 other authors
View PDF
HTML (experimental)
Abstract:Personalized virtual assistants powered by large language models (LLMs) on edge devices are attracting growing attention, with Retrieval-Augmented Generation (RAG) emerging as a key method for personalization by retrieving relevant profile data and generating tailored responses. However, deploying RAG on edge devices faces efficiency hurdles due to the rapid growth of profile data, such as user-LLM interactions and recent updates. While Computing-in-Memory (CiM) architectures mitigate this bottleneck by eliminating data movement between memory and processing units via in-situ operations, they are susceptible to environmental noise that can degrade retrieval precision. This poses a critical issue in dynamic, multi-domain edge-based scenarios (e.g., travel, medicine, and law) where both accuracy and adaptability are paramount. To address these challenges, we propose Task-Oriented Noise-resilient Embedding Learning (TONEL), a framework that improves noise robustness and domain adaptability for RAG in noisy edge environments. TONEL employs a noise-aware projection model to learn task-specific embeddings compatible with CiM hardware constraints, enabling accurate retrieval under noisy conditions. Extensive experiments conducted on personalization benchmarks demonstrate the effectiveness and practicality of our methods relative to strong baselines, especially in task-specific noisy scenarios.
Comments:
Accepted by ICASSP 2026
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20041 [cs.LG]
(or
arXiv:2601.20041v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20041
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Shih-Hsuan Chiu [view email]          [v1]
Tue, 27 Jan 2026 20:30:59 UTC (1,424 KB)
[v2]
Fri, 30 Jan 2026 10:00:53 UTC (1,424 KB)
[v3]
Tue, 3 Feb 2026 10:43:01 UTC (1,424 KB)



## 2601.19952

贡献符合；DATE待定：streaming固定chunk/投机破semantic与rollback→semantictrigger+backgroundthinkerforegroundspeaker双流→thinking启动和incrementalreasonstate解耦；Submitted早待date。

https://arxiv.org/abs/2601.19952v1
arXiv:2601.19952v1 (cs)
[Submitted on 26 Jan 2026]
Title:LTS-VoiceAgent: A Listen-Think-Speak Framework for Efficient Streaming Voice Interaction via Semantic Triggering and Incremental Reasoning
Authors:Wenhao Zou, Yuwei Miao, Zhanyu Ma, Jun Xu, Jiuchong Gao, Jinghua Hao, Renqing He, Jingwen Xu
View a PDF of the paper titled LTS-VoiceAgent: A Listen-Think-Speak Framework for Efficient Streaming Voice Interaction via Semantic Triggering and Incremental Reasoning, by Wenhao Zou and 7 other authors
View PDF
HTML (experimental)
Abstract:Real-time voice agents face a dilemma: end-to-end models often lack deep reasoning, while cascaded pipelines incur high latency by executing ASR, LLM reasoning, and TTS strictly in sequence, unlike human conversation where listeners often start thinking before the speaker finishes. Since cascaded architectures remain the dominant choice for complex tasks, existing cascaded streaming strategies attempt to reduce this latency via mechanical segmentation (e.g., fixed chunks, VAD-based splitting) or speculative generation, but they frequently either break semantic units or waste computation on predictions that must be rolled back. To address these challenges, we propose LTS-VoiceAgent, a Listen-Think-Speak framework that explicitly separates when to think from how to reason incrementally. It features a Dynamic Semantic Trigger to detect meaningful prefixes, and a Dual-Role Stream Orchestrator that coordinates a background Thinker (for state maintenance) and a foreground Speaker (for speculative solving). This parallel design enables "thinking while speaking" without blocking responses. We also introduce a Pause-and-Repair benchmark containing natural disfluencies to stress-test streaming robustness. Experiments across VERA, Spoken-MQA, BigBenchAudio, and our benchmark show that LTS-VoiceAgent achieves a stronger accuracy-latency-efficiency trade-off than serial cascaded baselines and existing streaming strategies.
Subjects:
Sound (cs.SD); Artificial Intelligence (cs.AI); Audio and Speech Processing (eess.AS)
Cite as:
arXiv:2601.19952 [cs.SD]
(or
arXiv:2601.19952v1 [cs.SD] for this version)
https://doi.org/10.48550/arXiv.2601.19952
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Wenhao Zou [view email]          [v1]
Mon, 26 Jan 2026 15:42:35 UTC (4,009 KB)



## 2601.19935

贡献符合；DATE待定：passivememoryfactrecall不等参数grounded工具行动→400memorydependenttools任务→memoryevaluation需actiongrounding；Submitted早待date。

https://arxiv.org/abs/2601.19935v1
arXiv:2601.19935v1 (cs)
[Submitted on 13 Jan 2026]
Title:Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents
Authors:Yiting Shen, Kun Li, Wei Zhou, Songlin Hu
View a PDF of the paper titled Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents, by Yiting Shen and 3 other authors
View PDF
HTML (experimental)
Abstract:Large Language Model (LLM)-based agents are increasingly deployed for complex, tool-based tasks where long-term memory is critical to driving actions. Existing benchmarks, however, primarily test a angent's ability to passively retrieve isolated facts in response to explicit questions. They fail to evaluate the more crucial capability of actively applying memory to execute tasks. To address this gap, we introduce \textsc{Mem2ActBench}, a benchmark for evaluating whether agents can proactively leverage long-term memory to execute tool-based actions by selecting appropriate tools and grounding their parameters. The benchmark simulates persistent assistant usage, where users mention the same topic across long, interrupted interactions and expect previously established preferences and task states to be implicitly applied. We build the dataset with an automated pipeline that merges heterogeneous sources (ToolACE, BFCL, Oasst1), resolves conflicts via consistency modeling, and synthesizes 2,029 sessions with 12 user--assistant--tool turns on average. From these memory chains, a reverse-generation method produces 400 tool-use tasks, with human evaluation confirming 91.3\% are strongly memory-dependent. Experiments on seven memory frameworks show that current systems remain inadequate at actively utilizing memory for parameter grounding, highlighting the need for more effective approaches to evaluate and improve memory application in task execution.
Subjects:
Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.19935 [cs.CL]
(or
arXiv:2601.19935v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.19935
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yiting Shen [view email]          [v1]
Tue, 13 Jan 2026 06:22:32 UTC (1,766 KB)


