# 2601.08838v1 — primary PDF necessary raw cache

URL: https://arxiv.org/pdf/2601.08838v1
Fetched: 2026-10-03; original page/line markers; only method/evaluation/critical tables, not runtime reproduction.

L85@P2: models [16,17]. However, generalization remained limited by model capacity and training data.
L86@P2: Recently, large language models (LLMs) such as GPT-4 [18], Gemini [19], and open-source
L87@P2: models such as LLaMA [20] and DeepSeek [21] have driven a new wave of Text-to-SQL
L88@P2: research. Prompting-based approaches include C3 [22], DIN-SQL [23], MCS-SQL [24] with
L89@P2: self-consistency [25], data synthesis and model scaling efforts such as SENSE [26] and CodeS
L90@P2: [9], and self-refinement strategies such as E-SQL [27] and Self-Polish [28]. Fine-tuning and
L91@P2: ensemble selection frameworks (e.g., XiYan-SQL [29], CHASE-SQL [30], MSc-SQL [31]) and
L92@P2: verification-based systems such as CHESS [7] further improve robustness.
L93@P2: 2.2 Datasets and the role of evidence
L94@P2: NL2SQL datasets evolved from single-domain corpora (e.g., ATIS [32], GeoQuery [33]) to
L95@P2: larger and more complex settings, including domain-specific benchmarks [34–36]. Crossdomain datasets such as WikiSQL [37] and Spider [3] emphasize generalization. BIRD [4]
L96@P2: introduces noisy, large-scale databases closer to industrial environments, and categorizes
L97@P2: evidence into four types: (i) numeric reasoning knowledge, (ii) domain knowledge, (iii)
L98@P2: synonym knowledge, and (iv) value illustration. Importantly, much of this “external knowledge”
L99@P2: can be derived from careful analysis of schema, metadata, and data samples—an observation
L100@P2-3: that motivates CA’s database-side mining.3. Method
L101@P3: 3.1 Problem definition
L102@P3: Let a database instance be 𝐷 with schema 𝑆 (tables, columns, and foreign-key constraints),
L103@P3: an NL question be 𝑞, and human-provided evidence be 𝑒. The goal of Text-to-SQL is to
L104@P3: generate an SQL query y whose execution result matches the ground truth.
L105@P3: For an LLM-based approach without parameter fine-tuning, SQL generation can be abstracted
L106@P3: as:
L107@P3: 𝑦% = 𝑓!(𝑃(𝑞, 𝑆, 𝑒))
L108@P3: where 𝑓! is the LLM, 𝑃 (⋅) is a prompt construction function, and e provides additional
L109@P3: knowledge related to the question and database. In the evidence-missing scenario (𝑒=∅), we
L110@P3: propose to construct substitute evidence 𝑒̅ using Companion Agents:
L111@P3: 𝑒̅= 𝑔∅(𝐷, 𝑆, 𝑞), 𝑦% = 𝑓!(𝑃(𝑞, 𝑆, 𝑒̅))
L112@P3: Our objective is to maximize execution accuracy (EX) and logical consistency under evidencemissing conditions.
L113@P3: 3.2 Companion Agents (CA)
L114@P3: The CA framework targets scenarios where schema annotations are missing or incomplete. It
L115@P3: proactively mines and generates query-relevant contextual evidence to support robust LLMbased SQL synthesis. CA consists of three core modules (Figure 2):
L116@P3: • Schema Mining Agent (SMA): deep schema mining and database profiling;
L117@P3: • Query Routing Agent (QRA): query-type recognition and evidence-type routing;
L118@P3: • Evidence Generation Agent (EGA): evidence construction, retrieval, and semantic
L119@P3: strengthening.
L120@P3-4: Figure 2. Overview of the Companion Agents framework.3.2.1 Schema Mining Agent: deep structural mining
L121@P4: Based on BIRD’s evidence taxonomy, we observe that beyond numeric reasoning formulas, the
L122@P4: remaining evidence types—domain knowledge, synonym knowledge, and value illustration—
L123@P4: can often be derived from structured schema metadata and sampled data values. SMA is
L124@P4: designed to automatically extract such signals and store them as reusable schema-knowledge.
L125@P4: It contains three stages:
L126@P4: (1) Schema Extraction.
L127@P4: SMA performs automatic structural parsing, statistical profiling, and constrained semantic
L128@P4: induction for each database. It first extracts table- and column-level information via database
L129@P4: interfaces, including simplified DDL statements, foreign-key constraints, and sampled rows,
L130@P4: forming a base structural description. It then computes column-level profiles from samples,
L131@P4: including typical values, distribution ranges, and high-frequency enumerations to build
L132@P4: reproducible field portraits. Finally, SMA invokes an LLM over (column name + structural
L133@P4: context + profile statistics + sampled values) to produce semantic summaries and tags,
L134@P4: generating: (i) field semantic descriptions, (ii) candidate aliases/synonym mappings, (iii) time
L135@P4: granularity/unit hints, and (iv) readable glossaries for frequent enumerated values. All outputs
L136@P4: are encoded into a structured schema-knowledge file for downstream routing and evidence
L137@P4: construction.
L138@P4: (2) Few-shot Knowledge Library Building.
L139@P4: To enhance reasoning under knowledge scarcity, SMA builds a few-shot QA library and uses
L140@P4: an LLM to standardize examples and abstract their structure. Specifically, it extracts (question,
L141@P4: SQL) pairs from training data, then asks the LLM to denoise and normalize questions (e.g.,
L142@P4: resolve references, remove ambiguity) and to skeletonize SQL (e.g., abstract SELECT–FROM–
L143@P4: WHERE–GROUP–ORDER templates and operator chains). This produces transferable entries
L144@P4: of “semantic question template + SQL logical skeleton”. After rule-based deduplication and
L145@P4: schema-compatibility checks, SMA yields a clean, reusable QA library that provides experience
L146@P4: priors when explicit evidence is missing.
L147@P4: (3) Similar-case matching.
L148@P4: Given a new Text-to-SQL query, SMA retrieves the top-k most semantically similar examples
L149@P4: from the QA library and concatenates them into a structured few-shot prompt. This enables the
L150@P4: LLM to borrow solutions from analogous problems, improving stability on complex reasoning
L151@P4: and cross-table join queries.
L152@P4: 3.2.2 Query Routing Agent: semantic guidance and query typing
L153@P4: Given question q and schema-knowledge, QRA performs multi-label routing (via an LLM) to
L154@P4: determine which evidence types are required, including: numeric reasoning, domain knowledge,
L155@P4: synonym/alias, and enum/value illustration.
L156@P4: • Numeric reasoning: QRA selects candidate numeric columns and uses column
L157@P4: profiles (mean/variance/range/quantiles) to build computation-oriented explanation
L158@P4: templates that clarify the required fields and reasoning chain.
L159@P4: • Domain knowledge: QRA identifies relevant fields using schema-knowledge and
L160@P4: schema-linking signals; if database-side signals are insufficient, it can trigger
L161@P4: controlled web retrieval as a fallback to supply necessary domain rules.
L162@P4: • Synonym/alias: QRA uses SMA-produced alias sets and mapping tables to
L163@P4-5: rewrite/expand the query (synonym substitution, coreference resolution, phrase alignment) to improve column alignment.
L164@P5: • Enumerations: QRA extracts value domains and typical samples for discrete fields
L165@P5: (e.g., gender, region, category), reducing constraint mismatches and empty-result risks;
L166@P5: if enum evidence is needed, QRA provides enum dictionaries to EGA.
L167@P5: 3.2.3 Evidence Generation Agent: evidence construction and semantic enhancement
L168@P5: EGA generates or retrieves contextual evidence based on QRA’s routing. It includes three
L169@P5: evidence strategies:
L170@P5: (1) Schema-consistency evidence.
L171@P5: By comparing foreign-key constraints and semantic similarity, EGA proposes plausible join
L172@P5: relations and connection paths.
L173@P5: Example evidence: “Table customer is linked to order via customer_id, enabling aggregation
L174@P5: of order records per customer.”
L175@P5: (2) Semantic constraint evidence.
L176@P5: EGA generates natural-language constraints for time/range/category conditions.
L177@P5: Example: “Column year denotes the sales year; records with year > 2020 correspond to 2021
L178@P5: and later.”
L179@P5: (3) Logical completion evidence.
L180@P5: EGA retrieves similar cases from the few-shot library to complete multi-step logic.
L181@P5: Example: “Compute total sales per employee via a subquery, then apply a window function
L182@P5: RANK() for group-wise ranking and top-10% filtering.”
L183@P5: Finally, EGA embeds these evidence items into the model prompt, forming a closed-loop
L184@P5: enhancement pipeline from structure mining and semantic routing to evidence construction.
L185@P5: 4. Experiments
L186@P5: 4.1 Datasets
L187@P5: We evaluate on BIRD, which bridges academic and industrial scenarios by introducing largescale noisy databases. BIRD contains 12,751 NL–SQL pairs spanning 95 databases (33.4 GB)
L188@P5: and 37 domains. Queries are categorized into Simple (~60%), Moderate (~30%), and
L189@P5: Challenging (~10%), reflecting increasing difficulty.
L190@P5: 4.2 Evaluation metrics
L191@P5: We use the official BIRD execution evaluation script to compute Execution Accuracy (EX): a
L192@P5: prediction is correct if the execution result of the generated SQL exactly matches that of the
L193@P5: gold SQL. We report overall EX and EX stratified by difficulty (Simple/Moderate/Challenging).
L194@P5: 4.3 Baselines
L195@P5: We select representative SOTA baselines with public implementations:
L196@P5: • RSL-SQL [5]: robust schema linking + structured prompting.
L197@P5: • CHESS [7]: multi-agent candidate generation + unit-test verification.
L198@P5: • DAIL-SQL [38]: evidence-heavy prompt engineering / in-context learning.
L199@P5: To isolate method effects, both baselines and CA-augmented versions use the same LLM
L200@P5-6: (qwen-plus) for inference.4.4 Implementation details
L201@P6: All methods share the same inference configuration: temperature = 0.2, top-p = 0.9, max_tokens
L202@P6: = 1024. For schema extraction, we sample n=200 rows per column (prioritizing distinct values)
L203@P6: to build column profiles. Few-shot retrieval uses top-k=5. QRA adopts zero-shot multi-label
L204@P6: routing with confidence threshold τ=0.5 to filter irrelevant evidence types. Reported EX values
L205@P6: are averaged.
L206@P6: 4.5 Results
L207@P6: Table 1 summarizes performance under the fully missing evidence setting. Removing human
L208@P6: evidence causes substantial degradation for all baselines, especially on Challenging queries,
L209@P6: confirming heavy reliance on external annotations. With CA, overall EX improves by 4.49%,
L210@P6: 4.37%, and 14.13% on RSL-SQL/CHESS/DAIL-SQL, respectively; on the Challenging subset,
L211@P6: gains further increase to 9.65%, 7.58%, and 16.71%. This indicates that CA can effectively
L212@P6: mine internal database knowledge and construct substitute evidence, narrowing the gap
L213@P6: between “with evidence” and “without evidence”.
L214@P6: DAIL-SQL benefits the most because its ICL-style prompting depends most heavily on
L215@P6: evidence, whereas RSL-SQL and CHESS already have internal priors (schema linking and unit
L216@P6: tests), resulting in milder degradation and smaller but consistent recovery.
L217@P6: Table 1. Execution accuracy without BIRD evidence and recovery with Companion Agents.
L218@P6: Simple Moderate Challenging Total
L219@P6: RSL-SQL-w/o evi 61.41 40.09 29.66 51.96
L220@P6: RSL-SQL-evi 71.68 55.60 48.97 64.67
L221@P6: RSL-SQL-CA 65.19(↑3.78) 44.40(↑4.31) 39.31(↑9.65) 56.45(↑4.49)
L222@P6: Chess-w/o evi 56.00 37.93 26.90 47.78
L223@P6: Chess-evi 67.38 56.82 47.06 62.14
L224@P6: Chess-CA 59.46(↑3.46) 43.10(↑5.17) 34.48(↑7.58) 52.15(↑4.37)
L225@P6: DAIL-SQL-w/o evi 38.76 27.39 17.77 39.52
L226@P6: DAIL-SQL-evi 63.78 51.72 40.00 57.89
L227@P6: DAIL-SQL-CA 62.16(↑23.4) 42.67(↑15.28) 34.48(↑16.71) 53.65(↑14.13)
L228@P6: 4.6 Ablation study
L229@P6: To quantify each module’s contribution, we perform ablations (under the DAIL-SQL baseline)
L230@P6: with four variants:
L231@P6: • A) Baseline (w/o evidence)
L232@P6: • B) SMA Only: schema-knowledge only (no routing)
L233@P6: • C) QRA Only: routing only (without substantive knowledge content)
L234@P6: • D) Full CA (SMA + QRA + EGA)
L235@P6: As shown in Table 2, SMA Only provides substantial gains on Simple and Moderate, suggesting
L236@P6: that structural/value-domain profiling already compensates for many missing semantics. QRA
L237@P6: Only yields limited improvements, indicating that “routing without content” is insufficient. Full
L238@P6: CA performs best across all difficulty levels, with the largest gain on Challenging (+16.71),
L239@P6: showing that the closed-loop design—knowledge consolidation + on-demand activation +
L240@P6-7: evidence construction—is key to CA’s effectiveness.Table 2. Ablation results on DAIL-SQL.
L241@P7:  Simple Moderate Challenging Total
L242@P7: w/o evidence 38.76 27.39 17.77 39.52
L243@P7: SMA only 55.83 36.47 27.96 48.95
L244@P7: QRA only 42.14 29.82 19.61 41.39
L245@P7: SMA + QRA(CA) 62.16 42.67 34.48 53.65
L246@P7: 5. Discussion
L247@P7: Our experiments demonstrate that Companion Agents (CA) consistently and significantly
L248@P7: improve execution accuracy for three distinct paradigms of Text-to-SQL baselines under
L249@P7: evidence-missing conditions, with larger recovery on Challenging queries. This supports the
L250@P7: central claim that replacing the conventional “human evidence–dependent” enhancement
L251@P7: pathway with a closed-loop mechanism—database-side knowledge consolidation → ondemand routing → evidence generation—is both effective and broadly applicable.
L252@P7: To better understand CA’s boundary of effectiveness, we manually analyze dev-set failures
L253@P7: where CA-augmented systems still produce incorrect SQL. As summarized in Table 3 (from
L254@P7: your manuscript), we observe two stable error modes:
L255@P7: 1. Missing enum instantiation. CA sometimes identifies that a query requires filtering
L256@P7: on a categorical/code field, but fails to provide executable value mappings that appear
L257@P7: in gold evidence (e.g., mapping “Unified School District” / “Elementary School
L258@P7: District” to DOC=54 / DOC=52). Without concrete mappings, EGA cannot instantiate
L259@P7: WHERE predicates, leading to missing or incorrect constraints and potentially empty
L260@P7: results.
L261@P7: 2. Focus drift from structural rules. CA may over-attend to secondary semantics and
L262@P7: omit structural requirements encoded in gold evidence, such as composing a “full
L263@P7: communication address” by selecting Street, City, State, and Zip. Such omissions often
L264@P7: manifest as incomplete SELECT fields or mismatched aggregation scope.
L265@P7: These patterns suggest that CA’s remaining bottlenecks are not merely whether relevant
L266@P7: columns can be found, but whether evidence can be (i) concretized into executable
L267@P7: enum/value mappings and (ii) aligned with structural completeness constraints. In
L268@P7: industrial settings with highly discrete enumerations and rich profiles, CA may be further
L269@P7: strengthened by integrating an external enum knowledge base for long-tail mappings, and by
L270@P7: adding structure-aware coverage checks to ensure that evidence explicitly enumerates required
L271@P7: field compositions.
L272@P7: Table 3. Typical failure modes under CA.
L273@P7: Error Mode Case ID NL Query Gold Evidence Error Analysis
L274@P7: Incomplete
L275@P7: enumeration
L276@P7: mapping
L277@P7: #49
L278@P7: Compute ratio of Unified
L279@P7: School District vs
L280@P7: Elementary School District
L281@P7: schools in Orange County
L282@P7: Elementary SD =
L283@P7: DOC 52; Unified SD
L284@P7: = DOC 54
L285@P7: States “count and
L286@P7: compute ratio”
L287@P7: without giving
L288@P7: executable

