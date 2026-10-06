[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Contextual Memory Virtualisation: DAG-Based State Management and Structurally Lossless Trimming for LLM Agents

[3] h6: Abstract

[4] p: As large language models engage in extended reasoning tasks, they accumulate significant state – architectural mappings, trade-off decisions, codebase conventions – within the context window. This understanding is lost when sessions reach context limits and undergo lossy compaction. We propose contextual memory virtualisation (CMV), a system that treats accumulated LLM understanding as version-controlled state. Borrowing from operating system virtual memory, CMV models session history as a Directed Acyclic Graph (DAG) with formally defined snapshot, branch, and trim primitives that enable context reuse across independent parallel sessions. We introduce a three-pass structurally lossless trimming algorithm that preserves every user message and assistant response verbatim while reducing token counts by a mean of 20% and up to 86% for sessions with significant overhead by stripping mechanical bloat such as raw tool outputs, base64 images, and metadata. A single-user case-study evaluation across 76 real-world coding sessions demonstrates that trimming remains economically viable under prompt caching, with the strongest gains in mixed tool-use sessions, which average 39% reduction and reach break-even within 10 turns. A reference implementation is available at https://github.com/CosmoNaught/claude-code-cmv .

[5] h2: 1 Introduction

[6] p: Extended work sessions with LLM coding agents build cumulative state within the context window. Architecture gets mapped, trade-offs get weighed, decisions are recorded, conventions are learned. After 30 minutes of deep work, the model holds a mental model of an entire codebase, built at significant computational cost in both time and tokens. When the context window fills, native compaction (e.g., /compact in Claude Code ( Anthropic, 2024b ) ) summarises this state into a few sentences. In observed sessions, autocompaction reduced 132k tokens of accumulated message state to 2.3k—a 98% reduction (Figure 1 )—discarding the nuanced understanding that took an entire session to build. Each new session starts from scratch.

[7] figure: Figure 1: Context window before (left, 132k message tokens, 76% capacity) and after (right, 2.3k message tokens, 12% capacity) native autocompaction (e.g., Claude Code). Autocompaction summarises 98% of accumulated session state into a brief summary to reclaim window space.

[8] p: This is a fundamental inefficiency. The cost of building context is paid repeatedly, and the resulting understanding is never preserved in a reusable form. Existing approaches address fragments of this problem. Retrieval-Augmented Generation (RAG) ( Lewis et al., 2020 ) augments prompts with retrieved documents but does not preserve conversational state. MemGPT ( Packer et al., 2023 ) applies OS-inspired paging to swap context segments in and out of the window, but is limited to a single session and relies on the model to manage its own memory. Memory plugins persist summary facts across sessions but lose the full conversational nuance. Native session utilities ( /rewind , --fork ) provide within-session undo and one-off copies but lack named states, lineage tracking, or context cleanup.

[9] p: A separate line of work addresses context window pressure through prompt compression. LongLLMLingua ( Jiang et al., 2023 ) accelerates inference by compressing long prompts via perplexity-guided token pruning. Chevalier et al. ( Chevalier et al., 2023 ) train models to produce compressed soft tokens from long contexts. RECOMP ( Xu et al., 2024 ) selectively compresses retrieved documents before augmentation. Ge et al. ( Ge et al., 2024 ) propose an in-context autoencoder that learns to compress and reconstruct context segments. These approaches modify the representation of context at the model or embedding level. Contextual memory virtualisation (CMV) operates at a different layer entirely: it manages the raw conversation log, preserving full fidelity while removing structural bloat. The two approaches are complementary. The attention mechanism underlying modern LLMs ( Vaswani et al., 2017 ) processes all tokens in the context window with equal cost, making window size reduction valuable regardless of the method used.

[10] p: We frame this solution as contextual memory virtualisation . Just as virtual memory in an operating system abstracts away the physical limits of hardware RAM—giving each process the illusion of a vast, contiguous memory space via paging—CMV abstracts away the strict physical token limits of the LLM context window. Instead of forcing the model to live entirely within its ”RAM” (the current window), CMV allows the user to page saved architectural understanding in and out of active context as needed, effectively decoupling the cost of building context from the cost of executing a task.

[11] p: CMV comprises three contributions. At its core is a DAG-based state model that formalises context snapshots as nodes and branches as edges, allowing a single context-building session to act as a persistent root for multiple independent workstreams. We pair this with a three-pass structurally lossless trimming algorithm that safely strips mechanical overhead—such as raw tool outputs and base64 images—while keeping all user and assistant messages intact and handling orphaned tool results to maintain API correctness. Finally, we provide an empirical cost analysis across 76 real-world sessions to demonstrate that this trimming approach remains economically viable even under prompt caching penalties. The reference implementation targets Claude Code, but the DAG model and trimming architecture are agent-agnostic; any system that stores conversation logs and uses tool-call schemas can apply the same approach.

[12] h2: 2 The DAG State Model

[13] h3: 2.1 Formal Definition

[14] p: We model session history as a DAG G = ( V , E ) G=(V,E) where:

[15] p: Each node v ∈ V v\in V is a snapshot : an immutable copy of a session’s JSONL conversation log at a point in time, annotated with metadata (name, timestamp, source session, estimated tokens, tags).

[16] p: Each directed edge ( v i , v j ) ∈ E (v_{i},v_{j})\in E represents a branch : an independent work session forked from snapshot v i v_{i} that eventually yields snapshot v j v_{j} . The forked session receives a copy of v i v_{i} ’s conversation state (optionally trimmed) and a fresh session identifier.

[17] p: A snapshot v v may have a parent snapshot parent ​ ( v ) \text{parent}(v) if the session from which v v was captured was itself branched from an earlier snapshot. This induces a lineage chain: v 0 → v 1 → ⋯ → v k v_{0}\to v_{1}\to\cdots\to v_{k} , where each v i + 1 v_{i+1} inherits the cumulative understanding of all ancestors. This branching structure forms a directed tree (a strict subclass of Directed Acyclic Graphs). We adopt the broader DAG terminology to align with version-control conventions and to accommodate future merge primitives.

[18] h3: 2.2 Core Operations

[19] p: Four primitives operate on this graph:

[20] p: Snapshot ( s s ) → v \to v : Given a session s s , copies the JSONL conversation file to immutable storage and creates a new node v v with metadata. The original session is never modified.

[21] p: Branch ( v v , trim) → s ′ \to s^{\prime} : Given a snapshot v v , creates a new session s ′ s^{\prime} with a fresh UUID. If trim is enabled (the default), the conversation is processed by the trimming algorithm (Section 3 ) before being written to the new session. An optional orientation message can be prepended as the first user line to point the model toward a specific task on the new branch.

[22] p: Trim ( s s ) → s ′ \to s^{\prime} : A convenience operation that composes Snapshot and Branch: captures the current session, trims it, and launches a new session in one step.

[23] p: Tree ( G G ) → \to visualisation: Traverses parent links to reconstruct the full DAG and renders it with ASCII connectors, providing a git log --graph equivalent for conversational context.

[24] h3: 2.3 Practical Implications

[25] p: By modeling conversation state as a DAG, CMV introduces a version-control paradigm for LLM context —effectively a Git-like workflow for conversational memory. Previously, interacting with an LLM was strictly linear and ephemeral: a single thread that inevitably degrades upon compaction. Under CMV, a user who spends 40 minutes generating 80k tokens of architectural understanding can snapshot that state as a stable root commit. From this root, they can spawn independent, parallel branches for authentication work, API refactoring, or performance tuning, without ever repeating the context-building phase.

[26] h2: 3 Three-Pass Structurally Lossless Trimming

[27] p: The core technical challenge is reducing the token payload without losing the model’s synthesised understanding. Inspection of real session data reveals that the majority of context window usage is consumed by mechanical overhead (raw file dumps returned as tool results, base64-encoded images, thinking block signatures, file-history metadata) rather than by the conversation itself. The model’s synthesis of these inputs (its architectural summaries, design decisions, and explanations) is contained in assistant response blocks, which are typically a small fraction of total tokens.

[28] p: We introduce a streaming algorithm that strips this mechanical overhead while preserving every user message and assistant response verbatim. If the model needs a file’s contents again after trimming, it simply re-reads the file.

[29] h3: 3.1 Algorithm Architecture

[30] p: The trimmer processes JSONL-formatted conversation logs in three sequential passes, as outlined in Algorithm 1 . Pass 1 and Pass 2 are cheap preparatory scans; Pass 3 performs the actual filtering and writes the output.

[31] figure: Algorithm 1 Three-Pass Structurally Lossless Trimmer Input: source JSONL path S S , stub threshold τ \tau (default 500 chars) Output: trimmed JSONL path D D , metrics M M // Pass 1: Compaction Boundary Detection 1 B ← − 1 B\leftarrow-1 2 foreach line ℓ i \ell_{i} in S S do 3 if String.includes() matches compaction markers then 4 parse ℓ i \ell_{i} 5 if type ∈ { \in\{ summary , compact_boundary } \} then 6 B ← i B\leftarrow i // Pass 2: Pre-Boundary Tool ID Collection 7 𝒪 ← ∅ \mathcal{O}\leftarrow\emptyset 8 foreach line ℓ i \ell_{i} in S S where i < B i<B do 9 foreach content block b b in ℓ i \ell_{i} do 10 if b . type = b.\text{type}= tool_use then 11 𝒪 ← 𝒪 ∪ { b . id } \mathcal{O}\leftarrow\mathcal{O}\cup\{b.\text{id}\} // Pass 3: Stream-Process with Trim Rules 12 foreach line ℓ i \ell_{i} in S S do 13 if i < B i<B then 14 skip (pre-compaction content) 15 if type ∈ { \in\{ file-history , queue-op } \} then 16 skip 17 Strip base64 image blocks 18 Remove thinking blocks (non-portable signatures) 19 Stub tool_result content > τ >\tau chars 20 Stub write-tool inputs > τ >\tau chars (preserve metadata fields) 21 Strip tool_result blocks where id ∈ 𝒪 \text{id}\in\mathcal{O} (orphans) 22 Remove API usage metadata 23 Write processed ℓ i \ell_{i} to D D 24 return D , M D,M

[32] p: Pass 1 uses String.includes() on raw lines to detect potential compaction boundaries without parsing JSON on every line, making the scan near-costless on large files. Only matching lines are parsed. Pass 2 collects tool_use IDs that will be needed in Pass 3 for orphan detection (Section 3.3 ).

[33] h3: 3.2 Trim Rules and Preservation Guarantees

[34] p: The algorithm applies the following rules during Pass 3. Critically, every user message, every assistant response, and every tool request (the invocation metadata) is preserved verbatim. Only mechanical outputs are reduced:

[35] p: Pre-compaction skip: All lines before the last compaction boundary are discarded (already summarised by native compaction).

[36] p: Metadata removal: file-history-snapshot and queue-operation entries are discarded.

[37] p: Image stripping: Base64 image blocks are removed unconditionally.

[38] p: Tool result stubbing: tool_result content exceeding τ \tau characters is replaced with a stub: [Trimmed: ~N chars] .

[39] p: Tool input stubbing: For write-oriented tools, large content , old_string , and new_string fields are stubbed. A whitelist of metadata fields ( file_path , command , description , path , url , etc.) is never stubbed, ensuring the model retains knowledge of which files were read and which commands were run.

[40] p: Thinking block removal: Thinking blocks require a cryptographic signature that is not portable across sessions and are removed entirely.

[41] p: Orphaned tool result stripping: Detailed in Section 3.3 .

[42] p: The stub threshold τ \tau defaults to 500 characters (minimum 50) and is configurable per-operation.

[43] h3: 3.3 Orphaned Tool Result Handling

[44] p: LLM tool-use APIs typically enforce a strict schema: every tool_result block must reference a tool_use block present in a preceding assistant message. Native compaction often places its boundary between a tool invocation (in an assistant turn) and the corresponding result (in the next user turn). When pre-boundary content is discarded in Pass 3, the tool_use blocks that lived before the boundary are removed, but their corresponding tool_result blocks may exist after the boundary. Without correction, submitting a session containing these “orphaned” results causes an API validation error and the session cannot be resumed.

[45] p: Pass 2 collects the set 𝒪 \mathcal{O} of all tool_use IDs from pre-boundary content. During Pass 3, any tool_result whose tool_use_id ∈ 𝒪 \in\mathcal{O} is silently discarded. This maintains API correctness without user intervention and was the primary motivation for the three-pass architecture.

[46] h2: 4 Economic Evaluation

[47] p: Major LLM APIs implement prompt caching (e.g., Anthropic 2024a ). If the prompt prefix matches a previously cached prefix, cached tokens are read at a reduced rate rather than reprocessed at the write rate. Trimming necessarily changes the prefix, invalidating the cache and incurring a one-time miss penalty. We evaluate whether per-turn savings from caching a smaller prefix recover that penalty.

[48] h3: 4.1 Cost Model

[49] p: For a cache hit rate h h , the steady-state cost per turn at token count T T is:

[50] table: C ⁡ ( T , h ) = T 10 6 ​ ( h ⋅ P read + ( 1 − h ) ⋅ P write ) C(T,h)=\frac{T}{10^{6}}\left(h\cdot P_{\text{read}}+(1-h)\cdot P_{\text{write}}\right)

[51] p: where P read P_{\text{read}} and P write P_{\text{write}} are the per-million-token cache read and write prices respectively. The first turn after a trim incurs a cold-cache penalty at the full write rate:

[52] table: C cold ​ ( T ) = T 10 6 ⋅ P write C_{\text{cold}}(T)=\frac{T}{10^{6}}\cdot P_{\text{write}}

[53] p: The one-time penalty and per-turn savings are:

[54] table: Δ penalty \displaystyle\Delta_{\text{penalty}} = C cold ​ ( T post ) − C ⁡ ( T pre , h ) \displaystyle=C_{\text{cold}}(T_{\text{post}})-C(T_{\text{pre}},h) Δ savings \displaystyle\Delta_{\text{savings}} = C ⁡ ( T pre , h ) − C ⁡ ( T post , h ) \displaystyle=C(T_{\text{pre}},h)-C(T_{\text{post}},h)

[55] p: Break-even occurs at turn n ∗ n^{*} , where turn 1 is the initial cold-cache turn:

[56] table: n ∗ = ⌈ Δ penalty Δ savings ⌉ + 1 n^{*}=\left\lceil\frac{\Delta_{\text{penalty}}}{\Delta_{\text{savings}}}\right\rceil+1

[57] h3: 4.2 Methodology

[58] p: We scanned sessions from a single user’s Claude Code installation (running Claude Opus 4.6) over a three-month period, excluding internal subagent sessions and sessions with fewer than 10 messages or 5,000 tokens, yielding 76 qualifying sessions. Sessions were categorised by bloat profile based on tool result bytes as a proportion of total JSONL bytes: mixed ( ≥ 15 % \geq 15\% ) and conversational ( < 15 % <15\% ). Token counts are derived from byte counts via a chars/4 heuristic plus a fixed system overhead estimate. This overestimates reduction for image-heavy sessions, where the API charges a fixed vision-token cost ( ∼ \sim 1,600 tokens) independent of base64 encoding size; text-dominated sessions (the majority of the corpus) are unaffected. We assume a steady-state cache hit rate of h = 0.9 h=0.9 and report results under Opus 4.6 pricing. Break-even values are capped at 60 turns as a practical planning horizon; sessions with negligible reduction yield arbitrarily large raw break-even values that are not operationally meaningful.

[59] h3: 4.3 Results

[60] p: Table 1 shows the pricing model used for the primary analysis. Table 2 summarises overall trimming results, and Table 3 segments results by session bloat profile.

[61] figure: Table 1: API pricing per million tokens as of February 2026. Cache write cost is 1.25 × 1.25\times base input. Break-even results scale linearly across pricing tiers. Model Base Input Cache Write Cache Read Opus 4.6 $5.00 $6.25 $0.50

[62] figure: Table 2: Trimming results across 76 sessions from a single API-key user (Opus 4.6, h = 0.9 h=0.9 ). Column extrema are independent; the 0% minimum reduction yields the 60-turn cap, while the 1-turn minimum break-even corresponds to the session with maximum reduction. The negative minimum penalty arises when the trimmed session is small enough that its cold-cache cost is lower than the pre-trim steady-state cost. Metric Min Median Mean Max Token reduction (%) 0 12 20 86 Cache miss penalty ($) − - 0.02 0.32 0.30 0.82 Break-even (turns, Opus 4.6) 1 38 35 60

[63] figure: Table 3: Trimming results segmented by session bloat profile (tool result bytes as % of total JSONL bytes). Bloat Profile Sessions Mean Red. Median Red. Mean Break-even Mean Context Mixed ( ≥ \geq 15%) 12 39% 33% 10 turns 97k Conversational ( < < 15%) 64 17% 10% 40 turns 82k All sessions 76 20% 12% 35 turns 84k

[64] p: Figure 2 shows the distribution of token reduction across sessions. The majority of sessions are conversational with modest trim gains, but a long tail of sessions with significant trimmable overhead achieves reductions of 40–86%. Figure 3 shows the relationship between reduction and break-even: sessions above 30% reduction reach break-even within 15 turns. The highest-reduction sessions (60–86%) are driven primarily by pre-compaction history skipping rather than tool result stubbing, indicating two distinct reduction modes: sessions that accumulated large pre-compaction logs benefit from boundary detection, while mixed-profile sessions benefit from tool output and metadata stripping.

[65] figure: Figure 2: Distribution of token reduction across 76 sessions, segmented by bloat profile. The median reduction is 12%; the mean is pulled higher (20%) by a tail of sessions with significant trimmable overhead.

[66] figure: Figure 3: Break-even turns vs. token reduction. Sessions with > > 30% reduction reach break-even within 15 turns. Sessions with minimal overhead cluster at the 60-turn cap, correctly indicating trimming is unnecessary.

[67] figure: Figure 4: Cumulative input cost with and without trimming. The highlighted session (46% reduction) reaches break-even at turn 6. Faint lines show other sessions; sessions with greater reduction diverge earlier, while sessions with minimal reduction show negligible separation.

[68] p: Figure 4 illustrates cumulative input cost for a representative session with 46% reduction. The trimmed session incurs a higher first-turn cost (cold cache), but the lower per-turn rate causes the curves to diverge, with break-even at turn 6. Faint lines show other sessions in the corpus; the spread reflects the range of reduction percentages.

[69] p: The composition of context varies substantially across sessions (Figure 5 ). In some sessions, tool results and file history account for over 40% of JSONL bytes; in others, the conversation itself dominates. This explains the bimodal trim distribution: the trimmer can only remove what is there to remove.

[70] figure: Figure 5: Context composition by session. Green represents conversation content (preserved by trimming); red, orange, purple, and blue represent trimmable overhead. Sessions with more overhead see larger reductions.

[71] p: For flat-rate subscription users, per-token costs do not apply. Trimming serves purely as a context window optimisation. While there is no direct financial penalty, it significantly extends effective session length by reducing the per-turn token footprint, which otherwise causes rate limits to deplete rapidly when repeatedly sending large, untrimmed contexts.

[72] h3: 4.4 Context Rebuilding: The Unquantified Cost

[73] p: The trimming analysis above captures only the marginal savings from reducing an existing session’s token count. In practice, the dominant cost avoided by CMV is not trimming but context rebuilding : the tokens, time, and output cost required to reconstruct a codebase mental model from scratch when starting a new session. The mean session in our corpus contains 84k tokens of accumulated state. Rebuilding this understanding from a blank session requires the model to re-read files, re-derive architectural relationships, and re-establish conventions—a process that in observed usage takes 10–20 user turns and 15–30 minutes of wall-clock time, with cumulative input costs growing quadratically as each turn re-sends the expanding prefix.

[74] p: Branching from a snapshot eliminates this cost entirely: the model receives the full prior context in a single prompt load ($0.53 at cache-write rates for an 84k-token session under the pricing in Table 1 , dropping to $0.04 on subsequent cache hits). This is the primary value proposition of the DAG model, and it is orthogonal to trimming. The evaluation in this section quantifies trimming because it is the component with a measurable trade-off (cache invalidation penalty vs. per-turn savings). The branching benefit—avoiding context rebuilding altogether—is harder to measure in a controlled setting but dominates the user-perceived value in practice.

[75] h2: 5 Limitations and Future Work

[76] p: The most significant limitation of our approach is that CMV’s trimming is entirely structural rather than semantic. It removes content blindly by type (tool outputs, images, metadata) without assessing its downstream importance to the model’s reasoning. If a stripped tool result is needed for subsequent reasoning, the model may hallucinate its contents or request a re-read. This is mitigated by two design choices: first, trims are applied at branch points where the new branch typically has different information needs than the source session; second, the algorithm preserves the model’s own synthesis of tool outputs verbatim, so while the raw 847-line file dump is removed, the model’s architectural summary of that file remains in the conversation. We have not yet quantified the impact on downstream reasoning accuracy in a controlled setting.

[77] p: More broadly, the need for CMV points to a missing abstraction in current systems. AIOS ( Mei et al., 2025 ) proposes an LLM Agent Operating System that embeds language models into the OS layer, with kernel-level services for scheduling, context management, memory, and access control. Their architecture treats LLM instances as cores (analogous to CPU cores) and agent requests as system calls. This is the right direction, but the specific problem of persistent, version-controlled conversational state across sessions remains underspecified in their framework. AIOS provides context snapshot and restoration within a single agent lifecycle; it does not address named branching points, DAG-based lineage, or conversationally lossless trimming of accumulated session state. CMV provides empirical evidence for this gap. The fact that context reuse, branching, and trimming had to be built in userland on top of JSONL files and filesystem copies motivates the inclusion of persistent conversational state management as a first-class concern in future agent OS designs.

[78] p: The evaluation is a single-user case study; results may not generalise across usage patterns, codebases, or programming styles. The byte-to-token estimation used in the benchmark overestimates reduction for image-heavy sessions due to the discrepancy between base64 encoding size and API vision-token cost. Future work includes: (1) controlled comparisons of trimmed vs. untrimmed branches given identical follow-up tasks to quantify any downstream reasoning degradation; (2) multi-user evaluation across diverse usage patterns; (3) adaptive trim thresholds informed by auto-trim log data; and (4) exploration of how CMV’s DAG state model and trimming algorithm might serve as a reference implementation for the persistent context subsystem in an AIOS-style architecture.

[79] h2: 6 Conclusion

[80] p: Contextual memory virtualisation provides a principled framework for treating LLM conversational state as a persistent, version-controlled resource rather than ephemeral session data. The DAG-based state model enables context reuse patterns (branching, chaining, team sharing) that are impossible under the current session-per-task paradigm. The three-pass trimming algorithm achieves significant token reduction while maintaining both conversational completeness and API correctness. Economic analysis confirms viability. API users recover the prompt caching penalty within a small number of turns, and subscription users gain pure context window savings. Ultimately, as agents are deployed for increasingly complex, multi-day tasks, routinely discarding hours of accumulated context due to window limits becomes an unacceptable overhead. CMV shows that we do not need to wait for model-level breakthroughs or endlessly expanding context windows to fix this; we can solve context ephemerality right now at the tooling layer.

[81] h2: References

[82] h2: Instructions for reporting errors

[83] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[84] p: Tip: You can select the relevant text first, to include it in your report.

[85] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[86] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
