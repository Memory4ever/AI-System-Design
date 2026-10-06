# 2026-01-30 第三批完整题摘准入（作者初判）

最终修正：root实际28完整题摘与必要core通过；FPL20224的59–89只是CLIP classprototype ridge+blend且无新有效条件，EX；SwitchCodec20362官方撤回不评分/入选/Books。19912/19904各最小决定结果已读，局部SDC/DUE、scale/task与SN30跨机TP反侧潜在贡献成立，early Submitted日期继续隔离，不扩正文；19960/19942/19908同DATE隔离。9确认落窗项必要Evidence与Only边界已独立核，以下初判不覆盖最终README。

原始题摘与判据；先贡献后日期、评分。宽标题线索非逐项全文队列。

## 2601.20856

准入 2+2+2=6：保留状态的混杂被简化后仍出现长规划退化，PDDL辅助仅有限改善→需区别状态持久性、规划长度与可执行验证，不采用25步普遍架构上限。

https://arxiv.org/abs/2601.20856v1
arXiv:2601.20856v1 (cs)
[Submitted on 28 Jan 2026]
Title:SokoBench: Evaluating Long-Horizon Planning and Reasoning in Large Language Models
Authors:Sebastiano Monti, Carlo Nicolini, Gianni Pellegrini, Jacopo Staiano, Bruno Lepri
View a PDF of the paper titled SokoBench: Evaluating Long-Horizon Planning and Reasoning in Large Language Models, by Sebastiano Monti and 4 other authors
View PDF
HTML (experimental)
Abstract:Although the capabilities of large language models have been increasingly tested on complex reasoning tasks, their long-horizon planning abilities have not yet been extensively investigated. In this work, we provide a systematic assessment of the planning and long-horizon reasoning capabilities of state-of-the-art Large Reasoning Models (LRMs). We propose a novel benchmark based on Sokoban puzzles, intentionally simplified to isolate long-horizon planning from state persistence. Our findings reveal a consistent degradation in planning performance when more than 25 moves are required to reach the solution, suggesting a fundamental constraint on forward planning capacity. We show that equipping LRMs with Planning Domain Definition Language (PDDL) parsing, validation, and solving tools allows for modest improvements, suggesting inherent architectural limitations which might not be overcome by test-time scaling approaches alone.
Subjects:
Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20856 [cs.AI]
(or
arXiv:2601.20856v1 [cs.AI] for this version)
https://doi.org/10.48550/arXiv.2601.20856
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Carlo Nicolini [view email]          [v1]
Wed, 28 Jan 2026 18:56:00 UTC (733 KB)



## 2601.20727

贡献关闭：append-only审计、emitters、审批provenance成熟机制的框架和开源实现，未新增事件完备性/防篡改/跨组织信任边界。

https://arxiv.org/abs/2601.20727v1
arXiv:2601.20727v1 (cs)
[Submitted on 28 Jan 2026]
Title:Audit Trails for Accountability in Large Language Models
Authors:Victor Ojewale, Harini Suresh, Suresh Venkatasubramanian
View a PDF of the paper titled Audit Trails for Accountability in Large Language Models, by Victor Ojewale and 2 other authors
View PDF
HTML (experimental)
Abstract:Large language models (LLMs) are increasingly embedded in consequential decisions across healthcare, finance, employment, and public services. Yet accountability remains fragile because process transparency is rarely recorded in a durable and reviewable form. We propose LLM audit trails as a sociotechnical mechanism for continuous accountability. An audit trail is a chronological, tamper-evident, context-rich ledger of lifecycle events and decisions that links technical provenance (models, data, training and evaluation runs, deployments, monitoring) with governance records (approvals, waivers, and attestations), so organizations can reconstruct what changed, when, and who authorized it.
This paper contributes: (1) a lifecycle framework that specifies event types, required metadata, and governance rationales; (2) a reference architecture with lightweight emitters, append only audit stores, and an auditor interface supporting cross organizational traceability; and (3) a reusable, open-source Python implementation that instantiates this audit layer in LLM workflows with minimal integration effort. We conclude by discussing limitations and directions for adoption.
Subjects:
Computers and Society (cs.CY)
Cite as:
arXiv:2601.20727 [cs.CY]
(or
arXiv:2601.20727v1 [cs.CY] for this version)
https://doi.org/10.48550/arXiv.2601.20727
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Victor Ojewale [view email]          [v1]
Wed, 28 Jan 2026 16:04:33 UTC (810 KB)



## 2601.20676

贡献关闭：训练Agent判断各mRAG步骤必要性是现成自适应工具选择配方；题摘未给新的可归因调度机制或可迁移质量/成本失效边界。

https://arxiv.org/abs/2601.20676v1
arXiv:2601.20676v1 (cs)
[Submitted on 28 Jan 2026]
Title:Efficient Multimodal Planning Agent for Visual Question-Answering
Authors:Zhuo Chen, Xinyu Geng, Xinyu Wang, Yong Jiang, Zhen Zhang, Pengjun Xie, Kewei Tu
View a PDF of the paper titled Efficient Multimodal Planning Agent for Visual Question-Answering, by Zhuo Chen and 6 other authors
View PDF
HTML (experimental)
Abstract:Visual Question-Answering (VQA) is a challenging multimodal task that requires integrating visual and textual information to generate accurate responses. While multimodal Retrieval-Augmented Generation (mRAG) has shown promise in enhancing VQA systems by providing more evidence on both image and text sides, the default procedure that addresses VQA queries, especially the knowledge-intensive ones, often relies on multi-stage pipelines of mRAG with inherent dependencies. To mitigate the inefficiency limitations while maintaining VQA task performance, this paper proposes a method that trains a multimodal planning agent, dynamically decomposing the mRAG pipeline to solve the VQA task. Our method optimizes the trade-off between efficiency and effectiveness by training the agent to intelligently determine the necessity of each mRAG step. In our experiments, the agent can help reduce redundant computations, cutting search time by over 60\% compared to existing methods and decreasing costly tool calls. Meanwhile, experiments demonstrate that our method outperforms all baselines, including a Deep Research agent and a carefully designed prompt-based method, on average over six various datasets. Code will be released.
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2601.20676 [cs.CL]
(or
arXiv:2601.20676v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20676
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Zhuo Chen [view email]          [v1]
Wed, 28 Jan 2026 14:58:59 UTC (2,596 KB)



## 2601.20659

贡献关闭：self-dialogue+oracleRAG的多步反思流程；未新增纠错有效性条件或改变部署判断的对照边界。

https://arxiv.org/abs/2601.20659v1
arXiv:2601.20659v1 (cs)
[Submitted on 28 Jan 2026]
Title:A Dialectic Pipeline for Improving LLM Robustness
Authors:Sara Candussio
View a PDF of the paper titled A Dialectic Pipeline for Improving LLM Robustness, by Sara Candussio
View PDF
HTML (experimental)
Abstract:Assessing ways in which Language Models can reduce their hallucinations and improve the outputs' quality is crucial to ensure their large-scale use.
However, methods such as fine-tuning on domain-specific data or the training of a separate \textit{ad hoc} verifier require demanding computational resources (not feasible for many user applications) and constrain the models to specific fields of knowledge.
In this thesis, we propose a dialectic pipeline that preserves LLMs' generalization abilities while improving the quality of its answer via self-dialogue, enabling it to reflect upon and correct tentative wrong answers.
We experimented with different pipeline settings, testing our proposed method on different datasets and on different families of models. All the pipeline stages are enriched with the relevant context (in an oracle-RAG setting) and a study on the impact of its summarization or its filtering is conducted.
We find that our proposed dialectic pipeline is able to outperform by significative margins the standard model answers and that it consistently achieves higher performances than Chain-of-Thought only prompting.
Subjects:
Computation and Language (cs.CL); Multiagent Systems (cs.MA)
Cite as:
arXiv:2601.20659 [cs.CL]
(or
arXiv:2601.20659v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20659
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Sara Candussio [view email]          [v1]
Wed, 28 Jan 2026 14:42:49 UTC (8,915 KB)



## 2601.20641

准入 2+2+2=6；安全强制深入：受控referential game中任务适配协议可能更难被人/外部模型解释且相近模型无显式共享协议可协调→输出自然语言可读性不等于协作透明性；限定受控任务。

https://arxiv.org/abs/2601.20641v1
arXiv:2601.20641v1 (cs)
[Submitted on 28 Jan 2026]
Title:Investigating the Development of Task-Oriented Communication in Vision-Language Models
Authors:Boaz Carmeli, Orr Paradise, Shafi Goldwasser, Yonatan Belinkov, Ron Meir
View a PDF of the paper titled Investigating the Development of Task-Oriented Communication in Vision-Language Models, by Boaz Carmeli and 4 other authors
View PDF
HTML (experimental)
Abstract:We investigate whether \emph{LLM-based agents} can develop task-oriented communication protocols that differ from standard natural language in collaborative reasoning tasks. Our focus is on two core properties such task-oriented protocols may exhibit: Efficiency -- conveying task-relevant information more concisely than natural language, and Covertness -- becoming difficult for external observers to interpret, raising concerns about transparency and control. To investigate these aspects, we use a referential-game framework in which vision-language model (VLM) agents communicate, providing a controlled, measurable setting for evaluating language variants. Experiments show that VLMs can develop effective, task-adapted communication patterns. At the same time, they can develop covert protocols that are difficult for humans and external agents to interpret. We also observe spontaneous coordination between similar models without explicitly shared protocols. These findings highlight both the potential and the risks of task-oriented communication, and position referential games as a valuable testbed for future work in this area.
Subjects:
Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20641 [cs.AI]
(or
arXiv:2601.20641v1 [cs.AI] for this version)
https://doi.org/10.48550/arXiv.2601.20641
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Boaz Carmeli [view email]          [v1]
Wed, 28 Jan 2026 14:28:31 UTC (1,830 KB)



## 2601.20617

贡献关闭：公共行政要求的文献归纳与benchmark覆盖审计；未新增主线Agent执行机制或具体跨域可靠性失效证据，不由法律要求映射owner准入。

https://arxiv.org/abs/2601.20617v1
arXiv:2601.20617v1 (cs)
[Submitted on 28 Jan 2026]
Title:Agent Benchmarks Fail Public Sector Requirements
Authors:Jonathan Rystrøm, Chris Schmitz, Karolina Korgul, Jan Batzner, Chris Russell
View a PDF of the paper titled Agent Benchmarks Fail Public Sector Requirements, by Jonathan Rystr{\o}m and 3 other authors
View PDF
HTML (experimental)
Abstract:Deploying Large Language Model-based agents (LLM agents) in the public sector requires assuring that they meet the stringent legal, procedural, and structural requirements of public-sector institutions. Practitioners and researchers often turn to benchmarks for such assessments. However, it remains unclear what criteria benchmarks must meet to ensure they adequately reflect public-sector requirements, or how many existing benchmarks do so. In this paper, we first define such criteria based on a first-principles survey of public administration literature: benchmarks must be \emph{process-based}, \emph{realistic}, \emph{public-sector-specific} and report \emph{metrics} that reflect the unique requirements of the public sector. We analyse more than 1,300 benchmark papers for these criteria using an expert-validated LLM-assisted pipeline. Our results show that no single benchmark meets all of the criteria. Our findings provide a call to action for both researchers to develop public sector-relevant benchmarks and for public-sector officials to apply these criteria when evaluating their own agentic use cases.
Comments:
Forthcoming @ IASEAI 2026
Subjects:
Computers and Society (cs.CY); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20617 [cs.CY]
(or
arXiv:2601.20617v1 [cs.CY] for this version)
https://doi.org/10.48550/arXiv.2601.20617
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Jonathan Rystrøm [view email]          [v1]
Wed, 28 Jan 2026 13:51:30 UTC (464 KB)



## 2601.20546

准入 2+1+2=5：DAT仅新颖性可被无创造能力基线超过→条件适切性的CDAT拆开噪声与创造力→不能把无约束距离分数当创造能力。

https://arxiv.org/abs/2601.20546v1
arXiv:2601.20546v1 (cs)
[Submitted on 28 Jan 2026]
Title:Beyond Divergent Creativity: A Human-Based Evaluation of Creativity in Large Language Models
Authors:Kumiko Nakajima, Jan Zuiderveld, Sandro Pezzelle
View a PDF of the paper titled Beyond Divergent Creativity: A Human-Based Evaluation of Creativity in Large Language Models, by Kumiko Nakajima and 2 other authors
View PDF
HTML (experimental)
Abstract:Large language models (LLMs) are increasingly used in verbal creative tasks. However, previous assessments of the creative capabilities of LLMs remain weakly grounded in human creativity theory and are thus hard to interpret. The widely used Divergent Association Task (DAT) focuses on novelty, ignoring appropriateness, a core component of creativity. We evaluate a range of state-of-the-art LLMs on DAT and show that their scores on the task are lower than those of two baselines that do not possess any creative abilities, undermining its validity for model evaluation. Grounded in human creativity theory, which defines creativity as the combination of novelty and appropriateness, we introduce Conditional Divergent Association Task (CDAT). CDAT evaluates novelty conditional on contextual appropriateness, separating noise from creativity better than DAT, while remaining simple and objective. Under CDAT, smaller model families often show the most creativity, whereas advanced families favor appropriateness at lower novelty. We hypothesize that training and alignment likely shift models along this frontier, making outputs more appropriate but less creative. We release the dataset and code.
Comments:
Accepted to Findings of EACL 2026
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2601.20546 [cs.CL]
(or
arXiv:2601.20546v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20546
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Kumiko Nakajima [view email]          [v1]
Wed, 28 Jan 2026 12:41:32 UTC (5,779 KB)



## 2601.20465

贡献关闭：时间线、episodic/semantic/salience/control分库及融合检索均为现成memory组织；局部LoCoMo数字和脑类比不提供新的更新可靠性或选择条件。

https://arxiv.org/abs/2601.20465v1
arXiv:2601.20465v1 (cs)
[Submitted on 28 Jan 2026]
Title:BMAM: Brain-inspired Multi-Agent Memory Framework
Authors:Yang Li, Jiaxiang Liu, Yusong Wang, Yujie Wu, Mingkun Xu
View a PDF of the paper titled BMAM: Brain-inspired Multi-Agent Memory Framework, by Yang Li and 4 other authors
View PDF
HTML (experimental)
Abstract:Language-model-based agents operating over extended interaction horizons face persistent challenges in preserving temporally grounded information and maintaining behavioral consistency across sessions, a failure mode we term soul erosion. We present BMAM (Brain-inspired Multi-Agent Memory), a general-purpose memory architecture that models agent memory as a set of functionally specialized subsystems rather than a single unstructured store. Inspired by cognitive memory systems, BMAM decomposes memory into episodic, semantic, salience-aware, and control-oriented components that operate at complementary time scales. To support long-horizon reasoning, BMAM organizes episodic memories along explicit timelines and retrieves evidence by fusing multiple complementary signals. Experiments on the LoCoMo benchmark show that BMAM achieves 78.45 percent accuracy under the standard long-horizon evaluation setting, and ablation analyses confirm that the hippocampus-inspired episodic memory subsystem plays a critical role in temporal reasoning.
Comments:
Submitted to ACL (ARR 2026 January submission); non-anonymous preprint
Subjects:
Computation and Language (cs.CL)
MSC classes:
68T50, 68T05
ACM classes:
I.2.7; I.2.4; H.3.3
Cite as:
arXiv:2601.20465 [cs.CL]
(or
arXiv:2601.20465v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20465
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yang Li [view email]          [v1]
Wed, 28 Jan 2026 10:36:03 UTC (11,268 KB)



## 2601.20419

贡献关闭：IoU图块去重+cos描述去重是输入冗余过滤组合，六数据集准确率未显示新增跨模态表示/校准条件。

https://arxiv.org/abs/2601.20419v1
arXiv:2601.20419v1 (cs)
[Submitted on 28 Jan 2026]
Title:Let's Roll a BiFTA: Bi-refinement for Fine-grained Text-visual Alignment in Vision-Language Models
Authors:Yuhao Sun, Chengyi Cai, Jiacheng Zhang, Zesheng Ye, Xingliang Yuan, Feng Liu
View a PDF of the paper titled Let's Roll a BiFTA: Bi-refinement for Fine-grained Text-visual Alignment in Vision-Language Models, by Yuhao Sun and 5 other authors
View PDF
HTML (experimental)
Abstract:Recent research has shown that aligning fine-grained text descriptions with localized image patches can significantly improve the zero-shot performance of pre-trained vision-language models (e.g., CLIP). However, we find that both fine-grained text descriptions and localized image patches often contain redundant information, making text-visual alignment less effective. In this paper, we tackle this issue from two perspectives: \emph{View Refinement} and \emph{Description refinement}, termed as \textit{\textbf{Bi}-refinement for \textbf{F}ine-grained \textbf{T}ext-visual \textbf{A}lignment} (BiFTA). \emph{View refinement} removes redundant image patches with high \emph{Intersection over Union} (IoU) ratios, resulting in more distinctive visual samples. \emph{Description refinement} removes redundant text descriptions with high pairwise cosine similarity, ensuring greater diversity in the remaining descriptions. BiFTA achieves superior zero-shot performance on 6 benchmark datasets for both ViT-based and ResNet-based CLIP, justifying the necessity to remove redundant information in visual-text alignment.
Comments:
25 pages
Subjects:
Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20419 [cs.CV]
(or
arXiv:2601.20419v1 [cs.CV] for this version)
https://doi.org/10.48550/arXiv.2601.20419
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yuhao Sun [view email]          [v1]
Wed, 28 Jan 2026 09:24:14 UTC (745 KB)



## 2601.20380

贡献关闭：bottom-up探索/top-down分类数据合成+SFT→GRPO+MoE GUI配方；局部offline step score不改变动作提交、状态或部署可靠性判断。

https://arxiv.org/abs/2601.20380v1
arXiv:2601.20380v1 (cs)
[Submitted on 28 Jan 2026]
Title:OmegaUse: Building a General-Purpose GUI Agent for Autonomous Task Execution
Authors:Le Zhang, Yixiong Xiao, Xinjiang Lu, Jingjia Cao, Yusai Zhao, Jingbo Zhou, Lang An, Zikan Feng, Wanxiang Sha, Yu Shi, Congxi Xiao, Jian Xiong, Yankai Zhang, Hua Wu, Haifeng Wang
View a PDF of the paper titled OmegaUse: Building a General-Purpose GUI Agent for Autonomous Task Execution, by Le Zhang and 14 other authors
View PDF
HTML (experimental)
Abstract:Graphical User Interface (GUI) agents show great potential for enabling foundation models to complete real-world tasks, revolutionizing human-computer interaction and improving human productivity. In this report, we present OmegaUse, a general-purpose GUI agent model for autonomous task execution on both mobile and desktop platforms, supporting computer-use and phone-use scenarios. Building an effective GUI agent model relies on two factors: (1) high-quality data and (2) effective training methods. To address these, we introduce a carefully engineered data-construction pipeline and a decoupled training paradigm. For data construction, we leverage rigorously curated open-source datasets and introduce a novel automated synthesis framework that integrates bottom-up autonomous exploration with top-down taxonomy-guided generation to create high-fidelity synthetic data. For training, to better leverage these data, we adopt a two-stage strategy: Supervised Fine-Tuning (SFT) to establish fundamental interaction syntax, followed by Group Relative Policy Optimization (GRPO) to improve spatial grounding and sequential planning. To balance computational efficiency with agentic reasoning capacity, OmegaUse is built on a Mixture-of-Experts (MoE) backbone. To evaluate cross-terminal capabilities in an offline setting, we introduce OS-Nav, a benchmark suite spanning multiple operating systems: ChiM-Nav, targeting Chinese Android mobile environments, and Ubu-Nav, focusing on routine desktop interactions on Ubuntu. Extensive experiments show that OmegaUse is highly competitive across established GUI benchmarks, achieving a state-of-the-art (SOTA) score of 96.3% on ScreenSpot-V2 and a leading 79.1% step success rate on AndroidControl. OmegaUse also performs strongly on OS-Nav, reaching 74.24% step success on ChiM-Nav and 55.9% average success on Ubu-Nav.
Subjects:
Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20380 [cs.AI]
(or
arXiv:2601.20380v1 [cs.AI] for this version)
https://doi.org/10.48550/arXiv.2601.20380
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Jingbo Zhou [view email]          [v1]
Wed, 28 Jan 2026 08:45:17 UTC (660 KB)



## 2601.20224

准入 2+1+2=5：CLIP有限标签适配中以原型→query特征重构误差替代相似度分类，若可归因改变局部参数/训练预算选择；不将性能宣传当理论。

https://arxiv.org/abs/2601.20224v1
arXiv:2601.20224v1 (cs)
[Submitted on 28 Jan 2026]
Title:Feature Projection Learning for Better Vision-Language Reasoning
Authors:Yi Zhang, Weicheng Lin, Liang-Jie Zhang
View a PDF of the paper titled Feature Projection Learning for Better Vision-Language Reasoning, by Yi Zhang and 2 other authors
View PDF
HTML (experimental)
Abstract:Vision-Language Pre-Trained models, notably CLIP, that utilize contrastive learning have proven highly adept at extracting generalizable visual features. To inherit the well-learned knowledge of VLP models for downstream tasks, several approaches aim to adapt them efficiently with limited supervision. However, these methods either suffer from limited performance, excessive learnable parameters, or extended training times, all of which hinder their effectiveness in adapting the CLIP model to downstream tasks. In this work, we propose a simple yet efficient and effective method called \textit{\textbf{F}eature \textbf{P}rojection \textbf{L}earning(FPL)} to address these problems. Specifically, we develop a projection model that projects class prototype features into the query image feature space and reconstructs the query image feature map. The negative average squared reconstruction error is used as the class score. In this way, we transform the classification problem into a feature projection problem. The final output of this method is a combination of the prediction from the projection model and the original pre-trained CLIP. Comprehensive empirical evaluations confirm that FPL delivers superior accuracy, surpassing the current state-of-the-art methods by a substantial margin.
Comments:
Accepted to ICASSP 2026
Subjects:
Computer Vision and Pattern Recognition (cs.CV)
Cite as:
arXiv:2601.20224 [cs.CV]
(or
arXiv:2601.20224v1 [cs.CV] for this version)
https://doi.org/10.48550/arXiv.2601.20224
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Weicheng Lin [view email]          [v1]
Wed, 28 Jan 2026 03:54:36 UTC (2,992 KB)



## 2601.20171

贡献关闭：文档PR数量与后续少修改只说明review实践，未测实际语义错误或新增可操作质量边界。

https://arxiv.org/abs/2601.20171v1
arXiv:2601.20171v1 (cs)
[Submitted on 28 Jan 2026]
Title:Who Writes the Docs in SE 3.0? Agent vs. Human Documentation Pull Requests
Authors:Kazuma Yamasaki, Joseph Ayobami Joshua, Tasha Settewong, Mahmoud Alfadel, Kazumasa Shimari, Kenichi Matsumoto
View a PDF of the paper titled Who Writes the Docs in SE 3.0? Agent vs. Human Documentation Pull Requests, by Kazuma Yamasaki and 5 other authors
View PDF
HTML (experimental)
Abstract:As software engineering moves toward SE3.0, AI agents are increasingly used to carry out development tasks and contribute changes to software projects. It is therefore important to understand the extent of these contributions and how human developers review and intervene, since these factors shape the risks of delegating work to AI agents. While recent studies have examined how AI agents support software development tasks (e.g., code generation, issue resolution, and PR automation), their role in documentation tasks remains underexplored-even though documentation is widely consumed and shapes how developers understand and use software.
Using the AIDev, we analyze 1,997 documentation-related pull requests (PRs) authored by AI agents and human developers, where documentation PRs are those that create or modify project documentation artifacts. We find that AI agents submit substantially more documentation-related PRs than humans in the studied repositories. We further observe that agent-authored documentation edits are typically integrated with little follow-up modification from humans, raising concerns about review practices and the reliability of agent-generated documentation. Overall, while AI agents already contribute substantially to documentation workflows, our results suggest concerns for emerging challenges for documentation quality assurance and human-AI collaboration in SE3.0.
Comments:
Comments: 5 pages, 5 figures. To appear in MSR 2026 Mining Challenge (April 2026). Code available at this https URL
Subjects:
Software Engineering (cs.SE)
ACM classes:
D.2.7; D.2.13; I.2.11
Cite as:
arXiv:2601.20171 [cs.SE]
(or
arXiv:2601.20171v1 [cs.SE] for this version)
https://doi.org/10.48550/arXiv.2601.20171
Focus to learn more
arXiv-issued DOI via DataCite
Related DOI:
https://doi.org/10.1145/3793302.3793612
Focus to learn more
DOI(s) linking to related resources
Submission history From: Kazuma Yamasaki [view email]          [v1]
Wed, 28 Jan 2026 02:11:34 UTC (106 KB)



## 2601.20162

贡献关闭：personal reward+长期/app层次偏好记忆用于移动指令个性化组合；缺少新偏好冲突/可靠性/更新边界。

https://arxiv.org/abs/2601.20162v1
arXiv:2601.20162v1 (cs)
[Submitted on 28 Jan 2026]
Title:Me-Agent: A Personalized Mobile Agent with Two-Level User Habit Learning for Enhanced Interaction
Authors:Shuoxin Wang, Chang Liu, Gowen Loo, Lifan Zheng, Kaiwen Wei, Xinyi Zeng, Jingyuan Zhang, Yu Tian
View a PDF of the paper titled Me-Agent: A Personalized Mobile Agent with Two-Level User Habit Learning for Enhanced Interaction, by Shuoxin Wang and 7 other authors
View PDF
HTML (experimental)
Abstract:Large Language Model (LLM)-based mobile agents have made significant performance advancements. However, these agents often follow explicit user instructions while overlooking personalized needs, leading to significant limitations for real users, particularly without personalized context: (1) inability to interpret ambiguous instructions, (2) lack of learning from user interaction history, and (3) failure to handle personalized instructions. To alleviate the above challenges, we propose Me-Agent, a learnable and memorable personalized mobile agent. Specifically, Me-Agent incorporates a two-level user habit learning approach. At the prompt level, we design a user preference learning strategy enhanced with a Personal Reward Model to improve personalization performance. At the memory level, we design a Hierarchical Preference Memory, which stores users' long-term memory and app-specific memory in different level memory. To validate the personalization capabilities of mobile agents, we introduce User FingerTip, a new benchmark featuring numerous ambiguous instructions for daily life. Extensive experiments on User FingerTip and general benchmarks demonstrate that Me-Agent achieves state-of-the-art performance in personalization while maintaining competitive instruction execution performance.
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2601.20162 [cs.CL]
(or
arXiv:2601.20162v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20162
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yu Tian [view email]          [v1]
Wed, 28 Jan 2026 01:44:19 UTC (32,065 KB)



## 2601.20126

准入 2+1+2=5：可验证三值abstention reward在选择题和开放题呈不同探索约束→不把奖励拒答的局部正确率/覆盖折衷当通用幻觉修复。

https://arxiv.org/abs/2601.20126v1
arXiv:2601.20126v1 (cs)
[Submitted on 27 Jan 2026]
Title:Rewarding Intellectual Humility Learning When Not To Answer In Large Language Models
Authors:Abha Jha, Akanksha Mahajan, Ashwath Vaithinathan Aravindan, Praveen Saravanan, Sai Sailaja Policharla, Sonal Chaturbhuj Gehlot
View a PDF of the paper titled Rewarding Intellectual Humility Learning When Not To Answer In Large Language Models, by Abha Jha and 5 other authors
View PDF
HTML (experimental)
Abstract:Large Language Models (LLMs) often produce hallucinated or unverifiable content, undermining their reliability in factual domains. This work investigates Reinforcement Learning with Verifiable Rewards (RLVR) as a training paradigm that explicitly rewards abstention ("I don't know") alongside correctness to promote intellectual humility. We fine-tune and evaluate Granite-3.3-2B-Instruct and Qwen-3-4B-Instruct on the MedMCQA and Hendrycks Math benchmarks using a ternary reward structure ($-1$, r_abs, 1) under varying abstention reward structures. We further study the effect of combining RLVR with supervised fine-tuning strategies that teach abstention prior to reinforcement learning. Our results show that moderate abstention rewards (r_abs $\approx -0.25$ to 0.3) consistently reduce incorrect responses without severe accuracy degradation on multiple-choice tasks, with larger models exhibiting greater robustness to abstention incentives. On open-ended question answering, we observe limitations due to insufficient exploration, which can be partially mitigated through supervised abstention training. Overall, these findings demonstrate the feasibility and flexibility of verifiable reward design as a practical approach for hallucination mitigation in language models. Reproducible code for our abstention training framework is available here this https URL.
Subjects:
Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
Cite as:
arXiv:2601.20126 [cs.CL]
(or
arXiv:2601.20126v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20126
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Akanksha Mahajan [view email]          [v1]
Tue, 27 Jan 2026 23:42:07 UTC (103 KB)



## 2601.20109

准入 2+1+2=5：agent原始postmergeissue排名经代码churn归一化消失→merge success不是代码质量且比较需控制改动量；局部SonarQube不等实际漏洞。

https://arxiv.org/abs/2601.20109v1
arXiv:2601.20109v1 (cs)
[Submitted on 27 Jan 2026]
Title:Beyond Bug Fixes: An Empirical Investigation of Post-Merge Code Quality Issues in Agent-Generated Pull Requests
Authors:Shamse Tasnim Cynthia, Al Muttakin, Banani Roy
View a PDF of the paper titled Beyond Bug Fixes: An Empirical Investigation of Post-Merge Code Quality Issues in Agent-Generated Pull Requests, by Shamse Tasnim Cynthia and 1 other authors
View PDF
HTML (experimental)
Abstract:The increasing adoption of AI coding agents has increased the number of agent-generated pull requests (PRs) merged with little or no human intervention. Although such PRs promise productivity gains, their post-merge code quality remains underexplored, as prior work has largely relied on benchmarks and controlled tasks rather than large-scale post-merge analyses. To address this gap, we analyze 1,210 merged agent-generated bug-fix PRs from Python repositories in the AIDev dataset. Using SonarQube, we perform a differential analysis between base and merged commits to identify code quality issues newly introduced by PR changes. We examine issue frequency, density, severity, and rule-level prevalence across five agents. Our results show that apparent differences in raw issue counts across agents largely disappear after normalizing by code churn, indicating that higher issue counts are primarily driven by larger PRs. Across all agents, code smells dominate, particularly at critical and major severities, while bugs are less frequent but often severe. Overall, our findings show that merge success does not reliably reflect post-merge code quality, highlighting the need for systematic quality checks for agent-generated bug-fix PRs.
Subjects:
Software Engineering (cs.SE)
Cite as:
arXiv:2601.20109 [cs.SE]
(or
arXiv:2601.20109v1 [cs.SE] for this version)
https://doi.org/10.48550/arXiv.2601.20109
Focus to learn more
arXiv-issued DOI via DataCite
Related DOI:
https://doi.org/10.1145/3793302.3793615
Focus to learn more
DOI(s) linking to related resources
Submission history From: Shamse Tasnim Cynthia [view email]          [v1]
Tue, 27 Jan 2026 22:55:05 UTC (194 KB)



## 2601.20072

准入 2+1+2=5：limitedlabels MAE中validation-gated伪标签时机与双视图一致性抑制确认偏差→不能只优化伪标签生成忽略引入时机。

https://arxiv.org/abs/2601.20072v1
arXiv:2601.20072v1 (cs)
[Submitted on 27 Jan 2026]
Title:Semi-Supervised Masked Autoencoders: Unlocking Vision Transformer Potential with Limited Data
Authors:Atik Faysal, Mohammad Rostami, Reihaneh Gh. Roshan, Nikhil Muralidhar, Huaxia Wang
View a PDF of the paper titled Semi-Supervised Masked Autoencoders: Unlocking Vision Transformer Potential with Limited Data, by Atik Faysal and 3 other authors
View PDF
HTML (experimental)
Abstract:We address the challenge of training Vision Transformers (ViTs) when labeled data is scarce but unlabeled data is abundant. We propose Semi-Supervised Masked Autoencoder (SSMAE), a framework that jointly optimizes masked image reconstruction and classification using both unlabeled and labeled samples with dynamically selected pseudo-labels. SSMAE introduces a validation-driven gating mechanism that activates pseudo-labeling only after the model achieves reliable, high-confidence predictions that are consistent across both weakly and strongly augmented views of the same image, reducing confirmation bias. On CIFAR-10 and CIFAR-100, SSMAE consistently outperforms supervised ViT and fine-tuned MAE, with the largest gains in low-label regimes (+9.24% over ViT on CIFAR-10 with 10% labels). Our results demonstrate that when pseudo-labels are introduced is as important as how they are generated for data-efficient transformer training. Codes are available at this https URL.
Subjects:
Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
Cite as:
arXiv:2601.20072 [cs.CV]
(or
arXiv:2601.20072v1 [cs.CV] for this version)
https://doi.org/10.48550/arXiv.2601.20072
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Atik Faysal [view email]          [v1]
Tue, 27 Jan 2026 21:32:22 UTC (1,720 KB)



## 2601.20006

贡献关闭：按具体LLM/家族finetune文本检测+数据规模/99.6%成绩，题摘未给未知generator迁移、改写或真实性判断失效边界；不借安全场景自动准入。

https://arxiv.org/abs/2601.20006v1
arXiv:2601.20006v1 (cs)
[Submitted on 27 Jan 2026]
Title:On the Effectiveness of LLM-Specific Fine-Tuning for Detecting AI-Generated Text
Authors:Michał Gromadzki, Anna Wróblewska, Agnieszka Kaliska
View a PDF of the paper titled On the Effectiveness of LLM-Specific Fine-Tuning for Detecting AI-Generated Text, by Micha{\l} Gromadzki and 2 other authors
View PDF
HTML (experimental)
Abstract:The rapid progress of large language models has enabled the generation of text that closely resembles human writing, creating challenges for authenticity verification in education, publishing, and digital security. Detecting AI-generated text has therefore become a crucial technical and ethical issue. This paper presents a comprehensive study of AI-generated text detection based on large-scale corpora and novel training strategies. We introduce a 1-billion-token corpus of human-authored texts spanning multiple genres and a 1.9-billion-token corpus of AI-generated texts produced by prompting a variety of LLMs across diverse domains. Using these resources, we develop and evaluate numerous detection models and propose two novel training paradigms: Per LLM and Per LLM family fine-tuning. Across a 100-million-token benchmark covering 21 large language models, our best fine-tuned detector achieves up to $99.6\%$ token-level accuracy, substantially outperforming existing open-source baselines.
Comments:
34 pages, 6 figures. Under review at Information Sciences
Subjects:
Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
ACM classes:
I.2.7
Cite as:
arXiv:2601.20006 [cs.CL]
(or
arXiv:2601.20006v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20006
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Michał Gromadzki [view email]          [v1]
Tue, 27 Jan 2026 19:22:38 UTC (2,436 KB)



## 2601.19970

贡献关闭；日期未核：LlamaGuard专用分类器与base Llama prompt的100例局部比较未新增通用security机制/评价边界；模型小大因训练职责混杂，不能外推逆尺度安全规律。

https://arxiv.org/abs/2601.19970v1
arXiv:2601.19970v1 (cs)
[Submitted on 27 Jan 2026]
Title:Benchmarking LLAMA Model Security Against OWASP Top 10 For LLM Applications
Authors:Nourin Shahin, Izzat Alsmadi
View a PDF of the paper titled Benchmarking LLAMA Model Security Against OWASP Top 10 For LLM Applications, by Nourin Shahin and Izzat Alsmadi
View PDF
HTML (experimental)
Abstract:As large language models (LLMs) move from research prototypes to enterprise systems, their security vulnerabilities pose serious risks to data privacy and system integrity. This study benchmarks various Llama model variants against the OWASP Top 10 for LLM Applications framework, evaluating threat detection accuracy, response safety, and computational overhead. Using the FABRIC testbed with NVIDIA A30 GPUs, we tested five standard Llama models and five Llama Guard variants on 100 adversarial prompts covering ten vulnerability categories. Our results reveal significant differences in security performance: the compact Llama-Guard-3-1B model achieved the highest detection rate of 76% with minimal latency (0.165s per test), whereas base models such as Llama-3.1-8B failed to detect threats (0% accuracy) despite longer inference times (0.754s). We observe an inverse relationship between model size and security effectiveness, suggesting that smaller, specialized models often outperform larger general-purpose ones in security tasks. Additionally, we provide an open-source benchmark dataset including adversarial prompts, threat labels, and attack metadata to support reproducible research in AI security, [1].
Subjects:
Cryptography and Security (cs.CR); Machine Learning (cs.LG)
Cite as:
arXiv:2601.19970 [cs.CR]
(or
arXiv:2601.19970v1 [cs.CR] for this version)
https://doi.org/10.48550/arXiv.2601.19970
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Izzat Alsmadi [view email]          [v1]
Tue, 27 Jan 2026 18:20:14 UTC (13 KB)



## 2601.19960

贡献符合；firstday待核：streaming ASR可删除attention或以deformable conv代替且不显著损WER，足以检验受限流式负载是否需要attention；早Submitted01/27不能定窗。

https://arxiv.org/abs/2601.19960v1
arXiv:2601.19960v1 (eess)
[Submitted on 27 Jan 2026]
Title:Do we really need Self-Attention for Streaming Automatic Speech Recognition?
Authors:Youness Dkhissi (LIUM), Valentin Vielzeuf, Elys Allesiardo, Anthony Larcher (LIUM)
View a PDF of the paper titled Do we really need Self-Attention for Streaming Automatic Speech Recognition?, by Youness Dkhissi (LIUM) and 3 other authors
View PDF
HTML (experimental)
Abstract:Transformer-based architectures are the most used architectures in many deep learning fields like Natural Language Processing, Computer Vision or Speech processing. It may encourage the direct use of Transformers in the constrained tasks, without questioning whether it will yield the same benefits as in standard tasks.  Given specific constraints, it is essential to evaluate the relevance of transformer models. This work questions the suitability of transformers for specific domains. We argue that the high computational requirements and latency issues associated with these models do not align well with streaming applications. Our study promotes the search for alternative strategies to improve efficiency without sacrificing performance.  In light of this observation, our paper critically examines the usefulness of transformer architecture in such constrained environments. As a first attempt, we show that the computational cost for Streaming Automatic Speech Recognition (ASR) can be reduced using deformable convolution instead of Self-Attention. Furthermore, we show that Self-Attention mechanisms can be entirely removed and not replaced, without observing significant degradation in the Word Error Rate.
Subjects:
Audio and Speech Processing (eess.AS); Artificial Intelligence (cs.AI); Sound (cs.SD)
Cite as:
arXiv:2601.19960 [eess.AS]
(or
arXiv:2601.19960v1 [eess.AS] for this version)
https://doi.org/10.48550/arXiv.2601.19960
Focus to learn more
arXiv-issued DOI via DataCite
Journal reference:
International Conference on Acoustics, Speech, and Signal Processing (ICASSP), IEEE Signal Processing Society, May 2026, Barcelona, Spain
Submission history From: Youness Dkhissi [view email] [via CCSD proxy]          [v1]
Tue, 27 Jan 2026 08:07:14 UTC (205 KB)



## 2601.19942

贡献符合；firstday待核：多层隐状态谱/稀疏orderparameter出现深度阈值及可复用结构，若条件真实会修正表示/推理形成解释；Submitted01/16先日期核，不采用相变普遍结论。

https://arxiv.org/abs/2601.19942v1
arXiv:2601.19942v1 (cs)
[Submitted on 16 Jan 2026]
Title:Latent Object Permanence: Topological Phase Transitions, Free-Energy Principles, and Renormalization Group Flows in Deep Transformer Manifolds
Authors:Faruk Alpay, Bugra Kilictas
View a PDF of the paper titled Latent Object Permanence: Topological Phase Transitions, Free-Energy Principles, and Renormalization Group Flows in Deep Transformer Manifolds, by Faruk Alpay and 1 other authors
View PDF
HTML (experimental)
Abstract:We study the emergence of multi-step reasoning in deep Transformer language models through a geometric and statistical-physics lens. Treating the hidden-state trajectory as a flow on an implicit Riemannian manifold, we analyze the layerwise covariance spectrum of activations, where $C^{(\ell)}=\mathbb{E}[h^{(\ell)}h^{(\ell)\top}]$, and track deviations from a random-matrix bulk. Across model scales (1.5B--30B), we observe a sharp reduction in effective dimensionality consistent with a phase transition: an order parameter based on sparsity/localization, $\Omega(h)=1-\|h\|_1/(\sqrt{d}\|h\|_2)$, exhibits a discontinuity near a critical normalized depth $\gamma_c\approx 0.42$ in sufficiently large models. We formalize the forward pass as a discrete coarse-graining map and relate the appearance of stable "concept basins" to fixed points of this renormalization-like dynamics. The resulting low-entropy regime is characterized by a spectral tail collapse and by the formation of transient, reusable object-like structures in representation space, which we call Transient Class Objects (TCOs). We provide theoretical conditions connecting logical separability to spectral decay and validate the predicted signatures with layerwise probes on multiple open-weight model families.
Comments:
12 pages, 3 figures
Subjects:
Machine Learning (cs.LG); Computation and Language (cs.CL)
MSC classes:
68T50, 68T07, 68T05
ACM classes:
I.2.7; I.2.6
Cite as:
arXiv:2601.19942 [cs.LG]
(or
arXiv:2601.19942v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.19942
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Buğra Kılıçtaş [view email]          [v1]
Fri, 16 Jan 2026 23:11:02 UTC (802 KB)



## 2601.19925

贡献关闭；日期未核：本地160摘要LLM与人rubric一致度不同属于特定科学内容评价，未新增通用LLMjudge可靠性条件；AIforScience暂缓。

https://arxiv.org/abs/2601.19925v1
arXiv:2601.19925v1 (cs)
[Submitted on 9 Jan 2026]
Title:Evaluating Large Language Models for Abstract Evaluation Tasks: An Empirical Study
Authors:Yinuo Liu, Emre Sezgin, Eric A. Youngstrom
View a PDF of the paper titled Evaluating Large Language Models for Abstract Evaluation Tasks: An Empirical Study, by Yinuo Liu and 2 other authors
View PDF
Abstract:Introduction: Large language models (LLMs) can process requests and generate texts, but their feasibility for assessing complex academic content needs further investigation. To explore LLM's potential in assisting scientific review, this study examined ChatGPT-5, Gemini-3-Pro, and Claude-Sonnet-4.5's consistency and reliability in evaluating abstracts compared to one another and to human reviewers. Methods: 160 abstracts from a local conference were graded by human reviewers and three LLMs using one rubric. Composite score distributions across three LLMs and fourteen reviewers were examined. Inter-rater reliability was calculated using intraclass correlation coefficients (ICCs) for within-AI reliability and AI-human concordance. Bland-Altman plots were examined for visual agreement patterns and systematic bias. Results: LLMs achieved good-to-excellent agreement with each other (ICCs: 0.59-0.87). ChatGPT and Claude reached moderate agreement with human reviewers on overall quality and content-specific criteria, with ICCs ~.45-.60 for composite, impression, clarity, objective, and results. They exhibited fair agreement on subjective dimensions, with ICC ranging from 0.23-0.38 for impact, engagement, and applicability. Gemini showed fair agreement on half criteria and no reliability on impact and applicability. Three LLMs showed acceptable or negligible mean difference (ChatGPT=0.24, Gemini=0.42, Claude=-0.02) from the human mean composite scores. Discussion: LLMs could process abstracts in batches with moderate agreement with human experts on overall quality and objective criteria. With appropriate process architecture, they can apply a rubric consistently across volumes of abstracts exceeding feasibility for a human rater. The weaker performance on subjective dimensions indicates that AI should serve a complementary role in evaluation, while human expertise remains essential.
Comments:
17 pages, 4 figures, 2 tables
Subjects:
Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.19925 [cs.CL]
(or
arXiv:2601.19925v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.19925
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Emre Sezgin [view email]          [v1]
Fri, 9 Jan 2026 15:21:17 UTC (1,107 KB)



## 2601.19912

贡献定义待定；日期先保留：instruction-level GPU LLM fault injection题摘仅宣称架构/规模/任务效果，具体脆弱方向尚无；不从first标签倒准入。早Submitted12/25，必要日期未定。

https://arxiv.org/abs/2601.19912v1
arXiv:2601.19912v1 (cs)
[Submitted on 25 Dec 2025]
Title:Analysis of LLM Vulnerability to GPU Soft Errors: An Instruction-Level Fault Injection Study
Authors:Duo Chai, Zizhen Liu, Shuhuai Wang, Songwei Pei, Cheng Liu, Huawei Li, Shangguang Wang
View a PDF of the paper titled Analysis of LLM Vulnerability to GPU Soft Errors: An Instruction-Level Fault Injection Study, by Duo Chai and 5 other authors
View PDF
HTML (experimental)
Abstract:Large language models (LLMs) are highly compute- and memory-intensive, posing significant demands on high-performance GPUs. At the same time, advances in GPU technology driven by shrinking transistor sizes and lower operating voltages have made these devices increasingly susceptible to soft errors. While prior work has examined GPU reliability, most studies have focused on general-purpose applications or conventional neural networks mostly used for vision tasks such as classification and detection. In contrast, systematic analysis of modern large-scale LLMs remains limited, despite their rapid adoption in diverse application scenarios. Given the unique characteristics of LLMs, their resilience to soft errors may differ substantially from earlier models. To bridge this gap, we conduct the first instruction-level fault injection study of LLM inference. Our approach reveals reliability characteristics from multiple perspectives, highlighting the effects of model architecture, parameter scale, and task complexity. These findings provide new insights into LLM reliability and inform the design of more effective fault tolerance mechanisms.
Comments:
14 pages, 13 figures
Subjects:
Hardware Architecture (cs.AR); Artificial Intelligence (cs.AI); Cryptography and Security (cs.CR)
Cite as:
arXiv:2601.19912 [cs.AR]
(or
arXiv:2601.19912v1 [cs.AR] for this version)
https://doi.org/10.48550/arXiv.2601.19912
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Duo Chai [view email]          [v1]
Thu, 25 Dec 2025 11:59:54 UTC (3,157 KB)



## 2601.19908

贡献符合；firstday待核：attention带宽与weights密度分离映射到DRAM/RRAM chiplet并近数据融合→重考虑同质存储和跨chiplet流量；Submitted12/12先日期核，54x非实测默认。

https://arxiv.org/abs/2601.19908v1
arXiv:2601.19908v1 (cs)
[Submitted on 12 Dec 2025]
Title:CHIME: Chiplet-based Heterogeneous Near-Memory Acceleration for Edge Multimodal LLM Inference
Authors:Yanru Chen, Runyang Tian, Yue Pan, Zheyu Li, Weihong Xu, Tajana Rosing
View a PDF of the paper titled CHIME: Chiplet-based Heterogeneous Near-Memory Acceleration for Edge Multimodal LLM Inference, by Yanru Chen and 5 other authors
View PDF
HTML (experimental)
Abstract:The proliferation of large language models (LLMs) is accelerating the integration of multimodal assistants into edge devices, where inference is executed under stringent latency and energy constraints, often exacerbated by intermittent connectivity. These challenges become particularly acute in the context of multimodal LLMs (MLLMs), as high-dimensional visual inputs are transformed into extensive token sequences, thereby inflating the key-value (KV) cache and imposing substantial data movement overheads to the LLM backbone. To address these issues, we present CHIME, a chiplet-based heterogeneous near-memory acceleration for edge MLLMs inference. CHIME leverages the complementary strengths of integrated monolithic 3D (M3D) DRAM and RRAM chiplets: DRAM supplies low-latency bandwidth for attention, while RRAM offers dense, non-volatile storage for weights. This heterogeneous hardware is orchestrated by a co-designed mapping framework that executes fused kernels near data, minimizing cross-chiplet traffic to maximize effective bandwidth. On FastVLM (0.6B/1.7B) and MobileVLM (1.7B/3B), CHIME achieves up to 54x speedup and up to 246x better energy efficiency per inference as compared to the edge GPU NVIDIA Jetson Orin NX. It sustains 116.5-266.5 token/J compared to Jetson's 0.7-1.1 token/J. Furthermore, it delivers up to 69.2x higher throughput than the state-of-the-art PIM accelerator FACIL. Compared to the M3D DRAM-only design, CHIME's heterogeneous memory further improves energy efficiency by 7% and performance by 2.4x.
Subjects:
Hardware Architecture (cs.AR); Machine Learning (cs.LG)
Cite as:
arXiv:2601.19908 [cs.AR]
(or
arXiv:2601.19908v1 [cs.AR] for this version)
https://doi.org/10.48550/arXiv.2601.19908
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yanru Chen [view email]          [v1]
Fri, 12 Dec 2025 03:59:36 UTC (3,706 KB)



## 2601.19904

贡献定义待定；日期先保留：dataflow training profiling框架未在题摘说实际瓶颈规律；不从3硬件覆盖倒准入，必要一点评价事实待定。Submitted12/04先日期核。

https://arxiv.org/abs/2601.19904v1
arXiv:2601.19904v1 (cs)
[Submitted on 4 Dec 2025]
Title:DABench-LLM: Standardized and In-Depth Benchmarking of Post-Moore Dataflow AI Accelerators for LLMs
Authors:Ziyu Hu, Zhiqing Zhong, Weijian Zheng, Zhijing Ye, Xuwei Tan, Xueru Zhang, Zheng Xie, Rajkumar Kettimuthu, Xiaodong Yu
View a PDF of the paper titled DABench-LLM: Standardized and In-Depth Benchmarking of Post-Moore Dataflow AI Accelerators for LLMs, by Ziyu Hu and 8 other authors
View PDF
HTML (experimental)
Abstract:The exponential growth of large language models has outpaced the capabilities of traditional CPU and GPU architectures due to the slowdown of Moore's Law. Dataflow AI accelerators present a promising alternative; however, there remains a lack of in-depth performance analysis and standardized benchmarking methodologies for LLM training. We introduce DABench-LLM, the first benchmarking framework designed for evaluating LLM workloads on dataflow-based accelerators. By combining intra-chip performance profiling and inter-chip scalability analysis, DABench-LLM enables comprehensive evaluation across key metrics such as resource allocation, load balance, and resource efficiency. The framework helps researchers rapidly gain insights into underlying hardware and system behaviors, and provides guidance for performance optimizations. We validate DABench-LLM on three commodity dataflow accelerators, Cerebras WSE-2, SambaNova RDU, and Graphcore IPU. Our framework reveals performance bottlenecks and provides specific optimization strategies, demonstrating its generality and effectiveness across a diverse range of dataflow-based AI hardware platforms.
Subjects:
Hardware Architecture (cs.AR); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Distributed, Parallel, and Cluster Computing (cs.DC); Performance (cs.PF)
Cite as:
arXiv:2601.19904 [cs.AR]
(or
arXiv:2601.19904v1 [cs.AR] for this version)
https://doi.org/10.48550/arXiv.2601.19904
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Ziyu Hu [view email]          [v1]
Thu, 4 Dec 2025 22:43:14 UTC (433 KB)



## 2601.20595

准入 2+2+2=6：whole-kernel overlap的launch/barrier长尾→可与backend/kernel解耦的chunk schedule并kernel内消费→需按chunk依赖而非只stream边界组织重叠；精确v1标题需核正文。

https://arxiv.org/abs/2601.20595v1
arXiv:2601.20595v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 1 Jul 2026 (v4)]
Title:AutoOverlap: Enabling Fine-Grained Overlap of Computation and Communication with Chunk-Based Scheduling
Authors:Xinwei Qiang, Yue Guan, Zhengding Hu, Yufei Ding, Adnan Aziz
View a PDF of the paper titled AutoOverlap: Enabling Fine-Grained Overlap of Computation and Communication with Chunk-Based Scheduling, by Xinwei Qiang and 4 other authors
View PDF
HTML (experimental)
Abstract:Communication has become a first-order bottleneck in large-cale GPU workloads, and existing distributed compilers address it mainly by overlapping whole compute and communication kernels at the stream level. This coarse granularity incurs extra kernel launches, forces device-wide synchronizations at kernel boundaries, and leaves substantial slack when the slowest tile or kernel stretches the communication tail. We present AutoOverlap, a compiler and runtime that enables automatic fine-grained overlap inside a single fused kernel. AutoOverlap introduces a communication chunk abstraction that decouples communication granularity from kernel structure and backend mechanisms, allowing chunk-level plans to be ported from existing distributed compilers, written directly by users, or instantiated from reusable templates. Given a local Triton kernel and a chunk schedule, AutoOverlap performs transformations to align computation with chunk availability. Implemented as a source-to-source compiler on Triton, AutoOverlap delivers an average end-to-end speedup of 1.3$\times$ and up to 4.7$\times$ on multi-GPU workloads.
Subjects:
Distributed, Parallel, and Cluster Computing (cs.DC)
Cite as:
arXiv:2601.20595 [cs.DC]
(or
arXiv:2601.20595v1 [cs.DC] for this version)
https://doi.org/10.48550/arXiv.2601.20595
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Xinwei Qiang [view email]          [v1]
Wed, 28 Jan 2026 13:29:51 UTC (429 KB)
[v2]
Fri, 27 Mar 2026 08:04:43 UTC (429 KB)
[v3]
Fri, 3 Apr 2026 01:00:32 UTC (428 KB)
[v4]
Wed, 1 Jul 2026 05:30:30 UTC (1,235 KB)



## 2601.20273

准入 2+2+2=6：DiT SP跨机alltoall与双侧同步成为关键路径→topologyaware/Torus overlap/onesided→拓扑与通信语义共同决定SP实现；不外推所有集群。

https://arxiv.org/abs/2601.20273v1
arXiv:2601.20273v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 22 May 2026 (v2)]
Title:StreamFusion: Scalable Sequence Parallelism for Distributed Inference of Diffusion Transformers on GPUs
Authors:Jiacheng Yang, Jun Wu, Yaoyao Ding, Zhiying Xu, Yida Wang, Gennady Pekhimenko
View a PDF of the paper titled StreamFusion: Scalable Sequence Parallelism for Distributed Inference of Diffusion Transformers on GPUs, by Jiacheng Yang and 5 other authors
View PDF
HTML (experimental)
Abstract:Diffusion Transformers (DiTs) have gained increasing adoption in high-quality image and video generation. As demand for higher-resolution images and longer videos increases, single-GPU inference becomes inefficient due to increased latency and large activation sizes. Current frameworks employ sequence parallelism (SP) techniques such as Ulysses Attention and Ring Attention to scale inference. However, these implementations have three primary limitations: (1) suboptimal communication patterns for network topologies on modern GPU machines, (2) latency bottlenecks from all-to-all operations in inter-machine communication, and (3) GPU sender-receiver synchronization and computation overheads from using two-sided communication libraries. To address these issues, we present StreamFusion, a topology-aware efficient DiT serving engine. StreamFusion incorporates three key innovations: (1) a topology-aware sequence parallelism technique that accounts for inter- and intra-machine bandwidth differences, (2) Torus Attention, a novel SP technique enabling overlapping of inter-machine all-to-all operations with computation, and (3) a one-sided communication implementation that minimizes GPU sender-receiver synchronization and computation overheads. Our experiments demonstrate that StreamFusion outperforms the state-of-the-art approach by an average of $1.35\times$ (up to $1.77\times$).
Subjects:
Distributed, Parallel, and Cluster Computing (cs.DC); Computer Vision and Pattern Recognition (cs.CV)
Cite as:
arXiv:2601.20273 [cs.DC]
(or
arXiv:2601.20273v1 [cs.DC] for this version)
https://doi.org/10.48550/arXiv.2601.20273
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Jiacheng Yang [view email]          [v1]
Wed, 28 Jan 2026 05:42:07 UTC (1,104 KB)
[v2]
Fri, 22 May 2026 19:27:59 UTC (1,086 KB)



## 2601.20317

准入 2+2+2=6：VGGT饱和channel与3D语义使LLM校准失真→orthogonal calibrationfree量化及非线性/重算tile协同→不能直接迁移LLM量化；模拟/ASIC边界需核。

https://arxiv.org/abs/2601.20317v1
arXiv:2601.20317v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 15 Jul 2026 (v2)]
Title:VersaQ-3D: A Reconfigurable Accelerator Enabling Feed-Forward and Generalizable 3D Reconstruction via Versatile Quantization
Authors:Yipu Zhang, Jintao Cheng, Xingyu Liu, Zeyu Li, Carol Jingyi Li, Jin Wu, Lin Jiang, Yuan Xie, Jiang Xu, Wei Zhang
View a PDF of the paper titled VersaQ-3D: A Reconfigurable Accelerator Enabling Feed-Forward and Generalizable 3D Reconstruction via Versatile Quantization, by Yipu Zhang and 9 other authors
View PDF
HTML (experimental)
Abstract:The Visual Geometry Grounded Transformer (VGGT) enables strong feed-forward 3D reconstruction without per-scene optimization. However, its billion-parameter scale creates high memory and compute demands, hindering on-device deployment. Existing LLM quantization methods fail on VGGT due to saturated activation channels and diverse 3D semantics, which cause unreliable calibration. Furthermore, VGGT presents hardware challenges regarding precision-sensitive nonlinear operators and memory-intensive global attention. To address this, we propose VersaQ-3D, an algorithm-architecture co-design framework. Algorithmically, we introduce the first calibration-free, scene-agnostic quantization for VGGT down to 4-bit, leveraging orthogonal transforms to decorrelate features and suppress outliers. Architecturally, we design a reconfigurable accelerator supporting BF16, INT8, and INT4. A unified systolic datapath handles both linear and nonlinear operators, reducing latency by 60%, while two-stage recomputation-based tiling alleviates memory pressure for long-sequence attention. Evaluations show VersaQ-3D preserves 98-99% accuracy at W4A8. At W4A4, it outperforms prior methods by 1.61x-2.39x across diverse scenes. The accelerator delivers 5.2x-10.8x speedup over edge GPUs with low power, enabling efficient instant 3D reconstruction.
Subjects:
Hardware Architecture (cs.AR)
Cite as:
arXiv:2601.20317 [cs.AR]
(or
arXiv:2601.20317v1 [cs.AR] for this version)
https://doi.org/10.48550/arXiv.2601.20317
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yipu Zhang [view email]          [v1]
Wed, 28 Jan 2026 07:21:32 UTC (6,982 KB)
[v2]
Wed, 15 Jul 2026 02:22:26 UTC (3,323 KB)



## 2601.20362

撤回排除；不评分不Books：当前官方v2页面明确整稿实验参数/算法推导Section3/4严重错误导致结论误解，2026-05-07撤回；不因v1仍可读而采用旧收益。

https://arxiv.org/abs/2601.20362v1
arXiv:2601.20362v1 (cs)
A newer version of this paper has been withdrawn by Xiangbo Wang
[Submitted on 28 Jan 2026 (this version), latest version 7 May 2026 (v2)]
Title:Switchcodec: Adaptive residual-expert sparse quantization for high-fidelity neural audio coding
Authors:Xiangbo Wang, Wenbin Jiang, Jin Wang, Yubo You, Sheng Fang, Fei Wen
View a PDF of the paper titled Switchcodec: Adaptive residual-expert sparse quantization for high-fidelity neural audio coding, by Xiangbo Wang and 5 other authors
View PDF
HTML (experimental)
Abstract:Recent neural audio compression models often rely on residual vector quantization for high-fidelity coding, but using a fixed number of per-frame codebooks is suboptimal for the wide variability of audio content-especially for signals that are either very simple or highly complex. To address this limitation, we propose SwitchCodec, a neural audio codec based on Residual Experts Vector Quantization (REVQ). REVQ combines a shared quantizer with dynamically routed expert quantizers that are activated according to the input audio, decoupling bitrate from codebook capacity and improving compression efficiency. This design ensures full training and utilization of each quantizer. In addition, a variable-bitrate mechanism adjusts the number of active expert quantizers at inference, enabling multi-bitrate operation without retraining. Experiments demonstrate that SwitchCodec surpasses existing baselines on both objective metrics and subjective listening tests.
Comments:
4page,3figure,Accepted by ICASSP 2026,We would like to express our sincere gratitude to Senior Fellow Jing Wang for his continuous support and assistance. He has made an indelible and significant contribution to this work
Subjects:
Sound (cs.SD); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20362 [cs.SD]
(or
arXiv:2601.20362v1 [cs.SD] for this version)
https://doi.org/10.48550/arXiv.2601.20362
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Xiangbo Wang [view email]          [v1]
Wed, 28 Jan 2026 08:26:20 UTC (1,446 KB)
[v2]
Thu, 7 May 2026 16:51:49 UTC (1 KB) (withdrawn)


