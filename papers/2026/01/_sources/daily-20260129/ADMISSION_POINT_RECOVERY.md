RPO-RAG: Aligning Small LLMs with Relation-aware Preference Optimization for Knowledge Graph Question Answering (https://arxiv.org/html/2601.19225v1)
citeturn28118view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"turn28117view1","pattern":"3 Method"}); Total lines: 465
L15:   1. cite5†Abstract. L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Work L18:     1. cite8†2.1 Preference Optimization L19:     2. cite9†2.2 KG-based RAG L20:   4. cite10†3 Method L21:     1. cite11†3.1 Query-Path Semantic Sampling L22:     2. cite12†3.2 Semantic-Matching based Path Retrieval L23:     3. cite13†3.3 Dual-Objective Optimization L24:   5. cite14†4 Experiments L25:     1. cite15†4.1 Experimental Settings L26:     2. cite16†4.2 Main Results (RQ1) L27:     3. cite17†4.3 Competitiveness of Small LLMs (RQ2) L28:     4. cite18†4.4 Ablation Study (RQ3) L29:     5. cite19†4.5 Dataset Quality Analysis (RQ4) L30:   6. cite20†5 Conclusion L31:   7. cite21†References L32:   8. cite22†A Limitations and Future Work L33:   9. cite23†B Experimental Details L34:     1. cite24†B.1 KGQA benchmarks L35:     2. cite25†B.2 Implementation Details L36:     3. cite26†B.3 Baselines L37:     4. cite27†B.4 Answer-Centered Prompt Detailed L38:   10. cite28†C Error Case L39: cite29†License: CC BY-NC-ND 4.0†info.arxiv.org L40: 
L41: arXiv:2601.19225v1 [cs.CL] 27 Jan 2026
L42: # RPO-RAG: Aligning Small LLMs with Relation-aware Preference Optimization for Knowledge Graph Question Answering
L43: 
L44: Conference: Proceedings of the ACM Web Conference 2026; April 13–17, 2026; Dubai, United Arab Emirates Proceedings of the ACM Web Conference 2026 (WWW ’26), April 13–17, 2026, Dubai, United Arab Emirates DOI: cite30†10.1145/3774904.3792730†doi.org ISBN: 979-8-4007-2307-0/2026/04 CCS: Information systems Question answering
L104: Despite these advances, both lines of work share notable limitations: reliance on shortest-path heuristics that ignore query-path semantics, and limited modeling of intermediate relational reasoning caused by flat, ungrouped prompt design, which is particularly detrimental for smaller LLMs.
L105: Within this landscape, our framework aligns with efficiency-oriented approaches by employing a PLM-based semantic retriever. Its novelty lies in introducing adaptive, semantics-aware path sampling and relation-level optimization.
L106: ## 3. Method
L107: RPO (R elation-aware P reference O ptimization)-RAG is a novel framework designed to enhance the reasoning capabilities of small LLMs in the KG-based RAG paradigm. The framework adopts an end-to-end retrieval-and-reasoning pipeline that refines learning signals across the system. It consists of three main components. (1) Query-Path Semantic Sampling constructs a high-fidelity dataset that captures query intent and provides supervisory signals for both retriever and reasoner.
L108: (2) Semantic-Matching Retriever trained on this sampled dataset employs dynamic beam search to efficiently extract semantically relevant reasoning paths. Finally, (3) Dual-Objective Optimization integrates relation-aware relevance-weighted preference optimization with answer-centered prompt optimization, substantially improving the reasoning ability of small LLMs. The overall architecture is illustrated in Figure  cite65†2 .
L109: ### 3.1. Query-Path Semantic Sampling
--------------------------------------------------------------------------------
RPO-RAG: Aligning Small LLMs with Relation-aware Preference Optimization for Knowledge Graph Question Answering (https://arxiv.org/html/2601.19225v1)
citeturn28118view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"turn28117view1","pattern":"preference"}); Total lines: 465
L85: RPO-RAG explicitly models the reasoning process of LLMs at the relation level. To the best of our knowledge, it is the first framework that incorporates relations into preference optimization for KG-based RAG.
L86: 
L87:   * •
L88: 
L89: Experimental results on KGQA benchmarks show that our framework consistently outperforms existing methods and, in particular, substantially narrows the performance gap of small-scale LLMs compared to larger-scale baselines.
L90: cite55†Image: Main Architecture Figure 2. Overview of the RPO-RAG framework. (1) Query-Path Semantic Sampling: constructs query-aligned training paths via dynamic clustering to capture query intent. (2) Semantic-Matching Retriever: retrieves reasoning paths semantically consistent with the query using a pretrained language model. (3) Dual-Objective Optimization: optimizes relation-level preference and answer-centered prompt objectives to align small LLMs with structured reasoning. Main Architecture
L91: ## 2. Related Work
L92: ### 2.1. Preference Optimization
L93: Preference optimization (PO) is a training paradigm that optimizes a model’s generation with human preferences by comparing pairs of responses, typically consisting of a preferred $(y^{+})$ and a non-preferred $(y^{-})$. Early approaches are grounded in Reinforcement Learning from Human Feedback (RLHF) (cite56†Christiano et al., 2017 ; cite57†Ouyang et al., 2022 ). In this setting, a supervised model is first trained, followed by a separate reward model learned from human-annotated preferences.
L94: While effective, this two-stage pipeline suffers from instability and inefficiency, as reinforcement learning is computationally intensive and slow. To improve efficiency, Direct Preference Optimization (DPO)  (cite58†Rafailov et al., 2023 ) directly optimizes the model such that the probability of generating $y^{+}$ exceeds that of $y^{-}$, removing the need for a reward model. However, DPO typically requires a costly reference model to prevent policy collapse.
L95: SimPO  (cite59†Meng et al., 2024 ) further enhances efficiency by discarding the reference model and employing length correction to mitigate response bias.
L96: Despite these advances, existing PO methods  (cite60†Stiennon et al., 2020 ; cite57†Ouyang et al., 2022 ; cite58†Rafailov et al., 2023 ; cite61†Ko et al., 2024 ) have been exclusively applied to high-level text generation tasks such as dialogue or summarization, relying heavily on human-annotated data. In contrast, we present an approach that extends preference optimization to relation-level supervision in KGQA.
L97: Specifically, we optimize the probability of generating the next relation conditioned on partial paths, aligning the model with the query’s intent. Crucially, we construct preference pairs via a weakly supervised method based on semantic relevance of sampled paths, avoiding reliance on costly manual annotations.
L150: (6)  |  | $$\hat{m}_{q,\tau}=ReLU(\textbf{W}_{q}\textbf{h}_{q}\times\textbf{W}_{\tau}\textbf{h}_{\tau}),$$  |
L151: 
L152: where $\textbf{W}_{q},\textbf{W}_{\tau}$ are projection matrices, and $\textbf{h}_{q},\textbf{h}_{\tau}$ are embeddings of $q$ and $\tau$, respectively. Finally, we optimize the following cross-entropy loss to predict top-$K$ answer entity types for each question:
L153: (7)  |  | $$\begin{split}\mathcal{L}_{Type}=-\sum_{q\in Q}\sum_{\tau\in T_{q}}(m_{q,\tau}\log(\hat{m}_{q,\tau})+\\
L154: (1-m_{q,\tau})\log(1-\hat{m}_{q,\tau})),\end{split}$$  |
L155: 
L156: where $m_{q,\tau}$ is a labeled entity type score. After training, we use the top-5 prediction result to exclude paths whose terminal entity is inconsistent with the predicted types.
L157: ### 3.3. Dual-Objective Optimization
L158: Relation-aware Weighted Preference Optimization
L159: A key novelty of our framework is, to our knowledge, the first application of preference optimization at the relation level for knowledge graph reasoning. While prior works mainly focus on optimizing answers or paths as whole units, we introduce a fine-grained objective that supervises the inference of intermediate relations. This design explicitly guides small LLMs to reason over structured relation sequences step by step, rather than only focusing on end entities.
L160: As illustrated in Figure cite71†4 , our model learns to prefer relations semantically consistent with the query context. As shown in the example, these relation-level preference signals encourage step-by-step, semantically grounded reasoning.
L161: cite72†Image: Relation-aware Weighted Preference Optimization Figure 4. Illustration of Relation-aware Weighted Preference Optimization. For the same question and current path (left), candidate next relations (right) are scored by semantic relevance. Higher-scored relations are treated as preferred (CHOSEN), while semantically misaligned ones are treated as non-preferred (REJECT).Relation-aware Weighted Preference Optimization
L162: Since the importance of each relation varies across queries, we assign adaptive confidence weights based on semantic relevance. To construct preference signals, we first identify positive and negative relation sets. Relations from the representative cluster $\mathcal{C}^{*}$ obtained during path sampling are regarded as preferred responses $Y^{+}$, while relations from alternative clusters are treated as non-preferred responses $Y^{-}$.
L163: This weakly supervised construction enables preference pairs without annotation.
L164: Each relation is weighted according to its semantic proximity to the cluster centroid. Preferred relations closer to the centroid receive higher confidence, while non-preferred relations farther away are penalized. Formally, letting $u(y)$ denote the centroid distance and $\alpha>0$ a decay rate, we define:
L165: 
L166: (8)  |  | $$s(y)=\begin{cases}e^{-\alpha\,u(y)}&\text{if }y\in Y^{+}\;\;\text{(preferred)}\\[2.0pt]
L167: 1-e^{-\alpha\,u(y)}&\text{if }y\in Y^{-}\;\;\text{(non-preferred)}\end{cases}$$  |
L168: These confidence scores are transformed into weights $(w^{+},w^{-})$ with a scaling factor $\beta>0$:
L169: 
L170: (9)  |  | $$w=\beta\big(1+0.5(s-0.5)\big)$$  |
L171: 
L172: Training then proceeds with a margin-based preference objective:
L173: 
L174: (10)  |  | $$\mathcal{L}(\pi_{\theta})=-\mathbb{E}\Big[\log\sigma\big(W^{+}\log\pi_{\theta}(y^{+}\mid x)-W^{-}\log\pi_{\theta}(y^{-}\mid x)-\gamma\big)\Big],$$  |
L175: where $W^{+}=w^{+}/|y^{+}|$ and $W^{-}=w^{-}/|y^{-}|$ are normalized by relation length, and $\gamma$ is a margin term. By explicitly applying relation-level preference optimization with relevance-weighted signals, our approach introduces a new training paradigm for KGQA. This enables small LLMs to internalize structured, step-by-step relational reasoning and improve their capacity to execute faithful, interpretable inference over KGs.
L176: Answer-Centered Prompt Optimization
L177: The second objective complements relation-level training by aligning answer generation with answer-centered reasoning paths. Prompts are explicitly designed to incorporate multiple reasoning paths as evidence supporting candidate answers. Unlike conventional prompts that treat each path in isolation and fail to integrate information from multiple topic entities, our proposed prompt unifies these paths into a coherent representation better suited for small LLMs.
--------------------------------------------------------------------------------
MetaGen: Self-Evolving Roles and Topologies for Multi-Agent LLM Reasoning (https://arxiv.org/html/2601.19290v1)
citeturn28118view2 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: find({"ref_id":"turn28117view2","pattern":"feedback"}); Total lines: 355
L53: We introduce MetaGen, a training-free framework that adapts both the role space and the collaboration topology at inference time, without updating base model weights. MetaGen generates and rewrites query-conditioned role specifications to maintain a controllable dynamic role pool, then instantiates a constrained execution graph around a minimal backbone. During execution, it iteratively updates role prompts and adjusts structural decisions using lightweight feedback signals.
L65: We present MetaGen, a training-free framework that adapts both the role space and the collaboration topology at test time (Figure cite57†1 ). MetaGen introduces an Architect that synthesizes and revises query-conditioned role specifications to form a controllable dynamic role pool. It then constructs an initial execution graph around a minimal backbone and iteratively updates role prompts and structural decisions using lightweight feedback signals, without modifying backbone weights.
L66: To prevent unrestricted chatter, MetaGen enforces explicit controls, including schema/validity checks for generated roles, constrained graph construction, selective activation and edge gating, and cost-aware stopping.
L67: MetaGen is designed to be effective and inspectable. It logs generated roles, selected participants, structural edits, and the feedback that triggers each update, supporting reproducibility and diagnosis beyond ad hoc orchestration. This combination of dynamic roles, inference-time evolution, and structured control targets the core limitations of rigid MAS while retaining the engineering advantages of graph-based collaboration. In summary, our contributions are:
L68: 
L69:   * •
L70: We propose MetaGen, a training-free framework that improves multi-agent collaboration by adapting role specifications and communication topology during inference.
L71: 
L72:   * •
L73: 
L74: We introduce query-conditioned role generation and revision with lightweight validity constraints, yielding a controllable dynamic role pool.
L75: 
L76:   * •
L77: 
L78: We develop an inference-time evolution loop that updates prompts and structural decisions under explicit constraints to bound cost and maintain auditability.
L79: 
L80:   * •
L81: Extensive experiments demonstrate that MetaGen consistently improves the accuracy–cost trade-off over competitive multi-agent baselines, and ablations confirm the complementary benefits of dynamic roles, within-instance refinement, and cross-instance accumulation.
L82: cite58†Image: Refer to caption Figure 2: MetaGen framework overview. Given a query, an Architect generates and filters candidate roles, then performs novelty-driven role selection and hybrid graph initialization to form an initial DAG $G_{\text{init}}$. MetaGen supports intra-task evolution by updating role prompts and structure using execution feedback, and inter-task evolution by accumulating cross-instance priors and solidifying verified roles for future reuse.
L83: ## 2 Related Work
L84: ### 2.1 Multi-agent collaboration with LLMs.
L85: A growing body of work solves complex tasks via LLM-based multi-agent collaboration cite59†Akata et al. (2025) ; cite60†Guo et al. (2024) ; cite61†Zhao et al. (2024) ; cite62†Hao et al. (2025) , where multiple agents exchange intermediate results to reduce single-agent blind spots and improve reliability. Common paradigms include discussion-style coordination that aggregates diverse perspectives and iteratively refines candidate solutions 【63†Saha et al.
L165:  | $$s_{r}=\mathbf{w}_{\text{role}}^{\top}\phi(r),\qquad s_{u\to v}=\mathbf{w}_{\text{edge}}^{\top}\psi(u\!\to\!v),$$  |  | (8)
L166: 
L167: and select a Top-$K$ committee with an $\epsilon$-greedy strategy. Edges are added to form $G_{\text{init}}$ when their scores exceed a threshold $\delta$, subject to DAG constraints.
L168: #### Intra-task Evolution.
L169: 
L170: Starting from $G_{\text{init}}$, MetaGen performs lightweight within-instance refinement over multiple rounds. We denote by $\mathcal{F}$ the feedback collected during inference and tool execution, consisting of naturally observable signals such as runtime logs, compilation/test outcomes, format validators, and self-consistency checks. This feedback is available without introducing additional supervision and serves as the trigger for instance-level edits.
L171: Given $\mathcal{F}$, MetaGen applies two types of edits that operate only on textual role specifications and a constrained subset of structural choices. First, role prompt rewrite targets a low-utility role whose messages are consistently unhelpful (e.g., redundant, unstable, or verbose) under the current instance.
L172: Using the feedback traces (error messages, failed checks, or inconsistency patterns), MetaGen revises the role’s system/user templates to better align the role behavior with the instance requirements. Second, prior-filtered edge exploration updates topology within the instance in a conservative manner.
L173: MetaGen first filters candidate non-critical edges using current priors and structural constraints (e.g., preserving at least one path to the exit/judge node and avoiding cycles), then selectively deactivates or swaps one edge to encourage simpler, more informative communication. Across rounds, these edits allow the collaboration process to react to observed failure modes while keeping the execution stable and auditable.
L174: #### Inter-task Evolution.
L175: 
L176: While intra-task evolution adapts behavior for a single instance, MetaGen also improves future decisions by maintaining lightweight state across instances. After an instance completes, we summarize its overall outcome into a scalar reward that trades off success and cost,
L177: 
L178:  | $$R=\mathbb{I}(\text{pass})-\lambda_{\text{cost}}\cdot\mathcal{C}_{\text{token}},$$  |  | (9)
L179: where $\mathbb{I}(\text{pass})$ is a task-specific pass indicator produced by the evaluator and $\mathcal{C}_{\text{token}}$ is the total token usage. We then update the parameters that govern role/edge scoring with a reward-weighted linear rule:
L180: 
L181:  | $$\mathbf{w}\leftarrow\mathbf{w}+\eta\,R\,\mathbf{f},$$  |  | (10)
L182: where $\mathbf{f}$ is the feature vector for the decision that was used, i.e., $\mathbf{f}=\phi(r)$ for a selected role (updating $\mathbf{w}_{\text{role}}$) or $\mathbf{f}=\psi(u\!\to\!v)$ for an activated edge (updating $\mathbf{w}_{\text{edge}}$). Intuitively, decisions that lead to successful, low-cost executions receive positive updates and become more likely under similar contexts, whereas costly or unsuccessful executions yield weaker (or negative) reinforcement.
L191: 2:  $\Delta\mathcal{R}\leftarrow\textsc{SelectNovel}(\mathcal{C},\mathcal{R}_{L})$; $\mathcal{V}\leftarrow\mathcal{R}_{L}\cup\Delta\mathcal{R}$
L192: 
L193: 3:  $\mathcal{V}_{K}\leftarrow\textsc{EpsGreedySelect}(\mathcal{V};\mathbf{w}_{\text{role}},K,\epsilon)$
L194: 
L195: 4:  $G_{\text{init}}\leftarrow G_{\text{skel}}\ \cup\ \textsc{AddEdges}(\mathcal{V}_{K};\mathbf{w}_{\text{edge}},\delta)$
L196: 
L197: 5:  $G_{\text{init}}\leftarrow\textsc{EnforceDAG}(G_{\text{init}})$
L198: 
L199: 6:  for $t=1$ to $T_{\max}$ do
L200: 7:   $(\tau,y)\leftarrow\textsc{Execute}(G_{\text{init}},x)$
L201: 
L202: 8:   $\mathcal{F}\leftarrow\textsc{Feedback}(\tau)$; $p\leftarrow\textsc{Pass}(\mathcal{F})$
L203: 
L204: 9:   if $p=1$ then
L205: 
L206: 10:    break
L207: 
L208: 11:   end if
L209: 
L210: 12:   $\mathcal{V}\leftarrow\textsc{PromptRewrite}(\mathcal{V},\mathcal{F})$
L211: 
L212: 13:   $G_{\text{init}}\leftarrow\textsc{PriorFilteredExplore}(G_{\text{init}},\mathcal{F};\mathbf{w})$
L213: 
L214: 14:  end for
L215: 
L216: 15:  $R\leftarrow p-\lambda_{\text{cost}}\cdot\textsc{TokenCost}(\tau)$
L341: ## Instructions for reporting errors
L342: 
L343: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
L344: 
L345:   * Click the "Report Issue" () button, located in the page header.
L346: 
L347: Tip: You can select the relevant text first, to include it in your report.
--------------------------------------------------------------------------------
Modular Foundation Model Inference at the Edge:Network-Aware Microservice Optimization (https://arxiv.org/html/2601.19563v1)
citeturn28118view3 [wordlim: 200] Crawled: 5 days ago; Content type: text/html; Source: find({"ref_id":"turn28117view3","pattern":"Simulation"}); Total lines: 278
L234: TABLE I: Key Simulation Parameters
L235:  | $r_{m,k}/R_{v,k}$(CPU;RAM;GPU;VRAM)  | $a_{m}$(MB)  | $b_{m}$(MB)  | $f_{m}$(MB/ms)  | $c_{m}^{\text{dp}},c_{m}^{\text{mt}},c_{m}^{\text{pl}}$
L236: Core MS  | [2,16];[1,4];[4,32];[4,32]  | [2,16]  | [0.1,1]  | [8,32]  | 20.0; 4.0; 0.0
L237: Light MS  | [0.5,2];[0,0.5];[0.25,4];[0,1]  | [0.5,2]  | [0.25,1.5]  | $Gamma$([1,2],[1,20])  | 4.0; 1.0; 0.5
L238: ED  | [1,64];[1,32];[0,64];[0,64]  | $z_{u,n,t}$(/ms)  | $D_{n}$(ms)  | $\gamma_{u}$(Gbs)  | $A_{n}$(MB)  | $w$(MB/ms)
L239: ES  | [128,256];[64,128];[1024,2048];[256,512]  | $Poisson$([0.15,1.5])  | [50,100]  | $Nakagami$([1.5,3],[0.5,1])  | [0.5,4]  | [0.1,1.0]
L240: cite42†Image: Refer to caption Fig. 3: Violin-plot comparison of on-time task completion rate and total system cost across four deployment strategies. cite43†Image: Refer to caption Fig. 4: Comparison of the proposed framework and the PropAvg ablation under escalating system loads.
L241: Fig. cite44†3 visualizes, via violin plots, the distributions of the on-time task completion rate and the total system cost across four deployment strategies. Narrow, concentrated violins indicate stable performance, whereas wider ones suggest inconsistency. An effective deployment should exhibit a compact distribution with high completion rates and moderate costs.
--------------------------------------------------------------------------------
In-Network Collective Operations: Game Changer or Challenge for AI Workloads? (https://arxiv.org/html/2601.19132v1)
citeturn28118view4 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: find({"ref_id":"turn28117view0","pattern":"Low Precision"}); Total lines: 245
L15:   1. cite5†Abstract L16:   2. cite6†The Role of Collective Operations and CCLs in AI L17:   3. cite7†Opportunities for In-Network Computation to Accelerate AI L18:     1. cite8†Collective Acceleration using Edge-INC L19:     2. cite9†Collective Acceleration using Core-INC L20:   4. cite10†Problems for In-Network Compute Acceleration of AI L21:     1. cite11†Low Precision Data Types L22:     2. cite12†Vector Data Types L23:     3. cite13†Sparse Vector Reductions L24:     4. cite14†Bitwise Reduction Result Reproducibility L25:     5. cite15†Endpoint Interfaces and Coordination L100: The advantages of In-Network Computation (INC) are both evident and substantial, with potential traffic reductions at both edge links and in the core network of up to $2\times$ for operations such as Allreduce, Reduce_scatter, Broadcast, and Allgather. Additionally, INC can significantly reduce host memory load and provide opportunities for overlapping computation and communication during collective operations [cite27†10 ]. However, the intricacies of INC can be complex and challenging to navigate.
L101: In the following sections, we present several obstacles that architects and engineers developing INC systems must consider.
L102: ### Low Precision Data Types
L103: One of the most effective optimizations in deep learning and AI is the utilization of low-precision data types. Reducing the number of bits used to represent numerical values not only linearly decreases data volume and movement but can also lead to a quadratic increase in computational performance. Specifically, reducing values from $16$-bit to $8$-bit precision results in a $2\times$ savings in memory and memory bandwidth, as well as a potential $4\times$ speedup in computations.
L104: The computational speedup is because the multiplication of n-bit integers generally requires $O(n^{2})$ logic or time, making low-precision representations highly advantageous for efficient AI computations.
L105: Low-precision types can only express a narrower range of numbers. An $8$-bit integer can represent $256$ distinct values, while a $4$-bit integer is limited to just $16$ different values. The selection of which numbers these types represent can be determined either algorithmically, such as setting a uniform range like $-128$ to $127$ for signed integers, or through a predefined code-book.
L106: Moreover, the range can be dynamically adjusted by scaling factors that are applied block- or tensor-wise to better fit the data’s dynamic range. However, a significant challenge with low-bit representations, particularly in processing long sequences, is temporary overflow, underflow, or accumulating rounding errors.
L107: This occurs when intermediate computations exceed the representational capacity of the low-bit format, even if the final result could theoretically be accurately represented within that format.
L108: To illustrate the challenges with low-precision arithmetic, consider performing a series of operations using a signed int4 type (range $-8$ to $7$): $7-5+5+5-3-7$. If we compute from left to right, we get intermediate results of $7$, $2$, $7$, then an overflow to $-3$, $-6$, and an underflow to $2$.
L109: Although the final result might be correct, these intermediate results are inaccurate, leading to errors when used in further calculations like dot-products or matrix multiplications, especially when combined with multiplication operations. Another example is the multiplication task $2*2*3/2$, which yields intermediate results of $2$, $4$, then an overflow to $-4$, and finally the incorrect $-2$, instead of the expected $6$.
L110: These precision issues also affect sequences of mixed addition and multiplications. Since floating-point operations fundamentally involve both multiplication and addition in operations (e.g., floating point multiplication multiplies the mantissas and adds the exponents), the same problems can occur. To prevent these errors, AI accelerators employ higher-precision internal accumulation registers.
L111: Core-INC requires sending intermediate results to upstream switches by design, which introduces challenges with precision and bandwidth. Since the maximum bandwidth savings from Core-INC is a factor of two, transmitting numbers with higher precision to maintain accuracy would essentially negate this advantage. Compounding the issue, most internal higher-precision registers are significantly larger than just twice the size of the input data types.
L112: This situation is commonly referred to as the "problem of communicating the accumulator" in Core-INC systems, where accumulators need to be relayed between switches. Conversely, in Edge-INC scenarios, where large vectors of numbers are reduced, one can mitigate this by designating a specific host for each range, thereby allowing for the local maintenance of a high-precision accumulator at each Network Interface (NI), keeping the benefits of precision without the overhead of excessive data transmission.
L113: One potential, though complex, workaround involves sending only low-precision values from the edge hosts to the first reduction switch, then using a high-precision accumulator for communication between core switches, finally casting down to the lower target precision at the root switch. This approach requires careful consideration because the accumulation switches are not always the first in the chain.
L114: For instance, in the Core-INC example figure above, the source S does not directly connect to an accumulation switch; instead, the accumulator size should increase at the second hop, which coincidentally is also the root. In other parts of the green network tree in our example, the precision would need to be increased at the second switch encountered. If more than two group members would be connected to an edge switch, then the result would need to be upcast there.
--------------------------------------------------------------------------------
In-Network Collective Operations: Game Changer or Challenge for AI Workloads? (https://arxiv.org/html/2601.19132v1)
citeturn28118view5 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: find({"ref_id":"turn28117view0","pattern":"Performance for"}); Total lines: 245
L15:   1. cite5†Abstract L16:   2. cite6†The Role of Collective Operations and CCLs in AI L17:   3. cite7†Opportunities for In-Network Computation to Accelerate AI L18:     1. cite8†Collective Acceleration using Edge-INC L19:     2. cite9†Collective Acceleration using Core-INC L20:   4. cite10†Problems for In-Network Compute Acceleration of AI L21:     1. cite11†Low Precision Data Types L22:     2. cite12†Vector Data Types L23:     3. cite13†Sparse Vector Reductions L24:     4. cite14†Bitwise Reduction Result Reproducibility L25:     5. cite15†Endpoint Interfaces and Coordination L26:     6. cite16†Encryption and Authentication L27:   5. cite17†Performance for INC in Deep Learning L28:   6. cite18†Summary and Predictions L29:   7. cite19†ACKNOWLEDGMENTS L30:   8. cite20†REFERENCES L31: cite21†License: CC BY 4.0†info.arxiv.org L32: 
L33: arXiv:2601.19132v1 [cs.NI] 27 Jan 2026
L34: # In-Network Collective Operations:
L35: Game Changer or Challenge for AI Workloads?
L36: Torsten Hoefler Affiliation: ETH Zürich, Zurich, Switzerland and Microsoft, Redmond, USA    Mikhail Khalilov Affiliation: ETH Zürich, Zurich, Switzerland    Josiah Clark Affiliation: AMD, Santa Clara, USA    Surendra Anubolu Affiliation: Broadcom Inc., San Jose, USA    Mohan Kalkunte Affiliation: Broadcom Inc., San Jose, USA    Karen Schramm Affiliation: Broadcom Inc., San Jose, USA    Eric Spada Affiliation: Broadcom Inc., San Jose, USA    Duncan Roweth Affiliation: Hewlett Packard Enterprise, Palo Alto, USA    Keith Underwood Affiliation: Hewlett Packard Enterprise, Palo Alto, USA    Adrian Caulfield Affiliation: Microsoft, Redmond, USA    Abdul Kabbani Affiliation: Microsoft, Redmond, USA    Amirreza Rastegari Affiliation: Microsoft, Redmond, USA
L142: Implementing encryption and authentication in a Core-INC system remains challenginga and a topic for research, even when utilizing separate keys and security domains. This complexity arises because switches must partake in key rotation and re-keying, potentially incorporating key derivation and other advanced security mechanisms.
L143: The necessary overhead in memory for managing these keys and the logic required for system administration is not only intricate and costly but also introduces additional security vulnerabilities. Edge-INC systems may simplify the security handling as only the local NI would need to be part of the trust domain.
L144: ## Performance for INC in Deep Learning
L145: The primary objective of INC is to expedite computations within the network and decrease communication volumes. While reducing communication volumes is advantageous because it frees network resources to handle other types of traffic, accelerating computations presents a more intricate challenge. In the context of accelerating real-world applications, a variant of Amdahl’s Law becomes a significant constraint.
L146: Consequently, claims of a tenfold improvement in application performance should prompt scrutiny from astute performance experts.
L147: cite49†Image: Refer to caption L148: 
L149: Figure 5: Performance model for INC-enabled DP training.
L150: In Figure cite50†5 we consider the following simple example of DP parallel training where we model a fixed 8GiB Allreduce with varying iteration times to adjust the communication overhead (portion of iteration time (%) spent in Allreduce) between $10$-$50$% on the x-axis. Without INC, the ring Allreduce takes 352ms and INC can reduce the time to 151ms, a nearly 60% speedup. Yet, due to Amdahl’s law, the maximum speedup achieved is $34$%.


In-Network Collective Operations: Game Changer or Challenge for AI Workloads? (https://arxiv.org/html/2601.19132v1)
citeturn28119view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28117view0","lineno":110}); Total lines: 245
L94: Reduce_scatter can be implemented as multiple reductions that are identical to broadcast trees. Here, the same idea as Allgather applies and bandwidth can be saved in the core network. Furthermore, concurrent Reduce_scatter can be combined with Allgather in Core-INC to gain bandwidth savings up to $2\times$ due to their different bottlenecks [cite39†13 ].
L95: Alltoall cannot be optimized easily with Core-INC as there is no reduction in data at all. Alltoall simply transposes a large array. Here, Edge- or Core-INC could be used to synchronize nodes to orchestrate congestion-free schedules for sending the data. This is generally hard given that the network may not be exclusively used by a single tenant.
L96: Core-INC and Edge-INC both have complex relationships with the system itself. From a reliability perspective, Core-INC utilizes fewer links, but becomes more dependent on the links it uses and carries state in the switches that is not resilient to switch failure. Edge-INC can use traditional techniques to route around failures, but incurs delays during failures and is more dependent on a high fraction of the bandwidth being available.
L97: Job fragmentation can cause point-to-point communications in Edge-INC to take substantially longer, whereas Core-INC is more immune to fragmentation - until the fragmentation reaches a level where the network is no longer able to achieve a data reduction. Both Edge-INC and Core-INC can be complementary and multiply their benefits.
L98: For example, a local NI can take charge of coordinating the Core-INC such that the accelerator is completely freed from communication overheads and full overlap of communication and computation can be achieved.
L99: ## Problems for In-Network Compute Acceleration of AI
L100: The advantages of In-Network Computation (INC) are both evident and substantial, with potential traffic reductions at both edge links and in the core network of up to $2\times$ for operations such as Allreduce, Reduce_scatter, Broadcast, and Allgather. Additionally, INC can significantly reduce host memory load and provide opportunities for overlapping computation and communication during collective operations [cite27†10 ]. However, the intricacies of INC can be complex and challenging to navigate.
L101: In the following sections, we present several obstacles that architects and engineers developing INC systems must consider.
L102: ### Low Precision Data Types
L103: One of the most effective optimizations in deep learning and AI is the utilization of low-precision data types. Reducing the number of bits used to represent numerical values not only linearly decreases data volume and movement but can also lead to a quadratic increase in computational performance. Specifically, reducing values from $16$-bit to $8$-bit precision results in a $2\times$ savings in memory and memory bandwidth, as well as a potential $4\times$ speedup in computations.
L104: The computational speedup is because the multiplication of n-bit integers generally requires $O(n^{2})$ logic or time, making low-precision representations highly advantageous for efficient AI computations.
L105: Low-precision types can only express a narrower range of numbers. An $8$-bit integer can represent $256$ distinct values, while a $4$-bit integer is limited to just $16$ different values. The selection of which numbers these types represent can be determined either algorithmically, such as setting a uniform range like $-128$ to $127$ for signed integers, or through a predefined code-book.
L106: Moreover, the range can be dynamically adjusted by scaling factors that are applied block- or tensor-wise to better fit the data’s dynamic range. However, a significant challenge with low-bit representations, particularly in processing long sequences, is temporary overflow, underflow, or accumulating rounding errors.
L107: This occurs when intermediate computations exceed the representational capacity of the low-bit format, even if the final result could theoretically be accurately represented within that format.
L108: To illustrate the challenges with low-precision arithmetic, consider performing a series of operations using a signed int4 type (range $-8$ to $7$): $7-5+5+5-3-7$. If we compute from left to right, we get intermediate results of $7$, $2$, $7$, then an overflow to $-3$, $-6$, and an underflow to $2$.
L109: Although the final result might be correct, these intermediate results are inaccurate, leading to errors when used in further calculations like dot-products or matrix multiplications, especially when combined with multiplication operations. Another example is the multiplication task $2*2*3/2$, which yields intermediate results of $2$, $4$, then an overflow to $-4$, and finally the incorrect $-2$, instead of the expected $6$.
L110: These precision issues also affect sequences of mixed addition and multiplications. Since floating-point operations fundamentally involve both multiplication and addition in operations (e.g., floating point multiplication multiplies the mantissas and adds the exponents), the same problems can occur. To prevent these errors, AI accelerators employ higher-precision internal accumulation registers.
L111: Core-INC requires sending intermediate results to upstream switches by design, which introduces challenges with precision and bandwidth. Since the maximum bandwidth savings from Core-INC is a factor of two, transmitting numbers with higher precision to maintain accuracy would essentially negate this advantage. Compounding the issue, most internal higher-precision registers are significantly larger than just twice the size of the input data types.
L112: This situation is commonly referred to as the "problem of communicating the accumulator" in Core-INC systems, where accumulators need to be relayed between switches. Conversely, in Edge-INC scenarios, where large vectors of numbers are reduced, one can mitigate this by designating a specific host for each range, thereby allowing for the local maintenance of a high-precision accumulator at each Network Interface (NI), keeping the benefits of precision without the overhead of excessive data transmission.
L113: One potential, though complex, workaround involves sending only low-precision values from the edge hosts to the first reduction switch, then using a high-precision accumulator for communication between core switches, finally casting down to the lower target precision at the root switch. This approach requires careful consideration because the accumulation switches are not always the first in the chain.
L114: For instance, in the Core-INC example figure above, the source S does not directly connect to an accumulation switch; instead, the accumulator size should increase at the second hop, which coincidentally is also the root. In other parts of the green network tree in our example, the precision would need to be increased at the second switch encountered. If more than two group members would be connected to an edge switch, then the result would need to be upcast there.
L115: Even if this strategy is implemented correctly, it still necessitates transmitting at least double the data volume upwards through intermediate links, thus diminishing the potential for bandwidth savings within the core network. Furthermore, such savings would depend strongly on the tree topology.
L116: ### Vector Data Types
L117: Some deep learning accelerators and workloads leverage vector data types, which, like the quantized numbers previously discussed, incorporate scaling factors. However, these scaling factors are not uniformly applied across entire tensors or large blocks but are instead tailored to smaller blocks that constitute the basic units of computation. An example of this is a set of 16 integer values scaled by an exponential floating-point value, a method referred to as block floating point.
L118: This technique has been adopted to formulate various blocked data types, such as MxFP [cite41†18 ], enhancing efficiency in deep learning computations.
L119: If block floating-point and similar vector data types are extensively utilized, INC systems might need to inherently support these formats. Although one could convert these block formats into types that INC currently supports, such conversions introduce additional overhead. This overhead could diminish the performance benefits of INC, particularly since operations on these vector types can be executed very efficiently on native architectures using traditional collective algorithms like ring.
L120: Consequently, implementing complex type handling within the INC switch or Network Interface (NI) might be necessary, which could increase both cost and design complexity.
L121: Another broad challenge in this domain is the rapid evolution of data types used in deep learning. Over the past decade, we’ve witnessed a "Cambrian explosion" of various data types, with new formats like BF16, E4M3, and E5M2 gaining quick and widespread acceptance due to their availability on modern accelerators.
L122: This swift pace of change in data types poses a significant challenge for the networking field, which often operates within a slower silicon design cycle, making it difficult to keep pace with the latest advancements in deep learning.
L123: ### Sparse Vector Reductions
L124: Sparse computations offer significant advantages for deep learning workloads by reducing computational overhead and memory usage [cite42†8 ]. This advantage extends into network computations but introduces the problem of fill-in. Similar to the issue of communicating accumulators, fill-in can lead to even more substantial slowdowns.
L125: The core problem arises when multiplying two sparse vectors in a large index space; the result often becomes much larger because it must accommodate as many elements as the union of the indices from both vectors. If non-zeros are randomly distributed, this leads to a rapid increase in vector size as computations progress through the reduction tree.
L126: Consequently, vectors might become so dense that even switching to a dense representation becomes more efficient at some height along the tree [cite43†17 , cite44†19 ].
L127: Supporting sparse reductions in Core-INC is inherently complex and prone to errors, which can negate much of the efficiency gains provided. To circumvent this issue, one potential strategy involves sharding the index space across endpoints, thereby directing all values associated with a particular index space to their respective endpoint.
L128: It’s mathematically provable, given certain distributions of non-zero elements, that such an approach can optimize communication volume, potentially reducing the data traffic in the core network more effectively than with Core-INC methods. These advanced, endpoint-based schemes [cite45†14 ] could be effectively realized through Edge-INC, allowing for all the associated benefits to be fully exploited.
L129: ### Bitwise Reduction Result Reproducibility
L130: For certain workloads and use-cases, such as debugging, bitwise reproducibility is critical. This is straightforward with integer data types, but floating-point sum is not associative. Therefore, floating-point calculations can only achieve bitwise reproducibility if the exact order of operations is maintained or if specific reproducibility schemes are employed [cite46†5 , cite47†1 ].
L131: However, these schemes typically introduce up to twice the data and computational overhead, which can negate the $2\times$ efficiency gain offered by Core-INC, akin to the problem encountered with accumulator communication. While there might be room for innovation in developing schemes for INC, ensuring a consistent order of operations is often the simplest solution.
L132: Users care about intra-job and inter-job reproducibility. Intra-job reproducibility ensures that reductions within a single job are bitwise identical, while inter-job reproducibility extends this guarantee across different jobs, specifically to those involving the same number of processes.
L133: Achieving inter-job reproducibility necessitates ensuring an identical tree structure for data reduction across jobs, which presents significant challenges because the distribution of processes across nodes can vary greatly between different job executions. Ensuring consistent tree ordering is both theoretically and practically complex and is an open research problem. It might not be feasible for certain configurations of process-to-node mappings.
L134: ### Endpoint Interfaces and Coordination
L135: When implementing INC, it’s essential for the switch to incorporate a basic networking stack to handle reliability, flow control, and congestion management. This is due to the shared nature of the physical link, where both INC and regular end-to-end traffic compete for bandwidth, necessitating compatible congestion control mechanisms.
L136: Additionally, NIs at the endpoints must manage INC states and contexts in hardware, leading to increased complexity in logic (e.g., when considering link aggregation) and additional memory overhead.
L137: Constructing Core-INC groups and their corresponding reduction trees presents significant system-level challenges and hindered early adoption. The hardware resources available at each switch constrain the number of trees it can support. Given that switches are interconnected in complex topologies, and jobs launch on dynamic subsets of nodes, creating and dismantling these trees must be managed efficiently at job (or even communicator) initiation and termination.
L138: Multi-tenancy can exacerbate this by increasing the number of trees within the network, potentially necessitating strict isolation measures. However, many of these complexities can be sidestepped with Edge-INC systems, which can operate effectively using simpler switches designed purely for data movement, thereby reducing the overhead associated with managing intricate network structures.
L139: ### Encryption and Authentication
L140: Encryption and authentication crucial in confidential computing systems. Unfortunately, Core-INC faces significant challenges in supporting end-to-end encryption due to its data manipulation operations. While homomorphic encryption presents a potential solution, its application is currently limited and most effective for integer data types only. Chrapek et al. develop several initial ideas for Homomorphic Core-INC systems [cite48†4 ].
L141: Yet, for a system to support all operations and data types, it would necessitate extending trust to the switches, thereby substantially expanding the trust domain. Employing separate keys for INC communication can help limit the trust domain’s scope. However, any data transmitted through INC remains susceptible to compromise.
L142: Implementing encryption and authentication in a Core-INC system remains challenginga and a topic for research, even when utilizing separate keys and security domains. This complexity arises because switches must partake in key rotation and re-keying, potentially incorporating key derivation and other advanced security mechanisms.
--------------------------------------------------------------------------------
Modular Foundation Model Inference at the Edge:Network-Aware Microservice Optimization (https://arxiv.org/html/2601.19563v1)
citeturn28119view1 [wordlim: 200] Crawled: 5 days ago; Content type: text/html; Source: open({"ref_id":"turn28117view3","lineno":74}); Total lines: 278
L49: Despite these efforts, many works treat microservices as homogeneous components with similar requirements, overlooking their distinct workload and operational characteristics, which, however, are essential for fine-grained resource match, QoS delivery, and efficient scaling in FM-based inference tasks.
L50: Specifically, FM inference pipelines comprise heterogeneous MSs with fundamentally different deployment behaviors. Core MSs, which encapsulate the computation-intensive models (e.g., transformers, vision backbones), exhibit long startup times and limited fault tolerance, making them rigid yet performance-critical anchors of the inference workflow.
L51: Conversely, light MSs perform auxiliary, typically stateless operations such as pre- or post-processing, forming an elastic tier that can be rapidly instantiated and parallelized across shared resources to sustain data flow toward the cores.
L52: This operational asymmetry creates a multi-timescale coordination challenge, where slow-to-deploy, fault-sensitive core components must coexist with agile, contention-prone light components, demanding a type-aware deployment framework for reliable, responsive, and cost-efficient FM inference.
L53: This work presents a two-tier FM inference framework that leverages the core–light MS dichotomy to manage system uncertainty, with three key contributions:
L54: 
L55:   1. $\bullet$
L56: 
L57: For the first time, we design a hybrid MS deployment strategy for FM edge inference: Slow-startup core services are statically placed to form a reliable system backbone based on long-term workload statistics, while lightweight services are dynamically deployed to elastically adapt to real-time system fluctuations.
L58: 
L59:   2. $\bullet$
L60: To achieve a forward-looking and fault-tolerant static core MS placement, we formulate a sparsity-constrained integer program that co-optimizes for cost and a statistical QoS score while ensuring deployment diversity.
L61: 
L62:   3. $\bullet$
L63: To enable QoS-aware online decision-making under resource contention, we pioneer the use of effective capacity theory to link service parallelism with statistical latency bounds, which is then integrated into a Lyapunov optimization framework to derive a low-complexity online algorithm for light MS deployment.
L64: cite27†Image: Refer to caption Fig. 1: Illustration of FM-based inference application with the MS architecture. Squares denote core MSs, circles denote light MSs, and different line styles represent different task types of inter-service dependencies.
L65: ## II System Model and Problem Formulation
L66: In this section, we develop an MS-based FM inference framework at the edge network, where the FMs are decomposed into a collection of functionally distinct core and light MSs deployed across the network. We consider a heterogeneous edge network with varying resource capacities, which consists of edge devices (EDs) and edge servers (ESs) represented by $\mathcal{V}$ and interconnected by the set of communication links, $\mathcal{E}$.
L67: Specifically, resource capacity of node $v$ is denoted by $\mathbf{R}_{v}=[R_{v,k}]_{k\in[K]}$, where $K$ is the number of distinct resource types (e.g., CPU, RAM, GPU), and $[K]=\{1,2,...,K\}$ is the set of integers up to any $K\in\mathbb{Z}_{>0}$.
L68: ### II-A Microservice Specification for FM Inference
L69: An FM inference application architecture is characterized by a fundamental functional asymmetry, which segregates MSs into two categories with distinct operational profiles, as illustrated in Fig. cite28†2 . Specifically, core MSs ($\mathcal{M}^{\text{cr}}$) are heavyweight and stateful services operated under strict resource isolation to yield deterministic performance, which form the computational backbone.
L70: Light MSs ($\mathcal{M}^{\text{lt}}$), in contrast, are stateless components with small footprints and can be quickly redeployed elsewhere; their performance is stochastic, a direct result of resource contention incurred by their efficient parallel processing of concurrent tasks on shared resources.
L71: Formally, we characterize each MS $m\in\mathcal{M}=\mathcal{M}^{\text{lt}}\cup\mathcal{M}^{\text{cr}}$ by its resource requirement vector $\mathbf{r}_{m}=[r_{m,k}]_{k\in[K]}$, and the computational workload, $a_{m}$ (bits), that must be executed to produce an output of size $b_{m}$ (bits). Its processing rate, $f_{m}$ (bits/ms), is a deterministic constant for a core MS but a random variable for any light MS to capture the effects of resource contention.
L72: These MSs are orchestrated to execute inference tasks. A task of type $n$ is represented by a DAG $\mathcal{G}_{n}=(\mathcal{M}_{n},\mathcal{L}_{n})$, where $\mathcal{M}_{n}\subseteq\mathcal{M}$ denotes the required MSs ($|\mathcal{M}_{n}|=I_{n}$) and $\mathcal{L}_{n}$ the date dependencies. Consistent with multimodal data fusion, these graphs typically form inverse-tree structures, where each node may have multiple incoming but at most one outgoing edge.
L73: starts with an input payload of $A_{n}$ and must meet an end-to-end latency constraint $D_{n}$.
L74: cite29†Image: Refer to caption Fig. 2: MS-based FM inference on a heterogeneous edge network.
L75: ### II-B Latency Formulation under Network Uncertainty
L76: The system dynamics are driven by several stochastic events. Users $u\in\mathcal{U}$ stochastically generate tasks of type $n$, and we denote the number of such arrivals at time $t$ by the random variable $z_{t,u,n}$. These tasks are transmitted to an associated edge device over a wireless fading channel, where the signal-to-noise ratio $\gamma_{u}$ is also random.
L77: These external uncertainties, along with the processing rates of light MS $f_{m}$, are assumed to be stationary and statistically independent over time, and their distributions can be accurately profiled.
L78: An admitted task $j$, uniquely identified by its origin $(u,n,t)$, joins the set of active tasks $J(t)$ and is executed along a routing path $P_{j}=[(v_{i},m_{i})]_{i\in[I_{n}]}$ determined by our strategy. Its end-to-end latency comprises the uplink transmission delay from user $u$ to its first node, the inter-node transmission and propagation delay along the routing path, and the processing delay of each invoked service, respectively expressed as
L79:  | $$\tau_{j}^{\text{ul}}=\frac{A_{n}}{b_{u}\log(1+\gamma_{u})},$$  |  | (1)
L80:  | $$\tau_{j}^{\text{tr}}(v_{i1},v_{i2})=\frac{b_{m_{i1}}}{w_{(i1,i2)}},\quad\tau_{j}^{\text{pp}}(v_{i1},v_{i2})=\frac{W_{(i1,i2)}}{l},$$  |  | (2)
L81:  | $$\tau_{j}^{\text{pc}}(v_{i})=\frac{a_{m_{i}}}{f_{m_{i}}}.$$  |  | (3)
L82: Here, $b_{u}$ denotes the bandwidth allocated to user $u$, and $b_{u}\log(1+\gamma_{u})$ is its achievable uplink rate; $w_{(i1,i2)}$ and $W_{(i1,i2)}$ are the bandwidth and distance of the link between nodes $v_{i1}$ and $v_{i2}$; $l$ is the propagation speed.
L83: 
L84: The DAG dependencies necessitate a recursive calculation for the completion time $T_{j}$ at any node $v$, as a service must wait for all its predecessors:
L85:  | $\displaystyle T_{j}(v_{1})$  | $\displaystyle=\tau_{j}^{\text{ul}}+\tau_{j}^{\text{pc}}(v_{1}),v_{1}\in P_{j},$  |
L86:  | $\displaystyle T_{j}(v_{i2})$  | $\displaystyle=\max_{\begin{subarray}{c}v_{i1},v_{i2}\in P_{j}\\
L87: v_{i1}\in\mathcal{V}_{P_{j}}^{\text{pa}}(v_{i2})\end{subarray}}\left\{T_{j}(v_{i1})+\tau_{j}^{\text{tr}}(v_{i1},v_{i2})\right.$  |  | (4)
L88:  |  | $\displaystyle\qquad\qquad\qquad\quad\left.+\tau_{j}^{\text{pp}}(v_{i1},v_{i2})+\tau_{j}^{\text{pc}}(v_{i2})\right\},$  |
L89: where $\mathcal{V}_{P_{j}}^{\text{pa}}(v)$ denotes the set of parent nodes of $v$ in path $P_{j}$. The total end-to-end latency of task $j$ is
L90: 
L91:  | $$T_{j}^{\text{E2E}}=T_{j}(v_{I_{n}}),v_{I_{n}}\in P_{j}.$$  |  | (5)
L92: 
L93: Crucially, $T_{j}^{\text{E2E}}$ is a complex, stochastic function of the path $j$, making it challenging to satisfy the deadline $D_{n}$ while simultaneously optimizing for resource costs.
L94: ### II-C Problem Formulation
L95: The deployment of core MSs remains fixed throughout a finite time horizon $\mathcal{T}$, governed by $\mathbf{X}^{\text{cr}}\in\mathbb{N}^{|\mathcal{V}|\times|\mathcal{M}^{\text{cr}}|}$, where $x_{v,m}^{\text{cr}}$ denotes the instance number of core MS $m$ placed on node $v$.
L96: In contrast, light MSs are deployed dynamically, controlled by two time-varying tensors: $\mathbf{X}^{\text{lt}}\in\mathbb{N}^{|\mathcal{V}|\times|\mathcal{M}^{\text{lt}}|\times|\mathcal{T}|}$ specifies the instance count $x_{v,m,t}^{\text{lt}}$, while $\mathbf{Y}\in\mathbb{N}^{|\mathcal{V}|\times|\mathcal{M^{\text{lr}}}|\times|\mathcal{T}|}$ defines the parallelism level $y_{v,m,t}$, the number of concurrent tasks an instance can process, to manage resource contention.
L97: The objective is to minimize the total system cost over $\mathcal{T}$. The cost of core MSs includes initial deployment and ongoing maintenance for each instance:
L98: 
L99:  | $$C^{\text{cr}}(\mathbf{X^{\text{cr}}})=\sum_{v\in\mathcal{V}}\sum_{m\in\mathcal{M}^{\text{cr}}}\left(c_{m}^{\text{cr,dp}}+\sum_{t\in\mathcal{T}}c_{m}^{\text{cr,mt}}\right)x_{v,m}^{\text{cr}},$$  |  | (6)
L100: where $c_{m}^{\text{cr,dp}}$, $c_{m}^{\text{cr,mt}}$ are the one-time deployment price and per-slot maintenance price, respectively. For light MSs, the cost accounts for instantiation, maintenance, and parallelism:
L101:  | $\displaystyle C^{\text{lt}}(\mathbf{X}^{\text{lt}})=$  | $\displaystyle\sum_{v\in\mathcal{V}}\sum_{m\in\mathcal{M}^{\text{lt}}}\sum_{\begin{subarray}{c}t\in\mathcal{T}\\
L102: t\neq 0\end{subarray}}c_{m}^{\text{lt,dp}}\max\{0,x_{t,v,m}^{\text{lt}}-x_{t-1,v,m}^{\text{lt}}\}$  |  | (7)
L103:  |  | $\displaystyle+\sum_{v\in\mathcal{V}}\sum_{m\in\mathcal{M}^{\text{lt}}}\sum_{t\in\mathcal{T}}(c_{m}^{\text{lt,mt}}+c_{m}^{\text{lt,pl}})x_{v,m}^{\text{lt}},$  |
L104: where $c_{m}^{\text{lt,dp}}$, $c_{m}^{\text{lt,mt}}$, and $c_{m}^{\text{lt,pl}}$ are the instantiation, per-slot maintenance, and parallelism cost of light MS $m$, respectively.
L105: 
L106: This optimization is subject to several operational constraints. Firstly, the total resource consumption at any node cannot exceed its capacity:
L107:  | $\displaystyle\sum_{m\in\mathcal{M}^{\text{cr}}}r_{m,k}x_{v,m}^{\text{cr}}+\sum_{m\in\mathcal{M}^{\text{lt}}}r_{m,k}x_{v,m,t}^{\text{lt}}\leq R_{v,k},$  |  | (8)
L108:  | $\displaystyle\forall k\in[K],v\in\mathcal{V},t\in\mathcal{T}.$  |
L109: 
L110: To ensure timeliness, the end-to-end latency of every task must meet its deadline:
L111: 
L112:  | $$T_{j}^{\text{E2E}}\leq D_{n},\forall j\in J(t),t\in\mathcal{T}.$$  |  | (9)
L113: Furthermore, the provisioned capacity must be sufficient to handle the incoming workload. Let $z_{v,m,t}$ denote the number of tasks requiring MS $m$ at node $v$ at time $t$, which is determined by the routing paths of all concurrent tasks. The deployment must adhere to the following capacity constraints:
L114:  | $$x_{v,m}^{\text{cr}}\geq z_{v,m,t},\forall m\in\mathcal{M}^{\text{cr}},v\in\mathcal{V},t\in\mathcal{T},$$  |  | (10)
L115:  | $$x_{v,m,t}^{\text{lt}}y_{v,m,t}\geq z_{v,m,t},\forall m\in\mathcal{M}^{\text{lt}},v\in\mathcal{V},t\in\mathcal{T}.$$  |  | (11)
L116: 
L117: Finally, all decision variables must be non-negative integers:
L118: 
L119:  | $$x_{v,m}^{\text{cr}},x_{v,m,t}^{\text{lt}},y_{v,m,t}\in\mathbb{N},\forall v\in\mathcal{V},m\in\mathcal{M},t\in\mathcal{T}.$$  |  | (12)
L120: The overall MS deployment problem can be formulated as
L121: 
L122:  | $\displaystyle\min_{\mathbf{X}^{\text{cr}},\mathbf{X}^{\text{lt}},\mathbf{Y}}$  | $\displaystyle C^{\text{cr}}+C^{\text{lt}},$  |  | (13)
L123:  | $\displaystyle\text{s.t.}$  | $\displaystyle\eqref{resouce_cons}\sim\eqref{eq:var_cons}.$  |
L124: Problem (cite30†13 ) is intractable due to a triad of compounding challenges. First, stochasticity in arrivals and processing rates makes the hard QoS constraint (cite31†9 ) analytically unmanageable, as feasibility itself becomes probabilistic. Second, the workload $z_{v,m,t}$ creates a circular dependency: the optimal deployment strategy depends on the anticipated task load at each node, yet this load itself is a direct consequence of how tasks are routed through the deployed services.
L125: Finally, the problem is high dimensional integer nonlinear programming and renders exact solution methods computationally prohibitive, challenging to meet real-time environments.
L126: ## III Network-Aware Microservice Deployment for FM Edge Inference
L127: 
L128: To tackle the challenging problem (cite30†13 ), we propose a two-tier deployment strategy that exploits the functional asymmetry of the FM inference pipelines.
L129: ### III-A Reliable Core MS Deployment
L130: 
L131: The static core MS placement must be cost-efficient and also account for future QoS demands without knowledge of exact, real-time task arrivals. To achieve this, we introduce a heuristic QoS score $Q_{v,m}$ to quantify the expected value of placing an instance of type $m$ on node $v$. By incorporating this score into the objective, we can transform the stochastic deployment into a deterministic integer program:
L132:  | $\displaystyle\min_{\mathbf{X}^{\text{cr}}}$  | $\displaystyle\sum_{v\in\mathcal{V}}\sum_{m\in\mathcal{M}^{\text{cr}}}x_{v,m}^{\text{cr}}(c_{m}^{\text{cr}}-\xi Q_{v,m}),$  |  | (14)
L133:  | $\displaystyle\text{s.t.}$  | $\displaystyle\text{C1: }r_{m,k}x_{v,m}^{\text{cr}}\leq R_{v,k},\forall k\in[K],v\in\mathcal{V},$  |
L134:  |  | $\displaystyle\text{C2: }\sum_{v\in\mathcal{V}}\tilde{z}_{v,m}\leq\sum_{v\in\mathcal{V}}x_{v,m}^{\text{cr}},\forall m\in\mathcal{M}^{\text{cr}},$  |
L135:  |  | $\displaystyle\text{C3: }x_{v,m}^{\text{cr}}\in\mathbb{N},\forall v\in\mathcal{V},m\in\mathcal{M}^{\text{cr}},$  |
L136: where, $c_{m}^{\text{cr}}=c_{m}^{\text{cr,dp}}+c_{m}^{\text{cr,mt}}$ and $\xi\geq 0$ is a weight balancing cost against the QoS measure. The term $\tilde{z}_{v,m}$ is the average estimate for load $z_{v,m,t}$. For this static formulation, the real-time per-node capacity constraint (cite32†10 ) is relaxed into a global constraint, which ensures the total long-term capacity meets the total estimated demand across the network.
L137: The heuristics $\tilde{z}_{v,m}$ and $Q_{v,m}$ are derived from a mean-value analysis of latency profiles.
L138: To obtain these estimates, we consider a typical task $j$ (identified by its origin $(u,n,t)$) requiring MS $m\in\mathcal{M}^{\text{cr}}\cap\mathcal{M}_{n}$ at node $v\in\mathcal{V}$ and partition its estimated end-to-end latency into three parts: the preceding latency to reach node $v$, $d_{j}^{\text{pr}}(v,m)=\max_{v^{{}^{\prime}}\in\mathcal{V}_{P_{j,v}}^{\text{pa}}(v)}\bar{T}_{j}(v^{{}^{\prime}})$; the processing time at the current node, $d_{j}^{\text{cu}}(v,m)=\frac{a_{m}}{f_{m}}$; and the succeeding latency for all subsequent MSs, $d_{j}^{\text{su}}(v,m)=\sum_{m^{{}^{\prime}}\in\mathcal{M}_{n}^{\text{de}}(m)}\frac{a_{m^{{}^{\prime}}}}{\bar{f}_{m^{{}^{\prime}}}}$, respectively.
L139: Specifically, $\bar{T}_{j}$ is calculated via (cite33†4 ) using mean values for all random variables, $P_{j,v}$ is the shortest path from the task’s source to node $v$ where path length is measured as the sum of network and average computation latencies, and $\mathcal{M}_{n}^{\text{de}}(m)$ is the set of descendant MSs of $m$ in $\mathcal{G}_{n}$.
L140: For the estimated load $\tilde{z}_{v,m}$, we apportion the mean task arrival rate to nodes based on an exponential decay of the preceding latency:
L141: 
--------------------------------------------------------------------------------
From Observations to Events: Event-Aware World Model for Reinforcement Learning (https://arxiv.org/html/2601.19336v1)
citeturn28119view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19336v1","lineno":null}); Total lines: 853
--------------------------------------------------------------------------------
LightSBB-M: Bridging Schrödinger and Bass for Generative Diffusion Modeling (https://arxiv.org/html/2601.19312v1)
citeturn28119view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19312v1","lineno":null}); Total lines: 552

