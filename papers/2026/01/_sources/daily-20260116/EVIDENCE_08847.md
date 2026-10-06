# 2601.08847v1 — 必要证据审阅

精确源：https://arxiv.org/html/2601.08847v1；实际阅读：§3–4、§6.6。

RIKER先SQLite entities/relations groundtruth再template文档，global entity pools保持跨文档coherence；SQL求count/set/temporal reference；L11 unused entities vs L12 absentoptionalfield分别unknown/N-A，exact/numeric/set/structure known equivalence deterministic matcher。本文只contextstuffing，非已验证RAG/agent；32K/128K/200K、temperature.4、8runs，模型数33/24/11不同不可当pairedlongcontext因果结论。Crosscorpus fourseed保持结构但documentcounts369/420/385/368，freshseed不能逻辑保证训练无contamination，也不保证真实enterprise代表性。英文lease/fieldreport/HR，未includeOCR/conflicts/jargon。采用groundtruth-first&query-type分解，不采用排行榜、21Btokens泛化或无限合成真实validity。校准后6分(2+2+2)：consistentrelationalgenerator→deterministic scorer具体接口增量；标准必要阅读足够。拟已有覆盖：PLATFORM-EVALUATION-SYSTEM，Ch66 L1709–1738 canonicalfactledger→rendered events→query、L1293–1326 generatorpopulation/answerability、L4183–4194 constraintgraph/stateverifier；待root非作者通过。

## 实际源核心（不作为论文全附件审阅声明）

Root 非作者实际核SQL/template、L11/12、matcher与§6.6，读Ch66 canonicalledger和generatorpopulation正文；6分标准、已有覆盖通过。仅采用truth-before-render/deterministicscorer/answerability范围，不授无污染保证。不授日级/日期Gate。

3  The RIKER Approach
Unlike benchmarks that rely on static datasets or LLM-as-judge evaluation, RIKER generates synthetic corpora from embedded ground truth, enabling deterministic scoring at scale. The methodology is application-agnostic - it can evaluate context-stuffing, retrieval-augmented generation, or knowledge graph systems by instrumenting the system under test to answer RIKER-generated questions.
3.1  Synthetic Corpus Generation
RIKER employs a ground-truth-first architecture: the complete knowledge base—all entities, relationships, and facts—is populated in a relational database 
before
 any document is generated. Documents are then rendered as human-readable views of this underlying ground truth. This inversion of the typical “extract facts from documents”approach provides three key advantages: (1) every question has a verifiable answer by construction, enabling deterministic scoring, (2) corpora can be regenerated with different random seeds while maintaining structural equivalence, enabling robustness validation, and (3) the approach is easily scalable to practically-unlimited scale, requiring no human-intensive document annotation.
3.1.1  Synthetic Data Generation
Built upon the PICARD framework 
49
, RIKER inherits and expands various synthetic data generation functions - names, amounts, dates, and other entities - which are used to generate a diverse set of ground truth elements, from which documents will later be created.
3.1.2  Ground Truth Database
All generated ground truth is recorded in a SQLite database with full relational structure. For example, for a lease document corpus, this includes:
•
Document metadata (parties, dates, amounts, clauses present, clauses absent)
•
Entities (lessors, lessees, agents, addresses, etc.)
•
Entity relationships (which lessors have which lessees)
This database serves as the authoritative answer key for all generated questions. Questions that require computed aggregations (counts, sums, temporal relationships) can be derived from this ground truth through SQL, which enables complex test question generation (e.g. ”What is the total monthly rent of all leases $LESSOR has in $YEAR and $MONTH”)
3.1.3  Template-Based Document Generation
After the ground truth database is created, documents are generated using modular templates with controlled variation. Each template defines the document structure while allowing randomized selection of:
•
Language style (formal, semi-formal, casual)
•
Structural organization (section ordering, optional clauses)
•
Boilerplate text variations
This produces documents that are structurally consistent yet superficially diverse, preventing models from exploiting surface-level patterns while maintaining ground truth integrity.
3.2  Coherent Simulated Universe
One of the significant shortcomings of synthetic generated data comes from naive generation - that is, when 100 synthetic documents are generated, but they are all 
independent generations
. This gives the synthetic data set a characteristic that is very 
un-enterprise-like
 - the documents are not related to each other, or worse, they have chaotic and unrealistic connections.
For example, in a naive generation, we could generate 100 HR documents using a pool of human names. Being independently randomly generated, our documents (for example, HR evaluations or employee information) would naively randomize facts like employee name, manager, department, etc. The result is a dataset that models no realistic enterprise corpus, for example:
•
Employees in similar randomized department (by chance) will have a different dept manager or supervisor named
•
Employees in different departments may accidentally have a similar randomized person name
•
An employee, named as a manager or supervisor in a particular department from a previous document, can have a different department or position
The above is not an exhaustive list. This incoherence resulting from naive random generation is a problem. It does not model a realistic enterprise scenario (therefore metrics against that dataset may have very weak correlation to real-world performance), and will prevent the creation of challenging comprehension and aggregation questions, such as 
‘which manager gave the most evaluations this quarter?’
, because necessary relationships will either not be diverse or coherent enough, or may not even exist at all.
RIKER solves this problem through its 
Coherent Simulated Universe
 approach. The very first step in document generation is ground truth creation (see 
3.1.2
), and this includes necessary relationships among the different entities. To make this coherence spread across different document types and across the entire universe of generated documents, RIKER has the concept of 
Global Entity Pools
, which are pre-generated and filled as the first step of synthetic data generation. Relationships are then created by drawing from the global entity pools, which are saved in the ground truth database. These global entity pools are used across all document types to create a coherent dataset. For example, a global entity pool called ‘sales_agent’ contains human names that are used for three types of documents in the current RIKER implementation:
•
An 
optional sales agent
 that is named and credited for closing a 
Lease Contract
•
A 
sales agent
 that is named in a 
Sales Agent Field Report
, as the agent who created and submitted the field report detailing sales activities and potential contract status
•
An 
employee
 that is named in an 
HR Employee Evaluation
 document, as the sales employee being evaluated
In RIKER’s Coherent Simulated Universe, all the three document types above (in bold) draw from the same Global Entity Pool - meaning the agents you will see who closed lease contracts will be the same agents named in relevant field reports, and named in relevant HR evaluation documents.
It will also never happen that a Field Report talking about a particular Lease Contract will have a different human name randomized for it as the sales agent - this incoherence is avoided through logic specifically baked-in to the document generation feature, as part of the Coherent Simulated Universe strategy.
This results in having arbitrary scale document generation where ground truth is immediately available with no human annotation effort (because ground truth is where the process actually begins), and the knowledge generated - the entire set of facts and documents - are coherent according to the generation design.
3.3  Multi-Level Question Taxonomy
RIKER generates questions across twelve difficulty levels organized into three categories, each testing distinct capabilities.
3.3.1  Single-Document Questions (L01 - L04)
These questions require locating and extracting information from a single document:
•
L01 - Direct Extraction:
 Surface-level facts stated explicitly (“What is the monthly rent?”)
•
L02 - Indirect Extraction:
 Facts requiring minimal inference (“What is the lease duration?” when start/end dates are given)
•
L03 - Conditional Extraction:
 Facts from optional document sections (“What is the pet deposit?” — may be N/A)
•
L04 - Complex Extraction:
 Facts requiring multiple conditions or cross-referencing within a document
3.3.2  Aggregation Questions (L05 - L10)
These questions require synthesizing information across multiple documents:
•
L05 - Counting:
 “How many leases does Lessor X have?”
•
L06 - Summation/Averaging:
 “What is the total monthly rent across all leases?”
•
L07 - Comparison:
 “Which lessor has more leases, X or Y?”
•
L08 - Enumeration:
 “List all lessees for Lessor X”
•
L09 - Multi-hop:
 “What is Lessor X’s most recent lease end date?”
•
L10 - Temporal:
 “How many leases were active in Q3 2024?”
Aggregation questions are particularly challenging because they require the model to: (1) identify all relevant documents, (2) extract the relevant facts from each, and (3) perform the required computation correctly.
3.3.3  Hallucination Probe Questions (L11 - L12)
These questions are designed to detect fabrication:
•
L11 - Non-existent Entities:
 Questions about entities that do not appear anywhere in the corpus. The entity names are drawn from unused portions of the entity pool, ensuring they are plausible but definitively absent. The only correct response is “Unknown” or equivalent.
•
L12 - Absent Information:
 Questions about optional fields that are absent from specific documents. For example, asking about the pet deposit for a lease that has no pet clause. The only correct response is “N/A” or equivalent.
L11 questions are particularly valuable because any specific answer constitutes unambiguous fabrication—the model cannot have retrieved the information from the corpus because it does not exist.
3.4  Deterministic Scoring
RIKER employs answer-key-based scoring, eliminating the variability inherent in LLM-as-judge approaches.
3.4.1  Scoring Mechanisms
Each question specifies its scoring type:
•
Exact match:
 For categorical responses (names, yes/no)
•
Numeric extraction:
 Parses numerical answers with tolerance for formatting variations
•
Set comparison:
 For enumeration questions, compares answer sets regardless of ordering
•
Semantic equivalence:
 For structured responses with known equivalent forms
All scoring logic operates against the ground truth database, ensuring reproducibility. The same model outputs will always receive the same scores.
In this particular
3.4.2  Response Format Enforcement
Questions include explicit format instructions (e.g., “Reply with only the number” or “Indicate your final answer with: Final answer: [your answer]”). This structured output requirement reduces ambiguity in answer extraction and improves scoring reliability.
3.5  Fidelity Metrics Taxonomy
We define a three-level taxonomy for hallucination-related metrics
3.5.1  Faithfulness (L01 - L04 + L11 - L12)
The broadest metric, measuring accuracy on all questions where the model had sufficient information to answer correctly. This encompasses both grounding failures (wrong answers from documents that exist) and fabrication (invented information). Faithfulness aligns with the colloquial enterprise definition of “hallucination” as any confidently wrong answer when correct information was available.
3.5.2  Grounding (L01 - L04)
Accuracy on single-document questions only. Grounding failures indicate the model could not locate or correctly extract information from documents that definitively contain the answer. This isolates retrieval and comprehension errors from fabrication.
3.5.3  Fabrication (L11 - L12)
Error rate on hallucination probe questions. Because L11 questions ask about non-existent entities, any specific answer is definitively fabricated—there is no ambiguity about the failure mode. This provides the cleanest signal for measuring a model’s tendency to invent information.
3.5.4  Aggregation (L05 - L10)
Reported separately as a capability metric rather than a hallucination metric. Aggregation errors conflate multiple failure modes (incomplete document retrieval, computation errors, working memory limitations) that are distinct from hallucination in the traditional sense.
3.6  Robustness Validation
A methodology is only useful if it produces stable, reproducible results. We validated RIKER’s robustness through cross-corpus experiments.
3.6.1  Cross-Corpus Stability
Four corpora were generated from identical configuration parameters but different random seeds, producing documents with different entity names, dates, and surface content while maintaining structural equivalence. Four models spanning different performance tiers were evaluated on all four corpora.
Results demonstrated strong stability: top-performing models showed less than 2% accuracy variance across corpora (CV 
<
<
 1%), with consistent ranking preservation. This validates that RIKER results reflect model capability rather than corpus-specific artifacts.
3.6.2  Implications for Reproducibility
The cross-corpus stability finding has practical implications: researchers can generate their own RIKER corpora and expect comparable results to other studies using the same configuration parameters. This addresses a key limitation of static benchmarks: their fixed nature means they inevitably leak into training corpora, while RIKER’s regenerability ensures fresh, uncontaminated test data.
4  Experimental Design
Table 
2
 summarizes the scale of our evaluation for this RIKER study. 33 models and over 21B tokens were processed.
Table 2: 
RIKER Experimental Scale
Corpus
Questions
Runs
Models
Input Tokens
Output Tokens
Total Tokens
Main Experiment:
32K
110
8
33
0.79B
7M
0.80B
128K
301
8
24
5.67B
47M
5.72B
200K
525
8
11
9.26B
85M
9.34B
Main Subtotal
15.72B
139M
15.86B
Cross-Corpus Validation (Section 
5.9
):
128K (B,C,D)
301
8
4
3.02B
7M
3.03B
Expanded Hallucination Analysis (Section 
5.10
):
32K (HA,HB,HC,HD)
300
8
10
2.64B
9M
2.65B
Grand Total
21.38B
155M
21.54B
Token counts reflect total compute consumed across all experimental attempts, including a few runs that failed to produce scorable output due to API errors, timeouts, or malformed responses.
Table 3: 
Corpus Document Composition
Corpus
Leases
Field Reports
HR Reports
Total Docs
Main Experiment:
32K
10
44
56
110
128K (Set A)
37
216
116
369
200K
60
381
196
637
Cross-Corpus Validation:
128K (Set B)
37
255
128
420
128K (Set C)
37
228
120
385
128K (Set D)
37
211
120
368
Table 
3
 details the document breakdown across corpora; question counts scale proportionally, with approximately 50% single-document extraction, 40% cross-document aggregation, and 10% hallucination probes. All three document types appear in every corpus, demonstrating the Coherent Simulated Universe in practice: the same entities (people, properties, companies) appear across leases, field reports, and HR evaluations. The document distribution reflects realistic business ratios - leases are fewer (one per tenancy), field reports dominate (generated per agent-prospect interaction), and HR reports fall in between (periodic per employee).
Model coverage decreases with context size (33 
→
\rightarrow
 24 
→
\rightarrow
 11) as fewer models support longer contexts - this stratification is itself a finding. Eight runs per model enable statistical significance testing with variance and confidence interval reporting.
All experiments use a temperature setting of 0.4, balancing determinism with natural response variation. Future work will explore the effects of LLM temperature on performance in enterprise knowledge extraction settings.

6.6  Limitations
RIKER’s current implementation has several limitations that constrain generalizability:
Domain scope.
 Our evaluation uses enterprise documents (commercial leases, facility field reports, HR records). While chosen for realism, performance on these document types may not transfer to other domains such as scientific literature, legal contracts, or medical records.
Language.
 All documents and questions are in English. Multilingual performance remains untested.
Architecture.
 In this study, we evaluate pure context-stuffing - the entire corpus is provided in the prompt. Future work will test retrieval-augmented generation and agentic retrieval patterns.
Synthetic realism.
 While our Coherent Simulated Universe approach maintains entity consistency across documents, synthetic documents may lack certain characteristics of real-world data: OCR errors, inconsistent formatting, contradictory information across sources, or domain-specific jargon. Models may perform differently on messier real-world corpora. These characteristics can be modeled into RIKER’s (or any RIKER-like system’s) synthetic data generation logic, but in this current work and results, such characteristics are not included.
Model coverage.
 Our evaluation covers 33 models available at the time of testing. The rapidly evolving LLM landscape means new models may exhibit different patterns.
