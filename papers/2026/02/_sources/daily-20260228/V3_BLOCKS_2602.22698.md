[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Tokenization, Fusion and Decoupling: Bridging the Granularity Mismatch Between Large Language Models and Knowledge Graphs

[3] h6: Abstract

[4] p: Leveraging Large Language Models (LLMs) for Knowledge Graph Completion (KGC) is promising but hindered by a fundamental granularity mismatch. LLMs operate on fragmented token sequences, whereas entities are the fundamental units in knowledge graphs (KGs) scenarios. Existing approaches typically constrain predictions to limited candidate sets or align entities with the LLM’s vocabulary by pooling multiple tokens or decomposing entities into fixed-length token sequences, which fail to capture both the semantic meaning of the text and the structural integrity of the graph. To address this, we propose KGT , a novel framework that uses dedicated entity tokens to enable efficient, full-space prediction. Specifically, we first introduce specialized tokenization to construct feature representations at the level of dedicated entity tokens. We then fuse pre-trained structural and textual features into these unified embeddings via a relation-guided gating mechanism, avoiding training from scratch. Finally, we implement decoupled prediction by leveraging independent heads to separate and combine semantic and structural reasoning. Experimental results show that KGT consistently outperforms state-of-the-art methods across multiple benchmarks.

[5] h2: 1 Introduction

[6] p: Knowledge Graphs (KGs) serve as pivotal resources for modern artificial intelligence, supporting a multitude of knowledge-intensive tasks Ji et al. (2021) ; Rossi et al. (2021) , such as question answering Zhai et al. (2024) and recommendation systems Zhao et al. (2024) . However, real-world KGs frequently suffer from incompleteness, necessitating Knowledge Graph Completion (KGC) to predict missing triplets based on observed facts. Recently, Large Language Models (LLMs) have revolutionized Natural Language Processing (NLP), achieving state-of-the-art performance Touvron et al. (2023) ; Qin et al. (2023) ; Liu et al. (2024) . Powered by massive parameters that encode vast open-world knowledge, LLMs exhibit exceptional semantic reasoning capabilities. Consequently, leveraging this rich parametric knowledge to enhance KGC has emerged as a promising frontier. Despite this potential, applying LLMs to KGC faces a fundamental granularity mismatch. Tokens are the basic elements for language models, but it needs to take at least several tokens to describe and identify different entities in a KG. Consequently, one category of methods Liu et al. (2025) ; Wei et al. (2023) ; Yao et al. (2025) ; Chen et al. (2024) ; Jiang et al. (2024) avoids generation by picking from a limited set of options, sacrificing the LLM’s potential for global ranking over the entire entity space and rendering the process inefficient.

[7] figure: Figure 1: An illustration of existing two strategies of full-space LLM-based methods and KGT. (a) Pooling multiple tokens to unified representations for entities; (b) Decomposing entities into fixed-length sub-word sequences; (c) Constructing feature representations directly at the indivisible entity level.

[8] p: To achieve full-space prediction, another category of approaches attempts to align entities with the LLM’s native vocabulary, typically via two strategies: pooling Huang et al. (2025) ; Guo et al. (2024) or decomposition Guo et al. (2025) as illustrated in Figure 1 . However, these two strategies struggle with some significant challenges. Pooling operations compress entity tokens into a single vector, inevitably leading to semantic dilution, which is particularly severe for long or polysemous entities. Besides, decomposing entities into fixed-length sub-word sequences preserves fine-grained semantics but disrupts the structural integrity. Consequently, such methods remain trapped in a trade-off between semantic expressiveness and structural modeling. This compels us to question: Is following the LLM’s native vocabulary truly necessary for full-space prediction on KGs? To this end, we propose KGT, a novel framework that bridges the granularity mismatch between LLMs and KGs by orchestrating Tokenization, Fusion, and Decoupling . Specifically, as illustrated in Figure 1 , we first register entities and relations as special tokens, treating them as indivisible units to maintain granularity consistency. Next, to circumvent the high cost of learning these tokens from scratch, we employ dual-stream specialized token embedding at the input level, where we project pre-trained textual and structural features into a unified latent space and fuse them via a relation-guided gating mechanism to explicitly inject structural priors. Finally, we implement decoupled prediction via dual-view heads, which project the LLM’s hidden states into distinct textual and structural subspaces. This design explicitly separates semantic and structural reasoning, producing independent scores that are then adaptively combined via learnable scalers for comprehensive full-space prediction. Our major contributions are summarized as follows:

[9] p: We propose KGT, a novel end-to-end framework that bridges the granularity mismatch via specialized tokenization. By representing entities as indivisible specialized tokens, KGT eliminates the need for candidate filtering, enabling full-space prediction in a single step.

[10] p: We develop a dual-stream fusion and decoupling architecture. Specifically, we employ a relation-guided gating mechanism to fuse textual and structural features, and dual-view heads to disentangle reasoning. Additionally, utilizing pre-trained embeddings as a warm start ensures superior training efficiency.

[11] p: To evaluate the performance of KGT, we conduct comprehensive experiments and further explorations on three public benchmarks. Empirical results demonstrate that KGT outperforms 19 recent baselines, achieving new state-of-the-art results, promoting the stronger capability of LLMs for KGC tasks.

[12] h2: 2 Preliminary

[13] figure: Figure 2: Overview of the KGT framework. Part 1 illustrates the overall pipeline of KGT. The tokenizer first processes the input text containing the incomplete triple query, where entities and relations are represented as special tokens added to the original vocabulary. These special tokens obtain their embeddings via the Dual-Stream Specialized Token Embedding module. Subsequently, the LLM Backbone encodes the sequence, extracting the feature of the last token, which is then fed into the Dual-View Decoupled Predictor to generate the probability distribution over the entire entity vocabulary. Part 2 details the implementation of the Dual-Stream Specialized Token Embedding, where the dashed line indicates the assignment of the fused specialized feature to the special token representing the head entity h. Part 3 depicts the detailed architecture of the Dual-View Decoupled Predictor.

[14] h3: 2.1 Task Definition

[15] p: A Knowledge Graph is formally defined as 𝒢 = ( ℰ , ℛ , 𝒯 ) \mathcal{G}=(\mathcal{E},\mathcal{R},\mathcal{T}) , where ℰ \mathcal{E} , ℛ \mathcal{R} , and 𝒯 \mathcal{T} denote the sets of entities, relations, and triplets, respectively. To explicitly model the dual nature of KGs, we define two modalities: textual ( t t ) and structural ( s s ). For any entity e ∈ ℰ e\in\mathcal{E} (or relation r ∈ ℛ r\in\mathcal{R} ), we denote its available raw information as 𝒳 t ​ ( e ) \mathcal{X}_{t}(e) and 𝒳 s ​ ( e ) \mathcal{X}_{s}(e) , corresponding to the textual semantics and structural topology, respectively. KGC aims to predict the missing tail entity t t given a query ( h , r , ? ) (h,r,?) Bordes et al. (2013) . We utilize inverse relations r − 1 r^{-1} to unify head entity prediction ( ? , r , t ) (?,r,t) into the tail prediction format ( t , r − 1 , ? ) (t,r^{-1},?) .

[16] h3: 2.2 Large Language Models

[17] p: Generally, a typical LLM comprises four key components: Tokenizer: Splits input text into a token sequence t 0 : n t_{0:n} based on vocabulary 𝒱 \mathcal{V} . In this work, we adopt an expanded tokenizer, registering individual entities and relations as indivisible tokens. For example, entity "Mainz" and relation "capital of" are encoded as tokens <kgl: Mainz> and <kgl: capital of>, respectively; Token Embedding: Maps the discrete tokens to a sequence of low-dimensional vectors 𝐭 0 : n \mathbf{t}_{0:n} ; Transformer: The core of the LLM, which processes the input embeddings into deep hidden states:

[18] table: 𝐡 0 : n = ℳ ( 𝐭 0 : n ) ; \mathbf{h}_{0:n}=\mathcal{M}(\mathbf{t}_{0:n}); (1)

[19] p: Head Layer: Maps the final hidden state 𝐡 n \mathbf{h}_{n} to a probability distribution 𝐩 n + 1 ∈ ℝ | 𝒱 | \mathbf{p}_{n+1}\in\mathbb{R}^{\lvert\mathcal{V}\rvert} for predicting the next token t n + 1 t_{n+1} :

[20] table: 𝐩 n + 1 = ℋ ⁡ ( 𝐡 n ) . \mathbf{p}_{n+1}=\mathcal{H}(\mathbf{h}_{n}). (2)

[21] p: In this paper, we focus on customizing the Token Embedding and Head Layer . For KG elements added to the vocabulary, we design token embeddings that integrate both textual semantics and structural priors. Distinctively, unlike standard LLMs that generate over the general vocabulary, we re-implement the head layer to map hidden states specifically to the full entity set ℰ \mathcal{E} , where ℰ ⊂ 𝒱 \mathcal{E}\subset\mathcal{V} .

[22] h2: 3 Methodology

[23] p: In this section, we elaborate on the proposed framework, KGT, in two parts: Dual-Stream Special Token Embedding, Dual-View Decoupled Predictor. Figure illustrates the overview of KGT. Notably, the prompt in this paper follows that of MKGL Guo et al. (2024) .

[24] h3: 3.1 Dual-Stream Specialized Token Embedding

[25] p: Prior research Zhang et al. (2024a) ; Zhang et al. (2025) ; Cao et al. (2022) confirms that textual semantics and structural topology are both indispensable for KGC. However, existing LLM-based methods relying on sub-token composition often compromise or neglect one modality. To effectively model entities and relations, we replace the standard embedding layer with a Dual-Stream Specialized Token Embedding module ( E specialized E_{\text{specialized}} ). This module treats entities and relations as holistic tokens and processes them via parallel streams of feature extraction, projection and gating fusion. For clarity, we delineate the process for entities below, noting that relations follow a symmetric procedure.

[26] h4: Feature Extraction.

[27] p: For an entity e ∈ ℰ e\in\mathcal{E} , we transform its raw inputs 𝒳 t ​ ( e ) \mathcal{X}_{t}(e) and 𝒳 s ​ ( e ) \mathcal{X}_{s}(e) into dense feature vectors. For textual information, we employ a sentence embedding extractor (e.g., text-embedding-3-small 1 1 1 https://platform.openai.com/docs/guides/embeddings ) to encode the raw text 𝒳 t ​ ( e ) \mathcal{X}_{t}(e) into a semantic vector 𝐞 t ∈ ℝ d t \mathbf{e}_{t}\in\mathbb{R}^{d_{t}} . Conversely, for the raw structural information, we initialize the structural vector 𝐞 s ∈ ℝ d s \mathbf{e}_{s}\in\mathbb{R}^{d_{s}} using embeddings derived from the TuckER model.

[28] h4: Feature Projection.

[29] p: Since the extracted feature vectors 𝐞 t \mathbf{e}_{t} and 𝐞 s \mathbf{e}_{s} originate from latent spaces disjoint from the LLM, we employ modality-specific projectors to map them into the LLM’s unified semantic space ℝ d \mathbb{R}^{d} . Each projector consists of four components: a dropout layer, a fully connected layer, an activation function, and a normalization layer. Specifically, the aligned token embedding 𝐞 t ′ \mathbf{e}^{\prime}_{t} and 𝐞 s ′ \mathbf{e}^{\prime}_{s} is computed as:

[30] table: 𝐞 t ′ = RMSNorm ⁡ ( σ ⁡ ( 𝐖 t ⋅ Dropout ⁡ ( 𝐞 t ) ) ) \mathbf{e}^{\prime}_{t}=\mathrm{RMSNorm}\left(\sigma\left(\mathbf{W}_{t}\cdot\mathrm{Dropout}(\mathbf{e}_{t})\right)\right) (3)

[31] table: 𝐞 s ′ = RMSNorm ⁡ ( σ ⁡ ( 𝐖 s ⋅ Dropout ⁡ ( 𝐞 s ) ) ) \mathbf{e}^{\prime}_{s}=\mathrm{RMSNorm}\left(\sigma\left(\mathbf{W}_{s}\cdot\mathrm{Dropout}(\mathbf{e}_{s})\right)\right) (4)

[32] p: where 𝐖 t ∈ ℝ d × d t \mathbf{W}_{t}\in\mathbb{R}^{d\times d_{t}} and 𝐖 s ∈ ℝ d × d s \mathbf{W}_{s}\in\mathbb{R}^{d\times d_{s}} are learnable projection matrix. Note that the bias term is omitted. Consistent with Llama-2, we utilize SiLU Elfwing et al. (2018) as the activation function σ \sigma and LlamaRMSNorm Zhang and Sennrich (2019) for normalization to ensure seamless integration with subsequent layers.

[33] h4: Relation-Guided Gating Fusion.

[34] p: To effectively capture the varying reliance on textual semantics versus structural topology, we employ a Relation-Guided Gating Fusion (ReGF) mechanism:

[35] table: ( g t , g s ) \displaystyle(g_{t},g_{s}) = Softmax ⁡ ( z t , z s ) \displaystyle=\mathrm{Softmax}(z_{t},z_{s}) (5) z m \displaystyle z_{m} = 𝒰 m ​ ( 𝐞 m ′ ) / d + δ m σ ⁡ ( ϵ r ) \displaystyle=\frac{\mathcal{U}_{m}(\mathbf{e}^{\prime}_{m})/\sqrt{d}+\delta_{m}}{\sigma(\epsilon_{r})} (6)

[36] p: Here, z m z_{m} represents the relation-aware logit for modality m ∈ { t , s } m\in\{t,s\} , reflecting the relative importance of the textual and structural modalities, respectively. 𝒰 m \mathcal{U}_{m} , 𝒰 m ′ \mathcal{U}^{\prime}_{m} are two projection layers and the term OPEN δ m ∼ 𝒩 ⁡ ( 0 , 𝒰 m ′ ​ ( 𝐞 m ′ ) / d ) ) \delta_{m}\sim\mathcal{N}(0,\mathcal{U}^{\prime}_{m}(\mathbf{e}^{\prime}_{m})/\sqrt{d})) denotes the tunable Gaussian noise introduced to enhance robustness, which has been proven to work Shazeer et al. (2017) . Furthermore, we introduce a learnable relation-aware temperature ϵ r \epsilon_{r} with a sigmoid function σ \sigma to limit the temperature in the range ( 0 , 1 ) (0,1) . This formulation dynamically calibrates the gating weights according to the relational context before the final fusion Finally, the entity token embedding 𝐭 e \mathbf{t}_{e} is derived via soft weighted summation:

[37] table: 𝐭 e = g t ​ 𝐞 t ′ + g s ​ 𝐞 s ′ \mathbf{t}_{e}=g_{t}\mathbf{e}^{\prime}_{t}+g_{s}\mathbf{e}^{\prime}_{s} (7)

[38] p: This fused embedding 𝐭 e \mathbf{t}_{e} serves as the vector representation for entity tokens in the input sequence 𝐭 0 : n \mathbf{t}_{0:n} , as defined in the Preliminary. Similarly, the relation token embedding 𝐭 r \mathbf{t}_{r} is obtained via a symmetric process of feature extraction and gating fusion.

[39] h3: 3.2 Dual-View Decoupled Predictor

[40] p: To overcome the limitations of restricted candidate sets inherent in some prior approaches Wei et al. (2023) ; Liu et al. (2025) , we propose the Dual-View Decoupled Predictor ( P decoupled P_{\text{decoupled}} ) to achieve one-shot global ranking over the entire entity vocabulary. Additionally, by projecting LLM representations into decoupled textual and structural latent spaces, we effectively utilize the distinct advantages of each modality during the prediction phase.

[41] h4: Dual-View Head MLPs.

[42] p: We employ dual-view head MLPs to process the LLM’s final hidden state 𝐡 n ∈ ℝ d \mathbf{h}_{n}\in\mathbb{R}^{d} into distinct textual and structural latent representations, denoted as 𝐡 t ′ ∈ ℝ d t \mathbf{h}^{\prime}_{t}\in\mathbb{R}^{d_{t}} and 𝐡 s ′ ∈ ℝ d s \mathbf{h}^{\prime}_{s}\in\mathbb{R}^{d_{s}} . Each MLP consists of four components: a dropout layer, a fully connected layer, an activation function, and a normalization layer:

[43] table: 𝐡 t ′ = RMSNorm ⁡ ( σ ⁡ ( Dropout ⁡ ( 𝐡 n ) ⋅ 𝐖 t ′ ) ) \mathbf{h}^{\prime}_{t}=\mathrm{RMSNorm}\left(\sigma\left(\mathrm{Dropout}(\mathbf{h}_{n})\cdot\mathbf{W}^{\prime}_{t}\right)\right) (8)

[44] table: 𝐡 s ′ = RMSNorm ⁡ ( σ ⁡ ( Dropout ⁡ ( 𝐡 n ) ⋅ 𝐖 s ′ ) ) \mathbf{h}^{\prime}_{s}=\mathrm{RMSNorm}\left(\sigma\left(\mathrm{Dropout}(\mathbf{h}_{n})\cdot\mathbf{W}^{\prime}_{s}\right)\right) (9)

[45] p: where 𝐖 t ′ ∈ ℝ d × d t \mathbf{W}^{\prime}_{t}\in\mathbb{R}^{d\times d_{t}} and 𝐖 s ′ ∈ ℝ d × d s \mathbf{W}^{\prime}_{s}\in\mathbb{R}^{d\times d_{s}} are learnable projection matrices. Consistent with the input projector, we employ SiLU Elfwing et al. (2018) as the activation function σ \sigma and LlamaRMSNorm Zhang and Sennrich (2019) for normalization. It is noteworthy that the bias vector is not used.

[46] h4: LoRA Score Layer.

[47] p: To efficiently adapt the model to the KGC task without full-parameter fine-tuning, we propose a LoRA Hu et al. (2022) scoring mechanism that leverages the pre-trained entity embeddings as a warm start. We instantiate two separate scoring matrices, 𝐖 t S \mathbf{W}^{S}_{t} and 𝐖 s S \mathbf{W}^{S}_{s} , corresponding to the textual and structural streams. Taking the textual modality as an example, the scoring weight is computed as:

[48] table: 𝐖 t S \displaystyle\mathbf{W}^{S}_{t} = 𝐖 b ​ a ​ s ​ e , t + 𝐀 t ​ 𝐁 t \displaystyle=\mathbf{W}_{base,t}+\mathbf{A}_{t}\mathbf{B}_{t} (10) 𝐩 t \displaystyle\mathbf{p}_{t} = 𝐡 t ′ ​ ( 𝐖 t S ) ⊤ \displaystyle=\mathbf{h}^{\prime}_{t}(\mathbf{W}^{S}_{t})^{\top} (11)

[49] p: where 𝐩 t ∈ ℝ | ℰ | \mathbf{p}_{t}\in\mathbb{R}^{|\mathcal{E}|} denotes the prediction logits over the entity vocabulary. Crucially, the frozen base matrix 𝐖 b ​ a ​ s ​ e , t ∈ ℝ | ℰ | × d t \mathbf{W}_{base,t}\in\mathbb{R}^{|\mathcal{E}|\times d_{t}} is initialized with the pre-trained textual entity embeddings defined in the 3.1 module, rather than random initialization. Similarly, the structural base matrix 𝐖 b ​ a ​ s ​ e , s \mathbf{W}_{base,s} is initialized with the TuckER embeddings. 𝐀 t \mathbf{A}_{t} and 𝐁 t \mathbf{B}_{t} are low-rank learnable adapters ( r ≪ d t r\ll d_{t} ) initialized with Gaussian noise and zeros, respectively. This design ensures the predictor retains the rich semantic and structural priors captured during the pre-training phase while adapting to the specific ranking objective.

[50] h4: Optimization.

[51] p: To effectively combine the predictions from textual and structural views, we employ a learnable logit scaling mechanism (LLS) with two learnable scalar parameters, λ t \lambda_{t} and λ s \lambda_{s} , to dynamically adjust the contribution of each view. The final hybrid logits 𝐩 n + 1 \mathbf{p}_{n+1} are computed as the weighted average of the dual-view logits, aligning with the next-token prediction objective:

[52] table: 𝐩 n + 1 = 1 2 ​ ( λ t ​ 𝐩 t + λ s ​ 𝐩 s ) \mathbf{p}_{n+1}=\frac{1}{2}\left(\lambda_{t}\mathbf{p}_{t}+\lambda_{s}\mathbf{p}_{s}\right) (12)

[53] p: The model is optimized using the standard Cross-Entropy Loss to maximize the likelihood of the ground truth entity e + e^{+} :

[54] table: ℒ = − 𝐩 n + 1 e + + log ⁡ ( ∑ e j ∈ ℰ exp ⁡ ( 𝐩 n + 1 e j ) ) \mathcal{L}=-\mathbf{p}_{n+1}^{e^{+}}+\log\left(\sum_{e_{j}\in\mathcal{E}}\exp(\mathbf{p}_{n+1}^{e_{j}})\right) (13)

[55] p: where 𝐩 n + 1 e \mathbf{p}_{n+1}^{e} denotes the final prediction logit of entity e e as the next token t n + 1 t_{n+1} .

[56] h2: 4 Experiment

[57] figure: Methods MKG-W MKG-Y DB15K MRR ↑ \uparrow H@1 ↑ \uparrow MRR ↑ \uparrow H@1 ↑ \uparrow MRR ↑ \uparrow H@1 ↑ \uparrow H@3 ↑ \uparrow H@10 ↑ \uparrow TransE 29.19 21.06 30.73 23.45 24.86 12.78 31.48 47.07 DistMult 20.99 15.93 25.04 19.33 23.03 14.78 26.28 39.59 RotatE 33.67 26.80 34.95 29.10 29.28 17.87 36.12 49.66 TuckER 30.39 24.44 37.05 34.59 33.86 25.33 37.91 50.38 IKRL 32.36 26.11 33.22 30.37 26.82 14.09 34.93 49.09 KG-Bert 28.68 21.12 - - 23.94 11.98 31.05 46.54 FLT-LM 32.75 25.89 - - 33.45 24.56 37.67 50.12 OTKGE 34.36 28.85 35.51 31.97 23.86 18.45 25.89 34.23 MANS 30.88 24.89 29.03 25.25 28.82 16.87 36.58 49.26 MMRNS 35.03 28.59 35.93 30.53 32.68 23.01 37.86 51.01 IMF 34.50 28.77 35.79 32.95 32.25 24.20 36.00 48.19 VISTA 32.91 26.12 30.45 24.87 30.42 22.49 33.56 45.94 AdaMF 34.27 27.21 38.06 33.49 32.51 21.31 39.60 51.68 MyGO 36.10 29.78 38.44 35.01 37.72 30.08 41.26 52.21 MOMOK 35.89 30.38 37.91 35.09 39.54 32.38 43.45 54.14 KG-Llama-7b - 20.20 - - - 13.46 - - GPT 3.5 Turbo - 22.66 - - - 21.71 - - MKGL ♣ 32.86 26.54 29.11 24.30 27.14 18.68 30.39 43.87 K-ON 36.64 30.05 - - 38.10 30.13 42.77 53.59 KGT 43.27 36.02 43.62 37.68 42.16 34.06 46.03 57.69 Improvements +18.1% +18.6% +13.5% +7.4% +6.6% +5.2% +5.9% +6.6% Table 1: The main KGC results. ♣ \clubsuit represents the experimental results that we reproduced through source code. The best and second-best results are boldfaced and underlined, respectively. -: unavailable entry.

[58] h4: Datasets.

[59] p: In this paper, we employ three widely recognized MKGC benchmarks DB15K Liu et al. (2019) , MKG-W, and MKG-Y Xu et al. (2022) to evaluate the model performance. MKG-W and MKG-Y are subsets derived from Wikidata Vrandečić and Krötzsch (2014) , YAGO Suchanek et al. (2007) , and DBpedia Lehmann et al. (2015) , respectively. These datasets encompass not only structural triplets but also rich unstructured modalities including text and images. Since LLM-based methods utilize additional textual information, comparing them directly against conventional baselines Yao et al. (2025) ; Wei et al. (2023) leads to unfair evaluations. Therefore, we conduct experiments on multi-modal datasets to guarantee a more rigorous and fairer comparison. The raw data are obtained from their official release sources. The detailed information on the datasets can be found in Table 6 in Appendix C .

[60] h4: Evaluation Protocol.

[61] p: Following established protocols Sun et al. (2019) , we utilize rank-based metrics including Mean Reciprocal Rank (MRR) and Hits@K ( K = 1 , 3 , 10 K=1,3,10 ) , short for H@K, to evaluate the performance. All results are reported under the filtered setting Bordes et al. (2013) , which excludes candidate triples existing in the training data for fair comparisons.

[62] h4: Baselines.

[63] p: To make a comprehensive performance evaluation, we employ 19 different state-of-the-art MMKGC methods as baselines: the conventional structure-only methods, such as TransE Bordes et al. (2013) , DistMult Yang et al. (2014) , RotatE Sun et al. (2019) and Tucker Balažević et al. (2019) ; the methods leveraging external knowledge of image and text modalities, such as IKRL Xie et al. (2016) , TransAE Wang et al. (2019) , KG-Bert Yao et al. (2019) and FLT-LM Lin et al. (2023) , OTKGE Cao et al. (2022) , MMRNS Xu et al. (2022) , VISTA Lee et al. (2023) , IMF Li et al. (2023) , AdaMF Zhang et al. (2024c) , MyGO Zhang et al. (2025) , MOMOK Zhang et al. (2024a) ; and the LLM-based methods such as KG-Llama7b Yao et al. (2025) and GPT 3.5 Zhu et al. (2024) , MKGL Guo et al. (2024) , K-ON Guo et al. (2025) .

[64] h4: Implementation Details.

[65] p: We employ Llama-2-7b-chat Touvron et al. (2023) as the base LLM model. For parameter-efficient fine-tuning, we set the LoRA rank r = 8 r=8 , alpha α = 16 \alpha=16 and dropout = 0.05 =0.05 . The model is trained on 8 NVIDIA H200 GPUs. Full hyper-parameter configurations are available in Appendix B .

[66] h3: 4.1 Main Results

[67] p: The main KGT results are detailed in Table 1 . We can easily find that methods combining image and text modalities usually show higher performance than conventional structure-only approaches, highlighting the advantages of external knowledge. However, We also notice that some multi-modal methods perform worse than conventional methods on specific datasets. For instance, FLT-LM Lin et al. (2023) and MANS Zhang et al. (2023) perform worse than RotatE Sun et al. (2019) on the MKG-W dataset. This suggests that additional information is not always beneficial, for it may introduce noise to training. In contrast, KGT makes significant progress in all the metrics and achieves new SOTA results, with an improvement of about 5%-18%. This demonstrates the superior reasoning capability of our LLM-based framework and the importance of effectively fusing textual and structural information. In addition, we find that the improvement ratio of the KGT for Hits@1 and MRR metrics is usually large, which means that the model achieves the best results in both overall prediction and accurate prediction. Early LLM-based methods, as mentioned in previous sections, are optimized against tokens, resulting in fragmented semantics and performance often inferior to even non-LLM baselines. While recent approaches Guo et al. (2024) ; Guo et al. (2025) have attempted to achieve entity-level optimization by aligning entity with the LLM’s native vocabulary, their performance remains significantly lower than KGT. By contrast, our method constructs features directly at the indivisible entity level, which not only facilitates the seamless injection of structural topology but also maximally preserves the integrity of textual semantics.

[68] h3: 4.2 Computational Cost

[69] figure: Setting MKG-W MKG-Y DB15K MRR H@1 MRR H@1 MRR H@1 Full Model 43.27 36.02 43.61 37.68 42.16 34.06 Modality Contribution (1.1). Structure Modality 32.73 27.16 36.12 33.39 37.62 28.85 (1.2). Text Modality 40.69 32.44 40.86 34.36 38.08 30.14 Model Design (2.1). w/o structural input 41.43 33.31 42.15 35.91 41.57 33.47 (2.2). w/o textual input 39.90 32.78 39.10 33.78 41.74 33.53 (2.3). w/o structural predictor 42.39 34.81 41.99 35.27 39.53 32.11 (2.4). w/o textual predictor 33.03 26.46 34.20 31.01 37.84 29.06 (2.5). w/o noise σ m \sigma_{m} 41.05 33.00 42.78 37.23 41.81 33.68 (2.6). w/o relational ϵ r \epsilon_{r} 42.63 35.50 43.23 37.29 41.77 33.55 (2.7). w/o LLS 42.81 35.33 42.48 36.55 41.93 33.65 Table 2: Ablation study of different settings on MKG-W, MKG-Y, and DB15K datasets.

[70] figure: Figure 3: A comprhensive comparison between several viriants of KGT on DB15K.

[71] p: Given that In-Context Learning (ICL) represents an alternative to address the granularity mismatch by supplementing context, we further investigated the rationality and computational efficiency of KGT by comparing it against four variants: (1) NewToken t ​ ( desc. ) \text{NewToken}_{t}(\text{desc.}) , which replaces pre-trained textual features with random initialization while incorporating entity descriptions as context; (2) NewToken s ​ ( 1-hop ) \text{NewToken}_{s}(\text{1-hop}) , which replaces pre-trained structural features with random initialization while incorporating 1-hop subgraphs as context; (3) NewToken ​ ( desc. + 1-hop ) \text{NewToken}(\text{desc. + 1-hop}) , which utilizes randomly initialized tokens with both entity descriptions and 1-hop subgraphs as context. Notably, for this variant, we train both the embedding and the predictor with full parameters to maximize the exploration of ICL effectiveness; and (4) KGT w/o P decoupled P_{\text{decoupled}} , which replaces the decoupled predictor P decoupled P_{\text{decoupled}} with a direct prediction head. As illustrated in Figure 3 , our method outperforms all variants. First, compared to variants relying on ICL, KGT significantly reduces the average input sequence length and training time by directly leveraging sentence encoders and pre-trained structural features for token initialization. Second, although the NewToken s ​ ( 1-hop ) \text{NewToken}_{s}(\text{1-hop}) variant lag slightly behind KGT in performance, it suffers from the neighborhood explosion problem. Furthermore, the comparison with KGT w/o P decoupled P_{\text{decoupled}} validates the rationality and necessity of our dual-head prediction mechanism. This demonstrates that merely injecting knowledge at the input side is insufficient for KGT, necessitating a coordinated output design to fully leverage the initialized representations. Ultimately, KGT supports larger batch sizes during both training and inference phases, enhancing computational efficiency. On the other side, compared to other LLM-based frameworks Guo et al. (2024) ; Guo et al. (2025) ; Touvron et al. (2023) , our model incurs minimal additional training parameters, even though generating new token embeddings for all entities and relations aligned with the LLM space. The trainable parameters primarily stem from feature alignment, decoupled projections, and the full-space scoring layer. Our approach remains linear in the growth of graph complexity. Figure 4 illustrates the parameter comparison across various LLM-based KGC methods. When viewed in conjunction with the SOTA KGC performance of KGT in Table 1 , we conclude that our method achieves state-of-the-art performance while maintaining high parameter efficiency.

[72] figure: Figure 4: Trainable parameters of some LLM-based KGC methods based on MKG-W.

[73] h3: 4.3 Ablation Studies

[74] figure: Figure 5: Results of different logits scaling.

[75] p: To confirm the soundness of our design, we conduct further ablation studies to investigate the contribution of modalites and design in KGT. The experimental results are presented in Table 2 . From the first group of experimental results, we can observe that both textual and structural information positively contribute to the final result. Notably, the textual modality exhibits a dominant influence, which we attribute to the high-quality sentence embeddings and the inherent linguistic advantages of the LLM. Moreover, the results from the second group reveal that our key designs significantly contribute to the final performance. Experiments of settings (2.1)–(2.4) confirm the effectiveness of the symmetric dual-stream architecture in balancing textual and structural information. Experiments of settings (2.5) and (2.6) confirm the effectiveness of relational context and tunable noise in the ReGF module. Experiment of setting (2.7) further validates the learnable logit scaling strategy for harmonizing output distributions. We also investigate the effect of the logit scaling coefficient γ = λ t / λ s \gamma=\lambda_{t}/\lambda_{s} , as depicted in Figure 5 . It can be observed that the impact of γ \gamma on the final results generally follows a pattern of initial increase followed by a slow decrease. Setting the scaling factor to either too small or too large is detrimental to the model’s learning performance. The model achieves the best results with γ = 1.4 \gamma=1.4 and γ = 1.6 \gamma=1.6 for MKG-W and MKG-Y, respectively.

[76] figure: Figure 6: KGC results using different feature extractors. We evaluate diverse textual feature extractors ( text-embedding-3-large , bge-large-en-v1.5 ) on the MKG-W dataset, and structural feature extractors (TransE, RotatE) on the DB15K dataset.

[77] h3: 4.4 Impact of Different Feature Extractors

[78] p: To further investigate the impact of different feature extractors on KGT, we conducted experiments using different extraction strategies. The performance results of these combinations are illustrated in Figure 6 . We observe that the choice of feature extractors actually does impact performance. However, even the least effective variant surpasses existing SOTA models, underscoring the robustness of KGT. This finding also aligns with our intuition that stronger extractors provide richer and more discriminative features, which naturally lead to superior performance after fine-tuning. Notably, these richer features often come with higher dimensionality and computational overhead.

[79] h3: 4.5 Case Study

[80] p: To intuitively demonstrate the effectiveness of KGT, we present several representative cases from the DB15K dataset. As shown in Figure 7 , KGT adaptively assign modality weights for different triples. Specifically, triples involving geographical topology tend to receive higher structural weights, while those dominated by conceptual semantics are assigned higher textual weights.

[81] figure: Figure 7: The comparison of model weights among various cases

[82] p: Table 3 presents three representative cases corresponding to structure-dominant, text-dominant, and synergistic scenarios to demonstrate that KGT can rescue a weak modality via the dominant modality’s probability distribution. Furthermore, KGT synergizes knowledge from both sides to achieve accurate joint predictions.

[83] figure: Table 3: Case study experiments on the DB15K dataset Case 1: ( ? , composer , Adaptation_(film) ) Textual Rank of the head entity “ Carter Burwell ” : 179 Structural Rank of the head entity “ Carter Burwell ” : 1 KGT Rank of the head entity “ Carter Burwell ” : 1 Case 2: ( ? , distributingCompany , Warner_Music_Group ) Textual Rank of the head entity “ Atlantic_Records ” : 1 Structural Rank of the head entity “ Atlantic_Records ” : 29 KGT Rank of the head entity “ Atlantic_Records ” : 1 Case 3: ( New York Stories , starring , ? ) Textual Rank of the tail entity “ Mia Farrow ” : 12 Structural Rank of the tail entity “ Mia Farrow ” : 15 KGT Rank of the tail entity “ Mia Farrow ” : 1

[84] h2: 5 Conclusion

[85] p: In this paper, we presented KGT to address the granularity mismatch between LLMs and KGs. Instead of relying on fragmented token sequences, KGT treats entities as indivisible tokens initialized via dual-stream specialized token embedding, allowing for the direct injection of structural priors and warm-start training. Crucially, we introduced a decoupled head predictor to leverage these representations, as our experiments confirm that such specialized inputs should be paired with a corresponding output mechanism. Overall, this end-to-end approach significantly reduces input length and training costs, achieving SOTA performance and promoting the capability of LLMs for KGC tasks.

[86] h2: 6 Limitations

[87] p: Although empirical experiments have confirmed the effectiveness of the proposed KGT, a limitation remains regarding its reliance on pre-computed structural priors. Specifically, since the current framework uses these priors for initialization without joint optimization, it cannot dynamically refine structural features during training. This makes the performance partially dependent on the quality of external KGE models. While employing stronger pre-trained models can mitigate this challenge, it introduces additional computational overhead, which we consider less cost-effective. Consequently, we regard implementing end-to-end structure learning as a more promising avenue. In the future, we will continue to explore this direction, aiming to devise a solution that integrates end-to-end structural learning into our framework. We believe that such an approach will drive further breakthroughs in the performance of LLMs for KG.

[88] h2: References

[89] h2: Appendix A Related Works

[90] h4: Knowledge Graph Completion

[91] p: Knowledge Graph (KG) completion is one of the most important tasks in the KG area, with mainstream methods generally falling into two categories: embedding-based and text-based approaches. Embedding-based methods ( Bordes et al. (2013) ; Sun et al. (2019) ; Yang et al. (2014) ; Balažević et al. (2019) ) generate low-dimensional vectors to model connectivity patterns via scoring functions. While simple and effective, they focus on relational information but often ignore the rich contextual information embedded within the text. Conversely, text-based methods ( Yao et al. (2019) ; Daza et al. (2021) ; Chen et al. (2022) ; Wang et al. (2022) ) utilize Pre-trained Language Models (PLMs) to encode textual descriptions, often introducing contrastive learning to enhance discriminative ability. However, these methods lack the inherent structural knowledgeof KGs. Consequently, recent efforts Zhang et al. (2020) ; Qiu et al. (2024) ; Chen et al. (2023) ; Liu et al. (2022) ; Wang et al. (2021) have attempted to combine embedding- and text-based paradigms to leverage their complementary strengths for superior performance.

[92] h4: LLM-based Knowledge Graph Completion.

[93] p: Due to rich semantic features, LLMs are deemed highly promising in the realm of KGC. However, the natural gap between the graph structure of KGs and the natural language makes it difficult to apply LLMs directly to KGC tasks. For instance, methods like KGLlama Yao et al. (2025) and KoPA Zhang et al. (2024b) simplify the task into triplet classification, i.e., estimating the correctness of a given triplet. Subsequently, many approaches attempt to complete the task within restricted candidate sets. Some works ( Wei et al. (2023) ; Sun et al. (2023) ; Kau et al. (2024) ) employ prompt engineering or retrieval strategies to obtain KG information and input it into LLMs for entity reranking. However, such an approach is evidently suboptimal. Recently, some methods Guo et al. (2025) ; Guo et al. (2024) ; Luo et al. (2025) have explored how to achieve full-space prediction. For example, K-ON Guo et al. (2025) integrates KG knowledge into the LLM by employing multiple head layers to predict multi-step tokens simultaneously, and aggregates the multi-step prediction tokens into an entity probability. Nevertheless, methods for full-space prediction are still scarce, and specifically, the effective synergy of textual and structural information remains an open problem.

[94] h2: Appendix B Implementation Details

[95] p: We introduce Algorithm 1 to demonstrate the fine-tuning process of KGT for KGC. The main hyper-parameter settings are summarized in Table 4 . Besides, we also provide the prompt we used in Table 5 .

[96] figure: Algorithm 1 KGT for KGC 1: Input: the training KG 𝒢 \mathcal{G} , the language model ℳ \mathcal{M} , the original vocabulary of the LLM 𝒱 llm \mathcal{V}_{\text{llm}} , the original token embedding layer of the LLM 𝐓 \mathbf{T} , dual-stream specialized token embedding E specialized E_{\text{specialized}} , and decoupled full-space predictor P decoupled P_{\text{decoupled}} . 2: for each batched triplets in the training KG 𝒢 \mathcal{G} do 3: Construct and tokenize the input instructions; 4: for each input token sequence t 0 : n t_{0:n} do 5: for each token t k t_{k} do 6: if t k ∈ 𝒱 llm t_{k}\in\mathcal{V}_{\text{llm}} then 7: 𝐭 k ← 𝐓 ⁡ ( t k ) \mathbf{t}_{k}\leftarrow\mathbf{T}(t_{k}) ; 8: else 9: 𝐭 k ← E specialized ​ ( t k ) \mathbf{t}_{k}\leftarrow E_{\text{specialized}}(t_{k}) (Equations ( 3 – 7 )); 10: end if 11: end for 12: end for 13: 𝐡 0 : n ← ℳ ( 𝐭 0 : n ) \mathbf{h}_{0:n}\leftarrow\mathcal{M}(\mathbf{t}_{0:n}) , obtaining the output hidden states of LLM (Equation ( 1 )); 14: Compute KGT textual and structural predictions with P decoupled P_{\text{decoupled}} (Equations ( 8 – 11 )); 15: Compute the final full-space prediction 𝐩 n + 1 \mathbf{p}_{n+1} following (Equation ( 12 )); 16: Compute and minimize the cross-entropy loss ℒ \mathcal{L} (Equation ( 13 )); 17: end for

[97] figure: Dataset LLM text dim struct dim LoRA r r LoRA α \alpha LORA target modules logits scaling ratio γ \gamma MKG-W Llama-2-7b 1536 256 8 16 query, value 1.4 MKG-Y Llama-2-7b 1536 256 8 16 query, value 1.6 DB15K Llama-2-7b 1536 256 8 16 query, value 1.5 Dataset epoch batch size per device gradient accumulation steps learning rate optimizer text dropout struct dropout MKG-W 8 32 1 2e-4 Adamw_8bit 0.2 0.4 MKG-Y 8 32 1 2e-4 Adamw_8bit 0.1 0.3 DB15K 8 32 1 4e-4 Adamw_8bit 0.0 0.5 Table 4: Hyper-parameter settings in the main experients.

[98] figure: Suppose that you are an excellent linguist studying a new three-word language for knowledge graph. Given the following dictionary: Input Type Description < < kgl: Mainz > > Head entity Mainz < < kgl: capital of > > Relation capital of Please complete the last word (?) of the sentence: < < kgl: Mainz > > < < kgl: capital of > > ? Table 5: The prompt of KGT. Note that we take entity "Mainz" and relation "capital of" as a example.

[99] h2: Appendix C Dataset Datails

[100] figure: Dataset #Entity #Relation #Train #Valid #Test Text MKG-W 15000 169 34196 4276 4274 14123 MKG-Y 15000 28 21310 2665 2663 12305 DB15K 12842 279 79222 9902 9904 9078 Table 6: Statistical information of the three datasets in our experiments. The entity descriptions are provided by the original datasets.

[101] h2: Appendix D Additional Experiment Results

[102] p: We present the additional experimental results in this section.

[103] h3: D.1 Full results on MKG-W and MKG-Y

[104] p: In our experiments, we present the MRR and Hits@1 results in Table 1 . We now present the results for the complete set of four metrics in both datasets in the Table 7 .

[105] figure: Methods MKG-W MKG-Y MRR H@1 H@3 H@10 MRR H@1 H@3 H@10 TransE 29.19 21.06 33.20 44.23 30.73 23.45 35.18 43.37 RotatE 33.67 26.80 36.68 46.76 34.95 29.10 38.35 45.30 TuckER 30.39 24.44 32.91 41.25 37.05 34.59 38.43 41.45 IKRL 32.36 26.11 34.75 44.07 33.22 30.37 34.28 38.60 TransAE 30.00 21.23 34.91 44.72 28.10 25.31 29.10 33.03 KG-Bert 28.68 21.12 32.57 43.46 - - - - KGLM 34.12 27.01 36.87 46.62 - - - - FLT-LM 32.75 25.89 32.87 44.56 - - - - OTKGE 34.36 28.85 34.36 36.25 35.51 31.97 37.18 41.38 MMRNS 35.03 28.59 37.49 47.47 35.93 30.53 39.07 45.47 VISTA 32.91 26.12 35.38 45.61 30.45 24.87 32.39 41.53 MANS 30.88 24.89 33.63 41.78 29.03 25.25 31.35 34.49 AdaMF 34.27 27.21 37.86 47.21 38.06 33.49 40.44 45.48 MyGO 36.10 29.78 38.54 47.75 38.44 35.01 39.84 44.19 MOMOK 35.89 30.38 37.54 46.13 37.91 35.09 39.20 43.20 KG-Llama-7b - 20.20 - - - - - - GPT 3.5 Turbo - 22.66 - - - - - - K-ON 36.64 30.05 38.72 48.26 - - - - our model 43.27 36.02 46.51 57.12 43.62 37.68 45.78 54.66 Improvements +18.1% +18.6% +20.1% +18.4% +13.5% +7.4% +13.2% +20.2% Table 7: Full results on the MKG-W and MKG-Y datasets.

[106] h3: D.2 Additional Results on WN18RR

[107] p: As our method involves registering all entities and relations into the LLM’s vocabulary, we conducted additional experiments on WN18RR Dettmers et al. (2018) to evaluate its performance on a dataset with a significantly larger entity space. While the datasets in our main settings contain at most 15,000 entities, WN18RR comprises 40,943 entities. We believe these supplementary experiments further demonstrate the generalizability and scalability of our approach.

[108] figure: Methods WN18RR MRR ↑ \uparrow Hits@1 ↑ \uparrow Hits@3 ↑ \uparrow Hits@10 ↑ \uparrow TransE .232 .061 .366 .522 RotatE .476 .428 .492 .571 TuckER .470 .443 .526 .526 KG-BERT .216 .041 .302 .524 StAR .401 .243 .491 .709 KGLM .467 .330 .538 .741 GPT-3.5 - .212 - - Llama-2-13B - .315 - - KICGPT .549 .474 .585 .641 MKGL .552 .500 .577 .656 KGT .622 .524 .679 .811 Table 8: Additional results on WN18RR.

[109] h2: Instructions for reporting errors

[110] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[111] p: Tip: You can select the relevant text first, to include it in your report.

[112] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[113] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
