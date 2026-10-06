[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Evaluating Stochasticity in Deep Research Agents Thanks: Corresponding author: haotian.zhai@utexas.edu , leqiliu@utexas.edu

[3] h6: Abstract

[4] p: Deep Research Agents (DRAs) are promising agentic systems that gather and synthesize information to support research across domains such as financial decision-making, medical analysis, and scientific discovery. Despite recent improvements in research quality (e.g., outcome accuracy when ground truth is available), DRA system design often overlooks a critical barrier to real-world deployment: stochasticity . Under identical queries, repeated executions of DRAs can exhibit substantial variability in terms of research outcome, findings, and citations. In this paper, we formalize the study of stochasticity in DRAs by modeling them as information acquisition Markov Decision Processes. We introduce an evaluation framework that quantifies variance in the system and identify three sources of it: information acquisition, information compression, and inference. Through controlled experiments, we investigate how stochasticity from these modules across different decision steps influences the variance of DRA outputs. Our results show that reducing stochasticity can improve research output quality, with inference and early-stage stochasticity contributing the most to DRA output variance. Based on these findings, we propose strategies for mitigating stochasticity while maintaining output quality via structured output and ensemble-based query generation. Our experiments on DeepSearchQA show that our proposed mitigation methods reduce average stochasticity by 22% while maintaining high research quality.

[5] h2: 1 Introduction

[6] p: Deep Research Agents (DRAs) are a specialized class of LLM-driven agents designed for autonomous knowledge discovery [ 10 ] . By interleaving iterative tool execution with adaptive reasoning and planning [ 25 , 19 ] , these agents systematically retrieve and synthesize external data to fulfill complex, information-heavy research objectives [ 3 , 8 , 21 ] .

[7] p: However, the deployment of DRAs is hindered by a fundamental lack of reliability. The execution of a DRA involves an iterative cycle of search, reasoning, and synthesis, where minor generation or search variations can cascade into vastly different research conclusions. This stochasticity, manifesting as significant variability in research output, findings and citations across repeated executions of the same query, remains largely underexplored.

[8] p: The implications of this stochasticity span from general user experience to high-stakes professional applications, which depend largely on whether the user possesses the domain expertise to audit the system’s outputs. For lay users, DRAs are often used to inform day-to-day decisions – for example, medical information seeking. Lacking the expertise to verify the underlying evidence, these users often treat the DRA outputs as the ground truth. If a DRA provides conflicting advice on the safety of a medication across three different runs, the resulting stochasticity signals a lack of reliability, potentially leading to users following flawed advice. For professional users, the challenge is operational. In fields like pharmaceutical R&D or quantitative finance, DRAs are employed to automate high-volume workflows, such as synthesizing literature on protein folding or conducting systematic risk analyses. While these experts can differentiate between rigorous and unconvincing outputs, if a system produces a different risk profile for the same financial instrument each time it is queried, the expert must manually verify every execution. In this context, stochasticity transforms a tool meant for efficiency into a liability, as the time saved by automation is reclaimed by the necessity of rigorous validation.

[9] p: To quantify and analyze the stochasticity in DRAs, we first formalize the execution of a deep research agent as an information acquisition Markov Decision Process (MDP), in which the agent iteratively performs query generation (information acquisition), summarization (information compression), and reasoning (inference) to uncover a set of task-relevant atomic findings and citations to source documents. This formulation provides a unifying abstraction for analyzing DRA’s behavior across heterogeneous tasks and instantiations.

[10] p: Building on this formulation, we introduce a suite of metrics that characterize DRA stochasticity at multiple levels, including variability in final research outputs (e.g., answers), findings, and citation sources. These metrics enable fine-grained measurements that allow us to disentangle whether two runs disagree because they retrieve and cite different evidence, reason differently over the same evidence, or both.

[11] p: We then adopt a measurement framework grounded in variance decomposition that attributes stochasticity in DRA’s evolving knowledge state to two sources: (i) propagated stochasticity inherited from earlier states, and (ii) intrinsic stochasticity arising from the current decision modules. The intrinsic stochasticity term further decomposes into stochasticity from the information acquisition policy, the information compression policy, and the inference policy. This decomposition provides a conceptual lens for investigating where stochasticity enters the DRA system and how it compounds over time. We empirically validate this framework using temperature ablations that selectively increase sampling temperature for individual modules at specific time steps while keeping all other modules deterministic. This controlled analysis allows us to understand how stochasticity propagates in DRAs and why early-stage stochasticity dominates final output variance.

[12] p: Finally, guided by findings from temperature ablations, we study practical mitigation strategies that reduce stochasticity while preserving research output quality. By combining structured summarization and reasoning output with ensembling early-stage search queries, we demonstrate that average stochasticity can be successfully reduced by 22%, while the research output quality is maintained.

[13] p: The key contributions of this work are as follows:

[14] p: We identify the stochasticity problem and propose an information acquisition MDP formulation for deep research agents that supports principled analysis of stochasticity (Section 3 ).

[15] p: We introduce multi-level stochasticity metrics over answers, findings, and citations for evaluating stochasticity across executions (Section 4 ).

[16] p: We conceptually decompose DRA stochasticity into propagated and intrinsic stochasticity across agent modules (Section 5.1 ), and introduce temperature ablation experiments to empirically investigate how these naturally entangled sources of uncertainty propagate and affect the final output stochasticity (Section 5.2 ).

[17] p: We propose mitigation strategies that substantially reduce stochasticity without degrading answer accuracy (Section 6 ).

[18] h2: 2 Related Work

[19] p: Deep research and browsing agents. The evolution of Deep Research Agents (DRAs) stems from early Retrieval-Augmented Generation (RAG) systems, which utilized large corpora to enhance factual accuracy in knowledge-intensive question answering [ 12 , 5 ] . While initial efforts focused on short-form factoid synthesis [ 11 , 18 , 27 , 13 ] , these methods often lack the reasoning depth required for comprehensive reports [ 6 , 17 ] . Frameworks such as GPTResearcher [ 4 ] have bridged this gap by integrating agentic workflows for long-form generation, utilizing query decomposition and hierarchical planning to ensure completeness. Contemporary systems such as OpenDeepSearch [ 1 ] and Tongyi DeepResearch [ 19 ] further extend these capabilities by interleaving iterative action-observation cycles with external tool use, such as Python execution. Other work such as FlashResearch [ 16 ] also focuses on real-time agent orchestration, aiming at improve the efficiency of deep research agents. Collectively, these advancements transition AI from passive retrievers to autonomous agents capable of navigating complex, multi-stage research trajectories.

[20] p: Benchmarks and evaluation for DRAs. Early evaluations of research agents primarily relied on traditional Question Answering (QA) benchmarks [ 21 , 8 , 22 ] to assess performance based on direct retrieval accuracy. While effective for validating answer precision, these benchmarks often fail to capture the complexity of synthesizing comprehensive research reports. To address the demands of open-ended, long-horizon research, recent works have introduced specialized benchmarks [ 3 , 23 , 26 , 20 ] to evaluate deep research agents. These benchmarks move beyond simple accuracy, employing metrics based on content quality and factual reliability by decomposing final reports into atomic findings [ 14 ] and utilizing LLM-as-a-judge [ 7 ] to automate the assessment of the final report. Related work also develops specialized diagnostics for retrieval faithfulness and claim verification in DRA settings [ 2 ] . Mustahsan et al. [15] studies stochasticity of evaluation for agentic systems, proposing statistical reliable measures.

[21] p: Although these methodologies have significantly advanced our ability to measure content quality and factual reliability, none of them quantify stochasticity in DRAs across runs. Our work bridges this gap by introducing a systematic framework to evaluate the stochasticity, attributing stochasticity to different components, and proposing stochasticity mitigation methods in DRAs.

[22] h2: 3 Modeling Deep Research Agents

[23] p: We model a single execution run of a deep research agent as an information acquisition MDP . Let 𝒬 \mathcal{Q} denote the set of all problem instances (user queries). For a fixed instance q ∈ 𝒬 q\in\mathcal{Q} , let ℱ ⁡ ( q ) = { f 1 , … , f N } \mathcal{F}(q)=\{f_{1},\dots,f_{N}\} denote a finite universe of candidate atomic findings relevant to q q .

[24] p: At step t t , we track an abstract knowledge state 𝐛 t ∈ { 0 , 1 } N \mathbf{b}_{t}\in\{0,1\}^{N} , where 𝐛 t ​ [ k ] = 1 \mathbf{b}_{t}[k]=1 indicates that finding f k f_{k} is supported by the evidence acquired so far. We initialize 𝐛 0 = 𝟎 \mathbf{b}_{0}=\mathbf{0} . At each step, the agent either issues an information-seeking query or terminates. Let the action space be 𝒜 = 𝒮 ∪ { 𝚂𝚃𝙾𝙿 } \mathcal{A}=\mathcal{S}\cup\{\mathtt{STOP}\} , where 𝒮 \mathcal{S} is the set of allowable search queries. The agent samples an action

[25] table: a t ∼ π query ( ⋅ ∣ q , 𝐛 t ) , a_{t}\sim\pi_{\mathrm{query}}(\cdot\mid q,\mathbf{b}_{t}), (1)

[26] p: where π query \pi_{\mathrm{query}} is the query policy . If a t = 𝚂𝚃𝙾𝙿 a_{t}=\mathtt{STOP} the run terminates. Otherwise, the environment (e.g., a search engine) returns retrieved content (documents, snippets, metadata, etc.), modeled as an observation

[27] table: i t ∼ β env ( ⋅ ∣ a t ) , i_{t}\sim\beta_{\mathrm{env}}(\cdot\mid a_{t}), (2)

[28] p: where β env \beta_{\mathrm{env}} captures exogenous variability (e.g., dynamic content, API nondeterminism, etc.).

[29] p: Retrieved content is typically too large and heterogeneous to store directly, so the agent compresses it into an intermediate representation (notes, extracted claims, structured tables, etc.). We model this as

[30] table: h t ∼ π sum ( ⋅ ∣ q , 𝐛 t , i t ) , h_{t}\sim\pi_{\mathrm{sum}}(\cdot\mid q,\mathbf{b}_{t},i_{t}), (3)

[31] p: where π sum \pi_{\mathrm{sum}} is an information compression policy. Finally, the agent integrates the new compressed information to update its knowledge state via an inference policy:

[32] table: 𝐛 t + 1 ∼ π update ( ⋅ ∣ q , 𝐛 t , h t , a t ) . \mathbf{b}_{t+1}\sim\pi_{\mathrm{update}}(\cdot\mid q,\mathbf{b}_{t},h_{t},a_{t}). (4)

[33] p: A trajectory of length T T is therefore

[34] table: τ = ( 𝐛 0 , a 0 , i 0 , h 0 , 𝐛 1 , … , 𝐛 T ) , \tau=(\mathbf{b}_{0},a_{0},i_{0},h_{0},\mathbf{b}_{1},\dots,\mathbf{b}_{T}),

[35] p: terminating either by 𝚂𝚃𝙾𝙿 \mathtt{STOP} or a maximum horizon.

[36] p: This factorization isolates three key decision modules that are typically under the agent designer’s control:

[37] p: Information acquisition ( π query \pi_{\mathrm{query}} ): whether or what to retrieve (query generating and stopping).

[38] p: Information compression ( π sum \pi_{\mathrm{sum}} ): how retrieved content is distilled into a usable memory representation.

[39] p: Inference ( π update \pi_{\mathrm{update}} ): how the agent integrates accumulated evidence to update supported findings.

[40] p: The environment kernel β env \beta_{\mathrm{env}} may also be stochastic (e.g., dynamic web search). Our analysis framework assumes β env \beta_{\mathrm{env}} is held fixed (e.g., via cached or reproducible search).

[41] p: We can instantiate different DRA frameworks based on our modeling. In this work, we adopt ReAct [ 25 , 19 ] as a representative instantiation. In ReAct setup, the agent operates in a single, flat loop where the agent performs information acquisition, information compression and inference simultaneously. After “reasoning” about the current belief state (inference), the agent would “act” to generate search queries (information acquisition), and then uses another module to summarize the retrieved content (information compression) before “reasoning” of the next round begins. We also provide another instantiation example in Appendix C.1 .

[42] figure: Figure 1: Overview of the evaluation pipeline. The process begins with a user question which triggers multiple independent Deep Research Agent (DRA) runs (in this example we use number of runs k = 2 k=2 ). The resulting reports are decomposed into answers, findings, and citations, and then clustered. After clustering, each report’s answers, findings, and citations are mapped to binary vectors and normalized to compute the Total Variance (TV) as a measure of stochasticity. We expand findings as an example to illustrate the whole process. In reality, answers and citations are also processed in similar ways as in Section 4 .

[43] h2: 4 Evaluation Framework for DRA Stochasticity

[44] p: We quantify stochasticity by running the same agent n n times on the same instance q q under identical configuation, producing trajectories 𝒯 = { τ ( 1 ) , … , τ ( n ) } \mathcal{T}=\{\tau^{(1)},\dots,\tau^{(n)}\} and final reports { r ( 1 ) , … , r ( n ) } \{r^{(1)},\dots,r^{(n)}\} . For each report, we extract three objects of interest: (i) an answer (when a verifiable answer exists), (ii) a set of atomic findings, and (iii) a set of citations (URLs). We then cannonicalize these objects across runs and map each run to a vector representation that enables a unified variance-based metric.

[45] p: We have three random vectors of interest: the answer 𝐘 \mathbf{Y} , the citations 𝐂 \mathbf{C} , and the findings 𝐁 \mathbf{B} . They are all categorical distributions and can be represented in similar ways. Note that for open-ended questions, we lack answers 𝐘 \mathbf{Y} . Thus, in the following, we model the agent’s output as a realization of a random vector 𝐗 ∈ { 0 , 1 } d \mathbf{X}\in\{0,1\}^{d} . While the dimension d d and the semantic interpretation vary, the mathematical treatment of stochasticity remains unified. We describe the three specific instantiations of 𝐗 \mathbf{X} as follows:

[46] p: Answers ( 𝐘 \mathbf{Y} ): The answer per run is a categorical random variable modeled as a one-hot vector 𝐲 ∈ { 0 , 1 } K A \mathbf{y}\in\{0,1\}^{K_{A}} . Here, K A K_{A} represents the total number of unique answers observed across all runs. The support of 𝐘 \mathbf{Y} is the set of standard basis vectors { 𝐞 1 , … , 𝐞 K A } \{\mathbf{e}_{1},\dots,\mathbf{e}_{K_{A}}\} . Note that answers exist only for questions that are not open-ended. For open-ended questions, this can be replaced by some measurement on the quality of report.

[47] p: Findings ( 𝐁 \mathbf{B} ): The findings per run are modeled as a binary vector 𝐛 ∈ { 0 , 1 } K F \mathbf{b}\in\{0,1\}^{K_{F}} . Here, K F K_{F} is the size of the global union of unique findings across runs. The global set of findings is indexed from 1 1 to K F K_{F} , such that a value of 1 1 at the k k -th entry of 𝐛 \mathbf{b} indicates the presence of the k k -th finding in that run.

[48] p: Citations ( 𝐂 \mathbf{C} ): The citations per run are modeled as a binary vector 𝐜 ∈ { 0 , 1 } K C \mathbf{c}\in\{0,1\}^{K_{C}} . Here, K C K_{C} is the size of the global union of unique citations across runs. The global set of citations is indexed from 1 1 to K C K_{C} , such that a value of 1 1 at the k k -th entry of 𝐜 \mathbf{c} indicates the presence of the k k -th citation in that run.

[49] h3: 4.1 Total Variance as a Measure of Stochasticity

[50] p: We seek a scalar that captures run-to-run variability. We use the trace of the covariance (“total variance”) of the embedded output vector. Let us recall a convenient identity.

[51] h6: Proposition 4.1 .

[52] p: Let 𝐗 \mathbf{X} be a random vector in ℝ d \mathbb{R}^{d} with finite mean 𝛍 = 𝔼 ⁡ [ 𝐗 ] \bm{\mu}=\mathbb{E}[\mathbf{X}] and covariance matrix 𝚺 = Var ⁡ ( 𝐗 ) \bm{\Sigma}=\Var(\mathbf{X}) . Let 𝐗 1 \mathbf{X}_{1} and 𝐗 2 \mathbf{X}_{2} be independent and identically distributed (i.i.d.) copies of 𝐗 \mathbf{X} . The covariance matrix 𝚺 \bm{\Sigma} is given by:

[53] table: 𝚺 = 1 2 ​ 𝔼 ​ [ ( 𝐗 1 − 𝐗 2 ) ​ ( 𝐗 1 − 𝐗 2 ) ⊤ ] . \bm{\Sigma}=\frac{1}{2}\mathbb{E}\left[(\mathbf{X}_{1}-\mathbf{X}_{2})(\mathbf{X}_{1}-\mathbf{X}_{2})^{\top}\right].

[54] h6: Corollary 4.2 (Total variance) .

[55] p: We have

[56] table: TV ( 𝐗 ) ≔ Tr ( 𝚺 ) = 1 2 ​ 𝔼 ​ [ ‖ 𝐗 1 − 𝐗 2 ‖ 2 ] . \mathop{\mathrm{TV}}(\mathbf{X})\coloneq\mathop{\mathrm{Tr}}(\bm{\Sigma})=\frac{1}{2}\mathbb{E}\left[\|\mathbf{X}_{1}-\mathbf{X}_{2}\|^{2}\right]. (5)

[57] p: The raw trace variance scales with vector magnitude and output size. To make metrics comparable across runs and output types, we normalize each realization by its ℓ 2 \ell_{2} norm. Let 𝐱 ~ i = 𝐱 i / ‖ 𝐱 i ‖ 2 \widetilde{\mathbf{x}}_{i}={\mathbf{x}_{i}}/{\|\mathbf{x}_{i}\|_{2}} be the normalized observation for run i i if ‖ 𝐱 i ‖ 2 > 0 \|\mathbf{x}_{i}\|_{2}>0 and 𝟎 \mathbf{0} otherwise. We then define (normalized) stochasticity as TV ( 𝐗 ~ ) ≔ Tr ( Var ⁡ ( 𝐗 ~ ) ) ∈ [ 0 , 1 ] \mathop{\mathrm{TV}}(\widetilde{\mathbf{X}})\coloneq\mathop{\mathrm{Tr}}(\Var(\widetilde{\mathbf{X}}))\in[0,1] .

[58] p: Given n n runs with normalized vectors { 𝐱 ~ ( i ) } i = 1 n \{\widetilde{\mathbf{x}}^{(i)}\}_{i=1}^{n} , we estimate:

[59] table: TV ^ ​ ( 𝐗 ~ ) = 1 2 ​ n ​ ( n − 1 ) ​ ∑ i = 1 n ∑ j = 1 n ‖ 𝐱 ~ i − 𝐱 ~ j ‖ 2 . \widehat{\mathop{\mathrm{TV}}}(\widetilde{\mathbf{X}})=\frac{1}{2n(n-1)}\sum_{i=1}^{n}\sum_{j=1}^{n}\|\widetilde{\mathbf{x}}_{i}-\widetilde{\mathbf{x}}_{j}\|^{2}. (6)

[60] p: This is a U-statistic estimator corresponding to ( 5 ) which is unbiased. Before applying the estimator TV ^ \widehat{\mathop{\mathrm{TV}}} to our variables of interest, we must ensure that the vector dimensions are semantically consistent across the n n independent runs, i.e., dimension 3 for different 𝐱 ~ i \widetilde{\mathbf{x}}_{i} should represent the same answer/finding/citation.

[61] p: For one-hot answers, TV ^ ​ ( 𝐗 ~ ) \widehat{\mathop{\mathrm{TV}}}(\widetilde{\mathbf{X}}) equals the empirical probability that two independent runs yield different canonical answers. For binary findings/citations, normalization yields a cosine-overlap notion: the metric increases when runs share fewer canonical items relative to their sizes. We provide further interpretation and analysis of TV ^ \widehat{\mathop{\mathrm{TV}}} in Appendix C.2 .

[62] p: To capture the variability in how much the agent outputs (e.g., number of findings or citations), we can also measure variance of the support size ‖ 𝐗 ‖ 0 \|\mathbf{X}\|_{0} , using the same pairwise form as ( 5 ):

[63] table: TV ^ ​ ( ‖ 𝐗 ‖ 0 ) = 1 2 ​ n ​ ( n − 1 ) ​ ∑ i = 1 n ∑ j = 1 n ( ‖ 𝐱 i ‖ 0 − ‖ 𝐱 j ‖ 0 ) 2 . \hskip-5.0pt\widehat{\mathop{\mathrm{TV}}}(\|\mathbf{X}\|_{0})=\frac{1}{2n(n-1)}\sum_{i=1}^{n}\sum_{j=1}^{n}\left(\|\mathbf{x}_{i}\|_{0}-\|\mathbf{x}_{j}\|_{0}\right)^{2}. (7)

[64] h3: 4.2 Constructing Metrics from Agent Outputs

[65] p: To implement the proposed variance estimators on real agent outputs, we need to extract the required information from the agent’s final report. We take the agent’s final report, and adopt a decomposition procedure inspired by FactScore [ 14 ] . We extract: (i) the final answer (for non–open-ended tasks), (ii) all URLs as citations, and (iii) a set of atomic findings obtained by decomposing the final report into minimal factual claims using LLM for each report. We include our prompts in Appendix B .

[66] p: To ensure cross-run semantic alignment, findings from all trajectories are clustered into canonical findings using LLM-as-a-judge that determines whether two findings express the same underlying fact. Citations are canonicalized via URL normalization followed by exact string matching. After that, analogous binary vectors are constructed for answers and citations using their respective canonical sets. For non open-ended tasks, accuracy is computed by comparing the extracted final answer to the ground-truth answer using LLM-as-a-judge. We use greedy decoding for the reproducibility of evaluation pipeline. We demonstrate our evaluation pipeline in Figure 1 .

[67] h2: 5 Analysis of Stochasticity via Variance Decomposition

[68] p: Following the metrics and evaluation pipeline we proposed in Section 4 , we model the progression of the random variable of interest over time, denoted as 𝐗 t \mathbf{X}_{t} (e.g., the accumulated findings or citations at step t t ). Since TV corresponds to the trace of the covariance matrix, it allows us to apply the Law of Total Variance to mathematically decompose the variance of 𝐗 t + 1 \mathbf{X}_{t+1} , identifying how a policy ( π query , π sum , π update \pi_{\text{query}},\pi_{\text{sum}},\pi_{\text{update}} ) introduce stochasticity at each step.

[69] h3: 5.1 Decomposing Stochasticity in Deep Research Agents

[70] p: As DRAs iteratively gather and process information, stochasticity accumulates at each decision step. While we model this process as an information acquisition MDP , isolating the exact contribution of every variable during a full execution is computationally intractable. However, to understand and mitigate the variance in the final research output, we conceptually decompose the stochasticity at any given step t t into two primary components:

[71] p: Propagated Stochasticity. This represents the stochasticity inherited from previous steps. Because a DRA’s current action depends on its prior state (e.g., previous search results and intermediate reasoning), any stochasticity introduced early in the process naturally cascades. Conceptually, it captures how much of the stochasticity in the next state 𝐗 t + 1 \mathbf{X}_{t+1} is simply a result of the agent starting from a noisy or varying distribution at 𝐗 t \mathbf{X}_{t} . Even if the agent were to act completely deterministically at step t t , the stochasticity in the incoming state would still cause variability in the subsequent trajectory.

[72] p: Intrinsic Stochasticity. This is the new, step-specific stochasticity introduced by the agent’s internal policies during the current time step t t . It measures the stochasticity that remains even if the previous state 𝐗 t \mathbf{X}_{t} were known with absolute certainty. Given the exact same starting state, the LLM-driven components of the DRA will still exhibit variability.

[73] p: To provide a structural lens for auditing this uncertainty, we further categorize Intrinsic Stochasticity based on the three distinct functional modules of the DRA at each step:

[74] p: Information Acquisition ( Δ Query \Delta_{\text{Query}} ): The stochasticity introduced when the agent formulates search queries. Different phrasings of search queries can lead to vastly different retrieved documents and paragraphs.

[75] p: Information Compression ( Δ Sum \Delta_{\text{Sum}} ): The stochasticity introduced when the agent parses, filters, and summarizes the raw retrieved content. Different extractions of facts from the exact same source document lead to divergent contexts.

[76] p: Inference ( Δ Update \Delta_{\text{Update}} ): The stochasticity introduced when the agent reasons over the newly synthesized information to update its internal belief state, answer open questions, or draw intermediate conclusions.

[77] p: We provide the mathematical formulation of the stochasticity decomposition in Appendix A.2 . In practice, perfectly disentangling these two sources of stochasticity is fundamentally intractable. Because of the autoregressive nature of the agent’s trajectory, the intrinsic stochasticity introduced by any module at step t t immediately alters the resulting state 𝐗 t + 1 \mathbf{X}_{t+1} . Consequently, this intrinsic stochasticity naturally becomes the propagated stochasticity for step t + 1 t+1 and all subsequent steps. Furthermore, calculating the exact mathematical boundaries between them requires computing expectations over all possible future agent states and search engine responses, which is computationally infeasible for open-ended tasks.

[78] p: Therefore, rather than attempting to compute exact analytical stochasticity terms, our empirical framework in the following section relies on targeted interventions. By temporally and modularly ablating the DRA’s steps, we can approximate how these deeply entangled sources of uncertainty propagate and ultimately impact the stochasticity and quality of the final research outcome.

[79] figure: Table 1: Full Ablation Results. A comprehensive breakdown of stochasticity metrics across varying temperatures ( λ \lambda ), temporal injection points (Steps), and specific modules. This table corresponds to the experimental decomposition analyzed in Section 5.1 . λ \lambda Step Module TV ^ ​ ( 𝐗 ~ ) \widehat{\text{TV}}(\widetilde{\mathbf{X}}) TV ^ ​ ( ‖ 𝐗 ‖ 0 ) \sqrt{\widehat{\text{TV}}(\|\mathbf{X}\|_{0})} Mean Count ( μ \mu ) Acc. Ans. Find. Cit. Find. Cit. Find. Cit. 0.5 1 Query ( π query \pi_{\text{query}} ) 0.37 0.76 0.42 29.97 2.10 90.82 6.62 0.40 Sum ( π sum \pi_{\text{sum}} ) 0.58 0.84 0.52 32.01 2.17 90.84 6.46 0.40 Update ( π update \pi_{\text{update}} ) 0.59 0.85 0.55 31.45 2.49 88.80 6.96 0.52 2 Query 0.36 0.70 0.30 27.35 2.30 92.46 5.96 0.46 Sum 0.36 0.65 0.38 30.85 2.60 88.14 6.48 0.44 Update 0.38 0.82 0.40 28.68 2.48 96.58 6.40 0.40 3 Query 0.36 0.61 0.30 32.08 2.26 86.92 6.08 0.34 Sum 0.28 0.52 0.28 31.88 2.14 96.82 6.84 0.34 Update 0.32 0.68 0.34 32.62 2.67 89.96 6.32 0.44 Combined Query 0.44 0.76 0.50 35.84 2.41 102.90 6.52 0.40 Sum 0.59 0.84 0.55 34.46 2.76 89.52 6.96 0.44 Update 0.59 0.89 0.55 39.17 2.55 96.88 7.62 0.41 1.0 1 Query ( π query \pi_{\text{query}} ) 0.51 0.80 0.46 25.98 2.71 91.38 6.12 0.36 Sum ( π sum \pi_{\text{sum}} ) 0.53 0.88 0.51 38.32 2.51 88.46 6.60 0.46 Update ( π update \pi_{\text{update}} ) 0.62 0.89 0.59 28.22 2.48 88.10 6.70 0.46 2 Query 0.43 0.79 0.45 25.85 1.93 93.53 6.74 0.42 Sum 0.37 0.54 0.29 24.57 1.63 93.77 6.02 0.46 Update 0.40 0.85 0.48 28.48 2.14 84.60 6.62 0.40 3 Query 0.34 0.63 0.32 30.65 1.90 83.54 6.30 0.50 Sum 0.30 0.53 0.29 31.29 2.04 94.47 6.09 0.38 Update 0.41 0.63 0.38 37.55 2.68 101.00 6.70 0.40 Combined Query 0.49 0.87 0.51 36.14 2.70 89.50 6.52 0.50 Sum 0.61 0.92 0.62 34.93 2.67 88.93 6.07 0.41 Update 0.59 0.88 0.58 39.49 2.30 88.74 6.00 0.56

[80] h3: 5.2 Empirical Investigation via Temperature Ablation

[81] p: To empirically quantify these theoretical components, we leverage temperature to control the variance of different policies. By increasing the temperature λ \lambda for specific policy modules ( π query \pi_{\text{query}} , π sum \pi_{\text{sum}} , π update \pi_{\text{update}} ) at specific steps while setting λ = 0 \lambda=0 (greedy decoding) for others, we empirically investigate how these modules affect DRA’s stochasticity over time. We applied these temperature controls at distinct temporal stages: early (Step 1), middle (Step 2), late (Step 3), and combined (Steps 1–3). This setup allows us to trace how stochasticity introduced by specific modules at specific times impacts the variance of the final research output 𝐗 T \mathbf{X}_{T} .

[82] p: For the DRA system, we use ReAct realization based on Tongyi DeepResearch [ 19 ] . In order to see the relationship between accuracy and stochasticity, we use 20 instances from QA dataset WebWalkerQA [ 22 ] . We use Qwen3-30B-A3B-Instruct-2507 [ 24 ] as our backbone LLM, and set the number of runs k = 10 k=10 for each instance. We use You.com search API that is designed to return consistent results for identical queries. All experiments are conducted within a short time window (50 hours) to minimize potential variation due to search index updates or webpage changes, thereby eliminating environmental stochasticity from retrieval. We summarize our experiment results in Table 1 .

[83] figure: (a) Propagation of stochasticity across steps. (b) Pairwise correlations of stochasticity metrics. (c) Effect of temperature on total variance. (d) Module-wise contribution to stochasticity. Figure 2: Comprehensive Analysis of Stochasticity Behavior. (a) Early-stage injections dominate propagation. (b) Strong positive correlations across answer, finding, and citation TV. (c) Higher sampling temperature increases total variance. (d) The Update module contributes the largest variance.

[84] h5: Finding 1: Early-stage stochasticity influences final-stage stochasticity more than late-stage stochasticity.

[85] p: To isolate temporal stochasticity effects independent of module choices, we average TV ^ ​ ( 𝐗 ~ ) \widehat{\mathrm{TV}}(\widetilde{\mathbf{X}}) over the three modules ( π query , π sum , π update \pi_{\text{query}},\pi_{\text{sum}},\pi_{\text{update}} ) for each perturbation step. Figure 2(a) plot the resulting mean final variance for answer-level ( 𝐘 \mathbf{Y} ), finding-level ( 𝐁 \mathbf{B} ), and citation-level ( 𝐂 \mathbf{C} ) variances.

[86] p: Across both temperatures and variance types, applying higher stochasticity to different modules at earlier steps consistently yields greater final variance than applying the same stochasticity at later stages. This empirical observation directly shows the significant influence of propagated stochasticity on the final variance. It confirms that uncertainty introduced in an initial state is magnified and “carried forward” to the total variance of the final output. The fact that the highest overall stochasticity occurs when policy temperatures are introduced at steps 1, 2, and 3 indicates that variance is cumulative, arising from the compounding of propagated and intrinsic stochasticity. Consequently, stochasticity-control mechanisms are most effective when applied to early-stage modules to prevent this propagation.

[87] h5: Finding 2: Findings, citations and answer stochasticity are positively correlated.

[88] p: To examine the relationship between different types of stochasticity, we plot pairwise scatter plots between variance of findings TV ^ ​ ( 𝐁 ) \widehat{\mathrm{TV}}(\mathbf{B}) , variance of citations TV ^ ​ ( 𝐂 ) \widehat{\mathrm{TV}}(\mathbf{C}) , and variance of answers TV ^ ​ ( 𝐘 ) \widehat{\mathrm{TV}}(\mathbf{Y}) across all temperatures, steps, and modules ( Figure 2(b) ). Each point corresponds to one experimental condition.

[89] p: We observe strong positive correlations among all variance metrics TV ^ ​ ( 𝐘 ) \widehat{\mathrm{TV}}(\mathbf{Y}) , TV ^ ​ ( 𝐁 ) \widehat{\mathrm{TV}}(\mathbf{B}) , and TV ^ ​ ( 𝐂 ) \widehat{\mathrm{TV}}(\mathbf{C}) , confirming that these metrics capture a shared underlying notion of knowledge state stochasticity.

[90] h5: Finding 3: Variance magnitude increases monotonically with temperature.

[91] p: To examine how stochasticity scales with sampling temperature, we compare TV ^ ​ ( 𝐗 ~ ) \widehat{\mathrm{TV}}(\widetilde{\mathbf{X}}) under λ = 0.5 \lambda=0.5 and λ = 1.0 \lambda=1.0 while averaging across the three modules. Figure 2(c) plot the resulting mean final total variance for single-step perturbations at Step 1 and cumulative perturbations across Steps 1–3, respectively.

[92] p: Across both single-step and cumulative settings, higher sampling temperature consistently leads to larger estimated total variance. This monotonic increase indicates that temperature can act as a direct scaling factor for the total variance of the research output. Increasing λ \lambda raises the entropy of the component policies ( π query , π sum , π update \pi_{\text{query}},\pi_{\text{sum}},\pi_{\text{update}} ), thereby increasing intrinsic stochasticity at each step and the overall variance.

[93] h5: Finding 4: Higher stochasticity does not imply higher accuracy.

[94] p: Although increased stochasticity can encourage exploration, our results show that larger variance TV ^ ​ ( 𝐗 ~ ) \widehat{\mathrm{TV}}(\widetilde{\mathbf{X}}) does not consistently lead to higher answer accuracy. Table 2 shows examples where the final variance corresponds to similar or worse accuracy, as stochasticity increases.

[95] figure: Table 2: Examples showing that higher stochasticity does not monotonically improve accuracy. We select examples that have each one of λ \lambda , step, and module different. λ \lambda Step Module TV ^ ​ ( 𝐁 ) \widehat{\mathrm{TV}}(\mathbf{B}) Acc. 0.5 Step 1 Query 0.76 0.40 1.0 Step 1 Query 0.80 0.36 0.5 Combined Update 0.89 0.41 1.0 Combined Update 0.88 0.56 0.5 Step 1 Sum 0.84 0.40 0.5 Step 3 Sum 0.52 0.34

[96] p: Across these examples, we observe that larger TV ^ ​ ( 𝐁 ) \widehat{\mathrm{TV}}(\mathbf{B}) do not consistently imply higher accuracy, indicating that stochasticity alone is not a reliable driver of performance.

[97] h5: Finding 5: Findings are more stochastic than citations.

[98] p: We compare stochasticity at the level of internal findings ( 𝐁 \mathbf{B} ) and external citations ( 𝐂 \mathbf{C} ). Table 3 reports averages across λ \lambda , step, and module.

[99] figure: Table 3: Average stochasticity of findings vs. citations across modules, steps, and temperatures. Metric Findings ( 𝐁 \mathbf{B} ) Citations ( 𝐂 \mathbf{C} ) TV ^ ​ ( 𝐗 ~ ) \widehat{\mathrm{TV}}(\widetilde{\mathbf{X}}) 0.76 0.44

[100] p: Findings ( 𝐁 \mathbf{B} ) exhibit substantially larger total variance than citations ( 𝐂 \mathbf{C} ). This suggests that even though DRAs retrieve relatively consistent evidence sources (indicated by lower citation variance), the process of internalizing that evidence through information compression and inference policy introduces a significant amount of stochasticity.

[101] h5: Finding 6: The inference module has a greater impact on the final stochasticity than the information acquisition and compression modules.

[102] p: To compare the effect of different modules causing intrinsic stochasticity, we average the stochasticity metrics across time for the three policy modules ( Figure 2(d) ). We find that adding stochasticity to π update \pi_{\text{update}} yields the highest final output stochasticity across all three metrics. This suggests that mitigating stochasticity during inference (belief update) is more impactful for achieving overall system stability than controlling variances for the information acquisition and compression stages.

[103] h2: 6 Mitigation Attempt for Stochasticity

[104] p: Based on our findings, we provide initial strategies to lower stochasticity in DRA systems while maintaining (or increasing) their accuracy. In order to make our methods generalizable, we switch from a controlled environment to calling backbone LLMs through APIs. A significant challenge in this setting is the non-determinism in API LLM inference. Unlike local inference, API inference is non-batch invariant [ 9 ] , meaning that setting temperature to be 0 0 is insufficient to eliminate stochasticity.

[105] p: Since we cannot reduce stochasticity under this more general setting through lowering temperature as in C.3 , we try to mitigate stochasticity while preserving accuracy through other algorithmic designs. We call Qwen3-235B-A22B-Instruct-2507-tput through Together AI API as backbone and use 20 instances from DeepSearchQA [ 8 ] as a more complex dataset to test our mitigation strategies. We keep the number of runs k = 10 k=10 for each instance. Throughout the experiments, we set the temperature to be λ = 1 \lambda=1 . We use the same search API settings as in Section 5.2 .

[106] h3: 6.1 Method 1: Structured Summarization and Reasoning Output

[107] p: To reduce the intrinsic stochasticity of the information compression ( π sum \pi_{\text{sum}} ) and inference policy ( π update \pi_{\text{update}} ), we impose a structured output constraint for them. By forcing the model to generate outputs within a predefined JSON or Markdown schema, we expect to reduce the stylistic variations in the output, there by reducing Δ Sum \Delta_{\text{Sum}} and Δ Update \Delta_{\text{Update}} . An example of the structured output is shown in C.4 . As discussed in Finding 6 , the stochasticity of the inference module has the greatest influence on the variance of the final output. Therefore, we expect that imposing a structured output constraint on π update \pi_{\text{update}} will reduce overall stochasticity more than imposing such a constraint on π sum \pi_{\text{sum}} .

[108] h3: 6.2 Method 2: Reducing Early-stage Query Stochasticity

[109] p: We also adopt a consensus-based ensemble for the information acquisition module ( π query \pi_{\text{query}} ). We issue N N independent sets of queries and retain only the intersection a t = ⋂ i = 1 N queries i a_{t}=\bigcap_{i=1}^{N}\text{queries}_{i} . This ensures the agent only proceeds with queries that multiple runs have consensus in, effectively reducing early-stage query stochasticity Δ Query \Delta_{\text{Query}} . To maintain efficiency, we decay N → 1 N\to 1 as t t increases. Since early-stage stochasticity has a greater impact than later-stage stochasticity ( Finding 1 ), we expect that this annealing over the number of runs will still effectively reduce variance. Finally, if no intersection exists, we use the first proposed set of queries.

[110] h3: 6.3 Experimental Result

[111] p: As shown in Table 4 , both mitigation methods reduce the stochasticity of the research output while maintaining (or sometimes increasing) the research quality. In addition, imposing structural output constraints on π update \pi_{\text{update}} does reduce overall stochasticity more than imposing such a constraint on π sum \pi_{\text{sum}} , reducing the average stochasticity by 5%, and imposing structural output constraints for both modules yields more output stability than filtering search queries via intersection by an average of 6%. By utilizing all mitigations together, we achieve the lowest stochasticity while having the highest accuracy. For Accuracy, we see a 12% increase w.r.t Baseline, with an average 22% decrease in stochasticity. These results demonstrate that stochasticity can be effectively mitigated through algorithmic design and controlling for stochasticity will not degrade the quality of the research output.

[112] figure: Table 4: Comparison of Stochasticity Mitigation Strategies. The best performance in each category is highlighted in bold. Struc. Comb. applies structured summarization and reasoning simultaneously; Comb. integrates all three mitigation methods. Avg. TV represents the average value of the three-level stochasticity. Method Acc. TV ^ ​ ( 𝐘 ) \widehat{\mathrm{TV}}(\mathbf{Y}) TV ^ ​ ( 𝐁 ) \widehat{\mathrm{TV}}(\mathbf{B}) TV ^ ​ ( 𝐂 ) \widehat{\mathrm{TV}}(\mathbf{C}) Avg. TV Baseline 0.24 0.62 0.83 0.62 0.69 Struc. Sum. 0.28 0.58 0.80 0.64 0.67 Struc. Update 0.32 0.52 0.75 0.58 0.62 Struc. Comb. 0.36 0.44 0.68 0.56 0.56 Quer. Int. 0.32 0.50 0.74 0.61 0.62 Comb. 0.36 0.38 0.61 0.43 0.47

[113] h2: 7 Conclusion

[114] p: In this paper, we provide a systematic analysis of stochasticity in DRAs, introducing principled metrics and a variance-decomposition framework for attributing stochasticity to specific modules and time steps. Our results show that stochasticity injected early in a trajectory propagates strongly and that inference is the dominant source of stochasticity. We also showcase the possibility of reducing stochasticity by proposing mitigation methods based on algorithmic designs. Overall, this work takes the first step toward building more reproducible deep research agents. Future directions include designing a broader range of mitigation strategies and developing deeper theoretical analyses of stochasticity in DRAs.

[115] h2: References

[116] h2: Appendix A Proofs

[117] h3: A.1 Proof of Proposition 4.1

[118] h6: Proof.

[119] p: By definition, the covariance matrix is the expected outer product of the centered random variable:

[120] table: 𝚺 = 𝔼 ⁡ [ ( 𝐗 − 𝝁 ) ​ ( 𝐗 − 𝝁 ) ⊤ ] = 𝔼 ⁡ [ 𝐗𝐗 ⊤ ] − 𝝁 ​ 𝝁 ⊤ . \bm{\Sigma}=\mathbb{E}\left[(\mathbf{X}-\bm{\mu})(\mathbf{X}-\bm{\mu})^{\top}\right]=\mathbb{E}[\mathbf{X}\mathbf{X}^{\top}]-\bm{\mu}\bm{\mu}^{\top}.

[121] p: On the RHS, we have

[122] table: 𝔼 ⁡ [ ( 𝐗 1 − 𝐗 2 ) ​ ( 𝐗 1 ⊤ − 𝐗 2 ⊤ ) ] \displaystyle\mathbb{E}\left[(\mathbf{X}_{1}-\mathbf{X}_{2})(\mathbf{X}_{1}^{\top}-\mathbf{X}_{2}^{\top})\right] = 𝔼 ⁡ [ 𝐗 1 ​ 𝐗 1 ⊤ ] − 𝔼 ⁡ [ 𝐗 1 ​ 𝐗 2 ⊤ ] − 𝔼 ⁡ [ 𝐗 2 ​ 𝐗 1 ⊤ ] + 𝔼 ⁡ [ 𝐗 2 ​ 𝐗 2 ⊤ ] . \displaystyle=\mathbb{E}[\mathbf{X}_{1}\mathbf{X}_{1}^{\top}]-\mathbb{E}[\mathbf{X}_{1}\mathbf{X}_{2}^{\top}]-\mathbb{E}[\mathbf{X}_{2}\mathbf{X}_{1}^{\top}]+\mathbb{E}[\mathbf{X}_{2}\mathbf{X}_{2}^{\top}].

[123] p: Since 𝐗 1 \mathbf{X}_{1} and 𝐗 2 \mathbf{X}_{2} are i.i.d., the second moments are equal:

[124] table: 𝔼 ⁡ [ 𝐗 1 ​ 𝐗 1 ⊤ ] = 𝔼 ⁡ [ 𝐗 2 ​ 𝐗 2 ⊤ ] = 𝔼 ⁡ [ 𝐗𝐗 ⊤ ] . \mathbb{E}[\mathbf{X}_{1}\mathbf{X}_{1}^{\top}]=\mathbb{E}[\mathbf{X}_{2}\mathbf{X}_{2}^{\top}]=\mathbb{E}[\mathbf{X}\mathbf{X}^{\top}].

[125] p: Since 𝐗 1 \mathbf{X}_{1} and 𝐗 2 \mathbf{X}_{2} are independent, we have the expectation of the product is the product of expectations.

[126] table: 𝔼 ⁡ [ 𝐗 1 ​ 𝐗 2 ⊤ ] = 𝔼 ⁡ [ 𝐗 1 ] ​ 𝔼 ​ [ 𝐗 2 ] ⊤ = 𝝁 ​ 𝝁 ⊤ , \mathbb{E}[\mathbf{X}_{1}\mathbf{X}_{2}^{\top}]=\mathbb{E}[\mathbf{X}_{1}]\mathbb{E}[\mathbf{X}_{2}]^{\top}=\bm{\mu}\bm{\mu}^{\top},

[127] table: 𝔼 ⁡ [ 𝐗 2 ​ 𝐗 1 ⊤ ] = 𝔼 ⁡ [ 𝐗 2 ] ​ 𝔼 ​ [ 𝐗 1 ] ⊤ = 𝝁 ​ 𝝁 ⊤ . \mathbb{E}[\mathbf{X}_{2}\mathbf{X}_{1}^{\top}]=\mathbb{E}[\mathbf{X}_{2}]\mathbb{E}[\mathbf{X}_{1}]^{\top}=\bm{\mu}\bm{\mu}^{\top}.

[128] p: Substituting these back into the expression for the RHS, we get

[129] table: 𝔼 ⁡ [ ( 𝐗 1 − 𝐗 2 ) ​ ( 𝐗 1 ⊤ − 𝐗 2 ⊤ ) ] \displaystyle\mathbb{E}\left[(\mathbf{X}_{1}-\mathbf{X}_{2})(\mathbf{X}_{1}^{\top}-\mathbf{X}_{2}^{\top})\right] = 𝔼 ⁡ [ 𝐗𝐗 ⊤ ] − 𝝁 ​ 𝝁 ⊤ − 𝝁 ​ 𝝁 ⊤ + 𝔼 ⁡ [ 𝐗𝐗 ⊤ ] \displaystyle=\mathbb{E}[\mathbf{X}\mathbf{X}^{\top}]-\bm{\mu}\bm{\mu}^{\top}-\bm{\mu}\bm{\mu}^{\top}+\mathbb{E}[\mathbf{X}\mathbf{X}^{\top}] = 2 ​ 𝔼 ​ [ 𝐗𝐗 ⊤ ] − 2 ​ 𝝁 ​ 𝝁 ⊤ \displaystyle=2\mathbb{E}[\mathbf{X}\mathbf{X}^{\top}]-2\bm{\mu}\bm{\mu}^{\top} = 2 ​ ( 𝔼 ⁡ [ 𝐗𝐗 ⊤ ] − 𝝁 ​ 𝝁 ⊤ ) . \displaystyle=2\left(\mathbb{E}[\mathbf{X}\mathbf{X}^{\top}]-\bm{\mu}\bm{\mu}^{\top}\right).

[130] p: This completes the derivation. ∎

[131] h3: A.2 Formal Stochasticity Decomposition

[132] h6: Proposition A.1 (TV Decomposition) .

[133] p: Let 𝐗 t \mathbf{X}_{t} be the state at time t t . The Total Variance at t + 1 t+1 , denoted TV ​ ( 𝐗 t + 1 ) = Tr ⁡ ( Var ⁡ ( 𝐗 t + 1 ) ) \text{TV}(\mathbf{X}_{t+1})=\mathrm{Tr}(\mathrm{Var}(\mathbf{X}_{t+1})) , decomposes into a propagated stochasticity term and an intrinsic stochasticity term ℐ t \mathcal{I}_{t} :

[134] table: TV ​ ( 𝐗 t + 1 ) = TV 𝐗 t ​ ( 𝔼 ⁡ [ 𝐗 t + 1 ∣ 𝐗 t ] ) ⏟ Propagated Stochasticity + 𝔼 𝐗 t ​ [ ℐ t ​ ( 𝐗 t ) ] ⏟ Intrinsic Stochasticity , \text{TV}(\mathbf{X}_{t+1})=\underbrace{\text{TV}_{\mathbf{X}_{t}}\left(\mathbb{E}[\mathbf{X}_{t+1}\mid\mathbf{X}_{t}]\right)}_{\text{Propagated Stochasticity}}+\underbrace{\mathbb{E}_{\mathbf{X}_{t}}[\mathcal{I}_{t}(\mathbf{X}_{t})]}_{\text{Intrinsic Stochasticity}}, (8)

[135] p: where the intrinsic stochasticity ℐ t ​ ( 𝐗 t ) = Tr ⁡ ( Var ⁡ ( 𝐗 t + 1 ∣ 𝐗 t ) ) \mathcal{I}_{t}(\mathbf{X}_{t})=\mathrm{Tr}(\mathrm{Var}(\mathbf{X}_{t+1}\mid\mathbf{X}_{t})) can be further decomposed into three components controlled by the three policies, respectively:

[136] table: ℐ t ​ ( 𝐗 t ) = Δ Query ⏟ π query + Δ Sum ⏟ π sum + Δ Update ⏟ π update . \mathcal{I}_{t}(\mathbf{X}_{t})=\underbrace{\Delta_{\text{Query}}}_{\pi_{\text{query}}}+\underbrace{\Delta_{\text{Sum}}}_{\pi_{\text{sum}}}+\underbrace{\Delta_{\text{Update}}}_{\pi_{\text{update}}}. (9)

[137] p: Assuming search results i t i_{t} are deterministic given query a t a_{t} , these components are defined as the traces of their respective conditional variances:

[138] table: Δ Query = TV a t ∼ π query ( 𝔼 [ 𝐗 t + 1 ∣ 𝐗 t , a t ] ) , \displaystyle\Delta_{\text{Query}}=\text{TV}_{a_{t}\sim\pi_{\text{query}}}\left(\mathbb{E}[\mathbf{X}_{t+1}\mid\mathbf{X}_{t},a_{t}]\right), Δ Sum = 𝔼 a t [ TV h t ∼ π sum ( 𝔼 [ 𝐗 t + 1 ∣ 𝐗 t , a t , h t ] ) ] , \displaystyle\Delta_{\text{Sum}}=\mathbb{E}_{a_{t}}\left[\text{TV}_{h_{t}\sim\pi_{\text{sum}}}(\mathbb{E}[\mathbf{X}_{t+1}\mid\mathbf{X}_{t},a_{t},h_{t}])\right], Δ Update = 𝔼 a t , h t ​ [ TV 𝐗 t + 1 ∼ π update ​ ( 𝐗 t + 1 ∣ 𝐗 t , a t , h t ) ] . \displaystyle\Delta_{\text{Update}}=\mathbb{E}_{a_{t},h_{t}}\left[\text{TV}_{\mathbf{X}_{t+1}\sim\pi_{\text{update}}}\left(\mathbf{X}_{t+1}\mid\mathbf{X}_{t},a_{t},h_{t}\right)\right].

[139] p: The decomposition presented in Proposition A.1 provides a structural lens through which we can audit the sources of uncertainty in the agent’s state evolution. By applying the Law of Total Variance, we distinguish between uncertainty that is inherited from previous steps and uncertainty that is generated at the current step.

[140] p: The first term, Propagated Stochasticity , quantifies the ‘momentum’ of prior stochasticity. Mathematically, it represents the variance of the conditional expectation; conceptually, it captures how much of the variance in 𝐗 t + 1 \mathbf{X}_{t+1} is simply a result of the agent starting from a noisy distribution 𝐗 t \mathbf{X}_{t} .

[141] p: On the other hand, the Intrinsic Stochasticity term, 𝔼 𝐗 t ​ [ ℐ t ​ ( 𝐗 t ) ] \mathbb{E}_{\mathbf{X}_{t}}[\mathcal{I}_{t}(\mathbf{X}_{t})] , represents the stochasticity introduced during the current time step t + 1 t+1 . It measures the variance that remains even if the previous state 𝐗 t \mathbf{X}_{t} were known with absolute certainty. By labeling this as a intrinsic , the framework treats the agent’s internal policies as sources of randomness that increases the stochasticity of the trajectory.

[142] p: The decomposition of ℐ t ​ ( 𝐗 t ) \mathcal{I}_{t}(\mathbf{X}_{t}) isolates the contribution of each policy:

[143] p: Δ Query \Delta_{\text{Query}} measures the variance of the expected output caused by the agent’s choice of information acquisition actions a t a_{t} .

[144] p: Δ Sum \Delta_{\text{Sum}} reflects the variance introduced by the compression and synthesis of external search results into the summary h t h_{t} .

[145] p: Δ Update \Delta_{\text{Update}} captures the variance in the belief state update (inference), i.e., the stochasticity in integrating the synthesized information to infer the next state 𝐗 t + 1 \mathbf{X}_{t+1} .

[146] h4: A.2.1 Proof of Proposition A.1

[147] h6: Proof.

[148] p: We apply the Law of Total Variance for random vectors, Var ⁡ ( 𝐗 ) = Var ⁡ ( 𝔼 ⁡ [ 𝐗 | 𝐙 ] ) + 𝔼 ⁡ [ Var ⁡ ( 𝐗 | 𝐙 ) ] \mathrm{Var}(\mathbf{X})=\mathrm{Var}(\mathbb{E}[\mathbf{X}|\mathbf{Z}])+\mathbb{E}[\mathrm{Var}(\mathbf{X}|\mathbf{Z})] . Since the trace operator is linear, Tr ⁡ ( Var ⁡ ( 𝐗 ) ) = Tr ⁡ ( Var ⁡ ( 𝔼 ⁡ [ 𝐗 | 𝐙 ] ) ) + 𝔼 ⁡ [ Tr ⁡ ( Var ⁡ ( 𝐗 | 𝐙 ) ) ] \mathrm{Tr}(\mathrm{Var}(\mathbf{X}))=\mathrm{Tr}(\mathrm{Var}(\mathbb{E}[\mathbf{X}|\mathbf{Z}]))+\mathbb{E}[\mathrm{Tr}(\mathrm{Var}(\mathbf{X}|\mathbf{Z}))] . We apply this recursively across the causal chain: 𝐗 t → a t → h t → 𝐗 t + 1 \mathbf{X}_{t}\to a_{t}\to h_{t}\to\mathbf{X}_{t+1} .

[149] p: Isolation of History. Conditioning on the previous state 𝐗 t \mathbf{X}_{t} , we separate the variance propagated from the history distribution from the fresh variance introduced at step t t :

[150] table: TV ​ ( 𝐗 t + 1 ) \displaystyle\text{TV}(\mathbf{X}_{t+1}) = Tr ⁡ ( Var 𝐗 t ​ ( 𝔼 ⁡ [ 𝐗 t + 1 ∣ 𝐗 t ] ) ) \displaystyle=\mathrm{Tr}\left(\mathrm{Var}_{\mathbf{X}_{t}}\left(\mathbb{E}[\mathbf{X}_{t+1}\mid\mathbf{X}_{t}]\right)\right) + 𝔼 𝐗 t ​ [ TV ​ ( 𝐗 t + 1 ∣ 𝐗 t ) ] \displaystyle\quad+\mathbb{E}_{\mathbf{X}_{t}}\left[\text{TV}(\mathbf{X}_{t+1}\mid\mathbf{X}_{t})\right]

[151] p: The second term is the expected intrinsic injection. We now decompose the inner term TV ​ ( 𝐗 t + 1 ∣ 𝐗 t ) \text{TV}(\mathbf{X}_{t+1}\mid\mathbf{X}_{t}) .

[152] p: Isolation of Query Divergence ( Δ Query \Delta_{\text{Query}} ). Conditioning on the action a t ∼ π query a_{t}\sim\pi_{\text{query}} , we apply the Law of Total Variance:

[153] table: TV ​ ( 𝐗 t + 1 ∣ 𝐗 t ) \displaystyle\text{TV}(\mathbf{X}_{t+1}\mid\mathbf{X}_{t}) = Tr ( Var a t ( 𝔼 [ 𝐗 t + 1 ∣ 𝐗 t , a t ] ) ) ⏟ Δ Query \displaystyle=\underbrace{\mathrm{Tr}\left(\mathrm{Var}_{a_{t}}(\mathbb{E}[\mathbf{X}_{t+1}\mid\mathbf{X}_{t},a_{t}])\right)}_{\Delta_{\text{Query}}} (10) + 𝔼 a t ​ [ TV ​ ( 𝐗 t + 1 ∣ 𝐗 t , a t ) ] \displaystyle+\mathbb{E}_{a_{t}}\left[\text{TV}(\mathbf{X}_{t+1}\mid\mathbf{X}_{t},a_{t})\right]

[154] p: Here, Δ Query \Delta_{\text{Query}} captures the spread in the future state caused solely by the stochastic choice of queries.

[155] p: Isolation of Summarization Noise ( Δ Sum \Delta_{\text{Sum}} ). We decompose the residual term 𝔼 a t ​ [ TV ​ ( 𝐗 t + 1 ∣ 𝐗 t , a t ) ] \mathbb{E}_{a_{t}}[\text{TV}(\mathbf{X}_{t+1}\mid\mathbf{X}_{t},a_{t})] . Since retrieved information i t i_{t} is deterministic given a t a_{t} , the next stochastic component is the distilled findings h t ∼ π sum h_{t}\sim\pi_{\text{sum}} . Conditioning on h t h_{t} :

[156] table: TV ​ ( 𝐗 t + 1 ∣ 𝐗 t , a t ) \displaystyle\text{TV}(\mathbf{X}_{t+1}\mid\mathbf{X}_{t},a_{t}) = Tr ( Var h t ( 𝔼 [ 𝐗 t + 1 ∣ 𝐗 t , a t , h t ] ) ) ⏟ Variance due to summarization \displaystyle=\underbrace{\mathrm{Tr}\left(\mathrm{Var}_{h_{t}}(\mathbb{E}[\mathbf{X}_{t+1}\mid\mathbf{X}_{t},a_{t},h_{t}])\right)}_{\text{Variance due to summarization}} (11) + 𝔼 h t ​ [ TV ​ ( 𝐗 t + 1 ∣ 𝐗 t , a t , h t ) ] \displaystyle+\mathbb{E}_{h_{t}}\left[\text{TV}(\mathbf{X}_{t+1}\mid\mathbf{X}_{t},a_{t},h_{t})\right]

[157] p: Taking the expectation over a t a_{t} yields Δ Sum \Delta_{\text{Sum}} .

[158] p: Isolation of Update Instability ( Δ Update \Delta_{\text{Update}} ). The remaining term represents the variance of the update step itself, given fixed history, action, and summary. This captures the inherent stochasticity of the reasoning policy π update \pi_{\text{update}} :

[159] table: Δ Update = 𝔼 a t ​ 𝔼 h t ​ [ TV ​ ( 𝐗 t + 1 ∣ 𝐗 t , a t , h t ) ] \Delta_{\text{Update}}=\mathbb{E}_{a_{t}}\mathbb{E}_{h_{t}}\left[\text{TV}(\mathbf{X}_{t+1}\mid\mathbf{X}_{t},a_{t},h_{t})\right]

[160] p: Substituting these terms back into Eq. ( 8 ) yields the full decomposition. ∎

[161] h2: Appendix B Prompts

[162] h3: B.1 Claim Decomposition

[163] figure: Listing 1: Claim Decomposition ⬇ ## Task Description Extract all factual claims from the provided report . Each claim should be a factual statement that can be verified . Claims may or may not have supporting citations . ## Input A Research Question and a complete report containing factual claims , some of which may have citation markers and corresponding URLs ( either inline or in a reference section ). ## Output Requirements - Extract each distinct factual claim throughout the entire report - For each claim , output a JSON object with : - The exact claim text as a string - The original text from the report containing this claim ( context ) - The corresponding citation URL as source ( if a citation marker directly follows the claim ) - If a claim has a citation marker directly following it , return the supporting URL as source - If a claim does not have a citation marker directly following it , return an empty string for source - Ensure all string values are properly escaped for valid JSON format ( e . g ., Replace internal quotation marks ( ") with escaped quotation marks (\\" )) in the claim and context - Return a JSON array containing all claim objects ## Format Specification [ { "claim" : "The exact statement representing a factual claim" , "context" : "The original sentence or passage from the report containing this claim" , "source" : "https://example.com/source1" }, { "claim" : "Another factual statement without direct citation" , "context" : "The original sentence or passage from the report containing this claim" , "source" : "" } ] ## Guidelines for Claim Identification 1. A claim should be a complete , standalone factual statement 2. Maintain the original wording where possible , but remove unnecessary context 3. Extract all factual claims regardless of whether they have citation support 4. Only map citation markers ( numbers , author names , etc .) to their corresponding URLs in the references section when the marker directly follows the claim statement 5. Exclude opinions , speculations , or methodological descriptions 6. Extract the context passage containing each claim for verification purposes 7. If multiple claims are associated with the same citation , extract them as separate entries ## Citation URL Mapping - If URLs appear directly after claims , use those URLs directly - Citation markers ( e . g ., a number or [ number ]) must directly follow the claim to be considered as supporting that claim - If claims use citation markers that reference a bibliography or reference section , locate the corresponding URLs in that section - If a claim has no directly following citation marker , use an empty string for source

[164] h3: B.2 Atomic Finding Decomposition

[165] figure: Listing 2: Atomic Fact Decomposition ⬇ You are given a factual statement ( a claim ) from a technical report . Break the claim down into independent , minimal atomic facts that can each be verified in isolation . Keep each atomic fact short , declarative , and free of conjunctions when possible . Avoid duplicating the same content in multiple ways unless it clarifies distinct atomic facts ( e . g ., subject + membership vs subject + role ). Format : - Return a JSON array of strings . Each string is one atomic fact . - Do not include any extra commentary or Markdown . Only return the JSON array . Examples : Input : " He was an American composer , conductor , and musical director ." Output : [ " He was an American .", " He was a composer .", " He was a conductor .", " He was a musical director ." ] Input : " She currently stars in the romantic comedy series , Love and Destiny , which premiered in 2019." Output : [ " She currently stars in Love and Destiny .", " Love and Destiny is a romantic comedy series .", " Love and Destiny premiered in 2019." ] Input : " During his professional career , McCoy played for the Broncos , the San Diego Chargers , the Minnesota Vikings , and the Jacksonville Jaguars ." Output : [ " McCoy played for the Broncos .", " McCoy played for the Broncos during his professional career .", " McCoy played for the San Diego Chargers .", " McCoy played for the San Diego Chargers during his professional career .", " McCoy played for the Minnesota Vikings .", " McCoy played for the Minnesota Vikings during his professional career .", " McCoy played for the Jacksonville Jaguars .", " McCoy played for the Jacksonville Jaguars during his professional career ." ] Input : " The EU approved the AI Act in 2024 and introduced new compliance requirements ." Output : [ " The EU approved the AI Act in 2024.", " The AI Act introduced new compliance requirements ." ] Input : " The Amazon River is the largest by discharge and flows into the Atlantic Ocean ." Output : [ " The Amazon River is the largest river by discharge .", " The Amazon River flows into the Atlantic Ocean ." ] Now decompose the following claim into atomic facts and return only a JSON array of strings :

[166] h3: B.3 Answer Extraction

[167] figure: Listing 3: Atomic Fact Decomposition ⬇ ## Task Description Extract the answer to the research question from the provided report . ## Input A Research Question and a complete report containing the answer . ## Output Requirements Extract the direct answer to the research question Provide supporting evidence / context from the report Return a JSON object with the answer and supporting context ## Format Specification { " question ": " The research question ", " answer ": " The direct answer extracted from the report ", " supporting_context ": " Key passages from the report that support this answer " } ## Guidelines 1. Focus on directly answering the research question 2. Be concise but comprehensive 3. Include relevant evidence and context 4. Maintain factual accuracy

[168] h2: Appendix C Additional Details

[169] h3: C.1 Instantiation 2: Open Deep Research

[170] p: The Outer Loop (Supervisor). The outer loop operates on the global research state. It operates over a sequence of discrete steps t = 1 , 2 , … , T t=1,2,...,T . We define the components as follows:

[171] p: Information Acquisition ( π query outer \pi_{\text{query}}^{\text{outer}} ): The outer loop thinking strategy is parameterized by a backbone LLM. It generates an action a t ∈ 𝒮 outer ∪ 𝒯 outer a_{t}\in\mathcal{S}^{\text{outer}}\cup\mathcal{T}^{\text{outer}} , where 𝒮 outer \mathcal{S}^{\text{outer}} is the space of research topics and 𝒯 outer \mathcal{T}^{\text{outer}} is the termination signal.

[172] p: Search Engine ( β engine outer \beta_{\text{engine}}^{\text{outer}} ): If a t ∈ 𝒮 outer a_{t}\in\mathcal{S}^{\text{outer}} , the agent executes the inner loop to generate synthesized reports i t ∼ InnerLoop ( ⋅ ∣ a t ) i_{t}\sim\text{InnerLoop}(\cdot\mid a_{t}) .

[173] p: Information Compression ( π sum outer \pi_{\text{sum}}^{\text{outer}} ): The outer loop does not conduct this step. Therefore, h t = 𝟙 ​ ( i t ) h_{t}=\mathbb{1}(i_{t}) , where 𝟙 \mathbb{1} is the identity function.

[174] p: Inference ( π update outer \pi_{\text{update}}^{\text{outer}} ): The outer belief is updated by appending the synthesized report returned by the inner-process: 𝐛 t + 1 = Append ​ ( 𝐛 t , a t , h t ) \mathbf{b}_{t+1}=\text{Append}(\mathbf{b}_{t},a_{t},h_{t}) .

[175] p: The Inner Loop (Researcher). The inner loop realizes the engine β engine outer \beta_{\text{engine}}^{\text{outer}} for the outer loop. It operates over a sequence of discrete steps k = 1 , 2 , … , K k=1,2,...,K . We define the components as follows:

[176] p: Information Acquisition( π query inner \pi_{\text{query}}^{\text{inner}} ): A reactive LLM policy that generates an action a k ∈ 𝒮 inner ∪ 𝒯 inner a_{k}\in\mathcal{S}^{\text{inner}}\cup\mathcal{T}^{\text{inner}} , where 𝒮 inner \mathcal{S}^{\text{inner}} represents search queries and 𝒯 inner \mathcal{T}^{\text{inner}} is the local stop signal.

[177] p: Search Engine ( β engine inner \beta_{\text{engine}}^{\text{inner}} ): If a k ∈ 𝒮 inner a_{k}\in\mathcal{S}^{\text{inner}} , the search engine returns raw information i k ∼ β engine inner ( ⋅ ∣ a k ) i_{k}\sim\beta_{\text{engine}}^{\text{inner}}(\cdot\mid a_{k}) .

[178] p: Information Compression ( π sum inner \pi_{\text{sum}}^{\text{inner}} ): An information processing policy condenses raw information i k i_{k} into a concise observation h k ∼ π sum inner ( ⋅ ∣ i k ) h_{k}\sim\pi_{\text{sum}}^{\text{inner}}(\cdot\mid i_{k}) .

[179] p: Inference ( π update inner \pi_{\text{update}}^{\text{inner}} ): The inner belief is updated by appending the concise observation into the current belief state: 𝐛 k + 1 = Append ​ ( 𝐛 k , a k , h k ) \mathbf{b}_{k+1}=\text{Append}(\mathbf{b}_{k},a_{k},h_{k}) .

[180] h3: C.2 Details about Evaluation Metrics

[181] h4: C.2.1 Probabilistic Interpretation

[182] p: For the one-hot encoding vector 𝐘 \mathbf{Y} , let 𝐲 i \mathbf{y}_{i} denote the one-hot vector representation of the outcome y ( i ) y^{(i)} from run i i . Since 𝐲 i \mathbf{y}_{i} is a standard basis vector, it has unit norm ( ‖ 𝐲 i ‖ 2 = 1 \|\mathbf{y}_{i}\|_{2}=1 ). Consequently, the squared Euclidean distance between two runs simplifies to a discrete metric:

[183] table: ‖ 𝐲 i − 𝐲 j ‖ 2 = { 0 if ​ y ( i ) ≡ y ( j ) 2 if ​ y ( i ) ≢ y ( j ) \|\mathbf{y}_{i}-\mathbf{y}_{j}\|^{2}=\begin{cases}0&\text{if }y^{(i)}\equiv y^{(j)}\\ 2&\text{if }y^{(i)}\not\equiv y^{(j)}\end{cases} (12)

[184] p: Substituting this into Eq. ( 6 ), the estimator reduces to the proportion of discordant pairs across all possible comparisons:

[185] table: TV ^ ​ ( 𝐘 ) = 1 n ⁡ ( n − 1 ) ​ ∑ i ≠ j 𝕀 ⁡ ( y ( i ) ≢ y ( j ) ) . \widehat{\text{TV}}(\mathbf{Y})=\frac{1}{n(n-1)}\sum_{i\neq j}\mathbb{I}(y^{(i)}\not\equiv y^{(j)}). (13)

[186] p: This value represents the empirical probability that two independently sampled runs will produce different answers.

[187] p: For binary vectors 𝐁 , 𝐂 \mathbf{B},\mathbf{C} , the squared distance between two normalized vectors relates directly to their Cosine similarity:

[188] table: ‖ 𝐱 ~ i − 𝐱 ~ j ‖ 2 = 2 − 2 ​ ( 𝐱 ~ i ⋅ 𝐱 ~ j ) . \|\widetilde{\mathbf{x}}_{i}-\widetilde{\mathbf{x}}_{j}\|^{2}=2-2(\widetilde{\mathbf{x}}_{i}\cdot\widetilde{\mathbf{x}}_{j}). (14)

[189] p: Substituting the cosine identity ‖ 𝐱 ~ i − 𝐱 ~ j ‖ 2 = 2 − 2 ​ ( 𝐱 ~ i ⋅ 𝐱 ~ j ) \|\widetilde{\mathbf{x}}_{i}-\widetilde{\mathbf{x}}_{j}\|^{2}=2-2(\widetilde{\mathbf{x}}_{i}\cdot\widetilde{\mathbf{x}}_{j}) into Eq. ( 6 ), the estimator simplifies to the average complement of the cosine similarity:

[190] table: TV ^ = 1 − 1 n ⁡ ( n − 1 ) ​ ∑ i ≠ j ( 𝐱 ~ i ⋅ 𝐱 ~ j ) . \widehat{\text{TV}}=1-\frac{1}{n(n-1)}\sum_{i\neq j}(\widetilde{\mathbf{x}}_{i}\cdot\widetilde{\mathbf{x}}_{j}). (15)

[191] p: We use findings as an illustrative example. Let S i S_{i} denote the set of finding indices discovered in run i i . Consider two runs i i and j j . Assuming the volume of findings is consistent across runs such that | S i | = | S j | = k |S_{i}|=|S_{j}|=k , the dot product of the normalized vectors approximates the conditional probability of recurrence:

[192] table: 𝐱 ~ i ⋅ 𝐱 ~ j \displaystyle\widetilde{\mathbf{x}}_{i}\cdot\widetilde{\mathbf{x}}_{j} = | S i ∩ S j | | S i | ​ | S j | \displaystyle=\frac{|S_{i}\cap S_{j}|}{\sqrt{|S_{i}||S_{j}|}} = | S i ∩ S j | k \displaystyle=\frac{|S_{i}\cap S_{j}|}{k} = P ⁡ ( finding ∈ S j ∣ finding ∈ S i ) . \displaystyle=P(\text{finding}\in S_{j}\mid\text{finding}\in S_{i}). (16)

[193] p: Taking the expectation over all pairs, we arrive at the following probabilistic interpretation:

[194] table: 𝔼 ⁡ [ TV ^ ] = 1 − P ⁡ ( finding ∈ S j ∣ finding ∈ S i ) . \mathbb{E}[\widehat{\text{TV}}]=1-P(\text{finding}\in S_{j}\mid\text{finding}\in S_{i}). (17)

[195] h4: C.2.2 Incorporating Semantic Geometry

[196] p: In our primary analysis, we treat answers and findings as categorical distributions — disagreeing on ‘cat’ vs. ‘dog’ incurs the same penalty as ‘cat’ vs. ‘car’. If we consider the semantic geometry of answers (i.e., answer ‘cat’ is closer to ‘dog’ than to ‘car’ in some embedding space) and findings, our TV framework naturally extends to this setting by redefining the realization vectors using embedding distances.

[197] p: For a semantic space equipped with a similarity metric s ⁡ ( u , v ) ∈ [ 0 , 1 ] s(u,v)\in[0,1] , we can generalize our vector construction.

[198] p: Answers: Instead of a one-hot vector 𝐞 k \mathbf{e}_{k} , the realization 𝐲 i \mathbf{y}_{i} becomes the dense embedding vector 𝐯 y ( i ) \mathbf{v}_{y^{(i)}} . The Euclidean distance ‖ 𝐲 i − 𝐲 j ‖ 2 \|\mathbf{y}_{i}-\mathbf{y}_{j}\|^{2} then directly captures semantic divergence (e.g., small for ‘cat’ vs. ‘dog’, large for ‘cat’ vs. ‘car’).

[199] p: Findings/Citations: If the global set of findings is { f 1 , … , f K } \{f_{1},\dots,f_{K}\} , the k k -th entry of 𝐛 i \mathbf{b}_{i} can be defined as max f ∈ S i ⁡ s ⁡ ( f k , f ) \max_{f\in S_{i}}s(f_{k},f) . For example, suppose the global findings are { cat , dog , car } \{\text{cat},\text{dog},\text{car}\} with s ⁡ ( cat , dog ) = 0.8 s(\text{cat},\text{dog})=0.8 .

[200] p: A run finding only “cat” yields 𝐛 = [ 1 , 0.8 , 0 ] \mathbf{b}=[1,0.8,0] .

[201] p: A run finding “dog” and “car” yields 𝐛 = [ 0.8 , 1 , 1 ] \mathbf{b}=[0.8,1,1] .

[202] p: In this formulation, TV can be used to measure the variance of the agent’s output in the semantic embedding space rather than the discrete symbolic space.

[203] h4: C.2.3 Sensitivity to Relative Scale

[204] p: A potential concern with using L 2 L_{2} normalization is that it discards the absolute magnitude of the vectors (i.e., the total number of findings). However, this property is desirable for measuring stability: it ensures that our metric focuses on the relative consistency of the information retrieved, rather than the raw volume.

[205] p: To illustrate this, consider how the metric penalizes a “single omission’ error — where one run misses exactly one finding discovered by another run. Intuitively, missing 1 finding out of 10 is a more severe failure of consistency compared to missing 1 finding out of 100. Our normalized TV ^ \widehat{\text{TV}} captures this distinction. As an example, we compare two scenarios where Run 1 generates a set of findings S 1 S_{1} and Run 2 generates S 2 S_{2} , with an intersection size of | S 1 ∩ S 2 | |S_{1}\cap S_{2}| .

[206] p: Case A: The agent discovers 100 findings in Run 1, but misses one in Run 2 ( | S 1 | = 100 , | S 2 | = 99 , | S 1 ∩ S 2 | = 99 |S_{1}|=100,|S_{2}|=99,|S_{1}\cap S_{2}|=99 ).

[207] table: TV ^ A = 1 − 99 100 × 99 = 1 − 0.995 = 0.005 \widehat{\text{TV}}_{A}=1-\frac{99}{\sqrt{100\times 99}}=1-0.995=\mathbf{0.005}

[208] p: Case B: The agent discovers 10 findings in Run 1, but misses one in Run 2 ( | S 1 | = 10 , | S 2 | = 9 , | S 1 ∩ S 2 | = 9 |S_{1}|=10,|S_{2}|=9,|S_{1}\cap S_{2}|=9 ).

[209] table: TV ^ B = 1 − 9 10 × 9 = 1 − 0.949 = 0.051 \widehat{\text{TV}}_{B}=1-\frac{9}{\sqrt{10\times 9}}=1-0.949=\mathbf{0.051}

[210] p: Although the absolute disagreement is identical (1 finding difference) in both cases, the estimator assigns a penalty to Case B that is an order of magnitude larger ( ≈ 10 × \approx 10\times ). This confirms that TV ^ \widehat{\text{TV}} correctly scales.

[211] h3: C.3 Mitigation in API Setting through Temperature Tuning

[212] figure: Table 5: Stochasticity and Accuracy Metrics across Sampling Temperatures ( λ \lambda ) under API Setting. Metric T = 0 T=0 λ = 0.5 \lambda=0.5 λ = 1.0 \lambda=1.0 TV ^ ​ ( 𝐘 ) \widehat{\mathrm{TV}}(\mathbf{Y}) 0.700 0.670 0.620 TV ^ ​ ( 𝐁 ) \widehat{\mathrm{TV}}(\mathbf{B}) 0.828 0.836 0.834 TV ^ ​ ( 𝐂 ) \widehat{\mathrm{TV}}(\mathbf{C}) 0.621 0.608 0.612 Accuracy 0.28 0.24 0.24

[213] h3: C.4 Example for Structured Output

[214] figure: Listing 4: Structured Reasoning Output ⬇ < reasoning >{\ n \" established_facts \": [],\ n \" open_questions \": [\ n \" Which countries were in the top 10 with the lowest GPI scores in both 2022 and 2023 according to Vision of Humanity ?\",\ n \" Of those countries , which had a gun homicide rate below 0.20 per 100,000 population in both 2022 and 2023 according to World Population Review ?\",\ n \" Are the GPI scores and gun homicide rate data available and comparable for the same set of countries across both years ?\"\ n ],\ n \" next_search_directions \": [\ n \" Search for the Global Peace Index ( GPI ) 2022 and 2023 reports from Vision of Humanity to identify the top 10 most peaceful countries ( lowest scores ).\",\ n \" Cross - reference the list of countries that appear in both the 2022 and 2023 top 10 lowest GPI scores .\",\ n \" Search World Population Review ’ s data for gun homicide rates in 2022 and 2023 for those countries .\",\ n \" Filter countries with gun homicide rates less than 0.20 per 100,000 in both years .\"\ n ],\ n \" contradictions_or_uncertainties \": [\ n \" Potential mismatch in country naming or classification between Vision of Humanity and World Population Review .\",\ n \" Possible discrepancies in reporting years or data collection methods between the two sources .\",\ n \" Uncertainty about whether World Population Review reports gun homicide rates for all countries listed in the GPI top 10.\"\ n ]\ n }</ reasoning >

[215] h2: Instructions for reporting errors

[216] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[217] p: Tip: You can select the relevant text first, to include it in your report.

[218] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[219] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
