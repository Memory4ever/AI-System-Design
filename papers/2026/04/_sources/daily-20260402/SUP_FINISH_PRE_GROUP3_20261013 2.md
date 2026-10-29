# 五个已过Source的具体owner窄PRE

只本日既存精确v1，Source/反侧复用STOP §9.19/21/26/32，正常日门复用§9.29/55。不扩发现/附件。作者实际回读Ch24 102–122/232–259、Ch17 651–679、Ch49 2267–2285、Ch28 367–386完整左右邻。每项一段及本人注，root具体授锁前不写Books。以下不是全recipe或普遍性能承诺。

## Gaussian 28992 — MULTIMODAL-GENERATIVE-PARADIGMS / Ch24

在CFM「生成时从噪声开始积分」完整段后、「少样本图像微调」前。现平均场/solver分责不等配对transport cost近似已验。

~~~~markdown
解析构造也须分开“把分布运过去”与“为配对选择正确的最小代价”：在Gaussian mixture的有限分支中，可令各Gaussian均值与协方差沿仿射路径变化，按component responsibility混合velocity，再用路径的动能代价选择带熵正则的配对。这满足相应continuity条件，不代表非交换协方差下的最小Wasserstein能量。[受限Gaussian分析](https://arxiv.org/html/2603.28992v1)只在SPD、局部距离及commuting条件下给近似界；把长路径拆短只改善locality，不取消commuting，近奇异边界还会放大常数。显式surrogate仍含whitening逆平方根与matrix log，不能称完全免spectral计算；CPU构造计时又排除了ODE，不是神经生成端到端加速。配对、矩阵函数、split和实际积分均付费；条件失配时保留exact Gaussian cost或原CFM配对并独立验质量，不由解析式、连续性或拆段批准全局最优与廉价采样。<!-- source-family:SF-2026-ARXIV-2603-28992 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-28992` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.28992v1)II–VIII必要Eq3/6/9/Alg1/Theorems1–2，2+1+2=5，仅affine Gaussian-path kinetic surrogate/配对cost与exact W2条件分责。保SPD/ρ<1/commuting、split不消条件、W²98.52对C2363.09及noncomm/mean gap.23；CPU d2–300构造排ODE、硬件/CI未披露，全部矩阵/配对/积分费，不授神经/全局最优；未核代码/复现。
~~~~

## Gloria 29931 — MULTIMODAL-GENERATIVE-PARADIGMS / Ch24

在外部VACE reference/自产history分责完整段后、「历史压缩是否可用」前。新差额是参考池人口与typed positional条件，而不是新增持久world state。

~~~~markdown
参考人口还会改变生成器学到的是身份条件还是复制捷径：训练短clip时，参考可同时来自该clip内外的较长shot，并把global、view与expression anchors分成不同类型的位置条件，而不让所有参考默认指向待生成帧。较弱的RoPE offset帮助区分来源，不构成无冲突或语义解耦证明；固定anchors与最近自产latent prefix也承担不同责任。[Gloria的受限对照](https://arxiv.org/html/2603.29931v1)支持此采样/条件接口，但训练prefix是真实历史，部署prefix是自产历史，ArcFace/CLIP/DINO又只是指定消费者的proxy，不认证身份真值或无限稳定。数据筛选、三阶段训练、anchor编码、chunk/overlap和消费者回归均付费，局部美学及条件切片仍有反退；参考标签、历史人口或质量失配时保留直接参考、较短chunk和重新锚定，分别验外观/表情/运动，不由长分钟展示批准全历史正确或真实环境状态。<!-- source-family:SF-2026-ARXIV-2603-29931 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29931` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29931v1)S3–5.4/Eq1–2/T1–4，2+1+2=5，仅跨短clip的superset参考人口与global/view/expression弱位置条件，保GT四latent prefix到自产history交接。17B/512A800/20kstep与三阶段数据费、20long/50view/40expression/95cases/60expert有限人口，AES3.63<3.65与标签noise，proxy非identity truth/CI和完整延迟未披露；未核代码/复现。
~~~~

## VecAttention 29494 — INFER-TENSORRT-LLM / Ch49

在完整Serving Pipeline硬件选择段后、「这些source-specific结果」前；保该句及旧六markers，使近似selector/traffic成为执行计划的具体条件。

~~~~markdown
选择稀疏粒度时，还须把selector自身和不连续KV访问放进同一执行计划：先以pooled queries给key vectors打分，用最大值差阈值免排序，tile中只写选中indices，再gather对应K/V并重新softmax。这减少的是指定attention计算和访问，不是物理KV eviction或cache容量自动下降。[VecAttention的受限对照](https://arxiv.org/html/2603.29494v1)还表明query pool与key tile大小共同影响质量/占用；逐tile running-max追加indices且不回删，不等最终整row阈值的exact实现。局部attention 2.65倍、selector相对朴素路径9.12倍与TTFT 1.17倍是三种分母，不能互换，若干视频质量切片仍低于dense。校准、选择、indices/gather、归一化及完整请求均计费；稀疏支持、质量或净费用失配时，保留dense或更保守稀疏计划，另验precision、batch/concurrency和SLO，不由kernel加速签发无损与生产收益。<!-- source-family:SF-2026-ARXIV-2603-29494 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29494` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29494v1)S2.2/3.1–3.2/Eq2–5/Alg1/S4/T1–2及限制，2+2+2=6，仅Pq64/minS/fused index/vector gather/重新softmax接口。A10080GB/InternVL3.5-8B17K/Qwen2.5VL7B26K、Wan14B76K/Hunyuan13B119K/720p50steps6%warm；保51.1<52.7、long59.4<59.9/LPIPS.330>.326、tile runningmax非global exact、三性能分母及precision/batch/concurrency/SLO/CI未披露，未核代码/复现。
~~~~

## KFAC 29108 — TRAIN-PRETRAINING / Ch28

在Somax更新后控制信号两段后、「Optimizer不是与参数化无关的旋钮」前。Canonical外层curvature surrogate在本章；Ch27数据权重只消费，不双写。

~~~~markdown
曲率还有不同于inner optimizer的一位消费者：外层数据权重或超参数更新需要inverse-Hessian-vector product来形成hypergradient，可用逐layer的Kronecker factors近似这一求解，而不改名为新的内层优化器。Hessian到GGN/Fisher、再到block与factor期望分别丢信息，empirical Fisher不是一般Hessian，factor damping也不等完整曲率加同一λI。[受限KFAC双层对照](https://arxiv.org/html/2603.29108v1)支持一种outer近似接口，不授普通深网exact hypergradient或一般收敛；线性平方实验恰在其精确regime，固定CG次数也不是等墙钟预算。曲率制备、factor状态/刷新、外内循环和调参全付费，cadence最优记述与表中反侧、BERT可训层人口变化及直接EM更强更便宜仍须保留。近似、阻尼或质量费用失配时保留CG/较简单unrolling或原外层配置，内层继续使用已验收step，不把少一份IHVP成本当全部训练更便宜。<!-- source-family:SF-2026-ARXIV-2603-29108 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29108` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29108v1)S2–7必要，2+2+2=6，仅outer IHVP/hypergradient逐层Kronecker surrogate与bias/damping/cadence接口。保linear-square exact regime/N100、τ1loss1.24优于τ5 1.33记述冲突、Res18/CIFAR10/1000iterations/grid费、BERT100M可训1/7/12层与L2/判分人口变化，EM更强便宜；不采非奇异即强凸/PSD即CG保证，不采有害配方；未核代码/复现。
~~~~

## Metriplector 29496 — MODEL-TRANSFORMER-LAYER / Ch17

在fixed-point solver/residual分支及其SF2605-12466 marker后、FROST「还有一条不求fixed point」前。明确是不同参数化，不把场演化写成fixed-point保证。

~~~~markdown
反复计算也可改变被更新对象，而不只重用同一feature变换：让输入表示配置场的算子与source，从新初始化的field开始有限演化，再由演化后的field及其空间梯度组合读出结果。这里representation负责配置operator，field负责数值状态，readout负责交回任务，三者不等同于求共享Transformer状态的fixed point。[Metriplector的受限实例](https://arxiv.org/html/2603.29496v1)提供此替代primitive，但图像的coupled field与语言的因果一维scan是任务特定实现，不是同一算子直接覆盖全部域；有限CG/Euler和Noether命名也不认证精确解、守恒或symplectic执行。算子/field状态、求解与反向、substeps/readout全部付费，语言模型的参数、token/context和硬件预算并不匹配GPT对照，较少训练token不证明净计算更省。数值条件、readout或质量费用失配时保留标准layer、显式loop或已验固定深度，分别验任务与数值误差，不由物理术语批准普适架构优势。<!-- source-family:SF-2026-ARXIV-2603-29496 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29496` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29496v1)S3.1–3.5/Eq15–19/S4T3–7/S5，2+2+2=6，仅input h配置operator/freshψ演化/readout分责。保CG40–60与Euler有限误差、CIFAR组合改变/去J与fromψ反侧、LM18.5M/2B/512/GH200对9.8M/7.2B/1024/8H100非matched compute、156vs80GPUmin/不同quant，不授守恒/全size或净优；未核代码/复现。
~~~~
