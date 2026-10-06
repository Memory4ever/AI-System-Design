Prior-Informed Zeroth-Order Optimization with Adaptive Direction Alignment for Memory-Efficient LLM Fine-Tuning (https://arxiv.org/html/2601.04710v1)
citeturn26863view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04710v1","lineno":50}); Total lines: 649
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†I Introduction L17:   3. cite7†II Related Work L18:     1. cite8†II-A Memory-Efficient ZO-SGD (MeZO) L19:     2. cite9†II-B Parameter-Efficient Fine-Tuning (PEFT) L20:     3. cite10†II-C Gradient-free Optimization of LLMs L21:   4. cite11†III Our Proposed Method L22:     1. cite12†III-A Memory-efficient ZO with Guiding Vector L23:     2. cite13†III-B Memory-efficient ZO with Greedy Perturbation L24:   5. cite14†IV Theory Analysis L25:     1. cite15†IV-A Per-Step Decrease Analysis with Prior-Informed ZO L26:   6. cite16†V Experiments and Analysis L27:     1. cite17†V-A Medium-sized Language Models L28:     2. cite18†V-B Large Language Models L29:     3. cite19†V-C MeZO with Greedy Strategy L30:     4. cite20†V-D Single Step Analysis for Different Models L31:     5. cite21†V-E Comparison with n-SPSA L32:     6. cite22†V-F Impact of the Number of Evaluations L33:     7. cite23†V-G Memory Usage of Different Methods L34:     8. cite24†V-H Directional Alignment Analysis L35:   7. cite25†VI Conclusion L36:   8. cite26†References L37: cite27†License: CC BY-NC-ND 4.0†info.arxiv.org L38: 
L39: arXiv:2601.04710v1 [cs.CL] 08 Jan 2026
L40: # Prior-Informed Zeroth-Order Optimization with Adaptive Direction Alignment for Memory-Efficient LLM Fine-Tuning
L41: 
L42: Feihu Jin    Shipeng Cen    and Ying Tan ^{†}^{†}thanks: The authors are with the School of Intelligence Science and Technology and the Institute for Artificial Intelligence, Peking University, Beijing 100190, China. Y. Tan is also with the State Key Laboratory of General Artificial Intelligence, Beijing 100190, China (e-mail: fhjin@stu.pku.edu.cn; censhipeng@pku.edu.cn, ytan@pku.edu.cn).
L43: ###### Abstract
L44: Fine-tuning large language models (LLMs) has achieved remarkable success across various NLP tasks, but the substantial memory overhead during backpropagation remains a critical bottleneck, especially as model scales grow. Zeroth-order (ZO) optimization alleviates this issue by estimating gradients through forward passes and Gaussian sampling, avoiding the need for backpropagation.
L45: However, conventional ZO methods suffer from high variance in gradient estimation due to their reliance on random perturbations, leading to slow convergence and suboptimal performance. We propose a simple plug-and-play method that incorporates prior-informed perturbations to refine gradient estimation.
L46: Our method dynamically computes a guiding vector from Gaussian samples, which directs perturbations toward more informative directions, significantly accelerating convergence compared to standard ZO approaches. We further investigate a greedy perturbation strategy to explore the impact of prior knowledge on gradient estimation. Theoretically, we prove that our gradient estimator achieves stronger alignment with the true gradient direction, enhancing optimization efficiency.
L47: Extensive experiments across LLMs of varying scales and architectures demonstrate that our proposed method could seamlessly integrate into existing optimization methods, delivering faster convergence and superior performance. Notably, on the OPT-13B model, our method outperforms traditional ZO optimization across all 11 benchmark tasks and surpasses gradient-based baselines on 9 out of 11 tasks, establishing a robust balance between efficiency and accuracy.
L48: ###### Index Terms:
L49: 
L50: Zeroth-order optimization, large language models, memory-efficient tuning, Black-box optimization.
L51: ## I Introduction
L52: The emergence of fine-tuning techniques for large language models (LLMs) has revolutionized natural language processing (NLP), enabling state-of-the-art performance in tasks such as text generation and question answering [cite28†1 , cite29†2 ]. However, as LLMs scale, the computational and memory demands of full fine-tuning grow exponentially. A key bottleneck arises during backpropagation [cite30†3 ], which requires the storage of intermediate activations and gradients, leading to prohibitive memory overhead.
L53: While parameter-efficient fine-tuning (PEFT) methods [cite31†4 , cite32†5 , cite33†6 ] mitigate this issue by updating only a subset of parameters. Despite these advancements, memory efficiency remains limited: experiments on OPT-13B [cite34†7 ] indicate that full fine-tuning and PEFT still consume 12× and 6× more GPU memory than inference, respectively [cite35†8 ].
L54: Fig. 1: The training loss curves for the WSC, SST-2, and BoolQ tasks are evaluated using the OPT-1.3B model. Our proposed methods (MeZO-Greedy and MeZO-GV) are compatible with MeZO. For full fine-tuning, a learning rate of 2e-7 is employed. All experiments are conducted with a consistent batch size of 16 to ensure uniformity across evaluations.
L55: To address these challenges, zeroth-order optimization has emerged as a promising alternative, replacing backpropagation with gradient estimation via forward passes and Gaussian sampling [cite35†8 ]. By eliminating the need to store intermediate activations, ZO methods drastically reduce memory overhead.
L56: Recent advances focus on improving convergence and reducing gradient variance, such as sparse perturbation strategies [cite36†9 ] and hybrid frameworks that combine ZO with Adam optimization [cite37†10 ] or Hessian-aware estimation [cite38†11 ]. Concurrent work integrates ZO with PEFT techniques [cite39†12 ] to further minimize trainable parameters, advancing scalable and flexible optimization.
L57: Despite these innovations, a fundamental challenge in zeroth-order (ZO) optimization arises from the inherent limitations of conventional gradient estimators, which typically rely on random Gaussian perturbations. Our work explicitly acknowledges that achieving perfect unbiasedness in the estimation of the ZO gradient is theoretically infeasible in practice due to the presence of the finite difference parameter $\epsilon$ and the necessity of approximating expectations over random perturbations.
L58: Motivated by this inherent limitation, we propose to intentionally deviate from the standard Gaussian perturbation scheme by incorporating prior-informed perturbations.
L59: We present the Guiding Vector-Augmented Zeroth-Order (GV-ZO) optimization framework, a novel approach that systematically incorporates prior knowledge to direct the perturbation process. The method employs an adaptive Gaussian sampling mechanism to dynamically estimate a guiding vector, enabling precise alignment of stochastic perturbations with the expected gradient direction - a paradigm we formalize as directional gradient guidance.
L60: Additionally, we develop a prior-informed greedy perturbation strategy that provides both empirical validation and practical implementation of our direction-aware optimization framework.
L61: Theoretically, we demonstrate that our proposed prior-informed perturbation strategies achieve significantly stronger directional alignment with the true gradient compared to conventional ZO methods. This improved alignment ensures that each optimization step contributes more effectively to the convergence dynamics (see Figure cite40†3 ).
L62: Empirical experiments conducted on diverse LLM architectures and scales show that our method not only converges faster (see Figure cite41†1 ) but also yields substantial performance improvements over existing approaches. Notably, despite the additional computations required for learning the guiding vector (GV), the accelerated convergence reduces the total training time compared to baseline methods.
L63: Furthermore, on the OPT-13B model, GV-based approaches consistently achieve state-of-the-art performance across all 11 benchmark tasks, outperforming traditional zeroth-order optimization methods. When compared to gradient-based baselines, GV-based methods exhibit superior results on 9 out of 11 tasks, demonstrating a strong balance between efficiency and accuracy. Moreover, our method employs a plug-and-play design, allowing for seamless integration into a wide range of optimization pipelines.
L64: This makes it a versatile and practical solution for optimizing modern large language models (LLMs), particularly in resource-constrained environments.
L65: ## II Related Work
L66: ### II-A Memory-Efficient ZO-SGD (MeZO)
L67: 
L68: The Simultaneous Perturbation Stochastic Approximation (SPSA) [cite42†13 ] is a zeroth-order optimization method used to approximate the gradient of scalar-valued functions $f(\bm{x})$ where $\bm{x}\in\mathbb{R}^{d}$. The SPSA gradient estimate employs finite differences along random Gaussian directions:
L69: 
L70:  | $$\hat{\nabla}f(\bm{x})=\frac{1}{q}\sum_{i=1}^{q}\left(\frac{f(\bm{x}+\mu\bm{u}_{i})-f(\bm{x}-\mu\bm{u}_{i})}{2\mu}\right)\bm{u}_{i},$$  |  | (1)
L71: where $q$ represents the number of function evaluations, $\mu>0$ denotes the perturbation step size, and $\bm{u}_{i}\sim\mathcal{N}(\bm{0},\bm{I})$ are random direction vectors. As $\mu\to 0$, the finite difference converges to the directional derivative $f^{\prime}(\bm{x},\bm{u})=\bm{u}^{\top}\nabla f(\bm{x})$. This results in an unbiased gradient estimator:
L72: 
L73:  | $$\mathbb{E}_{\bm{u}}[f^{\prime}(\bm{x},\bm{u})\bm{u}]=\mathbb{E}_{\bm{u}}[\bm{u}\bm{u}^{\top}\nabla f(\bm{x})]=\nabla f(\bm{x}),$$  |  | (2)
L74: making SPSA particularly effective for high-dimensional optimization tasks, such as fine-tuning LLMs.
L75: 
L76: Given a labeled dataset $\mathcal{D}=\{(\bm{x}_{i},y_{i})\}_{i=1}^{|\mathcal{D}|}$, minibatch $\mathcal{B}\subset\mathcal{D}$, and a loss function $\mathcal{L}(\bm{\theta};\mathcal{B})$ with parameters $\bm{\theta}\in\mathbb{R}^{d}$, the SPSA gradient estimate is expressed as follows:
L77:  | $$\hat{\nabla}\mathcal{L}(\bm{\theta};\mathcal{B})=\frac{\mathcal{L}(\bm{\theta}+\epsilon\bm{z};\mathcal{B})-\mathcal{L}(\bm{\theta}-\epsilon\bm{z};\mathcal{B})}{2\epsilon}\bm{z},$$  |  | (3)
L78: where $\bm{z}\sim\mathcal{N}(\bm{0},\bm{I})$ represents a random perturbation vector, and $\epsilon>0$ denotes the perturbation scale. The estimator $\hat{\nabla}\mathcal{L}(\bm{\theta};\mathcal{B})\approx\bm{z}\bm{z}^{\top}\nabla\mathcal{L}(\bm{\theta};\mathcal{B})$ requires only two forward passes, facilitating memory-efficient optimization. This serves as the foundation for Zeroth-Order Stochastic Gradient Descent (ZO-SGD):
L79:  | $$\bm{\theta}_{t+1}=\bm{\theta}_{t}-\eta\hat{\nabla}\mathcal{L}(\bm{\theta};\mathcal{B}_{t}),$$  |  | (4)
L80: 
L81: where $\mathcal{B}_{t}$ represents the $t$-th minibatch and $\eta$ denotes the learning rate, ZO-SGD mitigates the memory overhead associated with backpropagation by substituting exact gradients with SPSA estimates.
L82: ### II-B Parameter-Efficient Fine-Tuning (PEFT)
L83: 
L84: We consider two PEFT methods, including {LoRA, prefix tuning}.
L85: 
L86: 1) Low-Rank Adaptation (LoRA) LoRA modifies a pre-trained model by introducing trainable low-rank matrices, enabling fine-tuning with a limited parameters. Given a weight matrix $W\in\mathbb{R}^{m\times n}$ in a transformer model, LoRA decomposes it as:
L87: 
L88:  | $$W^{\prime}=W+BA\quad$$  |
L89: where $W$ is the original weight matrix, $B\in\mathbb{R}^{m\times r}$ and $A\in\mathbb{R}^{r\times n}$ are the low-rank matrices, and $r\ll\min(m,n)$ represents the rank. During fine-tuning, only $B$ and $A$ are updated, keeping $W$ frozen.
L90: 
L91: 2) Prefix Tuning Prefix tuning adds context vectors to the attention mechanism of transformer models. Given an input sequence $x$, the model processes it with additional context vectors $C_{k}$ and $C_{v}$ serving as keys and values in the attention mechanism:
L92:  | $$\text{Attention}(Q,K,V)=\text{softmax}\left(\frac{Q(K+C_{k})^{T}}{\sqrt{d_{k}}}\right)(V+C_{v})$$  |
L93: 
L94: where $Q$, $K$, and $V$ represent the query, key, and value matrices in the attention mechanism, $C_{k}\in\mathbb{R}^{l\times d_{k}}$, $C_{v}\in\mathbb{R}^{l\times d_{v}}$, and $l$ is the length of the prefix. During training, only $C_{k}$ and $C_{v}$ are updated, and the original model parameters are frozen.
L95: ### II-C Gradient-free Optimization of LLMs
L96: Recent advancements in gradient-free optimization have utilized evolutionary algorithms, particularly the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) [cite43†30 ], to optimize continuous prompt vectors in black-box tuning methods. This approach has demonstrated significant advantages for applying large language models by reducing complexity. However, training these prompt vectors has exhibited instability and slow convergence rates [cite44†31 , cite45†32 ].
L97: To address these issues, [cite46†33 ] proposed a gradient-free optimization framework for low-rank adaptation to stabilize training and improve convergence speed.
L98: Zeroth-order optimization (ZO) has emerged as a pivotal gradient-free method in machine learning, particularly in scenarios where gradient computation is infeasible or prohibitively expensive [cite47†34 , cite48†35 , cite49†36 ]. ZO has also inspired the development of distributed optimization techniques [cite50†37 ] and has been effectively applied to black-box adversarial example generation in deep learning [cite51†38 , cite52†39 ].
L99: In addition, several ZO methods have been proposed that achieve optimization without explicitly estimating gradients [cite53†40 , cite54†41 , cite55†42 ]. Recently, the application of ZO optimization to fine-tuning LLMs has demonstrated significant reductions in GPU utilization and memory footprint [cite35†8 , cite56†43 , cite57†44 ]. These advancements have catalyzed a growing body of research on zeroth-order optimization techniques tailored for LLMs.
L100: Recent advancements in ZO optimization have primarily focused on enhancing convergence rates and minimizing gradient estimation variance to optimize fine-tuning of LLMs. Increasing the batch size has effectively reduced noise in ZO gradient estimation [cite56†43 , cite58†45 ]. Sparse perturbation strategies improve efficiency by selectively perturbing a subset of parameters, thereby reducing computational overhead and gradient variance [cite36†9 , cite37†10 ].
L101: These strategies achieve sparse parameter perturbations through techniques such as random and sparse pruning masks or block-coordinate perturbations. Notably, [cite58†45 ] extended zero-order optimization to the Adam algorithm, while [cite38†11 ] enhanced model inference performance by incorporating Hessian matrix-based gradient estimation in ZO optimization, albeit at the expense of increased memory consumption.
L102: Additionally, innovative approaches have been proposed to reduce the number of trainable parameters, such as mapping models to subspaces and employing PEFT methods [cite31†4 , cite33†6 ] alongside tensorized adapters [cite39†12 ].
L103: ## III Our Proposed Method
L104: The proposed method is a plug-and-play strategy designed for seamless integration into any zeroth-order optimization algorithm that employs stochastic perturbation for gradient estimation. The guiding vector mechanism and the greedy perturbation strategy are intentionally architecture-agnostic, ensuring broad compatibility with various optimization frameworks.
L105: This inherent flexibility allows the proposed method to be easily adapted to diverse optimization techniques without necessitating significant modifications to the underlying process. To rigorously demonstrate the effectiveness and generality of our approach, we have integrated the proposed mechanisms into two prominent zeroth-order optimization algorithms: MeZO [cite35†8 ] and SubZero [cite59†14 ]. We conduct comprehensive experiments to evaluate the performance across a range of models and tasks.
L106: ### III-A Memory-efficient ZO with Guiding Vector
L107: In this work, we propose Memory-Efficient Zeroth-Order Optimization with Guiding Vectors (MeZO-GV), an advanced zeroth-order optimization algorithm designed to efficiently optimize high-dimensional parameters $\theta\in\mathbb{R}^{d}$ in scenarios where gradient computations are either infeasible or computationally expensive. The algorithm builds upon the traditional MeZO framework by introducing a guiding vector $\bm{v}$ that directs parameter updates toward more promising regions of the loss landscape.
L108: This guiding vector is computed using a perturbation-based exploration strategy, which significantly enhances convergence speed and optimization performance compared to standard zeroth-order methods.
L109: The MeZO-GV algorithm iteratively updates the model parameters $\theta$ over a fixed step budget $T$. At each iteration $t$, MeZO-GV begins by sampling a minibatch $\mathcal{B}_{t}$ from the dataset $\mathcal{D}$ and generating a random seed $s$ to ensure in-place operation.
L110: The guiding vector $\bm{v}$ is derived from a set of $M$ perturbations $\{\bm{z}_{i}\}_{i=1}^{M}$, where each $\bm{z}_{i}\sim\mathcal{N}(\bm{0},\bm{I})$ is a random perturbation vector generated using a unique seed $s_{i}=\text{Hash}(s\oplus i)$. The perturbations are evaluated on the loss function $\mathcal{L}$, and the top $\alpha M$ perturbations with the lowest losses are selected as the elite group $\mathcal{O}_{\text{top}}$, while the remaining form the non-elite group $\mathcal{O}_{\text{bottom}}$.
L111: The guiding vector $\bm{v}$ is computed as:
L112:  | $$\bm{v}=\frac{1}{|\mathcal{O}_{\text{top}}|}\sum_{\bm{z}_{i}\in\mathcal{O}_{\text{top}}}\bm{z}_{i}-\frac{1}{|\mathcal{O}_{\text{bottom}}|}\sum_{\bm{z}_{i}\in\mathcal{O}_{\text{bottom}}}\bm{z}_{i},$$  |  | (5)
L113: 
L114: Using the guiding vector $\bm{v}$, MeZO-GV estimates the directional gradient $\hat{\nabla}\mathcal{L}(\bm{\theta};\mathcal{B})$ via:
L115:  | $$\hat{\nabla}\mathcal{L}(\bm{\theta};\mathcal{B})=\frac{\mathcal{L}(\bm{\theta}+\epsilon\bm{v};\mathcal{B})-\mathcal{L}(\bm{\theta}-\epsilon\bm{v};\mathcal{B})}{2\epsilon}\bm{v},$$  |  | (6)
L116: where $\epsilon>0$ is the perturbation scale, this estimator approximates the gradient as $\hat{\nabla}\mathcal{L}(\bm{\theta};\mathcal{B})\approx\bm{v}\bm{v}^{\top}\nabla\mathcal{L}(\bm{\theta};\mathcal{B})$. This approach requires only two forward passes and eliminates the need for backpropagation, thereby facilitating memory-efficient optimization. The parameters $\bm{\theta}$ are updated according to Equation cite60†4 .
L117: By leveraging the guiding vector $\bm{v}$, MeZO-GV allows the algorithm to concentrate on the most promising directions for parameter updates, resulting in faster convergence and improved optimization performance. We present the overall pipeline in Algorithm cite61†1 and cite62†2 .
L118: Algorithm 1 MeZO with Guiding Vector
L119: 
L120: 0:  Parameters $\theta\in\mathbb{R}^{d}$, loss function $\mathcal{L}(\theta;\mathcal{B})$, step budget $T$, perturbation scale $\epsilon$, batch size $\mathcal{B}$, learning rate $\eta$, weight decay $\lambda$, fireworks size $M$, split ratio $\alpha\in(0,1)$
L121: 
L122: 1:  for iteration $t=1$ to $T$ do
L123: 
L124: 2:   Sample minibatch $\mathcal{B}_{t}\sim\mathcal{D}$ and random seed $s$
L125: 3:   Compute guiding vector: $v\leftarrow\textsc{ComputeGuidingVector}(\theta,M,\alpha,s,\mathcal{B})$
L126: 
L127: 4:   GuidingPerturbation($\theta$, $+\epsilon$, $v$)
L128: 
L129: 5:   Evaluate $\mathcal{L}^{+}\leftarrow\mathcal{L}(\theta;\mathcal{B}_{t})$
L130: 
L131: 6:   GuidingPerturbation($\theta$, $-2\epsilon$, $v$)
L132: 
L133: 7:   Evaluate $\mathcal{L}^{-}\leftarrow\mathcal{L}(\theta;\mathcal{B}_{t})$
L134: 
L135: 8:   GuidingPerturbation($\theta$, $+\epsilon$, $v$)
L136: 9:   Estimate directional gradient: $g\leftarrow(\mathcal{L}^{+}-\mathcal{L}^{-})/(2\epsilon)$
L137: 
L138: 10:   Update parameters: $\theta\leftarrow\theta-\eta\cdot(g\cdot v)$
L139: 
L140: 11:  end for
L141: 
L142: Algorithm 2 Subroutines for MeZO with Guiding Vector
L143: 
L144: 1:  Subroutine: ComputeGuidingVector($\theta$, $M$, $\alpha$, $s$, $\mathcal{B}$)
L145: 
L146: 2:  Initialize perturbation set $\mathcal{O}\leftarrow\emptyset$
L147: 
L148: 3:  for particle $i=1$ to $M$ do
L149: 
L150: 4:   Generate unique seed $s_{i}\leftarrow\text{Hash}(s\oplus i)$
L151: 5:   RandomPerturbation($\theta$, $\epsilon$, $s_{i}$)
L152: 
L153: 6:   Evaluate fitness $l_{i}\leftarrow\mathcal{L}(\theta;\mathcal{B})$
L154: 
L155: 7:   RandomPerturbation($\theta$, $-\epsilon$, $s_{i}$)
L156: 
L157: 8:   Store perturbation seed $s_{i}$
L158: 
L159: 9:   $\mathcal{O}\leftarrow\mathcal{O}\cup\{(l_{i},s_{i})\}$
L160: 
L161: 10:  end for
L162: 
L163: 11:  Sort $\mathcal{O}$ by ascending $l_{i}$ values
L164: 
L165: 12:  Split into elite/non-elite groups:
L166: 
L167: 13:   $\mathcal{O}_{\text{top}}\leftarrow\text{First}(\lfloor\alpha M\rfloor,\mathcal{O})$
L168: 14:   $\mathcal{O}_{\text{bottom}}\leftarrow\text{Last}(M-\lfloor\alpha M\rfloor,\mathcal{O})$
L169: 
L170: 15:  Compute guide vector through the $z_{i}$ corresponding to the seed $s_{i}$ :
L171: 
L172: 16:   $v_{\text{top}}\leftarrow\frac{1}{|\mathcal{O}_{\text{top}}|}\sum_{(l_{i},s_{i})\in\mathcal{O}_{\text{top}}}z_{i}$
L173: 
L174: 17:   $v_{\text{bottom}}\leftarrow\frac{1}{|\mathcal{O}_{\text{bottom}}|}\sum_{(l_{i},s_{i})\in\mathcal{O}_{\text{bottom}}}z_{i}$
L175: 
L176: 18:  $v\leftarrow v_{\text{top}}-v_{\text{bottom}}$
L177: 
L178: 19:  Return $v$
L179: 
L180: 20:
L181: 21:  Subroutine: GuidingPerturbation($\theta$, $\epsilon$, $v$)
L182: 
L183: 22:  for each parameter $\theta_{j}\in\theta$ do
L184: 
L185: 23:   $\theta\leftarrow\theta+\epsilon\cdot v$
L186: 
L187: 24:  end for
L188: 
L189: 25:
L190: 
L191: 26:  Subroutine: RandomPerturbation($\theta$, $\epsilon$, $s$)
L192: 
L193: 27:  Reset random number generator with seed $s$
L194: 
L195: 28:  for each parameter $\theta_{j}\in\theta$ do
L196: 
L197: 29:   $z_{j}\sim\mathcal{N}(0,1)$
L198: 
L199: 30:   $\theta_{j}\leftarrow\theta_{j}+\epsilon\cdot z_{j}$
L200: 
L201: 31:  end for
L202: ### III-B Memory-efficient ZO with Greedy Perturbation
L203: In addition to the guiding vector mechanism, we propose another Memory-efficient ZO with Greedy Perturbation (MeZO-Greedy) strategy as a complementary optimization component to further enhance the performance of the optimization process. MeZO-Greedy functions as an independent mechanism that actively explores the most promising update directions at each iteration.
L204: Specifically, the algorithm generates a set of $M$ candidate perturbations $\{\bm{z}_{i}\}_{i=1}^{M}$, where each $\bm{z}_{i}$ is sampled from a predefined distribution. The greedy selection process then identifies the optimal perturbation $\bm{z}^{*}$ that minimizes the loss function in the vicinity of the current parameters:
L205:  | $$\bm{z}^{*}=\text{arg min}_{\bm{z}_{i}}\mathcal{L}(\bm{\theta}+\epsilon\bm{z}_{i};\mathcal{B}),$$  |  | (7)
L206: 
L207: where $\epsilon$ controls the exploration radius, and $\mathcal{B}$ represents the current mini-batch of data, the selected perturbation $\bm{z}^{*}$ encapsulates the most favorable direction for parameter updates based on immediate feedback from the loss landscape, effectively capturing the local geometry of the optimization surface.
L208: Building upon this selected direction, we calculate an independent gradient estimate using a symmetric difference approximation:
L209: 
L210:  | $$\hat{\nabla}^{*}\mathcal{L}(\bm{\theta};\mathcal{B})=\frac{\mathcal{L}(\bm{\theta}+\epsilon\bm{z}^{*};\mathcal{B})-\mathcal{L}(\bm{\theta}-\epsilon\bm{z}^{*};\mathcal{B})}{2\epsilon}\bm{z}^{*},$$  |  | (8)
L211: 
L212: Then the parameters $\bm{\theta}$ are updated using the Equation cite60†4 . The complete algorithmic implementation is presented in Algorithm cite63†3 and cite64†4 .
L213: Algorithm 3 MeZO with Greedy Strategy
L214: 
L215: 0:  Parameters $\theta\in\mathbb{R}^{d}$, loss function $\mathcal{L}(\theta;\mathcal{B})$, step budget $T$, perturbation scale $\epsilon$, batch size $\mathcal{B}$, learning rate $\eta$, weight decay $\lambda$, candidate perturbations $M$
L216: 
L217: 1:  for iteration $t=1$ to $T$ do
L218: 
L219: 2:   Sample minibatch $\mathcal{B}_{t}\sim\mathcal{D}$ and random seed $s$
L220: 3:   Compute optimal perturbation: $z^{*}\leftarrow\textsc{ComputeGreedyPerturbation}(\theta,M,\epsilon,s,\mathcal{B}_{t})$
L221: 
L222: 4:   GreedyPerturbation($\theta$, $+\epsilon$, $z^{*}$)
L223: 
L224: 5:   Evaluate $\mathcal{L}^{+}\leftarrow\mathcal{L}(\theta;\mathcal{B}_{t})$
L225: 
L226: 6:   GreedyPerturbation($\theta$, $-2\epsilon$, $z^{*}$)
L227: 
L228: 7:   Evaluate $\mathcal{L}^{-}\leftarrow\mathcal{L}(\theta;\mathcal{B}_{t})$
L229: 
L230: 8:   GreedyPerturbation($\theta$, $+\epsilon$, $z^{*}$)
L231: 9:   Estimate directional gradient: $g\leftarrow(\mathcal{L}^{+}-\mathcal{L}^{-})/(2\epsilon)$
L232: 
L233: 10:   Update parameters: $\theta\leftarrow\theta-\eta\cdot(g\cdot z^{*})$
L234: 
L235: 11:  end for
L236: 
L237: Algorithm 4 Subroutines for MeZO with Greedy Strategy
L238: 
L239: 1:  Subroutine: ComputeGreedyPerturbation($\theta$, $M$, $\epsilon$, $s$, $\mathcal{B}$)
L240: 
L241: 2:  Initialize perturbation set $\mathcal{O}\leftarrow\emptyset$
L242: 
L243: 3:  for particle $i=1$ to $M$ do
L244: 
L245: 4:   Generate unique seed $s_{i}\leftarrow\text{Hash}(s\oplus i)$
L246: 5:   RandomPerturbation($\theta$, $\epsilon$, $s_{i}$)
L247: 
L248: 6:   Evaluate fitness $l_{i}\leftarrow\mathcal{L}(\theta;\mathcal{B})$
L249: 
L250: 7:   RandomPerturbation($\theta$, $-\epsilon$, $s_{i}$)
L251: 
L252: 8:   Store perturbation $z_{i}$ and loss $l_{i}$
L253: 
L254: 9:   $\mathcal{O}\leftarrow\mathcal{O}\cup\{(l_{i},z_{i})\}$
L255: 
L256: 10:  end for
L257: 
L258: 11:  Find the optimal perturbation:
L259: 
L260: 12:   $z^{*}\leftarrow\text{arg min}_{(l_{i},z_{i})\in\mathcal{O}}l_{i}$
L261: 
L262: 13:  Return $z^{*}$
L263: 
L264: 14:
L265: 15:  Subroutine: GreedyPerturbation($\theta$, $\epsilon$, $z^{*}$)
L266: 
L267: 16:  for each parameter $\theta_{j}\in\theta$ do
L268: 
L269: 17:   $\theta_{j}\leftarrow\theta_{j}+\epsilon\cdot z^{*}_{j}$
L270: 
L271: 18:  end for
L272: 
L273: 19:
L274: 
L275: 20:  Subroutine: RandomPerturbation($\theta$, $\epsilon$, $s$)
L276: 
L277: 21:  Reset random number generator with seed $s$
L278: 
L279: 22:  for each parameter $\theta_{j}\in\theta$ do
L280: 
L281: 23:   $z_{j}\sim\mathcal{N}(0,1)$
L282: 
L283: 24:   $\theta_{j}\leftarrow\theta_{j}+\epsilon\cdot z_{j}$
L284: 
L285: 25:  end for
L286: ## IV Theory Analysis
L287: 
L288: ### IV-A Per-Step Decrease Analysis with Prior-Informed ZO
L289: 
L290: To investigate the approximation efficiency of the expectation in Equation cite65†3 , we first present the following lemma.
L291: ###### Lemma 1.
L292: 

