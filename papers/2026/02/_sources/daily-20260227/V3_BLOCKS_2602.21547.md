[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: 𝖱𝖠𝖢 \mathsf{RAC} : Relation-Aware Cache Replacement for Large Language Models

[3] h6: Abstract.

[4] p: The scaling of Large Language Model ( 𝖫𝖫𝖬 \mathsf{LLM} ) services faces significant cost and latency challenges, making effective caching under tight capacity crucial. Existing cache replacement policies, from heuristics to learning-based methods, predominantly rely on limited-window statistics such as recency and frequency. We show these signals are not robust for real-world 𝖫𝖫𝖬 \mathsf{LLM} workloads, which exhibit long reuse distances and sparse local recurrence.

[5] p: To address these limitations, we propose Relation-Aware Cache ( 𝖱𝖠𝖢 \mathsf{RAC} ), an online eviction strategy that leverages semantic relations among requests to guide eviction decisions. 𝖱𝖠𝖢 \mathsf{RAC} synthesizes two relation-aware signals: (1) Topical Prevalence , which aggregates access evidence at the topic level to capture long-horizon reuse; and (2) Structural Importance , which leverages local intra-topic dependency structure to discriminate entries by their future reuse value. Extensive evaluations show that 𝖱𝖠𝖢 \mathsf{RAC} maintains high effectiveness across diverse workloads, consistently surpassing state-of-the-art baselines by 20%–30% in cache hit ratio.

[6] h2: 1. Introduction

[7] p: Large language model ( 𝖫𝖫𝖬 \mathsf{LLM} ) services have been widely deployed at scale, operating under growing request concurrency and context lengths ( OpenAI, 2022 ; Anthropic, 2023 ) . To reduce the cost of transformer-based inference, recent systems increasingly rely on caching to reuse previously generated content ( i.e. , semantic cache) ( Bang, 2023 ; Li et al., 2024 ; Gill and others, 2024 ) or intermediate states ( i.e. , 𝖪𝖵 \mathsf{KV} cache) ( Lin et al., 2025 ; Yao et al., 2024 ) . However, real-world deployments operate under tight cache budgets, making trace-driven admission and eviction decisions a central challenge for maximizing future reuse ( Yang et al., 2001 ) .

[8] p: Existing 𝖫𝖫𝖬 \mathsf{LLM} cache replacement methods mainly fall into two categories. (1) Traditional policies ( Mattson et al., 1970a ; Lee and others, 2001 ; Megiddo and Modha, 2003a ; Cao and Irani, 1997 ; Cherkasova and Ciardo, 1998 ; Beckmann et al., 2018 ; Liu et al., 2023 ; Zhang et al., 2023b ; Zhang et al., 2023a ; Hu et al., 2024 ) compute an eviction score from short-window statistics ( e.g. , recency, frequency, or their combinations) and evict the entry with the minimum score under capacity pressure. (2) Learning-based methods ( Song and others, 2020 ; Liu et al., 2020 ; Vietri et al., 2018b ; Rodriguez et al., 2021a ; Song and others, 2023 ; Yang et al., 2023 ) learn a predictor from historical access traces to estimate future reuse ( e.g. , reuse within a horizon or next access distance) and evict entries according to the predictions.

[9] p: However, recent studies show that real 𝖫𝖫𝖬 \mathsf{LLM} workloads exhibit long reuse distances and sparse local recurrence ( Yu et al., 2025 ) . As a result, most cache entries are accessed only once or reappear after long gaps, leaving little reuse signal within short observation windows. Under such workloads, traditional policies that rely on short-range statistics become ineffective, as recency and frequency no longer correlate with future reuse. Learning-based methods, constrained by finite prediction horizons, similarly fail to capture reuse events beyond their observable scope. We next use a concrete example to illustrate how such failures arise in practice.

[10] figure: Items Request semantics ( context ) a 0 a_{0} (queries) a 1 a_{1} – a 5 a_{5} A code-centric request sequence. a 0 a_{0} ( context ) asks the 𝖫𝖫𝖬 \mathsf{LLM} to read and explain a given code snippet. a 1 a_{1} queries the functionality of a specific function; a 2 a_{2} queries variable roles and data flow; a 3 a_{3} queries invariants or assumptions; a 4 a_{4} queries potential corner cases; and a 5 a_{5} queries possible optimizations. (queries) a 1 ∗ a_{1}^{*} – a 5 ∗ a_{5}^{*} A set of follow-up queries reusing the code context in a 0 a_{0} , where a 1 ∗ a_{1}^{*} – a 5 ∗ a_{5}^{*} target different functions, variables, assumptions, corner cases, and optimizations of the same code. ( context ) b 2 b_{2} (queries) b 0 b_{0} , b 1 b_{1} , b 3 b_{3} – b 5 b_{5} A writing task sequence. b 0 b_{0} asks the 𝖫𝖫𝖬 \mathsf{LLM} to draft a short text on a given topic. b 1 b_{1} asks for revision suggestions. b 2 b_{2} ( context ) specifies explicit writing constraints ( e.g. , tone and formatting rules). b 3 b_{3} asks to rewrite the text under the constraints; b 4 b_{4} asks to condense it; and b 5 b_{5} asks to finalize the text accordingly. (queries) b 0 ∗ , b 1 ∗ b_{0}^{*},b_{1}^{*} b 3 ∗ b_{3}^{*} – b 5 ∗ b_{5}^{*} A repeated writing task that reuses the same constraints in b 2 b_{2} . b 0 ∗ b_{0}^{*} and b 1 ∗ b_{1}^{*} draft a new text on a different topic, while b 3 ∗ b_{3}^{*} – b 5 ∗ b_{5}^{*} request revision, rewriting, condensation, and finalization under the same constraints specified in b 2 b_{2} . Table 1 . Example items and their request semantics.

[11] figure: Figure 1 . Demonstration of traditional, learning-based, and offline-optimal policies on Example 1.

[12] h6: Example 1.

[13] p: Consider the 𝖫𝖫𝖬 \mathsf{LLM} request sequence { a 0 ∼ a 5 } → { b 0 ∼ b 5 } → { a 0 , a 1 ∗ ∼ a 5 ∗ } → { b 0 ∗ ∼ b 5 ∗ } \{a_{0}\!\sim\!a_{5}\}\!\rightarrow\!\{b_{0}\!\sim\!b_{5}\}\!\rightarrow\!\{a_{0},a_{1}^{*}\!\sim\!a_{5}^{*}\}\!\rightarrow\!\{b_{0}^{*}\!\sim\!b_{5}^{*}\} , where each item corresponds to a query listed in Table 1 , and the sequence alternates between two topics ( i.e. , A: coding and B: writing), each forming a coherent task in which context-setting requests ( i.e. , a 0 a_{0} and b 2 b_{2} ) are followed by related queries. Figure 1 illustrates the semantic structure among requests induced by semantic relatedness. Assume a cache of size | 𝒞 | = 6 |{\mathcal{C}}|=6 ; we compare the outcomes of different cache strategies.

[14] p: Traditional policies . As shown in Fig. 1(I), taking 𝖫𝖱𝖴 \mathsf{LRU} ( Mattson et al., 1970a ) as an example, each batch of semantically related requests fills the cache. The arrival of the next batch evicts all resident entries before any reuse can occur, resulting in zero cache hits.

[15] p: Online learning policies . Taking 𝖫𝖱𝖡 \mathsf{LRB} ( Song and others, 2020 ) as an example, at cold start (Fig. 1(I)) or with a small training window (Fig. 1(II-left)), no reuse is observed and the policy degenerates to traditional behavior. Only with a sufficiently large window (Fig. 1(II-right)) can reuse be learned, at the cost of significantly higher overhead (especially for semantic caches, where hit determination itself requires costly similarity computation).

[16] p: Offline optimal . As shown in Fig. 1(III), the offline optimal policy preserves structurally central entries while evicting peripheral ones. Across topic switches, core requests ( e.g. , a 0 a_{0} and b 2 b_{2} ) are retained and repeatedly reused, while peripheral entries are trimmed, maximizing reuse by preserving structurally central items.

[17] p: The example above shows that under tight cache capacity, many entries are evicted before they are reused but offline optimal shows it can be reused. As a result, short-window signals such as recency and access frequency provide weak indications of future reuse. Nevertheless, we observe that reuse in 𝖫𝖫𝖬 \mathsf{LLM} can depend on request relations such as topical recurrence across episodes and prerequisite dependencies within a topic.

[18] p: These observations raise three questions: (1) what relations among requests are observable online with low overhead; (2) how to convert such relations into an eviction signal beyond entry-local recency/frequency; and (3) how to implement the resulting policy under a hard capacity constraint.

[19] p: To address them, we (1) operationalize the two patterns as two online eviction signals: Topical Prevalence (TP) aggregates long-horizon semantic recurrence at the topic level, while Topic Structural Importance (TSI) prioritizes within-topic context anchors induced by prerequisite dependency; (2) integrate TP and TSI into a unified eviction value via a lightweight heuristic; and (3) implement the resulting policy under a hard capacity budget. Both signals are lightweight to maintain online, yield relation-derived cues beyond recency/frequency, and are directly actionable under hard-capacity replacement.

[20] p: Contributions & Organization. We propose Relation-Aware Cache ( 𝖱𝖠𝖢 \mathsf{RAC} ), an online cache eviction strategy that uses relation-aware values and provides an end-to-end pipeline from relation capture to eviction decisions.

[21] p: Relation-aware eviction rule. (Section 3.1 ) We formalize semantic cache replacement under a capacity constraint and show why entry-local short-window signals are insufficient when reuse is delayed. Based on this model, we introduce two relation-aware values and combine them into a single eviction score, yielding an online rule that specifies both cache updates and eviction under pressure.

[22] p: Computation of Topical Prevalence. (Section 3.2 ) We design an online mechanism to estimate topical prevalence by organizing requests into topic clusters and aggregating access evidence at the topic level. The resulting topic score summarizes long-horizon reuse signals shared by entries in the same topic, providing information that is missing from per-entry recency/frequency.

[23] p: Computation of Structural Importance. (Section 3.3 ) We design an online module to estimate structural importance using a lightweight identifier of local dependency structure. It assigns higher value to prerequisite entries that support more downstream requests, complementing purely statistical signals when direct repeats are sparse.

[24] p: Experimental study. (Section 4 ) We evaluate 𝖱𝖠𝖢 \mathsf{RAC} on real-world dialogue traces and on synthetic workloads derived from the modeled process. On real traces, 𝖱𝖠𝖢 \mathsf{RAC} improves hit ratio by 20% on average over representative frequency-/recency-based baselines; on model-driven synthetic workloads, it achieves an average 30% gain in regimes where relation-aware aggregation is most beneficial.

[25] p: We introduce the problem setting in Section 2 , discuss related work in Sections 5 , and conclude in Section 6 .

[26] h2: 2. Preliminary and Problem Formulation

[27] p: We first define the workload and cache abstractions and then formalize the online cache admission and eviction problem.

[28] p: Preliminary . We specify (1) a topic-aware workload model for dialogue queries and (2) a cache model that maps queries to cache entries and defines cache hits.

[29] p: Topic. Following ( Arguello and Rosé, 2006 ; Grosz and Sidner, 1986 ) , we define a topic as a dialogue segment with a relatively stable semantic focus ( i.e. , a consistent discourse segment purpose , DSP). We model the dialogue as a query sequence indexed by time steps t = 1 , 2 , … t=1,2,\ldots . Each query q t q_{t} is assigned a topic label Z t ∈ { 1 , … , S } Z_{t}\in\{1,\ldots,S\} , where S S is the number of distinct topics; when Z t = s Z_{t}=s , query q t q_{t} belongs to topic s s . A topic s s may appear in multiple topic episodes , where each episode is a maximal contiguous time interval during which Z t = s Z_{t}=s . Episodes of the same topic can be separated by other topics, allowing topic s s to reappear later.

[30] p: Topic sequence as a semi-Markov process. Given the topic labels { Z t } \{Z_{t}\} , we obtain an episode-level sequence by collapsing each topic episode into a single state visit. Each visit is represented by (1) the topic identity and (2) its episode length (the number of consecutive queries in that episode). For example, if the topic-label sequence is { A , A , B , B , B , A } \{A,A,B,B,B,A\} , then the episode-level sequence is ( A , 2 ) → ( B , 3 ) → ( A , 1 ) (A,2)\!\to\!(B,3)\!\to\!(A,1) . We model this episode-level sequence as a semi-Markov process over topics, where: (1) transitions occur only at episode boundaries; (2) the sojourn time in a state equals the episode length; and (3) the next topic depends only on the current topic ( i.e. , a first-order Markov property for the embedded jump chain).

[31] p: Intra-topic query dependency. Following ( Li et al., 2020 ; Li et al., 2014 ) , we assume that queries within a topic episode exhibit an implicit dependency structure. For each topic s ∈ { 1 , … , S } s\in\{1,\ldots,S\} and any episode of topic s s , we represent the intra-episode dependencies as a set of time-respecting discourse dependency links ℰ s \mathcal{E}_{s} . Each link ( i , j ) ∈ ℰ s (i,j)\in\mathcal{E}_{s} with i < j i<j indicates that query q j q_{j} depends on an earlier query q i q_{i} for context ( e.g. , co-reference resolution, clarification, or continuation). Therefore, queries in an episode induce a directed acyclic graph (DAG) that captures the flow of context. Unless otherwise specified, we define and use these dependencies only within the same topic episode.

[32] p: Cache. We next define the cache model used in this paper, including (1) the cache entry abstraction, (2) the cache store 𝒞 {\mathcal{C}} and its capacity, and (3) the cache hit criterion.

[33] p: Entry. A cache entry e e is the atomic object managed by the cache. Each entry has a semantic embedding, and we use a similarity function 𝗌𝗂𝗆 ⁡ ( ⋅ , ⋅ ) {\mathsf{sim}}(\cdot,\cdot) ( e.g. , cosine similarity) to measure proximity between embeddings. A user query q t q_{t} may map to one entry (query-level caching) or multiple entries (chunk-level caching).

[34] p: Store. We denote the cache as a set of entries 𝒞 = { e 1 , … , e m } {\mathcal{C}}=\{e_{1},\dots,e_{m}\} with capacity | 𝒞 | ≤ C |{\mathcal{C}}|\leq C . Depending on the cache type, an entry may store reusable content in one of the following forms: (a) semantic content ( e.g. , passages, past responses, summaries, or prompt patches ( Bang, 2023 ) ), (b) 𝖪𝖵 \mathsf{KV} states for prefill reuse ( Yang et al., 2024 ; Yang et al., 2025 ) , or (c) a hybrid payload that jointly manages text and 𝖪𝖵 \mathsf{KV} states ( Li et al., 2025 ) . Each entry also maintains lightweight intrinsic metadata ( e.g. , recency and frequency).

[35] p: Hits. A query q i q_{i} is a hit on entry e j e_{j} if it satisfies the system-defined equivalence condition, typically via one of the following: (a) semantic equivalence , where 𝗌𝗂𝗆 ⁡ ( q i , e j ) ≥ τ {\mathsf{sim}}(q_{i},e_{j})\geq\tau for a predefined threshold τ \tau ; or (b) content equivalence , where the cached payload in e j e_{j} matches the required content or aligns with the query context ( e.g. , prefix alignment in 𝖪𝖵 \mathsf{KV} caches). Otherwise, q i q_{i} is a miss.

[36] p: Problem. We are now ready to formalize the online cache admission and eviction problem for maximizing cache hits.

[37] p: Input : A time-ordered 𝖫𝖫𝖬 \mathsf{LLM} query stream Q = { q 1 , q 2 , … } Q\!=\!\{q_{1},q_{2},\ldots\} ; a cache of capacity C C that is initially empty; and the cache hit criterion.

[38] p: Output : An online caching policy π \pi that decides, upon each request arrival, (1) whether to admit the corresponding entry into the cache and (2) which entries to evict when the cache is full.

[39] p: Objective : Maximize the total number of cache hits over Q Q subject to the capacity constraint C C .

[40] p: Remark. Observe the following. (1) This problem is fully online: π \pi makes decisions without future knowledge and can only use information available up to the current time step. (2) The hit criterion is system-defined, and our formulation is agnostic to the specific cache type. In other words, our method can be instantiated across mainstream caching settings today, such as embedding-based semantic equivalence for semantic caching ( Bang, 2023 ) and compositional content equivalence for 𝖪𝖵 \mathsf{KV} caching in LLM serving. ( Agarwal et al., 2025 ; Lin et al., 2025 ; Yao et al., 2024 ) (3) The topic-aware workload abstractions (topics, episodes, and intra-episode dependencies) specify additional structure in Q Q that our policy can exploit, but they do not change the underlying objective of maximizing cache hits.

[41] h2: 3. Design of Relation-Aware Caching

[42] p: This section designs the relation-aware cache value used by the online admission and eviction policy. Section 3.1 introduces the basic idea and defines the entry value as the product of two online signals, where (1) topical prevalence captures topic-level activeness over time and (2) structural importance captures how critical an entry is as a context anchor within a topic episode. Section 3.2 and Section 3.3 detail the online computation and maintenance of topical prevalence and structural importance, respectively.

[43] h3: 3.1. Basic Idea

[44] p: As in Section 2 , we model the workload as a query sequence { q t } \{q_{t}\} with topic labels { Z t } \{Z_{t}\} ( Jelenković and Radovanović, 2009 ) . We further interpret the topic-label process at episode granularity as a semi-Markov process.

[45] p: Topic occupancy and query generation. For each topic s ∈ { 1 , … , S } s\in\{1,\ldots,S\} , let (1) π s \pi_{s} denote its long-run occupancy probability, i.e. , the steady-state fraction of time steps with topic label Z t = s Z_{t}=s , and (2) p ⁡ ( q ∣ s ) p(q\mid s) denote the conditional probability of observing the concrete query content q q when the topic label is s s . By the law of total probability, the marginal probability of observing a specific query q t q_{t} at time t t is

[46] table: p ⁡ ( q t ) ≜ ∑ s = 1 S π s ​ p ​ ( q t ∣ s ) . p(q_{t})\;\triangleq\;\sum_{s=1}^{S}\pi_{s}\,p(q_{t}\mid s).

[47] p: Equivalently, isolating the in-topic component for the realized topic label Z t Z_{t} yields

[48] table: p ⁡ ( q t ) = π Z t ​ p ​ ( q t ∣ Z t ) + ∑ s ≠ Z t π s ​ p ​ ( q t ∣ s ) . p(q_{t})=\pi_{Z_{t}}p\big(q_{t}\mid Z_{t}\big)+\sum_{s\neq Z_{t}}\pi_{s}\,p(q_{t}\mid s).

[49] p: Due to topic locality, we typically have p ⁡ ( q t ∣ Z t ) ≫ p ⁡ ( q t ∣ s ) p(q_{t}\mid Z_{t})\gg p(q_{t}\mid s) for s ≠ Z t s\neq Z_{t} , so the in-topic term π Z t ​ p ​ ( q t ∣ Z t ) \pi_{Z_{t}}p\big(q_{t}\mid Z_{t}\big) dominates the mixture.

[50] p: Relation-aware value. We design a heuristic value to estimate the factorized term π Z t ​ p ​ ( q ∣ Z t ) \pi_{Z_{t}}p(q\mid Z_{t}) by tracking its two factors with observable online signals:

[51] p: Topical Prevalence ( 𝖳𝖯 \mathsf{TP} ). A per-topic temporal signal 𝖳𝖯 ⁡ ( s ) {\mathsf{TP}}(s) tracks the topic weight π s \pi_{s} via a lightweight decay-and-accumulate update on topic hits (see details in Section 3.2 ).

[52] p: Topic Structural Importance ( 𝖳𝖲𝖨 \mathsf{TSI} ). A per-item topological signal 𝖳𝖲𝖨 ⁡ ( q ) {\mathsf{TSI}}(q) proxies the in-topic strength p ⁡ ( q ∣ s ) p(q\mid s) by tracking the dependency in-degree ( i.e. , dependency count) of item q q within its topic episode (see details in Section 3.3 ).

[53] p: Consequently, to approximate the dominant in-topic component π Z ​ p ​ ( q ∣ Z ) \pi_{Z}p(q\mid Z) using these online statistics, we define the unified heuristic value for a query q q associated with topic Z Z as

[54] table: (1) 𝖵𝖺𝗅𝗎𝖾 ⁡ ( q ) = 𝖳𝖯 ⁡ ( Z ) ⋅ 𝖳𝖲𝖨 ⁡ ( q ) . {\mathsf{Value}}(q)={\mathsf{TP}}(Z)\cdot{\mathsf{TSI}}(q).

[55] p: Online flow. With the relation-aware value 𝖵𝖺𝗅𝗎𝖾 ⁡ ( ⋅ ) {\mathsf{Value}}(\cdot) in place, we next design a complete cache management workflow to make it actionable online. The workflow integrates two computation components that maintain the required online signals, and specifies how these signals are refreshed and used to guide eviction (Algorithm 1 ). Upon the arrival of request q t q_{t} , we: (1) refresh 𝖳𝖯 ⁡ ( Z t ) {\mathsf{TP}}(Z_{t}) ; (2) update 𝖳𝖲𝖨 ⁡ ( q ) {\mathsf{TSI}}(q) for items q q that are structurally related to q t q_{t} within the current topic episode; and (3) insert the corresponding cache entry into 𝒞 {\mathcal{C}} and, if | 𝒞 | > C |{\mathcal{C}}|>C , evict the entry whose associated item q q has the smallest 𝖵𝖺𝗅𝗎𝖾 ⁡ ( q ) {\mathsf{Value}}(q) .

[56] figure: Algorithm 1 Cache-Side Main Workflow Input: incoming request q t q_{t} ; cache 𝒞 {\mathcal{C}} ; current time step t t Output: updated cache 𝒞 {\mathcal{C}} 1 Procedure OnArrive ( q t , 𝒞 , t q_{t},{\mathcal{C}},t ) 2 Z t , { 𝖳𝖯 ⁡ ( s ) } ← UpdateTP ​ ( q t , 𝒞 , t ) Z_{t},\{{\mathsf{TP}}(s)\}\leftarrow\textsc{UpdateTP}(q_{t},{\mathcal{C}},t) ; // Alg. 2 3 { 𝖳𝖲𝖨 ⁡ ( q ) } ← UpdateTSI ​ ( q t , 𝒞 , t ) \{{\mathsf{TSI}}(q)\}\leftarrow\textsc{UpdateTSI}(q_{t},{\mathcal{C}},t) ; // Alg. 4 insert the cache entries e ¯ t \bar{e}_{t} of q t q_{t} (with label Z t Z_{t} ) into 𝒞 {\mathcal{C}} ; 5 while | 𝒞 | > C |{\mathcal{C}}|>C do 6 evict entries e ¯ i ⊂ 𝒞 \bar{e}_{i}\subset{\mathcal{C}} (for query q i q_{i} with label Z i Z_{i} ) with the minimum 𝖳𝖯 ⁡ ( Z i ) ⋅ 𝖳𝖲𝖨 ⁡ ( q i ) {\mathsf{TP}}(Z_{i})\cdot{\mathsf{TSI}}(q_{i}) ; 7 return 𝒞 {\mathcal{C}} ;

[57] h3: 3.2. Computation of Topical Prevalence.

[58] p: As a key component of RAC and the first step in its online workflow, we maintain a topic-level topical prevalence signal as an online surrogate for the occupancy π s \pi_{s} , and use it to guide cache admission and eviction. For each topic s s , we maintain a score 𝖳𝖯 ⁡ ( s ) {\mathsf{TP}}(s) that summarizes how active s s is at the current time, combining both hit frequency and recency via exponential decay. This score is evaluated during eviction to compare entries across topics.

[59] h6: Definition 1 (Topical prevalence ( 𝖳𝖯 {\mathsf{TP}} )).

[60] p: For a topic s s , let ℋ t ​ ( s ) ≜ { i ≤ t : Z i = s } \mathcal{H}_{t}(s)\triangleq\{i\leq t:Z_{i}=s\} denote its hit times up to time t t . Given a decay coefficient α ≥ 0 \alpha\geq 0 , we define

[61] table: 𝖳𝖯 t ​ ( s ) ≜ ∑ i ∈ ℋ t ​ ( s ) ( 1 2 ) α ⁡ ( t − i ) . {\mathsf{TP}}_{t}(s)\;\triangleq\;\sum_{i\in\mathcal{H}_{t}(s)}\Big(\tfrac{1}{2}\Big)^{\alpha\,(t-i)}.\vskip-8.61108pt

[62] p: Intuitively, hits are exponentially down-weighted by age, such that 𝖳𝖯 t ​ ( s ) {\mathsf{TP}}_{t}(s) captures both recency and frequency.

[63] p: Online maintenance for 𝖳𝖯 {\mathsf{TP}} . Directly maintaining 𝖳𝖯 {\mathsf{TP}} in Definition 1 requires iterating over all hit times i ∈ ℋ t ​ ( s ) i\in\mathcal{H}_{t}(s) . To enable O ⁡ ( 1 ) O(1) updates, we cache the value at the latest hit. Specifically, let t 𝗅𝖺𝗌𝗍 ​ ( s ) ≜ max ⁡ ℋ t ​ ( s ) t_{{\mathsf{last}}}(s)\triangleq\max\mathcal{H}_{t}(s) denote the most recent hit time of topic s s (with t 𝗅𝖺𝗌𝗍 ​ ( s ) = 0 t_{{\mathsf{last}}}(s)=0 if ℋ t ​ ( s ) = ∅ \mathcal{H}_{t}(s)=\emptyset ), and let 𝖳𝖯 𝗅𝖺𝗌𝗍 ​ ( s ) {\mathsf{TP}}_{{\mathsf{last}}}(s) denote the stored 𝖳𝖯 {\mathsf{TP}} value right after processing the request at time t 𝗅𝖺𝗌𝗍 ​ ( s ) t_{{\mathsf{last}}}(s) . For any time t ≥ t 𝗅𝖺𝗌𝗍 ​ ( s ) t\geq t_{{\mathsf{last}}}(s) , we have

[64] table: 𝖳𝖯 t ​ ( s ) = ( 1 2 ) α ​ ( t − t 𝗅𝖺𝗌𝗍 ​ ( s ) ) ⋅ 𝖳𝖯 𝗅𝖺𝗌𝗍 ​ ( s ) . {\mathsf{TP}}_{t}(s)=\Big(\tfrac{1}{2}\Big)^{\alpha\,(t-t_{{\mathsf{last}}}(s))}\cdot{\mathsf{TP}}_{{\mathsf{last}}}(s).

[65] p: Therefore, we store only two per-topic scalars: t 𝗅𝖺𝗌𝗍 ​ ( s ) t_{{\mathsf{last}}}(s) and 𝖳𝖯 𝗅𝖺𝗌𝗍 ​ ( s ) {\mathsf{TP}}_{{\mathsf{last}}}(s) . On a hit to s s , we update 𝖳𝖯 𝗅𝖺𝗌𝗍 ​ ( s ) ← 𝖳𝖯 t ​ ( s ) {\mathsf{TP}}_{{\mathsf{last}}}(s)\leftarrow{\mathsf{TP}}_{t}(s) and set t 𝗅𝖺𝗌𝗍 ​ ( s ) ← t t_{{\mathsf{last}}}(s)\leftarrow t . During eviction, we compute 𝖳𝖯 t ​ ( s ) {\mathsf{TP}}_{t}(s) on demand using the closed form above. We next describe how the cache performs topic routing and triggers the above 𝖳𝖯 {\mathsf{TP}} refresh online.

[66] p: Cache-side topic routing and 𝖳𝖯 {\mathsf{TP}} refresh. Algorithm 2 specifies how the cache assigns each request q t q_{t} to a topic and refreshes the corresponding 𝖳𝖯 {\mathsf{TP}} state. We maintain a cache-side topic index: each topic s s stores (1) a representative embedding r ⁡ ( s ) r(s) for routing and (2) a list of resident entries currently assigned to s s . On arrival of q t q_{t} , we: (1) compute its similarity to each r ⁡ ( s ) r(s) and keep topics within the similarity threshold τ \tau ; (2) if no candidate exists, create a new topic label Z t Z_{t} and initialize its states; (3) otherwise set Z t Z_{t} to the most similar candidate; (4) treat Z t Z_{t} as a hit and refresh 𝖳𝖯 𝗅𝖺𝗌𝗍 ​ ( Z t ) {\mathsf{TP}}_{{\mathsf{last}}}(Z_{t}) by decay-and-increment, and set t 𝗅𝖺𝗌𝗍 ​ ( Z t ) ← t t_{{\mathsf{last}}}(Z_{t})\leftarrow t . We detail how to update representatives and maintain membership under eviction in Appendix 8 .

[67] figure: Algorithm 2 Cache-side Topic Routing and 𝖳𝖯 {\mathsf{TP}} Refresh Input: incoming request q t q_{t} ; cache 𝒞 {\mathcal{C}} ; current time step t t ; similarity threshold τ \tau ; decay coefficient α \alpha Data: states { t 𝗅𝖺𝗌𝗍 ​ ( s ) } \{t_{{\mathsf{last}}}(s)\} , { 𝖳𝖯 𝗅𝖺𝗌𝗍 ​ ( s ) } \{{\mathsf{TP}}_{{\mathsf{last}}}(s)\} , and representative embedding { r ⁡ ( s ) } \{r(s)\} for each appeared topic s s Output: assigned topic label Z t Z_{t} of q t q_{t} , and { 𝖳𝖯 ⁡ ( s ) } \{{\mathsf{TP}}(s)\} for each topic s s that appears in 𝒞 {\mathcal{C}} 1 Procedure UpdateTP ( q t , 𝒞 , t q_{t},{\mathcal{C}},t ) 2 Z t ← 𝖲𝖾𝖺𝗋𝖼𝗁𝖳𝗈𝗉𝗂𝖼 ⁡ ( q t , τ , { r ⁡ ( s ) } ) Z_{t}\leftarrow{\mathsf{SearchTopic}}(q_{t},\tau,\{r(s)\}) ; 3 if Z t = ∅ Z_{t}=\emptyset then 4 create a new topic label Z t Z_{t} and assign Z t Z_{t} to q t q_{t} ; 5 initialize t 𝗅𝖺𝗌𝗍 ​ ( Z t ) ← t t_{{\mathsf{last}}}(Z_{t})\leftarrow t , 𝖳𝖯 𝗅𝖺𝗌𝗍 ​ ( Z t ) ← 0 {\mathsf{TP}}_{{\mathsf{last}}}(Z_{t})\leftarrow 0 , and r ⁡ ( Z t ) ← r(Z_{t})\leftarrow the embedding of q t q_{t} ; 6 𝖳𝖯 𝗅𝖺𝗌𝗍 ​ ( Z t ) ← ( 1 2 ) α ⋅ ( t − t 𝗅𝖺𝗌𝗍 ​ ( Z t ) ) ⋅ 𝖳𝖯 𝗅𝖺𝗌𝗍 ​ ( Z t ) + 1 {\mathsf{TP}}_{{\mathsf{last}}}(Z_{t})\leftarrow\big(\tfrac{1}{2}\big)^{\alpha\cdot\big(t-t_{{\mathsf{last}}}(Z_{t})\big)}\cdot{\mathsf{TP}}_{{\mathsf{last}}}(Z_{t})+1 ; 7 t 𝗅𝖺𝗌𝗍 ​ ( Z t ) ← t t_{{\mathsf{last}}}(Z_{t})\leftarrow t ; 8 evaluate 𝖳𝖯 ⁡ ( s ) = ( 1 2 ) α ⋅ ( t − t 𝗅𝖺𝗌𝗍 ​ ( s ) ) ⋅ 𝖳𝖯 𝗅𝖺𝗌𝗍 ​ ( s ) {\mathsf{TP}}(s)=\big(\tfrac{1}{2}\big)^{\alpha\cdot\big(t-t_{{\mathsf{last}}}(s)\big)}\cdot{\mathsf{TP}}_{{\mathsf{last}}}(s) lazily for topics s s that appear in 𝒞 {\mathcal{C}} during eviction process; 9 return Z t Z_{t} and { 𝖳𝖯 ⁡ ( s ) } \{{\mathsf{TP}}(s)\} ;

[68] h3: 3.3. Computation of Structural Importance.

[69] p: We next introduce an item-level signal to prioritize entries within the same topic. Within each episode of topic s s , queries are connected by dependency links ℰ s \mathcal{E}_{s} as defined in Section 2 . Intuitively, a query q q is important for two reasons: (1) it is requested multiple times within topic s s , and (2) it provides context required by downstream queries through ℰ s \mathcal{E}_{s} . We capture these two effects by using a topic structural importance score 𝖳𝖲𝖨 ⁡ ( q ) {\mathsf{TSI}}(q) to guide within-topic eviction, and we formally define 𝖳𝖲𝖨 ⁡ ( q ) {\mathsf{TSI}}(q) as follows.

[70] h6: Definition 2 (Topic Structural Importance ( 𝖳𝖲𝖨 \mathsf{TSI} )).

[71] p: For a query q q routed to topic s s , we define

[72] table: 𝖳𝖲𝖨 ⁡ ( q ) ≜ 𝖿𝗋𝖾𝗊 ⁡ ( q ) + λ ​ 𝖽𝖾𝗉 ​ ( q ) , {\mathsf{TSI}}(q)\;\triangleq\;{\mathsf{freq}}(q)\;+\;\lambda\,{\mathsf{dep}}(q),

[73] p: where 𝖿𝗋𝖾𝗊 ⁡ ( q ) {\mathsf{freq}}(q) is the number of cache hits to q q so far in topic s s , λ ≥ 0 \lambda\geq 0 is a weight parameter, and 𝖽𝖾𝗉 ⁡ ( q ) {\mathsf{dep}}(q) is the downstream hit mass induced by dependency links ℰ s \mathcal{E}_{s} :

[74] table: 𝖽𝖾𝗉 ⁡ ( q k ) ≜ ∑ ( q k , q j ) ∈ ℰ s 𝖿𝗋𝖾𝗊 ⁡ ( q j ) . {\mathsf{dep}}(q_{k})\;\triangleq\;\sum_{(q_{k},q_{j})\in\mathcal{E}_{s}}{\mathsf{freq}}(q_{j}).

[75] p: Intuitively, 𝖽𝖾𝗉 ⁡ ( q k ) {\mathsf{dep}}(q_{k}) aggregates the request mass of downstream queries that rely on q k q_{k} through ℰ s \mathcal{E}_{s} . Therefore, evicting q k q_{k} can trigger additional misses on every future access to those dependent queries. The following theorem formalizes this monotonic relation between eviction cost and 𝖽𝖾𝗉 ⁡ ( q k ) {\mathsf{dep}}(q_{k}) .

[76] h6: Theorem 3.

[77] p: Within a topic, evicting a query q k q_{k} increases the long-run miss probability by an amount that is monotonically increasing in 𝖽𝖾𝗉 ⁡ ( q k ) {\mathsf{dep}}(q_{k}) .

[78] p: Proof sketch: Under the dependency links ℰ s \mathcal{E}_{s} , any downstream query q j q_{j} with ( q k , q j ) ∈ ℰ s (q_{k},q_{j})\in\mathcal{E}_{s} treats q k q_{k} as a dependency context anchor. When q k q_{k} is absent, each request to such q j q_{j} incurs an extra miss attributable to the absence of q k q_{k} , so the incremental miss cost scales with the aggregate downstream request mass. Since 𝖽𝖾𝗉 ⁡ ( q k ) = ∑ ( q k , q j ) ∈ ℰ s 𝖿𝗋𝖾𝗊 ⁡ ( q j ) {\mathsf{dep}}(q_{k})=\sum_{(q_{k},q_{j})\in\mathcal{E}_{s}}{\mathsf{freq}}(q_{j}) explicitly aggregates this mass, the miss increase is monotone in 𝖽𝖾𝗉 ⁡ ( q k ) {\mathsf{dep}}(q_{k}) . A complete proof is provided in Appendix 7 .

[79] p: To make the structure-induced miss cost usable in an online policy, we need an online mechanism to maintain the dependency-link set ℰ s \mathcal{E}_{s} and hence the structural term 𝖽𝖾𝗉 ⁡ ( ⋅ ) {\mathsf{dep}}(\cdot) in Definition 2 .

[80] p: Lightweight dependency link detector. To maintain ℰ s \mathcal{E}_{s} online, we attach each incoming query q t q_{t} to at most one dependency parent q p q_{p} within the current topic episode. If such a parent exists, we add a directed link ( q p , q t ) (q_{p},q_{t}) to ℰ s \mathcal{E}_{s} . This one-parent design enables constant-time updates of the structural term 𝖽𝖾𝗉 ⁡ ( ⋅ ) {\mathsf{dep}}(\cdot) in Definition 2 . Intuitively, the dependency parent should satisfy the requirements that it is (1) recent enough to reflect the local conversational context, and (2) semantically related to q t q_{t} , so that q t q_{t} is likely to reuse its information. Accordingly, DetectParent selects the parent from a small set of recent resident predecessors. Specifically, it scans only cached candidates q k ∈ 𝒞 q_{k}\in{\mathcal{C}} within a look-back window t − k ≤ T t-k\leq T and with 𝗌𝗂𝗆 ⁡ ( q k , q t ) ≥ τ {\mathsf{sim}}(q_{k},q_{t})\geq\tau .

[81] p: We impose the look-back window T T and restrict candidates to resident entries for three reasons. (1) Dependencies inside an episode are typically local in time, so very old queries are unlikely to supply the context that q t q_{t} reuses. (2) A bounded window limits the candidate set and keeps the per-request detection cost stable. (3) The parent is meant to be an in-cache context anchor; if a candidate is not currently in 𝒞 {\mathcal{C}} , linking q t q_{t} to it neither improves hit probability nor yields a maintainable anchor state for downstream queries.

[82] p: Therefore, for each candidate q k ∈ 𝒞 q_{k}\in{\mathcal{C}} , we compute

[83] table: 𝗌𝖼𝗈𝗋𝖾 ⁡ ( k , t ) = 1 t − k ⋅ 𝗌𝗂𝗆 ⁡ ( q k , q t ) . {\mathsf{score}}(k,t)=\frac{1}{t-k}\cdot{\mathsf{sim}}(q_{k},q_{t}).

[84] p: This score combines: (1) a recency discount 1 t − k \frac{1}{t-k} , and (2) semantic similarity 𝗌𝗂𝗆 ⁡ ( q k , q t ) {\mathsf{sim}}(q_{k},q_{t}) . Finally, DetectParent returns the Top- 1 1 candidate under 𝗌𝖼𝗈𝗋𝖾 ⁡ ( k , t ) {\mathsf{score}}(k,t) and returns ∅ \emptyset if no candidate survives the filters. The result is cached as 𝗉𝖺𝗋 ⁡ ( q t ) {\mathsf{par}}(q_{t}) for future accesses.

[85] figure: Algorithm 3 Constant-time 𝖳𝖲𝖨 {\mathsf{TSI}} Update Input: incoming request q t q_{t} ; cache 𝒞 {\mathcal{C}} ; current time step t t ; look-back window T T ; similarity threshold τ \tau ; weight λ \lambda Data: entry states 𝖿𝗋𝖾𝗊 ⁡ ( ⋅ ) {\mathsf{freq}}(\cdot) , 𝖽𝖾𝗉 ⁡ ( ⋅ ) {\mathsf{dep}}(\cdot) , 𝖳𝖲𝖨 ⁡ ( ⋅ ) {\mathsf{TSI}}(\cdot) , and a cached parent pointer 𝗉𝖺𝗋 ⁡ ( ⋅ ) {\mathsf{par}}(\cdot) for each cached query Output: updated 𝖳𝖲𝖨 {\mathsf{TSI}} scores for q t q_{t} and its dependency parent q p q_{p} (if any) 1 Procedure UpdateTSI ( q t , 𝒞 , t q_{t},{\mathcal{C}},t ) 2 𝖿𝗋𝖾𝗊 ⁡ ( q t ) ← 𝖿𝗋𝖾𝗊 ⁡ ( q t ) + 1 {\mathsf{freq}}(q_{t})\leftarrow{\mathsf{freq}}(q_{t})+1 ; 3 𝖳𝖲𝖨 ⁡ ( q t ) ← 𝖿𝗋𝖾𝗊 ⁡ ( q t ) + λ ⋅ 𝖽𝖾𝗉 ⁡ ( q t ) {\mathsf{TSI}}(q_{t})\leftarrow{\mathsf{freq}}(q_{t})+\lambda\cdot{\mathsf{dep}}(q_{t}) ; 4 if 𝗉𝖺𝗋 ⁡ ( q t ) ≠ ∅ {\mathsf{par}}(q_{t})\neq\emptyset then 5 q p ← 𝗉𝖺𝗋 ⁡ ( q t ) q_{p}\leftarrow{\mathsf{par}}(q_{t}) ; 6 𝗇𝖾𝗐 ← 0 {\mathsf{new}}\leftarrow 0 ; 7 else 8 q p ← DetectParent ​ ( q t , 𝒞 , t , T , τ ) q_{p}\leftarrow\textsc{DetectParent}(q_{t},{\mathcal{C}},t,T,\tau) ; 9 𝗉𝖺𝗋 ⁡ ( q t ) ← q p {\mathsf{par}}(q_{t})\leftarrow q_{p} ; 10 𝗇𝖾𝗐 ← 1 {\mathsf{new}}\leftarrow 1 ; 11 if q p ≠ ∅ q_{p}\neq\emptyset and q p ∈ 𝒞 q_{p}\in{\mathcal{C}} then 12 if 𝗇𝖾𝗐 = 1 {\mathsf{new}}=1 then 13 𝖽𝖾𝗉 ⁡ ( q p ) ← 𝖽𝖾𝗉 ⁡ ( q p ) + 𝖿𝗋𝖾𝗊 ⁡ ( q t ) {\mathsf{dep}}(q_{p})\leftarrow{\mathsf{dep}}(q_{p})+{\mathsf{freq}}(q_{t}) ; 14 else 15 𝖽𝖾𝗉 ⁡ ( q p ) ← 𝖽𝖾𝗉 ⁡ ( q p ) + 1 {\mathsf{dep}}(q_{p})\leftarrow{\mathsf{dep}}(q_{p})+1 ; 16 𝖳𝖲𝖨 ⁡ ( q p ) ← 𝖿𝗋𝖾𝗊 ⁡ ( q p ) + λ ⋅ 𝖽𝖾𝗉 ⁡ ( q p ) {\mathsf{TSI}}(q_{p})\leftarrow{\mathsf{freq}}(q_{p})+\lambda\cdot{\mathsf{dep}}(q_{p}) ; 17 return 𝖳𝖲𝖨 ⁡ ( q t ) {\mathsf{TSI}}(q_{t}) and 𝖳𝖲𝖨 ⁡ ( q p ) {\mathsf{TSI}}(q_{p}) ;

[86] p: Online 𝖳𝖲𝖨 {\mathsf{TSI}} maintenance. Equipped with the dependency detector and cached parents, each access to q t q_{t} triggers a constant-time update cascade: (1) increment 𝖿𝗋𝖾𝗊 ⁡ ( q t ) {\mathsf{freq}}(q_{t}) and recompute 𝖳𝖲𝖨 ⁡ ( q t ) {\mathsf{TSI}}(q_{t}) ; (2) if 𝗉𝖺𝗋 ⁡ ( q t ) = ∅ {\mathsf{par}}(q_{t})=\emptyset , run DetectParent to assign a parent (otherwise reuse the cached parent); (3) if q p ∈ 𝒞 q_{p}\in{\mathcal{C}} , update 𝖽𝖾𝗉 ⁡ ( q p ) {\mathsf{dep}}(q_{p}) and 𝖳𝖲𝖨 ⁡ ( q p ) {\mathsf{TSI}}(q_{p}) using Algorithm 3 .

[87] h2: 4. Evaluation

[88] h3: 4.1. Evaluation Questions

[89] p: The goal of our evaluation is twofold: to validate RAC in scenarios where standard policies fail, and to verify the effectiveness of our relation-aware signals and unified heuristic. We design our experiments to answer the following research questions:

[90] p: Q1 Robustness under sparse recurrence. ( 4.3 ) On workloads with long reuse distances and sparse local recurrence, does RAC maintain stable gains by leveraging relation-aware signals, whereas recency-/frequency-driven policies become unreliable?

[91] p: Q2 Effectiveness on real-world traces.( 4.3 ) On timestamp-continuous 𝖫𝖫𝖬 \mathsf{LLM} dialogue traces from real datasets, how does RAC compare with state-of-the-art eviction policies under identical semantic hit semantics?

[92] p: Q3 Ablation on components.( 4.4 ) Under identical cache budgets and hit semantics, what is the marginal contribution of (A) Topical Prevalence (TP) and (B) Topic Structural Importance (TSI) to RAC’s performance gains?

[93] p: Q4 Parameter impact and robustness.( 4.5 ) How do key hyperparameters in RAC affect cache hit rate and latency, and how stable is RAC across a wide parameter range?

[94] figure: (a) Simulated sequences varying long reuse-distance ratio (b) Simulated sequences varying long-tail coefficient Figure 2 . Hit ratio on simulated sequences under two stress axes: (a) varying long reuse-distance ratio; (b) varying long-tail coefficient.

[95] figure: (a) True trace at 2.5% capacity (b) True trace at 10% capacity (c) True trace at 20% capacity Figure 3 . Normalized hit ratio on timestamp-continuous OASST1 sub-traces under different cache capacities.

[96] h3: 4.2. Evaluation Setup

[97] p: Workloads. We utilize both real-world logs and synthetically constructed traces to evaluate performance across varying degrees of locality and contention.

[98] p: Real traces (OASST1). To answer RQ2 , we extract traces from OASST1, a publicly available human-assistant dialogue corpus collected by the OpenAssistant project and released with conversation-thread structure and message-level metadata. OASST1 provides chronological timestamps and conversation-thread structure, which enables constructing timestamp-continuous traces without splitting or interleaving threads. We extract 10 non-overlapping, timestamp-continuous sub-traces , each containing 10,000 dialogue requests. All policies process the same request sequence under identical semantic hit semantics for a fair comparison.

[99] p: Synthetic traces. To address RQ1 by overcoming the limited structural diversity of real traces, we construct synthetic traces that, under tight cache budgets, induce workload regimes where recency and frequency become weak reuse predictors, and thus stress-test whether RAC sustains gains when short-window policies fail. We adopt a topic-level semi-Markov generator: each trace concatenates variable-length topic episodes, where each episode is a complete multi-turn session that is never split or interleaved; hence topic switches occur only at session boundaries.

[100] p: We sample N = 120 N=120 topics and maintain a session pool, expanding each topic to ∼ \sim 40 complete sessions (original + generated variants) using ChatGPT. Within each topic, sessions exhibit context-ordered dependencies that can be abstracted as a DAG; we preserve this property in generated variants while enriching structural diversity by extending dependency branches with consistent continuations.

[101] p: We fix cache capacity to C = 1000 C{=}1000 and trace length to 10,000 10{,}000 requests. We conduct controlled sweeps along two workload axes, generating 20 independent traces per setting :

[102] p: Reuse-distance axis. We call a reuse long if its reuse distance exceeds the cache capacity C C . The long-reuse ratio is the fraction of reuse events in a trace that are long under this definition. Fixing γ = 0.7 \gamma{=}0.7 , we vary the long-reuse ratio from 50% to 90% (step 10%) by repeating prior sessions and placing repeats at randomized positions.

[103] p: Long-tail skew axis. We fix the long-reuse ratio at 50% and vary the Zipf exponent γ ∈ { 0.7 , 0.8 , … , 1.2 } \gamma\in\{0.7,0.8,\ldots,1.2\} , which controls how concentrated the topic popularity is (smaller γ \gamma yields a flatter distribution, while larger γ \gamma yields a heavier head and a longer tail). This range is consistent with empirical observations that query frequencies in real logs follow heavy-tailed Zipf/power-law-like distributions ( Petersen et al., 2016 ; Lillo and Ruggieri, 2021 ) .

[104] p: Metrics(Normalized Hit Ratio H ​ R norm HR_{\text{norm}} ). Let H ​ R algo ​ ( C ) HR_{\text{algo}}(C) be the hit ratio of an eviction policy under cache capacity C C on the given request sequence (with the same hit semantics). Let H ​ R full HR_{\text{full}} be the hit ratio of an infinite cache on the same sequence, i.e., the upper bound when no evictions occur. We report

[105] table: H ​ R norm ​ ( C ) = H ​ R algo ​ ( C ) H ​ R full . HR_{\text{norm}}(C)\;=\;\frac{HR_{\text{algo}}(C)}{HR_{\text{full}}}.

[106] p: This normalization controls for dataset-dependent hit ceilings and highlights the effect of the eviction policy.

[107] p: Capacity Configuration. We report cache capacity as a fraction of the total unique request footprint in each trace (e.g., C ∈ { 50 , … , 400 } C\in\{50,\ldots,400\} for OASST1), covering the cache-cliff to moderately provisioned regimes. For RQ1 (synthetic), we fix capacity at 10% ; for RQ2 (real), we evaluate 2.5% , 10% , and 20% ; and for RQ3 (ablation), we sweep 2.5%–20% with a 2.5% step.

[108] p: Methods and baselines. We evaluate RAC against representative eviction policies under identical hit semantics and cache budgets.

[109] p: Our methods: RAC (full; TP+TSI), RAC w/o TP (TSI only), and RAC w/o TSI (TP only). The ablations isolate each component’s marginal contribution ( RQ3 ).

[110] p: External baselines:

[111] p: Classic heuristics: FIFO , LRU , CLOCK , TTL . LRU is a common production default (including KV caches).

[112] p: Frequency-/scan-resistant: TinyLFU , ARC , S3-FIFO , SIEVE , 2Q . These policies mitigate scans but do not model semantic relations.

[113] p: Learning-based: LHD , LeCaR , which adapt online using observed access outcomes.

[114] p: Implementation Details.

[115] p: Implementation Details. Unless otherwise specified, RAC uses Top-1 vector retrieval with a topic-routing (hit) threshold τ = 0.85 \tau=0.85 , a conservative value calibrated to match ChatGPT-judged semantic equivalence. We maintain relation evidence with an edge-pruning threshold τ edge = 0.6 \tau_{\text{edge}}=0.6 and decay factor λ = 1 \lambda=1 . For synthetic workloads, unless a stress axis is being swept, we fix the Zipf exponent to γ = 0.7 \gamma=0.7 and set the long-reuse fraction to 50%, where an event is counted as long reuse if its reuse distance exceeds the cache capacity C C . To answer RQ4 , we further vary these hyperparameters and report their sensitivity in § 4.5 .

[116] figure: (a) Performance vs. capacity (b) Marginal gains ( Δ \Delta TP, Δ \Delta TIC) Figure 4 . Ablation results under varying cache capacities.

[117] h3: 4.3. Main Results

[118] p: We evaluate RAC under the unified simulator and the semantic hit semantics defined in § 4.2 . For RQ1 , we conduct controlled stress tests on synthetic traces along the reuse-distance and popularity-skew dimensions (Figure 2 ). For RQ2 , we evaluate on timestamp-continuous OASST1 sub-traces under multiple cache capacities (Figure 3 ).

[119] p: RQ1 (Robustness under sparse recurrence). Figure 2 presents the hit ratios on simulated traces. Impact of Reuse Distance (a): RAC consistently ranks first, and its advantage widens as the workload becomes increasingly adversarial to short-window statistics. As reuse shifts beyond the cache horizon, the recency and frequency signals relied upon by conventional policies weaken substantially. Consequently, baselines deteriorate, whereas RAC degrades much more slowly, yielding a widening performance gap under stronger contention. Quantitatively, compared with the strongest baseline, RAC achieves double-digit relative gains under mild contention, growing to tens of percent in the most challenging regimes. Relative to the baseline average, these gains are even more pronounced. These trends indicate that RAC remains robust precisely when sparse recurrence renders local hit statistics unreliable.

[120] p: Impact of Popularity Skew (b): While all methods generally improve as popularity concentrates on a smaller head set of topics, RAC maintains superiority across the entire tail-to-head spectrum. RAC outperforms the strongest baseline by roughly 15%–20% consistently, and exceeds the baseline average by an even larger margin (typically tens of percent ). This suggests that RAC not only benefits from frequency concentration but also extracts additional value within head topics by preserving structurally critical context anchors (TIC), thereby capturing semantic hits that queue- or sketch-based policies miss.

[121] p: RQ2 (Effectiveness on real-world traces). Figure 3 reports performance on timestamp-continuous OASST1 sub-traces, spanning capacities from the cache-cliff to moderately provisioned regimes. RAC achieves the best overall effectiveness under identical hit semantics across all evaluated capacities. Specifically, RAC improves over the strongest baseline by around 5%–12% , and over the baseline average by a larger margin (often well above 10% , especially under tighter budgets). These results confirm that RAC’s relation-aware design generalizes beyond controlled simulations to real dialogue workloads, where irregular topic shifts and heavy-tailed reuse distances often invalidate short-window statistics. By aggregating topic-level evidence (TP) and prioritizing structurally critical context anchors (TIC), RAC delivers stable improvements without altering the hit predicate.

[122] h3: 4.4. Ablation Study (RQ3)

[123] p: To address RQ3 , we isolate the contributions of RAC’s two relation-aware signals by comparing the full model with two ablated variants: (i) RAC w/o TP , which removes topic-level evidence aggregation (topical prevalence); and (ii) RAC w/o TIC , which removes intra-topic dependency aggregation. Figure 4 reports normalized hit ratios and the corresponding marginal gains.

[124] p: Figure 4 (a) shows that full RAC consistently outperforms both ablations across all cache sizes, indicating that TP and TIC are complementary: removing either component yields substantial degradation. Figure 4 (b) further reveals their distinct roles across the capacity spectrum. In the cache-cliff regime (tight budgets), removing TIC causes the sharpest drop, highlighting the importance of preserving within-topic context anchors when capacity is scarce. As capacity increases, the marginal benefit of TIC diminishes naturally because larger caches retain such anchors by default.

[125] p: In contrast, TP contributes persistently across all capacities. Removing TP induces steady degradation even at larger budgets, suggesting that topic-level aggregation remains crucial for long-horizon revisits and irregular topic transitions where local statistics remain sparse. Overall, RAC’s gains arise from the synergy between TP (long-horizon topical awareness) and TIC (intra-topic discrimination), ensuring robust effectiveness across diverse budgets.

[126] figure: (a) Decay coefficient α \alpha (b) Weight λ \lambda (c) Threshold τ \tau Figure 5 . RQ4: Parameter sensitivity at 10% cache capacity.

[127] h3: 4.5. Parameter Sensitivity (RQ4)

[128] p: To answer RQ4 , Figure 5 reports RAC’s sensitivity to three key hyperparameters at 10% cache capacity: routing threshold τ \tau , decay factor α \alpha , and structural weight λ \lambda . Overall, RAC exhibits a broad region of stable performance: once a parameter enters a reasonable operating range, performance becomes relatively insensitive to moderate changes. This indicates that RAC does not rely on delicate tuning to achieve strong effectiveness.

[129] p: Routing threshold τ \tau . As shown in Figure 5 (right), an overly small τ \tau makes routing permissive, admitting noisy matches that dilute effective reuse. Increasing τ \tau into a reasonable semantic-matching range improves effectiveness substantially before saturating; further increasing τ \tau yields limited gains and may slightly reduce reuse by becoming overly strict. This supports the use of a strict semantic gate while demonstrating stability within a sensible band.

[130] p: Decay factor α \alpha . Regarding temporal aggregation (Figure 5 , left), when α \alpha is too small, topic evidence decays slowly and can overweight stale history; increasing α \alpha improves effectiveness by discounting older evidence appropriately. However, when α \alpha becomes overly large, evidence is discounted too aggressively, making decisions more reactive to short-term fluctuations and slightly degrading performance. The curve is smooth with a wide near-optimal region, indicating robustness to α \alpha .

[131] p: Structural weight λ \lambda . Regarding the TP–TIC trade-off (Figure 5 , middle), small λ \lambda underutilizes dependency signals, whereas excessively large λ \lambda overemphasizes structure at the expense of topical prevalence. The best performance occurs in a moderate-to-high band and remains close to optimal over a broad interval, consistent with our default setting. Taken together, these results show that each parameter has an interpretable effect and that RAC maintains stable performance over wide ranges.

[132] h3: 4.6. Evaluation Summary

[133] p: For Q1 (Robustness under sparse recurrence): RAC is robust when local hit statistics become uninformative under sparse recurrence, sustaining stable advantages by relying on relation-aware evidence rather than short-window recency/frequency signals.

[134] p: For Q2 (Effectiveness on real-world traces): RAC generalizes to timestamp-continuous real dialogue traces and remains effective under identical hit semantics, indicating that its gains are not an artifact of synthetic construction.

[135] p: For Q3 (Ablation on components): TP and TSI play complementary roles: TP captures reuse regularities via topic-level aggregation (beyond independent items), while TSI enables efficient within-topic discrimination of reuse value, which stabilizes performance under heavy-tailed popularity.

[136] p: For Q4 (Parameter impact and robustness): RAC is insensitive to moderate hyperparameter perturbations within a wide operating region, suggesting that its effectiveness does not depend on delicate tuning.

[137] h2: 5. Related Work

[138] p: We review prior work from two perspectives: reusing computed content in 𝖫𝖫𝖬 \mathsf{LLM} serving, and cache eviction under limited capacity.

[139] p: Reuse of computed content in 𝖫𝖫𝖬 \mathsf{LLM} serving. Focusing on caching inference artifacts to skip recomputation, our method supports both semantic matching and compositional chunking .

[140] p: Semantic caches. Focusing on reusing final generations via similarity, GPTCache employs embedding lookup ( Bang, 2023 ) , MeanCache leverages cluster representatives ( Gill and others, 2024 ) , and ScaLM optimizes for scalable serving constraints ( Li et al., 2024 ) .

[141] p: Compositional 𝖢𝗁𝗎𝗇𝗄𝖪𝖵 \mathsf{ChunkKV} reuse. Targeting intermediate 𝖢𝗁𝗎𝗇𝗄𝖪𝖵 \mathsf{ChunkKV} reuse, PromptCache and CacheBlend enable modular reuse via structural compatibility ( Gim et al., 2024 ) and component blending ( Yao et al., 2025 ) . RAGCache and Cache-Craft optimize management via hierarchical policies ( Jin et al., 2024 ) and composability-based retention ( Agarwal et al., 2025 ) , respectively, while KVCache in the Wild characterizes production-level memory pressure ( Wang et al., 2025 ) .

[142] p: Eviction algorithms under limited capacity. Eviction policies use lightweight metadata to prioritize cached items and select victims under capacity pressure.

[143] p: Simple heuristics. These policies use deterministic metrics for ranking. Belady’s MIN establishes the offline optimum ( Belady, 1966 ; Mattson et al., 1970b ) , while LRU/FIFO implement constant-overhead tail eviction ( Corbató, 1969 ; Sleator and Tarjan, 1985 ) . Similarity caching groups items via modified hit semantics ( Neglia et al., 2022 ; Sabnis et al., 2021 ) . GDS/GDSF and LRFU unify size, cost, and frequency into tunable priority scores ( Cao and Irani, 1997 ; Cherkasova and Ciardo, 1998 ; Lee and others, 2001 ) .

[144] p: Composite-structure heuristics. These designs employ multi-level queues or auxiliary structures to refine value estimation. 2Q, ARC/CAR, and TinyLFU filter one-timers and churn via probationary queues or sketches ( Johnson and Shasha, 1994 ; Megiddo and Modha, 2003b ; Einziger et al., 2017 ) . S3-FIFO and Sieve offer high-performance demotion rules with minimal metadata ( Liu et al., 2023 ; Zhang et al., 2023b ) . LRU- k k and LIRS/LIRS2 utilize reuse distance to separate persistent items from transients ( O’Neil et al., 1993 ; Jiang and Zhang, 2002 ; Zhong et al., 2021 ) . In 𝖫𝖫𝖬 \mathsf{LLM} runtimes, SGLang manages 𝖪𝖵 \mathsf{KV} states via radix trees; however, its eviction remains LRU-like and is primarily constrained by parent–child dependencies to preserve structural validity ( Zheng et al., 2024 ) .

[145] p: Learning-based eviction. Learning-guided policies approximate utility via data-driven signals. Hawkeye and Glider learn cache-friendliness from OPT-derived supervision ( Jain and Lin, 2016 ; Shi et al., 2019 ) . LRB/HALP and ILCache map features to priorities approximating reuse distance ( Song and others, 2020 ; Song and others, 2023 ; Liu et al., 2020 ) , while LeCaR and CACHEUS adaptively weight experts via online feedback ( Vietri et al., 2018a ; Rodriguez et al., 2021b ) . DRLCache and its variants further model replacement as a sequential process via reinforcement learning ( Zhong et al., 2017 ; Zhou et al., 2022 ) .

[146] p: This work differs from previous approaches in three key aspects: (1) unlike simple heuristics , we estimate value from semantic associations and structural dependencies rather than isolated hit statistics; (2) unlike composite heuristics , we use query relations to identify and preserve critical context anchors instead of auxiliary admission/filtering structures; and (3) unlike prior learning-based policies , we adopt a lightweight, interpretable online rule that adapts to structural shifts without training or inference overhead.

[147] h2: 6. Conclusion

[148] p: We present Relation-Aware Cache ( 𝖱𝖠𝖢 \mathsf{RAC} ), an online cache replacement strategy tailored for dynamic 𝖫𝖫𝖬 \mathsf{LLM} workloads. Based on the insight that reuse is governed by discourse structure, 𝖱𝖠𝖢 \mathsf{RAC} substitutes isolated item signals with more stable topic-level frequency and recency, and utilizes Structural Importance to identify critical dependency anchors, thereby minimizing miss rates caused by sparse recurrence. We evaluate 𝖱𝖠𝖢 \mathsf{RAC} on both real-world dialogue traces and synthetic benchmarks. Experimental results demonstrate that 𝖱𝖠𝖢 \mathsf{RAC} outperforms state-of-the-art baselines by 20% in hit ratio, validating that exploiting relation-aware signals is key to efficient memory management in long-context serving.

[149] h2: References

[150] h2: 7. Complete Proof for Theorem 3 and Extensions

[151] p: This appendix provides the complete proof for Theorem 3 in the main text, which formalizes the monotone relation between the eviction-induced miss increase and the downstream dependency mass 𝖽𝖾𝗉 ⁡ ( ⋅ ) {\mathsf{dep}}(\cdot) . We then outline an extension that connects dependency-DAG structure to a principled notion of structural-importance ranking.

[152] h3: 7.1. Complete Proof of Theorem 3

[153] p: Setup and prerequisite semantics. Fix a topic s s and its dependency links ℰ s \mathcal{E}_{s} . Consider the in-topic request sequence { Q t } t = 1 T \{Q_{t}\}_{t=1}^{T} , where Q t Q_{t} denotes the realized query at time t t . We interpret each edge ( q k , q j ) ∈ ℰ s (q_{k},q_{j})\in\mathcal{E}_{s} as a prerequisite relation: q k q_{k} is a context anchor required by q j q_{j} within the topic. Accordingly, if q k q_{k} is absent from the cache when serving a request to such a dependent query q j q_{j} , then the request to q j q_{j} incurs at least one additional miss that is attributable to the absence of q k q_{k} (independent of how other entries are arranged). This defines a conservative, unavoidable miss semantics: we only charge misses that must occur due to the missing prerequisite anchor.

[154] p: Unavoidable miss lower bound induced by evicting q k q_{k} . Let 𝒩 ⁡ ( q k ) ≜ { q j : ( q k , q j ) ∈ ℰ s } \mathcal{N}(q_{k})\triangleq\{q_{j}:(q_{k},q_{j})\in\mathcal{E}_{s}\} denote the set of one-hop dependents of q k q_{k} . We define, over a horizon T T , the number of unavoidable additional misses induced by the absence of q k q_{k} as

[155] table: (2) Δ T ( q k ) ≜ ∑ t = 1 T 𝟙 { Q t ∈ 𝒩 ( q k ) } . \Delta_{T}(q_{k})\;\triangleq\;\sum_{t=1}^{T}\mathbbm{1}\{Q_{t}\in\mathcal{N}(q_{k})\}.

[156] p: That is, Δ T ​ ( q k ) \Delta_{T}(q_{k}) counts how many requests in the horizon target dependent queries of q k q_{k} . Under the prerequisite semantics, if q k q_{k} is evicted (and thus missing whenever these dependent requests arrive), then each of these requests must incur at least one extra miss attributable to the missing anchor.

[157] p: Proof: [Proof of Theorem 3 ] Fix topic s s and an anchor query q k q_{k} . Consider any time step t ∈ { 1 , … , T } t\in\{1,\ldots,T\} .

[158] p: If Q t ∉ 𝒩 ⁡ ( q k ) Q_{t}\notin\mathcal{N}(q_{k}) , then by definition there is no edge ( q k , Q t ) ∈ ℰ s (q_{k},Q_{t})\in\mathcal{E}_{s} , and the prerequisite semantics imposes no additional miss that is attributable to the absence of q k q_{k} for serving Q t Q_{t} . Thus, the absence of q k q_{k} does not force an extra miss at time t t .

[159] p: If Q t ∈ 𝒩 ⁡ ( q k ) Q_{t}\in\mathcal{N}(q_{k}) , then there exists a dependent query q j q_{j} such that Q t = q j Q_{t}=q_{j} and ( q k , q j ) ∈ ℰ s (q_{k},q_{j})\in\mathcal{E}_{s} . By the prerequisite semantics, whenever q k q_{k} is absent, serving this request to q j q_{j} must incur at least one additional miss attributable to the missing anchor q k q_{k} . Therefore, for each such time step t t , the eviction of q k q_{k} contributes at least one unit to the eviction-induced miss increase.

[160] p: Summing these unavoidable contributions over t = 1 t=1 to T T , we conclude that over any horizon T T , the cumulative miss increase attributable to evicting q k q_{k} is lower bounded by the number of dependent-query requests within the horizon, namely Δ T ​ ( q k ) \Delta_{T}(q_{k}) in ( 2 ). Equivalently, the eviction-induced miss increase is monotonically increasing in Δ T ​ ( q k ) \Delta_{T}(q_{k}) .

[161] p: We now connect this lower bound to the online statistic 𝖽𝖾𝗉 ⁡ ( q k ) {\mathsf{dep}}(q_{k}) . Recall the definition

[162] table: 𝖽𝖾𝗉 ⁡ ( q k ) ≜ ∑ ( q k , q j ) ∈ ℰ s 𝖿𝗋𝖾𝗊 ⁡ ( q j ) , {\mathsf{dep}}(q_{k})\;\triangleq\;\sum_{(q_{k},q_{j})\in\mathcal{E}_{s}}{\mathsf{freq}}(q_{j}),

[163] p: where 𝖿𝗋𝖾𝗊 ⁡ ( q j ) {\mathsf{freq}}(q_{j}) is the observed hit/request mass of q j q_{j} within topic s s over the same measurement horizon. Since 𝖽𝖾𝗉 ⁡ ( q k ) {\mathsf{dep}}(q_{k}) aggregates the downstream mass over exactly the dependent set 𝒩 ⁡ ( q k ) \mathcal{N}(q_{k}) , it is a direct empirical proxy for how frequently requests fall into 𝒩 ⁡ ( q k ) \mathcal{N}(q_{k}) , i.e., for Δ T ​ ( q k ) \Delta_{T}(q_{k}) up to a common scaling determined by the horizon and counting convention. Hence, the eviction-induced miss increase (via its unavoidable lower bound) is monotonically increasing in 𝖽𝖾𝗉 ⁡ ( q k ) {\mathsf{dep}}(q_{k}) . □ \Box

[164] h3: 7.2. Extension: Structural-Importance Ranking on a Dependency DAG

[165] p: Theorem 3 motivates a first-order proxy that aggregates direct dependents. Within a topic, prerequisite relations form a directed acyclic graph (DAG), and the eviction externality of an anchor can be shaped by the global dependency structure rather than only its one-hop neighborhood. To obtain a lightweight structural ordering beyond one-hop counts, we adopt a PageRank/TextRank-style graph-based ranking, which assigns vertex importance via the stationary distribution of a random walk on a directed graph ( Page et al., 1998 ; Mihalcea and Tarau, 2004 ; Erkan and Radev, 2004 ) .

[166] p: Reverse-edge construction. Fix a topic and let G = ( V , E ) G=(V,E) denote its prerequisite DAG, where each node v ∈ V v\in V is a query (cache entry) in the topic, and each directed edge ( u → v ) ∈ E (u\!\to\!v)\in E indicates that u u is a prerequisite context anchor for v v . To rank anchors, we propagate importance from dependents back to prerequisites. Concretely, we run the ranking walk on the reversed edges: for each prerequisite link ( u → v ) ∈ E (u\!\to\!v)\in E , we use a reversed link ( v → u ) (v\!\to\!u) in the walk.

[167] p: Random walk with uniform restart. Let Out ⁡ ( v ) ≜ { u ∈ V : ( v → u ) ∈ E } \mathrm{Out}(v)\triangleq\{u\in V:\ (v\!\to\!u)\in E\} denote the outgoing neighbors of v v in the reversed graph. We define a random walk over V V with damping parameter β ∈ ( 0 , 1 ) \beta\in(0,1) : with probability β \beta , the walk follows a reversed edge chosen uniformly from Out ⁡ ( v ) \mathrm{Out}(v) ; with probability 1 − β 1-\beta , it restarts to a uniformly random node in V V . For dangling nodes ( | Out ⁡ ( v ) | = 0 |\mathrm{Out}(v)|=0 ), we fall back to a uniform jump. Formally, the transition probability is

[168] table: P ⁡ ( u ∣ v ) ≜ { 1 | Out ⁡ ( v ) | , u ∈ Out ⁡ ( v ) ​ and | Out ⁡ ( v ) | > 0 , 1 | V | , | Out ⁡ ( v ) | = 0 , 0 , otherwise . P(u\mid v)\;\triangleq\;\begin{cases}\frac{1}{|\mathrm{Out}(v)|},&u\in\mathrm{Out}(v)\ \text{and}\ |\mathrm{Out}(v)|>0,\\[4.0pt] \frac{1}{|V|},&|\mathrm{Out}(v)|=0,\\[4.0pt] 0,&\text{otherwise}.\end{cases}

[169] p: We define the structural-importance score r : V → ℝ ≥ 0 r:V\to\mathbb{R}_{\geq 0} as the stationary distribution of this Markov chain, i.e., the unique solution to

[170] table: (3) r ( u ) = ( 1 − β ) ⋅ 1 | V | + β ∑ v : ( v → u ) ∈ E P ( u ∣ v ) r ( v ) . r(u)\;=\;(1-\beta)\cdot\frac{1}{|V|}\;+\;\beta\sum_{v:\ (v\to u)\in E}P(u\mid v)\,r(v).

[171] h6: Proposition 1 (Existence, uniqueness, and computability).

[172] p: For any β ∈ ( 0 , 1 ) \beta\in(0,1) , the uniform-restart walk is irreducible and aperiodic. Hence the stationary distribution in ( 3 ) exists and is unique. Moreover, it can be computed by power iteration: starting from any distribution r ( 0 ) r^{(0)} over V V , repeatedly applying the update in ( 3 ) yields a sequence { r ( t ) } \{r^{(t)}\} that converges to r r .

[173] p: Centrality induced by dependency structure. The score r ⁡ ( u ) r(u) is the long-run visit probability of the random-surfer walk on the reversed dependency graph ( Page et al., 1998 ) . As in TextRank/LexRank, a node becomes important if it is pointed to by other important nodes, yielding an eigenvector-centrality-like notion of salience that reflects the global link structure ( Mihalcea and Tarau, 2004 ; Erkan and Radev, 2004 ) . In our setting, this means a prerequisite anchor receives higher importance when it is a structurally central dependency target of many downstream queries, especially when those downstream queries themselves occupy central positions in the workflow.

[174] p: A path-sum view (global dependency influence). Equation ( 3 ) admits a standard expansion that makes the propagation effect explicit. Let u u denote the uniform distribution over V V , i.e., u ⁡ ( v ) = 1 / | V | u(v)=1/|V| . In vector form, ( 3 ) can be written as

[175] table: r = ( 1 − β ) ​ u + β ​ P ⊤ ​ r , r\;=\;(1-\beta)\,u\;+\;\beta\,P^{\top}r,

[176] p: which yields

[177] table: (4) r = ( 1 − β ) ​ ∑ ℓ = 0 ∞ β ℓ ​ ( P ⊤ ) ℓ ​ u . r\;=\;(1-\beta)\sum_{\ell=0}^{\infty}\beta^{\ell}(P^{\top})^{\ell}u.

[178] p: This expansion shows that r r reflects the global dependency structure: importance is repeatedly propagated along reversed prerequisite links with geometric attenuation. As a result, anchors that are structurally central in the dependency workflow obtain higher scores.

[179] p: Why a structural term in 𝖳𝖲𝖨 {\mathsf{TSI}} is sensible under sparse recurrence. The stationary score r ⁡ ( ⋅ ) r(\cdot) induces a lightweight structural-centrality ordering from the prerequisite DAG, reflecting eviction externalities that are not captured by entry-local recency/frequency. This view is consistent with our one-hop proxy 𝖽𝖾𝗉 ⁡ ( ⋅ ) {\mathsf{dep}}(\cdot) in the main text: 𝖽𝖾𝗉 ⁡ ( q ) {\mathsf{dep}}(q) conservatively aggregates the direct dependent-side request mass attributable to an anchor, and thus provides a reasonable first-order structural signal in 𝖳𝖲𝖨 ⁡ ( ⋅ ) {\mathsf{TSI}}(\cdot) . When finer structural discrimination is desired, the propagation-based score r ⁡ ( ⋅ ) r(\cdot) can be used as an optional refinement to account for indirect support paths mediated by the dependency structure, while remaining efficiently computable by power iteration.

[180] figure: Algorithm 4 Topic Retrieval via Representative Index (ANN Shortlist + Gated Routing) Input: incoming request q t q_{t} ; threshold τ \tau ; shortlist size K K Output: routed topic id Z t Z_{t} (or ∅ \emptyset if none passes) Data: representatives { r ⁡ ( s ) } \{r(s)\} for active topics and a topic index supporting IndexQuery ( ϕ ⁡ ( q t ) , K ) (\phi(q_{t}),K) 1 𝒮 t ← IndexQuery ​ ( ϕ ⁡ ( q t ) , K ) \mathcal{S}_{t}\leftarrow\textsf{IndexQuery}(\phi(q_{t}),K) // retrieve up to K K nearest representatives 2 Z t ← ∅ Z_{t}\leftarrow\emptyset 3 foreach s ∈ 𝒮 t s\in\mathcal{S}_{t} do 4 if sim ⁡ ( ϕ ⁡ ( q t ) , r ⁡ ( s ) ) ≥ τ \mathrm{sim}(\phi(q_{t}),r(s))\geq\tau then 5 if Z t = ∅ Z_{t}=\emptyset or sim ⁡ ( ϕ ⁡ ( q t ) , r ⁡ ( s ) ) > sim ⁡ ( ϕ ⁡ ( q t ) , r ⁡ ( Z t ) ) \mathrm{sim}(\phi(q_{t}),r(s))>\mathrm{sim}(\phi(q_{t}),r(Z_{t})) then 6 Z t ← s Z_{t}\leftarrow s 7 return Z t Z_{t}

[181] h2: 8. Representative Selection and Maintenance for Topic Routing

[182] p: Topic abstraction and maintained state. We organize the cache into topics , where each active topic s s groups cached queries routed to the same topical cluster. Online, each topic maintains a compact state: (i) a member set ℳ ⁡ ( s ) \mathcal{M}(s) of resident queries currently assigned to s s ; (ii) a representative embedding r ⁡ ( s ) r(s) serving as the routing key; and (iii) per-query signals required by replacement (e.g., recency and TSI ⁡ ( ⋅ ) \mathrm{TSI}(\cdot) in Section 3.3 ). To enable sub-linear routing across topics, we additionally maintain a topic-level vector index over { r ⁡ ( s ) } \{r(s)\} that supports top- K K nearest-neighbor queries and per-topic representative updates. Topic creation/deletion is handled by the main workflow; here we focus on retrieval and on maintaining the above state consistently under online cache updates.

[183] figure: Algorithm 5 Representative and Index Maintenance (TSI-max Anchor with Lazy Refresh) Input: topic id s s ; event Insert ( q ) (q) or Evict ( q ) (q) ; optional on-demand call Refresh ( s ) (s) Output: updated r ⁡ ( s ) r(s) and the topic-index entry of s s Data: topic state { ℳ ( s ) , r ( s ) , src ( s ) ∈ ℳ ( s ) s.t. r ( s ) = ϕ ( src ( s ) ) } \{\mathcal{M}(s),\,r(s),\,\textsf{src}(s)\in\mathcal{M}(s)\ \text{s.t.}\ r(s)=\phi(\textsf{src}(s))\} ; per-query signal TSI ⁡ ( q ) \mathrm{TSI}(q) (Section 3.3 ); topic index with IndexUpdate ( s , r ⁡ ( s ) ) (s,r(s)) 1 Procedure Refresh ( s ) (s) 2 if ℳ ⁡ ( s ) = ∅ \mathcal{M}(s)=\emptyset then 3 delete topic s s from the index 4 return 5 if src ​ ( s ) = ∅ \textsf{src}(s)=\emptyset or src ​ ( s ) ∉ ℳ ​ ( s ) \textsf{src}(s)\notin\mathcal{M}(s) then 6 src ​ ( s ) ← arg ⁡ max e ∈ ℳ ⁡ ( s ) ⁡ TSI ⁡ ( q ) \textsf{src}(s)\leftarrow\arg\max_{e\in\mathcal{M}(s)}\mathrm{TSI}(q) 7 r ​ ( s ) ← ϕ ​ ( src ​ ( s ) ) r(s)\leftarrow\phi(\textsf{src}(s)) 8 IndexUpdate ( s , r ⁡ ( s ) ) (s,r(s)) 9 Procedure OnInsert ( s , q ) (s,q) 10 append q q to ℳ ⁡ ( s ) \mathcal{M}(s) 11 compute/update TSI ⁡ ( q ) \mathrm{TSI}(q) 12 if src ​ ( s ) = ∅ \textsf{src}(s)=\emptyset or TSI ​ ( q ) > TSI ​ ( src ​ ( s ) ) \mathrm{TSI}(q)>\mathrm{TSI}(\textsf{src}(s)) then 13 src ​ ( s ) ← q \textsf{src}(s)\leftarrow q 14 r ⁡ ( s ) ← ϕ ⁡ ( q ) r(s)\leftarrow\phi(q) 15 IndexUpdate ( s , r ⁡ ( s ) ) (s,r(s)) 16 Procedure OnEvict ( s , q ) (s,q) 17 remove q q from ℳ ⁡ ( s ) \mathcal{M}(s) 18 if ℳ ⁡ ( s ) = ∅ \mathcal{M}(s)=\emptyset then 19 delete topic s s from the index 20 return 21 if src ​ ( s ) = q \textsf{src}(s)=q then 22 src ​ ( s ) ← ∅ \textsf{src}(s)\leftarrow\emptyset // invalidate; refreshed lazily by Refresh

[184] p: Anchor-based representative (invariant). We adopt an anchor-based representative: at any time, r ⁡ ( s ) r(s) equals the embedding of a single resident query in ℳ ⁡ ( s ) \mathcal{M}(s) . Among current members, the anchor is chosen as a query with maximal TSI ⁡ ( ⋅ ) \mathrm{TSI}(\cdot) (Section 3.3 ), with deterministic tie-breaking (e.g., by recency or a fixed id order). This invariant avoids centroid-like summaries and yields a stable routing key under churn, while the TSI-max rule biases the anchor toward the topic core and structurally necessary context.

[185] p: Topic-level retrieval and routing (coarse stage). Given an incoming request q t q_{t} , we first use the representative index to retrieve a small candidate set of topics:

[186] table: 𝒮 t ← IndexQuery ​ ( ϕ ⁡ ( q t ) , K ) , \mathcal{S}_{t}\leftarrow\textsf{IndexQuery}(\phi(q_{t}),K),

[187] p: where IndexQuery returns up to K K topics whose representatives are nearest to ϕ ⁡ ( q t ) \phi(q_{t}) in the embedding space. We then apply a similarity gate and select the best passing candidate:

[188] table: Z t ← arg max s ∈ 𝒮 t : sim ⁡ ( ϕ ⁡ ( q t ) , r ⁡ ( s ) ) ≥ τ sim ( ϕ ( q t ) , r ( s ) ) , Z_{t}\leftarrow\arg\max_{s\in\mathcal{S}_{t}:\ \mathrm{sim}(\phi(q_{t}),r(s))\geq\tau}\ \mathrm{sim}(\phi(q_{t}),r(s)),

[189] p: and set Z t = ∅ Z_{t}=\emptyset if no candidate passes the gate. Algorithm 4 summarizes this retrieval-and-gate routine. (New-topic creation for Z t = ∅ Z_{t}=\emptyset is handled in the main workflow and is not repeated here.) This stage implements coarse-to-fine retrieval: the index constrains routing to a shortlist, while the gate preserves topic purity.

[190] p: Within-topic verification (fine stage). After routing, we decide semantic reuse by a local search restricted to the routed topic. Concretely, we find the most similar resident query within ℳ ⁡ ( Z t ) \mathcal{M}(Z_{t}) :

[191] table: q hit ← arg ⁡ max q ∈ ℳ ⁡ ( Z t ) ⁡ sim ⁡ ( ϕ ⁡ ( q t ) , ϕ ⁡ ( q ) ) . q_{\mathrm{hit}}\leftarrow\arg\max_{q\in\mathcal{M}(Z_{t})}\mathrm{sim}\!\big(\phi(q_{t}),\phi(q)\big).

[192] p: A semantic hit is declared if sim ⁡ ( ϕ ⁡ ( q t ) , ϕ ⁡ ( q hit ) ) ≥ τ \mathrm{sim}\!\big(\phi(q_{t}),\phi(q_{\mathrm{hit}})\big)\geq\tau (or a stricter reuse threshold if routing and reuse gates are decoupled in the implementation). This separates coarse candidate-topic retrieval from fine in-topic verification, while keeping verification localized to the routed topic.

[193] p: Representative and index maintenance. We maintain r ⁡ ( s ) r(s) and the topic-level index online under insertions and evictions, while preserving the anchor-based invariant. Representative updates are event-driven: r ⁡ ( s ) r(s) changes only when a newly inserted query becomes the TSI-max anchor, or when the current anchor is invalidated by eviction. When r ⁡ ( s ) r(s) changes, we update the corresponding entry in the topic-level index to keep retrieval consistent. Algorithm 5 summarizes the maintenance logic.

[194] p: On insertion. When a new query q q is assigned to topic s s , we append it to ℳ ⁡ ( s ) \mathcal{M}(s) and compute (or refresh) TSI ⁡ ( q ) \mathrm{TSI}(q) . If TSI ⁡ ( q ) \mathrm{TSI}(q) exceeds that of the query currently realizing r ⁡ ( s ) r(s) , we update r ⁡ ( s ) ← ϕ ⁡ ( q ) r(s)\leftarrow\phi(q) and update the index entry of s s ; otherwise, r ⁡ ( s ) r(s) remains unchanged. This yields O ⁡ ( 1 ) O(1) representative updates on insertions.

[195] p: On eviction (lazy refresh). When a query is evicted from topic s s , we remove it from ℳ ⁡ ( s ) \mathcal{M}(s) . If the evicted query is the one realizing r ⁡ ( s ) r(s) , we refresh the representative lazily: the refresh is deferred until the next time s s is needed as a routing candidate (e.g., returned by IndexQuery ) or otherwise accessed, at which time we scan ℳ ⁡ ( s ) \mathcal{M}(s) to select a query with maximal TSI ⁡ ( ⋅ ) \mathrm{TSI}(\cdot) and reset r ⁡ ( s ) r(s) to its embedding, followed by an index update. This scan is amortized since it is triggered only when the current anchor query is evicted.

[196] p: Empty-topic handling. If ℳ ⁡ ( s ) = ∅ \mathcal{M}(s)=\emptyset , we delete topic s s and remove it from the topic-level index, ensuring that the index only contains representatives of active topics.

[197] p: Retrieval-oriented discussion. The shortlist size K K trades off routing recall and per-request cost, while the threshold τ \tau trades off topic purity and fragmentation. Compared with centroid-like summaries, an anchor-based representative is cheaper to maintain and more stable under churn; selecting the anchor by TSI further biases r ⁡ ( s ) r(s) toward core and structurally necessary context, mitigating representativeness loss under mild intra-topic variability.

[198] h2: Instructions for reporting errors

[199] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[200] p: Tip: You can select the relevant text first, to include it in your report.

[201] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[202] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
