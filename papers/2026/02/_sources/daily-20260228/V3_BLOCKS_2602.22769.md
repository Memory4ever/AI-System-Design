[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: AMA- Bench: Evaluating Long-Horizon Memory for Agentic Applications

[3] h6: Abstract

[4] p: Large Language Models (LLMs) are deployed as autonomous agents in increasingly complex applications, where enabling long-horizon memory is critical for achieving strong performance. However, a significant gap exists between practical applications and current evaluation standards for agent memory: existing benchmarks primarily focus on dialogue-centric, human-agent interactions. In reality, agent memory consists of a continuous stream of agent-environment interactions that are primarily composed of machine-generated representations. To bridge this gap, we introduce AMA- Bench ( A gent M emory with A ny length), to evaluates long-horizon memory for LLMs in real agentic applications. It features two key components: (1) a set of real-world agentic trajectories across representative agentic applications, paired with expert-curated QA, and (2) a set of synthetic agentic trajectories that scale to arbitrary horizons paired with rule-based QA. Our comprehensive study shows that existing memory systems underperform on AMA-Bench primarily because they lack causality and objective information, and are constrained by the lossy nature similarity-based retrieval employed by many memory systems. To address these limitations, we propose AMA- Agent , an effective memory system featuring a causality graph and tool-augmented retrieval. Our results demonstrate that AMA- Agent achieves 57.22 % 57.22\% average accuracy on AMA- Bench, surpassing the strongest memory system baselines by 11.16 % 11.16\% .

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] figure: Figure 1 : Comparison of memory across reasoning, chatbots, and agent applications. Agent trajectories exhibit unique properties, including being causally grounded, diverse symbolic artifacts, and dense objective information.

[8] figure: Figure 2 : Model performance across agent task families in AMA- Bench.

[9] p: Large Language Models (LLMs) have rapidly evolved from solving closed-form reasoning tasks (Fig. 1 (a)) and serving as chatbots (Fig. 1 (b)), to serving as autonomous agents (Fig. 1 (c)). Autonomous agents require long-horizon reasoning and experience reuse to complete tasks like open-space navigation, code editing, and web search. To empower LLMs with these capabilities, agent memory has become an important component of agent design to manage LLM context ( Wang et al., 2025b ; Agashe et al., 2024 ) . Strong memory modules are expected to satisfy two core capabilities: (1) effective memory processing, where complete agentic trajectories are transformed into structured factual representations, such as summaries, fact tables, or embeddings ( Edge et al., 2025 ; Packer et al., 2023 ; Liu et al., 2026 ) ; and (2) effective memory retrieval, reliably selecting and leveraging the most relevant memory to guide decision-making. Existing benchmarks typically evaluate these capabilities in dialogue-centric or synthetic retrieval tasks ( Hsieh et al., 2024 ; Maharana et al., 2024 ) , focusing on specific subcomponents, such as single- or multi-hop questions for memory retrieval or state updating and memory condensation questions for memory processing. There is a lack of benchmarks and evaluations of memory modules in long-horizon agentic tasks.

[10] p: Real-world agents mainly operate in machine generated environments such as databases, code executors, and web interfaces, where they must process large volumes of machine generated representations . Yet, most existing memory benchmarks are still natural language centric and have three key limitations: (1) A lack of representation types : Agent trajectories encompass diverse machine generated symbolics (e.g., ASCII tables, JSON data, Unicode snippets, Python or HTML code blocks), whereas current benchmarks predominantly center on free-form natural languages; (2) A lack of causality : agent trajectories are causally grounded, where each action induces a latent environment state transition that constrains subsequent observations; but existing benchmarks follow unconstrained linguistic flow; (3) Sparse objective information : agent trajectories are machine-generated and objective, whereas dialog-centric benchmarks contain abundant redundant information such as phatic chit-chat.

[11] figure: Figure 3 : Domain and question type distribution in AMA- Bench.

[12] p: To bridge this gap, we introduce AMA- Bench (Benchmarking Agent Memory with Any length), which comprises two complementary subsets: a real-world subset and a synthetic subset. The real-world component consists of expert-annotated and sanity-checked Question-Answer (QA) pairs sourced from six representative agent domains: Web, open-world QA, Text2SQL, Software Engineering, Gaming, and Embodied AI (see Fig. 3 ). Furthermore, we construct a synthetic subset in programmatic agent environments with automatically generated QA pairs. This design enables controlled synthesis of tasks at arbitrary horizons while keeping the agent-environment interaction pattern.

[13] p: As shown in Fig. 2 , our systematic evaluation indicates that agent memory remains challenging even for frontier commercial models, with GPT 5.2 achieving only 72.26% accuracy. Evaluating memory systems on AMA- Bench yields three key insights : (1) While existing agent memory techniques often outperform long-context LLM baselines on dialogue-centric benchmarks, they fall short to the baselines in many long-horizon agentic tasks, highlighting the unique diagnostic value of our benchmark (Sec. 4 ); (2) Our analysis reveals that suboptimal memory system design, rather than base model capability, serves as the primary bottleneck for their poor performance (Sec. 4 ); (3) Existing lossy compression and similarity-based retrieval techniques are insufficient for the nuanced demands of agent memory, necessitating a paradigm shift toward agent-centric memory management strategies (Sec. 4 ).

[14] p: Motivated by these insights, we present AMA- Agent, a framework designed to address the memory demands of agentic applications. Moving beyond lossy compression or similarity-based graphs, AMA- Agent implements a Causality Graph to preserve the objective information and explicit causal dependencies within interaction histories. To transcend the limitations of similarity-based retrieval, we introduce a Hybrid Tool-Augmented Retrieval mechanism. This approach enables more efficient information extraction and synthesis in machine-generated representations.

[15] p: This paper makes the following main contributions:

[16] p: AMA- Bench. We introduce the first benchmark suite built for evaluating memory in agent applications, AMA- Bench, with two complementary subsets: Real world preserves authentic machine-generated interaction patterns, and a Synthetic suite that enables controlled scaling of any horizon length and complexity.

[17] p: Comprehensive Evaluations. Through comprehensive evaluation using AMA-Bench, we show that many existing agent memory designs underperform the long-context baseline, as errors introduced by lossy memory compression and similarity-based retrieval accumulate and compound over long-horizon agentic tasks; this highlights the critical need for agent-centric memory designs.

[18] p: AMA- Agent. We propose AMA- Agent that addresses the identified bottlenecks with two mechanisms: (i) Causality Graph that preserves the integrity of objective information and causal dependencies, and (ii) Tool-Augmented Retrieval, which utilizes both graph node search and keyword-based search. Experimental results show that AMA- Agent outperforms the strongest existing memory baselines by 11.16 % 11.16\% on average.

[19] h2: 2 Related Work

[20] figure: Table 1: Comparison of memory benchmarks. NL: Natural Language. Category Benchmark Interaction Content Average Length Representation Memory Paradigm Source (tokens) Types Organization Dialogue-Centric LoCoMo ( Maharana et al., 2024 ) Dialogue Real + Synthetic 9K NL + Vision Episodic LongMemEval ( Wu et al., 2025 ) Dialogue Synthetic 115K NL Multi-session MemoryAgentBench ( Hu et al., 2025b ) Dialogue Real + Synthetic 100K–500K NL Multi-domain MemoryBench ( Ai et al., 2025 ) Dialogue Real + Synthetic ∼ \sim 30–380K NL Multi-session + Feedback RealTalk ( Lee et al., 2025 ) Dialogue Real 17K NL Multi-day Long-Context QuALITY ( Pang et al., 2022 ) Long-Context Real 5K NL Multi-hop RULER ( Hsieh et al., 2024 ) Long-Context Synthetic 4K–128K NL Single-turn LongBench v2 ( Bai et al., 2025 ) Long-Context Real 8K–2M NL Document-level Agent-Centric AMA-Bench Agent-Env Real + Synthetic 57K NL + Machine Trajectory-based

[21] h3: 2.1 Agent Memory Evaluation

[22] p: We categorize existing memory benchmarks into two primary classes (as shown in Tab. 1 ): Dialogue-Centric and Long-Context. Dialogue-centric benchmarks evaluate memory retention over multi-turn human-agent interactions. LoCoMo ( Maharana et al., 2024 ) and LongMemEval ( Wu et al., 2025 ) evaluate long-term interactive memory in assistant-style chats; MemoryAgentBench ( Hu et al., 2025b ) tests multiple long-term memory competencies across diverse memory capabilities; MemoryBench ( Ai et al., 2025 ) unifies diverse memory tasks into a continual learning suite; and RealTalk ( Lee et al., 2025 ) grounds long-term memory evaluation in multi-day human dialogues. Long-context benchmarks such as QuALITY ( Pang et al., 2022 ) , RULER ( Hsieh et al., 2024 ) , and LongBench v2 ( Bai et al., 2025 ) evaluate static document-level reasoning, focusing on multi-hop comprehension over long inputs rather than interactive or incremental memory. In contrast, AMA-Bench evaluates memory for agent applications, where the interaction trajectory is characterized by machine-generated representations, causal dependencies, and dense, objective information.

[23] h3: 2.2 Agent Memory Mechanisms

[24] p: Three main approaches have been explored to equip agents with long-horizon memory.

[25] p: Long-Context Models. The first direction adapts LLMs to process memory directly as the context. For instance, GPT 5.2 ( OpenAI, 2025 ) exposes an effective context window of approximately 400,000 tokens. On the open-source side, the Qwen2.5 1M ( Yang et al., 2025b ) series extends models to 100,000 tokens. Although simple and often strong in practice, this strategy remains bounded by physical context limits.

[26] p: Retrieval-Augmented Generation (RAG). Another prominent research direction is RAG, which externalizes information into external storage during the memory construction stage and fetches relevant items based on similarity to augment the model’s context during retrieval. Traditional methods, such as BM25 ( Robertson and Zaragoza, 2009 ) and the Qwen3 Embedding series ( Zhang et al., 2025b ) , store memory by partitioning data into discrete chunks. Structured RAG approaches have emerged to capture more complex relationships. For instance, GraphRAG ( Edge et al., 2025 ) utilizes graph-based retrieval by constructing and aggregating entity-document graphs to capture these structural dependencies. Furthermore, HippoRAG2 ( Gutiérrez et al., 2025 ) formalizes retrieval as a nonparametric form of Despite these advances, existing methods primarily rely on similarity-based or entity-centric retrieval, often neglecting the underlying causality within stored information.

[27] p: Memory Agent Systems. Recent research has shifted from rule-based RAG pipelines to agent-centric memory management, where LLM agents autonomously decide how to perform memory construction and retrieval. MemoryBank ( Zhong et al., 2023 ) enables models to autonomously summon and update the stored memories. MemGPT ( Packer et al., 2023 ) formulates memory access as a decision problem, where the LLM learns when to retrieve and how to manage the long-term context. MemoRAG ( Qian et al., 2025 ) proposes a dual system RAG architecture that maintains a global memory store and retrieves semantically similar clues to assemble a high-level draft for answering. MEM1 ( Zhou et al., 2025 ) , Mem- α \alpha ( Wang et al., 2025a ) , Mem0 ( Chhikara et al., 2025 ) , MemAgent ( Yu et al., 2025 ) , and A MEM ( Xu et al., 2025 ) construct memory by iterative compression or edit-style operations such as insertion, deletion, and modification, and then directly condition generation on the compressed memory. SimpleMem ( Liu et al., 2026 ) introduced a structured compression pipeline that filters redundancy, organizes memories into hierarchies, and adaptively retrieves relevant contexts. However, memory compression and similarity-based retrieval perform poorly on agent memory tasks for two main reasons. First, most compression methods are designed for natural language, where redundancy and subjective fillers are common. However, agent trajectories contain dense, causally structured state transitions. Second, agent memories are often machine-generated representations, and similarity retrieval frequently fails to extract the required evidence.

[28] h2: 3 AMA- Bench

[29] p: In this section, we introduce AMA- Bench (Benchmarking A gent M emory with A ny length), a benchmark suite designed to evaluate memory systems in agent-centric memory. We first present a general problem formulation that abstracts agent-environment interaction and provides a unified definition of memory systems for agent applications in Sec. 3.1 . Building on this formulation, Sec. 3.2 identifies which memory capabilities are essential for long-horizon decision-making and operationalizes them as evaluation dimensions. Finally, Sec. 3.3 describes how we construct AMA- Bench, including both real-world and synthetic subsets.

[30] h3: 3.1 Problem formulation

[31] p: Agent Environment Interactions. We consider LLM agents operating within the reason and act paradigm ( Yao et al., 2022 ; Shinn et al., 2023 ; Wang et al., 2023 ) , where sequential decision-making is formulated as a Partially Observable Markov Decision Process (POMDP) defined by the tuple ℳ = ( 𝒮 , 𝒜 , 𝒪 , P , r ) \mathcal{M}=(\mathcal{S},\mathcal{A},\mathcal{O},P,r) (See Fig. 4 (a)). At each time step t t , the environment resides in a latent state s t ∈ 𝒮 s_{t}\in\mathcal{S} . Upon executing an action a t ∈ 𝒜 a_{t}\in\mathcal{A} , the agent receives an observation o t ∈ 𝒪 o_{t}\in\mathcal{O} sampled from the observation function O ⁡ ( s t ) O(s_{t}) , and the environment transitions to s t + 1 s_{t+1} according to the dynamics P ⁡ ( s t ∣ s t , a t + 1 ) P(s_{t}\mid s_{t},a_{t+1}) . Given a task instruction x x , the interaction generates a trajectory history h t = ( x , a 1 , o 1 , … , o t ) h_{t}=(x,a_{1},o_{1},\dots,o_{t}) . The partial observability motivates an explicit memory mechanism to persist the agent memory.

[32] p: The Memory System. We formalized a memory system through two stages (see Fig. 4 (a)), memory construction ( 𝖡𝗎𝗂𝗅𝖽 ) (\mathsf{Build}) and memory retrieval, ( 𝖱𝖾𝗍𝗋𝗂𝖾𝗏𝖾 ) (\mathsf{Retrieve}) . The construction stage, 𝖡𝗎𝗂𝗅𝖽 : ℋ → ℳ mem \mathsf{Build}:\mathcal{H}\to\mathcal{M}_{\mathrm{mem}} , maps the interaction history h t h_{t} to an external memory state m t ∈ ℳ mem m_{t}\in\mathcal{M}_{\mathrm{mem}} . The memory space ℳ mem \mathcal{M}_{\mathrm{mem}} accommodates diverse structured representations, such as recursive summaries, knowledge graphs, and vector embeddings ( Edge et al., 2025 ; Packer et al., 2023 ; Liu et al., 2026 ) . Upon receiving a query q t q_{t} , the retrieval module extracts a query-relevant context c t = 𝖱𝖾𝗍𝗋𝗂𝖾𝗏𝖾 ⁡ ( m t , q t ) c_{t}=\mathsf{Retrieve}(m_{t},q_{t}) . The agent policy π \pi then determines the subsequent response based on the retrieved context and query: a t ∼ π ( ⋅ ∣ q t , c t ) a_{t}\sim\pi(\cdot\mid q_{t},c_{t}) .

[33] figure: Figure 4 : Formalizing memory system and capability for agentic applications.

[34] figure: Table 2 : Memory capability described in Sec 3.2 . We group evaluation dimensions into three mechanisms and four capabilities. Mechanism Capability Description Memory Retrieval A. Recall Identification of Temporal and sequential information. B. Causal Inference Verification of action preconditions and dependency relations between states. Memory Evolution C. State Updating Tracking updates to states, including explicit observations and hidden states. Memory Condensation D. State Abstraction Filtering redundant content while extracting precise and condensed key information.

[35] h3: 3.2 Memory Capability Categories

[36] p: The proposed formulation, supported by recent literature ( Du et al., 2025 ; Zhang et al., 2024 ) , underscores that an effective memory system must facilitate three core mechanisms: 1. Memory Retrieval: targeted access to the correct evidence. 2. Memory Evolution: continually updates memory as new observations arrive. 3. Memory Condensation: precisely extracting and condensing memory without information loss. Aligning these essential mechanisms with the specific requirements of agent-based tasks, we categorize memory capabilities into four functional capabilities. The formal definitions are detailed in Tab. 2 , while illustrative examples are provided in Fig. 4 (b). These mechanisms encompass: Recall and Causal Inference (Retrieval), State Updating (Evolution), and State Abstraction (Condensation).

[37] h3: 3.3 Benchmark Construction

[38] p: With the above formulation and capability taxonomy, we now describe how we build AMA- Bench to jointly capture real-world complexity and provide controllable scaling complexity. AMA- Bench comprises two complementary components: (i) a real-world subset and (ii) a synthetic subset.

[39] figure: Figure 5 : Synthetic subset construction pipeline. We synthesize an executable environment backend with explicit latent states and transitions, render machine-generated observations to form trajectories, and programmatically generate trajectory-grounded QA pairs.

[40] h4: 3.3.1 Real-world Subset

[41] p: We curate high-quality, long-horizon trajectories from six representative real-world agent tasks, including web navigation, software engineering, text-to-SQL, embodied AI, gaming, and open-world tool with 2496 QA pairs (see Fig. 3 and Tab. 8 in Appendix A for the detailed category). For each task family, we gathered action-observation interaction traces from representative benchmarks using either state-of-the-art agent frameworks or expert-level trajectories provided directly by the environment. From this pool, we curated a subset for annotation, prioritizing longer trajectories while maintaining the original task distribution within each family. Specific details regarding the benchmarks and frameworks used are provided in Appendix A .

[42] p: The real-world environments are treated as black boxes: we only observe agent-environment interaction logs (action and observation trajectories) and do not have access to the environment backend state. Building on the capability taxonomy in Sec. 3.2 , we manually annotate each selected trajectory with 12 memory-intensive QA pairs that collectively cover all categories in Tab. 2 . Each question is formulated such that its answer is supported by explicit and unambiguous evidence within the trajectory, ensuring that the correctness of the question can be verified from the log itself.

[43] p: QA pairs are then authored by graduate-level annotators with research experience in LLM agents, following shared guidelines that standardize evidence grounding and category coverage across six domains. To improve annotation reliability, each annotated trajectory undergoes a cross-review sanity check by a second annotator. This protocol yields expert-level QA annotations that are trajectory-grounded, category-aligned, and consistent across the task families. Examples of trajectories and QA are listed in Appendix E.1 .

[44] h4: 3.3.2 Synthetic Subset

[45] p: To systematically evaluate agent memory scaling, we construct a synthetic subset via programmatic environment synthesis. Each instance comprises an executable backend with controllable state transitions and a tunable perception interface, enabling the generation of verifiable trajectories with arbitrary horizons. Fig. 5 shows the pipeline of the synthetic subset construction. We synthesize tasks from two distinct environments characterized by long-range dependencies and partial observability: TextWorld ( Côté et al., 2018 ) , BabyAI ( Chevalier-Boisvert et al., 2019 ) . The description of the two tasks is listed in Appendix A.2 .

[46] p: Environment Synthesis. We parameterize each instance using a difficulty vector ϕ \phi and a random seed to synthesize the environment backend. The latent state s t s_{t} and transition kernel s t + 1 = P ϕ ​ ( s t , a t + 1 ) s_{t+1}=P_{\phi}(s_{t},a_{t+1}) are programmatically defined and machine-verifiable. This allows us to systematically scale the interaction context length L L by increasing the environmental difficulty as dictated by ϕ \phi . For instance, in BabyAI, ϕ \phi encompasses parameters such as the grid dimensions, the number of rooms, and the length of the instruction chain. By increasing the map size or adding nested dependencies, we can provably extend the trajectory length L L .

[47] p: Trajectory Synthesis. The synthetic nature of our environments grants full access to the environment MDP, enabling the derivation of an optimal policy π ∗ \pi^{*} despite the agent’s partial observability. We generate stepwise sequences { ( a t , o t ) } t = 1 T \{(a_{t},o_{t})\}_{t=1}^{T} grounded in these gold-standard transitions to resolve the issue of low-structural density. To further address representational diversity and robustness, we introduce two auxiliary perturbations beyond ϕ \phi : (1) Action Stochasticity ( ϵ \epsilon ): we inject random noise into π ∗ \pi^{*} to simulate sub-optimal action ratios, testing memory robustness under varying agent policies; and (2) Observation Verbosity ( γ \gamma ): we employ various symbolic representations with controllable descriptive granularity γ \gamma for o t o_{t} .

[48] p: QA Synthesis. Since we have access to the full MDP, we can programmatically generate golden QA pairs anchored to backend state variables such as state s t s_{t} or transition kernel s t + 1 = P ϕ ​ ( s t , a t ) s_{t+1}=P_{\phi}(s_{t},a_{t}) .

[49] p: Needle Synthesis. Following the widely used needle-in-a-haystack (NIAH) paradigm ( Nelson et al., 2024 ; Hsieh et al., 2024 ; Kamradt, ) for evaluating memory capabilities, we also instantiate a needle protocol in AMA- Bench. The needle here is the minimal set of trajectory turn IDs that contains all the evidence necessary to answer a query. Crucially, because AMA- Bench is backed by a programmatic environment, we can automatically synthesize and verify the needles. More details about the needle generation pipeline are listed in Appendix F .

[50] figure: Figure 6 : LLM-as-a-judge accuracy across different memory systems using Qwen3-32B as the base model.

[51] h2: 4 Empirical Motivation

[52] p: We benchmarked a broad set of representative memory systems on the AMA-Bench (see Fig. 6 ). The results reveal three key empirical insights that highlight the current limitations and directly motivate the design of our proposed method in Sec. 2.2 .

[53] h3: Motivation1: Memory systems fall short of the long-context baseline.

[54] p: Fig. 6 compares representative memory systems against a long context baseline across six agent task families. A clear pattern emerges: the long context baseline is consistently strong and often achieves the best performance, whereas existing memory systems exhibit large variance across families and frequently underperform, even when they introduce structured memory construction or retrieval augmentation.

[55] h3: Motivation2: Memory Design bottlenecks the model performance.

[56] figure: Figure 7 : Impact of Model Scale vs. Memory Architecture. While scaling the backbone yields marginal gains, the choice of memory system accounts for the majority of performance variance.

[57] p: A central question in building memory-augmented agents is whether performance bottlenecks reside in the backbone capacity or memory system design. Fig. 7 illustrates that scaling from 8B to 32B provides only marginal improvements (avg. improvement is 0.038), whereas varying the memory architecture induces significantly higher variance, with score ranges reaching 0.45.

[58] h3: Motivation3: Limitations of Existing Memory System Designs.

[59] p: To further pinpoint bottlenecks, we performed needle protocol ablation in BabyAI with three settings. Full Observation (Needle) provides the raw needle turns and serves as an upper bound. Constructed Memory (Needle) replaces them with method specific constructed memory to isolate construction loss. End to End System evaluates the full pipeline with retrieval.

[60] p: Tab. 3 demonstrates two limitations. First, many methods degrade sharply after construction, e.g., MemoryBank drops by 41.3%, suggesting that compression tuned for redundant natural language fails to preserve dense state and causal information in agent memory. Second, similarity-based retrieval is unreliable: HippoRAG2 remains strong under constructed memory with needle turn but drops by 43.2% performance end-to-end.

[61] figure: Method Full Observation w/ Needle ACC Consturcted Memory w/ Needle ACC End to End System ACC HippoRAG2 0.46 0.37 (−19.6%) 0.21 (−43.2%) Mem1 0.29 (−37.0%) 0.20 (−31.0%) AMem 0.29 (−37.0%) 0.24 (−17.2%) MemoryBank 0.27 (−41.3%) 0.26 (−3.7%) Table 3: Ablation study on performance bottlenecks under the needle retrieval protocol in BabyAI, evaluated by accuracy (ACC) . Dark red values denote relative decrease vs. the previous column.

[62] figure: Figure 8 : Overview of the AMA- agent. (A) Illustrates the transition from trajectories to a structured causality graph. (B) depicts the retrieval mechanism, utilizing tool-augment search.

[63] h2: 5 The AMA- Agent

[64] p: Motivated by the observations in Sec. 4 , we develop the AMA- Agent with two core mechanisms: (A) a Causality Graph for memory construction to minimize information loss; and (B) a tool augmented retrieval module that complements standard retrieval with graph node traversal and keyword search to improve retrieval effectiveness.

[65] h3: 5.1 Memory Construction: Causality Graph

[66] p: AMA- Agent constructs a Causality Graph from the agent’s trajectory. The construction proceeds in three stages: For each timestep t t , the agent parses the adjacent turn pairs ( o t − 1 , a t , o t ) (o_{t-1},a_{t},o_{t}) to extract environment and object states, identifying latent inter-state causal dependencies and state-object associations (Fig. 8 (A) 1 ). These signals are instantiated as directed causality edges and undirected association edges connecting the respective state nodes (Fig. 8 (A) 2 ). Finally, these local interactions are integrated into a global Causality Graph, where nodes are mapped into a latent embedding space to facilitate similarity-based retrieval and relational reasoning (Fig. 8 (A) 3 ).

[67] h3: 5.2 Memory Retrieval: Tool-Augmented Search

[68] p: Beyond similarity-based retrieval, AMA- Agent adopts a tool-augmented search mechanism. It first retrieves the top K K nodes based on embedding similarity (Fig. 8 (B) 1 ) and performs self-evaluation to assess whether the retrieved evidence is sufficient to answer the query. If the evidence is insufficient, the agent categorizes the missing context and invokes either the graph node search tool or the keyword search tool .

[69] p: Under the graph node search tool route, the agent performs depth-controlled neighborhood traversal to aggregate multi-hop context and causal relations (Fig. 8 (B) 2 ). Under the keyword search tool route, the AMA- Agent uses a tool interface that allows it to write and execute scripts for programmatic analysis, enabling precise keyword matching and statistical aggregation (Fig. 8 (B) 3 ). Finally, the AMA- Agent synthesizes the retrieved evidence to produce a response (Fig. 8 (B) 4 ).

[70] h2: 6 Evaluation

[71] h3: 6.1 Experimental Setup

[72] figure: Table 4: Performance of different models on real-world subset. Method Recall Causal Inference State Updating State Abstraction Average Claude Haiku 3.5 ( Anthropic, 2025 ) 0.4943 (0.3510) 0.4507 (0.2792) 0.4287 (0.3015) 0.3090 (0.2648) 0.4361 (0.3067) GPT-5-mini ( OpenAI, 2025 ) 0.6951 (0.4010) 0.7157 (0.3027) 0.6575 (0.3288) 0.6235 (0.3262) 0.6784 (0.3464) GPT 5.2 ( Wailgum, 2025 ) 0.7741 (0.4758) 0.8047 (0.3512) 0.6563 (0.3686) 0.6037 (0.3582) 0.7226 (0.3988) Gemini 2.5 flash ( Gemini Team, 2025 ) 0.5834 (0.3682) 0.5087 (0.2628) 0.5000 (0.2395) 0.4196 (0.2361) 0.5168 (0.2878) Qwen2.5-14B-1M ( Yang et al., 2025b ) 0.5570 (0.4157) 0.4111 (0.3209) 0.4728 (0.3348) 0.3368 (0.3560) 0.4638 (0.3622) Qwen3-32B ( Yang et al., 2025a ) 0.6149 (0.4074) 0.5178 (0.3289) 0.4903 (0.3334) 0.3657 (0.3172) 0.5181 (0.3545) Qwen3-14B ( Yang et al., 2025a ) 0.5675 (0.3636) 0.4430 (0.2931) 0.4502 (0.3204) 0.3176 (0.2716) 0.4659 (0.3203) Qwen3-8B ( Yang et al., 2025a ) 0.5024 (0.3801) 0.3776 (0.2830) 0.3987 (0.3177) 0.2923 (0.2792) 0.4109 (0.3240) Note: Results are reported as Accuracy (F1). The best and second best Accuracy values are highlighted.

[73] figure: Table 5: Performance comparison of Agent Memory and RAG methods using base model Qwen-32B on real-world subset. Method Recall Causal Inference State Updating State Abstraction Average RAG BM25 0.3301 (0.1465) 0.4264 (0.1549) 0.3450 (0.1325) 0.2498 (0.1623) 0.3436 (0.1475) Qwen3-Emb-4B ( Zhang et al., 2025b ) 0.4843 (0.1590) 0.4974 (0.1549) 0.3520 (0.1353) 0.3011 (0.1610) 0.4227 (0.1522) GraphRAG ( Edge et al., 2025 ) 0.3077 (0.2769) 0.3905 (0.2634) 0.3140 (0.2551) 0.2879 (0.2588) 0.3258 (0.2650) HippoRAG2 ( Gutiérrez et al., 2025 ) 0.4579 (0.2356) 0.5080 (0.1966) 0.4403 (0.1892) 0.3538 (0.1785) 0.4480 (0.2048) Agent Memory Methods MemAgent ( Yu et al., 2025 ) 0.2550 (0.1489) 0.3380 (0.1606) 0.2849 (0.1432) 0.2202 (0.1655) 0.2768 (0.1530) Mem1 ( Zhou et al., 2025 ) 0.1180 (0.1857) 0.1427 (0.1732) 0.1205 (0.1659) 0.1080 (0.2042) 0.1229 (0.1807) Amem ( Xu et al., 2025 ) 0.3084 (0.2707) 0.3653 (0.2731) 0.3088 (0.2480) 0.2873 (0.2953) 0.3186 (0.2695) Mem0 ( Chhikara et al., 2025 ) 0.2011 (0.2413) 0.2645 (0.2443) 0.2101 (0.2225) 0.1516 (0.2241) 0.2104 (0.2343) MemoRAG ( Qian et al., 2025 ) 0.4708 (0.1789) 0.5497 (0.1811) 0.4257 (0.1713) 0.3659 (0.2073) 0.4606 (0.1822) MemGPT ( Packer et al., 2023 ) 0.3289 (0.1318) 0.4404 (0.1475) 0.2809 (0.1259) 0.2526 (0.1431) 0.3304 (0.1359) Mem-alpha ( Wang et al., 2025a ) 0.2876 (0.2325) 0.4172 (0.1993) 0.3064 (0.2000) 0.2171 (0.2135) 0.3117 (0.2130) MemoryBank ( Zhong et al., 2023 ) 0.3231 (0.3128) 0.4100 (0.2861) 0.3006 (0.2678) 0.3332 (0.3011) 0.3397 (0.2928) Simple mem ( Liu et al., 2026 ) 0.2012 (0.2039) 0.1884 (0.1612) 0.1764 (0.1594) 0.1373 (0.1689) 0.1811 (0.1764) AMA- Agent (AMA) 0.6238 (0.3280) 0.6145 (0.3103) 0.5305 (0.2625) 0.4719 (0.2825) 0.5722 (0.2992) Note: Results are reported as Accuracy (F1). The best and second best Accuracy values are highlighted.

[74] p: Benchmarks. We evaluate our baselines on two complementary subsets: 1. Real-world Subset: This subset comprising a total of 2,496 QA pairs. 2. Synthetic Subset: we utilize two tasks with a total of 1,200 QA pairs. These tasks are stratified across five trajectory lengths ( 8 ​ K , 16 ​ K , 32 ​ K , 64 ​ K 8\text{K},16\text{K},32\text{K},64\text{K} , and 128 ​ K 128\text{K} tokens), with 240 samples per interval.

[75] p: Baselines. We consider three categories of baselines: long context models, RAG, and memory agents.

[76] p: Implementation Details. To ensure a fair comparison, we evaluate all RAG baselines, memory-based agents, and our proposed AMA- Agent using the same backbone architectures: Qwen3-32B and Qwen3-8B . For each baseline, we adhere to the original authors’ default embedding models and indexing configurations (refer to Appendix B for reproduction details). For AMA- Agent, we employ Qwen3-4B-embedding to map the causality graph into the latent space and set K = 5 K=5 for similarity-based node retrieval.

[77] p: Metrics. We report both Accuracy and F1-score. Accuracy measures the instances judged as correct by an LLM-as-judge based on Qwen3-32B. Additional details and validation of the LLM-as-judge protocol are provided in Appendix C .

[78] h3: 6.2 Key Results

[79] p: Real-world Subset. We report the main results on the real-world subset in Tab. 4 (evaluating models with long contexts) and Tab. 5 (comparing different memory systems). While GPT 5.2 achieves the highest average accuracy (0.73) as Tab. 4 shows , its performance suggests that even strong commercial models have not fully mastered trajectory-based agent memory capabilities. Crucially, when controlled under the Qwen3 32B backbone (Tab. 5 ), AMA- Agent establishes a new state-of-the-art across all dimensions—Recall (0.6238), Causal Inference (0.6145), State Updating (0.5305), and State Abstraction (0.4719)—reaching an average of 0.5722. This significantly outperforms the strongest RAG baseline HippoRAG2 (0.4480) and the leading memory method MemoRAG (0.4606). These results demonstrate that explicit modeling of long-horizon state dynamics and causal memory organization provides a more robust framework for agent reasoning than standalone retrieval-based approaches.

[80] figure: Figure 9 : Performance Benchmarking. We evaluate 15 memory methods across Qwen 8B and 32B backbones.

[81] p: Synthetic Subset . We also evaluate all memory methods on the Synthetic subset and compare their scores against the real-world subset. Fig. 9 A illustrates the strong ranking correlation between real-world scenarios and our synthetic subset. The close alignment of most methods with the diagonal line demonstrates that the synthetic environment serves as a high-fidelity proxy for real-world performance, which is crucial given the high costs of real-world data acquisition and manual annotation.

[82] p: Fig. 9 evaluates the performance stability of our method compared to other baselines as the sequence length increases from 8K to 128K. While the Long Context approach maintains competitive accuracy at shorter scales, its performance degrades significantly beyond 32K, revealing the inherent limitations of fixed context window. In contrast, AMA-agent exhibits superior scalability, maintaining robust and consistently high accuracy even at 128K. .

[83] h3: 6.3 Ablation Study

[84] figure: Table 6 : Ablation results for AMA- Agent Method Recall Causal Inference State Updating State Abstraction Avg. AMA-agent 0.62 0.61 0.53 0.47 0.57 w/o Causality Graph 0.48 ( − 22.6 % -22.6\% ) 0.48 ( − 21.3 % -21.3\% ) 0.36 ( − 32.1 % -32.1\% ) 0.35 ( − 25.5 % -25.5\% ) 0.43 ( − 24.6 % -24.6\% ) w/o Tool-Augmented Retrieval 0.47 ( − 24.2 % -24.2\% ) 0.51 ( − 16.4 % -16.4\% ) 0.42 ( − 20.8 % -20.8\% ) 0.31 ( − 34.0 % -34.0\% ) 0.44 ( − 22.8 % -22.8\% ) Note: Values in dark red indicate the relative performance decrease compared to the full AMA agent.

[85] p: To validate the contributions of our key components, we perform ablation studies on the Causality Graph and tool augmented retrieval. The variant w/o Causality Graph replaces our structured Graph-based memory with a vanilla Qwen3 Embedding 4B indexs the context directly, while w/o Tool Augmented Retrieval disables tool calls and relies solely on embedding similarity retrieval. The results in Tab. 6 show that both modules are necessary for strong performance. Removing the Causality Graph causes a substantial degradation, with the average score dropping from 0.57 to 0.43, indicating that causality-aware representations are critical for agent memory. Likewise, removing tool augmented retrieval reduces performance to 0.44, suggesting that similarity search alone is insufficient and that tools provide complementary evidence access for robust reasoning.

[86] h2: 7 Conclusion

[87] p: In this paper, we introduced AMA- Bench to bridge the disparity between natural language-centric evaluations and the machine-generated, causally grounded nature of real-world agent trajectories. Our systematic analysis revealed that memory architecture is the primary determinant of performance, highlighting the limitation of lossy compression and similarity-based retrieval for dense, objective information. To address these challenges, we proposed AMA- Agent, which leverages a Causality Graph and Hybrid Tool-Augmented Retrieval to significantly outperform state-of-the-art baselines. A limitation of this study is its focus on in-episode memory; future work should extend these rigorous standards to cross-task scenarios involving lifelong learning.

[88] h2: Impact Statement

[89] p: This paper presents work whose goal is to advance the field of Machine Learning. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted. Regarding the introduced benchmark, we confirmed that it was constructed entirely from open-source data sources. All data entries underwent human verification to ensure that no personally identifiable information (PII) or private data were included.

[90] h2: References

[91] h2: Appendix

[92] h2: Appendix A Details of Dataset

[93] p: Here, we provide a detailed introduction to the datasets used for evaluating the four core competencies, including the dataset curation, corresponding metrics, average context length, and a brief description.

[94] h3: A.1 Real-world Subset

[95] p: This section details the composition of the real-world subset, which comprises multi-turn trajectories curated from six diverse domains of agent-environment interactions (Tab. 7 ).

[96] figure: Table 7: Implementation details of collected agent trajectories across task families. Field Benchmark Trace Source Total Selected Embodied AI ALFWorld-verified (seen) ALFRED ( Li et al., 2025 ) 140 33 Gaming BALROG / lmgame bench BALROG / GamingAgent 367 30 Web Task Execution WebArena ( Zhou et al., 2023 ) WebArena ( Zhou et al., 2023 ) 162 31 Software Engineering SWE-bench ( Jimenez et al., 2023 ) OpenHands ( Wang et al., 2024 ) 162 34 Open World Tool QA GAIA ( Mialon et al., 2023 ) CoSight ( Zhang et al., 2025a ) 100 30 Text 2 SQL Spider 2.0 ( Lei et al., 2024 ) Spider2 agent ( Lei et al., 2024 ) 120 51

[97] h5: Embodied AI.

[98] p: We collect trajectories from both the seen and unseen test splits of ALFWorld ( Shridhar et al., 2020b ) , a text-based embodied environment aligned with the ALFRED benchmark. These trajectories are generated using the expert-level demonstrations from ALFRED ( Shridhar et al., 2020a ) to ensure high-quality task completion in both familiar and novel environments.

[99] h5: Gaming.

[100] p: We curate gaming trajectories from two sources: BALROG ( Paglieri et al., 2024 ) , which includes Crafter (resource management), Baba is AI (long-horizon puzzle solving), and MiniHack (navigation); and LMGame-Bench ( Hu et al., 2025a ) , which includes 2048 and Candy Crush. Trajectories are collected using GPT-5.1 with the BALROG agent framework and GamingAgent ( lmgame-org, 2025 ) with memory and perception modules. For 2048, we use rule-based methods due to the extensive action sequences required. We select 30 trajectories totaling 360 QA pairs, with an average of 150 turns per episode.

[101] h5: Web Task Execution.

[102] p: We use WebArena ( Zhou et al., 2023 ) , a realistic web environment featuring fully functional websites across e-commerce, social forums, software development, and content management domains. Trajectories are collected using GPT-4.1 with the WebArena agent framework. We select 31 trajectories comprising 372 QA pairs, with an average of 25 turns and 34K tokens per trajectory, reaching up to 166K tokens for complex tasks.

[103] h5: Software Engineering.

[104] p: We collect trajectories from SWEBench Verified ( Jimenez et al., 2023 ; OpenAI, 2024 ) , which consists of real GitHub issues and pull requests from popular Python repositories. Trajectories are generated using Claude Sonnet 4 with the OpenHands framework ( Wang et al., 2024 ) , an open platform for AI software developers. We select 36 trajectories totaling 432 QA pairs, with an average of 103 turns and 19K tokens per trajectory.

[105] h5: Open World Tool QA.

[106] p: We use the GAIA benchmark ( Mialon et al., 2023 ) , which tests general AI assistants on real-world questions requiring reasoning, multi-modality handling, web browsing, and tool-use proficiency. Trajectories are collected using GPT-5 with the Co-Sight framework ( Zhang et al., 2025a ) , which achieves state-of-the-art performance on open-sourced agent benchmarks. We select 30 trajectories across all three difficulty levels from the validation set, comprising 360 QA pairs with an average of 41 turns and 289K tokens – the longest among all domains, reaching up to 997K tokens.

[107] h5: Text-to-SQL.

[108] p: We collect trajectories from the Spider 2.0 benchmark ( Lei et al., 2024 ) , specifically sampling from the Spider2-Snow subset which focuses on enterprise-level text-to-SQL tasks with Snowflake databases. Spider 2.0 comprises three subsets (Snow, DBT, and Lite), with the Snow subset containing 547 examples. Among these, gold answers are provided for 120 examples to enable verification of generated SQL queries. We sample 51 trajectories from these verified examples to ensure answer correctness can be validated. Trajectories are generated using Claude Sonnet 4.5 with the Spider2-Agent framework, totaling 612 QA pairs with an average of 22 turns and 6K tokens per trajectory.

[109] p: A comprehensive breakdown of the Real-world Subset is provided in Table 8 . To provide a clearer illustration of our defined problem types, we present a representative example from the Web Task Execution domain (Figure E.1 ). This example shows how an agent must use different memory operations, such as tracking incremental UI changes, recognizing high level strategic failures, and handling long horizon interactions. Aligned with the three memory capabilities (Table 2 ), we define four QA categories that probe whether an agent has acquired the corresponding competencies required to answer them reliably, and we instantiate all four categories in this example. For additional qualitative visualizations of data samples, please refer to Appendix E .

[110] figure: Table 8: Statistics of QA pairs, evaluation type distribution, and interaction complexity. Field #Samples #QA Evaluation Type Avg. Turns Avg. Tokens Max Tokens Type A Type B Type C Type D Text 2 SQL 51 612 223 153 134 102 21.80 6,049 10,718 Open World Tool QA 30 360 98 95 107 60 41.40 288,651 996,826 Web Task Execution 31 372 125 93 93 61 24.77 34,265 166,260 Gaming 30 360 120 90 90 60 149.87 14,909 33,360 Embodied AI 30 360 61 90 150 59 130.33 26,306 60,717 Software Engineering 36 432 212 75 73 72 103.22 19,296 28,615 TOTAL 208 2,496 839 596 647 414 73.29 57,506 996,826

[111] h3: A.2 Synthetic Subset

[112] h5: BabyAI

[113] p: are generated from the BabyAI environment ( Chevalier-Boisvert et al., 2019 ) , which supports six difficulty levels: easy , medium , medium_hard , hard , very_hard , and hard_large . Each trajectory is paired with 12 questions by default, and we collect a total of 50 trajectories, with an average length of 563 turns and 30,042 tokens per trajectory.

[114] h5: TextWorld

[115] p: are generated from the TextWorld ( Côté et al., 2018 ) environment. We consider three game types: coin_collector , cooking , and treasure_hunter . The environment supports eight difficulty levels: easy , medium , medium_hard , hard , very_hard , extreme , ultra , and mega . On average, each trajectory contains 57 turns and 31,662 tokens.

[116] p: To provide a concrete realization of the Synthetic subset described in Section 3.3 , we present qualitative case studies from BabyAI and TextWorld. These examples are designed to illustrate how our programmatic framework evaluates specific agent capabilities by modulating synthesis parameters. For additional qualitative visualizations of data samples, please refer to Appendix E .

[117] p: Probing Memory Robustness under Action Stochasticity ( ϵ \epsilon ): Figure E.2 presents a diagnostic episode from the BabyAI environment under high action stochasticity ( ϵ \epsilon ). This setup evaluates the agent’s ability to maintain the task goal within its interaction context when π ∗ \pi^{*} is perturbed by suboptimal exploratory noise. The observed failure—a task truncation—indicates that the agent’s memory mechanism fails to distinguish gold-standard goal alignment from the increased ”interaction noise,” even when target objects are clearly rendered via the perception interface O ϕ ​ ( s t ) O_{\phi}(s_{t}) .

[118] p: Evaluating State Tracking across Subgoal Chains ( ϕ \phi ): Figure E.2 captures a failure in TextWorld that probes the agent’s internal state-tracking of the backend transition kernel P ϕ P_{\phi} . By scaling the difficulty vector ϕ \phi to increase subgoal chain length, we test whether the agent can correctly update its ”memory slots” based on transition events Δ ​ s \Delta s . The repetitive invalid actions (e.g., attempting a put before a verified take event) reveal a breakdown in causal reasoning, where the agent loses track of the latent state s t s_{t} despite having navigated the correct spatial transitions.

[119] figure: Table 9: Maximum context lengths used for long context baselines. Model Max context tokens Notes Claude 3.5 Haiku 200,000 API context window OpenAI GPT 5 mini 400,000 API context window OpenAI GPT 5.2 400,000 API context window Gemini 2.5 Flash 1,048,576 Max input tokens Qwen2.5 14B Instruct 1M 1,010,000 Long context checkpoint Qwen3 32B 32,768 Native Qwen3 14B 32,768 Native

[120] h2: Appendix B Baseline Implementation Details

[121] p: Long-Context Model Baseline. For long-context baselines, we directly pack the trajectory into the model input without retrieval or compression until reaching the maximum context length permitted by each API or checkpoint in Tab. 9 . We reserve a fixed 4K-token budget for the model to generate the final answer, and use the remaining tokens as the effective input budget. When a trajectory exceeds this budget, we apply a simple truncation strategy that preserves both early and late interactions: we keep the first 50% and the last 50% budget length of the trajectory (by token count) and discard the middle portion to fit the context window.

[122] h3: B.1 RAG Baseline

[123] h5: GraphRAG.

[124] p: constructs memory by using an LLM (Qwen3-8B/32B) to extract entities (object, location, action) and their relationships from trajectory text, storing them as a knowledge graph in parquet format. The trajectory is first chunked into semantic units of 15 turns per chunk with a maximum of 24,000 tokens. This construction process is inherently lossy, as it discards substantial raw trajectory details, particularly the detailed observation states and fine-grained action sequences present in the original data. During retrieval, GraphRAG selects the top- k k most relevant entities and relationships from the knowledge graph based on their descriptions, concatenating these structured elements into the prompt as context rather than including the full trajectory. We follow the default GraphRAG configuration with k = 50 k=50 entities and relationships, max_gleanings=0 , and a description summarization disabled to preserve extraction fidelity.

[125] h5: HippoRAG.

[126] p: constructs memory by applying OpenIE-style extraction to trajectory text, yielding entities and relation triples that form a heterogeneous graph of passage (trajectory chunk), entity, and fact nodes; synonymy edges are added via nearest-neighbor search over entity embeddings. This construction is lossy because raw trajectories are distilled into triples and edges, potentially omitting fine-grained state transitions or action details. At retrieval time, HippoRAG computes query–fact similarity with dense embeddings, reranks top facts, maps them to linked entities, and runs personalized PageRank over the graph; the graph scores are combined with dense passage retrieval to select top- k k passages for QA. We use the default HippoRAG configuration with top- k k fact/entity linking = 5 =5 , passage retrieval top- k = 200 k=200 , and QA context limited to the top 5 passages. All passage, entity, and fact embeddings use the same model BAAI/bge-m3.

[127] h3: B.2 Memory Agents Baseline

[128] h5: MemoryBank.

[129] p: constructs a hierarchical memory by first chunking the trajectory into segments of 5,000 tokens with 500-token overlap, then using the LLM to summarize each chunk into a compact memory piece that preserves key subgoals, actions, observations, and failures. Each memory piece is embedded using a local sentence-transformer model (all-MiniLM-L6-v2), and a global summary is generated from all memory pieces to capture the overall strategy and critical facts. This summarization process is lossy, as fine-grained trajectory details are compressed into concise text. During retrieval, MemoryBank computes cosine similarity between the question embedding and memory piece embeddings, combined with an Ebbinghaus-inspired retention score that accounts for memory strength and recency of recall. The top- k k memory pieces are retrieved and concatenated with the global summary as context for answering. We use the default configuration with k = 6 k=6 , forget decay τ = 5.0 \tau=5.0 , and strength increment of 1 upon each recall.

[130] h5: MemAgent.

[131] p: processes the trajectory as a stream of fixed-length sections, iteratively updating a recurrent memory state. For each chunk of 5,000 tokens, the LLM reads the current trajectory section along with the previous memory, then generates an updated memory that summarizes the agent’s progress while retaining relevant details from earlier sections. This recurrent summarization is inherently lossy, as information from earlier chunks may be progressively compressed or forgotten as new sections are processed. During retrieval, MemAgent directly reads from its final accumulated memory without additional retrieval mechanisms, the memory itself serves as the complete context for answering questions. We follow the default configuration with a 4,096-token context window partitioned into: the current trajectory chunk (5,000 tokens, truncated if needed), the accumulated memory (dynamically sized), and generation budget (1,024 tokens), with memory truncated from the beginning when context limits are exceeded to preserve more recent information.

[132] h5: Mem-alpha.

[133] p: employs a three-tier hierarchical memory architecture with an agentic approach to memory management. The system maintains: (1) Core Memory for high-level task understanding and rules, (2) Semantic Memory for storing factual knowledge as embedded vectors, and (3) Episodic Memory for recording specific events with temporal context. Trajectories are chunked using sentence-aware tokenization into segments of 4,096 tokens, preserving sentence boundaries. For each chunk, an agent equipped with memory tools (insert, update, delete, retrieve) autonomously decides which information to store and in which memory tier. Both semantic and episodic memories are embedded using text-embedding-3-small (1,536 dimensions) and retrieved via Top-K similarity search. During question answering, MemAlpha retrieves relevant memories using BM25 sparse retrieval, fetching the top-20 most relevant items per memory type. We follow the default configuration with a thinking budget of 1,024 tokens, maximum generation of 2,048 tokens, and memory consolidation occurring every 5 items.

[134] h5: Mem1.

[135] p: processes the trajectory through recurrent memory consolidation, iteratively updating a compact memory state with each new chunk of observations. For each chunk of 5,000 tokens, the LLM reads the current trajectory section along with the previous accumulated memory, then generates an updated memory that integrates new information while maintaining context and discarding redundant details. After processing all chunks, a final comprehensive summary is generated that consolidates key actions, important observations, overall progress, and patterns encountered. MEM1 directly uses this global consolidated memory as the complete context for answering all questions. We follow the default configuration with a 120,000-token maximum context window, trajectory chunks of 5,000 tokens, memory update budget of 1,024 tokens per chunk.

[136] h5: Mem0.

[137] p: constructs its memory layer through an LLM-driven fact extraction process, distilling raw trajectory data into a series of ”atomic facts.” These facts are subsequently embedded and stored in a vector database. To ensure memory consistency, Mem0 incorporates a conflict resolution mechanism that updates or replaces outdated information (e.g., evolving user locations). However, this extraction-based approach is inherently lossy for structured trajectory data, as it often omits critical low-level details. Empirical observations during our experiments indicate that bypassing the extraction layer and utilizing raw data directly can significantly enhance performance on trajectory-based benchmarks. During retrieval, Mem0 employs vector-based cosine similarity to identify the top- k k most relevant facts, which are then injected into the LLM prompt as context

[138] h5: A-Mem.

[139] p: implements a recurrent memory processing strategy to handle long-term trajectories. The input is segmented into chunks, and new memory states are built recursively by integrating the current chunk with preceding memory. Each memory entry consists of a concatenated representation of content, context, keywords, and tags, which is then embedded and stored in a vector database. This recursive construction, while thorough, introduces significant computational latency for long-context sequences. Furthermore, A-Mem supports memory evolution: it retrieves top- k k neighboring entries via vector search, and an LLM determines whether to establish new relational connections or update existing metadata. We set the RECURRENT_CHUNK_SIZE to 8,000 8,000 tokens.

[140] h5: MemGPT.

[141] p: implements a hierarchical memory architecture that separates memory into core memory (in-context) and archival memory (external storage with retrieval). The trajectory is inserted directly into archival memory as a complete text block, which is then indexed for retrieval. MemGPT uses an agentic approach where the LLM autonomously manages memory through function calls. It can search, insert, and retrieve from archival memory as needed during question answering. The archival memory is embedded using a local embedding model (BAAI/bge-small-en-v1.5) for vector-based retrieval. Unlike other memory agents that pre-process trajectories into summaries, MemGPT stores the raw trajectory text and relies on the agent’s retrieval capabilities to fetch relevant portions at query time. During question answering, the agent receives the question and uses its memory tools to search archival storage, with retrieved content brought into the limited core memory context window. We use the default MemGPT configuration with auto-save disabled, maximum chaining steps set to 5 to prevent infinite tool-calling loops, and observations truncated to 8,000 characters when exceeding length limits.

[142] h5: MemoRAG.

[143] p: constructs memory by first building a global memory representation of the entire trajectory using a dedicated memory model, then enabling retrieval-augmented generation for question answering. The trajectory is converted to text format and processed by a memory encoder (Qwen2-7B-Instruct with beacon compression at ratio 4) that compresses the long context into a compact memory representation. This memory is then used to guide retrieval from the original text chunks. During retrieval, MemoRAG uses a dual-model architecture: the memory model generates retrieval cues based on the query and global memory, while a separate retriever (BAAI/bge-m3) fetches the top- k k most relevant chunks from the original trajectory. The retrieved chunks are then passed to a generation model to produce the final answer. This approach is lossy during memory encoding, as the beacon compression mechanism reduces the original context to a fraction of its size. We use the default configuration with retrieval chunk size of 512 tokens, top- k = 3 k=3 retrieved hits, beacon ratio of 4, and maximum generation length of 256 tokens, retrieval via bge-m3.

[144] h5: SimpleMem.

[145] p: constructs memory through an LLM-driven extraction process that converts raw trajectory data into atomic memory entries. The trajectory is processed in sliding windows, where each window is passed to an LLM that extracts structured fields including lossless restatements with forced coreference resolution (eliminating pronouns and converting relative time to absolute timestamps), keywords, locations, persons, entities, and topics. These atomic entries are embedded and stored in a vector database. This extraction process is lossy, as trajectory details are abstracted into discrete semantic units. During retrieval, SimpleMem employs a hybrid strategy combining semantic vector similarity, lexical keyword matching, and symbolic metadata filtering. The system supports multi-query planning that decomposes complex questions into targeted sub-queries, and reflection-based refinement that iteratively checks information completeness and generates additional queries to fill gaps. We use the default configuration with parallel memory building (2 workers), parallel retrieval (3 workers), reflection enabled with maximum 2 rounds, and planning enabled for query decomposition.

[146] h2: Appendix C LLM-as-Judge Calibration Protocol

[147] p: We include the following materials to ensure reproducibility and transparency of our LLM-as-judge evaluation.

[148] h3: C.1 Judge Prompt and Output Format

[149] p: We use Qwen3 32B as the primary evaluator. The judge receives the input triplet (question, reference answer, predicted answer) and returns a binary decision. The judge is required to output only one token in { yes , no }.

[150] h3: C.2 Human-Judge Agreement

[151] p: To validate the reliability of our LLM-as-judge evaluation, we conducted human annotation on a sample of 300 instances (50 per subset) from the GPT-5.2 results. We obtain gold labels via independent human annotation. Each instance is labeled by at least two annotators with access to the question, reference answer, and predicted answer. Labels are binary: yes if the predicted answer is correct, otherwise no . Disagreements are resolved by majority vote, with a third annotator used for adjudication when needed.

[152] p: Table 10 presents the confusion matrix and performance metrics aggregated across all subsets. The judge achieves 92.67% accuracy, indicating reliable alignment with human judgment.

[153] figure: Table 10: Confusion matrix (left) and performance metrics (right) for LLM-as-judge vs. human annotations. Human Label Judge Label Correct Incorrect Total Correct 190 (TP) 7 (FP) 197 Incorrect 15 (FN) 88 (TN) 103 Total 205 95 300 Metric Value Accuracy 92.67% Precision 96.45% Recall 92.68% F1 Score 94.53%

[154] h2: Appendix D Prompt Templates for AMA- Agents

[155] p: This appendix provides the prompt templates used by AMA- agent in both phases. The first phase constructs the Causality Graph by extracting objective inventories, detecting environment and objective state changes, and emitting structured, machine parsable records in Markdown. The second phase performs retrieval time routing, including chunk sufficiency judgement and trajectory based code generation.

[156] h3: D.1 Memory Construction Prompt

[157] h3: D.2 Chunk Sufficiency Judgement Prompt

[158] h3: D.3 Trajectory Based Code Generation Prompt

[159] h2: Appendix E Dataset Examples

[160] p: We provide representative examples from subset below.

[161] h3: E.1 Real-world subset example

[162] h3: E.2 Synthetic subset example

[163] h2: Appendix F Needle-in-a-Haystack QA Generation Pipeline

[164] p: To evaluate the long-context retrieval capabilities of memory-augmented agents, we developed a structured pipeline to generate QA pairs where the answer is anchored to specific ”needle” turns within a trajectory ”haystack.” The generation logic is formalized in Algorithm 1 .

[165] figure: Algorithm 1 QA Needle Generation for Trajectory Evaluation 0: Source trajectory data 𝒯 \mathcal{T} , Bin sizes ℬ ∈ { 8 ​ K , 16 ​ K , … , 128 ​ K } \mathcal{B}\in\{8K,16K,\dots,128K\} , QA Types 𝒬 ∈ { A , B , C , D } \mathcal{Q}\in\{A,B,C,D\} 0: Final balanced dataset 𝒟 f ​ i ​ n ​ a ​ l \mathcal{D}_{final} 1: 𝒞 ← ∅ \mathcal{C}\leftarrow\emptyset {Initialize candidate pool} 2: H ← split_by_turns ​ ( 𝒯 ) H\leftarrow\text{split\_by\_turns}(\mathcal{T}) {Chunk haystack with unique turn identifiers} 3: for all b ​ i ​ n ​ _ ​ s ​ i ​ z ​ e ∈ ℬ bin\_size\in\mathcal{B} do 4: for all q ​ a ​ _ ​ t ​ y ​ p ​ e ∈ 𝒬 qa\_type\in\mathcal{Q} do 5: τ n ​ e ​ e ​ d ​ l ​ e ← sample ​ ( H , strategy=“diversity_first” ) \tau_{needle}\leftarrow\text{sample}(H,\text{strategy=``diversity\_first''}) {Ensure depth diversity} 6: q ​ a n ​ e ​ e ​ d ​ l ​ e ← generate_qa ​ ( H , q ​ a ​ _ ​ t ​ y ​ p ​ e , τ n ​ e ​ e ​ d ​ l ​ e , b ​ i ​ n ​ _ ​ s ​ i ​ z ​ e ) qa_{needle}\leftarrow\text{generate\_qa}(H,qa\_type,\tau_{needle},bin\_size) 7: q a n ​ e ​ e ​ d ​ l ​ e . source_ids ← { t . i d ∣ t ∈ τ n ​ e ​ e ​ d ​ l ​ e } qa_{needle}.\text{source\_ids}\leftarrow\{t.id\mid t\in\tau_{needle}\} {Map for traceability} 8: if verify_qa_quality ( q ​ a n ​ e ​ e ​ d ​ l ​ e qa_{needle} ) then 9: 𝒞 ← 𝒞 ∪ { q ​ a n ​ e ​ e ​ d ​ l ​ e } \mathcal{C}\leftarrow\mathcal{C}\cup\{qa_{needle}\} 10: end if 11: end for 12: end for 13: 𝒟 f ​ i ​ n ​ a ​ l ← select_balanced ( 𝒞 , quota = { A : 4 , B : 3 , C : 3 , D : 2 } ) \mathcal{D}_{final}\leftarrow\text{select\_balanced}(\mathcal{C},\text{quota}=\{A:4,B:3,C:3,D:2\})

[166] h5: Key Strategies in Pipeline:

[167] p: Diversity-First Sampling: Instead of random sampling, we pick ”needle” turns from various depths of the trajectory (early, middle, and late stages) to prevent the LLM from exploiting positional biases.

[168] p: Ground Truth Traceability: By binding each QA pair to specific turn_ids , we can verify whether the agent’s retrieval mechanism successfully identified the correct ”needle” from the ”haystack” during inference.

[169] p: Balanced Distribution: The final selection ensures that different reasoning types (e.g., spatial reasoning vs. object state tracking) are represented proportionally to avoid data skew.

[170] h2: Appendix G Example of needle turn for ablation study

[171] p: To further illustrate the distinction between the three evaluation branches discussed in Section 5.3, we provide a concrete example from a Type A3 task (Object Visibility Change).

[172] p: Raw Observation Branch:

[173] p: [Turn 0] Action: forward; Obs: "In your view: a yellow box, a purple box, a green ball..." [Turn 1] Action: forward; Obs: "In your view: a yellow box, a green ball..."

[174] p: Note: The LLM must compare the two raw observation strings to infer the disappearance of the purple box.

[175] p: Oracle Memory Branch (and System Branch upon success):

[176] p: Note: The state change is explicitly summarized. In the Oracle branch, this shard is force-fed to the LLM; in the System branch, the agent must retrieve this specific shard from the database.

[177] h2: Appendix H Case-study

[178] p: To further illustrate the distinction between our raw data storage approach and the default Mem0 extraction process discussed in Section 3, we provide a comparative analysis using a Q ​ w ​ e ​ n ​ 3 − 32 ​ B Qwen3-32B model. This example demonstrates why LLM-driven ”fact distillation” is inherently lossy for structured agent experiences.

[179] p: Narrative Extraction Logic: Mem0’s extraction prompt is optimized for high-level entities and static properties. In Case 1, the LLM successfully maps the input into an atomic ”subject-predicate-object” structure, which is ideal for standard user profiling.

[180] p: The Bottleneck in Trajectory Data:

[181] p: Note: As evidenced by Case 2, the extraction-based approach is inherently lossy for agent-based tasks. By bypassing the infer=True extraction layer and utilizing raw trajectory segments directly in our System Branch , we preserve the environmental context that is otherwise discarded by the LLM-driven fact extractor.

[182] h2: Instructions for reporting errors

[183] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[184] p: Tip: You can select the relevant text first, to include it in your report.

[185] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[186] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
