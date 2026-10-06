[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Towards Dynamic Dense Retrieval with Routing Strategy

[3] h6: Abstract.

[4] p: The de facto paradigm for applying dense retrieval (DR) to new tasks involves fine-tuning a pre-trained model for a specific task. However, this paradigm has two significant limitations: (1) It is difficult adapt the DR to a new domain if the training dataset is limited. (2) Old DR models are simply replaced by newer models that are trained from scratch when the former are no longer up to date. Especially for scenarios where the model needs to be updated frequently, this paradigm is prohibitively expensive. To address these challenges, we propose a novel dense retrieval approach, termed dynamic dense retrieval (DDR). DDR uses prefix tuning as a module specialized for a specific domain. These modules can then be compositional combined with a dynamic routing strategy, enabling highly flexible domain adaptation in the retrieval part. Extensive evaluation on six zero-shot downstream tasks demonstrates that this approach can surpass DR while utilizing only 2% of the training parameters, paving the way to achieve more flexible dense retrieval in IR. We see it as a promising future direction for applying dense retrieval to various tasks.

[5] h6: Keywords:

[6] h2: 1. Introduction

[7] p: Dense retrieval approaches have shown remarkable capabilities, representing a notable advancement from classical retrieval methods ( Karpukhin et al., 2020b ; Lin et al., 2020 ; Qu et al., 2020 ; Zhao et al., 2024 ; Mo et al., 2024 ; Xiong et al., 2020 ) to neural retrieval ( Gao and Callan, 2021a ) . By embedding queries and documents into a latent vector space using dual-encoders, dense retrieval methods have demonstrated remarkable success in tasks such as web search ( Kim, 2022 ) , question answering ( Karpukhin et al., 2020b ) , and recommendation systems ( Huang et al., 2024 ) . In web search, DR has enhanced the ability of search engines to deliver more relevant results by understanding the intent behind user queries ( Zhu et al., 2021 ) . In question answering, DR bridges the semantic gap between queries and candidate answers by embedding both into a shared semantic space, allowing for more accurate retrieval of contextually relevant information ( Karpukhin et al., 2020a ; Roy and Anand, 2022 ; Huang et al., 2024 ) .

[8] p: Despite their success, current DR approaches still face two challenges: (1) Once DR models are trained and fixed, it is difficult to adapt them to a new domain when training data is limited. A common approach is to build domain-specific datasets and fine-tune the retriever on them ( Zhao et al., 2024 ) . However, collecting and annotating such data is often difficult and expensive. (2) In scenarios where dense retrieval models need frequent updates, older models are often replaced by new models trained from scratch. This wastes significant training resources. These two challenges lead to a natural question: Can we develop a dynamic dense retrieval approach that can adapt to new domains quickly while fully leveraging previously trained models?

[9] p: To answer this question, we propose dynamic dense retrieval (DDR) with a fine-grained routing function. In this approach, we use prefix tuning ( Li and Liang, 2021 ) to adapt dense retrieval models to new domains efficiently. Prefix tuning prepends l l trainable prefix vectors to the pre-trained model. During training, the parameters of the backbone remain frozen, and only the parameters associated with the prefix vectors are updated. We treat each prefix vector as an module specialized in a specific domain (§ 4.1 ). Then a routing function can dynamically select which module should be activated in the retrieval part (§ 4.2 ). This approach enables rapid adaptation to new tasks, domains, or emerging topics without requiring training from scratch. In addition, DDR can leverage previously trained modules for new tasks, rather than simply discarding old dense retrieval models, thereby significantly reducing training cost and improving knowledge reuse.

[10] p: We evaluate DDR on downstream retrieval tasks that require domain composition. The experimental results demonstrate that DDR can surpass traditional dense retrieval models while utilizing only 2% of training parameters.

[11] p: To sum up, our contributions are as follows:

[12] p: We formally introduce a new dense retrieval approach: Dynamic dense retrieval , converting dense models into modular models in the field of information retrieval. DDR addresses the limitations of traditional dense retrieval systems by offering flexibility, scalability, and efficiency.

[13] p: We propose fine-grained routing strategies, which dynamically activate the prefix vectors during retrieval, resulting in a dynamic dense retrieval system capable of adapting to new tasks.

[14] p: The experimental results indicate that DDR can surpass the traditional DR while only using 2% training parameters. Meanwhile, the DDR can leverage the previously trained modules for new tasks and avoid discarding old dense retrieval models, thereby reducing training cost and improving knowledge reuse. The code is released: 1 1 1 https://anonymous.4open.science/r/REMOP-sigir2026-short/README.md

[15] figure: Figure 1. Overview of DDR framework, built upon a dual-encoder architecture. The general prefix vector learns the general knowledge across tasks, while the domain prefix focuses on the specificity of each task domain. The frozen backbone incorporates both the general prefix and aspect prefix for query encoding, whereas the passage encoder only utilizes the general prefix.

[16] h2: 2. Related Work

[17] p: Dense Retrieval (DR) models convert queries and documents into dense embeddings through which documents are selected ( Peng et al., 2025 ; Zhan et al., 2021 ; Kong et al., 2022 ; Zhao et al., 2024 ; Lin et al., 2023 ; Ma et al., 2024 ; Izacard et al., 2021 ; Chen et al., 2022 ) . The dense passage retrieval (DPR) model employs a two-tower architecture based on BERT to encode the query and document separately ( Karpukhin et al., 2020a ) . Colbert ( Khattab and Zaharia, 2020 ) utilizes one BERT encoder by concatenating the query and the document as the input, and outputs a similarity score. ANCE ( Xiong et al., 2020 ) is a bi-encoder trained on (query, positive document, negative document) tuples where the negative document is retrieved from an ANN built on the checkpoint of the last step. Contriever ( Izacard et al., 2022 ) trains a bi-encoder model through contrastive learning. CoCondenser ( Gao and Callan, 2021b ) introduces a novel pre-training architecture, which learns to condense information into a dense vector through LM pre-training. Ma, Xueguang, et al. ( Ma et al., 2024 ) finetune an open-source LLaMA-2 model as a dense retriever. However, both dense retrieval models have been trained independently from scratch. For a new task or domain, one needs to retrain a new model with domain-specific data. There are no principled methods capable of combining them in a flexible way to take advantage of different models’ capabilities. Our contribution precisely lies in a new paradigm to enhance the flexibility of dense retrieval by combining the available models.

[18] h2: 3. Preliminary

[19] h3: 3.1. Prefix Tuning

[20] p: Multi-head attention performs the attention function in N h N_{h} heads, where each head is separately parametrized by ( w q ( i ) , w k ( i ) , w v ( i ) ∈ ℝ d × d h w_{q}^{(i)},w_{k}^{(i)},w_{v}^{(i)}\in\mathbb{R}^{d\times d_{h}} ) ( He et al., 2021 ) . Given a sequence of m m vectors C ∈ ℝ m × d C\in\mathbb{R}^{m\times d} over which we perform attention, and a query vector x ∈ ℝ d x\in\mathbb{R}^{d} , Prefix tuning ( Li and Liang, 2021 ) prepends l l tunable prefix vectors to the keys and values of the multi-head attention at each layer. Two sets of prefix vectors P k P_{k} and P v P_{v} are concatenated with the original key W k W_{k} and value W v W_{v} . Then the computation of head becomes:

[21] table: (1) head ( i ) = Attention ⁡ ( x ​ W q ( i ) , [ P k ( i ) ; C ​ W k ( i ) ] , [ P v ( i ) ; C ​ W v ( i ) ] ) \mathrm{head}_{(i)}=\mathrm{Attention}(xW_{q}^{(i)},[P_{k}^{(i)};CW_{k}^{(i)}],[P^{(i)}_{v};CW_{v}^{(i)}])

[22] p: where [ ; ] [;] is the concat operation, P k P_{k} and P v P_{v} are the split into N N heads and P k ( i ) P_{k}^{(i)} and P v ( i ) P_{v}^{(i)} denote the i i -th head vector.

[23] h2: 4. DDR: Dynamic Dense Retrieval with Routing Strategy

[24] p: In this section, we present the details of DDR. Specifically, we first introduce dynamic dense retrieval training based on prefix vector tuning and routing strategy. § ​ 4.1 \lx@sectionsign\ref{sec:modularization_prompt} . Then we compare the various routing strategy in ( § \lx@sectionsign 4.2 ).

[25] h3: 4.1. Dynamic Dense Retrieval Training

[26] p: As shown in Figure 1 . DDR adopts a dual-encoder architecture consisting of a query encoder f q f_{q} and a passage encoder f p f_{p} , which project queries and passages into a shared embedding space. We introduce two types of modules: a general module, which captures domain-agnostic retrieval knowledge, and a domain module, which encodes domain-specific information. In practice, dense retrievers pre-compute passage embeddings and build an approximate nearest neighbor (ANN) index for efficient retrieval ( Peng et al., 2025 ) . To minimize storage overhead and enable reuse of indexed passages, we incorporate the general module into both the query and passage encoders, while attaching the domain module only to the query encoder. This design allows a single set of passage embeddings to be shared across domains, making DDR efficient to deploy and easy to adapt to new tasks.

[27] p: Let the encoder consist of L L transformer layers, each with H H attention heads, and the head dimension d d . We define the general prefix vector 𝒫 g = { P k g , P v g } \mathcal{P}^{g}=\{P_{k}^{g},P_{v}^{g}\} and domain prefix vector 𝒫 d = { P k d , P v d } \mathcal{P}^{d}=\{P_{k}^{d},P_{v}^{d}\} . Then the prefix vector of the passage encoder f p f_{p} in each transformer layer is :

[28] table: (2) 𝒫 ( p ​ a ​ s ​ s ​ a ​ g ​ e ) = 𝒫 g \mathcal{P}^{(passage)}=\mathcal{P}^{g}

[29] p: For the query encoder, DDR uses both the general prefix vector and the domain prefix vector. To allow DDR to dynamically choose the required domain during retrieval, we introduce a selection mechanism, which is implemented through a routing function r ⁡ ( ⋅ ) r(\cdot) . Given the input x l x_{l} at layer l l , the router produce logits z l = W r ​ x l z_{l}=W_{r}x_{l} with routing parameters Δ r = W r ∈ ℝ N × d \Delta_{r}=W_{r}\in\mathbb{R}^{N\times d} , then the routing distribution is computed by:

[30] table: (3) β i = r ⁡ ( x l ) = softmax ​ ( z l ) \beta_{i}=r(x_{l})=\text{softmax}(z_{l})

[31] p: Then the prefix vector of the query encoder f q f_{q} in each transformer layer is:

[32] table: (4) 𝒫 ( q ​ u ​ e ​ r ​ y ) = 𝒫 g + ∑ i N β i ⋅ 𝒫 d \mathcal{P}^{(query)}=\mathcal{P}^{g}+\sum_{i}^{N}\beta_{i}\cdot\mathcal{P}^{d}

[33] p: where P v g ∈ ℝ H × L g × d P_{v}^{g}\in\mathbb{R}^{H\times L_{g}\times d} and P k d , P v d ∈ ℝ H × L d × d P_{k}^{d},P_{v}^{d}\in\mathbb{R}^{H\times L_{d}\times d} and L g L_{g} and L d L_{d} denote the prefix lengths; N N indicates the total number of domain. The attention output for the query encoder and passage encoder is computed as:

[34] table: (5) head ( q ) = Attention ⁡ ( x ​ W q , [ 𝒫 k ( q ​ u ​ e ​ r ​ y ) , C ​ W k ] , [ 𝒫 v ( q ​ u ​ e ​ r ​ y ) , C ​ W v ] ) head ( p ) = Attention ⁡ ( x ​ W p , [ 𝒫 k ( p ​ a ​ s ​ s ​ a ​ g ​ e ) , C ​ W k ] , [ 𝒫 v ( p ​ a ​ s ​ s ​ a ​ g ​ e ) , C ​ W v ] ) \begin{split}\mathrm{head}_{(q)}&=\mathrm{Attention}(xW_{q},[\mathcal{P}^{(query)}_{k},CW_{k}],[\mathcal{P}^{(query)}_{v},CW_{v}])\\ \mathrm{head}_{(p)}&=\mathrm{Attention}(xW_{p},[\mathcal{P}^{(passage)}_{k},CW_{k}],[\mathcal{P}^{(passage)}_{v},CW_{v}])\end{split}

[35] p: Then we can compute the final query presentation and passage representation as follows:

[36] table: (6) z q = f q ​ ( q , 𝒫 g , 𝒫 d ) z p = f p ​ ( p , 𝒫 g ) \begin{split}z_{q}&=f_{q}(q;\mathcal{P}^{g},\mathcal{P}^{d})\\ z_{p}&=f_{p}(p;\mathcal{P}^{g})\end{split}

[37] p: Given a query-passage pair, the relevance score is computed by the inner product:

[38] table: (7) s ⁡ ( q , p ) = z q T ​ z p s(q,p)=z_{q}^{T}z_{p}

[39] p: We train the DDR using a contrastive objective:

[40] table: (8) ℒ DDR = min 𝒫 g , 𝒫 d , W r − 1 n ​ ∑ i = 1 n log ⁡ exp ⁡ ( s ⁡ ( q i , p i + ) ) ∑ j = 1 K exp ⁡ ( s ⁡ ( q i , p j ) ) \mathcal{L}_{\text{DDR}}=\min_{\mathcal{P}^{g},\mathcal{P}^{d},W_{r}}-\frac{1}{n}\sum_{i=1}^{n}\log\frac{\exp(s(q_{i},p_{i}^{+}))}{\sum_{j=1}^{K}\exp(s(q_{i},p_{j}))}

[41] p: where 𝒫 g , 𝒫 d \mathcal{P}^{g},\mathcal{P}^{d} are the training parameters of general prefix vectors and domain prefix vectors, W r W_{r} is the training parameters of the routing function, and p i + p_{i}^{+} denotes a positive sample.

[42] h3: 4.2. Routing Strategy Comparison

[43] p: The routing function in Eq. 4 is a soft routing distribution, in which all modules will be activated. In this subsection, we discuss two sparse routing, which only activate a subset of modules.

[44] h4: 4.2.1. Top- k k routing (DDR-topk)

[45] p: Inspired by the top- k k routing function from the mixture of experts ( Jiang et al., 2024 ) , we can activate only the top prefix vectors based on the routing scores. Then the prefix vector in the query encoder f q f_{q} is:

[46] table: (9) 𝒫 ( q ​ u ​ e ​ r ​ y ) = 𝒫 g + ∑ i K 𝕀 [ i ∈ 𝐭𝐨𝐩𝐤 ( β ) ] ⋅ β i ⋅ 𝒫 d \mathcal{P}^{(query)}=\mathcal{P}^{g}+\sum_{i}^{K}\mathbb{I}[i\in\mathbf{topk}(\beta)]\cdot\beta_{i}\cdot\mathcal{P}^{d}

[47] h4: 4.2.2. Routing with prior information (DDR-prior)

[48] p: Instead of top- k k routing, we can activate a subset of prefix vectors using prior information. As shown in Table 1 , the training instructions can be decomposed into multiple domains, and we can use these prelabelled prior signals. Based on the labeled instruction, we select the corresponding prefix vectors. The resulting prefix vector used in the query encoder f q f_{q} is:

[49] table: (10) 𝒫 ( q ​ u ​ e ​ r ​ y ) = 𝒫 g + ∑ i 𝕀 [ i ∈ ℳ ( β ) ] ⋅ β i ⋅ 𝒫 d \mathcal{P}^{(query)}=\mathcal{P}^{g}+\sum_{i}\mathbb{I}[i\in\mathcal{M}(\beta)]\cdot\beta_{i}\cdot\mathcal{P}^{d}

[50] p: where ℳ ⁡ ( ⋅ ) \mathcal{M}(\cdot) is a instruction-domain mapping function. In this paper, we use the pre-labeled instruction datasets used in the BERRI ( Asai et al., 2022 ) . Each instruction is mapped into several domains.

[51] figure: Table 1. Examples of instruction decomposition for retrieval tasks in the BERRI ( Asai et al., 2022 ) . Each task has diverse domains, which are denoted by experts. Task Instruction NF Corpus Retrieve scientific paper paragraph to answer this question. SciFact Retrieve a scientific paper sentence to verify if the following claim is true. domains Science , QA , Fact-Checking , Wikipedia

[52] figure: Table 2. Zero-shot retrieval results measured by NDCG@10. # Params denote the trainable parameters. The highest results among dense retrievers are bolded, and the second-best results are underlined . We report the results of baselines from their original papers. The labeled domains for each task are listed in colors: Science , QA , Fact-Checking , Wikipedia , Summarization . Method PLM (# Params) TREC NFC SCD SCF CLI DBP Avg. SCI QA SCI QA SCI SUM SCI FC FC WIKI DeepCT BERT-base (110M) 40.6 28.3 12.4 63.0 6.6 17.7 28.1 SPARTA DistilBERT (66M) 53.8 30.1 12.6 58.2 8.2 31.4 32.8 Contriever BERT-base (110M) 27.4 31.7 14.9 64.9 15.5 29.2 30.6 ANCE RoBERTa-base (110M) 65.4 23.7 12.2 50.7 19.8 28.1 33.3 DR coCondenser (110M) 63.6 28.8 11.5 48.6 19.9 36.3 34.8 DDR-topk coCondenser (2.3M×8) 61.9 31.0 13.6 52.8 20.3 34.5 35.7 DDR-prior coCondenser (2.3M×8) 65.3 31.4 15.4 54.0 22.3 36.3 37.5

[53] figure: Table 3. Ablation study of DDR. We remove the trainable routing and assign uniform weights to all modules (w/o routing). We then remove the prior domain labels and let DDR activate all eight modules (w/o prior). Method PLM (# Params) TREC NFC SCD SCF CLI DBP Avg. SCI QA SCI QA SCI SUM SCI FC FC WIKI DDR-prior coCondenser (2.3M×8) 65.3 31.4 15.4 54.0 22.3 36.3 37.5 w/o routing coCondenser (2.3M×8) 64.3 30.9 13.5 52.8 22.3 36.3 36.3 w/o prior coCondenser (2.3M×8) 60.9 31.1 13.2 52.3 20.0 34.6 35.4

[54] h2: 5. Experimental results

[55] p: To test the advantages of the DDR approach, we empirically evaluate our approach with other strong baselines in zero-shot retrieval tasks, which demand the integration of various domains to achieve effective retrieval.

[56] h3: 5.1. Datasets and Metrics

[57] p: During training, we use BERRI (Bank of Explicit Retrieval Instructions) ( Asai et al., 2022 ) , a large-scale retrieval dataset with expert-written task instructions, where each instruction is decomposed into multiple domain labels. As a result, we can extract several domains per task. During evaluation, we test DDR on the zero-shot retrieval benchmark BEIR ( Thakur et al., 2021 ) . Following prior work ( Asai et al., 2022 ; Dai et al., 2022 ) , we exclude Natural Questions ( Wagner et al., 2001 ) , MS MARCO ( Nguyen et al., 2016 ) , HotpotQA ( Yang et al., 2018 ) , FEVER ( Thorne et al., 2018 ) , and CQADupStack ( Hoogeveen et al., 2015 ) to avoid overlap between training and test tasks. We report the official NDCG@10 metric.

[58] h3: 5.2. Experimental Setup

[59] p: We divide training into two phases: general prefix training and domain prefix training. In the first phase, we use general retrieval tasks (e.g., MS-MARCO ( Nguyen et al., 2016 ) ) to train only the general prefix. This helps the model learn common knowledge and ensures basic retrieval ability. In the second phase, we jointly train the domain prefix vector and the routing function. We follow the coCondenser training procedure ( Gao and Callan, 2021b ) and use a pre-trained condenser-base model as the backbone. Following prior work ( Tang et al., 2022 ) , the prefix length is set to 128. We set the number of modules to 8 and set the 2 in the top- k k routing. The learning rate is 7e-3 for general prefix training and 7e-6 for domain prefix training. For each positive document, we select 5 negative passages as in BERRI ( Asai et al., 2022 ) . All training and inference are performed on a single server with 1 NVIDIA A100 80G GPU.

[60] h3: 5.3. Baselines

[61] p: We compare DDR with several strong retrieval baseline methods, including sparse retrieval approaches like DeepCT ( Dai and Callan, 2020 ) and SPARTA ( Zhao et al., 2020 ) , as well as dense retrieval approaches like Contriever ( Izacard et al., 2022 ) and ANCE ( Xiong et al., 2020 ) . We also compare DDR with a standard dense retrieval model that updates all model weights during training. We implement the DDR with various routing strategies (refer to the Sec. 4.2 ). DDR-topk uses a top- k k routing strategy. DDR-prior uses prior information to guide the routing strategy.

[62] h3: 5.4. Experimental Results and Analysis

[63] p: Table 2 shows the results on the six zero-shot retrieval benchmarks in BEIR. Compared to other strong sparse retrieval and dense retrieval baselines, DDR-prior achieves the best average performance among all models, while using fewer trainable parameters. This shows its strong generalization ability and parameter efficiency. In particular, DDR-prior outperforms Contriever and ANCE by a clear margin on most datasets. Both DDR-prior and DDR-topk perform better than standard dense retrieval (DR), indicating that DDR generalizes better than DR. Compared with DDR-topk, DDR-prior improves the average score by 1.8 points, highlighting the importance of prior information for generalization.

[64] p: DDR also demonstrates interpretability compared to DR approaches. For instance, DDR shows a great improvement over DR in Fact-Checking-related tasks. This outcome suggests that the Fact-Checking retrieval module is effectively trained during the training phase. Such observations provide valuable insights for guiding the allocation of training resources to areas where they are most needed for further enhancement.

[65] h3: 5.5. Ablation Study

[66] p: In this subsection, we study the various components that can improve performance. First, we discard the routing function and activate the modules only based on the prior domain label. Then we assign a uniform routing to each module (w/o routing). As shown in Table 3 , the performance of DDR-prior will decrease by 1.2 when discarding the routing function. This result indicates the importance of routing distribution in the training of DDR. Then we remove the prior information, which activates all eight modules during retrieval (w/o prior). The performance drops by 2.1 when we activate all the modules. This demonstrates that the prior labeled domain is necessary to specialize each retriever in a specific domain.

[67] h2: 6. Conclusion

[68] p: This paper proposes a new dense retrieval paradigm, dynamic dense retrieval. We argue that DDR can address the limitations of traditional dense retrieval systems by offering flexibility, scalability, and efficiency, which makes it particularly well-suited for dynamic environments, low-resource scenarios, and applications requiring frequent updates. Specifically, DDR has the potential to solve several long-standing challenges in dense retrieval, such as adaptability to new tasks and dynamic knowledge management. Our experiments show the advantages of this framework. It improves flexibility and efficiency while using only a small number of trainable parameters. Currently, our dense retrieval model is built on coCondenser. In future work, we plan to explore stronger backbone models trained based on large language models, such as RepLLaMA ( Ma et al., 2024 ) .

[69] h2: References

[70] h2: Instructions for reporting errors

[71] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[72] p: Tip: You can select the relevant text first, to include it in your report.

[73] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[74] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
