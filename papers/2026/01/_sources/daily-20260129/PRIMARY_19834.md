# Exact-v1 necessary primary — 2601.19834

Preserved original tool responses; repeated returned context is not a claim of full-appendix review.

## jan29_stdvisionhead

Visual Generation Unlocks Human-Like Reasoning through Multimodal World Models (https://arxiv.org/html/2601.19834v1)
citeturn28473view2 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19834v1","lineno":null}); Total lines: 584


## jan29_stdvisionroute

Visual Generation Unlocks Human-Like Reasoning through Multimodal World Models (https://arxiv.org/html/2601.19834v1)
citeturn28474view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19834v1","pattern":"3."}); Total lines: 584
L0:   1. cite0†1 Introduction L1:   2. cite1†2 Related Work L2:   3. cite2†3 A World Model Perspective on Multimodal Reasoning L3:     1. cite3†3.1 Formulation: Multiple Observations of the World L4:     2. cite4†3.2 Atomic Capabilities of World Models L5:     3. cite5†3.3 Deliberate Reasoning with World Modeling Across Modalities L6:     4. cite6†3.4 The Visual Superiority Hypothesis L7:   4. cite7†4 Experiment Settings L8:     1. cite8†4.1 VisWorld-Eval: Task Suite for Reasoning with Visual World Modeling L81: ## 3 A World Model Perspective on Multimodal Reasoning
L82: 
L83: Inspired by the aforementioned connections between human cognition and artificial intelligence, we formalize our world-model perspective on multimodal reasoning (see Figure cite88†2 ) in this section.
L84: ### 3.1 Formulation: Multiple Observations of the World
L85: Without loss of generality, the world of a specific task can be formulated as a multi-observable Markov decision process (MOMDP) $\mathcal{M}=(\mathcal{S},\mathcal{A},p,\Phi,\mathcal{O}_{\phi},e_{\phi})$, where $\mathcal{S}$ denotes the state space, $\mathcal{A}$ the action space, $p$ the transition function, $\Phi$ the parameter space of observation functions, $\mathcal{O}_{\phi}$ the observation space, and $e_{\phi}$ the observation function.
L86: Each $s\in\mathcal{S}$ represents the underlying state of the world, which is typically hidden and not directly observable. Instead, it can be perceived through different instantiations of observations (hereafter also referred to as views) [cite89†27 ], given by $o=e_{\phi}(s)\in\mathcal{O}_{\phi}$, parameterized by $\phi\in\Phi$.
L87: As illustrated in Figure cite88†2 a, such views can span multiple modalities—for example, visual observations corresponding to different camera poses, or verbal descriptions expressed with different emphases or styles. When an action $a\in\mathcal{A}$ is applied to the current state, the world transits according to the dynamics $s^{\prime}\sim p(s^{\prime}|s,a)$ and yields new observations.
L88: ### 3.2 Atomic Capabilities of World Models
L89: cite90†Image: Refer to caption Figure 2: Theoretical formulation of the world model perspective on multimodal reasoning. (a) Observations of the same underlying world state can span multiple modalities, including verbal and visual observations, each reflecting different views or emphases.
L90: (b) Two atomic capabilities of world models are defined: world reconstruction, which infers complete structure from partial observations and enables novel view synthesis, and world simulation, which models dynamics to predict future observations. (c) Chain-of-thought reasoning includes internal world modeling, by explicitly maintaining an evolving sequence of observations, generated through either of the atomic world model capabilities.
L98: The second capability is world simulation. Humans can mentally simulate how the world evolves into the future, supporting reasoning and decision-making, either purely in their minds or with external aids such as a scratchpad. Formally, this corresponds to the prediction component of a world model, which predicts the transition of the current state and action: $\hat{s}^{\prime}\sim\operatorname{pred}(\hat{s},a)$, providing an internal "experience" of interacting with the world.
L99: Similarly, for modern generative models, this capability is more typically realized through predictions of future observations:
L100:  | $\displaystyle p_{\theta}(o_{t+1}\mid o_{\leq t},a_{\leq t}).$  |  | (2)
L101: 
L102: In our new evaluation suite, we deliberately curate tasks that specifically demand each capability, allowing us to independently validate its contribution to multimodal reasoning (see Section cite8†4.1 ).
L103: ### 3.3 Deliberate Reasoning with World Modeling Across Modalities
L104: We then formalize how world-modeling capabilities within multimodal models contribute to reasoning. Given a question $Q$ and input images $I$, the chain-of-thought reasoning process of a multimodal AI system can be expressed as a sequence of intermediate steps (or thoughts) $R=\tau_{1},\tau_{2},\dots,\tau_{H}$, followed by the answer $A$.
L105: Although this general formulation treats each reasoning step $\tau_{i}$ as an unconstrained, free-form operation, our world model perspective suggests that humans reason by prediction and planning, and each step inherently manipulates the underlying world observations of the problem [cite75†59 , cite91†10 , cite34†72 ]. We therefore refine the reasoning formulation as $\tau_{i}=(r_{i},o_{i})$ to explicitly incorporate an evolving sequence of observations:
L106:  | $\displaystyle R=\left(r_{1},o_{1}\right),\left(r_{2},o_{2}\right),\dots,\left(r_{H},o_{H}\right),$  |  | (3)
L107: where $r_{i}$^{2}^{2}2 We use $i$ to index reasoning steps in order to distinguish them from the true time step $t$ of the underlying MOMDP. The twos are not generally aligned, as we may include branching and backtracking in the reasoning. denotes a logical reasoning step based on the accumulated context, typically expressed in text, and $o_{i}$ denotes the observation generated at that step.
L108: Specifically, the input images serve as the initial observation $o_{0}=I$, and subsequent observations are generated from previous reasoning and observations, by invoking atomic world modeling capabilities: world reconstruction (Eq. (cite92†1 )) and world simulation (Eq. (cite93†2 )), where reasoning steps imply actions $a$ and view transformations $\phi$, as illustrated in Figure cite88†2 c.
L109: This formulation is modality-agnostic, allowing observations—and thus world modeling—to arise across various modalities. We focus specifically on verbal and visual observations, motivated by dual-coding theory in human cognition and by the fact that UMMs are equipped to generate both. This yields several concrete CoT instantiations.
L110: Specifically, verbal world modeling produces purely verbal CoTs, with $o_{i}$ as verbal descriptions, whereas visual world modeling produces verbal-visual interleaved CoTs, with $o_{i}$ as generated images. In addition, prior work has discovered that language models can implicitly learn world models with emergent internal representations of board-game states without explicit supervision [cite94†37 ].
L111: Motivated by this, we also consider implicit world modeling, in which no explicit observation is generated ($o_{i}=\emptyset$)^{3}^{3}3 In practice, strictly distinguishing implicit from verbal world modeling can be difficult, because there are often partial descriptions of the current state in the reasoning part $r_{i}$. In this work, we treat verbal world modeling as explicitly expressing world states or observations in text, such as coordinates or symbolic matrices..
L112: ### 3.4 The Visual Superiority Hypothesis
L113: Contemporary LLMs and VLMs have achieved impressive performance in structured and abstract domains, such as mathematics and programming, largely driven by large-scale language-centric pre-training and verbal chain-of-thought post-training. Although these models have accumulated extensive verbal and symbolic knowledge, their understanding of the visual world remains limited when trained under purely verbal supervision.
L114: As a result, they continue to struggle with tasks grounded in basic physical and spatial intuition that even young children naturally master [cite54†49 , cite55†8 ].
L115: Visual world modeling is therefore essential for endowing multimodal AI with complementary forms of information and knowledge. (1) In terms of informativeness, while verbal and symbolic representations capture high-level semantic abstractions, they often suffer from ambiguity and representational bottlenecks. In contrast, visual observations are more concrete and information-rich, directly encoding physical properties such as motion and spatial relationships.
L168: Tracking
L169:  |
L170: Cube
L171: 3-View
L172:  |
L173: MMSI
L174: (Pos. Rel.)
L175:  | Maze  | Sokoban  |
L176: Overall
L177: (5 tasks)
L178:  |
L179: Overall
L180: (7 tasks)
L181: Proprietary Models
L182: Gemini 3 Flash  | 25.6  | 75.4  | 55.3  | 52.7  | 41.3  | 73.9  | 99.3  | 50.0  | 60.5
L183: Gemini 3 Pro  | 27.0  | 74.5  | 44.7  | 53.3  | 49.6  | 33.5  | 90.2  | 49.8  | 53.2
L184: Seed 1.8  | 10.6  | 75.2  | 24.4  | 42.5  | 38.8  | 83.9  | 68.3  | 38.3  | 49.1
L185: GPT 5.1  | 6.4  | 73.9  | 34.8  | 44.5  | 44.8  | 0.6  | 62.8  | 40.8  | 38.2
L217: ### 5.3 Visual World Modeling is Unhelpful for Certain Tasks


## jan29_stdvisioncore

Visual Generation Unlocks Human-Like Reasoning through Multimodal World Models (https://arxiv.org/html/2601.19834v1)
citeturn28475view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19834v1","lineno":125}); Total lines: 584
L115: Visual world modeling is therefore essential for endowing multimodal AI with complementary forms of information and knowledge. (1) In terms of informativeness, while verbal and symbolic representations capture high-level semantic abstractions, they often suffer from ambiguity and representational bottlenecks. In contrast, visual observations are more concrete and information-rich, directly encoding physical properties such as motion and spatial relationships.
L116: This provides precise, fine-grained grounding for reasoning about the complex real world, particularly in spatial and physical tasks. (2) In terms of prior knowledge, visual world knowledge is inherently complementary to symbolic knowledge. Humans and animals acquire much of this knowledge (e.g., physical interactions and spatial transformations) through perception, largely independent of language.
L117: Consequently, humans naturally represent and communicate such knowledge visually—for example, by sketching an approximate parabolic trajectory without performing explicit calculations. This suggests that different aspects of world knowledge are concentrated in different data modalities, and learning from large-scale generative modeling of visual data can thereby expand the effective knowledge landscape available for multimodal reasoning.
L118: We next formalize and justify these insights through theoretical analysis, with formal statements and proofs provided in Appendix cite17†7 .
L119: Informativeness. For notational convenience, we denote the question $Q$ as $r_{0}$, the input images as $o_{0}$, and the final answer as $r_{H+1}$. Prefixes of a CoT are defined as $R_{i}=(r_{0},o_{0},r_{1},o_{1},\dots,r_{i-1},o_{i-1}),\tilde{R}_{i}=(r_{0},o_{0},r_{1},o_{1},\dots,r_{i-1},o_{i-1},r_{i})$. We use $\mathbb{H}(\cdot)$ and $\mathbb{I}(\cdot;\cdot)$ to denote Shannon entropy and mutual information, respectively.
L120: We first establish that the end-to-end answer error admits an upper bound that naturally decomposes into reasoning and world-modeling errors.
L121: ###### Theorem 1.
L122: 
L123: Let $p$ denote the distribution over optimal chain-of-thoughts and answers, and let $p_{\theta}$ be a learned reasoning model. Then the following inequality holds:
L124:  | $\displaystyle\operatorname{KL}(p(A\mid Q,I)\mid\mid p_{\theta}(A\mid Q,I))$  | $\displaystyle\leq\operatorname{KL}(p(R,A\mid Q,I)\mid\mid p_{\theta}(R,A\mid Q,I))$  |
L125:  | $\displaystyle=$  | $\displaystyle\sum_{i=1}^{H+1}\underbrace{\mathbb{E}_{p}\left[\operatorname{KL}(p(r_{i}|R_{i})\mid\mid p_{\theta}(r_{i}|R_{i}))\right]}_{\textnormal{reasoning errors}}+\sum_{i=1}^{H}\underbrace{\mathbb{E}_{p}\left[\operatorname{KL}(p(o_{i}|\tilde{R}_{i})\mid\mid p_{\theta}(o_{i}|\tilde{R}_{i}))\right]}_{\textnormal{world-modeling errors}}.$  |  | (4)
L126: This decomposition reveals a fundamental trade-off between the informativeness of world models for reasoning and the fidelity of the world model itself. In the case of implicit world modeling, where $o_{i}=\emptyset$, we get rid of the world-modeling error. However, this typically comes at the cost of increased uncertainty and learning difficulty in reasoning, as all state transitions must be implicitly encoded.
L127: Empirically, world models that explicitly track the task states, serving as verbal or visual sketchpads, are generally beneficial for reasoning. We dive into the reasoning component of Eq. (cite95†4 ) to elucidate the factors underlying these benefits.
L128: ###### Theorem 2.
L129: 
L130: Let $s_{i}$ denote the latent states associated with the observations $o_{i}$. Under appropriate assumptions, the reduction in reasoning uncertainty achieved by explicit world modeling satisfies the following properties:
L131: 
L132:   1. 1.
L133: 
L134: Reasoning uncertainty does not increase: $\mathbb{H}(r_{i}|o_{0},r_{0:i-1})-\mathbb{H}(r_{i}|R_{i})=\mathbb{I}(o_{1:i-1};r_{i}|o_{0},r_{0:i-1})\geq 0.$
L135: 
L136:   2. 2.
L137: The reasoning uncertainty improvement is bounded by both (i) the information that observations provide about the underlying states and (ii) the information that the reasoning step requires about those states:
L138: 
L139:  | $$\mathbb{I}(o_{1:i-1};r_{i}|o_{0},r_{0:i-1})\leq\min\left(\mathbb{I}(o_{1:i-1};s_{1:i-1}),\mathbb{I}(r_{i};s_{0:i-1},r_{0:i-1})\right).$$  |  | (5)
L140: The uncertainty of the target distribution is closely related to sample efficiency and learning difficulty. Consequently, the upper bound on the improvement of reasoning uncertainty (Eq. (cite96†5 )) highlights another trade-off in the choice of observation modality for world modeling. The first term indicates that observations should be sufficiently informative about the underlying latent states.
L141: In contrast, the second suggests that they need only preserve the task-relevant aspects of the states required to select appropriate reasoning steps. Excessively detailed observations may be unnecessary and even detrimental, increasing world modeling errors.
L142: Prior knowledge. Although visual world models are more informative, they are intrinsically more difficult to learn from scratch due to the high dimensionality and complexity of visual observations. Fortunately, modern AI systems are typically large-scale pre-trained, which endows them with strong prior knowledge and enables faster convergence and improved generalization during downstream post-training.
L143: As discussed earlier, humans tend to represent different aspects of world knowledge through different modalities. Consequently, for a given downstream task, the distribution shift between its transition distribution and that learned during large-scale Internet pre-training can vary substantially across modalities.
L144: The generalization bound in Theorem cite97†6 of Appendix cite19†7.2 suggests that this modality-dependent distribution shift is closely related to the post-training sample efficiency of the corresponding world model. This highlights the importance of acquiring broad prior knowledge across modalities during pre-training, and of leveraging the proper modality whose priors are best aligned with the downstream task.
L145: Drawing on the above analysis, we formulate our central hypothesis regarding when and how visual generation benefits reasoning, thereby helping narrow the gap between multimodal AI and human capabilities.
L146: ## 4 Experiment Settings
L147: 
L148: Finally, we empirically validate the insights and theoretical analyses presented above through a series of controlled experiments. In this section, we describe the evaluation tasks and model training procedures.
L149: ### 4.1 VisWorld-Eval: Task Suite for Reasoning with Visual World Modeling
L150: While prior work has primarily designed evaluation tasks heuristically, we principledly evaluate multimodal reasoning across tasks designed to specific world model capabilities. Building on related benchmarks, we identify and curate a total of seven tasks, forming an evaluation suite tailored to assess reasoning with visual world modeling. All tasks are framed as question answering with concise, verifiable answers, and performance is measured by answer accuracy.
L151: We refer to this suite as VisWorld-Eval, and summarize it in Figure cite98†3 .
L152: World simulation. We consider the following tasks that primarily require simulating world dynamics over time: (1) Paper folding: Adapted from SpatialViz-Bench [cite99†61 ], this task presents a sequence of paper folds followed by hole punching, and asks for the distribution of holes after the paper is unfolded. Successfully solving this task requires simulating the unfolding process, relying on prior knowledge of symmetry and spatial transformations that is commonly grounded in visual experience.
L153: (2) Multi-hop manipulation: Build upon CLEVR [cite100†30 ], this task features a scene containing objects with various shapes and colors that undergo a sequence of operations, such as addition, removal, or color changes. The final question queries properties of the resulting layouts. Since target objects of operations are often specified via relative spatial relationships, this task places strong demands on state tracking and spatial understanding.


## jan29_stdvisioneval1

Visual Generation Unlocks Human-Like Reasoning through Multimodal World Models (https://arxiv.org/html/2601.19834v1)
citeturn28476view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19834v1","lineno":176}); Total lines: 584
L154: (3) Ball tracking: Adapted from RBench-V [cite101†20 ], this task evaluates physical dynamics simulation by requiring the model to infer the trajectory of a ball undergoing ideal specular reflections within a given scene and predicting which numbered hole it will ultimately enter. In addition, we include (4) Maze [cite102†29 ] and (5) Sokoban [cite103†55 ], as these two grid-world tasks are commonly used in prior work of studying visual generation for reasoning [cite104†67 , cite60†36 ].
L155: World reconstruction. We also evaluate tasks that emphasize reconstructing underlying world structure from partial observations: (6) Cube 3-view projection: Adapted from SpatialViz-Bench [cite99†61 ], this task provides an isometric view and two orthographic views of a connected cube stack, and asks about an unseen viewpoint.
L156: Solving the task requires reconstructing the full 3D structure and mentally rotating or projecting it into the queried view, a process closely aligned with human visual mental representations. (7) Real-world spatial reasoning: We focus on the positional relationship subset of MMSI-Bench [cite105†69 ]. Given multiple views of a realistic scene, these tasks ask about positional relationships among the cameras, objects, and regions.
L157: Successfully answering these questions requires constructing a coherent spatial mental model of the scene from limited viewpoints to support accurate spatial reasoning.
L158: For each task, we construct SFT data by designing different CoT patterns with implicit, verbal, or visual world modeling, enabling controlled comparative evaluations. Data construction pipeline and examples across tasks are presented in Appendix cite23†8.1 .
L159: cite106†Image: Refer to caption Figure 3: The VisWorld-Eval suite for assessing multimodal reasoning with visual world modeling. VisWorld-Eval comprises seven tasks spanning both synthetic and real-world domains, each designed to isolate and demand specific atomic world-model capabilities. Table 1: Zero-shot evaluation of advanced VLMs on VisWorld-Eval. We report the average accuracy over five tasks (excluding Maze and Sokoban) and over all seven tasks.
L160: Models  |
L161: Paper
L162: Folding
L163:  |
L164: Multi-Hop
L165: Manip.
L166:  |
L167: Ball
L168: Tracking
L169:  |
L170: Cube
L171: 3-View
L172:  |
L173: MMSI
L174: (Pos. Rel.)
L175:  | Maze  | Sokoban  |
L176: Overall
L177: (5 tasks)
L178:  |
L179: Overall
L180: (7 tasks)
L181: Proprietary Models
L182: Gemini 3 Flash  | 25.6  | 75.4  | 55.3  | 52.7  | 41.3  | 73.9  | 99.3  | 50.0  | 60.5
L183: Gemini 3 Pro  | 27.0  | 74.5  | 44.7  | 53.3  | 49.6  | 33.5  | 90.2  | 49.8  | 53.2
L184: Seed 1.8  | 10.6  | 75.2  | 24.4  | 42.5  | 38.8  | 83.9  | 68.3  | 38.3  | 49.1
L185: GPT 5.1  | 6.4  | 73.9  | 34.8  | 44.5  | 44.8  | 0.6  | 62.8  | 40.8  | 38.2
L186: o3  | 13.5  | 68.1  | 24.7  | 37.7  | 44.4  | 0.0  | 36.0  | 37.6  | 32.0
L187: Open-Source Models
L188: Qwen3-VL-8B-Thinking [cite107†5 ]  | 11.0  | 49.3  | 17.8  | 21.2  | 27.7  | 0.0  | 5.8  | 25.4  | 18.9
L189: BAGEL-7B-MoT [cite59†13 ]  | 11.2  | 31.6  | 19.4  | 26.8  | 27.2  | 0.0  | 0.2  | 23.2  | 16.6
L190: Evaluation of advanced VLMs. Table cite108†1 reports the zero-shot performance of advanced VLMs on VisWorld-Eval. Overall, these models perform suboptimally, highlighting limitations of current multimodal AI systems. Among them, Gemini 3 Flash and Gemini 3 Pro remarkably outperform the other models; however, their performance remains far from satisfactory on challenging tasks like paper folding, ball tracking, cube 3-view projection, and real-world spatial reasoning.
L191: ### 4.2 Unified Multimodal Model Training and Evaluation
L192: Evaluation protocol. To investigate the benefits of visual generation in multimodal reasoning, we evaluate post-trained UMMs, rather than the zero-shot performance of base models. To the best of our knowledge, no open-source model has been natively optimized for interleaved verbal-visual generation for reasoning. Even commercial closed-source models currently exhibit fundamental limitations in generating visual intermediate reasoning steps [cite62†38 , cite63†76 ].
L193: Focusing on post-trained models, therefore, provides a more meaningful estimate of the upper bound for multimodal reasoning performance, while reducing confounding effects arising from insufficient pre-training due to limited interleaved data availability or quality.
L194: Model training. We adopt BAGEL [cite59†13 ], a state-of-the-art open-source unified multimodal model, as our base model. Most experiments are conducted by supervised fine-tuning (SFT) on task-specific datasets, where verbal and visual generation in both chain-of-thought reasoning and final answers are optimized using cross-entropy and flow-matching loss. Specifically, the loss for reasoning with visual world modeling is as follows:
L195:  | $$\mathcal{L}_{\theta}(Q,I,R,A)=-\sum_{i=1}^{H+1}\sum_{j=1}^{|r_{i}|}\log p_{\theta}\left(r_{i,j}\mid r_{i,<j},R_{i}\right)+\sum_{i=1}^{H}\mathbb{E}_{t,\epsilon}\left\|v_{\theta}(o_{i}^{t},t\mid\tilde{R}_{i})-(\epsilon-o_{i})\right\|_{2}^{2},$$  |  | (6)
L196: where $o_{i}^{t}=to_{i}+(1-t)\epsilon$ are noisy observations. We emphasize that in our formulation, $r_{i}$ refers to a verbal reasoning step, instead of a reward. We also perform reinforcement learning from verifiable rewards (RLVR) following SFT. During RL, only the verbal generation component is optimized by GRPO [cite31†18 ], while visual generation is regularized via the KL-divergence with respect to the SFT-trained reference model:
L197:  | $\displaystyle\mathcal{J}_{\theta}(Q,I)=\mathbb{E}_{o,r\sim p_{\theta_{\text{old}}}}\Bigg[$  | $\displaystyle\sum_{i=1}^{H+1}\sum_{j=1}^{|r_{i}|}\Bigg(\min\Big(\frac{p_{\theta}\left(r_{i,j}\mid r_{i,<j},R_{i}\right)}{p_{\theta_{\text{old}}}\left(r_{i,j}\mid r_{i,<j},R_{i}\right)}{A},\ \text{clip}\Big(\frac{p_{\theta}\left(r_{i,j}\mid r_{i,<j},R_{i}\right)}{p_{\theta_{\text{old}}}\left(r_{i,j}\mid r_{i,<j},R_{i}\right)},1-\varepsilon,1+\varepsilon\Big){A}\Big)\Bigg)$  |
L198:  |  | $\displaystyle-\sum_{i=1}^{H}\mathbb{E}_{t,\epsilon}\left\|v_{\theta}(o_{i}^{t},t\mid\tilde{R}_{i})-v_{\theta_{\text{ref}}}(o_{i}^{t},t\mid\tilde{R}_{i})\right\|_{2}^{2}\Bigg].$  |  | (7)
L199: Full implementation details and hyperparameters are provided in Appendix cite24†8.2 .
L200: ## 5 Experimental Results
L201: 
L202: In this section, we demonstrate that visual world modeling boosts multimodal reasoning through two atomic capabilities: world simulation (Section cite11†5.1 ) and world reconstruction (Section cite12†5.2 ). We also identify tasks in which it is unhelpful (Section cite13†5.3 ), where implicit or verbal world modeling is sufficient. We conduct analysis in detail. Interestingly, we reveal emergent internal representations in UMMs that support implicit world modeling on simple maze tasks.
L203: ### 5.1 Visual World Simulation Boosts Multimodal Reasoning
L204: Main results. Figure cite109†4 summarizes the performance of SFT-trained UMMs under different chain-of-thought formulations across all tasks. We observe that interleaved CoT with visual world modeling significantly outperforms its purely verbal counterparts on three world simulation tasks: paper folding, multi-hop manipulation, and ball tracking. These gains are attributed to both the richer expressiveness and stronger prior knowledge afforded by the visual modality.


## jan29_stdvisioneval2

Visual Generation Unlocks Human-Like Reasoning through Multimodal World Models (https://arxiv.org/html/2601.19834v1)
citeturn28477view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19834v1","lineno":222}); Total lines: 584
L215: Even under this relaxed evaluation setting, Figure cite112†6 shows that verbal world modeling exhibits dramatically low fidelity, with scores degrading to near zero. Notably, approximately half of the samples require predicting the opposite view of a given input view, a transformation that only involves horizontal mirroring.
L216: Visual world modeling, benefiting from stronger prior knowledge of such geometric transformations, captures these patterns effectively and achieves fidelity scores consistently exceeding $50\%$.
L217: ### 5.3 Visual World Modeling is Unhelpful for Certain Tasks
L218: Main results. (Un)surprisingly, we do not observe notable improvements on grid-world tasks, including maze and Sokoban. In the maze tasks, reasoning with implicit world modeling—without explicitly tracking coordinates—achieves the best performance with a slight advantage. These results are consistent with recent empirical findings [cite32†14 ]. We argue that this is also well explained by our world model perspective.
L219: In these tasks, state tracking is relatively simple, typically requiring the maintenance of only one or two two-dimensional coordinates, which can be adequately handled through verbal reasoning alone. Furthermore, in the maze task, we hypothesize that such world modeling can be implicitly encoded in the model’s hidden representations [cite94†37 ], which helps explain the competitive performance of verbal reasoning without explicit coordinate tracking.
L220: cite114†Image: Refer to caption Figure 5: Probing implicit world models, by training a set of probes, i.e., MLPs which infer the masked point coordinates during reasoning from internal representations.
L221: Demystifying implicit world modeling. To validate this hypothesis, we probe the internal representations of models, as illustrated in Figure cite115†5 . We consider the same architecture, BAGEL, with three different sets of weights: a randomly initialized model, the pre-trained model, and the model supervised fine-tuned on CoT data in the implicit world modeling format, in which special tokens mask all explicit point coordinates during the reasoning process.
L222: For each model, we extract the hidden representations of these special tokens at each layer. We then train multilayer perceptrons (MLPs) on these representations to predict the underlying true point coordinates.
L223: Figure cite112†6 reports the prediction accuracy on a validation set. As expected, the randomly initialized model completely fails to internally track point states, achieving only random-guess accuracy on $5\times 5$ mazes. In contrast, the pre-trained model [cite59†13 ] already exhibits emergent representations that are predictive of maze states.
L224: Notably, we observe a non-monotonic trend across layers: prediction accuracy increases from lower layers (which capture low-level features) to middle layers, and then decreases toward the final layers, which are likely specialized for next-token prediction. Finally, supervised fine-tuning on domain-specific data, despite providing no explicit coordinate supervision, substantially enhances this internal predictability, achieving near-perfect accuracy.
L225: These in-depth results help explain our main experimental findings: as the model already possesses the capability for implicit world modeling, it does not necessarily benefit from explicit verbal world modeling, let alone more complex forms of visual world modeling.
L226: cite116†Image: Refer to caption (a) Sample efficiency.
L227: 
L228: cite117†Image: Refer to caption (b) World model fidelity.
L229: 
L230: cite118†Image: Refer to caption (c) Implicit world modeling.
L231: Figure 6: Model analysis: (a) Performance of UMMs on the paper-folding task with varying numbers of SFT samples. Reasoning with visual world modeling achieves a $4\times$ improvement in sample efficiency. WM = world modeling. (b) Performance of UMMs on the cube 3-view projection task with increasing sizes of input cube stacks, evaluated using both answer accuracy and world-model fidelity. Visual world modeling demonstrates dramatically better fidelity of view synthesis.
L232: (c) Prediction accuracy of masked point coordinates in CoTs using representations extracted from different layers of different UMMs, revealing emergent internal world representations. PT = Pre-trained. cite119†Image: Refer to caption Figure 7: Performance of SFT-trained VLMs compared with UMMs across three tasks. cite120†Image: Refer to caption Figure 8: Performance of RLVR-trained VLMs and UMMs with different world-model-based CoT formulations across three tasks.
L233: ### 5.4 Comparison with VLMs: Do UMMs Compromise Verbal Reasoning Capabilities?
L234: One may argue that UMMs are typically trained with a stronger emphasis on visual generation [cite59†13 ], which could compromise verbal reasoning capabilities, and bias comparisons in favor of visual world modeling. To address this concern, we compare with a pure VLM baseline, Qwen2.5-VL-7B-Instruct [cite48†6 ], which shares the same Qwen 2.5 LLM base model, with BAGEL.
L235: We fine-tune Qwen2.5-VL on the same verbal CoT datasets used in the previous subsections and evaluate it on three representative tasks: paper folding, cube 3-view projection, and multi-hop manipulation.
L236: Results. As shown in Figure cite121†7 , the SFT performance of Qwen2.5-VL with implicit and verbal world modeling is comparable to that of BAGEL, without exhibiting significant advantages. It still lags behind BAGEL in settings that leverage visual world modeling. These results indicate that our findings arise from the inherent advantages of visual world modeling rather than from compromised verbal reasoning capabilities in UMMs.
L237: ### 5.5 RL Enhances Various CoTs, Yet Does Not Close the Gap
L238: Reinforcement learning from verifiable rewards (RLVR) has been a major driver of recent progress in reasoning models equipped with verbal chain-of-thoughts, achieving strong performance across domains such as mathematics [cite31†18 ]. While Figure cite109†4 shows a clear advantage of reasoning with visual world modeling after SFT, RLVR may further incentivize emergent reasoning behaviors that improve verbal CoTs.
L239: We thus conduct comparative RLVR experiments across different world model–based CoT formulations on three representative tasks.
L240: Results. Figure cite122†8 presents the learning curves under RLVR for different models. We observe consistent improvements during RLVR for different CoT formulations. However, the performance gap persists. We also find that VLMs and UMMs generally perform similarly with verbal CoTs. These results suggest that the superiority arises from inherent advantages of the world modeling approach, rather than insufficient post-training.


## jan29_stdvisionsettingsroute

Visual Generation Unlocks Human-Like Reasoning through Multimodal World Models (https://arxiv.org/html/2601.19834v1)
citeturn28478view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19834v1","pattern":"GPU"}); Total lines: 584
No matching text found for "GPU"

## jan29_stdvisionnecessary3

Visual Generation Unlocks Human-Like Reasoning through Multimodal World Models (https://arxiv.org/html/2601.19834v1)
citeturn28479view2 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19834v1","pattern":"8.2"}); Total lines: 584
L0:   1. cite0†1 Introduction L1:   2. cite1†2 Related Work L2:   3. cite2†3 A World Model Perspective on Multimodal Reasoning L3:     1. cite3†3.1 Formulation: Multiple Observations of the World L4:     2. cite4†3.2 Atomic Capabilities of World Models L5:     3. cite5†3.3 Deliberate Reasoning with World Modeling Across Modalities L6:     4. cite6†3.4 The Visual Superiority Hypothesis L7:   4. cite7†4 Experiment Settings L8:     1. cite8†4.1 VisWorld-Eval: Task Suite for Reasoning with Visual World Modeling L9:     2. cite9†4.2 Unified Multimodal Model Training and Evaluation L10:   5. cite10†5 Experimental Results L11:     1. cite11†5.1 Visual World Simulation Boosts Multimodal Reasoning L12:     2. cite12†5.2 Visual World Reconstruction Boosts Multimodal Reasoning L13:     3. cite13†5.3 Visual World Modeling is Unhelpful for Certain Tasks L14:     4. cite14†5.4 Comparison with VLMs: Do UMMs Compromise Verbal Reasoning Capabilities? L15:     5. cite15†5.5 RL Enhances Various CoTs, Yet Does Not Close the Gap L16:   6. cite16†6 Discussions L17:   7. cite17†7 Theorectical Analysis L18:     1. cite18†7.1 Informativeness L19:     2. cite19†7.2 Prior Knowledge L20:       1. cite20†7.2.1 General Transfer Learning Analysis L21:       2. cite21†7.2.2 Remarks on Multimodal Reasoning L22:   8. cite22†8 Experiment Details L23:     1. cite23†8.1 VisWorld-Eval and Training Data L24:     2. cite24†8.2 Model Training L25:     3. cite25†8.3 Analytic Experiments L26:   9. cite26†9 Extended Experimental Results L27:     1. cite27†9.1 Full Results on MMSI-Bench L28:     2. cite28†9.2 Additional Qualitative Evaluation L29: 1]Tsinghua University 2]ByteDance Seed \contribution[*]Work done at ByteDance Seed \contribution[†]Corresponding authors
L30: # Visual Generation Unlocks Human-Like Reasoning through Multimodal World Models
L31: 
L32: Jialong Wu    Xiaoying Zhang    Hongyi Yuan    Xiangcheng Zhang    Tianhao Huang    Changjing He    Chaoyi Deng    Renrui Zhang    Youbin Wu    Mingsheng Long [ [ wujialong0229@gmail.com mingsheng@tsinghua.edu.cn zhangxiaoying.xy@bytedance.com
L33: 
L34: (January 27, 2026)
L35: ###### Abstract
L36: Humans construct internal models of the world and reason by manipulating the concepts within these models. Recent advances in artificial intelligence (AI), particularly chain-of-thought (CoT) reasoning, approximate such human cognitive abilities, where world models are believed to be embedded within large language models.
L37: Expert-level performance in formal and abstract domains such as mathematics and programming has been achieved in current systems, which rely predominantly on verbal reasoning as their primary information-processing pathway. However, they still lag far behind humans in domains like physical and spatial intelligence, which require richer representations and prior knowledge.
L38: The emergence of unified multimodal models (UMMs) capable of both verbal and visual generation has therefore sparked interest in more human-like reasoning grounded in complementary multimodal pathways, though a clear consensus on their benefits has not yet been reached. From a world-model perspective, this paper presents the first principled study of when and how visual generation benefits reasoning.
L39: Our key position is the visual superiority hypothesis: for certain tasks–particularly those grounded in the physical world–visual generation more naturally serves as world models, whereas purely verbal world models encounter bottlenecks arising from representational limitations or insufficient prior knowledge.
L40: Theoretically, we formalize internal world modeling as a core component of deliberate CoT reasoning and analyze distinctions among different forms of world models from both informativeness and knowledge aspects. Empirically, we identify and design tasks that necessitate interleaved visual-verbal CoT reasoning, constructing a new evaluation suite, VisWorld-Eval.
L41: Through controlled experiments on a state-of-the-art UMM, we show that interleaved CoT significantly outperforms purely verbal CoT on tasks that favor visual world modeling. Conversely, it offers no clear advantage for tasks that do not require explicit visual modeling. Together, these insights and findings clarify the applicability and potential of multimodal world modeling and reasoning for more powerful, human-like multimodal AI. We publicly release our evaluation suite to facilitate further research.
L194: Model training. We adopt BAGEL [cite59†13 ], a state-of-the-art open-source unified multimodal model, as our base model. Most experiments are conducted by supervised fine-tuning (SFT) on task-specific datasets, where verbal and visual generation in both chain-of-thought reasoning and final answers are optimized using cross-entropy and flow-matching loss. Specifically, the loss for reasoning with visual world modeling is as follows:
L195:  | $$\mathcal{L}_{\theta}(Q,I,R,A)=-\sum_{i=1}^{H+1}\sum_{j=1}^{|r_{i}|}\log p_{\theta}\left(r_{i,j}\mid r_{i,<j},R_{i}\right)+\sum_{i=1}^{H}\mathbb{E}_{t,\epsilon}\left\|v_{\theta}(o_{i}^{t},t\mid\tilde{R}_{i})-(\epsilon-o_{i})\right\|_{2}^{2},$$  |  | (6)
L196: where $o_{i}^{t}=to_{i}+(1-t)\epsilon$ are noisy observations. We emphasize that in our formulation, $r_{i}$ refers to a verbal reasoning step, instead of a reward. We also perform reinforcement learning from verifiable rewards (RLVR) following SFT. During RL, only the verbal generation component is optimized by GRPO [cite31†18 ], while visual generation is regularized via the KL-divergence with respect to the SFT-trained reference model:
L197:  | $\displaystyle\mathcal{J}_{\theta}(Q,I)=\mathbb{E}_{o,r\sim p_{\theta_{\text{old}}}}\Bigg[$  | $\displaystyle\sum_{i=1}^{H+1}\sum_{j=1}^{|r_{i}|}\Bigg(\min\Big(\frac{p_{\theta}\left(r_{i,j}\mid r_{i,<j},R_{i}\right)}{p_{\theta_{\text{old}}}\left(r_{i,j}\mid r_{i,<j},R_{i}\right)}{A},\ \text{clip}\Big(\frac{p_{\theta}\left(r_{i,j}\mid r_{i,<j},R_{i}\right)}{p_{\theta_{\text{old}}}\left(r_{i,j}\mid r_{i,<j},R_{i}\right)},1-\varepsilon,1+\varepsilon\Big){A}\Big)\Bigg)$  |
L198:  |  | $\displaystyle-\sum_{i=1}^{H}\mathbb{E}_{t,\epsilon}\left\|v_{\theta}(o_{i}^{t},t\mid\tilde{R}_{i})-v_{\theta_{\text{ref}}}(o_{i}^{t},t\mid\tilde{R}_{i})\right\|_{2}^{2}\Bigg].$  |  | (7)
L199: Full implementation details and hyperparameters are provided in Appendix cite24†8.2 .
L200: ## 5 Experimental Results
L201: 
L202: In this section, we demonstrate that visual world modeling boosts multimodal reasoning through two atomic capabilities: world simulation (Section cite11†5.1 ) and world reconstruction (Section cite12†5.2 ). We also identify tasks in which it is unhelpful (Section cite13†5.3 ), where implicit or verbal world modeling is sufficient. We conduct analysis in detail. Interestingly, we reveal emergent internal representations in UMMs that support implicit world modeling on simple maze tasks.
L203: ### 5.1 Visual World Simulation Boosts Multimodal Reasoning
L204: Main results. Figure cite109†4 summarizes the performance of SFT-trained UMMs under different chain-of-thought formulations across all tasks. We observe that interleaved CoT with visual world modeling significantly outperforms its purely verbal counterparts on three world simulation tasks: paper folding, multi-hop manipulation, and ball tracking. These gains are attributed to both the richer expressiveness and stronger prior knowledge afforded by the visual modality.
L205: In particular, it is difficult for models to precisely ground object coordinates and perform arithmetic operations without external tools in tasks such as multi-hop manipulation and ball tracking, with the latter being especially challenging. Thus, verbal world modeling is inappropriate and omitted in these tasks. This exacerbates ambiguity and hallucinations in purely verbal reasoning.
L206: Similarly, in paper folding, although models can track the states of holes, it remains difficult to completely depict the paper contour during unfolding. Moreover, as showcased in Figure cite110†9 and cite111†16 , the spatial transformation involved in paper unfolding critically relies on an understanding of geometric symmetry, which can be more naturally learned from visual data like images and videos.
L207: Sample efficiency. To further demonstrate the stronger prior knowledge embedded in the visual modality, we experiment comparing the sample efficiency of verbal and visual world modeling on the paper folding task. As shown in Figure cite112†6 , reasoning with visual world modeling exhibits substantially higher sample efficiency, achieving performance comparable to verbal world modeling while using more than $4\times$ less SFT data.
L208: ### 5.2 Visual World Reconstruction Boosts Multimodal Reasoning
L209: Main results. As shown in Figure cite109†4 , multimodal reasoning tasks that rely on world reconstruction capabilities also benefit substantially from visual world modeling. In the cube 3-view task, predicting a novel view of stacked cubes, denoted symbolic character matrices, suffers from limited prior knowledge, whereas visually rotating objects has been a rich experience during pre-training with large-scale Internet videos.
L210: For MMSI tasks, fully describing a novel view of a realistic scene using text alone is similarly ill-suited as in the previous subsection, and we also discover hallucinations in pure verbal reasoning, which lacks grounding to visual generation.
L508: We summarize the training and test sample counts for each task in VisWorld-Eval, along with the corresponding original or referenced benchmarks, in Table cite150†2 .
L509: Table 2: Overview of VisWorld-Eval and corresponding training data: features, statistics, and references.
L510: Task  | Capability  | Domain  |
L511: Training
L512: Samples
L513:  |
L514: Test
L515: Samples
L516:  | Source/Reference
L517: Paper folding  | Simulation  | Synthetic  | 2,357  | 480  | SpatialViz [cite99†61 ]
L518: Multi-hop manipulation  | Simulation  | Synthetic  | 2,000  | 480  | ZebraCoT [cite151†35 ], CLEVR [cite100†30 ]
L519: Ball tracking  | Simulation  | Synthetic  | 2,254  | 1,024  | RBench-V [cite101†20 ]
L520: Maze  | Simulation  | Synthetic  | 8,448  | 480  | maze-dataset [cite102†29 ]
L521: Sokoban  | Simulation  | Synthetic  | 7,715  | 480  | GameRL [cite103†55 ]
L522: Cube 3-view projection  | Reconstruction  | Synthetic  | 2,500  | 480  | SpatialViz [cite99†61 ]
L523: Real-world spatial reasoning  | Reconstruction  | Real-world  | 10,661  | 522  | MMSI-Bench [cite105†69 ]
L524: Examples of training CoTs are presented in Figure cite152†10 , cite153†11 , cite154†12 , cite155†13 , and cite156†14 .
L525: ### 8.2 Model Training
L526: 
L527: We perform supervised fine-tuning (SFT) of BAGEL based on its official repository^{5}^{5}5cite157†https://github.com/ByteDance-Seed/Bagel†github.com , using 8 GPUs, and conduct reinforcement learning from verifiable rewards (RLVR) using verl^{6}^{6}6cite158†https://github.com/volcengine/verl†github.com on 64 GPUs. Hyperparameters for SFT and RLVR are reported in Table cite159†4 and Table cite159†4 , respectively.
L528: 
L529: Table 3: Hyperparameters for supervised fine-tuning UMMs.
L530: Hyperparameter  | Value
L531: Learning rate  | $3\times 10^{-5}$
L532: LR Schedule  | Constant
L533: Optimizer  | AdamW
L534: Loss weight (CE:MSE)  | 1:10
L535: Warm-up steps  | 200
L536: Training steps  | 4000
L537: Gen. resolution  | (256, 1024) for paper folding, cube 3-view
L538:  | (240, 1024) for multi-hop manipulation
L539:  | (256, 512) otherwise
L540: Und. resolution  | (224, 980)
L541: Sequence length per rank  | 32K
L542: Num. ranks  | 8
L543: 
L544: Table 4: Hyperparameters for reinforcement learning UMMs.
L545: Hyperparameter  | Value
L546: Learning rate  | $1\times 10^{-5}$
L547: Batch size  | 128
L548: GRPO mini batch size  | 32
L549: Group size  | 16
L550: KL loss coefficient for visual gen.  | 0.1
L551: KL loss coefficient for verbal gen.  | 0.0
L552: cite160†Image: Refer to caption Figure 10: Examples of chain-of-thought SFT data for the paper folding task, under visual world modeling (left) and verbal world modeling (right). cite161†Image: Refer to caption Figure 11: Examples of chain-of-thought SFT data for the ball tracking and multi-hop manipulation task. cite162†Image: Refer to caption Figure 12: Examples of chain-of-thought SFT data for the maze and sokoban task.
L553: cite163†Image: Refer to caption Figure 13: Examples of chain-of-thought SFT data for the cube 3-view projection task, under visual world modeling (left) and verbal world modeling (right). cite164†Image: Refer to caption Figure 14: Examples of chain-of-thought SFT data for the real-world spatial reasoning task.
L554: The Qwen-VL baselines are trained using LLaMA-Factory^{7}^{7}7cite165†https://github.com/hiyouga/LLaMA-Factory†github.com for supervised fine-tuning (SFT) and verl for reinforcement learning from verifiable rewards (RLVR).
L555: ### 8.3 Analytic Experiments
L556: 
L557: Sample efficiency. For Figure cite112†6 , we randomly subsample either 500 or 1000 training examples. The resulting models are evaluated under two settings: (i) a hard setting with the maximum difficulty (grid size 8 and 4 folding steps, default in VisWorld-Eval), and (ii) an in-distribution setting (denoted as Normal in the figure) with randomly sampled grid sizes (3–8) and folding steps (1–4).
L558: Task difficulties and world model fidelity. For Figure cite112†6 , we generate test samples with varying cube-stack sizes (3–6), where size 6 is out-of-distribution relative to the training data. To assess world-model fidelity, we compare the generated views with the ground-truth views: for verbal world modeling, we use string pattern matching; for visual world modeling, we use Gemini 3 Pro to compare images.
L559: Since accurately inferring colors becomes particularly challenging at larger stack sizes, we evaluate only the shapes of the views and ignore color information. We also find that overall accuracy can be bottlenecked by verbal subskills (e.g., counting holes) after SFT, thus we report the accuracy of RL-trained models in Figure cite112†6 .
L560: In contrast, RL can distract verbal world modeling capabilities, leading to invalid formats of generated symbolic matrices, thus we report world-model fidelity of SFT-trained models.
L561: Implicit world modeling. For Figure cite112†6 , we supervised fine-tune (SFT) BAGEL on CoTs with implicit world modeling, in which all explicit point coordinates are replaced by the placeholder token sequence <point>masked<point>. After training, we extract the hidden representations at the position of the token masked from each transformer layer.
L562: We then split the extracted representations from different CoTs into training and validation sets with an 8:2 ratio and train a two-layer MLP (hidden size 4096) to predict the ground-truth point coordinates. Since all samples are $5\times 5$ mazes, we formulate coordinate prediction as two 5-way classification tasks (for $x$ and $y$, respectively). We compute classification accuracy for each coordinate and report the average of the two.
L563: ## 9 Extended Experimental Results
L564: ### 9.1 Full Results on MMSI-Bench
L565: 
L566: We report all scores on positional relationship tasks of MMSI-Bench in Table cite166†5 .
L567: 
L568: Table 5: Full results of SFT-trained UMMs on MMSI-Bench positional relationship tasks.
L569:  | MMSI-Bench (Positional Relationship)
L570: Models  | Cam.-Cam.  | Obj.–Obj.  | Reg.–Reg.  | Cam.–Obj.  | Obj.–Reg.  | Cam.–Reg.  | Overall
L571: Implicit WM  | 33.1  | 31.2  | 31.8  | 46.5  | 29.1  | 37.3  | 34.8
L572: Visual WM  | 29.6  | 29.5  | 31.6  | 60.9  | 25.8  | 54.4  | 38.4
L573: ### 9.2 Additional Qualitative Evaluation
L574: 
L575: We provide additional qualitative evaluation of trained UMMs’ reasoning, particularly failure cases.
L576: Real-world spatial reasoning. As shown in Figure cite167†15 a, reasoning with implicit world modeling is prone to hallucinations. In contrast, visual generation (Figure cite167†15 b) yields more faithful world models, but still suffers from insufficient quality, including blurring and corrupted details. Moreover, we find that current VLMs and UMMs continue to exhibit limited understanding of positions and directions across different viewpoints.
L577: We expect that stronger base models and better-curated post-training data will enable more effective use of visual world models for spatial reasoning in future work.
L578: Paper folding. As illustrated in Figure cite111†16 , verbal reasoning about geometric symmetry is prone to hallucinations, leading to inaccurate verbal world modeling. In contrast, visual world models, benefiting from stronger prior knowledge, generate correct intermediate unfolding steps even in the presence of erroneous verbal reasoning.
L579: Cube 3-view projection. As shown in Figure cite168†17 , visual world models are able to approximately generate novel views of cube stacks even in the challenging out-of-distribution setting with an unseen stack size of 6, indicating strong prior knowledge of spatial transformations. Nevertheless, overall task performance remains limited by subtle shape-generation errors (Figure cite168†17 b,d) and inaccurate color inference (Figure cite168†17 c).
L580: We expect these issues to be alleviated through improved post-training and stronger base models.
L581: cite169†Image: Refer to caption Figure 15: Showcases of reasoning generateed by post-trained UMMs in the real-world spatial reasoning task. We highlight hallucinations or incorrect reasoning steps in red. cite170†Image: Refer to caption Figure 16: Showcases of reasoning generated by post-trained UMMs in the paper folding task. We highlight hallucinations or incorrect reasoning steps in red, but also mark correctly generated visual unfolding intermediate steps with green borders.
L582: cite171†Image: Refer to caption Figure 17: Showcases of reasoning generated by post-trained UMMs in the paper folding task. We mark correct and incorrect generated cube views with green and red borders, respectively. For incorrect generations, the corresponding ground-truth views are provided for reference (note that these are shown only for readers and are never provided to the models during reasoning).
