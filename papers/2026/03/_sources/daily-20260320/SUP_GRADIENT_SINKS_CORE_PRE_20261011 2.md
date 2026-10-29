# GradientSinks17771：有限机制与PRE

resume_mar17，独立03-20补03-19。2+2+2=6准入/day独核§3复用；本次实际必要[exact-v1](https://arxiv.org/html/2603.17771v1)§2–6/Theorems1–2/Figures1–5文字与直接限制（L55–171）。当前v2只定点回受影响RMSNorm说明§4.3/L185–187与value接口§5.1/L196–200；返回的其他v2扩规模/检索信号不作为本命题证据，不审全版本diff、图精确拟合、附录/代码。准入笔记“只改反传”已窄纠，潜力/6分不变。

## 精确支持与边界

- 因果attention V侧局部导数是Σ_t a_ts g_t；Q首位置只一个可见key，attention权重对q导数0，不等该token全部参数/总梯度0。K/V聚合与Q行局部不同。带相同均值μ/噪声协方差条件的T1界不是任意真实随机a/g联合保证；固定a或条件矩需另明，μ=0、相反梯度抵消时不由高attention质量保证大norm。只采用精确局部identity与可能路径，不采“强sink必强gradient”的普遍单调命题。
- T2 RMSNorm Jacobian operator界≤||γ||∞/rms(x)，数学成立；是给定γ/上游梯度与输入的最坏增益上界，不等实际每方向严格同比例缩小或训练自动优化norm。γ和梯度本身改变、residual identity/K/Q/MLP共同作用时不授整网稳定或唯一中介。v2§4.3明确sufficient targetgradient界，与这受限解释相容，未纠正/推翻v1局部界。
- V-scale在标准valueprojection之后/aggregation之前把v变φ(r)v，r=||v||²，φ=r/(r+C)，C=(d_head σ)² expθ、σ=.02，learned oneparameter/layer/head。它保持同次Q/K attention权重计算，但改变当前attentionoutput、后续states和训练；不是detach/custombackward-only。原首批拟稿“只改反传”错误已保纠正。
- Jacobian切向r/(r+C)、径向(r²+3Cr)/(r+C)²；r≪C两路小，r>C径向可大于1（r=3C为9/8），不能授全局gradient contraction。Q/K以及identity旁路仍在，§5Remark1自认仅V不能消除全gradient sink。变换不按token index硬编码，按value norm抑制，语义重要但小norm的value也可能受影响。
- 作者C4/AdamW/Llama-like pre-RMSNorm/RoPE/SwiGLU，0.1B与0.3B训练模型，每1000steps一次checkpoint probe、fullbatch梯度先聚合后token norm；并非逐sample norm平均。baseline与V-scale同data/optimizer/modelconfigs，强attention sink仍在、residual/MLP MA降低，attentionoutput也直接降低，支持有限分离结果但不隔离唯一backward原因。略低valloss只文字、无下游任务/全scale搜索；不造精确图值/幅度或普遍质量保证。
- v1训练tokens、batch、contextlength、steps/learningrate、硬件、precision、seed/重复、不确定性及完整墙钟费用未充分披露。改value与learnedC、训练和诊断probe有成本，不能由oneparameter/head授零开销/量化收益/生产能力。Limitations明确denseLlama only，MoE/multimodal迁移不明，不完整解释AS/MA学习全过程，无exhaustivesweep/downstream。

v2 L202–203另将尺度定义改为 `C=d_model*d_head*σ²*expθ`，而v1为 `(d_head*σ)²*expθ`。这是尺度归一化变化，不能把两精确配方互换；正文仅采用 `C>0` 的逐层逐head受限接口，不授全域recipe。

## actualowner与差额

actual `MODEL-TRANSFORMER-LAYER` Ch17 L100–340完整Norm位置→shape→Residual写入/ReadBlindness→Jacobian路径→分层控制/诊断已顺读，16/18入口和Ch17末交接实际读。Ch14 L255–298完整no-op/结构sink/跨深度diagnosis有效，仍ownattention路由。Ch17已有局部Jacobian/前反分责与跨层outlier写读，却未承载attention value列梯度聚合、RMSNorm gain界及φ(r)v既改前向又改反向的有限干预；非主题NC。不改14/28重复主线。拟Ch17当前296后、`解决手段属于不同控制层`前两短段，仅机制/因果权限差额；未授锁。

## 逐字PRE（待非准备者）

梯度诊断还要展开 token 与路径，而不只沿层深看一个 norm。因果 Attention 中，某个 value 的局部梯度是后续合法 query 的上游梯度按 attention 权重求和；前向质量集中会提供反向聚合通路，却可能因方向抵消而没有同等大的净梯度。Pre-RMSNorm 又使这一支路的最坏增益受 `||γ||∞/rms(x)` 约束，较大激活可以降低局部上界，但上游梯度、γ 与 residual identity 仍共同决定完整信号。因而高 attention、massive activation 与 gradient concentration 应分别测量，不能把其中一幅曲线当成另两者的唯一原因。<!-- source-family:SF-2026-ARXIV-2603-17771 -->

一条[受限 value-path 干预](https://arxiv.org/html/2603.17771v1#S5)在聚合前将 value 乘以 `φ(r)=r/(r+C)`，其中 `r` 是其平方范数，`C>0` 为逐层逐 head 学习的尺度。小范数 value 的前向贡献和反向信号同时减弱；这不是只改 backward，保持当前 Q/K 权重也不保证后续状态不变。小型 C4 预训练模型保留较强 attention sinks 而减少激活尖峰，支持这两种现象可部分分离，却不证明唯一训练中介、全局梯度收缩或全部能力改善。径向增益在部分尺度仍可大于一，Q/K 与 identity 路径也未消除；新增门、训练与诊断费用必须计入。质量、数值或完整成本未核时保留原 Attention/Norm 路径，不以激活变小直接批准低位量化、长窗或生产稳定性。

静态注：`SF-2026-ARXIV-2603-17771` — [exact-v1](https://arxiv.org/html/2603.17771v1)§2–6/Theorems1–2与V-scale/Figures1–5文字、Limitations；当前v2仅RMSNorm局部上界/value接口定点。仅路径聚合、局部gain与前反共同干预的受限分离；不采纯反传/唯一中介、全局收缩、泛化质量或零成本。小C4条件/配置缺失保留，未核实现或复现。

## 未采用中心重开条件

如未来要授唯一gradient媒介/全局稳定或普遍量化/检索收益，只请求一次同forward不同backward及同backward不同forward的matched干预、完整训练配置/seed与下游质量—费用trace；当前有限局部采用不依赖这些强保证。等待非准备者Source/actualowner/PRE裁，不自计safe/DAY。
