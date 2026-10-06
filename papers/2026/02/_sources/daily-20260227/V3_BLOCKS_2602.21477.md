[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Pancake: Hierarchical Memory System for Multi-Agent LLM Serving

[3] h6: Abstract

[4] p: In this work, we identify and address the core challenges of agentic memory management in LLM serving, where large-scale storage, frequent updates, and multiple coexisting agents jointly introduce complex and high-cost approximate nearest neighbor (ANN) searching problems. We present Pancake, a multi-tier agentic memory system that unifies three key techniques: (i) multi-level index caching for single agents, (ii) coordinated index management across multiple agents, and (iii) collaborative GPU–CPU acceleration. Pancake exposes easy-to-use interface that can be integrated into memory-based agents like Mem-GPT, and is compatible with agentic frameworks such as LangChain and LlamaIndex. Experiments on realistic agent workloads show that Pancake substantially outperforms existing frameworks, achieving more than 4.29× end-to-end throughput improvement.

[5] h2: 1 Introduction

[6] p: Agents have emerged as one of the defining paradigms of the LLM era, enabling complex task scenarios including task planning [ 24 , 58 ] , knowledge organization [ 17 , 4 ] , tool-augmented generation [ 57 , 76 ] and even scientific researches [ 64 , 47 ] . These complex tasks, often carried out through multi-turn environment interaction [ 77 ] , self-reflection [ 59 ] , or multi-agent collaboration [ 39 ] , has introduced substantial information into the generation process and poses significant challenges for context length and attention fidelity [ 45 ] .

[7] p: In response to this trend, Agent Memory [ 82 ] has emerged as a key mechanism to manage complex contexts and enhance generation quality. Unlike prior Retrieval-Augmented Generation (RAG) methods [ 4 , 71 , 28 , 37 , 29 , 38 ] , which rely on a static knowledge database and lack the ability to capture an agent’s runtime state, results, and other dynamic information, agent memory maintains an external database that records essential information, including external knowledge [ 53 , 29 ] , action history [ 73 , 88 ] , user profile [ 67 , 20 ] , and more. The agent must retrieve the most relevant memory items to guide generation throughout LLM inference, while also dynamically inserting newly generated items for future reference.

[8] figure: Figure 1 : Memory-based workflow of agentic LLMs.

[9] figure: Figure 2 : An example of multi-agent memory in Pancake.

[10] p: Agent Memory enables reliable, consistent, and progressively refined agent outputs over complex tasks. Yet, such a continuous memory mechanism also introduces a highly dynamic database environment that demands frequent approximate nearest-neighbor (ANN) operations [ 40 ] , typically implemented through embedding vector indexes [ 22 ] . Such operations introduce a new and substantial source of overhead in agent serving when the index scale becomes large.

[11] p: Existing agentic memory implementations largely focus on functional support while lacking performance-oriented optimization. As shown in Figure 1 , for popular memory-based workflows [ 53 , 73 ] , the memory operational cost grows sharply with memory size, reaching more than 82% of the total execution time. Meanwhile, most existing vector database systems fall short in supporting agentic memory: they either optimize only a static index [ 16 , 8 , 25 , 81 , 72 ] , or rely on batch-oriented updates [ 50 , 49 , 74 , 60 ] designed for periodic maintenance in traditional databases [ 63 ] , making them ill-suited for highly dynamic and fine-grained memory operations.

[12] p: In this work, we present Pancake, a multi-tier memory management system designed to address the key challenges of implementing an agentic memory system:

[13] p: First, for a single agent , a key limitation of existing vector search systems is their inability to efficiently handle the frequent, fine-grained updates characteristic of memory workloads [ 53 , 73 ] . Existing incremental indexing methods [ 74 , 49 ] are designed for large-batch insertions in traditional databases [ 63 , 33 ] and rely on direct in-place inserts with periodic rebalancing. Under the small-batch insertion patterns and interleaved search of agent workloads, inserted vectors are often scattered across various clusters due to high-dimensional distance concentration [ 19 ] despite strong semantic coherence, degrading both search efficiency and recall.

[14] p: To address this inefficiency, we explicitly incorporate agent-specific access behaviors into index construction and maintenance. Specifically, Pancake exploits both intra-agent and inter-request locality through a multi-level cache index that progressively promotes related vectors to upper levels, improving search ordering and enabling early termination. To guide caching behavior, Pancake models each agent’s memory access pattern as finite-state machine (FSMs) with continuous updating and merging, enabling index cluster construction closely aligned with the agent’s workload.

[15] p: Second, supporting multi-agent workloads is challenging, as they frequently invoke different sets of agents to perform memory searches at runtime [ 54 ] . Using conventional two-level index structures [ 16 ] while maintaining separate indexes for each agent is inefficient. At the upper level, this design must traverse the coarse index of every agent, even when only a subset is involved in the query, leading to excessive coarse-search overhead. At the lower level, it uses uniform clusters for the shared memory part, ignoring the inconsistent access patterns across agents, thus causing misaligned cluster organization and inefficient fine-grained search.

[16] p: Pancake addresses these challenges with a hybrid graph that connects multiple agents’ indexes into a unified structure, enabling the upper-level coarse search to be performed through a single graph traversal. Pancake also records agent-specific access patterns for each cluster, to reduce cross-agent search overhead caused by inconsistent access patterns.

[17] p: For programmability in multi-agent applications, Pancake provides a simple Python interface that supports operations over arbitrary memory scopes, including different shared and local memory parts, which existing frameworks do not offer. Figure 2 shows a multi-agent code-generation setup, where different agents flexibly operate over knowledge, code, and history memories with Pancake interface.

[18] p: Third, modern LLM serving systems are typically deployed at GPU-CPU platforms [ 35 , 86 ] , which creates an opportunity to accelerate memory operations. Existing vector databases can only reside entirely on the GPU [ 31 , 32 ] , or GPU caching mechanism for static indexes [ 61 , 84 ] . However, in agentic serving scenarios, the coexistence of large-scale memory bases [ 53 ] and LLM inference engine severely restricts available GPU memory. More importantly, the frequent memory updates makes static caching techniques infeasible to apply. To fully utilize resources, Pancake implements CPU–GPU coordinated index management to accelerate hotspot cluster computation, with an insertion buffer design and asynchronous transfers for low-latency online updates.

[19] p: In summary, the contribution of this paper is as follows:

[20] p: We introduce Pancake, the first multi-tier memory management system tailored for multi-agent applications. Pancake exploits agent workload characteristics to optimize update strategy for single-agent memory, cluster construction for multi-agent coordination, and dynamic CPU–GPU collaborative execution.

[21] p: Pancake can be directly integrated into agent workflows like Mem-GPT [ 53 ] and plugged into mainstream agentic frameworks like LangChain [ 36 ] and LlamaIndex [ 44 ] . It provides a concise API through which agents can perform memory operations across flexible memory scopes.

[22] p: Extensive experiments across diverse agent datasets show that Pancake delivers over 4.29 × \times average end-to-end performance speedup compared with existing memory libraries, and reduces the memory-operation time share to an average of 3.2% under large-scale database.

[23] h2: 2 Background and Related Work

[24] h3: 2.1 Memory-based Agent and ANN

[25] p: A memory-based agent typically perform three operations: LLM Generation; Memory Search, which retrieves items relevant to the current context; and Memory Update, which inserts, deletes, or modifies items in the memory store. As shown in Figure 3 , different agent roles induce different operation patterns. For instance, multi-turn dialogue agents search and update memory at every step to remain consistent with the interaction history [ 53 , 78 ] , whereas context-summarization agents search and generate for several rounds and then insert a compressed memory item [ 9 , 52 , 79 ] .

[26] p: These search and update memory operations inherently introduce requirements for approximate nearest neighbor (ANN) queries. ANN is typically implemented through vector databases, where textual information is encoded into vector embeddings [ 66 , 13 ] and relevance is quantized based on vector similarities [ 10 ] . Such ANN queries occur repeatedly throughout an agent’s step-wise generation, their latency and accuracy therefore become increasingly critical to the overall performance of modern LLM serving systems.

[27] p: To support memory operations, existing memory-based agents such as Mem-GPT [ 53 ] and A-Mem [ 73 ] provide their own memory implementations, and open-sourced agent frameworks like LlamaIndex [ 44 ] and LangChain [ 36 ] also offer built-in storage interfaces. However, these modules emphasize functionality and rely on suboptimal indexing and searching implementations. As the memory size grows, their query latency increases sharply, reaching more than 99% of the end-to-end runtime at scale. This trend highlights the need for a scalable and efficient agentic memory framework.

[28] figure: Figure 3 : Memory-based agents and their workflows.

[29] h3: 2.2 Dynamic Vector Database

[30] p: Numerous vector-database frameworks [ 16 , 65 , 8 , 21 , 25 ] have explored techniques for efficient search by organizing vectors into structured storage formats, known as indexes. Among them, the Inverted File (IVF) index [ 26 ] is widely used: it partition vectors into clusters and rank these clusters by the distance between their centroids and the query. Only the top- n ​ p ​ r ​ o ​ b ​ e nprobe clusters are selected for vector-wise search, making n ​ p ​ r ​ o ​ b ​ e nprobe a tunable accuracy–efficiency trade-off [ 56 ] . We refer to cluster selection as coarse search , and to the search within the selected clusters as fine search . Coarse search typically relies on a Flat index or graph-based indexes such as HNSW [ 48 ] or Vamana [ 25 ] in large-scale settings.

[31] p: However, existing frameworks are primarily designed for read-only scenarios like RAG, and therefore assume a static vector database with one-shot, full-index construction. Such designs are incompatible with agentic memory workloads, where frequent updates make reconstruction prohibitively expensive. To support online updates, several dynamic vector-database techniques have been proposed [ 60 , 74 , 50 , 49 , 70 ] . For example, SPFresh [ 74 ] avoids global rebuilding through in-place inserts and lightweight local rebalancing, while Quake [ 50 ] uses a hierarchical cluster structure and adaptively splits clusters based on access frequency. However, these designs typically assume periodic, batch-oriented updates consistent with traditional database workloads [ 34 , 63 ] . In contrast, agentic memory serving involves highly frequent updates that interleave closely with search operations, leading to degraded efficiency and accuracy in such systems.

[32] h2: 3 Motivation

[33] h3: 3.1 Inefficient Update Strategy for Single-Agent Memory Access

[34] p: In this section, we analyze single-agent memory access patterns and show that existing vector database maintenance algorithms struggle to efficiently handle frequent-update workloads. In typical agent-serving systems, an agent processes many independent requests, each involving multi-step LLM generation and frequent interleaved search–insert operations. Examples include coding agents receiving continuous user tasks [ 75 ] and scientific agents analyzing large batches of experimental data [ 80 ] .

[35] p: For vector insertion during memory updates, existing dynamic vector databases [ 50 , 74 , 49 ] typically adopt in-place inserts with periodic updates, as shown in Figure 4 . New vectors are inserted directly into the nearest clusters, with distances calculated between the cluster centroids. Reconstruction is triggered only when the size or the semantic shift [ 49 ] of the cluster reaches a threshold. This strategy is effective for large-batch scenarios, while becomes suboptimal with interleaved small-batch search and insert operations.

[36] p: Scattered Cluster Problem of In-Place Insertion . A key issue of in-place insertion is that new vectors inserted into a large pre-clustered index often get scattered across many clusters, even when they are semantically close. As shown in Figure 4 (a), across 100 requests from several agent datasets [ 14 , 12 , 46 ] , memory items from the same agent are dispersed into up to 175 clusters, with 38%–100% of these clusters being accessed with frequency less than 5%. This behavior stems from the high-dimensional shell effect [ 5 , 2 ] , where points concentrate near the surface of a hypersphere, causing small semantic variations to translate into large differences in centroid distance calculations. Thus, even highly related memory items may be inserted to different clusters.

[37] p: Such scattered cluster assignments bring challenges for both efficiency and accuracy. First, this forces scanning a larger number of clusters to retrieve semantically related items, incurring extra computation over mostly irrelevant vectors. Second, items in such scattered clusters become harder to locate by centroid distances, and their clusters may be eliminated during the coarse search stage, leading to drop in recall.

[38] p: To tackle this problem, we first study two locality characteristics of agent memory, which provide critical guidance for designing effective clustering strategies.

[39] figure: Figure 4 : Direct in-place updates scatter the new vectors into a large number of existing clusters, leading to degradation in efficiency and recall. A naive solution is to leverage intra-agent locality and maintain dedicated clusters for a agent.

[40] figure: Figure 5 : For more complex workloads, locality across multiple reasoning steps of different requests can be observed. This makes naive dedicated clusters for the agent inefficient, as it fails to capture step-wise clustering.

[41] p: Intra-Agent Locality . As shown in Figure 4 (b), requests in agentic workflows insert memory items that remain highly coherent across steps and across requests of the same agent. The distances between each item and (i) the centroid of the memory items in the request and (ii) the aggregated centroid of all the agent’s memory items are both substantially smaller than the distances to existing large clusters in the database. This phenomenon is particularly pronounced in task-focused workflows (e.g., mathematical reasoning [ 11 ] ). A straightforward strategy is therefore to assign a dedicated cluster to each agent’s insertion requests. However, this approach is insufficient in more complex workflows, where multi-step reasoning introduces cross-step transitions that cannot be captured by a single cluster (we will detail this in the next paragraph).

[42] p: Inter-Request Step-wise Locality . Beyond intra-agent locality, more complex workflows reveal an additional layer of structure: memory items from the same reasoning step across different requests tend to cluster together. For example, in tool-augmented agents [ 57 ] , the planning, tool-calling, and reflection steps across different requests tend to access similar regions of memory. As shown in Figure 5 (a), memory items belonging to the same reasoning step across different requests demonstrate higher similarity, compared to the intra-request and intra-agent similarity. Figure 5 (b) further illustrates the clustering patterns of memory items through 2-dimensional PCA visualization in the tool-calling dataset [ 46 ] with 100 requests, where three clusters emerge, each corresponding to an individual step of the workflow.

[43] p: This step-wise organization induces frequent transitions across multiple clusters. Therefore, although maintaining a single dedicated cluster for each agent works for simple workflows in Figure 4 , it is insufficient to capture the step-wise structures in more complicated scenarios, as shown in Figure 5 . The green centroid becomes semantically unrepresentative, ultimately degrading accuracy and search efficiency.

[44] p: In this work, we aim to optimize the agent memory management considering both intra-agent and step-wise locality. Compared to existing approaches [ 74 , 49 ] , Pancake introduces more efficient cluster assignment and construction strategies that align with the agent’s complex memory access patterns.

[45] h3: 3.2 Challenges for Multi-Agent Memory Index Management

[46] figure: Figure 6 : Coarse search costs with different index methods.

[47] p: Beyond the memory inefficiency for a single agent, we identify the challenges of effectively managing and searching across multiple agent memories, which is a clear need for today’s agentic workloads. In a typical multi-agent setting, each agent continuously updates its local memory, yet may search on the memories of other agents. For example, in generative-agent simulations like AI Town [ 54 ] , each agent records its own action and observation histories, but relies on information originating from other agents’ memories to plan behaviors and coordinate group activities. Because different agents become active or interact at different moments, the set of agent memories to search also varies over time.

[48] p: This brings a clear demand for memory frameworks to support flexible specification of the memory search scope. However, existing ANN libraries [ 16 , 8 , 25 ] only provide interfaces for maintaining and querying on a single index for a given vector database, while offer no native support for search operations across different vector databases.

[49] p: A straightforward approach is to maintain independent indexes for each agent’s memory. When querying the memories of different scopes, the system searches the corresponding indexes and then merges the results. Although this approach can be implemented directly using existing library interfaces, it suffers from search efficiency issues, described as follows.

[50] figure: Figure 7 : Coarse and Fine Search Challenges in Multi-Agent Memory. (a) Coarse search overhead grows rapidly as the number of agents increases. (b) When two agents access the same cluster in the static memory, their access patterns exhibit non-uniform distributions; circles denote accessed vectors, and stars denote the centroids formed by those vectors.

[51] p: Excessive Coarse Search Cost . Large-scale vector indexes typically adopt a two-step search: a coarse search first selects the nearest clusters based on centroid distances, and a fine search is then performed within the selected clusters. When independent indexes are maintained for each agent, a wide-scope query must traverse the coarse index of every agent. As shown in Figure 6 , when querying two agents and the static memory: (a) using a Flat index requires computing the distances to all centroids, and (b) using HNSW [ 48 ] requires a full traversal of the coarse-index graph of every agent.

[52] p: We observe that such multi-index search patterns cause a significant amplification of coarse search cost when the number of agents increases. As shown in Figure 7 (a), with the two commonly recommended Faiss indexes for large-scale settings [ 16 ] , the cost of coarse-grained search rises sharply and exceeds 80% of the total latency when the number of agents reaches 20. Therefore, it becomes necessary to reorganize coarse indexes across agents, thereby reducing search costs during search across different agent memories.

[53] p: Non-Uniform Fine Search Patterns across Agents . We further observe fine search inefficiency due to the different agent memory access patterns. As shown in Figure 7 (b), when multiple agents query the same cluster in a memory index (constructed with static memory base [ 53 ] ), the vectors they access differ markedly in distribution and clustering behavior. This divergence causes the effective centroid for each agent to shift in the embedding space. This divergence causes the centroids formed by each agent’s accessed vectors within the same cluster to shift noticeably in the embedding space.

[54] p: This finding indicates that the optimal fine-index organization is highly scope-dependent: for example, an index layout optimized for Agent 1’s access pattern may be poorly aligned with Agent 2’s pattern. As a result, Agent 1’s cluster organization may force Agent 2 to compute over many irrelevant vectors and potentially suffer degraded recall. Such disalignment makes it necessary for coordinated organization of fine indexes across multiple agents.

[55] p: To address the above issues, Pancake introduces a hybrid graph for efficient coarse search within only one graph traversal, as illustrated in Figure 6 . Pancake also aligns fine-index access by associating each cluster with the pattern recognition of other agents, enabling optimized cross-agent search performance.

[56] figure: Figure 8 : Comparison of operation costs on GPU and CPU, including (a) search time and (b) data transfer and allocation. The results are sampled on the MS MARCO [ 51 ] dataset.

[57] h3: 3.3 Difficulties for GPU-CPU Collaboration

[58] p: In this section, we explore how to fully utilize the hardware resources of the GPU-CPU platform, which is widely adopted in LLM inference [ 35 , 86 ] . Vector search involves high-dimensional floating-point computation and therefore benefits substantially from GPU acceleration. As shown in Figure 8 (a), we characterize the performance advantages of CPU and GPU execution. When the number of vectors per cluster is small (< 256), CPU-based computation exhibits lower latency. In contrast, once the cluster size reaches a moderate range ( ≥ \geq 512), GPU-based vector search achieves a clear speedup of more than 3 × 3\times . The GPU search latency remains largely stable as the cluster grows, since the dominant overhead arises from kernel launch rather than computation. Prior work has extensively explored fully GPU-resident indexes [ 31 ] and search frameworks [ 84 ] .

[59] p: However, large-scale vector databases (often over 100 GB [ 18 ] ) place heavy demands on GPU memory and make it impractical for the GPU to store the entire index. The large model weights and KV cache further exacerbate this pressure. This necessitates an on-demand data transfer mechanism between the CPU and GPU. However, such transfer introduces significant overhead, typically far exceeding the actual computation time, as shown in Figure 8 (b). To address this challenge, existing hybrid CPU–GPU designs employ hotspot caching and offloading [ 23 , 32 , 61 , 43 ] for large-scale indexes.

[60] p: The highly dynamic nature of agent memory introduces an additional dimension of complexity for maintaining consistency in CPU–GPU co-managed indexes. Hotspot clusters in agent memory are not only frequently queried but also frequently updated. However, because CUDA lacks efficient mechanisms for concurrent dynamic list expansion, clusters cached on the GPU cannot flexibly support frequent insertions. Prior work primarily supports cache management for static indexes, while performing updates on the CPU index and retransferring the modified clusters back to the GPU incurs prohibitive eviction and transfer costs.

[61] p: To address the above challenge, Pancake implements a GPU–CPU coordinated dynamic index management scheme based on insertion buffers and asynchronous transfers. This design enables dynamically extensible hotspot clusters to be accelerated during both search and update operations.

[62] h2: 4 Pancake: Methods and System Design

[63] h3: 4.1 Overview

[64] p: In this work, we present Pancake, a multi-tier ANN-based system designed to meet the demands of dynamic agentic memory workloads. Pancake follows a coordinated multi-tier design that consists of: (i) Multi-level, cache-inspired index orchestration informed by trajectory-based agent workload embeddings, enabling locality-aware search and update behavior; (ii) Multi-layer memory storage that supports efficient sharing, reuse, and migration of memory across agents; and (iii) Multi-device efficient execution with dynamic hotspot detection and cross-device consistency management to fully leverage heterogeneous CPU–GPU resources.

[65] h3: 4.2 Pattern-Driven Multi-Level Index Cache

[66] figure: Figure 9 : Three-level memory index cache to optimize search efficiency, with FSM-based modeling for access patterns.

[67] p: Existing dynamic ANN methods either rely on streaming insertion and local rebalancing [ 50 , 49 , 74 ] , or on coarse-grained buffering and periodic merging [ 87 , 60 ] . Both approaches lack awareness of agent-level workload patterns, including intra-request locality and inter-request step-wise locality.

[68] p: Three-Level Cluster Caching . We employ partial caching to resolve the mismatch between localized access operations and the coarse-grained cluster structure of the underlying ANN index. As shown in Figure 9 , each upper level index forms a subset of the level below, but is organized to more closely reflect the agent’s intrinsic memory-access patterns.

[69] p: Search and update over the index always begin at the top level. L0 maintains a table S S that tracks the most frequently accessed N p N_{p} tiny clusters, which contains the most recently accessed vectors to preserve the agent’s temporal locality. When an L0 cluster overflows, evicted vectors are written back into the L1 index. L1 also maintains N p N_{p} intermediate clusters. It caches the top- k ′ k^{\prime} neighbors for each search and update, where k ′ k^{\prime} is slightly larger than the actual retrieval parameter k k , allowing L1 to store the broader neighborhood around frequently accessed vectors. Finally, once an L1 cluster exceeds a predefined size threshold, it is merged with the L2 clusters, forming a stable and coarse-grained structure.

[70] p: We leverage the early termination mechanism [ 3 ] in vector search to accelerate computation using cached data. During search, whenever all top- k k candidates at the current level have distances smaller than α e ​ t ⋅ d a ​ g ​ e ​ n ​ t \alpha_{et}\cdot d_{agent} , we skip computation at the next level. Here, d a ​ g ​ e ​ n ​ t d_{agent} denotes the average top- k k distance across recent queries of the same agent. In practice, setting α e ​ t = 0.6 ∼ 0.8 \alpha_{et}=0.6\sim 0.8 provides a strong trade-off between efficiency and accuracy. We further introduce a verification mode in the system: after an early return, the system optionally performs the complete search in the background. This enables dynamic adjustment of α e ​ t \alpha_{et} without incurring additional latency, while maintaining compatibility with LLM-coordinated speculative-generation workflows [ 30 , 23 , 83 ] .

[71] p: FSM-based Pattern Modeling. The agent memory access patterns can be modeled as a Finite-State-Machine (FSM):

[72] table: P = ( S , T ) , ( c i → c j ) ∈ T , c i , c j ∈ S , P=(S,\,T),\qquad(c_{i}\rightarrow c_{j})\in T,\;c_{i},c_{j}\in S,

[73] p: where S S is the set of semantic cluster states. Each cluster ( c , δ ) ∈ S (c,\delta)\in S stores its cluster centroid c c and the average intra-cluster vector deviation δ \delta from the centroid. The transition set T T captures the directed movement of memory accesses across cluster states. Such FSM abstraction preserves both semantic grouping and step-wise transition behavior.

[74] p: The L0 index maintains a pattern table with N p N_{p} FSM entries. Given a new request with memory embedding sequence ( v 1 , v 2 , … , v t ) (v_{1},v_{2},\ldots,v_{t}) , we compute its similarity to pattern P i P_{i} based on prefix-state alignment and transition consistency:

[75] table: sim ( P i , v 1 : t ) = ∑ k = 1 t I [ ( c k − 1 → c k ) ∈ T i ] ⋅ δ k 1 + | c k − v k | , \mathrm{sim}(P_{i},v_{1:t})=\sum_{k=1}^{t}I\big[(c_{k-1}\rightarrow c_{k})\in T_{i}\big]\cdot\frac{\delta_{k}}{1+|c_{k}-v_{k}|},

[76] p: where I ⁡ [ ⋅ ] I[\cdot] is the indicator function. Using this similarity, each request identifies the best-matching pattern and infers the expected target cluster for subsequent memory accesses.

[77] p: Pattern-based Reordering and Prefetching . Modeling the access pattern enables workload-aware search reordering. For each search operation, the cache manager matches its recent access sequence to a pattern in the FSM table and predicts the most probable L0 and L1 cluster. The search process then prioritizes the predicted cluster, enabling a more efficient search order and increasing the likelihood of early termination.

[78] p: FSM-based modeling also enables prefetch-like behavior in the index cache. After each completed search or update, the system predicts the clusters likely to be accessed next. If these clusters have been evicted or written back, background prefetching is triggered to proactively refresh the cache ahead of time. Prefetching is carried out through an independent search, it can run in parallel with the agent’s LLM-generation steps, creating additional opportunities to reduce overhead.

[79] p: FSM Construction . Constructing such FSMs online is challenging, as agent memory accesses arrive in the form of embedding vectors rather than pre-labeled semantic clusters. Classical pattern-recognition approaches (e.g., PCA [ 1 ] , HMMs [ 55 ] ) are prohibitively expensive for high-dimensional and fine-grained online agent workloads. We therefore adopt a lightweight heuristic FSM construction and merging strategy.

[80] p: When an agent request completes, the cache system first attempts to match it against an existing FSM in the table. If no match is found, a new FSM is created. During creation, each access in the request sequence becomes an independent state, and states are subsequently merged according to the maximum number of states N S N_{S} and the minimum merging distance d merge d_{\text{merge}} . If the number of FSM entries exceeds N p N_{p} , the system merges two FSMs with the highest similarity, producing a compact and continuously updated FSM table.

[81] figure: Figure 10 : Multi-agent index management with hybrid graph and agent-specific pattern profiling on shared clusters.

[82] h3: 4.3 Multi-Agent Indexing with Hybrid Graph

[83] p: We propose a multi-agent–friendly index mechanism that incorporates coordinated coarse search and alignment. As shown in Figure 10 , our design unifies the multiple coarse indexes into a hybrid graph structure, enabling efficient coarse search through graph traversal. Meanwhile, by associating each cluster with agent-specific memory access patterns, referred to as agent profiles, we further reduce overhead and improve recall for the cross-index operations.

[84] p: Hybrid Graph Construction . We introduce a graph structure that connects the static memory and each agent’s local memory. For the fine index, vectors in each static and agent local memory are stored only once, eliminating redundant storage. For the coarse index, each memory scope maintains its own coarse index, organized as a multi-level graph structure similar to HNSW [ 48 ] . Each layer forms a bounded-degree graph with up to M M neighbors per node. Queries perform a greedy descent through the upper layers, followed by a best-first search at the bottom layer using a frontier of size e ​ f s ​ e ​ a ​ r ​ c ​ h ef_{search} to approximate the nearest neighbors.

[85] p: Among multiple coarse indexes, we further introduce inter-graph connections to enable navigation across different memory scopes. Specifically, when maintaining each agent’s coarse index, each node in the graph is additionally connected into the static coarse index with probability of 1 / e ​ f c ​ o ​ n ​ n ​ e ​ c ​ t 1/ef_{connect} , thereby creating a controlled number of cross-agent portal nodes that support collaborative multi-agent search.

[86] p: A cross-scope memory operation begins in the static coarse index entry and performs a BFS-like traversal. When the traversal encounters a node with an inter-connection to the target scope, the search adds the corresponding graph to the search frontier, and set the inter-connected node as the entry. This enables seamless transition across memory scopes while avoiding unnecessary searching over irrelevant regions.

[87] p: To determine a suitable value for e ​ f connect ef_{\text{connect}} , we compare the density of the static coarse index with that of each agent-specific index. We measure the average centroid spacing within the private index ( d agent d_{\text{agent}} ) and the static index ( d static d_{\text{static}} ), and set the inter-connection probability as

[88] table: e ​ f connect = min ⁡ ( α i ​ c ⋅ d static d agent , 1 ) . ef_{\text{connect}}=\min\!\left(\alpha_{ic}\cdot\frac{d_{\text{static}}}{d_{\text{agent}}},\;1\right).

[89] p: The intuition is as follows: when the static index covers a broader space, only sparse connections are needed; when the two spaces have similar density, denser connections help avoid cross-graph local minima. Empirically, we choose α i ​ c \alpha_{ic} between 4 and 8 to balance efficiency and recall.

[90] p: Search Optimization with Agent Profile . Due to highly non-uniform access patterns, clusters in the static memory exhibit different usage patterns across agents. However, the static memory index cannot adapt to these differences, leading to unnecessary search overhead and preventing the index from aligning with agent-specific access patterns.

[91] p: To address this, Pancakeintroduces an agent profile mechanism for each static cluster. Specifically, every static cluster is associated with an agent-specific table that records the local IDs of recently accessed vectors within that cluster. Such list is maintained as a fixed-size sorted list. Whenever the top- k k results of a query fall inside the current cluster, the corresponding vector IDs are promoted to the front of the list. For subsequent accesses, when the agent revisits the cluster, it first retrieves the vectors referenced in its profile by their stored local IDs, enabling a better search order and increasing the likelihood of early termination. Because the profile maintains only vector IDs and a lightweight list structure, the additional storage and management overhead is negligible comparing to the high-dimensional embedding computations.

[92] h3: 4.4 Dynamic GPU-CPU Index Coordination

[93] figure: Figure 11 : GPU-CPU coordinated index management to enable hotspot cluster computation acceleration.

[94] p: To further leverage heterogeneous hardware resources, we introduce a GPU–CPU coordinated dynamic index management mechanism, as illustrated in Figure 11 . Our heterogeneous design consists of a CPU-side insertion buffer and a GPU-side manager for hotspot-aware caching, onloaded search, and consistent cluster maintenance. Such a system enables memory-efficient hotspot acceleration and dynamic cluster organization across devices. This is particularly critical in the co-located serving scenario with LLMs [ 23 ] , where the inference engine occupys tens of gigabytes of GPU memory.

[95] p: Hotspot-aware Caching . In our hybrid index manager, GPU memory dynamically caches hotspot clusters to accelerate critical computation. For each CPU-resident cluster, the system tracks its access frequency and selects the most frequently accessed clusters according to a predefined GPU memory budget. Whenever the hotspot set changes, the system performs cluster eviction and reallocation to keep the GPU cache aligned with the current workload. Data migration is through asynchronous CPU–GPU transfers to avoid high latency. However, insertions in the agentic memory may cause frequent staleness of the cached clusters.

[96] p: CPU Insertion Buffer . As shown in the sampling results of § 3.3 , the CPU computation time of a small set of vectors is lower than the GPU’s cluster processing latency. Therefore, we maintain a per-cluster insertion buffer: once a cluster is resident on the GPU, subsequent insertions targeting that cluster are first accumulated in its CPU-side buffer of size B i ​ n ​ s ​ e ​ r ​ t B_{insert} . For all the searches targeting that cluster, computation is performed collaboratively using both the GPU-cached portion of the cluster and the vectors newly inserted the CPU buffer. The partial results from the two devices are then merged to produce the final results. Because the additional CPU-side search runs in parallel with the GPU computation and contributes only a small fraction of the overall processing time, the end-to-end request latency effectively matches that of a single-GPU execution. Based on this observation, we set B i ​ n ​ s ​ e ​ r ​ t B_{insert} to the largest cluster size where CPU-side search cost is lower than GPU-side search, which is 128 on our platform.

[97] p: Asynchronized Consistency Management . When the insertion buffer becomes full, the corresponding GPU-cached cluster is resized, and the buffered vectors are migrated from the CPU to the GPU. To avoid the substantial latency caused by on-demand data transfers, we adopt a fully asynchronous cluster-expansion mechanism. The GPU-side index manager proactively allocates new space for clusters to expand and performs data transfers in parallel with online serving. Already cached data are migrated using low-cost GPU–GPU copies, while newly inserted buffer data are transferred through GPU–CPU copies. Once the new data transfer completes, the old GPU cluster is released, enabling seamless online cluster switching. This design eliminates both the waiting overhead associated with synchronous data movement and the memory waste incurred by over-allocating GPU space.

[98] p: On-GPU Cluster Splitting . The GPU cache introduces another optimization opportunity: accelerating the computation for cluster splitting. Clustering algorithms like K-means-based methods [ 85 , 15 ] typically incurs a vector similarity cost that is multiple times higher than that of regular search. Thus, we implement a lightweight kernel based on GPU-based K-means algorithms [ 41 , 6 ] to onload cluster splitting, avoiding the high computational load and latency on the CPU. Importantly, due to the locality of memory access, clusters that require splitting are usually cached on the GPU, so this technique can reduce the majority of splitting overhead.

[99] h2: 5 Implementation

[100] p: User Interface . Pancake provides a user-friendly Python interface that exposes simple primitives for agent-memory operations, including search, insert, update, and delete, with explicit specification of the target memory scope. Our initialization interface also supports loading from existing indexes, such as Faiss [ 16 ] , enabling reconstruction that is friendly to IVF-based indexes. Operations submitted through the interface are batched, and adjacent operations of the same type are further grouped into a single batch to improve resource utilization.

[101] p: Multi-threaded Index Construction . In Pancake, clusters are implemented as multithread-shared data structures, protected by shared-read and exclusive-write locks. Each cluster is associated with metadata, including its index identifier, multi-agent profiles, and its residency status across the multi-level cache and the GPU cache. We maintain a multithreaded execution pool that includes dedicated search threads, update threads, cache-management threads, and GPU-management threads. Insert and delete operations are also handled within the search threads, where items are updated based on the search results. Pancake adopts asynchronous invocation to ensure concurrency with LLM calls and to maintain compatibility with existing RAG-style systems [ 23 , 30 , 27 ] .

[102] h2: 6 Evaluation

[103] figure: Figure 12 : End-to-end throughput comparison between Pancake and other agentic frameworks, in a single agent scenario across four different access patterns. The experiments are conducted with vLLM [ 35 ] for Llama models [ 62 ] and API calls for GPT-5.

[104] h3: 6.1 Experimental Setup

[105] p: Hardware . We conduct all experiments on a CPU–GPU hybrid server. Each node is equipped with one 64-core AMD EPYC 9534 processor and eight NVIDIA H100 GPUs with 80 GB of memory. The main control, scheduling, and computation logic of Pancake run on the CPU, while the LLM generation and GPU caching are performed on the H100 GPUs.

[106] p: Baseline . For agent serving, we compare four memory design algorithms and their system implementations. These systems provide default ANN-based interfaces for memory management and retrieval. We evaluate them end-to-end by integrating their memory backends with LLM generation workloads. The baselines include: A-Mem [ 73 ] : backend for semantically evolving memory in long-term conversational retrieval. MemGPT [ 53 ] : backend for OS-style memory that swaps information between main context and external storage. LlamaIndex [ 44 ] , vector-store backend in the RAG-oriented framework. LangMem : vector-store backend in the agentic framework LangChain [ 36 ] .

[107] p: For evaluating the performance of standalone vector databases, we compare our system against state-of-the-art dynamically updatable vector-index libraries. We use the vectors generated from the memory operations in our end-to-end agent workloads as input to these systems. The baselines include: Quake [ 50 ] , structured and insert-friendly index library with dynamic hot-region–aware optimization. SpFresh [ 74 ] , a large-scale vector search framework based on streaming insertion and localized, balancing-aware reconstruction. DiskANN [ 25 , 60 ] , open ANN library that combines an upper-layer graph with a lower-layer cluster index.

[108] p: For ablation study, we also implement two dynamic maintenance strategies within our framework, including: Pancake-IVF-Static , which initializes an IVF index once and simply appends new vectors to the nearest centroid without any further maintenance. Pancake-IVF-Split , which performs cluster splitting when the size reaches a threshold, consistent with streaming-update and lazy-reconstruction strategies [ 49 ] .

[109] p: Dataset . We evaluate our system across diverse forms of agent dataset, including multi-turn human–agent dialogue datasets (UltraChat [ 14 ] , UltraFeedback [ 12 ] ), long chain-of-thought mathematical reasoning (Prm800k [ 42 ] , Gsm8k [ 11 ] ), and task-oriented agent datasets covering function calling (APIGen [ 46 ] ) and environment interaction (AgentGym [ 69 ] ).

[110] p: Workload . We evaluate several representative memory access patterns, which can be observed in different types of agents:

[111] p: – One-Search-One-Insert : Each generation step search the memory and updates it with the new output, typical for multi-turn conversational agents [ 53 , 78 ] .

[112] p: – Step-Search-Then-Insert : Each step search the memory, but updates occur only at the end, typical for summarization or long-context compression agents [ 9 , 52 , 79 ] .

[113] p: – Search-Then-Step-Insert : Only the first step performs memory search, while the update occurs in each step, typical for personalized agents driven by user profiles [ 20 , 67 ] .

[114] p: – Search-Only : The agent only queries memory without updates, typical for RAG-style agents [ 4 , 71 , 7 ] .

[115] p: Static Knowledge Database . We initialize the vector database similar to the Mem-GPT [ 53 ] setup, using the MS MARCO corpus [ 51 ] , 8M passages in total, as the initial knowledge base. All embeddings are encoded using the E5 model [ 66 ] with 1024 dimension.

[116] h3: 6.2 Overall Performance

[117] p: In this section, we evaluate the end-to-end improvements on memory-based agents performance when using Pancake.

[118] figure: Figure 13 : End-to-end throughput comparison in two-agent mixed workload, conducted with Llama3.1-8B.

[119] figure: Figure 14 : Scaling behavior of end-to-end throughput with an increasing agent number. The experiments are conducted with Llama3.1-8B.

[120] figure: Figure 15 : Query throughput of Pancake and existing vector database implementations, with the batch size set as 8.

[121] p: Single-Agent Throughput. We compare different memory management libraries in single-agent settings across multiple models and datasets, as shown in Figure 12 . Across both local inference servers [ 35 ] and remote API execution, Pancake consistently sustains stable single-agent request throughput, achieving end-to-end performance improvements ranging from 1.12 × \times to 26.18 × \times . On average, the speedup over existing libraries is more than 4.29 × \times .

[122] p: For the memory operations only, Pancake achieves speedups of more than 6.81 × \times . The average memory operation time of Pancake accounts for less than 17.9%, and on average 3.2% of the total execution time. This demonstrates the effectiveness of Pancake in mitigating memory-related bottlenecks.

[123] p: In addition, we observe that workloads dominated by search operations, including One-Search-One-Insert and Search-only, exert a pronounced performance impact on baseline systems. This is because existing systems rely on suboptimal index constructions and maintenance strategies, which allow low-cost insertions but incur excessive search overhead.

[124] p: Mixed-Workload Throughput. We evaluate the impact of two-agent mixed workloads on end-to-end performance, where each agent performs inserts on its private memory and searches on both shared and private memory. As shown in Figure 13 , existing memory frameworks exhibit additional performance degradation, dropping by 29.9% ∼ \sim 55.9%. This degradation arises from separate memory instance maintenance and the lack of coordinated management across shared and private memory regions, which leads to interference between agents and amplifies operation overhead. In contrast, Pancake leverages its hybrid-graph design to enable efficient cross-agent search and index alignment, thereby preserving search locality and reducing redundant scans, Pancake limits the performance drop to no more than 9.8% under mixed workloads.

[125] p: Multi-Agent Scalability. We construct varying numbers of memory-based agents and execute distinct requests over the same dataset, then measure overall throughput with operations across shared and private memory regions. As shown in Figure 14 , Pancake achieves near-linear scalability in multi-agent settings. With up to 20 concurrent agents (the typical scale of common multi-agent frameworks [ 39 , 68 ] ), the end-to-end performance degradation remains below 10.2%.

[126] p: We also observe that more complex dataset sequences, such as AgentGym and APIGen, exhibit larger performance drops. This is because broader dataset coverage increases the number of nodes traversed during the coarse-level graph search, resulting in proportionally higher search overhead.

[127] h3: 6.3 Comparison with Existing Vector Database

[128] figure: Figure 16 : Tradeoff between recall and query latency over different indexing strategies.

[129] p: Query Throughput Improvement . We compare Pancake with existing vector databases and indexing strategies under online serving workloads. As shown in Figure 15 , Pancake consistently improves throughput across memory-intensive agent-serving scenarios, achieving 1.9 × \times to 4.2 × \times average speedups over the baselines. These speedups stem from cache and index designs tailored to agent memory-access patterns, which is overlooked in prior work. When leveraging GPU acceleration, Pancake further achieves an additional 2.2× performance gain, resulting in more than 3.9× speedup over other baselines. This demonstrates the effectiveness of dynamically coordinating GPU resources through our management mechanisms.

[130] p: Tradeoff between Efficiency and Recall . We compare recall–latency trade-offs under both mixed search–update and search-only workloads. As shown in Figure 16 , directly applying IVF index yields relatively low recall: in the search-only setting, IVF must scan up to 128 clusters to reach recall above 0.9. Under the search–update workload, IVF suffers an even larger recall drop because newly inserted vectors are scattered across different clusters, leading to reduced locality and suboptimal index organization.

[131] p: By exploiting agent locality and memory-access patterns, Pancake effectively leverages its caching mechanism to reduce latency while maintaining high recall. Moreover, with coordinated GPU processing, Pancake can scan additional clusters while simultaneously serving cache hits, achieving lower latency together with a slight improvement in recall.

[132] h3: 6.4 Ablation Study

[133] p: In this section, we conduct detailed comparative experiments on the optimization techniques and provide an in-depth analysis of their effects and the root causes of the improvements.

[134] p: Optimized Index with Multi-level Cache . We compare how different dynamic maintenance strategies affect the search costs with dynamism. A lower number of scanned vectors indicates that the index has evolved into a structure better aligned with the current agent’s access pattern and provides stronger early-termination opportunities, thereby improving performance. As shown in Figure 17 , performing IVF-Static updates leads to significantly higher scan counts, because newly inserted memory items are distributed across many clusters rather than being localized. IVF-Split eventually reduces the number of scanned vectors with sufficient insertions and the stable clusters formed. However, the long pre-convergence phase can be observed since the index cannot rebalance until the splitting threshold is reached. In contrast, our multi-level index cache effiently exploits agent-specific spatial and temporal locality, allowing it to stabilize at a low scan cost much earlier. This early adaptation leads to up to 2.23 × \times latency reduction over long-serving workloads.

[135] figure: Figure 17 : Number of scanned vectors to achieve fully recall of top-5 memory items. The insertion-to-search ratio is 1:1.

[136] p: Search Efficiency with Multi-Agent Index . We first compare the reduction in coarse index search cost under multi-agent index management. As shown in Figure 18 (a), maintaining separate indexes for each agent leads to a near-linear increase in coarse search overhead as the number of agents grows. In contrast, our multi-index management employs a hybrid graph that interconnects agents’ coarse indexes, enabling efficient navigation of the global search space and achieving more than a 20× reduction in coarse search cost.

[137] p: We further compare the total search cost under different optimization strategies. As shown in Figure 18 (b), the hybrid-graph construction reduces the number of vector similarity computations by up to 11.6% compared to independently constructed indexes. Moreover, when incorporating agent profiles, we can track each agent’s access preferences within the static clusters, achieving an additional 21.8% reduction in average computation cost without modifying the global index layout. These results highlight the unique advantages of Pancake in multi-agent index management.

[138] figure: Figure 18 : Efficiency improvements from multi-level index management on (a) coarse index search cost and (b) total computation cost.

[139] figure: Figure 19 : (a) GPU speedups under varying pre-allocated GPU cache sizes. (b) Computation latency of each query over the input workload with AgentGym dataset and 10GB GPU memory cache size. The insertion-to-search ratio is 1:1.

[140] p: Speedups with GPU Caching . We evaluate how GPU cache size affects performance. As shown in Figure 19 (a), the GPU-accelerated version achieves up to 1.92 × \times speedup over the CPU baseline and reaches a performance plateau with only 5 ∼ \sim 15 GB of GPU memory. The effectiveness of GPU acceleration depends on the workload: conversational datasets distribute query-relevant clusters more widely, requiring a larger GPU cache to fully exploit acceleration.

[141] p: We also examine latency over time under a mixed search–insert workload. As shown in Figure 19 (b), the GPU version warms up quickly by caching hot clusters and maintains low, stable latency. Occasional spikes arise when streaming insertions trigger cluster splits, temporarily introducing additional computation. In our GPU-enabled design, most cluster operations are performed on the GPU, reducing the cost of these split events and keeping their impact minimal.

[142] h2: 7 Conclusion

[143] p: We presented Pancake, a multi-tier memory management system that bridges the gap between dynamic agentic memory and ANN-based vector indexing. Pancake leverages semantic locality for single-agent workloads, hybrid indexing for multi-agent memory management, and CPU–GPU collaborative indexing for acceleration. With a simple Python interface and support for flexible multi-scope memory operations, Pancake integrates easily into existing agent frameworks. Experiments across diverse agent datasets show that Pancake significantly reduces memory operation overhead and delivers more than 4.29 × \times average end-to-end speedup over existing implementations.

[144] h2: References

[145] h2: Instructions for reporting errors

[146] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[147] p: Tip: You can select the relevant text first, to include it in your report.

[148] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[149] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
