[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: ϕ \phi -DPO: Fairness Direct Preference Optimization Approach to Continual Learning in Large Multimodal Models

[3] h6: Abstract

[4] p: Fairness in Continual Learning for Large Multimodal Models (LMMs) is an emerging yet underexplored challenge, particularly in the presence of imbalanced data distributions that can lead to biased model updates and suboptimal performance across tasks. While recent continual learning studies have made progress in addressing catastrophic forgetting, the problem of fairness caused by imbalanced data remains largely underexplored. This paper presents a novel Fairness Direct Preference Optimization (FaiDPO or ϕ \phi -DPO) framework for continual learning in LMMs. In particular, we first propose a new continual learning paradigm based on Direct Preference Optimization (DPO) to mitigate catastrophic forgetting by aligning learning with pairwise preference signals. Then, we identify the limitations of conventional DPO in imbalanced data and present a new ϕ \phi -DPO loss that explicitly addresses distributional biases. We provide a comprehensive theoretical analysis demonstrating that our approach addresses both forgetting and data imbalance. Additionally, to enable ϕ \phi -DPO-based continual learning, we construct pairwise preference annotations for existing benchmarks in the context of continual learning. Extensive experiments and ablation studies show the proposed ϕ \phi -DPO achieves State-of-the-Art performance across multiple benchmarks, outperforming prior continual learning methods of LMMs.

[5] h2: 1 Introduction

[6] p: Large multimodal models (LMMs) have shown their strong performance as general-purpose assistants in various visual learning tasks [ 67 , 65 , 66 , 5 , 56 , 55 , 19 ] . The success of LMMs typically relies on supervised finetuning on carefully curated, large-scale multi-task datasets. In practical deployment, LMMs often suffer from performance degradation when encountering novel knowledge, tasks, or shifts in data distribution. However, fully retraining large models to incorporate new knowledge and capabilities is computationally expensive and time-consuming. Meanwhile, direct fine-tuning on the new datasets may result in a performance drop for previously learned tasks [ 116 ] . This phenomenon is called the catastrophic forgetting problem. In addition, although recent Retrieval-Augmented Generation (RAG) improves the contextual understanding of LMMs for more accurate responses [ 41 , 108 , 40 , 87 ] , RAG-LMM systems struggle with distribution shifts and novel tasks. Since the retrieval only augments the input without updating model parameters, the internal knowledge representations remain unchanged. Therefore, to ensure the reliable performance of the LMMs in a dynamic and adaptive environment, it is crucial to develop a Continual Learning paradigm for LMMs (Figure 1 ) so that the models can incrementally acquire new information and skills while preserving the knowledge learned previously.

[7] figure: Figure 1 : Our Fairness DPO ( ϕ \phi -DPO) approach to Continual Learning in LMMs . Prior continual learning methods, e.g . , LoRA , struggle under imbalanced multimodal data and suffer from catastrophic forgetting . The vanilla DPO is still influenced by the imbalanced data distributions . Our ϕ \phi -DPO approach can (1) mitigate forgetting, (2) adapt continuously to new learning tasks, and (3) maintain robustness under data imbalance.

[8] p: In continual learning, two primary challenges are identified: (1) Catastrophic Forgetting and (2) Fairness. Fairness in LMMs is particularly crucial for real-world deployment, since the biased or inconsistent behaviors can result in unequal outcomes and reduce trustworthiness, especially in human-centric applications. Recent studies of continual learning in LMMs [ 13 , 116 ] have introduced several methods to address the catastrophic forgetting problem. However, fairness remains a fundamental issue in the continual learning of LMMs that has been unexplored .

[9] figure: Figure 2 : The Imbalanced Distribution of Multimodal Continual Learning Benchmarks. The distribution of samples across ScienceQA topics is highly skewed, i.e . categories with fewer training examples ( e.g . Grammar, Phonological Awareness, Word Study) exhibit significantly lower accuracy, while topics with richer data ( e.g . Biology, Physics) achieve stronger performance.

[10] p: As shown in Figure 2 , multimodal datasets often exhibit significant topic imbalance, introducing bias during each incremental task and resulting in skewed performance. This imbalance poses two key challenges: (1) Representation Alignment and (2) Adaptability and Forgetting. Unlike traditional LMMs trained on diverse modality pairs in a single stage, continual multimodal learning proceeds sequentially, requiring incremental alignment. Under imbalanced conditions, this leads to biased gradient updates across tasks, groups, or domains (see Section 3 ). For example, Figure 3 illustrates the progression of training across tasks, starting with ScienceQA, which focuses on structured visual reasoning through diagram-text alignment. The subsequent Grounding task redirects attention toward object-level localization, whereas OCR-VQA centers on fine-grained text extraction. These tasks exhibit distinct visual distributions, language prompts, and alignment objectives, ultimately leading to modality imbalance and a degradation of prior representation alignment. As each task may be dominated by a particular modality or semantic class, gradient updates often favor current majority signals, undermining prior alignment and degrading performance on earlier tasks. These imbalances undermine representation alignment and may exacerbate catastrophic forgetting. Moreover, prior continual learning studies have focused on unimodal settings [ 10 , 21 , 74 , 93 , 91 ] , whereas LMMs introduce new complexity due to their multimodal settings. In this context, biased data becomes a critical issue, as the imbalance in multi-modalities or semantic classes not only exaggerates catastrophic forgetting but also limits the adaptability of LMMs to new tasks or knowledge.

[11] figure: Figure 3 : ScienceQA, Grounding, and OCR-VQA introduce progressively shifting visual distributions and alignment objectives, creating modality imbalance across tasks.

[12] p: While data imbalance poses critical challenges, current methods remain inadequate in addressing this problem. Low-rank Adaptation (LoRA) [ 36 ] is widely used in continual learning for LMMs [ 13 , 26 , 116 ] . Although it preserves the frozen backbone, its adapters can inherit dataset bias, leading to gradient updates skewed toward majority semantic classes [ 12 , 100 ] . Moreover, LoRA does not inherently mitigate bias propagation [ 12 ] and is prone to catastrophic forgetting, especially when adapters are shared or new ones induce representation drift [ 114 , 31 ] . Meanwhile, Knowledge Distillation has also been widely adopted in unimodal continual learning [ 10 , 21 , 74 ] . However, it remains limited in multimodal contexts. LMMs often encode demographic and distributional biases from their large-scale pretraining, which distillation can transfer or amplify in the student model [ 113 , 81 ] . Imitating biased teacher outputs could lead to suboptimal and biased predictions [ 113 ] . Under imbalance, majority data dominate distillation gradients, lowering generalization to tail classes [ 91 , 93 ] . In addition, while distillation aligns output probabilities, it fails to preserve internal representations critical for maintaining prior knowledge, particularly in LMMs where knowledge spans multiple modalities and layers [ 3 , 88 ] .

[13] p: Contributions. This work proposes a novel Fairness Direct Preference Optimization (FaiDPO or ϕ \phi -DPO) approach to Continual Learning in LMMs. Our contributions can be summarized as follows. First, we introduce a new continual learning paradigm, Direct Preference Optimization (DPO), which addresses the catastrophic forgetting problem in continual learning. Second, by analyzing the limitations of traditional DPO, we present a new Fairness DPO loss to address the fairness problem caused by imbalanced data. We provide a comprehensive theoretical analysis to show that our proposed approach can address both catastrophic forgetting and imbalanced data. Third, to support the DPO learning in our framework, we contribute the DPO labels for current continual learning benchmarks. Finally, our intensive experiments and ablation studies have illustrated the effectiveness and State-of-the-Art performance (SoTA) of our approach compared to prior continual learning methods.

[14] h2: 2 Related Work

[15] p: Large Multimodal Models. Early advances in large language models (LLMs) [ 58 , 17 , 2 , 82 , 5 ] have driven rapid progress in LMMs. Recent models span across vision-language [ 67 , 65 , 95 ] , video-language [ 102 , 117 , 61 , 57 ] , and audio-language domains [ 39 , 24 ] , with LMMs playing a central role in scaling multimodal understanding. Early work by [ 4 ] effectively bridged vision and language modalities in a few-shot learning setting, followed by [ 55 ] , which enhanced inter-modality connectivity via Q-Former. This was further developed into an instruction-aware model within the vision-language instruction-tuning framework [ 67 ] . LLaVA [ 67 ] established a streamlined visual-to-language space projection using a linear layer, later refined by [ 65 ] with an MLP and AnyRes, a technique adept at handling high-resolution images. Subsequent studies [ 66 , 51 , 115 , 50 , 54 ] contributed further improvements, culminating in a robust model [ 52 ] capable of handling diverse vision tasks. These multimodal models are finding real-world use across a variety of domains. For instance, they have been adapted for biomedical analysis [ 53 ] , improved through multimodal federated learning [ 14 ] , and applied to 3D point cloud understanding [ 104 , 103 , 64 ] . Recent work [ 6 , 98 , 78 ] with more effective training techniques and better architectures, serve as a stepping stone for a wide range of more advanced research efforts aimed at developing generalist LMMs.

[16] p: Continual Learning. The topic of continual learning has evolved through several core paradigms, each approaching the stability-plasticity dilemma from a unique angle. The field has largely centered around rehearsal-base approaches [ 48 , 7 ] , regularization-based methods [ 90 , 94 , 89 , 47 , 60 ] , structure-based strategies [ 92 , 93 , 71 , 22 ] , and prompt-based methods [ 101 , 85 ] . In parallel, continual learning for large language models has rapidly become a focal point of recent work [ 79 ] . Depending on where adaptation occurs, current efforts can be categorized into three major stages: continual pre-training [ 42 , 18 ] , continual instruction tuning [ 76 , 109 , 106 , 99 ] , and continual alignment [ 111 , 86 ] . Meanwhile, for LMMs, progress remains relatively limited [ 13 , 110 , 8 , 28 , 26 , 116 ] . Chen et al . [ 13 ] introduced one of the first systematic benchmarks for continual instruction tuning of LMMs. Building on this, Zeng et al . [ 110 ] proposed a dual-modality guided prompt framework to improve efficiency and stability. Cao et al . [ 8 ] and Guo et al . [ 26 ] explored hierarchical and modular strategies to better preserve multimodal representations over sequential updates. Chen et al . [ 15 ] and Zhao et al . [ 116 ] further attempted to mitigate forgetting and enhance continual adaptability, while Lin et al . [ 62 ] proposed a novel paradigm of sparse memory fine-tuning. While prior continual learning studies in unimodal learning has taken fairness into consideration [ 91 , 93 ] , there are limited studies addressing this problem in LMMs. Unlike prior methods, we propose to address the catastrophic forgetting problem via a new continual learning paradigm and achieve fairness under imbalanced data settings.

[17] h2: 3 The Proposed ϕ \phi -DPO Approach

[18] p: Given a large multimodal model π \pi , continual learning involves incrementally learning it on a sequence of datasets 𝒟 = { 𝒟 1 , … , 𝒟 T } \mathcal{D}=\{\mathcal{D}_{1},...,\mathcal{D}_{T}\} , where T T is the number of learning steps. For each learning step t t , 𝒟 t = { x j , y j } j = 1 | 𝒟 i | \mathcal{D}_{t}=\{x^{j},y^{j}\}_{j=1}^{|\mathcal{D}_{i}|} constraints | 𝒟 i | |\mathcal{D}_{i}| instruction data, where x j = ( x img j , x ins j ) x^{j}=(x^{j}_{\mathrm{img}},x^{j}_{\mathrm{ins}}) consists of a pair image ( x img j x^{j}_{\mathrm{img}} ) and textual instruction ( x ins j x^{j}_{\mathrm{ins}} ), and y j y^{j} is the corresponding answer. Formally, learning the LMM π t \pi_{t} at step t t on dataset 𝒟 t \mathcal{D}_{t} can be formed as follows:

[19] table: π t ∗ = arg max π t 𝔼 x , y ∈ 𝒟 t log p ( y | x ) + D Forget ( π t ∥ π t − 1 ) \footnotesize\pi^{*}_{t}=\arg\!\max_{\pi_{t}}\mathbb{E}_{x,y\in\mathcal{D}_{t}}\log p(y|x)+D_{\mathrm{Forget}}(\pi_{t}\|\pi_{t-1}) (1)

[20] p: where log ⁡ p ⁡ ( y | x ) \log p(y|x) is the supervised fine-tuning loss on the instruction data, D Forget ( π t ∥ π t − 1 ) D_{\mathrm{Forget}}(\pi_{t}\|\pi_{t-1}) is the forgetting mitigation that prevents the current LMM π t \pi_{t} drifted away from the previous learned LMM π t − 1 \pi_{t-1} , i.e . , avoid forgetting.

[21] p: Prior continual learning studies commonly adopt knowledge distillation [ 10 , 21 ] to mitigate the forgetting. However, as shown in Sec. 1 , the traditional knowledge distillation may exaggerate the bias and cause catastrophic forgetting, especially in the context of multimodal learning. Several recent studies adopt contrastive clustering [ 93 , 91 ] to model catastrophic forgetting. Although it has yielded promising results in unimodal problems, defining clusters in multimodal settings is infeasible. Thus, to address this problem, our approach adopts Reinforcement Learning from Human Feedback (RLHF) to model the forgetting.

[22] p: Formally, let r ⁡ ( x , y ) r(x,y) be the reward model to evaluate the forgetting and adaptability level of π t \pi_{t} , i.e . , the higher r ⁡ ( x , y ) r(x,y) , the better memory retained and adaptability. Then, to model catastrophic forgetting ( D Forget D_{\mathrm{Forget}} ), our continual learning can be reformulated under an RLHF perspective as in Eqn. ( 2 ).

[23] table: π t ⋆ = arg max π t 𝔼 x ∼ 𝒳 t 𝔼 y ∼ π t ( ⋅ ∣ x ) [ r ( x , y ) ] s.t. D KL ( π t ( ⋅ ∣ x ) ∥ π t − 1 ( ⋅ ∣ x ) ) ≤ δ , \footnotesize\begin{split}\pi_{t}^{\star}\;=\;\arg\!\max_{\pi_{t}}\;\mathbb{E}_{x\sim\mathcal{X}_{t}}\,\mathbb{E}_{y\sim\pi_{t}(\cdot\mid x)}\big[r(x,y)\big]\\ \hskip 8.50012pt\text{s.t.}\hskip 8.50012ptD_{\mathrm{KL}}\!\big(\pi_{t}(\cdot\mid x)\,\big\|\,\pi_{t-1}(\cdot\mid x)\big)\leq\delta,\end{split} (2)

[24] p: where π t − 1 \pi_{t-1} is the reference (previous learning step) policy, D KL ( π t ∥ π t − 1 ) D_{\textrm{KL}}(\pi_{t}\|\pi_{t-1}) is the KL divergence to measure the difference of predictions between previous and current LMMs, δ \delta is the threshold to constraint the policy update.

[25] p: Although learning Eqn. ( 2 ) can be achieved via Proximal Policy Optimization Algorithms (PPO), it still presents two major challenges. First, learning the reward model r r requires the corresponding training data. In addition, in the context of continual learning, it may require incrementally learn the reward model r r at each learning step, which is not feasible. Second, learning the reward model via PPO on the imbalanced data may lead to biased predictions produced by the model [ 77 ] . To address these challenges, inspired by [ 75 ] , we propose modeling RLHF reward in continual learning via Direct Preference Optimization. We introduce a new Fairness DPO loss to address fairness modeling.

[26] h3: 3.1 Direct Preference Optimization to Continual Learning in LMMs

[27] h4: 3.1.1 DPO as Continual Learning

[28] p: Inspired by [ 75 ] , learning the LMM at learning step t t of Eqn. ( 2 ) via RLHF can be rewritten using the Lagrangian multiplier as follows:

[29] table: π t ⋆ = max π t 𝔼 x , y ∼ π t [ r ( x , y ) ] − β D KL ( π t ( ⋅ ∣ x ) ∥ π t − 1 ( ⋅ ∣ x ) ) \footnotesize\begin{split}\pi_{t}^{\star}=\max_{\pi_{t}}\;\mathbb{E}_{x,y\sim\pi_{t}}[r(x,y)]-\beta D_{\mathrm{KL}}\!\big(\pi_{t}(\cdot\mid x)\,\big\|\,\pi_{t-1}(\cdot\mid x)\big)\end{split} (3)

[30] p: where β \beta is the Lagrangian multiplier that controls the divergence of the LMM at the current learning step from the previous step. As shown in [ 75 ] , the learning objective in Eqn. ( 3 ) achieves optimal when it takes the following forms:

[31] table: π t ⋆ ​ ( y ∣ x ) = π t − 1 ​ ( y ∣ x ) ​ exp ⁡ ( 1 β ​ r ​ ( x , y ) ) Z ⁡ ( x ) , r ⁡ ( x , y ) = β ​ log ⁡ π t ⋆ ​ ( y ∣ x ) π t − 1 ​ ( y ∣ x ) + β ​ log ⁡ Z ⁡ ( x ) , \footnotesize\begin{split}\pi_{t}^{\star}(y\mid x)&=\frac{\pi_{t-1}(y\mid x)\,\exp\left(\tfrac{1}{\beta}\,r(x,y)\right)}{Z(x)},\\ r(x,y)&=\beta\log\frac{\pi_{t}^{\star}(y\mid x)}{\pi_{t-1}(y\mid x)}+\beta\log Z(x),\end{split} (4)

[32] p: where Z ⁡ ( x ) = ∑ y π t − 1 ​ ( y | x ) ​ exp ⁡ ( 1 β ​ r ​ ( x , y ) ) Z(x)=\sum_{y}\pi_{t-1}(y|x)\exp\left(\frac{1}{\beta}r(x,y)\right) .

[33] p: From RLHF to Pairwise Preferences. In our continual learning setting, for each sample instruction data x x , let y + y^{+} be the well-retrained (good memory) and well-adapted output, and let y − y^{-} be the forgotten output. The preference of y + y^{+} over y − y^{-} , i.e . , p ⁡ ( y + ≻ y − | x ) p(y^{+}\succ y^{-}|x) can be formed via the Bradley-Terry model as follows:

[34] table: p ⁡ ( y + ≻ y − | x ) = σ ⁡ ( β ⁡ [ r ⁡ ( x , y + ) − r ⁡ ( x , y − ) ] ) , \footnotesize\begin{split}p(y^{+}\succ y^{-}|x)=\sigma\!\big(\beta\,[r(x,y^{+})-r(x,y^{-})]\big),\end{split} (5)

[35] p: where σ ⁡ ( u ) = 1 1 + exp ⁡ ( − u ) \sigma(u)=\frac{1}{1+\exp(-u)} is the Sigmoid function. Then, maximizing the (conditional) log-likelihood over pairs to avoid catastrophic forgetting in continual learning can be reformed as the following logistic loss:

[36] table: ℒ pref ​ ( π t , π t − 1 ) = 𝔼 ( x , y + , y − ) ​ [ − log ⁡ σ ⁡ ( β ⁡ [ r ⁡ ( x , y + ) − r ⁡ ( x , y − ) ] ) ] \footnotesize\mathcal{L}_{\text{pref}}(\pi_{t},\pi_{t-1})=\mathbb{E}_{(x,y^{+},y^{-})}\Big[-\log\sigma\big(\beta\big[r(x,y^{+})-r(x,y^{-})\big]\big)\Big] (6)

[37] p: Continual Learning Paradigm with DPO. Under the optimum conditions defined in Eqn. ( 4 ), the logistic loss of the reward difference in Eqn. ( 6 ) can be written in terms of policy log-ratios as in Eqn. ( 7 ).

[38] table: ℒ DPO ( π t , π t − 1 ) = − 𝔼 x , y + , y − [ log σ ( β log π t ​ ( y + | x ) π t − 1 ​ ( y + | x ) − β log π t ​ ( y − | x ) π t − 1 ​ ( y − | x ) ) ] = − 𝔼 x , y + , y − log σ [ β [ ( log π t ( y + | x ) − log π t ( y − | x ) ] ⏟ trainable policy − β [ log ⁡ π t − 1 ​ ( y + | x ) − log ⁡ π t − 1 ​ ( y − | x ) ] ⏟ fixed reference ] \footnotesize\begin{split}&\mathcal{L}_{\mathrm{DPO}}(\pi_{t},\pi_{t-1})=-\mathbb{E}_{x,y^{+},y^{-}}\Bigg[\log\sigma\Bigg(\beta\log\frac{\pi_{t}(y^{+}|x)}{\pi_{t-1}(y^{+}|x)}\\ &\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt-\beta\log\frac{\pi_{t}(y^{-}|x)}{\pi_{t-1}(y^{-}|x)}\Bigg)\Bigg]\\ &=-\mathbb{E}_{x,y^{+},y^{-}}\log\sigma\Bigg[\beta\underbrace{\Big[\Big(\log\pi_{t}(y^{+}|x)-\log\pi_{t}(y^{-}|x)\Big]}_{\text{trainable policy}}\\ &\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt\hskip 8.50012pt-\beta\underbrace{\Big[\log\pi_{t-1}(y^{+}|x)-\log\pi_{t-1}(y^{-}|x)\Big]}_{\text{fixed reference}}\Bigg]\end{split} (7)

[39] p: Interpretation. As in continual learning, each training stage aims to adapt the current policy π t \pi_{t} to a new learning task while preserving consistency with the reference model π t − 1 \pi_{t-1} to avoid catastrophic forgetting. The DPO objective encourages π t \pi_{t} to increase the relative log-odds of well-retained (or memory-consistent) y + y^{+} over forgotten output y − y^{-} compared to π t − 1 \pi_{t-1} , effectively favoring outputs that remain aligned with prior knowledge. Our learning objective prevents the policy from drifting away from the previous learning task and implicitly regularizes updates toward the information manifold of the previous model, thereby mitigating catastrophic forgetting. Meanwhile, the hyper-parameter β \beta controls the adaptability of the LMM, i.e . , larger values constrain π t \pi_{t} to remain close to π t − 1 \pi_{t-1} ( stability ). In comparison, smaller values permit more flexible adaptation to new distributions ( plasticity ). Our learning mechanism replaces the explicit reward-based RLHF objective in Eqn. ( 2 ) with a preference-based contrastive loss that directly enforces policy consistency under a bounded divergence constraint. As a result, our DPO approach provides a principled mechanism for continual alignment, i.e . , preserving prior knowledge while enabling controlled updates that enhance adaptability across sequential tasks.

[40] h4: 3.1.2 Theoretical Analysis of Direct Preference Optimization in Forgetting Mitigation

[41] p: Prior studies [ 21 , 10 ] have shown that Knowledge Distillation (KD) is a common approach to mitigate catastrophic forgetting. In this section, we will provide a theoretical analysis to demonstrate that the knowledge distillation loss is bounded by the DPO loss, which offers a more effective mechanism for preventing catastrophic forgetting and enhancing adaptability. In a typical knowledge distillation approach used in continual learning, the current model π t \pi_{t} is encouraged to remain close to the previous model π t − 1 \pi_{t-1} via the Kullback–Leibler (KL) divergence to mitigate catastrophic forgetting:

[42] table: ℒ KD ​ ( π t , π t − 1 ) = D KL ( π t − 1 ∥ π t ) = 𝔼 x , y ∼ π t − 1 [ log π t − 1 ​ ( y | x ) π t ​ ( y | x ) ] \footnotesize\begin{split}\mathcal{L}_{\mathrm{KD}}(\pi_{t},\pi_{t-1})&=D_{\mathrm{KL}}(\pi_{t-1}\,\|\,\pi_{t})=\mathbb{E}_{x,y\sim\pi_{t-1}}\left[\log\frac{\pi_{t-1}(y|x)}{\pi_{t}(y|x)}\right]\end{split} (8)

[43] h6: Lemma 1

[44] p: Lower Bound of KL Divergence Governed by DPO Loss. The lower bound of the D KL ( π t − 1 ∥ π t ) D_{\mathrm{KL}}(\pi_{t-1}\|\pi_{t}) is governed by the DPO loss as follows:

[45] table: D KL ( π t − 1 ∥ π t ) ≥ 1 C lower ( log 2 − ℒ DPO ( π t ; π t − 1 ) ) 2 \footnotesize D_{\mathrm{KL}}(\pi_{t-1}\|\pi_{t})\geq\frac{1}{C_{\mathrm{lower}}}(\log 2-\mathcal{L}_{\mathrm{DPO}}(\pi_{t};\pi_{t-1}))^{2} (9)

[46] p: where C lower C_{\mathrm{lower}} is a constant number.

[47] h6: Lemma 2

[48] p: Upper Bound of KL Divergence Governed by DPO Loss. The upper bound of the D KL ( π t − 1 ∥ π t ) D_{\mathrm{KL}}(\pi_{t-1}\|\pi_{t}) is governed by the DPO loss as follows:

[49] table: D KL ( π t − 1 ∥ π t ) ≤ C upper ℒ DPO ( π t ; π t − 1 ) \footnotesize D_{\mathrm{KL}}(\pi_{t-1}\|\pi_{t})\leq C_{\mathrm{upper}}\mathcal{L}_{\mathrm{DPO}}(\pi_{t};\pi_{t-1}) (10)

[50] p: where C upper C_{\mathrm{upper}} is a constant number.

[51] p: Proof. The proof of Lemmas 1 - 2 is in our appendix. We show the exact form of C lower C_{\mathrm{lower}} and C upper C_{\mathrm{upper}} in our proof.

[52] p: Interpretation. Lemmas 1 and 2 establish a two-sided relationship between the DPO loss and the KL divergence used in prior knowledge distillation methods [ 10 , 21 ] . The lower bound implies that a small DPO loss ensures π t \pi_{t} remains close to π t − 1 \pi_{t-1} , thereby preserving prior knowledge and mitigating catastrophic forgetting. The upper bound further constrains the KL divergence, indicating that DPO regularizes updates so that D KL ( π t − 1 ∥ π t ) D_{\mathrm{KL}}(\pi_{t-1}\|\pi_{t}) grows proportionally to the DPO loss. These bounds indicate that DPO implicitly controls catastrophic forgetting and adaptation, i.e . a small ℒ DPO \mathcal{L}_{\mathrm{DPO}} constrains the divergence, ensuring semantic consistency with π t − 1 \pi_{t-1} while allowing new learning task updates. Different from KD, which minimizes KL divergence directly, DPO introduces an adaptive, pairwise preference mechanism. Therefore, DPO can be viewed as a generalized form of distillation, i.e . , retaining the regularization effect while selectively amplifying high-reward (well-retained) responses and suppressing low-reward (forgotten) ones. This makes DPO more robust to forgetting while maintaining flexibility for continual learning in LMMs.

[53] h3: 3.2 Fairness DPO in Continual Learning

[54] figure: Figure 4 : Our Proposed Continual Learning Approach via Fairness DPO for Large Multimodal Models . Traditional reinforcement learning with human feedback (RLHF) method optimize models through explicit reward maximization. Our framework instead reformulates RLHF as Direct Preference Optimization (DPO). The Fairness DPO loss mitigate the gradient biased under the imbalanced data.

[55] p: While the vanilla DPO loss can help prevent catastrophic forgetting and improve adaptability, the imbalance in data distribution can influence the behavior of DPO, leading to suboptimal performance. Indeed, let us revise the gradient produced by the DPO loss defined in Eqn. ( 7 ) as follows:

[56] table: ∇ θ ℒ DPO ​ ( θ , μ ) = 𝔼 μ ​ [ ( p ⁡ ( z ) − 1 ) ​ ∇ θ s θ ​ ( z ) ] ℒ DPO ​ ( θ , μ ) = − 𝔼 ( x , y + , y − ) ∼ μ ​ [ log ⁡ p ⁡ ( y + ≻ y − | x ) ] , \footnotesize\begin{split}\nabla_{\theta}\mathcal{L}_{\mathrm{DPO}}(\theta;\mu)&=\mathbb{E}_{\mu}\!\big[(p(z)-1)\,\nabla_{\theta}s_{\theta}(z)\big]\\ \mathcal{L}_{\mathrm{DPO}}(\theta;\mu)&=-\mathbb{E}_{(x,y^{+},y^{-})\sim\mu}\big[\log p(y^{+}\succ y^{-}|x)\big],\end{split} (11)

[57] p: where θ \theta is the parameters of LMM, z = ( x , y + , y − ) z=(x,y^{+},y^{-}) , and s θ ​ ( z ) = β ⁡ ( r ⁡ ( x , y + ) − r ⁡ ( x , y − ) ) s_{\theta}(z)=\beta\big(r(x,y^{+})-r(x,y^{-})\big) , μ \mu is the data distribution of the current learning task. Let us define p ⁡ ( z ) = p ⁡ ( y + ≻ y − | x ) p(z)=p(y^{+}\succ y^{-}|x) . In addition, we partition training data into K K disjoint groups { G k } k = 1 K \{G_{k}\}_{k=1}^{K} , with mixture weights μ k = μ ⁡ ( G k ) \mu_{k}=\mu(G_{k}) . Then, the group gradients can be rewritten as follows:

[58] table: ∇ θ ℒ DPO ​ ( θ , μ ) = ∑ k = 1 K μ k ​ m k ​ ( θ ) m k ​ ( θ ) = 𝔼 ⁡ [ ( p ⁡ ( z ) − 1 ) ​ ∇ θ s θ ​ ( z ) ∣ z ∈ G k ] \footnotesize\begin{split}\nabla_{\theta}\mathcal{L}_{\mathrm{DPO}}(\theta;\mu)&=\sum_{k=1}^{K}\mu_{k}\,m_{k}(\theta)\\ m_{k}(\theta)&=\mathbb{E}\!\big[(p(z)-1)\nabla_{\theta}s_{\theta}(z)\mid z\in G_{k}\big]\end{split} (12)

[59] p: where m k ​ ( θ ) m_{k}(\theta) is the group mean gradient. Let q ′ = ( q 1 ′ , … , q K ′ ) q^{\prime}=(q^{\prime}_{1},\dots,q^{\prime}_{K}) be the desired (ideal) balanced mixture over groups, and q = ( q 1 , … , q K ) q=(q_{1},\dots,q_{K}) the observed imbalanced distribution, with p ≠ q p\neq q . In an ideal scenario, the LLM π t \pi_{t} trained on the balanced data distribution q ′ q^{\prime} will perform fairly. Then, the gradient difference incurred when optimizing with biased distribution q q instead of balanced distribution q ′ q^{\prime} can be defined as:

[60] table: B ⁡ ( θ ) = ∇ θ ℒ DPO ​ ( θ , q ) − ∇ θ ℒ DPO ​ ( θ , q ′ ) = ∑ k = 1 K ( q k − q k ′ ) ​ m k ​ ( θ ) \footnotesize B(\theta)=\nabla_{\theta}\mathcal{L}_{\mathrm{DPO}}(\theta;q)-\nabla_{\theta}\mathcal{L}_{\mathrm{DPO}}(\theta;q^{\prime})=\sum_{k=1}^{K}(q_{k}-q^{\prime}_{k})\,m_{k}(\theta) (13)

[61] p: Then, suppose there exists a group j j such that q j > q j ′ q_{j}>q^{\prime}_{j} (major group), the j j -th group contributes ( q j − q j ′ ) ​ m j ​ ( θ ) (q_{j}-q^{\prime}_{j})\,m_{j}(\theta) in the gradient updates, which is a systematic overweighting of group j j ’s gradient. Meanwhile, if q i < q i ′ q_{i}<q^{\prime}_{i} for a minority group i i , then the i i -th term is underweighted. In other words, the gradient updates produced by the vanilla DPO loss will be biased towards major groups, and the gradient difference between ideal and practical data distribution will not be identical, i.e . , ‖ B ⁡ ( θ ) ‖ ≠ 0 \|B(\theta)\|\neq 0 .

[62] figure: Figure 5 : Example of Our DPO Data in the Continual Learning Benchmark. Best viewed in color.

[63] p: To address the problem caused by the imbalanced data distribution, inspired by the focal loss [ 63 ] , we introduce a new Fair DPO loss to improve the fairness of the LMM. In particular, the Fair DPO loss can be defined as follows:

[64] table: ℒ DPO γ ​ ( θ , μ ) = − 𝔼 z ∼ μ ​ [ ( 1 − p ⁡ ( z ) ) γ ​ log ⁡ p ⁡ ( z ) ] \footnotesize\mathcal{L}^{\gamma}_{\mathrm{DPO}}(\theta;\mu)=-\,\mathbb{E}_{z\sim\mu}\Big[(1-p(z))^{\gamma}\,\log p(z)\Big] (14)

[65] p: where γ \gamma is the focusing parameter. Then, the gradient updates in Eqn. ( 12 ) can be rewritten as follows:

[66] table: ∇ ℒ DPO γ ​ ( θ , μ ) = ∑ k = 1 K μ k ​ w k γ ​ ( θ ) ​ m k ​ ( θ ) where ​ w k γ ​ ( θ ) = 𝔼 ⁡ [ α γ ​ ( p ⁡ ( z ) ) ∣ z ∈ G k ] and ​ α γ ​ ( p ) = ( 1 − p ) γ − 1 ​ [ ( 1 − p ) + γ ​ p ​ log ⁡ p ] \footnotesize\begin{split}\nabla\mathcal{L}^{\gamma}_{\mathrm{DPO}}(\theta;\mu)&=\sum_{k=1}^{K}\mu_{k}\,w_{k}^{\gamma}(\theta)\,m_{k}(\theta)\\ \text{where}\hskip 8.50012ptw_{k}^{\gamma}(\theta)&=\mathbb{E}\!\big[\alpha_{\gamma}(p(z))\mid z\in G_{k}\big]\\ \text{and}\hskip 8.50012pt\alpha_{\gamma}(p)&=(1-p)^{\gamma-1}\Big[(1-p)+\gamma p\log p\Big]\end{split} (15)

[67] p: In Eqn. ( 15 ), w k γ ​ ( θ ) w_{k}^{\gamma}(\theta) plays a role as a modulating factor to balance the gradients of each group. Then, the gradient difference in Eqn. ( 13 ) with respect to the Fair DPO loss can be rewritten as:

[68] table: B γ ​ ( θ ) = ∇ ℒ DPO γ ​ ( θ , q ) − ∇ ℒ DPO γ ​ ( θ , q ′ ) = ∑ k = 1 K ( q k − q k ′ ) ​ w k γ ​ ( θ ) ​ m k ​ ( θ ) \footnotesize\begin{split}B_{\gamma}(\theta)&=\nabla\mathcal{L}^{\gamma}_{\mathrm{DPO}}(\theta;q)-\nabla\mathcal{L}^{\gamma}_{\mathrm{DPO}}(\theta;q^{\prime})\\ &=\sum_{k=1}^{K}(q_{k}-q^{\prime}_{k})\,w_{k}^{\gamma}(\theta)\,m_{k}(\theta)\end{split} (16)

[69] h6: Lemma 3

[70] p: Balanced Gradient Update of Fair DPO Loss . Given a sufficient large value of γ \gamma , the Fair DPO loss will produce the balanced gradient update across groups regardless of the biased data distribution, i.e . lim γ → ∞ ‖ B γ ​ ( θ ) ‖ = 0 \lim_{\gamma\to\infty}\|B_{\gamma}(\theta)\|=0 .

[71] p: Proof. The proof of Lemma 3 is included in our appendix.

[72] p: Interpretation. When the focusing parameter γ \gamma becomes sufficiently large, the discrepancy between optimization over the imbalanced distribution and the idealized balanced distribution vanishes, i.e . , lim γ → ∞ B γ ​ ( θ ) = 0 \lim_{\gamma\to\infty}B_{\gamma}(\theta)=0 . This indicates that our proposed Fair DPO loss can yield fairer gradient updates as γ \gamma increases. However, excessively large values of γ \gamma can cause gradient vanishing, leading to a numerically flat loss landscape. As a result, this limits the adaptability of the LMMs in continual learning settings. Meanwhile, if γ \gamma is too small, the loss behaves similarly to the standard DPO objective, potentially reinforcing the unfairness induced by imbalanced data. Therefore, careful tuning of γ \gamma is crucial to strike a balance between fairness and plasticity in the continual learning of LMMs.

[73] p: Continual Learning Procedure. Figure 4 illustrates our continual learning framework. In particular, the final learning objective of our proposed approach at each learning step t t can be formed as follows:

[74] table: π t ∗ = arg min π t 𝔼 x , y ∈ 𝒟 t − log p ( y | x ) + ℒ DPO γ ( π t ∥ π t − 1 ) \footnotesize\pi^{*}_{t}=\arg\!\min_{\pi_{t}}\mathbb{E}_{x,y\in\mathcal{D}_{t}}-\log p(y|x)+\mathcal{L}^{\gamma}_{\mathrm{DPO}}(\pi_{t}\|\pi_{t-1}) (17)

[75] p: To avoid the overfitting on small-scale size data and increase the memory-efficiency during training DPO, the LMM π t \pi_{t} at learning step t t is optimized via LoRA.

[76] h3: 3.3 DPO Data in Continual Learning Benchmark

[77] p: We conduct our experiments on three benchmark suites: CoIN [ 13 ] , MLLM-CL Domain [ 116 ] , and MLLM-CL Ability [ 116 ] . The CoIN benchmark comprises eight diverse learning tasks: ScienceQA [ 70 ] , TextVQA [ 84 ] , ImageNet [ 20 ] , GQA [ 38 ] , VizWiz [ 30 ] , Grounding [ 72 , 44 ] , VQAv2 [ 25 ] , and OCR-VQA [ 73 ] . The MLLM-CL Domain benchmark is designed for domain-incremental learning and consists of five sequential domains: Remote Sensing [ 69 ] , Medical [ 33 ] , Autonomous Driving [ 83 ] , Science [ 45 , 29 , 11 , 46 ] , and Finance [ 116 ] . The MLLM-CL Ability benchmark focuses on task-incremental learning and includes four tasks: OCR [ 59 , 68 ] , Math and Logic [ 80 , 112 ] , Visual Perception [ 43 , 1 ] , and GUI Agent [ 107 , 35 , 96 ] .

[78] p: While these benchmarks provide instruction-following data suitable for training LMMs, they lack pairwise preference annotations required for DPO. To address this gap and enable continual learning via DPO, we construct pairwise preference data for each dataset within these three benchmarks. In particular, for each instruction instance, we treat the provided reference answer as the preferred output y + y^{+} , which represents a well-retained (good-memory) and well-adapted response. To simulate the less preferred (forgotten) output y − y^{-} , we prompt a large language model to hallucinate an alternative response. The model is conditioned on both the textual instruction and the reference answer y + y^{+} , and is instructed to generate an output y − y^{-} that is plausible and coherent, yet distinct from y + y^{+} and potentially flawed in subtle ways. This design encourages the formation of challenging preference pairs suitable for effective DPO training. Finally, all labels are manually verified by human annotators to ensure that the rejected responses accurately reflect undesirable or suboptimal behavior (Figure 5 ).

[79] h2: 4 Experimental Results

[80] h3: 4.1 Benchmarks, Metrics, and Implementation

[81] p: Benchmark and Metrics. We evaluate on three benchmarks: CoIN, MLLM-CL Domain, and MLLM-CL Ability. Following standard protocols [ 116 , 26 , 13 ] , continual learning performance is measured using five metrics. Last Accuracy reports accuracy on all seen tasks after learning the final one. Mean Finetune Accuracy (MFT) reflects accuracy on each task immediately after learning, serving as an upper bound without forgetting. Mean Final Accuracy (MFN) averages accuracy across all tasks after full training. Mean Average Accuracy (MAA) captures the average performance over all tasks after each step. Backward Transfer (BWT) quantifies forgetting by comparing final accuracy to post-learning accuracy for each task. Higher scores indicate better performance.

[82] p: Implementation. Our framework adopts the implementation of LLaVA v1.5 [ 65 ] , using CLIP-ViT-L-14 ( 336 2 336^{2} ) as the vision encoder and Vicuna 7B [ 17 ] as the language backbone. For fair comparison, we follow the training setup of [ 116 , 26 , 13 ] , with LoRA rank 32, AdamW optimizer, a cosine learning rate schedule (base LR: 2 ​ e − 5 2\mathrm{e}{-5} ), and batch size 64 for one training epoch. All experiments are run on 16 NVIDIA A100 40GB GPUs.

[83] h3: 4.2 Main Results

[84] p: Results on the MLLM-CL Domain Benchmark. Table 1 shows results on the MLLM-CL Domain benchmark across five incremental domains: Remote Sensing (RS), Medical, Autonomous Driving (AD), Science, and Finance. Our ϕ \phi -DPO achieves consistently outperforms prior methods in both individual accuracy (on last step) and continual learning metrics. In particular, ϕ \phi -DPO achieves 85.58% on RS, 95.28% on Finance, and shows similar improvements on Medical (69.74%), AD (57.75%), and Science (61.55%). The results has indicated the robustness of our ϕ \phi -DPO under domain shifts. In terms of continual learning performance, ϕ \phi -DPO achieves an MFT of 74.29%, an MFN of 74.00%, and an MAA of 75.78%. The BWT is -0.37%, further confirming the ability for ϕ \phi -DPO in forgetting mitigation across incremental domain adaptation. Compared to prior methods that rely on LoRA ( e.g . , MR-LoRA) or Mixture-of-Expert architectures ( e.g . , CL-MoE), ϕ \phi -DPO offers a more unified framework while gaining superior results. These findings reinforce the generalizability and stability of ϕ \phi -DPO in continual domain-incremental learning.

[85] figure: Table 1 : Results on MLLM-CL Domain (* denote the method using relay data). RS: Remote Sensing, Med: Medical, AD: Autonmous Driving, Sci: ScienceQA, Fin: Finance. Method RS Med AD Sci Fin MFT ↑ \uparrow MFN ↑ \uparrow MAA ↑ \uparrow BWT ↑ \uparrow Zeroshot 32.29 28.28 15.59 35.55 62.56 34.85 − - − - − - LoRA-FT* [ 36 ] 76.54 50.27 43.01 43.32 89.85 66.32 60.60 64.72 -7.15 O-LoRA* [ 99 ] 76.94 41.17 34.18 39.61 83.22 60.49 55.02 60.73 -6.83 MoELoRA* [ 13 ] 77.63 49.54 39.08 41.04 89.21 66.24 59.30 64.81 -8.68 CL-MoE* [ 37 ] 76.58 52.31 39.65 45.64 90.21 66.65 60.88 64.95 -7.22 HiDe* [ 26 ] 74.80 42.29 34.03 38.01 79.22 60.83 53.67 61.81 -8.95 SEFE* [ 15 ] 78.43 52.85 46.21 47.76 89.33 66.89 62.92 66.51 -4.97 DISCO* [ 27 ] 77.78 46.25 50.45 49.51 89.71 65.27 62.74 64.92 -3.17 LoRA-FT [ 36 ] 69.65 41.59 25.43 40.88 87.45 64.98 53.00 61.13 -14.97 O-LoRA [ 99 ] 74.64 44.42 30.02 41.47 87.15 65.16 55.54 62.12 -12.03 MoELoRA [ 13 ] 77.54 41.85 27.62 40.13 86.75 64.94 54.78 61.76 -12.70 CL-MoE [ 37 ] 71.34 46.84 26.33 41.17 88.74 66.06 54.88 61.79 -13.96 HiDe [ 26 ] 74.31 48.95 33.21 38.54 81.55 60.77 55.31 60.68 -6.82 SEFE [ 15 ] 77.26 50.37 37.21 40.87 86.82 65.01 58.51 63.63 -8.13 DISCO [ 27 ] 76.03 45.20 43.79 42.33 88.95 64.43 59.26 63.35 -6.46 MR-LoRA [ 116 ] 80.87 65.32 54.12 56.71 91.12 69.64 69.63 71.06 -0.01 ϕ \phi -DPO 85.68 69.74 57.73 61.55 95.28 74.29 74.00 75.68 -0.37

[86] p: Results on the MLLM-CL Ability Benchmark. Table 2 shows results on the MLLM-CL Ability benchmark across four incremental tasks: OCR, Math & Logic (M&L), Visual Programming (VP), and GUI Agent (GUI), with the first four columns reporting performance after the final task. Our ϕ \phi -DPO achieves consistently strong results across all tasks, with 38.40% on OCR, 39.20% on M&L, 68.65% on VP, and 35.00% on GUI Agent. In addition, ϕ \phi -DPO outperforms prior methods on all continual learning metrics. ϕ \phi -DPO achieves a MFT of 45.55%, MFN of 45.31%, and MAA of 43.03, while gaining a BWT of -0.31%, indicating minimal forgetting. Compared to DISCO and MR-LoRA, which rely on LoRA and routing strategies, ϕ \phi -DPO demonstrates improved overall performance. These results highlight the effectiveness of ϕ \phi -DPO in maintaining stability and generalization throughout the incremental learning process.

[87] figure: Table 2 : Results on MLLM-CL Ability (* denote the method using relay data). M&L: Math and Logic, VP: Visual Perception. Method OCR M&L VP GUI MFT ↑ \uparrow MFN ↑ \uparrow MAA ↑ \uparrow BWT ↑ \uparrow Zeroshot [ 36 ] 31.20 30.20 60.79 10.00 33.05 − - − - − - LoRA-FT* [ 36 ] 21.80 32.70 58.38 28.75 40.32 35.41 36.32 -6.55 O-LoRA* [ 99 ] 29.60 31.30 60.79 27.50 39.96 37.30 36.34 -3.55 MoELoRA* [ 13 ] 19.80 32.20 54.19 30.00 40.35 34.05 35.39 -8.41 CL-MoE* [ 37 ] 25.40 31.80 60.91 30.00 41.22 37.03 37.28 -5.59 HiDe* [ 26 ] 24.60 28.40 30.71 23.75 36.84 26.86 33.54 -13.30 SEFE* [ 15 ] 25.60 34.80 57.61 31.39 42.25 37.35 37.93 -6.53 DISCO* [ 37 ] 34.20 35.00 61.55 27.50 40.14 39.56 37.85 -0.77 LoRA-FT [ 36 ] 23.60 33.70 55.84 32.50 41.28 36.41 36.58 -6.49 O-LoRA [ 99 ] 29.60 32.90 52.41 33.75 39.72 37.16 35.42 -3.41 MoELoRA [ 13 ] 26.70 32.80 56.85 27.22 39.45 35.89 36.07 -4.75 CL-MoE [ 37 ] 19.90 32.70 53.43 30.69 40.50 34.18 35.65 -8.43 HiDe [ 26 ] 24.60 32.10 46.32 28.75 37.98 32.94 34.60 -6.72 SEFE [ 15 ] 26.00 33.40 57.74 33.75 40.98 37.72 36.59 -4.35 DISCO [ 27 ] 32.90 33.10 60.15 30.14 39.02 39.07 36.57 0.07 MR-LoRA [ 116 ] 33.70 36.20 65.10 32.50 41.89 41.88 38.86 -0.02 ϕ \phi -DPO 38.40 39.20 68.65 35.00 45.55 45.31 43.03 -0.31

[88] figure: Table 3 : Results on CoIN. SciQA: ScienceQA, Image: ImageNet, Viz: VizWiz, Ground: Grounding, Text: TextVQA, VQA: VQAv2. Method SciQA Image Viz Ground Text GQA VQA OCR MFN ↑ \uparrow MAA ↑ \uparrow Zeroshot 69.79 9.93 45.50 58.47 57.75 60.77 66.50 64.93 − - − - FineTune 57.43 28.90 41.88 30.05 51.39 50.76 53.28 64.78 47.31 52.86 LwF [ 60 ] 60.71 30.58 41.49 36.01 52.80 47.07 53.43 65.12 48.40 53.22 EWC [ 47 ] 59.75 31.88 42.26 34.96 51.06 51.84 55.30 64.55 48.95 53.30 L2P [ 101 ] 70.21 23.31 44.21 43.76 56.25 58.46 62.32 64.11 52.83 53.96 O-LoRA [ 99 ] 72.56 62.84 48.43 58.97 57.66 59.14 63.21 63.31 60.77 62.60 MoELoRA [ 13 ] 62.02 37.21 43.32 33.22 52.05 53.12 57.92 65.75 50.58 55.24 HiDe [ 26 ] 73.20 69.28 50.76 59.18 56.92 61.33 67.12 64.76 62.82 64.70 ϕ \phi -DPO 77.84 95.61 54.55 60.74 59.17 64.32 69.99 68.69 68.86 74.94

[89] p: Results on the CoIN Benchmark. Table 3 shows results on the CoIN benchmark. MFT and BWT are omitted for prior methods since intermediate models were not published. The first eight columns report final-task accuracy on: ScienceQA (SciQA), ImageNet (Image), VizWiz (Viz), Grounding (Ground), TextVQA (Text), GQA, VQAv2 (VQA), and OCR. Our ϕ \phi -DPO consistently outperforms all prior methods across these tasks. In particular, it achieves major gains on vision-centric tasks, i.e . , ImageNet (95.61%), VizWiz (54.55%), and OCR (68.69%), while also obtaining strong results on language and reasoning benchmarks, i.e . , ScienceQA (77.84%), GQA (64.32%), and VQAv2 (69.99%). Importantly, our approach maintains a high Mean Final Accuracy (MFN) of 68.86%, reflecting superior knowledge preservation across incremental tasks. ϕ \phi -DPO further achieves the best MAA of 74.94%, demonstrating stable performance throughout continual training. These results confirm the effectiveness of ϕ \phi -DPO in mitigating catastrophic forgetting and increasing adaptability.

[90] h3: 4.3 Ablation Study

[91] p: Effectiveness of Fairness DPO. Table 4 presents an ablation study on the impact of each component in our approach. Compared to knowledge distillation (KD), vanilla DPO achieves consistently better performance across incremental domains, i.e . RS (82.26%), Med (67.12%), AD (55.79%), Sci (59.58%), and Fin (93.94%), as well as improved continual learning metrics: MFT of 72.80%, MFN of 71.74%, MAA of 73.68%, and BWT of -1.33%, indicating reduced forgetting. Our ϕ \phi -DPO further improves the performance, i.e . 74.29% MFT, 74.00% MFN, 75.68% MAA, and -0.37% BWT, demonstrating stronger task performance and greater stability. These results highlight the effectiveness of our Fair DPO loss in continual learning.

[92] figure: Table 4 : Effectiveness of Our Fairness DPO. RS Med AD Sci Fin MFT ↑ \uparrow MFN ↑ \uparrow MAA ↑ \uparrow BWT ↑ \uparrow Zeroshot 32.29 28.28 15.59 35.55 62.56 34.85 − - − - − - LoRA-FT 69.65 41.59 25.43 40.88 87.45 64.98 53.00 61.13 -14.97 KD 77.82 63.92 52.88 58.57 92.85 71.37 69.21 71.49 -2.71 DPO 82.26 67.12 55.79 59.58 93.94 72.80 71.74 73.68 -1.33 ϕ \phi -DPO 85.68 69.74 57.73 61.55 95.28 74.29 74.00 75.68 -0.37

[93] p: Effectiveness of Divergence Parameter β \beta . Table 5 studies the impact of the divergence parameter β \beta in our approach. The β \beta parameter controls the trade-off between adaptability to new tasks and the forgetting level of previous knowledge. As shown in Table 5 , lower values of β \beta ( i.e . , 0.01 0.01 and 0.05 0.05 ) lead to faster adaptation, reflected in higher MFT scores (75.43% and 75.27%). However, it will result in increased forgetting, as indicated by degraded BWT values (-2.66% and -1.66%). Meanwhile, larger values of β \beta ( i.e . , 0.50 0.50 ) reduce forgetting with improved BWT (-0.32%), but at the cost of reduced overall performance, including lower MFT (72.11%), MFN (71.85%), and MAA (73.60%). Among our configurations, β = 0.10 \beta=0.10 achieves the best balance, with competitive MFT (74.29%), MFN (74.00%), and MAA (75.68%), while maintaining a favorable BWT of -0.37%. These results have illustrated the role of β \beta in stability and plasticity in continual learning.

[94] figure: Table 5 : Effectiveness of Divergence Parameter β \beta . β \beta RS Med AD Sci Fin MFT ↑ \uparrow MFN ↑ \uparrow MAA ↑ \uparrow BWT ↑ \uparrow 0.01 83.09 67.71 56.90 62.06 96.77 75.43 73.31 75.83 -2.66 0.05 84.91 69.30 57.16 62.21 96.12 75.27 73.94 76.27 -1.66 0.10 85.68 69.74 57.73 61.55 95.28 74.29 74.00 75.68 -0.37 0.50 83.74 67.55 55.44 59.64 92.88 72.11 71.85 73.60 -0.32

[95] p: Effectiveness of Focusing Parameter γ \gamma . Table 6 presents an ablation on the focusing parameter γ \gamma , which controls the emphasis on harder preference pairs during training. When γ = 0.0 \gamma=0.0 , the loss reduces to the standard DPO formulation, corresponding to the vanilla DPO baseline in Table 4 . Lower values of γ \gamma ( i.e . , 0.50 0.50 and 1.00 1.00 ) yield moderate improvements in stability and forgetting, as reflected in reduced BWT (-1.07% and -0.77%) while maintaining competitive MFT (72.79% and 73.38%) and MAA (73.87% and 74.66%). This result suggests that incorporating moderate focus on harder examples enhances knowledge preservation without compromising adaptability. Meanwhile, the high values of γ \gamma ( e.g . , 5.00 5.00 ) lead to degraded performance across most metrics, with reduced MFT (73.21%), MFN (72.18%), and MAA (74.27%), indicating that overemphasizing difficult pairs can lower overall learning dynamics. In our experiments, γ = 2.00 \gamma=2.00 provides the best trade-off, achieving favorable MFT (74.29%), MFN (74.00%), MAA (75.68%), and BWT (-0.37%). These results have indicated the importance of focusing parameter γ \gamma in balancing plasticity and stability in our ϕ \phi -DPO approach.

[96] figure: Table 6 : Effectiveness of Focusing Parameter γ \gamma . γ \gamma RS Med AD Sci Fin MFT ↑ \uparrow MFN ↑ \uparrow MAA ↑ \uparrow BWT ↑ \uparrow 0.00 82.26 67.12 55.79 59.58 93.94 72.80 71.74 73.68 -1.33 0.50 82.84 67.84 55.50 59.71 93.78 72.79 71.93 73.87 -1.07 1.00 84.01 68.44 56.56 60.74 94.06 73.38 72.76 74.66 -0.77 2.00 85.68 69.74 57.73 61.55 95.28 74.29 74.00 75.68 -0.37 5.00 83.08 67.74 55.99 60.05 94.03 73.21 72.18 74.27 -1.29

[97] p: Effectiveness of Different LMMs. Table 7 evaluates ϕ \phi -DPO across different LMMs: LLaVA-7B, LLaVA-13B, and InternVL-7B [ 16 ] . In all cases, ϕ \phi -DPO outperforms standard DPO, confirming the generality of our Fair DPO objective. Larger models ( i.e . LLaVA-13B) show improved performance over LLaVA-7B in MFT (76.29% vs. 74.29%), MFN (75.81% vs. 74.00%), MAA (77.57% vs. 75.68%), and BWT (-0.59% vs. -0.37%), reflecting better knowledge preservation due to greater capacity. InternVL-7B, despite similar size to LLaVA-7B, benefits from stronger vision-language alignment and achieves competitive results. ϕ \phi -DPO consistently enhances performance across all backbones, demonstrating robustness and compatibility with diverse LMM architectures.

[98] figure: Table 7 : Effectiveness of Different LMM Framework. LLM Method RS Med AD Sci Fin MFT ↑ \uparrow MFN ↑ \uparrow MAA ↑ \uparrow BWT ↑ \uparrow LLaVA-7B DPO 82.26 67.12 55.79 59.58 93.94 72.80 71.74 73.68 -1.33 ϕ \phi -DPO 85.68 69.74 57.73 61.55 95.28 74.29 74.00 75.68 -0.37 LLaVA-13B DPO 86.24 70.28 58.02 63.26 96.84 75.89 74.93 77.00 -1.21 ϕ \phi -DPO 87.40 71.09 59.34 63.96 97.28 76.29 75.81 77.57 -0.59 InternVL-7B DPO 82.69 67.69 55.97 60.67 94.83 73.88 72.37 74.68 -1.89 ϕ \phi -DPO 85.64 69.88 57.94 61.95 95.74 74.62 74.23 75.94 -0.49

[99] h2: 5 Conclusions and Limitations

[100] p: Conclusions. This paper has presented a novel Fairness DPO approach to Continual Learning in LMMs. In particular, our Fair DPO learning objective has been introduced to address both catastrophic forgetting and fairness problems. Our theoretical analysis has also shown the effectiveness of our proposed approach. Our SoTA results on three benchmarks have further confirmed the effectiveness of our ϕ \phi -DPO compared to prior methods.

[101] p: Limitations. Our work adopts a set of learning hyper-parameters aligned with theoretical analysis, but this choice introduces limitations, particularly in tuning β \beta , γ \gamma , the weighted loss in Eqn. ( 17 ), and DPO data construction. The quality of DPO data is sensitive to label stability, which may be affected by class imbalance, domain shifts, or model uncertainty, potentially leading to suboptimal distillation targets and misleading pairwise correlations. These limitations highlight the need for future work on more robust and adaptive DPO strategies for continual multimodal learning.

[102] p: Acknowledgment. This work is partly supported by NSF CAREER (No. 2442295), NSF SCH (No. 2501021), NSF E-RISE (No. 2445877), NSF BIO (No. 2524623) and USDA/NIFA Award. We also acknowledge the Arkansas High-Performance Computing Center (HPC) for GPU servers.

[103] h2: References

[104] p: Supplementary Material

[105] h2: Appendix A Proof of Lemmas

[106] h3: A.1 Proof of Lemma 1

[107] p: The DPO loss in Eqn. ( 7 ) can be rewrite as follows:

[108] table: ℒ DPO ​ ( π t , π t − 1 ) = 𝔼 x , y + , y ​ [ ℓ β ​ ( Δ t ​ ( y + , y − ) ) ] ℓ β ​ ( u ) = log ⁡ ( 1 + exp ⁡ ( β ​ u ) ) Δ t ​ ( y + , y − ) = ( log ⁡ π t ​ ( y + | x ) − log ⁡ π t ​ ( y − | x ) ) − ( log ⁡ π t − 1 ​ ( y + | x ) − log ⁡ π t − 1 ​ ( y − | x ) ) \footnotesize\begin{split}\mathcal{L}_{\mathrm{DPO}}(\pi_{t},\pi_{t-1})&=\mathbb{E}_{x,y^{+},y}\Bigg[\ell_{\beta}\left(\Delta_{t}(y^{+},y^{-})\right)\Bigg]\\ \ell_{\beta}\left(u\right)&=\log\Big(1+\exp(\beta u)\Big)\\ \Delta_{t}(y^{+},y^{-})&=\Big(\log\pi_{t}(y^{+}|x)-\log\pi_{t}(y^{-}|x)\Big)\\ &\hskip 8.50012pt\hskip 8.50012pt-\Big(\log\pi_{t-1}(y^{+}|x)-\log\pi_{t-1}(y^{-}|x)\Big)\end{split} (18)

[109] h6: Lemma 4

[110] p: Pairwise Logistic Lower Bound by Margin . For any u ∈ ℝ u\in\mathbb{R} and β > 0 \beta>0 ,

[111] table: ℓ β ​ ( u ) = log ⁡ ( 1 + e − β ​ u ) ≥ log ⁡ 2 − β 2 ​ u . \ell_{\beta}(u)=\log(1+e^{-\beta u})\;\;\geq\;\;\log 2-\tfrac{\beta}{2}u.

[112] p: Proof. Since log ⁡ ( 1 + e − v ) \log(1+e^{-v}) is convex and symmetric around v = 0 v=0 in the sense that its tangent at 0 is log ⁡ 2 − 1 2 ​ v \log 2-\tfrac{1}{2}v , the global underestimator follows from convexity log ⁡ ( 1 + e − v ) ≥ log ⁡ 2 − 1 2 ​ v \log(1+e^{-v})\;\geq\;\log 2-\tfrac{1}{2}v . Then, we substitute v = β ​ u v=\beta u follow by taking expectation over pairs:

[113] table: 𝔼 [ ℓ β ( Δ t ( y + , y − ) ) ≥ log 2 − β 2 𝔼 [ Δ t ( y + , y − ) ] . \mathbb{E}[\ell_{\beta}(\Delta_{t}(y^{+},y-))\geq\log 2-\frac{\beta}{2}\,\mathbb{E}[\Delta_{t}(y^{+},y-)]. (19)

[114] p: As a result, the small value of the DPO loss forces large average margin 𝔼 ⁡ [ Δ t ​ ( y + , y − ) ] \mathbb{E}[\Delta_{t}(y^{+},y-)] . In other words, the smaller value of DPO loss enforces the model’s preference for well-retained y + y^{+} responses stronger than for forgotten ones y − y^{-} .

[115] h6: Lemma 5

[116] p: Average Margin Controls an Integral Probability Metrics (IPM) . Let ℱ 1 \mathcal{F}_{1} be the set of all 1-Lipschitz functions, If the reward function r r is L L -Lipschitz, then r / L ∈ ℱ 1 r/L\in\mathcal{F}_{1} . Then, for any pair of marginals P + , P − P^{+},P^{-} where y + ∼ P + ​ ( y + ) y^{+}\sim P^{+}(y^{+}) and y − ∼ P − ​ ( y − ) y^{-}\sim P^{-}(y^{-}) , we have

[117] table: 𝔼 ⁡ [ Δ t ​ ( y + , y − ) ] = 𝔼 P + ​ [ r ⁡ ( x , y + ) ] − 𝔼 P − ​ [ r ⁡ ( x , y − ) ] ≤ L ​ IPM ℱ 1 ⁡ ( P + , P − ) ≤ L ​ W 1 ​ ( P + , P − ) IPM ℱ 1 ⁡ ( P + , P − ) = sup f ∈ ℱ 1 ( 𝔼 y + ∼ P + ​ [ f ⁡ ( y + ) ] − 𝔼 y − ∼ P − ​ [ f ⁡ ( y − ) ] ) \footnotesize\begin{split}\mathbb{E}[\Delta_{t}(y^{+},y^{-})]&=\mathbb{E}_{P^{+}}[r(x,y+)]-\mathbb{E}_{P^{-}}[r(x,y-)]\\ &\leq L\operatorname{IPM}_{\mathcal{F}_{1}}(P^{+},P^{-})\leq LW_{1}(P^{+},P^{-})\\ \operatorname{IPM}_{\mathcal{F}_{1}}(P^{+},P^{-})&=\sup_{f\in\mathcal{F}_{1}}\left(\mathbb{E}_{y^{+}\sim P^{+}}[f(y^{+})]-\mathbb{E}_{y^{-}\sim P^{-}}[f(y^{-})]\right)\end{split} (20)

[118] p: where W 1 W_{1} is the 1-Wasserstein distance.

[119] p: Proof. By definition of IPM over 1-Lipschitz functions and r / L r/L is admissible, the above inequality is the Kantorovich-Rubinstein duality IPM \mathrm{IPM} over 1-Lipschitz functions equals W 1 W_{1} provided in [ 23 ] . In addition, although Lemma 5 requires r r to be an L L -Lipschitz function, we have observed that a local L L -Lipschitz reward function, which is satisfied in our setup, is also sufficient. Indeed, prior studies [ 34 ] rigorously derives bounds on the local Lipschitz constants of deep neural networks and shows they can be meaningfully controlled despite huge global constants. This result indicate that the LLMs behave smoothly around their high-probability outputs. In our context, we only need the log-ratio to be Lipschitz on the region visited by preference pairs, not globally over all possible outputs. Transformer-based LLMs incorporate norm control, weight decay, and normalization layers, which implicitly bound gradient magnitudes and curtail abrupt jumps in logits. Empirically, small semantic perturbations rarely cause extreme changes in logits, suggesting local smoothness holds on the data manifold [ 105 , 32 ] Thus, a locally valid Lipschitz constant suffices the requirement of Lemma 5 . Therefore, while LLMs may not be globally Lipschitz, they plausibly satisfy the needed local Lipschitz continuity in the regions relevant to DPO, making Lemma 5 still valid in practice.

[120] p: In addition, it can be shown that W 1 ​ ( P + , P − ) ≤ 3 ​ W 1 ​ ( π t , π t − 1 ) W_{1}(P^{+},P^{-})\leq 3W_{1}(\pi_{t},\pi_{t-1}) follows naturally from the triangle inequality of the Wasserstein distance. In particular, if the preference distributions P + P^{+} and P − P^{-} remain close to the current and previous policies, respectively, such that W 1 ​ ( P + , π t ) ≤ W 1 ​ ( π t , π t − 1 ) W_{1}(P^{+},\pi_{t})\leq W_{1}(\pi_{t},\pi_{t-1}) and W 1 ​ ( P − , π t − 1 ) ≤ W 1 ​ ( π t , π t − 1 ) W_{1}(P^{-},\pi_{t-1})\leq W_{1}(\pi_{t},\pi_{t-1}) , then we obtain

[121] table: W 1 ​ ( P + , P − ) ≤ W 1 ​ ( P + , π t ) + W 1 ​ ( π t , π t − 1 ) + W 1 ​ ( π t − 1 , P − ) ≤ 3 ​ W 1 ​ ( π t , π t − 1 ) \footnotesize\begin{split}W_{1}(P^{+},P^{-})&\leq W_{1}(P^{+},\pi_{t})+W_{1}(\pi_{t},\pi_{t-1})+W_{1}(\pi_{t-1},P^{-})\\ &\leq 3W_{1}(\pi_{t},\pi_{t-1})\end{split} (21)

[122] p: This conditions are typically satisfied in the DPO training, where preference sampling is a monotone and non-expansive process, e.g., sampling candidates from a mixture (please refer to Remark 1 in Section A.2 ). In the context of continual learning of LMMs, the inequality W 1 ​ ( P + , P − ) ≤ 3 ​ W 1 ​ ( π t , π t − 1 ) W_{1}(P^{+},P^{-})\leq 3W_{1}(\pi_{t},\pi_{t-1}) implies that the discrepancy between well-retained and forgotten knowledge is bounded by the overall policy shift between two learning steps. Intuitively, both P + P^{+} and P − P^{-} remain anchored around their respective policies, so the overall variation between them is bounded by a constant multiple of the inter-policy shift W 1 ​ ( π t , π t − 1 ) W_{1}(\pi_{t},\pi_{t-1}) . Concurrently, both P + P^{+} and P − P^{-} remain anchored around their respective policies— P + P^{+} near the current policy π t \pi_{t} and P − P^{-} near the previous policy π t − 1 \pi_{t-1} —so if the model update between tasks is smooth, the semantic drift between memory retention and forgetting remains limited. This highlights that our continual DPO training enforces a stable adaptation process, where catastrophic forgetting is controlled by bounding the inter-policy Wasserstein distance.

[123] p: Now, the inequality in Eqn. ( 20 ) can be further rewritten as follows:

[124] table: 𝔼 ⁡ [ Δ t ​ ( y + , y − ) ] = 𝔼 P + ​ [ r ⁡ ( x , y + ) ] − 𝔼 P − ​ [ r ⁡ ( x , y − ) ] ≤ 3 ​ L ​ W 1 ​ ( π t , π t − 1 ) \small\begin{split}\mathbb{E}[\Delta_{t}(y^{+},y^{-})]&=\mathbb{E}_{P^{+}}[r(x,y+)]-\mathbb{E}_{P^{-}}[r(x,y-)]\\ &\leq 3LW_{1}(\pi_{t},\pi_{t-1})\end{split} (22)

[125] h6: Lemma 6

[126] p: A Transport–Entropy Inequality . Since the output probability p ⁡ ( y | x ) p(y|x) produced by the LMM of previous learning step π t 1 \pi_{t_{1}} is computed based on the softmax on the logit scores of token y y , we can view π t − 1 \pi_{t-1} as a Boltzmann distribution over token sequences. Then, without a strict argument, we assume that π t − 1 \pi_{t-1} satisfies the Talagrand T 2 ​ ( C 0 ) T_{2}(C_{0}) inequality [ 49 , 97 ] :

[127] table: W 2 2 ( μ , π t − 1 ) ≤ 2 C 0 D KL ( μ ∥ π t − 1 ) for all μ , W_{2}^{2}(\mu,\pi_{t-1})\leq 2C_{0}\,D_{\mathrm{KL}}(\mu\,\|\,\pi_{t-1})\quad\text{for all }\mu, (23)

[128] p: Then, since W 1 ≤ W 2 W_{1}\leq W_{2} , by substituting μ \mu by π t \pi_{t} , we have the final inequality as follows:

[129] table: W 1 ​ ( π t , π t − 1 ) ≤ 2 C 0 D KL ( π t ∥ π t − 1 ) W_{1}(\pi_{t},\pi_{t-1})\;\leq\;\sqrt{2C_{0}\,D_{\mathrm{KL}}(\pi_{t}\,\|\,\pi_{t-1})} (24)

[130] p: Proof. The proof of Talagrand T 2 ​ ( C 0 ) T_{2}(C_{0}) inequality has been shown in prior studies [ 9 ] .

[131] p: Proof of Lemma 1 . From Lemmas 4 - 6 , we have

[132] table: ℒ DPO ​ ( θ , x ) ≥ log ⁡ 2 − β 2 ​ 𝔼 ​ [ Δ t ] ≥ log ⁡ 2 − 3 ​ β 2 ​ L ​ W 1 ​ ( π t , π t − 1 ) ≥ log ⁡ 2 − 3 ​ β 2 ​ L ​ 2 C 0 D KL ( π t ∥ π t − 1 ) ⇒ log ⁡ 2 − ℒ DPO ​ ( θ , x ) ≤ 3 ​ β ​ L 2 ​ 2 C 0 D KL ( π t ∥ π t − 1 ) ⇒ D KL ( π t ∥ π t − 1 ) ≥ ( log ⁡ 2 − ℒ DPO ​ ( π t , π t − 1 ) ) 2 1 2 ​ β 2 ​ 3 2 ​ L 2 ​ 2 ​ C 0 D KL ( π t ∥ π t − 1 ) ≥ ( log ⁡ 2 − ℒ DPO ​ ( π t , π t − 1 ) ) 2 β 2 ​ 3 2 ​ L 2 ​ C 0 \footnotesize\begin{split}\mathcal{L}_{\mathrm{DPO}}(\theta;x)&\;\geq\;\log 2-\tfrac{\beta}{2}\,\mathbb{E}[\Delta_{t}]\\ &\;\geq\;\log 2-\tfrac{3\beta}{2}LW_{1}(\pi_{t},\pi_{t-1})\\ &\;\geq\;\log 2-\tfrac{3\beta}{2}L\sqrt{2C_{0}\,D_{\mathrm{KL}}(\pi_{t}\|\pi_{t-1})}\\ \Rightarrow\log 2-\mathcal{L}_{\mathrm{DPO}}(\theta;x)&\;\leq\;\tfrac{3\beta L}{2}\sqrt{2C_{0}D_{\mathrm{KL}}(\pi_{t}\|\pi_{t-1})}\\ \Rightarrow D_{\mathrm{KL}}(\pi_{t}\|\pi_{t-1})&\;\geq\;\frac{(\log 2-\mathcal{L}_{\mathrm{DPO}}(\pi_{t},\pi_{t-1}))^{2}}{\tfrac{1}{2}\beta^{2}3^{2}L^{2}2C_{0}}\\ D_{\mathrm{KL}}(\pi_{t}\|\pi_{t-1})&\geq\frac{(\log 2-\mathcal{L}_{\mathrm{DPO}}(\pi_{t},\pi_{t-1}))^{2}}{\beta^{2}3^{2}L^{2}C_{0}}\end{split} (25)

[133] p: Then, assume that there exists a constant M ≥ 1 M\geq 1 such that for all ( x , y ) (x,y) ,

[134] table: 1 M ≤ π t − 1 ​ ( y | x ) π t ​ ( y | x ) ≤ M . \frac{1}{M}\leq\frac{\pi_{t-1}(y|x)}{\pi_{t}(y|x)}\leq M. (26)

[135] p: This ensures that the predicted distributions of the LMM model at the previous learning step π t − 1 \pi_{t-1} and the current learning step π t \pi_{t} are mutually absolutely continuous and that their density ratio is uniformly bounded. In other words, it prevents the predictions of the LMM from collapsing across consecutive learning steps, ensuring a stable and smooth evolution of the output distribution during the continual learning procedure. Let h ⁡ ( x , y ) = π t − 1 ​ ( y | x ) π t ​ ( y | x ) h(x,y)=\frac{\pi_{t-1}(y|x)}{\pi_{t}(y|x)} denote the likelihood ratio. The forward and reverse KL divergence can be rewritten as follows

[136] table: D KL ( π t − 1 ∥ π t ) \displaystyle D_{\mathrm{KL}}(\pi_{t-1}\|\pi_{t}) = 𝔼 ( x , y ) ∼ π t ​ [ h ⁡ ( x , y ) ​ log ⁡ h ⁡ ( x , y ) ] , \displaystyle=\mathbb{E}_{(x,y)\sim\pi_{t}}\!\big[h(x,y)\log h(x,y)\big], (27) D KL ( π t ∥ π t − 1 ) \displaystyle D_{\mathrm{KL}}(\pi_{t}\|\pi_{t-1}) = 𝔼 ( x , y ) ∼ π t ​ [ − log ⁡ h ⁡ ( x , y ) ] , \displaystyle=\mathbb{E}_{(x,y)\sim\pi_{t}}\!\big[-\log h(x,y)\big], (28)

[137] p: where h ⁡ ( x , y ) = π t − 1 ​ ( y | x ) π t ​ ( y | x ) h(x,y)=\frac{\pi_{t-1}(y|x)}{\pi_{t}(y|x)} .

[138] p: Lower bound of D KL ( π t − 1 ∥ π t ) D_{\mathrm{KL}}(\pi_{t-1}\|\pi_{t}) . The function f ⁡ ( u ) = u ​ log ⁡ u f(u)=u\log u is convex with f ′′ ​ ( u ) = 1 / u f^{\prime\prime}(u)=1/u . On the interval [ 1 / M , M ] [1/M,M] , the smallest curvature is 1 / M 1/M . By the second-order convexity bound around u = 1 u=1 ,

[139] table: u ​ log ⁡ u ≥ ( u − 1 ) + 1 2 ​ M ​ ( u − 1 ) 2 . u\log u\;\geq\;(u-1)+\frac{1}{2M}(u-1)^{2}. (29)

[140] p: Since 𝔼 x , y ∼ π t ​ ( y | x ) ​ [ h ⁡ ( x , y ) − 1 ] = 0 \mathbb{E}_{x,y\sim\pi_{t}(y|x)}[h(x,y)-1]=0 , taking the expectation under π t \pi_{t} will result in

[141] table: D KL ( π t − 1 ∥ π t ) ≥ 1 2 ​ M 𝔼 π t [ ( h ( x , y ) − 1 ) 2 ] . D_{\mathrm{KL}}(\pi_{t-1}\|\pi_{t})\;\geq\;\frac{1}{2M}\,\mathbb{E}_{\pi_{t}}\!\big[(h(x,y)-1)^{2}\big]. (1)

[142] p: Upper bound of D KL ( π t ∥ π t − 1 ) D_{\mathrm{KL}}(\pi_{t}\|\pi_{t-1}) . Similarly, with g ⁡ ( u ) = − log ⁡ u g(u)=-\log u , we have g ′′ ​ ( u ) = 1 / u 2 g^{\prime\prime}(u)=1/u^{2} , and on [ 1 / M , M ] [1/M,M] , the largest curvature is M 2 M^{2} . Hence,

[143] table: − log ⁡ u ≤ ( 1 − u ) + M 2 2 ​ ( u − 1 ) 2 . -\log u\;\leq\;(1-u)+\frac{M^{2}}{2}(u-1)^{2}. (30)

[144] p: Then, taking expectation under π t \pi_{t} will result in

[145] table: D KL ( π t ∥ π t − 1 ) ≤ M 2 2 𝔼 π t [ ( h ( x , y ) − 1 ) 2 ] . D_{\mathrm{KL}}(\pi_{t}\|\pi_{t-1})\;\leq\;\frac{M^{2}}{2}\,\mathbb{E}_{\pi_{t}}\!\big[(h(x,y)-1)^{2}\big]. (31)

[146] p: From Eqn. ( 1 ) and and Eqn. ( 30 ), we can obtain

[147] table: D KL ( π t − 1 ∥ π t ) \displaystyle D_{\mathrm{KL}}(\pi_{t-1}\|\pi_{t}) ≥ 1 M 3 D KL ( π t ∥ π t − 1 ) . \displaystyle\geq\frac{1}{M^{3}}\,D_{\mathrm{KL}}(\pi_{t}\|\pi_{t-1}). (32)

[148] p: Then, let us define c = M 3 c=M^{3} . Eqn. ( 25 ) can be further derived as follows:

[149] table: D KL ( π t − 1 ∥ π t ) ≥ ( log ⁡ 2 − ℒ DPO ​ ( θ , x ) ) 2 c ​ β 2 ​ 3 2 ​ L 2 ​ C 0 ≥ 1 C lower ​ ( log ⁡ 2 − ℒ DPO ​ ( θ , x ) ) 2 \begin{split}D_{\mathrm{KL}}(\pi_{t-1}\|\pi_{t})&\geq\frac{(\log 2-\mathcal{L}_{\mathrm{DPO}}(\theta;x))^{2}}{c\beta^{2}3^{2}L^{2}C_{0}}\\ &\geq\frac{1}{C_{\mathrm{lower}}}(\log 2-\mathcal{L}_{\mathrm{DPO}}(\theta;x))^{2}\end{split} (33)

[150] p: where C lower = c ​ β 2 ​ 3 2 ​ L 2 ​ C 0 C_{\mathrm{lower}}=c\beta^{2}3^{2}L^{2}C_{0} .

[151] h3: A.2 Proof of Lemma 2

[152] h5: Remark 1. Mixture Sampling and Monotone Labeling.

[153] p: For each prompt x x , the output candidates are sampled from

[154] table: Q x = α π t − 1 ( ⋅ ∣ x ) + ( 1 − α ) π t ( ⋅ ∣ x ) with α ∈ ( 0 , 1 ] , Q_{x}\;=\;\alpha\,\pi_{t-1}(\cdot\mid x)\;+\;(1-\alpha)\,\pi_{t}(\cdot\mid x)\quad\text{with }\alpha\in(0,1], (34)

[155] p: and the selection kernel (human or reward model) chooses the preferred/dispreferred outputs ( y + , y − ) (y^{+},y^{-}) monotonically with the underlying reward, inducing pair marginals P x + , P x − P^{+}_{x},P^{-}_{x} that do not expand total variation beyond what is present in Q x Q_{x} . Formally, we have

[156] table: TV ( π t − 1 ( ⋅ ∣ x ) , π t ( ⋅ ∣ x ) ) ≤ 1 α TV ( P + , P − ) . \mathrm{TV}\!\big(\pi_{t-1}(\cdot\mid x),\,\pi_{t}(\cdot\mid x)\big)\;\;\leq\;\;\frac{1}{\alpha}\;\mathrm{TV}\!\big(P^{+},P^{-}\big). (35)

[157] p: Remark 1 is both natural and theoretically justified in the context of continual learning via DPO. The candidate responses of DPO are typically drawn from a mixture of the previous and current policies, Q x Q_{x} , to ensure balanced exposure to both past and newly adapted behaviors. The monotone labeling condition further indicates that the preference signal, whether derived from humans or a reward model, preserves the true reward ordering of outputs. Then, the total-variation inequality then follows from the data-processing principle, i.e., applying a monotone labeling kernel cannot increase statistical divergence between distributions. Intuitively, the preference selection process can only reveal discrepancies already present in the mixture Q x Q_{x} , not amplify them. Consequently, Remark 1 enforces a bounded relationship between the divergence of the induced pairwise marginals ( P x + , P x − ) (P_{x}^{+},P_{x}^{-}) and the divergence between the underlying policies ( π t − 1 , π t ) (\pi_{t-1},\pi_{t}) . In addition, this guarantees that updates to π t \pi_{t} remain geometrically close to π t − 1 \pi_{t-1} , providing a stability-adaptability balance in the continual learning setting, i.e., the model can adapt to new data or tasks while preventing catastrophic forgetting.

[158] p: Remark 2. Sign Consistency. The predictor π t \pi_{t} is Bayes-consistent in sign on the support of M x := 1 2 ​ ( P x + + P x − ) M_{x}:=\frac{1}{2}(P_{x}^{+}+P_{x}^{-}) :

[159] table: sgn ⁡ ( q θ ​ ( z ) − 1 2 ) = sgn ⁡ ( η ⁡ ( z ) − 1 2 ) for M x -a.e. ​ z , \mathrm{sgn}\!\big(q_{\theta}(z)-\tfrac{1}{2}\big)\;=\;\mathrm{sgn}\!\big(\eta(z)-\tfrac{1}{2}\big)\quad\text{for $M_{x}$-a.e. }z,

[160] p: where η ​ ( z ) = d ​ P x + d ⁡ ( P x + + P x − ) ​ ( z ) \eta(z)=\frac{dP_{x}^{+}}{d(P_{x}^{+}+P_{x}^{-})}(z) and q θ ​ ( z ) = σ ⁡ ( β ​ s θ ​ ( z ) ) q_{\theta}(z)=\sigma(\beta s_{\theta}(z)) with σ ⁡ ( u ) = 1 1 + e − u \sigma(u)=\tfrac{1}{1+e^{-u}} . This remark is standard in excess-risk calibration and holds whenever the logistic excess risk is sufficiently small to ensure boundary consistency.

[161] h6: Lemma 7

[162] p: Logistic Calibration for Pairs . Given P + P^{+} and P − P^{-} , the total variation of T ​ V ​ ( P + , P − ) TV(P^{+},P^{-}) will be bounded by the DPO loss:

[163] table: TV ⁡ ( P + , P − ) ≤ 2 ​ 2 ​ ℒ DPO ​ ( π t , π t − 1 ) − ℒ DPO ⋆ ​ ( π t , π t − 1 ) \footnotesize\mathrm{TV}\!\big(P^{+},P^{-}\big)\leq 2\sqrt{2}\sqrt{\,\mathcal{L}_{\mathrm{DPO}}(\pi_{t},\pi_{t-1})\;-\;\mathcal{L}_{\mathrm{DPO}}^{\star}(\pi_{t},\pi_{t-1})\,} (36)

[164] p: where ℒ DPO ⋆ ​ ( π t , π t − 1 ) \mathcal{L}_{\mathrm{DPO}}^{\star}(\pi_{t},\pi_{t-1}) is the Bayes-optimal logistic pairwise loss.

[165] p: Proof. Let us abbreviate P + = P x + P^{+}=P_{x}^{+} , P − = P x − P^{-}=P_{x}^{-} , and M = 1 2 ​ ( P + + P − ) M=\frac{1}{2}(P^{+}+P^{-}) . The DPO loss and its Bayes-optimal counterpart can be written as

[166] table: ℒ DPO ​ ( π t , π t − 1 ) = 𝔼 Z ∼ M ​ [ CE ⁡ ( η ⁡ ( Z ) , q θ ​ ( Z ) ) ] ℒ DPO ⋆ ​ ( π t , π t − 1 ) = 𝔼 Z ∼ M ​ [ CE ⁡ ( η ⁡ ( Z ) , η ⁡ ( Z ) ) ] \begin{split}\mathcal{L}_{\mathrm{DPO}}(\pi_{t},\pi_{t-1})&=\mathbb{E}_{Z\sim M}\!\big[\mathrm{CE}(\eta(Z),q_{\theta}(Z))\big]\\ \mathcal{L}_{\mathrm{DPO}}^{\star}(\pi_{t},\pi_{t-1})&=\mathbb{E}_{Z\sim M}\!\big[\mathrm{CE}(\eta(Z),\eta(Z))\big]\end{split} (37)

[167] p: where CE ⁡ ( ⋅ , ⋅ ) \mathrm{CE}(\cdot,\cdot) is the binary cross-entropy function, η ⁡ ( ⋅ ) \eta(\cdot) represents the true (Bayes-optimal) preference probability between positive and negative outcomes, q θ ​ ( Z ) q_{\theta}(Z) is model-predicted probability obtained from the logit margin of the LMM model. Then, the excess DPO risk is formed as:

[168] table: ℜ π t , π t − 1 ​ ( x ) = ℒ DPO ​ ( π t , π t − 1 ) − ℒ DPO ⋆ ​ ( π t , π t − 1 ) = 𝔼 Z ∼ M [ KL ( Bern ( η ( Z ) ) ∥ Bern ( q θ ( Z ) ) ) ] . \begin{split}\mathfrak{R}_{\pi_{t},\pi_{t-1}}(x)&=\mathcal{L}_{\mathrm{DPO}}(\pi_{t},\pi_{t-1})-\mathcal{L}_{\mathrm{DPO}}^{\star}(\pi_{t},\pi_{t-1})\\ &=\mathbb{E}_{Z\sim M}\!\Big[\mathrm{KL}\big(\mathrm{Bern}(\eta(Z))\,\big\|\,\mathrm{Bern}(q_{\theta}(Z))\big)\Big].\end{split} (38)

[169] p: where Bern \mathrm{Bern} is the Bernoulli distribution.

[170] p: Bernoulli Pinsker Inequality. For any z z , Pinsker’s inequality for Bernoulli distributions gives

[171] table: KL ( Bern ( η ( z ) ) ∥ Bern ( q θ ( z ) ) ) ≥ 2 ( η ( z ) − q θ ( z ) ) 2 . \mathrm{KL}\big(\mathrm{Bern}(\eta(z))\,\|\,\mathrm{Bern}(q_{\theta}(z))\big)\;\geq\;2\,(\eta(z)-q_{\theta}(z))^{2}. (39)

[172] p: Hence,

[173] table: 𝔼 M ​ [ ( η − q θ ) 2 ] ≤ 1 2 ​ ℜ π t , π t − 1 ​ ( x ) . \mathbb{E}_{M}[(\eta-q_{\theta})^{2}]\;\leq\;\frac{1}{2}\,\mathfrak{R}_{\pi_{t},\pi_{t-1}}(x). (40)

[174] p: Sign Consistency Implies Margin Control. Under Remark 2, since η \eta and q θ q_{\theta} lie on the same side of 1 2 \tfrac{1}{2} for almost every z z :

[175] table: | η ⁡ ( z ) − 1 2 | ≤ | η ⁡ ( z ) − q θ ​ ( z ) | + | q θ ​ ( z ) − 1 2 | ≤ 2 ​ | η ⁡ ( z ) − q θ ​ ( z ) | ⇒ | 2 ​ η ​ ( z ) − 1 | ≤ 4 ​ | η ⁡ ( z ) − q θ ​ ( z ) | \footnotesize\begin{split}|\eta(z)-\tfrac{1}{2}|\leq|\eta(z)-q_{\theta}(z)|+|q_{\theta}(z)-\tfrac{1}{2}|&\leq 2\,|\eta(z)-q_{\theta}(z)|\\ \Rightarrow|2\eta(z)-1|&\leq 4\,|\eta(z)-q_{\theta}(z)|\end{split} (41)

[176] p: By definition of total variation, we have

[177] table: TV ⁡ ( P + , P − ) = 𝔼 Z ∼ M ​ [ | 2 ​ η ​ ( Z ) − 1 | ] . \mathrm{TV}(P^{+},P^{-})=\mathbb{E}_{Z\sim M}\!\big[|2\eta(Z)-1|\big]. (42)

[178] p: Then, applying Eqn. ( 41 ) and Cauchy–Schwarz, we will receive

[179] table: TV ⁡ ( P + , P − ) ≤ 4 ​ 𝔼 M ​ | η − q θ | ≤ 4 ​ 𝔼 M ​ ( η − q θ ) 2 . \mathrm{TV}(P^{+},P^{-})\;\leq\;4\,\mathbb{E}_{M}|\eta-q_{\theta}|\;\leq\;4\,\sqrt{\mathbb{E}_{M}(\eta-q_{\theta})^{2}}. (43)

[180] p: Then, substitute Eqn.( 40 ) will result in

[181] table: TV ⁡ ( P + , P − ) ≤ 4 ​ 1 2 ​ ℜ π t , π t − 1 ​ ( x ) = 2 ​ 2 ​ ℒ DPO ​ ( π t , π t − 1 ) − ℒ DPO ⋆ ​ ( π t , π t − 1 ) . \begin{split}\mathrm{TV}(P^{+},P^{-})&\leq 4\,\sqrt{\tfrac{1}{2}\,\mathfrak{R}_{\pi_{t},\pi_{t-1}}(x)}\\ &=2\sqrt{2}\,\sqrt{\,\mathcal{L}_{\mathrm{DPO}}(\pi_{t},\pi_{t-1})-\mathcal{L}_{\mathrm{DPO}}^{\star}(\pi_{t},\pi_{t-1})\,}.\end{split} (44)

[182] p: Proof of Lemma 2 . By Pinsker’s inequality, we have

[183] table: TV ⁡ ( π t − 1 , π t ) ≤ 1 2 D KL ( π t − 1 ∥ π t ) , ⇒ D KL ( π t − 1 ∥ π t ) ≤ 2 ​ TV ​ ( π t − 1 , π t ) 2 . \begin{split}\mathrm{TV}\!\big(\pi_{t-1},\pi_{t}\big)&\;\leq\;\sqrt{\tfrac{1}{2}\,D_{\mathrm{KL}}\!\big(\pi_{t-1}\,\|\,\pi_{t}\big)},\\ \Rightarrow D_{\mathrm{KL}}\!\big(\pi_{t-1}\,\|\,\pi_{t}\big)&\;\leq\;2\,\mathrm{TV}\!\big(\pi_{t-1},\pi_{t}\big)^{2}.\end{split} (45)

[184] p: Then, substituting Remark 1 and Lemma 7 into Pinsker’s relation will result in

[185] table: D KL ( π t − 1 ∥ π t ) ≤ 2 ​ ( 2 ​ 2 α ​ ℒ DPO ​ ( π t , π t − 1 ) − ℒ DPO ⋆ ​ ( π t , π t − 1 ) ) 2 ≤ 16 α 2 ​ ( ℒ DPO ​ ( π t , π t − 1 ) − ℒ DPO ⋆ ​ ( π t , π t − 1 ) ) ≤ 16 α 2 ​ ℒ DPO ​ ( π t , π t − 1 ) = C upper ​ ℒ DPO ​ ( π t , π t − 1 ) \footnotesize\begin{split}D_{\mathrm{KL}}\!\big(\pi_{t-1}\,\|\,\pi_{t}\big)&\leq 2\left(\frac{2\sqrt{2}}{\alpha}\sqrt{\,\mathcal{L}_{\mathrm{DPO}}(\pi_{t},\pi_{t-1})-\mathcal{L}_{\mathrm{DPO}}^{\star}(\pi_{t},\pi_{t-1})\,}\right)^{2}\\ &\leq\frac{16}{\alpha^{2}}\left(\mathcal{L}_{\mathrm{DPO}}(\pi_{t},\pi_{t-1})-\mathcal{L}_{\mathrm{DPO}}^{\star}(\pi_{t},\pi_{t-1})\right)\\ &\leq\frac{16}{\alpha^{2}}\mathcal{L}_{\mathrm{DPO}}(\pi_{t},\pi_{t-1})\\ &=C_{\mathrm{upper}}\mathcal{L}_{\mathrm{DPO}}(\pi_{t},\pi_{t-1})\end{split} (46)

[186] p: where C upper = 16 α 2 C_{\mathrm{upper}}=\frac{16}{\alpha^{2}} .

[187] h3: A.3 Proof of Lemma 3

[188] p: Proof. Since log ⁡ p ≤ 0 \log p\leq 0 , one has 0 ≤ α γ ​ ( p ) ≤ ( 1 − p ) γ 0\;\leq\;\alpha_{\gamma}(p)\;\leq\;(1-p)^{\gamma} , and ( 1 − p ) γ → 0 (1-p)^{\gamma}\to 0 exponentially as γ → ∞ \gamma\to\infty . Then, for any fixed p ∈ ( 0 , 1 ) p\in(0,1) , we have lim γ → ∞ α γ ​ ( p ) = 0 \lim_{\gamma\to\infty}\alpha_{\gamma}(p)=0 . As a result, for each group k k , if p ⁡ ( z ) ∈ ( 0 , 1 ) p(z)\in(0,1) a.s. and 𝔼 [ ∥ ( p θ − 1 ) ∇ s θ ∥ ∣ G k ] < ∞ \mathbb{E}[\|(p_{\theta}-1)\nabla s_{\theta}\|\mid G_{k}]<\infty , then lim γ → ∞ w k γ ​ ( θ ) = 0 \lim_{\gamma\to\infty}w_{k}^{\gamma}(\theta)=0 . By definition, we have

[189] table: ‖ B γ ​ ( θ ) ‖ ≤ ∑ k = 1 K | q k − q k ′ | ​ | w k γ ​ ( θ ) | ​ ‖ m k ​ ( θ ) ‖ . \|B_{\gamma}(\theta)\|\;\leq\;\sum_{k=1}^{K}|q_{k}-q^{\prime}_{k}|\,|w_{k}^{\gamma}(\theta)|\,\|m_{k}(\theta)\|. (47)

[190] p: Since w k γ ​ ( θ ) → 0 w_{k}^{\gamma}(\theta)\to 0 for each k k as γ → ∞ \gamma\to\infty , the sum tends to 0 0 .

[191] h2: Appendix B DPO Data

[192] h3: B.1 Data Description

[193] p: We share a part of our data in the supplementary submission. Due to the file size limitations of the supplementary submission, we provide only a partial subset of the dataset used in our experiments. This subset is intended to illustrate the data structure, annotation format, and representative visual characteristics. The full dataset , including all images and finalized annotations, will be released publicly upon acceptance of the paper.

[194] h3: B.2 Copyright and Usage Notice

[195] p: All images included in this supplementary package remain the intellectual property of their original creators and data sources. We do not claim copyright over any raw images provided here. The images are included solely for scientific reference and reproducibility under fair-use guidelines.

[196] p: In the final version of the dataset, we will release the complete annotations produced in this work while preserving the copyright of all images. Access to the full image collection will be provided in accordance with the licensing and usage terms of the original datasets. Users of this supplementary material are responsible for ensuring that any use of these images complies with the corresponding copyright requirements.

[197] h2: Instructions for reporting errors

[198] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[199] p: Tip: You can select the relevant text first, to include it in your report.

[200] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[201] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
