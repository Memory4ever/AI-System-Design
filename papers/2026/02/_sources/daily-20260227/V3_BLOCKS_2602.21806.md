[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Bugs in Modern LLM Agent Frameworks: An Empirical Study

[3] h6: Abstract.

[4] p: LLM agents have been widely adopted in real-world applications, relying on agent frameworks for workflow execution and multi-agent coordination. As these systems scale, understanding bugs in the underlying agent frameworks becomes critical. However, existing work mainly focuses on agent-level failures, overlooking framework-level bugs. To address this gap, we conduct an empirical study of 998 bug reports from CrewAI and LangChain, constructing a taxonomy of 15 root causes and 7 observable symptoms across five agent lifecycle stages: ‘Agent Initialization’, ‘Perception’, ‘Self-Action’, ‘Mutual Interaction’ and ‘Evolution’. Our findings show that agent framework bugs mainly arise from ‘API misuse’, ‘API incompatibility’, and ‘Documentation Desync’, largely concentrated in the ‘Self-Action’ stage. Symptoms typically appear as ‘Functional Error’, ‘Crash’, and ‘Build Failure’, reflecting disruptions to task progression and control flow.

[5] h6: Keywords:

[6] h2: 1. Introduction

[7] p: Large language models (LLMs) achieve rapid progress in real-world industry applications like intelligent Q&A ( Lewis et al., 2020 ) , automated software engineering ( Chen et al., 2021 ) , and multimodal autonomous driving ( Li et al., 2023 ; Huang et al., 2023 ) . As LLMs’ capabilities grow, single-call usage patterns fail to support long-horizon, tool-driven tasks, motivating the agent paradigm that integrates models with memory, tools, and control logic. To support the development of LLM agents, researchers introduce LLM agent frameworks (e.g., LangChain ( , 2023 ) ) that help users define task workflows, manage agent state, coordinate actions and tools, and integrate agents into larger software systems. When bugs arise in LLM agent frameworks, they can propagate to upper-layer systems and amplify their impact, leading to incorrect execution, resource misuse, and security risks. Such bugs in LLM infrastructure may propagate throughout the LLM software supply chain ( Wang et al., 2025 ) and pose a serious security threat to agent-based software systems. Therefore, there is an urgent need to study and understand their observable symptoms and underlying root causes to strengthen the quality of the LLM software supply chain. However, existing work ( Cemri et al., 2025 ; Zhang et al., 2025 ) primarily investigates agent-level failures in reasoning, planning, and action processes, often through behavioral analysis or benchmark evaluation. These studies enhance our understanding of agent behaviors and model limitations, but largely overlook bugs rooted in the underlying agent frameworks. While a recent study ( Xue et al., 2025 ) starts to analyze agent library bugs by mapping pull requests to static components of libraries (e.g., data preprocessing), this approach overlooks the dynamic execution and temporal workflows of agents. Consequently, how LLM agent framework bugs manifest across the dynamic agent lifecycle remains largely unexplored.

[8] p: To address this gap, in this paper, we collect and manually analyze 998 bug reports from two representative agent frameworks, CrewAI ( , 2024 ) and LangChain ( , 2023 ) , to identify the root causes and symptoms of diverse agent framework bugs. We map these findings onto five agent lifecycle stages (i.e., ‘Agent Initialization’, ‘Perception’, ‘Self-Action’, ‘Mutual Interaction’, and ‘Evolution’) and construct a taxonomy comprising 15 root causes and 7 symptoms. This lifecycle-oriented taxonomy clarifies where bugs arise and how framework-level issues propagate during execution. We further formulate two research questions (RQs) to examine their root causes and observable manifestations, as shown in the following.

[9] p: ∙ \bullet RQ1: What are the root causes of Agent framework bugs? Identifying root causes is essential for explaining why failures repeatedly occur and for revealing dominant bug sources within agent frameworks. From 998 issue reports, we identify 15 root cause categories, with ‘API Misuse’ (32.97%) and ‘API Incompatibility’ (22.34%) accounting for over 55% of all cases. Most root causes concentrate in the Self-Action stage, indicating that mechanisms related to execution semantics are the primary source of framework failures.

[10] p: ∙ \bullet RQ2: What are the symptoms of Agent framework bugs? Characterizing symptoms clarifies how LLM agent framework bugs surface during execution and what breakdown patterns users ultimately encounter. We identify 7 symptom categories, which also predominantly cluster in the ‘Self-Action’ stage. The categories of ‘Crash’, ‘Functional Error’, and ‘Build Failure’ account for the majority of observable disruptions, suggesting that framework bugs mainly manifest as breakdowns in workflow progression rather than isolated interface bugs.

[11] p: Overall, the main contributions of this work are as follows.

[12] p: Innovative Perspective. We introduce a lifecycle-oriented perspective for analyzing LLM agent framework bugs, systematically organizing bugs across key stages of ‘Agent Initialization’, ‘Perception’, ‘Self-Action’, ‘Mutal Interaction’, and ‘Evolution’. This perspective provides a structured foundation for understanding where and how framework-level bugs arise during agent execution.

[13] p: Empirical Study and Key Findings. Based on 998 issue reports from two LLM agent frameworks, our study constructs a taxonomy of 15 root causes and 7 symptoms, and reveals their non-trivial distributions and correlations across lifecycle stages, highlighting execution-semantics mechanisms as the dominant source of failures.

[14] p: Reproducible Artifacts. We release our curated dataset, taxonomy definitions, and analysis scripts to facilitate replication and future research on LLM agent frameworks.

[15] h2: 2. Methodology

[16] p: To investigate agent framework bugs, we adopt a three-step methodology, as shown in Figure 1 . (1) Issue Collection. We gather bug reports from open-source agent framework communities. (2) Bug Filtering. We apply predefined criteria to remove irrelevant or duplicate reports, ensuring data reliability. (3) Individual Labeling. Two authors independently label each report with its target component, root cause, and symptom, and cross-check results to maintain consistency. Finally, we construct a lifecycle-oriented taxonomy that maps root causes and symptoms to the five agent lifecycle stages, providing a structured foundation for analysis.

[17] h3: 2.1. Issue Collection

[18] p: To study bugs in agent frameworks, we select two representative and widely used open-source agent frameworks, namely CrewAI ( , 2024 ) and LangChain ( , 2023 ) , as research subjects. Both of these frameworks are suitable for agent orchestration and development scenarios and occupy similar niches in the LLM agent workflow. Developers can use them to organize models, invoke tools, and complete multi-step tasks. Specifically, LangChain offers a mature framework with rich abstractions for tool invocation and execution pipelines, while CrewAI focuses on role-based multi-agent collaboration, reflecting different design emphases in agent framework development. They totally have 68.5k stars on GitHub. These complementary characteristics allow us to examine diverse framework mechanisms and bug patterns. We collect bug reports from the official GitHub repositories of both frameworks, which maintain active developer communities and extensive user adoption.

[19] p: We adopt a full data scraping strategy that includes both open and closed issues to reduce sampling bias and ensure comprehensive coverage of framework bugs. We collect a total of 2,773 original issue reports from the two selected frameworks, including 1,660 issues from CrewAI and 1,113 issues from LangChain, spanning the period from December 7, 2023, to January 10, 2026. For each issue report, we retrieve and extract its core content for subsequent bug analysis, including title, labels, content, and comments. These elements together form the basis for our empirical analysis.

[20] h3: 2.2. Bug filtering

[21] p: We adopt a two-stage filtering process to refine the collected issue reports and ensure analytical relevance, as follows.

[22] p: Stage 1: Label Filtering. We first leverage GitHub labels to perform preliminary filtering. For each issue, we check whether maintainers assign the label ‘bug’. If the issue contains this label, we retain it for further analysis; otherwise, we exclude it. This step narrows the dataset to issues that the community explicitly recognizes as potential bugs and reduces irrelevant entries at an early stage. After this stage, 1,010 issue reports remain.

[23] p: Stage 2: Manual Inspection. We then conduct a manual inspection to eliminate mislabeled or irrelevant reports. Two researchers independently examine the title, issue description, and associated comments of each pre-screened issue and evaluate them against our operational definition of an agent framework bug.

[24] p: During this stage, we exclude three main categories of issue reports, including ❶ non-functional textual errors such as documentation typos, ❷ incomplete documentation requests or usage questions, ❸ invalid or infrastructure-related issues that do not involve framework logic. After this two-stage filtering process, we obtain a refined dataset of 998 issues that directly relate to agent framework bugs and form the basis for subsequent analysis and classification.

[25] figure: Figure 1. Overview of our Three-Step Methodology

[26] h3: 2.3. Individual Labeling

[27] p: Two authors serve as the annotators to label the bug reports. The overall process consists of two key stages: initial taxonomy construction and large-scale annotation.

[28] p: Stage I: Initial Taxonomy Construction. To ensure labeling reliability and establish a principled classification scheme, we randomly sample 100 issue reports from the refined dataset as a representative subset for initial analysis. We invite two authors with at least one year experience in software engineering with LLM independently examine each sampled report and perform three tasks: identifying the primary framework component involved, inferring the underlying root causes of the abnormal behavior, and documenting the symptoms manifested during execution. For the inconsistencies, two authors conduct online meetings to reach an agreement. From this process, we derive an initial taxonomy consisting of 15 root cause categories and 7 symptom categories.

[29] p: Stage II: Large-Scale Annotation. With the initial taxonomy established, two annotators apply it to the remaining issue reports for large-scale labeling. For each issue, annotators follow the same process used in Stage I. Then, annotators record category assignments directly using the predefined taxonomy and document brief justifications when classification requires interpretation. During this process, a new category is introduced only if meeting issues whose root causes or symptoms do not clearly fit any existing category.

[30] p: Finally, we obtain a taxonomy consisting of 15 root cause categories and 7 symptom categories from 998 issue reports.

[31] h2: 3. Result Analysis

[32] h3: 3.1. RQ1: Root Causes

[33] p: Based on the classification of 998 bug reports, we identify 15 root cause categories. ‘API Misuse’ and ‘API Incompatibility’ dominate the distribution, together accounting for over half of the cases, highlighting the central role of interface-related problems in agent framework failures. Other categories, such as ‘Frontend–Backend Mismatch’ and ‘Console Interaction’, occur far less frequently. These results indicate that most bugs stem from execution semantics and API evolution rather than isolated infrastructure issues ( Figure 2 ).

[34] p: ∙ \bullet R1.API Incompatibility (223/998). This root cause emerges when changes in agent framework APIs alter execution semantics across planning, tool invocation, or multi-step workflows, thereby breaking assumptions embedded in agent logic rather than merely causing surface-level version conflicts.

[35] p: ∙ \bullet R2.API Misuse (329/998). This root cause occurs when developers misunderstand the agent framework’s execution abstractions, control-flow design, or lifecycle semantics, leading to incorrect orchestration of tools, memory, or agent interactions.

[36] p: ∙ \bullet R3.Configuration Misalignment (53/998). It appears when the agent framework expects specific runtime configurations (e.g., model backends, tool registries), but the actual environment violates these assumptions and disrupts agent execution semantics.

[37] p: ∙ \bullet R4.Telemetry Malfunction (32/998). This root cause arises when tracing, logging, or observability components embedded in the agent framework interfere with execution flow or fail to correctly capture agent state transitions.

[38] p: ∙ \bullet R5.Streaming Instability (67/998). This root cause occurs when the framework’s streaming mechanisms, which coordinate incremental model outputs and tool responses, lose synchronization or terminate prematurely, breaking workflow continuity.

[39] p: ∙ \bullet R6.Serialization Error (53/998). This root cause appears when the framework fails to correctly encode or decode structured execution artifacts such as agent state, intermediate plans, or tool-call messages, leading to corrupted execution context.

[40] p: ∙ \bullet R7.Execution Isolation (20/998). This root cause emerges when sandboxing policies or security constraints enforced by the agent framework conflict with intended tool execution or cross-agent coordination semantics.

[41] p: ∙ \bullet R8.Memory Persistence Bug (30/998). This root cause occurs when the framework’s memory management mechanisms fail to maintain consistent long-term state, embedding indices, or retrieval mappings across agent iterations.

[42] p: ∙ \bullet R9.Console Interaction Issue (15/998). This root cause arises when the framework assumes interactive execution patterns that do not align with the actual runtime context, thereby disrupting command handling or workflow triggering.

[43] p: ∙ \bullet R10.Documentation Desync (75/998). This root cause appears when inconsistencies between documented abstractions and actual framework behavior mislead developers about lifecycle semantics, API contracts, or execution guarantees.

[44] p: ∙ \bullet R11.Knowledge Transmission Issue (21/998). It emerges in multi-agent settings when the framework fails to correctly propagate context, task specifications, or role-specific information across agents.

[45] p: ∙ \bullet R12.Frontend-Backend Mismatch (7/998). This root cause occurs when inconsistencies between monitoring interfaces and backend execution logic lead to misleading state visualization or incorrect control signals during agent operation.

[46] p: ∙ \bullet R13.Concurrency Behavior Confusion (20/998). This root cause arises when frameworks’ concurrency model, e.g., asynchronous graph execution or task scheduling semantics, creates implicit behaviors that developers misinterpret during agent orchestration.

[47] p: ∙ \bullet R14.Dependency Environment Inconsistency (35/998). This root cause appears when the framework’s required software stack conflicts with the surrounding ecosystem, preventing the correct initialization of agent runtimes, model backends, or tool integrations.

[48] p: ∙ \bullet R15.Other (18/998). This category includes low-frequency root causes that do not fit existing groups but still expose implicit design assumptions in agent frameworks, such as hidden dependencies on file systems, operating systems, or execution boundaries.

[49] figure: Figure 2. Root Cause Distribution of Agent Framework Bugs

[50] p: Analysis on Lifecycle Distribution. We further examine how root causes distribute across the five lifecycle stages. Although some types span multiple stages, clear concentration patterns emerge.

[51] p: The ‘Agent Initialization’ stage mainly involves ‘Documentation Desync’ (11/36), ‘API Misuse‘ (8/36), and ‘API Incompatibility’ (6/36), with fewer cases of ‘Dependency Environment Inconsistency’, ‘Configuration Misalignment’, and ‘Execution isolation’. These issues block proper setup, capability registration, or parameter configuration, creating flawed execution foundations.

[52] p: The ‘Perception’ stage centers on interface and configuration consistency. ‘API Misuse’ (8/18) and ‘Documentation Desync’ (3/18) lead to incorrect calls or outdated assumptions, while ‘Configuration Misalignment’ and ‘Frontend–Backend Mismatch’ disrupt environmental alignment, reducing input reliability for reasoning.

[53] p: The ‘Self-Action’ stage shows the highest concentration of bugs. ‘API Misuse’ (289/882) and ‘API Incompatibility’ (211/882) dominate, followed by ‘Streaming Instability’, ‘Documentation Desync’, ‘Serialization Error’, ‘Configuration Misalignment’, and ‘Dependency Inconsistency’. These issues arise during scheduling, tool invocation, and graph execution, where mismatches between developer expectations and execution semantics often cause duplicated runs, stalled workflows, or premature termination.

[54] p: The ‘Mutual Interaction’ stage features coordination failures, including ‘API Misuse’ (20/53) and ‘Streaming Instability’ (8/53), which disrupt delegation logic and shared state consistency.

[55] p: The ‘Evolution’ stage focuses on ‘Memory Persistence Issue’, where inconsistent state updates, embedding refresh failures, or dependency drift weaken long-term continuity and adaptation.

[56] h3: 3.2. RQ2: Symptoms

[57] p: We conduct annotation and summarization on 998 bug issues in the dataset and identify the following 7 core symptom categories and their distribution. Detailed results are shown in Figure 3 .

[58] p: ∙ \bullet S1.Crash (100/998). This symptom represents the most explicit symptom of an agent framework bug. The framework crashes, terminates unexpectedly, or loses its execution capability because internal components fail at runtime. The agent cannot continue task execution once the bug triggers.

[59] p: ∙ \bullet S2.Functional Error (781/998). This symptom reflects logical bugs inside the agent framework. The system keeps running, but core mechanisms such as state tracking, planning flow, or tool coordination behave incorrectly. As a result, the agent produces wrong outcomes or fails to complete tasks reliably.

[60] p: ∙ \bullet S3.Build Failure (67/998). This symptom indicates structural or dependency-related bugs in the framework. Installation, configuration, or startup processes break before the agent enters an operational state, which prevents any task execution from beginning.

[61] p: ∙ \bullet S4.Poor Performance (10/998). This symptom reveals efficiency-related bugs in framework design or resource management. The agent continues operating, but response time increases, resource usage grows abnormally, or throughput drops, which degrades overall system effectiveness.

[62] p: ∙ \bullet S5.Hang (17/998). This symptom exposes control-flow or coordination bugs inside the agent framework. Execution stops progressing without explicit errors, and the agent remains stuck in an unresolved state instead of completing or terminating the workflow.

[63] p: ∙ \bullet S6.Unreported (4/998). This symptom reflects validation or handling bugs in the framework. The system accepts inputs or configurations but ignores them or fails to enforce constraints, which creates silent misbehavior without clear failure signals.

[64] p: ∙ \bullet S7.Display Anomaly (19/998). This symptom captures inconsistencies caused by a framework-level bug in logging, visualization, or interface rendering. The agent may execute internally, but the framework presents misleading or incorrect information to users.

[65] p: Analysis on Agent Lifecycle Distribution. We analyze symptom manifestations across the five stages of the agent lifecycle and observe clear stage-level concentration patterns. Although each symptom reflects a different observable failure, their distribution reveals structural imbalances across stages.

[66] p: In the ‘Agent Initialization’ stage, symptoms are mainly in the categories of ‘Functional Error ’ (21/36) and ‘Build Failure ’ (6/36). Agents fail to start properly, ignore configuration parameters, or display incorrect setup information, which undermines reliable preparation before execution begins.

[67] p: The ‘Perception’ stage frequently exhibits ‘Functional Error’ (13/18), ‘Display Anomaly’ (3/18), ‘Crash’, and ‘Build Failure’. Interrupted data streams, malformed inputs, or inefficient processing distort internal state construction or delay input handling.

[68] p: The ‘Self-Action’ stage shows the highest diversity of symptoms, including ‘Functional Error’ (692/882), ‘Crash’ (91/882), ‘Build Failure’ (58/882), ‘Hang’, and ‘Display Anomaly’. Since this stage controls planning and tool invocation, bugs here directly disrupt workflow progression or generate incorrect task outcomes.

[69] p: The ‘Mutual Interaction’ stage primarily involves ‘Functional Error’ (49/53), ‘Crash’, ‘Build Failure’, ‘Poor Performance’ and ‘Display Anomaly’, which weaken coordination and shared state consistency across agents.

[70] p: The ‘Evolution’ stage mainly presents ‘Functional Error’ (6/9), ‘Crash’, and ‘Build Failure’. bugs in memory updating, experience accumulation, or adaptive adjustment prevent agents from correctly refining internal states over time, which gradually reduces system reliability and long-term task effectiveness.

[71] figure: Figure 3. Symptoms Distribution of Agent Framework Bugs

[72] h2: 4. Conclusion & Future Work

[73] p: We present a lifecycle-oriented study of bugs in agent frameworks by analyzing 998 reports from CrewAI and LangChain. We identify dominant root causes, observable symptoms, and their structured relationships, showing how framework-level issues affect agent execution. Our taxonomy of 15 root causes and 7 symptoms across five lifecycle stages highlights API-related problems and execution-stage mechanisms as primary failure drivers. This paper provides insights for the development and maintenance of LLM agent infrastructure, promoting research on the LLM software supply chain.

[74] p: This paper provides a systematic study of agent framework bugs. Future work can explore lifecycle-aware testing and analysis methods to detect execution-semantic bugs early. As agent ecosystems evolve, research should address state-consistency, coordination, and resource-management bugs in multi-agent and long-running workflows. Finally, integrating our insights into framework design, including standardized APIs, dependency management, and runtime monitoring, may help reduce systemic failures.

[75] h2: References

[76] h2: Instructions for reporting errors

[77] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[78] p: Tip: You can select the relevant text first, to include it in your report.

[79] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[80] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
