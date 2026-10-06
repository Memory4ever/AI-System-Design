# 19285 exact-v1 EVAL necessary primary excerpts

Source: https://arxiv.org/html/2601.19285v1
Original labels retained. Sorted within the single paper; only necessary positions actually fetched, not full-document review.

L213: We give an example to build intuition about how large the ratio can be even for modest values of $\alpha$. For the case of $\alpha=\frac{1}{3}$ (that is, $\sigma_{opt}$ is only slightly closer to $\sigma_{i}$ than to $\sigma_{i+1}$), we have $\gamma_{\sigma}\approx e^{6}\approx 403$, so $w_{ij}(\mathbf{x})$ dominates its closest neighbor. Its dominance over all other weights will be even greater.
L214: Based on this property, we can then simplify the score function, representing the weight of a center $\mu_{j}$ by only using its optimal noise level $\sigma_{j}^{*}$:
L215:  | $$w_{j}^{*}(\mathbf{x}):=\frac{\sigma_{j}^{*2}\mathcal{N}(\mathbf{x};\bm{\mu}_{j},\sigma_{j}^{*2}\mathbf{I})}{\sum_{l=1}^{M}\sigma_{l}^{*2}\mathcal{N}(\mathbf{x};\bm{\mu}_{l},\sigma_{l}^{*2}\mathbf{I})}.$$  |  | (5)
L216: Property 2. $\mu$ domination: Given a position $\mathbf{x}$, the score function weight of a center decreases exponentially as the distance between the center and $\mathbf{x}$ increases. We have the following conclusion for the case that two training points $\mu_{j}$ and $\mu_{l}$ are a similar distance from $\mathbf{x}$, namely $\sigma_{j}^{*}=\sigma_{l}^{*}$ but $\|\mathbf{x}-\mu_{l}\|\geq\|\mathbf{x}-\mu_{j}\|$:
L217:  | $$\gamma_{\mu}\approx\frac{w_{j}^{*}}{w_{l}^{*}}=\exp\left(\frac{\delta||\mu_{j}-\mu_{l}||^{2}}{\sigma_{j}^{*2}}\right)$$  |  | (6)
L218: where $\delta:=\frac{||x-\mu_{l}||\cos\angle x\mu_{l}\mu_{j}}{||\mu_{j}-\mu_{l}||}-\frac{1}{2}\geq 0$ represents the relative distance advantage of $\mu_{j}$ over $\mu_{l}$ with respect to $\mathbf{x}$ (see derivation in cite37†Section A.4.2 ) and $\gamma_{\mu}$ captures the ratio of the weights corresponding to the two centers $\mu_{j}$ and $\mu_{l}$. Typically, $\delta\lesssim O(\frac{1}{\sqrt{d}})$ maintains the condition $\sigma_{j}^{*}=\sigma_{l}^{*}$.
L219: However, during the sampling, the progressive reduction of $\sigma_{j}^{*}$ causes $\gamma_{\mu}$ to grow. When $\sigma_{j}^{*}$ is sufficiently small, the single center $\mu_{j}$ will dominate the score function weight, resulting in collapse and subsequent memorization.
L220: ### 3.2 Generalization Evaluation
L221: From Property 2 in cite11†Section 3.1 , we know that memorization occurs when $\sigma$ is small because the closest training point dominates the score function weight, even when it is not much closer than other points. However, in practice, we generate samples using neural networks to approximate the empirical score function, and this often results in novel samples. These observations suggest that the score function learned by the neural network must differ from the empirical score function.
L222: A natural explanation is that the neural network fits the score function quite well, but implicitly smooths its weights at small noise levels, preventing the dominance of individual training points and avoiding sampling collapse. Following this insight, we analyze the generalization ability of neural networks, standard diffusion, noise unconditioning, and temperature smoothing by comparing the expansiveness of their sampling process at points where the shells from different training points overlap.
L223: We simplify the analysis by considering only the two training points closest to $\mathbf{x}$, which is sufficient for our purposes because Proposition 2 indicates that the closest training samples have the greatest (dominant) influence on the flow.
L224: Denoting the two closest training points by $\mu_{0}$ and $\mu_{1}$, assume that the sampling point $\mathbf{x}$ is similarly close to both of them, with the same shell radius $\sigma^{*}\sqrt{d}$ for both. We assume $\|\mathbf{x}-\mu_{0}\|=C\|\mathbf{x}-\mu_{1}\|=C\sigma^{*}\sqrt{d}$, where $C\geq 1$. We then slightly perturb $\mathbf{x}$ along the direction $(\mu_{0}-\mu_{1})$ to obtain position $\mathbf{y}$, such that $\|\mathbf{y}-\mu_{1}\|=C\|\mathbf{y}-\mu_{0}\|=C\sigma^{*}\sqrt{d}$.
L225: After one sampling step for both $\mathbf{x}$ and $\mathbf{y}$, we arrive at $\mathbf{x^{\prime}}$ and $\mathbf{y^{\prime}}$ respectively. We then evaluate the expansion factor
L226:  | $$\gamma_{\scriptsize{ex}}:=\frac{\|\mathbf{y^{\prime}}-\mathbf{x^{\prime}}\|}{\|\mathbf{y}-\mathbf{x}\|}.$$  |
L227: This ratio serves as an indicator of generalization because 1) memorization can induce an arbitrarily large ratio (formally unbounded in the limit); 2) a bounded ratio (i.e., a locally non-expansive sampling map, in the same sense as non-expansive updates in optimization) preserves the local connectivity of the sampled distribution, and thus serves as a quantitative proxy for generalization.
L228: Empirical vs. Neural Network: Under the above assumption, for the empirical score function of standard diffusion, we have:
L229: 
L230:  | $$\gamma_{\scriptsize{ex}}\approx\frac{\|\eta(\mu_{0}-\mu_{1})\|}{\|y-x\|}\left|1-\frac{2}{a+1}\right|$$  |  | (7)
L231: where $\eta$ is the sampling stepsize and $a>1$ represents the ratio of the dominant to subdominant score function weight (see derivation in cite39†Section A.5 ). This result still holds for $\|y-x\|\to 0$ if $d\to\infty$, which means that $a\to\infty$ and the ratio could be unbounded, showing poor generalization. However, the results of interpolation experiments in diffusion models (cite90†Song et al., 2021 ; cite89†Ho et al., 2020 ) show that $\|y^{\prime}-x^{\prime}\|\to 0$ if $\|y-x\|\to 0$.
L232: Our experiments (cite19†5.1.2 ) also show that the learned score function has a much smaller ratio than the empirical one.
L233: Conditioning vs. Unconditioning. Under our assumption, the unconditioning modeling has the same ratio formula as in cite112†Equation 7 but with a different coefficient $a$. From the property of $\sigma$-domination, we know that the unconditioning case has a smoother score function weight, leading to a smaller ratio $\gamma_{\scriptsize{ex}}$ and therefore better generalization.
L234: Temperature. We modify the weight calculations by introducing a temperature vector $T\in\mathbb{R}^{N}$ whose $i$-th component $T_{i}$ contains the temperature for shell $i$. We define $T^{*}_{j}$ to be the value of $T_{i}$ for which $\sigma_{i}=\sigma_{j}^{*}$. Generalizing cite113†Equation 5 , the temperature-based score function weight is defined as:
L235:  | $$w_{j}^{*}(\mathbf{x};T)={\frac{\exp\left(\frac{f(\mathbf{x},\mu_{j},\sigma_{j}^{*})}{T_{j}^{*}}\right)}{\sum_{l=1}^{M}\exp\left(\frac{f(\mathbf{x},\mu_{l},\sigma_{l}^{*})}{T_{l}^{*}}\right)}}.$$  |
L236: 
L237: (We recover cite113†Equation 5 by setting $T_{i}=1$, $i=1,2,\dotsc,N$.) As the $T_{i}$ increase to $\infty$, the temperature smoothing reduces the dominance ratio $a$, resulting in smaller $\gamma_{\scriptsize{ex}}$ and better generalization.
L238: ## 4 Learning the Smoothed Score Function
L239: We next describe our methods for training the neural network score functions $\mathbf{s}_{\theta}$, parametrized by weight vector $\theta$. Our noise scheduling follows the variance exploding SDE in (cite90†Song et al., 2021 ), where the noise scale $\sigma$ is sampled from a discrete set of $N$ points that approximate a log-uniform distribution over the range $[\sigma_{\text{min}},\sigma_{\text{max}}]$. The probability of selecting each $\sigma_{i}$ is equally $\frac{1}{N}$.
L240: We denote sampling from this noise schedule as $\sigma_{i}\sim p_{\sigma}$.
L241: ### 4.1 Unconditioning Score Matching
L242: 
L243: The loss function in standard noise conditioning score-based neural networks (NCSN) (cite97†Song and Ermon, 2019 ) is
L244: 
L245:  | $$\mathcal{L}_{\text{c}}=\mathbb{E}_{\mathbf{\sigma}_{i}\sim p_{\sigma}}\mathbb{E}_{\mathbf{\mu}\sim p^{*}}\mathbb{E}_{{\mathbf{x}}\sim\mathcal{N}(\mu,\sigma_{i}^{2}\mathbf{I})}\left[\frac{\sigma_{i}^{2}}{2}\left\|\mathbf{s}_{\theta}({\mathbf{x}},\sigma_{i})+\frac{{\mathbf{x}}-\mu}{\sigma_{i}^{2}}\right\|_{2}^{2}\right].$$  |  | (8)
L246: We have a similar objective function for the unconditioning modeling:
L247: 
L248:  | $$\mathcal{L}_{\text{u}}=\mathbb{E}_{\mathbf{\sigma}_{i}\sim p_{\sigma}}\mathbb{E}_{\mathbf{\mu}\sim p^{*}}\mathbb{E}_{{\mathbf{x}}\sim\mathcal{N}(\mu,\sigma_{i}^{2}\mathbf{I})}\left[\frac{\sigma_{i}^{2}}{2}\left\|\mathbf{s}_{\theta}({\mathbf{x}})+\frac{{\mathbf{x}}-\mu}{\sigma_{i}^{2}}\right\|_{2}^{2}\right].$$  |  | (9)
L249: The only difference is that we remove the noise as an input to the neural networks. Following the denoising score matching (cite96†Vincent, 2011 ), we show in cite47†Section A.6 that optimizing this loss function is equivalent to performing explicit score matching for the distribution $p_{\text{\scriptsize{MN}}}$.
L250: ### 4.2 Temperature-based Score Matching
L251: From cite114†Equation 6 and the analysis in Section cite10†3 , we know that when the noise level is small, training samples close to $\mathbf{x}$ will dominate the score function weights. Therefore, we set a threshold $\sigma_{\text{collapse}}$ to determine when we should introduce temperature scaling.
L252: When $\sigma_{i}\leq\sigma_{\text{collapse}}$, for a noisy point $\mathbf{x}$ drawn from $\mathcal{N}(\mu,\sigma_{i}^{2}\mathbf{I})$ where $\mu\sim p^{*}$, $\mu$ should be the closest training sample to $\mathbf{x}$. We can then approximate the score function using the top-$K$ nearest training samples to $\mu$, denoted by $\mu_{(j)}$, $j=1,2,\dotsc,K$, as follows:
L253:  | $$\nabla_{\mathbf{x}}\log p_{\text{\scriptsize{MN}}}(x;T)\approx\sum_{j=1}^{K}w_{(j)}^{*}(x;T)\left(-\frac{\mathbf{x}-\mu_{(j)}}{\sigma_{(j)}^{*2}}\right)$$  |  | (10)
L254: 
L255: where
L256: 
L257:  | $$\quad w_{(j)}^{*}(x;T)=\frac{\exp\left(\frac{f(\mathbf{x},\mu_{(j)},\sigma_{(j)}^{*})}{T_{(j)}^{*}}\right)}{\sum_{l=1}^{K}\exp\left(\frac{f(\mathbf{x},\mu_{(l)},\sigma_{(l)}^{*})}{T_{(l)}^{*}}\right)}.$$  |
L258: 
L259: We thus define the score matching loss to be:
L260:  | $$\mathcal{L}_{\text{T}}=\mathbb{E}_{{\mathbf{x}}\sim p_{\text{\scriptsize{MN}}}}\left[\frac{1}{2}\left\|\mathbf{s}_{\theta}({\mathbf{x}})-\nabla_{\mathbf{x}}\log p_{\text{\scriptsize{MN}}}(\mathbf{x};T)\right\|_{2}^{2}\right].$$  |
L261: 
L262: where practically we use cite115†Equation 10 to approximate $\nabla_{\mathbf{x}}\log p_{\text{\scriptsize{MN}}}(\mathbf{x};T)$.
L263: 
L264: To sum up, the complete temperature-based training loss adaptively combines both approaches based on the noise level of each sample:
L265:  | $$\mathcal{L}=\mathbb{E}_{\sigma_{i}\sim p_{\sigma}}\left[\begin{cases}\mathcal{L}_{\text{u}},&\text{if }\sigma_{i}>\sigma_{\text{collapse}}\\
L266: \mathcal{L}_{\text{T}},&\text{if }\sigma_{i}\leq\sigma_{\text{collapse}}\end{cases}\right]$$  |  | (11)
L267: 
L268: Experimentally, we set $T_{i}=\max(\frac{\sigma_{\text{collapse}}}{\sigma_{i}},1)$. Note that temperature-based score matching is not rigorously learning the score function of $p_{\text{\scriptsize{MN}}}$, but its smoothed proxy version.
L1015: The condition $\beta_{n}>1$ triggers the correction mechanism: the stochastic term dominates the deterministic drift, and the noise injection effectively controls the distance. Specifically:
L1016: 
L1017:  | $$\sigma_{n+1}^{*2}=\sigma_{n}^{*2}(1-\beta_{n}+\beta_{n}^{2})\approx\sigma_{n}^{*2}\beta_{n}^{2}=\frac{(\sigma_{n}^{2}-\sigma_{n+1}^{2})^{2}}{\sigma_{n}^{*2}}$$  |
L1018: 
L1019: Since $\beta_{n}\gg 1$, this gives $\sigma_{n+1}^{*}\approx\frac{\sigma_{n}^{2}-\sigma_{n+1}^{2}}{\sigma_{n}^{*}}\gg\sigma_{n}^{*}$.
L1020: 
L1021:   3. 3.
L1022: Why this prevents large deviations: The noise injection creates a lower bound for how small $\sigma_{n}^{*}$ can become. Even if $\sigma_{n}^{*}$ tries to collapse to zero, the stochastic term ensures that:
L1023: 
L1024:  | $$\sigma_{n+1}^{*}\geq\sqrt{\sigma_{n}^{2}-\sigma_{n+1}^{2}}$$  |
L1025: 
L1026: This lower bound is determined by the schedule difference $\sqrt{\sigma_{n}^{2}-\sigma_{n+1}^{2}}$, which is typically on the same order as the scheduled noise levels.
L1027: 
L1028:   4. 4.
L1029: Automatic regulation: If $\sigma_{n}^{*}$ becomes much smaller than $\sigma_{n}$, the correction pushes it back up. If $\sigma_{n}^{*}$ is already close to $\sigma_{n}$, then $\beta_{n}\approx 1$ and the system evolves smoothly without dramatic corrections. This creates a self-correction mechanism that keeps $\sigma_{n}^{*}$ within a reasonable range of $\sigma_{n}$.
L1030: ## Appendix B Experiments
L1031: 
L1032: In this section, we provide training details and additional experimental results.
L1033: ### B.1 Implementation Details
L1034: 
L1035: Model Architecture. As we mentioned in the main paper, we use the NCSN++ architecture and VE-SDE (our baseline) (cite90†Song et al., 2021 ) on all datasets. The only difference is that, for the unconditioning modeling, we remove the noise embedding blocks. All models are unconditional (i.e., without class labels) across different datasets and trained on 4$\times$ NVIDIA-L40S GPUs (45G) and 2$\times$ NVIDIA-H200 GPUs (140G).
L1036: Training Setup. We train all models with the AdamW (cite180†Loshchilov and Hutter, 2019 ) optimizer using learning rate 0.0002. Using a batch size of 128, we train 1M iterations on CIFAR-10; Using a batch size of 64, we train 40,000 iterations on Cat-Caracal, 700,000 iterations on CelebA 64$\times$64, and 700,000 iterations on ImageNet 64$\times$64; Using a batch size of 36, we train 500,000 iterations on CelebA-hq 256$\times$256.
L1037: Although the reported FIDs are based on the best checkpoints of each setting, for fair comparison, we do not modify other hyperparameters in the baseline paper, e.g., we use EMA decay rate of 0.9999, and all experiments are trained with the PyTorch random seed 42.
L1038: Training Cost and Scalability. For the standard setting with a single temperature level ($T=1$), conditioning vs. unconditioning only differs in whether the noise is fed into the network. Consequently, noise unconditioning introduces no additional asymptotic cost; in fact, removing the noise embedding slightly reduces both GPU memory and wall-clock time per batch.
L1039: When enabling temperature-based score matching, the only extra component is the KNN-based approximation of the explicit score, which naively scales with both dataset size and data dimension and can be prohibitive on very large, high-resolution datasets. However, this additional cost is avoidable. We provide two simple but effective strategies:
L1040:   1. 1.
L1041: 
L1042: Class-restricted neighborhoods for labeled data. For datasets with class labels (e.g., ImageNet), we can restrict KNN search to samples within the same class. In practice, this means we only search over about $1{,}300$ images per query on ImageNet, so the nearest-neighbor step adds almost no overhead.
L1043: 
L1044:   2. 2.
L1045: KNN in the feature space. We perform KNN in a low-dimensional feature space produced by a fixed encoder rather than in pixel space. This converts a high-dimensional search (e.g., $64\times 64\times 3$) into a low-dimensional one (hundreds of dimensions), and is compatible with approximate nearest neighbor libraries that scale to tens or hundreds of millions of points.
L1046: As a result, the additional cost of temperature smoothing is dominated by the encoder forward pass and becomes essentially independent of image resolution.
L1047: With these design choices, the extra computation from temperature-based KNN becomes a small, bounded overhead rather than a bottleneck, even as the dataset and resolution grow. Table cite181†2 reports the empirical per-batch runtime and peak GPU memory under different variants, averaged over the first 1000 iterations on two NVIDIA L40S GPUs.
L1048: 
L1049: From Table cite181†2 , we observe:
L1050: 
L1051:   1. 1.
L1052: Unconditioning is essentially free. Removing the noise embedding consistently reduces runtime and memory relative to the conditioning baseline. This empirically confirms that noise-unconditioned models do not introduce any extra training overhead and remain compatible with existing large-scale training budgets.
L1053: 
L1054:   2. 2.
L1055: Feature-space KNN scales like standard diffusion. When KNN is computed in feature space, the per-batch runtime and memory are virtually identical to the conditioning baseline (e.g., CIFAR-10: 0.3551 s vs. 0.3540 s and 16.22 GB vs. 16.86 GB; CelebA: 0.4115 s vs. 0.4168 s and 45.02 GB vs. 45.02 GB).
L1056: This indicates that temperature smoothing with feature-space KNN behaves, in practice, as a constant-factor modification to standard diffusion training, and does not change the overall scaling with model size or data size.
L1057:   3. 3.
L1058: 
L1059: Naive pixel-space KNN is the only non-scalable variant—and is unnecessary. Direct KNN in pixel space leads to noticeable overhead on higher resolutions (CelebA: 0.4115 s $\to$ 0.5066 s and 45.02 GB $\to$ 52.50 GB), which is expected because the cost grows with the ambient dimension. Since class-restricted and feature-space KNN both avoid this issue and empirically perform better, there is no need to rely on the pixel-space variant in large-scale settings.
L1060: Table 2: Per-batch training cost (time and peak GPU memory) under different model variants. Runtimes are measured on two NVIDIA L40S GPUs and averaged over the first 1000 batches. “KNN-pixel” and “KNN-feature” denote temperature-based score matching with KNN computed in pixel space and feature space, respectively (all with $T_{i}=5/\sigma_{i}$, $K=30$).
L1061: Dataset & Resolution  | Method  | Time / batch (s)  | Mem (GB)  | Batch size
L1062: CIFAR-10 $32\times 32$  | Conditioning  | 0.3551  | 16.22  | 128
L1063: Unconditioning  | 0.3371  | 16.13  | 128
L1064: KNN-pixel  | 0.3466  | 16.40  | 128
L1065: KNN-feature  | 0.3540  | 16.86  | 128
L1066: Cat-Caracal $64\times 64$  | Conditioning  | 0.4075  | 24.74  | 64
L1067: Unconditioning  | 0.3957  | 24.72  | 64
L1068: KNN-pixel  | 0.3976  | 24.92  | 64
L1069: KNN-feature  | 0.4031  | 24.98  | 64
L1070: CelebA $64\times 64$  | Conditioning  | 0.4115  | 45.02  | 64
L1071: Unconditioning  | 0.3946  | 45.01  | 64
L1072: KNN-pixel  | 0.5066  | 52.50  | 64
L1073: KNN-feature  | 0.4168  | 45.02  | 64
L1074: Overall, Noise Unconditioning and Temperature Smoothing can be trained with virtually the same computational budget as standard diffusion models. The only non-negligible overhead arises from a deliberately naive KNN implementation in pixel space, which is avoidable in practice.
L1075: By restricting neighborhoods (for labeled datasets) and operating in a compact feature space, our method maintains the same asymptotic scaling as conventional diffusion training and can be plugged into existing large diffusion pipelines without increasing the number of GPUs or the total training time.

