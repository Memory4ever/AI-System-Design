[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Vectorizing the Trie: Efficient Constrained Decoding for LLM-based Generative Retrieval on Accelerators

[3] h6: Abstract.

[4] p: Generative retrieval has emerged as a powerful paradigm for LLM-based recommendation. However, industrial recommender systems often benefit from restricting the output space to a constrained subset of items based on business logic (e.g. enforcing content freshness or product category), which standard autoregressive decoding cannot natively support. Moreover, existing constrained decoding methods that make use of prefix trees (Tries) incur severe latency penalties on hardware accelerators (TPUs/GPUs). In this work, we introduce STATIC ( S parse T ransition Matrix- A ccelerated T rie I ndex for C onstrained Decoding), an efficient and scalable constrained decoding technique designed specifically for high-throughput LLM-based generative retrieval on TPUs/GPUs. By flattening the prefix tree into a static Compressed Sparse Row (CSR) matrix, we transform irregular tree traversals into fully vectorized sparse matrix operations, unlocking massive efficiency gains on hardware accelerators.

[5] p: We deploy STATIC on a large-scale industrial video recommendation platform serving billions of users. STATIC produces significant product metric impact with minimal latency overhead ( 0.033 0.033 ms per step and 0.25 % 0.25\% of inference time), achieving a 948 × 948\text{\small$\times$} speedup over a CPU trie implementation and a 47 47 – 1033 × 1033\text{\small$\times$} speedup over a hardware-accelerated binary-search baseline. Furthermore, the runtime overhead of STATIC remains extremely low across a wide range of practical configurations. To the best of our knowledge, STATIC enables the first production-scale deployment of strictly constrained generative retrieval. In addition, evaluation on academic benchmarks demonstrates that STATIC can considerably improve cold-start performance for generative retrieval. Our code is available at https://github.com/youtube/static-constraint-decoding .

[6] h6: Keywords:

[7] h2: 1. Introduction

[8] p: Recommender systems have long served as the core discovery engines powering massive online platforms like YouTube and Amazon ( Linden et al., 2003 ; Covington et al., 2016 ) . While neural network techniques continue to improve these engines, this domain is undergoing a paradigm shift whereby embedding-based neural retrieval models that recommend candidates through approximate nearest neighbor search such as ScaNN ( Guo et al., 2019 ; Sun et al., 2024 ) are being superseded with LLM-based generative retrieval ( Rajput et al., 2023 ; He et al., 2025 ; Deng et al., 2025 ; Yang et al., 2024 ; Si et al., 2023 ; Zhou et al., 2026 ) . By representing each item as a sequence of discrete tokens (called Semantic IDs or SIDs) and training Transformers ( Vaswani et al., 2017 ) to autoregressively decode the Semantic ID tokens of the target items ( Rajput et al., 2023 ) , generative retrieval bypasses key limitations of traditional dual (user, item)-encoders ( Weller et al., 2026 ) to capture deeper semantic relationships. Additionally, it obviates the need for an external nearest-neighbor indexing infrastructure ( Rajput et al., 2023 ) and allows one to adapt pre-trained LLMs for recommendation tasks ( He et al., 2025 ; Liu et al., 2025 ; Zhou et al., 2026 ) .

[9] p: However, generative retrieval models as they were originally designed lack a critical feature: control over the generated output space, as required to enforce business logic across a variety of industry applications. The absence of this feature has not stopped these next generation recommendation models from becoming widespread in large-scale industry settings ( He et al., 2025 ; Deng et al., 2025 ; Zhou et al., 2025a ; Zhou et al., 2025b ) , but more fine-grained output space control would enable practitioners to restrict the output space based on business logic, such as enforcing freshness constraints (e.g. “uploaded within the last day”), locality (e.g. regional recommendations), product categories (e.g. “recommend summer clothes”), or inventory availability (e.g. “in stock” only). This makes it possible to train a single large model and deploy it across multiple use cases.

[10] p: In a traditional recommendation setting, business logic is enforced by filtering items post-retrieval or constraining the search space a priori (e.g. by running a restricted ScaNN search ( Guo et al., 2019 ) ). If a system requires items to be “in stock” or “uploaded within 7 days,” a boolean filter simply drops invalid candidates from the retrieved set or the ScaNN index. In generative retrieval, however, the “retriever” is a probabilistic autoregressive model that synthesizes Semantic IDs ( Rajput et al., 2023 ) . Without intervention, an LLM will confidently generate SIDs for items that are out-of-stock, stale, or legally restricted. Relying on post-generation filtering is computationally wasteful; the model may spend its entire inference budget generating invalid items, resulting in zero valid recommendations.

[11] p: To address this issue, constraints must be enforced during the LLM decoding process. The standard algorithmic solution is to implement constrained decoding with a prefix tree (trie), which masks invalid tokens at each step ( Ye et al., 2025 ) . While conceptually sound, we observe that naive pointer-chasing trie-based constraints are fundamentally hostile to hardware accelerators for two reasons:

[12] p: Memory Latency Pointer-based structures result in non-contiguous, random memory access patterns. This prevents memory coalescing, failing to utilize the High-Bandwidth Memory (HBM) burst capabilities of modern TPUs/GPUs ( Jouppi et al., 2017 ) . Furthermore, these irregular patterns nullify hardware prefetchers designed for linear streaming, leading to severe memory-bound latency and stalled execution units.

[13] p: Compilation Incompatibility Modern accelerator architectures (e.g. Google’s XLA-reliant ( Sabne, 2020 ) TPUs) require static computation graphs for ML compilation ( Li et al., 2020 ) . Naive trie implementations rely on data-dependent control flow and irregular linked structures, which are fundamentally incompatible with this paradigm. While accelerators support dynamic indexing into fixed-size buffers (e.g. vectorized gather), the irregular memory access and recursive branching of pointer-chasing preclude end-to-end ML compilation.

[14] p: In our preliminary experiments, a CPU-offloaded trie implementation increased inference time by 2 × 2\text{\small$\times$} , rendering it unusable for our target per-decoding-step latency of ≤ 10 \leq\!10 ms. More sophisticated existing approaches utilizing binary search also exhibited significant latency penalties ( Ye et al., 2025 ) . While alternative methods like Finite State Transducers (FSTs) are standard in natural language processing, they suffer from state explosion when applied to production-scale SID vocabularies (e.g. on the order of millions of items) and lack native TPU support ( Koo et al., 2024 ) .

[15] p: In this work, we introduce STATIC ( S parse T ransition Matrix- A ccelerated T rie I ndex for C onstrained Decoding), a framework that recasts constrained decoding from a graph traversal problem into a series of vectorized sparse matrix operations. STATIC is designed to resolve the aforementioned issues and enable extremely fast and scalable constrained decoding for generative retrieval. Notably, our I/O complexity 1 1 1 Unlike traditional time or space complexity, I/O complexity ( Hong and Kung, 1981 ) on a TPU evaluates algorithmic efficiency by counting the number of costly data block transfers between off-chip High Bandwidth Memory (HBM) and on-chip SRAM. is O ⁡ ( 1 ) O(1) with respect to constraint set size, in contrast with the logarithmic scaling from existing binary search-based methods.

[16] p: Our contributions are as follows:

[17] p: We propose a method to flatten prefix tree-specified constraints into static Compressed Sparse Row (CSR) matrices, enabling O ⁡ ( 1 ) O(1) memory access overhead via coalesced reads for fast decoding constraint extraction.

[18] p: We design a branch-free decoding algorithm using dynamic slicing and mask arithmetic. This makes constrained decoding fully accelerator-native and eliminates host-device round-trips, thereby enabling massive efficiency gain.

[19] p: We deploy this system on an ultra-large-scale video recommendation platform (YouTube) for multiple product use cases. We present one specific setting in which we constrain an generative retrieval LLM to a pre-specified vocabulary of 20 20 million fresh items, improving key online metrics with minimal latency overhead compared to baseline methods.

[20] p: We evaluate the scalability of STATIC and find that its latency remains extremely low across a wide range of constraint set and Semantic ID vocabulary sizes.

[21] p: We demonstrate how one can use constrained decoding to improve cold-start recommendation performance in a principled setting using Amazon Reviews ( He and McAuley, 2016 ) datasets.

[22] h2: 2. Related Work

[23] p: In the recommender systems field, the shift from embedding-based retrieval ( Guo et al., 2019 ) to generative retrieval ( Rajput et al., 2023 ) has necessitated the design of novel Transformer decoding strategies. Our work lies at the intersection of large-scale generative recommendation ( Rajput et al., 2023 ) , constrained token generation, and hardware-aware system optimization.

[24] h3: 2.1. Generative Retrieval and Semantic Indexing

[25] p: Generative retrieval (GR) represents a paradigm shift wherein the item corpus is internalized within the model parameters, replacing the traditional large-scale embedding and nearest neighbor search pipeline with a direct sequence generation task ( Tay et al., 2022 ) .

[26] p: Recent approaches in this area, specifically TIGER ( Rajput et al., 2023 ) , SEATER ( Si et al., 2023 ) , and LIGER ( Yang et al., 2024 ) , utilize Semantic IDs—hierarchical, discrete token-based item representations, where semantically similar items are optimized to share the same prefix. These generative retrieval techniques produce improved results and have been deployed in multiple online recommendation platforms, as seen in PLUM ( He et al., 2025 ) and OneRec ( Deng et al., 2025 ; Zhou et al., 2025a ; Zhou et al., 2025b ; Liu et al., 2025 ) . However, a critical limitation of these autoregressive retrieval models is the “validity gap.” Unlike natural language generation, where the output space is open-ended, retrieval requires the generated string to map perfectly to a valid item index. As noted by Rajput et al. (2023) , without constraints, the model effectively “hallucinates” non-existent inventory, leading to retrieval failures. This issue is especially pertinent in industry settings where practitioners deploy the same pre-trained model across multiple product environments, each having its own valid corpus, with some requiring candidates to fall within a certain regional locality or meet certain “freshness” requirements. While previous work focuses on improving recall metrics ( He et al., 2025 ; Si et al., 2023 ; Zhou et al., 2025a ; Deng et al., 2025 ; Ju et al., 2025 ) , it largely ignores the latency costs of enforcing validity constraints in a high-throughput production environment; we explicitly address this in our paper.

[27] p: Additionally, existing generative retrieval papers ( Yang et al., 2024 ) have noted that generative retrieval models struggle with cold-start item recommendation: the setting in which a model must recommend items it has never before seen during training. We demonstrate in Section 6 that by implementing constrained decoding with a cold-start item set, one can improve cold-start performance significantly.

[28] h3: 2.2. Constrained Decoding in NLP

[29] p: Constrained decoding (CD) has a rich history in NLP. For example, NeuroLogic ( Lu et al., 2021 ) uses search-based heuristics to satisfy complex logical predicates, and Synchromesh ( Poesia et al., 2022 ) enforces Context-Free Grammars (CFGs) to ensure syntactic correctness in code generation. An approach related to our use case is that of Finite State Transducers (FSTs), which have long been the standard for constrained speech recognition ( Koo et al., 2024 ) . However, FSTs suffer from state explosion when applied to the unstructured, high-cardinality vocabularies found in recommendation systems (often 10 7 + 10^{7}+ items). As observed by Koo et al. (2024) , while FSTs are powerful, their irregularity makes them difficult to parallelize on TPUs/GPUs compared to dense matrix operation-based methods.

[30] h3: 2.3. Hardware-Aware Inference and Acceleration

[31] p: The “Memory Wall” remains the primary bottleneck for Large Language Model inference. Because autoregressive decoding is memory-bandwidth bound, performance is dictated by how fast data moves to the chip’s arithmetic units ( Dao et al., 2022 ) .

[32] p: Pointer Chasing vs. Coalesced Access. Standard trie implementations used in various constrained decoding approaches rely on pointer chasing ( Liao et al., 2025 ) . On modern accelerators (TPUs/GPUs), pointer chasing induces random memory access patterns that lead to uncoalesced loads and cache thrashing. This is antithetical to the design of accelerators, which thrive on static, contiguous memory access (as seen in optimizations like FlashAttention ( Dao et al., 2022 ) ).

[33] p: Accelerator-Compatible Decoding. The recent paper DISC-PPV ( Ye et al., 2025 ) represents the state-of-the-art in adapting constrained decoding to hardware accelerators. The authors implement an on-chip validity check using a flattened sorted array and parallelized binary search, a method they call Parallel Prefix-Verification (PPV). While PPV eliminates the CPU-GPU communication overhead, its reliance on binary search introduces an I/O complexity scaling factor of O ⁡ ( log ⁡ | 𝒞 | ) O(\log|\mathcal{C}|) with respect to the constrained item set size | 𝒞 | |\mathcal{C}| . In ultra-large vocabularies (e.g. 20 20 million items), even logarithmic scaling becomes an I/O bottleneck. Our introduced STATIC approach advances this line of research by replacing the O ⁡ ( log ⁡ | 𝒞 | ) O(\log|\mathcal{C}|) dependent block transfers of PPV with O ⁡ ( 1 ) O(1) vectorized sparse matrix operations, fetching all required working sets in a single coalesced phase.

[34] h3: 2.4. Linearized Tree Structures

[35] p: The concept of flattening tree structures into array-based representations dates back to the Double-Array Trie ( Aoe, 1989 ) , originally designed to improve memory efficiency for string matching. Similarly, the GraphBLAS standard ( Kepner et al., 2016 ) posits that graph algorithms can be expressed as linear algebra operations over sparse semirings.

[36] p: While these concepts are established in theoretical computer science, their application to LLM constrained decoding is novel. We bridge the gap between these classical data structures and modern deep learning compilers (XLA/Inductor). By reformulating trie traversal via sparse matrix operations, we enable the use of high-performance, ML-compiler-accelerated kernels that maintain the parallelism required for real-time recommendation at scale.

[37] figure: Main figure for Sparse Transition Matrix-based Trie Decoding. Figure 1. This figure showcases the full STATIC pipeline. Figures 1a and 1b present the prefix tree construction for the case 𝒱 = { 1 , 2 , 3 } \mathcal{V}=\{1,2,3\} , L = 3 L=3 , and restricted vocabulary 𝒞 = { ( 1 , 2 , 1 ) , ( 3 , 1 , 2 ) , ( 3 , 1 , 3 ) } \mathcal{C}=\{(1,2,1),(3,1,2),(3,1,3)\} . We prepend the letters A , B , C A,B,C to the semantic tokens to denote first, second, and third levels, respectively. The corresponding transition matrix is then shown in Figure 1c, with explicit labels and color-coding. Figure 1d presents the sparse matrix (CSR) representation of the full transition matrix. Figure 1e shows how the sparse matrix is applied to constrain the vocabulary at decoding time. Main figure for Sparse Transition Matrix-based Trie Decoding.

[38] h2: 3. Background

[39] p: In this section, we provide the background necessary to understand our paper and define the technical terminology central to generative retrieval and constrained decoding.

[40] h3: 3.1. Generative Retrieval and Semantic IDs

[41] p: Generative retrieval is a recommendation paradigm wherein a model directly predicts target candidate identifiers token-by-token rather than through nearest-neighbor search in an embedding space. Central to this approach is the concept of the Semantic ID: a discrete, token-based identifier that captures the semantic properties of an item.

[42] p: In the TIGER framework ( Rajput et al., 2023 ) , Semantic IDs are created using a Residual-Quantized Variational AutoEncoder (RQ-VAE). An RQ-VAE first encodes item features into a latent vector 𝐳 \mathbf{z} , which is then iteratively quantized across L L levels. The first-level residual is defined as: 𝐫 1 := 𝐳 \mathbf{r}_{1}:=\mathbf{z} . At each level d d , the residual 𝐫 d \mathbf{r}_{d} is identified with the nearest embedding 𝐞 y d \mathbf{e}_{y_{d}} in a level-specific codebook ℰ d \mathcal{E}_{d} . The index y d y_{d} becomes the d d -th codeword in the Semantic ID. The next-level residual is computed as: 𝐫 d + 1 := 𝐫 d − 𝐞 y d \mathbf{r}_{d+1}:=\mathbf{r}_{d}-\mathbf{e}_{y_{d}} .

[43] p: This recursive approach allows semantically similar items to share prefix tokens, enabling the model to effectively generalize across the item space. The final resulting Semantic ID is simply the tuple comprised of the embedding indices, i.e. ( y 1 , … , y L ) (y_{1},\ldots,y_{L}) .

[44] h3: 3.2. Autoregressive Decoding via Beam Search

[45] p: During inference, the retrieval model autoregressively decodes the token sequences of Semantic IDs. To generate target items we typically employ beam search ( Freitag and Al-Onaizan, 2017 ) over the Semantic ID space (although our approach is also compatible with other decoding methods). Let 𝒱 \mathcal{V} be the vocabulary of semantic tokens and let L L be the fixed length of a Semantic ID. At each step t t , the algorithm maintains a beam search state 𝐒 t \mathbf{S}_{t} which tracks the M M most probable sequences across a batch of size B B . We formally define 𝐒 t \mathbf{S}_{t} as a structure with the following members and accessors:

[46] p: 𝐒 t . tokens ∈ 𝒱 B × M × t \mathbf{S}_{t}.\text{tokens}\in\mathcal{V}^{B\times M\times t} : The token buffer containing the decoded prefixes for each beam.

[47] p: 𝐒 t . scores ∈ ℝ B × M \mathbf{S}_{t}.\text{scores}\in\mathbb{R}^{B\times M} : The cumulative log-probability scores for the sequences.

[48] p: At step t t , the model generates logits 𝐋 t ∈ ℝ B × M × | 𝒱 | \mathbf{L}_{t}\in\mathbb{R}^{B\times M\times|\mathcal{V}|} which are normalized into log-probabilities before selecting the next set of candidates. The cumulative log-probability score is updated by adding the model’s predicted log-probabilities for the next token to the current prefix scores. The top M M candidates with the highest cumulative scores are retained, while others are pruned.

[49] h3: 3.3. Prefix Trees and Constrained Decoding

[50] p: Standard generative models can “hallucinate” identifiers that either (1) do not map to valid items in the corpus or (2) do not map to desirable items (e.g. too old, in the context of freshness). To prevent this, constrained decoding restricts the output to a restricted vocabulary set 𝒞 \mathcal{C} containing only desirable Semantic IDs.

[51] p: Because Semantic IDs are structured as sequences, the restricted vocabulary inherently forms a prefix tree (i.e. trie). Constraints are enforced at each step t t , that is, if appending the current token to the prefix results in a invalid path in the trie, the path is pruned. In practice, the log-probabilities of invalid tokens are set to − ∞ -\infty , ensuring that beam search only selects valid sequences. The challenge addressed in this work is that naive pointer-chasing implementations of trie constraints incur severe latency penalties on hardware accelerators like TPUs/GPUs, making them infeasible in practice.

[52] h2: 4. Methodology

[53] p: We propose an accelerator-native constrained decoding technique designed for LLM-based generative retrieval. Our approach replaces dynamic pointer-chasing CPU-based prefix tree traversals with a static sparse matrix lookup, enabling purely on-device execution (TPU/GPU) compatible with XLA/Inductor compilation.

[54] h3: 4.1. Problem Formulation

[55] p: Recall that 𝒱 \mathcal{V} represents the set of semantic tokens (i.e. indices) in our context, and L L , the fixed length of a Semantic ID. Note that the space of all Semantic IDs is simply the product space 𝒱 L \mathcal{V}^{L} . Although the vocabulary of indices is the same across all levels, the codewords are different, with a different codebook ℰ d \mathcal{E}_{d} trained for each level.

[56] p: The retrieval model generates a sequence (i.e. a Semantic ID) 𝐲 = ( y 1 , … , y L ) \mathbf{y}=(y_{1},\dots,y_{L}) auto-regressively, where y i ∈ 𝒱 y_{i}\in\mathcal{V} . In standard beam search, the validity of a sequence is determined solely by the model’s learned probability distribution P θ P_{\theta} . However, in constrained decoding we require the generated output to belong to a strictly defined subset 𝒞 ⊂ 𝒱 L \mathcal{C}\subset\mathcal{V}^{L} (e.g. a “Freshness” corpus or “Inventory” list). An example of a restricted subset is given in Figure 1 a.

[57] p: We formally define constraint functions F t : 𝒱 t − 1 × 𝒱 → { 0 , 1 } F_{t}:\mathcal{V}^{t-1}\times\mathcal{V}\rightarrow\{0,1\} for 1 ≤ t < L 1\leq t<L by: F t ​ ( y < t , y t ) = 𝕀 ⁡ ( ∃ c ∈ 𝒞 ​ s.t. ​ ( y < t , y t ) ⊑ c ) F_{t}(y_{<t},y_{t})=\mathbb{I}(\exists\>c\in\mathcal{C}\>\text{s.t.}\>(y_{<t},y_{t})\sqsubseteq c) , where 𝕀 ⁡ ( ⋅ ) \mathbb{I}(\cdot) is the indicator function and ⊑ \sqsubseteq denotes prefix inclusion. F t ​ ( y < t , y t ) F_{t}(y_{<t},y_{t}) is an indicator function that returns 1 1 if and only if appending y t y_{t} to the prefix y < t y_{<t} results in a valid prefix in 𝒞 \mathcal{C} . Our goal is to enforce this constraint only during inference, such that P ⁡ ( y t | y < t ) = 0 P(y_{t}|y_{<t})=0 if F t ​ ( y < t , y t ) = 0 F_{t}(y_{<t},y_{t})=0 , with minimal latency overhead.

[58] h3: 4.2. Sparse Transition Matrix (STM)-based Trie Conversion

[59] p: Standard implementations of prefix trees rely on pointer-chasing operations that have a huge CPU callback bottleneck and are poorly supported on accelerators. To resolve this, we flatten the prefix tree into a Compressed Sparse Row (CSR) transition matrix.

[60] p: Let the number of total prefix nodes in the trie be S S . We map every unique prefix node in the tree to a state integer s ∈ [ S ] s\in[S] . We then define a sparse matrix 𝐓 ∈ ℤ S × | 𝒱 | \mathbf{T}\in\mathbb{Z}^{S\times|\mathcal{V}|} where:

[61] table: 𝐓 s , v = { s next s → 𝑣 s n ​ e ​ x ​ t ​ exists 0 otherwise \mathbf{T}_{s,v}=\begin{cases}s_{\text{next}}&s\xrightarrow{v}s_{next}\>\text{exists}\\ 0&\text{otherwise}\\ \end{cases}

[62] p: Conceptually, 0 0 denotes a terminal state where no more transitions are possible (think of it as a “sink”). To better illustrate the idea, we give the conceptual transition matrix for the restricted vocabulary from Figure 1 a in Figure 1 c (corresponding to the trie in Figure 1 b).

[63] h4: 4.2.1. Matrix Construction

[64] p: The construction of 𝐓 \mathbf{T} is performed offline. Given the high sparsity of the vocabulary constraints (often ≤ 0.01 % \leq\!0.01\% of valid paths), the CSR representation is highly memory efficient. In our case, we fill the three parts of the CSR representation as follows:

[65] p: Row Pointers ( 𝐏 \mathbf{P} ): Stores indices for the allowed transitions for current state s s , i.e. these are effectively node pointers.

[66] p: Column Indices ( 𝐂 \mathbf{C} ): Stores the valid token IDs ( v v ) that trigger transitions.

[67] p: Values Array ( 𝐕 \mathbf{V} ): Stores the target state node IDs ( s n ​ e ​ x ​ t s_{next} ).

[68] p: This static structure allows us to utilize hardware-optimized sparse matrix operations rather than dynamic control flow. To illustrate, for the transition matrix in Figure 1 c we provide the CSR arrays in Figure 1 d. Notice, for example, to extract the transitions from Node 4 in Figure 1 c, we would first extract row_start = P ​ [ 4 ] = 5 \texttt{row\_start}=\textbf{P}[4]=5 and row_end = P ​ [ 4 + 1 ] = 7 \texttt{row\_end}=\textbf{P}[4+1]=7 . Then we form the slices:

[69] table: C [ row_start : row_end ] = C [ : 7 ] = [ 2 , 3 ] \displaystyle\textbf{C}[\texttt{row\_start}\!:\!\texttt{row\_end}]=\textbf{C}[5\!:\!7]=[2,3] V [ row_start : row_end ] = V [ : 7 ] = [ 6 , 7 ] \displaystyle\textbf{V}[\texttt{row\_start}\!:\!\texttt{row\_end}]=\textbf{V}[5\!:\!7]=[6,7]

[70] p: to observe that taking “Token 2” from Node 4 leads to Node 6, and taking “Token 3” from Node 4 leads to Node 7. One can confirm that this is indeed correct by noting the transitions present in Figure 1 c.

[71] figure: Algorithm 1 Hardware-Accelerated Constrained Decoding Step Input: Logits 𝐋 t ∈ ℝ B × M × | 𝒱 | \mathbf{L}_{t}\in\mathbb{R}^{B\times M\times|\mathcal{V}|} , Beam State 𝐒 t − 1 \mathbf{S}_{t-1} , Step t t Input: Dense Count d d , Dense Restrict Tensor 𝐃 ∈ ℝ | 𝒱 | × ⋯ × | 𝒱 | ⏞ d ​ times \mathbf{D}\in\mathbb{R}^{\overbrace{|\mathcal{V}|\times\cdots\times|\mathcal{V}|}^{d\>\text{times}}} Input: Constraints: Trans. Matrix 𝐓 \mathbf{T} , Node Indices 𝐧 t − 1 ∈ ℤ B × M \mathbf{n}_{t-1}\in\mathbb{Z}^{B\times M} Output: Updated State 𝐒 t \mathbf{S}_{t} , New Node Indices 𝐧 t \mathbf{n}_{t} 1 Phase 1: Log-Space Projection 2 𝐏 t ← LogSoftmax ​ ( 𝐋 t ) \mathbf{P}_{t}\leftarrow\textnormal{{{LogSoftmax}}}(\mathbf{L}_{t}) // Convert logits to log-probs 3 Phase 2: Constraint Masking // For earlier layers, we employ dense lookups 4 if t − 1 < d t-1<d then 5 ( 𝐧 n ​ e ​ x ​ t , 𝐦 ) ← DenseLookup ​ ( 𝐧 t − 1 , 𝐃 , t − 1 ) (\mathbf{n}_{next},\mathbf{m})\leftarrow\textnormal{{{DenseLookup}}}(\mathbf{n}_{t-1},\mathbf{D},t-1) 6 else 7 ( 𝐧 n ​ e ​ x ​ t , 𝐦 ) ← VNTK ​ ( 𝐧 t − 1 , 𝐓 , t − 1 ) (\mathbf{n}_{next},\mathbf{m})\leftarrow\textnormal{{{VNTK}}}(\mathbf{n}_{t-1},\mathbf{T},t-1) // Execute Algorithm 2 8 end if 9 𝐏 t ′ ← Where ​ ( 𝐦 , 𝐏 t , − ∞ ) \mathbf{P}^{\prime}_{t}\leftarrow\textnormal{{{Where}}}(\mathbf{m},\mathbf{P}_{t},\textnormal{{$-\infty$}}) // Mask invalid transitions 10 Phase 3: Beam Search Optimization 11 ( 𝐒 b ​ e ​ s ​ t , 𝐈 b ​ e ​ s ​ t ) ← BeamSearch ( 𝐏 t ′ , 𝐒 t − 1 . scores , M ) (\mathbf{S}_{best},\mathbf{I}_{best})\leftarrow\textnormal{{{BeamSearch}}}(\mathbf{P}^{\prime}_{t},\mathbf{S}_{t-1}.\text{scores},M) 12 Phase 4: State Update 13 𝐒 t . tokens ← Gather ( 𝐒 t − 1 . tokens , indices = 𝐈 b ​ e ​ s ​ t ) \mathbf{S}_{t}.\text{tokens}\leftarrow\textnormal{{{Gather}}}(\mathbf{S}_{t-1}.\text{tokens},\text{indices}=\mathbf{I}_{best}) 14 𝐒 t . scores ← 𝐒 b ​ e ​ s ​ t \mathbf{S}_{t}.\text{scores}\leftarrow\mathbf{S}_{best} 15 𝐧 t ← Gather ​ ( 𝐧 n ​ e ​ x ​ t , indices = 𝐈 b ​ e ​ s ​ t ) \mathbf{n}_{t}\leftarrow\textnormal{{{Gather}}}(\mathbf{n}_{next},\text{indices}=\mathbf{I}_{best}) // Advance constraint state 16 return 𝐒 t , 𝐧 t \mathbf{S}_{t},\mathbf{n}_{t}

[72] h3: 4.3. Accelerator-Native Decoding Algorithm

[73] p: To achieve high throughput on hardware accelerators, we reformulate the validity check as a vectorized lookup. Critically, we maintain a transition state vector 𝐧 t ∈ ℤ B × M \mathbf{n}_{t}\in\mathbb{Z}^{B\times M} that tracks the current node index in the prefix tree for each beam. Additionally, we employ the following optimization. For a number of layers 0 ≤ d < L 0\leq d<L , we maintain a dense tensor mask 𝐃 ∈ ℝ | 𝒱 | × ⋯ × | 𝒱 | ⏞ d ​ times \mathbf{D}\in\mathbb{R}^{\overbrace{|\mathcal{V}|\times\cdots\times|\mathcal{V}|}^{d\>\text{times}}} that indicates precisely which d d -length prefixes exist in the restricted vocabulary 𝒞 \mathcal{C} . Lookups in this tensor are extremely fast and the construction of 𝐃 \mathbf{D} is a one-time fixed cost; however, 𝐃 \mathbf{D} becomes prohibitively expensive to construct for d ≥ 3 d\geq 3 in most cases due to the fact that | 𝒱 | d |\mathcal{V}|^{d} grows exponentially in d d . Hence, we have d ≤ 2 d\leq 2 for most real-world use cases and rely on the sparse CSR transition matrix for deeper layers. The full sequential constrained decoding process is given in Algorithm 1 . Our approach relies on several hardware-accelerated operations:

[74] p: LogSoftmax ​ ( 𝐱 ) \textbf{LogSoftmax}(\mathbf{x}) : Converts raw logits into normalized log-probabilities according to the following transformation: LogSoftmax ( 𝐱 ) i = x i − log ∑ j = 1 | 𝒱 | exp ( x j ) \text{LogSoftmax}(\mathbf{x})_{i}=x_{i}-\log\sum_{j=1}^{|\mathcal{V}|}\exp(x_{j}) .

[75] p: DenseLookup ​ ( 𝐧 t − 1 , 𝐃 , t − 1 ) \textbf{DenseLookup}(\mathbf{n}_{t-1},\mathbf{D},t-1) : This primitive performs a high-performance lookup on the dense tensor mask 𝐃 \mathbf{D} to identify valid semantic extensions for each beam.

[76] p: VNTK ​ ( 𝐧 t − 1 , 𝐓 , t − 1 ) \textbf{VNTK}(\mathbf{n}_{t-1},\mathbf{T},t-1) : The Vectorized Node Transition Kernel (Algorithm 2 ). It performs a high-performance lookup on the sparse transition matrix 𝐓 \mathbf{T} to identify valid semantic extensions for each beam. It encapsulates the speculative slicing and projection logic required to return the next-node IDs 𝐧 n ​ e ​ x ​ t \mathbf{n}_{next} and the dense log probability mask 𝐦 \mathbf{m} in a single vectorized pass. See Section 4.4 for more detail.

[77] p: Where ​ ( mask , 𝐱 , value ) \textbf{Where}(\text{mask},\mathbf{x},\text{value}) : This conditional operator enforces validity constraints in log-probability space. It prunes invalid paths by setting their scores to − ∞ -\infty where the mask 𝐦 \mathbf{m} is false.

[78] p: BeamSearch ​ ( 𝐏 t ′ , 𝐒 s ​ c ​ o ​ r ​ e ​ s , M ) \textbf{BeamSearch}(\mathbf{P}^{\prime}_{t},\mathbf{S}_{scores},M) : A selection framework that identifies M M most probable valid sequences across the batch. It computes cumulative scores by combining the new masked log-probabilities 𝐏 t ′ \mathbf{P}^{\prime}_{t} with existing prefix scores 𝐒 s ​ c ​ o ​ r ​ e ​ s \mathbf{S}_{scores} and retains the top candidates for the next step.

[79] p: Gather ​ ( 𝐱 , indices ) \textbf{Gather}(\mathbf{x},\text{indices}) : A vectorized selection operator used in the state update phase (Phase 4). It extracts the specific tokens, scores, and constraint states from the candidate pool that correspond to the top-performing beams ( 𝐈 b ​ e ​ s ​ t \mathbf{I}_{best} ).

[80] h3: 4.4. Implementation and Hardware Optimization

[81] p: While the theoretical formulation of STATIC guarantees correctness, achieving negligible latency overhead on modern accelerators requires rigorous alignment with the underlying hardware characteristics. In this section, we detail the vectorized kernel design that makes our approach portable across both TPUs and GPUs.

[82] figure: Algorithm 2 Vectorized Node Transition Kernel (VNTK) Input: Curr. Node n c ​ u ​ r ​ r n_{curr} , Trans. Matrix 𝐓 \mathbf{T} (Row Pointers 𝐏 \mathbf{P} , Columns 𝐂 \mathbf{C} , Values 𝐕 \mathbf{V} ), Step t t Input: (Constant) Token Cardinality | 𝒱 | |\mathcal{V}| , Max Branch Factors 𝐁 \mathbf{B} Output: Next Nodes 𝐧 n ​ e ​ x ​ t \mathbf{n}_{next} , Logit Mask 𝐦 \mathbf{m} 1 Phase 1: Boundary Lookup 2 i ​ d ​ x s ​ t ​ a ​ r ​ t ← 𝐏 ⁡ [ n c ​ u ​ r ​ r ] idx_{start}\leftarrow\mathbf{P}[n_{curr}] 3 N c ​ h ​ i ​ l ​ d ← 𝐏 ⁡ [ n c ​ u ​ r ​ r + 1 ] − i ​ d ​ x s ​ t ​ a ​ r ​ t N_{child}\leftarrow\mathbf{P}[n_{curr}+1]-idx_{start} // Compute # of children 4 Phase 2: Speculative Slicing // Slice fixed size 𝐁 t \mathbf{B}_{t} regardless of actual child count 5 𝐝 c ​ o ​ l ← DynamicSlice ​ ( 𝐂 , start = i ​ d ​ x s ​ t ​ a ​ r ​ t , len = 𝐁 t ) \mathbf{d}_{col}\leftarrow\textnormal{{{DynamicSlice}}}(\mathbf{C},\text{start}=idx_{start},\text{len}=\mathbf{B}_{t}) 6 𝐝 v ​ a ​ l ← DynamicSlice ​ ( 𝐕 , start = i ​ d ​ x s ​ t ​ a ​ r ​ t , len = 𝐁 t ) \mathbf{d}_{val}\leftarrow\textnormal{{{DynamicSlice}}}(\mathbf{V},\text{start}=idx_{start},\text{len}=\mathbf{B}_{t}) 7 Phase 3: Sanitization (Branch-Free) 8 J ← Range ​ ( 𝐁 t ) J\leftarrow\textnormal{{{Range}}}(\mathbf{B}_{t}) // Generate vector [ 0 , … , 𝐁 t − 1 ] [0,\dots,\mathbf{B}_{t}-1] 9 𝐦 v ​ a ​ l ​ i ​ d ← ( J < N c ​ h ​ i ​ l ​ d ) \mathbf{m}_{valid}\leftarrow(J<N_{child}) // Identify valid slots 10 𝐭 v ​ a ​ l ​ i ​ d ← Where ​ ( 𝐦 v ​ a ​ l ​ i ​ d , 𝐝 c ​ o ​ l , { } ) \mathbf{t}_{valid}\leftarrow\textnormal{{{Where}}}(\mathbf{m}_{valid},\mathbf{d}_{col},\textnormal{{$\{\}$}}) 11 𝐧 n ​ e ​ x ​ t ← Where ​ ( 𝐦 v ​ a ​ l ​ i ​ d , 𝐝 v ​ a ​ l , 0 ) \mathbf{n}_{next}\leftarrow\textnormal{{{Where}}}(\mathbf{m}_{valid},\mathbf{d}_{val},\textnormal{{$0$}}) 12 Phase 4: Projection // Create dense boolean mask for Softmax 13 𝐦 ← Scatter ​ ( indices = 𝐭 v ​ a ​ l ​ i ​ d , values = 𝐦 v ​ a ​ l ​ i ​ d ) \mathbf{m}\leftarrow\textnormal{{{Scatter}}}(\text{indices}=\mathbf{t}_{valid},\text{values}=\mathbf{m}_{valid}) 14 return 𝐧 n ​ e ​ x ​ t , 𝐦 \mathbf{n}_{next},\mathbf{m}

[83] p: The core engineering challenge in constrained decoding is handling the dynamic nature of the prefix tree (where nodes possess a varying number of children) within the static execution model of hardware accelerators. Standard pointer-chasing traversals are inefficient: on TPUs (XLA), dynamic branching triggers costly graph recompilation or forces the use of serial ‘while’ loops that prevent hardware pipelining; on GPUs, processing beams with mismatched child counts leads to GPU warp divergence, where threads must wait for the longest path to finish, destroying SIMT parallelism.

[84] p: To overcome these bottlenecks, we implement a branch-free transition kernel (Algorithm 2 ). For efficient slicing, it becomes critical to introduce some new definitions. Consider the prefix tree corresponding to a sparse transition matrix 𝐓 \mathbf{T} . For a node n n in the tree at level ℓ \ell , let the number of children be b n ℓ b^{\ell}_{n} . Given that the tree has L L levels, let the set of all nodes at level ℓ ∈ [ L ] \ell\in[L] be N ℓ N_{\ell} and define the vector 𝐁 ∈ ℝ L \mathbf{B}\in\mathbb{R}^{L} such that 𝐁 ℓ = max n ∈ N ℓ ⁡ b n ℓ \mathbf{B}_{\ell}=\max_{n\in N_{\ell}}b^{\ell}_{n} . That is, 𝐁 \mathbf{B} is the level-indexed vector of max branch factors exhibited by the tree. Note that computing this vector is a one-time fixed cost per transition matrix 𝐓 \mathbf{T} . Our algorithm takes this vector as an input. Moreover, Algorithm 2 relies on the following vectorized primitive operations:

[85] p: DynamicSlice ​ ( 𝐌 , start , len ) \textbf{DynamicSlice}(\mathbf{M},\text{start},\text{len}) : Extracts a contiguous sub-tensor of fixed length l ​ e ​ n = 𝐁 t len=\mathbf{B}_{t} from the data matrix 𝐌 \mathbf{M} starting at a dynamic offset ( s ​ t ​ a ​ r ​ t start ). Recall decoding step t t is synonymous with level ℓ \ell in the underlying prefix tree.

[86] p: Range ​ ( c ) \textbf{Range}(c) : Generates a constant sequence vector [ 0 , … , c − 1 ] [0,\dots,c-1] used for index-based masking and sanitization of the speculatively sliced children.

[87] p: Scatter ​ ( indices , values ) \textbf{Scatter}(\text{indices},\text{values}) : A projection operator that converts the sparse list of valid tokens into a dense boolean mask 𝐦 \mathbf{m} of size | 𝒱 | |\mathcal{V}| . This mask is applied directly to the model’s log-probabilities in the main decoding step to enforce the prefix-tree constraints.

[88] p: As shown in Phase 2, the kernel always slices a fixed number of entries 𝐁 t \mathbf{B}_{t} for any given level t t regardless of the actual child count. If a node has fewer than 𝐁 t \mathbf{B}_{t} children, we use a Range -generated vector to create a boolean mask 𝐦 v ​ a ​ l ​ i ​ d \mathbf{m}_{valid} and the Where operator to sanitize the result. This ensures that the arithmetic units of the GPU/TPU remain fully saturated and that the entire decoding step remains a single, static computation graph. We discuss additional relevant hardware considerations of our method in Appendix A . We also benchmark our method for high maximum branch factors in Appendix D and demonstrate linear scaling on this axis. Importantly, we note that for sufficiently large | 𝒱 | |\mathcal{V}| and practical ranges of | 𝒞 | |\mathcal{C}| , the max branch factor will actually remain quite low for later layers, since the number of children | 𝒱 | ℓ |\mathcal{V}|^{\ell} grows exponentially with level ℓ \ell and quickly exceeds the constraint set size | 𝒞 | |\mathcal{C}| .

[89] h2: 5. Large-scale Deployment on YouTube

[90] p: By testing STATIC at YouTube scale, we seek to evaluate the STATIC algorithm along three dimensions critical for industrial deployment:

[91] p: System Efficiency : We measure latency and throughput on TPU accelerators compared to baselines.

[92] p: Scalability : We analyze the storage footprint and runtime as both constraint set size and vocabulary size increase.

[93] p: Online Product Impact : We quantify the improvement of recommendation quality and user satisfaction from applying constrained decoding in a live production environment.

[94] h3: 5.1. Experimental Setup

[95] p: We conduct our evaluation on a large-scale video recommendation corpus from YouTube. The videos are tokenized into Semantic IDs (SIDs) ( Rajput et al., 2023 ) with L = 8 L=8 discrete tokens and token cardinality | 𝒱 | = 2048 |\mathcal{V}|=2048 . The total recommendable corpus is on the order of 100 100 million to 1 1 billion items, and the unconstrained model can recommend any item from this set. We fix d = 2 d=2 as an input to Algorithm 1 and maintain the dense tensor mask 𝐃 ∈ ℝ 2048 × 2048 \mathbf{D}\in\mathbb{R}^{2048\times 2048} for early lookups; we use the CSR sparse matrix representation for later levels.

[96] p: The model is a Gemini-based generative retrieval model similar to PLUM ( He et al., 2025 ) , served with a batch size of 2 (per chip) and a beam size of M = 70 M=70 . The model is based on a non-Mixture-of-Experts (MoE) architecture with 3 billion dense parameters. All benchmark experiments are conducted on Google TPU v6e accelerators.

[97] figure: Table 1. Latency Overhead per Decoding Step on a Large-scale Video Recommendation Corpus with 𝟐𝟎 \mathbf{20} Million Constrained Vocabulary Items. STATIC (Ours) achieves minimal latency overhead relative to baselines. Method Latency (ms) % of Inference Unconstrained + 0.0 +0.0 – PPV Exact ( Ye et al., 2025 ) + 34.1 +34.1 260 % 260\% CPU Trie + 31.3 +31.3 239 % 239\% Hash Bitmap + 12.3 +12.3 94.0 % 94.0\% PPV Approximate ( Ye et al., 2025 ) + 1.56 +1.56 11.9 % 11.9\% STATIC (Ours) + 0.033 \mathbf{+0.033} 0.25 % \mathbf{0.25\%}

[98] h3: 5.2. System Efficiency Analysis

[99] p: We limit our attention to a constrained vocabulary (target set) consisting of a “fresh video” subset containing approximately 20 20 million high-quality items uploaded in the last 7 7 days (relative to the experiment date). This setup represents a restrictive environment for constrained decoding: the valid subset is sparse, yet large enough ( 20 20 million items) to make naive enumeration infeasible.

[100] p: We compare our STATIC approach against several distinct implementations commonly found in academic literature and production systems:

[101] p: Unconstrained: Standard beam search with no validity checks. This represents the lower bound on latency.

[102] p: CPU Trie: A standard prefix tree stored in CPU memory using JAX’s PyTree data structure (Python dictionary). At every decoding step, the TPU halts, sends partial beams to the CPU, waits for the validity mask, and resumes.

[103] p: PPV Exact ( Ye et al., 2025 ) : Following Ye et al. (2025) , we store valid SIDs in a sorted flat array on TPU and perform binary search to verify every candidate extension. In the original paper, the authors consider only the top 50 50 logits of the vocabulary per decoding step. This is suboptimal for beam search with larger fan-out since constrained set items frequently fall outside of the top 50 50 logits. Thus, in this baseline, we consider the PPV method using all 2048 2048 logits. This yields an exact solution but is significantly slower than PPV Approximate below, due to PPV’s linear scaling with the number of logits.

[104] p: PPV Approximate ( Ye et al., 2025 ) : Just as above, we perform binary search on a sorted flat SID array for every candidate extension; however, as in the original paper, this baseline only verifies the top 50 50 logits per decoding step. This gives only approximate solutions for the reasons mentioned above, and is not directly comparable to STATIC.

[105] p: Hash Bitmap: A Bloom-filter ( Bloom, 1970 ) style approach where valid prefixes are hashed. This method introduces false positives (with a non-negligible 2.1% false positive rate in our Table 1 evaluation), so it is not directly comparable to STATIC, but useful as a reference.

[106] p: We measured the latency of the constraint enforcement logic per decoding step, and summarized the results in Table 1 , where we give the means over 100 100 trials. Our STATIC approach achieves a latency overhead of + 0.033 0.033 ms per decoding step, only taking 0.25 0.25 % of the inference time for a 3 billion parameter model. In contrast, the “CPU Trie” method incurs a massive penalty ( 31.3 31.3 ms, 948 × 948\text{\small$\times$} higher than STATIC) due to the PCIe transfer overhead and synchronization locks between the TPU and CPU. Crucially, we outperform the “PPV Exact” baseline by a factor of 1033 × 1033\text{\small$\times$} ( 34.1 34.1 ms vs. 0.033 0.033 ms) and even the “PPV Approximate” baseline by factor of 47 × 47\text{\small$\times$} ( 1.56 1.56 ms vs. 0.033 0.033 ms). While PPV’s binary search is technically “on-device” and vectorized, it suffers from logarithmic scaling of I/O complexity with respect to the constraint set size | 𝒞 | |\mathcal{C}| (on top of linear scaling with respect to number of logits considered), whereas STATIC reduces the I/O complexity to O ⁡ ( 1 ) O(1) using the single-pass VNTK kernel (Algorithm 2 ).

[107] h3: 5.3. Scalability

[108] p: While a naive boolean mask of the entire Semantic ID space would be petabytes in size, our STATIC approach requires only approximately 90 90 MB of memory for every 1 million restricted vocabulary items in this setting. That is, for our tested restricted vocabulary of 20 20 million items, we expect a maximal HBM usage of ≈ 1.8 \approx 1.8 GB, which we can further tighten to ≈ 1.5 \approx 1.5 GB via the analysis in Appendix B . In practice, the required memory is usually ≤ 75 % \leq 75\% of this upper limit. We elaborate on the derivations and why this is the case in Appendix B . The crucial takeaway is that the memory usage is tied directly to the storage of the dense tensor mask 𝐃 \mathbf{D} and the sparse CSR matrix, which is tied to the number of nodes in the underlying trie. Given a vocabulary size | 𝒱 | |\mathcal{V}| , Semantic ID length L L , dense layer count d d , number of constraints | 𝒞 | |\mathcal{C}| , storage cost per node of K 1 K_{1} bytes, and storage cost per dense state of K 2 K_{2} bytes, the upper bound on memory usage (in bytes) is given by:

[109] table: U max ​ ( K 1 , K 2 , | 𝒱 | , | 𝒞 | , L , d ) = ( 1 8 + K 2 ) ​ | 𝒱 | d + K 1 ⋅ ∑ ℓ = d + 1 L min ⁡ ( | 𝒱 | ℓ , | 𝒞 | ) U_{\text{max}}(K_{1},K_{2},|\mathcal{V}|,|\mathcal{C}|,L,d)=\left(\frac{1}{8}+K_{2}\right)|\mathcal{V}|^{d}+K_{1}\cdot\sum_{\ell=d+1}^{L}\min(|\mathcal{V}|^{\ell},|\mathcal{C}|)

[110] p: Additionally, STATIC’s time complexity scales logarithmically with respect to constraint set size and maintains low latency relative to all measured baselines across a wide range of | 𝒞 | |\mathcal{C}| . A direct comparison with the Table 1 baselines is given in Figure 2 , where we generate constraint sets uniformly at random, fixing | 𝒱 | = 2048 |\mathcal{V}|=2048 , L = 8 L=8 and vary only | 𝒞 | |\mathcal{C}| from 10 5 10^{5} to 10 8 10^{8} . The means over 100 100 trials are plotted and the shaded region indicates one standard deviation above and below the mean 2 2 2 The | 𝒞 | = 10 8 |\mathcal{C}|=10^{8} data point for CPU Trie is missing due to an Out-Of-Memory error. .

[111] figure: Figure 2. Scaling of different constraint decoding methods relative to constraint set size (log-log scale), fixing | 𝒱 | = 2048 |\mathcal{V}|=2048 . STATIC considerably outperforms existing methods.

[112] p: Furthermore, STATIC exhibits almost constant latency with respect to the SID vocabulary size | 𝒱 | |\mathcal{V}| , as shown in Figure 3 , where we generate constraint sets uniformly at random just as above, fixing | 𝒞 | = 10 7 |\mathcal{C}|=10^{7} , L = 8 L=8 , and vary only | 𝒱 | |\mathcal{V}| from 256 to 32k. In theory, the pure sparse matrix look-ups scale with maximum branch factor (as shown in Algorithm 2 ), whose average (under mild assumptions) scales linearly with | 𝒱 | |\mathcal{V}| . However, since we employ a dense mask with O ⁡ ( 1 ) O(1) look-up for the highly saturated first d = 2 d=2 layers, the sparse look-ups happen for later layers with small constant maximum branch factors. As such, STATIC exhibits near constant scaling with | 𝒱 | |\mathcal{V}| . In almost all production systems ( He et al., 2025 ; Zhou et al., 2025a ) as of 2025 2025 , | 𝒱 | ≤ 8192 |\mathcal{V}|\leq 8192 , meaning STATIC exhibits consistently low latency across all current real-world settings. Exact numbers for Figures 2 and 3 are given in Appendix C .

[113] figure: Figure 3. Scaling of different constraint decoding methods relative to SID vocabulary size | 𝒱 | |\mathcal{V}| (log-log scale) at | 𝒞 | = 10 7 |\mathcal{C}|=10^{7} . STATIC compares favorably for all tested SID vocab sizes.

[114] h3: 5.4. Online A/B Testing

[115] p: We deployed a STATIC-enabled PLUM-based generative retrieval model across multiple use cases in the YouTube ecosystem. In one setting, we used it as an additional candidate source to a short-form video product’s “Home Feed” with a “Last 7 Days” freshness constraint, and conducted A/B experiments to measure the impact. The results are shown in Table 2 .

[116] p: As expected, STATIC achieved 100% compliance with the specified constraint. A standard generative retrieval model without this constraint would frequently generate SIDs for older videos, whereas the STATIC model strictly produced valid 7-day fresh videos.

[117] p: We observed a significant increase in the consumption of fresh content: as given in Table 2 , we note a + 5.1 % +5.1\% increase in 7-day fresh video views and a + 2.9 % +2.9\% increase in 3-day fresh video views.

[118] p: Moreover, we observed a positive impact on user experience metrics: the click-through rate (CTR) increased by + 0.15 % 0.15\% and user satisfaction of a strategic user segment increased by + 0.15 0.15 %. This is a significant improvement and shows the positive impact of recommending more high-quality fresh videos.

[119] figure: Table 2. Online A/B Test Results for “Home Feed” Impact with the “Last 7 Days” Freshness Constraint. Metric Impact 95 % 95\% Confidence Interval 7 Day Fresh Views + 5.1 % +5.1\% [ 5.0 % 5.0\% , 5.2 % 5.2\% ] 3 Day Fresh Views + 2.9 % +2.9\% [ 2.8 % 2.8\% , 3.0 % 3.0\% ] Click-Through Rate + 0.15 % +0.15\% [ 0.01 % 0.01\% , 0.29 % 0.29\% ] Strategic User Segment Satisfaction + 0.15 % +0.15\% [ 0.03 % 0.03\% , 0.27 % 0.27\% ]

[120] h2: 6. Cold-Start Retrieval on Amazon Reviews Datasets

[121] p: A long-standing drawback of generative retrieval is its inability to generalize to cold-start items ( Yang et al., 2024 ) . Here, we show how one can use constrained decoding on the cold-start item set to considerably improve cold-start performance. We use the Amazon Reviews ( He and McAuley, 2016 ) datasets to showcase a viable set-up and the associated benefits.

[122] h3: 6.1. Experimental Setup

[123] p: The Amazon items are tokenized into Semantic IDs (SIDs) by training separate RQ-VAE ( Rajput et al., 2023 ) models to quantize the items of each Amazon Reviews subdataset separately, with L = 4 L=4 discrete tokens and token cardinality | 𝒱 | = 256 |\mathcal{V}|=256 . Each subdataset’s valid item corpus consists of anywhere from 10 10 to 20 20 thousand items, and the unconstrained model can recommend any item from this corpus.

[124] p: We train a separate generative retrieval model on the sequences from each Amazon subdataset based on the Gemma ( Kamath et al., 2025 ) architecture with 1 billion dense parameters, served with a batch size of 16 16 and a beam size of M = 20 M=20 . All experiments are conducted on a Google TPU v6e.

[125] h3: 6.2. Cold-Start Results

[126] p: We perform cold-start experiments in the following way. For a given Amazon item, we define its “age” by the age of its oldest review. Thereafter, for each Amazon subdataset, we isolate the newest 2 % 2\% (and separately, 5 % 5\% ) of the items into a cold-start set. We filter out all item sequences that do not contain any items from this set, and train the models on these “no cold-start train sequences.” We evaluate the models on the “cold-start test sequence” set which contains sequences that have cold-start items as targets. We tested the following approaches for retrieval:

[127] p: Unconstrained: Beam search with no validity checks.

[128] p: Constrained Random Guessing: A baseline that guesses items uniformly at random from the constraint set.

[129] p: STATIC (Ours): Our proposed method, where the model decodes from the Transformer while restricting to the cold-start item set at every step.

[130] p: Table 3 shows Recall@1 metrics for the “cold-start test sequences.” In both the 2 % 2\% and 5 % 5\% cold-start settings, STATIC improves over the unconstrained and constrained random guessing approaches considerably, showing that one can attain nontrivial cold-start performance with generative retrieval using constrained decoding alone .

[131] figure: Table 3. Comparison of Unconstrained and Constrained Decoding Performance on Amazon Cold-start Items. All values given are Recall@1 percentages. Subdataset Method 2 % 2\% Cold-start 5 % 5\% Cold-start Beauty Unconstrained 0.00 % 0.00\% 0.00 % 0.00\% Const. Random 0.42 % 0.42\% 0.17 % 0.17\% STATIC 4.29 % \mathbf{4.29\%} 1.60 % \mathbf{1.60\%} Sports & Outdoors Unconstrained 0.00 % 0.00\% 0.00 % 0.00\% Const. Random 0.27 % 0.27\% 0.11 % 0.11\% STATIC 1.24 % \mathbf{1.24\%} 1.17 % \mathbf{1.17\%} Toys & Games Unconstrained 0.00 % 0.00\% 0.00 % 0.00\% Const. Random 0.42 % 0.42\% 0.17 % 0.17\% STATIC 4.39 % \mathbf{4.39\%} 2.25 % \mathbf{2.25\%}

[132] h2: 7. Conclusion

[133] p: Generative retrieval holds the promise of leveraging LLMs for next-generation recommendations in myriad real-world settings, but its adoption in industry has been hindered by the lack of a controllable output space. In this work, we bridged the gap between prefix tree-based constraints and vector-based hardware (TPUs/GPUs). Regarding trie-constrained decoding, the authors of Ye et al. (2025) claim: “whether an efficient GPU trie algorithm exists remains to be [seen].” This is a hypothesis that we answer in the affirmative with the contribution in our paper. The STATIC framework transforms pointer-chasing trie lookups into vectorized sparse matrix operations, achieving a 47 47 – 1033 × 1033\text{\small$\times$} speedup over alternative on-device methods. We demonstrated the effectiveness of this approach in production environments serving billions of users, showing that strict constraints can be enforced at scale without compromising serving latency. Moreover, we demonstrated the viability of improving cold-start performance through constrained-decoding alone on the Amazon Reviews ( He and McAuley, 2016 ) datasets.

[134] p: Future Work. Currently the sparse transition matrix construction is an offline process. An important future extension is to develop dynamic sparse updates, which would allow for real-time inventory changes without full model recompilation.

[135] h2: References

[136] p: Appendix

[137] h2: Appendix A Hardware Optimization: A Detailed Discussion

[138] p: We shall now discuss some of the additional hardware-related details of our constrained decoding implementation.

[139] h3: A.1. The JIT Compilation Challenge and Data Structures

[140] p: A unique constraint of XLA (Accelerated Linear Algebra) compilers used for TPUs is the static shape requirement for tensors. The compiler must know the exact dimensions of all tensors at compile time to generate optimized fusion kernels. Standard trie traversals are inherently dynamic: node A A may have 2 2 children, while node B B may have 1000 1000 . In a CPU environment, one would simply allocate dynamic vectors. Chasing pointers with dynamic vectors, in XLA, would trigger the compilation error “ConcretizationTypeError”, indicating that an abstract tracer value was encountered where a concrete value was expected.

[141] p: Our Vectorized Node Transition Kernel (VNTK) (Algorithm 2 ) addresses this by converting the dynamic traversal into a static gather operation. Instead of processing a variable number of children, we process precisely B ℓ B_{\ell} , where this value is the maximum branch factor at level ℓ \ell (as defined in Section 4 ). We then use a vectorized Gather operation (e.g., jnp.take with mode=‘fill’ ) to fetch exactly 𝐁 ℓ \mathbf{B}_{\ell} potential transitions for every beam in parallel.

[142] p: To handle nodes with N c ​ h ​ i ​ l ​ d < 𝐁 ℓ N_{child}<\mathbf{B}_{\ell} children, we compute a validity mask on the fly:

[143] table: m v ​ a ​ l ​ i ​ d = Range ​ ( 𝐁 ℓ ) < N c ​ h ​ i ​ l ​ d m_{valid}=\text{Range}(\mathbf{B}_{\ell})<N_{child}

[144] p: We then use this boolean mask to zero out invalid entries in the score calculation. This transformation converts a dynamic control flow problem (“loop N N times”) into a static data flow problem (“gather fixed 𝐁 ℓ \mathbf{B}_{\ell} elements and mask”). This ensures the entire decoding step remains a single, static XLA graph, enabling full loop unrolling and pipelining on TPU systolic arrays.

[145] h4: A.1.1. Stacked CSR Layout

[146] p: To further minimize memory access latency within the VNTK, we employ a stacked CSR memory layout. In a standard Compressed Sparse Row (CSR) format, column indices and data values (next-state pointers) are stored in separate arrays, typically requiring two distinct memory fetches per transition. In STATIC, we interleave these into a single ( N e ​ d ​ g ​ e ​ s , 2 ) (N_{edges},2) tensor. This alignment allows the accelerator to coalesce reads, retrieving both the candidate token ID and the pointer to the next node in a single memory transaction. This optimization effectively halves the number of random memory accesses.

[147] h4: A.1.2. Dense Mask Optimization

[148] p: While sparse traversal is efficient for deep levels of the trie, the initial layers exhibit an extremely high branching factor due to the congestion of common prefixes. As analyzed in the memory usage model (Appendix B ), the number of unique nodes at a shallow level ℓ \ell grows as | 𝒱 | ℓ |\mathcal{V}|^{\ell} , making sparse gathers computationally inefficient.

[149] p: To address this, we introduce a dense layer cutoff parameter, d d . For the first d d decoding steps (where 0 ≤ d < L 0\leq d<L ), we bypass the VNTK and utilize a dense tensor mask optimization. We pre-compute a dense boolean tensor of shape | 𝒱 | × ⋯ × | 𝒱 | ⏞ d ​ times \overbrace{|\mathcal{V}|\times\cdots\times|\mathcal{V}|}^{d\>\text{times}} (bit-packed for storage efficiency) that represents all valid prefixes of length d d . During the first d d steps, validity is checked via direct index lookups into this dense tensor. This hybrid approach allows us to trade a small amount of static memory (for d ≤ 2 d\leq 2 ) for a significant throughput gain in the most computationally expensive layers of the retrieval process. In our experiments for YouTube in Section 5 , we set d = 2 d=2 , effectively densifying the first two layers of the trie.

[150] h3: A.2. Cross-Platform Portability (JAX & PyTorch)

[151] p: While our primary implementation utilizes JAX for XLA compilation, the STATIC design is inherently portable to PyTorch and CUDA environments. The shift to a Gather -based kernel unifies the implementation strategy across frameworks:

[152] p: JAX/XLA : The kernel relies on jnp.take (Gather). This operation aligns perfectly with the hardware’s scatter-gather capabilities and allows the XLA compiler to fuse the index computation and memory fetch into a single optimized kernel.

[153] p: PyTorch/Inductor : The logic translates directly to

[154] p: torch.gather . On GPUs, our stacked CSR layout ensures coalesced memory access. When a GPU warp of 32 threads fetches transitions for 32 different beams, the contiguous storage of the transition matrix minimizes the number of cache lines fetched. This contrasts sharply with pointer-based tries, which result in random memory access patterns (uncoalesced loads) that stall execution units.

[155] h3: A.3. Memory Footprint

[156] p: In large-scale serving setups (e.g., TPU v6e Pods or H100 Clusters), LLM parameters are typically sharded across devices. However, the sparse transition matrix (representing the constraints) is relatively compact. For a constrained vocabulary of 20 20 million items in the context of Section 5 , the sparse representation requires only approximately 1.5 1.5 GB of memory. Consequently, we adopt a replication strategy: the sparse transition matrix is replicated on the HBM (High-Bandwidth Memory) of every device. This eliminates the need for cross-chip communication (All-Gather or All-Reduce) during the constraint check. Each chip independently computes the validity mask for its local batch of beams, preserving the linear scalability of the serving system.

[157] p: As item corpora scale toward billions, future research should explore hierarchical storing or sharding strategies to maintain this linear scalability without saturating device memory.

[158] h2: Appendix B Analysis of STATIC Memory Usage

[159] p: We present an analysis of the HBM memory usage of our STATIC method.

[160] h3: B.1. Absolute Upper Bound

[161] p: Given that the core memory usage for STATIC lies in the storage of the associated trie (which represents the restricted vocabulary) and the dense tensor mask 𝐃 \mathbf{D} , we focus our analysis in this direction. Note that the storage associated with the dense tensor mask framework is simply the cost of storing | 𝒱 | d |\mathcal{V}|^{d} bits and | 𝒱 | d |\mathcal{V}|^{d} state IDs. The total storage cost for a trie in CSR format is a function of the number of unique prefix nodes at each level ℓ \ell of the tree. For a restricted vocabulary of | 𝒞 | |\mathcal{C}| items, where each item is a Semantic ID (SID) of length L L and each token has a vocabulary size | 𝒱 | |\mathcal{V}| , the number of unique nodes at level ℓ \ell ( N ℓ N_{\ell} ) is strictly limited by two factors:

[162] p: Level Capacity : The maximum possible unique sequences of length ℓ \ell , which is | 𝒱 | ℓ |\mathcal{V}|^{\ell} .

[163] p: Total Constraints : The total number of unique constraint items | 𝒞 | |\mathcal{C}| , as no level can have more unique prefixes than there are total items in the vocabulary.

[164] p: The absolute upper bound for nodes at level ℓ \ell is therefore:

[165] table: N ℓ ≤ min ⁡ ( | 𝒱 | ℓ , | 𝒞 | ) N_{\ell}\leq\min(|\mathcal{V}|^{\ell},|\mathcal{C}|)

[166] p: The total storage upper bound in bytes, U max ​ ( K 1 , K 2 , | 𝒱 | , | 𝒞 | , L , d ) U_{\text{max}}(K_{1},K_{2},|\mathcal{V}|,|\mathcal{C}|,L,d) , is given by a contribution of ( 1 8 + K 2 ) ​ | 𝒱 | d (\frac{1}{8}+K_{2})|\mathcal{V}|^{d} for the dense tensor mask ( 1 1 bit for the mask and K 2 K_{2} bytes per state, where K 2 = 4 K_{2}=4 typically), as well as by multiplying the sum of the per-level prefix node upper bounds for later levels by the storage cost per node K 1 K_{1} (typically 12 bytes, due to the three arrays of the CSR sparse matrix format):

[167] table: U max ​ ( K 1 , K 2 , | 𝒱 | , | 𝒞 | , L , d ) = ( 1 8 + K 2 ) ​ | 𝒱 | d + K 1 ⋅ ∑ ℓ = d + 1 L min ⁡ ( | 𝒱 | ℓ , | 𝒞 | ) U_{\text{max}}(K_{1},K_{2},|\mathcal{V}|,|\mathcal{C}|,L,d)=\left(\frac{1}{8}+K_{2}\right)|\mathcal{V}|^{d}+K_{1}\cdot\sum_{\ell=d+1}^{L}\min(|\mathcal{V}|^{\ell},|\mathcal{C}|)

[168] h3: B.2. Calculation for YouTube

[169] p: We compute the upper bound for the YouTube setting in Section 5 . Our main configuration variables are fixed to | 𝒱 | = 2048 |\mathcal{V}|=2048 , L = 8 L=8 , K 1 = 12 K_{1}=12 , K 2 = 4 K_{2}=4 , and d = 2 d=2 . Note since we have 20 20 million constraints in the restricted vocabulary, we also have | 𝒞 | = 20 ⋅ 10 6 |\mathcal{C}|=20\cdot 10^{6} . Now we compute the total memory usage

[170] p: Dense Mask Phase ( ℓ = 1 , 2 \ell=1,2 ):

[171] p: The number of bytes we need to store the dense mask is simply ( 1 8 + 4 ) ⋅ 2048 2 = 17301504 \left(\frac{1}{8}+4\right)\cdot 2048^{2}=17301504 bytes, or ≈ 17.3 \approx 17.3 MB.

[172] p: Constraint Phase ( ℓ ≥ 3 \ell\geq 3 ):

[173] p: For 3 ≤ ℓ ≤ 8 3\leq\ell\leq 8 , the capacity | V | n |V|^{n} is significantly larger than | 𝒞 | |\mathcal{C}| (e.g., | V | 3 ≈ 8.5 |V|^{3}\approx 8.5 billion). Hence, each of these 6 6 levels contributes | 𝒞 | ⋅ 12 |\mathcal{C}|\cdot 12 bytes.

[174] p: Contribution: ( L − 2 ) ⋅ | 𝒞 | ⋅ 12 = 6 ⋅ 20 ⋅ 10 6 ⋅ 12 = 1.44 (L-2)\cdot|\mathcal{C}|\cdot 12=6\cdot 20\cdot 10^{6}\cdot 12=1.44 GB.

[175] p: Our maximum per-chip usage is thus ≈ 1.46 ​ GB \approx\!1.46\>\text{GB} , validating our claim of approximately 1.5 1.5 GB of HBM usage for 20 20 million constraints. Due to the fact that the YouTube video distribution is highly non-uniform and exhibits significant clustering ( He et al., 2025 ) , the semantic ID distribution will also, which produces a significant amount of collision in the prefix space. As such, for most restrict vocabularies, the actual HBM usage will be much less than this upper bound. In practice, we note that our utilization is ≤ 75 % \leq\!75\% of this amount.

[176] h3: B.3. Capacity Planning

[177] p: In the context of our YouTube setting (Section 5 ), we use the rule of thumb that every 1 million constraints introduce an additional ≈ 90 \approx 90 MB of HBM usage. This approximation is valid because the storage cost is dominated by the constraint phase described in the previous section.

[178] p: As shown above, the dense mask phase (early levels) contribution remains constant (for fixed d d ), while each additional level in the constraint phase adds exactly | 𝒞 | × K 1 |\mathcal{C}|\times K_{1} bytes to the storage cost.

[179] p: When 𝒞 \mathcal{C} is 1 million:

[180] p: Dense Mask Phase Contribution : Only ( 1 8 + 4 ) ⋅ 2048 2 = 17301504 \left(\frac{1}{8}+4\right)\cdot 2048^{2}=17301504 bytes, or ≈ 17.3 \approx 17.3 MB.

[181] p: Constraint Phase Contribution : For | 𝒞 | = 10 6 |\mathcal{C}|=10^{6} , we see the total contribution is 6 ⋅ 10 6 ⋅ 12 ​ bytes = 72 6\cdot 10^{6}\cdot 12\>\text{bytes}=72 MB.

[182] p: Total : 17.3 ​ MB + 72 ​ MB ≈ 90 ​ MB 17.3\>\text{MB}+72\>\text{MB}\approx 90\>\text{MB} per million items.

[183] p: For the production-scale restrict corpus in Appendix B.2 of 20 20 million items, we saw the transition to the constraint phase happen later, resulting in an average of ≈ 𝟕𝟑 ​ MB \approx\!\mathbf{73\>\text{MB}} per 1 million items, making 90 90 MB a highly reliable linear upper bound approximation for capacity planning. A similar rule-of-thumb can be computed for different values of L L , | 𝒱 | |\mathcal{V}| , and | 𝒞 | |\mathcal{C}| using the principles laid out in this appendix section.

[184] h2: Appendix C Detailed Latency Analysis

[185] p: In this section, we present a fine-grained latency overhead analysis of our STATIC method in the setting of Section 5 compared to the baselines in Table 1 . All numbers given represent the per-step latency throughout the full decoding (over L = 8 L=8 decoding steps). All values represent the additional latency (in milliseconds) incurred by the constraint enforcement logic relative to the unconstrained baseline (which performs no masking), calculated over 100 100 trials.

[186] p: The precise numbers (means and standard deviations) for Figure 2 are given in Table 4 a, with the exclusion of the N = 2 ⋅ 10 7 N=2\cdot 10^{7} row, which gives the precise means and standard deviations for Table 1 .

[187] p: The precise numbers (means and standard deviations) for Figure 3 are given in Table 4 b.

[188] figure: Table 4. Per-Step Latency Overhead (ms) over the Unconstrained Baseline. We report mean and standard deviation over 100 100 trials. Setting STATIC (Ours) Hash Bitmap PPV Approximate PPV Exact CPU Trie (a) Scaling with Constraint Size | 𝒞 | |\mathcal{C}| ( | 𝒱 | = 2048 |\mathcal{V}|=2048 ) | 𝒞 | = 10 5 |\mathcal{C}|=10^{5} 0.023 ± 0.008 0.023\pm 0.008 12.335 ± 0.020 12.335\pm 0.020 0.588 ± 0.008 0.588\pm 0.008 6.375 ± 0.268 6.375\pm 0.268 27.070 ± 0.416 27.070\pm 0.416 | 𝒞 | = 10 6 |\mathcal{C}|=10^{6} 0.030 ± 0.008 0.030\pm 0.008 12.339 ± 0.016 12.339\pm 0.016 0.846 ± 0.008 0.846\pm 0.008 15.368 ± 0.338 15.368\pm 0.338 27.579 ± 0.353 27.579\pm 0.353 | 𝒞 | = 10 7 |\mathcal{C}|=10^{7} 0.034 ± 0.006 0.034\pm 0.006 12.341 ± 0.026 12.341\pm 0.026 1.486 ± 0.020 1.486\pm 0.020 31.765 ± 2.150 31.765\pm 2.150 28.060 ± 0.396 28.060\pm 0.396 | 𝒞 | = 2 ⋅ 10 7 |\mathcal{C}|=2\cdot 10^{7} 0.033 ± 0.008 0.033\pm 0.008 12.343 ± 0.020 12.343\pm 0.020 1.564 ± 0.033 1.564\pm 0.033 34.116 ± 2.118 34.116\pm 2.118 31.336 ± 0.479 31.336\pm 0.479 | 𝒞 | = 10 8 |\mathcal{C}|=10^{8} 0.039 ± 0.010 0.039\pm 0.010 12.331 ± 0.013 12.331\pm 0.013 1.713 ± 0.038 1.713\pm 0.038 38.691 ± 2.469 38.691\pm 2.469 OOM (b) Scaling with Vocabulary Size | 𝒱 | |\mathcal{V}| ( | 𝒞 | = 10 7 |\mathcal{C}|=10^{7} ) | 𝒱 | = 256 |\mathcal{V}|=256 0.040 ± 0.008 0.040\pm 0.008 1.554 ± 0.008 1.554\pm 0.008 1.584 ± 0.035 1.584\pm 0.035 6.004 ± 0.228 6.004\pm 0.228 27.359 ± 0.365 27.359\pm 0.365 | 𝒱 | = 512 |\mathcal{V}|=512 0.041 ± 0.008 0.041\pm 0.008 3.094 ± 0.008 3.094\pm 0.008 1.543 ± 0.035 1.543\pm 0.035 10.586 ± 0.655 10.586\pm 0.655 27.853 ± 0.294 27.853\pm 0.294 | 𝒱 | = 1024 |\mathcal{V}|=1024 0.038 ± 0.008 0.038\pm 0.008 6.180 ± 0.011 6.180\pm 0.011 1.509 ± 0.036 1.509\pm 0.036 18.360 ± 1.313 18.360\pm 1.313 29.239 ± 0.491 29.239\pm 0.491 | 𝒱 | = 2048 |\mathcal{V}|=2048 0.034 ± 0.006 0.034\pm 0.006 12.341 ± 0.026 12.341\pm 0.026 1.486 ± 0.020 1.486\pm 0.020 31.765 ± 2.150 31.765\pm 2.150 31.176 ± 0.446 31.176\pm 0.446 | 𝒱 | = 4096 |\mathcal{V}|=4096 0.034 ± 0.008 0.034\pm 0.008 24.620 ± 0.033 24.620\pm 0.033 1.620 ± 0.025 1.620\pm 0.025 57.066 ± 3.540 57.066\pm 3.540 29.810 ± 0.426 29.810\pm 0.426 | 𝒱 | = 8192 |\mathcal{V}|=8192 0.041 ± 0.008 0.041\pm 0.008 49.191 ± 0.090 49.191\pm 0.090 1.668 ± 0.024 1.668\pm 0.024 107.015 ± 9.269 107.015\pm 9.269 29.383 ± 0.741 29.383\pm 0.741 | 𝒱 | = 16384 |\mathcal{V}|=16384 0.044 ± 0.008 0.044\pm 0.008 98.273 ± 0.025 98.273\pm 0.025 1.824 ± 0.031 1.824\pm 0.031 287.181 ± 4.321 287.181\pm 4.321 30.885 ± 0.276 30.885\pm 0.276 | 𝒱 | = 32768 |\mathcal{V}|=32768 0.041 ± 0.006 0.041\pm 0.006 196.474 ± 0.038 196.474\pm 0.038 2.093 ± 0.029 2.093\pm 0.029 578.738 ± 14.596 578.738\pm 14.596 31.676 ± 0.399 31.676\pm 0.399

[189] h2: Appendix D Hardware Scaling with High Branching Factor

[190] p: To isolate the hardware-level scaling efficiency of the STATIC masking kernel, we design a benchmark that stresses the vectorized burst-read mechanism under extreme sparsity and high-cardinality conditions. Specifically, we evaluate the execution time of the core Vectorized Node Transition Kernel (VNTK), i.e. Algorithm 2 , as the maximum branching factor increases.

[191] p: For each tested max branching factor B ∈ { 2 1 , 2 2 , … , 2 18 } B\in\{2^{1},2^{2},\dots,2^{18}\} , we dynamically set the token vocabulary size such that | 𝒱 | = B |\mathcal{V}|=B . Under this configuration, we synthesize a new constraint set comprising | 𝒞 | = 10 6 |\mathcal{C}|=10^{6} Semantic IDs generated uniformly at random. We then flatten this newly generated prefix tree into a Compressed Sparse Row (CSR) matrix for the VNTK algorithm.

[192] p: During the timed trials, we execute the JIT-compiled masking kernel, which performs a coalesced read of B B contiguous elements from High-Bandwidth Memory (HBM) and applies the validity mask. To ensure robust measurements, we perform synchronous wall-clock timing over multiple iterations, capturing the amortized pure hardware compute time per operation while aggressively clearing the accelerator memory between scales to prevent out-of-memory (OOM) errors. The scaling results are illustrated in Figure 4 . Crucially, the benchmark demonstrates that the STATIC decoding framework exhibits strict asymptotic linear scaling, O ⁡ ( B ) O(B) , with respect to the maximum branch factor B B . We note that STATIC exhibits constant runtime before reaching TPU VMEM bandwidth, at which point the linear regime begins.

[193] figure: Figure 4. Scaling of the STATIC masking kernel with respect to the max branch factor (log-log scale). We plot means and standard deviations (shaded region) over 100 100 trials. For each trial, the token vocabulary size is set to the branch factor, while the number of constraints is fixed at | 𝒞 | = 10 6 |\mathcal{C}|=10^{6} . The STATIC method exhibits asymptotically linear 𝒪 ⁡ ( B ) \mathcal{O}(B) scaling.

[194] h2: Appendix E STATIC Code: JAX Implementation

[195] p: In this section, we give a code snippet to demonstrate an explicit example implementation of Algorithms 1 and 2 using the JAX ( Bradbury et al., 2018 ) and Flax ( Heek et al., 2024 ) frameworks. Note that the code works on both TPU and GPU with almost identical latency overhead.

[196] h2: Instructions for reporting errors

[197] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[198] p: Tip: You can select the relevant text first, to include it in your report.

[199] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[200] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
