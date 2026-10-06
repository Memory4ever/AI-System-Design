[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: DWA-KD: Dual-Space Weighting and Time-Warped Alignment for Cross-Tokenizer Knowledge Distillation

[3] h6: Abstract

[4] p: Knowledge Distillation (KD) has emerged as a crucial technique for compressing Large Language Models (LLMs). Although existing cross-tokenizer KD methods have made notable progress, their effectiveness remains constrained by suboptimal alignment across sequence and vocabulary levels. To address these limitations, we introduce Dual-Space Weighting and Time-Warped Alignment (DWA-KD), a novel cross-tokenizer distillation framework that enhances token-wise distillation through dual-space entropy-based weighting and achieves precise sequence-level alignment by leveraging both lexical and semantic information. At the token level, DWA-KD maps teacher representations into the student space and vice versa, performing dual-space KD via Kullback–Leibler divergence (KL). The process is modulated by dual-space weights that up-weight tokens where the student is uncertain and the teacher is confident, thereby focusing learning on informative tokens rather than treating all positions equally. At the sequence level, DWA-KD applies Soft Dynamic Time Warping (Soft-DTW) to both the embedding and final hidden-state layers, enabling robust alignment of lexical and contextual semantics between teacher and student sequences. Extensive experiments across diverse NLP benchmarks demonstrate that DWA-KD outperforms state-of-the-art KD baselines, while ablation studies confirm the complementary contributions of entropy-based token weighting and embedding and final hidden state layer Soft-DTW alignment.

[5] h2: 1 Introduction

[6] p: Large language models deliver strong results but incur high compute, memory, and latency Kaplan et al. (2020) ; Chowdhery et al. (2023) ; Touvron et al. (2023) ; OpenAI (2023) . This creates a need for smaller models that remain efficient in practice. Knowledge distillation (KD) Hinton et al. (2015) has emerged as a promising solution to this challenge by transferring knowledge from a large teacher model to a compact student model, maintaining essential performance while reducing inference overhead ( Ko et al., 2024 ; Chen et al., 2025 ; Gu et al., 2024 ) . Conventional KD is effective for LLMs but is often constrained by a same-tokenizer setting, i.e., requiring shared vocabulary between teacher and student, which limits applicability across heterogeneous models Wen et al. (2023) ; Gu et al. (2024) ; Ko et al. (2024) .

[7] p: Cross-tokenizer KD (CTKD) removes the shared-tokenizer assumption but introduces main challenges: (i) tokenization mismatch and (ii) sequence misalignment . Recent CTKD methods address these challenges by leveraging Optimal Transport (OT) ( Boizard et al., 2024 ; Cui et al., 2025 ) , learning projectors and uses cross-model attention to reconcile hidden spaces ( Zhang et al., 2024 ) or aligning strings with dynamic programming on token sequences ( Wan et al., 2024 ) . While OT-based sequence alignment ( Boizard et al., 2024 ; Cui et al., 2025 ; Truong et al., 2025 ) does not inherently preserve temporal order ( Su and Hua, 2017 ) , Wan et al. (2024) and Zhang et al. (2024) only captures surface form or logit-level and overlook semantics ( Chen et al., 2025 ) . Meanwhile, a novel method - Contextual Dynamic Mapping (CDM) ( Chen et al., 2025 ) - introduces entropy-weighted dynamic programming based on Dynamic Time Warping (DTW) to adapt token alignment. However, CDM is computationally expensive. Its string-level DP uses CPU-side loops each forward pass, which leads to GPU under-utilization. Recent work has also explored cross-tokenizer distillation under preference/alignment signals ( Nguyen et al., 2026 ) .

[8] p: DTW-based objectives also appear in broader settings (e.g., Fu et al. (2023) ; Wan et al. (2024) ), which is used to align at sequence-level. Despite recent progress in cross-tokenizer knowledge distillation, current approaches exhibit significant limitations. These methods assume all tokens contribute equally, neglecting the varying importance or informativeness of individual tokens. Moreover, sequence-level context is often under-weighted in CTKD, weakening robustness when tokenizers diverge substantially.

[9] p: To address these limitations, we propose Dual-Space Weighting and Time-Warped Alignment (DWA-KD) , a CTKD framework that aligns teacher and student at both token and sequence levels. At the token level, we adopt an asymmetric scheme: on the student side , each position is weighted by the product of the student’s normalized entropy and the teacher’s projected confidence (the maximum probability after mapping the teacher distribution into the student vocabulary), emphasizing updates where the student is uncertain and the teacher target is reliable; on the teacher side , we use entropy-only weighting, assigning larger weights to low-entropy (confident) teacher tokens. This dual mechanism concentrates learning on the most consequential tokens while avoiding noisy or redundant updates. At the sequence level, we employ normalized Soft-DTW ( Cuturi and Blondel, 2017 ) with an attention-informed soft band over both embeddings and final hidden states, reducing input-level mismatch and encouraging the student to track the teacher’s semantic trajectory before producing logits.

[10] p: We evaluate our framework across multiple benchmarks under cross-tokenizer setting. The experimental results demonstrate that DWA-KD exhibits superiority over existing cross-tokenizer distillation approaches among different datasets. Furthermore, ablation study confirms the effectiveness of our main components. In summary, the main contributions of this work are:

[11] p: We present Dual-Space Weighting and Time-Warped Alignment (DWA-KD) , a cross-tokenizer distillation framework that couples selective token-level transfer with sequence-level Soft-DTW, applied to both embeddings and final hidden states, with an attention-informed soft band that keeps alignments plausible and gradients smooth.

[12] p: We introduce a dual-space token weighting scheme : on the student side, weights scale with the product of student uncertainty and teacher → \to student projected confidence; on the teacher side, weights increase with teacher confidence (low entropy). This focuses learning on tokens that matter while suppressing noisy updates.

[13] p: We conduct comprehensive experiments across diverse datasets to evaluate our approach, showing that it enhances the performance of student models compared to standard knowledge distillation baselines.

[14] h2: 2 Related Work and Background

[15] h5: Knowledge Distillation

[16] p: Knowledge distillation (KD) is a widely adopted technique for transferring knowledge from a teacher to a student model by aligning soft targets such as logits or intermediate representations Hinton et al. (2015) ; Kim and Rush (2016) . With the rise of large language models (LLMs), many conventional KD methods Park et al. (2021) ; Gu et al. (2023) ; Wu et al. (2024) ; Ko et al. (2024) , while effective, are often limited to same-tokenizer setting. Cross-tokenizer KD Zhou et al. (2022) ; Zhang et al. (2023) ; Liu et al. (2022) addresses this challenge but introduce other problem, mainly tokenization mismatch and sequence mismatch. To address these issues, DSKD ( Zhang et al., 2024 ) aligns tokens by learning projectors that map student and teacher hidden states into a shared space, but it treats all positions equally and ignores token-wise importance. MultiLevelOT ( Cui et al., 2025 ) and MCW-KD ( Vuong et al., 2026 ) leverage Wasserstein/OT-style objectives for distillation. Beyond token-level matching, MultiLevelOT ( Cui et al., 2025 ) and CDM ( Chen et al., 2025 ) further extend alignment to token and sequence levels: MultiLevelOT measures discrepancies within and across tokens via optimal transport but does not inherently preserve temporal order, while CDM applies entropy-weighted DTW in the logit space, which can underuse contextual information encoded in hidden states. In contrast, our approach employs asymmetric token weighting and applies normalized Soft-DTW at both the embedding and final hidden-state layers. This combination reduces input-level mismatch and better captures semantic trajectories, enabling more precise and efficient knowledge transfer.

[17] h5: Dynamic Time Warping

[18] p: Dynamic Time Warping (DTW) Sakoe and Chiba (1978) is a classical algorithm for computing optimal alignments between temporal sequences, accommodating differences in length or variations in speed. Its original formulation, however, is non-differentiable, limiting use in gradient-based learning. Soft Dynamic Time Warping (Soft-DTW) Cuturi and Blondel (2017) addresses this by replacing the hard minimum with a smooth approximation, enabling end-to-end training. Soft-DTW has demonstrated improved stability and performance in domains such as time series regression, speech, handwriting, and motion trajectory prediction. Building on this, several DTW-based methods leverage soft alignment to capture temporal or structural correspondences between teacher and student representations, aligning token spans before pooling logits for divergence computation Fu et al. (2023) ; Wan et al. (2024) ; Chen et al. (2025) . In contrast, our approach applies Soft-DTW directly at the embedding and hidden-state levels, providing differentiable alignment that captures both lexical and semantic dependencies for more effective knowledge transfer.

[19] h3: 2.1 Background

[20] h4: 2.1.1 Dual-Space Knowledge Distillation

[21] p: DSKD ( Zhang et al., 2024 ) addresses tokenization mismatch by learning soft correspondences between student and teacher tokens via a cross-model attention (CMA) layer. Concretely, student embeddings of input and target tokens are concatenated and projected to query vectors Q ∈ ℝ S × 2 ​ D Q\in\mathbb{R}^{S\times 2D} ; teacher embeddings and output hidden states are then normalized to form key vectors K ∈ ℝ T × 2 ​ D K\in\mathbb{R}^{T\times 2D} and projected to value vectors V ∈ ℝ T × d V\in\mathbb{R}^{T\times d} . Scaled dot-product attention is formalized as:

[22] table: a t → s = softmax ⁡ ( Q ​ K ⊤ 2 ​ D ) ∈ ℝ S × T . a^{t\to s}=\mathrm{softmax}\!\left(\frac{QK^{\top}}{\sqrt{2D}}\right)\in\mathbb{R}^{S\times T}. (1)

[23] p: produces teacher-to-student alignments and being used to align teacher hidden state to student hidden state h ~ t → s = a t → s ​ V ∈ ℝ n × d . \tilde{h}^{t\to s}=a^{t\to s}V\in\mathbb{R}^{n\times d}. A reverse alignment matrix is defined as:

[24] table: a s → t = softmax ​ ( K ​ Q ⊤ 2 ​ D ) ∈ ℝ T × S a^{s\to t}=\text{softmax}\left(\frac{KQ^{\top}}{\sqrt{2D}}\right)\in\mathbb{R}^{T\times S} (2)

[25] p: and also be used to project and align student’s hidden states to teacher’s hidden state h ~ s → t = a s → t ​ P s → t ​ ( h s , θ P s → t ) ∈ ℝ T × D . \tilde{h}^{s\to t}=a^{s\to t}P^{s\to t}\big(\,h^{s};\theta^{s\to t}_{P}\,\big)\in\mathbb{R}^{T\times D}. where h s h^{s} is the output hidden states of the whole sequence from the student model.

[26] h5: Dual-Space KD.

[27] p: (i) Student space: h ~ t → s \tilde{h}^{t\to s} is mapped by the student head to produce output distribution p t → s p^{t\to s} . Because the projectors start at random, an auxiliary cross-entropy is used to warm them up; then a KL term matches p t → s p^{t\to s} to the student distribution p s p^{s} . (ii) Teacher space: reverse-aligned hidden state h ~ s → t \tilde{h}^{s\to t} are passed through the teacher head to obtain p s → t p^{s\to t} , which is aligned to the teacher distribution p t p^{t} via KL.

[28] h5: Objective.

[29] p: The final loss sums KD in both spaces plus the auxiliary CE:

[30] table: ℒ DSKD = ℒ kd stu + ℒ kd tea + ℒ ce t → s . \mathcal{L}_{\mathrm{DSKD}}=\mathcal{L}_{\mathrm{kd}}^{\mathrm{stu}}+\mathcal{L}_{\mathrm{kd}}^{\mathrm{tea}}+\mathcal{L}_{\mathrm{ce}}^{t\to s}. (3)

[31] h4: 2.1.2 Dynamic Time Warping (DTW)

[32] p: DTW ( Sakoe and Chiba, 1978 ) is a dynamic-programming method that aligns two time sequences by allowing non-linear time warping. This property makes DTW particularly useful for sequences with varying lengths or speed variations. Formally, given sequences X = ( x 1 , … , x N ) , X=(x_{1},\dots,x_{N}), and Y = ( y 1 , … , y M ) , Y=(y_{1},\dots,y_{M}), DTW constructs a cost matrix 𝐂 ∈ ℝ N × M \mathbf{C}\in\mathbb{R}^{N\times M} with entries:

[33] table: C i ​ j = d ⁡ ( x i , y j ) , C_{ij}=d(x_{i},y_{j}), (4)

[34] p: where d ⁡ ( ⋅ , ⋅ ) d(\cdot,\cdot) is a local distance function (e.g., squared Euclidean distance), and computes the accumulated cost matrix 𝐑 \mathbf{R} recursively via:

[35] table: R i ​ j = C i ​ j + min ⁡ ( R i − 1 , j , R i , j − 1 , R i − 1 , j − 1 ) . R_{ij}=C_{ij}+\min\big(R_{i-1,j},\,R_{i,j-1},\,R_{i-1,j-1}\big). (5)

[36] p: While DTW preserves the temporal order of elements, the non-differentiability of the min \min operator prevents its direct integration into gradient-based learning frameworks. Soft Dynamic Time Warping (Soft-DTW) Cuturi and Blondel (2017) extends DTW by introducing a differentiable relaxation of the alignment cost. The non-differentiable min \min in the recurrence is replaced with a smooth softmin operator:

[37] table: min ( a 1 , … , a n ) γ = − γ log ∑ i e − a i / γ \min{}^{\gamma}(a_{1},\dots,a_{n})=-\gamma\log\sum_{i}e^{-a_{i}/\gamma} (6)

[38] p: where γ > 0 \gamma>0 controls the smoothness and as γ → 0 \gamma\to 0 , it converges to the standard minimum. Incorporating this operator into the DTW recurrence yields a differentiable cost that supports backpropagation, enabling end-to-end training in sequence modeling tasks such as knowledge distillation, speech modeling, and time series prediction.

[39] h2: 3 Methodology

[40] h3: 3.1 Notations

[41] p: Let the student and teacher models produce token sequences 𝐱 = ( x 1 , x 2 , … , x S ) \mathbf{x}=(x_{1},x_{2},\ldots,x_{S}) and 𝐲 = ( y 1 , y 2 , … , y T ) \mathbf{y}=(y_{1},y_{2},\ldots,y_{T}) , with respective vocabularies of sizes V s V^{s} and V t V^{t} . The student’s predictive distribution over its vocabulary is denoted as p s ​ ( x i ∣ x < i ) ∈ ℝ V s p^{s}(x_{i}\mid x_{<i})\in\mathbb{R}^{V^{s}} , and the teacher’s predictive distribution over its own vocabulary is denoted as p t ​ ( y j ∣ y < j ) ∈ ℝ V t p^{t}(y_{j}\mid y_{<j})\in\mathbb{R}^{V^{t}} . The entropy of the student model at position i i is defined as

[42] table: H s ( x i ) = − ∑ i = 1 V s p s ( x i ∣ x < i ) log p s ( x i ∣ x < i ) , H^{s}(x_{i})=-\sum_{i=1}^{V^{s}}p^{s}(x_{i}\mid x_{<i})\log p^{s}(x_{i}\mid x_{<i}), (7)

[43] p: and the entropy of the teacher model at position j j is given by

[44] table: H t ( y j ) = − ∑ j = 1 V t p t ( y j ∣ y < j ) log p t ( y j ∣ y < j ) . H^{t}(y_{j})=-\sum_{j=1}^{V^{t}}p^{t}(y_{j}\mid y_{<j})\log p^{t}(y_{j}\mid y_{<j}). (8)

[45] p: Additionally, let the student and teacher produce embedding sequences E s = ( e 1 s , e 2 s , … , e S s ) ∈ ℝ S × d S E^{s}=(e^{s}_{1},e^{s}_{2},\ldots,e^{s}_{S})\in\mathbb{R}^{S\times d_{S}} and E t = ( e 1 t , e 2 t , … , e T t ) ∈ ℝ T × d T , E^{t}=(e^{t}_{1},e^{t}_{2},\ldots,e^{t}_{T})\in\mathbb{R}^{T\times d_{T}}, as well as final hidden-state representations H s = ( h 1 s , h 2 s , … , h S s ) ∈ ℝ S × d S H^{s}=(h^{s}_{1},h^{s}_{2},\ldots,h^{s}_{S})\in\mathbb{R}^{S\times d_{S}} and H t = ( h 1 t , h 2 t , … , h T t ) ∈ ℝ T × d T . H^{t}=(h^{t}_{1},h^{t}_{2},\ldots,h^{t}_{T})\in\mathbb{R}^{T\times d_{T}}. Since teacher and student models typically differ in dimensionality, two lightweight linear projections W e t → s , W h t → s ∈ ℝ d S × d T W^{t\rightarrow s}_{e},W^{t\rightarrow s}_{h}\in\mathbb{R}^{d_{S}\times d_{T}} are introduced to map teacher representations into the student space:

[46] table: E ~ t \displaystyle\tilde{E}^{t} = E t ​ ( W e t → s ) ⊤ , \displaystyle=E^{t}(W^{t\rightarrow s}_{e})^{\top}, (9) H ~ t \displaystyle\tilde{H}^{t} = H t ​ ( W h t → s ) ⊤ . \displaystyle=H^{t}(W^{t\rightarrow s}_{h})^{\top}. (10)

[47] p: Moreover, as in DSKD, the teacher to student distribution p t → s ​ ( x i ∣ x < i ) p^{t\to s}(x_{i}\mid x_{<i}) is aligned to the student distribution p s ​ ( x i ∣ x < i ) p^{s}(x_{i}\mid x_{<i}) via D ( ⋅ ∣ ⋅ ) D(\cdot\mid\cdot) . Conversely, student to teacher distribution p s → t ​ ( y j ∣ y < j ) p^{s\to t}(y_{j}\mid y_{<j}) is aligned to the teacher distribution p t ​ ( y j ∣ y < j ) p^{t}(y_{j}\mid y_{<j}) via D ( ⋅ ∣ ⋅ ) D(\cdot\mid\cdot) . Here D ( ⋅ ∣ ⋅ ) D(\cdot\mid\cdot) denotes KL divergence.

[48] h3: 3.2 Weighted Dual-Space Knowledge Distillation

[49] p: In sequence modeling, not all tokens contribute equally to the learning process. Certain tokens carry more informative or uncertain content, whereas others are predictable or less critical Zhong et al. (2024) ; Akhauri et al. (2025) . To more effectively guide the student model during knowledge distillation, it is beneficial to assign distinct weights to individual tokens, thereby emphasizing those of greater significance ( Le et al., 2025 ) . Our approach enables the learning process to concentrate on the most certain teacher token elements of the sequence, enhancing both training efficiency and overall model performance. In this work, we propose a mechanism for assigning weights to each token in both the student and teacher spaces. To ensure stability during training, we scale the token weights so that their sum equals the sequence length. This normalization makes the KD process robust to both sequence length variability and shifting entropy distributions as the model learns, avoiding the need for constant retuning of loss coefficients.

[50] h5: Token weight in student space.

[51] p: Inspired by Wang et al. (2025) and Furlanello et al. (2018) , in the student space, we weight each token by combining the student’s uncertainty with the teacher’s confidence projected into the student vocabulary. Formally, we define peak confidence from teacher at student sequence position i i as:

[52] table: g t → s ​ ( x i ) = max i ∈ V s ⁡ p t → s ​ ( x i ∣ x < i ) . g^{t\to s}(x_{i})\;=\;\max_{i\in V_{s}}\;p^{t\to s}(x_{i}\mid x_{<i}). (11)

[53] p: The weight w i ( s ) w_{i}^{(s)} of student token i i is defined as:

[54] table: w i ( s ) = H s ​ ( x i ) ⋅ g t → s ​ ( x i ) . w^{(s)}_{i}={H}^{s}(x_{i})\;\cdot\;g^{t\to s}(x_{i}). (12)

[55] p: By weighting each student token as Eq. 12 , we consider a token to be important only when the student needs help (high uncertainty), and that token has a reliable teacher target in the student’s vocabulary (high peak confidence). Consequently, the knowledge distillation loss in the student space is formulated as:

[56] table: L ~ KD stu = ∑ i w i ( s ) D ( p t → s ( x i ∣ x < i ) ∥ p s ( x i ∣ x < i ) ) , \widetilde{L}_{\text{KD}}^{\text{stu}}=\sum_{i}w_{i}^{(s)}\,D(p^{t\to s}(x_{i}\mid x_{<i})\;\|\;p^{s}(x_{i}\mid x_{<i})), (13)

[57] p: This weighting mechanism prevent wasting capacity on tokens the student already knows (low entropy) or where the teacher is unsure (low max-probability).

[58] h5: Token weight in teacher space.

[59] p: In the teacher space, we assign token weights based on the teacher’s confidence, computed as a normalized complement of the token-level entropy.

[60] table: w j ( t ) = 1 − H t ​ ( y j ) log ⁡ V t w^{(t)}_{j}=1-\frac{H^{t}(y_{j})}{\log V^{t}} (14)

[61] p: This weighting mechanism ensures that the student primarily learns from tokens where the teacher is confident (low entropy), while ignoring uncertain teacher tokens, thereby reducing potential noise. Consequently, the knowledge distillation loss in the teacher space is formulated as:

[62] table: L ~ KD tea = ∑ j w j ( t ) D ( p t ( x j ∣ x < j ) ∥ p s → t ( x j ∣ x < j ) ) \widetilde{L}_{\text{KD}}^{\text{tea}}=\sum_{j}w_{j}^{(t)}\,D\big(p^{t}(x_{j}\mid x_{<j})\,\|\,p^{s\to t}(x_{j}\mid x_{<j})\big) (15)

[63] h5: Token alignment loss.

[64] p: The overall loss of token level alignment combines the KD losses in both spaces with the cross-entropy loss:

[65] table: L W-KD = L ~ KD stu + L ~ KD tea + L CE t → s . {L}_{\text{W-KD}}=\widetilde{L}_{\text{KD}}^{\text{stu}}+\widetilde{L}_{\text{KD}}^{\text{tea}}+{L}_{\text{CE}}^{t\to s}. (16)

[66] h3: 3.3 Dynamic Time Warping Alignment

[67] p: We align teacher and student embeddings and hidden states in shared latent spaces via DTW loss to transfer representational and temporal knowledge across models with different architectures.

[68] h5: Pairwise costs.

[69] p: For each representation type (embedding or hidden), we measure pairwise dissimilarity between the student sequence and the projected-teacher sequence using cosine distance. * * * We share the projector for hidden-state representations with the projector used in DSKD and introduce an independent projector for embeddings. Let S S and T T be the student/teacher sequence lengths. The cost matrices C ∈ ℝ S × T C\in\mathbb{R}^{S\times T} are

[70] table: C ⁡ ( E stu , E ~ tea ) \displaystyle C\!\big(E^{\text{stu}},\tilde{E}^{\text{tea}}\big) = 1 − cos ⁡ ( E stu , E ~ tea ) , \displaystyle=1-\cos\!\big(E^{\text{stu}},\tilde{E}^{\text{tea}}\big), (17) C ⁡ ( H stu , H ~ tea ) \displaystyle C\!\big(H^{\text{stu}},\tilde{H}^{\text{tea}}\big) = 1 − cos ⁡ ( H stu , H ~ tea ) , \displaystyle=1-\cos\!\big(H^{\text{stu}},\tilde{H}^{\text{tea}}\big), (18)

[71] p: where cos ⁡ ( ⋅ , ⋅ ) \cos(\cdot,\cdot) denotes cosine similarity applied row-wise to produce an S × T S\times T matrix.

[72] h5: Banding via Attention Entropy.

[73] p: We start from the Sakoe–Chiba (SC) idea ( Sakoe and Chiba, 1978 ) and discourage off - diagonal warps by adding a fixed penalty to cross - cost entries outside a diagonal band. Rather than a hard mask, this soft penalty keeps the objective differentiable. The band is adapted per student position using DSKD cross - model attention matrix A between student and teacher tokens. Let A ∈ ℝ S × T A\in\mathbb{R}^{\text{S}\times\text{T}} be the row - normalized cross - model attention from student tokens to teacher tokens (rows sum to 1). We apply a row - wise softmax over teacher tokens, and use that distribution to set the band. For each student index, we form a soft center as the attention - weighted average teacher index, a linear center from the proportional diagonal, and blend the two to obtain the row’s band center; the band width widens with the row’s attention entropy. Formally, for each row i i :

[74] table: c i = α ​ ∑ j = 1 T j ​ A i , j + ( 1 − α ) ​ i ⋅ T S . c_{i}=\alpha\sum_{j=1}^{T}jA_{i,j}+(1-\alpha)i\cdot\frac{T}{S}. (19)

[75] p: The band width is then set from the attention entropy - high entropy (uncertain attention) yields a wider band, while low entropy tightens it:

[76] table: H i = − ∑ j = 1 T A i , j log A i , j , H_{i}=-\sum_{j=1}^{T}A_{i,j}\log A_{i,j}, (20)

[77] p: And the adaptive width is the combination of base width b b (the minimum band size even under low uncertainty) and attention entropy H i H_{i} :

[78] table: w i = b + β ​ H i . w_{i}=b+\beta H_{i}. (21)

[79] p: The final cross-cost is penalized outside the adaptive band:

[80] table: C ~ i , j s , t = C i , j s , t + λ band ⋅ 𝟏 | j − c i | > w i . \tilde{C}^{s,t}_{i,j}=C^{s,t}_{i,j}+\lambda_{\text{band}}\cdot\mathbf{1}_{|j-c_{i}|>w_{i}}. (22)

[81] p: Additional details of formulation of attention matrix A A are provided in Appendix C .

[82] h5: Sequence-level Alignment via Soft-DTW

[83] p: Let s γ ​ ( X , Y ) ≡ sDTW γ ​ ( C ~ ​ ( X , Y ) ) s_{\gamma}(X,Y)\equiv\mathrm{sDTW}_{\gamma}\!\big(\widetilde{C}(X,Y)\big) denote the Soft-DTW score on the cost matrix with adaptive band C ~ ​ ( X , Y ) \widetilde{C}(X,Y) . Following prior work on Soft-DTW divergence ( Cuturi and Blondel, 2017 ; Blondel et al., 2021 ) , we remove self-similarity bias and enforce symmetry by

[84] table: nDTW γ ​ ( X , Y ) = s γ ​ ( X , Y ) − Δ γ ​ ( X , Y ) \displaystyle\mathrm{nDTW}_{\gamma}(X,Y)=s_{\gamma}(X,Y)-\Delta_{\gamma}(X,Y) (23) Δ γ ​ ( X , Y ) = 1 2 ​ [ s γ ​ ( X , X ) + s γ ​ ( Y , Y ) ] . \displaystyle\Delta_{\gamma}(X,Y)\;=\;\tfrac{1}{2}\!\left[s_{\gamma}(X,X)+s_{\gamma}(Y,Y)\right]. (24)

[85] p: We apply these formulas to the pairs ( X , Y ) ∈ { ( E stu , E ~ tea ) , ( H stu , H ~ tea ) } (X,Y)\in\{(E^{\text{stu}},\tilde{E}^{\,\text{tea}}),\;(H^{\text{stu}},\tilde{H}^{\,\text{tea}})\} . This normalization makes distances comparable across sequences of different lengths or embedding magnitudes and stabilizes gradients. We sum the divergences at the hidden and embedding levels:

[86] table: L DTW = n ​ D ​ T ​ W γ ​ ( H s ​ t ​ u , H ~ t ​ e ​ a ) \displaystyle L_{\text{DTW}}\;=\;nDTW_{\gamma}\!\big(H^{stu},\,\tilde{H}^{\,tea}\big) + n ​ D ​ T ​ W γ ​ ( E s ​ t ​ u , E ~ t ​ e ​ a ) \displaystyle+nDTW_{\gamma}\!\big(E^{stu},\,\tilde{E}^{\,tea}\big) (25)

[87] p: The first term promotes temporal agreement between hidden-state trajectories; the second anchors lexical correspondences via token embeddings. Together, they encourage the student to absorb both contextual (semantic) and lexical structure under tokenizer and length mismatches.

[88] h3: 3.4 Overall Loss

[89] p: The final training objective is formulated as a weighted combination of complementary components:

[90] table: L = λ CE ​ L CE + λ W-KD ​ L W-KD + λ DTW ​ L DTW L=\lambda_{\text{CE}}L_{\text{CE}}+\lambda_{\text{W-KD}}L_{\text{W-KD}}+\lambda_{\text{DTW}}L_{\text{DTW}}

[91] p: Here, ℒ CE \mathcal{L}_{\text{CE}} denotes the standard cross-entropy loss for supervised learning, ℒ W-KD \mathcal{L}_{\text{W-KD}} represents the knowledge distillation objective that transfers soft distributions from the teacher, and ℒ DTW \mathcal{L}_{\text{DTW}} captures temporal alignment between student and teacher via dynamic time warping. The coefficients λ CE , λ W-KD , λ DTW \lambda_{\text{CE}},\lambda_{\text{W-KD}},\lambda_{\text{DTW}} balance the contribution of each term.

[92] h2: 4 Experiments

[93] p: Our experiments demonstrate that DWA-KD outperforms existing cross-tokenizer distillation methods across multiple benchmarks. Ablation studies further verify the effectiveness of entropy-based token weighting and DTW with attention-informed banding in enhancing alignment and knowledge transfer. Additional experiments are in appendix D .

[94] h3: 4.1 Settings

[95] h4: Baselines and LLMs.

[96] p: We evaluate our method in cross-tokenizer settings using both small- and large-scale teacher-student pairs. For the small-scale setup, we consider Qwen 1.5–1.8B as the teacher and GPT-2 120M as the student, and Qwen 1.5–1.8B as the teacher and GPT-2 340M as the student. For the large-scale setup, we use Mistral 7B as the teacher with TinyLlama 1.1B as the student, and Qwen 2.5–7B as the teacher with GPT-2 1.5B and OPT 2.7B as the student. We benchmark our approach against several cross-tokenizer knowledge distillation baselines, including ULD Boizard et al. (2024) , MinED Wan et al. (2024) , MultiLevelOT Cui et al. (2025) , and DSKD Zhang et al. (2024) 1 1 1 We exclude CDM ( Chen et al., 2025 ) from baselines because its string-level dynamic programming requires CPU-side loops at each forward pass, making large-scale GPU training impractical. .

[97] h4: Datasets

[98] p: We perform experiments on multiple instruction-following datasets. Following the approach of Gu et al. (2024) , we employ the DATABRICKS-DOLLY-15K dataset for the knowledge distillation process. For evaluation purposes, beyond this primary dataset, we incorporate three instruction-tuning benchmarks as supplementary test sets for out-of-distribution assessment: Super-Natural-Instructions ( S-NI ) Wang et al. (2022) , Vicuna Evaluation (VicunaEval) Chiang et al. (2023) , and Self-Instruct (Self-Inst) Wang et al. (2023) . This comprehensive evaluation enables us to examine the model’s generalization performance across a broad spectrum of instruction domains.

[99] h4: Training and Evaluation

[100] p: For GPT-2, we fully fine-tune both teacher and student models, while for TinyLLaMA we apply LoRA fine-tuning. Specifically, the temperature τ \tau is set to 2.0 based on validation set performance. In addition, all projectors in our approach are implemented as linear layers, which introduce only a small number of additional parameters during training. For evaluation, we generate responses from each model using five different random seeds, and the final performance is quantified by Rouge-L Lin (2004) between the generated outputs and the human-annotated references. Additional details on model configurations, along with the training and evaluation setup, are provided in Appendix A .

[101] h3: 4.2 Main Results

[102] figure: Methods Dolly SelfInst Vicuna S-NI Avg. Qwen-1.5 − - 1.8B → \rightarrow GPT2-120M Teacher 28.23 19.58 19.59 34.36 25.44 SFT 23.78 6.78 17.04 7.81 13.85 ULD 23.77 9.30 14.33 14.04 15.36 DSKD 24.26 10.07 15.25 17.15 16.68 MinED 24.21 10.02 14.96 16.40 16.40 MultiLevelOT 23.02 8.41 13.79 12.26 14.37 DWA-KD 24.29 11.15 15.64 19.63 17.68 Qwen-1.5 − - 1.8B → \rightarrow GPT2-340M Teacher 28.23 19.58 19.59 34.36 25.44 SFT 23.11 9.09 14.89 13.03 15.03 ULD 23.90 9.96 15.04 16.26 16.29 DSKD 25.43 11.29 15.08 17.18 17.25 MinED 24.48 11.21 15.56 15.69 16.74 MultiLevelOT 23.95 10.21 14.80 15.87 16.21 DWA-KD 26.64 12.10 16.99 21.67 19.35 Table 1: Rouge-L scores (in %) averaged over five random seeds across multiple benchmarks for two teacher–student pairs.

[103] figure: Methods Dolly SelfInst Vicuna S-NI Avg Qwen2.5-7B → \rightarrow GPT2-1.5B Teacher 28.49 24.67 20.48 39.87 28.38 SFT 21.83 13.62 15.95 21.66 18.27 ULD 24.52 15.11 15.94 26.18 20.44 MinED 25.52 15.39 16.15 26.25 20.83 MultiLevelOT 24.40 14.53 15.97 23.94 19.71 DSKD 25.38 16.10 16.84 25.82 21.04 DWA-KD 26.64 16.54 17.86 30.34 22.85 Qwen2.5-7B-Instruct → \rightarrow OPT-2.7B Teacher 28.49 24.67 20.48 39.87 28.38 SFT 27.10 13.90 16.60 24.90 20.63 ULD 26.65 15.37 16.97 25.44 21.11 MinED 26.89 14.98 17.04 25.94 21.21 MultiLevelOT 26.76 15.51 16.56 24.84 20.92 DSKD 26.93 16.22 17.86 27.33 22.09 DWA-KD 28.45 15.65 18.16 30.54 23.20 Mistral-7B → \rightarrow TinyLLaMA-1.1B Teacher 31.56 25.10 20.50 36.07 28.31 SFT 23.20 14.88 16.42 27.79 20.57 ULD 25.48 17.72 17.31 32.54 23.26 DSKD 26.28 17.19 18.74 31.93 23.54 MinED 25.54 18.23 17.02 31.42 23.05 MultiLevelOT 24.56 15.61 16.84 27.91 21.23 DWA-KD 26.38 19.62 17.63 36.59 25.06 Table 2: Rouge-L (%) on multiple teacher–student pairs. Bold indicates the best student score per block.

[104] p: Table 1 and table 2 summarizes the ROUGE-L performance of DWA-KD compared with standard supervised fine-tuning (SFT) and recent state-of-the-art cross-tokenizer knowledge distillation (CTKD) baselines, including ULD, DSKD, MinED, and MultiLevelOT. Evaluations were conducted across four teacher–student model pairs with distinct tokenization schemes on multiple benchmarks (Dolly, Self-Inst, Vicuna, and S-NI). Overall, DWA-KD achieves the best or competitive ROUGE-L scores across all teacher–student model pairs. For the Mistral-7B → TinyLLaMA-1.1B setting, DWA-KD attains the highest scores on four benchmarks, while remaining close to the best method on Dolly. In the Qwen-1.5B → GPT2-340M pair, it again delivers the best overall results, showing clear improvements on Vicuna and S-NI. For the Qwen2.5-7B-Instruct → GPT2-1.5B configuration, DWA-KD outperforms all baselines, being only slightly below DSKD on SelfInst. These results demonstrate that DWA-KD maintains strong and stable performance across diverse model scales and datasets. These results confirm that DWA-KD provides consistent improvements over existing CTKD approaches, validating the effectiveness of its dual-space weighting and time-warped alignment mechanisms.

[105] h3: 4.3 Evaluation via GPT-4

[106] p: To complement ROUGE-L, we also use the GPT-4.1 API as an automatic judge for pairwise comparisons between our method and each baseline. With a fixed evaluation prompt (Figure 4 ), the model selects the response that better follows the instruction; to reduce position bias ( Zheng et al., 2023 ) , outputs are randomly assigned to Responses A and B for every example. We report win rates over 100 pairs together with tie rates, and Figures 1 and 2 show that DWA-KD consistently outperforms all baselines in instruction-following quality.

[107] figure: Figure 1: Win rates (%) for distilling Mistral-7B to TinyLLaMA-1.1B , evaluated by GPT-4.1 on response quality.

[108] figure: Figure 2: Win rates (%) for distilling Qwen2.5-7B-Instruct to OPT-2.7B , evaluated by GPT-4.1 on response quality.

[109] h3: 4.4 Representation Similarity between Teacher and Student Models

[110] p: To conduct an empirical study to compare token-level response patterns between teacher and student models despite differing hidden state dimensions, we adopt the approach from Zhang et al. (2024) . For a given sentence with n tokens, we construct n × n structure matrices using cosine similarity and normalized inner products of the models’ hidden states. Lower values indicate that the student’s representations are closer to the teacher’s. We compute these distances over 100 training sentences and present results as box plots for the teacher–student pair Mistral-7B → TinyLlama-1.1B. Across Figure 3 , DWA-KD attains the smallest median distances, significantly smaller than others’, on both structure matrices—cosine and normalized inner product—indicating that DWA-KD more faithfully preserves the teacher’s token-to-token representation structure than all other methods.

[111] h3: 4.5 Ablation study

[112] h5: Impact of Each Component

[113] p: To understand the contribution of each module we introduced in our DWA-KD framework, we conducted an ablation study comparing 4 configurations: (1) using only entropy weighting, (2) using only the DTW alignment loss, (3) using only the DTW alignment loss with banding and (4) removing the gating mechanism we introduced in ( 11 ). Table 3 shows that each component contributes positively to the overall performance. Incorporating the DTW loss consistently improves alignment quality, while entropy-based weighting enhances token-level selectivity. Adding the adaptive banding further refines sequence matching, leading to the best overall performance when all modules are combined in the full DWA-KD framework.

[114] figure: Methods Dolly SelfInst Vicuna S-NI Avg. Qwen-1.5–1.8B → \rightarrow GPT2-120M ℒ D ​ S ​ K ​ D \mathcal{L}_{DSKD} 24.26 10.07 15.25 17.15 16.68 w/ EW 23.99 10.83 15.65 18.44 17.23 w/ DTW 23.76 11.26 15.25 18.93 17.30 w/ bDTW 24.05 10.77 15.75 18.42 17.25 w/o gate 23.94 10.89 15.82 19.36 17.50 DWA-KD 24.29 11.15 15.65 19.63 17.68 Mistral-7B → \rightarrow TinyLLaMA-1.1B ℒ D ​ S ​ K ​ D \mathcal{L}_{DSKD} 26.28 17.19 18.74 31.93 23.54 w/ EW 26.36 18.01 17.97 34.77 24.28 w/ DTW 26.36 18.35 17.72 32.39 23.71 w/ bDTW 26.67 18.84 17.76 33.17 24.11 w/o gate 26.47 18.77 16.91 37.98 25.03 DWA-KD 26.38 19.62 17.63 36.59 25.06 Table 3: Ablation results on instruction-following benchmarks. “Avg.” denotes the mean over the listed datasets. EW: entropy-only token weights; DTW: Soft-DTW loss; bDTW: Soft-DTW with attention-entropy banding; gate: applying the teacher → \to student max-probability gate.

[115] figure: Figure 3: Teacher–student representation structure distance (cosine and normalized inner product; lower is better) for the Qwen-1.5–1.8B → \to GPT2-120M pair.

[116] h2: 5 Conclusion

[117] p: We propose DWA-KD , a knowledge distillation framework that aligns teacher and student at both the token and sequence levels. At the token level, DWA-KD extends DSKD with importance weights to emphasize informative tokens during distillation. At the sequence level, it applies DTW to both embedding and final hidden-state sequences, aligning lexical and semantic trajectories across tokenizers. Experiments show that DWA-KD improves teacher–student alignment and consistently boosts student performance across diverse evaluation settings. Future work will explore multi-teacher distillation for stronger knowledge integration.

[118] h2: 6 Limitation

[119] p: While DWA-KD effectively improves knowledge transfer across heterogeneous tokenizers, several limitations remain. First, the Soft-DTW loss introduces quadratic complexity in sequence length, which can increase computational and memory overhead. Second, the approach relies on a stable teacher–student projection, and poor initialization may weaken early-stage supervision. Moreover, our work was conducted under limited computational budgets, which constrained the scale and diversity of experimentation. We view these limitations as opportunities for further development and broader evaluation, particularly with stronger projection/calibration schemes under tight compute.

[120] h2: Acknowledgments

[121] p: This project is funded by Vietnam National Foundation for Science and Technology Development (NAFOSTED) under grant number 102.05-2025.16.

[122] h2: References

[123] h2: Appendix A Experimental Details

[124] h3: A.1 Data

[125] p: All datasets in our experiments are preprocessed following Wan et al. (2024) . For training, we use the Databricks-Dolly- 15k dataset, which contains human-written instruction–response pairs and consists of 11435 samples for training, 1000 for validation, and 500 for testing. To evaluate the generalization ability of our models beyond the Dolly domain, we employ 3 additional datasets:

[126] p: SelfIns Wang et al. (2023) : A user-oriented instruction-following set contains 252 samples, covering a diverse range of practical tasks such as email composition, social-media postings, entertainment prompts or programming assistance.

[127] p: VicunaEval Chiang et al. (2023) : The 80 challenging questions used in the Vicuna evaluation, spanning 9 categories such as writing, roleplay, math, coding, and knowledge.

[128] p: S-NI Wang et al. (2022) : A large benchmark of NLP tasks and their natural language instructions. The test set of SuperNatural-Instructions consisting of 9K samples ranging from 119 tasks. Following Peng et al. (2023) , we split the set into 3 subsets whose ground response lengths lie in [0, 5], [6, 10] and [11, + ∞ +\infty ], and use the [11, + ∞ +\infty ] subset comprising 1694 samples.

[129] h3: A.2 Baselines

[130] p: We compare our method against state-of-the-art knowledge distillation techniques specifically designed to address discrepancies in tokenizers and vocabularies. These baselines provide a comprehensive framework for evaluating our method’s effectiveness to handle tokenizer and vocabulary disparities:

[131] p: ULD Boizard et al. (2024) : employs a Wasserstein distance-based loss to replace KL divergence, enabling distillation across different architectures and tokenizers.

[132] p: MinED Wan et al. (2024) : introduces a method based on Dynamic Time Warping (DTW) for sequence alignment, which aligns the logits between two token lists of the same sentence tokenized by different tokenizers.

[133] p: DSKD Zhang et al. (2024) : unifies the output spaces of the teacher and student distributions by projecting the output hidden states of teacher/student to the representation spaces of student/teacher, overcome limitations in similarity caused by their differing output spaces.

[134] p: MultiLevelOT Cui et al. (2025) : a cross-tokenizer knowledge distillation approach that leverages both sequence-aware token-level and sequence-level optimal transport for comprehensive distribution matching.

[135] h3: A.3 Training and Evaluation

[136] figure: Settings KD with Qwen1.5-1.8B KD with Mistral7B KD with Qwen2.5 GPT2-120M GPT2-340M Qwen1.5 TinyLLaMA Mistral7B GPT2-1.5B OPT2.7B Qwen2.5 Epoch 20 20 15 15 15 15 15 15 LR 5 × 10 − 4 5\times 10^{-4} 5 × 10 − 4 5\times 10^{-4} 2 × 10 − 5 2\times 10^{-5} 1 × 10 − 3 1\times 10^{-3} 1 × 10 − 3 1\times 10^{-3} 1 × 10 − 3 1\times 10^{-3} 1 × 10 − 3 1\times 10^{-3} 1 × 10 − 3 1\times 10^{-3} Projector LR 1 × 10 − 3 1\times 10^{-3} 1 × 10 − 3 1\times 10^{-3} 1 × 10 − 3 1\times 10^{-3} 1 × 10 − 3 1\times 10^{-3} 1 × 10 − 3 1\times 10^{-3} 1 × 10 − 3 1\times 10^{-3} 1 × 10 − 3 1\times 10^{-3} 1 × 10 − 3 1\times 10^{-3} Batch Size 8 8 8 8 8 8 8 8 LR Scheduler Cosine Cosine Cosine Cosine Cosine Cosine Cosine Cosine Fine-Tuning Method Full Full Full LoRA LoRA LoRA LoRA LoRA LoRA Rank N/A N/A N/A 256 256 256 256 256 LoRA Alpha N/A N/A N/A 8 8 8 8 8 LoRA Dropout N/A N/A N/A 0.1 0.1 0.1 0.1 0.1 Table 4: Detailed training configurations of KD with Qwen1.5-1.8B, Mistral7B, and Qwen2.5.

[137] p: We list the detailed training configurations for all models we trained in Table 4 . For evaluation, we used random sampling to decode the responses from all models. We set the decoding temperature and top_p to 1.0. We then generate the responses with 5 random seeds and report the averaged ROUGE-L score Lin (2004) of each seed. Besides, we also evaluate models using GPT-4.1 judgments. We randomly sample 100 instructions from the Dolly test set and generate one response per model using the same decoding settings (temperature and top-p = 1.0). The GPT-4.1 API is then prompted with a fixed evaluation template (Figure 4 ) to perform pairwise comparisons. To reduce position bias Zheng et al. (2023) , the two model outputs are randomly ordered as Response A and Response B for each case. We report the proportion of wins and ties across the 100 comparisons. In all experiments, we use fixed DTW banding hyperparameters without tuning; see Table 5 for values.

[138] figure: Symbol Description Value b b Base band width (in tokens) 5 β \beta Entropy sensitivity 2.0 α \alpha Blend between soft center and linear diagonal 0.7 λ \lambda Additive cost outside the band 1.0 Table 5: Hyperparameters used for soft-DTW banding.

[139] h2: Appendix B Representation Similarity between Teacher and Student Model

[140] p: Following Zhang et al. (2024) , we empirically evaluate how well the student’s token-level response patterns align with those of the teacher in a realistic KD setting. As the two models differ in hidden dimensionality, direct token-wise comparison of hidden states is infeasible. Instead, given the same input sentence, we compare the structure of token-to-token responses by constructing n × n n\times n structure matrices—computed via cosine similarity and normalized inner products between the models’ output hidden states:

[141] table: ℳ cosine ​ ( i , j ) = h i ⊤ ​ h j ‖ h i ‖ ​ ‖ h j ‖ ∈ ℝ n × n \mathcal{M}_{\text{cosine}}(i,j)=\frac{h_{i}^{\top}h_{j}}{\|h_{i}\|\|h_{j}\|}\in\mathbb{R}^{n\times n}

[142] table: ℳ prod ​ ( i , j ) = h i ⊤ ​ h j ∑ k h i ⊤ ​ h k ∈ ℝ n × n \mathcal{M}_{\text{prod}}(i,j)=\frac{h_{i}^{\top}h_{j}}{\sum_{k}h_{i}^{\top}h_{k}}\in\mathbb{R}^{n\times n}

[143] p: where ℳ prod \mathcal{M}_{\text{prod}} and ℳ prod \mathcal{M}_{\text{prod}} are structure matrices calculated by cosine and normalized inner-product between output hidden states, respectively. Then we calculate the L1 distance between the matrices of the student and the teacher:

[144] table: 𝒟 cosine = ∑ i = 1 n ∑ j = 1 n | ℳ cosine t ​ ( i , j ) − ℳ cosine s ​ ( i , j ) | \mathcal{D}_{\text{cosine}}=\sum_{i=1}^{n}\sum_{j=1}^{n}\left|\mathcal{M}_{\text{cosine}}^{t}(i,j)-\mathcal{M}_{\text{cosine}}^{s}(i,j)\right|

[145] table: 𝒟 prod = ∑ i = 1 n ∑ j = 1 n | ℳ prod t ​ ( i , j ) − ℳ prod s ​ ( i , j ) | \mathcal{D}_{\text{prod}}=\sum_{i=1}^{n}\sum_{j=1}^{n}\left|\mathcal{M}_{\text{prod}}^{t}(i,j)-\mathcal{M}_{\text{prod}}^{s}(i,j)\right|

[146] p: Lower values indicate closer alignment between student and teacher representations. We compute these distances on 1,000 training sentences and visualize them using box plots. Two teacher–student pairs are evaluated: Mistral-7B → TinyLLaMA-1.1B. As shown in figures 3 , DWA-KD achieves the lowest median L1 distances on both cosine and product-based structure matrices, showing that it better preserves the teacher’s token-level structure.

[147] h2: Appendix C Attention matrix in DTW banding

[148] p: Following Zhang et al. (2024) , we use a cross-model attention (CMA) matrix that automatically learns the alignment between tokens of the student sequence consist of S tokens and teacher sequence consist of T tokens. Specifically, the student’s input embeddings e s 1 : S e^{s}_{1:S} and target embeddings e s 2 : S + 1 e^{s}_{2:S+1} are concatenated along the last dimension, and project them through a query projector P q P_{q} :

[149] table: Q = P q ( [ e 1 : S s ; e 2 : S + 1 s ] ; θ P q ) ∈ ℝ S × 2 ​ D , Q=P_{q}([e^{s}_{1:S};e^{s}_{2:S+1}];\theta_{P}^{q})\in\mathbb{R}^{S\times 2D},

[150] p: For the teacher model, the key and value vectors are obtained from its embeddings and output hidden states:

[151] table: K = N ( [ e 1 : T t ; e 2 : T + 1 t ] ) ∈ ℝ T × 2 ​ D , K=N([e^{t}_{1:T};e^{t}_{2:T+1}])\in\mathbb{R}^{T\times 2D},

[152] table: V = P v ( N ( e 2 : T + 1 t ) + N ( h 1 : T t ) ; θ P v ) ∈ ℝ T × d , V=P_{v}(N(e^{t}_{2:T+1})+N(h^{t}_{1:T});\theta_{P}^{v})\in\mathbb{R}^{T\times d},

[153] p: where N ⁡ ( x ) = x / std ⁡ ( x ) N(x)=x/\mathrm{std}(x) denotes normalization by the standard deviation, which promotes faster convergence. The attention matrix is then computed as:

[154] table: A = softmax ⁡ ( Q ​ K ⊤ 2 ​ D ) ∈ ℝ T × S . A=\mathrm{softmax}\!\left(\frac{QK^{\top}}{\sqrt{2D}}\right)\in\mathbb{R}^{T\times S}.

[155] p: The attention-based center in Eq. 19 leverages the cross-model attention matrix A A to capture semantic alignment between student and teacher tokens. The term ∑ j j ​ A i , j \sum_{j}jA_{i,j} reflects a content-informed correspondence, indicating where the teacher’s information most strongly aligns with the student token i i . In contrast, the linear center i ⋅ T S i\cdot\tfrac{T}{S} encodes an absolute positional prior assuming uniform progression. Blending the two allows the band center to incorporate both semantic and positional alignment cues, yielding a more adaptive and stable alignment.

[156] h2: Appendix D Additional Experiments

[157] h3: D.1 Comparing with stronger CTKD baselines

[158] p: To better position DWA-KD against more recent cross-tokenizer distillation approaches suggested by reviewers, we implemented and evaluated two additional baselines: ALM ( Minixhofer et al., 2025 ) and DSKDv2 ( Zhang et al., 2025 ) , following their official descriptions/implementations under the same training recipe used throughout the paper (same data, epochs, optimizer settings, and evaluation protocol). Across representative teacher–student pair ( Qwen-1.5-1.8B → \rightarrow GPT2-120M ), DWA-KD remains consistently competitive and achieves higher average performance.

[159] figure: Method Dolly SelfInst Vicuna S-NI Avg. Qwen-1.5-1.8B → \rightarrow GPT2-120M Teacher 28.23 19.58 19.59 34.36 25.44 SFT 23.78 6.78 17.04 7.81 13.85 ALM 20.86 10.65 14.76 17.76 16.01 DSKD 24.26 10.07 15.25 17.15 16.68 DWA-KD 24.29 11.15 15.64 19.63 17.68 DSKDv2 24.37 10.89 15.52 20.37 17.78 DWA-KDv2 24.66 10.96 15.21 20.71 17.89 Table 6: Comparison with DSKDv2 and ALM on a representative teacher-student pair.

[160] h3: D.2 Efficiency and resource overhead

[161] p: Since DWA-KD includes a sequence-level Soft-DTW objective, we additionally report step time and GPU memory usage measured under the same sequence length regime as our main experiments. Table 7 shows that DWA-KD incurs only a modest overhead compared to common GPU-based CTKD baselines (DSKD, MinED, ULD) at batch size 4, while remaining substantially more efficient than CPU-based CDM in its supported batch-size-1 setting.

[162] figure: Method Avg Mem (GB) Peak Mem (GB) Step time (s) Batch size 4 DSKD 20.11 26.38 0.35 MinED 19.63 22.29 0.42 ULD 19.63 27.17 0.44 DWA-KD 20.17 29.92 0.45 Batch size 1 CDM* 22.61 24.64 1.01 DWA-KD 20.16 22.36 0.30 Table 7: Efficiency measurements. *CDM uses the authors’ original implementation which does not support batch sizes > 1 >1 , hence the batch-size-1 comparison reflects its practical regime.

[163] h2: Appendix E Prompt for GPT-4.1 evaluation

[164] figure: Please act as an impartial judge and compare the quality of response A and response B provided by two AI assistants to the user question displayed below. Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of the response. Just tell me which response you think is better: - If A is significantly better than B, just answer me “A”; - If B is significantly better than A, just answer me “B”; - If A and B have similar quality (both good or both wrong), just answer me “Tied”. [Question] {question or instruction} [Response A] {response A} [Response B] {response B} Figure 4: Prompt for GPT-4.1 evaluation.

[165] h2: Instructions for reporting errors

[166] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[167] p: Tip: You can select the relevant text first, to include it in your report.

[168] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[169] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
