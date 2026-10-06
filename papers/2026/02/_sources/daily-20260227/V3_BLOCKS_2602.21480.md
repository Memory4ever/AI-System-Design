[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Both Ends Count! Just How Good are LLM Agents at Text-to-“Big SQL”?

[3] h6: Abstract.

[4] p: Text-to-SQL and Big Data are both extensively benchmarked fields, yet there is limited research that evaluates them jointly. In the real world, Text-to-SQL systems are often embedded with Big Data workflows, such as large-scale data processing or interactive data analytics. We refer to this as “Text-to-Big SQL” . However, existing text-to-SQL benchmarks remain narrowly scoped and overlook the cost and performance implications that arise at scale. For instance, translation errors that are minor on small datasets lead to substantial cost and latency overheads as data scales, a relevant issue completely ignored by text-to-SQL metrics.

[5] p: In this paper, we overcome this overlooked challenge by introducing novel and representative metrics for evaluating Text-to-Big SQL. Our study focuses on production-level LLM agents, a database-agnostic system adaptable to diverse user needs. Via an extensive evaluation of frontier models, we show that text-to-SQL metrics are insufficient for Big Data. In contrast, our proposed text-to-Big SQL metrics accurately reflect execution efficiency, cost, and the impact of data scale. Furthermore, we provide LLM-specific insights, including fine-grained, cross-model comparisons of latency and cost.

[6] h6: Keywords:

[7] h2: 1. Introduction

[8] p: Text-to-SQL is a longstanding problem in NLP that seeks to bridge natural language (NL) interfaces and structured query generation. Recent advances in production Large Language Models (LLMs) have substantially improved cross-domain performance, placing them as effective text-to-SQL engines ( Anthropic, 2024 ; OpenAI, 2025 ; Chung et al., 2025 ) that can generalize across varying data schemas and terminology, improving state-of-the-art results ( Zhu et al., 2024 ; Li et al., 2024 ) .

[9] p: In practice, this generalization ability is further enhanced via the integration of AI agents, which act as task-specific LLM scaffolds to iteratively inspect database schemas, refine SQL generation, validate SQL syntax, enabling text-to-SQL execution to adapt to the unique traits of user-specific data sources ( Sapkota et al., 2026 ) . Precisely, the existing ecosystem of open-source stacks for agent implementation ( Microsoft, 2024 ; LangChain, 2026 ; crewAI, 2026 ) , combined with the current state of production LLMs ( Anthropic, 2024 ; OpenAI, 2025 ; Chung et al., 2025 ) , has made text-to-SQL systems more accessible than ever.

[10] p: However, when moving beyond traditional databases to Big Data systems, text-to-SQL faces additional complexities. For instance, systems such as Amazon Athena ( Amazon Web Services, Inc., 2026a ) enable interactive analytics on massive datasets without requiring ETL, supporting various formats (CSV, JSON, ORC, Avro) and serverless, on-demand execution. In Big Data systems such as Athena, focusing only on the text-to-SQL end is not enough. The Big Data end itself introduces critical constraints that directly affect overall performance and cost. First, incorrect SQL has amplified consequences: failed queries can consume substantial compute resources, scan massive volumes of data, and increase execution costs, making accuracy essential not only for correctness but also for efficiency. For instance, ( Koutsoukos et al., 2025 ) report that running TPC-H benchmark at a moderate scale factor of 100 100 on Amazon Athena using Parquet data takes 132.3 132.3 seconds, illustrating how failed queries can sharply increase execution time and costs in Big Data environments.

[11] p: Second, inefficiencies can arise not only from failed queries but also from the SQL generation process itself. In agentic text-to-SQL, the LLM instructs the agent to use structured tools to inspect schemas and extract data-specific traits ( Deng et al., 2025 ; Xie et al., 2024 ; Zhang et al., 2024b ) . While this enables context-aware query adaptation, the reasoning overhead and tool orchestration can increase latency, making efficient SQL generation critical in Big Data systems. Simply put, if SQL generation becomes slower than physical query execution, interactive analysis may become impractical, undermining the performance gains of decades of optimizations in Query-as-a-Service (QaaS) engines like Athena and BigQuery ( Google Cloud, 2026a ) .

[12] p: Overall, these reasons lead to the following observation:

[13] h3: 1.1. Why Current Text-to-SQL Approaches Fall Short for Big Data?

[14] p: Traditional text-to-SQL methods have largely been evaluated on moderate-scale relational databases, focusing on query translation or isolated accuracy metrics ( Lei et al., 2025 ; Li et al., 2024 ; Zhang et al., 2024a ; Deochake and Mukhopadhyay, 2025 ) . While these benchmarks provide insights into LLM capabilities, they often overlook the complexities of interactive execution, streaming data, and cost considerations ( Cheng et al., 2025 ) .

[15] p: One example of this is that many text-to-SQL benchmarks use binary correctness metrics, tagging each generated query with a simple 0 0 / 1 1 label, thereby diluting degrees of partial correctness ( Li et al., 2023 ; Zhang et al., 2024a ) . This is obvious, for example, when a generated query incorrectly projects an unnecessary column. In traditional text-to-SQL this counts as a wrong translation, but in text-to-Big SQL it should be partially acceptable, since re-running a query for a single extra column could be extremely costly. Consequently, new evaluation metrics are needed to jointly account for partial correctness and cost, reflecting practical text-to-SQL performance for Big Data.

[16] p: While LLMs are effective text-to-SQL processors ( Li et al., 2025b ; Li et al., 2024 ) , their performance depends on how agents scaffold tool use ( Sapkota et al., 2026 ; Yao et al., 2023 ) . In a ReAct-style framework, the LLM controller guides reasoning, selects tools, and interprets feedback, while the executor runs the tools. Fast tools, such as fetching a table schema from a data catalog can be bottlenecked by extensive LLM reasoning for query validation, or vice versa. Efficient interaction between LLM, agent, and tools is thus critical for responsive interactive analytics. However, there are no evaluations that focus on this interplay and its effect on Big Data performance. In this paper, we start addressing this gap by jointly measuring agent and tool utilization, reasoning latency, and downstream query execution.

[17] h3: 1.2. Our Contribution

[18] p: In this work, we propose a benchmarking methodology for text-to-Big SQL agents that treats both ends, namely query generation and execution, as first-class citizens. We focus on zero-shot LLM agents to examine a worst-case scenario where no specific fine-tuning or additional optimization is applied, revealing the true impact of SQL generation, agent action, and tool interaction on performance and cost in Big Data settings. Our contributions are the following:

[19] p: A novel evaluation framework for text-to-SQL agents designed to capture big query execution. We propose new metrics that jointly assess agent action, reasoning latency, and the cost-effectiveness of generated queries, reflecting both partial correctness and the practical implications of running queries on Big Data engines.

[20] p: A systematic evalution of state-of-the-art LLMs within a unified ReAct-style agent architecture. This analysis reveals insights beyond accuracy, identifying scenarios where newer models achieve high correctness but are less interactive due to reasoning or tool orchestration overhead, which happens for instance with Opus 4.6.

[21] p: A discussion of the unique challenges, as well as open research questions in text-to-Big SQL, including the interplay between SQL generation, agent tool use, and execution performance, an area largely overlooked by existing benchmarks.

[22] h2: 2. Text-to-Big SQL Demands New Metrics

[23] h3: 2.1. Limitations of Current Metrics

[24] p: Typically, a text-to-SQL benchmark suite comprises a set of triples containing a natural language (NL) query, a golden query in SQL, and a ground truth ( V n V^{n} ) result ( Li et al., 2023 ) . During evaluation, system performance is measured by comparing the generated SQL to the golden query, and the resulting output ( V ^ n \hat{V}^{n} ) to V n V^{n} . Overall accuracy is then computed by aggregating these comparisons across the benchmark suite using standard evaluation metrics, such as Exact Matching (EM), Execution Accuracy (EA), and Valid Efficiency Score (VES) ( Hong et al., 2025 ; Zhu et al., 2024 ; Luo et al., 2025 ) .

[25] p: The major limitation of these metrics is their reliance on all-or-nothing correctness 2 2 2 The corresponding formulas are provided in the Appendix. . In practice, however, a generated query may deviate from the expected result without being entirely invalid, provided that end users may still be able to determine its correctness through simple validation, for example, by detecting an additional column in the projected output. We summarize the possible outcomes of an SQL execution as follows:

[26] p: Incorrect row count : The result is invalid due to poor SQL translation, for example, mis-specified WHERE conditions or inappropriate join types ( INNER , LEFT , etc.), leading to an incorrect number of rows. Such silent failures may remain unnoticed by the user, but always need a new translation and re-execution cycle to ensure correctness.

[27] p: Missing columns : The result is invalid due to omission of mandatory attributes in the projection list, requiring query re-execution to retrieve the complete output by adding the missing attributes in the SELECT clause.

[28] p: Superfluous columns : The result is valid, as we assume that experienced users can manually drop the extra columns without modifying the returned output, which is very cheap and fast. For instance, df.drop(‘‘extra_col’’) returns a new DataFrame without the extra column in Spark ( The Apache Software Foundation, 2026 ) . However, processing superfluous data affects execution performance and cost and should be penalized in the assessment.

[29] h3: 2.2. Proposed Metrics

[30] p: To encode our notion of correctness in a measurable metric, we extend the standard text-to-SQL VES metric to account for superfluous columns. Specifically, to quantify the overhead introduced by including irrelevant columns, we compute the column-level precision: P ⁡ ( S , S ^ ) = | columns in ​ S ∩ columns in ​ S ^ | | S ^ | P(S,\hat{S})=\frac{|\text{columns in }S\cap\text{columns in }\hat{S}|}{|\hat{S}|} , where S S is the set of ground-truth columns and S ^ \hat{S} is the set of columns in the execution result. This captures the fraction of retrieved columns that are actually relevant, penalizing extra, unnecessary columns without discarding partially correct results ( C ).

[31] p: Also, our new metric considers the total end-to-end (e2e) time ( T e2e T_{\text{e2e}} ), which includes all back-and-forth interactions between the LLM and the agent, the execution of interim tools, as well as the time required to run the generated SQL query on the underlying Big Data engine. Combining both concepts, we propose the novel text-to-Big SQL metric called VES ∗ \mathrm{VES}^{*} , which is defined as follows for N N queries:

[32] table: (1) VES ∗ = 1 N ​ ∑ i = 1 N ( 𝟙 ​ ( V i , V ^ i ) ⋅ P ⁡ ( S i , S ^ i ) ⋅ T g ​ o ​ l ​ d T e ​ 2 ​ e ) , \mathrm{VES}^{*}=\frac{1}{N}\sum_{i=1}^{N}\left(\mathds{1}(V_{i},\hat{V}_{i})\cdot P(S_{i},\hat{S}_{i})\cdot\frac{T_{gold}}{T_{e2e}}\right),

[33] p: where T g ​ o ​ l ​ d T_{gold} denotes the execution time of the golden query, and 𝟙 ​ ( V i , V ^ i ) \mathds{1}(V_{i},\hat{V}_{i}) is an indicator function that tells whether the output of the generated query matches the expected output ( A and B ):

[34] table: (2) 𝟙 ​ ( V , V ^ ) = { 1 , if V ^ is contained in expected output V 0 , otherwise , \mathds{1}(V,\hat{V})=\begin{cases}1,&\text{if $\hat{V}$ is contained in expected output $V$}\\ 0,&\text{otherwise}\end{cases},

[35] p: We also introduce the Valid Cost-Efficiency Score (VCES), a cost-oriented derivative of VES ∗ \text{VES}^{*} to account for the overall execution cost C e2e C_{\text{e2e}} , including the iterative interactions between the LLM and agent, the execution of agent-invoked tools, and the runtime of the generated query on the Big Data engine. For text-to-Big SQL, benchmarking query execution cost is relevant, particularly in cloud deployments:

[36] table: (3) VCES = 1 N ​ ∑ i = 1 N ( 𝟏 ​ ( V i , V ^ i ) ⋅ P ⁡ ( S i , S ^ i ) ⋅ T g ​ o ​ l ​ d T e ​ 2 ​ e C e ​ 2 ​ e ) . \text{VCES}=\frac{1}{N}\sum_{i=1}^{N}\left(\frac{\mathbf{1}(V_{i},\hat{V}_{i})\cdot P(S_{i},\hat{S}_{i})\cdot\frac{T_{gold}}{T_{e2e}}}{C_{e2e}}\right).

[37] p: To complement the previous metrics, we introduce the Expected Cost per Valid Query (CVQ), which quantifies the anticipated cost to obtain a valid result under a retry-until-success strategy. Let p p denote the single-shot validity rate, that is, the fraction of generated big queries that are valid. Consequently, the expected number of attempts until success follows a geometric distribution with mean 1 / p 1/p . Accordingly, we define C ​ V ​ Q = C e2e p CVQ=\frac{C_{\text{e2e}}}{p} .

[38] h2: 3. AI Agent Design

[39] p: To evaluate the novel text-to-Big SQL paradigm, we use a ReAct (Reasoning + Acting) agent ( Yao et al., 2023 ) , a well-established framework ( Sapkota et al., 2026 ; Starace et al., 2025 ; Liu et al., 2025 ) , which decomposes agentic operation into three intertwined components: Thought , Action , and Observation . Via Thought , the agent reasons about the task and decides its next step; through Action , it interacts with the environment or an external tool to gather or process information; and through Observation , it interprets feedback from these actions to refine subsequent reasoning steps.

[40] p: We deliberately keep the agent simple to provide a broader perspective in our analysis. While more complex AI agents exist ( Li et al., 2025a ) , we opt to leverage the long-context capabilities of production LLMs guided by iterative cycles of Thought, Action, and Observation, which has already demonstrated its effectiveness in text-to-SQL tasks ( Chung et al., 2025 ) .

[41] p: We define the controller as the connected LLM that guides ReAct-style reasoning, decides when and how to use tools, and produces the final answer. Conversely, the executor is the program that connects the LLM with external tools and handles the execution loop. We illustrate the architecture and execution loop of the agent in the Appendix.

[42] p: For the downstream query engine, we choose Spark SQL ( The Apache Software Foundation, 2026 ) due to its widespread adoption for large-scale structured data analysis. The controller interacts with the Spark session through a set of four tools, whose specifications are fully inserted into the context in a zero-shot manner ( Hsieh et al., 2023 ) . We define the tools as follows:

[43] p: list_tables : Look up the Spark Catalog ( Apache Software Foundation, 2026 ) to retrieve available tables by executing a SHOW TABLES statement.

[44] p: get_schema : Retrieve the schema for one or more tables from the Spark Catalog using SHOW CREATE TABLE t . Optionally, the controller can fetch an adjustable number of sample rows from each table with the same tool call, which triggers an additional SELECT * FROM t statement.

[45] p: check_query : Verify the syntax of a proposed query using predefined heuristics ( Chung et al., 2025 ) using a connected LLM (the checker ). While we use the same LLM for both the checker and the controller, they can be different.

[46] p: run_query : Execute a SQL query in the connected Spark Session, regardless of whether the deployment is local or cluster-based.

[47] p: To prevent the model from iteratively correcting and re-running queries, we terminate the agent immediately after the first run_query execution. We take this design decision because, in Big Data systems, unrestricted execution loops can lead to excessive resource consumption or high billing costs, and may even result in stuck-in-the-loop ( Cheng et al., 2025 ) scenarios without improving the accuracy of the inferred query.

[48] p: We base our implementation on the original LangChain Spark SQL Toolkit ( LangChain Inc., 2026 ) but port it to LangGraph ( LangChain Inc., 2024 ) . We utilize the LangChain stack because it is actively maintained ( LangChain, 2026 ) and frequently serves as a research baseline ( Ding and Stevens, 2025 ; Bhagat et al., 2025 ; Ma et al., 2025 ) .

[49] h2: 4. Evaluation

[50] p: Our evaluation proceeds as follows. § 4.1 shows that text-to-SQL metrics lack informativeness, revealing opportunities from fine-grained agent benchmarking. § 4.2 demonstrates the superior discriminability of text-to-Big SQL versus text-to-SQL metrics in differentiating agents across latency and cost objectives. Finally, § 4.3 shows data scale matters and that its impact can be quantified via text-to-Big SQL metrics. We employ two benchmarks: a text-to-SQL-focused one and a Big Data-focused one.

[51] p: BIRD ( Li et al., 2023 ) , a text-to-SQL benchmark that assesses translation accuracy for realistic databases.

[52] p: TPC-H ( Transaction Processing Performance Council, 2024 ) , a classic data analytics benchmark that measures database performance on complex ad-hoc business queries over relational data. TPC-H is very useful for text-to-Big SQL because it allows for the deterministic scaling of data.

[53] p: We conducted all experiments on an AWS m5.xlarge EC2 ( Amazon Web Services, Inc., 2026b ) instance in the us-east-1 region. We selected a set of representative frontier models from various providers for the evaluation. For all Large Language Models (LLMs), we used the official provider APIs and calculated costs based on their respective per-token pricing.

[54] p: To ensure consistency for interactive use, all models are deployed with low-latency reasoning configurations. We standardize sampling hyperparameters, such as temperature, top- p p , and maximum token limits, across all APIs, except where specific parameters are not exposed by the provider. These configurations are detailed in the Appendix.

[55] h3: 4.1. Accuracy is Not Enough in Text-to-Big SQL

[56] p: When models achieve similar accuracy, standard text-to-SQL metrics fail to differentiate between setups. We prove this by inspecting the Execution-based Focused Evaluation (EX) ( Lei et al., 2025 ) , a SOTA text-to-SQL accuracy metric. Since text-to-SQL performance continues to improve independently ( Hong et al., 2025 ) , we design a practical testbed assuming near-perfect accuracy. To this end, we select eight queries from the BIRD dataset where all tested models (except the later-added GPT-5.2) attain an average EX of at least 0.85.

[57] p: EX and e2e execution time alone lack the informativeness to discriminate models effectively. Figure 1 shows this: for faster models, the accuracy/speed tradeoff is unclear: e.g., is GPT-4o better than Gemini 3 Flash (27.79% faster but imperfect accuracy)? If wrong-query costs are high, a slightly slower but more accurate model may be preferable in production .

[58] p: Later-generation models do not clearly outperform their predecessors in zero-shot agentic text-to-SQL. For example, Opus 4.6 achieves perfect accuracy but takes 92.37% longer execution time than GPT-4o. Similarly, Gemini 3 Pro exhibits poor latency, further exacerbated by high variance from API instabilities. Notably, GPT-4o was released in 2024, nearly two years before the other two models.

[59] figure: Table 1 . EX, total execution time and the breakdown of execution time per "Observation-Thought-Action" stage for each LLM, on selected BIRD queries. Results are displayed in descending order of total execution time. Model EX E2E (s) % of E2E Time Mean σ \sigma list schema check run GPT-4o 0.93 6.55 2.08 9.22 13.15 62.08 13.64 Gemini 3 Flash 1.00 8.37 2.61 9.74 10.15 66.76 11.71 GPT-5.2 0.69 8.44 2.74 13.18 21.36 48.88 14.88 Gemini 2.5 Flash 0.95 9.18 3.21 11.70 10.53 66.07 10.11 Claude Opus 4.5 1.00 11.40 2.82 16.90 18.57 42.32 20.93 Claude Opus 4.6 1.00 12.60 2.09 17.18 18.11 42.70 20.93 Kimi K2.5 0.98 13.61 5.72 9.99 14.35 62.89 11.74 GPT-5 0.88 15.45 8.63 7.91 11.09 72.04 7.98 GLM-5 1.00 79.63 50.57 11.77 10.60 66.91 10.53 Gemini 3 Pro 1.00 115.95 159.97 18.29 19.70 46.82 14.33

[60] p: For better observability, we breakdown execution time, aggregating Observation-Thought-Action iterations that call the same tool into the stage abstraction. Common patterns emerge across models: the check_query stage dominates end-to-end time in all LLMs, as expected since it runs within the LLM rather than the local Spark session. Yet percentages vary widely (e.g., a 23% spread between GPT-5 and GPT-5.2).

[61] p: These results suggest stage-specific optimization via model selection. For instance, the time split between list_tables and run_query differs by model. Overall, smart per-stage model assignment (as in model ensembles ( Cheng et al., 2025 ) ) offers clear optimization potential .

[62] h3: 4.2. Big SQL Metrics Zoom In on Performance

[63] p: In the context of Big Data, text-to-SQL metrics fail to inform model selection. Instead, a Big SQL lens differentiates LLMs more clearly, providing sharper selection criteria. Table 2 shows normalized VES and VES* with respect to the best scoring LLM setup: GPT-4o. As seen in the table, VES* better discriminates accurate models (809.09% dispersion range vs. 54.93% in VES) .

[64] p: VES considers only query execution time and result accuracy ( Hong et al., 2025 ) . However, modern LLMs excel at text-to-SQL: their generated queries often functionally resemble the gold query (even if not identical) yielding similar execution times. At high accuracy levels, this hinders model discrimination, underscoring the role of precision and agent execution time.

[65] figure: Table 2 . VES and VES* for the selected BIRD queries. Both metrics are normalized to the best scoring LLM. LLMs are displayed in descending order of VES*. Model VES (norm) VES* (norm) Time Variation (x) list schema check run GPT-4o 1.00 1.00 1.00x 1.00x 1.00x 1.00x Gemini 3 Flash 1.06 0.81 1.35x 0.99x 1.37x 1.10x Gemini 2.5 Flash 1.00 0.78 1.78x 1.12x 1.49x 1.04x Claude Opus 4.5 1.09 0.57 3.19x 2.46x 1.19x 2.67x Claude Opus 4.6 1.09 0.51 3.58x 2.65x 1.32x 2.95x GPT-5 0.89 0.46 2.02x 1.99x 2.74x 1.38x Kimi K2.5 1.05 0.45 2.25x 2.27x 2.10x 1.79x GPT-5.2 0.71 0.39 1.84x 2.09x 1.01x 1.41x Gemini 3 Pro 1.10 0.33 35.12x 26.52x 13.35x 18.61x GLM-5 1.05 0.11 15.52x 9.81x 13.10x 9.39x

[66] p: A high VES* effectively reflects both accurate and low latency models , ranking GPT-4o highest (Table 2 ). It also reveals nuances, such as Opus models’ gains from perfect accuracy despite elevated execution times. Normalizing execution times to the fastest model (GPT-4o) shows it leads across all stages, suggesting a clear split between “fast” and “slow” models.

[67] figure: Table 3 . VCES and CVQ for the selected BIRD queries. The VCES values are normalized to the best-performing LLM, and models are shown in descending order of VCES. Model VCES norm. ( $ − 1 \$^{-1} ) CVQ ($) Cost Variation (x) list schema check run Gemini 3 Flash 1.00 0.0044 1.00x 1.00x 1.00x 1.00x Gemini 2.5 Flash 0.85 0.0053 1.36x 1.18x 1.12x 0.98x GPT-4o 0.55 0.0107 2.14x 2.93x 2.10x 2.64x Kimi K2.5 0.53 0.0047 1.07x 1.48x 0.99x 1.05x GPT-5.2 0.25 0.0124 2.62x 4.07x 1.42x 2.46x GPT-5 0.24 0.0118 1.92x 2.58x 2.55x 1.61x Claude Opus 4.5 0.08 0.0388 15.30x 16.13x 5.59x 15.76x Claude Opus 4.6 0.08 0.0359 14.39x 14.56x 5.22x 14.58x Gemini 3 Pro 0.07 0.0254 10.85x 11.21x 4.05x 7.07x GLM-5 0.05 0.0129 3.54x 3.06x 2.94x 2.63x

[68] p: VCES matches the dispersion range of VES* while incorporating cost, as it factors in per-token billing and the expenses of suboptimal query execution. Table 3 presents VCES per LLM and identifies Gemini 3 Flash as the most cost-efficient option due to its low per-token pricing 3 3 3 0.5 / 3.0 /3.0 per input/output token for Gemini 3 Flash ( Google, 2026 ) , vs. 2.5 / 10.0 /10.0 for GPT-4o ( OpenAI, 2026 ) . . Ultimately, VCES complements VES* by enabling the selection of cost-efficient configurations, thereby addressing a significant gap in text-to-SQL metrics that directly ignore cost . We attach CVQ to better support our finding: GPT-4o more than doubles the per-query cost of Gemini 3 Flash due to its lower accuracy, which leads to more failed queries and higher token consumption.

[69] p: As with execution time results, the leading cost performer in Table 3 dominates across nearly all stages. Mirroring the findings from VES*, there could be a separation of “cheap” and “expensive” models; the former may be particularly effective for stages with less stringent accuracy or latency requirements.

[70] h3: 4.3. The Aftermath of Data Scale

[71] p: Text-to-SQL metrics do not provide a representative picture of data scale. However, data scale plays a crucial role in text-to-Big SQL, as illustrated in Figure 1 . Two key observations emerge. First, as the scale increases, the relative importance of agent performance decreases, while SQL execution becomes more significant. Second, query failures at scale factors (SF) 10 and 1000 should be clearly distinguished; for example, executing an invalid Query 21 from TPC-H on the same cluster is 13.30 × 13.30\times more costly at scale factor 1000 than at scale factor 10.

[72] figure: Figure 1 . Breakdown of agent execution time (a) and cost (b) across different scale factors for TPC-H Query 21. Each bar series represents a specific model: Gemini 3 Pro (G), Claude Opus 4.5 (A), and GPT-5.2 (O).

[73] p: To investigate these concerns, we selected four TPC-H queries that LLMs struggle with (see Figure 2 ): complex ones (17, 18, 21) with nested subqueries, plus simpler Query 1 on a single table. We used TPC-H business questions as NL inputs and official SQL as ground truth (see Appendix for selection details). Tests ran on Amazon EMR ( Amazon Web Services, 2026 ) with r5b.xlarge master/core nodes, 32 core nodes (4 vCPUs each), and 128 GB gp3 EBS volumes.

[74] figure: Figure 2 . Average EX across three models for TPC-H queries 1, 17, 18, and 21.

[75] p: Text-to-SQL metrics data scale, as illustrated in Figure 3 . VES (which incorporates SQL execution time) yields constant relationships between models across scale factors. In contrast, SVQ better captures each model’s potential cost loss at varying scales: less accurate models (e.g., Gemini 3 Pro here) pose greater risk at large scale factors, where query errors incur substantially higher costs.

[76] p: Consequently, failing a query at SF 1000 is far more expensive than at SF 10. Even a modest accuracy gap (such as the 10% difference between Opus 4.5 and GPT-5.2) becomes critically amplified at higher scales.

[77] figure: (a) VES (b) SVQ Figure 3 . Text-to-SQL (a) and Text-to-Big SQL (b) metrics across three models and scale factors, averaged for TPC-H queries 1, 17, 18, and 21.

[78] p: Our evaluation clarifies the interpretation of Text-to-Big SQL metrics. VES* and VCES provide practical assessments at fixed scale factors, as they normalize generated SQL execution times and costs relative to the ground truth. In contrast, SVQ serves as an essential complement by quantifying the amplified impact of query inaccuracies as data scales.

[79] h2: 5. Discussion and Future Opportunities

[80] p: Based on our result, we identify several promising avenues in the broader text-to-Big SQL domain. Figure 4 summarizes our key insight: even if text-to-SQL reached 99% accuracy since natural language ambiguity is unavoidable, text-to-Big SQL challenges would still remain.

[81] figure: Figure 4 . Challenges of Text-to-Big SQL include, but are not limited to, those of Text-to-SQL.

[82] p: Agent performance tuning. Optimizing the internal stages of agents itself presents a significant research opportunity. Both our findings and prior work ( Cheng et al., 2025 ) demonstrate that both performance and cost could be improved by “strategically” assigning specialized models to different stages (e.g., navigating “fast” and‘ “cheap” models). However, existing physical plan optimization approaches for semantic operators incur latencies of tens of seconds ( Russo et al., 2026 ; Zhu et al., 2025 ) , making them incompatible with interactive analytics. Adapting these models to meet the latency constraints of interactive Big Data analytics remains a major open challenge.

[83] p: Text-to-SQL must be optimized for large-scale query execution. In Big Data, syntactically correct SQL may still be impractical if it triggers large shuffles, unnecessary joins, or full-table scans. Text-to-Big SQL must therefore optimize for both correctness and cost-efficient, large-scale execution, which remains an open challenge.

[84] p: One promising direction is to leverage historical execution traces enriched with performance metrics and system-level quality indicators, such as VCES and CVQ. By semantically matching newly generated queries ( Fu et al., 2023 ) to past executions ( Wang et al., 2025 ) , the system can estimate expected cost and runtime before execution and proactively rewrite inefficient queries ( Song et al., 2026 ; He et al., 2025 ) . Incorporating physical plans and cost models ( Baldacci and Golfarelli, 2019 ) further enables extrapolation across data scales, supporting scale-aware optimization rather than static SQL translation. Alternatively, the agent can be few-shot with similar past queries and their Big SQL metrics to infer optimized SQL.

[85] p: Beyond exact execution, Big Data systems often rely on approximate queries to trade precision for performance ( Chaudhuri et al., 2017 ) . However, current text-to-SQL models rarely reason about such semantic alternatives. A text-to-Big SQL framework should instead consider approximate joins, sampling-based aggregations, or sketch-based summaries when they satisfy user intent while significantly reducing execution cost. User-provided QoS annotations (e.g., “run this fast”) could further guide optimization.

[86] p: User-defined functions (UDFs). Another key challenge in text-to-Big SQL arises from UDFs. Big Data engines like Spark, Athena, and BigQuery often leverage custom UDFs, which are not fully expressible in standard SQL. As a result, text-to- Big SQL solutions must produce UDF-compatible SQL or hybrid code, for example, combining SQL with Spark DataFrames, which goes beyond classical text-to-SQL.

[87] h2: 6. Conclusion

[88] p: In this work, we address the surprisingly underexplored domain of “Text-to-Big SQL”: the integration of Text-to-SQL systems within Big Data workflows. We prove the shortcomings of Text-to-SQL benchmarking in this context and we propose tailored Text-to-Big SQL metrics that capture execution efficiency, cost and scaling effects.

[89] p: We evaluate state-of-the-art production LLMs to demonstrate that our metrics provide an effective framework for assessing Text-to-Big SQL performance and cost. Our contributions pave the way for promising real-world challenges and highlight avenues for integrating our findings into future research endeavors within Text-to-Big SQL.

[90] h6: Acknowledgements.

[91] h2: References

[92] h2: Appendix

[93] h2: Appendix A Related Work

[94] p: While other works address Big Data in text-to-SQL, they often overlook downstream analysis. Existing benchmarks focus on complex upstream data sources ( Lei et al., 2025 ; Li et al., 2024 ; Zhang et al., 2024a ) or isolate execution cost from accuracy ( Deochake and Mukhopadhyay, 2025 ; Zhang et al., 2024a ) . Others study LLM performance at scale but emphasize data diversity over job cost ( Li et al., 2025b ) . We target the gap in this domain, which is already a reality in production with tools like BigQuery’s Generative AI ( Google Cloud, 2026b ) .

[95] p: Non-binary accuracy metrics exist ( Lei et al., 2025 ; Pinna et al., 2025 ) , and some works apply similar logic to improve column linking ( Yuan et al., 2025 ) . However, we are the first to integrate this idea into the Big Data domain to account for their influence on SQL execution performance.

[96] p: LLMs are effective text-to-SQL processors ( Li et al., 2025b ; Li et al., 2024 ) , yet they require agent-based scaffolding to interact with user-specific databases ( Luo et al., 2025 ) . While some agents integrate with Big Data ( Ma et al., 2025 ) , their text-to-SQL effectiveness remains unevaluated. Conversely, current agent benchmarks ( Huo et al., 2025 ) neglect the query execution. This work introduces an evaluation framework that jointly assesses agent interactivity, accuracy and job performance.

[97] h2: Appendix B Text-to-SQL formulas

[98] p: A text-to-SQL benchmark suite includes a set of triples containing a natural language (NL) query, a golden query in SQL ( Q n Q^{n} ), and a ground truth ( V n V^{n} ) result ( Li et al., 2023 ) . During evaluation, system performance is measured by comparing the generated SQL ( Q ^ n \hat{Q}^{n} ) to the golden query, and the resulting output ( V ^ n \hat{V}^{n} ) to V n V^{n} ( Hong et al., 2025 ) .

[99] h3: B.1. Exact Matching (EM)

[100] table: (4) E ​ M = 1 N ​ ∑ i = 1 N 𝕀 ⁡ ( Q i , Q ^ i ) EM=\frac{1}{N}\sum_{i=1}^{N}\mathbb{I}\left(Q_{i},\hat{Q}_{i}\right)

[101] p: where

[102] table: (5) 𝕀 ⁡ ( Q i , Q ^ i ) = { 1 , Q i = Q ^ i 0 , Q i ≠ Q ^ i \mathbb{I}(Q_{i},\hat{Q}_{i})=\begin{cases}1,&Q_{i}=\hat{Q}_{i}\\ 0,&Q_{i}\neq\hat{Q}_{i}\end{cases}

[103] h3: B.2. Execution Accuracy (EA)

[104] table: (6) E ​ A = 1 N ​ ∑ i = 1 N 𝕀 ⁡ ( V i , V ^ i ) EA=\frac{1}{N}\sum_{i=1}^{N}\mathbb{I}\left(V_{i},\hat{V}_{i}\right)

[105] p: where

[106] table: (7) 𝕀 ⁡ ( V i , V ^ i ) = { 1 , V i = V ^ i 0 , V i ≠ V ^ i \mathbb{I}(V_{i},\hat{V}_{i})=\begin{cases}1,&V_{i}=\hat{V}_{i}\\ 0,&V_{i}\neq\hat{V}_{i}\end{cases}

[107] h3: B.3. Valid Efficiency Score

[108] table: (8) VES = 1 N ​ ∑ i = 1 N ( 𝕀 ⁡ ( V i , V ^ i ) ⋅ T g ​ o ​ l ​ d T g ​ e ​ n ) \text{VES}=\frac{1}{N}\sum_{i=1}^{N}\left(\mathbb{I}(V_{i},\hat{V}_{i})\cdot\frac{T_{gold}}{T_{gen}}\right)

[109] p: Where T g ​ o ​ l ​ d T_{gold} and T g ​ e ​ n T_{gen} are the execution times of the golden query and the generated SQL, respectively.

[110] h2: Appendix C BIRD evaluation

[111] h3: C.1. Model Selection

[112] p: We selected the models according to the following criteria: (1) current frontier models from Google, Anthropic, and OpenAI; (2) previous-generation frontier models from these same providers; and (3) the three open-source models with the highest scores on SWE-rebench 4 4 4 https://swe-rebench.com/ (all at the time of the experiment, mid-February 2026).

[113] h3: C.2. Detailed Results

[114] p: Our BIRD evaluation averages each metric over 50 iterations. Table 4 provides a detailed breakdown of the resulting Text-to-SQL and Text-to-Big SQL metrics per query and model.

[115] figure: Table 4 . Per-query BIRD metrics by model (mean ± \pm std across runs). VES, VES*, VCES and SVQ follow the paper definitions. Query ID Model EX VES VES* VCES SVQ 61 GPT-4o 1.00 ± \pm 0.00 1.0776 ± \pm 0.1609 0.0111 ± \pm 0.0040 1.1146 ± \pm 0.4623 0.0099 ± \pm 0.0008 GPT-5.2 1.00 ± \pm 0.00 0.9884 ± \pm 0.1617 0.0063 ± \pm 0.0022 0.6872 ± \pm 0.3280 0.0092 ± \pm 0.0019 Claude Opus 4.6 1.00 ± \pm 0.00 1.0577 ± \pm 0.1326 0.0060 ± \pm 0.0017 0.2045 ± \pm 0.0562 0.0296 ± \pm 0.0002 Gemini 3 Flash 1.00 ± \pm 0.00 1.0612 ± \pm 0.1561 0.0056 ± \pm 0.0019 0.9073 ± \pm 0.5326 0.0062 ± \pm 0.0016 Claude Opus 4.5 1.00 ± \pm 0.00 1.0707 ± \pm 0.1468 0.0055 ± \pm 0.0016 0.1368 ± \pm 0.0445 0.0401 ± \pm 0.0033 Kimi K2.5 1.00 ± \pm 0.00 1.0837 ± \pm 0.1747 0.0052 ± \pm 0.0013 1.1084 ± \pm 0.3150 0.0046 ± \pm 0.0004 DeepSeek Chat 0.86 ± \pm 0.35 0.9004 ± \pm 0.4139 0.0033 ± \pm 0.0018 1.7322 ± \pm 1.4172 0.0022 ± \pm 0.0002 Gemini 3 Pro 1.00 ± \pm 0.00 1.0892 ± \pm 0.1364 0.0031 ± \pm 0.0011 0.1487 ± \pm 0.0728 0.0210 ± \pm 0.0040 Gemini 2.5 Flash 0.60 ± \pm 0.49 0.6223 ± \pm 0.5169 0.0031 ± \pm 0.0030 0.4032 ± \pm 0.5152 0.0128 ± \pm 0.0017 GPT-5 1.00 ± \pm 0.00 1.0561 ± \pm 0.1747 0.0029 ± \pm 0.0009 0.2275 ± \pm 0.0848 0.0129 ± \pm 0.0017 GLM-5 1.00 ± \pm 0.00 1.0153 ± \pm 0.1511 0.0008 ± \pm 0.0004 0.0531 ± \pm 0.0435 0.0150 ± \pm 0.0056 606 Gemini 3 Flash 1.00 ± \pm 0.00 0.9771 ± \pm 0.0830 0.0115 ± \pm 0.0021 1.8689 ± \pm 0.6777 0.0062 ± \pm 0.0011 Claude Opus 4.5 1.00 ± \pm 0.00 1.0093 ± \pm 0.0652 0.0114 ± \pm 0.0012 0.3002 ± \pm 0.0452 0.0379 ± \pm 0.0012 Gemini 2.5 Flash 1.00 ± \pm 0.00 0.9724 ± \pm 0.0780 0.0112 ± \pm 0.0032 1.6157 ± \pm 1.1519 0.0069 ± \pm 0.0027 GPT-4o 0.52 ± \pm 0.50 0.5069 ± \pm 0.4884 0.0106 ± \pm 0.0114 1.0953 ± \pm 1.3342 0.0187 ± \pm 0.0013 Claude Opus 4.6 1.00 ± \pm 0.00 0.9840 ± \pm 0.0805 0.0103 ± \pm 0.0009 0.2953 ± \pm 0.0259 0.0349 ± \pm 0.0002 Kimi K2.5 1.00 ± \pm 0.00 0.9998 ± \pm 0.0674 0.0097 ± \pm 0.0016 2.1353 ± \pm 0.4786 0.0046 ± \pm 0.0005 DeepSeek Chat 0.92 ± \pm 0.27 0.8326 ± \pm 0.3136 0.0060 ± \pm 0.0019 2.8653 ± \pm 0.9997 0.0023 ± \pm 0.0002 GLM-5 1.00 ± \pm 0.00 0.9554 ± \pm 0.0817 0.0012 ± \pm 0.0006 0.0580 ± \pm 0.0723 0.0215 ± \pm 0.0087 Gemini 3 Pro 1.00 ± \pm 0.00 0.9385 ± \pm 0.1275 0.0012 ± \pm 0.0018 0.0358 ± \pm 0.1153 0.0342 ± \pm 0.0108 GPT-5.2 0.04 ± \pm 0.20 0.0212 ± \pm 0.1049 0.0007 ± \pm 0.0033 0.0849 ± \pm 0.4161 0.1979 ± \pm 0.0002 GPT-5 0.06 ± \pm 0.24 0.0312 ± \pm 0.1238 0.0003 ± \pm 0.0014 0.0228 ± \pm 0.1033 0.2526 ± \pm 0.0023 645 GPT-4o 1.00 ± \pm 0.00 0.9775 ± \pm 0.1205 0.0115 ± \pm 0.0030 1.3142 ± \pm 0.4871 0.0088 ± \pm 0.0011 GPT-5.2 1.00 ± \pm 0.00 0.9913 ± \pm 0.1306 0.0111 ± \pm 0.0017 1.9508 ± \pm 0.3330 0.0057 ± \pm 0.0002 Gemini 3 Flash 1.00 ± \pm 0.00 0.9947 ± \pm 0.0889 0.0097 ± \pm 0.0012 2.8552 ± \pm 0.5324 0.0034 ± \pm 0.0003 Gemini 2.5 Flash 1.00 ± \pm 0.00 0.9907 ± \pm 0.1083 0.0091 ± \pm 0.0013 2.3973 ± \pm 0.5125 0.0038 ± \pm 0.0004 Kimi K2.5 1.00 ± \pm 0.00 0.9993 ± \pm 0.0927 0.0060 ± \pm 0.0007 1.5733 ± \pm 0.2495 0.0038 ± \pm 0.0002 Claude Opus 4.5 1.00 ± \pm 0.00 0.9909 ± \pm 0.0996 0.0058 ± \pm 0.0008 0.1549 ± \pm 0.0223 0.0374 ± \pm 0.0007 GPT-5 1.00 ± \pm 0.00 0.9931 ± \pm 0.1166 0.0057 ± \pm 0.0013 0.7266 ± \pm 0.1910 0.0078 ± \pm 0.0004 Claude Opus 4.6 1.00 ± \pm 0.00 1.0188 ± \pm 0.1081 0.0055 ± \pm 0.0007 0.1604 ± \pm 0.0214 0.0341 ± \pm 0.0002 DeepSeek Chat 1.00 ± \pm 0.00 0.9986 ± \pm 0.0854 0.0037 ± \pm 0.0003 1.9634 ± \pm 0.2096 0.0019 ± \pm 0.0001 GLM-5 1.00 ± \pm 0.00 0.9793 ± \pm 0.0789 0.0014 ± \pm 0.0004 0.1458 ± \pm 0.0576 0.0094 ± \pm 0.0013 Gemini 3 Pro 1.00 ± \pm 0.00 0.9824 ± \pm 0.1100 0.0004 ± \pm 0.0003 0.0127 ± \pm 0.0690 0.0323 ± \pm 0.0128 776 GPT-4o 0.98 ± \pm 0.14 0.9596 ± \pm 0.2170 0.0090 ± \pm 0.0032 0.8559 ± \pm 0.3818 0.0107 ± \pm 0.0013 Gemini 3 Flash 1.00 ± \pm 0.00 0.9893 ± \pm 0.1598 0.0087 ± \pm 0.0017 2.1869 ± \pm 0.5540 0.0040 ± \pm 0.0006 Gemini 2.5 Flash 1.00 ± \pm 0.00 0.9971 ± \pm 0.1216 0.0083 ± \pm 0.0014 1.9412 ± \pm 0.4800 0.0043 ± \pm 0.0005 GPT-5.2 1.00 ± \pm 0.00 1.0895 ± \pm 0.1598 0.0064 ± \pm 0.0013 0.6279 ± \pm 0.2007 0.0102 ± \pm 0.0012 Claude Opus 4.5 1.00 ± \pm 0.00 1.0796 ± \pm 0.1737 0.0058 ± \pm 0.0009 0.1463 ± \pm 0.0236 0.0398 ± \pm 0.0002 Claude Opus 4.6 1.00 ± \pm 0.00 1.1299 ± \pm 0.1927 0.0051 ± \pm 0.0011 0.1362 ± \pm 0.0292 0.0373 ± \pm 0.0001 Kimi K2.5 0.96 ± \pm 0.20 0.9410 ± \pm 0.2426 0.0046 ± \pm 0.0014 0.9439 ± \pm 0.3565 0.0050 ± \pm 0.0008 GPT-5 1.00 ± \pm 0.00 1.0371 ± \pm 0.2007 0.0044 ± \pm 0.0010 0.4871 ± \pm 0.1361 0.0091 ± \pm 0.0008 DeepSeek Chat 0.50 ± \pm 0.50 0.4874 ± \pm 0.5029 0.0016 ± \pm 0.0017 0.7707 ± \pm 0.7466 0.0042 ± \pm 0.0001 GLM-5 1.00 ± \pm 0.00 1.1182 ± \pm 0.1901 0.0013 ± \pm 0.0003 0.1146 ± \pm 0.0379 0.0112 ± \pm 0.0027 Gemini 3 Pro 1.00 ± \pm 0.00 0.9586 ± \pm 0.0761 0.0004 ± \pm 0.0001 0.0109 ± \pm 0.0046 0.0330 ± \pm 0.0045 607 GPT-4o 1.00 ± \pm 0.00 0.9931 ± \pm 0.1001 0.0113 ± \pm 0.0031 1.3643 ± \pm 0.4998 0.0083 ± \pm 0.0012 Gemini 3 Flash 1.00 ± \pm 0.00 0.9754 ± \pm 0.0724 0.0091 ± \pm 0.0012 2.8852 ± \pm 0.5663 0.0032 ± \pm 0.0003 GPT-5.2 1.00 ± \pm 0.00 0.9578 ± \pm 0.0667 0.0090 ± \pm 0.0012 1.5754 ± \pm 0.3005 0.0057 ± \pm 0.0003 Gemini 2.5 Flash 1.00 ± \pm 0.00 0.9612 ± \pm 0.0611 0.0085 ± \pm 0.0011 2.4684 ± \pm 0.5187 0.0034 ± \pm 0.0004 Claude Opus 4.5 1.00 ± \pm 0.00 1.0013 ± \pm 0.1086 0.0056 ± \pm 0.0011 0.1576 ± \pm 0.0482 0.0358 ± \pm 0.0016 GPT-5 1.00 ± \pm 0.00 1.0077 ± \pm 0.1079 0.0053 ± \pm 0.0010 0.7238 ± \pm 0.1735 0.0073 ± \pm 0.0005 Kimi K2.5 1.00 ± \pm 0.00 0.9899 ± \pm 0.1223 0.0049 ± \pm 0.0008 1.2700 ± \pm 0.2678 0.0038 ± \pm 0.0003 Claude Opus 4.6 1.00 ± \pm 0.00 0.9798 ± \pm 0.0845 0.0046 ± \pm 0.0005 0.1372 ± \pm 0.0153 0.0338 ± \pm 0.0001 DeepSeek Chat 1.00 ± \pm 0.00 0.9787 ± \pm 0.0989 0.0036 ± \pm 0.0003 2.0750 ± \pm 0.2060 0.0017 ± \pm 0.0000 GLM-5 1.00 ± \pm 0.00 0.9850 ± \pm 0.0631 0.0015 ± \pm 0.0003 0.1741 ± \pm 0.0428 0.0085 ± \pm 0.0007 Gemini 3 Pro 1.00 ± \pm 0.00 1.0523 ± \pm 0.1248 0.0002 ± \pm 0.0001 0.0060 ± \pm 0.0029 0.0349 ± \pm 0.0042 785 Gemini 3 Flash 0.98 ± \pm 0.14 0.9794 ± \pm 0.2044 0.0072 ± \pm 0.0016 1.9708 ± \pm 0.5443 0.0037 ± \pm 0.0005 GPT-4o 0.90 ± \pm 0.30 0.8845 ± \pm 0.3341 0.0068 ± \pm 0.0051 0.6551 ± \pm 1.0487 0.0116 ± \pm 0.0034 GPT-5.2 1.00 ± \pm 0.00 0.5852 ± \pm 0.0956 0.0067 ± \pm 0.0012 0.8905 ± \pm 0.2136 0.0075 ± \pm 0.0008 Gemini 2.5 Flash 1.00 ± \pm 0.00 0.9617 ± \pm 0.1679 0.0066 ± \pm 0.0012 1.5462 ± \pm 0.3506 0.0043 ± \pm 0.0003 Gemini 3 Pro 1.00 ± \pm 0.00 1.0416 ± \pm 0.1996 0.0050 ± \pm 0.0040 0.1907 ± \pm 0.2120 0.0265 ± \pm 0.0084 Claude Opus 4.5 1.00 ± \pm 0.00 0.9943 ± \pm 0.1450 0.0046 ± \pm 0.0006 0.1168 ± \pm 0.0156 0.0392 ± \pm 0.0002 Kimi K2.5 1.00 ± \pm 0.00 0.9698 ± \pm 0.1714 0.0040 ± \pm 0.0009 0.8368 ± \pm 0.2027 0.0048 ± \pm 0.0004 Claude Opus 4.6 1.00 ± \pm 0.00 0.9938 ± \pm 0.1542 0.0038 ± \pm 0.0007 0.1054 ± \pm 0.0199 0.0365 ± \pm 0.0001 GPT-5 0.96 ± \pm 0.20 0.5326 ± \pm 0.1370 0.0038 ± \pm 0.0011 0.4073 ± \pm 0.1385 0.0097 ± \pm 0.0009 GLM-5 1.00 ± \pm 0.00 0.7441 ± \pm 0.2308 0.0011 ± \pm 0.0003 0.1135 ± \pm 0.0351 0.0101 ± \pm 0.0009 DeepSeek Chat 0.26 ± \pm 0.44 0.1633 ± \pm 0.2789 0.0006 ± \pm 0.0011 0.3938 ± \pm 0.4810 0.0063 ± \pm 0.0000 813 GPT-4o 0.98 ± \pm 0.14 1.4618 ± \pm 0.2675 0.0163 ± \pm 0.0049 1.5711 ± \pm 0.6311 0.0106 ± \pm 0.0014 Gemini 3 Pro 1.00 ± \pm 0.00 1.4871 ± \pm 0.2484 0.0150 ± \pm 0.0043 0.6948 ± \pm 0.2329 0.0215 ± \pm 0.0015 Gemini 3 Flash 1.00 ± \pm 0.00 1.4672 ± \pm 0.1450 0.0147 ± \pm 0.0045 3.2074 ± \pm 1.3323 0.0046 ± \pm 0.0008 GPT-5.2 1.00 ± \pm 0.00 1.4145 ± \pm 0.1573 0.0147 ± \pm 0.0019 1.8987 ± \pm 0.3136 0.0077 ± \pm 0.0010 Gemini 2.5 Flash 0.96 ± \pm 0.20 1.3410 ± \pm 0.3267 0.0119 ± \pm 0.0031 2.2072 ± \pm 0.7463 0.0056 ± \pm 0.0007 Claude Opus 4.5 1.00 ± \pm 0.00 1.5073 ± \pm 0.1882 0.0111 ± \pm 0.0018 0.2780 ± \pm 0.0465 0.0398 ± \pm 0.0001 Claude Opus 4.6 1.00 ± \pm 0.00 1.4065 ± \pm 0.1678 0.0086 ± \pm 0.0010 0.2246 ± \pm 0.0259 0.0381 ± \pm 0.0001 Kimi K2.5 0.94 ± \pm 0.24 1.3564 ± \pm 0.4013 0.0083 ± \pm 0.0026 1.5839 ± \pm 0.7307 0.0055 ± \pm 0.0013 GPT-5 1.00 ± \pm 0.00 1.4285 ± \pm 0.1680 0.0081 ± \pm 0.0011 0.7875 ± \pm 0.1343 0.0102 ± \pm 0.0007 GLM-5 1.00 ± \pm 0.00 1.5179 ± \pm 0.1824 0.0017 ± \pm 0.0009 0.1106 ± \pm 0.0876 0.0153 ± \pm 0.0039 DeepSeek Chat 0.18 ± \pm 0.38 0.2602 ± \pm 0.5612 0.0011 ± \pm 0.0024 0.8861 ± \pm 1.2098 0.0071 ± \pm 0.0000 895 GPT-4o 1.00 ± \pm 0.00 0.9521 ± \pm 0.0391 0.0731 ± \pm 0.0134 5.6117 ± \pm 1.6328 0.0130 ± \pm 0.0034 Gemini 2.5 Flash 1.00 ± \pm 0.00 0.9775 ± \pm 0.0408 0.0582 ± \pm 0.0089 10.1518 ± \pm 2.6428 0.0057 ± \pm 0.0009 Gemini 3 Flash 1.00 ± \pm 0.00 0.9624 ± \pm 0.0633 0.0542 ± \pm 0.0071 10.7101 ± \pm 2.2685 0.0051 ± \pm 0.0005 GPT-5 0.94 ± \pm 0.24 0.9035 ± \pm 0.2332 0.0374 ± \pm 0.0126 2.7033 ± \pm 1.1059 0.0147 ± \pm 0.0017 Gemini 3 Pro 1.00 ± \pm 0.00 0.9835 ± \pm 0.0725 0.0325 ± \pm 0.0062 1.2292 ± \pm 0.5011 0.0265 ± \pm 0.0071 Claude Opus 4.5 1.00 ± \pm 0.00 0.9504 ± \pm 0.0780 0.0325 ± \pm 0.0029 0.6086 ± \pm 0.0552 0.0534 ± \pm 0.0005 Claude Opus 4.6 1.00 ± \pm 0.00 0.9633 ± \pm 0.0758 0.0314 ± \pm 0.0021 0.6513 ± \pm 0.0443 0.0482 ± \pm 0.0003 Kimi K2.5 1.00 ± \pm 0.00 0.9716 ± \pm 0.0766 0.0239 ± \pm 0.0041 3.8241 ± \pm 1.1679 0.0063 ± \pm 0.0014 GLM-5 1.00 ± \pm 0.00 0.9824 ± \pm 0.0487 0.0073 ± \pm 0.0018 0.5158 ± \pm 0.1935 0.0141 ± \pm 0.0024 DeepSeek Chat 0.28 ± \pm 0.45 0.2648 ± \pm 0.4250 0.0059 ± \pm 0.0098 3.2359 ± \pm 3.9557 0.0065 ± \pm 0.0007 GPT-5.2 0.12 ± \pm 0.32 0.1108 ± \pm 0.3007 0.0049 ± \pm 0.0132 0.2930 ± \pm 0.8119 0.1386 ± \pm 0.0007 968 GPT-4o 1.00 ± \pm 0.00 0.9189 ± \pm 0.1193 0.0034 ± \pm 0.0009 0.3918 ± \pm 0.1327 0.0087 ± \pm 0.0010 Claude Opus 4.5 1.00 ± \pm 0.00 0.9280 ± \pm 0.1291 0.0030 ± \pm 0.0005 0.1208 ± \pm 0.0227 0.0250 ± \pm 0.0006 Gemini 2.5 Flash 1.00 ± \pm 0.00 0.9239 ± \pm 0.1139 0.0028 ± \pm 0.0004 0.8190 ± \pm 0.1684 0.0035 ± \pm 0.0004 Gemini 3 Flash 1.00 ± \pm 0.00 0.8686 ± \pm 0.1100 0.0028 ± \pm 0.0004 0.8079 ± \pm 0.1836 0.0034 ± \pm 0.0005 Claude Opus 4.6 1.00 ± \pm 0.00 0.9534 ± \pm 0.1726 0.0022 ± \pm 0.0006 0.0727 ± \pm 0.0182 0.0308 ± \pm 0.0060 Gemini 3 Pro 1.00 ± \pm 0.00 0.9264 ± \pm 0.1033 0.0019 ± \pm 0.0002 0.1159 ± \pm 0.0205 0.0167 ± \pm 0.0016 Kimi K2.5 0.96 ± \pm 0.20 0.8471 ± \pm 0.2204 0.0019 ± \pm 0.0008 0.5379 ± \pm 0.5124 0.0037 ± \pm 0.0004 GPT-5 0.96 ± \pm 0.20 0.8096 ± \pm 0.2532 0.0017 ± \pm 0.0006 0.2090 ± \pm 0.0933 0.0083 ± \pm 0.0010 DeepSeek Chat 0.74 ± \pm 0.44 0.6497 ± \pm 0.3990 0.0008 ± \pm 0.0005 0.4673 ± \pm 0.2764 0.0023 ± \pm 0.0000 GLM-5 0.98 ± \pm 0.14 0.9016 ± \pm 0.1775 0.0003 ± \pm 0.0001 0.0236 ± \pm 0.0119 0.0114 ± \pm 0.0021 GPT-5.2 0.04 ± \pm 0.20 0.0352 ± \pm 0.1723 0.0001 ± \pm 0.0006 0.0212 ± \pm 0.1134 0.1509 ± \pm 0.0000

[116] h2: Appendix D TPC-H evaluation

[117] h3: D.1. Model and Query Selection

[118] p: We selected three last generation frontier models available at the time of our original experiments in January 2026: Gemini 3 Pro, Claude Opus 4.5, and GPT-5.2. We excluded additional models due to budget constraints, as a single TPC-H query run at the specified scale factor costs approximately $1 within our proposed EMR cluster. Given 50 replicas per model and the orginal set of 10 models from the BIRD evaluation, the total cost for four TPC-H queries would reach roughly $2,000, excluding lower scale factor tests. Because an exhaustive assessment of all available models and queries would not further clarify the primary contributions of this paper, we limited this evaluation to a representative subset.

[119] p: Regarding query selection, we prioritized TPC-H queries that Claude Opus 4.5 could not translate correctly. We then verified that (1) accuracy remained imperfect in the other two models and (2) no model had memorized the TPC-H specification during training. While methods exist to prove memorization in production Large Language Models (LLMs), verifying the absolute absence of memorization remains an open challenge. As a workaround, we adapted the methodology from ( Ahmed et al., 2026 ) , implementing the code at https://github.com/GEizaguirre/memorization-LLM-prod , and attempted to detect TPC-H memorization in the models; however, these efforts were unsuccessful.

[120] h2: Appendix E Detailed Results

[121] p: Our TPC-H evaluation averages each metric over 50 iterations at scale factor 1. Table 5 provides a detailed breakdown of the resulting Text-to-SQL and Text-to-Big SQL metrics for each query and model.

[122] figure: Table 5 . Per-query TPC-H (SF1) metrics by model (mean ± \pm std across runs). VES, VES*, and VCES follow the paper definitions; SVQ reports the expected cost per valid query. Query ID Model EX VES VES* VCES SVQ 1 GPT-5.2 0.60 ± \pm 0.49 0.6507 ± \pm 0.5318 0.2608 ± \pm 0.2134 23.1794 ± \pm 19.0188 0.0188 ± \pm 0.0000 Claude Opus 4.5 1.00 ± \pm 0.00 0.9567 ± \pm 0.1057 0.2513 ± \pm 0.0138 3.6030 ± \pm 0.2671 0.0697 ± \pm 0.0015 Gemini 3 Pro (T) 0.00 ± \pm 0.00 0.0000 ± \pm 0.0000 0.0000 ± \pm 0.0000 0.0000 ± \pm 0.0000 – 17 Claude Opus 4.5 0.20 ± \pm 0.40 0.2028 ± \pm 0.4235 0.0323 ± \pm 0.0647 0.3865 ± \pm 0.6072 0.4182 ± \pm 0.0025 Gemini 3 Pro (T) 0.10 ± \pm 0.30 0.1294 ± \pm 0.3883 0.0140 ± \pm 0.0420 0.3525 ± \pm 0.7373 0.3973 ± \pm 0.0000 GPT-5.2 0.40 ± \pm 0.49 0.0000 ± \pm 0.0000 0.0000 ± \pm 0.0000 0.0000 ± \pm 0.0000 0.0168 ± \pm 0.0004 18 Gemini 3 Pro (T) 1.00 ± \pm 0.00 1.3223 ± \pm 0.1182 0.2449 ± \pm 0.0232 6.4131 ± \pm 0.8326 0.0382 ± \pm 0.0019 GPT-5.2 0.40 ± \pm 0.49 0.2206 ± \pm 0.6619 0.0711 ± \pm 0.2133 7.5480 ± \pm 17.8560 0.0236 ± \pm 0.0030 Claude Opus 4.5 0.00 ± \pm 0.00 0.0000 ± \pm 0.0000 0.0000 ± \pm 0.0000 0.0000 ± \pm 0.0000 – 21 Claude Opus 4.5 0.80 ± \pm 0.40 0.7732 ± \pm 0.3889 0.2639 ± \pm 0.1321 2.8673 ± \pm 1.7429 0.1150 ± \pm 0.0003 GPT-5.2 0.20 ± \pm 0.40 0.0000 ± \pm 0.0000 0.0000 ± \pm 0.0000 0.0000 ± \pm 0.0000 0.0915 ± \pm 0.0000 Gemini 3 Pro (T) 0.00 ± \pm 0.00 0.0000 ± \pm 0.0000 0.0000 ± \pm 0.0000 0.0000 ± \pm 0.0000 –

[123] p: We then execute the generated SQL queries across different scale factors and average the proposed metrics for all queries. These results are shown in Table 6 .

[124] figure: Table 6 . TPC-H metrics aggregated by scale factor (mean ± \pm std across models and queries). Scale Factor VES VES* VCES SVQ SF10 0.1701 ± \pm 0.0689 0.0731 ± \pm 0.0264 0.7768 ± \pm 0.2230 0.2679 ± \pm 0.0992 SF100 0.0894 ± \pm 0.0368 0.0521 ± \pm 0.0198 0.3488 ± \pm 0.0794 0.3931 ± \pm 0.1484 SF1000 0.0158 ± \pm 0.0045 0.0139 ± \pm 0.0041 0.0244 ± \pm 0.0058 1.7746 ± \pm 0.6972

[125] h2: Instructions for reporting errors

[126] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[127] p: Tip: You can select the relevant text first, to include it in your report.

[128] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[129] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
