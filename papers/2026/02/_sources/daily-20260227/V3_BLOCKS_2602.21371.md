[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Interleaved Head Attention

[3] h6: Abstract

[4] p: Multi-Head Attention (MHA) is the core computational primitive underlying modern Large Language Models (LLMs). However, MHA suffers from a fundamental linear scaling limitation: H H attention heads produce exactly H H independent attention matrices, with no communication between heads during attention computation. This becomes problematic for multi-step reasoning, where correct answers depend on aggregating evidence from multiple parts of the context and composing latent token-to-token relations over a chain of intermediate inferences. To address this, we propose Interleaved Head Attention (IHA), which enables cross-head mixing by constructing P P pseudo-heads per head (typically P = H P=H ), where each pseudo query/key/value is a learned linear combination of all H H original queries, keys and values respectively. Interactions between pseudo-query and pseudo-key heads induce up to P 2 P^{2} attention patterns per head with modest parameter overhead 𝒪 ⁡ ( H 2 ​ P ) \mathcal{O}(H^{2}P) . We provide theory showing improved efficiency in terms of number of parameters on the synthetic Polynomial task (IHA uses Θ ⁡ ( k ​ n 2 ) \Theta(\sqrt{k}n^{2}) parameters vs. Θ ⁡ ( k ​ n 2 ) \Theta(kn^{2}) for MHA) and on the synthetic order-sensitive CPM-3 task (IHA uses ⌈ N max ⌉ \lceil\sqrt{N_{\mathrm{max}}}\rceil heads vs. N max N_{\mathrm{max}} for MHA). On real-world benchmarks, IHA improves Multi-Key retrieval on RULER by 10–20% (4k–16k) and, after fine-tuning for reasoning on OpenThoughts, improves GSM8K by 5.8% and MATH-500 by 2.8% (Majority Vote) over full attention.

[5] h2: 1 Introduction

[6] p: Multi-head attention (MHA) is the core computational primitive underlying modern Large Language Models ( Vaswani et al., 2017 ) . In MHA, each of the H H heads computes an attention matrix independently: each query head attends only to its corresponding key–value projections, and heads do not interact during attention computation. Consequently, MHA exhibits a fundamental linear scaling constraint: H H heads produce exactly H H attention matrices. While this is sufficient in many settings, it can be limiting for multi-step, compositional reasoning, where a token must aggregate evidence from multiple parts of the context and compose token-to-token relations over a chain of intermediate inferences. For example, in question answering, correct predictions often require chaining evidence: for example, to answer “ Where was the author of The Hobbit born? ”, the model must first infer The Hobbit → \rightarrow J.R.R. Tolkien and then infer Tolkien → \rightarrow born in South Africa . This requires composing intermediate reasoning relations rather than relying on a single direct association.

[7] p: To formalize this limitation, we study the Polynomial Filter problem ( Defferrard et al., 2016 ; Chien et al., 2021 ; Lingam et al., 2021 ; Ekbote et al., 2023 ) as a controlled proxy for multi-step reasoning. Concretely, an r r -step dependency means that information reaches a token through r r successive relation applications (e.g., r = 1 r=1 is direct, while r = 2 r=2 composes two relations). We show that an individual MHA head (i.e., a single attention matrix) can represent only one such dependency pattern at a time. Representing k k distinct chain lengths within one layer (i.e., simultaneously modeling direct and longer-range composed relations) requires Θ ⁡ ( k ) \Theta(k) heads (or additional depth), leading to parameter requirements that scale linearly with task complexity. Our theory on Polynomial Filters also generalize to other compositional primitives like binary relations ( Kozachinskiy et al., 2024 ) and Match-3 ( Sanford et al., 2023 ) .

[8] p: In this work, we propose Interleaved Head Attention (IHA), which addresses this bottleneck. Whereas standard MHA computes each head in isolation and therefore scales linearly with the number of distinct step-patterns it can represent, IHA breaks this constraint by enabling cross-head mixing within attention. For each head, IHA constructs P P pseudo-queries, pseudo-keys, and pseudo-values (typically P = H P=H ) as learned linear combinations of the original heads’ query, key, and value projections. Interacting the P P pseudo-queries with the P P pseudo-keys induces up to P 2 P^{2} attention patterns per head, yielding quadratic scaling in P P (and typically in H H when P = H P=H ). Unlike Talking-Heads and Knocking ( Shazeer et al., 2020 ; Zhou and others, 2025 ) , which mix heads at the level of attention logits/weights, IHA performs this mixing before attention while preserving the standard attention operator, making it compatible with efficient kernels such as FlashAttention ( Dao et al., 2022 ) . The extra parameters come only from pseudo-head mixing and scale as 𝒪 ⁡ ( H 2 ​ P ) \mathcal{O}(H^{2}P) , which is modest since H , P ≪ d model H,P\ll d_{\text{model}} , where d model d_{\text{model}} denotes the model dimension. On Polynomial Filters of order k k , we show that MHA needs Θ ⁡ ( k ​ n 2 ) \Theta(kn^{2}) parameters, whereas IHA matches the same expressivity with Θ ⁡ ( k ​ n 2 ) \Theta(\sqrt{k}n^{2}) parameters using 𝒪 ⁡ ( k ) \mathcal{O}(\sqrt{k}) heads.

[9] p: We run extensive experiments on long-context modeling and supervised fine-tuning for reasoning. On the RULER long-context benchmark ( Hsieh et al., 2024 ) , IHA achieves 10–20% relative improvements over full attention on Multi-Key Retrieval across 4k to 16k context lengths. After fine-tuning on OpenThoughts ( Guha et al., 2025 ) for reasoning, IHA outperforms full attention baselines by 5.8% on GSM8K ( Cobbe et al., 2021 ) and 2.8% on MATH-500 ( Hendrycks et al., 2021 ) under majority voting. Our contributions are:

[10] h2: 2 Related Work

[11] p: Recent work has begun to characterize when standard multi-head attention (MHA) is a poor fit for compositional, multi-step reasoning. A recurring theme is that many reasoning primitives require both (i) aggregating evidence spread across many positions and (ii) composing multiple intermediate transformations before producing an answer (e.g., relation/function composition and Match-3 ( Kozachinskiy et al., 2025 ; Sanford et al., 2023 ) , as well as multi-hop QA benchmarks such as bAbI ( Weston et al., 2016 ) ). To study this behavior in a controlled theoretical fashion, we focus on two synthetic proxies: polynomial filters ( Defferrard et al., 2016 ; Chien et al., 2021 ) , which model k k -step aggregation, and CPM-3, which isolates order-sensitive composition and counting. In these settings, we show that IHA realizes the underlying primitives more efficiently than MHA, yielding quadratic improvements in the heads/parameters required by the corresponding constructions. In parallel, prior work extends attention along two main directions: adding richer token interactions or improving computational efficiency. Some methods go beyond standard pairwise query–key attention by modeling interactions among three or more tokens at once (e.g., simplicial/trilinear attention ( Clift et al., 2019 ; Roy and others, 2025 ) , Strassen-style constructions ( Kozachinskiy et al., 2025 ) and other multi-token mechanisms ( Golovneva et al., 2025 ) ) while increasing the number of parameters, while MQA/GQA ( Shazeer, 2019 ; Ainslie et al., 2023 ) reduce KV cost. Other lines of work mix information across heads (Talking-Heads, Knocking-Heads ( Shazeer et al., 2020 ; Zhou and others, 2025 ) ) or modify attention maps (e.g., Differential Attention ( Ye et al., 2024 ) ). IHA is complementary: it enables cross-head interaction within attention by mixing query, key and values into pseudo-heads, inducing quadratic interaction patterns while preserving the standard attention operator (and thus remaining compatible with FlashAttention ( Dao et al., 2022 ) ). An extended related works section appears in App. A .

[12] h2: 3 Background

[13] h4: Notation.

[14] p: We denote matrices with bold uppercase letters (e.g., 𝑿 , 𝑾 \bm{X},\bm{W} ) and vectors with bold lowercase (e.g., 𝒙 \bm{x} ). For an input sequence of N N tokens with embedding dimension D D , the input matrix is 𝑿 ∈ ℝ N × D \bm{X}\in\mathbb{R}^{N\times D} . We use h h to index attention heads, d = D / H d=D/H for per-head dimension where H H is the total number of heads, and softmax ⁡ ( ⋅ ) \mathrm{softmax}(\cdot) for row-wise softmax. We use [ 𝑨 , 𝑩 ] [\bm{A},\bm{B}] for column-wise (horizontal) concatenation and [ 𝑨 ; 𝑩 ] [\bm{A};\bm{B}] for row-wise (vertical) stacking. In Algorithm 4 , we use reshape ( 𝑻 , [ d 1 , … , d k ] ) (\bm{T},[d_{1},\ldots,d_{k}]) to reshape tensor 𝑻 \bm{T} to dimensions d 1 × ⋯ × d k d_{1}\times\cdots\times d_{k} , einsum for Einstein summation following NumPy conventions (e.g., ‘mhp,nmd → \to hpnd’ contracts index m m and permutes the result), and merge_pseudo to interleave the pseudo-head dimension P P into the sequence dimension, transforming shape ( H , P , N , d ) → ( H , N ​ P , d ) (H,P,N,d)\to(H,NP,d) . Throughout, 𝟙 ​ [ ⋅ ] \mathbbm{1}[\cdot] denotes the indicator function; e.g., 𝟙 [ x = y ] = 1 \mathbbm{1}[x=y]=1 if x = y x=y and 0 0 otherwise. We also write this equivalently as 𝟏 ( x = y ) \bm{1}_{(x=y)} .

[15] h3: 3.1 Multi-head Attention and Polynomial Filters

[16] h4: MHA.

[17] p: We use the standard scaled dot-product causal self-attention mechanism ( Vaswani et al., 2017 ) , with the causal mask applied implicitly.

[18] h4: Polynomial filters.

[19] p: Polynomial graph filters are a core primitive in graph signal processing.

[20] p: The above defines a node representation which aggregates information from nodes up to k k hops away. This is a controlled proxy for multi-step reasoning in language tasks such as Weston et al. (2016) : consider the story (i) “Mary picked up the football.” (ii) “Mary went to the kitchen.” and the question “Where is the football?” A model must connect football to Mary (fact i ) and then Mary to kitchen (fact ii ), i.e., a two-step composition. If we build a fact graph with one node per sentence and connect two nodes when they share an entity (here, facts i and ii are connected via Mary ), then one-hop aggregation 𝑨 ​ 𝑿 \bm{A}\bm{X} retrieves the directly linked fact, while two-hop aggregation 𝑨 2 ​ 𝑿 \bm{A}^{2}\bm{X} captures precisely the required two-step chain. In a language model, this graph is implicitly induced by the particular input (and thus varies across examples); however, as a controlled proxy for analyzing multi-step information propagation, we treat 𝑨 \bm{A} as fixed for a given instance and study how well attention can realize the corresponding k k -hop operators. A natural question is therefore: how many attention heads does MHA need to represent (or approximate) these k k -hop aggregations, and to produce the full filter bank [ 𝑿 , 𝑨 ​ 𝑿 , … , 𝑨 k − 1 ​ 𝑿 ] \big[\bm{X},\bm{A}\bm{X},\ldots,\bm{A}^{k-1}\bm{X}\big] in parallel? We aim to answer this question via Subsec. 3.1 .

[21] h4: Proof sketch.

[22] p: Why does MHA need k k heads? We augment 𝑿 \bm{X} with positional encodings 𝑿 ^ = [ 𝑿 , 𝑰 N ] \widehat{\bm{X}}=[\bm{X},\bm{I}_{N}] . In linear (no-softmax) attention, head h h outputs

[23] table: 𝑶 h = 𝑿 ^ ​ 𝑾 Q ( h ) ​ 𝑾 K ( h ) ⊤ ​ 𝑿 ^ ⊤ ​ 𝑿 ^ ​ 𝑾 V ( h ) ∈ ℝ N × d . \displaystyle\bm{O}_{h}=\widehat{\bm{X}}\bm{W}_{Q}^{(h)}{\bm{W}_{K}^{(h)}}^{\top}\widehat{\bm{X}}^{\top}\widehat{\bm{X}}\bm{W}_{V}^{(h)}\in\mathbb{R}^{N\times d}.

[24] p: To realize 𝑨 i ​ 𝑿 \bm{A}^{i}\bm{X} , choose

[25] table: 𝑾 Q ( h ) \displaystyle\bm{W}_{Q}^{(h)} = [ 𝟎 d × N 𝑨 i ] , \displaystyle=\begin{bmatrix}\bm{0}_{d\times N}\\ \bm{A}^{i}\end{bmatrix}, 𝑾 K ( h ) \displaystyle\bm{W}_{K}^{(h)} = [ 𝟎 d × N 𝑰 N ] , \displaystyle=\begin{bmatrix}\bm{0}_{d\times N}\\ \bm{I}_{N}\end{bmatrix}, 𝑾 V ( h ) \displaystyle\bm{W}_{V}^{(h)} = [ 𝑰 d 𝟎 N × d ] , \displaystyle=\begin{bmatrix}\bm{I}_{d}\\ \bm{0}_{N\times d}\end{bmatrix},

[26] p: which gives 𝑿 ^ ​ 𝑾 Q ( h ) ​ 𝑾 K ( h ) ⊤ ​ 𝑿 ^ ⊤ = 𝑨 i \widehat{\bm{X}}\bm{W}_{Q}^{(h)}{\bm{W}_{K}^{(h)}}^{\top}\widehat{\bm{X}}^{\top}=\bm{A}^{i} and 𝑿 ^ ​ 𝑾 V ( h ) = 𝑿 \widehat{\bm{X}}\bm{W}_{V}^{(h)}=\bm{X} , hence 𝑶 h = 𝑨 i ​ 𝑿 \bm{O}_{h}=\bm{A}^{i}\bm{X} . Since each head yields a single power 𝑨 i \bm{A}^{i} , producing 𝑨 0 , … , 𝑨 k − 1 \bm{A}^{0},\ldots,\bm{A}^{k-1} requires at least k k heads. See Subsec. B.2 for more details. Note that the assumption that d ≪ N d\ll N and k ≪ N k\ll N is consistent with prior works on polynomial graph filters such as Defferrard et al. (2016) ; Chien et al. (2021) ; Lingam et al. (2021) ; Ekbote et al. (2023) .

[27] h4: Intuition.

[28] p: The fundamental bottleneck in MHA is head isolation: head h h uses only its own query/key/value projections, yielding at most one attention pattern per head. Thus, if the target requires k k distinct relational patterns (e.g., k k polynomial terms), then a single MHA layer typically needs Ω ⁡ ( k ) \Omega(k) heads (or additional depth). IHA relaxes this constraint by constructing, for each head, P P pseudo-queries/ keys/ values as learned linear combinations of the original heads’ query/ key/ value projections, so each head can realize up to P 2 P^{2} attention patterns. In particular, setting P = ⌈ k ⌉ P=\lceil\sqrt{k}\rceil allows k k patterns to be realized within a single head, so IHA can represent k k patterns with only H = 𝒪 ⁡ ( k ) H=\mathcal{O}(\sqrt{k}) heads (up to constants/modeling constraints). We formalize this in Sec. 4 .

[29] h2: 4 Interleaved-Head Attention (IHA)

[30] figure: Figure 1 : Overview of Interleaved Head Attention (IHA). First, the model generates P P pseudo-tokens for each of the H H original heads via a learned linear transformation ( × α 𝐐 \times\mathbf{\mathcal{\alpha}_{Q}} ) operating on the heads axis (green). These tokens are then interleaved to create an expanded sequence of length P ⋅ N P\cdot N . Finally, standard causal self-attention is computed on this expanded sequence, utilizing a sliding window (e.g., N / 2 ​ P N/2P ) to manage computational complexity while enabling cross-head interaction. Different linear transforms are used in query, key and values.

[31] p: IHA overcomes the one-to-one coupling of standard multi-head attention (MHA) by constructing, for each head, P P pseudo-queries, pseudo-keys, and pseudo-values as learned linear combinations of the H H queries, keys and values respectively (typically P = H P=H ). This enlarges the set of query/key/value projections and allows attention to mix information across heads, rather than restricting each query head to its paired key–value head. Within each head, the P P pseudo-queries attending to the P P pseudo-keys can induce up to P 2 P^{2} distinct attention patterns, and this mechanism is applied independently across heads. The added expressivity incurs only modest overhead: pseudo-mixing weights scale as 𝒪 ⁡ ( H 2 ​ P ) \mathcal{O}(H^{2}P) , which is small relative to the overall parameter budget since H H (and thus P P ) is typically much smaller than the model dimension. The full IHA algorithm is given in Sec. 4 and the architecture figure can be found in Fig. 1 .

[32] p: In Sec. 4 , Step 2 constructs, for each head h h and token index n ∈ [ N ] n\in[N] , P P pseudo-head tokens by taking learned linear combinations of the H H original heads’ query, key and value projections. Step 3 interleaves them by replacing each original token with P P consecutive virtual tokens, so the sequence becomes ( 1 , 1 ) , ( 1 , 2 ) , … , ( 1 , P ) , ( 2 , 1 ) , … , ( N , P ) (1,1),(1,2),\ldots,(1,P),(2,1),\ldots,(N,P) where ( n , p ) (n,p) denotes the p p -th pseudo-head token at position n n . Step 4 then runs standard scaled dot-product attention once on this length- N ​ P NP sequence. This lets different pseudo-head tokens attend differently (including to different pseudo-head tokens at the same original position), yielding up to P 2 P^{2} attention patterns per head (and H ​ P 2 HP^{2} overall) without custom kernels. Interleaving is useful with RoPE because RoPE depends on the position index: giving each ( n , p ) (n,p) its own virtual position assigns each pseudo-head token a distinct RoPE phase, and variable-length inference is handled by generating RoPE for length N ​ P NP . The procedure is also compatible with FlashAttention ( Dao et al., 2022 ) , since Step 4 is standard attention. For the theoretical analysis, Sec. 4 gives an equivalent, more algebraic formulation of IHA that omits interleaving and the output projection. Since our proofs do not use positional encodings (e.g., RoPE), interleaving is unnecessary, and dropping the projection cleanly isolates the core pseudo-head mixing and attention computation.

[33] p: In the following sections, we (i) establish a strict expressivity separation by showing that the class of functions representable by MHA is contained in (and generally a strict subset of) those representable by IHA, (ii) analyze IHA on two synthetic benchmarks (the polynomial filter and CPM3 tasks; defined later), and (iii) experimentally show that IHA outperforms other attention variants.

[34] h3: 4.1 IHA Strictly Generalizes MHA

[35] p: We formalize the sense in which IHA strictly generalizes standard multi-head attention (MHA) while making the parameter overhead explicit. Fix a sequence length N N and number of heads H H . Let ℳ \mathcal{M} denote the set of all single-layer H H -head MHA modules with query, key, value matrices as defined in Subsec. 3.1 , requiring Q Q parameters in total. Let 𝒫 P \mathcal{P}_{P} denote the corresponding set of H H -head IHA modules as in Sec. 4 (and Sec. 4 ) with P P pseudo-heads per head, whose query, key, and value weight matrices have the same dimensions as those in MHA (hence also contributing Q Q parameters), but which additionally introduce mixing tensors α Q , α K , α V ∈ ℝ H × H × P \alpha^{Q},\alpha^{K},\alpha^{V}\in\mathbb{R}^{H\times H\times P} and a collapse map 𝑹 ∈ ℝ H × H ​ P \bm{R}\in\mathbb{R}^{H\times HP} .

[36] p: Proof sketch. Inclusion. Fix any MHA instance with weights { 𝑾 Q ( m ) , 𝑾 K ( m ) , 𝑾 V ( m ) } m = 1 H \{\bm{W}_{Q}^{(m)},\bm{W}_{K}^{(m)},\bm{W}_{V}^{(m)}\}_{m=1}^{H} . We construct an IHA instance (with any chosen P ≥ 1 P\geq 1 ) that computes the same function by selecting parameters that ignore all but one pseudo-channel. Specifically, for all m , i ∈ [ H ] m,i\in[H] and all j ∈ [ P ] j\in[P] , set α m , i , j Q = 𝟏 ( m = i ) , α m , i , j K = 𝟏 ( m = i ) , α m , i , j V = 𝟏 ( m = i ) \alpha^{Q}_{m,i,j}=\bm{1}_{(m=i)},\ \alpha^{K}_{m,i,j}=\bm{1}_{(m=i)},\ \alpha^{V}_{m,i,j}=\bm{1}_{(m=i)} and choose 𝑹 \bm{R} to select only the ( i , 1 ) (i,1) pseudo-block:

[37] table: 𝑹 i , ( i ′ − 1 ) ​ P + j = { 1 if ​ i ′ = i ​ and ​ j = 1 , 0 otherwise. \displaystyle\bm{R}_{\,i,\,(i^{\prime}-1)P+j}=\begin{cases}1&\text{if }i^{\prime}=i\text{ and }j=1,\\ 0&\text{otherwise.}\end{cases}

[38] p: Then 𝑸 ~ i , j = 𝑿 ​ 𝑾 Q ( i ) \widetilde{\bm{Q}}_{i,j}=\bm{X}\bm{W}_{Q}^{(i)} , 𝑲 ~ i , j = 𝑿 ​ 𝑾 K ( i ) \widetilde{\bm{K}}_{i,j}=\bm{X}\bm{W}_{K}^{(i)} , and 𝑽 ~ i , j = 𝑿 ​ 𝑾 V ( i ) \widetilde{\bm{V}}_{i,j}=\bm{X}\bm{W}_{V}^{(i)} for all j j , so the stacked attention produces copies of the original MHA head outputs and the collapse map returns exactly the MHA outputs. Hence ℳ ⊆ 𝒫 P \mathcal{M}\subseteq\mathcal{P}_{P} .

[39] p: Strictness. Consider the repeated-token subspace 𝒮 = { 𝑿 = 𝟏 N ​ 𝒙 ⊤ : 𝒙 ∈ ℝ d } , N ≥ 2 \mathcal{S}=\{\bm{X}=\bm{1}_{N}\bm{x}^{\top}:\bm{x}\in\mathbb{R}^{d}\},\ N\geq 2 . On 𝒮 \mathcal{S} , every MHA head has identical queries/keys/values at all positions, so each score matrix has identical rows and the row-wise softmax is uniform; consequently each head output reduces to 𝟏 N ​ 𝒙 ⊤ ​ 𝑾 V ( m ) \bm{1}_{N}\bm{x}^{\top}\bm{W}_{V}^{(m)} , which is linear in 𝒙 \bm{x} . Therefore every H H -head MHA module is linear on 𝒮 \mathcal{S} . In contrast, IHA with P = 2 P=2 can be parameterized (using only the additional 4 ​ H 2 ​ P 4H^{2}P mixing/collapse parameters on top of the same projections) so that the stacked attention produces a nonlinear function of 𝒙 \bm{x} on 𝒮 \mathcal{S} : for example, by creating two pseudo-query/key variants with opposite signs and choosing the pseudo-values/collapse so that the output involves a difference of softmax-normalized terms depending on the cosine score ⟨ 𝒙 ⊤ ​ 𝑾 Q , 𝒙 ⊤ ​ 𝑾 K ⟩ \langle\bm{x}^{\top}\bm{W}_{Q},\bm{x}^{\top}\bm{W}_{K}\rangle , yielding a nonlinearity (e.g., a tanh \tanh -like dependence). Since no MHA can be nonlinear on 𝒮 \mathcal{S} , this IHA mapping cannot be represented by any MHA, proving ℳ ⊊ 𝒫 P \mathcal{M}\subsetneq\mathcal{P}_{P} for all P ≥ 2 P\geq 2 . For a detailed proof please refer to Subsec. B.1

[40] h3: 4.2 Representing Polynomial Filters using IHA

[41] p: As established in Subsec. 3.1 , polynomial graph filters provide a clean proxy for multi-hop information propagation (and thus multi-step reasoning): the i i -th term 𝑨 i ​ 𝑿 \bm{A}^{i}\bm{X} aggregates information from i i -hop neighborhoods. Computing 𝑿 , 𝑨 ​ 𝑿 , … , 𝑨 k − 1 ​ 𝑿 \bm{X},\bm{A}\bm{X},\ldots,\bm{A}^{k-1}\bm{X} in parallel captures k k -step composition in a controlled setting. In Subsec. 4.2 , we show how IHA represents this polynomial filter.

[42] h4: Proof sketch.

[43] p: We consider representing the polynomial filter bank, 𝑿 ~ = [ 𝑿 , 𝑨 ​ 𝑿 , … , 𝑨 k − 1 ​ 𝑿 ] \widetilde{\bm{X}}\;=\;\big[\bm{X},\;\bm{A}\bm{X},\;\ldots,\;\bm{A}^{k-1}\bm{X}\big] using a single linear-attention layer (i.e., without softmax). Since 𝑿 ∈ ℝ N × d \bm{X}\in\mathbb{R}^{N\times d} is low-rank when d < N d<N , we augment the input with positional encodings 𝑿 ^ = [ 𝑿 , 𝑰 ] \widehat{\bm{X}}=[\bm{X},\bm{I}] .

[44] p: Why MHA needs k k heads. As established in Section 3.1 , in linear MHA, each head produces exactly one attention operator (matrix) 𝑺 h ∈ ℝ N × N \bm{S}_{h}\in\mathbb{R}^{N\times N} . To represent all k k distinct powers 𝑨 0 , … , 𝑨 k − 1 \bm{A}^{0},\ldots,\bm{A}^{k-1} in parallel, one therefore needs k k independently parameterized heads. The parameter-minimal exact MHA construction thus uses k k heads.

[45] p: Why IHA only needs ⌈ k ⌉ \lceil\sqrt{k}\rceil heads. Let H = ⌈ k ⌉ H=\lceil\sqrt{k}\rceil (and in the construction we set the number of pseudo-heads to P = H P=H ). IHA exploits the factorization

[46] table: 𝑨 i = 𝑨 ( h − 1 ) ​ H + ( j − 1 ) , h , j ∈ { 1 , … , H } , \displaystyle\bm{A}^{i}\;=\;\bm{A}^{(h-1)H+(j-1)},\qquad h,j\in\{1,\ldots,H\},

[47] p: so that H 2 ≥ k H^{2}\geq k distinct powers can be generated via pairwise query–key interactions. Instead of assigning one head per power, IHA assigns heads to blocks of powers. Concretely, we choose H H query and key matrices (where ∀ h , j ∈ { 1 , ⋯ , H } \forall\ h,j\ \in\ \{1,\cdots,H\}

[48] table: 𝑾 Q , IHA ( h ) = [ 𝟎 d × N 𝑨 ( h − 1 ) ​ H ] 𝑾 K , IHA ( j ) = [ 𝟎 d × N ( 𝑨 j − 1 ) ⊤ ] , \displaystyle\bm{W}_{Q,\texttt{IHA}}^{(h)}\;=\;\begin{bmatrix}\bm{0}_{d\times N}\\ \bm{A}^{(h-1)H}\end{bmatrix}\qquad\bm{W}_{K,\texttt{IHA}}^{(j)}\;=\;\begin{bmatrix}\bm{0}_{d\times N}\\ \left({\bm{A}^{j-1}}\right)^{\top}\end{bmatrix},

[49] p: When query head h h interacts with key head j j , the resulting (linear) attention matrix is

[50] table: 𝑺 h , j \displaystyle\bm{S}_{h,j} = 𝑿 ^ ​ 𝑾 Q , IHA ( h ) ​ ( 𝑾 K , IHA ( j ) ) ⊤ ​ 𝑿 ^ ⊤ = 𝑨 ( h − 1 ) ​ H + ( j − 1 ) . \displaystyle=\widehat{\bm{X}}\bm{W}_{Q,\texttt{IHA}}^{(h)}\big(\bm{W}_{K,\texttt{IHA}}^{(j)}\big)^{\!\top}\widehat{\bm{X}}^{\!\top}=\bm{A}^{(h-1)H+(j-1)}.

[51] p: Thus, H H query matrices and H H key matrices generate H 2 ≥ k H^{2}\geq k distinct polynomial powers through pairwise interaction. Pseudo-head mixing ensures that, within each head h h , a single query attends to all H H key/value branches, producing the entire block

[52] table: [ 𝑨 ( h − 1 ) ​ H ​ 𝑿 , 𝑨 ( h − 1 ) ​ H + 1 ​ 𝑿 , … , 𝑨 ( h − 1 ) ​ H + ( H − 1 ) ​ 𝑿 ] \displaystyle\big[\bm{A}^{(h-1)H}\bm{X},\;\bm{A}^{(h-1)H+1}\bm{X},\;\ldots,\;\bm{A}^{(h-1)H+(H-1)}\bm{X}\big]

[53] p: in one shot. Value matrices are chosen to route each 𝑨 ( h − 1 ) ​ H + ( j − 1 ) ​ 𝑿 \bm{A}^{(h-1)H+(j-1)}\bm{X} into a distinct d d -dimensional output block, and concatenating the H H heads recovers [ 𝑿 , 𝑨 ​ 𝑿 , … , 𝑨 H 2 − 1 ​ 𝑿 ] \big[\bm{X},\;\bm{A}\bm{X},\;\ldots,\;\bm{A}^{H^{2}-1}\bm{X}\big] with any extra ( H 2 − k ) (H^{2}-k) blocks treated as padding. Consequently, IHA represents the same polynomial filter bank using only O ⁡ ( k ) O(\sqrt{k}) heads, reducing the dominant parameter cost from Θ ⁡ ( k ​ N 2 ) \Theta(kN^{2}) (MHA) to Θ ⁡ ( ⌈ k ⌉ ​ N 2 ) \Theta(\lceil\sqrt{k}\rceil N^{2}) , up to lower-order routing terms (including the 4 ​ H 3 4H^{3} pseudo-mixing/collapse parameters). For more details and the full proof, see Subsec. B.2 .

[54] h3: 4.3 Representing CPM-3 using IHA

[55] p: Polynomial filters provide a controlled proxy for multi-step retrieval: they aggregate information from k k -hop neighborhoods, but the result is essentially a bag of k k -hop evidence. To probe a complementary regime, we introduce Count Permutation Match-3 (CPM-3), which isolates order-sensitive composition and counting. For each position i i , the model ranges over ordered pairs of other positions ( j 1 , j 2 ) (j_{1},j_{2}) , checks whether the triple ( x i , x j 1 , x j 2 ) (x_{i},x_{j_{1}},x_{j_{2}}) satisfies a simple modular predicate, and outputs how many ordered pairs satisfy it. CPM-3 is an arithmetic analogue of multi-fact QA Weston et al. (2016) : instead of only retrieving relevant facts, the model must combine two facts in the correct order and then count how many such combinations exist. For example, in a story with facts of the form “ u u is in v v ,” a query about u = i u=i asks how many ordered pairs of facts ( j 1 , j 2 ) (j_{1},j_{2}) form a valid two-step chain, the first fact says i i is in some z z , and the second fact says that same z z is in some y y . Each ordered pair that correctly links through a shared intermediate z z is a valid supporting pair for the query, and the answer is the count of all such pairs. We formalize this intuition by encoding tokens as scalars and replacing this chain test with the modular relation defined below.

[56] h4: Count Permutation Match-3 (CPM-3).

[57] p: We introduce the CPM-3 task. The input is a length- N N sequence of natural numbers ( x 1 , … , x N ) (x_{1},\ldots,x_{N}) , with N ≤ N max N\leq N_{\mathrm{max}} . For each position i i , the desired output is

[58] table: CPM i ​ ( 3 ) = | { ( j 1 , j 2 ) ∈ [ N ] 2 : ϕ ⁡ ( x i , x j 1 , x j 2 ) = 0 } | , \displaystyle\mathrm{CPM}_{i}(3)\;=\;\bigl|\{(j_{1},j_{2})\in[N]^{2}:\ \phi(x_{i},x_{j_{1}},x_{j_{2}})=0\}\bigr|,

[59] p: where the predicate is the (order-sensitive) modular expression ϕ ⁡ ( x i , x j 1 , x j 2 ) := x i + G ​ x j 1 + x j 2 ​ mod ​ M , \phi(x_{i},x_{j_{1}},x_{j_{2}})\;:=\;x_{i}+Gx_{j_{1}}+x_{j_{2}}\ \mathrm{mod}\ M, with modulus M ∈ ℕ M\in\mathbb{N} and coefficient G > 2 ​ M G>2M . The condition G > 2 ​ M G>2M ensures the predicate is not permutation invariant: typically ϕ ⁡ ( x i , x j 1 , x j 2 ) ≠ ϕ ⁡ ( x i , x j 2 , x j 1 ) \phi(x_{i},x_{j_{1}},x_{j_{2}})\neq\phi(x_{i},x_{j_{2}},x_{j_{1}}) when x j 1 ≠ x j 2 x_{j_{1}}\neq x_{j_{2}} . We next ask how efficiently different attention mechanisms can realize CPM-3 in a single layer; in particular, we show that IHA admits a construction with ⌈ N max ⌉ \lceil\sqrt{N_{\mathrm{max}}}\rceil heads, whereas known MHA constructions require N max N_{\mathrm{max}} heads (in Subsec. 4.3 ).

[60] h4: Proof sketch.

[61] p: We sketch why CPM-3 can be implemented with ⌈ N max ⌉ \lceil\sqrt{N_{\mathrm{max}}}\rceil IHA heads but (in known constructions) requires N max N_{\mathrm{max}} MHA heads. The task is to output, for each position i i , the count of ordered pairs ( j 1 , j 2 ) (j_{1},j_{2}) such that

[62] table: x i + G ​ x j 1 + x j 2 ≡ 0 ( mod ​ M ) , \displaystyle x_{i}+Gx_{j_{1}}+x_{j_{2}}\equiv 0\quad(\mathrm{mod}\ M),

[63] p: with G > 2 ​ M G>2M ensuring order sensitivity. As in the polynomial-filter construction, we use positional encodings to make positions addressable:

[64] table: 𝑿 ^ = [ 𝑿 , 𝑰 ] ∈ ℝ N max × ( N max + 1 ) , 𝑿 ∈ ℝ N max × 1 . \displaystyle\widehat{\bm{X}}=[\bm{X},\bm{I}]\in\mathbb{R}^{N_{\mathrm{max}}\times(N_{\mathrm{max}}+1)},\qquad\bm{X}\in\mathbb{R}^{N_{\mathrm{max}}\times 1}.

[65] p: Note that the CPM-3 output at position i i depends on all ordered pairs ( j 1 , j 2 ) (j_{1},j_{2}) , so a convenient one-layer strategy is to first use attention to build, at every i i , a local “workspace” that contains all token values { x j } j = 1 N max \{x_{j}\}_{j=1}^{N_{\mathrm{max}}} in a fixed, known order. A downstream MLP can then (i) select any ordered pair of coordinates ( j 1 , j 2 ) (j_{1},j_{2}) , (ii) form x i + G ​ x j 1 + x j 2 x_{i}+Gx_{j_{1}}+x_{j_{2}} , (iii) test the modulo constraint, and (iv) sum indicators. We now sketch why MHA needs N max N_{\mathrm{max}} heads to build this workspace, while IHA needs only ⌈ N max ⌉ \lceil\sqrt{N_{\mathrm{max}}}\rceil .

[66] p: Why MHA needs N max N_{\mathrm{max}} heads. With positional encodings 𝑿 ^ = [ 𝑿 , 𝑰 ] \hat{\bm{X}}=[\bm{X},\bm{I}] and hard attention (softmax temperature 0 0 ), each MHA head can implement one cyclic shift of the sequence. Let 𝑷 ∈ ℝ N max × N max \bm{P}\in\mathbb{R}^{N_{\mathrm{max}}\times N_{\mathrm{max}}} be the cyclic permutation matrix. For h ∈ { 1 , … , N max } h\in\{1,\ldots,N_{\mathrm{max}}\} set 𝑾 V , MHA ( h ) = [ 1 𝟎 N max × 1 ⊤ ] ⊤ \bm{W}_{V,\texttt{MHA}}^{(h)}=\begin{bmatrix}1&\bm{0}_{N_{\mathrm{max}}\times 1}^{\top}\end{bmatrix}^{\top} and,

[67] table: 𝑾 Q , MHA ( h ) \displaystyle\bm{W}_{Q,\texttt{MHA}}^{(h)} = [ 𝟎 1 × N max 𝑷 h − 1 ] , 𝑾 K , MHA ( h ) = [ 𝟎 1 × N max 𝑰 N max × N max ] \displaystyle=\begin{bmatrix}\bm{0}_{1\times N_{\mathrm{max}}}\\ \bm{P}^{h-1}\end{bmatrix},\quad\bm{W}_{K,\texttt{MHA}}^{(h)}=\begin{bmatrix}\bm{0}_{1\times N_{\mathrm{max}}}\\ \bm{I}_{N_{\mathrm{max}}\times N_{\mathrm{max}}}\end{bmatrix}

[68] p: and so the head produces 𝑺 h = 𝑷 h − 1 \bm{S}_{h}=\bm{P}^{h-1} and outputs 𝑷 h − 1 ​ 𝑿 \bm{P}^{h-1}\bm{X} . Concatenating all heads yields [ 𝑿 , 𝑷 ​ 𝑿 , … , 𝑷 N max − 1 ​ 𝑿 ] \big[\bm{X},\bm{P}\bm{X},\ldots,\bm{P}^{N_{\mathrm{max}}-1}\bm{X}\big] , which places all N max N_{\mathrm{max}} symbols into each position’s workspace. Since each head contributes only one shift 𝑷 t \bm{P}^{t} , producing all N max N_{\mathrm{max}} shifts in one layer requires N max N_{\mathrm{max}} heads, giving attention-parameter scaling Ω ⁡ ( N max 3 ) \Omega(N_{\mathrm{max}}^{3}) .

[69] p: Why IHA only needs ⌈ N max ⌉ \lceil\sqrt{N_{\mathrm{max}}}\rceil heads. Let H = ⌈ N max ⌉ H=\lceil\sqrt{N_{\mathrm{max}}}\rceil and set P = H P=H . IHA factors each shift index t ∈ { 0 , … , N max − 1 } t\in\{0,\ldots,N_{\mathrm{max}}-1\} as

[70] table: t = ( h − 1 ) ​ H + ( j − 1 ) , h , j ∈ { 1 , … , H } , \displaystyle t=(h-1)H+(j-1),\qquad h,j\in\{1,\ldots,H\},

[71] p: so 𝑷 t = 𝑷 ( h − 1 ) ​ H ​ 𝑷 j − 1 \bm{P}^{t}=\bm{P}^{(h-1)H}\bm{P}^{j-1} . Define query and key matrices by

[72] table: 𝑾 Q , IHA ( h ) = [ 𝟎 1 × N max 𝑷 ( h − 1 ) ​ H ] , 𝑾 K , IHA ( j ) = [ 𝟎 1 × N max ( 𝑷 j − 1 ) ⊤ ] , \displaystyle\bm{W}_{Q,\texttt{IHA}}^{(h)}=\begin{bmatrix}\bm{0}_{1\times N_{\mathrm{max}}}\\ \bm{P}^{(h-1)H}\end{bmatrix},\qquad\bm{W}_{K,\texttt{IHA}}^{(j)}=\begin{bmatrix}\bm{0}_{1\times N_{\mathrm{max}}}\\ \big(\bm{P}^{j-1}\big)^{\top}\end{bmatrix},

[73] p: so the ( h , j ) (h,j) interaction realizes 𝑺 h , j = 𝑷 ( h − 1 ) ​ H + ( j − 1 ) \bm{S}_{h,j}=\bm{P}^{(h-1)H+(j-1)} . The crucial difference from MHA is that pseudo-head mixing lets a single query head h h attend to all j ∈ { 1 , … , H } j\in\{1,\ldots,H\} key/value heads, producing in one head the block

[74] table: [ 𝑷 ( h − 1 ) ​ H ​ 𝑿 , 𝑷 ( h − 1 ) ​ H + 1 ​ 𝑿 , … , 𝑷 ( h − 1 ) ​ H + ( H − 1 ) ​ 𝑿 ] , \displaystyle\big[\bm{P}^{(h-1)H}\bm{X},\;\bm{P}^{(h-1)H+1}\bm{X},\;\ldots,\;\bm{P}^{(h-1)H+(H-1)}\bm{X}\big],

[75] p: with value projections routing each shift into a distinct coordinate block. Concatenating over h ∈ { 1 , … , H } h\in\{1,\ldots,H\} yields all { 𝑷 t ​ 𝑿 } t = 0 N max − 1 \{\bm{P}^{t}\bm{X}\}_{t=0}^{N_{\mathrm{max}}-1} at each position. i.e., the same workspace as above, but using only H = ⌈ N max ⌉ H=\lceil\sqrt{N_{\mathrm{max}}}\rceil heads. The downstream MLP is then identical to that of the MHA construction. The key difference is that IHA can realize many distinct attention patterns per head: with P P pseudo-queries and P P pseudo-keys per head, each head can implement up to P 2 P^{2} different attention maps, and across H H heads this gives up to H ​ P 2 HP^{2} patterns. Taking P = H = ⌈ N max ⌉ P=H=\lceil\sqrt{N_{\mathrm{max}}}\rceil provides enough distinct patterns to cover the N max N_{\mathrm{max}} required shifts while reducing the head count from N max N_{\mathrm{max}} to ⌈ N max ⌉ \lceil\sqrt{N_{\mathrm{max}}}\rceil . Consequently, the best-known one-layer MHA construction incurs Θ ⁡ ( N max 3 ) \Theta(N_{\mathrm{max}}^{3}) attention cost, whereas the IHA construction achieves Θ ⁡ ( N max 2 ​ N max ) \Theta(N_{\mathrm{max}}^{2}\sqrt{N_{\mathrm{max}}}) (up to the O ⁡ ( H 3 ) O(H^{3}) pseudo-mixing/collapse overhead). For full details, see Subsec. B.3 .

[76] h2: 5 Experiments

[77] p: We evaluate Interleaved Head Attention (IHA) in large-scale language model training to answer two questions: (i) does IHA improve long-context retrieval and length generalization when adapting models beyond their pretraining window, and (ii) does IHA improve reasoning on math and code benchmarks before and after supervised fine-tuning? To isolate architectural effects, we keep the backbone, optimizer, data, and training budget fixed across variants and compare against strong attention baselines. Building on prior sections showing that IHA is strictly more expressive than standard MHA and yields separations on controlled reasoning proxies, we test whether these advantages translate into practical gains during pretraining, long-context adaptation, and downstream evaluation. We also report additional experiments on synthetic reasoning datasets in App. D .

[78] h3: 5.1 Experimental Setup

[79] h4: Model architecture.

[80] p: All experiments use a 2.4B-parameter decoder-only Transformer with hidden size 2560, 26 layers, and H = 20 H=20 attention heads (head dimension 128). We use a 4 × 4\times FFN expansion (FFN size 10,240), vocabulary size 128,256 (Llama 3 tokenizer; ( Dubey et al., 2024 ) ), and RoPE positional encoding ( Su et al., 2021 ) with θ = 500,000 \theta=500{,}000 . Pretraining context length is 8,192 tokens.

[81] h4: Training.

[82] p: All models are trained for 240,000 steps (240B tokens) with identical hyperparameters: peak learning rate 8 × 10 − 4 8\times 10^{-4} with 1,000-step warmup and cosine decay ( Loshchilov and Hutter, 2017 ) to 8 × 10 − 6 8\times 10^{-6} , AdamW ( Loshchilov and Hutter, 2019 ) ( β 1 = 0.9 \beta_{1}{=}0.9 , β 2 = 0.95 \beta_{2}{=}0.95 , weight decay 0.1), gradient clipping 1.0, and BF16 mixed precision ( Micikevicius et al., 2018 ) . Training uses FSDP ( Zhao et al., 2023 ) over 128 H200 GPUs.

[83] h4: Baselines.

[84] p: We compare five attention mechanisms. (1) Global Attention ( Vaswani et al., 2017 ) is standard multi-head self-attention, where every layer attends to the full sequence. (2) Global+Local ( Vaswani et al., 2017 ) is a hybrid schedule that alternates local sliding-window attention (window size 512) with periodic global-attention layers in a 4:1 ratio. (3) Talking Heads ( Shazeer et al., 2020 ) augments multi-head attention by learning to mix information across heads both before and after the softmax, enabling richer head-to-head interactions. (4) Diff Transformer ( Ye et al., 2024 ) defines attention as the difference of two softmax attention maps, which can sharpen or suppress patterns via contrastive weighting. and (5) IHA (Ours) , interleaved-head attention with pseudo-heads. Let N N be the sequence length, d d the per-head dimension, H H the number of heads, and P P the number of pseudo-heads per head. Since interleaving expands the effective sequence length from N N to N ​ P NP , global IHA has per-head complexity O ⁡ ( ( N ​ P ) 2 ​ d ) = O ⁡ ( P 2 ​ N 2 ​ d ) O((NP)^{2}d)=O(P^{2}N^{2}d) , i.e., a factor- P 2 P^{2} over global MHA; we therefore FLOP-match all comparisons. We use a hybrid local–global schedule (four sliding-window IHA layers with W ≔ N / ( 2 ​ P 2 ) W\coloneqq N/(2P^{2}) followed by one global layer) so the average cost matches the global-attention baseline up to constants; see App. C for details.

[85] h4: Benchmarks.

[86] p: For long-context evaluation we use RULER ( Hsieh et al., 2024 ) . For reasoning and coding we evaluate GSM8K ( Cobbe et al., 2021 ) , MATH-500 ( Hendrycks et al., 2021 ) , MBPP ( Austin et al., 2021 ) , and HumanEval ( Chen et al., 2021 ) .

[87] figure: Table 1 : SFT evaluation after fine-tuning on OpenThoughts. IHA achieves the best overall performance, with larger gains over the baselines than at pre-training. Δ \Delta is relative to Global Attention (green/red denote improvement/regression), and Avg. Rank ↓ \downarrow is the mean rank across metrics (lower is better). Model GSM8K P@1 Δ \Delta GSM8K Maj@16 Δ \Delta MATH-500 P@1 Δ \Delta MATH-500 Maj@16 Δ \Delta MBPP P@1 Δ \Delta MBPP P@10 Δ \Delta Avg. Rank ↓ \downarrow IHA (Ours) 34.3% + 4.8 54.2% + 5.8 10.0% + 1.2 18.4% + 2.8 15.5% + 0.8 41.6% + 0.4 1.5 Global Attention 29.5% – 48.4% – 8.8% – 15.6% – 14.7% – 41.2% – 3.8 Global+Local 26.5% – 3.0 46.9% – 1.5 7.6% – 1.2 15.0% – 0.6 15.0% + 0.3 41.9% + 0.7 4.3 Talking Heads 29.3% – 0.2 49.4% + 1.0 7.8% – 1.0 18.2% + 2.6 15.9% + 1.2 43.1% + 1.9 2.5 Diff Transformer 31.6% + 2.1 53.5% + 5.1 9.0% + 0.2 18.0% + 2.4 15.3% + 0.6 39.2% – 2.0 2.8

[88] figure: Table 2 : Pre-trained model evaluation (5-shot). IHA achieves the best overall reasoning performance, improving over Global Attention and Global+Local on GSM8K. Δ \Delta is relative to Global Attention (green/red denote improvement/regression), and Avg. Rank ↓ \downarrow is the mean rank across reported metrics (lower is better). Model GSM8K EM Δ \Delta GSM8K Maj@5 Δ \Delta MATH-500 EM Δ \Delta MBPP P@1 Δ \Delta HumanEval P@1 Δ \Delta Avg. Rank ↓ \downarrow IHA (Ours) 8.34% + 2.73 8.42% + 2.81 3.54% + 0.66 24.5% + 1.1 17.1% – 0.1 1.4 Global Attention 5.61% – 5.61% – 2.88% – 23.4% – 17.2% – 2.9 Global+Local 6.82% + 1.21 6.90% + 1.29 2.26% – 0.62 23.6% + 0.2 16.0% – 1.2 2.9 Talking Heads 5.46% – 0.15 5.38% – 0.23 – – 23.8% + 0.4 16.0% – 1.2 4.0 Diff Transformer 5.46% – 0.15 5.61% – – – 25.0% + 1.6 15.4% – 1.8 3.5

[89] h3: 5.2 Long Context Evaluation

[90] p: For long-context evaluation, we fine-tuned all models at 64k (beyond the pretraining window) and evaluated on RULER ( Fig. 2 ). IHA is consistently stronger on retrieval: on Multi-Key Retrieval it improves over Global Attention by +27% (4k), +32% (8k), and +112% (16k). Across the full RULER suite, IHA achieves the best average EM (exact match) ( 44.0% ), outperforming Global+Local ( 40.6% ), Diff Transformer ( 37.2% ), and Global Attention ( 35.0% ).

[91] figure: Figure 2 : RULER long-context results after 64k fine-tuning. (a) Multi-Key Retrieval accuracy at 4k/8k/16k context lengths (orange: IHA improvement over Sliding Window). (b) Overall RULER Exact Match (EM) show strong improvements using IHA.

[92] h3: 5.3 Reasoning Evaluation

[93] p: We evaluate pre-trained models in a 5-shot setting to probe reasoning ability prior to supervised instruction tuning ( Tab. 2 ). IHA (Ours) consistently improves over Global Attention on the core reasoning benchmarks: on GSM8K it achieves the best scores ( 8.34% EM and 8.42% Maj@5; +2.73 / +2.81 ), and it also leads on MATH-500 EM with 3.54% ( +0.66 ). Coding results are mixed, with a modest gain on the MBPP benchmark to 24.5% (second best) while HumanEval is near parity, but IHA is the most consistent method overall, achieving the best mean rank across reported metrics ( Avg. Rank ↓ = 1.4 \downarrow=1.4 ). Overall, these results indicate that IHA’s added expressivity translates into stronger reasoning performance even before downstream fine-tuning.

[94] h4: Supervised fine-tuning.

[95] p: We fine-tuned all variants on OpenThoughts ( Guha et al., 2025 ) (8B tokens) and evaluated with temperature 0.6 using 16 generations ( Tab. 1 ). IHA (Ours) achieves the best overall performance, leading on all reasoning metrics (e.g., 54.2% GSM8K Maj@16, +5.8 over Global Attention ; 18.4% MATH-500 Maj@16, +2.8 ) . On coding (MBPP), Talking Heads is best (15.9% P@1, 43.1% P@10), while IHA is second best on both MBPP metrics (15.5% P@1, 41.6% P@10) suggesting that while IHA’s expressivity excels at logical state tracking for math, head mixing is well-suited for function-level code generation. Overall, IHA remains consistently strong across tasks after SFT, whereas other variants tend to peak on specific datasets. and attaining the best Avg. Rank ↓ \downarrow ( 1.5 ) )

[96] h2: 6 Conclusion

[97] p: We introduced Interleaved Head Attention (IHA) , which overcomes MHA’s linear scaling by learning P P pseudo-queries, pseudo-keys, and pseudo-values per head as linear combinations of the original heads. Interactions between pseudo-queries and pseudo-keys induce up to P 2 P^{2} attention patterns per head. Our theory shows improved parameter efficiency on Polynomial Filters (IHA uses Θ ⁡ ( k ​ n 2 ) \Theta(\sqrt{k}n^{2}) parameters vs. Θ ⁡ ( k ​ n 2 ) \Theta(kn^{2}) for MHA) and on the order-sensitive CPM-3 task (IHA uses ⌈ N max ⌉ \lceil\sqrt{N_{\mathrm{max}}}\rceil heads vs. N max N_{\mathrm{max}} for MHA). Empirically, under FLOP-matched training, IHA improves Multi-Key retrieval on RULER by 10–20% (4k–16k) and, after OpenThoughts fine-tuning, improves reasoning on GSM8K by 5.8% and MATH-500 by 2.8% (majority vote) over full attention. Limitations. Global IHA can increase attention cost (scaling as O ⁡ ( P 2 ​ N 2 ) O(P^{2}N^{2}) ), which we mitigate with a sliding-window schedule; future work includes adaptive pseudo-head allocation and extensions to encoder–decoder and vision architectures.

[98] h2: Acknowledgements

[99] p: We thank Rohan Anil for their comments on the IHA algorithm and Niladri S. Chatterji for helping with the experiment setup.

[100] h2: References

[101] p: Appendix

[102] h6: Contents

[103] h2: Appendix A Extended Related Work

[104] h4: Hardness results for compositional reasoning.

[105] p: Recent theory has begun to formalize when standard multi-head attention (MHA) is an inefficient mechanism for compositional multi-step reasoning. Kozachinskiy et al. [2025] prove hardness results for binary relation composition and function composition, and Sanford et al. [2023] show that Match-3 requires Θ ⁡ ( N 3 ) \Theta(N^{3}) parameters under standard attention-based constructions. These settings share two structural requirements: global aggregation of evidence across many positions, and composition of intermediate relational signals prior to producing an output. Related behavior also appears in multi-hop QA benchmarks such as bAbI [ Weston et al., 2016 ] , which require combining information across multiple hops. We study these challenges through two controlled proxies that separate these requirements. Polynomial filters provide a standard k k -hop aggregation primitive from spectral GNNs [ Defferrard et al., 2016 , Chien et al., 2021 , Lingam et al., 2021 , Ekbote et al., 2023 ] , and CPM-3 isolates order-sensitive composition and counting. In both settings, we show that IHA realizes the relevant primitives with quadratic improvements in head and parameter efficiency relative to comparable MHA constructions.

[106] h4: Higher-order and multi-token attention.

[107] p: Several works enrich token interactions by going beyond pairwise query-key attention. The 2-Simplicial Transformer [ Clift et al., 2019 ] generalizes attention to trilinear interactions, and Roy and others [2025] provide an efficient Triton implementation. Strassen-style attention constructions use fast matrix multiplication ideas to accelerate particular compositional patterns [ Kozachinskiy et al., 2025 ] . Multi-Token Attention [ Golovneva et al., 2025 ] introduces mechanisms that mix information across small token groups, for example via local mixing over attention weights. These approaches typically modify the attention operator or introduce specialized higher-order structure. IHA is complementary. It preserves the standard attention operator and induces effective higher-order behavior by learning cross-head mixing of Q Q , K K , and V V into pseudo-heads, yielding a broad family of quadratic interaction patterns while remaining compatible with optimized attention kernels.

[108] h4: Iterative computation via depth or recurrence.

[109] p: Another approach to multi-step reasoning is to increase the number of sequential transformations, either via depth or recurrence. Looped transformers [ Saunshi et al., 2025 ] show that iterating a k k -layer block for L L loops can match a k ​ L kL -layer model, and can support chain-of-thought-like behavior through repeated refinement. These methods increase computation across iterations. Our approach is complementary. IHA increases within-layer interaction capacity by constructing P P pseudo-heads per head, typically with P = H P=H , using learned linear combinations of the original queries, keys, and values. Interactions between pseudo queries and pseudo keys induce up to P 2 P^{2} attention patterns per head within a single attention computation, without adding sequential depth.

[110] h4: Efficient and cross-head attention variants.

[111] p: A large body of work improves attention efficiency and head utilization. Multi-Query Attention (MQA) [ Shazeer, 2019 ] and Grouped Query Attention (GQA) [ Ainslie et al., 2023 ] reduce inference cost by sharing key and value projections across heads. Other methods explicitly couple heads by mixing attention logits or weights, including Talking-Heads [ Shazeer et al., 2020 ] and Knocking-Heads [ Zhou and others, 2025 ] , or by shaping attention maps, as in Differential Attention [ Ye et al., 2024 ] . In contrast, IHA enables cross-head interaction within attention by mixing Q Q , K K , and V V representations into pseudo-heads via learned linear combinations. This induces quadratic interaction structure while preserving the standard attention computation, and it remains compatible with efficient kernels such as FlashAttention [ Dao et al., 2022 ] .

[112] h2: Appendix B Theoretical Properties of IHA

[113] p: In this section, we establish theoretical properties of IHA that highlight its advantages over MHA. We present and prove several key representational results below.

[114] h3: B.1 IHA Superset Property

[115] h6: Proof.

[116] p: (Inclusion ℳ ⊆ 𝒫 p \mathcal{M}\subseteq\mathcal{P}_{p} ). Fix any MHA instance with weights { W Q ( m ) , W K ( m ) , W V ( m ) } m = 1 h \{W_{Q}^{(m)},W_{K}^{(m)},W_{V}^{(m)}\}_{m=1}^{h} . We construct a IHA instance (with any chosen p ≥ 1 p\geq 1 ) that realizes the same function by selecting parameters that ignore all but one pseudo-channel.

[117] p: Specifically, set for all m , i ∈ { 1 , … , h } m,i\in\{1,\ldots,h\} and ∀ j ∈ { 1 , ⋯ , p } \forall\ j\ \in\ \{1,\cdots,p\} ,

[118] table: α m , i , j Q = 𝟏 ( m = i ) , α m , i , j K = 𝟏 ( m = i ) , α m , i , j V = 𝟏 ( m = i ) , \displaystyle\alpha^{Q}_{m,i,j}=\bm{1}_{(m=i)},\qquad\alpha^{K}_{m,i,j}=\bm{1}_{(m=i)},\qquad\alpha^{V}_{m,i,j}=\bm{1}_{(m=i)},

[119] p: Further, choosing R ℓ ∈ ℝ h × h ​ p R^{\ell}\in\mathbb{R}^{h\times hp} so that it selects only the ( i , 1 ) (i,1) pseudo-block:

[120] table: R i , ( i ′ − 1 ) ​ p + j ℓ = { 1 if ​ i ′ = i ​ and ​ j = 1 , 0 otherwise. \displaystyle R^{\ell}_{\,i,\,(i^{\prime}-1)p+j}=\begin{cases}1&\text{if }i^{\prime}=i\text{ and }j=1,\\ 0&\text{otherwise.}\end{cases}

[121] p: Then for each head i i we have 𝑸 ~ i , j = 𝑿 ​ 𝑾 Q ( i ) \widetilde{\bm{Q}}_{i,j}=\bm{X}\bm{W}_{Q}^{(i)} , 𝑲 ~ i , j = 𝑿 ​ 𝑾 K ( i ) \widetilde{\bm{K}}_{i,j}=\bm{X}\bm{W}_{K}^{(i)} , 𝑽 ~ i , j = 𝑿 ​ 𝑾 V ( i ) \widetilde{\bm{V}}_{i,j}=\bm{X}\bm{W}_{V}^{(i)} ∀ j ∈ { 1 , ⋯ , p } \forall j\in\{1,\cdots,p\} . Consequently, the stacked attention produces an output whose only nonzero contribution is exactly the usual MHA head output, and the collapse via R ℓ R^{\ell} returns O i O_{i} equal to that MHA head output. Concatenating heads yields exactly the original MHA module. Hence ℳ ⊆ 𝒫 p \mathcal{M}\subseteq\mathcal{P}_{p} .

[122] p: Strictness for p ≥ 2 p\geq 2 (works for any n ≥ 2 n\geq 2 and any d d and any h ≥ 1 h\geq 1 ). It suffices to exhibit one h h -head IHA/PseudoIHA configuration (with p ≥ 2 p\geq 2 ) that cannot be represented by any h h -head MHA configuration.

[123] p: MHA is linear on repeated-token inputs. Fix n ≥ 2 n\geq 2 and consider inputs with repeated tokens

[124] table: 𝑿 = 𝟏 n ​ 𝒙 ⊤ ∈ ℝ n × d , \displaystyle\bm{X}=\mathbf{1}_{n}\bm{x}^{\top}\in\mathbb{R}^{n\times d},

[125] p: where 𝟏 n ∈ ℝ n \mathbf{1}_{n}\in\mathbb{R}^{n} is the all-ones vector and 𝒙 ∈ ℝ d \bm{x}\in\mathbb{R}^{d} . For any MHA head m m , define

[126] table: 𝒒 := 𝒙 ⊤ ​ 𝑾 Q ( m ) , 𝒌 := 𝒙 ⊤ ​ 𝑾 K ( m ) , 𝒗 := 𝒙 ⊤ ​ 𝑾 V ( m ) . \displaystyle\bm{q}:=\bm{x}^{\top}\bm{W}_{Q}^{(m)},\qquad\bm{k}:=\bm{x}^{\top}\bm{W}_{K}^{(m)},\qquad\bm{v}:=\bm{x}^{\top}\bm{W}_{V}^{(m)}.

[127] p: Then every token position has identical query/key/value, so the attention score matrix is constant:

[128] table: 𝑺 ( m ) = ( 𝑿 ​ 𝑾 Q m ) ​ ( 𝑿 ​ 𝑾 K m ) ⊤ = ( 𝟏 n ​ 𝒒 ) ​ ( 𝟏 n ​ 𝒌 ) ⊤ = ( ⟨ 𝒒 , 𝒌 ⟩ ) ​ 1 n ​ 𝟏 n ⊤ . \displaystyle\bm{S}^{(m)}=(\bm{X}\bm{W}_{Q}^{m})(\bm{X}\bm{W}_{K}^{m})^{\top}=(\mathbf{1}_{n}\bm{q})(\mathbf{1}_{n}\bm{k})^{\top}=(\langle\bm{q},\bm{k}\rangle)\,\mathbf{1}_{n}\mathbf{1}_{n}^{\top}.

[129] p: Since each row of S ( m ) S^{(m)} is the same, hence the row-wise softmax is uniform:

[130] table: σ ⁡ ( S ( m ) ) = 1 n ​ 𝟏 n ​ 𝟏 n ⊤ . \displaystyle\sigma\!\big(S^{(m)}\big)=\frac{1}{n}\mathbf{1}_{n}\mathbf{1}_{n}^{\top}.

[131] p: Therefore the head output equals

[132] table: Att ⁡ ( 𝑿 ​ 𝑾 Q ( m ) , 𝑿 ​ 𝑾 K ( m ) , 𝑿 ​ 𝑾 V ( m ) ) = 1 n ​ 𝟏 n ​ 𝟏 n ⊤ ​ ( 𝟏 n ​ v ) = 𝟏 n ​ 𝒗 = 𝟏 n ​ 𝒙 ⊤ ​ 𝑾 V ( m ) , \displaystyle\mathrm{Att}(\bm{X}\bm{W}_{Q}^{(m)},\bm{X}\bm{W}_{K}^{(m)},\bm{X}\bm{W}_{V}^{(m)})=\frac{1}{n}\mathbf{1}_{n}\mathbf{1}_{n}^{\top}(\mathbf{1}_{n}v)=\mathbf{1}_{n}\bm{v}=\mathbf{1}_{n}\bm{x}^{\top}\bm{W}_{V}^{(m)},

[133] p: which is linear in 𝒙 \bm{x} . Concatenating heads and applying any fixed output projection preserves linearity in each head. Hence every h h -head MHA module is linear on the repeated-token subspace { 𝟏 n ​ 𝒙 ⊤ : 𝒙 ∈ ℝ d } \{\mathbf{1}_{n}\bm{x}^{\top}:\bm{x}\in\mathbb{R}^{d}\} .

[134] p: IHA yields a non-linear mapping of the input when p ≥ 2 p\geq 2 . It is enough to consider the case p = 2 p=2 , since for any p > 2 p>2 we can deactivate the additional pseudo channels by setting their mixing coefficients to zero. Concretely, we could impose

[135] table: α m , i , j Q = α m , i , j K = α m , i , j V = 0 ∀ m , i ∈ { 1 , … , h } , ∀ j > 2 , \displaystyle\alpha^{Q}_{m,i,j}=\alpha^{K}_{m,i,j}=\alpha^{V}_{m,i,j}=0\qquad\forall\,m,i\in\{1,\dots,h\},\ \forall\,j>2,

[136] p: so that only the first two pseudo heads contribute (with the right reduction matrix R R ). We now construct a IHA layer whose output is nonlinear even on repeated-token inputs of the form 𝑿 = 𝟏 n ​ 𝒙 ⊤ \bm{X}=\mathbf{1}_{n}\bm{x}^{\top} .

[137] p: Towards this, we focus on only one head h h with two psudo tokens / heads. We let α m , i , 1 Q = α m , i , 1 K = α m , i , 1 V = α m , i , 2 V = 𝟏 ( m = i ) \alpha^{Q}_{m,i,1}=\alpha^{K}_{m,i,1}=\alpha^{V}_{m,i,1}=\alpha^{V}_{m,i,2}=\bm{1}_{(m=i)} and α m , i , 2 Q = α m , i , 2 K = − 𝟏 ( m = i ) \alpha^{Q}_{m,i,2}=\alpha^{K}_{m,i,2}=-\bm{1}_{(m=i)} . Hence, for any arbitrary head h h , we obtain,

[138] table: 𝑸 ¯ h = [ 𝑸 ~ h , 1 𝑸 ~ h , 2 ] 𝑲 ¯ h = [ 𝑲 ~ h , 1 𝑲 ~ h , 2 ] 𝑽 ¯ h = [ 𝑽 ~ h , 1 𝑽 ~ h , 2 ] \displaystyle\overline{\bm{Q}}_{h}=\begin{bmatrix}\widetilde{\bm{Q}}_{h,1}\\ \widetilde{\bm{Q}}_{h,2}\end{bmatrix}\qquad\overline{\bm{K}}_{h}=\begin{bmatrix}\widetilde{\bm{K}}_{h,1}\\ \widetilde{\bm{K}}_{h,2}\end{bmatrix}\qquad\overline{\bm{V}}_{h}=\begin{bmatrix}\widetilde{\bm{V}}_{h,1}\\ \widetilde{\bm{V}}_{h,2}\end{bmatrix}

[139] p: Hence, on computing, we obtain:

[140] table: 𝑸 ¯ h = [ 𝑸 h − 𝑸 h ] 𝑲 ¯ h = [ 𝑲 h − 𝑲 h ] 𝑽 ¯ h = [ 𝑽 h 𝑽 h ] \displaystyle\overline{\bm{Q}}_{h}=\begin{bmatrix}\bm{Q}_{h}\\ -\bm{Q}_{h}\end{bmatrix}\qquad\overline{\bm{K}}_{h}=\begin{bmatrix}{\bm{K}}_{h}\\ -{\bm{K}}_{h}\end{bmatrix}\qquad\overline{\bm{V}}_{h}=\begin{bmatrix}{\bm{V}}_{h}\\ {\bm{V}}_{h}\end{bmatrix}

[141] p: Note, that here, 𝑸 h , 𝑲 h , 𝑽 h \bm{Q}_{h},\bm{K}_{h},\bm{V}_{h} refer to the query, key and value matrices of MHA respectively. Hence, on computing attention, we obtain:

[142] table: 𝑷 ¯ h \displaystyle\overline{\bm{P}}_{h} = softmax ​ ( [ 𝑸 h ​ 𝑲 h ⊤ − 𝑸 h ​ 𝑲 h ⊤ − 𝑸 h ​ 𝑲 h ⊤ 𝑸 h ​ 𝑲 h ⊤ ] ) ​ [ 𝑽 h 𝑽 h ] \displaystyle=\text{softmax}\left({\begin{bmatrix}\bm{Q}_{h}\bm{K}_{h}^{\top}&-\bm{Q}_{h}\bm{K}_{h}^{\top}\\ -\bm{Q}_{h}\bm{K}_{h}^{\top}&\bm{Q}_{h}\bm{K}_{h}^{\top}\end{bmatrix}}\right)\begin{bmatrix}\bm{V}_{h}\\ \bm{V}_{h}\end{bmatrix}

[143] p: Further, choosing R ℓ ∈ ℝ h × h ​ p R^{\ell}\in\mathbb{R}^{h\times hp} so that it selects only the ( i , 1 ) (i,1) pseudo-block:

[144] table: R i , ( i ′ − 1 ) ​ p + j ℓ = { 1 if ​ i ′ = i ​ and ​ j = 1 , 0 otherwise. \displaystyle R^{\ell}_{\,i,\,(i^{\prime}-1)p+j}=\begin{cases}1&\text{if }i^{\prime}=i\text{ and }j=1,\\ 0&\text{otherwise.}\end{cases}

[145] p: The output of each head is:

[146] table: 𝑶 h = softmax ​ ( [ 𝑸 h ​ 𝑲 h ⊤ − 𝑸 h ​ 𝑲 h ⊤ ] ) ​ [ 𝑽 h 𝑽 h ] \displaystyle\bm{O}_{h}=\text{softmax}\left({\begin{bmatrix}\bm{Q}_{h}\bm{K}_{h}^{\top}&-\bm{Q}_{h}\bm{K}_{h}^{\top}\\ \end{bmatrix}}\right)\begin{bmatrix}\bm{V}_{h}\\ \bm{V}_{h}\end{bmatrix}

[147] p: Thus the overall IHA layer computes a nonlinear function of the input data.

[148] p: Conclusion. On the repeated-token subspace { 𝟏 n ​ 𝒙 ⊤ : 𝒙 ∈ ℝ d } \{\mathbf{1}_{n}\bm{x}^{\top}:\bm{x}\in\mathbb{R}^{d}\} , every h h -head MHA layer reduces to a linear map in 𝒙 \bm{x} , whereas the h h -head IHA construction above is nonlinear on the same set. Consequently, no h h -head MHA configuration can represent this IHA mapping, and thus ℳ ⊊ 𝒫 p \mathcal{M}\subsetneq\mathcal{P}_{p} for all p ≥ 2 p\geq 2 . ∎

[149] h3: B.2 Representing Polynomial Filters

[150] h4: Background.

[151] p: Given fixed input data 𝑿 ∈ ℝ N × d \bm{X}\in\mathbb{R}^{N\times d} and a full-rank graph adjacency matrix 𝑨 ∈ ℝ N × N \bm{A}\in\mathbb{R}^{N\times N} , the goal of this task is to obtain representations that depend on the graph in a polynomial manner. Specifically, given a polynomial order k k , our objective is to compute:

[152] table: 𝑿 ~ ≔ [ 𝑿 , 𝑨 ​ 𝑿 , … , 𝑨 k − 1 ​ 𝑿 ] . \displaystyle\widetilde{\bm{X}}\coloneqq[\bm{X},\bm{A}\bm{X},\ldots,\bm{A}^{k-1}\bm{X}].

[153] p: Note that, in most cases, it is not possible to recover 𝑨 \bm{A} or its powers 𝑨 i \bm{A}^{i} from any linear combination of the input features 𝑿 \bm{X} , primarily because 𝑿 \bm{X} is typically sparse or low-rank.

[154] h6: Proof.

[155] p: In this proof, our goal is to determine whether we can represent 𝑿 ~ \widetilde{\bm{X}} using MHA and IHA and if yes, the goal is to understand the number of parameters needed to do so. Since 𝑨 \bm{A} is full-rank, we cannot directly use 𝑿 \bm{X} . Instead, we define

[156] table: 𝑿 ^ = [ 𝑿 𝑰 ] , \widehat{\bm{X}}=\begin{bmatrix}\bm{X}&\bm{I}\end{bmatrix},

[157] p: which effectively augments 𝑿 \bm{X} with positional encodings. Henceforth, we work with 𝑿 ^ \widehat{\bm{X}} . We now examine the constructions and parameter requirements for MHA and IHA, omitting explicit layer dependence ℓ \ell for brevity.

[158] h4: MHA.

[159] p: From the definition, for linear attention, each head in MHA computes

[160] table: 𝑿 ~ MHA ( h ) \displaystyle\widetilde{\bm{X}}^{(h)}_{\texttt{MHA}} = ( 𝑿 ^ ​ 𝑾 Q , MHA h ​ ( 𝑾 K , MHA h ) ⊤ ​ 𝑿 ^ ⊤ ) ​ 𝑿 ^ ​ 𝑾 V , MHA h . \displaystyle=\left(\widehat{\bm{X}}\bm{W}_{Q,\texttt{MHA}}^{h}\left(\bm{W}_{K,\texttt{MHA}}^{h}\right)^{\!\top}\widehat{\bm{X}}^{\!\top}\right)\widehat{\bm{X}}\bm{W}_{V,\texttt{MHA}}^{h}.

[161] p: Since d < N d<N , we have 𝑿 ^ ​ 𝑾 Q , MHA h ​ ( 𝑾 K , MHA h ) ⊤ ​ 𝑿 ^ ⊤ ∈ ℝ N × N \widehat{\bm{X}}\bm{W}_{Q,\texttt{MHA}}^{h}\left(\bm{W}_{K,\texttt{MHA}}^{h}\right)^{\!\top}\widehat{\bm{X}}^{\!\top}\in\mathbb{R}^{N\times N} . To recover a polynomial filter, we must be able to solve

[162] table: [ 𝑿 , 𝑨 ​ 𝑿 , … , 𝑨 k − 1 ​ 𝑿 ] = [ 𝑿 ~ MHA ( 1 ) , … , 𝑿 ~ MHA ( H ) ] . \displaystyle[\bm{X},\bm{A}\bm{X},\ldots,\bm{A}^{k-1}\bm{X}]=\left[\widetilde{\bm{X}}^{(1)}_{\texttt{MHA}},\ldots,\widetilde{\bm{X}}^{(H)}_{\texttt{MHA}}\right].

[163] p: There are multiple design choices that can satisfy this equation. However, we are constrained by the fact that 𝑾 V , MHA h \bm{W}_{V,\texttt{MHA}}^{h} cannot depend on the input data 𝑿 ^ \widehat{\bm{X}} , and that the downstream embedding dimension must be k ​ d kd . Under these constraints, we can construct a minimal solution such that, for each head h h ,

[164] table: 𝑿 ^ ​ 𝑾 V , MHA h \displaystyle\widehat{\bm{X}}\bm{W}_{V,\texttt{MHA}}^{h} = 𝑿 , \displaystyle=\bm{X}, ( 𝑿 ^ ​ 𝑾 Q , MHA h ​ ( 𝑾 K , MHA h ) ⊤ ) ​ 𝑿 ^ ⊤ \displaystyle\left(\widehat{\bm{X}}\bm{W}_{Q,\texttt{MHA}}^{h}\left(\bm{W}_{K,\texttt{MHA}}^{h}\right)^{\!\top}\right)\widehat{\bm{X}}^{\!\top} = 𝑨 h − 1 . \displaystyle=\bm{A}^{h-1}.

[165] p: This construction requires exactly 2 ​ n ​ ( N + d ) ​ k + d ⁡ ( N + d ) ​ k 2n(N+d)k+d(N+d)k parameters. To show that it is indeed minimal, we proceed as follows. We first argue that atleast k k heads are needed to represent 𝑿 ~ \widetilde{\bm{X}} , and then we make arguments about the parameters. Towards this we argue about the rank of 𝑿 ~ \widetilde{\bm{X}} . By definition, we know that:

[166] table: 𝑿 ~ = [ 𝑿 𝑨 ​ 𝑿 ⋯ 𝑨 k − 1 ​ 𝑿 ] \displaystyle\widetilde{\bm{X}}=\begin{bmatrix}\bm{X}&\bm{A}\bm{X}&\cdots&\bm{A}^{k-1}\bm{X}\end{bmatrix}

[167] p: Hence,

[168] table: rank ​ ( 𝑿 ~ ) \displaystyle\text{rank}(\widetilde{\bm{X}}) = min ​ ( N , ∑ i = 0 k rank ​ ( 𝑨 i ​ 𝑿 ) ) \displaystyle=\text{min}\left({N,\sum_{i=0}^{k}\text{rank}(\bm{A}^{i}\bm{X})}\right) (1) ≤ min ​ ( N , k ​ d ) \displaystyle\leq\text{min}(N,kd) ≤ k ​ d \displaystyle\leq kd

[169] p: Where in the above, we have used that rank ​ ( 𝑨 i ​ 𝑿 ) ≤ d , ∀ i ∈ { 0 , ⋯ , k − 1 } \text{rank}(\bm{A}^{i}\bm{X})\leq d,\forall\ i\in\{0,\ \cdots,\ k-1\} , that k ​ d < N kd<N by assumption. Moreover, we would also like to note that for a generic 𝑿 \bm{X} , the rank can be tight. That is ∃ X \exists X such that rank ​ ( 𝑿 ~ ) = k ​ d \text{rank}(\widetilde{\bm{X}})=kd . It is tight. Hence we will make the argument that ecven IHA needs to have ranks greater or equal to this to be able to represnt the output. Hence, towards this lets first assume that we have the number of heads H H to be less than k k . Moreover, to match the dimensions of 𝑿 ~ \widetilde{\bm{X}} , we let the value weights for some heads to be arbitrary such that the final dimensions match. We weould like to note that for any particular head h h 𝑾 K , MHA h \bm{W}_{K,\texttt{MHA}}^{h} must depend only on 𝑨 \bm{A} and not on 𝑿 \bm{X} ; hence, we can write

[170] table: 𝑾 K , MHA h = [ B h ​ ( 𝑨 ) d × d h C h ​ ( 𝑨 ) N × d h ] . \displaystyle\bm{W}_{K,\texttt{MHA}}^{h}=\begin{bmatrix}B_{h}(\bm{A})_{d\times d_{h}}\\ C_{h}(\bm{A})_{N\times d_{h}}\end{bmatrix}.

[171] p: Note that for the dimensions to match, we would need ∑ h = 1 H d h = k ​ d \sum_{h=1}^{H}d_{h}=kd . Moreover, per head, we define for shorthand, Att h ​ ( 𝑿 ^ ) ≔ ( 𝑿 ^ ​ 𝑾 Q , MHA h ​ ( 𝑾 K , MHA h ) ⊤ ) ​ 𝑿 ^ ⊤ \text{Att}_{h}(\widehat{\bm{X}})\coloneqq\left(\widehat{\bm{X}}\bm{W}_{Q,\texttt{MHA}}^{h}\left(\bm{W}_{K,\texttt{MHA}}^{h}\right)^{\!\top}\right)\widehat{\bm{X}}^{\!\top} .

[172] p: We let the representation of MHA for H H number of heads less than k k be denoted by 𝑿 ′ ~ \widetilde{\bm{X}^{\prime}} , where:

[173] table: 𝑿 ′ ~ \displaystyle\widetilde{\bm{X}^{\prime}} = [ Att 1 ( OPEN 𝑿 ) ^ 𝑿 B 1 ( 𝑨 ) + Att 1 ( OPEN 𝑿 ) ^ C 1 ( 𝑨 ) , ⋯ , Att h ( OPEN 𝑿 ) ^ 𝑿 B H ( 𝑨 ) + Att H ( OPEN 𝑿 ) ^ C H ( 𝑨 ) ] \displaystyle=\begin{bmatrix}\text{Att}_{1}(\widehat{\bm{X})}\bm{X}B_{1}(\bm{A})+\text{Att}_{1}(\widehat{\bm{X})}C_{1}(\bm{A}),\ \cdots,\ \text{Att}_{h}(\widehat{\bm{X})}\bm{X}B_{H}(\bm{A})+\text{Att}_{H}(\widehat{\bm{X})}C_{H}(\bm{A})\end{bmatrix}

[174] p: Now since we want 𝑿 ′ ~ = 𝑿 ~ , ∀ 𝑿 \widetilde{\bm{X}^{\prime}}=\widetilde{\bm{X}},\forall~\bm{X} , if we substitute 𝑿 = 𝟎 \bm{X}=\bm{0} , then we can easily see that would imply that ∀ h ∈ { 1 , ⋯ , H } ​ Att h ​ C h ​ ( 𝑨 ) = 𝟎 \forall h\in\{1,\cdots,H\}~\text{Att}_{h}C_{h}(\bm{A})=\bm{0} . However, Att h ≠ 0 \text{Att}_{h}\neq 0 as if it were 𝟎 \bm{0} , then 𝑿 ′ ~ = 𝟎 \widetilde{\bm{X}^{\prime}}=\bm{0} which would then imply that 𝑿 ′ ~ ≠ 𝑿 ~ \widetilde{\bm{X}^{\prime}}\neq\widetilde{\bm{X}} for any arbitrary non-zero 𝑿 \bm{X} . Hence, the only solution is that C h ​ ( 𝑨 ) = 𝟎 C_{h}(\bm{A})=\bm{0} . Hence, we can cleanly write that:

[175] table: 𝑿 ′ ~ \displaystyle\widetilde{\bm{X}^{\prime}} = [ Att 1 ​ ( OPEN 𝑿 ) ^ ​ 𝑿 ​ B 1 ​ ( 𝑨 ) , ⋯ , Att H ​ ( OPEN 𝑿 ) ^ ​ 𝑿 ​ B H ​ ( 𝑨 ) CLOSE CLOSE ] \displaystyle=\begin{bmatrix}\text{Att}_{1}(\widehat{\bm{X})}\bm{X}B_{1}(\bm{A}),\ \cdots,\ \text{Att}_{H}(\widehat{\bm{X})}\bm{X}B_{H}(\bm{A})\end{bmatrix}

[176] p: Now we try to compute the rank of 𝑿 ′ ~ \widetilde{\bm{X}^{\prime}} . Note that again, we have assumed that H < k H<k . Hence,

[177] table: rank ​ ( 𝑿 ′ ~ ) \displaystyle\text{rank}(\widetilde{\bm{X}^{\prime}}) = min ​ ( N , ∑ i = 1 H rank ​ ( Att 1 ​ ( OPEN 𝑿 ) ^ ​ 𝑿 ​ B i ​ ( 𝑨 ) ) ) CLOSE \displaystyle=\text{min}\left({N,\sum_{i=1}^{H}\text{rank}(\text{Att}_{1}(\widehat{\bm{X})}\bm{X}B_{i}(\bm{A}))}\right) (2) ≤ min ​ ( N , ∑ i = 1 H min ​ ( rank ​ ( Att 1 ​ ( OPEN 𝑿 ) ^ ) , rank ​ ( 𝑿 ) , rank ​ ( B i ​ ( 𝑨 ) ) ) ) ) \displaystyle\leq\text{min}\left({N,\sum_{i=1}^{H}\text{min}\left({\text{rank}(\text{Att}_{1}(\widehat{\bm{X})}),\ \text{rank}(\bm{X}),\ \text{rank}(B_{i}(\bm{A})))}\right)}\right) ≤ min ​ ( N , H ​ d ) \displaystyle\leq\text{min}(N,Hd) ≤ H ​ d \displaystyle\leq Hd

[178] p: Now from Eq. 1 , we can see that the rank of the concatenation of the embeddings of polynomial filter are k ​ d kd when tight, however the rank in the case of 𝑿 ′ ~ \widetilde{\bm{X}^{\prime}} is at most H ​ d Hd . If H < k H<k , clearly the polynomial filter is more expressive and has a higher rank than that of 𝑿 ′ ~ \widetilde{\bm{X}^{\prime}} which implies that if H < k H<k , then the polynomial filter cannot be represented Multi-Head attention. Now we argue that for heads H > k H>k , there are constructions that can represnt the polynomial filter, however, it is not tight in terms of the parameters. Let us assume that there are H > k H>k heads. Moreover, we only make the arguement for the first head of MHA, and then this argument will essentially hold for all of the heads. We split this situation into multiple cases. Note that we are not really specifying what the dimension of each head in this case and assume it to be arbitrary. Hence, for the first case, we assume that the output dimension of the head is less than that of the first output of the polynomial filter. Hence, for equality, we need:

[179] table: Att 1 ​ ( 𝑿 ^ ) ​ X ​ B 1 ​ ( 𝑨 ) = X ​ Q 1 \displaystyle\text{Att}_{1}(\widehat{\bm{X}})XB_{1}(\bm{A})=XQ_{1}

[180] p: Note that B 1 ​ ( 𝑨 ) ∈ ℝ N × d 1 B_{1}(\bm{A})\in\mathbb{R}^{N\times d_{1}} , where d 1 ≤ d d_{1}\leq d Note that Q 1 ∈ ℝ d × d 1 Q_{1}\in\mathbb{R}^{d\times d_{1}} , and clearly Q 1 Q_{1} is a d 1 d_{1} rank matrix with one hot vectors across each column to isolate the rows that correspond to Att 1 ​ ( 𝑿 ^ ) ​ X ​ B 1 ​ ( 𝑨 ) \text{Att}_{1}(\widehat{\bm{X}})XB_{1}(\bm{A}) . Therefore, on taking the vec ​ ( ⋅ ) \text{vec}(\cdot) operator on both sides, we obtain:

[181] table: ( B ​ ( 𝑨 ) T ⊗ Att 1 ​ ( 𝑿 ^ ) ) ​ vec ​ ( 𝑿 ) = ( Q 1 T ⊗ 𝑰 ) ​ vec ​ ( X ) \displaystyle\left({B(\bm{A})^{T}\otimes\text{Att}_{1}(\widehat{\bm{X}})}\right)\text{vec}(\bm{X})=\left({Q_{1}^{T}\otimes\bm{I}}\right)\text{vec}(X)

[182] p: Since, we want this to be true for all X X , clearly,

[183] table: B ​ ( 𝑨 ) T ⊗ Att 1 ​ ( 𝑿 ^ ) \displaystyle B(\bm{A})^{T}\otimes\text{Att}_{1}(\widehat{\bm{X}}) = Q 1 T ⊗ 𝑰 \displaystyle=Q_{1}^{T}\otimes\bm{I} ⟹ rank ​ ( Att 1 ​ ( 𝑿 ^ ) ) \displaystyle\implies\text{rank}(\text{Att}_{1}(\widehat{\bm{X}})) = rank ​ ( Q 1 T ) ⋅ rank ​ ( 𝑰 ) / rank ​ ( B ⁡ ( 𝑨 ) ) \displaystyle=\text{rank}(Q_{1}^{T})\cdot\text{rank}(\bm{I})/\text{rank}(B(\bm{A}))

[184] p: Note that we have used rank ​ ( 𝑨 ⊗ 𝑩 ) = rank ​ ( 𝑨 ) ⋅ rank ​ ( 𝑩 ) \text{rank}(\bm{A}\otimes\bm{B})=\text{rank}(\bm{A})\cdot\text{rank}(\bm{B}) We know that rank ​ ( Q 1 T ) = d 1 \text{rank}(Q_{1}^{T})=d_{1} and hence, since rank ​ ( B ⁡ ( 𝑨 ) ) ≤ d 1 \text{rank}(B(\bm{A}))\leq d_{1} , then clearly,

[185] table: rank ​ ( Att 1 ​ ( 𝑿 ^ ) ) ≥ N \displaystyle\text{rank}(\text{Att}_{1}(\widehat{\bm{X}}))\geq N

[186] p: For this to be satisfied, we can see that the query and the key matrices both have to be of size at-least ( N + d ) ​ N (N+d)N . Moreover, the value matrix weights are then going to be of size ( N + d ) ​ d 1 (N+d)d_{1} . Hence, the total dimensions required for this is 2 ​ ( N + d ) ​ N + ( N + d ) ​ d 1 2(N+d)N+(N+d)d_{1} . We then argue about the second case which is what happens if d 1 > d d_{1}>d . For the argument, we assume that this spans two actual polynimial filters that is d < d 1 < 2 ​ d d<d_{1}<2d , but we will then show that the argument will hold even if d 1 d_{1} was arbitarty. Due to this, we obtain that, for equality between the representations when the number of heads are greater than that of the degree of the polynomial filter ( H > k H>k ), the following:

[187] table: [ Att 1 ​ ( OPEN 𝑿 ) ^ ​ 𝑿 ​ B 1 ​ ( 𝑨 ) ​ 𝑸 1 CLOSE Att 1 ​ ( OPEN 𝑿 ) ^ ​ 𝑿 ​ B 1 ​ ( 𝑨 ) ​ 𝑸 2 CLOSE ] = [ 𝑿 𝑨 ​ 𝑿 ​ 𝑸 ^ 𝟐 ] \displaystyle\begin{bmatrix}\text{Att}_{1}(\widehat{\bm{X})}\bm{X}B_{1}(\bm{A})\bm{Q}_{1}&\text{Att}_{1}(\widehat{\bm{X})}\bm{X}B_{1}(\bm{A})\bm{Q}_{2}\end{bmatrix}=\begin{bmatrix}\bm{X}&\bm{A}\bm{X}\bm{\widehat{Q}_{2}}\end{bmatrix}

[188] p: Note that 𝑸 𝟏 ∈ ℝ d 1 × d , 𝑸 𝟐 ∈ ℝ d 1 × ( d 1 − d ) , 𝑸 ^ 𝟐 ∈ ℝ d × d 1 \bm{Q_{1}}\in\mathbb{R}^{d_{1}\times d},\bm{Q_{2}}\in\mathbb{R}^{d_{1}\times(d_{1}-d)},\bm{\widehat{Q}_{2}}\in\mathbb{R}^{d\times d_{1}} , with ranks d , d 1 , d 1 − d d,d_{1},d_{1}-d respectively. Now we just equate them,

[189] table: ( ( B 1 ​ ( 𝑨 ) ​ 𝑸 1 ) T ⊗ Att 1 ​ ( OPEN 𝑿 ) ^ ) ⋅ vec ​ 𝑿 CLOSE \displaystyle\left({(B_{1}(\bm{A})\bm{Q}_{1})^{T}\otimes\text{Att}_{1}(\widehat{\bm{X})}}\right)\cdot\text{vec}\bm{X} = ( 𝑰 d × d ⊗ 𝑰 N × N ) ⋅ vec ​ 𝑿 \displaystyle=\left({\bm{I}_{d\times d}\otimes\bm{I}_{N\times N}}\right)\cdot\text{vec}\bm{X} ( ( B 1 ​ ( 𝑨 ) ​ 𝑸 2 ) T ⊗ Att 1 ​ ( OPEN 𝑿 ) ^ ) ⋅ vec ​ 𝑿 CLOSE \displaystyle\left({(B_{1}(\bm{A})\bm{Q}_{2})^{T}\otimes\text{Att}_{1}(\widehat{\bm{X})}}\right)\cdot\text{vec}\bm{X} = ( 𝑸 ^ 2 ⊗ 𝑨 ) ⋅ vec ​ 𝑿 \displaystyle=\left({\bm{\hat{Q}}_{2}\otimes\bm{A}}\right)\cdot\text{vec}\bm{X}

[190] p: Now we use the same rank argument as before, to conclude that rank ​ ( Att 1 ​ ( OPEN 𝑿 ) ^ ) ≥ N CLOSE \text{rank}(\text{Att}_{1}(\widehat{\bm{X})})\geq N , which again implies that the key and query weight matrices have weights ( N + d ) ​ N (N+d)N respectively.

[191] p: We make two generalizations now. We would first like to note that this argument also holds when d 1 ≥ ( k − 1 ) ​ d d_{1}\geq(k-1)d and hence, the above proof works for any dimensions. We would also like to note that this while this proof is done for the first head of MHA, it also generlizes to other heads. The proof holds similarly, and constructively that is for the second head of MHA, one can make the similar argument as that of the first with the only difference being that one needs to udnerstand the dimensions of the output polynomial filter that is which dimensions of the second head of MHA corresponds to which dimensiond of the polynomial filter. Then by repeating the argument of the ranks, one can obtain that again, key and query weight matrices have weights ( N + d ) ​ N (N+d)N respectively. This argument can be repeated for the third head and so on to finally conclude that the number of dimensions needed to represent this is H ​ n ​ ( N + d ) + ( d + N ) ​ ( k ​ d ) Hn(N+d)+(d+N)(kd) , when H ≥ k H\geq k . Clearly, this is minimal when H = k H=k .

[192] h4: IHA.

[193] p: We present a construction that achieves comparable parametric complexity while requiring only ⌈ k ⌉ \lceil\sqrt{k}\rceil heads. The proof proceeds by explicit construction. We note that 𝑿 ~ ( 𝟏 ) \bm{\widetilde{X}^{(1)}} denotes the representation after the first layer of attention.

[194] table: 𝑾 K , IHA ( 1 , h ) \displaystyle\bm{W}_{K,\texttt{IHA}}^{(1,h)} = [ 𝟎 d × N ( A h − 1 ) ⊤ ] ​ ∀ h ∈ { 1 , 2 , ⋯ , ⌈ k ⌉ } \displaystyle=\begin{bmatrix}\bm{0}_{d\times N}\\ (A^{h-1})^{\top}\end{bmatrix}~\forall~h\in\{1,2,\cdots,\lceil\sqrt{k}\rceil\} 𝑾 Q , IHA ( 1 , h ) \displaystyle\bm{W}_{Q,\texttt{IHA}}^{(1,h)} = [ 𝟎 d × N A ( h − 1 ) ⋅ ⌈ k ⌉ ] ​ ∀ h ∈ { 1 , 2 , ⋯ , ⌈ k ⌉ } \displaystyle=\begin{bmatrix}\bm{0}_{d\times N}\\ A^{(h-1)\cdot\lceil\sqrt{k}\rceil}\end{bmatrix}~\forall~h\in\{1,2,\cdots,\lceil\sqrt{k}\rceil\} 𝑾 V , IHA ( 1 , h ) \displaystyle\bm{W}_{V,\texttt{IHA}}^{(1,h)} = [ 𝑳 d × d ​ ⌈ k ⌉ h 𝟎 N × d ​ ⌈ k ⌉ ] ∈ ℝ ( N + d ) × ⌈ d ​ k ⌉ \displaystyle=\begin{bmatrix}\bm{L}^{h}_{d\times d\lceil\sqrt{k}\rceil}\\ \bm{0}_{N\times d\lceil\sqrt{k}\rceil}\end{bmatrix}\in\mathbb{R}^{(N+d)\times\lceil d\sqrt{k}\rceil} where, ​ 𝑳 d × d ​ ⌈ k ⌉ ( 1 , h ) \displaystyle\text{where, }\bm{L}^{(1,h)}_{d\times d\lceil\sqrt{k}\rceil} = [ 𝟎 d × ( h − 1 ) ​ d I d × d 𝟎 d × ⌈ k ⌉ − h ​ d ] ​ ∀ h ∈ { 1 , 2 , ⋯ , ⌈ k ⌉ } \displaystyle=\begin{bmatrix}\bm{0}_{d\times(h-1)d}&I_{d\times d}&\bm{0}_{d\times\lceil\sqrt{k}\rceil-hd}\end{bmatrix}\forall\ h~\in\{1,\ 2,\ \cdots,\ \lceil\sqrt{k}\rceil\} with the convention that ​ 𝟎 d × 0 ​ represents an empty vector. \displaystyle\quad\text{with the convention that }\bm{0}_{d\times 0}\text{ represents an empty vector.} moreover, ​ m k , h ( 1 ) \displaystyle\text{moreover, }m_{k,h}^{(1)} = 1 ​ ∀ k , h ∈ { 1 , 2 , ⋯ , ⌈ k ⌉ } \displaystyle=1\ \forall k,h\in\{1,2,\cdots,\lceil\sqrt{k}\rceil\}

[195] p: Hence, after one layer of attention we obtain the following. Using bracket notation [ ⋅ , ⋅ ] [\cdot,\cdot] for concatenation:

[196] table: 𝑿 ~ ( 𝟏 ) \displaystyle\bm{\widetilde{X}^{(1)}} = [ 𝑿 ~ IHA ( 1 , 1 ) , 𝑿 ~ IHA ( 1 , 2 ) , … , 𝑿 ~ IHA ( 1 , ⌈ k ⌉ ) ] \displaystyle=\Big[\widetilde{\bm{X}}^{(1,1)}_{\texttt{IHA}},\;\widetilde{\bm{X}}^{(1,2)}_{\texttt{IHA}},\;\ldots,\;\widetilde{\bm{X}}^{(1,\lceil\sqrt{k}\rceil)}_{\texttt{IHA}}\Big]

[197] p: where each 𝑿 ~ IHA ( 1 , h ) \widetilde{\bm{X}}^{(1,h)}_{\texttt{IHA}} aggregates over all key heads.

[198] table: 𝑿 ~ ( 𝟏 ) \displaystyle\bm{\widetilde{X}^{(1)}} = [ 𝑿 𝑨 ​ 𝑿 ⋯ 𝑨 ⌈ k ⌉ 2 − 1 ​ 𝑿 ] \displaystyle=\begin{bmatrix}\bm{X}&\bm{A}\bm{X}&\cdots&\bm{A}^{\lceil\sqrt{k}\rceil^{2}-1}\bm{X}\end{bmatrix}

[199] p: Hence, under this construction, the number of parameters is OPEN 2 ​ n ​ ( N + d ) ​ ⌈ k ⌉ + d ⁡ ( d + N ) ​ ⌈ k ⌉ 2 ) + ⌈ k ⌉ 2 2n(N+d)\lceil\sqrt{k}\rceil+d(d+N)\lceil\sqrt{k}\rceil^{2})+\lceil\sqrt{k}\rceil^{2}

[200] h4: Example.

[201] p: We present an example here to solidify the intuition of why such a construction helps. We assume that k = 4 k=4 . Hence, using the above constructions, the query, key, value matrices are defined as follows.

[202] table: 𝑾 Q , IHA ( 1 , 1 ) \displaystyle\bm{W}_{Q,\texttt{IHA}}^{(1,1)} = [ 𝟎 d × N 𝑰 N × N ] 𝑾 Q , IHA ( 1 , 2 ) = [ 𝟎 d × N ( A 2 ) ⊤ ] \displaystyle=\begin{bmatrix}\bm{0}_{d\times N}\\ \bm{I}_{N\times N}\end{bmatrix}\quad\bm{W}_{Q,\texttt{IHA}}^{(1,2)}=\begin{bmatrix}\bm{0}_{d\times N}\\ \left({A^{2}}\right)^{\top}\end{bmatrix} 𝑾 K , IHA ( 1 , 1 ) \displaystyle\bm{W}_{K,\texttt{IHA}}^{(1,1)} = [ 𝟎 d × N 𝑰 N × N ] 𝑾 K , IHA ( 1 , 2 ) = [ 𝟎 d × N ( A ) ⊤ ] \displaystyle=\begin{bmatrix}\bm{0}_{d\times N}\\ \bm{I}_{N\times N}\end{bmatrix}\quad\bm{W}_{K,\texttt{IHA}}^{(1,2)}=\begin{bmatrix}\bm{0}_{d\times N}\\ \left({A}\right)^{\top}\end{bmatrix} 𝑾 V , IHA ( 1 , 1 ) \displaystyle\bm{W}_{V,\texttt{IHA}}^{(1,1)} = [ 𝑰 d × d 𝟎 d × d 𝟎 N × d 𝟎 N × d ] 𝑾 V , IHA ( 1 , 2 ) = [ 𝟎 d × d 𝑰 d × d 𝟎 N × d 𝟎 N × d ] \displaystyle=\begin{bmatrix}\bm{I}_{d\times d}&\bm{0}_{d\times d}\\ \bm{0}_{N\times d}&\bm{0}_{N\times d}\end{bmatrix}\quad\bm{W}_{V,\texttt{IHA}}^{(1,2)}=\begin{bmatrix}\bm{0}_{d\times d}&\bm{I}_{d\times d}\\ \bm{0}_{N\times d}&\bm{0}_{N\times d}\end{bmatrix} m k , h ( 1 ) \displaystyle m_{k,h}^{(1)} = 1 ​ ∀ k , h ∈ { 1 , 2 } \displaystyle=1\ \forall\ k,h\in\{1,2\}

[203] p: We can see that first head of attention computes to

[204] table: Z 1 \displaystyle Z_{1} = [ ( 𝑿 ^ ​ 𝑾 Q , IHA ( 1 , 1 ) ​ ( 𝑾 K , IHA ( 1 , 1 ) ) ⊤ ​ 𝑿 ^ ⊤ ) ( 𝑿 ^ ​ 𝑾 Q , IHA ( 1 , 1 ) ​ ( 𝑾 K , IHA ( 1 , 2 ) ) ⊤ ​ 𝑿 ^ ⊤ ) ] ​ [ X ^ ​ 𝑾 V , IHA ( 1 , 1 ) X ^ ​ 𝑾 V , IHA ( 1 , 2 ) ] \displaystyle=\begin{bmatrix}\left({\widehat{\bm{X}}\bm{W}_{Q,\texttt{IHA}}^{(1,1)}(\bm{W}_{K,\texttt{IHA}}^{(1,1)})^{\top}\widehat{\bm{X}}^{\top}}\right)&\left({\widehat{\bm{X}}\bm{W}_{Q,\texttt{IHA}}^{(1,1)}(\bm{W}_{K,\texttt{IHA}}^{(1,2)})^{\top}\widehat{\bm{X}}^{\top}}\right)\end{bmatrix}\begin{bmatrix}\widehat{X}\bm{W}_{V,\texttt{IHA}}^{(1,1)}\\ \widehat{X}\bm{W}_{V,\texttt{IHA}}^{(1,2)}\end{bmatrix} = [ 𝑰 𝑨 ] ​ [ 𝑿 𝟎 𝟎 𝑿 ] \displaystyle=\begin{bmatrix}\bm{I}&\bm{A}\end{bmatrix}\begin{bmatrix}\bm{X}&\bm{0}\\ \bm{0}&\bm{X}\end{bmatrix} = [ 𝑿 𝑨 ​ 𝑿 ] \displaystyle=\begin{bmatrix}\bm{X}&\bm{A}\bm{X}\end{bmatrix}

[205] p: Similarly, for the second layer of attention, we obtain

[206] table: Z 2 \displaystyle Z_{2} = [ ( 𝑿 ^ ​ 𝑾 Q , IHA ( 1 , 2 ) ​ ( 𝑾 K , IHA ( 1 , 1 ) ) ⊤ ​ 𝑿 ^ ⊤ ) ( 𝑿 ^ ​ 𝑾 Q , IHA ( 1 , 2 ) ​ ( 𝑾 K , IHA ( 1 , 2 ) ) ⊤ ​ 𝑿 ^ ⊤ ) ] ​ [ X ^ ​ 𝑾 V , IHA ( 1 , 1 ) X ^ ​ 𝑾 V , IHA ( 1 , 2 ) ] \displaystyle=\begin{bmatrix}\left({\widehat{\bm{X}}\bm{W}_{Q,\texttt{IHA}}^{(1,2)}(\bm{W}_{K,\texttt{IHA}}^{(1,1)})^{\top}\widehat{\bm{X}}^{\top}}\right)&\left({\widehat{\bm{X}}\bm{W}_{Q,\texttt{IHA}}^{(1,2)}(\bm{W}_{K,\texttt{IHA}}^{(1,2)})^{\top}\widehat{\bm{X}}^{\top}}\right)\end{bmatrix}\begin{bmatrix}\widehat{X}\bm{W}_{V,\texttt{IHA}}^{(1,1)}\\ \widehat{X}\bm{W}_{V,\texttt{IHA}}^{(1,2)}\end{bmatrix} = [ 𝑨 2 𝑨 3 ] ​ [ 𝑿 𝟎 𝟎 𝑿 ] \displaystyle=\begin{bmatrix}\bm{A}^{2}&\bm{A}^{3}\end{bmatrix}\begin{bmatrix}\bm{X}&\bm{0}\\ \bm{0}&\bm{X}\end{bmatrix} = [ 𝑨 2 ​ 𝑿 𝑨 3 ​ 𝑿 ] \displaystyle=\begin{bmatrix}\bm{A}^{2}\bm{X}&\bm{A}^{3}\bm{X}\end{bmatrix}

[207] p: Hence, on concatenating the the embeddings from both the heads, we obtain

[208] table: 𝑿 ~ ( 𝟏 ) \displaystyle\bm{\widetilde{X}^{(1)}} = [ 𝑿 𝑨 ​ 𝑿 𝑨 2 ​ 𝑿 𝑨 3 ​ 𝑿 ] \displaystyle=\begin{bmatrix}\bm{X}&\bm{A}\bm{X}&\bm{A}^{2}\bm{X}&\bm{A}^{3}\bm{X}\end{bmatrix}

[209] p: ∎

[210] h4: IHA.

[211] p: We present a construction that requires only H ≔ ⌈ k ⌉ H\coloneqq\lceil\sqrt{k}\rceil heads. We set the number of pseudo heads to be P ≔ H P\coloneqq H . Note that the input to IHA is the same as MHA as defined below.

[212] table: 𝑿 ^ = [ 𝑿 𝑰 ] , \widehat{\bm{X}}=\begin{bmatrix}\bm{X}&\bm{I}\end{bmatrix},

[213] p: The proof proceeds by explicit construction. For every base head index m ∈ { 1 , 2 , … , H } m\in\{1,2,\ldots,H\} define

[214] table: 𝑾 K , IHA ( 1 , m ) \displaystyle\bm{W}_{K,\texttt{IHA}}^{(1,m)} = [ 𝟎 d × N ( A m − 1 ) ⊤ ] , \displaystyle=\begin{bmatrix}\bm{0}_{d\times N}\\ \left({A^{m-1}}\right)^{\top}\end{bmatrix}, 𝑾 Q , IHA ( 1 , m ) \displaystyle\bm{W}_{Q,\texttt{IHA}}^{(1,m)} = [ 𝟎 d × N A ( m − 1 ) ⋅ H ] , \displaystyle=\begin{bmatrix}\bm{0}_{d\times N}\\ A^{(m-1)\cdot H}\end{bmatrix}, 𝑾 V , IHA ( 1 , m ) \displaystyle\bm{W}_{V,\texttt{IHA}}^{(1,m)} = [ 𝑳 d × d ​ H ( 1 , m ) 𝟎 N × d ​ H ] ∈ ℝ ( N + d ) × d ​ H , \displaystyle=\begin{bmatrix}\bm{L}^{(1,m)}_{d\times dH}\\ \bm{0}_{N\times dH}\end{bmatrix}\in\mathbb{R}^{(N+d)\times dH},

[215] p: where 𝑳 d × d ​ H ( 1 , m ) \bm{L}^{(1,m)}_{d\times dH} routes into the m m -th d d -block (same selector trick as before):

[216] table: 𝑳 d × d ​ H ( 1 , m ) ≔ [ 𝟎 d × ( m − 1 ) ​ d I d × d 𝟎 d × ( H − m ) ​ d ] , ∀ m ∈ { 1 , … , H } , \displaystyle\bm{L}^{(1,m)}_{d\times dH}\;\coloneqq\;\begin{bmatrix}\bm{0}_{d\times(m-1)d}&I_{d\times d}&\bm{0}_{d\times(H-m)d}\end{bmatrix},\qquad\forall\ m\in\{1,\ldots,H\},

[217] p: with the convention that 𝟎 d × 0 \bm{0}_{d\times 0} is empty.

[218] p: We choose pseudo-head coefficients to be one-hot routers so that, inside each head h h , the P = H P=H pseudo-heads instantiate the same “key heads”:

[219] table: α m , h , j Q \displaystyle\alpha^{Q}_{m,h,j} ≔ 𝟙 [ m = h ] ⋅ 𝟙 [ j = 1 ] , \displaystyle\coloneqq\mathbbm{1}[m=h]\cdot\mathbbm{1}[j=1], α m , h , j K \displaystyle\alpha^{K}_{m,h,j} ≔ 𝟙 [ m = j ] , \displaystyle\coloneqq\mathbbm{1}[m=j], α m , h , j V \displaystyle\alpha^{V}_{m,h,j} ≔ 𝟙 [ m = j ] , ∀ m , h ∈ { 1 , … , H } , ∀ j ∈ { 1 , … , P } . \displaystyle\coloneqq\mathbbm{1}[m=j],\qquad\forall\ m,h\in\{1,\ldots,H\},\ \forall j\in\{1,\ldots,P\}.

[220] p: Thus, for each head h h and pseudo-head j j ,

[221] table: 𝑸 ~ h , j \displaystyle\widetilde{\bm{Q}}_{h,j} = ∑ m = 1 H α m , h , j Q 𝑿 ^ 𝑾 Q , IHA ( 1 , m ) = 𝟙 [ j = 1 ] 𝑿 ^ 𝑾 Q , IHA ( 1 , h ) , \displaystyle=\sum_{m=1}^{H}\alpha^{Q}_{m,h,j}\,\widehat{\bm{X}}\bm{W}_{Q,\texttt{IHA}}^{(1,m)}=\mathbbm{1}[j=1]\ \widehat{\bm{X}}\bm{W}_{Q,\texttt{IHA}}^{(1,h)}, 𝑲 ~ h , j \displaystyle\widetilde{\bm{K}}_{h,j} = ∑ m = 1 H α m , h , j K ​ 𝑿 ^ ​ 𝑾 K , IHA ( 1 , m ) = 𝑿 ^ ​ 𝑾 K , IHA ( 1 , j ) , \displaystyle=\sum_{m=1}^{H}\alpha^{K}_{m,h,j}\,\widehat{\bm{X}}\bm{W}_{K,\texttt{IHA}}^{(1,m)}=\widehat{\bm{X}}\bm{W}_{K,\texttt{IHA}}^{(1,j)}, 𝑽 ~ h , j \displaystyle\widetilde{\bm{V}}_{h,j} = ∑ m = 1 H α m , h , j V ​ 𝑿 ^ ​ 𝑾 V , IHA ( 1 , m ) = 𝑿 ^ ​ 𝑾 V , IHA ( 1 , j ) . \displaystyle=\sum_{m=1}^{H}\alpha^{V}_{m,h,j}\,\widehat{\bm{X}}\bm{W}_{V,\texttt{IHA}}^{(1,m)}=\widehat{\bm{X}}\bm{W}_{V,\texttt{IHA}}^{(1,j)}.

[222] p: For each head h h , IHA stacks pseudo-queries and keys row-wise:

[223] table: 𝑸 ¯ h ≔ [ 𝑸 ~ h , 1 ⊤ ; … ; 𝑸 ~ h , H ⊤ ] ⊤ , 𝑲 ¯ h ≔ [ 𝑲 ~ h , 1 ⊤ ; … ; 𝑲 ~ h , H ⊤ ] ⊤ , 𝑽 ¯ h ≔ [ 𝑽 ~ h , 1 ⊤ ; … ; 𝑽 ~ h , H ⊤ ] ⊤ . \displaystyle\overline{\bm{Q}}_{h}\coloneqq\left[\widetilde{\bm{Q}}_{h,1}^{\top};\ldots;\widetilde{\bm{Q}}_{h,H}^{\top}\right]^{\top},\quad\overline{\bm{K}}_{h}\coloneqq\left[\widetilde{\bm{K}}_{h,1}^{\top};\ldots;\widetilde{\bm{K}}_{h,H}^{\top}\right]^{\top},\quad\overline{\bm{V}}_{h}\coloneqq\left[\widetilde{\bm{V}}_{h,1}^{\top};\ldots;\widetilde{\bm{V}}_{h,H}^{\top}\right]^{\top}.

[224] p: IHA computes 𝑷 ¯ h = softmax ⁡ ( 𝑸 ¯ h ​ 𝑲 ¯ h ⊤ ) ​ 𝑽 ¯ h \overline{\bm{P}}_{h}=\mathrm{softmax}(\overline{\bm{Q}}_{h}\overline{\bm{K}}_{h}^{\top})\overline{\bm{V}}_{h} . Consider the output corresponding to the first pseudo query (i.e., the first N N rows of 𝑷 ¯ h \overline{\bm{P}}_{h} ), which we denote by 𝑷 h , 1 ∈ ℝ N × d ​ H \bm{P}_{h,1}\in\mathbb{R}^{N\times dH} . By construction, 𝑸 ~ h , 1 = 𝑿 ^ ​ 𝑾 Q , IHA ( 1 , h ) \widetilde{\bm{Q}}_{h,1}=\widehat{\bm{X}}\bm{W}_{Q,\texttt{IHA}}^{(1,h)} and 𝑲 ~ h , j = 𝑿 ^ ​ 𝑾 K , IHA ( 1 , j ) \widetilde{\bm{K}}_{h,j}=\widehat{\bm{X}}\bm{W}_{K,\texttt{IHA}}^{(1,j)} for all j j , so the same “aggregate over all key heads” block product:

[225] table: 𝑷 h , 1 \displaystyle\bm{P}_{h,1} = [ ( 𝑿 ^ ​ 𝑾 Q , IHA ( 1 , h ) ​ ( 𝑾 K , IHA ( 1 , 1 ) ) ⊤ ​ 𝑿 ^ ⊤ ) ⋯ ( 𝑿 ^ ​ 𝑾 Q , IHA ( 1 , h ) ​ ( 𝑾 K , IHA ( 1 , H ) ) ⊤ ​ 𝑿 ^ ⊤ ) ] ​ [ 𝑿 ^ ​ 𝑾 V , IHA ( 1 , 1 ) 𝑿 ^ ​ 𝑾 V , IHA ( 1 , H ) ] . \displaystyle=\begin{bmatrix}\left({\widehat{\bm{X}}\bm{W}_{Q,\texttt{IHA}}^{(1,h)}(\bm{W}_{K,\texttt{IHA}}^{(1,1)})^{\top}\widehat{\bm{X}}^{\top}}\right)&\cdots&\left({\widehat{\bm{X}}\bm{W}_{Q,\texttt{IHA}}^{(1,h)}(\bm{W}_{K,\texttt{IHA}}^{(1,H)})^{\top}\widehat{\bm{X}}^{\top}}\right)\end{bmatrix}\begin{bmatrix}\widehat{\bm{X}}\bm{W}_{V,\texttt{IHA}}^{(1,1)}\\ \vdots\\ \widehat{\bm{X}}\bm{W}_{V,\texttt{IHA}}^{(1,H)}\end{bmatrix}.

[226] p: Using the definitions of 𝑾 Q ( 1 , h ) \bm{W}_{Q}^{(1,h)} and 𝑾 K ( 1 , j ) \bm{W}_{K}^{(1,j)} ,

[227] table: 𝑿 ^ ​ 𝑾 Q , IHA ( 1 , h ) ​ ( 𝑾 K , IHA ( 1 , j ) ) ⊤ ​ 𝑿 ^ ⊤ = A ( h − 1 ) ​ H ​ A j − 1 = A ( h − 1 ) ​ H + ( j − 1 ) . \displaystyle\widehat{\bm{X}}\bm{W}_{Q,\texttt{IHA}}^{(1,h)}(\bm{W}_{K,\texttt{IHA}}^{(1,j)})^{\top}\widehat{\bm{X}}^{\top}\;=\;A^{(h-1)H}\,A^{j-1}\;=\;A^{(h-1)H+(j-1)}.

[228] p: Moreover, 𝑿 ^ ​ 𝑾 V , IHA ( 1 , j ) \widehat{\bm{X}}\bm{W}_{V,\texttt{IHA}}^{(1,j)} routes 𝑿 \bm{X} into the j j -th d d -block inside the d ​ H dH -dimensional head space. Therefore,

[229] table: 𝑷 h , 1 \displaystyle\bm{P}_{h,1} = [ A ( h − 1 ) ​ H ​ 𝑿 A ( h − 1 ) ​ H + 1 ​ 𝑿 ⋯ A ( h − 1 ) ​ H + ( H − 1 ) ​ 𝑿 ] . \displaystyle=\begin{bmatrix}A^{(h-1)H}\bm{X}&A^{(h-1)H+1}\bm{X}&\cdots&A^{(h-1)H+(H-1)}\bm{X}\end{bmatrix}.

[230] p: IHA then collapses the H ​ P HP pseudo-outputs down to H H heads via 𝑹 ∈ ℝ H × H ​ P \bm{R}\in\mathbb{R}^{H\times HP} . We choose 𝑹 \bm{R} to select only pseudo j = 1 j=1 from each head h h :

[231] table: 𝑹 h , ( h − 1 ) ​ H + 1 = 1 , 𝑹 h , ( h − 1 ) ​ H + j = 0 ∀ j ∈ { 2 , … , H } , 𝑹 h , ( h ′ − 1 ) ​ H + j = 0 ∀ h ′ ≠ h . \displaystyle\bm{R}_{h,(h-1)H+1}=1,\qquad\bm{R}_{h,(h-1)H+j}=0\ \ \forall j\in\{2,\ldots,H\},\qquad\bm{R}_{h,(h^{\prime}-1)H+j}=0\ \ \forall h^{\prime}\neq h.

[232] p: Hence the collapsed head output is

[233] table: 𝑶 h = 𝑷 h , 1 = [ A ( h − 1 ) ​ H ​ 𝑿 A ( h − 1 ) ​ H + 1 ​ 𝑿 ⋯ A ( h − 1 ) ​ H + ( H − 1 ) ​ 𝑿 ] . \displaystyle\bm{O}_{h}\;=\;\bm{P}_{h,1}\;=\;\begin{bmatrix}A^{(h-1)H}\bm{X}&A^{(h-1)H+1}\bm{X}&\cdots&A^{(h-1)H+(H-1)}\bm{X}\end{bmatrix}.

[234] p: Concatenate heads. Finally on concatenating representations from different heads, we obtain,

[235] table: 𝑿 ~ ( 𝟏 ) \displaystyle\bm{\widetilde{X}^{(1)}} = [ 𝑶 1 , 𝑶 2 , … , 𝑶 H ] = [ 𝑿 𝑨 ​ 𝑿 ⋯ 𝑨 H 2 − 1 ​ 𝑿 ] . \displaystyle=\Big[\bm{O}_{1},\bm{O}_{2},\ldots,\bm{O}_{H}\Big]=\begin{bmatrix}\bm{X}&\bm{A}\bm{X}&\cdots&\bm{A}^{H^{2}-1}\bm{X}\end{bmatrix}.

[236] p: Thus the construction realizes all powers up to A H 2 − 1 A^{H^{2}-1} in one layer. If H 2 > k H^{2}>k , the extra ( H 2 − k ) (H^{2}-k) blocks may be treated as padding (or zeroed by an output mask).

[237] p: Hence, under this construction, the number of parameters is OPEN 2 ​ n ​ ( N + d ) ​ ⌈ k ⌉ + d ⁡ ( d + N ) ​ ⌈ k ⌉ 2 ) + 4 ​ ⌈ k ⌉ 3 2n(N+d)\lceil\sqrt{k}\rceil+d(d+N)\lceil\sqrt{k}\rceil^{2})+4\lceil\sqrt{k}\rceil^{3}

[238] h4: Example ( k = 4 k=4 ).

[239] p: Let k = 4 k=4 , so H = P = 2 H=P=2 . Then

[240] table: 𝑾 Q ( 1 , 1 ) = [ 0 I ] , 𝑾 Q ( 1 , 2 ) = [ 0 A 2 ] , 𝑾 K ( 1 , 1 ) = [ 0 I ] , 𝑾 K ( 1 , 2 ) = [ 0 A ⊤ ] , \bm{W}_{Q}^{(1,1)}=\begin{bmatrix}0\\ I\end{bmatrix},\quad\bm{W}_{Q}^{(1,2)}=\begin{bmatrix}0\\ A^{2}\end{bmatrix},\quad\bm{W}_{K}^{(1,1)}=\begin{bmatrix}0\\ I\end{bmatrix},\quad\bm{W}_{K}^{(1,2)}=\begin{bmatrix}0\\ A^{\top}\end{bmatrix},

[241] p: and 𝑾 V ( 1 , 1 ) , 𝑾 V ( 1 , 2 ) \bm{W}_{V}^{(1,1)},\bm{W}_{V}^{(1,2)} route into the first/second d d -block, exactly as in the old proof. Choose α \alpha one-hot as above, and choose 𝑹 \bm{R} to pick pseudo j = 1 j=1 from each head. Then head h = 1 h=1 outputs [ 𝑿 , 𝑨 ​ 𝑿 ] [\bm{X},\bm{A}\bm{X}] , head h = 2 h=2 outputs [ 𝑨 2 ​ 𝑿 , 𝑨 3 ​ 𝑿 ] [\bm{A}^{2}\bm{X},\bm{A}^{3}\bm{X}] , and concatenation yields

[242] table: 𝑿 ~ ( 𝟏 ) = [ 𝑿 𝑨 ​ 𝑿 𝑨 2 ​ 𝑿 𝑨 3 ​ 𝑿 ] . \displaystyle\bm{\widetilde{X}^{(1)}}=\begin{bmatrix}\bm{X}&\bm{A}\bm{X}&\bm{A}^{2}\bm{X}&\bm{A}^{3}\bm{X}\end{bmatrix}.

[243] h3: B.3 Representing Count Permutation Match 3 (CPM-3)

[244] h4: Count Permutation Match-3 (CPM-3):

[245] p: We define a task denoted as Count Permutation Match-3 (CPM-3) where the goal is given a sequence of natural numbers denoted as { x i } i ∈ ℕ \{x_{i}\}_{i\in\mathbb{N}} , the goal is to be able to count the number of occurrences of a specific function, defined as follows. Let us define the number of triples ( OPEN i , j 1 , j 2 ) i,j_{1},j_{2}) where i i denotes the token in consideration, that satisfy:

[246] table: CPM i ​ ( 3 ) \displaystyle\mathrm{CPM}_{i}(3) = Count ( ∀ j 1 , j 2 : ϕ ( x i , x j 1 , x j 2 ) = 0 ) , \displaystyle=\mathrm{Count}\Bigl(\forall j_{1},j_{2}\ :\phi(x_{i},x_{j_{1}},x_{j_{2}})=0\Bigr),

[247] p: where,

[248] table: ϕ ⁡ ( x i , x j 1 , x j 2 ) \displaystyle\phi(x_{i},x_{j_{1}},x_{j_{2}}) : = x i + G ​ x j 1 + x j 2 ​ mod ​ M \displaystyle:=x_{i}+Gx_{j_{1}}+x_{j_{2}}\;\mathrm{mod}\;M where ​ M ​ is an arbitrary number and ​ G ​ is another number such that ​ G > 2 ​ M . \displaystyle\quad\text{ where }M\text{ is an arbitrary number and }G\text{ is another number such that}G>2M.

[249] p: The above condition is required to make sure that the function is not permutation invariant. That is, if x j 1 ≠ x j 2 x_{j_{1}}\neq x_{j_{2}} then, one can clearly see that:

[250] table: ϕ ⁡ ( x i , x j 1 , x j 2 ) ≠ ϕ ⁡ ( x i , x j 2 , x j 1 ) \displaystyle\phi(x_{i},x_{j_{1}},x_{j_{2}})\neq\phi(x_{i},x_{j_{2}},x_{j_{1}})

[251] p: Example. Let the sequence be ( 1 , 2 , 3 ) (1,2,3) and let G = 10 G=10 . Then we can compute x j 1 + x j 2 x_{j_{1}}+x_{j_{2}} as follows:

[252] table: 11 , 12 , 13 , 21 , 22 , 23 , 31 , 32 , 33 \displaystyle 11,\;12,\;13,\;21,\;22,\;23,\;31,\;32,\;33

[253] p: Then we can finally compute x i + x j 1 + x j 2 x_{i}+x_{j_{1}}+x_{j_{2}} which is computed as follows:

[254] table: 1 + x j 1 + x j 2 \displaystyle 1+x_{j_{1}}+x_{j_{2}} : = 12 , 13 , 14 , 22 , 23 , 24 , 32 , 33 , 34 \displaystyle:=12,\;13,\;14,\;22,\;23,\;24,\;32,\;33,\;34 2 + x j 1 + x j 2 \displaystyle 2+x_{j_{1}}+x_{j_{2}} : = 13 , 14 , 15 , 23 , 24 , 25 , 33 , 34 , 35 \displaystyle:=13,\;14,\;15,\;23,\;24,\;25,\;33,\;34,\;35 3 + x j 1 + x j 2 \displaystyle 3+x_{j_{1}}+x_{j_{2}} : = 14 , 15 , 16 , 24 , 25 , 26 , 34 , 35 , 36 \displaystyle:=14,\;15,\;16,\;24,\;25,\;26,\;34,\;35,\;36

[255] table: CPM 1 ​ ( 3 ) \displaystyle\mathrm{CPM}_{1}(3) : = 3 \displaystyle:=3 CPM 2 ​ ( 3 ) \displaystyle\mathrm{CPM}_{2}(3) : = 3 \displaystyle:=3 CPM 3 ​ ( 3 ) \displaystyle\mathrm{CPM}_{3}(3) : = 3 \displaystyle:=3

[256] h6: Proof.

[257] p: The proof will follow by construction as before. That is, we show that a representative solution exists, which is constructed via different components such as attention, MLP etc. We first describe the Encoder and Positional Encodings below

[258] h4: IHA.

[259] p: We first show the IHA construction and then proceed to the MHA construction.

[260] p: We prove realizability by explicit construction. The construction has three components: (i) an encoder/positional encoding map, (ii) one IHA attention layer (with pseudo-heads) that brings all symbols into a single vector space at each position via structured cyclic shifts, and (iii) an MLP that computes CPM i ​ ( 3 ) \mathrm{CPM}_{i}(3) by enumerating ordered pairs ( j 1 , j 2 ) (j_{1},j_{2}) and aggregating indicators of the constraint ϕ ⁡ ( x i , x j 1 , x j 2 ) ≡ 0 ​ ( mod ​ M ) \phi(x_{i},x_{j_{1}},x_{j_{2}})\equiv 0\ (\mathrm{mod}\ M) .

[261] h4: Encoder and Positional Encoding.

[262] p: The input is a length- N max N_{\max} sequence of natural numbers { x i } i = 1 N max \{x_{i}\}_{i=1}^{N_{\max}} . Assume the encoder and positional encoding produce

[263] table: 𝑿 ^ = [ 𝑿 , 𝑰 ] , \displaystyle\hat{\bm{X}}=[\,\bm{X},\ \bm{I}\,],

[264] p: where 𝑿 ∈ ℝ N max × 1 \bm{X}\in\mathbb{R}^{N_{\max}\times 1} stores the scalar token values, and 𝑰 ∈ ℝ N max × N max \bm{I}\in\mathbb{R}^{N_{\max}\times N_{\max}} is the identity positional encoding. Hence

[265] table: 𝑿 ^ ∈ ℝ N max × ( N max + 1 ) . \displaystyle\hat{\bm{X}}\in\mathbb{R}^{N_{\max}\times(N_{\max}+1)}.

[266] h4: IHA Attention (Layer 1).

[267] p: Let 𝑷 ∈ ℝ N max × N max \bm{P}\in\mathbb{R}^{N_{\max}\times N_{\max}} denote the cyclic permutation matrix and 𝒆 1 = [ 1 , 𝟎 1 × N max ] ⊤ \bm{e}_{1}=[1,\bm{0}_{1\times N_{\max}}]^{\top} . Set

[268] table: H ≔ ⌈ N max ⌉ , P ≔ H . H\coloneqq\lceil\sqrt{N_{\max}}\rceil,\qquad P\coloneqq H.

[269] p: We construct a single new-IHA layer with H H heads and P P pseudos per head. For each index m ∈ { 1 , … , H } m\in\{1,\dots,H\} define

[270] table: 𝑾 Q ( m ) \displaystyle\bm{W}_{Q}^{(m)} ≔ [ 𝟎 1 × N max 𝑷 ( m − 1 ) ​ H ] , 𝑾 K ( m ) ≔ [ 𝟎 1 × N max ( 𝑷 m − 1 ) ⊤ ] , \displaystyle\coloneqq\begin{bmatrix}\bm{0}_{1\times N_{\max}}\\ \bm{P}^{(m-1)H}\end{bmatrix},\qquad\bm{W}_{K}^{(m)}\coloneqq\begin{bmatrix}\bm{0}_{1\times N_{\max}}\\ \big(\bm{P}^{m-1}\big)^{\top}\end{bmatrix},

[271] p: and define value projections that route the scalar symbol coordinate into the m m -th coordinate of an H H -dimensional value space:

[272] table: 𝑾 V ( 1 ) = [ 𝒆 𝟏 ⋅ ⌈ N max ⌉ 𝟎 ( N max + 1 ) × ( ⌈ N max ⌉ − 1 ) ] , \displaystyle\bm{W}_{V}^{(1)}=\begin{bmatrix}\bm{e_{1}}\cdot{\lceil\sqrt{N_{\mathrm{max}}}\rceil}&\bm{0}_{(N_{\mathrm{max}}+1)\times(\lceil\sqrt{N_{\mathrm{max}}}\rceil-1)}\end{bmatrix},

[273] table: 𝑾 V , IHA ( 1 , ⌈ N max ⌉ ) = [ 𝟎 ( N max + 1 ) × ( ⌈ N max ⌉ − 1 ) 𝒆 𝟏 ⋅ ⌈ N max ⌉ ] , \displaystyle\bm{W}_{V,\texttt{IHA}}^{(1,\lceil\sqrt{N_{\mathrm{max}}}\rceil)}=\begin{bmatrix}\bm{0}_{(N_{\mathrm{max}}+1)\times(\lceil\sqrt{N_{\mathrm{max}}}\rceil-1)}&\bm{e_{1}}\cdot{\lceil\sqrt{N_{\mathrm{max}}}\rceil}\end{bmatrix},

[274] table: 𝑾 V , IHA ( 1 , h ) = [ 𝟎 ( N max + 1 ) × ( h − 1 ) 𝒆 𝟏 ⋅ ⌈ N max ⌉ 𝟎 ( N max + 1 ) × ( ⌈ N max ⌉ − h ) ] , \displaystyle\bm{W}_{V,\texttt{IHA}}^{(1,h)}=\begin{bmatrix}\bm{0}_{(N_{\mathrm{max}}+1)\times(h-1)}&\bm{e_{1}}\cdot{\lceil\sqrt{N_{\mathrm{max}}}\rceil}&\bm{0}_{(N_{\mathrm{max}}+1)\times(\lceil\sqrt{N_{\mathrm{max}}}\rceil-h)}\end{bmatrix},

[275] p: Pseudo-head mixing. Let α Q , α K , α V ∈ ℝ H × H × P \alpha^{Q},\alpha^{K},\alpha^{V}\in\mathbb{R}^{H\times H\times P} be the new-IHA mixing coefficients. We set them to one-hot routers:

[276] table: α m , h , j Q \displaystyle\alpha^{Q}_{m,h,j} ≔ 𝟙 [ m = h ] ⋅ 𝟙 [ j = 1 ] , \displaystyle\coloneqq\mathbbm{1}[m=h]\cdot\mathbbm{1}[j=1], α m , h , j K \displaystyle\alpha^{K}_{m,h,j} ≔ 𝟙 [ m = j ] , \displaystyle\coloneqq\mathbbm{1}[m=j], α m , h , j V \displaystyle\alpha^{V}_{m,h,j} ≔ 𝟙 [ m = j ] , ∀ m , h ∈ { 1 , … , H } , ∀ j ∈ { 1 , … , P } . \displaystyle\coloneqq\mathbbm{1}[m=j],\qquad\forall m,h\in\{1,\dots,H\},\ \forall j\in\{1,\dots,P\}.

[277] p: Consequently, for each head h h and pseudo j j ,

[278] table: 𝑸 ~ h , j \displaystyle\widetilde{\bm{Q}}_{h,j} = ∑ m = 1 H α m , h , j Q 𝑿 ^ 𝑾 Q ( m ) = 𝟙 [ j = 1 ] 𝑿 ^ 𝑾 Q ( h ) , \displaystyle=\sum_{m=1}^{H}\alpha^{Q}_{m,h,j}\ \hat{\bm{X}}\bm{W}_{Q}^{(m)}=\mathbbm{1}[j=1]\ \hat{\bm{X}}\bm{W}_{Q}^{(h)}, 𝑲 ~ h , j \displaystyle\widetilde{\bm{K}}_{h,j} = ∑ m = 1 H α m , h , j K ​ 𝑿 ^ ​ 𝑾 K ( m ) = 𝑿 ^ ​ 𝑾 K ( j ) , \displaystyle=\sum_{m=1}^{H}\alpha^{K}_{m,h,j}\ \hat{\bm{X}}\bm{W}_{K}^{(m)}=\hat{\bm{X}}\bm{W}_{K}^{(j)}, 𝑽 ~ h , j \displaystyle\widetilde{\bm{V}}_{h,j} = ∑ m = 1 H α m , h , j V ​ 𝑿 ^ ​ 𝑾 V ( m ) = 𝑿 ^ ​ 𝑾 V ( j ) . \displaystyle=\sum_{m=1}^{H}\alpha^{V}_{m,h,j}\ \hat{\bm{X}}\bm{W}_{V}^{(m)}=\hat{\bm{X}}\bm{W}_{V}^{(j)}.

[279] p: Pseudo-major stacking and attention. For each h ∈ { 1 , … , H } h\in\{1,\dots,H\} define the stacked pseudo matrices

[280] table: 𝑸 ¯ h ≔ [ 𝑸 ~ h , 1 ⊤ ; … ; 𝑸 ~ h , P ⊤ ] ⊤ , 𝑲 ¯ h ≔ [ 𝑲 ~ h , 1 ⊤ ; … ; 𝑲 ~ h , P ⊤ ] ⊤ , 𝑽 ¯ h ≔ [ 𝑽 ~ h , 1 ⊤ ; … ; 𝑽 ~ h , P ⊤ ] ⊤ . \displaystyle\overline{\bm{Q}}_{h}\coloneqq\left[\widetilde{\bm{Q}}_{h,1}^{\top};\ldots;\widetilde{\bm{Q}}_{h,P}^{\top}\right]^{\top},\quad\overline{\bm{K}}_{h}\coloneqq\left[\widetilde{\bm{K}}_{h,1}^{\top};\ldots;\widetilde{\bm{K}}_{h,P}^{\top}\right]^{\top},\quad\overline{\bm{V}}_{h}\coloneqq\left[\widetilde{\bm{V}}_{h,1}^{\top};\ldots;\widetilde{\bm{V}}_{h,P}^{\top}\right]^{\top}.

[281] p: Let

[282] table: 𝑺 h ≔ 1 H ​ 𝑸 ¯ h ​ 𝑲 ¯ h ⊤ , 𝑷 ¯ h ≔ softmax ⁡ ( 𝑺 h ) ​ 𝑽 ¯ h . \bm{S}_{h}\coloneqq\frac{1}{\sqrt{H}}\ \overline{\bm{Q}}_{h}\overline{\bm{K}}_{h}^{\top},\qquad\overline{\bm{P}}_{h}\coloneqq\mathrm{softmax}(\bm{S}_{h})\ \overline{\bm{V}}_{h}.

[283] p: We set the softmax temperature to 0 0 (hard attention), so that the attention map implements the unique routing induced by the permutation structure. Define 𝑷 h , 1 ∈ ℝ N max × H \bm{P}_{h,1}\in\mathbb{R}^{N_{\max}\times H} to be the output block of 𝑷 ¯ h \overline{\bm{P}}_{h} corresponding to the first pseudo (i.e., the rows aligned with 𝑸 ~ h , 1 \widetilde{\bm{Q}}_{h,1} ). Under hard attention, the construction ensures that 𝑸 ~ h , 1 \widetilde{\bm{Q}}_{h,1} routes to each pseudo-key 𝑲 ~ h , j \widetilde{\bm{K}}_{h,j} according to the cyclic shifts, yielding

[284] table: 𝑷 h , 1 \displaystyle\bm{P}_{h,1} = ∑ j = 1 H 𝑷 ( h − 1 ) ​ H + ( j − 1 ) ​ 𝑿 ^ ​ 𝑾 V ( j ) . \displaystyle=\sum_{j=1}^{H}\bm{P}^{(h-1)H+(j-1)}\ \hat{\bm{X}}\bm{W}_{V}^{(j)}.

[285] p: Since 𝑿 ^ ​ 𝑾 V ( j ) \hat{\bm{X}}\bm{W}_{V}^{(j)} places the scalar symbol value into the j j -th coordinate of ℝ H \mathbb{R}^{H} , it follows that 𝑷 h , 1 \bm{P}_{h,1} contains, in an H H -dimensional value space, the H H cyclic shifts

[286] table: [ 𝑷 ( h − 1 ) ​ H ​ 𝑿 , 𝑷 ( h − 1 ) ​ H + 1 ​ 𝑿 , … , 𝑷 ( h − 1 ) ​ H + ( H − 1 ) ​ 𝑿 ] \displaystyle\begin{bmatrix}\bm{P}^{(h-1)H}\bm{X},&\bm{P}^{(h-1)H+1}\bm{X},&\ldots,&\bm{P}^{(h-1)H+(H-1)}\bm{X}\end{bmatrix}

[287] p: Let 𝑹 ∈ ℝ H × H ​ P \bm{R}\in\mathbb{R}^{H\times HP} be the collapse matrix in the new-IHA definition. Choose 𝑹 \bm{R} to select only pseudo j = 1 j=1 from each head:

[288] table: 𝑹 h , ( h − 1 ) ​ H + 1 = 1 , 𝑹 h , ( h − 1 ) ​ H + j = 0 ​ ∀ j ∈ { 2 , … , H } , 𝑹 h , ( h ′ − 1 ) ​ H + j = 0 ​ ∀ h ′ ≠ h . \displaystyle\bm{R}_{h,(h-1)H+1}=1,\qquad\bm{R}_{h,(h-1)H+j}=0\ \forall j\in\{2,\dots,H\},\qquad\bm{R}_{h,(h^{\prime}-1)H+j}=0\ \forall h^{\prime}\neq h.

[289] p: Then the per-head output is 𝑶 h = 𝑷 h , 1 \bm{O}_{h}=\bm{P}_{h,1} .

[290] p: Representation after Layer 1. Let 𝑿 ^ ( 1 ) \hat{\bm{X}}^{(1)} denote the representation after the new-IHA layer, obtained by concatenating heads:

[291] table: 𝑿 ^ ( 1 ) ≔ [ 𝑶 1 , 𝑶 2 , … , 𝑶 H ] ∈ ℝ N max × H 2 . \hat{\bm{X}}^{(1)}\coloneqq[\,\bm{O}_{1},\bm{O}_{2},\ldots,\bm{O}_{H}\,]\in\mathbb{R}^{N_{\max}\times H^{2}}.

[292] p: By the expression for 𝑶 h = 𝑷 h , 1 \bm{O}_{h}=\bm{P}_{h,1} , 𝑿 ^ ( 1 ) \hat{\bm{X}}^{(1)} contains all cyclic shifts { 𝑷 t ​ 𝑿 } t = 0 H 2 − 1 \{\bm{P}^{t}\bm{X}\}_{t=0}^{H^{2}-1} arranged in a fixed, known indexing across its H 2 H^{2} coordinates. In particular, for every token position i i , the vector 𝑿 ^ ( 1 ) [ i , : ] \hat{\bm{X}}^{(1)}[i,:] provides access to the entire multiset of symbols { x 1 , … , x N max } \{x_{1},\dots,x_{N_{\max}}\} (with their cyclic order), within a single vector space.

[293] h4: MLP.

[294] p: Note that 𝑿 ^ ( 1 ) \hat{\bm{X}}^{(1)} allows each token to access all N max N_{\mathrm{max}} symbols within a single (known) coordinate system. Hence, the MLP can be constructed as follows. The first linear layer is chosen to enumerate all ordered pairs ( j 1 , j 2 ) (j_{1},j_{2}) (i.e., all P 2 N max = N max ​ ( N max − 1 ) {}^{N_{\mathrm{max}}}P_{2}=N_{\mathrm{max}}(N_{\mathrm{max}}-1) permutations, or N max 2 N_{\mathrm{max}}^{2} pairs if allowing j 1 = j 2 j_{1}=j_{2} ), and for each such pair it forms the quantity

[295] table: x i + G ​ x j 1 + x j 2 . x_{i}+Gx_{j_{1}}+x_{j_{2}}.

[296] p: This can be implemented by a linear map whose hidden width scales with the number of pairs, with weights that (i) select x j 1 x_{j_{1}} and x j 2 x_{j_{2}} from 𝑿 ^ ( 1 ) [ i , : ] \hat{\bm{X}}^{(1)}[i,:] and (ii) multiply the selected x j 1 x_{j_{1}} by G G while leaving x j 2 x_{j_{2}} unscaled. Furthermore, if the activation after this first layer is defined as f ⁡ ( ⋅ ) = ReLU ⁡ ( 1 − ϕ ⁡ ( ⋅ ) ) f(\cdot)=\mathrm{ReLU}\bigl(1-\phi(\cdot)\bigr) where ϕ ⁡ ( ⋅ ) \phi(\cdot) is the modulo- M M operation, then the activation produces a nonzero output if and only if

[297] table: x i + G ​ x j 1 + x j 2 ≡ 0 ( mod ​ M ) . x_{i}+Gx_{j_{1}}+x_{j_{2}}\equiv 0\quad(\mathrm{mod}\ M).

[298] p: Finally, the second linear layer is responsible solely for aggregating (summing) these indicators across all ordered pairs ( j 1 , j 2 ) (j_{1},j_{2}) , thereby producing CPM i ​ ( 3 ) \mathrm{CPM}_{i}(3) at each token position i i .

[299] h4: Total Parameter Count.

[300] p: Considering all parameters described above, the total parameter count (for the new-IHA construction) denoted by T IHA T_{\textbf{IHA}} can be upper bounded by the sum of: (i) base query/key/value projections, (ii) pseudo mixing coefficients, (iii) the collapse matrix 𝑹 \bm{R} , and (iv) the MLP parameters. Concretely, with H = ⌈ N max ⌉ H=\lceil\sqrt{N_{\mathrm{max}}}\rceil and P = H P=H , the attention-layer parameters satisfy

[301] table: ( Query + Key ) \displaystyle(\text{Query}+\text{Key}) = 2 ⋅ H ⋅ ( N max + 1 ) ​ N max , \displaystyle=2\cdot H\cdot(N_{\mathrm{max}}+1)N_{\mathrm{max}}, Value = H ⋅ ( N max + 1 ) ⋅ H = ( N max + 1 ) ​ H 2 , \displaystyle=H\cdot(N_{\mathrm{max}}+1)\cdot H=(N_{\mathrm{max}}+1)H^{2}, Pseudo Mix Coeffs = 3 ⋅ H ⋅ H ⋅ P = 3 ​ H 3 , \displaystyle=3\cdot H\cdot H\cdot P=3H^{3}, Collapse ​ ( 𝑹 ) \displaystyle\text{Collapse }(\bm{R}) = H ⋅ ( H ​ P ) = H 3 . \displaystyle=H\cdot(HP)=H^{3}.

[302] p: For the MLP, the first layer requires width proportional to the number of ordered pairs, i.e. P 2 N max {}^{N_{\mathrm{max}}}P_{2} , and thus contributes on the order of H 2 ⋅ N max ​ ( N max − 1 ) H^{2}\cdot N_{\mathrm{max}}(N_{\mathrm{max}}-1) parameters (up to constant factors depending on the exact hidden width choice), while the second layer aggregates these counts and contributes at most N max 2 N_{\mathrm{max}}^{2} parameters. Putting these together,

[303] table: T IHA \displaystyle T_{\textbf{IHA}} = ( Query + Key ) + Value + MLP + Pseudo Mix Coeffs + Collapse \displaystyle\;=\;(\text{Query}+\text{Key})+\text{Value}+\text{MLP}+\text{Pseudo Mix Coeffs}+\text{Collapse} ≤ 2 ​ ( N max 2 + N max ) ​ H + ( N max + 1 ) ​ H 2 + H 2 ​ N max ​ ( N max − 1 ) + N max 2 + 4 ​ H 3 . \displaystyle\;\leq\;2(N_{\mathrm{max}}^{2}+N_{\mathrm{max}})H\;+\;(N_{\mathrm{max}}+1)H^{2}\;+\;H^{2}N_{\mathrm{max}}(N_{\mathrm{max}}-1)\;+\;N_{\mathrm{max}}^{2}\;+\;4H^{3}. ≤ 2 ​ ( N max 2 + N max ) ​ ⌈ N max ⌉ + ( N max + 1 ) ​ ⌈ N max ⌉ 2 + ⌈ N max ⌉ 2 ​ N max ​ ( N max − 1 ) + N max 2 + 4 ​ ⌈ N max ⌉ 3 . \displaystyle\;\leq\;2(N_{\mathrm{max}}^{2}+N_{\mathrm{max}})\lceil\sqrt{N_{\mathrm{max}}}\rceil\;+\;(N_{\mathrm{max}}+1)\lceil\sqrt{N_{\mathrm{max}}}\rceil^{2}\;+\;\lceil\sqrt{N_{\mathrm{max}}}\rceil^{2}N_{\mathrm{max}}(N_{\mathrm{max}}-1)\;+\;N_{\mathrm{max}}^{2}\;+\;4\lceil\sqrt{N_{\mathrm{max}}}\rceil^{3}. ≤ 37 ​ N max 2.5 + N max 2 ​ ( N max − 1 ) + N max 2 \displaystyle\;\leq\;37N_{\mathrm{max}}^{2.5}+N_{\mathrm{max}}^{2}(N_{\mathrm{max}}-1)+N_{\mathrm{max}}^{2}

[304] p: Substituting H = ⌈ N max ⌉ H=\lceil\sqrt{N_{\mathrm{max}}}\rceil yields a polynomial bound in N max N_{\mathrm{max}} (with the same dominant scaling coming from the MLP term), completing the construction.

[305] h4: Example N max = 4 N_{\max}=4 ).

[306] p: We solidify the intuition behind the construction with a concrete instance. Let the input tokens be 1 , 2 , 3 , 4 1,2,3,4 and N max = 4 N_{\mathrm{max}}=4 . Then the encoder with positional encoding produce

[307] table: 𝑿 ^ = [ 1 1 0 0 0 2 0 1 0 0 3 0 0 1 0 4 0 0 0 1 ] ∈ ℝ 4 × 5 . \displaystyle\hat{\bm{X}}=\begin{bmatrix}1&1&0&0&0\\ 2&0&1&0&0\\ 3&0&0&1&0\\ 4&0&0&0&1\end{bmatrix}\in\mathbb{R}^{4\times 5}.

[308] p: Set H ≔ ⌈ N max ⌉ = 2 H\coloneqq\lceil\sqrt{N_{\mathrm{max}}}\rceil=2 and P ≔ H = 2 P\coloneqq H=2 . Let 𝑷 ∈ ℝ 4 × 4 \bm{P}\in\mathbb{R}^{4\times 4} be the cyclic permutation matrix (shifting down by one):

[309] table: 𝑷 = [ 0 0 0 1 1 0 0 0 0 1 0 0 0 0 1 0 ] , 𝒆 1 = [ 1 , 0 , 0 , 0 , 0 ] ⊤ ∈ ℝ 5 . \bm{P}=\begin{bmatrix}0&0&0&1\\ 1&0&0&0\\ 0&1&0&0\\ 0&0&1&0\end{bmatrix},\qquad\bm{e}_{1}=[1,0,0,0,0]^{\top}\in\mathbb{R}^{5}.

[310] p: Let 𝒖 1 = [ 1 , 0 ] ⊤ \bm{u}_{1}=[1,0]^{\top} and 𝒖 2 = [ 0 , 1 ] ⊤ \bm{u}_{2}=[0,1]^{\top} denote the standard basis of ℝ 2 \mathbb{R}^{2} .

[311] p: Query, Keys and Values. We define the query and key matrices for m ∈ { 1 , 2 } m\in\{1,2\} :

[312] table: 𝑾 Q , IHA ( 1 , m ) \displaystyle\bm{W}_{Q,\texttt{IHA}}^{(1,m)} = [ 𝟎 1 × N max 𝑷 ( m − 1 ) ​ H ] , \displaystyle=\begin{bmatrix}\bm{0}_{1\times N_{\mathrm{max}}}\\ \bm{P}^{(m-1)H}\end{bmatrix}, 𝑾 K ( 1 , m ) \displaystyle\bm{W}_{K}^{(1,m)} = [ 𝟎 1 × N max ( 𝑷 m − 1 ) ⊤ ] , \displaystyle=\begin{bmatrix}\bm{0}_{1\times N_{\mathrm{max}}}\\ \big(\bm{P}^{m-1}\big)^{\top}\end{bmatrix},

[313] p: Hence, explicitly,

[314] table: 𝑾 Q ( 1 , 1 ) = [ 𝟎 𝑰 ] , 𝑾 Q ( 1 , 2 ) = [ 𝟎 𝑷 2 ] , \displaystyle\bm{W}_{Q}^{(1,1)}=\begin{bmatrix}\bm{0}\\ \bm{I}\end{bmatrix},\qquad\bm{W}_{Q}^{(1,2)}=\begin{bmatrix}\bm{0}\\ \bm{P}^{2}\end{bmatrix},

[315] table: 𝑾 K ( 1 , 1 ) = [ 𝟎 𝑰 ] , 𝑾 K ( 1 , 2 ) = [ 𝟎 𝑷 ⊤ ] , \displaystyle\bm{W}_{K}^{(1,1)}=\begin{bmatrix}\bm{0}\\ \bm{I}\end{bmatrix},\qquad\bm{W}_{K}^{(1,2)}=\begin{bmatrix}\bm{0}\\ \bm{P}^{\top}\end{bmatrix},

[316] p: and

[317] table: 𝑾 V ( 1 , 1 ) = 2 ​ 𝒆 1 ​ 𝒖 1 ⊤ = [ 2 0 0 0 0 0 0 0 0 0 ] , 𝑾 V , IHA ( 1 , 2 ) = 2 ​ 𝒆 1 ​ 𝒖 2 ⊤ = [ 0 2 0 0 0 0 0 0 0 0 ] . \displaystyle\bm{W}_{V}^{(1,1)}=2\,\bm{e}_{1}\,\bm{u}_{1}^{\top}=\begin{bmatrix}2&0\\ 0&0\\ 0&0\\ 0&0\\ 0&0\end{bmatrix},\qquad\bm{W}_{V,\texttt{IHA}}^{(1,2)}=2\,\bm{e}_{1}\,\bm{u}_{2}^{\top}=\begin{bmatrix}0&2\\ 0&0\\ 0&0\\ 0&0\\ 0&0\end{bmatrix}.

[318] p: Pseudo-head mixing. In IHA , each head h ∈ { 1 , 2 } h\in\{1,2\} forms pseudos j ∈ { 1 , 2 } j\in\{1,2\} via α Q , α K , α V ∈ ℝ H × H × P \alpha^{Q},\alpha^{K},\alpha^{V}\in\mathbb{R}^{H\times H\times P} . We choose one-hot mixing:

[319] table: α m , h , j Q \displaystyle\alpha^{Q}_{m,h,j} ≔ 𝟙 [ m = h ] 𝟙 [ j = 1 ] , \displaystyle\coloneqq\mathbbm{1}[m=h]\mathbbm{1}[j=1], α m , h , j K \displaystyle\alpha^{K}_{m,h,j} ≔ 𝟙 [ m = j ] , \displaystyle\coloneqq\mathbbm{1}[m=j], α m , h , j V \displaystyle\alpha^{V}_{m,h,j} ≔ 𝟙 [ m = j ] . \displaystyle\coloneqq\mathbbm{1}[m=j].

[320] p: Therefore, for each head h h ,

[321] table: 𝑸 ~ h , 1 = 𝑿 ^ ​ 𝑾 Q ( 1 , h ) , 𝑸 ~ h , 2 = 𝟎 , 𝑲 ~ h , 1 = 𝑿 ^ ​ 𝑾 K ( 1 , 1 ) , 𝑲 ~ h , 2 = 𝑿 ^ ​ 𝑾 K ( 1 , 2 ) , \displaystyle\widetilde{\bm{Q}}_{h,1}=\hat{\bm{X}}\bm{W}_{Q}^{(1,h)},\quad\widetilde{\bm{Q}}_{h,2}=\bm{0},\qquad\widetilde{\bm{K}}_{h,1}=\hat{\bm{X}}\bm{W}_{K}^{(1,1)},\quad\widetilde{\bm{K}}_{h,2}=\hat{\bm{X}}\bm{W}_{K}^{(1,2)}, 𝑽 ~ h , 1 = 𝑿 ^ ​ 𝑾 V ( 1 , 1 ) , 𝑽 ~ h , 2 = 𝑿 ^ ​ 𝑾 V ( 1 , 2 ) . \displaystyle\widetilde{\bm{V}}_{h,1}=\hat{\bm{X}}\bm{W}_{V}^{(1,1)},\quad\widetilde{\bm{V}}_{h,2}=\hat{\bm{X}}\bm{W}_{V}^{(1,2)}.

[322] p: Stacking and attention (per head). New-IHA stacks pseudos row-wise:

[323] table: 𝑸 ¯ h = [ 𝑸 ~ h , 1 𝑸 ~ h , 2 ] , 𝑲 ¯ h = [ 𝑲 ~ h , 1 𝑲 ~ h , 2 ] , 𝑽 ¯ h = [ 𝑽 ~ h , 1 𝑽 ~ h , 2 ] . \overline{\bm{Q}}_{h}=\begin{bmatrix}\widetilde{\bm{Q}}_{h,1}\\ \widetilde{\bm{Q}}_{h,2}\end{bmatrix},\quad\overline{\bm{K}}_{h}=\begin{bmatrix}\widetilde{\bm{K}}_{h,1}\\ \widetilde{\bm{K}}_{h,2}\end{bmatrix},\quad\overline{\bm{V}}_{h}=\begin{bmatrix}\widetilde{\bm{V}}_{h,1}\\ \widetilde{\bm{V}}_{h,2}\end{bmatrix}.

[324] p: Let 𝑷 ¯ h = softmax ⁡ ( 𝑸 ¯ h ​ 𝑲 ¯ h ⊤ ) ​ 𝑽 ¯ h \overline{\bm{P}}_{h}=\mathrm{softmax}(\overline{\bm{Q}}_{h}\overline{\bm{K}}_{h}^{\top})\overline{\bm{V}}_{h} . If the softmax temperature is set to 0 0 , the attention reduces to hard attention induced by the permutation structure.

[325] p: Head h = 1 h=1 . Since 𝑸 ~ 1 , 1 = 𝑿 ^ ​ 𝑾 Q ( 1 , 1 ) \widetilde{\bm{Q}}_{1,1}=\hat{\bm{X}}\bm{W}_{Q}^{(1,1)} and the two pseudo-keys correspond to 𝑰 \bm{I} and 𝑷 \bm{P} , the first-pseudo output of head 1 1 (denoted 𝑷 1 , 1 \bm{P}_{1,1} ) takes the form

[326] table: 𝑷 1 , 1 \displaystyle\bm{P}_{1,1} = 2 ​ 𝑰 ⋅ ( 𝑿 ^ ​ 𝑾 V ( 1 , 1 ) ) + 2 ​ 𝑷 ⋅ ( 𝑿 ^ ​ 𝑾 V ( 1 , 2 ) ) . \displaystyle=2\,\bm{I}\cdot\big(\hat{\bm{X}}\bm{W}_{V}^{(1,1)}\big)\;+\;2\,\bm{P}\cdot\big(\hat{\bm{X}}\bm{W}_{V}^{(1,2)}\big).

[327] p: Compute the value projections:

[328] table: 𝑿 ^ ​ 𝑾 V ( 1 , 1 ) \displaystyle\hat{\bm{X}}\bm{W}_{V}^{(1,1)} = [ 2 0 4 0 6 0 8 0 ] 𝑿 ^ ​ 𝑾 V ( 1 , 2 ) = [ 0 2 0 4 0 6 0 8 ] . \displaystyle=\begin{bmatrix}2&0\\ 4&0\\ 6&0\\ 8&0\end{bmatrix}\qquad\hat{\bm{X}}\bm{W}_{V}^{(1,2)}=\begin{bmatrix}0&2\\ 0&4\\ 0&6\\ 0&8\end{bmatrix}.

[329] p: Thus,

[330] table: 𝑷 1 , 1 \displaystyle\bm{P}_{1,1} = 1 2 ​ 𝑰 ⋅ [ 2 0 4 0 6 0 8 ​ ` 0 ] + 1 2 ​ 𝑷 ⋅ [ 0 1 2 0 1 0 3 2 0 2 ] = [ 1 2 2 3 3 4 4 1 ] . \displaystyle=\frac{1}{2}\bm{I}\cdot\begin{bmatrix}2&0\\ 4&0\\ 6&0\\ 8`&0\end{bmatrix}+\frac{1}{2}\bm{P}\cdot\begin{bmatrix}0&\frac{1}{2}\\ 0&1\\ 0&\frac{3}{2}\\ 0&2\end{bmatrix}=\begin{bmatrix}1&2\\ 2&3\\ 3&4\\ 4&1\end{bmatrix}.

[331] p: Head h = 2 h=2 . Here 𝑸 ~ 2 , 1 = 𝑿 ^ ​ 𝑾 Q ( 1 , 2 ) \widetilde{\bm{Q}}_{2,1}=\hat{\bm{X}}\bm{W}_{Q}^{(1,2)} , so the induced shifts are 𝑷 2 \bm{P}^{2} and 𝑷 3 \bm{P}^{3} . Hence

[332] table: 𝑷 2 , 1 \displaystyle\bm{P}_{2,1} = 1 2 ​ 𝑷 2 ⋅ ( 𝑿 ^ ​ 𝑾 V ( 1 , 1 ) ) + 1 2 ​ 𝑷 3 ⋅ ( 𝑿 ^ ​ 𝑾 V ( 1 , 2 ) ) = [ 3 4 4 1 1 2 2 3 ] . \displaystyle=\frac{1}{2}\,\bm{P}^{2}\cdot\big(\hat{\bm{X}}\bm{W}_{V}^{(1,1)}\big)\;+\;\frac{1}{2}\,\bm{P}^{3}\cdot\big(\hat{\bm{X}}\bm{W}_{V}^{(1,2)}\big)=\begin{bmatrix}3&4\\ 4&1\\ 1&2\\ 2&3\end{bmatrix}.

[333] p: Collapse H ​ P → H HP\to H (select pseudo j = 1 j=1 ). New-IHA uses 𝑹 ∈ ℝ H × H ​ P \bm{R}\in\mathbb{R}^{H\times HP} . Choose 𝑹 \bm{R} to pick only pseudo j = 1 j=1 from each head:

[334] table: 𝑹 1 , 1 = 1 , 𝑹 2 , 3 = 1 , and all other entries are 0 , \bm{R}_{1,1}=1,\quad\bm{R}_{2,3}=1,\quad\text{and all other entries are }0,

[335] p: so that 𝑶 1 = 𝑷 1 , 1 \bm{O}_{1}=\bm{P}_{1,1} and 𝑶 2 = 𝑷 2 , 1 \bm{O}_{2}=\bm{P}_{2,1} .

[336] p: Concatenate heads. The representation after the attention layer is

[337] table: 𝑿 ^ ( 1 ) = [ 𝑶 1 , 𝑶 2 ] = [ 1 2 3 4 2 3 4 1 3 4 1 2 4 1 2 3 ] . \displaystyle\hat{\bm{X}}^{(1)}=[\bm{O}_{1},\bm{O}_{2}]=\begin{bmatrix}1&2&3&4\\ 2&3&4&1\\ 3&4&1&2\\ 4&1&2&3\end{bmatrix}.

[338] p: Thus each token position now contains all symbols in a fixed, known order (a cyclic listing), which allows the subsequent MLP to enumerate ordered pairs ( j 1 , j 2 ) (j_{1},j_{2}) , form x i + G ​ x j 1 + x j 2 x_{i}+Gx_{j_{1}}+x_{j_{2}} , apply the mod- M M test, and aggregate counts to compute CPM i ​ ( 3 ) \mathrm{CPM}_{i}(3) .

[339] h4: MHA.

[340] p: We now proceed with the MHA construction.

[341] h4: Encoder and Positional Encoding:

[342] p: The input to the network is a sequence of tokens where each token is a natural number. Concretely its defined as: { x i } i ∈ ℕ ∈ ℕ \{x_{i}\}_{i\in\mathbb{N}}\in\mathbb{N} . We assume the encoder and the positional encoding to be defined such that they output the following:

[343] table: 𝑿 ^ = [ 𝑿 , 𝑰 ] , \displaystyle\hat{\bm{X}}=[\,\bm{X},\;\bm{I}\,],

[344] p: where I I is the identity matrix used for positional encoding, and X X integer value of of the input symbol.

[345] table: 𝑿 ∈ ℝ N max × 1 , 𝑰 ∈ ℝ N max × N max , 𝑿 ^ ∈ ℝ N max × ( N max + 1 ) . \displaystyle\bm{X}\in\mathbb{R}^{N_{\mathrm{max}}\times 1},\qquad\bm{I}\in\mathbb{R}^{N_{\mathrm{max}}\times N_{\mathrm{max}}},\qquad\hat{\bm{X}}\in\mathbb{R}^{N_{\mathrm{max}}\times(N_{\mathrm{max}}+1)}.

[346] h4: Layer 1. (Attention)

[347] p: We provide the sketch of what the intended outcome of the first layer is via an example and then proceed with the construction.

[348] p: Main Idea. Similar to the prior construction, the goal of the first layer of attention is to able to permute all input symbols to obtain all the symbols in a sequence within a single vector space. For example, given an input sequence 1 2 3 1\quad 2\quad 3 , we obtain the following:

[349] table: Token 1: 1 2 3 \displaystyle 1\quad 2\quad 3 Token 2: 2 3 2 \displaystyle 2\quad 3\quad 2 Token 3: 3 1 2 . \displaystyle 3\quad 1\quad 2.

[350] p: This allows us to obtain all tokens that can then be used by the MLP to obtain all the permutations needed to solve the CPM-3 task. We first define the construction (the query, key and value matrices) in generality below and then describe an example below to make things concrete. Note that in the equation below, 𝑷 ∈ ℝ N max × N max \bm{P}\in\mathbb{R}^{N_{\mathrm{max}}\times N_{\mathrm{max}}} denotes a cyclic permutation matrix and 𝒆 1 = [ 1 , 𝟎 1 × N max ] T \bm{e}_{1}=[1,\bm{0}_{1\times N_{\mathrm{max}}}]^{T} . We first define the query matrices below.

[351] table: 𝑾 Q , MHA ( 1 , h ) = [ 𝟎 1 × N max 𝑷 ( h − 1 ) ] \displaystyle\bm{W}_{Q,\texttt{MHA}}^{(1,h)}=\begin{bmatrix}\bm{0}_{1\times N_{\mathrm{max}}}\\ \bm{P}^{(h-1)}\end{bmatrix}

[352] p: where, h ∈ { 1 , 2 , ⋯ , N max } h\in\{1,2,\cdots,N_{\mathrm{max}}\} . We now define the key matrices below.

[353] table: 𝑾 K , MHA ( 1 , h ) = [ 𝟎 1 × N max 𝑰 N max × N max ] , \displaystyle\bm{W}_{K,\texttt{MHA}}^{(1,h)}=\begin{bmatrix}\bm{0}_{1\times N_{\mathrm{max}}}\\ \bm{I}_{N_{\mathrm{max}}\times N_{\mathrm{max}}}\end{bmatrix},

[354] p: where, h ∈ { 1 , 2 , ⋯ , N max } h\in\{1,2,\cdots,N_{\mathrm{max}}\} . We now define the value matrices below.

[355] table: 𝑾 V , IHA ( 1 , h ) = [ 𝒆 𝟏 ] , \displaystyle\bm{W}_{V,\texttt{IHA}}^{(1,h)}=\begin{bmatrix}\bm{e_{1}}\end{bmatrix},

[356] p: where, h ∈ { 1 , 2 , 3 , ⋯ , N max } h\in\{1,2,3,\cdots,N_{\mathrm{max}}\} .

[357] p: Hence, basis this construction, if the temperature of softmax is set to 0 0 (leading to hard attention), one can obtain the following (Note that ⋅ | | ⋅ \cdot||\cdot denotes the concatenation operation), and X ^ ( 1 ) \hat{X}^{(1)} denote the representation after the first layer of IHA ,

[358] table: X ^ ( 1 ) \displaystyle\hat{X}^{(1)} = 𝑿 ^ ​ 𝑾 V , IHA ( 1 , 1 ) | | 𝑷 ​ 𝑿 ^ ​ 𝑾 V , IHA ( 1 , 2 ) | ​ | ⋯ | | 𝑷 ( N max − 1 ) ​ 𝑿 ^ ​ 𝑾 V , IHA ( 1 , N max ) \displaystyle=\bm{\hat{X}}\bm{W}_{V,\texttt{IHA}}^{(1,1)}\ ||\ \bm{P}\bm{\hat{X}}\bm{W}_{V,\texttt{IHA}}^{(1,2)}||\ \cdots\ ||\ \bm{P}^{(N_{\mathrm{max}}-1)}\bm{\hat{X}}\bm{W}_{V,\texttt{IHA}}^{(1,N_{\mathrm{max}})}

[359] h4: MLP.

[360] p: Note that X ^ ( 1 ) \hat{X}^{(1)} allows for having all the N max N_{\mathrm{max}} tokens in the same vector space. Then the MLP can be constructed as follows. The first layer can contain ⌈ N max ⌉ 2 × ( N max ) ​ ( N max − 1 ) \lceil N_{\mathrm{max}}\rceil^{2}\times(N_{\mathrm{max}})(N_{\mathrm{max}}-1) parameters where the first layer via the MLP is responsible for all P 2 N max {}^{N_{\mathrm{max}}}P_{2} permutations along with multiplications with the right token with G G . Furthermore, if the activation function after the first layer is defined as f ​ ( ⋅ ) = ReLU ​ ( 1 − ϕ ​ ( ⋅ ) ) f(\cdot)=\text{ReLU}(1-\phi(\cdot)) where ϕ ⁡ ( ⋅ ) \phi(\cdot) the modulo- M M operation, then the second linear layer is responsible solely for aggregating all the resulting counts. This aggregation can be implemented by a linear layer whose parameter matrix has dimension max 2 \max^{2} .

[361] h4: Total Parameter Count.

[362] p: Considering all the parameters described above, the total parameter count denoted by T MHA T_{\textbf{MHA}} is as follows:

[363] table: T MHA \displaystyle T_{\textbf{MHA}} = ( Query Parameters + Key Parameters ) + Value Parameters + MLP Parameters \displaystyle=(\text{Query Parameters}+\text{Key Parameters})+\text{Value Parameters}+\text{MLP Parameters} = 2 ​ N max 3 + N max 3 + ( N max + 1 ) ​ ( N max ) ​ ( N max − 1 ) + N max 2 \displaystyle=2N_{\mathrm{max}}^{3}+N_{\mathrm{max}}^{3}+(N_{\mathrm{max}}+1)(N_{\mathrm{max}})(N_{\mathrm{max}}-1)+N_{\mathrm{max}}^{2} > 3 ​ N max 3 + ( N max ) 2 ​ ( N max − 1 ) + N max 2 \displaystyle>3N_{\mathrm{max}}^{3}+(N_{\mathrm{max}})^{2}(N_{\mathrm{max}}-1)+N_{\mathrm{max}}^{2}

[364] p: ∎

[365] h2: Appendix C Compute and FLOP Matching for IHA

[366] h4: Global complexity.

[367] p: Let N N be the sequence length, d d the per-head dimension, H H the number of heads, and P P the number of pseudo-heads per head. Interleaving increases the effective sequence length from N N to N ​ P NP . A global IHA layer therefore has per-head complexity

[368] table: 𝒪 ⁡ ( ( N ​ P ) 2 ​ d ) \displaystyle\mathcal{O}\left((NP)^{2}d\right) = 𝒪 ⁡ ( P 2 ​ N 2 ​ d ) , \displaystyle=\mathcal{O}(P^{2}N^{2}d),

[369] p: which is a factor- P 2 P^{2} increase relative to global MHA. Accordingly, we FLOP-match all comparisons so that any improvements cannot be attributed to additional compute.

[370] h4: Hybrid local-global schedule.

[371] p: We use a local-global schedule: four layers apply sliding-window IHA with window size

[372] table: W ≔ N 2 ​ P 2 , \displaystyle W\coloneqq\frac{N}{2P^{2}},

[373] p: followed by one global-attention layer (a 4:1 ratio). In a sliding-window IHA layer, attention is computed over N ​ P NP query virtual tokens and W ​ P WP key virtual tokens, yielding per-layer cost

[374] table: 𝒪 ⁡ ( H ⋅ ( N ​ P ) ⋅ ( W ​ P ) ⋅ d ) \displaystyle\mathcal{O}\left(H\cdot(NP)\cdot(WP)\cdot d\right) = 𝒪 ⁡ ( H ⋅ N 2 ​ d 2 ) . \displaystyle=\mathcal{O}\left(H\cdot\frac{N^{2}d}{2}\right).

[375] p: Averaging four local layers with one global layer gives

[376] table: 4 ⋅ 𝒪 ⁡ ( H ​ N 2 ​ d / 2 ) + 𝒪 ⁡ ( H ​ N 2 ​ d ) 5 \displaystyle\frac{4\cdot\mathcal{O}(HN^{2}d/2)+\mathcal{O}(HN^{2}d)}{5} = 3 5 ​ 𝒪 ​ ( H ​ N 2 ​ d ) ≈ 𝒪 ⁡ ( H ​ N 2 ​ d ) , \displaystyle=\frac{3}{5}\mathcal{O}(HN^{2}d)\approx\mathcal{O}(HN^{2}d),

[377] p: which matches the global-attention baseline up to constant factors.

[378] h2: Appendix D Synthetic Reasoning Tasks

[379] p: In this section, we investigate whether different attention mechanisms, such as standard multi-head attention (MHA), interleaved head attention (IHA), and simplicial attention Roy and others [2025] , provide measurable improvements in compositional and multi-hop reasoning. Following the methodology of Kozachinskiy et al. [2025] , we isolate the contribution of the attention architecture using fully synthetic benchmarks with (i) ground-truth labels defined exactly by relational composition, (ii) a controlled input distribution, and (iii) dependencies that require aggregating evidence across multiple (and potentially distant) sequence positions. We describe the tasks next.

[380] h3: D.1 Data and Task Formulation

[381] p: We evaluate attention mechanisms on two synthetic multi-hop reasoning tasks derived from boolean matrix composition. Both tasks share a common input format: a random m × m m\times m boolean matrix R R , flattened into a sequence of m 2 m^{2} binary tokens (each 0 or 1). The model must predict, for every entry ( i , j ) (i,j) , whether the corresponding entry in the composed relation equals 1. This is a sequence-to-sequence binary classification problem, the input and output sequences are aligned position-wise, and training minimizes binary cross-entropy averaged over all valid positions.

[382] h4: Binary Relation Composition (2-hop).

[383] p: Given R R , the target is R ∘ R R\circ R , where

[384] table: ( R ∘ R ) i ​ j = 1 ​ iff ​ ∃ k ​ s.t. ​ R i ​ k = 1 ∧ R k ​ j = 1 . \displaystyle(R\circ R)_{ij}=1\;\;\text{iff}\;\;\exists\,k\;\;\text{s.t.}\;\;R_{ik}=1\;\land\;R_{kj}=1.

[385] p: This task asks whether entities i i and j j are connected by a directed path of length exactly 2 through the relation R R . The matrix size m m is sampled uniformly from { 6 , … , 10 } \{6,\ldots,10\} , yielding input sequences of length m 2 ∈ { 36 , … , 100 } m^{2}\in\{36,\ldots,100\} that vary across examples. Each entry of R R is drawn i.i.d. from Bernoulli ​ ( P ) \text{Bernoulli}(P) with P = 0.325 P=0.325 , a value chosen empirically to yield approximately balanced positive and negative labels in R ∘ R R\circ R .

[386] h4: Ternary Relation Composition (3-hop).

[387] p: Given R R , the target is R ∘ R ∘ R R\circ R\circ R , where

[388] table: ( R ∘ R ∘ R ) i ​ j = 1 ​ iff ​ ∃ k , l ​ s.t. ​ R i ​ k = 1 ∧ R k ​ l = 1 ∧ R l ​ j = 1 . \displaystyle(R\circ R\circ R)_{ij}=1\;\;\text{iff}\;\;\exists\,k,l\;\;\text{s.t.}\;\;R_{ik}=1\;\land\;R_{kl}=1\;\land\;R_{lj}=1.

[389] p: This task asks whether entities i i and j j are connected by a directed path of length exactly 3 through the relation R R . The matrix size m m is sampled uniformly from { 5 , … , 8 } \{5,\ldots,8\} , yielding input sequences of length m 2 ∈ { 25 , … , 64 } m^{2}\in\{25,\ldots,64\} that vary across examples. Each entry of R R is drawn i.i.d. from Bernoulli ​ ( P ) \text{Bernoulli}(P) with P = 0.264 P=0.264 : at higher values the 3-hop composition quickly saturates (outputs become nearly all ones), so we reduce both m m and P P to maintain approximately balanced positive and negative labels.

[390] h3: D.2 Dataset Construction

[391] p: Each task uses 40,000 training examples, 5,000 validation examples, and 5,000 test examples. Since m m varies across examples, sequence lengths within a split are non-uniform; sequences within a minibatch are padded on the right to the maximum length in that batch.

[392] h3: D.3 Hyperparameter Sweep and Training Protocol

[393] p: We evaluate multiple attention mechanisms including standard multi-head attention (MHA), interleaved head attention (IHA), and simplicial attention Roy and others [2025] . All models use a single attention layer ( L = 1 L=1 ) with 8 8 heads ( H = 8 H=8 ), and we sweep over two learning rates η ∈ { 10 − 3 , 10 − 4 } \eta\in\{10^{-3},10^{-4}\} . We use early stopping with a patience of 10 epochs. Note that for IHA, the number of pseudo, keys and values is 8 8 . In Fig. 3 , we report final test accuracy for each attention mechanism across the two learning rates. IHA consistently outperforms the other variants on both tasks and for both learning rates, achieving gains of up to 4.7 % 4.7\% on binary relation composition and 3.3 % 3.3\% on ternary relation composition relative to the strongest baseline, simplicial attention. For completeness, Fig. 4 and Fig. 5 also show training, validation, and test accuracy as a function of epochs for each attention mechanism.

[394] figure: (a) Binary composition: final test accuracy across learning rates. (b) Ternary composition: final test accuracy across learning rates. Figure 3 : Final test accuracy summaries for binary and ternary relation composition. Bars compare MHA, IHA, and simplicial attention under L = 1 L=1 , H = 8 H=8 , for η ∈ { 10 − 3 , 10 − 4 } \eta\in\{10^{-3},10^{-4}\} .

[395] figure: (a) Binary composition, η = 10 − 3 \eta=10^{-3} , L = 1 L=1 , H = 8 H=8 . (b) Binary composition, η = 10 − 4 \eta=10^{-4} , L = 1 L=1 , H = 8 H=8 . Figure 4 : Learning curves for Binary Relation Composition. Each panel shows train, validation, and test accuracy versus epoch for MHA, IHA, and simplicial attention under a one-layer, eight-head transformer.

[396] figure: (a) Ternary composition, η = 10 − 3 \eta=10^{-3} , L = 1 L=1 , H = 8 H=8 . (b) Ternary composition, η = 10 − 4 \eta=10^{-4} , L = 1 L=1 , H = 8 H=8 . Figure 5 : Learning curves for Ternary Relation Composition. Each panel shows train, validation, and test accuracy versus epoch for MHA, IHA, and simplicial attention under a one-layer, eight-head transformer.

[397] h2: Instructions for reporting errors

[398] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[399] p: Tip: You can select the relevant text first, to include it in your report.

[400] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[401] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
