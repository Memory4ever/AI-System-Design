# Exact-v1 necessary primary — 2601.19827

Preserved original tool responses; repeated returned context is not a claim of full-appendix review.

## jan29_stdvisionhead

When Iterative RAG Beats Ideal Evidence: A Diagnostic Study in Scientific Multi-hop Question Answering (https://arxiv.org/html/2601.19827v1)
citeturn28473view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19827v1","lineno":null}); Total lines: 744


## jan29_stdvisionroute

When Iterative RAG Beats Ideal Evidence: A Diagnostic Study in Scientific Multi-hop Question Answering (https://arxiv.org/html/2601.19827v1)
citeturn28474view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19827v1","pattern":"3."}); Total lines: 744
L26:         3. cite16†III. Information Synthesis Diagnostics L27:     2. cite17†3.2 Experimental Setup L28:       1. cite18†3.2.1 Dataset and Indexing L29:       2. cite19†3.2.2 Synergized Reasoning and Retrieval Implementation L30:         1. cite20†Step Definition and Loop. L31:         2. cite21†Partial Answer State. L32:         3. cite22†Context Management. L33:       3. cite23†3.2.3 Correctness and Difficulty L34:   5. cite24†4 Results L35:     1. cite25†4.1 Decomposing Performance: The "Synchronized" Advantage L36:     2. cite26†4.2 Stability Analysis: Recoveries vs. Regressions L37:     3. cite27†4.3 The Cost of Retrieval: Parametric Memory Suppression L38:     4. cite28†4.4 Portion of Unanswered Questions L39:   6. cite29†5 Analysis L40:     1. cite30†5.1 Dynamics of Iterative Utilization L41:       1. cite31†5.1.1 Mechanism of Control: Self-Correction via Anchor Propagation L42:       2. cite32†5.1.2 Step-Count Distribution and Model Strategy L43:     2. cite33†5.2 Failure Modes in Iterative RAG L44:       1. cite34†5.2.1 Retrieval Coverage Gaps: The Prerequisite for Reasoning L45:       2. cite35†5.2.2 Evidence Sufficiency vs. Retrieval Coverage L46:       3. cite36†5.2.3 Confidence Miscalibration: Stopping Too Early or Too Late L47:       4. cite37†5.2.4 Composition Failure: The Synthesis Bottleneck L48:       5. cite38†5.2.5 Distractor Latch: The Retrieval Trap L49:     3. cite39†5.3 Efficiency Analysis L50:       1. cite40†5.3.1 The Trade-off: Adaptivity vs. Predictability L51:     4. cite41†5.4 Adherence and Controllability L52:       1. cite42†Success Rate of Compliance Attempts L53:   7. cite43†6 Discussion L54:   8. cite44†7 Conclusion L55:   9. cite45†References L56:   10. cite46†S1 Appendix L57:     1. cite47†S1.1 Extended Literature Review L58:     2. cite48†S1.2 Performance and Token Utilization L59:     3. cite49†S1.3 Detailed Failure Mode Analysis L60:       1. cite50†S1.3.1 Prevalence and Impact L61:       2. cite51†S1.3.2 Damage Index L62:     4. cite52†S1.4 Query Characteristics L63:     5. cite53†S1.5 Case Studies and System Prompts L145: ### 3.1 Evaluation Framework and Metrics
L150: ##### Difficulty Stratification.
L151: 
L152: To characterize model performance across complexity levels, we define questions as: Easy: Answered correctly by majority of models (2 or less models made mistake out of 11 tested models). Medium: Answered incorrectly by around half of the evaluated models (5 - 7 models). Hard: Answered incorrectly by majority of models (9 to 11).
L153: #### 3.1.1 Diagnostic Suite
L154: To attribute failure modes to specific components (retrieval, reasoning, or control), we audit every iterative run using three families of diagnostics. Since the selected database, provide the oracle hops, their path and gold context for each hop, in addition to the questions, answers and corpus; detailed evaluation of models performance and their reasoning path is possible.
L204: #### 3.2.1 Dataset and Indexing
L230: This ensures that even at the step budget limit, the model processes a focused context of approximately 18 passages, preventing older information from overwhelming the latest evidence. Furthermore, partial answers and previous queries along with original question and the step number is passed to the model to make decision.
L231: #### 3.2.3 Correctness and Difficulty
L232: Given the complexity of chemical nomenclature, exact string matching is insufficient. We verify answers using an LLM-as-a-judge (GPT-5-mini) protocol. The evaluation prompt (see cite108†S11 ) is designed to treat aliases, synonyms, molecular formulas, and IUPAC names as identical to the canonical answer. In the Iterative RAG setting, models may include brief explanations; such responses are considered correct if the final answer string is present as the specific final output.
L233: This verifier is the same verifier used in cite73†Khodadad et al. (2025b) that introduced the paper.
L234: Figure 1: The Iterative RAG System: A training-free controller alternates between targeted retrieval and partial answer updates.
L238:  | Accuracy (%)  | Average Output Tokens
L239: Model  | No Ctx  | Gold Ctx  | Iter. RAG  | No Ctx  | Gold Ctx  | Iter. RAG
L240: OpenAI GPT-4o  | 32.29  | 56.32  | 81.96  | 9  | 10  | 448.63
L241: OpenAI GPT-5  | 45.11  | 71.68  | 80.86  | 1565.48  | 713.41  | 5592.61
L242: Anthropic Claude 3.7 Sonnet (Reasoning)  | 39.80  | 73.27  | 86.09  | 1777  | 715  | 4309.00
L243: Anthropic Claude 3.7 Sonnet (Standard)  | 37.52  | 68.13  | 84.49  | 30  | 30  | 714.73
L244: DeepSeek R1  | 39.04  | 72.51  | 82.29  | 162  | 573  | 3671.38
L402: While this phenomenon is universal, the frequency varies significantly by model (Figure cite132†13(b) ). Mistral Large (24.2%) and Llama 3.3 70B (21.7%) latch most often to incorrect entities, indicating weaker discrimination between relevant and irrelevant chemical scaffolds. They are followed by GPT-4o (19.1%) and DeepSeek R1 (18.6%). GPT-5 latches the least frequently (11.1%), showcasing superior understanding of texts and questions.
L403: ### 5.3 Efficiency Analysis
L404: Beyond raw accuracy, the viability of iterative RAG systems in production environments is governed by their computational efficiency and economic scalability. In this section, we analyze the trade-offs between performance and resource consumption, explicitly mapping the cost-accuracy and dissecting the tension between adaptive reasoning effort and token consumption predictability.
L594: Front-loaded controllers (e.g., Sonnet 4.5, Gemini 2.5 Pro, Claude 3.7) gain early but are drop-sensitive if they over-iterate, while depth-tolerant controllers (e.g., GLM 4.6, Llama 3.3) peak later with smaller late-step losses.
L606: Table S1: Retrieval Coverage gap prevalence by model (%).
L607: Model  | Coverage Gap Rate (%)
L608: GPT-5  | 28.95
L609: Llama 3.3 70B  | 26.73
L610: DeepSeek R1  | 16.86
L611: GLM 4.6  | 15.79
L612: Grok 4 Fast  | 15.53
L613: Mistral Large  | 15.43
L614: GPT-4o  | 13.24
L615: Gemini 2.5 Pro  | 12.98
L616: Claude Sonnet 4.5  | 11.55
L617: Claude 3.7 + Reasoning  | 10.43
L618: Claude 3.7 Sonnet  | 8.51
L619: Average  | 16.00
L620: Table S2: Prevalence $p_{m,f}$ of each failure (% of runs).
L621: Model  | Coverage Gap (%)  | Overconfident (%)  | Distractor Latch (%)
L622: Claude 3.7 Sonnet  | 9.2  | 3.2  | 20.4
L623: Grok 4 Fast  | 12.7  | 17.9  | 16.7
L624: Gemini 2.5 Pro  | 13.9  | 15.5  | 19.1
L625: Mistral Large 2402  | 15.6  | 12.6  | 25.8
L626: GPT-5  | 29.2  | 22.9  | 17.2
L627: Llama 3.3 70B Instruct  | 27.4  | 15.8  | 24.2
L628: Claude 3.7 Sonnet + Reasoning  | 10.7  | 4.5  | 19.1
L629: GLM 4.6  | 16.4  | 29.6  | 16.4
L630: DeepSeek R1  | 18.4  | 33.9  | 21.6
L631: Claude Sonnet 4.5  | 13.6  | 11.5  | 15.0
L632: GPT-4o  | 14.0  | 35.0  | 22.1
L633: Table S3: Impact $\Delta_{m,f}$ of each failure (accuracy drop in percentage points; higher is worse).
L634: Model  | Coverage Gap (pp)  | Overconfident (pp)  | Distractor Latch (pp)
L635: Claude 3.7 Sonnet  | 38.9  | 21.5  | 53.5
L636: Grok 4 Fast  | 12.2  | 21.3  | 43.6
L637: Gemini 2.5 Pro  | 30.8  | 9.0  | 60.8
L638: Mistral Large 2402  | 31.2  | 23.8  | 47.9
L639: GPT-5  | 15.8  | 15.6  | 58.6
L640: Llama 3.3 70B Instruct  | 21.9  | 24.0  | 53.8
L641: Claude 3.7 Sonnet + Reasoning  | 28.7  | $0$  | 46.1
L642: GLM 4.6  | 31.0  | 23.1  | 51.8
L646: #### S1.3.2 Damage Index
L647: 
L648: Finally, we calculate the **Damage Index** ($d_{m,f}=p_{m,f}\times\Delta_{m,f}$), which represents the expected accuracy loss (pp) per question attributable to failure $f$ for model $m$. Intuitively, $d_{m,f}$ combines “how often it happens” with “how much it hurts when it happens.”
L649: 
L650: Table cite223†S4 summarizes the damage index across models. Three patterns stand out:
L651: 
L652:   1. 1.
L653: Distractor-Latch causes the highest expected loss among evaluated failure modes for most models, signaling the need for stronger anchor discipline and distractor filtering late in the chain.
L654: 
L655:   2. 2.
L656: Coverage-Gap is the second critical factor; some models like Llama 3.3 70B ($6.01$ pp), DeepSeek R1 ($5.11$ pp), and GLM 4.6 ($5.07$ pp) are sensitive to this factor, while others like Claude Sonnet 4.5 ($2.00$ pp) and Grok 4 Fast ($1.55$ pp) are more resilient, recovering with minimal hops or parametric knowledge.
L657: 
L658:   3. 3.
L659: Overconfidence (finalizing too early without enough coverage/sufficiency) negatively impacts some models (e.g., GPT-5: $3.58$ pp; GLM 4.6: $3.39$ pp), whereas models like Claude 3.7 + Reasoning show a near-zero damage index, indicating that their occasional early finalizations do not systematically reduce accuracy.
L660: Overall, the observed damage indices suggest incorporating extended controller strategies: (i) reducing distractor latch via coverage-gated retrieval and anchor tracking; (ii) closing coverage gaps earlier for models with high coverage damage; and (iii) installing stricter early-stop guards for models prone to overconfidence.
L661: Table S4: Damage index $d_{m,f}$ (expected pp lost per question) for each model and failure. Higher is worse. Composition failure is omitted by design as it only manifests on incorrect answers.
L662: Model  | Coverage Gap  | Overconfident  | Distractor Latch
L663: Claude 3.7 Sonnet  | 3.6  | 0.7  | 10.9
L664: Grok 4 Fast  | 1.5  | 3.8  | 7.3
L665: Gemini 2.5 Pro  | 4.3  | 1.4  | 11.6
L666: Mistral Large 2402  | 4.9  | 3.0  | 12.4
L667: GPT-5  | 4.6  | 3.6  | 10.1
L668: Llama 3.3 70B Instruct  | 6.0  | 3.8  | 13.0
L669: Claude 3.7 Sonnet + Reasoning  | 3.1  | $0$  | 8.8
L670: GLM 4.6  | 5.1  | 3.9  | 8.5
L671: DeepSeek R1  | 5.1  | 2.2  | 11.9
L672: Claude Sonnet 4.5  | 2.0  | 1.3  | 8.2
L673: GPT-4o  | 3.4  | 0.9  | 11.5
L674: ### S1.4 Query Characteristics
L675: To understand the qualitative differences in how models navigate the search space, we analyze the semantic properties of the queries they generate. We classify each retrieval query using four mutually exclusive quality flags: Vague (lacking concrete targets), Over-Broad (scope is too wide), Off-Topic (targets a subject not required by any oracle hop), and Fusion (attempts to solve multiple oracle hops simultaneously).
L676: Figure cite224†S3 combines our analysis of the accuracy impact (Panel a) and model prevalence (Panel b).
L677: Our analysis of Fusion queries reveals a surprisingly mild impact on performance. As shown in Figure cite224†S3 a, the accuracy gap between runs with and without fusion is relatively small ($78.3\%\to 72.3\%$). This suggests that modern retrievers are increasingly capable of handling compound queries. Figure cite224†S3 b confirms that high-performing reasoning models like DeepSeek R1 and Claude Sonnet 4.5 utilize fusion frequently ($>20\%$ of steps), effectively using it as an efficiency strategy.


## jan29_stdvisioncore

When Iterative RAG Beats Ideal Evidence: A Diagnostic Study in Scientific Multi-hop Question Answering (https://arxiv.org/html/2601.19827v1)
citeturn28475view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19827v1","lineno":130}); Total lines: 744
L122: For instance, financial question answering requires models to combine narrative text with tables and then carry out operations such as comparisons or basic arithmetic. This is the focus of FinQA cite66†Chen et al. (2021) and TAT-QAcite67†Yu et al. (2021) , the latter being larger in scale and intentionally rich in numerical reasoning challenges. In the scientific domain, QASPER cite68†Dasigi et al.
L123: (2021) asks questions about research papers where answers may lie across different sections, meaning that retrieval alone is rarely sufficient. To resolve whether a scientific statement is supported, refuted, or left without evidence, SciFact cite69†Wadden et al. (2020) locate relevant material in multiple abstracts and weigh it together.
L124: In chemistry, recent resources extend beyond generic multi-hop QA: ChemKGMultiHopQA introduces 1–4-hop, multi-document chains with KG supervision, while ChemLit-QA offers expert-validated literature questions tailored for RAG evaluation (cite70†Khodadad et al., 2025a ; cite71†Wellawatte et al., 2025a ). For benchmarking synergizing RAG and reasoning systems, a multi-hop QA dataset that features distinct intermediate answers and clearly defined linking entities provides the most effective evaluation framework.
L125: Although ChemLitQA-multi cite72†Wellawatte et al. (2025b) includes multi-hop questions, they are generally centered on a single shared entity connecting all hops. In contrast, the ChemKGMultiHopQA cite73†Khodadad et al. (2025b) dataset used in this study contains 1186 questions derived from ChemRxiv and enriched with information from PubChem and Wikipedia.
L126: It spans one to four hops and incorporates an automatically constructed knowledge graph with an expert-verified subset, enabling more comprehensive and diverse multi-hop chemical reasoning than both HotpotQA and ChemLitQA.
L127: ### 2.2 Iterative Retrieval-Augmented Generation
L128: Synergized retrieval-augmented generation (RAG) and reasoning has received substantial recent attention (cite58†Gao et al., 2025 ; cite74†Li et al., 2025c ; cite75†Trivedi et al., 2023 ; cite76†Tran et al., 2025 ; cite77†Shao et al., 2023 ), motivated by the need to bring large reasoning models closer to solving complex, real-world questions.
L129: Broadly, these methods fall into two complementary directions: reasoning-enhanced retrieval, where reasoning signals improve what to retrieve (e.g., cite59†Nahid and Rafiei, 2025 ; cite63†Chen et al., 2025 ; cite78†Cheng et al., 2024 ; cite79†Yan et al., 2025 ), and retrieval-enhanced reasoning, where retrieved evidence is repeatedly integrated to strengthen multi-step inference (e.g., cite60†Xu et al., 2024 ; cite61†Li et al., 2025b ; cite62†Wu et al., 2025 ; cite80†Song et al., 2025a ; cite81†Wang et al., 2025 ).
L130: In this landscape, iterative RAG instantiates synergy as explicit retrieve–reason–retrieve loops, where intermediate reasoning artifacts (plans, sub-questions, summaries, self-assessments, or verifiers) actively steer subsequent retrieval and synthesis.
L131: A useful organizing lens is the procedural dynamism taxonomy of cite58†Gao et al. (2025) , which contrasts pre-defined workflows (fixed pre-/post-retrieval reasoning hooks, or hybrid templates) with dynamic workflows in which retrieval and reasoning actions are conditionally triggered by the evolving problem state.
L132: Dynamic workflows tend to be superior in complex or open-world settings because they adapt to emergent task complexity through state-contingent proactivity, reflection, and feedback loops, rather than following a rigid template. Concretely, iterative designs often rely on (i) planning and decomposition mechanisms that decide what to retrieve next and how to aggregate evidence, and (ii) explicit control signals that encode retrieval triggers, relevance, or verification decisions.
L133: For instance, PlanRAG follows an iterative plan-then-retrieve pattern: the model drafts a structured plan, issues targeted queries aligned with that plan, and re-plans as needed until sufficient evidence is gathered (cite82†Lee et al., 2024a ; cite83†Lee et al., 2024b ).
L134: Complementarily, Self-RAG and SmartRAG use explicit prediction and control signals (e.g., special-token style decisions) to represent when to retrieve, whether evidence is relevant, and when to verify or revise (cite84†Asai et al., 2023 ; cite85†Gao et al., 2024 ).
L135: Several recent methods highlight how iterative control and memory within the loop governs performance. ReSP targets multi-hop QA by recording the retrieval trajectory and using a dual-purpose summarizer to compress evidence with respect to both the global question and the current sub-question, mitigating context overload while supporting continued multi-step retrieval (cite86†Jiang et al., 2025 ).
L136: In domain settings with frequent follow-up needs, i-MedRAG operationalizes iteration as a sequence of LLM-generated follow-up questions: each is answered via a conventional RAG call, and the accumulated answers guide subsequent query generation, yielding an interpretable information-seeking chain (cite87†Xiong et al., 2024 ).
L137: Other work focuses on stopping and efficiency within the loop: Probing-RAG uses an auxiliary “prober” over intermediate representations to decide whether more retrieval is needed, reducing redundant steps while maintaining accuracy (cite88†Baek et al., 2025 ).
L138: More agentic frameworks emphasize evidence sufficiency: FAIR-RAG formalizes this by decomposing the question into required findings, identifying evidence gaps, and triggering targeted query refinement until the evidence set is deemed complete for faithful generation (cite89†Asl et al., 2025 ).
L139: Across these approaches, controller design, meaning deciding when to continue retrieving versus finalize an answer, is repeatedly identified as a key driver of iterative gains, motivating hop-aware diagnostics and late-step gating in recent studies (cite90†Park et al., 2025a ; cite86†Jiang et al., 2025 ; cite91†Chu and others, 2025 ).
L140: This is particularly salient in industrial and scientific use cases that require long-range, multi-step reasoning and multi-source evidence integration, where missing an intermediate retrieval step can break the logical chain (cite58†Gao et al., 2025 ).
L141: ## 3 Methodology
L142: 
L143: In this section, we first define our evaluation protocol and the failure mode categories developed for this study. We then describe the Iterative RAG system used for evaluation of synchronized retrieval and reasoning, and the chemistry benchmark that is used as the experimental testbed.
L144: In this section, we present the framework developed to evaluate our main hypothesis. Specifically, we describe the approach used to identify questions that require retrieval, the method employed to simulate an ideal static RAG setup, and the implementation details and parameters for dynamic (iterative) RAG. We then introduce the dataset selected for this evaluation. Finally, we outline the error categories defined for failure mode analysis and the metrics used to assess them.
L145: ### 3.1 Evaluation Framework and Metrics
L146: We evaluate model performance across three distinct configurations to isolate the contributions of parametric memory, ideal evidence, and iterative reasoning. (i) No Context: The model answers the question relying solely on internal parametric knowledge, reflecting the internal knowledge gap of each model.
L147: (ii) Gold Context: An oracle text where the model receives the question and all ground truth paragraphs supporting every reasoning hop (the multi-hop question is generated from that paragraphs), with no further retrieval permitted. Synthesizing the upper band of static retrieval then generation scenario, where the ground truth context is achieved in the retrieval attempt.
L148: (iii) Iterative RAG: The model utilizes our controller to actively retrieve evidence, refine hypotheses, and determine when to stop, subject to a step budget.
L149: The main, questions that we would like to answer here, is that whether providing explicit reasoning opportunity to models during test time – independent of their previous training reasoning fune-tuning –, could provide them the opportunity of outperforming the static ideal retrieval and generation in a domain specific muti-hop reasoning task. And how this observation would relate to models set up and number of hops.


## jan29_stdvisioneval1

When Iterative RAG Beats Ideal Evidence: A Diagnostic Study in Scientific Multi-hop Question Answering (https://arxiv.org/html/2601.19827v1)
citeturn28476view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19827v1","lineno":203}); Total lines: 744
L186: We diagnose stopping logic by flagging: (i) Over-confident Finalize (stopping before covering $\geq 80\%$ of hops despite having insufficient evidence), and (ii) Under-confident Continue (continuing retrieval despite having sufficient evidence).
L187:   * •
L188: 
L189: Procedural Compliance Rate (PCR): To complement Confidence Miscalibration, we introduce PCR to quantify adherence to the instructed verification protocol. It measures the proportion of known multi-hop questions (correctly answered in No Context) where the model actively verifies its answer by continuing the search beyond the mandatory minimum step ($Steps>1$) rather than lazily finalizing at the first step.
L190: 
L191:   * •
L192: Distractor Latch: This is another process-level metric for measuring unfaithful execution and reasoning drift, capturing cases where the system fixates on near-miss terminology. Distractor Latch is a run-level failure where the system repeatedly locks onto a domain-specific similar but incorrect terminology. In the selected dataset, this manifests as a chemically similar but incorrect scaffold (e.g., retrieving “benzylic” instead of “phenoxyl”).
L193: ##### III. Information Synthesis Diagnostics
L194: 
L195:   * •
L196: Composition Failure: Recent multi-hop evaluations show that models can still answer incorrectly despite having sufficient retrieved evidence, and diagnostic analyses further report final-hop entity substitutions from entity confusion, motivating a metric that isolates synthesis failures from retrieval failures (cite101†Song et al., 2025b ).
L197: Occurs when the correct entity/claim is present in the retrieved evidence, yet the final answer selects the wrong entity, provides a vague paraphrase, or merges competing entities. This isolates synthesis failures from retrieval failures.
L198:   * •
L199: Sufficiency Score ($\hat{s}$): RAG evaluation frameworks emphasize claim-level faithfulness/attribution and explicitly distinguish retrieval misses from generator-side synthesis errors that occur even when supporting evidence is present in the retrieved context (cite102†Es et al., 2024 ). Sufficiency Score quantifies the fraction of sentences in the partial answers that are supported by at least one retrieved snippet.
L200: This measure reflects the extent to which generated claims are grounded in the provided evidence.
L201: ### 3.2 Experimental Setup
L202: 
L203: To form our analysis, we implement a training-free, iterative retrieval-augmented framework designed to handle the heterogeneity and complexity of chemical reasoning. The system is composed of a specialized chemistry benchmark and a modular controller that alternates between retrieval and planning.
L204: #### 3.2.1 Dataset and Indexing
L205: As explained earlier, to properly evaluate our hypothesis multiple criteria where required in identifying a suitable dataset for this experiment: multi-hop reasoning, domain specificity, and dependency on retrieval. These constraints made our search space relatively narrow. Consequently, benchmarks designed to evaluate reasoning capability independently of retrieval (e.g., OlympicArena (cite103†Huang et al., 2024 ), Humanity’s Last Exam (cite104†Phan et al., 2025 )) were excluded.
L206: Older benchmarks such as HotpotQA (cite64†Yang et al., 2018 ) were also not ideal, as they have been widely leaked into training corpora and contain only a limited subset of questions that genuinely require retrieval to address knowledge gaps. To minimize the impact of answer variability and dependency on writing style, we restricted our search to multi-hop QA datasets with short answers.
L207: Furthermore, to enable comprehensive failure mode analysis, we added the requirement that the dataset must provide all sub-questions, intermediate answers, and explicit connections between reasoning hops. Finally, we required the dataset to focus on a specific domain rather than general multi-hop QA. After applying these conditions, ChemKGMultihopQA cite73†Khodadad et al. (2025b) emerged as the benchmark that best satisfied our requirements, and we selected it as the experimental testbed for this study.
L208: ChemKGMultihopQA is a multi-hop chemistry dataset, constructed from heterogeneous sources including ChemRxiv, PubChem, and Wikipedia. We selected this dataset because it requires traversing distinct documents (1–4 hops) to answer questions, ensuring that the model must actively gather evidence rather than performing single-step lookups.
L209: In addition, the answers in this dataset are short and make it easier to verify whether the answer is correct and minimize the dependency on more complex measures for answer verification. Furthermore, the dataset is relatively new with relatively low reported accuracy of evaluated models with parametric memory. This reflects that the questions are hard for the models to be answeredwithout access to external tool or additional explicit reasoning or retrieval opportunity.
L210: Also, availability of required reasoning path with middle hops details opens up the opportunity of detailed failure modes diagnosis.
L211: To prepare the corpus, we normalize text (Unicode canonicalization, whitespace cleanup) and segment documents into overlapping sliding windows of 220 words with a 50-word overlap. This window size is large enough to capture complete definitions or property mentions while avoiding the dilution of retrieval signals. We embed chunks using a chemistry-specific sentence encoder, BASF-AI/ChEmbed cite105†Kasmaee et al.
L212: (2025) , which provides superior retrieval recall for scientific nomenclature compared to generic models.
L213: #### 3.2.2 Synergized Reasoning and Retrieval Implementation
L214: 
L215: Our system (Figure cite106†1 ) functions as an orchestrator that coordinates three core responsibilities: Retrieval (finding evidence), Planning (deciding the next atomic step), and Orchestration (managing the loop). To enforce discipline, the process operates under a fixed budget of maximum 5 retrieval steps.
L216: ##### Step Definition and Loop.
L217: We define a single “step” as one distinct retrieval action. Therefore, a model that takes 1 step performs exactly one retrieval query and immediately generates a final answer. A model that takes 5 steps performs five sequential retrieval rounds before finalizing. The process begins with a mandatory first retrieval (Step 1) based on the user’s initial question. Upon receiving the top-10 passages from Step 1, the planner enters the loop and must choose exactly one of two actions:
L218: 
L219:   * •
L220: Retrieve (Step $K+1$): If knowledge gaps remain, the planner formulates a new sub-query targeting the next logical hop (e.g., asking for a property of a compound identified in Step $K$).
L221: 
L222:   * •
L223: 
L224: Finalize: If the planner decides that sufficient evidence has been gathered, it triggers a conservative composer that answers strictly from the provided passages with citations.
L225: ##### Partial Answer State.
L226: To maintain reasoning continuity, the system requires the generation of a Partial Answer before formulating a new query. We define the “Step $K$ Partial Answer” as the hypothesis generated after the model observes the query and passages from Step $K$. Although this generation technically occurs at the beginning of the prompt for Step $K+1$, it represents the state of knowledge derived from Step $K$.
L227: This summary acts as a communication channel (cite107†Yang et al., 2024 ), explicitly stating what has been confirmed to guide the subsequent retrieval.


## jan29_stdvisioneval2

When Iterative RAG Beats Ideal Evidence: A Diagnostic Study in Scientific Multi-hop Question Answering (https://arxiv.org/html/2601.19827v1)
citeturn28477view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19827v1","lineno":236}); Total lines: 744
L226: To maintain reasoning continuity, the system requires the generation of a Partial Answer before formulating a new query. We define the “Step $K$ Partial Answer” as the hypothesis generated after the model observes the query and passages from Step $K$. Although this generation technically occurs at the beginning of the prompt for Step $K+1$, it represents the state of knowledge derived from Step $K$.
L227: This summary acts as a communication channel (cite107†Yang et al., 2024 ), explicitly stating what has been confirmed to guide the subsequent retrieval.
L228: ##### Context Management.
L229: To prevent context dilution as steps increase, the planner receives a curated evidence view rather than the full history. At any given Step $K$, the model sees: 1. All passages from the current retrieval (Step $K$) in full (top-10). 2. A compact selection from previous steps (up to the 2 best passages from each Step $1\dots K-1$).
L230: This ensures that even at the step budget limit, the model processes a focused context of approximately 18 passages, preventing older information from overwhelming the latest evidence. Furthermore, partial answers and previous queries along with original question and the step number is passed to the model to make decision.
L231: #### 3.2.3 Correctness and Difficulty
L232: Given the complexity of chemical nomenclature, exact string matching is insufficient. We verify answers using an LLM-as-a-judge (GPT-5-mini) protocol. The evaluation prompt (see cite108†S11 ) is designed to treat aliases, synonyms, molecular formulas, and IUPAC names as identical to the canonical answer. In the Iterative RAG setting, models may include brief explanations; such responses are considered correct if the final answer string is present as the specific final output.
L233: This verifier is the same verifier used in cite73†Khodadad et al. (2025b) that introduced the paper.
L234: Figure 1: The Iterative RAG System: A training-free controller alternates between targeted retrieval and partial answer updates.
L235: ## 4 Results
L236: 
L237: Table 1: Per-mode accuracy and average output length (in tokens), reported by metric, under three conditions: parametric memory only (No Context), access to full oracle evidence (Gold Context), and Iterative RAG with synchronized retrieval and reasoning.
L238:  | Accuracy (%)  | Average Output Tokens
L239: Model  | No Ctx  | Gold Ctx  | Iter. RAG  | No Ctx  | Gold Ctx  | Iter. RAG
L240: OpenAI GPT-4o  | 32.29  | 56.32  | 81.96  | 9  | 10  | 448.63
L241: OpenAI GPT-5  | 45.11  | 71.68  | 80.86  | 1565.48  | 713.41  | 5592.61
L242: Anthropic Claude 3.7 Sonnet (Reasoning)  | 39.80  | 73.27  | 86.09  | 1777  | 715  | 4309.00
L243: Anthropic Claude 3.7 Sonnet (Standard)  | 37.52  | 68.13  | 84.49  | 30  | 30  | 714.73
L244: DeepSeek R1  | 39.04  | 72.51  | 82.29  | 162  | 573  | 3671.38
L245: Mistral Large 2402  | 32.29  | 72.60  | 75.30  | 13  | 14  | 513.13
L246: Meta Llama 3.3 70B Instruct  | 25.13  | 53.54  | 70.40  | 11  | 11  | 428.63
L247: Google Gemini 2.5 pro  | 41.27  | 73.85  | 84.40  | 1733.71  | 1183.81  | 7214.59
L248: Anthropic Claude 4.5 Sonnet  | 40.02  | 73.85  | 87.68  | 683.61  | 552.10  | 3524.80
L249: Z.ai GLM 4.6  | 35.49  | 72.51  | 78.67  | 3071.39  | 751.8  | 4303.75
L250: Grok 4 Fast  | 40.85  | 72.26  | 77.66  | 2738.14  | 780.40  | 5292.99
L251: Table cite109†1 shows the results under three setups: No Context, Gold Context, and Iterative RAG. Figure cite110†2 illustrates the Gaussian distributions of observed accuracy across these three setups aggregated over all evaluated models. Horizontal bars indicate pairwise $t$-test comparisons of accuracy, showing that the observed trends are consistent across models. Performance is weak in the No-Context condition ($37.16\pm 5.54\%$). Providing Gold Context substantially improves accuracy ($69.14\pm 7.22\%$).
L252: Iterative RAG, which couples retrieval with stepwise reasoning, yields further gains: ($80.89\pm 5.8\%$); even the weakest Iterative RAG model, Llama 3 (cite111†et al., 2024 ), performs nearly as well as the best Gold Context model (Gemini 2.5 Pro or Claude Sonnet 4.5) (cite112†Gemini, 2025 ; cite113†Anthropic, 2025b ), and the top Iterative RAG model (Claude Sonnet 4.5) surpasses the best Gold Context result by 13.83 percentage points. All differences are reported in percentage points (pp) in this study.
L253: cite114†Image: Refer to caption Figure 2: Models’ accuracy Distribution of models’ accuracy in three setups of No Context (Parametric memory), Gold context, and Iterative retrieval and reasoning, shown in blue, red and green, respectively. Horizontal bars shows the results of t-test statistical analysis (Significance: *** p<0.001, , ** p<0.01)
L254: Moving from the parametric memory baseline (No Context) to ideal retrieval (Gold Context) yields substantial accuracy gains across all architectures and training set ups. This reflects the importance of retrieval in models performance in this scientific multi-hop reasoning task. Synchronizing retrieval and reasoning (iterative RAG), yielded even more dramatic performance shift, consistently outperforming the Gold Context static retrieval setup.
L255: For instance, GPT-4o (cite115†OpenAI, 2024a ) jumps from 32.29% (No Context) to 81.96% (Iterative RAG), a massive 49.67 pp gain, significantly exceeding the 24.03 pp gain achieved by providing Gold Context. Similarly, Claude Sonnet 4.5 sees its performance more than double, rising from 40.02% to 87.68%.
L256: This indicates that for complex multi-hop tasks, the process of active information retrieval and stepwise state tracking is often more valuable than being provided with the correct supporting passages achievable in an ideal static RAG.
L257: When isolating the specific gains from Gold Context to Iterative RAG, we observe distinct behaviors. On average, non-reasoning models gain 15.39%, whereas reasoning models gain 9.67%. However, the non-reasoning group exhibits high variance: GPT-4o achieves the largest relative gain of 25.64%, while Mistral Large (cite116†AI, 2024b ) shows the smallest increase (2.70%).
L258: This suggests that iterative retrieval acts as a critical scaffold for models with weaker static context utilization (like GPT-4o), whereas strong non-reasoning models like Mistral Large maximize the Gold Context effectively, leaving less marginal utility for the iterative process.
L259: Nevertheless, reasoning-optimized models still derive consistent value; for example, Claude Sonnet 4.5 improves by 13.83 pp, confirming that structured iteration helps narrow the search space even for the most capable reasoning engines.


## jan29_stdvisionsettingsroute

When Iterative RAG Beats Ideal Evidence: A Diagnostic Study in Scientific Multi-hop Question Answering (https://arxiv.org/html/2601.19827v1)
citeturn28478view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19827v1","pattern":"5.3.1"}); Total lines: 744
L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Works L18:     1. cite8†2.1 Datasets for Multi-hop Reasoning L19:     2. cite9†2.2 Iterative Retrieval-Augmented Generation L20:   4. cite10†3 Methodology L21:     1. cite11†3.1 Evaluation Framework and Metrics L22:       1. cite12†Difficulty Stratification. L23:       2. cite13†3.1.1 Diagnostic Suite L24:         1. cite14†I. Evidence Acquisition Diagnostics (Retrieval Quality) L25:         2. cite15†II. Strategic Control Diagnostics (Planning & Adherence) L26:         3. cite16†III. Information Synthesis Diagnostics L27:     2. cite17†3.2 Experimental Setup L28:       1. cite18†3.2.1 Dataset and Indexing L29:       2. cite19†3.2.2 Synergized Reasoning and Retrieval Implementation L30:         1. cite20†Step Definition and Loop. L31:         2. cite21†Partial Answer State. L32:         3. cite22†Context Management. L33:       3. cite23†3.2.3 Correctness and Difficulty L34:   5. cite24†4 Results L35:     1. cite25†4.1 Decomposing Performance: The "Synchronized" Advantage L36:     2. cite26†4.2 Stability Analysis: Recoveries vs. Regressions L37:     3. cite27†4.3 The Cost of Retrieval: Parametric Memory Suppression L38:     4. cite28†4.4 Portion of Unanswered Questions L39:   6. cite29†5 Analysis L40:     1. cite30†5.1 Dynamics of Iterative Utilization L41:       1. cite31†5.1.1 Mechanism of Control: Self-Correction via Anchor Propagation L42:       2. cite32†5.1.2 Step-Count Distribution and Model Strategy L43:     2. cite33†5.2 Failure Modes in Iterative RAG L44:       1. cite34†5.2.1 Retrieval Coverage Gaps: The Prerequisite for Reasoning L45:       2. cite35†5.2.2 Evidence Sufficiency vs. Retrieval Coverage L46:       3. cite36†5.2.3 Confidence Miscalibration: Stopping Too Early or Too Late L47:       4. cite37†5.2.4 Composition Failure: The Synthesis Bottleneck L48:       5. cite38†5.2.5 Distractor Latch: The Retrieval Trap L49:     3. cite39†5.3 Efficiency Analysis L50:       1. cite40†5.3.1 The Trade-off: Adaptivity vs. Predictability L51:     4. cite41†5.4 Adherence and Controllability L52:       1. cite42†Success Rate of Compliance Attempts L53:   7. cite43†6 Discussion L54:   8. cite44†7 Conclusion L55:   9. cite45†References L56:   10. cite46†S1 Appendix L57:     1. cite47†S1.1 Extended Literature Review L58:     2. cite48†S1.2 Performance and Token Utilization L59:     3. cite49†S1.3 Detailed Failure Mode Analysis L60:       1. cite50†S1.3.1 Prevalence and Impact L61:       2. cite51†S1.3.2 Damage Index L62:     4. cite52†S1.4 Query Characteristics L63:     5. cite53†S1.5 Case Studies and System Prompts L64: cite54†License: CC BY 4.0†info.arxiv.org L65: 
L66: arXiv:2601.19827v1 [cs.CL] 27 Jan 2026
L67: # When Iterative RAG Beats Ideal Evidence: A Diagnostic Study in Scientific Multi-hop Question Answering
L68: Mahdi Astaraki astarakm@mcmaster.ca Affiliation: Department of Computational Science and Engineering, McMaster University, Canada Affiliation: BASF Canada Inc., Canada    Mohammad Arshi Saloot mohammad.arshi-saloot@basf.com Affiliation: BASF Canada Inc., Canada    Ali Shiraee Kasmaee shiraeea@mcmaster.ca Affiliation: BASF Canada Inc., Canada    Hamidreza Mahyar mahyarh@mcmaster.ca Affiliation: Department of Computational Science and Engineering, McMaster University, Canada    Soheila Samiee soheila.samiee@basf.com ^{†}^{†}thanks: Corresponding author.
L69: Affiliation: BASF Canada Inc., Canada
L70: ###### Abstract
L71: Retrieval Augmented Generation (RAG) is widely used to extend large language models (LLMs) beyond their parametric knowledge, yet it remains unclear when iterative retrieval-reasoning loops meaningfully outperform traditional static RAG, particularly in scientific domains where multi hop reasoning, sparse domain knowledge, and heterogeneous evidence impose substantial complexity.
L72: This study provides the first controlled, mechanism level diagnostic evaluation of whether synchronized iterative retrieval and reasoning can surpass even an idealized static upper bound (Gold-Context) RAG.
L145: ### 3.1 Evaluation Framework and Metrics
L149: The main, questions that we would like to answer here, is that whether providing explicit reasoning opportunity to models during test time – independent of their previous training reasoning fune-tuning –, could provide them the opportunity of outperforming the static ideal retrieval and generation in a domain specific muti-hop reasoning task. And how this observation would relate to models set up and number of hops.
L150: ##### Difficulty Stratification.
L151: 
L152: To characterize model performance across complexity levels, we define questions as: Easy: Answered correctly by majority of models (2 or less models made mistake out of 11 tested models). Medium: Answered incorrectly by around half of the evaluated models (5 - 7 models). Hard: Answered incorrectly by majority of models (9 to 11).
L153: #### 3.1.1 Diagnostic Suite
L154: To attribute failure modes to specific components (retrieval, reasoning, or control), we audit every iterative run using three families of diagnostics. Since the selected database, provide the oracle hops, their path and gold context for each hop, in addition to the questions, answers and corpus; detailed evaluation of models performance and their reasoning path is possible.
L403: ### 5.3 Efficiency Analysis
L414: The Premium Frontier: The Claude family (Sonnet 3.7, 4.5) and Gemini 2.5 Pro push the accuracy ceiling ($\geq 84\%$). Notably, Claude Sonnet 4.5 appears to be the most capable model, surpassing Claude 3.7 + Reasoning in accuracy while incurring lower costs ($\approx\$110$ vs. $\$140$), indicating algorithmic improvements in efficiency over the brute-force “extended thinking” approach.
L415: 
L416:   * •
L417: Inefficiency Traps: Mistral Large stands out as an outlier in inefficiency, with costs exceeding $\$100$ (comparable to Gemini/Claude) but accuracy lingering near $75\%$. This highlights that parameter count or generation pricing does not strictly correlate with reasoning capability in iterative settings.
L418: 
L419: Figure 14: Iterative RAG Cost vs Accuracy per model.
L420: #### 5.3.1 The Trade-off: Adaptivity vs. Predictability
L421: 
L422: A central challenge in deploying reasoning-heavy models is managing the tension between the ability to "think longer" on complex problems (Adaptivity) and the requirement for stable system latency (Predictability). Figure cite134†15 visualizes this trade-off by mapping models along two dimensions:
L423: 
L424:   * •
L425: Token Scaling Factor ($S$): This metric measures how much a model increases its computational effort when faced with harder problems. It is calculated as the ratio of the average token count for hard questions ($Q_{hard}$, where 9-11 models failed) to easy questions ($Q_{easy}$, where 0-2 models failed):
L426: 
L427:  | $$S=\frac{\mu_{tokens}(Q_{hard})}{\mu_{tokens}(Q_{easy})}$$  |  | (3)
L428: 
L429: A value of $2.0\times$ implies the model doubles its generation length for difficult queries.
L430: 
L431:   * •
L432: Token Usage Consistency ($C$): This metric quantifies the "noise" or volatility in output length within similar difficulty levels. It is defined as the mean Coefficient of Variation (CV) across difficulty buckets ($D=\{easy,medium,hard\}$):
L433: 
L434:  | $$CV=\frac{1}{3}\sum_{d\in D}\left(\frac{\sigma_{tokens}(Q_{d})}{\mu_{tokens}(Q_{d})}\times 100\right)$$  |  | (4)
L435: 
L436: Lower values indicate highly predictable latency profiles, while higher values signal erratic generation lengths.
L603: #### S1.3.1 Prevalence and Impact
L604: 
L605: First, we analyze **Prevalence** ($p_{m,f}$), which measures how often a specific failure occurs. Table cite220†S1 highlights the frequency of Retrieval Coverage Gaps, while Table cite221†S2 details the prevalence of Overconfidence and Distractor Latching. Second, we evaluate **Impact** ($\Delta_{m,f}$), quantifying the penalty—specifically, the drop in accuracy (in percentage points) when a failure is present compared to when it is absent (Table cite222†S3 ).
L646: #### S1.3.2 Damage Index
L647: 
L648: Finally, we calculate the **Damage Index** ($d_{m,f}=p_{m,f}\times\Delta_{m,f}$), which represents the expected accuracy loss (pp) per question attributable to failure $f$ for model $m$. Intuitively, $d_{m,f}$ combines “how often it happens” with “how much it hurts when it happens.”
L649: 
L650: Table cite223†S4 summarizes the damage index across models. Three patterns stand out:
L651: 
L652:   1. 1.
L653: Distractor-Latch causes the highest expected loss among evaluated failure modes for most models, signaling the need for stronger anchor discipline and distractor filtering late in the chain.
L654: 
L655:   2. 2.
L656: Coverage-Gap is the second critical factor; some models like Llama 3.3 70B ($6.01$ pp), DeepSeek R1 ($5.11$ pp), and GLM 4.6 ($5.07$ pp) are sensitive to this factor, while others like Claude Sonnet 4.5 ($2.00$ pp) and Grok 4 Fast ($1.55$ pp) are more resilient, recovering with minimal hops or parametric knowledge.
L657: 
L658:   3. 3.
L659: Overconfidence (finalizing too early without enough coverage/sufficiency) negatively impacts some models (e.g., GPT-5: $3.58$ pp; GLM 4.6: $3.39$ pp), whereas models like Claude 3.7 + Reasoning show a near-zero damage index, indicating that their occasional early finalizations do not systematically reduce accuracy.
L660: Overall, the observed damage indices suggest incorporating extended controller strategies: (i) reducing distractor latch via coverage-gated retrieval and anchor tracking; (ii) closing coverage gaps earlier for models with high coverage damage; and (iii) installing stricter early-stop guards for models prone to overconfidence.
L661: Table S4: Damage index $d_{m,f}$ (expected pp lost per question) for each model and failure. Higher is worse. Composition failure is omitted by design as it only manifests on incorrect answers.
L662: Model  | Coverage Gap  | Overconfident  | Distractor Latch
L663: Claude 3.7 Sonnet  | 3.6  | 0.7  | 10.9
L664: Grok 4 Fast  | 1.5  | 3.8  | 7.3
L665: Gemini 2.5 Pro  | 4.3  | 1.4  | 11.6
L666: Mistral Large 2402  | 4.9  | 3.0  | 12.4
L667: GPT-5  | 4.6  | 3.6  | 10.1
L668: Llama 3.3 70B Instruct  | 6.0  | 3.8  | 13.0
L669: Claude 3.7 Sonnet + Reasoning  | 3.1  | $0$  | 8.8
L670: GLM 4.6  | 5.1  | 3.9  | 8.5
L671: DeepSeek R1  | 5.1  | 2.2  | 11.9
L672: Claude Sonnet 4.5  | 2.0  | 1.3  | 8.2
L673: GPT-4o  | 3.4  | 0.9  | 11.5
L674: ### S1.4 Query Characteristics
L675: To understand the qualitative differences in how models navigate the search space, we analyze the semantic properties of the queries they generate. We classify each retrieval query using four mutually exclusive quality flags: Vague (lacking concrete targets), Over-Broad (scope is too wide), Off-Topic (targets a subject not required by any oracle hop), and Fusion (attempts to solve multiple oracle hops simultaneously).
L676: Figure cite224†S3 combines our analysis of the accuracy impact (Panel a) and model prevalence (Panel b).
L677: Our analysis of Fusion queries reveals a surprisingly mild impact on performance. As shown in Figure cite224†S3 a, the accuracy gap between runs with and without fusion is relatively small ($78.3\%\to 72.3\%$). This suggests that modern retrievers are increasingly capable of handling compound queries. Figure cite224†S3 b confirms that high-performing reasoning models like DeepSeek R1 and Claude Sonnet 4.5 utilize fusion frequently ($>20\%$ of steps), effectively using it as an efficiency strategy.
L678: In contrast, Over-Broad queries impose a consistent penalty, dropping performance from 78.0% to 70.5%, likely due to noisy contexts diluting the signal. Panel b highlights that non-reasoning models generate over-broad queries less frequently than models like Mistral Large or GPT-4o. Vague queries represent a clearer failure of intent formulation, leading to a significant accuracy drop ($77.5\%\to 66.0\%$). Finally, Off-Topic queries are the most detrimental, reducing accuracy to 59.2%.
L679: Although rare ($<4\%$ for most models), GPT-5 and Gemini 2.5 Pro exhibit slightly higher rates of off-topic drift.
L680: (a) Impact on Accuracy: Vague and Off-Topic queries cause the steepest drops ($>10$ pp).
L681: 
L682: (b) Prevalence by Model: Reasoning models (left) favor Fusion; Standard models (right) prone to Over-Broad.
L683: Figure S3: Query Quality Analysis. We diagnose query intent using four flags. Panel (a) shows that while Fusion is benign (small accuracy drop), Vague and Off-Topic queries are destructive. Panel (b) reveals that reasoning-optimized models leverage Fusion as an efficiency tool, whereas standard models struggle with Over-Broad queries.


## jan29_stdvisionnecessary3

When Iterative RAG Beats Ideal Evidence: A Diagnostic Study in Scientific Multi-hop Question Answering (https://arxiv.org/html/2601.19827v1)
citeturn28479view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19827v1","lineno":272}); Total lines: 744
L264: For non-reasoning models, the No-Context and Gold-Context settings typically require only the final answer string; by design, Iterative RAG additionally permits partial answers and cross step state, which increases token usage. Within this group, Llama uses the fewest tokens, whereas Claude 3.7 Sonnet (Standard) uses the most. This increase is expected, as iterative setups trade tokens for improved grounding and accuracy.
L265: ### 4.1 Decomposing Performance: The "Synchronized" Advantage
L266: While aggregate metrics indicate strong performance, Figure cite118†3 decomposes the problem space into four mutually exclusive categories to reveal how each model achieves its final accuracy.
L267: The rows sum to 100%, partitioning the dataset into: (i) Parametric Memory Wins (solved by internal knowledge alone), (ii) Optimum Retrieval Wins(unlocked only when ideal evidence is provided statically), (iii) Synchronized retrieval and reasoning Wins (solved only via Iterative RAG, failing under both No Context and Gold Context), and (iv) not solved (failed in all settings).
L268: This partition reveals a critical finding: Iterative RAG does not simply subsume Gold Context; it solves a distinct class of problems. The "Synchronized Retrieval" column represents questions where static evidence is insufficient, and the model explicitly requires stepwise navigation to derive the answer.
L269: 
L270:   * •
L271: High-Value Scaffolding for Non-Reasoning Models: Non-reasoning models, such as Llama 3.3 70B and GPT-4o, exhibit the largest "Iterative-Exclusive" shares (25.6% and 27.8% respectively). For these models, the iterative process acts as a necessary scaffold, allowing them to solve over a quarter of the dataset that they could not handle even with perfect static evidence.
L272: 
L273:   * •
L274: Hidden Volatility in Strong Models: The figure exposes trade-offs hidden by the net accuracy scores. For instance, Mistral Large 2402 shows 13.8% in the "Iterative-Exclusive" column, meaning it successfully reasoned through many hard problems that Gold Context failed to solve. However, its net gain in Table cite109†1 is only about 2.7%.
L275: This discrepancy implies a high regression rate: while iteration enables the model to solve 13.8% of new hard cases, it simultaneously loses the ability to solve approximately 11% of cases that could have been addressed in a single static run under ideal retrieval conditions.
L276: Thus, Figure cite118†3 clarifies that the benefit of Iterative RAG is orthogonal to Gold Context: it unlocks complex reasoning chains (Column 3) but introduces a stability risk that varies by model. The share of not solved questions also varies appreciably across models. Claude Sonnet 4.5 and Gemini 2.5 Pro leave relatively few questions unresolved (about 7–8%), whereas Llama 3.3 70B Instruct, Grok 4 Fast, and GPT-4o retain larger unsolved portions ($\approx$11–18%).
L277: Figure 3: Partition of Solvability. This heatmap classifies correct answers by the necessary condition for success: internal knowledge (Parametric), static evidence (Gold-Dependent), or dynamic retrieval (Iterative-Exclusive).
L278: ### 4.2 Stability Analysis: Recoveries vs. Regressions
L279: To investigate the volatility identified in the solvability partition, we analyze the specific trade-offs between static and dynamic setups. As shown previously in Table cite109†1 , all models benefit from Iterative RAG relative to both No Context and Gold Context. Nevertheless, iteration does not dominate everywhere: there remains a subset of questions answered correctly under Gold but not under Iterative RAG.
L280: Figure cite119†4 quantifies this trade-off by contrasting recoveries (Gold incorrect $\rightarrow$ Iterative correct) with regressions (Gold correct $\rightarrow$ Iterative incorrect).
L281: Mistral Large 2402 exhibits many recoveries but also many regressions, yielding the lowest net gain (approximately $+33$). In contrast, the other non-reasoning models GPT–4o and Llama 3.3 70B Instruct achieve the largest net gains, followed by Claude 3.7 Sonnet (standard). Among all models, Claude Sonnet 4.5 has the fewest regressions.
L282: The dominant pattern is that iteration recovers many questions that static Gold Context fails to resolve, confirming that interleaving retrieval with reasoning adds capability rather than merely adding more text.
L283: Figure 4: Recoveries vs. Regressions from Gold Context to Iterative RAG. Green bars count recoveries (Gold incorrect $\rightarrow$ Iterative correct) and red bars count regressions (Gold correct $\rightarrow$ Iterative incorrect) per model; the black line (top) and the condensed panel (bottom) show the net gain questions count (= recoveries $-$ regressions).
L284: The plot quantifies iteration’s overall benefit: models like GPT–4o and Llama 3.3 Instruct post the largest net gains, while Mistral Large 2402 shows the smallest due to higher regressions.


## jan29_stdvisionlast

When Iterative RAG Beats Ideal Evidence: A Diagnostic Study in Scientific Multi-hop Question Answering (https://arxiv.org/html/2601.19827v1)
citeturn28480view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19827v1","lineno":150}); Total lines: 744
L138: More agentic frameworks emphasize evidence sufficiency: FAIR-RAG formalizes this by decomposing the question into required findings, identifying evidence gaps, and triggering targeted query refinement until the evidence set is deemed complete for faithful generation (cite89†Asl et al., 2025 ).
L139: Across these approaches, controller design, meaning deciding when to continue retrieving versus finalize an answer, is repeatedly identified as a key driver of iterative gains, motivating hop-aware diagnostics and late-step gating in recent studies (cite90†Park et al., 2025a ; cite86†Jiang et al., 2025 ; cite91†Chu and others, 2025 ).
L140: This is particularly salient in industrial and scientific use cases that require long-range, multi-step reasoning and multi-source evidence integration, where missing an intermediate retrieval step can break the logical chain (cite58†Gao et al., 2025 ).
L141: ## 3 Methodology
L142: 
L143: In this section, we first define our evaluation protocol and the failure mode categories developed for this study. We then describe the Iterative RAG system used for evaluation of synchronized retrieval and reasoning, and the chemistry benchmark that is used as the experimental testbed.
L144: In this section, we present the framework developed to evaluate our main hypothesis. Specifically, we describe the approach used to identify questions that require retrieval, the method employed to simulate an ideal static RAG setup, and the implementation details and parameters for dynamic (iterative) RAG. We then introduce the dataset selected for this evaluation. Finally, we outline the error categories defined for failure mode analysis and the metrics used to assess them.
L145: ### 3.1 Evaluation Framework and Metrics
L146: We evaluate model performance across three distinct configurations to isolate the contributions of parametric memory, ideal evidence, and iterative reasoning. (i) No Context: The model answers the question relying solely on internal parametric knowledge, reflecting the internal knowledge gap of each model.
L147: (ii) Gold Context: An oracle text where the model receives the question and all ground truth paragraphs supporting every reasoning hop (the multi-hop question is generated from that paragraphs), with no further retrieval permitted. Synthesizing the upper band of static retrieval then generation scenario, where the ground truth context is achieved in the retrieval attempt.
L148: (iii) Iterative RAG: The model utilizes our controller to actively retrieve evidence, refine hypotheses, and determine when to stop, subject to a step budget.
L149: The main, questions that we would like to answer here, is that whether providing explicit reasoning opportunity to models during test time – independent of their previous training reasoning fune-tuning –, could provide them the opportunity of outperforming the static ideal retrieval and generation in a domain specific muti-hop reasoning task. And how this observation would relate to models set up and number of hops.
L150: ##### Difficulty Stratification.
L151: 
L152: To characterize model performance across complexity levels, we define questions as: Easy: Answered correctly by majority of models (2 or less models made mistake out of 11 tested models). Medium: Answered incorrectly by around half of the evaluated models (5 - 7 models). Hard: Answered incorrectly by majority of models (9 to 11).
L153: #### 3.1.1 Diagnostic Suite
L154: To attribute failure modes to specific components (retrieval, reasoning, or control), we audit every iterative run using three families of diagnostics. Since the selected database, provide the oracle hops, their path and gold context for each hop, in addition to the questions, answers and corpus; detailed evaluation of models performance and their reasoning path is possible.
L155: All judgments are made strictly from the provided question, oracle hop path, and retrieval logs without using outside knowledge (See Prompts cite92†S8 , cite93†S9 , and cite94†S10 .).
L156: ##### I. Evidence Acquisition Diagnostics (Retrieval Quality)
L157: 
L158:   * •
L159: Retrieval Coverage Gap: This metric is inspired by the sub-question coverage framework proposed by cite95†Xie et al. (2025) , which evaluates whether retrieved chunks and the final answer collectively cover the facets (sub-questions) required by a complex query, and explicitly distinguishes failures due to missing retrieval evidence versus missing utilization of retrieved evidence.
L160: Building on this idea, we operationalize coverage at the level of oracle reasoning hops: for each oracle hop $k$, we check if any retrieved snippet at any step mentions the hop’s key entity or relationship. If not, the hop is marked as missed. A missed hop indicates the retriever failed to fetch the necessary prerequisite for reasoning.
L161:   * •
L162: 
L163: Query Quality Flags: Multi-hop queries can draw on evidence from multiple steps, which helps reduce missing-information issues, but generating such queries directly with LLMs remains difficult (cite96†Shen et al., 2025 ). To analyze the semantic properties of the generated search intent, we classify each retrieval query using four mutually exclusive flags (For a detailed discussion of the impact, see Appendix cite52†S1.4 ):
L164: 
L165:     * –
L166: 
L167: Vague: The query lacks concrete targets (e.g., “learn more about HAT”).
L168:     * –
L169: 
L170: Over-Broad: The scope is too wide or mixes unrelated facets for the required hop.
L171: 
L172:     * –
L173: 
L174: Fusion: The query attempts to solve multiple oracle hops simultaneously in a single compound query.
L175: 
L176:     * –
L177: 
L178: Off-Topic: The query targets a subject not required by any oracle hop.
L179: ##### II. Strategic Control Diagnostics (Planning & Adherence)
L180: 
L181:   * •
L182: Anchor Carry–Drop: Prior multi-hop RAG work shows that intermediate retrieval and reasoning frequently drift away from intended subgoals (“unfaithful execution”) and can become misaligned with retrieved evidence, motivating fine-grained, process-level evaluation beyond final-answer accuracy alone (cite97†Luo et al., 2026 ; cite98†Wei et al., 2025 ; cite99†Liu et al., 2025 ).
L183: We introduce Anchor Carry–Drop, a process-level drift indicator that detects whether a model preserves salient entities across hops—an essential prerequisite for stable multi-step reasoning in multi-hop RAG. From step $t>1$, if the previous partial answer contains a salient anchor (e.g., a chemical formula), the subsequent query must carry at least one anchor. Failure to do so is flagged as a carry–drop, signaling a loss of working memory.
L184:   * •
L185: Confidence Miscalibration: Following cite100†Yang et al. (2025) , who define the core challenge in multi-round RAG as determining information sufficiency, namely deciding whether the currently retrieved information is adequate to answer the query or whether further retrieval rounds are required, we introduce Confidence Miscalibration to diagnose stopping logic.
L186: We diagnose stopping logic by flagging: (i) Over-confident Finalize (stopping before covering $\geq 80\%$ of hops despite having insufficient evidence), and (ii) Under-confident Continue (continuing retrieval despite having sufficient evidence).
L187:   * •
L188: 
L189: Procedural Compliance Rate (PCR): To complement Confidence Miscalibration, we introduce PCR to quantify adherence to the instructed verification protocol. It measures the proportion of known multi-hop questions (correctly answered in No Context) where the model actively verifies its answer by continuing the search beyond the mandatory minimum step ($Steps>1$) rather than lazily finalizing at the first step.
L190: 
L191:   * •
L192: Distractor Latch: This is another process-level metric for measuring unfaithful execution and reasoning drift, capturing cases where the system fixates on near-miss terminology. Distractor Latch is a run-level failure where the system repeatedly locks onto a domain-specific similar but incorrect terminology. In the selected dataset, this manifests as a chemically similar but incorrect scaffold (e.g., retrieving “benzylic” instead of “phenoxyl”).
L193: ##### III. Information Synthesis Diagnostics
L194: 
L195:   * •
L196: Composition Failure: Recent multi-hop evaluations show that models can still answer incorrectly despite having sufficient retrieved evidence, and diagnostic analyses further report final-hop entity substitutions from entity confusion, motivating a metric that isolates synthesis failures from retrieval failures (cite101†Song et al., 2025b ).
L197: Occurs when the correct entity/claim is present in the retrieved evidence, yet the final answer selects the wrong entity, provides a vague paraphrase, or merges competing entities. This isolates synthesis failures from retrieval failures.
L198:   * •
L199: Sufficiency Score ($\hat{s}$): RAG evaluation frameworks emphasize claim-level faithfulness/attribution and explicitly distinguish retrieval misses from generator-side synthesis errors that occur even when supporting evidence is present in the retrieved context (cite102†Es et al., 2024 ). Sufficiency Score quantifies the fraction of sentences in the partial answers that are supported by at least one retrieved snippet.
L200: This measure reflects the extent to which generated claims are grounded in the provided evidence.
L201: ### 3.2 Experimental Setup
L202: 
L203: To form our analysis, we implement a training-free, iterative retrieval-augmented framework designed to handle the heterogeneity and complexity of chemical reasoning. The system is composed of a specialized chemistry benchmark and a modular controller that alternates between retrieval and planning.
L204: #### 3.2.1 Dataset and Indexing
L205: As explained earlier, to properly evaluate our hypothesis multiple criteria where required in identifying a suitable dataset for this experiment: multi-hop reasoning, domain specificity, and dependency on retrieval. These constraints made our search space relatively narrow. Consequently, benchmarks designed to evaluate reasoning capability independently of retrieval (e.g., OlympicArena (cite103†Huang et al., 2024 ), Humanity’s Last Exam (cite104†Phan et al., 2025 )) were excluded.
