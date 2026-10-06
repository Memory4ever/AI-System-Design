Proactive Hardening of LLM Defenses with HASTE (https://arxiv.org/html/2601.19051v1)
citeturn28098view0 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19051v1","pattern":"IV"}); Total lines: 469
L29:     5. cite19†III-E Data Preparation L30:     6. cite20†III-F Training and Benchmarking L31:   5. cite21†IV Experiment Methodology L32:     1. cite22†IV-A Experimental Design and Configurations L33:       1. cite23†Metrics L34:     2. cite24†IV-B Pipeline Configuration L35:       1. cite25†Collection L36:       2. cite26†Generation L37:       3. cite27†Evaluation L38:       4. cite28†Refinement L39:       5. cite29†Data Preparation L40:       6. cite30†Training and Benchmarking L41:   6. cite31†V Results L42:     1. cite32†V-A Impact of Fuzzing L43:     2. cite33†V-B Impacts of Hard-Negative Sampling L141: Experiment configurations are defined in Section cite22†IV-A . The remaining seed set is continuously augmented with hard positives, hard negatives, and/or fuzzed samples, as dictated by the parameters of the particular experiment configuration for the HASTE pipeline iterations.
L142: 
L143: Figure cite75†3 illustrates the data ingestion and augmentation process within the Collection stage.
L209: ## IV Experiment Methodology
L210: 
L211: The HASTE framework is capable of supporting a wide range of experimental directions. To understand how the parameter options in each stage influence the evasiveness and efficacy of the generated prompts, we establish baselines configurations and controlled variations (e.g., fuzzing, hard-mining, sampling strategies), to compare the evolution of performance across multiple temporal iterations.
L212: ### IV-A Experimental Design and Configurations
L213: 
L214: Each configuration represents the combination of key settings within the temporal loop of iteration. The tested parameters compose the columns of Table cite89†I , and shorthand experiment names define the rows. The naming convention and purpose of these configurations are discussed below:
L215: 
L216:   * •
L241: ##### Metrics
L242: 
L243: We record (i) iteration accuracy, measuring how well the detector generalizes to new prompts before retraining; (ii) temporal accuracy, capturing improvement after retraining on accumulated samples to quantify adversarial strength over time.
L244: 
L245: ### IV-B Pipeline Configuration
L246: 
L247: Our experimental pipeline comprises six key stages: Collection, Generation, Evaluation, Refinement and finally Training and Benchmarking.
L290: We evaluate the HASTE process with the experiment parameter configurations documented in Table cite89†I and described in Section cite21†IV . Experiments are evaluated to assess two functional goals: the effectiveness of generating evasive malicious prompts and two, improving the robustness of the defensive classifier retrained with the synthetic malicious prompts.
L359: Table cite98†IV summarizes HASTE-Optimized detection model accuracy, after fine-tuning with the corresponding HASTE parameter configuration, (referred to herein as “H accuracy”. The baseline model (Base) exhibits limited improvement at the M5 stage, but at M10, becomes on par with the gains with hard-negative mining, effectively eliminating the need for half the training cycles and accelerating convergence by 50%.
L362: The comparable final accuracies between semantic-fuzzing (Base+Sem) and the hard-mining (HM) configurations should be contextualized. Although both approaches ultimately achieve roughly the same accuracy of ~93% accuracy (Table cite98†IV ), the quality of the adversarial training signal differs significantly. As shown in Table cite97†III , Base+Sem reduces the baseline detector’s accuracy to only 66.16%, whereas the HM-Max discovers substantially more evasive prompts, driving the accuracy down to 31.76%.
L366: TABLE IV: H accuracy results for the baseline model (M0), re-trained model at iteration 5 (M5) and re-trained model at iteration 10 (M10). Each row represents different configurations of HASTE sample generation strategies, as measured on the out-of-loop evaluation dataset.
L367: Experiment  | M0  | M5  | M10
L368: --- | --- | --- | ---
L369: Base  | 82.12  | 81.06  | 92.80
L370: Base+All  | 82.12  | 92.22  | 93.13
L371: Base+Sem  | 82.12  | 93.94  | 94.14
L372: HM-Bal  | 82.12  | 92.82  | 93.74
L373: HM-Bal+All  | 82.12  | 93.74  | 94.44
L439:   * [21] ProtectAI.com (2023) Deberta-v3-base-prompt-injection: Fine-Tuned DeBERTa-v3 for Prompt Injection Detection. Note: https://huggingface.co/ProtectAI/deberta-v3-base-prompt-injection Model hosted on Hugging Face, Apache 2.0 license Cited by: cite136†§II-C1 , cite137†§IV-B .
--------------------------------------------------------------------------------
Privacy-Preserving Model Transcription with Differentially Private Synthetic Distillation (https://arxiv.org/html/2601.19090v1)
citeturn28098view1 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19090v1","pattern":"Experiments"}); Total lines: 646
L178: Different from the approaches that also use synthetic data for distillation [cite64†30 , cite65†31 ], our unified framework provides switchable data-sensitive or label-sensitive privacy protection and an end-to-end competitive-cooperative learning by top-$k$ dimensionality reduction as well as taking the student prediction as prior into the differentially private annotation, which facilitates knowledge transfer and learning efficiency, e.g., only 33 minutes with 20 iterations to transcribe a ResNet34 into a three-layer CNN using three GeForce RTX 3090 GPUs.
L179: ## IV Experiments
L180: To verify the effectiveness of our DPSD approach, we conduct experiments on 8 datasets and comparisons with 26 state-of-the-arts. These baselines consist of three categories, including 17 data-sensitive privacy protection approaches, 4 label-sensitive privacy protection approaches and 5 approaches under federated learning setup.
L181: Among them, most approaches involve original private data in their learning, and we keep their settings for the comparisons, while our DPSD uses synthetic data generated by the trainable generator in the learning. We evaluate the test accuracy of all models under different privacy, e.g., transcribing pretrained models into their privacy-preserving counterparts and then evaluating their performance.
L182: To make the comparisons fair, our experiments use the same settings as these baselines and take the results from their original papers or by executing the official source codes.
--------------------------------------------------------------------------------
In-Network Collective Operations: Game Changer or Challenge for AI Workloads? (https://arxiv.org/html/2601.19132v1)
citeturn28098view2 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19132v1","pattern":"Obstacles"}); Total lines: 245
L100: The advantages of In-Network Computation (INC) are both evident and substantial, with potential traffic reductions at both edge links and in the core network of up to $2\times$ for operations such as Allreduce, Reduce_scatter, Broadcast, and Allgather. Additionally, INC can significantly reduce host memory load and provide opportunities for overlapping computation and communication during collective operations [cite27†10 ]. However, the intricacies of INC can be complex and challenging to navigate.
L101: In the following sections, we present several obstacles that architects and engineers developing INC systems must consider.
L102: ### Low Precision Data Types
L103: One of the most effective optimizations in deep learning and AI is the utilization of low-precision data types. Reducing the number of bits used to represent numerical values not only linearly decreases data volume and movement but can also lead to a quadratic increase in computational performance. Specifically, reducing values from $16$-bit to $8$-bit precision results in a $2\times$ savings in memory and memory bandwidth, as well as a potential $4\times$ speedup in computations.
--------------------------------------------------------------------------------
MATA: A Trainable Hierarchical Automaton System for Multi-Agent Visual Reasoning (https://arxiv.org/html/2601.19204v1)
citeturn28098view3 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19204v1","pattern":"transition"}); Total lines: 499
L67: To supervise the hyper agent’s transition policy, we build transition-trajectory trees and transform to memory-to-next-state pairs, forming the MATA-SFT-90K dataset for supervised finetuning (SFT). The finetuned LLM as the transition policy understands the query and the capacity of agents, and it can efficiently choose the optimal agent to solve the task. Across multiple visual reasoning benchmarks, MATA achieves the state-of-the-art results compared with monolithic and compositional baselines.
L78: Motivated by the requirements above, we cast this decision problem as a finite-state automaton where the transition function picks a discrete next state and the lifecycle is naturally expressed by explicit states and transitions. This provides explainability, verifiable control flow, and modularity that yield greater versatility, reliability, and performance.
L80: Designing rules to select among functionally overlapping (competitive) agents is hard since the criteria are ambiguous and task-dependent, and human priors about which agents fit which tasks and queries are uncertain. We therefore design a trainable hyper agent to learn a transition policy that selects the next state. Notably, not every transition needs learning: within an agent, micro-steps (e.g., LLM/VLM prompting, verifier checks, tool I/O) follow clear procedures that are easy to define.
L81: As the number of agents grows, the main difficulty is cross-agent transition rather than agent’s inside control. This motivates a hierarchical automaton in which each top-level state is an agent with a small rule-based sub-automaton, and a trainable hyper agent provides the transition function that observes the shared memory and selects the next agent. All agents read and write to a shared memory that records variables, tool outputs, code history, and verifier feedback, recording an explainable process.
L82: This replaces an inflexible rule-based transition policy with a data-driven, error-aware, and dynamic policy that can redirect to alternative solutions when needed. This design focuses on learning the ambiguous selection between competitive agents, while preserving reliable execution inside agents.
L83: We introduce these ideas in MATA (Multi-Agent hierarchical Trainable Automaton), a hierarchical automaton for visual reasoning. MATA contains a specialized agent for fast, System 1-style perception (e.g., object detection, simple question answers); a slow, System 2-style step-wise reasoner that generates and executes Python programs for multi-step inference; and a one-shot workflow reasoner that solves queries without iteration.
L84: To supervise the hyper agent, we need labeled transition decisions. We therefore run the system for each image-query pair, expand a transition trajectory tree (cite79†Kearns et al., 2002 ) and log the state history, prompts, intermediate artifacts (detections, captions, code), feedback, and performance results. The leaves are scored by the appropriate task performance, and each decision is labeled with the child that leads to the highest-scoring subtree.
L85: This generates memory-to-next-state pairs (MATA-SFT-90K) for LLM supervised finetuning (SFT), as shown in cite80†Figure 1 (c).
L86: The contributions of our paper are:
L87: 
L88:   * •
L89: 
L90: A hierarchical deterministic finite-state automaton-based system, MATA, that unifies neuro-symbolic framework with collaborative and competitive multi-agent design for visual reasoning.
L91: 
L92:   * •
L93: Proposing (i) a learnable mechanism that trains a hyper agent as the transition policy of the hyper automaton over collaborative and competitive agents; (ii) a transition-trajectory data generation pipeline and the dataset, MATA-SFT-90K, for supervised finetuning (SFT) of the hyper agent.
L94: 
L95:   * •
L96: 
L97: Comprehensive experiments across visual-reasoning benchmarks, with extensive ablations and analysis.
L98: ## 2 Related Works
L99: Monolithic vision-language models (VLM) map images and text directly to answers with a single forward pass (cite64†Xiao et al., 2024 ; cite63†Liu et al., 2023b ; cite81†Li et al., 2023a ; cite82†Li et al., 2023b ; cite83†Wu et al., 2023 ; cite84†Stanić et al., 2024 ; cite85†Zhu et al., 2023 ).
L100: While these models have strong perceptual capabilities, their implicit reasoning processes are hard to explain and often degrade on queries requiring spatial relations, counting, or multi-step reasoning (cite86†Jahangard et al., 2024 ; cite87†Jahangard et al., 2025 ). This motivates modular designs that expose intermediate, explainable symbolic processes (cite88†Andreas et al., 2016 ; cite89†Hsu et al., 2023 ).
L101: Compositional methods decompose a task into multiple stages (cite51†Ke et al., 2025b ), often by having an LLM generate grounded actions (e.g., programs or JSON) executed by tools (cite90†Gupta & Kembhavi, 2023 ; cite55†Surís et al., 2023 ; cite91†Shen et al., 2023 ; cite66†Lu et al., 2023 ). These pipelines improve interpretability and enable external tools use, but usually operate in a single forward pass with a fixed manually designed pipeline.
L104: In broader domains, multi-agent frameworks assign disjoint roles and connect them with hand-crafted collaboration patterns (cite70†Hong et al., 2023 ; cite71†Li et al., 2024 ; cite72†Nguyen et al., 2025 ; cite73†Zhang et al., 2025 ), achieving better performance in reasoning. However, this idea is still under-explored for visual reasoning.
L105: Notably, noise from perception and LLM/VLM hallucinations can accumulate across steps (cite74†Ke et al., 2025a ) from the collaborating pipelines, and most designs overlook competition between functionally overlapping agents (cite69†Wang et al., 2025c ). This lack of a learned transition policy limits flexibility and robustness on complex and diverse queries.
L106: Finite-state automata as abstractions provide explicit control flow and interpretability. NAVER introduces probabilistic logic inside an automaton and equips modules with self-correction (cite58†Cai et al., 2025 ), but relies on a hand-crafted transition policy that is hard to manually define as states grow. HYDRA introduces an agent that includes a planner, an RL controller, and a code-executing reasoner (cite57†Ke et al., 2024 ).
L107: While data-driven, it still focuses on instruction-level planning without a learned, high-level policy for switching across qualitatively different agents on demand. By contrast, we propose MATA that explicitly learns the inter-agent transition function over a hyper-automaton whose states are agents, while keeping intra-agent micro-steps rule-based.
L108: This learned transition function enables collaboration and competition among overlapping experts and transfers across different domains and tasks (cite27†subsection 4.2 ), which previous visual reasoning methods with hand-written transitions or single-agent controllers do not address. States are agents; each agent runs a small, rule-based sub-automaton for reliable micro-control, while a trainable hyper agent learns cross-agent transitions over a shared memory.
L109: This hierarchical view retains the interpretability of explicit state machines, avoids hand-coded transitions, and supports both collaboration and competition. Unlike prior work (cite57†Ke et al., 2024 ; cite58†Cai et al., 2025 ), our controller is supervised-trained from transition-trajectory data to transit between agents and to report a final result only when it is certain of the answer, directly addressing the gap identified above.
L110: cite92†Image: Refer to caption Figure 2: Pipeline of MATA. A trainable hyper agent reads a snapshot of the shared memory, predicts the next state with an LLM State Controller. Its decision (blue arrows) routes control among agent states in the hyper automaton: Oneshot Reasoner, Stepwise Reasoner, and Specialized Agent. Each agent runs a rule-based sub-automaton that iterates until return to the hyper automaton.
L111: All agents read/write an append-only Shared Memory, enabling the hyper agent to access the current context for choosing the optimal next state. Lifecycle states Initial and Failure are shown outside the agents (see cite10†subsection 3.2 for details).
L112: ## 3 Methodology
L113: 
L114: We explore multi-agent visual reasoning by learning a high-level transition function over agents within a hierarchical automaton, enabling data-driven collaboration and competition among overlapping skills and replacing inflexible hand-written pipelines.
L115: ### 3.1 Overview
L116: A visual reasoning instance is an image-query pair $(v,q)$ mapped to an output $y$ (cite51†Ke et al., 2025b ). MATA organizes inference as a hierarchical automaton operated by a trainable hyper-agent. Informally, the hyper automaton $\mathcal{M}_{\theta}$ is a top-level automaton whose states include a set of sub-agents, with each sub-agent running a small rule-based sub-automaton, and the trainable hyper agent controlling the learned transition $\delta_{\theta}$.
L117: Formally, it can be described as a Mealy machine (cite93†Mealy, 1955 ): $\mathcal{M}_{\theta}=(S,S_{0},\Sigma,\Lambda,\delta_{\theta},\Gamma)$ where $S$ denotes the set of states (containing both agent states for task execution and lifecycle states for process coordination), $S_{0}$ the initial state where reasoning begins, $\Sigma$ the inputs drawn from shared-memory snapshots (storing intermediate results from agents), $\Lambda$ the answer space of visual reasoning queries (e.g., discrete labels, bounding box coordinates, or free-text responses), $\delta_{\theta}$ the learned transition function that determines the next state based on the current state and memory inputs, and $\Gamma$ the output function that generates the final answer $\hat{y}$ once the automaton reaches a terminal state.
L118: Detailed breakdowns of the states, transition mechanics, and output generation process are provided in the subsequent sections (cite94†Figure 2 ).
L119: ### 3.2 Hyper Automaton
L120: ##### States.
L121: The finite state set is the union of agent states and lifecycle states: $S=S_{\text{agent}}\cup S_{\text{life}}$, where $S_{\text{agent}}=\{\textsc{Oneshot},\textsc{Stepwise},\textsc{Specialized}\}$, $S_{\text{life}}=\{\textsc{Initial},\textsc{Final},\textsc{Failure}\}$ and the initial state $S_{0}=\textsc{Initial}$.
L122: Agent states invoke concrete skills; lifecycle states orchestrate the progression and termination of the reasoning episode (e.g., starting the task, handling uncertainty, concluding with an answer). Details of the states are shown in cite95†Table 1 .
L123: Table 1: States of the hyper automaton. The table specifies the description and the triggering condition for each state. $\delta_{\theta}$: transition function of hyper automaton.
L124: State  | Description  | Selected by
L125: --- | --- | ---
L126: Initial  | The unique state where reasoning begins.  | Initial state
L127: --- | --- | ---
L128: Oneshot  | A workflow agent that executes a single-pass program generation and execution workflow for solvable queries, equipped with a lightweight verifier.  | $\delta_{\theta}$
L129: Stepwise  | A stepwise reasoner that produces step-wise Python programs for complex queries; code is verified and executed in a sandboxed environment to ensure correctness.  |
L130: Specialized  | An expert agent that performs fast perception tasks; built-in verifiers validate outputs and adapt parameters.  |
L131: Final  | A terminal state in which sufficient evidence has accumulated; the output function $\Gamma$ is invoked when in this state to produce the final answer $\hat{y}$.  |
L132: Failure  | A state triggered by unrecoverable errors or exceeding iteration limit.  | Error occurs
L133: Agents in our system are intentionally both collaborative and competitive. When control transitions from one agent to another, the successor agent reads the shared memory containing the prior history and feedback, and builds on that context; this is collaboration. At the same time, multiple agents may attempt the same task; if one agent stalls or fails, another can take over and complete it; this is competition.
L134: The learned transition policy $\delta_{\theta}$ selects among them based on context (e.g., Oneshot vs. Stepwise for moderately compositional VQA; Specialized vs. Oneshot for grounding with simple perception). This overlap is intentional, as the three agents represent a spectrum: perception (system 1), one-shot reasoning (fast thinking), and stepwise reasoning (slow thinking).
L135: Although all agents can answer all queries, each agent has different advantages and disadvantages, enabling hyper agent to choose the optimal transition and re-route on failure. The implementation details of agents are shown in the supplementary material (cite34†Appendix B ).
L136: ##### Shared Memory.
L137: 
L138: All agents read from and write to a structured shared memory $m_{t}$ at the $t$-th step that accumulates intermediate variables, perception results, program history, verifier feedback, and task metadata. We keep the formalism minimal: when an agent runs for one cycle, it appends its new memory $\Delta m_{t}$, and $m_{t+1}=m_{t}\cup\Delta m_{t}$. Memory is append-only so the full reasoning process is auditable and visible to the hyper agent.
L139: ##### Execution Step.
L140: 
L141: At step $t$ the system is in $(s_{t},m_{t})$. The hyper-agent observes the memory $m_{t}$ and selects the next state $s_{t+1}$ via the learned transition function $\delta_{\theta}$:
L142: 
L143:  | $$s_{t+1}=\delta_{\theta}(s_{t},m_{t}),\ \ \ s_{t+1}\in S.$$  |  | (1)
L144: If $s_{t+1}\in S_{\mathrm{agent}}$, the corresponding agent executes its rule-based sub-automaton until returning to the hyper automaton and updating the memory; if $s_{t+1}=\textsc{Final}$ or $t>T$ where $T$ is the max step limit, the episode terminates.
L145: ##### Output.
L146: 
L147: The answer space $\Lambda$ contains the required output $\hat{y}$ for visual reasoning. For example, $\Lambda=\{y\mid y\text{ is text for VQA, bounding box for VG, etc}\}$. The output function $\Gamma$ extracts the output from the memory $m_{t}$ at Final state: $\hat{y}=\Gamma(\textsc{Final},m_{t})$.
L148: ### 3.3 Trainable Transition Function (Hyper Agent)
L149: 
L150: The transition function $\delta_{\theta}$ in cite96†Equation 1 is implemented by a trainable LLM-based hyper agent $\mathcal{F}_{\theta}$. This agent acts as the state-transition controller, selecting the next state $s_{t+1}$ from a limited set of available candidate states. Since the LLM requires textual input, we derive a prompt $x_{t}$ from the shared memory $m_{t}$. The template for constructing $x_{t}$ from $m_{t}$ is shown below:
L151: Our hyper agent $\mathcal{F}_{\theta}$ maps the prompt $x_{t}$ to a distribution over the available states, from which $s_{t+1}$ is selected, either through greedy decoding or stochastic sampling.
L152: The parameter $\theta$ of the hyper agent is supervised finetuned (SFT) on our collected transition trajectory dataset $\mathcal{D}$ (cite16†subsection 3.4 ). Each training example provides a textual memory $x_{t}$ as prompt and a target next state chosen by scanning branches in the trajectory tree that lead to successful and higher final scores:
L153: 
L154:  | $$\theta\leftarrow\arg\min_{\theta}\mathcal{L}_{\mathrm{SFT}}(\theta;\mathcal{D})$$  |  | (2)
L155: This objective guides the hyper agent on how to switch between sub-agents, and finalize the output.
L156: ### 3.4 Dataset Generation
L157: Learning the transition policy of the hyper automaton requires examples of how agent states interact during visual reasoning. We therefore build a dataset of transition trajectories. We regard the set of possible transition trajectories from an initial state as a trajectory tree $\mathcal{T}(v,q)$ (cite79†Kearns et al., 2002 ) that records, for each node: the state history, intermediate reasoning outcomes, and final metric scores, as a textual prompt $x_{t}$ based on cite15†prompt 3.1 .
L158: We collect this data by running MATA while systematically traversing each next-state option rather than committing to a single path. Unlike end-to-end LLM/VLM training, this procedure explicitly explores the space of possible agent states and yields labeled decisions for our model.
L159: Concretely, we sample images and queries from the training splits of GQA (cite97†Hudson & Manning, 2019 ), OK-VQA (cite98†Marino et al., 2019 ), and RefCOCO/RefCOCO+/RefCOCOg (cite99†Kazemzadeh et al., 2014 ) and run the hyper automaton $\mathcal{M}_{\theta}$ step-wise.
L160: Rather than limiting to a single route, we expand a bounded trajectory tree to depth $T$: at each node (state) the controller branches over the possible next states $s_{t+1}\in S$, executes the corresponding sub-automaton, and saves a memory checkpoint $m_{t+1}$. When a terminal state is reached (e.g., Final), which by construction corresponds to a leaf of the tree $\mathcal{T}$, the output function $\Gamma$ produces a prediction $\hat{y}$ for the given image-query pair $(v,q)$ with ground truth $y$.
L161: We then compute a scalar task score for that leaf: for VG we use $\mathrm{IoU}(\hat{y},y)$; for VQA we use $\mathrm{Acc}(\hat{y},y)$. During data collection we perform a near-exhaustive expansion of the transition tree to a fixed depth, which is tractable with the current three agents but, we acknowledge, grows rapidly as more agents/states are added.
L266: On popular benchmarks RefCOCO, RefCOCO+, RefCOCOg (cite99†Kazemzadeh et al., 2014 ) and Ref-Adv (cite103†Akula et al., 2020 ), MATA obtains state-of-the-art performance (cite121†Table 4 ). It sets a new state-of-the-art on these datasets, exceeding strong monolithic and compositional baselines. Notably, Ref-Adv only contains a test set, which means the MATA-SFT-90K does not contain the data collected from it, showing promising domain-transfer generalizability of MATA.
L267: Note that due to learned transition, short simple queries are solved by Specialized perception with verification, while complex cases trigger Stepwise and Oneshot reasoning. Domain-specific SFT is slightly stronger because the language query styles is dataset-specific.
L268: Table 5: Ablation of hyper agent. In this table, we report the accuracy for all VQA and referring expression comprehension benchmarks, and the inference time per query (tested on GQA). HA: Hyper Automaton. Transition: Transition policy ($\delta_{\theta}$). SFT: Supervised finetuning. Refer to cite25†subsection 4.2 for details.
L269: Components  | Accuracy ($\uparrow$)  | Time ($\downarrow$)
L270: --- | --- | ---
L271: HA  | Transition  | SFT  | GQA  | OK-VQA  | RefCOCO  | RefCOCO+  | RefCOCOg  | Ref-Adv  | Avg Sec.
L272: --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
L273: ✗  | Exhaustive  | ✗  | 57.7  | 71.5  | 87.7  | 85.6  | 81.7  | 73.1  | 34.58
L274: ✓  | Random  | ✗  | 57.1  | 71.1  | 85.3  | 83.8  | 81.1  | 73.2  | 6.91
L275: ✓  | LLM  | ✗  | 58.5  | 75.1  | 95.8  | 93.5  | 88.0  | 76.0  | 8.07
L276: ✓  | LLM  | ✓  | 64.9  | 76.5  | 96.3  | 93.9  | 90.8  | 77.3  | 8.01
L277: Table 6: Generalizability results. The top-left header cell uses a diagonal split to indicate Training Data (rows, $\downarrow$) versus Test Data (columns, $\rightarrow$). Diagonal values (domain-specific) train and test on the same dataset; off-diagonal values evaluate cross-domain/task transfer (domain-transfer) . The last row reports joint training on the whole MATA-SFT-90K dataset (general) .
L278: Off-diagonal values are close to the diagonal ones, indicating strong generalizability of the learned transition policy.
L279:  | VQA  | Visual Grounding
L280:  | GQA  | OK-VQA  | RefCOCO  | RefCOCO+  | RefCOCOg  | Ref-Adv
L281: GQA  | 64.7  | 75.8  | 96.1  | 93.7  | 90.4  | 77.0
L282: OK-VQA  | 64.1  | 76.5  | 96.2  | 93.8  | 90.5  | 76.9
L283: RefCOCO  | 63.8  | 75.5  | 96.3  | 93.9  | 90.8  | 77.2
L284: RefCOCO+  | 63.6  | 75.4  | 96.2  | 93.9  | 90.7  | 77.1
L285: RefCOCOg  | 63.1  | 75.4  | 96.1  | 93.7  | 90.8  | 77.2
L286: All  | 64.9  | 76.0  | 96.3  | 93.8  | 90.7  | 77.3
L287: Figure 3: Results of different LLM sizes. Accuracy versus the model size (in billions of parameters) of the hyper agent’s LLM state controller. Left: GQA; right: OK-VQA. X-axis: LLM size; Y-axis: accuracy.
L288: 
L289: Figure 4: Results of different numbers of sub-agents. X-axis: number of sub-agents; Y-axis: accuracy in GQA.
L290: ### 4.2 Ablation Studies
L291: ##### Hyper Agent.
L292: cite122†Table 5 isolates the main contribution of the trainable hyper agent and the hierarchical automaton design. We compare: (1) Exhaustive Ensemble without hierarchical automaton (HA): exhaustively call all sub-agents and aggregate with a VLM; (2) Random Transition: HA enabled but the next state is chosen randomly; (3) LLM without SFT: a pretrained LLM is used as the state controller (no supervised finetuning); (4) LLM + SFT: a supervised finetuned LLM controls transitions.
L293: Both the exhaustive baseline and random transition yield the weakest performance, but introducing the hyper automaton already cuts runtime significantly. Replacing random with a pretrained LLM in hyper agent improves accuracy across tasks. This suggests that (i) the hyper automaton and the LLM primarily drive effective multi-agent collaboration and competition and (ii) SFT further helps the understanding of the capacity of agents in different types of questions.
L294: ##### Generalizability.
L295: We conduct generalization analysis by training the hyper agent on GQA subset only of MATA-SFT-90K dataset, OK-VQA subset only, or the whole dataset. cite123†Table 6 organizes results by different training/evaluation types: domain-specific, domain-transfer, and general. domain-transfer performance is strong in both directions (GQA$\to$OK-VQA; OK-VQA$\to$GQA) with less than 1% difference.
L296: The model trained on all data reaches similar performance to the model trained on the corresponding subset only, indicating the controller learns a task-agnostic transition policy with minimal negative impact. We further discuss the effects in the next paragraph.
L297: ##### LLM Size.
L298: cite124†Figure 4 compares the sizes of the LLM state controller from 0.6B to 8B under three settings: (i) no SFT, (ii) domain-specific SFT, and (iii) SFT on all. With domain-specific SFT, even small models (0.6B/1.7B) perform competitively matching 4B and 8B. When finetuned jointly on all data, small models are worse than 4B/8B by a few percentage points, indicating limited capacity to absorb cross-task knowledge. Without SFT, accuracy drops sharply for smaller models and improves mainly with size.
L307: We present MATA, a visual reasoning method that uses a trainable hyper agent to learn the transition policy of a hierarchical finite-state automaton. By transitioning between agents based on a shared memory, the system reduces hallucinations, and preserves explainability through explicit states and context. To supervise the hyper agent, we introduced the transition-trajectory dataset MATA-SFT-90K, which converts the trajectory data into a standard SFT format and adapts as agents are added.
L308: From experiments, MATA achieves state-of-the-art performance across multiple datasets. Limitations. The data generation pipeline performs a near-exhaustive transition search over the state space; this is tractable with the current three agents but may become costly as the number of states grows.
L417: Off-domain accuracies are close to the domain-specific ones, indicating that the learned transition policy generalizes across tasks.

