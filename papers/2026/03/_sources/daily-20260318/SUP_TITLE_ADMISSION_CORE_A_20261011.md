Token Coherence: Adapting MESI Cache Protocols to Minimize Synchronization Overhead in Multi-Agent LLM Systems (https://arxiv.org/html/2603.15183v1)
citeturn33069view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2603.15183v1","lineno":null}); Total lines: 785
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Background L18:     1. cite8†2.1 Cache Coherence and the MESI Protocol L19:     2. cite9†2.2 Multi-Agent LLM Orchestration L20:     3. cite10†2.3 The Always-Read Objection L21:   4. cite11†3 Conditional Artifact Access Semantics L22:     1. cite12†3.1 The Naive Access Model L23:     2. cite13†3.2 Artifact Externalization in Production Systems L24:     3. cite14†3.3 Formal Conditional Access Model L25:   5. cite15†4 Formal Model L26:     1. cite16†4.1 Artifact Coherence System L27:     2. cite17†4.2 MESI State Mapping L28:     3. cite18†4.3 The Broadcast Cost Baseline L29:     4. cite19†4.4 The Token Coherence Theorem L30:     5. cite20†4.5 Artifact Volatility and the Coherence Condition L31:   6. cite21†5 Protocol Specification L32:     1. cite22†5.1 System Assumptions L33:     2. cite23†5.2 System Architecture L34:     3. cite24†5.3 Protocol Operations L35:     4. cite25†5.4 Message Schema L36:     5. cite26†5.5 Synchronization Strategies L37:   7. cite27†6 Formal Verification L38:     1. cite28†6.1 TLA+ Specification L39:     2. cite29†6.2 Verified Invariants L40:     3. cite30†6.3 Verification Results L41:   8. cite31†7 Implementation L42:     1. cite32†7.1 Architecture Overview L43:     2. cite33†7.2 Framework Adapters L44:     3. cite34†7.3 Logical Clock and Version Ordering L45:   9. cite35†8 Evaluation L46:     1. cite36†8.1 Experimental Setup L47:     2. cite37†8.2 Token Savings Results L48:     3. cite38†8.3 The Volatility Cliff L49:     4. cite39†8.4 Prompt Caching Amplification L50:     5. cite40†8.5 Agent-Count Scaling L51:     6. cite41†8.6 Artifact-Size Scaling L52:     7. cite42†8.7 Step-Count Scaling L53:     8. cite43†8.8 Pointer Semantics Compatibility L54:   10. cite44†9 Related Work L55:     1. cite45†9.1 Multi-Agent Coordination Frameworks L56:     2. cite46†9.2 Conflict-Free Replicated Data Types L57:     3. cite47†9.3 Operational Transformation and Version Vectors L58:     4. cite48†9.4 Retrieval-Augmented Generation L59:     5. cite49†9.5 Long-Context and Context Compression L60:     6. cite50†9.6 Software Cache Coherence L61:     7. cite51†9.7 Agent Authorization Coherence L62:     8. cite52†9.8 Multi-Agent Failure Taxonomy L63:   11. cite53†10 Limitations and Future Work L64:   12. cite54†11 Conclusion L65:     1. cite55†11.1 Reproducibility
L66:     2. cite56†11.2 References
L67: cite57†License: arXiv.org perpetual non-exclusive license†info.arxiv.org L68: 
L69: arXiv:2603.15183v1 [cs.DC] 16 Mar 2026
L70: # Token Coherence: Adapting MESI Cache Protocols to Minimize Synchronization Overhead in Multi-Agent LLM Systems
L71: 
L72: Vladyslav Parakhin Affiliation: Independent Researcher
L73: ###### Abstract
L74: Per-token economics in multi-agent large language model orchestration are, at present, governed by a synchronization pathology that scales as $O(n\times S\times|D|)$ in agents, steps, and artifact size—a regime I designate broadcast-induced triply-multiplicative overhead. I contend this pathology does not inhere in multi-agent coordination per se; it is a structural residue of full-state rebroadcast, a design decision absorbed uncritically from early orchestration scaffolding.
L75: The central claim of this manuscript: the synchronization cost explosion in LLM-based multi-agent systems (MAS) maps, with formal precision, onto the cache coherence problem in shared-memory multiprocessors, and the canonical hardware remedy—MESI-protocol invalidation [Papamarcos and Patel 1984]—transfers to the artifact synchronization domain under minimal structural modification.
L76: I construct the Artifact Coherence System (ACS), a six-tuple $\langle A,D,\Sigma,\delta,\alpha,\mathcal{T}\rangle$ endowed with an identity state-mapping function $\varphi$ from hardware MESI states onto artifact authorization states.
L77: The Token Coherence Theorem delineates a savings lower bound: lazy artifact invalidation attenuates synchronization cost by a factor no less than $S/(n+W(d_{i}))$ subject to $S>n+W(d_{i})$, where $S$ is the step count, $n$ the agent population, and $W(d_{i})$ the per-artifact write frequency.
L78: I sequester the principal reviewer objection—that LLM agents invariably embed their full context and therefore cannot benefit from coherence—by formally delineating conditional artifact access semantics as instantiated in production architectures through tool calls, MCP resources, vector stores, and file search APIs.
L79: A TLA+-verified protocol (CCS v0.1) enforces three invariants: single-writer safety (SWMR), monotonic artifact versioning, and bounded-staleness (agents cannot reason on stale artifact state beyond $K$ steps).
L80: Through tick-based discrete event simulation across four workload configurations (10 runs per configuration, population standard deviation reported), comparing broadcast synchronization against three coherence strategies (eager, lazy, access-count), observed token savings reach $95.0\%\pm 1.3\%$ at $V=0.05$, $92.3\%\pm 1.4\%$ at $V=0.10$, $88.3\%\pm 1.5\%$ at $V=0.25$, and $84.2\%\pm 1.3\%$ at $V=0.50$—each exceeding the theorem’s conservative lower bounds of 85%, 80%, 65%, and 40% respectively.
L81: Contrary to the lower-bound formula’s prediction ($V^{*}\approx 0.9$ for $n=4$, $S=40$ marking the savings collapse threshold), simulation indicates savings of approximately 81% persist at $V=0.9$ because lazy deferred-fetch accumulation obviates worst-case collapse from materializing (§8.3).
L82: Contributions: (1) a formal mapping between MESI cache coherence and multi-agent artifact synchronization; (2) the Token Coherence Theorem as savings lower bound with the condition under which coherence dominates broadcast; (3) a TLA+-verified protocol with three proven invariants; (4) a characterization of conditional artifact access semantics that resolves the always-read objection; (5) a reference Python implementation integrating with LangGraph, CrewAI, and AutoGen via thin adapter layers.
L83: Subjects: Distributed, Parallel, and Cluster Computing (cs.DC); Multiagent Systems (cs.MA); Machine Learning (cs.LG)
L84: ## 1 Introduction
L85: Five agents, fifty reasoning steps, one 8,192-token planning document. Under naive broadcast, the cost is $5\times 50\times 8{,}192=2{,}048{,}000$ tokens—and the vast majority of that budget is unchanged context, retransmitted without necessity. The waste is banal, not exotic.
L86: It is the default behavior—I have verified this by instrumenting every major orchestration framework I could obtain access to—that upon modification of any shared artifact, the orchestrator rebroadcasts its full contents to every subscribing agent at the next synchronization boundary. At modest scale, tolerable.
L87: At production scale—and I should be precise about what I mean by “production” here, meaning $n\geq 5$ agents sustaining $S\geq 40$ reasoning steps over multiple artifacts simultaneously—the cost structure becomes, without exaggeration, ruinous.
L88: Beyond the invoice, the damage compounds in subtler and arguably more corrosive ways. Token budget constraints coerce practitioners into truncating reasoning traces, compressing artifacts, culling agent populations—each a degradation that trades capability for a cost reduction that is, under certain structural conditions I formalize below, entirely avoidable.
L89: Building on [4], Cemri et al.’s analysis of 1,642 execution traces spanning seven production MAS frameworks reports task failure rates between 41% and 86.7%. Inter-agent misalignment—including what they designate FM-1.4, Loss of Conversation History, where agents revert to stale artifact states following context truncation—accounts for 32.3% of observed failures.
L90: They note explicitly that multi-agent memory and state management persists as an open structural problem, one that most prior work sidesteps by addressing single-agent contexts only [4, Appendix G.2].
L91: Independently—and this is a datum I consider underappreciated in the current discourse—empirical benchmarking across multi-agent frameworks reports token duplication rates of 86% in flat topologies and 72% in linear topologies [28], confirming that redundant artifact retransmission, not generation, constitutes the dominant cost driver.
L92: Hardware engineers confronted an isomorphic problem four decades ago. I want to be careful with “isomorphic”—the word does nontrivial load-bearing work, and I will qualify the claim in §4.2 with a discussion of where the stable-state mapping breaks down at the transient-state boundary. The short version: in shared-memory multiprocessors, multiple CPU cores sharing a memory bus incur catastrophic bandwidth costs when every write forces full memory retransmission to all caches.
L93: The remedy—cache coherence protocols, MESI [19] being canonical—tracks per-cache-line state and propagates invalidation signals rather than data. A cache line transitions from Shared to Invalid upon a remote write; subsequent reads trigger a targeted fetch. Bandwidth cost becomes proportional to write frequency, not to step count.
L94: The structural parallel maps cleanly: agents are processors, artifacts are cache lines, the orchestration coordinator is the memory controller, prompt injection of an artifact is a cache fill. I submit that this analogy admits a formal state-mapping function between MESI states and artifact coherence states, and that hardware-derived cost bounds transfer—with caveats I enumerate—into the agent coordination domain.
L95: Before formalizing this claim, I must confront what I term the always-read objection. The objection runs as follows: LLM agents consume their entire context window at every inference call, so lazy invalidation is useless because the artifact must be injected regardless. This objection is descriptively incorrect for modern production architectures—a point I delineate at length in §3.
L96: Tool-based retrieval, MCP resource access [1], vector store retrieval, and provider-side prompt caching all instantiate conditional artifact access semantics in which $R(a,s)\subsetneq D$. The always-read model describes naive prompt concatenation only. It does not describe the externalized architectures that dominate production deployments.
L97: Whether it describes a majority of current deployments, I cannot certify without broader instrumentation data—but the architectural trend is unmistakable, and the formal argument stands contingent on conditional access holding.
L98: Contribution 1 — Formal equivalence. I define the Artifact Coherence System (ACS) as a six-tuple $\langle A,D,\Sigma,\delta,\alpha,\mathcal{T}\rangle$ and construct an explicit MESI state-mapping function $\varphi$ from hardware cache states to artifact authorization states, establishing that the structural properties of MESI transfer intact to the artifact domain (§4).
L99: Contribution 2 — Token Coherence Theorem. I prove that lazy artifact invalidation attenuates multi-agent token cost by a factor bounded below by $S/(n+W(d_{i}))$ when $S>n+W(d_{i})$, establishing that broadcast cost grows as $O(n\times S\times|D|)$ while coherent cost grows as $O((n+W)\times|D|)$ at worst. Simulation confirms consistently higher savings than this lower bound (§8).
L100: The condition under which coherence dominates is precisely characterized by the artifact volatility factor $V(d_{i})=W(d_{i})/S$ (§4.3–4.5).
L101: Contribution 3 — TLA+-verified protocol. I specify Coherent Context Synchronization (CCS) in TLA+ and verify three invariants: SWMR, monotonic versioning, and $K$-bounded staleness. I report the state space explored (approximately 2,400 states for 3 agents) and construct an explicit counterexample demonstrating that removing invalidation violates SWMR (§5–6).
L102: Contribution 4 — Conditional access semantics. I formally characterize real agent access patterns as $R(a,s)\subseteq D$ rather than $R(a,s)=D$, grounding this in four production architecture patterns and identifying the token duplication phenomenon that coherence eliminates (§3).
L103: Contribution 5 — Reproducible implementation. I present a reference Python implementation (agent-coherence v0.1) integrating with LangGraph, CrewAI, and AutoGen through adapter layers requiring no framework modifications, with a simulation engine supporting four synchronization strategies and full reproducibility from published seeds (§7, §8).
L104: ## 2 Background
L105: ### 2.1 Cache Coherence and the MESI Protocol
L106: Per Sorin, Hill, and Wood [22], cache coherence requires that all reads to a memory location return the value of the most recent write and that writes to the same location are serialized across processors.
L107: Under MESI [19], four stable states per cache line per processor obtain: Modified (valid only in this cache; memory is stale), Exclusive (valid only in this cache; identical to memory), Shared (valid here and possibly elsewhere; no writes since last commit), Invalid (not valid; coherence fill required before use).
L108: Between stable states, transient states model in-flight operations [22, Ch.6]—e.g., $M^{IS}$ denotes a line that was Modified, is transitioning to Invalid, and awaits acknowledgment. These transient states bear on protocol correctness. I elide them in the first-order model that follows—a deliberate simplification constraining the analysis to quiescent-state reasoning and foreclosing claims about transient-state behavior in ACS.
L109: The limitation is real; I will revisit it in §4.2 when the question of what “structural isomorphism” means across asynchronous event-bus semantics becomes non-trivially relevant.
L110: The core efficiency property of MESI: update-on-demand. Transitions from Invalid to Shared or Exclusive are triggered only by actual reads, not by writes elsewhere. Broadcast-on-write bandwidth converts to targeted-fetch-on-read bandwidth. When write frequency $W$ is low relative to read frequency $R$, savings are substantial. When $W\approx R$, protocol overhead approaches the broadcast baseline. The mapping from CPU memory hierarchies to multi-agent systems is summarized in Table 0.
L111: CCS v0.1 targets the L1/L2 $\leftrightarrow$ LLC tier (agent runtime cache $\leftrightarrow$ shared artifact store); persistent storage and cross-workflow artifact retention are explicitly out of scope.
L112: Table 0: Agent Memory Hierarchy Analogy
L113: CPU Memory Hierarchy  | Agent Memory Hierarchy  | Coherence Mechanism
L114: --- | --- | ---
L115: L1/L2 cache (per-core)  | Agent artifact cache (per-agent runtime)  | MESI state per agent–artifact pair
L116: Shared LLC / main memory  | Shared artifact store (authority service)  | Canonical version + invalidation events
L117: Memory bus / coherence fabric  | Event bus (Redis / Kafka / NATS)  | Invalidation and version-update messages
L118: Disk / persistent storage  | Long-term persistence (vector DB, file store)  | Out of scope for CCS v0.1
L119: ### 2.2 Multi-Agent LLM Orchestration
L120: Multi-agent LLM systems [24; 26; 23] coordinate multiple language model instances on shared tasks. LangGraph [21], CrewAI [5], AutoGen [24], Semantic Kernel [15]—each represents agents as nodes in a computation graph, passing state via structured messages or shared memory constructs. The synchronization pattern is uniform, and I state this without observed exception across every framework I have instrumented: full-state rebroadcast.
L121: Upon artifact modification by any agent, the orchestrator injects the complete updated artifact into the next prompt of every agent that might need it. Consistency is purchased at the cost described above.
L122: Building on [4], the MAST taxonomy identifies 14 failure modes across 1,642 annotated execution traces. Failure rates: 41%–86.7%. Dominant categories: system design issues (44.2%), inter-agent misalignment (32.3%). FM-1.4—Loss of Conversation History—describes agents reverting to earlier artifact states following unexpected context truncation, at 2.8% occurrence across all traces.
L123: The bounded-staleness invariant of CCS (§6) instantiates a formal upper bound on the number of reasoning steps any agent can operate on stale artifact state—a structural, not heuristic, constraint on exactly the failure class Cemri et al. identify.
L124: ### 2.3 The Always-Read Objection
L125: 
L126: Before the formal model, I confront the objection that will—and should—be raised by reviewers conversant with transformer inference mechanics. The objection: LLM agents ingest their entire context window at every forward pass. Lazy invalidation cannot prevent artifact injection. A token in the prompt is a token consumed.
L127: Correct on one point, this objection: a token in the prompt is indeed a token consumed. What it misdescribes is the prompt construction process—and here I remain cautious (the diversity of production deployment architectures is wider than any single author can claim to have instrumented exhaustively), but I am confident enough to state categorically: modern agents do not assemble context from artifacts embedded inline.
L128: They assemble context from references to externally stored artifacts, retrieving conditionally via tool calls, MCP resource requests, or retrieval APIs. I formalize this in §3. The always-read model applies to naive single-turn prompt construction exclusively. Whether it still describes a non-negligible fraction of deployed systems—yes, almost certainly. Whether it describes the architectures consuming the majority of the multi-agent token budget—no.
L129: The distinction matters for the applicability claim, and I draw it deliberately.
L130: ## 3 Conditional Artifact Access Semantics
L131: ### 3.1 The Naive Access Model
L132: 
L133: Let $A=\{a_{1},\ldots,a_{n}\}$ denote a set of agents and $D=\{d_{1},\ldots,d_{m}\}$ a set of shared artifacts. Denote by $R(a,s)$ the set of artifacts whose full token contents are injected into the prompt of agent $a$ at reasoning step $s$. Under the naive broadcast model:
L134: 
L135:  | $$R(a,s)=D\quad\forall a\in A,\;\forall s$$  |
L136: Per-step token cost under this assumption: $\sum_{i}|d_{i}|$ per agent. Total cost: $n\times S\times\sum_{i}|d_{i}|$. Lazy invalidation is trivially useless under this regime—even a cached-and-valid artifact must be injected to remain accessible. MESI savings: zero.
L137: ### 3.2 Artifact Externalization in Production Systems
L138: 
L139: The assertion $R(a,s)=D$ is not the access model instantiated by modern production agent architectures. Four patterns bifurcate the naive model, each yielding $R(a,s)\subsetneq D$:
L140: Tool-based retrieval. LangChain and OpenAI Assistants expose retrieval tools—get\_document(), read\_file(), query\_memory(). System prompts carry artifact identifiers, not artifact contents. Tool invocation is conditional; tool calls that never fire never inject tokens. $R(a,s)\subseteq D$ with proper subset holding whenever not all tools are invoked.
L141: The mechanism is straightforward; the implication for coherence economics is less so, because the decision to invoke a tool is itself a stochastic function of the agent’s reasoning trace—a dependency I have not modeled formally and acknowledge as a simplification.
L142: MCP resource access. Under the Model Context Protocol [1], artifacts are external resources identified by URIs (resource://shared\_plan, resource://research\_notes). Injection occurs only upon explicit request. The resource reference in the system prompt costs $O(1)$ tokens, not $O(|d_{i}|)$—a distinction whose significance scales with artifact size.
L143: Vector retrieval systems. Retrieval-augmented architectures store artifacts in vector stores and inject only top-$k$ retrieved fragments. The prompt contains $\min(k,|d_{i}|)\ll|d_{i}|$ tokens for any large artifact. Agent exposure to artifact tokens it did not retrieve is structurally precluded.
L144: Provider-side prompt caching. Anthropic, OpenAI, and Google all implement prompt prefix caching attaining non-trivial reuse across consecutive agent calls [2; 17]. The caching mechanism operates only when the prompt prefix is identical across calls. Were artifacts re-embedded with updated content at every step, cache hit rates would approach zero—but production deployments report substantial reuse.
L145: This is attainable only when prompt prefixes remain stable, attainable only when artifacts are not re-embedded at every step. I find this a minor but telling methodological observation: the existence of high prompt cache hit rates in production constitutes indirect evidence that real-world systems do not, in fact, operate under the always-read model.
L146: The evidence is circumstantial—I cannot rule out that high cache hit rates arise from other prefix-stability mechanisms—but the inference is, within its constraints, sound.
L147: The 86% token duplication measured in flat multi-agent topologies [28] is not a contradiction. Systems currently operating under naive broadcast semantics do incur this cost. The argument is that they ought not—and the conditional access patterns above delineate how production systems already escape it at scale.
L148: ### 3.3 Formal Conditional Access Model
L149: 
L150: I define the conditional artifact access model as:
L151: 
L152:  | $$R(a,s)\subseteq D\quad\forall a\in A,\;\forall s$$  |
L153: 
L154: with the conditional access condition requiring that for most artifacts and steps:
L155: 
L156:  | $$\Pr[d_{i}\in R(a,s)]\ll 1$$  |
L157: Under this model, the relevant cost is not prompt token consumption per step but artifact injection frequency—how often $d_{i}$’s full contents must be transmitted to agent $a$’s context. Lazy invalidation attenuates this frequency: when $d_{i}$ has not been modified since agent $a$ last received it, no retransmission occurs. The agent holds a valid local reference; the cached version remains coherent.
L158: This restores the conditions under which MESI savings are attainable and renders the formal argument in §4 applicable to deployed systems.
L159: ## 4 Formal Model
L160: ### 4.1 Artifact Coherence System
L161: 
L162: Definition 1 (Artifact Coherence System). An Artifact Coherence System (ACS) is a tuple $\langle A,D,\Sigma,\delta,\alpha,\mathcal{T}\rangle$ where:
L163: 
L164:   * •
L165: 
L166: $A=\{a_{1},\ldots,a_{n}\}$ is a finite set of agents;
L167: 
L168:   * •
L169: 
L170: $D=\{d_{1},\ldots,d_{m}\}$ is a finite set of shared artifacts (analogous to memory locations / cache lines);
L171: 
L172:   * •
L173: 
L174: $\Sigma=\{M,E,S,I\}$ is the set of stable artifact coherence states;
L175: 
L176:   * •
L177: $\delta:\Sigma\times\mathcal{E}\rightarrow\Sigma$ is the state transition function, where $\mathcal{E}=\{\texttt{read},\texttt{write},\texttt{upgrade},\texttt{fetch},\texttt{invalidate},\texttt{commit}\}$;
L178: 
L179:   * •
L180: 
L181: $\alpha:A\times D\rightarrow\Sigma$ is the coherence state function mapping each agent–artifact pair to its current state;
L182: 
L183:   * •
L184: 
L185: $\mathcal{T}:\Sigma\rightarrow\{0,1\}$ is the validity predicate, with $\mathcal{T}(I)=0$ and $\mathcal{T}(s)=1$ for $s\in\{M,E,S\}$.
L186: The validity predicate renders the MESI safety invariant precise: an agent may reference a cached artifact only when $\mathcal{T}(\alpha(a,d_{i}))=1$. State $I$ mandates a coherence fill—a fetch from the authority service—before use.
L187: ### 4.2 MESI State Mapping
L188: 
L189: I construct an explicit mapping $\varphi$ from hardware MESI states to artifact coherence states.
L190: 
L191: Definition 2 (MESI State Mapping). The mapping $\varphi:\Sigma_{\text{hw}}\rightarrow\Sigma$ is the identity function on the shared state space $\{M,E,S,I\}$, with the following semantic interpretations in the artifact domain:
L192: Hardware State  | Artifact State  | Semantic Interpretation
L193: --- | --- | ---
L194: Modified ($M$)  | Modified ($M$)  | Agent holds the only valid copy; authority copy is stale; other agents are invalidated
L195: Exclusive ($E$)  | Exclusive ($E$)  | Agent holds the only copy, identical to authority; write permitted without broadcast
L196: Shared ($S$)  | Shared ($S$)  | Multiple agents hold valid copies; no agent has written since last commit
L197: Invalid ($I$)  | Invalid ($I$)  | Agent’s cached copy is stale; full fetch required before next use
L198: Every state transition in the hardware protocol possesses a direct semantic counterpart in the artifact protocol: “cache fill” maps to “artifact fetch,” “bus invalidation” maps to “invalidation event” over the message bus.
L199: 
L200: Proposition 1 (Structural Equivalence). The ACS transition system $(\Sigma,\delta)$ is isomorphic to the MESI hardware transition system under $\varphi$. Every safety result that holds for MESI under the SWMR invariant holds for ACS under the identical invariant.
L201: Proof sketch. By construction of $\varphi$ as the identity mapping on $\{M,E,S,I\}$, and by the fact that $\delta$ reproduces the MESI transition table exactly (read causes $I\rightarrow S$, write causes $S\rightarrow M$ with peer invalidation, commit causes $M\rightarrow S$, fetch causes $I\rightarrow S$). The SWMR invariant $\forall a\neq b:\neg(\alpha(a,d)=M\wedge\alpha(b,d)=M)$ is maintained by the identical write-invalidates-peers rule present in both systems. $\square$
L202: A limitation I want to foreground rather than relegate to §10: the isomorphism holds at the stable-state level, but the transient-state behavior of hardware MESI—which involves non-trivial race conditions on the bus fabric—maps only approximately to asynchronous event-bus semantics in CCS. I have not formalized the transient-state correspondence. I remain cautious about extending the equivalence claim beyond quiescent states until that formalization is complete. This is not, I suspect, a trivial gap.
L203: The liveness pathologies of snoopy-bus transient interleavings under hardware MESI are well-documented [22, Ch.6], and their analogs in asynchronous message delivery are, at minimum, non-obvious. Whether this gap undermines the practical utility of the mapping—I think not, because the protocol operates at quiescent-state granularity by design—but a reviewer insisting on transient-state completeness would have a legitimate objection that I cannot yet discharge.
L204: ### 4.3 The Broadcast Cost Baseline
L205: 
L206: Under the naive broadcast model ($R(a,s)=D$), total token cost for $n$ agents, $S$ steps, and $m$ artifacts:
L207: 
L208:  | $$T_{\text{broadcast}}=n\times S\times\sum_{i=1}^{m}|d_{i}|$$  |
L209: 
L210: where $|d_{i}|$ denotes token size of artifact $d_{i}$. The cost grows multiplicatively—doubling agents, steps, or artifact size each doubles total cost. For a typical configuration ($n=5$, $S=50$, $m=3$, $|d_{i}|=4{,}096$ tokens):
L211:  | $$T_{\text{broadcast}}=5\times 50\times 3\times 4{,}096=3{,}072{,}000\text{ tokens}$$  |
L212: 
L213: Under conditional access ($R(a,s)\subseteq D$), the relevant per-step cost is not full artifact injection but the coherence synchronization cost: tokens transmitted due to initial reads and write-triggered re-fetches.
L214: ### 4.4 The Token Coherence Theorem
L215: 
L216: Definition 3 (Coherent Synchronization Cost Upper Bound). Under the ACS model with lazy invalidation, total token cost is bounded above by:
L217: 
L218:  | $$T_{\text{coherent}}\leq\sum_{i=1}^{m}n\cdot\bigl(n+W(d_{i})\bigr)\times|d_{i}|$$  |
L219: where $W(d_{i})$ denotes total write operations to artifact $d_{i}$ across all agents and steps. The bound arises because each of $n$ agents performs at most one initial fetch per artifact, and each write event can trigger at most $n-1$ invalidations each followed by one re-fetch. Conservatively counting the writer’s own fetch, worst-case total fetches per artifact: $n(1+W(d_{i}))$, approximated as $n(n+W(d_{i}))$ for the multi-agent stochastic access model (§8.1).
L220: The bound is tight only when every invalidation immediately triggers a re-fetch—a condition that lazy coherence precludes by collapsing multiple write events into a single re-fetch when agents do not access an invalidated artifact between consecutive writes.
L221: The gap between bound and observation is, in my experience, substantial—ranging from 10 to 45 percentage points depending on workload—and this gap is itself a finding worth flagging, because it suggests that the analytical bound, while correct, may be too conservative to serve as a useful planning heuristic for practitioners at high $V$.
L222: Assumptions. Two modeling assumptions bound the scope of Theorem 1:
L223: 
L224: (A1) Full-artifact transmission on cache miss. Each cache miss triggers transmission of the full artifact $d_{i}$ ($|d_{i}|$ tokens). Sub-artifact delta fetches are not modeled; this is a conservative assumption that overestimates coherent cost.
L225: (A2) Serialized writes via authority. All writes to a given artifact are serialized through the authority service. Concurrent peer-to-peer writes are not modeled; the single-writer invariant (§6.2) enforces this structurally.
L226: 
L227: Theorem 1 (Token Coherence Theorem — Savings Lower Bound). (Under Assumptions A1 and A2.) The token savings from lazy artifact invalidation are bounded below by:
L228:  | $$\text{Savings}\geq 1-\frac{T_{\text{coherent}}^{\text{upper}}}{T_{\text{broadcast}}}=1-\frac{\sum_{i}n(n+W(d_{i}))|d_{i}|}{n\times S\times\sum_{i}|d_{i}|}$$  |
L229: 
L230: The condition under which savings are strictly positive is:
L231: 
L232:  | $$S>n+W(d_{i})\quad\text{for most artifacts }d_{i}$$  |
L233: 
L234: For identical artifact sizes $|d_{i}|=|d|$, the lower bound simplifies to:
L235: 
L236:  | $$\text{Savings}\geq 1-\frac{n+W(d_{i})}{S}$$  |
L237: Proof. Substitute the Definition 3 upper bound for $T_{\text{coherent}}$ and the broadcast formula into the savings ratio. For uniform artifact sizes the $|d|$ and the leading $n$ cancel: $n(n+W)|d|\;/\;nS|d|=(n+W)/S$. Savings $\geq 1-(n+W)/S$. Since $T_{\text{coherent}}^{\text{actual}}\leq T_{\text{coherent}}^{\text{upper}}$, actual savings meet or exceed this bound. The condition $S>n+W(d_{i})$ ensures positivity. $\square$
--------------------------------------------------------------------------------
AutoMoT: A Unified Vision-Language-Action Model with Asynchronous Mixture-of-Transformers for End-to-End Autonomous Driving (https://arxiv.org/html/2603.14851v1)
citeturn33069view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2603.14851v1","lineno":null}); Total lines: 402
--------------------------------------------------------------------------------
Balancing Saliency and Coverage:Semantic Prominence-Aware Budgeting for Visual Token Compression in VLMs (https://arxiv.org/html/2603.14892v1)
citeturn33069view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2603.14892v1","lineno":null}); Total lines: 530
--------------------------------------------------------------------------------
Flash-Unified: A Training-Free and Task-Aware Acceleration Framework for Native Unified Models (https://arxiv.org/html/2603.15271v1)
citeturn33069view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2603.15271v1","lineno":null}); Total lines: 579

