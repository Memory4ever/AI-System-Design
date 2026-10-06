# 19285 exact-v1 necessary primary cache

Source: https://arxiv.org/html/2601.19285v1
Original web line labels preserved; sorted and deduplicated within this paper, not contiguous full text.

L241: ### 4.1 Unconditioning Score Matching
L242: 
L243: The loss function in standard noise conditioning score-based neural networks (NCSN) (cite97†Song and Ermon, 2019 ) is
L244: 
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
L269: ## 5 Experiments
L270: Experimental Setup. To evaluate the effectiveness of our smoothing methods, we adopt VE-SDE (cite90†Song et al., 2021 ) as the baseline, which is known as the first time-reverse SDE framework of diffusion models. For fair comparison, we reproduce the VE-SDE setup and apply our smoothing methods with the same implementations. For example, our unconditioning approach uses the same NN architecture as the baseline, with only the time embedding layers removed.
L271: (see cite52†Section B.1 for other details) In addition to the four commonly used datasets, CIFAR-10 (cite116†Krizhevsky et al., 2009 ), CelebA 64$\times$64 (cite117†Liu et al., 2015 ), ImageNet 64$\times$64 (cite118†Deng et al., 2009 ) and CelebA-HQ 256$\times$256 (cite119†Karras et al., 2018 ), we also collect a small 64$\times$64 dataset for ablation studies, consisting of 1,000 pet cats and 200 images of caracals.
L272: Caracals differ from pet cats in having long ears and ferocious faces (see cite120†Figure 2 ), so that we can clearly see any possible generalizations.
L273: cite121†Image: Refer to caption Figure 2: Illustration for the dataset of cat (left) and caracal (right). Note that there are no yellow or long-eared pet cats in the dataset.
L274: KNN Spaces. The curvature of the image manifold in pixel space is large, so when K is large, or the temperature is high, the learned score function may guide samples deviating from the manifold. Therefore, we also apply KNN in the feature space (with significantly smaller curvature). Specifically, we use a pre-trained ResNet-18 first to map all samples to a 512-dimensional latent space, then calculate the KNN and return their indexes for later explicit score function calculation, still in the pixel space.
L275: We find that under the same temperature and K, the feature space-based KNN will lead to obviously better generation quality than the pixel space-based one. This phenomenon further verifies our former explanation that neural networks achieve generalization via learning a smoother score function determined by a local manifold. Note that in this section, all illustrated samples are obtained by pixel space-based KNN to support our claim. We show more results and comparison in the cite72†Section B.4.2 .
L276: Quality Metric. Besides calculating the Fréchet Inception Distance (FID) (cite122†Heusel et al., 2017 ) between generated samples ${G}$ and training samples $\mathcal{T}_{\text{tr}}$, we also calculate the FID between generated samples and test samples $\mathcal{T}_{\text{test}}$. Smaller ratio $\frac{\text{FID}(G,\mathcal{T}_{\text{test}})}{\text{FID}(G,\mathcal{T}_{\text{tr}})}$ could be roughly regarded as better generalization.
L277: Specifically, we randomly select the same number of samples per class from the training set as in the test set to calculate FID. For CelebA, we randomly select 10k images from both the training set and test set.
L278: Sampling for Unconditioning. We first try the existing samplers (cite90†Song et al., 2021 ) by replacing the conditioning score function $s_{\theta}(x,t)$ with our unconditional version $s_{\theta}(x)$. We find that SDE samplers can still succeed while ODE samplers may fail catastrophically.
L279: Under our framework, this occurs because at late sampling stages, the unconditional score function adapts to the true noise level $\sigma_{n*}:=\frac{||\mathbf{x}_{n}-\mu_{*}||}{\sqrt{d}}$, where $\mathbf{x}_{n}$ is current sample and $\mu_{*}$ is its closest training point. However, the sampling schedule still uses the predetermined noise level $\sigma_{n}$. In ODE samplers, we empirically observe that $\sigma_{n}\gg\sigma_{n*}$ as $\mathbf{x}_{n}$ approaches training data, creating a critical mismatch.
L280: We prove in cite49†Section A.7.1 that this mismatch causes ODE samplers to take excessively large steps $\propto\sigma_{n}^{2}/\sigma_{n*}^{2}$, leading to catastrophic overshoot. In contrast, SDE samplers remain stable because their stochastic noise term creates a self-correcting mechanism that keeps $\sigma_{n*}$ reasonably close to $\sigma_{n}$ (cite50†Section A.7.2 ).
L281: To address this mismatch, one way is to fix the implicit noise level after every ODE step like the Predictor-Corrector (PC) sampling in (cite90†Song et al., 2021 ). Another way is to directly replacing the predetermined $\sigma_{n}$ by $\sigma_{n*}$:
L282:  | $$\mathbf{x}_{n+1}=\mathbf{x}_{n}+\alpha\sigma_{n*}^{2}s_{\theta}(\mathbf{x}_{n})$$  |
L283: where $\alpha$ controls the step size. Although computing $\sigma_{n*}$ requires finding the nearest training point which may be expensive for large-scale datasets, our unconditional score function enables bigger step sizes than standard diffusion models, resulting in significantly fewer function evaluations (NFE) that often compensate for this overhead.
L284: This is because the unconditioning score function is well-defined across the entire support of $p_{\text{\scriptsize{MN}}}$, and so avoids the error accumulation of large time steps in standard diffusion models.
L285: ### 5.1 Ablation Studies on Cat Caracal Dataset
L286: #### 5.1.1 Qualitative Experiments
L287: 
L288: cite123†Image: Refer to caption Figure 3: Qualitative comparison with different methods. (a, b, c) illustrates the generated images (left of red line) and their top-3 nearest neighbors of training samples in pixel space. (d) shows the generated images (2, 3, 4) and their corresponding closest training sample (1). (closest in both pixel and feature spaces)
L289: Since the cat-caracal dataset uses only 1,200 images for training, there are relatively few regions where the empirical score function is sharp, i.e., where different training points compete. Therefore, a neural network with sufficient capacity can capture this sharpness, leading to pure memorization, as we see in cite124†Figure 3 (a).
L290: However, either unconditioning modeling or temperature smoothing (here $T_{i}=7/\sigma_{i}$ for $i=1,2,\dotsc,N$ and K=10) can generalize well, illustrated by cite124†Figure 3 (b) and (c) respectively. We can see obvious generalization in (c), e.g., the first generated cat, which has a caracal face but short ears and gray color. Meanwhile, in cite124†Figure 3 (d), we compare the generated images with their same collapse training sample (1). Conditioning modeling (2) can only replicate the source image.
L291: In contrast, the unconditioning modeling (3) will not fully memorize, and temperature smoothing (4) shows significant generalization.
L292: #### 5.1.2 Quantitative Experiments
L293: To empirically support our argument in cite12†Section 3.2 , we calculate $\gamma_{\scriptsize{ex}}$ under different noise levels using the learned score functions (NN Conditioning and Unconditioning), the empirical conditioning score function, the unconditioning (T=1), and the temperature-based ones (T=10,100,1000).
L301: To further verify the effectiveness of our methods, we also implement experiments on some commonly used datasets. We first present ablation studies evaluated by FID on the CIFAR-10 and CelebA datasets. As shown in cite127†Table 1 , although the FID score slightly deteriorates at some settings, this is accompanied by observable and meaningful generalization.
L302: As illustrated in cite128†Figure 5 (b) and (c), for example, the generated images on CelebA exhibit clear generalization: the red face in (b) and a similar countenance in (c), both of which indicate that the NN has captured the common characteristics of training samples in the local manifold. In practice, we can simply choose an appropriate temperature to achieve strong generalization while maintaining comparable quality.
L303: Table 1: Ablation studies of our smoothing methods on the CIFAR-10 and CelebA datasets. “$\to$” indicates the performance change from pixel space-based KNN to feature space-based KNN.
L304: Method  | FID$(G,\mathcal{T}_{\text{tr}})$  | FID$(G,\mathcal{T}_{\text{test}})$
L305: CIFAR-10 32$\times$32
L306: SDE (PC) 1K NFE  |  |
L307: Conditioning  | 6.49  | 6.56
L308: Unconditioning  | 7.33  | 7.34
L309: $T_{i}=1/\sigma_{i}$, K=30  | 8.32 $\to$ 8.08  | 8.25 $\to$ 8.02
L310: $T_{i}=1/\sigma_{i}$, K=100  | 8.67 $\to$ 7.97  | 8.61 $\to$ 7.89
L311: $T_{i}=5/\sigma_{i}$, K=30  | 8.56 $\to$ 8.12  | 8.60 $\to$ 8.15
L312: $T_{i}=5/\sigma_{i}$, K=100  | 13.25 $\to$ 8.35  | 13.41 $\to$ 8.30
L313: $T_{i}=7/\sigma_{i}$, K=30  | 21.28 $\to$ 8.26  | 21.34 $\to$ 8.22
L314: $T_{i}=7/\sigma_{i}$, K=100  | 50.81 $\to$ 7.96  | 51.08 $\to$ 7.98
L315: ODE (PC) 1K NFE  |  |
L316: Conditioning  | 8.48  | 8.50
L317: Unconditioning  | 8.84  | 8.88
L318: $T_{i}=1/\sigma_{i}$, K=30  | 8.75 $\to$ 8.45  | 8.67 $\to$ 8.43
L319: CelebA 64$\times$64
L320: SDE (PC) 1K NFE  |  |
L321: Conditioning  | 7.25  | 7.81
L322: Unconditioning  | 7.07  | 7.34
L323: $T_{i}=5/\sigma_{i}$, K=30  | 9.58 $\to$ 8.78  | 9.32 $\to$ 8.54
L324: $T_{i}=5/\sigma_{i}$, K=100  | 36.63 $\to$ 9.47  | 35.01 $\to$ 9.10
L325: $T_{i}=10/\sigma_{i}$, K=30  | 9.88 $\to$ 8.64  | 9.48 $\to$ 8.56
L326: $T_{i}=10/\sigma_{i}$, K=100  | 61.97 $\to$ 8.40  | 60.91 $\to$ 8.19
L327: ODE (PC) 1K NFE  |  |
L328: Conditioning  | 7.65  | 7.87
L329: Unconditioning  | 7.71  | 7.88
L330: $T_{i}=5/\sigma_{i}$, K=30  | 9.36 $\to$ 8.67  | 9.50 $\to$ 8.80
L331: Moreover, the results in cite127†Table 1 show that the feature space-based KNN consistently outperforms the pixel space-based KNN across all settings. Operating in feature space enables more aggressive smoothing (larger temperatures and $K$) while maintaining strong performance. For instance, on CIFAR-10 with $T_{i}=7/\sigma_{i}$ and $K=100$, pixel-space KNN collapses (FID increases to 50.81), whereas feature-space KNN still attains an FID of 7.96.
L332: This observation also supports our hypothesis that the neural network generalizes by smoothing the local manifolds, as lower local curvature (feature space) allows for stronger score smoothing without driving samples off the manifold. The consistent improvements suggest that feature space provides a more appropriate geometric structure for our smoothing methods.
L333: These results motivate us to extend our approach to latent diffusion models, which may further enhance generalization while preserving computational efficiency.
L334: In the Appendix, we present complementary results on other high-resolution datasets, including ImageNet 64$\times$64 and CelebA-HQ 256$\times$256. We also provide detailed proofs, training cost analysis, and extensive experiments to validate our theoretical approximations and claims.
L335: ## 6 Conclusion
L336: This work establishes a theoretical framework for understanding memorization in diffusion models through the analysis of several variants of the empirical score function and its NN approximations. It reveals that memorization arises from the dominance of individual training samples in softmax-weighted score functions, while generalization emerges through smoothed weight distributions that enable local manifold exploration.
L337: By exploring the fundamental properties of the score function, we identify the cause of memorization and propose two smoothing methods — Noise Unconditioning and Temperature Smoothing — which elegantly control the concentration of the score function weight and effectively reduce memorization while maintaining high generation quality.
L338: We started from a theory-practice inconsistency, then developed mathematical analysis and experimental validations, each step revealing how neural networks achieve the remarkable property of generalization. Our framework not only rationalizes previously observed memorization behavior but also unifies and extends prior unconditioning approaches under an optimization-based viewpoint.
L339: ## 7 Broader Impact
L340: Generalization Perspective. Memorization in diffusion models poses significant concerns across multiple domains. In healthcare applications, patient data leakage through generated medical images could violate privacy regulations and compromise sensitive health information. In creative industries, models that memorize copyrighted content risk intellectual property infringement when used for commercial image generation.
L341: Our methods address these risks by reducing the likelihood of exact training data replication while preserving the quality and diversity of generated samples, enabling safer deployment of diffusion models in privacy-sensitive and legally regulated contexts.
L342: Gradient Ascent Perspective. Our noise unconditioning reformulates sampling as gradient ascent on a unified distribution, enabling constraints to be integrated via projected gradient methods. This feature is particularly valuable for applications requiring adherence to physical laws, such as video generation, which struggles to learn complex physical dynamics from data alone.
L343: Intuitive Understanding. By visualizing the sampling process as moving from large shells (high noise) to small shells (low noise), we offer a natural geometric interpretation that bridges the gap between complex mathematical formulations and intuitive understanding. Further, our unconditioning modeling transfers the time-reverse SDE into a familiar optimization process, making diffusion models more accessible to the broader generative community.

