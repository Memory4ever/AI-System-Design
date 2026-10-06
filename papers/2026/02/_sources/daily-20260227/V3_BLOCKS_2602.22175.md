[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: DySCO : Dynamic Attention-Scaling Decoding for Long-Context LMs

[3] h6: Abstract

[4] p: Understanding and reasoning over long contexts is a crucial capability for language models (LMs). Although recent models support increasingly long context windows, their accuracy often deteriorates as input length grows. In practice, models often struggle to keep attention aligned with the most relevant context throughout decoding. In this work, we propose DySCO , a novel decoding algorithm for improving long-context reasoning. DySCO leverages retrieval heads —a subset of attention heads specialized for long-context retrieval—to identify task-relevant tokens at each decoding step and explicitly up-weight them. By doing so, DySCO dynamically adjusts attention during generation to better utilize relevant context. The method is training-free and can be applied directly to any off-the-shelf LMs. Across multiple instruction-tuned and reasoning models, DySCO consistently improves performance on challenging long-context reasoning benchmarks, yielding relative gains of up to 25% on MRCR and LongBenchV2 at 128K context length with modest additional compute. Further analysis highlights the importance of both dynamic attention rescaling and retrieval-head-guided selection for the effectiveness of the method, while providing interpretability insights into decoding-time attention behavior. Our code is available at https://github.com/princeton-pli/DySCO .

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] p: Recent advances in language models (LMs) have enabled processing of extremely long context windows, unlocking applications such as repository-level code understanding and long-document question answering. Driven by improvements in data curation and transformer architectures, modern LMs now support context lengths of 128K tokens and beyond ( Gemini Team, 2025 ; Yang et al., 2025 ; Kimi Team, 2025 ; OpenAI, 2025 ; Anthropic, 2026 ) . However, model performance often degrades significantly as input length increases, even on simple tasks, commonly known as “context rot” ( Hong et al., 2025 ; Goldman et al., 2024 ) . As illustrated in Figure 1 , even on a simple Path Traversal task ( Ye et al., 2025 ) , models such as Qwen3-8B and Llama-3.1-8B see accuracy drop from around 60% at 4K tokens to below 20% at 16K tokens, despite supporting context lengths of up to 128K tokens.

[8] figure: Figure 1 : Top: An illustrative Path Traversal task (simplified). Solving the task requires dynamically locating relevant context during decoding. Bottom: Accuracy as a function of context length for models with and without DySCO . Despite the total context being only 16K tokens, both models exhibit severe performance degradation as context length increases.

[9] figure: Figure 2 : Overview of DySCO algorithm. At each decoding step, DySCO consists of three stages: (1) Aggregation : We run a partial forward pass over the input sequence to obtain attentions of retrieval heads, such as QRHead , and use them to assign relevance scores to context tokens; (2) Selection : We use the relevance scores to select the important tokens; (3) Rescaling : We up-weight the important tokens by intervening attention logits of all attention heads and run a full forward pass to sample the next token.

[10] p: We attribute this degradation to a key challenge in how LMs utilize long and information-dense contexts during genera- tion: effective long-context reasoning requires models to continuously focus attention on the most task-relevant parts of the context as the generation state evolves. In practice, however, vanilla decoding often fails to exhibit this behavior over long contexts. For example, in the Path Traversal task shown in Figure 1 , LMs must iteratively identify the next edge from the context based on the current node. Our analysis (§ 2.2 ) shows that attention is often insufficiently focused on the relevant context at each generation step, leading to errors even when the required information is present. In this work, we propose a novel decoding algorithm, DySCO ( Dy namic Attention- S caling De CO ding), which dynamically adjusts attention on the fly during generation. DySCO is lightweight, training-free, and directly applicable to off-the-shelf language models. DySCO operates exclusively at the decoding stage, after the long-context prefilling phase that accounts for the majority of computation. As a result, it introduces only modest additional overhead—for example, approximately 4% extra FLOPs when generating 8K tokens from 128K-token inputs.

[11] p: The key idea of DySCO is to identify relevant tokens at each decoding step using retrieval heads ( Wu et al., 2025a ; Zhang et al., 2025c ) , and then upweight attention to these tokens during generation. Retrieval heads are a specialized subset (1-2%) of attention heads that are responsible for long-context retrieval: compared to other heads, they assign higher and more stable attention to context that is critical for next-token prediction. Notably, we find that retrieval heads remain consistently focused on relevant tokens even when overall model performance degrades with increasing context length (§ 2.2 ). After prefilling, DySCO operates in three stages at each decoding step (Figure 2 ). 1) aggregation : we run a partial forward pass (§ 3.1 ) to aggregate attention scores from retrieval heads; 2) selection : we identify a small set of context tokens with the highest aggregated attention scores; 3) rescaling : we upweight attention to the selected tokens by intervening on the attention logits of all heads and run a full forward pass to generate the next token.

[12] p: DySCO introduces a new paradigm for attention shaping to improve long-context reasoning. Prior work on attention scaling focuses on long-context extension by uniformly scaling all attention logits by a constant factor ( Peng et al., 2024 ; Chen et al., 2026 ; Nakanishi, 2025 ) ; in contrast, DySCO performs dynamic, token-selective scaling at each decoding step, yielding substantial gains even within the model’s native context window. More broadly, most prior long-context inference methods, such as KV-cache eviction and compression ( Xiao et al., 2024 ; Li et al., 2024a ; Bhaskar et al., 2025 ) , prioritize efficiency and may degrade reasoning performance, while DySCO explicitly trades a small amount of additional compute for improved accuracy. Unlike higher-level scaffolding approaches such as agentic pipelines or external context-management systems ( Zhang et al., 2025a ; Yu et al., 2025 ; Wu et al., 2025b ) , DySCO operates directly at the attention level, is independent of any specific scaffold, and can be naturally combined with such systems.

[13] p: We evaluate DySCO across a diverse set of models, including both instruction-tuned and reasoning LMs, on a wide range of long-context tasks. DySCO consistently improves performance on challenging long-context reasoning benchmarks. Notably, for Qwen3-8B, DySCO delivers up to 25% relative improvements on MRCR and LongBenchV2 compared to YaRN alone, with ≤ \leq 4% additional FLOPs. Further analysis highlights the importance of both dynamic scaling and the use of retrieval heads for identifying important tokens.

[14] p: We summarize our contributions:

[15] p: We explore a new axis for long-context inference methods: improving accuracy rather than efficiency.

[16] p: We propose DySCO , a training-free decoding algorithm that yields strong gains on long-context reasoning tasks.

[17] p: We provide mechanistic insights into how retrieval heads can help mitigate long-context failures.

[18] h2: 2 Background and Motivation

[19] p: We first set up the preliminaries of retrieval heads ( Wu et al., 2025a ; Zhang et al., 2025c ) , an important building block of our approach (§ 2.1 ). We then study Path Traversal , a synthetic task designed to stress-test basic reasoning over long and information-dense context, and use it to reveal the connection between retrieval heads and long-context reasoning capabilities (§ 2.2 ).

[20] h3: 2.1 Preliminaries: Retrieval Heads

[21] p: We consider an autoregressive transformer LM ℳ \mathcal{M} ( Vaswani et al., 2017 ) that generates the next token x t + 1 x_{t+1} conditioned on the prefix x ≤ t x_{\leq t} , which includes both the input context and previously generated tokens. Let ℋ = { h i } \mathcal{H}=\{h_{i}\} denote the set of attention heads in ℳ \mathcal{M} . At decoding step t t , each head h ∈ ℋ h\in\mathcal{H} produces an attention distribution: 𝜶 t ( h ) ∈ ℝ t \boldsymbol{\alpha}_{t}^{(h)}\in\mathbb{R}^{t} , where α t , i ( h ) \alpha_{t,i}^{(h)} is the attention mass for token x i ∈ 𝒙 ≤ t x_{i}\in\boldsymbol{x}_{\leq t} .

[22] h4: Retrieval Heads.

[23] p: Wu et al. (2025a) discovered a universal set of attention heads that exhibit copy-like behavior during decoding, which they term retrieval heads . Concretely, when generating token x t x_{t} , a retrieval head h h concentrates its attention on a prior occurrence of the same token in the context. That is, α t , i ( h ) \alpha^{(h)}_{t,i} is high for some i < t i<t such that x i = x t x_{i}=x_{t} . These heads are typically sparse (less than 5% of all heads) and provide a mechanistic explanation for how language models perform explicit token lookup and copy-paste from long context.

[24] h4: Query-Focused Retrieval Heads ( QRHead ).

[25] p: Retrieval heads can be identified using different criteria: Wu et al. (2025a) rely on copy-paste behavior measured in synthetic retrieval tasks (e.g., Needle-in-a-Haystack). Zhang et al. (2025c) proposed QRHead , an improved approach that instead aggregates query-context attention mass across examples from realistic long-context tasks (e.g., long-form question answering). This yields a more semantic and task-aligned selection, which Zhang et al. (2025c) show to be more effective for long-context reasoning. We therefore adopt QRHead in this work; see Appendix A for details.

[26] h3: 2.2 Retrieval Heads Stay Focused on Relevant Context

[27] h4: Diagnostic task: Path Traversal .

[28] p: Long-context reasoning requires dynamically attending to relevant information at each decoding step, conditioned not only on the inputs but also on the intermediate state encoded in x ≤ t x_{\leq t} . To analyze this capability in a controlled setting, we use a synthetic task, Path Traversal ( Ye et al., 2025 ) .

[29] p: The input to Path Traversal consists of a long list of graph edges E = { ⟨ v i , v j ⟩ } E=\{\langle v_{i},v_{j}\rangle\} between nodes. The task is to find a path 𝒯 = ( ⟨ v start , v 1 ⟩ ​ … , ⟨ v t − 1 , v target ⟩ ) \mathcal{T}=(\langle v_{\text{start}},v_{1}\rangle\,\ldots,\langle v_{t-1},v_{\text{target}}\rangle) connecting a given start node to a target node. Crucially, the graph is designed in a way that each node along the gold path has exactly one outgoing edge. As a result, solving the task reduces to repeatedly identifying the next correct outgoing node and chaining them together. This constraint is explicitly stated in the prompt, ensuring a deterministic reasoning procedure. By varying the number of nodes, we can control the input length and construct tasks with different context sizes. See Appendix E for a full prompt example.

[30] h4: Severe performance degradation on Path Traversal .

[31] p: Specifically, we generate instances with approximately 4, 8, 16, and 32K tokens, corresponding to roughly 250, 500, 1000, and 2000 edges, respectively. LMs are required to find a path of 5 nodes (four edges). As shown in Figure 3 (left), although the task is structurally simple, model performance degrades rapidly as context length increases to 32K, well below the claimed context size, with step-level accuracy (correctness of each ⟨ v t − 1 , v t ⟩ \langle v_{t-1},v_{t}\rangle along the path) dropping from near-perfect to approximately 20%. Path Traversal thus isolates a central challenge of long-context reasoning: the need for repeated dynamic key-context lookup during decoding.

[32] h4: Behavior of retrieval heads.

[33] p: We further analyze the behavior of retrieval heads, which provides insight into LMs’ failure modes on long-context reasoning tasks. We partition the context into edge-level spans and compute the sum of attention mass assigned by QRHead to each span at every decoding step. Our analysis focuses on two metrics: 1) the fraction of decoding steps for which the gold edge (i.e., the next edge on the correct path) appears among the top 5% most-attended spans (Gold Edge in Top 5%). 2) the total attention mass assigned to the gold edge at each decoding step (Gold Attention). For this analysis (Figure 3 , middle and right), we only consider the second step (edge) among the four steps to explicitly study the attention dynamics occurring in the middle of the reasoning process.

[34] figure: Figure 3 : Left : Performance of Qwen3-8B on Path Traversal as context length increases. Middle : Fractions that the gold edge appear among the top-5% edges ranked by attention score (sum of attention over all tokens in the span) from QRHead versus random heads. Right : Attention mass assigned to gold edges by QRHead and random heads. Despite severe performance degradation and a reduction in attention mass on gold edges, QRHead consistently allocates substantially higher attention to the gold edges.

[35] p: We additionally include randomly selected attention heads as a baseline for comparison. As shown in Figure 3 (middle), retrieval head remain consistently aligned with the gold edge. Even as single-step prediction accuracy drops from over 90% to approximately 20% with increasing context length, retrieval head continue to rank the gold edge among the top 5% at most steps. At the same time, we observe a sharp decline in absolute attention to the gold edge , closely mirroring the overall performance degradation (see Figure 3 right). In contrast, random attention heads exhibit a much steeper drop in relative attention and much lower attention mass on gold spans.

[36] h4: Steering overall attention with retrieval heads.

[37] p: Our analysis find that QRHead consistently rank gold edges among the top-attended context spans and preserve strong relative retrieval signals (Figure 3 , middle). At the same time, as context length increases, the absolute attention mass assigned to gold spans decreases across all heads (including both QRHead and other heads) and task performance deteriorates (Figure 3 , right). This suggests that while QRHead continue to correctly identify relevant context, their signal becomes diluted within the overall attention distribution. Motivated by this observation, we investigate whether the relatively stable retrieval behavior of QRHead can be leveraged at decoding time to steer overall attention to better preserve focus on relevant context during generation.

[38] h2: 3 DySCO : Dynamic Attention Scaling

[39] h4: Overview

[40] p: We propose a novel decoding algorithm, DySCO , that improves long-context reasoning at inference time. The core idea of DySCO is to dynamically up-weight tokens in the context based on the attention distribution of retrieval heads during decoding. As shown in Figure 2 , each decoding step of DySCO contains three stages: 1) Aggregation : we run a partial forward pass over the input sequence to obtain the attention scores of QRHead and use them to compute context relevance scores for the current generation step; 2) Selection : we select the most important tokens based on the relevance scores; 3) Rescaling : we run a full forward pass in which we up-weight the attention logits of selected tokens across all attention heads.

[41] p: DySCO only modifies the decoding procedure and requires no training. It relies solely on attention scores produced by the model itself. These properties make DySCO highly flexible: it can be directly applied to off-the-shelf LMs without any architectural changes, and it is compatible with arbitrary inputs and tasks without task-specific preprocessing.

[42] figure: Algorithm 1 DySCO Input: LM ℳ \mathcal{M} with attention heads ℋ \mathcal{H} , QRHead heads ℋ ∗ \mathcal{H}^{*} , input 𝒙 ≤ T \boldsymbol{x}_{\leq T} , rescale strength β \beta , momentum γ \gamma , cumulative probability threshold p p (for token selection). Output: Generated sequence 𝒙 ≤ T ′ \boldsymbol{x}_{\leq T^{\prime}} 1: t ← T t\leftarrow T 2: 𝐫 T ← 𝐫 init \mathbf{r}_{T}\leftarrow\mathbf{r}_{\mathrm{init}} // Initialize Relevance 3: while not finished do 4: t ← t + 1 t\leftarrow t+1 5: (Aggregation) Run a partial forward pass to obtain attention logits from ℋ ∗ \mathcal{H}^{*} : 𝐚 t ( h ) \mathbf{a}_{t}^{(h)} for h ∈ ℋ ∗ h\in\mathcal{H}^{*} . 6: 𝐫 t ← 1 | ℋ ∗ | ​ ∑ h ∈ ℋ ∗ Softmax ⁡ ( 𝐚 t ( h ) ) \mathbf{r}_{t}\leftarrow\frac{1}{|\mathcal{H}^{*}|}\sum_{h\in\mathcal{H}^{*}}\mathrm{Softmax}(\mathbf{a}_{t}^{(h)}) 7: 𝐫 t ← γ ⋅ 𝐫 t − 1 + ( 1 − γ ) ⋅ 𝐫 t \mathbf{r}_{t}\leftarrow\gamma\cdot\mathbf{r}_{t-1}+(1-\gamma)\cdot\mathbf{r}_{t} // Apply Momentum 8: (Selection) 𝒙 * ← SelectTop ⁡ ( 𝒙 ≤ t , 𝐫 t , p ) \boldsymbol{x}^{\text{*}}\leftarrow\mathrm{SelectTop}(\boldsymbol{x}_{\leq t},\mathbf{r}_{t},p) // Select top- p p tokens 9: 𝐯 ⁡ [ i ] ← { log ⁡ ( β ) x i ∈ 𝒙 ∗ 0 otherwise \mathbf{v}[i]\leftarrow\begin{cases}\log(\beta)&x_{i}\in\boldsymbol{x}^{*}\\ 0&\text{otherwise}\end{cases} // Intervention 10: (Rescaling) 𝜶 ~ t ( h ) ← Softmax ⁡ ( 𝐚 t ( h ) + 𝐯 ) \tilde{\boldsymbol{\alpha}}_{t}^{(h)}\leftarrow\mathrm{Softmax}\!\left(\mathbf{a}_{t}^{(h)}+\mathbf{v}\right) for h ∈ ℋ h\in\mathcal{H} 11: ℓ t ← ℳ ⁡ ( 𝒙 ≤ t ∣ 𝜶 ~ t ) \ell_{t}\leftarrow\mathcal{M}(\boldsymbol{x}_{\leq t}\mid\tilde{\boldsymbol{\alpha}}_{t}) // Rescaled Forward 12: x t + 1 ∼ Softmax ⁡ ( ℓ t ) x_{t+1}\sim\mathrm{Softmax}(\ell_{t}) // Sampling next token 13: end while

[43] h3: 3.1 The DySCO Algorithm

[44] p: Algorithm ( 1 ) details the full procedure of DySCO . Given an LM ℳ \mathcal{M} with attention heads ℋ \mathcal{H} and a set of retrieval heads ( QRHead ) ℋ ∗ ⊂ ℋ \mathcal{H}^{*}\subset\mathcal{H} , we decode from an input sequence 𝒙 ≤ T \boldsymbol{x}_{\leq T} . At each decoding step t ≥ T + 1 t\geq T+1 , DySCO maintains context relevance scores 𝒓 = r 1 , … , r t \boldsymbol{r}=r_{1},...,r_{t} where each r i r_{i} denotes the relevance of each token x i x_{i} in the prefix 𝒙 ≤ t \boldsymbol{x}_{\leq t} for the current generation step. For clarity of presentation, we assume the relevance scores are properly initialized (line 2), and defer the details of initialization after we introduce the aggregation step. DySCO produces the next token in the following three stages:

[45] h4: Aggregation.

[46] p: We first perform a partial forward pass at decoding step t t , and extract the attention distributions of the selected QRHead heads. The forward pass is partial as we skip the forward pass over higher layers given that retrieval heads are primarily located in the middle layers (see § 3.2 for details). We then compute a relevance score over tokens in the prefix by averaging the attention scores across these heads: 𝐫 t = 1 | ℋ ∗ | ​ ∑ h ∈ ℋ ∗ 𝜶 t ( h ) \mathbf{r}_{t}\;=\;\frac{1}{|\mathcal{H}^{*}|}\sum_{h\in\mathcal{H}^{*}}\boldsymbol{\alpha}^{(h)}_{t} . where 𝜶 t ( h ) \boldsymbol{\alpha}^{(h)}_{t} is the attention distribution after softmax at step t t . To incorporate information from previous decoding steps, we maintain a moving average of the relevance scores with momentum γ ∈ [ 0 , 1 ) \gamma\in[0,1) :

[47] table: 𝐫 t ← γ ⋅ 𝐫 t − 1 + ( 1 − γ ) ⋅ 𝐫 t . \mathbf{r}_{t}\;\leftarrow\;\gamma\cdot\mathbf{r}_{t-1}+(1-\gamma)\cdot\mathbf{r}_{t}.

[48] p: Empirically, this momentum-based smoothing stabilizes the relevance estimates and makes DySCO more robust to hyperparameter variations.

[49] p: We note that at the first decoding step, we need to obtain an initial relevance score. We use a short warm-up window of length T w T_{w} , relying on the last T w T_{w} tokens of the input prompt to initialize the relevance distribution. Specifically, for the first decoding step T T , we compute:

[50] table: 𝐫 T = Normalize ⁡ ( ∑ d = 0 T w − 1 γ d ⋅ 𝜶 T − d ℋ ∗ ) , \mathbf{r}_{T}\;=\;\mathrm{Normalize}\!\left(\sum_{d=0}^{T_{w}-1}\gamma^{d}\cdot\boldsymbol{\alpha}^{\mathcal{H}^{*}}_{T-d}\right),

[51] p: where 𝜶 T − d ℋ ∗ = 1 | ℋ ∗ | ​ ∑ h ∈ ℋ ∗ 𝜶 T − d ( h ) \boldsymbol{\alpha}^{\mathcal{H}^{*}}_{T-d}=\frac{1}{|\mathcal{H}^{*}|}\sum_{h\in\mathcal{H}^{*}}\boldsymbol{\alpha}^{(h)}_{T-d} is the averaged attention of QRHead at time T − d T-d , and norm ⁡ ( ⋅ ) \mathrm{norm}(\cdot) rescales the scores to form a valid distribution. We do not tune γ \gamma or T w T_{w} , and fix them to γ = 0.75 \gamma=0.75 and T w = 16 T_{w}=16 in all experiments.

[52] h4: Selection.

[53] p: At each decoding step t t , we use the relevance distribution to estimate the importance of context tokens in the prefix 𝒙 ≤ t \boldsymbol{x}_{\leq t} . Based on this distribution, we select a subset of relevant tokens 𝒙 ∗ ∈ 𝒙 ≤ t \boldsymbol{x}^{*}\in\boldsymbol{x}_{\leq t} . Our selection strategy follows nucleus (top- p p ) sampling ( Holtzman et al., 2020 ) used for LM decoding, but is applied over relevance scores rather than next-token probabilities. Specifically, we rank tokens in 𝒙 ≤ t \boldsymbol{x}_{\leq t} by their relevance scores and retain the smallest set of tokens whose cumulative relevance mass exceeds a threshold p p , while additionally enforcing a maximum of K K (8192) tokens to avoid overly large number of selected tokens.

[54] p: In practice, we find performance to be robust to moderate variations in parameters. In all experiments, we determine these parameters using a validation set of fully synthetic tasks, and directly use the resulting parameters on diverse downstream datasets without further tuning (§ 4.1 ). Concretely, we set top- p p to be 0.95 or 0.975.

[55] h4: Rescaling.

[56] p: Given the selected relevant tokens 𝒙 ∗ \boldsymbol{x}^{*} , we intervene on the attention computation to up-weight the selected tokens by modifying the attention logits. Concretely, for each layer and each attention head, we compute an intervention vector of bias terms added to the attention logits. The bias is log ⁡ β \log\beta for the selected tokens, and 0 0 otherwise, where β > 1 \beta>1 is the rescale strength factor:

[57] table: 𝐯 ⁡ [ i ] = log ⁡ ( β ) ​ if ​ x i ∈ 𝒙 ∗ , else ​ 0 \mathbf{v}[i]=\log(\beta)\;\;\text{if }x_{i}\in\boldsymbol{x}^{*},\text{ else }0

[58] p: Then, we add the intervention vector to the attention logits 𝐚 t ( h ) \mathbf{a}_{t}^{(h)} of all attention heads h ∈ ℋ h\in\mathcal{H} before the softmax operation, and obtain rescaled attention distributions 𝜶 ~ t ( h ) \tilde{\boldsymbol{\alpha}}_{t}^{(h)} . We apply the intervention to all heads to propagate the relevance signal identified by QRHead throughout the model’s attention computation.

[59] table: 𝜶 ~ t ( h ) = Softmax ⁡ ( 𝐚 t ( h ) + 𝐯 ) ​ for ​ h ∈ ℋ \tilde{\boldsymbol{\alpha}}_{t}^{(h)}=\mathrm{Softmax}\!\left(\mathbf{a}_{t}^{(h)}+\mathbf{v}\right)\text{ for }h\in\mathcal{H}

[60] p: This intervention effectively rescales the pre-softmax attention logits by β \beta . Finally, we perform a full forward pass with the modified attention logits across all layers, and the next token x t + 1 x_{t+1} is sampled or selected from the output distribution produced by this rescaled forward pass. Importantly, this procedure operates entirely at inference time and does not require any modification to model parameters.

[61] h3: 3.2 Efficient Implementation

[62] h4: Early stopping of attention aggregation.

[63] p: We describe our design that makes DySCO more efficient. Prior work shows that attention heads responsible for retrieval and reasoning tend to concentrate in the middle layers of transformer models ( Wu et al., 2025a ; Zhao et al., 2025 ) . For instance, for Qwen3-8B (36 layers), QRHead are distributed between 17 − - 20 layers. Hence, we early-stop attention aggregation during the partial forward pass and only collect QRHead attention up to the middle layers of the model, rather than across all layers. With early stopping, this adds approximately 60 % 60\% extra computation per decoding step .

[64] h4: Overhead analysis.

[65] p: As mentioned above, the attention aggregation stage introduces an additional partial forward pass during decoding, but no additional cost during prefilling. As a result, the total FLOP overhead of DySCO remains small for long-context workloads, where computation is dominated by the quadratic-cost prefilling pass over the input context. To make this concrete, consider a setting with a 128K-token input context. Following Hoffmann et al. (2022) , our estimate of the FLOPs is that generating 4K and 8K output tokens accounts for roughly 3.2 % 3.2\% and 6.4 % 6.4\% of the prefilling FLOPs, respectively. When using DySCO , the additional partial decoding pass increases the total computation by only about 2.0 % 2.0\% and 3.8 % 3.8\% relative to prefilling for these two settings.

[66] h2: 4 Experiments

[67] p: We test the effectiveness of DySCO on a diverse array of long-context reasoning tasks.

[68] h3: 4.1 Models and Baselines

[69] h4: Models.

[70] p: We experiment with multiple open-weight LMs from two families, including Qwen3-4B, 8B, and 32B of Qwen3 family ( Yang et al., 2025 ) , and Llama-3.1-8B-Instruct ( Llama-3 Team, 2024 ) . Qwen3-8B and Qwen3-4B support thinking mode that uses long CoT ( Guo et al., 2025 ) , and Llama-3-8B-Instruct can use chain-of-thought (CoT) prompting ( Wei et al., 2022 ) .

[71] h4: Head selection.

[72] p: We directly use the set of QRHead ( Zhang et al., 2025c ) from the official implementation across all experiments. We note that these heads are detected on Natural Questions ( Kwiatkowski et al., ) and applied directly across all tasks evaluated in this paper, demonstrating strong cross-task transfer.

[73] h4: Baselines.

[74] p: Our approach operates on the decoding process for improving long-context reasoning. We compare against baselines that directly operate on decoding, including:

[75] p: 1) Vanilla , standard decoding without alteration.

[76] p: 2) YaRN ( Peng et al., 2024 ) , which is designed for context extension by modifying rotary position embeddings ( Su et al., 2024 ) at inference time. YaRN primarily targets extending the usable context window of pretrained models, rather than improving long-context reasoning accuracy.

[77] p: 3) Uniform Attention Scaling ( UniAttnS ) . Prior work has shown that sharpening attention distributions can improve long-context extrapolation ( Peng et al., 2024 ; Chen et al., 2026 ; Nakanishi, 2025 ) . Concretely, this is achieved by applying a temperature τ ∈ ( 0 , 1 ] \tau\in(0,1] to rescale attention logits, i.e., 𝐚 ′ = 𝐚 / τ \mathbf{a}^{\prime}=\mathbf{a}/\tau , where 𝐚 \mathbf{a} denotes the original attention logits. Following this line of work, we adopt length-dependent attention temperature scaling, using different values of τ \tau for different input lengths. While prior approaches typically scale attention with a factor that grows linearly with log ⁡ n \log n , we instead tune τ \tau separately for each context length. Importantly, UniAttnS rescales attention logits uniformly across all tokens, whereas DySCO selectively up-weights step-relevant tokens at each decoding step.

[78] p: Both UniAttnS and DySCO can be combined with YaRN.

[79] h4: Setting parameters for DySCO and UniAttnS .

[80] p: DySCO and UniAttnS both require setting additional parameters for controlling the decoding. We use MRCR ( Vodrahalli et al., 2024 ) (Multi-Round Coreference Resolution) as a development dataset for deciding hyperparameters. We use MRCR as it is a fully synthetically generated dataset, which makes it less biased for a particular real-world dataset. For each model, we pick one set of parameters for length span (0,64K) and one set of parameters for length span (64K, 128K) using performance on MRCR, and we directly apply the same set of parameters on other datasets. We include more details in Appendix B .

[81] figure: Table 1 : Performance across different context lengths with Uniform Attention Scaling ( UniAttnS ) and DySCO . Path Traversal 4K 8K 16K 32K Qwen3-32B 80 67 32 21 + UniAttnS 82 68 40 19 + DySCO 79 71 46 33 Qwen3-8B 57 45 19 1 + UniAttnS 59 46 25 2 + DySCO 65 51 33 2

[82] h3: 4.2 Diagnostic Test on Path Traversal

[83] p: We first use Path Traversal to evaluate whether reshaping attention with DySCO or UniAttnS helps LMs maintain focus on relevant context at each decoding step. We do not include YaRN in this setting, as the maximum input length (32K) is well within the supported context window of the evaluated models. Results are reported in Table 1 . As shown, DySCO yields consistent performance improvements across context lengths. UniAttnS also leads to measurable gains for Qwen3-8B at 4K and 32K input lengths, though the improvements are smaller and less consistent. These results suggest that attention sharpening alone can yield modest improvements, whereas explicitly up-weighting important tokens identified by QRHead leads to substantially larger gains.

[84] figure: Figure 4 : Performance on MRCR , LongBenchV2 , and Clipper . DySCO substantially outperforms vanilla decoding, and UniAttnS . YaRN is applied to Qwen models at 128K context length, but not to Llama-3.1-8B-Instruct, which natively supports 128K.

[85] h3: 4.3 Long Context Reasoning Tasks (with CoT)

[86] p: We now evaluate DySCO on the primary focus of this paper, improving multi-step CoT reasoning over long context.

[87] h4: Datasets.

[88] p: We use 3 datasets with natural texts and enable LMs to use CoT as follows:

[89] p: 1) MRCR ( Vodrahalli et al., 2024 ) requires LMs to retrieve a conversation following a query from a list of highly similar conversations. The task is introduced to test LMs’ direct recall. To allow LMs to use CoT, we activate thinking mode (4096-token budget) for Qwen3 models. We do not evaluate Llama models in this setting, as they do not support long CoT (direct recall results are reported in § 4.4 ).

[90] p: 2) LongBenchV2 ( Bai et al., 2025 ) requires multi-step reasoning over realistic long contexts spanning diverse domains. We use a subset of data points with input length ranging from 0-128K (264 data points). For Qwen models, we enable thinking mode with a maximum of 10,240 tokens to accommodate the difficulty; for Llama models, we apply CoT prompting from Bai et al. (2025) .

[91] p: 3) Clipper ( Pham et al., 2025 ) evaluates claim verification over full-length books. The model is given a complete book (90–128K tokens) along with a claim to verify, requiring multi-step reasoning over evidence distributed throughout the text. We include this dataset because it provides a native CoT prompting template, which is well-suited for evaluating instruction-tuned models (Llama-3.1-8B-Instruct). We follow the original experimental setup and response template from Pham et al. (2025) .

[92] h4: Settings.

[93] p: We use YaRN (factor 4.0) for Qwen3 models to extend their context window from 32K to 128K, following the recommendation in Yang et al. (2025) . For 128K-context experiments, both UniAttnS and DySCO are applied on top of YaRN. We use the recommended generation configurations for Qwen models. For Llama models with explicit CoT prompting, we use greedy decoding.

[94] h4: Results.

[95] p: As shown in Figure 4 , DySCO improves CoT reasoning under long-context settings across model families, benchmarks, and context lengths. At 128K context length, DySCO (with YaRN) improves Qwen3-8B by 3.5 absolute points (22% relative) on MRCR , 8.2 points (29%) on LongBenchV2 , and 2.5 points (10%) on Clipper compared to YaRN alone.

[96] p: While UniAttnS yields gains in some cases (e.g., a 7.2% improvement for Qwen3-8B on LongBenchV2 at 64K), these improvements are not consistent across datasets or context lengths. In contrast, DySCO provides larger and more stable gains, particularly at longer context lengths, and consistently outperforms UniAttnS across all benchmarks.

[97] figure: Table 2 : Performance on long-context recall tasks with 128K input length. We apply YaRN for Qwen models. MRCR Hotpot InfMC InfQA Avg 128K 128K 128K 128K 128K Qwen3-4B + YaRN 16.7 37 50 27.1 32.7 + UniAttnS 18.4 34 39 24.1 28.9 + DySCO 19.0 39 54 31.3 35.8 Qwen3-8B + YaRN 16.7 61 61 39.6 44.6 + UniAttnS 17.5 58 63 39.7 44.6 + DySCO 19.5 58 65 39.2 45.4 Qwen3-32B + YaRN 24.4 51 79 48.7 50.8 + UniAttnS 24.2 51 78 48.6 50.5 + DySCO 25.3 53 77 48.7 51.0 Llama-3.1-8B-Inst. 17.2 46 61 37.1 40.3 + UniAttnS 18.9 51 56 35.7 40.4 + DySCO 18.6 52 62 38.4 42.8

[98] h3: 4.4 Long Context Recall Tasks

[99] p: We next evaluate DySCO on long-context recall tasks, which primarily follow a needle-in-the-haystack setup ( Kamradt, 2023 ) . For these tasks, models directly produce the final answer without using CoT (we turn off thinking for Qwen models).

[100] h4: Datasets.

[101] p: We evaluate MRCR under its intended direct-answering setup (directly outputting the final response). Additionally, we consider the following tasks: HotpotQA ( Yang et al., 2018 ) , QA and multiple-choice tasks from InfBench ( Zhang et al., 2024a ) . For Hotpot and InfBench, we use the processed versions released in HELMET ( Yen et al., 2025 ) , and evaluate all tasks with a context length setting of 128K tokens.

[102] h4: Results.

[103] p: Table 2 reports performance on these long-context recall tasks. As shown, DySCO is also able to improve model accuracy in long-context recall. For example, with Llama-3.1-8B-Instruct, DySCO increases HotpotQA accuracy from 46 to 52, and InfQA accuracy from 37.1 to 38.4. While UniAttnS yields modest gains on MRCR, it also degrades performance in several other cases. Notably, these recall tasks require only very short outputs (typically tens of tokens), and DySCO introduces negligible additional overhead compared to vanilla decoding.

[104] h3: 4.5 Comparison with RAG and Prompt Compression

[105] figure: Figure 5 : Comparison between DySCO , RAG (Stella), LongLLMLingua, and vanilla decoding. For RAG and LongLLMLingua, we report the results after reducing the context to different length (4K, 8K, and 16K tokens).

[106] p: We compare our decoding-time approach with methods that reduce the effective context length via external scaffolding. Specifically, we consider two representative classes of approaches: (1) Retrieval-Augmented Generation (RAG) to select the most relevant portions of the input context given a query; and (2) Prompt compression methods, which explicitly rewrite or prune the input prompt to fit within a shorter token budget. For RAG, we use Stella ( Zhang et al., 2025b ) as the dense retriever. For prompt compression, we evaluate LongLLMLingua ( Jiang et al., 2024b ) , which uses an auxiliary LM to compress long prompts while preserving task-relevant information.

[107] p: Unlike these methods, which require auxiliary components, DySCO operates purely at decoding time on the original input. We evaluate RAG and LongLLMLingua on LongBenchV2 , reducing the effective context length to { 4 , 8 , 16 } \{4,8,16\} K tokens, and compare against our DySCO . Full details are provided in Appendix D .

[108] h4: Results.

[109] p: Figure 5 summarizes the results. Overall, DySCO outperforms both RAG and LongLingua on Qwen3-8B (Think), and achieves performance comparable to these baselines on Llama-3.1-8B. As both models have undergone substantial post-training and already exhibit strong long-context capabilities, neither RAG nor LongLingua yields consistent improvements on LongBenchV2 when the input context length is within 64K tokens. In contrast, DySCO continues to improve performance in this regime. When the context length increases to 128K tokens, RAG-based systems begin to outperform vanilla decoding. However, they still lag behind DySCO on Qwen3-8B.

[110] h2: 5 Analysis & Ablations

[111] figure: Figure 6 : Performance of Qwen3-8B on MRCR and LongBenchV2 at 64K and 128K under four decoding settings: direct answer vs. Think, with vanilla decoding or DySCO . DySCO yields larger gains when combined with CoT.

[112] h3: 5.1 Impact of CoT Reasoning and Context Length

[113] p: DySCO dynamically focuses on key context as generation progresses, making it naturally compatible with CoT, where different reasoning steps rely on different parts of the context. We analyze the interaction between DySCO and CoT across varying context lengths. We evaluate DySCO and vanilla decoding with and without CoT on MRCR and LongBenchV2 at 64K and 128K context lengths, under four decoding settings (direct answer vs. CoT, each with vanilla decoding or DySCO ). We report the results for Qwen3-8B.

[114] h4: Interplay between DySCO and CoT reasoning.

[115] p: Figure 6 summarizes the results. Overall, DySCO yields larger benefits when combined with CoT reasoning . On MRCR , which primarily evaluates long-context recall, DySCO improves performance in both the direct-answer and CoT settings, with larger gains when CoT is enabled. On LongBenchV2 , which emphasizes multi-step reasoning over long contexts, DySCO substantially improves performance in the CoT setting, while causing only minor degradation when CoT is disabled. We hypothesize that this occurs because LongBenchV2 is inherently reasoning-intensive, and disabling CoT limits the model’s ability to capitalize on improved attention to relevant context.

[116] h4: Impact of context length.

[117] p: We find that the interaction between CoT reasoning and decoding strategy depends on input length. Under vanilla decoding, CoT outperforms direct answering at 64K context length, but not at longer context lengths (128K). However, DySCO reverses this trend at 128K: when combined with CoT reasoning, DySCO substantially improves performance at longer input lengths , where direct-answer decoding is comparatively weaker. By dynamically rescaling attention, DySCO restores effective long-context reasoning at 128K input length.

[118] h3: 5.2 Ablations

[119] figure: Table 3 : Ablations of DySCO on head selection and dynamic rescaling with Qwen3-8B. DySCO consistently outperforms its variants with random attention heads and with static scaling. Task MRCR 64K LongBV2 64K Path 16K InfMC 128K Think Yes No Yes No No Vanilla 24.8 24.8 43.4 19 61 DySCO 27.3 26.3 51.2 33 66 w/ RandomHead 26.6 24.2 47.0 20 63 w/ StaticScaling 22.5 23.1 47.5 23 64

[120] h4: Ablation: Importance of head selection.

[121] p: We compare DySCO instantiated with QRHead against a variant that uses randomly selected heads. Both variants use 16 heads. Table 3 reports results on multiple datasets with Qwen3-8B. DySCO with random heads can outperform vanilla decoding on some tasks, since random heads may still capture weak retrieval signals (§ 2.2 ). Using QRHead consistently yields the best results across all settings, highlighting the advantage of more reliable relevance signals.

[122] h4: Ablation: Importance of dynamic rescaling.

[123] p: We further ablate the role of dynamic rescaling by comparing DySCO with a static rescaling variant. Static rescaling applies attention reweighting to a fixed set of context tokens, selected during an initial warm-up stage, and reuses this set throughout decoding. Conceptually, static rescaling can be viewed as an adaptation of KV-cache eviction methods that avoids explicit context pruning, as it relies on similar criteria for identifying important tokens (e.g., SnapKV).

[124] p: As shown in Table 3 , static rescaling yields improvements on recall tasks (e.g., InfMC), but it consistently underperforms dynamic rescaling. This gap highlights the importance of dynamic rescaling in DySCO , as the set of relevant tokens can shift substantially over the course of generation.

[125] h4: Hyperparameter robustness.

[126] p: We examine the robustness of DySCO to variations of its hyperparameters. DySCO shows consistent performance across reasonable choices of hyperparameters. Full results are provided in Appendix C .

[127] h2: 6 Related Work

[128] h4: Improving long-context LMs.

[129] p: The need for better support of long context has motivated extensive research across multiple dimensions, including architectural designs ( Gu & Dao, 2024 ; Lieber et al., 2024 ; Peng et al., 2023 ; Xiao et al., 2023 ; Bertsch et al., 2023 ; Jin et al., 2024 ; Yen et al., 2024 ) , data engineering strategies ( Xiong et al., 2023 ; An et al., 2024 ; Gao et al., 2024b ; Hu et al., 2024 ; Fu et al., 2024 ; Chen et al., 2025a ; Gao et al., 2025 ; Bai et al., 2024 ; Chen et al., 2025b ) , context window extension techniques ( Peng et al., 2024 ; Chen et al., 2024b ; Chen et al., 2023 ; Zhu et al., 2024 ) , evaluation benchmarks ( Yen et al., 2025 ; Ye et al., 2025 ; Bai et al., 2023 ; Bai et al., 2025 ; Liu et al., 2024 ; Wu et al., 2024 ; Hsieh et al., 2024 ; Wang et al., 2024 ) , and analyses of long-context behavior and failure modes ( Wu et al., 2025a ; Zhao et al., 2025 ; Goldman et al., 2024 ; Liu et al., 2023 ; Gao et al., 2024a ; Yin et al., 2024 ) . Most existing approaches improve long-context performance by modifying model parameters, architectures, or training data, whereas our work improves the decoding procedure.

[130] h4: Long-context inference techniques.

[131] p: One line of work studies inference-time techniques for long context, primarily focusing on improving efficiency. Representative approaches include streaming inference ( Xiao et al., 2024 ; Zhang et al., 2023 ) , KV cache eviction or compression ( Xu et al., 2024 ; Li et al., 2024a ; Cai et al., 2024 ; Corallo & Papotti, 2024 ; Kim et al., 2024 ) , and sparse attention mechanisms ( Xu et al., 2025 ; Jiang et al., 2024a ; Xiao et al., 2025 ) . These methods trade off accuracy for computational or memory efficiency. In contrast, DySCO is explicitly designed to improve accuracy under long context. Recent work has also explored inference-time accuracy improvements by training on input context at test time ( Bansal et al., 2025 ; Chen et al., 2025c ) , whereas our approach requires no additional training and can be directly applied to off-the-shelf models. Most closely related to our approach, prior work has used attention scaling ( Peng et al., 2024 ; Nakanishi, 2025 ; Chen et al., 2026 ; Puvvada et al., 2025 ) , which applies a global rescaling factor to all attention logits to reshape the overall distribution. In contrast, DySCO performs selective rescaling and up-weights attention to task-relevant tokens, enabling more targeted and effective improvements in long-context reasoning.

[132] h4: Scaffolding and external systems for long context.

[133] p: Another line of work builds external scaffolding around LMs. This includes RAG ( Zhao et al., 2024b ; Li et al., 2024b ) , prompt compression modules ( Jiang et al., 2024b ; Wu et al., 2025b ) , recursive or multi-stage LM calls ( Zhang et al., 2025a ) , memory systems ( Chen et al., 2024a ) , and agentic frameworks ( Zhang et al., 2024b ; Zhao et al., 2024a ) . DySCO directly improves the LM’s internal attention behavior during decoding, without introducing additional scaffolding, and can be integrated with any scaffolding.

[134] h2: 7 Conclusion

[135] p: In this work, we have presented DySCO , a training-free decoding algorithm that improves long-context reasoning. DySCO leverages retrieval heads to dynamically identify relevant context tokens at each decoding step and intervenes on attention logits to up-weight their attention across heads. Across multiple instruct and reasoning LMs, DySCO consistently improves accuracy on challenging long-context benchmarks while incurring modest extra FLOPs. Our analyses further indicate that long-context failures are associated with degraded focus on relevant context, and that dynamic attention scaling can mitigate this issue. Overall, DySCO provides an inference-time approach for improving long-context accuracy and offers insight into the mechanisms underlying long-context failures in LMs.

[136] h2: Acknowledgments

[137] p: This work is gratefully supported by an NSF CAREER award (IIS-2239290). Howard Yen is supported by the William A. Dippel’ 50 * 55 Graduate Fellowship.

[138] h2: References

[139] h2: Appendix A Additional Details on Query-Focused Retrieval Heads ( QRHead ).

[140] p: Original retrieval heads are identified through strict copy behavior, which overlooks more general semantic retrieval. To address this limitation, Zhang et al. (2025c) propose Query-Focused Retrieval Heads (QRHeads), which generalize retrieval behavior to query-conditioned context lookup.

[141] p: Specifically, consider a long-context QA setting in which the input consists of a query q q and a large context containing one gold document d ∗ d^{*} (the “needle”) along with many distractor documents. Zhang et al. (2025c) define a query-context retrieval score (QRScore) for each attention head h h as:

[142] table: QRScore ⁡ ( h ) = ∑ i ∈ q ∑ j ∈ d ∗ α i , j ( h ) , \mathrm{QRScore}(h)=\sum_{i\in q}\sum_{j\in d^{*}}\alpha^{(h)}_{i,j},

[143] p: where α i , j ( h ) \alpha^{(h)}_{i,j} denotes the attention weight from query token i i to context token j j under head h h . Heads are ranked by their QRScore, and the top- K K heads (typically 1 1 – 2 % 2\% of all attention heads) are selected as QRHeads.

[144] p: Unlike original retrieval heads, QRHeads capture semantic context lookup rather than exact token copying. Prior work shows that attention from QRHeads is more effective for retrieving relevant information from long contexts across tasks and domains ( Zhang et al., 2025c ) .

[145] h2: Appendix B Parameter Selection for DySCO and UniAttnS

[146] p: Our method performs inference-time attention scaling to improve long-context accuracy. Both DySCO and the baseline UniAttnS introduce a small number of inference-time hyperparameters. Here, we describe 1) how these parameters are selected, and 2) the robustness of DySCO to reasonable variations around the chosen defaults.

[147] h3: B.1 Choosing Parameters for DySCO

[148] p: We select hyperparameters using MRCR , a fully synthetic long-context recall benchmark. We choose MRCR for parameter tuning for two main reasons: 1) it is synthetically generated and therefore does not risk data contamination with real-world evaluation benchmarks, and 2) its context length is configurable, allowing controlled analysis across different lengths. Importantly, for each model, we fix a single set of hyper-parameters and apply it uniformly across all downstream tasks.

[149] p: For Qwen models, we distinguish between two context-length settings. For inputs up to 64 64 K tokens, we use the native context window without extrapolation. For 64 64 – 128 128 K tokens, we use YaRN-based extrapolation, which globally changes the attention computation. As a result, we select parameters separately for the 0 0 – 64 64 K and 64 64 – 128 128 K settings, using MRCR - 64 64 K and MRCR - 128 128 K, respectively. Within each length span, a single parameter configuration is shared across all tasks.

[150] h4: Hyperparameters.

[151] p: We perform a small grid search on MRCR over the following values:

[152] table: p ∈ { 0.95 , 0.975 } , K ∈ { 4096 , 8192 } , β ∈ { 2.0 , 2.5 , 3.0 } . p\in\{0.95,0.975\},\quad K\in\{4096,8192\},\quad\beta\in\{2.0,2.5,3.0\}.

[153] p: When multiple configurations yield comparable performance, we prefer less aggressive settings—specifically, larger p p , smaller β \beta , and smaller K K —as they intervene more conservatively on the attention distribution.

[154] p: The parameter choices used throughout the paper are summarized below:

[155] table: Model / Length 𝒑 \boldsymbol{p} 𝑲 \boldsymbol{K} 𝜷 \boldsymbol{\beta} Qwen3-4B (0–64K) 0.975 4096 2.0 Qwen3-4B + YaRN (64–128K) 0.95 8192 2.5 Qwen3-8B (0–64K) 0.975 4096 2.0 Qwen3-8B + YaRN (64–128K) 0.975 8192 2.5 Qwen3-32B (0–64K) 0.975 4096 2.0 Qwen3-32B + YaRN (64–128K) 0.95 8192 2.5 LLaMA-3.1-8B (0–128K) 0.975 4096 2.0

[156] p: We observe that models within the same family exhibit consistent optimal configurations. For example, all Qwen models without extrapolation favor ( K = 4096 , β = 2.0 ) (K=4096,\beta=2.0) , while Qwen models with YaRN consistently favor ( K = 8192 , β = 2.5 ) (K=8192,\beta=2.5) .

[157] h3: B.2 Choosing Parameters for UniAttnS

[158] p: We select the temperature parameter τ \tau for UniAttnS using the same MRCR -based protocol. We search over τ ∈ { 0.975 , 0.95 , 0.9 , 0.85 } \tau\in\{0.975,0.95,0.9,0.85\} . Due to differences in attention sharpness across model families and scales, the optimal τ \tau varies slightly:

[159] table: τ = 0.95 ​ for Qwen3-4B , τ = 0.975 ​ for Qwen3-8B , τ = 0.975 ​ for Qwen3-32B , τ = 0.9 ​ for LLaMA . \tau=0.95\text{ for Qwen3-4B},\quad\tau=0.975\text{ for Qwen3-8B},\quad\tau=0.975\text{ for Qwen3-32B},\quad\tau=0.9\text{ for LLaMA}.

[160] p: These values are fixed across all tasks and context lengths for each model.

[161] h2: Appendix C Robustness to Hyperparameter Variations

[162] figure: Table 4 : Evaluation of hyperparameter robustness of DySCO with Qwen3-8B. DySCO is robust to modest variations in the rescale strength β \beta , selection constraint K K , and selection threshold p p . p p K K 𝜷 \boldsymbol{\beta} MRCR LongBenchV2 Vanilla – – – 16.1 28.6 Default 0.975 8192 2.5 19.6 36.8 Vary p p 0.95 0.95 8192 2.5 18.4 31.7 Varying K K 2048 0.975 2048 2.5 19.6 38.0 4096 0.975 4096 2.5 19.0 32.7 Varying β \beta 3.0 0.975 8192 3.0 18.5 36.8 3.5 0.975 8192 3.5 18.1 31.7

[163] p: We evaluate the robustness of DySCO to hyperparameter variations on MRCR -128K and LongBenchV2 -128K using Qwen3-8B. We vary one hyperparameter at a time while fixing the others to the default configuration.

[164] p: Table 4 shows that DySCO consistently outperforms vanilla decoding across all tested settings . While more aggressive configurations (e.g., β = 3.5 \beta=3.5 ) lead to smaller gains, they still outperform the vanilla baseline.

[165] p: Importantly, we observe a strong correspondence between performance on MRCR and LongBenchV2 : hyperparameters that perform well on the synthetic MRCR benchmark also tend to yield strong improvements on LongBenchV2 . This trend indicates that the effects of hyperparameter choices are consistent across tasks, and that parameters selected on a synthetic long-context benchmark generalize well to more realistic long-context reasoning tasks.

[166] h2: Appendix D Detailed Setup for Retrieval-Augmented Generation and Prompt Compression

[167] p: In § 4.5 , we compare our decoding-time approach with methods that reduce the effective context length via external scaffolding. Specifically, we consider two representative classes of approaches: (1) Retrieval-Augmented Generation (RAG), which employs a dense retriever to select the most relevant portions of the input context given a query; and (2) Prompt compression methods, which explicitly rewrite or prune the input prompt to fit within a shorter token budget. In particular, we evaluate LongLLMLingua ( Jiang et al., 2024b ) , which uses an auxiliary LM to compress long prompts while attempting to preserve task-relevant information.

[168] p: Both RAG and prompt compression methods are less flexible than DySCO . They require additional system components (e.g., external retrievers or compression models) and rely on explicit partitioning of the input into instruction, context, and query segments. In contrast, DySCO operates purely at decoding time on the original input sequence, without modifying the prompt or introducing any external scaffolding.

[169] p: We evaluate DySCO , RAG, and LongLLMLingua on the challenging long-context reasoning benchmark LongBenchV2 . We do not include benchmarks such as MRCR and InfBench, which are specifically designed to stress-test long-context processing and are largely solvable by RAG-style designs.

[170] h4: Setup.

[171] p: For RAG, we adopt a strong dense retriever, Stella-1.5B-V5 ( Zhang et al., 2025b ) . Following Bai et al. (2025) , we apply a chunk-and-concatenate strategy to reduce the context length. Specifically, we first partition the original long context into chunks of 1024 tokens. Given a query, Stella V5 retrieves the top- 4 , 8 , 16 {4,8,16} most relevant chunks, which are then concatenated in their original order, resulting in shortened contexts of 4K, 8K, and 16K tokens. For LongLLMLingua, we use the official implementation released by Jiang et al. (2024b) . We partition the input prompt into context and question components, set the target compressed length to 4 ​ K , 8 ​ K , 16 ​ K {4\text{K},8\text{K},16\text{K}} tokens, and feed the compressed prompt to the model for decoding.

[172] h2: Appendix E Prompt Example for Path Traversal Task

[173] h2: Instructions for reporting errors

[174] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[175] p: Tip: You can select the relevant text first, to include it in your report.

[176] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[177] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
