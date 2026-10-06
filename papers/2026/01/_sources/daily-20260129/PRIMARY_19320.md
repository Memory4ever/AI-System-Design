# Exact v1 primary: 2601.19320

Raw primary excerpts, grouped by original tool response; physical lines distinguish local L-number resets.

## Original response: jan29_stdnext4head

StableQAT: Stable Quantization-Aware Training at Ultra-Low Bitwidths (https://arxiv.org/html/2601.19320v1)
citeturn28434view0 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19320v1","lineno":null}); Total lines: 721
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:     1. cite7†Forward-Backward Mismatch in QAT. L18:     2. cite8†1.1 Contributions L19:   3. cite9†2 Preliminary and Related Work L20:     1. cite10†2.1 Quantization L21:     2. cite11†2.2 Straight-Through Estimator (STE) L22:     3. cite12†2.3 Soft Surrogate Quantization L23:   4. cite13†3 StableQAT L24:     1. cite14†Backward Pass via RDFS: L25:     2. cite15†3.1 Rotated Damped Fourier Surrogate (RDFS) L26:       1. cite16†Coordinate Rotation. L27:       2. cite17†Fourier Approximation. L28:       3. cite18†Inverse Rotation. L29:     3. cite19†3.2 Damped Amplitude and Gradient Stabilization L30:       1. cite20†Role of Amplitude. L31:       2. cite21†Well-Conditioned Surrogate Region. L32:       3. cite22†Practical Amplitude Selection. L33:   5. cite23†4 Theoretical and Efficiency Analysis L34:     1. cite24†4.1 Theoretical Comparison with STE L35:     2. cite25†4.2 Theoretical Comparison with DSQ L36:     3. cite26†4.3 Efficiency Comparison L37:       1. cite27†Computational Efficiency: cosine vs. exp. L38:       2. cite28†RDFS is Fusion-Friendly. L39:       3. cite29†Negligible Computational Overhead. L40:   6. cite30†5 Experiments L41:     1. cite31†5.1 Large Language Model L42:       1. cite32†Experiment Setup. L43:       2. cite33†Results on LLaMA-3-1B. L44:       3. cite34†Results on LLaMA-3-3B. L45:     2. cite35†5.2 Training Stability Validation L46:       1. cite36†Gradient Dynamics and Convergence Behavior. L47:       2. cite37†Performance Error Bar. L48:     3. cite38†5.3 Ablation Studies L49:       1. cite39†Fourier Order of RDFS. L50:       2. cite40†Amplitude. L51:   7. cite41†6 Conclusion L52:   8. cite42†References L53:   9. cite43†A Related Work L54:   10. cite44†B Rotated Damped Fourier Surrogate Derivation L55:     1. cite45†Fourier series derivation. L56:     2. cite46†Rotation to the rounding function. L57:     3. cite47†Gradient surrogate derivation. L58:   11. cite48†C Proof of Theorem L59:   12. cite49†D Proof of Theorem L60:     1. cite50†DSQ details. L61:     2. cite51†DSQ Expectation. L62:     3. cite52†DSQ Variance. L63:     4. cite53†StableQAT Expectation. L64:     5. cite54†StableQAT Variance. L65:     6. cite55†StableQAT expectation limit. L66:     7. cite56†DSQ variance limit. L67:     8. cite57†StableQAT variance limit. L68: cite58†License: CC BY 4.0†info.arxiv.org L69: 
L70: arXiv:2601.19320v1 [cs.LG] 27 Jan 2026
L71: # StableQAT: Stable Quantization-Aware Training at Ultra-Low Bitwidths
L72: 
L73: Tianyi Chen Affiliation: Microsoft Correspondence to: Tianyi.Chen@microsoft.com    Sihan Chen Affiliation: Renmin University of China    Xiaoyi Qu Affiliation: Lehigh University    Dan Zhao Affiliation: New York University    Ruomei Yan Affiliation: Microsoft    Jongwoo Ko Affiliation: Microsoft    Luming Liang Affiliation: Microsoft    Pashmina Cameron Affiliation: Microsoft
L74: ###### Abstract
L75: Quantization-aware training (QAT) is essential for deploying large models under strict memory and latency constraints, yet achieving stable and robust optimization at ultra-low bitwidths remains challenging. Common approaches based on the straight-through estimator (STE) or soft quantizers often suffer from gradient mismatch, instability, or high computational overhead.
L76: As such, we propose StableQAT, a unified and efficient QAT framework that stabilizes training in ultra low-bit settings via a novel, lightweight, and theoretically grounded surrogate for backpropagation derived from a discrete Fourier analysis of the rounding operator.
L77: StableQAT strictly generalizes STE as the latter arises as a special case of our more expressive surrogate family, yielding smooth, bounded, and inexpensive gradients that improve QAT training performance and stability across various hyperparameter choices. In experiments, StableQAT exhibits stable and efficient QAT at 2-4 bit regimes, demonstrating improved training stability, robustness, and superior performance with negligible training overhead against standard QAT techniques.
L78: Our code is available at cite59†https://github.com/microsoft/StableQAT†github.com .
L79: ^{†}^{†}affiliationnotice: Equal contribution
L80: ## 1 Introduction
L81: Large language models (LLMs) are increasingly deployed under strict constraints on memory bandwidth, energy consumption, and hardware throughput, making full-precision inference impractical at scale. Quantization of weights and activations has therefore become a key technique for efficient deployment.
L82: Although post-training quantization (PTQ) achieves competitive accuracy at 8-bit precision, its performance degrades sharply below 4 bits due to the heterogeneous distributions (cite60†Ding et al., 2023 ), motivating the use of quantization-aware training (QAT) (cite61†Frantar et al., 2023 ; cite62†Xiao et al., 2023 ; cite63†Liu et al., 2024a ). QAT addresses this limitation by exposing models to quantization effects during training, allowing models to adapt to noise from discretization (cite64†Jacob et al., 2018 ).
L83: Quantization-aware training (QAT) exhibits increasing optimization fragility as target bitwidths decrease, with both stability and accuracy becoming difficult to maintain at and below 4-bit precision (cite65†Du et al., 2024b ; cite66†Panferov et al., 2025 ).
L84: Recent studies attribute this instability to multiple interacting factors, including outlier-dominated distributions, sensitivity to quantizer scaling and clipping, complex optimizer–quantization interactions, and the accumulation of approximation errors across layers (cite67†Choi et al., 2018 ; cite68†Esser et al., 2019 ).
L85: Although many methods attempt to mitigate these issues from different perspectives (cite69†Kundu et al., 2024 ; cite70†Chen et al., 2025 ), low-bit QAT remains unstable and often yields suboptimal performance. A key underlying reason is that existing approaches are unable to effectively resolve the fundamental mismatch between the discrete quantization process in the forward pass and continuous gradient-based optimization in the backward pass.
L86: Figure 1: StableQAT procedure.
L87: #### Forward-Backward Mismatch in QAT.
L88: A central challenge in QAT arises from the rounding operator. Exact quantization relies on hard rounding to map continuous values to discrete levels, yet the rounding function is non-differentiable and has zero gradient almost everywhere. To enable backpropagation, the straight-through estimator (STE) is commonly adopted as a surrogate (cite71†Bengio et al., 2013b ; cite72†Hubara et al., 2018 ).
L89: While STE makes QAT practically usable, it introduces a significant approximation error in the optimization direction, which often leads to unstable training, especially at low bitwidths.
L90: Recent approaches attempt to address this mismatch by introducing differentiable or stochastic relaxations of quantization, including noise-based training, soft rounding, and smooth approximations that gradually anneal toward discrete behavior (cite73†Gong et al., 2019 ; cite74†Zhong et al., 2023 ; cite75†Défossez et al., 2022 ; cite76†Huang et al., 2022 ; cite77†Semenov, 2025 ).
L91: Although these methods smoothen the optimization process, they typically incur additional computational overhead, introduce extra variance, or require careful scheduling to balance fidelity to discrete inference against optimization stability.
L92: ### 1.1 Contributions
L93: We introduce StableQAT, a simple but flexible and effective framework to address the optimization bottlenecks of QAT that can be seamlessly integrated into existing training pipelines. StableQAT introduces a rotated Fourier surrogate that models the rounding operator through its spectral structure, yielding a smooth and bounded optimization direction. As a result, StableQAT provides a theoretically grounded and computationally efficient plug-and-play solution to stabilize and boost QAT performance.
L94: Our main contributions are summarized as follows.
L95:   * •
L96: 
L97: Rotated Damped Fourier Surrogate (RDFS). We propose a novel surrogate for the quantization operator by modeling quantization via a Fourier analysis, applying a geometric rotation, and damping the amplitude, yielding a computationally efficient, smooth, bounded, and stable optimization behavior for QAT.
L98: 
L99:   * •
L100: Theoretical Analysis. We provide comprehensive theoretical insights into the properties of our proposed rotated fourier surrogate, including its approximation error and variance, revealing its advantages compared to STE and prior soft rounding alternatives.
L101: 
L102:   * •
L103: Robust Performance & Stability. Extensive experiments demonstrate that StableQAT achieves consistently improved training stability and LLM performance at 2-4 bit precision, without incurring additional computational overhead compared to standard QAT.
L104: Table 1: Qualitative comparison of QAT methods.
L105: Characteristic  | StableQAT  | DSQ  | ParetoQ
L106: Theoretically grounded surrogate  | ✓  | ✓  | ✗
L107: Computationally lightweight  | ✓  | ✗  | ✓
L108: Bounded gradient variance  | ✓  | ✗  | ✗
L109: Low-bit training & performance stability  | ✓  | ✗  | ✗
L110: ## 2 Preliminary and Related Work
L111: 
L112: This section reviews the necessary preliminaries and the most closely related works. Additional discussions on post-training quantization (PTQ) and other quantization-aware training (QAT) paradigms are deferred to Appendix cite43†A .
L113: ### 2.1 Quantization
L114: Quantization maps high-precision floating values (e.g., FP32 or FP16) into low-precision discrete representations (e.g., INT8 or INT4), thereby reducing memory footprint and inference-time computational cost. Given a floating-point variable ${x}_{\text{original}}$ (e.g., weights or activations) and a target bit-width $b$, a quantizer maps ${x}_{\text{original}}$ to an integer domain $[q_{\min},q_{\max}]$.
L115: For signed quantization, the range is typically $[-2^{b-1},2^{b-1}-1]$, and becomes $[0,2^{b}-1]$ for unsigned quantization.
L116: The quantization process is parameterized by a scaling factor $s\in\mathbb{R}^{+}$ and a zero-point $z\in\mathbb{Z}$, and is defined as:
L117: 
L118:  | $$\begin{split}{x}_{q}&=\mathrm{clip}\left(\mathrm{round}({x}_{\text{original}}/s)+z,q_{\min},q_{\max}\right)\\
L119: &=\mathrm{clip}\left(\mathrm{round}({x})+z,q_{\min},q_{\max}\right),\end{split}$$  |  | (1)
L120: where $\mathrm{round}(\cdot)$ denotes the round-to-nearest-integer operator, and $\mathrm{clip}(v,a,b)=\min(\max(v,a),b)$ enforces the feasible range constraint. We denote ${x}\triangleq{x}_{\text{original}}/s$ for simplicity of notations. Here, the scaling factor $s$ (also referred to as the quantization step size) determines the quantization resolution, while the zero-point $z$ controls the alignment between the floating-point and integer domains.
L121: Without loss of generality, we assume $z=0$ throughout the remainder of this paper for notational simplicity. We note that our analysis remains valid for for arbitrary $z$.
L122: ### 2.2 Straight-Through Estimator (STE)
L123: 
L124: Training quantized networks poses a fundamental optimization challenge due to the non-differentiability of the rounding operation in Eq. (cite78†1 ). In particular, the rounding function has zero derivative almost everywhere and is undefined at integer transition points. As a result, its first-order derivative carries no informative signal, causing standard backpropagation to fail with ineffective parameter updates under gradient-based optimization.
L125: To address this, the Straight-Through-Estimator (STE) (cite79†Bengio et al., 2013a ) has been widely adopted to provide a surrogate to the derivative. STE simply ignores the rounding operation during the backward pass and approximates the differential of the quantized value ${x}_{q}$ with respect to the input ${x}$ as an identity function. More formally, let $\mathcal{L}$ denote the task loss. The derivative of the loss with respect to the pre-quantized input ${x}$ is then approximated by STE as:
L126:  | $$\frac{\partial\mathcal{L}}{\partial{x}}=\frac{\partial\mathcal{L}}{\partial{x}_{q}}\cdot{\fcolorbox{black}{white}{$\displaystyle\frac{\partial{x}_q}{\partial{x}}
L127: $}}_{\hskip 0.81949pt\text{STE}}\approx\frac{\partial\mathcal{L}}{\partial{x}_{q}},$$  |  | (2)
L128: where the true derivative $\partial{x}_{q}/\partial{x}$ is replaced by an identity surrogate. Although STE makes QAT practically feasible, it introduces substantial gradient mismatch due to the large deviation between the straight-through surrogate and the rounding operator. This mismatch injects significant optimization noise, leading to biased and unstable gradient updates, impaired convergence behavior, and ultimately sub-optimal performance, especially at ultra-low bitwidths.
L129: ### 2.3 Soft Surrogate Quantization
L130: 
L131: Soft surrogate quantization methods more directly target the rounding operation by introducing continuous relaxations. DSQ (cite73†Gong et al., 2019 ) is a representative approach that employs a parameterized tanh function whose sharpness is gradually increased during training. More recent work (cite77†Semenov, 2025 ) utilizes a sigmoid function to smooth the rounding operator in cite78†Equation 1 .
L132: While these approaches capture richer structural information of the quantization process, they still suffer from the inherently ill-conditioned optimization landscape induced by the rounding operator. Moreover, they rely on computationally expensive exp-based functions, significantly slowing down training, typically by 3$\times$–5$\times$ in both forward and backward passes (see cite80†Figure 5 ).
L133: Other soft quantization methods introduce additional relaxation regularizers; however, they continue to face similar optimization challenges stemming from the underlying rounding behavior.
L134: ## 3 StableQAT
L135: StableQAT is a simple QAT framework that addresses the critical forward-backward mismatch challenges of low-bit optimization. StableQAT achieves improved training stability and higher performance without incurring additional computational cost. At its core, StableQAT is built upon a Rotated Damped Fourier Surrogate (RDFS) of the quantization operator.
L136: The key idea is to model the discrete quantization process via a Fourier series and to derive a smooth, analytically grounded surrogate for backpropagation through a geometric rotation of this representation. This construction yields a stable and well-behaved optimization direction for gradient-based training.
L137: #### Backward Pass via RDFS:
L138: 
L139: As illustrated in cite81†Figure 2 , we approximate the rounding operator using a Rotated Damped Fourier Surrogate (RDFS). By preserving richer structural information of the rounding operation, RDFS provides more informative learning signals while addressing the ill-defined Jacobian $\partial{x}_{q}/\partial{x}$, thereby stabilizing and improving gradient-based QAT. Formally, the derivative with respect to the input ${x}$ is computed by RDFS as:
L140:  | $$\frac{\partial\mathcal{L}}{\partial{x}}=\frac{\partial\mathcal{L}}{\partial{x}_{q}}\cdot{\fcolorbox{StableBlueStrong}{white}{$\displaystyle\frac{\partial{x}_q}{\partial{x}}$}}_{\hskip 0.81949pt\text{{\color[rgb]{0.1172,0.4297,0.707}RDFS}}}\approx\frac{\partial\mathcal{L}}{\partial{x}_{q}}\cdot g({x},{x}_{q}),$$  |  | (3)
L141: 
L142: where our proposed rotated Fourier surrogate $g({x},{x}_{q})$ is defined as:
L143:  | $$g({x},{x}_{q})=\frac{1-A\sqrt{2}\pi\sum_{m=0}^{M}\frac{(-1)^{m}}{2m+1}\cos\!\big((2m+1)\pi({x}+{x}_{q})\big)}{1+A\sqrt{2}\pi\sum_{m=0}^{M}\frac{(-1)^{m}}{2m+1}\cos\!\big((2m+1)\pi({x}+{x}_{q})\big)}.$$  |  | (4)
L144: 
L145: In practice, we truncate the series and typically use the first-order RDFS (i.e., $M=0$):
L146: 
L147:  | $$\fcolorbox{StableBlueStrong}{white}{$\displaystyle g(x,x_q)=
L148: \frac{1 - A\sqrt{2}\pi\cos\!\big(\pi(x+x_q)\big)}
L149: {1 + A\sqrt{2}\pi\cos\!\big(\pi(x+x_q)\big)}
L150: $}.$$  |  | (5)
L151: Here, $A$ is a tunable hyperparameter controlling the sharpness of the surrogate. The derivation, based on a geometric rotation and Fourier analysis, is provided in the following.
L152: STE as a Special Case of RDFS. Note that $A=0$, the RDFS degenerates to identity mapping, which exactly becomes the Straight-Through Estimator (STE). It shows that STE is a special case of RDFS, and highlights the increased generality of RDFS, revealing that the potential of RDFS to carry-out richer structural information leading towards stronger convergence and better performance.
L153: ### 3.1 Rotated Damped Fourier Surrogate (RDFS)
L154: 
L155: Figure 2: Rotated Damped Fourier Surrogate (RDFS) under different orders and amplitudes.
L156: #### Coordinate Rotation.
L157: 
L158: We observe that applying a $45^{\circ}$ counterclockwise rotation to the coordinate system $(x,x_{q})$ transforms the staircase-shaped rounding operator into a periodic, continuous, piecewise-linear function, commonly referred to as a triangle wave function, shown in cite81†Figure 2 .
L159: More formally, we introduce a rotated coordinate system $(t,f(t))$ obtained by rotating the original coordinates $(x,x_{q})$ by an angle $\theta=45^{\circ}$ counterclockwise. The resulting coordinates are given by
L160: 
L161:  | $$t=\frac{x+x_{q}}{\sqrt{2}},\quad f(t)=\frac{-x+x_{q}}{\sqrt{2}}.$$  |  | (6)
L162: Under the rotated coordinate system, the rounding operator becomes a periodic zig-zag function with fundamental period $T=\sqrt{2}$. Specifically, the transformed function can be expressed as a centered triangle wave:
L163: 
L164:  | $$f(t)=\frac{1}{2\sqrt{2}}\left(1-4\left|r(t)-\frac{1}{2}\right|\right),$$  |  | (7)
L165: where $r(t)=\left\{\frac{t-T/4}{T}\right\}$ denotes the phase-shifted fractional part operator, and $\{\cdot\}$ extracts the fractional component by discarding the integer part. The phase shift $T/4$ centers the triangle wave symmetrically around zero, which will be convenient for subsequent Fourier analysis.
L166: #### Fourier Approximation.
L167: 
L168: Since the rotated rounding function $f(t)$ is periodic and square-integrable, it admits a Fourier series expansion. Applying the Fourier transformation on cite82†Equation 7 , we obtain the following closed-form Fourier approximation:
L169: 
L170:  | $$\begin{split}f(t)&\approx-A\sum_{m=0}^{\infty}\frac{(-1)^{m}}{(2m+1)^{2}}\sin\!\left((2m+1)\sqrt{2}\pi\,t\right),\end{split}$$  |  | (8)
L171: where $(2m+1)\sqrt{2}\pi$ denotes the angular frequency of the $m$-th sinusoid term. The scalar $A$ is an amplitude coefficient, as illustrated in cite81†Figure 2 , which controls the sharpness of the resulting curve. Notably, instead of fixing $A$ to the vanilla Fourier amplitude $A=2\sqrt{2}/\pi^{2}$, we treat it as a tunable parameter.
L172: An appropriate choice of $A$ can yield improved training stability and optimization behavior, whereas an improper choice may lead to gradient vanishing or explosion; see Section cite19†3.2 for a detailed discussion.
L173: We further consider a truncated Fourier approximation as
L174: 
L175:  | $$f_{M}(t)=-A\sum_{m=0}^{M}\frac{(-1)^{m}}{(2m+1)^{2}}\sin\!\left((2m+1)\sqrt{2}\pi\,t\right),$$  |  | (9)
L176: 
L177: where $M$ refers to the order of Fourier approximation. Higher-order terms encode finer structural details of the rounding operator but incur increasing computational cost.
L178: #### Inverse Rotation.
L179: 
L180: To employ the rotated Fourier approximation as a gradient surrogate, we map the smooth function $f(t)$ back to the original coordinates $(x,x_{q})$. Based on the coordinate transformation in (cite83†6 ), the Fourier expansion of $f(t)$, and the chain rule, the general form of the rotated damped Fourier surrogate (RDFS) for the rounding operator can be expressed as
L181:  | $$\frac{\partial x_{q}}{\partial x}=\frac{1-A\sqrt{2}\pi\sum_{m=0}^{M}\frac{(-1)^{m}}{2m+1}\cos\!\left((2m+1)\pi(x+x_{q})\right)}{1+A\sqrt{2}\pi\sum_{m=0}^{M}\frac{(-1)^{m}}{2m+1}\cos\!\left((2m+1)\pi(x+x_{q})\right)}.$$  |  | (10)
L182: In practice, we retain only the first-order term ($M=0$), which provides an effective trade-off between approximation fidelity and negligible computational overhead. Under this setting, the RDFS in cite84†Equation 10 reduces to its first-order form as cite85†Equation 5 . A complete derivation of the RDFS is provided in Appendix cite44†B .
L183: ### 3.2 Damped Amplitude and Gradient Stabilization
L184: 
L185: The choice of the amplitude parameter $A$ requires careful consideration, as it directly governs the trade-off between approximation fidelity and optimization stability.
L186: #### Role of Amplitude.
L187: The amplitude $A$ controls the sharpness of the rotated Fourier surrogate and determines how closely it approximates the true rounding operator. When $A$ is small (approaching the STE case as $A\to 0$), the surrogate is overly smooth, which weakens its ability to capture the fine-grained structure of rounding and leads to biased or ineffective gradient signals.
L188: Increasing $A$ (while remaining within the admissible range implied by the Fourier construction) improves approximation accuracy by bringing the surrogate closer to hard rounding. However, as the surrogate sharpens, it progressively inherits the pathological optimization behavior of the true rounding operator: gradients vanish over large regions and become highly unstable in the vicinity of discontinuities, resulting in gradient vanishing or explosion.
L189: This intrinsic trade-off motivates the use of a damped amplitude that balances expressiveness and numerical stability.
L190: #### Well-Conditioned Surrogate Region.
L191: Our analysis reveals the existence of an ill-conditioned amplitude regime in which the rotated Fourier surrogate becomes nearly tangential to horizontal plateaus as $A$ approaches $1/(\sqrt{2}\pi)$, leading to severely attenuated gradients. To avoid this failure mode, our design explicitly excludes this region.
L192: As shown in the amplitude sensitivity study in cite86†Figure 8 , this ill-conditioned regime manifests as a pronounced performance “well” in empirical results, which closely aligns with the theoretical conditioning analysis. This consistency between theory and observation provides strong evidence that an proper amplitude choice can fundamentally improve optimization gain and avoid potential instability.
L193: #### Practical Amplitude Selection.
L194: Although Fourier analysis suggests a theoretically admissible amplitude of $A=\tfrac{2\sqrt{2}}{\pi^{2}}$, strictly adhering to this value is suboptimal in practice for large-scale LLM training due to the aforementioned conditioning issues. We therefore treat $A$ as a damped and tunable parameter.
L195: In all experiments, we select a default value of $A=0.21$, which lies safely outside the ill-conditioned regime while still capturing sufficient structural information of the rounding operator to yield effective gradient signals. This choice provides a stable and robust operating point across models and training settings.
L196: While more sophisticated strategies such as dynamically evolving $A$ during training, may further improve performance, we leave such curriculum-based designs as an interesting direction for future work.
L197: ## 4 Theoretical and Efficiency Analysis
L198: 
L199: ### 4.1 Theoretical Comparison with STE
L200: 
L201: We compare STE and StableQAT using surrogate approximations of the rotated rounding function (cite82†7 ). By periodicity, we may focus on a single period $[0,T]$ without loss of generality. As the rotated function is square-integrable, we conduct our analysis in the space $L^{2}([0,T])$.
L202: ###### Theorem 4.1.
L203: 
L204: Let $f\in L^{2}([0,T])$ and let $f_{n}$ be the $n$th partial Fourier sum of $f$. Then, for all $n\in\mathbb{N}$,
L205: (i) $f_{n}$ is the unique minimizer of the $L^{2}$ approximation error among trigonometric polynomials of degree at most $n$;
L206: (ii) For $n\geq 1$, $\|f-f_{n}\|_{2}<\|f-f_{0}\|_{2}$ if and only if $f$ is non-constant almost everywhere.
L207: ###### Proof.
L208: 
L209: See Appendix cite48†C . ∎
L210: 
L211: Remark I. Theorem cite87†4.1 (i) implies that the $n$th partial Fourier sum is the optimal $L^{2}$ surrogate of the rotated rounding function among trigonometric polynomials of degree at most $n$. For STE, the surrogate is restricted to constant functions. In contrast, StableQAT admits surrogates from trigonometric polynomials of degree at most $n\in\mathbb{N}$, making STE a special case of StableQAT with $n=0$.
L212: Remark II. Theorem cite87†4.1 (ii) implies that, unless the function is constant almost everywhere, its surrogate drawn from trigonometric polynomials of degree at least 1 achieves a strictly smaller $L^{2}$ approximation error than those restricted to constant functions. Consequently, StableQAT admits surrogate functions that are provably closer to the rotated rounding function than STE in the $L^{2}$ sense.
L213: ### 4.2 Theoretical Comparison with DSQ
L214: 
L215: We then compare DSQ and StableQAT in terms of gradient stability by analyzing the statistical properties of their surrogate gradients under uniform sampling over the clipping range. Our analysis focuses on the asymptotic regime in which the surrogate function closely approximates the rounding function. Such setting is particularly relevant for low-bit QAT (2–4 bits), where accurately capturing discrete quantization effects is critical.
L216: ###### Theorem 4.2.
L217: 
L218: Let $g_{\mathrm{DSQ}}(\cdot;\alpha)$ and $g_{\emph{StableQAT{}}}(\cdot;A)$ be the gradient surrogates of DSQ and StableQAT, parameterized by $\alpha>0$ and $A\in(0,\frac{1}{\sqrt{2}\pi})$, respectively. Let random variable $\xi$ be uniformly distributed on the interval $[l,u]$, i.e., $\xi\sim U(l,u)$. Consider the asymptotic regimes in which the surrogate functions move close to the rounding function. Then, the limits of the expectations satisfy
L219:  | $\displaystyle\lim_{\alpha\to 0^{+}}\mathbb{E}_{\xi\sim U(l,u)}\!\left[g_{\mathrm{DSQ}}(\xi;\alpha)\right]$  | $\displaystyle=1,$  |
L220:  | $\displaystyle\lim_{A\to\left(\frac{1}{\sqrt{2}\pi}\right)^{-}}\mathbb{E}_{\xi\sim U(l,u)}\!\left[g_{\emph{StableQAT{}}}(\xi;A)\right]$  | $\displaystyle=\frac{4}{\pi}-1,$  |
L221: 
L222: and the limits of the variances satisfy
L223:  | $\displaystyle\lim_{\alpha\to 0^{+}}\mathrm{Var}_{\xi\sim U(l,u)}\!\left[g_{\emph{DSQ}}(\xi;\alpha)\right]$  | $\displaystyle=\infty,$  |
L224:  | $\displaystyle\lim_{A\to\left(\frac{1}{\sqrt{2}\pi}\right)^{-}}\mathrm{Var}_{\xi\sim U(l,u)}\!\left[g_{\emph{StableQAT{}}}(\xi;A)\right]$  | $\displaystyle=\frac{16}{3\pi}-\frac{16}{\pi^{2}}.$  |
L225: ###### Proof.
L226: 
L227: See Appendix cite49†D . ∎
L228: 
L229: Remark I. In Theorem cite88†4.2 , $g_{\emph{StableQAT{}}}(\cdot;A)$ is derived using the first-order Fourier partial sum of the rotated rounding function. Although StableQAT allows higher-order Fourier partial sums, we focus on the first-order case as it is the variant used in our experiments and suffices to reveal the differences in gradient stability.
L230: Remark II. Theorem cite88†4.2 shows that DSQ’s gradient variance diverges as it sharpens towards the rounding function, whereas the periodic structure of StableQAT maintains bounded variance ($\approx 0.076$) at maximum sharpness. This distinction directly impacts training stability: bounded variance ensures consistent gradient magnitudes, while divergent variance may cause gradient explosion. Thus, gradient stability is a key advantage of StableQAT over DSQ in low-bit QAT regimes.
L231: cite89†Image: Refer to caption Figure 3: Gradient spread of DSQ and StableQAT. As the surrogate sharpens toward rounding operator, DSQ exhibits exploding variance, while StableQAT shows bounded variance.
L232: ### 4.3 Efficiency Comparison
L233: 
L234: We further show that RDFS achieves nearly identical computational efficiency to STE, while being several times faster and more lightweight than DSQ. This makes StableQAT a plug-and-play surrogate for a wide range of QAT pipelines, providing consistent performance gains without additional computational or memory cost.
L235: #### Computational Efficiency: cosine vs. exp.
L236: 
L237: Soft quantization methods such as DSQ (cite73†Gong et al., 2019 ) and SigmoidQuant (cite77†Semenov, 2025 ) approximate rounding using sigmoid or tanh, which rely on expensive exponential evaluations. On modern hardwares, exp typically requires high-order polynomial approximation, and numerical-stability handling, leading to high latency and register pressure (cite90†Muller et al., 2018 ; cite91†NVIDIA, 2024 ).
L238: In contrast, trigonometric functions like cosine and sine operate on bounded inputs, admit lower-degree polynomial approximations, and avoid saturation handling. Consequently, RDFS exhibits lower and more predictable execution cost, which is especially beneficial in QAT where surrogate gradients are repeatedly evaluated.
L239: #### RDFS is Fusion-Friendly.

## Original response: jan29_stdnext4core

StableQAT: Stable Quantization-Aware Training at Ultra-Low Bitwidths (https://arxiv.org/html/2601.19320v1)
citeturn28435view0 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"turn28434view0","lineno":239}); Total lines: 721
L223:  | $\displaystyle\lim_{\alpha\to 0^{+}}\mathrm{Var}_{\xi\sim U(l,u)}\!\left[g_{\emph{DSQ}}(\xi;\alpha)\right]$  | $\displaystyle=\infty,$  |
L225: ###### Proof.
L226: 
L227: See Appendix cite49†D . ∎
L228: 
L229: Remark I. In Theorem cite88†4.2 , $g_{\emph{StableQAT{}}}(\cdot;A)$ is derived using the first-order Fourier partial sum of the rotated rounding function. Although StableQAT allows higher-order Fourier partial sums, we focus on the first-order case as it is the variant used in our experiments and suffices to reveal the differences in gradient stability.
L230: Remark II. Theorem cite88†4.2 shows that DSQ’s gradient variance diverges as it sharpens towards the rounding function, whereas the periodic structure of StableQAT maintains bounded variance ($\approx 0.076$) at maximum sharpness. This distinction directly impacts training stability: bounded variance ensures consistent gradient magnitudes, while divergent variance may cause gradient explosion. Thus, gradient stability is a key advantage of StableQAT over DSQ in low-bit QAT regimes.
L231: cite89†Image: Refer to caption Figure 3: Gradient spread of DSQ and StableQAT. As the surrogate sharpens toward rounding operator, DSQ exhibits exploding variance, while StableQAT shows bounded variance.
L232: ### 4.3 Efficiency Comparison
L233: 
L234: We further show that RDFS achieves nearly identical computational efficiency to STE, while being several times faster and more lightweight than DSQ. This makes StableQAT a plug-and-play surrogate for a wide range of QAT pipelines, providing consistent performance gains without additional computational or memory cost.
L235: #### Computational Efficiency: cosine vs. exp.
L236: 
L237: Soft quantization methods such as DSQ (cite73†Gong et al., 2019 ) and SigmoidQuant (cite77†Semenov, 2025 ) approximate rounding using sigmoid or tanh, which rely on expensive exponential evaluations. On modern hardwares, exp typically requires high-order polynomial approximation, and numerical-stability handling, leading to high latency and register pressure (cite90†Muller et al., 2018 ; cite91†NVIDIA, 2024 ).
L238: In contrast, trigonometric functions like cosine and sine operate on bounded inputs, admit lower-degree polynomial approximations, and avoid saturation handling. Consequently, RDFS exhibits lower and more predictable execution cost, which is especially beneficial in QAT where surrogate gradients are repeatedly evaluated.
L239: #### RDFS is Fusion-Friendly.
L240: 
L241: RDFS consists only of elementary arithmetic and a single trigonometric operation, without auxiliary states or annealing schedules. Its low register footprint and branch-free structure make it well suited for kernel fusion in modern deep learning runtimes, e.g., PyTorch (cite92†Imambi et al., 2021 ), CUDA (cite91†NVIDIA, 2024 ), and Triton (cite93†Tillet et al., 2019 ).
L242: #### Negligible Computational Overhead.
L243: 
L244: We benchmark RDFS on LLaMA-3-1B with batch size 4 and sequence length 128. As shown in cite94†Figure 4 , StableQAT matches STE in backward-pass latency and memory usage, while being up to $5\times$ more efficient than exp-based surrogate like DSQ.
L245: 
L246: cite95†Image: Refer to caption Figure 4: Time and space cost comparison (lower is better). They are measured on an input tensor with batch size 4 and sequence length 128. Each method is repeated 20 times.
L247: ## 5 Experiments
L248: 
L249: We comprehensively evaluate StableQAT from three complementary perspectives: (i) model performance, (ii) training stability, and (iii) ablation studies that reveal the impact of key design choices. Our experiments span both Large Language Models (LLMs) and Vision Transformers (ViTs) in Appendix , demonstrating the generality, effectiveness, and robustness of StableQAT across scenarios.
L250: ### 5.1 Large Language Model
L251: 
L252: Table 2: LLaMA-3.2-1B results. StableQAT at 4-bit outperforms the 16-bit baseline, while 3-bit StableQAT remains competitive.
L253: Bits  | Method  | Setting  | Arc-e  | Arc-c  | Boolq  | Hellaswag  | Openbookqa  | Piqa  | SciQ  | Winogrande  | Avg  | $\Delta$
L254: 16  | Baseline  | Baseline  | 60.61  | 36.01  | 63.70  | 63.78  | 36.60  | 74.43  | 88.40  | 60.06  | 60.45  | –
L255: 4  | Baseline no QAT  | Baseline no QAT  | 43.31  | 27.05  | 52.57  | 46.75  | 31.20  | 65.83  | 78.00  | 53.12  | 49.73  | –
L256: 4  | ParetoQ  | 10B Tokens & lr=1e-5  | 59.89  | 30.97  | 59.27  | 56.07  | 34.40  | 71.65  | 88.80  | 56.83  | 57.24  | –
L257: 4  | DSQ  | 10B Tokens & lr=1e-5  | 55.01  | 31.66  | 61.16  | 55.75  | 34.20  | 71.87  | 86.00  | 56.27  | 56.49  | –
L258: 4  | StableQAT  | 10B Tokens & lr=1e-5  | 60.48  | 32.17  | 62.02  | 56.54  | 32.60  | 72.63  | 89.60  | 56.91  | 57.87  | +1.38
L259: 4  | ParetoQ  | 20B Tokens & lr=1e-4  | 65.49  | 36.86  | 63.82  | 61.22  | 39.40  | 74.70  | 86.70  | 59.51  | 60.96  | –
L260: 4  | DSQ  | 20B Tokens & lr=1e-4  | 65.45  | 37.37  | 63.73  | 62.04  | 39.40  | 74.16  | 86.40  | 59.98  | 61.07  | –
L261: 4  | StableQAT  | 20B Tokens & lr=1e-4  | 65.74  | 37.54  | 64.01  | 61.15  | 40.00  | 74.59  | 86.4  | 60.46  | 61.24  | +0.25
L262: 3  | Baseline no QAT  | Baseline no QAT  | 24.74  | 26.30  | 40.64  | 26.11  | 29.00  | 50.49  | 24.90  | 48.30  | 33.81  | –
L263: 3  | ParetoQ  | 10B Tokens & lr=1e-5  | 30.85  | 22.10  | 48.53  | 29.19  | 27.80  | 55.33  | 50.30  | 47.28  | 38.92  | –
L264: 3  | DSQ  | 10B Tokens & lr=1e-5  | 29.88  | 23.63  | 46.27  | 29.31  | 28.00  | 53.86  | 46.90  | 48.54  | 38.30  | –
L265: 3  | StableQAT  | 10B Tokens & lr=1e-5  | 38.55  | 23.98  | 59.24  | 33.14  | 27.00  | 59.63  | 67.70  | 52.17  | 45.18  | +6.88
L266: 3  | ParetoQ  | 20B Tokens & lr=2e-4  | 35.69  | 64.24  | 61.23  | 58.91  | 37.40  | 73.32  | 87.50  | 58.27  | 59.57  | –
L267: 3  | DSQ  | 20B Tokens & lr=2e-4  | 32.85  | 60.77  | 59.76  | 56.21  | 36.6  | 72.42  | 83.10  | 57.62  | 57.42  | –
L268: 3  | StableQAT  | 20B Tokens & lr=2e-4  | 36.43  | 64.06  | 63.24  | 59.49  | 37.80  | 73.67  | 86.7  | 59.59  | 60.12  | +2.70
L269: 2  | ParetoQ  | 30B Tokens & lr=1e-4  | 60.02  | 34.22  | 57.65  | 55.63  | 35.80  | 72.91  | 82.90  | 59.19  | 57.29  | –
L270: 2  | DSQ  | 30B Tokens& lr=1e-4  | 59.13  | 32.59  | 58.72  | 55.65  | 36.20  | 72.03  | 80.50  | 56.27  | 56.39  | –
L271: 2  | StableQAT  | 30B Tokens& lr=1e-4  | 61.53  | 32.94  | 63.00  | 56.24  | 37.40  | 72.63  | 83.10  | 57.77  | 58.08  | +1.69
L272: #### Experiment Setup.
L273: Similarly to ParetoQ, we evaluate two representative LLMs, LLaMA-3-1B and LLaMA-3-3B (cite96†Meta, 2024 ), under weight-only quantization at 2–4 bit precision. Model performance is assessed on a popular suite of benchmarks, including ARC-Easy, ARC-Challenge, BoolQ, HellaSwag, OpenBookQA, PIQA, SciQ, Winogrande, using the lm-evaluation-harness (cite97†Gao et al., 2024 ).
L274: We compare against the recent LLM-QAT method ParetoQ and the representative soft-rounding approach DSQ, both reproduced from their official repositories with recommended hyperparameters and training schedules. The training corpus is constructed by mixing SlimPajama (cite98†Soboleva et al., 2023 ) and FineWeb-Edu (cite99†Penedo et al., 2024 ) at a one-by-one ratio, while varying the total token budget across experiments.
L275: #### Results on LLaMA-3-1B.
L276: Across all evaluated bit-widths (2–4 bits), StableQAT consistently outperforms both ParetoQ and DSQ, as shown in cite100†Table 2 , achieving improvements of up to 6.88% under different training recipes. At 4 bits, StableQAT delivers the best overall performance, surpassing ParetoQ and DSQ by 0.25%–1.38%, and in several settings even exceeding the FP16 baseline.
L277: The advantage becomes substantially more pronounced at 3 bits, where StableQAT consistently improves over both baselines by 2.70%–6.88%, highlighting its effectiveness in the regime where QAT noise becomes severe. Under the most challenging 2-bit setting, StableQAT remains stable and achieves higher performance by 1.69%, while ParetoQ and DSQ face more variance or training collapse (cite101†Figure 6 ).

## Original response: jan29_stdnext4eval

StableQAT: Stable Quantization-Aware Training at Ultra-Low Bitwidths (https://arxiv.org/html/2601.19320v1)
citeturn28436view0 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"turn28434view0","lineno":278}); Total lines: 721
L261: 4  | StableQAT  | 20B Tokens & lr=1e-4  | 65.74  | 37.54  | 64.01  | 61.15  | 40.00  | 74.59  | 86.4  | 60.46  | 61.24  | +0.25
L262: 3  | Baseline no QAT  | Baseline no QAT  | 24.74  | 26.30  | 40.64  | 26.11  | 29.00  | 50.49  | 24.90  | 48.30  | 33.81  | –
L265: 3  | StableQAT  | 10B Tokens & lr=1e-5  | 38.55  | 23.98  | 59.24  | 33.14  | 27.00  | 59.63  | 67.70  | 52.17  | 45.18  | +6.88
L266: 3  | ParetoQ  | 20B Tokens & lr=2e-4  | 35.69  | 64.24  | 61.23  | 58.91  | 37.40  | 73.32  | 87.50  | 58.27  | 59.57  | –
L267: 3  | DSQ  | 20B Tokens & lr=2e-4  | 32.85  | 60.77  | 59.76  | 56.21  | 36.6  | 72.42  | 83.10  | 57.62  | 57.42  | –
L268: 3  | StableQAT  | 20B Tokens & lr=2e-4  | 36.43  | 64.06  | 63.24  | 59.49  | 37.80  | 73.67  | 86.7  | 59.59  | 60.12  | +2.70
L269: 2  | ParetoQ  | 30B Tokens & lr=1e-4  | 60.02  | 34.22  | 57.65  | 55.63  | 35.80  | 72.91  | 82.90  | 59.19  | 57.29  | –
L270: 2  | DSQ  | 30B Tokens& lr=1e-4  | 59.13  | 32.59  | 58.72  | 55.65  | 36.20  | 72.03  | 80.50  | 56.27  | 56.39  | –
L271: 2  | StableQAT  | 30B Tokens& lr=1e-4  | 61.53  | 32.94  | 63.00  | 56.24  | 37.40  | 72.63  | 83.10  | 57.77  | 58.08  | +1.69
L272: #### Experiment Setup.
L273: Similarly to ParetoQ, we evaluate two representative LLMs, LLaMA-3-1B and LLaMA-3-3B (cite96†Meta, 2024 ), under weight-only quantization at 2–4 bit precision. Model performance is assessed on a popular suite of benchmarks, including ARC-Easy, ARC-Challenge, BoolQ, HellaSwag, OpenBookQA, PIQA, SciQ, Winogrande, using the lm-evaluation-harness (cite97†Gao et al., 2024 ).
L274: We compare against the recent LLM-QAT method ParetoQ and the representative soft-rounding approach DSQ, both reproduced from their official repositories with recommended hyperparameters and training schedules. The training corpus is constructed by mixing SlimPajama (cite98†Soboleva et al., 2023 ) and FineWeb-Edu (cite99†Penedo et al., 2024 ) at a one-by-one ratio, while varying the total token budget across experiments.
L275: #### Results on LLaMA-3-1B.
L276: Across all evaluated bit-widths (2–4 bits), StableQAT consistently outperforms both ParetoQ and DSQ, as shown in cite100†Table 2 , achieving improvements of up to 6.88% under different training recipes. At 4 bits, StableQAT delivers the best overall performance, surpassing ParetoQ and DSQ by 0.25%–1.38%, and in several settings even exceeding the FP16 baseline.
L277: The advantage becomes substantially more pronounced at 3 bits, where StableQAT consistently improves over both baselines by 2.70%–6.88%, highlighting its effectiveness in the regime where QAT noise becomes severe. Under the most challenging 2-bit setting, StableQAT remains stable and achieves higher performance by 1.69%, while ParetoQ and DSQ face more variance or training collapse (cite101†Figure 6 ).
L278: #### Results on LLaMA-3-3B.
L279: We observe consistent and often amplified trends on the larger LLaMA-3-3B model, as reported in cite102†Table 3 , indicating that the benefits of StableQAT scale favorably with model size. Across all 2–4 bit settings, StableQAT uniformly outperforms ParetoQ and DSQ, achieving gains of up to 2.67 at 4 bits and 2.38% at 3 bits.
L280: Notably, the 4-bit StableQAT model surpasses the FP16 baseline, while the 3-bit configuration reaches near full-precision performance, demonstrating that aggressive quantization can be achieved without sacrificing accuracy on larger models. Even at 2 bits, where optimization is particularly fragile, StableQAT maintains stable training dynamics and competitive performance. These results confirm that StableQAT provides a scalable and robust solution for ultra-low-bit QAT of large language models.
L281: Table 3: LLaMA-3.2-3B results. StableQAT at 4-bit outperforms the 16-bit baseline, while 3-bit StableQAT remains competitive.
L282: Bits  | Method  | Setting  | Arc-e  | Arc-c  | Boolq  | Hellaswag  | Openbookqa  | Piqa  | SciQ  | Winogrande  | Avg  | $\Delta$
L283: 16  | Baseline  | Baseline  | 71.63  | 45.99  | 73.39  | 73.61  | 43.00  | 77.48  | 92.70  | 69.85  | 68.46  | –
L284: 4  | Baseline no QAT  | Baseline no QAT  | 61.99  | 37.63  | 68.44  | 66.87  | 36.40  | 74.48  | 89.40  | 61.96  | 62.15  | –
L285: 4  | ParetoQ  | 20B Tokens & lr=1e-4  | 71.83  | 45.48  | 70.13  | 71.20  | 42.40  | 76.58  | 90.60  | 66.25  | 66.81  | –
L286: 4  | DSQ  | 20B Tokens & lr=1e-4  | 70.19  | 41.73  | 68.39  | 64.58  | 39.40  | 76.51  | 90.93  | 64.40  | 64.48  | –
L287: 4  | StableQAT  | 20B Tokens & lr=1e-4  | 72.05  | 44.97  | 70.21  | 71.28  | 42.00  | 77.58  | 91.50  | 67.64  | 67.15  | +2.67
L288: 3  | Baseline no QAT  | Baseline no QAT  | 26.14  | 25.43  | 44.01  | 26.61  | 28.40  | 52.50  | 26.00  | 49.01  | 34.76  | –
L289: 3  | ParetoQ  | 20B Tokens & lr=1e-4  | 71.47  | 45.16  | 70.28  | 70  | 42  | 76.15  | 91  | 65.93  | 66.50  | –
L290: 3  | DSQ  | 20B Tokens & lr=1e-4  | 66.58  | 41.64  | 70.24  | 66.58  | 40.60  | 76.28  | 89.80  | 64.48  | 64.52  | –
L291: 3  | StableQAT  | 20B Tokens & lr=1e-4  | 71.04  | 44.97  | 69.02  | 70.81  | 44.00  | 78.29  | 90.4  | 66.69  | 66.90  | +2.38
L292: 2  | Baseline no QAT  | Baseline no QAT  | 25.55  | 24.91  | 43.88  | 26.03  | 28.80  | 53.26  | 21.40  | 48.30  | 34.02  | –
L293: 2  | ParetoQ  | 30B Tokens & lr=1e-4  | 65.73  | 38.08  | 65.73  | 64.13  | 39.40  | 74.68  | 84.30  | 61.43  | 61.69  | –
L294: 2  | DSQ  | 30B Tokens & lr=1e-4  | 69.19  | 40.78  | 65.54  | 66.03  | 41.60  | 74.92  | 88.60  | 63.61  | 63.78  | –
L295: 2  | StableQAT  | 30B Tokens & lr=1e-4  | 68.48  | 40.87  | 63.06  | 65.20  | 41.00  | 75.41  | 87.00  | 63.38  | 63.05  | +1.36
L296: cite103†Image: Refer to caption L297: 
L298: cite104†Image: Refer to caption L299: 
L300: (a) Learning rate $1\times 10^{-5}$.
L301: 
L302: cite105†Image: Refer to caption L303: 
L304: cite106†Image: Refer to caption L305: 
L306: (b) Learning rate $2\times 10^{-4}$.
L307: 
L308: Figure 5: Training loss (left) and gradient norm (right) comparison for Llama-3-1B under different learning rates.
L309: ### 5.2 Training Stability Validation
L310: #### Gradient Dynamics and Convergence Behavior.
L311: cite80†Figure 5 provides a clear empirical validation of our theoretical analysis in Section cite23†4 . StableQAT exhibits smooth and well-behaved optimization dynamics across learning rates, with steadily decreasing training loss and controlled gradient norms throughout training.
L312: This behavior is consistent with cite87†Theorem 4.1 , which shows that our rotated damped Fourier surrogate achieves strictly smaller approximation error to the rotated rounding function than STE, resulting in a more faithful optimization direction and improved convergence. Moreover, StableQAT maintains reliable and substantial gradient signals while effectively eliminating extreme gradient outliers. In contrast to DSQ, which typically display sharp gradient spikes and outliers inducing instability.
L313: The phenomenon is well aligned with cite88†Theorem 4.2 , the gradient variance of StableQAT remains bounded, leading to gradual gradient-norm decay rather than explosion or premature vanishing. Together, these properties enable StableQAT to converge to lower loss values and better optimum, demonstrating that its theoretical advantages translate directly into stable and reliable training behavior in practice.
L314: cite107†Image: Refer to caption Figure 6: Performance error bar for LLaMA-3-1B across a shared hyperparameter set.
L315: #### Performance Error Bar.
L316: The performance error bars in cite101†Figure 6 characterize training robustness across multiple random seeds and learning-rate settings. For each method and bit-width, we report the mean performance together with its dispersion, thereby capturing sensitivity to optimization noise beyond single-run best results.
L317: StableQAT consistently achieves the highest mean performance with the tightest error bars, indicating reliable convergence under different hyperparameter perturbations, with the margin becoming more pronounced at lower bit-widths where optimization is particularly fragile. In contrast, ParetoQ exhibits both lower mean performance and larger variance. Its relies on the STE, which does not capture the intrinsic structure of the rounding operator, often yields noisy and misleading update directions.

## Original response: jan29_stdnext4tail

StableQAT: Stable Quantization-Aware Training at Ultra-Low Bitwidths (https://arxiv.org/html/2601.19320v1)
citeturn28437view0 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"turn28434view0","lineno":317}); Total lines: 721
L312: This behavior is consistent with cite87†Theorem 4.1 , which shows that our rotated damped Fourier surrogate achieves strictly smaller approximation error to the rotated rounding function than STE, resulting in a more faithful optimization direction and improved convergence. Moreover, StableQAT maintains reliable and substantial gradient signals while effectively eliminating extreme gradient outliers. In contrast to DSQ, which typically display sharp gradient spikes and outliers inducing instability.
L313: The phenomenon is well aligned with cite88†Theorem 4.2 , the gradient variance of StableQAT remains bounded, leading to gradual gradient-norm decay rather than explosion or premature vanishing. Together, these properties enable StableQAT to converge to lower loss values and better optimum, demonstrating that its theoretical advantages translate directly into stable and reliable training behavior in practice.
L314: cite107†Image: Refer to caption Figure 6: Performance error bar for LLaMA-3-1B across a shared hyperparameter set.
L315: #### Performance Error Bar.
L316: The performance error bars in cite101†Figure 6 characterize training robustness across multiple random seeds and learning-rate settings. For each method and bit-width, we report the mean performance together with its dispersion, thereby capturing sensitivity to optimization noise beyond single-run best results.
L317: StableQAT consistently achieves the highest mean performance with the tightest error bars, indicating reliable convergence under different hyperparameter perturbations, with the margin becoming more pronounced at lower bit-widths where optimization is particularly fragile. In contrast, ParetoQ exhibits both lower mean performance and larger variance. Its relies on the STE, which does not capture the intrinsic structure of the rounding operator, often yields noisy and misleading update directions.
L318: These misaligned gradients can push weights across quantization thresholds in an uncontrolled manner, increasing sensitivity, sometimes leading to training collapse. DSQ shows elevated variance for a different reason. Its sigmoid-style surrogate introduces regions of extremely large gradients near the transition boundaries. Such gradient explosion amplifies small perturbations during training, making optimization sensitive and introducing widened error bars.
L319: ### 5.3 Ablation Studies
L320: 
L321: cite108†Image: Refer to caption L322: 
L323: cite109†Image: Refer to caption L324: 
L325: Figure 7: Training loss and gradient norm dynamics across RDFS’s order $M=0,1,2$.
L326: #### Fourier Order of RDFS.
L327: We study the effect of Fourier truncation order $M$ in RDFS. cite110†Figure 7 compares training dynamics across $M=0,1,2$. A first-order approximation ($M=0$) already captures the majority of the performance and stability gains, yielding smooth loss decay and well-controlled gradient norms. While higher-order terms introduce finer structural details of the quantization operator, their empirical benefits are marginal and come at increased numerical complexity.
L328: These observations well validate our design choice of adopting the first-order RDFS as cite85†Equation 5 , which offers an effective balance between approximation fidelity, training stability, and computational simplicity for quantization-aware training.
L329: cite111†Image: Refer to caption Figure 8: Performance of 3-bit Llama-3.2-1B across different amplitudes.
L330: #### Amplitude.
L331: We next vary the amplitude $A$ to control the sharpness of surrogate gradient, to empirically validate the damped amplitude design predicted by the theoretical analysis in Section cite19†3.2 . As shown in cite86†Figure 8 , the empirical results closely align with the theoretical characterization and clearly reveal the presence of an ill-conditioned regime, where the surrogate curves become nearly tangential to horizontal plateaus.
L332: In contrast, moderate amplitude values provide a favorable balance between approximation fidelity and optimization stability. In particular, the selected setting $A=0.21$ consistently achieves stronger performance, benefiting from an adequate approximation of the rounding operator while maintaining stable and well-conditioned training dynamics.

