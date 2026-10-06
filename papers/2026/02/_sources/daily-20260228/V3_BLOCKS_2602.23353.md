[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: SOTAlign: Semi-Supervised Alignment of Unimodal Vision and Language Models via Optimal Transport

[3] h6: Abstract

[4] p: The Platonic Representation Hypothesis posits that neural networks trained on different modalities converge toward a shared statistical model of the world. Recent work exploits this convergence by aligning frozen pretrained vision and language models with lightweight alignment layers, but typically relies on contrastive losses and millions of paired samples. In this work, we ask whether meaningful alignment can be achieved with substantially less supervision. We introduce a semi-supervised setting in which pretrained unimodal encoders are aligned using a small number of image–text pairs together with large amounts of unpaired data. To address this challenge, we propose SOTAlign, a two-stage framework that first recovers a coarse shared geometry from limited paired data using a linear teacher, then refines the alignment on unpaired samples via an optimal-transport-based divergence that transfers relational structure without overconstraining the target space. Unlike existing semi-supervised methods, SOTAlign effectively leverages unpaired images and text, learning robust joint embeddings across datasets and encoder pairs, and significantly outperforming supervised and semi-supervised baselines.

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] figure: Figure 1 : Semi-Supervised Vision-Language Alignment. We tackle the alignment of frozen unimodal encoders where paired data (red blocks) is scarce but unpaired data is abundant. The key challenge is: how to define a training signal for unpaired data when ground-truth cross-modal correspondences are missing?

[8] p: Vision-language models (VLMs) learn a shared embedding space for images and text, enabling zero-shot transfer to unseen concepts and domains. Since CLIP ( Radford et al., 2021 ) and ALIGN ( Jia et al., 2021 ) , the dominant paradigm has relied on large-scale contrastive training on paired image-text data, with performance improving predictably as supervision scales. While effective, this approach requires hundreds of millions of paired samples ( Cherti et al., 2023 ) , making VLMs costly to train and difficult to adapt when paired data are limited. This issue arises in many critical applications, such as specialized scientific, medical, or industrial domains, where collecting large-scale annotations is expensive, time-consuming, or infeasible.

[9] p: In this paper, we investigate vision–language alignment beyond large-scale supervision, asking whether meaningful alignment can be achieved from pretrained encoders using only a small number of paired samples together with abundant unimodal data. We posit that, under the Platonic Representation Hypothesis ( Huh et al., 2024 ) , unimodal models should already encode compatible semantic structures, making such alignment possible with minimal supervision.

[10] p: SOTAlign Overview. We focus on training lightweight alignment layers on top of pretrained unimodal encoders. In this setting, we first demonstrate that meaningful cross-modal alignment can be recovered from very few paired samples using simple linear methods, providing empirical support for the Platonic Representation Hypothesis. Then, we introduce SOTAlign (Semi-supervised Optimal Transport-based Alignment), a simple approach that enables to further refine such alignment by leveraging large unimodal datasets , achieving state-of-the-art results in this semi-supervised setting. SOTAlign relies on KLOT, an optimal-transport-based divergence that enables to transfer the initial geometric structure of the linear teacher while allowing sufficient flexibility to avoid underfitting. Critically, we derive the explicit gradient of KLOT divergence, removing the memory bottlenecks that have limited the scalability of previously optimal-transport-based alignment methods. In the experimental section, we implement strong supervised and semi-supervised baselines and demonstrate the superior performances of SOTAlign across a wide range of downstream tasks. We carefully explore the robustness of SOTAlign to a variety of factors such as the number of paired samples, the number of unimodal samples, and the pretrained unimodal models. Critically, we also show that SOTAlign can leverage samples from multiple sources simultaneously, for example combining unimodal images from ImageNet and captions from CC12M to improve performances on COCO despite a significant distribution shift.

[11] p: In short, we make the following contributions:

[12] p: We show that meaningful vision–language alignment can be recovered from very few paired samples using simple linear methods.

[13] p: We introduce SOTAlign, a semi-supervised approach that leverages unpaired unimodal data to achieve state-of-the-art alignment.

[14] p: We propose KLOT, a novel optimal-transport-based divergence, and fully address the memory bottlenecks that plagued prior OT-based methods.

[15] p: We validate the robustness of SOTAlign through extensive experiments across tasks, datasets, and encoders.

[16] h2: 2 Related Work

[17] p: Vision–Language Models. VLMs learn a joint embedding space for images and text, enabling zero-shot transfer across downstream tasks. CLIP ( Radford et al., 2021 ) established this paradigm through large-scale contrastive pretraining on 400 million image–text pairs, demonstrating that strong alignment can emerge from frozen pretrained encoders.

[18] p: Subsequent work has focused on scaling data and refining contrastive objectives to improve performance. ALIGN ( Jia et al., 2021 ) leveraged noisy web-scale supervision, while SigLIP ( Zhai et al., 2023 ) and SigLIPv2 ( Tschannen et al., 2025 ) introduced alternative losses and massive multilingual datasets, with SigLIPv2 training on WebLI, comprising 10 billion images and 12 billion alt-texts across 109 languages. These efforts are consistent with empirical scaling laws observed for CLIP-style models ( Cherti et al., 2023 ) , but also highlight a central limitation: achieving state-of-the-art performance requires millions or billions of paired samples , which is impractical in many settings and modalities.

[19] p: More recently, OT-CLIP ( Shi et al., 2024 ) proposed an Optimal Transport (OT) interpretation of the InfoNCE objective ( Oord et al., 2018 ) , viewing contrastive learning as inverse OT with a fixed identity transport plan. We adopt this perspective in the present work, but extend it beyond fully supervised settings by allowing target transport plans that are not restricted to the identity. Moreover, we derive an explicit expression for the gradient of the resulting objective (Theorem 5.1 ), removing the memory bottlenecks that have limited OT-based approaches to small batch sizes.

[20] p: The Platonic Representation Hypothesis. Huh et al. (2024) posit that neural networks trained on different modalities, architectures, or objectives tend to converge toward compatible latent representations that reflect shared underlying structure in the data. In the context of vision-language models, this perspective suggests that pretrained unimodal image and text encoders may already produce semantically aligned representations, even in the absence of explicit cross-modal training. This observation motivates an alternative approach to VLM construction, in which the pretrained encoders are kept frozen and only lightweight alignment layers are learned to reconcile their representation spaces. Several recent works adopt this paradigm, demonstrating that strong vision–language performance can be achieved by aligning frozen pretrained unimodal encoders rather than training multimodal models from scratch ( Vouitsis et al., 2024 ; Zhang et al., 2025a ; Maniparambil et al., 2025 ; Huang et al., 2025 ) . Our work follows this line of research, but focuses on regimes where paired supervision is severely limited.

[21] p: Low-Supervision Alignment. A growing body of work has explored alignment under weak, limited, or absent supervision. In unimodal settings, Jha et al. (2025) show that text embeddings can be aligned across representation spaces without paired data. Extending this idea to cross-modal alignment, Maniparambil et al. (2024) and Schnaus et al. (2025) demonstrate that vision–language representations can also be matched without supervision, but rely on quadratic assignment problem solvers that scale only to a few hundred samples, limiting applicability.

[22] p: Closer to our setting, S-CLIP ( Mo et al., 2023 ) introduces a semi-supervised framework in which optimal transport defines target similarities between unpaired images and paired captions, with promising results for domain adaptation of CLIP. In contrast, we define target similarities even between unpaired images and unpaired captions, enabling effective use of large-scale unimodal data on both sides (Figure 1 ). SUE ( Yacobi et al., 2025 ) also considers semi-supervised vision–language alignment, but is limited to a single dataset and a single downstream task. Our work generalizes this setting across tasks, datasets, and encoder combinations. Finally, STRUCTURE ( Gröger et al., 2025 ) augments InfoNCE with a regularization term encouraging preservation of unimodal geometry. While evaluated in supervised settings, this idea could in principle leverage unpaired data and is therefore included as a baseline in our experiments.

[23] h2: 3 Methodology

[24] figure: Figure 2 : SOTAlign is a two-step method for the alignment of pretrained unimodal image and text encoders. First, we fit a linear alignment model only using the limited amount of available image-text pairs. Then, we use this linear model as a teacher to regularize the training of alignment layers f f and g g for a joint embedding space leveraging unimodal (unpaired) data.

[25] p: Notations. For u , v ∈ ℝ d u,v\in\mathbb{R}^{d} , we denote the cosine similarity by k ⁡ ( u , v ) = ⟨ u , v ⟩ ‖ u ‖ ​ ‖ v ‖ k(u,v)=\frac{\langle u,v\rangle}{\left\lVert u\right\rVert\left\lVert v\right\rVert} . We stack batches of n n vectors as matrices in ℝ n × d \mathbb{R}^{n\times d} . Given U ∈ ℝ n × d U\in\mathbb{R}^{n\times d} and V ∈ ℝ m × d V\in\mathbb{R}^{m\times d} , we define the affinity matrix K ⁡ [ U , V ] ∈ ℝ n × m K[U,V]\in\mathbb{R}^{n\times m} with entries

[26] table: K ​ [ U , V ] i , j = k ⁡ ( U i , V j ) . K[U,V]_{i,j}=k(U_{i},V_{j}).

[27] p: We define the (row-wise) Softmax normalization as

[28] table: Softmax ε ⁡ ( K ) i , j = exp ⁡ ( K i , j / ε ) ∑ k = 1 n exp ⁡ ( K i , k / ε ) . \operatorname{Softmax}_{\varepsilon}(K)_{i,j}=\frac{\exp\!\left(\nicefrac{{K_{i,j}}}{{\varepsilon}}\right)}{\sum_{k=1}^{n}\exp\!\left(\nicefrac{{K_{i,k}}}{{\varepsilon}}\right)}.

[29] h3: 3.1 Problem Formulation

[30] p: We denote d x d_{x} (resp. d y d_{y} ) the latent dimension of the pretrained vision (resp. language) encoder. We consider the problem of learning alignment layers f θ 1 : ℝ d x → ℝ d f_{\theta_{1}}:\mathbb{R}^{d_{x}}\rightarrow\mathbb{R}^{d} and g θ 2 : ℝ d y → ℝ d g_{\theta_{2}}:\mathbb{R}^{d_{y}}\rightarrow\mathbb{R}^{d} that encode vision and language into a shared space of dimension d d , parametrized by θ = ( θ 1 , θ 2 ) \theta=(\theta_{1},\theta_{2}) .

[31] p: In this setting, the training objective is often formulated as minimizing the divergence between the geometry of the shared space and a target geometry. Formally, given a dataset of image and language embeddings X ∈ ℝ n × d x X\in\mathbb{R}^{n\times d_{x}} and Y ∈ ℝ n × d y Y\in\mathbb{R}^{n\times d_{y}} , the goal is to minimize

[32] table: ℒ ⁡ ( θ , X , Y ) = \displaystyle\mathcal{L}(\theta;X,Y)= (1) DIV ( K [ f θ 1 ( X ) , g θ 2 ( Y ) ] | | K ∗ [ X , Y ] ) , \displaystyle\operatorname{DIV}\!\left(K[f_{\theta_{1}}(X),\,g_{\theta_{2}}(Y)]\,\middle|\middle|\,K^{*}[X,Y]\right),

[33] p: where K ∗ K^{*} denotes the “target geometry” and DIV \operatorname{DIV} is some divergence between two affinity matrices. In the fully supervised setting, the dataset is made of pairs i.e. Y i Y_{i} is the caption of X i X_{i} and the target similarity is set to the identity

[34] table: K ∗ ​ [ X , Y ] = I n . K^{*}[X,Y]=I_{n}. (2)

[35] p: For instance, the InfoNCE loss ( Oord et al., 2018 )

[36] table: − 1 n ∑ i = 1 n log exp ⁡ ( K ​ [ f ⁡ ( X ) , g ⁡ ( Y ) ] i , i ) ∑ j = 1 n exp ⁡ ( K ​ [ f ⁡ ( X ) , g ⁡ ( Y ) ] i , j ) , -\frac{1}{n}\sum_{i=1}^{n}\log\frac{\exp\!\left(K\!\left[f(X),g(Y)\right]_{i,i}\right)}{\sum_{j=1}^{n}\exp\!\left(K\!\left[f(X),g(Y)\right]_{i,j}\right)}, (3)

[37] p: is a special case of ( 1 ) for K ∗ = I n K^{*}=I_{n} and DIV ( K | | K ∗ ) = lim ε → 0 KL ( Softmax ε ( K ∗ ) | | Softmax 1 ( K ) ) \operatorname{DIV}\!\left(K\,\middle|\middle|\,K^{*}\right)=\lim_{\varepsilon\to 0}\operatorname{KL}\!\left(\operatorname{Softmax}_{\varepsilon}(K^{*})\,\middle||\,\operatorname{Softmax}_{1}(K)\right) .

[38] p: Thus, the main challenge to extend these approaches to unsupervised data is to introduce a target K ∗ ​ [ X , Y ] K^{*}[X,Y] that is defined even if we don’t assume that X X and Y Y are pairs.

[39] h3: 3.2 Semi-Supervised Setting

[40] p: We consider a semi-supervised setting with three types of data. First, we observe a small set of paired samples ( A , B ) (A,B) , where A ∈ ℝ n p × d x A\in\mathbb{R}^{n_{p}\times d_{x}} and B ∈ ℝ n p × d y B\in\mathbb{R}^{n_{p}\times d_{y}} , and each row of A A is aligned with the corresponding row of B B . In addition, we have access to large collections of unpaired data: unlabeled images X ∈ ℝ n x × d x X\in\mathbb{R}^{n_{x}\times d_{x}} and unlabeled text Y ∈ ℝ n y × d y Y\in\mathbb{R}^{n_{y}\times d_{y}} . Finally, we assume that the number of supervised pairs is limited, i.e., n p ≪ n x n_{p}\ll n_{x} and n p ≪ n y . n_{p}\ll n_{y}. This setting is motivated by two considerations. First, it allows us to study how far supervision can be reduced while still enabling the recovery of a meaningful alignment between modalities, providing a direct test of the Platonic Representation Hypothesis. Second, such a regime reflects many practical scenarios in multimodal learning, where collecting paired data is expensive or infeasible and only a small number of aligned samples is available.

[41] h3: 3.3 SOTAlign

[42] p: We address this setting with a two step approach:

[43] p: First, we fit a a simple linear alignment model with the supervised pairs ( A , B ) (A,B) . We denote W x ∈ ℝ d x × d ′ W_{x}\in\mathbb{R}^{d_{x}\times d^{\prime}} and W y ∈ ℝ d y × d ′ W_{y}\in\mathbb{R}^{d_{y}\times d^{\prime}} the linear projections produced by this model. An important finding of this work is that such linear models already yield surprisingly strong alignment . We dedicate Section 4 to this fundamental component of our method.

[44] p: Then we use this linear model to regularize the training of the final alignment layers f θ 1 f_{\theta_{1}} and g θ 2 g_{\theta_{2}} in a pseudo-labeling fashion. More precisely, we constrain the geometry of the learned shared space to stay close to that produced by the linear teacher. This regularization writes as

[45] table: Ω ⁡ ( θ , X , Y ) = \displaystyle\Omega(\theta;X,Y)= (4) DIV ( K [ f θ 1 ( X ) , g θ 2 ( Y ) ] ) | | K [ X W x T , Y W y T ] ) , \displaystyle\operatorname{DIV}\!\left(K\left[f_{\theta_{1}}(X),g_{\theta_{2}}(Y)]\right)\,\middle|\middle|\,K[XW_{x}^{T},YW_{y}^{T}]\right),

[46] p: where the choice of the divergence DIV \operatorname{DIV} is the second core component of the method and is discussed in Section 5 .

[47] p: Finally, our training loss is

[48] table: ℒ α ​ ( θ , A , B , X , Y ) = ℒ ⁡ ( θ , A , B ) + α ​ Ω ​ ( θ , X , Y ) , \mathcal{L}_{\alpha}(\theta;A,B,X,Y)=\mathcal{L}(\theta;A,B)+\alpha\Omega(\theta;X,Y), (5)

[49] p: where α \alpha controls the strength of the regularization.

[50] figure: Algorithm 1 SOTAlign Training 0: ( A , B ) , X , Y (A,B),X,Y 1: ( W x , W ​ y ) ← LinearAlignement ​ ( A , B ) (W_{x},Wy)\leftarrow\text{LinearAlignement}(A,B) 2: Initialize encoders f f and g g 3: for i = 1 , … , T i=1,\dots,T do 4: Sample X b ∼ X X_{b}\sim X # Sample batch of image embeddings 5: Sample Y b ∼ Y Y_{b}\sim Y # Sample batch of text embeddings 6: K ∗ ← cosine ​ ( X b ​ W x ⊤ , Y b ​ W y ⊤ ) K^{*}\leftarrow\text{cosine}(X_{b}W_{x}^{\top},Y_{b}W_{y}^{\top}) 7: K ← cosine ​ ( f ⁡ ( X b ) , g ⁡ ( Y b ) ) K\leftarrow\text{cosine}(f(X_{b}),g(Y_{b})) 8: K p ← cosine ​ ( f ⁡ ( A ) , g ⁡ ( B ) ) K_{p}\leftarrow\text{cosine}(f(A),g(B)) 9: ℒ ← SigLIP ⁡ ( K p , I n p ) + α ​ KLOT ⁡ ( K , K ∗ ) \mathcal{L}\leftarrow\operatorname{SigLIP}(K_{p},I_{n_{p}})+\alpha\operatorname{KLOT}(K,K^{*}) 10: Update f , g f,g using ∇ ℒ \nabla\mathcal{L} 11: end for

[51] h2: 4 Linear Alignment Model

[52] p: The first core component of the proposed method is the linear alignment model. This model is trained with the limited amount of pairs available and then used as a teacher to regularize the training of the full semi-supervised model. As highlighted in the experimental section, such linear models achieve surprisingly strong alignment performances. We now discuss a selection of suitable candidates.

[53] p: Procrustes Alignment. In the Orthogonal Procrustes problem, one tries to align two point clouds by looking for the orthogonal transformation that minimizes the RMSE ( Schönemann, 1966 ) . We slightly adapt its formulation to our setting by looking for two orthogonal transformations that map the pairs ( A , B ) (A,B) to a shared space. Formally,

[54] table: ( W x , W y ) \displaystyle(W_{x},W_{y}) = arg ⁡ max P , Q ​ ⟨ A ​ P ⊤ , B ​ Q ⊤ ⟩ \displaystyle=\arg\max_{P,Q}\,\langle AP^{\top},BQ^{\top}\rangle (6) s.t. P ​ P ⊤ = Q ​ Q ⊤ = I d ′ \displaystyle\text{s.t.}\quad PP^{\top}=QQ^{\top}=I_{d^{\prime}}

[55] p: This formulation assumes that the data is first centered and normalized which is omitted here for the sake of simplicity.

[56] p: Canonical Correlation Analysis. In statistics, CCA is used to find a space in which two random variable are maximally correlated which each others ( Mardia et al., 2024 ) . Transposing to our setting, the two random variables are the text and image embeddings and CCA writes as

[57] table: ( W x , W y ) = arg ⁡ max P , Q ​ ⟨ A ​ P ⊤ , B ​ Q ⊤ ⟩ \displaystyle(W_{x},W_{y})=\arg\max_{P,Q}\,\langle AP^{\top},BQ^{\top}\rangle (7) s.t. \displaystyle\text{s.t.} ( A ​ P ⊤ ) ⊤ ​ ( A ​ P ⊤ ) = ( B ​ Q ⊤ ) ⊤ ​ ( B ​ Q ⊤ ) = I d ′ \displaystyle(AP^{\top})^{\top}(AP^{\top})=(BQ^{\top})^{\top}(BQ^{\top})=I_{d^{\prime}}

[58] p: The main difference from Procrustes is that the orthogonality constraint is applied to the shared space directions instead of the transformation itself. The solutions to Equation ( 6 ) and ( 7 ) are provided in Appendix C.1 .

[59] p: Contrastive Learning. Finally, perhaps the most natural choice is to consider a linear projection trained with a classical contrastive learning approach, formally

[60] table: ( W x , W y ) = arg min P , Q DIV ( K [ A P T , B Q T ] | | I n p ) , (W_{x},W_{y})=\arg\min_{P,Q}\,\operatorname{DIV}\!\left(K[AP^{T},BQ^{T}]\,\middle|\middle|\,I_{n_{p}}\right), (8)

[61] p: where DIV \operatorname{DIV} is the InfoNCE loss defined in equation ( 3 ) or an alternative such as the SigLIP loss ( Zhai et al., 2023 ) .

[62] h2: 5 Choice of Divergence

[63] p: The second core component of our method is the choice of a divergence DIV ( K | | K ∗ ) \operatorname{DIV}\!\left(K\,\middle|\middle|\,K^{\ast}\right) , where K , K ∗ ∈ ℝ n × n K,K^{\ast}\in\mathbb{R}^{n\times n} denote, respectively, the affinity matrix induced by the trainable shared representation and the target affinity matrix. This section examines several possible choices for this divergence and discusses their respective strengths and limitations.

[64] p: Centered Kernel Alignment. One of the most popular ways to compare affinity/kernel matrices is Centered Kernel Alignment (CKA) ( Cristianini et al., 2001 ) . Denoting H = I n − 𝟙𝟙 T H=I_{n}-\mathbbm{1}\mathbbm{1}^{T} , CKA writes as

[65] table: CKA ​ ( K , K ∗ ) = ⟨ K ​ H , H ​ K ∗ ⟩ ⟨ K ​ H , H ​ K ⟩ ​ ⟨ K ∗ ​ H , H ​ K ∗ ⟩ . \text{CKA}(K,K^{*})=\frac{\langle KH,HK^{*}\rangle}{\sqrt{\langle KH,HK\rangle\langle K^{*}H,HK^{*}\rangle}}. (9)

[66] p: CKA admits a linear-time computation in the batch size n n when implemented via kernel factorizations (Proposition C.6 ), which constitutes a non-negligible practical property for alignment methods operating with large batches ( Zhang et al., 2025a ) . However, CKA also suffers from known limitations ( Davari et al., 2022 ) and, more importantly in our setting, enforces a strong constraint of the form K ≈ K ∗ K\approx K^{\ast} . This can be overly restrictive when K ∗ K^{\ast} is only intended as a regularizing signal provided by a linear teacher, rather than an exact target geometry.

[67] p: Generalized InfoNCE. As highlighted above, it might be beneficial to use a regularization that does not enforce K K to be exactly aligned with K ∗ K^{*} . To this end, one can consider the generalized InfoNCE loss ( Shi et al., 2024 ) as it only enforces that arg ​ max j ⁡ K i , j ≈ arg ​ max j ⁡ K i , j ∗ \argmax_{j}K_{i,j}\approx\argmax_{j}K^{*}_{i,j} . This is achieved by first applying a Softmax on the affinity matrices before comparing them, i.e.,

[68] table: InfoNCE ( K ∣ ∣ K ∗ ) = \displaystyle\operatorname{InfoNCE}(K\mid\mid K^{*})= (10) KL ( Softmax ϵ ∗ ( K ∗ ) | | Softmax ϵ ( K ) ) . \displaystyle\operatorname{KL}\!\left(\operatorname{Softmax}_{\epsilon^{*}}(K^{*})\,\middle||\,\operatorname{Softmax}_{\epsilon}(K)\right).

[69] p: The classical version is recovered for ε ∗ → 0 \varepsilon^{*}\!\to\!0 and K ∗ = I n K^{*}=I_{n} .

[70] p: KLOT. Given the previous interpretation of InfoNCE, we consider a natural extension that seeks the preservation of the entire Optimal Transport (OT) plan instead of only the nearest neighbor. Introducing Π n = { P ∈ ℝ + n × n | P 𝟏 = 𝟏 , P ⊤ 𝟏 = 𝟏 } , \Pi_{n}=\bigl\{\,P\in\mathbb{R}_{+}^{n\times n}\;\big|\;P\mathbf{1}=\mathbf{1},\;P^{\top}\mathbf{1}=\mathbf{1}\,\bigr\}, the OT plan is defined as

[71] table: O ​ T ϵ ​ ( K ) = arg ​ min P ∈ Π n − ⟨ P , K ⟩ + ϵ ​ H ​ ( P ) , OT_{\epsilon}(K)=\argmin_{P\in\Pi_{n}}-\langle P,K\rangle+\epsilon H(P), (11)

[72] p: where H ⁡ ( P ) = ⟨ P , log ⁡ P ⟩ H(P)=\langle P,\log P\rangle is the negative entropy. Note that it is a natural extension of Softmax as Softmax ϵ ⁡ ( K ) = arg ​ min P ​ 𝟏 = 𝟏 − ⟨ P , K ⟩ + ϵ ​ H ​ ( P ) \operatorname{Softmax}_{\epsilon}(K)=\argmin_{P\mathbf{1}=\mathbf{1}}-\langle P,K\rangle+\epsilon H(P) and, similarly to Softmax, setting ϵ = 0 \epsilon=0 recovers a strict one-to-one mapping. More details about OT are available in Appendix C.2 .

[73] p: Then, we define the KLOT divergence as

[74] table: KLOT ( K ∣ ∣ K ∗ ) = KL ( O T ϵ ∗ ( K ∗ ) | | O T ϵ ( K ) ) . \operatorname{KLOT}(K\mid\mid K^{*})=\operatorname{KL}\!\left(OT_{\epsilon^{*}}(K^{*})\,\middle||\,OT_{\epsilon}(K)\right). (12)

[75] p: This formulation is similar to that proposed by Van Assel et al. (2023) for the purpose of dimensionality reduction and generalizes ( Shi et al., 2024 ) beyond K ∗ = I n K^{*}=I_{n} .

[76] p: The main limitation of KLOT ( 5 ) is that O ​ T ϵ ​ ( K ) OT_{\epsilon}(K) does not admit a closed-form solution. While the Sinkhorn algorithm ( Cuturi, 2013 ) provides fast convergence on GPUs, computing the gradient ∇ K O ​ T ϵ ​ ( K ) \nabla_{K}OT_{\epsilon}(K) remains challenging. Existing approaches rely either on backpropagating through the Sinkhorn iterations by unrolling the algorithm ( Genevay et al., 2018 ) , which induces a severe memory bottleneck, or on implicit differentiation techniques ( Eisenberger et al., 2022 ) , which significantly increase time complexity. We fully address this limitation by deriving an explicit expression for the gradient (Theorem 5.1 ).

[77] h6: Theorem 5.1 .

[78] p: For any transport plan P ∈ Π n P\in\Pi_{n} ,

[79] table: ∇ K KLOT ( K ∣ ∣ K ∗ ) = OT ϵ ​ ( K ) − OT ϵ ∗ ​ ( K ∗ ) ϵ ∗ . \nabla_{K}\operatorname{KLOT}(K\mid\mid K^{*})=\frac{\text{OT}_{\epsilon}(K)-\text{OT}_{\epsilon^{*}}(K^{*})}{\epsilon^{*}}. (13)

[80] p: Proof is provided in Appendix C.2 .

[81] p: As illustrated in Figure 3 , our approach removes the memory bottleneck inherent to Sinkhorn unrolling and can be up to 50 × 50\times faster than implicit differentiation (Figure 6 ). This is a general result that could potentially apply to a range of OT-based methods using similar objectives, including recent approaches in model alignment and contrastive learning ( Van Assel et al., 2023 ; Mo et al., 2023 ; Shi et al., 2024 ) .

[82] figure: Figure 3 : GPU memory usage for a batchsize n = 10 n=10 k when computing the gradient of the OT-based divergence with naive solver unrolling (blue) and the provided explicit gradient formula (orange). Additionnal results are reported in appendix B.1 .

[83] h2: 6 Experiments

[84] p: Experimental Setting. We train all models using a maximum batch size of 32k, composed of up to 10k paired samples and completed with unpaired images and text. We use the LION optimizer ( Chen et al., 2023 ) with a cosine annealing learning-rate schedule, a maximum learning rate of 10 − 4 10^{-4} , and a weight decay of 10 − 5 10^{-5} , and train for 2000 iterations. For the supervised component of the loss, we employ the SigLIP objective, initializing the logit scale to 20 20 and the logit bias to − 10 -10 , with both parameters learned during training. Unless otherwise specified, we use DINOv3 ViT-L ( Siméoni et al., 2025 ) and NV-Embed-v2 ( Lee et al., 2025 ) as the pretrained vision and language encoders, respectively. By default, experiments are conducted with 10k paired samples and, when applicable, up to 1M unpaired images and texts drawn from CC3M ( Sharma et al., 2018 ) . We vary the weight of the regularization in Equation 5 over α ∈ { 10 − 3 , 10 − 4 , 10 − 5 } \alpha\in\{10^{-3},10^{-4},10^{-5}\} and select it based on retrieval performance on CC3M, accounting for different ratios of supervised to unsupervised data. We show in Section 6.2 that comparable results can be obtained with alternative settings.

[85] p: By default, the metric that we report is the average of the text-to-image (T2I) and image-to-text (I2T) retrieval (Recall@1) performance on the COCO validation set which we denote MeanR@1.

[86] h3: 6.1 Ablation Studies

[87] p: Linear Methods. SOTAlign employs a linear teacher which can be fit using the methods described in Section 4 . We report the standalone zero-shot retrieval performance of these linear models when trained on only 10k image-text pairs from CC3M in the first row of Table 1 . Notably, even the closed form models (CCA and Procrustes) reach MeanR@1 scores larger than 21%. The linear contrastive approach (SigLIP loss, SAIL baseline) reaches 24.2% and will serve as the main supervised baseline.

[88] p: Divergences. To align the teacher’s affinity matrix with the affinity matrix in the learnable shared space, SOTAlign can utilize any of the three divergences detailed in Section 5 . Table 1 displays all combinations of linear methods and divergences. Critically, we observe that the proposed OT-based divergence KLOT systematically outperforms the classical alternatives. The best results is achieved for CCA and KLOT and we select this setting for the next experiments.

[89] figure: Table 1 : Comparison of linear methods across different divergences. Zero-shot retrieval on COCO (MeanR@1). “None” indicates the standalone performances of the linear method. Linear Method Divergence Procrustes CCA Contrastive None 21.1 21.5 24.2 CKA 23.5 23.5 24.2 InfoNCE 23.9 24.1 26.5 KLOT 30.0 30.3 28.5

[90] figure: Figure 4 : Left: Effect of the number of paired samples (while fixing 1M unpaired samples). Right: Effect of the number of unpaired samples (while fixing 10k pairs). We report the zero-shot retrieval (MeanR@1) on COCO. More metrics are reported in Appendix B .

[91] h3: 6.2 Robustness of SOTAlign

[92] p: Number of Supervised Pairs. We first analyze how the number of paired image–text samples affects downstream performance. In this experiment, we fix the amount of unpaired data to 1M images and 1M text samples from CC3M, and vary the number of paired examples from 10 2 10^{2} to 10 5 10^{5} . Figure 4 reports zero-shot retrieval results. Across all supervision levels, SOTAlign consistently outperforms the supervised SAIL baseline, with gains of up to + 10 % +10\% accuracy in the intermediate regime between 10 3 10^{3} and 10 4 10^{4} pairs. As expected, these gains diminish as the number of paired samples increases, and both methods fail under extremely sparse supervision (100 pairs). Overall, SOTAlign reaches the same performances as SAIL with roughly 4 times less supervision.

[93] p: Number of Unsupervised Samples. Next, we investigate the effect of unpaired data on downstream performance. In this experiment, we fix the number of pairs to 10k, and vary the number of additional unpaired image and text samples between 10 4 10^{4} and 10 6 10^{6} . Figure 4 shows that our method successfully leverages unpaired data for zero-shot retrieval. We observe consistent gains from the unpaired data up to 500k unpaired samples.

[94] figure: Figure 5 : Relationship between the total sliced Wasserstein distance between CC3M image/text dataset and unimodal datasets, and the downstream performance of SOTAlign trained on 10k CC3M image–text pairs and up to 1M samples from the corresponding unimodal datasets.

[95] p: Unsupervised Data Source. We further evaluate our method in a challenging cross-dataset regime where unpaired images and texts originate from entirely different sources ( Table 7 ). Using a fixed set of 10k paired samples from CC3M, we introduce unpaired unimodal data from CC12M, COCO, and ImageNet-1k, as well as synthetic captions. Despite these shifts in the data distributions, our approach consistently outperforms the supervised baseline. Notably, incorporating ImageNet-1k images improves classification performance, while leveraging COCO samples yields retrieval gains by narrowing the gap to the test distribution. These results demonstrate that our framework can effectively exploit unpaired data even when the visual and textual modalities are drawn from disjoint, heterogeneous corpora.

[96] p: Quantifying the Distribution Shift. Motivated by these results, we next seek to quantify the effect of distribution shift and relate it to the observed performance gains. Given a source of unpaired data 𝒟 = ( X , Y ) \mathcal{D}=(X,Y) and the paired dataset 𝒟 p = ( A , B ) \mathcal{D}_{p}=(A,B) , we define the distribution shift as

[97] table: d ⁡ ( 𝒟 , 𝒟 p ) = SSW ⁡ ( X , A ) + SSW ⁡ ( Y , B ) , \mathrm{d}(\mathcal{D},\mathcal{D}_{p})=\mathrm{SSW}(X,A)+\mathrm{SSW}(Y,B), (14)

[98] p: where SSW \mathrm{SSW} denotes the Spherical Sliced Wasserstein distance ( Liu et al., 2024 ) , with details in Appendix C.2 . We adopt this metric because it is scalable to large datasets, well suited to unit-normalized embeddings, and does not require X X and A A (or Y Y and B B ) to be aligned. As shown in Figure 5 , this distance strongly correlates with downstream performance: unpaired data that are closer to the paired distribution consistently yield larger performance gains when incorporated during training.

[99] p: Supervised Data Source. We next study the impact of the paired data source on SOTAlign performance ( Table 2 ), while fixing the unpaired data to 1M samples from CC3M. Varying the source of the 10k image–text pairs reveals that higher-quality supervision can substantially influence alignment. In particular, using CC3M pairs with synthetic captions yields a notable improvement in retrieval performance (+4.8% T2I R@1), suggesting that cleaner textual supervision better guides the exploitation of noisy unpaired data. While pairs drawn from the larger CC12M corpus improve ImageNet classification, the strongest retrieval performance is obtained when using COCO pairs.

[100] p: Unimodal Encoders. In the same vein, we examine the impact of the choice of unimodal encoders on zero-shot classification and retrieval performance. We fix the training data to the standard setting of 10k paired samples and 1M unpaired samples from CC3M, and vary only the vision and language encoders. As reported in Table 3 , aligning DINOv3 ViT-L with NV-Embed-v2 yields the strongest downstream performance, achieving 46.1% accuracy on ImageNet and 26.5% T2I R@1 on COCO. Among the evaluated vision models, DINOv3 consistently outperforms earlier variants, which we attribute to its substantially larger pretraining corpus of 1.7 billion images, compared to 142 million for DINOv2. This trend aligns with the Platonic Representation Hypothesis ( Huh et al., 2024 ) , which suggests that as models scale in data and capacity, their representation spaces increasingly converge. We hypothesize that this intrinsic convergence reduces the alignment gap between modalities, thereby facilitating semi-supervised alignment with SOTAlign. In Appendix B , we reveal a strong positive correlation between representational similarity and downstream MeanR@1 (Pearson r = 0.83 r=0.83 ).

[101] figure: Table 2 : SOTAlign compared to supervised SAIL across different paired datasets (10k pairs) and 1M unpaired samples from CC3M. Zero-shot retrieval on COCO (MeanR@1). Green values ( + ) represent the absolute gain. Paired data Method ImageNet 1K COCO T2I COCO I2T CC3M SAIL 35.6 21.0 27.4 SOTAlign 46.1 +10.5 26.5 +5.5 34.1 +6.7 CC3M SAIL 36.2 28.3 37.2 synthetic SOTAlign 46.5 +10.3 31.3 +3.0 43.1 +5.9 CC12M SAIL 38.5 20.1 27.2 SOTAlign 47.4 +8.9 26.1 +6.0 36.3 +9.1 COCO SAIL 21.8 30.7 42.4 SOTAlign 35.8 +14.0 34.8 +4.1 46.7 +4.3

[102] figure: Table 3 : SOTAlign trained on 10k pairs and 1M unpaired samples from CC3M with different unimodal encoders. Zero-shot classification (top-1 acc) and retrieval (R@1). Green values represent the absolute gain over supervised SAIL. Vision Model Language Model ImageNet 1K COCO T2I COCO I2T DINOv2 Nemotron-8B 32.4 +6.9 15.5 +3.8 23.3 +5.3 Qwen3-8B 39.5 +7.7 20.9 +4.1 31.1 +7.3 NV-Embed-v2 42.5 +9.8 23.1 +4.1 31.1 +7.7 DINOv3 Nemotron-8B 35.5 +10.1 16.6 +3.8 26.2 +5.2 Qwen3-8B 42.7 +9.3 24.1 +5.0 35.3 +7.3 NV-Embed-v2 46.1 +10.5 26.5 +5.5 34.1 +6.7

[103] h3: 6.3 Benchmarking Semi-Supervised Alignment

[104] p: Baselines. Since the semi-supervised alignment setting we consider is relatively unexplored, there are no established standard baselines. We therefore compare SOTAlign against a range of supervised and semi-supervised methods which we adapt to our setting. The primary supervised baseline is SAIL ( Zhang et al., 2025a ) , trained on paired image–text data with a SigLIP loss; we also propose a semi-supervised variant that incorporates unpaired samples as additional negatives. We further consider STRUCTURE ( Gröger et al., 2025 ) , which regularizes joint embeddings to preserve unimodal geometry, and evaluate this term using either paired data only or both paired and unpaired samples. In addition, we include pseudo-labeling approaches that construct synthetic pairs from similarity distributions, including NNCLR ( Dwibedi et al., 2021 ) (as used in DeCLIP ( Li et al., 2022 ) ) and S-CLIP ( Mo et al., 2023 ) . Finally, we compare against SUE ( Yacobi et al., 2025 ) , a semi-supervised alignment method restricted to retrieval on a single dataset. Full details of all baselines are provided in Appendix A.2 .

[105] figure: Table 4 : Zero-shot image-text retrieval (Recall@1) on COCO and Flickr30. Comparison of supervised and semi-supervised methods trained with 10k image-text pairs and 1M unpaired samples from CC3M. Upper bound with 1M supervised pairs in grey. COCO Flickr30k Method T2I I2T T2I I2T Sup. SAIL (1M) 35.5 45.5 63.1 75.0 SAIL 21.0 27.4 45.7 54.1 STRUCTURE 21.0 28.7 46.8 54.0 Semi-sup. SAIL 20.7 26.5 44.9 53.1 STRUCTURE 20.9 28.0 45.7 56.0 NNCLR 21.3 27.9 46.6 53.0 S-CLIP 20.4 27.8 44.5 52.6 SOTAlign (Ours) 26.5 34.1 51.7 60.8

[106] figure: Table 5 : Zero-shot image classification (top-1 accuracy). Comparison of supervised and semi-supervised methods trained with 10k image-text pairs and 1M unpaired samples from CC3M. Upper bound with 1M supervised pairs in grey. Method Food-101 CIFAR-10 CIFAR-100 DTD ImageNet Sup. SAIL (1M) 63.9 97.8 82.3 53.5 56.4 SAIL 36.4 96.2 71.2 36.8 35.6 STRUCTURE 38.5 96.7 72.2 39.5 38.2 Semi-sup. SAIL 36.5 96.2 71.3 35.9 35.6 STRUCTURE 37.6 96.5 70.8 38.7 36.8 NNCLR 37.9 96.5 73.0 38.8 37.4 S-CLIP 35.3 95.9 69.3 37.6 36.4 SOTAlign (Ours) 50.0 97.5 78.3 42.4 46.1

[107] p: Zero-Shot Image-Text Retrieval. We evaluate SOTAlign against these baselines in T2I and I2T retrieval on COCO ( Lin et al., 2014 ) and Flickr30k ( Plummer et al., 2015 ) , and report the results in Table 4 . In the low-resource regime with 10k image-text pairs, the supervised baseline SAIL reaches 21.0 T2I R@1 and 27.4 I2T R@1. STRUCTURE performs marginally better benefiting from its structure-preservation objective. However, both methods fail to exploit unpaired data, either as additional negatives or for structure preservation. Notably, even the adapted semi-supervised approaches, NNCLR and S-CLIP, are unable to successfully exploit unpaired data. S-CLIP has been originally developed for domain adaptation and appears less robust when confronted with the large diversity of unpaired samples in our setting. Its pseudo-labels are further limited to the small set of paired instances. In contrast, SOTAlign successfully leverages the 1M unpaired images and text from CC3M to improve cross-modal alignment. On Flickr30k, our method reaches 51.7 T2I R@1 and 60.8 I2T R@1, yielding gains of +4.9 and +4.8 over the strongest baselines, respectively. For comparison, we include in gray the supervised upper bound obtained by training SAIL with 1M paired examples.

[108] p: Zero-Shot Image Classification. We further evaluate SOTAlign in zero-shot classification on ImageNet ( Deng et al., 2009 ) and more fine-grained classification datasets. The results are displayed in Table 5 and mirror the trends observed in zero-shot retrieval. STRUCTURE outperforms SAIL in the supervised setting, but is not able to leverage unpaired data for additional performance gains. Existing semi-supervised methods like NNCLR and S-CLIP do not show any improvements over the supervised baselines. Only SOTAlign is able to leverage 1M unpaired samples during alignment to improve zero-shot image classification. Our method achieves an ImageNet top-1 accuracy of 46.1%, which is an improvement of +7.9 over the best baseline. In grey we display the supervised SAIL baseline trained on 1M image-text pairs as an upper bound.

[109] p: Alignment per Dataset. Yacobi et al. (2025) study semi-supervised vision–language alignment using pretrained encoders, but under a substantially simpler setting than ours: their method operates within a single dataset, with paired and unpaired samples drawn from the same distribution and evaluation restricted to retrieval on small test splits (400 samples). In contrast, our setting involves cross-dataset unpaired data and multiple downstream tasks. Nevertheless, when evaluated in their setting, SOTAlign consistently outperforms SUE ( Yacobi et al., 2025 ) and its baselines, achieving gains of +14.3 I2T R@5 on COCO, +40.0 on Flickr30k, and +32.5 on Polyvore (see Table 6 ).

[110] figure: Table 6 : Alignment per dataset. Following the setup of SUE ( Yacobi et al., 2025 ) , we train for alignment per dataset and evaluate image-text retrieval (Recall@5). COCO Flickr30k Polyvore 100 Pairs 500 Pairs 500 Pairs Method I2T T2I I2T T2I I2T T2I CSA 1.3 1.0 1.3 0.8 1.3 1.0 Contrastive 8.5 5.8 9.5 9.8 13.8 11.5 SUE 21.5 18.3 19.8 22.0 22.8 20.8 SOTAlign (Ours) 35.8 35.0 59.8 63.3 55.3 55.3

[111] h2: 7 Conclusion

[112] p: In this work, we introduced a semi-supervised setting for aligning pretrained unimodal encoders, which we believe is relevant to many real-world modalities where large-scale paired data are scarce. We argue that Vision–Language alignment provides an ideal testbed for this problem, as abundant paired data enable systematic exploration of different supervision regimes. To the best of our knowledge, SOTAlign is the first model that can effectively leverage large-scale unimodal data for multi-modal alignment in this setting. We hope that the simplicity of SOTAlign will inspire future work on multi-modal representation alignment beyond fully supervised regimes.

[113] h2: Acknowledgments

[114] p: This work was partially funded by the ERC (853489 - DEXIM) and the Alfried Krupp von Bohlen und Halbach Foundation, which we thank for their generous support. This work was also supported by Hi! PARIS and ANR/France 2030 program (ANR-23- IACL-0005) and by the French National Research Agency (ANR) through the France 2030 program under the MacLeOD project (ANR-25-PEIA-0005). Finally, it received funding from the Fondation de l’École polytechnique. We are grateful to Rémi Flamary for his review of the manuscript.

[115] h2: Impact Statement

[116] p: This work aims to advance research in machine learning, particularly in the study of multimodal representation alignment. While improved alignment methods may have broad downstream applications, we do not identify any specific societal impacts that require explicit discussion here.

[117] h2: References

[118] h2: Appendix A Experimental Setting

[119] p: We outline the experimental setup in Section 6.3 . Here, we provide further details on our implementation and baselines.

[120] h3: A.1 Implementation Details

[121] p: Following Zhang et al. (2025a) , we create global image representations by concatenating the [CLS] token with the mean of the remaining patch tokens. Text features are computed by averaging all patch tokens. We project both modalities into a shared embedding space of dimensionality d = 1024 d=1024 using linear layers f f and g g . We found them to be more robust in our low-supervision regime compared to non-linear layers.

[122] p: When performing CCA, we add a regularization λ = 0.1 \lambda=0.1 to the eigenvalues of matrices that need to be inverted. Our divergence, KLOT, is computed using the Sinkhorn algorithm with n = 100 n=100 iterations in both spaces. We set the entropic regularization to ϵ = 0.01 \epsilon=0.01 in the reference space and ϵ = 0.05 \epsilon=0.05 in the joint embedding space.

[123] p: Our experiments are conducted with 10k paired samples and, when applicable, up to 1M unpaired images and texts drawn from CC3M ( Sharma et al., 2018 ) . We train all models using a maximum batch size of 32k, composed of up to 10k paired samples and completed with unpaired images and text. If there are less than 32k total samples available in our robustness studies, we adjust the batch size accordingly. We use the LION optimizer ( Chen et al., 2023 ) with a cosine annealing learning-rate schedule, a maximum learning rate of 10 − 4 10^{-4} , and a weight decay of 10 − 5 10^{-5} , and train for 2000 iterations.

[124] p: We mainly employ DINOv3 ViT-L ( Siméoni et al., 2025 ) and NV-Embed-v2 ( Lee et al., 2025 ) as the pretrained vision and language encoders, respectively. In Section 6.2 , we additionally evaluate SOTAlign with DINOv2 ViT-L ( Oquab et al., 2024 ) , Qwen3-Embedding-8B ( Zhang et al., 2025b ) , and Llama-Embed-Nemotron-8B ( Babakhin et al., 2025 ) . All of these language models are among the top performing models in the MMTEB benchmark ( Enevoldsen et al., 2025 ) .

[125] p: Our main evaluation metric is the average of the text-to-image (T2I) and image-to-text (I2T) retrieval (Recall@1) performance on the COCO validation set which we denote MeanR@1. Whenever required, we use a similar score on the CC3M validation split for hyperparameter selection.

[126] p: All experiments can be run on a single A100 GPU with 80 GB memory.

[127] h3: A.2 Baselines

[128] p: In Section Section 6.3 , we compare SOTAlign against several supervised and semi-supervised baselines in zero-shot image classification and retrieval. For each baseline, we consider various configurations as detailed below, and report their optimal performance after hyperparameter tuning.

[129] p: SAIL ( Zhang et al., 2025a ) performs contrastive learning of alignment layers with the SigLIP ( Zhai et al., 2023 ) loss exclusively on paired data. This method represents a series of recent supervised contrastive methods for the alignment of pretrained unimodal vision and language models ( Vouitsis et al., 2024 ; Maniparambil et al., 2025 ; Huang et al., 2025 ) . Following Zhang et al. (2025a) , we initialize the logit scale to 20 20 and the logit bias to − 10 -10 and allow both parameters to be trained. We examine the extension of SAIL to our semi-supervised setting by incorporating unpaired samples as additional negatives in the SigLIP loss.

[130] p: STRUCTURE ( Gröger et al., 2025 ) aligns pretrained encoders in low-resource regimes by augmenting the contrastive objective with an additional loss that forces the similarity distribution in the joint embedding space to lie between the unimodal similarity distributions. While STRUCTURE focuses on a fully supervised setting with paired data, we also evaluate the strength of its regularization term on unpaired data in our semi-supervised setting. We set the number of levels to 1 and the temperature in the softmax function to τ = 0.07 \tau=0.07 . We tune the weight of the structure preservation term over λ ∈ { 0.1 , 1 , 10 , 100 , 1000 } \lambda\in\{0.1,1,10,100,1000\} , and consider both no warmup and a 500-step warmup schedule.

[131] p: Further semi-supervised techniques can be borrowed from contrastive pretraining and low-resource domain adaptation to construct pseudo-pairs based on similarity distributions in the unimodal or joint embedding spaces.

[132] p: NNCLR ( Dwibedi et al., 2021 ) enriches contrastive learning by retrieving the nearest-neighbors of an instance and using them as additional positives. DeCLIP ( Li et al., 2022 ) has adopted such nearest-neighbor supervision in image-language pre-training. We follow this line of work and utilize unpaired images and text as augmentation for the few paired samples. Specifically, for a given image, we find the closest neighbor of its paired caption in the unimodal language space, which then serves as an additional positive for the image. Similarly, for a given text, we find the closest neighbor of its paired image in the unimodal vision space, and can use it as an additional positive for the text. While NNCLR is often implemented with a queue containing the last few batches during training, we can compute the nearest neighbors for all CC3M samples in the unimodal spaces a priori since we utilize pretrained encoders. When training the alignment layers, we then randomly sample a nearest neighbor from the top k ∈ { 1 , 5 , 10 } k\in\{1,5,10\} neighbors, and further perform hyperparameter search for the weights of the contrastive losses with the additional positives: w img , w text ∈ { 0 , 0.1 , 1 , 10 } w_{\text{img}},w_{\text{text}}\in\{0,0.1,1,10\} .

[133] p: S-CLIP ( Mo et al., 2023 ) addresses the domain adaption of CLIP with pseudo-labeling at the caption and keyword level. We evaluate their caption-level supervision in our setting. Given an unpaired image, S-CLIP computes similarity scores to paired images, and then uses the resulting similarity distribution to determine pseudo positives from the paired text. The pseudo-positives can be chosen in a hard assignment as the single nearest neighbor (argmax of the distribution, similar to NNCLR) or in a soft assignment as a weighted average of representations. A key component of S-CLIP is its use of OT to find the optimal matching between unpaired and paired images. The method is limited by the small pool of positives. We apply S-CLIP in the unimodal vision and language spaces as well as in the joint-embedding space. We search for pseudo-labels for both unpaired images as well as unpaired text and tune their corresponding weights in the final objective via a grid search: w img , w text ∈ { 0 , 0.1 , 1 , 10 } w_{\text{img}},w_{\text{text}}\in\{0,0.1,1,10\} .

[134] p: SUE ( Yacobi et al., 2025 ) studies the alignment of unimodal encoders on a single image-text dataset. Their approach combines learnable spectral embeddings on unpaired data, with CCA on paired data for linear alignment, and a residual network to further refine the alignment.

[135] h3: A.3 Datasets

[136] p: We construct our semi-supervised setting primarily using CC3M ( Sharma et al., 2018 ) with both raw web captions and synthetic captions generated by DreamLIP ( Zheng et al., 2024 ) . We further experiment with disjoint images and texts from CC12M ( Changpinyo et al., 2021 ) , COCO ( Lin et al., 2014 ) , ImageNet ( Deng et al., 2009 ) , and WikiText ( Merity et al., 2016 ) . We select models based on their average text-to-image (T2I) and image-to-text (I2T) retrieval performance on the CC3M validation set.

[137] p: In Section 6.3 , we evaluate our model in a zero-shot setting across a diverse suite of classification and retrieval benchmarks.

[138] p: Classification: ImageNet ( Deng et al., 2009 ) , Food-101 ( Bossard et al., 2014 ) , CIFAR-10 ( Krizhevsky, 2009 ) , CIFAR-100 ( Krizhevsky, 2009 ) , Aircraft ( Maji et al., 2013 ) , DTD ( Cimpoi et al., 2014 ) , Flowers ( Nilsback & Zisserman, 2008 )

[139] p: Retrieval (T2I, I2T): COCO ( Lin et al., 2014 ) , Flickr30 ( Plummer et al., 2015 )

[140] h2: Appendix B Additional Experiments

[141] h3: B.1 Sinkhorn Backpropagation

[142] p: The Sinkhorn algorithm has recently been used as a differentiable layer in a wide range of applications, including reinforcement learning ( Emami & Ranka, 2018 ) , learning to rank ( Adams & Zemel, 2011 ) , discriminant analysis ( Flamary et al., 2018 ) , graph matching ( Krzakala et al., 2025 ) , and representation learning ( Van Assel et al., 2023 ) . Closer to our setting, several recent works have applied Sinkhorn-based objectives to contrastive learning for vision–language models ( Mo et al., 2023 ; Shi et al., 2024 ) .

[143] p: While the Sinkhorn algorithm (defined in Appendix C.2 ) is differentiable in theory, computing its gradient in practice is challenging. The most common approach consists in unrolling the Sinkhorn iterations and directly backpropagating through the solver. However, this strategy incurs a large memory overhead, as the full computational graph must be retained for all iterations, causing memory consumption to grow rapidly with the number of Sinkhorn steps.

[144] p: An alternative is to rely on implicit differentiation, which amounts to solving the linear system defined by the optimality conditions of the entropic OT problem. In the case of Sinkhorn, this system exhibits a particular structure that enables more efficient solvers ( Cuturi et al., 2020 ; Eisenberger et al., 2022 ) . While this approach alleviates the memory explosion associated with unrolling, it remains computationally expensive in practice.

[145] p: In the context of our proposed divergence,

[146] table: KLOT ( K ∣ ∣ K ∗ ) = KL ( O T ϵ ∗ ( K ∗ ) | | O T ϵ ( K ) ) , \operatorname{KLOT}(K\mid\mid K^{*})=\operatorname{KL}\!\left(OT_{\epsilon^{*}}(K^{*})\,\middle||\,OT_{\epsilon}(K)\right), (15)

[147] p: a naive application of the chain rule would suggest that computing the gradient

[148] table: ∇ K KLOT ( K ∣ ∣ K ∗ ) \nabla_{K}\operatorname{KLOT}(K\mid\mid K^{*})

[149] p: requires explicitly forming the Jacobian

[150] table: ∂ O ​ T ϵ ​ ( K ) ∂ K , \frac{\partial\,OT_{\epsilon}(K)}{\partial K},

[151] p: thereby necessitating either Sinkhorn unrolling or implicit differentiation.

[152] p: Crucially, Theorem 5.1 shows that this is not required. Instead, the gradient of KLOT \operatorname{KLOT} admits a closed-form expression that can be computed directly, without evaluating the Jacobian of the Sinkhorn operator.

[153] p: To empirically illustrate the efficiency of this result, we extract an n × n n\times n affinity matrix with n = 10 ​ k n=10\text{k} from a checkpoint of SAIL training and compare three strategies for computing ∇ K KLOT ( K ∣ ∣ K ∗ ) \nabla_{K}\operatorname{KLOT}(K\mid\mid K^{*}) : Sinkhorn unrolling, implicit differentiation, and our closed-form gradient. The results are reported in Figure 6 . Our approach significantly outperforms both alternatives in terms of memory usage and runtime. In particular, depending on the value of ϵ \epsilon , which controls the number of Sinkhorn iterations (with convergence scaling as 𝒪 ⁡ ( 1 / ϵ 2 ) \mathcal{O}(1/\epsilon^{2}) ), the proposed method can be up to 100 × 100\times more memory efficient than unrolling and up to 50 × 50\times faster than implicit differentiation.

[154] figure: Figure 6 : Comparison of memory usage, runtime, and number of Sinkhorn iterations for different gradient computation strategies. We run as many Sinkhorn iterations as required to achieve marginal convergence within a tolerance of 10 − 6 10^{-6} .

[155] h3: B.2 Robustness of SOTAlign

[156] p: In Section 6.2 , we analyze the robustness of SOTAlign to variations in both the amount and the source of supervised and unsupervised data. Here, we report the full set of results.

[157] p: Figure 7 shows how zero-shot classification and retrieval performance vary as a function of the number of paired samples used during alignment. Figure 8 illustrates the effect of increasing the number of unpaired samples, in comparison to the supervised SAIL baseline. Table 8 reports zero-shot classification and retrieval results for different combinations of unimodal vision and language encoders, along with absolute gains over supervised SAIL. Finally, Figure 9 relates these performances to the mutual k k -NN similarity between encoder pairs, revealing a strong correlation ( r = 0.83 r=0.83 ), although additional data points will be required to draw firm conclusions.

[158] h3: B.3 Benchmarking Semi-Supervised Alignment

[159] p: Table 9 reports retrieval performance on COCO and Flickr30k, while Table 10 presents zero-shot image classification accuracy across a variety of downstream datasets.

[160] p: In Section 6.3 , we evaluate SOTAlign in a semi-supervised alignment setting proposed by Yacobi et al. (2025) . We train for alignment on a single dataset, and evaluate retrieval on the test split of the same dataset (with only 400 test instances for retrieval). The datasets are: COCO ( Lin et al., 2014 ) , Flickr30k ( Plummer et al., 2015 ) , and Polyvore ( Han et al., 2017 ) . Yacobi et al. (2025) use MLPs for alignment and an embedding dimensionality of 8. In Table 11 , we report the performance of SOTAlign adhering to their architectural choices. Our method achieves gains of +5.5 on COCO, +28.7 on Flickr30k, and +18.2 on Polyvore I2T R@5. However, if we lift these constraints and instead use linear alignment layers with a target dimension of 512, performance increases further, reaching +14.3 on COCO, +40.0 on Flickr30k, and +32.5 on Polyvore.

[161] h3: B.4 Quantifying the distribution shift

[162] p: We study the effect of the distribution shift arising from the use of unpaired data ( X , Y ) (X,Y) drawn from different sources from those of the paired data ( A , B ) (A,B) using the total spherical sliced Wasserstein distance (see Appendix C.2 ) computed using the Python library POT ( Flamary et al., 2021 ; Flamary et al., 2024 ) . In all experiments, we set p = 2 p=2 and use N = 500 N=500 projection directions. Distances between unimodal datasets are reported in Figure 12 averaged over 20 20 random seeds corresponding to a different subset of 100 000 100\,000 samples of the dataset and projection set. All distances are computed between embeddings from Dinov3 and NV-Embed-V2 for images and text respectively.

[163] p: In Figure 5 we exhibit a strong correlation between distance and performance, which provides a good proxy for performance that can be computed without any training or inference. In addition, this correlation is even stronger when one of the unimodal unpaired dataset is fixed to be CC3M and the other is varied. We show that performance is strongly correlated with the SSW distances between the unimodal datasets, S ​ S ​ W ​ ( B , Y ) SSW(B,Y) and S ​ S ​ W ​ ( A , X ) SSW(A,X) in Figure 10 and 11 respectively.

[164] figure: (a) ImageNet classification (b) COCO T2I retrieval (c) COCO I2T retrieval Figure 7 : Effect of the number of paired samples during alignment on downstream zero-shot classification and retrieval. We fix 1M unpaired samples from CC3M and vary the number of paired samples.

[165] figure: (a) ImageNet classification (b) COCO T2I (c) COCO I2T Figure 8 : Effect of the number of unpaired samples during alignment on downstream zero-shot classification and retrieval. We fix 10k paired samples from CC3M and vary the number of unpaired samples.

[166] figure: Table 7 : We train SOTAlign on 10k image-text pairs from CC3M and up to 1M samples from varying unimodal datasets and report the zero-shot classification (top-1 accuracy) and retrieval (R@1). For comparison we report SAIL trained with as many samples and SAIL 1M i.e. the version trained using 1M supervised samples from CC3M (100x more supervision). Method Unpaired Images Unpaired Text ImageNet-1K COCO T2I COCO I2T SAIL 1M — — 56.4 35.5 45.5 SAIL — — 35.6 21.0 27.4 SOTAlign CC3M CC3M 46.1 26.5 34.1 SOTAlign CC3M CC3M synth. 46.2 30.4 39.7 SOTAlign CC3M CC12M 44.6 24.5 32.0 SOTAlign CC12M CC3M 43.8 24.9 32.8 SOTAlign CC12M CC12M 46.8 25.7 34.4 SOTAlign ImageNet CC3M 43.4 23.8 31.5 SOTAlign ImageNet CC12M 44.3 24.2 31.5 SOTAlign CC3M COCO 38.4 28.4 26.7 SOTAlign CC12M COCO 38.3 27.7 30.6 SOTAlign ImageNet COCO 40.6 25.5 26.1 SOTAlign COCO CC3M 38.0 21.7 33.9 SOTAlign COCO CC12M 38.5 22.0 33.1 SOTAlign CC3M WikiText103 39.8 21.4 27.8 SOTAlign COCO WikiText103 37.1 19.5 29.4 SOTAlign ImageNet WikiText103 40.7 20.7 28.1

[167] figure: Table 8 : SOTAlign trained on 10k pairs and 1M unpaired samples from CC3M with different unimodal encoders. Zero-shot classification (top-1 accuracy) and retrieval (R@1). Green values represent the absolute gain over supervised SAIL. Vision Language Mutual k-NN Method ImageNet COCO COCO Model Model 1K T2I I2T DINOv2 Nemotron-8B 14.6 SAIL 25.5 11.7 18.0 SOTAlign 32.4 +6.9 15.5 +3.8 23.3 +5.3 Qwen3-8B 18.9 SAIL 31.8 16.8 23.8 SOTAlign 39.5 +7.7 20.9 +4.1 31.1 +7.3 NV-Embed-v2 18.2 SAIL 32.7 19.0 23.4 SOTAlign 42.5 +9.8 23.1 +4.1 31.1 +7.7 DINOv3 Nemotron-8B 14.1 SAIL 25.4 12.8 21.0 SOTAlign 35.5 +10.1 16.6 +3.8 26.2 +5.2 Qwen3-8B 18.0 SAIL 33.4 19.1 28.0 SOTAlign 42.7 +9.3 24.1 +5.0 35.3 +7.3 NV-Embed-v2 17.6 SAIL 35.6 21.0 27.4 SOTAlign 46.1 +10.5 26.5 +5.5 34.1 +6.7

[168] figure: Table 9 : Zero-shot text-image retrieval (Recall@K) on COCO and Flickr30k. Comparison of supervised and semi-supervised methods trained with 10k image-text pairs and 1M unpaired samples from CC3M. Upper bound with 1M supervised pairs in grey. COCO Flickr30k Method T2I I2T T2I I2T R@1 R@5 R@1 R@5 R@1 R@5 R@1 R@5 Sup. SAIL (1M) 35.5 61.0 45.5 72.0 63.1 87.2 75.0 94.4 SAIL 21.0 44.3 27.4 51.7 45.7 75.1 54.1 81.2 STRUCTURE 21.0 43.7 28.7 52.7 46.8 74.9 54.0 82.9 Semi-sup. SAIL 20.7 43.6 26.5 51.7 44.9 74.2 53.1 82.1 STRUCTURE 20.9 43.5 28.0 52.2 45.7 74.9 56.0 83.3 NNCLR 21.3 44.4 27.9 52.2 46.6 75.3 52.9 82.1 S-CLIP 20.4 42.6 27.8 50.5 44.5 74.4 52.6 82.3 SOTAlign (Ours) 26.5 49.8 34.1 59.4 51.7 79.2 60.8 85.7

[169] figure: Figure 9 : (R@1COCO) vs mutual k-NN.

[170] figure: Table 10 : Zero-shot image classification (top-1 accuracy). Comparison of supervised and semi-supervised methods trained with 10k image-text pairs and 1M unpaired samples from CC3M. Upper bound with 1M supervised pairs in grey.. Method Food-101 CIFAR-10 CIFAR-100 Aircraft DTD Flowers ImageNet Sup. SAIL (1M) 63.9 97.8 82.3 9.7 53.5 47.2 56.4 SAIL 36.4 96.2 71.2 3.9 36.8 24.1 35.6 STRUCTURE 38.5 96.7 72.2 5.4 39.5 23.6 38.2 Semi-sup. SAIL 36.5 96.2 71.3 3.8 35.9 21.1 35.6 STRUCTURE 37.6 96.5 70.8 4.9 38.7 23.2 36.8 NNCLR 37.9 96.5 73.0 3.8 38.8 24.6 37.4 S-CLIP 35.3 95.9 69.3 4.4 37.6 22.5 36.4 SOTAlign (Ours) 50.0 97.5 78.3 5.0 42.4 30.1 46.1

[171] figure: Table 11 : Alignment per dataset. Following the setup of SUE ( Yacobi et al., 2025 ) , we train for alignment per dataset and evaluate image-text retrieval (Recall@5). We report SOTAlign results adhering to the architectural choices of SUE (MLP, embedding dimensionality of 8) and without these constraints. COCO Flickr30k Polyvore 100 Pairs 500 Pairs 500 Pairs Method I2T T2I I2T T2I I2T T2I CSA 1.3 1.0 1.3 0.8 1.3 1.0 Contrastive 8.5 5.8 9.5 9.8 13.8 11.5 SUE 21.5 18.3 19.8 22.0 22.8 20.8 SOTAlign (with SUE constraints) 27.0 28.8 48.5 48.8 41.0 39.8 SOTAlign (without SUE constraints) 35.8 35.0 59.8 63.3 55.3 55.3

[172] figure: Figure 10 : Performance when using CC3M as paired data, CC3M text as unpaired text, and other image datasets as unpaired images, together with a comparison to the spherical sliced Wasserstein distance between CC3M image and the other image datasets.

[173] figure: Figure 11 : Performance when using CC3M as paired data, CC3M text as unpaired text, and other image datasets as unpaired images, together with a comparison to the spherical sliced Wasserstein distance between CC3M image and the other image datasets.

[174] figure: Figure 12 : Spherical sliced Wasserstein distances between different image datasets (left) and text datasets (right). We report mean and std of the distances over 20 20 seeds.

[175] h2: Appendix C Mathematical Details

[176] h3: C.1 Linear Alignment Models

[177] p: We now provide the closed-form solutions for the proposed linear alignment models.

[178] h4: Procrustes.

[179] p: The classical Orthogonal Procrustes problem is defined for two point clouds A , B ∈ ℝ n × d A,B\in\mathbb{R}^{n\times d} and seeks an orthogonal transformation that best aligns A A to B B . It can be written as

[180] table: max P ∈ ℝ d × d ⁡ ⟨ P ​ A ⊤ , B ⟩ s.t. ​ P ​ P ⊤ = I d . \displaystyle\max_{P\in\mathbb{R}^{d\times d}}\;\langle PA^{\top},B\rangle\quad\text{s.t. }PP^{\top}=I_{d}. (16)

[181] p: This formulation learns a single linear mapping from A A to B B and implicitly assumes that both point clouds lie in the same ambient space ℝ d \mathbb{R}^{d} .

[182] p: However, Procrustes alignment is known to admit flexible generalizations beyond this setting ( Gower & Dijksterhuis, 2004 ) . In particular, it can be extended to handle representations of different dimensionalities and to learn projections into a shared lower-dimensional space. We now introduce a natural variant of Procrustes alignment that is better suited to our setting.

[183] h6: Proposition C.1 (Closed form solution of Procrustes Alignment) .

[184] p: Let A ∈ ℝ n × d a A\in\mathbb{R}^{n\times d_{a}} and B ∈ ℝ n × d b B\in\mathbb{R}^{n\times d_{b}} , and let d ′ ≤ min ⁡ { d a , d b } d^{\prime}\leq\min\{d_{a},d_{b}\} . Consider the optimization problem

[185] table: max P ∈ ℝ d ′ × d a , Q ∈ ℝ d ′ × d b ⁡ ⟨ P ​ A ⊤ , B ​ Q ⊤ ⟩ s.t. ​ P ​ P ⊤ = I d ′ , Q ​ Q ⊤ = I d ′ . \displaystyle\max_{P\in\mathbb{R}^{d^{\prime}\times d_{a}},\,Q\in\mathbb{R}^{d^{\prime}\times d_{b}}}\;\langle PA^{\top},BQ^{\top}\rangle\quad\text{s.t. }PP^{\top}=I_{d^{\prime}},\;QQ^{\top}=I_{d^{\prime}}. (17)

[186] p: Let the singular value decomposition of A ⊤ ​ B A^{\top}B be

[187] table: A ⊤ ​ B = U ​ Σ ​ V ⊤ , A^{\top}B=U\Sigma V^{\top},

[188] p: with singular values in non-increasing order. Then an optimal solution is given by

[189] table: W x = U : , 1 : d ′ , W y = V : , 1 : d ′ . W_{x}=U_{:,1:d^{\prime}},\qquad W_{y}=V_{:,1:d^{\prime}}.

[190] h6: Proof.

[191] p: We introduce the change of variables

[192] table: P ~ = P ​ U , Q ~ = Q ​ V . \tilde{P}=PU,\qquad\tilde{Q}=QV.

[193] p: Since U U and V V are orthogonal, P ~ \tilde{P} and Q ~ \tilde{Q} also satisfy P ~ ​ P ~ ⊤ = Q ~ ​ Q ~ ⊤ = I d ′ \tilde{P}\tilde{P}^{\top}=\tilde{Q}\tilde{Q}^{\top}=I_{d^{\prime}} . Using invariance of the Frobenius inner product under orthogonal transformations, the objective rewrites as

[194] table: ⟨ P ​ A ⊤ , B ​ Q ⊤ ⟩ = ⟨ P ~ ​ Σ , Q ~ ⟩ . \langle PA^{\top},BQ^{\top}\rangle=\langle\tilde{P}\Sigma,\tilde{Q}\rangle.

[195] p: By the Cauchy–Schwarz inequality,

[196] table: ⟨ P ~ ​ Σ , Q ~ ⟩ ≤ ‖ P ~ ​ Σ ‖ F ​ ‖ Q ~ ‖ F . \langle\tilde{P}\Sigma,\tilde{Q}\rangle\leq\|\tilde{P}\Sigma\|_{F}\,\|\tilde{Q}\|_{F}.

[197] p: Since Q ~ ∈ ℝ d ′ × d b \tilde{Q}\in\mathbb{R}^{d^{\prime}\times d_{b}} has orthonormal rows, we have

[198] table: ‖ Q ~ ‖ F 2 = tr ⁡ ( Q ~ ​ Q ~ ⊤ ) = d ′ . \|\tilde{Q}\|_{F}^{2}=\mathrm{tr}(\tilde{Q}\tilde{Q}^{\top})=d^{\prime}.

[199] p: We now bound ‖ P ~ ​ Σ ‖ F 2 \|\tilde{P}\Sigma\|_{F}^{2} . By definition,

[200] table: ‖ P ~ ​ Σ ‖ F 2 = tr ⁡ ( P ~ ​ Σ 2 ​ P ~ ⊤ ) = tr ⁡ ( Σ 2 ​ P ~ ⊤ ​ P ~ ) , \|\tilde{P}\Sigma\|_{F}^{2}=\mathrm{tr}(\tilde{P}\Sigma^{2}\tilde{P}^{\top})=\mathrm{tr}(\Sigma^{2}\tilde{P}^{\top}\tilde{P}),

[201] p: where we used cyclic invariance of the trace. Since P ~ \tilde{P} has orthonormal rows, the matrix

[202] table: Π = P ~ ⊤ ​ P ~ \Pi=\tilde{P}^{\top}\tilde{P}

[203] p: is an orthogonal projector of rank d ′ d^{\prime} , with eigenvalues in { 0 , 1 } \{0,1\} and tr ⁡ ( Π ) = d ′ \mathrm{tr}(\Pi)=d^{\prime} .

[204] p: Let Σ 2 = diag ⁡ ( σ 1 2 , … , σ r 2 ) \Sigma^{2}=\mathrm{diag}(\sigma_{1}^{2},\dots,\sigma_{r}^{2}) with σ 1 ≥ σ 2 ≥ ⋯ ≥ σ r ≥ 0 \sigma_{1}\geq\sigma_{2}\geq\cdots\geq\sigma_{r}\geq 0 . Then

[205] table: tr ⁡ ( Σ 2 ​ Π ) = ∑ i = 1 r σ i 2 ​ Π i ​ i . \mathrm{tr}(\Sigma^{2}\Pi)=\sum_{i=1}^{r}\sigma_{i}^{2}\,\Pi_{ii}.

[206] p: Because 0 ≤ Π i ​ i ≤ 1 0\leq\Pi_{ii}\leq 1 for all i i and ∑ i Π i ​ i = d ′ \sum_{i}\Pi_{ii}=d^{\prime} , the sum is maximized by assigning weight 1 1 to the d ′ d^{\prime} largest diagonal entries of Σ 2 \Sigma^{2} . Therefore,

[207] table: tr ⁡ ( Σ 2 ​ Π ) ≤ ∑ i = 1 d ′ σ i 2 . \mathrm{tr}(\Sigma^{2}\Pi)\leq\sum_{i=1}^{d^{\prime}}\sigma_{i}^{2}.

[208] p: Combining the above bounds yields

[209] table: ⟨ P ~ ​ Σ , Q ~ ⟩ ≤ d ′ ​ ( ∑ i = 1 d ′ σ i 2 ) 1 / 2 , \langle\tilde{P}\Sigma,\tilde{Q}\rangle\leq\sqrt{d^{\prime}}\left(\sum_{i=1}^{d^{\prime}}\sigma_{i}^{2}\right)^{1/2},

[210] p: and the bound is tight when P ~ = Q ~ = I d ′ \tilde{P}=\tilde{Q}=I_{d^{\prime}} which concludes the proof. ∎

[211] h4: Canonical Correlation Analysis (CCA).

[212] p: Canonical Correlation Analysis (CCA) is a classical tool for studying linear relationships between two sets of variables and is widely used in multivariate statistics and representation learning. In this work, CCA is already defined in ( 7 ); we briefly recall its formulation here in a form that is convenient for deriving its closed-form solution and for highlighting its connection to Procrustes alignment.

[213] p: Denoting

[214] table: Σ x , x = A ⊤ ​ A , Σ x , y = A ⊤ ​ B , Σ y , y = B ⊤ ​ B , \Sigma_{x,x}=A^{\top}A,\qquad\Sigma_{x,y}=A^{\top}B,\qquad\Sigma_{y,y}=B^{\top}B,

[215] p: the CCA problem ( 7 ) can be equivalently rewritten as

[216] table: ( W x , W y ) \displaystyle(W_{x},W_{y}) = arg ⁡ max P , Q ​ ⟨ P ​ Σ x , y , Q ⟩ \displaystyle=\arg\max_{P,Q}\;\langle P\Sigma_{x,y},Q\rangle (18) s.t. P ​ Σ x , x ​ P ⊤ = I d ′ , Q ​ Σ y , y ​ Q ⊤ = I d ′ . \displaystyle\text{s.t.}\quad P\Sigma_{x,x}P^{\top}=I_{d^{\prime}},\qquad Q\Sigma_{y,y}Q^{\top}=I_{d^{\prime}}.

[217] p: We now present a standard derivation of the closed-form solution, included for completeness, which makes explicit the relationship between CCA and the Procrustes problem introduced above.

[218] h6: Proposition C.2 (Closed-form solution of CCA) .

[219] p: Let

[220] table: Σ x , x − 1 / 2 Σ x , y Σ y , y − 1 / 2 = U Σ V ⊤ \Sigma_{x,x}^{-1/2}\Sigma_{x,y}\Sigma_{y,y}^{-1/2}=U\Sigma V^{\top}

[221] p: be the singular value decomposition, with singular values in non-increasing order. Then an optimal solution to ( 18 ) is given by

[222] table: W x = U : , 1 : d ′ ⊤ Σ x , x − 1 / 2 , W y = V : , 1 : d ′ ⊤ Σ y , y − 1 / 2 . W_{x}=U_{:,1:d^{\prime}}^{\top}\Sigma_{x,x}^{-1/2},\qquad W_{y}=V_{:,1:d^{\prime}}^{\top}\Sigma_{y,y}^{-1/2}.

[223] h6: Proof.

[224] p: We introduce the change of variables

[225] table: P ~ = P ​ Σ x , x 1 / 2 , Q ~ = Q ​ Σ y , y 1 / 2 . \tilde{P}=P\Sigma_{x,x}^{1/2},\qquad\tilde{Q}=Q\Sigma_{y,y}^{1/2}.

[226] p: Under this transformation, the constraints become

[227] table: P ~ ​ P ~ ⊤ = I d ′ , Q ~ ​ Q ~ ⊤ = I d ′ , \tilde{P}\tilde{P}^{\top}=I_{d^{\prime}},\qquad\tilde{Q}\tilde{Q}^{\top}=I_{d^{\prime}},

[228] p: and the objective rewrites as

[229] table: ⟨ P ​ Σ x , y , Q ⟩ \displaystyle\langle P\Sigma_{x,y},Q\rangle = ⟨ P ~ Σ x , x − 1 / 2 Σ x , y Σ y , y − 1 / 2 , Q ~ ⟩ . \displaystyle=\left\langle\tilde{P}\,\Sigma_{x,x}^{-1/2}\Sigma_{x,y}\Sigma_{y,y}^{-1/2},\tilde{Q}\right\rangle.

[230] p: Thus, the CCA problem reduces to an orthogonal Procrustes problem:

[231] table: max P ~ ​ P ~ ⊤ = Q ~ ​ Q ~ ⊤ = I d ′ ⟨ P ~ M , Q ~ ⟩ , where M = Σ x , x − 1 / 2 Σ x , y Σ y , y − 1 / 2 . \max_{\tilde{P}\tilde{P}^{\top}=\tilde{Q}\tilde{Q}^{\top}=I_{d^{\prime}}}\left\langle\tilde{P}M,\tilde{Q}\right\rangle,\quad\text{where }M=\Sigma_{x,x}^{-1/2}\Sigma_{x,y}\Sigma_{y,y}^{-1/2}.

[232] p: Let M = U ​ Σ ​ V ⊤ M=U\Sigma V^{\top} be its singular value decomposition. By the Procrustes result, the maximum is attained for

[233] table: P ~ = U : , 1 : d ′ ⊤ , Q ~ = V : , 1 : d ′ ⊤ . \tilde{P}=U_{:,1:d^{\prime}}^{\top},\qquad\tilde{Q}=V_{:,1:d^{\prime}}^{\top}.

[234] p: Substituting back yields

[235] table: P = U : , 1 : d ′ ⊤ Σ x , x − 1 / 2 , Q = V : , 1 : d ′ ⊤ Σ y , y − 1 / 2 , P=U_{:,1:d^{\prime}}^{\top}\Sigma_{x,x}^{-1/2},\qquad Q=V_{:,1:d^{\prime}}^{\top}\Sigma_{y,y}^{-1/2},

[236] p: which concludes the proof. ∎

[237] h3: C.2 Optimal Transport

[238] h4: Introduction to Optimal Transport

[239] p: We briefly recall the discrete optimal transport (OT) problem and its entropic relaxation. We refer to ( Peyré et al., 2019 ) for more details. Let n ∈ ℕ n\in\mathbb{N} and denote by 𝒫 n \mathcal{P}_{n} the set of permutation matrices,

[240] table: 𝒫 n = { P ∈ { 0 , 1 } n × n ∣ P 𝟏 = 𝟏 , P ⊤ 𝟏 = 𝟏 } , \mathcal{P}_{n}=\{P\in\{0,1\}^{n\times n}\mid P\mathbf{1}=\mathbf{1},\;P^{\top}\mathbf{1}=\mathbf{1}\},

[241] p: and by Π n \Pi_{n} the set of bistochastic matrices,

[242] table: Π n = { T ∈ ℝ + n × n ∣ T 𝟏 = 𝟏 , T ⊤ 𝟏 = 𝟏 } . \Pi_{n}=\{T\in\mathbb{R}_{+}^{n\times n}\mid T\mathbf{1}=\mathbf{1},\;T^{\top}\mathbf{1}=\mathbf{1}\}.

[243] p: We further define the (negative) entropy of a transport plan T ∈ Π n T\in\Pi_{n} as

[244] table: H ⁡ ( T ) = ∑ i , j T i ​ j ​ log ⁡ T i ​ j . H(T)=\sum_{i,j}T_{ij}\log T_{ij}.

[245] p: In the discrete OT setting, we are given two sets of points indexed by i , j ∈ { 1 , … , n } i,j\in\{1,\dots,n\} and a cost matrix C ∈ ℝ n × n C\in\mathbb{R}^{n\times n} , where C i ​ j C_{ij} denotes the cost of transporting mass from point i i to point j j . The classical Monge formulation seeks the permutatin minimizing the total transport cost,

[246] table: min P ∈ 𝒫 n ⁡ ⟨ P , C ⟩ . \min_{P\in\mathcal{P}_{n}}\langle P,C\rangle. (Monge)

[247] p: This formulation enforces a one-to-one matching and is combinatorial in nature.

[248] p: Kantorovich proposed a convex relaxation of this problem by allowing fractional transport plans,

[249] table: min T ∈ Π n ⁡ ⟨ T , C ⟩ , \min_{T\in\Pi_{n}}\langle T,C\rangle, (Kantorovich)

[250] p: which can be shown to be equivalent to the Monge formulation in the discrete balanced setting ( Peyré et al., 2019 ) , while being more flexible and amenable to generalizations such as non-uniform marginals and continuous measures.

[251] p: When the cost matrix is defined as C i , j = d ​ ( x i , y j ) p C_{i,j}=d(x_{i},y_{j})^{p} , where d d is a distance on the underlying space and p ≥ 1 p\geq 1 , the optimal value of the Kantorovich problem induces the p-Wasserstein distance, defined as

[252] table: W p = ( min T ∈ Π n ⁡ ⟨ T , C ⟩ ) 1 / p . W_{p}=\left(\min_{T\in\Pi_{n}}\langle T,C\rangle\right)^{1/p}. (Wasserstein distance)

[253] p: To further improve computational tractability, Cuturi (2013) introduced the entropic regularized OT problem, also known as the Sinkhorn relaxation,

[254] table: min T ∈ Π n ⁡ ⟨ T , C ⟩ + ε ​ H ​ ( T ) , \min_{T\in\Pi_{n}}\;\langle T,C\rangle+\varepsilon H(T), (19)

[255] p: where ε > 0 \varepsilon>0 controls the strength of the regularization. This formulation yields a strictly convex objective and can be efficiently solved using the Sinkhorn algorithm.

[256] h4: Sliced Wasserstein distance

[257] p: Although entropically regularized optimal transport can be efficiently solved using the Sinkhorn algorithm, its computational complexity remains O ⁡ ( n 2 ) O(n^{2}) , which becomes prohibitive when comparing distributions supported on millions of high-dimensional points. To address this limitation, the sliced Wasserstein distance (SW) was introduced ( Bonneel et al., 2015 ) . The key observation underlying this approach is that the Wasserstein distance between one-dimensional distributions admits a closed-form solution obtained by sorting the samples and matching them monotonically. The sliced Wasserstein distance exploits this property by projecting high-dimensional distributions onto multiple one-dimensional subspaces and averaging the resulting one-dimensional Wasserstein distances.

[258] p: Let μ = ∑ i = 1 n a i ​ δ x i \mu=\sum_{i=1}^{n}a_{i}\delta_{x_{i}} and ν = ∑ j = 1 m b i ​ δ y j \nu=\sum_{j=1}^{m}b_{i}\delta_{y_{j}} be two discrete probability measures with x i , y j ∈ ℝ d x_{i},y_{j}\in\mathbb{R}^{d} . For a given projection θ ∈ 𝕊 d − 1 \theta\in\mathbb{S}^{d-1} , we define the projected one dimensional distributions as

[259] table: μ θ = ∑ i = 1 n a i ​ δ ⟨ x i , θ ⟩ , ν θ = ∑ j = 1 m b j ​ δ ⟨ y j , θ ⟩ . \mu^{\theta}=\sum_{i=1}^{n}a_{i}\delta_{\left\langle x_{i},\theta\right\rangle},\quad\nu^{\theta}=\sum_{j=1}^{m}b_{j}\delta_{\left\langle y_{j},\theta\right\rangle}. (20)

[260] p: Given a set of projection directions ( θ 1 , … , θ N ) (\theta_{1},...,\theta_{N}) , the p-SW distance is defined as

[261] table: S ​ W p ​ ( μ , ν ) = ( 1 N ​ ∑ i = 1 N W p p ​ ( μ θ i , ν θ i ) ) 1 / p . SW_{p}(\mu,\nu)=\left(\frac{1}{N}\sum_{i=1}^{N}W_{p}^{p}(\mu^{\theta_{i}},\nu^{\theta_{i}})\right)^{1/p}. (21)

[262] p: When data are constrained to the unit sphere, the spherical sliced Wasserstein (SSW) distance ( Liu et al., 2024 ) replaces linear projections with angular projections and computes optimal transport on the circle, thereby respecting the intrinsic geometry of directional data.

[263] h4: Total sliced Wasserstein distance

[264] p: We introduce the total spherical sliced Wasserstein distance d as a measure of the distribution shift between a source of unpaired data 𝒟 = ( X , Y ) \mathcal{D}=(X,Y) and the paired dataset 𝒟 p = ( A , B ) \mathcal{D}_{p}=(A,B) . Using the spherical sliced Wasserstein distance in place of the standard sliced Wasserstein distance ensures that the resulting distances between text distributions and between image distributions are computed on a comparable scale, enabling fair comparison across modalities. The total SSW distance is defined as

[265] table: d ​ ( 𝒟 , 𝒟 p ) = SSW ​ ( X , A ) + SSW ​ ( Y , B ) . \text{d}(\mathcal{D},\mathcal{D}_{p})=\text{SSW}(X,A)+\text{SSW}(Y,B). (22)

[266] h4: Theoretical Results.

[267] p: We now present the theoretical contribution underlying our proposed divergence and its efficient differentiation. Throughout, we work with an affinity matrix K ∈ ℝ n × n K\in\mathbb{R}^{n\times n} rather than a cost matrix, following the convention C = − K C=-K for consistency with the rest of the paper.

[268] p: For any transport plan T ∈ Π n T\in\Pi_{n} , we define the entropic OT objective

[269] table: W ϵ ​ ( T , K ) = − ⟨ T , K ⟩ + ϵ ​ H ​ ( T ) , W_{\epsilon}(T,K)=-\langle T,K\rangle+\epsilon H(T), (23)

[270] p: and the associated optimal value

[271] table: W ϵ ​ ( K ) = min T ∈ Π n ⁡ W ϵ ​ ( T , K ) . W_{\epsilon}(K)=\min_{T\in\Pi_{n}}W_{\epsilon}(T,K). (24)

[272] p: Finally, we denote

[273] table: OT ϵ ​ ( K ) = arg ​ min T ∈ Π n ⁡ W ϵ ​ ( T , K ) \mathrm{OT}_{\epsilon}(K)=\argmin_{T\in\Pi_{n}}W_{\epsilon}(T,K) (25)

[274] p: the corresponding optimal transport plan.

[275] p: Importantly, we recall the following fundamental result in entropic optimal transport states that there exist dual potentials u , v ∈ ℝ n u,v\in\mathbb{R}^{n} such that the optimal transport plan admits the decomposition

[276] table: log ⁡ OT ϵ ​ ( K ) = u ​ 𝟏 ⊤ + K ϵ + 𝟏 ​ v ⊤ , \log{\text{OT}_{\epsilon}(K)}=u\mathbf{1}^{\top}+\frac{K}{\epsilon}+\mathbf{1}v^{\top}, (26)

[277] p: see e.g. Peyré et al. (2019) . This characterization allows us to establish the following lemma.

[278] h6: Lemma C.3 .

[279] p: For any transport plan T ∈ Π n T\in\Pi_{n} ,

[280] table: ⟨ T , log ⁡ OT ϵ ​ ( K ) ⟩ = ⟨ T , K ⟩ + W ϵ ​ ( K ) ϵ . \langle T,\log{\text{OT}_{\epsilon}(K)}\rangle=\frac{\langle T,K\rangle+W_{\epsilon}(K)}{\epsilon}. (27)

[281] h6: Proof.

[282] p: For any T ∈ Π n T\in\Pi_{n} , we have

[283] table: ⟨ T , log ⁡ OT ϵ ​ ( K ) ⟩ = ⟨ T , u ​ 𝟏 ⊤ ⟩ + ⟨ T , 𝟏 ​ v ⊤ ⟩ + 1 ϵ ​ ⟨ T , K ⟩ . \langle T,\log{\text{OT}_{\epsilon}(K)}\rangle=\langle T,u\mathbf{1}^{\top}\rangle+\langle T,\mathbf{1}v^{\top}\rangle+\frac{1}{\epsilon}\langle T,K\rangle.

[284] p: Since T T is bistochastic, ⟨ T , u ​ 𝟏 ⊤ ⟩ = ⟨ 𝟏 , u ⟩ \langle T,u\mathbf{1}^{\top}\rangle=\langle\mathbf{1},u\rangle and ⟨ T , 𝟏 ​ v ⊤ ⟩ = ⟨ 𝟏 , v ⟩ \langle T,\mathbf{1}v^{\top}\rangle=\langle\mathbf{1},v\rangle , yielding

[285] table: ⟨ T , log ⁡ OT ϵ ​ ( K ) ⟩ = ⟨ 𝟏 , u + v ⟩ + 1 ϵ ​ ⟨ T , K ⟩ . \langle T,\log{\text{OT}_{\epsilon}(K)}\rangle=\langle\mathbf{1},u+v\rangle+\frac{1}{\epsilon}\langle T,K\rangle.

[286] p: In particular, setting T = OT ϵ ​ ( K ) T=\mathrm{OT}_{\epsilon}(K) yields

[287] table: H ⁡ ( OT ϵ ​ ( K ) ) = ⟨ 𝟏 , u + v ⟩ + 1 ϵ ​ ⟨ OT ϵ ​ ( K ) , K ⟩ . H(\mathrm{OT}_{\epsilon}(K))=\langle\mathbf{1},u+v\rangle+\frac{1}{\epsilon}\langle\mathrm{OT}_{\epsilon}(K),K\rangle.

[288] p: which recovers a classical duality result

[289] table: ⟨ 𝟏 , u + v ⟩ = W ϵ ​ ( K ) ϵ . \langle\mathbf{1},u+v\rangle=\frac{W_{\epsilon}(K)}{\epsilon}.

[290] p: which gives the result. ∎

[291] p: Our main theoretical result follows by combining Lemma 27 with the envelope theorem, yielding an explicit expression for the gradient of the proposed divergence.

[292] h6: Theorem C.4 .

[293] p: For any transport plan T ∈ Π n T\in\Pi_{n} ,

[294] table: ∇ K KL ( T ∥ OT ϵ ( K ) ) = OT ϵ ​ ( K ) − T ϵ . \nabla_{K}\,\mathrm{KL}\!\left(T\,\|\,\mathrm{OT}_{\epsilon}(K)\right)=\frac{\mathrm{OT}_{\epsilon}(K)-T}{\epsilon}. (28)

[295] h6: Proof.

[296] p: By definition,

[297] table: KL ( T ∥ OT ϵ ( K ) ) \displaystyle\mathrm{KL}\!\left(T\,\|\,\mathrm{OT}_{\epsilon}(K)\right) = ⟨ T , log ⁡ T OT ϵ ​ ( K ) ⟩ \displaystyle=\left\langle T,\log\frac{T}{\mathrm{OT}_{\epsilon}(K)}\right\rangle = ⟨ T , log ⁡ T ⟩ − ⟨ T , log ⁡ OT ϵ ​ ( K ) ⟩ \displaystyle=\left\langle T,\log T\right\rangle-\left\langle T,\log\mathrm{OT}_{\epsilon}(K)\right\rangle

[298] p: and only the second term depends on K K . Differentiating yields

[299] table: ∇ K KL ( T ∥ OT ϵ ( K ) ) = − ∇ K ⟨ T , log OT ϵ ( K ) ⟩ . \nabla_{K}\,\mathrm{KL}\!\left(T\,\|\,\mathrm{OT}_{\epsilon}(K)\right)=-\nabla_{K}\langle T,\log{\text{OT}_{\epsilon}(K)}\rangle.

[300] p: Applying Lemma 27 gives

[301] table: ∇ K KL ( T ∥ OT ϵ ( K ) ) = − 1 ϵ ∇ K ( ⟨ T , K ⟩ + W ϵ ( K ) ) . \nabla_{K}\,\mathrm{KL}\!\left(T\,\|\,\mathrm{OT}_{\epsilon}(K)\right)=-\frac{1}{\epsilon}\nabla_{K}\big(\langle T,K\rangle+W_{\epsilon}(K)\big).

[302] p: Since W ϵ ​ ( K ) W_{\epsilon}(K) is defined as the minimum of W ϵ ​ ( T , K ) W_{\epsilon}(T,K) over T ∈ Π n T\in\Pi_{n} which is a strongly convex problem, the envelope theorem implies

[303] table: ∇ K W ϵ ​ ( K ) = ∇ K W ϵ ​ ( OT ϵ ​ ( K ) , K ) = − OT ϵ ​ ( K ) \nabla_{K}W_{\epsilon}(K)=\nabla_{K}W_{\epsilon}(\mathrm{OT}_{\epsilon}(K),K)=-\mathrm{OT}_{\epsilon}(K)

[304] p: from which the result follows. We note that a related derivation is presented in this blog post ( Assel, 2024 ) , which draws an insightful connection to the Monge Gap regularizer introduced in ( Uscidda & Cuturi, 2023 ) . ∎

[305] h3: C.3 Centered Kernel Alignment (CKA)

[306] p: Centered Kernel Alignment (CKA) ( Cristianini et al., 2001 ) is a widely used measure of similarity between representation spaces, defined in terms of their associated kernel (or Gram) matrices. Let H = I n − 1 n ​ 𝟏𝟏 ⊤ H=I_{n}-\frac{1}{n}\mathbf{1}\mathbf{1}^{\top} denote the centering matrix and ∥ ⋅ ∥ F \|\cdot\|_{F} the Frobenius norm. Given two kernel matrices K 1 , K 2 ∈ ℝ n × n K_{1},K_{2}\in\mathbb{R}^{n\times n} , CKA is defined as

[307] table: CKA ⁡ ( K 1 , K 2 ) = ⟨ K 1 ​ H , H ​ K 2 ⟩ ⟨ K 1 ​ H , H ​ K 1 ⟩ ​ ⟨ K 2 ​ H , H ​ K 2 ⟩ . \mathrm{CKA}(K_{1},K_{2})=\frac{\langle K_{1}H,HK_{2}\rangle}{\sqrt{\langle K_{1}H,HK_{1}\rangle\,\langle K_{2}H,HK_{2}\rangle}}. (29)

[308] p: For the sake of completeness we now share a few classical results regarding CKA.

[309] h4: Kernel centering.

[310] p: The matrix H H plays the role of centering the data in feature space. We define the centered kernel as

[311] table: K ¯ = H ​ K ​ H . \bar{K}=HKH. (30)

[312] p: This operation corresponds to centering the underlying representations before computing pairwise similarities. Indeed, in the linear case where K = X ​ X ⊤ K=XX^{\top} for data matrix X ∈ ℝ n × d X\in\mathbb{R}^{n\times d} , we have

[313] table: K ¯ = X ¯ ​ X ¯ ⊤ , \bar{K}=\bar{X}\bar{X}^{\top}, (31)

[314] p: where X ¯ \bar{X} denotes the centered features X ¯ i = X i − 1 n ​ ∑ j = 1 n X j \bar{X}_{i}=X_{i}-\frac{1}{n}\sum_{j=1}^{n}X_{j} i.e. X ¯ = H ​ X \bar{X}=HX .

[315] h4: CKA as a cosine affinity.

[316] p: A well known property of CKA is that it can be interpreted as a cosine similarity between centered kernels, viewed as vectors in ℝ n 2 \mathbb{R}^{n^{2}} .

[317] h6: Proposition C.5 .

[318] p: Let K ¯ 1 = H ​ K 1 ​ H \bar{K}_{1}=HK_{1}H and K ¯ 2 = H ​ K 2 ​ H \bar{K}_{2}=HK_{2}H . Then CKA can be written as

[319] table: CKA ⁡ ( K 1 , K 2 ) = k ⁡ ( vec ⁡ ( K ¯ 1 ) , vec ⁡ ( K ¯ 2 ) ) , \mathrm{CKA}(K_{1},K_{2})=k\!\left(\mathrm{vec}(\bar{K}_{1}),\mathrm{vec}(\bar{K}_{2})\right), (32)

[320] p: where k ⁡ ( ⋅ , ⋅ ) k(\cdot,\cdot) denotes the cosine affinity and vec ⁡ ( ⋅ ) \mathrm{vec}(\cdot) denotes matrix vectorization.

[321] h6: Proof.

[322] p: Recall that H = I n − 1 n ​ 𝟏𝟏 ⊤ H=I_{n}-\frac{1}{n}\mathbf{1}\mathbf{1}^{\top} is symmetric and idempotent, i.e., H ⊤ = H H^{\top}=H and H 2 = H H^{2}=H . We compute

[323] table: ⟨ H ​ K 1 ​ H , H ​ K 2 ​ H ⟩ \displaystyle\langle HK_{1}H,HK_{2}H\rangle = tr ⁡ ( H ​ K 1 ​ H ​ H ​ K 2 ​ H ) \displaystyle=\mathrm{tr}\!\left(HK_{1}H\,HK_{2}H\right) = tr ⁡ ( H ​ K 1 ​ H ​ K 2 ​ H ) \displaystyle=\mathrm{tr}\!\left(HK_{1}HK_{2}H\right) = tr ⁡ ( K 1 ​ H ​ K 2 ​ H ) \displaystyle=\mathrm{tr}\!\left(K_{1}HK_{2}H\right) = ⟨ K 1 ​ H , H ​ K 2 ⟩ , \displaystyle=\langle K_{1}H,HK_{2}\rangle,

[324] p: where we used cyclic invariance of the trace and the idempotence of H H .

[325] p: In particular, setting K 1 = K 2 = K K_{1}=K_{2}=K yields

[326] table: ⟨ H ​ K ​ H , H ​ K ​ H ⟩ = ‖ H ​ K ​ H ‖ F 2 . \langle HKH,HKH\rangle=\|HKH\|_{F}^{2}. (33)

[327] p: Combining these identities proves that CKA is exactly the cosine similarity between the vectorized centered kernels. ∎

[328] h4: Computational Complexity.

[329] p: We conclude this section by providing the computational complexity of CKA for linear kernels, as considered in this work.

[330] h6: Proposition C.6 .

[331] p: Assume that

[332] table: K 1 = X 1 ​ X 1 ⊤ with ​ X 1 ∈ ℝ n × d 1 , K 2 = X 2 ​ X 2 ⊤ with ​ X 2 ∈ ℝ n × d 2 , K_{1}=X_{1}X_{1}^{\top}\quad\text{with }X_{1}\in\mathbb{R}^{n\times d_{1}},\qquad K_{2}=X_{2}X_{2}^{\top}\quad\text{with }X_{2}\in\mathbb{R}^{n\times d_{2}},

[333] p: and denote d = max ⁡ ( d 1 , d 2 ) d=\max(d_{1},d_{2}) . Then the memory complexity of computing CKA ⁡ ( K 1 , K 2 ) \mathrm{CKA}(K_{1},K_{2}) is

[334] table: 𝒪 ⁡ ( n ​ d + d 2 ) . \mathcal{O}\big(nd+d^{2}\big).

[335] h6: Proof.

[336] p: Assume that X 1 X_{1} and X 2 X_{2} are centered, which can be done in 𝒪 ⁡ ( n ​ D ) \mathcal{O}(nD) time and memory. Using the identities established above, we have

[337] table: ⟨ K 1 ​ H , H ​ K 2 ⟩ = ⟨ X 1 ​ X 1 ⊤ , X 2 ​ X 2 ⊤ ⟩ = ⟨ X 1 ⊤ ​ X 2 , X 1 ⊤ ​ X 2 ⟩ = ‖ X 1 ⊤ ​ X 2 ‖ F 2 . \langle K_{1}H,HK_{2}\rangle=\langle X_{1}X_{1}^{\top},X_{2}X_{2}^{\top}\rangle=\langle X_{1}^{\top}X_{2},\,X_{1}^{\top}X_{2}\rangle=\|X_{1}^{\top}X_{2}\|_{F}^{2}.

[338] p: Thus, computing the numerator only requires storing the d 1 × d 2 d_{1}\times d_{2} matrix X 1 ⊤ ​ X 2 X_{1}^{\top}X_{2} .

[339] p: Similarly,

[340] table: ‖ K 1 ​ H ‖ F 2 = ‖ X 1 ⊤ ​ X 1 ‖ F 2 , ‖ K 2 ​ H ‖ F 2 = ‖ X 2 ⊤ ​ X 2 ‖ F 2 , \|K_{1}H\|_{F}^{2}=\|X_{1}^{\top}X_{1}\|_{F}^{2},\qquad\|K_{2}H\|_{F}^{2}=\|X_{2}^{\top}X_{2}\|_{F}^{2},

[341] p: which require storing only the d 1 × d 1 d_{1}\times d_{1} and d 2 × d 2 d_{2}\times d_{2} Gram matrices, respectively.

[342] p: Therefore, the overall memory complexity is dominated by storing X 1 , X 2 X_{1},X_{2} and the associated Gram matrices, yielding

[343] table: 𝒪 ⁡ ( n ​ D + d 2 ) , \mathcal{O}(nD+d^{2}),

[344] p: as claimed. ∎

[345] h2: Instructions for reporting errors

[346] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[347] p: Tip: You can select the relevant text first, to include it in your report.

[348] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[349] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
