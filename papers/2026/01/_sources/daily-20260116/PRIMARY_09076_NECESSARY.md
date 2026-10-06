# Exact-v1 minimum primary: 2601.09076

Source: https://arxiv.org/html/2601.09076v1 . Only selected necessary method/evaluation/counterevidence; full fetched body is not a whole-paper review.

## Raw body offsets 15866–27050

III-B Zeroth-Order Gradient Estimator
Unlike prior methods [38, 16, 39] that rely on full forward and backward passes through the client and its auxiliary network to compute first-order gradients ∇ℓ​(𝜽l,ξi)\nabla\ell(\bm{\theta}_{l};\xi_{i}), we adopt a mini-batch-type ZO gradient estimator with two-point evaluation. Specifically, for function fl,if_{l,i}, the two-point type stochastic ZO gradient estimator is defined as:
∇^​fl,i​(𝜽l,ξi)=1B​∑j=1Bd​𝒖μ​[ℓl,i​(𝜽l+μ​𝒖,ξi,j)−ℓl,i​(𝜽l,ξi,j)],\displaystyle\widehat{\nabla}f_{l,i}(\bm{\theta}_{l};\xi_{i})=\frac{1}{B}\sum\nolimits_{j=1}^{B}\frac{d\bm{u}}{\mu}[\ell_{l,i}(\bm{\theta}_{l}+\mu\bm{u};\xi_{i,j})-\ell_{l,i}(\bm{\theta}_{l};\xi_{i,j})],
(2)
where 𝒖\bm{u} is a random vector drawn from either a Gaussian or a Uniform ball distribution, μ\mu is a positive perturbation step size.
This estimator approximates the smoothed objective function’s gradient. Formally, it can be shown that this estimator is an unbiased estimate of ∇fl,iμ​(𝜽l)\nabla f_{l,i}^{\mu}(\bm{\theta}_{l}), where fl,iμf_{l,i}^{\mu} is the Gaussian-smoothed surrogate of the original function fl,if_{l,i}.
This estimator approximates the gradient of a smoothed surrogate objective, which is defined below.
Definition 1 (Gaussian Smoothed Function with Unit-Sphere Normalization).
A function f:ℝd→ℝf:\mathbb{R}^{d}\to\mathbb{R} is said to be spherically smoothed with radius μ>0\mu>0 if
fμ​(𝒙)=𝔼𝒛∼𝒩⁡(0,Id)​[f⁡(𝒙+μ​𝒛‖𝒛‖)],f^{\mu}(\bm{x})=\mathbb{E}_{\bm{z}\sim\mathcal{N}(0,I_{d})}\!\big[f\!\big(\bm{x}+\mu\,\frac{\bm{z}}{\|\bm{z}\|}\big)\big],
(3)
where 𝐮:=𝐳/‖𝐳‖\bm{u}:=\bm{z}/\|\bm{z}\| satisfies ‖𝐮‖=1\|\bm{u}\|=1 almost surely and
𝐮∼Unif⁡(𝕊d−1)\bm{u}\sim\mathrm{Unif}(\mathbb{S}^{d-1}).
We recall a standard result on Gaussian smoothing [41]:
if ff is LL-smooth, then fμf^{\mu} is continuously differentiable with Lμ≤LL_{\mu}\leq L, and
∇fμ​(𝒙)=𝔼𝒖​[f⁡(𝒙+μ​𝒖)−f⁡(𝒙)μ​𝒖].\nabla f^{\mu}(\bm{x})=\mathbb{E}_{\bm{u}}\!\left[\frac{f(\bm{x}+\mu\bm{u})-f(\bm{x})}{\mu}\bm{u}\right].
(4)
Consequently, the two-point zeroth-order estimator in (2) is an unbiased estimator of the gradient
of the smoothed objective:
𝔼𝒖​[∇^​fl,i​(𝜽l,ξi)]=∇fl,iμ​(𝜽l,ξi).\mathbb{E}_{\bm{u}}\!\big[\widehat{\nabla}f_{l,i}(\bm{\theta}_{l};\xi_{i})\big]=\nabla f_{l,i}^{\mu}(\bm{\theta}_{l};\xi_{i}).
(5)
The bias with respect to ∇fl,i\nabla f_{l,i} is solely due to smoothing and is controlled by μ\mu.
IV Proposed Algorithm: HERON-SFL
Fig. 1: The proposed HERON-SFL algorithm. 
We present the end-to-end training process of our proposed framework, which operates over a series of communication rounds with synchronized aggregation (high-level illustration depicted in Fig. 1).
Each round, indexed by tt, encompasses four key stages: model initialization, local client computation, server-side updates, and local model aggregation in Fed-Server.
The entire process is formalized as follows:
1. Model Initialization.
At the start of the tt-th communication round, the Fed-Server broadcasts the global model parameters 𝜽ct{\bm{\theta}}_{c}^{t} and 𝜽at{\bm{\theta}}_{a}^{t} that are resulted from the federated aggregation at the end of the last round. Upon receiving these parameters, each client ii initializes its local models for the subsequent update process: 𝜽l,it,0={𝜽c,it,0,𝜽a,it,0}={𝜽ct,𝜽at}\bm{\theta}_{l,i}^{t,0}=\{\bm{\theta}_{c,i}^{t,0},\bm{\theta}_{a,i}^{t,0}\}=\{{\bm{\theta}}_{c}^{t},{\bm{\theta}}_{a}^{t}\}.
2. Local Model Update and Smashed Data Upload.
The client then proceeds with hh local model updates. During this process, the update of the client-side model is decoupled from the server-side model by leveraging an auxiliary network.
Distinct from existing methods, our paradigm employs a ZO gradient estimator (defined in Eq. (2)) to approximate the gradients of a local loss function. This allows the client to perform timely updates without requiring traditional back-propagation from the server.
After performing hh local gradient descent steps, the cumulative update for the client-side models can be concisely written as:
𝜽l,it,h=𝜽l,it,0−ηl​∑m=1h∇^​fl,i​(𝜽l,it,m,ξi).\bm{\theta}_{l,i}^{t,h}=\bm{\theta}_{l,i}^{t,0}-\eta_{l}\sum\nolimits_{m=1}^{h}\widehat{\nabla}f_{l,i}(\bm{\theta}_{l,i}^{t,m};\xi_{i}).
(6)
During the local update phase, the client uploads its smashed data to the server every kk local steps for the subsequent server-side training phase.
3. Server Model Update.
The server receives the smashed data from each client ii and performs model updates sequentially using an SFLV2 [50] training scheme. In this setting, each client’s smashed data is processed one-by-one, and standard first-order optimization based on forward and backward propagation is used to estimate gradients and update the server-side model parameters 𝜽st\bm{\theta}_{s}^{t} accordingly:
𝜽st+1=𝜽st−ηs​∑i=1N1|𝒟i|​∑ξi∈𝒟i∇ℓ​(𝜽st,𝜽c,it​(ξi)),\bm{\theta}_{s}^{t+1}=\bm{\theta}_{s}^{t}-\eta_{s}\sum\nolimits_{i=1}^{N}\frac{1}{|\mathcal{D}_{i}|}\sum\nolimits_{\xi_{i}\in\mathcal{D}_{i}}\nabla\ell(\bm{\theta}_{s}^{t};{\bm{\theta}_{c,i}^{t}}(\xi_{i})),
(7)
where ∇𝜽sl​(𝜽st,𝜽c,it​(ξi))\nabla_{\bm{\theta}_{s}}\mathit{l}(\bm{\theta}_{s}^{t};{\bm{\theta}_{c,{i}}^{t}}(\xi_{i})) is the real gradient of the server-side loss function using back propagation.
4. Model Aggregation in Fed-Server.
Upon completion of the hh local updates, each client transmits its updated local parameters 𝜽l,it,h\bm{\theta}_{l,i}^{t,h} to the Fed-Server for aggregation. The Fed-Server averages these parameters across all NN clients to compute the global model combined by client-side and auxiliary models for the next round:
𝜽lt+1=𝜽¯lt=1N​∑i=1N𝜽l,it,h\bm{\theta}_{l}^{t+1}=\bar{\bm{\theta}}_{l}^{t}=\frac{1}{N}\sum\nolimits_{i=1}^{N}\bm{\theta}_{l,i}^{t,h}
(8)
The server-side model, 𝜽st+1\bm{\theta}_{s}^{t+1}, which was updated sequentially during the round, is already finalized and requires no aggregation. Finally, the new global model 𝜽gt+1={𝜽ct+1,𝜽st+1}\bm{\theta}_{g}^{t+1}=\{\bm{\theta}_{c}^{t+1},\bm{\theta}_{s}^{t+1}\} is assembled and prepared for distribution in the subsequent communication round.
In essence, HERON-SFL uses a client-side ZO gradient estimator to eliminate backpropagation/activation caching while keeping the same smashed-activation upload schedule as standard decoupled SFL, and thus incurs no additional communication overhead beyond the auxiliary-network-based SFL protocol(e.g., CSE-FSL[38] and FSL-SAGE[39]).
V Theoretical Analysis
V-A Convergence Analysis
In this section, we provide a formal convergence analysis to establish the theoretical guarantees for the proposed FSL-HERON framework. The theoretical framework is built upon the following standard assumptions, which are widely adopted in the analysis of distributed optimization algorithms [21, 47, 38, 10].
Assumption 1 (L-smoothness).
The loss functions of clients and server are LL-smooth. Mathematically, for any 𝐱∈ℝd\bm{x}\in\mathbb{R}^{d} and 𝐲∈ℝd\bm{y}\in\mathbb{R}^{d}, the following holds:
∥∇f(𝒙)−∇f(𝒚)∥≤L∥𝒙−𝒚∥,f(𝒚)≤f(𝒙)+∇f(𝒙)T(𝒚−𝒙)+L2∥𝒚−𝒙∥2,\displaystyle\|\nabla f(\bm{x})-\nabla f(\bm{y})\|\leq L\|\bm{x}-\bm{y}\|,\quad f(\bm{y})\leq f(\bm{x})+\nabla f(\bm{x})^{T}(\bm{y}-\bm{x})+\frac{L}{2}\|\bm{y}-\bm{x}\|^{2},
(9)
where ff is the loss function, and LL is the Lipschitz constant.
Assumption 2 (Bounded gradients).
The gradients of the local loss function ℓi​(𝛉c,𝛉s)\ell_{i}(\bm{\theta}_{c},\bm{\theta}_{s}) are bounded, i.e., there exists a constant GG such that:
‖∇𝜽cℓi​(𝜽c)‖2≤Gc2,‖∇𝜽sℓi​(𝜽s)‖2≤Gs2.\|\nabla_{\bm{\theta}_{c}}\ell_{i}(\bm{\theta}_{c})\|^{2}\leq G_{c}^{2},\|\nabla_{\bm{\theta}_{s}}\ell_{i}(\bm{\theta}_{s})\|^{2}\leq G_{s}^{2}.
(10)
Assumption 3 (Bounded variance for ZO estimator).
The variance of the zeroth-order gradient estimator is bounded, i.e., there exists a constant σ2\sigma^{2} such that:
𝔼⁡[‖𝒈^c,it,m−∇𝜽cfi​(𝜽c,𝜽s)‖2]≤σ2.\mathbb{E}[\|\widehat{\bm{g}}_{c,i}^{t,m}-\nabla_{\bm{\theta}_{c}}f_{i}(\bm{\theta}_{c},\bm{\theta}_{s})\|^{2}]\leq\sigma^{2}.
(11)
Assumption 4 (Uniformly bounded drift of client sub-model).
For each client ii at global round tt, let zc,it=gxc,it,h​(z)z_{c,i}^{t}=g_{x_{c,i}^{t},h}(z) be the output of the ii-th client-side model (with input determined by xc,itx_{c,i}^{t} and 𝒟i\mathcal{D}_{i}), and denote by Pc,it​(z)P_{c,i}^{t}(z) its output distribution. Let Pc,i∗​(z)P^{\ast}_{c,i}(z) be the reference (time-invariant) output distribution of the ii-th client-side model evaluated at xc∗x_{c}^{\ast} and 𝒟i\mathcal{D}_{i}. Define the distribution distance
dc,it:=∫𝒵|Pc,it​(z)−Pc,i∗​(z)|​𝑑z,d_{c,i}^{t}:=\int_{\mathcal{Z}}\big|\,P_{c,i}^{t}(z)-P^{\ast}_{c,i}(z)\,\big|\,dz,
(12)
i.e. the L1L_{1} (total-variation) distance between Pc,itP_{c,i}^{t} and Pc,i∗P^{\ast}_{c,i}.
We assume that the aggregate drift across clients is uniformly bounded as follows: there exists a finite δ\delta such that
1T​∑t=1T∑i=1Ndc,it≤δ.\frac{1}{T}\sum\nolimits_{t=1}^{T}\sum\nolimits_{i=1}^{N}d_{c,i}^{t}\leq\delta.
(13)
Remark 1.
Together, the Assumptions above ensure a well-behaved optimization environment. Assumption 1 guarantees Lipschitz-continuous gradients and provides the usual quadratic upper bound used in descent arguments; Assumption 2 prevents arbitrarily large client/server updates and thus promotes numerical stability; and Assumption 3 limits the stochastic error between the estimator and the true gradient.
Assumption 4 is tailored to the auxiliary-network-assisted FSL setting, as also adopted in [38] and motivated by centralized synthetic-gradient frameworks [2].
This condition is essential for guaranteeing the stability and convergence of the SFL process under local gradient updates.
Theorem 1 (Convergence rate of HERON-SFL in the i.i.d. setting).
Under Assumptions 1–4,
if the client learning rate satisfies ηc≤{13​L​h,2N​L​h2,N72​L}\eta_{c}\leq\{\frac{1}{3Lh},\frac{2}{NLh^{2}},\frac{N}{72L}\},
and is chosen as ηc=𝒪⁡((N​B)/(d​h​T))\eta_{c}=\mathcal{O}(\sqrt{{({NB)}/{(dhT)}}}) while the server learning rate is set to ηs=𝒪⁡((h​B)/(d​N​T))\eta_{s}=\mathcal{O}(\sqrt{{{(hB)}/{(dNT)}}}), and perturbation step size is set to μ=𝒪⁡(1/(d​h​N​B​T)1/4)\mu=\mathcal{O}(1/(dhNBT)^{{1}/{4}}),
the convergence rate of the HERON-SFl algorithm satisfies:
mint∈[T]⁡𝔼⁡[‖∇f​(𝜽gt)‖2]≤𝒪⁡(dh​N​B​T)+𝒪⁡(1d​h​N​B​T).\displaystyle\min_{t\in[T]}\ \mathbb{E}\big[\|\nabla f(\bm{\theta}^{t}_{\text{g}})\|^{2}\big]\leq\mathcal{O}\big(\sqrt{\frac{d}{hNBT}}\big)+\mathcal{O}\big(\sqrt{\frac{1}{dhNBT}}\big).
(14)
Remark 2.
The convergence bound on the expected gradient norm indicates that the algorithm can achieve a favorable trade-off between the model complexity (characterized by the dimensionality dd) and the training batchsize (captured by BB) over the training horizon TT.
The bound is dominated by 𝒪⁡(d/(h​N​B​T))\mathcal{O}\!(\sqrt{d/(hNBT)}) (the second term is smaller by 1/d1/\sqrt{d}).
Equivalently, in terms of the communication complexity, achieving an ε\varepsilon-stationary point requires a total of T=𝒪⁡(d/(h​N​B​ε2))T=\mathcal{O}\!\big(d/(hNB\varepsilon^{2})\big) communication rounds. This implies that the algorithm achieves a linear s

## Raw body offsets 26900–29000

 total of T=𝒪⁡(d/(h​N​B​ε2))T=\mathcal{O}\!\big(d/(hNB\varepsilon^{2})\big) communication rounds. This implies that the algorithm achieves a linear speedup with respect to the number of clients NN and the local batch size BB (i.e., the required rounds scale inversely with the product N​BNB).
Furthermore, increasing the number of local steps hh reduces the required communication rounds by a factor of hh, effectively trading fewer communication rounds for more intensive local computation.
The dependence on model size is d\sqrt{d} (or dd in sample complexity), which is the drawback of ZO optimization: convergence degrades with increasing dimensionality. Below, we show that the dependency on dd can be reduced under structural assumptions on an effective dimension.
Assumption 5 (Low κ\kappa-Effective Rank[35, 18, 26]
).
Let Gt≜maxi,ξi⊂𝒟i⁡‖∇𝛉lll​(θl,it,ξi)‖G_{t}\triangleq\max_{i,\xi_{i}\subset\mathcal{D}_{i}}\|\nabla_{\bm{\theta}_{l}}l_{l}(\theta_{l,i}^{t};\xi_{i})\|. There exists a Hessian matrix Hl​(θl,it)⪯L⋅IdlH_{l}(\theta_{l,i}^{t})\preceq L\cdot I_{d_{l}} such that:
• 
For all 𝜽l\bm{\theta}_{l} such that ‖𝜽l−θl,it‖≤2​ηc​dl​Gt\|\bm{\theta}_{l}-\theta_{l,i}^{t}\|\leq 2\eta_{c}d_{l}G_{t}, we have ∇2ll​(𝜽l)⪯Hl​(𝜽l,it)\nabla^{2}l_{l}(\bm{\theta}_{l})\preceq H_{l}(\bm{\theta}_{l,i}^{t}).
• 
The effective rank of Hl​(𝜽l,it)H_{l}(\bm{\theta}_{l,i}^{t}), i.e., tr​(Hl​(𝜽l,it))‖Hl​(𝜽l,it)‖2\frac{\text{tr}(H_{l}(\bm{\theta}_{l,i}^{t}))}{\|H_{l}(\bm{\theta}_{l,i}^{t})\|_{2}}, is at most κ\kappa.
The low effective rank assumption posits that, although the client-side model may be high-dimensional, its local loss landscape is governed by only a few dominant curvature directions. This phenomenon is widely observed in the training dynamics of deep models [35, 26]; detailed discussion and empirical evidence that supports this assumption in practice are provided in Appendix B.
Theorem 2 (Convergence rate of HERON-SFL with Low Effective Rank Assumption).
Under Assumptions 1–5,
if the client learning rate satisfies ηc≤14​L​(1+d​κ+d−2d+2)\eta_{c}\leq\frac{1}{4L}(1+\frac{d\kapp

## Raw body offsets 33700–37700

VI-A Experiment Setting
In this section, we conduct experiments on both model training and fine-tuning to show the performance of our proposed HERON-SFL algorithm.
For comparison, we use the following baseline methods:
SFLV1/V2 [50] or SplitLoRA22
              2
            While SFLV1/V2 are designed for the training-from-scratch paradigm, our focus on the distinct task of language fine-tuning led to the development of SplitLoRA, which integrates LoRA with the SFLV2 framework. We omit a comparison with an SFLV1-based approach because its need for multiple server models is computationally prohibitive for large-scale models. [27], CSE-FSL [38], and FSL-SAGE [39]. We conduct the experiments under two complementary training paradigms, implementing all models in PyTorch and running them on NVIDIA RTX A6000 NVL GPU (48 GB):
Full Training from Scratch. We study the convergence of ResNet-18 [18] under SFL on CIFAR-10 [24] with 5 clients.
The model is split after the second 2-D BatchNorm layer; the client holds the front part while the server holds the back part.
An auxiliary head consisting of a single fully connected layer is attached to the cut layer.
Unless otherwise stated, we adopt the hyperparameters in [50]: batch size 256 and Adam optimizers on both sides with a learning rate of 1​e−41e{-4}.
Language Model Fine-tuning. We fine-tune GPT2-Small and GPT2-Medium [46] on the E2E dataset [43] with 3 clients. Unless specified otherwise, for GPT2-Small, the model is split after the third transformer block, with an auxiliary network consisting of one transformer block and the unembedding layer. For GPT2-Medium, the split occurs after the sixth block, with a three-block auxiliary network plus the unembedding layer. As the auxiliary network is not pre-trained, we initialize its parameters by copying the weights from the initial blocks of the server-side model. All components are fine-tuned using Low-Rank Adaptation (LoRA) [19], where only adapters of rank 8 are updated and all other parameters are frozen.
The former setting evaluates whether SFL can train a model from scratch, a prerequisite when no reliable checkpoint exists. The latter mirrors the prevailing industrial practice of pre-training a large language model once and then adapting it with parameter- and memory-efficient techniques such as LoRA.
By examining both regimes, we separately measure the contributions of data-parallel federation, model partitioning, and parameter-efficient adapters, and we show that HERON-SFL consistently outperforms strong baselines in both scenarios.
VI-B Training from Scratch: ResNet18 on CIFAR-10
Fig. 2: ResNet-18 test accuracy vs. communication rounds on CIFAR-10 for IID (left) and non-IID (right) distributions.
VI-B1 Convergence Behavior
Fig. 2 illustrates the test accuracy of each method versus the number of communication rounds. In the IID setting, our proposed HERON-SFL shows convergence behavior nearly identical to other auxiliary-network baselines like CSE-FSL and FSL-SAGE33
                3
              We note that FSL-SAGE does not exhibit a significant advantage in our experiments, which we attribute to our design choice of using a minimal auxiliary network purely for decoupling the updates of server and clients. This contrasts with the approach in [39], where the alignment mechanism of FSL-SAGE is more impactful as the auxiliary model is intentionally designed to be even larger than the client model, thus requiring explicit alignment to ensure consistency with the server’s task., with all three performing slightly below the top-performing SFLV2. A similar trend is observed in the more challenging non-IID setting, which confirms that our hybrid algorithm achieves convergence comparable to its first-order counterparts.
TABLE II: Client consumptions for ResNet-18 on CIFAR-10.
Algorithm
Comm. (GB)
Peak FP (MB)
FLOPS (G)
SFLV1
1216.00
709.93
59.51
SFLV2
390.67
CSE-FSL
258.55
726.46
59.85
FSL-SAGE
244.24
HERON-SFL
244.19
259.44
39.90
VI-B

## Raw body offsets 42336–46400

VI-C Language Model Fine-tuning
VI-C1 Training Behavior
For the task of language model fine-tuning, HERON-SFL demonstrates superior communication efficiency and faster convergence. As illustrated in Fig.5, its validation perplexity decreases more rapidly than the baselines for both GPT2-Small and GPT2-Medium. Notably, for GPT2-Small, HERON-SFL converges faster and achieves a final perplexity that is competitive with SplitLoRA while outperforming both CSE-FSL and FSL-SAGE. While all methods reach a similar performance on GPT2-Medium, HERON-SFL does so with significantly less communication costs, and even slightly surpasses CSE-FSL and FSL-SAGE on GPT2-Small. This mild performance gain is consistent with recent findings in ZO-based LM fine-tuning, where the update landscape exhibits strong low-rank structure, making zeroth-order steps exceptionally effective. Similar behavior is reported in MeZO [35], which shows that ZO fine-tuning can match or even surpass first-order methods under comparable settings.
Fig. 5: GPT2 perplexity curves vs. Communication Volume on E2E for small (left) and medium (right) models.
TABLE III: Client consumptions for GPT2-Medium on E2E dataset.
Algorithm
Peak FP (GB)
FLOPS (T)
SplitLora
4.59
5.68
CSE-FSL
9.09
9.48
FSL-SAGE
HERON-SFL
4.03
5.26
VI-C2 Storage and Computational Costs
Echoing the resource efficiency observed in the ResNet experiments, HERON-SFL substantially lowers the on-device computational and memory burden for clients. Table III provides a clear comparison of the resource consumption per local update. HERON-SFL requires a peak memory (Peak FP) of only 4.03 GB, which is less than half that of CSE-FSL (9.09 GB) and also more efficient than the SplitLoRA baseline (4.59 GB).
The reduction in computational cost is even more pronounced, with HERON-SFL needing only 5.26 TFLOPS, a decrease of approximately 44% compared to CSE-FSL and FSL-SAGE. This reduction in both memory footprint and floating-point operations confirms that by eliminating client-side backpropagation, our method significantly lowers the hardware barrier, making it feasible to fine-tune language models on resource-constrained devices.
VI-C3 Ablation study of local model complexity
‘
We investigate the impact of local model complexity on the GPT2-medium fine-tuning task.
Fig. 6: Effect of aux-model complexity on the GPT2-medium fine-tuning task.
We ablate auxiliary-model complexity on the GPT2-medium fine-tuning task under two client partitions, where the client-side model contains either the first 3 or 6 transformer blocks. For each setting, we vary the auxiliary network from a minimal design (LayerNorm and unembedding layers only) to larger variants with 1–3 transformer blocks. Fig.6 reports the final training loss after a fixed number of communication rounds.
HERON-SFL is largely insensitive to the auxiliary model’s capacity: in both settings, it achieves strong final loss even with the minimal auxiliary network. In contrast, the first-order baseline CSE-FSL benefits substantially from a stronger auxiliary model, with performance improving as the auxiliary network grows. These results suggest that ZO-based client updates do not require a resource-intensive auxiliary network, whereas FO baselines rely on auxiliary capacity to reach their full potential. Overall, HERON-SFL delivers strong convergence while reducing peak client memory to inference-level by eliminating client-side backpropagation, providing a better performance–cost trade-off than FO baselines without introducing additional communication overhead.
VII Conclusion
In this work, we have proposed HERON-SFL, a novel hybrid ZO-FO framework that addresses the critical computation and memory limitations on edge devices within SFL. By performing zeroth-order optimization on the client side, HERON-SFL eliminates the need for backpropagation and activation caching during local updates, thereby significantly reducing on-device computational and memory requirements, while operating under the same communication budget as existing auxiliary

## Raw body offsets 85070–86800

Appendix B Evidence for Low Rank Assumption
In this section, we provide empirical and literature evidence that the low-effective-rank phenomenon is broadly present in deep model training (including CNN training and LM fine-tuning), which motivates the low-rank assumption used in our analysis.
First, we validated the low-effective rank assumption using a modified ResNet-18 on CIFAR-10. We estimated the Hessian eigenvalue density via the stochastic Lanczos algorithm [13], following the methodology of [12]. As shown in Fig. 7, the resulting distribution, heavily concentrated at zero, suggests that the low-rank structure is an intrinsic property of the optimization landscape. The same empirical evidence can be seen in Appendix C.3.1 of [26].
This observation extends to the regime of LMs, particularly during the fine-tuning phase. Recent works, such as GaLore [59], have provided robust evidence that while pre-training may necessitate high-rank updates, the weight modifications required for fine-tuning naturally reside in a low-rank subspace. This intrinsic low-dimensionality is a critical factor explaining the success of ZO optimization methods in this domain [35].
It theoretically justifies why methods like MeZO [35] can achieve competitive performance with LoRA updates, as they effectively navigate this low-rank manifold.
Fig. 7: Hessian eigenvalue distribution with training a custom ResNet on the CIFAR-10 dataset.
References
[1]
E. Belilovsky, M. Eickenberg, and E. Oyallon (2019)
Greedy layerwise learning can scale to imagenet.
In International conference on machine learning,
pp. 583–593.
Cited by: §II-A.
[2]
E. Belilovsky, M. Eickenberg, and E. Oyallon (2020)
Decoupled greedy learning of cnns.
In Inter
