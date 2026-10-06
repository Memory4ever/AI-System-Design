GenProve: Learning to Generate Text with Fine-Grained Provenance (https://arxiv.org/html/2601.04932v1)
citeturn26861view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04932v1","lineno":50}); Total lines: 547
L0: ##### Report GitHub Issue
L1: 
L2: [Button: ×]
L3: 
L4: Title: [Input: Enter title]
L5: 
L6: Content selection saved. Describe the issue below:
L7: 
L8: Description:
L9: 
L10: [Button: Submit without GitHub] [Button: Submit in GitHub]
L11: 
L12: cite0†Back to arXiv L13: 
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Work L18:   4. cite8†3 Dataset L19:     1. cite9†3.1 Overview L20:     2. cite10†3.2 Dataset construction L21:     3. cite11†3.3 Dataset Analysis L22:     4. cite12†3.4 Comparison with Existing Benchmarks L23:   5. cite13†4 Method L24:     1. cite14†4.1 Supervised Fine-Tuning L25:     2. cite15†4.2 GRPO-based Reinforcement Learning L26:       1. cite16†Reward Design. L27:       2. cite17†Reward A: Sentence-matching content similarity. L28:       3. cite18†Reward B: Reference-guided provenance F1. L29:       4. cite19†Composite reward. L30:   6. cite20†5 Experiments L31:     1. cite21†5.1 Experimental Setup L32:     2. cite22†5.2 Main Results L33:     3. cite23†5.3 Ablation Study L34:     4. cite24†5.4 Diagnostic Analysis L35:     5. cite25†5.5 Consistency with Human Evaluation L36:   7. cite26†6 Conclusion L37:   8. cite27†References L38:   9. cite28†A Task Definition L39:   10. cite29†B Additional Details of ReFInE Construction L40:     1. cite30†B.1 Preliminary filtering criteria L41:       1. cite31†Instruction compliance. L42:       2. cite32†Fluency and completeness. L43:       3. cite33†Ethical compliance. L44:       4. cite34†Format validity. L45:     2. cite35†B.2 Expert validation protocol L46:       1. cite36†Evidence sufficiency. L47:       2. cite37†Relation correctness. L48:     3. cite38†B.3 Prompt for GPT-4o Annotation L49:     4. cite39†B.4 Examples of ReFInE Instances L50:     5. cite40†B.5 Additional Dataset Statistics L51:     6. cite41†B.6 Benchmark Comparison Details L52:   11. cite42†C Additional Experimental Details L53:     1. cite43†C.1 Inference Prompt for Provenance-Aware Generation L54:     2. cite44†C.2 LLM Judge for Traceable QA L55:     3. cite45†C.3 Human Evaluation Guidelines L56:       1. cite46†Answer quality (0–5). L57:       2. cite47†Provenance quality (0–5). L58:     4. cite48†C.4 LLM-as-a-Judge Breakdown L59:     5. cite49†C.5 Full Ablation Results L60:     6. cite50†C.6 Human Evaluation Results L61:   12. cite51†D Error Analysis L62:     1. cite52†Unsynchronized Provenance Generation. L63:     2. cite53†Incomplete Provenance Coverage. L64:     3. cite54†Incorrect Provenance Localization. L65:     4. cite55†Incorrect Provenance Type. L66:   13. cite56†E Potential Risks L67:     1. cite57†Over-reliance on provenance signals. L68:     2. cite58†False sense of completeness. L69:     3. cite59†Annotation and evaluation bias. L70:     4. cite60†Computational and deployment considerations. L71: cite61†License: arXiv.org perpetual non-exclusive license†info.arxiv.org L72: 
L73: arXiv:2601.04932v1 [cs.CL] 08 Jan 2026
L74: # GenProve: Learning to Generate Text with Fine-Grained Provenance
L75: 
L76: Jingxuan Wei    Xingyue Wang    Yanghaoyu Liao    Jie Dong    Yuchen Liu    Caijun Jia    Bihui Yu    Junnan Zhu ^{†}^{†}thanks: Corresponding author. Affiliation: MAIS, Institute of Automation, Chinese Academy of Sciences Affiliation: Shenyang Institute of Computing Technology, Chinese Academy of Sciences Affiliation: University of Chinese Academy of Sciences
L77: ###### Abstract
L78: Large language models (LLM) often hallucinate, and while adding citations is a common solution, it is frequently insufficient for accountability as users struggle to verify how a cited source supports a generated claim. Existing methods are typically coarse-grained and fail to distinguish between direct quotes and complex reasoning.
L79: In this paper, we introduce Generation-time Fine-grained Provenance, a task where models must generate fluent answers while simultaneously producing structured, sentence-level provenance triples. To enable this, we present ReFInE (Re lation-aware F ine-grained In terpretability & E vidence), a dataset featuring expert-verified annotations that distinguish between Quotation, Compression, and Inference.
L80: Building on ReFInE, we propose GenProve, a framework that combines Supervised Fine-Tuning (SFT) with Group Relative Policy Optimization (GRPO). By optimizing a composite reward for answer fidelity and provenance correctness, GenProve significantly outperforms 14 strong LLMs in joint evaluation.
L81: Crucially, our analysis uncovers a reasoning gap where models excel at surface-level quotation but struggle significantly with inference-based provenance, suggesting that verifiable reasoning remains a frontier challenge distinct from surface-level citation.
L82: ## 1 Introduction
L83: While LLMs demonstrate impressive fluency, their tendency to hallucinate remains a major barrier to widespread adoption cite62†Fan et al. (2025) . Users need to verify not just whether an answer sounds correct, but exactly where it comes from in the external evidence. To address this issue, current systems typically use Retrieval-Augmented Generation (RAG) or simply add citations to the text cite63†Gao et al. (2023) ; cite64†Li et al. (2024) .
L84: However, these standard approaches often function as black boxes because they provide a list of documents yet fail to specify which exact sentence supports a claim or how that evidence is used. This ambiguity leaves users guessing whether the model is directly quoting a fact, summarizing scattered details, or making a logical inference, which makes verification difficult and inefficient. For rigorous verification, knowing how a model uses evidence (e.g., inferring vs.
L85: quoting) is as important as knowing which document it used.
L86: cite65†Image: Refer to caption Figure 1: Overview of Generation-time Fine-grained Provenance. Given a query and source documents, the model simultaneously produces the answer and structured triples (DocID, SentID, Relation) to explain how the evidence supports each generated sentence.
L87: We advocate for a more transparent approach, which we refer to as Generation-time Fine-grained Provenance. Unlike simple citation generation, this task requires the model to function as a transparent reasoner. For every generated sentence, the model must simultaneously identify the specific supporting source sentence and explicitly classify the evidence usage relation as Quotation, Compression, or Inference (Figure cite66†1 ).
L88: A major obstacle to this goal is the lack of training data. Most existing benchmarks are designed for analysis after generation or lack structured supervision on evidence types cite63†Gao et al. (2023) ; cite67†Zhu et al. (2025) . To bridge this gap, we construct ReFInE (Re lation-aware F ine-grained In terpretability & E vidence). Unlike previous heuristic-based datasets, ReFInE is built via a rigorous human-in-the-loop pipeline where LLM-assisted proposals undergo multi-stage expert verification.
L89: This ensures the dataset accurately captures complex evidence usage patterns, serving as a reliable testbed for transparent generation.
L90: Building on ReFInE, we propose GenProve, a training framework tailored for this objective. We observe that standard SFT is insufficient; models often struggle to balance the fluidity of the answer with the strict structural constraints of provenance triples. GenProve overcomes this by integrating GRPO cite68†Guo et al. (2025) with a novel multi-dimensional reward modeling strategy. Specifically, we design a composite reward that goes beyond simple text quality.
L91: While strictly adhering to the structural constraints learned during SFT, our objective explicitly optimizes for content fidelity and provenance correctness, penalizing hallucinations where the cited evidence does not semantically support the generated claim. This holistic alignment forces the model to treat citation not as a stylistic decoration, but as an intrinsic reasoning constraint.
L92: We evaluate GenProve against 14 strong LLMs. Results show that GenProve establishes a new state-of-the-art, significantly outperforming competitors in both answer quality and provenance accuracy. Crucially, our diagnostic analysis exposes a reasoning gap where models easily master exact Quotation, yet they struggle significantly with Inference. This suggests that the reliability of logical deductions remains a key challenge for future research.
L93: 
L94: Our contributions are summarized as follows:
L95: 
L96:   * •
L97: We define Generation-time Fine-grained Provenance, shifting from coarse document-level citations to sentence-level attribution with explicit relation typing.
L98: 
L99:   * •
L100: 
L101: We release ReFInE, the first expert-annotated QA dataset that provides dense, typed provenance supervision for multi-document generation, enabling rigorous training and evaluation of model interpretability.
L102: 
L103:   * •
L104: We propose GenProve, integrating SFT with GRPO alignment to master structured provenance generation. Experiments demonstrate that GenProve establishes a new state-of-the-art, while our analysis reveals the difficulty of verifying inference-based claims compared to direct quotation.
L105: cite69†Image: Refer to caption Figure 2: The construction pipeline of ReFInE. The process ensures high-quality provenance supervision through three stages: (1) preprocessing, (2) LLM-assisted annotation with filtering, and (3) reconstruction with rigorous human-in-the-loop expert validation to verify evidence sufficiency and relation correctness.
L106: ## 2 Related Work
L107: Citation-Aware Text Generation. Incorporating citations into generated text is a critical step towards verifiable AI. Early approaches focus on stylistic imitation of academic writing cite70†Xing et al. (2020) or utilize post-hoc retrieval to verify generated claims after the fact cite64†Li et al. (2024) ; cite71†Hsu et al. (2024) . With the advent of LLMs, the focus has shifted to RAG. Benchmarks like ALCE cite63†Gao et al.
L108: (2023) have standardized the evaluation of citation quality, emphasizing document recall and precision. However, these methods typically operate at a coarse granularity, retrieving entire documents or passages without pinpointing the specific evidence used. Recent training-based methods cite72†Aly et al. (2024) ; cite73†Slobodkin et al. (2024) attempt to improve robustness by fine-tuning models to cite sources.
L109: However, these approaches are limited by treating citations as untyped pointers (e.g., simply linking to [1]). Our study advances this paradigm by enforcing typed relations, requiring the model to demonstrate an explicit understanding of the semantic relationship between the claim and the evidence, such as whether it is quoting or inferring.
L110: Fine-Grained Provenance & Verification. To improve interpretability, granularity in attribution has evolved from document-level to sentence-level. Previous works like GERE cite74†Chen et al. (2022) and SCIFI cite75†Cao and Wang (2024) explore generating sentence identifiers, while cite76†Kambhamettu et al. (2024) introduce phrase-level links. Most relevant to our work is TROVE cite67†Zhu et al. (2025) , which introduces a comprehensive taxonomy for provenance relations.
L111: We adopt their core taxonomy (Quotation, Compression, Inference) to ensure rigorous classification. However, we explicitly exclude their "Other" category. We omit this label for two reasons: first, it represents a negligible long-tail of the distribution; second, it serves as an ambiguous catch-all bucket. Such undefined signals lack clear semantic boundaries, making them unsuitable optimization targets for precise model alignment.
L112: Furthermore, while TROVE focuses on post-hoc analysis of static text, GenProve targets generation-time provenance. We integrate these fine-grained types directly into the training process, shifting the paradigm from checking after generation to generating with inherent verification.
L113: Reasoning with Evidence. Research studies investigate how LLMs reason with retrieved context. Studies like FRONT cite77†Huang et al. (2024) and SciRGC cite78†Li and Chen (2025) have begun to model the latent reasoning process behind citations, inspired by chain-of-thought prompting. GenProve pushes this direction further by explicitly supervising the Inference relation.
L114: Unlike previous works that often conflate simple retrieval with complex reasoning, our framework distinguishes between surface-level copying and deep synthesis. By optimizing for specific relation types, we evaluate and improve the model’s ability to abstract and deduce information rather than merely retrieving and copying verbatim segments.
L115: ## 3 Dataset
L116: ### 3.1 Overview
L117: We study GenProve, a generation-time fine-grained provenance task where a system produces an answer together with sentence-level evidence links and typed provenance relations. A central obstacle to learning GenProve is the lack of training data that aligns each answer sentence to specific source sentences while also distinguishing how the evidence is used, such as quotation, compression, or inference.
L118: To address this gap, we construct ReFInE, a supervised dataset that provides multi-document inputs and reference answers annotated with structured provenance tags.
L119: Each ReFInE instance pairs a user question with multiple source documents and a reference answer, where every sentence carries a provenance annotation linking it to source sentences via Quotation, Compression, or Inference. We build the dataset through a three-stage pipeline comprising sentence-level preprocessing, GPT-4o–based provenance annotation with human screening, and expert-validated reconstruction into a unified message format. Figure cite79†2 summarizes the construction process.
L120: ### 3.2 Dataset construction
L121: Raw data and sentence-level preprocessing We build ReFInE on top of a public long-form QA corpus with retrieved multi-document evidence cite80†Yehudai et al. (2024) , where each example contains a user question, a set of source documents, and a long-form reference answer (Figure cite79†2 , Stage 1).
L122: For each instance, we treat the user query as the question $Q$, segment the long answer into sentences to obtain a sequence of target sentences $\{t_{1},t_{2},\dots\}$, and segment all source documents into sentences. Each source sentence in $D$ is assigned a unique pair $(\text{Doc\_ID},\text{Sent\_ID})$, which later serves as the indexing scheme for the provenance triples in Eq. cite81†11 .
L123: This stage produces a candidate pool of sentence-level evidence drawn from the source documents, together with a set of target sentences that require provenance labels.
L124: GPT-4o-based provenance annotation and preliminary filtering. Given a question $Q$, a document set $D$, and a target sentence $t_{j}$, we prompt GPT-4o to predict provenance triples. These triples follow the (DocID, SentID, Relation) format, covering Quotation, Compression, and Inference (Figure cite79†2 , Stage 2). This process annotates each sentence independently to form a candidate pool. Next, three annotators screen the outputs for quality. They verify instruction compliance, fluency, and ethical safety.
L125: Crucially, they enforce strict [PROVE] formatting, checking for tag completeness, evidence merging, and index consistency. Violating samples are removed or corrected. Appendix cite30†B.1 details this protocol.
L126: Reconstruction, expert validation, and final formatting. We reconstruct instance-level examples by aggregating sentence-level annotations (Figure cite79†2 , Stage 3). Target sentences are sorted by their original order and concatenated, with each sentence receiving a [PROVE] tag that enumerates its evidence and relations (Eq. cite82†12 ). Subsequently, three experts conduct a second-round validation.
L127: Under a dual-check protocol, they rigorously verify evidence sufficiency and relation correctness (Quotation, Compression, Inference); instances failing either check are revised or discarded. Finally, valid samples are formatted for training: the user message comprises the question $Q$ and documents $D$, while the assistant message contains the long answer $A$ with embedded [PROVE] tags. Appendix cite35†B.2 details this protocol.
L128: ### 3.3 Dataset Analysis
L129: Split composition and relation distribution. ReFInE consists of three subsets that support SFT, RL-based training (GRPO), and held-out evaluation (EVAL), containing 12,540, 5,256, and 4,838 instances, respectively. Figure cite83†3 summarizes the split composition and the relation-type mixture within each subset. The split proportions are 55.4% (SFT), 23.22% (GRPO), and 21.38% (EVAL).
L130: The outer ring further shows that Quotation dominates across all splits, whereas GRPO allocates a larger share to Inference and Compression than EVAL, making it more suitable for optimizing reasoning and abstraction under sentence-level evidence constraints.
L131: Figure 3: Relation-type distribution in ReFInE.
L132: 
L133: Provenance density and corpus-level statistics. In ReFInE, each answer contains 3.96 provenance tags on average, with each tag aggregating 1.98 provenance triples. Full corpus-level statistics are reported in Appendix cite40†B.5 .
L134: ### 3.4 Comparison with Existing Benchmarks
L135: 
L136: Table cite84†4 compares ReFInE with representative citation-aware and provenance benchmarks along axes central to fine-grained accountability, including relation expressivity, provenance granularity, task form, and whether provenance is produced alongside the answer using structured tags.
L137: Fine-grained, typed sentence-level provenance. Many prior benchmarks emphasize attribution but collapse provenance into a single untyped support signal or operate at a coarser granularity, which limits sentence-level inspection and weakens the interpretability of how evidence supports each claim. In contrast, ReFInE annotates each answer sentence with sentence-level evidence links and explicit relation types, enabling relation-aware auditing beyond identifying the source alone.
L138: cite85†Image: Refer to caption Figure 4: The GenProve framework. The model first undergoes SFT for instruction following and format learning. It is then aligned using GRPO with a composite reward mechanism that jointly optimizes for answer fidelity (content similarity reward) and fine-grained provenance accuracy (F1 Reward).
L139: Generation-time supervision. Several settings perform provenance analysis post hoc or append/verify citations in multi-step pipelines. ReFInE instead requires the answer and its provenance to be produced simultaneously, providing direct supervision and evaluation for generation-time provenance-aware decoding. Full benchmark comparison details are provided in Appendix cite41†B.6 .
L140: ## 4 Method
L141: 
L142: We develop GenProve, a two-step training framework that enables a model to generate answers with fine-grained provenance. Given a question $Q$ and a document collection $D=\{d_{1},\dots,d_{m}\}$, the model produces an answer $A=(t_{1},\dots,t_{n})$. Each answer sentence $t_{j}$ is accompanied by a set of provenance triples that identify supporting source sentences in $D$ and their relation types. Figure cite86†4 shows the overall procedure.
L143: ### 4.1 Supervised Fine-Tuning
L144: We treat SFT as a foundational warm-up stage primarily designed to enforce structure adherence. It trains the base model to follow instructions and to emit well-formed provenance annotations together with fluent answers. Let $\mathcal{D}_{\text{SFT}}=\{(Q_{i},D_{i},A^{\mathrm{ref}}_{i})\}_{i=1}^{N}$ denote the training set constructed from ReFInE, where $A^{\mathrm{ref}}_{i}$ is the reference answer annotated with sentence-level provenance.
L145: We fine-tune the model by maximizing the conditional likelihood of the reference output:
L146:  | $$\mathcal{L}_{\text{SFT}}(\theta)=-\sum_{i=1}^{N}\log p_{\theta}\!\left(A^{\mathrm{ref}}_{i}\mid Q_{i},D_{i}\right).$$  |  | (1)
L147: 
L148: This step provides a stable policy initialization that reliably produces syntactically valid provenance tags and on-topic content. Crucially, this structural foundation enables the subsequent RL stage to focus on refining the model’s provenance accuracy rather than struggling with basic formatting errors.
L149: ### 4.2 GRPO-based Reinforcement Learning
L150: 
L151: Reinforcement learning improves provenance accuracy and reduces unsupported statements by optimizing a reward that evaluates both content and provenance. Starting from the SFT policy $\pi_{\theta}$, we sample a group of candidate answers for each input $(Q,D)$ and update the policy using GRPO. The objective maximizes the expected reward:
L152:  | $$\mathcal{J}(\theta)=\mathbb{E}_{(Q,D)\sim\mathcal{D}_{\text{GRPO}}}\Big[\mathbb{E}_{A\sim\pi_{\theta}(\cdot\mid Q,D)}\big[R(A,A^{\mathrm{ref}})\big]\Big].$$  |  | (2)
L153: 
L154: The reward $R(A,A^{\mathrm{ref}})$ aggregates two components: a sentence-matching content reward and a reference-guided provenance F1 reward (Figure cite86†4 ).
L155: #### Reward Design.
L156: 
L157: GenProve computes rewards at sentence granularity by parsing provenance tags and splitting both the generated answer and the reference into sentence units. Let $A=(t_{1},\dots,t_{n})$ and $A^{\mathrm{ref}}=(t^{\mathrm{ref}}_{1},\dots,t^{\mathrm{ref}}_{M})$. We represent both answers as sentence–provenance pairs:
L158: 
L159:  | $$\begin{cases}A=\{(t_{j},P_{j})\}_{j=1}^{n},\\
L160: A^{\mathrm{ref}}=\{(t^{\mathrm{ref}}_{k},P^{\mathrm{ref}}_{k})\}_{k=1}^{M}.\end{cases}$$  |  | (3)
L161: Each $P_{j}$ (or $P^{\mathrm{ref}}_{k}$) is a set of triples of the form $(\mathrm{doc\_id},\mathrm{sent\_id},r)$ with $r\in\{\mathrm{Quotation},\mathrm{Compression},\mathrm{Inference}\}$.
L162: #### Reward A: Sentence-matching content similarity.
L163: 
L164: This reward encourages semantic alignment with the reference while preserving sentence-level structure. For each generated sentence $t_{j}$, we find the best-matching reference sentence by cosine similarity between sentence embeddings produced by a Sentence-Transformer encoder:
L165: 
L166:  | $$k(j)=\arg\max_{k\in\{1,\dots,M\}}\cos\big(\phi(t_{j}),\phi(t^{\mathrm{ref}}_{k})\big).$$  |  | (4)
L167: Here $\phi(\cdot)$ denotes the encoder. If the best cosine score is below a threshold $\tau_{c}$, the reward for this sentence is zero; otherwise we compute ROUGE-L between the matched pair:
L168: 
L169:  | $$\begin{split}r_{\text{sim}}(t_{j})&=\mathbb{I}\Big[\cos\big(\phi(t_{j}),\phi(t^{\mathrm{ref}}_{k(j)})\big)\geq\tau_{c}\Big]\\
L170: &\quad\cdot\mathrm{ROUGE\text{-}L}\big(t_{j},t^{\mathrm{ref}}_{k(j)}\big).\end{split}$$  |  | (5)
L171: 
L172: The content reward is the mean across sentences:
L173:  | $$R_{\text{sim}}(A,A^{\mathrm{ref}})=\frac{1}{n}\sum_{j=1}^{n}r_{\text{sim}}(t_{j}).$$  |  | (6)
L174: #### Reward B: Reference-guided provenance F1.
L175: 
L176: This reward encourages generating correct provenance triples and relation types. To reduce missed provenance, we align sentences inversely. For each reference sentence $t^{\mathrm{ref}}_{k}$, we retrieve the closest generated sentence by cosine similarity:
L177: 
L178:  | $$j(k)=\arg\max_{j\in\{1,\dots,n\}}\cos\big(\phi(t^{\mathrm{ref}}_{k}),\phi(t_{j})\big).$$  |  | (7)
L179: We gate mismatched pairs using a similarity threshold $\tau_{p}$. Given an aligned pair, we compare their provenance sets. Let $I_{k}=P_{j(k)}\cap P^{\mathrm{ref}}_{k}$ denote the set of correctly reproduced provenance triples. We compute sentence-level precision and recall as $\mathrm{Prec}_{k}=|I_{k}|/|P_{j(k)}|$ and $\mathrm{Rec}_{k}=|I_{k}|/|P^{\mathrm{ref}}_{k}|$, and define the provenance score by
L180:  | $$F1_{k}=\frac{2\,\mathrm{Prec}_{k}\,\mathrm{Rec}_{k}}{\mathrm{Prec}_{k}+\mathrm{Rec}_{k}+\epsilon}.$$  |  | (8)
L181: 
L182: The provenance reward averages sentence-level scores over all reference sentences, while gating out mismatched pairs:
L183: 
L184:  | $\begin{aligned} R_{\text{prov}}(A,A^{\mathrm{ref}})=\frac{1}{M}\sum_{k=1}^{M}\mathbb{I}\!\left[\cos\big(\phi(t^{\mathrm{ref}}_{k}),\phi(t_{j(k)})\big)\geq\tau_{p}\right]\cdot F1_{k}.\end{aligned}$  |  | (9)
L185: #### Composite reward.
L186: 
L187: We combine the two components into a single scalar reward:
L188: 
L189:  | $$R(A,A^{\mathrm{ref}})=\alpha\,R_{\text{sim}}(A,A^{\mathrm{ref}})+\beta\,R_{\text{prov}}(A,A^{\mathrm{ref}}),$$  |  | (10)
L190: 
L191: where $\alpha$ and $\beta$ balance content fidelity and provenance correctness. This design penalizes common failure modes shown in Figure cite86†4 , including incorrect relation typing and unsupported or out-of-document provenance.
L192: 
L193: ## 5 Experiments
L194: ### 5.1 Experimental Setup
L195: Models. We evaluate 14 LLMs, covering both open- and closed-source systems. The open-source models include Llama-3.1-8B-Instruct cite87†Grattafiori et al. (2024) , Gemma-3-12B-it cite88†Team et al. (2025a) , Yi-1.5-9B-Chat cite89†Liu et al. () , Qwen3-8B cite90†Yang et al. (2025) , InternLM2.5-7B-Chat cite91†Cai et al. (2024) , Hunyuan-7B-Instruct cite92†Zheng et al. (2025) , Vicuna-7B-v1.5 cite93†Zheng et al. (2023) , Baichuan2-7B-Chat cite94†Yang et al. (2023) , Qwen3-14B cite90†Yang et al. (2025) , GLM-4-9B cite95†GLM et al.
L196: (2024) , and GLM-4.5 cite95†GLM et al. (2024) . The closed-source models include Gemini 2.5 Pro cite96†Comanici et al. (2025) , GPT-5 cite97†Achiam et al. (2024) , and Kimi cite98†Team et al. (2025b) . All models use a unified input format of questions and source documents. The full inference prompt is given in Appendix cite43†C.1 .
L197: Training configuration. GenProve is trained in two steps. For supervised fine-tuning, we start from Qwen3-8B cite90†Yang et al. (2025) and perform full-parameter optimization with AdamW, using a learning rate of $2\times 10^{-5}$, a maximum sequence length of 2048, and gradient accumulation to achieve an effective batch size of 16.
L198: For GRPO alignment, we initialize from the SFT model and continue optimization under the same learning rate and sequence length settings, with temperature set to 1, $\beta=0.02$, and 4 iterations per update. For reward computation, the sentence-matching and provenance-alignment thresholds are set to $\tau_{c}=0.45$ and $\tau_{p}=0.50$, respectively.
L199: Model  | ROUGE-L$\uparrow$  | BLEU$\uparrow$  | METEOR$\uparrow$  | MoverScore$\uparrow$  | Prec.$\uparrow$  | Rec.$\uparrow$  | F1$\uparrow$  | Format (%)$\uparrow$  | LLM-as-judge (1–5)$\uparrow$
L200: Baichuan2-7B cite94†Yang et al. (2023) | 34.68  | 19.41  | 48.08  | 32.03  | 3.22  | 3.41  | 3.04  | 26.60  | 0.78
L201: Vicuna-7b-v1.5 cite93†Zheng et al. (2023) | 38.83  | 24.37  | 50.08  | 34.73  | 9.01  | 5.85  | 6.70  | 92.40  | 1.10
L202: InternLM2.5-7B cite91†Cai et al. (2024) | 47.79  | 30.60  | 53.47  | 43.60  | 12.64  | 13.35  | 11.94  | 80.24  | 1.67
L203: Hunyuan-7B cite92†Zheng et al. (2025) | 39.91  | 24.70  | 43.74  | 32.99  | 22.78  | 22.86  | 21.43  | 90.88  | 1.72
L204: Yi-1.5-9B cite89†Liu et al. () | 48.26  | 30.11  | 47.77  | 43.35  | 20.71  | 22.91  | 20.11  | 96.81  | 1.80
L205: Llama-3.1-8B cite87†Grattafiori et al. (2024) | 47.71  | 26.36  | 42.04  | 41.14  | 21.78  | 20.30  | 20.05  | 99.85  | 2.00
L206: GLM-4-9B cite95†GLM et al. (2024) | 50.33  | 32.62  | 50.00  | 44.93  | 34.57  | 34.12  | 32.79  | 100.0  | 2.16
L207: Qwen3-8B cite90†Yang et al. (2025) | 51.80  | 35.56  | 55.38  | 45.90  | 37.78  | 30.56  | 32.53  | 100.0  | 2.25
L208: Gemma-3-12B cite88†Team et al. (2025a) | 48.97  | 32.13  | 50.80  | 43.79  | 41.06  | 31.11  | 34.03  | 100.0  | 2.47
L209: Qwen3-14B cite90†Yang et al. (2025) | 52.85  | 35.70  | 55.34  | 47.06  | 45.80  | 40.33  | 41.16  | 99.70  | 2.59
L210: GLM-4.5-355B cite95†GLM et al. (2024) | 49.81  | 35.05  | 57.69  | 44.92  | 48.84  | 44.03  | 44.55  | 98.63  | 2.63
L211: Kimi cite98†Team et al. (2025b) | 49.33  | 31.24  | 51.56  | 43.84  | 31.55  | 32.09  | 29.70  | 99.09  | 2.20

