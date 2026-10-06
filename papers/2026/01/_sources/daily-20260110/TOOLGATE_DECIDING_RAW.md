# ToolGate 原准入决定核心

ToolGate: Contract-Grounded and Verified Tool Execution for LLMs (https://arxiv.org/html/2601.04688v1)
citeturn26842view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04688v1","lineno":120}); Total lines: 633
L75: However, existing frameworks for LLM tool calling rely heavily on natural language reasoning to determine when tools should be invoked and whether their results should be trusted and committed to the system’s understanding of the world cite57†Yang et al. (2024a) . This reliance on implicit natural language reasoning creates challenges for ensuring logical safety, verifiability in tool-augmented LLM systems.
L76: The fundamental problem lies in the lack of formal guarantees for tool invocation and result validation. Current approaches treat tool calling as a black-box process where the LLM decides based on its internal reasoning, without explicit mechanisms to verify whether the preconditions for tool invocation are satisfied or whether the tool’s output meets the expected postconditions cite58†Zhu et al. (2025) ; cite59†Shi et al. (2023) .
L77: This can lead to several critical issues: tools may be called with insufficient or incorrect parameters, invalid results may be incorporated into the reasoning process, and the system’s internal representation of the world state may become inconsistent or corrupted by hallucinated or erroneous tool outputs cite60†Huang et al. (2025) .
L78: Moreover, as the number of available tools grows into the thousands, efficiently retrieving and selecting appropriate tools becomes increasingly challenging, requiring sophisticated retrieval mechanisms beyond simple keyword matching cite61†Xu et al. (2024) . Recent approaches still lack a unified framework that provides formal guarantees for when tools can be safely invoked and when their results can be trusted.
L79: The absence of explicit state management and contract-based verification means that errors can propagate through the reasoning chain, making it difficult to identify and debug failures in complex multi-step tool-calling scenarios.
L80: To address these limitations, we propose ToolGate, a forward execution framework that provides logical safety guarantees and verifiable state evolution for LLM tool calling. ToolGate introduces an explicit symbolic state space that maintains a typed key-value mapping representing trusted world information throughout the reasoning process.
L81: Each tool is formalized as a Hoare-style contract with a precondition that gates tool invocation and a postcondition that determines whether the tool’s result can be committed to update the state.
L82: By combining Retrieval with embedding semantic search for efficient tool retrieval and hoare contract logical checks for safe tool execution, ToolGate ensures that the symbolic state evolves only through verified tool executions, preventing invalid or hallucinated results from corrupting the world representation.
L83: Our Contributions. Our contributions are detailed as follows.
L84: 
L85:   * •
L86: 
L87: We present ToolGate, a novel framework that formalizes tool calling through Hoare-style contracts, providing logical safety guarantees and verifiable state evolution for LLM tool-augmented systems.
L88: 
L89:   * •
L90: 
L91: We introduce an explicit symbolic state space that maintains trusted world information throughout reasoning, enabling precise precondition and postcondition checking for tool invocations.
L92: 
L93:   * •
L94: We demonstrate that contract-based verification significantly improves the reliability and debuggability of tool-augmented LLM systems while maintaining competitive performance on complex multi-step reasoning tasks.
L95: ## 2 Related Work
L96: ### 2.1 Tool Learning of LLMs
L97: The integration of external tools with Large Language Models has emerged as a critical capability for extending LLM reasoning beyond text generation to real-world interactions. Early work on function calling, such as OpenAI’s function calling API, enables LLMs to invoke external functions with structured parameterscite62†Ouyang et al. (2022) .
L98: The ReAct framework formalizes the reasoning-acting paradigm, where LLMs explicitly alternate between reasoning steps and tool invocations, demonstrating improved performance on complex multi-step reasoning tasks cite57†Yang et al. (2024a) . Building on this foundation, Tool Learning has emerged as an effective paradigm for significantly expanding the capabilities of Large Language Models cite63†Schick et al. (2023) ; cite64†Qin et al. (2023) ; cite65†Yu et al. (2025) .
L99: Early research proposed that by integrating LLMs with external tools—such as program executors or search engines cite66†Erdogan et al. (2024) ; cite67†Paranjape et al. (2023) . To comprehensively measure performance in tool usage, researchers have introduced a series of benchmarks to systematically evaluate dimensions ranging from API selection and parameter generation quality to generalization capabilities cite68†Ye et al. (2025) ; cite69†Patil et al. (2024) ; cite70†Du et al. (2024) .
L100: These techniques have been extended to multimodal tasks like GUI Agents cite71†Zhang et al. (2025a) ; cite72†Liu et al. (2025b) and specialized domains cite73†Su et al. (2025) . More recently, Reinforcement Learning (RL) has been incorporated into the framework to further optimize tool-learning performance cite74†Qian et al. (2025) ; cite75†Li et al. (2025) , yielding significant results in information retrieval and dynamic reasoning.
L101: These developments demonstrate that tool-augmented LLMs are revealing vast potential for open-domain general reasoning.
L102: ### 2.2 Hoare Logic and Formal Verification
L103: Hoare logic cite76†Hoare (1969) provides a formal system for reasoning about program correctness through preconditions and postconditions. In recent years, Formal Verification and Hoare logic has been increasingly introduced into the field of deep learning to characterize and constrain the provable behaviors of neural network systems under different inputs and internal states cite77†Corsi et al. (2021) .
L104: As deep learning models are being widely deployed in high-risk and safety-critical domains such as autonomous driving, robotics control, medical decision-making, and industrial systems, ensuring that model outputs are not only effective but also verifiable and compliant with predefined specifications has become an increasingly important problem cite78†Meng et al. (2022) ; cite79†Swaroop et al. (2024) .
L105: In this context, the precondition–postcondition framework provided by Hoare logic is used to specify the functional, safety, or robustness properties that neural networks must satisfy under given input conditions or first-order logic cite80†Yang et al. (2024b) ; cite81†Han et al. (2024) , and it is further combined with neural network verification and LLMs to form a unified and rigorous approach to reasoning and verification cite82†Lee et al. (2025) ; cite83†Grigorev et al. (2025) ; cite84†Wang et al.
L106: (2019) ; cite85†Lin et al. (2024) .
L107: ## 3 Methodology
L108: ### 3.1 Problem Setting and Overview
L109: Tool learning equips LLMs with the ability to plan, invoke, and reason over external tools. However, hallucination propagation and unreliable tool planning remain major bottlenecks, frequently leading to unstable and unreliable outcomes. To address these problems, we propose ToolGate, a framework integrates both probabilistic reasoning foundations and logically verifiable guarantees.
L110: It consists of a typed symbolic world state $S$ that maintains trusted information, Hoare-style logical contracts $\{P_{t}\}\ t\ \{Q_{t}\}$ for tools, and a probabilistic reasoning mechanism driven by large language models but constrained by Hoare logic.
L111: Problem description. Given an input sequence $x$ and a set of available tools $T=\{t_{1},t_{2},\dots,t_{n}\}$, tool learning aims to produce an answer through:
L112: 
L113:  | $$y=\arg\max_{y_{i}}P(y_{i}\mid x,\;T_{0}=\{t_{x_{i}}\})$$  |  | (1)
L114: 
L115: where $T_{0}$ represents the tools selected based on the input $x$, along with their corresponding outputs.
L116: cite86†Image: Refer to caption Figure 1: ToolGate framework overview. The framework is built on Hoare Logic, formalizing the tool-calling process as a sequence of constrained logical reasoning steps, and continuously maintaining a trusted state $S$ to verify the conditions for tool invocation.
L117: ### 3.2 Symbolic State Construction and Tool Contracts
L118: 
L119: To ensure that tool execution is not driven merely by unstructured natural-language memory but is grounded in a verifiable and logically interpretable world model, we first construct a typed symbolic state space $\Sigma$. We maintain a trusted symbolic state $S\in\Sigma$, where each element is represented as a tuple $(k,v,\sigma)$ capturing a key, its value, and its associated type, i.e.,
L120: 
L121:  | $$\Sigma=\{(k,v,\sigma)\}$$  |  | (2)
L122: This representation allows the system to explicitly encode “what is currently known” in a structured and inspectable manner. Verified entities, intermediate reasoning outcomes, and validated tool outputs are all written into this state space.
L123: To enforce logical consistency throughout reasoning and tool execution, we additionally define a set of logical predicates over $\Sigma$ to express existence constraints, type consistency, and semantic invariants, and we denote $S\models\varphi$ to indicate that a given symbolic state $S$ satisfies a logical condition $\varphi$.
L124: To prevent the model from invoking tools arbitrarily and reduce hallucinated or unconstrained execution behavior, we assign each tool $t\in\mathcal{T}$ a Hoare-style logical contract of the form
L125: 
L126:  | $$\{P_{t}\}\ t\ \{Q_{t}\}$$  |  | (3)
L127: The precondition $P_{t}:\Sigma\rightarrow\{true,false\}$ specifies the minimal state requirements that must be satisfied for the tool to be legally callable, meaning a tool is not executable unless $S\models P_{t}$ holds. Meanwhile, the postcondition $Q_{t}:\Sigma\times R_{t}\rightarrow\{\text{true},\text{false}\}.$ constrains the structural validity, typing correctness, and semantic consistency of the runtime output $r_{t}$, while also defining how a verified result updates the system state.
L128: ### 3.3 Tool Call and Reranking
L129: 
L130: We first treat the model’s reasoning as a process of conditional probability propagation over time. At the $k$-th step, the reasoning state is represented as
L131: 
L132:  | $$p(R_{k}\mid q,H,S_{k})$$  |  | (4)
L133: where $q$ denotes the current user query, $H$ represents the stable and externally visible dialogue history, and $S_{k}$ denotes the trusted symbolic state at this time. We define $R_{k}$ as the current reasoning trajectory, which records the intermediate reasoning content, reasoning path, and any tool results already injected before step $k$.
L134: In this formulation, $H$ tracks externally observable interaction, while $R_{k}$ captures the evolution of the model’s internal reasoning process, making it clear, in subsequent tool selection and state updates, which information originates from the user and which originates from internal reasoning.
L135: Next, we turn the choice to call a tool into an endogenous stochastic decision within the reasoning process itself. Under the current information state, the model estimates:
L136:  | $$p(\text{\hbox to80.5pt{\vbox to13.69pt{\pgfpicture\makeatletter\hbox{\hskip 40.25116pt\lower-4.34444pt\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} \lxSVG@begingroup@{stroke=#000000} \lxSVG@begingroup@{fill=#000000} \lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width=0.4pt} \lx@inpgf@ignorespaces\nullfont\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} {}{
L137: {{}}\lx@inpgf@ignorespaces\hbox{\hbox{{\lxSVG@begingroup@{_scopebegin=1} \lxSVG@begingroup@{stroke=#056B34} \lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width=0.8pt} \lx@inpgf@ignorespaces{{}{}{{
L138: {}{}}}{
L139: {}{}}
L140: {{}{{\lx@inpgf@ignorespaces}}}{{}{\lx@inpgf@ignorespaces}}{}{{}{\lx@inpgf@ignorespaces}}
L141: {\lxSVG@begingroup@{_scopebegin=1} \lxSVG@begingroup@{stroke=#056B34} \lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width=0.8pt} \lx@inpgf@ignorespaces{}\lxSVG@stroke\lxSVG@drawpath@unclipped{M -55.14 -5.46 h 110.28 v 17.83 h -110.28 Z}{fill:none} \lx@inpgf@ignorespaces
L142: \lxSVG@closescope }{{{{\lx@inpgf@ignorespaces}}\lxSVG@begingroup@{_scopebegin=1} \lxSVG@transformcm{1.0}{0.0}{0.0}{1.0}{-37.85117pt}{0.0pt}\lxSVG@begingroup@{transform=matrix(1.0 0.0 0.0 1.0 -52.37 0)} \pgfsys@hbox{58}\lxSVG@closescope }}}
L143: \lxSVG@closescope }}}
L144: }
L145: \lxSVG@closescope \hbox to0.0pt{}{{
L146: {}{}{}}}{\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}\hss}\lxSVG@discardpath\lxSVG@closescope \hss}}\lxSVG@closescope\endpgfpicture}}}\mid q,H,S_{k},R_{k})$$  |  | (5)
L147: and this probability directly drives whether the model generates . Once this marker appears, the system enters the tool selection and execution phase; when , are later concatenated, the system exits the tool phase and returns to pure natural language answering.
L148: This design allows tool usage to be determined by the model’s uncertainty and task requirements at the moment, rather than by inflexible hand-crafted triggers, enabling smoother adaptation to scenarios where tools are sometimes necessary and sometimes unnecessary.
L149: Based on the current query $q$, dialogue history $H$, symbolic state $S_{k}$, and reasoning trajectory $R_{k}$, we construct a tool requirement representation:
L150: 
L151:  | $$u_{k}=f(q,H,S_{k},R_{k})$$  |  | (6)
L152: which provides a structured description of the present subproblem and clarifies what the system aims to achieve and what type of tool output it expects. We then treat $u_{k}$ as a query to retrieve from the large tool set $\mathcal{T}$, using vector embeddings jointly to extract the Top-$K$ candidate tools:
L153: 
L154:  | $$\mathcal{C}_{k}=\text{TopK-Retrieve}(u_{k},\mathcal{T})$$  |  | (7)
L155: 
L156: which effectively shrinks the tool space, preserving only a small, highly relevant candidate set.
L157: With the candidate set $\mathcal{C}_{k}$, we apply a reranking model within $\mathcal{C}_{k}$, producing a refined ranking distribution:
L158: 
L159:  | $$p_{\text{rank}}(t\mid u_{k}),\quad t\in\mathcal{C}_{k}$$  |  | (8)
L160: ### 3.4 Tool Contracts on Planning
L161: 
L162: For each candidate tool $t\in\mathcal{C}_{k}$, we determine whether its precondition is satisfied under the current symbolic state $S_{k}$, using the indicator $\mathbf{1}[S_{k}\models P_{t}]$ to eliminate all tools whose prerequisites are unmet. We then renormalize the ranking distribution only over those tools whose preconditions hold, forming a logically valid execution policy:
L163:  |  | $\displaystyle p^{*}(t\mid q,H,S_{k},R_{k})=$  |  | (9)
L164:  |  | $\displaystyle\frac{p_{\text{rank}}(t\mid u_{k})\cdot\mathbf{1}[S_{k}\models P_{t}]}{\sum_{t^{\prime}\in\mathcal{C}_{k}}p_{\text{rank}}(t^{\prime}\mid u_{k})\cdot\mathbf{1}[S_{k}\models P_{t^{\prime}}]}$  |
L165: This filtering mechanism transcends simple semantic matching by establishing formal execution admissibility; it necessitates that the current state $S_{k}$ satisfies the weakest precondition of the selected tool, denoted as $S_{k}\models wp(t,P_{t})$. By embedding such deterministic constraints into the probabilistic sampling process, we ensure that the model’s trajectory remains within a logically grounded solution space rather than relying on unconstrained heuristic transitions.
L166: We treat $p^{*}(t)$ as a logically constrained policy distribution and sample from it:
L167: 
L168:  | $$t^{*}\sim p^{*}(t\mid q,H,S_{k},R_{k})$$  |  | (10)
L169: As long as a tool is both legal and meaningfully relevant, it naturally retains the chance to be explored, while its sampling probability reflects its contextual priority. Once the final tool $t^{*}$ is selected and invoked, it returns a result $r_{t}$. Before updating the system state with this output, we introduce a safety gate, a runtime contract verification process that checks whether the returned result satisfies the Hoare postcondition $Q_{t}$.
L170: We formalize this as a binary acceptance event $\mathcal{A}_{t}\in\{0,1\}$, with conditional probability $p(\mathcal{A}_{t}=1\mid S_{k},r_{t},Q_{t})$ and implement it as a concrete verification function:
L171:  | $$\mathcal{A}_{t}=\begin{cases}1,&\text{if }(S_{k},r_{t})\models Q_{t}\land\text{wf}(r_{t}),\\
L172: 0,&\text{otherwise.}\end{cases}$$  |  | (11)
L173: 
L174: Through this step, every tool output must satisfy structural validity, value range constraints, and format expectations before it can affect the global state. Only if verification passes does the symbolic state update:
L175: 
L176:  | $$S_{k+1}=\begin{cases}\mathsf{Update}_{t}(S_{k},r_{k}),&\mathcal{A}_{t}=1,\\
L177: S_{k},&\mathcal{A}_{t}=0,\end{cases}$$  |  | (12)
L178: and the accepted result is injected into the subsequent reasoning trajectory $R_{k+1}$. If verification fails, the result is discarded entirely, preventing contaminated outputs from propagating and providing a clear debugging breakpoint.
L179: 
L180: Simultaneously, we inject the verified results wrapped in and tags into the subsequent reasoning trajectory $R_{k+1}$, enabling both subsequent natural language reasoning and the next round of tool selection to fully leverage this newly acquired trusted information.
L181: Building on this foundation, we treat the entire system as a family of stochastic trajectories $\tau$, each consisting of $(S_{k},R_{k})$, the chosen tools $t_{k}$, and the acceptance events $\mathcal{A}_{k}$. The system performs probabilistic reasoning over all feasible execution trajectories, and the final output $y$ can be expressed via trajectory-level marginalization:
L182: 
L183:  | $$p(y\mid q,H)=\sum_{\tau}p\bigl(y\mid q,H,\tau\bigr)\,p\bigl(\tau\mid q,H\bigr)$$  |  | (13)
L184: where $p(\tau\mid q,H)$ integrates all components discussed above: tool trigger probability, requirement abstraction, retrieval and ranking, contract filtering, constrained sampling, and acceptance verification.
L185: 
L186: To ensure Hoare contracts regulate not only local behavior but also the global behavior space, we impose a strict trajectory-level constraint: if any trajectory $\tau$ violates any tool precondition $P_{t}$ or postcondition $Q_{t}$ at any step, then
L187: 
L188:  | $$p(\tau\mid q,H)=0$$  |  | (14)
L189: Under this formulation, reasoning and sampling proceed exclusively within a trajectory subspace that adheres to predefined contracts, thereby providing a formal logical justification for each state transition and tool execution.
L190: ## 4 Experimental Setup
L191: ### 4.1 Dataset.
L192: 
L193: We utilize ToolBench (cite64†Qin et al., 2023 ) and MCP-Universe cite87†Luo et al. (2025) as our experimental datasets. ToolBench contains more than 16,000 APIs organized into structured tool categories, covering a wide range of functional capabilities. These settings jointly assess both local tool invocation ability and global planning robustness.
L194: MCP-Universe reflects more realistic multi-tool environments. It aggregates diverse tools, plugins, and APIs from real-world systems covering information retrieval, automation, data processing, system operations, and task execution. We use the tools selected in ToolBench and MCP-Universe along with their official documentation, specifications, and usage descriptions to extract structured functional representations. More dataset details are provided in Appendix cite27†A .
L195: Table 1: Main experimental results on ToolBench and MCP-Universe. We report Pass Rate (%) and Win Rate (%) for ToolBench G1, G2, and G3 tasks, and Success Rate (%) for three MCP-Universe subtasks.
L196: Model  | Method  | ToolBench  | MCP-Universe
L197: --- | --- | --- | ---
L198: G1  | G2  | G3  | Location Navigation  | Repository Management  | Financial Analysis
L199: --- | --- | --- | --- | --- | ---
L200: Pass.  | Win.  | Pass.  | Win.  | Pass.  | Win.
L201: --- | --- | --- | --- | --- | ---
L202: Qwen-3-235B  | ReACT  | 50.5  | –  | 53.5  | –  | 46.0  | –  | 11.10  | 9.09  | 50.0
L203: DFSDT  | 57.0  | 53.8  | 61.5  | 67.5  | 48.8  | 56.8  | 11.10  | 12.12  | 50.0
L204: LATS  | 62.5  | 59.3  | 78.0  | 70.3  | 77.8  | 83.3  | 15.54  | 15.15  | 52.5
L205: ToolChain*  | 65.0  | 62.8  | 79.3  | 72.5  | 78.0  | 83.5  | 16.65  | 18.18  | 55.0
L206: Tool-Planner  | 60.3  | 58.0  | 70.5  | 68.8  | 65.5  | 72.3  | 13.32  | 12.12  | 52.5
L207: ToolGate  | 68.3  | 65.5  | 82.5  | 78.0  | 81.0  | 82.3  | 18.87  | 21.21  | 60.0
L208: Deepseek V3.2  | ReACT  | 52.0  | 48.5  | 55.3  | 51.0  | 48.5  | 53.5  | 12.21  | 12.12  | 52.5
L209: DFSDT  | 58.5  | 55.0  | 63.0  | 69.3  | 50.3  | 58.8  | 13.32  | 15.15  | 55.0
L210: LATS  | 65.3  | 61.8  | 80.0  | 72.5  | 80.3  | 85.5  | 17.76  | 18.18  | 60.0
L211: ToolChain*  | 68.8  | 65.0  | 82.5  | 75.3  | 81.0  | 88.8  | 18.87  | 21.21  | 62.5
L212: Tool-Planner  | 62.5  | 60.3  | 73.8  | 70.0  | 68.0  | 75.5  | 15.54  | 15.15  | 57.5
L213: ToolGate  | 72.0  | 70.3  | 85.5  | 80.0  | 85.3  | 81.3  | 22.20  | 24.24  | 67.5
L214: GPT-5.2  | ReACT  | 63.5  | 62.8  | 65.0  | 63.2  | 58.3  | 59.5  | 18.87  | 24.24  | 65.0
L215: DFSDT  | 70.0  | 68.5  | 75.3  | 78.0  | 63.8  | 70.5  | 19.98  | 27.27  | 67.5
L216: LATS  | 80.3  | 78.8  | 88.5  | 85.3  | 85.0  | 90.8  | 28.86  | 36.36  | 82.5
L217: ToolChain*  | 82.8  | 80.0  | 90.5  | 88.3  | 88.5  | 92.5  | 29.97  | 39.39  | 85.0
L218: Tool-Planner  | 75.5  | 72.3  | 82.0  | 80.5  | 78.3  | 85.0  | 25.53  | 30.30  | 75.0
L219: ToolGate  | 85.5  | 83.5  | 93.0  | 90.5  | 91.8  | 95.3  | 35.52  | 45.45  | 90.0
L220: Gemini 3 Pro  | ReACT  | 60.0  | 60.5  | 63.8  | 57.0  | 55.5  | 56.5  | 16.65  | 21.21  | 62.5
L221: DFSDT  | 68.3  | 65.5  | 72.0  | 75.8  | 60.3  | 68.5  | 17.76  | 24.24  | 65.0
L222: LATS  | 78.5  | 75.3  | 85.8  | 82.0  | 82.5  | 88.3  | 26.64  | 33.33  | 77.5
L223: ToolChain*  | 80.0  | 78.5  | 88.3  | 85.0  | 85.8  | 90.0  | 27.75  | 36.36  | 80.0
L224: Tool-Planner  | 73.8  | 70.0  | 80.5  | 78.3  | 75.0  | 82.8  | 22.20  | 27.27  | 72.5
L225: ToolGate  | 83.0  | 80.5  | 91.3  | 88.0  | 90.0  | 93.5  | 33.30  | 42.42  | 87.5
L226: ### 4.2 Evaluation Metrics
L227: For ToolBench, we adopt two evaluation metrics from ToolEval (cite64†Qin et al., 2023 ). The first metric is Pass Rate, computed as the proportion of successfully completed tasks, which reflects overall task-solving capability. The second metric is Win Rate, where we compare the execution plans and results produced by our framework with those generated by Qwen-3 235B-ReACT and request LLMs judges to determine which solution is superior.
L228: If our method yields a better solution, we mark it as a win; if it is equivalent or worse, we mark it as a tie or loss. Win Rate therefore measures both reasoning quality and execution superiority.
L229: For MCP-Universe, we evaluate Success Rate and execution stability. Many tasks in MCP-Universe involve relatively fewer tool invocation steps but arise from real-world complex systems.
L230: ### 4.3 Baselines
L231: 
L232: We compare our framework against the following representative tool-use and planning baselines: ReACT (cite53†Yao et al., 2022 ), DFSDT (cite64†Qin et al., 2023 ), LATS cite88†Zhou et al. (2024) , ToolChain* (cite89†Zhuang et al., 2024 ), Tool-Planner (cite90†Liu et al., 2025c ), More baselise details are provided in Appendix cite30†B .
L233: ### 4.4 Models
L234: We evaluate our framework across a range of large language models to verify generality and robustness. Proprietary models include Gemini 3 Pro cite91†Google Inc. (2025) , GPT-5.2 cite92†OpenAI (2025) . Open-source models include DeepSeek V3.2 cite93†Liu et al. (2025a) , Qwen3-235B-A22B-Instruct-2507 cite94†Yang et al. (2025) . These models cover heterogeneous training paradigms, reasoning capabilities, and scales. While we use Qwen3-embedding-0.6B and Qwen3-Reranker-0.6B cite95†Zhang et al.
L235: (2025b) for tool embedding and retrieval.
L236: ## 5 Experiments
L237: ### 5.1 Main Results
L238: 
L239: As shown in Table cite96†1 , we conduct comprehensive evaluations on ToolBench (G1/G2/G3) and MCP-Universe.
L240: For ToolBench. The results show that ToolGate achieves the best or near-best performance across all models and all evaluation benchmarks. On ToolBench, ToolGate leads to substantial improvements in both Pass Rate and Win Rate across all three task groups. For instance, under GPT-5.2, ToolGate reaches 85.5 / 83.5, 93.0 / 90.5, and 91.8 / 95.3 on G1/G2/G3 respectively, outperforming the strongest baseline ToolChain* by approximately $4-6\%$ in Win Rate.
L241: Similar improvements are consistently observed on Qwen-3-235B, DeepSeek V3.2, and Gemini 3 Pro, demonstrating that ToolGate is model-agnostic and provides stable enhancement to tool reasoning and execution capabilities across different LLM backbones.
L242: Table 2: Comprehensive ablation study of the Hoare logic verification module. We compare the full ToolGate architecture against variants: No $\{P\}$ check (skips pre-condition validation) and No $\{Q\}$ check (skips post-condition assertion). MCP-Avg represents the mean success rate of MCP subtasks.
L243: Model  | Method  | ToolBench  | MCP-Universe
L244: G1  | G2  | G3  | Loc.  | Repo.  | Fin.  | MCP-Avg
L245: Pass.  | Win.  | Pass.  | Win.  | Pass.  | Win.
L246: DeepSeek V3.2  | ReACT  | 52.0  | 48.5  | 55.3  | 51.0  | 48.5  | 53.5  | 12.2  | 12.1  | 52.5  | 25.6
L247: DFSDT  | 58.5  | 55.0  | 63.0  | 69.3  | 50.3  | 58.8  | 13.3  | 15.2  | 55.0  | 27.8
L248: ToolChain*  | 68.8  | 65.0  | 82.5  | 75.3  | 81.0  | 88.8  | 18.9  | 21.2  | 62.5  | 34.2
L249: ToolGate w/o Hoare  | 57.2  | 53.8  | 61.5  | 67.5  | 49.8  | 57.5  | 12.8  | 14.5  | 54.2  | 27.2
L250: – No $\{P\}$ check  | 67.8  | 66.5  | 79.5  | 77.2  | 78.4  | 82.8  | 19.8  | 21.5  | 62.2  | 34.5
L251: – No $\{Q\}$ check  | 63.2  | 61.0  | 71.5  | 72.8  | 70.8  | 73.5  | 16.2  | 18.2  | 58.2  | 30.9
L252: ToolGate (Full)  | 72.0  | 70.3  | 85.5  | 80.0  | 85.3  | 81.3  | 22.2  | 24.2  | 67.5  | 38.0
L253: GPT-5.2  | ReACT  | 63.5  | 62.8  | 65.0  | 63.2  | 58.3  | 59.5  | 18.9  | 24.2  | 65.0  | 36.0

