[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] p: Yanyi Li, Yimu Zhang, and Cong Fang

[3] h1: PRAC: Principal-Random Subspace for LLM Activation Compression and Memory-Efficient Training

[4] h6: Abstract

[5] p: Activations have become the primary memory bottleneck in large-batch LLM training. However, existing compression methods fail to exploit the spectral structure of activations, resulting in slow convergence or limited compression. To address this, we bridge the relationship between the algorithm’s fast convergence and the requirements for subspace projection, and show that an effective compression should yield an unbiased estimate of the original activation with low variance. We propose P rincipal- R andom Subspace for LLM A ctivation C ompression ( PRAC ), which novelly decomposes activations into two components: a principal subspace captured via SVD to retain dominant information, and a random subspace sampled from the orthogonal complement to approximate the tail. By introducing a precise scaling factor, we prove that PRAC yields an unbiased gradient estimator with minimum variance under certain conditions. Extensive experiments on pre-training and fine-tuning tasks demonstrate that PRAC achieves up to 36% total memory reduction with negligible performance degradation and minimal computational cost.

[6] h2: 1 Introduction

[7] p: Memory footprint has emerged as a critical bottleneck in the training of large language models (LLMs). During training, the memory overhead primarily consists of three components: model parameters (weights), optimizer states, and activations memory. The activations represent the intermediate outputs of each layer computed during the forward pass, which are typically retained to compute gradients in the subsequent backward propagation. In practice, a moderately large batch size generally promotes more stable training dynamics and improves GPU parallelism utilization, thereby accelerating convergence efficiently. However, a larger batch size substantially increases the activation memory footprint, turning it into the primary bottleneck and limiting both training efficiency and scalability. As illustrated in Figure 1 (Right), training a LLaMA-1B model (batch size 1 1 1 In this paper, “batch size” denotes the micro-batch size, representing the maximum number of samples processed during a single forward and backward pass on an individual GPU. of 128 and sequence length of 256) requires 94.5GB of memory, with model parameters 2.48GB, optimizer states and weight gradients 7.95GB for popular used ADAM algorithm ( Adam and others, 2014 ) , and activation 84.17GB, where activations account for a staggering 89% of the total usage.

[8] figure: Figure 1: The proposed PRAC projects activations onto both the principal and random subspaces and yields the minimum variance unbiased estimator, thus achieving up to 36% total memory reduction with negligible performance degradation. (Left) The flowchart of PRAC; (Middle) A conceptual comparison of subspace strategies; (Right) Performance comparison on LLaMA-1B.

[9] p: A straightforward approach to reducing activation memory is to modify the implementation of the training algorithm while preserving its underlying logic. For instance, gradient checkpointing ( Chen et al., 2016 ) selectively re-computes certain activations during the back-propagation phase, rather than storing them throughout the forward pass. This technique introduces additional computational overhead in the backward pass, thereby increasing overall training time.

[10] p: The other line of research focuses on reducing activation memory through novel algorithmic design. The core idea of such approaches is to iteratively optimize within a special chosen subspace of the model parameters.

[11] p: One representative example is zeroth-order optimization, which has attracted considerable attention in recent years, leading to multiple proposed variants ( Malladi et al., 2023 ; Gautam et al., 2024 ; Chen et al., 2024b ; Zhang et al., 2024a ; Zhao et al., 2024b ; Shu et al., 2025 ; Petrov et al., 2025 ) . From an algorithmic perspective, the algorithm per-step samples a random direction ξ \xi , typically drawn from a standard normal or uniform spherical distribution, and constructs a gradient estimator of the form 1 η ​ [ f ⁡ ( w + η ​ ξ ) − f ⁡ ( w ) ] ​ ξ \frac{1}{\eta}[f(w+\eta\xi)-f(w)]\xi , where w w denotes the model parameters and η \eta is a small positive constant. Intuitively, as η → 0 \eta\to 0 , this estimator approximates [ ξ ⊤ ∇ f ( W ) ] ξ [\xi^{\top}\nabla f(W)]\xi , which corresponds to performing an update only along the normalized direction ξ / ‖ ξ ‖ \xi/\|\xi\| , scaled by the directional derivative of the objective function. In implementation, such methods only require access to the final output of the forward pass, allowing intermediate activations to be released immediately. This substantially reduces the peak memory footprint during training. However, since these approaches typically update only a one-dimensional subspace per iteration, they converge much more slowly than first-order methods in practice and are generally not suitable for challenging tasks such as large-scale pre-training.

[12] p: To improve efficiency, some advanced methods incorporate architectural information to enable multi-dimensional subspace updates. For example, RSO (Random Subspace Optimization) introduced by Chen et al. (2025) in the outerloop uniformly samples subspaces and in the inner loop optimizes weights in the subspaces by inserting a low-dimensional trainable module. Activation memory is reduced because only the projected activations need to be stored—a principle inspired by LoRA ( Hu et al., 2022 ) and ReLoRA ( Lialin et al., 2023 ) . Despite these memory savings, this method still results in non-negligible performance degradation during pre-training, limiting its practical applicability.

[13] p: We emphasize that a central limitation of existing activation-efficient methods is their inability to leverage the spectral structure of activations, which ultimately compromises training effectiveness. In this paper, we directly focus on how to compress activations during training with minimal impact on convergence rate. Following Zhao et al. (2024a) ; He et al. (2024) ; Malladi et al. (2023) ; Gautam et al. (2024) , we still adopt a linear compression scheme: given a projection matrix P P , the activation matrix X X is compressed as X ​ P XP and reconstructed as X ​ P ​ P ⊤ XPP^{\top} .

[14] p: Our starting point is a standard stochastic optimization formulation, through which we bridge the relationship between the algorithm’s fast convergence and the requirements for subspace projection. We demonstrate that a well-chosen projection should yield an unbiased estimate of the original activation with low variance that ensures provable and efficient training convergence.

[15] p: To design an efficient estimator, we leverage the spectral structure of activations. We formalize widely observed “low-rank” phenomenon ( Hu et al., 2022 ; Zhao et al., 2024a ; Chen et al., 2024a ; Zhang et al., 2025 ) as the Activation Degenerate Condition , which assumes that the singular values of activations consist of a few dominant ones, followed by a long tail of smaller values whose cumulative energy (squared sum) is bounded.

[16] p: The primary contribution of this paper is the introduction of an activation compression technique, termed PRAC ( P rincipal- R andom Subspace for LLM A ctivation C ompression). We show this method is optimal in the sense that it achieves minimum variance among all unbiased estimators under the Activation Degenerate Condition. PRAC consists of two simple components: a principal subspace projection, which obtains a subspace projection matrix Q 1 Q_{1} via SVD, and a random subspace projection, where Q 2 Q_{2} is sampled uniformly from the orthogonal complement of Q 1 Q_{1} . Additionally, a key scaling factor k k is introduced to ensure the unbiasedness of the estimator.

[17] table: X ~ = ( X ​ P ) ​ P ⊤ = ( X ​ Q 1 ) ​ Q 1 ⊤ + k ⁡ ( X ​ Q 2 ) ​ Q 2 ⊤ . \tilde{X}=(XP)P^{\top}=(XQ_{1})Q_{1}^{\top}+k(XQ_{2})Q_{2}^{\top}.

[18] p: In implemtation for memory-efficient LLM training, PRAC employs a dynamic subspace update schedule that refreshes projection matrices at fixed intervals, thereby rendering the cost of SVD and QR decompositions negligible. The method further maximizes memory efficiency through subspace sharing and a layer-wise policy (see details in Section 5.1 ). We analyze the memory footprint and computational overhead of PRAC, demonstrating its efficiency in both aspects.

[19] p: We conduct extensive experiments on both pre-training and fine-tuning tasks. Our experiments demonstrate that PRAC matches or surpasses baselines across various tasks, achieving up to 36% memory saving while maintaining competitive performance.

[20] p: Our key contributions are summarized as follows:

[21] p: We propose PRAC, a novel activation compression method that effectively integrates principal and random subspace projections. PRAC is the first method to leverage the structural information of activations for memory-efficient pre-training. Theoretically, we prove that PRAC yields an unbiased estimator with minimum variance under the Activation Degeneration Condition.

[22] p: We demonstrate the practical efficacy of PRAC through extensive experiments on both pre-training and fine-tuning tasks. PRAC consistently achieves substantial memory reduction with negligible performance loss and very small computational overhead.

[23] h2: 2 Related Works

[24] p: Activation-Efficient Methods. To alleviate activation memory overhead, a technique modifying the checkpointing mechanism during backpropagation was proposed in Chen et al. (2016) . This approach has not only achieved widespread adoption but has also catalyzed subsequent research into modifications of the backpropagation algorithm itself ( Yang et al., 2024 ; Luo et al., 2025 ) .

[25] p: Furthermore, alternative approaches employ zeroth-order optimization to bypass backpropagation entirely ( Malladi et al., 2023 ; Gautam et al., 2024 ; Chen et al., 2024b ; Miles et al., 2024 ; Chen et al., 2025 ; Shamshoum et al., 2025 ; Petrov et al., 2025 ) , while others retain first-order methods but address the optimization problem within a low-dimensional subspace ( Chen et al., 2025 ) .

[26] p: Compression-based approaches ( Yang et al., 2024 ; Shamshoum et al., 2025 ; Miles et al., 2024 ) offer an alternative strategy by approximating intermediate variables. However, these methods are generally designed for specific sub-components of the model architecture. Furthermore, they fail to explicitly address how compression artifacts influence the convergence rate, limiting their potential in general-purpose compression for memory-efficient training.

[27] p: Optimization States-Efficient Methods. Considerable research aim to improve the memory efficiency for optimizer states. GaLore (Gradient Low-Rank Projection) and its variants ( Zhao et al., 2024a ; Liang et al., 2024 ; He et al., 2024 ) perform low-rank compression on gradients. To address the compression of momentum terms in the Adam optimizer, Adafactor ( Shazeer and Stern, 2018 ) utilizes factorization techniques to approximate the storage of the second moment. Adam-mini ( Zhang et al., 2024b ) designs a block-wise learning rate strategy based on the heterogeneity of the neural network’s Hessian matrix, reducing the memory footprint of the second moment. Fira ( Chen et al., 2024a ) and Apollo ( Zhu et al., 2025 ) utilize optimizer states to update adaptive learning rates. However, these algorithms do not modify the backpropagation process and thus cannot reduce the memory usage of activations, which is the dominant factor. Our method is orthogonal to this kind of method and can be combined with them for additional memory savings.

[28] h2: 3 Starting Point of Activation Compression

[29] h3: 3.1 Problem Formulation

[30] p: The training of Large Language Models (LLMs) can be formulated as the following stochastic optimization problem:

[31] table: min W ⁡ f ⁡ ( W ) ≔ 𝔼 ζ ​ [ F ⁡ ( W , ζ ) ] , \min_{W}f(W)\coloneqq\mathbb{E}_{\zeta}[F(W;\zeta)], (1)

[32] p: where W W denotes the model parameters and ζ \zeta represents the random data batch. We simply study the Stochastic Gradient Descent (SGD) ( Bottou, 2010 ) method, noting that the analysis extends naturally to other optimizers. The update of SGD goes as:

[33] table: W t + 1 = W t − η t ​ ∇ F ​ ( W t , ζ t ) ⏟ update term . W_{t+1}=W_{t}-\eta_{t}\underbrace{\nabla F(W_{t};\zeta_{t})}_{\text{update\;term}}. (2)

[34] p: To mitigate memory bottlenecks, various methods compress training artifacts (parameters, gradients, or activations). Consequently, the exact gradient is replaced by an approximate update term, denoted as G ~ ​ ( W t , ζ t ) \tilde{G}(W_{t};\zeta_{t}) , leading to the modified update rule:

[35] table: W t + 1 = W t − η t ​ G ~ ​ ( W t , ζ t ) . W_{t+1}=W_{t}-\eta_{t}\tilde{G}(W_{t};\zeta_{t}). (3)

[36] p: A fundamental question arises: What properties should the compression satisfy to guarantee fast convergence?

[37] p: To address this, we first examine the impact of systematic bias in the gradient estimator.

[38] h6: Proposition 1 (Non-convergence under Constant Bias) .

[39] p: Consider two-dimensional strongly convex problem: f ⁡ ( w ( 1 ) , w ( 2 ) ) = 𝔼 ξ ′ ​ ( w ( 1 ) − 3 ​ ξ ′ ) 2 + ( w ( 2 ) ) 2 f(w^{(1)},w^{(2)})=\mathbb{E}_{\xi^{\prime}}(w^{(1)}-3\xi^{\prime})^{2}+(w^{(2)})^{2} with ξ ′ \xi^{\prime} following a Bernoulli distribution. The parameters are initialized at w ( 1 ) = 0 , w ( 2 ) = 1 w^{(1)}=0,w^{(2)}=1 . At each step, only the first coordinate is updated by a stochastic gradient: G ~ = [ 2 ​ ( w ( 1 ) − 3 ​ ξ ′ ) , 0 ] ⊤ . \tilde{G}=[2(w^{(1)}-3\xi^{\prime}),0]^{\top}. Then for any { η t } \left\{\eta_{t}\right\} satisfies the Robbins-Monro condition: ∑ t = 0 ∞ η t = ∞ , ∑ t = 0 ∞ η t 2 < ∞ \sum_{t=0}^{\infty}\eta_{t}=\infty,\sum_{t=0}^{\infty}\eta_{t}^{2}<\infty , one has w t ( 2 ) = 1 w^{(2)}_{t}=1 for all t t . Consequently, ( w t ( 1 ) , w t ( 2 ) ) (w^{(1)}_{t},w^{(2)}_{t}) will never converge to an approximate stationary point.

[40] p: In the simple example above, the gradient estimator is biased by Θ ⁡ ( 1 ) \Theta(1) because w ( 2 ) w^{(2)} is never updated. It is interesting to observe that when | w ( 1 ) | < 2 |w^{(1)}|<2 , the magnitude of the stochastic gradient for w ( 1 ) w^{(1)} (i.e., 2 ​ | w ( 1 ) − 3 ​ ξ ′ | 2|w^{(1)}-3\xi^{\prime}| ) is always larger than that for w ( 2 ) w^{(2)} (i.e., 2 ​ | w ( 2 ) | 2|w^{(2)}| ). Consequently, even if w ( 1 ) w^{(1)} converges to its minimizer 0 0 , the maximum selection rule that consistently picks the coordinate with the largest gradient magnitude will never update w ( 2 ) w^{(2)} . It implies that principal methods, such as Galore ( Zhao et al., 2024a ) , may fail to converge in general stochastic optimization settings. Proposition 1 also establishes that a constant biased estimator cannot ensure convergence. We then consider unbiased estimator with non-negligible variance.

[41] h6: Proposition 2 (Convergence Rate with Bounded Gradient Variance, Ghadimi and Lan (2013) ) .

[42] p: Let the objective function f f is L-smooth and bounded below, and denote Δ = f ⁡ ( W 1 ) − inf f \Delta=f(W_{1})-\inf{f} . Assume that at each iteration t t we have access to an unbiased stochastic gradient G ~ ​ ( W t , ζ t ) \tilde{G}(W_{t},\zeta_{t}) satisfying 𝔼 ⁡ [ G ~ ​ ( W t , ζ t ) ∣ W t ] = ∇ f ​ ( W t ) , 𝔼 ⁡ [ ‖ G ~ ​ ( W t , ζ t ) − ∇ f ​ ( W t ) ‖ 2 ∣ W t ] ≤ σ 2 . \mathbb{E}[\tilde{G}(W_{t},\zeta_{t})\mid W_{t}]=\nabla f(W_{t}),\mathbb{E}[\|\tilde{G}(W_{t},\zeta_{t})-\nabla f(W_{t})\|^{2}\mid W_{t}]\leq\sigma^{2}. Consider the update rule in ( 3 ) with constant step sizes η t = min ⁡ { 1 L , 2 ​ Δ / L σ ​ N } \eta_{t}=\min\left\{\frac{1}{L},\frac{\sqrt{2\Delta/L}}{\sigma\sqrt{N}}\right\} and then randomly selects an output W R W_{R} from { W 1 , ⋯ , W T } \{W_{1},\cdots,W_{T}\} according to the certain probability mass function. Then the following bound holds:

[43] table: 𝔼 ⁡ [ ‖ ∇ f ​ ( W R ) ‖ 2 ] ≤ 2 ​ L ​ Δ T + 2 ​ 2 ​ L ​ Δ T ​ σ . \mathbb{E}[\|\nabla f(W_{R})\|^{2}]\leq\frac{2L\Delta}{T}+2\sqrt{\frac{2L\Delta}{T}}\sigma.

[44] p: Proposition 2 is a standard result in non-convex optimization ( Nesterov, 2013 ; Ghadimi and Lan, 2013 ) . It demonstrates that unbiased compression ensures convergence. Moreover, the convergence rate is hindered by the variance σ 2 \sigma^{2} . Therefore, an effective compression should yield a gradient estimator that is both unbiased and low-variance .

[45] p: Since activations dominate memory usage in LLM training, we translate the gradient-level requirements established above into concrete criteria for activation compression.

[46] h3: 3.2 Criteria for Activation Compression

[47] p: The theoretical constraints established in Section 3.1 for general gradients directly inform the design of activation compression. For a linear layer, such as the Query layer in the attention block, the quality of the activation reconstruction dictates the quality of the gradient estimate.

[48] h6: Lemma 3 .

[49] p: Consider a linear layer with forward pass Y = X ​ W Y=XW . Let X ~ \tilde{X} be a compressed estimator of the activation X X . If X ~ \tilde{X} is unbiased ( 𝔼 ⁡ [ X ~ ] = X \mathbb{E}[\tilde{X}]=X ) with bounded variance 𝔼 ⁡ [ ‖ X ~ − X ‖ F 2 ] ≤ σ 2 \mathbb{E}[\|\tilde{X}-X\|_{F}^{2}]\leq\sigma^{2} , then the resulting gradient estimator G ~ = X ~ ⊤ ​ ( ∇ Y L ) \tilde{G}=\tilde{X}^{\top}(\nabla_{Y}L) satisfies:

[50] p: Unbiasedness: The gradient estimator is unbiased with respect to the true gradient:

[51] table: 𝔼 ⁡ [ G ~ ] = 𝔼 ⁡ [ X ~ ⊤ ] ​ ( ∇ Y L ) = ∇ W L . \mathbb{E}[\tilde{G}]=\mathbb{E}[\tilde{X}^{\top}](\nabla_{Y}L)=\nabla_{W}L.

[52] p: Bounded Variance: The gradient variance is bounded by the activation variance and the upstream gradient norm:

[53] table: 𝔼 ⁡ [ ‖ G ~ − ∇ W L ‖ F 2 ] ≤ σ 2 ​ ‖ ∇ Y L ‖ 2 2 . \mathbb{E}[\|\tilde{G}-\nabla_{W}L\|_{F}^{2}]\leq\sigma^{2}\|\nabla_{Y}L\|_{2}^{2}.

[54] p: Lemma 3 shows that constructing an unbiased and low-variance approximation of activations suffices to satisfy the convergence guarantees in Propositions 1 and 2 .

[55] p: Following Zhao et al. (2024a) ; He et al. (2024) ; Malladi et al. (2023) ; Gautam et al. (2024) , we adopt a subspace projection approach. Let P ∈ ℝ n × r P\in\mathbb{R}^{n\times r} be a projection matrix, and the activation X X is compressed to a lower-dimensional representation X ​ P XP and reconstructed as X ~ = ( X ​ P ) ​ P ⊤ \tilde{X}=(XP)P^{\top} . The central challenge, therefore, lies in designing the projection matrix P P such that the reconstruction X ~ \tilde{X} minimizes variance while maintaining unbiasedness, specifically tailored to the spectral structure of the activations.

[56] h2: 4 Proposed Method: PRAC

[57] p: In this section, we introduce PRAC, a hybrid framework motivated by the spectral structure of activations. By integrating the principal and random subspaces to address their respective limitations, we balance the bias-variance trade-off. Finally, we prove that PRAC yields the minimum variance unbiased estimator under certain conditions.

[58] h3: 4.1 Spectral Analysis of Activations

[59] figure: Figure 2: Singular value spectrum (Left) and cumulative energy ratio (Right).

[60] p: To design an effective projection matrix P P in Section 3.2 , we analyze the spectral structure of activations using the 10th layer of LLaMA-130M (at 10% training progress) as an example.

[61] p: As shown in Figure 2 , the spectrum exhibits two distinct characteristics: a few dominant singular values capture the majority of the spectral energy; and the remaining singular values form a long tail that decays slowly.

[62] p: Note the “low-rank” structure is commonly observed in weight matrices ( Hu et al., 2022 ; Lialin et al., 2023 ) . We study activation matrix and emphasize that the long-tail directions cannot be ignored—truncating them significantly slows down convergence ( Chen et al., 2024a ; Zhang et al., 2025 ) . We introduce the term degenerate condition to characterize this observed phenomenon.

[63] p: [Activation Degenerate Condition] For activation matrix X X , let σ i \sigma_{i} be the i i -th largest singular value of the activations. We say X X satifies the ( s , q ) (s,q) -degenerate condition ( X ∼ ( s , q ) − D X\sim(s,q)-D in short) if it admits: ∑ s + 1 n σ i 2 ≤ q \sum_{s+1}^{n}\sigma_{i}^{2}\leq q . This assumption posits that only the top s s singular values of the activation matrix are large. Since the remaining singular values are typically small and roughly equal in practice, we bound the rest squared sum (same as the square of the Frobenius norm for the rest matrix) by a constant q q .

[64] p: Based on Assumption 4.1 , we can conduct a theoretical analysis of the optimal design of the projection matrix P P (see Section 4.3 ). Before that, let us first introduce two key components of PRAC, which are also subspace projection methods.

[65] h3: 4.2 Key Components of PRAC

[66] p: Intuitively, one might consider two natural approaches to activation compression: projecting onto the principal subspace of the activations, or onto a random subspace. However, both have inherent drawbacks that our method addresses.

[67] p: Principal Subspace for Activation Compression (PAC). PAC retains the significant information by projecting activations onto their principal subspaces. Let the Singular Value Decomposition (SVD) of the activation matrix be X = U ​ Σ ​ V ⊤ = ∑ i = 1 n s i ​ u i ​ v i ⊤ X=U\Sigma V^{\top}=\sum_{i=1}^{n}s_{i}u_{i}v_{i}^{\top} . We define the projection matrix Q 1 = [ v 1 ( 1 ) , ⋯ , v r 1 ( 1 ) ] ∈ ℝ n × r 1 Q_{1}=\left[v_{1}^{(1)},\cdots,v_{r_{1}}^{(1)}\right]\in\mathbb{R}^{n\times r_{1}} using the top- r 1 r_{1} right singular vectors. Then X ​ Q 1 XQ_{1} captures the rank- r 1 r_{1} principal information. For the rank r 1 < n r_{1}<n , PAC introduces a systematic reconstruction bias Δ = ‖ X − X ​ Q 1 ​ Q 1 ⊤ ‖ F 2 = ∑ i = r 1 + 1 n σ i 2 > 0 \Delta=\|X-XQ_{1}Q_{1}^{\top}\|_{F}^{2}=\sum_{i=r_{1}+1}^{n}\sigma_{i}^{2}>0 . As discussed in Section 3.2 , this bias can lead to non-convergence in the optimization problem ( 1 ).

[68] p: Random Subspace for Activation Compression (RAC). To avoid bias, RAC projects activations onto a random subspace sampled uniformly from the Stiefel manifold St n , r 2 \mathrm{St}_{n,r_{2}} , defined as St n , r = { P ∈ ℝ n × r | P ⊤ ​ P = I r } \mathrm{St}_{n,r}=\left\{P\in\mathbb{R}^{n\times r}|P^{\top}P=I_{r}\right\} . The construction proceeds as follows: First, we generate a random matrix S ∈ ℝ n × r 2 S\in\mathbb{R}^{n\times r_{2}} with entries S i ​ j ∼ 𝒩 ⁡ ( 0 , 1 ) S_{ij}\sim\mathcal{N}(0,1) . We then perform QR decomposition on S S to obtain an orthogonal basis Q 2 ∈ ℝ n × r 2 Q_{2}\in\mathbb{R}^{n\times r_{2}} , such that Q 2 ⊤ ​ Q 2 = I Q_{2}^{\top}Q_{2}=I .

[69] p: While RAC can provide an unbiased estimator of the activation (via setting a scaling factor), the inherent randomness introduces high variance: 𝔼 ​ ‖ X ~ rac − X ‖ F 2 ≤ ( n r 2 − 1 ) ​ ( ∑ i = 1 s σ i 2 + q ) \mathbb{E}\|\tilde{X}_{\text{rac}}-X\|_{F}^{2}\leq(\frac{n}{r_{2}}-1)\left(\sum_{i=1}^{s}\sigma_{i}^{2}+q\right) due to the top singular values. (see Theorem 13 and 15 in Appendix C.2 ). This high variance destabilizes the training process and slows convergence.

[70] h3: 4.3 Optimal Design via Hybrid Projection

[71] p: We now establish the lower bound variance to estimate the activations. Specifically, for any activation X X , we consider the random subspace projection method where the projection matrix P ∈ ℝ n × r P\in\mathbb{R}^{n\times r} is drawn from a distribution ℙ X \mathbb{P}_{X} , which must satisfy the unbiasedness condition (i.e. 𝔼 P ∼ ℙ X ​ [ X ​ P ​ P ⊤ ] = X \mathbb{E}_{P\sim\mathbb{P}_{X}}[XPP^{\top}]=X ) and depend on X X , then the lower bound variance can be written as

[72] table: sup X ∼ ( s , q ) − D ( inf P ∼ ℙ X , 𝔼 ℙ X ​ [ X ​ P ​ P ⊤ ] = X 𝔼 ℙ X ​ ‖ X ​ P ​ P ⊤ − X ‖ F 2 ) . \sup_{X\sim(s,q)-D}\left(\inf_{\begin{subarray}{c}P\sim\mathbb{P}_{X},\\ \mathbb{E}_{\mathbb{P}_{X}}[XPP^{\top}]=X\end{subarray}}\mathbb{E}_{\mathbb{P}_{X}}\|XPP^{\top}-X\|_{F}^{2}\right). (4)

[73] p: For this min-max optimization problem, if the small singular values of X X exhibit non-uniformity, P P can be tailored to exploit this structure. Intuitively, a distribution where X X possesses approximately uniform tail singular values represents a relatively worst-case scenario. The following lemma gives the lower bound explicity.

[74] h6: Lemma 4 (Lower Bound) .

[75] p: Under Assumption 4.1 , when s < r < n s<r<n , we have ( 4 ) ≥ ( n − s r − s − 1 ) ​ q \eqref{eq:lower bound}\geq(\frac{n-s}{r-s}-1)q .

[76] p: We now propose our method and demonstrate that its variance achieves the lower bound in Lemma 4 , thereby demonstraining its optimality in attaining the minimum variance.

[77] p: Construction of the Projection Matrix. We first extract the principal basis vectors v i ( 1 ) ​ ( i ∈ [ 1 , r 1 ] ) v_{i}^{(1)}(i\in[1,r_{1}]) via SVD, and let the projection matrix Q 1 = [ v 1 ( 1 ) , ⋯ , v r 1 ( 1 ) ] Q_{1}=\left[v_{1}^{(1)},\cdots,v_{r_{1}}^{(1)}\right] . Then we sample a random matrix whose columns lie in the orthogonal complement of the column space of Q 1 Q_{1} :

[78] table: S o = ( I − Q 1 ​ Q 1 ⊤ ) ​ S , where ​ S i ​ j ∼ i . i . d 𝒩 ⁡ ( 0 , 1 ) . S_{o}=(I-Q_{1}Q_{1}^{\top})S,\quad\text{where}\;S_{ij}\stackrel{{\scriptstyle i.i.d}}{{\sim}}\mathcal{N}(0,1). (5)

[79] p: Let v j ( 2 ) ​ ( j ∈ [ 1 , r 2 ] ) v_{j}^{(2)}(j\in[1,r_{2}]) be the column vectors obtained from QR ⁡ ( S o ) \mathrm{QR}(S_{o}) . By construction, the principal and random subspaces are orthogonal ( v i ( 1 ) ⟂ v j ( 2 ) v_{i}^{(1)}\perp v_{j}^{(2)} ). The unified projection matrix P ∈ ℝ n × ( r 1 + r 2 ) P\in\mathbb{R}^{n\times(r_{1}+r_{2})} is defined as:

[80] table: P = [ v 1 ( 1 ) , ⋯ , v r 1 ( 1 ) ⏟ Principal , k ​ v 1 ( 2 ) , ⋯ , k ​ v r 2 ( 2 ) ⏟ Random ] , P=\left[\underbrace{v_{1}^{(1)},\cdots,v_{r_{1}}^{(1)}}_{\mathrm{Principal}},\underbrace{\sqrt{k}v_{1}^{(2)},\cdots,\sqrt{k}v_{r_{2}}^{(2)}}_{\mathrm{Random}}\right], (6)

[81] p: where k k is a scaling factor used to ensure unbiased reconstruction. It’s critical, since we only sample a subspace of dimension r 2 r_{2} to represent the entire tail of dimension n − r 1 n-r_{1} , the energy of the random component must be amplified to ensure the estimator remains unbiased in expectation.

[82] p: Unbiased Estimation. By selecting an appropriate k k , PRAC ensures the unbiasedness.

[83] h6: Theorem 5 (Unbiased Reconstruction of PRAC) .

[84] p: Let P P be the projection matrix defined in ( 6 ). If the scaling factor is set to k = n − r 1 r 2 k=\frac{n-r_{1}}{r_{2}} , the reconstruction X ~ = X ​ P ​ P ⊤ \tilde{X}=XPP^{\top} satisfies 𝔼 ⁡ [ X ~ ] = X \mathbb{E}[\tilde{X}]=X .

[85] p: Variance Reduction Analysis. A key advantage of PRAC is its ability to achieve the minimum variance.

[86] h6: Theorem 6 (Variance Bound of PRAC) .

[87] p: For X X admiting ( s , q ) (s,q) -D condition with s < r < n s<r<n , by choosing r 1 = s r_{1}=s and r 2 = r − r 1 r_{2}=r-r_{1} , we have:

[88] table: 𝔼 ⁡ [ ‖ X ​ P ​ P ⊤ − X ‖ F 2 ] ≤ ( n − r 1 r 2 − 1 ) ​ q . \mathbb{E}\bigl[\|XPP^{\top}-X\|_{F}^{2}\bigr]\leq(\frac{n-r_{1}}{r_{2}}-1)q.

[89] p: Theorem 5 confirms that setting k = n − r 1 r 2 k=\frac{n-r_{1}}{r_{2}} yields an unbiased reconstruction of activations and, by extension, gradients (Lemma 3 ). Theorem 6 demonstrates its optimality in the sense that it achieves the minimum variance among all unbiased estimators under the degenerate condition. Ablation study in Section 6.3 empirically validates this theoretical finding. A comparison of the three projection methods is presented in Table 1 .

[90] h2: 5 PRAC for Memory-Efficient Training

[91] p: In this section, we detail the practical implementation of PRAC for memory-efficient LLM training. We introduce dynamic and sharing strategy to minimize computational overhead. Furthermore, we present a layer-wise adaptation scheme tailored to the distinct sensitivity of different model components. Finally, we provide a complexity analysis of PRAC, focusing on activation memory reduction and the amortized computational cost.

[92] figure: Table 1: Comparison of Estimation Unbiasedness and Variance across Projection Methods. Algorithm Form Scaling Unbiasedness Variance PAC X ~ pac = ( X ​ Q 1 ) ​ Q 1 ⊤ \tilde{X}_{\text{pac}}=(XQ_{1})Q_{1}^{\top} - × \times - RAC X ~ rac = ( X ​ Q 2 ) ​ Q 2 ⊤ \tilde{X}_{\text{rac}}=(XQ_{2})Q_{2}^{\top} n / r 2 n/r_{2} ✓ \checkmark High PRAC X ~ prac = ( X ​ P ) ​ P ⊤ \tilde{X}_{\text{prac}}=(XP)P^{\top} ( n − r 1 ) / r 2 (n-r_{1})/r_{2} ✓ \checkmark Minimum

[93] h3: 5.1 PRAC for LLM Training

[94] p: Dynamic Subspace Update. Recall that the PRAC reconstruction can be written as:

[95] table: X ​ P ​ P ⊤ \displaystyle XPP^{\top} = X ⁡ [ ∑ i = 1 r 1 v i ( 1 ) ​ ( v i ( 1 ) ) ⊤ + k ​ ∑ i = 1 r 2 v i ( 2 ) ​ ( v i ( 2 ) ) ⊤ ] = X ​ Q 1 ​ Q 1 ⊤ + k ​ X ​ Q 2 ​ Q 2 ⊤ , \displaystyle=X\left[\sum_{i=1}^{r_{1}}v_{i}^{(1)}(v_{i}^{(1)})^{\top}+k\sum_{i=1}^{r_{2}}v_{i}^{(2)}(v_{i}^{(2)})^{\top}\right]=XQ_{1}Q_{1}^{\top}+kXQ_{2}Q_{2}^{\top}, (7)

[96] p: where Q 1 = [ v 1 ( 1 ) , ⋯ , v r 1 ( 1 ) ] , Q 2 = [ v 1 ( 2 ) , ⋯ , v r 2 ( 2 ) ] Q_{1}=[v_{1}^{(1)},\cdots,v_{r_{1}}^{(1)}],Q_{2}=[v_{1}^{(2)},\cdots,v_{r_{2}}^{(2)}] are the principal and random projection matrices respectively.

[97] p: Computing the exact principal subspace (via SVD) and generating orthogonal random projections (via QR) at every step incurs significant computational cost. To mitigate this, we employ a lazy update strategy. The principal and random components Q 1 , Q 2 Q_{1},Q_{2} are updated only at fixed intervals T 1 T_{1} and T 2 T_{2} , respectively. The rationale is that the activation statistics (and thus the related subspace) change slowly over training steps, especially after the initial warm-up phase. This lazy update mechanism drastically reduces the amortized computational overhead. The full procedure is outlined in Algorithm 1 .

[98] p: Subspace Sharing. In Transformer architectures, many layers share the same input activation X X such as the Query, Key and Value projections. To cut memory usage, we enforce subspace sharing: a single set of projection matrices ( Q 1 , Q 2 Q_{1},Q_{2} ) and compressed activations ( X ​ Q 1 , X ​ Q 2 XQ_{1},XQ_{2} ) is computed and shared across these layers. Beyond memory savings, this strategy ensures that gradient updates for parallel heads reside in a consistent subspace, reducing gradient noise variance and stabilizing optimization.

[99] figure: Algorithm 1 Dynamic Activation Compression via PRAC 0: Input activation X X , ranks ( r 1 , r 2 ) (r_{1},r_{2}) , update intervals ( T 1 , T 2 ) (T_{1},T_{2}) , current step t t 0: Projection matrices Q 1 ( t ) Q_{1}^{(t)} , Q 2 ( t ) Q_{2}^{(t)} , Compressed Activations X 1 ( t ) X_{1}^{(t)} , X 2 ( t ) X_{2}^{(t)} 1: k ← ( n − r 1 ) / r 2 k\leftarrow(n-r_{1})/r_{2} 2: // Update Principal Subspace: 3: if t mod T 1 = 0 t\bmod T_{1}=0 then 4: Q 1 ( t ) ← top- ​ r 1 ​ right singular vectors of ​ X Q_{1}^{(t)}\leftarrow\text{top-}r_{1}\text{ right singular vectors of }X 5: else 6: Q 1 ( t ) ← Q 1 ( t − 1 ) Q_{1}^{(t)}\leftarrow Q_{1}^{(t-1)} 7: end if 8: // Update Random Subspace 9: if t mod T 2 = 0 t\bmod T_{2}=0 then 10: Sample S ∼ 𝒩 ⁡ ( 0 , I n × r 2 ) S\sim\mathcal{N}(0,I_{n\times r_{2}}) 11: Q 2 ( t ) ← orthonormal basis of ​ ( I − Q 1 ( t ) ​ Q 1 ( t ) ⊤ ) ​ S Q_{2}^{(t)}\leftarrow\text{orthonormal basis of }(I-Q_{1}^{(t)}Q_{1}^{(t)\top})S 12: else 13: Q 2 ( t ) ← Q 2 ( t − 1 ) Q_{2}^{(t)}\leftarrow Q_{2}^{(t-1)} 14: end if 15: // Compression 16: X 1 ( t ) ← X ​ Q 1 ( t ) X_{1}^{(t)}\leftarrow XQ_{1}^{(t)} , X 2 ( t ) ← k ⋅ X ​ Q 2 ( t ) X_{2}^{(t)}\leftarrow k\cdot XQ_{2}^{(t)} 17: Return: Q 1 ( t ) , Q 2 ( t ) , X 1 ( t ) , X 2 ( t ) Q_{1}^{(t)},Q_{2}^{(t)},X_{1}^{(t)},X_{2}^{(t)}

[100] p: Layer-Wise Design. Building on the periodic update strategy, we further tailor the compression to the specific roles of different layer types, as not all layers contribute equally to training dynamics. To this end, we adopt a layer-wise configuration tailored to the specific characteristics of linear and non-linear modules:

[101] p: Linear Layers (MLP, Attention Projections): Due to their large parameter scale, the updates of their weight matrices impose a higher demand on gradient quality. Therefore, more activation information needs to be retained to ensure optimization performance. During compression, we allocate a relatively higher rank to these layers (e.g., r 1 = r 2 = ⌊ 0.3 ​ n ⌋ r_{1}=r_{2}=\lfloor 0.3n\rfloor ).

[102] p: Non-linear Layers (LayerNorm, RMSNorm, GeLU, SiLU): These layers typically involve element-wise operations or vector-wise scaling parameters, resulting in lower information density. Although our theoretical analysis does not directly cover all cases, we find that our method remains effective for most layers. It is worth noting that certain intermediate variables in these layers, such as the mean and variance in LayerNorm, are not compressed due to their negligible memory footprint (e.g., b ​ s bs vs. b ​ s ​ n bsn ). Likewise, operations like Flash Attention are excluded from PRAC compression because of their intricate coupled structure and engineering optimizations. In practice, we process all the selected non-linear layers using a lower rank ( r 1 = r 2 = ⌊ 0.2 ​ n ⌋ r_{1}=r_{2}=\lfloor 0.2n\rfloor ).

[103] figure: Table 2: Comparison with memory-efficient algorithms on pretraining tasks. Validation perplexity (PPL, lower is better) and peak memory consumption (MEM, in GB, lower is better) are reported. For methods marked out-of-memory (OOM), perplexity is measured using half the batch size specified above. B , S , Δ B,S,\Delta denote the micro-batch size, sequence length and total memory reduction respectively. LLaMA-130M LLaMA-350M LLaMA-1B GPT-2-124M GPT-2-355M Method PPL MEM Δ \Delta PPL MEM Δ \Delta PPL MEM Δ \Delta PPL MEM Δ \Delta PPL MEM Δ \Delta Baseline 24.41 21.26 - 18.77 46.10 - 15.33 OOM 19.83 62.27 - 16.26 55.94 - GaLore 25.12 21.08 -1% 19.65 45.37 -2% 15.64 OOM 21.01 62.15 -0% 17.88 55.64 -1% RSO 25.41 19.57 -8% 19.57 40.36 -13% 15.72 79.32 -16% 22.31 54.79 -12% 18.29 46.90 -16% PRAC 24.66 15.65 -27% 18.92 32.21 -30% 15.41 60.48 -36% 19.95 49.68 -20% 16.35 44.21 -21% B / S 128/256 128/256 128/256 64/1024 32/1024

[104] h3: 5.2 Memory and Computational Efficiency

[105] figure: Table 3: Activation memory footprint comparison for the GELU and linear layer. Baseline PRAC GeLU Input b ​ s ​ n bsn b ​ s ​ ( r 1 + r 2 ) bs(r_{1}+r_{2}) W down ​ Input W_{\text{down}}\;\text{Input} b ​ s ​ n bsn b ​ s ​ ( r 1 + r 2 ) bs(r_{1}+r_{2}) Total 2 ​ b ​ s ​ n 2bsn 2 ​ b ​ s ​ ( r 1 + r 2 ) 2bs(r_{1}+r_{2})

[106] p: Theoretical Memory Footprint. We analyze memory usage in the GeLU layer A u = GeLU ​ ( A u ′ ) A_{u}=\text{GeLU}(A_{u}^{\prime}) and linear layer A d ′ = A u ​ W down ⊤ A_{d}^{\prime}=A_{u}W_{\text{down}}^{\top} . Standard backpropagation requires storing full tensors A u , A u ′ ∈ ℝ b ⋅ s × n A_{u},A_{u}^{\prime}\in\mathbb{R}^{b\cdot s\times n} , costing 2 ​ b ​ s ​ n 2bsn . In contrast, PRAC projects these activations onto principal ( r 1 r_{1} ) and random ( r 2 r_{2} ) subspaces, caching only the low-dimensional projections in ℝ b ⋅ s × ( r 1 + r 2 ) \mathbb{R}^{b\cdot s\times(r_{1}+r_{2})} . In particular, since P u , P u ′ P_{u},P_{u}^{\prime} are independent of the batch size, their memory overhead is negligible. The memory usage is summarized in Table 3 .

[107] p: In the experiments, r 1 + r 2 r_{1}+r_{2} is typically set to less than ⌊ 0.6 ​ n ⌋ \lfloor 0.6n\rfloor , which results in over 40% reduction in the activations. The complete analysis for the full GPT architecture is provided in Appendix B .

[108] p: Computational Overhead. The primary computational cost of PRAC arises from SVD and QR decompositions. However, by setting the update intervals T 1 T_{1} and T 2 T_{2} to sufficiently large values (e.g., T 1 = T 2 = 500 T_{1}=T_{2}=500 steps), the amortized cost becomes negligible. Furthermore, the additional matrix multiplications introduced by the projection operation X ​ P XP incur minimal overhead compared to the memory throughput gains. The experimental results of training efficiency are shown in Section 6.1 .

[109] h2: 6 Experiments

[110] p: In this section, we extensively evaluate PRAC on both pre-training and fine-tuning tasks across various model architectures. PRAC consistently achieves up to 36% memory reduction while maintaining competitive performance.

[111] h3: 6.1 Memory-Efficient Pre-training

[112] p: Setup. We evaluate PRAC by pre-training LLaMA ( Touvron et al., 2023 ) models (130M, 350M, 1B parameters) on the C4 dataset ( Raffel et al., 2020 ) and GPT-2 ( Brown et al., 2020 ) models (124M, 355M) on OpenWebText ( Gokaslan et al., 2019 ) , following the standard configurations in the nanoGPT codebase 2 2 2 https://github.com/karpathy/nanoGPT . For PRAC, we configure the subspace ranks as r 1 = r 2 = ⌊ 0.3 ​ n ⌋ r_{1}=r_{2}=\lfloor 0.3n\rfloor for linear layers and r 1 = r 2 = ⌊ 0.2 ​ n ⌋ r_{1}=r_{2}=\lfloor 0.2n\rfloor for non-linear layers (e.g., RMSNorm, SiLU), where n n is the hidden dimension. We compare against two memory-efficient baselines: GaLore ( Zhao et al., 2024a ) and RSO ( Chen et al., 2025 ) , using their reported hyperparameters. Detailed configurations are provided in Appendix D.1 . To ensure statistical robustness, all experiments are conducted over multiple runs with different random seeds, and we report the averaged results.

[113] figure: (a) LLaMA 130M (b) LLaMA 350M Figure 3: Loss curves of pre-training LLaMA-130M and LLaMA-350M model.

[114] p: Results. Table 2 summarizes the quantitative results. PRAC achieves the optimal trade-off between training performance and memory usage, achieving a 36% total memory reduction for the LLaMA-1B model. Figure 3 illustrates the validation loss trajectories. PRAC maintains competitive convergence throughout the entire training process. In contrast, GaLore (Principal-only) suffers from stagnation in the later stages due to bias, while RSO (Random-only) exhibits slower initial convergence due to high variance. In the GPT-2 experiments, we restrict the batch size to avoid OOM failures in the comparison methods; under these conditions, our method achieves 20 × \times and 21 × \times total memory compression for GPT-124M and 355M respectively.

[115] figure: Table 4: Training Time Comparison on 4 × 4\times A800 GPU for LLaMA-1B. Method Batch Size Memory (GB) Training Time (h) Baseline 64 50.35 156 PRAC 64 36.90 179 96 ( ↑ 𝟓𝟎 % \bf{\uparrow 50\%} ) 48.70 117 ( ↓ 𝟐𝟓 % \bf{\downarrow 25\%} )

[116] p: Training Efficiency. To verify the practical speedup of PRAC, we measure training time and peak memory on LLaMA-1B using 4×A800 GPUs. As shown in Table 4 , PRAC reduces peak memory by approximately 27% at a fixed batch size of 64 (to prevent OOM for the baseline). Crucially, this memory headroom allows for a larger batch size (increasing from 64 to 96), which reduces the total training time by 25%.

[117] p: Scaling Laws. We validate the scalability of PRAC by training a LLaMA series ranging from 35M to 1B parameters. Following Chinchilla’s law ( Hoffmann et al., 2022 ) , we set the token budget to 20 × 20\times the parameter count. Figure 4 (a) shows that PRAC tracks the AdamW baseline loss curves almost identically across all scales while using around 30% less memory. The linear fit in Figure 4 (b) confirms that PRAC adheres to the power-law scaling relationship, suggesting robust performance for even larger models.

[118] figure: (a) Scaling laws in terms of compute (b) Scaling laws in terms of parameters Figure 4: Scaling behavior of PRAC across model sizes (35M to 1B parameters)

[119] figure: Table 5: Comparison with memory-efficient algorithms on fine-tuning RoBERTa models. Average scores across the GLUE benchmark and the peak memory usage of activations in MRPC task are provided. Method Memory (GB) COLA STSB MRPC RTE SST2 MNLI QNLI QQP AVG Full Fine-Tuning 0.42 62.24 90.92 91.30 79.42 94.57 87.18 92.33 92.28 86.28 RSO (rank=4) 0.29 62.47 90.62 92.25 78.70 94.84 86.67 92.29 90.94 86.10 PRAC (rank=4) 0.26 ( ↓ 𝟑𝟖 % \bf{\downarrow 38\%} ) 63.56 90.83 93.28 78.71 94.72 86.60 92.35 90.95 86.38

[120] h3: 6.2 Memory-Efficient Fine-tuning

[121] p: We evaluate PRAC on the GLUE benchmark ( Wang et al., 2018 ) by fine-tuning RoBERTa ( Liu et al., 2019 ) . For a fair comparison with RSO (rank r = 4 r=4 ), we set r 1 = r 2 = 2 r_{1}=r_{2}=2 for PRAC. As shown in Table 5 , PRAC not only outperforms the RSO baseline but, in certain tasks, surpasses full fine-tuning. This suggests that the random subspace component may act as a beneficial regularizer during fine-tuning by introducing stochasticity.

[122] h3: 6.3 Ablation Study

[123] figure: (a) LLaMA 60M (b) LLaMA 130M Figure 5: Loss curve of using PRAC, PAC, RAC in LLaMA series pre-training. RAC reports the result of r = 0.6 r=0.6 due to the divergence of r = 0.3 r=0.3 .

[124] p: We assess the efficacy of the hybrid projection by comparing PAC, RAC, and PRAC with equivalent total rank (using r 1 + r 2 r_{1}+r_{2} for PRAC). As shown in Figure 5 , PAC converges slowly in the later stages, where gradient noise dominates the true gradient (Proposition 1 ). In contrast, RAC struggles in the early stages due to its inability to capture principal subspace properties. PRAC overcomes these limitations, achieving faster convergence throughout the entire training process and validating the advantage of combining dual subspaces.

[125] p: Appendix D.3 details the ablation analysis for the scaling factor. Results indicate that the theoretical setting k = n − r 1 r 2 k=\frac{n-r_{1}}{r_{2}} is effective across both linear and non-linear layers.

[126] h2: 7 Conclusion

[127] p: In this work, we propose PRAC, a theoretically optimal activation compression strategy that provides unbiased estimates and leverages the low-rank structure of LLM activations to minimize estimation variance. Unlike prior subspace methods, PRAC ensures stable convergence while reducing total memory by up to 36% across both pre-training and fine-tuning tasks. With negligible computational overhead, PRAC offers a robust and scalable solution for training large language models on memory-constrained hardware.

[128] h2: Impact Statement

[129] p: This paper presents a method to substantially improve the memory and computational efficiency of LLM training. By compressing activations via principal and random subspaces, our approach reduces the hardware requirements for pre-training and fine-tuning, thereby minimizing the energy consumption and carbon emissions associated with large-scale deep learning workloads.

[130] h2: References

[131] h2: Appendix A Implementation of PRAC

[132] p: We present the PRAC method for compressing activations in Algorithm 1 , and introduce its application during forward and backward propagation in Algorithm 2 .

[133] figure: Algorithm 2 Activation Storage and Recovery for Backpropagation 0: Input X X , parameters W W , forward function f f , ranks ( r 1 r_{1} , r 2 r_{2} ), step intervals ( T 1 T_{1} , T 2 T_{2} ), current training step t t 1: Forward Propagation: 2: Compute output: Y ← f ⁡ ( X , W ) Y\leftarrow f(X;W) 3: Store compression components: { Q 1 ( t ) , Q 2 ( t ) , 𝒳 1 ( t ) , 𝒳 2 ( t ) } ← 𝒞 ⁡ ( X , r 1 , r 2 , T 1 , T 2 , t ) \{Q_{1}^{(t)},Q_{2}^{(t)},\mathcal{X}_{1}^{(t)},\mathcal{X}_{2}^{(t)}\}\leftarrow\mathcal{C}(X,r_{1},r_{2},T_{1},T_{2},t) (Algorithm 1 ) 4: Return: Y Y 5: 6: Backward Propagation: 7: Receive gradient w.r.t output: ∇ Y ℒ ← ∂ ℒ ∂ Y \nabla_{Y}\mathcal{L}\leftarrow\frac{\partial\mathcal{L}}{\partial Y} 8: Reconstruct input approximation from cache: X ~ ← 𝒳 1 ( t ) ​ Q 1 ( t ) + 𝒳 2 ( t ) ​ Q 2 ( t ) \tilde{X}\leftarrow\mathcal{X}_{1}^{(t)}Q_{1}^{(t)}+\mathcal{X}_{2}^{(t)}Q_{2}^{(t)} 9: Compute parameter and input gradients: ∇ X ℒ , ∇ W ℒ ← backward ​ ( ∇ Y ℒ , X ~ , W ) \nabla_{X}\mathcal{L},\nabla_{W}\mathcal{L}\leftarrow\text{backward}(\nabla_{Y}\mathcal{L},\tilde{X},W) 10: Return: ∇ W ℒ , ∇ X ℒ \nabla_{W}\mathcal{L},\nabla_{X}\mathcal{L}

[134] h2: Appendix B Memory Complexity Analysis

[135] p: We take GPT structure as an example to show theoretical activation memory of PRAC. We assume a uniform rank ratio r 1 , r 2 ≥ 0 r_{1},r_{2}\geq 0 for the principal and random subspaces, respectively. Usually, r 1 + r 2 ≤ 0.6 r_{1}+r_{2}\leq 0.6 .

[136] figure: Table 6: Comparison of activation stored in the GPT series architecture, with decreased activation values highlighted in red for PRAC. Operation Activation Saved Baseline PRAC ( 0 ≤ r 1 + r 2 ≤ 0.6 ) (0\leq r_{1}+r_{2}\leq 0.6) X = LayerNorm ⁡ ( X ~ ) X=\mathrm{LayerNorm}(\tilde{X}) X ~ ∈ ℝ b × s × n \tilde{X}\in\mathbb{R}^{b\times s\times n} ( μ ⁡ ( X ~ ) , σ ​ ( X ~ ) 2 ) ∈ ℝ b × s (\mu(\tilde{X}),\sigma(\tilde{X})^{2})\in\mathbb{R}^{b\times s} X ~ ​ P x ∈ ℝ b × s × ( n ​ r 1 ) , X ~ ​ Q x ∈ ℝ b × s × ( n ​ r 2 ) {\color[rgb]{1,0,0}\tilde{X}P_{x}\in\mathbb{R}^{b\times s\times(nr_{1})},\tilde{X}Q_{x}\in\mathbb{R}^{b\times s\times(nr_{2})}} ( μ ⁡ ( X ) , σ ​ ( X ) 2 ) ∈ ℝ b × s (\mu(X),\sigma(X)^{2})\in\mathbb{R}^{b\times s} q = X ​ W q q=XW_{q}\ k = X ​ W k k=XW_{k} v = X ​ W v v=XW_{v} X ∈ ℝ b × s × n X\in\mathbb{R}^{b\times s\times n} X ​ P q ∈ ℝ b × s × ( n ​ r 1 ) {\color[rgb]{1,0,0}XP_{q}\in\mathbb{R}^{b\times s\times(nr_{1})}} X ​ Q q ∈ ℝ b × s × ( n ​ r 2 ) {\color[rgb]{1,0,0}XQ_{q}\in\mathbb{R}^{b\times s\times(nr_{2})}} reshape q , k , v q,k,v to ( b , h , s , n / h ) (b,h,s,n/h) None None A h = flash ​ _ ​ attn ​ ( q , k , v ) A_{h}=\mathrm{flash\_attn}(q,k,v) q , k , v ∈ ℝ b × h × s × n / h q,k,v\in\mathbb{R}^{b\times h\times s\times n/h} two buffers ∈ ℝ b × s × h \in\mathbb{R}^{b\times s\times h} q , k , v ∈ ℝ b × h × s × n / h q,k,v\in\mathbb{R}^{b\times h\times s\times n/h} two buffers ∈ ℝ b × s × h \in\mathbb{R}^{b\times s\times h} reshape A h A_{h} to ( b , s , n ) (b,s,n) None None A o ′′ = A h ​ W o T A_{o}^{\prime\prime}=A_{h}W_{o}^{T} A h ∈ ℝ b × s × n A_{h}\in\mathbb{R}^{b\times s\times n} A h ​ P h ∈ ℝ b × s × ( n ​ r 1 ) {\color[rgb]{1,0,0}A_{h}P_{h}\in\mathbb{R}^{b\times s\times(nr_{1})}} A h ​ Q h ∈ ℝ b × s × ( n ​ r 2 ) {\color[rgb]{1,0,0}A_{h}Q_{h}\in\mathbb{R}^{b\times s\times(nr_{2})}} residual: A o ′ = A o ′′ + X ~ A_{o}^{\prime}=A_{o}^{\prime\prime}+\tilde{X} None None A o = LayerNorm ⁡ ( A o ′ ) A_{o}=\mathrm{LayerNorm}(A_{o}^{\prime}) A o ′ ∈ ℝ b × s × n A_{o}^{\prime}\in\mathbb{R}^{b\times s\times n} ( μ ⁡ ( A o ′ ) , σ ​ ( A o ′ ) 2 ) ∈ ℝ b × s (\mu(A_{o}^{\prime}),\sigma(A_{o}^{\prime})^{2})\in\mathbb{R}^{b\times s} A o ′ ​ P o ′ ∈ ℝ b × s × ( n ​ r 1 ) , A o ′ ​ Q o ′ ∈ ℝ b × s × ( n ​ r 2 ) {\color[rgb]{1,0,0}A_{o}^{\prime}P_{o}^{\prime}\in\mathbb{R}^{b\times s\times(nr_{1})},A_{o}^{\prime}Q_{o}^{\prime}\in\mathbb{R}^{b\times s\times(nr_{2})}} ( μ ⁡ ( A o ′ ) , σ ​ ( A o ′ ) 2 ) ∈ ℝ b × s (\mu(A_{o}^{\prime}),\sigma(A_{o}^{\prime})^{2})\in\mathbb{R}^{b\times s} A u ′ = A o ​ W up T A_{u}^{\prime}=A_{o}W_{\mathrm{up}}^{T} A o ∈ ℝ b × s × n A_{o}\in\mathbb{R}^{b\times s\times n} A o ​ P o ∈ ℝ b × s × ( n ​ r 1 ) {\color[rgb]{1,0,0}A_{o}P_{o}\in\mathbb{R}^{b\times s\times(nr_{1})}} A o ​ Q o ∈ ℝ b × s × ( n ​ r 2 ) {\color[rgb]{1,0,0}A_{o}Q_{o}\in\mathbb{R}^{b\times s\times(nr_{2})}} A u = GeLU ⁡ ( A u ′ ) A_{u}=\mathrm{GeLU}(A_{u}^{\prime}) A u ′ ∈ ℝ b × s × m A_{u}^{\prime}\in\mathbb{R}^{b\times s\times m} A u ′ ​ P u ′ ∈ ℝ b × s × ( m ​ r 1 ) {\color[rgb]{1,0,0}A_{u}^{\prime}P_{u}^{\prime}\in\mathbb{R}^{b\times s\times(mr_{1})}} A u ′ ​ Q u ′ ∈ ℝ b × s × ( m ​ r 2 ) {\color[rgb]{1,0,0}A_{u}^{\prime}Q_{u}^{\prime}\in\mathbb{R}^{b\times s\times(mr_{2})}} A d ′ = A u ​ W down T A_{d}^{\prime}=A_{u}W_{\mathrm{down}}^{T} A u ∈ ℝ b × s × m A_{u}\in\mathbb{R}^{b\times s\times m} A u ​ P u ∈ ℝ b × s × ( m ​ r 1 ) {\color[rgb]{1,0,0}A_{u}P_{u}\in\mathbb{R}^{b\times s\times(mr_{1})}} A u ​ Q u ∈ ℝ b × s × ( m ​ r 2 ) {\color[rgb]{1,0,0}A_{u}Q_{u}\in\mathbb{R}^{b\times s\times(mr_{2})}} residual: A d = A d ′ + A o ′ A_{d}=A_{d}^{\prime}+A_{o}^{\prime} None None

[137] p: A comparison of activation compression between PRAC and baseline methods is presented in Table 6 . The proposed PRAC compresses both linear layers (including the projection layers in Attention and the MLP) and non-linear layers (including LayerNorm and the GeLU activation). The mean and variance results in LayerNorm are not compressed, as they contribute negligibly to the total memory footprint (i.e., b ​ s ≪ b ​ s ​ n bs\ll bsn ). Flash Attention operations are not compressed by PRAC due to their intricate coupled structure and engineering optimizations. Nevertheless, the compressions above are sufficient for PRAC to achieve an overall memory reduction of nearly 40% in large-batch-size training tasks.

[138] h2: Appendix C Theoretical Results for PRAC

[139] h3: C.1 Notations and Useful Lemma

[140] h6: Definition 7 (Orthogonal Group) .

[141] p: For a positive integer m m , let M m ​ ( ℝ ) M_{m}(\mathbb{R}) denote the set of all m × m m\times m real matrices. The orthogonal group, denoted 𝒪 ⁡ ( m ) \mathcal{O}(m) , is defined as:

[142] table: 𝒪 ⁡ ( m ) ≔ { A ∈ M m ​ ( ℝ ) ∣ A ⊤ ​ A = I m } . \mathcal{O}(m)\coloneqq\left\{A\in M_{m}(\mathbb{R})\mid A^{\top}A=I_{m}\right\}. (8)

[143] h6: Lemma 8 .

[144] p: Let S ~ ∈ ℝ m × k \tilde{S}\in\mathbb{R}^{m\times k} be a random matrix whose entries are independent and identically distributed (i.i.d.) standard normal variables, i.e., S ~ i ​ j ∼ i . i . d . 𝒩 ⁡ ( 0 , 1 ) \tilde{S}_{ij}\stackrel{{\scriptstyle i.i.d.}}{{\sim}}\mathcal{N}(0,1) . Consider the (thin) QR decomposition of S ~ = V ​ R \tilde{S}=VR , where V ∈ ℝ m × k V\in\mathbb{R}^{m\times k} satisfies V ⊤ ​ V = I k V^{\top}V=I_{k} and R ∈ ℝ k × k R\in\mathbb{R}^{k\times k} is an upper-triangular matrix with positive diagonal entries. Then for any orthogonal matrix O ∈ 𝒪 ⁡ ( m ) O\in\mathcal{O}(m) , O ​ V OV and V V are identically distributed, i.e.

[145] table: O ​ V = d V ​ ∀ O ∈ 𝒪 ⁡ ( m ) . OV\stackrel{{\scriptstyle d}}{{=}}V\;\;\forall O\in\mathcal{O}(m). (9)

[146] h6: Proof.

[147] p: Let O ∈ 𝒪 ⁡ ( m ) O\in\mathcal{O}(m) be an arbitrary fixed orthogonal matrix and set S ~ ′ = O ​ S ~ \tilde{S}^{\prime}=O\tilde{S} . Consider the QR decomposition of S ~ \tilde{S} and S ~ ′ \tilde{S}^{\prime} , we have

[148] table: S ~ = V ​ R , S ~ ′ = V ′ ​ R ′ , \tilde{S}=VR,\tilde{S}^{\prime}=V^{\prime}R^{\prime}, (10)

[149] p: where V , V ′ ∈ ℝ m × k V,V^{\prime}\in\mathbb{R}^{m\times k} satisfie V ⊤ ​ V = I k , ( V ′ ) ⊤ ​ V ′ = I k V^{\top}V=I_{k},(V^{\prime})^{\top}V^{\prime}=I_{k} and R , R ′ R,R^{\prime} are upper-triangular matrices with positive diagonal entries. Since the standard normal distribution is rotationally invariant, S ~ ′ \tilde{S}^{\prime} has the same distribution as S ~ \tilde{S} , i.e., S ~ ′ = d S ~ \tilde{S}^{\prime}\stackrel{{\scriptstyle d}}{{=}}\tilde{S} , therefore we have V = d V ′ V\stackrel{{\scriptstyle d}}{{=}}V^{\prime} . What’s more,

[150] table: S ~ ′ = O ​ S ~ = O ​ V ​ R . \tilde{S}^{\prime}=O\tilde{S}=OVR. (11)

[151] p: Comparing ( 10 ) and ( 11 ), from the uniqueness of the thin QR decomposition we have V ′ = O ​ V , R ′ = R V^{\prime}=OV,R^{\prime}=R , then

[152] table: V ′ = O ​ V = d V ​ ∀ O ∈ 𝒪 ⁡ ( m ) . V^{\prime}=OV\stackrel{{\scriptstyle d}}{{=}}V\;\;\forall O\in\mathcal{O}(m). (12)

[153] p: ∎

[154] h6: Lemma 9 .

[155] p: Suppose the matrix M ∈ ℝ m × m M\in\mathbb{R}^{m\times m} satisfies M ​ O = O ​ M ​ ∀ O ∈ 𝒪 ⁡ ( m ) MO=OM\;\;\forall O\in\mathcal{O}(m) , then M M must be a scalar matrix (i.e., M = c ​ I m M=cI_{m} ).

[156] h6: Proof.

[157] p: We construct the reflection matrix as follows:

[158] table: J i = diag ⁡ ( 1 , ⋯ , 1 , − 1 ⏟ i , 1 , ⋯ , 1 ) ∈ ℝ m × m , J_{i}=\mathrm{diag}(1,\cdots,1,\underbrace{-1}_{i},1,\cdots,1)\in\mathbb{R}^{m\times m}, (13)

[159] p: where only the i i -th diagonal entry is -1 and the others are 1. Clearly, J i ∈ 𝒪 ⁡ ( m ) J_{i}\in\mathcal{O}(m) . From the commutativity condition J k J_{k} , compare the entries in the i i -th row and j j -th column (with i ≠ j i\neq j ), we have

[160] table: ( J i ​ M ) i ​ j = − M i ​ j , ( M ​ J k ) i ​ j = M i ​ j . (J_{i}M)_{ij}=-M_{ij},(MJ_{k})_{ij}=M_{ij}. (14)

[161] p: Equating the two expressions gives:

[162] table: − M i ​ j = M i ​ j ⇒ M i ​ j = 0 ​ ( i ≠ j ) . -M_{ij}=M_{ij}\Rightarrow M_{ij}=0\;(i\neq j).

[163] p: Therefore, M M is a diagonal matrix. Denote it as:

[164] table: M = diag ⁡ ( λ 1 , λ 2 , ⋯ , λ m ) . M=\mathrm{diag}(\lambda_{1},\lambda_{2},\cdots,\lambda_{m}). (15)

[165] p: Then consider a permutation matrix P i ​ j P_{ij} that swaps the i i -th and j j -th rows (and columns). It is also orthogonal, with P i ​ j − 1 = P i ​ j ⊤ = P i ​ j P_{ij}^{-1}=P_{ij}^{\top}=P_{ij} . From the commutativity condition P i ​ j ​ M = M ​ P i ​ j P_{ij}M=MP_{ij} , we have:

[166] table: M = P i ​ j ​ M ​ P i ​ j . M=P_{ij}MP_{ij}. (16)

[167] p: Conjugating M M by P i ​ j P_{ij} swaps the i i -th and j j -th diagonal entries of M M . Since the matrices M M and P i ​ j ​ M ​ P i ​ j P_{ij}MP_{ij} are equal, their diagonal entries must coincide, giving λ i = λ j \lambda_{i}=\lambda_{j} for any pair i , j i,j . Hence, M M must be a scalar matrix (i.e., M = c ​ I m M=cI_{m} ). ∎

[168] h6: Lemma 10 .

[169] p: Suppose the random matrix V ∈ ℝ m × k V\in\mathbb{R}^{m\times k} satisfies V ⊤ ​ V = I k V^{\top}V=I_{k} and ∀ O ∈ 𝒪 ⁡ ( m ) , O ​ V = d V \forall O\in\mathcal{O}(m),OV\stackrel{{\scriptstyle d}}{{=}}V . Then we have

[170] table: 𝔼 ⁡ [ V ​ V ⊤ ] = k m ​ I m . \mathbb{E}[VV^{\top}]=\frac{k}{m}I_{m}. (17)

[171] h6: Proof.

[172] p: For any orthogonal matrix O ∈ 𝒪 ⁡ ( m ) O\in\mathcal{O}(m) , O ​ V OV has the same distribution as V V . Then,

[173] table: 𝔼 ⁡ [ V ​ V ⊤ ] = 𝔼 ⁡ [ ( O ​ V ) ​ ( O ​ V ) ⊤ ] = O ​ 𝔼 ​ [ V ​ V ⊤ ] ​ O ⊤ , \mathbb{E}[VV^{\top}]=\mathbb{E}[(OV)(OV)^{\top}]=O\mathbb{E}[VV^{\top}]O^{\top},

[174] p: due to O ⊤ = O − 1 O^{\top}=O^{-1} ,

[175] table: 𝔼 ⁡ [ V ​ V ⊤ ] ​ O = O ​ 𝔼 ​ [ V ​ V ⊤ ] ​ ∀ O ∈ 𝒪 ⁡ ( m ) . \mathbb{E}[VV^{\top}]O=O\mathbb{E}[VV^{\top}]\;\;\forall O\in\mathcal{O}(m).

[176] p: From Lemma 9 , the expectation 𝔼 ⁡ [ V ​ V ⊤ ] \mathbb{E}[VV^{\top}] of the random matrix must be a scaler matrix, i.e.,

[177] table: 𝔼 ⁡ [ V ​ V ⊤ ] = c ​ I m . \mathbb{E}[VV^{\top}]=cI_{m}. (18)

[178] p: The constant c c is determined by computing the trace:

[179] table: tr ⁡ ( 𝔼 ⁡ [ V ​ V ⊤ ] ) = 𝔼 ⁡ [ tr ⁡ ( V ​ V ⊤ ) ] = 𝔼 ⁡ [ tr ⁡ ( V ⊤ ​ V ) ] = k . \mathrm{tr}(\mathbb{E}[VV^{\top}])=\mathbb{E}[\mathrm{tr}(VV^{\top})]=\mathbb{E}[\mathrm{tr}(V^{\top}V)]=k. (19)

[180] p: Meanwhile, tr ⁡ ( c ​ I m ) = c ​ m \mathrm{tr}(cI_{m})=cm , thus c ​ m = k ⇒ c = k m cm=k\Rightarrow c=\frac{k}{m} . ∎

[181] h6: Lemma 11 .

[182] p: Suppose Q 1 ∈ ℝ n × r 1 Q_{1}\in\mathbb{R}^{n\times r_{1}} be a fixed orthogonal matrix, random matrix S o S_{o} be generated by ( 5 ), and let the random matrix Q 2 ∈ ℝ n × r 2 Q_{2}\in\mathbb{R}^{n\times r_{2}} be the first component of QR ​ ( S o ) \text{QR}(S_{o}) , then we have:

[183] table: 𝔼 ⁡ [ Q 2 ​ Q 2 ⊤ ] = r 2 n − r 1 ​ ( I n − Q 1 ​ Q 1 ⊤ ) . \mathbb{E}[Q_{2}Q_{2}^{\top}]=\frac{r_{2}}{n-r_{1}}(I_{n}-Q_{1}Q_{1}^{\top}). (20)

[184] h6: Proof.

[185] p: Let U ∈ ℝ n × ( n − r 1 ) U\in\mathbb{R}^{n\times(n-r_{1})} be an orthonormal basis for the orthogonal complement of P P :

[186] table: U ⊤ ​ U = I n − r 1 , Q 1 ⊤ ​ U = O r 1 × ( n − r 1 ) , Q 1 ​ Q 1 ⊤ + U ​ U ⊤ = I n , U^{\top}U=I_{n-r_{1}},Q_{1}^{\top}U=O_{r_{1}\times(n-r_{1})},Q_{1}Q_{1}^{\top}+UU^{\top}=I_{n}, (21)

[187] p: then

[188] table: S o = S − Q 1 ​ Q 1 ⊤ ​ S = U ​ U ⊤ ​ S . S_{o}=S-Q_{1}Q_{1}^{\top}S=UU^{\top}S. (22)

[189] p: We define S ~ = U ⊤ ​ S ∈ ℝ ( n − r 1 ) × r 2 \tilde{S}=U^{\top}S\in\mathbb{R}^{(n-r_{1})\times r_{2}} , then S o = U ​ S ~ S_{o}=U\tilde{S} . Since U U has orthonormal columns and the entries of S S are i.i.d Gaussian, the entries of S ~ \tilde{S} are also i.i.d Gaussian. Perform QR decomposition on S ~ \tilde{S} : S ~ = V ​ R \tilde{S}=VR , then

[190] table: S o = U ​ S ~ = ( U ​ V ) ​ R , S_{o}=U\tilde{S}=(UV)R, (23)

[191] p: according to the uniqueness of the thin QR decomposition, the projection matrix in the algorithm satisfies Q 2 = U ​ V ∈ ℝ n × r 2 Q_{2}=UV\in\mathbb{R}^{n\times r_{2}} . Then,

[192] table: 𝔼 ⁡ [ Q 2 ​ Q 2 ⊤ ] = 𝔼 ⁡ [ U ​ V ​ V ⊤ ​ U ⊤ ] \displaystyle\mathbb{E}[Q_{2}Q_{2}^{\top}]=\mathbb{E}[UVV^{\top}U^{\top}] = U ​ 𝔼 ​ [ V ​ V ⊤ ] ​ U ⊤ \displaystyle=U\mathbb{E}[VV^{\top}]U^{\top} (24) = ( a ) U ⁡ ( r 2 n − r 1 ​ I n − r 1 ) ​ U ⊤ \displaystyle\stackrel{{\scriptstyle(a)}}{{=}}U(\frac{r_{2}}{n-r_{1}}I_{n-r_{1}})U^{\top} = r 2 n − r 1 ​ ( I n − Q 1 ​ Q 1 ⊤ ) \displaystyle=\frac{r_{2}}{n-r_{1}}(I_{n}-Q_{1}Q_{1}^{\top})

[193] p: where the equality (a) holds according to Lemma 10 and V ∈ ℝ ( n − r 1 ) × r 2 V\in\mathbb{R}^{(n-r_{1})\times r_{2}} . ∎

[194] h3: C.2 Omitted Proofs in Section 4

[195] h6: Theorem 12 (Unbiased Reconstruction of PRAC) .

[196] p: Let P ∈ ℝ n × r 1 P\in\mathbb{R}^{n\times r_{1}} be the projection matrix defined in ( 6 ). If the scaling factor is set to k = n − r 1 r 2 k=\frac{n-r_{1}}{r_{2}} , the reconstruction X ~ = X ​ P ​ P ⊤ \tilde{X}=XPP^{\top} satisfies 𝔼 ⁡ [ X ~ ] = X \mathbb{E}[\tilde{X}]=X .

[197] h6: Proof.

[198] p: The expectations for the reconstruction X ~ \tilde{X} are as follows:

[199] table: 𝔼 ⁡ [ X ~ ] = 𝔼 ⁡ [ X ​ Q 1 ​ Q 1 T + k ​ X ​ Q 2 ​ Q 2 ⊤ ] \displaystyle\mathbb{E}[\tilde{X}]=\mathbb{E}[XQ_{1}Q_{1}^{T}+kXQ_{2}Q_{2}^{\top}] = X ​ Q 1 ​ Q 1 ⊤ + k ​ X ​ 𝔼 ​ [ Q 2 ​ Q 2 ⊤ ] \displaystyle=XQ_{1}Q_{1}^{\top}+kX\mathbb{E}[Q_{2}Q_{2}^{\top}] (25) = ( a ) X ​ Q 1 ​ Q 1 ⊤ + k ​ r 2 n − r 1 ​ X ​ ( I n − Q 2 ​ Q 2 ⊤ ) \displaystyle\stackrel{{\scriptstyle(a)}}{{=}}XQ_{1}Q_{1}^{\top}+k\frac{r_{2}}{n-r_{1}}X(I_{n}-Q_{2}Q_{2}^{\top}) = X ​ Q 1 ​ Q 1 ⊤ + n − r 1 r 2 ​ r 2 n − r 1 ​ X ​ ( I n − Q 2 ​ Q 2 ⊤ ) \displaystyle=XQ_{1}Q_{1}^{\top}+\frac{n-r_{1}}{r_{2}}\frac{r_{2}}{n-r_{1}}X(I_{n}-Q_{2}Q_{2}^{\top}) = X , \displaystyle=X,

[200] p: where in (a) we use Lemma 11 to replace the 𝔼 ⁡ [ Q 2 ​ Q 2 ⊤ ] \mathbb{E}[Q_{2}Q_{2}^{\top}] term. ∎

[201] h6: Theorem 13 (Unbiased Reconstruction of RAC) .

[202] p: Let Q 2 ∈ ℝ n × r 2 Q_{2}\in\mathbb{R}^{n\times r_{2}} sample uniformly from the Stiefel manifold. Set the scaling factor k = n r 2 k=\frac{n}{r_{2}} . Then the reconstruction X ~ rac = ( k ​ X ​ Q 2 ) ​ Q 2 ⊤ \tilde{X}_{\text{rac}}=(kXQ_{2})Q_{2}^{\top} satisfies 𝔼 ⁡ [ X ~ rac ] = X \mathbb{E}[\tilde{X}_{\text{rac}}]=X .

[203] h6: Proof.

[204] p: This result follows as a special case of Theorem 12 by setting r 1 = 0 r_{1}=0 and then k = n / r 2 k=n/r_{2} . ∎

[205] h6: Theorem 14 (Variance Bound of PRAC) .

[206] p: Under the conditions of Theorem 12 , the reconstruction error variance is bounded by:

[207] table: 𝔼 ⁡ [ ‖ X ~ − X ‖ F 2 ] ≤ ( n − r 1 r 2 − 1 ) ​ ‖ X − X ​ Q 1 ​ Q 1 ⊤ ‖ F 2 . \mathbb{E}\bigl[\|\tilde{X}-X\|_{F}^{2}\bigr]\leq(\frac{n-r_{1}}{r_{2}}-1)\,\bigl\|X-XQ_{1}Q_{1}^{\top}\bigr\|_{F}^{2}.

[208] h6: Proof.

[209] p: We evaluate the expected squared Frobenius norm of the reconstruction error,

[210] table: 𝔼 ⁡ [ ‖ X − X ~ ‖ F 2 ] \displaystyle\mathbb{E}[\|X-\tilde{X}\|_{F}^{2}] = 𝔼 ⁡ [ ‖ X ⁡ ( I n − Q 1 ​ Q 1 ⊤ − k ​ Q 2 ​ Q 2 ⊤ ) ‖ F 2 ] . \displaystyle=\mathbb{E}[\|X(I_{n}-Q_{1}Q_{1}^{\top}-kQ_{2}Q_{2}^{\top})\|_{F}^{2}]. (26)

[211] p: Recall from the properties of Q 1 Q_{1} that I n − Q 1 ​ Q 1 ⊤ = U ​ U ⊤ I_{n}-Q_{1}Q_{1}^{\top}=UU^{\top} . Substituting this relation, we obtain

[212] table: 𝔼 ⁡ [ ‖ X − X ~ ‖ F 2 ] = 𝔼 ⁡ [ ‖ X ⁡ ( U ​ U ⊤ − k ​ Q 2 ​ Q 2 ⊤ ) ‖ F 2 ] = 𝔼 ⁡ [ tr ⁡ ( X ​ ( U ​ U ⊤ − k ​ Q 2 ​ Q 2 ⊤ ) 2 ​ X ⊤ ) ] , \displaystyle\mathbb{E}[\|X-\tilde{X}\|_{F}^{2}]=\mathbb{E}[\|X(UU^{\top}-kQ_{2}Q_{2}^{\top})\|_{F}^{2}]=\mathbb{E}[\operatorname{tr}(X(UU^{\top}-kQ_{2}Q_{2}^{\top})^{2}X^{\top})], (27)

[213] p: where the last equality follows from the identity ‖ A ‖ F 2 = tr ⁡ ( A ​ A ⊤ ) \|A\|_{F}^{2}=\operatorname{tr}(AA^{\top}) . Then, we compute the expectation of the squared matrix term:

[214] table: 𝔼 ⁡ [ ( U ​ U ⊤ − k ​ Q 2 ​ Q 2 ⊤ ) 2 ] = U ​ U ⊤ − 2 ​ k ​ 𝔼 ​ [ Q 2 ​ Q 2 ⊤ ] + k 2 ​ 𝔼 ​ [ Q 2 ​ Q 2 ⊤ ] \mathbb{E}\left[(UU^{\top}-kQ_{2}Q_{2}^{\top})^{2}\right]=UU^{\top}-2k\mathbb{E}[Q_{2}Q_{2}^{\top}]+k^{2}\mathbb{E}[Q_{2}Q_{2}^{\top}] (28)

[215] p: From Lemma 10 , we have 𝔼 ⁡ [ Q 2 ​ Q 2 ⊤ ] = 1 k ​ U ​ U ⊤ \mathbb{E}[Q_{2}Q_{2}^{\top}]=\frac{1}{k}UU^{\top} . Substituting this yields

[216] table: 𝔼 ⁡ [ ( U ​ U ⊤ − k ​ Q 2 ​ Q 2 ⊤ ) 2 ] = U ​ U ⊤ ​ ( 1 − 2 ​ k ​ 1 k + k 2 ​ 1 k ) = U ​ U ⊤ ​ ( k − 1 ) , \mathbb{E}\left[(UU^{\top}-kQ_{2}Q_{2}^{\top})^{2}\right]=UU^{\top}(1-2k\frac{1}{k}+k^{2}\frac{1}{k})=UU^{\top}(k-1), (29)

[217] p: Substituting ( 29 ) into ( 27 ), we have:

[218] table: 𝔼 ⁡ [ ‖ X − X ~ ‖ F 2 ] = tr ⁡ ( X ​ U ​ U ⊤ ​ X ⊤ ) ​ ( k − 1 ) = ( n − r 1 r 2 − 1 ) ​ ‖ X − X ​ Q 1 ​ Q 1 ⊤ ‖ F 2 \mathbb{E}[\|X-\tilde{X}\|_{F}^{2}]=\mathrm{tr}(XUU^{\top}X^{\top})(k-1)=(\frac{n-r_{1}}{r_{2}}-1)\|X-XQ_{1}Q_{1}^{\top}\|_{F}^{2} (30)

[219] p: ∎

[220] h6: Theorem 15 (Variance Bound of RAC) .

[221] p: Under the conditions of Theorem 13 , then the reconstruction error variance is bounded by:

[222] table: 𝔼 ⁡ [ ‖ X ~ rac − X ‖ F 2 ] ≤ ( n r 2 − 1 ) ​ ‖ X ‖ F 2 . \mathbb{E}\bigl[\|\tilde{X}_{\text{rac}}-X\|_{F}^{2}\bigr]\leq(\frac{n}{r_{2}}-1)\,\|X\|_{F}^{2}.

[223] h6: Proof.

[224] p: This result follows as a special case of Theorem 14 by setting r 1 = 0 r_{1}=0 and then k = n / r 2 k=n/r_{2} . ∎

[225] h6: Theorem 16 (Lower Bound) .

[226] p: Under Assumption 4.1 , if s < r < n s<r<n , then

[227] table: ( 4 ) ≥ ( n − s r − s − 1 ) ​ q . \eqref{eq:lower bound}\geq\left(\frac{n-s}{r-s}-1\right)q.

[228] h6: Proof.

[229] p: Without loss of generality, assume the activation matrix is X = diag ⁡ ( σ 1 , … , σ n ) ∈ ℝ n × n X=\operatorname{diag}(\sigma_{1},\dots,\sigma_{n})\in\mathbb{R}^{n\times n} with σ 1 ≥ σ 2 ≥ ⋯ ≥ σ n > 0 \sigma_{1}\geq\sigma_{2}\geq\cdots\geq\sigma_{n}>0 and, by Assumption 4.1 , ∑ i = s + 1 n σ i 2 ≤ q \sum_{i=s+1}^{n}\sigma_{i}^{2}\leq q . The unbiasedness condition 𝔼 ⁡ [ X ​ P ​ P ⊤ ] = X \mathbb{E}[XPP^{\top}]=X implies 𝔼 ⁡ [ P ​ P ⊤ ] = I \mathbb{E}[PP^{\top}]=I . Set A = P ​ P ⊤ ∈ ℝ n × n A=PP^{\top}\in\mathbb{R}^{n\times n} ; then the expected error can be written as

[230] table: ϵ = 𝔼 ​ ‖ X ⁡ ( A − I ) ‖ F 2 = ∑ i = 1 n σ i 2 ​ [ 𝔼 ​ ( A i ​ i − 1 ) 2 + ∑ j ≠ i 𝔼 ​ A i ​ j 2 ] ≡ ∑ i = 1 n σ i 2 ​ α i , \epsilon=\mathbb{E}\|X(A-I)\|_{F}^{2}=\sum_{i=1}^{n}\sigma_{i}^{2}\Bigl[\mathbb{E}(A_{ii}-1)^{2}+\sum_{j\neq i}\mathbb{E}A_{ij}^{2}\Bigr]\equiv\sum_{i=1}^{n}\sigma_{i}^{2}\alpha_{i}, (31)

[231] p: where α i ≥ 0 \alpha_{i}\geq 0 is defined by the bracket.

[232] p: Vanishing of the first s s coefficients. Consider a family of X X where σ i = t \sigma_{i}=t for i ≤ s i\leq s while σ s + 1 , … , σ n \sigma_{s+1},\dots,\sigma_{n} are fixed and satisfy the sum‑of‑squares constraint. If for some distribution of P P we have ∑ i = 1 s α i > 0 \sum_{i=1}^{s}\alpha_{i}>0 , then sending t → ∞ t\to\infty would make ϵ \epsilon arbitrarily large, so sup X inf P ϵ = ∞ \sup_{X}\inf_{P}\epsilon=\infty and the bound holds trivially. Hence we need only consider strategies with ∑ i = 1 s α i = 0 \sum_{i=1}^{s}\alpha_{i}=0 , i.e. α i = 0 \alpha_{i}=0 for all i ≤ s i\leq s . This forces P P to be block‑diagonal almost surely:

[233] table: P = [ I s 0 0 P ~ ] , P ~ ∈ ℝ ( n − s ) × ( r − s ) . P=\begin{bmatrix}I_{s}&0\\ 0&\tilde{P}\end{bmatrix},\qquad\tilde{P}\in\mathbb{R}^{(n-s)\times(r-s)}. (32)

[234] p: Consequently the error reduces to

[235] table: ϵ = ∑ i = s + 1 n α i ​ σ i 2 . \epsilon=\sum_{i=s+1}^{n}\alpha_{i}\sigma_{i}^{2}. (33)

[236] p: Lower bound on the sum of the remaining α i \alpha_{i} . Let A ~ = P ~ ​ P ~ ⊤ ∈ ℝ ( n − s ) × ( n − s ) \tilde{A}=\tilde{P}\tilde{P}^{\top}\in\mathbb{R}^{(n-s)\times(n-s)} . From 𝔼 ⁡ [ A ] = I \mathbb{E}[A]=I we obtain 𝔼 ⁡ [ tr ⁡ ( A ~ ) ] = 𝔼 ⁡ [ tr ⁡ ( A ) ] − s = n − s \mathbb{E}[\operatorname{tr}(\tilde{A})]=\mathbb{E}[\operatorname{tr}(A)]-s=n-s . Because rank ⁡ ( A ~ ) ≤ r − s \operatorname{rank}(\tilde{A})\leq r-s , Cauchy–Schwarz gives

[237] table: tr ⁡ ( A ~ 2 ) ≥ [ tr ⁡ ( A ~ ) ] 2 r − s . \operatorname{tr}(\tilde{A}^{2})\geq\frac{[\operatorname{tr}(\tilde{A})]^{2}}{r-s}. (34)

[238] p: Taking expectations and using Jensen’s inequality,

[239] table: 𝔼 ⁡ [ tr ⁡ ( A ~ 2 ) ] ≥ ( 𝔼 ⁡ [ tr ⁡ ( A ~ ) ] ) 2 r − s = ( n − s ) 2 r − s . \mathbb{E}[\operatorname{tr}(\tilde{A}^{2})]\geq\frac{(\mathbb{E}[\operatorname{tr}(\tilde{A})])^{2}}{r-s}=\frac{(n-s)^{2}}{r-s}. (35)

[240] p: Now compute the sum of α i \alpha_{i} for i > s i>s :

[241] table: ∑ i = s + 1 n α i \displaystyle\sum_{i=s+1}^{n}\alpha_{i} = ∑ i = s + 1 n [ 𝔼 ​ ( A i ​ i − 1 ) 2 + ∑ j ≠ i 𝔼 ​ A i ​ j 2 ] \displaystyle=\sum_{i=s+1}^{n}\Bigl[\mathbb{E}(A_{ii}-1)^{2}+\sum_{j\neq i}\mathbb{E}A_{ij}^{2}\Bigr] (36) = ∑ i = s + 1 n [ ∑ j = 1 n 𝔼 A i ​ j 2 − 1 ] ( since 𝔼 A i ​ i = 1 ) \displaystyle=\sum_{i=s+1}^{n}\Bigl[\sum_{j=1}^{n}\mathbb{E}A_{ij}^{2}-1\Bigr]\qquad(\text{since }\mathbb{E}A_{ii}=1) = ∑ i = s + 1 n ∑ j = s + 1 n 𝔼 A i ​ j 2 − ( n − s ) ( by the block‑diagonal form ) \displaystyle=\sum_{i=s+1}^{n}\sum_{j=s+1}^{n}\mathbb{E}A_{ij}^{2}-(n-s)\qquad(\text{by the block‑diagonal form}) = 𝔼 ⁡ [ tr ⁡ ( A ~ 2 ) ] − ( n − s ) \displaystyle=\mathbb{E}[\operatorname{tr}(\tilde{A}^{2})]-(n-s) ≥ ( n − s ) 2 r − s − ( n − s ) ≡ C . \displaystyle\geq\frac{(n-s)^{2}}{r-s}-(n-s)\equiv C.

[242] p: Completion of the lower bound. For any fixed σ s + 1 , … , σ n \sigma_{s+1},\dots,\sigma_{n} , using α i ≥ 0 \alpha_{i}\geq 0 we have

[243] table: ∑ i = s + 1 n α i ​ σ i 2 ≥ ( ∑ i = s + 1 n α i ) ​ min s + 1 ≤ i ≤ n ​ σ i 2 ≥ C ⋅ min i ⁡ σ i 2 . \sum_{i=s+1}^{n}\alpha_{i}\sigma_{i}^{2}\geq\Bigl(\sum_{i=s+1}^{n}\alpha_{i}\Bigr)\min_{s+1\leq i\leq n}\sigma_{i}^{2}\geq C\cdot\min_{i}\sigma_{i}^{2}. (37)

[244] p: Taking the infimum over admissible α i \alpha_{i} (i.e. over distributions of P P ) and then the supremum over σ i \sigma_{i} satisfying ∑ i = s + 1 n σ i 2 ≤ q \sum_{i=s+1}^{n}\sigma_{i}^{2}\leq q yields

[245] table: sup σ i inf α i ∑ i = s + 1 n α i ​ σ i 2 ≥ C ⋅ sup σ i min i ⁡ σ i 2 . \sup_{\sigma_{i}}\inf_{\alpha_{i}}\sum_{i=s+1}^{n}\alpha_{i}\sigma_{i}^{2}\geq C\cdot\sup_{\sigma_{i}}\min_{i}\sigma_{i}^{2}. (38)

[246] p: Under the sum‑of‑squares constraint, sup min i ⁡ σ i 2 \sup\min_{i}\sigma_{i}^{2} is attained when all σ i 2 \sigma_{i}^{2} are equal, i.e. σ i 2 = q / ( n − s ) \sigma_{i}^{2}=q/(n-s) ; hence sup min i ⁡ σ i 2 = q / ( n − s ) \sup\min_{i}\sigma_{i}^{2}=q/(n-s) . Substituting this together with the value of C C from ( 36 ) gives

[247] table: sup σ i inf α i ∑ i = s + 1 n α i ​ σ i 2 ≥ ( ( n − s ) 2 r − s − ( n − s ) ) ​ q n − s = ( n − s r − s − 1 ) ​ q . \sup_{\sigma_{i}}\inf_{\alpha_{i}}\sum_{i=s+1}^{n}\alpha_{i}\sigma_{i}^{2}\geq\Bigl(\frac{(n-s)^{2}}{r-s}-(n-s)\Bigr)\frac{q}{n-s}=\Bigl(\frac{n-s}{r-s}-1\Bigr)q. (39)

[248] p: By ( 33 ) this is exactly a lower bound for the quantity ( 4 ) , completing the proof.

[249] p: ∎

[250] h2: Appendix D Experiment Details

[251] h3: D.1 Pre-training Setting

[252] p: We detail the architectural configurations and pre-training hyperparameters for both the LLaMA and GPT models. To ensure numerical stability and computational efficiency, all LLaMA models are trained using bfloat16 precision and GPT models are trained using Automatic Mixed Precision. The key hyperparameters for LLaMA and GPT models across different scales are summarized in Table 7 .

[253] p: LLaMA Settings. The LLaMA models are trained with a maximum sequence length of 256 and a global batch size of 512. We employ a learning rate schedule comprising a linear warmup over the first 10% of training steps, followed by a cosine annealing phase that decays the learning rate to 10% of its peak value. Across all LLaMA model scales, we adopt the optimal learning rates reported in the original papers for comparison methods. For PRAC, the learning rate is selected from the grid { 0.0006 , 0.0008 , 0.001 , 0.002 , 0.004 } \left\{0.0006,0.0008,0.001,0.002,0.004\right\} , which is closely aligned with the settings used by the baselines.

[254] p: GPT Settings. For the GPT models, we adopt a maximum sequence length of 1024 while maintaining a global batch size of 512. We set the warmup steps to 2K, which corresponds to 4% of the total steps 3 3 3 https://github.com/zyushun/Adam-mini/tree/main . Notably, given that the official code and hyperparameters for GaLore ( Zhao et al., 2024a ) and RSO ( Chen et al., 2025 ) on GPT models are not publicly available, we train these models using learning rates aligned with the baseline. For these methods, we configure the ranks as 256 and 512 for the 124M and 355M models, respectively.

[255] figure: Table 7: Hyperparameter settings for pre-traing LLaMA and GPT-2 model. Params Hidden Intermediate Heads Layers Steps LLaMA 35M 384 1024 8 6 5K 60M 512 1376 8 8 10K 130M 768 2048 12 12 20K 350M 1024 2736 16 24 60K 1B 2048 5461 24 32 150K GPT-2 124M 768 3072 12 12 50K 355M 1024 4096 16 24 50K

[256] h3: D.2 Fine-tuning Setting

[257] p: We fine-tune the pre-trained RoBERTa-Base model on the GLUE benchmark using the Hugging Face library 4 4 4 https://huggingface.co/transformers/model_doc/roberta.html . All tasks are trained for 30 epochs with a batch size of 16. Refer to Table 8 for the specific hyperparameters employed for PRAC.

[258] figure: Table 8: Hyperparameter settings for fine-tuning RoBERTa-Base model on the GLUE benchmark using the PRAC method. COLA STSB MRPC RTE SST2 MNLI QNLI QQP Batch Size 16 16 16 16 16 16 16 16 Epochs 30 30 30 30 30 30 30 30 Learing Rate 3E-05 3E-05 3E-05 3E-05 1E-05 1E-05 1E-05 1E-05 Rank ( r 1 + r 2 r_{1}+r_{2} ) 4 PRAC Interval 200 Max Seq Length 512

[259] h3: D.3 Additional Result

[260] p: Compatibility with Advanced Optimizers. PRAC is orthogonal to optimizer choice. We integrate PRAC with memory-efficient optimizers Muon ( Liu et al., 2025 ) and Adam-mini ( Zhang et al., 2024b ) . As shown in Figure 6 and Table 9 , PRAC successfully reduces memory by an additional approximately 30% on top of these optimizers with negligible perplexity degradation, highlighting its versatility.

[261] figure: (a) Muon (LLaMA 130M) (b) Muon (LLaMA 350M) (c) Adam-mini (LLaMA 130M) (d) Adam-mini (LLaMA 350M) Figure 6: Loss curves of pre-training LLaMA model based on the Muon and Adam-mini optimizers w./w.o. PRAC.

[262] figure: Table 9: Combining with advanced optimizers on pretraining LLaMA. Report validation perplexity (PPL, lower is better) and the algorithm’s peak memory usage (lower is better). Method PRAC LLaMA-130M LLaMA-350M Ppl Mem Ppl Mem Muon × \times 23.90 21.04 17.98 45.26 ✓ \checkmark 24.16 15.37 ( ↓ 𝟐𝟕 % \bf{\downarrow 27\%} ) 18.04 30.82 ( ↓ 𝟑𝟐 % \bf{\downarrow 32\%} ) Adam- mini × \times 24.22 21.01 18.60 45.42 ✓ \checkmark 24.48 15.36 ( ↓ 𝟐𝟕 % \bf{\downarrow 27\%} ) 18.92 31.09 ( ↓ 𝟑𝟏 % \bf{\downarrow 31\%} )

[263] p: Selection of the Scaling Factor k k . We evaluate different values of k k on the linear and normalization layers of LLaMA-130M. Defining the theoretical baseline as k 0 = n − r 1 r 2 k_{0}=\frac{n-r_{1}}{r_{2}} , we test k ∈ { k 0 , 0.5 ​ k 0 , 0.2 ​ k 0 , 1.2 ​ k 0 } k\in\left\{k_{0},0.5k_{0},0.2k_{0},1.2k_{0}\right\} . The results in Figure 7 indicate that k = k 0 k=k_{0} yields the best convergence, whereas other settings result in performance degradation. This empirical evidence aligns with our theoretical findings (See Section 4.3 ).

[264] figure: (a) Linear Layer (b) Norm Layer Figure 7: Loss curve of using different k k in LLaMA-130M pre-training, where k 0 = n − r 1 r 2 k_{0}=\frac{n-r_{1}}{r_{2}} , Setting k = k 0 k=k_{0} performs better than larger or smaller settings, whether in linear or nonlinear layers.

[265] h2: Instructions for reporting errors

[266] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[267] p: Tip: You can select the relevant text first, to include it in your report.

[268] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[269] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
