[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Efficient Continual Learning in Language Models via Thalamically Routed Cortical Columns

[3] h6: Abstract

[4] p: Continual learning is a core requirement for deployed language models, yet standard training and fine-tuning pipelines remain brittle under non-stationary data. Online updates often induce catastrophic forgetting, while methods that improve stability frequently increase latency, memory footprint, or dense computation in ways that do not scale well to long contexts. We introduce TRC 2 (Thalamically Routed Cortical Columns), a decoder-only backbone that addresses continual learning at the architectural level. TRC 2 combines sparse thalamic routing over cortical columns with mechanisms for modulation, prediction, memory, and feedback, together with a fast corrective pathway that supports rapid adaptation without destabilizing slower parameters. The resulting block is sparse and chunk-parallel, enabling efficient training and inference while preserving clean ablations of each subsystem. We instantiate a reproducible training and evaluation stack and a continual-learning harness that measures proxy forgetting under streaming domain shifts. Across language modeling and continual learning benchmarks, TRC 2 improves the stability–plasticity tradeoff at comparable compute, enabling rapid on-stream adaptation while preserving previously acquired behavior.

[5] h2: 1 Introduction

[6] p: Large language models are increasingly deployed as long-lived systems that must remain useful under shifting data, shifting user intents, and shifting domains. In practice, this creates a persistent tension: the model must adapt quickly to new distributions while preserving previously learned behavior. The default remedy, periodic retraining or heavy fine-tuning, is expensive and slow. Lightweight updates such as adapters and low-rank tuning reduce cost, but sequential updates still induce interference and forgetting, especially when task boundaries are unclear and storage of prior data is restricted.

[7] p: Recent work has exposed both the opportunity and the limits of current architectures. On the efficiency side, modern state-space models have narrowed the quality gap with Transformers while offering favorable inference scaling; Mamba-3 pushes this line further with improved discretization, richer dynamics, and hardware-aware decoding efficiency Lahoti et al. (2026) . Hybrid designs such as Jamba combine attention and Mamba-like blocks to trade off long-context capability and throughput Lenz et al. (2025) . On the stability side, gating has emerged as a surprisingly powerful primitive: Gated Attention shows that a small, structured modification to attention can improve training stability, reduce attention pathologies, and support long-context extrapolation Qiu et al. (2025a) . At the same time, sparse routing and mixtures introduce their own fragility when the data distribution evolves, motivating careful study of router robustness in continual pre-training Thérien et al. (2025) and new routing schemes for scaling SSMs Zhan et al. (2025) .

[8] p: In parallel, the community has begun to treat adaptation at inference time as a first-class capability. Test-Time Learning for LLMs frames adaptation as input perplexity minimization on unlabeled test streams and shows large gains under distribution shift when updates are constrained to low-rank subspaces Hu et al. (2025) . Model-merging approaches provide a complementary lens: local mixtures constructed via model merging can approximate test-time training while amortizing cost to training time Bertolissi et al. (2025) , and null-space constrained gating can reduce interference during continual merging Qiu et al. (2025b) . These results underscore a key point: useful adaptation signals exist at deployment time, but today they are typically exploited through bolt-on procedures that are not native to the backbone and therefore remain difficult to scale, difficult to stabilize, and hard to compare cleanly across settings.

[9] p: This paper argues that continual learning should be treated as an architectural property. We introduce TRC 2 (Thalamically Routed Cortical Columns), a decoder-only backbone designed around two principles. First, communication should be sparse and controllable, so that new information can be routed to a small subset of computation without globally perturbing the model. Second, plasticity should be localized in fast mechanisms that can update online at low cost, while slower representational structures remain stable and support abstraction across time.

[10] p: TRC 2 implements these principles with a looped layer structure. Each layer contains a thalamic router that selects a top- k k set of cortical columns per token and encourages temporal continuity via a topology-aware prior. Each selected column is a compact microcircuit whose core is a selective state-space update, augmented with explicit excitatory and inhibitory modulation. A cerebellar fast-weight corrector provides a dedicated, low-rank pathway for online updates driven by deployment data, enabling rapid adjustment without rewriting the slow cortical parameters. The resulting layer is linear-time in sequence length within each active column, with constant-time routing overhead, and supports chunked scan implementations that reduce kernel-launch overhead in practice.

[11] p: The architecture is motivated by an empirical gap in current continual learning for LLMs. Replay-free adapter methods such as ELLA show that careful control of update subspaces can substantially reduce forgetting, but they still treat the backbone as a static substrate and rely on external regularizers Biswas et al. (2025) . TRC 2 instead makes interference control and rapid adaptation part of the computation graph through routing, inhibition, and fast weights. This also aligns with recent evidence that local, iterative learning mechanisms can be scaled in deep networks; predictive-coding style training has reached 100+ layer regimes, suggesting that looped correction dynamics need not be confined to toy scales Innocenti et al. (2025) .

[12] p: Our contributions are as follows.

[13] p: We present TRC 2 , a decoder-only backbone for continual learning that combines sparse thalamic top- k k routing over cortical columns with biologically grounded mechanisms for modulation, prediction, memory, feedback, and fast correction.

[14] p: We develop a sparse, chunk-parallel implementation of TRC 2 that supports efficient training and inference on modern accelerators, including topology-aware routing, chunk-level computation, and memory-aware execution with optional activation checkpointing.

[15] p: We provide a reproducible continual-learning evaluation stack with distributed multi-GPU training, standardized logging, and task-wise evaluations that track forgetting and forward transfer under streaming domain shifts. The framework includes targeted ablations and strong baselines, enabling direct analysis of which TRC 2 components drive gains in adaptation and retention.

[16] p: The remainder of the paper details the TRC 2 layer, then evaluates efficiency and adaptation across language modeling and continual learning benchmarks, with direct comparisons to strong Transformer, hybrid, and state space model baselines.

[17] h2: 2 Related Work

[18] p: Continual learning for large language models has expanded from classic task-incremental settings to broader regimes such as continual pre-training, domain-adaptive pre-training, instruction updates, and lifelong knowledge maintenance. Recent surveys organize this space into internal model updates versus external augmentation, and they highlight open evaluation issues that become more severe at scale Zheng et al. (2025) ; Shi et al. (2025) . This framing motivates backbones that are themselves robust to streaming distribution shift, rather than relying only on training-time interventions.

[19] p: A dominant line of work for post-training adaptation constrains updates to small parameter subspaces. DoRA improves low-rank adaptation by decomposing weight updates into magnitude and direction, narrowing the gap to full fine-tuning without changing inference cost Liu et al. (2024) . Other work studies composition across many updates, including gated combinations of LoRA modules Wu et al. (2024) and lifelong mixtures with routing constraints and order sensitivity Wang and Li (2024) . These results suggest that the structure of the update pathway and the routing mechanism both matter for long adaptation sequences.

[20] p: Mixture-of-Experts remains a practical route to higher capacity under bounded per-token compute. DeepSeekMoE studies expert specialization and shared experts to reduce redundancy and improve routing behavior Dai et al. (2024) . LLaMA-MoE shows that dense decoders can be converted into sparse expert systems and recovered through continued pre-training Zhu et al. (2024) . At the tuning stage, sparse expertization can also be made highly parameter-efficient for instruction adaptation Zadouri et al. (2024) . Work on router design, including mixtures of routers, further emphasizes that routing quality is often the limiting factor in sparse systems Zhang et al. (2025) .

[21] p: Efficient sequence backbones have also shifted attention away from dense attention-only designs. Mamba established selective state-space computation as a competitive foundation-model backbone with linear-time sequence processing Gu and Dao (2024) . BlackMamba combines state-space dynamics with sparse experts, showing that routing and recurrent sequence cores can be integrated in one architecture Anthony et al. (2024) . RWKV-family models provide another recurrent path with stronger state parameterization Peng et al. (2024) . At the systems level, FlashAttention-3 highlights how strongly performance depends on kernel-level implementation choices, which is directly relevant when evaluating alternative backbones Shah et al. (2024) .

[22] p: Our design is informed by computational and systems neuroscience as architectural guidance. The predictive branch follows predictive-coding formulations that separate top-down prediction from bottom-up mismatch signals Rao and Ballard (1999) , while the modulation controller is motivated by classical accounts of reward prediction and uncertainty-dependent gain control Schultz et al. (1997) ; Angela and Dayan (2005) . The gated readout is inspired by compartment-specific integration and coincidence effects in cortical pyramidal neurons Larkum et al. (1999) , and is further supported by recent evidence that cortical feedback engages active dendritic processing Fişek et al. (2023) . The routing-weight refinement stage is motivated by reciprocal cortico-thalamic feedback loops that shape thalamic processing Born et al. (2021) . The associative memory pathway uses modern Hopfield retrieval as a differentiable content-addressable memory mechanism Ramsauer et al. (2021) , and is broadly consistent with recent work on systems consolidation and predictive reward representations in hippocampal-cortical circuits Lee et al. (2023) ; Yaghoubi et al. (2026) . We also view recent studies on large-scale neurotransmitter-system organization and biologically grounded learning principles as complementary motivation for structured control signals and local computation in scalable sequence models Hansen et al. (2022) ; Liu et al. (2025) ; Song et al. (2024) .

[23] h2: 3 Method

[24] h3: 3.1 Overview and notation

[25] p: Let x 1 : T x_{1:T} be a token sequence from a vocabulary of size V V . TRC 2 is a decoder-only language model with hidden width d d and L L stacked blocks. For batch size B B and sequence length T T , the hidden representation at layer ℓ \ell is

[26] table: X ( ℓ ) ∈ ℝ B × T × d . X^{(\ell)}\in\mathbb{R}^{B\times T\times d}.

[27] p: Token and position embeddings are learned:

[28] table: X b , t ( 0 ) = E ⁡ [ x b , t ] + P ⁡ [ t ] . X^{(0)}_{b,t}=E[x_{b,t}]+P[t]. (1)

[29] p: Each block uses pre-normalization,

[30] table: U ( ℓ ) = RMSNorm ⁡ ( X ( ℓ ) ) . U^{(\ell)}=\mathrm{RMSNorm}(X^{(\ell)}). (2)

[31] p: TRC 2 1 combines chunk-level sparse routing, a routed cortical computation, an optional modulation and predictive pathway, an optional associative memory with top-down gating, an optional routing-weight refinement step, and an optional low-rank corrective path. Each subsystem is independently toggleable. Implementation details that are useful for exact reproduction, including padding and tensor layouts, are summarized in Appendix A .

[32] figure: Figure 1: TRC 2 architecture block.

[33] h3: 3.2 Block computation

[34] p: For one block, let X ∈ ℝ B × T × d X\in\mathbb{R}^{B\times T\times d} be the input and let X + X^{+} denote the output. The core computation is

[35] table: U \displaystyle U = RMSNorm ⁡ ( X ) , \displaystyle=\mathrm{RMSNorm}(X), (3) ( s route , s pred , s gain ) \displaystyle(s_{\mathrm{route}},s_{\mathrm{pred}},s_{\mathrm{gain}}) = ModCtrl ⁡ ( U ) , \displaystyle=\mathrm{ModCtrl}(U), (4) U ^ , ℒ pred \displaystyle\hat{U},\mathcal{L}_{\mathrm{pred}} = PredictivePath ⁡ ( U , s pred ) , \displaystyle=\mathrm{PredictivePath}(U,s_{\mathrm{pred}}), (5) ( I , R , S , ℒ route ) \displaystyle(I,R,S,\mathcal{L}_{\mathrm{route}}) = Router ⁡ ( U ^ ) , \displaystyle=\mathrm{Router}(\hat{U}), (6) C mem \displaystyle C^{\mathrm{mem}} = AssocMem ⁡ ( U ¯ ) , \displaystyle=\mathrm{AssocMem}(\bar{U}), (7) Y \displaystyle Y = Cortex ⁡ ( U ^ , I , R , C mem ) , \displaystyle=\mathrm{Cortex}(\hat{U},I,R,C^{\mathrm{mem}}), (8) R ′ \displaystyle R^{\prime} = RefineWeights ⁡ ( Y , I , S ) , \displaystyle=\mathrm{RefineWeights}(Y,I,S), (9) Y \displaystyle Y ← Cortex ( U ^ , I , R ′ , C mem ) if refinement is enabled , \displaystyle\leftarrow\mathrm{Cortex}(\hat{U},I,R^{\prime},C^{\mathrm{mem}})\quad\text{if refinement is enabled}, (10) Δ \displaystyle\Delta = Corrector ⁡ ( U ^ , Y ) , \displaystyle=\mathrm{Corrector}(\hat{U},Y), (11) Y \displaystyle Y ← g gain ⊙ Y (if modulation is enabled) , \displaystyle\leftarrow g_{\mathrm{gain}}\odot Y\quad\text{(if modulation is enabled)}, (12) X ~ \displaystyle\tilde{X} = X + Drop ⁡ ( Y + Δ ) , \displaystyle=X+\mathrm{Drop}(Y+\Delta), (13) X + \displaystyle X^{+} = X ~ + Drop ⁡ ( SwiGLU ⁡ ( RMSNorm ⁡ ( X ~ ) ) ) . \displaystyle=\tilde{X}+\mathrm{Drop}\!\left(\mathrm{SwiGLU}\!\left(\mathrm{RMSNorm}(\tilde{X})\right)\right). (14)

[36] p: Here I I are top- k k routed column indices, R R are routing mixture weights, and S S are the selected router logits used by the refinement step. The block returns X + X^{+} together with auxiliary terms ℒ route \mathcal{L}_{\mathrm{route}} and, when enabled, ℒ pred \mathcal{L}_{\mathrm{pred}} .

[37] h3: 3.3 Modulation controller and predictive pathway

[38] h4: Modulation controller.

[39] p: When enabled, the controller outputs three sequence-level scalars in [ 0 , 1 ] [0,1] : a routing-control signal s route s_{\mathrm{route}} , a predictive-blend signal s pred s_{\mathrm{pred}} , and a global-gain signal s gain s_{\mathrm{gain}} . The controller is a small MLP that operates on per-sequence statistics of U U together with deviations from running exponential moving averages:

[40] table: μ b \displaystyle\mu_{b} = 1 T ∑ t = 1 T U b , t , : , σ b = Std t ( U b , t , : ) , \displaystyle=\frac{1}{T}\sum_{t=1}^{T}U_{b,t,:},\qquad\sigma_{b}=\mathrm{Std}_{t}(U_{b,t,:}), (15) d b μ \displaystyle d^{\mu}_{b} = | μ b − μ ema | , d b σ = | σ b − v ema | . \displaystyle=|\mu_{b}-\mu_{\mathrm{ema}}|,\qquad d^{\sigma}_{b}=\left|\sigma_{b}-\sqrt{v_{\mathrm{ema}}}\right|. (16)

[41] p: The concatenated vector [ μ b ; σ b ; d b μ ; d b σ ] ∈ ℝ 4 ​ d [\mu_{b};\sigma_{b};d^{\mu}_{b};d^{\sigma}_{b}]\in\mathbb{R}^{4d} is passed through a two-layer MLP with SiLU and sigmoid to produce the three control signals. The implementation broadcasts these signals across token positions and channels.

[42] h4: Predictive pathway.

[43] p: When enabled, the block predicts each normalized token representation from its left context using a causal depthwise 1D convolution followed by a pointwise 1D convolution:

[44] table: P ^ ∈ ℝ B × T × d . \hat{P}\in\mathbb{R}^{B\times T\times d}. (17)

[45] p: The convolution is implemented with left padding and a one-step shift so that position t t depends only on positions < t <t (Appendix A.1 ).

[46] p: The predictive auxiliary loss is

[47] table: ℒ pred = λ pc MSE ( P ^ : , 2 : T , : , stopgrad ( U : , 2 : T , : ) ) . \mathcal{L}_{\mathrm{pred}}=\lambda_{\mathrm{pc}}\,\mathrm{MSE}\!\left(\hat{P}_{:,2:T,:},\mathrm{stopgrad}(U_{:,2:T,:})\right). (18)

[48] p: The predictor enters the block through a controller-weighted prediction-error blend:

[49] table: U ^ = U − ( 1 − s pred ) ​ P ~ , \hat{U}=U-(1-s_{\mathrm{pred}})\,\tilde{P}, (19)

[50] p: where P ~ \tilde{P} is either P ^ \hat{P} or stopgrad ⁡ ( P ^ ) \mathrm{stopgrad}(\hat{P}) depending on whether gradient flow through the predictive branch is enabled. If the modulation controller is disabled, the implementation uses the fixed value s pred = 0.5 s_{\mathrm{pred}}=0.5 .

[51] h3: 3.4 Chunked sparse routing

[52] p: Routing is computed at chunk resolution. Let C C be the routing chunk size and n c = ⌈ T / C ⌉ n_{c}=\lceil T/C\rceil . The sequence is padded by repeating the last representation if needed, reshaped to

[53] table: U ^ chunk ∈ ℝ B × n c × C × d , \hat{U}_{\mathrm{chunk}}\in\mathbb{R}^{B\times n_{c}\times C\times d},

[54] p: and pooled within each chunk:

[55] table: U ¯ b , c = { U ^ chunk [ b , c , 1 , : ] (first-position pooling) , 1 C ∑ τ = 1 C U ^ chunk [ b , c , τ , : ] (mean pooling) . \bar{U}_{b,c}=\begin{cases}\hat{U}_{\mathrm{chunk}}[b,c,1,:]&\text{(first-position pooling)},\\[3.0pt] \frac{1}{C}\sum_{\tau=1}^{C}\hat{U}_{\mathrm{chunk}}[b,c,\tau,:]&\text{(mean pooling)}.\end{cases} (20)

[56] p: The exact padding and chunking behavior is given in Appendix A.2 .

[57] h4: Router logits.

[58] p: Given router width d r d_{r} and M M columns, the router computes

[59] table: Q \displaystyle Q = U ¯ ​ W q ( r ) ∈ ℝ B × n c × d r , \displaystyle=\bar{U}W_{q}^{(r)}\in\mathbb{R}^{B\times n_{c}\times d_{r}}, (21) K ( r ) \displaystyle K^{(r)} ∈ ℝ M × d r , \displaystyle\in\mathbb{R}^{M\times d_{r}}, (22) L b , c , m base \displaystyle L^{\mathrm{base}}_{b,c,m} = ⟨ Q b , c , : , K m , : ( r ) ⟩ . \displaystyle=\langle Q_{b,c,:},K^{(r)}_{m,:}\rangle. (23)

[60] h4: Topology-aware prior.

[61] p: When enabled, the router predicts a 2D coordinate for each chunk,

[62] table: π b , c = tanh ⁡ ( U ¯ b , c ​ W pos + b pos ) ∈ ℝ 2 , \pi_{b,c}=\tanh(\bar{U}_{b,c}W_{\mathrm{pos}}+b_{\mathrm{pos}})\in\mathbb{R}^{2}, (24)

[63] p: and applies a distance penalty to fixed column coordinates P m ∈ ℝ 2 P_{m}\in\mathbb{R}^{2} :

[64] table: L b , c , m topo = − γ ​ ‖ π b , c − P m ‖ 2 2 . L^{\mathrm{topo}}_{b,c,m}=-\gamma\|\pi_{b,c}-P_{m}\|_{2}^{2}. (25)

[65] p: The column coordinates form a grid when M M is a square and a circle otherwise.

[66] h4: Routing-logit modulation and top- k k selection.

[67] p: When the modulation controller is enabled, the router scales logits by a sequence-level factor:

[68] table: a route = 1 + ρ route ​ ( 2 ​ s route − 1 ) , a_{\mathrm{route}}=1+\rho_{\mathrm{route}}(2s_{\mathrm{route}}-1), (26)

[69] p: and uses

[70] table: L b , c , m = a route ​ ( L b , c , m base + 𝟏 topo ​ L b , c , m topo ) . L_{b,c,m}=a_{\mathrm{route}}\left(L^{\mathrm{base}}_{b,c,m}+\mathbf{1}_{\mathrm{topo}}L^{\mathrm{topo}}_{b,c,m}\right). (27)

[71] p: The router then selects top- k k columns per chunk,

[72] table: I b , c , 1 : k = TopK ( L b , c , : , k ) , I_{b,c,1:k}=\mathrm{TopK}(L_{b,c,:},k), (28)

[73] p: and forms routing weights by a softmax on the selected logits:

[74] table: R b , c , j = exp ⁡ ( L b , c , I b , c , j ) ∑ j ′ = 1 k exp ⁡ ( L b , c , I b , c , j ′ ) . R_{b,c,j}=\frac{\exp(L_{b,c,I_{b,c,j}})}{\sum_{j^{\prime}=1}^{k}\exp(L_{b,c,I_{b,c,j^{\prime}}})}. (29)

[75] p: The selected pre-softmax values

[76] table: S b , c , j = L b , c , I b , c , j S_{b,c,j}=L_{b,c,I_{b,c,j}}

[77] p: are retained for the routing-weight refinement step.

[78] h4: Routing auxiliary loss.

[79] p: When routing regularization is enabled, the implementation accumulates the top- k k routing mass back into a dense ( B , n c , M ) (B,n_{c},M) tensor and applies the quadratic penalty

[80] table: ℒ route = λ lb ​ M ​ ∑ m = 1 M p m 2 , \mathcal{L}_{\mathrm{route}}=\lambda_{\mathrm{lb}}\,M\sum_{m=1}^{M}p_{m}^{2}, (30)

[81] p: where p m p_{m} is the normalized routing mass assigned to column m m across the batch and chunks (Appendix A.2 ).

[82] h3: 3.5 Associative memory and routed cortical computation

[83] h4: Associative memory (optional).

[84] p: The associative-memory module operates on chunk summaries U ¯ ∈ ℝ B × n c × d \bar{U}\in\mathbb{R}^{B\times n_{c}\times d} using a Modern Hopfield retrieval. It stores n s n_{s} learnable slots

[85] table: Ξ ∈ ℝ n s × d h , \Xi\in\mathbb{R}^{n_{s}\times d_{h}},

[86] p: normalizes both projected chunk queries and slots, and retrieves

[87] table: C mem ∈ ℝ B × n c × d . C^{\mathrm{mem}}\in\mathbb{R}^{B\times n_{c}\times d}. (31)

[88] p: This retrieved context is used both in the readout stage and in chunk-level lateral propagation. The exact retrieval equations are listed in Appendix A.4 .

[89] h4: Routed cortical computation.

[90] p: The cortex reuses the chunk-level routing decisions ( I , R ) (I,R) for all tokens in the chunk. A dense projection maps each padded token to column-specific parameters:

[91] table: Proj ⁡ ( U ^ b , t ) ∈ ℝ M ⁡ ( 3 ​ n + 3 ) , \mathrm{Proj}(\hat{U}_{b,t})\in\mathbb{R}^{M(3n+3)}, (32)

[92] p: where n n is the cortical state width. After reshaping to ( B , n c , C , M , 3 ​ n + 3 ) (B,n_{c},C,M,3n+3) and gathering the selected columns, the block obtains

[93] table: δ , B in , C in ∈ ℝ B × n c × C × k × n , \delta,\;B_{\mathrm{in}},\;C_{\mathrm{in}}\in\mathbb{R}^{B\times n_{c}\times C\times k\times n},

[94] p: and three gate tensors

[95] table: g state , g out , g dis ∈ ( 0 , 1 ) B × n c × C × k . g_{\mathrm{state}},\;g_{\mathrm{out}},\;g_{\mathrm{dis}}\in(0,1)^{B\times n_{c}\times C\times k}.

[96] p: When excitatory-inhibitory gating is enabled, the third gate acts as a disinhibitory controller:

[97] table: g state \displaystyle g_{\mathrm{state}} ← ( 1 − g dis ) ​ g state + g dis , \displaystyle\leftarrow(1-g_{\mathrm{dis}})\,g_{\mathrm{state}}+g_{\mathrm{dis}}, (33) g out \displaystyle g_{\mathrm{out}} ← ( 1 − g dis ) ​ g out + g dis . \displaystyle\leftarrow(1-g_{\mathrm{dis}})\,g_{\mathrm{out}}+g_{\mathrm{dis}}. (34)

[98] p: The state-related tensors are then scaled by g state g_{\mathrm{state}} .

[99] p: Next, the block forms a token-dependent coefficient from the projected state parameters and a learned per-column tensor A log ∈ ℝ M × n A_{\log}\in\mathbb{R}^{M\times n} :

[100] table: A base \displaystyle A_{\mathrm{base}} = σ ⁡ ( − A log ) , \displaystyle=\sigma(-A_{\log}), (35) α \displaystyle\alpha = σ ⁡ ( δ ) ⊙ A sel , \displaystyle=\sigma(\delta)\odot A_{\mathrm{sel}}, (36) D state \displaystyle D_{\mathrm{state}} = ( 1 − α ) ⊙ B in . \displaystyle=(1-\alpha)\odot B_{\mathrm{in}}. (37)

[101] p: A causal depthwise 1D convolution followed by a pointwise 1D convolution is applied along the within-chunk token axis, producing a filtered state tensor

[102] table: H ∈ ℝ B × n c × C × k × n . H\in\mathbb{R}^{B\times n_{c}\times C\times k\times n}.

[103] p: This is a chunk-causal operation. Cross-chunk propagation is handled later by a separate chunk-level convolution.

[104] h4: Readout, output gating, and routed mixture.

[105] p: The bottom-up readout input is

[106] table: B read = C in ⊙ H . B_{\mathrm{read}}=C_{\mathrm{in}}\odot H. (38)

[107] p: If the top-down gated readout is enabled and associative memory is active, the code uses a two-branch readout:

[108] table: S read \displaystyle S_{\mathrm{read}} = W bot ​ B read , \displaystyle=W_{\mathrm{bot}}B_{\mathrm{read}}, (39) G top \displaystyle G_{\mathrm{top}} = σ ⁡ ( W gate ​ ϕ ​ ( W top ​ C bcast mem ) ) , \displaystyle=\sigma\!\left(W_{\mathrm{gate}}\,\phi(W_{\mathrm{top}}C^{\mathrm{mem}}_{\mathrm{bcast}})\right), (40) Y sel \displaystyle Y_{\mathrm{sel}} = RMSNorm ⁡ ( S read ⊙ ( 1 + G top ) ) , \displaystyle=\mathrm{RMSNorm}\!\left(S_{\mathrm{read}}\odot(1+G_{\mathrm{top}})\right), (41)

[109] p: where C bcast mem C^{\mathrm{mem}}_{\mathrm{bcast}} denotes the chunk-level memory retrieval broadcast across token and selected-column axes, and ϕ \phi is SiLU. Otherwise, the block uses a linear readout:

[110] table: Y sel = W out ​ B read . Y_{\mathrm{sel}}=W_{\mathrm{out}}B_{\mathrm{read}}. (42)

[111] p: The selected-column outputs are then scaled by the output-control gate:

[112] table: Y sel ← Y sel ⊙ g out . Y_{\mathrm{sel}}\leftarrow Y_{\mathrm{sel}}\odot g_{\mathrm{out}}. (43)

[113] p: If the skip connection is enabled, a learned scalar coefficient per selected column adds a gated skip from the chunk input:

[114] table: Y sel ← Y sel + tanh ⁡ ( s I ) ⊙ U ^ chunk . Y_{\mathrm{sel}}\leftarrow Y_{\mathrm{sel}}+\tanh(s_{I})\odot\hat{U}_{\mathrm{chunk}}. (44)

[115] p: The routed chunk output is the weighted sum

[116] table: Y chunk [ b , c , τ , : ] = ∑ j = 1 k R b , c , j Y sel [ b , c , τ , j , : ] . Y_{\mathrm{chunk}}[b,c,\tau,:]=\sum_{j=1}^{k}R_{b,c,j}\,Y_{\mathrm{sel}}[b,c,\tau,j,:]. (45)

[117] h4: Chunk-level lateral propagation.

[118] p: The cortex forms chunk summaries

[119] table: C ctx [ b , c , : ] = 1 C ∑ τ = 1 C Y chunk [ b , c , τ , : ] , C_{\mathrm{ctx}}[b,c,:]=\frac{1}{C}\sum_{\tau=1}^{C}Y_{\mathrm{chunk}}[b,c,\tau,:], (46)

[120] p: optionally adds the associative-memory retrieval C mem C^{\mathrm{mem}} , and applies a causal depthwise-plus-pointwise convolution along the chunk axis. The resulting chunk signal is broadcast back to all token positions in the chunk and added to Y chunk Y_{\mathrm{chunk}} . The final cortex output Y ∈ ℝ B × T × d Y\in\mathbb{R}^{B\times T\times d} is obtained after reshaping and removing padding. Appendix A.3 gives the exact tensorized implementation and the activation-checkpointing option used to reduce memory.

[121] h3: 3.6 Routing-weight refinement and low-rank corrective path

[122] h4: Routing-weight refinement (optional).

[123] p: After a first cortex pass, the block can refine routing weights without recomputing top- k k indices. The cortex output is pooled to chunk summaries, projected back to router space, and scored against the router keys to obtain feedback logits. The code gathers only the logits for the already-selected columns and mixes them with the original selected router logits:

[124] table: R b , c , : ′ = softmax ( S b , c , : + α fb S b , c , : fb ) , α fb = tanh ( c mix ) ∈ ( − 1 , 1 ) . R^{\prime}_{b,c,:}=\mathrm{softmax}\!\left(S_{b,c,:}+\alpha_{\mathrm{fb}}\,S^{\mathrm{fb}}_{b,c,:}\right),\qquad\alpha_{\mathrm{fb}}=\tanh(c_{\mathrm{mix}})\in(-1,1). (47)

[125] p: The cortex is then executed a second time with the same indices I I and refined weights R ′ R^{\prime} . This is a full second cortex pass over the fixed routing support, not a post-hoc reweighting of cached outputs (Appendix A.4 ).

[126] h4: Low-rank corrective path (optional).

[127] p: The corrective path computes a low-rank residual from the normalized block input and cortex output. Let d z d_{z} be the intermediate width and r r the low-rank width. The implementation uses a split linear map (equivalent to a single linear layer on [ U ^ ; Y ] [\hat{U};Y] ):

[128] table: Z pre = U ^ ​ ( W z ( 1 ) ) ⊤ + Y ​ ( W z ( 2 ) ) ⊤ + b z , Z = ϕ ⁡ ( Z pre ) , Z_{\mathrm{pre}}=\hat{U}(W^{(1)}_{z})^{\top}+Y(W^{(2)}_{z})^{\top}+b_{z},\qquad Z=\phi(Z_{\mathrm{pre}}), (48)

[129] p: with ϕ = SiLU \phi=\mathrm{SiLU} . The low-rank correction is

[130] table: Δ b , t , q = ∑ p = 1 d z ∑ r ′ = 1 r Z b , t , p ​ V p , r ′ ​ U q , r ′ . \Delta_{b,t,q}=\sum_{p=1}^{d_{z}}\sum_{r^{\prime}=1}^{r}Z_{b,t,p}\,V_{p,r^{\prime}}\,U_{q,r^{\prime}}. (49)

[131] p: If this path is disabled, the block sets Δ = 0 \Delta=0 .

[132] h3: 3.7 Global gain modulation, output head, and training objective

[133] p: When the modulation controller is enabled, the block applies a sequence-level gain to the cortex output before the residual update:

[134] table: g gain = 1 + ρ gain ​ ( 2 ​ s gain − 1 ) , Y ← g gain ⊙ Y , g_{\mathrm{gain}}=1+\rho_{\mathrm{gain}}(2s_{\mathrm{gain}}-1),\qquad Y\leftarrow g_{\mathrm{gain}}\odot Y, (50)

[135] p: with broadcasting over token and feature dimensions.

[136] p: After L L blocks, the model applies a final RMS normalization and a tied output projection:

[137] table: logits = LMHead ⁡ ( RMSNorm ⁡ ( X ( L ) ) ) ∈ ℝ B × T × V . \mathrm{logits}=\mathrm{LMHead}\!\left(\mathrm{RMSNorm}(X^{(L)})\right)\in\mathbb{R}^{B\times T\times V}. (51)

[138] p: Each block may produce a routing auxiliary regularizer and a predictive reconstruction loss. The wrapper accumulates these terms across layers:

[139] table: ℒ route Σ = ∑ ℓ = 1 L ℒ route ( ℓ ) , ℒ pred Σ = ∑ ℓ = 1 L ℒ pred ( ℓ ) . \mathcal{L}_{\mathrm{route}}^{\Sigma}=\sum_{\ell=1}^{L}\mathcal{L}_{\mathrm{route}}^{(\ell)},\qquad\mathcal{L}_{\mathrm{pred}}^{\Sigma}=\sum_{\ell=1}^{L}\mathcal{L}_{\mathrm{pred}}^{(\ell)}. (52)

[140] p: The wrapper computes token cross-entropy ℒ CE \mathcal{L}_{\mathrm{CE}} from logits and labels . In the provided trainer, the total objective is

[141] table: ℒ train = ℒ CE + 0.1 ​ ℒ pred Σ + ℒ route Σ , \mathcal{L}_{\mathrm{train}}=\mathcal{L}_{\mathrm{CE}}+0.1\,\mathcal{L}_{\mathrm{pred}}^{\Sigma}+\mathcal{L}_{\mathrm{route}}^{\Sigma}, (53)

[142] p: with fixed coefficients (Appendix A.5 ).

[143] p: A detailed complexity analysis of TRC 2 is provided in Appendix B .

[144] h2: 4 Experiments and Results

[145] h3: 4.1 Experimental setup

[146] p: We evaluate TRC 2 as a drop-in decoder-only language modeling backbone under two requirements: (i) competitive next-token modeling and efficiency, and (ii) stable adaptation under streaming shifts without task boundaries. All experiments run on a single node with 4 × \times NVIDIA V100 (32GB) using mixed precision.

[147] h4: Training data.

[148] p: For dense pre-training style runs we use C4 Raffel et al. (2020) , a large web corpus that approximates evolving deployment text; we train either in streaming mode (to model non-stationary inputs) or from a cached snapshot for controlled comparisons. For held-out perplexity we evaluate on wikitext-103-v1 Merity et al. (2017) and LAMBADA Paperno et al. (2016) as fixed anchors: WikiText is a curated Wikipedia benchmark that is sensitive to over-specialization, while LAMBADA probes discourse-level, long-context prediction. Together these evaluations help quantify the stability side of the stability–plasticity tradeoff while the model adapts.

[149] h4: Models and baselines.

[150] p: We compare TRC 2 against parameter-matched Transformer, and Mamba decoder baselines trained under the same pipeline.

[151] h4: Training and evaluation protocol.

[152] p: All experiments run on a single node with 4 NVIDIA V100 GPUs (32GB) using distributed data parallelism and mixed precision. We use batch size 8 per GPU, gradient accumulation over 4 micro-steps, and sequence length 1024, giving an effective global batch of 128 sequences (131,072 tokens) per optimizer step. Unless stated otherwise, runs use AdamW with learning rate 2 × 10 − 4 2\times 10^{-4} , weight decay 0.1 0.1 , ( β 1 , β 2 ) = ( 0.9 , 0.95 ) (\beta_{1},\beta_{2})=(0.9,0.95) , 1,000 warmup steps, cosine decay, and gradient clipping at 1.0. The main training budget is 22,000 optimizer steps, which corresponds to 2,883,584,000 tokens (approximately 2.88B). Training uses streaming C4 with the GPT-NeoX tokenizer and context length 1024. Evaluation is performed every 500 optimizer steps on fixed validation probes (C4, WikiText, and LAMBADA). Full configuration details, including tokenizer, data caps, logging, and checkpoint selection, are listed in Appendix A.6 .

[153] h4: Metrics.

[154] p: We report (i) held-out loss and perplexity, (ii) efficiency metrics including end-to-end throughput (tokens/s and sequences/s) and peak memory, and (iii) continual-learning metrics computed over the validation probes treated as a task stream. For continual evaluation, we maintain a historical best value for each probe and report a forgetting proxy: for lower-is-better metrics (such as perplexity), forgetting is the increase from the best-so-far value; for higher-is-better metrics (such as token accuracy or BLEU), forgetting is the drop from the best-so-far value; in both cases, values are clipped at zero. We report mean forgetting across probes together with aggregate best-task and worst-task summaries. The evaluation pipeline can also compute teacher-forced text metrics from arg ⁡ max \arg\max predictions on labeled positions, including token accuracy, exact match, BLEU, chrF, and ROUGE (when available). Additional implementation details for metric computation and trainer-side aggregation are summarized in Appendix A .

[155] h3: 4.2 Results

[156] p: Table 1 reports held-out perplexity, Bleu score, and throughput. Table 2 summarizes continual learning on a streaming task suite.

[157] figure: Table 1: Evaluation performance and efficiency compared to baselines; tokens/s measured during steady-state training. d m d_{m} and n b n_{b} represent model depth and the number of t ​ r ​ c 2 trc^{2} blocks, respectively. Wiki and LAM represent WikiText, and LAMBADA datasets respectively. Model Params d m d_{m} n b n_{b} PPL ↓ \downarrow Bleu ↑ \uparrow Tokens/s ↑ \uparrow Mem × H ​ o ​ u ​ r GPU ↓ \frac{\mathrm{Mem}\times Hour}{\mathrm{GPU}}\ \downarrow c4 Wiki LAM c4 Wiki LAM Transformer 162M 768 13 60.70 215.18 105.72 8.12 8.23 5.09 ∼ \sim 127000 𝟏𝟏𝟖 ​ 𝐆𝐁 ⋅ 𝐡 118\,\mathrm{GB\cdot h} Mamba 176M 768 11 70.45 357.67 116.73 6.90 2.87 3.97 ∼ \sim 108000 178 ​ GB ⋅ h 178\,\mathrm{GB\cdot h} TRC 2 (ours) 169M 512 8 2.00 2.56 2.02 71.66 66.57 70.07 ∼ \sim 57000 268 ​ GB ⋅ h 268\,\mathrm{GB\cdot h}

[158] figure: Table 2: Continual-learning evaluation on a streaming tasks. Avg Forgetting is the mean increase in PPL (or decrease in token accuracy, bleu score) relative to the best-so-far per task after each update. Model Params d m d_{m} n b n_{b} Average forgetting - last step ↓ \downarrow Average forgetting - normalized AUC ↓ \downarrow PPL t ​ o ​ k ​ e ​ n a ​ c ​ c token_{acc} Bleu PPL t ​ o ​ k ​ e ​ n a ​ c ​ c token_{acc} Bleu Transformer 162M 768 13 0.0000 0.0014 0.3757 0.0669 0.0008 0.1684 Mamba 176M 768 11 0.0000 0.0006 0.0900 0.3371 0.0011 0.1957 TRC 2 (ours) 169M 512 8 0.0110 0.0010 0.0435 0.0018 0.0008 0.0981

[159] h2: 5 Discussion

[160] p: The results support the main design claim of TRC 2 : continual learning can be improved by allocating plasticity to a small, explicit pathway while keeping most representational structure stable. In Table 2 , TRC 2 shows markedly lower normalized forgetting area under the curve on perplexity and Bleu than the baselines, which indicates that the model retains earlier behavior more consistently over the full stream rather than only at the end of training. At the same time, the last-step forgetting values suggest that stability is not achieved by freezing learning entirely, since the model continues to move and occasionally pays a small short-term cost in some probes.

[161] p: From an efficiency perspective, TRC 2 trades throughput for structured sparsity and online-correctable computation. Table 1 shows lower tokens/s than the dense Transformer baseline in this implementation. This is consistent with additional routing, gathering, and per-column computation. The chunked routing scheme helps amortize router overhead, but end to end performance is still sensitive to kernel fusion, memory layout, and the fraction of active columns. In practice, the favorable scaling regime appears when routing decisions are stable across neighboring tokens and when the implementation can keep column-local scans contiguous in memory.

[162] p: Several mechanisms likely contribute to the observed stability trend. Topology-aware routing encourages temporal continuity in column selection, which can reduce parameter interference by keeping related updates localized. The excitatory-inhibitory gating provides a simple control handle that can suppress unstable activations before they propagate through residual pathways. The corrective path offers a fast route for stream-driven adjustment without rewriting slower parameters, which is aligned with the continual-learning objective used in training. A limitation of the current study is robustness under sharper distribution shifts, longer contexts, and more frequent regime changes, where routers can become brittle and chunk summaries may lose fine-grained signals.

[163] h2: 6 Conclusion

[164] p: This work introduced TRC 2 , a decoder-only backbone that targets continual learning through architectural separation of stable representation, sparse routed computation, and a low-rank corrective pathway for rapid updates. The model combines chunk-level top- k k routing over cortical columns with modulation, prediction, associative memory, feedback refinement, and fast correction, while retaining a systems-friendly, chunk-parallel execution strategy. Empirically, TRC 2 demonstrates improved retention over a streaming evaluation suite as reflected by lower accumulated proxy forgetting, while maintaining competitive held-out behavior under the same training pipeline and domain shifts.

[165] p: The results suggest that continual learning can benefit from making interference control part of the forward computation rather than relying only on external fine-tuning procedures. Future work should extend the evaluation to larger scales and longer contexts, and study router stability under harder non-stationary streams. A promising direction is to couple the corrective pathway with deployment-time constraints, so adaptation can be bounded, interpretable, and reversible when the stream contains noisy or adversarial segments.

[166] h2: References

[167] h2: Appendix A Technical Derivations and Implementation Details

[168] p: This appendix records implementation details needed for exact reproduction and clarifies points that are easy to misread from the compact method description. It also summarizes the optimization protocol and the ablation controls exposed by the code.

[169] p: We log full run configurations and metrics to Weights & Biases.

[170] h3: A.1 Predictive pathway: causal one-step-ahead convolution

[171] p: The predictive pathway operates on the normalized token representation

[172] table: U ∈ ℝ B × T × d , U\in\mathbb{R}^{B\times T\times d},

[173] p: and uses a depthwise 1D convolution followed by a pointwise 1D convolution. Let

[174] table: U ⊤ ∈ ℝ B × d × T U^{\top}\in\mathbb{R}^{B\times d\times T}

[175] p: denote the channel-first view used by the implementation. Let the depthwise kernel width be k pc k_{\mathrm{pc}} .

[176] p: The code implements a causal one-step-ahead predictor by left-padding by k pc k_{\mathrm{pc}} , applying the depthwise convolution, and then dropping the final output position:

[177] table: U ~ = DWConv pc ( PadLeft ( U ⊤ , k pc ) ) : , : , 1 : T . \widetilde{U}=\mathrm{DWConv}_{\mathrm{pc}}\!\left(\mathrm{PadLeft}(U^{\top},k_{\mathrm{pc}})\right)_{:,:,1:T}. (A.1)

[178] p: A pointwise convolution then produces the predictor output

[179] table: P ^ ⊤ = PWConv pc ​ ( U ~ ) , P ^ ∈ ℝ B × T × d . \hat{P}^{\top}=\mathrm{PWConv}_{\mathrm{pc}}(\widetilde{U}),\qquad\hat{P}\in\mathbb{R}^{B\times T\times d}. (A.2)

[180] p: The predictive reconstruction loss used by the block is

[181] table: ℒ pred = λ pc ⋅ MSE ( P ^ : , 2 : T , : , stopgrad ( U : , 2 : T , : ) ) , \mathcal{L}_{\mathrm{pred}}=\lambda_{\mathrm{pc}}\cdot\mathrm{MSE}\!\left(\hat{P}_{:,2:T,:},\mathrm{stopgrad}(U_{:,2:T,:})\right), (A.3)

[182] p: The predictive blend used as cortex input is

[183] table: U ^ = U − ( 1 − s pred ) ​ P ~ , \hat{U}=U-(1-s_{\mathrm{pred}})\,\tilde{P}, (A.4)

[184] p: where

[185] table: P ~ = { P ^ , if predictive blending allows gradient flow , stopgrad ⁡ ( P ^ ) , otherwise . \tilde{P}=\begin{cases}\hat{P},&\text{if predictive blending allows gradient flow},\\ \mathrm{stopgrad}(\hat{P}),&\text{otherwise}.\end{cases}

[186] p: If the modulation controller is disabled, the implementation uses the fixed blending value

[187] table: s pred = 0.5 . s_{\mathrm{pred}}=0.5.

[188] h3: A.2 Chunked routing and padded execution

[189] p: Routing is performed at chunk resolution. Let C C be the routing chunk size and

[190] table: n c = ⌈ T C ⌉ . n_{c}=\left\lceil\frac{T}{C}\right\rceil.

[191] p: If T T is not divisible by C C , the code pads by repeating the last valid token representation:

[192] table: U ^ pad = { U ^ , if ​ T = n c ​ C , [ U ^ ; U ^ : , T , : repeated ( n c C − T ) times ] , otherwise , \hat{U}_{\mathrm{pad}}=\begin{cases}\hat{U},&\text{if }T=n_{c}C,\\[2.0pt] \big[\hat{U};\ \hat{U}_{:,T,:}\ \text{repeated}\ (n_{c}C-T)\ \text{times}\big],&\text{otherwise},\end{cases} (A.5)

[193] p: then reshapes to

[194] table: U ^ chunk ∈ ℝ B × n c × C × d . \hat{U}_{\mathrm{chunk}}\in\mathbb{R}^{B\times n_{c}\times C\times d}.

[195] p: This padding choice matters because the padded values are not zeros.

[196] p: Chunk summaries are computed by either first-position pooling or mean pooling:

[197] table: U ¯ b , c = { U ^ chunk [ b , c , 1 , : ] (first-position pooling) , 1 C ∑ τ = 1 C U ^ chunk [ b , c , τ , : ] (mean pooling) . \bar{U}_{b,c}=\begin{cases}\hat{U}_{\mathrm{chunk}}[b,c,1,:]&\text{(first-position pooling)},\\[3.0pt] \frac{1}{C}\sum_{\tau=1}^{C}\hat{U}_{\mathrm{chunk}}[b,c,\tau,:]&\text{(mean pooling)}.\end{cases} (A.6)

[198] h4: Router logits and topology term.

[199] p: Let d r d_{r} denote the router width and let M M be the number of columns. The router computes

[200] table: Q \displaystyle Q = U ¯ ​ W q ( r ) ∈ ℝ B × n c × d r , \displaystyle=\bar{U}W_{q}^{(r)}\in\mathbb{R}^{B\times n_{c}\times d_{r}}, (A.7) K ( r ) \displaystyle K^{(r)} ∈ ℝ M × d r , \displaystyle\in\mathbb{R}^{M\times d_{r}}, (A.8) L base \displaystyle L^{\mathrm{base}} = Q ​ ( K ( r ) ) ⊤ ∈ ℝ B × n c × M . \displaystyle=Q(K^{(r)})^{\top}\in\mathbb{R}^{B\times n_{c}\times M}. (A.9)

[201] p: If topology-aware routing is enabled, the code predicts 2D chunk coordinates

[202] table: π b , c = tanh ⁡ ( U ¯ b , c ​ W pos + b pos ) ∈ ℝ 2 , \pi_{b,c}=\tanh(\bar{U}_{b,c}W_{\mathrm{pos}}+b_{\mathrm{pos}})\in\mathbb{R}^{2}, (A.10)

[203] p: and uses fixed column coordinates P m ∈ ℝ 2 P_{m}\in\mathbb{R}^{2} stored as buffers. The topology penalty is

[204] table: L b , c , m topo = − γ ​ ‖ π b , c − P m ‖ 2 2 . L^{\mathrm{topo}}_{b,c,m}=-\gamma\|\pi_{b,c}-P_{m}\|_{2}^{2}. (A.11)

[205] p: We compute the squared distance with

[206] table: ‖ π b , c − P m ‖ 2 2 = ‖ π b , c ‖ 2 2 + ‖ P m ‖ 2 2 − 2 ​ ⟨ π b , c , P m ⟩ , \|\pi_{b,c}-P_{m}\|_{2}^{2}=\|\pi_{b,c}\|_{2}^{2}+\|P_{m}\|_{2}^{2}-2\langle\pi_{b,c},P_{m}\rangle, (A.12)

[207] p: using a precomputed buffer for ‖ P m ‖ 2 2 \|P_{m}\|_{2}^{2} .

[208] h4: Routing-logit modulation and top- k k selection.

[209] p: If routing modulation is enabled, a sequence-level scalar s route ∈ [ 0 , 1 ] s_{\mathrm{route}}\in[0,1] scales the router logits:

[210] table: a route = 1 + ρ route ​ ( 2 ​ s route − 1 ) , a_{\mathrm{route}}=1+\rho_{\mathrm{route}}(2s_{\mathrm{route}}-1), (A.13)

[211] p: and the final logits are

[212] table: L b , c , m = a route ​ ( L b , c , m base + 𝟏 topo ​ L b , c , m topo ) . L_{b,c,m}=a_{\mathrm{route}}\left(L^{\mathrm{base}}_{b,c,m}+\mathbf{1}_{\mathrm{topo}}L^{\mathrm{topo}}_{b,c,m}\right). (A.14)

[213] p: The code then computes top- k k indices and selected logits

[214] table: I b , c , 1 : k = TopK ( L b , c , : , k ) , S b , c , j = L b , c , I b , c , j , I_{b,c,1:k}=\mathrm{TopK}(L_{b,c,:},k),\qquad S_{b,c,j}=L_{b,c,I_{b,c,j}}, (A.15)

[215] p: and routing weights by a softmax over the selected values:

[216] table: R b , c , j = exp ⁡ ( S b , c , j ) ∑ j ′ = 1 k exp ⁡ ( S b , c , j ′ ) . R_{b,c,j}=\frac{\exp(S_{b,c,j})}{\sum_{j^{\prime}=1}^{k}\exp(S_{b,c,j^{\prime}})}. (A.16)

[217] p: These routing decisions are shared by all C C token positions in the chunk.

[218] h4: Routing auxiliary term.

[219] p: When routing regularization is enabled, the implementation scatters the selected weights back into a dense tensor

[220] table: M imp ∈ ℝ B × n c × M , M_{\mathrm{imp}}\in\mathbb{R}^{B\times n_{c}\times M},

[221] p: with

[222] table: M imp [ b , c , m ] = ∑ j = 1 k 𝟏 [ I b , c , j = m ] R b , c , j . M_{\mathrm{imp}}[b,c,m]=\sum_{j=1}^{k}\mathbf{1}[I_{b,c,j}=m]\,R_{b,c,j}. (A.17)

[223] p: Summing across batch and chunks gives a column-importance vector

[224] table: u m = ∑ b = 1 B ∑ c = 1 n c M imp ​ [ b , c , m ] , p m = u m ∑ m ′ = 1 M u m ′ + ε . u_{m}=\sum_{b=1}^{B}\sum_{c=1}^{n_{c}}M_{\mathrm{imp}}[b,c,m],\qquad p_{m}=\frac{u_{m}}{\sum_{m^{\prime}=1}^{M}u_{m^{\prime}}+\varepsilon}. (A.18)

[225] p: The routing auxiliary loss is

[226] table: ℒ route = λ lb ​ M ​ ∑ m = 1 M p m 2 . \mathcal{L}_{\mathrm{route}}=\lambda_{\mathrm{lb}}\,M\sum_{m=1}^{M}p_{m}^{2}. (A.19)

[227] h3: A.3 Parallel cortical computation

[228] p: The proposed method does not maintain a persistent token-by-token recurrent state across the full sequence. Instead, it performs a fully tensorized routed computation within chunks, using causal convolutions along the within-chunk token axis and a separate causal convolution along the chunk axis.

[229] h4: Dense projection and routed gather.

[230] p: For each padded token representation U ^ pad [ b , t , : ] \hat{U}_{\mathrm{pad}}[b,t,:] , a shared projection emits parameters for all M M columns:

[231] table: Proj ( U ^ pad [ b , t , : ] ) ∈ ℝ M ⁡ ( 3 ​ n + 3 ) , \mathrm{Proj}(\hat{U}_{\mathrm{pad}}[b,t,:])\in\mathbb{R}^{M(3n+3)}, (A.20)

[232] p: where n n is the cortical state width. After reshaping, the raw tensor has shape

[233] table: P raw ∈ ℝ B × n c × C × M × ( 3 ​ n + 3 ) . P_{\mathrm{raw}}\in\mathbb{R}^{B\times n_{c}\times C\times M\times(3n+3)}.

[234] p: Using the chunk-level routed indices I I , the code gathers only the selected columns:

[235] table: P sel ∈ ℝ B × n c × C × k × ( 3 ​ n + 3 ) . P_{\mathrm{sel}}\in\mathbb{R}^{B\times n_{c}\times C\times k\times(3n+3)}.

[236] p: This tensor is split into

[237] table: Δ coef , B in , C in \displaystyle\Delta_{\mathrm{coef}},\ B_{\mathrm{in}},\ C_{\mathrm{in}} ∈ ℝ B × n c × C × k × n , \displaystyle\in\mathbb{R}^{B\times n_{c}\times C\times k\times n}, (A.21) g 1 , g 2 , g 3 \displaystyle g_{1},\ g_{2},\ g_{3} ∈ ℝ B × n c × C × k , \displaystyle\in\mathbb{R}^{B\times n_{c}\times C\times k}, (A.22)

[238] p: where the three gates are obtained by applying a sigmoid to the final three channels:

[239] table: g state = σ ⁡ ( g 1 ) , g out = σ ⁡ ( g 2 ) , g dis = σ ⁡ ( g 3 ) . g_{\mathrm{state}}=\sigma(g_{1}),\quad g_{\mathrm{out}}=\sigma(g_{2}),\quad g_{\mathrm{dis}}=\sigma(g_{3}). (A.23)

[240] h4: Excitatory-inhibitory gate remapping.

[241] p: When excitatory-inhibitory gating is enabled, the third gate acts as a disinhibitory controller that modifies the first two gates:

[242] table: g state \displaystyle g_{\mathrm{state}} ← ( 1 − g dis ) ​ g state + g dis , \displaystyle\leftarrow(1-g_{\mathrm{dis}})\,g_{\mathrm{state}}+g_{\mathrm{dis}}, (A.24) g out \displaystyle g_{\mathrm{out}} ← ( 1 − g dis ) ​ g out + g dis . \displaystyle\leftarrow(1-g_{\mathrm{dis}})\,g_{\mathrm{out}}+g_{\mathrm{dis}}. (A.25)

[243] p: The state-related tensors are then scaled by g state g_{\mathrm{state}} :

[244] table: Δ coef ← g state ⊙ Δ coef , B in ← g state ⊙ B in , C in ← g state ⊙ C in . \Delta_{\mathrm{coef}}\leftarrow g_{\mathrm{state}}\odot\Delta_{\mathrm{coef}},\quad B_{\mathrm{in}}\leftarrow g_{\mathrm{state}}\odot B_{\mathrm{in}},\quad C_{\mathrm{in}}\leftarrow g_{\mathrm{state}}\odot C_{\mathrm{in}}. (A.26)

[245] p: If this option is disabled, the remapping is skipped and the raw sigmoid gates are used.

[246] h4: Adaptive state coefficients and within-chunk causal filtering.

[247] p: Each column has a learned parameter tensor

[248] table: A log ∈ ℝ M × n . A_{\log}\in\mathbb{R}^{M\times n}.

[249] p: Then

[250] table: A base = σ ⁡ ( − A log ) ∈ ( 0 , 1 ) M × n , A_{\mathrm{base}}=\sigma(-A_{\log})\in(0,1)^{M\times n}, (A.27)

[251] p: gathers the selected rows using I I , and obtains

[252] table: A sel ∈ ℝ B × n c × k × n . A_{\mathrm{sel}}\in\mathbb{R}^{B\times n_{c}\times k\times n}.

[253] p: Broadcasting over the token axis yields the token-dependent coefficient

[254] table: α = σ ⁡ ( Δ coef ) ⊙ A sel ( bcast ) ∈ ℝ B × n c × C × k × n . \alpha=\sigma(\Delta_{\mathrm{coef}})\odot A_{\mathrm{sel}}^{\mathrm{(bcast)}}\in\mathbb{R}^{B\times n_{c}\times C\times k\times n}. (A.28)

[255] p: The driven state signal is

[256] table: D state = ( 1 − α ) ⊙ B in . D_{\mathrm{state}}=(1-\alpha)\odot B_{\mathrm{in}}. (A.29)

[257] p: To apply causal filtering within each chunk, the tensor is permuted and reshaped to merge batch, chunk, and routed-column axes:

[258] table: D flat ∈ ℝ ( B ​ n c ​ k ) × n × C . D_{\mathrm{flat}}\in\mathbb{R}^{(Bn_{c}k)\times n\times C}.

[259] p: We apply a depthwise 1D convolution followed by a pointwise 1D convolution along the length- C C axis:

[260] table: H flat = PWConv mem ​ ( DWConv mem ​ ( PadLeft ⁡ ( D flat , k mem − 1 ) ) ) . H_{\mathrm{flat}}=\mathrm{PWConv}_{\mathrm{mem}}\!\left(\mathrm{DWConv}_{\mathrm{mem}}\!\left(\mathrm{PadLeft}(D_{\mathrm{flat}},k_{\mathrm{mem}}-1)\right)\right). (A.30)

[261] p: Reshaping back gives the filtered state tensor

[262] table: H ∈ ℝ B × n c × C × k × n . H\in\mathbb{R}^{B\times n_{c}\times C\times k\times n}.

[263] p: This operation is causal only within chunks. Long-range propagation is handled separately at chunk resolution.

[264] h4: Readout with optional top-down gating.

[265] p: The bottom-up readout input is

[266] table: B read = C in ⊙ H . B_{\mathrm{read}}=C_{\mathrm{in}}\odot H. (A.31)

[267] p: If the top-down gated readout is enabled and associative memory is active, let

[268] table: C mem ∈ ℝ B × n c × d C^{\mathrm{mem}}\in\mathbb{R}^{B\times n_{c}\times d}

[269] p: be the retrieved chunk context and define its broadcast form

[270] table: C bcast mem ∈ ℝ B × n c × 1 × 1 × d . C^{\mathrm{mem}}_{\mathrm{bcast}}\in\mathbb{R}^{B\times n_{c}\times 1\times 1\times d}.

[271] p: The readout is

[272] table: S read \displaystyle S_{\mathrm{read}} = W bot ​ B read ∈ ℝ B × n c × C × k × d , \displaystyle=W_{\mathrm{bot}}\,B_{\mathrm{read}}\in\mathbb{R}^{B\times n_{c}\times C\times k\times d}, (A.32) G top \displaystyle G_{\mathrm{top}} = σ ⁡ ( W gate ​ ϕ ​ ( W top ​ C bcast mem ) ) ∈ ℝ B × n c × 1 × 1 × d , \displaystyle=\sigma\!\left(W_{\mathrm{gate}}\,\phi\!\left(W_{\mathrm{top}}\,C^{\mathrm{mem}}_{\mathrm{bcast}}\right)\right)\in\mathbb{R}^{B\times n_{c}\times 1\times 1\times d}, (A.33) Y sel \displaystyle Y_{\mathrm{sel}} = RMSNorm ⁡ ( S read ⊙ ( 1 + G top ) ) , \displaystyle=\mathrm{RMSNorm}\!\left(S_{\mathrm{read}}\odot(1+G_{\mathrm{top}})\right), (A.34)

[273] p: with ϕ = SiLU \phi=\mathrm{SiLU} .

[274] p: If top-down gated readout is disabled, the method uses a linear readout:

[275] table: Y sel = W out ​ B read . Y_{\mathrm{sel}}=W_{\mathrm{out}}\,B_{\mathrm{read}}. (A.35)

[276] h4: Output gate, skip connection, and routed mixture.

[277] p: The selected-column outputs are scaled by the output-control gate:

[278] table: Y sel ← Y sel ⊙ g out ( bcast ) . Y_{\mathrm{sel}}\leftarrow Y_{\mathrm{sel}}\odot g_{\mathrm{out}}^{\mathrm{(bcast)}}. (A.36)

[279] p: If the skip connection is enabled, the block uses a learned scalar per column,

[280] table: s ∈ ℝ M , s\in\mathbb{R}^{M},

[281] p: gathers the selected entries using I I , and adds a gated skip from the chunk input:

[282] table: Y sel ← Y sel + tanh ⁡ ( s I ) ( bcast ) ⊙ U ^ chunk ( bcast ) . Y_{\mathrm{sel}}\leftarrow Y_{\mathrm{sel}}+\tanh(s_{I})^{\mathrm{(bcast)}}\odot\hat{U}_{\mathrm{chunk}}^{\mathrm{(bcast)}}. (A.37)

[283] p: The routed chunk output is then formed by the weighted sum over the k k selected columns:

[284] table: Y chunk [ b , c , τ , : ] = ∑ j = 1 k R b , c , j Y sel [ b , c , τ , j , : ] . Y_{\mathrm{chunk}}[b,c,\tau,:]=\sum_{j=1}^{k}R_{b,c,j}\,Y_{\mathrm{sel}}[b,c,\tau,j,:]. (A.38)

[285] h4: Chunk-level lateral propagation.

[286] p: We compute chunk summaries by averaging over the token axis:

[287] table: C ctx [ b , c , : ] = 1 C ∑ τ = 1 C Y chunk [ b , c , τ , : ] . C_{\mathrm{ctx}}[b,c,:]=\frac{1}{C}\sum_{\tau=1}^{C}Y_{\mathrm{chunk}}[b,c,\tau,:]. (A.39)

[288] p: If associative memory is enabled, the retrieved context is added:

[289] table: C ctx ← C ctx + C mem . C_{\mathrm{ctx}}\leftarrow C_{\mathrm{ctx}}+C^{\mathrm{mem}}. (A.40)

[290] p: A causal depthwise 1D convolution and pointwise 1D convolution are then applied along the chunk axis:

[291] table: C ~ ctx ⊤ = PWConv lat ​ ( DWConv lat ​ ( PadLeft ⁡ ( C ctx ⊤ , k lat − 1 ) ) ) . \widetilde{C}_{\mathrm{ctx}}^{\top}=\mathrm{PWConv}_{\mathrm{lat}}\!\left(\mathrm{DWConv}_{\mathrm{lat}}\!\left(\mathrm{PadLeft}(C_{\mathrm{ctx}}^{\top},k_{\mathrm{lat}}-1)\right)\right). (A.41)

[292] p: After transposing back, the result is broadcast across the token axis and added to the chunk outputs:

[293] table: Y chunk ← Y chunk + C ~ ctx ( bcast ) . Y_{\mathrm{chunk}}\leftarrow Y_{\mathrm{chunk}}+\widetilde{C}_{\mathrm{ctx}}^{\mathrm{(bcast)}}. (A.42)

[294] p: Finally, the chunk tensor is reshaped back to ( B , n c ​ C , d ) (B,n_{c}C,d) and trimmed to the original length T T .

[295] h4: Activation checkpointing.

[296] p: If enabled, the cortex function is wrapped with torch.utils.checkpoint.checkpoint (non-reentrant mode) with exact gradients. This reduces activation memory without changing the forward computation.

[297] h3: A.4 Associative memory and routing-weight refinement

[298] h4: Associative-memory retrieval.

[299] p: The associative-memory module operates on chunk summaries

[300] table: U ¯ ∈ ℝ B × n c × d . \bar{U}\in\mathbb{R}^{B\times n_{c}\times d}.

[301] p: It stores n s n_{s} learned memory slots

[302] table: Ξ ∈ ℝ n s × d h , \Xi\in\mathbb{R}^{n_{s}\times d_{h}},

[303] p: and uses learned projections into the memory space of width d h d_{h} :

[304] table: Q mem \displaystyle Q_{\mathrm{mem}} = U ¯ ​ W q ( mem ) ∈ ℝ B × n c × d h , \displaystyle=\bar{U}W_{q}^{(\mathrm{mem})}\in\mathbb{R}^{B\times n_{c}\times d_{h}}, (A.43) R mem \displaystyle R_{\mathrm{mem}} = (retrieval in memory space) . \displaystyle=\text{(retrieval in memory space)}. (A.44)

[305] p: We normalize both projected queries and memory slots:

[306] table: Q ~ mem \displaystyle\widetilde{Q}_{\mathrm{mem}} = normalize ⁡ ( Q mem ) , \displaystyle=\mathrm{normalize}(Q_{\mathrm{mem}}), (A.45) Ξ ~ \displaystyle\widetilde{\Xi} = normalize ⁡ ( Ξ ) . \displaystyle=\mathrm{normalize}(\Xi). (A.46)

[307] p: With inverse temperature β \beta , retrieval weights are

[308] table: A mem = softmax ⁡ ( β ​ Q ~ mem ​ Ξ ~ ⊤ ) ∈ ℝ B × n c × n s , A_{\mathrm{mem}}=\mathrm{softmax}\!\left(\beta\,\widetilde{Q}_{\mathrm{mem}}\widetilde{\Xi}^{\top}\right)\in\mathbb{R}^{B\times n_{c}\times n_{s}}, (A.47)

[309] p: and the retrieved memory vector is

[310] table: R mem = A mem ​ Ξ ~ ∈ ℝ B × n c × d h . R_{\mathrm{mem}}=A_{\mathrm{mem}}\widetilde{\Xi}\in\mathbb{R}^{B\times n_{c}\times d_{h}}. (A.48)

[311] p: A final projection and RMS normalization produce the chunk-level context used by the cortex:

[312] table: C mem = RMSNorm ⁡ ( R mem ​ W v ( mem ) ) ∈ ℝ B × n c × d . C^{\mathrm{mem}}=\mathrm{RMSNorm}(R_{\mathrm{mem}}W_{v}^{(\mathrm{mem})})\in\mathbb{R}^{B\times n_{c}\times d}. (A.49)

[313] h4: Routing-weight refinement (cortico-thalamic feedback).

[314] p: When enabled, the block first computes a cortex output

[315] table: Y ∈ ℝ B × T × d , Y\in\mathbb{R}^{B\times T\times d},

[316] p: then pools it to chunk resolution and maps it back to router space. We pad Y Y to length n c ​ C n_{c}C using zeros (not repeated-token padding), reshape to chunks, and average over the C C positions:

[317] table: Y ¯ b , c , : = 1 C ∑ τ = 1 C Y pad [ b , c , τ , : ] . \bar{Y}_{b,c,:}=\frac{1}{C}\sum_{\tau=1}^{C}Y_{\mathrm{pad}}[b,c,\tau,:]. (A.50)

[318] p: The feedback router scores are

[319] table: Q fb \displaystyle Q_{\mathrm{fb}} = Y ¯ ​ W fb ∈ ℝ B × n c × d r , \displaystyle=\bar{Y}W_{\mathrm{fb}}\in\mathbb{R}^{B\times n_{c}\times d_{r}}, (A.51) L fb \displaystyle L_{\mathrm{fb}} = Q fb ​ ( K ( r ) ) ⊤ ∈ ℝ B × n c × M . \displaystyle=Q_{\mathrm{fb}}(K^{(r)})^{\top}\in\mathbb{R}^{B\times n_{c}\times M}. (A.52)

[320] p: Only the already-selected columns are gathered:

[321] table: S b , c , j fb = L fb ​ [ b , c , I b , c , j ] ∈ ℝ B × n c × k . S^{\mathrm{fb}}_{b,c,j}=L_{\mathrm{fb}}[b,c,I_{b,c,j}]\in\mathbb{R}^{B\times n_{c}\times k}. (A.53)

[322] p: A learned scalar parameter is passed through tanh \tanh to obtain a bounded mixing coefficient

[323] table: α fb = tanh ⁡ ( c mix ) ∈ ( − 1 , 1 ) , \alpha_{\mathrm{fb}}=\tanh(c_{\mathrm{mix}})\in(-1,1),

[324] p: and the refined routing weights are

[325] table: R b , c , : ′ = softmax ( S b , c , : + α fb S b , c , : fb ) . R^{\prime}_{b,c,:}=\mathrm{softmax}\!\left(S_{b,c,:}+\alpha_{\mathrm{fb}}\,S^{\mathrm{fb}}_{b,c,:}\right). (A.54)

[326] p: The top- k k indices I I are not recomputed.

[327] p: A key implementation detail is that we then execute the cortex a second time with the same routing support I I and refined weights R ′ R^{\prime} . This is a full second cortex call, not a lightweight reweighting of cached selected-column outputs.

[328] h3: A.5 Model wrapper, auxiliary losses, and trainer objective

[329] p: The model wrapper stacks decoder blocks, applies a final RMS normalization, and uses a tied output projection. At each layer, the wrapper accumulates the routing auxiliary term and the predictive reconstruction term when present:

[330] table: ℒ route Σ = ∑ ℓ = 1 L ℒ route ( ℓ ) , ℒ pred Σ = ∑ ℓ = 1 L ℒ pred ( ℓ ) . \mathcal{L}_{\mathrm{route}}^{\Sigma}=\sum_{\ell=1}^{L}\mathcal{L}_{\mathrm{route}}^{(\ell)},\qquad\mathcal{L}_{\mathrm{pred}}^{\Sigma}=\sum_{\ell=1}^{L}\mathcal{L}_{\mathrm{pred}}^{(\ell)}. (A.55)

[331] p: The wrapper returns the token cross-entropy loss, logits, and the accumulated auxiliary quantities. In the provided training script, the total optimization objective is formed explicitly as

[332] table: ℒ train = ℒ CE + w p ​ r ​ e ​ d ​ ℒ pred Σ + w r ​ o ​ u ​ t ​ e ​ r ​ ℒ route Σ . \mathcal{L}_{\mathrm{train}}=\mathcal{L}_{\mathrm{CE}}+w_{pred}\,\mathcal{L}_{\mathrm{pred}}^{\Sigma}+w_{router}\,\mathcal{L}_{\mathrm{route}}^{\Sigma}. (A.56)

[333] p: We use w pred = 0.1 w_{\mathrm{pred}}=0.1 and w router = 0.1 w_{\mathrm{router}}=0.1 in the trainer.

[334] h3: A.6 Main training configuration

[335] p: This subsection records the optimization and training configuration details.

[336] h4: Hardware and precision.

[337] p: Runs use a single node with 4 NVIDIA V100 GPUs (each 32GB) and fp16 mixed precision with gradient scaling.

[338] h4: Optimization and schedule.

[339] p: The trainer uses AdamW with learning rate 2 × 10 − 4 2\times 10^{-4} , weight decay 0.1 0.1 , and ( β 1 , β 2 ) = ( 0.9 , 0.95 ) (\beta_{1},\beta_{2})=(0.9,0.95) . The learning-rate schedule is linear warmup for 1,000 optimizer steps followed by cosine decay, indexed by optimizer steps (not micro-steps). Gradient clipping is applied with threshold 1.0.

[340] p: We use:

[341] table: batch size per GPU = 8 , gradient accumulation = 4 , world size = 4 , T = 1024 . \text{batch size per GPU}=8,\quad\text{gradient accumulation}=4,\quad\text{world size}=4,\quad T=1024.

[342] p: This gives an effective global batch of

[343] table: 8 × 4 × 4 = 128 8\times 4\times 4=128

[344] p: sequences per optimizer step, or

[345] table: 128 × 1024 = 131,072 128\times 1024=131{,}072

[346] p: tokens per optimizer step.

[347] p: With 22,000 optimizer steps, the total training budget is

[348] table: 22,000 × 131,072 = 2,883,584,000 22{,}000\times 131{,}072=2{,}883{,}584{,}000

[349] p: tokens (approximately 2.88B tokens).

[350] h4: Data and tokenization.

[351] p: We use the EleutherAI/gpt-neox-20b tokenizer, sequence length 1024, streaming training and evaluation. The training dataset is allenai/c4:en (train split). The evaluation probes are:

[352] p: allenai/c4:en (validation split),

[353] p: wikitext:wikitext-103-v1 ,

[354] p: EleutherAI/lambada_openai .

[355] p: The configuration caps the number of training and evaluation samples at 3,000,000 and 300,000, respectively. The data loader uses 8 workers.

[356] h4: Logging and checkpointing.

[357] p: Training metrics are logged every 20 optimizer steps. Evaluation runs every 500 optimizer steps. The trainer saves only improved best checkpoints according to the selected validation criterion, and it defaults to average perplexity.

[358] h4: Model hyperparameters.

[359] p: Model hyperparameters are read from the model section of the experiment configuration and are logged with the run metadata. The code supports multiple backbones ( trc2 , neurocognitive , transformer , mamba , and moe ) through the same training pipeline. For the neurocognitive TRC 2 block used in the main method, the exact architectural options are controlled by booleans for routing topology, excitatory-inhibitory gating, skip connections, modulation controller, predictive pathway, associative memory, top-down gated readout, routing-weight refinement, and the cerebellar corrective path.

[360] h2: Appendix B Complexity

[361] p: Let B B be batch size, T T sequence length, d d model width, C C routing chunk size, and n c = ⌈ T / C ⌉ n_{c}=\lceil T/C\rceil the number of routing chunks. Let M M be the number of cortical columns, k ≪ M k\ll M the routed columns per chunk, n n the cortical state width ( n_state ), d r d_{r} the router width, d h d_{h} the hippocampal memory width ( d_memory ), n s n_{s} the number of hippocampal slots, d z d_{z} the cerebellar hidden width, and r r the cerebellar low-rank width ( fast_rank ).

[362] h4: Modulation controller.

[363] p: The neuromodulator path computes batch and per-sequence statistics over U ∈ ℝ B × T × d U\in\mathbb{R}^{B\times T\times d} and applies a small MLP on a 4 ​ d 4d input per sequence. Its cost is

[364] table: O ⁡ ( B ​ T ​ d ) + O ⁡ ( B ​ d ​ d nm ) , O(BTd)+O(Bd\,d_{\mathrm{nm}}),

[365] p: where d nm d_{\mathrm{nm}} is the hidden size of the neuromodulator MLP. This term is small relative to the main routed cortex path for the default settings.

[366] h4: Predictive coding.

[367] p: The predictive path applies a causal depthwise 1D convolution and a pointwise 1D convolution over the full token sequence, both at width d d , followed by an MSE loss:

[368] table: O ⁡ ( B ​ T ​ d ​ k pc ) + O ⁡ ( B ​ T ​ d 2 ) + O ⁡ ( B ​ T ​ d ) , O(BTd\,k_{\mathrm{pc}})+O(BTd^{2})+O(BTd),

[369] p: where k pc k_{\mathrm{pc}} is the predictive kernel width. The pointwise convolution term O ⁡ ( B ​ T ​ d 2 ) O(BTd^{2}) is usually the leading term inside this subsystem.

[370] h4: Chunked sparse router.

[371] p: Routing is performed on chunk summaries, so the router runs over n c n_{c} positions instead of T T . The base router cost is

[372] table: O ⁡ ( B ​ n c ​ d ​ d r ) + O ⁡ ( B ​ n c ​ d r ​ M ) , O(Bn_{c}dd_{r})+O(Bn_{c}d_{r}M),

[373] p: for the query projection and dense logits over M M columns. If topology is enabled, the additional cost is

[374] table: O ⁡ ( B ​ n c ​ d ) + O ⁡ ( B ​ n c ​ M ) , O(Bn_{c}d)+O(Bn_{c}M),

[375] p: from the 2D position projection and distance-to-column computations. Top- k k selection and the top- k k softmax are then applied per chunk over the M M logits.

[376] h4: Associative memory.

[377] p: The associative memory module also runs at chunk resolution. Its cost is

[378] table: O ⁡ ( B ​ n c ​ d ​ d h ) + O ⁡ ( B ​ n c ​ n s ​ d h ) + O ⁡ ( B ​ n c ​ n s ​ d h ) + O ⁡ ( B ​ n c ​ d h ​ d ) , O(Bn_{c}dd_{h})+O(Bn_{c}n_{s}d_{h})+O(Bn_{c}n_{s}d_{h})+O(Bn_{c}d_{h}d),

[379] p: which corresponds to the query projection, Hopfield score computation, Hopfield retrieval, and projection back to model width. The two middle terms come from Q h ​ Ξ ⊤ Q_{h}\Xi^{\top} and ( softmax ⁡ ( ⋅ ) ) ​ Ξ (\mathrm{softmax}(\cdot))\Xi .

[380] h4: Cortical field, one pass.

[381] p: The cortex is the main computation in the block. For one cortex pass, the cost has two parts.

[382] p: (1) Dense token-to-column projection. Each padded token is projected to all columns:

[383] table: O ⁡ ( B ​ T ​ d ​ M ​ ( 3 ​ n + 3 ) ) . O\!\left(BT\,d\,M(3n+3)\right).

[384] p: This is dense in M M and is often a major cost term.

[385] p: (2) Routed selected-column path. After gathering the routed columns, the selected-column path scales with k k rather than M M . It includes:

[386] p: gather and parameter splitting for selected columns, with tensor sizes proportional to B ​ n c ​ C ​ k ​ ( 3 ​ n + 3 ) Bn_{c}Ck(3n+3) ,

[387] p: membrane filtering within chunks using a depthwise 1D convolution and a pointwise 1D convolution on width n n :

[388] table: O ⁡ ( B ​ n c ​ k ​ n ​ C ​ k mem ) + O ⁡ ( B ​ n c ​ k ​ C ​ n 2 ) , O(Bn_{c}k\,n\,C\,k_{\mathrm{mem}})+O(Bn_{c}k\,C\,n^{2}),

[389] p: readout from state width n n to model width d d :

[390] table: O ⁡ ( B ​ n c ​ C ​ k ​ n ​ d ) , O(Bn_{c}Ck\,nd),

[391] p: both for the plain readout and for the basal branch of the dendritic readout,

[392] p: routed weighted mixing across the k k selected columns:

[393] table: O ⁡ ( B ​ n c ​ C ​ k ​ d ) , O(Bn_{c}Ckd),

[394] p: chunk-level lateral propagation using depthwise and pointwise convolutions on chunk summaries:

[395] table: O ⁡ ( B ​ n c ​ d ​ k lat ) + O ⁡ ( B ​ n c ​ d 2 ) . O(Bn_{c}d\,k_{\mathrm{lat}})+O(Bn_{c}d^{2}).

[396] p: When the readout is enabled, the gating path adds a chunk-level cost (not multiplied by C ​ k Ck in the linear layers because the signal is broadcast):

[397] table: O ⁡ ( B ​ n c ​ d ​ d ap ) + O ⁡ ( B ​ n c ​ d ap ​ d ) , O(Bn_{c}\,d\,d_{\mathrm{ap}})+O(Bn_{c}\,d_{\mathrm{ap}}\,d),

[398] p: plus broadcasted elementwise operations over the selected-token tensor.

[399] h4: Corrector feedback.

[400] p: The feedback path pools the first cortex output to chunk resolution, projects it to router space, computes logits over all M M columns, gathers feedback scores for the already-selected columns, and forms refined top- k k weights:

[401] table: O ⁡ ( B ​ T ​ d ) + O ⁡ ( B ​ n c ​ d ​ d r ) + O ⁡ ( B ​ n c ​ d r ​ M ) + O ⁡ ( B ​ n c ​ k ) . O(BTd)+O(Bn_{c}dd_{r})+O(Bn_{c}d_{r}M)+O(Bn_{c}k).

[402] p: It does not run a second top- k k search. It does, however, call the cortex a second time with the same indices and new weights. Therefore, enabling feedback adds approximately one extra cortex pass (including the dense token-to-column projection) plus the chunk-level feedback projection above.

[403] h4: Low-rank corrective pathway.

[404] p: The corrective path computes two linear terms into width d z d_{z} , applies SiLU, and then a low-rank projection:

[405] table: O ⁡ ( B ​ T ⋅ 2 ​ d ​ d z ) + O ⁡ ( B ​ T ​ d z ) + O ⁡ ( B ​ T ⋅ d z ​ r ) + O ⁡ ( B ​ T ⋅ d ​ r ) . O(BT\cdot 2dd_{z})+O(BTd_{z})+O(BT\cdot d_{z}r)+O(BT\cdot dr).

[406] p: The O ⁡ ( B ​ T ⋅ 2 ​ d ​ d z ) O(BT\cdot 2dd_{z}) term comes from the split implementation of the linear map on ( U , Y ) (U,Y) , which is equivalent to a single linear layer on [ U ; Y ] [U;Y] but avoids explicitly materializing the concatenation.

[407] h4: Summary.

[408] p: The block is sparse in the routed column dimension after routing, but it still contains a dense token-to-column projection to produce per-column parameters. In one cortex pass, this dense projection scales as

[409] table: O ⁡ ( B ​ T ​ d ​ M ​ ( 3 ​ n + 3 ) ) , O\!\left(BT\,d\,M(3n+3)\right),

[410] p: while the routed computations scale with k k . With corrective feedback enabled, the cortex is executed twice with the same selected indices, which roughly doubles the cortex-side cost without repeating the top- k k search.

[411] h2: Instructions for reporting errors

[412] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[413] p: Tip: You can select the relevant text first, to include it in your report.

[414] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[415] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
