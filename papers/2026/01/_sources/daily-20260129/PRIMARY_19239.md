# 2601.19239v1 — necessary primary excerpts

Source: https://arxiv.org/html/2601.19239v1

L133: ### III-B Evaluated Methods
L134: 
L135: TABLE I: Studied vulnerability detection methods in this paper
L136: Category  | Method  | LLM Backbone  | Languages  | Evaluated CWE Type  | Workflow  | Src&Sink Source
L137: LLM-based  | RepoAudit [cite59†21 ]  | cite94†Image: [Uncaptioned image] Claude 3.5 Sonnet  | C/C++  | CWE-401, CWE-416, CWE-476  | Multi-Agent  | Manual
L138: Knighter [cite61†23 ]  | cite95†Image: [Uncaptioned image] O3-mini  | C/C++  | CWE-401, CWE-416, CWE-476  | LLM+CSA [cite96†55 ]  | LLM-inferred
L139: IRIS [cite50†12 ]  | cite95†Image: [Uncaptioned image] GPT-4  | Java  | CWE-022, CWE-078, CWE-079, CWE-094  | LLM+CodeQL  | LLM-inferred
L140: LLMDFA [cite60†22 ]  | cite95†Image: [Uncaptioned image] GPT-4  | Java  | CWE-078, CWE-079  | Multi-Agent  | LLM-inferred
L141: INFERROI [cite63†25 ]  | cite95†Image: [Uncaptioned image] GPT-4  | Java  | CWE-772  | LLM+CFG  | LLM-inferred
L142: Traditional  | CodeQL [cite43†5 ]  | -  | C/C++, Java  | All above  | Query-driven  | Built-in
L143: Semgrep [cite44†6 ]  | -  | C/C++, Java  | All above  | Pattern-driven  | Built-in
L144: As shown in Table cite97†I , we selected five latest and representative LLM-based methods and two traditional static analysis methods that (i) are publicly available, (ii) cover a diverse range of workflows, and (iii) can be readily applied across different projects and programming languages. This selection enables us to assess the effectiveness of LLM-based approaches as well as their advantages, limitations, and potential complementarity with existing traditional tools in real-world scenarios.
L145: These methods are selected to represent a diverse range of detection workflows, LLM backbones, supported programming languages, and targeted CWE types^{1}^{1} 1 CWE categories and definitions referenced in this paper are based on the official MITRE classification at cite98†https://cwe.mitre.org/†cwe.mitre.org .. In the following, we briefly introduce each of them.
L146: #### III-B 1 LLM-based Methods
L147: 
L148:   * •
L149: 
L150: RepoAudit [cite59†21 ] A multi-agent framework initiates scanning from predefined source points and systematically explores program paths by identifying critical callee or caller functions with the assistance of LLMs. When a path reaches a predefined sink point, it reports a potential vulnerability. The reported paths are then subsequently validated by LLMs to reduce false positives and improve the overall performance.
L151: 
L152:   * •
L153: KNighter [cite61†23 ] An LLM-based checker generation framework that automatically generates Clang Static Analyzer (CSA) [cite96†55 ] checkers from a vulnerability fixing commit. The generation process includes few-shot prompting, iterative regeneration with syntax validation and repair, and refinement steps to ensure high detection precision. Since KNighter relies on the CSA, it can detect multiple types of vulnerabilities in C/C++.
L154: 
L155:   * •
L156: IRIS [cite50†12 ] IRIS utilizes LLMs to automatically identify and label all methods and their corresponding parameters within a project as potential sources or sinks. This information is then embedded into predefined CodeQL query templates to detect possible vulnerabilities. The paths flagged as potentially vulnerable by these queries are then re-evaluated by LLMs to reduce false positives.
L157: 
L158:   * •
L159: LLMDFA [cite60†22 ] An agent-centric method initiates scanning from source program points defined by the LLM. Unlike RepoAudit, which will explore program paths on demand, LLMDFA will explore all possible paths. When a path reaches a sink point defined by the LLM, it reports a potential vulnerability path. These paths are further validated for reachability by using LLMs or the Z3 solver [cite99†56 ].
L160: 
L161:   * •
L162: INFERROI [cite63†25 ] This method is specifically designed to detect resource leak vulnerability (CWE-772). It first employs LLMs to infer the intent of program statements (resource acquisition, release, or check). Then it explores program paths based on the control flow graph (CFG). If a path exists where a resource is acquired but never released, it is reported as a potential vulnerability.
L163: #### III-B 2 Traditional Static Methods
L164: 
L165:   * •
L166: CodeQL [cite43†5 ] A semantic, query-based static analysis framework widely used in industry for vulnerability detection. It models source code as a relational dataset and uses logic-style queries to identify relevant patterns across control-flow and data-flow paths. It supports multiple programming languages, including C/C++ and Java, and provides a rich collection of built-in security queries covering a broad range of CWEs.
L167: In this study, we apply CodeQL to C/C++ and Java vulnerability types supported by the evaluated LLM-based vulnerability detectors, enabling a consistent and comparable assessment across all methods.
L168:   * •
L169: 
L170: Semgrep [cite44†6 ] A lightweight, pattern-based static analysis tool that identifies vulnerabilities using rule-based matching over Abstract Syntax Trees (ASTs). It also supports many programming languages, including C/C++ and Java, and offers an extensive rule ecosystem maintained by the community and security researchers. Similarly, we apply Semgrep to C/C++ and Java vulnerabilities that are supported by both the LLM-based tools and the available Semgrep rule set.
L171: ### III-C Datasets
L172: 
L173: TABLE II: Overview of the in-house dataset used in this paper
L174: 
L175: Language  | CWE Type  | Amount  | Source
L176:  | CWE-401  | 40  | ReposVul [cite92†53 ]
L177: C/C++  | CWE-416  | 10
L178:  | CWE-476  | 14
L179:  | CWE-022  | 51  | CWE-Bench-Java [cite50†12 ]
L180:  | CWE-078  | 13
L181: JAVA  | CWE-079  | 29
L182:  | CWE-094  | 15
L183:  | CWE-772  | 50  | JLeaks [cite93†54 ]
L184: 
L185: TABLE III: Evaluated real-world projects used in this study
L186: CWE  | Repository Name  | Commit  | Size (LOC)  | Stars
L187:  | linux/sound  | 6093a68  | 1,253,234  | 207K
L188: CWE-401  | linux/mm  | 6093a68  | 133,952  | 207K
L189:  | ImageMagic  | 3bf1076  | 680,878  | 14.9K
L190:  | linux/net  | 6093a68  | 962,143  | 207K
L191: CWE-416  | linux/drivers/net  | 6093a68  | 3,924,621  | 207K
L192:  | vim  | 8feaa94  | 1,192,925  | 39.3K
L193:  | linux/drivers/peci  | 6093a68  | 1,715  | 207K
L194: CWE-476  | gpac  | c6a72c3  | 859,528  | 3.1K
L195:  | bitlbee  | 8af06ca  | 33,650  | 632
L196:  | OpenOLAT  | df53b85  | 1,907,083  | 394
L197: CWE-022  | spark  | 1973e40  | 11,941  | 9.7K
L198:  | Dspace  | 3b24801  | 448,030  | 1K
L199:  | xstream  | a22d3af  | 76,339  | 752
L200: CWE-078  | workflow-cps-plugin  | e4b9517  | 238,588  | 179
L201:  | tika  | 2b38ed1  | 228,309  | 3.4K
L202:  | xwiki-platform  | fc73498  | 5,553,098  | 1.2K
L203: CWE-079  | jenkins  | 69d5a54  | 300,491  | 24.7K
L204:  | keycloak  | 4f55b9b6  | 6,033,855  | 31K
L205:  | onedev  | b8a4d7cd  | 552,486  | 14.5K
L206: CWE-094  | activemq  | 56ea235e  | 611,964  | 2.4K
L207:  | cron-utils  | bac6e866  | 16,244  | 1.2K
L208:  | sql2o  | 744b85b3  | 8,027  | 1.2K
L209: CWE-722  | RxJava  | f07765ed  | 325,394  | 48.4K
L210:  | jsoup  | acafbcf3  | 38,128  | 11.3K
L211: As illustrated in our research questions, we evaluate the selected methods in two scenarios: an in-house dataset containing projects that are verified to contain known vulnerabilities, and a real-world dataset composed of the latest open-source projects. Since different methods support diverse CWE types, we choose a subset of CWE-categories (as shown in Table cite97†I ) covered most of them, to enable a fair comparison and meaningful analysis across methods.
L212: This choice is also practical in real-world settings, where extending these LLM-based tools (many of which target only a limited set of CWEs) to new CWE types often requires substantial engineering effort (e.g., redesigning rules, prompts, or analysis pipelines), rather than being a simple configuration change. The details of the studied datasets are presented in Table cite100†II and Table cite101†III .
L213:   * •
L214: In-house dataset: We construct an in-house dataset by consolidating vulnerabilities from three peer-reviewed benchmarks, providing a controlled setting to assess the detection effectiveness of the evaluated methods: ReposVul [cite92†53 ], CWE-Bench-Java [cite50†12 ], and JLeaks [cite93†54 ]. ReposVul is an automatically curated dataset built using LLMs and static analysis tools, containing 6,134 CVE entries covering 236 CWE types across 1,491 open-source projects.
L215: For the C/C++ portion of ReposVul, we retain only cases from the Linux kernel after 2019 to ensure recency and buildability. CWE-Bench-Java provides manually curated Java vulnerabilities from real-world projects. From this benchmark, we select vulnerable cases from Maven projects to guarantee successful building and analysis. JLeaks is a high-quality benchmark focusing on Java resource leak vulnerabilities and has been manually validated. From JLeaks, we randomly sample 50 representative cases.
L216: All selected cases from these three sources are further manually checked to ensure correctness, validity, and successful compilation.
L217:   * •
L218: Real-world projects: To complement the in-house dataset and avoid data leakage, we construct a real-world dataset by selecting actively maintained open-source projects that have historically exhibited vulnerabilities of the studied CWE types. As summarized in Table cite101†III , these projects span both C/C++ and Java and cover diverse domains such as operating systems, multimedia processing, networking, data platforms, and web frameworks.
L219: For C/C++ projects, we select the latest versions of widely used software (e.g., the Linux kernel, ImageMagick, Vim) that historically contain vulnerabilities of the corresponding CWE types [cite92†53 ], ensuring that the chosen commits are recent and the projects remain actively maintained.
L220: Similarly, for Java projects, we select the latest versions of well-maintained projects (e.g., XStream, Jenkins, Keycloak) that historically contain vulnerabilities of the studied CWE types [cite50†12 ], and ensure that each project can be successfully built and analyzed. This dataset provides a realistic and diverse foundation for evaluating the scalability and practical effectiveness of the evaluated methods.
L221: ### III-D Evaluation Metrics
L222: 
L223: To evaluate the effectiveness of the evaluated methods, we adopt several standard detection metrics by following existing studies [cite65†27 , cite64†26 , cite66†28 , cite67†29 , cite68†30 , cite69†31 , cite70†32 , cite71†33 , cite72†34 ], and additionally consider tool costs in terms of token usage and time overhead.
L224: In-house dataset. For the curated in-house dataset, each vulnerable project is labeled with the actual vulnerable program point(s). Consequently, we consider a vulnerability successfully detected by a tool as long as it reports the associated vulnerable point(s) (a.k.a, true positive: TP), otherwise, the vulnerability is missed by the tool (a.k.a, false negative: FN).
L225: In particular, since the non-vulnerable code space in the projects is huge and not fully labeled, we focus on recall rather than full precision on this dataset:
L226:  | $$\mathrm{Recall}=\frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FN}}\times 100\%.$$  |
L227: Real-world projects. For these real-world open-source projects, it is unknown whether there are vulnerabilities in them. For each tool and project, we therefore report: 1) #Reports, the total number of warnings produced, 2) #Files, the number of distinct source files that contain at least one warning, and 3) #Sampled FPs, the number of FPs (benign instances incorrectly reported as vulnerabilities by the tools) among the sampled warnings.
L228: Since manually validating a warning is time-consuming and labor-intensive, it often requires inspecting project-specific APIs, transitive dependencies, and relevant control and data flows across the entire project. Therefore, two authors sampled up to 10 warnings per tool per project and independently labeled each as a true positive or false positive, resolving disagreements through discussion.
L229: In total, we manually examined 385 sampled warnings across all tools and projects, which required more than 150 human hours. Based on these labels, we estimate the Sampled False Discovery Rate (SFDR) as
L230:  | $$\mathrm{SFDR}=\frac{\mathrm{\#Sampled\;FPs}}{\mathrm{\#Sampled\;Reports}}$$  |
L231: 
L232: Token usage and time overhead. For RQ4, we quantify the computational overhead of LLM-based methods by measuring the input and output token consumption of each tool, as well as the end-to-end detection time per project (Section cite23†V-D ).
L233: ## IV Experimental Setup
L234: For LLM-based vulnerability detection methods, we directly use their released replication packages and follow the backbone models and hyperparameters (e.g. function call-chain exploration depth, temperature, and top-p) recommended in the original papers. All experiments are conducted via the official OpenAI and Anthropic Claude APIs [cite102†57 , cite103†58 , cite104†59 ].
L235: For tools that require manually specified sources and sinks (e.g., RepoAudit), we explicitly configure all source–sink pairs for the in-house dataset, and rely on the tool’s default source–sink configuration when analyzing the real-world projects. For tools whose sources and sinks are inferred by LLMs, we directly adopt the definitions generated by the models.
L236: For traditional static vulnerability detection methods, we manually curate the predefined rule set by selecting only those rules that are relevant to the target CWE types evaluated in this study.
L237: Specifically, for CodeQL, we finally selected 48 predefined rules that are relevant to our target CWE types from the official CodeQL rule set, such as CWE-401/MemoryLeakOnFailedCallToRealloc.ql and Critical/MemoryMayNotBeFreed.ql for CWE-401, for Semgrep, we finally selected 59 predefined rules that are relevant to our target CWE types from the official rule sets (e.g., the official XSS rules for CWE-079).
L238: More details about the selected CodeQL and Semgrep rules are available in our Appendix B and on our homepage [cite105†60 ]. Although different rules may produce reports with varying severity levels (e.g., some are marked as errors and others as recommendations), we treat all reports equally in this study.
L239: All experiments are conducted on a local server equipped with dual Intel Xeon 6388 CPUs, 512 GB of RAM, and four NVIDIA A800 GPUs, running Ubuntu 20.04.6 LTS. All LLM API requests, as well as CodeQL and Semgrep analyses, are executed on this server in our experiments.
L240: ## V Result Analysis
L241: 
L242: TABLE IV: Effectiveness of evaluated tools on the in-house dataset. In this table, #Detected is shown as X/Y, where X denotes the number of true positives and Y the total number of vulnerabilities.
L243: CWE  | Method  | #Detected  | Recall (%)  | CWE  | Method  | #Detected  | Recall (%)
L244: CWE-401 (C/C++)  | RepoAudit  | 22/40  | 55.00  | CWE-022 (Java)  | IRIS  | 19/51  | 37.25
L245: KNighter  | 0  | 0.00
L246: CodeQL  | 0  | 0.00  | CodeQL  | 16/51  | 31.37
L247: Semgrep  | 0  | 0.00  | Semgrep  | 6/51  | 11.76
L248: CWE-416 (C/C++)  | RepoAudit  | 1/10  | 10.00  | CWE-078 (Java)  | IRIS  | 6/13  | 46.15
L249: KNighter  | 0  | 0.00  | LLMDFA  | 0  | 0.00
L250: CodeQL  | 0  | 0.00  | CodeQL  | 0  | 0.00
L251: Semgrep  | 0  | 0.00  | Semgrep  | 1/13  | 7.69
L252: CWE-476 (C/C++)  | RepoAudit  | 4/14  | 28.57  | CWE-079 (Java)  | IRIS  | 7/31  | 22.58
L253: KNighter  | 0  | 0.00  | LLMDFA  | 0  | 0.00
L254: CodeQL  | 0  | 0.00  | CodeQL  | 1/29  | 3.44
L255: Semgrep  | 0  | 0.00  | Semgrep  | 0  | 0.00
L256: CWE-772 (Java)  | INFERROI  | 31/50  | 62.00  | CWE-094 (Java)  | IRIS  | 6/15  | 40.00
L257: CodeQL  | 0  | 0.00
L258: CodeQL  | 5/50  | 10.00  | Semgrep  | 0  | 0.00
L303: CWE  | Project  | IRIS  | LLMDFA  | CodeQL  | Semgrep  | INFERROI
L304: #R(#F)  | #FPs  | SFDR  | #R(#F)  | #FPs  | SFDR  | #R(#F)  | #FPs  | SFDR  | #R(#F)  | #FPs  | SFDR  | #R(#F)  | #FPs  | SFDR
L307:  | Dspace  | 552(160)  | 9/10  | 90.0%  | -  | -  | -  | 2(2)  | 2/2  | 100.0%  | 107(46)  | 10/10  | 100.0%  | -  | -  | -
L308: Average of CWE-022  | 423(125)  | 8.3/9  | 92.6%  | -  | -  | -  | 24(7)  | 5.7/5.7  | 100.0%  | 99(46)  | 8.3/8.3  | 100.0%  | -  | -  | -
L309:  | xstream  | 17(11)  | 10/10  | 100.0%  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | -  | -  | -
L310: CWE-078  | workflow-cps-plugin  | 5(5)  | 5/5  | 100.0%  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | -  | -  | -
L311:  | tika  | 71(42)  | 10/10  | 100.0%  | 4(3)  | 4/4  | 100.0%  | 13(5)  | 10/10  | 100.0%  | 32(17)  | 10/10  | 100.0%  | -  | -  | -
L312: Average of CWE-078  | 31(20)  | 8.3/8.3  | 100.0%  | 2(1)  | 1.3/1.3  | 100.0%  | 5(2)  | 3.3/3.3  | 100.0%  | 11(6)  | 3.3/3.3  | 100.0%  | -  | -  | -
L313:  | xwiki-platform  | 458(197)  | 10/10  | 100.0%  | 5(2)  | 5/5  | 100.0%  | 1(1)  | 1/1  | 100.0%  | 1(1)  | 1/1  | 100.0%  | -  | -  | -
L314: CWE-079  | jenkins  | 208(100)  | 8/10  | 80.0%  | 4(3)  | 3/4  | 75.0%  | 0  | 0  | 0  | 1(1)  | 1/1  | 100.0%  | -  | -  | -
L315:  | keycloak  | 358(177)  | 9/10  | 90.0%  | 2(1)  | 2/2  | 100.0%  | 6(3)  | 4/6  | 66.7%  | 0  | 0  | 0  | -  | -  | -
L316: Average of CWE-079  | 342(158)  | 9.0/10.0  | 90.0%  | 4(2)  | 3.3/3.7  | 90.9%  | 3(2)  | 1.7/2.3  | 71.4%  | 1(1)  | 0.7/0.7  | 100.0%  | -  | -  | -
L317:  | onedev  | 128(27)  | 10/10  | 100.0%  | -  | -  | -  | 24(18)  | 10/10  | 100.0%  | 0  | 0  | 0  | -  | -  | -
L318: CWE-094  | activemq  | 271(91)  | 9/10  | 90.0%  | -  | -  | -  | 0  | 0  | 0  | 0  | 0  | 0  | -  | -  | -
L319:  | cron-utils  | 5(4)  | 5/5  | 100.0%  | -  | -  | -  | 0  | 0  | 0  | 0  | 0  | 0  | -  | -  | -
L320: Average of CWE-094  | 135(41)  | 8.0/8.3  | 96.0%  | -  | -  | -  | 8(6)  | 3.3/3.3  | 100.0%  | 0  | 0  | 0  | -  | -  | -
L321:  | sql2o  | -  | -  | -  | -  | -  | -  | 0  | 0  | 0  | -  | -  | -  | 23(10)  | 9/10  | 90.0%
L322: CWE-722  | RxJava  | -  | -  | -  | -  | -  | -  | 0  | 0  | 0  | -  | -  | -  | 360(228)  | 9/10  | 90.0%
L323:  | jsoup  | -  | -  | -  | -  | -  | -  | 9(5)  | 6/9  | 66.7%  | -  | -  | -  | 66(19)  | 10/10  | 100.0%
L324: Average of CWE-772  | -  | -  | -  | -  | -  | -  | 3(2)  | 2.0/3.0  | 66.7%  | -  | -  | -  | 150(86)  | 9.3/10  | 93.3%
L325: Average  | 233(86)  | 8.4/8.9  | 94.4%  | 3(2)  | 2.3/2.5  | 93.3%  | 9(5)  | 3.2/3.5  | 94.3%  | 28(13)  | 3.1/3.1  | 100.0%  | 150(86)  | 9.7/10  | 96.7%
L326: ### V-C RQ3: Causes of False Positives
L327: 
L328: Fig. 4: Taxonomy of FP reasons that are related to the cases detected by the selected methods.
L329: As described in Section cite17†III-D , two authors with a background in security and software engineering manually analyzed the sampled false positives. We applied an inductive open-coding procedure with double coding [cite113†61 ]. Each author first reviewed all examples to derive a coherent taxonomy of FP causes and iteratively refined the codebook. After consolidating and resolving disagreements on category definitions, the experts independently assigned the primary FP reason for each case.
L330: Finally, they reconciled disagreements and consolidated the labels into a unified annotation set.
L331: cite114†Image: Refer to caption Fig. 5: Distribution of false positive reasons introduced by evaluated methods.
L332: In the following, we analyze several representative reasons from this taxonomy. The taxonomy and the definition of each reason are summarized in Figure cite115†4 and Figure cite116†5 . Since we evaluate RepoAudit using its default source–sink definitions for simulating real-world deployment scenario rather than providing them manually like the in-house evaluation, the count for Reason B1 is non-zero.
L333: Due to page limits, we present two representative illustrative examples here, and include more detailed examples for the remaining FP reasons in Appendix A. As shown in the figures, LLM-based and traditional methods share two major sources of false positives: (1) Shallow Interprocedural Reasoning (A1). To limit analysis complexity, most tools rely either on source–sink style reasoning or on fixed-depth call-graph exploration.
L334: For example, RepoAudit explores three layers of function calls from each specified source by default, and traditional static analyzers such as CodeQL are configured with explicit source and sink definitions and track data flows only along the extracted source–sink paths.
L335: However, in real-world projects, where data may originate from diverse entry points and propagate through rich, multi-hop control-data paths, such restricted flow modeling often fails to capture the full chain from input to output, leading to extensive false positives. (2) Inaccurate identification of sources and sinks (B1), where tools either misclassify benign program points as security-relevant or fail to correctly interpret the semantics of API usages.
L336: As shown in Figure cite117†6 , the LLM misidentifies the variable new as a pointer to newly allocated memory in C++ and assumes it may be NULL. However, new is an unsigned char variable that is assigned a value at line 13 and therefore cannot be NULL. However, throughout the entire reasoning process on this path, the LLM fails to recognize this and continues to treat the use of new as a potentially NPD vulnerability at line 17.
L337: cite118†Image: Refer to caption Fig. 6: An illustrating FP example of reason B1
L338: Beyond the shared sources of false positives, we further analyze the reasons unique to LLM-based vulnerability detection methods. Although LLMs exhibit strong code analysis abilities, their performance on vulnerability detection still faces several inherent limitations: First, LLMs often fail to recover the correct execution flow in the presence of complex control structures (Reason A2).
L339: For example, 24.6% of RepoAudit’s false positives arise because it overlooks key control-flow branches or constructs an incorrect data-flow graph, causing the detector to analyze paths that do not actually exist in the program. There is another interesting example in Figure cite119†7 , in the vim project, there are two gui_mch_destroy_scrollbar functions with the same signature, defined in gui_haiku.cc and gui_w32.c to support different operating systems.
L340: In practice, these two functions cannot be invoked together in a single build. However, when the LLM analyzes the two consecutive invocations of gui_mch_destroy_scrollbar in window.c, it incorrectly concludes that the first call resolves to the implementation in gui_haiku.cc and the second to the implementation in gui_w32.c, merging mutually exclusive execution paths and leading to an incorrect understanding of the program behavior.
L341: Second, LLMs frequently overlook implicit sanitization logic within a dataflow (Reason D1). Four out of five selected LLM-based methods suffer noticeably from this issue, leading them to flag dataflows as vulnerable even when proper sanitizers exist along the path. Finally, LLMs sometimes do not follow the prompt or CWE definition well (Reason C1). Both RepoAudit and IRIS flag benign code as vulnerable or report issues that do not conform to the CWE definitions specified in the prompt.
L342: The corresponding examples are shown in our Appendix A. These findings suggest that although LLMs are capable of reasoning about code semantics, reliably capturing precise and complete program behavior in complex real-world projects, as well as strictly adhering to prompt specifications, remain major challenges.
L344: ### V-D RQ4: Detection Overhead at Project Scale
L345: 
L346: TABLE VII: Computational overhead of evaluated tools on real-world projects. – represents tools that do not rely on LLMs.
L347: Tool  | Input Tokens (K)  | Output Tokens (K)  | Time (min)
L348: Min  | Max  | Avg  | Min  | Max  | Avg  | Min  | Max  | Avg
L349: RepoAudit  | 748.51  | 225,493.97  | 45,078.21  | 102.44  | 38,078.26  | 6,561.46  | 7.02  | 2,450.41  | 448.31
L350: KNighter  | 20.39  | 131.66  | 48.16  | 3.78  | 70.07  | 17.07  | 37.55  | 221.51  | 144.09
L351: IRIS  | 8.47  | 1,752.77  | 508.77  | 1.45  | 267.13  | 87.70  | 2.55  | 2,089.47  | 213.44
L352: LLMDFA  | 2,535.12  | 38,310.33  | 17,445.71  | 69.50  | 2,646.89  | 1,199.05  | 44.00  | 4,638.00  | 2,000.00
L353: INFERROI  | 142.50  | 2,871.49  | 1,193.45  | 64.51  | 1,408.23  | 575.84  | 20.25  | 176.27  | 78.10
L354: CodeQL  | –  | –  | –  | –  | –  | –  | 0.21  | 378.95  | 21.29
L355: Semgrep  | –  | –  | –  | –  | –  | –  | 0.07  | 2.43  | 0.64
L356: One primary concern for LLM-based methods is their cost and efficiency. In this research question, we measure the token consumption and time cost of the selected tools. Table cite121†VII reports the average overhead of these methods, and more detailed statistics are provided in Appendix C. Overall, LLM-based vulnerability detection methods impose substantial computational costs, raising practical concerns for project-scale adoption.
L357: Among all LLM-based methods, RepoAudit and LLMDFA exhibit the highest computational overhead on C/C++ and Java projects, respectively. RepoAudit can consume more than 225 million input tokens and more than 38 million output tokens for a single project, resulting in an average analysis time of over 448 minutes (more than 7 hours) per project.
L358: Similarly, LLMDFA also incurs extremely high token consumption, up to 38 million output tokens, and requires 2000 minutes (more than 33 hours) on average to analyze a single Java project. These results indicate that current LLM-based approaches face a severe scalability challenge when applied to large real-world repositories.
L359: In contrast, hybrid approaches such as IRIS and INFERROI, which integrate LLMs with static analysis, show more moderate overhead, though still requiring hundreds of thousands to millions of tokens and multi-hour runtimes for large projects. These results indicate that current LLM-based vulnerability detection methods remain computationally expensive, and their scalability is highly sensitive to prompting strategies and detection workflows, posing practical challenges for project scale adoption.
L360: In contrast, traditional tools (CodeQL and Semgrep) incur negligible overhead, completing analysis within seconds to minutes. This difference emphasizes a significant scalability gap: while LLM-based methods provide stronger semantic reasoning capabilities, they do so at the cost of significantly higher computational resources.
L361: These results suggest that improving cost efficiency, through better context pruning, incremental analysis, or lighter-weight LLM pipelines, remains essential before LLM-based vulnerability detectors can be deployed reliably at the project scale.
L362: ## VI Discussion
L363: ### VI-A Implications
L364: Our comprehensive analysis across five LLM-based vulnerability detectors and two traditional tools reveals that, although LLMs offer promising semantic reasoning capabilities and the potential to generalize beyond manually modeled security patterns, they remain far from mature enough for reliable vulnerability analysis in real-world scenarios.
L365: Despite demonstrating an ability to infer higher-level intentions that traditional static tools often miss, current LLM-based methods suffer from several practical limitations that restrict their effectiveness:
L366: (1) Dataflow reasoning is shallow and incomplete. LLM-based tools frequently construct partial or truncated dataflows, capturing only short caller-callee chains or dataflow paths (e.g., RepoAudit by default expands only three layers of the call-graph, and extending this depth results in exponential prompt growth and token cost).
L367: Consequently, risk is often inferred from local evidence without the global execution context, causing models to overlook sanitization or correct sink behavior that occurs further along the program path. Shallow dataflow is therefore a fundamental bottleneck: when the full path from “input $\rightarrow$ propagation $\rightarrow$ output” is not analyzed holistically, real vulnerabilities may be missed, while safe code is frequently misclassified as risky.
L368: (2) Imprecise source-sink identification. Based on our experiments, a considerable portion of FNs and FPs is due to the inaccurate classification of sources or sinks. In real-world projects, sources may be wrapped or abstracted behind project-specific APIs, propagate through multiple layers before reaching sinks, or be triggered via reflection, callbacks, and framework-driven lifecycle events.
L369: Although several LLM-based approaches (IRIS, LLMDFA) attempt to infer project-specific or vulnerability-specific sources/sinks via prompting, the inferred results are often unreliable in practice (e.g., IRIS mislabels Map.put() as a sink in Java projects, resulting in an amount of FPs). Thus, robust and context-aware source-sink inference remains an unresolved challenge.
L370: (3) Semantic understanding in complex contexts remains limited. As shown in Section cite22†V-C , a substantial portion of false positives produced by LLM-based vulnerability detectors stems from the misinterpretation of code semantics.
L371: In many cases, models overlook key program points along a dataflow (e.g., a sanitizer, a deferred release, a null-check, or a conditional exit), or fail to infer the actual execution behavior of code due to language-specific constructs such as try-with-resources, destructors, template expansion, or macro-controlled branching. These semantic gaps often cause LLMs to reason along incorrect control paths or assume unsafe behavior where none exists, ultimately misclassifying benign code as vulnerable.
L372: We suggest future work strengthen semantic reasoning through hybrid workflows, augmenting LLMs with intermediate program representations, graph-based context retrieval, and static analysis signals to provide more complete execution context [cite122†62 , cite53†15 ].
L373: (4) Prompt-alignment and task compliance are inconsistent. In our evaluation, we observe that methods such as RepoAudit and IRIS, which rely on LLMs to perform reasoning over extracted dataflows, may still fail to adhere to the intended vulnerability definition or CWE scope in the prompt.
L374: Even when the reasoning is correct at a syntactic or control-flow level, the model occasionally drifts from the task objective, producing conclusions that do not align with the vulnerability type under detection—reflecting semantic drift and task-misalignment. To improve this, future systems may require structured multi-agent collaboration, self-verification modules, or constraint-guided reasoning to enforce consistent detection goals [cite123†63 , cite124†64 ].
L375: (5) Scalability remains the bottleneck. Project-scale analysis demands enormous computational overhead. As shown in Section cite23†V-D , RepoAudit and LLMDFA consume up to hundreds of millions of tokens and require hours to days to complete a single project, making them unsuitable for continuous integration.
L376: This observation aligns with both the authors’ discussions in their papers and the feedback we received from them, who confirmed that the current implementations may incur substantial computational overhead when analyzing large projects. Hybrid approaches (IRIS, INFERROI) reduce, but do not eliminate, the high cost. To achieve scalable detection, future work may adopt hierarchical analysis, reuse intermediate reasoning through caching, and minimize redundant LLM calls [cite122†62 ].
L377: ### VI-B Threats to Validity
L378: Internal Validity Our analysis involves expert judgment. Although two independent authors conducted labeling and reconciliation to reduce subjectivity (Section cite18†IV ), classification accuracy may still be influenced by personal experience, interpretation of code semantics, or reasoning about exploitability. Misreading or misinterpretation of complex code flows may introduce bias into the taxonomy of FP causes.
L379: To overcome these threats, the two authors adopt an inductive open-coding procedure with double coding [cite113†61 ], independently validated all sampled cases and resolved any disagreements through discussion, and we released all experimental artifacts, including evaluation scripts, prompts, taxonomy labels, and detailed statistics for external inspection and replication.
L380: External Validity Our evaluation considers 5 LLM-based and 2 traditional vulnerability detectors, selected because they are open-source, runnable at the project scale, and representative of emerging design workflows. However, they may not fully represent all possible architectures, languages, or prompting paradigms. As the field evolves rapidly, future models or customized enterprise-scale deployments may demonstrate different capabilities.
L381: Moreover, our evaluation covers a set of real-world repositories across two major programming languages (Java, C/C++), but may not generalize uniformly to systems written in Rust, Go, TypeScript, or large multi-language projects.
L382: ## VII Conclusion
L383: In this paper, we conduct the first comprehensive study of specialized LLM-based vulnerability detectors at the project scale, analyzing 5 representative LLM-based tools and comparing them against 2 traditional static analysis tools. Our evaluation begins with 222 known vulnerabilities spanning 8 CWE types, where we observe that current approaches often fail to identify these vulnerabilities, primarily due to inaccurate source-sink identification.
L384: We then scale our analysis to 24 open-source projects and manually examine 385 sampled reports. From this investigation, we construct a taxonomy of false positive causes and quantify how different tools are affected. Our findings reveal that although LLM-based methods exhibit stronger performance than traditional static analyzers, they still face fundamental challenges in dataflow construction, source-sink identification, and deep semantic understanding.
L385: Furthermore, our runtime and token usage measurements show that scalability remains a core bottleneck, especially for end-to-end LLM workflows. Finally, to support future progress in this domain, we distill our observations into 5 implications for the research community. We hope this work can inspire future designs that make automated security detection both more accurate and more practical in real-world scenarios.

