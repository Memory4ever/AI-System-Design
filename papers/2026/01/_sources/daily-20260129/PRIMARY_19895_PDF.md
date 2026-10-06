# 19895 exact-v1 PDF necessary primary excerpts

Source: https://arxiv.org/pdf/2601.19895v1
Original labels retained. Sorted within the single paper; only necessary positions actually fetched, not full-document review.

L0@P0: Post-LayerNorm Is Back: Stable, ExpressivE, and Deep
L1@P0: Chen Chen∗, Lai Wei∗,†
L2@P0: ByteDance Seed
L3@P0: ∗Equal Contribution,†Corresponding authors
L4@P0: Abstract
L5@P0: Large language model (LLM) scaling is hitting a wall. Widening models yields diminishing returns,
L6@P0: and extending context length does not improve fundamental expressivity. In contrast, depth scaling
L7@P0: offers theoretically superior expressivity, yet current Transformer architectures struggle to train
L8@P0: reliably at extreme depths. We revisit the Post-LayerNorm (Post-LN) formulation, whose instability
L9@P0: at scale caused its replacement by Pre-LN in modern LLMs. We show that the central failure mode
L10@P0: of Post-LN arises from the ResNet-style residual pathway, which introduces gradient vanishing in
L11@P0: deep networks. We present Keel, a Post-LN Transformer that replaces this residual path with
L12@P0: a Highway-style connection. This modification preserves the gradient flow through the residual
L13@P0: branch, preventing signal vanishing from the top layers to the bottom. Unlike prior methods, Keel
L14@P0: enables stable training at extreme depths without requiring specialized initialization or complex
L15@P0: optimization tricks. Keel trains robustly at depths exceeding 1000 layers and consistently
L16@P0: improves perplexity and depth-scaling characteristics over Pre-LN. These findings indicate that
L17@P0: Post-LN, when paired with a Highway-style connection, provides a simple and effective foundation
L18@P0: for building deeply scalable LLMs, opening the possibility for future infinite-depth architectures.
L19@P0: Date: January 28, 2026
L20@P0: Correspondence: Lai Wei at laiwei.future@bytedance.com
L21@P0: 0 200 400 600 800 1000
L22@P0: Training Step
L23@P0: 4
L24@P0: 6
L25@P0: 8
L26@P0: 10
L27@P0: 12
L28@P0: Training Loss
L29@P0: Training Stability (LR = 4.5×10 ³)
L30@P0: Pre-LN
L31@P0: KEEL
L32@P0: (a) Training Stability
L33@P0: Multilingual
L34@P0: Understanding
L35@P0: General Knowledge
L36@P0: & Commonsense
L37@P0: Math & Code Overall
L38@P0: Average
L39@P0: 0
L40@P0: 10
L41@P0: 20
L42@P0: 30
L43@P0: 40
L44@P0: 50
L45@P0: 60
L46@P0: 70
L47@P0: 80
L48@P0: Average Score (%)
L49@P0: 66.4
L50@P0: 63.6
L51@P0: 38.6
L52@P0: 58.7
L53@P0: 70.8
L54@P0: 66.4
L55@P0: 45.0
L56@P0: 62.5
L57@P0: +6.6%
L58@P0: +4.4%
L59@P0: +16.5%
L60@P0: +6.5%
L61@P0: Performance Across Capabilities
L62@P0: Pre-LN
L63@P0: KEEL
L64@P0: (b) Expressiveness
L65@P0: 64 128 512 1024
L66@P0: Number of Layers
L67@P0: 35
L68@P0: 40
L69@P0: 45
L70@P0: 50
L71@P0: 55
L72@P0: 60
L73@P0: Average Benchmark Score (%)
L74@P0: 37.9
L75@P0: 39.6
L76@P0: 45.3
L77@P0: 46.5
L78@P0: 54.3
L79@P0: 58.1
L80@P0: 57.9
L81@P0: 60.9
L82@P0: Depth Scaling of KEEL
L83@P0: Pre-LN
L84@P0: KEEL
L85@P0: (c) Depth Scaling
L86@P0: Figure 1 KEEL enables stable, expressive, and deep LLM training. (a) Training Stability: Keel maintains
L87@P0: smooth convergence at aggressive learning rates, while Pre-LN exhibits severe instability under the same configuration.
L88@P0: (b) Expressiveness: Keel demonstrates superior performance across all capability domains, particularly in Math
L89@P0: & Code (+16.5%). (c) Depth Scaling: Keel consistently outperforms Pre-LN across all depths (64-1024 layers).
L90@P0: Together, these results demonstrate that Keel’s architectural improvements enable stable optimization of ultra-deep
L91@P0: networks with enhanced learning efficiency and model expressiveness.
L92@P0: 1
L93@P0-1: arXiv:2601.19895v1 [cs.LG] 27 Jan 20261 Introduction
L94@P1: Large language model (LLM) progress has been driven primarily by scaling: bigger models, longer context
L95@P1: windows, and larger training corpora. Yet these conventional scaling axes are beginning to show diminishing
L96@P1: returns. Width scaling saturates quickly, context scaling grows increasingly expensive, and parameter growth
L97@P1: alone does not unlock qualitatively new behaviors. As a result, LLM scaling is hitting a wall, and there is
L98@P1: increasing interest in architectural directions that can deliver more expressivity per parameter.
L99@P1: Depth scaling offers a promising path forward. In principle, deeper networks can represent exponentially
L100@P1: richer functions and support more hierarchical reasoning. However, current LLM architectures struggle to
L101@P1: capitalize on depth. Training becomes increasingly unstable at extreme depths, and even when optimization
L102@P1: succeeds, depth scaling delivers substantially worse returns than width scaling under current architectures.
L103@P1: The placement of Layer Normalization (LN), which is a seemingly simple architectural choice, has an enormous
L104@P1: effect on depth scaling. The original Transformer architecture used Post-LayerNorm (Post-LN), but modern
L105@P1: LLMs overwhelmingly adopt Pre-LayerNorm (Pre-LN) [4, 25]. Pre-LN stabilizes early training by normalizing
L106@P1: each sublayer’s input, preventing the divergence commonly seen in deep Post-LN networks [29]. However,
L107@P1: Pre-LN introduces its own structural limitations: it weakens gradient propagation and reduces the effective
L108@P1: contribution of deeper layers [17]. As models grow deeper, this results in poor depth scaling and representational
L109@P1: expressivity, limiting the potential of depth as a new scaling axis.
L110@P1: In contrast, Post-LN maintains large gradient signals in deeper layers, which can support superior depth
L111@P1: scaling. Yet its training instability has made it unsuitable for LLM-scale models. When the residual output
L112@P1: and transformed features are summed and then normalized, gradients in LayerNorm can exhibit extreme
L113@P1: variability, especially in deep regimes [29]. Previous attempts to revive Post-LN, such as DeepNorm [27],
L114@P1: Admin [15], and more recent hybrid normalization strategies [14, 35], mitigate some failure modes but do not
L115@P1: fundamentally resolve the gradient pathologies of Post-LN LLMs, nor do they demonstrate reliable behavior
L116@P1: at the depths needed to break the scaling limits of today.
L117@P1: To understand the root cause of these instabilities, we formally analyze the gradient dynamics of Post-LN. We
L118@P1: derive bounds on the backward signal and show that the ResNet-style residual path is the primary source
L119@P1: of gradient vanishing. These issues arise not from normalization itself, but from the way that residual and
L120@P1: transformed activations are mixed before normalization.
L121@P1: Motivated by this analysis, we consider a small yet impactful architectural change: replace the ResNet-style
L122@P1: residual branch with a simplified Highway-style connection, and re-express its gradient dynamics under the
L123@P1: same theoretical framework. Our results show that this Highway-style pathway provides provable control of
L124@P1: gradient magnitudes, allowing signals to propagate through depth without vanishing. Crucially, it maintains
L125@P1: the inter-layer coupling that makes Post-LN expressive, while suppressing the unstable mixing that previously
L126@P1: made Post-LN difficult to train.
L127@P1: Guided by these findings, we introduce Keel, a Post-LN architecture that incorporates a lightweight Highwaystyle gated connection [21]. The gate dynamically balances carry and transform signals, regulating both
L128@P1: forward and backward information flow. This simple modification stabilizes Post-LN at scale, enabling it to
L129@P1: realize its expressivity advantages without special initialization or customized residual scaling.
L130@P1: Empirically, Keel delivers substantial gains in depth scalability and model performance, effectively addressing
L131@P1: the training stability issues often associated with traditional deep architectures. By integrating a Highwaystyle pathway with a revived Post-LN configuration, Keel enables robust training at depths exceeding 1000
L132@P1: layers.1 While standard Post-LN or Pre-LN architectures often exhibit severe instability when subjected to
L133@P1: aggressive learning rates, Keel maintains smooth convergence, suggesting a more well-conditioned optimization
L134@P1: landscape.
L200@P3: • HybridNorm [35], which interleaves Post-LN and Pre-LN blocks throughout the network to blend their
L201@P3: respective optimization and expressivity properties,
L202@P3: • Mix-LN [14], which applies Post-LN in lower layers and transitions to Pre-LN in upper layers, aiming to
L203@P3: leverage stronger representational coupling at the bottom while retaining stability in deeper regions.
L204@P3: These hybrid designs provide improved robustness over pure Post-LN and can outperform pure Pre-LN in
L205@P3: certain regimes. However, they do not fundamentally resolve the gradient degeneration inherent to Post-LN
L206@P3: at very large depths, nor do they provide principled guarantees for stable scaling in the extreme-depth setting
L207@P3: required for future LLM architecture development.
L208@P3: 3 KEEL
L209@P3: We introduce Keel, a novel architecture designed to stabilize training in deep LLMs. The forward propagation
L210@P3: for the l-th layer is defined as:
L211@P3: xl+1 = LN (αxl + Fl(LN(xl))) (8)
L212@P3: Compared to the vanilla Post-LN architecture, our method incorporates two critical structural modifications.
L213@P3: Highway-style Residual Scaling: We introduce a scalar α to weight the skip connection, creating a highway-like
L214@P3: structure. Based on our gradient flow analysis (detailed in Section 3.3), we set α = L, where L represents the
L215@P3: total number of sub-layers (including both Attention and FFN layers)2. Unlike standard gating mechanisms
L216@P3: that require coefficients to sum to 1 (e.g., (1 − λ)x + λF(x)), we rely on the final Post-LN to normalize the
L217@P3: output magnitude, rendering explicit variance constraints on the summation unnecessary.
L218@P3: Residual Branch Normalization: We inject an additional Layer Normalization step into the input of the
L219@P3: residual function Fl. While this conceptually aligns the residual branch with a Pre-LN formulation (where
L220@P3: the input is normalized), the global architecture retains the Post-LN topology. As discussed in Section 4, this
L221@P3: additional normalization is crucial for stabilizing the gradient flow through the residual branch, preventing
L222@P3: the attenuation often seen in deep networks.
L223@P3: 2Setting α = L is critical for maintaining training stability in very large-scale or deep models. For smaller architectures where
L224@P3: vanishing or exploding gradients are less pronounced, α can be treated as a tunable hyperparameter (α > 1) to potentially
L225@P3: accelerate convergence.
L226@P3-4: 4Attn
L227@P4: Norm
L228@P4: FFN
L229@P4: Norm
L230@P4: Norm
L231@P4: Attn/FFN
L232@P4: Norm
L233@P4: α
L234@P4: 1st layer
L235@P4: x L-1
L236@P4: Norm
L237@P4: Figure 2 Illustration of our Keel architecture.
L238@P4: 3.1 Implementation Details
L239@P4: To ensure optimal performance and stability, we adopt the following implementation strategies for Keel.
L240@P4: Input Layer Initialization: As shown in Figure 2, for the very first attention and FFN layers, we remove the
L241@P4: final Post-LN and the scaling factor α. Consequently, they effectively degrade to standard Pre-LN blocks,
L242@P4: ensuring stable signal initialization from the embedding layer.
L243@P4: Hyperparameters: Empirically, Keel allows for and benefits from a larger learning rate compared to standard
L244@P4: Pre-LN baselines, accelerating convergence.
L245@P4: Normalization Configuration: All Layer Normalization operations utilize learnable affine weights (γ) but omit
L246@P4: the additive bias term (β = 0) to improve parameter efficiency and stability.
L247@P4: 3.2 Instability of Post-LN LLMs: A Gradient Perspective
L248@P4: We first define the operation of the RMS-based Layer Normalization (LN) used in the l-th layer. Given an
L249@P4: input vector x, the normalization is formulated as:
L250@P4: LN(x) = x
L251@P4: ∥x∥2
L252@P4: ⊙ γ, (9)
L253@P4: where ⊙ denotes element-wise multiplication, and γ ∈ R
L254@P4: d
L255@P4: is a learnable affine transformation parameter. We
L256@P4: define the scalar magnitude of this parameter as γ = ∥γ∥∞.
L257@P4: In a standard Post-LN architecture, the forward propagation of the l-th and (l + 1)-th sub-layers is formulated
L258@P4: as:
L259@P4: xl+1 = LNl (xl + Fl(xl)), (10)
L260@P4: xl = LNl−1 (xl−1 + Fl−1(xl−1)). (11)
L261@P4: Here, the residual connection is a simple summation. Let zl = xl + Fl(xl) denote the pre-normalization state.
L262@P4: During backpropagation, the gradient flows from the loss L through the layers via the chain rule:
L263@P4: ∂L
L264@P4: ∂xl
L265@P4: =
L266@P4: ∂L
L267@P4: ∂xl+1
L268@P4: ∂xl+1
L269@P4: ∂xl
L270@P4: . (12)
L271@P4-5: 5Expanding the Jacobian ∂xl+1
L272@P5: ∂xl
L273@P5: yields:
L274@P5: ∂xl+1
L275@P5: ∂xl
L276@P5: =
L277@P5: ∂ LNl(zl)
L278@P5: ∂zl
L279@P5: ∂zl
L280@P5: ∂xl
L281@P5: =
L282@P5: ∂ LNl(zl)
L283@P5: ∂zl
L284@P5: 
L285@P5: I +
L286@P5: ∂Fl
L287@P5: ∂xl
L288@P5: 
L289@P5: . (13)
L290@P5: Focusing on the gradient flow through the residual connection, the Jacobian magnitude is determined by the
L291@P5: normalization step. Consequently, the gradient magnitude satisfies:
L292@P5: J
L293@P5: ∗
L294@P5: LNl
L295@P5: (zl) =
L296@P5: 
L297@P5: 
L298@P5: 
L299@P5: 
L300@P5: 
L301@P5: 
L302@P5: 
L303@P5: 
L304@P5: ∂ LNl(zl)
L305@P5: ∂zl
L306@P5: 
L307@P5: 
L308@P5: 
L309@P5: 
L310@P5: 
L311@P5: 
L312@P5: 
L313@P5: 
L314@P5: 2
L315@P5: = O
L316@P5: 
L317@P5: γl
L318@P5: √
L319@P5: 2γl−1
L320@P5: 
L321@P5: . (14)
L322@P5: Typically, γ is initialized to 1. The cumulative gradient magnitude across L layers thus scales as:
L323@P5: Y
L324@P5: L
L325@P5: l=1
L326@P5: J
L327@P5: ∗
L328@P5: LNl,1
L329@P5: (zl) = O
L330@P5: 
L331@P5: 1
L332@P5: 2
L333@P5: L
L334@P5: 2
L335@P5: 
L336@P5: . (15)
L337@P5: This indicates that in standard Post-LN, the gradient signal exponentially decays as it propagates to lower
L338@P5: layers, hindering the training of deep models.
L339@P5: 3.3 KEEL: Stabilizing Deep LLMs
L340@P5: To mitigate this instability, Keel introduces a scaling factor α and an additional normalization step. The
L341@P5: forward pass is reformulated as:
L342@P5: xl+1 = LNl,1 (αxl + Fl(LNl,2(xl))), (16)
L343@P5: xl = LNl−1,1 (αxl−1 + Fl−1(LNl−1,2(xl−1))). (17)
L344@P5: With the reintroduction of α to scale the shortcut branch, the denominator in the gradient derivation changes.
L345@P5: The gradient magnitude through the l-th sub-layer’s residual connection satisfies:
L346@P5: J
L347@P5: ∗
L348@P5: LNl,1
L349@P5: (zl) = O
L350@P5: 
L351@P5: 
L352@P5: γl,1α
L353@P5: q
L354@P5: γ
L355@P5: 2
L356@P5: l−1,1α2 + γ
L357@P5: 2
L358@P5: l,2
L359@P5: 
L360@P5:  . (18)
L361@P5: We propose setting α = L. Analyzing the asymptotic behavior as L → ∞, we observe:
L362@P5: lim
L363@P5: L→∞
L364@P5: Y
L365@P5: L
L366@P5: l=1
L367@P5: J
L368@P5: ∗
L369@P5: LNl,1
L370@P5: (zl) = lim
L371@P5: L→∞ 
L372@P5: α
L373@P5: √
L374@P5: α2 + 1L
L375@P5: = lim
L376@P5: L→∞ "
L377@P5: 1 +
L378@P5: 1
L379@P5: L2
L380@P5: − L
L381@P5: 2
L382@P5: #
L383@P5: = 1. (19)
L384@P5: This limit confirms that our formulation prevents gradient vanishing.
L385@P5: 3.4 KEEL is a Post-LN Architecture
L386@P5: We classify Keel as a Post-LN architecture. Although Keel includes a normalization step inside the
L387@P5: transformation branch F (similar to Pre-LN), its structure is fundamentally Post-LN. This is because the
L388@P5: distinction between Pre-LN and Post-LN depends on the shortcut branch, not the input to the transformation
L389@P5: function.
L557@P8: long-context sequence recurrence can likely be adapted to develop infinite-depth model propagation, and vice
L558@P8: versa.
L559@P8: 5 Experiments
L560@P8: 5.1 Stability Analysis
L561@P8: We evaluate the training stability of Keel against a comprehensive suite of established normalization strategies.
L562@P8: Our baselines include the standard Post-LN and Pre-LN architectures, as well as recent variants designed for
L563@P8: stability: DeepNorm [27], and hybrid approaches such as HybridNorm [35] and Mix-LN [14].
L564@P8: Benchmark Protocol: Maximum Tolerable Learning Rate. To quantify stability, we measure the Maximum
L565@P8: Tolerable Learning Rate (Max LR). It is defined as the highest learning rate a model can sustain during
L566@P8: warm-up stage without diverging.
L567@P8: We adopt a stress-test protocol where the learning rate schedule is set with an aggressively high peak of
L568@P8: ηpeak = 5 × 10−2. The learning rate increases linearly from 0 to ηpeak over the warm-up period. We monitor
L569@P8: the training dynamics at every step; the learning rate recorded at the exact step immediately preceding
L570@P8: divergence is reported as the Max LR. A higher Max LR indicates a more robust optimization landscape and
L571@P8: superior training stability.
L572@P8: Criteria for Divergence. Identifying divergence in LLMs goes beyond simple numerical overflow (NaN). Based
L573@P8: on our observations, we categorize divergence into three distinct pathological behaviors:
L574@P8: 1. Loss Stagnation: The loss curve enters a plateau significantly earlier than expected, ceasing to decrease
L575@P8: despite continued training. This often indicates vanishing gradients or saturation in the normalization
L576@P8: layers.
L577@P8-9: 90 5000 10000 15000 20000
L578@P9: Step
L579@P9: 2
L580@P9: 4
L581@P9: 6
L582@P9: 8
L583@P9: 10
L584@P9: 12
L585@P9: Loss
L586@P9: converged
L587@P9: diverged
L588@P9: (a) Loss stagnation
L589@P9: 0 500 1000 1500 2000
L590@P9: Step
L591@P9: 4
L592@P9: 6
L593@P9: 8
L594@P9: 10
L595@P9: 12
L596@P9: Loss
L597@P9: converged
L598@P9: diverged
L599@P9: (b) Irrecoverable instability
L600@P9: 0 1000 2000 3000 4000 5000
L601@P9: Step
L602@P9: 2
L603@P9: 4
L604@P9: 6
L605@P9: 8
L606@P9: 10
L607@P9: 12
L608@P9: Loss
L609@P9: converged
L610@P9: diverged
L611@P9: (c) Optimization degradation
L612@P9: Figure 3 The illustration of three distinct pathological behaviors of model divergence in the training of LLMs.
L613@P9: Post-LN DeepNorm HybridNorm Mix-LN Pre-LN KEEL
L614@P9: Configuration A: 64 Layers, 5,000 Warm-ups, ηpeak = 5 × 10−2
L615@P9: Max LR 3.0 × 10−43.5 × 10−44.9 × 10−48.6 × 10−47.65 × 10−3 1.01 × 10−2
L616@P9: Configuration B: 512 Layers, 5,000 Warm-ups, ηpeak = 5 × 10−2
L617@P9: Max LR 2.8 × 10−43.5 × 10−43.5 × 10−43.5 × 10−44.67 × 10−3 6.31 × 10−3
L618@P9: Table 1 Comparison of Maximum Tolerable Learning Rates across different architectures. Keel consistently supports
L619@P9: higher learning rates, indicating superior training stability, particularly as model depth increases to 256 layers.
L620@P9: 2. Irrecoverable Instability: The loss exhibits high-magnitude spikes from which the model fails to recover.
L621@P9: Unlike transient spikes common in LLM training, these result in a permanent degradation of the loss
L622@P9: value (i.e., the loss never returns to the pre-spike baseline).
L623@P9: 3. Optimization Degradation: The model does not exhibit explicit spikes, and the loss continues to decrease.
L624@P9: However, the convergence rate is anomalously slow compared to a healthy baseline run. This “silent”
L625@P9: failure mode typically suggests that the effective update step size has been excessively dampened.
L626@P9: If a training run satisfies any of the above criteria, it is marked as diverged.
L627@P9: Results. Table 1 summarizes the stability limits across varying depths (64 and 512 layers). Keel demonstrates
L628@P9: a significant improvement in stability compared to all baselines.
L629@P9: Notably, in the 64-layer configuration, Keel tolerates a learning rate of 1.01 × 10−2, surpassing the standard
L630@P9: Pre-LN (7.65 × 10−3) and exceeding the vanilla Post-LN baseline by nearly two order of magnitude. This
L631@P9: trend holds for extremely deep networks: at 512 layers, Keel maintains a Max LR of 6.31 × 10−3, validating
L632@P9: our theoretical claims regarding training stability in deep architectures.
L633@P9: 5.2 Optimal Learning Rate
L634@P9: Having established the theoretical stability of Keel, we investigate its impact on downstream performance.
L635@P9: We hypothesize that the ability to tolerate larger learning rates is not merely a stability metric, but an
L636@P9: optimization advantage that allows the model to traverse the loss landscape more effectively and escape local
L637@P9: minima.
L638@P9: To verify this, we conducted a controlled sweep of peak learning rates (ηpeak ∈ {1.5, 3.0, 6.0} × 10−3) for both
L639@P9: the Pre-LN baseline and Keel. All models have 512 layers and a hidden dimension of 1024. We pre-train
L640@P9: these models with the same 250B tokens from the internal data. The learning rate linearly increases from 0 to
L641@P9: ηpeak over the first 2500 steps, then concludes with a cosine decay to 1.0 × 10−7.
L642@P9: As summarized in Table 2, the results reveal two critical optimization behaviors. The Pre-LN baseline exhibits
L643@P9-10: 100 250 500 750 1000 1250 1500
L644@P10: Step
L645@P10: 4
L646@P10: 6
L647@P10: 8
L648@P10: 10
L649@P10: 12
L650@P10: Loss
L651@P10: Peak LR = 4.5e-3
L652@P10: Peak LR = 3e-3
L653@P10: (a) 256 layers, batch size 8M
L654@P10: 0 500 1000 1500 2000 2500 3000
L655@P10: Step
L656@P10: 2
L657@P10: 4
L658@P10: 6
L659@P10: 8
L660@P10: 10
L661@P10: 12
L662@P10: Loss
L663@P10: Peak LR = 4.5e-3
L664@P10: Peak LR = 3e-3
L665@P10: (b) 512 layers, batch size 4M
L666@P10: Figure 4 Training loss curves of Pre-LN during the early stage of training. Pre-LN exhibits a pronounced loss spike
L667@P10: when trained with a higher learning rate.
L668@P10: performance saturation and instability at higher learning rates. While some tasks (e.g., MMLU) improve at
L669@P10: η = 6.0 × 10−3
L670@P10: , others suffer from degradation (e.g., ARC-Easy drops from 75.8 to 74.0; MBPP drops from
L671@P10: 25.0 to 22.8), suggesting that the model is oscillating in specific subspaces. In contrast, Keel demonstrates a
L672@P10: consistent, monotonic performance gain across all benchmarks as the learning rate increases. At η = 6.0×10−3,
L673@P10: Keel achieves a global average of 55.5, significantly outperforming the best Pre-LN configuration (52.3).
L674@P10: The benefits of stable, high-learning-rate training are most pronounced in reasoning-intensive tasks. On
L675@P10: GSM-8K, increasing the learning rate to 6.0 × 10−3 boosts Keel to 43.8, a massive improvement over the
L676@P10: Pre-LN baseline (38.1). This confirms that Keel effectively unlocks the optimization potential of large step
L677@P10: sizes without suffering from the gradient vanishing or instability typical of deep LLMs.
L678@P10: 5.3 Scalability Analysis: Performance at Depth Scaling
L679@P10: To validate the advantages of Keel in mitigating training instability, we conducted a comprehensive scaling
L680@P10: study. We compared Keel against the robust Pre-LN baseline across three distinct depth configurations: 64,
L681@P10: 128, 512 and 1024 layers. All models underwent a rigorous two-stage training protocol consisting of general
L682@P10: pre-training followed by continued pre-training (CPT).
L683@P10: Setup. We use a batch size of 1024 and a sequence length of 4096. All models are first pre-trained on 190B
L684@P10: tokens and then further pre-trained on an additional 60B tokens. We adopt the AdamW optimizer with
L685@P10: β1 = 0.9, β2 = 0.95, and a weight decay of 0.01. Gradient clipping is applied with a maximum norm of 1.0.
L686@P10: The learning rate schedule consists of a linear warmup over the first 2500 steps, followed by cosine decay
L687@P10: to 1.0 × 10−7. We set the peak learning rate to 9.0 × 10−3for the 64-layer and 128-layer models, and to
L688@P10: 6.0 × 10−3for the 512-layer models. For the 1024-layer models, we adopt a peak learning rate of 4.5 × 10−3for
L689@P10: Keel and 3.0 × 10−3for Pre-LN, as we observe that training 1024-layer Pre-LN models with a peak learning
L690@P10: rate of 4.5 × 10−3leads to substantial instability (see Figure 4b).
L691@P10: Results. Table 3 details the zero-shot and few-shot performance across a diverse suite of benchmarks. The
L692@P10: results reveal a clear trend: while Keel provides consistent gains at shallower depths (64L), its advantage
L693@P10: becomes significantly more pronounced as the model depth increases, maintaining strong scalability even at
L694@P10: 1024 layers.
L695@P10: • Reasoning Capabilities: On complex reasoning tasks like GSM-8K and HumanEval, the performance
L696@P10: gap widens dramatically at extreme depths. For instance, on GSM-8K, Keel achieves a score of 58.6
L697@P10: at 1024 layers, surpassing the 1024-layer Pre-LN baseline (49.8) by 8.8 points. Notably, the Pre-LN
L698@P10: baseline shows signs of stagnation between 512 and 1024 layers on several reasoning tasks, whereas
L699@P10-11: 11Benchmark Pre-LN KEEL
L700@P11: Peak LR (×10−3) 1.5 3.0 6.0 1.5 3.0 6.0
L701@P11: Common Sense & Knowledge
L702@P11: MMLU (5-shot) 47.5 48.1 52.9 49.8 53.5 56.3
L703@P11: ARC-Easy (25-shot) 75.8 75.3 74.0 74.5 76.4 77.1
L704@P11: ARC-Challenge (25-shot) 45.9 44.4 43.6 45.1 44.5 48.9
L705@P11: HellaSwag (0-shot) 64.2 64.2 64.9 64.3 65.5 67.4
L706@P11: LAMBADA (0-shot) 66.7 66.3 67.0 66.5 67.9 68.8
L707@P11: PIQA (0-shot) 75.6 75.5 75.1 76.3 75.8 76.7
L708@P11: AGI-Eval (0-shot) 29.3 29.7 34.7 30.5 34.6 39.6
L709@P11: Winogrande (0-shot) 64.1 64.2 63.5 63.8 64.5 65.7
L710@P11: CommonsenseQA (0-shot) 48.6 46.6 55.7 53.2 52.3 61.3
L711@P11: Reasoning & Coding
L712@P11: GSM-8K (5-shot) 30.3 31.1 38.1 30.5 36.6 43.8
L713@P11: HumanEval (0-shot) 14.0 17.7 17.7 14.6 18.3 19.5
L714@P11: MBPP (0-shot) 25.0 24.0 22.8 22.6 26.0 26.0
L715@P11: Multilingual Understanding
L716@P11: CMMLU (5-shot) 52.8 52.7 60.3 57.0 61.5 64.4
L717@P11: C-Eval (5-shot) 52.7 52.1 61.4 55.9 60.8 62.0
L718@P11: Average Score 49.5 49.4 52.3 50.5 52.7 55.5
L719@P11: Table 2 Performance scaling with Learning Rate. While Pre-LN results are inconsistent at high learning rates
L720@P11: (degrading on tasks like ARC-Easy and MBPP at η = 6.0 × 10−3), Keel exhibits robust, monotonic improvement,
L721@P11: effectively leveraging larger step sizes to achieve superior convergence.
L722@P11: Keel continues to yield significant gains.
L723@P11: • Global Average: The average performance improvement scales significantly with depth. Keel improves
L724@P11: over the baseline by approximately +1.7 points at 64 layers, +1.2 points at 128 layers, +3.8 points at
L725@P11: 512 layers, and +3.0 points at 1024 layers.
L726@P11: This empirical evidence confirms that Keel effectively stabilizes optimization in ultra-deep LLMs, unlocking
L727@P11: capabilities that are otherwise hindered by optimization difficulties or diminishing returns in standard
L728@P11: architectures.
L729@P11: 5.4 Scalability Analysis: Performance at Data Scaling
L730@P11: To assess the scalability of Keel with increasing training data, we compare it against Pre-LN across different
L731@P11: token budgets. We train Pre-LN and Keel on 10B and 40B tokens from the FineWeb-EDU dataset [16].
L732@P11: Both models have 256 layers and a hidden size of 1024, resulting up to 3B parameters. On the 10B-token run,
L733@P11: we tune the peak learning rate for both Keel and the Pre-LN baseline over {1.0, 1.5, 3.0, 4.5} × 10−3. The
L734@P11: batch size is set as 256. We use a maximum sequence length of 2048 for the 10B-token training and 4096 for
L735@P11: the 40B-token training. The learning rate schedule uses a 2000-step linear warmup followed by cosine decay.
L736@P11: Figure 5 presents the training loss curves of Keel and the baseline. As shown in Figure 5a, although Keel
L737@P11: exhibits higher loss early in training, it overtakes Pre-LN as training proceeds and achieves lower loss by
L738@P11: the end. More importantly, when scaling the training budget from 10B to 40B tokens, the performance gap
L739@P11-12: 12Benchmark
L740@P12: 64 Layers 128 Layers 512 Layers 1024 Layers
L741@P12: Pre-LN KEEL Pre-LN KEEL Pre-LN KEEL Pre-LN KEEL
L742@P12: Common Sense & Knowledge
L743@P12: MMLU (5-shot) 36.8 38.8 45.4 46.9 53.9 57.0 57.5 59.2
L744@P12: ARC-Easy (25-shot) 65.8 65.0 69.7 68.7 76.6 78.6 80.4 80.3
L745@P12: ARC-Challenge (25-shot) 33.7 33.6 38.7 37.8 45.5 50.4 51.1 51.7
L746@P12: HellaSwag (0-shot) 46.7 48.0 53.7 55.4 64.1 66.3 68.2 69.1
L747@P12: LAMBADA (0-shot) 51.5 52.9 57.7 59.0 65.1 67.5 68.8 70.0
L748@P12: PIQA (0-shot) 69.3 69.0 71.7 72.1 75.0 76.3 77.0 78.3
L749@P12: AGI-Eval (0-shot) 26.0 26.1 28.8 31.0 34.3 39.8 37.3 44.9
L750@P12: Winogrande (0-shot) 57.4 58.2 59.5 59.5 64.2 65.4 66.1 67.0
L751@P12: CommonsenseQA (0-shot) 31.4 37.8 48.2 49.1 60.0 65.8 60.6 67.1
L752@P12: Reasoning & Coding
L753@P12: GSM-8K (5-shot) 9.6 12.9 22.4 28.0 45.6 49.8 49.8 58.6
L754@P12: HumanEval (0-shot) 9.8 11.0 17.1 15.9 22.6 32.3 29.9 32.9
L755@P12: MBPP (0-shot) 13.0 13.2 20.8 22.2 32.0 34.2 36.2 38.6
L756@P12: Multilingual Understanding
L757@P12: CMMLU (5-shot) 39.3 43.4 50.1 52.7 61.0 65.0 64.9 67.0
L758@P12: C-Eval (5-shot) 40.3 44.6 50.0 53.1 60.6 64.9 63.2 67.3
L759@P12: Average Score 37.9 39.6 45.3 46.5 54.3 58.1 57.9 60.9
L760@P12: Table 3 Scalability Benchmark. Performance comparison between Pre-LN and Keel across increasing model depths
L761@P12: (64L, 128L, 512L, 1024L). The gain provided by Keel increases significantly with depth, particularly in reasoning-heavy
L762@P12: tasks (GSM-8K, HumanEval), highlighting the method’s effectiveness in stabilizing ultra-deep networks.
L763@P12: further widens in favor of Keel. As shown in Table 4, the accuracy on various end tasks also exhibits similar
L764@P12: trends: the improvement on HellaSwag increases from 0.9% to 2.6%. We attribute this to the lower effective
L765@P12: depth of Pre-LN relative to Keel, which limits its representational capacity. As the amount of training data
L766@P12: increases, the performance gain gradually plateaus. Overall, these results suggest that Keel is particularly
L767@P12: well suited for large-scale training, while its advantages are less pronounced in low-data regimes.
L768@P12: 5.5 Deeper vs. Wider
L769@P12: A fundamental question in neural scaling laws is the optimal allocation of a fixed parameter budget: is it
L770@P12: more effective to build deeper, narrower networks or shallower, wider ones? Theoretically, deeper networks
L771@P12: possess greater expressivity and reasoning depth. However, in practice, Wide topologies often outperform
L772@P12: Deep ones because deep networks are notoriously difficult to train.
L773@P12: To investigate whether Keel overcomes this optimization barrier, we conducted a controlled experiment with
L774@P12: a fixed parameter budget of 3B. We compare three configurations:
L775@P12: 1. Baseline Deep (Pre-LN): A standard deep topology (512 layers) which typically suffers from gradient
L776@P12: degradation.
L777@P12: 2. Baseline Wide (Pre-LN): A standard wide topology (128 layers, 2048 hidden size), representing the
L778@P12: industry standard for stability.
L779@P12: 3. Ours (Deep): The same deep topology (512 layers) augmented with Keel.
L780@P12-13: 130 5k 10k 15k 20k
L781@P13: Step
L782@P13: 2.6
L783@P13: 2.7
L784@P13: 2.8
L785@P13: 2.9
L786@P13: 3.0
L787@P13: Loss
L788@P13: Keel
L789@P13: Pre-LN
L790@P13: (a) 10B tokens, 512 layers
L791@P13: 0 10k 20k 30k 40k
L792@P13: Step
L793@P13: 2.4
L794@P13: 2.5
L795@P13: 2.6
L796@P13: 2.7
L797@P13: 2.8
L798@P13: Loss
L799@P13: Keel
L800@P13: Pre-LN
L801@P13: (b) 40B tokens, 512 layers
L802@P13: Figure 5 Training loss curves of Pre-LN and Keel on FineWeb-EDU dataset [16] with varying training tokens. As the
L803@P13: training token scales from 10B to 40B tokens, Keel achieves larger gain on training loss compared to Pre-LN baseline.
L804@P13: Models Best LR
L805@P13: (×10−3)
L806@P13: ARC-Easy
L807@P13: 25-shot
L808@P13: PIQA
L809@P13: 0-shot
L810@P13: HellaSwag
L811@P13: 0-shot
L812@P13: LAMBADA
L813@P13: 0-shot
L814@P13: Winogrande
L815@P13: 0-shot
L816@P13: SciQ
L817@P13: 0-shot Average
L818@P13: 10B tokens, 256 layers, 3B parameters
L819@P13: Pre-LN 1.5 56.9 72.7 52.9 50.0 52.6 76.1 60.3
L820@P13: Keel 3.0 58.8 73.4 53.8 49.6 56.0 78.1 61.5
L821@P13: 40B tokens, 256 layers, 3B parameters
L822@P13: Pre-LN 1.5 64.4 75.4 61.8 56.3 59.6 82.9 66.7
L823@P13: Keel 3.0 64.1 76.3 64.4 58.5 62.4 83.6 68.2
L824@P13: Table 4 Performance comparison between Pre-LN and Keel across increasing training data (10B, 40B) on FineWebEDU dataset [16].
L825@P13: We pre-train these models on 250B tokens of private data. We use a peak learning rate of 6.0 × 10−3for the
L826@P13: 512-layer models and 3.0×10−3for the 128-layer models. We set the AdamW β coefficients to (0.9, 0.95). The
L827@P13: batch size and sequence length are set to 1024 and 4096, respectively. We use a warmup phase of 2500 steps.
L828@P13: Results. Table 5 reports the results under a fixed budget of 3B parameters. We first compare the two Pre-LN
L829@P13: variants. Although the shallow-and-wide model achieves a lower training loss than the deep-and-narrow model
L830@P13: (see Appendix B), their average downstream scores are close. This discrepancy suggests that training loss is
L831@P13: not necessarily positively correlated with end-task performance, particularly when optimizing very deep LLMs.
L832@P13: Meanwhile, the deep-and-narrow model exhibits a consistent advantage on more complex reasoning-oriented
L833@P13: benchmarks (e.g., GSM-8K and MMLU), indicating that increasing depth has the potential to improve
L834@P13: complex reasoning when the model can be trained effectively.
L835@P13: Motivated by these observations, Keel targets the stability and degradation issues of deep modeling.
L836@P13: By stabilizing gradient flow and making deep training more reliable, Keel not only improves reasoning
L837@P13: performance beyond the deep Pre-LN baseline (e.g., 43.8 on GSM-8K vs. 38.1), but also achieves the best
L838@P13: overall performance: our 512-layer Keel model reaches an average score of 55.5, outperforming both the deep
L839@P13: Pre-LN baseline (+3.2) and the wide Pre-LN baseline (+3.3).
L840@P13-14: 14Configuration Deep (Pre-LN) Wide (Pre-LN) Deep (KEEL)
L841@P14: Parameters 3B 3B 3B
L842@P14: Layers 512 128 512
L843@P14: Hidden Dim 1024 2048 1024
L844@P14: Multilingual Understanding
L845@P14: CMMLU (5-shot) 60.3 59.3 64.4
L846@P14: C-Eval (5-shot) 61.4 57.8 62.0
L847@P14: General Knowledge & Commonsense
L848@P14: MMLU (5-shot) 52.9 51.5 56.3
L849@P14: ARC-Easy (25-shot) 74.0 75.2 77.1
L850@P14: ARC-Challenge (25-shot) 43.6 45.2 48.9
L851@P14: HellaSwag (0-shot) 64.9 65.9 67.4
L852@P14: LAMBADA (0-shot) 67.0 68.3 68.8
L853@P14: PIQA (0-shot) 75.1 76.3 76.7
L854@P14: AGI-Eval (0-shot) 34.7 36.1 39.6
L855@P14: Winogrande (0-shot) 63.5 65.5 65.7
L856@P14: CommonsenseQA (0-shot) 55.7 52.9 61.3
L857@P14: Math & Code
L858@P14: GSM-8K (5-shot) 38.1 35.3 43.8
L859@P14: HumanEval (0-shot) 17.7 16.5 19.5
L860@P14: MBPP (0-shot) 22.8 24.4 26.0
L861@P14: Average Score 52.3 52.2 55.5
L862@P14: Table 5 Deeper vs. Wider. Comparison of models with a fixed 3B parameter budget. While standard Deep models
L863@P14: underperform Wide ones due to optimization difficulties, Keel effectively stabilizes the deep network, allowing it to
L864@P14: outperform the Wide baseline significantly, particularly on reasoning-intensive tasks.
L865@P14: 5.6 Experimental Setup
L866@P14: To rigorously evaluate the scalability of our approach, we train a deep 512-layer LLM using the Keel
L867@P14: formulation and compare it against a standard Pre-LN baseline. Both models utilize a hidden dimension
L868@P14: of dmodel = 1024, resulting in an extreme depth-to-width ratio of 0.5 (512 layers vs. 1024 width). This
L869@P14: topology is specifically chosen to stress-test the optimization stability of deep networks where gradient signal
L870@P14: preservation is critical. Both models contain approximately 3 Billion parameters.
L871@P14: Models are trained on a massive corpus of 1T tokens from our internal dataset. The training pipeline proceeds
L872@P14: in two distinct phases: a general pre-training stage on the first 750B tokens, followed by continued pre-training
L873@P14: (CPT) on the remaining 250B tokens to enhance reasoning and coding capabilities. The optimization is
L874@P14: performed using AdamW with β1 = 0.9, β2 = 0.95, a weight decay of 0.01, a global batch size of 2048, and a
L875@P14: sequence length of 4096.
L876@P14: A critical differentiator in our setup is the learning rate schedule. We employ a linear warm-up over 2500 steps
L877@P14: followed by cosine decay. Keel remains robust at higher learning rates, while the Pre-LN baseline becomes
L878@P14: unstable, exhibiting pronounced loss spikes that force us to cap its peak rate at 3.0 × 10−3(see Figure 4a).
L879@P14: This stability allows us to train Keel at a significantly higher peak learning rate of 4.5 × 10−3, unlocking
L880@P14: superior convergence properties.
L881@P14: Following pre-training, both models undergo supervised fine-tuning (SFT) on a high-quality instruction mix.
L882@P14: We perform a comprehensive grid search over learning rates ({1.0, 2.0, 3.0} × 10−6) and training durations (1
L883@P14: to 3 epochs) to ensure that the reported results reflect the optimal capability of each architecture. We utilize
L884@P14: the lm-evaluation-harness [8] for standardized assessment across a broad suite of benchmarks spanning general
L885@P14-15: 15Configuration Pre-LN KEEL
L886@P15: Architecture 512 Layers / 3B Params 512 Layers / 3B Params
L887@P15: Peak Learning Rate 3.0 × 10−3 4.5 × 10−3
L888@P15: Multilingual Understanding
L889@P15: CMMLU (5-shot) 66.6 72.0
L890@P15: C-Eval (5-shot) 66.2 69.5
L891@P15: General Knowledge & Commonsense
L892@P15: MMLU (5-shot) 59.5 62.7
L893@P15: ARC-Easy (25-shot) 79.7 81.6
L894@P15: ARC-Challenge (25-shot) 51.6 53.6
L895@P15: HellaSwag (0-shot) 68.2 69.8
L896@P15: LAMBADA (0-shot) 68.0 69.7
L897@P15: PIQA (0-shot) 76.6 77.5
L898@P15: AGI-Eval (0-shot) 37.9 46.5
L899@P15: Winogrande (0-shot) 66.7 66.7
L900@P15: CommonsenseQA (0-shot) 64.5 69.8
L901@P15: Math & Code
L902@P15: GSM-8K (5-shot) 51.0 60.9
L903@P15: HumanEval (0-shot) 29.9 33.5
L904@P15: MBPP (0-shot) 35.0 40.6
L905@P15: Average Score 58.7 62.5
L906@P15: Table 6 Pre-training Results (1T Tokens). Comparison of a 512-layer Pre-LN baseline vs. Keel. Keel capitalizes
L907@P15: on its superior stability to train with a 50% higher learning rate, resulting in substantial gains across all categories,
L908@P15: particularly in reasoning-intensive tasks like GSM-8K and AGI-Eval.
L909@P15: knowledge [3, 6, 11, 18, 20, 23, 32, 34], reasoning [7], coding [1, 5], and multilingual understanding [12, 13].
L910@P15: 5.7 Main Results
L911@P15: Pre-training Performance. Table 6 summarizes the zero-shot and few-shot performance after the 1T token pretraining phase. Keel demonstrates a decisive advantage over the Pre-LN baseline, achieving a global average
L912@P15: improvement of +3.8 points (62.5 vs. 58.7). A deeper analysis reveals that while Keel provides consistent
L913@P15: gains across general knowledge tasks (e.g., MMLU, HellaSwag), the performance gap widens dramatically
L914@P15: on tasks requiring complex, multi-step reasoning. For instance, on the GSM-8K math benchmark, Keel
L915@P15: outperforms the baseline by nearly +10 points (60.9 vs. 51.0). Similarly, we observe significant improvements
L916@P15: in code generation, with MBPP and HumanEval scores increasing by +5.6 and +3.6 respectively. This
L917@P15: suggests that the improved gradient flow in Keel is particularly beneficial for learning the deep, hierarchical
L918@P15: representations necessary for algorithmic reasoning, rather than simple pattern matching.
L919@P15: Supervised Fine-Tuning (SFT) Results. We further investigate whether the advantages of Keel persist after
L920@P15: supervised fine-tuning. Table 7 presents the results on a suite of challenging benchmarks, including MMLU-Pro
L921@P15: and BBH (BIG-Bench Hard), which are designed to probe the limits of model capabilities. The results
L922@P15: confirm that the “pre-training advantage” is effectively transferred to the SFT stage. The performance delta in
L923@P15: reasoning tasks is preserved and, in some cases, amplified. On GSM-8K, the gap remains over 10 points (68.8
L924@P15: vs. 58.7), and on MMLU-Pro which requires nuanced understanding and robust instruction following, Keel

