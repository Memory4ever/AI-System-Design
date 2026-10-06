[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: FlashOptim: Optimizers for Memory Efficient Training Thanks: Now at Standard Kernel Co. Thanks: Now at Google DeepMind

[3] h6: Abstract

[4] p: Standard mixed-precision training of neural networks requires many bytes of accelerator memory for each model parameter. These bytes reflect not just the parameter itself, but also its gradient and one or more optimizer state variables. With each of these values typically requiring 4 bytes, training even a 7 billion parameter model can be impractical for researchers with less than 100GB of accelerator memory.

[5] p: We introduce FlashOptim, a suite of optimizations that reduces per-parameter memory by over 50% while preserving model quality and API compatibility. Our approach introduces two key techniques. First, we improve master weight splitting by finding and exploiting a tight bound on its quantization error. Second, we design companding functions that greatly reduce the error in 8-bit optimizer state quantization. Together with 16-bit gradients, these techniques reduce AdamW memory from 16 bytes to 7 bytes per parameter, or 5 bytes with gradient release. They also cut model checkpoint sizes by more than half.

[6] p: Experiments with FlashOptim applied to SGD, AdamW, and Lion show no measurable quality degradation on any task from a collection of standard vision and language benchmarks, including Llama-3.1-8B finetuning.

[7] h2: 1 Introduction

[8] p: Recent advances in deep learning have been driven largely by scaling: larger models trained on more data consistently yield better results across language ( Kaplan et al., 2020 ; Hoffmann et al., 2022 ; Chowdhery et al., 2023 ) and vision ( Rosenfeld et al., 2019 ; Tan and Le, 2019 ; Dehghani et al., 2023 ) domains. Training large models can require a great deal of accelerator memory, with each training iteration requiring memory to store parameters, activations, gradients, and optimizer state.

[9] p: How much memory do these tensors require? Table 1 shows a typical breakdown. Excluding activations, which scale with batch size rather than parameter count, training with Adam uses about 16 bytes per parameter. Training a 7-billion-parameter LLM therefore requires at least 112GB of accelerator memory, plus more memory for activations.

[10] figure: Table 1 : Memory per parameter (bytes) for model training . FlashOptim reduces Adam from 16 to 7 bytes and SGD from 12 to 6 bytes. ( ⋆ ) (\star) With gradient release, we further reduce total memory requirements by 2 bytes. Tensor SGD FlashSGD Adam FlashAdam Master Weights 4 2 4 2 Weight Correction 1 1 Gradients 4 2 (0 ⋆ ) 4 2 (0 ⋆ ) Momentum 4 1 4 1 Variance 4 1 Total 12 6 (4 ⋆ ) 16 7 (5 ⋆ )

[11] p: Several approaches mitigate this memory consumption. Distributed training with tensor sharding ( Rajbhandari et al., 2020 ) divides the memory load across multiple accelerators. While this is standard practice in well-resourced organizations, it requires access to multiple accelerators that many practitioners lack. Another alternative is to perform CPU offloading ( Ren et al., 2021 ) , which moves some tensors to host memory at the cost of added overhead and complexity. Third, parameter-efficient methods ( Li and Liang, 2021 ; Hu et al., 2022 ) reduce trainable parameters by freezing most weights and training either a small subset of the original weights or a small set of new auxiliary weights, but fundamentally alter the training dynamics ( Biderman et al., 2024 ) .

[12] p: In this work, we describe FlashOptim, a set of techniques to reduce parameter-associated memory in common deep learning optimizers. Figure 1 shows an example: with FlashOptim, finetuning Llama-3.1-8B drops from 175 GiB to 113 GiB peak memory. Crucially, these memory savings are effectively free—FlashOptim runs just as fast as standard optimizers and causes no measurable loss of model quality across a suite of established training tasks (§ 4 ). This allows our optimizer implementations to serve as drop-in replacements for their unoptimized counterparts. FlashOptim incorporates existing enhancements, such as gradient release ( Zhang et al., 2023 ; Warner, 2024 ) , while also introducing improved float splitting ( Zamirai et al., 2020 ; Warner, 2024 ) and simplified 8-bit optimizer state quantization ( Dettmers et al., 2022 ; Peng et al., 2023 ; Xi et al., 2025 ; Fishman et al., 2025 ) . Furthermore, FlashOptim composes cleanly with existing memory-reduction techniques, such as sharding tensors across accelerators, offloading to CPU, or freezing parameters.

[13] figure: Figure 1 : Memory breakdown for finetuning Llama-3.1-8B. FlashOptim reduces peak memory from 175 to 113 GiB by compressing parameters and optimizer states.

[14] p: We make the following contributions:

[15] p: Improved float splitting : Instead of materializing both a 32-bit master weight and a 16-bit downcast weight for forward and backward, one can split each master weight into a low-precision weight and a correction term stored in the optimizer ( Zamirai et al., 2020 ; Warner, 2024 ) . We improve on existing float splitting techniques by (a) enabling either 8- or 16-bit error correction and (b) achieving much lower reconstruction error for a given number of correction bits. This allows us to use 24-bit master weights with no loss of model quality.

[16] p: Companded optimizer state quantization : Several works have shown that one can compress optimizer states to 8 bits per element given sufficient software complexity. We demonstrate that one can do this much more simply, with nothing more than a one-line preprocessing function before standard group-wise linear quantization. Our ablations across different tensor types suggest that designing custom companding functions is a fruitful direction for future research.

[17] p: Fused optimized kernels : We implement FlashOptim as optimizer step kernels that fuse all compression and quantization operations, reducing memory while preserving throughput during training. Our implementation is publicly available at https://github.com/databricks/flashoptim .

[18] h2: 2 Related Work

[19] p: Low-Precision Training. Mixed-precision training ( Micikevicius et al., 2018 ) executes forward and backward passes in FP16 to reduce memory and compute, while retaining FP32 precision for optimizer states and master weights to preserve numerical stability. Kalamkar et al. (2019) showed that BFloat16 ( Google, 2019 ) works equally well, and Zamirai et al. (2020) explored pure BF16 master weights with stochastic rounding and Kahan summation. Recent work has pushed further with FP8 training ( Wang et al., 2018 ; Mellempudi et al., 2019 ; Micikevicius et al., 2022 ; Fishman et al., 2025 ; Narayan et al., 2025 ) , though these approaches primarily target compute formats and retain higher-precision storage for master weights. FlashOptim extends this line of work with an improved float splitting mechanism that reduces storage to 3 bytes per parameter, down from 4-byte FP32, while maintaining FP32-equivalent training semantics.

[20] p: Optimizer State Compression. Dettmers et al. (2022) applied 8-bit block-wise dynamic quantization to Adam’s momentum and variance, reducing optimizer state from 8 to 2 bytes per parameter. Follow-up work explored FP8 representations ( Peng et al., 2023 ; Xi et al., 2025 ; Fishman et al., 2025 ) , and Li et al. (2023) compressed both moments to 4-bit using row and column-wise quantization. MicroAdam ( Modoranu et al., 2024 ) instead compresses gradients before updating optimizer states. Rather than design elaborate quantization methods or number formats, we show that one can obtain 8-bit optimizer states with no quality loss using simple, one-line preprocessing functions. Beyond optimizer states, we address additional sources of per-parameter memory, eliminating entire bytes from other tensors.

[21] p: Gradient Memory and Communication. LOMO ( Lv et al., 2024b ) , AdaLOMO ( Lv et al., 2024a ) , and Adam Accumulation ( Zhang et al., 2023 ) fuse parameter updates into the backward pass to release gradient memory eagerly. However, this conflicts with gradient accumulation, which requires the full accumulated gradient before updating. In distributed settings, gradient communication can also become a bottleneck. One can reduce this bottleneck by, e.g., compressing gradients to 1-bit with error feedback ( Tang et al., 2021 ) , or using low-rank approximations ( Vogels et al., 2019 ) . FlashOptim supports gradient release when compatible and could be used alongside communication compression techniques.

[22] p: Memory-Efficient Optimization. Alternative optimizer designs reduce memory by restructuring update rules and stored buffers. Adafactor ( Shazeer and Stern, 2018 ) achieves sublinear memory by factorizing the second moment into row and column statistics; SM3 ( Anil et al., 2019 ) stores structured maxima; NovoGrad ( Ginsburg et al., 2019 ) replaces per-parameter variance with layer-wise normalization. Adam-mini ( Zhang et al., 2025 ) shares variance terms across parameter blocks, while Adapprox ( Zhao et al., 2024b ) uses a low-rank approximation. Other approaches eliminate the second moment entirely: Lion ( Chen et al., 2023 ) uses sign-based momentum, and Muon ( Jordan et al., 2024 ; Liu et al., 2025 ) applies orthogonalized updates. Pethick et al. (2025) extend Muon to unify gradient accumulation with momentum, removing dedicated optimizer memory altogether.

[23] p: Low-rank decompositions approximate full tensors while requiring less memory. For fine-tuning, LoRA ( Hu et al., 2022 ) and QLoRA ( Dettmers et al., 2023 ) freeze base weights and train only low-rank adapters. For pretraining, GaLore ( Zhao et al., 2024a ) projects gradients to a low-rank subspace, and APOLLO ( Zhu et al., 2025 ) approximates adaptive scaling with random projections. Unlike these approaches that modify the optimizer’s update rule, FlashOptim preserves standard optimizer semantics and can be combined with these techniques.

[24] p: System-Level Memory Optimizations. System-level approaches reduce accelerator memory without changing optimization semantics. Activation checkpointing ( Chen et al., 2016 ; Korthikanti et al., 2023 ) trades compute for memory by recomputing activations during the backward pass. ZeRO ( Rajbhandari et al., 2020 ) partitions optimizer states, gradients, and parameters across data-parallel ranks, while offloading ( Rajbhandari et al., 2021 ; Ren et al., 2021 ) moves state to CPU or NVMe memory. FlashOptim is orthogonal to these approaches: it reduces the per-rank footprint and can be used with ZeRO, FSDP ( Zhao et al., 2023 ) , and activation checkpointing.

[25] h2: 3 Method

[26] p: This section describes the two key techniques behind FlashOptim: weight splitting (§ 3.1 ) and companded optimizer state quantization (§ 3.2 ). We then describe how to integrate these ideas into common optimizer updates while minimizing associated overhead (§ 3.3 ).

[27] h3: 3.1 Weight Splitting

[28] p: Mixed-precision training uses 16-bit weights for forward and backward passes, but accumulating gradient updates requires higher precision to avoid stagnation ( Micikevicius et al., 2018 ) . Thus, the standard practice is to maintain FP32 precision master weights during training.

[29] p: However, this introduces waste: the downcast weights take space, but store no information beyond what’s saved in the master weights. To eliminate this redundancy, weight splitting ( Zamirai et al., 2020 ; Warner, 2024 ) instead stores the downcast weights and narrow error-correction values. By combining a 16-bit weight θ ′ \theta^{\prime} with a 16-bit error correction value ρ \rho , one has enough information to reconstruct a 32-bit master weight θ \theta with no redundancy.

[30] p: The core questions in a weight splitting scheme are 1) how to set ( θ ′ , ρ ) (\theta^{\prime},\rho) given θ \theta and 2) how to estimate θ \theta given ( θ ′ , ρ ) (\theta^{\prime},\rho) . One obvious approach is to use the high 16 bits of θ \theta as θ ′ \theta^{\prime} and the low 16 bits as ρ \rho . This admits exact reconstruction of θ \theta for the special case of BF16 θ ′ \theta^{\prime} and FP32 θ \theta , since these formats happen to share the same exponent sizes and offsets. However, this approach doesn’t generalize to other pairs of number formats. It also rounds towards zero instead of towards the nearest low-precision value.

[31] p: A more general alternative, used in previous work ( Zamirai et al., 2020 ; Warner, 2024 ) , is to set ρ = θ − θ ′ \rho=\theta-\theta^{\prime} , represented as a BF16 value. The problem with this is that the difference of two floating-point numbers requires as many bits to store exactly as the wider of the two floats. 1 1 1 Consider, e.g., storing the minimum float32 subnormal, which will be rounded to zero by any narrower datatype. This means that a BF16 ρ \rho incurs approximation error. E.g., if the rounding error were 1e-5, BF16 could only represent 1.0014e-5. In general, while BF16’s wide exponent lets it represent nearly the full range of FP32, its 7 mantissa bits only guarantee a relative error bound of 1/256.

[32] p: Our observation is that all exponent bits in this scheme are wasted . The exponent of e ≜ θ − θ ′ e\triangleq\theta-\theta^{\prime} can always be inferred from θ ′ \theta^{\prime} : under round-to-nearest, θ \theta must lie within [ θ ′ − u / 2 , θ ′ + u / 2 ] [\theta^{\prime}-u/2,\theta^{\prime}+u/2] , where u = ULP ​ ( θ ′ ) u=\text{ULP}(\theta^{\prime}) is the unit in the last place ( Goldberg, 1991 ) . If θ \theta were outside this interval, it would have rounded to a different value. It therefore suffices to encode where e e falls within this tiny interval rather than across the full FP32 range.

[33] p: To exploit this observation, we rescale e e such that [ − u / 2 , u / 2 ] [-u/2,u/2] maps to [ − N , N ] [-N,N] ; N ≜ 2 b − 1 N\triangleq 2^{b}-1 and then quantize this rescaled e e to the nearest b b -bit integer. That is,

[34] table: θ ′ \displaystyle\theta^{\prime} = downcast ​ ( θ ) \displaystyle=\text{downcast}(\theta) (1) ρ \displaystyle\rho = round ​ ( θ − θ ′ ULP ​ ( θ ′ ) / 2 ⋅ N ) , \displaystyle=\text{round}\left(\frac{\theta-\theta^{\prime}}{\text{ULP}(\theta^{\prime})/2}\cdot N\right),

[35] p: To reconstruct θ \theta from ( θ ′ , ρ ) (\theta^{\prime},\rho) , we invert this scaling and add the result to θ ′ \theta^{\prime} .

[36] table: θ ^ = θ ′ + ρ N ⋅ ULP ​ ( θ ′ ) 2 \displaystyle\hat{\theta}=\theta^{\prime}+\frac{\rho}{N}\cdot\frac{\text{ULP}(\theta^{\prime})}{2} (2)

[37] p: For tensors of floating-point values we apply this transformation elementwise. Algorithm 1 provides a lower-level description of the compression and decompression operations with numerical precision considerations.

[38] figure: Algorithm 1 Weight Splitting 1: Constants: N N (127 for INT8, 32767 for int16) 2: function 𝒞 \mathcal{C} ( θ \theta ) 3: θ ′ ← Downcast ⁡ ( θ ) \theta^{\prime}\leftarrow\mathrm{Downcast}(\theta) 4: e ← θ − Float32 ⁡ ( θ ′ ) e\leftarrow\theta-\mathrm{Float32}(\theta^{\prime}) 5: ℓ ← ⌊ log 2 ​ ULP ​ ( θ ′ ) ⌋ − 1 \ell\leftarrow\lfloor\mathrm{log_{2}ULP}(\theta^{\prime})\rfloor-1 6: h ← ⌊ − ℓ / 2 ⌋ h\leftarrow\lfloor-\ell/2\rfloor // For numerical stability 7: e norm ← ( e ⋅ 2 h ) ⋅ 2 − ℓ − h e_{\mathrm{norm}}\leftarrow(e\cdot 2^{h})\cdot 2^{-\ell-h} 8: ρ ← Int ⁡ ( Round ⁡ ( Clamp ⁡ ( e norm , − 1 , 1 ) ⋅ N ) ) \rho\leftarrow\mathrm{Int}(\mathrm{Round}(\mathrm{Clamp}(e_{\mathrm{norm}},-1,1)\cdot N)) 9: return θ ′ , ρ \theta^{\prime},\rho 10: function 𝒞 − 1 \mathcal{C}^{-1} ( θ ′ , ρ \theta^{\prime},\rho ) 11: ℓ ← ⌊ log 2 ​ ULP ​ ( θ ′ ) ⌋ − 1 \ell\leftarrow\lfloor\mathrm{log_{2}ULP}(\theta^{\prime})\rfloor-1 12: h ← ⌊ ℓ / 2 ⌋ h\leftarrow\lfloor\ell/2\rfloor 13: e ← ( ( Float32 ⁡ ( ρ ) / N ) ⋅ 2 h ) ⋅ 2 ℓ − h e\leftarrow((\mathrm{Float32}(\rho)/N)\cdot 2^{h})\cdot 2^{\ell-h} 14: return Float32 ⁡ ( θ ′ ) + e \mathrm{Float32}(\theta^{\prime})+e

[39] p: When using BF16 for θ ′ \theta^{\prime} and INT8 for ρ \rho , the compressed representation provides approximately 24 bits of effective precision (16 from BF16 plus 8 from the error term). This is analogous to the PXR24 format used in high-dynamic-range imaging, which achieves similar precision by rounding 32-bit floats to 24 bits ( Kainz et al., 2004 ) .

[40] h3: 3.2 Companded Optimizer State Quantization

[41] p: For optimizer state variables such as momentum and variance estimates, a common approach is group-wise quantization: dividing tensors into fixed-length groups and mapping values to a lower-precision format like INT8 ( Dettmers et al., 2022 ) . To increase the precision range of the group of values, they are rescaled using the maximum absolute value ( absmax ), which is stored as an additional scale with 32 or 16 bits of precision. While simple, this uniform quantization allocates bins evenly across the value range, implicitly assuming that values are roughly uniformly distributed. Our measurements show that optimizer state distributions violate this assumption, and we find that applying nonlinear companding functions before quantization can reshape these distributions toward uniformity, improving utilization of quantization bins and reducing quantization error. As we show in § 4.5 , this companding step is critical: without it, linear quantization of optimizer states causes training to diverge.

[42] p: We design specialized transformations for each optimizer state type. For momentum tensors (used in SGD, Adam, and Lion), we first normalize each group by its absmax scale, then apply a softsign-like function:

[43] table: ϕ m ​ ( x ) = 2 ​ x 1 + | x | ϕ m − 1 ​ ( z ) = z 2 − | z | \phi_{m}(x)=\frac{2x}{1+|x|}\qquad\phi_{m}^{-1}(z)=\frac{z}{2-|z|} (3)

[44] p: This function compresses extreme values: inputs near ± 1 \pm 1 are pushed toward the center, spreading the momentum distribution more evenly across quantization bins. In contrast, for variance tensors in Adam, we first apply a square root, then normalize by the group absmax:

[45] table: ϕ v ​ ( x ) = x ϕ v − 1 ​ ( z ) = z 2 \phi_{v}(x)=\sqrt{x}\qquad\phi_{v}^{-1}(z)=z^{2} (4)

[46] p: Here the square root is motivated by Adam’s variance update v t = β 2 ​ v t − 1 + ( 1 − β 2 ) ​ g 2 v_{t}=\beta_{2}v_{t-1}+(1-\beta_{2})g^{2} that accumulates squared gradients, producing heavy-tailed distributions with large dynamic range. Both transformations satisfy key design criteria: they are exactly invertible, computationally efficient (one division or square root per element), their inverses are computationally efficient, and require no hyperparameters.

[47] figure: Algorithm 2 𝒬 m \mathcal{Q}_{m} : Momentum Quantization 1: Constants: Group size G = 32 G=32 2: function 𝒬 m \mathcal{Q}_{m} ( m m ) 3: for each group g g of G G elements do 4: s g ← max ⁡ ( | m g | ) s_{g}\leftarrow\max(|m_{g}|) 5: m g ′ ← m g / s g m^{\prime}_{g}\leftarrow m_{g}/s_{g} 6: m g ′′ ← 2 ​ m g ′ / ( 1 + | m g ′ | ) m^{\prime\prime}_{g}\leftarrow 2m^{\prime}_{g}/(1+|m^{\prime}_{g}|) 7: m g q ← Round ⁡ ( m g ′′ ⋅ 127 , INT8 ) m^{q}_{g}\leftarrow\mathrm{Round}(m^{\prime\prime}_{g}\cdot 127,\text{INT8}) 8: return m q , s m^{q},s 9: function 𝒬 m − 1 \mathcal{Q}_{m}^{-1} ( m q , s m^{q},s ) 10: for each group g g do 11: m g ′′ ← m g q / 127 m^{\prime\prime}_{g}\leftarrow m^{q}_{g}/127 12: m g ′ ← m g ′′ / ( 2 − | m g ′′ | ) m^{\prime}_{g}\leftarrow m^{\prime\prime}_{g}/(2-|m^{\prime\prime}_{g}|) 13: m g ← m g ′ ⋅ s g m_{g}\leftarrow m^{\prime}_{g}\cdot s_{g} 14: return m m

[48] figure: Algorithm 3 𝒬 v \mathcal{Q}_{v} : Variance Quantization 1: Constants: Group size G = 32 G=32 2: function 𝒬 v \mathcal{Q}_{v} ( v v ) 3: v ′ ← v v^{\prime}\leftarrow\sqrt{v} 4: for each group g g of G G elements do 5: s g ← max ⁡ ( v g ′ ) s_{g}\leftarrow\max(v^{\prime}_{g}) 6: v g q ← Round ⁡ ( ( v g ′ / s g ) ⋅ 255 , UINT8 ) v^{q}_{g}\leftarrow\mathrm{Round}((v^{\prime}_{g}/s_{g})\cdot 255,\text{UINT8}) 7: return v q , s v^{q},s 8: function 𝒬 v − 1 \mathcal{Q}_{v}^{-1} ( v q , s v^{q},s ) 9: for each group g g do 10: v g ′ ← ( v g q / 255 ) ⋅ s g v^{\prime}_{g}\leftarrow(v^{q}_{g}/255)\cdot s_{g} 11: v g ← ( v g ′ ) 2 v_{g}\leftarrow(v^{\prime}_{g})^{2} 12: return v v

[49] p: For both momentum and variance, we partition the tensor into groups of G = 32 G=32 elements and store a separate FP16 scale factor per group, introducing an overhead of 2 / G = 1 / 16 2/G=1/16 bytes per parameter. We store the normalized momentum in signed integers (INT8) and variance in unsigned integers (UINT8) since it is non-negative. Algorithms 2 and 3 detail the quantization and dequantization procedures for momentum and variance respectively.

[50] figure: Algorithm 4 FlashAdamW: Memory-Efficient AdamW. We highlight the changes from AdamW. 1: Parameters θ 0 \theta_{0} , learning rate schedule { η t } t = 1 T \{\eta_{t}\}_{t=1}^{T} , β 1 , β 2 ∈ [ 0 , 1 ) \beta_{1},\beta_{2}\in[0,1) , ε > 0 \varepsilon>0 , weight decay λ ≥ 0 \lambda\geq 0 , loss ℒ ⁡ ( θ ) \mathcal{L}(\theta) , minibatch sampler ℬ ⁡ ( ⋅ ) \mathcal{B}(\cdot) 2: m 0 q , m 0 s ← 𝒬 m ​ ( 0 ) m_{0}^{q},m_{0}^{s}\leftarrow\mathcal{Q}_{m}(0) 3: v 0 q , v 0 s ← 𝒬 v ​ ( 0 ) v_{0}^{q},v_{0}^{s}\leftarrow\mathcal{Q}_{v}(0) 4: θ 0 ′ , ρ 0 ← 𝒞 ⁡ ( θ 0 ) \theta^{\prime}_{0},\rho_{0}\leftarrow\mathcal{C}(\theta_{0}) 5: Initialize t ← 0 t\leftarrow 0 6: while not converged do 7: t ← t + 1 t\leftarrow t+1 8: B t ∼ ℬ B_{t}\sim\mathcal{B} 9: g t ← ∇ θ ℒ ​ ( B t , θ t − 1 ′ ) g_{t}\leftarrow\nabla_{\theta}\mathcal{L}(B_{t};{{\text{\hbox{\pagecolor{SpringGreen}$\theta^{\prime}_{t-1}$}}}}) 10: // Reconstruct optimizer state and master weight 11: m t − 1 ← 𝒬 m − 1 ​ ( m t − 1 q , m t − 1 s ) m_{t-1}\leftarrow\mathcal{Q}_{m}^{-1}(m^{q}_{t-1},m^{s}_{t-1}) 12: v t − 1 ← 𝒬 v − 1 ​ ( v t − 1 q , v t − 1 s ) v_{t-1}\leftarrow\mathcal{Q}_{v}^{-1}(v^{q}_{t-1},v^{s}_{t-1}) 13: θ t − 1 ← 𝒞 − 1 ​ ( θ t − 1 ′ , ρ t − 1 ) \theta_{t-1}\leftarrow\mathcal{C}^{-1}(\theta^{\prime}_{t-1},\rho_{t-1}) 14: // Standard optimizer update 15: m t ← β 1 ​ m t − 1 + ( 1 − β 1 ) ​ g t m_{t}\leftarrow\beta_{1}m_{t-1}+(1-\beta_{1})g_{t} 16: v t ← β 2 ​ v t − 1 + ( 1 − β 2 ) ​ g t 2 v_{t}\leftarrow\beta_{2}v_{t-1}+(1-\beta_{2})g_{t}^{2} 17: m ^ t ← m t / ( 1 − β 1 t ) \hat{m}_{t}\leftarrow m_{t}/(1-\beta_{1}^{t}) 18: v ^ t ← v t / ( 1 − β 2 t ) \hat{v}_{t}\leftarrow v_{t}/(1-\beta_{2}^{t}) 19: θ t ← θ t − 1 − η t ​ ( m ^ t / ( v ^ t + ε ) + λ ​ θ t − 1 ) \theta_{t}\leftarrow\theta_{t-1}-\eta_{t}\left(\hat{m}_{t}/(\sqrt{\hat{v}_{t}}+\varepsilon)+\lambda\theta_{t-1}\right) 20: // Quantize optimizer state and split master weight 21: m t q , m t s ← 𝒬 m ​ ( m t ) m^{q}_{t},m^{s}_{t}\leftarrow\mathcal{Q}_{m}(m_{t}) 22: v t q , v t s ← 𝒬 v ​ ( v t ) v^{q}_{t},v^{s}_{t}\leftarrow\mathcal{Q}_{v}(v_{t}) 23: θ t ′ , ρ t ← 𝒞 ⁡ ( θ t ) \theta^{\prime}_{t},\rho_{t}\leftarrow\mathcal{C}(\theta_{t})

[51] h3: 3.3 Optimizer Update

[52] p: We modify any given gradient update rule by adding a prologue and an epilogue. In the prologue, we dequantize the optimizer states and reconstruct the master weight θ \theta from the low-precision weight θ ′ \theta^{\prime} and the error correction bits ρ \rho . In the epilogue, we quantize the new optimizer state and split the new θ \theta into an updated ( θ ′ , ρ ) (\theta^{\prime},\rho) . At the start of training, we downcast the master weights to BF16 to ensure training runs directly on the low-precision θ ′ \theta^{\prime} with no downcasts apart from our optimizer step. Algorithm 4 illustrates these changes for the AdamW optimizer, and Algorithms 5 and 6 in the appendix show the corresponding changes to SGD and Lion respectively.

[53] h3: 3.4 Implementation

[54] p: Update kernels. Since compression and quantization are bandwidth-bound operations, we implement the optimizer step as a single fused Triton kernel ( Tillet et al., 2019 ) . For example, for the AdamW update our kernel encompasses steps 9 through 22 from Algorithm 4 .

[55] p: Gradient release. We implement gradient release ( Zhang et al., 2023 ) , interleaving gradient computation with optimizer updates during backpropagation. As each gradient is computed, we eagerly apply the optimizer rule to free the gradient memory. We apply this optimization only when gradient accumulation is disabled.

[56] p: Distributed training. Our implementation is compatible with parameter sharding approaches such as PyTorch FSDP ( Zhao et al., 2023 ) . During forward and backward passes, only the 16-bit θ ′ \theta^{\prime} parameters are all-gathered; the correction term ρ \rho remains local with the optimizer states.

[57] p: Checkpoint size. Our representation reduces checkpoint size. For instance, standard Adam checkpoints require 12 bytes per parameter (4 for weights, 4 for momentum, 4 for variance); FlashAdamW requires only 5 bytes (2 for weights, 1 for correction, 1 for momentum, and 1 for variance). For a 7B model, checkpoint size reduces from 84GB to 35GB.

[58] p: Code availability. We make our implementation widely available as an open-source PyTorch library at https://github.com/databricks/flashoptim .

[59] h2: 4 Experiments

[60] h3: 4.1 Experimental Setup

[61] p: We evaluate FlashOptim with three optimizers: SGD with momentum ( Polyak, 1964 ) , AdamW ( Loshchilov and Hutter, 2017 ) , and Lion ( Chen et al., 2023 ) . We refer to these variants as FlashSGD, FlashAdamW, and FlashLion. We test these across several large-scale deep learning tasks, including image classification, language model pretraining, and supervised finetuning.

[62] p: To ensure a fair comparison, all experiments use identical hyperparameters between reference optimizers and their FlashOptim counterparts. We re-implement the reference optimizers with similar fused Triton kernels for consistent measurement of memory and throughput, and all reference implementations use mixed precision ( Micikevicius et al., 2018 ) to keep activations in 16-bit precision. The precisions of master weights θ \theta , error correction term ρ \rho , gradients g g , momentum m m , variance v v , and activations a a are as follows:

[63] figure: θ \theta ρ \rho g g m m v v a a Reference FP32 — FP32 FP32 FP32 BF16 FlashOptim BF16 INT8 BF16 INT8 UINT8 BF16

[64] p: Our experiments demonstrate four main findings. First, FlashOptim matches reference convergence and accuracy across all tested configurations (§ 4.2 ). Second, it reduces optimizer memory by over 50% with negligible computational overhead (§ 4.3 ). Third, our ULP-based weight splitting achieves near-optimal reconstruction (§ 4.4 ). Finally, our companding functions significantly reduce quantization error for both momentum and variance states (§ 4.5 ).

[65] p: Image Classification. We train a ResNet-50 architecture ( He et al., 2016b ) on the ILSVRC2012 (ImageNet-1K) dataset ( Deng et al., 2009 ) . We use the hyperparameters recommended by Nvidia ( NVIDIA, 2023 ) , with additional details provided in Appendix B.1 .

[66] p: LLM Pretraining. We evaluate LLM pretraining using the training recipe outlined in the nanoGPT repository ( Karpathy, 2023 ) . We use the GPT-2 ( Radford et al., 2019 ) architecture and train on a 10B token subset of the FineWeb dataset ( Penedo et al., 2024 ) , following the setup of Jordan (2024) . We provide hyperparameter details in Appendix B.2 . We evaluate models using a suite of in-context learning (ICL) benchmarks that assess commonsense reasoning and language understanding capabilities. We provide a complete list of benchmarks in Appendix B.3 .

[67] p: LLM Finetuning. We run supervised finetuning on a pretrained Llama-3.1-8B model ( Dubey et al., 2024 ) on OpenMathInstruct-2 ( Toshniwal et al., 2024 ) , and evaluate on the GSM8k ( Cobbe et al., 2021 ) benchmark. We provide further hyperparameter details in Appendix B.4 .

[68] p: Training and Infrastructure. We train with distributed data parallelism for the image classification and LLM pretraining tasks, and for LLM finetuning we use FSDP ( Zhao et al., 2023 ) and activation checkpointing. We train all models using PyTorch 2.8 and CUDA 12.8 on NVIDIA H100 GPUs. We report the mean and standard deviation for all our results with 3 random seeds. For loss curve comparisons, we use identical data ordering across methods. System metrics (memory, timing) are measured in steady-state.

[69] figure: (a) LLM Pretraining (GPT-2 + AdamW) (b) Vision Classification (ResNet-50 + SGD) Figure 2 : Training convergence . Comparison of training loss trajectories between reference optimizers and their FlashOptim variants. Both achieve nearly identical loss curves throughout training, demonstrating that our memory optimizations do not impact model quality.

[70] figure: Table 2 : Image Classification & LLM Finetuning Results . Validation accuracy for ResNet-50 (first two columns), and GSM8k accuracy for the LLM finetuning task (last column). We report standard deviation across 3 training runs. In all settings FlashOptim matches the reference scores. ImageNet Top-1 Acc. GSM8k Acc. SGD AdamW AdamW Reference 77.01 ± \pm 0.02 75.51 ± \pm 0.09 75.09 ± \pm 0.40 FlashOptim 77.16 ± \pm 0.09 75.67 ± \pm 0.04 74.98 ± \pm 0.77

[71] figure: Table 3 : LLM Pretraining Results . NanoGPT results with GPT-2 (124M). We report validation loss and accuracy (%) on in-context learning benchmarks assessing commonsense reasoning and language understanding. We report standard deviation across 3 training runs. Optimizer Val Loss HellaSwag ARC-E CSQA PIQA LAMBADA Winograd BoolQ Mean ICL AdamW 3.263 ± \pm 0.001 31.9 ± \pm 0.2 39.6 ± \pm 0.7 25.9 ± \pm 4.1 64.3 ± \pm 0.0 31.0 ± \pm 1.2 57.3 ± \pm 0.6 58.1 ± \pm 3.6 44.0 ± \pm 0.4 FlashAdamW 3.265 ± \pm 0.001 31.9 ± \pm 0.5 39.5 ± \pm 0.9 30.8 ± \pm 2.1 64.5 ± \pm 0.3 31.9 ± \pm 0.7 59.1 ± \pm 1.1 57.2 ± \pm 4.8 45.0 ± \pm 1.0 Lion 3.240 ± \pm 0.002 32.3 ± \pm 0.0 40.0 ± \pm 0.5 23.3 ± \pm 1.8 63.8 ± \pm 1.0 31.5 ± \pm 0.2 58.9 ± \pm 2.0 58.1 ± \pm 2.4 44.0 ± \pm 0.5 FlashLion 3.240 ± \pm 0.001 32.4 ± \pm 0.3 40.8 ± \pm 0.2 25.4 ± \pm 2.9 64.2 ± \pm 0.5 31.6 ± \pm 0.5 59.1 ± \pm 2.4 59.1 ± \pm 2.3 44.7 ± \pm 0.5

[72] h3: 4.2 Convergence and Accuracy

[73] p: We first verify that FlashOptim introduces no measurable degradation by comparing training convergence and validation accuracy. Figure 2(a) shows training loss for LLM pretraining with AdamW and FlashAdamW. FlashAdamW produces a nearly identical trajectory to the reference AdamW and closely tracks AdamW even after 20,000 parameter updates, indicating that reduced precision does not affect learning dynamics. Figure 2(b) shows similar results for image classification: FlashSGD matches reference SGD throughout training. For LLM finetuning, Figure 8 in the appendix shows an analogous result for AdamW.

[74] p: Table 2 reports final scores for the image classification and LLM finetuning tasks. FlashSGD and FlashAdamW match the reference optimizer scores in all three settings. Table 3 compares final validation loss and in-context learning scores for the LLM pretraining task. Models trained with FlashOptim achieve scores within variance of reference optimizers across all metrics.

[75] h3: 4.3 Memory and Speed

[76] p: We compare memory requirements and optimizer step time, demonstrating that FlashOptim reduces peak memory ( PyTorch Contributors, 2025 ) without practical overhead. We focus on parameter-related memory (weights, optimizer state, gradients) since activation memory is identical across both settings. To isolate contributions, we ablate: weight splitting (Weight Split) with full-precision optimizer states, and optimizer state quantization with companding (Opt. Quant.) with FP32 master weights.

[77] p: Table 4 breaks down the memory usage for LLM finetuning on a Llama-3.1-8B model. As anticipated, we reduce parameter memory by 50% from dropping precision from FP32 to BF16, and reduce optimizer memory by 60% from quantizing the optimizer state tensors. Moreover, when looking at peak memory (including activations), FlashOptim reduces it by 36% with no practical slowdown in optimizer step times.

[78] p: Ablating each component confirms that weight splitting halves master weight memory while adding 12% of extra optimizer state. Optimizer state quantization reduces optimizer state by ∼ \sim 73% by mapping FP32 tensors to INT8/UINT8; the reduction is slightly less than 75% due to the overhead of storing FP16 scale factors for each group of 32 elements. Tables 6 and 8 in the appendix show similar trends for LLM pretraining and image classification.

[79] figure: Table 4 : Profiling . Runtime measurements for LLM Finetuning with Llama-3.1-8B. We capture master weight memory (Params), optimizer state memory (Optim), peak GPU memory (Peak), and optimizer step times (Step). Params Optim Peak Step Variant GiB Δ \Delta GiB Δ \Delta GiB Δ \Delta ms Reference 29.9 59.8 175.2 12.5 FlashOptim 15.0 -50% 23.4 -61% 112.9 -36% 11.5 Ablations Weight Split 15.0 -50% 67.3 +12% 156.7 -11% 10.7 Opt. Quant. 29.9 15.9 -73% 131.4 -25% 10.5

[80] h3: 4.4 Weight Error Correction

[81] p: We compare our weight splitting scheme to Zamirai et al. (2020) , who store the rounding error in a floating-point buffer for Kahan summation error correction. Since both approaches are data-independent, we evaluate them exhaustively over all finite FP32 bitstrings, computing relative error after applying compression and decompression in sequence. We consider four methods: a no error correction baseline, storing error in the same 16-bit format, our ULP-normalized error with 8-bit integers, and ours with 16-bit integers.

[82] p: Figure 3 plots mean relative error versus exponent for BF16 and FP16. For BF16, our ULP approach with 16-bit correction achieves near-zero error ( < 10 − 9 <10^{-9} ). With 16 bits of correction term, we achieve perfect bitwise reconstruction in 99.92 % 99.92\% of the values. In contrast, storing the error in BF16 (BF16+BF16) produces substantially worse error ( > 10 − 6 >10^{-6} ), comparable to our 24-bit format. For FP16, our 32-bit ULP format perfectly reconstructs values in the normal range and dominates FP16+FP16 throughout. Our 24-bit format produces constant error across the normal range, improving worst-case error from 10 − 4 10^{-4} to under 10 − 6 10^{-6} .

[83] figure: Figure 3 : FP32 Reconstruction Error. Comparison of FP32 reconstruction error for different weight compression schemes across exponent ranges for a target datatype of BF16 (top) and FP16 (bottom). Our ULP-based error correction achieves lower relative error particularly for small exponents. Denormal floating point ranges are indicated with vertical dotted lines.

[84] h3: 4.5 Optimizer State Quantization

[85] p: We validate our companding functions by comparing quantization error against standard scaled integer quantization. Using a fixed full precision training trajectory for consistency, we quantize and dequantize momentum and variance buffers at each step, computing normalized MSE (NMSE) against the original values. Figure 4 shows quantile distributions of NMSE for each optimizer and buffer type. Companding reduces error for momentum buffers and provides substantial improvements for variance buffers, where NMSE drops significantly.

[86] figure: Figure 4 : Optimizer state quantization error. NMSE comparison between standard scaled integer quantization (Linear) and our companding approach for momentum ( m m ) and variance ( v v ) buffers across different optimizers and datasets. Companding reduces quantization error across all optimizer types and tensor types, with particularly large improvements for variance tensors.

[87] p: Beyond reducing quantization error, in some cases companding is essential for training stability. Figure 5 shows LLM pretraining with and without variance companding: linear quantization causes training to diverge, while companding maintains stable convergence.

[88] figure: Figure 5 : Companding prevents training divergence. GPT-2 training with AdamW and quantized optimizer states: linear quantization (no companding) causes rapid divergence, while our companding approach maintains stable training dynamics.

[89] h2: 5 Limitations

[90] p: FlashOptim is designed to minimize parameter-associated memory consumption, so models with large parameter counts and small activations benefit most from our optimizations. Smaller architectures with large activations, such as convolutional networks with high-resolution feature maps, are often dominated by activation memory. In these activation-dominated regimes, a 50% reduction in parameter memory translates to modest total memory savings and techniques like activation checkpointing are more effective for such workloads.

[91] p: Another limitation is that some tasks and architectures may be more sensitive to quantization than those in our benchmarks. The effectiveness of a quantization pipeline depends on the data distribution, and there is no guarantee that our method (or any quantization approach) will preserve model quality in all cases. Consequently, our implementation allows selectively disabling compression or excluding specific layers as needed.

[92] p: Finally, while we find that 24-bit master weights are sufficient in our experiments, not even 32 bits are guaranteed to suffice in all cases. Successive (normal) floating-point values differ by a factor of roughly 2 − num_mantissa_bits 2^{-\text{num\_mantissa\_bits}} , and if the ratio of weight update to weight magnitude falls below this threshold, the update will be discarded.

[93] h2: 6 Conclusion

[94] p: We introduced FlashOptim, a method to reduce the memory footprint of neural network training while preserving optimizer semantics and model quality. FlashOptim provides drop-in replacements for common optimizers and requires no additional tuning.

[95] p: Our approach combines two key techniques. First, we reduce master weights from 32 to 24 bits via improved floating point error correction. Second, we use companding functions to enable 8-bit optimizer state quantization. Together with 16-bit gradients, these reduce per-parameter memory by over 50% for AdamW.

[96] p: We validated FlashOptim on image and language benchmarks using SGD, AdamW, and Lion. Across all settings, our method matches reference implementations in both loss and accuracy while providing significant memory savings. FlashOptim composes with FSDP and activation checkpointing, enabling multiplicative benefits for large-scale training. By lowering memory requirements, FlashOptim enables practitioners and researchers with limited hardware to train larger models than previously feasible.

[97] h2: Acknowledgements

[98] p: We are grateful to Jonathan Frankle, Xing Chen, and Matei Zaharia for their continued support and guidance. We also thank Jialu Liu and Erich Elsen for insightful discussions.

[99] h2: References

[100] h2: Appendix A Method Details

[101] p: This section provides detailed pseudocode for the FlashOptim version of SGD ( Algorithm 5 ) and Lion ( Algorithm 6 ).

[102] figure: Algorithm 5 FlashSGD: Memory-Efficient SGD. We highlight the changes from SGD. 1: Parameters θ 0 \theta_{0} , learning rate schedule { η t } t = 1 T \{\eta_{t}\}_{t=1}^{T} , momentum μ ∈ [ 0 , 1 ) \mu\in[0,1) , weight decay λ ≥ 0 \lambda\geq 0 , loss ℒ ⁡ ( θ ) \mathcal{L}(\theta) , minibatch sampler ℬ ⁡ ( ⋅ ) \mathcal{B}(\cdot) 2: m 0 q , m 0 s ← 𝒬 m ​ ( 0 ) m_{0}^{q},m_{0}^{s}\leftarrow\mathcal{Q}_{m}(0) 3: θ 0 ′ , ρ 0 ← 𝒞 ⁡ ( θ 0 ) \theta^{\prime}_{0},\rho_{0}\leftarrow\mathcal{C}(\theta_{0}) 4: Initialize t ← 0 t\leftarrow 0 5: while not converged do 6: t ← t + 1 t\leftarrow t+1 7: B t ∼ ℬ B_{t}\sim\mathcal{B} 8: g t ← ∇ θ ℒ ​ ( B t , θ t − 1 ′ ) g_{t}\leftarrow\nabla_{\theta}\mathcal{L}(B_{t};{{\text{\hbox{\pagecolor{SpringGreen}$\theta^{\prime}_{t-1}$}}}}) 9: m t − 1 ← 𝒬 m − 1 ​ ( m t − 1 q , m t − 1 s ) m_{t-1}\leftarrow\mathcal{Q}_{m}^{-1}(m^{q}_{t-1},m^{s}_{t-1}) 10: m t ← μ ​ m t − 1 + g t m_{t}\leftarrow\mu m_{t-1}+g_{t} 11: m t q , m t s ← 𝒬 m ​ ( m t ) m^{q}_{t},m^{s}_{t}\leftarrow\mathcal{Q}_{m}(m_{t}) 12: θ t − 1 ← 𝒞 − 1 ​ ( θ t − 1 ′ , ρ t − 1 ) \theta_{t-1}\leftarrow\mathcal{C}^{-1}(\theta^{\prime}_{t-1},\rho_{t-1}) 13: θ t ← θ t − 1 − η t ​ ( m t + λ ​ θ t − 1 ) \theta_{t}\leftarrow\theta_{t-1}-\eta_{t}(m_{t}+\lambda\theta_{t-1}) 14: θ t ′ , ρ t ← 𝒞 ⁡ ( θ t ) \theta^{\prime}_{t},\rho_{t}\leftarrow\mathcal{C}(\theta_{t})

[103] figure: Algorithm 6 FlashLion: Memory-Efficient Lion. We highlight the changes from Lion. 1: Parameters θ 0 \theta_{0} , learning rate schedule { η t } t = 1 T \{\eta_{t}\}_{t=1}^{T} , β 1 , β 2 ∈ [ 0 , 1 ) \beta_{1},\beta_{2}\in[0,1) , weight decay λ ≥ 0 \lambda\geq 0 , loss ℒ ⁡ ( θ ) \mathcal{L}(\theta) , minibatch sampler ℬ ⁡ ( ⋅ ) \mathcal{B}(\cdot) 2: m 0 q , m 0 s ← 𝒬 m ​ ( 0 ) m_{0}^{q},m_{0}^{s}\leftarrow\mathcal{Q}_{m}(0) 3: θ 0 ′ , ρ 0 ← 𝒞 ⁡ ( θ 0 ) \theta^{\prime}_{0},\rho_{0}\leftarrow\mathcal{C}(\theta_{0}) 4: Initialize t ← 0 t\leftarrow 0 5: while not converged do 6: t ← t + 1 t\leftarrow t+1 7: B t ∼ ℬ B_{t}\sim\mathcal{B} 8: g t ← ∇ θ ℒ ​ ( B t , θ t − 1 ′ ) g_{t}\leftarrow\nabla_{\theta}\mathcal{L}(B_{t};{{\text{\hbox{\pagecolor{SpringGreen}$\theta^{\prime}_{t-1}$}}}}) 9: m t − 1 ← 𝒬 m − 1 ​ ( m t − 1 q , m t − 1 s ) m_{t-1}\leftarrow\mathcal{Q}_{m}^{-1}(m^{q}_{t-1},m^{s}_{t-1}) 10: u t ← sign ⁡ ( β 1 ​ m t − 1 + ( 1 − β 1 ) ​ g t ) u_{t}\leftarrow\mathrm{sign}(\beta_{1}m_{t-1}+(1-\beta_{1})g_{t}) 11: m t ← β 2 ​ m t − 1 + ( 1 − β 2 ) ​ g t m_{t}\leftarrow\beta_{2}m_{t-1}+(1-\beta_{2})g_{t} 12: m t q , m t s ← 𝒬 m ​ ( m t ) m^{q}_{t},m^{s}_{t}\leftarrow\mathcal{Q}_{m}(m_{t}) 13: θ t − 1 ← 𝒞 − 1 ​ ( θ t − 1 ′ , ρ t − 1 ) \theta_{t-1}\leftarrow\mathcal{C}^{-1}(\theta^{\prime}_{t-1},\rho_{t-1}) 14: θ t ← θ t − 1 − η t ​ ( u t + λ ​ θ t − 1 ) \theta_{t}\leftarrow\theta_{t-1}-\eta_{t}(u_{t}+\lambda\theta_{t-1}) 15: θ t ′ , ρ t ← 𝒞 ⁡ ( θ t ) \theta^{\prime}_{t},\rho_{t}\leftarrow\mathcal{C}(\theta_{t})

[104] h2: Appendix B Experimental Details

[105] p: For all our experiments we use the MosaicML Streaming ( MosaicML, 2022 ) library to ensure deterministic data loading for distributed training.

[106] h3: B.1 Image Classification

[107] p: We train the ResNet-50 ( He et al., 2016b ) model using the timm library on the ILSVRC2012 (ImageNet-1K) dataset ( Deng et al., 2009 ) , which contains approximately 1.28 million training images and 50,000 validation images across 1,000 classes. Our implementation of ImageNet follows the standard setup from ( Krizhevsky et al., 2012 ; Simonyan and Zisserman, 2014 ) . The image is resized with its shorter side randomly sampled in [256, 480] for scale augmentation ( Simonyan and Zisserman, 2014 ) . A 224 × 224 crop is randomly sampled from an image or its horizontal flip, and then normalized. For evaluation, the image is first resized to 256 × 256, followed by a 224 × 224 center crop, and then normalized. We initialize the network with Kaiming He initialization ( He et al., 2016a ) and zero-init residuals ( He et al., 2016b ) .

[108] p: We train for 90 epochs with a batch size of 1024, using a 5-epoch linear warmup followed by cosine learning rate decay, following the recommended settings from ( Goyal et al., 2017 ) . We disable weight-decay for biases and BatchNorm layers. We apply label smoothing ( Szegedy et al., 2016 ) with coefficient 0.1. Both reference (FP32 master weights) and FlashOptim use BF16 activations. Table 5 summarizes the hyperparameters we use for training.

[109] figure: Table 5 : Optimizer hyperparameters for ImageNet/ResNet-50. SGD AdamW Learning Rate 1.024 3 × 10 − 3 3\times 10^{-3} Momentum / Betas 0.9 (0.9, 0.999) Weight Decay 3 × 10 − 5 3\times 10^{-5} 3 × 10 − 4 3\times 10^{-4}

[110] h4: Memory and Speed Profiling.

[111] p: Table 6 presents the results of the memory and speed profile for training.

[112] figure: Table 6 : Memory and speed profiling for image classification (ResNet-50). Params Optim Total Step Variant GiB Δ \Delta GiB Δ \Delta GiB Δ \Delta ms SGD Reference 0.10 0.10 0.30 8.4 FlashOptim 0.05 -46% 0.05 -45% 0.17 -45% 9.0 Weight Split 0.05 -46% 0.12 +23% 0.23 -22% 8.7 Opt. Quant. 0.10 0.03 -73% 0.23 -23% 8.7 AdamW Reference 0.10 0.19 0.40 11.9 FlashOptim 0.05 -46% 0.08 -56% 0.20 -50% 12.2 Weight Split 0.05 -46% 0.21 +11% 0.33 -17% 12.1 Opt. Quant. 0.10 0.05 -73% 0.25 -36% 12.6

[113] figure: Figure 6 : Training convergence for image classification (ResNet-50 + AdamW). Comparison of validation accuracy between reference AdamW and FlashAdamW on ImageNet.

[114] p: Figure 6 shows training loss for ResNet-50 with AdamW and FlashAdamW. FlashAdamW produces a nearly identical trajectory to the reference AdamW implementation.

[115] h3: B.2 LLM Pretraining

[116] p: We train the GPT-2 ( Radford et al., 2019 ) (124M) architecture with 12 transformer layers, 12 attention heads, embedding dimension 768, and context length of 1024. We train on the FineWeb10B ( kjj0, 2024 ) dataset, a subset of approximately 10 billion tokens from the FineWeb ( Penedo et al., 2024 ) dataset, tokenized using the GPT-2 BPE tokenizer. We train for 20,000 steps with a batch size of roughly 0.5 million tokens per step. We apply learning rate warmup for the first 700 steps, followed by a cosine decay to 0. The global norm is clipped at 1.0 and a weight decay of 0.1 is used. Weight decay is applied only to 2D parameters (i.e., weight matrices and embeddings), excluding biases and layer normalization parameters. We train in BF16 mixed precision. Table 7 summarizes the optimizer hyperparameters.

[117] figure: Table 7 : Optimizer hyperparameters for GPT-2 124M pretraining. AdamW Lion Learning Rate 6 × 10 − 4 6\times 10^{-4} 2 × 10 − 4 2\times 10^{-4} Betas (0.9, 0.95) (0.9, 0.95)

[118] h4: Memory and Speed Profiling.

[119] p: Table 8 presents the memory and speed profiling results for LLM pretraining.

[120] figure: Table 8 : Memory and speed profiling for LLM pretraining (GPT-2 124M). Params Optim Total Step Variant GiB Δ \Delta GiB Δ \Delta GiB Δ \Delta ms AdamW Reference 0.46 0.93 1.77 5.7 FlashOptim 0.23 -50% 0.36 -61% 0.74 -58% 5.9 Weight Split 0.23 -50% 1.04 +12% 1.43 -20% 5.9 Opt. Quant. 0.46 0.25 -73% 1.08 -39% 5.8 Lion Reference 0.46 0.46 1.30 4.3 FlashOptim 0.23 -50% 0.24 -48% 0.62 -53% 4.5 Weight Split 0.23 -50% 0.58 +25% 0.96 -26% 4.4 Opt. Quant. 0.46 0.12 -73% 0.96 -26% 4.4

[121] figure: Figure 7 : Training convergence for LLM pretraining (GPT-2 + Lion). Comparison of validation loss between reference Lion and FlashLion on FineWeb10B.

[122] p: Figure 7 shows training loss for LLM pretraining with Lion and FlashLion. FlashLion produces a nearly identical trajectory to the reference Lion implementation and closely tracks Lion even after 20,000 parameter updates.

[123] h3: B.3 In-Context Learning Benchmarks

[124] p: We evaluate our pretrained language models on a suite of eight in-context learning ( Brown et al., 2020 ) benchmarks that assess diverse commonsense reasoning and language understanding capabilities:

[125] p: HellaSwag ( Zellers et al., 2019 ) : A sentence completion benchmark requiring physical and temporal commonsense.

[126] p: ARC-Easy ( Clark et al., 2018 ) : The easy subset of the AI2 Reasoning Challenge, containing grade-school science questions.

[127] p: CommonsenseQA ( Talmor et al., 2019 ) : Multiple-choice questions requiring commonsense knowledge from ConceptNet.

[128] p: PIQA ( Bisk et al., 2020 ) : Physical Interaction Question Answering, testing physical commonsense reasoning.

[129] p: OpenBookQA ( Mihaylov et al., 2018 ) : Elementary science questions requiring multi-step reasoning over facts.

[130] p: LAMBADA ( Paperno et al., 2016 ) : Word prediction requiring broad discourse context understanding.

[131] p: Winograd ( Levesque et al., 2012 ) : Pronoun resolution problems requiring commonsense reasoning.

[132] p: BoolQ ( Clark et al., 2019 ) : Naturally occurring yes/no reading comprehension questions.

[133] p: All benchmarks are evaluated in a zero-shot setting.

[134] h3: B.4 LLM Finetuning

[135] p: We fine-tune Llama-3.1-8B ( Dubey et al., 2024 ) on OpenMathInstruct-2 ( Toshniwal et al., 2024 ) . For evaluation, we use GSM8k ( Cobbe et al., 2021 ) , a benchmark of 1,319 grade school math word problems that require multi-step arithmetic reasoning.

[136] h4: Training and Evaluation.

[137] p: We use FSDP2 ( Feng et al., 2022 ) with full parameter sharding and enabled training with activation checkpointing ( Chen et al., 2016 ) applied to every transformer layer. We use the AdamW optimizer, with β 1 = 0.9 \beta_{1}=0.9 and β 2 = 0.95 \beta_{2}=0.95 . The global norm is clipped at 1.0 and a weight decay of 0.1 is used. Weight decay is applied only to weight matrices, excluding biases, embeddings, and layer normalization parameters. We train for 5000 steps with an effective batch size of approximately 5.2 million tokens per step. We apply learning rate warmup for the first 1000 steps, followed by a cosine decay to 0.

[138] p: We evaluate on the GSM8k test set using temperature T = 0.2 T=0.2 decoding. Following standard practice, we extract the final numerical answer from model generations and compare against ground truth.

[139] figure: Figure 8 : Training convergence for LLM finetuning (Llama-3.1-8B + AdamW). Comparison of training loss between reference AdamW and FlashAdamW during supervised finetuning on OpenMathInstruct-2.

[140] h2: Instructions for reporting errors

[141] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[142] p: Tip: You can select the relevant text first, to include it in your report.

[143] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[144] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
