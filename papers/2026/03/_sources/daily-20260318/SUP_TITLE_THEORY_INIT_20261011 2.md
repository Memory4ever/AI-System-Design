Muon Converges under Heavy-Tailed Noise: Nonconvex Hölder-Smooth Empirical Risk Minimization (https://arxiv.org/html/2603.15059v1)
citeturn33072view0 [wordlim: 200] Crawled: last week; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2603.15059v1","lineno":null}); Total lines: 698
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:     1. cite7†1.1 Background L18:     2. cite8†1.2 Motivation L19:     3. cite9†1.3 Main results L20:       1. cite10†1.3.1 Descent property L21:       2. cite11†1.3.2 Convergence L22:       3. cite12†1.3.3 Convergence rate L23:   3. cite13†2 Nonconvex Hölder-Smooth ERM L24:     1. cite14†2.1 Assumptions and Examples L25:     2. cite15†2.2 Useful properties of mini-batch gradient L26:   4. cite16†3 Mini-batch SGD L27:     1. cite17†3.1 Descent property L28:     2. cite18†3.2 Convergence L29:     3. cite19†3.3 Convergence Rate L30:       1. cite20†3.3.1 Upper convergence bound L31:       2. cite21†3.3.2 Lower convergence bound L32:   5. cite22†4 Muon without Momentum: Comparisons with Mini-batch SGD L33:     1. cite23†4.1 Descent property L34:     2. cite24†4.2 Convergence L35:     3. cite25†4.3 Convergence rate L36:       1. cite26†4.3.1 Upper convergence bound L37:       2. cite27†4.3.2 Lower convergence bound L38:   6. cite28†5 Muon L39:     1. cite29†5.1 Descent property L40:     2. cite30†5.2 Convergence L41:     3. cite31†5.3 Convergence Rate L42:       1. cite32†5.3.1 Upper convergence bound L43:       2. cite33†5.3.2 Lower convergence bound L44:   7. cite34†6 Conclusion L45:   8. cite35†A Examples of $(\eta_{t})$ and $(b_{t})$ L46:     1. cite36†A.1 Examples of $(\eta_{t})$ and $(b_{t})$ satisfying () and () L47:     2. cite37†A.2 Examples of $(\eta_{t})$ and $(b_{t})$ satisfying () L48:   9. cite38†References L49: cite39†License: CC BY 4.0†info.arxiv.org L50: 
L51: arXiv:2603.15059v1 [cs.LG] 16 Mar 2026
L52: # Muon Converges under Heavy-Tailed Noise: Nonconvex Hölder-Smooth Empirical Risk Minimization
L53: 
L54: Hideaki Iiduka iiduka@cs.meiji.ac.jp Affiliation: Department of Computer Science Affiliation: Meiji University Affiliation: 1-1-1 Higashimita, Tama-ku, Kawasaki-shi, Kanagawa 214-8571 Japa
L55: ###### Abstract
L56: Muon is a recently proposed optimizer that enforces orthogonality in parameter updates by projecting gradients onto the Stiefel manifold, leading to stable and efficient training in large-scale deep neural networks. Meanwhile, the previously reported results indicated that stochastic noise in practical machine learning may exhibit heavy-tailed behavior, violating the bounded-variance assumption.
L57: In this paper, we consider the problem of minimizing a nonconvex Hölder-smooth empirical risk that works well with the heavy-tailed stochastic noise. We then show that Muon converges to a stationary point of the empirical risk under the boundedness condition accounting for heavy-tailed stochastic noise. In addition, we show that Muon converges faster than mini-batch SGD.
L58: ^{†}^{†}shortheadings: Muon Converges / Hideaki Iiduka^{†}^{†}firstpage: 1
L59: ###### keywords
L60: 
L61: convergence, heavy-tailed noise, Hölder-smooth, mini-batch SGD, Muon
L62: 
L63: ## 1 Introduction
L64: ### 1.1 Background
L65: 
L66: Empirical risk minimization (ERM) is a central issue in training deep neural networks (DNNs) on certain training datasets. ERM is an optimization problem for minimizing an empirical risk (ER) defined by the sum of loss functions corresponding to the training set. Since a loss function such as the cross entropy loss is nonconvex, we can consider ERM to be a nonconvex minimization problem.
L67: Mini-batch stochastic gradient descent (SGD) (cite40†Robbins and Monro, 1951 ; cite41†Zinkevich, 2003 ; cite42†Nemirovski et al., 2009 ; cite43†Ghadimi and Lan, 2012 ; cite44†Ghadimi and Lan, 2013 ; cite45†Umeda and Iiduka, 2025 ) is a simple and useful optimizer for finding appropriate parameters of the DNN in the sense of minimizing the ER.
L68: A standard assumption when analyzing mini-batch SGD is the smoothness of the ER, i.e., the Lipschitz continuity of the gradient of the ER, since almost all analyses of mini-batch SGD have been based on the descent lemma (see, e.g., (cite46†Beck, 2017 , Lemma 5.7) for the descent lemma).
L69: Mini-batch SGD uses a stochastic gradient of the ER that is randomly chosen from the gradients of loss functions. Hence, a discrepancy arises between the stochastic gradient and the true gradient of the ER. We call such a discrepancy the stochastic noise. It is commonly assumed that the stochastic noise is bounded in the sense of the expectation of the squared norm; i.e., the variance of the stochastic gradient is bounded.
L70: This is because, in theory, the boundedness condition of the variance works well with the descent lemma that is satisfied under the condition of smoothness of the ER.
L71: However, the numerical results in (cite47†Simsekli et al., 2019 ; cite48†Garg et al., 2021 ; cite49†Battash et al., 2024 ; cite50†Ahn et al., 2024 ) indicated that stochastic noise may exhibit heavy-tailed behavior. Heavy-tailed noise refers to stochastic noise whose distribution allows large fluctuations with non-negligible probability due to its slowly decaying tails.
L72: Moreover, it was reported that the stochastic noise of SGD can be heavy-tailed (cite51†Gorbunov et al., 2020 ; cite52†Hodgkinson and Mahoney, 2021 ; cite53†Liu and Zhou, 2025 ). Accordingly, the bounded variance condition of the stochastic gradient would be unrealistic in practical machine-learning problems.
L73: ### 1.2 Motivation
L74: A standard condition (cite54†Zhang et al., 2020 , Assumption 1) to analyze optimizers under heavy-tailed noise is that the stochastic noise is bounded in the sense of the expectation of the $\mathfrak{p}$-th power of the norm, where $\mathfrak{p}\in(1,2]$. In particular, we say that the stochastic noise is heavy-tailed when $\mathfrak{p}\in(1,2)$ (cite54†Zhang et al., 2020 , Assumption 1).
L75: We call the expectation of the $\mathfrak{p}$-th power stochastic noise norm the $\mathfrak{p}$-variance of the stochastic gradient (The precise mathematical formulation of the $\mathfrak{p}$-variance of the stochastic gradient is given in Assumption cite55†2.1 (A2)(ii)).
L76: Under the boundedness of the $\mathfrak{p}$-variance of the stochastic gradient, mini-batch SGD and its variants have been analyzed in (cite54†Zhang et al., 2020 ; cite56†Cutkosky and Mehta, 2021 ; cite57†Nguyen et al., 2023 ; cite58†Sadiev et al., 2023 ; cite59†Liu et al., 2024 ). Meanwhile, cite60†Fatkhullin et al. (2025) and cite61†Yamada et al.
L77: (2026) showed that the Hölder smoothness (cite62†Hölder, 1882 ) that is weaker than the smoothness works well in both theory and practice with the heavy-tailed stochastic noise (The precise mathematical formulation of the Hölder smoothness is given in Assumption cite55†2.1 (A1)). The motivation behind this work is thus to show that, under the Hölder smoothness of the ER and the boundedness of the $\mathfrak{p}$-variance of the stochastic gradient, mini-batch SGD converges.
L78: Many optimizers have been presented to accelerate mini-batch SGD. For example, adaptive gradient methods such as Adam (cite63†Kingma and Ba, 2015 ) and its variant AdamW (cite64†Loshchilov and Hutter, 2019 ) have become the de facto standard in modern deep learning, owing to their fast convergence and strong empirical performance across a wide range of tasks.
L79: Subsequent work has explored richer preconditioning strategies, including methods such as Shampoo (cite65†Gupta et al., 2018 ), which leverage matrix-valued statistics of gradients. More recently, the Muon (Momentum orthogonalized by Newton-Schulz) optimizer (cite66†Jordan et al., 2024 ) has been proposed as a new optimizer that performs updates based on orthogonalized gradients.
L80: Convergence analyses of the Muon optimizer have been presented in (cite67†Tang et al., 2026 ; cite68†Sato et al., 2025 ; cite69†Pethick et al., 2025a ; cite70†Pethick et al., 2025b ; cite71†Nagashima and Iiduka, 2026 ) under the smoothness or $(L_{0},L_{1})$-smoothness of the ER. Meanwhile, we are interested in verifying that, under the Hölder smoothness of the ER and the boundedness of the $\mathfrak{p}$-variance of the stochastic gradient, Muon converges faster than mini-batch SGD.
L81: ### 1.3 Main results
L82: This paper considers the ERM under the Hölder smoothness of the ER and the boundedness of the $\mathfrak{p}$-variance of the stochastic gradient and provides useful properties of mini-batch gradient (Section cite13†2 ). Let $(\bm{W}_{t})\subset\mathbb{R}^{m\times n}$ be the sequence generated by an optimizer with step size $\eta_{t}$ and batch size $b_{t}$ to minimize the ER $f$.
L83: $\nu\in(0,1]$ appears in the definition of the Hölder smoothness (see Assumption cite55†2.1 (A1)), and $\mathfrak{p}\in(1,2]$ appears in the definition of the $\mathfrak{p}$-variance of the stochastic gradient (see Assumption cite55†2.1 (A2)(ii)). The following summarizes convergence of the Muon optimizer when the momentum parameter $\beta$ is $0$ (Section cite22†4 ), compared with mini-batch SGD (Section cite16†3 ). Section cite28†5 shows that Muon with $\beta\neq 0$ has the same results in Section cite22†4 .
L84: #### 1.3.1 Descent property
L85: Let $\eta_{t}$ be a diminishing step size converging to $0$ and let $b_{t}$ be a constant or an increasing batch size. Then, for all $\epsilon>0$, there exists $s_{0}\in\mathbb{N}$ such that, for all $t\geq s_{0}$, $\eta_{t}^{\nu}<\frac{2}{L}$, $O(\eta_{t}^{1+\nu}+\eta_{t}^{1+\nu}b_{t}^{1-\mathfrak{p}})<\epsilon$, and $O(\eta_{t}^{1+\nu}+\eta_{t}b_{t}^{(1-\mathfrak{p})\mathfrak{p}^{-1}})<\epsilon$, where $L>0$ is the Hölder constant (see Lemma cite72†3.1 for the definition) and $O$ is Landau’s symbol.
L86: Mini-batch SGD satisfies the following inequality (Lemma cite72†3.1 (ii)) based on the generalized descent lemma (see (cite73†2 )) under the assumption of Hölder smoothness of the ER: if $1+\nu\leq\mathfrak{p}$ holds, then, for all $t\geq s_{0}$,
L87:  | $\displaystyle\text{[SGD] }\mathbb{E}_{\bm{\xi}_{t}}\left[f(\bm{W}_{t+1})|\bm{\xi}_{[t-1]}\right]$  | $\displaystyle\leq f(\bm{W}_{t})\underbrace{-\eta_{t}\left(1-\frac{L\eta_{t}^{\nu}}{2}\right)\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}^{2}}_{<0}+\underbrace{O\left(\eta_{t}^{1+\nu}+\frac{\eta_{t}^{1+\nu}}{b_{t}^{\mathfrak{p}-1}}\right)}_{\to 0\text{ }(t+\infty)}$  |
L88:  |  | $\displaystyle<f(\bm{W}_{t})+\epsilon,$  |
L89: where $\mathbb{E}_{\bm{\xi}_{t}}[f(\bm{W}_{t+1})|\bm{\xi}_{[t-1]}]$ is the expectation of $f(\bm{W}_{t+1})$ with respect to a random variable $\bm{\xi}_{t}$ conditioned on $\bm{\xi}_{[t-1]}=(\bm{\xi}_{0},\cdots,\bm{\xi}_{t-1})$ and $\|\cdot\|_{\mathrm{F}}$ is the Frobenius norm. Meanwhile, the Muon optimizer satisfies the following inequality (Lemma cite74†4.1 (ii)): for all $t\geq s_{0}$,
L90:  | $\displaystyle\text{[Muon] }\mathbb{E}_{\bm{\xi}_{t}}\left[f(\bm{W}_{t+1})|\bm{\xi}_{[t-1]}\right]$  | $\displaystyle\leq f(\bm{W}_{t})\underbrace{-\eta_{t}\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}}_{<0}+\underbrace{O\left(\eta_{t}^{1+\nu}+\frac{\eta_{t}}{b_{t}^{\frac{\mathfrak{p}-1}{\mathfrak{p}}}}\right)}_{\to 0\text{ }(t\to+\infty)}$  |
L91:  |  | $\displaystyle<f(\bm{W}_{t})+\epsilon.$  |
L92: The above inequalities imply that mini-batch SGD and Muon have a descent property in the sense that $\mathbb{E}_{\bm{\xi}_{t}}[f(\bm{W}_{t+1})|\bm{\xi}_{[t-1]}]<f(\bm{W}_{t})+\epsilon\approx f(\bm{W}_{t})$. The main difference between the above two inequalities is the exponent of $\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}$. This difference between the two optimizers arises from the definition of the search direction.
L93: While the search direction of mini-batch SGD uses the mini-batch gradient (see (cite75†7 ) and $\bm{D}_{t}^{\mathrm{SGD}}$ in (cite76†10 )), the search direction of Muon uses the point on the Stiefel manifold $\mathrm{St}(n,m)\coloneqq\{\bm{O}\in\mathbb{R}^{m\times n}\colon\bm{O}^{\top}\bm{O}=\bm{I}_{n}\}$ closest to the mini-batch gradient (see $\bm{D}_{t}^{\mathrm{Muon}}$ in (cite77†17 ) and (cite78†18 )).
L94: #### 1.3.2 Convergence
L95: 
L96: The above inequalities, together with the super martingale convergence theorem (cite79†Bertsekas et al., 2003 , Proposition 8.2.10), ensure that mini-batch SGD and Muon with $\eta_{t}$ satisfying $\sum_{t=0}^{+\infty}\eta_{t}=+\infty$ satisfy
L97:  | $\displaystyle\begin{cases}\text{[SGD] }\sum_{t=0}^{+\infty}\left(\eta_{t}^{1+\nu}+\frac{\eta_{t}^{1+\nu}}{b_{t}^{\mathfrak{p}-1}}\right)<+\infty\\
L98: \text{[Muon] }\sum_{t=0}^{+\infty}\left(\eta_{t}^{1+\nu}+\frac{\eta_{t}}{b_{t}^{\frac{\mathfrak{p}-1}{\mathfrak{p}}}}\right)<+\infty\end{cases}\Rightarrow\liminf_{t\to+\infty}\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}=0\text{ a.s.},$  |
L99: which, together with the descent properties, implies that mini-batch SGD and Muon converge to a stationary point of $f$ that corresponds to either a local minimizer or a saddle point (Theorems cite80†3.1 and cite81†4.1 ).
L100: #### 1.3.3 Convergence rate
L101: Sections cite10†1.3.1 and cite11†1.3.2 indicate that both mini-batch SGD and Muon converge to appropriate points almost surely. The difference between the two optimizers is reflected in the convergence rate, since the main difference between them in Section cite10†1.3.1 is the exponent of $\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}$.
L102: Under certain assumptions, mini-batch SGD (Theorems cite82†3.2 and cite83†3.3 ) and Muon (Theorems cite84†4.2 and cite85†4.3 ) have the following convergence rate: there exists $s\in\mathbb{N}$ such that, for all $T\geq s$,
L103:  |  | $\displaystyle\text{[SGD] }\frac{1}{\sum_{t=s}^{T}\eta_{t}}\sum_{t=s}^{T}\eta_{t}\mathbb{E}\left[\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}^{2}\right]=\Theta\left(\frac{1}{\sum_{t=s}^{T}\eta_{t}}\right)$  |
L104:  |  | $\displaystyle\text{[Muon] }\frac{1}{\sum_{t=s}^{T}\eta_{t}}\sum_{t=s}^{T}\eta_{t}\mathbb{E}\left[\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}\right]=\Theta\left(\frac{1}{\sum_{t=s}^{T}\eta_{t}}\right),$  |
L105: where $f(T)=\Theta(g(T))$ implies that there exist $c_{1},c_{2}>0$ and $t\in\mathbb{N}$ such that, for all $T\geq t$, $c_{1}g(T)\leq f(T)\leq c_{2}g(T)$. When $\eta_{t}=\frac{1}{(t+1)^{a}}$ ($t\in\{0\}\cup\mathbb{N}$) is used, where $a\in(0,1)$ satisfies $(1+\nu)a>1$ (e.g., $a>\frac{1}{2}$ when $\nu=1$), we have that $\frac{T^{1-a}}{1-a}\leq\sum_{t=1}^{T}\frac{1}{t^{a}}\leq\frac{T^{1-a}}{1-a}+1$, i.e., $\sum_{t=1}^{T}\frac{1}{t^{a}}=\Theta(T^{1-a})$.
L106: Hence, mini-batch SGD has a $\Theta(\frac{1}{T^{1-a}})$ rate of convergence in the sense of the mean of the total expectation of the squared norm $\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}^{2}$, while Muon has a $\Theta(\frac{1}{T^{1-a}})$ rate of convergence in the sense of the mean of the total expectation of the norm $\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}$. In particular, since we have
L107:  | $\displaystyle\min_{t\in\{1,2,\cdots,T\}}\mathbb{E}\left[\|\nabla f(\bm{W}_{t})\|_{\mathrm{F}}\right]=\begin{cases}O\left(\frac{1}{T^{\frac{1-a}{2}}}\right)\text{ }&(\text{SGD})\\
L108: O\left(\frac{1}{T^{1-a}}\right)\text{ }&(\text{Muon}),\end{cases}$  |
L109: 
L110: we can check that Muon converges faster than mini-batch SGD.
L111: ### Notation and definitions
L112: Here, we describe the notation and state some definitions. Let $\mathbb{N}$ be the set of natural numbers. Let $[N]\coloneqq\{1,2,\cdots,N\}$ and $[0:N]\coloneqq\{0,1,\cdots,N\}$ for $N\in\mathbb{N}$. Let $\mathbb{R}_{+}\coloneqq\{x\in\mathbb{R}\colon x\geq 0\}$.
L113: Let $\mathbb{R}^{m\times n}$ be the set of $m\times n$ matrices with inner product $\bm{W}_{1}\bullet\bm{W}_{2}\coloneqq\mathrm{Tr}(\bm{W}_{1}^{\top}\bm{W}_{2})$ ($\bm{W}_{1},\bm{W}_{2}\in\mathbb{R}^{m\times n}$) and the norm $\|\bm{W}\|_{\mathrm{F}}\coloneqq\sqrt{\bm{W}\bullet\bm{W}}$, where $\mathrm{Tr}(\bm{X})$ is the trace of $\bm{X}$.
L114: The dual norm $\|\bm{W}\|_{2,*}$ of the spectral norm $\|\bm{W}\|_{2}\coloneqq\max\{\|\bm{W}\bm{x}\|_{2}\colon\|\bm{x}\|_{2}\leq 1\}$ is defined by $\|\bm{W}\|_{2,*}\coloneqq\max\{\bm{W}\bullet\bm{X}\colon\|\bm{X}\|_{2}\leq 1\}$, where $\|\bm{x}\|_{2}$ is the Euclidean norm of $\bm{x}\in\mathbb{R}^{n}$. $\bm{O}_{m\times n}$ denotes the $m\times n$ zero matrix and $\bm{I}_{n}$ denotes the $n\times n$ identity matrix.
L115: $\mathrm{P}(A)$ denotes the probability of event $A$. $\mathbb{E}_{\xi}[\bm{X}(\xi)]$ denotes the expectation of a random variable $\bm{X}(\xi)$ with respect to a random variable $\xi$. The variance of $\bm{X}(\xi)$ with respect to $\xi$ is defined by $\mathbb{V}_{\xi}[\bm{X}(\xi)]\coloneqq\mathbb{E}_{\xi}[\|\bm{X}(\xi)-\mathbb{E}_{\xi}[\bm{X}(\xi)]\|_{\mathrm{F}}^{2}]$. Let $\mathfrak{p}>1$.
L116: The $\mathfrak{p}$-variance of $\bm{X}(\xi)$ with respect to $\xi$ is defined by $\mathbb{V}_{\xi}^{\mathfrak{p}}[\bm{X}(\xi)]\coloneqq\mathbb{E}_{\xi}[\|\bm{X}(\xi)-\mathbb{E}_{\xi}[\bm{X}(\xi)]\|_{\mathrm{F}}^{\mathfrak{p}}]$. The $2$-variance coincides with the variance (i.e., $\mathbb{V}_{\xi}^{2}[\bm{X}(\xi)]=\mathbb{V}_{\xi}[\bm{X}(\xi)]$). $\mathbb{E}_{\xi}[\bm{X}(\xi)|\bm{Y}]$ (resp. $\mathbb{V}_{\xi}^{\mathfrak{p}}[\bm{X}(\xi)|\bm{Y}]$) denotes the expectation (resp.
L117: the $\mathfrak{p}$-variance) of $\bm{X}(\xi)$ conditioned on $\bm{Y}$. When $\bm{\xi}_{0},\bm{\xi}_{1},\cdots,\bm{\xi}_{t}$ are independent, we define the total expectation $\mathbb{E}$ by $\mathbb{E}\coloneqq\mathbb{E}_{\bm{\xi}_{0}}\mathbb{E}_{\bm{\xi}_{1}}\cdots\mathbb{E}_{\bm{\xi}_{t}}$. We denote $\xi\sim\mathrm{DU}(N)$ when $\xi$ follows a discrete uniform distribution on $[N]$.
L118: The gradient of a differentiable function $f\colon\mathbb{R}^{m\times n}\to\mathbb{R}$ is denoted by $\nabla f\colon\mathbb{R}^{m\times n}\to\mathbb{R}^{m\times n}$.
L119: ## 2 Nonconvex Hölder-Smooth ERM
L120: Let $\bm{W}\in\mathbb{R}^{m\times n}$ be a parameter of a DNN, $S=\{(\bm{x}_{1},\bm{y}_{1}),\ldots,(\bm{x}_{N},\bm{y}_{N})\}$ be the training set, where data point $\bm{x}_{i}$ is associated with label $\bm{y}_{i}$, and $f_{i}(\cdot)\coloneqq f(\cdot;(\bm{x}_{i},\bm{y}_{i}))\colon\mathbb{R}^{m\times n}\to\mathbb{R}$ be the loss function corresponding to the $i$-th labeled training data $(\bm{x}_{i},\bm{y}_{i})$.
L121: Empirical risk minimization (ERM) minimizes the empirical risk (ER) defined for all $\bm{W}\in\mathbb{R}^{m\times n}$ as
L122:  | $\displaystyle f(\bm{W})=\frac{1}{N}\sum_{i=1}^{N}f_{i}(\bm{W}).$  |  | (1)
L123: 
L124: This paper considers the following stationary point problem: Find $\bm{W}^{\star}\in\mathbb{R}^{m\times n}$ such that $\nabla f(\bm{W}^{\star})=\bm{O}_{m\times n}$.
L125: ### 2.1 Assumptions and Examples
L126: 
L127: We assume that the loss functions $f_{i}$ ($i\in[N]$) satisfy the following conditions.
L128: ###### Assumption 2.1.
L129: 
L130: Let $N\in\mathbb{N}$, $\nu\in(0,1]$, $L_{i}=L_{i}(\nu)>0$ ($i\in[N]$), and $\mathfrak{p}\in(1,2]$.
L131: 
L132: (A1) $f_{i}\colon\mathbb{R}^{m\times n}\to\mathbb{R}$ ($i\in[N]$) is $L_{i}$-Hölder smooth, i.e., for all $\bm{W}_{1},\bm{W}_{2}\in\mathbb{R}^{m\times n}$,
L133: 
L134:  | $\displaystyle\|\nabla f_{i}(\bm{W}_{1})-\nabla f_{i}(\bm{W}_{2})\|_{\mathrm{F}}\leq L_{i}\|\bm{W}_{1}-\bm{W}_{2}\|_{\mathrm{F}}^{\nu}$  |
L135: and $f_{i}^{\star}\coloneqq\inf\{f_{i}(\bm{W})\colon\bm{W}\in\mathbb{R}^{m\times n}\}\in\mathbb{R}$.
L136: 
L137: (A2) Let $\xi$ be a random variable that is independent of $\bm{W}\in\mathbb{R}^{m\times n}$. $\nabla f_{\xi}\colon\mathbb{R}^{m\times n}\to\mathbb{R}^{m\times n}$ is the stochastic gradient of $\nabla f$ such that
L138: 
L139:   1. (i)
L140: 
L141: [Unbiasedness of stochastic gradient] for all $\bm{W}\in\mathbb{R}^{m\times n}$, $\mathbb{E}_{\xi}[\nabla f_{\xi}(\bm{W})]=\nabla f(\bm{W})$ and
L142: 
L143:   2. (ii)
L144: [Boundedness of $\mathfrak{p}$-variance of stochastic gradient] there exists $\sigma\geq 0$ such that, for all $\bm{W}\in\mathbb{R}^{m\times n}$, $\mathbb{V}_{\xi}^{\mathfrak{p}}[\nabla f_{\xi}(\bm{W})]\coloneqq\mathbb{E}_{\xi}[\|\nabla f_{\xi}(\bm{W})-\mathbb{E}_{\xi}[\nabla f_{\xi}(\bm{W})]\|^{\mathfrak{p}}]\leq\sigma^{\mathfrak{p}}$.
L145: The $L_{i}$-Hölder smoothness (cite62†Hölder, 1882 ) of $f_{i}$ in Assumption cite55†2.1 (A1) is used to analyze mini-batch SGD (cite60†Fatkhullin et al., 2025 , Assumption 4), (cite61†Yamada et al., 2026 , Assumption 2.1), since almost all of the analyses of mini-batch SGD have been based on the following inequality (cite86†Nesterov, 2015 , (2.5)), (cite87†Yashtini, 2016 , Lemma 1) that is satisfied under $L_{i}$-Hölder smoothness of $f_{i}$: for all $\bm{W}_{1},\bm{W}_{2}\in\mathbb{R}^{m\times n}$,
L146:  | $\displaystyle f_{i}(\bm{W}_{1})\leq f_{i}(\bm{W}_{2})+\nabla f_{i}(\bm{W}_{2})\bullet(\bm{W}_{1}-\bm{W}_{2})+\frac{L_{i}}{1+\nu}\|\bm{W}_{1}-\bm{W}_{2}\|_{\mathrm{F}}^{1+\nu}.$  |  | (2)
L147: Inequality (cite73†2 ) is called the generalized descent lemma, since this is a generalization of the descent lemma (cite46†Beck, 2017 , Lemma 5.7) that is satisfied under $L_{i}$-smoothness of $f_{i}$ (Assumption cite55†2.1 (A1) when $\nu=1$).
--------------------------------------------------------------------------------
More Test-Time Compute Can Hurt: Overestimation Bias in LLM Beam Search (https://arxiv.org/html/2603.15377v1)
citeturn33072view1 [wordlim: 200] Crawled: 4 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2603.15377v1","lineno":null}); Total lines: 401
--------------------------------------------------------------------------------
Massive Redundancy in Gradient TransportEnables Sparse Online Learning (https://arxiv.org/html/2603.15195v1)
citeturn33072view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2603.15195v1","lineno":null}); Total lines: 608
--------------------------------------------------------------------------------
Directional Routing in Transformers (https://arxiv.org/html/2603.14923v1)
citeturn33072view3 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2603.14923v1","lineno":null}); Total lines: 286

