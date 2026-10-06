[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: RADAR: Reasoning as Discrimination with Aligned Representations for LLM-based Knowledge Graph Reasoning

[3] h6: Abstract

[4] p: Knowledge graph reasoning (KGR) infers missing facts, with recent advances increasingly harnessing the semantic priors and reasoning abilities of Large Language Models (LLMs). However, prevailing generative paradigms are prone to memorize surface-level co-occurrences rather than learning genuine relational semantics, limiting out-of-distribution generalization. To address this, we propose RADAR, which reformulates KGR from generative pattern matching to discriminative relational reasoning. We recast KGR as discriminative entity selection, where reinforcement learning enforces relative entity separability beyond token-likelihood imitation. Leveraging this separability, inference operates directly in representation space, ensuring consistency with the discriminative optimization and bypassing the generation-induced hallucinations. Across four benchmarks, RADAR achieves 5–6% relative gains on link prediction and triple classification over strong LLM baselines, while increasing task-relevant mutual information in intermediate representations by 62.9%, indicating more robust and transferable relational reasoning.

[5] h2: 1 Introduction

[6] p: Knowledge graphs (KGs) represent facts as structured triples and support applications such as semantic search and question answering Chen et al. (2020) ; Huang et al. (2019) ; Wang et al. (2024) . However, real-world KGs are inevitably incomplete, limiting their effectiveness in downstream use Shen et al. (2022b) . Knowledge graph reasoning (KGR) addresses this by inferring missing facts from observed triples. Classical embedding-based methods exploit graph structure effectively, but often struggle under sparsity and have limited capacity to express fine-grained relational semantics beyond local topology Pujara et al. (2017) ; Yao et al. (2019) . Consequently, recent work has shifted toward large language models (LLMs), harnessing their rich semantic priors and reasoning capabilities to mitigate these limitations Zhang et al. (2024b) ; Yao et al. (2025) ; Li et al. (2024b) ; Li et al. (2024a) .

[7] figure: Figure 1: FB15K-237N triple classification with a shared LLaMA backbone: co-occurrence-based SFT yields only marginal gains over the frozen baseline, whereas RADAR substantially improves accuracy by optimizing discriminative relational reasoning.

[8] figure: Figure 2: RADAR, a data-to-inference alignment framework for discriminative KGR.

[9] p: A central requirement of KGR is generalization : the ability to answer queries involving entity–relation combinations unseen during training Liu et al. (2021) ; Bordes et al. (2013) . Yet prevailing LLM-based paradigms formulate KGR as sequence modeling, optimizing next-token likelihood over serialized textual triples. This formulation encourages a shortcut: models minimize loss by exploiting surface co-occurrences between entity names and relations rather than learning relation-conditioned validity Zhang et al. (2024a) ; Kang and Choi (2023) ; Ju et al. (2024) . Such behavior yields strong in-distribution performance but fails under distribution shift where those co-occurrence statistics no longer hold. Crucially, this reliance on co-occurrence shortcuts is further exacerbated by supervised fine-tuning (SFT), as cross-entropy objectives reinforce token-level imitation over relational reasoning Chu et al. (2025) ; Lv et al. (2025) . As illustrated in Figure 1 , co-occurrence-based SFT yields only marginal gains over the frozen baseline, highlighting the necessity for a paradigm shift from generative pattern matching to relational reasoning.

[10] p: To address co-occurrence-driven shortcuts, we propose RADAR (Figure 2 ), which fundamentally shifts KGR from generative pattern matching to discriminative relational reasoning. By recasting KGR as discriminative entity selection, we redirect the learning signal from token-level imitation to the relative separability of ground truth against hard distractors, rendering co-occurrence shortcuts insufficient Si et al. (2022) . This reformulation pivots KGR from local token-level prediction to global entity discrimination within a discrete candidate space, where Reinforcement Learning (RL) naturally aligns with optimizing global discrete outcomes and effectively resolving the objective mismatch inherent in token-level SFT Chu et al. (2025) . Operationalizing this shift necessitates staged training, where RL exploits SFT-grounded structure to amplify reward-driven contrast between correct entities and distractors, transforming the objective from likelihood-based imitation to generalizable discrimination Lv et al. (2025) . As a consequence of optimizing for relative entity separability, relational information is encoded in discriminative latent representations rather than through autoregressive decoding Zou et al. (2023) . Accordingly, we perform inference directly in representation space, aligning inference with the discriminative signals induced during training and avoiding generation-induced hallucinations.

[11] p: Across four KGR benchmarks, RADAR consistently achieves an average 5–6% relative improvement over strong LLM-based baselines on link prediction and triple classification. Ablations show that the gains come from a tightly integrated design that aligns what the model is trained to optimize, what it is allowed to rely on, and what is ultimately extracted for reasoning. Furthermore, our proposed information-theoretic probe reveals that RADAR increases task-relevant mutual information in intermediate representations by 62.9% on average, consistent with improved inductive robustness and domain transfer. Our contributions are threefold:

[12] p: We expose co-occurrence shortcuts as a fundamental bottleneck in LLM-based KGR and recast KGR as a discriminative relational reasoning problem, moving beyond autoregressive pattern matching to achieve robust out-of-distribution generalization.

[13] p: We introduce RADAR, a data-to-inference alignment framework that restructures supervision, optimization, and inference around discrete entity separation, inducing relational semantics to emerge as discriminative structures within the representation space and bypassing surface-level co-occurrence shortcuts.

[14] p: Extensive evaluations across four benchmarks demonstrate superior performance over strong baselines, while information-theoretic quantification validates that RADAR substantially enhances task-relevant mutual information to achieve robust inductive generalization.

[15] h2: 2 Methods

[16] h3: 2.1 Setup

[17] p: A knowledge graph 𝒢 = { ℰ , ℛ , 𝒯 } \mathcal{G}=\{\mathcal{E},\mathcal{R},\mathcal{T}\} is a collection of an entity set ℰ \mathcal{E} , a relation set ℛ \mathcal{R} , and a triple set 𝒯 \mathcal{T} . Each triple is denoted as ( h , r , t ) ∈ 𝒯 (h,r,t)\in\mathcal{T} , where h , t ∈ ℰ h,t\in\mathcal{E} represent the entities and r ∈ ℛ r\in\mathcal{R} denotes the relation. Let ℓ ⁡ ( ⋅ ) \ell(\cdot) denote the function that maps each entity or relation to its textual sequence for LLM processing.

[18] p: In this work, we focus on two standard KGR tasks: triple classification and link prediction. Triple classification determines whether a triple ( h , r , t ) (h,r,t) is valid. Link prediction aims to identify the missing entity in an incomplete triple ( h , r , ? ) (h,r,?) .

[19] h3: 2.2 Task Reformulation for Discriminative Selection

[20] p: Prevailing generative paradigms Saxena et al. (2022) ; Yao et al. (2025) optimizing serialized triples (e.g., " ℓ ⁡ ( h ) \ell(h) ℓ ⁡ ( r ) \ell(r) ℓ ⁡ ( t ) \ell(t) ") inherently biases models toward minimizing loss via surface-level entity-relation co-occurrences rather than relational validity Kang and Choi (2023) ; Ju et al. (2024) . To redirect this bias, we recast KGR as discriminative entity selection within a constrained candidate space. This reformulation fundamentally alters the learning signal: the model is compelled to explicitly discriminate ground truth from distractors, thereby forcing the optimization trajectory toward inducing discriminative latent structures governed by relational validity, rendering co-occurrence shortcuts insufficient for objective minimization.

[21] p: Formally, given a query triple ( h , r , ? ) (h,r,?) , we define ℰ gt ​ ( h , r ) = { t ∣ ( h , r , t ) ∈ 𝒯 } \mathcal{E}_{\text{gt}}(h,r)=\{t\mid(h,r,t)\in\mathcal{T}\} as the ground-truth tail entity set. We construct a candidate set 𝒞 ⁡ ( h , r ) = { c 1 , c 2 , … , c K } \mathcal{C}(h,r)=\{c_{1},c_{2},\ldots,c_{K}\} , where 𝒞 ⁡ ( h , r ) = ℰ p ​ o ​ s ​ ( h , r ) ∪ ℰ n ​ e ​ g ​ ( h , r ) \mathcal{C}(h,r)=\mathcal{E}_{pos}(h,r)\cup\mathcal{E}_{neg}(h,r) , ℰ p ​ o ​ s ​ ( h , r ) ⊆ ℰ gt ​ ( h , r ) \mathcal{E}_{pos}(h,r)\subseteq\mathcal{E}_{\text{gt}}(h,r) denotes positive entities and ℰ n ​ e ​ g ​ ( h , r ) ⊂ ℰ ∖ ℰ gt ​ ( h , r ) \mathcal{E}_{neg}(h,r)\subset\mathcal{E}\setminus\mathcal{E}_{\text{gt}}(h,r) denotes negative entities. Each training instance is formatted as shown in Figure 3 .

[22] figure: Figure 3: Training prompt.

[23] p: The model is trained to output the option labels corresponding to entities in ℰ p ​ o ​ s ​ ( h , r ) \mathcal{E}_{pos}(h,r) .

[24] h4: Hierarchical Task Difficulty.

[25] p: To progressively challenge the model’s relational reasoning capabilities, we design a hierarchical framework along two dimensions: answer cardinality and negative sample hardness.

[26] p: For answer cardinality, we construct two task variants: (1) single-answer : | ℰ p ​ o ​ s ​ ( h , r ) | = 1 |\mathcal{E}_{pos}(h,r)|=1 ; (2) variable-answer : | ℰ p ​ o ​ s ​ ( h , r ) | ≥ 1 |\mathcal{E}_{pos}(h,r)|\geq 1 , where the number of correct entities is not given a priori, encompassing both one-to-one and one-to-many relations and requiring cardinality determination.

[27] p: For negative sample hardness, we stratify negative candidates based on their plausibility given the query. We use a pre-trained knowledge graph embedding (KGE) model to score all potential entities and partition ℰ n ​ e ​ g ​ ( h , r ) \mathcal{E}_{neg}(h,r) into three tiers based on plausibility. (1) Tier 1 (Easy) : lowest-scoring entities that are structurally implausible as tails for the query; (2) Tier 2 (Medium) : randomly sampled entities; (3) Tier 3 (Hard) : highest-scoring entities that are highly confusable with ground-truth answers, requiring fine-grained relational reasoning.

[28] h3: 2.3 Optimization for Discriminative Relational Reasoning

[29] p: To overcome the pattern matching, we develop a two-stage training paradigm tightly coupled with discrete entity selection formulation. While SFT grounds output structure, its cross-entropy objective inherently favors token-level imitation over relational reasoning Lv et al. (2025) . This mismatch necessitates RL, which pivots the learning signal from token likelihood to global outcome validity Chu et al. (2025) . Crucially, the reformulation in Section 2.2 yields explicit, verifiable rewards, enabling stable RL and promoting genuine relational discrimination over statistical mimicry.

[30] h4: Stage I: Supervised Fine-Tuning.

[31] p: We construct chain-of-thought (CoT) reasoning traces Wei et al. (2022) for each training instance, where each trace verifies semantic compatibility of candidate entities with the query ( h , r , ? ) (h,r,?) before producing the final answer set (see Appendix E for details). Given a training dataset 𝒟 train \mathcal{D}_{\text{train}} , where each instance consists of a discriminative prompt x x and a target sequence comprising the CoT reasoning and the final answer. The model is fine-tuned using the standard next-token prediction objective.

[32] h4: Stage II: Reinforcement Learning.

[33] p: We apply Group Relative Policy Optimization (GRPO) Shao et al. (2024) , leveraging group-normalized advantages for stable policy updates, to enhance generalization on challenging entity-relation compositions.

[34] p: Let y ^ \hat{y} denote the model output for input x x , and let 𝒜 ^ ​ ( y ^ ) ⊆ 𝒞 ​ ( h , r ) \hat{\mathcal{A}}(\hat{y})\subseteq\mathcal{C}(h,r) denote the set of entities extracted from y ^ \hat{y} . To amplify reasoning signals on instances where SFT fails, we construct an error-focused dataset 𝒟 error \mathcal{D}_{\text{error}} by evaluating the SFT model on 𝒟 train \mathcal{D}_{\text{train}} and retaining only instances where 𝒜 ^ ​ ( y ^ ) ≠ ℰ p ​ o ​ s ​ ( h , r ) \hat{\mathcal{A}}(\hat{y})\neq\mathcal{E}_{pos}(h,r) .

[35] p: To guide learning on 𝒟 error \mathcal{D}_{\text{error}} while accommodating variable-cardinality predictions, we define a composite reward R ⁡ ( x , y ^ ) R(x,\hat{y}) :

[36] table: R ⁡ ( x , y ^ ) = α ⋅ R fmt ​ ( y ^ ) + ( 1 − α ) ⋅ R acc ​ ( x , y ^ ) R(x,\hat{y})=\alpha\cdot R_{\text{fmt}}(\hat{y})+(1-\alpha)\cdot R_{\text{acc}}(x,\hat{y}) (1)

[37] p: where α \alpha is the weighting coefficient, R fmt ​ ( y ^ ) ∈ { 0 , 1 } R_{\text{fmt}}(\hat{y})\in\{0,1\} verifies format adherence, and R acc ​ ( x , y ^ ) R_{\text{acc}}(x,\hat{y}) measures answer accuracy. For each query ( h , r , ? ) (h,r,?) encoded in x x , the accuracy reward is:

[38] table: R acc ​ ( x , y ^ ) = 2 ⋅ | 𝒜 ^ ​ ( y ^ ) ∩ ℰ p ​ o ​ s ​ ( h , r ) | | 𝒜 ^ ​ ( y ^ ) | + | ℰ p ​ o ​ s ​ ( h , r ) | R_{\text{acc}}(x,\hat{y})=\frac{2\cdot|\hat{\mathcal{A}}(\hat{y})\cap\mathcal{E}_{pos}(h,r)|}{|\hat{\mathcal{A}}(\hat{y})|+|\mathcal{E}_{pos}(h,r)|} (2)

[39] p: This F1-based formulation provides credit assignment for partially correct predictions, which is essential for variable-answer instances. We optimize the policy to maximize the expected reward using GRPO, with details provided in Appendix E .

[40] h3: 2.4 Representation-based Inference

[41] p: By explicitly discriminating against distractors, the task reformulation and staged training shape the model’s internal representations toward relational separability. Autoregressive decoding evaluates relational plausibility indirectly through next-token likelihood, introducing a mismatch between token-level generation and the entity-level discriminative separability induced during training Zou et al. (2023) ; Orgad et al. (2024) . We therefore perform inference directly in representation space, enabling faithful extraction of discriminative relational knowledge and ensuring that the inference mechanism is intrinsically aligned with the discriminative learning signals optimized during training.

[42] p: For triple classification, we extract the model’s internal representations to assess triple plausibility. We construct prompt PT cls ​ ( h , r , t ) \text{PT}_{\text{cls}}(h,r,t) as follows:

[43] figure: Figure 4: Inference prompt.

[44] p: We extract the hidden state at the final token position from an intermediate layer l l , as intermediate representations have been shown to better preserve factual knowledge than final-layer outputs Skean et al. (2025) :

[45] table: 𝐳 ( l ) ​ ( h , r , t ) = ( LLM ( l ) ​ ( PT cls ​ ( h , r , t ) ) ) T , \mathbf{z}^{(l)}(h,r,t)=(\text{LLM}^{(l)}\left(\text{PT}_{\text{cls}}(h,r,t)\right))_{T}, (3)

[46] p: where 𝐳 ( l ) ​ ( h , r , t ) ∈ ℝ d \mathbf{z}^{(l)}(h,r,t)\in\mathbb{R}^{d} denotes the extracted hidden state, LLM ( l ) ​ ( ⋅ ) \text{LLM}^{(l)}(\cdot) represents output of the first l l layers of the fine-tuned model, ( ⋅ ) T (\cdot)_{T} extracts the representation at position T T (the final token), and d d is the hidden dimension.

[47] p: We then train a binary classifier f ϕ : ℝ d → [ 0 , 1 ] f_{\phi}:\mathbb{R}^{d}\to[0,1] that maps the extracted representation to a plausibility score s ⁡ ( h , r , t ) = f ϕ ​ ( 𝐳 ( l ) ​ ( h , r , t ) ) s(h,r,t)=f_{\phi}(\mathbf{z}^{(l)}(h,r,t)) . Training data consists of positive samples from ground-truth triples and negative samples constructed by corrupting tail entities Bordes et al. (2013) . We optimize f ϕ f_{\phi} using binary cross-entropy loss and implement f ϕ f_{\phi} as a two-layer MLP, which maps 𝐳 ( l ) \mathbf{z}^{(l)} through a hidden layer of dimension d v d_{v} to produce the binary classification score.

[48] p: For link prediction, where the goal is to identify the missing tail entity in ( h , r , ? ) (h,r,?) , we adopt a retrieval-then-reranking approach Li et al. (2025) . Given the large entity set size, exhaustively scoring all entities is computationally prohibitive. We therefore leverage a lightweight pre-trained KGE model to retrieve the top- n n structurally plausible candidates ( n ≪ | ℰ | n\ll|\mathcal{E}| ), then rerank them using our learned classifier f ϕ f_{\phi} . For each retrieved candidate e i e_{i} , we compute s ⁡ ( h , r , e i ) = f ϕ ​ ( 𝐳 ( l ) ​ ( h , r , e i ) ) s(h,r,e_{i})=f_{\phi}(\mathbf{z}^{(l)}(h,r,e_{i})) and rank candidates by this score.

[49] h3: 2.5 Task-Adaptive Information Quantification

[50] p: To quantify discriminative relational signals internalized during our reformulated KGR training, we propose a task-adaptive mutual information measure defined over internal representations 𝐳 ( l ) \mathbf{z}^{(l)} . While standard sliced mutual information (SMI) relies on random projections that treat all directions equally, this indiscriminate averaging can dilute task - relevant information in LLM representations Goldfeld and Greenewald (2021) ; Wongso et al. (2023) . In contrast, we derive projections from the learned probing classifier f ϕ f_{\phi} to target the most discriminative subspace, concentrating information estimation on directions that encode relational separability induced by discriminative KGR training.

[51] p: Since f ϕ f_{\phi} is optimized to distinguish valid triples, its weight matrix encodes discriminative directions in the representation space. For N N samples with representations 𝐙 ( l ) ∈ ℝ d × N \mathbf{Z}^{(l)}\in\mathbb{R}^{d\times N} , we define task-adaptive projections using the first layer of f ϕ f_{\phi} :

[52] table: 𝐕 = PReLU ​ ( 𝐖 1 ​ 𝐙 ( l ) + 𝐛 1 ) ∈ ℝ d v × N , \mathbf{V}=\text{PReLU}(\mathbf{W}_{1}\mathbf{Z}^{(l)}+\mathbf{b}_{1})\in\mathbb{R}^{d_{v}\times N}, (4)

[53] p: where 𝐖 1 ∈ ℝ d v × d \mathbf{W}_{1}\in\mathbb{R}^{d_{v}\times d} and 𝐛 1 ∈ ℝ d v \mathbf{b}_{1}\in\mathbb{R}^{d_{v}} are the trained parameters. Each row 𝐯 i ∈ ℝ N \mathbf{v}_{i}\in\mathbb{R}^{N} of 𝐕 \mathbf{V} corresponds to the representations projected onto a dimension optimized for KGR.

[54] p: Let Y ∈ { 0 , 1 } N Y\in\{0,1\}^{N} denote the ground-truth validity labels. We then quantify the task-specific information encoded in the representation space by averaging the mutual information between the projected feature activations and the labels:

[55] table: ℐ task = 1 d v ​ ∑ i = 1 d v I ^ ​ ( 𝐯 i , Y ) , \mathcal{I}_{\text{task}}=\frac{1}{d_{v}}\sum_{i=1}^{d_{v}}\hat{I}(\mathbf{v}_{i};Y), (5)

[56] p: where I ^ \hat{I} is mutual information computed via the KSG method Kraskov et al. (2004) . This metric quantifies the KGR-relevant information within the representations that is captured by the discriminative features of f ϕ f_{\phi} , enabling comparison across training strategies (details in Appendix D ).

[57] h2: 3 Experiment

[58] p: Our experiments address the following research questions: RQ1: Does RADAR achieve strong and consistent performance across standard KGR benchmarks and tasks? RQ2: How do the core design components of RADAR individually and synergistically contribute to performance and generalization? RQ3: Can RADAR achieve robust inductive generalization to unseen entities and transfer relational knowledge to domain-related tasks?

[59] h3: 3.1 Experiment Settings

[60] p: Datasets. We evaluate RADAR on four benchmarks across two tasks. For link prediction, we use FB15K-237 Schlichtkrull et al. (2018) and FB15K-237N Lv et al. (2022) . For triple classification, we employ WN18RR Dettmers et al. (2018) , UMLS Yao et al. (2019) , and FB15K-237N. Dataset details are provided in Appendix B .

[61] p: Baselines. We compare RADAR against two categories of baselines: 1) Knowledge Graph Embedding models, which map entities and relations into low-dimensional vector spaces, including TransE Bordes et al. (2013) , DistMult Yang et al. (2014) , ComplEx Trouillon et al. (2016) , RotatE Sun et al. (2019) , ConvE Dettmers et al. (2018) , and TuckER Balažević et al. (2019) . 2) Language Model-based methods, which leverage the textual semantics of KGs. These include KG-BERT Yao et al. (2019) , MTL-KGC Kim et al. (2020) , KG-S2S Chen et al. (2022a) , SimKGC Wang et al. (2022) , iGT Luo et al. (2025) , CSPromp-KG Chen et al. (2023) , COSIGN Li et al. (2024b) , KG-LLAMA Yao et al. (2025) , CD Li et al. (2024a) , LLAMA-ICL, Structure IT, KoPA Zhang et al. (2024b) and FLAME Xue et al. (2024) . Among these, KG-LLAMA and FLAME are the most directly comparable baselines because they rely solely on LLaMA’s intrinsic capabilities without external structural embeddings, in contrast to hybrid approaches such as KoPA. Further details on these baselines are provided in Section A .

[62] p: Evaluation Metrics. For link prediction, we report the Mean Reciprocal Rank (MRR) and Hits@ k k ( k = 1 , 3 , 10 k=1,3,10 ) following standard protocols.

[63] p: Implementation Details. Unless otherwise noted, we adopt the variable-answer setting with Tier 2 negative sampling (random negatives) for all experiments. To ensure fair comparison with KG-LLAMA and FLAME, we adopt LLaMA Touvron et al. (2023) as the backbone model across all configurations. For link prediction inference and negative sample stratification in data construction (Section 2.2 ), we employ TuckER Balažević et al. (2019) as the KGE model to score candidate entities. Additional implementation details are provided in Appendix C .

[64] figure: Table 1: Link prediction performance (MRR and Hits@k) on FB15K-237 and FB15K-237N. Best scores are in bold and second-best are underlined . Paradigm Model FB15K-237 FB15K-237N MRR H@1 H@3 H@10 MRR H@1 H@3 H@10 Embedding -based TransE 0.279 0.198 0.376 0.441 0.255 0.152 0.301 0.459 DistMult 0.281 0.199 0.301 0.446 0.209 0.143 0.234 0.330 ComplEx 0.278 0.194 0.297 0.450 0.249 0.180 0.276 0.380 RotatE 0.338 0.241 0.375 0.533 0.279 0.177 0.320 0.481 ConvE 0.312 0.225 0.341 0.497 0.273 0.192 0.305 0.429 TuckER 0.347 0.253 0.382 0.536 0.301 0.217 0.332 0.463 Language Model -based KG-BERT 0.237 0.169 0.260 0.427 0.203 0.139 0.201 0.403 MTL-KGC 0.267 0.172 0.298 0.458 0.241 0.160 0.284 0.430 SimKGC 0.333 0.246 0.362 0.510 0.372 0.289 0.402 0.534 KG-S2S 0.336 0.257 0.373 0.498 0.353 0.282 0.385 0.495 CSPromp-KG 0.358 0.269 0.393 0.538 0.360 0.281 0.395 0.511 CD – – – – 0.372 0.288 0.410 0.530 COSIGN 0.368 0.315 0.434 0.520 0.394 0.355 0.457 0.526 KG-LLAMA 0.238 0.165 0.272 0.423 – – – – RADAR 0.377 0.273 0.421 0.579 0.415 0.301 0.476 0.633

[65] figure: Table 2: Triple classification accuracy on WN18RR, FB15K-237N, and UMLS. Best scores are in bold and second-best are underlined . Paradigm Model WN18RR FB15K-237N UMLS Embedding -based TransE 88.4 69.7 84.5 DistMult 85.1 58.7 86.4 ComplEx 84.1 65.7 87.1 RotatE 88.2 68.5 87.7 Language Model -based KG-BERT 91.6 56.0 77.3 LLAMA-ICL 50.2 59.2 55.5 KG-LLAMA 92.1 74.8 85.8 Structure IT 92.7 76.4 89.9 FLAME 93.8 74.4 86.6 KoPA 94.9 77.7 92.6 RADAR 95.3 81.6 91.7

[66] h3: 3.2 Main Results (RQ1)

[67] p: Table 1 reports link prediction results of RADAR on FB15K-237 and FB15K-237N. Specifically, RADAR attains the best MRR across both datasets, outperforming all KGE-based and language model-based baselines, while ranking first or second on all Hits@k metrics. On FB15K-237, RADAR reaches an MRR of 0.377, corresponding to a 2.4% relative improvement over the previous best model COSIGN. Notably, RADAR demonstrates substantial improvements on the more challenging FB15K-237N dataset, achieving a 5.3% improvement in MRR over COSIGN.

[68] p: To complement link prediction, we further evaluate triple classification on WN18RR, FB15K-237N, and UMLS as shown in Table 2 . RADAR achieves the best accuracy on WN18RR and FB15K-237N, and is second on UMLS (91.7%), slightly below KoPA (92.6%). KoPA leverages external structural embeddings, whereas RADAR operates in the LLM-only setting. Focusing on the LLM-only setting with the same LLaMA backbone, RADAR substantially improves over KG-LLAMA and FLAME, yielding an average relative gain of 6.1% and 5.7% across the three datasets, respectively, suggesting reduced reliance on entity–relation co-occurrence shortcuts and stronger generalization in LLaMA-based KGR.

[69] figure: Table 3: Triple classification accuracy on FB15K-237N under controlled ablations of task difficulty: answer cardinality and negative hardness. Answer Cardinality Negative Hardness (Fixing Negatives: Tier 2) (Fixing Cardinality: Variable) Setting Accuracy Setting Accuracy Single-answer 79.9 Tier 1 (Easy) 80.2 Variable-answer 81.6 Tier 2 (Medium) 81.6 Tier 3 (Hard) 81.0

[70] p: Finally, Table 3 studies task variants on FB15K-237N by varying answer cardinality and negative hardness. The variable-answer setting performs better than single-answer, suggesting that exposing multiple correct tails for one-to-many relations provides richer supervision for relation-conditioned discrimination. Under the variable-answer setting, Tier-2 is marginally better than Tier-3 and Tier 1, and overall performance differences across tiers remain small, motivating our default choice of Tier-2 in subsequent experiments. See Appendix F for further analysis on negative hardness.

[71] p: Taken together, these results show that RADAR delivers consistent gains across link prediction and triple classification under a unified discriminative training-and-inference pipeline, outperforming prior LLM-only baselines while remaining competitive against methods that explicitly fuse KG structural embeddings.

[72] h3: 3.3 Ablation Results (RQ2)

[73] p: We ablate RADAR along three axes—data formulation (serialization vs. discrimination), training objective (sft vs. two-stage training), and inference (generation vs. representation extraction)—using four variants named by Data–Train–Infer . Serial-SFT-Generation follows the KG-LLaMA-style generative setup, fine-tuning on serialized triples (e.g., Is this true: ℓ ⁡ ( h ) ​ ℓ ​ ( r ) ​ ℓ ​ ( t ) \ell(h)\ \ell(r)\ \ell(t) ?). Serial-SFT-Extraction keeps the same serialized SFT setup but replaces decoding with representation extraction-based inference (Section 2.4 ), isolating the effect of inference. Discriminative-SFT-Extraction replaces serialization with the discriminative candidate-selection formulation (Section 2.2 ), which reduces entity–relation co-occurrence shortcuts while keeping SFT-only training and extraction inference, isolating the impact of task formulation. Discriminative-Full-Extraction represents our full framework with discriminative formulation, two-stage full training (Section 2.3 ), and extraction inference, isolating the effect of two-stage training.

[74] figure: Table 4: Ablation across task formulation, training objective, and inference strategy on triple classification accuracy (WN18RR, FB15k-237N, UMLS). Method WN18RR 15K-237N UMLS Serial-SFT-Generation 0.921 0.748 0.858 Serial-SFT-Extraction 0.925 0.753 0.861 Discriminative-SFT-Extraction 0.945 0.793 0.898 Discriminative-Full-Extraction 0.953 0.816 0.917

[75] p: Table 4 quantifies the contribution of each design axis in RADAR. First, replacing autoregressive decoding with representation-based inference ( Serial-SFT-Extraction ) yields consistent gains over generation ( Serial-SFT-Generation ), suggesting that internal representations capture relational information more reliably than autoregressive outputs. Second, reformulating KGR as a discriminative task leads to substantial performance improvements. Specifically, Discriminative-SFT-Extraction improves over Serial-SFT-Extraction by an average of 3.9% across benchmarks. These improvements align with our hypothesis that the discriminative formulation mitigates entity–relation co-occurrence shortcuts and promotes reasoning over relational semantics. Incorporating RL refinement yields further gains, with Discriminative-Full-Extraction achieving an average relative improvement of 6.5% over the standard serial SFT generation baseline. Together, these results show that effective relational reasoning in LLM-based KGR requires a tightly integrated design across task formulation, optimization, and inference. In this system, outcome-based optimization does not merely refine supervised learning, but works in concert with the discriminative setup and representation-based inference to resolve non-trivial challenges in aligning what the model is trained to optimize, what it is allowed to rely on, and what knowledge is ultimately extracted for reasoning.

[76] figure: Figure 5: Task-Adaptive SMI of intermediate representations across different methods on WN18RR.

[77] p: To better interpret the performance gains observed in the ablation study, we measure how each design choice affects the amount of KGR-relevant information encoded in intermediate representations using task-adaptive mutual information ℐ task \mathcal{I}_{\text{task}} . As shown in Figure 7 , RADAR yields a 62.9% average relative increase in ℐ task \mathcal{I}_{\text{task}} over the serialized SFT baseline on WN18RR (please refer to Appendix D for corresponding analyses on other datasets). Discriminative reformulation establishes a representation space suitable for relational discrimination, while reinforcement learning further aligns this space with outcome-level relational correctness beyond supervised likelihood. Together, these results indicate that the gains of RADAR stem from systematic changes in how task-relevant information is organized in the representation space.

[78] figure: Table 5: Link prediction performance on FB15K-237N across different LLM backbones. Method MRR H@1 H@3 H@10 LLaMA-7B Touvron et al. (2023) Serial-SFT-Extraction 0.365 0.229 0.438 0.584 Discriminative-Full-Extraction 0.415 0.301 0.476 0.633 Pythia-6.9B Biderman et al. (2023) Serial-SFT-Extraction 0.353 0.259 0.401 0.616 Discriminative-Full-Extraction 0.384 0.267 0.437 0.635 Qwen3-8B Yang et al. (2025) Serial-SFT-Extraction 0.402 0.287 0.442 0.622 Discriminative-Full-Extraction 0.426 0.312 0.499 0.641

[79] p: We evaluate the architectural robustness of RADAR by examining whether its relative improvements are preserved across diverse LLM backbones. As shown in Table 5 , RADAR consistently outperforms the corresponding Serial-SFT-Extraction baselines across all evaluated architectures. Specifically, on Qwen3-8B, RADAR yields an relative improvement of 6.0% in MRR and 8.7% in Hits@1 over the Serial-SFT-Extraction baseline. These results indicate that RADAR is robust to backbone choice, yielding consistent performance improvements across diverse LLM architectures.

[80] h3: 3.4 Additional Results (RQ3)

[81] figure: Figure 6: Inductive generalization performance for triple classification on WN18RR under varying inductive rates (IR). We report accuracy on seen (S), unseen (U), and overall (A) test triples.

[82] p: We evaluate inductive generalization under an entity-disjoint setting in which a subset of entities is completely excluded from training, directly testing the model’s ability to reason beyond observed entity identities Teru et al. (2020) . Following Chen et al. (2022b) , we define an inductive rate (IR) as the proportion of entities excluded from training. Given IR= ρ \rho , a fraction ρ \rho of entities is designated as inductive, and all training triples involving them are removed. We stratify test triples into seen (S) where all entities appeared in the training set, unseen (U) involving at least one inductive entity, and (A) denoting the aggregate set. This setting presents a stringent generalization challenge, as inductive entities are never observed during training.

[83] p: Discriminative-Full-Extraction consistently outperforms the Serial-SFT baseline across all inductive rates, with particularly pronounced gains on unseen triples. At IR=40%, the baseline exhibits a sharp degradation on unseen triples, while our method remains substantially more stable. This gap supports our hypothesis that serialization-based SFT encourages reliance on entity co-occurrence statistics, which fails when such correlations are unavailable. In contrast, RADAR encourages the model to internalize relation-conditioned distinction patterns that are decoupled from specific entity identities. As a result, the learned relational criteria can be consistently applied to unseen entities at inference time, indicating that the components interact in a principled and complementary manner rather than functioning as isolated heuristics.

[84] p: To evaluate whether knowledge learned through KGR generalizes beyond the training task, we conduct zero-shot evaluations on MMLU Hendrycks et al. (2020) subjects aligned with the UMLS domain, following the protocol of Zhang et al. (2024b) . As shown in Table 6 , KGR training on UMLS leads to an average performance gain of 11.6% across five subjects. These gains suggest that our KGR training encourages relation-conditioned and compositional reasoning that generalizes to domain-adjacent tasks, rather than reliance on memorized triples.

[85] figure: Table 6: Zero-shot performance on domain-aligned MMLU subjects after UMLS-based KGR training. Subjects w/o Training w/ Training Clinical 0.340 0.455 College Medicine 0.341 0.397 High School Biology 0.313 0.439 High School Chemistry 0.271 0.355 Medical Genetics 0.290 0.490

[86] h2: 4 Conclusion

[87] p: In this work, we introduce RADAR, a framework that fundamentally realigns LLM-based KGR from autoregressive pattern matching to discriminative relational reasoning. By unifying task reformulation, optimization, and inference toward discriminative entity selection, our approach suppresses memorization of surface statistics in favor of robust relational semantics. Validated by information-theoretic analysis and extensive benchmarks, RADAR not only achieves superior generalization but also establishes a principled route to more reliable and generalizable KGR with LLMs.

[88] h2: 5 Limitations

[89] p: To balance large-scale inference efficiency, RADAR adopts a retrieve-then-rerank paradigm, introducing an inherent recall bottleneck. Additionally, our discriminative alignment via reinforcement learning incurs higher training costs than standard fine-tuning. Future work will focus on optimizing training efficiency and exploring retriever-free LLM reasoning mechanisms.

[90] h2: References

[91] h2: Appendix A Related Work

[92] p: Knowledge graph reasoning aims to infer missing triples from incomplete KGs Tang et al. (2024) . Classical methods learn embedding-based scoring functions over graph topology, including translational models (e.g., TransE Bordes et al. (2013) , RotatE Sun et al. (2019) ), semantic matching models (e.g., DistMult Yang et al. (2014) , ComplEx Trouillon et al. (2016) , TuckER Balažević et al. (2019) ), and convolutional models (e.g., ConvE Dettmers et al. (2018) ). While effective at capturing local structural patterns, these methods struggle with data sparsity.

[93] p: Language model-based methods address these limitations by incorporating textual semantics. Early encoder-only approaches, including KG-BERT Yao et al. (2019) and LASS Shen et al. (2022a) , reformulate KGC as sequence classification. Later work enhances this paradigm through multi-task learning Kim et al. (2020) and contrastive objectives Wang et al. (2022) . Generative methods such as KG-S2S Chen et al. (2022a) and KGT5 Saxena et al. (2022) adopt generative paradigms with encoder-decoder architectures. CSProm-KG Chen et al. (2023) introduces conditional soft prompts to balance structural and textual knowledge. Recent advances leverage decoder-only LLMs for KGC. KoPA Zhang et al. (2024b) combines structural embeddings with Alpaca for triple classification, KG-LLAMA Yao et al. (2025) frames KGR as instruction-following question answering with parameter-efficient fine-tuning and FLAME leverages frozen LLM representations with task-specific KGC classifiers.

[94] p: However, existing LM-based methods primarily rely on supervised fine-tuning over data with explicit entity-relation co-occurrences, which biases models toward memorizing surface-level statistical patterns rather than relational reasoning. In contrast, RADAR co-designs the task formulation, training objective, and inference mechanism to prioritize generalization over surface-form memorization in KGR.

[95] h2: Appendix B Datasets and Metrics Details

[96] figure: Table 7: Dataset statistics. Dataset | ℰ | |\mathbf{\mathcal{E}}| | ℛ | |\mathbf{\mathcal{R}}| # Train # Valid # Test FB15K-237 14,541 237 272,115 17,535 20,466 FB15K-237N 13,104 93 87,282 7,041 8,226 WN18RR 40,943 11 86,835 6,068 6,268 UMLS 135 46 5,216 1,304 1,322

[97] p: We evaluate the performance of RADAR on four benchmark datasets, covering two distinct tasks: link prediction and triple classification. The statistics of these datasets are summarized in Table 7 . For link prediction, we utilize FB15K-237, a subset of Freebase with inverse relations removed to prevent data leakage, and FB15K-237N, a modified version that removes mediator nodes and introduces hard negatives to increase difficulty. For triple classification, we employ WN18RR, a subset of WordNet derived from WN18 by removing inverse relations; UMLS, a medical semantic network consisting of biomedical concepts and their semantic relations; and the aforementioned FB15K-237N.

[98] p: For link prediction, we report the Mean Reciprocal Rank (MRR) and Hits@ k k ( k = 1 , 3 , 10 k=1,3,10 ) following standard protocols. MRR is the average of the reciprocal ranks of the correct entities, while Hits@ k k measures the proportion of correct entities ranked in the top- k k . For triple classification, we report accuracy. To ensure a fair evaluation, the test sets for triple classification are constructed with an equal number of positive and negative triples.

[99] h2: Appendix C Additional Implementation Details

[100] p: For each query ( h , r , ? ) (h,r,?) , we construct a discriminative candidate set 𝒞 ⁡ ( h , r ) \mathcal{C}(h,r) with a fixed size of K = 4 K=4 , containing both positive and negative tail entities as described in Section 2.2 .

[101] p: Entity descriptions are sourced from Xie et al. (2016) for FB15K-237 and FB15K-237N, synset definitions from Yao et al. (2019) for WN18RR, and the original dataset for UMLS. Both Stage I SFT and Stage II GRPO are implemented using LoRA for parameter-efficient fine-tuning, with all backbone parameters kept frozen. For representation-based inference, we consistently extract hidden states from an intermediate layer with index l = 15 l=15 , following prior work showing that intermediate representations better preserve relational knowledge.

[102] p: For link prediction, exhaustively scoring the entire entity set ℰ \mathcal{E} is computationally prohibitive for LLMs. We therefore adopt a retrieve-then-rerank strategy Li et al. (2025) ; Wei et al. (2024) , utilizing a lightweight pre-trained TuckER model to retrieve the top- n = 15 n=15 candidates, which are subsequently reranked by our learned classifier. For MRR calculation, should the ground truth entity fall outside this retrieved top- n n set, we use the rank provided by the retriever. While this imposes a recall bottleneck, it balances large-scale inference efficiency with precision, offering a more rigorous evaluation than ranking against randomly sampled negatives Yao et al. (2025) . Crucially, this reliance on retrieval is exclusive to link prediction task. Our triple classification results (Table 2 ) and the core analytical experiments in Section 3 are conducted without retrieval, directly validating the intrinsic discriminative reasoning capabilities of RADAR.

[103] figure: Table 8: Link classification performance on FB15K-237N under varying parameter n n . Parameter n n MRR 15 0.415 20 0.402 25 0.393

[104] h2: Appendix D Additional Details on Task-Adaptive Information Quantification

[105] p: Section 2.5 introduces a task-adaptive mutual information metric for quantifying how much KGR-relevant signal is encoded in intermediate representations. Here we provide additional motivation for this design and explain why standard SMI may be suboptimal in our setting.

[106] p: Standard SMI approximates I ⁡ ( X , Y ) I(X;Y) by averaging mutual information over random one-dimensional projections. However, in LLM representations, task-relevant information often concentrates in low-dimensional subspaces Hu et al. (2022) , and random projections dilute this signal by uniformly sampling directions regardless of their informativeness. This leads to noisier estimates with weaker task alignment. Moreover, restricting to linear projections can be suboptimal when the relevant structure is expressed through nonlinear feature interactions.

[107] p: To address these limitations, We leverage the trained probe f ϕ f_{\phi} (Section 2.4 ) to define task-aligned projections. Given N N samples with representations 𝐙 ( l ) ∈ ℝ d × N \mathbf{Z}^{(l)}\in\mathbb{R}^{d\times N} , we compute the probe’s first-layer activations:

[108] table: 𝐕 = PReLU ​ ( 𝐖 1 ​ 𝐙 ( l ) + 𝐛 1 ) ∈ ℝ d v × N , \mathbf{V}=\text{PReLU}(\mathbf{W}_{1}\mathbf{Z}^{(l)}+\mathbf{b}_{1})\in\mathbb{R}^{d_{v}\times N}, (6)

[109] p: where 𝐖 1 ∈ ℝ d v × d \mathbf{W}_{1}\in\mathbb{R}^{d_{v}\times d} is the learned weight matrix, 𝐛 1 ∈ ℝ d v \mathbf{b}_{1}\in\mathbb{R}^{d_{v}} is the bias vector (with broadcasting across samples), and 𝐕 ∈ ℝ d v × N \mathbf{V}\in\mathbb{R}^{d_{v}\times N} is the matrix of transformed hidden representations. Crucially, since 𝐖 1 \mathbf{W}_{1} is optimized via supervised learning to minimize classification loss on KGR, each row of 𝐖 1 \mathbf{W}_{1} defines a projection direction that is implicitly optimized for label discriminability.

[110] p: This learned transformation differs from random projections in two respects. First, the PReLU nonlinearity enables modeling of nonlinear feature interactions inherent to contextualized embeddings. Second, supervised optimization shapes 𝐖 1 \mathbf{W}_{1} to emphasize label-informative subspaces while suppressing task-irrelevant dimensions. As a result, the hidden layer of f ϕ f_{\phi} defines a compact, task-aligned projection space that preserves KGR-relevant information, leading to more focused and better aligned mutual information estimates than random projections.

[111] figure: Figure 7: Task-Adaptive SMI of intermediate representations across different methods on FB15K-237N.

[112] h2: Appendix E Additional Details on Training

[113] h4: Stage I: Supervised Fine-Tuning.

[114] p: In Stage I, we perform supervised fine-tuning using structured CoT rationales to guide relational reasoning. For each entity, we use a long-form textual description d ⁡ ( ⋅ ) d(\cdot) . Prompts are constructed using a fixed template that presents the semantics of the head entity and all candidate entities, followed by the answer selection instruction. The prompts are shown in Figure 8 :

[115] figure: Figure 8: COT prompt.

[116] p: Formally, given a training dataset 𝒟 train \mathcal{D}_{\text{train}} , where each instance consists of a discriminative prompt x x constructed from ( h , r , 𝒞 ⁡ ( h , r ) ) (h,r,\mathcal{C}(h,r)) and a target sequence y y comprising the CoT reasoning and the final answer. We optimize the model parameters θ \theta using the standard next-token prediction objective:

[117] table: ℒ SFT = − 𝔼 ( x , y ) ∼ 𝒟 train ​ [ ∑ t = 1 | y | log ⁡ p θ ​ ( y t ∣ x , y < t ) ] \mathcal{L}_{\text{SFT}}=-\mathbb{E}_{(x,y)\sim\mathcal{D}_{\text{train}}}\left[\sum_{t=1}^{|y|}\log p_{\theta}(y_{t}\mid x,y_{<t})\right] (7)

[118] h4: Stage II: Reinforcement Learning.

[119] p: We optimize the policy using GRPO, which updates the model by comparing the relative quality of sampled responses for each input. For each query, the model samples a group of G G candidate responses { y ^ i } i = 1 G \{\hat{y}_{i}\}_{i=1}^{G} , each scored by R ⁡ ( x , y ^ i ) R(x,\hat{y}_{i}) . Rewards are normalized within each group to compute advantages that guide policy updates. The objective is:

[120] table: 𝒥 GRPO ​ ( θ ) = \displaystyle\mathcal{J}_{\text{GRPO}}(\theta)= 𝔼 x ∼ 𝒟 error , { y ^ i } ∼ π θ old [ 1 G ∑ i = 1 G L i c ​ l ​ i ​ p \displaystyle\mathbb{E}_{x\sim\mathcal{D}_{\text{error}},\{\hat{y}_{i}\}\sim\pi_{\theta_{\text{old}}}}\Bigg[\frac{1}{G}\sum_{i=1}^{G}L_{i}^{clip} (8) − β 𝔻 KL ( π θ | | π ref ) ] , \displaystyle-\beta\,\mathbb{D}_{\text{KL}}(\pi_{\theta}\,||\,\pi_{\text{ref}})\Bigg],

[121] table: L i c ​ l ​ i ​ p = min ⁡ ( w i ​ A i , clip ​ ( w i , 1 − ϵ , 1 + ϵ ) ​ A i ) , L_{i}^{clip}=\min\left(w_{i}A_{i},\text{clip}(w_{i},1-\epsilon,1+\epsilon)A_{i}\right), (9)

[122] p: where w i = π θ ​ ( y ^ i ∣ x ) π θ old ​ ( y ^ i ∣ x ) w_{i}=\frac{\pi_{\theta}(\hat{y}_{i}\mid x)}{\pi_{\theta_{\text{old}}}(\hat{y}_{i}\mid x)} , π θ old \pi_{\theta_{\text{old}}} is the policy before the update, π ref \pi_{\text{ref}} is the reference policy (the initial SFT model), ϵ \epsilon and β \beta are hyperparameters controlling update clipping and KL regularization, and A i A_{i} denotes the normalized advantage of each candidate within its group based on the reward R ⁡ ( x , y ^ i ) R(x,\hat{y}_{i}) .

[123] h2: Appendix F Additional Ablation Results

[124] figure: Figure 9: Layer-wise triple classification accuracy of RADAR across datasets. The horizontal axis denotes the layer depth in LLaMA, and the vertical axis corresponds to different datasets.

[125] p: Figure 9 shows that as the layer depth increases, the effectiveness of hidden states for triple classification exhibits a unimodal trend, with performance first improving and then degrading. Hidden states from intermediate and upper layers generally yield higher prediction accuracy than those from lower layers. This observation is consistent with prior findings Geva et al. (2020) , which show that Transformer-based language models encode knowledge hierarchically across layers, with higher layers progressively integrating information from lower-level representations. During pretraining, the lower layers may not have stored certain knowledge, thus failing to produce hidden states informative for triple classification. Furthermore, layers closest to the output head tend to underperform relative to middle layers in triple classification accuracy. This phenomenon may be attributed to the capacity of intermediate layers to strike an optimal balance between semantic abstraction and information retention. While lower layers contain raw input noise and upper layers converge toward generic token-prediction objectives, intermediate layers distill task-salient features that are most conducive to discriminative relational reasoning Jiang et al. (2024) ; Zou et al. (2023) .

[126] figure: Table 9: Triple classification accuracy on UMLS under varying parameter K K of Discriminative-SFT-Extraction. The best result is highlighted in bold. Parameter K K Accuracy 3 0.892 4 0.898 5 0.887 6 0.893

[127] p: Finally, we investigate the impact of the candidate set size K K in Table 9 . While increasing K K raises task difficulty—potentially necessitating more robust representations to distinguish the ground truth from a larger pool of distractors—we observe that performance peaks at K = 4 K=4 and subsequently plateaus. This phenomenon parallels our findings on negative hardness in Table 3 , where escalating difficulty from Tier 2 (Medium) to Tier 3 (Hard) yields no significant performance gain.

[128] p: These results collectively suggest that the primary driver of our method’s effectiveness is not the severity of the classification task, but the mechanism of discrimination itself. The critical factor is the paradigm shift: by constraining the LLM to select among discrete options, we successfully sever the reliance on generative co-occurrence shortcuts and force the activation of relational reasoning circuits. Once this discriminative mode is engaged, the model learns to isolate relational semantics; further increasing the complexity of the candidate space (via larger K K or harder negatives) offers diminishing returns and may introduce optimization noise rather than stronger learning signals.

[129] h2: Instructions for reporting errors

[130] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[131] p: Tip: You can select the relevant text first, to include it in your report.

[132] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[133] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
