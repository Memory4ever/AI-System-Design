# 04945 STaR-Quant：必要Source/实际owner与最小PRE提案

作者supp_20260605_author，2026-10-24。恢复重读当前AGENTS/合同/Prompt/来源说明、每日/arXiv/恢复、ROADMAP、Books三公共上下文与仅本2026路由/本日停点。R27–28既成StreamMA已I实际采用，累计新增I7，原Kimi另保/DistIL7争议不变；不第三既成Source/POST。04945准入与Jun04联合日证R13–14复用，不重AB/date；本次只本单篇必要层。

## 精确版本和必要读域

[官方exact-v1 HTML](https://arxiv.org/html/2606.04945v1)已实际实存`SUP_2606.04945v1_20261024.html`，同日官方abs/notice与exact DOI原件保留复用。必要读§3 SGAT/TAC全部方法和公式、§4设置/Table1–4/消融、Limitations、A计算一致性/B校准实现/C TAC全部统计与稳定化/D W8A8表及E直接限制。未核全代码/复现实验、未扩相关引文；支持与直接反侧已足够。因state-gate的条件等价和actual-owner知识缺口而深入，保持2+2+2=6。

## SGAT不等于无条件等价旋转

§3.2按当步masked/unmasked index把token分组，使用共同正交基P=[Ush,Um,Uu]，Gm/Gu二值gate保shared与本状态子空间、把另一状态坐标置零，激活为Xs P Gs。两组量化/投影后scatter回原顺序，统一静态weight-side P^T W^T校准后量化一次，无两份state权重。B默认dm=du=d/32，余shared；随机Gaussian正交化初始化，只更新变换基、原模型参数冻结，逐层AdamW 1e-3/batch4/15epochs。这是有优化的PTQ calibration，不是“无训练所以零准备费”。

A Eq25明确给出充分条件Xs P (I−Gs)=0，此时gate后的浮点linear结果可与原计算一致；不是必要条件，仅P正交也不够。一般差额Δs=Xs P(I−Gs)P^T W^T还受weight作用，不能把非活跃activation非零直接等同输出误差必非零；layer reconstruction同时承担子空间allocation误差与量化误差，不保证优化后非活跃分量严格零，也不由浮点条件授量化无损。因此不采用“单权重保持任何输入原计算”的宽说法；它是可校准有损state-conditioned接口，不把d/32视为普适最优。共享weight减少重复驻留，却不免partition/gather、transform/gate、activation量化和scatter费用。

## TAC是固定统计补偿，不是逐步在线控制器

§3.3/C在Softmax(QK^T/√dh)V之后、Wo之前，对每层每块拟合affine M、bias；默认g16，不能整除时选不超过16的最大约数。SGAT学完后采paired FP/quant attention representations，C明确FP pass关闭quantizers但保留学得transformation modules，故reference不自动等于未改原模型全部状态。按校准token人口估计mean/covariance，先做damping与eigenvalue clamp的covariance matching，再平滑singular values、向identity shrink，最后重算bias使mean匹配。

C默认最多64calibration samples、dampingρ3e-4/ε1e-8、SV smoothingη.15/identityα.55，参数在inference固定，不是每t独立拟合或实时探测误差。正文temporal指减少多步去噪中representation偏移传播，不证明任意schedule长程稳定。damping/clamp/shrink改变精确covariance匹配，matched二阶统计更不保证逐token数值/完整distribution/任务保真；“closed form”不等全模型最优误差解。未披露具体time采样/权重及跨schedule支持，保为外推限制，不补造轨迹校准细节或融合Wo零运行费。

## 评价、反侧、性能范围

§4.1：NVIDIA A40（未另说明项），LLaDA8B/LLaDA1.5-8B/Dream7B；W4A4，activation per-token/weight per-channel uniform quantization；128 WinoGrande segments作calibration。QuaRot按其official实现加入GPTQ。Table1含知识/推理/代码9任务，均值优于作者所选PTQ baseline但并非FP无损：三模型FP均值58.99/69.86/66.94，W4A4为57.07/66.93/63.59；PIQA在LLaDA与LLaDA1.5低于DLLMQuant++，Dream MMLU也低于QuaRot/DLLMQuant++。HumanEval超FP的局部数值不能认证整体能力提升，重复/CI未披露，不能只看小差值定稳健排序。D W8A8仍有任务/均值损伤，未证2/3bit或更多模型/schedule。

Table2去TAC/SGAT均值55.43/56.39低于组合57.07，支持两分支在该配置的增量，不是机制独占因果。Table3 g4/8/16/32/64均值52.48/54.66/57.07/56.39/56.03，larger block不单调，g16是有限校准下选择。更多covariance表达换估计噪声，不能由二阶拟合授更大总更好。

§4.4/Table4声明沿QuaRot W4A4 kernel/protocol，A40三模型tps相对FP16约1.64–1.69x、peak GPU memory约3.05–3.14x减少；这是作者结果，未复现。必要域未给input/output lengths、denoising steps/schedule、batch/concurrency、完整warmup/repeats/CI或service SLO，不能由“follow另一论文protocol”补其未写条件。无仅量化baseline分离SGAT/TAC增量开销，速度不能全归本两模块；runtime precision/kernel support亦非所有INT4 backend相同。Limitations承认dedicated fused kernels仍有改进空间，不采用无运行overhead/任意服务加速或峰值memory即完整部署memory。校准轨迹、原/quant前向、基优化、统计eigendecomp/SVD、量化/packing和真实kernel/任务回归均计费。

## 实际owner差额及精确两段提案

2+2+2=6：增量是mask-state选择有损activation子空间而共用weight artifact，及固定attention-consumer统计补偿的限定接口；不是给已有旋转、均值匹配或INT4原则加分。唯一owner `INFER-TENSORRT-LLM`，Ch49“粒度与校准决定谁共享同一份误差预算”组；现静态/动态校准段只分提前统计与在线scale，已有视频格式一致性/递归rounding与VLA downstream统计不解释本两状态子空间gate的条件等价及TAC固定state/time人口。实际读Ch49上述完整组、邻Ch48/50开头；Ch24拥有去噪生成语义，本项交付量化artifact/执行费用，不复制另一owner。

建议仅下列完整前段后/完整后段前两段，无本项新Books授权，待非writer必要Source/owner/PRE。

前完整锚：

> 静态 calibration 提前用代表性数据确定 activation 范围或重构目标，运行时路径较轻，但分布漂移会使旧 scale 失配；动态量化根据当前输入计算 scale，降低对固定范围的依赖，却把 reduction、转换和 metadata 带入热路径。Weight-only 的最简单方案也可以直接从权重统计定标；是否需要校准样本取决于量化目标，不能把所有 PTQ 都写成同一种准备流程。

拟新增literal两段：

> 量化人口还可能在同一次去噪中分成masked与unmasked两类。一个受限分支让两类activation使用同一正交基的shared及各自子空间，将另一状态坐标gate为零，再消费同一份已折叠变换的静态量化weight，最后scatter回原token顺序。共用weight避免两套驻留，却不保证原计算等价：原文给出的充分条件是该状态在被关掉的子空间没有分量，此时gate后的浮点linear结果可与原计算一致；一般仍有allocation与量化误差，须由逐层重构校准和完整任务验收约束，不能把正交或单权重当无损证明。
>
> STaR-Quant还在attention的softmax-value结果进入输出projection前，按块用paired参考与量化表示的均值/协方差拟合affine补偿，经damping、奇异值平滑及identity shrink后冻结；这不是每个去噪步在线纠错，reference保留已学变换，统计对齐也不认证原模型分布。有限W4A4对照仍损FP质量，较大块和个别任务会反退；未写清长度、步数与并发的作者速度/显存倍率不授服务SLO。状态划分、校准时间人口、基/weight、补偿与kernel须共同绑定，校准优化、分组变换/量化、scatter、补偿及回归全计费；schedule或输入支持漂移、质量或净成本不合时，重校准或保留统一变换、较高精度与原FP路径，不由固定统计签发长程稳定。<!-- source-family:SF-2026-ARXIV-2606-04945 -->

后完整锚：

> 同一模态内部的 token 也不必共享相同校准权重。一个受限分支沿参考 activation 到当前 activation 的路径，对浮点与量化 block 的输出差进行积分梯度估计，再把 token 级代理用于原 channel-wise equalization 的 scale search；weight-only 与 weight–activation 的参考路径不同，这不是运行时动态分配 token 位宽。校准 artifact 因而还要绑定 reference、标量误差目标、跨 token 聚合、剪裁与权重归一规则，而不能只登记“用了梯度”。<!-- source-family:SF-2026-ARXIV-2603-17809 -->

## 当前阶段交接

本项必要Source/actualowner/两段literal已ready；尚未非writer必要层或root新窄授/Books SAVE/POST/I，不预DAY。既成新增I7和原Kimi旧I另保、DistIL7争议不第三。机构差额/主题有界发现与剩余题摘ordinary尚可执行，本轮到单篇ready即交root释放slot，不把旧73/706导航当配额、不冒外阻归零。只本日记录；无State/index/其他日期/共享Books技术正文写入，无stage/commit/push。

## 当前R29–30采用与真实SAVE

实际读回reader R29–30，必要Source/actualowner/PRE通过；按唯一修句把Eq25明确为充分条件，且只约束gate后的浮点linear一致，不写必要条件/iff/量化无损；原证据笔记对应“才”也已窄修，Eq28受weight作用保留。root本轮新窄授后，Ch49静态calibration完整段后/积分校准完整段前原两段加唯一修句和本人true-H2注已实际保存。作者真实完整自读新增两段、完整直接两侧和本人注；去掉本两正文段和本人一注后Ch49完整字节校验与写前一致，其他正文/他注未变，原literal两段逐字存在、正文family marker恰一处。

当前待唯一非writer actualPOST，不预I/DAY；既成新增仍7I、旧Kimi另保/DistIL7争议不变。本写入阶段即交root释放slot供唯一POST，不扩第三Source/PRE或新Methods；随后本日机构差额/主题和题摘仍ordinary。无State/index/他日写入、无stage/commit/push。

## 当前R31–32既成采用

reader R31唯一actualPOST已通过，04945整合生效且窄位释放，R32行政保存态窄核通过；累计新增I8，旧Kimi另保（合计9I），DistIL7双争议不变。作者只行政同步README/本人注/source/恢复，不第三旧必要层/正文/POST，不以此授DAY。当前普通项在机构/有限发现/题摘层。
