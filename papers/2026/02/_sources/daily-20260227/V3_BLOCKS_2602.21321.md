[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] p: marginparsep has been altered. topmargin has been altered. marginparpush has been altered.

[3] p: The page layout violates the ICML style.

[4] p: Please do not change the page layout, or include packages like geometry, savetrees, or fullpage, which change it for you.

[5] p: We’re not able to reliably undo arbitrary changes to the style. Please remove the offending package(s), or layout-changing commands and try again.

[6] p: Dynamic Symmetric Point Tracking: Tackling Non-ideal Reference in Analog In-memory Training

[7] p: Quan Xiao * 1 Jindan Li * 1 Zhaoxian Wu 1 Tayfun Gokmen 2 Tianyi Chen 1

[8] h6: Abstract

[9] p: Analog in-memory computing (AIMC) performs computation directly within resistive crossbar arrays, offering an energy-efficient platform to scale large vision and language models. However, non-ideal analog device properties make the training on AIMC devices challenging. In particular, its update asymmetry can induce a systematic drift of weight updates towards a device-specific symmetric point (SP), which typically does not align with the optimum of the training objective. To mitigate this bias, most existing works assume the SP is known and pre-calibrate it to zero before training by setting the reference point as the SP. Nevertheless, calibrating AIMC devices requires costly pulse updates, and residual calibration error can directly degrade training accuracy. In this work, we present the first theoretical characterization of the pulse complexity of SP calibration and the resulting estimation error. We further propose a dynamic SP estimation method that tracks the SP during model training, and establishes its convergence guarantees. In addition, we develop an enhanced variant based on chopping and filtering techniques from digital signal processing. Numerical experiments demonstrate both the efficiency and effectiveness of the proposed method.

[10] h3: 1 Introduction

[11] p: Recent breakthroughs in large vision and language models have been driven by the rapid maturation of modern hardware accelerators, including GPU, TPU ( Jouppi et al., 2023 ) , NPU ( Esmaeilzadeh et al., 2012 ) , and emerging AI-specific chips such as NorthPole ( Modha et al., 2023 ) . Despite these advances, the energy costs of training and deploying such models still remain prohibitively high ( Touvron et al., 2023 ; Brown et al., 2020 ) .

[12] p: To mitigate the energy bottleneck, analog in-memory computing (AIMC) has emerged as a promising platform that leverages resistive crossbar arrays to enable in-situ analog matrix–vector multiplications (MVMs). In AIMC, the weight matrix is stored as the conductance of resistive devices on a crossbar array, while MVM inputs and outputs are encoded as analog voltages and currents. By leveraging Kirchhoff’s and Ohm’s laws, AIMC devices perform MVMs directly without data movement, achieving 10 × \times -10,000 × \times lower inference energy than GPUs ( Jain and others, 2019 ; Cosemans et al., 2019 ; Papistas et al., 2021 ) .

[13] p: Consider a model training problem with the objective f ⁡ ( ⋅ ) : ℝ D → ℝ f(\,\cdot\,):{\mathbb{R}}^{D}\to{\mathbb{R}} and its model parameters W ∈ ℝ D W\in{\mathbb{R}}^{D} by

[14] table: W ∗ := arg ​ min W ∈ ℝ D { f ( W ) := 𝔼 ξ [ f ( W ; ξ ) ] } \displaystyle W^{*}:=\operatornamewithlimits{arg\,min}_{W\in{\mathbb{R}}^{D}}~\big\{f(W):={\mathbb{E}}_{\xi}[f(W;\xi)]\big\} (1)

[15] p: where ξ \xi is a random data sample. Different from digital training, on AIMC hardware, the weights are updated by the so-called pulse update . When receiving electrical pulses, a resistive element updates its conductance based on its pulse polarity ( Gokmen and Vlasov, 2016 ) . At each pulse cycle, the weight changes by either Δ ​ w min ⋅ q + ​ ( w ) \Delta w_{\min}\cdot q_{+}(w) or − Δ w min ⋅ q − ( w ) -\Delta w_{\min}\cdot q_{-}(w) , where Δ ​ w min > 0 \Delta w_{\min}>0 is the known response granularity , and q + ​ ( w ) q_{+}(w) and q − ​ ( w ) q_{-}(w) are fixed but unknown response functions . One of the key challenges in analog training is update asymmetry : at a fixed weight w w , the conductance change induced by a single positive pulse q + ​ ( w ) q_{+}(w) differs from that induced by a negative pulse q − ​ ( w ) q_{-}(w) , causing the weights to drift towards device-specific fixed points.

[16] p: By decomposing q + ​ ( w ) q_{+}(w) and q − ​ ( w ) q_{-}(w) into a symmetric component and an asymmetric component that capture the device-specific drift (will explain in ( 6 )), we model the analog update as a scaled desired update plus an asymmetric drift term. Mathematically, each resistive element admits a device-specific symmetric component F ⁡ ( ⋅ ) F(\,\cdot\,) , an asymmetric component G ⁡ ( ⋅ ) G(\,\cdot\,) . To apply an increment Δ W k = α ∇ f ( W k ; ξ k ) \Delta W_{k}=\alpha\nabla f(W_{k};\xi_{k}) with stepsize α \alpha , the analog device performs the following Analog Update Wu et al. (2025) ; Li et al. (2025)

[17] p: where | ⋅ | |\cdot| and ⊙ \odot denote the coordinate-wise absolute value and multiplication, and b k b_{k} quantifies the stochastic discretization error of sending a finite number of pulses of length Δ ​ w min \Delta w_{\min} to change each d d -th element of W k W_{k} . Unlike on digital devices, where G ⁡ ( ⋅ ) ≡ 0 G(\cdot)\equiv 0 , G ⁡ ( ⋅ ) ≢ 0 G(\cdot)\not\equiv 0 on analog devices induces the update asymmetry . Specifically, even without the discretization error b k b_{k} , the training optimum W ∗ W^{*} is generally not a stationary point of the Analog Update because

[18] table: 𝔼 ⁡ [ W k + 1 | W k = W ∗ ] \displaystyle\mathbb{E}[W_{k+1}|W_{k}=W^{*}] = W ∗ − α ​ 𝔼 ξ ​ [ | ∇ f ​ ( W ∗ , ξ ) | ] ⊙ G ⁡ ( W ∗ ) \displaystyle=W^{*}-\alpha\mathbb{E}_{\xi}[|\nabla f(W^{*};\xi)|]\odot G(W^{*})

[19] p: does not equal W ∗ W^{*} whenever the device-asymmetry term is nonzero (i.e., G ⁡ ( W ∗ ) ≠ 0 G(W^{*})\neq 0 ) as 𝔼 ξ ​ [ | ∇ f ​ ( W ∗ , ξ ) | ] > 0 \mathbb{E}_{\xi}[|\nabla f(W^{*};\xi)|]>0 . This motivates us to study the symmetric points where we do not have device-asymmetry as defined below.

[20] h6: Definition 1.1 ( Symmetric point ) .

[21] p: A point is termed symmetric point (SP) if the following equation holds

[22] table: G ⁡ ( W ⋄ ) = 0 . \displaystyle G(W^{\diamond})=0. (3)

[23] p: With this, SGD with Analog Update can be interpreted as implicitly minimizing a regularized objective of the form

[24] table: min W ⁡ f ⁡ ( W ) + Θ ⁡ ( σ 2 ​ ‖ W − W ⋄ ‖ 2 ) \displaystyle\min_{W}~~f(W)+{\Theta}(\sigma^{2}\|W-W^{\diamond}\|^{2}) (4)

[25] p: where σ 2 \sigma^{2} denotes the variance of the stochastic gradient noise ( Wu et al., 2025 ) . Consequently, obtaining an accurate estimate of W ⋄ W^{\diamond} is a key prerequisite for analog training algorithm design, as it enables effective compensation of the drift induced by update asymmetry .

[26] p: In existing algorithm design and convergence theory of analog training ( Wu et al., 2024 ; Wu et al., 2025 ) , W ⋄ W^{\diamond} is assumed to be 0 0 for simplicity. However, in practice, the SP is device-specific, so it requires per-device estimation and calibration to zero before training ( Gokmen, 2021 ) . To estimate the SP, a typical zero-shifting (ZS) algorithm has been proposed by Kim et al. (2019) , which sends alternative up-down pulses to push the device to its SP. However, as shown in Figure 1 , its pulse count significantly impacts the precision of SP estimation, and higher-precision devices (smaller Δ ​ w min \Delta w_{\min} ) require more pulses to achieve a target accuracy. These observations lead to a critical question regarding the trade-off between pulse overhead and accuracy for SP estimation:

[27] p: Q1) How to quantify the pulse efficiency of the SP estimation algorithm in terms of the number of pulses?

[28] p: After obtaining the estimate of SP and calibrating it to zero (through a reference device), we can leverage existing zero-SP-based analog training algorithms for the model training ( Wu et al., 2025 ; Wu et al., 2024 ; Gokmen, 2021 ) . However, this renders the subsequent training phase vulnerable to estimation error propagated from the SP estimation stage when we do not have enough pulse budget; see Figure 2 . Intuitively, the training process can also provide valuable feedback for SP tracking: if W ⋄ W^{\diamond} is inaccurate, the resulting compensation deviates from the true drift term in ( 4 ), which in turn degrades training. Considering the benefits of integrating SP tracking with training, another natural question is

[29] p: Q2) Can we develop a dynamic SP tracking algorithm during training to reduce the overall pulse complexity?

[30] p: To address the above two questions, we develop a dynamic SP-tracking algorithm based on multi-sequence update and the filtering theory from digital signal processing.

[31] figure: (a) Offset vs. pulse budget. (b) Pulse cost v.s. Δ ​ w min \Delta w_{\min} Figure 1: Trade-off between SP estimation accuracy and pulse cost for ZS algorithm. (a) For each N N , we obtain per-cell SP estimates on a 512 × 512 512\times 512 array, and compute the mean and standard deviation across all cells. We plot the offsets of these statistics relative to the ground truth. (b) As Δ ​ w min \Delta w_{\min} decreases, achieving a target accuracy (e.g., ≤ 1 % \leq 1\% relative mean error) needs substantially more pulses.

[32] h4: 1.1 Our contributions

[33] p: We summarize the contributions of this paper as follows:

[34] p: We provide the first theoretical complexity analysis of the standard ZS algorithm for SP estimation ( Kim et al., 2019 ) . Crucially, we prove that the pulse count required for accurate estimation scales inversely with device update granularity 𝒪 ⁡ ( Δ ​ w min − 1 ) \mathcal{O}(\Delta w_{\min}^{-1}) . This reveals a fundamental efficiency limit: as hardware becomes more precise, static SP estimation becomes prohibitively expensive, motivating the need for dynamic tracking.

[35] p: We propose a novel ResIdual learning with Dynamic symmEtric point tRacking (RIDER) algorithm that jointly performs SP tracking and model training on the analog devices.

[36] p: We proved that the proposed RIDER algorithm can estimate the SP during the model training with reduced pulse complexity, and achieves the same rate 𝒪 ⁡ ( 1 / K ) \mathcal{O}(1/\sqrt{K}) as standard SGD.

[37] p: Building on C2), we propose an Enhanced variant of RIDER, termed E-RIDER, that leverages the frequency theory to accelerate the SP estimation and a periodic synchronization mechanism to reduce weight programming costs, making the method feasible for energy-constrained edge implementations.

[38] p: Numerical experiments validate the effectiveness and efficiency of the E-RIDER for simultaneous SP tracking and model training. With a more accurate SP estimation, the proposed method is able to improve the analog training accuracy in neural network training, and outperforms other analog training algorithms.

[39] figure: Figure 2: Training loss on MNIST (LeNet-5, TT-v1 Gokmen and Haensch (2020) ) using ground-truth SP and SPs estimated with different numbers of pulses N N via zero-shifting Algorithm 1 .

[40] h4: 1.2 Related works

[41] p: AIMC accelerates deep learning by executing compute-intensive MVM operations directly within resistive crossbar arrays Yao et al. (2017) ; Wang et al. (2019) . However, hardware imperfection introduces errors into the training. A series of works proposes methods to offload parts of error-sensitive operations on digital circuits to mitigate the issues Nandakumar et al. (2020) ; Wan et al. (2022) ; Yao et al. (2020) . While effective, this digital overhead compromises the intrinsic energy and latency benefits of the architecture. Consequently, this paper focuses on the more challenging regime of fully on-chip training, which maximizes operations in the analog domain to preserve efficiency.

[42] p: The primary challenges of on-chip training arise from inherent hardware imperfections, such as asymmetric update Burr et al. (2015) ; Chen et al. (2015) , reading/writing noise Agarwal et al. (2016) ; Zhang et al. (2022) ; Deaville et al. (2021) , device/cycle variations Lee et al. (2019) . Researchers have developed various architectural and algorithmic solutions to mitigate these imperfections. For example, Gokmen and Haensch (2020) ; Gokmen (2021) ; Wang et al. (2020) ; Huang et al. (2020) introduce an auxiliary analog array to suppress update noise; Li et al. (2025) addresses the constraints of limited update granularity through a multi-tile orchestration method. Complementing these empirical methods, recent works have established rigorous theoretical frameworks to model these imperfections, proposing residual learning as a principled mechanism to recover training performance Wu et al. (2024) ; Wu et al. (2025) . However, their theory requires the SP to be exactly zero, and empirically they are not robust to nonzero SP. Most closely related to our work, Rasch et al. (2024) proposed a dynamic SP tracking method AGAD with strong empirical performance. However, their methodology lacks theoretical guarantees even without chopping. As will be demonstrated in this paper, omitting a residual learning mechanism results in inferior performance compared to the E-RIDER in this work.

[43] figure: Algorithm 1 ZS algorithm ( Kim et al., 2019 ) 1: Inputs: initialization W 0 W_{0} ; response granularity Δ ​ w min \Delta w_{\min} 2: for n = 0 , 1 , … , N − 1 n=0,1,\ldots,N-1 do 3: draw ϵ n ∈ ℝ D \epsilon_{n}\in\mathbb{R}^{D} with ϵ n [ d ] ∼ 𝒰 ⁡ ( { − Δ ​ w min , Δ ​ w min } ) \epsilon_{n}^{[d]}\sim\mathcal{U}(\{-\Delta w_{\min},\Delta w_{\min}\}) 4: update W n + 1 W_{n+1} via analog pulse update, i.e. ( 7 ) 5: end for 6: outputs: W N W_{N}

[44] h3: 2 Pulse Complexity of SP Estimation

[45] p: In this section, we model the ZS algorithm as a discrete-time dynamic using pulse updates, and analyze its convergence as the number of pulses increases.

[46] h4: 2.1 Mathematical Model of Zero-shifting Algorithm

[47] p: We will first introduce the mathematical formulation of Analog Update in ( 2 ), and then abstract the update rule for the ZS algorithm ( Kim et al., 2019 ) .

[48] p: For each AIMC device, we stack the response functions q − ​ ( w ) q_{-}(w) and q + ​ ( w ) q_{+}(w) into Q + ​ ( W ) Q_{+}(W) and Q − ​ ( W ) : ℝ D → ℝ D Q_{-}(W):{\mathbb{R}}^{D}\rightarrow{\mathbb{R}}^{D} , and express the analog weight updates as

[49] table: W k + 1 [ d ] = { W k [ d ] + Δ ​ W k [ d ] ⋅ Q + ​ ( W k ) [ d ] , Δ ​ W k [ d ] ≥ 0 , W k [ d ] + Δ ​ W k [ d ] ⋅ Q − ​ ( W k ) [ d ] , Δ ​ W k [ d ] < 0 \displaystyle W_{k+1}^{[d]}=\begin{cases}W_{k}^{[d]}+\Delta W_{k}^{[d]}\cdot Q_{+}(W_{k})^{[d]},~~~\Delta W_{k}^{[d]}\geq 0,\\ W_{k}^{[d]}+\Delta W_{k}^{[d]}\cdot Q_{-}(W_{k})^{[d]},~~~\Delta W_{k}^{[d]}<0\end{cases} (5)

[50] p: where Δ ​ W k ∈ ℝ D \Delta W_{k}\in\mathbb{R}^{D} is the target update increment and A [ d ] A^{[d]} denotes the d d -th element of A ∈ ℝ D A\in\mathbb{R}^{D} . Following ( Wu et al., 2025 ) , the symmetric component F ⁡ ( ⋅ ) F(\,\cdot\,) and the asymmetric component G ⁡ ( ⋅ ) G(\,\cdot\,) of this device are given by

[51] table: F ⁡ ( W ) := ( Q − ​ ( W ) + Q + ​ ( W ) ) / 2 , \displaystyle F(W):=(Q_{-}(W)+Q_{+}(W))/2, (6a) G ⁡ ( W ) := ( Q − ​ ( W ) − Q + ​ ( W ) ) / 2 , \displaystyle G(W):=(Q_{-}(W)-Q_{+}(W))/2, (6b)

[52] p: pluging which into ( 5 ) leads to the Analog Update ( 2 ).

[53] p: ZS algorithm ( Kim et al., 2019 ) estimates the SP of an analog device by applying positive (up) and negative (down) update pulses alternatively until the weight no longer drifts, which we model as the following stochastic dynamic

[54] p: where ϵ n ∈ ℝ D \epsilon_{n}\in\mathbb{R}^{D} and ϵ n [ d ] ∼ 𝒰 ⁡ ( { − Δ ​ w min , Δ ​ w min } ) \epsilon_{n}^{[d]}\sim\mathcal{U}(\{-\Delta w_{\min},\Delta w_{\min}\}) is uniformly randomly generated as either up or down pulse, which is summarized in Algorithm 1 . Note that the original ZS algorithm proposed in ( Kim et al., 2019 ) is a cyclic sampling version of Algorithm 1 ; i.e. ϵ 2 ​ n ′ [ d ] = Δ ​ w min \epsilon_{2n^{\prime}}^{[d]}=\Delta w_{\min} and ϵ 2 ​ n ′ + 1 [ d ] = − Δ ​ w min \epsilon_{2n^{\prime}+1}^{[d]}=-\Delta w_{\min} . As the convergence analysis for the cyclic version is built upon the stochastic version ( 7 ) and the convergence rate order of them are the same, we only present the stochastic case in the main paper and defer the cyclic-case result to the Appendix C.3 – C.4 .

[55] h4: 2.2 Convergence Analysis for ZS Algorithm

[56] p: To analyze the convergence of ZS algorithm, we focus on the devices with response functions in ( Wu et al., 2025 ) .

[57] h6: Definition 2.1 (Training-friendly response functions) .

[58] p: Response functions q + ​ ( ⋅ ) q_{+}(\,\cdot\,) and q − ​ ( ⋅ ) q_{-}(\,\cdot\,) are said to be training-friendly if they satisfy

[59] p: (Positive-definiteness) there exist q min > 0 q_{\min}>0 and q max > 0 q_{\max}>0 such that q min ≤ q + ​ ( w ) ≤ q max q_{\min}\leq q_{+}(w)\leq q_{\max} and q min ≤ q − ​ ( w ) ≤ q max , ∀ w q_{\min}\leq q_{-}(w)\leq q_{\max},\forall w ; and,

[60] p: (Differentiable) Both q + ​ ( ⋅ ) q_{+}(\,\cdot\,) and q − ​ ( ⋅ ) q_{-}(\,\cdot\,) are differentiable.

[61] p: Definition 2.1 covers a wide range of response functions in different kinds of AIMC devices, including PCM ( Burr et al., 2016 ; Le Gallo and Sebastian, 2020 ) , ReRAM ( Jang et al., 2014 ; Jang et al., 2015 ; Stecconi et al., 2024 ) , ECRAM ( Tang et al., 2018 ; Onen et al., 2022 ) . For this family of response functions, the convergence of ZS algorithm in Algorithm 1 can be characterized below.

[62] h6: Theorem 2.2 (Convergence rate of Algorithm 1 ) .

[63] p: Considering the response functions in Definition 2.1 , then the iterates given by Algorithm 1 with N N pulses satisfy

[64] table: 1 N ​ ∑ n = 0 N − 1 𝔼 ⁡ [ ‖ G ⁡ ( W n ) ‖ 2 ] ≤ 𝒪 ⁡ ( 1 N ​ Δ ​ w min ) + Θ ⁡ ( Δ ​ w min ) . \displaystyle\frac{1}{N}\sum_{n=0}^{N-1}\mathbb{E}\left[\|G(W_{n})\|^{2}\right]\leq{\cal O}\left(\frac{1}{N\Delta w_{\min}}\right)+{\Theta}(\Delta w_{\min}).

[65] p: The proof of Theorem 2.2 is deferred to Appendix C.1 . Theorem 2.2 shows that, for a device with response granularity Δ ​ w min \Delta w_{\min} , the minimal achievable SP estimation error is δ = Θ ⁡ ( Δ ​ w min ) \delta={\Theta}(\Delta w_{\min}) , meaning that higher-precision devices (smaller Δ ​ w min \Delta w_{\min} ) can attain more accurate SP estimates. However, to achieve the same fixed estimation error δ ≥ Θ ⁡ ( Δ ​ w min ) \delta\geq{\Theta}(\Delta w_{\min}) , the required number of pulses scales inversely with the response granularity Δ ​ w min \Delta w_{\min} , which is N = 𝒪 ⁡ ( δ − 1 ​ Δ ​ w min − 1 ) N={\cal O}(\delta^{-1}\Delta w_{\min}^{-1}) . In practice, the response granularity Δ ​ w min \Delta w_{\min} of AIMC device is made sufficiently small to ensure the gradient conversion precision ( Rao et al., 2023 ; Sharma et al., 2024 ) , so that the computational complexity of Algorithm 1 is relatively high.

[66] h6: Remark 2.3 .

[67] p: With additional assumptions on device behavior, we can derive tighter bounds for N N w.r.t. target error δ \delta for specific classes of response functions; we defer these results (Theorem C.2 ) to Appendix C.2 . Nonetheless, the number of pulses required to achieve a target SP estimation error still remains inversely proportional to Δ ​ w min \Delta w_{\min} .

[68] p: Empirical evidence. To illustrate the negative impact of Δ ​ w min \Delta w_{\min} on the pulse complexity of the ZS algorithm, we test its pulse cost on a linear device; see detailed setup in Appendix F.1 . Figure 1(a) shows the empirical estimated offset of the SP mean and standard deviation when Δ ​ w min = 0.001 \Delta w_{\min}=0.001 , defined as the ground-truth statistic minus the estimated statistic. It can be seen that achieving relative 1 % 1\% error requires more than 2000 2000 number of pulses in ZS algorithm, which is computationally heavy. In Figure 1(b) , we report the smallest N N such that the relative error of the estimated SP mean is within 1 % 1\% under different device response granularity Δ ​ w min \Delta w_{\min} . The result shows that higher-precision devices (smaller Δ ​ w min \Delta w_{\min} ) require substantially more pulses to reach the same target error δ \delta . Moreover, the relationship of Δ ​ w min \Delta w_{\min} and N N is nearly inversely linear, as predicted by our Theorem 2.2 .

[69] p: To study the effect of SP estimation error on model training, we train a LeNet-5 on MNIST with TT-v1 using SPs estimated from Algorithm 1 with different numbers of pulses and report the results in Figure 2 . It shows that a smaller N N in Algorithm 1 leads to significant training loss degradation and even failure to converge, which motivates the design of dynamic SP tracking algorithm.

[70] h3: 3 Dynamic SP Tracking Algorithm

[71] p: In this section, we aim to develop a dynamic SP tracking algorithm that leverages the inherent SP-attraction property of AIMC devices, i.e., repeated gradient pulse updates drive the device state towards its SP. The challenge of algorithm design is deferred to Appendix B.3 .

[72] h4: 3.1 Basic Design

[73] p: We first design a basic dynamic SP-tracking algorithm based on Residual Learning in ( Wu et al., 2025 ) that rectifies the update asymmetry in AIMC devices. Residual Learning introduces another AIMC device to learn the asymmetric residual and compensate for it through gradient updates. However, it assumes an exactly zero SP , which in turn requires precise zero-shifting calibration prior to training. To enable dynamic SP tracking, we introduce an SP-tracking variable Q k ∈ ℝ D Q_{k}\in\mathbb{R}^{D} that approaches the SP over iterations. For each iteration k k , we aim to solve the following bilevel problem to correct the asymmetry bias

[74] p: where P − Q k P-Q_{k} serves as a zero-shifting (residual) vector. The lower-level problem seeks the optimal compensation vector to correct device-induced errors, while the upper-level problem drives the system toward a zero-shifted state. If we can design a SP-tracking sequence Q k Q_{k} such that Q k → W ⋄ Q_{k}\rightarrow W^{\diamond} , then the optimal solution for ( 8 ) is P ∗ = Q ∗ = W ⋄ P^{*}=Q^{*}=W^{\diamond} and W ∗ = arg ​ min W ⁡ f ​ ( W ) W^{*}=\operatornamewithlimits{arg\,min}_{W}f(W) . To design an algorithm for solving ( 8 ), we make the following assumptions.

[75] h6: Assumption 3.1 ( L L -smoothness) .

[76] p: The objective f ⁡ ( W ) f(W) is L L -smooth, that is for any W , W ′ ∈ ℝ D W,W^{\prime}\in{\mathbb{R}}^{D} , it follows

[77] table: ‖ ∇ f ​ ( W ) − ∇ f ​ ( W ′ ) ‖ ≤ L ​ ‖ W − W ′ ‖ . \displaystyle\|\nabla f(W)-\nabla f(W^{\prime})\|\leq L\|W-W^{\prime}\|. (9)

[78] h6: Assumption 3.2 (Unbiasness and bounded variance) .

[79] p: The samples { ξ k } \{\xi_{k}\} are i.i.d. sampled from a distribution. Moreover, the stochastic gradient is unbiased and has bounded variance, i.e., 𝔼 ξ k ​ [ ∇ f ​ ( W k , ξ k ) ] = ∇ f ​ ( W k ) {\mathbb{E}}_{\xi_{k}}[\nabla f(W_{k};\xi_{k})]=\nabla f(W_{k}) and 𝔼 ξ k ​ [ ‖ ∇ f ​ ( W k , ξ k ) − ∇ f ​ ( W k ) ‖ 2 ] ≤ σ 2 {\mathbb{E}}_{\xi_{k}}[\|\nabla f(W_{k};\xi_{k})-\nabla f(W_{k})\|^{2}]\leq\sigma^{2} .

[80] h6: Assumption 3.3 ( μ \mu -SC condition) .

[81] p: The objective f ⁡ ( W ) f(W) is strongly convex (SC) with modulus μ \mu .

[82] h6: Assumption 3.4 .

[83] p: The stochastic discretization error b k b_{k} in ( 2 ) satisfies 𝔼 ⁡ [ b k ] = 0 \mathbb{E}[b_{k}]=0 and Var ⁡ [ b k ] = Θ ⁡ ( α ​ Δ ​ w min ) \operatorname{Var}[b_{k}]={\Theta}(\alpha\Delta w_{\min}) .

[84] p: Assumptions 3.1 – 3.3 are standard in the stochastic optimization ( Bottou et al., 2018 ) , and are all used in the pilot theoretical analysis for analog training ( Wu et al., 2025 ) . Assumption 3.4 is used and verified in ( Li et al., 2025 ) .

[85] p: With these assumptions, the lower-level solution of problem ( 8 ) is unique, given by

[86] table: P ∗ ​ ( W , Q k ) = Q k + ( W ∗ − W ) / γ . \displaystyle P^{*}(W,Q_{k})=Q_{k}+(W^{*}-W)/\gamma. (10)

[87] p: Basically, the optimal P ∗ ​ ( W , Q k ) − Q k P^{*}(W,Q_{k})-Q_{k} tracks the difference of current W k W_{k} towards the optimal solution W ∗ W^{*} . Besides, the gradient of the bilevel problem ( 8 ) with respect to W W can be computed via chain rule

[88] table: ∇ W ‖ P ∗ ​ ( W , Q k ) − Q k ‖ 2 \displaystyle\nabla_{W}\|P^{*}(W,Q_{k})-Q_{k}\|^{2} = − 2 ( P ∗ ( W , Q k ) − Q k ) / γ . \displaystyle=-2(P^{*}(W,Q_{k})-Q_{k})/\gamma.

[89] p: Let us define W ¯ k = W k + γ ⁡ ( P k − Q k ) \bar{W}_{k}=W_{k}+\gamma(P_{k}-Q_{k}) . Inspired by alternating bilevel algorithms ( Chen et al., 2021 ; Ji et al., 2021 ; Hong et al., 2020 ; Ghadimi and Wang, 2018 ; Maclaurin et al., 2015 ; Franceschi et al., 2017 ; Franceschi et al., 2018 ; Pedregosa, 2016 ) and putting P k P_{k} and Q k Q_{k} on different analog devices, the update rules using Analog Update in ( 2 ) can be written as

[90] p: where both b k , b k ′ b_{k},b^{\prime}_{k} denote the discretization errors, and we denote the corresponding response functions by F p , G p F_{p},G_{p} for the device of P k P_{k} , and by F w , G w F_{w},G_{w} for the device of W k W_{k} .

[91] p: Design for Q k Q_{k} sequence. We first note that the SP-drifting issue arises only in the presence of stochastic noise (see ( 4 )), i.e., the device used for P k P_{k} , as the W k W_{k} sequence is conditionally deterministic given P k + 1 P_{k+1} and Q k Q_{k} , so we only need to estimate the SP of the device for P k P_{k} . Our key observation is that the update of P k P_{k} in ( 11a ) combines both descent on f ⁡ ( W ¯ ) f(\bar{W}) via a stochastic-gradient increment, and an additional increment that drives G p ​ ( P k ) G_{p}(P_{k}) towards zero, scaled by a positive stepsize | ∇ f ​ ( W ¯ k , ξ k ) | |\nabla f(\bar{W}_{k};\xi_{k})| . This suggests that the update of P k P_{k} contains an inherent component that pulls it towards the SP. Therefore, we propose a moving averaging sequence Q k Q_{k} to magnify the SP-attracting property of P k P_{k} sequence

[92] p: where the Q k Q_{k} sequence is updated on the digital device so that there is no analog update bias. The complete ResIdual learning with Dynamic symmEtric point tRacking (RIDER) algorithm is summarized in Algorithm 2 . The following lemma formalizes the key insight that moving averaging amplifies the SP-attraction property.

[93] h6: Lemma 3.5 .

[94] p: Let W ⋄ W^{\diamond} be the SP used for P k P_{k} , i.e. G p ​ ( W ⋄ ) = 0 G_{p}(W^{\diamond})=0 . For any iteration k k , if cos ⁡ ( P k + 1 − W ⋄ , P k + 1 − Q k ) > 0 \cos(P_{k+1}-W^{\diamond},P_{k+1}-Q_{k})>0 , then there exists η ∈ ( 0 , 1 ) \eta\in(0,1) in ( 12 ) such that

[95] table: ‖ Q k + 1 − W ⋄ ‖ 2 < ‖ P k + 1 − W ⋄ ‖ 2 . \displaystyle\|Q_{k+1}-W^{\diamond}\|^{2}<\|P_{k+1}-W^{\diamond}\|^{2}. (13)

[96] p: The proof of Lemma 3.5 is provided in Appendix D.1 . Because the update of P P includes a gradient-descent term for the objective in addition to SP drift, so that both W ⋄ W^{\diamond} and Q k Q_{k} tend to sit on the same side from P k + 1 P_{k+1} . This suggests that the angle condition is likely to hold so that Q k Q_{k} sequence remains closer to W ⋄ W^{\diamond} than P k P_{k} sequence.

[97] figure: Algorithm 2 RIDER algorithm 1: Inputs: initialization P 0 , Q 0 , W 0 P_{0},Q_{0},W_{0} ; residual parameter γ \gamma ; response granularity F p ​ ( ⋅ ) , F w ​ ( ⋅ ) , G p ​ ( ⋅ ) , G w ​ ( ⋅ ) F_{p}(\cdot),F_{w}(\cdot),G_{p}(\cdot),G_{w}(\cdot) 2: for k = 0 , 1 , … , K − 1 k=0,1,\ldots,K-1 do 3: evaluate W ¯ k = W k + γ ⁡ ( P k − Q k ) \bar{W}_{k}=W_{k}+\gamma(P_{k}-Q_{k}) 4: sample stochastic gradient ∇ f ​ ( W ¯ k , ξ k ) \nabla f(\bar{W}_{k};\xi_{k}) 5: update P k + 1 P_{k+1} on analog device via ( 11a ) 6: update Q k + 1 Q_{k+1} on digital device via ( 12 ) 7: update W k + 1 W_{k+1} on analog device via ( 11b ) 8: end for 9: outputs: { P K , Q K , W K } \left\{P_{K},Q_{K},W_{K}\right\}

[98] p: To analyze the convergence of Algorithm 2 with respect to three sequences, we define the convergence metric as

[99] table: E K = 1 K ​ ∑ k = 0 K − 1 𝔼 \displaystyle E_{K}=\frac{1}{K}\sum_{k=0}^{K-1}{\mathbb{E}} [ ∥ W k − W ∗ ∥ 2 + 𝒪 ( ∥ P k − Q k ∥ 2 ) \displaystyle\big[\big\|W_{k}-W^{*}\big\|^{2}+{\cal O}\left(\|P_{k}-Q_{k}\|^{2}\right) + 𝒪 ( ∥ G p ( P k ) ∥ 2 ) ] \displaystyle~~~+{\cal O}\left(\|G_{p}(P_{k})\|^{2}\right)\big] (14)

[100] p: where the three terms quantifies the convergence of W k W_{k} , Q k Q_{k} and P k P_{k} , respectively. For simplicity, the constants in front of some terms in E K E_{K} are hidden. When E k → 0 E_{k}\rightarrow 0 , it can be seen that W k → W ∗ W_{k}\rightarrow W^{*} and P k , Q k → W ⋄ P_{k},Q_{k}\rightarrow W^{\diamond} . To prove the convergence, we need the following assumption.

[101] h6: Assumption 3.6 (Rayleigh-type lower bound) .

[102] p: There exists C ⋆ > 0 C_{\star}>0 such that for all k k , 𝔼 ξ k ​ [ | ∇ f ​ ( W ¯ k , ξ k ) | d ] ≥ C ∗ \mathbb{E}_{\xi_{k}}\big[|\nabla f(\bar{W}_{k};\xi_{k})|_{d}\big]\geq C_{*} .

[103] p: Assumption 3.6 is mild since the operations in the analog domain intrinsically involve thermal and electrical noise.

[104] h6: Theorem 3.7 (Convergence of Algorithm 2 ) .

[105] p: Suppose Assumptions 3.1 - 3.4 , 3.6 hold and the response functions F p , G p , F w , G w F_{p},G_{p},F_{w},G_{w} satisfy Definition 2.1 . If C ⋆ ≥ 4 ​ 2 ​ σ μ ​ ( q max q min ) 3 2 C_{\star}\geq\frac{4\sqrt{2}\sigma}{\mu}\left(\frac{q_{\max}}{q_{\min}}\right)^{\frac{3}{2}} , let α = Θ ⁡ ( 1 K ) \alpha=\Theta\left(\frac{1}{\sqrt{K}}\right) , β = Θ ⁡ ( α ​ γ ​ μ ) \beta=\Theta(\alpha\gamma\mu) , η = Θ ⁡ ( α ​ μ ) \eta=\Theta(\alpha\mu) , γ = Θ ⁡ ( 1 ) \gamma=\Theta(1) , it holds that

[106] table: E K ≤ 𝒪 ⁡ ( κ 1 ​ κ 2 5 K ) + Θ ⁡ ( Δ ​ w min ) . \displaystyle E_{K}\leq\mathcal{O}\left(\frac{\kappa_{1}\kappa_{2}^{5}}{\sqrt{K}}\right)+{\Theta}(\Delta w_{\min}). (15)

[107] p: where κ 1 := L / μ \kappa_{1}:=L/\mu and κ 2 := q max / q min \kappa_{2}:=q_{\max}/q_{\min} are the condition number of the function and device.

[108] p: The proof of Theorem 3.7 is provided in Appendix E . Theorem 3.7 shows that, Algorithm 2 can simultaneously track the SP and perform model training, and the minimal achievable training error ‖ W k − W ∗ ‖ 2 ≤ δ \|W_{k}-W^{*}\|^{2}\leq\delta is δ = Θ ⁡ ( Δ ​ w min ) \delta={\Theta}(\Delta w_{\min}) . Moreover, the convergence rate of Algorithm 2 matches that of Residual Learning ( Wu et al., 2025 ) , although we address a more challenging setting with nonzero and unknown SP.

[109] h6: Remark 3.8 .

[110] p: As a theoretical baseline, we consider Residual Learning ( Wu et al., 2025 ) paired with SP estimation via the ZS algorithm, which we refer to as two-stage Residual Learning with ZS algorithm. This two-stage method first estimates a static SP W ^ ⋄ \hat{W}^{\diamond} with ZS and then fixes Q k ≡ W ^ ⋄ Q_{k}\equiv\hat{W}^{\diamond} during training. We provide its pseudocode in Appendix B.1 .

[111] h6: Corollary 3.9 (Overall pulse complexity) .

[112] p: To achieve training accuracy δ ≥ Θ ⁡ ( Δ ​ w min ) \delta\geq{\Theta}(\Delta w_{\min}) , RIDER in Algorithm 2 requires 𝒪 ⁡ ( K ) = 𝒪 ⁡ ( δ − 2 ) {\cal O}(K)={\cal O}(\delta^{-2}) number of pulses, but the two-stage Residual Learning with ZS algorithm requires 𝒪 ⁡ ( K + N ) = 𝒪 ⁡ ( δ − 2 + δ − 1 ​ Δ ​ w min − 1 ) {\cal O}(K+N)={\cal O}(\delta^{-2}+\delta^{-1}\Delta w_{\min}^{-1}) number of pulses.

[113] p: Corollary 3.9 directly follows from Theorem 3.7 and Theorem 2.2 . This corollary suggests that when the target training error δ > Θ ⁡ ( Δ ​ w min ) \delta>\Theta(\Delta w_{\min}) , RIDER offers a clear benefit in pulse complexity. In practical high-precision AIMC devices, Δ ​ w min \Delta w_{\min} is typically engineered to be as small as possible (e.g. Δ ​ w min = 10 − 4 \Delta w_{\min}=~10^{-4} ) to preserve gradient-conversion fidelity ( Rao et al., 2023 ; Sharma et al., 2024 ) , whereas the acceptable training error δ \delta can be substantially larger to enhance generalization. Consequently, RIDER is expected to require fewer pulses than two-stage approaches.

[114] figure: Algorithm 3 Enhanced version of RIDER (E-RIDER) 1: Inputs: initialization P 0 , Q ~ 0 , W 0 P_{0},\tilde{Q}_{0},W_{0} on analog device and Q 0 = Q ~ 0 Q_{0}=\tilde{Q}_{0} on digital device; residual parameter γ \gamma ; response granularity F p ​ ( ⋅ ) , F w ​ ( ⋅ ) , G p ​ ( ⋅ ) , G w ​ ( ⋅ ) F_{p}(\cdot),F_{w}(\cdot),G_{p}(\cdot),G_{w}(\cdot) ; chopper initialization c 0 = 1 c_{0}=1 2: for k = 0 , 1 , … , K − 1 k=0,1,\ldots,K-1 do 3: draw the chopper variable c k c_{k} via ( 17 ) 4: if sign ⁡ ( c k ) ≠ sign ⁡ ( c k − 1 ) \operatorname{sign}(c_{k})\neq\operatorname{sign}(c_{k-1}) then 5: correct Q ~ k = Q k \tilde{Q}_{k}=Q_{k} via weight programming 6: end if 7: sample stochastic gradient ∇ f ​ ( W ¯ k , ξ k ) \nabla f(\bar{W}_{k};\xi_{k}) 8: update P k + 1 P_{k+1} on analog device via ( 18a ) 9: update Q k + 1 Q_{k+1} on digital device via ( 12 ) 10: update W k + 1 W_{k+1} on analog device via ( 18b ) 11: end for 12: outputs: { P K , Q K , W K } \left\{P_{K},Q_{K},W_{K}\right\}

[115] h4: 3.2 Enhancement via Chopping and Filtering

[116] p: To enhance the empirical performance, we will design a variant of Algorithm 2 through chopping and filtering, inspired by ( Rasch et al., 2023 ) .

[117] figure: Table 1: Test accuracy on LeNet-5 (MNIST) of different methods under different reference mean/std. Best results are highlighted in bold. Method 0.05 0.2 0.3 0.4 0.7 1.0 TT-v2 0 75.19 ± 1.0 \pm 1.0 72.62 ± 0.9 \pm 0.9 72.39 ± 1.1 \pm 1.1 71.50 ± 0.6 \pm 0.6 68.55 ± 0.9 \pm 0.9 66.96 ± 1.3 \pm 1.3 AGAD 90.81 ± 0.2 \pm 0.2 90.69 ± 1.1 \pm 1.1 91.02 ± 0.7 \pm 0.7 90.42 ± 0.7 \pm 0.7 90.15 ± 0.3 \pm 0.3 88.11 ± 0.3 \pm 0.3 E-RIDER 93.75 ± 0.1 \pm 0.1 93.71 ± 0.2 \pm 0.2 94.15 ± 0.6 \pm 0.6 93.26 ± 1.3 \pm 1.3 91.67 ± 0.3 \pm 0.3 89.02 ± 0.3 \pm 0.3 TT-v2 0.2 75.01 ± 1.4 \pm 1.4 72.60 ± 2.1 \pm 2.1 71.68 ± 2.2 \pm 2.2 70.70 ± 1.1 \pm 1.1 66.54 ± 2.9 \pm 2.9 66.43 ± 1.3 \pm 1.3 AGAD 91.14 ± 0.8 \pm 0.8 90.66 ± 0.9 \pm 0.9 91.61 ± 0.1 \pm 0.1 90.61 ± 0.9 \pm 0.9 88.59 ± 0.6 \pm 0.6 87.73 ± 1.1 \pm 1.1 E-RIDER 93.90 ± 0.6 \pm 0.6 93.06 ± 1.0 \pm 1.0 93.33 ± 0.8 \pm 0.8 93.15 ± 0.5 \pm 0.5 91.99 ± 0.1 \pm 0.1 89.41 ± 0.8 \pm 0.8 TT-v2 0.3 73.64 ± 0.5 \pm 0.5 72.50 ± 1.1 \pm 1.1 72.66 ± 0.3 \pm 0.3 70.70 ± 1.7 \pm 1.7 65.43 ± 2.5 \pm 2.5 66.78 ± 1.6 \pm 1.6 AGAD 90.86 ± 0.4 \pm 0.4 89.87 ± 0.4 \pm 0.4 90.37 ± 1.2 \pm 1.2 89.42 ± 0.8 \pm 0.8 89.43 ± 1.2 \pm 1.2 86.76 ± 0.4 \pm 0.4 E-RIDER 92.45 ± 1.9 \pm 1.9 92.15 ± 1.5 \pm 1.5 92.27 ± 0.6 \pm 0.6 91.45 ± 1.1 \pm 1.1 89.74 ± 0.7 \pm 0.7 90.26 ± 1.2 \pm 1.2 TT-v2 0.4 71.71 ± 1.8 \pm 1.8 71.89 ± 3.3 \pm 3.3 70.83 ± 3.1 \pm 3.1 71.01 ± 2.8 \pm 2.8 66.63 ± 1.2 \pm 1.2 67.08 ± 1.6 \pm 1.6 AGAD 89.63 ± 1.3 \pm 1.3 89.79 ± 1.1 \pm 1.1 89.99 ± 1.9 \pm 1.9 90.16 ± 0.8 \pm 0.8 87.32 ± 1.2 \pm 1.2 86.54 ± 1.1 \pm 1.1 E-RIDER 91.72 ± 0.4 \pm 0.4 91.76 ± 0.4 \pm 0.4 91.29 ± 1.1 \pm 1.1 91.54 ± 1.5 \pm 1.5 91.17 ± 0.5 \pm 0.5 88.02 ± 0.3 \pm 0.3

[118] p: From the digital signal processing perspective, we can treat P k P_{k} and Q k Q_{k} as two time-domain signals, and view the mapping from P k P_{k} to Q k Q_{k} as a difference equation system ( Proakis, 2007 ) . Then the following lemma shows that this system can filter out the high-frequency signal components in P k P_{k} .

[119] h6: Lemma 3.10 .

[120] p: The moving average update ( 12 ) defines a stable low-pass filter from P k P_{k} to Q k Q_{k} with the following magnitude of the frequency response

[121] table: | H ⁡ ( e j ​ ω ) | 2 = η 2 1 + ( 1 − η ) 2 − 2 ​ ( 1 − η ) ​ cos ⁡ ω . \displaystyle|H(e^{j\omega})|^{2}=\frac{\eta^{2}}{1+(1-\eta)^{2}-2(1-\eta)\cos\omega}. (16)

[122] p: The proof of this lemma is provided in Appendix D.2 . Observing that the magnitude response is maximized at zero frequency ( ω = 0 \omega=0 ) and minimized at the high frequency ( ω = ± π \omega=\pm\pi ), the moving average operator functions as a low-pass filter. Consequently, it effectively attenuates the high-frequency (sign-flipping) components of P k P_{k} .

[123] p: This motivates us to use a chopper variable to further diversify the frequency for the two components in the P k P_{k} update and keep the SP drifting part in the low-frequency band. Specifically, let us define the chopper variable c k c_{k} that flips the sign with probability (w. p.) p ∈ ( 0 , 1 ) p\in(0,1) , i.e.

[124] table: c k + 1 = { c k , w. p. ​ 1 − p , − c k , w. p. ​ p . \displaystyle c_{k+1}=\begin{cases}c_{k},~~~~&\text{w. p. }~~~1-p,\\ -c_{k},~~~~&\text{w. p. }~~~p.\end{cases} (17)

[125] p: With W ¯ k = W k + γ ​ c k ​ ( P k − Q k ) \bar{W}_{k}=W_{k}+\gamma c_{k}(P_{k}-Q_{k}) , the update ( 11 ) becomes

[126] p: Frequency domain interpretation. In the frequency domain, P k P_{k} comprises two distinct components: a high-frequency, sign-flipping term (corresponding to c k ∇ f ( W ¯ k ; ξ k ) ⊙ F p ( P k ) c_{k}\nabla f(\bar{W}_{k};\xi_{k})\odot F_{p}(P_{k}) ) and a low-frequency, slowly varying term (corresponding to | c k ∇ f ( W ¯ k ; ξ k ) | ⊙ G p ( P k ) |c_{k}\nabla f(\bar{W}_{k};\xi_{k})|\odot G_{p}(P_{k}) ). The crucial distinction is that the absolute value in the second term eliminates sign changes, causing it to accumulate non-negatively rather than oscillating. Following Lemma 3.10 , applying a moving average to P k P_{k} acts as a low-pass filter, which results in the Q k Q_{k} sequence suppressing the sign-flipping component and retaining the low-frequency signals only; see Figure 3 . As the low-frequency component of the P k P_{k} update is a scaled increment proportional to G p ​ ( P k ) G_{p}(P_{k}) , it forces the Q k Q_{k} drifting towards the SP of the P P device faster.

[127] p: Furthermore, to stabilize the updates of W ¯ k \bar{W}_{k} , we incorporate the chopper c k c_{k} directly into the W ¯ k \bar{W}_{k} update rule - a novel modification compared to prior works ( Wu et al., 2025 ; Rasch et al., 2023 ) . This is because the update term c k ​ ( P k − Q k ) c_{k}(P_{k}-Q_{k}) is stable and (approximately) aligned in sign of ∇ f ​ ( W ¯ k ) \nabla f(\bar{W}_{k}) , which is independent of the flipping. Together, chopping and filtering help the Q k Q_{k} sequence converge to W ⋄ W^{\diamond} faster while ensuring the objective descent for W ¯ k \bar{W}_{k} , yielding enhanced empirical performance.

[128] p: Practical implementation. As Q k Q_{k} is stored on the digital device, but P k P_{k} and W k W_{k} are stored on the analog device, computing P k − Q k P_{k}-Q_{k} and P k + 1 − Q k P_{k+1}-Q_{k} requires frequent weight programming. To reduce this cost, we store a fake Q ~ k \tilde{Q}_{k} on an additional analog device and only periodically correct it using the digitally stored Q k Q_{k} when the sign of c k c_{k} flips. Overall, the weight programming cost of the E-RIDER is the same order as the existing dynamic SP tracking method AGAD ( Rasch et al., 2023 ) , and the difference of them is summarized in Appendix B.2 . We summarize the Enhanced RIDER (E-RIDER) algorithm in Algorithm 3 .

[129] figure: Figure 3: Chopping and filtering via moving average.

[130] h3: 4 Experiments

[131] figure: Figure 4: (Left) total pulse cost to reach the target training loss 0.2 0.2 on LeNet-5 (MNIST) across different number of states settings. Solid bars indicate the number of pulses using ZS algorithm, while hatched bars indicate the training cost computed as epochs × ⌈ data size / B ⌉ × BL \text{epochs}\times\lceil\text{data size}/B\rceil\times\mathrm{BL} , with batch size B = 64 B=64 and an average update pulse length BL = 5 \mathrm{BL}=5 . For 2000 2000 states, ZS ( N = 4000 N=4000 ) fails to reach the target loss. (Middle & right) training loss of E-RIDER and baselines under different reference std/mean on ResNet-18 (CIFAR-100) after 80 epochs.

[132] p: We evaluate our method on MNIST using a fully analog LeNet-5 and a fully analog fully connected network, and on CIFAR-100 by training a ResNet-18 with the fully connected layer and the last residual block implemented in analog. All experiments are implemented in the AIHWKit simulator Rasch et al. (2021) . Note that RIDER is a special case of E-RIDER with p = 0 p=0 . As shown in the Appendix F.4 , using a small p > 0 p>0 yields a clear improvement in training performance, so we use E-RIDER with the best-tuned p p in all subsequent experiments. For fairness, we also tune the chopper probability p > 0 p>0 for the dynamic SP tracking baseline AGAD ( Rasch et al., 2023 ) .

[133] figure: Table 2: Test accuracy on FCN (MNIST) for different algorithms under different reference mean/std. Best results are highlighted in bold. Method 0.05 0.2 0.3 0.4 0.7 1.0 TT-v2 0 90.26 ± 0.4 \pm 0.4 88.75 ± 0.6 \pm 0.6 87.40 ± 0.7 \pm 0.7 85.98 ± 0.2 \pm 0.2 82.85 ± 2.4 \pm 2.4 79.20 ± 3.2 \pm 3.2 AGAD 92.59 ± 0.2 \pm 0.2 91.96 ± 0.8 \pm 0.8 92.11 ± 0.9 \pm 0.9 92.48 ± 0.1 \pm 0.1 92.19 ± 0.4 \pm 0.4 91.37 ± 0.4 \pm 0.4 E-RIDER 95.45 ± 0.2 \pm 0.2 95.48 ± 0.1 \pm 0.1 95.39 ± 0.1 \pm 0.1 95.34 ± 0.4 \pm 0.4 95.42 ± 0.3 \pm 0.3 93.86 ± 0.2 \pm 0.2 TT-v2 0.2 73.37 ± 0.3 \pm 0.3 73.99 ± 0.7 \pm 0.7 71.88 ± 0.4 \pm 0.4 70.40 ± 0.8 \pm 0.8 68.63 ± 1.1 \pm 1.1 62.35 ± 0.6 \pm 0.6 AGAD 92.86 ± 1.3 \pm 1.3 91.95 ± 0.4 \pm 0.4 92.63 ± 0.7 \pm 0.7 92.80 ± 0.2 \pm 0.2 92.22 ± 0.3 \pm 0.3 90.77 ± 0.3 \pm 0.3 E-RIDER 95.78 ± 0.1 \pm 0.1 95.63 ± 0.1 \pm 0.1 95.84 ± 0.3 \pm 0.3 95.82 ± 0.3 \pm 0.3 95.82 ± 0.3 \pm 0.3 95.18 ± 0.3 \pm 0.3 TT-v2 0.3 72.86 ± 1.3 \pm 1.3 72.65 ± 0.5 \pm 0.5 69.70 ± 1.6 \pm 1.6 69.96 ± 1.5 \pm 1.5 66.44 ± 2.0 \pm 2.0 61.45 ± 1.0 \pm 1.0 AGAD 92.31 ± 0.4 \pm 0.4 92.52 ± 0.4 \pm 0.4 92.47 ± 0.5 \pm 0.5 92.88 ± 0.3 \pm 0.3 91.68 ± 0.5 \pm 0.5 91.35 ± 0.4 \pm 0.4 E-RIDER 95.76 ± 0.1 \pm 0.1 95.81 ± 0.5 \pm 0.5 95.91 ± 0.6 \pm 0.6 95.88 ± 0.1 \pm 0.1 95.79 ± 0.2 \pm 0.2 94.84 ± 0.2 \pm 0.2 TT-v2 0.4 72.00 ± 2.8 \pm 2.8 68.08 ± 2.1 \pm 2.1 68.80 ± 1.9 \pm 1.9 67.85 ± 1.4 \pm 1.4 66.15 ± 0.9 \pm 0.9 57.79 ± 0.8 \pm 0.8 AGAD 92.55 ± 0.2 \pm 0.2 92.42 ± 0.6 \pm 0.6 92.42 ± 0.8 \pm 0.8 92.06 ± 0.4 \pm 0.4 90.62 ± 0.3 \pm 0.3 90.43 ± 0.3 \pm 0.3 E-RIDER 96.07 ± 0.2 \pm 0.2 96.21 ± 0.1 \pm 0.1 96.20 ± 0.1 \pm 0.1 96.23 ± 0.3 \pm 0.3 95.87 ± 0.3 \pm 0.3 95.14 ± 0.3 \pm 0.3

[134] p: E-RIDER achieves better overall pulse complexity. We conduct an ablation study on LeNet-5 (MNIST) with a convergence criterion of training loss ≤ 0.2 \leq 0.2 . Figure 4 (left) reports the total pulse cost required to reach this target for E-RIDER and the two-stage TT-v2 Gokmen (2021) with ZS algorithm under different numbers of device states. For the two-stage ZS approach, the total pulse cost is the sum of N N pulses for SP estimation and the subsequent training pulses, determined by the number of training epochs K K when training with TT-v2 after calibration. When the number of states is low ( Δ ​ w min \Delta w_{\min} is large), SP estimation with fewer pulses (e.g., N = 4000 N=4000 ) leads to better convergence than using larger N N , which consists with Theorem 2.2 . However, as the number of states increases (smaller Δ ​ w min \Delta w_{\min} ), the two-stage ZS approach becomes more expensive because accurate SP estimation requires a larger pulse budget; for 2000 2000 states, ZS with N = 4000 N=4000 pulses fails to meet the training target loss. Meanwhile, E-RIDER consistently achieves a lower total pulse cost across all settings.

[135] p: E-RIDER is robust to nonzero SP. We conduct an ablation study on the robustness of E-RIDER to a nonzero SP reference. The device model follows the RRAM-RfO 2 preset Gong et al. (2022) to emulate practical update non-idealities in filamentary RRAM. We focus on a limited-state scenario where the number of states is ∼ \sim 4–5. It also mimics the strong device-to-device mismatch and cycle-to-cycle writing noise. We initialize W ⋄ W^{\diamond} by sampling each entry W i ​ j W_{ij} i.i.d. from a Gaussian distribution with varying reference mean (Ref Mean) and standard deviation (Ref Std) to model different nonzero SP scenarios. We compare E-RIDER with both TT-v2 and AGAD, summarizing the test accuracy after 40 epochs in Tables 1 and 2 . Each setting is repeated three times, and we report the sample mean and standard deviation results; the hyperparameters are both tuned to optimum (See Appendix F.2 for details). The results demonstrate that: 1) TT-v2 exhibits a substantial accuracy gap to both AGAD and E-RIDER, and its performance degrades markedly as the reference mean/std offsets increase. This is expected because TT-v2 cannot compensate for nonzero reference offsets. 2) E-RIDER consistently outperforms TT-v2 and AGAD in all reference mean/std offset settings, especially with larger SP offset. This is because E-RIDER dynamically tracks SP, and further improves training under low-state devices, which increases the effective weight resolution and enables more accurate gradient updates.

[136] p: We further evaluate the robustness of our method on CIFAR-100 using a ResNet-18 trained for 80 epochs. We first fix the reference mean to 0.4 and sweep the reference standard deviation, and then fix the reference standard deviation to 0.4 and sweep the reference mean. The results are summarized in Figure 4 (middle & right). We observe similar trends: 1) TT-v2 suffers from a significant degrade in testing accuracy as the reference standard deviation and mean grows, whereas AGAD and E-RIDER remain more stable. 2) E-RIDER consistently achieves higher testing accuracy than both TT-v2 and AGAD, especially for large SP offset.

[137] h3: 5 Conclusions

[138] p: In this paper, we characterize the pulse complexity of ZS algorithm and quantify how the required number of pulse updates for achieving a certain target SP estimation error scales with device response granularity Δ ​ w min \Delta w_{\min} . Building on these insights, we propose a dynamic SP tracking algorithm, RIDER, which estimates the SP during training, achieving target training accuracy with substantially fewer pulse updates than the two-stage analog training approaches theoretically. We further develop an enhanced variant of RIDER that accelerates SP tracking through chopper-and-filtering, while reducing weight programming overhead by periodical synchronization. Numerical experiments validate the efficiency and effectiveness of the proposed E-RIDER.

[139] h3: Impact Statement

[140] p: This paper aims to advance AIMC training via dynamic SP tracking, providing a principled algorithmic framework to mitigate update asymmetry and device drift during learning. By addressing the key challenges in dynamic SP estimation and calibration, our work contributes to the broader development of more robust and hardware-aware training methods for energy-efficient AIMC accelerators. Potential societal impacts include enabling lower-power AI training and adaptation at the edge, reducing the energy and carbon footprint of AI workloads. While we acknowledge the possibility of unintended uses, we do not identify any specific societal risks that need to be highlighted in this context.

[141] h3: Acknowledgement

[142] p: The work was supported by the National Science Foundation Projects 2401297 and 2532349, by NVIDIA Academic Grant, by IBM through the IBM-Rensselaer Future of Computing Research Collaboration, and by Cisco Research.

[143] h3: References

[144] p: Appendix for “Dynamic Symmetric Point Tracking: Tackling Non-ideal Reference in Analog In-memory Training”

[145] h3: Appendix A Notations and Preliminaries

[146] p: In this section, we define a series of notations that will be used in the analysis.

[147] p: Pseudo-inverse of diagonal matrix or vector. For a given diagonal matrix U ∈ ℝ D × D U\in{\mathbb{R}}^{D\times D} with its d d -th diagonal element [ U ] d [U]_{d} , we define the pseudo-inverse of a diagonal matrix U U as U † U^{\dagger} , which is also a diagonal matrix with its d d -th diagonal element

[148] table: [ U † ] d := { 1 / [ U ] d , [ U ] d ≠ 0 , 0 , [ U ] d = 0 . \displaystyle[U^{\dagger}]_{d}:=\begin{cases}1/[U]_{d},~~~&{[U]_{d}\neq 0},\\ 0,~~~&{[U]_{d}=0}.\end{cases} (19)

[149] p: By definition, the pseudo-inverse satisfies U ​ U † ​ V = U † ​ U ​ V UU^{\dagger}V=U^{\dagger}UV for any diagonal matrix U ∈ ℝ D U\in{\mathbb{R}}^{D} and any matrix V ∈ ℝ D V\in{\mathbb{R}}^{D} . With a slight abuse of notation, we also define the pseudo-inverse of a vector W ∈ ℝ D W\in{\mathbb{R}}^{D} as W † := diag ​ ( W ) † W^{\dagger}:=\text{diag}(W)^{\dagger} .

[150] p: Weighted norm. For a weight M ∈ ℝ + D M\in{\mathbb{R}}^{D}_{+} , the weighted norm ∥ ⋅ ∥ M \|\cdot\|_{M} of W ∈ ℝ D W\in{\mathbb{R}}^{D} is defined by

[151] table: ‖ W ‖ M := ∑ d = 1 D [ M ] d ​ [ W ] d 2 = W ⊤ ​ Diag ​ ( M ) ​ W \displaystyle\|W\|_{M}:=\sqrt{\sum_{d=1}^{D}[M]_{d}[W]_{d}^{2}}=\sqrt{W^{\top}\text{Diag}(M)W} (20)

[152] p: where Diag ​ ( M ) ∈ ℝ D × D \text{Diag}(M)\in{\mathbb{R}}^{D\times D} rearranges the vector M ∈ ℝ D M\in{\mathbb{R}}^{D} into a diagonal matrix.

[153] h6: Lemma A.1 ( ( Wu et al., 2025 , Lemma 1) ) .

[154] p: ‖ W ‖ M \|W\|_{M} has the following properties: (a) ‖ W ‖ M = ‖ W ⊙ M ‖ \|W\|_{M}=\|W\odot\sqrt{M}\| ; (b) ‖ W ‖ M ≤ ‖ W ‖ ​ ‖ M ‖ ∞ \|W\|_{M}\leq\|W\|\sqrt{\|M\|_{\infty}} ; (c) ∥ W ∥ M ≥ ∥ W ∥ min { [ M ] d : k ∈ [ K ] , d ∈ [ D ] } \|W\|_{M}\geq\|W\|\sqrt{\min\{[M]_{d}:k\in[K],d\in[D]\}} .

[155] h6: Lemma A.2 ( ( Wu et al., 2025 , Lemma 2) ) .

[156] p: Consider response functions in Definition 2.1 , the increment defined in ( 2 ) is Lipschitz continuous with respect to Δ ​ W \Delta W under any weighted norm ∥ ⋅ ∥ M \|\cdot\|_{M} , i.e., for any W , Δ ​ W , Δ ​ W ′ ∈ ℝ D W,\Delta W,\Delta W^{\prime}\in{\mathbb{R}}^{D} and M ∈ ℝ + D M\in{\mathbb{R}}^{D}_{+} , it holds

[157] table: ‖ Δ ​ W ⊙ F ⁡ ( W ) − | Δ ​ W | ⊙ G ⁡ ( W ) − ( Δ ​ W ′ ⊙ F ⁡ ( W ) − | Δ ​ W ′ | ⊙ G ⁡ ( W ) ) ‖ M ≤ \displaystyle\|\Delta W\odot F(W)-|\Delta W|\odot G(W)-(\Delta W^{\prime}\odot F(W)-|\Delta W^{\prime}|\odot G(W))\|_{M}\leq q max ​ ‖ Δ ​ W − Δ ​ W ′ ‖ M . \displaystyle\ q_{\max}\|\Delta W-\Delta W^{\prime}\|_{M}.

[158] h3: Appendix B Discussion of Algorithms

[159] p: In this section, we discuss some implementation details of algorithms.

[160] h4: B.1 Two-stage analog training approach: Residual Learning with ZS algorithm

[161] p: The two-stage analog training algorithm consists of an independent SP estimation stage that uses Algorithm 1 to obtain a static SP estimate W ^ ⋄ \hat{W}^{\diamond} , and an independent training stage that applies residual learning with W ^ ⋄ \hat{W}^{\diamond} fixed; i.e. we remove the Q k Q_{k} -sequence update in Algorithm 2 and set Q k ≡ W ^ ⋄ Q_{k}\equiv\hat{W}^{\diamond} . We give a pseudo-code for this algorithm in Algorithm 4 .

[162] figure: Algorithm 4 Two-stage analog training algorithm 1: Inputs: initialization P 0 , Q 0 , W 0 P_{0},Q_{0},W_{0} ; residual parameter γ \gamma ; response granularity F p ​ ( ⋅ ) , F w ​ ( ⋅ ) , G p ​ ( ⋅ ) , G w ​ ( ⋅ ) F_{p}(\cdot),F_{w}(\cdot),G_{p}(\cdot),G_{w}(\cdot) 2: estimate W ^ ⋄ \hat{W}^{\diamond} by Algorithm 1 with N N number of pulses 3: for k = 0 , 1 , … , K − 1 k=0,1,\ldots,K-1 do 4: evaluate W ¯ k = W k + γ ⁡ ( P k − Q k ) \bar{W}_{k}=W_{k}+\gamma(P_{k}-Q_{k}) 5: sample stochastic gradient ∇ f ​ ( W ¯ k , ξ k ) \nabla f(\bar{W}_{k};\xi_{k}) 6: update P k + 1 P_{k+1} on analog device via ( 11a ) 7: set Q k + 1 = W ^ ⋄ Q_{k+1}=\hat{W}^{\diamond} 8: update W k + 1 W_{k+1} on analog device via ( 11b ) 9: end for 10: outputs: { P K , Q K , W K } \left\{P_{K},Q_{K},W_{K}\right\}

[163] h4: B.2 Comparison of E-RIDER, Residual Learning/TT-v2 and AGAD

[164] p: The proposed E-RIDER has a similar form of AGAD Rasch et al. (2023) . However, AGAD uses the gradient ∇ f ​ ( W k , ξ k ) \nabla f(W_{k};\xi_{k}) that are solely computed on the main array W k W_{k} . Instead, E-RIDER computes gradient on a mixed weight W ¯ k = W k + γ ​ c k ​ ( P k − Q k ) \bar{W}_{k}=W_{k}+\gamma c_{k}(P_{k}-Q_{k}) so that achieves better performance in simulation. The key reason is that introducing the residual term γ ​ c k ​ ( P k − Q k ) \gamma c_{k}(P_{k}-Q_{k}) with a nonzero γ \gamma effectively rescales the update, yielding a finer effective dynamic range and granularity than the raw device response. Moreover, this zero-shifting vector mitigates update asymmetry through the bilevel optimization. In simulation, we show that E-RIDER which uses the gradient evaluated at the mixed weight improves test accuracy, especially when the SP is substantially nonzero.

[165] p: Compared with Residual Learning ( Wu et al., 2025 ) , E-RIDER uses a moving average sequence to track the SP and adds a chopper mechanism to amplify the SP tracking performance. From a theoretical perspective, Residual Learning fails to converge when the SP is nonzero, whereas E-RIDER with p = 0 p=0 is guaranteed to converge in our paper. Empirically, Residual Learning performs similarly to TT-v2, and both suffer substantial performance degradation under nonzero SP.

[166] h4: B.3 Failure of dynamic zero-shifting algorithm design.

[167] p: From an optimization perspective, to balance the pulse overhead of SP estimation and model training, a natural approach is to integrate Algorithm 1 into analog training algorithms via multi-sequence updates Yang et al. (2019) ; Shen and Chen (2022) , enabling dynamic SP estimation during the model training process. However, this approach is infeasible in analog training because each update sequence is executed on a different device, and the SP is device-specific. As a result, the SP tracked by the zero-shifting Algorithm 1 cannot be directly transferred to the sequence used for model training.

[168] h3: Appendix C Proof of Convergence Rate of Algorithm 1 and Cyclic Version

[169] h4: C.1 Proof of Theorem 2.2 : Convergence rate of Algorithm 1

[170] p: See 2.2

[171] h6: Theorem 2.2 .

[172] p: Define the following notations:

[173] table: φ ⁡ ( W ) := ∫ W ⋄ W G ⁡ ( W ′ ) ​ d ​ W ′ , ∇ φ ​ ( W ) := G ⁡ ( W ) , L q := max W ⁡ Δ ​ G ​ ( W ) . \displaystyle\varphi(W):=\int_{W^{\diamond}}^{W}G(W^{\prime})dW^{\prime},\qquad\nabla\varphi(W):=G(W),\qquad L_{q}:=\max_{W}\Delta G(W). (21)

[174] p: Under gradient boundedness implied by Definition 2.1 , it holds that:

[175] table: φ ⁡ ( W n + 1 ) \displaystyle\varphi(W_{n+1}) ≤ φ ⁡ ( W n ) + ⟨ ∇ φ ​ ( W n ) , W n + 1 − W n ⟩ + L q 2 ​ ‖ W n + 1 − W n ‖ 2 \displaystyle\leq\varphi(W_{n})+\left\langle\nabla\varphi(W_{n}),\,W_{n+1}-W_{n}\right\rangle+\frac{L_{q}}{2}\left\|W_{n+1}-W_{n}\right\|^{2} = φ ⁡ ( W n ) + ⟨ G ⁡ ( W n ) , ε n ​ F ​ ( W n ) − | ε n | ​ G ​ ( W n ) ⟩ + L q 2 ​ ‖ ε n ​ F ​ ( W n ) − | ε n | ​ G ​ ( W n ) ‖ 2 . \displaystyle=\varphi(W_{n})+\left\langle G(W_{n}),\,\varepsilon_{n}F(W_{n})-|\varepsilon_{n}|G(W_{n})\right\rangle+\frac{L_{q}}{2}\left\|\varepsilon_{n}F(W_{n})-|\varepsilon_{n}|G(W_{n})\right\|^{2}. (22)

[176] p: where L q L_{q} is the gradient boundedness constant implied by Definition 2.1 . The equality holds by substituting the stochastic updating equation ( 7 ). Taking expectation over ε n \varepsilon_{n} on both sides, we get:

[177] table: 𝔼 ⁡ [ φ ⁡ ( W n + 1 ) ∣ W n ] \displaystyle\mathbb{E}\!\left[\varphi(W_{n+1})\mid W_{n}\right] ≤ φ ⁡ ( W n ) − 𝔼 ⁡ [ | ε n | ] ​ ‖ G ⁡ ( W n ) ‖ 2 + L q 2 ​ Δ ​ w min 2 ​ q max 2 \displaystyle\leq\varphi(W_{n})-\mathbb{E}[|\varepsilon_{n}|]\;\|G(W_{n})\|^{2}+\frac{L_{q}}{2}\Delta w_{\min}^{2}q_{\max}^{2} = φ ⁡ ( W n ) − Δ ​ w min ​ ‖ G ⁡ ( W n ) ‖ 2 + L q 2 ​ Δ ​ w min 2 ​ q max 2 \displaystyle=\varphi(W_{n})-\Delta w_{\min}\;\|G(W_{n})\|^{2}+\frac{L_{q}}{2}\Delta w_{\min}^{2}q_{\max}^{2} ≤ φ ⁡ ( W n ) − Δ ​ w min ​ ‖ G ⁡ ( W n ) ‖ 2 + L q 2 ​ Δ ​ w min 2 ​ q max 2 . \displaystyle\leq\varphi(W_{n})-\Delta w_{\min}\;\|G(W_{n})\|^{2}+\frac{L_{q}}{2}\Delta w_{\min}^{2}q_{\max}^{2}. (23)

[178] p: Taking total expectation ℱ n \mathcal{F}_{n} to both sides of ( 23 ) and using 𝔼 ⁡ [ 𝔼 ⁡ [ φ ⁡ ( W n + 1 ) ∣ ℱ n ] ] = 𝔼 ⁡ [ φ ⁡ ( W n + 1 ) ] \mathbb{E}\left[\mathbb{E}\left[\varphi(W_{n+1})\mid\mathcal{F}_{n}\right]\right]=\mathbb{E}\left[\varphi(W_{n+1})\right] , we get:

[179] table: 𝔼 ⁡ [ φ ⁡ ( W n + 1 ) ] \displaystyle\mathbb{E}\!\left[\varphi(W_{n+1})\right] ≤ 𝔼 ⁡ [ φ ⁡ ( W n ) ] − Δ ​ w min ​ 𝔼 ​ [ ‖ G ⁡ ( W n ) ‖ 2 ] + L q 2 ​ Δ ​ w min 2 ​ q max 2 . \displaystyle\leq\mathbb{E}\left[\varphi(W_{n})\right]-\Delta w_{\min}\mathbb{E}\left[\|G(W_{n})\|^{2}\right]+\frac{L_{q}}{2}\Delta w_{\min}^{2}q_{\max}^{2}. (24)

[180] p: Taking average over all n n form 0 0 to N − 1 N-1 , we get:

[181] table: 1 N ​ ∑ n = 0 N − 1 𝔼 ⁡ [ ‖ G ⁡ ( W n ) ‖ 2 ] \displaystyle\frac{1}{N}\sum_{n=0}^{N-1}\mathbb{E}\left[\|G(W_{n})\|^{2}\right] ≤ φ ⁡ ( W 0 ) − φ ⁡ ( W ∗ ) N ​ Δ ​ w min + L q 2 ​ Δ ​ w min ​ q max 2 \displaystyle\leq\frac{\varphi(W_{0})-\varphi(W^{*})}{N\Delta w_{\min}}+\frac{L_{q}}{2}\Delta w_{\min}q_{\max}^{2} (25)

[182] p: which completes the proof. ∎

[183] h4: C.2 Proof of Theorem C.2 : Last-iterate convergence of Algorithm 1

[184] p: To get the enhanced last-iterate pulse complexity for Algorithm 1 , we focus on the family of devices with the following monotone response functions.

[185] h6: Definition C.1 (Monotone response functions) .

[186] p: Response functions q + ​ ( ⋅ ) q_{+}(\,\cdot\,) and q − ​ ( ⋅ ) q_{-}(\,\cdot\,) are said to be monotone with modulus μ q > 0 \mu_{q}>0 if

[187] table: ∇ q − ( w ) ≥ μ q , and ∇ q + ( w ) ≤ − μ q . \displaystyle\nabla q_{-}(w)\geq\mu_{q},~~\text{ and }~~\nabla q_{+}(w)\leq-\mu_{q}. (26)

[188] p: Definition C.1 suggests that q − ​ ( ⋅ ) q_{-}(\cdot) is monotonically increasing and q + ​ ( ⋅ ) q_{+}(\cdot) is monotonically decreasing. The response functions of a wide range of AIMC devices, such as linear, exponential, and power device, satisfy Definition C.1 ( Wu et al., 2025 ) . With Definition C.1 , G ⁡ ( W ) G(W) is strongly monotone with μ q \mu_{q} so that we have the following last-iterates convergence.

[189] h6: Theorem C.2 (Last-iterate convergence of Algorithm 1 ) .

[190] p: Considering the response functions satisfying Definition 2.1 and C.1 and assuming μ g < 1 2 ​ Δ ​ w min \mu_{g}<\frac{1}{2\Delta w_{\min}} , then to achieve 𝔼 ⁡ [ ‖ W N − W ⋄ ‖ 2 ] ≤ δ \mathbb{E}[\|W^{N}-W^{\diamond}\|^{2}]\leq\delta , we need

[191] table: N ≤ 1 2 ​ μ q ​ Δ ​ w min ​ log ⁡ ( 2 ​ ‖ W 0 − W ⋄ ‖ 2 δ ) . \displaystyle N\leq\frac{1}{2\mu_{q}\Delta w_{\min}}\log\left(\frac{2\|W^{0}-W^{\diamond}\|^{2}}{\delta}\right).

[192] p: and the minimal achievable error δ \delta is δ = 2 ​ q max 2 ​ Δ ​ w min μ q \delta=\frac{2q_{\max}^{2}\Delta w_{\min}}{\mu_{q}} .

[193] p: From Theorem C.2 , we know that the zero-shifting Algorithm 1 achieves a sublinear dependence on the target error δ \delta , and that the required number of pulses scales linearly with 1 / Δ ​ w min 1/\Delta w_{\min} . In practice, the response granularity Δ ​ w min \Delta w_{\min} of AIMC device is made sufficiently small to ensure the gradient conversion precision ( Rao et al., 2023 ; Sharma et al., 2024 ) , so that the computational complexity of Algorithm 1 is relatively high.

[194] h6: Theorem C.2 .

[195] p: We begin the proof by one step descent form stochastic updating equation ( 7 ) and taking expectation over ε n \varepsilon_{n} on both sides:

[196] table: 𝔼 ⁡ [ ‖ W n + 1 − W ⋄ ‖ 2 | W n ] \displaystyle\quad\mathbb{E}\!\left[\left\|W_{n+1}-W^{\diamond}\right\|^{2}\,|\,W_{n}\right] = 𝔼 ⁡ [ ‖ W n − Δ ​ w min ​ ε n ​ F ​ ( W n ) − Δ ​ w min ​ G ​ ( W n ) − W ⋄ ‖ 2 | W n ] \displaystyle=\mathbb{E}\!\left[\left\|W_{n}-\Delta w_{\min}\varepsilon_{n}F(W_{n})-\Delta w_{\min}G(W_{n})-W^{\diamond}\right\|^{2}\,|\,W_{n}\right] = ‖ W n − W ⋄ ‖ 2 − 2 ​ Δ ​ w min ​ ⟨ W n − W ⋄ , G ⁡ ( W n ) − G w ​ ( W ⋄ ) ⟩ + Δ ​ w min 2 ​ 𝔼 ​ [ ‖ ε n ​ F ​ ( W n ) + G ⁡ ( W n ) ‖ 2 | W n ] \displaystyle=\left\|W_{n}-W^{\diamond}\right\|^{2}-2\Delta w_{\min}\left\langle W_{n}-W^{\diamond},\,G(W_{n})-G_{w}(W^{\diamond})\right\rangle+\Delta w_{\min}^{2}\,\mathbb{E}\!\left[\left\|\varepsilon_{n}F(W_{n})+G(W_{n})\right\|^{2}\,|\,W_{n}\right] ≤ ( 1 − 2 ​ Δ ​ w min ​ μ q ) ​ ‖ W n − W ⋄ ‖ 2 + 2 ​ Δ ​ w min 2 ​ q max 2 . \displaystyle\leq(1-2\Delta w_{\min}\mu_{q})\left\|W_{n}-W^{\diamond}\right\|^{2}+2\Delta w_{\min}^{2}q_{\max}^{2}. (27)

[197] p: The second equality holds for 𝔼 ⁡ [ ε n ​ F ​ ( W n ) ] = 0 \mathbb{E}\!\left[\varepsilon_{n}F(W_{n})\right]=0 and G w ​ ( W ⋄ ) = 0 G_{w}(W^{\diamond})=0 . The inequality holds for the strongly convex assumptions in definition C.1 and bounded response functions in definition 2.1 :

[198] table: ⟨ W n − W ⋄ , G ⁡ ( W n ) − G w ​ ( W ⋄ ) ⟩ ≥ μ q ​ ‖ W n − W ⋄ ‖ 2 , 𝔼 ⁡ [ ‖ ε n ​ F ​ ( W n ) + G ⁡ ( W n ) ‖ 2 | W n ] ≤ 2 ​ q max 2 . \left\langle W_{n}-W^{\diamond},\,G(W_{n})-G_{w}(W^{\diamond})\right\rangle\geq\mu_{q}\left\|W_{n}-W^{\diamond}\right\|^{2},\qquad\mathbb{E}\!\left[\left\|\varepsilon_{n}F(W_{n})+G(W_{n})\right\|^{2}\,|\,W_{n}\right]\leq 2q_{\max}^{2}.

[199] p: Taking total expectation ℱ n \mathcal{F}_{n} to both sides of ( 27 ) and iterating this recursion for n = 0 , … , N − 1 n=0,\ldots,N-1 gives:

[200] table: 𝔼 ⁡ [ ‖ W N − W ⋄ ‖ 2 ] \displaystyle\mathbb{E}\!\left[\left\|W_{N}-W^{\diamond}\right\|^{2}\right] ≤ ( 1 − 2 ​ Δ ​ w min ​ μ q ) N ​ ‖ W 0 − W ⋄ ‖ 2 + 2 ​ Δ ​ w min 2 ​ q max 2 ​ ∑ n = 0 N − 1 ( 1 − 2 ​ Δ ​ w min ​ μ q ) n \displaystyle\leq(1-2\Delta w_{\min}\mu_{q})^{N}\left\|W_{0}-W^{\diamond}\right\|^{2}+2\Delta w_{\min}^{2}q_{\max}^{2}\sum_{n=0}^{N-1}(1-2\Delta w_{\min}\mu_{q})^{n} ≤ ( 1 − 2 ​ Δ ​ w min ​ μ q ) N ​ ‖ W 0 − W ⋄ ‖ 2 + Δ ​ w min ​ q max 2 μ q . \displaystyle\leq(1-2\Delta w_{\min}\mu_{q})^{N}\left\|W_{0}-W^{\diamond}\right\|^{2}+\frac{\Delta w_{\min}q_{\max}^{2}}{\mu_{q}}. (28)

[201] p: To ensure that the error bound is below a given tolerance δ \delta , we split the upper bound into two terms and require each of them to be at most δ 2 \frac{\delta}{2} , which means Δ ​ w min ​ q max 2 μ q ≤ δ 2 \frac{\Delta w_{\min}q_{\max}^{2}}{\mu_{q}}\leq\frac{\delta}{2} and ( 1 − 2 ​ μ q ​ Δ ​ w min ) N ​ ‖ W 0 − W ⋄ ‖ 2 ≤ δ 2 (1-2\mu_{q}\Delta w_{\min})^{N}\,\|W_{0}-W^{\diamond}\|^{2}\leq\frac{\delta}{2} .

[202] p: The first inequality holds when Δ ​ w min ≤ δ ​ μ q 2 ​ q max 2 \Delta w_{\min}\leq\frac{\delta\mu_{q}}{2q_{\max}^{2}} . Taking logarithms on both sides of the second inequality gives:

[203] table: log ⁡ ( 2 ​ ‖ W 0 − W ⋄ ‖ 2 δ ) ≤ N ​ log ⁡ ( 1 1 − 2 ​ μ q ​ Δ ​ w min ) . \displaystyle\log\!\left(\frac{2\|W_{0}-W^{\diamond}\|^{2}}{\delta}\right)\leq N\,\log\!\left(\frac{1}{1-2\mu_{q}\Delta w_{\min}}\right). (29)

[204] p: Using the inequality log ⁡ ( 1 p ) ≥ 1 − p \log(\frac{1}{p})\geq 1-p , when μ q < 1 2 ​ Δ ​ w min \mu_{q}<\frac{1}{2\Delta w_{\min}} , it suffices to require

[205] table: N ≥ 1 2 ​ μ q ​ Δ ​ w min ​ log ⁡ ( 2 ​ ‖ W 0 − W ⋄ ‖ 2 δ ) \displaystyle N\geq\frac{1}{2\mu_{q}\Delta w_{\min}}\log\!\left(\frac{2\|W_{0}-W^{\diamond}\|^{2}}{\delta}\right) (30)

[206] p: which completes the proof. ∎

[207] h4: C.3 Proof of Theorem C.3 : Convergence rate of Algorithm 1 , cyclic version

[208] p: In this section, we model the empirical implementation of the zero-shifting technique, where cyclic alternating pulses are applied. We also establish a convergence guarantee analogous to Theorem 2.2 . We first show the update dynamics below:

[209] table: W 2 ​ n \displaystyle W_{2n} = W 2 ​ n − 1 − Δ ​ w min ​ F ​ ( W 2 ​ n − 1 ) − Δ ​ w min ​ G ​ ( W 2 ​ n − 1 ) , \displaystyle=W_{2n-1}-\Delta w_{\min}F(W_{2n-1})-\Delta w_{\min}G(W_{2n-1}), W 2 ​ n + 1 \displaystyle W_{2n+1} = W 2 ​ n + Δ ​ w min ​ F ​ ( W 2 ​ n ) − Δ ​ w min ​ G ​ ( W 2 ​ n ) . \displaystyle=W_{2n}+\Delta w_{\min}F(W_{2n})-\Delta w_{\min}G(W_{2n}). (31)

[210] h6: Theorem C.3 (Convergence rate of Algorithm 1 , cyclic version) .

[211] p: Considering the response functions satisfying Definition 2.1 , then when N = 𝒪 ⁡ ( Δ ​ w min − 2 ​ κ 2 − 2 ) N={\cal O}\left(\Delta w_{\min}^{-2}\kappa_{2}^{-2}\right) , it holds that

[212] table: 1 2 ​ N ​ ∑ n = 0 2 ​ N − 1 ‖ G ⁡ ( W n ) ‖ 2 ≤ φ ⁡ ( W 0 ) − φ ∗ 2 ​ N ​ Δ ​ w min + 3 ​ Δ ​ w min ​ q max 2 ​ L q 2 \displaystyle\frac{1}{2N}\sum_{n=0}^{2N-1}\|G(W_{n})\|^{2}\leq\frac{\varphi(W_{0})-\varphi^{\ast}}{2N\,\Delta w_{\min}}+\frac{3\,\Delta w_{\min}\,q_{\max}^{2}\,L_{q}}{2} (32)

[213] p: where L q L_{q} is the gradient boundedness constant implied by Definition 2.1 . Therefore, the minimal achievable SP estimation error 1 2 ​ N ​ ∑ n = 0 2 ​ N − 1 𝔼 ⁡ [ ‖ G ⁡ ( W n ) ‖ 2 ] ≤ δ \frac{1}{2N}\sum_{n=0}^{2N-1}\mathbb{E}\left[\|G(W_{n})\|^{2}\right]\leq\delta is δ = 𝒪 ⁡ ( Δ ​ w min ) \delta={\cal O}(\Delta w_{\min}) . To achieve error δ ≥ 𝒪 ⁡ ( Δ ​ w min ) \delta\geq{\cal O}(\Delta w_{\min}) , it requires N = 𝒪 ⁡ ( 1 δ ​ Δ ​ w min ) N={\cal O}(\frac{1}{\delta\Delta w_{\min}}) number of pulses.

[214] h6: Theorem C.3 .

[215] p: We begin the proof by using the same notations defined in equation ( 21 ). Under gradient boundedness implied by Definition 2.1 , it holds that:

[216] table: φ ⁡ ( W n + 1 ) \displaystyle\varphi(W_{n+1}) ≤ φ ⁡ ( W n ) + ⟨ ∇ φ ​ ( W n ) , W n + 1 − W n ⟩ + L q 2 ​ ‖ W n + 1 − W n ‖ 2 \displaystyle\leq\varphi(W_{n})+\left\langle\nabla\varphi(W_{n}),\,W_{n+1}-W_{n}\right\rangle+\frac{L_{q}}{2}\left\|W_{n+1}-W_{n}\right\|^{2} = φ ⁡ ( W n ) + Δ ​ w min ​ ⟨ G ⁡ ( W n ) , F ⁡ ( W n ) − G ⁡ ( W n ) ⟩ + L q 2 ​ Δ ​ w min 2 ​ ‖ F ⁡ ( W n ) − G ⁡ ( W n ) ‖ 2 \displaystyle=\varphi(W_{n})+\Delta w_{\min}\left\langle G(W_{n}),\,F(W_{n})-G(W_{n})\right\rangle+\frac{L_{q}}{2}\Delta w_{\min}^{2}\left\|F(W_{n})-G(W_{n})\right\|^{2} ≤ φ ⁡ ( W n ) − Δ ​ w min ​ ‖ G ⁡ ( W n ) ‖ 2 + Δ ​ w min ​ ⟨ G ⁡ ( W n ) , F ⁡ ( W n ) ⟩ + L q 2 ​ Δ ​ w min 2 ​ q max 2 . \displaystyle\leq\varphi(W_{n})-\Delta w_{\min}\left\|G(W_{n})\right\|^{2}+\Delta w_{\min}\left\langle G(W_{n}),\,F(W_{n})\right\rangle+\frac{L_{q}}{2}\Delta w_{\min}^{2}q_{\max}^{2}. (33)

[217] p: The second equality holds by substituting the stochastic updating equation ( 31 ). The inequality holds for F ⁡ ( W n ) − G ⁡ ( W n ) = q + ​ ( W n ) + q − ​ ( W n ) 2 − q + ​ ( W n ) − q − ​ ( W n ) 2 = q + ​ ( W n ) ≤ q max F(W_{n})-G(W_{n})=\frac{q_{+}(W_{n})+q_{-}(W_{n})}{2}-\frac{q_{+}(W_{n})-q_{-}(W_{n})}{2}=q_{+}(W_{n})\leq q_{\max} . Similarly we have:

[218] table: φ ⁡ ( W n + 2 ) \displaystyle\varphi(W_{n+2}) ≤ φ ⁡ ( W n + 1 ) + Δ ​ w min ​ ⟨ G ⁡ ( W n + 1 ) , − F ⁡ ( W n + 1 ) − G ⁡ ( W n + 1 ) ⟩ + L q 2 ​ Δ ​ w min 2 ​ q max 2 \displaystyle\leq\varphi(W_{n+1})+\Delta w_{\min}\left\langle G(W_{n+1}),\,-F(W_{n+1})-G(W_{n+1})\right\rangle+\frac{L_{q}}{2}\Delta w_{\min}^{2}q_{\max}^{2} = φ ⁡ ( W n + 1 ) − Δ ​ w min ​ ‖ G ⁡ ( W n + 1 ) ‖ 2 − Δ ​ w min ​ ⟨ G ⁡ ( W n + 1 ) , F ⁡ ( W n + 1 ) ⟩ + L q 2 ​ Δ ​ w min 2 ​ q max 2 . \displaystyle=\varphi(W_{n+1})-\Delta w_{\min}\left\|G(W_{n+1})\right\|^{2}-\Delta w_{\min}\left\langle G(W_{n+1}),\,F(W_{n+1})\right\rangle+\frac{L_{q}}{2}\Delta w_{\min}^{2}q_{\max}^{2}. (34)

[219] p: Combining ( 33 ) and ( 34 ), we get:

[220] table: φ ⁡ ( W n + 2 ) \displaystyle\varphi(W_{n+2}) ≤ φ ⁡ ( W n ) − Δ ​ w min ​ ‖ G ⁡ ( W n ) ‖ 2 − Δ ​ w min ​ ‖ G ⁡ ( W n + 1 ) ‖ 2 \displaystyle\leq\varphi(W_{n})-\Delta w_{\min}\left\|G(W_{n})\right\|^{2}-\Delta w_{\min}\left\|G(W_{n+1})\right\|^{2} + Δ ​ w min ​ ( ⟨ G ⁡ ( W n ) , F ⁡ ( W n ) ⟩ − ⟨ G ⁡ ( W n + 1 ) , F ⁡ ( W n + 1 ) ⟩ ) + L q ​ Δ ​ w min 2 ​ q max 2 \displaystyle\quad+\Delta w_{\min}\Big(\left\langle G(W_{n}),\,F(W_{n})\right\rangle-\left\langle G(W_{n+1}),\,F(W_{n+1})\right\rangle\Big)+L_{q}\,\Delta w_{\min}^{2}q_{\max}^{2} ≤ φ ⁡ ( W n ) − Δ ​ w min ​ ‖ G ⁡ ( W n ) ‖ 2 − Δ ​ w min ​ ‖ G ⁡ ( W n + 1 ) ‖ 2 + 3 ​ Δ ​ w min 2 ​ q max 2 ​ L q . \displaystyle\leq\varphi(W_{n})-\Delta w_{\min}\|G(W_{n})\|^{2}-\Delta w_{\min}\|G(W_{n+1})\|^{2}+3\,\Delta w_{\min}^{2}\,q_{\max}^{2}\,L_{q}. (35)

[221] p: The second inequality holds for

[222] table: ⟨ G ⁡ ( W n ) , F ⁡ ( W n ) ⟩ − ⟨ G ⁡ ( W n + 1 ) , F ⁡ ( W n + 1 ) ⟩ \displaystyle\quad\left\langle G(W_{n}),\,F(W_{n})\right\rangle-\left\langle G(W_{n+1}),\,F(W_{n+1})\right\rangle = ⟨ G ⁡ ( W n ) , F ⁡ ( W n ) − F ⁡ ( W n + 1 ) ⟩ − ⟨ G ⁡ ( W n + 1 ) − G ⁡ ( W n ) , F ⁡ ( W n + 1 ) ⟩ \displaystyle=\left\langle G(W_{n}),\,F(W_{n})-F(W_{n+1})\right\rangle-\left\langle G(W_{n+1})-G(W_{n}),\,F(W_{n+1})\right\rangle ≤ ‖ G ⁡ ( W n ) ​ ‖ ‖ F ⁡ ( W n ) − F ⁡ ( W n + 1 ) ‖ + ‖ ​ G ​ ( W n + 1 ) − G ⁡ ( W n ) ‖ ​ ‖ F ⁡ ( W n + 1 ) ‖ \displaystyle\leq\|G(W_{n})\|\,\|F(W_{n})-F(W_{n+1})\|+\|G(W_{n+1})-G(W_{n})\|\,\|F(W_{n+1})\| ≤ 2 ​ q max ​ L q ​ ‖ W n + 1 − W n ‖ \displaystyle\leq 2q_{\max}L_{q}\,\|W_{n+1}-W_{n}\| ≤ 2 ​ q max ​ L q ​ Δ ​ w min ​ q max . \displaystyle\leq 2q_{\max}L_{q}\,\Delta w_{\min}\,q_{\max}. (36)

[223] p: By summing the recursion in Eq. ( 35 ) over the iterations, we obtain:

[224] table: φ ⁡ ( W 2 ​ N ) \displaystyle\varphi(W_{2N}) ≤ φ ⁡ ( W 0 ) − ∑ n = 0 2 ​ N − 1 Δ ​ w min ​ ‖ G ⁡ ( W n ) ‖ 2 + 3 ​ Δ ​ w min 2 ​ q max 2 ​ L q ​ N . \displaystyle\leq\varphi(W_{0})-\sum_{n=0}^{2N-1}\Delta w_{\min}\,\|G(W_{n})\|^{2}+3\,\Delta w_{\min}^{2}\,q_{\max}^{2}\,L_{q}N. (37)

[225] p: Taking average, we get:

[226] table: 1 2 ​ N ​ ∑ n = 0 2 ​ N − 1 ‖ G ⁡ ( W n ) ‖ 2 \displaystyle\frac{1}{2N}\sum_{n=0}^{2N-1}\|G(W_{n})\|^{2} ≤ φ ⁡ ( W 0 ) − φ ∗ 2 ​ N ​ Δ ​ w min + 3 ​ Δ ​ w min ​ q max 2 ​ L q 2 . \displaystyle\leq\frac{\varphi(W_{0})-\varphi^{\ast}}{2N\,\Delta w_{\min}}+\frac{3\,\Delta w_{\min}\,q_{\max}^{2}\,L_{q}}{2}. (38)

[227] p: ∎

[228] h4: C.4 Proof of Theorem C.4 : Last-iterate convergence of Algorithm 1 , cyclic version

[229] h6: Theorem C.4 (Last-iterate convergence of Algorithm 1 , cyclic version) .

[230] p: Considering the response functions satisfying Definition 2.1 and C.1 and assuming μ q < 1 3 ​ μ q ​ Δ ​ w min \mu_{q}<\frac{1}{3\mu_{q}\Delta w_{\min}} , then it holds that

[231] table: ( 1 − 2 ​ Δ ​ w min ​ μ q ) 2 ​ N ​ ‖ W 0 − W ⋄ ‖ 2 + Δ ​ w min ​ q max 2 ​ ( 4 + L q 2 μ q + 2 ​ μ q ) μ q . \displaystyle(1-2\Delta w_{\min}\mu_{q})^{2N}\,\|W_{0}-W^{\diamond}\|^{2}+\frac{\Delta w_{\min}q_{\max}^{2}\left(4+\frac{L_{q}^{2}}{\mu_{q}}+2\mu_{q}\right)}{\mu_{q}}.

[232] p: Moreover, the minimal achievable error ‖ W 2 ​ N − W ⋄ ‖ 2 ≤ δ \|W^{2N}-W^{\diamond}\|^{2}\leq\delta is δ = 𝒪 ⁡ ( Δ ​ w min ) \delta={\cal O}(\Delta w_{\min}) , and to achieve ‖ W 2 ​ N − W ⋄ ‖ 2 ≤ δ \|W^{2N}-W^{\diamond}\|^{2}\leq\delta with δ ≥ 𝒪 ⁡ ( Δ ​ w min ) \delta\geq{\cal O}(\Delta w_{\min}) , one need the number of pulses satisfying

[233] table: N ≥ 1 4 ​ μ q ​ Δ ​ w min ​ log ⁡ ( 2 ​ ‖ W 0 − W ⋄ ‖ 2 δ ) . \displaystyle N\geq\frac{1}{4\mu_{q}\Delta w_{\min}}\log\left(\frac{2\|W^{0}-W^{\diamond}\|^{2}}{\delta}\right).

[234] h6: Theorem C.4 .

[235] p: We begin the proof by one step descent form cyclic updating equation ( 31 )

[236] table: ‖ W n + 1 − W ⋄ ‖ 2 \displaystyle\|W_{n+1}-W^{\diamond}\|^{2} = ‖ W n − Δ ​ w min ​ F ​ ( W n ) − Δ ​ w min ​ G ​ ( W n ) − W ⋄ ‖ 2 \displaystyle=\|W_{n}-\Delta w_{\min}F(W_{n})-\Delta w_{\min}G(W_{n})-W^{\diamond}\|^{2} = ‖ W n − W ⋄ ‖ 2 − 2 ​ Δ ​ w min ​ ⟨ W n − W ⋄ , G ⁡ ( W n ) − G ⁡ ( W ⋄ ) ⟩ + Δ ​ w min 2 ​ ‖ F ⁡ ( W n ) + G ⁡ ( W n ) ‖ 2 \displaystyle=\|W_{n}-W^{\diamond}\|^{2}-2\Delta w_{\min}\langle W_{n}-W^{\diamond},\,G(W_{n})-G(W^{\diamond})\rangle+\Delta w_{\min}^{2}\,\|F(W_{n})+G(W_{n})\|^{2} − 2 ​ Δ ​ w min ​ ⟨ W n − W ⋄ , F ⁡ ( W n ) ⟩ \displaystyle\ -2\Delta w_{\min}\langle W_{n}-W^{\diamond},\,F(W_{n})\rangle ≤ ( 1 − 2 ​ Δ ​ w min ​ μ q ) ​ ‖ W n − W ⋄ ‖ 2 + 2 ​ Δ ​ w min 2 ​ q max 2 − 2 ​ Δ ​ w min ​ ⟨ W n − W ⋄ , F ⁡ ( W n ) ⟩ . \displaystyle\leq(1-2\Delta w_{\min}\mu_{q})\|W_{n}-W^{\diamond}\|^{2}+2\Delta w_{\min}^{2}q_{\max}^{2}-2\Delta w_{\min}\langle W_{n}-W^{\diamond},\,F(W_{n})\rangle. (39)

[237] p: The second equality holds for G w ​ ( W ⋄ ) = 0 G_{w}(W^{\diamond})=0 . The inequality holds for the strongly convex assumptions in definition C.1 and bounded response functions in definition 2.1 :

[238] table: ⟨ W n − W ⋄ , G ⁡ ( W n ) − G w ​ ( W ⋄ ) ⟩ ≥ μ q ​ ‖ W n − W ⋄ ‖ 2 , ‖ F ⁡ ( W n ) + G ⁡ ( W n ) ‖ 2 ≤ 2 ​ q max 2 . \left\langle W_{n}-W^{\diamond},\,G(W_{n})-G_{w}(W^{\diamond})\right\rangle\geq\mu_{q}\left\|W_{n}-W^{\diamond}\right\|^{2},\qquad\left\|F(W_{n})+G(W_{n})\right\|^{2}\leq 2q_{\max}^{2}.

[239] p: Similarly we have:

[240] table: ‖ W n + 2 − W ⋄ ‖ 2 \displaystyle\|W_{n+2}-W^{\diamond}\|^{2} = ‖ W n + 1 + Δ ​ w min ​ F ​ ( W n + 1 ) − Δ ​ w min ​ G ​ ( W n + 1 ) − W ⋄ ‖ 2 \displaystyle=\|W_{n+1}+\Delta w_{\min}F(W_{n+1})-\Delta w_{\min}G(W_{n+1})-W^{\diamond}\|^{2} ≤ ( 1 − 2 ​ Δ ​ w min ​ μ q ) ​ ‖ W n + 1 − W ⋄ ‖ 2 + 2 ​ Δ ​ w min 2 ​ q max 2 + 2 ​ Δ ​ w min ​ ⟨ W n + 1 − W ⋄ , F ⁡ ( W n + 1 ) ⟩ . \displaystyle\leq(1-2\Delta w_{\min}\mu_{q})\|W_{n+1}-W^{\diamond}\|^{2}+2\Delta w_{\min}^{2}q_{\max}^{2}+2\Delta w_{\min}\langle W_{n+1}-W^{\diamond},\,F(W_{n+1})\rangle. (40)

[241] p: The last term in ( 39 ) and ( 40 ) can be bounded by:

[242] table: 2 ​ Δ ​ w min ​ ⟨ W n − W ⋄ , F ⁡ ( W n + 1 ) ⟩ − 2 ​ Δ ​ w min ​ ⟨ W n − W ⋄ , F ⁡ ( W n ) ⟩ ​ ( 1 − 2 ​ Δ ​ w min ​ μ q ) \displaystyle\quad 2\Delta w_{\min}\langle W_{n}-W^{\diamond},\;F(W_{n+1})\rangle-\,2\Delta w_{\min}\langle W_{n}-W^{\diamond},\;F(W_{n})\rangle\,(1-2\Delta w_{\min}\mu_{q}) ≤ 2 ​ Δ ​ w min ​ ⟨ W n − W ⋄ , F ⁡ ( W n + 1 ) − F ⁡ ( W n ) ⟩ + 4 ​ Δ ​ w min 2 ​ μ q ​ ‖ W n − W ⋄ ‖ ​ ‖ F ⁡ ( W n ) ‖ \displaystyle\leq 2\Delta w_{\min}\langle W_{n}-W^{\diamond},\;F(W_{n+1})-F(W_{n})\rangle+4\Delta w_{\min}^{2}\mu_{q}\|W_{n}-W^{\diamond}\|\,\|F(W_{n})\| ≤ Δ ​ w min 2 ​ μ q ​ ‖ W n − W ⋄ ‖ 2 + ‖ F ⁡ ( W n + 1 ) − F ⁡ ( W n ) ‖ 2 μ q + 4 ​ Δ ​ w min 2 ​ μ q ​ ‖ W n − W ⋄ ‖ ​ q max \displaystyle\leq\Delta w_{\min}^{2}\mu_{q}\|W_{n}-W^{\diamond}\|^{2}+\frac{\|F(W_{n+1})-F(W_{n})\|^{2}}{\mu_{q}}+4\Delta w_{\min}^{2}\mu_{q}\|W_{n}-W^{\diamond}\|\,q_{\max} ≤ Δ ​ w min 2 ​ μ q ​ ‖ W n − W ⋄ ‖ 2 + L q 2 ​ Δ ​ w min 2 ​ q max 2 μ q + 2 ​ Δ ​ w min 2 ​ μ q ​ ‖ W n − W ⋄ ‖ 2 + 2 ​ Δ ​ w min 2 ​ μ q ​ q max 2 \displaystyle\leq\Delta w_{\min}^{2}\mu_{q}\|W_{n}-W^{\diamond}\|^{2}+\frac{L_{q}^{2}\Delta w_{\min}^{2}q_{\max}^{2}}{\mu_{q}}+2\Delta w_{\min}^{2}\mu_{q}\|W_{n}-W^{\diamond}\|^{2}+2\Delta w_{\min}^{2}\mu_{q}q_{\max}^{2} ≤ 3 ​ Δ ​ w min 2 ​ μ q ​ ‖ W n − W ⋄ ‖ 2 + L q 2 ​ Δ ​ w min 2 ​ q max 2 μ q + 2 ​ Δ ​ w min 2 ​ μ q ​ q max 2 \displaystyle\leq 3\Delta w_{\min}^{2}\mu_{q}\|W_{n}-W^{\diamond}\|^{2}+\frac{L_{q}^{2}\Delta w_{\min}^{2}q_{\max}^{2}}{\mu_{q}}+2\Delta w_{\min}^{2}\mu_{q}q_{\max}^{2} ≤ Δ ​ w min ​ μ q ​ ‖ W n − W ⋄ ‖ 2 + L q 2 ​ Δ ​ w min 2 ​ q max 2 μ q + 2 ​ Δ ​ w min 2 ​ μ q ​ q max 2 . \displaystyle\leq\Delta w_{\min}\mu_{q}\|W_{n}-W^{\diamond}\|^{2}+\frac{L_{q}^{2}\Delta w_{\min}^{2}q_{\max}^{2}}{\mu_{q}}+2\Delta w_{\min}^{2}\mu_{q}q_{\max}^{2}. (41)

[243] p: The first inequality follows by expanding the term and applying Cauchy–Schwarz. The second and fourth inequalities use Young’s inequality together with the bound | F ⁡ ( W n ) | ≤ q max |F(W_{n})|\leq q_{\max} . The last step holds under the step-size condition 3 ​ Δ ​ w min 2 ​ μ q ≤ Δ ​ w min ​ μ q 3\Delta w_{\min}^{2}\mu_{q}\leq\Delta w_{\min}\mu_{q} . Combining ( 39 ) and ( 40 ) and substituting ( 41 ), we get:

[244] table: ‖ W n + 2 − W ⋄ ‖ 2 \displaystyle\|W_{n+2}-W^{\diamond}\|^{2} ≤ ( 1 − 2 ​ Δ ​ w min ​ μ q ) 2 ​ ‖ W n − W ⋄ ‖ 2 + 4 ​ Δ ​ w min 2 ​ q max 2 + L q 2 ​ Δ ​ w min 2 ​ q max 2 μ q \displaystyle\leq(1-2\Delta w_{\min}\mu_{q})^{2}\,\|W_{n}-W^{\diamond}\|^{2}+4\Delta w_{\min}^{2}q_{\max}^{2}+\frac{L_{q}^{2}\Delta w_{\min}^{2}q_{\max}^{2}}{\mu_{q}} + Δ ​ w min ​ μ q ​ ‖ W n − W ⋄ ‖ 2 + 2 ​ Δ ​ w min 2 ​ μ q ​ q max 2 \displaystyle\ +\Delta w_{\min}\mu_{q}\,\|W_{n}-W^{\diamond}\|^{2}+2\Delta w_{\min}^{2}\mu_{q}q_{\max}^{2} ≤ ( 1 − Δ ​ w min ​ μ q ) 2 ​ ‖ W n − W ⋄ ‖ 2 + Δ ​ w min 2 ​ q max 2 ​ ( 4 + L q 2 μ q + 2 ​ μ q ) . \displaystyle\leq(1-\Delta w_{\min}\mu_{q})^{2}\,\|W_{n}-W^{\diamond}\|^{2}+\Delta w_{\min}^{2}q_{\max}^{2}\left(4+\frac{L_{q}^{2}}{\mu_{q}}+2\mu_{q}\right). (42)

[245] p: Iterating the recursion for n = 0 , … , 2 ​ N − 1 n=0,\ldots,2N-1 gives:

[246] table: ‖ W 2 ​ N − W ⋄ ‖ 2 \displaystyle\|W_{2N}-W^{\diamond}\|^{2} ≤ ( 1 − 2 ​ Δ ​ w min ​ μ q ) 2 ​ N ​ ‖ W 0 − W ⋄ ‖ 2 + ∑ n = 0 2 ​ N − 1 ( 1 − 2 ​ Δ ​ w min ​ μ q ) n ​ Δ ​ w min 2 ​ q max 2 ​ ( 4 + L q 2 μ q + 2 ​ μ q ) \displaystyle\leq(1-2\Delta w_{\min}\mu_{q})^{2N}\,\|W_{0}-W^{\diamond}\|^{2}+\sum_{n=0}^{2N-1}(1-2\Delta w_{\min}\mu_{q})^{n}\Delta w_{\min}^{2}q_{\max}^{2}\left(4+\frac{L_{q}^{2}}{\mu_{q}}+2\mu_{q}\right) ≤ ( 1 − 2 ​ Δ ​ w min ​ μ q ) 2 ​ N ​ ‖ W 0 − W ⋄ ‖ 2 + Δ ​ w min ​ q max 2 ​ ( 4 + L q 2 μ q + 2 ​ μ q ) μ q . \displaystyle\leq(1-2\Delta w_{\min}\mu_{q})^{2N}\,\|W_{0}-W^{\diamond}\|^{2}+\frac{\Delta w_{\min}q_{\max}^{2}\left(4+\frac{L_{q}^{2}}{\mu_{q}}+2\mu_{q}\right)}{\mu_{q}}. (43)

[247] p: To ensure the total error remains within the tolerance δ \delta , we bound each term in the upper bound by δ / 2 \delta/2 . This yields the following two sufficient conditions:

[248] table: Δ ​ w min ​ q max 2 ​ ( 4 + L q 2 μ q + 2 ​ μ q ) μ q ≤ δ 2 and ( 1 − 2 ​ μ q ​ Δ ​ w min ) 2 ​ N ​ ‖ W 0 − W ⋄ ‖ 2 ≤ δ 2 . \displaystyle\frac{\Delta w_{\min}q_{\max}^{2}\left(4+\frac{L_{q}^{2}}{\mu_{q}}+2\mu_{q}\right)}{\mu_{q}}\leq\frac{\delta}{2}\quad\text{and}\quad(1-2\mu_{q}\Delta w_{\min})^{2N}\|W_{0}-W^{\diamond}\|^{2}\leq\frac{\delta}{2}. (44)

[249] p: The first condition implies a lower bound on the achievable tolerance, requiring δ ≥ 2 ​ q max 2 ​ ( 4 + L q 2 / μ q + 2 ​ μ q ) ​ Δ ​ w min μ q \delta\geq\frac{2q_{\max}^{2}\left(4+L_{q}^{2}/\mu_{q}+2\mu_{q}\right)\Delta w_{\min}}{\mu_{q}} . For the second condition, rearranging terms and taking the logarithm yields

[250] table: log ⁡ ( 2 ​ ‖ W 0 − W ⋄ ‖ 2 δ ) ≤ 2 ​ N ​ log ⁡ ( 1 1 − 2 ​ μ q ​ Δ ​ w min ) . \displaystyle\log\left(\frac{2\|W_{0}-W^{\diamond}\|^{2}}{\delta}\right)\leq 2N\log\left(\frac{1}{1-2\mu_{q}\Delta w_{\min}}\right). (45)

[251] p: Applying the inequality log ⁡ ( 1 / x ) ≥ 1 − x \log(1/x)\geq 1-x (valid for x ∈ ( 0 , 1 ] x\in(0,1] ) with x = 1 − 2 ​ μ q ​ Δ ​ w min x=1-2\mu_{q}\Delta w_{\min} , we observe that the right-hand side is lower-bounded by 2 ​ N ​ ( 2 ​ μ q ​ Δ ​ w min ) = 4 ​ N ​ μ q ​ Δ ​ w min 2N(2\mu_{q}\Delta w_{\min})=4N\mu_{q}\Delta w_{\min} . Therefore, to satisfy the inequality, it suffices to set

[252] table: N ≥ 1 4 ​ μ q ​ Δ ​ w min ​ log ⁡ ( 2 ​ ‖ W 0 − W ⋄ ‖ 2 δ ) , \displaystyle N\geq\frac{1}{4\mu_{q}\Delta w_{\min}}\log\left(\frac{2\|W_{0}-W^{\diamond}\|^{2}}{\delta}\right), (46)

[253] p: which completes the proof. ∎

[254] h3: Appendix D Proof of Auxiliary Lemmas

[255] h4: D.1 Proof of Lemma 3.5

[256] h6: Proof.

[257] p: According to the update of Q k Q_{k} in ( 12 ), we know

[258] table: Q k + 1 − W ⋄ = ( 1 − η ) ​ ( Q k − W ⋄ ) + η ⁡ ( P k + 1 − W ⋄ ) . \displaystyle Q_{k+1}-W^{\diamond}=(1-\eta)(Q_{k}-W^{\diamond})+\eta(P_{k+1}-W^{\diamond}).

[259] p: Taking square norm of both sides yield

[260] table: ‖ Q k + 1 − W ⋄ ‖ 2 \displaystyle\|Q_{k+1}-W^{\diamond}\|^{2} = ( 1 − η ) 2 ​ ‖ Q k − W ⋄ ‖ 2 + η 2 ​ ‖ P k + 1 − W ⋄ ‖ 2 + 2 ​ η ​ ( 1 − η ) ​ ⟨ P k + 1 − W ⋄ , Q k − W ⋄ ⟩ \displaystyle=(1-\eta)^{2}\|Q_{k}-W^{\diamond}\|^{2}+\eta^{2}\|P_{k+1}-W^{\diamond}\|^{2}+2\eta(1-\eta)\langle P_{k+1}-W^{\diamond},Q_{k}-W^{\diamond}\rangle = ( 1 − η ) 2 ​ ‖ Q k − W ⋄ ‖ 2 + η 2 ​ ‖ P k + 1 − W ⋄ ‖ 2 \displaystyle=(1-\eta)^{2}\|Q_{k}-W^{\diamond}\|^{2}+\eta^{2}\|P_{k+1}-W^{\diamond}\|^{2} + η ⁡ ( 1 − η ) ​ ‖ P k + 1 − W ⋄ ‖ 2 + η ⁡ ( 1 − η ) ​ ‖ Q k − W ⋄ ‖ 2 − η ⁡ ( 1 − η ) ​ ‖ P k + 1 − Q k ‖ 2 \displaystyle~~~~~+\eta(1-\eta)\|P_{k+1}-W^{\diamond}\|^{2}+\eta(1-\eta)\|Q_{k}-W^{\diamond}\|^{2}-\eta(1-\eta)\|P_{k+1}-Q_{k}\|^{2} = ( 1 − η ) ​ ‖ Q k − W ⋄ ‖ 2 + η ​ ‖ P k + 1 − W ⋄ ‖ 2 − η ⁡ ( 1 − η ) ​ ‖ P k + 1 − Q k ‖ 2 \displaystyle=(1-\eta)\|Q_{k}-W^{\diamond}\|^{2}+\eta\|P_{k+1}-W^{\diamond}\|^{2}-\eta(1-\eta)\|P_{k+1}-Q_{k}\|^{2} (47)

[261] p: where the second equation is because ⟨ A , B ⟩ = 1 2 ​ ‖ A ‖ 2 + 1 2 ​ ‖ B ‖ 2 − 1 2 ​ ‖ A − B ‖ 2 \langle A,B\rangle=\frac{1}{2}\|A\|^{2}+\frac{1}{2}\|B\|^{2}-\frac{1}{2}\|A-B\|^{2} . On the other hand, letting cos ⁡ ( P k + 1 − W ⋄ , P k + 1 − Q k ) := cos ⁡ θ \cos(P_{k+1}-W^{\diamond},P_{k+1}-Q_{k}):=\cos\theta , we have

[262] table: ‖ Q k − W ⋄ ‖ 2 = ‖ P k + 1 − W ⋄ ‖ 2 + ‖ P k + 1 − Q k ‖ 2 − 2 ​ ‖ P k + 1 − W ⋄ ‖ ​ ‖ P k + 1 − Q k ‖ ​ cos ⁡ θ . \displaystyle\|Q_{k}-W^{\diamond}\|^{2}=\|P_{k+1}-W^{\diamond}\|^{2}+\|P_{k+1}-Q_{k}\|^{2}-2\|P_{k+1}-W^{\diamond}\|\|P_{k+1}-Q_{k}\|\cos\theta. (48)

[263] p: Plugging ( 48 ) into ( 47 ), we get

[264] table: ‖ Q k + 1 − W ⋄ ‖ 2 \displaystyle\|Q_{k+1}-W^{\diamond}\|^{2} = ‖ P k + 1 − W ⋄ ‖ 2 + ( 1 − η ) 2 ​ ‖ P k + 1 − Q k ‖ 2 − 2 ​ ( 1 − η ) ​ ‖ P k + 1 − W ⋄ ‖ ​ ‖ P k + 1 − Q k ‖ ​ cos ⁡ θ \displaystyle=\|P_{k+1}-W^{\diamond}\|^{2}+(1-\eta)^{2}\|P_{k+1}-Q_{k}\|^{2}-2(1-\eta)\|P_{k+1}-W^{\diamond}\|\|P_{k+1}-Q_{k}\|\cos\theta

[265] p: Since cos ⁡ θ > 0 \cos\theta>0 implies ‖ P k + 1 − Q k ‖ ≠ 0 \|P_{k+1}-Q_{k}\|\neq 0 , then choosing 1 > η > max ⁡ { 1 − 2 ​ ‖ P k + 1 − W ⋄ ‖ ​ cos ⁡ θ ‖ P k + 1 − Q k ‖ , 0 } 1>\eta>\max\left\{1-\frac{2\|P_{k+1}-W^{\diamond}\|\cos\theta}{\|P_{k+1}-Q_{k}\|},0\right\} yields

[266] table: ‖ Q k + 1 − W ⋄ ‖ 2 \displaystyle\|Q_{k+1}-W^{\diamond}\|^{2} < ‖ P k + 1 − W ⋄ ‖ 2 . \displaystyle<\|P_{k+1}-W^{\diamond}\|^{2}.

[267] p: ∎

[268] h4: D.2 Proof of Lemma 3.10

[269] h6: Proof.

[270] p: From the digital signal processing perspective, the moving average update ( 12 ) defines a stable first-order infinite impulse response (IIS) low-pass filter from P k P_{k} to Q k Q_{k} . Taking the z z -transform of ( 12 ) yields

[271] table: Q ⁡ ( z ) = ( 1 − η ) ​ z − 1 ​ Q ​ ( z ) + η ​ P ​ ( z ) , \displaystyle Q(z)=(1-\eta)z^{-1}Q(z)+\eta P(z),

[272] p: which gives the filter’s transfer function

[273] table: H ⁡ ( z ) ≜ Q ⁡ ( z ) P ⁡ ( z ) = η 1 − ( 1 − η ) ​ z − 1 . H(z)\triangleq\frac{Q(z)}{P(z)}=\frac{\eta}{1-(1-\eta)z^{-1}}. (49)

[274] p: The transfer function has a single pole at z = 1 − η z=1-\eta with the following magnitude of the frequency response

[275] table: | H ⁡ ( e j ​ ω ) | 2 = η 2 1 + ( 1 − η ) 2 − 2 ​ ( 1 − η ) ​ cos ⁡ ω . \displaystyle|H(e^{j\omega})|^{2}=\frac{\eta^{2}}{1+(1-\eta)^{2}-2(1-\eta)\cos\omega}. (50)

[276] p: ∎

[277] h3: Appendix E Proof of Theorem 3.7 : Convergence of Algorithm 2

[278] p: This section provides the convergence analysis details of the Algorithm 2 under the strongly convexity condition. See 3.7

[279] h4: E.1 Main proof

[280] h6: Theorem 3.7 .

[281] p: Define the following notations M w ​ ( W k ) := Q + ​ ( W k ) ⊙ Q − ​ ( W k ) ∈ ℝ D M_{w}(W_{k}):=Q_{+}(W_{k})\odot Q_{-}(W_{k})\in{\mathbb{R}}^{D} , M p ​ ( P k ) := Q + ​ ( P k ) ⊙ Q − ​ ( P k ) ∈ ℝ D M_{p}(P_{k}):=Q_{+}(P_{k})\odot Q_{-}(P_{k})\in{\mathbb{R}}^{D} . The proof of the RIDER convergence relies on the following two lemmas, which provide the sufficient descent of W k W_{k} and W ¯ k \bar{W}_{k} , respectively.

[282] h6: Lemma E.1 (Descent lemma of lower-level problem) .

[283] p: Under Assumptions 3.1 - 3.2 , it holds that

[284] table: ? ​ ? ​ ? \displaystyle??? (51)

[285] p: Keeping W k W_{k} fixed, we also have

[286] table: ? ​ ? ​ ? \displaystyle??? (52)

[287] p: Recall that we use the square norm of P ∗ ​ ( W , Q ) − Q = ( W ∗ − W ) / γ P^{*}(W,Q)-Q=(W^{*}-W)/\gamma to measure the convergence of the upper-level problem.

[288] h6: Lemma E.2 (Descent lemma of upper-level problem) .

[289] p: Under Assumption 2.1 , it holds that

[290] table: ? ​ ? ​ ? . \displaystyle???. (53)

[291] h6: Lemma E.3 (Descent lemma of accumulated asymmetric sequence) .

[292] p: Under Assumption 2.1 and 3.6 , it holds that

[293] table: ? ​ ? ​ ? \displaystyle??? (54)

[294] p: The proof of Lemma E.1 , E.2 and E.3 are deferred to Appendices E.2 , E.3 and E.4 respectively. For the response functions that satisfy Definition 2.1 , we have

[295] table: min ⁡ { [ M w ​ ( W k ) ] d : d ∈ [ D ] } ≥ q min 2 > 0 , and min ⁡ { [ M p ​ ( P k ) ] d : d ∈ [ D ] } ≥ q min 2 > 0 . \displaystyle\min\{[M_{w}(W_{k})]_{d}:d\in[D]\}\geq q_{\min}^{2}>0,\quad\text{and}\quad\min\{[M_{p}(P_{k})]_{d}:d\in[D]\}\geq q_{\min}^{2}>0. (55)

[296] p: Now we deal with the weighted norm in two lemmas by Lemma A.1

[297] table: β 2 ​ γ ​ q max ​ ‖ P ∗ ​ ( W k , Q k ) ‖ M p ​ ( P k ) 2 ≥ \displaystyle\frac{\beta}{2\gamma q_{\max}}\|P^{*}(W_{k},Q_{k})\|^{2}_{M_{p}(P_{k})}\geq β ​ q min 2 2 ​ γ ​ q max ​ ‖ P ∗ ​ ( W k , Q k ) ‖ 2 \displaystyle\ \frac{\beta q_{\min}^{2}}{2\gamma q_{\max}}\|P^{*}(W_{k},Q_{k})\|^{2} (56) α 4 ​ q max ​ ‖ ∇ f ​ ( W ¯ k ) ‖ M p ​ ( P k ) 2 ≥ \displaystyle\frac{\alpha}{4q_{\max}}\|\nabla f(\bar{W}_{k})\|^{2}_{M_{p}(P_{k})}\geq α ​ q min 2 4 ​ q max ​ ‖ ∇ f ​ ( W ¯ k ) ‖ 2 \displaystyle\ \frac{\alpha q_{\min}^{2}}{4q_{\max}}\|\nabla f(\bar{W}_{k})\|^{2} (57) q max α ​ ‖ W k + 1 − W k ‖ M p ​ ( P k ) † 2 ≤ \displaystyle\frac{q_{\max}}{\alpha}\|W_{k+1}-W_{k}\|^{2}_{M_{p}(P_{k})^{\dagger}}\leq q max α ​ q min 2 ​ ‖ W k + 1 − W k ‖ 2 \displaystyle\ \frac{q_{\max}}{\alpha q_{\min}^{2}}\|W_{k+1}-W_{k}\|^{2} (58) 2 ​ β ​ q max 3 γ ​ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ M w ​ ( W k ) † 2 ≤ \displaystyle\frac{2\beta q_{\max}^{3}}{\gamma}\left\|P_{k+1}-P^{*}(W_{k},Q_{k})\right\|^{2}_{M_{w}(W_{k})^{\dagger}}\leq 2 ​ β ​ q max 3 γ ​ q min 2 ​ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 \displaystyle\ \frac{2\beta q_{\max}^{3}}{\gamma q_{\min}^{2}}\left\|P_{k+1}-P^{*}(W_{k},Q_{k})\right\|^{2} (59) 2 ​ q max ​ γ 2 α ​ ‖ Q k + 1 − Q k ‖ M p ​ ( P k ) † 2 ≤ \displaystyle\frac{2q_{\max}\gamma^{2}}{\alpha}\left\|Q_{k+1}-Q_{k}\right\|^{2}_{M_{p}(P_{k})^{\dagger}}\leq 2 ​ q max ​ γ 2 α ​ q min 2 ​ ‖ Q k + 1 − Q k ‖ 2 . \displaystyle\ \frac{2q_{\max}\gamma^{2}}{\alpha q_{\min}^{2}}\left\|Q_{k+1}-Q_{k}\right\|^{2}. (60)

[298] p: By inequality ( 58 ), the last two terms in the RHS ( RHS ) of ( 51 ) is bounded by

[299] table: q max α ​ γ ​ 𝔼 b k ′ ​ [ ‖ W k + 1 − W k ‖ M p ​ ( P k ) † 2 ] + 3 ​ L 2 ​ 𝔼 b k ′ ​ [ ‖ W k + 1 − W k ‖ 2 ] \displaystyle\ \frac{q_{\max}}{\alpha\gamma}\mathbb{E}_{b_{k}^{\prime}}\left[\|W_{k+1}-W_{k}\|^{2}_{M_{p}(P_{k})^{\dagger}}\right]+\frac{3L}{2}\mathbb{E}_{b_{k}^{\prime}}\left[\|W_{k+1}-W_{k}\|^{2}\right] (61) ≤ \displaystyle\leq q max α ​ q min 2 ​ γ ​ 𝔼 b k ′ ​ [ ‖ W k + 1 − W k ‖ 2 ] + 3 ​ L 2 ​ 𝔼 b k ′ ​ [ ‖ W k + 1 − W k ‖ 2 ] \displaystyle\ \frac{q_{\max}}{\alpha q_{\min}^{2}\gamma}\mathbb{E}_{b_{k}^{\prime}}\left[\|W_{k+1}-W_{k}\|^{2}\right]+\frac{3L}{2}\mathbb{E}_{b_{k}^{\prime}}\left[\|W_{k+1}-W_{k}\|^{2}\right] ≤ ( a ) \displaystyle\overset{(a)}{\leq} 2 ​ q max α ​ q min 2 ​ γ ​ 𝔼 b k ′ ​ [ ‖ W k + 1 − W k ‖ 2 ] ≤ 2 ​ β 2 ​ q max α ​ q min 2 ​ γ ​ ‖ ( P k + 1 − Q k ) ⊙ F w ​ ( W k ) − | P k + 1 − Q k | ⊙ G w ​ ( W k ) ‖ 2 + Θ ⁡ ( β ​ q max ​ Δ ​ w min α ​ q min 2 ​ γ ) \displaystyle\ \frac{2q_{\max}}{\alpha q_{\min}^{2}\gamma}\mathbb{E}_{b_{k}^{\prime}}\left[\|W_{k+1}-W_{k}\|^{2}\right]\leq\frac{2\beta^{2}q_{\max}}{\alpha q_{\min}^{2}\gamma}\|(P_{k+1}-Q_{k})\odot F_{w}(W_{k})-|P_{k+1}-Q_{k}|\odot G_{w}(W_{k})\|^{2}+{\Theta}\left(\frac{\beta q_{\max}\Delta w_{\min}}{\alpha q_{\min}^{2}\gamma}\right) ≤ \displaystyle\leq 4 ​ β 2 ​ q max α ​ q min 2 ​ γ ​ ‖ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) − | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) ‖ 2 + Θ ⁡ ( β ​ q max ​ Δ ​ w min α ​ q min 2 ​ γ ) \displaystyle\ \frac{4\beta^{2}q_{\max}}{\alpha q_{\min}^{2}\gamma}\|(P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})\|^{2}+{\Theta}\left(\frac{\beta q_{\max}\Delta w_{\min}}{\alpha q_{\min}^{2}\gamma}\right) ≤ ( b ) + 4 ​ β 2 ​ q max α ​ q min 2 ​ γ | ( P k + 1 − Q k ) ⊙ F w ​ ( W k ) − | P k + 1 − Q k | ⊙ G w ​ ( W k ) \displaystyle\overset{(b)}{\leq}\ +\frac{4\beta^{2}q_{\max}}{\alpha q_{\min}^{2}\gamma}\|(P_{k+1}-Q_{k})\odot F_{w}(W_{k})-|P_{k+1}-Q_{k}|\odot G_{w}(W_{k}) − ( ( P ∗ ( W k , Q k ) − Q k ) ⊙ F w ( W k ) − | P ∗ ( W k , Q k ) − Q k | ⊙ G w ( W k ) ) ∥ 2 + Θ ( γ ​ Δ ​ w min q max 2 ) \displaystyle\ \quad-((P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k}))\|^{2}+{\Theta}\left(\frac{\gamma\Delta w_{\min}}{q_{\max}^{2}}\right) ≤ ( c ) \displaystyle\overset{(c)}{\leq} 4 ​ β 2 ​ q max α ​ q min 2 ​ γ ​ ‖ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) − | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) ‖ 2 + 4 ​ β 2 ​ q max 3 α ​ q min 2 ​ γ ​ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 \displaystyle\ \frac{4\beta^{2}q_{\max}}{\alpha q_{\min}^{2}\gamma}\|(P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})\|^{2}+\frac{4\beta^{2}q_{\max}^{3}}{\alpha q_{\min}^{2}\gamma}\|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2} + Θ ⁡ ( γ ​ Δ ​ w min q min ) \displaystyle~~~~+{\Theta}\left(\frac{\gamma\Delta w_{\min}}{q_{\min}}\right)

[300] p: where ( a ) (a) holds if the learning rate α \alpha is sufficiently small such that α ≤ 2 ​ q max 3 ​ q min ​ γ ​ L \alpha\leq\frac{2q_{\max}}{3q_{\min}\gamma L} ; ( b ) (b) is because and β ≤ γ 2 ​ q max , α ≤ q max q min 2 ​ γ ​ L \beta\leq\frac{\gamma}{2q_{\max}},\alpha\leq\frac{q_{\max}}{q_{\min}^{2}\gamma L} ; and ( c ) (c) comes from the fact that the analog update is Lipschitz continuous (see Lemma A.2 ).

[301] p: By inequality ( 60 ), the two terms related to ‖ Q k + 1 − Q k ‖ 2 \left\|Q_{k+1}-Q_{k}\right\|^{2} in the RHS of ( 51 ) is bounded by

[302] table: 2 ​ q max ​ γ α ​ 𝔼 ξ k ​ [ ‖ Q k + 1 − Q k ‖ M p ​ ( P k ) † 2 ] + L ​ γ 2 ​ 𝔼 ξ k ​ [ ‖ Q k + 1 − Q k ‖ 2 ] ≤ \displaystyle\frac{2q_{\max}\gamma}{\alpha}\mathbb{E}_{\xi_{k}}\left[\|Q_{k+1}-Q_{k}\|^{2}_{M_{p}(P_{k})^{\dagger}}\right]+L\gamma^{2}\mathbb{E}_{\xi_{k}}\left[\|Q_{k+1}-Q_{k}\|^{2}\right]\leq 3 ​ q max ​ γ α ​ q min 2 ​ 𝔼 ξ k ​ [ ‖ Q k + 1 − Q k ‖ 2 ] . \displaystyle\frac{3q_{\max}\gamma}{\alpha q_{\min}^{2}}\mathbb{E}_{\xi_{k}}\left[\|Q_{k+1}-Q_{k}\|^{2}\right]. (62)

[303] p: where the last inequality holds when choosing stepsize α ≤ q max q min 2 ​ γ ​ L \alpha\leq\frac{q_{\max}}{q_{\min}^{2}\gamma L} .

[304] p: With all the inequalities and lemmas above, we are ready to prove the main conclusion in Theorem 3.7 now. Define a Lyapunov function by

[305] table: V k := \displaystyle V_{k}:= f ⁡ ( W ¯ k ) − f ∗ + C 1 ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 + C 2 ​ ( φ ⁡ ( P k ) − φ ∗ ) . \displaystyle\ f(\bar{W}_{k})-f^{*}+C_{1}\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}+C_{2}(\varphi(P_{k})-\varphi^{*}). (63)

[306] p: By Lemmas E.1 and E.2 , we show that V k V_{k} has sufficient descent in expectation

[307] table: 𝔼 ξ k , b k , b k ′ ] [ V k + 1 ] = 𝔼 ξ k , b k , b k ′ [ f ( W ¯ k + 1 ) − f ∗ + C 1 ∥ P ∗ ( W k + 1 , Q k + 1 ) − Q k + 1 ∥ 2 + C 2 ( φ ( P k + 1 ) − φ ∗ ) ] \displaystyle\ {\mathbb{E}}_{\xi_{k},b_{k},b_{k}^{\prime}]}[V_{k+1}]={\mathbb{E}}_{\xi_{k},b_{k},b_{k}^{\prime}}\left[f(\bar{W}_{k+1})-f^{*}+C_{1}\|P^{*}(W_{k+1},Q_{k+1})-Q_{k+1}\|^{2}+C_{2}(\varphi(P_{k+1})-\varphi^{*})\right] (64) ≤ \displaystyle\leq f ⁡ ( W ¯ k ) − f ∗ − α ​ γ 8 ​ q max ​ ‖ ∇ f ​ ( W ¯ k ) ‖ M p ​ ( P k ) 2 + α ​ σ 2 ​ γ 2 ​ ‖ G p ​ ( P k ) F p ​ ( P k ) ‖ ∞ 2 + 3 ​ α 2 ​ L ​ q max 2 ​ σ 2 + Θ ⁡ ( γ ​ Δ ​ w min q min ) \displaystyle\ f(\bar{W}_{k})-f^{*}-\frac{\alpha\gamma}{8q_{\max}}\|\nabla f(\bar{W}_{k})\|^{2}_{M_{p}(P_{k})}+\frac{\alpha\sigma^{2}\gamma}{2}\left\|\frac{G_{p}(P_{k})}{\sqrt{F_{p}(P_{k})}}\right\|^{2}_{\infty}+3\alpha^{2}Lq_{\max}^{2}\sigma^{2}+{\Theta}\left(\frac{\gamma\Delta w_{\min}}{q_{\min}}\right) + 6 ​ q max ​ γ 2 ​ η 2 α ​ q min 2 ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 + ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 ] + 4 ​ β 2 ​ q max 3 α ​ q min 2 ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 ] \displaystyle\ +\frac{6q_{\max}\gamma^{2}\eta^{2}}{\alpha q_{\min}^{2}}\mathbb{E}_{\xi_{k},b_{k}}\left[\|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2}+\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}\right]+\frac{4\beta^{2}q_{\max}^{3}}{\alpha q_{\min}^{2}}{\mathbb{E}}_{\xi_{k},b_{k}}[\|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2}] − ( 1 2 ​ α ​ q max − 3 ​ γ 2 ​ L ) ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k + α ⁡ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) − b k ‖ 2 ] \displaystyle\ -\left(\frac{1}{2\alpha q_{\max}}-3\gamma^{2}L\right)~\mathbb{E}_{\xi_{k},b_{k}}\left[\left\|P_{k+1}-P_{k}+\alpha(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot F_{p}(P_{k})-b_{k}\right\|^{2}\right] + 4 ​ β 2 ​ q max α ​ q min 2 ​ ‖ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) − | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) ‖ 2 \displaystyle\ +\frac{4\beta^{2}q_{\max}}{\alpha q_{\min}^{2}}\|(P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})\|^{2} + C 1 ​ ( ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 − β 2 ​ γ ​ q max ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ M w ​ ( W k ) 2 + 3 ​ β ​ q max 3 γ ​ q min 2 ​ 𝔼 ξ k ​ [ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 ] CLOSE \displaystyle\ +C_{1}\Bigg(~\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}-\frac{\beta}{2\gamma q_{\max}}\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}_{M_{w}(W_{k})}+\frac{3\beta q_{\max}^{3}}{\gamma q_{\min}^{2}}{\mathbb{E}}_{\xi_{k}}[\|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2}] OPEN − β 2 ​ γ ​ q max ​ ‖ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) − | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) ‖ 2 + Θ ⁡ ( Δ ​ w min γ ​ q max ) ) \displaystyle\ \hskip 30.00005pt-\frac{\beta}{2\gamma q_{\max}}\|(P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})\|^{2}+{\Theta}\left(\frac{\Delta w_{\min}}{\gamma q_{\max}}\right)~\Bigg) + C 2 ​ ( φ ⁡ ( P k ) − φ ∗ − α ​ C ⋆ 2 ​ ‖ G p ​ ( P k ) ‖ 2 + α 2 ​ L ​ q max 2 ​ σ 2 + α ​ q max 2 2 ​ C ⋆ ​ ‖ ∇ f ​ ( W ¯ k ) ‖ 2 CLOSE \displaystyle\ +C_{2}\Bigg(~\varphi(P_{k})-\varphi^{*}-\frac{\alpha C_{\star}}{2}\|G_{p}(P_{k})\|^{2}+\alpha^{2}Lq_{\max}^{2}\sigma^{2}+\frac{\alpha q_{\max}^{2}}{2C_{\star}}\|\nabla f(\bar{W}_{k})\|^{2} OPEN + L ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k + α ⁡ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) − b k ‖ 2 ] + Θ ⁡ ( Δ ​ w min γ ​ q max ) ) \displaystyle\ \quad+L\mathbb{E}_{\xi_{k},b_{k}}\left[\left\|P_{k+1}-P_{k}+\alpha(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot F_{p}(P_{k})-b_{k}\right\|^{2}\right]+{\Theta}\left(\frac{\Delta w_{\min}}{\gamma q_{\max}}\right)~\Bigg) ≤ \displaystyle\leq V k − ( α ​ q min 2 8 ​ q max − C 2 ​ α ​ q max 2 2 ​ C ⋆ ) ​ ‖ ∇ f ​ ( W ¯ k ) ‖ 2 − ( α ​ C 2 ​ C ⋆ 2 − α ​ σ 2 2 ​ q min ) ​ ‖ G p ​ ( P k ) ‖ 2 + Θ ⁡ ( ( C 1 + C 2 ) ​ Δ ​ w min γ ​ q max + γ ​ Δ ​ w min q min ) \displaystyle\ V_{k}-\left(\frac{\alpha q_{\min}^{2}}{8q_{\max}}-\frac{C_{2}\alpha q_{\max}^{2}}{2C_{\star}}\right)\|\nabla f(\bar{W}_{k})\|^{2}-\left(\frac{\alpha C_{2}C_{\star}}{2}-\frac{\alpha\sigma^{2}}{2q_{\min}}\right)\|G_{p}(P_{k})\|^{2}+{\Theta}\left(\frac{(C_{1}+C_{2})\Delta w_{\min}}{\gamma q_{\max}}+\frac{\gamma\Delta w_{\min}}{q_{\min}}\right) + ( 3 + C 2 ) ​ α 2 ​ L ​ q max 2 ​ σ 2 − ( β ​ q min 2 2 ​ γ ​ q max ​ C 1 − 6 ​ q max ​ γ 2 ​ η 2 α ​ q min 2 ) ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 \displaystyle\ +(3+C_{2})\alpha^{2}Lq_{\max}^{2}\sigma^{2}-\left(\frac{\beta q_{\min}^{2}}{2\gamma q_{\max}}C_{1}-\frac{6q_{\max}\gamma^{2}\eta^{2}}{\alpha q_{\min}^{2}}\right)\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2} − ( β 2 ​ γ ​ q max ​ C 1 − 4 ​ β 2 ​ q max α ​ q min 2 ) ​ ‖ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) − | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) ‖ 2 \displaystyle\ -\left(\frac{\beta}{2\gamma q_{\max}}C_{1}-\frac{4\beta^{2}q_{\max}}{\alpha q_{\min}^{2}}\right)\left\|(P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})\right\|^{2} + ( 3 ​ β ​ q max 3 γ ​ q min 2 ​ C 1 + 4 ​ β 2 ​ q max 3 α ​ q min 2 + 6 ​ q max ​ γ 2 ​ η 2 α ​ q min 2 ) ​ 𝔼 ξ k ​ [ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 ] \displaystyle\ +\left(\frac{3\beta q_{\max}^{3}}{\gamma q_{\min}^{2}}C_{1}+\frac{4\beta^{2}q_{\max}^{3}}{\alpha q_{\min}^{2}}+\frac{6q_{\max}\gamma^{2}\eta^{2}}{\alpha q_{\min}^{2}}\right){\mathbb{E}}_{\xi_{k}}[\|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2}] − ( 1 2 ​ α ​ q max − 3 ​ γ 2 ​ L − C 2 ​ L ) ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k + α ⁡ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) − b k ‖ 2 ] . \displaystyle\ -\left(\frac{1}{2\alpha q_{\max}}-3\gamma^{2}L-C_{2}L\right)~\mathbb{E}_{\xi_{k},b_{k}}\left[\left\|P_{k+1}-P_{k}+\alpha(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot F_{p}(P_{k})-b_{k}\right\|^{2}\right].

[308] p: The first inequality holds for:

[309] table: 𝔼 ξ k ​ [ ‖ Q k + 1 − Q k ‖ 2 ] \displaystyle\mathbb{E}_{\xi_{k}}\left[\|Q_{k+1}-Q_{k}\|^{2}\right] = 𝔼 ξ k ​ [ ‖ − η ⁡ ( P k + 1 − Q k ) ‖ 2 ] \displaystyle=\mathbb{E}_{\xi_{k}}\left[\|-\eta(P_{k+1}-Q_{k})\|^{2}\right] ≤ 2 ​ η 2 ​ 𝔼 ξ k ​ [ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 + ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 ] \displaystyle\leq 2\eta^{2}\mathbb{E}_{\xi_{k}}\left[\|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2}+\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}\right] (65)

[310] p: and the learning rate β \beta is sufficiently small such that 2 ​ β 2 γ 2 ≤ β ​ q max 3 γ ​ q min 2 \frac{2\beta^{2}}{\gamma^{2}}\leq\frac{\beta q_{\max}^{3}}{\gamma q_{\min}^{2}} . Let C 1 = 10 ​ β ​ γ ​ q max 2 α ​ q min 2 C_{1}=\frac{10\beta\gamma q_{\max}^{2}}{\alpha q_{\min}^{2}} , which leads to the positive coefficient in front of ‖ P ∗ ​ ( W k , Q k ) ⊙ F w ​ ( W k ) − | P ∗ ​ ( W k , Q k ) | ⊙ G w ​ ( W k ) ‖ 2 \left\|P^{*}(W_{k},Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})|\odot G_{w}(W_{k})\right\|^{2} . Let α \alpha large enough, which leads to the positive coefficient in front of 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k + α ⁡ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) − b k ‖ 2 ] \mathbb{E}_{\xi_{k},b_{k}}\left[\left\|P_{k+1}-P_{k}+\alpha(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot F_{p}(P_{k})-b_{k}\right\|^{2}\right] .

[311] table: 𝔼 ξ k , b k ​ [ V k + 1 ] ≤ \displaystyle{\mathbb{E}}_{\xi_{k},b_{k}}[V_{k+1}]\leq V k − ( α ​ q min 2 8 ​ q max − C 2 ​ α ​ q max 2 2 ​ C ⋆ ) ​ ‖ ∇ f ​ ( W ¯ k ) ‖ 2 − ( α ​ C 2 ​ C ⋆ 2 − α ​ σ 2 2 ​ q min ) ​ ‖ G p ​ ( P k ) ‖ 2 \displaystyle\ V_{k}-\left(\frac{\alpha q_{\min}^{2}}{8q_{\max}}-\frac{C_{2}\alpha q_{\max}^{2}}{2C_{\star}}\right)\|\nabla f(\bar{W}_{k})\|^{2}-\left(\frac{\alpha C_{2}C_{\star}}{2}-\frac{\alpha\sigma^{2}}{2q_{\min}}\right)\|G_{p}(P_{k})\|^{2} (66) + ( 30 ​ β 2 ​ q max 5 α ​ q min 4 + 4 ​ β 2 ​ q max 3 α ​ q min 2 + 6 ​ q max ​ γ 2 ​ η 2 α ​ q min 2 ) ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 ] \displaystyle\ +\left(\frac{30\beta^{2}q_{\max}^{5}}{\alpha q_{\min}^{4}}+\frac{4\beta^{2}q_{\max}^{3}}{\alpha q_{\min}^{2}}+\frac{6q_{\max}\gamma^{2}\eta^{2}}{\alpha q_{\min}^{2}}\right){\mathbb{E}}_{\xi_{k},b_{k}}[\|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2}] − ( β ​ q min 2 2 ​ γ ​ q max ​ C 1 − 6 ​ q max ​ γ 2 ​ η 2 α ​ q min 2 ) ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 + ( 3 + C 2 ) ​ α 2 ​ L ​ q max 2 ​ σ 2 + Θ ⁡ ( Δ ​ w min ) . \displaystyle\ -\left(\frac{\beta q_{\min}^{2}}{2\gamma q_{\max}}C_{1}-\frac{6q_{\max}\gamma^{2}\eta^{2}}{\alpha q_{\min}^{2}}\right)\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}+(3+C_{2})\alpha^{2}Lq_{\max}^{2}\sigma^{2}+{\Theta}(\Delta w_{\min}).

[312] p: Now we bound the term ‖ ∇ f ​ ( W ¯ k ) ‖ 2 \left\|\nabla f(\bar{W}_{k})\right\|^{2} in ( 66 ) by μ \mu -PL condition (which is implied by Assumption 3.3 )

[313] table: α ​ q min 2 8 ​ q max ​ ‖ ∇ f ​ ( W ¯ k ) ‖ 2 ≥ \displaystyle\frac{\alpha q_{\min}^{2}}{8q_{\max}}\left\|\nabla f(\bar{W}_{k})\right\|^{2}\geq α ​ μ ​ q min 2 4 ​ q max ​ ( f ⁡ ( W ¯ k ) − f ∗ ) . \displaystyle\ \frac{\alpha\mu q_{\min}^{2}}{4q_{\max}}(f(\bar{W}_{k})-f^{*}). (67)

[314] p: Notice that the ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 \|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2} appears in the RHS of ( 66 ) above, we also need the following lemma to bound it.

[315] h6: Lemma E.4 (Quadratic growth, Theorem 2, Karimi et al. (2016) ) .

[316] p: Under Assumption 3.3 , defining the optimal solution as W ∗ := arg ​ min W ⁡ f ​ ( W ) W^{*}:=\operatornamewithlimits{arg\,min}_{W}f(W) , it holds that

[317] table: 2 μ ​ ( f ⁡ ( W ) − f ∗ ) ≥ ‖ W − W ∗ ‖ 2 . \displaystyle\frac{2}{\mu}(f(W)-f^{*})\geq\|W-W^{*}\|^{2}. (68)

[318] p: Replacing W W in ( 68 ) with W k + γ ⁡ ( P k + 1 − Q k ) W_{k}+\gamma(P_{k+1}-Q_{k}) , we bound the term ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 \|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2} in ( 53 ) by

[319] table: 2 μ ​ ( f ⁡ ( W k + γ ⁡ ( P k + 1 − Q k ) ) − f ∗ ) ≥ ‖ W k + γ ​ P k + 1 − γ ​ Q k − W ∗ ‖ 2 = γ 2 ​ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 . \displaystyle\frac{2}{\mu}(f(W_{k}+\gamma(P_{k+1}-Q_{k}))-f^{*})\geq\|W_{k}+\gamma P_{k+1}-\gamma Q_{k}-W^{*}\|^{2}=\gamma^{2}\|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2}. (69)

[320] p: By inequality ( 52 ) in Lemma E.1 and ( 69 ), we bound the ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 \|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2} by

[321] table: ( 30 ​ β 2 ​ q max 5 α ​ q min 4 + 4 ​ β 2 ​ q max 3 α ​ q min 2 + 6 ​ q max ​ γ 2 ​ η 2 α ​ q min 2 ) ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 ] \displaystyle\ \left(\frac{30\beta^{2}q_{\max}^{5}}{\alpha q_{\min}^{4}}+\frac{4\beta^{2}q_{\max}^{3}}{\alpha q_{\min}^{2}}+\frac{6q_{\max}\gamma^{2}\eta^{2}}{\alpha q_{\min}^{2}}\right){\mathbb{E}}_{\xi_{k},b_{k}}[\|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2}] (70) ≤ ( a ) \displaystyle\overset{(a)}{\leq} ( 34 ​ β 2 ​ q max 5 α ​ q min 4 + 6 ​ q max ​ γ 2 ​ η 2 α ​ q min 2 ) ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 ] \displaystyle\ \left(\frac{34\beta^{2}q_{\max}^{5}}{\alpha q_{\min}^{4}}+\frac{6q_{\max}\gamma^{2}\eta^{2}}{\alpha q_{\min}^{2}}\right){\mathbb{E}}_{\xi_{k},b_{k}}[\|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2}] ≤ ( b ) \displaystyle\overset{(b)}{\leq} ( 68 ​ β 2 ​ q max 5 α ​ γ 2 ​ μ ​ q min 4 + 12 ​ q max ​ η 2 α ​ q min 2 ​ μ ) ​ 𝔼 ξ k , b k ​ [ f ⁡ ( W k + γ ⁡ ( P k + 1 − Q k ) ) − f ∗ ] \displaystyle\ \left(\frac{68\beta^{2}q_{\max}^{5}}{\alpha\gamma^{2}\mu q_{\min}^{4}}+\frac{12q_{\max}\eta^{2}}{\alpha q_{\min}^{2}\mu}\right){\mathbb{E}}_{\xi_{k},b_{k}}[f(W_{k}+\gamma(P_{k+1}-Q_{k}))-f^{*}] ≤ ( c ) \displaystyle\overset{(c)}{\leq} ( 68 ​ β 2 ​ q max 5 α ​ γ 2 ​ μ ​ q min 4 + 12 ​ q max ​ η 2 α ​ q min 2 ​ μ ) ​ ( f ⁡ ( W ¯ k ) − f ∗ + α ​ σ 2 2 ​ ‖ G p ​ ( P k ) F p ​ ( P k ) ‖ ∞ 2 + α 2 ​ L ​ q max 2 ​ σ 2 + Θ ⁡ ( γ ​ Δ ​ w min q min ) ) \displaystyle\ \left(\frac{68\beta^{2}q_{\max}^{5}}{\alpha\gamma^{2}\mu q_{\min}^{4}}+\frac{12q_{\max}\eta^{2}}{\alpha q_{\min}^{2}\mu}\right)\left(f(\bar{W}_{k})-f^{*}+\frac{\alpha\sigma^{2}}{2}\left\|\frac{G_{p}(P_{k})}{\sqrt{F_{p}(P_{k})}}\right\|_{\infty}^{2}+\alpha^{2}Lq_{\max}^{2}\sigma^{2}+{\Theta}\left(\frac{\gamma\Delta w_{\min}}{q_{\min}}\right)\right) − ( 68 ​ β 2 ​ q max 5 α ​ γ 2 ​ μ ​ q min 4 + 12 ​ q max ​ η 2 α ​ q min 2 ​ μ ) ​ α 2 ​ q max ​ ‖ ∇ f ​ ( W ¯ k ) ‖ 2 \displaystyle\ -\left(\frac{68\beta^{2}q_{\max}^{5}}{\alpha\gamma^{2}\mu q_{\min}^{4}}+\frac{12q_{\max}\eta^{2}}{\alpha q_{\min}^{2}\mu}\right)\frac{\alpha}{2q_{\max}}\|\nabla f(\bar{W}_{k})\|^{2} ≤ ( d ) \displaystyle\overset{(d)}{\leq} ( 68 ​ β 2 ​ q max 5 α ​ γ 2 ​ μ ​ q min 4 + 12 ​ q max ​ η 2 α ​ q min 2 ​ μ ) ​ ( f ⁡ ( W ¯ k ) − f ∗ ) + 𝒪 ⁡ ( β 2 ​ σ 2 ​ ‖ G p ​ ( P k ) F p ​ ( P k ) ‖ ∞ 2 + α ​ β 2 ​ q max 2 ​ σ 2 ) + Θ ⁡ ( γ ​ q max ​ Δ ​ w min q min 2 ) \displaystyle\ \left(\frac{68\beta^{2}q_{\max}^{5}}{\alpha\gamma^{2}\mu q_{\min}^{4}}+\frac{12q_{\max}\eta^{2}}{\alpha q_{\min}^{2}\mu}\right)(f(\bar{W}_{k})-f^{*})+{\mathcal{O}}\left(\beta^{2}\sigma^{2}\left\|\frac{G_{p}(P_{k})}{\sqrt{F_{p}(P_{k})}}\right\|_{\infty}^{2}+\alpha\beta^{2}q_{\max}^{2}\sigma^{2}\right)+{\Theta}\left(\frac{\gamma q_{\max}\Delta w_{\min}}{q_{\min}^{2}}\right) ≤ ( e ) \displaystyle\overset{(e)}{\leq} ( 68 ​ β 2 ​ q max 5 α ​ γ 2 ​ μ ​ q min 4 + 12 ​ q max ​ η 2 α ​ q min 2 ​ μ ) ​ ( f ⁡ ( W ¯ k ) − f ∗ ) + α ​ σ 2 ​ ‖ G p ​ ( P k ) F p ​ ( P k ) ‖ ∞ 2 + α 2 ​ L ​ q max 2 ​ σ 2 + Θ ⁡ ( γ ​ q max ​ Δ ​ w min q min 2 ) \displaystyle\ \left(\frac{68\beta^{2}q_{\max}^{5}}{\alpha\gamma^{2}\mu q_{\min}^{4}}+\frac{12q_{\max}\eta^{2}}{\alpha q_{\min}^{2}\mu}\right)(f(\bar{W}_{k})-f^{*})+\alpha\sigma^{2}\left\|\frac{G_{p}(P_{k})}{\sqrt{F_{p}(P_{k})}}\right\|_{\infty}^{2}+\alpha^{2}Lq_{\max}^{2}\sigma^{2}+{\Theta}\left(\frac{\gamma q_{\max}\Delta w_{\min}}{q_{\min}^{2}}\right)

[322] p: where ( a ) (a) uses q max q min ≥ 1 \frac{q_{\max}}{q_{\min}}\geq 1 ; (b) comes from ( 69 ); (c) comes from ( 52 ) in Lemma E.1 ; (d) holds by setting η ≤ β ​ q max 2 γ ​ q min \eta\leq\frac{\beta q_{\max}^{2}}{\gamma q_{\min}} and β ≤ γ q max \beta\leq\frac{\gamma}{q_{\max}} ; (e) holds given α \alpha and β \beta is sufficiently small.

[323] p: Substituting ( 67 ) and ( 70 ) back into ( 66 ) yields

[324] table: 𝔼 ξ k , b k ​ [ V k + 1 ] \displaystyle\ {\mathbb{E}}_{\xi_{k},b_{k}}[V_{k+1}] (71) ≤ \displaystyle\leq V k − ( α ​ C 2 ​ C ⋆ 2 − 3 ​ α ​ σ 2 2 ​ q min ) ​ ‖ G p ​ ( P k ) ‖ 2 − ( α ​ μ ​ q min 2 4 ​ q max − 68 ​ β 2 ​ q max 5 α ​ γ 2 ​ μ ​ q min 4 − 12 ​ q max ​ η 2 α ​ q min 2 ​ μ − C 2 ​ α ​ q max 2 2 ​ C ⋆ ) ​ ( f ⁡ ( W ¯ k ) − f ∗ ) \displaystyle\ V_{k}-\left(\frac{\alpha C_{2}C_{\star}}{2}-\frac{3\alpha\sigma^{2}}{2q_{\min}}\right)\|G_{p}(P_{k})\|^{2}-\left(\frac{\alpha\mu q_{\min}^{2}}{4q_{\max}}-\frac{68\beta^{2}q_{\max}^{5}}{\alpha\gamma^{2}\mu q_{\min}^{4}}-\frac{12q_{\max}\eta^{2}}{\alpha q_{\min}^{2}\mu}-\frac{C_{2}\alpha q_{\max}^{2}}{2C_{\star}}\right)(f(\bar{W}_{k})-f^{*}) − ( β ​ q min 2 2 ​ γ ​ q max ​ C 1 − 6 ​ q max ​ γ 2 ​ η 2 α ​ q min 2 ) ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 + ( 4 + C 2 ) ​ α 2 ​ L ​ q max 2 ​ σ 2 + Θ ⁡ ( Δ ​ w min ) \displaystyle\ -\left(\frac{\beta q_{\min}^{2}}{2\gamma q_{\max}}C_{1}-\frac{6q_{\max}\gamma^{2}\eta^{2}}{\alpha q_{\min}^{2}}\right)\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}+(4+C_{2})\alpha^{2}Lq_{\max}^{2}\sigma^{2}+{\Theta}(\Delta w_{\min}) = \displaystyle= V k − ( α ​ C 2 ​ C ⋆ 2 − 3 ​ α ​ σ 2 2 ​ q min ) ​ ‖ G p ​ ( P k ) ‖ 2 − ( α ​ μ ​ q min 2 8 ​ q max − 12 ​ q max ​ η 2 α ​ q min 2 ​ μ − C 2 ​ α ​ q max 2 2 ​ C ⋆ ) ​ ( f ⁡ ( W ¯ k ) − f ∗ ) \displaystyle\ V_{k}-\left(\frac{\alpha C_{2}C_{\star}}{2}-\frac{3\alpha\sigma^{2}}{2q_{\min}}\right)\|G_{p}(P_{k})\|^{2}-\left(\frac{\alpha\mu q_{\min}^{2}}{8q_{\max}}-\frac{12q_{\max}\eta^{2}}{\alpha q_{\min}^{2}\mu}-\frac{C_{2}\alpha q_{\max}^{2}}{2C_{\star}}\right)(f(\bar{W}_{k})-f^{*}) − ( α ​ μ ​ q min 5 8 ​ 34 ​ q max 4 − 12 ​ 34 ​ q max 2 ​ η 2 5 ​ α ​ μ ​ q min 3 ) ​ C 1 ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 + ( 4 + C 2 ) ​ α 2 ​ L ​ q max 2 ​ σ 2 + Θ ⁡ ( Δ ​ w min ) \displaystyle\ -\left(\frac{\alpha\mu q_{\min}^{5}}{8\sqrt{34}q_{\max}^{4}}-\frac{12\sqrt{34}q_{\max}^{2}\eta^{2}}{5\alpha\mu q_{\min}^{3}}\right)C_{1}\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}+(4+C_{2})\alpha^{2}Lq_{\max}^{2}\sigma^{2}+{\Theta}(\Delta w_{\min}) ≤ \displaystyle\leq V k − ( α ​ μ ​ q min 5 8 ​ 34 ​ q max 4 − 12 ​ 34 ​ q max 2 ​ η 2 5 ​ α ​ μ ​ q min 3 ) ​ ( ( f ⁡ ( W ¯ k ) − f ∗ ) + C 1 ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 + ‖ G p ​ ( P k ) ‖ 2 ) \displaystyle\ V_{k}-\left(\frac{\alpha\mu q_{\min}^{5}}{8\sqrt{34}q_{\max}^{4}}-\frac{12\sqrt{34}q_{\max}^{2}\eta^{2}}{5\alpha\mu q_{\min}^{3}}\right)\left((f(\bar{W}_{k})-f^{*})+C_{1}\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}+\|G_{p}(P_{k})\|^{2}\right) + ( 4 + C 2 ) ​ α 2 ​ L ​ q max 2 ​ σ 2 + Θ ⁡ ( Δ ​ w min ) \displaystyle\ +(4+C_{2})\alpha^{2}Lq_{\max}^{2}\sigma^{2}+{\Theta}(\Delta w_{\min}) ≤ \displaystyle\leq V k − α ​ μ ​ q min 5 16 ​ 34 ​ q max 4 ​ ( ( f ⁡ ( W ¯ k ) − f ∗ ) + C 1 ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 + ‖ G p ​ ( P k ) ‖ 2 ) + 5 ​ α 2 ​ L ​ q max 2 ​ σ 2 + Θ ⁡ ( Δ ​ w min ) \displaystyle\ V_{k}-\frac{\alpha\mu q_{\min}^{5}}{16\sqrt{34}q_{\max}^{4}}\left((f(\bar{W}_{k})-f^{*})+C_{1}\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}+\|G_{p}(P_{k})\|^{2}\right)+5\alpha^{2}Lq_{\max}^{2}\sigma^{2}+{\Theta}(\Delta w_{\min})

[325] p: where the second step chooses the learning rate by β = α ​ γ ​ μ ​ q min 3 4 ​ 34 ​ q max 3 \beta=\frac{\alpha\gamma\mu q_{\min}^{3}}{4\sqrt{34}q_{\max}^{3}} . The third step holds since q max 2 q min 2 ≥ 1 \frac{q_{\max}^{2}}{q_{\min}^{2}}\geq 1 , and choose 4 ​ σ 2 C ⋆ ​ q min ≤ C 2 ≤ μ ​ q min 2 ​ C ⋆ 8 ​ q max 3 \frac{4\sigma^{2}}{C_{\star}q_{\min}}\leq C_{2}\leq\frac{\mu q_{\min}^{2}C_{\star}}{8q_{\max}^{3}} , such that α ​ C 2 ​ C ⋆ 2 − 3 ​ α ​ σ 2 2 ​ q min ≥ α ​ μ ​ q min 5 8 ​ 34 ​ q max 4 − 12 ​ 34 ​ q max 2 ​ η 2 5 ​ α ​ μ ​ q min 3 \frac{\alpha C_{2}C_{\star}}{2}-\frac{3\alpha\sigma^{2}}{2q_{\min}}\geq\frac{\alpha\mu q_{\min}^{5}}{8\sqrt{34}q_{\max}^{4}}-\frac{12\sqrt{34}q_{\max}^{2}\eta^{2}}{5\alpha\mu q_{\min}^{3}} and C 2 ​ α ​ q max 2 2 ​ C ⋆ ≤ α ​ μ ​ q min 2 16 ​ q max \frac{C_{2}\alpha q_{\max}^{2}}{2C_{\star}}\leq\frac{\alpha\mu q_{\min}^{2}}{16q_{\max}} . The last step chooses η ≤ α ​ μ ​ q min 4 52 ​ q max 3 \eta\leq\frac{\alpha\mu q_{\min}^{4}}{52q_{\max}^{3}} such that 12 ​ 34 ​ q max 2 ​ η 2 5 ​ α ​ μ ​ q min 3 ≤ α ​ μ ​ q min 5 32 ​ 34 ​ q max 4 . \frac{12\sqrt{34}q_{\max}^{2}\eta^{2}}{5\alpha\mu q_{\min}^{3}}\leq\frac{\alpha\mu q_{\min}^{5}}{32\sqrt{34}q_{\max}^{4}}.

[326] p: Rearranging ( 71 ), taking expectations with respect to { ξ k } k = 0 K \{\xi_{k}\}_{k=0}^{K} , and averaging over k = 0 , … , K k=0,\ldots,K , and choosing the stepsize α = Θ ( K − 1 / 2 ) \alpha=\Theta(K^{-1/2}) , we obtain

[327] table: 1 K ​ ∑ k = 0 K 𝔼 ⁡ ( ( f ⁡ ( W ¯ k ) − f ∗ ) + C 1 ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 + ‖ G p ​ ( P k ) ‖ 2 ) \displaystyle\frac{1}{K}\sum_{k=0}^{K}\mathbb{E}\left(\Big(f(\bar{W}_{k})-f^{*}\Big)+C_{1}\big\|P^{*}(W_{k},Q_{k})-Q_{k}\big\|^{2}+\big\|G_{p}(P_{k})\big\|^{2}\right) ≤ \displaystyle\leq 16 ​ 34 ​ q max 4 μ ​ q min 5 ​ ( V 0 − V [ K ] α ​ K + 5 ​ α ​ L ​ q max 2 ​ σ 2 ) + Θ ⁡ ( Δ ​ w min ) ≤ 𝒪 ⁡ ( κ 2 5 K ) + Θ ⁡ ( Δ ​ w min ) . \displaystyle\frac{16\sqrt{34}\,q_{\max}^{4}}{\mu\,q_{\min}^{5}}\left(\frac{V_{0}-V_{[K]}}{\alpha K}+5\alpha Lq_{\max}^{2}\sigma^{2}\right)+{\Theta}(\Delta w_{\min})\leq\mathcal{O}\left(\frac{\kappa_{2}^{5}}{\sqrt{K}}\right)+{\Theta}(\Delta w_{\min}). (72)

[328] p: Since ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ = ‖ W k − W ∗ ‖ / γ \|P^{*}(W_{k},Q_{k})-Q_{k}\|=\|W_{k}-W^{*}\|/\gamma and f ⁡ ( W ¯ k ) − f ∗ ≥ μ 2 ​ ‖ W ¯ k − W ∗ ‖ 2 = μ 2 ​ ‖ W k − W ∗ + γ ⁡ ( P k − Q k ) ‖ 2 f(\bar{W}_{k})-f^{*}\geq\frac{\mu}{2}\|\bar{W}_{k}-W^{*}\|^{2}=\frac{\mu}{2}\|W_{k}-W^{*}+\gamma(P_{k}-Q_{k})\|^{2} , we know that

[329] table: ‖ P k − Q k ‖ 2 \displaystyle\|P_{k}-Q_{k}\|^{2} ≤ 2 ​ γ − 2 ​ ‖ W ¯ k − W ∗ ‖ 2 + 2 ​ γ − 2 ​ ‖ W k − W ∗ ‖ 2 ≤ 2 ​ γ − 2 ​ ‖ W ¯ k − W ∗ ‖ 2 + 2 ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 \displaystyle\leq 2\gamma^{-2}\|\bar{W}_{k}-W^{*}\|^{2}+2\gamma^{-2}\|W_{k}-W^{*}\|^{2}\leq 2\gamma^{-2}\|\bar{W}_{k}-W^{*}\|^{2}+2\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2} ≤ 4 μ ​ γ − 2 ​ ( f ⁡ ( W ¯ k ) − f ∗ ) + 2 ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 \displaystyle\leq\frac{4}{\mu}\gamma^{-2}(f(\bar{W}_{k})-f^{*})+2\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}

[330] p: and thus by choosing C 1 = 𝒪 ⁡ ( γ 2 ) C_{1}={\cal O}(\gamma^{2}) , we have

[331] table: 1 K ​ ∑ k = 0 K 𝔼 ⁡ ( ‖ W k − W ∗ ‖ 2 + C 1 ​ ‖ P k − Q k ‖ 2 + ‖ G p ​ ( P k ) ‖ 2 ) \displaystyle\frac{1}{K}\sum_{k=0}^{K}\mathbb{E}\left(\big\|W_{k}-W^{*}\big\|^{2}+C_{1}\|P_{k}-Q_{k}\|^{2}+\big\|G_{p}(P_{k})\big\|^{2}\right) ≤ \displaystyle\leq 16 ​ 34 ​ q max 4 μ ​ q min 5 ​ ( V 0 − V [ K ] α ​ K + 5 ​ α ​ L ​ q max 2 ​ σ 2 ) + Θ ⁡ ( Δ ​ w min ) ≤ 𝒪 ⁡ ( κ 2 5 κ 1 ​ K ) + Θ ⁡ ( Δ ​ w min ) . \displaystyle\frac{16\sqrt{34}\,q_{\max}^{4}}{\mu\,q_{\min}^{5}}\left(\frac{V_{0}-V_{[K]}}{\alpha K}+5\alpha Lq_{\max}^{2}\sigma^{2}\right)+{\Theta}(\Delta w_{\min})\leq\mathcal{O}\left(\frac{\kappa_{2}^{5}}{\kappa_{1}\sqrt{K}}\right)+{\Theta}(\Delta w_{\min}). (73)

[332] p: The proof of Theorem 3.7 is completed. ∎

[333] h4: E.2 Proof of Lemma E.1 : Descent of sequence W ¯ k \bar{W}_{k}

[334] p: See E.1

[335] h6: Lemma E.1 .

[336] p: The L L -smooth assumption (Assumption 3.1 ) implies that

[337] table: 𝔼 ξ k , b k ​ [ f ⁡ ( W ¯ k + 1 ) ] ≤ f ⁡ ( W ¯ k ) + 𝔼 ξ k , b k ​ [ ⟨ ∇ f ​ ( W ¯ k ) , W ¯ k + 1 − W ¯ k ⟩ ] + L 2 ​ 𝔼 ξ k , b k ​ [ ‖ W ¯ k + 1 − W ¯ k ‖ 2 ] \displaystyle\ \mathbb{E}_{\xi_{k},b_{k}}[f(\bar{W}_{k+1})]\leq f(\bar{W}_{k})+\mathbb{E}_{\xi_{k},b_{k}}[\left\langle\nabla f(\bar{W}_{k}),\bar{W}_{k+1}-\bar{W}_{k}\right\rangle]+\frac{L}{2}\mathbb{E}_{\xi_{k},b_{k}}[\|\bar{W}_{k+1}-\bar{W}_{k}\|^{2}] (74) = \displaystyle= f ⁡ ( W ¯ k ) + γ ​ 𝔼 ξ k , b k ​ [ ⟨ ∇ f ​ ( W ¯ k ) , P k + 1 − P k ⟩ ] ⏟ ( a ) + 𝔼 ξ k ​ [ ⟨ ∇ f ​ ( W ¯ k ) , W k + 1 − W k ⟩ ] ⏟ ( b ) + L 2 ​ 𝔼 ξ k , b k ​ [ ‖ W ¯ k + 1 − W ¯ k ‖ 2 ] ⏟ ( c ) . \displaystyle\ f(\bar{W}_{k})+\gamma\underbrace{\mathbb{E}_{\xi_{k},b_{k}}[\left\langle\nabla f(\bar{W}_{k}),P_{k+1}-P_{k}\right\rangle]}_{(a)}+\underbrace{\mathbb{E}_{\xi_{k}}[\left\langle\nabla f(\bar{W}_{k}),W_{k+1}-W_{k}\right\rangle]}_{(b)}+\underbrace{\frac{L}{2}\mathbb{E}_{\xi_{k},b_{k}}[\|\bar{W}_{k+1}-\bar{W}_{k}\|^{2}]}_{(c)}. − γ ​ 𝔼 ξ k ​ [ ⟨ ∇ f ​ ( W ¯ k ) , Q k + 1 − Q k ⟩ ] ⏟ ( d ) \displaystyle-\gamma\underbrace{\mathbb{E}_{\xi_{k}}[\left\langle\nabla f(\bar{W}_{k}),Q_{k+1}-Q_{k}\right\rangle]}_{(d)}

[338] p: Next, we will handle each term in the RHS of ( 74 ) separately.

[339] p: Bound of the second term (a). To bound term (a) in the RHS of ( 74 ), we leverage the assumption that noise has expectation 0 0 (Assumption 3.2 )

[340] table: 𝔼 ξ k , b k ​ [ ⟨ ∇ f ​ ( W ¯ k ) , P k + 1 − P k ⟩ ] \displaystyle\ \mathbb{E}_{\xi_{k},b_{k}}[\left\langle\nabla f(\bar{W}_{k}),P_{k+1}-P_{k}\right\rangle] (75) = \displaystyle= α ​ 𝔼 ξ k , b k ​ [ ⟨ ∇ f ​ ( W ¯ k ) ⊙ F p ​ ( P k ) , P k + 1 − P k α ​ F p ​ ( P k ) + ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) − b k α ​ F p ​ ( P k ) ⟩ ] \displaystyle\ \alpha\mathbb{E}_{\xi_{k},b_{k}}\left[\left\langle\nabla f(\bar{W}_{k})\odot\sqrt{F_{p}(P_{k})},\frac{P_{k+1}-P_{k}}{\alpha\sqrt{F_{p}(P_{k})}}+(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot\sqrt{F_{p}(P_{k})}-\frac{b_{k}}{\alpha\sqrt{F_{p}(P_{k})}}\right\rangle\right] = \displaystyle= − α 2 ​ ‖ ∇ f ​ ( W ¯ k ) ⊙ F p ​ ( P k ) ‖ 2 \displaystyle\ -\frac{\alpha}{2}\|\nabla f(\bar{W}_{k})\odot\sqrt{F_{p}(P_{k})}\|^{2} − 1 2 ​ α ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k F p ​ ( P k ) + α ⁡ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) − b k F p ​ ( P k ) ‖ 2 ] \displaystyle\ -\frac{1}{2\alpha}\mathbb{E}_{\xi_{k},b_{k}}\left[\left\|\frac{P_{k+1}-P_{k}}{\sqrt{F_{p}(P_{k})}}+\alpha(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot\sqrt{F_{p}(P_{k})}-\frac{b_{k}}{\sqrt{F_{p}(P_{k})}}\right\|^{2}\right] + 1 2 ​ α 𝔼 ξ k , b k [ ‖ P k + 1 − P k F p ​ ( P k ) + α ∇ f ( W ¯ k ; ξ k ) ⊙ F p ​ ( P k ) − b k F p ​ ( P k ) ‖ 2 ] . \displaystyle\ +\frac{1}{2\alpha}\mathbb{E}_{\xi_{k},b_{k}}\left[\left\|\frac{P_{k+1}-P_{k}}{\sqrt{F_{p}(P_{k})}}+\alpha\nabla f(\bar{W}_{k};\xi_{k})\odot\sqrt{F_{p}(P_{k})}-\frac{b_{k}}{\sqrt{F_{p}(P_{k})}}\right\|^{2}\right].

[341] p: The second term in the RHS of ( 75 ) can be bounded by

[342] table: 1 2 ​ α ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k F p ​ ( P k ) + α ⁡ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) − b k F p ​ ( P k ) ‖ 2 ] \displaystyle\frac{1}{2\alpha}\mathbb{E}_{\xi_{k},b_{k}}\left[\left\|\frac{P_{k+1}-P_{k}}{\sqrt{F_{p}(P_{k})}}+\alpha(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot\sqrt{F_{p}(P_{k})}-\frac{b_{k}}{\sqrt{F_{p}(P_{k})}}\right\|^{2}\right] (76) = \displaystyle= 1 2 ​ α ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k + α ⁡ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) − b k F p ​ ( P k ) ‖ 2 ] \displaystyle\ \frac{1}{2\alpha}\mathbb{E}_{\xi_{k},b_{k}}\left[\left\|\frac{P_{k+1}-P_{k}+\alpha(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot F_{p}(P_{k})-b_{k}}{\sqrt{F_{p}(P_{k})}}\right\|^{2}\right] ≥ \displaystyle\geq 1 2 ​ α ​ q max ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k + α ⁡ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) − b k ‖ 2 ] . \displaystyle\ \frac{1}{2\alpha q_{\max}}\mathbb{E}_{\xi_{k},b_{k}}\left[\|P_{k+1}-P_{k}+\alpha(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot F_{p}(P_{k})-b_{k}\|^{2}\right].

[343] p: The third term in the RHS of ( 75 ) can be bounded by the bounded variance (Assumption 3.2 )

[344] table: 1 2 ​ α 𝔼 ξ k , b k [ ‖ P k + 1 − P k F p ​ ( P k ) + α ∇ f ( W ¯ k ; ξ k ) ⊙ F p ​ ( P k ) − b k F p ​ ( P k ) ‖ 2 ] \displaystyle~~~~~\frac{1}{2\alpha}\mathbb{E}_{\xi_{k},b_{k}}\left[\left\|\frac{P_{k+1}-P_{k}}{\sqrt{F_{p}(P_{k})}}+\alpha\nabla f(\bar{W}_{k};\xi_{k})\odot\sqrt{F_{p}(P_{k})}-\frac{b_{k}}{\sqrt{F_{p}(P_{k})}}\right\|^{2}\right] (77) ≤ α 2 ​ 𝔼 ξ k , b k ​ [ ‖ | ∇ f ​ ( W ¯ k , ξ k ) | ⊙ G p ​ ( P k ) F p ​ ( P k ) − b k α ​ F p ​ ( P k ) ‖ 2 ] \displaystyle\leq\frac{\alpha}{2}\mathbb{E}_{\xi_{k},b_{k}}\left[\left\||\nabla f(\bar{W}_{k};\xi_{k})|\odot\frac{G_{p}(P_{k})}{\sqrt{F_{p}(P_{k})}}-\frac{b_{k}}{\alpha\sqrt{F_{p}(P_{k})}}\right\|^{2}\right] (78) = ( a ) α 2 ​ 𝔼 ξ k , b k ​ [ ‖ ∇ f ​ ( W ¯ k , ξ k ) ⊙ G p ​ ( P k ) F p ​ ( P k ) − b k α ​ F p ​ ( P k ) ‖ 2 ] \displaystyle\stackrel{{\scriptstyle(a)}}{{=}}\frac{\alpha}{2}\mathbb{E}_{\xi_{k},b_{k}}\left[\left\|\nabla f(\bar{W}_{k};\xi_{k})\odot\frac{G_{p}(P_{k})}{\sqrt{F_{p}(P_{k})}}-\frac{b_{k}}{\alpha\sqrt{F_{p}(P_{k})}}\right\|^{2}\right] (79) ≤ ( b ) α 2 ​ ‖ ∇ f ​ ( W ¯ k ) ⊙ G p ​ ( P k ) F p ​ ( P k ) ‖ 2 + α ​ σ 2 2 ​ ‖ G p ​ ( P k ) F p ​ ( P k ) ‖ ∞ 2 + Θ ⁡ ( Δ ​ w min q min ) . \displaystyle\stackrel{{\scriptstyle(b)}}{{\leq}}\frac{\alpha}{2}\left\|\nabla f(\bar{W}_{k})\odot\frac{G_{p}(P_{k})}{\sqrt{F_{p}(P_{k})}}\right\|^{2}+\frac{\alpha\sigma^{2}}{2}\left\|\frac{G_{p}(P_{k})}{\sqrt{F_{p}(P_{k})}}\right\|^{2}_{\infty}+{\Theta}\left(\frac{\Delta w_{\min}}{q_{\min}}\right).

[345] p: where ( a ) (a) is because 𝔼 b k ​ ⟨ | ∇ f ​ ( W ¯ k , ξ k ) | ⊙ G p ​ ( P k ) F p ​ ( P k ) , b k α ​ F p ​ ( P k ) ⟩ = 0 \mathbb{E}_{b_{k}}\left\langle|\nabla f(\bar{W}_{k};\xi_{k})|\odot\frac{G_{p}(P_{k})}{\sqrt{F_{p}(P_{k})}},\frac{b_{k}}{\alpha\sqrt{F_{p}(P_{k})}}\right\rangle=0 according to Assumption 3.4 and ( b ) (b) comes from 𝔼 ⁡ [ ‖ A ‖ 2 ] = ‖ 𝔼 ⁡ [ A ] ‖ 2 + 𝔼 ⁡ [ ‖ A − 𝔼 ⁡ [ A ] ‖ 2 ] \mathbb{E}[\|A\|^{2}]=\|\mathbb{E}[A]\|^{2}+\mathbb{E}[\|A-\mathbb{E}[A]\|^{2}] and Assumption 3.2 .

[346] p: Notice that the first term in the RHS of ( 75 ) and the second term in the RHS of ( 77 ) can be bounded together

[347] table: − α 2 ​ ‖ ∇ f ​ ( W ¯ k ) ⊙ F p ​ ( P k ) ‖ 2 + α 2 ​ ‖ ∇ f ​ ( W ¯ k ) ⊙ G p ​ ( P k ) F p ​ ( P k ) ‖ 2 \displaystyle\ -\frac{\alpha}{2}\|\nabla f(\bar{W}_{k})\odot\sqrt{F_{p}(P_{k})}\|^{2}+\frac{\alpha}{2}\left\|\nabla f(\bar{W}_{k})\odot\frac{G_{p}(P_{k})}{\sqrt{F_{p}(P_{k})}}\right\|^{2} (80) = \displaystyle= − α 2 ∑ d ∈ [ D ] ( [ ∇ f ( W ¯ k ) ] d 2 ( [ F p ( P k ) ] d − [ G p ​ ( P k ) ] d 2 [ F p ​ ( P k ) ] d ) ) \displaystyle\ -\frac{\alpha}{2}\sum_{d\in[D]}\left([\nabla f(\bar{W}_{k})]_{d}^{2}\left([F_{p}(P_{k})]_{d}-\frac{[G_{p}(P_{k})]^{2}_{d}}{[F_{p}(P_{k})]_{d}}\right)\right) = \displaystyle= − α 2 ∑ d ∈ [ D ] ( [ ∇ f ( W ¯ k ) ] d 2 ( [ F p ​ ( P k ) ] d 2 − [ G p ​ ( P k ) ] d 2 [ F p ​ ( P k ) ] d ) ) \displaystyle\ -\frac{\alpha}{2}\sum_{d\in[D]}\left([\nabla f(\bar{W}_{k})]_{d}^{2}\left(\frac{[F_{p}(P_{k})]^{2}_{d}-[G_{p}(P_{k})]^{2}_{d}}{[F_{p}(P_{k})]_{d}}\right)\right) ≤ \displaystyle\leq − α 2 ​ q max ∑ d ∈ [ D ] ( [ ∇ f ( W ¯ k ) ] d 2 ( [ F p ( P k ) ] d 2 − [ G p ( P k ) ] d 2 ) ) \displaystyle\ -\frac{\alpha}{2q_{\max}}\sum_{d\in[D]}\left([\nabla f(\bar{W}_{k})]_{d}^{2}\left([F_{p}(P_{k})]_{d}^{2}-[G_{p}(P_{k})]^{2}_{d}\right)\right) = \displaystyle= − α 2 ​ q max ​ ‖ ∇ f ​ ( W ¯ k ) ‖ M p ​ ( P k ) 2 ≤ 0 . \displaystyle\ -\frac{\alpha}{2q_{\max}}\|\nabla f(\bar{W}_{k})\|^{2}_{M_{p}(P_{k})}\leq 0.

[348] p: Plugging ( 76 ) to ( 80 ) into ( 75 ), we bound the term (a) by

[349] table: γ ​ 𝔼 ξ k , b k ​ [ ⟨ ∇ f ​ ( W ¯ k ) , P k + 1 − P k ⟩ ] ≤ \displaystyle\gamma\mathbb{E}_{\xi_{k},b_{k}}[\left\langle\nabla f(\bar{W}_{k}),P_{k+1}-P_{k}\right\rangle]\leq − α ​ γ 2 ​ q max ​ ‖ ∇ f ​ ( W ¯ k ) ‖ M p ​ ( P k ) 2 + α ​ γ ​ σ 2 2 ​ ‖ G p ​ ( P k ) F p ​ ( P k ) ‖ ∞ 2 + Θ ⁡ ( γ ​ Δ ​ w min q min ) \displaystyle\ -\frac{\alpha\gamma}{2q_{\max}}\|\nabla f(\bar{W}_{k})\|^{2}_{M_{p}(P_{k})}+\frac{\alpha\gamma\sigma^{2}}{2}\left\|\frac{G_{p}(P_{k})}{\sqrt{F_{p}(P_{k})}}\right\|^{2}_{\infty}+{\Theta}\left(\frac{\gamma\Delta w_{\min}}{q_{\min}}\right) (81) − γ 2 ​ α ​ q max ​ 𝔼 ξ k ​ [ ‖ P k + 1 − P k + α ⁡ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) − b k ‖ 2 ] . \displaystyle\ -\frac{\gamma}{2\alpha q_{\max}}\mathbb{E}_{\xi_{k}}\left[\left\|P_{k+1}-P_{k}+\alpha(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot F_{p}(P_{k})-b_{k}\right\|^{2}\right].

[350] p: Bound of the third term (b). By Young’s inequality, we have

[351] table: 𝔼 ξ k ​ [ ⟨ ∇ f ​ ( W ¯ k ) , W k + 1 − W k ⟩ ] ≤ \displaystyle\mathbb{E}_{\xi_{k}}[\left\langle\nabla f(\bar{W}_{k}),W_{k+1}-W_{k}\right\rangle]\leq α ​ γ 4 ​ q max ​ ‖ ∇ f ​ ( W ¯ k ) ‖ M p ​ ( P k ) 2 + q max α ​ γ ​ 𝔼 ξ k ​ [ ‖ W k + 1 − W k ‖ M p ​ ( P k ) † 2 ] . \displaystyle\ \frac{\alpha\gamma}{4q_{\max}}\|\nabla f(\bar{W}_{k})\|^{2}_{M_{p}(P_{k})}+\frac{q_{\max}}{\alpha\gamma}\mathbb{E}_{\xi_{k}}[\|W_{k+1}-W_{k}\|^{2}_{M_{p}(P_{k})^{\dagger}}]. (82)

[352] p: Bound of the fourth term (c). Repeatedly applying inequality ‖ U + V ‖ 2 ≤ 2 ​ ‖ U ‖ 2 + 2 ​ ‖ V ‖ 2 \|U+V\|^{2}\leq 2\|U\|^{2}+2\|V\|^{2} for any U , V ∈ ℝ D U,V\in{\mathbb{R}}^{D} , we have

[353] table: L 2 ​ 𝔼 ξ k , b k ​ [ ‖ W ¯ k + 1 − W ¯ k ‖ 2 ] \displaystyle\ \frac{L}{2}\mathbb{E}_{\xi_{k},b_{k}}[\|\bar{W}_{k+1}-\bar{W}_{k}\|^{2}] (83) ≤ \displaystyle\leq 3 ​ L 2 ​ 𝔼 ξ k ​ [ ‖ W k + 1 − W k ‖ 2 ] + 3 ​ γ 2 ​ L 2 ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k ‖ 2 ] + 3 ​ γ 2 ​ L 2 ​ 𝔼 ξ k ​ [ ‖ Q k + 1 − Q k ‖ 2 ] \displaystyle\ \frac{3L}{2}\mathbb{E}_{\xi_{k}}[\|W_{k+1}-W_{k}\|^{2}]+\frac{3\gamma^{2}L}{2}\mathbb{E}_{\xi_{k},b_{k}}[\|P_{k+1}-P_{k}\|^{2}]+\frac{3\gamma^{2}L}{2}\mathbb{E}_{\xi_{k}}[\|Q_{k+1}-Q_{k}\|^{2}] ≤ \displaystyle\leq 3 ​ L 2 ​ 𝔼 ξ k ​ [ ‖ W k + 1 − W k ‖ 2 ] + 3 ​ γ 2 ​ L ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k + α ⁡ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) ‖ 2 ] \displaystyle\ \frac{3L}{2}\mathbb{E}_{\xi_{k}}[\|W_{k+1}-W_{k}\|^{2}]+3\gamma^{2}L\mathbb{E}_{\xi_{k},b_{k}}\left[\left\|P_{k+1}-P_{k}+\alpha(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot F_{p}(P_{k})\right\|^{2}\right] + 3 ​ α 2 ​ L ​ γ 2 ​ 𝔼 ξ k ​ [ ‖ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) ‖ 2 ] + 3 ​ γ 2 ​ L 2 ​ 𝔼 ξ k ​ [ ‖ Q k + 1 − Q k ‖ 2 ] \displaystyle\ +3\alpha^{2}L\gamma^{2}\mathbb{E}_{\xi_{k}}\left[\left\|(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot F_{p}(P_{k})\right\|^{2}\right]+\frac{3\gamma^{2}L}{2}\mathbb{E}_{\xi_{k}}[\|Q_{k+1}-Q_{k}\|^{2}] ≤ \displaystyle\leq 3 ​ L 2 ​ 𝔼 ξ k ​ [ ‖ W k + 1 − W k ‖ 2 ] + 3 ​ γ 2 ​ L ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k + α ⁡ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) − b k ‖ 2 ] + 3 ​ α 2 ​ γ 2 ​ L ​ q max 2 ​ σ 2 \displaystyle\ \frac{3L}{2}\mathbb{E}_{\xi_{k}}[\|W_{k+1}-W_{k}\|^{2}]+3\gamma^{2}L\mathbb{E}_{\xi_{k},b_{k}}\left[\left\|P_{k+1}-P_{k}+\alpha(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot F_{p}(P_{k})-b_{k}\right\|^{2}\right]+3\alpha^{2}\gamma^{2}Lq_{\max}^{2}\sigma^{2} + 3 ​ γ 2 ​ L 2 ​ 𝔼 ξ k ​ [ ‖ Q k + 1 − Q k ‖ 2 ] + Θ ⁡ ( 3 ​ γ 2 ​ L ​ α ​ Δ ​ w min ) \displaystyle+\frac{3\gamma^{2}L}{2}\mathbb{E}_{\xi_{k}}[\|Q_{k+1}-Q_{k}\|^{2}]+{\Theta}\left(3\gamma^{2}L\alpha\Delta w_{\min}\right)

[354] p: where the last inequality comes from Assumption 3.4 and the bounded variance assumption (Assumption 3.2 )

[355] table: 3 ​ α 2 ​ γ 2 ​ L ​ 𝔼 ξ k ​ [ ‖ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) ‖ 2 ] \displaystyle\ 3\alpha^{2}\gamma^{2}L\mathbb{E}_{\xi_{k}}\left[\left\|(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot F_{p}(P_{k})\right\|^{2}\right] (84) ≤ \displaystyle\leq 3 ​ α 2 ​ γ 2 ​ L ​ q max 2 ​ 𝔼 ξ k ​ [ ‖ ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ‖ 2 ] ≤ 3 ​ α 2 ​ γ 2 ​ L ​ q max 2 ​ σ 2 . \displaystyle\ 3\alpha^{2}\gamma^{2}Lq_{\max}^{2}\mathbb{E}_{\xi_{k}}\left[\left\|\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k})\right\|^{2}\right]\leq 3\alpha^{2}\gamma^{2}Lq_{\max}^{2}\sigma^{2}.

[356] p: Bound of the fifth term (d). By Young’s inequality, we have

[357] table: − γ ​ 𝔼 ξ k , b k ​ [ ⟨ ∇ f ​ ( W ¯ k ) , Q k + 1 − Q k ⟩ ] ≤ \displaystyle-\gamma\mathbb{E}_{\xi_{k},b_{k}}[\left\langle\nabla f(\bar{W}_{k}),Q_{k+1}-Q_{k}\right\rangle]\leq α ​ γ 8 ​ q max ​ ‖ ∇ f ​ ( W ¯ k ) ‖ M p ​ ( P k ) 2 + 2 ​ q max ​ γ α ​ 𝔼 ξ k ​ [ ‖ Q k + 1 − Q k ‖ M p ​ ( P k ) † 2 ] . \displaystyle\ \frac{\alpha\gamma}{8q_{\max}}\|\nabla f(\bar{W}_{k})\|^{2}_{M_{p}(P_{k})}+\frac{2q_{\max}\gamma}{\alpha}\mathbb{E}_{\xi_{k}}[\|Q_{k+1}-Q_{k}\|^{2}_{M_{p}(P_{k})^{\dagger}}]. (85)

[358] p: Combination of the upper bound ( a ) (a) , ( b ) (b) , ( c ) (c) and ( d ) (d) . Plugging ( 81 ), ( 82 ), ( 83 ) into ( 74 ) and letting α ≤ 1 2 ​ γ ​ L ​ q max \alpha\leq\frac{1}{2\gamma Lq_{\max}} ,

[359] table: 𝔼 ξ k , b k ​ [ f ⁡ ( W ¯ k + 1 ) ] ≤ \displaystyle\mathbb{E}_{\xi_{k},b_{k}}[f(\bar{W}_{k+1})]\leq f ⁡ ( W ¯ k ) − α ​ γ 8 ​ q max ​ ‖ ∇ f ​ ( W ¯ k ) ‖ M p ​ ( P k ) 2 + α ​ γ ​ σ 2 2 ​ ‖ G p ​ ( P k ) F p ​ ( P k ) ‖ ∞ 2 + Θ ⁡ ( γ ​ Δ ​ w min q min ) \displaystyle\ f(\bar{W}_{k})-\frac{\alpha\gamma}{8q_{\max}}\|\nabla f(\bar{W}_{k})\|^{2}_{M_{p}(P_{k})}+\frac{\alpha\gamma\sigma^{2}}{2}\left\|\frac{G_{p}(P_{k})}{\sqrt{F_{p}(P_{k})}}\right\|^{2}_{\infty}+{\Theta}\left(\frac{\gamma\Delta w_{\min}}{q_{\min}}\right) + 2 ​ q max ​ γ α ​ 𝔼 ξ k ​ [ ‖ Q k + 1 − Q k ‖ M p ​ ( P k ) † 2 ] + 3 ​ γ 2 ​ L 2 ​ 𝔼 ξ k ​ [ ‖ Q k + 1 − Q k ‖ 2 ] \displaystyle\ +\frac{2q_{\max}\gamma}{\alpha}\mathbb{E}_{\xi_{k}}\left[\|Q_{k+1}-Q_{k}\|^{2}_{M_{p}(P_{k})^{\dagger}}\right]+\frac{3\gamma^{2}L}{2}\mathbb{E}_{\xi_{k}}\left[\|Q_{k+1}-Q_{k}\|^{2}\right] (86) − ( γ 2 ​ α ​ q max − 3 ​ γ 2 ​ L ) ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k + α ⁡ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) − b k ‖ 2 ] \displaystyle\ -\left(\frac{\gamma}{2\alpha q_{\max}}-3\gamma^{2}L\right)~\mathbb{E}_{\xi_{k},b_{k}}\left[\left\|P_{k+1}-P_{k}+\alpha(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot F_{p}(P_{k})-b_{k}\right\|^{2}\right] + 3 ​ α 2 ​ γ 2 ​ L ​ q max 2 ​ σ 2 + q max α ​ γ ​ 𝔼 ξ k ​ [ ‖ W k + 1 − W k ‖ M p ​ ( P k ) † 2 ] + 3 ​ L 2 ​ 𝔼 ξ k ​ [ ‖ W k + 1 − W k ‖ 2 ] . \displaystyle\ +3\alpha^{2}\gamma^{2}Lq_{\max}^{2}\sigma^{2}+\frac{q_{\max}}{\alpha\gamma}~\mathbb{E}_{\xi_{k}}\left[\|W_{k+1}-W_{k}\|^{2}_{M_{p}(P_{k})^{\dagger}}\right]+\frac{3L}{2}\mathbb{E}_{\xi_{k}}[\|W_{k+1}-W_{k}\|^{2}].

[360] p: Now the proof of ( 51 ) is completed. Leveraging the L L -smooth assumption (Assumption 3.1 ), we have

[361] table: 𝔼 ξ k , b k ​ [ f ⁡ ( W k + γ ⁡ ( P k + 1 − Q k ) ) ] = f ⁡ ( W ¯ k ) + γ ​ 𝔼 ξ k , b k ​ [ ⟨ ∇ f ​ ( W ¯ k ) , P k + 1 − P k ⟩ ] + L ​ γ 2 2 ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k ‖ 2 ] . \displaystyle\ \mathbb{E}_{\xi_{k},b_{k}}[f(W_{k}+\gamma(P_{k+1}-Q_{k}))]=f(\bar{W}_{k})+\gamma{\mathbb{E}_{\xi_{k},b_{k}}[\left\langle\nabla f(\bar{W}_{k}),P_{k+1}-P_{k}\right\rangle]}+{\frac{L\gamma^{2}}{2}\mathbb{E}_{\xi_{k},b_{k}}[\|P_{k+1}-P_{k}\|^{2}]}. (87)

[362] p: Plugging ( 81 ) and ( 83 ) into ( 87 ), we have

[363] table: 𝔼 ξ k , b k ​ [ f ⁡ ( W k + γ ​ P k + 1 − γ ​ Q k ) ] \displaystyle\mathbb{E}_{\xi_{k},b_{k}}[f(W_{k}+\gamma P_{k+1}-\gamma Q_{k})] (88) ≤ \displaystyle\leq f ⁡ ( W ¯ k ) − α ​ γ 2 ​ q max ​ ‖ ∇ f ​ ( W ¯ k ) ‖ M p ​ ( P k ) 2 + α ​ γ ​ σ 2 2 ​ ‖ G p ​ ( P k ) F p ​ ( P k ) ‖ ∞ 2 + Θ ⁡ ( γ ​ Δ ​ w min q min ) \displaystyle\ f(\bar{W}_{k})-\frac{\alpha\gamma}{2q_{\max}}\|\nabla f(\bar{W}_{k})\|^{2}_{M_{p}(P_{k})}+\frac{\alpha\gamma\sigma^{2}}{2}\left\|\frac{G_{p}(P_{k})}{\sqrt{F_{p}(P_{k})}}\right\|^{2}_{\infty}+{\Theta}\left(\frac{\gamma\Delta w_{\min}}{q_{\min}}\right) − ( γ 2 ​ α ​ q max − γ 2 ​ L ) ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k + α ⁡ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) − b k ‖ 2 ] + α 2 ​ γ 2 ​ L ​ q max 2 ​ σ 2 . \displaystyle\ -\left(\frac{\gamma}{2\alpha q_{\max}}-\gamma^{2}L\right)~\mathbb{E}_{\xi_{k},b_{k}}\left[\left\|P_{k+1}-P_{k}+\alpha(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot F_{p}(P_{k})-b_{k}\right\|^{2}\right]+\alpha^{2}\gamma^{2}Lq_{\max}^{2}\sigma^{2}. ≤ \displaystyle\leq f ⁡ ( W ¯ k ) − α ​ γ 2 ​ q max ​ ‖ ∇ f ​ ( W ¯ k ) ‖ M p ​ ( P k ) 2 + α ​ γ ​ σ 2 2 ​ ‖ G p ​ ( P k ) F p ​ ( P k ) ‖ ∞ 2 + α 2 ​ γ 2 ​ L ​ q max 2 ​ σ 2 + Θ ⁡ ( γ ​ Δ ​ w min q min ) \displaystyle\ f(\bar{W}_{k})-\frac{\alpha\gamma}{2q_{\max}}\|\nabla f(\bar{W}_{k})\|^{2}_{M_{p}(P_{k})}+\frac{\alpha\gamma\sigma^{2}}{2}\left\|\frac{G_{p}(P_{k})}{\sqrt{F_{p}(P_{k})}}\right\|^{2}_{\infty}+\alpha^{2}\gamma^{2}Lq_{\max}^{2}\sigma^{2}+{\Theta}\left(\frac{\gamma\Delta w_{\min}}{q_{\min}}\right)

[364] p: where the second inequality holds by α ≤ 1 2 ​ γ ​ L ​ q max \alpha\leq\frac{1}{2\gamma Lq_{\max}} . Now the proof of ( 52 ) is completed. ∎

[365] h4: E.3 Proof of Lemma E.2 : Descent of sequence W k W_{k}

[366] p: See E.2

[367] h6: Lemma E.2 .

[368] p: Recall the definition P ∗ ​ ( W , Q ) − Q = ( W ∗ − W ) / γ P^{*}(W,Q)-Q=(W^{*}-W)/\gamma , it holds that

[369] table: ‖ P ∗ ​ ( W k + 1 , Q k + 1 ) − Q k + 1 ‖ 2 = 1 γ 2 ​ ‖ W k + 1 − Proj 𝒲 ∗ ⁡ ( W k + 1 ) ‖ 2 ≤ 1 γ 2 ​ ‖ W k + 1 − Proj 𝒲 ∗ ⁡ ( W k ) ‖ 2 \displaystyle\ \|P^{*}(W_{k+1},Q_{k+1})-Q_{k+1}\|^{2}=\frac{1}{\gamma^{2}}\|W_{k+1}-\operatorname{Proj}_{{\mathcal{W}}^{*}}(W_{k+1})\|^{2}\leq\frac{1}{\gamma^{2}}\|W_{k+1}-\operatorname{Proj}_{{\mathcal{W}}^{*}}(W_{k})\|^{2} (89) = \displaystyle= 1 γ 2 ​ ‖ W k − Proj 𝒲 ∗ ⁡ ( W k ) ‖ 2 + 2 γ 2 ​ ⟨ W k − Proj 𝒲 ∗ ⁡ ( W k ) , W k + 1 − W k ⟩ + 1 γ 2 ​ ‖ W k + 1 − W k ‖ 2 \displaystyle\ \frac{1}{\gamma^{2}}\|W_{k}-\operatorname{Proj}_{{\mathcal{W}}^{*}}(W_{k})\|^{2}+\frac{2}{\gamma^{2}}\left\langle W_{k}-\operatorname{Proj}_{{\mathcal{W}}^{*}}(W_{k}),W_{k+1}-W_{k}\right\rangle+\frac{1}{\gamma^{2}}\|W_{k+1}-W_{k}\|^{2} = \displaystyle= ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 − 2 γ ​ ⟨ P ∗ ​ ( W k , Q k ) − Q k , W k + 1 − W k ⟩ + 1 γ 2 ​ ‖ W k + 1 − W k ‖ 2 \displaystyle\ \|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}-\frac{2}{\gamma}\left\langle P^{*}(W_{k},Q_{k})-Q_{k},W_{k+1}-W_{k}\right\rangle+\frac{1}{\gamma^{2}}\|W_{k+1}-W_{k}\|^{2}

[370] p: where the first inequality comes from the fact that Proj 𝒲 ∗ ⁡ ( W k + 1 ) \operatorname{Proj}_{{\mathcal{W}}^{*}}(W_{k+1}) is the closest point to W k + 1 W_{k+1} in 𝒲 ∗ {\mathcal{W}}^{*} . We bound the second term in the RHS of ( 89 ) by

[371] table: − 𝔼 b k ′ ​ [ 2 γ ​ ⟨ P ∗ ​ ( W k , Q k ) − Q k , W k + 1 − W k ⟩ ] \displaystyle\quad-\mathbb{E}_{b^{\prime}_{k}}\left[\frac{2}{\gamma}\langle P^{*}(W_{k},Q_{k})-Q_{k},W_{k+1}-W_{k}\rangle\right] (90) = − 2 γ ​ ⟨ P ∗ ​ ( W k , Q k ) − Q k , β ⁡ ( P k + 1 − Q k ) ⊙ F w ​ ( W k ) − β ​ | P k + 1 − Q k | ⊙ G w ​ ( W k ) ⟩ \displaystyle=-\frac{2}{\gamma}\langle P^{*}(W_{k},Q_{k})-Q_{k},\beta(P_{k+1}-Q_{k})\odot F_{w}(W_{k})-\beta|P_{k+1}-Q_{k}|\odot G_{w}(W_{k})\rangle = − 2 ​ β γ ​ ⟨ P ∗ ​ ( W k , Q k ) − Q k , ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) − | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) ⟩ \displaystyle=-\frac{2\beta}{\gamma}\langle P^{*}(W_{k},Q_{k})-Q_{k},(P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})\rangle − 2 ​ β γ ⟨ P ∗ ( W k , Q k ) − Q k , ( P k + 1 − Q k ) ⊙ F w ( W k ) − | P k + 1 − Q k | ⊙ G w ( W k ) \displaystyle\quad-\frac{2\beta}{\gamma}\langle P^{*}(W_{k},Q_{k})-Q_{k},(P_{k+1}-Q_{k})\odot F_{w}(W_{k})-|P_{k+1}-Q_{k}|\odot G_{w}(W_{k}) − ( ( P ∗ ( W k , Q k ) − Q k ) ⊙ F w ( W k ) − | P ∗ ( W k , Q k ) − Q k | ⊙ G w ( W k ) ) ⟩ . \displaystyle\qquad-((P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k}))\rangle.

[372] p: where the first equality holds because 𝔼 ⁡ [ b k ′ ] = 0 \mathbb{E}[b_{k}^{\prime}]=0 .

[373] p: The first term in the RHS of ( 90 ) is bounded by

[374] table: − 2 ​ β γ ​ ⟨ P ∗ ​ ( W k , Q k ) − Q k , ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) − | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) ⟩ \displaystyle\ -\frac{2\beta}{\gamma}\langle P^{*}(W_{k},Q_{k})-Q_{k},(P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})\rangle (91) = \displaystyle= − 2 ​ β γ ​ ⟨ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) , ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) − | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) F w ​ ( W k ) ⟩ \displaystyle\ -\frac{2\beta}{\gamma}\left\langle(P^{*}(W_{k},Q_{k})-Q_{k})\odot\sqrt{F_{w}(W_{k})},\frac{(P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})}{\sqrt{F_{w}(W_{k})}}\right\rangle = ( a ) \displaystyle\overset{(a)}{=} − β γ ​ ‖ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) ‖ 2 + β γ ​ ‖ | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) F w ​ ( W k ) ‖ 2 \displaystyle\ -\frac{\beta}{\gamma}\|(P^{*}(W_{k},Q_{k})-Q_{k})\odot\sqrt{F_{w}(W_{k})}\|^{2}+\frac{\beta}{\gamma}\left\||P^{*}(W_{k},Q_{k})-Q_{k}|\odot\frac{G_{w}(W_{k})}{\sqrt{F_{w}(W_{k})}}\right\|^{2} − β γ ​ ‖ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) + | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) F w ​ ( W k ) ‖ 2 \displaystyle\ -\frac{\beta}{\gamma}\left\|(P^{*}(W_{k},Q_{k})-Q_{k})\odot\sqrt{F_{w}(W_{k})}+|P^{*}(W_{k},Q_{k})-Q_{k}|\odot\frac{G_{w}(W_{k})}{\sqrt{F_{w}(W_{k})}}\right\|^{2} ≤ ( b ) \displaystyle\overset{(b)}{\leq} − β γ ​ q max ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ M w ​ ( W k ) 2 − β γ ​ ‖ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) + | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) F w ​ ( W k ) ‖ 2 \displaystyle\ -\frac{\beta}{\gamma q_{\max}}\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}_{M_{w}(W_{k})}-\frac{\beta}{\gamma}\left\|(P^{*}(W_{k},Q_{k})-Q_{k})\odot\sqrt{F_{w}(W_{k})}+|P^{*}(W_{k},Q_{k})-Q_{k}|\odot\frac{G_{w}(W_{k})}{\sqrt{F_{w}(W_{k})}}\right\|^{2} ≤ \displaystyle\leq − β γ ​ q max ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ M w ​ ( W k ) 2 − β γ ​ q max ​ ‖ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) − | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) ‖ 2 \displaystyle\ -\frac{\beta}{\gamma q_{\max}}\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}_{M_{w}(W_{k})}-\frac{\beta}{\gamma q_{\max}}\left\|(P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})\right\|^{2}

[375] p: where ( a ) (a) leverages 2 ​ ⟨ U , V ⟩ = ‖ U ‖ 2 − ‖ V ‖ 2 − ‖ U − V ‖ 2 2\left\langle U,V\right\rangle=\|U\|^{2}-\|V\|^{2}-\|U-V\|^{2} for any U , V ∈ ℝ D U,V\in{\mathbb{R}}^{D} , ( b ) (b) is achieved by

[376] table: − β 2 ​ ‖ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) ‖ 2 + β 2 ​ ‖ | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) F w ​ ( W k ) ‖ 2 \displaystyle\ -\frac{\beta}{2}\|(P^{*}(W_{k},Q_{k})-Q_{k})\odot\sqrt{F_{w}(W_{k})}\|^{2}+\frac{\beta}{2}\left\||P^{*}(W_{k},Q_{k})-Q_{k}|\odot\frac{G_{w}(W_{k})}{\sqrt{F_{w}(W_{k})}}\right\|^{2} (92) = \displaystyle= − β 2 ∑ d ∈ [ D ] ( [ P ∗ ( W k , Q k ) − Q k ] d 2 ( [ F w ( W k ) ] d − [ G w ​ ( W k ) ] d 2 [ F w ​ ( W k ) ] d ) ) \displaystyle\ -\frac{\beta}{2}\sum_{d\in[D]}\left([P^{*}(W_{k},Q_{k})-Q_{k}]_{d}^{2}\left([F_{w}(W_{k})]_{d}-\frac{[G_{w}(W_{k})]^{2}_{d}}{[F_{w}(W_{k})]_{d}}\right)\right) = \displaystyle= − β 2 ∑ d ∈ [ D ] ( [ P ∗ ( W k , Q k ) − Q k ] d 2 ( [ F w ​ ( W k ) ] d 2 − [ G w ​ ( W k ) ] d 2 [ F w ​ ( W k ) ] d ) ) \displaystyle\ -\frac{\beta}{2}\sum_{d\in[D]}\left([P^{*}(W_{k},Q_{k})-Q_{k}]_{d}^{2}\left(\frac{[F_{w}(W_{k})]^{2}_{d}-[G_{w}(W_{k})]^{2}_{d}}{[F_{w}(W_{k})]_{d}}\right)\right) ≤ \displaystyle\leq − β 2 ​ q max ∑ d ∈ [ D ] ( [ P ∗ ( W k , Q k ) − Q k ] d 2 ( [ F w ( W k ) ] d 2 − [ G w ( W k ) ] d 2 ) ) = − β 2 ​ q max ∥ P ∗ ( W k , Q k ) − Q k ∥ M w ​ ( W k ) 2 . \displaystyle\ -\frac{\beta}{2q_{\max}}\sum_{d\in[D]}\left([P^{*}(W_{k},Q_{k})-Q_{k}]_{d}^{2}\left([F_{w}(W_{k})]_{d}^{2}-[G_{w}(W_{k})]^{2}_{d}\right)\right)=\ -\frac{\beta}{2q_{\max}}\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}_{M_{w}(W_{k})}.

[377] p: The second term in the RHS of ( 90 ) follows the Lipschitz continuity of analog update (see Lemma A.2 )

[378] table: − 2 ​ β γ ⟨ P ∗ ( W k , Q k ) − Q k , ( P k + 1 − Q k ) ⊙ F w ( W k ) − | P k + 1 − Q k | ⊙ G w ( W k ) \displaystyle-\frac{2\beta}{\gamma}\langle P^{*}(W_{k},Q_{k})-Q_{k},(P_{k+1}-Q_{k})\odot F_{w}(W_{k})-|P_{k+1}-Q_{k}|\odot G_{w}(W_{k}) (93) − ( ( P ∗ ( W k , Q k ) − Q k ) ⊙ F w ( W k ) − | P ∗ ( W k , Q k ) − Q k | ⊙ G w ( W k ) ) ⟩ \displaystyle\qquad-((P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k}))\rangle = 2 ​ β γ ⟨ P ∗ ( W k , Q k ) − Q k , − ( P k + 1 − Q k ) ⊙ F w ( W k ) + | P k + 1 − Q k | ⊙ G w ( W k ) \displaystyle=\frac{2\beta}{\gamma}\langle P^{*}(W_{k},Q_{k})-Q_{k},-(P_{k+1}-Q_{k})\odot F_{w}(W_{k})+|P_{k+1}-Q_{k}|\odot G_{w}(W_{k}) + ( ( P ∗ ( W k , Q k ) − Q k ) ⊙ F w ( W k ) − | P ∗ ( W k , Q k ) − Q k | ⊙ G w ( W k ) ) ⟩ \displaystyle\qquad+((P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k}))\rangle ≤ β 2 ​ γ ​ q max ∥ P ∗ ( W k , Q k ) − Q k ∥ M w ​ ( W k ) 2 + 2 ​ β ​ q max γ × ∥ ( P k + 1 − Q k ) ⊙ F w ( W k ) \displaystyle\leq\frac{\beta}{2\gamma q_{\max}}\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}_{M_{w}(W_{k})}+\frac{2\beta q_{\max}}{\gamma}\times\Bigl\|(P_{k+1}-Q_{k})\odot F_{w}(W_{k}) − | P k + 1 − Q k | ⊙ G w ( W k ) − ( ( P ∗ ( W k , Q k ) − Q k ) ⊙ F w ( W k ) − | P ∗ ( W k , Q k ) − Q k | ⊙ G w ( W k ) ) ∥ M w ​ ( W k ) † 2 . \displaystyle\quad-|P_{k+1}-Q_{k}|\odot G_{w}(W_{k})-\bigl((P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})\bigr)\Bigr\|^{2}_{M_{w}(W_{k})^{\dagger}}. ≤ β 2 ​ γ ​ q max ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ M w ​ ( W k ) 2 + 2 ​ β ​ q max 3 γ ​ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ M w ​ ( W k ) † 2 . \displaystyle\leq\ \frac{\beta}{2\gamma q_{\max}}\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}_{M_{w}(W_{k})}+\frac{2\beta q_{\max}^{3}}{\gamma}\left\|P_{k+1}-P^{*}(W_{k},Q_{k})\right\|^{2}_{M_{w}(W_{k})^{\dagger}}.

[379] p: Substituting ( 91 ) and ( 93 ) into ( 90 ), we bound the second term in the RHS of ( 89 ) by

[380] table: − 2 γ ​ 𝔼 b k ′ ​ [ ⟨ P ∗ ​ ( W k , Q k ) − Q k , W k + 1 − W k ⟩ ] \displaystyle\ -\frac{2}{\gamma}\mathbb{E}_{b^{\prime}_{k}}\left[\left\langle P^{*}(W_{k},Q_{k})-Q_{k},W_{k+1}-W_{k}\right\rangle\right] (94) ≤ \displaystyle\leq − β 2 ​ γ ​ q max ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ M w ​ ( W k ) 2 − β γ ​ q max ​ ‖ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) − | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) ‖ 2 \displaystyle\ -\frac{\beta}{2\gamma q_{\max}}\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}_{M_{w}(W_{k})}-\frac{\beta}{\gamma q_{\max}}\left\|(P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})\right\|^{2} + 2 ​ β ​ q max 3 γ ​ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ M w ​ ( W k ) † 2 . \displaystyle\ +\frac{2\beta q_{\max}^{3}}{\gamma}\left\|P_{k+1}-P^{*}(W_{k},Q_{k})\right\|^{2}_{M_{w}(W_{k})^{\dagger}}.

[381] p: The third term in the RHS of ( 89 ) follows the Lipschitz continuity of the analog update (Lemma A.2 )

[382] table: 1 γ 2 ​ 𝔼 b k ′ ​ [ ‖ W k + 1 − W k ‖ 2 ] = β 2 γ 2 ​ ‖ ( P k + 1 − Q k ) ⊙ F w ​ ( W k ) − | P k + 1 − Q k | ⊙ G w ​ ( W k ) ‖ 2 + Θ ⁡ ( β ​ Δ ​ w min γ 2 ) \displaystyle\ \frac{1}{\gamma^{2}}\mathbb{E}_{b^{\prime}_{k}}\left[\|W_{k+1}-W_{k}\|^{2}\right]=\frac{\beta^{2}}{\gamma^{2}}\|(P_{k+1}-Q_{k})\odot F_{w}(W_{k})-|P_{k+1}-Q_{k}|\odot G_{w}(W_{k})\|^{2}+{\Theta}\left(\frac{\beta\Delta w_{\min}}{\gamma^{2}}\right) ≤ \displaystyle\leq 2 ​ β 2 γ 2 ​ ‖ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) − | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) ‖ 2 \displaystyle\ \frac{2\beta^{2}}{\gamma^{2}}\|(P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})\|^{2} + 2 ​ β 2 γ 2 | ( P k + 1 − Q k ) ⊙ F w ​ ( W k ) − | P k + 1 − Q k | ⊙ G w ​ ( W k ) \displaystyle+\frac{2\beta^{2}}{\gamma^{2}}\bigl\|(P_{k+1}-Q_{k})\odot F_{w}(W_{k})-|P_{k+1}-Q_{k}|\odot G_{w}(W_{k}) − ( ( P ∗ ( W k , Q k ) − Q k ) ⊙ F w ( W k ) − | P ∗ ( W k , Q k ) − Q k | ⊙ G w ( W k ) ) ∥ 2 + Θ ( β ​ Δ ​ w min γ 2 ) \displaystyle\qquad-\bigl((P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})\bigr)\bigr\|^{2}+{\Theta}\left(\frac{\beta\Delta w_{\min}}{\gamma^{2}}\right) ≤ \displaystyle\leq 2 ​ β 2 γ 2 ​ ‖ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) − | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) ‖ 2 + 2 ​ β 2 γ 2 ​ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 \displaystyle\ \frac{2\beta^{2}}{\gamma^{2}}\|(P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})\|^{2}+\frac{2\beta^{2}}{\gamma^{2}}\|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2} + Θ ⁡ ( β ​ Δ ​ w min γ 2 ) \displaystyle~~+{\Theta}\left(\frac{\beta\Delta w_{\min}}{\gamma^{2}}\right) (95)

[383] p: Plugging ( 94 ) and ( 95 ) into ( 89 ) yields

[384] table: 𝔼 b k ′ ​ [ ‖ P ∗ ​ ( W k + 1 , Q k + 1 ) − Q k + 1 ‖ 2 ] ≤ \displaystyle\mathbb{E}_{b^{\prime}_{k}}\left[\|P^{*}(W_{k+1},Q_{k+1})-Q_{k+1}\|^{2}\right]\leq ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 − β 2 ​ γ ​ q max ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ M w ​ ( W k ) 2 + Θ ⁡ ( β ​ Δ ​ w min γ 2 ) \displaystyle\ \|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}-\frac{\beta}{2\gamma q_{\max}}\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}_{M_{w}(W_{k})}+{\Theta}\left(\frac{\beta\Delta w_{\min}}{\gamma^{2}}\right) − ( β γ ​ q max − 2 ​ β 2 γ 2 ) ​ ‖ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) − | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) ‖ 2 \displaystyle\ -\left(\frac{\beta}{\gamma q_{\max}}-\frac{2\beta^{2}}{\gamma^{2}}\right)\left\|(P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})\right\|^{2} + 2 ​ β ​ q max 3 γ ​ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ M w ​ ( W k ) † 2 + 2 ​ β 2 γ 2 ​ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 . \displaystyle\ +\frac{2\beta q_{\max}^{3}}{\gamma}\left\|P_{k+1}-P^{*}(W_{k},Q_{k})\right\|^{2}_{M_{w}(W_{k})^{\dagger}}+\frac{2\beta^{2}}{\gamma^{2}}\|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2}. (96)

[385] p: Notice the learning rate β \beta is chosen as β ≤ γ 2 ​ q max \beta\leq\frac{\gamma}{2q_{\max}} , we have

[386] table: 𝔼 b k ′ ​ [ ‖ P ∗ ​ ( W k + 1 , Q k + 1 ) − Q k + 1 ‖ 2 ] ≤ \displaystyle\mathbb{E}_{b^{\prime}_{k}}\left[\|P^{*}(W_{k+1},Q_{k+1})-Q_{k+1}\|^{2}\right]\leq ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ 2 − β 2 ​ γ ​ q max ​ ‖ P ∗ ​ ( W k , Q k ) − Q k ‖ M w ​ ( W k ) 2 + Θ ⁡ ( Δ ​ w min γ ​ q max ) \displaystyle\ \|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}-\frac{\beta}{2\gamma q_{\max}}\|P^{*}(W_{k},Q_{k})-Q_{k}\|^{2}_{M_{w}(W_{k})}+{\Theta}\left(\frac{\Delta w_{\min}}{\gamma q_{\max}}\right) − β 2 ​ γ ​ q max ​ ‖ ( P ∗ ​ ( W k , Q k ) − Q k ) ⊙ F w ​ ( W k ) − | P ∗ ​ ( W k , Q k ) − Q k | ⊙ G w ​ ( W k ) ‖ 2 \displaystyle\ -\frac{\beta}{2\gamma q_{\max}}\left\|(P^{*}(W_{k},Q_{k})-Q_{k})\odot F_{w}(W_{k})-|P^{*}(W_{k},Q_{k})-Q_{k}|\odot G_{w}(W_{k})\right\|^{2} + 2 ​ β ​ q max 3 γ ​ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ M w ​ ( W k ) † 2 + 2 ​ β 2 γ 2 ​ ‖ P k + 1 − P ∗ ​ ( W k , Q k ) ‖ 2 \displaystyle\ +\frac{2\beta q_{\max}^{3}}{\gamma}\left\|P_{k+1}-P^{*}(W_{k},Q_{k})\right\|^{2}_{M_{w}(W_{k})^{\dagger}}+\frac{2\beta^{2}}{\gamma^{2}}\|P_{k+1}-P^{*}(W_{k},Q_{k})\|^{2} (97)

[387] p: which completes the proof. ∎

[388] h4: E.4 Proof of Lemma E.3 : Descent of accumulated asymmetric sequence φ ⁡ ( P k ) \varphi(P_{k})

[389] p: In this section, we formally define the accumulated asymmetric function φ ⁡ ( P ) : ℝ D → ℝ D \varphi(P):{\mathbb{R}}^{D}\to{\mathbb{R}}^{D} element-wise defined by

[390] table: [ φ ⁡ ( P ) ] d := ∫ τ i min [ P ] d [ G p ​ ( P ) ] d ​ d ​ [ P ] d . \displaystyle[\varphi(P)]_{d}:=\int_{\tau_{i}^{\min}}^{[P]_{d}}~[G_{p}(P)]_{d}~{\mathrm{d}[P]_{d}}. (98)

[391] p: See E.3

[392] h6: Lemma E.3 .

[393] p: The Lipschitz continuity of the generic response function ensures that the accumulated asymmetric function φ ⁡ ( P ) \varphi(P) is L L -smooth.

[394] table: 𝔼 ξ k , b k ​ [ φ ⁡ ( P k + 1 ) ] ≤ φ ⁡ ( P k ) + 𝔼 ξ k , b k ​ [ ⟨ G p ​ ( P k ) , P k + 1 − P k ⟩ ] ⏟ ( a ) + L 2 ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k ‖ 2 ] ⏟ ( b ) \displaystyle\ \mathbb{E}_{\xi_{k},b_{k}}[\varphi(P_{k+1})]\leq\varphi(P_{k})+\underbrace{\mathbb{E}_{\xi_{k},b_{k}}[\left\langle G_{p}(P_{k}),P_{k+1}-P_{k}\right\rangle]}_{(a)}+\underbrace{\frac{L}{2}\mathbb{E}_{\xi_{k},b_{k}}[\|P_{k+1}-P_{k}\|^{2}]}_{(b)} (99)

[395] p: Next, we will handle each term in the RHS of ( 99 ) separately.

[396] p: Bound of the second term (a).

[397] table: 𝔼 ξ k , b k ​ [ ⟨ G p ​ ( P k ) , P k + 1 − P k ⟩ ] \displaystyle\mathbb{E}_{\xi_{k},b_{k}}\big[\langle G_{p}(P_{k}),P_{k+1}-P_{k}\rangle\big] = \displaystyle= 𝔼 ξ k [ ⟨ G p ( P k ) , − α ∇ f ( W ¯ k , ξ k ) ⊙ F p ( P k ) − α | ∇ f ( W ¯ k , ξ k ) | ⊙ G p ( P k ) ⟩ ] \displaystyle\mathbb{E}_{\xi_{k}}\big[\langle G_{p}(P_{k}),-\alpha\nabla f(\bar{W}_{k},\xi_{k})\odot F_{p}(P_{k})-\alpha|\nabla f(\bar{W}_{k},\xi_{k})|\odot G_{p}(P_{k})\rangle\big] = \displaystyle= ⟨ G p ( P k ) , − α ∇ f ( W ¯ k ) ⊙ F p ( P k ) − α 𝔼 ξ k [ | ∇ f ( W ¯ k , ξ k ) | ] ⊙ G p ( P k ) ⟩ \displaystyle\langle G_{p}(P_{k}),-\alpha\nabla f(\bar{W}_{k})\odot F_{p}(P_{k})-\alpha\mathbb{E}_{\xi_{k}}[|\nabla f(\bar{W}_{k},\xi_{k})|]\odot G_{p}(P_{k})\rangle = \displaystyle= ⟨ α ​ 𝔼 ξ k ​ [ | ∇ f ​ ( W ¯ k , ξ k ) | ] ⊙ G p ( P k ) , − α 𝔼 ξ k ​ [ | ∇ f ​ ( W ¯ k , ξ k ) | ] ∇ f ( W ¯ k ) ⊙ F p ( P k ) − α ​ 𝔼 ξ k ​ [ | ∇ f ​ ( W ¯ k , ξ k ) | ] ⊙ G p ( P k ) ⟩ \displaystyle\Big\langle\sqrt{\alpha\mathbb{E}_{\xi_{k}}[|\nabla f(\bar{W}_{k},\xi_{k})|]}\odot G_{p}(P_{k}),-\frac{\sqrt{\alpha}}{\sqrt{\mathbb{E}_{\xi_{k}}[|\nabla f(\bar{W}_{k},\xi_{k})|]}}\nabla f(\bar{W}_{k})\odot F_{p}(P_{k})-\sqrt{\alpha\mathbb{E}_{\xi_{k}}[|\nabla f(\bar{W}_{k},\xi_{k})|]}\odot G_{p}(P_{k})\Big\rangle = ( a ) \displaystyle\overset{(a)}{=} − 1 2 ∥ α ​ 𝔼 ξ k ​ [ | ∇ f ​ ( W ¯ k , ξ k ) | ] ⊙ G p ( P k ) ∥ 2 + 1 2 ∥ α 𝔼 ξ k ​ [ | ∇ f ​ ( W ¯ k , ξ k ) | ] ∇ f ( W ¯ k ) ⊙ F p ( P k ) ∥ 2 \displaystyle-\frac{1}{2}\Big\|\sqrt{\alpha\mathbb{E}_{\xi_{k}}[|\nabla f(\bar{W}_{k},\xi_{k})|]}\odot G_{p}(P_{k})\Big\|^{2}+\frac{1}{2}\Big\|\frac{\sqrt{\alpha}}{\sqrt{\mathbb{E}_{\xi_{k}}[|\nabla f(\bar{W}_{k},\xi_{k})|]}}\nabla f(\bar{W}_{k})\odot F_{p}(P_{k})\Big\|^{2} − 1 2 ∥ α 𝔼 ξ k ​ [ | ∇ f ​ ( W ¯ k , ξ k ) | ] ∇ f ( W ¯ k ) ⊙ F p ( P k ) + α ​ 𝔼 ξ k ​ [ | ∇ f ​ ( W ¯ k , ξ k ) | ] ⊙ G p ( P k ) ∥ 2 \displaystyle\hskip 28.45274pt-\frac{1}{2}\Big\|\frac{\sqrt{\alpha}}{\sqrt{\mathbb{E}_{\xi_{k}}[|\nabla f(\bar{W}_{k},\xi_{k})|]}}\nabla f(\bar{W}_{k})\odot F_{p}(P_{k})+\sqrt{\alpha\mathbb{E}_{\xi_{k}}[|\nabla f(\bar{W}_{k},\xi_{k})|]}\odot G_{p}(P_{k})\Big\|^{2} ≤ \displaystyle\leq − α 2 ∑ d ∈ [ D ] 𝔼 ξ k [ [ | ∇ f ( W ¯ k , ξ k ) | ] d ] [ G p ( P k ) ] d 2 + α 2 ∑ d ∈ [ D ] [ | ∇ f ​ ( W ¯ k ) | ] d 2 𝔼 ξ k ​ [ [ | ∇ f ​ ( W ¯ k , ξ k ) | ] d ] [ F p ( P k ) ] d 2 \displaystyle-\frac{\alpha}{2}\sum_{d\in[D]}\mathbb{E}_{\xi_{k}}\big[[|\nabla f(\bar{W}_{k},\xi_{k})|]_{d}\big][G_{p}(P_{k})]_{d}^{2}+\frac{\alpha}{2}\sum_{d\in[D]}\frac{[|\nabla f(\bar{W}_{k})|]_{d}^{2}}{\mathbb{E}_{\xi_{k}}\big[[|\nabla f(\bar{W}_{k},\xi_{k})|]_{d}\big]}[F_{p}(P_{k})]_{d}^{2} ≤ ( b ) \displaystyle\overset{(b)}{\leq} − α ​ C ⋆ 2 ​ ‖ G p ​ ( P k ) ‖ 2 + α 2 ​ C ⋆ ​ ‖ ∇ f ​ ( W ¯ k ) ⊙ F p ​ ( P k ) ‖ 2 \displaystyle\ -\frac{\alpha C_{\star}}{2}\|G_{p}(P_{k})\|^{2}+\frac{\alpha}{2C_{\star}}\|\nabla f(\bar{W}_{k})\odot F_{p}(P_{k})\|^{2} ≤ \displaystyle\leq − α ​ C ⋆ 2 ​ ‖ G p ​ ( P k ) ‖ 2 + α ​ q max 2 2 ​ C ⋆ ​ ‖ ∇ f ​ ( W ¯ k ) ‖ 2 . \displaystyle\ -\frac{\alpha C_{\star}}{2}\|G_{p}(P_{k})\|^{2}+\frac{\alpha q_{\max}^{2}}{2C_{\star}}\|\nabla f(\bar{W}_{k})\|^{2}. (100)

[398] p: The equality (a) holds by ⟨ A , − B ⟩ = − ‖ A ‖ 2 2 − ‖ B ‖ 2 2 + ‖ A − B ‖ 2 2 \left\langle A,-B\right\rangle=-\frac{\|A\|^{2}}{2}-\frac{\|B\|^{2}}{2}+\frac{\|A-B\|^{2}}{2} , the equality (b) holds by Assumption 3.6 .

[399] p: Bound the third term (b). Follow ( 83 ), we have:

[400] table: L 2 ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k ‖ 2 ] \displaystyle\frac{L}{2}\mathbb{E}_{\xi_{k},b_{k}}[\|P_{k+1}-P_{k}\|^{2}] ≤ \displaystyle\leq L ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k + α ⁡ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) − b k ‖ 2 ] + α 2 ​ L ​ q max 2 ​ σ 2 + Θ ⁡ ( α ​ L ​ Δ ​ w min ) . \displaystyle\ L\mathbb{E}_{\xi_{k},b_{k}}\left[\left\|P_{k+1}-P_{k}+\alpha(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot F_{p}(P_{k})-b_{k}\right\|^{2}\right]+\alpha^{2}Lq_{\max}^{2}\sigma^{2}+{\Theta}\left(\alpha L\Delta w_{\min}\right). (101)

[401] p: Substituting ( 100 ) and ( 101 ) into ( 99 ) and note that α ≤ 1 2 ​ γ ​ L ​ q max \alpha\leq\frac{1}{2\gamma Lq_{\max}} , we have:

[402] table: 𝔼 ξ k , b k ​ [ φ ⁡ ( P k + 1 ) ] ≤ \displaystyle\mathbb{E}_{\xi_{k},b_{k}}[\varphi(P_{k+1})]\leq φ ⁡ ( P k ) − α ​ C ⋆ 2 ​ ‖ G p ​ ( P k ) ‖ 2 + α 2 ​ L ​ q max 2 ​ σ 2 + α ​ q max 2 2 ​ C ⋆ ​ ‖ ∇ f ​ ( W ¯ k ) ‖ 2 + Θ ⁡ ( Δ ​ w min γ ​ q max ) \displaystyle\varphi(P_{k})-\frac{\alpha C_{\star}}{2}\|G_{p}(P_{k})\|^{2}+\alpha^{2}Lq_{\max}^{2}\sigma^{2}+\frac{\alpha q_{\max}^{2}}{2C_{\star}}\|\nabla f(\bar{W}_{k})\|^{2}+{\Theta}\left(\frac{\Delta w_{\min}}{\gamma q_{\max}}\right) + L ​ 𝔼 ξ k , b k ​ [ ‖ P k + 1 − P k + α ⁡ ( ∇ f ​ ( W ¯ k , ξ k ) − ∇ f ​ ( W ¯ k ) ) ⊙ F p ​ ( P k ) − b k ‖ 2 ] . \displaystyle\ +L\mathbb{E}_{\xi_{k},b_{k}}\left[\left\|P_{k+1}-P_{k}+\alpha(\nabla f(\bar{W}_{k};\xi_{k})-\nabla f(\bar{W}_{k}))\odot F_{p}(P_{k})-b_{k}\right\|^{2}\right]. (102)

[403] p: ∎

[404] h3: Appendix F Additional Experiments and Experimental Setups

[405] h4: F.1 Details of implementation for Figure 1 and Figure 2

[406] p: For a linear device with fixed conductance bounds τ min \tau_{\min} and τ max \tau_{\max} , a minimal update size Δ ​ w min \Delta w_{\min} , a controlled asymmetry between potentiation and depression, and realistic device-to-device variations in these quantities, the effective up/down slope parameters can be summarized by two coefficients, α + \alpha_{+} and α − \alpha_{-} . The corresponding linear response functions are

[407] table: q + ​ ( w ) = α + ​ ( 1 − w τ max ) , q − ​ ( w ) = α − ​ ( 1 + w τ min ) , \displaystyle q_{+}(w)=\alpha_{+}\left(1-\frac{w}{\tau_{\max}}\right),\qquad q_{-}(w)=\alpha_{-}\left(1+\frac{w}{\tau_{\min}}\right), (103)

[408] p: where α + , α − , τ max , τ min ∈ ℝ + \alpha_{+},\alpha_{-},\tau_{\max},\tau_{\min}\in\mathbb{R}_{+} are device-specific parameters.

[409] p: Under this model, there exists a unique SP at which the average positive and negative update sizes become equal; this weight is the SP w ⋄ w^{\diamond} . The ground truth value for SP of the device can be computed as :

[410] table: w ⋄ = α + − α − α + τ max − α − τ min = 2 ​ ρ γ + ρ τ max − γ − ρ τ min \displaystyle w^{\diamond}=\frac{\alpha_{+}-\alpha_{-}}{\frac{\alpha_{+}}{\tau_{\max}}-\frac{\alpha_{-}}{\tau_{\min}}}=\frac{2\rho}{\frac{\gamma+\rho}{\tau_{\max}}-\frac{\gamma-\rho}{\tau_{\min}}} (104)

[411] p: where γ = e σ d2d ​ ξ 1 \gamma=e^{\sigma_{\mathrm{d2d}}\xi_{1}} and ρ = σ ± ​ ξ 2 \rho=\sigma_{\pm}\xi_{2} , such that σ d2d \sigma_{\mathrm{d2d}} controls the device-to-device variation of the slope magnitude, while σ ± \sigma_{\pm} characterizes the device-to-device variation of the slope asymmetry between the up and down updates Rasch et al. (2024) .

[412] figure: Table 3: Hyperparameters for TT-v2, AGAD, and E-RIDER used in the analog training runs for Table 1 . Hyperparameter TT-v2 AGAD E-RIDER Units in mini-batch \ True True Transfer frequency ( transfer_every ) 1.0 1.0 1.0 Transfer columns ( transfer_columns ) True True True Self-transfer ( no_self_transfer ) True True True Reads per transfer ( n_reads_per_transfer ) 1 1 1 Input chopping ( in_chop_prob ) \ 0.1 0.05 Input chopper random ( in_chop_random ) \ False False Output chopping ( out_chop_prob ) \ 0.0 0.0 Fast learning rate ( fast_lr ) 0.005 0.01 0.5 Scale fast LR ( scale_fast_lr ) \ False False Transfer learning rate ( transfer_lr ) 0.005 0.2 0.05 Scale transfer LR ( scale_transfer_lr ) True True False Auto granularity ( auto_granularity ) \ 1000 1000 Auto scale ( auto_scale ) \ False False Auto momentum ( auto_momentum ) \ 0.99 0.99 Momentum ( momentum ) 0.1 0.0 0.0 Forget buffer ( forget_buffer ) True True True Tail weighting ( tail_weightening ) \ 5.0 5.0 Threshold scale ( thres_scale ) 0.8 \ \ Gamma ( gamma ) \ \ 0.1

[413] p: In practice, however, the SP of an analog device is usually determined experimentally by applying alternating positive and negative update pulses until the weight converges. We denote by r ⁡ ( N ) r(N) the SP estimated in this way after N N alternating pulses. To study how well this procedure recovers the true SP, we run simulations on the same 512 × 512 512\times 512 array with different pulse budgets N ∈ { 500 , 1000 , 2000 , 4000 , 8000 } N\in\{500,1000,2000,4000,8000\} , using a SoftBounds-based RPU preset with 2000 states. Figure 1(a) shows the empirical offsets of the SP mean and standard deviation over the 512 × 512 512\times 512 array, defined as the ground-truth statistics minus the corresponding estimated statistics. Here, the estimated SP statistics are computed by first estimating the SP for each array element, and then taking the mean and standard deviation across the 512 × 512 512\times 512 per-element SP estimates. As N N increases, the distribution of r ⁡ ( N ) r(N) gradually moves towards and eventually almost coincides with the ground-truth distribution of w ⋄ w^{\diamond} . For smaller pulse counts, however, both the mean and the standard deviation of r r can deviate significantly from those of w ⋄ w^{\diamond} . We model this mismatch element-wise using the following stochastic offset model:

[414] table: r = w ⋄ + μ r + σ r ​ ξ , ξ ∼ 𝒩 ⁡ ( 0 , 1 ) , {r}=w^{\diamond}+\mu_{r}+\sigma_{r}\xi,\qquad\xi\sim\mathcal{N}(0,1), (105)

[415] p: where μ r \mu_{r} captures the systematic offsets between the means of the two distributions and σ r \sigma_{r} accounts for the variance offsets introduced by using a finite number of pulses. The combined term o r = μ r + σ r ​ ξ o_{r}=\mu_{r}+\sigma_{r}\xi represents the residual offset on the reference device after SP subtraction. Our experiments in Figures 1(a) demonstrate that when the number of alternating pulses is not sufficiently large, this offset o r o_{r} introduces a non-negligible error in the estimated SP and the subsequent training. This effect is clearly visible in Figure 2 , where we train a LeNet-5(MNIST) with TT-v1 using SPs estimated from different numbers of pulses: smaller N N leads to significant degradation and even failure to converge.

[416] p: Furthermore, the pulse cost required for accurate SP estimation increases as the device update granularity Δ ​ w min \Delta w_{\min} improves. In Figure 1(b) , we sweep Δ ​ w min \Delta w_{\min} from 5 × 10 − 3 5\times 10^{-3} down to 1.6 × 10 − 6 1.6\times 10^{-6} and, for each setting, estimate the SP using alternating pulses with a discrete pulse-budget schedule N ∈ { 200,500 , 10 3 , 2 × 10 3 , … , 8.192 × 10 6 } N\in\{200,500,10^{3},2\times 10^{3},\ldots,8.192\times 10^{6}\} . We then report the smallest N N such that the relative error of the estimated SP mean is within 1 % 1\% of the ground-truth mean. The results show that higher-precision devices require substantially more pulses to reach the same accuracy target. Consequently, determining the SP by alternating pulses exhibits an inherent trade-off between pulse overhead and accuracy.

[417] h4: F.2 Hyperparameter settings for Tables 1 and 2

[418] p: We report the hyperparameter settings used in our MNIST experiments with fully analog LeNet-5 and FCN models and the IO/analog readout noise configuration used in both MNIST and CIFAR 100 tasks. We use a fully analog LeNet-5–style CNN with two 5 × 5 5\times 5 convolution layers with 16 and 32 channels and two analog fully connected layers of sizes 512 and 128. The network uses tanh \tanh activations in the hidden layers. For the fully connected network, we set the input dimension of 784, two hidden layers of sizes 256 and 128, and a 10-class output layer. The model uses sigmoid activations in the hidden layers. For LeNet-5, we use a batch size of 8, while for the FCN we use a batch size of 10.

[419] figure: Table 4: Hyperparameters for baseline algorithms and E-RIDER used in the CIFAR-100 fine-tuning experiments. Category TT-v2 AGAD E-RIDER Global learning rate ( lr ) 0.15 0.15 0.2 Fast learning rate ( fast_lr ) 0.01 0.01 0.1 Transfer learning rate ( transfer_lr ) 0.5 0.5 0.01 Scale transfer LR ( scale_transfer_lr ) True True True Momentum ( momentum ) 0.1 0.0 0.0 Threshold scale ( thres_scale ) 1.0 \ \ Input chopping ( in_chop_prob ) \ 0.1 0.05 Output chopping ( out_chop_prob ) \ 0.0 0.0 Auto granularity ( auto_granularity ) \ 1000 1000 Gamma ( gamma ) \ \ 0.1

[420] figure: Table 5: Hyperparameters for TT-v2, AGAD, and E-RIDER used in the analog training runs for Table 2 . Category TT-v2 AGAD E-RIDER Input chopping ( in_chop_prob ) \ 0.1 0.05 Input chopper random ( in_chop_random ) \ False False Output chopping ( out_chop_prob ) \ 0.0 0.0 Fast learning rate ( fast_lr ) 0.03 0.05 0.5 Scale fast LR ( scale_fast_lr ) \ False False Transfer learning rate ( transfer_lr ) 0.01 0.3 0.05 Scale transfer LR ( scale_transfer_lr ) True True False Threshold scale ( thres_scale ) 0.8 \ \ Gamma ( gamma ) \ \ 0.1

[421] figure: Table 6: IO and analog readout noise settings for the forward, backward, and transfer-forward passes. Parameter Forward Backward Transfer-forward MV type ONE_PASS ONE_PASS ONE_PASS Noise management ABS_MAX ABS_MAX NONE Bound management ITERATIVE ITERATIVE NONE Input bound ( inp_bound ) 1.0 1.0 1.0 Input resolution ( inp_res ) 0.0079365 0.0079365 0.0079365 Input noise ( inp_noise ) 0.0 0.0 0.0 Output bound ( out_bound ) 12.0 12.0 12.0 Output resolution ( out_res ) 0.0019608 0.0019608 0.0019608 Output noise ( out_noise ) 0.06 0.06 0.06 Input stochastic rounding False False False Output stochastic rounding False False False

[422] p: We focus our hyperparameter search on the learning-rate-related parameters, auto-granularity (threshold scale), and the input chopping probability. Consequently, the main distinctions between TT-v2, AGAD and E-RIDER are reflected in these tuned parameters. In addition, E-RIDER includes an extra residual scaling parameter γ \gamma , which controls the contribution of the residual term during gradient computation and is absent in AGAD. For the global learning rate on the LeNet model, we set TT-v2 to 0.005, and AGAD and E-RIDER to 0.05. Other parameters are kept identical across methods unless stated otherwise. It is worth noting that we use a very small learning rate for TT-v2, because with a small number of states and a large reference-point offset, training becomes unstable and can diverge after several epochs when a larger learning rate is used. Despite the smaller learning rate, the accuracy we report for TT-v2 is measured after training has converged. The complete set of hyperparameter is reported in Table 3 for Lenet-5 and Table 5 for FCN.

[423] p: Unless otherwise stated, TT-v2, AGAD and E-RIDER share the same IO and readout noise settings across both architectures: the input and output quantization resolutions are set to 7-bit and 9-bit, respectively; the output read noise is set to 0.06; and the input/output bounds are set to 1 and 12. This configuration is intended to reflect realistic analog hardware non-idealities; the corresponding parameters are summarized in Table 6 .

[424] h4: F.3 Hyperparameter settings for Figure 4

[425] p: For the ablation study comparing the total pulse budget of E-RIDER against the baseline zero-shifting algorithm, both methods use the same SoftBounds-based preset in the RPU configuration, and we set the desired update pulse length to be 5. For E-RIDER, we set the global learning rate to 0.1; the device-side learning rates are fast_lr =0.1 and transfer_lr =1, with auto_granularity =1000 and in_chop_prob =0.2. For the baseline zero-shifting setup, we use the TT-v2 algorithm after SP estimation is completed, train with a global learning rate of 0.05, and set fast_lr =0.01 and transfer_lr =1. We report the hyperparameter settings used in our CIFAR-100 experiments with ResNet-18. We replace the final fully connected layer and the last residual block with analog counterparts. For E-RIDER and AGAD, we report results after 80 epochs; for TT-v2, which consistently diverges during training, we report the best accuracy achieved before divergence. We use a batch size of 128, and decay the learning rate by a factor of 0.1 every 35 epochs. The complete set of hyperparameter is reported in Table 4 .

[426] h4: F.4 Ablation study on the chopper probability p p

[427] figure: Figure 5: Test accuracy of E-RIDER on MNIST-FCN after 50 epochs under different input chopper probabilities p p .

[428] p: Figure 5 reports the performance of E-RIDER on MNIST-FCN after 50 epochs under different input chopper probabilities p p . We observe that enabling chopping with a small p > 0 p>0 substantially improves test accuracy compared to p = 0 p=0 . Therefore, we use E-RIDER with the best-tuned p p in all subsequent experiments.

[429] h2: Instructions for reporting errors

[430] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[431] p: Tip: You can select the relevant text first, to include it in your report.

[432] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[433] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
