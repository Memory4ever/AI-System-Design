[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning

[3] h6: Abstract

[4] p: Long-running agentic tasks, such as deep research, require multi-hop reasoning over information distributed across multiple webpages and documents. In such tasks, the LLM context is dominated by tokens from external retrieval, causing memory usage to grow rapidly and limiting decode performance. While several KV cache compression techniques exist for long-context inputs, we find that existing heuristics fail to support multi-step reasoning models effectively. We address this challenge with SideQuest – a novel approach that leverages the Large Reasoning Model (LRM) itself to perform KV cache compression by reasoning about the usefulness of tokens in its context. To prevent the tokens associated with this management process from polluting the model’s memory, we frame KV cache compression as an auxiliary task executed in parallel to the main reasoning task. Our evaluations, using a model trained with just 215 215 samples, show that SideQuest reduces peak token usage by up to 65 % 65\% on agentic tasks with minimal degradation in accuracy, outperforming heuristic-based KV cache compression techniques.

[5] p: NVIDIA

[6] p: {skariyappa, esuh}@nvidia.com

[7] h2: 1 Introduction

[8] p: The evolution of Large Language Models (LLMs) from static conversational interfaces to autonomous agents has catalyzed a shift toward long-running, multi-hop reasoning tasks. In applications such as deep research, automated software engineering, and complex workflow orchestration, models must synthesize information distributed across numerous retrieved documents and intermediate thought traces. This shift has fundamentally changed the memory profile of LLM inference; rather than processing a single prompt, agents maintain a growing context that can span hundreds of thousands of tokens over the course of a single task.

[9] p: The primary bottleneck for scaling these agentic workloads is the Key-Value (KV) cache. The KV cache grows linearly with sequence length, posing two critical challenges for efficient inference. First, it consumes a significant and increasing fraction of GPU memory, which reduces the effective batch size and limits the number of concurrent requests a system can service. Second, as the cache grows, the attention mechanism becomes increasingly memory-bandwidth bound, as the GPU must load a massive volume of KV tensors to generate a single new token ( Fu, 2024 ) .

[10] p: To alleviate these pressures, the community has introduced KV cache compression, which aims to bound the memory footprint by retaining only a subset of the most important tokens in the context. Existing approaches largely rely on fixed heuristics to decide which entries to evict. For instance, techniques like H 2 ​ O H_{2}O ( Zhang et al., 2023 ) and Scissorhands ( Liu et al., 2023 ) identify Heavy Hitters —tokens that consistently receive high attention scores—and preserve them while pruning others. Other methods, such as SnapKV ( Li et al., 2024 ) , automatically identify and retain clusters of key information within local attention windows to preserve essential context. These methods operate on the premise that a token’s past importance is a reliable proxy for its future relevance.

[11] p: However, we observe that these existing techniques are ill-suited for the dynamic nature of agentic reasoning. Current KV cache compression methods are largely designed for settings where a fixed long-context corpus (e.g., a book or a legal document) is queried by a user. In contrast, agentic workloads involve a context that evolves over time as the model performs multiple rounds of tool-calling and internal reflection. In these scenarios, heuristic-based pruning is often too blunt a tool; a low-importance token in an early reasoning step may suddenly become critical for a synthesis step ten turns later. The imperfect nature of these heuristics can lead to the premature pruning of important information, resulting in reasoning failures that are difficult to debug.

[12] p: In this paper, we propose SideQuest , a novel approach that shifts KV cache management from a fixed heuristic to an intelligent, model-driven process. SideQuest equips the model with a mechanism to selectively clear segments of its own KV cache, effectively allowing the model to perform its own memory garbage collection. To ensure that the overhead of this self-management does not interfere with the primary task, we frame KV cache compression as an auxiliary task executed in parallel to the main reasoning process (Fig. 1 c). This architecture prevents the management tokens from polluting the model’s primary attention window while maintaining a lean, high-fidelity KV cache. We make the following key contributions in this paper.

[13] p: Evaluation of Heuristic-Based Methods: We measure the efficacy of heuristics based KV cache compression techniques on multi-step agentic workloads to show that static importance metrics fail to capture the dynamic, non-monotonic utility of tokens in multi-step reasoning.

[14] p: Model-Driven Memory Management: We introduce SideQuest , a novel framework that empowers Large Reasoning Models (LRMs) to actively manage their own context. By leveraging the model’s semantic understanding of the task state, SideQuest performs self-referential KV cache eviction to remove obsolete information.

[15] p: Low-Overhead Parallel Reasoning: We propose a shared-context parallel reasoning architecture that executes auxiliary tasks—such as memory management—concurrently with the main reasoning thread. This design allows for intelligent intervention without polluting the primary context window with management tokens.

[16] p: Training Methodology: We develop a scalable data synthesis pipeline that uses hindsight analysis on reasoning traces to generate high-quality supervision. This allows us to train the model to recognize stale information without requiring expensive human annotation.

[17] p: We demonstrate that SideQuest achieves up to 60% reduction in KV cache usage on complex agentic benchmarks with negligible degradation in accuracy, establishing a superior efficiency-utility trade-off compared to existing heuristic based techniques.

[18] figure: Figure 1 : Walkthrough example of SideQuest. (a) The main thread processes the user request by performing multi-turn reasoning and tool calling. (b) At regular intervals we spawn an auxiliary thread that runs in parallel with the shared context (c) The auxiliary thread reflects on the context and lists the cursors that can be deleted. (d) We clear the messages in the context by invoking a tool, reducing the context size for future turns.

[19] h2: 2 Related Work

[20] p: To mitigate the computational and memory overhead of long-context inference, the community has proposed various architectural and algorithmic optimizations. We provide a brief overview of these techniques in this section. Additional related work can be found in Appendix C

[21] h3: 2.1 Architectural Optimizations

[22] p: Architectural innovations aim to reduce the inherent size of the KV state at the model-design level. Grouped-Query Attention (GQA) ( Ainslie et al., 2023 ) and Multi-Head Latent Attention (MLA) ( Liu et al., 2024 ) reduce memory footprint by sharing key and value heads across multiple query heads, significantly lowering the per-token storage cost. Furthermore, alternatives to the standard attention layer, such as Mamba ( Gu and Dao, 2024 ) and Gated Delta Layers ( Yang et al., 2024 ) , have been proposed to achieve sub-linear memory growth. These are often interleaved with standard attention layers to create hybrid models (e.g. Qwen3-Next ( Qwen-Team, 2025 ) , Nemotron-3 ( NVIDIA, 2025 ) ) that balance long-range dependency modeling with inference efficiency. While these methods reduce the rate of memory consumption, they do not address the problem of managing the historical context that accumulates during multi-turn agentic reasoning.

[23] h3: 2.2 Sparse Attention Techniques

[24] p: Sparse attention aims to reduce the memory bandwidth bottleneck by attending to only a subset of tokens in the context. For instance, DeepSeek Sparse Attention (DSA) ( Liu et al., 2025 ) utilizes a lightning indexer to dynamically identify and attend to the most relevant tokens for a given query. While such techniques effectively reduce the pressure on memory bandwidth during the attention computation, they typically do not reduce the physical storage requirements of the KV cache; the full context remains resident in memory, even if only a fraction is accessed during decode.

[25] h3: 2.3 KV Cache Management and Eviction

[26] p: Closest to our work are KV cache eviction techniques that prune unimportant entries to bound the memory footprint. StreamingLLM and H 2 ​ O H_{2}O ( Zhang et al., 2023 ) utilize static heuristics, such as keeping attention sinks or heavy hitter tokens based on cumulative attention scores. SnapKV ( Li et al., 2024 ) further optimizes this by identifying key information clusters within an attention window.

[27] p: Recent work has extended these efforts to specifically target reasoning models. R-KV ( Cai et al., 2025 ) leverages the notion of redundancy to determine which reasoning tokens can be safely discarded. RaaS ( Hu et al., 2025 ) introduces the concept of milestone tokens —intermediate steps critical for logical progression—and prioritizes their retention. Similarly, LazyEviction ( Zhang et al., 2025b ) selectively retains thought tokens that demonstrate recurrent importance during the reasoning process, while ThinKV ( Ramachandran et al., 2025 ) employs a hierarchical approach, categorizing tokens to guide selective quantization and pruning based on their importance levels. Crucially, however, these reasoning-focused methods predominantly target single-step Chain-of-Thought (CoT) tasks, where the context is static and the goal is a single final answer.

[28] p: These methods face a fundamental limitation in agentic settings: heuristic rigidity . In multi-step agentic workflows, a token’s importance is highly dynamic. A piece of information that appears irrelevant in turn t t (resulting in low attention scores) may become the critical pivot for turn t + n t+n . Because existing heuristics lack semantic awareness of the agent’s high-level goals and evolving state, they risk irreversibly pruning information that is vital for downstream reasoning steps.

[29] h2: 3 SideQuest

[30] p: SideQuest is designed for agentic workloads that require multi-step reasoning to resolve complex user queries. These tasks typically employ the ReAct framework, where the model interleaves reasoning traces (thought) with external actions (tool calls) to progressively gather information.

[31] p: To illustrate the memory profile of such tasks, consider the example in Fig. 1 . Given a user query about “long weekends after GTC 2026”, the model must perform multiple distinct steps: determining the submission date, finding a calendar of holidays, and synthesizing the final answer. Each step generates tool outputs—such as search results or webpage content—that are appended to the context.

[32] p: Goal. Our primary objective is to identify stale tool calls and associated responses that have lost their utility and evict associated tokens from context as early as possible during the execution of the ReAct agent 1 1 1 We only focus on tool calls and associated responses (referred collectively as “tool response”) as they occupy a significant fraction of the context in the benchmarks that we consider. .

[33] p: Why is this challenging? The utility of a tool response is highly dynamic and non-monotonic, making it difficult to track with simple heuristics. For example, in Fig. 1 , the initial search results (Cursor 0) become obsolete the moment the model successfully retrieves the specific webpage containing the conference dates (Cursor 1). It can be safely deleted immediately. In contrast, Cursor 1 undergoes a more complex transition. It is critical to identify the dates of the conference (Mar 16-19), but it becomes temporarily irrelevant during the subsequent search for “long weekends”. However, unlike the search results, Cursor 1 regains utility at the end of the task when the model must cite its sources in the final response. Standard attention-based heuristics often fail to capture these semantic shifts, leading to either the retention of useless noise (wasteful) or the premature eviction of useful information (harmful).

[34] p: How SideQuest solves this challenge. Instead of relying on proxy metrics like attention scores, SideQuest leverages the inherent reasoning capabilities of the LRM itself. By analyzing the current state of the ReAct loop and the specific problem definitions, the model explicitly determines which tool responses are no longer needed.

[35] h3: 3.1 Overview

[36] p: SideQuest integrates directly with the ReAct framework to provide a mechanism for self-referential context management. As shown in Figure 1, the architecture operates by periodically spawning an auxiliary thread that executes in parallel with the main thread on the same shared context. The workflow proceeds as follows:

[37] p: Parallel Execution: At regular intervals, SideQuest forks the generation process ( 1 b). The auxiliary thread analyzes the history of open tool outputs (e.g., Cursors [0, 1]) relative to the current reasoning step.

[38] p: Staleness Reasoning: The model produces a dedicated reasoning trace to determine which inputs are redundant. In the example, it recognizes that because the conference dates were successfully found in Cursor 1, the search results page (Cursor 0) is no longer required.

[39] p: Eviction: The auxiliary thread outputs a structured command, such as {del_cursors: [0]} , flagging specific KV cache entries for removal.

[40] p: Synchronization: To prevent disrupting the main thread’s generation, the system waits for the current turn of the main thread to complete before evicting the tool responses that are marked for deletion.

[41] p: A more formal description of SideQuest’s operation is provided in Algorithm 1 .

[42] figure: Algorithm 1 Operation of SideQuest 0: User Query Q Q , Model ℳ \mathcal{M} , Trigger Interval K K , Trigger Phrase p p 1: Initialize context 𝒞 ← [ Q ] \mathcal{C}\leftarrow[Q] 2: Initialize turn counter t ← 0 t\leftarrow 0 3: Initialize auxiliary thread 𝒮 thread ← None \mathcal{S}_{\text{thread}}\leftarrow\text{None} 4: while True do 5: // Phase 1: Eviction 6: if 𝒮 thread ≠ None \mathcal{S}_{\text{thread}}\neq\text{None} and 𝒮 thread . is_finished ​ ( ) \mathcal{S}_{\text{thread}}.\text{is\_finished}() then 7: Δ ids ← 𝒮 thread . get_output ​ ( ) \Delta_{\text{ids}}\leftarrow\mathcal{S}_{\text{thread}}.\text{get\_output}() 8: 𝒞 . clear_kv ​ ( Δ ids ) \mathcal{C}.\text{clear\_kv}(\Delta_{\text{ids}}) // Prune stale tool outputs from cache 9: 𝒮 thread ← None \mathcal{S}_{\text{thread}}\leftarrow\text{None} 10: end if 11: // Phase 2: Auxiliary Thread Spawning 12: if t ( mod K ) = 0 t\pmod{K}=0 and 𝒮 thread = None \mathcal{S}_{\text{thread}}=\text{None} then 13: 𝒞 aux ← 𝒞 + p \mathcal{C}_{\text{aux}}\leftarrow\mathcal{C}+p // Append trigger phrase 14: 𝒮 thread ← AsyncGenerate ​ ( ℳ , 𝒞 aux ) \mathcal{S}_{\text{thread}}\leftarrow\textsc{AsyncGenerate}(\mathcal{M},\mathcal{C}_{\text{aux}}) 15: end if 16: // Phase 3: Main ReAct Execution 17: R ← ℳ ⁡ ( 𝒞 ) R\leftarrow\mathcal{M}(\mathcal{C}) 18: 𝒞 ← 𝒞 + R \mathcal{C}\leftarrow\mathcal{C}+R 19: if R R contains Final Answer then 20: return R R 21: end if 22: if R R contains Tool Call T T then 23: O ← ExecuteTool ​ ( T ) O\leftarrow\textsc{ExecuteTool}(T) 24: 𝒞 ← 𝒞 + O \mathcal{C}\leftarrow\mathcal{C}+O 25: else 26: break //End of turn if no tool called 27: end if 28: t ← t + 1 t\leftarrow t+1 29: end while

[43] p: Advantages of Parallel Execution. We chose a parallel thread architecture over a sequential approach (performing the user and memory management task in the main thread) for two reasons. First, interleaving memory management steps into the main thread would significantly increase latency, delaying the primary task. Second, explicit management tokens would pollute the context window, partially negating the benefits of compression. By isolating this logic in a transient parallel thread, SideQuest maintains a pristine context for the main agent.

[44] h3: 3.2 Steering the Model to Perform Auxiliary Task

[45] p: In standard multi-turn reasoning, models are conditioned to solve the user’s initial prompt. SideQuest requires a mechanism to override this behavior in the auxiliary thread, shifting the model’s focus from answering the user’s query to managing the context. We achieve this through a two-pronged steering strategy:

[46] p: Contextual Trigger: We append a distinct trigger phrase, ** Memory management mode ** , to the start of the auxiliary thread. This serves as a strong indicator to the model that it has entered a maintenance subroutine.

[47] p: Task-Specific Fine-Tuning: We train the model to recognize this trigger and output the expected deletion commands. This ensures that even when the main context contains complex reasoning about the user’s query, the presence of the trigger successfully switches the model’s output distribution to focus on analyzing the utility of tool responses.

[48] h3: 3.3 Generating Training Data

[49] p: To equip the model with memory management capabilities without degrading its general reasoning performance, we construct a hybrid training dataset composed of two types of data: main traces (for preserving capability) and auxiliary traces (for learning eviction). The complete pipeline is formalized in Algorithm 2 .

[50] p: Hindsight Annotation. The core of our data generation relies on hindsight analysis. We start by running inference on a dataset of web-browsing tasks using a base policy (the original model). We filter for traces that lead to correct answers to ensure high-quality supervision. For every tool output (cursor) in a correct trace, we compute its last-use index (Line 9). A cursor is considered ‘‘expired” at any given turn if it is never referenced again in the future either by tool calls or the final answer 2 2 2 This is a simplifying assumption to help with annotation. In reality it is possible that the model uses the information in a tool response without referencing the cursor in some cases. .

[51] p: Main Traces (Distillation). To prevent catastrophic forgetting of the model’s primary reasoning skills, we include the original correct traces in the training set. For these samples, we extract the logits from the base policy (Line 10). During training, we apply a logit distillation loss ( Hinton et al., 2015 ) to these entries. This forces the SideQuest model to match the probability distribution of the original model, ensuring that the introduction of memory management tokens does not alter the model’s behavior on standard tasks.

[52] p: Auxiliary Traces (Cross-Entropy). We synthesize auxiliary traces to teach the model how to identify stale tool responses. At fixed intervals along the trace (Line 15), we identify the set of expired cursors. To simulate realistic inference conditions where the cache is partially compressed, we randomly partition these expired cursors into two sets.

[53] p: Simulated Eviction: We mask out the tokens corresponding to evicted cursors (Line 16), presenting the model with a context where some eviction has already occurred.

[54] p: Target Generation: We prompt an annotation model (Line 19) to generate reasoning that explains why the remaining cursors are stale, followed by the requisite deletion command. The prompt used for annotation is provided in Appendix A .

[55] p: We prepend the trigger phrase to these sequences and use them to train the model using standard Cross-Entropy loss.

[56] p: Joint Optimization. The final model is trained on the union of these datasets using a weighted average of the two objectives ℒ = ℒ CE ​ ( 𝒟 aux ) + λ ​ ℒ distill ​ ( 𝒟 main ) \mathcal{L}=\mathcal{L}_{\text{CE}}(\mathcal{D}_{\text{aux}})+\lambda\mathcal{L}_{\text{distill}}(\mathcal{D}_{\text{main}}) . This joint optimization ensures the model learns to enter the auxiliary mode strictly when triggered, while retaining the robust reasoning capabilities of the base model for the main task.

[57] figure: Algorithm 2 Training Data Pipeline 0: Dataset 𝒟 \mathcal{D} , base policy π \pi , annotation model ℳ \mathcal{M} , interval k k , trigger phrase p p 1: 𝒟 train ← ∅ \mathcal{D}_{\text{train}}\leftarrow\emptyset 2: for each task x ∈ 𝒟 x\in\mathcal{D} do 3: τ ← RunInference ​ ( π , x ) \tau\leftarrow\textsc{RunInference}(\pi,x) 4: if IsCorrect ​ ( τ ) = false \textsc{IsCorrect}(\tau)=\texttt{false} then 5: continue 6: end if 7: // Annotate each cursor with its last-use turn index 8: for each cursor c c in τ \tau do 9: ℓ c ← LastUseIndex ​ ( τ , c ) \ell_{c}\leftarrow\textsc{LastUseIndex}(\tau,c) 10: end for 11: // Add main trace with full attention and logits 12: 𝐳 ← π ⁡ ( τ ) \mathbf{z}\leftarrow\pi(\tau) // Extract logits from base policy 13: 𝒟 train ← 𝒟 train ∪ { ( τ , 𝐈 , 𝐳 , main ) } \mathcal{D}_{\text{train}}\leftarrow\mathcal{D}_{\text{train}}\cup\{(\tau,\mathbf{I},\mathbf{z},\texttt{main})\} 14: // Generate auxiliary traces at intervals 15: for each reasoning turn t t where t mod k = 0 t\mod k=0 do 16: 𝒞 expired ← { c : ℓ c < t } \mathcal{C}_{\text{expired}}\leftarrow\{c:\ell_{c}<t\} // Cursors past last-use 17: 𝒞 open , 𝒞 closed ← RandomPartition ​ ( 𝒞 expired ) \mathcal{C}_{\text{open}},\mathcal{C}_{\text{closed}}\leftarrow\textsc{RandomPartition}(\mathcal{C}_{\text{expired}}) 18: 𝐌 ← BuildMask ( τ 1 : t , 𝒞 closed ) \mathbf{M}\leftarrow\textsc{BuildMask}(\tau_{1:t},\mathcal{C}_{\text{closed}}) // Mask out closed cursors 19: r ← ℳ ( τ 1 : t , 𝒞 open , 𝒞 closed ) r\leftarrow\mathcal{M}(\tau_{1:t},\mathcal{C}_{\text{open}},\mathcal{C}_{\text{closed}}) // Generate reasoning 20: r ← p ⊕ r r\leftarrow p\oplus r // Prepend trigger phrase 21: τ aux ← τ 1 : t ⊕ [ r , CloseAction ( 𝒞 open ) ] \tau_{\text{aux}}\leftarrow\tau_{1:t}\oplus[r,\textsc{CloseAction}(\mathcal{C}_{\text{open}})] 22: 𝒟 train ← 𝒟 train ∪ { ( τ aux , 𝐌 , ∅ , aux ) } \mathcal{D}_{\text{train}}\leftarrow\mathcal{D}_{\text{train}}\cup\{(\tau_{\text{aux}},\mathbf{M},\varnothing,\texttt{aux})\} 23: end for 24: end for 25: return 𝒟 train \mathcal{D}_{\text{train}}

[58] h3: 3.4 Overheads of SideQuest

[59] p: Storage Costs. The auxiliary thread operates on the shared context of the main thread, meaning it does not duplicate the large KV cache of the conversation history. The only additional storage cost arises from the transient tokens generated during the auxiliary reasoning phase. Once the thread concludes and the deletion targets are identified, these tokens are discarded, ensuring that SideQuest introduces zero permanent token overhead to the main context.

[60] p: Compute and Memory Movement Cost. Executing an auxiliary thread naturally incurs additional computational and memory bandwidth overhead. However, long-context agentic workloads are predominantly bottlenecked by memory bandwidth rather than compute capacity. Although the auxiliary thread imposes a transient cost, we demonstrate empirically that this investment yields a net reduction in resource consumption. By proactively pruning voluminous tool responses—often spanning hundreds of tokens—SideQuest significantly reduces the cumulative memory movement required for all subsequent reasoning turns.

[61] p: Furthermore, this overhead can be minimized by leveraging optimizations for shared-context inference. Techniques such as Cascade Inference ( Ye et al., 2024 ) and FastTree ( Pan et al., 2025 ) introduce specialized kernels that decouple attention computation for shared prefixes from unique suffixes. Since the Main and Auxiliary threads share the vast majority of their context history, these methods can eliminate redundant memory loads, allowing the auxiliary task to be executed with negligible marginal cost.

[62] h2: 4 Experiments

[63] h3: 4.1 Datasets

[64] p: We focus our evaluation on two long-context, multi-turn web browsing tasks that require agents to synthesize information across multiple retrieval steps. As illustrated in Figure 2 , these tasks are characterized by long reasoning chains and extensive context windows often exceeding 100k tokens.

[65] figure: Figure 2 : Distribution of ReAct Iterations and token count for FRAMES and BrowseComp with gpt-oss-20b (medium effort).

[66] figure: Figure 3 : Efficiency vs. Utility Trade-off. We evaluate Accuracy against Peak Token Usage and KV cache memory reads for gpt-oss-20b with Medium and High reasoning effort, on the FRAMES and BrowseComp benchmarks. The Uncompressed Baseline establishes the upper bound for accuracy but incurs the highest memory cost. SideQuest achieves substantial memory savings—reducing peak token usage by 56-65% compared to the baseline—while providing a better accuracy compared to heuristic based methods.

[67] p: FRAMES ( Krishna et al., 2024 ) . FRAMES evaluates a model’s ability to perform retrieval and multi-hop reasoning over Wikipedia articles. To simulate a realistic scale, we utilize a corpus of 6.4 million Wikipedia articles ( Wikimedia, ) . To ensure solvability, we augment this corpus with the specific articles containing the ground truth for each FRAMES query. We report our metrics on 424 samples from this dataset.

[68] p: BrowseComp ( Wei et al., 2025 ) . This dataset tests the ability to navigate the web to find specific, hard-to-locate information. It features difficult user queries with short, verifiable answers. To ensure a fair and reproducible comparison, we utilize the corpus from BrowseComp-Plus ( Chen et al., 2025 ) . This provides a fixed set of 100 100 k documents containing both the necessary supporting evidence and challenging negative distractors, simulating a realistic retrieval environment. We report results on a subset of 500 samples from this dataset.

[69] p: For both benchmarks, we implement a local server that exposes search and retrieval APIs (e.g., search() , open() ) backed by the respective corpora. This setup serves as the backend for the browser tool, ensuring deterministic evaluation by removing the variability of live web results. To facilitate effective retrieval within this environment, we employ the Qwen3-Embedding-8B ( Zhang et al., 2025c ) model to generate dense vector embeddings for all webpages in the corpus.

[70] h3: 4.2 Models

[71] p: We conduct experiments using the gpt-oss-20b ( OpenAI, 2025 ) model. This model is natively trained with a browser tool that indexes all tool outputs with unique cursor identifiers (e.g., [Cursor 0] ). This cursor-based indexing is central to our method, as it allows SideQuest to perform granular, object-level eviction of search results and web/document content. It also facilitates the automated collection of training data for the auxiliary task, as detailed in Section 3.3 . We report results for this model under both Medium and High reasoning effort configurations.

[72] h3: 4.3 Training

[73] p: To construct our training corpus, we sampled 400 tasks from the FRAMES ( Krishna et al., 2024 ) dataset. After filtering for traces that resulted in correct answers, we obtained 215 high-quality samples. We then applied the data generation pipeline described in Section 3.3 (Algorithm 2 ) using gpt-oss-120b as the annotation model ℳ \mathcal{M} and an interval of k = 4 k=4 . This process yielded a dataset comprising 215 main traces and 1274 auxiliary traces. To balance the dataset and preserve the model’s core reasoning capabilities, we upsampled the main traces by a factor of 3 × 3\times . We fine-tuned the gpt-oss-20b model using LoRA ( Hu et al., 2021 ) for 3 epochs with a learning rate of 2 × 10 − 4 2\times 10^{-4} and a distillation loss weight of λ = 500 \lambda=500 . The LoRA configuration used rank r = 8 r=8 and α = 16 \alpha=16 . To minimize training overhead while retaining capacity, we applied adapters exclusively to a subset of the projection layers ( gate_up_proj, down_proj ) in the Mixture-of-Experts (MoE) layers at depths 7, 15, and 23, keeping all other parameters frozen. Finally, we employed Quantization Aware Training (QAT) during this fine-tuning stage to ensure the final model could be robustly quantized to the mxfp4 format.

[74] figure: Figure 4 : Non-Completion Rate across benchmarks, categorized by failure type: Unparsable Responses (orange), Context Limits (green), and Turn Limits (purple). SideQuest demonstrates superior reliability, matching the near-zero failure rate of the uncompressed baseline, while other methods suffer from high rates of model collapse.

[75] h3: 4.4 Baselines

[76] p: We compare SideQuest against an uncompressed baseline (full attention) and three representative KV cache compression techniques. For all heuristic baselines, we evaluate performance at two token budgets: 16k and 24k tokens.

[77] p: 𝑯 𝟐 ​ 𝑶 \bm{H_{2}O} ( Zhang et al., 2023 ) . A “Heavy Hitter” oracle that retains tokens with the highest cumulative attention scores while evicting others. This represents the standard for frequency-based pruning.

[78] p: SnapKV ( Li et al., 2024 ) . This method identifies and retains clusters of key information within the attention window, aiming to preserve local semantic structure better than individual token pruning.

[79] p: R-KV ( Cai et al., 2025 ) . A reasoning-focused compression technique that scores tokens based on redundancy, pruning those deemed repetitive or non-essential for the current generation step.

[80] p: We implement our compression techniques within the SGLang framework ( Zheng et al., 2024 ) , ensuring full compatibility with prefix caching to enable efficient context reuse across multiple ReAct iterations.

[81] figure: Figure 5 : Serving Performance in SGLang. We compare Sidequest against the uncompressed baseline for gpt-oss-20b (Medium Effort) on the FRAMES benchmark using a single NVIDIA H100 GPU. (Left) Sidequest increases peak throughput by 83.9 % 83.9\% by enabling larger batch sizes. (Center) Peak KV cache usage is reduced by 53.9 % 53.9\% , freeing up significant memory headroom. (Right) The combination of higher concurrency and reduced memory movement lowers total benchmark runtime by 36.8 % 36.8\% .

[82] h3: 4.5 Metrics

[83] p: We evaluate the trade-off between system efficiency and model utility using three primary metrics:

[84] p: Peak Token Utilization: We report the maximum size of the KV cache reached during the execution of a task. This metric serves as a proxy for the worst-case memory capacity requirement, determining the maximum batch size that can be supported on a given GPU.

[85] p: KV Cache Memory Reads: We quantify the total volume of data transfer required by the attention mechanism during the decode phase. As agentic workloads are typically memory-bandwidth bound, this metric directly correlates with end-to-end inference latency and system throughput.

[86] p: Accuracy: We measure the success rate on the FRAMES and BrowseComp benchmarks to assess model utility.

[87] p: To visualize the cost-benefit trade-off, we plot Utility vs. Efficiency curves across both benchmarks under medium and high reasoning efforts, highlighting the Pareto frontier of memory savings versus reasoning performance.

[88] p: Serving Metrics. To evaluate the real-world impact on production systems, we additionally report System Throughput (tokens/second), Normalized KV Cache Usage, and Total Benchmark Runtime by implementing SideQuest in SGLang. These metrics capture the practical efficiency gains in a high-concurrency production-grade environment.

[89] h3: 4.6 Results

[90] p: We present our main experimental results in Figure 3 , plotting the trade-off between model utility (Accuracy) and system efficiency (Peak Token Usage and KV Cache Reads).

[91] p: Efficiency vs. Utility. SideQuest fundamentally shifts the Pareto frontier for agentic memory management. As shown in Figure 3 , SideQuest reduces Peak Token Utilization by 56 − 65 % 56-65\% and KV cache memory reads by 53 − 71 % 53-71\% , compared to the uncompressed baseline. This massive reduction in memory load comes with minimal cost to reasoning performance: we observe only a marginal degradation in accuracy of up to 2 % 2\% on the in-distribution FRAMES benchmark and a 5 % 5\% degradation on the out-of-distribution BrowseComp benchmark. In contrast, heuristic baselines like H 2 ​ O H_{2}O , SnapKV, and R-KV suffer precipitous drops in accuracy at comparable compression levels, failing to maintain the context fidelity required for complex multi-hop reasoning.

[92] p: Failure of Fixed Token Budgets. A key finding from our analysis is the inadequacy of fixed-budget compression for agentic tasks. As illustrated in the token distribution histograms in Figure 2 , there is significant variance in task difficulty, with token counts ranging from a few thousand to over 120k. Fixed-budget methods (e.g., forcing a 16k window) inevitably fail on the long tail of complex queries, while wasting memory on simple ones. Unlike these rigid approaches, SideQuest adaptively adjusts its context size based on the problem’s instantaneous difficulty. By dynamically evicting only the specific cursors that are no longer semantically relevant 3 3 3 See Appendix B for examples of SideQuest’s reasoning. , SideQuest discovers the optimal token budget for each specific query without a priori tuning.

[93] p: Robustness and Coherence. Beyond accuracy, we analyze the reliability of the model’s generation process. Figure 4 reports the Non-Completion Rate, which aggregates failures caused by unparsable/non-terminating responses, context length limits, or non-terminating loops. We find that heuristic baselines exhibit a dangerously high rate of unparsable responses (orange bars). This suggests that heuristic pruning often removes tokens critical for syntactic coherence or logic flow, causing the model to produce meaningless responses. SideQuest, by contrast, maintains a non-completion rate comparable to the uncompressed baseline, ensuring that the aggressive memory savings do not compromise the structural integrity of the agent’s reasoning loop. Note that the lower peak memory usage observed for some baselines in Figure 3 (e.g., BrowseComp-High) is partly an artifact of these early crashes; SideQuest achieves its efficiency gains while successfully running tasks to completion.

[94] h3: 4.7 Serving Efficiency Analysis

[95] p: To validate the real-world impact of our method on production systems, we report various performance metrics using an SGLang-based implementation of SideQuest. We report system throughput, peak KV Cache usage and total runtime by running 424 samples of the FRAMES benchmark with gpt-oss-20b under medium-effort setting. We report these metrics under different levels of concurrency (batch size). As shown in Figure 5 , Sidequest increases peak system throughput by 83.9 % 83.9\% ( 1523 1523 tok/s vs. 828 828 tok/s) compared to the uncompressed baseline, enabling the engine to scale to larger batch sizes (up to 36) without saturating memory. This performance gain is driven by a massive 53.9 % 53.9\% reduction in peak KV cache usage (dropping normalized occupancy from 0.977 0.977 to 0.450 0.450 ), which significantly alleviates the memory bandwidth bottlenecks inherent to long-context agentic workloads. Consequently, Sidequest reduces the total end-to-end benchmark runtime by 36.8 % 36.8\% ( 1489 1489 s vs. 2356 2356 s), demonstrating that our proactive memory management translates directly to faster, more efficient production serving for LRMs.

[96] figure: Figure 6 : The SideQuest framework can be extended to various auxiliary tasks beyond the memory management task.

[97] h2: 5 Limitations

[98] p: While SideQuest demonstrates significant memory savings, we acknowledge two primary limitations in our current implementation. First, although our method closely matches the uncompressed baseline, we observe minor performance degradation, especially for the out-of-distribution BrowseComp dataset. We hypothesize that this is a data scale issue rather than an architectural flaw. Our current model was fine-tuned on a relatively small dataset constructed from only 215 traces. We believe that scaling the training data to include a larger, more diverse distribution would close this remaining gap. Second, our current eviction strategy is scoped exclusively to tool-responses. Unlike heuristic techniques which can prune any token in the sequence, SideQuest does not yet attempt to compress the agent’s own intermediate reasoning steps. Extending our approach to perform thought pruning is a promising future direction of research. Additionally, our method operates at a higher level of abstraction compared to prior works on KV compression that rely on attention weights. Exploring a combination of the two is an interesting avenue for future research.

[99] h2: 6 Future Work

[100] p: New Domains for Memory Management. Our evaluations in this paper are focused on multi-turn web browsing, which serves as an ideal testbed for dynamic context management. However, the principles of SideQuest are domain-agnostic. A promising direction for future research is applying this framework to coding agents, where tasks involve traversing massive codebases and reasoning over long-context dependency graphs. The ability to selectively forget irrelevant file contents while retaining critical function definitions could unlock significant efficiency gains.

[101] p: SideQuest for Other Auxiliary Tasks. While this work explores memory management, the SideQuest architecture—running parallel auxiliary threads on a shared context—has far broader applications. As illustrated in Figure 6 , the same mechanism can be used to steer LRMs to perform various governance and safety tasks in parallel to the main user interaction. It can also be trained to follow a custom instruction that is inserted in the context after a trigger phrase. Currently, these auxiliary tasks (e.g. safety, security, governance) are typically handled by separate, smaller guardrail models. By leveraging SideQuest, these checks can be executed as auxiliary tasks on the shared context. This would allow the primary LRM to apply its full multi-turn context awareness to safety enforcement without incurring the cost of independent context reprocessing.

[102] h2: 7 Conclusion

[103] p: In this work, we demonstrate that static heuristic compression fails to capture the dynamic utility of tokens in long-running agentic tasks. We propose SideQuest, a novel framework that empowers Large Reasoning Models to actively manage their own memory via a parallel auxiliary thread. This architecture allows for precise, semantic-aware eviction of stale tool outputs without interfering with the primary reasoning process. Empirically, SideQuest achieves a reduction of up to 65 % 65\% in peak memory usage with only a minor drop in accuracy, strictly outperforming heuristic baselines. Crucially, our method eliminates the need for manual token budgeting, adaptively scaling context size to match the instantaneous complexity of the query. By transforming memory management from a fixed constraint into a learnable reasoning skill, SideQuest establishes a new paradigm for efficient, long-context agentic inference.

[104] h2: 8 Acknowledgements

[105] p: We thank Shizhe Diao and Yaosheng Fu for their feedback, which has helped shape this work.

[106] h2: References

[107] h2: Appendix A Prompt Used for Generating Auxiliary Traces

[108] p: We use the following prompt for the annotation model to generate reasoning that’s used to construct auxiliary traces as described in Section 3.3 .

[109] h2: Appendix B Examples of Memory Management Reasoning

[110] p: Due to the long nature of the agentic tasks we cannot fit an entire trace within a page. However, we provide some examples of the auxiliary trace produced by SideQuest in Fig. 7 to demonstrate the sophisticated reasoning used in KV cache management.

[111] figure: Figure 7 : Examples of memory-management reasoning produced by SideQuest.

[112] h2: Appendix C Related Works on Agentic Memory Management

[113] h3: C.1 Operating System and Retrieval-Based Approaches

[114] p: Recent works have proposed moving beyond static context windows by drawing inspiration from operating systems. The most prominent example, MemGPT ( Packer et al., 2023 ) , creates a hierarchical memory architecture where the model explicitly manages its own context by swapping text between its active prompt (Main Context) and external storage (External Context) via function calls. Similarly, in the domain of automated software engineering, Cursor has introduced Dynamic Context Discovery ( Katz, 2026 ) , which applies virtualization principles to code generation. Rather than stuffing the context window with static tool definitions and history, Cursor abstracts these elements as files that the agent can lazily load only when necessary.

[115] p: While both MemGPT and Cursor solve the information retrieval problem (deciding what text to show the model), they do not address the inference efficiency problem of linear context growth. Even with dynamic discovery, once information is loaded, it occupies GPU memory linearly. Sidequest complements these methods by operating on the internal state: it allows the model to “garbage collect” the heavy tensors of intermediate reasoning steps without breaking the continuity of the task.

[116] h3: C.2 Hierarchical and Decomposition-Based Context Management

[117] p: Another class of approaches addresses the long-context challenge by restructuring agentic reasoning into hierarchical or recursive formats. Recursive Language Models (RLMs) ( Zhang et al., 2025a ) treat the context as an external environment, allowing the model to write code that inspects, slices, and recursively calls itself on specific data chunks. Similarly, Context Fold ( Sun et al., 2025 ) introduces a dynamic branch-and-fold mechanism where agents can spawn temporary sub-trajectories for specific sub-tasks; upon completion, the entire sub-trajectory is folded into a concise summary, and the intermediate tokens are discarded.

[118] p: Complementarity with Sidequest. These approaches mitigate context growth by isolating intermediate reasoning steps into separate, transient contexts (child processes or branches) and propagating only the final result to the main thread. However, they do not solve the fundamental problem of linear context growth within a specific sub-task. A complex sub-problem (e.g., “fix a failing test”) will still accumulate a massive local context of tool outputs and retrieval artifacts before a result can be returned. Sidequest addresses this orthogonal challenge. By operating as a garbage collector for the active linear stream, Sidequest can be deployed inside the sub-tasks of an RLM or Context Fold architecture. It ensures that the local context of each branch remains lean by surgically evicting stale tool outputs (observations) while preserving the necessary tool outputs. Consequently, Sidequest is highly compatible with structural decomposition methods, offering a mechanism to maximize the efficiency of the individual workers within a hierarchical system.

[119] h2: Instructions for reporting errors

[120] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[121] p: Tip: You can select the relevant text first, to include it in your report.

[122] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[123] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
