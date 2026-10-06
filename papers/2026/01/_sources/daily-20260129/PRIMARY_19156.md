# Exact-v1 primary cached excerpts — 2601.19156

These are preserved tool responses, not author summaries. Each response is separated; its L labels are local to that response. No new fetch/revision review.

## Original response 1: stdnext2head

Convergence of Muon with Newton–Schulz (https://arxiv.org/html/2601.19156v1)
citeturn28349view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19156v1","lineno":null}); Total lines: 1787
L0: ##### Report GitHub Issue
L1: 
L2: [Button: ×]
L3: 
L4: Title: [Input: Enter title]
L5: 
L6: Content selection saved. Describe the issue below:
L7: 
L8: Description:
L9: 
L10: [Button: Submit without GitHub] [Button: Submit in GitHub]
L11: 
L12: cite0†Back to arXiv L13: 
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related work L18:   4. cite8†3 Preliminaries L19:     1. cite9†3.1 Notations L20:     2. cite10†3.2 Problem Setting: Nonconvex Optimization L21:     3. cite11†3.3 Muon Algorithm and Newton–Schulz Orthogonalization L22:     4. cite12†3.4 Newton–Schulz polynomial L23:   5. cite13†4 Main Results L24:     1. cite14†4.1 Convergence of Muon (with Newton–Schulz) L25:       1. cite15†Discussions of Theorem . L26:     2. cite16†4.2 Decay Rate of $\varepsilon_{q}$ and Convergence Rate of $\chi_{q}\to 1$ L27:       1. cite17†Discussion of Theorem . L28:       2. cite18†Practical implication. L29:     3. cite19†4.3 Proof Sketch for Theorem . L30:     4. cite20†4.4 Proof Sketch for Theorem  L31:     5. cite21†4.5 Comparisons with SGD with Momentum and Muon with $\mathrm{SVD}$ L32:       1. cite22†Discussion of Theorems  and . L33:   6. cite23†5 Numerical Experiments L34:   7. cite24†6 Conclusion L35:   8. cite25†References L36:   9. cite26†A Appendix L37:     1. cite27†A.1 Basic Facts for Matrix Norms L38:     2. cite28†A.2 Lemmas under Assumptions L39:       1. cite29†A.2.1 Assumption  L40:       2. cite30†A.2.2 Assumption  L41:     3. cite31†A.3 Newton–Schulz polynomial L42:       1. cite32†NS step preserves the unit spectral ball. L43:   10. cite33†B Muon with Finite Newton–Schulz Iteration L44:   11. cite34†C Muon with $\mathrm{SVD}$ and SGD with momentum L45:     1. cite35†C.1 Theorem  (Muon with SVD) L46:     2. cite36†C.2 Theorem  (SGD with Momentum) L47:   12. cite37†D Newton–Schulz Lemmas: Proofs L48:     1. cite38†D.1 Detailed proofs for case when $\kappa\in\{1,2\}$ L49:   13. cite39†E Wall-Clock via Computational Complexity. L50:     1. cite40†Per-iteration Orthogonalization FLOPs. L51:     2. cite41†Discussion of Lemma . L52:   14. cite42†F Numerical Experiments Detail L53:     1. cite43†F.1 Experimental Setting L54:     2. cite44†F.2 Newton–Schulz steps ($q$) ablations. L55:   15. cite45†G Additional Numerical Experiments L56:     1. cite46†Hyper-parameters L57:     2. cite47†G.1 MLP on MNIST L58:     3. cite48†G.2 CifarNet on CIFAR-10 L59:     4. cite49†G.3 ResNet-18 on CIFAR-100 L60:     5. cite50†G.4 WideResNet-28-10 on Tiny-ImageNet L61:     6. cite51†G.5 NanoGPT on FineWeb L62:     7. cite52†G.6 GPT-2 based model (1.3B) on FineWeb L63:   16. cite53†H Additional Ablation Experiments L64:     1. cite54†H.1 Newton–Schulz–polynomial degree-$\kappa$ ablations. L65:     2. cite55†H.2 Rank–dependence. L66:     3. cite56†H.3 Batch size $B$ ablations. L67:     4. cite57†H.4 Degree-2 NS polynomial vs. Ad-hoc degree-2 NS polynomial L68: cite58†License: CC BY-NC-ND 4.0†info.arxiv.org L69: 
L70: arXiv:2601.19156v1 [stat.ML] 27 Jan 2026
L71: # Convergence of Muon with Newton–Schulz
L72: 
L73: Gyu Yeol Kim Affiliation: Seoul National University Affiliation: Seoul, South Korea Email: gyuyeolkim@snu.ac.kr    Min-hwan Oh Affiliation: Seoul National University Affiliation: Seoul, South Korea Email: minoh@snu.ac.kr
L74: ###### Abstract
L75: We analyze Muon as originally proposed and used in practice—using the momentum orthogonalization with a few Newton–Schulz steps. The prior theoretical results replace this key step in Muon with an exact SVD-based polar factor. We prove that Muon with Newton–Schulz converges to a stationary point at the same rate as the SVD-polar idealization, up to a constant factor for a given number $q$ of Newton–Schulz steps.
L76: We further analyze this constant factor and prove that it converges to 1 doubly exponentially in $q$ and improves with the degree of the polynomial used in Newton–Schulz for approximating the orthogonalization direction. We also prove that Muon removes the typical square-root-of-rank loss compared to its vector-based counterpart, SGD with momentum.
L77: Our results explain why Muon with a few low-degree Newton–Schulz steps matches exact-polar (SVD) behavior at a much faster wall-clock time and explain how much momentum matrix orthogonalization via Newton–Schulz benefits over the vector-based optimizer. Overall, our theory justifies the practical Newton–Schulz design of Muon, narrowing its practice–theory gap.
L78: ## 1 Introduction
L79: Modern deep neural networks comprise billions of parameters and demand highly efficient training procedures. A persistent challenge is that most widely used optimizers—such as stochastic gradient descent (SGD) (cite59†Robbins and Monro, 1951 ) and adaptive methods such as Adam (cite60†Kingma and Ba, 2015 )—operate on vectorized parameters, thereby discarding the native matrix structure present in linear layers and attention projections.
L80: Optimizers that explicitly respect matrix structure can, in principle, yield search directions that are better aligned with the underlying geometry while remaining computationally efficient at scale.
L81: Muon (cite61†Jordan et al., 2024 ) is an optimizer designed for matrix-structured parameters. At each iteration, instead of following the raw momentum, Muon orthogonalizes the mntum matrix and then uses this orthogonalized direction to update the weights. In practice, this orthogonalization is not computed via an exact singular value decomposition (SVD)—which is accurate but expensive—but is approximated efficiently by a small, fixed number of Newton–Schulz steps.
L82: Empirical studies (cite61†Jordan et al., 2024 ; cite62†Liu et al., 2025a ) have reported strong performance at scale with this SVD-free implementation, making Muon an attractive alternative to vector-based optimizers. Despite recent attempts to analyze the convergence of Muon (cite63†Shen et al., 2025 ; cite64†Li and Hong, 2025 ; cite65†Sato et al., 2025 ), theory still lags behind practice.
L83: Existing analyses typically study an idealized variant that replaces the Newton–Schulz step—central to practical Muon—with an exact polar step computed by SVD for analytical convenience. This leaves open whether the actual SVD-free orthogonalization used in practice—i.e., a finite number of Newton–Schulz steps—admits principled nonconvex convergence guarantees, and how the Newton–Schulz approximation impacts rank dependence and efficiency. Therefore, the following research questions remain open:
L84: Research questions.
L85: 
L86:   * •
L87: 
L88: Does Muon with Newton–Schulz admit nonconvex convergence guarantees, and how do its rates compare to the exact SVD–polar idealization?
L89: 
L90:   * •
L91: 
L92: How does the Newton–Schulz steps $q$ and Newton–Schulz polynomial degree $\kappa$ control the accuracy–compute trade-off? In particular, how large is the gap caused by using Newton–Schulz, and how does that gap become negligible?
L93: 
L94:   * •
L95: Can we show that Muon converges faster than the vector-counterpart, SGD with momentum? What geometric mechanisms and rank dependence drive this gap?
L96: To address these questions, we analyze Muon as originally proposed (cite61†Jordan et al., 2024 ) and as used in practice: Muon with momentum orthogonalization computed via Newton–Schulz. For nonconvex objectives, under standard smoothness assumptions, we prove the convergence of Muon to a stationary point, measured by the nuclear norm of the gradient.
L97: We establish that the convergence rate in the number of iterations matches the idealized (but not used in practice) SVD-based exact polar variant, up to a constant factor that depends on the polar approximation error $\varepsilon_{q}$ (defined in Definition cite66†3 ) for the fixed number of Newton–Schulz steps $q$.
L98: Moreover, we show that the polar approximation error $\varepsilon_{q}$ shrinks doubly exponentially as $q$ grows and decays with larger $\kappa$, which is the degree of the polynomial used in Newton–Schulz steps. Recursive updates using this polynomial allow the optimizer to find the approximated orthogonalization direction of the momentum matrix. Hence, with only a few Newton–Schulz steps, the convergence rate of Muon quickly tends to the convergence rate of the exact polar step via SVD.
L99: Consequently, our results imply that, because a few Newton–Schulz steps are far cheaper per iteration than SVD, the practical Muon implementation with Newton–Schulz attains substantially faster wall-clock convergence.
L100: Our main contributions are summarized as follows:
L101: 
L102:   * •
L103: The first convergence result of Muon with Newton–Schulz. To our knowledge, we present the first nonconvex convergence guarantees for Muon with a finite number of Newton–Schulz steps (Theorem cite67†1 ), as originally proposed and practically used. It is important to note that even for convex optimization, the convergence of Muon with Newton–Schulz has not been shown previously.
L104: The key distinction from the existing analyses of Muon is that we do not replace Newton–Schulz in the original Muon with the exact polar computed by SVD.
L105:   * •
L106: Analysis of polar approximation error and wall-clock convergence. We prove that the polar approximation error $\varepsilon_{q}$ due to using Newton–Schulz instead of $\mathrm{SVD}$, in the Muon optimizer, decays doubly exponentially with the number of Newton–Schulz steps $q$ and decays with the degree $\kappa$ of the polynomial required to approximate the orthogonalization direction of the momentum matrix (Definition cite68†2 ).
L107: Thus, even with a few steps of Newton–Schulz, the convergence of Muon with Newton–Schulz becomes arbitrarily close to that of the SVD-variant in the number of iterations (Theorems cite69†2 and cite70†4 ). Hence, given that per-iteration computation is much more efficient for Newton–Schulz steps compared to SVD, the overall convergence in wall-clock time is much faster for Muon with Newton–Schulz.
L108:   * •
L109: 
L110: Sharper rank dependence in Muon with Newton–Schulz. To prove the comparative advantage of Muon against the vector-based counterpart, we demonstrate for the first time that Muon with Newton–Schulz sharpens the convergence rate by a factor of the square root of the rank of the momentum matrix (see Table cite71†1 and Theorem cite72†3 ).
L111: ## 2 Related work
L112: Muon and momentum orthogonalization. cite61†Jordan et al. (2024) introduced Muon, which orthogonalizes a momentum matrix via a few Newton–Schulz steps (SVD-free), and reported strong empirical results at LLM scale (cite62†Liu et al., 2025a ). Earlier work orthogonalized gradients by SVD before applying momentum (Orthogonal-SGDM; cite73†Tuddenham et al.
L113: (2022) ), whereas Muon applies momentum before orthogonalization and replaces SVD with Newton–Schulz, resulting in faster computation with only matrix multiplications. More details about Muon are described in cite11†3.3 .
L114: Second-order preconditioners vs. Muon. Matrix-aware optimizers such as Shampoo (cite74†Gupta et al., 2018 ) SOAP (cite75†Vyas et al., 2024 ) and their variants (cite76†An et al., 2025 ) are second-order preconditioners: they maintain layerwise curvature (Kronecker-factored second moments) and periodically apply inverse-root preconditioning.
L115: By contrast, Muon is not a second-order method; it neither estimates nor inverts curvature but orthogonalizes the momentum matrix via a few Newton–Schulz iterations (SVD-free, using only matrix multiplications). These methods target different mechanisms—curvature preconditioning vs. projection/normalization—and can be complementary rather than directly comparable.
L116: Practical efficiency of Muon. Large-scale training reports for Muon (cite62†Liu et al., 2025a ; cite77†Shah et al., 2025 ; cite78†Tveit et al., 2025 ) and communication/memory-aware variants (cite79†Ahn and Dion, 2025 ; cite80†Liu et al., 2025b ) motivate a theory that is SVD-free and GPU-aligned. Our analysis of Newton–Schulz, a key step in the Muon optimizer, adopts precisely that stance. The analysis provided in this work can be adapted to other variants of Muon.
L117: Convergence analysis of Muon.
L118: Several recent analyses examine Muon but typically either idealize the orthogonalization by assuming an exact SVD polar step (cite63†Shen et al., 2025 ), work under Frobenius-smoothness with dimension-driven constants (cite64†Li and Hong, 2025 ), focus on stability/variant phenomena (cite65†Sato et al., 2025 ), or offer complementary lenses (steepest descent under norms, trust-region views, implicit constraints, or LMO/Frank-Wolfe formulations) without addressing Newton–Schulz step accuracy in nonconvex rates (cite81†Bernstein and Newhouse, 2024 ; cite82†Kovalev, 2025 ; cite83†Chen et al., 2025 ; cite84†Riabinin et al., 2025 ).
L119: Key distinctions compared to the existing analyses of Muon. Prior work either assumes exact SVD polar steps, measures progress in a geometry that obscures rank benefits, or does not quantify the approximation from Newton–Schulz in Muon. Our work is the first to analyze how two key parameters—the number of Newton–Schulz steps and the degree of the polynomial used for finding the orthogonalization direction of the momentum matrix approximately—affect the convergence rate of Muon.
L120: The results indicate a nonconvex convergence rate to a stationary point, an explicit and rapidly vanishing constant factor derived from Newton–Schulz instead of SVD, and sharper rank dependence than SGD with momentum under the same metric. Overall, our work explains why Muon converges quickly (particularly in wall-clock time) as well as why only a few steps of Newton–Schulz suffice in practice.
L121: ## 3 Preliminaries
L122: ### 3.1 Notations
L123: For matrix $X\in\mathbb{R}^{m\times n}$, $X^{\top}$ is its transpose. For $X=(x_{ij})\in\mathbb{R}^{n\times n}$, $\tr(X):=\sum_{i=1}^{n}x_{ii}$. We write $\|X\|_{*}$, $\|X\|_{\mathrm{op}}$, and $\|X\|_{F}$ for the nuclear, spectral (operator), and Frobenius norms, respectively, and $\langle X,Y\rangle_{F}:=\tr(X^{\top}Y)$.
L124: For a thin SVD $X=U\Sigma V^{\top}$, the polar factor is $\polar(X):=UV^{\top}$, a partial isometry with $\|\polar(X)\|_{\mathrm{op}}\leq 1$ and $\langle X,\polar(X)\rangle_{F}=\|X\|_{*}$ (See Appendix cite27†A.1 ). For two sequences $\{a_{n}\}_{n=1}^{\infty}$ and $\{b_{n}\}_{n=1}^{\infty}$, $a_{n}=\mathcal{O}(b_{n})$ implies that there exists a constant $C>0$ such that $a_{n}\leq Cb_{n}$ holds for all $n\geq 1$. We use $\mathbb{E}[\cdot]$ for expectations over all algorithmic randomness.
L125: ### 3.2 Problem Setting: Nonconvex Optimization
L126: 
L127: We consider the stochastic optimization of a matrix-valued parameter: $W\in\mathbb{R}^{m\times n}$
L128: 
L129:  | $\displaystyle\min_{W\in\mathbb{R}^{m\times n}}f(W)\;=\;\mathbb{E}_{\xi}[f(W;\xi)],$  |
L130: where the objective $f$ is nonconvex with $f^{*}:=\inf_{W}f(W)>-\infty$. We denote by $r:=\min\{m,n\}$ the maximal possible rank of the matrix. At iteration $t$, a mini-batch $\xi_{t}=(\xi_{t,1},\ldots,\xi_{t,B})$ is drawn with $\{\xi_{t,i}\}_{i}$ i.i.d., and $\{\xi_{t}\}_{t}$ are independent across $t=1,\ldots,T$. At $t=0$, the model parameter $W_{0}\in\mathbb{R}^{m\times n}$ is initialized, and we define the initial sub-optimality as $D:=f(W_{0})-f^{*}$.
L131: In this paper, the following assumptions are made for the convergence analysis:
L132: ###### Assumption 1 (Lipschitz smoothness).
L133: 
L134: The objective function $f:\mathbb{R}^{m\times n}\to\mathbb{R}$ is continuously differentiable and $L$-Lipschitz smooth, i.e., for all $X,Y\in\mathbb{R}^{m\times n}$,
L135: 
L136:  | $\displaystyle\|\nabla f(X)-\nabla f(Y)\|_{*}\;\leq\;L\,\|X-Y\|_{\mathrm{op}}.$  |
L137: 
L138: We use smoothness with respect to the operator norm (and the nuclear norm as its dual).
L139: ###### Assumption 2 (Bounded variance).
L140: 
L141: We assume $\nabla f(W;\xi)$ is an unbiased stochastic estimator of the true gradient $\nabla f(W)$ and has bounded variance for all $W$ and a single sample $\xi$, i.e.
L142: 
L143:  | $\displaystyle\mathbb{E}[\nabla f(W;\xi)]=\nabla f(W),\qquad\mathbb{E}\big[\|\nabla f(W;\xi)-\nabla f(W)\|_{F}^{2}\big]\leq\sigma^{2}.$  |
L144: 
L145: For a mini-batch of size $B$, the variance is at most $\sigma^{2}/B$.
L146: Assumptions cite85†1 and cite86†2 are standard for analyzing first-order methods in stochastic optimization (cite87†Boyd and Vandenberghe, 2004 ; cite88†Nemirovski et al., 2009 ; cite89†Candes and Recht, 2012 ; cite90†Shapiro et al., 2021 ; cite91†Reddi et al., 2018 ; cite92†Zou et al., 2019 ).
L147: $L$-smoothness is typically defined using a norm and its dual, and the specific operator-nuclear geometry chosen here is a natural fit when working with matrix parameters and polar or orthogonal updates  (cite93†Nesterov, 2013 ; cite94†Beck, 2017 ; cite95†Jaggi, 2013 ). The bounded-variance assumption, where the mini-batch variance is $\sigma^{2}/B$, is a foundational concept for algorithms like SGD in both convex and nonconvex scenarios  (cite96†Bottou et al., 2018 ; cite97†Ghadimi and Lan, 2013 ).
L148: In this paper, the metric for the convergence rate is defined as follows:
L149: ###### Definition 1 ($\epsilon$-stationary point).
L150: 
L151: We call $W\in\mathbb{R}^{m\times n}$ an $\epsilon$-stationary point (in the nuclear norm) if $\mathbb{E}[\|\nabla f(W)\|_{*}]\leq\epsilon$. Equivalently, we say an algorithm attains $\epsilon$-stationarity in $T$ steps if
L152: 
L153:  | $\displaystyle\frac{1}{T}\sum_{t=1}^{T}\mathbb{E}[\|\nabla f(W_{t-1})\|_{*}]\leq\epsilon.$  |
L154: Note that when working with functions that have matrix inputs, using the nuclear norm to find a stationary point provides a more restrictive and precise condition than using the standard Frobenius norm. In other words, if a point satisfies the stationarity condition for the nuclear norm, it is guaranteed to also satisfy the condition for the Frobenius norm.
L155: ### 3.3 Muon Algorithm and Newton–Schulz Orthogonalization
L156: 
L157: Algorithm 1 Muon (with the illustration of Newton–Schulz orthogonalization)
L158: 
L159: 0:  learning rate $\eta>0$, momentum $\beta\in[0,1)$, Newton–Schulz steps $q\in\mathbb{N}$, Newton–Schulz polynomial $p_{\kappa}$ (degree $\kappa)$, batch size $B$, total iteration $T$.
L160: 
L161: 1:  Initialize: $M_{0}\leftarrow 0$, $W_{0}\in\mathbb{R}^{m\times n}$
L162: 
L163: 2:  for $t=1$ to $T$ do
L164: 3:   $G_{t}\leftarrow\frac{1}{B}\sum_{i=1}^{B}\nabla f(W_{t-1};\xi_{t,i})$ $\triangleright$ Compute (batch) gradients
L165: 
L166: 4:   $M_{t}\leftarrow\beta M_{t-1}+G_{t}$
L167: 
L168: 5:   $X_{t,0}\leftarrow M_{t}/\alpha_{t}$ with $\alpha_{t}=\max\{1,\|M_{t}\|_{F}\}$ $\triangleright$ Pre-Newton–Schulz scaling
L169: 
L170: 6:   for $j=1$ to $q$ do
L171: 
L172: 7:    $X_{t,j}\leftarrow p_{\kappa}(X_{t,j-1}X_{t,j-1}^{\top})\,X_{t,j-1}$ $\triangleright$ Newton–Schulz steps (Lines 6-9)
L173: 
L174: 8:   end for
L175: 
L176: 9:   $O_{t}\leftarrow X_{t,q}$
L177: 10:   $W_{t}\leftarrow W_{t-1}-\eta O_{t}$ $\triangleright$ Update parameters
L178: 
L179: 11:  end for
L180: For clarity of exposition, we present pseudocode for Muon with an explicit illustration of the Newton–Schulz steps (Lines 5–9) in Algorithm cite98†1 . Note that this is not a new algorithm; it is the original method of cite61†Jordan et al. (2024) , here written in a more general mini-batch form with a step-by-step illustration of Newton–Schulz.
L181: Rather than orthogonalizing via SVD, Muon approximates the orthogonalization direction using only matrix multiplications; the key mechanism enabling this is the Newton–Schulz-based orthogonalization.
L182: The key advantages of using Newton–Schulz for orthogonalization are as follows:
L183: 
L184:   * •
L185: 
L186: Newton–Schulz makes Muon inversion-free and SVD-free. SVD is computationally expensive and makes each iteration costly. In contrast, the Newton–Schulz approach relies solely on matrix multiplications, yielding substantially better per-iteration efficiency—especially for large parameter matrices.
L187: 
L188:   * •
L189: Newton–Schulz is an iterative method that allows for precise control over the degree of orthogonality by adjusting the number of iterations. The number of Newton–Schulz steps provides a direct trade-off between computational cost and the degree of orthogonality, offering valuable flexibility.
L190: ### 3.4 Newton–Schulz polynomial
L191: 
L192: In the Muon algorithm, at every iteration, a scaled momentum matrix $X$ is orthogonalized via Newton–Schulz steps. First, the matrix $XX^{\top}$ is formed and is then passed to a polynomial function $p_{\kappa}$ with degree $\kappa$. Recursive updates by this polynomial make the matrix $X$ nearly orthogonal, i.e., $XX^{\top}=I$. We first define this function $p_{\kappa}$ in Definition cite68†2 and state the properties of this polynomial used in Newton–Schulz.
L193: ###### Definition 2 (Newton–Schulz polynomial).
L194: 
L195: For degree $\kappa\in\mathbb{N}$, the Newton–Schulz polynomial is the Taylor truncation of $1/\sqrt{\lambda}$ at $\lambda=1$, i.e.,
L196: 
L197:  | $\displaystyle p^{(s)}(1)=\frac{d^{s}}{d\lambda^{s}}\lambda^{-1/2}\Bigg|_{\lambda=1}$  |
L198: 
L199: for $s=1,\ldots,\kappa$. The explicit form of the Newton–Schulz polynomial for degree $\kappa$ is
L200: 
L201:  | $\displaystyle p_{\kappa}(\lambda)=\sum_{s=0}^{\kappa}c_{s}(1-\lambda)^{s},\qquad c_{s}=\frac{(2s)!}{4^{s}(s!)^{2}}>0.$  |
L202: Equivalently, with reparametrization $u=1-\lambda\in[0,1]$, $p_{\kappa}(1-u)=\sum_{s=0}^{\kappa}c_{s}u^{s}$.
L203: ###### Proposition 1 (Properties of $p_{\kappa}$).
L204: 
L205: For $\lambda\in[0,1]$:
L206: 
L207:   * •
L208: 
L209: Positivity. $p_{\kappa}(\lambda)>0$ and $p_{\kappa}(\lambda)\geq 1$ with equality iff $\lambda=1$.
L210: 
L211:   * •
L212: 
L213: Monotonicity of $\tau$. Let $\tau(\lambda):=\lambda[p_{\kappa}(\lambda)]^{2}$, then we have $\tau$ non-decreasing on $[0,1]$ and $\tau(1)=1$.
L214: Consequently, for any symmetric $A\succeq 0$ with spectrum in $[0,1]$, the Newton–Schulz update $A\mapsto p_{\kappa}(A)Ap_{\kappa}(A)$ satisfies $\|p_{\kappa}(A)Ap_{\kappa}(A)\|_{\mathrm{op}}\leq 1$: Newton–Schulz steps preserve the unit spectral ball (see Appendix cite31†A.3 ). Moreover, the property of the function $\tau$ is used when proving how fast does one step of Newton–Schulz make the momentum orthogonal (Lemma cite99†2 ).
L215: In order to quantify the degree of orthogonality of the output matrix $X_{t,q}$ after $q$ steps of Newton–Schulz, and to measure the approximation error derived from Newton–Schulz compared to the exact-polar method via SVD under operator-norm, we define the following:
L216: ###### Definition 3 (Orthogonality residual and polar approximation error).
L217: 
L218: For fixed $t$, let $\Pi_{t}$ be the orthogonal projector onto $\mathrm{range}(M_{t})$. With $\{X_{t,j}\}_{j=0}^{q}$ from Algorithm cite98†1 , define the orthogonality residual $\delta_{t,j}$ and the polar approximation error $\varepsilon_{t,q}$ by
L219: 
L220:  | $\displaystyle\delta_{t,j}:=\|\Pi_{t}-X_{t,j}X_{t,j}^{\top}\|_{\mathrm{op}}\in[0,1),\qquad\varepsilon_{t,q}:=\|X_{t,q}-\polar(M_{t})\|_{\mathrm{op}}.$  |
L221: Define $\varepsilon_{q}:=\sup_{t}\varepsilon_{t,q}$ and $\delta_{0}:=\sup_{t}\delta_{t,0}$.
L222: ###### Remark 1.
L223: 
L224: In Muon, there is a scaling step for the momentum matrix before applying it to the recursive update by the Newton–Schulz polynomial (Line 5 in Algorithm cite98†1 ). This scaling ensures $\|X_{t,0}\|_{\mathrm{op}}\leq 1$, which is required to apply the Newton–Schulz polynomial properties described in Proposition cite100†1 . In parallel, the initial residual is strictly less than 1, i.e., $\delta_{t,0}\in[0,1)$ for every iteration $t$ (see Appendix cite37†D ).
L225: ## 4 Main Results
L226: We begin by stating our two main theorems: (i) a nonconvex convergence rate for Muon with a finite number of Newton–Schulz steps (Theorem cite67†1 ); and (ii) an explicit bound on the multiplicative constant induced by Newton–Schulz, together with its (doubly) exponential decay in $q$ (Theorem cite69†2 ). We then provide brief proof sketches for both theorems in Sections cite19†4.3 and cite20†4.4 .
L227: For comparisons, Section cite21†4.5 also presents convergence rates for the idealized Muon with an exact SVD-based polar step and for SGD with momentum—the vector-based baseline—stated under the same nuclear-norm stationarity metric.
L228: ### 4.1 Convergence of Muon (with Newton–Schulz)
L229: ###### Theorem 1 (Convergence of Muon with Newton–Schulz).
L230: 
L231: Suppose Assumptions cite85†1 and cite86†2 hold, and run Muon (Algorithm cite98†1 ) with initialization $W_{0}\in\mathbb{R}^{m\times n}$. Choose the stepsize and momentum as $\eta=\sqrt{\frac{(1-\beta)D}{TL}}$ and $\beta=1-\min\left\{\frac{\sqrt{LDB}}{\sigma\sqrt{rT}},1\right\}$ where $r=\min\{m,n\}$. Then there exists a factor $\chi_{q}>0$, depending only on the number $q$ of Newton–Schulz steps, such that
--------------------------------------------------------------------------------


## Original response 2: stdnext2core

Convergence of Muon with Newton–Schulz (https://arxiv.org/html/2601.19156v1)
citeturn28352view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28349view0","lineno":225}); Total lines: 1787
L190: ### 3.4 Newton–Schulz polynomial
L191: 
L192: In the Muon algorithm, at every iteration, a scaled momentum matrix $X$ is orthogonalized via Newton–Schulz steps. First, the matrix $XX^{\top}$ is formed and is then passed to a polynomial function $p_{\kappa}$ with degree $\kappa$. Recursive updates by this polynomial make the matrix $X$ nearly orthogonal, i.e., $XX^{\top}=I$. We first define this function $p_{\kappa}$ in Definition cite68†2 and state the properties of this polynomial used in Newton–Schulz.
L193: ###### Definition 2 (Newton–Schulz polynomial).
L194: 
L195: For degree $\kappa\in\mathbb{N}$, the Newton–Schulz polynomial is the Taylor truncation of $1/\sqrt{\lambda}$ at $\lambda=1$, i.e.,
L196: 
L197:  | $\displaystyle p^{(s)}(1)=\frac{d^{s}}{d\lambda^{s}}\lambda^{-1/2}\Bigg|_{\lambda=1}$  |
L198: 
L199: for $s=1,\ldots,\kappa$. The explicit form of the Newton–Schulz polynomial for degree $\kappa$ is
L200: 
L201:  | $\displaystyle p_{\kappa}(\lambda)=\sum_{s=0}^{\kappa}c_{s}(1-\lambda)^{s},\qquad c_{s}=\frac{(2s)!}{4^{s}(s!)^{2}}>0.$  |
L202: Equivalently, with reparametrization $u=1-\lambda\in[0,1]$, $p_{\kappa}(1-u)=\sum_{s=0}^{\kappa}c_{s}u^{s}$.
L203: ###### Proposition 1 (Properties of $p_{\kappa}$).
L204: 
L205: For $\lambda\in[0,1]$:
L206: 
L207:   * •
L208: 
L209: Positivity. $p_{\kappa}(\lambda)>0$ and $p_{\kappa}(\lambda)\geq 1$ with equality iff $\lambda=1$.
L210: 
L211:   * •
L212: 
L213: Monotonicity of $\tau$. Let $\tau(\lambda):=\lambda[p_{\kappa}(\lambda)]^{2}$, then we have $\tau$ non-decreasing on $[0,1]$ and $\tau(1)=1$.
L214: Consequently, for any symmetric $A\succeq 0$ with spectrum in $[0,1]$, the Newton–Schulz update $A\mapsto p_{\kappa}(A)Ap_{\kappa}(A)$ satisfies $\|p_{\kappa}(A)Ap_{\kappa}(A)\|_{\mathrm{op}}\leq 1$: Newton–Schulz steps preserve the unit spectral ball (see Appendix cite31†A.3 ). Moreover, the property of the function $\tau$ is used when proving how fast does one step of Newton–Schulz make the momentum orthogonal (Lemma cite99†2 ).
L215: In order to quantify the degree of orthogonality of the output matrix $X_{t,q}$ after $q$ steps of Newton–Schulz, and to measure the approximation error derived from Newton–Schulz compared to the exact-polar method via SVD under operator-norm, we define the following:
L216: ###### Definition 3 (Orthogonality residual and polar approximation error).
L217: 
L218: For fixed $t$, let $\Pi_{t}$ be the orthogonal projector onto $\mathrm{range}(M_{t})$. With $\{X_{t,j}\}_{j=0}^{q}$ from Algorithm cite98†1 , define the orthogonality residual $\delta_{t,j}$ and the polar approximation error $\varepsilon_{t,q}$ by
L219: 
L220:  | $\displaystyle\delta_{t,j}:=\|\Pi_{t}-X_{t,j}X_{t,j}^{\top}\|_{\mathrm{op}}\in[0,1),\qquad\varepsilon_{t,q}:=\|X_{t,q}-\polar(M_{t})\|_{\mathrm{op}}.$  |
L221: Define $\varepsilon_{q}:=\sup_{t}\varepsilon_{t,q}$ and $\delta_{0}:=\sup_{t}\delta_{t,0}$.
L222: ###### Remark 1.
L223: 
L224: In Muon, there is a scaling step for the momentum matrix before applying it to the recursive update by the Newton–Schulz polynomial (Line 5 in Algorithm cite98†1 ). This scaling ensures $\|X_{t,0}\|_{\mathrm{op}}\leq 1$, which is required to apply the Newton–Schulz polynomial properties described in Proposition cite100†1 . In parallel, the initial residual is strictly less than 1, i.e., $\delta_{t,0}\in[0,1)$ for every iteration $t$ (see Appendix cite37†D ).
L225: ## 4 Main Results
L226: We begin by stating our two main theorems: (i) a nonconvex convergence rate for Muon with a finite number of Newton–Schulz steps (Theorem cite67†1 ); and (ii) an explicit bound on the multiplicative constant induced by Newton–Schulz, together with its (doubly) exponential decay in $q$ (Theorem cite69†2 ). We then provide brief proof sketches for both theorems in Sections cite19†4.3 and cite20†4.4 .
L227: For comparisons, Section cite21†4.5 also presents convergence rates for the idealized Muon with an exact SVD-based polar step and for SGD with momentum—the vector-based baseline—stated under the same nuclear-norm stationarity metric.
L228: ### 4.1 Convergence of Muon (with Newton–Schulz)
L229: ###### Theorem 1 (Convergence of Muon with Newton–Schulz).
L230: 
L231: Suppose Assumptions cite85†1 and cite86†2 hold, and run Muon (Algorithm cite98†1 ) with initialization $W_{0}\in\mathbb{R}^{m\times n}$. Choose the stepsize and momentum as $\eta=\sqrt{\frac{(1-\beta)D}{TL}}$ and $\beta=1-\min\left\{\frac{\sqrt{LDB}}{\sigma\sqrt{rT}},1\right\}$ where $r=\min\{m,n\}$. Then there exists a factor $\chi_{q}>0$, depending only on the number $q$ of Newton–Schulz steps, such that
L232:  | $$\frac{1}{T}\sum_{t=1}^{T}\mathbb{E}\bigl[\|\nabla f(W_{t-1})\|_{*}\bigr]\leq\chi_{q}\cdot\mathcal{O}\left(\sqrt{\frac{LD}{T}}+\frac{\sigma r}{\sqrt{BT}}+\left(\frac{r\sigma^{2}LD}{BT}\right)^{1/4}\right)$$  |
L233: 
L234: Consequently, Muon with Newton–Schulz attains $\epsilon$-stationarity with an iteration complexity of $T=\mathcal{O}\left(\max\left\{\frac{\chi_{q}^{2}LD}{\epsilon^{2}},\frac{\chi_{q}^{2}r^{2}\sigma^{2}}{B\epsilon^{2}},\frac{\chi_{q}^{4}r\sigma^{2}LD}{B\epsilon^{4}}\right\}\right)$ iterations.
L235: ##### Discussions of Theorem cite67†1 .
L236: Theorem cite67†1 guarantees that Muon with Newton–Schulz converges to an $\epsilon$-stationary point. To the best of our knowledge, this convergence guarantee is the first result for Muon with Newton–Schulz. Moreover, as shown later by comparison with the SVD-based polar variant, the iteration complexity of Muon with Newton–Schulz matches the exact-polar rate up to a multiplicative factor $\chi_{q}$ that depends on the polar-approximation error $\varepsilon_{q}$ (e.g., Table cite71†1 ).
L237: Crucially, we show later in Theorem cite69†2 that $\chi_{q}\to 1$ converges at an exponential rate in the number of Newton–Schulz steps $q$, so the convergence gap (in the number of iterations) to the ideal SVD-polar rate can be made arbitrarily small. Since each Newton–Schulz step is substantially cheaper than an SVD, these results provide the first theoretical explanation for the superior practical performance observed for the original (SVD-free) Muon.
L238: ### 4.2 Decay Rate of $\varepsilon_{q}$ and Convergence Rate of $\chi_{q}\to 1$
L239: 
L240: We now quantify how fast $\chi_{q}$ approaches $1$. For a given number $q$ of Newton–Schulz steps, we can show that the polar-approximation error $\varepsilon_{q}$ decays doubly exponentially in $q$ (with faster decay for larger $\kappa$). Since $\chi_{q}$ is controlled by $\varepsilon_{q}$, it follows that $\chi_{q}\to 1$ is at the same rate. The following theorem formalizes this result.
L241: ###### Theorem 2 (Upper-bounds on $\varepsilon_{q}$ and $\chi_{q}$).
L242: 
L243: For the Newton–Schulz polynomial with degree $\kappa$ and for any $t$, $\delta_{t,q}\leq\delta_{t,0}^{(\kappa+1)^{q}}$. Hence, the bound of the polar approximation error $\varepsilon_{q}$ and the factor $\chi_{q}$ occurred by Newton–Schulz is
L244:  | $\displaystyle\varepsilon_{q}\leq 1-\sqrt{1-\delta_{0}^{(\kappa+1)^{q}}}\leq\delta_{0}^{(\kappa+1)^{q}},\qquad\chi_{q}=\frac{1}{1-\varepsilon_{q}}\leq\frac{1}{\sqrt{1-\delta_{0}^{(\kappa+1)^{q}}}},$  |
L245: 
L246: where $\delta_{0}:=\sup_{t}\delta_{t,0}<1$.
L247: ##### Discussion of Theorem cite69†2 .
L248: 
L249: The theorem shows that $\varepsilon_{q}$ is bounded by $\delta_{0}^{\,(\kappa+1)^{q}}$. Hence, $\varepsilon_{q}$ vanishes doubly exponentially in $q$ (and improves with larger $\kappa$). Therefore, $\chi_{q}\to 1$ at the same doubly exponential rate. Together with Theorem cite67†1 , this result implies that the iteration-complexity gap between Newton–Schulz and the idealized SVD-polar update becomes negligible after only a few Newton–Schulz steps.
L250: ##### Practical implication.
L251: 
L252: A finite number of Newton–Schulz steps yields iteration complexity essentially indistinguishable from exact SVD updates (up to the factor $\chi_{q}\to 1$ doubly exponentially fast), while dramatically reducing per-iteration cost by using only matrix multiplications.
L253: ### 4.3 Proof Sketch for Theorem cite67†1 .
L254: 
L255: We briefly outline the main ideas. First, introduce the scaled momentum $N_{t}=(1-\beta)M_{t}$ (faithfully following the original update rule), so the EMA becomes $N_{t}\leftarrow\beta N_{t-1}+(1-\beta)G_{t}$. Next, apply the descent lemma (Lemma cite101†6 ) to the update $W_{t}\leftarrow W_{t-1}-\eta O_{t}$, which yields a term of the form $\langle\nabla f(W_{t-1}),O_{t}\rangle_{F}$. Decompose this inner product as
L256:  | $\displaystyle\langle\nabla f(W_{t-1}),O_{t}\rangle_{F}=\langle N_{t},O_{t}\rangle_{F}+\langle\nabla f(W_{t-1})-N_{t},O_{t}\rangle_{F},$  |
L257: 
L258: thereby isolating the momentum mismatch. Prior analyses typically stop here and average over iterations. In contrast, we further split $\langle N_{t},O_{t}\rangle_{F}$ as
L259: 
L260:  | $\displaystyle\langle N_{t},O_{t}\rangle_{F}=\langle N_{t},P_{t}\rangle_{F}+\langle N_{t},O_{t}-P_{t}\rangle_{F},$  |
L261: separating the exact polar factor $P_{t}$ from the Newton–Schulz orthogonalizer (the output matrix of the Newton–Schulz routine). As we define the polar approximation error $\varepsilon_{q}$ as the discrepancy between the exact polar factor $P_{t}=\polar(N_{t})=\polar(M_{t})$ and the actual step $O_{t}$ produced by $q$ steps of Newton–Schulz, we can control this part with respect to $\varepsilon_{q}$.
L262: This yields a one-step descent inequality for Muon that explicitly includes the Newton–Schulz-induced error $\varepsilon_{q}$. Averaging this inequality over $t=1,\ldots,T$ and choosing $\eta$ and $\beta$ as specified in Theorem cite67†1 produces the stated convergence rate. Full details appear in Appendix cite33†B .
--------------------------------------------------------------------------------


## Original response 3: muon19156eval

Convergence of Muon with Newton–Schulz (https://arxiv.org/html/2601.19156v1)
citeturn28367view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: click({"ref_id":"turn28349view0","id":23}); Total lines: 1787
L0: ##### Report GitHub Issue
L1: 
L2: [Button: ×]
L3: 
L4: Title: [Input: Enter title]
L5: 
L6: Content selection saved. Describe the issue below:
L7: 
L8: Description:
L9: 
L10: [Button: Submit without GitHub] [Button: Submit in GitHub]
L11: 
L12: cite0†Back to arXiv L13: 
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related work L18:   4. cite8†3 Preliminaries L19:     1. cite9†3.1 Notations L20:     2. cite10†3.2 Problem Setting: Nonconvex Optimization L21:     3. cite11†3.3 Muon Algorithm and Newton–Schulz Orthogonalization L22:     4. cite12†3.4 Newton–Schulz polynomial L23:   5. cite13†4 Main Results L24:     1. cite14†4.1 Convergence of Muon (with Newton–Schulz) L25:       1. cite15†Discussions of Theorem . L26:     2. cite16†4.2 Decay Rate of $\varepsilon_{q}$ and Convergence Rate of $\chi_{q}\to 1$ L27:       1. cite17†Discussion of Theorem . L28:       2. cite18†Practical implication. L29:     3. cite19†4.3 Proof Sketch for Theorem . L30:     4. cite20†4.4 Proof Sketch for Theorem  L31:     5. cite21†4.5 Comparisons with SGD with Momentum and Muon with $\mathrm{SVD}$ L32:       1. cite22†Discussion of Theorems  and . L33:   6. cite23†5 Numerical Experiments L34:   7. cite24†6 Conclusion L35:   8. cite25†References L36:   9. cite26†A Appendix L37:     1. cite27†A.1 Basic Facts for Matrix Norms L38:     2. cite28†A.2 Lemmas under Assumptions L39:       1. cite29†A.2.1 Assumption  L40:       2. cite30†A.2.2 Assumption  L41:     3. cite31†A.3 Newton–Schulz polynomial L42:       1. cite32†NS step preserves the unit spectral ball. L43:   10. cite33†B Muon with Finite Newton–Schulz Iteration L44:   11. cite34†C Muon with $\mathrm{SVD}$ and SGD with momentum L45:     1. cite35†C.1 Theorem  (Muon with SVD) L46:     2. cite36†C.2 Theorem  (SGD with Momentum) L47:   12. cite37†D Newton–Schulz Lemmas: Proofs L48:     1. cite38†D.1 Detailed proofs for case when $\kappa\in\{1,2\}$ L49:   13. cite39†E Wall-Clock via Computational Complexity. L50:     1. cite40†Per-iteration Orthogonalization FLOPs. L51:     2. cite41†Discussion of Lemma . L52:   14. cite42†F Numerical Experiments Detail L53:     1. cite43†F.1 Experimental Setting L54:     2. cite44†F.2 Newton–Schulz steps ($q$) ablations. L55:   15. cite45†G Additional Numerical Experiments L56:     1. cite46†Hyper-parameters L57:     2. cite47†G.1 MLP on MNIST L58:     3. cite48†G.2 CifarNet on CIFAR-10 L59:     4. cite49†G.3 ResNet-18 on CIFAR-100 L60:     5. cite50†G.4 WideResNet-28-10 on Tiny-ImageNet L61:     6. cite51†G.5 NanoGPT on FineWeb L62:     7. cite52†G.6 GPT-2 based model (1.3B) on FineWeb L63:   16. cite53†H Additional Ablation Experiments L64:     1. cite54†H.1 Newton–Schulz–polynomial degree-$\kappa$ ablations. L65:     2. cite55†H.2 Rank–dependence. L66:     3. cite56†H.3 Batch size $B$ ablations. L67:     4. cite57†H.4 Degree-2 NS polynomial vs. Ad-hoc degree-2 NS polynomial L68: cite58†License: CC BY-NC-ND 4.0†info.arxiv.org L69: 
L70: arXiv:2601.19156v1 [stat.ML] 27 Jan 2026
L71: # Convergence of Muon with Newton–Schulz
L72: 
L73: Gyu Yeol Kim Affiliation: Seoul National University Affiliation: Seoul, South Korea Email: gyuyeolkim@snu.ac.kr    Min-hwan Oh Affiliation: Seoul National University Affiliation: Seoul, South Korea Email: minoh@snu.ac.kr
L74: ###### Abstract
L75: We analyze Muon as originally proposed and used in practice—using the momentum orthogonalization with a few Newton–Schulz steps. The prior theoretical results replace this key step in Muon with an exact SVD-based polar factor. We prove that Muon with Newton–Schulz converges to a stationary point at the same rate as the SVD-polar idealization, up to a constant factor for a given number $q$ of Newton–Schulz steps.
L76: We further analyze this constant factor and prove that it converges to 1 doubly exponentially in $q$ and improves with the degree of the polynomial used in Newton–Schulz for approximating the orthogonalization direction. We also prove that Muon removes the typical square-root-of-rank loss compared to its vector-based counterpart, SGD with momentum.
L77: Our results explain why Muon with a few low-degree Newton–Schulz steps matches exact-polar (SVD) behavior at a much faster wall-clock time and explain how much momentum matrix orthogonalization via Newton–Schulz benefits over the vector-based optimizer. Overall, our theory justifies the practical Newton–Schulz design of Muon, narrowing its practice–theory gap.
L78: ## 1 Introduction
L79: Modern deep neural networks comprise billions of parameters and demand highly efficient training procedures. A persistent challenge is that most widely used optimizers—such as stochastic gradient descent (SGD) (cite59†Robbins and Monro, 1951 ) and adaptive methods such as Adam (cite60†Kingma and Ba, 2015 )—operate on vectorized parameters, thereby discarding the native matrix structure present in linear layers and attention projections.
L80: Optimizers that explicitly respect matrix structure can, in principle, yield search directions that are better aligned with the underlying geometry while remaining computationally efficient at scale.
L81: Muon (cite61†Jordan et al., 2024 ) is an optimizer designed for matrix-structured parameters. At each iteration, instead of following the raw momentum, Muon orthogonalizes the mntum matrix and then uses this orthogonalized direction to update the weights. In practice, this orthogonalization is not computed via an exact singular value decomposition (SVD)—which is accurate but expensive—but is approximated efficiently by a small, fixed number of Newton–Schulz steps.
L82: Empirical studies (cite61†Jordan et al., 2024 ; cite62†Liu et al., 2025a ) have reported strong performance at scale with this SVD-free implementation, making Muon an attractive alternative to vector-based optimizers. Despite recent attempts to analyze the convergence of Muon (cite63†Shen et al., 2025 ; cite64†Li and Hong, 2025 ; cite65†Sato et al., 2025 ), theory still lags behind practice.
L83: Existing analyses typically study an idealized variant that replaces the Newton–Schulz step—central to practical Muon—with an exact polar step computed by SVD for analytical convenience. This leaves open whether the actual SVD-free orthogonalization used in practice—i.e., a finite number of Newton–Schulz steps—admits principled nonconvex convergence guarantees, and how the Newton–Schulz approximation impacts rank dependence and efficiency. Therefore, the following research questions remain open:
L84: Research questions.
L85: 
L86:   * •
L87: 
L88: Does Muon with Newton–Schulz admit nonconvex convergence guarantees, and how do its rates compare to the exact SVD–polar idealization?
L89: 
L90:   * •
L91: 
L92: How does the Newton–Schulz steps $q$ and Newton–Schulz polynomial degree $\kappa$ control the accuracy–compute trade-off? In particular, how large is the gap caused by using Newton–Schulz, and how does that gap become negligible?
L93: 
L94:   * •
L95: Can we show that Muon converges faster than the vector-counterpart, SGD with momentum? What geometric mechanisms and rank dependence drive this gap?
L96: To address these questions, we analyze Muon as originally proposed (cite61†Jordan et al., 2024 ) and as used in practice: Muon with momentum orthogonalization computed via Newton–Schulz. For nonconvex objectives, under standard smoothness assumptions, we prove the convergence of Muon to a stationary point, measured by the nuclear norm of the gradient.
L97: We establish that the convergence rate in the number of iterations matches the idealized (but not used in practice) SVD-based exact polar variant, up to a constant factor that depends on the polar approximation error $\varepsilon_{q}$ (defined in Definition cite66†3 ) for the fixed number of Newton–Schulz steps $q$.
L98: Moreover, we show that the polar approximation error $\varepsilon_{q}$ shrinks doubly exponentially as $q$ grows and decays with larger $\kappa$, which is the degree of the polynomial used in Newton–Schulz steps. Recursive updates using this polynomial allow the optimizer to find the approximated orthogonalization direction of the momentum matrix. Hence, with only a few Newton–Schulz steps, the convergence rate of Muon quickly tends to the convergence rate of the exact polar step via SVD.
L99: Consequently, our results imply that, because a few Newton–Schulz steps are far cheaper per iteration than SVD, the practical Muon implementation with Newton–Schulz attains substantially faster wall-clock convergence.
L100: Our main contributions are summarized as follows:
L101: 
L102:   * •
L103: The first convergence result of Muon with Newton–Schulz. To our knowledge, we present the first nonconvex convergence guarantees for Muon with a finite number of Newton–Schulz steps (Theorem cite67†1 ), as originally proposed and practically used. It is important to note that even for convex optimization, the convergence of Muon with Newton–Schulz has not been shown previously.
L104: The key distinction from the existing analyses of Muon is that we do not replace Newton–Schulz in the original Muon with the exact polar computed by SVD.
L105:   * •
L106: Analysis of polar approximation error and wall-clock convergence. We prove that the polar approximation error $\varepsilon_{q}$ due to using Newton–Schulz instead of $\mathrm{SVD}$, in the Muon optimizer, decays doubly exponentially with the number of Newton–Schulz steps $q$ and decays with the degree $\kappa$ of the polynomial required to approximate the orthogonalization direction of the momentum matrix (Definition cite68†2 ).
L107: Thus, even with a few steps of Newton–Schulz, the convergence of Muon with Newton–Schulz becomes arbitrarily close to that of the SVD-variant in the number of iterations (Theorems cite69†2 and cite70†4 ). Hence, given that per-iteration computation is much more efficient for Newton–Schulz steps compared to SVD, the overall convergence in wall-clock time is much faster for Muon with Newton–Schulz.
L108:   * •
L109: 
L110: Sharper rank dependence in Muon with Newton–Schulz. To prove the comparative advantage of Muon against the vector-based counterpart, we demonstrate for the first time that Muon with Newton–Schulz sharpens the convergence rate by a factor of the square root of the rank of the momentum matrix (see Table cite71†1 and Theorem cite72†3 ).
L111: ## 2 Related work
L112: Muon and momentum orthogonalization. cite61†Jordan et al. (2024) introduced Muon, which orthogonalizes a momentum matrix via a few Newton–Schulz steps (SVD-free), and reported strong empirical results at LLM scale (cite62†Liu et al., 2025a ). Earlier work orthogonalized gradients by SVD before applying momentum (Orthogonal-SGDM; cite73†Tuddenham et al.
L113: (2022) ), whereas Muon applies momentum before orthogonalization and replaces SVD with Newton–Schulz, resulting in faster computation with only matrix multiplications. More details about Muon are described in cite11†3.3 .
L114: Second-order preconditioners vs. Muon. Matrix-aware optimizers such as Shampoo (cite74†Gupta et al., 2018 ) SOAP (cite75†Vyas et al., 2024 ) and their variants (cite76†An et al., 2025 ) are second-order preconditioners: they maintain layerwise curvature (Kronecker-factored second moments) and periodically apply inverse-root preconditioning.
L115: By contrast, Muon is not a second-order method; it neither estimates nor inverts curvature but orthogonalizes the momentum matrix via a few Newton–Schulz iterations (SVD-free, using only matrix multiplications). These methods target different mechanisms—curvature preconditioning vs. projection/normalization—and can be complementary rather than directly comparable.
L116: Practical efficiency of Muon. Large-scale training reports for Muon (cite62†Liu et al., 2025a ; cite77†Shah et al., 2025 ; cite78†Tveit et al., 2025 ) and communication/memory-aware variants (cite79†Ahn and Dion, 2025 ; cite80†Liu et al., 2025b ) motivate a theory that is SVD-free and GPU-aligned. Our analysis of Newton–Schulz, a key step in the Muon optimizer, adopts precisely that stance. The analysis provided in this work can be adapted to other variants of Muon.
L117: Convergence analysis of Muon.
L118: Several recent analyses examine Muon but typically either idealize the orthogonalization by assuming an exact SVD polar step (cite63†Shen et al., 2025 ), work under Frobenius-smoothness with dimension-driven constants (cite64†Li and Hong, 2025 ), focus on stability/variant phenomena (cite65†Sato et al., 2025 ), or offer complementary lenses (steepest descent under norms, trust-region views, implicit constraints, or LMO/Frank-Wolfe formulations) without addressing Newton–Schulz step accuracy in nonconvex rates (cite81†Bernstein and Newhouse, 2024 ; cite82†Kovalev, 2025 ; cite83†Chen et al., 2025 ; cite84†Riabinin et al., 2025 ).
L119: Key distinctions compared to the existing analyses of Muon. Prior work either assumes exact SVD polar steps, measures progress in a geometry that obscures rank benefits, or does not quantify the approximation from Newton–Schulz in Muon. Our work is the first to analyze how two key parameters—the number of Newton–Schulz steps and the degree of the polynomial used for finding the orthogonalization direction of the momentum matrix approximately—affect the convergence rate of Muon.
L120: The results indicate a nonconvex convergence rate to a stationary point, an explicit and rapidly vanishing constant factor derived from Newton–Schulz instead of SVD, and sharper rank dependence than SGD with momentum under the same metric. Overall, our work explains why Muon converges quickly (particularly in wall-clock time) as well as why only a few steps of Newton–Schulz suffice in practice.
L121: ## 3 Preliminaries
L122: ### 3.1 Notations
L123: For matrix $X\in\mathbb{R}^{m\times n}$, $X^{\top}$ is its transpose. For $X=(x_{ij})\in\mathbb{R}^{n\times n}$, $\tr(X):=\sum_{i=1}^{n}x_{ii}$. We write $\|X\|_{*}$, $\|X\|_{\mathrm{op}}$, and $\|X\|_{F}$ for the nuclear, spectral (operator), and Frobenius norms, respectively, and $\langle X,Y\rangle_{F}:=\tr(X^{\top}Y)$.
L124: For a thin SVD $X=U\Sigma V^{\top}$, the polar factor is $\polar(X):=UV^{\top}$, a partial isometry with $\|\polar(X)\|_{\mathrm{op}}\leq 1$ and $\langle X,\polar(X)\rangle_{F}=\|X\|_{*}$ (See Appendix cite27†A.1 ). For two sequences $\{a_{n}\}_{n=1}^{\infty}$ and $\{b_{n}\}_{n=1}^{\infty}$, $a_{n}=\mathcal{O}(b_{n})$ implies that there exists a constant $C>0$ such that $a_{n}\leq Cb_{n}$ holds for all $n\geq 1$. We use $\mathbb{E}[\cdot]$ for expectations over all algorithmic randomness.
L125: ### 3.2 Problem Setting: Nonconvex Optimization
L126: 
L127: We consider the stochastic optimization of a matrix-valued parameter: $W\in\mathbb{R}^{m\times n}$
L128: 
L129:  | $\displaystyle\min_{W\in\mathbb{R}^{m\times n}}f(W)\;=\;\mathbb{E}_{\xi}[f(W;\xi)],$  |
L130: where the objective $f$ is nonconvex with $f^{*}:=\inf_{W}f(W)>-\infty$. We denote by $r:=\min\{m,n\}$ the maximal possible rank of the matrix. At iteration $t$, a mini-batch $\xi_{t}=(\xi_{t,1},\ldots,\xi_{t,B})$ is drawn with $\{\xi_{t,i}\}_{i}$ i.i.d., and $\{\xi_{t}\}_{t}$ are independent across $t=1,\ldots,T$. At $t=0$, the model parameter $W_{0}\in\mathbb{R}^{m\times n}$ is initialized, and we define the initial sub-optimality as $D:=f(W_{0})-f^{*}$.
L131: In this paper, the following assumptions are made for the convergence analysis:
L132: ###### Assumption 1 (Lipschitz smoothness).
L133: 
L134: The objective function $f:\mathbb{R}^{m\times n}\to\mathbb{R}$ is continuously differentiable and $L$-Lipschitz smooth, i.e., for all $X,Y\in\mathbb{R}^{m\times n}$,
L135: 
L136:  | $\displaystyle\|\nabla f(X)-\nabla f(Y)\|_{*}\;\leq\;L\,\|X-Y\|_{\mathrm{op}}.$  |
L137: 
L138: We use smoothness with respect to the operator norm (and the nuclear norm as its dual).
L139: ###### Assumption 2 (Bounded variance).
L140: 
L141: We assume $\nabla f(W;\xi)$ is an unbiased stochastic estimator of the true gradient $\nabla f(W)$ and has bounded variance for all $W$ and a single sample $\xi$, i.e.
L142: 
L143:  | $\displaystyle\mathbb{E}[\nabla f(W;\xi)]=\nabla f(W),\qquad\mathbb{E}\big[\|\nabla f(W;\xi)-\nabla f(W)\|_{F}^{2}\big]\leq\sigma^{2}.$  |
L144: 
L145: For a mini-batch of size $B$, the variance is at most $\sigma^{2}/B$.
L146: Assumptions cite85†1 and cite86†2 are standard for analyzing first-order methods in stochastic optimization (cite87†Boyd and Vandenberghe, 2004 ; cite88†Nemirovski et al., 2009 ; cite89†Candes and Recht, 2012 ; cite90†Shapiro et al., 2021 ; cite91†Reddi et al., 2018 ; cite92†Zou et al., 2019 ).
L147: $L$-smoothness is typically defined using a norm and its dual, and the specific operator-nuclear geometry chosen here is a natural fit when working with matrix parameters and polar or orthogonal updates  (cite93†Nesterov, 2013 ; cite94†Beck, 2017 ; cite95†Jaggi, 2013 ). The bounded-variance assumption, where the mini-batch variance is $\sigma^{2}/B$, is a foundational concept for algorithms like SGD in both convex and nonconvex scenarios  (cite96†Bottou et al., 2018 ; cite97†Ghadimi and Lan, 2013 ).
L148: In this paper, the metric for the convergence rate is defined as follows:
L149: ###### Definition 1 ($\epsilon$-stationary point).
L150: 
L151: We call $W\in\mathbb{R}^{m\times n}$ an $\epsilon$-stationary point (in the nuclear norm) if $\mathbb{E}[\|\nabla f(W)\|_{*}]\leq\epsilon$. Equivalently, we say an algorithm attains $\epsilon$-stationarity in $T$ steps if
L152: 
L153:  | $\displaystyle\frac{1}{T}\sum_{t=1}^{T}\mathbb{E}[\|\nabla f(W_{t-1})\|_{*}]\leq\epsilon.$  |
L154: Note that when working with functions that have matrix inputs, using the nuclear norm to find a stationary point provides a more restrictive and precise condition than using the standard Frobenius norm. In other words, if a point satisfies the stationarity condition for the nuclear norm, it is guaranteed to also satisfy the condition for the Frobenius norm.
L155: ### 3.3 Muon Algorithm and Newton–Schulz Orthogonalization
L156: 
L157: Algorithm 1 Muon (with the illustration of Newton–Schulz orthogonalization)
L158: 
L159: 0:  learning rate $\eta>0$, momentum $\beta\in[0,1)$, Newton–Schulz steps $q\in\mathbb{N}$, Newton–Schulz polynomial $p_{\kappa}$ (degree $\kappa)$, batch size $B$, total iteration $T$.
L160: 
L161: 1:  Initialize: $M_{0}\leftarrow 0$, $W_{0}\in\mathbb{R}^{m\times n}$
L162: 
L163: 2:  for $t=1$ to $T$ do
L164: 3:   $G_{t}\leftarrow\frac{1}{B}\sum_{i=1}^{B}\nabla f(W_{t-1};\xi_{t,i})$ $\triangleright$ Compute (batch) gradients
L165: 
L166: 4:   $M_{t}\leftarrow\beta M_{t-1}+G_{t}$
L167: 
L168: 5:   $X_{t,0}\leftarrow M_{t}/\alpha_{t}$ with $\alpha_{t}=\max\{1,\|M_{t}\|_{F}\}$ $\triangleright$ Pre-Newton–Schulz scaling
L169: 
L170: 6:   for $j=1$ to $q$ do
L171: 
L172: 7:    $X_{t,j}\leftarrow p_{\kappa}(X_{t,j-1}X_{t,j-1}^{\top})\,X_{t,j-1}$ $\triangleright$ Newton–Schulz steps (Lines 6-9)
L173: 
L174: 8:   end for
L175: 
L176: 9:   $O_{t}\leftarrow X_{t,q}$
L177: 10:   $W_{t}\leftarrow W_{t-1}-\eta O_{t}$ $\triangleright$ Update parameters
L178: 
L179: 11:  end for
L180: For clarity of exposition, we present pseudocode for Muon with an explicit illustration of the Newton–Schulz steps (Lines 5–9) in Algorithm cite98†1 . Note that this is not a new algorithm; it is the original method of cite61†Jordan et al. (2024) , here written in a more general mini-batch form with a step-by-step illustration of Newton–Schulz.
L181: Rather than orthogonalizing via SVD, Muon approximates the orthogonalization direction using only matrix multiplications; the key mechanism enabling this is the Newton–Schulz-based orthogonalization.
L182: The key advantages of using Newton–Schulz for orthogonalization are as follows:
L183: 
L184:   * •
L185: 
L186: Newton–Schulz makes Muon inversion-free and SVD-free. SVD is computationally expensive and makes each iteration costly. In contrast, the Newton–Schulz approach relies solely on matrix multiplications, yielding substantially better per-iteration efficiency—especially for large parameter matrices.
L187: 
L188:   * •
L189: Newton–Schulz is an iterative method that allows for precise control over the degree of orthogonality by adjusting the number of iterations. The number of Newton–Schulz steps provides a direct trade-off between computational cost and the degree of orthogonality, offering valuable flexibility.
L190: ### 3.4 Newton–Schulz polynomial
L191: 
L192: In the Muon algorithm, at every iteration, a scaled momentum matrix $X$ is orthogonalized via Newton–Schulz steps. First, the matrix $XX^{\top}$ is formed and is then passed to a polynomial function $p_{\kappa}$ with degree $\kappa$. Recursive updates by this polynomial make the matrix $X$ nearly orthogonal, i.e., $XX^{\top}=I$. We first define this function $p_{\kappa}$ in Definition cite68†2 and state the properties of this polynomial used in Newton–Schulz.
L193: ###### Definition 2 (Newton–Schulz polynomial).
L194: 
L195: For degree $\kappa\in\mathbb{N}$, the Newton–Schulz polynomial is the Taylor truncation of $1/\sqrt{\lambda}$ at $\lambda=1$, i.e.,
L196: 
L197:  | $\displaystyle p^{(s)}(1)=\frac{d^{s}}{d\lambda^{s}}\lambda^{-1/2}\Bigg|_{\lambda=1}$  |
L198: 
L199: for $s=1,\ldots,\kappa$. The explicit form of the Newton–Schulz polynomial for degree $\kappa$ is
L200: 
L201:  | $\displaystyle p_{\kappa}(\lambda)=\sum_{s=0}^{\kappa}c_{s}(1-\lambda)^{s},\qquad c_{s}=\frac{(2s)!}{4^{s}(s!)^{2}}>0.$  |
L202: Equivalently, with reparametrization $u=1-\lambda\in[0,1]$, $p_{\kappa}(1-u)=\sum_{s=0}^{\kappa}c_{s}u^{s}$.
L203: ###### Proposition 1 (Properties of $p_{\kappa}$).
L204: 
L205: For $\lambda\in[0,1]$:
L206: 
L207:   * •
L208: 
L209: Positivity. $p_{\kappa}(\lambda)>0$ and $p_{\kappa}(\lambda)\geq 1$ with equality iff $\lambda=1$.
L210: 
L211:   * •
L212: 
L213: Monotonicity of $\tau$. Let $\tau(\lambda):=\lambda[p_{\kappa}(\lambda)]^{2}$, then we have $\tau$ non-decreasing on $[0,1]$ and $\tau(1)=1$.
L214: Consequently, for any symmetric $A\succeq 0$ with spectrum in $[0,1]$, the Newton–Schulz update $A\mapsto p_{\kappa}(A)Ap_{\kappa}(A)$ satisfies $\|p_{\kappa}(A)Ap_{\kappa}(A)\|_{\mathrm{op}}\leq 1$: Newton–Schulz steps preserve the unit spectral ball (see Appendix cite31†A.3 ). Moreover, the property of the function $\tau$ is used when proving how fast does one step of Newton–Schulz make the momentum orthogonal (Lemma cite99†2 ).
L215: In order to quantify the degree of orthogonality of the output matrix $X_{t,q}$ after $q$ steps of Newton–Schulz, and to measure the approximation error derived from Newton–Schulz compared to the exact-polar method via SVD under operator-norm, we define the following:
L216: ###### Definition 3 (Orthogonality residual and polar approximation error).
L217: 
L218: For fixed $t$, let $\Pi_{t}$ be the orthogonal projector onto $\mathrm{range}(M_{t})$. With $\{X_{t,j}\}_{j=0}^{q}$ from Algorithm cite98†1 , define the orthogonality residual $\delta_{t,j}$ and the polar approximation error $\varepsilon_{t,q}$ by
L219: 
L220:  | $\displaystyle\delta_{t,j}:=\|\Pi_{t}-X_{t,j}X_{t,j}^{\top}\|_{\mathrm{op}}\in[0,1),\qquad\varepsilon_{t,q}:=\|X_{t,q}-\polar(M_{t})\|_{\mathrm{op}}.$  |
L221: Define $\varepsilon_{q}:=\sup_{t}\varepsilon_{t,q}$ and $\delta_{0}:=\sup_{t}\delta_{t,0}$.
L222: ###### Remark 1.
L223: 
L224: In Muon, there is a scaling step for the momentum matrix before applying it to the recursive update by the Newton–Schulz polynomial (Line 5 in Algorithm cite98†1 ). This scaling ensures $\|X_{t,0}\|_{\mathrm{op}}\leq 1$, which is required to apply the Newton–Schulz polynomial properties described in Proposition cite100†1 . In parallel, the initial residual is strictly less than 1, i.e., $\delta_{t,0}\in[0,1)$ for every iteration $t$ (see Appendix cite37†D ).
L225: ## 4 Main Results
L226: We begin by stating our two main theorems: (i) a nonconvex convergence rate for Muon with a finite number of Newton–Schulz steps (Theorem cite67†1 ); and (ii) an explicit bound on the multiplicative constant induced by Newton–Schulz, together with its (doubly) exponential decay in $q$ (Theorem cite69†2 ). We then provide brief proof sketches for both theorems in Sections cite19†4.3 and cite20†4.4 .
L227: For comparisons, Section cite21†4.5 also presents convergence rates for the idealized Muon with an exact SVD-based polar step and for SGD with momentum—the vector-based baseline—stated under the same nuclear-norm stationarity metric.
L228: ### 4.1 Convergence of Muon (with Newton–Schulz)
L229: ###### Theorem 1 (Convergence of Muon with Newton–Schulz).
L230: 
L231: Suppose Assumptions cite85†1 and cite86†2 hold, and run Muon (Algorithm cite98†1 ) with initialization $W_{0}\in\mathbb{R}^{m\times n}$. Choose the stepsize and momentum as $\eta=\sqrt{\frac{(1-\beta)D}{TL}}$ and $\beta=1-\min\left\{\frac{\sqrt{LDB}}{\sigma\sqrt{rT}},1\right\}$ where $r=\min\{m,n\}$. Then there exists a factor $\chi_{q}>0$, depending only on the number $q$ of Newton–Schulz steps, such that
--------------------------------------------------------------------------------


## Original response 4: muon19156eval

Convergence of Muon with Newton–Schulz (https://arxiv.org/html/2601.19156v1)
citeturn28367view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: click({"ref_id":"turn28349view0","id":43}); Total lines: 1787
--------------------------------------------------------------------------------


## Original response 5: muon19156eval

Convergence of Muon with Newton–Schulz (https://arxiv.org/html/2601.19156v1)
citeturn28367view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: click({"ref_id":"turn28349view0","id":57}); Total lines: 1787


## Original response 6: muon19156tail

Convergence of Muon with Newton–Schulz (https://arxiv.org/html/2601.19156v1)
citeturn28384view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28349view0","lineno":318}); Total lines: 1787
L307: ###### Theorem 4 (Muon with SVD).
L308: 
L309: Under Assumptions cite85†1 and cite86†2 , setting $\varepsilon_{q}=0$ in Theorem cite67†1 yields
L310: 
L311:  | $\displaystyle\frac{1}{T}\sum_{t=1}^{T}\mathbb{E}\|\nabla f(W_{t-1})\|_{*}\;\leq\;\mathcal{O}\!\left(\sqrt{\frac{LD}{T}}+\frac{\sigma r}{\sqrt{BT}}+\left(\frac{r\sigma^{2}LD}{BT}\right)^{1/4}\right),$  |
L312: Consequently, the idealized Muon with $\mathrm{SVD}$ attains $\epsilon$-stationarity with iteration complexity of $\mathcal{O}\left(\max\left\{\frac{LD}{\epsilon^{2}},\frac{r^{2}\sigma^{2}}{B\epsilon^{2}},\frac{r\sigma^{2}LD}{B\epsilon^{4}}\right\}\right)$
L313: ##### Discussion of Theorems cite72†3 and cite70†4 .
L314: Relative to SGD with momentum, the SVD-based polar variant of Muon removes the $\sqrt{r}$ factor from the deterministic (first) term and sharpens rank dependence in the stochastic terms under the same nuclear-norm stationarity metric.
L315: Geometrically, the polar step aligns the update with the leading singular structure of the gradient (via spectral–nuclear duality), converting a Frobenius-aligned descent direction into one that is optimally aligned for the nuclear norm, thereby sharpening the $r$ dependence.
L316: Turning to the practical Muon with Newton–Schulz, Theorem cite67†1 shows that its iteration complexity matches that of the SVD-based polar variant (Theorem cite70†4 ) up to a multiplicative factor $\chi_{q}$. By Theorem cite69†2 , $\chi_{q}\!\to\!1$ doubly exponentially fast in the number of Newton–Schulz steps $q$ (and improves with the polynomial degree $\kappa$). Consequently, a small $q$ already yields rates that are essentially indistinguishable from the ideal SVD-based baseline in iteration count.
L317: Since each Newton–Schulz step uses only matrix multiplications (and avoids SVD), the per-iteration cost is much lower, which explains the superior wall-clock performance of the original SVD-free Muon observed in practice.
L318: ## 5 Numerical Experiments
L319: Setup. We conduct a numerical experiment with the CIFAR-10 (50k/10k) dataset and a CNN model, specifically CifarNet, which has approximately $2$M parameters. We compare optimizers: SGD with momentum (baseline), idealized Muon with SVD, and Muon with Newton–Schulz ($q\in\{1,2,3\}$). For the Newton–Schulz step sweep, we use the Newton–Schulz polynomial $p_{\kappa}$ with degree $\kappa=2$. We run 50 epochs, and the batch size is $B=512$. Results are plotted in Fig. cite102†1 .
L320: Performance is assessed by plotting the training loss (left column) and test loss (right column) over epochs (top row) as well as the cumulative wall-clock time (bottom row). Results represent the average of five runs with different random seeds, including standard deviations. More detailed numerical settings are described in Appendix cite43†F.1 .
L321: Ablation on Newton–Schulz step $q$. As $q$ increases, the learning dynamics per epoch steadily improve: Muon with $q=1$ already outperforms SGD-M, and $q\in{2,3}$ nearly coincides with the SVD-based Muon in both train loss and test loss, in line with Theorems cite67†1 and cite69†2 , which state that the Newton–Schulz variant matches the SVD iteration complexity up to a factor $\chi_{q}\to 1$ that decays doubly exponentially in $q$.
L322: At the same time, the bottom row of Fig. cite102†1 shows that Muon with $q=2$ or $3$ reaches a given test loss substantially faster in wall-clock time than the SVD variant, reflecting the lower per-iteration cost of the Newton–Schulz update.
L323: Figure 1: Newton–Schulz steps ($q$) ablation. Muon with Newton–Schulz for $q\in\{1,2,3\}$ vs. Muon (SVD) and SGD with momentum (SGD-M, baseline).
L324: We additionally performed numerical experiments on various datasets using models at different scales (with the number of parameters indicated in parentheses): a multilayer perceptron (MLP) with 0.5M parameters on MNIST; ResNet-18 (11.2M) on CIFAR-100; WideResNet-28-10 (36.6M) on Tiny-ImageNet; NanoGPT (124M, Transformer) on FineWeb; and a GPT-2–based model (1.3B, Transformer) on FineWeb. All additional experimental results are presented in Appendix cite45†G .
L325: Ablation on Newton–Schulz polynomial degree $\kappa$. We perform a controlled ablation that varies the degree of the Newton–Schulz polynomial $\kappa$ while fixing the number of Newton–Schulz steps to $q=3$ for all variants. Increasing the degree $\kappa\in\{1,\dots,5\}$ improves optimization (the loss drops faster at a fixed epoch) but lengthens each step, yielding a clear accuracy–time trade-off (See Appendix cite54†H.1 ).
L326: This mirrors the theory that the residual contracts as $\delta_{j+1}\leq\delta_{j}^{\kappa+1}$ (Lemma cite103†3 ), while computation scales with polynomial evaluations.
L327: Rank dependence. We vary the monitored layer’s effective rank $r\in\{16,32,64,128,216\}$ and plot the epoch-averaged $\|\nabla f(W)\|_{*}$ on a log–log scale. SGD-M shows a positive slope of approximately $0.3$ (grows with $r$), whereas Muon and its variants are nearly flat. These observations are precisely in line with Theorem cite72†3 and Theorem cite70†4 , which state that orthogonalizing momentum removes the deterministic $\sqrt{r}$ penalty and softens the rank dependence of the stochastic terms.
L328: The more detailed experimental settings and results are deferred to Appendix cite55†H.2 .
--------------------------------------------------------------------------------


## Original response 7: muon19156tail

Convergence of Muon with Newton–Schulz (https://arxiv.org/html/2601.19156v1)
citeturn28384view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28349view0","lineno":1470}); Total lines: 1787
L1436: Hyperparameters and schedules. Unless stated otherwise, we train for $50$ epochs with a batch size of $B=512$ on the GPU (the CPU fallback uses $B=256$). Each run uses a different seed.
L1437: 
L1438:   * •
L1439: 
L1440: Main optimizer (one of Muon $(q)$, Muon ($\mathrm{SVD}$), or SGD-M) on convolutional filters: learning rate $\eta=0.0860632$, momentum $\beta=0.730778$.
L1441: 
L1442:   * •
L1443: Auxiliary SGD (whitening bias, BatchNorm biases, linear head): learning rates $\eta_{\text{other}}=1.4949\times 10^{-3}$ and $\eta_{\text{head}}=1.72446$ with momentum $0.989703$ (Nesterov).
L1444: 
L1445:   * •
L1446: 
L1447: Label smoothing $0.2$, and gradient clipping $\|\cdot\|_{2}\leq 1.0$.
L1448: 
L1449:   * •
L1450: 
L1451: Schedule: The same warm-up + cosine schedule is applied to all optimizers: a 5% linear warm-up of total steps followed by cosine decay to $0$. Schedulers step once per update.
L1452: Evaluation. At the end of each epoch, we evaluate the test loss using the same normalization (no augmentation). We record (i) epoch-wise training loss, (ii) test loss, and (iii) the cumulative wall-clock time. Results are aggregated across $5$ runs. Figures report $(mean\pm 1\cdot std)$ and include both epoch-aligned and time-aligned views to disentangle statistical and systemic effects.
L1453: ### F.2 Newton–Schulz steps ($q$) ablations.
L1454: 
L1455: Optimizers under comparison. We compare:
L1456: 
L1457:   1. 1.
L1458: 
L1459: Muon $q$-step: SGD with momentum followed by an orthogonalization of the momentum matrix using $q$ Newton–Schulz steps (Algorithm cite98†1 ); $q\in\{0,1,2,3\}$. The case $q=0$ is a normalization-only ablation (no orthogonalization).
L1460: 
L1461:   2. 2.
L1462: 
L1463: Muon ($\mathrm{SVD}$): Muon with an exact polar step $UV^{\top}$ via $\mathrm{SVD}$.
L1464: 
L1465:   3. 3.
L1466: 
L1467: SGD-M: SGD with momentum baseline with identical schedules.
L1468: All methods share identical schedules and auxiliary updates (Appendix cite43†F.1 ).
L1469: 
L1470: Orthogonalization details. For Muon with $q$-Newton–Schulz steps, we use Newton–Schulz polynomial, $p_{\kappa}$
L1471: 
L1472:  | $\displaystyle p(\lambda)=a+b\lambda+c\lambda^{2},\qquad(a,b,c)=(15/8,-5/4,3/8),$  |
L1473: applied as $X\leftarrow aX+(bA+cA^{2})X$ with $A=XX^{\top}$ and $X=M/\|M\|_{F}$; if the matrix is tall, we employ the transpose trick. The $\mathrm{SVD}$ variant normalizes $M$ by its Frobenius norm and returns $UV^{\top}$. In all Muon variants, each weight tensor is re-normalized once per step to the Frobenius norm $\sqrt{\text{out\_channels}}$ to stabilize scales.
L1474: Ablations on $q$. Our main comparison varies the number of Newton–Schulz steps $q\in\{1,2,3\}$ while holding the polynomial fixed to $p_{\kappa}$, and contrasts these with Muon with $\mathrm{SVD}$ and SGD-M. All other components (architecture, schedules, augmentation) are kept identical across methods to ensure a fair comparison.
L1475: ## Appendix G Additional Numerical Experiments
L1476: 
L1477: Optimizers compared:
L1478: 
L1479:   * •
L1480: 
L1481: SGD with Momentum
L1482: 
L1483:   * •
L1484: 
L1485: Muon (Newton–Schulz) with 1, 2, 3 steps per update
L1486: 
L1487:   * •
L1488: 
L1489: Muon with exact SVD (polar factor)
L1490: 
L1491: Dataset and Model:
L1492: 
L1493:   * •
L1494: 
L1495: MNIST (60K) / MLP (0.5M)
L1496: 
L1497:   * •
L1498: 
L1499: CIFAR-10 (50K) / CifarNet (2M) : Main text
L1500: 
L1501:   * •
L1502: 
L1503: CIFAR-100 (50K) / ResNet-18 (11.2M)
L1504: 
L1505:   * •
L1506: 
L1507: Tiny-ImageNet (100K) / WideResNet-28-10 (36.6M)
L1508: 
L1509:   * •
L1510: 
L1511: FineWeb (10M tokens from sample-10BT) / NanoGPT (124.2M) & GPT-2 (1.3B)
L1512: 
L1513:     * –
L1514: 
L1515: block_size = 1024
L1516:     * –
L1517: 
L1518: num_blocks = (10M - 1) // 1024 = 9,765 sequences (for causal LM)
L1519: 
L1520:     * –
L1521: 
L1522: n_layer: 12 & 24 (transformer blocks)
L1523: 
L1524:     * –
L1525: 
L1526: n_head: 12 & 16
L1527: 
L1528:     * –
L1529: 
L1530: n_embd: 768 & 2048
L1531: 
L1532:     * –
L1533: 
L1534: Vocab size: tokenizer.vocab_size from GPT2TokenizerFast (50257)
L1535: 
L1536:     * –
L1537: 
L1538: Token embedding: nn.Embedding(vocab_size, 768)
L1539: 
L1540:     * –
L1541: 
L1542: Positional embedding: nn.Embedding(block_size, 768)
L1543: 
L1544:     * –
L1545: 
L1546: Each of the 12 transformer blocks
L1547: 
L1548:       * *
L1549: LayerNorm $\rightarrow$ multi-head causal self-attention (QKV + output projection) $\rightarrow$ residual
L1550: 
L1551:       * *
L1552: 
L1553: LayerNorm $\rightarrow$ 4$\times$-wide MLP (3072 hidden) $\rightarrow$ residual
L1554: 
L1555:     * –
L1556: 
L1557: Final LayerNorm
L1558: 
L1559:     * –
L1560: 
L1561: Total n_params: 124.2M & 1313.63M (1.31B)
L1562: ##### Hyper-parameters
L1563: 
L1564:   * •
L1565: 
L1566: MLP on MNIST:
L1567: 
L1568:     * –
L1569: 
L1570: model: 784 $\rightarrow$ 512$\rightarrow$ 256 $\rightarrow$ 10
L1571: 
L1572:     * –
L1573: 
L1574: learning rate: 0.08; momentum: 0.7
L1575: 
L1576:     * –
L1577: 
L1578: 256 batch size; 50 epochs, 5 runs
L1579: 
L1580:   * •
L1581: 
L1582: ResNet-18 on CIFAR-100:
L1583: 
L1584:     * –
L1585: 
L1586: model: torchvision.models.resnet18
L1587: 
L1588:     * –
L1589: 
L1590: learning rate: 0.08; momentum: 0.7
L1591: 
L1592:     * –
L1593: 
L1594: 512 batch size; 50 epochs, 5 runs
L1595: 
L1596:   * •
L1597: 
L1598: WideResNet-28-10 on Tiny-ImageNet:
L1599: 
L1600:     * –
L1601: 
L1602: model: WideResNet(depth=28, widen_factor=10, num_classes=200, drop_rate=0.0)
L1603:     * –
L1604: 
L1605: learning rate: 0.08; momentum: 0.7
L1606: 
L1607:     * –
L1608: 
L1609: 128 batch size; 30 epochs, 3 runs
L1610: 
L1611:   * •
L1612: 
L1613: NanoGPT & GPT-1.3B on FineWeb:
L1614: 
L1615:     * –
L1616: 
L1617: model: NanoGPT & GPT-1.3B
L1618: 
L1619:     * –
L1620: 
L1621: learning rate: 0.02; momentum: 0.95; batch size: 8
L1622: 
L1623:     * –
L1624: 
L1625: 10M training tokens, 1M validation tokens
L1626: 
L1627:     * –
L1628: 
L1629: 8 RTX-3090 GPUs
L1630: 
L1631:     * –
L1632: 
L1633: max steps: 6000
L1634: ### G.1 MLP on MNIST
L1635: Figure 2: Train losses of MLP on MNIST across wall-clock time and epochs Table 2: Wall-clock time training performance of MLP (0.5M) on MNIST dataset
L1636:  | Wall-clock time train loss
L1637: --- | ---
L1638: Optimizer  | 50 sec  | 100 sec  | 150 sec  | 200 sec  | 250 sec
L1639: --- | --- | --- | --- | --- | ---
L1640: SGD-M  | 0.550  | 0.525  | 0.517  | 0.514  | 0.513
L1641: Muon with SVD  | 0.616  | 0.612  | 0.600  | 0.583  | 0.565
L1642: Muon ($q$=1)  | 0.526  | 0.514  | 0.506  | 0.502  | 0.501
--------------------------------------------------------------------------------


## Original response 8: muon19156tail

Convergence of Muon with Newton–Schulz (https://arxiv.org/html/2601.19156v1)
citeturn28384view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28349view0","lineno":1744}); Total lines: 1787
L1736: Results. Across $r\in\{16,32,64,128,216\}$, SGD-M exhibits a positive log–log slope (about $0.3$), while both Muon variants are nearly flat. After dividing by $\sqrt{r}$, the Muon curves show a slope of about $-0.5$ (Muon with $\mathrm{SVD}$: -0.4 and Muon with Newton–Schulz: -0.61) , as predicted, whereas SGD-M becomes almost flat (slope with $-0.21$).
L1737: ### H.3 Batch size $B$ ablations.
L1738: 
L1739: We sweep $B\in\{64,128,256,512,1024\}$ with Muon ($q=3$) under identical schedules and report epoch–aligned and time–aligned views (Fig. cite164†10 ). The schedule is step–based, so larger $B$ implies fewer total steps over $E$ epochs. We report both epoch–aligned and wall–clock-aligned curves.
L1740: From a systems perspective, increasing $B$ improves throughput up to a regime of diminishing returns. From an optimization perspective, a larger $B$ reduces gradient noise but also decreases the frequency of orthogonalization steps per epoch ($N_{\mathrm{proj}}=N_{\text{train}}/B$).
L1741: 
L1742: In our runs, the best time–to-accuracy is achieved for a large batch size $B=1024$, while a small $B$ suffers from noise, taking a greater amount of time.
L1743: Figure 10: Batch size. Train/test loss vs. epoch and wall-clock for $B\in\{64,128,256,512,1024\}$.
L1744: ### H.4 Degree-2 NS polynomial vs. Ad-hoc degree-2 NS polynomial
L1745: 
L1746: Figure 11: NS polynomial vs. Ad-hoc polynomial. Train/test loss vs. epoch and wall-clock.
L1747: 
L1748: Analysis of $p_{\text{ad-hoc}}$
L1749: 
L1750: Let $p_{\text{ad-hoc}}(\lambda)=3.4445-4.7750\,\lambda+2.0315\,\lambda^{2}$ and $\tau(\lambda)=\lambda p(\lambda)^{2}$.
L1751: 
L1752: The statement that $\tau_{\text{ad-hoc}}(\lambda)$ is monotone non-decreasing on $[0,1]$ is false, and the underlying condition that $p_{\text{ad-hoc}}(\lambda)\in[0,1]$ is also not met.
L1753: On the interval $[0,1]$, the range of $p(\lambda)$ is $[0.701,3.4445]$. Since this range is not contained within $[0,1]$, the premise $p(\lambda)\in[0,1]$ is false.
L1754: 
L1755: A function is monotone non-decreasing if its derivative is greater than or equal to zero over the entire interval. The derivative of $\tau(\lambda)$ is:
L1756: 
L1757:  | $\displaystyle\tau_{\text{ad-hoc}}^{\prime}(\lambda)=\frac{d}{d\lambda}\tau_{\text{ad-hoc}}(\lambda)=20.635\lambda^{4}-77.5824\lambda^{3}+110.3556\lambda^{2}-65.781\lambda+11.8641$  |
L1758: To check for monotonicity, we can evaluate the derivative at the endpoints of the interval $[0,1]$:
L1759: 
L1760:   * •
L1761: 
L1762: At $\lambda=0$: $\tau_{\text{ad-hoc}}^{\prime}(0)=11.8641$
L1763: 
L1764:   * •
L1765: 
L1766: At $\lambda=1$: $\tau_{\text{ad-hoc}}^{\prime}(1)=20.635-77.5824+110.3556-65.781+11.8641=-0.5087$
L1767: Since $\tau_{\text{ad-hoc}}^{\prime}(0)>0$ and $\tau_{\text{ad-hoc}}^{\prime}(1)<0$, the derivative changes from positive to negative within the interval. This means the function $\tau_{\text{ad-hoc}}(\lambda)$ increases for a portion of the interval and then decreases.
L1768: 
L1769: Therefore, the claim that $\tau_{\text{ad-hoc}}(\lambda)$ is monotone non-decreasing on $[0,1]$ is false. The function has a local maximum at approximately $\lambda\approx 0.308$.
L1770: Hence, the monotonicity premise of Lemma cite99†2 fails for $p_{\text{ad-hoc}}$, even though $\tau(1)=p(1)^{2}=0.701^{2}<1$ holds. This explains why our guarantees apply to $p_{\kappa}$ but not to the ad-hoc quadratic, which remains an empirical heuristic.
L1771: 
L1772: Experimental support, please cite165†view the build logs for errors. Generated by cite166†L A T E xml†math.nist.gov .
L1773: ## Instructions for reporting errors
L1774: 
L1775: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
L1776: 
L1777:   * Click the "Report Issue" () button, located in the page header.
L1778: 
L1779: Tip: You can select the relevant text first, to include it in your report.
L1780: Our team has already identified cite167†the following issues†github.com . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
L1781: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a cite168†list of packages that need conversion†github.com , and welcome cite169†developer contributions†github.com .
L1782: 
L1783: We gratefully acknowledge support from our major funders, cite170†member institutions†info.arxiv.org , , and all contributors.
L1784: cite171†About†info.arxiv.org · cite172†Help†info.arxiv.org · cite173†Contact†info.arxiv.org · cite174†Subscribe†info.arxiv.org · cite175†Copyright†info.arxiv.org · cite176†Privacy†info.arxiv.org · cite177†Accessibility†info.arxiv.org · cite178†Operational Status (opens in new tab)†status.arxiv.org L1785: 
L1786: Major funding support from
--------------------------------------------------------------------------------


## Original response 9: muon19156tail

Convergence of Muon with Newton–Schulz (https://arxiv.org/html/2601.19156v1)
citeturn28384view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"turn28349view0","pattern":"CUDA"}); Total lines: 1787
No matching text found for "CUDA"--------------------------------------------------------------------------------


## Original response 10: muon19156tail

Convergence of Muon with Newton–Schulz (https://arxiv.org/html/2601.19156v1)
citeturn28384view4 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"turn28349view0","pattern":"Hardware"}); Total lines: 1787
L1387:  | $\displaystyle\tau^{\prime}(\lambda)$  | $\displaystyle=\left(\frac{15}{8}-\frac{5}{4}\lambda+\frac{3}{8}\lambda^{2}\right)^{2}+2\lambda\left(\frac{15}{8}-\frac{5}{4}\lambda+\frac{3}{8}\lambda^{2}\right)$  |
L1389: Since $\tau^{\prime}(\lambda)\geq 0$ for $\lambda\in[0,1]$ and $\tau(1)=1$, we can apply Lemma cite99†2 . The orthogonality residual $\delta_{t,j}$ is updated by one Newton–Schulz step as
L1390:  | $\displaystyle\delta_{t,j+1}$  | $\displaystyle=\phi(\delta_{t,j})=1-(1-\delta_{t,j})[p(1-\delta_{t,j})]^{2}$  |
L1391:  |  | $\displaystyle=1-(1-\delta_{t,j})\left(\frac{15}{8}-\frac{5}{4}(1-\delta_{t,j})+\frac{3}{8}(1-\delta_{t,j})^{2}\right)^{2}$  |
L1392:  |  | $\displaystyle=1-(1-\delta_{t,j})\left(1+\frac{1}{2}\delta_{t,j}+\frac{3}{8}\delta_{t,j}^{2}\right)^{2}$  |
L1393:  |  | $\displaystyle=1-(1-\delta_{t,j})\left(1+\delta_{t,j}+\delta_{t,j}^{2}+\frac{3}{8}\delta_{t,j}^{3}+\frac{9}{64}\delta_{t,j}^{4}\right)$  |
L1394:  |  | $\displaystyle=\frac{\delta_{t,j}^{3}(40+15\delta_{t,j}+9\delta_{t,j}^{2})}{64}\leq\delta_{t,j}^{3}$  |
L1395: By induction, after $q$ steps, we get the relationship, $\delta_{t,q}\leq(\delta_{t,0})^{3^{q}}$. Given the assumption that $\delta_{t,0}\leq\rho<1$ for all $t$, the conclusion follows directly:
L1396: 
L1397:  | $\displaystyle\delta_{t,q}\leq\rho^{3^{q}}$  |
L1398: 
L1399: This shows that the orthogonality residual decreases cubically with each iteration, which is a very rapid rate of convergence. ∎
L1400: ## Appendix E Wall-Clock via Computational Complexity.
L1401: 
L1402: At each iteration $t$, Muon performs an orthogonalization of the momentum matrix $M_{t}$ via either $\mathrm{SVD}$ or Newton–Schulz (NS). We write $\Phi_{\text{gemm}}$ for the effective GEMM throughput (FLOP/s), and $\Phi_{\text{svd}}$ for the effective throughput of the $\mathrm{SVD}$ routine. In practice $\Phi_{\text{gemm}}\gg\Phi_{\text{svd}}$ due to far higher hardware utilization of GEMM.
L1403: ##### Per-iteration Orthogonalization FLOPs.
L1404: 
L1405: For a single layer index by $\ell$ with $m\leq n$ (for $m>n$, apply to $M_{t}^{\top}$ and transpose-trick):
L1406: 
L1407:   * •
L1408: 
L1409: Muon with SVD. A thin $\mathrm{SVD}$ of $M_{t}\in\mathbb{R}^{m\times n}$ and extracting the polar factor $U_{t}V_{t}^{\top}$ costs (cite160†Golub and Reinsch, 1971 ):
L1410: 
L1411:  | $\displaystyle\text{FLOPs}_{\text{svd}}^{(\ell)}(m,n)=\Theta(4m^{2}n+8m^{3})$  |
L1412: Wall-clock time per layer is $t_{\text{svd}}^{(\ell)}=\text{FLOPs}_{\text{svd}}^{(\ell)}(m,n)/\Phi_{\text{svd}}$.
L1413: 
L1414:   * •
L1415: Muon with NS ($q$-steps, $\kappa$-degree). Newton–Schulz follows Horner’s rule when recursively updating the scaled momentum matrix using the Newton–Schulz polynomial. Newton–Schulz forms $A=XX^{\top}\in\mathbb{R}^{m\times m}$ and applies the degree-$\kappa$ polynomial to $X$ via Horner’s rule. Each NS step needs one $m\times n$ by $n\times m$ GEMM to build $A$ and $\kappa$ multiplies $AY$ (each $m\times m$ by $m\times n$). Hence,
L1416:  | $\displaystyle\text{FLOPs}_{\text{ns}}^{(\ell)}(m,n;q,\kappa)=\Theta(2q(\kappa+1)m^{2}n)$  |
L1417: 
L1418: Wall-clock time per layer is $t_{\text{ns}}^{(\ell)}=\text{FLOPs}_{\text{ns}}^{(\ell)}(m,n;q,\kappa)/\Phi_{\text{gemm}}$.
L1419: ###### Lemma 11.
L1420: 
L1421: For a layer with $m\leq n$, the wall-clock time ratio between Muon with $\mathrm{SVD}$ and Muon with Newton–Schulz ($q$-steps, $\kappa$-degree) is,
L1422: 
L1423:  | $\displaystyle\frac{t_{\text{svd}}^{(\ell)}}{t_{\text{ns}}^{(\ell)}}=\frac{\Theta(4m^{2}n+8m^{3})}{\Theta(2q(\kappa+1)m^{2}n)}\cdot\frac{\Phi_{\text{gemm}}}{\Phi_{\text{svd}}}=\Theta\left(\frac{2+4\tfrac{m}{n}}{q(\kappa+1)}\right)\cdot\underbrace{\frac{\Phi_{\text{gemm}}}{\Phi_{\text{svd}}}}_{\text{efficiency ratio }\gg 1}$  |
L1424: ##### Discussion of Lemma cite161†11 .
L1425: 
L1426: With the practical setting $q\in\{2,3\}$ and $\kappa\in\{1,2\}$, the algebraic factor $\frac{2+4(m/n)}{q(\kappa+1)}$ is $\mathcal{O}(0.3{\sim}1)$, so the wall-clock speedup is essentially the GEMM/$\mathrm{SVD}$ efficiency ratio. On modern GPUs, $\Phi_{\text{gemm}}/\Phi_{\text{svd}}$ is often $4{\sim}10$, so NS typically yields a multi-$\times$ speedup per iteration over $\mathrm{SVD}$, matching empirical observations in Figure cite102†1 .
L1427: Practical Interpretation. Newton–Schulz scales linearly in $q$ (accuracy knob) and uses only GEMMs, which map efficiently to GPUs. Exact SVD pays an additional $m^{3}$ term and typically incurs larger constants. Hence for small $q$ and modest $\kappa$, Newton–Schulz is substantially cheaper per update than a full SVD while achieving near-exact orthogonalization in practice.
L1428: ## Appendix F Numerical Experiments Detail
L1429: ### F.1 Experimental Setting
L1430: 
L1431: Task and metric. All experiments are conducted on CIFAR-10 (50k train / 10k test) with the standard channel-wise normalization $\text{mean}=(0.4914,0.4822,0.4465)$ and $\text{std}=(0.2470,0.2435,0.2616)$.
L1432: 
L1433: We report cross-entropy train loss and test loss. Plots show the $(mean\pm 1\cdot std)$ over $5$ independent runs, and we also report the wall-clock time (in seconds) accumulated from the beginning of training.

