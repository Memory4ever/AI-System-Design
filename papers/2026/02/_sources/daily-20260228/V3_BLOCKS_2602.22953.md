[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: General Agent Evaluation

[3] h6: Abstract

[4] p: The promise of general-purpose agents—systems that perform tasks in unfamiliar environments without domain-specific engineering—remains largely unrealized. Existing agents are predominantly specialized, and while emerging implementations like OpenAI SDK Solo Agent and Claude Code hint at broader capabilities, no systematic evaluation of their general performance has been pursued. Current agentic benchmarks assume domain-specific integration, encoding task information in ways that preclude fair evaluation of general agents. This paper frames general-agent evaluation as a first-class research objective. We propose conceptual principles for such evaluation, a Unified Protocol enabling agent-benchmark integration, and Exgentic—a practical framework for general agent evaluation. We benchmark five prominent agent implementations across six environments as the first Open General Agent Leaderboard. Our experiments show that general agents generalize across diverse environments, achieving performance comparable to domain-specific agents without any environment-specific tuning. We release our evaluation protocol, framework, and leaderboard to establish a foundation for systematic research on general-purpose agents: www.exgentic.ai .

[5] h6: Keywords:

[6] p: IBM Research

[7] h2: 1 Introduction

[8] figure: # General Agent Model Avg Success Avg Cost App World Browse Comp+ SWE BenchV Tau 2 Airline Tau 2 Retail Tau 2 Telecom 1 OpenAI Solo Claude Opus 4.5 .73 $8.5 .68 .61 .81 .74 .85 .84 2 Claude Code Claude Opus 4.5 .67 $8.0 .66 .53 .74 .66 .83 .76 3 Smolagent Claude Opus 4.5 .66 $4.4 .70 .61 .65 .72 .78 .58 4 ReAct Short Gemini 3 .62 $0.7 .55 .48 .71 .70 .82 .73 5 ReAct Short Claude Opus 4.5 .62 $3.8 .64 .49 .61 .66 .78 .76 6 ReAct Gemini 3 .61 $0.8 .51 .48 .71 .70 .82 .73 7 ReAct Claude Opus 4.5 .61 $5.8 .61 .49 .61 .66 .78 .76 8 OpenAI Solo Gemini 3 .60 $2.8 .58 .33 .72 .62 .73 .89 9 Claude Code Gemini 3 .57 $2.5 .36 .51 .67 .70 .78 .69 10 Smolagent Gemini 3 .56 $1.8 .13 .57 .76 .68 .76 .88 11 ReAct Short GPT 5.2 .46 $0.3 .22 .46 .57 .54 .73 .54 12 ReAct GPT 5.2 .41 $0.2 .00 .46 .57 .54 .73 .54 13 OpenAI Solo GPT 5.2 .39 $0.2 .00 .48 .55 .50 .54 .53 14 Claude Code GPT 5.2 .38 $0.4 .00 .43 .58 .48 .51 .55 15 Smolagent GPT 5.2 .38 $0.4 .07 .26 .53 .60 .68 .71 Table 1 : The Open General Agent Leaderboard comparing emerging general agents across standardized benchmarks. Average Success represents the mean success rate across benchmarks; Average Cost represents the mean cost per task. Performance is strongly influenced by backbone model choice.

[9] p: The field of AI agents has witnessed remarkable progress, with agentic systems demonstrating impressive capabilities across diverse domains—from solving software engineering tasks to navigating web interfaces ( Zhang et al., 2024 ; Deng et al., 2023 ) . However, current progress largely relies on domain specialization and manual tuning; whereas, heterogeneous real-world settings demand general-purpose agents capable of scalable deployment without such manual customization ( Marreed et al., 2025 ; Bandel et al., 2026 , c.f.,) .

[10] p: Despite their importance, current evaluation practices cannot adequately assess general-purpose agent capabilities. Existing agentic benchmarks like SWE-Bench Verified ( Jimenez et al., 2023 ) and τ 2 \tau^{2} -Bench ( Yao et al., 2024 ) provide valuable assessments of domain-specific agents. Yet, they impose two constraints preventing general-agent evaluation: they use bespoke communication protocols ( Anonymous, 2026 ) , and they implicitly assume agents have prior knowledge of benchmark-specific goals and environment semantics. Recent consolidation efforts like BrowserGym ( Chezelles et al., 2025 ) and Harbor ( Shaw, 2025 ) have integrated multiple benchmarks within single domains, by exposing to the agent the current goals and environment semantics (Fig. 2 (B)). While a step forward, these frameworks still enforce a single protocol (web-based for BrowserGym, CLI-based for Harbor), preventing agents from using their native integration mechanisms and effectively evaluating a diminished version of the agent ( Yehudai et al., 2025 ) .

[11] p: We set general-purpose AI agents as a research target, propose a concrete method for evaluating them, and present the first systematic analysis of general agents across diverse environments (Fig. 3 ). Specifically, our contributions are threefold. (1) We present the Unified Protocol , a benchmark-agent mediation protocol (Fig. 2 (C)). The Unified Protocol bridges the communication between agent interfaces (e.g., CLI, tool-calling APIs, MCP) and benchmarks through a canonical task representation, decoupling evaluation from domain-specific implementations and communication protocols. (2) Based on the Unified Protocol, we release Exgentic an evaluation harness for general agents that supports modular insights—comparing architectures, analyzing language model impact, and optimizing agent-model pairings. (3) Running Exgentic we present the first public Open General Agent Leaderboard to guide general agent development, totaling in overall cost of $22K (See Table 1 ).

[12] p: Our analysis of the Open General Agent Leaderboard highlights both the capabilities and limitations of contemporary general-purpose agents. While these agents demonstrate notable cross-domain generalization—often performing on par with domain-optimized baselines—their success is primarily dictated by the underlying language model (Fig. 1 ). Conversely, different agentic scaffolds exhibit comparable performance, despite substantial variance in cost. Together, these findings point to the potential of general agents.

[13] p: Ultimately, advancing general-purpose agents requires a collective effort. We hope the Open General Agent Leaderboard serves as a catalyst for approaches that transcend individual tasks and invite the research community to expand this ecosystem by contributing benchmarks that challenge generalization and novel evaluation protocols.

[14] figure: Figure 1 : Cost-performance tradeoffs across agent-model configurations. The Pareto frontier (red dashed line) shows optimal tradeoffs: GPT 5.2 configurations offer the best cost-efficiency while Claude Opus 4.5 achieve the highest performance at 3-33 × \times higher cost.

[15] figure: Figure 2 : Evolution of Agentic Evaluation. (A) Collection of separate benchmarks, each requiring a custom agent or an agent with specific adaptation per benchmark (HAL) (B) Multiple benchmarks consolidated through a single protocol, such as CLI, or Web (C) Multiple benchmarks consolidated through a common protocol that can be adapted to any agent’s protocol (Exgentic).

[16] h2: 2 Unified Protocol Methodology

[17] p: This work provides an evaluation solution for any general agent on any agentic benchmark, overcoming the common case of incompatibility between agent and benchmark protocols that either prevent evaluation (Fig. 2 (B)), or require costly pairwise adaptation for each agent and benchmark (Fig. 2 (A)). To address these limitations, we introduce a Unified Protocol that serves as a mediation layer between agents and benchmarks.

[18] p: The Unified Protocol serves as a “narrow waist”, adding a new agent (or benchmark) only needs adhering to it rather than to all benchmarks (agents). Thus, it significantly reduces integration complexity, development effort and learning curve.

[19] p: The Unified Protocol is not an imposed standard, but rather one derived from existing agent and benchmark communication patterns. As such, it naturally accommodates and unifies prevalent interaction protocols—enabling faithful translation between any agent-benchmark pair that employs these paradigms.

[20] h3: 2.1 Agent Benchmark Unified Protocol

[21] p: The protocol defines instances that are passed between the benchmark and the agent. Each instance has three fields: task, context, and actions. Here we demonstrate them with τ 2 \tau^{2} -Bench as our running example (see other benchmark examples in Appendix B ).

[22] p: Task : What the agent should do? A textual description of the task. In τ 2 \tau^{2} -Bench, it is ”You are a customer service agent that helps the user according to the policy provided below. Try to be helpful and always follow the policy.” . In addition, the first user utterance, such as ”Cancel my flight reservation AH3BDS” , is passed to the agent separately as the first observation from the environment.

[23] p: Context : What the agent should know? Additional information provided to the agent to accomplish the task. In τ 2 \tau^{2} -Bench, the context contains the policy . We note that the agent can use the context in different ways. For example, the agent can naively append it to the task or store it in a dedicated agent memory or document store for conditional retrieval.

[24] p: Actions : What can the agent do? A set of environment actions. These actions constitute the complete set of operations the environment makes available for performing the task. Each action specifies a typed set of parameters and may return one or more observations of arbitrary types. In τ 2 \tau^{2} -Bench for the airline domain, some actions are cancel ​ _ ​ reservation ⁡ ( r ​ e ​ s ​ e ​ r ​ v ​ a ​ t ​ i ​ o ​ n ​ _ ​ i ​ d ) \operatorname{cancel\_reservation}(reservation\_id) and search ​ _ ​ direct ​ _ ​ flight ⁡ ( o ​ r ​ i ​ g ​ i ​ n , d ​ e ​ s ​ t ​ i ​ n ​ a ​ t ​ i ​ o ​ n , d ​ a ​ t ​ e ) . \operatorname{search\_direct\_flight}(origin,destination,date).

[25] p: Reviewing existing protocols and agents, we observed that many introduce special handling for two specific types of interactions with the environment: (1) sending a message to a user, and (2) submitting a final answer to the benchmark, signaling that the agent has completed the task. To support these common interaction patterns, the Unified Protocol allows implementers to optionally designate one action as the message action and one as the final‑answer action.

[26] h3: 2.2 Methodology for Adapting Existing Benchmarks

[27] p: Existing agent benchmarks are typically coupled with specific interaction protocols, and often implicitly assume that agents possess prior knowledge of the benchmark’s semantics, or that a human will manually perform the integration.

[28] p: A representative example is SWE-Bench Verified 1 1 1 SWE-Bench Verified . Each task specifies a GitHub repo, a base commit, and a free‑text bug description, with the expected output being a patch. The benchmark does not define how agents should access the repo or submit fixes—those details are left to the integrator. For general‑purpose agents without human intervention, this interface must be explicit. However, we cannot arbitrarily decide on a setup; instead, we derive the interface from a reference agent implementation.

[29] p: For SWE-Bench Verified , we examined mini-SWE agent 2 2 2 mini-SWE agent as the reference implementation. There, the agent is placed in a bash environment where the repository has already been cloned. When the agent outputs COMPLETE_TASK_AND_SUBMIT_FINAL_OUTPUT , the system automatically generates a patch and submits it for evaluation. This design fully specifies how the agent interacts with the benchmark, what actions it may take, and how it submits solutions—implictly indicating that repository cloning and patch creation are not evaluation targets.

[30] p: Accordingly, in the Exgentic protocol for SWE-Bench Verified , we introduce two explicit actions: one for executing bash commands and another for submitting a patch constructed from the agent’s code modifications.

[31] p: To define the protocol’s task and context fields, we review both the benchmark tasks and the reference implementation prompts. Many benchmark tasks include irrelevant implementation details, while key instructions appear only in the reference agent’s internal prompts. For instance, in τ 2 \tau^{2} -Bench, the reference prompt states: “You are a customer service agent that helps the user according to the <policy> below.” Such essential information belongs in the benchmark task itself and is included in the Exgentic task definition. In contrast, instructions like “Each turn you may either message the user or make a tool call, but not both” are excluded because they assume a particular tool‑calling protocol.

[32] p: In summary, we decouple each benchmark from its original protocol by making all agent‑visible assumptions explicit. First, we inspect the reference agent to see how it interacts with the environment and what actions and observations it uses. Then we build task descriptions that include only the information needed for the agent to solve the task, omitting implementation‑specific details and redundant signals. This yields tasks that preserve the benchmark’s intended semantics while remaining independent of any particular agent architecture or communication protocol, making them suitable for evaluating any general agent implementation.

[33] figure: Figure 3 : Open General Agent Leaderboard is the first benchmark to consistently test general-agent architectures across key skills in diverse environments.

[34] h3: 2.3 Methodology for Adapting Existing Agents

[35] p: Existing agents interface with existing environments through specific protocols such as MCP, python functions, or tool calls. They also receive the task description through some command line or programmatic API.

[36] p: Adapting agents to the Unified Protocol involves deciding how to map the task, context and actions of the protocol to the agents’ specific API. It is important to note that the agent adaptor is benchmark agnostic.

[37] p: The textual task descriptions are typically concatenated with the context fields to textual instructions passed to the model. While not implemented today, the context may be used in different ways. For example, an MCP-based agent may opt to store the context in MCP resources rather than add them to the instructions.

[38] p: Action adaptation is straightforward and largely reusable across agents using similar APIs, with each action mapped to a single Python function, OpenAI tool, or MCP tool.

[39] p: More subtle adaptation is dealing with special actions. One special action type is interacting with a user. Some agents, like tool-calling agents, natively interact with users using dedicated assistant - and user - messages rather than through tool API. To preserve the principle of presenting the benchmark to the agent in the most natural way, the tool-calling agent adaptor converts user and assistant message to the corresponding message action.

[40] h2: 3 Exgentic Framework

[41] p: General-purpose agents must operate across diverse environments, and hence viable evaluation frameworks must scale across many benchmarks and agents. The Exgentic framework enables running any currently supported agent on any supported benchmark task, with any LLM, using only a few lines of standard Python code or a dedicated GUI.

[42] p: The framework was built for use at scale and supports parallelism and caching. Every run is executed in an isolated environment and is reproducible. Benchmark results, interaction trajectories, and cost reports are created in a standardized format for all benchmarks and agents.

[43] p: The main orchestration loop is illustrated in Figure 4 . Each benchmark generates a set of sessions, where each session corresponds to a single benchmark task the agent must complete (e.g., resolving a GitHub issue, or fulfilling a specific user request). For each session, the orchestrator initializes the agent with the task description, contextual information, and the set of available actions.

[44] p: Following initialization, the agent receives the first observation from the session environment and responds by selecting one of the permissible actions. This action is executed by the environment, which returns a new observation.

[45] p: The loop continues until either the session concludes or the agent terminates by emitting no further actions. We also terminate if the number of actions/observations exceeds some threshold to avoid deadlocks or excessive costs.

[46] h3: 3.1 Solving the Integration Problem

[47] p: Adapting existing agents and benchmarks to the Unified Protocol and integrating them with the Exgentic orchestrator is conceptually straightforward but practically challenging. These components are developed independently by third‑party authors who are unaware of the Unified Protocol, the orchestrator’s execution model, or each other’s design assumptions.

[48] p: Presumably, one possible solution is to make intrusive modifications to the benchmark and agent code bases to make them use the Unified Protocol. However, such changes may be extremely costly to implement, difficult to maintain, or even impossible when the agent or benchmark is closed‑source.

[49] p: Instead, we use external adaptor code that handles synchronization and protocol translation. On the agent side, adaptors expose the Unified Protocol actions in whatever form the agent expects—Python functions, MCP server tools, or OpenAI tools. On the benchmark side, they translate each benchmark’s task definition and agent interface into the Unified Protocol. Since many adaptations repeat across agents and benchmarks, we provide base adaptors that simplify building specific ones.

[50] p: We allow agents and benchmarks to run natively and independently in separate processes, while all communication between them is mediated by the orchestrator and the corresponding adaptor components. This design ensures that neither the benchmarks nor the agents are affected by the fact that they are running inside the Exgentic framework, preserving their original behavior.

[51] p: For more details, see Appendix A , which demonstrates a complete interaction between a code-generation agent such as SmolAgents and τ 2 \tau^{2} -Bench.

[52] figure: Figure 4 : Exgentic architecture. Exgentic defines a unified protocol between agents and benchmarks. The Exgentic Orchestrator connects the agent and the benchmark, first passing the task definition and then mediates the observations and actions that are passed between the benchmark and the agent. Exgentic provides adaptors that convert the Unified Protocol into the specific protocols required by the agents and benchmarks. Finally, the benchmark provides the quality result metrics while the agent provides the agent runtime cost.

[53] h2: 4 Experimental Setup

[54] p: Our experiments include evaluation of 5 agent architectures across 3 frontier LLMs (GPT 5.2, Claude Opus 4.5, and Gemini 3 Pro, with default parameters), and a maximum of 100 turns per task, on 6 benchmark environments. Yielding 90 configurations with 100 tasks per benchmark environment. Appendix B provides detailed descriptions of the benchmark adaptations to the Unified Protocol.

[55] h3: 4.1 Benchmarks

[56] p: BrowseComp+ ( Chen et al., 2025 ) is a deep research benchmark to assess an agent’s ability to handle complex information—search tasks involving iterative search planning and multi‑step reasoning. While the original benchmark jointly evaluates LLMs and retrieval components, we fix the retriever to isolate agent reasoning and decision-making. We use the authors’ provided retriever with either BM25 ( Robertson et al., 1994 ) or Qwen3 Embedder-based dense retrieval ( Zhang et al., 2025 ) , and report results using the latter.

[57] p: τ 2 \tau^{2} -Bench evaluates customer-service agents across retail, airline, and telecom domains via LLM-simulated users, measuring both policy-compliant task completion and violation rejection. τ 2 \tau^{2} -Bench has a bespoke python API, where the agent receives a simulated user message and returns either a message reply or calls to one or more predefined tools. We map these into a message action and Exgentic actions respectively.

[58] p: SWE-Bench Verified A human-validated subset of 500 real-world software engineering tasks from popular Python repositories. Each provides a GitHub issue and repository snapshot; agents produce patches that are evaluated against hidden test suites. Following mini-swe-agent , we expose a single bash action for repository interaction in a sandboxed environment, generating patches via git diff for evaluation. This ensures uniform agent interaction.

[59] p: AppWorld is a benchmark for evaluating user-assistance agents on realistic day-to-day digital tasks. In the original protocol, the agent interacts with the environment by writing Python code that is executed in a dedicated interpreter with access to the AppWorld APIs. In our setup, we adopt this native interpreter-based interaction protocol and use the official task definitions and evaluation harness, ensuring consistent API access and evaluation conditions across all agent configurations.

[60] h3: 4.2 Agents

[61] p: ReAct We implement two ReAct-style ( Yao et al., 2023 ) agents: a vanilla ReAct baseline using LiteLLM’s tool-calling interface, and an extended version with tool shortlisting. Both are integrated with Exgentic by exposing benchmark actions as tool specifications, while the shortlisting variant is designed to handle large action spaces efficiently.

[62] p: Smolagent CodeAgent A code-generation agent that produces Python code to invoke tools rather than calling them directly. We integrate Smolagents v1.24.0 ( Roucher et al., 2025 ) with Exgentic by exposing benchmark actions as Python functions and adapting its termination behavior to use the benchmark-defined finish action.

[63] p: OpenAI Solo + MCP An agent built on OpenAI’s SDK v0.7.0 in solo mode with Model Context Protocol integration (OpenAI Solo for short). The agent operates in solo mode, interacting with environments exclusively through MCP tool calls. We integrate it with Exgentic by implementing an adapter that translates benchmark actions into MCP tool specifications.

[64] p: Claude Code A feature-rich command-line agent originally designed for software engineering tasks and recently claimed general effectiveness beyond coding 3 3 3 Building agents with the Claude Agent SDK. . We evaluate Claude Code v2.1.7 without modifying its internal logic, integrating it with Exgentic via MCP-exposed benchmark actions. The agent runs in a Docker container to ensure isolation and reproducibility.

[65] h4: 4.2.1 Agent Components

[66] p: Agents differ in implementation but share common conceptual components. To gain insight into agents’ internal behavior and its impact on performance, we adopt a component-level view covering execution runtime, tool shortlisting, schema guards, communication protocols, memory, and planning. Appendix C details their presence across agents.

[67] h3: 4.3 Metrics

[68] p: To enable consistent comparison across agents and tasks, we adopt the following general metrics. Success Rate. The proportion of runs deemed successful according to the original success definition and evaluation procedure of the benchmark. Cost per Task. The average monetary cost of completing a task, enabling comparison of agent efficiency in addition to performance. In our experiments, costs are reported using LiteLLM’s pricing data 4 4 4 Model prices and context window. . Average Steps. The mean number of steps taken by an agent to reach task completion.

[69] h2: 5 Results

[70] p: Our main results address three central questions: (1) Do agents generalize across domains? (2) What drives agent performance — Model quality or Agent architectural design? (3) What architectural components enable cross-domain capabilities?

[71] h3: 5.1 Key Leaderboard Findings

[72] p: Our benchmark evaluation reveals clear performance hierarchies at the model, agent, and configuration levels. These findings provide practitioners with actionable guidance for system selection and deployment (see Appendix D for complete leaderboard results).

[73] p: Top Configurations: The leaderboard (Table 1 ) is split between Claude Opus 4.5 and Gemini 3 based pairings, with Claude Opus 4.5 occupying the top three positions. No GPT 5.2 configuration appears in the top-10.

[74] p: We assessed statistical significance using a pooled McNemar test. While the top configuration (utilizing OpenAI Solo and Claude Opus 4.5) did not significantly outperform the second-ranked configuration, it demonstrated a significant advantage over the third-ranked ( p < 0.01 p<0.01 ) and all remaining configurations ( p < 0.001 p<0.001 ). See Appendix E for detailed statistical analysis.

[75] p: Model Performance: We compare models using their mean success rate across all agents and benchmarks, weighting τ 2 \tau^{2} -Bench subdomains equally (1/12 each) to balance benchmark representation. Claude Opus 4.5 ranks first with a success rate of 0.66, followed by Gemini 3 at 0.60, while GPT 5.2 underperforms at 0.40. Pairwise statistical tests over all (benchmark, task, agent) configurations confirm that these performance differences are significant ( p < 0.0001 p<0.0001 ). Claude Opus 4.5’s superiority is consistent across nearly all benchmarks, whereas GPT 5.2’s low aggregate performance is largely driven by failures in tool-rich environments.

[76] p: Agent Performance: We compare agents by their mean success rate across all models and benchmarks (weighting τ 2 \tau^{2} -Bench subdomains as 1/12 each to balance benchmark representation). ReAct Short leads with 0.57, closely followed by OpenAI Solo (0.57), ReAct (0.55), Claude Code (0.54), and Smolagent (0.53). Using paired McNemar test, comparing results over each pair of agents on all (benchmark, task, model) combinations, we saw that these differences not statistically significant ( p > 0.1 p>0.1 ).

[77] p: However, agent performance are model-dependent: OpenAI Solo excels with Claude Opus 4.5 (0.73) but struggles on GPT 5.2 (0.39), while ReAct Short performs more consistently across models.

[78] p: Notable Outliers: OpenAI Solo + Gemini 3 achieves the highest single-benchmark score (0.89 on τ 2 \tau^{2} -Bench-Telecom), while four GPT 5.2 configurations score 0.00 on AppWorld without tool shortlisting, as GPT 5.2 is limited to 128 tools while AppWorld requires 468. The performance spread within models ranges from 11 percentage points (Claude Opus 4.5: best 0.73, worst 0.62) to 6 percentage points (Gemini 3: best 0.62, worst 0.56), indicating that agent choice matters significantly even for strong models.

[79] h3: 5.2 No Single Agent Dominates Across Task Domains

[80] p: Table 2 shows the best-performing agent-model configuration for each benchmark.

[81] figure: Table 2 : Success rate (Score) of best agent-model configuration per benchmark. Top Score denotes the highest reported domain-specific agent performance on the original leaderboard (links are in App. D.1 ). Note: our results are on 100 randomly sampled benchmark instances, whereas the original leaderboard reports results on the full benchmark. Benchmark Best Configuration Score Top Score SWE-Bench Verified OpenAI Solo + Claude Opus 4.5 0.81 0.79 BrowseComp+ Smolagent+Claude Opus 4.5 0.61 0.80 τ 2 \tau^{2} -Bench-Airline OpenAI Solo + Claude Opus 4.5 0.74 0.73 τ 2 \tau^{2} -Bench-Retail OpenAI Solo + Claude Opus 4.5 0.85 0.86 τ 2 \tau^{2} -Bench-Telecom OpenAI Solo + Gemini 3 0.89 0.98 AppWorld Smolagent + Claude Opus 4.5 0.7 0.73

[82] p: No single agent dominates: OpenAI Solo wins 4 benchmarks and ties on 1 (SWE-Bench Verified, τ 2 \tau^{2} -Bench-Airline, τ 2 \tau^{2} -Bench-Retail, τ 2 \tau^{2} -Bench-Telecom, and BrowseComp+ tie), demonstrating particular strength on structured API interaction tasks and code generation. Smolagent wins 1 benchmark and ties on 1 (AppWorld and BrowseComp+ tie), excelling on web navigation and multi-application environments.

[83] h3: 5.3 Model Quality Drive Performance

[84] p: We performed variance decomposition to isolate the relative contributions of model choice versus agent architecture. We compute variance explained as η 2 = Var ​ ( 𝔼 ⁡ [ Y | X ] ) / Var ​ ( Y ) \eta^{2}=\text{Var}(\mathbb{E}[Y|X])/\text{Var}(Y) , where Y Y is the task success rate and X X is the grouping variable (model or agent). Model choice accounts for 28.2% of total success rate variance across all configurations, while agent architecture explains only 0.6%. The remaining 71.2% reflects task-level variance—differences in benchmark difficulty, task characteristics, and stochastic execution. Model quality is by far the strongest single factor, dominating agent architecture by more than 85-fold.

[85] h3: 5.4 Model Stability to Agent Architectures

[86] p: Beyond average performance, model stability across different agent architectures is critical for practical agent development. A stable model allows developers to iterate on agent design without model-specific tuning; an unstable model requires careful co-design of the agent-model pairing. We measure stability as the standard deviation of scores across agent architectures for each model.

[87] p: Claude Opus 4.5 exhibits the highest stability (Mean: 0.66, STD: 0.06), followed by GPT 5.2 (Mean: 0.40, STD: 0.071) and Gemini 3 (Mean: 0.59, STD: 0.09). Claude’s standard deviation is slightly lower than Gemini 3’s, indicating that agent performance with Claude varies minimally across architectural choices.

[88] p: Stability has practical implications for agent development workflows. With Claude Opus 4.5, developers may focus on agent architecture without extensive model-specific optimization. With Gemini, agent-model co-design may becomes necessary, increasing development cost and reducing modularity. For practitioners prioritizing development efficiency and deployment flexibility, model stability may be as important as absolute performance.

[89] h3: 5.5 Agent Components Effect

[90] p: Several agent components discussed in Section 4.2.1 prove useful across agent implementations or models. Notably, the top three performing architectures—OpenAI Solo, Claude Code, and Smolagent—all employ a schema guard component: a mechanism that detects when an action with an invalid schema is invoked and allows the agent to correct itself. This highlights the potential value of such self-correction mechanisms across agents based on Claude Opus 4.5. Tool shortlisting, when added to a simple ReAct agent with tool calling, improves performance across all models in tool-rich environments. For GPT 5.2, shortlisting adds 5 percentage points overall, while for Claude Opus 4.5 the gain is more modest (1 percentage point) but comes with a substantial cost reduction of $1.97 on average. These results underscore the importance of documenting agent components, sharing implementation details, and conducting ablation studies as a primary means of advancing general agent development.

[91] h3: 5.6 Cross-Benchmarks Agent Stability

[92] p: To assess whether agent performance generalizes across task types, we computed Spearman rank correlations between benchmark scores across all agent-model configurations. Results reveal moderate to strong positive correlations across most benchmark pairs: τ 2 \tau^{2} -Bench-Airline vs τ 2 \tau^{2} -Bench-Retail shows + 0.85 +0.85 (strong positive), SWE-Bench Verified vs τ 2 \tau^{2} -Bench-Telecom shows + 0.78 +0.78 , and AppWorld vs τ 2 \tau^{2} -Bench-Retail shows + 0.75 +0.75 . BrowseComp+ shows more moderate correlations with other benchmarks (0.32 to 0.74), suggesting it captures somewhat distinct capabilities while still following overall model quality trends.

[93] p: The predominantly positive correlations are driven by systematic model differences—GPT 5.2 underperforms across nearly all benchmarks (mean 0.40) while Claude Opus 4.5 excels broadly (mean 0.66). This creates cross-benchmark consistency at the model level but does not imply agent-level generalization. Within-model analysis reveals that agent rankings vary substantially: on Claude, OpenAI Solo leads (0.73), while on GPT 5.2, ReAct Short leads (0.46).

[94] p: These findings challenge the notion of ”general-purpose” agents. Current architectures do not achieve robust generalization but instead optimize for specific task distributions. An agent’s benchmark performance is a poor predictor of its performance on dissimilar tasks.

[95] h3: 5.7 Cost-Efficiency Tradeoffs

[96] p: We computed cost-efficiency as average score divided by average inference cost per task 5 5 5 Costs computed using LiteLLM’s pricing data as of January 2026, based on public API list prices. Enterprise pricing may differ substantially. . Table 3 shows that GPT 5.2 configurations dominate the efficiency rankings. For comparison, the best-performing configuration overall—OpenAI Solo + Claude Opus 4.5 (0.73 average score)—has substantially higher costs per task. Achieving state-of-the-art performance requires 30 × \times higher cost than the most efficient configurations, representing a fundamental tradeoff between absolute performance and cost.

[97] figure: Table 3: Most and least cost-efficient configurations per model Configuration Score Cost/Task Efficiency ReAct + GPT 5.2 0.41 $0.17 2.41 Claude Code + GPT 5.2 0.38 $0.38 1.00 ReAct + Gemini 3 0.62 $0.66 0.93 OpenAI Solo + Gemini 3 0.60 $2.81 0.21 ReAct Short + Claude Opus 4.5 0.62 $3.78 0.16 Claude Code + Claude Opus 4.5 0.67 $8.03 0.08

[98] p: This Pareto frontier shown in Figure 1 has practical implications. Cost-sensitive applications (internal tools, high-volume automation) may prefer GPT 5.2 configurations despite 27 point performance gaps. Performance-critical applications (customer-facing agents, high-stakes decisions) justify the premium for Claude-based configurations. Gemini 3 configurations may represent a middle ground between cost and performance. There is no universal “best” choice—optimal selection depends on application-specific cost-performance requirements.

[99] h3: 5.8 Failure Patterns and Agent Behavioral Differences

[100] p: We examined whether failures are associated with increased number of interactions between the agent and the environment, resulting in higher computational cost, and whether this pattern is consistent across agents architectures.

[101] p: To this end, we compared successful and failed runs at the task level, aggregating across backbone models for each benchmark and agent architecture 6 6 6 We excluded zero-step sessions and capped step counts at 50 to reduce the influence of long-tail outliers, which accounts to 7% of total runs. .

[102] p: For each benchmark and agent architecture, we report the percent increase in mean steps for failed runs relative to successful runs (positive means failures are longer). Table 4 shows this gap is positive in most settings, with the largest overheads on interaction-heavy benchmarks such as AppWorld and BrowseComp+ (e.g., ReAct is + 110.7 % +110.7\% on AppWorld). A few τ 2 \tau^{2} -Bench cells are near zero or negative, indicating some failures terminate early. The detailed interactions counts appear in App. D.2 .

[103] p: Benchmark-weighted averages are positive for every agent architecture (Claude Code 38.8 % 38.8\% , OpenAI Solo 20.0 % 20.0\% , Smolagent 26.4 % 26.4\% , ReAct 54.4 % 54.4\% , ReAct Short 45.1 % 45.1\% ), implying that failed runs generally consume more steps—and there fore more cost—than successful runs, amplifying the practical penalty of unreliability.

[104] p: This pattern indicates that tasks that ultimately fail tend to take longer, whereas easier tasks complete more quickly. While this trend appears across all architectures, they differ in the magnitude of the effect. These differences suggest the existence of variations along more subtle dimensions than overall performance and cost. Understanding these finer‑grained behavioral characteristics—for example, how architectures allocate interaction budget, manage uncertainty, or recover from partial progress—may be important when designing or selecting agent architectures.

[105] figure: Table 4: How much longer failed runs are than successful ones, measured by the percentage difference in number of interactions. Positive values mean failures take more interactions; negative values mean they take fewer. Benchmark Claude Code OpenAI Solo Smolagent ReAct ReAct Short AppWorld 63% 49% 33% 111% 74% BrowseComp+ 70% 18% 50% 67% 67% SWE-Bench Verified 16% 6% 9% 21% 21% τ 2 \tau^{2} -Bench-Airline 25% 34% 35% 31% 31% τ 2 \tau^{2} -Bench-Retail -2% -14% -2% 7% 7% τ 2 \tau^{2} -Bench-Telecom -6% 2% 6% 20% 20% Average 39% 20% 26% 54% 45%

[106] h3: 5.9 The Current State of General-Purpose Agents

[107] p: Four overarching themes emerge from our evaluation. First, model quality creates cross-benchmark consistency . No agent achieves consistently strong performance across all benchmarks, but strong positive correlations (0.75-0.85) across most benchmark pairs reflect systematic model differences. Claude Opus 4.5 excels broadly (mean 0.66), Gemini shows moderate performance (mean 0.60), and GPT 5.2 underperforms significantly (mean 0.40). Agent rankings vary within models, but model effects dominate overall patterns.

[108] p: Second, model quality dominates agent architecture . Model choice explains 28.2% of score variance while agent architecture explains only 0.6%. The model-agent interaction effect (5.0%) exceeds the agent main effect by more than 4.5-fold, indicating that optimal agent selection depends heavily on the model. However, model differences—particularly GPT 5.2 failures on tool-rich environments—drive most performance variation. Agent architecture matters primarily for enabling model capabilities (e.g., ReAct Short for GPT 5.2) rather than as an independent performance driver.

[109] p: Third, practical deployment considerations—cost, tool scalability, component complexity—are not secondary concerns but fundamental constraints . Tool shortlisting transforms GPT 5.2 from unusable to viable in tool-rich environments. Cost-efficiency varies by 33 × \times across configurations. Sophisticated components like memory and planning correlate with gains but increase implementation complexity. These tradeoffs define the space of viable deployments rather than being post-hoc optimizations.

[110] p: Fourth, general-purpose agents are competitive with benchmark-specific heavily customized agents . Our results show that across benchmarks, general agents largely match or exceed specialized systems (Tab. 2 ). Overall, although general agents have not yet been systematically pursued in full and still have substantial room to improve, these results establish general agents as a promising direction for future research and development.

[111] p: Progress toward general-purpose agents requires addressing generalization explicitly through cross-benchmark evaluation. Improving single-benchmark performance does not yield generalizing agents.

[112] h2: 6 Related Work

[113] p: Domain-Specific Agent Benchmarks. The rapid advancement of AI agents has led to a proliferation of benchmarks ( Zhou et al., 2023 ; Deng et al., 2023 ; Xie et al., 2024 ; Liu et al., 2023 ) , each targeting specific domains such as software engineering ( Jimenez et al., 2023 ; Merrill et al., 2026 ) , customer service ( Yao et al., 2024 ) and deep scientific research ( Bragg et al., 2025 ) . Each benchmark defines domain-specific protocols and task specifications.

[114] p: Attempts at Consolidation HAL ( Kapoor et al., 2025 ) unifies infrastructure across benchmarks but requires per-benchmark agent adaptation. BrowserGym ( Chezelles et al., 2025 ) and Harbor ( Shaw, 2025 ) standardize interaction via fixed protocols (web/CLI) but restrict evaluation to single environment classes. AgentBeats 7 7 7 AgentBeats models agents and benchmarks as interacting via A2A/MCP subsets, standardizing evaluation lifecycle components but leaving task semantics to individual benchmarks. Exgentic enables protocol-preserving evaluation across heterogeneous benchmarks, supporting consistent comparison without per-benchmark adaptation.

[115] h2: 7 Discussion

[116] p: This work takes a first step toward systematic research of general-purpose agents—a fundamental gap in the field. We develop Exgentic and the Unified Protocol to address the current landscape while providing infrastructure that evolves with emerging agents and benchmarks. Our initial results demonstrate that agents can generalize across domains without domain-specific adaptation, matching or exceeding domain-specific performance across most benchmarks and establishing general agents as a viable alternative (Tab. 2 ). Our evaluation reveals promising opportunities for advancement: substantial performance headroom, domain variations suggesting architectural improvements, and clear cost-performance optimization targets. These findings point to exciting research directions—enhancing performance through better reasoning and planning, achieving cross-domain consistency, developing cost-effective solutions, and expanding to multimodal and safety-critical scenarios. The Open General Agent Leaderboard and Exgentic provide a foundation for systematic comparison and iterative progress toward truly capable general-purpose agents.

[117] h2: Impact Statement

[118] p: The current research landscape for AI agents is fragmented by domain-specific benchmarks and communication protocols, which limit the development of general-purpose systems. This work introduces Exgentic and the Unified Protocol to bridge these gaps, enabling the first systematic evaluation of general agents across diverse environments. By establishing the Open General Agent Leaderboard, we provide the research community with a foundation for developing agents that transcend individual tasks and generalize across heterogeneous real-world settings. Our findings highlight that while model quality remains the primary driver of performance, standardized evaluation is essential for identifying the architectural components that enable scalable, cross-domain capabilities.

[119] h2: References

[120] h2: Appendix A Detailed Benchmark Agent Interaction Example

[121] p: This section demonstrate a complete interaction between a code-generation agent such as SmolAgents and the τ 2 \tau^{2} -Bench benchmark.

[122] p: Agent Side. During initialization, the SmolAgent adaptor converts all Exgentic actions into lightweight Python wrapper functions. A standard SmolAgent instance is then created using the session’s task definition and the set of wrapper functions.

[123] p: When the agent invokes one of these wrapper functions, the wrapper places the corresponding action into an action queue and blocks while waiting for a response in a observation queue .

[124] p: Later, when the orchestrator calls

[125] table: action = CodeAgentWrapper . react ⁡ ( observation ) , \text{action}=\operatorname{CodeAgentWrapper.react}(\text{observation}),

[126] p: the adaptor stores the observation in the observation queue , unblocking the agent-side wrapper function. The wrapper retrieves the observation and returns it to the agent as the result of the function call. Meanwhile, react ⁡ ( ⋅ ) \operatorname{react}(\cdot) waits for the next action to appear in the action queue .

[127] p: On the next invocation of a wrapper function, the agent places a new action in the action queue , which releases the blocked react ⁡ ( ⋅ ) \operatorname{react}(\cdot) call. The action is then returned to the orchestrator, which forwards it to the benchmark session, obtains the next observation, and calls react ⁡ ( ⋅ ) \operatorname{react}(\cdot) again.

[128] p: This cycle continues until either the agent produces no further actions or the benchmark provides no further observations, signaling the end of the session.

[129] p: Benchmark Side. During initialization in TauBenchBenchmark . start ⁡ ( ) \operatorname{TauBenchBenchmark.start}() , the list of available task names is retrieved from the τ 2 \tau^{2} -Bench codebase. When TauBenchBenchmark . next ​ _ ​ session ⁡ ( ) \operatorname{TauBenchBenchmark.next\_session}() is invoked, a Session wrapper object is constructed. This wrapper defines the textual task description for the selected task and translates τ 2 \tau^{2} -Bench’s OpenAI tool specifications into Exgentic protocol actions. It then builds a proxy agent compatible with τ 2 \tau^{2} -Bench’s internal agent API and begins executing τ 2 \tau^{2} -Bench code for the selected task.

[130] p: When τ 2 \tau^{2} -Bench calls the proxy agent to obtain the next action given a simulated user message, the proxy agent stores the message in an observation queue and waits for an action to appear in the action queue . Once the orchestrator executes

[131] table: observation = TauBenchBenchmark . step ⁡ ( action ) , \text{observation}=\operatorname{TauBenchBenchmark.step}(\text{action}),

[132] p: the benchmark wrapper stores the action in the action queue , allowing the proxy agent to resume and forward the action to τ 2 \tau^{2} -Bench. Meanwhile, TauBenchBenchmark . step ⁡ ( ⋅ ) \operatorname{TauBenchBenchmark.step}(\cdot) blocks on the observation queue . When the proxy agent is called again by the τ 2 \tau^{2} -Bench code with the next simulated user message , it stores the message in the observation queue, enabling the observation to be returned to the orchestrator, which then passes it to the real agent.

[133] h2: Appendix B Benchmark Adaptation

[134] h3: B.1 SweBench Task Definition Example

[135] h4: Task

[136] h4: Context

[137] table: Key Value (no entries)

[138] h4: Actions

[139] p: bash

[140] p: finish

[141] h3: B.2 BrowseComp Task Definition Example

[142] h4: Task

[143] h4: Context

[144] table: Key Value (no entries)

[145] h4: Actions

[146] p: search(query: str)

[147] p: submit(exact_answer: str, explanation: str, confidence: float)

[148] p: get_document(docid: str)

[149] h3: B.3 Appworld Task Definition Example

[150] h4: Task

[151] h4: Context

[152] table: Key Value policy This environment provides a set of applications, each exposing a predefined set of APIs that may be used to perform tasks on behalf of the supervisor. The applications include: api_docs, supervisor, amazon, phone, file_system, spotify, venmo, gmail, splitwise, simple_note, todoist. The available applications and their APIs are fixed for the task. Supervisor account credentials (such as emails, usernames, and passwords) are available through the supervisor application’s APIs and are accessed from there when required. If an application requires an access token to perform authenticated operations, the access token is obtained by calling that application’s authentication/login API using the credentials retrieved from the supervisor application. Access tokens are not provided by the supervisor application. References to people (e.g., friends, family, roommates) correspond to entries in the phone_contacts application. References to files or storage correspond to the file_system application, not the local machine filesystem. Time-based instructions (e.g., ’this month’, ’yesterday’) are interpreted with full calendar boundary ranges. If an API returns paginated results, all pages constitute the complete result. The environment consists only of the provided applications and their documented APIs and parameters. No additional endpoints, methods, arguments, or capabilities are assumed beyond those explicitly defined. When task execution is finished, the designated task-completion API is used to signal completion. If the task requires a final answer value, the answer is returned through that completion API. If the task cannot be completed using the available applications and APIs, the task may be marked as failed. supervisor {”first_name”: ”Ashley”, ”last_name”: ”Moore”, ”email”: ”as_moore@gmail.com”, ”phone_number”: ”7336094411” } datetime 2023-05-18T12:00:00

[153] h4: Actions (overall 468)

[154] p: finish

[155] p: supervisor.show_profile

[156] p: supervisor.show_addresses

[157] p: supervisor.show_payment_cards

[158] p: supervisor.show_account_passwords

[159] p: amazon.show_account

[160] p: amazon.signup

[161] p: amazon.delete_account

[162] p: amazon.update_account_name

[163] p: amazon.login

[164] p: amazon.logout

[165] p: amazon.clear_browsing_history

[166] p: amazon.search_sellers

[167] p: amazon.show_cart

[168] p: amazon.update_product_quantity_in_cart

[169] p: amazon.show_wish_list

[170] p: amazon.update_address

[171] p: amazon.show_product_reviews

[172] p: amazon.write_product_review

[173] p: amazon.show_product_questions

[174] p: .... many more tools ...

[175] p: phone.search_contacts

[176] p: phone.send_text_message

[177] p: phone.show_alarm

[178] p: phone.update_alarm

[179] p: file_system.create_directory

[180] p: file_system.show_file

[181] p: spotify.show_account

[182] p: spotify.search_songs

[183] p: simple_note.create_note

[184] p: todoist.create_task

[185] h3: B.4 Tau2Bench Task Definition Example

[186] h4: Task

[187] h4: Context

[188] table: Key Value policy # Airline Agent Policy The current time is 2024-05-15 15:00:00 EST. As an airline agent, you can help users **book**, **modify**, or **cancel** flight reservations. You also handle **refunds and compensation**. Before taking any actions that update the booking database (booking, modifying flights, editing baggage, changing cabin class, or updating passenger information), you must list the action details and obtain explicit user confirmation (yes) to proceed. You should not provide any information, knowledge, or procedures not provided by the user or available tools, or give subjective recommendations or comments. You should only make one tool call at a time, and if you make a tool call, you should not respond to the user simultaneously. If you respond to the user, you should not make a tool call at the same time. You should deny user requests that are against this policy. You should transfer the user to a human agent if and only if the request cannot be handled within the scope of your actions. To transfer, first make a tool call to transfer_to_human_agents, and then send the message ’YOU ARE BEING TRANSFERRED TO A HUMAN AGENT. PLEASE HOLD ON.’ to the user. ……

[189] h4: Actions

[190] p: message

[191] p: book_reservation

[192] p: calculate

[193] p: cancel_reservation

[194] p: get_reservation_details

[195] p: get_user_details

[196] p: list_all_airports

[197] p: search_direct_flight

[198] p: search_onestop_flight

[199] p: send_certificate

[200] p: transfer_to_human_agents

[201] p: update_reservation_baggages

[202] p: update_reservation_flights

[203] p: update_reservation_passengers

[204] p: get_flight_status

[205] h2: Appendix C Agent Components

[206] p: We outline the key components and, in Table 5 , analyze the components present in each agent.

[207] p: Execution Runtime . Agents may have access to sandboxed execution environments where they can run code dynamically. For example, SmolAgents provides a Python interpreter, while Claude Code operates within a Linux machine environment. These runtime environments enable agents to execute and test code as part of their problem-solving process. Tool Shortlisting . A preprocessing component that filters the available tool set before each action step, selecting a relevant subset based on current context. This improves efficiency and decision quality by focusing the agent on contextually appropriate tools, and addresses LLM constraints on tool count—when the full tool set exceeds model limits, shortlisting becomes necessary for task completion. Tool Schema Guard . A component that validates actions against expected schemas before execution. When an agent attempts to call a tool or execute an environment action with incorrect parameters or structure, the schema validator raises an internal error, allowing the agent to detect and correct the mistake. This component is implemented differently across agent types: tool-calling agents typically lack explicit schema validation (relying on the LLM to generate correct calls), MCP-based agents include built-in schema validation as part of the MCP protocol, and Python-based agents receive runtime errors from the Python interpreter that serve a similar validation function. Communication Protocol . The interface through which agents invoke tools and receive results. Agents may use direct tool-calling APIs (e.g., OpenAI function calling), code-generation approaches where the agent writes executable code, or standardized protocols like MCP. Protocol choice affects action expressiveness and error handling mechanisms available to the agent. Memory . Explicit storage and retrieval mechanisms beyond the conversation history. Memory components allow agents to maintain working state across turns, recall previous observations, and avoid redundant actions. Without explicit memory, agents rely solely on the LLM’s context window. Planning . Components that decompose tasks into structured subgoals before execution. Planning modules may generate explicit task hierarchies or action sequences, enabling more directed problem-solving. Agents without planning components select actions reactively at each step based on immediate observations.

[208] figure: Table 5 : Architectural components of evaluated agents. ✓ denotes an explicit, modular component; ✓ × \overset{\times}{\checkmark} denotes an implicit or non-modular capability; ✗ denotes absence. Agent Execution Runtime Tool Shortlisting Tool Schema Guard Communication Protocol Memory Planning ReAct ✗ ✗ ✗ Tool-calling ✓ × \overset{\times}{\checkmark} ✓ × \overset{\times}{\checkmark} ReAct Short ✗ ✓ ✗ Tool-calling ✓ × \overset{\times}{\checkmark} ✓ × \overset{\times}{\checkmark} Smolagent ✓ ✗ ✓ Python-Functions ✓ × \overset{\times}{\checkmark} ✓ × \overset{\times}{\checkmark} OpenAI Solo ✗ ✗ ✓ MCP ✓ × \overset{\times}{\checkmark} ✓ × \overset{\times}{\checkmark} Claude Code ✓ ✗ ✓ MCP ✓ ✓

[209] h2: Appendix D Detailed Results

[210] p: Table 1

[211] figure: Table 6: Agent-Model Configuration Leaderboard Agent Model App Browse SWE Airline Retail Telecom Mean Steps Cost Score (avg) ($) OpenAI Solo Claude Opus 4.5 0.68 0.61 0.81 0.74 0.85 0.84 0.73 30.7 8.54 Claude Code Claude Opus 4.5 0.66 0.53 0.74 0.66 0.83 0.76 0.67 31.7 8.03 Smolagent Claude Opus 4.5 0.70 0.61 0.65 0.72 0.78 0.58 0.66 29.2 4.39 ReAct Short Gemini 3 0.55 0.48 0.71 0.70 0.82 0.73 0.62 18.8 0.66 ReAct Short Claude Opus 4.5 0.64 0.49 0.61 0.66 0.78 0.76 0.62 24.5 3.78 ReAct Gemini 3 0.51 0.48 0.71 0.70 0.82 0.73 0.61 18.6 0.81 ReAct Claude Opus 4.5 0.61 0.49 0.61 0.66 0.78 0.76 0.61 25.0 5.75 OpenAI Solo Gemini 3 0.58 0.33 0.72 0.62 0.73 0.89 0.60 21.3 2.81 Claude Code Gemini 3 0.36 0.51 0.67 0.70 0.78 0.69 0.57 29.0 2.47 Smolagent Gemini 3 0.13 0.57 0.76 0.68 0.76 0.88 0.56 32.2 1.85 ReAct Short GPT 5.2 0.22 0.46 0.57 0.54 0.73 0.54 0.46 12.3 0.26 ReAct GPT 5.2 0.00 0.46 0.57 0.54 0.73 0.54 0.41 9.8 0.17 OpenAI Solo GPT 5.2 0.00 0.48 0.55 0.50 0.54 0.53 0.39 11.3 0.19 Claude Code GPT 5.2 0.00 0.43 0.58 0.48 0.51 0.55 0.38 10.7 0.38 Smolagent GPT 5.2 0.07 0.26 0.53 0.60 0.68 0.71 0.38 22.2 0.36

[212] p: presents the complete leaderboard results, including the average number of steps.

[213] h3: D.1 References to Leaderboards

[214] p: For reference, SWE-Bench Verified leaderboard top reported domain-specific agent achieves 0.79 8 8 8 SWE-Bench Verified , BrowseComp+ and AppWorld are 0.80 9 9 9 BrowseComp+ , and 0.73 0.73 10 10 10 AppWorld , respectively. τ 2 \tau^{2} -Bench Airline ( 0.73 0.73 ), Retail ( 0.86 0.86 ), and Telecom ( 0.98 0.98 ) 11 11 11 τ 2 \tau^{2} -Bench .

[215] h3: D.2 Steps Counts

[216] figure: Table 7: Average steps per benchmark and architecture, split by successful vs. failed sessions; models are aggregated, 0-step sessions are excluded, and steps are capped at 50. Benchmark Claude Code Succ Claude Code Fail OpenAI Solo Succ OpenAI Solo Fail Smolagent Succ Smolagent Fail ReAct Succ ReAct Fail ReAct Short Succ ReAct Short Fail AppWorld 23.67 38.56 26.41 39.39 25.69 34.17 13.24 27.91 12.34 21.41 BrowseComp+ 13.90 23.64 15.23 17.96 15.89 23.83 9.28 15.53 9.28 15.53 SWE-Bench Verified 27.69 32.21 27.76 29.30 29.28 32.03 28.38 34.22 28.38 34.22 airline 10.43 13.02 10.19 13.65 10.39 14.06 9.31 12.18 9.31 12.18 retail 11.73 11.54 11.36 9.81 11.48 11.31 10.81 11.52 10.81 11.52 telecom 12.98 12.25 13.06 13.26 11.99 12.75 13.23 15.84 13.23 15.84 weighted_avg 19.24 26.67 20.24 24.72 20.54 25.68 15.50 22.71 15.28 21.08

[217] h2: Appendix E Statistical Significance

[218] p: We assess the statistical significance of the benchmark results. The evaluation consists of six benchmarks, each containing 100 independent instances with binary (0/1) success outcomes (except τ 2 \tau^{2} -Bench Airline, which contains 50 instances).

[219] p: For a single benchmark with n = 100 binary trials, the 95% Wilson confidence‑interval half‑width typically ranges from 7 to 9.5 percentage points when the observed success rate lies between 0.3 and 0.8—the region where most leading models perform. This means that differences smaller than approximately 8–10 percentage points on individual benchmarks should be interpreted cautiously, as they fall within normal statistical uncertainty. To obtain a more stable measure, we compute a weighted aggregate score across all benchmark instances. Under the assumption that benchmarks are independent of one another, this yields an effective sample size of n = 650. The corresponding 95% delta‑method confidence‑interval half‑width for the aggregated score is substantially smaller—typically in the range of 4–5 percentage points. Thus, while individual benchmark scores have relatively wide uncertainty due to limited sample sizes, the aggregated metric provides a more reliable estimate of overall agent performance. It is important to note that these levels of statistical uncertainty are standard across existing agentic leaderboards. Most widely used agent‑evaluation platforms report confidence intervals on the order of only a few percentage points, reflecting the inherent variability of evaluations conducted on datasets of similar size.

[220] p: To enhance statistical power when comparing benchmarks, we employ McNemar’s test for pairwise analysis. This allows us to determine if one configuration significantly outperforms another by isolating performance discrepancies on identical tasks.

[221] h2: Appendix F Limitations

[222] p: While Exgentic provides a clear methodology and reusable building blocks for adaptation, familiarity with these capabilities and addition development work is still required when integrating new agents or benchmarks.

[223] p: Currently, Exgentic focuses on evaluating tasks where all agent–benchmark interactions are text‑based. Future extensions should support visual or web‑based interaction. The Unified Protocol was designed around the APIs of a subset of existing systems and may need to be expanded to accommodate these additional protocols

[224] p: Agent evaluation is expensive, more over for general‑purpose agents that must be tested across many benchmarks. Due to cost constraints, our selection of agents and models is limited and does not cover the full range of open‑source models or existing general‑purpose agents. To enable further progress in the field, future work should therefore explore techniques such as intelligent sampling and early stopping to reduce evaluation costs when it is clear that certain agent–model combinations underperform.

[225] p: 9

[226] h2: Instructions for reporting errors

[227] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[228] p: Tip: You can select the relevant text first, to include it in your report.

[229] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[230] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
