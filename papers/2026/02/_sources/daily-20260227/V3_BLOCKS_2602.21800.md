[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: An Evaluation of Context Length Extrapolation in Long Code via Positional Embeddings and Efficient Attention

[3] h6: Abstract.

[4] p: The rapid advancement of large language models (LLMs) has led to a significant increase in automated tools in the software engineering, capable of performing various code-related tasks such as code generation, completion, and translation. Despite these advancements, its effectiveness is constrained by fixed context lengths, limiting its ability to generalize across long, domain-specific code sequences. To address this challenge, we investigate zero-shot, inference-only methods aimed at improving position encodings and optimizing attention mechanisms. Our goal is to provide a thorough analysis of current approaches that facilitate context length extrapolation in code, particularly in the context of long code completion tasks.

[5] h6: Keywords:

[6] h2: 1. Introduction

[7] p: The rise of large language models (LLMs) like LLaMA-2 ( GenAI, 2023 ) , Codestral ( Mistral AI team, 2024 ) , and CodeLLaMA ( Roziere et al., 2023 ) has significantly changed the landscape of software engineering tasks with a considerable dependence on them for the development of various automated tools. More specifically, there is a noticeable trend towards using LLMs to assist developers in various programming activities like source code generation ( Liu et al., 2024 ) and completion ( Ding et al., 2024 ) , code translation ( Pan et al., 2024 ) , and legacy code understanding and explanation ( Bhattacharya and Gupta, 2024 ; Bhattacharya et al., 2023 ) .

[8] p: Transformer-based LLMs are potent tools for understanding and generating source code. However, they are pre-trained with fixed context lengths, which limits their ability to perform length extrapolation during inference ( Press et al., 2022 ; Sun et al., 2022 ) . This constraint poses a particular challenge when working with lengthy, domain-specific codebases, necessitating the effective extrapolation strategies.

[9] p: In the literature, there are approaches to address the challenge of handling long sequences in LLMs via task-specific fine-tuning and pre-training on extensive datasets ( Xiong et al., 2023 ; Chen et al., 2023 ; Chen et al., 2024 ; Peng et al., 2024 ; Wang et al., 2024 ) . However, these methods are resource-intensive and risk over-fitting, which can lead to decreased performance on shorter sequences. In contrast, training-free methods that employ windowed attention mechanisms ( Xiao et al., 2024 ; Han et al., 2024 ; Ding et al., 2023 ) , have been proposed. These methods often rely on local information and may overlook long-range dependencies. An alternative cost-effective approach for addressing this challenge is prompt compression which aims to preserve essential information by shortening prompts ( Jiang et al., 2023a ; Jiang et al., 2023b ; Li et al., 2023 ) . However, the suitability of these approaches might be very limited for code datasets, which are characterized by inherent dependencies between code data points for logical understanding. This makes prompt compression an unsuitable solution for code datasets.

[10] p: In addition, a set of cost-effective, inference-only methods include hardware-aware techniques to mitigate these challenges. Dao et al. (2022) introduced the Flash Attention mechanism, which parallelizes the sequential processing of long documents by dividing the sequence into smaller blocks. Another approach proposed by Kwon et al. (2023) addresses the memory-intensive caching mechanism of key-value pairs for long documents handling during auto-regressive decoding. However, all these inference-only methods have primarily been investigated on plain long text documents.

[11] p: This raises a pressing and pragmatic research question: Do training-free, inference-only methods possess the capability to adequately handle long code sequences, which inherently require a deep understanding of syntactical and hierarchical structures? Thus, we perform a comparative analysis of inference-only approaches, focusing on positional extrapolation and efficient attention mechanisms. These approaches seek to tackle the challenges of context length extrapolation in long source codes, where structural information is crucial for LLMs.

[12] h4: Our Contributions :

[13] p: To summarize, the following are the main contributions in this work.

[14] p: We present a comparative analysis of inference-only methods, focusing on positional extrapolation and efficient attention mechanisms to study context length extrapolation in LLMs using long code completion tasks.

[15] p: The empirical results demonstrate that how much these techniques are effective in handling long code sequences while preserving essential syntactical and hierarchical information which is crucial for code understanding.

[16] h2: 2. Related Work

[17] p: This study primarily focuses on length extrapolation in transformer-based language models applied to source code datasets. We categorize our study into two distinct classes of the approaches to address the context length extrapolation problem:

[18] h4: Positional Encoding Based Methods :

[19] p: Length extrapolation in transformers is closely tied to word positions. Vaswani et al. (2017) introduced sinusoidal positional encodings (PEs) to handle this, a method widely used for enhancing length extrapolation ( Neishi and Yoshinaga, 2019 ; Press et al., 2022 ; Ruoss et al., 2023 ) . Improving position encoding is thus crucial for enabling transformers to handle long documents. Later trainable PEs ( Chen et al., 2021 ) , relative PEs ( Shaw et al., 2018 ) , Rotary PEs (RoPE) ( Su et al., 2024a ) , ALiBi ( Press et al., 2022 ) , xPOS ( Sun et al., 2022 ) , and CLEX ( Chen et al., 2024 ) , propose novel approaches for positional representation. Additionally, techniques like dynamic scaling, NTK-aware scaling ( Tancik et al., 2020 ) , and ReRoPE ( Su, 2023 ) further extend the model’s capacity for length extrapolation.

[20] h4: Efficient Attention Based Technique :

[21] p: LLMs are intrinsically restricted by narrow context windows, which hinders their ability to effectively incorporate or leverage the complete information present in lengthy sequences. Training-free attention sinks ( Xiao et al., 2024 ) , a framework designed to handle very long sequences by maintaining key tokens throughout processing, thus preventing the model from losing essential information. Winata et al. (2020) transformed each of the three matrices of self-attention mechanism into smaller matrices. Unlike traditional methods such as singular value decomposition, Saragadam et al. (2024) uses a DNN to learn an optimal regularizer for tensor decomposition when the distributions of the tensor are non-Gaussian.

[22] p: The generation of long sequential tokens results in a workload that is bound by memory, consequently restricting the utilization of GPUs and overall throughput. To overcome this limitation, PagedAttention ( Kwon et al., 2023 ) utilizes a strategy inspired by virtual memory, which involves segmenting 𝐊𝐕 \mathbf{KV} caches into blocks to tackle issues related to internal and external fragmentation problem while autoregressive generation. On the other hand, Flash-Decoding ( Dao et al., 2023 ) enhances the acceleration of attention by introducing parallelization in the sequence length of keys and values, resulting in a significant improvement of up to 8 × 8\times in generation speed for long sequences.

[23] p: The primary distinction is that current inference-only methods for context length extrapolation concentrate on plain text. In contrast, we perform a thorough comparative analysis using long code completion tasks, with the goal of identifying a generalized context length extrapolation technique applicable to long source code datasets.

[24] h2: 3. Context Length Extrapolation for Code

[25] figure: Figure 1. Comparison of length extrapolation techniques for code completion, categorized into Positional Encoding Based (e.g., RoPE, ReRoPE) and Efficient Attention Based methods (e.g., StreamingLLM, Paged Attention, Flash Attention). These approaches address the challenges of handling long code sequences in Transformer models.

[26] p: In this section, we define the problem of context extrapolation for long code within the framework of a long code completion task, framing it as a masked token prediction challenge. In addition, we present the detailed explanations of various methods that we investigate for addressing the context length length extrapolation through the long code completion task.

[27] h4: Problem Definition :

[28] p: Given an incomplete source code sequence S = { s 1 , s 2 , … , s t } S=\{s_{1},s_{2},\ldots,s_{t}\} , where s i s_{i} represents the i i -th token of the code, the objective is to generate the subsequent tokens S ^ t + 1 : t + k \hat{S}_{t+1:t+k} that complete the next line of the code. The generation of these tokens is conditioned on the previous context. Mathematically it can be formulated as follows:

[29] table: (1) S ^ t + 1 : t + k = arg max S t + 1 : t + k P θ ( S t + 1 : t + k ∣ S ) \hat{S}_{t+1:t+k}=\arg\max_{S_{t+1:t+k}}P_{\theta}(S_{t+1:t+k}\mid S)

[30] p: where P θ ( S t + 1 : t + k ∣ S ) P_{\theta}(S_{t+1:t+k}\mid S) denotes the posterior probability distribution over the possible sequences S t + 1 : t + k S_{t+1:t+k} given the context S S . The goal is to find the sequence of tokens that maximizes this posterior probability, thereby predicting the most likely continuation of the code sequence.

[31] p: We categorize the length extrapolation methods into two different categories i.e., positional encoding based methods and effective attention based methods which can be useful to handle the long code data as depicted in the Figure 1 .

[32] h3: 3.1. Positional Encoding Based Methods

[33] p: The sinusoidal positional encoding is a crucial component in transformer based models, enabling them to capture the order of input tokens ( Vaswani et al., 2017 ) . However, the traditional positional encoding scheme produces a constant periodic structure that fails to generalize beyond the sequence lengths observed during training, resulting in suboptimal performance when extrapolating ( Chi et al., 2024 ) .

[34] p: To alleviate this, relative positional encoding was introduced, which mainly incorporates the positions by capturing the relative distances between tokens rather than their absolute positions ( Shaw et al., 2018 ) . Although this approach helps to improve the transformer model to generalize its performance on unseen data instances by focusing on the relative distances. But even this approach cannot capture the long range dependencies while dealing with long data instances due to its primary dependencies on local context ( Chen, 2021 ) .

[35] h4: Rotary Positional Encoding (RoPE) :

[36] p: In contrast to sinusoidal and relative positional encodings, Su et al. (2024b) proposed Rotary Positional Encoding (RoPE) to overcome their limitations. RoPE applies a rotation matrix to token embeddings, capturing both relative and absolute positional information. Formally speaking, for a token 𝒙 i \bm{x}_{i} at position i i , RoPE can be defined as follows:

[37] table: (2) 𝒙 i ′ = RoPE ​ ( 𝒙 i , i ) = 𝒙 i ⋅ 𝑹 ⁡ ( θ i ) , \bm{x}_{i}^{\prime}=\text{RoPE}(\bm{x}_{i},i)=\bm{x}_{i}\cdot\bm{R}(\theta_{i}),

[38] p: where 𝑹 ⁡ ( θ i ) \bm{R}(\theta_{i}) is a rotation matrix dependent on the position i i and a learnable parameter θ i \theta_{i} . The rotation matrix 𝑹 ⁡ ( θ i ) \bm{R}(\theta_{i}) can be formulated as follows:

[39] table: (3) 𝑹 ⁡ ( θ i ) = ( cos ⁡ ( θ i ) − sin ⁡ ( θ i ) sin ⁡ ( θ i ) cos ⁡ ( θ i ) ) . \bm{R}(\theta_{i})=\begin{pmatrix}\cos(\theta_{i})&-\sin(\theta_{i})\\ \sin(\theta_{i})&\cos(\theta_{i})\end{pmatrix}.

[40] p: In contrast to sinusoidal and relative positional encodings, RoPE effectively captures both short- and long-range dependencies by preserving the angular information of token positions. This characteristic is thought to enhance the model’s ability to extrapolate context lengths.

[41] h4: Rectified Rotary Positional Encoding (ReRoPE) :

[42] p: RoPE outperforms the traditional positional encoding approaches by capturing both relative and absolute positional information through a rotation matrix. However, after a certain length static 𝐑 ⁡ ( θ ) \mathbf{R}(\theta) cannot scale well to encode the positional information ( emozilla, 2023 ) . To address this, Su (2023) proposed an inference-only solution (ReRoPE) that leverages the pre-trained knowledge of LLMs. ReRoPE introduces a post-processing optimization technique to extend the capabilities of RoPE by employing an attention scores based sliding window mechanism. This approach balances extrapolation of position encodings, enabling the model to handle much longer sequences smoothly.

[43] p: More specifically speaking, for token positions i i and j j within the sliding window w w (i.e., | i − j | < w |i-j|<w ), the attention score α i , j ReRoPE \alpha_{i,j}^{\text{ReRoPE}} is computed as follows:

[44] table: (4) α i , j ReRoPE = ( 𝐑 ⁡ ( θ i ) ​ 𝐪 i ) ⊤ ​ ( 𝐑 ⁡ ( θ j ) ​ 𝐤 j ) , \alpha_{i,j}^{\text{ReRoPE}}=\left(\mathbf{R}(\theta_{i})\mathbf{q}_{i}\right)^{\top}\left(\mathbf{R}(\theta_{j})\mathbf{k}_{j}\right),

[45] p: where 𝐑 ⁡ ( θ i ) \mathbf{R}(\theta_{i}) and 𝐑 ⁡ ( θ j ) \mathbf{R}(\theta_{j}) are the rotation matrices corresponding to positions i i and j j , respectively. For token positions i i and j j outside the sliding window w w (i.e., | i − j | ≥ w |i-j|\geq w ), the attention score α i , j LeakyReRoPE \alpha_{i,j}^{\text{LeakyReRoPE}} is computed differently, using a scaling factor k k to adjust the increase distance:

[46] table: (5) α i , j LeakyReRoPE = ( 𝐑 ⁡ ( θ i ) ​ 𝐪 i ) ⊤ ​ ( 𝐑 ⁡ ( θ j k ) ​ 𝐤 j ) , \alpha_{i,j}^{\text{LeakyReRoPE}}=\left(\mathbf{R}(\theta_{i})\mathbf{q}_{i}\right)^{\top}\left(\mathbf{R}\left(\frac{\theta_{j}}{k}\right)\mathbf{k}_{j}\right),

[47] p: where 𝐑 ⁡ ( θ j k ) \mathbf{R}\left(\frac{\theta_{j}}{k}\right) represents the scaled rotation matrix for the position j j . The scaling factor k k effectively reduces the distance lies outside the window, ensuring that the attention mechanism can extrapolate effectively. The final attention score α i , j \alpha_{i,j} is then computed by combining the scores from within and outside the window:

[48] table: (6) α i , j = { α i , j ReRoPE , if ​ | i − j | < w , α i , j LeakyReRoPE , if ​ | i − j | ≥ w . \alpha_{i,j}=\begin{cases}\alpha_{i,j}^{\text{ReRoPE}},&\text{if }|i-j|<w,\\ \alpha_{i,j}^{\text{LeakyReRoPE}},&\text{if }|i-j|\geq w.\end{cases}

[49] h3: 3.2. Efficient Attention Based Technique

[50] p: Although RoPE and ReRoPE mitigate some limitations of traditional positional encodings, they do not completely overcome the challenges posed by extreme length extrapolation scenarios. In such cases, effective attention-based approaches could prove beneficial.

[51] h4: Streaming LLM :

[52] p: The main concept focuses on overcoming the limitations of traditional attention mechanisms through the introduction of two key components: attention sinks and Rolling Key-Value (KV) Cache. In the StreamingLLM ( Xiao et al., 2024 ) , the key-value cache is segmented into two parts: a rolling KV cache that retains the most recent tokens, and attention sinks that preserve the KV pairs of the initial tokens. This innovative strategy effectively maintains consistent performance while processing long documents by training within a finite attention window, enabling it to handle contexts of infinite length.

[53] p: Let 𝐊 sink \mathbf{K}_{\text{sink}} and 𝐕 sink \mathbf{V}_{\text{sink}} denote the KV pairs for the attention sinks, and 𝐊 roll \mathbf{K}_{\text{roll}} and 𝐕 roll \mathbf{V}_{\text{roll}} denote the KV pairs in the rolling cache. The modified attention (StrmAttn) computation is as follows:

[54] table: (7) StrmAttn \displaystyle\text{StrmAttn} = Softmax ​ ( 𝐐 t ​ [ 𝐊 sink , 𝐊 roll ] ⊤ d k ) \displaystyle=\text{Softmax}\left(\frac{\mathbf{Q}_{t}\left[\mathbf{K}_{\text{sink}},\mathbf{K}_{\text{roll}}\right]^{\top}}{\sqrt{d_{k}}}\right) × [ 𝐕 sink , 𝐕 roll ] , \displaystyle\times\left[\mathbf{V}_{\text{sink}},\mathbf{V}_{\text{roll}}\right],

[55] p: where [ 𝐊 sink , 𝐊 roll ] \left[\mathbf{K}_{\text{sink}},\mathbf{K}_{\text{roll}}\right] and [ 𝐕 sink , 𝐕 roll ] \left[\mathbf{V}_{\text{sink}},\mathbf{V}_{\text{roll}}\right] represent the concatenation of the KV pairs from the attention sinks and the rolling cache, respectively.

[56] h4: Paged Attention :

[57] p: PagedAttention ( Kwon et al., 2023 ) is designed to address the limitations of traditional attention mechanisms, particularly in managing memory efficiently while processing long sequences in LLMs. In general, traditional self-attention mechanism stores the key-value pair (KV) in a contiguous memory block, which leads to a very problem of effictive memory management such as internal and external fragmentation. To alleviate this challenge, Paged Attention propose a novel blockwise KV caching mechanism to store KV pair in non-contiguous fashion. Let 𝐊 j = ( 𝐤 ( j − 1 ) ​ B + 1 , … , 𝐤 j ​ B ) \mathbf{K}_{j}=(\mathbf{k}_{(j-1)B+1},\ldots,\mathbf{k}_{jB}) and 𝐕 j = ( 𝐯 ( j − 1 ) ​ B + 1 , … , 𝐯 j ​ B ) \mathbf{V}_{j}=(\mathbf{v}_{(j-1)B+1},\ldots,\mathbf{v}_{jB}) represent the key and value blocks, respectively. The attention computation in Paged Attention is performed in a block-wise manner as follows:

[58] table: (8) A i ​ j = exp ⁡ ( 𝐪 i ⊤ ​ 𝐊 j / d k ) ∑ t = 1 ⌈ i / B ⌉ exp ⁡ ( 𝐪 i ⊤ ​ 𝐊 t / d k ) , A_{ij}=\frac{\exp(\mathbf{q}_{i}^{\top}\mathbf{K}_{j}/\sqrt{d_{k}})}{\sum_{t=1}^{\lceil i/B\rceil}\exp(\mathbf{q}_{i}^{\top}\mathbf{K}_{t}/\sqrt{d_{k}})},

[59] p: where A i ​ j = ( a i , ( j − 1 ) ​ B + 1 , … , a i , j ​ B ) A_{ij}=(a_{i,(j-1)B+1},\ldots,a_{i,jB}) represents the attention scores for the j j -th KV block. The final attention output 𝐨 i \mathbf{o}_{i} is then computed as:

[60] table: (9) 𝐨 i = ∑ j = 1 ⌈ i / B ⌉ 𝐕 j ​ A i ​ j ⊤ . \mathbf{o}_{i}=\sum_{j=1}^{\lceil i/B\rceil}\mathbf{V}_{j}A_{ij}^{\top}.

[61] p: By storing KV blocks in a non-contiguous fashion, Paged Attention allows the system to dynamically allocate memory as per requirement, reducing memory waste and improving the model’s ability to perform extrapolation.

[62] h4: Flash Attention :

[63] p: Flash Attention optimizes both memory and computational complexity in attention mechanisms, especially for long sequences, by minimizing memory accesses to GPU High Bandwidth Memory (HBM) using a tiling strategy and recomputation. Flash Attention partitions input matrices 𝐐 , 𝐊 , 𝐕 ∈ ℝ N × d \mathbf{Q},\mathbf{K},\mathbf{V}\in\mathbb{R}^{N\times d} into smaller blocks, loaded into faster SRAM. The attention scores for each block are computed as follows:

[64] table: (10) 𝐒 i , j = 𝐐 i ​ 𝐊 j ⊤ , \mathbf{S}_{i,j}=\mathbf{Q}_{i}\mathbf{K}_{j}^{\top},

[65] p: where 𝐒 i , j \mathbf{S}_{i,j} is the score matrix for blocks i i and j j . The softmax is then computed:

[66] table: (11) 𝐏 i , j = softmax ​ ( 𝐒 i , j ) , \mathbf{P}_{i,j}=\text{softmax}(\mathbf{S}_{i,j}),

[67] p: and the final attention output is:

[68] table: (12) 𝐎 i = ∑ j 𝐏 i , j ​ 𝐕 j . \mathbf{O}_{i}=\sum_{j}\mathbf{P}_{i,j}\mathbf{V}_{j}.

[69] p: By keeping only small blocks in SRAM and avoiding large intermediate matrices, FlashAttention handles longer sequences efficiently.

[70] h2: 4. Experimental Setup

[71] p: In this section, we provide an overview of the dataset employed in our experiments. We then elaborate the various RoPE-based LLMs investigated, along with their specific configurations, to assess their capacity in processing long code sequences.

[72] h3: 4.1. Dataset Description

[73] p: The dataset used for this study, derived from Guo et al. (2023) , provides a comprehensive benchmark for evaluating the ability of models to handle long code sequences across three programming languages: Python, Csharp, and Java. Long code completion entails generating missing or incomplete segments of source code based on provided context, making it a significant challenge in software engineering. This task is complex due to the necessity of ensuring both syntactical correctness and semantic coherence over extensive contexts that can encompass hundreds or even thousands of tokens. The difficulty is further heightened in programming languages with rigid syntax and hierarchical structures, such as Csharp and Java, compared to more flexible languages like Python.

[74] p: The dataset statistics, summarized in Table 1 , provide insights into the average sequence lengths and their quartile distributions. Python exhibits the longest average sequence length at 3158 tokens, followed closely by Csharp at 3101 tokens and Java at 3057 tokens. All three languages share a 25% quartile value of 3000 tokens, indicating that the shortest 25% of sequences are of comparable lengths. However, variances arise in the median (50%) and 75% quartiles. Python’s median sequence length is slightly longer at 3207 tokens, compared to Csharp’s 3189 tokens and Java’s 3134 tokens. The 75% quartile values further highlight this trend, with Python at 3802 tokens, Csharp at 3715 tokens, and Java at 3632 tokens. These findings suggest that while handling long sequences presents challenges for all three languages, Python’s longer sequences may necessitate improved extrapolation capabilities to preserve syntactical and structural integrity.

[75] figure: Language Average Length 25% Quartile 50% Quartile 75% Quartile Python 3158 3000 3207 3802 Csharp 3101 3000 3189 3715 Java 3057 3000 3134 3632 Table 1. Dataset statistics for code completion tasks across three programming languages: Python, Csharp, and Java. The “25% Quartile" indicates that 25% of the code sequences in the dataset have a length shorter than the reported value. The “50% Quartile," also known as the median, is the midpoint, where half of the code sequences are shorter, and half are longer. The “75% Quartile" marks the point below which 75% of the code sequences fall, representing the upper quartile.

[76] h3: 4.2. Large Language Models (LLMs)

[77] p: Similar to Zhang et al. (2024a) , we have considered RoPE-based LLMs such as LLaMA-2 (7B) ( Touvron et al., 2023 ) , Sheared-LLaMA (1.3B) ( Xia et al., 2024 ) , TinyLlama (1.1B) ( Zhang et al., 2024b ) , Vicuna (7B) ( Chiang et al., 2023 ) to conduct zero-shot inference in a low-resource scenario. The detailed model statistics is presented in Table 2 .

[78] figure: LLaMA-2 ShearedLLaMA TinyLLaMA Vicuna Para. 7B 1.3B 1.1B 7B 𝐋 pretrain \mathbf{L}_{\textbf{pretrain}} 4096 4096 2048 2048 Vocab Size 32000 32000 32000 32000 Hidden Size 4096 2048 2048 4096 Table 2. Model statistics for various investigated Large Language Models (LLMs) used in code completion tasks. The table compares LLaMA-2, ShearedLLaMA, TinyLLaMA, and Vicuna across several parameters, including the number of parameters (Para.), the maximum pretraining sequence length ( L p ​ r ​ e ​ t ​ r ​ a ​ i ​ n L_{pretrain} ), vocabulary size, and hidden size.

[79] h3: 4.3. Parameter Settings

[80] p: For ReRoPE experiment, to apply the sliding window mechanism in long code completion task, we set the window size ( w = 512 w=512 ). We keep rest of the hyper parameters as mentioned in the corresponding works. Additionally, we use greedy decoding strategy to generate next 100 tokens for the long code completion task.

[81] h3: 4.4. Evaluation Metrics

[82] p: The evaluation of models in this study is based on two key metrics: Exact Match (EM) and Edit Similarity (Edit Sim) , as outlined by Guo et al. (2023) . The EM metric calculates the percentage of predictions that perfectly align with the ground truth sequence. This serves as a stringent evaluation criterion, where even small discrepancies, such as the omission of a single character or token, lead to a mismatch. While the EM metric is instrumental in measuring a model’s capacity to reproduce precise sequences, it can be overly harsh, penalizing instances where minor inaccuracies do not hinder the overall functionality or logic of the code.

[83] p: The Edit Sim, in contrast, examines the structural similarity between the predicted sequence and the ground truth, considering slight variations such as formatting changes or equivalent expressions. This metric offers a more nuanced perspective on the model’s performance by emphasizing its capacity to maintain semantic and syntactical coherence, even in the absence of exact matches.

[84] h2: 5. Results and Analysis

[85] figure: Model Python Csharp Java EM Edit Sim EM Edit Sim EM Edit Sim TinyLlama RoPE 0.000 8.886 0.025 10.533 0.000 11.141 ReRoPE 0.000 19.271 0.000 20.241 0.012 18.821 StreamingLLM 0.000 12.656 0.000 11.769 0.000 11.693 Paged Attn 0.034 2.278 0.087 4.194 0.024 3.019 Flash Attn 0.000 11.031 0.000 11.629 0.000 11.672 Vicuna RoPE 0.013 23.941 0.000 15.386 0.000 15.128 ReRoPE 0.000 24.630 0.000 23.189 0.000 21.145 StreamingLLM 0.000 18.925 0.000 15.428 0.000 15.006 Paged Attn 0.377 22.752 0.851 25.178 0.779 24.378 Flash Attn 0.013 23.919 0.000 25.021 0.000 23.553 Sheared-LLaMA RoPE 0.013 17.287 0.000 17.286 0.000 16.734 ReRoPE 0.000 18.144 0.000 18.515 0.000 17.660 StreamingLLM 0.000 17.602 0.000 15.434 0.012 16.022 Paged Attn 0.013 15.129 0.013 16.251 0.012 15.759 Flash Attn 0.013 17.302 0.000 17.250 0.000 16.687 Llama 2 RoPE 0.000 12.204 0.012 13.754 0.012 12.796 ReRoPE 0.000 22.848 0.000 24.957 0.000 21.815 StreamingLLM 0.000 18.538 0.000 16.150 0.012 15.581 Paged Attn 0.104 19.912 0.038 22.497 0.024 21.168 Flash Attn 0.013 12.215 0.013 13.791 0.012 12.750 Table 3. A Comparison of different models and their variants on code completion tasks across three programming languages: Python, Csharp, and Java. Each model’s performance is evaluated using two metrics: Exact Match (EM) and Edit Similarity (Edit Sim). EM represents the percentage of code completions that exactly match the ground truth, while Edit Sim measures the similarity between the predicted and actual code, accounting for minor variations. It is to be noted that the highest scores for each metric across all model variants for a particular language are highlighted in bold. Bold-faced values indicate the best-performing variants for a specific metric and programming language.

[86] p: As outlined in Section 1 , length extrapolation for code datasets presents a significant challenge compared to plain text datasets. Furthermore, the existing literature predominantly focuses on length extrapolation from the perspective of positional encoding. Therefore, this work aims to explore the following research questions (RQ).

[87] p: RQ-1 : Impact of Efficient Attention Mechanisms: How efficient attention mechanisms impact the performance of LLMs in code length extrapolation across programming languages?

[88] p: RQ-2 : Positional Extrapolation vs Efficient Attention: How does positional extrapolation (e.g., RoPE, ReRoPE) in LLMs performs in the code length extrapolation scenarios when compared with the efficient attention mechanisms?

[89] p: RQ-3 : Code Language-Specific Performance: How does the syntax and structure of different programming languages (Python, Csharp, Java) affect the performance of LLMs for code completion task in length extrapolation scenarios?

[90] h4: Impact of Efficient Attention Mechanisms :

[91] p: In relation to RQ-1, Table 3 indicates that the efficient attention mechanism, Paged Attention, generally surpasses positional extrapolation-based methods (RoPE and ReRoPE) in terms of EM scores across all programming languages. For instance, in a zero-shot code completion scenario with Python, Paged Attention attains an EM score of 0.377 0.377 , which is significantly higher than RoPE’s 0.013 0.013 . Similar patterns are evident in Csharp and Java, where Paged Attention consistently records the highest EM scores, highlighting its effectiveness in exact match situations.

[92] p: Paged Attention frequently excels in EM scores but significantly lags behind in Edit Sim scores. For example, when applied to the LLaMa2 model with Python, Paged Attention attains an EM score of 0.104 0.104 but only manages an Edit Sim score of 19.912 19.912 , markedly lower than ReRoPE’s 22.848 22.848 . This indicates that while Paged Attention is effective at generating exact matches, it struggles to preserve the overall structure and similarity of the code, resulting in reduced Edit Sim scores. This discrepancy may arise from Paged Attention’s design, which prioritizes efficiency and speed, potentially overlooking less critical aspects of the input sequence that are essential for maintaining the structural integrity of the code data.

[93] h4: Positional Extrapolation vs. Efficient Attention :

[94] p: In reference to RQ-2, it is evident from Table 3 that RoPE-based positional extrapolation methods, particularly ReRoPE, demonstrate superior stability in performance across longer code sequences as measured by Edit Sim scores. For instance, ReRoPE consistently achieves the highest Edit Sim scores across all models and languages. This consistent performance indicates that ReRoPE effectively maintains positional coherence throughout extended code sequences, facilitating the capture of syntactical and structural dependencies necessary for code completion tasks. This stability can be attributed to ReRoPE’s design, which enables it to adeptly capture and extrapolate positional information by scaling attention scores using a sliding window mechanism.

[95] p: Conversely, efficient attention mechanisms such as Paged Attention tend to perform poorly in terms of Edit Sim scores. While these methods prioritize optimizing attention computation over long sequences by examining only a portion of the context at any given moment, this efficiency comes at a cost. The limited context can result in a loss of information for tokens that are far apart in the sequence. This is especially detrimental in length extrapolation tasks, where comprehensive context is vital for accurate code completion. As a result, efficient attention mechanisms experience a notable decline in Edit Sim scores in comparison to ReRoPE.

[96] p: Furthermore, both Flash Attention and StreamingLLM demonstrate significant difficulties in zero-shot code completion tasks, particularly in length extrapolation scenarios, as evidenced by their lower EM and Edit Sim scores. The primary design of these methods prioritizes accelerating attention computation, often at the expense of maintaining critical positional information in extended code sequences. As a result, their performance declines with increasing input length.

[97] h4: Language-Specific Performance :

[98] p: In context to RQ-3, it is apparent from Table 3 that syntax and structure of different programming languages influence the performance of inference-only methods in length extrapolation scenario. For example, models generally achieve higher Edit Sim scores in Python compared to Csharp and Java. For instance, using Vicuna model, ReRoPE achieves an Edit Sim of 24.630 24.630 in Python, whereas it produces lower score in Csharp ( 23.189 23.189 ) and Java ( 21.145 21.145 ). This finding suggests that Python’s more flexible and concise syntax might be easier for models to predict and maintain structural and syntactical integrity over longer sequences. In contrast Csharp and Java, with its strict and detailed syntax, become challenging for LLMs to extrapolate, leading to lower performance. The structured nature of these languages, with its rigid rules and nested formats, makes it harder for the LLMs to maintain high performance when dealing with longer code sequences.

[99] h4: Need of Better Evaluation Metrics :

[100] p: The Exact Match (EM) metric does not adequately consider minor variations that do not impact the code’s functionality or logical correctness. For example, differences in formatting, variable naming, or equivalent syntactical structures are penalized under EM, despite the fact that they can result in functionally identical code. This rigid evaluation approach may reduce the practical utility of the model, especially in real-world situations where preserving functionality is more important than ensuring exact replication of code sequences.

[101] p: The Edit Similarity (Edit Sim) metric complements EM by leveraging the structural similarity between predicted and ground truth sequences. While it successfully captures minor variations and provides a more comprehensive view of a model’s ability to generate coherent outputs, it still falls short in evaluating the functional correctness of the generated code. This is because Edit Sim primarily focuses on syntactical and structural alignment, often disregarding whether the generated code behaves as intended or meets logical task requirements. For instance, a piece of code with high structural similarity to the ground truth but containing a critical logical error would still receive a high Edit Sim score, rendering it insufficient for a comprehensive evaluation.

[102] p: Given the limitations of existing evaluation metrics such as Edit Sim and EM, there is a pressing need for novel metrics tailored to the unique demands of the long code completion task. These metrics should assess not only the syntactical and structural accuracy of generated code but also its functional correctness and logical equivalence to the ground truth. To provide a more comprehensive evaluation, metrics that evaluate the following aspects are necessary:

[103] p: Compilation and Testability: Examine the ability of generated code to compile successfully and pass predefined test cases.

[104] p: Functional Correctness: Evaluate the generated code’s ability to meet specific functionality criteria, such as correct output or behavior.

[105] p: Code Quality: Incorporate metrics that assess code readability, maintainability, and adherence to best practices, such as code style, naming conventions, and commenting standards.

[106] p: By incorporating these enhanced evaluation criteria, a more realistic and comprehensive assessment of model performance can be achieved, ultimately leading to improved long code completion capabilities.

[107] h2: 6. Conclusions

[108] p: In this study, we conducted a comprehensive analysis of inference-only methods, such as positional encoding (e.g., ReRoPE) and efficient attention mechanisms (e.g., Paged Attention), specifically for length extrapolation in zero-shot long code completion tasks. Our findings indicate that ReRoPE effectively maintains structural integrity in long sequences, resulting in consistently higher Edit Similarity (Edit Sim) scores. Conversely, while Paged Attention achieves superior Exact Match (EM) scores, it often fails to preserve the overall structure of the code.

[109] p: Looking ahead, we intend to explore the synergy between Paged Attention and ReRoPE to enhance both EM and Edit Sim scores in zero-shot code completion tasks. We plan to perform experiments using various long code completion datasets and extend this strategy to other code-related challenges to improve the generalizability of our findings. Furthermore, future research could focus on hybrid attention mechanisms and task-specific fine-tuning strategies to bolster the performance of large language models (LLMs) across different programming languages.

[110] p: The EM metric evaluates model performance by measuring exact matches against the ground truth while disregarding minor variations, such as formatting or variable naming, that do not impact functional correctness. In contrast, Edit Sim captures structural alignment but does not assess the functional correctness of the generated code, potentially allowing logical errors to remain unnoticed. These shortcomings highlight the necessity for new metrics that gauge functional correctness , logical equivalence , and code quality . Such metrics should include criteria like compilation success and test case coverage.

[111] p: Our work relies on leveraging pretrained LLMs, which presented significant challenges due to computational resource limitations when processing very long context inputs. As a result, we were unable to explore the problem of code completion with extensive contexts. Additionally, we did not investigate the newly released, code-specific LLMs, as they primarily utilize newer versions of the Transformer module, which are not compatible with our current implementation of ReRoPE. Furthermore, the HiRoPE codebase ( Zhang et al., 2024a ) is unavailable, preventing us from evaluating its performance in long code completion tasks.

[112] h2: References

[113] h2: Instructions for reporting errors

[114] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[115] p: Tip: You can select the relevant text first, to include it in your report.

[116] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[117] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
