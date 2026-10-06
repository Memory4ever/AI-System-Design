[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Differentiable Zero-One Loss via Hypersimplex Projections

[3] h6: Abstract

[4] p: Recent advances in machine learning have emphasized the integration of structured optimization components into end-to-end differentiable models, enabling richer inductive biases and tighter alignment with task-specific objectives. In this work, we introduce a novel differentiable approximation to the zero–one loss—long considered the gold standard for classification performance, yet incompatible with gradient-based optimization due to its non-differentiability. Our method constructs a smooth, order-preserving projection onto the ( n , k ) (n,k) -dimensional hypersimplex through a constrained optimization framework, leading to a new operator we term Soft-Binary-Argmax. After deriving its mathematical properties, we show how its Jacobian can be efficiently computed and integrated into binary and multiclass learning systems. Empirically, our approach achieves significant improvements in generalization under large-batch training by imposing geometric consistency constraints on the output logits, thereby narrowing the performance gap traditionally observed in large-batch training. Our code is available here https://github.com/camilog04/Differentiable-Zero-One-Loss-via-Hypersimplex-Projections .

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] p: Recent developments in machine learning have demonstrated that optimization procedures can be used as fundamental components within end-to-end differentiable systems [ 1 , 6 , 11 , 9 ] . Rather than relying solely on traditional neural network layers, these approaches incorporate more structured, often nontrivial computations—such as constrained optimization—directly into the learning pipeline. These components usually have structural or computational properties that have been proven useful in downstream tasks. For instance, Sparsemax, a differentiable projection onto the simplex, produces sparse posterior distributions that are effective as attention mechanisms [ 17 ] . Similarly, Csoftmax, a projection onto the budget polytope, has demonstrated utility in sequence tagging [ 18 ] . This reflects a growing shift toward viewing learning systems as differentiable computational frameworks that blend elements of traditional statistical modeling with algorithmic computation [ 5 ] . In this paper, we focus on crafting a differentiable, order-preserving projection into the n , k n,k -dimensional hypersimplex [ 7 ] –a well-studied combinatorics polytope–in composition with a squared loss to generate a close approximation to the zero-one, misclassification loss compatible with modern large-scale differentiable systems.

[8] p: From a theoretical perspective in machine learning, the goal is to minimize the expected value of a task-specific loss function over a data distribution. For classification, the most natural choice is the zero-one loss, which directly measures misclassification error. However, zero-one loss is non-differentiable and discontinuous, as it depends on a hard threshold decision—yielding gradients of zero almost everywhere and rendering it incompatible with gradient-based optimization. To enable tractable training, modern approaches rely on surrogate losses (e.g., cross-entropy, hinge loss) that are smooth and differentiable [ 3 ] . These surrogates serve as proxies that approximate the zero-one loss while facilitating efficient optimization. Despite their practicality, such surrogates often exhibit a mismatch with the true evaluation metric, especially under large-batch regimes. This degradation in performance with large batch sizes is the so-called generalization gap [ 19 ] , leading to growing interest in tighter, more faithful approximations to the zero-one loss, under the hypothesis that closer surrogates yield better generalization.

[9] p: This work introduces a fully differentiable approximation to the zero–one loss, featuring an efficient forward pass with complexity 𝒪 ⁡ ( n ​ log ⁡ n ) \mathcal{O}(n\log n) and a backward pass with 𝒪 ⁡ ( n ) \mathcal{O}(n) complexity. This is achieved through our novel differentiable projection layer, Soft-Binary-Argmax@k . Rather than treating the output scores as independent, our layer explicitly enforces that the largest k k logits correspond to the predicted positive classes. This design ensures that small perturbations in the input produce coherent, structurally consistent adjustments in the output, making the Jacobian of the transformation inherently positionally aware with respect to the most confident predictions. The benefits of this approach are twofold: it allows binary classifiers to express multiple positive outcomes within a single forward pass, and it extends naturally to the multiclass setting by applying the same projection principle across one-hot encoded class dimensions. Importantly, the geometric constraints imposed on the output logits act as a form of regularization that mitigates the generalization degradation typically observed under large-batch training, enabling stable optimization and improved predictive performance.

[10] p: More precisely, our contributions and novelty can be summarized as follows:

[11] p: We introduce a differentiable projection layer—a smooth thresholding operator realized via projection onto the interior of the n , k n,k -dimensional hypersimplex—termed Soft-Binary-Argmax@k . It provides a differentiable relaxation of the binary argmax , reduces to isotonic regression, and enables efficient forward and backward computation on both CPU and GPU.

[12] p: We propose a smooth, almost-everywhere differentiable loss function for binary classification, the HyperSimplex Loss , and derive its mathematical properties. The loss couples the mean squared error with our projection layer and extends naturally to multiclass.

[13] p: Through rigorous experimentation, we provide empirical evidence that the proposed loss mitigates the generalization gap and improves performance across multiple classification benchmark datasets.

[14] h2: 2 Related work

[15] h3: 2.1 Differentiable optimization-based ML

[16] p: Optimization-based modeling integrates structure and constraints into machine learning architectures by embedding parameterized argmin / argmax operations as differentiable layers. Such layers are often formulated as convex, constrained programs, with differentiability achieved via the implicit function theorem applied to the KKT conditions [ 11 ] . Parallel work has explored differentiable optimization for order-constrained or monotonic outputs, including differentiable isotonic regression operators for smooth, order-aware learning [ 6 ] . To the best of our knowledge, no prior work has introduced a differentiable Euclidean projection onto the ( n , k ) (n,k) -dimensional hypersimplex—computed via the Pool Adjacent Violators (PAV) algorithm—as a learnable layer. Our approach fills this gap, providing an efficient and theoretically grounded formulation for integrating hypersimplex projections into modern differentiable systems.

[17] h3: 2.2 Generalization gap

[18] p: A well-known challenge in modern deep learning is the generalization gap , where models trained with large batch sizes achieve low training loss but exhibit degraded test performance. This phenomenon has been widely observed in neural networks, as large batches tend to converge to sharp minima that generalize poorly compared to the flatter solutions found by small-batch training [ 15 ] . Subsequent work has explored remedies such as adaptive learning rate schedules and warmup strategies, noise injection and regularization [ 12 ] , and stochastic weight averaging [ 14 ] to mitigate this effect. However, to the best of our knowledge, our work is the first to address the generalization gap through loss function design , introducing a principled framework that directly links the geometry of the loss landscape to generalization behavior.

[19] h2: 3 Preliminaries

[20] p: In supervised multiclass classification, we are given a dataset 𝒟 = { ( x i , y i ) } i = 1 n \mathcal{D}=\{(x_{i},y_{i})\}_{i=1}^{n} , where each input x i ∈ 𝒳 ⊂ ℝ d x_{i}\in\mathcal{X}\subset\mathbb{R}^{d} is associated with a categorical label y i ∈ { 1 , … , C } y_{i}\in\{1,\dots,C\} among C C possible classes. Let f : 𝒳 → ℝ C f:\mathcal{X}\to\mathbb{R}^{C} denote a prediction function producing a score vector f ⁡ ( x i ) = ( f 1 ​ ( x i ) , … , f C ​ ( x i ) ) ⊤ f(x_{i})=(f_{1}(x_{i}),\dots,f_{C}(x_{i}))^{\top} , where each component f c ​ ( x i ) f_{c}(x_{i}) reflects the model’s confidence for class c c .

[21] p: The learning objective is to minimize the multiclass zero–one loss , which measures the fraction of misclassified samples:

[22] table: ℒ 0 / 1 ( f ) = 1 n ∑ i = 1 n 𝕀 [ y ^ i ≠ y i ] , y ^ i = arg max c ∈ { 1 , … , C } f c ( x i ) . \mathcal{L}_{0/1}(f)=\frac{1}{n}\sum_{i=1}^{n}\mathbb{I}\!\left[\,\hat{y}_{i}\neq y_{i}\,\right],\qquad\hat{y}_{i}=\arg\max_{c\in\{1,\dots,C\}}f_{c}(x_{i}). (1)

[23] p: While ℒ 0 / 1 \mathcal{L}_{0/1} directly quantifies classification accuracy, it is discontinuous and non-differentiable, making it unsuitable for gradient-based optimization.

[24] p: To obtain a differentiable surrogate, convex losses are commonly employed. Common loss functions in machine learning—such as squared loss, hinge loss, and logistic loss—are convex approximations of the true 0–1 misclassification loss [ 3 ] . Among these, the squared loss provides the closest approximation to the 0–1 loss on the interval ( 0 , 1 ) (0,1) , making it a natural foundation for our formulation. The multiclass squared loss penalizes deviations between predicted scores and the corresponding one-hot target encodings, summing over all classes:

[25] table: ℒ sq ( f ) = 1 n ∑ i = 1 n ∑ c = 1 C ( f c ( x i ) − 𝕀 [ y i = c ] ) 2 . \mathcal{L}_{\text{sq}}(f)=\frac{1}{n}\sum_{i=1}^{n}\sum_{c=1}^{C}\big(f_{c}(x_{i})-\mathbb{I}[y_{i}=c]\big)^{2}. (2)

[26] p: Equivalently, in matrix form, ℒ sq ​ ( f ) = 1 n ​ ‖ F ⁡ ( X ) − Y ‖ F 2 , \mathcal{L}_{\text{sq}}(f)=\frac{1}{n}\|F(X)-Y\|_{F}^{2}, where F ⁡ ( X ) ∈ ℝ n × C F(X)\in\mathbb{R}^{n\times C} collects the model outputs and Y Y is the one-hot label matrix. While this smooth, convex loss provides analytic gradients and serves as a tractable approximation to ℒ 0 / 1 \mathcal{L}_{0/1} , it also suffers from a major drawback: it imposes a quadratic penalty on extreme predicted values, leading to sensitivity to outliers [ 13 , 8 ] . This limitation motivates our projection-based formulation introduced next, which preserves smoothness while constraining outputs within a geometrically consistent region.

[27] h2: 4 Methodology

[28] h3: 4.1 Overview

[29] p: This work begins by formulating the problem in the binary classification setting, where the objective is to distinguish between positive and negative outcomes. The same geometric principles, however, extend naturally to the multiclass setting, as shown in later sections. Common loss functions in machine learning—such as squared loss, hinge loss, and logistic loss—are convex surrogates of the true 0–1 misclassification loss [ 3 ] . However, the true 0–1 loss minimizer lies at one of the vertices of the ( n , k ) (n,k) -dimensional hypersimplex, as it satisfies two key properties:

[30] p: Its entries are binary, i.e., each component of f ⁡ ( 𝐗 ) f(\mathbf{X}) takes a value in { 0 , 1 } \{0,1\} .

[31] p: For any given sample 𝐲 \mathbf{y} drawn from the distribution of Y Y , a perfect prediction vector should contain exactly k k positive entries, matching the number of positives in 𝐲 \mathbf{y} ; that is, ‖ f ⁡ ( 𝐗 ) ‖ 1 = ‖ 𝐲 ‖ 1 = k \|f(\mathbf{X})\|_{1}=\|\mathbf{y}\|_{1}=k .

[32] p: Motivated by the geometry of the optimal solution, we now introduce a series of relaxations that make the learning problem tractable. First, we relax the binary constraint and allow f ⁡ ( 𝐗 ) f(\mathbf{X}) to take real values in ℝ n \mathbb{R}^{n} , while encouraging sparsity—pushing predictions as close as possible to 0 0 or 1 1 . To balance smoothness with structural fidelity, we compose our differentiable projection operator, the soft-binary-argmax@k , which produces sparse and nearly binary outputs, with the squared loss, which ensures smooth optimization and stability. This composition yields a surrogate objective that remains differentiable while closely aligning with the discrete geometry of the hypersimplex.

[33] p: The remainder of this section is organized as follows. We begin by establishing the connection between binary-argmax@k and thresholding. Next, we formulate binary-argmax@k as a projection onto the n , k {n,k} hypersimplex, from which we derive its continuous relaxation, soft-binary-argmax@k, and analyze its key properties. Finally, we combine the soft-binary-argmax@k with a squared loss to define the HyperSimplex loss, and demonstrate its effectiveness in generalization for large batch sizes.

[34] h3: 4.2 Thresholding and the Binary-Argmax@k

[35] p: This section establishes an intuitive connection between a real-valued vector 𝐱 ∈ ℝ n \mathbf{x}\in\mathbb{R}^{n} and its binary counterpart in { 0 , 1 } n \{0,1\}^{n} . A common discretization method is thresholding , where entries exceeding a fixed boundary (typically 0.5 0.5 ) are set to 1 1 , and the rest to 0 0 . Although simple, this approach ignores relative ordering and offers no control over the number of positive components.

[36] p: A more structured alternative is the binary-argmax@k operator, denoted r k r_{k} , which assigns 1 1 to the k k largest entries of 𝐱 \mathbf{x} and 0 0 to the remaining n − k n-k . Here, the threshold is adaptively defined by the k k -th largest value of 𝐱 \mathbf{x} , reducing to standard thresholding when k = ⌈ n / 2 ⌉ k=\lceil n/2\rceil , where the threshold equals the empirical median of the logits.

[37] p: Formally, let 𝐱 ∈ ℝ n \mathbf{x}\in\mathbb{R}^{n} be a vector of scores and k ∈ { 1 , … , n } k\in\{1,\dots,n\} . We define the binary-argmax@k operator as

[38] table: r k ​ ( 𝐱 ) = 𝕀 ⁡ ( x i ≥ T k ​ ( 𝐱 ) ) , T k ​ ( 𝐱 ) = k -th largest value of ​ 𝐱 . r_{k}(\mathbf{x})=\mathbb{I}\!\left(x_{i}\geq T_{k}(\mathbf{x})\right),\quad T_{k}(\mathbf{x})=\text{$k$-th largest value of }\mathbf{x}. (3)

[39] p: This rule ensures exactly k k components of 𝐱 \mathbf{x} are set to 1 1 , enforcing the constraint

[40] table: ‖ r k ​ ( 𝐱 ) ‖ 1 = k , r k ​ ( 𝐱 ) ∈ { 0 , 1 } n . \|r_{k}(\mathbf{x})\|_{1}=k,\quad r_{k}(\mathbf{x})\in\{0,1\}^{n}. (4)

[41] p: The binary-argmax@k mapping does not provide useful derivatives, hindering gradient-based optimization. To address this, we formulate it as a linear optimization problem over the ( n , k ) (n,k) -dimensional hypersimplex Δ k n \Delta^{n}_{k} and introduce a Euclidean regularization term with a temperature parameter, yielding a smooth relaxation—the soft-binary-argmax@k. This differentiable formulation preserves the hypersimplex geometry while providing informative gradients for end-to-end learning.

[42] h3: 4.3 Binary-Argmax@k: Euclidean Projections onto the Hypersimplex

[43] p: The Euclidean projection onto the ( n , k ) (n,k) -dimensional hypersimplex can be expressed as the solution of a simple regularized linear program:

[44] table: argmax 𝐲 ∈ ℝ n ​ ⟨ 𝐱 , 𝐲 ⟩ − ‖ 𝐲 ‖ 2 2 s.t. 𝟏 ⊤ ​ 𝐲 = k , 0 ≤ 𝐲 ≤ 1 . \underset{\mathbf{y}\in\mathbb{R}^{n}}{\mathrm{argmax}}\;\;\langle\mathbf{x},\mathbf{y}\rangle-\|\mathbf{y}\|_{2}^{2}\quad\text{s.t.}\quad\mathbf{1}^{\top}\mathbf{y}=k,\quad 0\leq\mathbf{y}\leq 1. (5)

[45] p: The first term encourages alignment with the input vector 𝐱 \mathbf{x} , while the quadratic regularization term enforces proximity to the origin, thereby inducing a balance between sparsity and fidelity. The affine constraint 𝟏 ⊤ ​ 𝐲 = k \mathbf{1}^{\top}\mathbf{y}=k fixes the ℓ 1 \ell_{1} mass of 𝐲 \mathbf{y} , ensuring exactly k k active components, while the box constraint 0 ≤ 𝐲 ≤ 1 0\leq\mathbf{y}\leq 1 confines the solution to the hypercube [ 0 , 1 ] n [0,1]^{n} .

[46] p: The feasible region defined by these two constraints is precisely the ( n , k ) (n,k) -dimensional hypersimplex:

[47] table: Δ k n = { 𝐲 ∈ [ 0 , 1 ] n | ∑ i = 1 n y i = k } . \Delta^{n}_{k}=\left\{\mathbf{y}\in[0,1]^{n}\;\big|\;\sum_{i=1}^{n}y_{i}=k\right\}. (6)

[48] p: Hence, the optimization problem in ( 5 ) is equivalent to the Euclidean projection over the hypersimplex:

[49] table: Π Δ k n ​ ( 𝐱 ) = argmin 𝐲 ∈ Δ k n ​ ‖ 𝐱 − 𝐲 ‖ 2 2 . \Pi_{\Delta^{n}_{k}}(\mathbf{x})=\underset{\mathbf{y}\in\Delta^{n}_{k}}{\mathrm{argmin}}\;\|\mathbf{x}-\mathbf{y}\|_{2}^{2}. (7)

[50] p: Since Δ k n \Delta^{n}_{k} is convex and compact, this problem admits a unique solution. Geometrically, Π Δ k n ​ ( 𝐱 ) \Pi_{\Delta^{n}_{k}}(\mathbf{x}) corresponds to the point within Δ k n \Delta^{n}_{k} that lies closest to 𝐱 \mathbf{x} in Euclidean distance, and algebraically, it coincides with the binary vector that activates the k k largest components of 𝐱 \mathbf{x} , the binary-argmax@k.

[51] figure: Figure 1: Binary-argmax@k of a point 𝐱 = ( 0.1 , 1.6 , 1 ) \mathbf{x}=(0.1,1.6,1) into the exterior of the Hypersimplex (left). At k = 1 k=1 , the solution is ( 0 , 1 , 0 ) (0,1,0) . Introducing temperature to the program yields an interior solution (right), i.e., the soft-binary-argmax@1. In ℝ 3 \mathbb{R}^{3} different k k values yield points on a standard simplex, but in higher dimensions yields a point on the hypersimplex. In ℝ 4 \mathbb{R}^{4} with k = 2 k=2 , the solution lies on an octahedron [ 2 ] .

[52] h3: 4.4 Soft-Binary-Argmax@k: A Differentiable Approximation

[53] p: The projection Π Δ k n ​ ( 𝐱 ) \Pi_{\Delta^{n}_{k}}(\mathbf{x}) provides a geometric mapping from a continuous vector 𝐱 \mathbf{x} to its structured binary counterpart, but it remains piecewise constant and thus non-differentiable. Small perturbations in 𝐱 \mathbf{x} can abruptly change the identity of the top- k k elements, yielding discontinuities and zero gradients almost everywhere. Consequently, the hard binary-argmax@k operator is incompatible with gradient-based optimization.

[54] h4: Temperature-Scaled Relaxation.

[55] p: To obtain a smooth approximation, we introduce a temperature parameter τ > 0 \tau>0 that scales the regularization strength in the projection objective:

[56] table: argmin 𝐲 ∈ Δ k n ​ ( τ ​ ‖ 𝐲 ‖ 2 2 − 2 ​ ⟨ 𝐱 , 𝐲 ⟩ ) = argmin 𝐲 ∈ Δ k n ​ ( ‖ 𝐲 ‖ 2 2 − 2 ​ ⟨ 𝐱 τ , 𝐲 ⟩ ) \underset{\mathbf{y}\in\Delta^{n}_{k}}{\mathrm{argmin}}\left(\tau\|\mathbf{y}\|_{2}^{2}-2\langle\mathbf{x},\mathbf{y}\rangle\right)=\underset{\mathbf{y}\in\Delta^{n}_{k}}{\mathrm{argmin}}\left(\|\mathbf{y}\|_{2}^{2}-2\Big\langle\tfrac{\mathbf{x}}{\tau},\mathbf{y}\Big\rangle\right) (8)

[57] p: leading to the compact expression

[58] table: Π τ ​ ( 𝐱 ) = argmin 𝐲 ∈ Δ k n ​ ‖ 𝐲 − 𝐱 τ ‖ 2 2 = Π Δ k n ​ ( 𝐱 τ ) \Pi_{\tau}\!\left({\mathbf{x}}\right)=\underset{\mathbf{y}\in\Delta^{n}_{k}}{\mathrm{argmin}}\Big\|\mathbf{y}-\tfrac{\mathbf{x}}{\tau}\Big\|_{2}^{2}=\Pi_{\Delta^{n}_{k}}\!\left(\tfrac{\mathbf{x}}{\tau}\right) (9)

[59] p: As τ → 0 \tau\!\to\!0 , the operator recovers the discontinuous hard projection, while larger τ \tau values yield smoother outputs closer to the hypersimplex—defining the soft-Binary-Argmax@k operator.

[60] h6: Proposition 1 (Differentiability a.e)

[61] p: Fix k ∈ { 1 , … , n } k\in\{1,\dots,n\} and τ > 0 \tau>0 . The mapping

[62] table: F τ : ℝ n → Δ k n , F τ ​ ( 𝐱 ) := Π Δ k n ​ ( 𝐱 τ ) F_{\tau}:\ \mathbb{R}^{n}\to\Delta^{n}_{k},\qquad F_{\tau}(\mathbf{x}):=\Pi_{\Delta^{n}_{k}}\!\left(\tfrac{\mathbf{x}}{\tau}\right)

[63] p: is ( 1 / τ ) (1/\tau) -Lipschitz, hence differentiable almost everywhere (a.e.) in ℝ n \mathbb{R}^{n} .

[64] h6: Proof

[65] p: The Euclidean projection onto a closed convex set in a Hilbert space is nonexpansive: ‖ Π C ​ ( 𝐮 ) − Π C ​ ( 𝐯 ) ‖ 2 ≤ ‖ 𝐮 − 𝐯 ‖ 2 \|\Pi_{C}(\mathbf{u})-\Pi_{C}(\mathbf{v})\|_{2}\leq\|\mathbf{u}-\mathbf{v}\|_{2} for all 𝐮 , 𝐯 \mathbf{u},\mathbf{v} . With C = Δ k n C=\Delta^{n}_{k} and 𝐮 = 𝐱 / τ \mathbf{u}=\mathbf{x}/\tau , 𝐯 = 𝐳 / τ \mathbf{v}=\mathbf{z}/\tau ,

[66] table: ‖ F τ ​ ( 𝐱 ) − F τ ​ ( 𝐳 ) ‖ = ‖ Π Δ k n ​ ( 𝐱 τ ) − Π Δ k n ​ ( 𝐳 τ ) ‖ ≤ ‖ 𝐱 τ − 𝐳 τ ‖ = 1 τ ​ ‖ 𝐱 − 𝐳 ‖ . \bigl\|F_{\tau}(\mathbf{x})-F_{\tau}(\mathbf{z})\bigr\|=\Bigl\|\Pi_{\Delta^{n}_{k}}\!\left(\tfrac{\mathbf{x}}{\tau}\right)-\Pi_{\Delta^{n}_{k}}\!\left(\tfrac{\mathbf{z}}{\tau}\right)\Bigr\|\leq\Bigl\|\tfrac{\mathbf{x}}{\tau}-\tfrac{\mathbf{z}}{\tau}\Bigr\|=\tfrac{1}{\tau}\,\|\mathbf{x}-\mathbf{z}\|.

[67] p: Thus F τ F_{\tau} is ( 1 / τ ) (1/\tau) -Lipschitz. By Rademacher’s theorem, every Lipschitz map on ℝ n \mathbb{R}^{n} is differentiable a.e., proving the claim.

[68] h6: Proposition 2 (Order preservation)

[69] p: The projection solution y i = Π Δ k n ​ ( x i τ ) y_{i}=\Pi_{\Delta^{n}_{k}}\!\left(\tfrac{x_{i}}{\tau}\right) is order preserving; that is, if x 1 / τ ≥ x 2 / τ ≥ ⋯ ≥ x n / τ x_{1}/\tau\geq x_{2}/\tau\geq\cdots\geq x_{n}/\tau , then the projected coordinates satisfy y 1 ≥ y 2 ≥ ⋯ ≥ y n y_{1}\geq y_{2}\geq\cdots\geq y_{n} .

[70] h6: Proof

[71] p: From the KKT conditions of the Lagrangian associated with ( 9 ), stationarity and complementarity yield, for each i i ,

[72] table: y i = clip ⁡ ( x i / τ − λ 2 , 0 , 1 ) , y_{i}=\mathrm{clip}\!\left(x_{i}/\tau-\tfrac{\lambda}{2},\,0,\,1\right),

[73] p: where the multiplier λ \lambda is uniquely determined to satisfy the equality constraint ∑ i y i = k \sum_{i}y_{i}=k . Since the mapping t ↦ clip ⁡ ( t − λ 2 , 0 , 1 ) t\mapsto\mathrm{clip}\!\left(t-\tfrac{\lambda}{2},0,1\right) is monotone nondecreasing in t t , it follows that x 1 / τ ≥ ⋯ ≥ x n / τ ⇒ y 1 ≥ ⋯ ≥ y n x_{1}/\tau\geq\cdots\geq x_{n}/\tau\Rightarrow y_{1}\geq\cdots\geq y_{n} . See [ 10 ] for details.

[74] h6: Corollary 1 (Computation)

[75] p: Since the projection is order preserving (Proposition 2 ), adding a monotonicity constraint does not change the solution. Hence, for any sorted input 𝐱 / τ \mathbf{x}/\tau , the projection can be computed via a reduction to isotonic regression:

[76] table: Π ⁡ ( 𝐱 / τ ) = arg ⁡ min 𝐲 ∈ [ 0 , 1 ] n , 𝟏 ⊤ ​ 𝐲 = k , y 1 ≥ ⋯ ≥ y n ​ ‖ 𝐱 τ − 𝐲 ‖ 2 . \Pi(\mathbf{x}/\tau)=\underset{\begin{subarray}{c}\mathbf{y}\in[0,1]^{n},\\ \mathbf{1}^{\top}\mathbf{y}=k,\\ y_{1}\geq\cdots\geq y_{n}\end{subarray}}{\arg\min}\;\left\|\tfrac{\mathbf{x}}{\tau}-\mathbf{y}\right\|^{2}.

[77] p: The feasible set is closed and convex, ensuring a unique and differentiable solution. This reduces to a standard isotonic projection problem, solvable efficiently via the pool-adjacent-violators (PAV) algorithm [ 4 ] in 𝒪 ⁡ ( n ​ log ⁡ n ) \mathcal{O}(n\log n) time.

[78] h3: 4.5 The HyperSimplex loss

[79] p: We now compose our projection operator with the squared loss to define a smooth surrogate for binary classification. The squared loss provides high fidelity to the zero–one objective within ( 0 , 1 ) (0,1) but can be dominated by large-magnitude predictions. By composing it with the projection operator Π Δ n k \Pi_{\Delta^{k}_{n}} , we constrain predictions to the hypersimplex, preventing any coordinate from overtaking the loss while preserving the discrete geometry of the solution.

[80] p: Formally, for 𝐱 , 𝐲 ∈ ℝ n \mathbf{x},\mathbf{y}\in\mathbb{R}^{n} , define

[81] table: 𝐲 ^ = Π Δ n k ​ ( 𝐱 τ ) , L ⁡ ( 𝐱 , 𝐲 ) = 1 2 ​ ‖ 𝐲 ^ − 𝐲 ‖ 2 2 , \hat{\mathbf{y}}=\Pi_{\Delta^{k}_{n}}\!\left(\frac{\mathbf{x}}{\tau}\right),\qquad L(\mathbf{x},\mathbf{y})=\tfrac{1}{2}\|\hat{\mathbf{y}}-\mathbf{y}\|_{2}^{2},

[82] p: where τ > 0 \tau>0 controls the smoothness of the relaxation. The gradient with respect to 𝐱 \mathbf{x} follows from the chain rule:

[83] table: ∇ 𝐱 L ​ ( 𝐱 , 𝐲 ) = 1 τ ​ J Π ​ ( 𝐱 τ ) ​ ( 𝐲 ^ − 𝐲 ) , \nabla_{\mathbf{x}}L(\mathbf{x},\mathbf{y})=\frac{1}{\tau}\,J_{\Pi}\!\left(\tfrac{\mathbf{x}}{\tau}\right)(\hat{\mathbf{y}}-\mathbf{y}),

[84] p: where J Π J_{\Pi} denotes the Jacobian of the projection operator Π Δ n k \Pi_{\Delta^{k}_{n}} . Let A = { i : 0 < y ^ i < 1 } A=\{i:0<\hat{y}_{i}<1\} denote the active coordinates. On this set, the Jacobian acts as

[85] table: J Π = I | A | − 1 | A | ​ 𝟏𝟏 ⊤ , J_{\Pi}=I_{|A|}-\tfrac{1}{|A|}\mathbf{1}\mathbf{1}^{\top},

[86] p: yielding the component-wise gradient

[87] table: ( ∇ 𝐱 L ) i = { 1 τ ​ [ ( y ^ i − y i ) − 1 | A | ​ ∑ j ∈ A ( y ^ j − y j ) ] , i ∈ A , 0 , i ∉ A . (\nabla_{\mathbf{x}}L)_{i}=\begin{cases}\dfrac{1}{\tau}\!\left[(\hat{y}_{i}-y_{i})-\dfrac{1}{|A|}\!\sum_{j\in A}(\hat{y}_{j}-y_{j})\right],&i\in A,\\[6.0pt] 0,&i\notin A.\end{cases}

[88] p: At boundary points where some y ^ i ∈ { 0 , 1 } \hat{y}_{i}\in\{0,1\} , the mapping is only directionally differentiable, and any subgradient consistent with this Jacobian form is valid.

[89] h3: 4.6 Extension to Multiclass Classification

[90] p: The formulation extends naturally to the multiclass setting. For each class c ∈ { 1 , … , C } c\in\{1,\dots,C\} with logits 𝐱 ( c ) ∈ ℝ n \mathbf{x}^{(c)}\in\mathbb{R}^{n} , one-hot target 𝐲 ( c ) \mathbf{y}^{(c)} , and temperature τ c > 0 \tau_{c}>0 , we project onto the ( n , k c ) (n,k_{c}) -hypersimplex:

[91] table: 𝐩 ( c ) = Π Δ k c n ​ ( 𝐱 ( c ) τ c ) . \mathbf{p}^{(c)}=\Pi_{\Delta^{n}_{k_{c}}}\!\left(\tfrac{\mathbf{x}^{(c)}}{\tau_{c}}\right).

[92] p: The total loss is

[93] table: ℒ ⁡ ( X , Y ) = 1 2 ​ ∑ c = 1 C ‖ 𝐩 ( c ) − 𝐲 ( c ) ‖ 2 2 , ∇ 𝐱 ( c ) ℒ = 1 τ c ​ J Π ​ ( 𝐱 ( c ) τ c ) ​ ( 𝐩 ( c ) − 𝐲 ( c ) ) . \mathcal{L}(X,Y)=\tfrac{1}{2}\sum_{c=1}^{C}\bigl\|\mathbf{p}^{(c)}-\mathbf{y}^{(c)}\bigr\|_{2}^{2},\qquad\nabla_{\mathbf{x}^{(c)}}\mathcal{L}=\tfrac{1}{\tau_{c}}J_{\Pi}\!\left(\tfrac{\mathbf{x}^{(c)}}{\tau_{c}}\right)(\mathbf{p}^{(c)}-\mathbf{y}^{(c)}).

[94] p: This provides a smooth, per-class projection framework that preserves hypersimplex structure while remaining fully differentiable. During the learning process each k c k_{c} is set to match the expected number of positive responses for class c c .

[95] h2: 5 Experiments

[96] p: For our experiments, we evaluate the effectiveness of the proposed HyperSimplex loss in reducing the generalization gap compared to standard classification losses, including Cross-Entropy, Hinge, and Mean Squared Error (MSE, without projection). This setup also serves as an ablation study to isolate the contribution of our projection layer, verifying that incorporating geometric constraints on the output logits yields more consistent performance across batch sizes than the MSE objective alone.

[97] h3: 5.1 Datasets

[98] p: We conduct experiments on two standard image classification benchmarks: CIFAR-10 [ 16 ] and Fashion-MNIST [ 21 ] . CIFAR-10 consists of 60,000 color images of size 32 × 32 32\times 32 pixels, split into 50,000 training and 10,000 test samples across 10 object categories. Fashion-MNIST contains 70,000 grayscale images of size 28 × 28 28\times 28 pixels, divided into 60,000 training and 10,000 test images from 10 clothing categories, serving as a more challenging replacement for the original MNIST dataset.

[99] h3: 5.2 Experimental Setup

[100] p: We employed a standard convolutional neural network (CNN) for multiclass image classification, consisting of four convolutional layers, each followed by batch normalization, max pooling, and ReLU activation. The final feature map is flattened and passed through two fully connected layers, with the last layer producing class logits. The datasets were preprocessed using random cropping, horizontal flipping, and per-channel normalization, and randomly split into training and test sets. All experiments were implemented in PyTorch [ 20 ] and executed on 32-core AMD Ryzen Threadripper PRO 5975WX CPU with 503 GB of RAM and three NVIDIA RTX 6000 Ada Generation GPUs, each with 48 GB of VRAM.

[101] p: To ensure statistical robustness, each configuration was trained using five independent random seeds, varying both model initialization and data splits. We evaluated four loss functions—our proposed HyperSimplex loss and three widely used baselines: Cross-Entropy, Hinge, and Mean Squared Error (MSE)–across seven batch sizes (128, 256, 512, 1024, 2048, 4096 and 8192) on both CIFAR-10 and Fashion-MNIST. In total, this resulted in 280 training runs. For each configuration, we recorded the maximum test accuracy achieved per loss function and batch size, and assessed differences against the Cross-Entropy baseline using paired t t -tests at the 10% significance level. This experimental design provides a rigorous and statistically grounded comparison, isolating the contribution of the HyperSimplex formulation to generalization stability under varying batch regimes.

[102] h3: 5.3 Results

[103] p: For CIFAR-10, all seven configurations report positive mean accuracy differences, and all ( 100 % 100\% ) show statistically significant improvements at the 10% level ( p < 0.1 p<0.1 ). For Fashion-MNIST, six of seven configurations ( ≈ 86 % \approx 86\% ) also achieve significance, with only the smallest batch size ( 128 128 ) falling above the 10% threshold. Across both datasets, therefore, 13 of 14 total comparisons ( ≈ 93 % \approx 93\% ) demonstrate statistically significant gains, indicating that the proposed loss systematically outperforms cross-entropy across a wide range of training conditions.

[104] p: These findings confirm that the HyperSimplex loss maintains accuracy stability at smaller batch sizes while mitigating the degradation observed in cross-entropy as batch size increases. This supports its effectiveness as a smooth, geometry-consistent surrogate that enhances generalization and robustness in large-batch training regimes.

[105] figure: Table 1: Batch-wise Comparison of Cross-Entropy (CE) vs. HyperSimplex (HS) Losses on CIFAR-10 and Fashion-MNIST. The highlighted scores are statistically significant at a 10% level of significance. CIFAR-10 FashionMNIST Batch CE HS (ours) Δ \Delta t-stat p-val CE HS (ours) Δ \Delta t-stat p-val 128 0.8885 0.8917 0.0032 2.29 0.084 0.9456 0.9467 0.0011 1.31 0.262 256 0.8843 0.8874 0.0030 3.47 0.026 0.9434 0.9473 0.0040 4.34 0.012 512 0.8807 0.8857 0.0050 6.08 <0.01 0.9436 0.9469 0.0033 5.51 <0.01 1024 0.8776 0.8821 0.0045 9.78 <0.01 0.9413 0.9453 0.0040 6.67 <0.01 2048 0.8725 0.8791 0.0066 7.81 <0.01 0.9388 0.9446 0.0058 12.97 <0.01 4096 0.8659 0.8750 0.0090 13.14 <0.01 0.9371 0.9439 0.0069 9.68 <0.01 8192 0.8541 0.8648 0.0108 8.52 <0.01 0.9338 0.9415 0.0077 14.99 <0.01

[106] h3: 5.4 Other Experiments: Cross-domain Validation

[107] p: Additional GBRT results on tabular datasets for classification are reported in Appendix 0.A , showing that the HyperSimplex loss also improves out-of-sample generalization beyond the neural settings studied in the main text.

[108] h2: 6 Conclusion

[109] p: We introduced the soft-binary-argmax@k, a differentiable projection onto the interior of the ( n , k ) (n,k) -dimensional hypersimplex, and established its key properties—differentiability, order preservation, and efficient GPU computation. We showed how this operator integrates naturally into end-to-end learning systems, and used it to construct a surrogate to the zero–one loss for binary and multiclass settings, with statistically significant reductions in the generalization gap.

[110] p: Owing to its close alignment with the true zero–one objective, the proposed HyperSimplex loss improves generalization under large-batch training. Additional cross-domain evaluations on tabular data further suggest that the benefits of the projection extend beyond neural models. Future work will explore applications to contrastive learning objectives and structured prediction.

[111] h2: Appendix 0.A Appendix: Cross-Domain Tabular Results

[112] figure: Dataset Higgs Flight KDD10 KDD12 Criteo Avazu KKBox MovieLens Cross Entropy 0.823 0.773 0.826 0.724 0.774 0.738 0.777 0.827 HyperSimplex 0.846 0.778 0.849 0.729 0.796 0.741 0.797 0.828

[113] h2: References

[114] h2: Instructions for reporting errors

[115] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[116] p: Tip: You can select the relevant text first, to include it in your report.

[117] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[118] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
