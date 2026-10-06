# Exact-v1 necessary primary excerpts — 2601.19773

Preserved original responses; local L labels are scoped to each response. No revised-version or unrelated appendix sweep.

## Original response 1: jan29_stdnext5head

Strong Reasoning Isn’t Enough: Evaluating Evidence Elicitation in Interactive Diagnosis (https://arxiv.org/html/2601.19773v1)
citeturn28451view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19773v1","lineno":null}); Total lines: 684
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Interactive Evidence Collection Evaluation Framework L18:     1. cite8†2.1 Roles L19:     2. cite9†2.2 Information Coverage Rate L20:   4. cite10†3 EviMed Benchmark Construction L21:     1. cite11†3.1 Source Datasets L22:     2. cite12†3.2 Automatic Construction L23:   5. cite13†4 REFINE: Feedback-Driven Evidence Collection L24:   6. cite14†5 Experiments L25:     1. cite15†5.1 Setup L26:     2. cite16†5.2 Static vs. Interactive Evaluation L27:     3. cite17†5.3 Strategy Comparison L28:     4. cite18†5.4 Relationship between ICR and SR L29:     5. cite19†5.5 Role-Aware Model Pairing L30:     6. cite20†5.6 Information Coverage in Successful vs. Failed Diagnosis L31:     7. cite21†5.7 Effect of Interaction Budget L32:     8. cite22†5.8 Evidence Construction Sanity Check L33:   7. cite23†6 Related Work L34:     1. cite24†Task-Oriented Agents L35:     2. cite25†Medical Agent Evaluation L36:   8. cite26†7 Conclusion L37:   9. cite27†References L38:   10. cite28†A Interactive Environment and Evaluation Details L39:     1. cite29†A.1 Interactive Environment Details L40:     2. cite30†A.2 Automatic Evaluation L41:   11. cite31†B EviMed Construction Details L42:     1. cite32†B.1 Data Sources and Sampling L43:     2. cite33†B.2 Automatic Evidence Construction L44:   12. cite34†C Interaction Turns L45:   13. cite35†D Latency L46:   14. cite36†E Strategy Prompts L47:     1. cite37†Baseline. L48:     2. cite38†ReAct. L49:     3. cite39†SC. L50:     4. cite40†REFINE. L51: cite41†License: arXiv.org perpetual non-exclusive license†info.arxiv.org L52: 
L53: arXiv:2601.19773v1 [cs.CL] 27 Jan 2026
L54: # Strong Reasoning Isn’t Enough:
L55: Evaluating Evidence Elicitation in Interactive Diagnosis
L56: 
L57: Zhuohan Long Affiliation: School of Data Science, Fudan University Email: zhlong24@m.fudan.edu.cn    Zhijie Bao Affiliation: School of Data Science, Fudan University Affiliation: Shanghai Innovation Institute Email: zjbao24@m.fudan.edu.cn    Zhongyu Wei ^{†}^{†}thanks: Corresponding author. Affiliation: School of Data Science, Fudan University Affiliation: Shanghai Innovation Institute Email: zywei@fudan.edu.cn
L58: ###### Abstract
L59: Interactive medical consultation requires an agent to proactively elicit missing clinical evidence under uncertainty. Yet existing evaluations largely remain static or outcome-centric, neglecting the evidence-gathering process. In this work, we propose an interactive evaluation framework that explicitly models the consultation process using a simulated patient and a simulated reporter grounded in atomic evidences.
L60: Based on this representation, we introduce Information Coverage Rate (ICR) to quantify how completely an agent uncovers necessary evidence during interaction. To support systematic study, we build EviMed, an evidence-based benchmark spanning diverse conditions from common complaints to rare diseases, and evaluate 10 models with varying reasoning abilities.
L61: We find that strong diagnostic reasoning does not guarantee effective information collection, and this insufficiency acts as a primary bottleneck limiting performance in interactive settings. To address this, we propose REFINE, a strategy that leverages diagnostic verification to guide the agent in proactively resolving uncertainties.
L62: Extensive experiments demonstrate that REFINE consistently outperforms baselines across diverse datasets and facilitates effective model collaboration, enabling smaller agents to achieve superior performance under strong reasoning supervision. Our code can be found at cite42†this URL†github.com .
L63: cite43†Image: Refer to caption Figure 1: Static evaluation provides full patient information upfront. Interactive diagnosis requires iterative evidence elicitation and may fail due to insufficient information gathering or flawed reasoning.
L64: ## 1 Introduction
L65: Large Language Models (LLMs) have achieved remarkable progress in recent years, evolving from passive language processors to autonomous agents ahn2022can; liu2023agentbench. Beyond text generation, these agents demonstrate increasing capabilities in interacting with external environments zhou2023webarena; yao2022webshop, using tools schick2023toolformer, and executing complex workflows jimenez2023swe.
L66: Such advancements suggest that LLM-based agents are becoming proficient at following user instructions to accomplish multi-step tasks.
L67: However, many real-world decision-making scenarios extend beyond simple instruction following. In these settings, the agent is not provided with all necessary context upfront. Instead, the agent must actively identify missing information and acquire it through interaction before making a decision. Consequently, the quality of the final outcome hinges heavily on the agent’s ability to gather information effectively under uncertainty.
L68: Medical consultation represents a quintessential instance of such information-seeking scenarios. In clinical practice, diagnosis is an interactive evidence-gathering process rather than an one-shot prediction task meyer2021patient. Key evidence, including symptoms, medical history, and examinations, must be actively elicited through patient inquiry or clinical testing.
L69: Therefore, an effective medical agent must proactively ask relevant questions and decide when sufficient evidence has been collected to support a reliable diagnosis.
L70: Despite this interactive nature (Fig. cite44†1 ), most existing evaluations nori2023can; chen2023meditron; lievin2024can; wu2024pmc; singhal2025toward focus on static settings where all patient information is provided to the LLM in advance. While recent studies have begun to explore interactive diagnosis, they still primarily assess the final diagnostic accuracy.
L71: This outcome-oriented evaluation overlooks the evidence-elicitation process, leaving it unclear whether the agent can efficiently and systematically gather the information required for a correct diagnosis.
L72: In this work, we argue that information collection ability should be treated as a first-class evaluation target for medical agents. To this end, we propose an interactive evaluation framework that explicitly models the consultation process using a simulated patient and a simulated reporter by leveraging the generative capabilities of language models park2023generative; du2024llms.
L73: We specifically represent all clinical information within these modules as atomic evidences, which are defined as minimal and self-contained units of facts. This granular representation enables us to introduce a new metric, the Information Coverage Rate (ICR). Unlike traditional success rates, ICR explicitly measures the proportion of necessary evidence successfully revealed by the agent, providing a fine-grained assessment of its active inquiry capabilities.
L74: To support this evaluation framework, we construct EviMed, a new benchmark for interactive medical consultation. We transform existing medical datasets into the evidence-based format through an automated construction process. The resulting benchmark covers a diverse range of scenarios, spanning from common medical inquiries to challenging rare disease diagnoses that require extensive evidence accumulation.
L75: We evaluate 10 LLMs of varying diagnostic reasoning ability on EviMed, revealing a performance disparity between static and interactive settings. On average, diagnostic success rates drop by approximately 20% when agents are required to actively collect information, with even sharper declines observed in rare disease scenarios. Moreover, our results show that strong diagnostic reasoning alone does not guarantee effective information acquisition.
L76: Insufficient information collection during interaction appears to be the main bottleneck underlying performance degradation.
L77: To address these challenges, we propose REFINE (Reasoning-Enhanced Feedback for INformation Elicitation). It employs a Diagnosis Verifier to examine whether a generated Diagnosis hypothesis is fully grounded in the collected evidences, guiding the agent to resolve uncertainties.
L78: Extensive experiments demonstrate that this strategy effectively mitigates the performance degradation in interactive settings, yielding substantial improvements in both information coverage and diagnostic success rates across diverse models. Furthermore, we find that REFINE enables effective collaboration between heterogeneous models, allowing smaller, inquisitive agents to achieve superior performance when supervised by strong reasoning models.
L79: Overall, our contributions are threefold:
L80: 
L81: (1) We propose an interactive evaluation framework for evidence collection and introduce the Information Coverage Rate (ICR) metric, which formalizes information collection as a measurable objective grounded in atomic evidence units.
L82: (2) We construct EviMed, a comprehensive diagnostic benchmark, and conduct a systematic evaluation of 10 models with varying diagnostic capabilities, revealing that strong diagnostic reasoning does not guarantee effective information collection, which emerges as a key performance bottleneck.
L83: (3) We introduce REFINE, a feedback-driven strategy that leverages diagnostic verification to guide the interaction. It effectively mitigates the performance degradation in interactive settings and supports heterogeneous model collaboration, enabling smaller models to excel in inquiry tasks under strong reasoning supervision.
L84: ## 2 Interactive Evidence Collection Evaluation Framework
L85: cite45†Image: Refer to caption Figure 2: Interactive Evaluation Framework. (Left) The consultation loop. The doctor agent iteratively interacts with a simulated patient that provides subjective/history-related information and a simulated reporter that returns objective examination or laboratory findings.
L86: The interaction reveals atomic evidences used for evaluation, where we track Information Coverage Rate (ICR) to measure how many relevant evidences have been collected during the dialogue, and assess diagnostic Success Rate based on the final diagnosis. (Right) An example consultation trajectory showing queries, evidence-grounded responses, test requests/results, and the final diagnosis.
L87: In real clinical settings, relevant information is often incomplete and distributed across multiple sources. A clinician must determine what information is missing, how to obtain it, and when the collected evidence is sufficient to support a diagnosis. To model this interactive evidence collection process, we construct a medical consultation environment concentrating on evidence collection shown in Figure cite46†2 .
L88: The environment is composed of three distinct roles, including a simulated patient, a simulated reporter, and the doctor agent being evaluated. The consultation proceeds in multiple turns. At each turn, the doctor agent chooses an action, including asking the patient a question, requesting a clinical examination, or issuing a diagnosis. In response, the simulated patient and the simulated reporter return information grounded in the case record.
L89: ### 2.1 Roles
L90: 
L91: We define the three roles and their modeling assumptions below.
L92: Simulated Patient. The simulated patient maintains the patient’s personal information in the form of atomic evidences, covering symptoms, history, and related clinical details. It follows an evidence selection mechanism similar to the Fact-Select approach in li2024mediq, the patient selects the most relevant evidences for a given query and generates a natural language response grounded in them. Each response is supported by at most two evidences.
L93: If the query is unrelated to any evidence, the patient explicitly indicates uncertainty.
L94: Simulated Reporter. The simulated reporter maintains clinical examination results and laboratory test findings. For each request, it returns one or more relevant evidences as objective observations. These results are provided directly without natural language generation. This component evaluates whether the agent can select appropriate examinations and utilize objective clinical evidence.
L95: Doctor Agent. The doctor agent is the model under evaluation. During the consultation, it decides its next action among asking a question, requesting a test, or issuing a diagnosis. This requires the agent to determine whom to interact with, how to formulate queries, and when to terminate the interaction. Therefore, the consultation process is modeled as a sequential decision-making problem under incomplete information.
L96: ### 2.2 Information Coverage Rate
L97: 
L98: To evaluate the agent’s ability to collect relevant information, we propose Information Coverage Rate (ICR). ICR measures the proportion of evidences that are successfully collected by the agent through interaction. It reflects how thoroughly the agent explores the evidence space required for diagnosis.
L99: Formally, let $E$ denote the set of all relevant evidences for a given case. Let $\hat{E}$ denote the set of evidences collected by the agent during the consultation. ICR is defined as
L100: 
L101:  | $$\mathrm{ICR}=\frac{|\hat{E}\cap E|}{|E|}.$$  |
L102: As both patient responses and test results are grounded in atomic evidences, ICR is directly computable from the evidence revealed during interaction. Together with diagnostic success rate, ICR provides a complementary view by separating evidence collection completeness from final diagnostic correctness.
L103: ## 3 EviMed Benchmark Construction
L104: 
L105: Most existing medical datasets present complete case narratives without explicit atomic evidence structure. This makes it difficult to support selective evidence disclosure and compute information collection coverage. To address this gap, we construct EviMed, an evidence-based benchmark for interactive medical consultation evaluation.
L106: ### 3.1 Source Datasets
L107: 
L108: EviMed integrates five complementary data sources covering general medicine, specialty diagnosis, complex multi-specialty reasoning, rare diseases, and real-world clinical records. We sample two hundred cases from each source, yielding the EviMed-1K benchmark, which spans a wide range of diagnostic settings. The five data sources are described as follows:
L109: AgentClinic-MedQA schmidgall2024agentclinic is adapted from USMLE-style medical examination cases and rewritten into consultation-oriented scenarios. It covers a wide range of common diseases and clinical conditions. We use this source to evaluate general diagnostic reasoning.
L110: Derm johri2024craft focuses on dermatological diagnosis and emphasizes fine-grained descriptions. It contains both publicly available cases and clinician-authored cases with similar structures. We include the full set to evaluate detailed symptom inquiry in a specialized domain.
L111: DiagnosisArena zhu2025diagnosisarena is constructed from real-world case reports published in top-tier medical journals. The cases require complex diagnostic reasoning across multiple clinical specialties. We use it to assess information collection in challenging diagnostic scenarios.
L112: RareArena zhao2025rarearena is built from publicly available case reports in PubMed Central (PMC) and covers a wide range of rare diseases, which involve limited prior knowledge and ambiguous symptom presentations. We sample cases according to disease frequency to encourage diversity across different levels of rarity.
L113: ClinicalBench yan2024clinicallab is derived from real electronic medical records containing both structured and unstructured information. It covers cases from multiple clinical departments and a broad set of disease categories. We sample cases to ensure coverage across disease types.
L114: ### 3.2 Automatic Construction
L115: 
L116: For each selected case, we transform the original case description into an evidence-based representation. We separate patient basic information from examination-related information, and then decompose each part into non-overlapping atomic evidences, where each evidence corresponds to a minimal and self-contained clinical fact. This conversion is performed automatically using GPT-5-mini.
L117: After construction, each case is associated with a set of patient evidences and a set of examination evidences. These evidences serve as the information sources accessed during interaction by the simulated patient and the simulated reporter. Table cite47†1 summarizes the benchmark statistics, including the average number of patient evidences and examination evidences per case in each source dataset.
L118: The number of atomic evidences varies across sources, reflecting differences in case complexity and information density.
L119: In Section cite22†5.8 , we verify that the automatic construction process preserves diagnostic information.
L120: 
L121: Table 1: Statistics of EviMed-1K.
L122: 
L123: Dataset  | Data Size  | Avg Pat. Evi.  | Avg Exam Evi.
L124: --- | --- | --- | ---
L125: AgentClinic-MedQA  | 200  | 14.87  | 12.73
L126: Derm  | 200  | 7.31  | 2.87
L127: DiagnosisArena  | 200  | 8.04  | 12.82
L128: RareArena  | 200  | 17.11  | 17.72
L129: ClinicalBench  | 200  | 21.76  | 21.14
L130: ## 4 REFINE: Feedback-Driven Evidence Collection
L131: 
L132: In interactive medical consultation, the agent must make diagnostic decisions under incomplete and evolving evidence. This setting introduces two tightly coupled challenges. First, the agent must determine which information to elicit next in order to efficiently reduce the diagnostic uncertainty. Second, it must decide when the accumulated evidence is sufficient to support a reliable diagnosis, rather than terminating the consultation prematurely.
L133: To address these challenges, we propose Reasoning-Enhanced Feedback for INformation Elicitation (REFINE), a feedback-driven strategy for evidence collection. As illustrated in Figure cite48†3 , REFINE consists of an Information Collector, an Evidence Organizer, a Diagnosis Reasoner and a Diagnosis Verifier. The Information Collector interacts with the consultation environment across multiple turns.
L134: At each turn, it assesses whether the currently collected information is sufficient, decides whether to continue acquiring evidence, or terminates the interaction to make a diagnosis. When the collector stops, the Evidence Organizer consolidates the collected findings into a structured evidence summary.
L135: Given the organized evidence summary, the Diagnosis Reasoner produces a diagnostic hypothesis. The Diagnosis Verifier then checks whether the hypothesis is fully supported by the available evidence. If the verifier detects the evidence is insufficient, it provides explicit feedback identifying missing information and unresolved uncertainties, which is sent back to the Information Collector to resume the interaction phase and guide subsequent evidence acquisition steps.
L136: This loop continues until the verifier finds that the hypothesis is sufficiently supported by collected evidence or the interaction reaches a maximum turn limit. This design separates an internal hypothesis used for probing the evidence state from the final diagnostic output. As a result, the feedback specifies what to collect next, and the absence of critical evidence gaps provides a natural criterion for when to stop.
L137: 
L138: cite49†Image: Refer to caption Figure 3: Overview of the REFINE Strategy.
L139: ## 5 Experiments
L140: ### 5.1 Setup
L141: 
L142: We evaluate different models and methods under the interactive evidence collection framework with a maximum of 16 interaction turns. We consider the following methods for comparison:
L143: Upper Bound uses a static full-information setting where all patient information and examination results are provided upfront. We prompt the model to generate intermediate reasoning before producing the final diagnosis, establishing a performance upper bound where active information acquisition is not required.
L144: Baseline represents a standard interactive setting where a single doctor agent interacts directly with the environment. At each turn, the model determines whether to ask a question, request a specific examination, or terminate the session to output a final diagnosis.
L145: ReAct yao2022react augments the baseline by enforcing an explicit Thought-Act cycle during the consultation. Before taking any external action, the agent must generate a reasoning trace to analyze the current clinical state and justify its next move, thereby improving decision-making.
L146: Summarized-Conversation (SC) johri2024craft decouples information gathering from diagnosis. It first conducts a full multi-turn consultation to collect evidence, then summarizes the entire interaction history into a structured format. The final diagnosis is produced solely based on this consolidated summary rather than turn-level context.
L147: REFINE is our proposed feedback-driven strategy designed to optimize evidence collection. It utilizes a diagnostic verification mechanism to assess the sufficiency of collected information, providing the agent with explicit feedback to guide subsequent inquiry steps and proactively resolve remaining uncertainties.
L148: We evaluate a diverse set of language models spanning different scales and domain specializations. The evaluated models include GPT-5 openai2025chatgpt5, GPT-5-mini, DeepSeek-v3.2 liu2025deepseek, GLM-4.6 zai2025glm46, Qwen2.5-72B hui2024qwen2, Qwen2.5-32B, Qwen2.5-7B, Qwen2.5-3B, Llama-3.1-8B-Instruct dubey2024llama, and Meditron3-8B sallinen2025llama.
L149: ### 5.2 Static vs. Interactive Evaluation
L150: 
L151: We compare static and interactive evaluation to assess whether strong full-information reasoning performance transfers to realistic consultations that require evidence acquisition. Specifically, we report the Success Rate under the static full-information upper bound setting and report both ICR and SR under the interactive baseline. Results are summarized in Table cite50†2 .
L152: Across datasets and models, SR decreases by approximately 20% on average when moving from static to interactive evaluation. This degradation is more pronounced on the more challenging DiagnosisArena and RareArena datasets. Even for the strongest model, GPT-5, performance drops substantially in the interactive setting, indicating that strong static reasoning does not directly translate to effective interactive decision-making.
L153: Interestingly, some models exhibit larger performance drops than others. For example, GPT-5-mini originally achieves a stronger static upper bound than DeepSeek-v3.2 and GLM-4.6, but its interactive SR lags behind them. A similar phenomenon is observed for Meditron3-8B. Although it is fine-tuned on clinical data based on Llama-3.1-8B, it shows a larger performance degradation than its base model.
L154: We further observe that models with larger degradation, such as GPT-5-mini and Meditron3-8B, also exhibit relatively low ICR. This suggests that insufficient or inefficient information acquisition may be a key factor limiting their diagnostic reasoning performance in interactive settings.
L155: Table 2: Static Upper Bound vs. interactive Baseline evaluation. UB denotes SR under static evaluation. ICR and SR are metrics under interactive evaluation framework. For SR, the subscript indicates the percentage decrease relative to UB. Bold values denote the best performance under each metric.
L156: Model  | ClinicalBench  | Derm  | DiagnosisArena  | MedQA  | RareArena
L157: --- | --- | --- | --- | --- | ---
L158:  | UB (%)$\uparrow$  | ICR (%)$\uparrow$  | SR (%)$\uparrow$  | UB (%)$\uparrow$  | ICR (%)$\uparrow$  | SR (%)$\uparrow$  | UB (%)$\uparrow$  | ICR (%)$\uparrow$  | SR (%)$\uparrow$  | UB (%)$\uparrow$  | ICR (%)$\uparrow$  | SR (%)$\uparrow$  | UB (%)$\uparrow$  | ICR (%)$\uparrow$  | SR (%)$\uparrow$
L159: GPT-5  | 64.0  | 35.2  | $47.0_{(-27\%)}$  | 93.5  | 54.9  | $\mathbf{75.0}_{(-20\%)}$  | 75.0  | 55.4  | $\mathbf{47.0}_{(-37\%)}$  | 97.5  | 31.3  | $\mathbf{78.0}_{(-20\%)}$  | 75.0  | 42.7  | $\mathbf{37.0}_{(-51\%)}$
L160: GPT-5-mini  | 67.5  | 31.3  | $46.5_{(-31\%)}$  | 84.0  | 51.7  | $57.5_{(-32\%)}$  | 63.0  | 47.2  | $23.0_{(-64\%)}$  | 92.0  | 33.0  | $61.0_{(-34\%)}$  | 68.0  | 35.7  | $15.5_{(-77\%)}$
L161: DeepSeek-v3.2  | 63.0  | 46.7  | $\mathbf{51.0}_{(-19\%)}$  | 80.5  | 77.0  | $65.0_{(-19\%)}$  | 56.5  | 63.4  | $21.5_{(-62\%)}$  | 92.5  | 44.3  | $70.5_{(-24\%)}$  | 61.5  | 49.1  | $24.5_{(-60\%)}$
L162: GLM-4.6  | 60.5  | 32.6  | $45.0_{(-26\%)}$  | 78.5  | 65.7  | $66.0_{(-16\%)}$  | 52.0  | 52.1  | $23.0_{(-56\%)}$  | 86.0  | 36.6  | $72.0_{(-16\%)}$  | 59.0  | 37.8  | $21.5_{(-64\%)}$
L163: Qwen2.5-72B  | 64.5  | 40.8  | $43.5_{(-33\%)}$  | 59.0  | 67.5  | $43.0_{(-27\%)}$  | 24.5  | 55.5  | $10.0_{(-59\%)}$  | 75.5  | 41.7  | $54.0_{(-29\%)}$  | 32.0  | 41.6  | $10.5_{(-67\%)}$
L164: Qwen2.5-32B  | 60.0  | 39.0  | $48.0_{(-20\%)}$  | 49.5  | 71.6  | $35.0_{(-29\%)}$  | 20.0  | 57.0  | $8.0_{(-60\%)}$  | 76.5  | 37.3  | $52.0_{(-32\%)}$  | 29.0  | 43.0  | $6.0_{(-79\%)}$
L165: Qwen2.5-7B  | 52.0  | 41.0  | $35.5_{(-32\%)}$  | 37.5  | 71.9  | $20.0_{(-47\%)}$  | 13.0  | 53.1  | $8.0_{(-39\%)}$  | 60.5  | 43.5  | $43.0_{(-29\%)}$  | 19.5  | 41.2  | $5.0_{(-74\%)}$
L166: Llama-3.1-8B  | 37.0  | 40.5  | $34.5_{(-7\%)}$  | 38.5  | 74.4  | $25.5_{(-34\%)}$  | 14.0  | 57.3  | $6.0_{(-57\%)}$  | 67.0  | 47.8  | $57.5_{(-14\%)}$  | 23.0  | 45.0  | $9.0_{(-61\%)}$
L167: Meditron3-8B  | 42.5  | 23.4  | $20.0_{(-53\%)}$  | 43.0  | 39.7  | $19.0_{(-56\%)}$  | 10.5  | 33.7  | $2.5_{(-76\%)}$  | 68.0  | 28.7  | $20.5_{(-70\%)}$  | 25.5  | 23.2  | $2.5_{(-90\%)}$
L168: Qwen2.5-3B  | 38.0  | 33.8  | $30.0_{(-21\%)}$  | 24.0  | 74.1  | $11.5_{(-52\%)}$  | 9.5  | 47.7  | $5.5_{(-42\%)}$  | 49.5  | 43.7  | $35.5_{(-28\%)}$  | 9.5  | 35.1  | $2.0_{(-79\%)}$
L169: Table 3: Comparison of representative models under different interactive strategies across datasets. Bold indicates the best performance for the same model on the same dataset.
L170: Dataset  | Model  | Baseline  | ReAct  | SC  | REFINE
L171: --- | --- | --- | --- | --- | ---
L172: ICR (%)$\uparrow$  | SR (%)$\uparrow$  | ICR (%)$\uparrow$  | SR (%)$\uparrow$  | ICR (%)$\uparrow$  | SR (%)$\uparrow$  | ICR (%)$\uparrow$  | SR (%)$\uparrow$
L173: --- | --- | --- | --- | --- | --- | --- | ---
L174: ClinicalBench  | GPT-5-mini  | 31.3  | 46.5  | 33.5  | 49.5  | 41.5  | 49.0  | 43.5  | 49.5
L175: Qwen2.5-72B  | 40.8  | 43.5  | 38.7  | 42.0  | 43.2  | 49.5  | 51.1  | 53.0
L176: Qwen2.5-7B  | 41.0  | 35.5  | 29.8  | 33.0  | 32.5  | 35.0  | 35.3  | 38.5
L177: Derm  | GPT-5-mini  | 51.7  | 57.5  | 59.5  | 62.0  | 70.9  | 66.5  | 76.7  | 66.0
L178: Qwen2.5-72B  | 67.5  | 43.0  | 71.2  | 45.0  | 77.9  | 45.5  | 80.8  | 44.0
L179: Qwen2.5-7B  | 71.9  | 20.0  | 63.5  | 23.0  | 62.8  | 25.0  | 67.1  | 28.5
L180: DiagnosisArena  | GPT-5-mini  | 47.2  | 23.0  | 53.9  | 29.5  | 60.8  | 39.5  | 64.6  | 42.0
L181: Qwen2.5-72B  | 55.5  | 10.0  | 58.9  | 12.5  | 63.4  | 15.5  | 73.8  | 18.5
L182: Qwen2.5-7B  | 53.1  | 8.0  | 45.1  | 3.5  | 53.6  | 10.5  | 50.8  | 13.0
L183: AgentClinic-MedQA  | GPT-5-mini  | 33.0  | 61.0  | 33.2  | 67.0  | 40.2  | 69.5  | 45.5  | 68.0
L184: Qwen2.5-72B  | 41.7  | 54.0  | 39.5  | 59.0  | 43.6  | 62.0  | 53.9  | 64.5
L185: Qwen2.5-7B  | 43.5  | 43.0  | 35.8  | 45.0  | 36.0  | 44.5  | 38.6  | 45.5
L186: RareArena  | GPT-5-mini  | 35.7  | 15.5  | 39.3  | 24.0  | 46.2  | 30.5  | 51.8  | 32.0
L187: Qwen2.5-72B  | 41.6  | 10.5  | 47.4  | 13.0  | 50.1  | 15.5  | 59.9  | 17.0
L188: Qwen2.5-7B  | 41.2  | 5.0  | 29.8  | 2.5  | 37.0  | 5.5  | 38.2  | 7.5
L189: ### 5.3 Strategy Comparison
L190: 
L191: We compare interaction strategies to assess their effects on ICR and SR. We report results for GPT-5-mini, Qwen2.5-72B, and Qwen2.5-7B in Table cite51†3 .
L192: 
L193: From the results, ReAct improves both ICR and SR for stronger models such as GPT-5-mini and Qwen2.5-72B. However, for the weaker model Qwen2.5-7B, ReAct decreases both ICR and SR. This may reflect increased difficulty under longer multi-turn trajectories laban2025llms, which is also suggested by Section cite21†5.7 .

## Original response 2: jan29_stdnext5core

Strong Reasoning Isn’t Enough: Evaluating Evidence Elicitation in Interactive Diagnosis (https://arxiv.org/html/2601.19773v1)
citeturn28453view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28451view0","lineno":193}); Total lines: 684
L165: Qwen2.5-7B  | 52.0  | 41.0  | $35.5_{(-32\%)}$  | 37.5  | 71.9  | $20.0_{(-47\%)}$  | 13.0  | 53.1  | $8.0_{(-39\%)}$  | 60.5  | 43.5  | $43.0_{(-29\%)}$  | 19.5  | 41.2  | $5.0_{(-74\%)}$
L166: Llama-3.1-8B  | 37.0  | 40.5  | $34.5_{(-7\%)}$  | 38.5  | 74.4  | $25.5_{(-34\%)}$  | 14.0  | 57.3  | $6.0_{(-57\%)}$  | 67.0  | 47.8  | $57.5_{(-14\%)}$  | 23.0  | 45.0  | $9.0_{(-61\%)}$
L167: Meditron3-8B  | 42.5  | 23.4  | $20.0_{(-53\%)}$  | 43.0  | 39.7  | $19.0_{(-56\%)}$  | 10.5  | 33.7  | $2.5_{(-76\%)}$  | 68.0  | 28.7  | $20.5_{(-70\%)}$  | 25.5  | 23.2  | $2.5_{(-90\%)}$
L168: Qwen2.5-3B  | 38.0  | 33.8  | $30.0_{(-21\%)}$  | 24.0  | 74.1  | $11.5_{(-52\%)}$  | 9.5  | 47.7  | $5.5_{(-42\%)}$  | 49.5  | 43.7  | $35.5_{(-28\%)}$  | 9.5  | 35.1  | $2.0_{(-79\%)}$
L169: Table 3: Comparison of representative models under different interactive strategies across datasets. Bold indicates the best performance for the same model on the same dataset.
L170: Dataset  | Model  | Baseline  | ReAct  | SC  | REFINE
L171: --- | --- | --- | --- | --- | ---
L172: ICR (%)$\uparrow$  | SR (%)$\uparrow$  | ICR (%)$\uparrow$  | SR (%)$\uparrow$  | ICR (%)$\uparrow$  | SR (%)$\uparrow$  | ICR (%)$\uparrow$  | SR (%)$\uparrow$
L173: --- | --- | --- | --- | --- | --- | --- | ---
L174: ClinicalBench  | GPT-5-mini  | 31.3  | 46.5  | 33.5  | 49.5  | 41.5  | 49.0  | 43.5  | 49.5
L175: Qwen2.5-72B  | 40.8  | 43.5  | 38.7  | 42.0  | 43.2  | 49.5  | 51.1  | 53.0
L176: Qwen2.5-7B  | 41.0  | 35.5  | 29.8  | 33.0  | 32.5  | 35.0  | 35.3  | 38.5
L177: Derm  | GPT-5-mini  | 51.7  | 57.5  | 59.5  | 62.0  | 70.9  | 66.5  | 76.7  | 66.0
L178: Qwen2.5-72B  | 67.5  | 43.0  | 71.2  | 45.0  | 77.9  | 45.5  | 80.8  | 44.0
L179: Qwen2.5-7B  | 71.9  | 20.0  | 63.5  | 23.0  | 62.8  | 25.0  | 67.1  | 28.5
L180: DiagnosisArena  | GPT-5-mini  | 47.2  | 23.0  | 53.9  | 29.5  | 60.8  | 39.5  | 64.6  | 42.0
L181: Qwen2.5-72B  | 55.5  | 10.0  | 58.9  | 12.5  | 63.4  | 15.5  | 73.8  | 18.5
L182: Qwen2.5-7B  | 53.1  | 8.0  | 45.1  | 3.5  | 53.6  | 10.5  | 50.8  | 13.0
L183: AgentClinic-MedQA  | GPT-5-mini  | 33.0  | 61.0  | 33.2  | 67.0  | 40.2  | 69.5  | 45.5  | 68.0
L184: Qwen2.5-72B  | 41.7  | 54.0  | 39.5  | 59.0  | 43.6  | 62.0  | 53.9  | 64.5
L185: Qwen2.5-7B  | 43.5  | 43.0  | 35.8  | 45.0  | 36.0  | 44.5  | 38.6  | 45.5
L186: RareArena  | GPT-5-mini  | 35.7  | 15.5  | 39.3  | 24.0  | 46.2  | 30.5  | 51.8  | 32.0
L187: Qwen2.5-72B  | 41.6  | 10.5  | 47.4  | 13.0  | 50.1  | 15.5  | 59.9  | 17.0
L188: Qwen2.5-7B  | 41.2  | 5.0  | 29.8  | 2.5  | 37.0  | 5.5  | 38.2  | 7.5
L189: ### 5.3 Strategy Comparison
L190: 
L191: We compare interaction strategies to assess their effects on ICR and SR. We report results for GPT-5-mini, Qwen2.5-72B, and Qwen2.5-7B in Table cite51†3 .
L192: 
L193: From the results, ReAct improves both ICR and SR for stronger models such as GPT-5-mini and Qwen2.5-72B. However, for the weaker model Qwen2.5-7B, ReAct decreases both ICR and SR. This may reflect increased difficulty under longer multi-turn trajectories laban2025llms, which is also suggested by Section cite21†5.7 .
L194: In contrast, SC more consistently improves both ICR and SR across the evaluated models. This strategy likely benefits from separating information collection from the final diagnosis, which helps the agent remain focused on evidence acquisition. Moreover, making the diagnosis based on a structured summary may mitigate reasoning degradation in long conversations.
L195: REFINE achieves the highest ICR across most datasets and models. The improvements are especially pronounced on the challenging DiagnosisArena and RareArena datasets. These results support reasoning-based feedback as an effective mechanism for aligning information collection with downstream diagnostic needs.
L196: 
L197: cite52†Image: Refer to caption Figure 4: Relationship between average Information Coverage Rate and Success Rate under interactive evaluation, with values averaged over the five datasets.
L198: ### 5.4 Relationship between ICR and SR
L199: 
L200: To better understand the relationship between evidence acquisition ability and diagnostic performance, we analyze the relationship between Information Collection Rate (ICR) and Success Rate (SR) across models and strategies. We include the interactive results of all models reported in Section cite16†5.2 , as well as the strategy variants for selected representative models in Section cite17†5.3 . The corresponding scatter plots are shown in Figure cite53†4 .
L201: We observe that SR generally correlates with ICR across models. For example, performance increases from GPT-5-mini to GLM-4.6 to DeepSeek-v3.2, and from Meditron3-8B to Llama-3.1-8B, in terms of both ICR and SR. However, this relationship is not always consistent. For instance, the GPT-5 series exhibits relatively high SR but comparatively low ICR, whereas the Qwen2.5 series shows high ICR but lower SR.
L202: This suggests that diagnostic reasoning ability and evidence elicitation ability are partially decoupled.
L203: Specifically, GPT-5 models appear to possess stronger diagnostic reasoning capabilities, enabling them to achieve high performance even with limited information. In contrast, the Qwen2.5 series demonstrates weaker diagnostic reasoning despite effective information collection. Interestingly, within the Qwen2.5 family, model scaling mainly improves SR while yielding marginal gains in ICR, indicating scaling primarily enhances reasoning capacity rather than evidence elicitation ability.
L204: From a strategy perspective, we find that most strategies improve SR in accordance with their improvements in ICR, with the exception of ReAct on Qwen2.5-7B, as discussed in Section cite17†5.3 . This further supports a general consistency between ICR and SR, suggesting that enhancing a model’s information acquisition ability is a promising direction for improving overall diagnostic success.
L205: Table 4: Performance comparison of role-aware model pairings under the REFINE strategy. $M_{1}\rightarrow M_{2}$ denotes using $M_{1}$ as the Information Collector and $M_{2}$ as the Organizer, Reasoner and Verifier.
L206: Dataset  | Qwen2.5-7B  | GPT-5-mini  | GPT$\rightarrow$Qwen  | Qwen$\rightarrow$GPT
L207: --- | --- | --- | --- | ---
L208: ICR (%)  | SR (%)  | ICR (%)  | SR (%)  | ICR (%)  | SR (%)  | ICR (%)  | SR (%)
L209: --- | --- | --- | --- | --- | --- | --- | ---
L210: ClinicalBench  | 35.3  | 38.5  | 43.5  | 49.5  | 39.9  | 36.5  | 52.2  | 50.5
L211: Derm  | 67.1  | 28.5  | 76.7  | 66.0  | 73.3  | 31.0  | 79.5  | 66.5
L212: DiagnosisArena  | 50.8  | 13.0  | 64.6  | 42.0  | 61.4  | 8.0  | 71.7  | 51.0
L213: MedQA  | 38.6  | 45.5  | 45.5  | 68.0  | 43.8  | 54.0  | 54.8  | 76.5
L214: RareArena  | 38.2  | 7.5  | 51.8  | 32.0  | 46.6  | 6.0  | 61.1  | 46.5
L215: Average  | 46.0  | 26.6  | 56.4  | 51.5  | 53.0  | 27.1  | 63.9  | 58.2
L216: ### 5.5 Role-Aware Model Pairing
L217: 
L218: Motivated by the mismatch between ICR and SR observed for the GPT-5 and Qwen2.5 series in Section cite18†5.4 , we investigate role-aware model pairing within REFINE. Specifically, we assign Qwen2.5-7B as the Information Collector and GPT-5-mini as the Organizer, Reasoner, and Verifier ($Qwen\rightarrow GPT$). For comparison, we also evaluate the reversed role assignment ($GPT\rightarrow Qwen$).
L219: As shown in Table cite54†4 , the $Qwen\rightarrow GPT$ configuration achieves the best ICR and SR across all datasets. In particular, it yields substantial improvements in both ICR and SR on DiagnosisArena and RareArena compared to the single GPT-5-mini setting. In contrast, the $GPT\rightarrow Qwen$ configuration consistently underperforms the single GPT-5-mini model in terms of ICR, and even falls below the single Qwen2.5-7B model in SR on three datasets.
L220: These results highlight that model mixing is beneficial only when model strengths are aligned with role requirements. They further suggest a cost-effective deployment strategy for REFINE: delegating high-frequency interactions and evidence elicitation to a smaller but inquiry-strong model, while reserving a stronger model for lower-frequency reasoning and verification
L221: ### 5.6 Information Coverage in Successful vs. Failed Diagnosis
L222: 
L223: We examine the association between diagnostic success and information coverage using outcome-conditioned ICR distributions.
L224: We study DiagnosisArena and RareArena, two challenging rare disease benchmarks that typically require extensive information collection. For each dataset, we aggregate successful and failed cases from the three models used in Section cite17†5.3 and present the distributions of their Information Coverage Rate. We compare three interaction strategies, Baseline, ReAct, and REFINE. Figure cite55†5 summarizes the resulting ICR distributions.

## Original response 3: jan29_stdnext5eval

Strong Reasoning Isn’t Enough: Evaluating Evidence Elicitation in Interactive Diagnosis (https://arxiv.org/html/2601.19773v1)
citeturn28454view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28451view0","lineno":225}); Total lines: 684
L205: Table 4: Performance comparison of role-aware model pairings under the REFINE strategy. $M_{1}\rightarrow M_{2}$ denotes using $M_{1}$ as the Information Collector and $M_{2}$ as the Organizer, Reasoner and Verifier.
L206: Dataset  | Qwen2.5-7B  | GPT-5-mini  | GPT$\rightarrow$Qwen  | Qwen$\rightarrow$GPT
L207: --- | --- | --- | --- | ---
L208: ICR (%)  | SR (%)  | ICR (%)  | SR (%)  | ICR (%)  | SR (%)  | ICR (%)  | SR (%)
L209: --- | --- | --- | --- | --- | --- | --- | ---
L210: ClinicalBench  | 35.3  | 38.5  | 43.5  | 49.5  | 39.9  | 36.5  | 52.2  | 50.5
L211: Derm  | 67.1  | 28.5  | 76.7  | 66.0  | 73.3  | 31.0  | 79.5  | 66.5
L212: DiagnosisArena  | 50.8  | 13.0  | 64.6  | 42.0  | 61.4  | 8.0  | 71.7  | 51.0
L213: MedQA  | 38.6  | 45.5  | 45.5  | 68.0  | 43.8  | 54.0  | 54.8  | 76.5
L214: RareArena  | 38.2  | 7.5  | 51.8  | 32.0  | 46.6  | 6.0  | 61.1  | 46.5
L215: Average  | 46.0  | 26.6  | 56.4  | 51.5  | 53.0  | 27.1  | 63.9  | 58.2
L216: ### 5.5 Role-Aware Model Pairing
L217: 
L218: Motivated by the mismatch between ICR and SR observed for the GPT-5 and Qwen2.5 series in Section cite18†5.4 , we investigate role-aware model pairing within REFINE. Specifically, we assign Qwen2.5-7B as the Information Collector and GPT-5-mini as the Organizer, Reasoner, and Verifier ($Qwen\rightarrow GPT$). For comparison, we also evaluate the reversed role assignment ($GPT\rightarrow Qwen$).
L219: As shown in Table cite54†4 , the $Qwen\rightarrow GPT$ configuration achieves the best ICR and SR across all datasets. In particular, it yields substantial improvements in both ICR and SR on DiagnosisArena and RareArena compared to the single GPT-5-mini setting. In contrast, the $GPT\rightarrow Qwen$ configuration consistently underperforms the single GPT-5-mini model in terms of ICR, and even falls below the single Qwen2.5-7B model in SR on three datasets.
L220: These results highlight that model mixing is beneficial only when model strengths are aligned with role requirements. They further suggest a cost-effective deployment strategy for REFINE: delegating high-frequency interactions and evidence elicitation to a smaller but inquiry-strong model, while reserving a stronger model for lower-frequency reasoning and verification
L221: ### 5.6 Information Coverage in Successful vs. Failed Diagnosis
L222: 
L223: We examine the association between diagnostic success and information coverage using outcome-conditioned ICR distributions.
L224: We study DiagnosisArena and RareArena, two challenging rare disease benchmarks that typically require extensive information collection. For each dataset, we aggregate successful and failed cases from the three models used in Section cite17†5.3 and present the distributions of their Information Coverage Rate. We compare three interaction strategies, Baseline, ReAct, and REFINE. Figure cite55†5 summarizes the resulting ICR distributions.
L225: Across both datasets and all strategies, successful cases consistently exhibit higher ICR than failed ones. These observations indicate that insufficient information coverage is commonly associated with diagnostic failure, supporting ICR as a indicator of diagnostic quality in interactive consultation.
L226: 
L227: cite56†Image: Refer to caption Figure 5: ICR distributions for successful and failed diagnoses on DiagnosisArena and RareArena.
L228: ### 5.7 Effect of Interaction Budget
L229: 
L230: We analyze how interaction budget affects ICR and SR. We vary the maximum number of interaction turns while keeping other settings fixed. We conduct this study on DiagnosisArena with Qwen2.5-72B, comparing Baseline and REFINE. Figure cite57†6 summarizes the results.
L231: At low budgets, both strategies improve quickly in both ICR and SR. Both metrics rise sharply in the first few turns. As the budget grows, the incremental gains taper off. ICR typically reaches its plateau slightly later than SR. Comparing the two strategies, REFINE sustains higher ICR and SR throughout the range of budgets and saturates later than Baseline.
L232: These results indicate that early turns are most effective for acquiring the evidence needed for diagnosis. After most relevant evidence is collected, additional interaction yields limited benefit and may increase reasoning burden.
L233: 
L234: cite58†Image: Refer to caption Figure 6: SR and ICR as functions of the maximum number of interaction turns.
L235: ### 5.8 Evidence Construction Sanity Check
L236: We conduct a sanity check to examine whether essential diagnostic information is preserved after evidence construction. To ensure essential information is preserved, we compare the diagnostic Success Rate of the original case descriptions against the concatenated constructed evidences in a static evaluation. Table cite59†5 shows that the performance differences between original cases and concatenated evidences are small, indicating the information loss introduced by this process is negligible.
L237: Table 5: Diagnostic success rate (%) under static evaluation using original case descriptions and concatenated evidences.
L238: Dataset  | Ori.  | Concat.
L239: --- | --- | ---
L240: DiagnosisArena  | 63.0  | 62.5
L241: RareArena  | 68.0  | 69.5
L242: MedQA  | 92.0  | 94.5
L243: ClinicalBench  | 67.5  | 67.5
L244: Derm  | 84.0  | 82.5
L245: ## 6 Related Work
L246: #### Task-Oriented Agents
L247: 
L248: Early research primarily focused on tool utilization in static scenarios. In these settings, agents are required to decompose specific user instructions and invoke appropriate APIs or search engines to execute actions yao2022react; qin2023toolllm; patil2024gorilla.
L249: Later work deng2023mind2web; wang2023mint; yao2022webshop; zhou2023webarena moved to dynamic environments that require multi-turn interaction, such as web navigation and database manipulation. Agents must track dialogue state and plan over long horizons to complete tasks reliably.
L250: Another line studies robustness under user-specified policies and evolving constraints in realistic workflows, including retail customer service and flight booking yao2024tau; barres2025tau. These evaluations prioritize constraint compliance and adaptability during interaction.
L251: Most of the above benchmarks assume an instruction-following paradigm where the user states intent and supplies sufficient information. In many real-world settings, users cannot provide complete information upfront, so agents must form hypotheses and elicit missing evidence through inquiry zhu2025ask; mukherjee2024polaris.
L252: Focusing on the medical consultation setting, our work introduces an interactive evaluation framework that requires agents to proactively gather information throughout the consultation process.
L253: #### Medical Agent Evaluation
L254: 
L255: Medical LLM evaluation has largely relied on static question answering datasets with complete case descriptions, testing knowledge retention and diagnostic reasoning jin2021disease; chen2025benchmarking; wang2024cmb; fansi2022ddxplus. Multi-agent collaboration can improve reasoning, but it typically remains within full-information inputs and does not require selective evidence discovery kim2024mdagents; tang2024medagents; wang2025medagent.
L256: To better reflect clinical practice, recent work simulates doctor patient encounters where agents interact with patients to gather symptoms and request examinations or tests schmidgall2024agentclinic; fan2025ai; johri2024craft; almansoori2025medagentsim; bao2025sfmss. These environments introduce interaction structure and information asymmetry compared with static benchmarks.
L257: However, interactive medical evaluations are still commonly scored by final diagnostic accuracy, which weakly captures the quality of the information collection process. Our work complements this literature by treating evidence collection as a first-class evaluation target and introducing ICR to quantify coverage of necessary atomic evidences during consultation.
L258: ## 7 Conclusion
L259: In this work, we revisit medical agent evaluation by shifting the focus from static prediction to interactive evidence collection. We establish a fine-grained evaluation framework grounded in atomic evidences and construct EviMed to systematically measure the agent’s active inquiry capabilities.
L260: Our analysis reveals a critical bottleneck: even models with strong reasoning capabilities often fail to collect sufficient information, leading to a significant performance gap between static and interactive settings. To address this, we propose REFINE, a strategy that utilizes diagnostic verification to guide the evidence-gathering process.
L261: Experiments demonstrate that REFINE not only improves information coverage and accuracy but also unlocks effective model collaboration, enabling smaller agents to achieve superior results through reasoning supervision. Ultimately, this work provides a valuable resource for assessing autonomous clinical decision-making and offers a scalable path toward bridging the gap between static knowledge retention and interactive diagnostic reasoning.
L262: ## Limitations
L263: Our evaluation is conducted in a controlled interactive simulator. This setting may not match the distribution of real patient narratives, clinician behaviors, and institutional constraints. Simulation can reduce ambiguity and compress the space of plausible follow up trajectories, which can shift the optimal elicitation strategy.
L264: Prior work on simulated patients and multi agent clinical simulators similarly highlights remaining gaps between multi turn interaction and curated or non interactive settings (holderried2024language; fan2025ai; almansoori2025medagentsim). Accordingly, our results should be read as comparative performance within this environment rather than a direct measure of clinical readiness.

## Original response 4: jan29_stdnext5tail

Strong Reasoning Isn’t Enough: Evaluating Evidence Elicitation in Interactive Diagnosis (https://arxiv.org/html/2601.19773v1)
citeturn28456view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28451view0","lineno":265}); Total lines: 684
L261: Experiments demonstrate that REFINE not only improves information coverage and accuracy but also unlocks effective model collaboration, enabling smaller agents to achieve superior results through reasoning supervision. Ultimately, this work provides a valuable resource for assessing autonomous clinical decision-making and offers a scalable path toward bridging the gap between static knowledge retention and interactive diagnostic reasoning.
L262: ## Limitations
L263: Our evaluation is conducted in a controlled interactive simulator. This setting may not match the distribution of real patient narratives, clinician behaviors, and institutional constraints. Simulation can reduce ambiguity and compress the space of plausible follow up trajectories, which can shift the optimal elicitation strategy.
L264: Prior work on simulated patients and multi agent clinical simulators similarly highlights remaining gaps between multi turn interaction and curated or non interactive settings (holderried2024language; fan2025ai; almansoori2025medagentsim). Accordingly, our results should be read as comparative performance within this environment rather than a direct measure of clinical readiness.
L265: We model clinical information as a set of atomic evidences to enable systematic scoring. This abstraction omits graded severity, temporal evolution, and dependencies across findings. Clinical facts also exhibit substantial semantic variability across documentation styles and contexts. Recent studies on feature and concept extraction from clinical notes suggest that fine grained clinical signal recovery remains challenging and can be sensitive to annotation and modeling choices (abumelha2025medical).
L266: As a result, higher atomic coverage may not always correspond to clinically sufficient information gathering.
L267: ICR is defined with respect to a case specific relevant evidence set $E$. In practice, multiple evidence subsets can justify the same diagnosis, and experts may disagree on what is necessary versus merely supportive. Inter rater reliability in related clinical evaluation settings varies across attributes and rubrics, indicating that a single reference set can encode subjective decisions (holderried2024language).
L268: Future work should report agreement statistics, test sensitivity to alternative definitions of $E$, and consider softer relevance modeling for borderline evidences.
L269: ## References
L270: 
L271: ## Appendix A Interactive Environment and Evaluation Details
L272: ### A.1 Interactive Environment Details
L273: We implement an interactive diagnostic environment with three roles: a doctor agent, a simulated patient, and a simulated reporter. All roles are instantiated using the CAMEL multi-agent framework li2023camel. Both the simulated patient and the simulated reporter operate with a context window of 1 and a temperature of 0, resulting in stateless behavior with respect to dialogue history and deterministic decoding across all experiments.
L274: This design choice reduces simulator drift over long conversations and improves stability across runs.
L275: The patient prompt is shown below:
L276: 
L277: ⬇
L278: 
L279: You are a patient undergoing a medical interview.
L280: 
L281: Your knowledge is strictly limited to the following list of indexed facts:
L282: 
L283: {patient_evidences}
L284: 
L285: Response protocols:
L286: 
L287: 1. Analyze the doctor question and search your list for the specific item or items that contain the answer.
L288: 
L289: 2. Format your output using two tags:
L290: 
L291: [REFERENCE] followed by the exact string or strings including the index from your list.
L292: 
L293: You may select up to two facts if necessary.
L294: If no fact exists write N/A.
L295: 
L296: [RESPONSE] followed by a natural language answer derived strictly from the selected references.
L297: 
L298: Do not add outside information.
L299: 
L300: 3. If the doctor question is not addressed by any fact in your list.
L301: 
L302: [REFERENCE] N/A
L303: 
L304: [RESPONSE] indicate that you are unsure or do not recall.
L305: 
L306: The reporter prompt is shown below:
L307: 
L308: ⬇
L309: 
L310: You are a specialized module named Measurement responsible for reporting test results to the physician.
L311: 
L312: You have access to the following list of indexed facts.
L313: Physical examination and diagnostic test data
L314: 
L315: {examination_evidences}
L316: 
L317: Response protocols:
L318: 
L319: 1. Search the provided list for all facts that are relevant to the doctor specific test request. Do not provide information that was not explicitly requested.
L320: 
L321: 2. Return the relevant facts exactly as they appear in the source list including their indices.
L322: 
L323: 3. If the requested test results are not found in the list assume the finding is non-significant and return Normal.

## Original response 5: jan29_stdnext5tail

Strong Reasoning Isn’t Enough: Evaluating Evidence Elicitation in Interactive Diagnosis (https://arxiv.org/html/2601.19773v1)
citeturn28456view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"turn28451view0","pattern":"## Appendix A"}); Total lines: 684
L264: Prior work on simulated patients and multi agent clinical simulators similarly highlights remaining gaps between multi turn interaction and curated or non interactive settings (holderried2024language; fan2025ai; almansoori2025medagentsim). Accordingly, our results should be read as comparative performance within this environment rather than a direct measure of clinical readiness.
L265: We model clinical information as a set of atomic evidences to enable systematic scoring. This abstraction omits graded severity, temporal evolution, and dependencies across findings. Clinical facts also exhibit substantial semantic variability across documentation styles and contexts. Recent studies on feature and concept extraction from clinical notes suggest that fine grained clinical signal recovery remains challenging and can be sensitive to annotation and modeling choices (abumelha2025medical).
L266: As a result, higher atomic coverage may not always correspond to clinically sufficient information gathering.
L267: ICR is defined with respect to a case specific relevant evidence set $E$. In practice, multiple evidence subsets can justify the same diagnosis, and experts may disagree on what is necessary versus merely supportive. Inter rater reliability in related clinical evaluation settings varies across attributes and rubrics, indicating that a single reference set can encode subjective decisions (holderried2024language).
L268: Future work should report agreement statistics, test sensitivity to alternative definitions of $E$, and consider softer relevance modeling for borderline evidences.
L269: ## References
L270: 
L271: ## Appendix A Interactive Environment and Evaluation Details
L272: ### A.1 Interactive Environment Details
L273: We implement an interactive diagnostic environment with three roles: a doctor agent, a simulated patient, and a simulated reporter. All roles are instantiated using the CAMEL multi-agent framework li2023camel. Both the simulated patient and the simulated reporter operate with a context window of 1 and a temperature of 0, resulting in stateless behavior with respect to dialogue history and deterministic decoding across all experiments.
L274: This design choice reduces simulator drift over long conversations and improves stability across runs.
L275: The patient prompt is shown below:
L276: 
L277: ⬇
L278: 
L279: You are a patient undergoing a medical interview.
L280: 
L281: Your knowledge is strictly limited to the following list of indexed facts:
L282: 
L283: {patient_evidences}
L284: 
L285: Response protocols:
L286: 
L287: 1. Analyze the doctor question and search your list for the specific item or items that contain the answer.
L288: 
L289: 2. Format your output using two tags:
L290: 
L291: [REFERENCE] followed by the exact string or strings including the index from your list.
L292: 
L293: You may select up to two facts if necessary.
L294: If no fact exists write N/A.
L295: 
L296: [RESPONSE] followed by a natural language answer derived strictly from the selected references.
L297: 
L298: Do not add outside information.
L299: 
L300: 3. If the doctor question is not addressed by any fact in your list.
L301: 
L302: [REFERENCE] N/A
L303: 
L304: [RESPONSE] indicate that you are unsure or do not recall.
L305: 
L306: The reporter prompt is shown below:
L307: 
L308: ⬇
L309: 
L310: You are a specialized module named Measurement responsible for reporting test results to the physician.
L311: 
L312: You have access to the following list of indexed facts.
L313: Physical examination and diagnostic test data
L314: 
L315: {examination_evidences}
L316: 
L317: Response protocols:
L318: 
L319: 1. Search the provided list for all facts that are relevant to the doctor specific test request. Do not provide information that was not explicitly requested.
L320: 
L321: 2. Return the relevant facts exactly as they appear in the source list including their indices.
L322: 
L323: 3. If the requested test results are not found in the list assume the finding is non-significant and return Normal.
L324: ### A.2 Automatic Evaluation
L325: 
L326: Following the original benchmarks, DiagnosisArena, RareArena, and ClinicalBench are differential diagnosis tasks where the model outputs five diseases ranked by likelihood. AgentClinic-MedQA and Derm are direct diagnosis tasks that require a single diagnosis.
L327: For direct diagnosis tasks, we evaluate whether the doctor predicted diagnosis matches the reference diagnosis. We use an LLM judge that outputs a binary decision with no additional text. The judge prompt for direct diagnosis is shown below.
L328: 
L329: ⬇
L330: 
L331: You determine whether the correct diagnosis and the doctor diagnosis refer to the same disease.
L332: 
L333: Respond only with Yes or No.
L334: 
L335: Correct diagnosis
L336: 
L337: {answer}
L338: 
L339: Doctor output
L340: 
L341: {diagnosis}
L342: 
L343: Are these the same disease?
L344: For differential diagnosis tasks, the doctor outputs five differential diagnoses. We use an LLM judge to score each of the five items against the reference diagnosis using a three-level rubric. A score of two indicates an exact match, a score of one indicates a broader category that contains the reference diagnosis, and a score of zero otherwise. We compute success rate (SR) using top-1 accuracy by checking whether the first listed diagnosis receives a score of two.

## Original response 6: jan29_stdnext5tail

Strong Reasoning Isn’t Enough: Evaluating Evidence Elicitation in Interactive Diagnosis (https://arxiv.org/html/2601.19773v1)
citeturn28456view4 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"turn28451view0","pattern":"## D Latency"}); Total lines: 684
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Interactive Evidence Collection Evaluation Framework L18:     1. cite8†2.1 Roles L19:     2. cite9†2.2 Information Coverage Rate L20:   4. cite10†3 EviMed Benchmark Construction L21:     1. cite11†3.1 Source Datasets L22:     2. cite12†3.2 Automatic Construction L23:   5. cite13†4 REFINE: Feedback-Driven Evidence Collection L24:   6. cite14†5 Experiments L25:     1. cite15†5.1 Setup L26:     2. cite16†5.2 Static vs. Interactive Evaluation L27:     3. cite17†5.3 Strategy Comparison L28:     4. cite18†5.4 Relationship between ICR and SR L29:     5. cite19†5.5 Role-Aware Model Pairing L30:     6. cite20†5.6 Information Coverage in Successful vs. Failed Diagnosis L31:     7. cite21†5.7 Effect of Interaction Budget L32:     8. cite22†5.8 Evidence Construction Sanity Check L33:   7. cite23†6 Related Work L34:     1. cite24†Task-Oriented Agents L35:     2. cite25†Medical Agent Evaluation L36:   8. cite26†7 Conclusion L37:   9. cite27†References L38:   10. cite28†A Interactive Environment and Evaluation Details L39:     1. cite29†A.1 Interactive Environment Details L40:     2. cite30†A.2 Automatic Evaluation L41:   11. cite31†B EviMed Construction Details L42:     1. cite32†B.1 Data Sources and Sampling L43:     2. cite33†B.2 Automatic Evidence Construction L44:   12. cite34†C Interaction Turns L45:   13. cite35†D Latency L46:   14. cite36†E Strategy Prompts L47:     1. cite37†Baseline. L48:     2. cite38†ReAct. L49:     3. cite39†SC. L50:     4. cite40†REFINE. L51: cite41†License: arXiv.org perpetual non-exclusive license†info.arxiv.org L52: 
L53: arXiv:2601.19773v1 [cs.CL] 27 Jan 2026
L54: # Strong Reasoning Isn’t Enough:
L55: Evaluating Evidence Elicitation in Interactive Diagnosis
L56: 
L57: Zhuohan Long Affiliation: School of Data Science, Fudan University Email: zhlong24@m.fudan.edu.cn    Zhijie Bao Affiliation: School of Data Science, Fudan University Affiliation: Shanghai Innovation Institute Email: zjbao24@m.fudan.edu.cn    Zhongyu Wei ^{†}^{†}thanks: Corresponding author. Affiliation: School of Data Science, Fudan University Affiliation: Shanghai Innovation Institute Email: zywei@fudan.edu.cn
L58: ###### Abstract
L59: Interactive medical consultation requires an agent to proactively elicit missing clinical evidence under uncertainty. Yet existing evaluations largely remain static or outcome-centric, neglecting the evidence-gathering process. In this work, we propose an interactive evaluation framework that explicitly models the consultation process using a simulated patient and a simulated reporter grounded in atomic evidences.
L60: Based on this representation, we introduce Information Coverage Rate (ICR) to quantify how completely an agent uncovers necessary evidence during interaction. To support systematic study, we build EviMed, an evidence-based benchmark spanning diverse conditions from common complaints to rare diseases, and evaluate 10 models with varying reasoning abilities.
L61: We find that strong diagnostic reasoning does not guarantee effective information collection, and this insufficiency acts as a primary bottleneck limiting performance in interactive settings. To address this, we propose REFINE, a strategy that leverages diagnostic verification to guide the agent in proactively resolving uncertainties.
L62: Extensive experiments demonstrate that REFINE consistently outperforms baselines across diverse datasets and facilitates effective model collaboration, enabling smaller agents to achieve superior performance under strong reasoning supervision. Our code can be found at cite42†this URL†github.com .
L63: cite43†Image: Refer to caption Figure 1: Static evaluation provides full patient information upfront. Interactive diagnosis requires iterative evidence elicitation and may fail due to insufficient information gathering or flawed reasoning.
L64: ## 1 Introduction
L65: Large Language Models (LLMs) have achieved remarkable progress in recent years, evolving from passive language processors to autonomous agents ahn2022can; liu2023agentbench. Beyond text generation, these agents demonstrate increasing capabilities in interacting with external environments zhou2023webarena; yao2022webshop, using tools schick2023toolformer, and executing complex workflows jimenez2023swe.
L66: Such advancements suggest that LLM-based agents are becoming proficient at following user instructions to accomplish multi-step tasks.
L454: Qwen2.5-7B  | 6.1  | 35.3  | 5.79  | 8.1  | 67.1  | 8.28  | 6.6  | 38.6  | 5.85  | 5.8  | 50.8  | 8.76  | 6.0  | 38.2  | 6.37
L455: Table cite60†6 reports the average number of interaction turns. We additionally report turn efficiency as Effi. = ICR / Turns to quantify evidence acquisition per interaction step.
L456: Across datasets, some models with stronger general reasoning ability, such as GPT-5 and GLM-4.6, exhibit longer dialogues, yet the resulting ICR gains remain limited. In contrast, the Qwen series often achieves relatively high ICR with fewer turns. This yields consistently higher efficiency, suggesting that these models ask more targeted questions and extract salient evidence earlier.
L457: Meditron3-8B frequently reaches the maximum turn budget but attains low ICR, indicating limited capability in interactive information collection.
L458: Among strategies, ReAct typically improves efficiency even when the absolute ICR gain is modest. REFINE more often increases ICR by extending the interaction, but this additional turn cost can lead to lower efficiency than ReAct.
L459: ## Appendix D Latency
L460: 
L461: Table 7: Average per-turn latency relative to Baseline.
L462: Strategy  | Avg. Turn Latency
L463: --- | ---
L464: Baseline  | $\times 1.00$
L465: ReAct  | $\times 3.85$
L466: SC  | $\times 10.22$
L467: REFINE  | $\times 16.48$
L468: 
L469: We report per-turn latency for the doctor agent as a proxy for interactive efficiency. A turn is timed from when the doctor receives the turn-level visible context to when the doctor finishes generating the next action. This proxy reflects user-perceived responsiveness in deployment settings.
L470: Experiments are run locally on a single NVIDIA A6000 GPU using vLLM with Qwen2.5-7B. All numbers are averaged over five datasets.
L471: 
L472: Table cite61†7 shows that strategies with explicit reasoning traces or additional internal steps increase per-turn latency. These results highlight a practical trade-off between accuracy improvements and runtime cost.
L473: ## Appendix E Strategy Prompts
L474: 
L475: This appendix lists all prompts used by different strategies.
L476: 
L477: #### Baseline.
L478: 
L479: The Baseline strategy includes only a doctor agent.
L480: 
L481: ⬇
L482: # Role: Doctor
L483: 
L484: You are a licensed physician conducting a medical consultation.
L485: 
L486: {task_description}
L487: 
L488: Your objective is to efficiently gather information and request necessary clinical examinations or laboratory tests to enable a subsequent diagnostic analysis.
L489: 
L490: You have access to a Medical Analyst who can retrieve specific test results upon request.
L491: 
L492: You must adhere to the following operational constraints:
L493: 
L494: 1. Efficiency: Gather sufficient information in as few turns as possible.
L495: 2. Turn Limit: You strictly cannot exceed {max_turns} total turns.
L496: 
L497: 3. No Repetition: Never ask a question or request a test that has already been covered.
L498: 
L499: 4. Atomic Inquiries: Each question must address a single, specific topic.
L500: 
L501: For example, ask "What are your symptoms?" and never combine multiple questions.
L502: 
L503: In every turn, you execute one of the following actions in the corresponding format:
L504: 
L505: 1. [QUERY] followed by your atomic question to the patient.
L506: 2. [TEST] followed by one specific examination or diagnostic test request to the Medical Analyst.
L507: 
L508: 3. [DIAGNOSIS] followed by {task_output_format}
L509: 
L510: Once you have gathered sufficient evidence, ensure your diagnosis is final.
L511: #### ReAct.
L512: 
L513: The ReAct strategy also includes only a doctor agent.
L514: 
L515: ⬇
L516: # Role: Doctor (ReAct)
L517: 
L518: You are a licensed physician conducting a medical consultation.
L519: 
L520: {task_description}
L521: 
L522: Your objective is to efficiently gather information and request necessary clinical examinations or laboratory tests to enable a subsequent diagnostic analysis.
L523: 
L524: You have access to a Medical Analyst who can retrieve specific test results upon request.
L525: 
L526: You must adhere to the following operational constraints:
L527: 
L528: 1. Efficiency: Gather sufficient information in as few turns as possible.
L529: 2. Turn Limit: You strictly cannot exceed {max_turns} total turns.
L530: 
L531: 3. No Repetition: Never ask a question or request a test that has already been covered.
L532: 
L533: 4. Atomic Inquiries: Each question must address a single, specific topic.
L534: 
L535: For example, ask "What are your symptoms?" and never combine multiple questions.
L536: 
L537: In every turn, you must follow a strict Reasoning-then-Acting process using the following format exactly.
L538: 
L539: [THOUGHT] <Your Clinical Reasoning>

## Original response 7: jan29_stdnext5finish

Strong Reasoning Isn’t Enough: Evaluating Evidence Elicitation in Interactive Diagnosis (https://arxiv.org/html/2601.19773v1)
citeturn28464view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19773v1","lineno":344}); Total lines: 684
L273: We implement an interactive diagnostic environment with three roles: a doctor agent, a simulated patient, and a simulated reporter. All roles are instantiated using the CAMEL multi-agent framework li2023camel. Both the simulated patient and the simulated reporter operate with a context window of 1 and a temperature of 0, resulting in stateless behavior with respect to dialogue history and deterministic decoding across all experiments.
L274: This design choice reduces simulator drift over long conversations and improves stability across runs.
L275: The patient prompt is shown below:
L276: 
L277: ⬇
L278: 
L279: You are a patient undergoing a medical interview.
L280: 
L281: Your knowledge is strictly limited to the following list of indexed facts:
L282: 
L283: {patient_evidences}
L284: 
L285: Response protocols:
L286: 
L287: 1. Analyze the doctor question and search your list for the specific item or items that contain the answer.
L288: 
L289: 2. Format your output using two tags:
L290: 
L291: [REFERENCE] followed by the exact string or strings including the index from your list.
L292: 
L293: You may select up to two facts if necessary.
L294: If no fact exists write N/A.
L295: 
L296: [RESPONSE] followed by a natural language answer derived strictly from the selected references.
L297: 
L298: Do not add outside information.
L299: 
L300: 3. If the doctor question is not addressed by any fact in your list.
L301: 
L302: [REFERENCE] N/A
L303: 
L304: [RESPONSE] indicate that you are unsure or do not recall.
L305: 
L306: The reporter prompt is shown below:
L307: 
L308: ⬇
L309: 
L310: You are a specialized module named Measurement responsible for reporting test results to the physician.
L311: 
L312: You have access to the following list of indexed facts.
L313: Physical examination and diagnostic test data
L314: 
L315: {examination_evidences}
L316: 
L317: Response protocols:
L318: 
L319: 1. Search the provided list for all facts that are relevant to the doctor specific test request. Do not provide information that was not explicitly requested.
L320: 
L321: 2. Return the relevant facts exactly as they appear in the source list including their indices.
L322: 
L323: 3. If the requested test results are not found in the list assume the finding is non-significant and return Normal.
L324: ### A.2 Automatic Evaluation
L325: 
L326: Following the original benchmarks, DiagnosisArena, RareArena, and ClinicalBench are differential diagnosis tasks where the model outputs five diseases ranked by likelihood. AgentClinic-MedQA and Derm are direct diagnosis tasks that require a single diagnosis.
L327: For direct diagnosis tasks, we evaluate whether the doctor predicted diagnosis matches the reference diagnosis. We use an LLM judge that outputs a binary decision with no additional text. The judge prompt for direct diagnosis is shown below.
L328: 
L329: ⬇
L330: 
L331: You determine whether the correct diagnosis and the doctor diagnosis refer to the same disease.
L332: 
L333: Respond only with Yes or No.
L334: 
L335: Correct diagnosis
L336: 
L337: {answer}
L338: 
L339: Doctor output
L340: 
L341: {diagnosis}
L342: 
L343: Are these the same disease?
L344: For differential diagnosis tasks, the doctor outputs five differential diagnoses. We use an LLM judge to score each of the five items against the reference diagnosis using a three-level rubric. A score of two indicates an exact match, a score of one indicates a broader category that contains the reference diagnosis, and a score of zero otherwise. We compute success rate (SR) using top-1 accuracy by checking whether the first listed diagnosis receives a score of two.
L345: The judge prompt for differential diagnosis scoring is shown below:
L346: 
L347: ⬇
L348: 
L349: You diagnose challenging cases.
L350: 
L351: You receive a student answer containing five differential diagnoses and a reference diagnosis.
L352: 
L353: Score each diagnosis using the rules below.
L354: 
L355: 2 The student diagnosis exactly matches the reference diagnosis.
L356: 
L357: 1 The student diagnosis is a broad category that includes the reference diagnosis.
L358: 
L359: 0 The student diagnosis does not meet the criteria for 1 or 2.
L360: 
L361: Student answer
L362: 
L363: {student_answer}
L364: Reference diagnosis
L365: 
L366: {final_diagnosis}
L367: 
L368: Output the scores in the format below and do not output anything else.
L369: 
L370: 1 Disease 1 Name \boxed{score}
L371: 
L372: 2 Disease 2 Name \boxed{score}
L373: 
L374: 3 Disease 3 Name \boxed{score}
L375: 
L376: 4 Disease 4 Name \boxed{score}
L377: 
L378: 5 Disease 5 Name \boxed{score}
L379: ## Appendix B EviMed Construction Details
L380: ### B.1 Data Sources and Sampling
L381: 
L382: EviMed-1K integrates five complementary sources that cover general medicine, specialty diagnosis, complex multi-specialty reasoning, rare diseases, and real-world clinical records. We sample 200 cases from each source to form a 1,000-case evaluation set.
L383: AgentClinic-MedQA schmidgall2024agentclinic is a pure-text interactive clinical diagnosis dataset within the AgentClinic benchmark. It contains 215 cases adapted from MedQA USMLE case challenges and rewritten into OSCE-style multi-round consultation scenarios. The initial JSON cases were auto-filled using GPT-4 and then manually verified to ensure consistency and usability. We randomly sample 200 cases to evaluate sequential information gathering and diagnosis under incomplete evidence.
L384: Derm johri2024craft evaluates dermatology diagnosis with a public split (Derm-Public) and a clinician-authored split (Derm-Private). Derm-Public contains 100 case-based questions collected from an online question bank. Derm-Private contains 100 case-based questions newly written by three dermatologists with similar structure and different condition coverage to reduce leakage risk. We include the full set of 200 cases to test detailed symptom inquiry in a specialized domain.
L385: DiagnosisArena zhu2025diagnosisarena is constructed from real-world case reports published in top-tier medical journals such as NEJM, The Lancet, and JAMA. It extracts and structures diagnostic information including history, physical examination, and tests while removing treatment and prognosis content to reduce answer leakage. The benchmark focuses on open-ended differential diagnosis without restricting candidates to a predefined list. We randomly sample 200 cases from the dataset.
L386: RareArena zhao2025rarearena is a large-scale rare disease benchmark built from PubMed Central (PMC) case reports and mapped to the Orphanet ORPHAcode system. It includes Rare Disease Screening (RDS) and Rare Disease Confirmation (RDC) settings that reflect different stages of the diagnostic process. To reflect the long-tail distribution and synonym variability, we sample 200 distinct diseases using a frequency-stratified scheme.
L387: Specifically, diseases are drawn in a 2:2:1 ratio from low-frequency (appearing once), mid-frequency (appearing 2–5 times), and high-frequency (appearing more than 5 times) strata based on their occurrence counts in the corpus.
L388: ClinicalBench yan2024clinicallab is derived from de-identified electronic medical records with both structured and unstructured content. It covers 24 clinical departments and primarily includes common diseases with clear diagnostic pathways that require multi-source clinical evidence. The cases reflect realistic combinations of history, examination, imaging, and laboratory findings. We sample 200 cases to ensure broad coverage across disease categories and specialties represented in the dataset.
L389: ### B.2 Automatic Evidence Construction
L390: 
L391: The prompt used to automatically construct atomic patient and examination evidences is shown below.
L392: 
L393: ⬇
L394: 
L395: Break the following information into independent atomic facts.
L396: 
L397: Rules
L398: 
L399: - One piece of information per statement.
L400: 
L401: - Facts must be self-contained and non-overlapping.
L402: 
L403: - Do NOT add, infer, or normalize beyond the given text.
L404: 
L405: - Keep the original language of the input.
L406: 
L407: - Each fact string must start with an index such as "1. ", "2. ", and so on.
L408: - Classify each fact into either patient_facts or exam_facts.
L409: 
L410: - patient_facts include demographics, history, symptoms, complaints, and clinical presentation.
L411: 
L412: - exam_facts include examinations, tests, laboratory results, and imaging studies.
L413: 
L414: - Do NOT duplicate facts across patient_facts and exam_facts.
L415: 
L416: If a fact could belong to both, choose the best list and omit it from the other.
L417: 
L418: - If there is no content for a list, return an empty list.
L419: 
L420: Case information in JSON
L421: 
L422: {case_json}
L423: ## Appendix C Interaction Turns
L424: 
L425: Table 6: Average interaction turns (Turns), Information Coverage Rate (ICR, %), and Turn Efficiency (Effi. = ICR / Turns) under different strategies across datasets.
L426: Model  | ClinicalBench  | Derm  | AgentClinic-MedQA  | DiagnosisArena  | RareArena
L427:  | Turns  | ICR  | Effi.  | Turns  | ICR  | Effi.  | Turns  | ICR  | Effi.  | Turns  | ICR  | Effi.  | Turns  | ICR  | Effi.
L428: Baseline
L429: ---
L430: GPT-5  | 12.1  | 35.2  | 2.91  | 6.8  | 54.9  | 8.07  | 7.4  | 31.3  | 4.23  | 11.1  | 55.4  | 4.99  | 12.3  | 42.7  | 3.47
L431: GPT-5-mini  | 12.5  | 31.3  | 2.50  | 10.3  | 51.7  | 5.02  | 10.9  | 33.0  | 3.03  | 12.8  | 47.2  | 3.69  | 12.9  | 35.7  | 2.77
L432: DeepSeek-v3.2  | 12.7  | 46.7  | 3.68  | 12.0  | 77.0  | 6.42  | 11.3  | 44.3  | 3.92  | 12.1  | 63.4  | 5.24  | 12.6  | 49.1  | 3.90
L433: GLM-4.6  | 8.6  | 32.6  | 3.79  | 7.2  | 65.7  | 9.13  | 7.5  | 36.6  | 4.88  | 8.2  | 52.1  | 6.35  | 9.2  | 37.8  | 4.11
L434: Qwen2.5-72B  | 8.2  | 40.8  | 4.98  | 8.7  | 67.5  | 7.76  | 7.9  | 41.7  | 5.28  | 7.9  | 55.5  | 7.03  | 8.0  | 41.6  | 5.20
L435: Qwen2.5-32B  | 7.9  | 39.0  | 4.94  | 8.1  | 71.6  | 8.84  | 7.1  | 37.3  | 5.25  | 7.7  | 57.0  | 7.40  | 8.3  | 43.0  | 5.18

## Original response 8: jan29_stdnext5last

Strong Reasoning Isn’t Enough: Evaluating Evidence Elicitation in Interactive Diagnosis (https://arxiv.org/html/2601.19773v1)
citeturn28465view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19773v1","lineno":175}); Total lines: 684
L161: DeepSeek-v3.2  | 63.0  | 46.7  | $\mathbf{51.0}_{(-19\%)}$  | 80.5  | 77.0  | $65.0_{(-19\%)}$  | 56.5  | 63.4  | $21.5_{(-62\%)}$  | 92.5  | 44.3  | $70.5_{(-24\%)}$  | 61.5  | 49.1  | $24.5_{(-60\%)}$
L162: GLM-4.6  | 60.5  | 32.6  | $45.0_{(-26\%)}$  | 78.5  | 65.7  | $66.0_{(-16\%)}$  | 52.0  | 52.1  | $23.0_{(-56\%)}$  | 86.0  | 36.6  | $72.0_{(-16\%)}$  | 59.0  | 37.8  | $21.5_{(-64\%)}$
L163: Qwen2.5-72B  | 64.5  | 40.8  | $43.5_{(-33\%)}$  | 59.0  | 67.5  | $43.0_{(-27\%)}$  | 24.5  | 55.5  | $10.0_{(-59\%)}$  | 75.5  | 41.7  | $54.0_{(-29\%)}$  | 32.0  | 41.6  | $10.5_{(-67\%)}$
L164: Qwen2.5-32B  | 60.0  | 39.0  | $48.0_{(-20\%)}$  | 49.5  | 71.6  | $35.0_{(-29\%)}$  | 20.0  | 57.0  | $8.0_{(-60\%)}$  | 76.5  | 37.3  | $52.0_{(-32\%)}$  | 29.0  | 43.0  | $6.0_{(-79\%)}$
L165: Qwen2.5-7B  | 52.0  | 41.0  | $35.5_{(-32\%)}$  | 37.5  | 71.9  | $20.0_{(-47\%)}$  | 13.0  | 53.1  | $8.0_{(-39\%)}$  | 60.5  | 43.5  | $43.0_{(-29\%)}$  | 19.5  | 41.2  | $5.0_{(-74\%)}$
L166: Llama-3.1-8B  | 37.0  | 40.5  | $34.5_{(-7\%)}$  | 38.5  | 74.4  | $25.5_{(-34\%)}$  | 14.0  | 57.3  | $6.0_{(-57\%)}$  | 67.0  | 47.8  | $57.5_{(-14\%)}$  | 23.0  | 45.0  | $9.0_{(-61\%)}$
L167: Meditron3-8B  | 42.5  | 23.4  | $20.0_{(-53\%)}$  | 43.0  | 39.7  | $19.0_{(-56\%)}$  | 10.5  | 33.7  | $2.5_{(-76\%)}$  | 68.0  | 28.7  | $20.5_{(-70\%)}$  | 25.5  | 23.2  | $2.5_{(-90\%)}$
L168: Qwen2.5-3B  | 38.0  | 33.8  | $30.0_{(-21\%)}$  | 24.0  | 74.1  | $11.5_{(-52\%)}$  | 9.5  | 47.7  | $5.5_{(-42\%)}$  | 49.5  | 43.7  | $35.5_{(-28\%)}$  | 9.5  | 35.1  | $2.0_{(-79\%)}$
L169: Table 3: Comparison of representative models under different interactive strategies across datasets. Bold indicates the best performance for the same model on the same dataset.
L170: Dataset  | Model  | Baseline  | ReAct  | SC  | REFINE
L171: --- | --- | --- | --- | --- | ---
L172: ICR (%)$\uparrow$  | SR (%)$\uparrow$  | ICR (%)$\uparrow$  | SR (%)$\uparrow$  | ICR (%)$\uparrow$  | SR (%)$\uparrow$  | ICR (%)$\uparrow$  | SR (%)$\uparrow$
L173: --- | --- | --- | --- | --- | --- | --- | ---
L174: ClinicalBench  | GPT-5-mini  | 31.3  | 46.5  | 33.5  | 49.5  | 41.5  | 49.0  | 43.5  | 49.5
L175: Qwen2.5-72B  | 40.8  | 43.5  | 38.7  | 42.0  | 43.2  | 49.5  | 51.1  | 53.0
L176: Qwen2.5-7B  | 41.0  | 35.5  | 29.8  | 33.0  | 32.5  | 35.0  | 35.3  | 38.5
L177: Derm  | GPT-5-mini  | 51.7  | 57.5  | 59.5  | 62.0  | 70.9  | 66.5  | 76.7  | 66.0
L178: Qwen2.5-72B  | 67.5  | 43.0  | 71.2  | 45.0  | 77.9  | 45.5  | 80.8  | 44.0
L179: Qwen2.5-7B  | 71.9  | 20.0  | 63.5  | 23.0  | 62.8  | 25.0  | 67.1  | 28.5
L180: DiagnosisArena  | GPT-5-mini  | 47.2  | 23.0  | 53.9  | 29.5  | 60.8  | 39.5  | 64.6  | 42.0
L181: Qwen2.5-72B  | 55.5  | 10.0  | 58.9  | 12.5  | 63.4  | 15.5  | 73.8  | 18.5
L182: Qwen2.5-7B  | 53.1  | 8.0  | 45.1  | 3.5  | 53.6  | 10.5  | 50.8  | 13.0
L183: AgentClinic-MedQA  | GPT-5-mini  | 33.0  | 61.0  | 33.2  | 67.0  | 40.2  | 69.5  | 45.5  | 68.0
L184: Qwen2.5-72B  | 41.7  | 54.0  | 39.5  | 59.0  | 43.6  | 62.0  | 53.9  | 64.5
L185: Qwen2.5-7B  | 43.5  | 43.0  | 35.8  | 45.0  | 36.0  | 44.5  | 38.6  | 45.5
L186: RareArena  | GPT-5-mini  | 35.7  | 15.5  | 39.3  | 24.0  | 46.2  | 30.5  | 51.8  | 32.0
L187: Qwen2.5-72B  | 41.6  | 10.5  | 47.4  | 13.0  | 50.1  | 15.5  | 59.9  | 17.0
L188: Qwen2.5-7B  | 41.2  | 5.0  | 29.8  | 2.5  | 37.0  | 5.5  | 38.2  | 7.5
L189: ### 5.3 Strategy Comparison
L190: 
L191: We compare interaction strategies to assess their effects on ICR and SR. We report results for GPT-5-mini, Qwen2.5-72B, and Qwen2.5-7B in Table cite51†3 .
L192: 
L193: From the results, ReAct improves both ICR and SR for stronger models such as GPT-5-mini and Qwen2.5-72B. However, for the weaker model Qwen2.5-7B, ReAct decreases both ICR and SR. This may reflect increased difficulty under longer multi-turn trajectories laban2025llms, which is also suggested by Section cite21†5.7 .
L194: In contrast, SC more consistently improves both ICR and SR across the evaluated models. This strategy likely benefits from separating information collection from the final diagnosis, which helps the agent remain focused on evidence acquisition. Moreover, making the diagnosis based on a structured summary may mitigate reasoning degradation in long conversations.
L195: REFINE achieves the highest ICR across most datasets and models. The improvements are especially pronounced on the challenging DiagnosisArena and RareArena datasets. These results support reasoning-based feedback as an effective mechanism for aligning information collection with downstream diagnostic needs.
L196: 
L197: cite52†Image: Refer to caption Figure 4: Relationship between average Information Coverage Rate and Success Rate under interactive evaluation, with values averaged over the five datasets.
L198: ### 5.4 Relationship between ICR and SR
L199: 
L200: To better understand the relationship between evidence acquisition ability and diagnostic performance, we analyze the relationship between Information Collection Rate (ICR) and Success Rate (SR) across models and strategies. We include the interactive results of all models reported in Section cite16†5.2 , as well as the strategy variants for selected representative models in Section cite17†5.3 . The corresponding scatter plots are shown in Figure cite53†4 .
L201: We observe that SR generally correlates with ICR across models. For example, performance increases from GPT-5-mini to GLM-4.6 to DeepSeek-v3.2, and from Meditron3-8B to Llama-3.1-8B, in terms of both ICR and SR. However, this relationship is not always consistent. For instance, the GPT-5 series exhibits relatively high SR but comparatively low ICR, whereas the Qwen2.5 series shows high ICR but lower SR.

## Original response 9: jan29_stdnext5last

Strong Reasoning Isn’t Enough: Evaluating Evidence Elicitation in Interactive Diagnosis (https://arxiv.org/html/2601.19773v1)
citeturn28465view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19773v1","pattern":"judge"}); Total lines: 684
L275: The patient prompt is shown below:
L276: 
L277: ⬇
L278: 
L279: You are a patient undergoing a medical interview.
L280: 
L281: Your knowledge is strictly limited to the following list of indexed facts:
L282: 
L283: {patient_evidences}
L284: 
L285: Response protocols:
L286: 
L287: 1. Analyze the doctor question and search your list for the specific item or items that contain the answer.
L288: 
L289: 2. Format your output using two tags:
L290: 
L291: [REFERENCE] followed by the exact string or strings including the index from your list.
L292: 
L293: You may select up to two facts if necessary.
L294: If no fact exists write N/A.
L295: 
L296: [RESPONSE] followed by a natural language answer derived strictly from the selected references.
L297: 
L298: Do not add outside information.
L299: 
L300: 3. If the doctor question is not addressed by any fact in your list.
L301: 
L302: [REFERENCE] N/A
L303: 
L304: [RESPONSE] indicate that you are unsure or do not recall.
L305: 
L306: The reporter prompt is shown below:
L307: 
L308: ⬇
L309: 
L310: You are a specialized module named Measurement responsible for reporting test results to the physician.
L311: 
L312: You have access to the following list of indexed facts.
L313: Physical examination and diagnostic test data
L314: 
L315: {examination_evidences}
L316: 
L317: Response protocols:
L318: 
L319: 1. Search the provided list for all facts that are relevant to the doctor specific test request. Do not provide information that was not explicitly requested.
L320: 
L321: 2. Return the relevant facts exactly as they appear in the source list including their indices.
L322: 
L323: 3. If the requested test results are not found in the list assume the finding is non-significant and return Normal.
L324: ### A.2 Automatic Evaluation
L325: 
L326: Following the original benchmarks, DiagnosisArena, RareArena, and ClinicalBench are differential diagnosis tasks where the model outputs five diseases ranked by likelihood. AgentClinic-MedQA and Derm are direct diagnosis tasks that require a single diagnosis.
L327: For direct diagnosis tasks, we evaluate whether the doctor predicted diagnosis matches the reference diagnosis. We use an LLM judge that outputs a binary decision with no additional text. The judge prompt for direct diagnosis is shown below.
L328: 
L329: ⬇
L330: 
L331: You determine whether the correct diagnosis and the doctor diagnosis refer to the same disease.
L332: 
L333: Respond only with Yes or No.
L334: 
L335: Correct diagnosis
L336: 
L337: {answer}
L338: 
L339: Doctor output
L340: 
L341: {diagnosis}
L342: 
L343: Are these the same disease?
L344: For differential diagnosis tasks, the doctor outputs five differential diagnoses. We use an LLM judge to score each of the five items against the reference diagnosis using a three-level rubric. A score of two indicates an exact match, a score of one indicates a broader category that contains the reference diagnosis, and a score of zero otherwise. We compute success rate (SR) using top-1 accuracy by checking whether the first listed diagnosis receives a score of two.
L345: The judge prompt for differential diagnosis scoring is shown below:
L346: 
L347: ⬇
L348: 
L349: You diagnose challenging cases.
L350: 
L351: You receive a student answer containing five differential diagnoses and a reference diagnosis.
L352: 
L353: Score each diagnosis using the rules below.
L354: 
L355: 2 The student diagnosis exactly matches the reference diagnosis.
L356: 
L357: 1 The student diagnosis is a broad category that includes the reference diagnosis.
L358: 
L359: 0 The student diagnosis does not meet the criteria for 1 or 2.
L360: 
L361: Student answer
L362: 
L363: {student_answer}
L364: Reference diagnosis
L365: 
L366: {final_diagnosis}
L367: 
L368: Output the scores in the format below and do not output anything else.
L369: 
L370: 1 Disease 1 Name \boxed{score}
L371: 
L372: 2 Disease 2 Name \boxed{score}
L373: 
L374: 3 Disease 3 Name \boxed{score}
L375: 
L376: 4 Disease 4 Name \boxed{score}
L377: 
L378: 5 Disease 5 Name \boxed{score}
L379: ## Appendix B EviMed Construction Details
L380: ### B.1 Data Sources and Sampling
L381: 
L382: EviMed-1K integrates five complementary sources that cover general medicine, specialty diagnosis, complex multi-specialty reasoning, rare diseases, and real-world clinical records. We sample 200 cases from each source to form a 1,000-case evaluation set.
L383: AgentClinic-MedQA schmidgall2024agentclinic is a pure-text interactive clinical diagnosis dataset within the AgentClinic benchmark. It contains 215 cases adapted from MedQA USMLE case challenges and rewritten into OSCE-style multi-round consultation scenarios. The initial JSON cases were auto-filled using GPT-4 and then manually verified to ensure consistency and usability. We randomly sample 200 cases to evaluate sequential information gathering and diagnosis under incomplete evidence.
L384: Derm johri2024craft evaluates dermatology diagnosis with a public split (Derm-Public) and a clinician-authored split (Derm-Private). Derm-Public contains 100 case-based questions collected from an online question bank. Derm-Private contains 100 case-based questions newly written by three dermatologists with similar structure and different condition coverage to reduce leakage risk. We include the full set of 200 cases to test detailed symptom inquiry in a specialized domain.
L385: DiagnosisArena zhu2025diagnosisarena is constructed from real-world case reports published in top-tier medical journals such as NEJM, The Lancet, and JAMA. It extracts and structures diagnostic information including history, physical examination, and tests while removing treatment and prognosis content to reduce answer leakage. The benchmark focuses on open-ended differential diagnosis without restricting candidates to a predefined list. We randomly sample 200 cases from the dataset.
L386: RareArena zhao2025rarearena is a large-scale rare disease benchmark built from PubMed Central (PMC) case reports and mapped to the Orphanet ORPHAcode system. It includes Rare Disease Screening (RDS) and Rare Disease Confirmation (RDC) settings that reflect different stages of the diagnostic process. To reflect the long-tail distribution and synonym variability, we sample 200 distinct diseases using a frequency-stratified scheme.
L387: Specifically, diseases are drawn in a 2:2:1 ratio from low-frequency (appearing once), mid-frequency (appearing 2–5 times), and high-frequency (appearing more than 5 times) strata based on their occurrence counts in the corpus.
L388: ClinicalBench yan2024clinicallab is derived from de-identified electronic medical records with both structured and unstructured content. It covers 24 clinical departments and primarily includes common diseases with clear diagnostic pathways that require multi-source clinical evidence. The cases reflect realistic combinations of history, examination, imaging, and laboratory findings. We sample 200 cases to ensure broad coverage across disease categories and specialties represented in the dataset.
L389: ### B.2 Automatic Evidence Construction
L390: 
L391: The prompt used to automatically construct atomic patient and examination evidences is shown below.
L392: 
L393: ⬇
L394: 
L395: Break the following information into independent atomic facts.
L396: 
L397: Rules
L398: 
L399: - One piece of information per statement.
L400: 
L401: - Facts must be self-contained and non-overlapping.
L402: 
L403: - Do NOT add, infer, or normalize beyond the given text.
L404: 
L405: - Keep the original language of the input.
L406: 
L407: - Each fact string must start with an index such as "1. ", "2. ", and so on.
L408: - Classify each fact into either patient_facts or exam_facts.
L409: 
L410: - patient_facts include demographics, history, symptoms, complaints, and clinical presentation.
L411: 
L412: - exam_facts include examinations, tests, laboratory results, and imaging studies.
L413: 
L414: - Do NOT duplicate facts across patient_facts and exam_facts.
L415: 
L416: If a fact could belong to both, choose the best list and omit it from the other.
L417:

