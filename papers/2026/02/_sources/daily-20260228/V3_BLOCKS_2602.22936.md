[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Generalization Bounds of Stochastic Gradient Descent in Homogeneous Neural Networks

[3] h6: Abstract

[4] p: Algorithmic stability is among the most potent techniques in generalization analysis. However, its derivation usually requires a stepsize η t = 𝒪 ⁡ ( 1 / t ) \eta_{t}=\mathcal{O}(1/t) under non-convex training regimes, where t t denotes iterations. This rigid decay of the stepsize potentially impedes optimization and may not align with practical scenarios. In this paper, we derive the generalization bounds under the homogeneous neural network regimes, proving that this regime enables slower stepsize decay of order Ω ⁡ ( 1 / t ) \Omega(1/\sqrt{t}) under mild assumptions. We further extend the theoretical results from several aspects, e.g. , non-Lipschitz regimes. This finding is broadly applicable, as homogeneous neural networks encompass fully-connected and convolutional neural networks with ReLU and LeakyReLU activations.

[5] h2: 1 Introduction

[6] p: Stochastic gradient descent (SGD) has become a cornerstone in the field of deep learning. Extensive empirical applications have demonstrated its remarkable success in both optimization and generalization ( Goyal, 2017 ; Brown, 2020 ) . On the theoretical side, researchers have proposed various approaches to address the challenge of generalization ( McAllester, 1999 ; Russo and Zou, 2016 ; Bartlett et al., 2020 ) . Among these, one of the most popular is uniform convergence ( Bartlett et al., 2017 ; Wei and Ma, 2020 ) , which, unfortunately, has proven to be inadequate for understanding generalization in deep learning ( Shalev-Shwartz et al., 2010 ; Nagarajan and Kolter, 2019 ; Glasgow et al., 2023 ) .

[7] p: As an alternative to uniform convergence, algorithmic stability has emerged as a potential solution. In convex training scenarios, it provides guaranteed generalization for a reasonable number of training iterations ( Bousquet and Elisseeff, 2002 ; Hardt et al., 2016 ) . However, real-world applications typically occur in non-convex landscapes, where the generalization behavior of SGD remains elusive. Existing works on algorithmic stability under non-convex training regimes usually apply to the case with a stepsize of 𝒪 ⁡ ( 1 / t ) \mathcal{O}(1/t) , where t t denotes the training iteration ( Hardt et al., 2016 ; Kuzborskij and Lampert, 2018 ; Zhang et al., 2022 ) . Unfortunately, this stepsize is rarely used in practice due to its slow training speed (see Section 3.4 for theoretical insights and Figure 1 for illustration). This creates a gap between theory and practice, significantly reducing the practical utility of algorithmic stability.

[8] figure: (a) (b) Figure 1 : The training and test accuracy curves for SGD with various stepsize schedulers on CIFAR-10 using ResNet 18. Models trained with stepsize Θ ⁡ ( 1 / t ) \Theta(1/\sqrt{t}) (dotted line) converge faster and perform better than those trained with stepsize Θ ⁡ ( 1 / t ) \Theta(1/t) (solid line).

[9] p: To bridge this gap, there are three main approaches: (a) employing alternative algorithms such as Stochastic Gradient Langevin Dynamics (SGLD) instead of SGD ( Mou et al., 2018 ; Li et al., 2020 ; Farghly and Rebeschini, 2021 ; Bassily et al., 2021 ) ; (b) utilizing Polyak-Lojasiewicz (PL) conditions, which are closely associated with convexity ( Charles and Papailiopoulos, 2018 ; Nikolakakis et al., 2022 ; Zhu et al., 2024 ) ; (c) adopting alternative generalization metrics such as the gradient norm rather than the traditional generalization gap ( Lei, 2023 ; Zhang et al., 2024 ) . However, (a) is challenging to extend to SGD settings; (b) relies on a restrictive assumption that is difficult to relax; and (c) typically fails to generalize to multi-pass scenarios. Consequently, it remains under-explored how SGD effectively generalizes in multi-epoch regimes without convexity-related assumptions beyond 𝒪 ⁡ ( 1 / t ) \mathcal{O}(1/t) stepsize.

[10] p: In this paper, we take a step forward in bridging the gap by proving that SGD can generalize with stepsizes of order Ω ⁡ ( 1 / t ) \Omega(1/\sqrt{t}) . To the best of our knowledge, this is the first result that relaxes the stepsize requirement while allowing multiple uses of each sample under non-convex SGD training regimes without relying on additional assumptions like PL conditions. The derivation of this result relies on a notion called homogeneous neural networks ( Du et al., 2018 ; Lyu and Li, 2020 ) . Informally, a neural network Φ \Phi is H H -homogeneous if

[11] table: ∀ c > 0 : Φ ⁡ ( c ​ 𝒘 , X ) = c H ​ Φ ​ ( 𝒘 , X ) ​ for ​ all ​ 𝒘 ​ and ​ X , \forall c>0:\Phi(c{\bm{w}};{X})=c^{H}\Phi({\bm{w}};{X})\ \text{for}\ \text{all}\ {\bm{w}}\ \text{and}\ {X},

[12] p: where 𝒘 {\bm{w}} denotes the weight and X {X} denotes the input. Our paper proves that for homogeneous neural networks with a loss function that preserves homogeneity, if the loss is Lipschitz and approximately smooth, its generalization gap can be bounded over a reasonable number of training iterations.

[13] h3: 1.1 Our Results in More Detail.

[14] p: In particular, we consider a binary classification task with noisy labels { − 1 , 1 } \{-1,1\} , leading to a non-zero Bayesian optimal within the sphere. This condition is imposed to regulate the decay rate of the weight norm. To harness the homogeneity of H H -homogeneous neural networks defined above, we focus on a loss function of the form ℓ ⁡ ( y , y ^ ) = max ⁡ { 0 , − y ​ y ^ } \ell(y,\hat{y})=\max\{0,-y\hat{y}\} . Despite the fact that the loss function might encourage a small prediction y ^ \hat{y} and correspondingly small weights, we concentrate on the direction of the weights rather than their absolute values, which is valid in classification regimes. To simplify our discussion, we define all generalization metrics within the sphere, as shown in ( 3 ). Besides homogeneity, we anchor our analysis on two mild assumptions:

[15] p: Bounded Loss (Assumption 1 ) We assume that the individual loss is upper bounded, and the whole training loss is lower bounded by its Bayesian optimal value. This assumption is necessary because, without it, achieving a consistent generalization gap in the presence of noisy labels would be unattainable.

[16] p: Lipschitz and Approximately Smooth (Assumption 2 ) This assumption is standard in algorithmic stability analysis. We extend the previous smoothness assumption to approximate smoothness, which aligns better with ReLU activations.

[17] p: We derive Theorem 1 based on the above assumptions, elucidating the correlation between homogeneous neural networks and generalization:

[18] table: E 𝒜 , 𝒟 ​ ℒ s ​ ( 𝐰 T ) − ℒ ^ s ​ ( 𝐰 T ) ≤ [ L ​ m 2 ] 1 m 1 + 1 ​ [ 1 + 1 m 1 ] ​ T m 1 m 1 + 1 n , \mathbb{E}_{\mathcal{A},\mathcal{D}}\mathcal{L}^{s}({\bm{w}}_{T})-\hat{\mathcal{L}}^{s}({\bm{w}}_{T})\leq\left[Lm_{2}\right]^{\frac{1}{m_{1}+1}}\left[1+\frac{1}{m_{1}}\right]\frac{T^{\frac{m_{1}}{m_{1}+1}}}{n},

[19] p: where T T is the number of iterations, n n is the sample size. We use 𝒜 \mathcal{A} and 𝒟 \mathcal{D} to represent the randomized algorithm and the distribution of training dataset, respectively. A comprehensive summary of the notation used throughout this paper is provided in Appendix B.1 . This bound is derived under stepsizes satisfying E ​ η t = Ω ⁡ ( t H − 4 2 ) \mathbb{E}\eta_{t}=\Omega(t^{\frac{H-4}{2}}) and applies to the multi-pass training regime. For the specific case of H = 3 H=3 , the required stepsize simplifies to E ​ η t = Ω ⁡ ( 1 / t ) \mathbb{E}\eta_{t}=\Omega(1/\sqrt{t}) . Notably, these homogeneous neural networks can be constructed by normalizing multiple layers while leaving the final several layers unnormalized (see Proposition 1 ). As such, our results encompass a wide range of scenarios.

[20] p: Extending the Reach of Our Findings. Our findings can be extended in several directions. First , we demonstrate the broad applicability of our framework. While our main result focuses on the loss function ℓ ⁡ ( y , y ^ ) = max ⁡ { 0 , − y ​ y ^ } \ell(y,\hat{y})=\max\{0,-y\hat{y}\} , Corollary 1 extends our findings to other loss functions, including smooth homogeneous variants, e.g. , ℓ ⁡ ( y , y ^ ) = max ⁡ { 0 , − y ​ y ^ } u \ell(y,\hat{y})=\max\{0,-y\hat{y}\}^{u} with u ≥ 1 u\geq 1 , and functions with relaxed homogeneity. Similarly, we expand the scope of activation functions beyond ReLU, for instance σ ⁡ ( ⋅ ) = max ⁡ { 0 , ⋅ } u \sigma(\cdot)=\max\{0,\cdot\}^{u} , and architectures beyond linear connections, such as normalized ResNet models, as described in Proposition 1 . Second , for the specific case of three-homogeneous networks, Corollary 2 demonstrates that the test error consistently converges to the Bayesian optimal if the training loss approximates the Bayesian optimal within a reasonable number of iterations. Third , Theorem 2 shows a separation in optimization performance, indicating that our proposed stepsizes of E ​ η t = Ω ⁡ ( 1 / t ) \mathbb{E}\eta_{t}=\Omega(1/\sqrt{t}) achieve polynomial convergence, potentially outperforming the logarithmic convergence of E ​ η t = 𝒪 ⁡ ( 1 / t ) \mathbb{E}\eta_{t}=\mathcal{O}(1/t) . Example 3 further illustrates the compatibility of our setting regarding generalization and optimization. Finally , Section 4 proves that our framework ensures generalization without Lipschitz assumptions via an adapted on-average model stability, while maintaining the applicability to the multi-pass training regime.

[21] p: Proof Key Insights. Our key insights stem from a straightforward observation: For classification problems with homogeneous neural networks, accuracy depends solely on the direction of the weights. To utilize this insight, we project the training trajectory onto a sphere. While the observed stepsize is in order Ω ⁡ ( 1 / t ) \Omega(1/\sqrt{t}) , the effective stepsize of the projected trajectory can be in order Θ ⁡ ( 1 / t ) \Theta(1/t) . This leads to generalization, as demonstrated by algorithmic stability. One may question whether this effective stepsize Θ ⁡ ( 1 / t ) \Theta(1/t) negatively affects optimization. To address this concern, we provide additional discussions on optimization performance in Section 3.4 and present the training loss curve across different stepsize regimes in Figure 2 (left), which illustrates that the training loss can be optimized efficiently with the stepsize Ω ⁡ ( 1 / t ) \Omega(1/\sqrt{t}) .

[22] h3: 1.2 Related Works

[23] figure: Table 1 : Comparison of our method with related works on non-convex training regimes with SGD. Stepsize Order PL Condition Multi- pass Overpara- meterization Generalization Metric Hardt et al. (2016) 𝒪 ⁡ ( 1 / t ) \mathcal{O}(1/t) No Yes Yes Loss Kuzborskij and Lampert (2018) 𝒪 ⁡ ( 1 / t ) \mathcal{O}(1/t) No Yes Yes Loss Zhang et al. (2022) 𝒪 ⁡ ( 1 / t ) \mathcal{O}(1/t) No Yes Yes Loss Charles and Papailiopoulos (2018) 𝒪 ⁡ ( 1 ) \mathcal{O}(1) Yes Yes Yes Loss Nikolakakis et al. (2022) 𝒪 ⁡ ( 1 ) \mathcal{O}(1) Yes Yes Yes Loss Zhu et al. (2024) 𝒪 ⁡ ( 1 ) \mathcal{O}(1) Yes Yes Yes Loss Lei and Tang (2021) o ⁡ ( 1 ) o(1) No Yes No Gradient Lei (2023) 𝒪 ⁡ ( 1 ) \mathcal{O}(1) No No Yes Gradient Zhang et al. (2024) 𝒪 ⁡ ( 1 ) \mathcal{O}(1) No No Yes Gradient This Paper Ω ⁡ ( 1 / t ) \Omega(1/\sqrt{t}) No Yes Yes Loss

[24] p: Algorithmic Stability under Non-convex Training. To derive algorithmic stability in non-convex regimes with SGD, a typical requirement is to employ stepsize 𝒪 ⁡ ( 1 / t ) \mathcal{O}(1/t) ( Hardt et al., 2016 ; Kuzborskij and Lampert, 2018 ; Zhang et al., 2022 ) . To relax the stepsize requirement, one possible approach is to utilize alternative algorithms ( e.g. , SGLD) ( Mou et al., 2018 ; Li et al., 2020 ; Farghly and Rebeschini, 2021 ; Bassily et al., 2021 ) . When restricted to SGD training with ω ⁡ ( 1 / t ) \omega(1/t) stepsize, a line of work leverages the PL condition, which closely relates to convexity ( Charles and Papailiopoulos, 2018 ; Nikolakakis et al., 2022 ; Zhu et al., 2024 ) . Another line of work concentrates on alternative generalization metrics, such as the gradient norm, rather than the conventional generalization gap. However, they may face challenges when applied to multi-pass training regimes ( Lei, 2023 ; Zhang et al., 2024 ) . In contrast, this paper introduces a novel approach parallel to the aforementioned two lines, based on the notion of homogeneity . Table 1 summarizes the comparison.

[25] p: Homogeneous Neural Networks. The concept of homogeneous neural networks has been explored in the literature ( Wei et al., 2019 ; Rangamani and Banburski-Fahey, 2022 ; Vardi et al., 2022 ) . A line of work focuses on the implicit bias towards max-margin solutions in homogeneous neural networks ( Nacson et al., 2019 ; Lyu and Li, 2020 ; Ji and Telgarsky, 2020 ) and its variants ( Kunin et al., 2023 ) . Of particular relevance here is Paquin et al. (2023) , which investigates algorithmic stability for SGD within the context of homogeneous neural networks. Different from their analysis, this paper (a) aims to improve stepsize requirements in stability analysis, and (b) introduces the concept of approximate smoothness to extend the scope of previous regimes.

[26] h2: 2 Homogeneity

[27] p: Distributions, Datasets and Algorithms. Let ( X , Y ) ∼ 𝒫 ∈ R d × R ({X},{Y})\sim\mathcal{P}\in\mathbb{R}^{d}\times\mathbb{R} denote the feature-response pair, where 𝒫 \mathcal{P} denotes the joint distribution. We consider a noisy classification problem where Y ∈ { − 1 , + 1 } {Y}\in\{-1,+1\} contains label noise. The model f 𝒘 ​ ( ⋅ ) f_{\bm{w}}(\cdot) is trained on an n n -sample dataset S = { ( X i , Y i ) } i ∈ [ n ] S=\{({X}_{i},{Y}_{i})\}_{i\in[n]} where the samples are drawn i.i.d. from the distribution 𝒫 \mathcal{P} . Here [ n ] [n] denotes the set { 1 , 2 , ⋯ , n } \{1,2,\cdots,n\} . We denote 𝒟 \mathcal{D} as the distribution of dataset S S .

[28] p: We consider a non-negative loss function ℓ ⁡ ( 𝒘 , X , Y ) \ell({\bm{w}};{X},{Y}) with the population loss ℒ ⁡ ( 𝒘 ) ≜ E ( X , Y ) ∼ 𝒫 ​ ℓ ​ ( 𝐰 , X , Y ) \mathcal{L}({\bm{w}})\triangleq\mathbb{E}_{({X},{Y})\sim\mathcal{P}}\allowbreak\ell({\bm{w}};{X},{Y}) and the empirical loss ℒ ^ ​ ( 𝒘 ) ≜ 1 n ​ ∑ i ∈ [ n ] ℓ ⁡ ( 𝒘 , X i , Y i ) \hat{\mathcal{L}}({\bm{w}})\triangleq\frac{1}{n}\sum_{i\in[n]}\ell({\bm{w}};{X}_{i},{Y}_{i}) . We assume that the Bayesian optimal on the unit sphere is non-zero, namely σ ¯ 2 ≜ min 𝒘 ⁡ ℒ ⁡ ( 𝒘 / ‖ 𝒘 ‖ ) ≠ 0 \underline{\sigma}^{2}\triangleq\min_{{\bm{w}}}\mathcal{L}({\bm{w}}/\|{\bm{w}}\|)\neq 0 . This condition generally holds in scenarios with label noise.

[29] p: The model is optimized via the SGD algorithm 𝒜 \mathcal{A} . Let 𝒘 t {\bm{w}}_{t} denote the trained weight at iteration t t , and let 𝒗 t ≜ 𝒘 t / ‖ 𝒘 t ‖ {\bm{v}}_{t}\triangleq{\bm{w}}_{t}/\|{\bm{w}}_{t}\| be its corresponding direction. Starting from an initialization E 𝒜 ​ ‖ 𝐰 0 ‖ 2 = 𝒪 ⁡ ( 1 ) \mathbb{E}_{\mathcal{A}}\|{\bm{w}}_{0}\|^{2}=\mathcal{O}(1) , the weight update follows:

[30] table: 𝒘 t + 1 = 𝒘 t − η t ​ ∇ 𝒘 t ℓ t ​ ( 𝒘 t ) , {\bm{w}}_{t+1}={\bm{w}}_{t}-\eta_{t}\nabla_{{\bm{w}}_{t}}\ell_{t}({\bm{w}}_{t}), (1)

[31] p: where η t \eta_{t} is the stepsize and ℓ t \ell_{t} is the loss function at iteration t t . In this paper, we consider SGD with replacement, and therefore, ℓ t ​ ( ⋅ ) ≜ ℓ ⁡ ( ⋅ , X i , Y i ) \ell_{t}(\cdot)\triangleq\ell(\cdot;{X}_{i},{Y}_{i}) with probability 1 / n 1/n for each index i ∈ [ n ] i\in[n] . Let E I \mathbb{E}_{I} denote the expectation over the choice of the index i i at the current iteration, given the parameters from all previous iterations. Let E 𝒟 \mathbb{E}_{\mathcal{D}} denote the expectation over the training dataset S ∼ 𝒟 S\sim\mathcal{D} , and E 𝒜 \mathbb{E}_{\mathcal{A}} denote the expectation over the randomness of the algorithm 𝒜 \mathcal{A} , including the initialization and the sampling of indices across all previous iterations. Standard asymptotic notations are defined in Appendix B.1 .

[32] p: Homogeneity. Our results are based on the homogeneity of neural networks. Next, we provide a detailed definition of homogeneous neural networks and explain how they can be constructed.

[33] h6: Definition 1 .

[34] p: (Homogeneous function and homogeneous neural network) A function h h is H H -homogeneous ( H ≥ 0 H\geq 0 ) if h ⁡ ( c ​ 𝐰 ) = c H ​ h ​ ( 𝐰 ) h(c{\bm{w}})=c^{H}h({\bm{w}}) . Specifically, a neural network Φ ⁡ ( 𝐰 , X ) \Phi({\bm{w}};{X}) is H H -homogeneous ( H ≥ 0 H\geq 0 ) if

[35] table: Φ ⁡ ( c ​ 𝒘 , X ) = c H ​ Φ ​ ( 𝒘 , X ) . \Phi(c{\bm{w}};{X})=c^{H}\Phi({\bm{w}};{X}).

[36] p: It’s worth noting that the concept of homogeneity is evident across a range of neural network architectures. Specifically, neural networks employing ReLU, LeakyReLU, linear layers, and max-pooling layers inherently exhibit homogeneity. One could construct an H H -homogeneous neural networks based on Proposition 1 , and we refer to Figure 3 in Appendix A.2 for an illustration.

[37] h6: Proposition 1 (Homogeneity Construction) .

[38] p: Consider two types of layers:

[39] p: Normalized layers 1 1 1 We only present linear connections here for simplicity but it allows for different structures, e.g. , ResNet connections 𝒩 𝒘 ​ ( a ) ≜ a + 𝒘 ‖ 𝒘 ‖ ​ σ n ​ ( a ) \mathcal{N}_{\bm{w}}(a)\triangleq a+\frac{{\bm{w}}}{\|{\bm{w}}\|}\sigma_{n}(a) and max-pooling layers. 𝒩 𝒘 ​ ( a ) = 𝒘 ‖ 𝒘 ‖ ​ σ n ​ ( a ) \mathcal{N}_{\bm{w}}(a)=\frac{{\bm{w}}}{\|{\bm{w}}\|}\sigma_{n}(a) , with arbitrary activation σ n \sigma_{n} , e.g. , ReLU, sigmoid;

[40] p: Unnormalized layers 𝒰 𝒘 ​ ( a ) ≜ 𝒘 ​ σ u ​ ( a ) \mathcal{U}_{\bm{w}}(a)\triangleq{\bm{w}}\sigma_{u}(a) , where σ u \sigma_{u} is ReLU, LeakyReLU, Linear activation, or σ ⁡ ( ⋅ ) = max ⁡ { 0 , ⋅ } u \sigma(\cdot)=\max\{0,\cdot\}^{u} with u ≥ 1 u\geq 1 .

[41] p: For convenience, we omit the bias when the context is clear. The h h -layer neural network Φ H ​ ( 𝐰 , X ) \Phi_{H}({\bm{w}};{X}) with h − H h-H normalized layers 𝒩 𝐰 \mathcal{N}_{\bm{w}} and H H unnormalized layers 𝒰 𝐰 \mathcal{U}_{\bm{w}} is H H -homogeneous, where

[42] table: Φ H ​ ( 𝒘 , X ) = 𝒰 𝒘 h ∘ 𝒰 𝒘 h − 1 ∘ ⋯ ∘ 𝒰 𝒘 h − H + 1 ⏟ H ​ unnormalized layers ∘ 𝒩 𝒘 h − H ∘ ⋯ ∘ 𝒩 𝒘 1 ( X ) ⏟ h − H ​ normalized layers . \begin{split}\Phi_{H}({\bm{w}};{X})&=\underbrace{\mathcal{U}_{{\bm{w}}_{h}}\circ\mathcal{U}_{{\bm{w}}_{h-1}}\circ\cdots\circ\mathcal{U}_{{\bm{w}}_{h-H+1}}}_{H\text{ unnormalized layers}}\\ &\quad\circ\underbrace{\mathcal{N}_{{\bm{w}}_{h-H}}\circ\cdots\circ\mathcal{N}_{{\bm{w}}_{1}}({X})}_{h-H\text{ normalized layers}}.\end{split}

[43] p: Loss Function. Following the H H -homogeneous neural network Φ ⁡ ( 𝒘 , X ) \Phi({\bm{w}};{X}) , the main result in Theorem 1 focuses on the loss function

[44] table: ℓ ⁡ ( 𝒘 , X , Y ) = max ⁡ { − Y ​ Φ ​ ( 𝒘 , X ) , 0 } . \ell({\bm{w}};{X},{Y})=\max\{-{Y}\Phi({\bm{w}};{X}),0\}. (2)

[45] p: Extensions to other loss functions are further discussed in the Remark of Theorem 1 .

[46] p: The Validity of the Loss Function. The loss function in ( 2 ) is valid because (a) the training direction depends only on the weight direction in classification problems with homogeneous neural networks, and (b) the generalization metric is defined on the unit sphere, meaning that the bound of the generalization gap does not necessarily converge to zero as ‖ 𝒘 ‖ \|{\bm{w}}\| approaches zero. We choose this loss function because it harnesses the homogeneity of neural networks, namely, applying ℓ \ell on an H H -homogeneous neural network returns an H H -homogeneous loss. Our theorems can be generalized to other loss functions that similarly harness homogeneity, e.g. , ( max ⁡ { − Y ​ Φ ​ ( 𝒘 , X ) , 0 } ) u (\max\{-{Y}\Phi({\bm{w}};{X}),0\})^{u} with u ≥ 1 u\geq 1 . To proceed, we derive Lemma 1 based on the homogeneity:

[47] h6: Lemma 1 .

[48] p: For any iteration t > 0 t>0 and a non-negative H H -homogeneous function ℓ t \ell_{t} where H ≠ 0 H\neq 0 , define the effective stepsize η ~ t \tilde{\eta}_{t} as the stepsize projected onto the sphere, namely, on 𝐯 t = 𝐰 t / ‖ 𝐰 t ‖ {\bm{v}}_{t}={\bm{w}}_{t}/\|{\bm{w}}_{t}\| , then the following properties hold:

[49] p: Effective Stepsize on the sphere: η ~ t = η t ​ ‖ 𝒘 t ‖ H − 2 \tilde{\eta}_{t}=\eta_{t}\|{\bm{w}}_{t}\|^{H-2} ;

[50] p: Inner Product: 𝒘 t ⊤ ​ ∇ 𝒘 t ℓ t ​ ( 𝒘 t ) = H ​ ℓ t ​ ( 𝒘 t ) {\bm{w}}_{t}^{\top}\nabla_{{\bm{w}}_{t}}\ell_{t}({\bm{w}}_{t})=H\ell_{t}({\bm{w}}_{t}) ;

[51] p: Norm Iteration over Projected Dynamics: ‖ 𝒘 t + 1 ‖ 2 = ‖ 𝒘 t ‖ 2 ​ ( 1 + η ~ t 2 ​ ‖ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) ‖ 2 − 2 ​ H ​ η ~ t ​ ℓ t ​ ( 𝒗 t ) ) \|{\bm{w}}_{t+1}\|^{2}=\|{\bm{w}}_{t}\|^{2}(1+\tilde{\eta}_{t}^{2}\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})\|^{2}-2H\tilde{\eta}_{t}\ell_{t}({\bm{v}}_{t})) .

[52] p: Notably, the effective stepsize is normalized by the weight norm. This normalization enables the possibility of having a large stepsize while maintaining a small effective stepsize. This observation constitutes a key aspect of our analysis. We defer the proof of Lemma 1 to Appendix B.4 .

[53] p: In the context of homogeneity, the weight direction matters much rather than its precise values. This phenomenon aligns with common practices in classification, where we mainly focus on the sign of the prediction instead of its precise value. Consequently, we evaluate the population loss and empirical loss on the sphere, as outlined in ( 3 ).

[54] table: ℒ s ​ ( 𝒘 ) = ℒ ⁡ ( 𝒘 / ‖ 𝒘 ‖ ) = ℒ ⁡ ( 𝒗 ) , ℒ ^ s ​ ( 𝒘 ) = ℒ ^ ​ ( 𝒘 / ‖ 𝒘 ‖ ) = ℒ ^ ​ ( 𝒗 ) . \begin{split}\mathcal{L}^{s}({\bm{w}})&=\mathcal{L}({\bm{w}}/\|{\bm{w}}\|)=\mathcal{L}({\bm{v}}),\\ \hat{\mathcal{L}}^{s}({\bm{w}})&=\hat{\mathcal{L}}({\bm{w}}/\|{\bm{w}}\|)=\hat{\mathcal{L}}({\bm{v}}).\end{split} (3)

[55] p: Algorithmic Stability. Algorithmic stability is a popular technique for bounding generalization error by measuring an algorithm’s sensitivity to perturbations in the training data ( Bousquet and Elisseeff, 2002 ; Shalev-Shwartz et al., 2010 ; Hardt et al., 2016 ) . This paper relies on this framework to motivate our analysis. We summarize the formal definitions of uniform stability ( ϵ T \epsilon_{T} -stable) and the classic stability bounds for SGD in Appendix B.8.1 .

[56] p: Why Algorithmic Stability Requires an 𝒪 ⁡ ( 1 / t ) \mathcal{O}(1/t) Stepsize under Non-Convexity? The distinction between convex and non-convex optimization under algorithmic stability is fundamentally linked to the expansive property, as detailed in Lemma 3.6 in Hardt et al. (2016) . In the context of convex training, if the same training sample is selected (with a probability of 1 − 1 n 1-\frac{1}{n} ), the following inequality holds: ‖ 𝒘 t + 1 − 𝒘 t + 1 ′ ‖ ≤ ‖ 𝒘 t − 𝒘 t ′ ‖ \|{\bm{w}}_{t+1}-{\bm{w}}_{t+1}^{\prime}\|\leq\|{\bm{w}}_{t}-{\bm{w}}_{t}^{\prime}\| . However, in the case of non-convex training, the inequality is modified to: ‖ 𝒘 t + 1 − 𝒘 t + 1 ′ ‖ ≤ ( 1 + β ​ η t ) ​ ‖ 𝒘 t − 𝒘 t ′ ‖ \|{\bm{w}}_{t+1}-{\bm{w}}_{t+1}^{\prime}\|\leq(1+\beta\eta_{t})\|{\bm{w}}_{t}-{\bm{w}}_{t}^{\prime}\| . This modification implies that errors can accumulate over iterations in non-convex training, leading to an accumulation term ∏ t ∈ [ T ] ( 1 + β ​ η t ) ≈ exp ⁡ ( β ​ ∑ t ∈ [ T ] η t ) \prod_{t\in[T]}(1+\beta\eta_{t})\approx\exp(\beta\sum_{t\in[T]}\eta_{t}) . To ensure that this term grows polynomially with the number of iterations T T , we require that the sum of the stepsizes over the iterations is ∑ t ∈ [ T ] η t = 𝒪 ⁡ ( log ⁡ T ) \sum_{t\in[T]}\eta_{t}=\mathcal{O}(\log T) , which in turn necessitates a stepsize of η t = 𝒪 ⁡ ( 1 / t ) \eta_{t}=\mathcal{O}(1/t) .

[57] h2: 3 Generalization Under Homogeneity

[58] p: In this section, we present our main theorems, which establish the connection between homogeneity and generalization. We begin by introducing the necessary assumptions in Section 3.1 . Next, we present our main generalization bound for general H H -homogeneous neural networks in Section 3.2 . We then specialize this result to the important case of three-homogeneous neural networks in Section 3.3 . Finally, we compare the optimization performance in Section 3.4 to demonstrate the separation between different stepsize choices.

[59] h3: 3.1 Assumptions

[60] p: Before delving into the main theorem, we introduce the following assumptions concerning the loss function and the optimization process.

[61] h6: Assumption 1 (Loss Bound) .

[62] p: Assume that the individual loss is upper bounded by a constant σ ¯ 2 \bar{\sigma}^{2} on the unit sphere for any sample, namely

[63] table: sup 𝒗 : ‖ 𝒗 ‖ = 1 sup X , Y ℓ ( 𝒗 ; X , Y ) ≤ σ ¯ 2 . \sup_{{\bm{v}}:\|{\bm{v}}\|=1}\sup_{{X},{Y}}\ell({\bm{v}};{X},{Y})\leq\bar{\sigma}^{2}.

[64] p: Additionally, assume that the training loss is lower bounded by half of the Bayesian optimal during the training process, namely, for t ∈ [ 0 , T ] t\in[0,T] with a given iteration T T ,

[65] table: inf t ℒ ^ ​ ( 𝒗 t ) ≥ 1 2 ​ σ ¯ 2 . \inf_{t}\hat{\mathcal{L}}({\bm{v}}_{t})\geq\frac{1}{2}\underline{\sigma}^{2}.

[66] p: Assumption 1 provides bounds for the training loss. The upper bound is standard in related analyses, ensuring that the training procedure does not result in excessively high loss values that could lead to an unstable optimization process. The lower bound is necessary to obtain a consistent generalization bound in noisy label settings, since without which the generalization gap would not converge to zero, as demonstrated in Proposition 2 . Notably, there is a small gap here where we assume the lower bound along the trajectory, while Proposition 2 only accounts for the necessity of the lower bound on the iteration T T . We argue that this gap is mild since the training loss usually decreases.

[67] h6: Proposition 2 .

[68] p: Given the Bayesian optimal σ ¯ 2 \underline{\sigma}^{2} , for any given iteration t t , if the training loss satisfies ℒ ^ ​ ( 𝐯 t ) ≤ 1 2 ​ σ ¯ 2 \hat{\mathcal{L}}({\bm{v}}_{t})\leq\frac{1}{2}\underline{\sigma}^{2} , the corresponding generalization gap satisfies | ℒ ⁡ ( 𝐯 t ) − ℒ ^ ​ ( 𝐯 t ) | ≥ 1 2 ​ σ ¯ 2 |\mathcal{L}({\bm{v}}_{t})-\hat{\mathcal{L}}({\bm{v}}_{t})|\geq\frac{1}{2}\underline{\sigma}^{2} .

[69] h6: Assumption 2 .

[70] p: (Lipschitz, Approximately Smooth) Assume that the loss function ℓ ⁡ ( ⋅ , X , Y ) \ell(\cdot;{X},{Y}) is L L -Lipschitz on the sphere for any sample ( X , Y ) ({X},{Y}) , namely,

[71] table: sup 𝒗 : ‖ 𝒗 ‖ = 1 ∥ ∇ 𝒗 ℓ ( 𝒗 ; X , Y ) ∥ ≤ L . \sup_{{\bm{v}}:\|{\bm{v}}\|=1}\|\nabla_{{\bm{v}}}\ell({\bm{v}};{X},{Y})\|\leq L.

[72] p: Additionally, we assume that the loss function is ( γ , β ) (\gamma,\beta) -approximately smooth on the sphere for any sample ( X , Y ) ({X},{Y}) , meaning that for each ℓ ⁡ ( 𝐯 , X , Y ) \ell({\bm{v}};{X},{Y}) , there exists a globally β \beta -smooth function ℓ ¯ ​ ( 𝐯 , X , Y ) \bar{\ell}({\bm{v}};{X},{Y}) such that for each 𝐯 {\bm{v}}

[73] table: sup 𝒗 : ‖ 𝒗 ‖ = 1 ∥ ∇ 𝒗 ℓ ( 𝒗 ; X , Y ) − ∇ 𝒗 ℓ ¯ ( 𝒗 ; X , Y ) ∥ ≤ γ . \sup_{{\bm{v}}:\|{\bm{v}}\|=1}\|\nabla_{\bm{v}}\ell({\bm{v}};{X},{Y})-\nabla_{\bm{v}}\bar{\ell}({\bm{v}};{X},{Y})\|\leq\gamma.

[74] p: The Assumption 2 introduces constraints on the loss function to ensure its Lipschitz and approximate smooth properties, which are widely used in related literature ( Hardt et al., 2016 ) . Note that Assumption 2 degenerates into the standard smoothness assumption when γ = 0 \gamma=0 . We extend the previous smoothness assumption to approximate smoothness to accommodate the non-smooth behavior of ReLU activations. It is worth noting that there exist smooth activation functions that maintain homogeneity, e.g. , σ ⁡ ( ⋅ ) = ( max ⁡ { ⋅ , 0 } ) u \sigma(\cdot)=(\max\{\cdot,0\})^{u} with u > 1 u>1 , which opens up possibilities where γ = 0 \gamma=0 .

[75] h3: 3.2 Generalization Under Homogeneity

[76] p: This section provides the generalization bounds for general homogeneous neural networks. We defer the complete proof to Appendix B.2 .

[77] h6: Theorem 1 (Generalization Under Homogeneity) .

[78] p: Assume that the neural network Φ ⁡ ( 𝐰 , X ) \Phi({\bm{w}};{X}) is H H -homogeneous for any X {X} , with H > 2 H>2 . Given any fixed T > 0 T>0 , let Assumption 1 hold with loss bounds σ ¯ 2 \underline{\sigma}^{2} and σ ¯ 2 \bar{\sigma}^{2} , and Assumption 2 hold with L L -Lipschitz and ( γ , β ) (\gamma,\beta) -approximately smooth loss, where γ = o ⁡ ( T / n ) \gamma=o(T/n) . Then, there exist infinitely many stepsizes satisfying E 𝒜 , 𝒟 ​ η t = Ω ⁡ ( t H − 4 2 ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}=\Omega(t^{\frac{H-4}{2}}) , for which the generalization bound holds:

[79] table: E 𝒜 , 𝒟 ​ ℒ s ​ ( 𝐰 T ) − ℒ ^ s ​ ( 𝐰 T ) ≤ [ L ​ m 2 ] 1 m 1 + 1 ​ [ 1 + 1 m 1 ] ​ T m 1 m 1 + 1 n , \mathbb{E}_{\mathcal{A},\mathcal{D}}\mathcal{L}^{s}({\bm{w}}_{T})-\hat{\mathcal{L}}^{s}({\bm{w}}_{T})\leq\left[Lm_{2}\right]^{\frac{1}{m_{1}+1}}\left[1+\frac{1}{m_{1}}\right]\frac{T^{\frac{m_{1}}{m_{1}+1}}}{n},

[80] p: where m 1 = 4 ​ c 2 σ ¯ 2 ​ [ σ ¯ 2 + β H ] m_{1}=\frac{4c_{2}}{\underline{\sigma}^{2}}\left[\bar{\sigma}^{2}+\frac{\beta}{H}\right] and m 2 = 8 ​ c 2 H ​ σ ¯ 2 ​ [ L + γ ​ n ] m_{2}=\frac{8c_{2}}{H\underline{\sigma}^{2}}\left[L+\gamma n\right] , with constant c 2 ≥ 1 c_{2}\geq 1 related to the stepsize.

[81] p: Remark: Validity for Smaller Stepsizes. While Theorem 1 specifies stepsizes satisfying E ​ η t = Ω ⁡ ( t H − 4 2 ) \mathbb{E}\eta_{t}=\Omega(t^{\frac{H-4}{2}}) to achieve Θ ⁡ ( 1 / t ) \Theta(1/t) effective stepsizes, the generalization result remains valid for smaller stepsizes, such as Θ ⁡ ( t H − 4 2 ) \Theta(t^{\frac{H-4}{2}}) . This is because a smaller stepsize induces a smaller effective stepsize, which naturally ensures generalization, even if it may lead to slower optimization.

[82] p: Remark: Extensions of Loss Functions. The core derivation can be extended to other loss functions beyond ℓ t ​ ( z ) = max ⁡ { − Y t ​ z , 0 } \ell_{t}\left(z\right)=\max\{-{Y}_{t}z,0\} . For a general loss form ℓ t ​ ( Φ ⁡ ( 𝒘 t ) ) \ell_{t}(\Phi({\bm{w}}_{t})) with a homogeneous neural network Φ ⁡ ( 𝒘 t ) \Phi({\bm{w}}_{t}) , the effective stepsize η ~ t \tilde{\eta}_{t} is derived as

[83] table: η ~ t = ρ t ​ ‖ 𝒘 t ‖ H − 2 ​ η t , \tilde{\eta}_{t}=\rho_{t}\|{\bm{w}}_{t}\|^{H-2}\eta_{t},

[84] p: where ρ t ≜ ℓ t ′ ​ ( Φ ⁡ ( 𝒘 t ) ) / ℓ t ′ ​ ( Φ ⁡ ( 𝒗 t ) ) \rho_{t}\triangleq\ell^{\prime}_{t}(\Phi({\bm{w}}_{t}))/{\ell^{\prime}_{t}(\Phi({\bm{v}}_{t}))} . Notably, the effective stepsize in Lemma 1 is a specific case with ρ t = 1 \rho_{t}=1 . For the hinge loss ℓ t ​ ( z ) = max ⁡ { 0 , 1 − Y t ​ z } \ell_{t}(z)=\max\{0,1-{Y}_{t}z\} , we assume that the zero-loss sets { 𝒘 t : ℓ ⁡ ( Φ ⁡ ( 𝒘 t ) ) = 0 } \{{\bm{w}}_{t}:\ell(\Phi({\bm{w}}_{t}))=0\} and { 𝒗 t : ℓ ⁡ ( Φ ⁡ ( 𝒗 t ) ) = 0 } \{{\bm{v}}_{t}:\ell(\Phi({\bm{v}}_{t}))=0\} approximately overlap. This implies the ratio ρ t = ℓ t ′ ​ ( Φ ⁡ ( 𝒘 t ) ) / ℓ t ′ ​ ( Φ ⁡ ( 𝒗 t ) ) = 1 \rho_{t}=\ell^{\prime}_{t}(\Phi({\bm{w}}_{t}))/\ell^{\prime}_{t}(\Phi({\bm{v}}_{t}))=1 and the property is preserved whenever ℓ t ​ ( Φ ⁡ ( 𝒘 t ) ) ≠ 0 \ell_{t}(\Phi({\bm{w}}_{t}))\neq 0 and ℓ t ​ ( Φ ⁡ ( 𝒗 t ) ) ≠ 0 \ell_{t}(\Phi({\bm{v}}_{t}))\neq 0 . We next provide in Corollary 1 a relaxed version of Theorem 1 regarding the loss form.

[85] h6: Corollary 1 .

[86] p: Under the assumptions of Theorem 1 , if the loss function ℓ ⁡ ( ⋅ ) \ell(\cdot) satisfies 0 < ρ t = ℓ t ′ ​ ( Φ ⁡ ( 𝐰 t ) ) / ℓ t ′ ​ ( Φ ⁡ ( 𝐯 t ) ) ≤ k 1 0<\rho_{t}=\ell_{t}^{\prime}(\Phi({\bm{w}}_{t}))/\ell_{t}^{\prime}(\Phi({\bm{v}}_{t}))\allowbreak\leq k_{1} with constant k 1 ≥ 1 k_{1}\geq 1 , and z ​ ℓ t ′ ​ ( z ) ≤ k 2 ​ ℓ t ​ ( z ) z\ell^{\prime}_{t}(z)\leq k_{2}\ell_{t}(z) with constant k 2 > 0 k_{2}>0 uniformly for all t ∈ [ T ] t\in[T] , the generalization bound in Theorem 1 remains valid with modified constants:

[87] table: m 1 = 4 ​ c 2 ​ k 1 σ ¯ 2 ​ [ k 1 ​ k 2 ​ σ ¯ 2 + β H ] , m 2 = 8 ​ c 2 ​ k 1 H ​ σ ¯ 2 ​ ( L + γ ​ n ) . m_{1}=\frac{4c_{2}k_{1}}{\underline{\sigma}^{2}}\left[k_{1}k_{2}\bar{\sigma}^{2}+\frac{\beta}{H}\right],\quad m_{2}=\frac{8c_{2}k_{1}}{H\underline{\sigma}^{2}}(L+\gamma n).

[88] p: Notably, these conditions can be satisfied by many homogeneous loss functions, including ℓ t ​ ( z ) = ( max ⁡ { − Y t ​ z , 0 } ) u \ell_{t}(z)=(\max\{-{Y}_{t}z,0\})^{u} with u ≥ 1 u\geq 1 .

[89] p: Comparison with T / n T/n -type Bound. Under reasonable assumptions, one can construct T / n T/n -type generalization bounds via algorithmic stability. The intuition is that for small iteration T T , the difference between S S and S ′ S^{\prime} is selected with probability T / n T/n ( Hardt et al., 2016 ) . However, this type of bound remains valid only when T = o ⁡ ( n ) T=o(n) , indicating that not all samples are utilized during training. Clearly, this does not accurately reflect real-world scenarios. As for the results in Theorem 1 , when L L , H H , β \beta , σ ¯ 2 \bar{\sigma}^{2} , and σ ¯ 2 \underline{\sigma}^{2} are all on a constant scale, the bound is approximately of order γ ~ 1 m 1 + 1 ​ [ T / n ] m 1 m 1 + 1 \tilde{\gamma}^{\frac{1}{m_{1}+1}}[T/n]^{\frac{m_{1}}{m_{1}+1}} , where γ ~ = max ⁡ { γ , 1 / n } \tilde{\gamma}=\max\{\gamma,1/n\} . Notably, this new bound remains consistent when setting T = o ⁡ ( n / γ ~ 1 / m 1 ) T=o(n/\tilde{\gamma}^{1/m_{1}}) , allowing for multiple uses of each sample during the training process.

[90] h3: 3.3 Generalization Under Three-Homogeneity

[91] p: This section specializes the general bound in Theorem 1 to three-homogeneous neural networks (Corollary 2 ). We focus on this specific case for two main reasons: (a) setting H = 3 H=3 could yield the stepsize E 𝒜 , 𝒟 ​ η t = Ω ⁡ ( 1 / t ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}=\Omega(1/\sqrt{t}) , a rate that commonly appears in theoretical analysis ( Nemirovski et al., 2009 ) ; and (b) three-homogeneous neural networks themselves are widely adopted in practice, such as VGG19 ( Simonyan and Zisserman, 2014 ) . This alignment is somewhat surprising since the above two reasons are independent. We leave further discussion on this alignment for future work.

[92] figure: (a) (b) Figure 2 : (left) Training accuracy of SGD with different schedulers over a three-layer ReLU network. The initial learning rate is selected via grid search over { 10 − 5 , 10 − 4 , ⋯ , 10 1 } \{10^{-5},10^{-4},\cdots,10^{1}\} . SGD with stepsize Θ ⁡ ( 1 / t ​ ‖ 𝒘 t ‖ ) \Theta(1/t\|{\bm{w}}_{t}\|) achieves similar training accuracy as SGD with stepsize Θ ⁡ ( 1 / t ) \Theta(1/\sqrt{t}) , both outperforming SGD with stepsize Θ ⁡ ( 1 / t ) \Theta(1/t) ; (right) When T a = o ⁡ ( n / γ ~ 1 / m 1 ) T_{a}=o(n/\tilde{\gamma}^{1/m_{1}}) , the training and test loss curve does not decrease at t ∈ ( T a , o ⁡ ( n / γ ~ 1 / m 1 ) ) t\in(T_{a},o(n/\tilde{\gamma}^{1/m_{1}})) .

[93] h6: Corollary 2 .

[94] p: Consider a three-homogeneous neural network as constructed in Proposition 1 with H = 3 H=3 . Let T a T_{a} denote the iteration at which the training error achieves a non-zero Bayesian optimal value 2 2 2 Here we allow for an o ⁡ ( 1 ) o(1) relaxation. , namely,

[95] table: T a = arg ​ min t { E 𝒜 , 𝒟 ℒ ^ ( 𝐯 t ) ≤ σ ¯ 2 } , T_{a}=\argmin_{t}\left\{\mathbb{E}_{\mathcal{A},\mathcal{D}}\hat{\mathcal{L}}({\bm{v}}_{t})\leq\underline{\sigma}^{2}\right\},

[96] p: where we omit the dependency on stepsize and dataset for simplicity. Let Assumption 1 and Assumption 2 hold with ( γ , β ) (\gamma,\beta) -approximately smooth loss, where γ = o ⁡ ( T a / n ) \gamma=o(T_{a}/n) . Then, there exist infinitely many stepsizes satisfying E 𝒜 , 𝒟 η t = Ω ( t − 1 / 2 ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}=\Omega(t^{-1/2}) , such that if T a = o ⁡ ( n / γ ~ 1 / m 1 ) T_{a}=o(n/\tilde{\gamma}^{1/m_{1}}) , where γ ~ = max ⁡ { γ , 1 / n } \tilde{\gamma}=\max\{\gamma,1/n\} and m 1 m_{1} denote a constant related to loss bound and smoothness, it holds that

[97] table: lim n → ∞ E 𝒜 , 𝒟 ​ ℒ s ​ ( 𝐯 T a ) = σ ¯ 2 . \lim_{n\to\infty}\mathbb{E}_{\mathcal{A},\mathcal{D}}\mathcal{L}^{s}({\bm{v}}_{T_{a}})=\underline{\sigma}^{2}.

[98] p: Corollary 2 demonstrates that the generalization gap would be small within o ⁡ ( n / γ ~ 1 / m 1 ) o(n/\tilde{\gamma}^{1/m_{1}}) iterations. Therefore, if the training loss achieves the Bayesian optimal within o ⁡ ( n / γ ~ 1 / m 1 ) o(n/\tilde{\gamma}^{1/m_{1}}) iterations, the corresponding test loss would also achieve the Bayesian optimal value. Additionally, o ⁡ ( n / γ ~ 1 / m 1 ) o(n/\tilde{\gamma}^{1/m_{1}}) enables multiple uses of each sample during the training given γ = o ⁡ ( 1 ) \gamma=o(1) , which is rarely achieved in previous works with a similar order of stepsize ( Lei and Tang, 2021 ; Lei, 2023 ) .

[99] p: The Role of Normalization. Doubts might arise regarding whether the results in Corollary 2 suggest that a three-layer MLP suffices in real-world scenarios, potentially rendering deeper architectures obsolete. To address this, we emphasize the pivotal role that normalization layers play. The significance lies in two key aspects. Firstly, they introduce non-linearity, effectively reducing approximation errors. Secondly, increasing the depth of a network might facilitate the optimization process ( Arora et al., 2018a ) , leading to faster attainment of Bayesian optimality in training error (smaller T a T_{a} ).

[100] p: Loss Curve. One can observe from Theorem 1 that the generalization gap remains within o ⁡ ( 1 ) o(1) for cases where T = o ⁡ ( n / γ ~ 1 / m 1 ) T=o(n/\tilde{\gamma}^{1/m_{1}}) . This observation implies that if T a T_{a} is relatively small, indicating a fast convergence of the training loss to its Bayesian optimal, it cannot sustain this decrease until the point where T T reaches Θ ⁡ ( n / γ ~ 1 / m 1 ) \Theta(n/\tilde{\gamma}^{1/m_{1}}) . Otherwise, such a trend would result in a test error smaller than the Bayesian optimal, which is impossible. We refer to Figure 2 (right) for an illustration. This phenomenon is empirically observed in Wen et al. (2023) .

[101] h3: 3.4 Additional Discussions on Optimization Performance

[102] p: This section demonstrates a separation in optimization performance between the stepsize in this paper and those in prior works. Following the setting H = 3 H=3 in Section 3.3 , we prove that a stepsize of order E 𝒜 , 𝒟 ​ η t = Ω ⁡ ( 1 / t ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}=\Omega(1/\sqrt{t}) potentially optimizes better compared to E 𝒜 , 𝒟 ​ η t = 𝒪 ⁡ ( 1 / t ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}=\mathcal{O}(1/t) . For convenience of discussion, we consider the class of stepsizes that could eliminate the randomness of the corresponding effective stepsize. The result is provided in Theorem 2 .

[103] h6: Theorem 2 .

[104] p: (Separation Between Stepsize Ω ⁡ ( 1 / t ) \Omega(1/\sqrt{t}) and 𝒪 ⁡ ( 1 / t ) \mathcal{O}(1/t) ) Under the settings of Theorem 1 with H = 3 H=3 , assume that the individual loss function ℓ i ​ ( ⋅ ) = ℓ ⁡ ( ⋅ , X i , Y i ) \ell_{i}(\cdot)=\ell(\cdot;{X}_{i},{Y}_{i}) on the sphere ( ‖ 𝐯 ‖ = 1 \|{\bm{v}}\|=1 ) satisfies

[105] p: 1. Smoothness: ‖ ∇ 𝐯 1 ℓ i ​ ( 𝐯 1 ) − ∇ 𝐯 2 ℓ i ​ ( 𝐯 2 ) ‖ ≤ β ​ ‖ 𝐯 1 − 𝐯 2 ‖ \|\nabla_{{\bm{v}}_{1}}\ell_{i}({\bm{v}}_{1})-\nabla_{{\bm{v}}_{2}}\ell_{i}({\bm{v}}_{2})\|\leq\beta\|{\bm{v}}_{1}-{\bm{v}}_{2}\| ;

[106] p: 2. PL condition: 1 2 ​ ‖ ∇ 𝐯 ℓ i ​ ( 𝐯 ) ‖ 2 ≥ μ ⁡ ( ℓ i ​ ( 𝐯 ) − min 𝐯 ⁡ ℓ i ​ ( 𝐯 ) ) \frac{1}{2}\|\nabla_{{\bm{v}}}\ell_{i}({\bm{v}})\|^{2}\geq\mu(\ell_{i}({\bm{v}})-\min_{\bm{v}}\ell_{i}({\bm{v}})) ;

[107] p: 3. Strong growth: max i ∈ [ n ] ⁡ { ‖ ∇ 𝐯 ℓ i ​ ( 𝐯 ) ‖ } ≤ B ​ ‖ ∇ 𝐯 ℒ ^ ​ ( 𝐯 ) ‖ \max_{i\in[n]}\{\|\nabla_{{\bm{v}}}\ell_{i}({\bm{v}})\|\}\leq B\|\nabla_{\bm{v}}\hat{\mathcal{L}}({\bm{v}})\| ;

[108] p: 4. E I ​ ℒ ^ ​ ( 𝐯 t ) ≥ ( 1 + α ) / α ​ ℒ ^ ​ ( 𝐯 ∗ ) \mathbb{E}_{I}\hat{\mathcal{L}}({\bm{v}}_{t})\geq(1+\alpha)/\alpha\hat{\mathcal{L}}({\bm{v}}^{*}) ,

[109] p: then for SGD with E 𝒜 ​ ‖ 𝐰 0 ‖ 2 = 𝒪 ⁡ ( 1 ) \mathbb{E}_{\mathcal{A}}\|{\bm{w}}_{0}\|^{2}=\mathcal{O}(1) and η ~ t ≤ min ⁡ { 1 β ​ B 2 , H ​ σ ¯ 2 2 ​ L 2 } \tilde{\eta}_{t}\leq\min\{\frac{1}{\beta B^{2}},\allowbreak\frac{H\underline{\sigma}^{2}}{2L^{2}}\} , if μ > 4 ​ B 2 ​ H 2 ​ σ ¯ 2 ​ ( 1 + α ) \mu>4B^{2}H^{2}\bar{\sigma}^{2}(1+\alpha) , it holds that for some given constant c > 0 c>0 ,

[110] p: For learning rates satisfying E 𝒜 , 𝒟 ​ η t = Ω ⁡ ( 1 / t ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}=\Omega(1/\sqrt{t}) used in Theorem 1 , the convergence rate would be

[111] table: E 𝒜 , 𝒟 ​ ℒ ^ ​ ( 𝐯 T ) − min 𝐯 ⁡ ℒ ^ ​ ( 𝐯 ) ≤ E 𝒜 , 𝒟 ​ ( ℒ ^ ​ ( 𝐯 0 ) − min 𝐯 ⁡ ℒ ^ ​ ( 𝐯 ) ) T c ​ λ , \mathbb{E}_{\mathcal{A},\mathcal{D}}\hat{\mathcal{L}}({\bm{v}}_{T})-\min_{\bm{v}}\hat{\mathcal{L}}({\bm{v}})\leq\frac{\mathbb{E}_{\mathcal{A},\mathcal{D}}(\hat{\mathcal{L}}({\bm{v}}_{0})-\min_{\bm{v}}\hat{\mathcal{L}}({\bm{v}}))}{T^{c\lambda}},

[112] p: There exist infinitely many learning rates satisfying E 𝒜 , 𝒟 ​ η t = 𝒪 ⁡ ( 1 / t ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}=\mathcal{O}(1/t) , leading to the convergence rate

[113] table: E 𝒜 , 𝒟 ​ ℒ ^ ​ ( 𝐯 T ) − min 𝐯 ⁡ ℒ ^ ​ ( 𝐯 ) ≤ E 𝒜 , 𝒟 ​ ( ℒ ^ ​ ( 𝐯 0 ) − min 𝐯 ⁡ ℒ ^ ​ ( 𝐯 ) ) [ log ⁡ T ] c ​ λ . \mathbb{E}_{\mathcal{A},\mathcal{D}}\hat{\mathcal{L}}({\bm{v}}_{T})-\min_{\bm{v}}\hat{\mathcal{L}}({\bm{v}})\leq\frac{\mathbb{E}_{\mathcal{A},\mathcal{D}}(\hat{\mathcal{L}}({\bm{v}}_{0})-\min_{\bm{v}}\hat{\mathcal{L}}({\bm{v}}))}{[\log T]^{c\lambda}}.

[114] p: where λ = μ B 2 − 4 ​ H 2 ​ σ ¯ 2 ​ ( 1 + α ) \lambda=\frac{\mu}{B^{2}}-4H^{2}\bar{\sigma}^{2}(1+\alpha) .

[115] p: Theorem 2 establishes a separation between the effects of different stepsizes during the optimization process. It asserts that there are certain training landscapes for which an optimization algorithm with stepsize Ω ⁡ ( 1 / t ) \Omega(1/\sqrt{t}) achieves a significantly better convergence rate compared to one with stepsize 𝒪 ⁡ ( 1 / t ) \mathcal{O}(1/t) . The PL condition is used to ensure convergence, while the strong growth condition is utilized to enhance the convergence rate of SGD. Notably, this result pertains to optimization performance, distinguishing it from prior works that apply the PL condition to derive generalization results via algorithmic stability. We provide the proof in Appendix B.5 .

[116] h6: Example 3 (Compatibility between Optimization and Generalization) .

[117] p: Consider the 3-homogeneous loss function:

[118] table: ℓ ⁡ ( 𝒗 ) = ( v 1 2 + 2 ​ v 2 2 ) 3 / 2 . \ell({\bm{v}})=(v_{1}^{2}+2v_{2}^{2})^{3/2}.

[119] p: This case illustrates that the optimization guarantees in Theorem 2 and the generalization requirements in Corollary 2 can be satisfied simultaneously. In the unit sphere, this loss satisfies the required regularity conditions with σ ¯ 2 = 1 ≤ ℓ ⁡ ( 𝐯 ) ≤ 2 3 / 2 = σ ¯ 2 \underline{\sigma}^{2}=1\leq\ell({\bm{v}})\leq 2^{3/2}=\bar{\sigma}^{2} , L = 6 ​ 2 L=6\sqrt{2} , γ = 0 \gamma=0 , β = 12 ​ 2 \beta=12\sqrt{2} and μ ≈ 19.7 \mu\approx 19.7 . Without affecting asymptotic behavior, relax the definition of hitting time in Corollary 2 to

[120] table: T a ​ ( τ ⁡ ( n ) ) = min ⁡ { t : E ​ ℒ ^ ​ ( 𝐯 t ) ≤ σ ¯ 2 + τ ⁡ ( n ) } T_{a}(\tau(n))=\min\{t:\mathbb{E}\hat{\mathcal{L}}({\bm{v}}_{t})\leq\underline{\sigma}^{2}+\tau(n)\}

[121] p: for some τ ⁡ ( n ) → 0 \tau(n)\rightarrow 0 . Theorem 2 implies ℓ ⁡ ( 𝐯 T ) − σ ¯ 2 = 𝒪 ⁡ ( T − c ​ μ ) \ell({\bm{v}}_{T})-\underline{\sigma}^{2}=\mathcal{O}(T^{-c\mu}) , which yields T a ≤ τ ( n ) − 1 / c μ T_{a}\leq\tau(n)^{-1/c\mu} for a constant c c . To satisfy the generalization requirement T a = o ⁡ ( n / γ ~ 1 / m 1 ) T_{a}=o(n/\tilde{\gamma}^{1/m_{1}}) with γ ~ = 1 / n \tilde{\gamma}=1/n , we can choose

[122] table: τ ⁡ ( n ) = n − c ​ μ ​ ( 1 + ϵ / m 1 ) \tau(n)=n^{-c\mu(1+\epsilon/m_{1})}

[123] p: for some ϵ ∈ ( 0 , 1 ) \epsilon\in(0,1) . This ensures T a ≤ n 1 + ϵ / m 1 = o ⁡ ( n 1 + 1 / m 1 ) T_{a}\leq n^{1+\epsilon/m_{1}}=o(n^{1+1/m_{1}}) . This argument naturally extends to ℓ ⁡ ( 𝐯 ) = ( v 1 2 + 2 ​ Σ i = 2 D ​ x i 2 ) 3 / 2 \ell({\bm{v}})=(v_{1}^{2}+2\Sigma_{i=2}^{D}x_{i}^{2})^{3/2} .

[124] h2: 4 Generalization Beyond Lipschitz

[125] p: This section demonstrates that the stepsize regime in Theorem 1 ensures generalization even without the Lipschitz assumption. The analysis proceeds by first defining a stability metric and establishing its relationship with generalization in Section 4.1 , subsequently deriving the non-Lipschitz generalization bound in Section 4.2 .

[126] h3: 4.1 Stability and Generalization

[127] p: This section starts from the definition of the conditional on-average stability, adapted from the on-average model stability ( Lei and Ying, 2020 ) in Appendix B.8.2 .

[128] h6: Definition 2 (Conditional On-Average Stability) .

[129] p: Let S = { z 1 , … , z n } S=\{z_{1},\dots,z_{n}\} and S ( i ) = { z 1 , … , z i ′ , … , z n } S^{(i)}=\{z_{1},\dots,\allowbreak z^{\prime}_{i},\dots,\allowbreak z_{n}\} be two datasets differing only at the i i -th index, where z i ≜ ( X i , Y i ) z_{i}\triangleq({X}_{i},{Y}_{i}) . 𝐯 T {\bm{v}}_{T} and 𝐯 T ( i ) {\bm{v}}_{T}^{(i)} are trained on S S and S ( i ) S^{(i)} over T T iterations, respectively. For any given t 0 ∈ [ T ] t_{0}\in[T] , let ℰ ( i ) \mathcal{E}_{(i)} be the event that the index i i is not selected during the first t 0 t_{0} iterations. The algorithm 𝒜 \mathcal{A} is said to be ϵ stab \epsilon_{\text{stab}} -conditionally stable on average if:

[130] table: ϵ avg , T | t 0 2 ≜ 1 n ​ ∑ i = 1 n E 𝒜 , 𝒟 ​ [ ‖ 𝐯 T − 𝐯 T ( i ) ‖ 2 ∣ ℰ ( i ) ] ≤ ϵ stab . \epsilon^{2}_{\text{avg},T\mid t_{0}}\triangleq\frac{1}{n}\sum_{i=1}^{n}\mathbb{E}_{\mathcal{A},\mathcal{D}}\left[\|{\bm{v}}_{T}-{\bm{v}}_{T}^{(i)}\|^{2}\mid\mathcal{E}_{(i)}\right]\leq\epsilon_{\text{stab}}.

[131] p: The following Lemma 2 connects the generalization gap to the conditional on-average stability. We focus on the setting where γ = 0 \gamma=0 . Notably, the assumptions of homogeneity and β \beta -smoothness can hold simultaneously, e.g. , with the loss ℓ t ​ ( z ) = ( max ⁡ { − Y t ​ z , 0 } ) 2 \ell_{t}(z)=(\max\{-{Y}_{t}z,0\})^{2} and activation σ ⁡ ( ⋅ ) = max ⁡ { 0 , ⋅ } 2 \sigma(\cdot)=\max\{0,\cdot\}^{2} .

[132] h6: Lemma 2 .

[133] p: Under Bounded Loss (Assumption 1 ) and β \beta -smoothness, for any t 0 > 0 t_{0}>0 and ζ > 0 \zeta>0 , the generalization bound holds:

[134] table: E 𝒜 , 𝒟 ​ [ ℒ s ​ ( 𝐰 T ) − ℒ ^ s ​ ( 𝐰 T ) ] ≤ ( t 0 n + β ζ ) ​ σ ¯ 2 + β + ζ 2 ​ ϵ avg , T | t 0 2 , \mathbb{E}_{\mathcal{A},\mathcal{D}}[\mathcal{L}^{s}({\bm{w}}_{T})-\hat{\mathcal{L}}^{s}({\bm{w}}_{T})]\leq\left(\frac{t_{0}}{n}+\frac{\beta}{\zeta}\right)\bar{\sigma}^{2}+\frac{\beta+\zeta}{2}\epsilon^{2}_{\text{avg},T\mid t_{0}},

[135] p: where ζ \zeta is a free parameter. The proof is deferred to Appendix B.7.1 .

[136] h3: 4.2 Generalization Beyond Lipschitz

[137] p: This section derives the generalization bounds without the Lipschitz assumption.

[138] h6: Theorem 4 (Generalization Beyond Lipschitz) .

[139] p: Given any fixed T > 0 T>0 , let Bounded Loss (Assumption 1 ) and β \beta -smoothness hold. Then, for an H H -homogeneous network ( H > 2 H>2 ) and the stepsize regime in Theorem 1 , the generalization gap satisfies:

[140] table: E 𝒜 , 𝒟 ​ [ ℒ s ​ ( 𝐰 T ) − ℒ ^ s ​ ( 𝐰 T ) ] = 𝒪 ⁡ ( n − m 1 ′ + 2 m 1 ′ + 3 ​ 𝒦 T 1 m 1 ′ + 3 ​ T m 1 ′ m 1 ′ + 3 ) , \mathbb{E}_{\mathcal{A},\mathcal{D}}[\mathcal{L}^{s}({\bm{w}}_{T})-\hat{\mathcal{L}}^{s}({\bm{w}}_{T})]=\mathcal{O}\left(n^{-\frac{m^{\prime}_{1}+2}{m^{\prime}_{1}+3}}\mathcal{K}_{T}^{\frac{1}{m^{\prime}_{1}+3}}T^{\frac{m^{\prime}_{1}}{m^{\prime}_{1}+3}}\right),

[141] p: where 𝒦 T = 1 + T / n \mathcal{K}_{T}=1+T/n and m 1 ′ = 8 ​ c 2 ​ σ ¯ 2 σ ¯ 2 + 4 ​ c 2 ​ β H ​ σ ¯ 2 m^{\prime}_{1}=8\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}+\frac{4c_{2}\beta}{H\underline{\sigma}^{2}} .

[142] p: Notably, this bound still supports multi-pass training. We defer the proof to Appendix B.7.2 .

[143] p: Remark: Comparison of Bounds. Theorem 4 removes the Lipschitz requirement in Assumption 2 , better reflecting practical scenarios. Interestingly, despite this relaxation, it sometimes yields a faster growth in the iteration upper bound compared to that in Theorem 1 . Specifically, it supports T = o ⁡ ( n 1 + 2 / ( m 1 ′ + 1 ) ) T=o(n^{1+2/(m^{\prime}_{1}+1)}) while ensuring generalization, which surpasses o ⁡ ( n 1 + 1 / m 1 ) o(n^{1+1/m_{1}}) when 4 ​ c 2 ​ β > σ ¯ 2 ​ H 4c_{2}\beta>\underline{\sigma}^{2}H , allowing for more training epochs. This improvement potentially stems from the different stability metrics utilized. It reveals that, in our setting, uniform stability may contain redundancy relative to the Assumptions 1 and 2 . We leave the application of our stepsize regime to other stability metrics for further exploration.

[144] h2: 5 Conclusion

[145] p: In this paper, we establish generalization bounds for homogeneous neural networks. We prove in Theorem 1 that for H H -homogeneous neural networks, there exist stepsizes of order Ω ⁡ ( t H − 4 2 ) \Omega(t^{\frac{H-4}{2}}) that ensure generalization via algorithmic stability. This is grounded in the observation that while the stepsize may be large, its effective stepsize on the unit sphere might be considerably small. Applying the main result to the specific case of H = 3 H=3 , Corollary 2 establishes generalization for stepsizes of order Ω ⁡ ( 1 / t ) \Omega(1/\sqrt{t}) , relaxing the previous requirement of 𝒪 ⁡ ( 1 / t ) \mathcal{O}(1/t) . Our results also extend to a broader range of loss functions, activation functions, and architectures, as detailed in Corollary 1 and Proposition 1 . Besides, we provide in Theorem 2 an optimization result on the separation between stepsize 𝒪 ⁡ ( 1 / t ) \mathcal{O}(1/t) and stepsize Ω ⁡ ( 1 / t ) \Omega(1/\sqrt{t}) . Furthermore, we strengthen our framework in Section 4 by deriving non-Lipschitz generalization bounds, better aligning our theory with real-world scenarios. Overall, our findings highlight homogeneity as a helpful property that enhances algorithmic stability, yielding benefits in both generalization and optimization.

[146] h2: References

[147] p: Appendix

[148] h2: Appendix A Additional Discussions

[149] p: This appendix provides additional discussion in Section A.1 on algorithmic stability and generalization analysis to complement Section 1.2 . Subsequently, Section A.2 offers a detailed explanation and visualization of the homogeneous neural network construction introduced in Proposition 1 .

[150] h3: A.1 Additional Related Work

[151] p: Algorithmic Stability. Algorithmic stability is a prominent generalization technique that may generalize to a broader range of loss functions and models in multi-pass settings ( Bousquet and Elisseeff, 2002 ; Feldman and Vondrák, 2019 ; Bousquet et al., 2020 ; Bassily et al., 2020 ; Teng et al., 2022 ; Yang et al., 2024 ) . This argument shows that if the model and the training method are not overly sensitive to data perturbations, the generalization error can be effectively bounded. It is provably effective under Lipschitz, convex, and smooth regimes ( Hardt et al., 2016 ; Asi et al., 2021 ; Zhang et al., 2025 ) . There is a line of work focusing on relaxing the constraints of Lipschitz condition ( Lei and Ying, 2020 ; Arora et al., 2022 ; Nikolakakis et al., 2022 ) and smoothness ( Yang et al., 2021 ; Wang et al., 2022 ; Lowy and Razaviyayn, 2023 ) .

[152] p: Generalization in Stochastic Optimization. Generalization in stochastic optimization has been thoroughly studied ( Shalev-Shwartz et al., 2010 ) , across various scenarios such as one-pass SGD ( Pillaud-Vivien et al., 2018a ; Lugosi and Nualart, 2024 ) , multi-pass SGD ( Pillaud-Vivien et al., 2018b ; Sekhari et al., 2021 ; Lei et al., 2021 ) , DPSGD ( Bassily et al., 2019 ; Ma et al., 2022 ) , and ERM solutions ( Feldman, 2016 ; Aubin et al., 2020 ) . Early research primarily focused on gradient descent in convex learning problems ( Amir et al., 2021 ) , where generalization can be bounded by uniform convergence ( Bartlett et al., 2017 ; Nagarajan and Kolter, 2019 ; Wei and Ma, 2020 ; Glasgow et al., 2023 ) . However, this approach struggles in high-dimensional spaces and can be inadequate ( Shalev-Shwartz et al., 2010 ; Feldman, 2016 ) . An alternative is online-to-batch conversion ( Nemirovskij and Yudin, 1983 ) , which mitigates the high-dimensional challenge and achieves minimax sample complexity, but it is limited to single-pass training, whereas in practice, longer training often results in better generalization ( Hoffer et al., 2017 ) . Recent works aim to close this gap by bounding generalization in multi-pass settings ( Soudry et al., 2018 ; Li et al., 2021 ; Lyu et al., 2021 ; Sekhari et al., 2021 ) , showing that gradient descent benefits from implicit bias. However, characterizing this implicit bias for more complex models remains an open problem. In addition to uniform convergence and implicit bias, various other approaches to generalization have been proposed, including PAC-Bayes ( McAllester, 1999 ; Dziugaite and Roy, 2017 ; Haddouche et al., 2021 ; Lotfi et al., 2022 ) , information-theoretic methods ( Russo and Zou, 2016 ; Xu and Raginsky, 2017 ; Negrea et al., 2019 ; Haghifam et al., 2020 ; Haghifam et al., 2022 ; Haghifam et al., 2023 ; Lugosi and Neu, 2022 ) , compression-based techniques ( Arora et al., 2018b ; Hsu et al., 2021 ) , and benign overfitting ( Bartlett et al., 2020 ; Zou et al., 2021 ; Koren et al., 2022 ; Xu et al., 2022 ; Wen et al., 2023 ) . Notably, as one of the most fundamental issues in machine learning theory, generalization theory focuses on the mechanism of deep learning, distinguishing itself from practical approaches such as validation tricks ( Zhang et al., 2021 ; Chatterjee and Zielinski, 2022 ) .

[153] h3: A.2 Detailed Construction and Visualization of H H -Homogeneous Networks

[154] p: First, we detail the underlying operations for the linear connections constructed in Proposition 1 . For an unnormalized layer, we define 𝒰 𝒘 ​ ( a ) ≜ 𝒘 ​ σ u ​ ( a ) \mathcal{U}_{\bm{w}}(a)\triangleq{\bm{w}}\sigma_{u}(a) . Here, a a denotes the input vector (the output of the previous layer), 𝒘 {\bm{w}} represents the weight matrix of the current layer, and σ u ​ ( ⋅ ) \sigma_{u}(\cdot) is an element-wise activation function. This operation proceeds by activating a a followed by matrix multiplication with 𝒘 {\bm{w}} . In contrast, the normalized layer 𝒩 𝒘 ​ ( a ) ≜ 𝒘 ‖ 𝒘 ‖ ​ σ n ​ ( a ) \mathcal{N}_{\bm{w}}(a)\triangleq\frac{{\bm{w}}}{\|{\bm{w}}\|}\sigma_{n}(a) incorporates an additional normalization step for 𝒘 {\bm{w}} prior to multiplication. This can be implemented either by dividing 𝒘 {\bm{w}} directly by its Frobenius norm or by normalizing each row independently. While both approaches ensure 0-homogeneity, they differ in signal propagation: the latter maintains the input’s scale, whereas the former significantly attenuates the output scale relative to the layer’s dimensions.

[155] p: Next, We provide a visualization for the specific case with H = 3 H=3 to illustrate our construction. This case is of particular interest as it leads to the Ω ⁡ ( 1 / t ) \Omega(1/\sqrt{t}) stepsize regime discussed in Corollary 2 .

[156] p: As shown in Figure 3 , the architecture is decoupled into two segments:

[157] p: Normalized: The initial h − 3 h-3 layers utilize normalization 𝒩 𝒘 \mathcal{N}_{\bm{w}} to ensure 0 0 -homogeneity, allowing for complex architectural features such as skip-connections or diverse activations without increasing the overall degree of the network.

[158] p: Unnormalized: The final 3 3 layers are unnormalized 𝒰 𝒘 \mathcal{U}_{\bm{w}} , which collectively contribute a degree of H = 3 H=3 to the network output.

[159] figure: (a) (b) Figure 3 : An instance of construction for H = 3 H=3 . Following the rules in Proposition 1 , normalized layers (left) accomodate arbitrary activations and connections with 0 0 -homogeneity, while the subsequent unnormalized layers (right) compose a 3 3 -layer MLP to achieve the desired three-homogeneity.

[160] h2: Appendix B Theoretical Results

[161] p: In this appendix, we organize the theoretical results as follows: Section B.1 details the notations used throughout the paper. Section B.2 presents the proofs and further discussions of the main results in Theorem 1 . Section B.3 provides the proof for the relaxation of the loss form as shown in Corollary 1 . Section B.4 establishes the foundational analysis of the effective stepsize in Lemma 1 . Section B.5 proves the optimization separation result between different stepsizes in Theorem 2 . Section B.6 analyzes the weight norm iteration under both Lipschitz and non-Lipschitz conditions. Finally, Section B.7 provides the detailed proofs for the non-Lipschitz results discussed in Section 4 .

[162] h3: B.1 Notations

[163] figure: Table 2 : Summary of Notations Symbol Description Model Φ ⁡ ( 𝒘 , X ) \Phi({\bm{w}};{X}) Neural network function Φ ⁡ ( ⋅ , ⋅ ) \Phi(\cdot;\cdot) with weights 𝒘 {\bm{w}} and input X {X} f 𝒘 ​ ( ⋅ ) f_{\bm{w}}(\cdot) Equivalent notation to Φ ⁡ ( 𝒘 , ⋅ ) \Phi({\bm{w}};\cdot) H H Degree of positive homogeneity of the neural network Φ \Phi 𝒘 t {\bm{w}}_{t} Weight vector at iteration t t 𝒗 t {\bm{v}}_{t} Direction of weight (normalized weight), defined as 𝒗 t = 𝒘 t / ‖ 𝒘 t ‖ {\bm{v}}_{t}={\bm{w}}_{t}/\|{\bm{w}}_{t}\| Optimization S S Training dataset, a realization of 𝒫 \mathcal{P} η t \eta_{t} Stepsize (learning rate) in SGD updates η ~ t \tilde{\eta}_{t} Effective stepsize governing dynamics on the unit sphere, η ~ t = ρ t ​ ‖ 𝒘 t ‖ H − 2 ​ η t \tilde{\eta}_{t}=\rho_{t}\|{\bm{w}}_{t}\|^{H-2}\eta_{t} ρ t \rho_{t} Gradient alignment ratio, defined as ρ t = ℓ t ′ ​ ( Φ ⁡ ( 𝒘 t ) ) / ℓ t ′ ​ ( Φ ⁡ ( 𝒗 t ) ) \rho_{t}=\ell^{\prime}_{t}(\Phi({\bm{w}}_{t}))/{\ell^{\prime}_{t}(\Phi({\bm{v}}_{t}))} T T Total number of training iterations n n Sample size of the training dataset [ n ] [n] The set { 1 , 2 , ⋯ , n } \{1,2,\cdots,n\} Loss and Generalization 𝒫 \mathcal{P} Joint distribution of feature-response pair 𝒟 , 𝒜 \mathcal{D},\mathcal{A} Distribution of datasets and randomized algorithm E \mathbb{E} Expectation of the random variable following it, taken over its subscript ℓ ⁡ ( y , y ^ ) \ell(y,\hat{y}) Individual loss function ℓ ⁡ ( ⋅ , ⋅ ) \ell(\cdot,\cdot) with label y y and prediction y ^ \hat{y} ℓ ⁡ ( 𝒘 , X , Y ) \ell({\bm{w}};{X},{Y}) Individual loss function equivalent to ℓ ⁡ ( Y , Φ ⁡ ( 𝒘 , X ) ) \ell({Y},\Phi({\bm{w}};{X})) ℓ t ​ ( z ) \ell_{t}(z) Equivalent to ℓ ⁡ ( Y t , z ) \ell({Y}_{t},z) where z z is the prediction ℒ ⁡ ( 𝒘 ) \mathcal{L}({\bm{w}}) Population loss, ℒ ⁡ ( 𝒘 ) ≜ E ( X , Y ) ∼ 𝒫 ​ ℓ ​ ( 𝐰 , X , Y ) \mathcal{L}({\bm{w}})\triangleq\mathbb{E}_{({X},{Y})\sim\mathcal{P}}\ell({\bm{w}};{X},{Y}) ℒ ^ ​ ( 𝒘 ) \hat{\mathcal{L}}({\bm{w}}) Empirical loss, ℒ ^ ​ ( 𝒘 ) ≜ 1 n ​ ∑ i ∈ [ n ] ℓ ⁡ ( 𝒘 , X i , Y i ) \hat{\mathcal{L}}({\bm{w}})\triangleq\frac{1}{n}\sum_{i\in[n]}\ell({\bm{w}};{X}_{i},{Y}_{i}) ℒ s ​ ( 𝒘 ) , ℒ ^ s ​ ( 𝒘 ) \mathcal{L}^{s}({\bm{w}}),\hat{\mathcal{L}}^{s}({\bm{w}}) Population and empirical risks evaluated on the unit sphere, i.e., ℒ s ​ ( 𝒘 ) ≜ ℒ ​ ( 𝒗 ) \mathcal{L}^{s}({\bm{w}})\triangleq\mathcal{L}({\bm{v}}) and ℒ ^ s ​ ( 𝒘 ) ≜ ℒ ^ ​ ( 𝒗 ) \hat{\mathcal{L}}^{s}({\bm{w}})\triangleq\hat{\mathcal{L}}({\bm{v}}) Constants and Bounds σ ¯ 2 \bar{\sigma}^{2} Upper bound of the individual loss on the unit sphere σ ¯ 2 \underline{\sigma}^{2} Bayesian optimal value of the given problem on the unit sphere, σ ¯ 2 ≜ min 𝒘 ⁡ ℒ ⁡ ( 𝒘 / ‖ 𝒘 ‖ ) ≠ 0 \underline{\sigma}^{2}\triangleq\min_{{\bm{w}}}\mathcal{L}({\bm{w}}/\|{\bm{w}}\|)\neq 0 γ , β \gamma,\beta Constants of ( γ , β ) (\gamma,\beta) -approximate smoothness for individual loss γ ~ \tilde{\gamma} Additional rate multiplier of generalization bound, γ ~ = max ⁡ { γ , 1 / n } \tilde{\gamma}=\max\{\gamma,1/n\} L L Lipschitz constant of individual loss m 1 m_{1} Derived constant governing the generalization, m 1 = 4 ​ c 2 ​ k 1 σ ¯ 2 ​ [ k 1 ​ k 2 ​ σ ¯ 2 + β H ] m_{1}=\frac{4c_{2}k_{1}}{\underline{\sigma}^{2}}\left[k_{1}k_{2}\bar{\sigma}^{2}+\frac{\beta}{H}\right] , where k 1 = k 2 = 1 k_{1}=k_{2}=1 in Theorem 1 c 2 c_{2} Constants specifying the stepsize

[164] p: This paper uses the following standard notations for asymptotic analysis. For any positive functions f ⁡ ( n ) f(n) and g ⁡ ( n ) g(n) , let C > 0 C>0 denote a constant independent of n n :

[165] p: f ⁡ ( n ) = Θ ⁡ ( g ⁡ ( n ) ) f(n)=\Theta(g(n)) if lim n → ∞ f ⁡ ( n ) g ⁡ ( n ) = C \lim_{n\to\infty}\frac{f(n)}{g(n)}=C ;

[166] p: f ⁡ ( n ) = 𝒪 ⁡ ( g ⁡ ( n ) ) f(n)=\mathcal{O}(g(n)) if lim sup n → ∞ f ⁡ ( n ) g ⁡ ( n ) < ∞ \limsup_{n\to\infty}\frac{f(n)}{g(n)}<\infty ;

[167] p: f ⁡ ( n ) = Ω ⁡ ( g ⁡ ( n ) ) f(n)=\Omega(g(n)) if lim inf n → ∞ f ⁡ ( n ) g ⁡ ( n ) > 0 \liminf_{n\to\infty}\frac{f(n)}{g(n)}>0 ;

[168] p: f ⁡ ( n ) = o ⁡ ( g ⁡ ( n ) ) f(n)=o(g(n)) if lim n → ∞ f ⁡ ( n ) g ⁡ ( n ) = 0 \lim_{n\to\infty}\frac{f(n)}{g(n)}=0 ;

[169] p: f ⁡ ( n ) = ω ⁡ ( g ⁡ ( n ) ) f(n)=\omega(g(n)) if lim n → ∞ f ⁡ ( n ) g ⁡ ( n ) = ∞ \lim_{n\to\infty}\frac{f(n)}{g(n)}=\infty .

[170] p: A comprehensive summary of the other notations used throughout this paper is provided in Table 2 .

[171] h3: B.2 Proof of Theorem 1

[172] p: This section derives the results in Theorem 1 . The outline of our approach unfolds as follows:

[173] p: First, we establish the relationship between the stepsize η t \eta_{t} and the effective stepsize η ~ t \tilde{\eta}_{t} on the unit sphere. Utilizing Lemma 1 , we analyze how different orders of stepsizes induce varying orders of effective stepsizes under the homogeneous setting. Building on this, we strategically select the stepsize regime to ensure the effective stepsize remains sufficiently small to guarantee generalization. We refer to Lemma 3 for more details.

[174] p: The remaining part requires deriving the algorithmic stability under such effective stepsize. Directly achieving stability proves elusive due to the presence of ‖ 𝒘 t + 1 ‖ \|{\bm{w}}_{t+1}\| and ‖ 𝒘 t ‖ \|{\bm{w}}_{t}\| within the updating rule stipulated in ( 17 ). Consequently, bounding the ratio ‖ 𝒘 t ‖ / ‖ 𝒘 t + 1 ‖ \|{\bm{w}}_{t}\|/\|{\bm{w}}_{t+1}\| emerges as a requirement. This imperative stems from the upper bound imposed on the loss function by Assumption 1 . We summarize the discussion in Lemma 4 .

[175] h4: B.2.1 (Effective) Stepsize

[176] h6: Lemma 3 ((Effective) stepsize) .

[177] p: Assume E 𝒜 ​ ‖ 𝐰 0 ‖ 2 = 1 \mathbb{E}_{\mathcal{A}}\|{\bm{w}}_{0}\|^{2}=1 and H > 2 H>2 without loss of generality. Under Assumption 1 and Assumption 2 :

[178] p: there exist infinitely many stepsizes satisfying E 𝒜 , 𝒟 ​ η t = Ω ⁡ ( t H − 4 2 ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}=\Omega(t^{\frac{H-4}{2}}) , such that the effective stepsize is of order Θ ⁡ ( 1 / t ) \Theta(1/t) ,

[179] p: there exist infinitely many stepsizes satisfying E 𝒜 , 𝒟 ​ η t ≤ 2 ​ c 2 H ​ σ ¯ 2 ​ ( t + 1 ) H − 4 2 = 𝒪 ⁡ ( t H − 4 2 ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}\leq\frac{2c_{2}}{H\underline{\sigma}^{2}}\left(t+1\right)^{\frac{H-4}{2}}=\mathcal{O}(t^{\frac{H-4}{2}}) with c 2 ≥ 1 c_{2}\geq 1 , such that the effective stepsize is of order 𝒪 ⁡ ( 1 / t ) \mathcal{O}\left(1/t\right) .

[180] p: there exist infinitely many stepsizes satisfying E 𝒜 , 𝒟 ​ η t = o ⁡ ( t H − 4 2 ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}=o(t^{\frac{H-4}{2}}) , such that the effective stepsize is of order o ⁡ ( 1 / t ) o(1/t) .

[181] p: where the expectation is taken over the randomness of the dataset and the algorithm.

[182] p: Lemma 3 is the core of our proof, which implies that while one may opt for a stepsize of the order Ω ⁡ ( t H − 4 2 ) \Omega(t^{\frac{H-4}{2}}) , its manifestation as an effective stepsize upon projection onto a sphere can be of order Θ ⁡ ( 1 / t ) \Theta(1/t) . This characteristic inherently holds the potential for establishing algorithmic stability. We remark that the existence arguments here are general since one could set η ~ t = Θ ⁡ ( 1 / t ) \tilde{\eta}_{t}=\Theta(1/t) with different constants. Hence, even in the context of existence arguments, there persists a degree of freedom attributed to constants. Discussion on Stochasticity and Stepsize Regimes. We clarify the stochastic nature of the relationship η ~ t = η t ​ ‖ 𝒘 t ‖ H − 2 \tilde{\eta}_{t}=\eta_{t}\|{\bm{w}}_{t}\|^{H-2} , which distinguishes our regime from standard SGD. In the SGD setting, the weight norm ‖ 𝒘 t ‖ \|{\bm{w}}_{t}\| is a random variable dependent on the sampling trajectory. Consequently, η t \eta_{t} and η ~ t \tilde{\eta}_{t} cannot simultaneously be deterministic unless ‖ 𝒘 t ‖ \|{\bm{w}}_{t}\| remains constant, which generally does not hold.

[183] p: Three scenarios arise: (1) η t \eta_{t} is deterministic, rendering η ~ t \tilde{\eta}_{t} random; (2) η ~ t \tilde{\eta}_{t} is deterministic, which requires η t \eta_{t} to be a random variable; or (3) both are random variables. Our analysis adopts Scenario (2). Specifically, we impose a deterministic decay on the effective stepsize η ~ t \tilde{\eta}_{t} ( e.g. , Θ ⁡ ( 1 / t ) \Theta(1/t) ), to ensure simple and stable update rule on the unit sphere.

[184] p: Therefore, the existence established in our statements is twofold: it asserts the existence of random variables η t \eta_{t} capable of rendering the effective stepsize (a) deterministic, and (b) falling within the regime where it, as a non-random variable, satisfies the stated asymptotic bounds.

[185] p: Discussion on log ⁡ ( T ) \log(T) convergence. We acknowledge the work by Soudry et al. (2018) , which similarly explores a classification setting with direction convergence. Different from the T \sqrt{T} rate proposed in Lemma 3 , the weight norm in Soudry et al. (2018) demonstrates an approximate log ⁡ T \log T growth. This distinction arises due to variations in loss forms, leading to non-conflicting conclusions. It’s worth noting that deriving an effective stepsize under their particular regime presents considerable complexity.

[186] h6: Proof of Lemma 3 .

[187] p: We begin by proving the first statement of Lemma 3 . By Lemma 12 , if η ~ t ≤ H ​ σ ¯ 2 2 ​ L 2 \tilde{\eta}_{t}\leq\frac{H\underline{\sigma}^{2}}{2L^{2}} , we have:

[188] table: E 𝒜 , 𝒟 ​ ‖ 𝐰 t + 1 ‖ 2 ≤ E 𝒜 , 𝒟 ​ ‖ 𝐰 t ‖ 2 ​ ( 1 − 1 2 ​ H ​ σ ¯ 2 ​ η ~ t ) , \mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t+1}\|^{2}\leq\mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t}\|^{2}\left(1-\frac{1}{2}H\underline{\sigma}^{2}\tilde{\eta}_{t}\right),

[189] p: Therefore, WLOG 3 3 3 Setting η ~ t = 2 ​ c 2 H ​ σ ¯ 2 ​ ( t + 1 ) \tilde{\eta}_{t}=\frac{2c_{2}}{H\underline{\sigma}^{2}(t+1)} with c 2 ≥ 1 c_{2}\geq 1 may lead to the requirement that 2 ​ L ≤ H ​ σ ¯ 2 2L\leq H\underline{\sigma}^{2} to satisfy the condition η ~ t ≤ H ​ σ ¯ 2 2 ​ L 2 \tilde{\eta}_{t}\leq\frac{H\underline{\sigma}^{2}}{2L^{2}} for all t ≥ 0 t\geq 0 . However, this is not strictly necessary. One can always set η ~ t = 2 ​ c 2 σ ¯ 2 ​ ( t + U ) \tilde{\eta}_{t}=\frac{2c_{2}}{\underline{\sigma}^{2}(t+U)} for a sufficiently large U U , which satisfies the requirement η ~ t ≤ H ​ σ ¯ 2 2 ​ L 2 \tilde{\eta}_{t}\leq\frac{H\underline{\sigma}^{2}}{2L^{2}} without influencing the asymptotic order. setting η ~ t = 2 ​ c 2 H ​ σ ¯ 2 ​ ( t + 1 ) \tilde{\eta}_{t}=\frac{2c_{2}}{H\underline{\sigma}^{2}(t+1)} with c 2 ≥ 1 c_{2}\geq 1 leads to

[190] table: E 𝒜 , 𝒟 ​ ‖ 𝐰 t ‖ 2 ≤ E 𝒜 , 𝒟 ​ ‖ 𝐰 t − 1 ‖ 2 ​ ( 1 − 1 / ( t + 1 ) ) ≤ 1 / ( t + 1 ) ​ E 𝒜 ​ ‖ 𝐰 0 ‖ 2 = 1 / ( t + 1 ) . \mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t}\|^{2}\leq\mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t-1}\|^{2}(1-1/{(t+1)})\leq 1/{(t+1)}\mathbb{E}_{\mathcal{A}}\|{\bm{w}}_{0}\|^{2}=1/{(t+1)}. (4)

[191] p: We derive the order of the stepsize given the choice of the effective stepsize. Notice that based on the order of the weight and the effective stepsize, the stepsize satisfies

[192] table: E 𝒜 , 𝒟 ​ η t \displaystyle\mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t} = ( i ) ​ E 𝒜 , 𝒟 ​ η ~ t ‖ 𝐰 t ‖ H − 2 \displaystyle\overset{(i)}{=}\mathbb{E}_{\mathcal{A},\mathcal{D}}\frac{\tilde{\eta}_{t}}{\|{\bm{w}}_{t}\|^{H-2}} ≥ ( i ​ i ) ​ η ~ t [ E 𝒜 , 𝒟 ​ ‖ 𝐰 t ‖ 2 ] H − 2 2 \displaystyle\overset{(ii)}{\geq}\frac{\tilde{\eta}_{t}}{[\mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t}\|^{2}]^{\frac{H-2}{2}}} ≥ ( i ​ i ​ i ) ​ 2 ​ ( t + 1 ) ( H − 2 ) / 2 H ​ σ ¯ 2 ​ ( t + 1 ) = 2 H ​ σ ¯ 2 ​ ( t + 1 ) ( H − 4 ) / 2 = Ω ⁡ ( t ( H − 4 ) / 2 ) , \displaystyle\overset{(iii)}{\geq}\frac{2(t+1)^{(H-2)/2}}{H\underline{\sigma}^{2}(t+1)}=\frac{2}{H\underline{\sigma}^{2}}(t+1)^{(H-4)/2}=\Omega(t^{(H-4)/2}),

[193] p: where the equation ( i ) (i) is due to the definition of η ~ t \tilde{\eta}_{t} , the inequality ( i ​ i ) (ii) is from Jensen’s inequality, and the inequality ( i ​ i ​ i ) (iii) is based on ( 4 ). Specifically, by taking f ( x ) = x − ( H − 2 ) / 2 f(x)=x^{-(H-2)/2} which is convex when x > 0 x>0 and H > 2 H>2 , we get from Jensen’s inequality that E ​ f ​ ( x ) ≥ f ⁡ ( E ​ x ) \mathbb{E}f(x)\geq f(\mathbb{E}x) . Therefore, setting x = ‖ 𝒘 ‖ 2 x=\|{\bm{w}}\|^{2} leads to E ∥ 𝐰 ∥ − ( H − 2 ) ≥ [ E ∥ 𝐰 ∥ 2 ] − ( H − 2 ) / 2 \mathbb{E}\|{\bm{w}}\|^{-(H-2)}\geq[{\mathbb{E}\|{\bm{w}}\|^{2}}]^{-(H-2)/2} .

[194] p: We next prove the second statement of Lemma 3 by contradiction. In this case, it still holds for the weight norm that:

[195] table: E 𝒜 , 𝒟 ∥ 𝐰 t + 1 ∥ 2 ≤ E 𝒜 , 𝒟 ∥ 𝐰 t ∥ 2 ( 1 − 1 2 H σ ¯ 2 η ~ t ) ≤ E 𝒜 ∥ 𝐰 0 ∥ 2 exp ( − 1 2 H σ ¯ 2 ∑ k = 0 t η ~ k ) . \mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t+1}\|^{2}\leq\mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t}\|^{2}\left(1-\frac{1}{2}H\underline{\sigma}^{2}\tilde{\eta}_{t}\right)\leq\mathbb{E}_{\mathcal{A}}\|{\bm{w}}_{0}\|^{2}\exp\left(-\frac{1}{2}H\underline{\sigma}^{2}\sum_{k=0}^{t}\tilde{\eta}_{k}\right).

[196] p: Suppose, for the sake of contradiction, that a stepsize satisfying E 𝒜 , 𝒟 ​ η t ≤ 2 ​ c 2 H ​ σ ¯ 2 ​ ( t + 1 ) H − 4 2 = 𝒪 ⁡ ( t H − 4 2 ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}\leq\frac{2c_{2}}{H\underline{\sigma}^{2}}\left(t+1\right)^{\frac{H-4}{2}}=\mathcal{O}(t^{\frac{H-4}{2}}) could lead to a larger effective stepsize η ~ t > 2 ​ c 2 H ​ σ ¯ 2 ⋅ 1 t + 1 \tilde{\eta}_{t}>\frac{2c_{2}}{H\underline{\sigma}^{2}}\cdot\frac{1}{t+1} . Given this assumption on η ~ t \tilde{\eta}_{t} , the summation in the exponent is lower bounded by:

[197] table: ∑ k = 0 t η ~ k > 2 ​ c 2 H ​ σ ¯ 2 ​ ∑ k = 0 t 1 k + 1 ≥ ln ⁡ ( k + 1 ) | 0 t + 1 = 2 ​ c 2 H ​ σ ¯ 2 ​ ln ⁡ ( t + 2 ) . \sum_{k=0}^{t}\tilde{\eta}_{k}>\frac{2c_{2}}{H\underline{\sigma}^{2}}\sum_{k=0}^{t}\frac{1}{k+1}\geq\left.\ln(k+1)\right|_{0}^{t+1}=\frac{2c_{2}}{H\underline{\sigma}^{2}}\ln(t+2).

[198] p: Consequently, the weight norm would decay at a rate of E 𝒜 , 𝒟 ​ ‖ 𝐰 t + 1 ‖ 2 < 1 t + 2 = 𝒪 ⁡ ( 1 / t ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t+1}\|^{2}<\frac{1}{t+2}=\mathcal{O}(1/t) . This rapid decay implies that the stepsize satisfies:

[199] table: E 𝒜 , 𝒟 ​ η t + 1 > 2 ​ c 2 H ​ σ ¯ 2 ⋅ 1 t + 2 [ 1 / ( t + 2 ) ] ( H − 2 ) / 2 = 2 ​ c 2 H ​ σ ¯ 2 ⋅ ( t + 2 ) ( H − 2 ) / 2 t + 2 = 2 ​ c 2 H ​ σ ¯ 2 ⋅ ( t + 2 ) ( H − 4 ) / 2 . \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t+1}>\frac{\frac{2c_{2}}{H\underline{\sigma}^{2}}\cdot\frac{1}{t+2}}{[1/(t+2)]^{(H-2)/2}}=\frac{2c_{2}}{H\underline{\sigma}^{2}}\cdot\frac{(t+2)^{(H-2)/2}}{t+2}=\frac{2c_{2}}{H\underline{\sigma}^{2}}\cdot(t+2)^{(H-4)/2}.

[200] p: which contradicts the initial hypothesis that E 𝒜 , 𝒟 ​ η t ≤ 2 ​ c 2 H ​ σ ¯ 2 ​ ( t + 1 ) H − 4 2 \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}\leq\frac{2c_{2}}{H\underline{\sigma}^{2}}\left(t+1\right)^{\frac{H-4}{2}} .

[201] p: Therefore, given the stepsize E 𝒜 , 𝒟 ​ η t ≤ 2 ​ c 2 H ​ σ ¯ 2 ​ ( t + 1 ) H − 4 2 \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}\leq\frac{2c_{2}}{H\underline{\sigma}^{2}}\left(t+1\right)^{\frac{H-4}{2}} , the deterministic effective stepsize must satisfy η ~ t = 𝒪 ⁡ ( 1 / t ) \tilde{\eta}_{t}=\mathcal{O}(1/t) .

[202] p: Finally, we prove the third statement of Lemma 3 . According to Lemma 9 , for any given sampling trajectory, the weight norm satisfies:

[203] table: ‖ 𝒘 t + 1 ‖ 2 = ‖ 𝒘 t ‖ 2 ​ ( 1 − 2 ​ H ​ η ~ t ​ ℓ ​ ( 𝒗 t ) + η ~ t 2 ​ ‖ ∇ ℓ ​ ( 𝒗 t ) ‖ 2 ) ≥ ‖ 𝒘 t ‖ 2 ​ ( 1 − 2 ​ H ​ σ ¯ 2 ​ η ~ t ) . \|{\bm{w}}_{t+1}\|^{2}=\|{\bm{w}}_{t}\|^{2}(1-2H\tilde{\eta}_{t}\ell({\bm{v}}_{t})+\tilde{\eta}_{t}^{2}\|\nabla\ell({\bm{v}}_{t})\|^{2})\geq\|{\bm{w}}_{t}\|^{2}(1-2H\bar{\sigma}^{2}\tilde{\eta}_{t}).

[204] p: Define an auxiliary sequence r t ≜ t ​ ‖ 𝒘 t ‖ 2 r_{t}\triangleq t\|{\bm{w}}_{t}\|^{2} . Since η ~ t = o ⁡ ( 1 / t ) \tilde{\eta}_{t}=o(1/t) , the iteration of r t r_{t} is governed by:

[205] table: r t + 1 r t = t + 1 t ⋅ ‖ 𝒘 t + 1 ‖ 2 ‖ 𝒘 t ‖ 2 ≥ ( 1 + 1 t ) ​ ( 1 − 2 ​ H ​ σ ¯ 2 ​ η ~ t ) = 1 + 1 t − 2 ​ H ​ σ ¯ 2 ​ η ~ t + o ⁡ ( 1 t 2 ) . \frac{r_{t+1}}{r_{t}}=\frac{t+1}{t}\cdot\frac{\|{\bm{w}}_{t+1}\|^{2}}{\|{\bm{w}}_{t}\|^{2}}\geq\left(1+\frac{1}{t}\right)(1-2H\bar{\sigma}^{2}\tilde{\eta}_{t})=1+\frac{1}{t}-2H\bar{\sigma}^{2}\tilde{\eta}_{t}+o(\frac{1}{t^{2}}).

[206] p: Then, there exists a t 0 t_{0} such that for all t > t 0 t>t_{0} , the term 2 ​ H ​ σ ¯ 2 ​ η ~ t < 1 2 ​ t 2H\bar{\sigma}^{2}\tilde{\eta}_{t}<\frac{1}{2t} . It holds that:

[207] table: r t + 1 r t > 1 + 1 2 ​ t . \frac{r_{t+1}}{r_{t}}>1+\frac{1}{2t}. (5)

[208] p: Iterating ( 5 ) from t 0 t_{0} to T − 1 T-1 , we obtain:

[209] table: r T ≥ r t 0 ​ ∏ t = t 0 T − 1 ( 1 + 1 2 ​ t ) ≥ r t 0 ​ ( 1 + ∑ t = t 0 T − 1 1 2 ​ t ) . r_{T}\geq r_{t_{0}}\prod_{t=t_{0}}^{T-1}(1+\frac{1}{2t})\geq r_{t_{0}}\left(1+\sum_{t=t_{0}}^{T-1}\frac{1}{2t}\right).

[210] p: The divergence of ∑ 1 t \sum\frac{1}{t} implies lim T → ∞ r T = ∞ \lim_{T\to\infty}r_{T}=\infty , which entails ‖ 𝒘 T ‖ 2 = ω ⁡ ( T − 1 ) \|{\bm{w}}_{T}\|^{2}=\omega(T^{-1}) . Recall that η ~ t ≜ ‖ 𝒘 t ‖ H − 2 ​ η t \tilde{\eta}_{t}\triangleq\|{\bm{w}}_{t}\|^{H-2}\eta_{t} from ( 17 ). Substituting the asymptotic order into this definition yields:

[211] table: η t = η ~ t [ ‖ 𝒘 t ‖ 2 ] H − 2 2 = o ⁡ ( 1 / t ) [ ω ⁡ ( 1 / t ) ] H − 2 2 = o ⁡ ( t H − 4 2 ) . \eta_{t}=\frac{\tilde{\eta}_{t}}{[\|{\bm{w}}_{t}\|^{2}]^{\frac{H-2}{2}}}\\ =\frac{o(1/t)}{[\omega(1/t)]^{\frac{H-2}{2}}}\\ =o(t^{\frac{H-4}{2}}).

[212] p: Notably, this upper bound holds with t 0 t_{0} independent of sampling randomness. Taking the expectation yields E 𝒜 , 𝒟 ​ η t = o ⁡ ( t H − 4 2 ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}=o(t^{\frac{H-4}{2}}) . This completes the proof. ∎

[213] h4: B.2.2 Generalization Gap

[214] p: We next show in Lemma 4 that under the effective stepsize η ~ t = Θ ⁡ ( 1 / t ) \tilde{\eta}_{t}=\Theta(1/t) , the generalization gap (or, algorithmic stability) can be bounded. Notably, the generalization gap is non-decreasing with respect to the effective stepsize sequence.

[215] h6: Lemma 4 (Generalization performance under effective stepsize) .

[216] p: Under the effective stepsize η ~ t = 2 ​ c 2 H ​ σ ¯ 2 ​ ( t + 2 ) \tilde{\eta}_{t}=\frac{2c_{2}}{H\underline{\sigma}^{2}(t+2)} with c 2 ≥ 1 c_{2}\geq 1 , assuming that the function is L L -Lipschitz and γ \gamma - β \beta approximately smooth, it holds that

[217] table: E 𝒜 , 𝒟 ​ ℒ ​ ( 𝐯 t ) − ℒ n ​ ( 𝐯 t ) ≤ ( L ​ m 2 ) 1 m 1 + 1 ​ [ 1 + 1 m 1 ] ​ T m 1 m 1 + 1 n , \mathbb{E}_{\mathcal{A},\mathcal{D}}\mathcal{L}({\bm{v}}_{t})-\mathcal{L}_{n}({\bm{v}}_{t})\leq(Lm_{2})^{\frac{1}{m_{1}+1}}\left[1+\frac{1}{m_{1}}\right]\frac{T^{\frac{m_{1}}{m_{1}+1}}}{n},

[218] p: where m 1 = 2 ​ c σ ¯ 2 ​ [ σ ¯ 2 + β H ] m_{1}=\frac{2c}{\underline{\sigma}^{2}}[\bar{\sigma}^{2}+\frac{\beta}{H}] , and m 2 = 4 ​ c H ​ σ ¯ 2 ​ ( L + γ ​ n ) m_{2}=\frac{4c}{H\underline{\sigma}^{2}}(L+\gamma n) .

[219] h6: Proof of Lemma 4 .

[220] p: Our results are partly inspired by the results in Hardt et al. (2016) . We focus on weight directions 𝒗 t {\bm{v}}_{t} and 𝒗 t ′ {\bm{v}}^{\prime}_{t} which are trained on dataset differing in at most one sample over t t iterations. To bound the algorithmic stability, the core is to bound the difference between 𝒗 t + 1 {\bm{v}}_{t+1} and 𝒗 t + 1 ′ {\bm{v}}^{\prime}_{t+1} , which is denoted by Δ ⁡ ( 𝒗 t + 1 , 𝒗 t + 1 ′ ) = ‖ 𝒗 t + 1 − 𝒗 t + 1 ′ ‖ \Delta({\bm{v}}_{t+1},{\bm{v}}^{\prime}_{t+1})=\|{\bm{v}}_{t+1}-{\bm{v}}^{\prime}_{t+1}\| . To do so, we first denote the weight after one iteration by 𝒗 ¯ t + 1 = 𝒗 t − η ~ t ​ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) \bar{{\bm{v}}}_{t+1}={\bm{v}}_{t}-\tilde{\eta}_{t}\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t}) .

[221] p: When choosing the same sample during the training,

[222] table: Δ ⁡ ( 𝒗 ¯ t + 1 , 𝒗 ¯ t + 1 ′ ) = ‖ 𝒗 ¯ t + 1 − 𝒗 ¯ t + 1 ′ ‖ = ‖ ( 𝒗 t − η ~ t ​ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) ) − ( 𝒗 t ′ − η ~ t ​ ∇ 𝒗 t ′ ℓ t ​ ( 𝒗 t ′ ) ) ‖ ≤ ‖ 𝒗 t − 𝒗 t ′ ‖ + η ~ t ​ ‖ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) − ∇ 𝒗 t ′ ℓ t ​ ( 𝒗 t ′ ) ‖ . \begin{split}&\Delta(\bar{{\bm{v}}}_{t+1},\bar{{\bm{v}}}^{\prime}_{t+1})\\ =&\|\bar{{\bm{v}}}_{t+1}-\bar{{\bm{v}}}^{\prime}_{t+1}\|\\ =&\|({\bm{v}}_{t}-\tilde{\eta}_{t}\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t}))-({\bm{v}}_{t}^{\prime}-\tilde{\eta}_{t}\nabla_{{\bm{v}}_{t}^{\prime}}\ell_{t}({\bm{v}}_{t}^{\prime}))\|\\ \leq&\|{\bm{v}}_{t}-{\bm{v}}_{t}^{\prime}\|+\tilde{\eta}_{t}\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})-\nabla_{{\bm{v}}_{t}^{\prime}}\ell_{t}({\bm{v}}_{t}^{\prime})\|.\end{split} (6)

[223] p: Note that the gradient difference can be bounded by Assumption 2 using a β \beta -smooth function ℓ ¯ \bar{\ell} , then we have that

[224] table: ‖ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) − ∇ 𝒗 t ′ ℓ t ​ ( 𝒗 t ′ ) ‖ = ‖ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) − ∇ 𝒗 t ℓ ¯ t ​ ( 𝒗 t ) + ∇ 𝒗 t ℓ ¯ t ​ ( 𝒗 t ) − ∇ 𝒗 t ′ ℓ ¯ t ​ ( 𝒗 t ′ ) + ∇ 𝒗 t ′ ℓ ¯ t ​ ( 𝒗 t ′ ) − ∇ 𝒗 t ′ ℓ t ​ ( 𝒗 t ′ ) ‖ ≤ ‖ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) − ∇ 𝒗 t ℓ ¯ t ​ ( 𝒗 t ) ‖ + | ∇ 𝒗 t ℓ ¯ t ​ ( 𝒗 t ) − ∇ 𝒗 t ′ ℓ ¯ t ​ ( 𝒗 t ′ ) | + ‖ ∇ 𝒗 t ′ ℓ ¯ t ​ ( 𝒗 t ′ ) − ∇ 𝒗 t ′ ℓ t ​ ( 𝒗 t ′ ) ‖ ≤ 2 ​ γ + β ​ ‖ 𝒗 t − 𝒗 t ′ ‖ . \begin{split}&\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})-\nabla_{{\bm{v}}_{t}^{\prime}}\ell_{t}({\bm{v}}_{t}^{\prime})\|\\ =&\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})-\nabla_{{\bm{v}}_{t}}\bar{\ell}_{t}({\bm{v}}_{t})+\nabla_{{\bm{v}}_{t}}\bar{\ell}_{t}({\bm{v}}_{t})-\nabla_{{\bm{v}}_{t}^{\prime}}\bar{\ell}_{t}({\bm{v}}_{t}^{\prime})+\nabla_{{\bm{v}}_{t}^{\prime}}\bar{\ell}_{t}({\bm{v}}_{t}^{\prime})-\nabla_{{\bm{v}}_{t}^{\prime}}\ell_{t}({\bm{v}}_{t}^{\prime})\|\\ \leq&\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})-\nabla_{{\bm{v}}_{t}}\bar{\ell}_{t}({\bm{v}}_{t})\|+\|\nabla_{{\bm{v}}_{t}}\bar{\ell}_{t}({\bm{v}}_{t})-\nabla_{{\bm{v}}_{t}^{\prime}}\bar{\ell}_{t}({\bm{v}}_{t}^{\prime})\|+\|\nabla_{{\bm{v}}_{t}^{\prime}}\bar{\ell}_{t}({\bm{v}}_{t}^{\prime})-\nabla_{{\bm{v}}_{t}^{\prime}}\ell_{t}({\bm{v}}_{t}^{\prime})\|\\ \leq&2\gamma+\beta\|{\bm{v}}_{t}-{\bm{v}}_{t}^{\prime}\|.\end{split} (7)

[225] p: By plugging ( 6 ) into ( 7 ), we obtain

[226] table: Δ ⁡ ( 𝒗 ¯ t + 1 , 𝒗 ¯ t + 1 ′ ) ≤ ( 1 + η ~ t ​ β ) ​ Δ ​ ( 𝒗 ¯ t , 𝒗 ¯ t ′ ) + 2 ​ η ~ t ​ γ . \Delta(\bar{{\bm{v}}}_{t+1},\bar{{\bm{v}}}^{\prime}_{t+1})\leq(1+\tilde{\eta}_{t}\beta)\Delta(\bar{{\bm{v}}}_{t},\bar{{\bm{v}}}^{\prime}_{t})+2\tilde{\eta}_{t}\gamma. (8)

[227] p: When choosing a different sample during the training, it similarly holds that

[228] table: Δ ⁡ ( 𝒗 ¯ t + 1 , 𝒗 ¯ t + 1 ′ ) = ‖ 𝒗 ¯ t + 1 − 𝒗 ¯ t + 1 ′ ‖ = ‖ ( 𝒗 t − η ~ t ​ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) ) − ( 𝒗 t ′ − η ~ t ​ ∇ 𝒗 t ′ ℓ t ​ ( 𝒗 t ′ ) ) ‖ ≤ ‖ 𝒗 t − 𝒗 t ′ ‖ + η ~ t ​ ‖ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) − ∇ 𝒗 t ′ ℓ t ​ ( 𝒗 t ′ ) ‖ ≤ Δ ⁡ ( 𝒗 ¯ t , 𝒗 ¯ t ′ ) + 2 ​ η ~ t ​ L . \begin{split}&\Delta(\bar{{\bm{v}}}_{t+1},\bar{{\bm{v}}}^{\prime}_{t+1})\\ =&\|\bar{{\bm{v}}}_{t+1}-\bar{{\bm{v}}}^{\prime}_{t+1}\|\\ =&\|({\bm{v}}_{t}-\tilde{\eta}_{t}\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t}))-({\bm{v}}_{t}^{\prime}-\tilde{\eta}_{t}\nabla_{{\bm{v}}_{t}^{\prime}}\ell_{t}({\bm{v}}_{t}^{\prime}))\|\\ \leq&\|{\bm{v}}_{t}-{\bm{v}}_{t}^{\prime}\|+\tilde{\eta}_{t}\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})-\nabla_{{\bm{v}}_{t}^{\prime}}\ell_{t}({\bm{v}}_{t}^{\prime})\|\\ \leq&\Delta(\bar{{\bm{v}}}_{t},\bar{{\bm{v}}}^{\prime}_{t})+2\tilde{\eta}_{t}L.\end{split} (9)

[229] p: Due to the randomness of SGD, where with probability 1 − 1 / n 1-1/n the same sample is chosen and with probability 1 / n 1/n a different sample is selected, based on ( 8 ) and ( 9 ), it holds that

[230] table: E 𝒜 , 𝒟 ​ Δ ​ ( 𝐯 ¯ t + 1 , 𝐯 ¯ t + 1 ′ ) ≤ E 𝒜 , 𝒟 ​ ( 1 − 1 n ) ​ [ ( 1 + η ~ t ​ β ) ​ Δ ​ ( 𝐯 ¯ t , 𝐯 ¯ t ′ ) + 2 ​ η ~ t ​ γ ] + 1 n ​ [ Δ ⁡ ( 𝐯 t , 𝐯 t ′ ) + 2 ​ η ~ t ​ L ] = E 𝒜 , 𝒟 ​ ( 1 + η ~ t ​ β ​ ( 1 − 1 n ) ) ​ Δ ​ ( 𝐯 t , 𝐯 t ′ ) + 2 ​ η ~ t ​ L n + ( 1 − 1 n ) ​ 2 ​ η ~ t ​ γ ≤ E 𝒜 , 𝒟 ​ ( 1 + η ~ t ​ β ) ​ Δ ​ ( 𝐯 t , 𝐯 t ′ ) + 2 ​ η ~ t ​ L n + 2 ​ η ~ t ​ γ . \begin{split}&\mathbb{E}_{\mathcal{A},\mathcal{D}}\Delta(\bar{{\bm{v}}}_{t+1},\bar{{\bm{v}}}^{\prime}_{t+1})\\ \leq&\mathbb{E}_{\mathcal{A},\mathcal{D}}(1-\frac{1}{n})\left[(1+\tilde{\eta}_{t}\beta)\Delta(\bar{{\bm{v}}}_{t},\bar{{\bm{v}}}^{\prime}_{t})+2\tilde{\eta}_{t}\gamma\right]+\frac{1}{n}[\Delta({{\bm{v}}}_{t},{{\bm{v}}}^{\prime}_{t})+2\tilde{\eta}_{t}L]\\ =&\mathbb{E}_{\mathcal{A},\mathcal{D}}\left(1+\tilde{\eta}_{t}\beta(1-\frac{1}{n})\right)\Delta({{\bm{v}}}_{t},{{\bm{v}}}^{\prime}_{t})+\frac{2\tilde{\eta}_{t}L}{n}+(1-\frac{1}{n})2\tilde{\eta}_{t}\gamma\\ \leq&\mathbb{E}_{\mathcal{A},\mathcal{D}}(1+\tilde{\eta}_{t}\beta)\Delta({{\bm{v}}}_{t},{{\bm{v}}}^{\prime}_{t})+\frac{2\tilde{\eta}_{t}L}{n}+2\tilde{\eta}_{t}\gamma.\end{split}

[231] p: By the results in Lemma 5 and Lemma 6 , we conclude that

[232] table: Δ ⁡ ( 𝒗 t + 1 , 𝒗 t + 1 ′ ) ≤ max ⁡ { ‖ 𝒘 t ‖ ‖ 𝒘 t + 1 ‖ , ‖ 𝒘 t ′ ‖ ‖ 𝒘 t + 1 ′ ‖ } ​ Δ ​ ( 𝒗 ¯ t + 1 , 𝒗 ¯ t + 1 ′ ) ≤ [ 1 + 4 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 ] ​ Δ ​ ( 𝒗 ¯ t + 1 , 𝒗 ¯ t + 1 ′ ) . \begin{split}\Delta({\bm{v}}_{t+1},{\bm{v}}^{\prime}_{t+1})\leq\max\left\{\frac{\|{\bm{w}}_{t}\|}{\|{\bm{w}}_{t+1}\|},\frac{\|{\bm{w}}_{t}^{\prime}\|}{\|{\bm{w}}_{t+1}^{\prime}\|}\right\}\Delta(\bar{{\bm{v}}}_{t+1},\bar{{\bm{v}}}^{\prime}_{t+1})\leq\left[1+4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}\right]\Delta(\bar{{\bm{v}}}_{t+1},\bar{{\bm{v}}}^{\prime}_{t+1}).\end{split} (10)

[233] p: When t ≥ T 0 = 8 ​ c 2 ​ σ ¯ 2 σ ¯ 2 = 𝒪 ⁡ ( 1 ) t\geq T_{0}=8\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}=\mathcal{O}(1) , taking expectations over the algorithms and dataset and plugging into η ~ t = 2 ​ c 2 H ​ σ ¯ 2 ​ ( t + 2 ) \tilde{\eta}_{t}=\frac{2c_{2}}{H\underline{\sigma}^{2}(t+2)} leads to

[234] table: E 𝒜 , 𝒟 ​ Δ ​ ( 𝐯 t + 1 , 𝐯 t + 1 ′ ) ≤ [ 1 + 4 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 ] ​ E 𝒜 , 𝒟 ​ Δ ​ ( 𝐯 ¯ t + 1 , 𝐯 ¯ t + 1 ′ ) ≤ [ 1 + 4 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 ] ​ [ ( 1 + η ~ t ​ β ) ​ E 𝒜 , 𝒟 ​ Δ ​ ( 𝐯 t , 𝐯 t ′ ) + 2 ​ η ~ t ​ L n + 2 ​ η ~ t ​ γ ] = [ 1 + 4 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 ] ​ [ ( 1 + 2 ​ c 2 ​ β H ​ σ ¯ 2 ​ ( t + 2 ) ) ​ E 𝒜 , 𝒟 ​ Δ ​ ( 𝐯 t , 𝐯 t ′ ) + 4 ​ c 2 ​ L n ​ H ​ σ ¯ 2 ​ ( t + 2 ) + 4 ​ c 2 H ​ σ ¯ 2 ​ ( t + 2 ) ​ γ ] ≤ [ 1 + 4 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 + 4 ​ c 2 ​ β H ​ σ ¯ 2 ​ ( t + 2 ) ] ​ E 𝒜 , 𝒟 ​ Δ ​ ( 𝐯 t , 𝐯 t ′ ) + 8 ​ c 2 ​ L n ​ H ​ σ ¯ 2 ​ ( t + 2 ) + 8 ​ c 2 ​ γ H ​ σ ¯ 2 ​ ( t + 2 ) ≤ exp ⁡ ( m 1 ​ 1 t ) ​ E 𝒜 , 𝒟 ​ Δ ​ ( 𝐯 t , 𝐯 t ′ ) + m 2 n ​ t , \begin{split}&\mathbb{E}_{\mathcal{A},\mathcal{D}}\Delta({\bm{v}}_{t+1},{\bm{v}}^{\prime}_{t+1})\\ \leq&\left[1+4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}\right]\mathbb{E}_{\mathcal{A},\mathcal{D}}\Delta(\bar{{\bm{v}}}_{t+1},\bar{{\bm{v}}}^{\prime}_{t+1})\\ \leq&\left[1+4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}\right]\left[(1+\tilde{\eta}_{t}\beta)\mathbb{E}_{\mathcal{A},\mathcal{D}}\Delta({{\bm{v}}}_{t},{{\bm{v}}}^{\prime}_{t})+\frac{2\tilde{\eta}_{t}L}{n}+2\tilde{\eta}_{t}\gamma\right]\\ =&\left[1+4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}\right]\left[(1+\frac{2c_{2}\beta}{H\underline{\sigma}^{2}(t+2)})\mathbb{E}_{\mathcal{A},\mathcal{D}}\Delta({{\bm{v}}}_{t},{{\bm{v}}}^{\prime}_{t})+\frac{4c_{2}L}{nH\underline{\sigma}^{2}(t+2)}+\frac{4c_{2}}{H\underline{\sigma}^{2}(t+2)}\gamma\right]\\ \leq&\left[1+4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}+\frac{4c_{2}\beta}{H\underline{\sigma}^{2}(t+2)}\right]\mathbb{E}_{\mathcal{A},\mathcal{D}}\Delta({{\bm{v}}}_{t},{{\bm{v}}}^{\prime}_{t})+\frac{8c_{2}L}{nH{\underline{\sigma}^{2}(t+2)}}+\frac{8c_{2}\gamma}{H\underline{\sigma}^{2}(t+2)}\\ \leq&\exp\left(m_{1}\frac{1}{t}\right)\mathbb{E}_{\mathcal{A},\mathcal{D}}\Delta({{\bm{v}}}_{t},{{\bm{v}}}^{\prime}_{t})+\frac{m_{2}}{nt},\end{split} (11)

[235] p: where η ~ t ≤ 1 / β \tilde{\eta}_{t}\leq 1/\beta , m 1 = 4 ​ c 2 σ ¯ 2 ​ [ σ ¯ 2 + β H ] m_{1}=\frac{4c_{2}}{\underline{\sigma}^{2}}[\bar{\sigma}^{2}+\frac{\beta}{H}] , and m 2 = 8 ​ c 2 H ​ σ ¯ 2 ​ ( L + γ ​ n ) m_{2}=\frac{8c_{2}}{H\underline{\sigma}^{2}}(L+\gamma n) .

[236] p: According to (3.10) in Hardt et al. (2016) , for any given t 0 t_{0} , generalization gap can be bounded by

[237] table: E 𝒜 , 𝒟 ​ ℒ T s ​ ( 𝐰 ) − ℒ ^ T s ​ ( 𝐰 ) ≤ t 0 n + L ​ E 𝒜 , 𝒟 ​ ( Δ ⁡ ( 𝐯 T , 𝐯 T ′ ) | Δ ⁡ ( 𝐯 t 0 , 𝐯 t 0 ′ ) = 0 ) . \mathbb{E}_{\mathcal{A},\mathcal{D}}\mathcal{L}^{s}_{T}({\bm{w}})-\hat{\mathcal{L}}^{s}_{T}({\bm{w}})\leq\frac{t_{0}}{n}+L\mathbb{E}_{\mathcal{A},\mathcal{D}}(\Delta({\bm{v}}_{T},{\bm{v}}^{\prime}_{T})\ |\ \Delta({\bm{v}}_{t_{0}},{\bm{v}}^{\prime}_{t_{0}})=0). (12)

[238] p: For the second term, notice that given Δ ⁡ ( 𝒗 t 0 , 𝒗 t 0 ′ ) = 0 \Delta({\bm{v}}_{t_{0}},{\bm{v}}^{\prime}_{t_{0}})=0 and ( 11 ), it holds that

[239] table: E 𝒜 , 𝒟 ​ Δ ​ ( 𝐯 T , 𝐯 T ′ ) ≤ ∑ t = t 0 + 1 T { ∏ k = t + 1 T exp ⁡ ( m 1 k ) } ​ m 2 n ​ t = ∑ t = t 0 + 1 T exp ⁡ ( m 1 ​ ∑ k = t + 1 T 1 k ) ​ m 2 n ​ t ≤ ∑ t = t 0 + 1 T exp ⁡ ( m 1 ​ log ⁡ ( T / t ) ) ​ m 2 n ​ t = m 2 n ​ T m 1 ​ ∑ t = t 0 + 1 T 1 t m 1 + 1 ≤ m 2 n ​ 1 m 1 ​ ( T t 0 ) m 1 . \begin{split}&\mathbb{E}_{\mathcal{A},\mathcal{D}}\Delta({\bm{v}}_{T},{\bm{v}}^{\prime}_{T})\\ \leq&\sum_{t=t_{0}+1}^{T}\{\prod_{k=t+1}^{T}\exp(\frac{m_{1}}{k})\}\frac{m_{2}}{nt}\\ =&\sum_{t=t_{0}+1}^{T}\exp(m_{1}\sum_{k=t+1}^{T}\frac{1}{k})\frac{m_{2}}{nt}\\ \leq&\sum_{t=t_{0}+1}^{T}\exp(m_{1}\log(T/t))\frac{m_{2}}{nt}\\ =&\frac{m_{2}}{n}T^{m_{1}}\sum_{t=t_{0}+1}^{T}\frac{1}{t^{m_{1}+1}}\\ \leq&\frac{m_{2}}{n}\frac{1}{m_{1}}(\frac{T}{t_{0}})^{m_{1}}.\end{split}

[240] p: Therefore, one can bound the generalization gap as

[241] table: E 𝒜 , 𝒟 ​ ℒ T s ​ ( 𝐰 ) − ℒ ^ T s ​ ( 𝐰 ) ≤ t 0 n + L ​ m 2 n ​ 1 m 1 ​ ( T t 0 ) m 1 . \mathbb{E}_{\mathcal{A},\mathcal{D}}\mathcal{L}^{s}_{T}({\bm{w}})-\hat{\mathcal{L}}^{s}_{T}({\bm{w}})\leq\frac{t_{0}}{n}+L\frac{m_{2}}{n}\frac{1}{m_{1}}(\frac{T}{t_{0}})^{m_{1}}.

[242] p: By choosing 4 4 4 Here the choice of t 0 t_{0} naturally holds that t 0 ≥ T 0 = 8 ​ c 2 ​ σ ¯ 2 σ ¯ 2 = 𝒪 ⁡ ( 1 ) . t_{0}\geq T_{0}=8\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}=\mathcal{O}(1). t 0 = ( L ​ m 2 ) 1 m 1 + 1 ​ T m 1 m 1 + 1 t_{0}=(Lm_{2})^{\frac{1}{m_{1}+1}}T^{\frac{m_{1}}{m_{1}+1}} , the generalization gap is bounded by

[243] table: E 𝒜 , 𝒟 ​ ℒ T s ​ ( 𝐰 ) − ℒ ^ T s ​ ( 𝐰 ) ≤ ( L ​ m 2 ) 1 m 1 + 1 ​ [ 1 + 1 m 1 ] ​ T m 1 m 1 + 1 n . \mathbb{E}_{\mathcal{A},\mathcal{D}}\mathcal{L}^{s}_{T}({\bm{w}})-\hat{\mathcal{L}}^{s}_{T}({\bm{w}})\leq(Lm_{2})^{\frac{1}{m_{1}+1}}\left[1+\frac{1}{m_{1}}\right]\frac{T^{\frac{m_{1}}{m_{1}+1}}}{n}.

[244] p: We finally remark that here it requires t 0 < T t_{0}<T , which leads to L ​ m 2 < T Lm_{2}<T . Recall that m 2 = 8 ​ c 2 H ​ σ ¯ 2 ​ ( L + γ ​ n ) m_{2}=\frac{8c_{2}}{H\underline{\sigma}^{2}}(L+\gamma n) and therefore it suffices to require γ = o ⁡ ( T / n ) \gamma=o(T/n) . ∎

[245] h6: Lemma 5 .

[246] p: Under the Assumptions in Lemma 4 , there exists a T 0 = 8 ​ c 2 ​ σ ¯ 2 σ ¯ 2 = 𝒪 ⁡ ( 1 ) T_{0}=8\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}=\mathcal{O}(1) such that for t > T 0 t>T_{0} ,

[247] table: ‖ 𝒘 t ‖ ‖ 𝒘 t + 1 ‖ ≤ 1 + 4 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 . \frac{\|{\bm{w}}_{t}\|}{\|{\bm{w}}_{t+1}\|}\leq 1+4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}. (13)

[248] h6: Proof of Lemma 5 .

[249] p: Due to Argument 3 in Lemma 1 , it holds that

[250] table: ‖ 𝒘 t ‖ ‖ 𝒘 t + 1 ‖ = [ 1 + η ~ t 2 ∥ ∇ 𝒗 t ℓ t ( 𝒗 t ) ∥ 2 − 2 H η ~ t ℓ t ( 𝒗 t ) ] − 1 / 2 . \frac{\|{\bm{w}}_{t}\|}{\|{\bm{w}}_{t+1}\|}=[1+\tilde{\eta}_{t}^{2}\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})\|^{2}-2H\tilde{\eta}_{t}\ell_{t}({\bm{v}}_{t})]^{-1/2}.

[251] p: By plugging into the effective stepsize η ~ t = 2 ​ c 2 H ​ σ ¯ 2 ​ ( t + 2 ) \tilde{\eta}_{t}=\frac{2c_{2}}{H\underline{\sigma}^{2}(t+2)} and the loss upper bound in Assumption 1 , it holds that

[252] table: ‖ 𝒘 t ‖ ‖ 𝒘 t + 1 ‖ ≤ [ 1 − 2 H η ~ t ℓ t ( 𝒗 t ) ] − 1 / 2 ≤ [ 1 − 4 c 2 ​ σ ¯ 2 σ ¯ 2 1 t + 2 ] − 1 / 2 . \frac{\|{\bm{w}}_{t}\|}{\|{\bm{w}}_{t+1}\|}\leq\left[1-2H\tilde{\eta}_{t}\ell_{t}({\bm{v}}_{t})\right]^{-1/2}\leq\left[1-4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}\right]^{-1/2}.

[253] p: Furthermore, due to the fact that ( 1 − u ) − 1 / 2 ≤ 1 + u (1-u)^{-1/2}\leq 1+u when u ∈ [ 0 , 1 / 2 ] u\in[0,1/2] ,

[254] table: ‖ 𝒘 t ‖ ‖ 𝒘 t + 1 ‖ ≤ 1 + 4 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 , \frac{\|{\bm{w}}_{t}\|}{\|{\bm{w}}_{t+1}\|}\leq 1+4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2},

[255] p: which is guaranteed by the condition t > T 0 = 8 ​ c 2 ​ σ ¯ 2 σ ¯ 2 t>T_{0}=8\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}} . ∎

[256] h6: Lemma 6 .

[257] p: Under the Assumptions in Lemma 4 , it holds that

[258] table: Δ ⁡ ( 𝒗 t + 1 , 𝒗 t + 1 ′ ) ≤ max ⁡ { ‖ 𝒘 t ‖ ‖ 𝒘 t + 1 ‖ , ‖ 𝒘 t ′ ‖ ‖ 𝒘 t + 1 ′ ‖ } ​ Δ ​ ( 𝒗 ¯ t + 1 , 𝒗 ¯ t + 1 ′ ) . \Delta({\bm{v}}_{t+1},{\bm{v}}^{\prime}_{t+1})\leq\max\left\{\frac{\|{\bm{w}}_{t}\|}{\|{\bm{w}}_{t+1}\|},\frac{\|{\bm{w}}_{t}^{\prime}\|}{\|{\bm{w}}_{t+1}^{\prime}\|}\right\}\Delta(\bar{{\bm{v}}}_{t+1},\bar{{\bm{v}}}^{\prime}_{t+1}). (14)

[259] h6: Proof of Lemma 6 .

[260] p: We first notice that 𝒗 t + 1 {{\bm{v}}}_{t+1} is the projection of 𝒗 ¯ t + 1 \bar{{\bm{v}}}_{t+1} to a standard sphere. Therefore, due to the iteration in ( 17 ), we derive that

[261] table: 𝒗 t + 1 = ‖ 𝒘 t ‖ ‖ 𝒘 t + 1 ‖ ​ 𝒗 ¯ t + 1 . {{\bm{v}}}_{t+1}=\frac{\|{\bm{w}}_{t}\|}{\|{\bm{w}}_{t+1}\|}\bar{{\bm{v}}}_{t+1}.

[262] p: We next show the results in ( 14 ). Due to the symmetry, we assume without loss of generality that ‖ 𝒘 t ‖ ‖ 𝒘 t + 1 ‖ ≤ ‖ 𝒘 t ′ ‖ ‖ 𝒘 t + 1 ′ ‖ \frac{\|{\bm{w}}_{t}\|}{\|{\bm{w}}_{t+1}\|}\leq\frac{\|{\bm{w}}_{t}^{\prime}\|}{\|{\bm{w}}_{t+1}^{\prime}\|} , which indicates that ‖ 𝒗 ¯ t + 1 ′ ‖ ≤ ‖ 𝒗 ¯ t + 1 ‖ \|\bar{{\bm{v}}}^{\prime}_{t+1}\|\leq\|\bar{{\bm{v}}}_{t+1}\| since ‖ 𝒗 t + 1 ‖ = ‖ 𝒗 t + 1 ′ ‖ = 1 \|{\bm{v}}_{t+1}\|=\|{\bm{v}}^{\prime}_{t+1}\|=1 . Therefore, it suffices to show that Δ ⁡ ( 𝒗 t + 1 , 𝒗 t + 1 ′ ) ≤ ‖ 𝒘 t ′ ‖ ‖ 𝒘 t + 1 ′ ‖ ​ Δ ​ ( 𝒗 ¯ t + 1 , 𝒗 ¯ t + 1 ′ ) . \Delta({\bm{v}}_{t+1},{\bm{v}}^{\prime}_{t+1})\leq\frac{\|{\bm{w}}_{t}^{\prime}\|}{\|{\bm{w}}_{t+1}^{\prime}\|}\Delta(\bar{{\bm{v}}}_{t+1},\bar{{\bm{v}}}^{\prime}_{t+1}).

[263] figure: 𝒗 t + 1 {\bm{v}}_{t+1} 𝒗 t + 1 ′ {\bm{v}}_{t+1}^{\prime} O O 𝒗 ¯ t + 1 \bar{{\bm{v}}}_{t+1} ω ​ 𝒗 ¯ t + 1 \omega\bar{{\bm{v}}}_{t+1} 𝒗 ¯ t + 1 ′ \bar{{\bm{v}}}_{t+1}^{\prime}

[264] p: We next only focus on the space spanned by vector 𝒗 t + 1 {\bm{v}}_{t+1} and 𝒗 t + 1 ′ {\bm{v}}_{t+1}^{\prime} . Let ω = ‖ 𝒗 ¯ t + 1 ′ ‖ ‖ 𝒗 ¯ t + 1 ‖ \omega=\frac{\|\bar{{\bm{v}}}^{\prime}_{t+1}\|}{\|\bar{{\bm{v}}}_{t+1}\|} denotes a ratio, which guarantees that ‖ ω ​ 𝒗 ¯ t + 1 ‖ = ‖ 𝒗 ¯ t + 1 ′ ‖ \|\omega\bar{{\bm{v}}}_{t+1}\|=\|\bar{{\bm{v}}}^{\prime}_{t+1}\| . When ‖ 𝒗 ¯ t + 1 ′ ‖ ≤ ‖ 𝒗 ¯ t + 1 ‖ \|\bar{{\bm{v}}}^{\prime}_{t+1}\|\leq\|\bar{{\bm{v}}}_{t+1}\| , we have Δ ⁡ ( ω ​ 𝒗 ¯ t + 1 , 𝒗 ¯ t + 1 ′ ) ≤ Δ ⁡ ( 𝒗 ¯ t + 1 , 𝒗 ¯ t + 1 ′ ) \Delta(\omega\bar{{\bm{v}}}_{t+1},\bar{{\bm{v}}}_{t+1}^{\prime})\leq\Delta(\bar{{\bm{v}}}_{t+1},\bar{{\bm{v}}}_{t+1}^{\prime}) . Therefore, it holds that

[265] table: Δ ⁡ ( 𝒗 t + 1 , 𝒗 t + 1 ′ ) = ‖ 𝒘 t ′ ‖ ‖ 𝒘 t + 1 ′ ‖ ​ Δ ​ ( ω ​ 𝒗 ¯ t + 1 , 𝒗 ¯ t + 1 ′ ) ≤ ‖ 𝒘 t ′ ‖ ‖ 𝒘 t + 1 ′ ‖ ​ Δ ​ ( 𝒗 ¯ t + 1 , 𝒗 ¯ t + 1 ′ ) , \begin{split}\Delta({\bm{v}}_{t+1},{\bm{v}}^{\prime}_{t+1})=\frac{\|{\bm{w}}_{t}^{\prime}\|}{\|{\bm{w}}_{t+1}^{\prime}\|}\Delta(\omega\bar{{\bm{v}}}_{t+1},\bar{{\bm{v}}}_{t+1}^{\prime})\leq\frac{\|{\bm{w}}_{t}^{\prime}\|}{\|{\bm{w}}_{t+1}^{\prime}\|}\Delta(\bar{{\bm{v}}}_{t+1},\bar{{\bm{v}}}_{t+1}^{\prime}),\end{split}

[266] p: where the first equation is due to the projection. This completes the proof. ∎

[267] h3: B.3 Proof of Corollary 1

[268] h6: Proof.

[269] p: For clarity, this proof follows the derivation of the second statement in Lemma 3 . The rest follows from a similar argument. The proof proceeds by substituting specific constants with new values while reusing the analytical framework established in the proof of Theorem 1 .

[270] p: Let c 2 ′ = k 1 ​ c 2 c_{2}^{\prime}=k_{1}c_{2} . We first show that for the identical stepsizes satisfying E 𝒜 , 𝒟 ​ η t ≤ 2 ​ c 2 H ​ σ ¯ 2 ​ ( t + 1 ) H − 4 2 \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}\leq\frac{2c_{2}}{H\underline{\sigma}^{2}}(t+1)^{\frac{H-4}{2}} , the effective stepsize in Corollary 1 is bounded by:

[271] table: η ~ t ≤ 2 ​ c 2 ′ H ​ σ ¯ 2 ​ ( t + 1 ) . \tilde{\eta}_{t}\leq\frac{2c_{2}^{\prime}}{H\underline{\sigma}^{2}(t+1)}. (15)

[272] p: Suppose, for the sake of contradiction, there exists some t t such that η ~ t > 2 ​ c 2 ′ H ​ σ ¯ 2 ​ ( t + 1 ) \tilde{\eta}_{t}>\frac{2c_{2}^{\prime}}{H\underline{\sigma}^{2}(t+1)} . We have:

[273] table: E 𝒜 , 𝒟 ​ η t + 1 \displaystyle\mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t+1} = E 𝒜 , 𝒟 ​ η ~ t + 1 ρ t + 1 ​ ‖ 𝐰 t + 1 ‖ H − 2 ≥ η ~ t + 1 ρ t + 1 ​ [ E 𝒜 , 𝒟 ​ ‖ 𝐰 t + 1 ‖ 2 ] ( H − 2 ) / 2 ≥ 1 k 1 ⋅ η ~ t + 1 [ E 𝒜 , 𝒟 ​ ‖ 𝐰 t + 1 ‖ 2 ] ( H − 2 ) / 2 \displaystyle=\mathbb{E}_{\mathcal{A},\mathcal{D}}\frac{\tilde{\eta}_{t+1}}{\rho_{t+1}\|{\bm{w}}_{t+1}\|^{H-2}}\geq\frac{\tilde{\eta}_{t+1}}{\rho_{t+1}[\mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t+1}\|^{2}]^{(H-2)/2}}\geq\frac{1}{k_{1}}\cdot\frac{\tilde{\eta}_{t+1}}{[\mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t+1}\|^{2}]^{(H-2)/2}} > 1 k 1 ⋅ 2 ​ c 2 ′ H ​ σ ¯ 2 ​ ( t + 2 ) ( 1 / ( t + 2 ) ) H − 2 2 = 2 ​ ( c 2 ′ / k 1 ) H ​ σ ¯ 2 ​ ( t + 2 ) H − 4 2 . \displaystyle>\frac{1}{k_{1}}\cdot\frac{\frac{2c_{2}^{\prime}}{H\underline{\sigma}^{2}(t+2)}}{(1/(t+2))^{\frac{H-2}{2}}}=\frac{2(c_{2}^{\prime}/k_{1})}{H\underline{\sigma}^{2}}(t+2)^{\frac{H-4}{2}}.

[274] p: Substituting c 2 ′ / k 1 = c 2 c_{2}^{\prime}/k_{1}=c_{2} , we obtain E 𝒜 , 𝒟 ​ η t + 1 > 2 ​ c 2 H ​ σ ¯ 2 ​ ( t + 2 ) H − 4 2 \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t+1}>\frac{2c_{2}}{H\underline{\sigma}^{2}}(t+2)^{\frac{H-4}{2}} , which contradicts the given condition on the stepsize. Thus, the effective stepsize must satisfy η ~ t ≤ 2 ​ c 2 ′ H ​ σ ¯ 2 ​ ( t + 1 ) \tilde{\eta}_{t}\leq\frac{2c_{2}^{\prime}}{H\underline{\sigma}^{2}(t+1)} .

[275] p: Next, we bound the norm ratio ‖ 𝒘 t ‖ ‖ 𝒘 t + 1 ‖ \frac{\|{\bm{w}}_{t}\|}{\|{\bm{w}}_{t+1}\|} . Combining the assumption that ρ t ≤ k 1 \rho_{t}\leq k_{1} , z ​ ℓ t ′ ​ ( z ) ≤ k 2 ​ ℓ t ​ ( z ) z\ell^{\prime}_{t}(z)\leq k_{2}\ell_{t}(z) , and the homogeneity of the neural network Φ \Phi , we have:

[276] table: 𝒘 t ⊤ ∇ 𝒘 t ℓ t ​ ( 𝒘 t ) = ℓ t ′ ​ ( Φ ⁡ ( 𝒘 t ) ) ​ 𝒘 t ⊤ ∇ 𝒘 t Φ ​ ( 𝒘 t ) = ρ t ​ ℓ t ′ ​ ( Φ ⁡ ( 𝒗 t ) ) ​ 𝒘 t ⊤ ∇ 𝒘 t Φ ​ ( 𝒘 t ) = ρ t ​ ‖ 𝒘 t ‖ H ​ ℓ t ′ ​ ( Φ ⁡ ( 𝒗 t ) ) ​ 𝒗 t ⊤ ∇ 𝒗 t Φ ​ ( 𝒗 t ) = ρ t ​ H ​ ‖ 𝒘 t ‖ H ​ Φ ​ ( 𝒗 t ) ​ ℓ t ′ ​ ( Φ ⁡ ( 𝒗 t ) ) ≤ k 1 ​ H ​ ‖ 𝒘 t ‖ H ​ Φ ​ ( 𝒗 t ) ​ ℓ t ′ ​ ( Φ ⁡ ( 𝒗 t ) ) ≤ k 1 ​ k 2 ​ H ​ ‖ 𝒘 t ‖ H ​ ℓ t ​ ( Φ ⁡ ( 𝒗 t ) ) ≤ k 1 ​ k 2 ​ σ ¯ 2 ​ H ​ ‖ 𝒘 t ‖ H . \begin{split}{\bm{w}}_{t}\top\nabla_{{\bm{w}}_{t}}\ell_{t}({\bm{w}}_{t})&=\ell^{\prime}_{t}(\Phi({\bm{w}}_{t})){\bm{w}}_{t}\top\nabla_{{\bm{w}}_{t}}\Phi({\bm{w}}_{t})\\ &=\rho_{t}\ell^{\prime}_{t}(\Phi({\bm{v}}_{t})){\bm{w}}_{t}\top\nabla_{{\bm{w}}_{t}}\Phi({\bm{w}}_{t})\\ &=\rho_{t}\|{\bm{w}}_{t}\|^{H}\ell^{\prime}_{t}(\Phi({\bm{v}}_{t})){\bm{v}}_{t}\top\nabla_{{\bm{v}}_{t}}\Phi({\bm{v}}_{t})\\ &=\rho_{t}H\|{\bm{w}}_{t}\|^{H}\Phi({\bm{v}}_{t})\ell^{\prime}_{t}(\Phi({\bm{v}}_{t}))\\ &\leq k_{1}H\|{\bm{w}}_{t}\|^{H}\Phi({\bm{v}}_{t})\ell^{\prime}_{t}(\Phi({\bm{v}}_{t}))\\ &\leq k_{1}k_{2}H\|{\bm{w}}_{t}\|^{H}\ell_{t}(\Phi({\bm{v}}_{t}))\\ &\leq k_{1}k_{2}\bar{\sigma}^{2}H\|{\bm{w}}_{t}\|^{H}.\end{split}

[277] p: Substituting this bound into the norm iteration ‖ 𝒘 t + 1 ‖ 2 = ‖ 𝒘 t ‖ 2 + η t 2 ​ ‖ ∇ 𝒘 t ℓ t ​ ( 𝒘 t ) ‖ 2 − 2 ​ η t ​ 𝒘 t ⊤ ​ ∇ 𝒘 t ℓ t ​ ( 𝒘 t ) \|{\bm{w}}_{t+1}\|^{2}=\|{\bm{w}}_{t}\|^{2}+\eta_{t}^{2}\|\nabla_{{\bm{w}}_{t}}\ell_{t}({\bm{w}}_{t})\|^{2}-2\eta_{t}{\bm{w}}_{t}^{\top}\allowbreak\nabla_{{\bm{w}}_{t}}\ell_{t}({\bm{w}}_{t}) , we obtain:

[278] table: ‖ 𝒘 t + 1 ‖ 2 \displaystyle\|{\bm{w}}_{t+1}\|^{2} ≥ ‖ 𝒘 t ‖ 2 − 2 ​ η t ​ ( k 1 ​ k 2 ​ H ​ σ ¯ 2 ​ ‖ 𝒘 t ‖ H ) \displaystyle\geq\|{\bm{w}}_{t}\|^{2}-2\eta_{t}\left(k_{1}k_{2}H\bar{\sigma}^{2}\|{\bm{w}}_{t}\|^{H}\right) = ‖ 𝒘 t ‖ 2 − 2 ​ ( η ~ t ‖ 𝒘 t ‖ H − 2 ) ​ k 1 ​ k 2 ​ H ​ σ ¯ 2 ​ ‖ 𝒘 t ‖ H \displaystyle=\|{\bm{w}}_{t}\|^{2}-2\left(\frac{\tilde{\eta}_{t}}{\|{\bm{w}}_{t}\|^{H-2}}\right)k_{1}k_{2}H\bar{\sigma}^{2}\|{\bm{w}}_{t}\|^{H} = ‖ 𝒘 t ‖ 2 ​ ( 1 − 2 ​ k 1 ​ k 2 ​ H ​ σ ¯ 2 ​ η ~ t ) . \displaystyle=\|{\bm{w}}_{t}\|^{2}\left(1-2k_{1}k_{2}H\bar{\sigma}^{2}\tilde{\eta}_{t}\right).

[279] p: Then, we can replace the upper bound in ( 10 ) with 1 + 4 ​ c 2 ​ k 1 ​ k 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 1+4\frac{c_{2}k_{1}k_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2} .

[280] p: As the remaining derivation for the generalization gap in Lemma 4 remains valid, we directly apply the established results by substituting c 2 c_{2} with c 2 ′ = k 1 ​ c 2 c_{2}^{\prime}=k_{1}c_{2} , and σ ¯ 2 \bar{\sigma}^{2} with σ ¯ 0 2 = k 1 ​ k 2 ​ σ ¯ 2 \bar{\sigma}^{2}_{0}=k_{1}k_{2}\bar{\sigma}^{2} . Finally, updating the definitions of m 1 m_{1} and m 2 m_{2} with these values yields the modified constants stated in Corollary 1 . ∎

[281] p: The proof of Theorem 2 can be directly derived from Theorem 1 given H = 3 H=3 .

[282] h3: B.4 Proof of Lemma 1

[283] p: Lemma 1 is a combination of Lemma 7 , Lemma 8 , and Lemma 9 .

[284] h6: Lemma 7 (Effective stepsize) .

[285] p: For an H H -homogeneous function ℓ t \ell_{t} with H ≠ 0 H\neq 0 , the effective stepsize satisfies η ~ t = η t ​ ‖ 𝐰 t ‖ H − 2 \tilde{\eta}_{t}=\eta_{t}\|{\bm{w}}_{t}\|^{H-2} , where the effective stepsize η ~ t \tilde{\eta}_{t} is defined as the stepsize in updating the direction 𝐯 t = 𝐰 t / ‖ 𝐰 t ‖ {\bm{v}}_{t}={\bm{w}}_{t}/\|{\bm{w}}_{t}\| .

[286] h6: Proof of Lemma 7 .

[287] p: For an H H -homogeneous function ℓ t \ell_{t} with H ≠ 0 H\neq 0 , it holds that

[288] table: ∇ 𝒘 t ℓ t ​ ( 𝒘 t ) = ‖ 𝒘 t ‖ H − 1 ​ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) , \nabla_{{\bm{w}}_{t}}\ell_{t}({\bm{w}}_{t})=\|{\bm{w}}_{t}\|^{H-1}\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t}), (16)

[289] p: where 𝒗 t = 𝒘 t / ‖ 𝒘 t ‖ {\bm{v}}_{t}={\bm{w}}_{t}/\|{\bm{w}}_{t}\| . This is due to the fact that ℓ t ​ ( 𝒘 t ) = ‖ 𝒘 t ‖ H ​ ℓ t ​ ( 𝒗 t ) \ell_{t}({\bm{w}}_{t})=\|{\bm{w}}_{t}\|^{H}\ell_{t}({\bm{v}}_{t}) and plug it into the definition of derivation. Therefore, we rewrite the update in ( 1 ) as

[290] table: 𝒗 t + 1 | 𝒘 t + 1 | = | 𝒘 t | ( 𝒗 t − η t ​ ‖ 𝒘 t ‖ H − 2 ​ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) ) . {\bm{v}}_{t+1}\|{\bm{w}}_{t+1}\|=\|{\bm{w}}_{t}\|({\bm{v}}_{t}-\eta_{t}\|{\bm{w}}_{t}\|^{H-2}\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})). (17)

[291] p: This implies that the update on the direction 𝒗 t {\bm{v}}_{t} has effective stepsize as η t ​ ‖ 𝒘 t ‖ H − 2 \eta_{t}\|{\bm{w}}_{t}\|^{H-2} . ∎

[292] h6: Lemma 8 (Inner Product) .

[293] p: For an H H -homogeneous function ℓ t \ell_{t} with H ≠ 0 H\neq 0 , it holds that

[294] table: 𝒘 t ⊤ ​ ∇ 𝒘 t ℓ t ​ ( 𝒘 t ) = H ​ ℓ t ​ ( 𝒘 t ) . {\bm{w}}_{t}^{\top}\nabla_{{\bm{w}}_{t}}\ell_{t}({\bm{w}}_{t})=H\ell_{t}({\bm{w}}_{t}). (18)

[295] h6: Proof of Lemma 8 .

[296] p: Note that for an H H -homogeneous ℓ t \ell_{t} , it holds that ℓ t ​ ( c ​ 𝒘 t ) = c H ​ ℓ t ​ ( 𝒘 t ) \ell_{t}(c{\bm{w}}_{t})=c^{H}\ell_{t}({\bm{w}}_{t}) . By taking derivation on c c , it holds that

[297] table: 𝒘 t ⊤ ​ ∇ ℓ t ​ ( c ​ 𝒘 t ) ∇ c 𝒘 t = H ​ c H − 1 ​ ℓ t ​ ( 𝒘 t ) . {\bm{w}}_{t}^{\top}\frac{\nabla\ell_{t}(c{\bm{w}}_{t})}{\nabla c{\bm{w}}_{t}}=Hc^{H-1}\ell_{t}({\bm{w}}_{t}).

[298] p: Taking c = 1 c=1 leads to

[299] table: 𝒘 t ⊤ ​ ∇ 𝒘 t ℓ t ​ ( 𝒘 t ) = H ​ ℓ t ​ ( 𝒘 t ) . {\bm{w}}_{t}^{\top}\nabla_{{\bm{w}}_{t}}\ell_{t}({\bm{w}}_{t})=H\ell_{t}({\bm{w}}_{t}).

[300] p: ∎

[301] h6: Lemma 9 (Norm Iterate) .

[302] p: For an H H -homogeneous function ℓ t \ell_{t} with H ≠ 0 H\neq 0 , it holds that

[303] table: ‖ 𝒘 t + 1 ‖ 2 = ‖ 𝒘 t ‖ 2 ​ ( 1 + η ~ t 2 ​ ‖ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) ‖ 2 − 2 ​ H ​ η ~ t ​ ℓ t ​ ( 𝒗 t ) ) . \|{\bm{w}}_{t+1}\|^{2}=\|{\bm{w}}_{t}\|^{2}(1+\tilde{\eta}_{t}^{2}\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})\|^{2}-2H\tilde{\eta}_{t}\ell_{t}({\bm{v}}_{t})). (19)

[304] h6: Proof of Lemma 9 .

[305] p: We consider the iteration of ‖ 𝒘 t + 1 ‖ \|{\bm{w}}_{t+1}\| , as follows:

[306] table: ‖ 𝒘 t + 1 ‖ 2 = ‖ 𝒘 t − η t ​ ∇ 𝒘 t ℓ t ​ ( 𝒘 t ) ‖ 2 = ‖ 𝒘 t ‖ 2 + η t 2 ​ ‖ ∇ 𝒘 t ℓ t ​ ( 𝒘 t ) ‖ 2 − 2 ​ η t ​ 𝒘 t ⊤ ​ ∇ 𝒘 t ℓ t ​ ( 𝒘 t ) = ( i ) ‖ 𝒘 t ‖ 2 + η t 2 ​ ‖ ∇ 𝒘 t ℓ t ​ ( 𝒘 t ) ‖ 2 − 2 ​ H ​ η t ​ ℓ t ​ ( 𝒘 t ) = ( i ​ i ) ‖ 𝒘 t ‖ 2 + η t 2 ​ ‖ 𝒘 t ‖ 2 ​ ( H − 1 ) ​ ‖ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) ‖ 2 − 2 ​ H ​ η t ​ ‖ 𝒘 t ‖ H ​ ℓ t ​ ( 𝒗 t ) = ‖ 𝒘 t ‖ 2 ​ ( 1 + η t 2 ​ ‖ 𝒘 t ‖ 2 ​ ( H − 2 ) ​ ‖ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) ‖ 2 − 2 ​ H ​ η t ​ ‖ 𝒘 t ‖ H − 2 ​ ℓ t ​ ( 𝒗 t ) ) = ( i ​ i ​ i ) ‖ 𝒘 t ‖ 2 ​ ( 1 + η ~ t 2 ​ ‖ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) ‖ 2 − 2 ​ H ​ η ~ t ​ ℓ t ​ ( 𝒗 t ) ) . \begin{split}&\|{\bm{w}}_{t+1}\|^{2}\\ =&\|{\bm{w}}_{t}-\eta_{t}\nabla_{{\bm{w}}_{t}}\ell_{t}({\bm{w}}_{t})\|^{2}\\ =&\|{\bm{w}}_{t}\|^{2}+\eta_{t}^{2}\|\nabla_{{\bm{w}}_{t}}\ell_{t}({\bm{w}}_{t})\|^{2}-2\eta_{t}{\bm{w}}_{t}^{\top}\nabla_{{\bm{w}}_{t}}\ell_{t}({\bm{w}}_{t})\\ \overset{(i)}{=}&\|{\bm{w}}_{t}\|^{2}+\eta_{t}^{2}\|\nabla_{{\bm{w}}_{t}}\ell_{t}({\bm{w}}_{t})\|^{2}-2H\eta_{t}\ell_{t}({\bm{w}}_{t})\\ \overset{(ii)}{=}&\|{\bm{w}}_{t}\|^{2}+\eta_{t}^{2}\|{\bm{w}}_{t}\|^{2(H-1)}\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})\|^{2}-2H\eta_{t}\|{\bm{w}}_{t}\|^{H}\ell_{t}({\bm{v}}_{t})\\ =&\|{\bm{w}}_{t}\|^{2}(1+\eta_{t}^{2}\|{\bm{w}}_{t}\|^{2(H-2)}\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})\|^{2}-2H\eta_{t}\|{\bm{w}}_{t}\|^{H-2}\ell_{t}({\bm{v}}_{t}))\\ \overset{(iii)}{=}&\|{\bm{w}}_{t}\|^{2}(1+\tilde{\eta}_{t}^{2}\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})\|^{2}-2H\tilde{\eta}_{t}\ell_{t}({\bm{v}}_{t})).\end{split}

[307] p: where the equation ( i ) (i) is due to Lemma 8 , the equation ( i ​ i ) (ii) is based on the fact that ‖ ∇ 𝒘 t ℓ t ​ ( 𝒘 t ) ‖ = ‖ 𝒘 t ‖ H − 1 ​ ‖ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) ‖ \|\nabla_{{\bm{w}}_{t}}\ell_{t}({\bm{w}}_{t})\|=\|{\bm{w}}_{t}\|^{H-1}\allowbreak\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})\| and ℓ t ​ ( 𝒘 t ) = ‖ 𝒘 t ‖ H ​ ℓ t ​ ( 𝒗 t ) \ell_{t}({\bm{w}}_{t})=\|{\bm{w}}_{t}\|^{H}\ell_{t}({\bm{v}}_{t}) , and the equation ( i ​ i ​ i ) (iii) follows from the effective stepsize result in Lemma 7 . ∎

[308] h3: B.5 Proof of Theorem 2

[309] p: This section provides the proofs of Theorem 2 . This result is based on the following Lemma 10 and Lemma 11 . Lemma 10 demonstrate that the effective stepsize would be 𝒪 ⁡ ( 1 t ​ log ⁡ t ) \mathcal{O}(\frac{1}{t\log t}) given the stepsize E 𝒜 , 𝒟 ​ η t = 𝒪 ⁡ ( 1 / t ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}=\mathcal{O}(1/t) . As a comparison, the effective stepsize used in the first statement of Lemma 3 would be Θ ⁡ ( 1 / t ) \Theta(1/t) , given a stepsize Ω ⁡ ( 1 / t ) \Omega(1/\sqrt{t}) . Lemma 11 further derives the convergence rate given the effective stepsize. Combining Lemma 10 and Lemma 11 leads to Theorem 2 .

[310] h6: Lemma 10 (The Effective Stepsize for Stepsize 𝒪 ⁡ ( 1 / t ) \mathcal{O}(1/t) ) .

[311] p: Under the settings in Theorem 2 , there exist infinitely many stepsizes satisfies E 𝒜 , 𝒟 ​ η t = 𝒪 ⁡ ( 1 / t ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}=\mathcal{O}(1/t) , such that the effective stepsize satisfies η ~ t = 𝒪 ⁡ ( 1 t ​ log ⁡ t ) \tilde{\eta}_{t}=\mathcal{O}(\frac{1}{t\log t}) .

[312] h6: Proof of Lemma 10 .

[313] p: Firstly, notice that according to Lemma 12 , it holds that

[314] table: E 𝒜 , 𝒟 ​ ‖ 𝐰 t + 1 ‖ 2 ≤ E 𝒜 , 𝒟 ​ ‖ 𝐰 t ‖ 2 ​ ( 1 − 1 2 ​ H ​ σ ¯ 2 ​ η ~ t ) ≤ E 𝒜 , 𝒟 ​ ‖ 𝐰 t ‖ 2 ​ exp ⁡ ( − 1 2 ​ H ​ σ ¯ 2 ​ η ~ t ) , \mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t+1}\|^{2}\leq\mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t}\|^{2}\left(1-\frac{1}{2}H\underline{\sigma}^{2}\tilde{\eta}_{t}\right)\leq\mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t}\|^{2}\exp\left(-\frac{1}{2}H\underline{\sigma}^{2}\tilde{\eta}_{t}\right),

[315] p: By taking η t \eta_{t} such that η ~ t = 4 H ​ σ ¯ 2 ​ ( ( t + 2 ) ​ log ⁡ ( t + 2 ) ) \tilde{\eta}_{t}=\frac{4}{H\underline{\sigma}^{2}((t+2)\log(t+2))} , it holds that for T > 0 T>0

[316] table: E 𝒜 , 𝒟 ​ ‖ 𝐰 T ‖ 2 ≤ exp ⁡ ( − 1 2 ​ H ​ σ ¯ 2 ​ η ~ T − 1 ) ​ E 𝒜 , 𝒟 ​ ‖ 𝐰 T − 1 ‖ 2 ≤ exp ( − 1 2 H σ ¯ 2 ∑ t ∈ [ T ] η ~ t ) E 𝒜 ∥ 𝐰 0 ∥ 2 ≤ E 𝒜 ​ ‖ 𝐰 0 ‖ 2 ( log ⁡ T ) 2 , \begin{split}\mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{T}\|^{2}\leq&\exp\left(-\frac{1}{2}H\underline{\sigma}^{2}\tilde{\eta}_{T-1}\right)\mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{T-1}\|^{2}\\ \leq&\exp\left(-\frac{1}{2}H\underline{\sigma}^{2}\sum_{t\in[T]}\tilde{\eta}_{t}\right)\mathbb{E}_{\mathcal{A}}\|{\bm{w}}_{0}\|^{2}\\ \leq&\frac{\mathbb{E}_{\mathcal{A}}\|{\bm{w}}_{0}\|^{2}}{(\log T)^{2}},\end{split}

[317] p: where we use the fact that ∑ t ∈ [ T ] 1 ( t + 2 ) ​ log ⁡ ( t + 2 ) ≤ log ⁡ ( log ⁡ ( T ) ) \sum_{t\in[T]}\frac{1}{(t+2)\log(t+2)}\leq\log(\log(T)) . This leads to the learning rate

[318] table: E 𝒜 , 𝒟 ​ η t = E 𝒜 , 𝒟 ​ η ~ t ‖ 𝐰 t ‖ ≥ η ~ t [ E 𝒜 , 𝒟 ​ ‖ 𝐰 t ‖ 2 ] 1 / 2 = 4 ​ log ⁡ t E 𝒜 ​ ‖ 𝐰 0 ‖ 2 ​ H ​ σ ¯ 2 ​ ( t + 2 ) ​ log ⁡ ( t + 2 ) = Ω ⁡ ( 1 / t ) , \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}=\mathbb{E}_{\mathcal{A},\mathcal{D}}\frac{\tilde{\eta}_{t}}{\|{\bm{w}}_{t}\|}\geq\frac{\tilde{\eta}_{t}}{[\mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t}\|^{2}]^{1/2}}=\frac{4\log t}{\sqrt{\mathbb{E}_{\mathcal{A}}\|{\bm{w}}_{0}\|^{2}}H\underline{\sigma}^{2}(t+2)\log(t+2)}=\Omega(1/t),

[319] p: where we use Jensen’s inequality, and the assumption that E 𝒜 ​ ‖ 𝐰 0 ‖ 2 \mathbb{E}_{\mathcal{A}}\|{\bm{w}}_{0}\|^{2} is a constant.

[320] p: We next prove Lemma 10 by contradiction. Assume that the stepsize E 𝒜 , 𝒟 ​ η t = 𝒪 ⁡ ( 1 / t ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\eta_{t}=\mathcal{O}(1/t) corresponds to a larger effective stepsize η ~ t = ω ⁡ ( 1 t ​ log ⁡ t ) \tilde{\eta}_{t}=\omega(\frac{1}{t\log t}) . In this case, it still holds for the weight norm that E 𝒜 , 𝒟 ​ ‖ 𝐰 T ‖ 2 = 𝒪 ⁡ ( E 𝒜 , 𝒟 ​ ‖ 𝐰 0 ‖ 2 ( log ⁡ T ) 2 ) \mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{T}\|^{2}=\mathcal{O}(\frac{\mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{0}\|^{2}}{(\log T)^{2}}) . Therefore, the corresponding learning rate would become larger according to the inequality that E 𝒜 ​ η t ≥ η ~ t [ E 𝒜 , 𝒟 ​ ‖ 𝐰 t ‖ 2 ] 1 / 2 = ω ⁡ ( 1 / t ) \mathbb{E}_{\mathcal{A}}\eta_{t}\geq\frac{\tilde{\eta}_{t}}{[\mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t}\|^{2}]^{1/2}}=\omega(1/t) , which contradict with the statement that η t = 𝒪 ⁡ ( 1 / t ) \eta_{t}=\mathcal{O}(1/t) . Therefore, given the stepsize η t = 𝒪 ⁡ ( 1 / t ) \eta_{t}=\mathcal{O}(1/t) , the corresponding effective learning rate must be η ~ t = 𝒪 ⁡ ( 1 t ​ log ⁡ t ) \tilde{\eta}_{t}=\mathcal{O}(\frac{1}{t\log t}) . The proof is done. ∎

[321] h6: Lemma 11 .

[322] p: Under the assumptions in Theorem 2 with smoothness (parameter β \beta ), PL condition (parameter μ \mu ), strong growth condition (parameter B B ) and E I ​ ℒ ^ ​ ( 𝐯 t ) ≥ ( 1 + α ) / α ​ ℒ ^ ​ ( 𝐯 ∗ ) \mathbb{E}_{I}\hat{\mathcal{L}}({\bm{v}}_{t})\geq(1+\alpha)/\alpha\hat{\mathcal{L}}({\bm{v}}^{*}) , given the effective learning rate η ~ t ≤ 1 β ​ B 2 \tilde{\eta}_{t}\leq\frac{1}{\beta B^{2}} , the convergence rate would be

[323] table: E 𝒜 , 𝒟 ℒ ^ ( 𝐯 T ) − min 𝐯 ℒ ^ ( 𝐯 ) ≤ exp ( − λ ∑ η ~ t ) E 𝒜 , 𝒟 ( ℒ ^ ( 𝐯 0 ) − min 𝐯 ℒ ^ ( 𝐯 ) ) . \mathbb{E}_{\mathcal{A},\mathcal{D}}\hat{\mathcal{L}}({\bm{v}}_{T})-\min_{\bm{v}}\hat{\mathcal{L}}({\bm{v}})\leq\exp\left(-\lambda\sum\tilde{\eta}_{t}\right)\mathbb{E}_{\mathcal{A},\mathcal{D}}(\hat{\mathcal{L}}({\bm{v}}_{0})-\min_{\bm{v}}\hat{\mathcal{L}}({\bm{v}})).

[324] p: Therefore, taking η ~ t = c / t \tilde{\eta}_{t}=c/t leads to

[325] table: E 𝒜 , 𝒟 ​ ℒ ^ ​ ( 𝐯 T ) − min 𝐯 ⁡ ℒ ^ ​ ( 𝐯 ) ≤ 1 T c ​ λ ​ E 𝒜 , 𝒟 ​ ( ℒ ^ ​ ( 𝐯 0 ) − min 𝐯 ⁡ ℒ ^ ​ ( 𝐯 ) ) . \mathbb{E}_{\mathcal{A},\mathcal{D}}\hat{\mathcal{L}}({\bm{v}}_{T})-\min_{\bm{v}}\hat{\mathcal{L}}({\bm{v}})\leq\frac{1}{T^{c\lambda}}\mathbb{E}_{\mathcal{A},\mathcal{D}}(\hat{\mathcal{L}}({\bm{v}}_{0})-\min_{\bm{v}}\hat{\mathcal{L}}({\bm{v}})).

[326] p: Taking η ~ t = c / [ t ​ log ⁡ t ] \tilde{\eta}_{t}=c/[t\log t] leads to

[327] table: E 𝒜 , 𝒟 ​ ℒ ^ ​ ( 𝐯 T ) − min 𝐯 ⁡ ℒ ^ ​ ( 𝐯 ) ≤ 1 [ log ⁡ T ] c ​ λ ​ E 𝒜 , 𝒟 ​ ( ℒ ^ ​ ( 𝐯 0 ) − min 𝐯 ⁡ ℒ ^ ​ ( 𝐯 ) ) . \mathbb{E}_{\mathcal{A},\mathcal{D}}\hat{\mathcal{L}}({\bm{v}}_{T})-\min_{\bm{v}}\hat{\mathcal{L}}({\bm{v}})\leq\frac{1}{[\log T]^{c\lambda}}\mathbb{E}_{\mathcal{A},\mathcal{D}}(\hat{\mathcal{L}}({\bm{v}}_{0})-\min_{\bm{v}}\hat{\mathcal{L}}({\bm{v}})).

[328] h6: Proof of Lemma 11 .

[329] p: For the ease of notation, denote 𝒗 ∗ {\bm{v}}^{*} as the one of the vectors which attains ℒ ^ ​ ( 𝒗 ∗ ) = min 𝒗 ⁡ ℒ ^ ​ ( 𝒗 ) \hat{\mathcal{L}}({\bm{v}}^{*})=\min_{\bm{v}}\hat{\mathcal{L}}({\bm{v}}) . We first focus on the unconstrained iteration on the sphere, that is

[330] table: 𝒗 ¯ t + 1 = 𝒗 t − η ~ t ​ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) . \bar{{\bm{v}}}_{t+1}={\bm{v}}_{t}-\tilde{\eta}_{t}\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t}).

[331] p: Notice that by strong growth condition, it holds that ( ( Schmidt and Roux, 2013 ) , (12)) when η ~ t ≤ 1 β ​ B 2 \tilde{\eta}_{t}\leq\frac{1}{\beta B^{2}}

[332] table: E I ​ ℒ ^ ​ ( 𝐯 ¯ t + 1 ) ≤ ℒ ^ ​ ( 𝐯 t ) − η ~ t ​ ( 1 − η ~ t ​ β ​ B 2 2 ) ​ ‖ ∇ 𝐯 t ℒ ^ ​ ( 𝐯 t ) ‖ 2 ≤ ℒ ^ ​ ( 𝐯 t ) − η ~ t 2 ​ ‖ ∇ 𝐯 t ℒ ^ ​ ( 𝐯 t ) ‖ 2 . \mathbb{E}_{I}\hat{\mathcal{L}}(\bar{{\bm{v}}}_{t+1})\leq\hat{\mathcal{L}}({\bm{v}}_{t})-\tilde{\eta}_{t}\left(1-\frac{\tilde{\eta}_{t}\beta B^{2}}{2}\right)\|\nabla_{{\bm{v}}_{t}}\hat{\mathcal{L}}({\bm{v}}_{t})\|^{2}\leq\hat{\mathcal{L}}({\bm{v}}_{t})-\frac{\tilde{\eta}_{t}}{2}\|\nabla_{{\bm{v}}_{t}}\hat{\mathcal{L}}({\bm{v}}_{t})\|^{2}. (20)

[333] p: Besides, by PL condition and strong growth condition, for any t t and 𝒗 t {\bm{v}}_{t} , it holds that

[334] table: ‖ ∇ 𝒗 t ℒ ^ ​ ( 𝒗 t ) ‖ 2 ≥ 1 B 2 ​ max i ​ { ‖ ∇ 𝒗 t ℓ i ​ t ​ ( 𝒗 t ) ‖ 2 } ≥ 2 ​ μ B 2 ​ ( ℓ i ​ t ​ ( 𝒗 t ) − ℓ i ​ t ​ ( 𝒗 ∗ ) ) . \|\nabla_{{\bm{v}}_{t}}\hat{\mathcal{L}}({\bm{v}}_{t})\|^{2}\geq\frac{1}{B^{2}}\max_{i}\{\|\nabla_{{\bm{v}}_{t}}\ell_{i}t({\bm{v}}_{t})\|^{2}\}\geq\frac{2\mu}{B^{2}}(\ell_{i}t({\bm{v}}_{t})-\ell_{i}t({\bm{v}}^{*})).

[335] p: By taking expectation E I \mathbb{E}_{I} over the last iteration, it holds that (note that 𝒗 t {\bm{v}}_{t} is independent of the choice of the last iteration ℓ t \ell_{t} )

[336] table: ‖ ∇ 𝒗 t ℒ ^ ​ ( 𝒗 t ) ‖ 2 ≥ 2 ​ μ B 2 ​ ( E I ​ ℓ i ​ ( 𝐯 t ) − E I ​ ℓ i ​ ( 𝐯 ∗ ) ) ≥ 2 ​ μ B 2 ​ ( ℒ ^ ​ ( 𝐯 t ) − ℒ ^ ​ ( 𝐯 ∗ ) ) . \|\nabla_{{\bm{v}}_{t}}\hat{\mathcal{L}}({\bm{v}}_{t})\|^{2}\geq\frac{2\mu}{B^{2}}(\mathbb{E}_{I}\ell_{i}({\bm{v}}_{t})-\mathbb{E}_{I}\ell_{i}({\bm{v}}^{*}))\geq\frac{2\mu}{B^{2}}(\hat{\mathcal{L}}({\bm{v}}_{t})-\hat{\mathcal{L}}({\bm{v}}^{*})). (21)

[337] p: Combining ( 20 ) and ( 21 )leads to

[338] table: OPEN E I ​ ℒ ^ ​ ( 𝐯 ¯ t + 1 ) ≤ ( 1 − η ~ t ​ μ B 2 ) ​ ℒ ^ ​ ( 𝐯 t ) + η ~ t ​ μ B 2 ​ ℒ ^ ​ ( 𝐯 ∗ ) ) . \mathbb{E}_{I}\hat{\mathcal{L}}(\bar{{\bm{v}}}_{t+1})\leq\left(1-\frac{\tilde{\eta}_{t}\mu}{B^{2}}\right)\hat{\mathcal{L}}({\bm{v}}_{t})+\frac{\tilde{\eta}_{t}\mu}{B^{2}}\hat{\mathcal{L}}({\bm{v}}^{*})).

[339] p: Next, we project 𝒗 ¯ t + 1 \bar{{\bm{v}}}_{t+1} back onto the unit sphere. Analogous to Lemma 5 , it holds that ‖ 𝒘 t ‖ ‖ 𝒘 t + 1 ‖ ≤ ( 1 − 2 ​ H ​ σ ¯ 2 ​ η ~ t ) − 1 2 ≤ 1 + 2 ​ H ​ σ ¯ 2 ​ η ~ t \frac{\|{\bm{w}}_{t}\|}{\|{\bm{w}}_{t+1}\|}\leq(1-2H\bar{\sigma}^{2}\tilde{\eta}_{t})^{-\frac{1}{2}}\leq 1+2H\bar{\sigma}^{2}\tilde{\eta}_{t} . Thus:

[340] table: E I ​ ℒ ^ ​ ( 𝐯 t + 1 ) − ℒ ^ ​ ( 𝐯 ∗ ) = E I ​ [ ‖ 𝐰 t ‖ ‖ 𝐰 t + 1 ‖ ] H ​ ℒ ^ ​ ( 𝐯 ¯ t + 1 ) − ℒ ^ ​ ( 𝐯 ∗ ) ≤ ( 1 + 4 ​ H 2 ​ σ ¯ 2 ​ η ~ t ) ​ [ ( 1 − η ~ t ​ μ B 2 ) ​ E I ​ ℒ ^ ​ ( 𝐯 t ) + η ~ t ​ μ B 2 ​ ℒ ^ ​ ( 𝐯 ∗ ) ] − ℒ ^ ​ ( 𝒗 ∗ ) = ( 1 + 4 ​ H 2 ​ σ ¯ 2 ​ η ~ t ) ​ ( 1 − η ~ t ​ μ B 2 ) ​ ( E I ​ ℒ ^ ​ ( 𝐯 t ) − ℒ ^ ​ ( 𝐯 ∗ ) ) + 4 ​ H 2 ​ σ ¯ 2 ​ η ~ t ​ ℒ ^ ​ ( 𝒗 ∗ ) . \begin{split}\mathbb{E}_{I}\hat{\mathcal{L}}({\bm{v}}_{t+1})-\hat{\mathcal{L}}({\bm{v}}^{*})&=\mathbb{E}_{I}\left[\frac{\|{\bm{w}}_{t}\|}{\|{\bm{w}}_{t+1}\|}\right]^{H}\hat{\mathcal{L}}(\bar{{\bm{v}}}_{t+1})-\hat{\mathcal{L}}({\bm{v}}^{*})\\ &\leq(1+4H^{2}\bar{\sigma}^{2}\tilde{\eta}_{t})\left[\left(1-\frac{\tilde{\eta}_{t}\mu}{B^{2}}\right)\mathbb{E}_{I}\hat{\mathcal{L}}({\bm{v}}_{t})+\frac{\tilde{\eta}_{t}\mu}{B^{2}}\hat{\mathcal{L}}({\bm{v}}^{*})\right]-\hat{\mathcal{L}}({\bm{v}}^{*})\\ &=(1+4H^{2}\bar{\sigma}^{2}\tilde{\eta}_{t})\left(1-\frac{\tilde{\eta}_{t}\mu}{B^{2}}\right)\left(\mathbb{E}_{I}\hat{\mathcal{L}}({\bm{v}}_{t})-\hat{\mathcal{L}}({\bm{v}}^{*})\right)+4H^{2}\bar{\sigma}^{2}\tilde{\eta}_{t}\hat{\mathcal{L}}({\bm{v}}^{*}).\end{split}

[341] p: By E I ​ ℒ ^ ​ ( 𝐯 t ) ≥ ( 1 + α ) / α ​ ℒ ^ ​ ( 𝐯 ∗ ) \mathbb{E}_{I}\hat{\mathcal{L}}({\bm{v}}_{t})\geq(1+\alpha)/\alpha\hat{\mathcal{L}}({\bm{v}}^{*}) , it holds that:

[342] table: E I ​ ℒ ^ ​ ( 𝐯 t + 1 ) − ℒ ^ ​ ( 𝐯 ∗ ) ≤ ( 1 + 4 ​ H 2 ​ σ ¯ 2 ​ η ~ t ) ​ ( 1 − η ~ t ​ μ B 2 ) ​ ( E I ​ ℒ ^ ​ ( 𝐯 t ) − ℒ ^ ​ ( 𝐯 ∗ ) ) + 4 ​ α ​ H 2 ​ σ ¯ 2 ​ η ~ t ​ ( E I ​ ℒ ^ ​ ( 𝐯 t ) − ℒ ^ ​ ( 𝐯 ∗ ) ) ≤ [ 1 − η ~ t ​ ( μ B 2 − 4 ​ H 2 ​ σ ¯ 2 ​ ( 1 + α ) ) ] ​ ( E I ​ ℒ ^ ​ ( 𝐯 t + 1 ) − ℒ ^ ​ ( 𝐯 ∗ ) ) . \begin{split}\mathbb{E}_{I}\hat{\mathcal{L}}({\bm{v}}_{t+1})-\hat{\mathcal{L}}({\bm{v}}^{*})&\leq(1+4H^{2}\bar{\sigma}^{2}\tilde{\eta}_{t})\left(1-\frac{\tilde{\eta}_{t}\mu}{B^{2}}\right)\left(\mathbb{E}_{I}\hat{\mathcal{L}}({\bm{v}}_{t})-\hat{\mathcal{L}}({\bm{v}}^{*})\right)\\ &\quad+4\alpha H^{2}\bar{\sigma}^{2}\tilde{\eta}_{t}\left(\mathbb{E}_{I}\hat{\mathcal{L}}({\bm{v}}_{t})-\hat{\mathcal{L}}({\bm{v}}^{*})\right)\\ &\leq\left[1-\tilde{\eta}_{t}\left(\frac{\mu}{B^{2}}-4H^{2}\bar{\sigma}^{2}(1+\alpha)\right)\right]\left(\mathbb{E}_{I}\hat{\mathcal{L}}({\bm{v}}_{t+1})-\hat{\mathcal{L}}({\bm{v}}^{*})\right).\end{split}

[343] p: Note that λ ≜ μ B 2 − 4 ​ H 2 ​ σ ¯ 2 ​ ( 1 + α ) > 0 \lambda\triangleq\frac{\mu}{B^{2}}-4H^{2}\bar{\sigma}^{2}(1+\alpha)>0 . Taking the expectation over the algorithm and dataset, the convergence would be

[344] table: E 𝒜 , 𝒟 ​ ℒ ^ ​ ( 𝐯 t + 1 ) − ℒ ^ ​ ( 𝐯 ∗ ) ≤ E 𝒜 , 𝒟 ​ ( ℒ ^ ​ ( 𝐯 0 ) − ℒ ^ ​ ( 𝐯 ∗ ) ) ​ ∏ ( 1 − η ~ t ​ λ ) ≤ exp ( − λ ∑ η ~ t ) E 𝒜 , 𝒟 ( ℒ ^ ( 𝐯 0 ) − ℒ ^ ( 𝐯 ∗ ) ) . \begin{split}\mathbb{E}_{\mathcal{A},\mathcal{D}}\hat{\mathcal{L}}({\bm{v}}_{t+1})-\hat{\mathcal{L}}({\bm{v}}^{*})\leq&\mathbb{E}_{\mathcal{A},\mathcal{D}}(\hat{\mathcal{L}}({\bm{v}}_{0})-\hat{\mathcal{L}}({\bm{v}}^{*}))\prod(1-\tilde{\eta}_{t}\lambda)\\ \leq&\exp(-\lambda\sum\tilde{\eta}_{t})\mathbb{E}_{\mathcal{A},\mathcal{D}}(\hat{\mathcal{L}}({\bm{v}}_{0})-\hat{\mathcal{L}}({\bm{v}}^{*})).\end{split}

[345] p: ∎

[346] h3: B.6 Technical Lemmas

[347] h6: Lemma 12 (Weight Norm Iteration) .

[348] p: Under Assumption 1 and Assumption 2 , assume that H > 0 H>0 and η ~ t ≤ H ​ σ ¯ 2 2 ​ L 2 \tilde{\eta}_{t}\leq\frac{H\underline{\sigma}^{2}}{2L^{2}} , if the loss is H H -homogeneous, it holds that

[349] table: E 𝒜 , 𝒟 ​ ‖ 𝐰 t + 1 ‖ 2 ≤ E 𝒜 , 𝒟 ​ ‖ 𝐰 t ‖ 2 ​ ( 1 − 1 2 ​ H ​ σ ¯ 2 ​ η ~ t ) , \mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t+1}\|^{2}\leq\mathbb{E}_{\mathcal{A},\mathcal{D}}\|{\bm{w}}_{t}\|^{2}(1-\frac{1}{2}H\underline{\sigma}^{2}\tilde{\eta}_{t}),

[350] p: where the expectation E 𝒜 \mathbb{E}_{\mathcal{A}} is taken over the training algorithm.

[351] h6: Proof of Lemma 12 .

[352] p: Note that due to Lemma 1 (argument 3), it holds that

[353] table: E I ​ ‖ 𝐰 t + 1 ‖ 2 = E I ​ ‖ 𝐰 t ‖ 2 ​ ( 1 + η ~ t 2 ​ ‖ ∇ 𝐯 t ℓ t ​ ( 𝐯 t ) ‖ 2 − 2 ​ H ​ η ~ t ​ ℓ t ​ ( 𝐯 t ) ) = ‖ 𝒘 t ‖ 2 ​ ( 1 + η ~ t 2 ​ E I ​ ‖ ∇ 𝐯 t ℓ t ​ ( 𝐯 t ) ‖ 2 − 2 ​ H ​ η ~ t ​ ℒ ^ ​ ( 𝐯 t ) ) , \begin{split}\mathbb{E}_{I}\|{\bm{w}}_{t+1}\|^{2}=&\mathbb{E}_{I}\|{\bm{w}}_{t}\|^{2}(1+\tilde{\eta}_{t}^{2}\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})\|^{2}-2H\tilde{\eta}_{t}\ell_{t}({\bm{v}}_{t}))\\ =&\|{\bm{w}}_{t}\|^{2}(1+\tilde{\eta}_{t}^{2}\mathbb{E}_{I}\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})\|^{2}-2H\tilde{\eta}_{t}\hat{\mathcal{L}}({\bm{v}}_{t})),\end{split}

[354] p: where the expectation E I \mathbb{E}_{I} is taken over the choice of the last iteration. Note that we use the fact that 𝒗 t {\bm{v}}_{t} is independent of the choice of the last iteration (namely, ℓ t \ell_{t} ), and therefore,

[355] table: E I ​ ℓ t ​ ( 𝐯 t ) = 1 n ​ ∑ i ∈ [ n ] ℓ t ​ ( 𝐯 t , X i , Y i ) = ℒ ^ t ​ ( 𝐯 t ) . \mathbb{E}_{I}\ell_{t}({\bm{v}}_{t})=\frac{1}{n}\sum_{i\in[n]}\ell_{t}({\bm{v}}_{t};X_{i},Y_{i})=\hat{\mathcal{L}}_{t}({\bm{v}}_{t}).

[356] p: We next plug the bound of Assumption 1 , that is, ℒ ^ ​ ( 𝒗 t ) ≥ 1 2 ​ σ ¯ 2 \hat{\mathcal{L}}({\bm{v}}_{t})\geq\frac{1}{2}\underline{\sigma}^{2} , and the bound of Assumption 2 , that is, sup 𝒗 : ‖ 𝒗 ‖ = 1 ∥ ∇ 𝒗 ℓ t ( 𝒗 ) ∥ ≤ L \sup_{{\bm{v}}:\|{\bm{v}}\|=1}\|\nabla_{{\bm{v}}}\ell_{t}({\bm{v}})\|\leq L , namely,

[357] table: E I ​ ‖ 𝐰 t + 1 ‖ 2 ≤ ‖ 𝒘 t ‖ 2 ​ ( 1 + η ~ t 2 ​ L 2 − 2 ​ H ​ η ~ t ​ ℒ ^ ​ ( 𝒗 t ) ) ≤ ‖ 𝒘 t ‖ 2 ​ ( 1 + η ~ t 2 ​ L 2 − H ​ η ~ t ​ σ ¯ 2 ) ≤ ‖ 𝒘 t ‖ 2 ​ ( 1 − η ~ t ​ ( H ​ σ ¯ 2 − η ~ t ​ L 2 ) ) . \begin{split}\mathbb{E}_{I}\|{\bm{w}}_{t+1}\|^{2}\leq&\|{\bm{w}}_{t}\|^{2}(1+\tilde{\eta}_{t}^{2}L^{2}-2H\tilde{\eta}_{t}\hat{\mathcal{L}}({\bm{v}}_{t}))\\ \leq&\|{\bm{w}}_{t}\|^{2}(1+\tilde{\eta}_{t}^{2}L^{2}-H\tilde{\eta}_{t}\underline{\sigma}^{2})\\ \leq&\|{\bm{w}}_{t}\|^{2}(1-\tilde{\eta}_{t}(H\underline{\sigma}^{2}-\tilde{\eta}_{t}L^{2})).\end{split}

[358] p: By the requirement that η ~ t ≤ H ​ σ ¯ 2 2 ​ L 2 \tilde{\eta}_{t}\leq\frac{H\underline{\sigma}^{2}}{2L^{2}} , it holds that

[359] table: E I ​ ‖ 𝐰 t + 1 ‖ 2 ≤ ‖ 𝒘 t ‖ 2 ​ ( 1 − 1 2 ​ H ​ σ ¯ 2 ​ η ~ t ) . \begin{split}\mathbb{E}_{I}\|{\bm{w}}_{t+1}\|^{2}\leq&\|{\bm{w}}_{t}\|^{2}(1-\frac{1}{2}H\underline{\sigma}^{2}\tilde{\eta}_{t}).\end{split}

[360] p: Taking expectations over the whole algorithm and the dataset finishes the proof.

[361] p: Remark: Extension to the non-Lipschitz setting. This result extends to the non-Lipschitz scenario. The analysis relies on the self-bounding property of β \beta -smooth functions:

[362] table: E I ​ ‖ 𝐰 t + 1 ‖ 2 ≤ ‖ 𝒘 t ‖ 2 ​ ( 1 + 2 ​ β ​ η ~ t 2 ​ E I ​ [ ℓ t ​ ( 𝐯 t ) ] − 2 ​ H ​ η ~ t ​ ℒ ^ ​ ( 𝐯 t ) ) = ‖ 𝒘 t ‖ 2 ​ ( 1 + 2 ​ β ​ η ~ t 2 ​ ℒ ^ ​ ( 𝒗 t ) − 2 ​ H ​ η ~ t ​ ℒ ^ ​ ( 𝒗 t ) ) = ‖ 𝒘 t ‖ 2 ​ ( 1 − 2 ​ η ~ t ​ ℒ ^ ​ ( 𝒗 t ) ​ ( H − β ​ η ~ t ) ) ≤ ‖ 𝒘 t ‖ 2 ​ ( 1 − σ ¯ 2 ​ η ~ t ​ ( H − β ​ η ~ t ) ) . \begin{split}\mathbb{E}_{I}\|{\bm{w}}_{t+1}\|^{2}\leq&\|{\bm{w}}_{t}\|^{2}(1+2\beta\tilde{\eta}_{t}^{2}\mathbb{E}_{I}[\ell_{t}({\bm{v}}_{t})]-2H\tilde{\eta}_{t}\hat{\mathcal{L}}({\bm{v}}_{t}))\\ =&\|{\bm{w}}_{t}\|^{2}(1+2\beta\tilde{\eta}_{t}^{2}\hat{\mathcal{L}}({\bm{v}}_{t})-2H\tilde{\eta}_{t}\hat{\mathcal{L}}({\bm{v}}_{t}))\\ =&\|{\bm{w}}_{t}\|^{2}(1-2\tilde{\eta}_{t}\hat{\mathcal{L}}({\bm{v}}_{t})(H-\beta\tilde{\eta}_{t}))\\ \leq&\|{\bm{w}}_{t}\|^{2}(1-\underline{\sigma}^{2}\tilde{\eta}_{t}(H-\beta\tilde{\eta}_{t})).\end{split}

[363] p: Consequently, if η ~ t ≤ H 2 ​ β \tilde{\eta}_{t}\leq\frac{H}{2\beta} , we still obtain:

[364] table: E I ​ ‖ 𝐰 t + 1 ‖ 2 ≤ ‖ 𝒘 t ‖ 2 ​ ( 1 − 1 2 ​ H ​ σ ¯ 2 ​ η ~ t ) . \begin{split}\mathbb{E}_{I}\|{\bm{w}}_{t+1}\|^{2}\leq&\|{\bm{w}}_{t}\|^{2}(1-\frac{1}{2}H\underline{\sigma}^{2}\tilde{\eta}_{t}).\end{split}

[365] p: ∎

[366] h3: B.7 Proofs for Section 4

[367] p: This section provides the proof for the results presented in Section 4 . We first derive Lemma 2 , and subsequently establish Theorem 4 .

[368] h4: B.7.1 Proof of Lemma 2

[369] h6: Proof.

[370] p: This proof decomposes the generalization gap by utilizing the notion of conditional on-average stability (Definition 2 ).

[371] p: Let z i ≜ ( X i , Y i ) z_{i}\triangleq({X}_{i},{Y}_{i}) and define the individual loss difference on the i i -th sample as δ ⁡ ( 𝒗 T , 𝒗 T ( i ) ) ≜ | ℓ ⁡ ( 𝒗 T , z i ) − ℓ ⁡ ( 𝒗 T ( i ) , z i ) | \delta({\bm{v}}_{T},{\bm{v}}_{T}^{(i)})\triangleq|\ell({\bm{v}}_{T};z_{i})-\ell({\bm{v}}_{T}^{(i)};z_{i})| . Following the standard stability analysis in Bousquet and Elisseeff (2002) , we have

[372] table: E 𝒜 , 𝒟 ​ [ ℒ s ​ ( 𝐰 T ) − ℒ ^ s ​ ( 𝐰 T ) ] \displaystyle\mathbb{E}_{\mathcal{A},\mathcal{D}}[\mathcal{L}^{s}({\bm{w}}_{T})-\hat{\mathcal{L}}^{s}({\bm{w}}_{T})] = E 𝒜 , 𝒟 ​ [ ℒ ⁡ ( 𝐯 T ) − ℒ ^ ​ ( 𝐯 T ) ] \displaystyle=\mathbb{E}_{\mathcal{A},\mathcal{D}}[\mathcal{L}({\bm{v}}_{T})-\hat{\mathcal{L}}({\bm{v}}_{T})] = E 𝒜 , 𝒟 ​ [ 1 n ​ ∑ i = 1 n ℓ ⁡ ( 𝐯 T ( i ) , z i ) − 1 n ​ ∑ i = 1 n ℓ ⁡ ( 𝐯 T , z i ) ] \displaystyle=\mathbb{E}_{\mathcal{A},\mathcal{D}}[\frac{1}{n}\sum_{i=1}^{n}\ell({\bm{v}}_{T}^{(i)};z_{i})-\frac{1}{n}\sum_{i=1}^{n}\ell({\bm{v}}_{T};z_{i})] ≤ 1 n ​ ∑ i = 1 n E 𝒜 , 𝒟 ​ [ δ ⁡ ( 𝐯 T , 𝐯 T ( i ) ) ] . \displaystyle\leq\frac{1}{n}\sum_{i=1}^{n}\mathbb{E}_{\mathcal{A},\mathcal{D}}[\delta({\bm{v}}_{T},{\bm{v}}_{T}^{(i)})].

[373] p: Let ℰ ( i ) \mathcal{E}_{(i)} denote the event that the algorithm 𝒜 \mathcal{A} does not select the index i i within the first t 0 t_{0} iterations. The probability of the complement event ℰ ( i ) c \mathcal{E}_{(i)}^{c} (i.e., index i i is selected at least once) is bounded by:

[374] table: P ⁡ ( ℰ ( i ) c ) ≤ ∑ t = 1 t 0 1 n = t 0 n , P(\mathcal{E}_{(i)}^{c})\leq\sum_{t=1}^{t_{0}}\frac{1}{n}=\frac{t_{0}}{n},

[375] p: Analogous to the technique in ( 12 ), invoking the Bounded Loss assumption (Assumption 1 ) yields:

[376] table: E ⁡ [ δ ⁡ ( 𝐯 T , 𝐯 T ( i ) ) ] \displaystyle\mathbb{E}[\delta({\bm{v}}_{T},{\bm{v}}_{T}^{(i)})] = P ⁡ ( ℰ ( i ) c ) ​ E ​ [ δ ⁡ ( 𝐯 T , 𝐯 T ( i ) ) ∣ ℰ ( i ) c ] + P ⁡ ( ℰ ( i ) ) ​ E ​ [ δ ⁡ ( 𝐯 T , 𝐯 T ( i ) ) ∣ ℰ ( i ) ] \displaystyle=P(\mathcal{E}_{(i)}^{c})\mathbb{E}[\delta({\bm{v}}_{T},{\bm{v}}_{T}^{(i)})\mid\mathcal{E}_{(i)}^{c}]+P(\mathcal{E}_{(i)})\mathbb{E}[\delta({\bm{v}}_{T},{\bm{v}}_{T}^{(i)})\mid\mathcal{E}_{(i)}] ≤ t 0 n ⋅ σ ¯ 2 + E ⁡ [ δ ⁡ ( 𝐯 T , 𝐯 T ( i ) ) ∣ ℰ ( i ) ] . \displaystyle\leq\frac{t_{0}}{n}\cdot\bar{\sigma}^{2}+\mathbb{E}[\delta({\bm{v}}_{T},{\bm{v}}_{T}^{(i)})\mid\mathcal{E}_{(i)}]. (22)

[377] p: We recall the result derived by Lei and Ying (2020) , as in Proposition 4 . Notably, its derivation relies solely on the properties of the individual loss rather than the empirical loss. Consequently, under the assumption of β \beta -smooth, the following inequality holds:

[378] table: | ℓ ⁡ ( 𝒗 T , z ) − ℓ ⁡ ( 𝒗 T ( i ) , z ) | ≤ β ζ ​ ℓ ​ ( 𝒗 T , z ) + β + ζ 2 ​ ‖ 𝒗 T − 𝒗 T ( i ) ‖ 2 . |\ell({\bm{v}}_{T};z)-\ell({\bm{v}}_{T}^{(i)};z)|\leq\frac{\beta}{\zeta}\ell({\bm{v}}_{T};z)+\frac{\beta+\zeta}{2}\|{\bm{v}}_{T}-{\bm{v}}_{T}^{(i)}\|^{2}. (23)

[379] p: where ζ > 0 \zeta>0 is a free parameter. Conditioning ( 23 ) on the event ℰ ( i ) \mathcal{E}_{(i)} and taking the expectation over the randomness of the algorithm and datasets on both sides, we obtain:

[380] table: E ⁡ [ δ ⁡ ( 𝐯 T , 𝐯 T ( i ) ) ∣ ℰ ( i ) ] ≤ β ζ ​ E ​ [ ℓ ⁡ ( 𝐯 T , z i ) ∣ ℰ ( i ) ] + β + ζ 2 ​ E ​ [ ‖ 𝐯 T − 𝐯 T ( i ) ‖ 2 ∣ ℰ ( i ) ] . \mathbb{E}[\delta({\bm{v}}_{T},{\bm{v}}_{T}^{(i)})\mid\mathcal{E}_{(i)}]\leq\frac{\beta}{\zeta}\mathbb{E}[\ell({\bm{v}}_{T};z_{i})\mid\mathcal{E}_{(i)}]+\frac{\beta+\zeta}{2}\mathbb{E}[\|{\bm{v}}_{T}-{\bm{v}}_{T}^{(i)}\|^{2}\mid\mathcal{E}_{(i)}].

[381] p: The first term E ⁡ [ ℓ ⁡ ( 𝐯 T , z i ) ∣ ℰ ( i ) ] \mathbb{E}[\ell({\bm{v}}_{T};z_{i})\mid\mathcal{E}_{(i)}] is uniformly bounded by σ ¯ 2 \bar{\sigma}^{2} under Assumption 1 , while the second term corresponds exactly to the definition of the conditional on-average stability. Substituting this back into ( 22 ) yields:

[382] table: E ⁡ [ δ ⁡ ( 𝐯 T , 𝐯 T ( i ) ) ] ≤ t 0 n ​ σ ¯ 2 + β ζ ​ σ ¯ 2 + β + ζ 2 ​ E ​ [ ‖ 𝐯 T − 𝐯 T ( i ) ‖ 2 ∣ ℰ ( i ) ] . \mathbb{E}[\delta({\bm{v}}_{T},{\bm{v}}_{T}^{(i)})]\leq\frac{t_{0}}{n}\bar{\sigma}^{2}+\frac{\beta}{\zeta}\bar{\sigma}^{2}+\frac{\beta+\zeta}{2}\mathbb{E}[\|{\bm{v}}_{T}-{\bm{v}}_{T}^{(i)}\|^{2}\mid\mathcal{E}_{(i)}].

[383] p: Finally, by setting a uniform t 0 t_{0} for all indices i i and averaging the individual bounds over i = 1 , … , n i=1,\dots,n , the generalization gap satisfies:

[384] table: E 𝒜 , 𝒟 ​ [ ℒ s ​ ( 𝐰 T ) − ℒ ^ s ​ ( 𝐰 T ) ] ≤ 1 n ​ ∑ i = 1 n [ ( t 0 n + β ζ ) ​ σ ¯ 2 + β + ζ 2 ​ E 𝒜 , 𝒟 ​ [ ‖ 𝐯 T − 𝐯 T ( i ) ‖ 2 ∣ ℰ ( i ) ] ] = ( t 0 n + β ζ ) ​ σ ¯ 2 + β + ζ 2 ​ 1 n ​ ∑ i = 1 n E 𝒜 , 𝒟 ​ [ ‖ 𝐯 T − 𝐯 T ( i ) ‖ 2 ∣ ℰ ( i ) ] ⏟ ϵ avg , T | t 0 2 . \begin{split}\mathbb{E}_{\mathcal{A},\mathcal{D}}[\mathcal{L}^{s}({\bm{w}}_{T})-\hat{\mathcal{L}}^{s}({\bm{w}}_{T})]&\leq\frac{1}{n}\sum_{i=1}^{n}\left[\left(\frac{t_{0}}{n}+\frac{\beta}{\zeta}\right)\bar{\sigma}^{2}+\frac{\beta+\zeta}{2}\mathbb{E}_{\mathcal{A},\mathcal{D}}[\|{\bm{v}}_{T}-{\bm{v}}_{T}^{(i)}\|^{2}\mid\mathcal{E}_{(i)}]\right]\\ &=\left(\frac{t_{0}}{n}+\frac{\beta}{\zeta}\right)\bar{\sigma}^{2}+\frac{\beta+\zeta}{2}\underbrace{\frac{1}{n}\sum_{i=1}^{n}\mathbb{E}_{\mathcal{A},\mathcal{D}}[\|{\bm{v}}_{T}-{\bm{v}}_{T}^{(i)}\|^{2}\mid\mathcal{E}_{(i)}]}_{\epsilon^{2}_{\text{avg},T\mid t_{0}}}.\end{split}

[385] p: This concludes the proof. ∎

[386] h4: B.7.2 Proof of Theorem 4

[387] p: We begin by establishing a recursive bound for stability in the following lemma.

[388] h6: Lemma 13 .

[389] p: Suppose the assumptions of Theorem 4 hold. Using the effective stepsize η ~ t \tilde{\eta}_{t} defined in Lemma 4 , for any iteration t > t 0 t>t_{0} , the following recurrence holds:

[390] table: E I ​ ‖ 𝐯 t + 1 − 𝐯 t + 1 ( i ) ‖ 2 ≤ exp ⁡ ( m 1 ′ t + 2 + 1 T ) ​ ‖ 𝐯 t − 𝐯 t ( i ) ‖ 2 + m 2 ′ ​ ( 1 + T n ) ​ 1 n ​ 1 ( t + 2 ) 2 , \mathbb{E}_{I}\|{\bm{v}}_{t+1}-{\bm{v}}_{t+1}^{(i)}\|^{2}\leq\exp\left(\frac{m^{\prime}_{1}}{t+2}+\frac{1}{T}\right)\|{\bm{v}}_{t}-{\bm{v}}_{t}^{(i)}\|^{2}+m^{\prime}_{2}\left(1+\frac{T}{n}\right)\frac{1}{n}\frac{1}{(t+2)^{2}},

[391] p: where m 1 ′ = 8 ​ c 2 ​ σ ¯ 2 σ ¯ 2 + 4 ​ c 2 ​ β H ​ σ ¯ 2 m^{\prime}_{1}=8\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}+\frac{4c_{2}\beta}{H\underline{\sigma}^{2}} and m 2 ′ = 32 ​ e ​ c 2 2 ​ β ​ σ ¯ 2 n ​ H 2 ​ σ ¯ 4 m^{\prime}_{2}=\frac{32ec_{2}^{2}\beta\bar{\sigma}^{2}}{nH^{2}\underline{\sigma}^{4}} .

[392] h6: Proof.

[393] p: We analyze the update at step t > t 0 t>t_{0} . Let i t i_{t} denote the sample index selected by SGD at step t t .

[394] p: With probability 1 − 1 / n 1-1/n , the algorithm selects an index i t ≠ i i_{t}\neq i (i.e., the identical sample is used). By the β \beta -smoothness of the loss function, the update satisfies:

[395] table: ‖ 𝒗 ¯ t + 1 − 𝒗 ¯ t + 1 ( i ) ‖ 2 \displaystyle\|\bar{{\bm{v}}}_{t+1}-\bar{{\bm{v}}}_{t+1}^{(i)}\|^{2} = ∥ ( 𝒗 t − 𝒗 t ( i ) ) − η ~ t [ ∇ 𝒗 t ℓ t ( 𝒗 t ) ) − ∇ 𝒗 t ( i ) ℓ t ( 𝒗 t ( i ) ) ] ∥ 2 \displaystyle=\|({\bm{v}}_{t}-{\bm{v}}_{t}^{(i)})-\tilde{\eta}_{t}[\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t}))-\nabla_{{\bm{v}}_{t}^{(i)}}\ell_{t}({\bm{v}}_{t}^{(i)})]\|^{2} (24) ≤ [ ∥ 𝒗 t − 𝒗 t ( i ) ∥ + η ~ t ∥ ∇ 𝒗 t ℓ t ( 𝒗 t ) ) − ∇ 𝒗 t ( i ) ℓ t ( 𝒗 t ( i ) ) ∥ ] 2 \displaystyle\leq[\|{\bm{v}}_{t}-{\bm{v}}_{t}^{(i)}\|+\tilde{\eta}_{t}\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t}))-\nabla_{{\bm{v}}_{t}^{(i)}}\ell_{t}({\bm{v}}_{t}^{(i)})\|]^{2} ≤ ( 1 + β ​ η ~ t ) 2 ​ ‖ 𝒗 t − 𝒗 t ( i ) ‖ 2 . \displaystyle\leq(1+\beta\tilde{\eta}_{t})^{2}\|{\bm{v}}_{t}-{\bm{v}}_{t}^{(i)}\|^{2}.

[396] p: With probability 1 / n 1/n , the algorithm selects the index i t = i i_{t}=i (i.e, the samples differ). Using the inequality ‖ a + b ‖ 2 ≤ ( 1 + p ) ​ ‖ a ‖ 2 + ( 1 + 1 / p ) ​ ‖ b ‖ 2 \|a+b\|^{2}\leq(1+p)\|a\|^{2}+(1+1/p)\|b\|^{2} with p > 0 p>0 , the self-bounding property ‖ ∇ ℓ ​ ( 𝒗 ) ‖ 2 ≤ 2 ​ β ​ ℓ ​ ( 𝒗 ) \|\nabla\ell({\bm{v}})\|^{2}\leq 2\beta\ell({\bm{v}}) , and the Bounded Loss assumption, we have

[397] table: ‖ 𝒗 ¯ t + 1 − 𝒗 ¯ t + 1 ( i ) ‖ \displaystyle\|\bar{{\bm{v}}}_{t+1}-\bar{{\bm{v}}}_{t+1}^{(i)}\| = ∥ ( 𝒗 t − 𝒗 t ( i ) ) − η ~ t [ ∇ 𝒗 t ℓ t ( 𝒗 t ) ) − ∇ 𝒗 t ( i ) ℓ t ( 𝒗 t ( i ) ) ] ∥ 2 \displaystyle=\|({\bm{v}}_{t}-{\bm{v}}_{t}^{(i)})-\tilde{\eta}_{t}[\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t}))-\nabla_{{\bm{v}}_{t}^{(i)}}\ell_{t}({\bm{v}}_{t}^{(i)})]\|^{2} (25) ≤ ( 1 + p ) ​ ‖ 𝒗 t − 𝒗 t ( i ) ‖ 2 + η ~ t 2 ​ ( 1 + 1 / p ) ​ ‖ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) − ∇ 𝒗 t ( i ) ℓ t ​ ( 𝒗 t ( i ) ) ‖ 2 \displaystyle\leq(1+p)\|{\bm{v}}_{t}-{\bm{v}}_{t}^{(i)}\|^{2}+\tilde{\eta}_{t}^{2}(1+1/p)\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})-\nabla_{{\bm{v}}_{t}^{(i)}}\ell_{t}({\bm{v}}_{t}^{(i)})\|^{2} ≤ ( 1 + p ) ​ ‖ 𝒗 t − 𝒗 t ( i ) ‖ 2 + 2 ​ η ~ t 2 ​ ( 1 + 1 / p ) ​ [ ‖ ∇ 𝒗 t ℓ t ​ ( 𝒗 t ) ‖ 2 + ‖ ∇ 𝒗 t ( i ) ℓ t ​ ( 𝒗 t ( i ) ) ‖ 2 ] \displaystyle\leq(1+p)\|{\bm{v}}_{t}-{\bm{v}}_{t}^{(i)}\|^{2}+2\tilde{\eta}_{t}^{2}(1+1/p)[\|\nabla_{{\bm{v}}_{t}}\ell_{t}({\bm{v}}_{t})\|^{2}+\|\nabla_{{\bm{v}}_{t}^{(i)}}\ell_{t}({\bm{v}}_{t}^{(i)})\|^{2}] ≤ ( 1 + p ) ​ ‖ 𝒗 t − 𝒗 t ( i ) ‖ 2 + 4 ​ β ​ ( 1 + 1 / p ) ​ η ~ t 2 ​ [ ℓ ⁡ ( 𝒗 t , z i ) + ℓ ⁡ ( 𝒗 t ( i ) , z i ′ ) ] \displaystyle\leq(1+p)\|{\bm{v}}_{t}-{\bm{v}}_{t}^{(i)}\|^{2}+4\beta(1+1/p)\tilde{\eta}_{t}^{2}[\ell({\bm{v}}_{t};z_{i})+\ell({\bm{v}}_{t}^{(i)};z_{i}^{\prime})] ≤ ( 1 + p ) ​ ‖ 𝒗 t − 𝒗 t ( i ) ‖ 2 + 8 ​ β ​ ( 1 + 1 / p ) ​ η ~ t 2 ​ σ ¯ 2 . \displaystyle\leq(1+p)\|{\bm{v}}_{t}-{\bm{v}}_{t}^{(i)}\|^{2}+8\beta(1+1/p)\tilde{\eta}_{t}^{2}\bar{\sigma}^{2}.

[398] p: Taking the expectation over the choice of i t i_{t} , we combine ( 24 ) and ( 25 ):

[399] table: E I ​ ‖ 𝐯 ¯ t + 1 − 𝐯 ¯ t + 1 ( i ) ‖ 2 ≤ [ ( 1 − 1 n ) ​ ( 1 + β ​ η ~ t ) 2 + 1 n ​ ( 1 + p ) ] ​ ‖ 𝐯 t − 𝐯 t ( i ) ‖ 2 + 8 ​ β n ​ ( 1 + 1 p ) ​ η ~ t 2 ​ σ ¯ 2 . \mathbb{E}_{I}\|\bar{{\bm{v}}}_{t+1}-\bar{{\bm{v}}}_{t+1}^{(i)}\|^{2}\leq\left[\left(1-\frac{1}{n}\right)(1+\beta\tilde{\eta}_{t})^{2}+\frac{1}{n}(1+p)\right]\|{{\bm{v}}}_{t}-{{\bm{v}}}_{t}^{(i)}\|^{2}+\frac{8\beta}{n}\left(1+\frac{1}{p}\right)\tilde{\eta}_{t}^{2}\bar{\sigma}^{2}. (26)

[400] p: Utilizing the norm ratio bound in ( 10 ), we have

[401] table: E I ​ ‖ 𝐯 t + 1 − 𝐯 t + 1 ( i ) ‖ 2 ≤ ( 1 + 4 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 ) 2 ​ E I ​ ‖ 𝐯 ¯ t + 1 − 𝐯 ¯ t + 1 ( i ) ‖ 2 . \mathbb{E}_{I}\|{\bm{v}}_{t+1}-{\bm{v}}_{t+1}^{(i)}\|^{2}\leq(1+4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2})^{2}\mathbb{E}_{I}\|\bar{{\bm{v}}}_{t+1}-\bar{{\bm{v}}}_{t+1}^{(i)}\|^{2}. (27)

[402] p: Setting p = n / T p=n/T and substituting ( 26 ) into ( 27 ), we obtain:

[403] table: E I ​ ‖ 𝐯 t + 1 − 𝐯 t + 1 ( i ) ‖ 2 \displaystyle{\mathbb\displaystyle E}_{I}\|{\bm{v}}_{t+1}-{\bm{v}}_{t+1}^{(i)}\|^{2} (28) ≤ ( 1 + 4 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 ) 2 ​ { [ ( 1 − 1 n ) ​ ( 1 + β ​ η ~ t ) 2 + 1 n ​ ( 1 + p ) ] ​ ‖ 𝒗 t − 𝒗 t ( i ) ‖ 2 + 8 ​ β n ​ ( 1 + 1 p ) ​ η ~ t 2 ​ σ ¯ 2 } \displaystyle\leq(1+4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2})^{2}\left\{\left[\left(1-\frac{1}{n}\right)(1+\beta\tilde{\eta}_{t})^{2}+\frac{1}{n}(1+p)\right]\|{{\bm{v}}}_{t}-{{\bm{v}}}_{t}^{(i)}\|^{2}+\frac{8\beta}{n}\left(1+\frac{1}{p}\right)\tilde{\eta}_{t}^{2}\bar{\sigma}^{2}\right\} = { ( 1 + 4 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 ) 2 ​ [ ( 1 − 1 n ) ​ ( 1 + β ​ η ~ t ) 2 + 1 n ​ ( 1 + n T ) ] } ​ ‖ 𝒗 t − 𝒗 t ( i ) ‖ 2 \displaystyle=\left\{\left(1+4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}\right)^{2}\left[\left(1-\frac{1}{n}\right)(1+\beta\tilde{\eta}_{t})^{2}+\frac{1}{n}\left(1+\frac{n}{T}\right)\right]\right\}\|{{\bm{v}}}_{t}-{{\bm{v}}}_{t}^{(i)}\|^{2} + ( 1 + 4 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 ) 2 ​ 8 ​ β n ​ ( 1 + 1 p ) ​ η ~ t 2 ​ σ ¯ 2 . \displaystyle+\left(1+4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}\right)^{2}\frac{8\beta}{n}\left(1+\frac{1}{p}\right)\tilde{\eta}_{t}^{2}\bar{\sigma}^{2}.

[404] p: For the first term in ( 28 ), we have:

[405] table: ( 1 + 4 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 ) 2 ​ [ ( 1 − 1 n ) ​ ( 1 + β ​ η ~ t ) 2 + 1 n ​ ( 1 + n T ) ] \displaystyle\quad\left(1+4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}\right)^{2}\left[\left(1-\frac{1}{n}\right)(1+\beta\tilde{\eta}_{t})^{2}+\frac{1}{n}\left(1+\frac{n}{T}\right)\right] ≤ ( 1 + 4 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 ) 2 ​ [ ( 1 + β ​ η ~ t ) 2 + 1 T ] \displaystyle\leq\left(1+4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}\right)^{2}\left[(1+\beta\tilde{\eta}_{t})^{2}+\frac{1}{T}\right] ≤ ( 1 + 4 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 ) 2 ​ ( 1 + β ​ η ~ t ) 2 ​ ( 1 + 1 T ) \displaystyle\leq\left(1+4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}\right)^{2}(1+\beta\tilde{\eta}_{t})^{2}\left(1+\frac{1}{T}\right) ≤ exp ⁡ ( 8 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 ) ​ exp ⁡ ( 2 ​ β ​ η ~ t ) ​ exp ⁡ ( 1 T ) \displaystyle\leq\exp\left(8\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}\right)\exp(2\beta\tilde{\eta}_{t})\exp\left(\frac{1}{T}\right) = exp ⁡ ( 1 T + 8 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 + 2 ​ β ​ 2 ​ c 2 H ​ σ ¯ 2 ​ ( t + 2 ) ) \displaystyle=\exp\left(\frac{1}{T}+8\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}+2\beta\frac{2c_{2}}{H\underline{\sigma}^{2}(t+2)}\right) = exp ⁡ ( 1 T + [ 8 ​ c 2 ​ σ ¯ 2 σ ¯ 2 + 4 ​ c 2 ​ β H ​ σ ¯ 2 ] ​ 1 t + 2 ) = exp ⁡ ( 1 T + m 1 ′ t + 2 ) . \displaystyle=\exp\left(\frac{1}{T}+\left[8\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}+\frac{4c_{2}\beta}{H\underline{\sigma}^{2}}\right]\frac{1}{t+2}\right)=\exp\left(\frac{1}{T}+\frac{m^{\prime}_{1}}{t+2}\right).

[406] p: For the second term in ( 28 ), we have:

[407] table: ( 1 + 4 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 ) 2 ​ 8 ​ β n ​ ( 1 + 1 p ) ​ η ~ t 2 ​ σ ¯ 2 \displaystyle\quad\left(1+4\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}\right)^{2}\frac{8\beta}{n}\left(1+\frac{1}{p}\right)\tilde{\eta}_{t}^{2}\bar{\sigma}^{2} ≤ exp ⁡ ( 8 ​ c 2 ​ σ ¯ 2 σ ¯ 2 ​ 1 t + 2 ) ​ 8 ​ β n ​ ( 1 + T n ) ​ ( 2 ​ c 2 H ​ σ ¯ 2 ​ ( t + 2 ) ) 2 ​ σ ¯ 2 \displaystyle\leq\exp\left(8\frac{c_{2}\bar{\sigma}^{2}}{\underline{\sigma}^{2}}\frac{1}{t+2}\right)\frac{8\beta}{n}\left(1+\frac{T}{n}\right)\left(\frac{2c_{2}}{H\underline{\sigma}^{2}(t+2)}\right)^{2}\bar{\sigma}^{2} ≤ e ⋅ 8 ​ β n ​ ( 1 + T n ) ​ 4 ​ c 2 2 H 2 ​ σ ¯ 4 ​ ( t + 2 ) 2 ​ σ ¯ 2 \displaystyle\leq e\cdot\frac{8\beta}{n}\left(1+\frac{T}{n}\right)\frac{4c_{2}^{2}}{H^{2}\underline{\sigma}^{4}(t+2)^{2}}\bar{\sigma}^{2} = [ 32 ​ e ​ c 2 2 ​ β ​ σ ¯ 2 H 2 ​ σ ¯ 4 ] ​ ( 1 + T n ) ​ 1 ( t + 2 ) 2 ​ 1 n \displaystyle=\left[\frac{32ec_{2}^{2}\beta\bar{\sigma}^{2}}{H^{2}\underline{\sigma}^{4}}\right]\left(1+\frac{T}{n}\right)\frac{1}{(t+2)^{2}}\frac{1}{n} = m 2 ′ ​ ( 1 + T n ) ​ 1 n ​ 1 ( t + 2 ) 2 . \displaystyle=m^{\prime}_{2}\left(1+\frac{T}{n}\right)\frac{1}{n}\frac{1}{(t+2)^{2}}.

[408] p: Consequently, ( 28 ) is equivalent to

[409] table: E I ​ ‖ 𝐯 t + 1 − 𝐯 t + 1 ( i ) ‖ 2 ≤ exp ⁡ ( m 1 ′ t + 2 + 1 T ) ​ ‖ 𝐯 t − 𝐯 t ( i ) ‖ 2 + m 2 ′ ​ ( 1 + T n ) ​ 1 n ​ 1 ( t + 2 ) 2 . \mathbb{E}_{I}\|{\bm{v}}_{t+1}-{\bm{v}}_{t+1}^{(i)}\|^{2}\leq\exp\left(\frac{m^{\prime}_{1}}{t+2}+\frac{1}{T}\right)\|{\bm{v}}_{t}-{\bm{v}}_{t}^{(i)}\|^{2}+m^{\prime}_{2}\left(1+\frac{T}{n}\right)\frac{1}{n}\frac{1}{(t+2)^{2}}. (29)

[410] p: This completes the proof of Lemma 13 . ∎

[411] p: We then proceed to derive the generalization bound in Theorem 4 . We first bound the conditional on-average stability, and then optimize the resulting generalization gap.

[412] h6: Proof.

[413] p: Taking expectations of ( 29 ) over the randomness of the algorithm and datasets, conditioned on ℰ ( i ) \mathcal{E}_{(i)} , we obtain:

[414] table: E 𝒜 , 𝒟 ​ [ ‖ 𝐯 t + 1 − 𝐯 t + 1 ( i ) ‖ 2 ∣ ℰ ( i ) ] \displaystyle{\mathbb\displaystyle E}_{\mathcal{A},\mathcal{D}}[\|{\bm{v}}_{t+1}-{\bm{v}}_{t+1}^{(i)}\|^{2}\mid\mathcal{E}_{(i)}] ≤ \displaystyle\leq exp ⁡ ( m 1 ′ t + 2 + 1 T ) ​ E 𝒜 , 𝒟 ​ [ ‖ 𝐯 t − 𝐯 t ( i ) ‖ 2 ∣ ℰ ( i ) ] + m 2 ′ ​ ( 1 + T n ) ​ 1 n ​ 1 ( t + 2 ) 2 . \displaystyle\exp\left(\frac{m^{\prime}_{1}}{t+2}+\frac{1}{T}\right)\mathbb{E}_{\mathcal{A},\mathcal{D}}[\|{\bm{v}}_{t}-{\bm{v}}_{t}^{(i)}\|^{2}\mid\mathcal{E}_{(i)}]+m^{\prime}_{2}\left(1+\frac{T}{n}\right)\frac{1}{n}\frac{1}{(t+2)^{2}}.

[415] p: Averaging over all samples 1 , … , n 1,\dots,n , and defining Δ t ≜ 1 n ​ ∑ i = 1 n E 𝒜 , 𝒟 ​ [ ‖ 𝐯 t − 𝐯 t ( i ) ‖ 2 ∣ ℰ ( i ) ] \Delta_{t}\triangleq\frac{1}{n}\sum_{i=1}^{n}\mathbb{E}_{\mathcal{A},\mathcal{D}}[\|{\bm{v}}_{t}-{\bm{v}}_{t}^{(i)}\|^{2}\mid\mathcal{E}_{(i)}] , we have:

[416] table: Δ t + 1 ≤ exp ⁡ ( m 1 ′ t + 2 + 1 T ) ​ Δ t + m 2 ′ ​ ( 1 + T n ) ​ 1 n ​ 1 ( t + 2 ) 2 . \Delta_{t+1}\leq\exp\left(\frac{m^{\prime}_{1}}{t+2}+\frac{1}{T}\right)\Delta_{t}+m^{\prime}_{2}\left(1+\frac{T}{n}\right)\frac{1}{n}\frac{1}{(t+2)^{2}}.

[417] p: Let K n , T ≜ e m 1 ′ + 1 ​ ( 1 + T n ) ​ 1 n ​ m 2 ′ K_{n,T}\triangleq\frac{e}{m^{\prime}_{1}+1}(1+\frac{T}{n})\frac{1}{n}m^{\prime}_{2} , where e e is the base of the natural logarithm. Then:

[418] table: Δ t + 1 ≤ exp ⁡ ( m 1 ′ t + 2 + 1 T ) ​ Δ t + m 1 ′ + 1 e ​ K n , T ​ 1 ( t + 2 ) 2 . \Delta_{t+1}\leq\exp\left(\frac{m^{\prime}_{1}}{t+2}+\frac{1}{T}\right)\Delta_{t}+\frac{m^{\prime}_{1}+1}{e}K_{n,T}\frac{1}{(t+2)^{2}}.

[419] p: Unrolling the recurrence from t = t 0 t=t_{0} to T − 1 T-1 yields:

[420] table: Δ T ≤ m 1 ′ + 1 e ​ K n , T ​ ∑ t = t 0 T − 1 1 ( t + 2 ) 2 ​ ∏ k = t + 1 T − 1 exp ⁡ ( m 1 ′ k + 2 + 1 T ) = m 1 ′ + 1 e ​ K n , T ​ ∑ t = t 0 T − 1 1 ( t + 2 ) 2 ​ exp ​ ∑ k = t + 1 T − 1 ( m 1 ′ k + 2 + 1 T ) = m 1 ′ + 1 e ​ K n , T ​ ∑ t = t 0 T − 1 1 ( t + 2 ) 2 ​ exp ⁡ ( m 1 ′ ​ ∑ k = t + 1 T − 1 1 k + 2 + T − t − 1 T ) ≤ ( m 1 ′ + 1 ) ​ K n , T ​ ∑ t = t 0 T − 1 1 ( t + 2 ) 2 ​ exp ⁡ ( m 1 ′ ​ ∑ k = t + 1 T − 1 1 k + 2 ) . \begin{split}\Delta_{T}&\leq\frac{m^{\prime}_{1}+1}{e}K_{n,T}\sum_{t=t_{0}}^{T-1}\frac{1}{(t+2)^{2}}\prod_{k=t+1}^{T-1}\exp\left(\frac{m^{\prime}_{1}}{k+2}+\frac{1}{T}\right)\\ &=\frac{m^{\prime}_{1}+1}{e}K_{n,T}\sum_{t=t_{0}}^{T-1}\frac{1}{(t+2)^{2}}\exp\sum_{k=t+1}^{T-1}\left(\frac{m^{\prime}_{1}}{k+2}+\frac{1}{T}\right)\\ &=\frac{m^{\prime}_{1}+1}{e}K_{n,T}\sum_{t=t_{0}}^{T-1}\frac{1}{(t+2)^{2}}\exp\left(m^{\prime}_{1}\sum_{k=t+1}^{T-1}\frac{1}{k+2}+\frac{T-t-1}{T}\right)\\ &\leq(m^{\prime}_{1}+1)K_{n,T}\sum_{t=t_{0}}^{T-1}\frac{1}{(t+2)^{2}}\exp\left(m^{\prime}_{1}\sum_{k=t+1}^{T-1}\frac{1}{k+2}\right).\end{split}

[421] p: Using the inequality ∑ k = t + 1 T − 1 1 k + 2 ≤ ln ⁡ ( T t + 1 ) \sum_{k=t+1}^{T-1}\frac{1}{k+2}\leq\ln(\frac{T}{t+1}) and ∑ t = t 0 T − 1 ( t + 1 ) − ( 2 + m 1 ′ ) ≤ ∫ t 0 ∞ x − ( 2 + m 1 ′ ) ​ 𝑑 x = 1 1 + m 1 ′ ​ t 0 − ( m 1 ′ + 1 ) \sum_{t=t_{0}}^{T-1}(t+1)^{-(2+m^{\prime}_{1})}\leq\int_{t_{0}}^{\infty}x^{-(2+m^{\prime}_{1})}dx=\frac{1}{1+m^{\prime}_{1}}t_{0}^{-(m^{\prime}_{1}+1)} , we obtain:

[422] table: Δ T ≤ ( m 1 ′ + 1 ) ​ K n , T ​ T m 1 ′ ​ ∑ t = t 0 T − 1 ( t + 1 ) − ( 2 + m 1 ′ ) ≤ K n , T ​ T m 1 ′ ​ t 0 − ( m 1 ′ + 1 ) . \Delta_{T}\leq(m^{\prime}_{1}+1)K_{n,T}T^{m^{\prime}_{1}}\sum_{t=t_{0}}^{T-1}(t+1)^{-(2+m^{\prime}_{1})}\leq K_{n,T}T^{m^{\prime}_{1}}t_{0}^{-(m^{\prime}_{1}+1)}. (30)

[423] p: Substituting ( 30 ) into ( B.7.1 ) gives

[424] table: E 𝒜 , 𝒟 ​ [ ℒ s ​ ( 𝐰 T ) − ℒ ^ s ​ ( 𝐰 T ) ] ≤ ( t 0 n + β ζ ) ​ σ ¯ 2 + β + ζ 2 ​ Δ T ≤ ( t 0 n + β ζ ) ​ σ ¯ 2 + β + ζ 2 ​ K n , T ​ T m 1 ′ ​ t 0 − ( m 1 ′ + 1 ) = K n , T ​ T m 1 ′ 2 ​ ( ζ + β ) ⋅ t 0 − ( m 1 ′ + 1 ) + β ​ σ ¯ 2 ​ 1 ζ + σ ¯ 2 n ​ t 0 . \begin{split}\mathbb{E}_{\mathcal{A},\mathcal{D}}[\mathcal{L}^{s}({\bm{w}}_{T})-\hat{\mathcal{L}}^{s}({\bm{w}}_{T})]&\leq\left(\frac{t_{0}}{n}+\frac{\beta}{\zeta}\right)\bar{\sigma}^{2}+\frac{\beta+\zeta}{2}\Delta_{T}\\ &\leq\left(\frac{t_{0}}{n}+\frac{\beta}{\zeta}\right)\bar{\sigma}^{2}+\frac{\beta+\zeta}{2}K_{n,T}T^{m^{\prime}_{1}}t_{0}^{-(m^{\prime}_{1}+1)}\\ &=\frac{K_{n,T}T^{m^{\prime}_{1}}}{2}(\zeta+\beta)\cdot t_{0}^{-(m^{\prime}_{1}+1)}+\beta\bar{\sigma}^{2}\frac{1}{\zeta}+\frac{\bar{\sigma}^{2}}{n}t_{0}.\end{split}

[425] p: Define g ⁡ ( ζ , t 0 ) ≜ K n , T ​ T m 1 ′ 2 ​ ( ζ + β ) ⋅ t 0 − ( m 1 ′ + 1 ) + β ​ σ ¯ 2 ​ 1 ζ + σ ¯ 2 n ​ t 0 g(\zeta,t_{0})\triangleq\frac{K_{n,T}T^{m^{\prime}_{1}}}{2}(\zeta+\beta)\cdot t_{0}^{-(m^{\prime}_{1}+1)}+\beta\bar{\sigma}^{2}\frac{1}{\zeta}+\frac{\bar{\sigma}^{2}}{n}t_{0} . Observing that the generalization gap is independent of ζ \zeta and t 0 t_{0} , we minimize g g to obtain:

[426] table: E 𝒜 , 𝒟 ​ [ ℒ s ​ ( 𝐰 T ) − ℒ ^ s ​ ( 𝐰 T ) ] ≤ min t 0 , ζ ⁡ g ⁡ ( t 0 , ζ ) = ( m 1 ′ + 3 ) / ( m 1 ′ + 1 ) m 1 ′ + 2 m 1 ′ + 3 ⋅ ( β ​ e ​ m 2 ′ / 2 ) 1 m 1 ′ + 3 ​ σ ¯ 2 ​ m 1 ′ + 4 m 1 ′ + 3 ⋅ n − m 1 ′ + 2 m 1 ′ + 3 ​ ( 1 + T n ) 1 m 1 ′ + 3 ​ T m 1 ′ m 1 ′ + 3 = 𝒪 ⁡ ( n − m 1 ′ + 2 m 1 ′ + 3 ​ ( 1 + T n ) 1 m 1 ′ + 3 ​ T m 1 ′ m 1 ′ + 3 ) . \begin{split}&\mathbb{E}_{\mathcal{A},\mathcal{D}}[\mathcal{L}^{s}({\bm{w}}_{T})-\hat{\mathcal{L}}^{s}({\bm{w}}_{T})]\\ \leq&\min_{t_{0},\zeta}g(t_{0},\zeta)\\ =&(m^{\prime}_{1}+3)/(m^{\prime}_{1}+1)^{\frac{m^{\prime}_{1}+2}{m^{\prime}_{1}+3}}\cdot\left(\beta em^{\prime}_{2}/2\right)^{\frac{1}{m^{\prime}_{1}+3}}\bar{\sigma}^{\frac{2m^{\prime}_{1}+4}{m^{\prime}_{1}+3}}\cdot n^{-\frac{m^{\prime}_{1}+2}{m^{\prime}_{1}+3}}\left(1+\frac{T}{n}\right)^{\frac{1}{m^{\prime}_{1}+3}}T^{\frac{m^{\prime}_{1}}{m^{\prime}_{1}+3}}\\ =&\mathcal{O}(n^{-\frac{m^{\prime}_{1}+2}{m^{\prime}_{1}+3}}\left(1+\frac{T}{n}\right)^{\frac{1}{m^{\prime}_{1}+3}}T^{\frac{m^{\prime}_{1}}{m^{\prime}_{1}+3}}).\end{split}

[427] p: This concludes the proof of Theorem 4 . ∎

[428] h3: B.8 Review of Several Stability Metrics

[429] h4: B.8.1 Review of Algorithmic Stability

[430] p: Algorithmic stability is a popular technique in generalization theory, offering the following favorable properties:

[431] h6: Proposition 3 .

[432] p: (Algorithmic stability and generalization) The arguments are based on Bousquet and Elisseeff (2002) ; Shalev-Shwartz et al. (2010) ; Hardt et al. (2016) . Assume that the algorithm is ϵ T \epsilon_{T} -stable, meaning that for all datasets S S and S ′ S^{\prime} differing in at most one sample, it holds that

[433] table: sup ( X , Y ) E 𝒜 , 𝒟 ​ [ ℓ ⁡ ( 𝐰 T , X , Y ) − ℓ ⁡ ( 𝐰 T ′ , X , Y ) ] ≤ ϵ T , \sup_{({X},{Y})}\mathbb{E}_{\mathcal{A},\mathcal{D}}[\ell({\bm{w}}_{T};{X},{Y})-\ell({\bm{w}}_{T}^{\prime};{X},{Y})]\leq\epsilon_{T},

[434] p: where 𝐰 T {\bm{w}}_{T} and 𝐰 T ′ {\bm{w}}_{T}^{\prime} are trained on datasets S S and S ′ S^{\prime} over T T iterations, respectively, and the expectation is taken over both the training set randomness and the algorithmic randomness. Then the generalization gap can be bounded via algorithmic stability:

[435] table: E 𝒜 , 𝒟 ​ ℒ ​ ( 𝐰 T ) − ℒ ^ ​ ( 𝐰 T ) ≤ ϵ T . \mathbb{E}_{\mathcal{A},\mathcal{D}}\mathcal{L}({\bm{w}}_{T})-\hat{\mathcal{L}}({\bm{w}}_{T})\leq\epsilon_{T}.

[436] p: Furthermore, it holds that for SGD with replacement using stepsize η t \eta_{t} for each iteration t t :

[437] p: For convex loss functions, provided they are L L -Lipschitz and β \beta -smooth, and the stepsize satisfies η T ≤ 2 / β \eta_{T}\leq 2/\beta , it holds that ϵ T ≤ 2 ​ L 2 n ​ ∑ t = 1 T η t \epsilon_{T}\leq\frac{2L^{2}}{n}\sum_{t=1}^{T}\eta_{t} .

[438] p: For non-convex loss functions, provided they are L L -Lipschitz and β \beta -smooth, and the stepsize is non-increasing with η t ≤ c / t \eta_{t}\leq c/t for a given constant c c , it holds that ϵ T ≤ 1 + 1 / β ​ c n − 1 ​ ( 2 ​ c ​ L 2 ) 1 β ​ c + 1 ​ T β ​ c β ​ c + 1 \epsilon_{T}\leq\frac{1+1/\beta c}{n-1}(2cL^{2})^{\frac{1}{\beta c+1}}T^{\frac{\beta c}{\beta c+1}} .

[439] h4: B.8.2 Review of On-Average Model Stability

[440] p: In this section, we provide the necessary background on the on-average model stability introduced by Lei and Ying (2020) . Unlike uniform stability, which requires an upper bound on the loss difference for any pair of sample in the distribution, on-average model stability measures the average distance of weights trained via the same algorithm on two datasets differing at most one sample.

[441] h6: Definition 3 ( ℓ 2 \ell_{2} On-Average Model Stability) .

[442] p: Let S = { z 1 , … , z n } S=\{z_{1},\dots,z_{n}\} and S ( i ) = { z 1 , … , z i ′ , … , z n } S^{(i)}=\{z_{1},\dots,z_{i}^{\prime},\dots,\allowbreak z_{n}\} be two datasets differing only in the i i -th sample. A randomized algorithm 𝒜 \mathcal{A} is ϵ avg \epsilon_{\text{avg}} -stable in ℓ 2 \ell_{2} on-average if:

[443] table: E S , S ~ , 𝒜 ​ [ 1 n ​ ∑ i = 1 n ‖ 𝒜 ⁡ ( S ) − 𝒜 ⁡ ( S ( i ) ) ‖ 2 2 ] ≤ ϵ avg 2 . \mathbb{E}_{S,\tilde{S},\mathcal{A}}\left[\frac{1}{n}\sum_{i=1}^{n}\|\mathcal{A}(S)-\mathcal{A}(S^{(i)})\|_{2}^{2}\right]\leq\epsilon_{\text{avg}}^{2}.

[444] p: Based on this definition, the generalization gap can be bounded as follows:

[445] h6: Proposition 4 (Generalization via Model Stability) .

[446] p: If for any z z , the loss ℓ ⁡ ( 𝐰 , z ) \ell({\bm{w}};z) is non-negative and β \beta -smooth, then for any free parameter ζ > 0 \zeta>0 :

[447] table: E 𝒜 , 𝒟 ​ [ ℒ ⁡ ( 𝐰 T ) − ℒ ^ ​ ( 𝐰 T ) ] ≤ β ζ ​ E 𝒜 , 𝒟 ​ [ ℒ ^ ​ ( 𝐰 T ) ] + β + ζ 2 ​ ϵ avg 2 , \mathbb{E}_{\mathcal{A},\mathcal{D}}[\mathcal{L}({\bm{w}}_{T})-\hat{\mathcal{L}}({\bm{w}}_{T})]\leq\frac{\beta}{\zeta}\mathbb{E}_{\mathcal{A},\mathcal{D}}[\hat{\mathcal{L}}({\bm{w}}_{T})]+\frac{\beta+\zeta}{2}\epsilon_{\text{avg}}^{2},

[448] p: where ϵ avg 2 \epsilon_{\text{avg}}^{2} denotes the on-average model stability of the algorithm’s output 𝐰 T {\bm{w}}_{T} .

[449] h2: Instructions for reporting errors

[450] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[451] p: Tip: You can select the relevant text first, to include it in your report.

[452] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[453] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
