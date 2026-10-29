# 第17章 Transformer Layer

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-TRANSFORMER-LAYER`
**Legacy Chapter:** Ch17
**Status:** Draft

**Roadmap Intent:** Residual、Normalization、Attention、MLP 如何组成可堆叠模块。

## 本章要回答的问题

第15章的 Multi-Head Attention 已完成跨 token 混合，第16章的 MLP 又把逐位置非线性变换的结果投影回 `[B,T,d_model]`。两个子层的接口已经对齐，但还缺少把它们接成深层网络的规则：Multi-Head Attention 与 MLP 单独都能计算，为什么不能简单首尾相接并无限堆叠？梯度为什么会随深度消失或爆炸？Residual connection 和 Normalization 分别稳定了什么？Pre-Norm 与 Post-Norm 为什么会改变深层训练行为？

本章的核心判断是：**Transformer Layer 是一个保持 residual stream shape 不变、并显式管理跨层信息与梯度路径的可堆叠状态更新单元。**Attention 负责跨 token 混合，MLP 负责逐位置变换，Residual 保留信息与梯度短路，Normalization 控制子层输入尺度。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`d_model` 表示 hidden dimension，`H` 表示 Query head 数，`d_h` 表示单个 head dimension，`d_ff` 表示 MLP 中间维度，`L` 表示 layer 数。

下面先把标准 Layer 的前向计算、shape 与堆叠接口走完，再解释深度增加后的梯度约束。随后讨论改变 Norm、跨层状态和执行次数的条件分支；它们分别改变不同约束，不构成一条必须逐级升级的架构路线。

## 直接串联为什么难以堆深

最朴素 block 可以写成：

```text
Y = MLP(MHA(X))
```

每层都完全覆盖上一层状态。深度增加后，早期信息必须穿过所有非线性变换，梯度也只能沿同一长路径反向传播。子层输出尺度变化还会逐层放大，训练更容易不稳定。

另一条更受限的稳定分支，是先把token混合约束为正交线性映射，而只在最后读出时加非线性：若同一个反对称K生成U(s)=exp(sK)，混合路径保持范数，同一总s拆成增量后换序仍相同。[受限混合对照](https://arxiv.org/html/2606.15085v1#S3)的保证止于这条路径；插入逐层MLP、换生成元或加residual后，都不能自动沿用Jacobian条件数1与交换性。不同s本来给不同函数，一次计算U(s)也不因s较小就更省，质量不保证单调；局部生成元的长度迁移还可能失败，全局频率分支只在有限transport得到支持。正交性限制内容依赖路由，不替代Attention与非线性特征的能力；矩阵指数/频率计算、训练和完整消费者回归仍付费。需要causal逐token生成、内容选择或实际质量/预算不合时，保原Attention—MLP与identity residual，不由混合路径稳定签发全网络可训练、无损换序或免费anytime推理。

<!-- source-family:SF-2026-ARXIV-2606-15085 -->

我们希望每个 layer 只是在已有表示上学习一个增量，而不是从头重写全部状态：

```text
new_state = old_state + learned_update
```

这就是 residual stream 的核心。

## Residual connection 保留恒等路径

若子层函数为 `F`：

```text
Y = X + F(X)
```

只要 `F(X)` shape 与 `X` 相同，就可以相加。对于 Transformer：

```text
X shape = [B,T,d_model]
F(X)    = [B,T,d_model]
Y        = [B,T,d_model]
```

Residual 提供两种能力：

第一，信息可以沿 identity path 跨层传播，子层只需要学习有用修正。

第二，梯度包含直接项：

```text
dY/dX = I + dF/dX
```

即使 `dF/dX` 在某些方向很小，梯度仍有 identity 路径。Residual 不能保证任意深网络稳定，却显著改变了优化条件。

层内相加需要同shape，不代表所有层必须处理同样多的坐标。另一分支为各层选择不同active宽度：缩小时截去尾坐标，重新扩展时从该坐标最近一次被active处理的位置恢复，只有从未存在的坐标才填零。这样可把网络理解为较宽global residual上按层选择读写子集；暂不计算不等状态已删除，恢复旧坐标也不等它已随窄层更新。[Variable-Width的受限构造](https://arxiv.org/html/2606.18246v1#S2)在相同输入输出embedding下重定首末接口，改变的是残差状态/算子安排，不是对旧checkpoint无损剪枝或任意宽度热切换。

在忽略边界修正的bulk参数匹配下，平方宽度和近似固定而平均active宽度可以下降，dense投影计算却不因此下降，减少的主要是attention点积项与对应KV槽；更宽global状态、resize搬运及多shape kernel另计。原件resize消融中回读旧坐标优于填零/学习投影，仍只支持受测规模和训练选型，MoE及若干任务有反退；fit得到的等loss计算比例不等墙钟。宽度/坐标历史、首末映射、head与KV布局、训练和全部kernel/TP/PP回归都须绑定付费；质量、shape或净预算不合时，保等宽层栈、原cache与独立任务验收，不由平均宽度或理论FLOPs批准总显存、服务SLO或无损扩缩。<!-- source-family:SF-2026-ARXIV-2606-18246 -->

恒等路径还允许选择是否执行整个block，而不只在执行后缩小更新：冻结旧权重，让轻量router读取前层状态，为本层提出跳过、执行一次或重复一次，得到输入相关的有限深度路径。[受限监督路由分支](https://arxiv.org/html/2510.12773v1)用离线搜索出的正确路径教router，这些标签依赖已知答案和搜索人口，不是线上最优路径真值；训练时按标签执行、部署时按自身决定执行，也会改变后层router看到的状态。重复同一block不等免费增加新知识，跳过也不保持原模型函数；路径、router和每次block调用的KV身份须共同验收，不能从相同hidden shape推出缓存兼容。全部离线搜索、router训练/读取及重复计算均付费，域外质量有反退；路径、缓存或总预算不合时，保留原单次完整层栈与独立质量检查，不由较少平均执行层或冻权重批准无损和净加速。

<!-- source-family:SF-2025-ARXIV-2510-12773 -->

保留 identity 也允许对已经计算出的层更新提出较窄的干预候选：用末层词表 head 读各层状态，在差向量非零时比较相邻两次预测分布差的余弦；方向明显反转时，将当前状态与前层状态插值，相当于衰减当前 residual 增量。这是 readout 条件下的方向信号，不是真实 loss gradient，也不能把被选层命名为幻觉来源；中间表示与末层 head 的失配仍可能改变读数。[有限研究](https://arxiv.org/html/2606.00819v1#S4)报告质量随启用层段、阈值和混合强度变化，部分任务/配置仍反退。但原文对混合系数方向的文字与公式相反，伪代码也未闭合分布制备、改后状态传播、cache 和零差向量处理；这里只采用公式定义的局部插值候选，不把所报质量表当成完整执行路径已验收。计算信号前已执行该层，还增加词表投影、softmax 与插值，不能因称作 skipping 就登记省算。代理、传播语义、质量或完整执行费不合时，保留原完整层栈、末层读出与独立任务评价，不由低方向一致性签发事实、无损分布或加速保证。<!-- source-family:SF-2026-ARXIV-2606-00819 -->

若目标是给整个 block 的输入扰动一个可证明界，就要收紧分支本身，而不只保留 identity。一条条件构造把更新写成凸势的负梯度 Euler 步：MLP 为 `x−τWᵀReLU(Wx+b)` 且 `τ≤2/‖W‖²`；attention 把 value 与约定的投影绑定为 `V=A`，以 `x−η softmax(xᵀAy)Ay` 更新，在固定 compact domain 上限制 `η≤2/sup‖Ay‖²`。这样的 query 非扩张性依赖 tied weights、符号、步长与逐层域；普通自由 Q/K/V 的正向 residual 不自动满足。context 则有自己的 Wasserstein-1 Lipschitz 常数，不继承 query 的1。<!-- source-family:SF-2026-ARXIV-2602-15503 -->

[这一形式架构的近似定理](https://arxiv.org/html/2602.15503v1#S4)限定 scalar 目标，以及目标 Lipschitz 类与 lift/project 架构可实现类的交集；lift/project 自身也不能随意破坏界。它不授任意参数网络、vector 输出、可训练性或无限 token 的有限成本，更不是部署安全证明。逐层 compact domain 和 supremum 的认证可能很难，约束会限制表达与优化选择；缺少这些前提时，旧 residual、Norm、梯度/扰动实测与独立质量验收仍是工程基线。

表示还可在 Attention 与 MLP 更新之后走一条粗子空间修正分支：先把 hidden state 限制到较小空间，求解粗系数并延拓回原 shape，再以可调强度与原状态混合；若使用多个粗尺度，可另学非负归一化权重。[这一受限构造](https://arxiv.org/html/2603.09815v1#S6)改变的是每层内部的表示与额外计算，不是免费恢复原 identity，也不同于把输入 embedding 作为共享 anchor。真正正交的 P 下，`αI+(1−α)P` 在 `α∈[0,1]` 时不放大固定输入扰动；独立学习的 restriction/prolongation、带稳定项的 coarse solve 或多尺度混合，则不能仅凭“投影”名称继承此界。
<!-- source-family:SF-2026-ARXIV-2603-09815 -->

抑制某些方向有利，仍以任务信息主要留在保留子空间为前提：有用信号若在被压低方向，也会损失。有限 encoder 分类、人工类不平衡与句子噪声对照不能证明大规模生成模型普遍稳定或更快；全序列 temporal projection 还必须另证 causal prefix invariance。coarse solve/QR、额外参数、迭代、多尺度与训练调参都纳入训练和部署预算，学习到的 oblique operator 要检查条件数与放大而不自签平滑。算子、held-out 质量、因果性或完整费用未通过时，保留标准 residual/Norm 和原 Attention/MLP，不将启发式训练曲线当普遍收敛保证。
<!-- source-family:SF-2026-ARXIV-2603-09815 -->

跨层保留信息还可另开投影 anchor 分支，而不把第一层同时当作通用参考与逐层计算起点：从 input embedding 用额外的 Q/K/V/gate 投影构造共享 anchor，各层先归一化 anchor，再与当前投影学习混合，之后对混合 Q/K 执行 QKNorm/RoPE、计算 attention 并应用 gate。[ExoFormer 的受限分支](https://arxiv.org/html/2601.08131v1)改变的是 attention 子层的信息来源；这条有投影、有混合的旁路不等于原 identity residual，更不能直接继承上式的导数 I。原 identity path 仍保留其梯度短路职责。<!-- source-family:SF-2026-ARXIV-2601-08131 -->

新增四个投影带来额外参数与缓存/计算状态，归一化次序和 Q/K 尺度又影响能否稳定复用。作者约450M参数、10B tokens、H100/BF16、sequence2048的比较支持局部设计选择，不是完整容量匹配或长上下文证据；部分任务也未改善。外 anchor 模型内部 token similarity 更高、维度更低却表现较好，支持进一步检查“信息被外部分支承载”的 offloading 假说，不证明 token identity 必被保留或 collapse 具有普遍因果收益。成本、归一化或 held-out 质量不成立时，保留普通 residual、单值复用或单独 gated attention，而不因诊断曲线推荐所有层都外置 anchor。

跨层复用还可以不只回读 input embedding，而保留前面 block boundary 的中间状态。普通 residual 把它们累加进当前状态，within-layer LoRA 则改变本层算子；另一条适配分支在边界处用当前状态的 pooled query 读取先前状态，再以 gate 加回当前表示。视觉与文本可分别生成 query、读取各自历史，同时保留 backbone 的跨模态 self-attention。这是条件化的跨深度消费路径，不是旧 residual 的精确替代，也不由模态分流证明语义已解耦。<!-- source-family:SF-2026-ARXIV-2603-26330 -->

[IADA 的受限 VLM 适配对照](https://arxiv.org/html/2603.26330v1)中，input-adaptive 的共享路径已取得大部分增益，独立模态路径只作局部细化，部分感知平均分还略退。新增参数、学习率与检索计算未完全匹配，故恢复 reasoning 分数不唯一诊断为旧表示访问丢失，更不证明所有低秩更新需加 depth router。历史 states、attention、gate 与任务回归均付费；原文 sigmoid gate 的近零参数也不等恒等初始化，这里不采用该稳定证明。适配、modality mask、开放生成或完整费用不合适时，保留普通 residual、层内 LoRA、固定聚合与原外 anchor，按真实消费者质量决定读取路径。<!-- source-family:SF-2026-ARXIV-2603-26330 -->

显式读取此前各层时，深度极限也不必沿用只消费当前状态的局部残差解释。一类稠密连接把当前输入支路与此前层输出的加权和共同送入变换；若在固定深度区间把网格步长取为tau=1/L，历史和可视为沿过去深度的积分，权重同时依赖消费层与来源层。这个视角把跨层记忆本身纳入状态合同，而不是只给当前hidden增加一个恒等短路；某些可微或可增广的特例仍能写回局部动力系统，并非积分与ODE互斥。

[受限的稠密非局部建模](https://arxiv.org/html/2510.02049v1#S3)提供这条表示分支，但固定有限网络中能把tau吸收进权重，不等于跨深度的正则优化问题仍相同。分析连续极限还要控制参数幅度和跨层变化，并声明插值、函数空间与收敛对象；全局最优值或极小元聚点的结论不能替SGD轨迹、测试泛化或任意Transformer稳定性签字。原稿显式状态界存在独立偏置项反例，因此这里不采用该界或完整稳定保证。保留历史状态、双时间权重、正则差分与全部训练/验证都有费用，较低训练loss也不证明净算力收益；假设、估计或实际质量无法核清时，保留有限层实测、普通Residual/Norm及离散历史读取，不由连续极限名称自动批准更深网络。

<!-- source-family:SF-2025-ARXIV-2510-02049 -->

跨层选择也可以放进attention内部，而不另存一组hidden history：对同一token，用当前层query读取当前及前面选定层的keys，混合当前raw Value和那些层已经混合过的Value，再让普通causal attention读取这个结果。Depth-Attention的受限分支把mixed Value原位写入标准V-cache槽，保留原Q/K和mask，因此不扩大持久KV的shape；它却改变了Value内容与后续消费语义，并不是对旧checkpoint或raw KV的无损替换。GQA可在组级读深度，稀疏stride又限制跨层source数，不能把固定半深stride视为普适最优。

同shape状态复用省去了额外持久buffer，但训练activation、depth读取以及pipeline跨stage通信仍付费。有限1.5B/3B同训练条件的比较有逐任务反退，算术FLOPs很小也不等墙钟为零：未融合PyTorch路径中训练和推理均有开销，更密source并不总更好。128K内存估算不是实际长Context服务证据，fused kernel和更大规模收益尚未验证。质量、cache构造身份或跨设备成本不合时，保留普通residual、原attention与独立hidden路由基线，不因无新增参数或持久槽就承诺速度与SLO。<!-- source-family:SF-2026-ARXIV-2606-05014 -->

## Normalization 控制什么

Residual 保留旧状态，但每次新增的 Attention/MLP 更新仍可能改变尺度。归一化先解决子层接收到什么尺度的输入或输出；其放置如何影响反向传播，待完整 block 建立后再分析。

Layer Normalization 对每个 token 的 hidden dimensions 计算统计量。对向量 `x in R^(d_model)`：

```text
mu    = mean(x)
var   = mean((x-mu)^2)
x_hat = (x-mu) / sqrt(var + epsilon)
y     = gamma elementwise_mul x_hat + beta
```

`gamma`、`beta` 是可学习参数。对于 `[B,T,d_model]`，统计通常沿最后一个 `d_model` 维计算，不在 batch 或 token positions 之间混合。

Normalization 让子层面对更稳定的输入尺度，降低参数更新导致 activation distribution 剧烈漂移的风险。但它不是把所有信息变成相同，也不能替代学习率、初始化和数值监控。

RMSNorm 等变体省略均值中心化，使用 root-mean-square 缩放。具体模型采用哪种 normalization 属于 checkpoint 架构，不应把二者混成同一个公式。

均值中心化还给表示诊断一个可直接核算的约束：若所有γ坐标非零，同一LayerNorm输出的`(y−β)·γ^-1`逐样本恒为零，所以跨样本中心化后的covariance在γ^-1方向必为零；γ为零时则单独处理该常量坐标，不能直接取倒数。这是[LayerNorm代数核](https://arxiv.org/html/2606.19491v1#S3)，不依赖训练是否已学到某项能力；在所有γ坐标非零时，RMSNorm没有由γ单独强制的同一通用核，却仍可能因数据人口或训练退化而出现小特征值。诊断必须固定hook、affine、人口与计算精度，分开centered covariance和含均值的raw Gram：β带来的常数投影不能被读成新信息，近零数值的比率也不自证训练产生更深的核。低方差不等语义无用、错误或可安全删除；读数低于精度地板、校准不覆盖真实模态或对象不一致时，应提高/核对测量精度并回到任务与原模型回归，而不是按一条谱值批准剪枝、adapter放置或架构替换。<!-- source-family:SF-2026-ARXIV-2606-19491 -->

两者也不必一概视为不可转换：若LN输入为`h=Wx+b`，可用`P=I−11ᵀ/d`把权重与bias改成`PW、Pb`，再保留相同epsilon及输出affine，以RMS缩放得到同一实数函数；这不是直接把原LN换名为RMSNorm。[受条件的centering折叠](https://arxiv.org/html/2605.14521v1)还要求检查被改写输出的所有消费者：残差各支、额外fanout与中间非线性不能只凭零均值标签放行，训练中的逐坐标dropout也可破坏等价。部署转换不自动延伸成任意图或继续训练的等价配方，浮点容差与真实kernel仍须验证。一次图检查/权重重写、辅助centering及独立质量和总延迟都计费；条件或净收益不成立时保留原LN，不因RMS算子较少就批准checkpoint兼容。<!-- source-family:SF-2026-ARXIV-2605-14521 -->

控制均值和尺度，也不等于规定了activation的完整分布形状。一条受限训练分支在原Norm之后、affine之前估计power transform的形状参数，再按变换后样本的平均绝对偏差缩放Gaussian噪声；噪声尺度停止梯度，噪声本身只在训练期使用。[Normality Normalization](https://arxiv.org/html/2505.00685v1)的形状参数来自局部二阶近似的一步估计，不是新增learned参数，也不证明原似然已达全局最优；Batch分支部署还要保存训练running均值、方差和形状估计，不能由“无新增参数”推无状态或把这份Batch合同搬成每token的LayerNorm。更像Gaussian的边际不保证联合Gaussian、独立特征或最优语义容量，原归一化也不为形状估计的零曲率/退化统计提供完整guard。估计、log/power、噪声、状态与完整训练/回归都付费，所测图像模型的更慢训练与近似测试耗时不授现有LLM可直接换层；支持、数值、质量或总费失配时，保原LayerNorm/BatchNorm/RMSNorm与已验配方，不能只凭分布更正态批准checkpoint兼容或真实鲁棒性。<!-- source-family:SF-2025-ARXIV-2505-00685 -->

## Post-Norm：原始 Transformer 的顺序

原始 Transformer 的常见 Post-Norm 抽象为：

```text
U = Norm(X + MHA(X))
Y = Norm(U + MLP(U))
```

每个子层输出先与 residual 相加，再 normalization。最终 `Y` 保持 `[B,T,d_model]`。

Post-Norm 让每次子层输出后的状态都被归一化，但跨很多层的梯度 identity path 仍会经过 Norm Jacobian，深层训练可能更敏感于 warmup、初始化和学习率。

## Pre-Norm：先归一化再更新

许多现代 decoder-only 模型使用 Pre-Norm：

```text
U = X + MHA(Norm(X))
Y = U + MLP(Norm(U))
```

Residual identity path 从 `X` 到 `Y` 不必穿过子层 Norm。这样通常更容易训练深网络，但最终输出尺度和表示行为与 Post-Norm 不同，模型末端常还会有 final norm。

Pre-Norm 并非无条件优于 Post-Norm。两者的表达、训练动态、初始化和最终性能要在具体架构中比较。稳定结论是：Norm 放置改变了梯度路径，不能在加载 checkpoint 时任意互换。

前向尺度与反向传播还可以采用不同的局部规则，而不只是给 residual 乘一个普通系数。一条[受限训练分支](https://arxiv.org/html/2506.22049v1)从子层相加后的状态中减去带 stop-gradient 的门控副本：前向改变该状态的尺度，反传到这份状态的局部 Jacobian 却保留 identity，门参数仍按自己的路径学习。这改变了 block 的训练合同，不等于原网络的全部梯度或优化轨迹保持不变；初始门为零时的首轮相同，也不保证之后等价。门可放大而非始终压低 activation，数值域、归一化的 epsilon、反向路径和 checkpoint 中的门/optimizer 状态必须共同定义实现，不能从尺度较小推信息无损或稳定证明。局部对照中固定门、替代插入位置与部分下游任务反而更差，门更新还可能产生梯度尖峰；简化理论中的上界也不能证明实际梯度永不消失或爆炸。额外逐层算子、门训练、监控/裁剪和达到同质量目标的完整训练均计费，较少 steps 不自动等于较低墙钟费用。质量、门域、数值稳定或净预算不成立时，保留原 Pre-Norm、已验初始化/学习率与普通梯度监控，而不是给现成 checkpoint 任意加尺度门。<!-- source-family:SF-2025-ARXIV-2506-22049 -->

Norm位置还会改变前向表示运动的速度，而不只改变反传路径。把非零token写成半径r与单位方向theta，连续深度下方向导数是原更新在球面切空间的投影再除以r；归一化放在读取前、相加后或更新支路内，便可能产生不同的token依赖速度，而非把同一条轨迹统一加快或减慢。[受限attention-only分析](https://arxiv.org/html/2510.22026v1)由此比较Pre/Post/Peri-Norm的聚类动态，但其tied或identity矩阵、随机初始化与终端窄cone等假设不能迁给有FFN的训练后decoder；局部多项式/指数速率也不是训练梯度或任务质量排名。半径增长会改变有效更新，应与角向变化分开诊断，仍支付完整训练与有限深度回归；模型或假设不合时保留已验Norm/residual配方，不从球面解释推出Peri普遍最佳或checkpoint可互换。
<!-- source-family:SF-2025-ARXIV-2510-22026 -->

## 一次完整 shape 流

假设：

```text
B = 2
T = 4
d_model = 8
H = 2
d_h = 4
d_ff = 32
```

Pre-Norm layer 的逻辑 shape：

```text
X                         [2,4,8]
Norm(X)                   [2,4,8]
Q/K/V reshape             [2,2,4,4]
Attention scores          [2,2,4,4]
Head outputs              [2,2,4,4]
Concat + output projection[2,4,8]
U = X + attention_output  [2,4,8]
Norm(U)                   [2,4,8]
MLP up / gate             [2,4,32]
MLP down                  [2,4,8]
Y = U + mlp_output        [2,4,8]
```

Layer 内部 shape 会扩展、拆 head 和形成 `T*T` scores，但入口与出口始终是 `[B,T,d_model]`。这使相同 block 可以重复 `L` 次。

## 一个 residual 小例子

假设某 token 当前状态和 Attention 更新为：

```text
x = [1.0, 2.0]
a = [0.1,-0.3]
```

Residual 后：

```text
u = x + a = [1.1,1.7]
```

接着 MLP 产生：

```text
m = [-0.2,0.4]
y = u + m = [0.9,2.1]
```

Layer 没有丢弃原状态，而是叠加两个学习到的增量。真实模型中的更新来自 Norm、MHA 和 MLP，此例只展示 residual arithmetic。

## 为什么顺序是 Attention 再 MLP

典型 block 先让每个 token 读取上下文，再对已混合状态做逐位置非线性变换：

```text
context mixing -> feature transformation
```

这是一种稳定主流设计，不是唯一可能顺序。并行 Attention/MLP、sandwich blocks 或其他变体也存在。本章不构建架构目录，因为无论顺序如何，仍要分析 token mixing、position-wise computation、residual path 和 normalization。

并行化也可以靠改变MLP读取的信号，而不是仅让执行器重排原依赖：保留各层Attention的residual更新，却将MLP输入改为当前层归一化状态加上首层Attention的归一化输出，使它不再等待本层Attention完成。[FAL的受限结构](https://arxiv.org/html/2510.14614v1#S4)因此允许两路并行，并在所测TP布局中先作本地加和再归约；这是需要重新训练和验收的模型图，不是原checkpoint的代数等价替换。另保留当前层依赖、只增加首层信号的质量分支，不能继承同样的通信收益。早层表示复用、训练与多流执行均有成本，较低PPL也不保每项下游质量；信号、任务或执行预算失配时，保留标准串行block或已验并行分支，不由一次归约减少批准全网无损。

<!-- source-family:SF-2025-ARXIV-2510-14614 -->

若不再把每个位置固定为一对Attention与MLP，还可以把两类模块的数量和排列列成有限搜索菜单：先让小宽深候选在便宜的token操作任务上训练，用代理分数筛选，再将候选结构聚合、扩展到目标规模后重新训练。[Composer的受限结构对照](https://arxiv.org/html/2510.00379v1#S3)提供这条离线设计分支，不是将已有checkpoint免费重排或删层。代理排序未必跨任务/规模保持，逐层取众数可能产生未测的新组合，stack/stretch也不能凭参数比率自动保住实际层数与预算；每次交接都需核具体结构、数据和训练身份。部分任务仍会反退，random-weight时延与已训质量不组成同一模型的Pareto，更少Attention/KV也不保证完整训练或Serving更省。候选/超参搜索、聚合扩展、目标重训和独立质量/运行回归均付费；代理、结构或净预算不合时，保留标准交替、已验固定比例与邻规模实测，不从局部最优签发通用Attention/MLP配方。<!-- source-family:SF-2025-ARXIV-2510-00379 -->

搜索菜单也可从完整Attention/MLP模块细化到primitive计算图：以卷积、归一化、矩阵乘法、分支与合并等节点构造DAG，约束边的shape及block输入/输出一致，再按声明的参数/算术预算增删节点或耦合支路。[UniNAS的受限结构分支](https://arxiv.org/html/2510.06035v1#S2)让局部与全局mixing能作为同一接口候选，却不使shape合法等于训练稳定、语义等价或全部架构均可达；外层stage模板与节点库仍限定空间。随机初始化的Fisher proxy只负责提名，不能替代最终训练质量，打印成本与shape未闭时也不补精确budget。搜索、proxy前反向、最终预训/适配及真实运行回归全部付费，相近参数、相同recipe或training-free筛选不等同FLOPs/墙钟/精度预算。该有限视觉对照不授语言模型收益；proxy、图语义或净预算失配时，保标准交替、已验Conv/Transformer/hybrid及实际profile，不由统一图或高分proxy批准普遍可训练、无损重排或免费架构搜索。

<!-- source-family:SF-2025-ARXIV-2510-06035 -->

标准 block 把非线性容量主要放在 Attention 权重和独立 MLP 中，Q/K/V 与输出等 projection 则保持线性，便于实现与成本核算。若目标是在较窄的中间空间增加逐位置函数容量，也可以从预训练开始，把任一线性 projection 改为 `xW + b + σ(xA)B`：A 将输入压到 rank r，σ 在瓶颈中作非线性变换，B 将结果投影回原输出 shape。它不改变该 projection 的外部接口，却改变了内部计算图；不同于[第30章 LoRA](../part-04-training-system/30-lora.md)的冻结基座加线性权重更新，这里的主矩阵也可训练，非线性支路通常不能合并成一个固定的 W，推理时仍须执行。<!-- source-family:SF-2026-ARXIV-2603-06492 -->

这种分支用额外参数、activation 与永久部署 FLOPs，交换达到某一训练损失所需步数的可能减少；因此应比较目标损失下的墙钟成本，而不是只比较步数。[NOBLE 的受限预训练对照](https://arxiv.org/html/2603.06492v1#S4)使用250M/1.5B模型、OpenWebText、长度1024及H100/BF16编译执行，不能直接外推大模型服务收益；ViT 对照中拟合损失改善也没有带来同幅度的验证准确率改善。瓶颈初始化与各参数组学习率另需调校，cosine 输出有界不保证整个支路 Jacobian 或梯度有界，作者的频率解释也不构成泛化证明。推理预算紧、局部收益不能覆盖新增计算或质量回归时，保留线性 projection 与独立 MLP；低秩非线性是有成本的架构分支，不是 residual/Norm 的替代稳定性保证。<!-- source-family:SF-2026-ARXIV-2603-06492 -->

若约束来自投影参数容量，还可把低秩限制放在跨层增量上，而不是把每层完整输出都压进低秩空间：首层保留完整投影，同一位置的后续投影写成 `Y_l=c_l Y_(l-1)+(X_l A_l)B_l`，两项保持相同输出 shape。这里完整历史路径与低秩新增路径共同形成表示，不是冻结基座上的 LoRA，也不由相邻层相关性证明无损。[这一受限分支](https://arxiv.org/html/2509.18993v1#S3.SS3)还让模型图与反向重算互相约束：保存层输入、低秩中间值和若干完整输出锚点，再从后层条件反求前层；只有系数非零且数值条件合格时才有可用的代数逆，小系数与减法消去会放大误差，给绝对值加 epsilon 也不自动解决 `sign(0)=0`。省下权重或优化器状态，仍须支付历史输出、锚点、重算和跨 pipeline stage 传递的费用；有限预训练存在规模与早期步数反退，峰值算力估算也不能当端到端训练或推理加速。质量、数值恢复或依赖预算不合时，保留完整投影、更密保存、普通低秩分支与标准 residual，而不把低秩增量称为免费可逆层。

<!-- source-family:SF-2025-ARXIV-2509-18993 -->

固定二维网格、局部交互足够的视觉负载，还可把部分 context mixing 与 feature interaction 合在一个结构化分支：从 normalized state 构造 detail/context 两路，用 depthwise 局部上下文和 channel shifts 形成逐通道乘法的 dot 项、反对称交叉的 wedge 项，拼接后投影，再经 gate 与 residual 写回。[这类 bilinear mixer](https://arxiv.org/html/2601.06793v1#S3)提供的是稀疏 channel-pair prior，不是恢复所有几何关系或等价于全局 Attention；不单独接大 FFN 的 variant 仍有 dense detail、projection 与 gate 变换，所以逐元素阶段的近线性成本不能授给整个 block。CIFAR-100 的局部作者实验使用额外 DropPath，shift/dot/wedge消融同时改变容量；保留 FFN 的版本略高于 No-FFN，Nano/Fast 训练又分别慢于所比较的 ShuffleNet/MobileNet，不能证明 FFN 普遍冗余或完整质量/预算优胜。Shift 取样与 data movement、dense readout 都要付费，未来 fused kernel 预期不算实测；长距离依赖、不同布局或质量回归未通过时，仍保留标准全局 Attention、独立 FFN 与原残差/归一化路径。<!-- source-family:SF-2026-ARXIV-2601-06793 -->

## Layer 堆叠后发生什么

设第 `l` 层输入为 `X_l`：

```text
X_(l+1) = TransformerLayer_l(X_l)
l = 0,...,L-1
```

不同 layers 通常不共享参数。早期层、中间层和后期层可以形成不同表示与计算，但不能机械地给每层指定固定人类语义。

随着 `L` 增加：

- 参数量和每 token compute 近似线性增加。
- 训练需要保存或重算更多 activations。
- KV Cache 需要为每个 Attention layer 保存 K/V。
- Pipeline Parallel 可以沿 layer depth 切分。

所以 `L` 不只是模型容量，也是 Training 与 Inference System 的关键维度。

<!-- semantic-body-binding:SF-2026-ARXIV-2609-35630:start -->
Residual让写入能跨层积累，但写得大不等于下一子层会敏感地读取这一方向。对线性算子A，输入侧AᵀA描述读方向的敏感性，输出侧AAᵀ描述写方向；二者不能按同一坐标权重互换。若Attention或FFN弱读某些已被写大的方向，局部反馈可能容许这些分量继续累积。因此极值诊断要分开读敏感、写增量和跨层累积，不能只凭activation幅度选择删除坐标，也不能把它归给唯一FFN分支。

[Read-Blindness v1 §3–6](https://arxiv.org/html/2609.35630v1)的有限pre-LN模型与约束干预支持这个解释，但coordinate proxy不是精确null，有符号写入也不总为正；最终极值坐标回溯的时间先后不是因果证明。冻结或正交约束改变训练自由度，阻断一路还可能由其它路径补偿，local AdamW一步probe又依赖存档moment状态。诊断新增算子谱、checkpoint与行为干预成本；没有多路径与held-out质量证据时保留原Residual/Norm，不把局部几何当任意架构抑制方法或训练全程增长保证。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-35630:end -->

## 梯度为什么会随深度消失或爆炸

相同 shape 让 block 在接口上可以重复，并不保证训练时梯度能穿过任意深度。现在回到直接串联方案，对比 residual 和 Norm 究竟改变了哪一段反向路径。

设一个没有 residual 的深网络满足：

```text
x_(l+1) = F_l(x_l)
```

从第 `L` 层的 loss 反向传播到第 `l` 层，需要连续乘上每层 Jacobian：

```text
dLoss/dx_l
= J_l^T * J_(l+1)^T * ... * J_(L-1)^T * dLoss/dx_L

J_k = dF_k(x_k) / dx_k
```

问题不在于“乘法次数多”本身，而在于这些 Jacobian 怎样缩放不同方向。若关键方向的 singular value 长期小于
`1`，乘积会指数式收缩，早期层几乎收不到可用信号；若长期大于 `1`，乘积会迅速放大，微小扰动也可能变成
巨大梯度。真实网络通常两者同时存在：某些子空间 vanishing，另一些子空间 exploding，所以只看一个 global
gradient norm 会掩盖方向和深度差异。

对某层参数 `W_l`，参数梯度还同时依赖 forward activation 与 backward signal：

```text
dLoss/dW_l
≈ input_activation_l outer_product dLoss/dpreactivation_l
```

因此“小梯度”可能来自上游 signal 已消失，也可能来自 activation 饱和、loss mask、数据分布或该层在当前 batch
根本没有被激活；“大梯度”可能来自 Jacobian 放大，也可能是异常样本、错误 loss reduction、mixed-precision
overflow 或 optimizer state 不连续。Vanishing / exploding gradient 是观测到的结果，不是自动给出根因的诊断标签。

Glorot initialization 的出发点正是让初始化时 activation 与 gradient 的尺度尽量跨层保持；He initialization
进一步把 rectifier 的 gating 统计纳入方差设计。它们改善第 0 步附近的 signal propagation，却不会保证训练后
权重、数据与 optimizer 共同演化时所有 Jacobian 仍接近等距。初始化是稳定起点，不是永久 invariant。

### Residual 怎样改变 Jacobian 乘积

对 residual block：

```text
x_(l+1) = x_l + F_l(x_l)
```

单层 Jacobian 变成：

```text
dx_(l+1)/dx_l = I + J_F_l
```

这为梯度增加不依赖 transform branch 的 identity component，使每一层不再只能穿过 `J_F_l`。但 residual 不是
“梯度永不消失/爆炸”的证明：若 `J_F_l` 尺度过大、方向长期一致，`I + J_F_l` 的乘积仍可能爆炸；若更新长期
抵消 identity path，某些方向仍会衰减。Residual scaling、gate 和初始化的作用，是让 transform branch 在训练早期
保持可控，而不是取消梯度数学。

前向累积也不能直接解释成一组独立浅网络的投票。对更新`x_(l+1)=x_l+λF_l(x_l)`，固定有限深度且分支在相关邻域足够光滑时，低阶展开会出现`λ²J_F_j(z)F_i(z)`（`i<j`）：后层在参考状态`z`的导数消费前层造成的变化，而不是把各层单独输出相加。[一条受限深度分析](https://arxiv.org/html/2510.03470v1#S3)支持区分这些交互与显式尺度，但光滑不等解析/级数收敛，低阶近似不能升级为无限展开的精确等式；项数随深度增多，也不证明幅度必爆，零分支、符号抵消和导数范数都影响结果。缩小`λ`同时改变更新与优化尺度，不由固定参数展开决定训练后容量或最佳归一化。作者CIFAR残差网络的极深对照还改变width，深度缩放未恢复BN全部准确率，不能搬成真实Transformer的普遍配方。导数/余项诊断、全部学习率与seed训练、质量回归和实际计算均计费；光滑邻域、数值或任务质量不合时，保留成熟Residual/Norm及已验初始化，按真实Jacobian、loss与任务结果验收，而不是让更深、较小更新或组合项计数自签稳定与能力。<!-- source-family:SF-2025-ARXIV-2510-03470 -->

不保留identity也可以作为重新训练的实验分支，而不是在旧checkpoint上直接删skip：同时把V/O乘积初始化为scaled orthogonal、给Q/K乘积加入mimetic identity偏好，再联合选择MLP初始化与optimizer。[受限skipless ViT对照](https://arxiv.org/html/2510.00345v1#S5)表明这能恢复部分可训练性，却不使权重条件数成为全网证书；重复token仍可令Attention均匀且退秩，实际输入、Norm/FFN与完整Jacobian路径必须另验。AdamW配置仍落后残差基线，SOAP的局部正侧和dense-feature收益也不证明所有深度、任务或LLM应去skip。SVD/初始化、完整重训、optimizer状态、readout选择与质量回归都计费；初始化后传播、任务质量或净预算不合时，保留成熟Residual/Norm与原optimizer，不用更深的名义组合或PCA图替代端到端验收。<!-- source-family:SF-2025-ARXIV-2510-00345 -->

谱曲线也必须绑定这条真实 Jacobian 链，不能把 static weight 的奇异值拟合直接当 `I+J_F(x)` 的传播证书。一类条件分析分别需要归一化、power-law chart 误差、局部 transport budget 与 non-backtracking slack；near-identity scaling 只控制其中的 budget，不自动保证 chart 品质或整条谱路径。进一步从主导谱窗口谈物理 channel 结构，又须声明 transport 的行/列究竟是 physical coordinates 还是 source modes，固定 extraction/rank/support 规则，并核截断误差、core-overlap/noise 与各类 margin。后择排列的热图亮块和部分 checkpoint 测量不能替代完整证书。[谱坐标条件](https://arxiv.org/html/2605.02108v1)与[物理结构条件](https://arxiv.org/html/2605.02111v1)因此是两层不同权限，不是普遍训练稳定或机制因果。SVD、Jacobian/误差测量和规则敏感性均计费，条件不足时回到实际梯度、loss 与任务回归，保留原 residual/Norm 路径。<!-- source-family:SF-2026-ARXIV-2605-02108; source-family:SF-2026-ARXIV-2605-02111 -->

Residual 与非线性还承担两种不同的几何责任。Residual identity path 让相邻层的表示和梯度方向更容易保持相干；非线性则必须真正打破仅由坐标旋转造成的等价方向，网络才能沿深度形成新的可区分变换。因而“存在激活函数”并不充分：若非线性仍保持 rotation equivariance，它可以保留梯度传播，却未必打破所需对称性。

这条解释把 stability 与 expressivity 分开，而不是把跨层方向连续性直接当成能力来源。现有因果干预主要来自 toy MLP 与 34M Transformer，大模型快照只展示相关几何；它们不证明任意架构都遵循同一训练动力学。若对称性假设不成立或经验信号与任务质量无关，应回到 Jacobian、loss 与端到端回归，而不是据此选择 activation。<!-- source-family:SF-2026-ARXIV-2605-04971 -->

Normalization placement 又改变了 identity path 是否必须经过 Norm Jacobian。抽象地看：

```text
Post-Norm: y = Norm(x + F(x))
           dy/dx = J_Norm * (I + J_F)

Pre-Norm:  y = x + F(Norm(x))
           dy/dx = I + J_F * J_Norm
```

Post-Norm 的直接路径仍经过 `J_Norm`；Pre-Norm 把 `I` 留在外侧，因此通常更容易把 gradient 传到早期层。
Xiong 等人的分析进一步表明，原始 Post-LN Transformer 在初始化时靠近输出的参数可能具有较大期望梯度，
learning-rate warmup 能缓和 early update；这不是“所有层梯度都同时爆炸”，也不意味着 Pre-Norm 永远不需要
warmup。数据、optimizer、precision 与架构变化后仍要重新测量。

梯度诊断还要展开 token 与路径，而不只沿层深看一个 norm。因果 Attention 中，某个 value 的局部梯度是后续合法 query 的上游梯度按 attention 权重求和；前向质量集中会提供反向聚合通路，却可能因方向抵消而没有同等大的净梯度。Pre-RMSNorm 又使这一支路的最坏增益受 `||γ||∞/rms(x)` 约束，较大激活可以降低局部上界，但上游梯度、γ 与 residual identity 仍共同决定完整信号。因而高 attention、massive activation 与 gradient concentration 应分别测量，不能把其中一幅曲线当成另两者的唯一原因。<!-- source-family:SF-2026-ARXIV-2603-17771 -->

一条[受限 value-path 干预](https://arxiv.org/html/2603.17771v1#S5)在聚合前将 value 乘以 `φ(r)=r/(r+C)`，其中 `r` 是其平方范数，`C>0` 为逐层逐 head 学习的尺度。小范数 value 的前向贡献和反向信号同时减弱；这不是只改 backward，保持当前 Q/K 权重也不保证后续状态不变。小型 C4 预训练模型保留较强 attention sinks 而减少激活尖峰，支持这两种现象可部分分离，却不证明唯一训练中介、全局梯度收缩或全部能力改善。径向增益在部分尺度仍可大于一，Q/K 与 identity 路径也未消除；新增门、训练与诊断费用必须计入。质量、数值或完整成本未核时保留原 Attention/Norm 路径，不以激活变小直接批准低位量化、长窗或生产稳定性。

### 解决手段属于不同控制层

| 控制层 | 典型机制 | 直接改变什么 | 不能替代什么 |
| --- | --- | --- | --- |
| Parameterization | Xavier/He initialization、residual scale、gate、DeepNorm | 初始 Jacobian 与 branch update 尺度 | 数据/optimizer 正确性 |
| Architecture | Residual、Pre-Norm/Post-Norm、RMSNorm/LayerNorm placement | forward state 与跨层 gradient path | 极端 batch 或 overflow 处理 |
| Optimizer schedule | warmup、decay、parameter-group multiplier | 参数 update 的时间尺度 | 已经消失的 backward signal |
| Update guard | gradient clipping | 限制一次 update 的 global norm | vanishing gradient、长期错误 scaling |
| Numeric policy | BF16/FP16 loss scaling、FP32 accumulation | 可表示范围与舍入误差 | 错误 objective 或 residual topology |

DeepNorm 一类方法把 residual scaling 与匹配的 initialization 联合设计，以约束极深 Transformer 的 model update；
它不是“给深层更小 learning rate”的同义词。反过来，给每层单独调 learning rate 只会在 backward 完成后缩放
参数 update，无法修复 forward saturation、错误 Norm placement 或梯度在到达该层前已经消失的问题。逐层
learning-rate policy 的适用边界留到第 28 章讨论。

### 工程上怎样判断是哪一种问题

一次可信诊断至少把以下量按 layer / parameter group 展开，而不是只看一个 aggregate：

```text
activation RMS / max and non-finite count
gradient RMS / norm before clipping
update RMS and update-to-weight ratio
clipping fraction and overflow / skipped-step count
loss, data batch identity and optimizer step
```

- 早期层 gradient 长期接近零、后层正常，优先检查 gradient path、activation saturation、mask 和 initialization。
- 多层在同一 batch 同时出现尖峰，优先检查数据、loss reduction、precision、collective 与 optimizer state。
- Gradient norm 正常但 update-to-weight ratio 异常，问题更可能在 learning rate、Adam moments、weight decay 或
  parameter grouping。
- 几乎每一步都触发 clipping，clipping 可能只是在隐藏错误 recipe；应回到 unclipped distribution 找根因。

这里的目标不是让所有层 gradient norm 相等。Embedding、Attention、MLP、Norm 和 output head 的参数尺度与功能不同；
健康训练需要的是可解释、可重复、与 loss 改善一致的信号，而不是人为把每层压成同一个数字。

## 从 Pre-Norm 到可控 Post-Norm：问题不只在 Norm 的位置

把架构史简化为“Post-Norm 不稳定，所以被 Pre-Norm 淘汰”会漏掉真正的设计变量。
Post-Norm 的困难来自 residual、transform branch 与 Norm Jacobian 的联合作用；
Pre-Norm 用干净的 identity path 改善梯度传播，却也可能让深层更新相对 residual
主干变弱。两者不是单独移动一层 Norm 就能互换的开关。

一种实验性演进分支，是重新引入可控的 carry / transform 路径：

```text
vanilla Post-Norm
  Norm(x + F(x))
  -> 深层时 residual 与 transform 一起穿过 Norm Jacobian

Pre-Norm
  x + F(Norm(x))
  -> 保留干净 identity path，但可能降低部分深层的有效贡献

gated / scaled Post-Norm
  Norm(alpha * x + F(controlled(x)))
  -> 显式控制 carry 与 transform 的比例
```

`Keel` 是该分支的一个受限案例。论文把 Highway-style scaling、额外的输入控制与
Post-Norm 组合，并在作者的极深、窄模型设定中报告比对应 Pre-Norm baseline 更稳定。
这支持的长期结论是：**Normalization placement、residual parameterization、depth /
width ratio、learning rate 与数据量必须联合设计。**它不证明 Post-Norm 已经成为所有
LLM 的新默认值；论文也明确指出 width scaling、低数据 regime 和不同宽深比仍是边界。

这条演进关系是 `Direct Evolution`：新分支修复旧 Post-Norm 的梯度路径，同时接受了
额外结构约束。Pre-Norm 在成熟实现、宽模型或证据不足的 workload 中仍然成立。

联合形状还有一条需要分开的解释：残差表示维度D、每层MLP隐宽M与层数L，并不是可互换的三个“规模”。[一项受限残差网分析](https://arxiv.org/pdf/2603.18168v1)在特定初始化/步长缩放（另须满足定理的log(L)∨D≤C₀M、误差上界足够小且固定随机输入/读出层的简化设定）、光滑激活导数与loss-gradient条件以及有界平滑的梯度截断下，给出固定训练步数时逼近同一极限动态的误差上界，包含1/L、√(D/(LM))和1/√D三项（省略固定失败概率的因子）。增大D会降低有限表示误差，却可能提高它相对深度和MLP宽度的耦合项；因此相同参数量不能只凭更宽就声称更接近该极限。这里的“收敛”是有限模型与极限动态之间的近似，不是任务loss到全局最优，也不是形状更好就更会学习；常数对训练步数和样本数的依赖又限制了长程外推。输出侧更快的形状律仍是猜想，Norm、真实任务质量、完整训练费用与硬件并行效率没有由这条误差界得到认证。比较实际模型时，继续验收残差缩放、传播、收敛和质量，保留已验证的Norm/宽深配方，而不按极限误差公式自动选型。<!-- source-family:SF-2026-ARXIV-2603-18168 -->

形状选择也可直接改变状态与更新的预算分配：先把输入映到较宽的 skip state，再叠加经窄瓶颈返回同一宽度的 residual 校正，初始投影可以固定，把更多可训练参数留给后续更新。这与只在原状态中加一条低秩投影不同，但窄校正也不等于每层任意全秩变换；多层可累积不同更新方向。[受限 MLP 形状对照](https://arxiv.org/html/2510.01796v1#S3)在图像任务中支持这条参数预算分支，未实测 Transformer，不能从上面的极限误差界或局部 PSNR 前沿推成通用宽深配方。线性初始升维本身不增加线性可分性，维度更宽也不单独保证保信息；冻结矩阵仅省其梯度/优化器状态，前向投影、输出映射、宽 activation 与逐层归一化仍付费。比较时须同时记完整参数、可训练参数与真实计算/驻留预算，印出搜索域与结果表未闭合也不能补成可执行 recipe。独立质量或总费用不合时，保留成熟窄状态/宽 FFN 与已验 residual/Norm，而不把参数较少或随机投影称作容量与净速度保证。

<!-- source-family:SF-2025-ARXIV-2510-01796 -->

联合尺度也影响随机 Attention 的表示动态，不能只以层数大解释 collapse。对独立随机 heads／layers、attention-only encoder 与球面归一化的受限模型，head field 的均值产生 drift，中心化波动则按 residual step、heads、权重方差及维度共同缩放；这些波动由全部 tokens 共享，不是给每个 token 独立添加 noise。中心化 Gaussian value 使 Attention 的均值 drift 消失，归一化修正与共享波动仍可驱动表示变化；静止、近似确定或保留随机性的极限需要分别声明联合尺度。<!-- source-family:SF-2026-ARXIV-2604-01978 -->

[Homogenized Transformers 的受限主结果](https://arxiv.org/html/2604.01978v1)只在初始化独立性、moment／球面状态与相应近似条件下支持这个分解，不授有MLP、causal decoder或训练后相关权重。Overlap 的趋同不同于整条路径同步，尖锐 Attention／高维近均匀分布下的慢 transient 也不等于永不坍塌；该慢动态还要求全时间密度规则性，不能从初始化 alone继承。极限近似、有限网络传播、训练可学性和任务质量继续分别验收；实际条件不符时，保留标准 Norm／residual 配方与有限状态/扰动诊断，不以随机极限替 checkpoint 认证。

MLP也会产生共享扰动，但不能直接沿用上面的Attention-only定理。另一个受限初始化模型固定Attention映射、令各层MLP独立随机，采用球面归一化；当Attention残差按T/L、MLP残差按√(T/L)缩放，前者进入确定性相互作用drift，后者进入由各token共同读取的随机field，而不是逐token独立噪声。[联合深宽极限的必要结果](https://arxiv.org/pdf/2604.26898v1)只在相应初始化、正则与有限时间条件下成立，三种极限全部交换另需更强光滑性。噪声是否促使表示合并，还取决于其协方差、激活与Attention反向扩张是否足够弱；仅在nonodd及负能量增长率等条件下，才有期望interaction energy指数下降。Odd的Tanh实例可保留两点吸引，故不能把MLP更宽或随机性更强直接当防collapse。有限网络、训练后相关权重、causal decoder与任务质量仍独立验收；条件不符时，保留已验Norm/residual配方和有限扰动诊断，不用初始化极限替训练checkpoint签证。<!-- source-family:SF-2026-ARXIV-2604-26898 -->

## 不计算归一化，也要控制信号与导数的深度传播

如果把 Norm 换成逐元素饱和函数，节省的是归一化运算，不是自动保留原来的梯度条件。以 `tanh(αh)` 或 `erf(αh)` 为例，`α` 是函数输入的可学习尺度，初始化时决定激活方差与平均平方导数；它不是另加在 residual branch 外面的乘法 gate。残差累加、权重初始化和最终读出层共同决定 Jacobian 随深度的行为。较小的 `α` 可减弱分支的有效贡献、延后初始化信号放大，却也可能过小而使收敛变慢。因此“函数有界”与“整网可训练”不是同一件事，学习率、warmup、深度和输入尺度仍需联合检查。<!-- source-family:SF-2026-ARXIV-2604-11890 -->

[受限初始化分析](https://arxiv.org/html/2604.11890v1)比较了 Pre-LN 与这类替代函数的 APJN，即 Jacobian 平方 Frobenius 范数的均值；它不是每个奇异值都稳定的保证。推导使用宽模型、双向均匀 attention、独立高斯初始化与 token 置换对称等近似，CIFAR-100 上的 ViT 实验主要检验初期训练的稳定边界，并不证明 causal LM 或完整训练后的质量。最终读出层也会改变整体放大因子，不能只校准中间 block。成熟 Pre-Norm 在证据不足时仍是更稳妥的基线；尝试无归一化分支时，应分别验收初始化传播、实际收敛与任务质量，而不是凭匹配一个 APJN 数字就认定二者等价。

若从已有checkpoint撤去Norm，另一条局部分支先收集每层激活，将原pre-affine映射拟合成逐层标量表达式，再继承原affine参数并做短程对齐训练。[受限symbolic替代](https://arxiv.org/html/2605.14047v1)避免每token重新计算跨特征统计，却不使标量函数等价于输入相关的均值/方差；在两个尾部anchor加软罚也不保证全域有界。拟合误差与节点数只是搜索代理，不能替真实任务和算子成本：部分affine-only结果弱于固定函数，完整回训仍低于同训LN，v1减少读取却增加估算算术，未测实际kernel净时延。逐层搜索、激活采样、全网或teacher蒸馏回训与新指令表达式均付费；现有单视觉架构/数据的结果不授NLP或现成checkpoint直接替换。域、数值、真实质量或总费用不合适时，保留原Norm/成熟固定函数及对应训练配方，不从局部MSE或解析流量签发无损与生产提速。<!-- source-family:SF-2026-ARXIV-2605-14047 -->

有界 activation 还会在 regularization 与容量瓶颈之间换位。任务所需信息量与参数容量的比例 `T/P`，连同架构，决定饱和约束是在限制无效变化还是截断必要表达；不能只凭函数有界就判定优劣。作者的跨设置分析只覆盖 `T/P < 1.84`，阈值 0.43 的 leave-one-setting-out 判别约为 50%，并不构成可自动选型的 controller。<!-- source-family:SF-2026-ARXIV-2604-23434 -->

估计任务信息需求、容量和跨架构校准增加实验成本，`T/P` 也不是线上可直接观测的充分统计量。应保留 matched learning curve、质量与饱和程度的联合检查；容量不足、阈值迁移失败或新任务未校准时，回退成熟 normalization/activation，而不是按单一比例静默替换架构。

逐 token 的 Norm 在训练初期输入尺度尚未稳定时仍是合理基线；若目标是移除推理路径上的归一化，还可把控制分成两个阶段：warmup 继续执行 Norm，同时收集其尺度统计，之后逐渐过渡到冻结、与 sample 无关的缩放。这样的常数才有机会折叠进相邻 linear 权重；LayerNorm 的 mean-centering/affine 结构仍需单独处理，不能把 RMS 的折叠规则直接套用。它改变训练轨迹和部署产物，校准窗口、gate schedule、冻结尺度与权重版本必须一起验收，而不是训练后直接删除 Norm。<!-- source-family:SF-2026-ARXIV-2602-10408 -->

内部尺度被冻结，并没有替最终读出层建立同一份合同。ε=0 的归一化读出具有零阶齐次性，径向梯度可为零；撤去这一锚后，正 margin 的交叉熵仍可能推动 logit scale 增长。保留 final Norm 与另加目标尺度 penalty 是不同分支，后者仅提供局部径向恢复力，不证明整个模型稳定。[TaperNorm 的受限对照](https://arxiv.org/html/2602.10408v1)中，移除更多 Norm 仍会损失部分 CE/任务质量；无 KV cache 的 forward microbenchmark 也不等完整生成提速。统计失配、OOD 尺度漂移或质量回归时，应保留动态 Norm/最终读出锚及原训练路径，而不是由可折叠性授予无条件替代。

## 层堆叠可以被解释成迭代优化，但不是 Hidden-state 真理

前面的 Jacobian 分析回答传播是否稳定，却还没有说明一层更新在执行什么算法。把更新解释成某种优化步骤，是比形状与梯度合同更强的命题，必须另加条件。

普通 residual layer 最稳妥的解释是对 representation 做逐层可学习更新；在受限函数类与分布假设下，也可以把 context-carried state 的层间变化构造成 normalized-gradient iteration。这个视角解释为何深度可能对应算法步数，但只要参数共享、归一化、目标构造或分布条件改变，就不能把 hidden state 直接命名为某个真实 optimizer state。

算法解释带来可分析的归纳偏置，却可能把存在性构造误当成实际机制。无法通过干预和跨设置验证时，应回退 representation-update 解释；现有 exact-v1 只证明作者定理与实验条件，不证明生产 LLM 在执行该优化器。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06609 -->

层间状态也可以用来决定下一层“还要从上下文收集什么”，而不只是重复一个固定优化更新。一个受限的 in-context 回归模型把同一潜在任务下的可交换样本经低维 attention 汇聚成 function vector，再让后层 MLP 读取已有统计、选择下一次 embedding 的测量方向；原 token 与统计状态保留在不同子空间。这样深度提供的是依前次结果改变后续测量的机会，attention 的通信与 MLP 的局部选择共同构成算法，而不是给中间层预定一个人类语义。

是否值得逐层测量仍取决于分布和资源约束。[精确首版的条件分析与干预](https://arxiv.org/html/2606.16694v1#S2)固定总通信维数 M=dL、在线性回归的大样本噪声极限中，让各层读取同一份带噪统计：Gaussian prior 下，给定已选测量方向时，后验协方差不依赖测量值，多轮 adaptive 测量不胜一次 M 维测量；层级 tree prior 则允许按此前结果沿分支继续测量，并在所比较的受限策略中延后噪声瓶颈。其 linear-attention 实验和 key patch 支持这个条件机制，不是任意 softmax LLM 已执行 Bayes 最优推理的证明，也没有穷尽所有非自适应策略。固定通信维数不等同等参数、训练或 FLOPs，宽统计状态、反复汇聚与干预验证都要计费；缺少分布和机制证据时，仍保留上面的普通 representation-update 解释，不以更深自动批准更强推理或更低系统成本。<!-- source-family:SF-2026-ARXIV-2606-16694 -->

若目标是执行一个给定数值更新，而不只是为可学习层提供优化类比，算子与状态可以直接按算法构造：把当前矩阵和乘子放在 persistent registers，用无 softmax 的 linear attention 做矩阵积、bilinear/ReLU 子层做乘法和阈值，再清理 scratch 后交给下一块。外部控制器仍拥有更新步长、penalty schedule 与停止，丢掉乘子可能使同一矩阵对应的下一步不再唯一。[受限固定权重构造](https://arxiv.org/html/2610.10395v1)因此要求分测同状态/控制下的单步对齐、完整 residual stream 的反复交接，以及 solver 自身的任务结果；每步重新编码和 arithmetic replay 不代替 scratch-reset 验收。有限 float64 检查不授任意 kernel 精确，fixed-stage 的收缩和误差界也不认证外部 controller、因果恢复或普通训练必能学会该执行器。编码、宽状态、完整更新与精度/回归检查都付费；状态或数值条件失配时保留显式数值 solver、完整状态和 reference transition 测试，不把流畅输出或最终 graph 命中批准为算法正确。<!-- source-family:SF-2026-ARXIV-2610-10395 -->

优化类比仍不能预测向某层注入一个小扰动后，读出会怎样变化。固定 prompt 时，可以只把最后一个有效 token 的 residual state 作为被干预变量，其余 prefix states 保持不变；围绕原轨迹求逐层 Jacobian，再投影到包含目标概念方向的低维可达子空间。该局部 surrogate 预测的是扰动跨层传播及最终指定 readout 的敏感度，不把整网、全部 token 或任意新上下文改写为线性系统。因果 mask 是固定 prefix 的前提，context、checkpoint、方向与局部尺度改变后必须重新核响应。<!-- source-family:SF-2026-ARXIV-2603-12541 -->

这样的响应模型可替代逐层盲试，为多层注入分配系数；在线性 surrogate 下，给定读出位移的最小平方控制范数有闭式方向，回到完整非线性模型仍须另行校准幅度并验证实际效果。[受限 GPT-2 家族对照](https://arxiv.org/html/2603.12541v1)只支持指定二分类概念与局部干预，不证明概念分数是真值、范数更小等于推理更快，或该模型能保证开放生成的安全。方向拟合、Jacobian/子空间构建及回归测试都有成本；任务或扰动范围失配时，保留实测层扫和不注入的基线。接下来判断哪些层可以删除，仍需要另一份完整干预协议。<!-- source-family:SF-2026-ARXIV-2603-12541 -->

跨层注入还可以先从两组校准样本提取逐层均值差，再组合当前层差、此前层差的累计量与相邻层差分，分别作为P/I/D三项；后层校准先计入前层已加的干预，避免把原轨迹当成修改后仍有效的参照。[这一受限steering分支](https://arxiv.org/html/2510.04309v1#S3)的时钟是模型深度，误差是source/target两人口的表征差，不是部署时逐token已知真实任务结果的闭环反馈。校准数据、方向、gain、层位和checkpoint因此共同定义干预身份，有限深度也不能继承无限时间收敛；原比较矩阵与PI系统存在满足其打印条件却谱半径大于一的反例，不采用其一般稳定保证。均值差不代表每个输入都应同向改变，目标style/行为更强也可能损害内容或旧能力；提高攻击ASR更不能改称安全增强。校准前向、顺序hooks、累计/差分状态、gain搜索与独立质量安全回归都付费，不训权重不等零在线成本。方向迁移、内容或数值窗口失配时，保单层/固定小幅干预、原模型与不注入基线，由真实任务和独立安全门决定采用，不由控制器名称或一个概念分数批准通用稳定和可靠行为。

<!-- source-family:SF-2025-ARXIV-2510-04309 -->

## Layer “冗余”取决于干预协议

稳定地堆深之后，另一个问题才是哪些层值得保留。梯度是否健康、表示是否相似与一层能否删除不是同一个判断，必须分别检验。

相邻 residual states 相似，不必然说明层更新没有新增计算：累计状态包含前面的共同历史，即使各层更新互不相关、大小相同，基于全 lag 相似性的一个 effective-depth 摘要也可小于2。这个结构参照不是“只用了两层”的证明，更不是能力上限。比较实际模型时还须匹配 update 大小、初始状态 carry 和 update 相关性；这些参照可改变相对 gap 的符号，global accumulated-state 几何与某层的功能贡献不能互换。

Pooling、BOS幅度、归一化和相似性不变性都限定诊断看得见什么，相关 update 也不自动意味着可删除。作者有限 residual-carry 干预中，提高该摘要的强干预反而破坏训练；局部按摘要变化剪层又劣于专门的邻层指标。因而把该量用于校准表示几何，仍须以当前任务上的具体干预、剪后完整回归和实际执行成本决定 release；没有对应证据时保留原层，不能以更低 effective depth 宣称模型浅、capability差或获得免费剪枝。[必要定义与反证](https://arxiv.org/html/2609.31098v1) <!-- source-family:SF-2026-ARXIV-2609-31098 -->

逐层替换为某个固定 baseline，适合测“删除这一层后模型是否仍工作”；把两层互换，则测它们在上下文位置和 residual state 下是否可替代。这两个 protocol 改变的输入状态、下游补偿空间和 evaluator 都不同，因此不能从 replacement 影响小直接推出 layers 可交换或可安全剪枝。

任何 layer-redundancy 结论都应绑定 checkpoint、干预操作、位置、数据切片和 evaluator，并在剪枝后重新验证完整模型。受限实验可以暴露 protocol-dependent redundancy，但不证明跨模型或跨任务存在固定“无用层”；证据不一致时保留原层结构，或只把干预作为诊断而非 release 决策。

干预参照也可以来自同输入的另一个checkpoint，而不是零值或固定均值：让pretrained前缀产生指定层activation，再交给finetuned后缀继续，逐层比较原模型、微调模型与拼接路径。[受限跨checkpoint对照](https://arxiv.org/html/2510.12229v1#S3)测的是这份替换对指定行为差的影响，不由差额消失定位唯一bias存储，也不能由一个intentionality标签恢复推出全部旧能力或公平性。前后模型、输入/层位、token对齐与读出协议须共同保存，跨模型状态分布失配本身也可能改变输出；80个scenario的随机温度重复不是同数量独立人类。双模型求值、activation驻留/拼接、层扫和独立旧任务回归均付费；语境、状态兼容或效用不稳时保各原checkpoint与普通干预对照，只将拼接用于有限诊断，不据其批准无损去偏、剪层或部署安全。

<!-- source-family:SF-2025-ARXIV-2510-12229 -->

若目标是替换而非直接删除，压缩单位还可从连续整层拆成非连续的Attention与FFN子模块，分别拟合其写入残差；先替换前一类，再按改变后的激活选择后一类，能显式容纳两者冗余与可拟合性的差异。低rank Attention bypass与共享输入basis的FFN bypass仍要执行和保存，并不重现原算子的内部依赖。[受限替换对照](https://arxiv.org/html/2606.02559v1#S5)中，mask后最不伤的排序不一定给出替换后的最佳质量，部分模型也弱于连续替换基线；校准、basis/rank、替换mask及完整新旧任务回归均计费，净参数/MAC与真实Decode收益分别验收。拟合失配或关键切片退步时，保留完整子模块、保守连续替换与原模型，不从局部低影响批准无损压缩。<!-- source-family:SF-2026-ARXIV-2606-02559 -->

测“何时必须读其它 token”时，等待期也应保留任务一般语境，而不把表示换成任意零值或原始 embedding。可固定当前 token、位置与任务模板，从同一条件输入分布估计该层表示的均值，再用显式 attention mask 只开放选定位置和层的读取；self-only 路径若仍允许 BOS，也须一并记明。[AF1 的有限算术对照](https://arxiv.org/html/2509.09650v1#S4)由此把分布外替换与输入特定信息传递分开，但子图在 full model 已答对样本上的保持率，不是全部输入准确率，也不证明原模型唯一使用该电路。单 token 数字、固定模板和选择过的层/头限定结论，word problem、代码与其它模型的直接反退仍在；条件均值制备、结构搜索、mask 计算与完整回归均付费。任务语境、tokenizer 或行为不保持时，保留原层和完整读取，只将干预用于诊断，不由几层足够就签发通用剪枝或推理加速。

<!-- source-family:SF-2025-ARXIV-2509-09650 -->

压缩的干预单位也不必是整个block或某组完整heads。一条受限分支在选中的高层去掉Q/K与跨token聚合，保留原V/O作为逐token残差支路，再逐模型搜索校准其幅度；它改变的是这一子层还允许读取哪些位置，不是把attention换成identity，也不等于均匀读取prefix。表示相似和所印范数论证不足以证明这两个算子等价，删去的依赖须由当前任务上的实测干预承担。[有限高层替换对照](https://arxiv.org/html/2507.01900v1)仍有生成、数学及长上下文代码/检索反退，PPL选出的scale也可能损害另一质量切片；因此checkpoint、替换层、V/O布局、校准人口和scale必须共同版本化。保留的权重与逐token计算、KV减少、网格校准和完整回归分别计费，整段序列处理变快不等decode服务SLO改善。跨token证据、质量或净预算不能成立时，应保留原attention、较保守的head/layer剪枝与完整模型，不从高层相似或一个均值批准普遍无损替代。<!-- source-family:SF-2025-ARXIV-2507-01900 -->

当命题从“某一层是否必要”扩展到 Attention head、MLP neuron 与 residual stream 共同形成的因果链时，单次
activation readout 或单点 ablation 也不够。更完整的验证顺序是：先用只改变目标属性的 minimal pairs 定位候选，
再用同数量随机干预和双向 activation patching 区分相关性与因果方向，最后把永久 weight edit 作为新的 checkpoint
重新执行自适应反例、utility 与副作用评估。每一步都要记录具体 projection、layer、token position、probe slice
与 evaluator；某个模型或某个方向失败时，不能用其他模型的平均收益补成一条普遍电路。

这种协议能提高局部 circuit claim 的可信度，却不能证明被定位组件拥有唯一语义，或证明放大少量权重就是生产安全
机制。干预可能沿其他 residual path 被补偿，也可能在新攻击、量化或继续训练后改变身份；永久编辑还可能以能力下降
和过度拒绝换取目标指标。证据链不闭合时，应保留原权重并把定位结果用于诊断，而不是把它直接升级为 release 决策。

<!-- source-family:SF-2026-ARXIV-2605.16234 -->

已校准的activation方向可以在特定线性输出接口上编译为rank-one权重改动，让指定input方向控制目标输出方向，正交input在该局部算子中保持不变。[Steer2Edit的受限结构](https://arxiv.org/html/2602.09870v1)以输入方向估计、强度与稀疏化决定作用域；这只保留局部线性映射，不保留后续非线性、全语义或所有攻击下行为。方向拟合、样本/层选择与weight回归均付费，Mistral自适应攻击有直接退化，均值方向还可牺牲效用，原文未测wall-clock收益。接口、样本支持或utility不稳时应保留运行时vector或原权重，不能从局部orthogonal invariance获得全模型无副作用证明。 <!-- source-family:SF-2026-ARXIV-2602-09870 -->

### 表示相似不等于任务决策可删减

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07271:start -->
Layer pruning 不能只比较平均 activation/CKA 相似度：深层表示仍看似保留时，模型也可能因前置层被删而无法跨过 decision-margin transition。压缩验收应沿层深记录 Silent phase 到 Decisive phase 的任务相关 transition，并把 pruning mask、模型、task 与 margin probe 绑定；它能解释突发 accuracy cliff，却依赖多选 logit 和作者定义，不能当通用因果证明。开放生成或 probe 不适用时，回退任务级回归、保守剪枝与完整模型。`arXiv:2605.07271v1` 的证据只覆盖作者模型、任务与 iterative pruning 分析设置。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07271:end -->

### Layer Pruning 需要在删除边界显式修复表示坐标系

<!-- semantic-body-binding:SF-2026-ARXIV-2605-15491:start -->
直接删除冗余层在校准分布稳定、相邻 hidden state 已近似对齐时成本最低；层数减少后，删除点前后的 activation 坐标系仍可能错位，使下游层接收到从未训练过的表示。一个低成本分支在 pruning boundary 收集成对 activation，并求一个无约束闭式线性 alignment operator 插回网络。pruner 只决定候选结构，alignment operator 拥有局部坐标转换，完整模型回归才决定 artifact 能否发布。

闭式修复避免全量 fine-tuning，却新增 calibration set、operator 参数与版本身份；线性映射只能补局部一阶错位，可能在 OOD、长上下文或安全 slice 上放大误差。exact-v1 的 §3.2.1–3.2.3、§5.1–5.3、Appendix G 与 §6 只支持作者模型、剪枝率和 latency 条件。校准分布不可信、operator ill-conditioned 或关键 slice 回归时，应保留未剪枝模型，或回退带训练的 pruning/fine-tuning 路径。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15491:end -->

减少顺序层数也可以保留来自不同原层的部分channel，而不直接平均权重或只删除整层：先用校准activation与权重范数提出channel重要性，再按block影响分配相邻层各自保留比例，将所选channel拼成较少的新block，最后用原模型恢复训练。[CoMe的受限分支](https://arxiv.org/html/2510.15304v1#S4)改变参数来源与层边界，不由相似hidden或拼接保存的参数证明原函数等价；蒸馏正是新增适配成本。逐段恢复与联合恢复的内存/预算不同，合并更多层、太少校准样本或换校准域都可恶化质量，不能按压缩比例承诺无损。Checkpoint、校准人口、channel集合/比例、拼接布局与teacher须共同版本化，全部统计、重构训练与生成回归都计费；映射、关键切片或实测费用不合时，保原层、保守剪枝/坐标修复与完整模型，不从参数保留或相对accuracy批准服务净加速。

<!-- source-family:SF-2025-ARXIV-2510-15304 -->

硬件和请求预算持续变化时，为每个目标稀疏率单独选一份pruning mask，会产生多套彼此不一致的artifact。另一条分支把每个MLP neuron与Attention head放到共同重要性尺度上，冻结主模型权重，用可微soft pruning同时观察多个计算预算下的loss，再学习一份统一排序；部署按预算从低排名端裁去单元。它不等于删除整层，也不是证明某个head/neuron具有固定语义所有权，校准任务仍决定哪些计算值得保留。

一套排序节省多个独立模型的维护，却增加校准、排序优化、每预算shape与编译/执行缓冲。FLOPs减少只有在实际切片和硬件tiling合适时才变成速度：[受限elastic对照](https://arxiv.org/html/2610.20588v1)的eager小batch不一定加速，GPU-friendly粒度也可能额外损失质量；快速预算切换未包含初次编译与驻留buffer。所测vision/text encoder的质量与速度不能直接授予LLM生成服务收益。预算稳定、校准失配或shape开销抵销节省时，固定size、已验证mask或完整模型仍更简单。<!-- source-family:SF-2026-ARXIV-2610-20588 -->

## Residual Stream 从单一累加状态走向 Depth-wise Routing

前面的干预是在既定 stack 上判断哪些计算能删；如果瓶颈不是层数本身，而是信息如何跨层保留，就需要重新设计 residual 接口。下面的分支改变状态组织，并不授权对已有 checkpoint 任意改接线。

标准 residual stream 每层只接收上一层聚合后的状态。它便宜、shape 稳定，也天然适配逐层执行与
Pipeline Parallel；但深度增加后，较早子层的信息已经被压进一个不断累加的向量，后层无法再区分
“来自哪一层”，固定等权累加还可能让单层更新相对主干越来越弱。

一种演进是把部分历史层输出保留为可选择的 depth state：当前层先对历史 sources 计算权重，再形成
本层输入。全量历史选择提供最强表达，却使 activation、跨 stage 传输和推理 I/O 随深度增长；按 block
汇总历史，把 block 内的普通 residual 与 block 间的选择性聚合组合起来，能把状态量压回有限数量的
summary。另一条分支只保留固定数量的 depth slots，并让注意力从槽位中选择，成本更可控，但会引入
slot 容量、写入、覆盖和选择错误。

扩展层间状态也不一定保存更多历史层。[一条受限替代分支](https://arxiv.org/html/2506.22696v1)直接把每个token的residual向量改成key与value两轴的矩阵：读key沿矩阵一轴收缩，供Attention与MLP消费；子层结果再与写key作外积，作为矩阵的加性更新。MLP核心的非线性权重仍保留，改变的是其前后的存取适配，而不是另加一个持久KV缓存或声称所有知识都在外积中。把存储width与内层head/FFN计算width分责，使前者不必按后者等比例扩展，却仍增加activation、归一化、读写与checkpoint流量；key寻址也不保证无串扰。Checkpoint须联合保存矩阵shape、read/write keys、Norm与训练配置，不能在旧向量模型上直接换接口。有限小模型对照中，较少FLOPs仍伴tensor-contraction运行更慢，初始化moment也不保证训练后稳定；布局、总训练时间或held-out质量不合预算时，保留成熟向量residual、较粗depth summary或已验的辅助记忆，不由理论存储容量签发无损与实际加速。
<!-- source-family:SF-2025-ARXIV-2506-22696 -->

```text
single accumulated residual
→ gated / scaled carry-transform path
→ explicit depth-history selection
→ block summaries or bounded depth slots
```

这里真正变化的是信息路由，不是简单“增加一层 Attention”。Checkpoint 拥有 depth query、block/slot
结构与聚合参数；训练 runtime 拥有历史 activation 的保存、重算与跨 stage 传输；推理 runtime 拥有
prefill/decode 的历史状态和 online reduction。更强的 depth routing 换来额外状态、kernel 与并行通信，
而且作者在特定 MoE 配方中的 loss/benchmark 不能证明它会普遍取代标准 residual。模型较浅、吞吐优先、
跨 stage 带宽紧张或公开实现尚不成熟时，单一 residual stream 仍是更稳健的设计。

不逐层保存历史，还可以保留标准additive residual `x`，另为每个token维护固定宽度的关联矩阵 `M`与inverse-covariance `P`：当前层读取 `x+Mq`，子层增量既更新residual，又以预测残差乘gain的rank-one项写入 `M`。正forgetting/importance与ridge条件下，Sherman–Morrison递推给出加权depth regression的RLS解；这利用层本已顺序执行的约束，不意味着同样的不可并行求解适合token-sequence Prefill，也不是跨token持久KV。普通residual与压缩关联记忆承担不同职责，不能把后者当作前者的无损替代。<!-- source-family:SF-2026-ARXIV-2610-18809 -->

固定的是随depth推进的state宽度，不是总activation成本。分组各有 `P`，`Dk=8`时单memory matrix已为每token `8D`、另加residual与covariance；unwinding/windowing以重算、紧凑中间量和延迟融合减少保存/流量。[受限消融](https://arxiv.org/html/2610.18809v1#S4)中去掉residual的两种变体都劣于PreLN，而RLS替换为delta/outer仅有局部小差额；400M/1.5B质量及B200 kernel结果不证明普遍优越，1.5B也未跑FullAttnRes。额外状态、递推数值与专用kernel不合预算时，保留标准residual、粗block summary或显式depth retrieval，不能由较低PPL签发全规模吞吐保证。

多路 depth retrieval 也不一定要求维护多份可更新 residual state。可以先保存完整维度的单流 source 或 block summary，再由多尺度因果 depthwise convolution 构造含不同局部上下文的视图；各视图以自己的 pseudo-query 对历史 sources 做 softmax retrieval，最后用输入相关标量混合成下一子层的单流输入。这里扩展的是历史的读取视角，不是切开 hidden channels，也不是把同一向量乘几个标量便获得多样信息；因果窗口只允许当前位置及更早 token，checkpoint 必须与这套扩展、查询和融合接口共同训练。<!-- source-family:SF-2026-ARXIV-2610-13630 -->

按需扩展让持久 source 保存与跨 stage payload 仍按 `O(Nd)` 计量，却不让全部中间状态、访存或计算都保持单流：批量预计算仍会产生每个目标层的多路 retrieved states，最终融合也需读写它们。[MSAR 的受限 MoE 对照](https://arxiv.org/html/2610.13630v1#S3)支持这种读取分支，去掉上下文扩展后收益缩小；较多 streams 的边际收益很小，论文的 iso-loss FLOPs 拟合也不是实测 wall-clock 加速。卷积、重算、深度读取、融合与并行缓存都计价，fused execution 尚须实际实现验证；净质量或预算不成立时，保留单头 depth retrieval、较粗 block summaries 或普通 residual，不对已有 checkpoint 任意改接线。

另一条分支不保存更多历史，而是改变当前状态的 carry 与 write。令 $X\in\mathbb R^{d\times d_v}$ 为层间状态，方向 $k(X)\in\mathbb R^d$、写入值 $v(X)\in\mathbb R^{d_v}$ 与 gate $\beta(X)\in[0,2]$ 由当前输入产生，可定义 $A(X)=I-\beta kk^\top/(k^\top k+\epsilon)$，再执行 $X'=A(X)X+\beta kv^\top$。同一 gate 同时控制旧投影的擦除与新值写入，不是先无条件删掉历史再补一个普通 residual。在单位方向、$\epsilon\to0$ 且固定输入的理想分析中，$A$ 在 $k$ 方向的特征值为 $1-\beta$，其余方向为 $1$：$\beta=0$ 保持状态，$\beta=1$ 擦除该方向后写入，$\beta=2$ 对 carry 做反射后写入；区间内 carry 的谱范数不超过 $1$，但一般并不等距。

这个算子界不等于整层 Jacobian 界：$k$、$v$ 与 $\beta$ 都依赖输入，导数还有这些分支与写入项；有限 $\epsilon$ 也不能直接照搬理想投影或精确反射。它提供的是 depth-wise rank-one 更新的替代结构，不是时间序列记忆的默认删除策略，更不能只从 carry 的谱推出训练稳定或质量收益。现有必要证据是结构与条件性分析，没有实测收益；采用前仍须训练匹配该接口，并验证方向归一化、gate 饱和、状态布局与执行成本。没有对应训练产物或任务回归不成立时，普通 residual 与现有 depth routing 仍是合理基线。由此再考虑下面的多流结构时，先分清改变单个状态的几何与增加状态流数量是两条不同分支。

### 多流 Residual 把 Layer Identity 从单一向量扩展为受控状态组

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23259:start -->
单一 residual stream 让层间接口稳定、实现简单，是默认可堆叠结构；当不同更新需要保留各自轨迹时，可以维护多条 residual state，再由 gate 与 attention pooling 决定哪些增量进入下一层。Layer identity 因而不仅是参数与 Norm，还包含 stream 数量、gate、pooling 与合并顺序。

多流结构增加表示容量，也增加显存、通信、gate collapse 和训练不稳定风险。exact-v1 只支持作者架构与实验，不证明 stream 越多越好；gate 饥饿、数值漂移或收益不足以覆盖状态成本时，应回退普通 residual 或较简单的 Attention Residual。arXiv:2605.23259v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23259:end -->

并行流还有另一种轴：每条流保存完整序列，只让少量选中位置在层处理中读取其他流，再经本流后续Attention传播，而不等到最后才投票。[受限batch-mixing分支](https://arxiv.org/html/2610.25254v1#S3.SS3)要求同时绑定通信组、位置选择、跨流因果mask与decode路由；它不是普通独立请求可无条件共享的batch。全序列TopK的prefill与逐位置预测的decode不同，只有位置mask不能替完整prefix-invariance验收。重复masked输入上的恢复和较低LM loss也不证明非冗余事实能跨流检索，直接QA/concatenated对照仍暴露明显差距。稀疏mask可在实际kernel中反比dense更慢；拆local/gather两pass后，只有互斥key集合、相同投影和log-normalizer合并才保持原selected-mask输出。全部流的主干、gate/gather、cache与训练均付费，单层prefill不授全链省费；隔离、路由或任务质量不合时，保独立流末端聚合、单序列显式context与已验dense路径，不从通信边存在批准可靠协作。<!-- source-family:SF-2026-ARXIV-2610-25254 -->

### 多流混合还要保留哪些几何约束

单一 residual 的 carry 路径是恒等映射；扩展为多流后，不能把读取、跨层传递和写回统称为一个 gate。令 `X` 的每一行是一条流，`H_pre` 将多流读入子层，`H_res` 混合并传递旧状态，`H_post` 将子层增量写回各流：

```text
X_next = H_res X + H_post^T F(H_pre X, W)
```

可学习的读写提高组合能力，但跨层 carry 变成 `H_res` 的乘积；若没有约束，它可能改变流均值，放大或削弱传播信号。一条替代分支把 carry mixer `M` 限制为非负双随机矩阵：每行、每列的和均为一，所以 `M1=1`、`1^T M=1^T`，且矩阵乘积仍满足这些约束。这保留了 carry 路径的均匀方向与流均值，并使这一路径的谱范数不超过一，却不等于恢复对任意向量的恒等映射：均匀平均矩阵会完全消掉流间差异。读写映射、子层增量和输入相关 mixer 的导数仍会改变完整 Jacobian，因此不能从 carry 的守恒推出整网梯度稳定。多流状态也增加访存和重算压力；子层 FLOPs 不变不是总执行成本不变。[受限机制证据：mHC v1 §3–5](https://arxiv.org/html/2512.24880v1#S4)

几何约束之外，多个流是否真能互换，还需要功能干预。表示相似只说明观测到的坐标关系；一个受限实验先缓存原轨迹并冻结混合矩阵，再同时清零两条流、分别恢复其中一条，以原模型输出分布的 KL 变化衡量恢复程度。相似的流仍可呈现不对称恢复，因而不能由高相似度直接授予删流或合流。这里冻结 mixer 是实验条件，避免把恢复效果与路由重新适应混在一起，不是推理部署应永久冻结原路由的建议。

恢复分布也不等于恢复正确答案：受测小模型知识检验通过率很低，分布距离更适合观测干预影响，却不能证明事实能力、任意任务或剪枝后质量。缓存原 activation、成对干预与受控恢复增加评测费用，删除后重新训练的自然轨迹还须独立验收。干预人口、路由条件或 evaluator 不匹配时，保留全部 stream、任务级回归及已训练的标准 residual；跨流几何、表示相似和功能使用是互补证据，不互相签发保证。<!-- source-family:SF-2026-ARXIV-2603-14833 -->

保留多个状态不自动保留多个独立方向。跨流 mixer 若只限制最大奇异值不超过一，只保证这一步不放大；最小奇异值仍可接近零，反复混合会抹去流间差异。正交约束同时限制上下界，却只保存所作用子空间的欧氏范数，不保证每个语义方向或流间差异不变，均值与差异仍可交换。它以更受限的混合几何、额外状态和数值实现约束换取传输稳定性；仍须将 mixer 与 write-back、初始化和训练配方共同评估，不能把局部等距当作全网络稳定或质量保证。

若 mixer 还要求每一步都保持 row/column 质量守恒，有限轮 Sinkhorn normalization 是成熟且易并行的旧方案；stream 数量少、近似误差可控时，它通常已经足够。有限迭代和数值精度只给近似可行性，不能直接继承理想双随机矩阵的精确守恒；实现仍须测量单层与跨层累积的约束误差。约束变化发生在深层反复混合必须同时满足 exact doubly-stochastic feasibility 与完整 mixing expressivity 时：可以用 transportation-polytope chart 的 `(n-1)^2` 个自由度逐项消耗 row/column budget，覆盖 Birkhoff polytope interior；recursive 分解则用层级状态换部分并行。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21724:start -->
Checkpoint 必须联合版本化 stream count、chart/recursion、边界处理与 optimizer，runtime 只执行冻结 mixer，不能把“减少归一化迭代”静默改成另一个算子。Exact chart 消除 finite Sinkhorn error 与 factorial permutation mixture，却引入顺序依赖、非线性耦合、kernel 成本与 optimizer sensitivity；矩阵可行性也不证明端到端质量或硬件效率。若 chart saturation、gradient stability、吞吐或 held-out quality 失败，应保留单 residual stream，或回退经过验证的 Sinkhorn、permutation mixture 与结构化 mixer。现有证据只覆盖作者的小规模语言模型和多数 single-seed 设置，不能外推 frontier-scale 稳定性。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21724:end -->

Exact feasibility 与完整表达力仍是两个不同要求，不必把所有替代分支都写成对同一 polytope 的无损参数化。另一条构造路线先把反对称矩阵经 Cayley transform 映射成 `ds × ds` 正交矩阵 `Q`，再将每个 `s × s` block 的平方 Frobenius 范数除以 `s`，得到 `d × d` 非负 mixer。正交矩阵每组行列的平方和保证结果满足双随机约束；但有限 `s` 可表示的 mixer 仍是受限集合，扩大 `s` 才逐步逼近完整 Birkhoff polytope。这不同于逐项消耗质量预算的 exact chart，也不同于仅组合小型 Kronecker factors。[受限证据：go-mHC §3–5](https://arxiv.org/html/2604.02309v1#S3)

这条分支把迭代归一化或顺序预算消耗换成矩阵求解与 block 归约，代价是约 `O((ds)^3)` 的求解成本、随 `s` 增加的参数和激活，以及有限表达空间；不能省略 `s` 后把任意表达力都称为低成本 `O(d^3)`。Checkpoint 需冻结 stream count、`s` 和映射，而双随机可行性不保证混合后的差异方向、write-back 或整网梯度稳定。作者的合成收敛和 30M 模型结果不足以证明大模型能力或真实硬件加速；需要完整 mixer 表达空间时保留 chart，流数少或近似已可接受时保留 Sinkhorn，通信与吞吐优先时也可能继续使用单 residual stream。
<!-- source-family:SF-2026-ARXIV-2604-02309; daily-trace:papers/2026/04/03/README.md -->

多流不一定是把同一 residual 复制成多个可更新槽位；另一条分支刻意分开只读的 token identity stream 与累积更新的 semantic stream。每次 forward 先由可训练 embedding 生成 token stream，随后跨层保持这份 activation 不变；Attention 与 FFN 可以读取两流，但只向 semantic stream 写入，最后的 readout 才组合两者。这样限制的是层间写入方向与融合时点，不是冻结 embedding 或全部模型参数，也不是禁止语义路径读取 token 信息。

这种结构使某些位置相关通道更容易单独观察和干预，却以额外状态、结构约束与训练配方换可干预性。[小型 TinyStories 对照](https://arxiv.org/html/2603.07482v1)中，位置 head 干预造成较小而非零的 semantic 损伤，语言建模 BPB 也劣于标准 Transformer；局部 coreference/recency probe 不证明所有概念独立、任意干预无副作用或 frontier-scale 优势。若任务需要更紧密的信息混合、干预目标不可校准或质量退步，标准单流及充分验证的可更新多流仍成立。应分别验收架构写入限制、局部功能探针与端到端质量，不把“late fusion”名称当独立性证书。<!-- source-family:SF-2026-ARXIV-2603-07482 -->

两流的读写规则与 head mixing 还须独立声明，不能由“dual-stream”名称推断 token activation 只读。另一条 Token-Factor 分支让 Attention 写 token stream、FFN 写 context stream，两者都读组合状态；Frozen-Token-Stream 才把跨层 token activation 固定。载荷投影可限制为 head 内 block-diagonal，或限制为跨 head 标量矩阵与通道恒等的 Kronecker 积：前者能变换 head 内坐标却不交换 heads，后者能交换 heads 却不能任意变换坐标，因此不是前者包含于后者的表达力阶梯。Dense Q/K 仍可使路由跨 head 依赖，per-head Norm 与可视化混合表也不授因果或语义完全隔离。[小型 pedagogical-corpus 对照](https://arxiv.org/html/2603.07461v1)仅支持固定模式、词表与训练预算内的 loss 取舍；attention sharpening 非精确 argmax，有限 loss 退步不证明离散算法或唯一错误补偿机制。额外两流状态、受限投影与训练/诊断费用均计价；功能干预或质量回归失败时保留 dense mixing、单流与既有可更新多流，不能将一组 Token-Factor 的 2.5% 移给 FTS 或所有规模。<!-- source-family:SF-2026-ARXIV-2603-07461 -->

### Residual Stream 之外还可能存在跨层更新状态

标准 residual block 把每层输出视为对同一 activation state 的局部修正，优点是路径清晰、并行实现成熟；但它没有显式利用连续层更新方向之间的相关性。若额外维护 depth-wise momentum，当前层可以结合先前层的更新方向再写回 residual stream，这改变的是跨层控制状态，而不是简单的归一化或矩阵预条件。潜在收益是更有效的深度传播，代价是顺序依赖、额外状态和初始化敏感性；动量失稳会沿深度累积。浅层或跨层相关性弱时，标准 residual 仍更稳妥。现有受控消融支持收益主要来自 momentum 而非 preconditioning，但不证明该结构适用于所有规模和训练配方。

<!-- source-family:SF-2026-ARXIV-2605-24425 -->

跨层动量也可以从 token 分布的惯性流构造，而不只把前层更新作欧氏外推。一条[受限架构分支](https://arxiv.org/pdf/2603.16535v1)让 token 同时携带 feature 与 velocity：softmax 几何中的动能依赖两份状态，位置和速度更新因而共同消费 attention 条件；attention momentum 又作为 MLP 的 lookahead 输入。这增加 velocity、阻尼、步长及可能的历史函数值状态，不能直接继承普通凸优化的 Nesterov 速率。连续推导的投影对称/正定条件与线性流的椭圆分布保持，不自动延伸到自由学习的 Q/K/V、多 head、MLP 或 LayerNorm；实际实现为节省 kernel 调用，让两状态同时读取旧状态再更新，也不因此保有先更新动量的几何积分器保证。同样的 attention/MLP 调用数仍可有更高墙钟成本，部分离散器的验证 loss 还反退，须将状态路径、积分次序、训练配方和达到质量目标的全费用分别验收；几何条件、数值稳定或净收益不成立时，保留普通 residual、较简单 depth-wise momentum 与已验证的固定层栈。<!-- source-family:SF-2026-ARXIV-2603-16535 -->

### Parallel Tracks 用周期融合换更少的跨设备依赖

标准 Transformer stack 让每层读取上一层唯一 residual state；配合 Tensor Parallel 时，每个子层内部通常还要
同步 partial result。这个结构简单、语义清楚，也能利用成熟 kernel，但在跨设备通信相对计算越来越昂贵时，逐层
同步会把网络延迟固定在 critical path 上。另一种架构分支把 block 划成多个相对独立的 parallel tracks：每条
track 连续更新自己的 residual state，只在声明的 fusion point 交换或聚合信息。

```text
one residual stream + per-operator synchronization
→ independent track-local states
→ several local layer updates
→ periodic fusion barrier
→ next track-local interval
```

这里 checkpoint 拥有 track topology、每条路径的参数和 fusion function；runtime 只能把完整 track 映射到设备，
并在 fusion point 执行同步，不能自行改变融合频率。它也不是 MoE：track 是架构规定的并行路径，而不是 router
按 token 选择的条件专家。减少同步次数的代价是重新分配参数、保留多份 track-local activation/residual state、
track 间信息陈旧、fusion hotspot
以及新的训练配方；任一 track 失衡还可能把周期 barrier 重新变成 straggler point。

`arXiv:2602.07306v1` 只在作者披露的模型与 TensorRT-LLM/vLLM serving 实现中支持这种结构—通信交换，不能
证明同等质量、通用速度或任意网络拓扑上的收益。模型较小、跨 track 交互必须逐层发生、设备负载不均或现有
Tensor Parallel 已能隐藏通信时，单 residual stream 加标准 TP 仍应保留。
<!-- source-family:SF-2026-ARXIV-2602-07306 -->

并行分支也可以不继承上一分支的hidden，而共同读取最初的输入，再由聚合器渐进接纳各分支结果。[ParaFormer首版的受限设计](https://arxiv.org/html/2510.15425v1#S4)把分支计算与聚合依赖分开，区别于各track连续演化后周期交换；但这是重新训练的架构，不是把既有顺序checkpoint原样切卡。存在可表达目标函数的宽度构造，不证明有限模型收敛、相同函数保留或所有深度无用；分支数增加也会改变容量、设备和通信预算。有限视觉任务有较少分支的精度反退，更多GPU的时间收益不等同硬件同质量收益。聚合拓扑、启用日程、全部训练/通信与任务回归都计费；跨分支信息、质量或净预算不合时，保标准顺序stack、原TP或已验证periodic tracks，不从并行可表达性签发普遍加速与替代资格。

<!-- source-family:SF-2025-ARXIV-2510-15425 -->

## Parameter Depth 与 Execution Depth 可以分离

跨层路由决定一次更新读取哪些状态，执行深度则决定这样的更新要运行多少次。以下递归分支沿用局部记号 `T` 表示循环轮次或其上限，与本章开篇表示序列长度的 `T` 不同。

普通 Transformer 把“有多少组不同参数”与“一个样本执行多少次 block”绑定为同一个 `L`。这使
checkpoint、dense batching 与 Pipeline Parallel 都很直接；但当任务所需的组合步数差异很大时，增加
parameter depth 不是唯一选择。另一条实验性分支复用同一个 block，让 full-sequence hidden state 循环
`T` 次，并把 step counter、depth budget 与 readout 明确成运行时状态：

```text
fixed parameter stack
→ shared block + recurrent hidden state
→ per-sample execution-depth budget
→ readout at a defined recurrence step
```

这条路线用参数复用换取可变的内部计算前沿，却没有免费获得“更深推理”。顺序 critical path、activation
residency、不同 `T` 的 batching divergence 与停止规则都会进入系统；若用 learned depth embedding，超出训练
步数还可能失去定义。Pre-Norm、接近 identity 的 gate 或 LayerScale 可以改善早期稳定性，但不能证明任意
开放语言任务会随 silent steps 单调提升。固定深度在吞吐、可预测性和停止证据不足时仍是默认分支；可见
CoT 则继续提供监督与 verifier 接口。Depth-recurrent 小模型实验只支持受控组合任务中的机制可行性。

共享参数也改变残差缩放的前提。独立层的更新若近似不相关，累计方差可随深度线性增加；同一权重反复作用时，更新可能持续同向，累计平方范数则随循环数N呈二次增长。因此不能把N次共享执行简单代成N个独立层，再机械沿用1/√N。对简化共享ReLU分支，在非退化激活质量、受控尺度和positive-cone gain等前提下，共享分支采用1/N缩放；SwiGLU只有实验支持，不能继承该ReLU证明。有L个不同层并保留弱跨层耦合时，可进一步分解为λ/(N√L)。这是初始化与受限更新的条件分析，不是所有Transformer的稳定定理。

这也把loop预算与unique depth的调参分开：在该缩放和更新假设内，循环数不再要求同样的学习率缩放，但跨独立层的深度仍影响学习率；实际最佳值要由训练验证。作者语言建模对照仍出现高学习率发散、后轮相关减弱或变负，不能由参数共享批准任意深度外推。额外展开计算、激活、调参和质量回归均计费；前提或验证失配时保留独立层stack、固定受训loop及重新校准。[受限证据：精确v1 §§3–5](https://arxiv.org/html/2606.18524v1)。<!-- source-family:SF-2026-ARXIV-2606-18524 -->

跨loop复用还可以改变读取范围，而不只重复同一token的更新：第一loop留下全局KV，后续loop各自计算局部window Attention，再按head gate混合冻结的全局读取；另一接口把上一loop的相邻前token状态右移，与本token embedding一起注入，显式改变跨token/loop的依赖。[受限LoopCoder-v2分支](https://arxiv.org/html/2606.18023v1#S3)因此要共同绑定global-cache producer、局部window/KV、loop编号、shift与gate，不是跨轮状态全相同或参数共享就可任意读旧cache。各R模型分别按相应轮数训练/评价，不证明同一checkpoint可临时加R或自适应退出；更多轮也非逐任务单调改善。hidden距离、rank、Attention差与logit差只诊断受测递推，不能把同源变化当独立因果或loop2普遍最优。全部后轮Attention/FFN、局部缓存与展开训练/调度均付费，single-forward和主导阶cache表达不免逐R循环，也不等任意R恒时恒内存。身份、训练支持或净质量失配时，保独立层stack、固定受训R及逐轮状态，不由较少unique参数或局部平均分批准免费test-time深度和思考能力已耗尽。<!-- source-family:SF-2026-ARXIV-2606-18023 -->

共享core之外，还可以显式保存每个token的有限槽状态，而不让一个hidden独自承载全部递归历史：初始embedding放进首槽，其余置零；每轮从当前hidden产生独立的写入与读取权重，把core输出加到各槽，再读取更新后的buffer形成下一hidden。[MeSH的受限分支](https://arxiv.org/html/2510.07739v1#S3)共享的是core，不是所有逐轮router；首槽同样可写，槽内保存的是混合历史而非不可变输入或逐轮原件。应把buffer初始化、写读顺序、router/步号与coda读态共同纳入checkpoint接口，训练外多跑一轮还须有对应router与质量支持，不能由非负混合权重宣称任意历史系数可独立指定或无损模拟所有残差。槽越多不必越好，较少存参也不免每token槽、展开反传和顺序core；初始化/全部读写、训练搜索与独立任务回归均费。状态、路由或净质量失配时，保普通独立层stack、固定受训loop与明确残差锚点，不由高CKA、小更新norm或少参数批准稳定、全历史保存和净加速。
<!-- source-family:SF-2025-ARXIV-2510-07739 -->

后训练复用已有层时，还可避免把深层表示重新送回浅层：先在同一物理层内完成几次局部循环，再进入下一层；首轮保留原残差路径，后续轮次分别用hidden-wise gate调节Attention与MLP写入。[受限upcycling分支](https://arxiv.org/html/2610.25004v1#S3)改变的是重复计算的接口与写幅，不等于复制出不同参数的深层网络，也不由小gate证明收敛或更多轮必然更好。训练同时监督各深度并鼓励后轮改善，整体收益不能全归门控；跨轮KV共享又是需另验质量的近似。额外循环、激活/KV、监督与调参仍付费，所测更深循环存在边际收益递减，净推理节省尚未实现；预算或质量不合时保留原单pass、固定受训loop及逐轮独立状态，不以共享参数替代计算和缓存验收。<!-- source-family:SF-2026-ARXIV-2610-25004 -->

共享层的执行预算还可以预先收敛成一个有限菜单，而不让每个token自由决定循环深度。固定一个中层窗口，为各预算重复该窗口的前若干层；被选层连续执行两次，再进入下一物理层，一次请求内所有token保持同一路径。训练每个micro-batch只抽一个菜单预算，并让全部data/expert-parallel worker使用同一选择，避免MoE通信顺序分叉。[这一弹性深度分支](https://arxiv.org/html/2610.32492v1)共享两轮的attention、expert、router与gate参数，却分别保存每轮的负载统计/balancing bias及KV；共享权重不等于共享运行状态，activation重算也须恢复原路径和相应轮次状态。

有限菜单的资格还必须贯穿后训练：SFT继续抽样全部受训路径，按领域训练的RL experts也覆盖同一菜单；合并expert增量后，student在自己生成的response上接受同领域teacher监督，而teacher使用与student相同的循环预算、token与prefix。这里的负裁剪log概率比只是token级蒸馏信号，task reward可只监控而不入该阶段目标；它不是把深预算teacher的分布直接移给浅路径，更不是证明其它预算或任意循环外推有效。每预算分别组织optimizer更新也会改变“一个training step”内的实际更新数，预算抽样、更新时钟、expert合并系数和teacher身份都应与checkpoint一起保存。

同token或估算FLOPs匹配的有限specialist对照支持一个checkpoint覆盖多个工作点，但两种预算控制不是同一实验，结构选择的小loss差也不构成通用最优配方。更多执行并不保证每个任务单调提升，预算匹配teacher又未被单独消融成唯一原因；共享路径、merge和蒸馏的联合收益不能全归给其中一个接口。各轮独立KV、更多顺序执行、多expert训练与teacher评分均付费，较大预算在原单H800测量中延迟和驻留内存都增加；无权重复制不等无额外费用，也不授在线混合预算的SLO。任务、路径或净预算未过时，保留固定预算specialist、原单pass与已验证的受训菜单，不将模型存参复用解释为免费弹性推理。<!-- source-family:SF-2026-ARXIV-2610-32492 -->

顺序 state-tracking 还可把“第 k 轮算了什么”直接放进监督：让它预测前 k 个操作后的中间 state，而非每轮都猜最终答案，再把各 token 的循环 state 缩回第一轮的 RMS 尺度。这个约束组合试图让额外深度复用同一操作规则，不由固定 norm 证明整个 transition 严格不变。[PAR 的有限消融](https://arxiv.org/html/2610.27628v1#S3)支持进度与尺度缺一时外推受损，但依赖可定义前缀和顺序中间 state，graph reachability 并行 frontier 反而不合；没有 step labels 时仍需 final 答案、prefix teacher 与额外适配。完成读出也须和 answer 有效期分开：确认多轮 Yes 后应返回初次触发时保存的答案，不能把后续仍说完成当 state 未漂；确认窗口仍支付更多执行，换训练方式还可能要换 stopping 规则。中间监督、展开/截断反传、尺度控制与独立质量回归均计费；任务无 canonical 进度、信号不稳或质量失配时，保固定受训深度、可验证显式 CoT 与原 loop，不以更少可见 tokens 或已知深度 oracle 签发通用长度泛化与加速。<!-- source-family:SF-2026-ARXIV-2610-27628 -->

已知算法状态时，递归还可在每步加入离散锚点，而不让连续hidden无限传递：分别预测若干状态因子，取离散值后重新embedding给下一轮，并用中间状态标签及受扰状态训练恢复。[受限模运算对照](https://arxiv.org/html/2510.14095v1#S4)支持这份监督与状态接口，但因子分解、计算步数和正确中间态是任务已知信息，不是任意语言模型自己发现了可验证思考。Argmax会丢失不确定性，选错状态也会改变后续轨迹；标签制备、逐轮执行、扰动训练与完整任务回归都付费。状态定义、监督或新长度质量不合时，保留连续state、固定受训loop或可核显式CoT，不由小型组合任务近满分批准开放域推理、独一电路因果或免费深度外推。

<!-- source-family:SF-2025-ARXIV-2510-14095 -->

执行次数之外，还须声明额外工作位置和每次运算允许保存什么。一个[受限表达力分析](https://arxiv.org/html/2605.30523v1)把 polynomial padding 当并行中间计算空间，把 loop 当复用参数的计算图展开；在可按输入长度构造的 uniform 模型族及逐运算 fixed-point rounding 下，宽度与精度即使给出相同量级的表示体积，也不必拥有同样表达力，继续增宽不能无条件补足精度。位置编码、温度、padding 和构造器复杂度都是前提，增长深度时的 uniformity 类也不能沿常深度结果直接照搬。这里的 rounding 能把微小数值间隔变成离散选择，不是浮点 GPU 自然实现同一定理；充分体积不认证可学习性、固定 checkpoint 的长度泛化或端到端速度。形式条件、实际精度或训练质量未建立时，保留固定 stack、受训 loop 与独立任务测试，不由参数少、scratch 多或理论可表达签发更强实用推理。<!-- source-family:SF-2026-ARXIV-2605-30523 -->

可见CoT与内部loop的交换还需要对齐持久状态，而不只是多跑共享层。[一个受限queue模拟构造](https://arxiv.org/html/2610.25998v1#S4)为每个loop iteration保留独立KV，仅从旧位置的同iteration读取；queue长度与L同余的设计使一次token内部执行L次transition，再发出间隔L步的机器状态。对固定机器及满足其space/loop条件的重新实例化，visible窗口与输出token可缩小L倍，总KV却仍为Θ(L×窗口)，serial block工作亦未减少。起始各iteration的正确cache还是显式预载假设，普通prompt Prefill没有被证明能构造它，初始化费用也不在界内。有限精度softmax模拟hard选择另依赖指定binary32下溢、累加与cast合同，不由生产kernel也减最大值便自动满足；它不证明自然语言trace等价、训练可学或端到端提速。预载、全部KV与内部执行均须进入实际预算，条件或任务质量未建立时，保留普通stack、受训loop及可验证显式CoT，不把更短可见窗口当更小总状态。<!-- source-family:SF-2026-ARXIV-2610-25998 -->

固定主干也不意味着目标模型的信息凭空消失。一个[受限 universal-transformer 构造](https://arxiv.org/html/2605.31423v1)将目标 attention-only 网络的权重编码到输入 embedding 矩阵，由固定稀疏路由逐层读取各 head 路径；它模拟的是明示的同规模模型类，而非任意实际 LLM。容纳全部路径的 embedding 可随深度指数增长，attention-matching 分支的下界也不能推广成所有模拟器的最小成本。随机固定主干“几乎处处存在可用 embedding”不是优化可找到的保证，有限实验还同时训练 unembedding，并依赖 Norm/residual 改善较深任务。应把目标描述、embedding 容量、固定与可训练参数、模拟精度及全部训练/执行费用分开计量；小任务或优化失效时保留普通可训练 stack、受训 loop 与较窄适配，不把冻结权重签成免费通用计算或已获长度泛化。<!-- source-family:SF-2026-ARXIV-2605-31423 -->

共享计算也不必沿预先固定的模块顺序展开：可保留一个可复用的模块池，让每个 token 在有限步数内选择下一模块、再次访问旧模块或走 identity；同一步被送入同一 Attention 模块的位置才共同参与该次读取。这改变了内部路径与可见支持，而不只是替某层 MLP 选择 expert 或把一个 block 统一多跑几轮。[DNA 的受限对照](https://arxiv.org/html/2506.22389v1)还保留少量固定前层，不能把自由接线理解为无训练约束；模块访问次数、去重后的活跃参数与总驻留容量须分账。路径相关或可视化不证明语义分工，少算模块仍可能损害质量，也不替 runtime 完成重排、负载和跨设备通信。Router、训练搜索、稀疏 Attention 与调度均付费；路径不稳、质量退步或执行节省无法兑现时，保留固定层序、普通 MoE 或受训的共享 loop，不由 active-parameter 数量批准真实加速与异步训练。<!-- source-family:SF-2025-ARXIV-2506-22389 -->

把已预训练的VLM改为共享loop，还须恢复被改变的接口，而不只替换层指针：剪去部分中层后，以prelude状态和上一轮state组成adapter输入，先恢复文本backbone，再对齐projector，最后恢复视觉指令路径。[Recurrent Retrofit的受限对照](https://arxiv.org/html/2610.22075v1)中，每pass仍有独立KV身份，默认存参少18.1%却走56层而非原22层、KV为2.55倍；循环复用较少cache副本则改变可读状态并损质量，首次pass共享K/V也需相应训练，不能任意当exact cache优化。固定r6训练在其它深度可崩溃，sampled-depth虽较稳定却未呈随loop单调获益；额外文本/KD、projector对齐、全VLM恢复及状态费用均须计入，阶段消融又同时改数据和监督投入。恢复、per-pass状态或预算失配时，保留原feedforward checkpoint、固定受训loop与独立跨模态回归，不把参数压缩等同更少执行、KV或更快推理。<!-- source-family:SF-2026-ARXIV-2610-22075 -->

需要固定上下文锚点时，还可把一次性的 causal encoding 与反复 state refinement 分开：encoder 为各 recurrent 层产生 forward 内固定的 Global KV，decoder 每轮从当前 state 重算 Local KV，让 query 在两路各自 causal 的支持上用同一个 softmax 分配权重。这不是把每轮 KV 任意合并的 cache 优化，而是需端到端训练的新信息读取路径；固定 anchor 也不等于直接把 encoder 输出每轮相加。[AsymLoop 的有限对照](https://arxiv.org/html/2610.28489v1#S3)支持两路共同读取，但 layerwise 学习率、额外投影与 attention 均影响收益，同有效层深/训练 tokens 并非同 FLOPs。较小模型补做的扩宽近 FLOP 对照仍保部分 loss 优势，却有训练 step 更慢的配置，未证明 decode 提速、任意增加 loop 稳定或更深必然更好。全局 KV、每轮局部状态、反向图和优化诊断都付费；重训、存储或实际净收益失配时，普通不同参数 stack、既有受训 loop 及逐轮显式 KV 仍是合理分支。<!-- source-family:SF-2026-ARXIV-2610-28489 -->

内部计算也可沿序列位置增长，而非只在当前位置反复运行共享 block。一个 continuous-thought 分支把 top-layer state 反馈为新的连续输入位置，写入后续 KV，只有需要可见输出时才作 vocabulary prediction。它保留了跨位置的 causal history，因此不是前述 same-position recurrence；省下输出词表接口不意味着省下追加位置的 attention、cache 或共享层执行。

训练可以并行 refinement，decode 却按这些连续位置顺序展开，二者的依赖图和实际成本不能互换。block application 数不等 FLOPs、KV 占用或 latency：同 block count 的物理加深仍可更好，vanilla baseline 也未按全部训练 FLOPs 匹配；分别训练的 K 不授予推理时任意切换预算。受限结果只支持参数容量与内部计算的一个取舍。串行等待、cache 增长或质量回退时，固定深层、原共享 loop 或可审查的显式 CoT 仍合理，不能把 continuous thought 写成免费计算。 [必要机制与反证](https://arxiv.org/html/2609.21605v1)。<!-- source-family:SF-2026-ARXIV-2609-21605 -->

跨位置复用还可在core内为同一token设置两个有序slot：latent slot读当前prefix表示，prediction slot另加上一token已完成的latent，两者共position ID、以前者在先的causal次序一起运行共享core；只prediction经过suffix预测，latent留给下一token。[受限双slot分支](https://arxiv.org/html/2610.25086v1#S3)移除了当前两轮之间的等待，却没有精确保留同token串行两次core的计算。训练先warm再在扩展slot序列上作少量Jacobi更新，读取前一轮shifted state；这仍是近似训练路径，局部状态趋稳不认证任意输入收敛或答案正确。相同参数/原token数未匹配warm、双slot Attention/KV、反向与调参费用，decode小幅慢于vanilla的局部测量又未计prefill与服务全程。应同时验boundary零态、slot顺序、训练/生成状态偏差及真实质量费用；准备串行成本、长prefill或稳定性不合时，保原单slot stack、受训显式loop与原cache，不把一趟paired调用签成免费双倍深度。<!-- source-family:SF-2026-ARXIV-2610-25086 -->

跨位置反馈还可把可监督的中间思考留在辅助模块，而不追加主模型的输入位置：[一条受限分支](https://arxiv.org/html/2602.08332v1#S3)读取一个 input chunk 的深层表示，由轻量 head 生成自然语言 thoughts，再压成固定大小的状态，加到下一 chunk 的浅层表示。这样以状态递归替代主上下文中的思考 token，但仍运行辅助生成、压缩和原 causal KV 路径。

训练若已拥有逐 chunk 对齐的 gold thoughts，可以先压成 gold states 并 teacher-force 各位置，消去跨 chunk BPTT、并行计算 backbone；线上没有 gold history，chunk 之间仍要等待实际状态。预设后续状态为空再固定最早有效边界、重算后缀，只在空状态足够稀疏时改善 prefill，轮数不等 TTFT。有限 Qwen task fine-tuning 的 GSM 质量仍低显式 CoT；问题目标直到尾部才揭晓时，早期状态还会追错量。对齐教师、附加模块与重算都增加费用，thought 可见也不认证内部忠实性；监督缺失、目标晚揭晓或净成本不合算时，保留原 fixed stack、连续输入反馈与可独立验证的显式 CoT。<!-- source-family:SF-2026-ARXIV-2602-08332 -->

跨位置反馈也不必全部回到新的 input embedding。一个更细的旁路把过去位置的高层状态，经连接专属的线性投影，加到后续位置的低层更新：`h_l^i = LayerBlock_l(...) + α D_(s→l)(h_s^(i−g))`，其中 `s>l`、`g≥1`。它避免同一位置高层与低层互相等待，保留因果次序；改变的是内部层之间的状态路径，不是新增 vocabulary token。按 `g` 个位置分组可减少这条 downward 路径的串行前沿，却不取消普通 causal attention 对组内先前位置的读取，也会缩短可沿序列累积的反馈路径。训练与 prefill 因新增高→低依赖而损失部分并行性，投影参数、过去 hidden state 与执行开销仍需计费；autoregressive decode 本来串行，不等于旁路没有额外成本。[受限 fine-tuning 对照](https://arxiv.org/html/2602.17993v1#S4.SS4)中，group size 与增益 `α` 的组合会改变训练时间和质量，大分组配大增益还可退步；参数数近似匹配与单一 soft-token 控制不足以证明所有 latent reasoning 的优劣。任务不需要这种内部路径、串行准备成本超预算或更新失稳时，原 fixed stack、连续输入反馈和显式 CoT 仍应保留。<!-- source-family:SF-2026-ARXIV-2602-17993 -->

高→低反馈也可只保上一token的core输出，直接加到当前固定prefix表示，再运行一次middle core，suffix仍只读当前结果；不必为同token建立两slot或另加投影。[受限单state分支](https://arxiv.org/html/2610.25076v1#S3)的增加深度来自沿token传递的计算，而非当前token免费多跑几层。Teacher forcing则先warm，再用前一轮shifted core state作整序列Jacobi更新并完整反传；少量训练更新与严格从左到右decode不是自动相同的state，packed boundary、误差与prefill费用应独立验。受测random-depth训练比fixed-depth更能耐额外迭代，但fullcore或较晚core仍可差于vanilla，状态趋稳也不保证普遍收敛和任务正确。相同参数和训练tokens不等相同FLOPs，近vanilla的decode时延又未计训练或prefill；全部展开、cache/state、调参与质量回归都付费。反馈失稳、长序列准备或总预算不合时，保留原fixed stack、较窄受训core与已验顺序计算，不从无新增参数签发无成本深度。<!-- source-family:SF-2026-ARXIV-2610-25076 -->

这种跨位置旁路还可以保留每一步可见 token：将上一位置的顶层状态 `h_t` 经由包含 RMSNorm 与线性投影的适配器 `A`，和下一 token 的 embedding 相加，再运行原 Transformer：`h_(t+1)=T(Emb(x_(t+1))+A(h_t))`。这里增加的是顶层到输入的直接通路，普通 causal Attention 的 KV 历史仍在，不能说原模型只保留了离散 token 或新状态替代了 KV。与只循环同一 token、只回馈 middle core 或新增不可见位置相比，这一选择保持原可见生成接口，却给训练与 Prefill 新增了跨位置依赖。

为保留序列并行，可用前一 pass 的 shifted hidden 近似当前 pass，并在各 pass 都施加 next-token loss；[受限 Recycler 对照](https://lf3-static.bytednsdoc.com/obj/eden-cn/hyvsmeh7uhobf/recycler_arxiv%20(2).pdf)采用零初始化适配器及 tied embedding，但浅训练深度不保证长生成稳定，较大配置已出现外推回退，需要额外训练。单 pass 与双 pass Prefill 是不同质量/准备成本工作点，少量 adapter 也不免除多 pass 训练和状态驻留。部分任务退步、较短 baseline 训练轨迹及不同 RL 路线配置，均不支持“免费能力”或严格同总计算优势；未披露完整硬件、精度和服务负载时，更不能由相近逐 token 算子数批准端到端 SLO。训练支持、深度外推或总预算失配时，保留原固定栈、已验 core 反馈与显式 token 路径，分别验质量、准备和 Decode 费用。

<!-- source-family:SF-2026-SEED-RECYCLER-20261025 -->

可变深度的训练还取决于停止器的初始先验，而不只是推理时把 `T` 上限调高。若 Adaptive Computation Time
一开始就以较高停止概率在浅层读出，需要深度的样本可能始终走不到后续轮次，深路径也收不到足够训练信号；
给共享 block 配 scratch slots 时，应把停止偏置、允许的训练轮次与 scratch 容量联合校准，并分别观察实际
停止轮次、深路径质量和延长计算的收益。<!-- source-family:SF-2026-ARXIV-2604-21999 -->

较低的初始停止概率可为深路径创造学习机会，却增加串行计算与显存占用；scratch 太少可能限制可用状态，
太多又可能稀释注意力。相关结果只来自单块约 3.2M 参数的 Sudoku 受控实验：不同初始偏置、`T` 上限与
scratch 数量共同改变结果，不能据此推出所有递归架构或大语言模型都必须配置显式 memory slots。早停
校准不可靠、收益无法覆盖成本时，固定深度或原有分层 block 仍是有效回退。

### Token 位置与 Latent Step 是两条依赖轴

统一循环预算还把不同位置的执行深度绑在一起。若以 `t` 表示 token 位置、`k` 表示 latent step，一条条件分支只允许当前位置读取满足 `t_j≤t_i` 且 `k_j≤k_i` 的状态，使同一 `k` 的活跃位置能批量推进。这是改变二维依赖图，不是精确保留“读取所有过去位置的全部 latent steps”的原计算；训练 critical path 可以按最大 `K` 计步，却仍支付各活跃位置的 block、Attention 与状态成本。autoregressive decode 仍须等待前一个可见 token，不能把训练并行前沿换成部署时所有 token 并行。<!-- source-family:SF-2026-ARXIV-2602-08220 -->

每个位置还可以持有继续概率 `g_k`：到达第 `k` 步的 mass 是先前继续概率的乘积，退出 mass 为该 reach mass 乘以 `1−g_k`，据此混合各步状态。以阈值剪掉低 reach 的后续执行，并在预算上限把剩余 mass 交给最后执行态，会把预算策略直接写入 readout 语义，而不只是少跑几个 block。训练可用正确 token 的预测概率、stop-gradient 与继续惩罚来学习 router；这种 target-informed 训练信号不代表部署知道真实答案，线上只拥有 router 分数和预算权限。同一 token 的 latent steps 共用 position ID，也不让多轮 KV 读取或中间状态免费。

mask、router、reach 阈值、最大步数及停止训练的权重须共同版本化；阈值漂移、稀疏批处理和过早停止都是新增成本与 failure mode。[有限从头预训练对照](https://arxiv.org/html/2602.08220v1#S4)报告的是 Pile、小模型与估算训练 FLOPs 下的质量取舍，不是 wall-clock、生产吞吐或 SLO；平均提升中仍有单项退步，router 消融的小差值也不足以认证在线正确停点。依赖图不适合任务、停止器不稳或实际执行节省不足时，统一固定预算、原 recurrence 与显式 CoT 继续成立；输出正确性仍交给独立任务验证。

停止器还要声明它在何时拥有何种信息。便宜的浅层预测器可以一次决定每个位置的深度，逐步停止器则读取已经付费得到的中间状态再决定继续；二者的决策调用费用与实际活跃 token-step 须分账。采用离散退出时，已退出位置可冻结在该深度，让其他位置继续读取其 KV；请求更深轮次只读取该位置最深已缓存状态。这保留退出语义而非完整深度的原计算，也不是把退出 token 从历史中删除。[受控递归实验](https://arxiv.org/html/2602.08864v1#S6)中，早期分配更关联结构线索，线上停止更关联执行状态，但相关分析只来自已答对人口；分配随算法复杂度增加也仍会在未见长度失效，自然语言更难切片甚至没有多分深度。故应把决策身份、freeze/cache 规则、训练与部署停止口径、质量和长度泛化共同版本化，不能用 depth/D 认证完整加速或把“多算”当正确性。停止头、静态训练展开与稀疏执行都付费，缺少可靠停点或质量回归时回退统一预算与独立任务验证。<!-- source-family:SF-2026-ARXIV-2602-08864 -->

### 单时钟与双时间尺度的递归

单一 recurrence clock 仍可能把“快速局部更新”和“较慢全局整合”绑在一起。层级递归分支可以用两个
parameter-shared modules 形成不同时间尺度：fast module 在局部 steps 内更新，slow module 只在外层 cycle
读取/写回全局 state，再由明确定义的 step 产生 readout。

```text
input / shared state
→ fast recurrent updates
→ slow recurrent consolidation
→ next outer cycle
→ readout at a declared horizon
```

这增加 effective depth 而不同比增加 parameter depth，却把 credit horizon、stop/readout policy、state
initialization 与 batching divergence变成训练和 runtime contract。PrefixLM、response-only loss 与 task-formatted
data 可能与 recurrence 共同贡献结果，不能把联合配方的收益全部归因于结构。HRM-Text 的作者实验只支持其
1B、固定 context 与任务格式中的机制分支；固定层深、单 clock recurrence 和显式 CoT 在可预测 latency、
通用 raw-text 或可验证中间过程更重要时继续成立。

双时钟的前向有效深度，还须与训练中真正保留的反向信用跨度分开。一条受限分支先在不建图的条件下推进快慢状态，仅为末次局部更新建立梯度路径；多个 segment 再分别读出、监督和更新参数，传到下一段的状态则 detach。这用较短反向图换取较低的跨轮 activation 保留，却不等于完整 BPTT 或精确隐式求导：固定点的精确梯度需要相应可微、可逆与达点条件，把 Jacobian 逆只取首项又是另一层近似，有限前向循环也不保证已经达到该点。[HRM 的受限 v1](https://arxiv.org/html/2506.21734v1)只支持这条状态/信用分工，不把轨迹趋稳或生物类比升级为普遍收敛与推理能力证明。训练可用答案真值监督 halt/continue 评分，部署却只有模型分数与预算，停止不认证答案正确；“单次 forward”内仍有多次模块更新和后续 segment。分段训练、任务样本与增强、重复推断/投票及状态管理都计入费用，不能把少样本主结果与更大数据上的结构分析合为同一预算。近似信用、停止校准或质量不可靠时，应保留较短的显式展开/BPTT、固定计算预算或可核验的显式 CoT，再独立检查任务结果。<!-- source-family:SF-2025-ARXIV-2506-21734 -->

截短反向图是否划算，还取决于前向轮数是不是必须固定：以T表示共享block执行次数、B表示末尾保留梯度的轮数，B<T在边界detach会省反向工作，却改变训练信用跨度。一项[受限loop scaling对照](https://arxiv.org/html/2610.26030v1#S5)中，固定T后重分模型与数据预算可偏好截断；允许同时减少T、增加B时，同architecture和tokens、相同T+2B的循环FLOPs却偏好较少轮full BPTT。这个选择依赖拟合法则中backward收益相对forward的条件与有限整数菜单，不是所有递归模型的最优定理；全部参数也可自由增加时，同一法则反而偏好非共享stack。两轮full近parity与多付训练compute后的反胜应分开报告，不能合成同预算优胜。拟合、全部训练、activation保存/重算与部署循环均计费，FLOPs配平也不保证HBM或墙钟配平；受限信用跨度、预算或任务质量不合时，保留原截断recipe、较短full BPTT或普通stack，以真实学习和执行回归选取，不只按参数省量决定循环深度。<!-- source-family:SF-2026-ARXIV-2610-26030 -->

层级也可沿序列分辨率组织，而不只让两个module持有快慢时钟：对因果chunk作pooling，让不同分辨率以共享core及各自recurrence预算更新，再交回细粒度位置。粗状态包含哪个chunk必须显式定义；g−1 shift用于避免当前位置读取尚未到达的同chunk信息，overlap另影响覆盖与质量，不把二者合称因果保护，pool/upsample、边界和位置身份须保持同一因果图。它改变多分辨率依赖与局部执行预算，不是对完整token recurrence的精确缓存优化。<!-- source-family:SF-2026-ARXIV-2602-11698 -->

Pooling、交接和overlap仍有算量与细节损失，较少prefill FLOPs不等wall-clock、decode费用或长历史无损。[Spiral exact-v1](https://arxiv.org/html/2602.11698v1)在Pythia160M–1.4B/Pile250B/context4096的受限对照中，移除overlap会伤质量，而相关baseline也受益，不能把全部收益唯一归因于hierarchy。预算、chunk边界或质量不稳时，保留完整token recurrence、固定层深或显式CoT；需要可寻址历史时仍按第22章独立验收，不靠增加局部loop补回被合并的信息。<!-- source-family:SF-2026-ARXIV-2602-11698 -->

多分辨率也可通过嵌套的层栈组织，而不只让共享core分配不同循环预算：细粒度ResBlocks之间插入down-pool、递归的inner block与up-pool，并让同分辨率skip绕过这组较粗计算。这样把局部细节路径与低频更新的粗状态分开；按块内位置使用不同线性映射再求和，仍可保留部分顺序信息，却把多个向量压到一个，后续上采样恢复shape不等于恢复全部输入。各层pool因子、块边界、返回位置和fine skip须同属一份时序合同，粗层不能在细位置读取尚未到达的同块输入；未展开shift、尾块与cache/reset时，不从“autoregressive”名称补成完整流式配方。

[Poolformer的受限raw-audio分支](https://arxiv.org/html/2510.02206v1#Ch3)支持这种粗细消费者分工，也说明记忆读数要换回真实时钟：输入相关门改变每步实际衰减，粗层每步又跨更多原始位置，平均base系数更接近一不能独自证明深层唯一承担长依赖或固定状态无损。有限同层数/近参数对照的pool改善训练吞吐与部分感知指标，但最佳验证点对应的NLL未全面胜出，扩大state和换长音频人口也有反退；训练epochs/h不代生成速度，八位量化更不等原音频无损。全部pool/unpool、粗细递推、量化/训练与多配置选择、完整采样和独立长依赖/内容回归均付费。块对齐、细节或完整预算不成立时，保留完整token递推、已验因果chunk分支或显式Attention，不由恢复长度、base衰减图或较快训练批准任意LLM/VLM替换与无限记忆。

<!-- source-family:SF-2025-ARXIV-2510-02206 -->

### 共享 block 的混合频率与校准身份

混合频率又是不同于 mixer 可行性的约束：逐子层混合让各流及时交换信息，却在中间 block 反复复用权重时重复支付混合。另一条条件分支保留多条 residual stream，仅在一整轮共享 block 结束时混合，再进入下一轮；输入/输出混合加 diagonal sigmoid carry 不要求双随机守恒，也不保证差异方向完整。loop-specific 位置和少量参数意味着这不是“所有权重严格共享”，少几次 mixer 也不等于少执行 block、少保留 activation/KV 或少付训练 FLOPs。<!-- source-family:SF-2026-ARXIV-2604-21254 -->

共享权重在各轮看到不同 activation，量化校准需覆盖各轮而不是只画像第一轮。[受限 Hyperloop 对照](https://arxiv.org/html/2604.21254v1)支持所测架构与 INT4 的部分质量/权重取舍，但 depth-matched 不等 compute-matched，过训练 PPL 与训练吞吐亦有反向结果；未证明动态早停或生产延迟下降。混合/校准失配时可回退普通 loop 或非共享层，成熟并行与固定延迟更重要时标准 residual stack 仍合理。前面讨论的 Parallel Tracks 把状态放在不同并行路径，交换的是跨设备融合频率，不是这里同一共享 block 的循环轮次。

### Recurrence 可以只占据 Decoder 的局部层段

复用完整 block 或完整 decoder 进行 silent recurrence，状态边界最清楚，却会让每个额外 reasoning step 重跑所有层；显式 CoT 则把步骤暴露成 token，便于监督和验证，但增加输出长度并把内部计算承诺给语言表面。若额外计算只在某类结构化变换中有价值，可以把执行深度局部化：lower decoder prefix 只运行一次并产生 boundary memory，选定的中间层段维护 recurrent state、按内部时钟迭代，达到声明预算后再交回普通上层 decoder 生成答案。

```text
lower decoder prefix once
→ versioned boundary memory
→ localized recurrent state for T internal steps
→ fixed upper decoder and answer generation
```

这里 checkpoint 拥有 recurrence span、time modulation、memory readout 与最大预算；runtime 只执行已发布的预算策略，不能把 latent step 数当作可随意增加的“免费思考”。局部化可少重跑无关层，并在受限结构化任务上形成 latency—accuracy 分支，但新增循环稳定性、boundary-memory 陈旧、不同 `T` 的 batching divergence 和隐藏推理不可解释性。validation-selected budget 也只是在给定分布上选 operating point，不是逐请求正确性证据。

当任务需要可审查的中间结论、增益不随 recurrence 深度稳定增长、循环状态失稳或 SLO 不能容忍额外串行步时，应回退固定 decoder 或显式 CoT。现有 exact-v1 结果只支持作者披露的 structured-reasoning 设置；Deep ListOps 的非单调结果尤其阻止把更多 latent steps 写成普遍收益。

<!-- source-family:SF-2026-ARXIV-2607-25915 -->

### Fixed-point Refinement 是 Recurrence 的条件分支

固定次数的 looped Transformer 用共享权重反复修正状态，参数经济但训练不稳，推理成本也固定。另一条分支把 refinement 写成 fixed-point solve：backbone 产生初始 proposal，solver 持有迭代状态，convergence rule 只提出停止，任务与数值 gate 决定是否接纳；implicit differentiation 使反向内存不随有效深度线性增长。它以自适应深度换来收敛失败、求解开销和隐式梯度数值风险。未收敛时应限制迭代并回退固定深度或显式 loop，持续记录 residual 与 per-sample convergence。exact-v1 只支持作者规模、任务和容差，不证明任意输入收敛、无限深度免费或普遍硬件收益。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12466 -->

表达能力还要区分逐输入的极限与有限预算能交付的函数：一条[函数空间存在性结果](https://arxiv.org/html/2510.03638v1#S2)允许收缩模数`mu(x)`随输入变化，在有界域上以满足输入方向Lipschitz等正则条件的共享operator的固定点表达局部Lipschitz目标；它不是固定大小神经网络可学、统一步数足够或全局input-output鲁棒的证明。以`x∈(0,1]`、`G(y,x)=(1−x)y+1`、初态0为例，每个固定x都收敛到`1/x`，但任一固定T的误差`(1−x)^T/x`在边界附近无界；逐请求存在收敛与统一latency预算因而不能互换。停止残差亦须连同收缩裕量验收，误差界中的`1/(1−mu(x))`会放大小残差及算子/数值误差，state收缩不认证输入扰动下的任务输出。若要求统一误差和最大步数，就需另限制输入域/收缩、验证学习到的operator及实际求解成本，而不是从存在性批准多算必有益；训练、反向和全部迭代照计，条件或预算不合时仍回固定深度、受训loop或外部task gate。<!-- source-family:SF-2025-ARXIV-2510-03638 -->

数值方法的名称还应与实际训练的展开图分开：一条[有限迭代分支](https://arxiv.org/html/2509.22463v1)先作显式残差初估，再在同一block参数下反复修正，并将先前block的输出按可学习系数混入；它保留有限次数的完整执行，不等于已经求得隐式方程的解，也不继承隐式微分的内存性质。精确Backward Euler对某些刚性系统稳定，不保证求它的Picard迭代收敛：在y=1、h=1、f(z)=−2z时，隐式解为1/3，显式初估后的迭代却为−1、3、−5；有限修正仍需自己的Jacobian、步长、混合与任务验收。若部署预算承受不了全部修正，可离线按各层迭代前后的余弦变化提出删步配置，再用完整教师的层输出MSE、最终分布KL及原next-token目标恢复；这个proxy不拥有任务重要性，正比例变幅也可余弦不变，保留的每层次数不是线上逐token正确性停止器。共享参数、保初步和较近hidden都不能认证删步无损，r按测试PPL选过的结果也不能再当独立择参验证。局部压缩后相对完整迭代变快，却仍慢于普通单pass，部分任务与较大模型保持率仍退；完整预训、教师前向、影响采集、额外蒸馏、历史状态及每步KV/执行费用都计入。数值、质量或净预算不合时，保留单pass、固定受训loop或完整未压缩模型，不用‘隐式’与更少参数批准稳定、更少可见推理或总服务提速。

<!-- source-family:SF-2025-ARXIV-2509-22463 -->

数值几何还可以把范数有界直接写进状态表示，而不把它当作收敛证明：让每个token保持单位范数，沿球面向输入注入，再运行共享块；proposal与当前状态的最坏token夹角残差提出停止，角度阻尼限制每步移动。[受限球面分支](https://arxiv.org/html/2610.25646v1#S3.SS2)的存在性仍需连续与避反极点条件，局部收敛需切空间谱和固定步长窗口，足够强输入注入的全局结果又是另一组固定input/network条件；patience调步并不自动认证这些前提。单位范数、小残差、唯一解和答案正确因而是四件事，强注入甚至可很快收敛到不解题的状态。该分支仍用分段BPTT与detach，并非免费隐式反传；几何更新、全部求解/训练与任务回归均计费，小puzzle单seed和混合published/retrained对照不授普遍架构优势。数值条件、质量或净预算不合时，保固定深度、显式loop/已验solver与外部task gate，不以球面有界批准任意输入收敛或正确早停。<!-- source-family:SF-2026-ARXIV-2610-25646 -->

对多个不同层组成的共享 block，收敛诊断还须保留层在 cycle 中的位置：完整 block 的重复更新趋于固定点，不要求每个中间层的输出也趋于同一个点；它们可以构成重复的有限轨迹。因此应比较“同一层跨 loop”的状态，而非把相邻不同层仍有差异当作发散。在 tied Q/K 与有界输入条件下，小的同层状态差可约束 attention-pattern 差，但这只是条件蕴含，不证明任意 looped 架构必然收敛。<!-- source-family:SF-2026-ARXIV-2604-11791 -->

[有限 looped-LM 诊断](https://arxiv.org/html/2604.11791v1)用第128次循环作为近似 reference，Ouro 仍可出现 successive change 很小却不接近该 reference；input injection、norm 及共享层段的选择改变受测稳定性，稳定的 Huginn 又未呈现清晰的 attention-mixing stages。ColSum 是 attention proxy，不是信息贡献或推理正确性，所以周期重复、状态停滞与任务可停止仍是三项验收。更多循环、状态读取和诊断均计费用；不能独立验证答案、固定点或串行预算时，保留固定深度、显式 CoT 和外部 task gate，不由这一观察签发通用 early exit 或“增加循环就更会推理”。<!-- source-family:SF-2026-ARXIV-2604-11791 -->

有可定义中间答案的任务，还可把“算得够深”“学得到”和“当前state真被后续使用”分开：同有效layer calls下，共享loop的逐hop表示可能较早出现，untied stack换较低学习率或加中层监督后也能学会，因此失败不等不能表示。[受限排列遍历诊断](https://arxiv.org/html/2610.24135v1#S5)的probe、原head读出及同图不同起点state替换支持部分迭代状态参与答案生成，但不证明一个loop恒等一个算法步；训练预算变动会让一轮容纳多hop，换图patch与部分seed又不支持通用可组合程序。比较还包含初始化/iterationembedding差异，部分probe采用共享prompt的row split，不能将所有差额归唯一weighttying或纯因果hop。训练、LR/中层监督、probe/双run干预及全部loop/KV均计费；自然语言、未见长度或额外loop未经验证时，保固定受训预算、untied stack及独立任务verifier，不从线性可读中间state签发普遍推理或可靠早停。<!-- source-family:SF-2026-ARXIV-2610-24135 -->

反复计算也可改变被更新对象，而不只重用同一feature变换：让输入表示配置场的算子与source，从新初始化的field开始有限演化，再由演化后的field及其空间梯度组合读出结果。这里representation负责配置operator，field负责数值状态，readout负责交回任务，三者不等同于求共享Transformer状态的fixed point。[Metriplector的受限实例](https://arxiv.org/html/2603.29496v1)提供此替代primitive，但图像的coupled field与语言的因果一维scan是任务特定实现，不是同一算子直接覆盖全部域；有限CG/Euler和Noether命名也不认证精确解、守恒或symplectic执行。算子/field状态、求解与反向、substeps/readout全部付费，语言模型的参数、token/context和硬件预算并不匹配GPT对照，较少训练token不证明净计算更省。数值条件、readout或质量费用失配时保留标准layer、显式loop或已验固定深度，分别验任务与数值误差，不由物理术语批准普适架构优势。<!-- source-family:SF-2026-ARXIV-2603-29496 -->

还有一条不求 fixed point 的停止分支：先令共享变换的不同 depth 状态保持可比较的表示几何，再用训练 batch 中各 sample/iteration 的 task loss 相对次序监督独立 halting head，推理时以历史 score 分布的经验 quantile 选择阈值。它把中间表示的可比较性、停止 score 与部署预算分开；quantile 只校准相对顺序，不把低 loss rank 或高停止 score 认证为本请求答案正确。<!-- source-family:SF-2026-ARXIV-2601-19551 -->

[FROST 的有限图像分类实验](https://arxiv.org/html/2601.19551v1)用 stationary SSM 细化实现这条分支；正文脚注的“contractive”指插值权重 λ，不是 Banach 收缩定义，λ 小于 1 本身不能保证任意非线性变换 A 收缩，几何 proxy 也不认证所有 backbone 的 self-similarity。相同 halting 训练在对照结构上曾 collapse，作者才以全 depth 报告其成本，这不是相同可运行 stop 策略的净收益证明。额外 SSM/head、全 depth 训练和 quantile 状态都付费，还需验阈值漂移、表示 expressivity、accuracy 与真实执行时间。中间状态不可比较、分布漂移或费用不合算时，保留固定 depth、显式 loop/solver 与外部 task gate，不由局部吞吐或经验分位数授任意输入收敛或 foundation-LM 收益。

### Recursive Depth 的评价要区分执行次数与有效计算

共享 block 反复执行能以固定参数换更深计算，但“运行了 N 次”不等于获得 N 层独立变换。评价至少要分开 block applications、distinct computation、residual change、停止准则与 OOD 行为；简单截断深度只测少算几步，不能说明后续迭代是否继续产生新状态。<!-- source-family:SF-2026-ARXIV-2609-19934 -->

更细的 depth diagnostics 增加 instrumentation 与任务依赖，也可能把表示变化误当能力增量。作者递归模型结果不证明共享层普遍优于独立深层；residual 已停滞、OOD 误差上升或自适应停止不可校准时，应回退固定深度或显式层堆叠，并报告真实 latency/activation cost。

判断递归模型是否还在有效计算，也不能只看一个 Jacobian 谱范数。令 J 为当前状态的局部更新 Jacobian、d 为实际 update 的单位方向，`||Jd|| < 1` 可以与 `||J|| > 1` 共存：实际轨迹方向收缩，不代表所有扰动方向收缩；本步最扩张的输出方向若与下一步最扩张的输入方向错位，单步最坏范数也不是实际多步增长的精确乘积。它们是不同稳定性诊断，均不拥有任务正确性或停止权限。首次任务完成、状态更新停滞与允许停止需要分别记录，不能把小 latent motion 当作答案已正确。

[递归模型的有限完成诊断](https://arxiv.org/html/2609.26487v1)以已知 exact answer 的首次命中作离线对齐；累计曾正确可包含后来暂时失解的轨迹，不是终态正确率，更不是未知答案上的在线 stop sensor。相同模型延长至有限步数的 Sudoku 实验、少量 checkpoint 与扰动子集也不证明无限收敛或所有任务最终完成；attention 的受测扰动被吸收时，MLP 分支仍可保留放大。Jacobian、扰动与更长迭代新增计算和任务标注成本。诊断不可迁移、正确性不能独立核或串行预算超限时，应保留固定 depth、外部 task Gate 与明确最大迭代预算，而非自动把失败归为“再算就会好”。<!-- source-family:SF-2026-ARXIV-2609-26487 -->

递归深度的输出诊断还要区分 score 大小与答案比较。固定候选及终点 T、当前唯一 winner a 时，令 `g_b = s_(t,a) − s_(t,b) > 0`、`δ = s_T − s_t`、`u_b = δ_b − δ_a`；答案在终点严格保留当且仅当每个 `g_b − u_b > 0`。共同平移不改比较，`osc(δ)` 只约束最坏相对变化；再保留朝 winner 的有符号方向与每个 competitor 自己的 gap，可以拆开保守半径的三种 slack，而不能用最大 update 配最小 gap 宣称实际一定翻转。

这是一条 completed-trajectory 诊断，不是在线停止器：δ 读取未来终点，保留终点答案也不保证真值正确。Huginn/Ouro 的固定多选与 quarter-depth 对照不外推开放生成；配对的 prefix 检验中 quotient ranking 仍逊 mean centering，2.5% 目标也不成为有限样本硬保证。需要另核预测 future relative update、退出误差和真实执行成本；不可校准时保留固定深度/外部 task Gate。 [必要机制与反证](https://arxiv.org/html/2609.21383v1)。<!-- source-family:SF-2026-ARXIV-2609-21383 -->

## 执行深度与序列历史是不同的状态预算

参数复用还会减少不同层可存储的变换，因此增加循环不能被当作补足参数容量的唯一办法。一条受限分支为循环 block 另配每层与跨层共享的 learned key/value bank，以当前 activation 查询，再用输入相关 gate 将读出写回 residual；这些 bank 是训练时更新、推理时固定的 checkpoint 参数，不是保存当前请求 token 的 KV Cache，更不是第77章跨调用更新的 Agent Memory。作者约200M模型、14B FineWeb-Edu tokens 的参数与 forward-FLOP 对照中，循环及 bank 对 math BPB 有收益，却仍弱于更深 iso-FLOP 模型的 commonsense 表现；BPB 不是生成答案正确率，forward-FLOP 匹配也不证明真实训练或 Serving 时间相同。额外参数、bank 查询、gate 与串行循环都付费，gate 初值和任务会改变效果；需要更广的知识容量、吞吐或稳定性时，保留不同参数的深层 stack，不让 learned storage 冒充免费动态记忆。<!-- source-family:SF-2026-ARXIV-2603-08391 -->

前面的 recurrence 沿深度反复更新当前状态；压缩序列历史则改变每一步能读取什么信息，不能用增加循环次数代替历史可寻址性。本章保留这一 Layer 接口边界，显式历史、SSM 与 hybrid 的完整容量取舍由[第22章](./22-long-context.md)继续展开。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-24330:start -->
标准 softmax Attention 为每个 query 直接寻址 token-level KV memory，精确 recall 强，但状态和计算随序列增长；固定大小的 recurrent/SSM state 把历史压进有限状态，长度成本更稳定，却可能丢失 query 之后才显得重要的细节。两者之间可以加入 query-conditioned basis projection：历史先形成受控数量的 basis state，query 再决定如何读取这些基，而不是预先把全部历史压成与 query 无关的单一摘要。

这条分支以有限 basis、投影计算和训练复杂度换取比完整 KV 更小的状态，同时保留一定 query-specific addressing；basis 预算不足或查询落在未保留方向时，精确 recall 会失效。状态 owner 必须绑定 basis 构造、预算和更新规则，runtime 不能把不同版本的 basis cache 混用。长程 recall gate、复杂度或稳定性不过关时，应回退 softmax Attention 或经过验证的 hybrid Attention；现有证据只覆盖论文的结构、FineWeb-Edu 与附录 scaling 实验，不证明它在任意模型和检索任务上替代 KV memory。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-24330:end -->
<!-- source-family:SF-2026-ARXIV-2605-24330 -->

## Dropout、precision 与训练/推理差异

无论采用固定 stack、跨层路由还是递归执行，逻辑 Layer 都还要落实为实际算子。这里需要区分三件事：训练时怎样扰动更新、哪些计算真的被跳过，以及执行后端是否保留原模型语义。

训练时可能在 Attention weights、sub-layer outputs 或 residual branches 使用 dropout；推理时通常关闭。Mixed precision 会让 Norm、residual accumulation 与 softmax 的数值策略更重要。

若目标还包括降低训练执行量，随机置零必须进一步变成结构化的跳过：整层或整条 residual branch 被选中不执行，才可能省掉对应计算，先算完再乘零只改变训练扰动。按样本与按batch选择不同深度，也会改变可批处理程度；比较时应联合固定depth/time schedule、累计active FLOPs、residual缩放与优化器配方，而不能拿最大dropout率代替实际节省。局部期望幅度匹配不保证整网输出等价，少执行也可能损害优化或能力。训练得到的深度弹性若用于推理，直接early exit仍是有损分支，只有完整target验证后的提交才属于第48章的speculation保证；固定深度在稳定性、吞吐和证据不足时仍然成立。

章节公式描述逻辑语义，不代表每个算子都以相同 dtype 独立执行。Fused kernels 可以合并 Norm、projection、bias、activation 或 residual add，但需要保持 checkpoint 与数值容差内的模型语义。

### 更换执行后端仍须保留完整 Layer 算子合同

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20289:start -->
当 Transformer 被映射到脉冲执行时，Layer contract 不能只保留矩阵乘：Softmax、SiLU 与 RMSNorm 还要被
分解为可执行的 division、exponential 和 norm primitives，并显式记录有限 timestep、population 与分段近似
误差。这样获得 spike-native operator coverage，代价是新的数值范围、累积误差和硬件支持边界。论文在披露的
转换框架与模型上给出的精度、延迟结果不证明所有 neuromorphic target 的能耗或兼容性；误差预算或 operator
coverage 不满足时，应回退原精度算子或常规 Transformer backend。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20289:end -->

## Causal 不是 Mask 属性，而是 Block 不变量

数值与算子合同之外，下一章的生成模型还会给 Layer 加上信息可见性的约束。Layer 本身并不强制 causal；但一旦被用于 causal stack，这项约束就必须由整个 block 的行为共同满足。

Decoder-only 模型通常用 causal mask 阻止位置 `t` 的 Attention 读取未来 token。这个局部构造很重要，却不能单独
证明整个 sequence block 具有因果性：并行 scan、跨位置 normalization、fused kernel、cache reuse 或 hybrid
state update 都可能在 mask 之外泄漏 future information。更强、也更接近模型语义的不变量是 **prefix
invariance**：保持输入前缀不变，只替换它之后的 suffix，前缀中任一位置的中间表示都不应改变。

```text
x  = prefix + suffix_a
x' = prefix + suffix_b

for every t inside prefix:
  hidden_l(x, t) ~= hidden_l(x', t)
```

这使 correctness check 从“配置里是否有三角 mask”演进为两层合同：实现审查验证 mask、scan 与 kernel 路径，
行为审查用两次 forward pass 比较逐层 prefix states，并定位第一个违反不变量的 layer / operator。浮点非确定性
要求阈值、dtype、kernel、seed 和 batch identity 一起版本化；测试通过也只证明已覆盖的长度与 execution path，
不能替代更广的变形测试。

该审计在 sequence length 短于 chunk、window 或 kernel tile 时可能根本触发不了缺陷；只检查 final logits 又会
丢失定位能力。反过来，严格逐元素相等可能把正常数值抖动误判为信息泄漏。因此应先构造足以跨越实现边界的
suffix perturbation，再比较 layer-local state 与误差尺度，并为 production fused path 保留单独测试。静态 mask
inspection 在普通 attention-only block 中仍是便宜的第一道门；prefix invariance 是跨 attention、state-space 与
hybrid block 的系统级补充，不是用一个 benchmark 淘汰代码审查。

2026 年的一项研究在 8 个 checkpoints 的 192 个 injected-fault trials 中用该审计定位全部注入缺陷，并报告在
两个共享实现 lineage 的模型中发现真实缺陷。它支持“observable invariant 比 mask inspection 更完整”，但样本
规模和实现相关性不足以估计行业缺陷率，故这里只沉淀机制与边界，不外推 prevalence。

## 本章没有解决什么

Transformer Layer 本身没有规定：

- 是双向还是 causal Attention。
- 输入输出任务怎样组织。
- 是否使用 encoder、decoder 或 decoder-only。
- 生成时怎样缓存 K/V。
- 最终 token 怎样采样。

这些分别由[第18章 Decoder-only](./18-decoder-only.md)、[第19章 KV Cache](./19-kv-cache.md)与[第20章 Sampling](./20-sampling.md)接手。尤其是第18章：它要在本章的 shape 稳定 block 之上，规定信息可见范围、训练预测位置与 vocabulary 输出接口。Layer 是可堆叠计算单元，不是完整语言模型。

## 本章在知识树中的位置

```text
Positioned hidden states
-> Norm
-> Multi-Head Attention
-> Residual
-> Norm
-> MLP
-> Residual
-> repeat L layers
-> Decoder-only language model
```

本章将第14～16章的局部机制收束为 block，并为第18章讨论完整模型架构建立稳定入口。

## 自检问题

1. 为什么简单 `MLP(MHA(X))` 难以无限堆深？
2. Residual connection 为什么要求子层输出保持 `[B,T,d_model]`？
3. `dY/dX = I + dF/dX` 提供了什么梯度路径？
4. LayerNorm 沿哪个维度计算统计量？
5. Pre-Norm 与 Post-Norm 的公式顺序有何不同？
6. 为什么二者不能在 checkpoint 上任意互换？
7. Shape 流中哪些张量包含 head 维，哪些保持 residual stream？
8. MLP 的 `d_ff` 为什么不会改变 layer 输出 shape？
9. Layer 数 `L` 会怎样影响 KV Cache 与 Pipeline Parallel？
10. 为什么 Transformer Layer 还不是完整 Decoder-only 模型？
11. 为什么 Jacobian singular value 长期偏离 `1` 会让某些方向的梯度消失或爆炸？
12. Residual connection 为什么改善 gradient path，却不能保证任意深度都稳定？
13. 为什么 gradient clipping 和逐层 learning rate 不能修复已经消失的 backward signal？
14. 为什么 causal mask 的配置审查不能替代 prefix invariance 的行为审计？

## 小结

Transformer Layer 通过 residual stream 把复杂计算组织成 shape 稳定的增量更新。Attention 混合上下文，MLP 变换逐位置 features，Residual 保留信息和梯度短路，Normalization 控制子层输入尺度。

Pre-Norm 与 Post-Norm 的差异不只是代码顺序，而是梯度路径设计。理解完整 shape 流后，模型深度、activation、KV Cache 与分布式切层之间的联系也变得可见。

改变跨层状态的路由、共享参数的执行次数或剪去部分层，都会建立新的状态与验证合同，不能从 shape 不变推出语义不变。带着这条边界进入第18章，接下来要回答的是：怎样让这些计算单元服务于一个完整的因果语言建模任务。

## Review notes

- `SF-2025-ARXIV-2510-22026` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22026v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。完整新论点为径向/角向及token依赖速度，不重复既有Jacobian或随机共享噪声；不照录受限速率为通用优化定理。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

- `SF-2026-ARXIV-2606-19491` — Jun20补Jun19；writer首次exact-v1§2–5/A1.1–2/A1.6必要，2+2+2=6，仅Prop2独立有效代数与centered/Gram诊断差额深入，actualCh17 Norm完整两肩/Ch16–18交接已读。保非零γ/β/epsilon/人口与精度地板；不采中心Schur ratio0/0→1/训练更深核、无条件residual界、Fisher/rate或功能缺陷，中心H与重开留本日A15。未核artifact/复现；完整PRE已过，SAVE后selfread/actualPOST只本日实际层，不以本注预签。

- `SF-2026-ARXIV-2606-18246` — Daily06-18补Jun17，2+2+2=6，作者首次必要完整v1§2–3/4.4T4/5/AppA；仅active坐标/最近恢复与bulk参数、cache及完整执行成本分账。保round/endpoint/MoEactive差、任务/投影反退、global残差非均宽内存、fit非墙钟及全费；未采4.1–4.3因果解释/完整scaling定律，未核代码/复现。root唯一REVIEW§47整体PRE通过，按批准稿实际保存，作者完整自读；actualPOST仅后到唯一非writer记录，不预签。

- `SF-2025-ARXIV-2510-12229` — Herschel，Daily2025-10-16补Oct15；消费Cicero R14 exact-v1 §3.1–3.3/Alg1/4.1–4.3首次必要，2+1+2=5，仅跨checkpoint activation拼接的干预身份差额。actual Ch17非lookup；保局部intentionality/80scenario与283重复输出、状态失配和全费，不授唯一bias定位/全部公平或能力恢复。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

本人注：`SF-2025-ARXIV-2510-14095` — Schrodinger，Daily2025-10-18补Oct17；exact-v1 §4.1/Eq2–4、4.2/§5机制分责必要，2+2+2=6，离散因子state投回递归接口深入。保modular arithmetic/两层16head256hidden/N≤32训练/已知中间标签与全费，不采全部细电路因果/开放语义或免费外推。未核完整机制附件/代码/复现；实际层见canonical。

本人注：`SF-2025-ARXIV-2510-14614` — Schrodinger，Daily2025-10-18补Oct17；exact-v1 §4–6.4/Eq2/T1–2，3+2+2=7。仅MLP读首attention/保当前MHA residual而改变依赖的结构；FAL+另账，保任务反退/需重训及真实执行全费，不授checkpoint等价或通用通信收益。未核实现/全附录或复现；PRE/SAVE/自读/solePOST以本日canonical为准。

- `SF-2026-ARXIV-2606-15085` — Daily2026-06-17补Jun16；exact-v1 §2.3–4.9/Eq5–15/Lemma1/T2–9/6必要，原2+1+2=5，仅同K正交流/固定总s换序与真实计算budget分责差额深入。保R非exp同物、任意正交control、MLP破群、local长度/recall反侧和单seed/no-pos人口与全费，不授全网Jacobian/causalAR/质量单调或省算。未核外部physics/代码/像素/复现，root§110有限必要/actualowner/完整三件PRE通过，作者已真实SAVE并完整自读，root§111唯一实际完整POST通过，窄位生效释放，不预DAY。

- `SF-2026-ARXIV-2610-32492`，Daily2026-10-27；exact-v1 §2.1–2.3、4.1.2/4.1.3采用域文字、4.2.2–4.2.4、E5/F1核心监督/预算对照与直接反侧首次必要；R163 2+2+2=6，仅finite-prefix预算菜单的同步训练/状态与后训练teacher-budget交接深入。保Loopie继承非本篇首创、每层连续两pass/固定request路径、passbias非独立learnedrouter/独立KV、80Btokenmatch与FLOPmatch不同、baseline联合路径与未独立budgetmismatch消融、单run及checkpoint选择/样本bootstrap非训练重复；task最优预算不单调、RLMOPD负cliplogratio/只distill、最多五次perbudget更新/step、teacher及全训练费、F1H800B1/8EOS忽略128output/离线p95非SLO。未读全§3/所有机制probe/逐shape/完整附录表/图像素/代码，不授任意深度或同预算净速度；PRE/SAVE/selfread/solePOST仅后到真实层。

- `SF-2025-ARXIV-2510-04309` — Arendt，Daily2025-10-08补Oct07；原7，直接采用root R460唯一exact-v1 S2.2/S3–6/T1–2/B2–5/B7.1必要，不第二Methods。仅深度时钟/双人口均值误差、P/I/D与sequential校准身份；保真实H特征式符号、PI例Abar−.5/Kp1/Ki.1/w0得谱半径1.04772256且打印条件满足，不采ISS/小Kd通用继承。B6/B7.2截断未冒全读，线性化/时变余项未补；MMLU/PPL与内容CLIP反退、T2提高ASR非安全增强、全校准/干预/搜索费保。未核C全表/图像素/代码或复现，不执行攻击。PRE/SAVE/fullselfread/solePOST仅本日canonical真实后到层，不以本注预签。

- `SF-2025-ARXIV-2510-06035` — Cicero，Daily2025-10-09补Oct08BJT；[UniNAS exact-v1](https://arxiv.org/html/2510.06035v1)A93首必要II–IV/Alg1/TableI/III–VI及VI，2+1+2=5，primitive-DAG/shape与proxy提名差额深入。保有限stage/节点库、pairedbranch删除/随机walk非全覆盖、ConvRed4打印costshape、真实FLOPs/traffic与COCO FPS反侧及完整搜索训练费，不采全架构通达/LLM结果/免费NAS或净速。未核原图像素/pip实现或训练复现，PRE/SAVE/selfread/solePOST仅本日canonical，不以本注预签。

- `SF-2025-ARXIV-2510-03638` — Arendt，Daily2025-10-08补Oct07；原2+2+3=7，直接采用root R72 exact-v1 S1/S2/AppA/B完整必要与已补足A1节点。两个200/exit28 partial不冒全文/AppF，只regular operator函数空间存在与点态/统一有限budget/残差消费者；保mu(x)非uniform、G=(1−x)y+1固定T无界反例、learnability/全局鲁棒/数值与训练求解全费，不采empirical净速/图像排名因果或科学应用。未核像素/代码/复现，root R77实际owner/整体PRE已成并直接窄授，作者A79真实SAVE/fullselfread后root R78唯一actualPOST通过，指定窄位即时释放；仅同步既成末态，不预DAY。

- `SF-2025-ARXIV-2510-03470` — Arendt，Daily2025-10-08补Oct07；原2+1+3=6，直接采用root R33互斥首次exact-v1 §3–5/A–C理论必要，不第二Methods。只有限深/足够光滑的低阶导数交互与尺度分责；保flat C∞/零分支反例、级数与深度一致界缺口、重参数化/印式反侧、CIFAR width/λ/BN与全部搜索训练费，不授infinite exact、幅度必爆、训练后容量或普遍Transformer配方。未核代码/曲线像素或复现；root R33必要/R36 actualowner与原稿整体PRE窄授已成，作者真实SAVE/fullselfread后root R39唯一actualPOST通过，指定窄位释放；仅同步既成末态，不预DAY。

- `SF-2025-ARXIV-2510-00379`：Daily2025-10-03补Oct02；[Composer exact-v1](https://arxiv.org/html/2510.00379v1#S3)，2+1+3=6/模块比例排列搜索具体gap深入。直接采用root R69唯一首次必要，只proxy→聚合→扩展→目标重训实测；保mode新组合/ceil身份、D2 GQA漏dim/D3 token单位、C8排列冲突、任务反侧与randomweights timing非已训Pareto及全搜索/重训回归费。不授通用1:2/搜索最优/无损重排/Serving净速，未核全E图表/代码或复现，作者不第二Methods。R35原分/日门复用；root R73 actualowner/整体PRE与本次窄授通过，R69必要直接采用，真实SAVE/fullselfread后root R76唯一actualPOST通过，指定窄位释放；本尾仅行政同步，不预DAY。

- `SF-2025-ARXIV-2510-00345`：Daily2025-10-03补Oct02；[Cutting the Skip exact-v1](https://arxiv.org/html/2510.00345v1#S5)，2+1+3=6/无identity训练分支gap深入。仅V/O scaled-orthogonal与mimetic Q/K初始化/optimizer联合验收；保重复token反例、chain-factor/全网拼接假设与扰动条件未闭、AdamW/ADE/少层反退和完整重训/搜索费。不采全理论、LLM无skip/通用净速度；未核图像素/代码或复现。R21原分/日门复用；root R47必要/actualowner/整体PRE与本次窄授通过，已真实SAVE/fullselfread；root R49本项唯一实际POST通过，指定窄位释放。仅行政同步既成，不预DAY。

- `SF-2025-ARXIV-2509-22463` — Aristotle，Daily2025-09-30补Sep29BJT；[exact-v1](https://arxiv.org/html/2509.22463v1)§2–4/E1–15/Alg1/T1–3/6/Limit/A–F/T4–9必要作者102→Einstein95实际采用，原2+2+2=6。只有限共享修正/历史混合与离线cosine删迭代＋fullteacher再训两consumer；保精确隐式解1/3与Picard−1/3/−5发散反例、Alg1状态/调用桥不闭、testPPL择r/非单调、proxy非任务真值、1.3B保持97.61%/E仍慢vanilla、dtype/LR/warmup原冲突和全部预训/teacher/额外5–30B蒸馏/KV费。未核全图像素/代码/复现，不授精确解/高阶/一般99.4%或75%全费省。Einstein101已actual唯一owner/原三项整体PRE，并依root本轮委托明确fresh新窄授；正文只12466完整fixedpoint段及独立binding后/球面25646完整段前，本人注只trueH2后/现场18993完整首注前，护全部他文他态。作者109按原稿真实保存并完整自读；Einstein103唯一非writer actualPOST已通过，本指定正文/本人注窄位生效且即时释放。仅同步既成态，不第三研究/POST，不授DAY。

- `SF-2025-ARXIV-2509-18993` — Singer，Daily2025-09-25补Sep24；exact-v1 §3–5/Eq3–9/Alg1/T2–4、B锚点/重算、D2必要配置/反侧、E2/T17/F必要，2+2+2=6。root唯一首次必要→本人A22唯一另一角色实际原域采用闭合，reader仅角色复用；只采完整跨层投影历史+低秩delta及重算依赖的有限分支，不授普遍低秩/无损、任意beta/precision可逆或净训练/serving速度。保sign0/小系数、B锚点与遍历文字/E2方向冲突、规模/早步反退、训练tokens及PP算术冲突和全部调参/保存/重算/通信费，未核C普遍理论/实现/像素/复现。Sartre R19完整原三项纯PRE通过，root本轮fresh独立新窄授；A27已按原稿实际保存/完整自读，Sartre R21唯一非writer actualPOST通过，新I3生效且本指定窄位释放；仅行政同步既成结果，不第三POST或授日级。

- `SF-2026-ARXIV-2606-05014` — Daily2026-06-05补Jun04，[Depth-Attention exact-v1](https://arxiv.org/html/2606.05014v1) §3–5/A/B必要域，2+1+2=5。只采用same-token当前/前层K读取与递归mixed V原槽接口，保非raw-KV等价、PP/activation费用、FP16有限规模及PyTorch实测非零开销；B6一次warmup/两测量run不等运行CI或独立训练重复。reader R17必要Source/actualowner/PRE通过，root明确新授两段，当前层key补全已真实采用；作者完整新增/直接两侧/本人注已自读，reader R19唯一非writer actualPOST已通过，整合生效且窄位释放，未实现/复现fused kernel，不签DAY。

- `SF-2026-ARXIV-2606-02559`：exact-v1 §3–5/T1–7/D必要域；2+1+2=5，按实际压缩粒度/可拟合性差额深入。保局部基线反退、mask/replacement分验、bypass参数/MAC及预算差异，不采无损或普遍提速，未核代码或复现。独立必要Source/逐字PRE通过，root实际保存；非writer `jun03_next_reader` 已真实读取完整新增、完整直接两侧与本人注，唯一actualPOST通过（本日SUP_NEXT_REVIEW_20261024，末项R20）；本句只同步既成结果，不授完整DAY。

- `SF-2026-ARXIV-2610-25998` — Daily2026-10-21窗Oct20；exact-v1必要proof域见RESUME_AGENT B4，2+2+2=6。保预载cache/构造位置/有限arithmetic/层与容量区分、非自然checkpoint/免费计算，全部费用近正文；未核代码/复现。core B-R7必要Source/actualowner/完整PRE原样通过，root既授padding-loop2605-30523完整段后/universal2605-31423前原单段/本人注；作者已真实保存并完整自读新增/完整直接两侧及本人注，core B-R15唯一非writer actualPOST已通过，窄位生效释放；仅行政同步既成事实，不第三核。未核代码/复现，不授DAY。

- `SF-2026-ARXIV-2610-26030` — Daily2026-10-21窗Oct20；exact-v1 §3–6.3/A2/C1，2+1+2=5。保forward/backward信用与N/D/T配置、拟合q>2p限定/反侧和全部费用；currentabs v2无具体重要cue，采用v1公告，未核代码/复现。core B-R3必要Source/actualowner/完整PRE原样通过，root既授HRM完整段后/Spiral前原单段/本人注；作者已真实保存并完整自读新增/完整直接两侧及本人注，core B-R6唯一非writer actualPOST已通过，窄位生效释放；仅行政同步既成事实，不第三核。未核代码/复现，不授DAY。

- `SF-2026-ARXIV-2610-25004` — Daily2026-10-21，exact-v1 §3.1–3.3/4.1/4.7/4.10/Limitations，5分；local loop/write接口、近似KV与全费分账；R74必要Source/owner/PRE通过，无code/复现，实际POST另见本日REVIEW。

- `SF-2026-ARXIV-2610-27628` — Daily2026-10-22，[PAR exact-v1](https://arxiv.org/html/2610.27628v1)§3–6与AppA必要域，2+1+2=5。只进度中间监督/first-pass尺度与初触发答案保存接口，保graph-reachability反侧、无step label仍需teacher/final监督、额外hold崩溃、外部RLT非同compute及确认费用；不授普遍长度泛化或加速。作者E16/reader R61必要Source/具体owner/PRE通过，actualPOST另见本日REVIEW；未核实现或复现。

- `SF-2026-ARXIV-2610-28489` — Daily2026-10-22，[AsymLoop exact-v1](https://arxiv.org/html/2610.28489v1)§3–5与A/C/D/E必要域，2+1+2=5。采用固定Global/逐轮Local、共同softmax与训练读取接口；保ALRS联合、额外FLOPs、135M更慢及无decode/SLO/任意loop稳定证明。作者E7/reader R45必要Source/具体owner/PRE通过，实际POST另见本日REVIEW；未核实现或复现。

- `SF-2026-ARXIV-2605-14047` — Daily05-16补May15；exactv1§2–4/Eq1–4/T1–2/F4，v2只GP/FLOP/knee/重跑受影响域，currentv3只轻查扩ViT-L/硬件动机，不提前采用窗外结果。2+1+2=5/逐层scalarfit→继承affine→再对齐gap深入。保软罚非全域界、非LN恒等、node非FLOP/跨层与单架构局限、同训LN/affine-only反侧及搜索/回训全费；无实际kernel runtime/实现复现。root R13必要Source/actual owner/A23逐字PRE已独核授本单段与本人注；真实新增、完整两侧与本人注经root R15非writer POST通过，计本日第6整合、窄位释放，不授日级完成。

- `SF-2026-ARXIV-2610-22075` — Daily2026-10-17窗10-16；[Recurrent Retrofit exact-v1](https://arxiv.org/html/2610.22075v1) §3–6/AppA.1，1+2+2=5。仅预训练跨模态恢复路径与per-pass KV分责；保default2.55×KV、训练外depth崩溃、sampled不等scaling及全部恢复费用。root必要Source/actual owner最小PRE独核后授本单段及本人注；作者已保存并顺读，live1017_org_a已实际新正文、完整直接两侧及本注非writer POST通过（ORG_A十二项POST），作者仅行政同步既成事实，不授DAY。未核代码/复现。

- `SF-2026-ARXIV-2605-02108`、`SF-2026-ARXIV-2605-02111` — Daily2026-05-06补May05；[exact-v1](https://arxiv.org/html/2605.02108v1)、[exact-v1](https://arxiv.org/html/2605.02111v1)，2+1+2=5、2+1+2=5。必要方法/条件、直接对照与反侧见本日SUP A6；只采A7指定受限命题，不授普遍能力/稳定/性能保证，全部测量与准备费用保留。root实际必要Source/具体owner及逐字PRE通过，授本单段及本人注窄位；作者已保存并实际self-read；root非writer实际完整正文/两侧/本人注POST通过，指定窄lease释放；仅同步既成事实，不授DAY；未核代码、全部附件或复现。

- `SF-2026-ARXIV-2604-26898` — Daily2026-05-01补Apr30自然日；[exact-v1 PDF](https://arxiv.org/pdf/2604.26898v1)p2–10必要架构/Thm1.1/Prop1.2/Cor1.3/Assumptions1–2/Thm1.4与Tanh反侧。2+1+3=6，固定Attention与iid初始化MLP的不同缩放/共享噪声来源差额深入；有限T、全极限交换更强光滑性、nonodd/负能量率及不授训练后/causal/任务保证近正文。root独立必要Source、实际owner完整邻接与逐字PRE通过并授本段/本人注窄lease；作者已写并实际读回，root非writer已实际独读正文、完整上下邻接与本人注，POST通过，窄lease释放。未全审证明、artifact或复现，不授DAY。

- `SF-2026-ARXIV-2604-01978` — Daily `2026-04-04`补Apr3自然日，2+1+3=6；作者/supp_apr04_reader实际v1 §2.1–2.3必要main results与Ch17联合shape链/Ch16–18交接PRE通过，root两body/本人注窄锁。仅random-init attention mean/commonnoise与jointscale，overlap非pathwise同步/slowtransient全时间密度条件近文，不授MLP扩展、trained decoder/fullTransformer、全部theorem率或一般collapse保证。作者实际写后完整局部/本人注读回，supp_apr04_reader实际非writer完整局部及本人注POST通过，作者同步状态实读，窄锁释放；未审全proof/代码或复现，不授DAY。

- `SF-2026-ARXIV-2603-07482` — Daily `2026-03-11`补查；[精确v1](https://arxiv.org/html/2603.07482v1) §2/5.2/5.4/8。作者与review_20260311必要Evidence通过，root实际机制/反侧与owner/Ch16/18邻接比较后窄写两段；frozen指跨层activation不是参数，局部干预仍有损伤、BPB代价及小规模限制近文，非全独立性定理。非写入者supplement_20260311已实际顺读新增正文、完整局部邻接及本注并回对必要原证，POST通过，不授DAY；未核artifact/复现。
- `SF-2026-ARXIV-2603-08391` — Daily `2026-03-11`补查；[精确v1](https://arxiv.org/html/2603.08391v1) §2、§3.1–3.3/Table1、§4。作者与review_20260311必要Evidence通过，root实际方法/参数及iso-FLOP反侧和owner/Ch16/18/77交接比较后窄写一段；static learned memory与KV/Agent状态分责，math BPB与commonsense反侧/成本保留，不授完整推理accuracy或真实Serving加速。非写入者supplement_20260311已实际顺读新增正文、完整局部邻接及本注并回对必要原证，POST通过，不授DAY；未核artifact/复现。

- `SF-2026-ARXIV-2602-08220` — Daily `2026-02-11`增量；[exact-v1](https://arxiv.org/html/2602.08220v1) §3.1–3.6/4.1–4.4/5.1–5.3。2+2+2=6，二维 causal mask、逐 token reach/exit mixture 与训练 truth privilege 的具体差额深入；O(K)仅训练 critical steps，不授原依赖精确保持、在线真值停止或部署 SLO。410M/1.4B、26B Pile/50ksteps、estimated FLOPs 与局部任务/停止消融反侧近正文，生产硬件/precision/batch/concurrency/SLO 未披露；未核实现或复现。root 必要原证与 actual owner/邻接 PRE 通过并授窄锁；作者实际正文/完整邻接顺读，root 非作者实际新正文/完整局部邻接及自身末注 POST 通过，窄锁释放；非日级验收。

- `SF-2026-ARXIV-2601-19551` — Daily `2026-01-29` 增量；[scale-consistent FROST exact-v1](https://arxiv.org/html/2601.19551v1) §3.1–3.3/Definition3.2脚注、§4.1–4.4/§5/§6.1–6.6及AppendixD受影响 collapse 对照。2+1+2=5，中间 depth 任务次序→history quantile 停止接口差额深入；不采用 λ<1 认证非线性 A/Banach 收缩，finite classification/proxy 与 collapsed full-depth 对照边界近正文。root 实际必要 Source/owner PRE 通过并授两段/自身末注窄锁；作者已实际顺读正文与完整邻接，root 非作者 actual POST 已通过（实际顺读上述两段、完整邻接及自身末注）。不是另篇 attention FROST2601.19001，未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-15503` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15503v1) Lemmas1/2/6、Theorem8、§3/5。3+1+3=7，条件理论深入；negativeEuler/tiedV/stepnorm/compactdomain下query非扩张、context另界、scalar交集限制近正文；不授任意训练Transformer安全或成本保证。root必要源/actualowner PRE通过；实际正文、邻接及末注root独立POST通过；未运行实现或复现实验。

- `SF-2026-ARXIV-2602-10408` — Daily `2026-02-13`；[SF-2026-ARXIV-2602-10408 exact-v1](https://arxiv.org/html/2602.10408v1) §3–5/§7；warmup→frozen scale与finalNorm分责、质量损伤和无KV微测边界。2+2+2=6，受影响深入；root必要原源与actual owner PRE通过授窄锁；实际正文/邻接已由root非作者POST通过，未授日级。未运行代码/复现。

- `SF-2026-ARXIV-2601-08131` — Daily 2026-01-15；[ExoFormer exact-v1](https://arxiv.org/html/2601.08131v1) §3.4–3.6/Eqs7–12、§4.1–4.4/Table1–2与Limitations。2+2+2=6，外置共享attention anchor与identity residual职责差额深入；不授identity导数I、offloading因果或longcontext收益。额外4projection、450M10B/H100BF16/seq2048、localcounter保留；未复现。root必要源/owner写前通过，root已实际核正文、前后交接及末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-00417` — Daily 2026-01-06；[Deep Delta Learning exact-v1](https://arxiv.org/html/2601.00417v1) §2.1–2.2/Eqs3–7、§3.1–3.3、§4.1–4.2。只采用矩阵状态的 rank-one carry/write 与 unit/epsilon→0/fixed-input 谱边界，不推 input-dependent full Jacobian、任意训练稳定或实测收益；§5 是 Related Work，无实验节。root 必要原源→实际 owner 写前及实际正文/相邻衔接非作者写后复核通过；未复现。

- `SF-2026-ARXIV-2512-24880`（mHC；Status: Experimental）：[exact-v1](https://arxiv.org/html/2512.24880v1) Intro Eqs3–4、§3.2、§4.1–4.3、§5.1–5.4及Appendix A.1；Daily 2026-01-02。采用read/carry/write分工、理想双随机carry的均值/均匀方向与乘积封闭，以及有限Sinkhorn不能授权精确守恒的边界，不采用“恢复任意方向identity”或整网梯度保证。20轮近似、27B选定序列tokens平均后的composite Amax row/column-sum gain约1.6不等于谱范数/任意输入界；3B/9B/27B MoE、n=4、4096上下文的作者训练结果不外推全架构，硬件及seed重复Not Disclosed，不采用6.7%为普遍overhead。root必要证据审阅及jan01_v3非作者写前、实际正文邻接与证据注写后复核通过；未复现实验。

- `SF-2026-ARXIV-2604-21999`：[exact-v1](https://arxiv.org/html/2604.21999v1) §2–5、§8；Daily 2026-04-27。仅吸收共享单块 ACT 停止先验会锁住深路径训练、须与 scratch slots 和执行预算联校的受限分支；初始偏置、T 上限、长轮次 dilution 与 Sudoku-only/3-seed 条件保留。作者已完成必要源与相邻 owner 对读，root 独立 source→owner 及实际正文/邻接写后复核通过；未复现实验。

- `SF-2026-ARXIV-2604-21254`：[exact-v1](https://arxiv.org/html/2604.21254v1) §2–4.3；Daily 2026-04-24。仅吸收共享 block 轮次边界混合与逐子层 mixer 的频率分账；diagonal carry 非双随机、非全参数共享、量化跨轮校准和 depth/compute 不匹配的反证保留。root 已完成必要源→当前 owner 写前及实际正文/相邻衔接的非作者写后复核，通过；未复现实验。

- `SF-2026-ARXIV-2604-11890`：[exact-v1](https://arxiv.org/html/2604.11890v1) §2.1–2.4、§3.2–3.3、§4及最终读出因素，支持无归一化饱和函数的条件性初始化传播分支；不提供 causal LM、全部 Jacobian 奇异值或完整训练质量保证。本轮作者必要证据审阅完成，等待非作者写后复核。

- [Layer dropout v1](https://arxiv.org/html/2609.05275v1)：采用§3–11的结构mask、实际跳过、schedule/optimizer共同校准及推理分支边界。实验基于Celerity/CS3，不外推GPU加速；部分正文与表格对优劣的概述不一致，8.2B缺dense对照，不采用普遍质量提升、最优dropout率或无损early exit主张。

- oHC（Status: Experimental）：[exact-v1 §3–5、Appendix9–11](https://arxiv.org/html/2609.02672v1)区分mixer上下奇异值界、总范数与均值—差异交换。单一3.9B-A0.4B配方及73B内部语料不证明普遍质量；Eq12的epsilon使理想精确正交与数值实现不同，初始化bit-exact仅按Appendix10的fp32舍入条件。

- `SF-2026-ARXIV-2602-07306`（Parallel Track Transformer；Status: Experimental）：exact-v1 的 §2
  定义 independent tracks 与 periodic fusion，§3.3 报告作者模型和 serving stacks 下的 evaluation，§4 不证明
  跨模型质量等价、任意互连拓扑的普遍加速或对标准 Tensor Parallel 的全面替代。
  https://arxiv.org/html/2602.07306v1

本章聚焦标准可堆叠 block，不扩展为 Transformer 变体目录。后续 Review 应以具体架构核验 Norm 类型、放置、bias、activation 和 residual 形式；这些都属于 checkpoint 语义，而非 runtime 可随意切换的优化。

Primary-source 校验入口：

- Kaiming He et al., "Deep Residual Learning for Image Recognition", 2015: https://arxiv.org/abs/1512.03385
- Jimmy Lei Ba, Jamie Ryan Kiros, Geoffrey E. Hinton, "Layer Normalization", 2016: https://arxiv.org/abs/1607.06450
- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
- Ruibin Xiong et al., "On Layer Normalization in the Transformer Architecture", 2020: https://arxiv.org/abs/2002.04745
- Xavier Glorot, Yoshua Bengio, "Understanding the difficulty of training deep feedforward neural networks", 2010:
  https://proceedings.mlr.press/v9/glorot10a.html
- Kaiming He et al., "Delving Deep into Rectifiers", 2015: https://arxiv.org/abs/1502.01852
- Razvan Pascanu, Tomas Mikolov, Yoshua Bengio, "On the difficulty of training Recurrent Neural Networks", 2013:
  https://arxiv.org/abs/1211.5063
- Hongyu Wang et al., "DeepNet: Scaling Transformers to 1,000 Layers", 2022: https://arxiv.org/abs/2203.00555
- Chen Chen, Lai Wei, "Post-LayerNorm Is Back: Stable, ExpressivE, and Deep", arXiv v2, 2026: https://arxiv.org/abs/2601.19895
- Attention Residuals（Status: Experimental；depth-history aggregation 与 block-state trade-off）:
  https://arxiv.org/abs/2603.15031
- Mixture-of-Depths Attention（Status: Experimental；bounded depth slots）:
  https://arxiv.org/abs/2603.15619
- Thinking Deeper, Not Longer（Status: Experimental；parameter depth 与 execution depth 分离）:
  https://arxiv.org/abs/2603.21676
- HRM-Text（双时间尺度 recurrence；Status: Experimental）:
  https://arxiv.org/abs/2605.20613
- Post-Norm under Curriculum Depth Growing（No Change；受限九层 distillation curriculum 证据）:
  https://arxiv.org/abs/2608.13156
- `SF-2026-PREFIX-INVARIANCE`，The Mask Is Not the Model（Status: Experimental；两次 forward-pass
  prefix invariance audit 在 8 个 checkpoints、192 个 injected-fault trials 中定位全部注入缺陷，并报告两个共享
  lineage 的实现缺陷；不能外推为行业缺陷率，也不能替代跨长度、dtype、kernel 与 distributed path 的覆盖）:
  https://arxiv.org/abs/2608.22876v1
- `SF-2026-ARXIV-2609-00051`，From Detection to Refusal（Status: Experimental；minimal-pair localization、
  matched random ablation、双向 activation patching 与 adaptive re-attack 共同支持受限 circuit-edit evidence
  chain；六个 4B--8B instruction models 的链路强度和 utility/over-refusal 代价不一致，不构成生产安全保证）:
  https://arxiv.org/html/2609.00051v1

<!-- daily-books-trace:SF-2026-ARXIV-2607-25915:start -->
- `SF-2026-ARXIV-2607-25915` — Daily `2026-07-29`；primary `arXiv:2607.25915v1`；正文锚点“Recurrence 可以只占据 Decoder 的局部层段”。
  证据限作者的局部 recurrent decoder 与 structured-reasoning evaluation，不证明 latent steps 等价于正确推理或收益随深度单调。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25915:end -->

- `SF-2026-ARXIV-2602-17993` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.17993v1) §3.2–3.4/Eq4/7及§4.2–4.5/Table2/3。2+1+2=5，内部跨token高→低投影旁路具体缺口深入；分组只改变downward依赖，仍保causal attention组内读取。单A10080G训练时间、g/α交互退步、baseline rank140对120与λ=.1 soft-token控制不授普遍表达力或无推理成本；projection/state/prefill费用近正文。root必要原源/actual owner PRE通过并授一段/自身末注窄锁；作者实际正文/完整邻接及自身末注顺读、限定diff-check通过，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2601-06793` — Daily `2026-01-14`增量；[CliffordNet exact-v1](https://arxiv.org/html/2601.06793v1) §3/Algorithm1、§4/Tables1–4、§5，2+1+2=5，局部bilinear mixer责任差额必要深入；只采用detail/context两路、shift dot/wedge与projection/gate/residual共存分支，dense成本/CIFAR-only/DropPath及capacity不匹配消融、FFN及时间反侧近正文。O(ND|S|)仅逐元素阶段，不授整网线性、完整Clifford几何或LLM/global attention替代。root必要原证/actual owner完整邻接PRE通过并授一段窄锁；作者实际正文/完整局部邻接及本末注已顺读，root非作者实际169–216完整邻接、新正文184及note790–800 POST通过，窄锁释放。未核artifact执行/复现，非DAY。

- `SF-2026-ARXIV-2602-08332` — Daily `2026-02-11`补查；[exact-v1](https://arxiv.org/html/2602.08332v1) §3/4、A.1–3/Alg1/A.5.3，2+2+2=6。auxiliary自然语言压为固定state后加原input位置，与连续新增位置及内部高低投影并存；gold-state训练并行与线上chunk等待分开。不授随机采样exact、CoT等质量更快或完整制备成本，GSM42.22<60.50/late-query反侧、A100 batch1 L128训练分母与教师对齐费用保留。root实际必要Source/owner邻接与逐字PRE通过并授本两段及自身末注窄锁；作者已实际顺读正文/完整局部，root非作者实际529–552完整邻接、新537/539及自身末注POST通过，窄锁释放。未核artifact/复现，不授DAY。

- `SF-2026-ARXIV-2602-09870` — Daily `2026-02-12`补遗漏；[exact-v1](https://arxiv.org/html/2602.09870v1)。本日具名必要方法、关键评价与直接反侧由root独立Source限定通过，actual owner/局部邻接及逐字拟文PRE通过后授窄锁；作者已写最小差额，review_20260214非作者实际新正文、完整局部邻接及本人末注POST通过，窄锁释放，不授DAY。原件与配置/中心争议边界见本日同名前缀review笔记；未核artifact或复现。

- `SF-2026-ARXIV-2602-08864` — Daily `2026-02-11`补查；[ANIRA exact-v1](https://arxiv.org/html/2602.08864v1) §3–6与必要A.2/A.4–5/A.8。2+1+2=5，early structural 信息与 online 执行状态、离散退出冻结KV语义深入；median/mode默认口径冲突隔离，correct-only不同人口/expected depth与实际执行区别保留。GSM更难切片未多分深度、online质量反退，不授统一Pareto、算法泛化或depth比完整加速。root 实际必要Source与Ch17具体owner PRE通过，先前共享锁释放后授本段/自身末注窄锁；作者已写并顺读完整邻接，root非写入者实际551–578/新563完整邻接及826末注POST通过，Ch17窄锁释放。未核artifact/复现，不授DAY。

- `SF-2026-ARXIV-2602-11698` — Daily `2026-02-14`补查；[Spiral exact-v1](https://arxiv.org/html/2602.11698v1) §2–5，因果chunk pool及g−1 shift、overlap另影响质量/覆盖；Pythia160M–1.4B/Pile250B/4096的prefill FLOPs不等wall-clock，baseline同受overlap益处，不授全长窗无损。2+2+2=6，实际owner差额受影响深入。root/reviewer必要Source及actual owner/完整邻接与逐字拟文PRE通过，root授两段+本末注窄锁；作者已写并顺读完整邻接，review_20260214已实际独核新正文、完整邻接及本末注，非作者actual POST通过，root释放窄锁，不授DAY。未核artifact/复现。 本轮补查事件的首次公开日期未证，必要Source/PRE/实际POST研究仍有效，但不计本日已确认新增成果；归属只按[本日日报§5](../../papers/2026/02/14/README.md#5-缺口与下一步)的57日期请求定点重开，不撤正文或补造公开日。

- `SF-2026-ARXIV-2603-06492` — [2026-03-10补查](../../papers/2026/03/10/README.md)，[NOBLE exact-v1](https://arxiv.org/html/2603.06492v1) §3.1–3.4、§4.1.1/4.2.1/activation ablation与§6；Experimental。正文仅承载从预训练保留的非线性低秩projection、不可线性merge及训练/部署成本分离；不采cosine梯度、频率或泛化保证，不将step speedup当wallclock/服务收益。必要原证与Ch16/17/18、Ch30差额已读；supplement_20260310非写入者实际正文/完整局部邻接及末注POST通过，日级补查验收以日报为准，未执行artifact或复现。

- `SF-2026-ARXIV-2603-07461` — Daily `2026-03-11`补查；[DualStream exact-v1](https://arxiv.org/html/2603.07461v1) 方法、Table1/2/4/5与限制（本日 SUP_CORE_07461.txt 106–237、270–342、359–376），2+1+2=5；确认两流读写规则与两种不嵌套的受限投影类差额后定点深入。Dense Q/K路由、固定activation非固定训练参数、小型语料和Token-Factor/FTS结果人口边界近正文，不授语义隔离或普遍表达力阶梯。review_mar11_continue实际必要Source及Ch17/Ch15完整局部比较、逐字PRE通过，root授本段/自身末注窄锁；作者已写并实际顺读正文452–505完整邻接、Ch15 75–113交接及本末注，review_mar11_continue非写入者实际452–507完整局部、新489及本851注POST通过，root已释放窄锁，不授DAY。未核artifact或复现。

- `SF-2026-ARXIV-2603-09815` — Daily `2026-03-12`补查；[exact-v1](https://arxiv.org/html/2603.09815v1) §3/4/6/7.1–2/8–9，2+1+2=5 gap深入。只收coarse hidden correction分支/orthogonal与untied界区分，Eq1/2非等式、oblique放大、信号误压/temporal非causal、有限classification与完整费用近文；不采精确图数、医用结果/大LM或全稳定、实现/复现/完整SLO。root必要Source/date/actual owner逐字PRE通过，作者窄写两段及本注，非writer root实际顺读新70/73、64–86完整局部和本末注并回对必要原证，actualPOST通过，Ch17窄锁释放，不授DAY。

- `SF-2026-ARXIV-2610-10395` — Daily `2026-10-09`；[exact-v1](https://arxiv.org/html/2610.10395v1) §3–9与F.1必要状态纠错说明；2+1+2=5，persistent W/α与scratch交接具体缺口深入。有限构造和采样float64、single-fresh-encode与full-stream、solver/graph分责及所有费用近文；不授普通训练不可学、因果恢复或生产runtime保证。必要Source/actualCh17 owner与逐字PRE已由review_mar11_continue非作者实际通过，root授本单段及本人注窄锁；作者已写，root非writer actualPOST已顺读366–410完整Norm→算法→新389→Layer冗余及本人863注，回对有效Source/PRE通过，窄锁释放。未读全部证明/附件、artifact或复现，不授DAY。

- `SF-2026-ARXIV-2603-12541` — Daily `2026-03-17`补03/16自然日；[exact-v1](https://arxiv.org/html/2603.12541v1)，2+1+2=5，必要核心/关键反侧及具体差额见本日SUP_LINEAR_DEPTH_PRE_20261011.md。supp_mar17必要Source、实际唯一owner/完整邻接与逐字PRE由review_mar17_18独立局部通过，root授本正文与本人注窄锁；作者按PRE实际写入，review_mar17_18非writer实际顺读378–415完整局部、新391/393与本人869注，回对已核必要Source/逐字PRE，局部POST通过；resume_review17_18最终末注定点回读局部通过，不授DAY。采用范围、费用、反侧及原路径回退近正文；未核artifact/复现。

- `SF-2026-ARXIV-2603-14833` — Daily `2026-03-18`补03/17；[Ablate and Rescue exact-v1](https://arxiv.org/html/2603.14833v1) 必要§3.1–3.4/4.1–4.3/Table1/5，2+1+2=5。旧无依据先稿隔离纠正，只采用缓存冻结mixer下的成对ablation/single rescue接口及相似性非可互换边界；781M/Dolma、CounterFact仅65/21919通过knowledge check，分布KL恢复非正确率、非任意自然路由剪枝保证，CKA一般可逆线性不变性不采用。root必要Source/actual owner与两段逐字PRE经resume_review17_18独立限定通过；root授本两段与本人注窄锁后resume_mar18按原稿写入，resume_review17_18非writer实际完整474–500及867–877本人875/邻注逐字回对必要Source/PRE，局部actualPOST通过，不授DAY。未核artifact或复现。

- `SF-2026-ARXIV-2603-16535` — [SympFormer exact-v1 PDF](https://arxiv.org/pdf/2603.16535v1)必要§2–6/Propositions4.1/4.3/4.5/5.1/5.2、Algorithm1/Tables1–3与A相关证明/B。仅feature/velocity联合状态及连续几何、实际离散消费/费用分责；不授一般metric严格性、自由QKV/完整网络椭圆保持、Nesterov收敛或普遍质量/加速保证。有限TinyStories/RTX6000Ada对照和离散器反侧近文，未核代码/复现。

- `SF-2026-ARXIV-2603-17771` — [exact-v1](https://arxiv.org/html/2603.17771v1)§2–6/Theorems1–2与V-scale/Figures1–5文字、Limitations；当前v2仅RMSNorm局部上界/value接口定点。仅路径聚合、局部gain与前反共同干预的受限分离；不采纯反传/唯一中介、全局收缩、泛化质量或零成本。小C4条件/配置缺失保留，未核实现或复现。

- `SF-2026-ARXIV-2603-18168`：[ResNets of All Shapes exact-v1 PDF](https://arxiv.org/pdf/2603.18168v1)，必要Eq1/GD、Theorems1.1/2.5与§1.2–1.3及§5.2组合证明；仅三形状轴在指定ClippedGD/光滑条件下的有限步极限动态误差分责。保clip/shape门、k/N常数、finite-reference/手调系数、output猜想和未含Norm；不授全证明认证、全局优化/泛化、通用形状或硬件加速，未核代码/复现。

- `SF-2026-ARXIV-2603-26330` — [exact-v1](https://arxiv.org/html/2603.26330v1)§3/4.1–4.3.3/T1–4/5；2+1+2=5。跨boundary中间状态检索与层内适配分责，保pooledquery/共享attention、split反侧、额外容量/lr混杂及σnearzero非identity；不采全因果reasoningtax/低维定律/通用稳定或完整runtime配方，未核全部appendix/code/复现。

- `SF-2026-ARXIV-2610-13630` — Daily2026-10-13，窗10-12；[exact-v1](https://arxiv.org/html/2610.13630v1)必要位置、采用边界与actual-owner差额见[本日模型证据](../../papers/2026/10/_sources/daily-20261013/model-evidence.md)。today_models准备必要Source/逐字PRE，root独立定点Source/PRE通过后授本局部与本人末注窄锁；today_models已最小写入，root已实际顺读新增正文、完整局部邻接、diff及本人末注，nonwriter POST通过，窄锁释放，不授DAY。保正文限定与原路径，未核代码、复现或生产SLO。

- `SF-2026-ARXIV-2603-29496` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29496v1)S3.1–3.5/Eq15–19/S4T3–7/S5，2+2+2=6，仅input h配置operator/freshψ演化/readout分责。保CG40–60与Euler有限误差、CIFAR组合改变/去J与fromψ反侧、LM18.5M/2B/512/GH200对9.8M/7.2B/1024/8H100非matched compute、156vs80GPUmin/不同quant，不授守恒/全size或净优；未核代码/复现。

- `SF-2026-ARXIV-2604-11791` — Apr15补Apr14；[Looped exact-v1](https://arxiv.org/html/2604.11791v1) §2/§4Prop4.1–4.2/4.1–4.2、§5–6/B/C1。2+1+2=5具体同层跨loop与异层cycle fixedpoint缺口深入；保bounded tiedQK条件蕴含、128approx reference/Ouro小Δ仍未固定、Huginn稳定无clear mixing、ColSum非信息贡献/正确性，无通用早停/部署收益。256GSM8K与有限Ouro/Huginn/retro小模型配置，不外推全部架构；root必要Source/date/actual owner/PRE通过授两段+本人末注，root实际完整正文/上下邻/本人注非writer POST通过，作者仅同步本注并实读回，Ch17窄锁释放，不授DAY。未核实现/复现。

- `SF-2026-ARXIV-2610-20588` — Daily2026-10-16窗10-15；[Elastic exact-v1](https://arxiv.org/html/2610.20588v1)必要Source见本日唯一LIVE记录R6，2+1+2=5。只采冻结主模型的联合排序、预算截取与实际kernel/预编译分责；保小batch无收益、tiling质量损失、编译与buffer全费，不授生产LLM收益。独立reader A6逐字PRE/R9通过，root授指定两段与本人末注窄lease，作者已保存并读回；独立reader R11实际正文、完整邻接与本人注POST通过，root已释放指定窄lease；作者仅行政同步本注并实际读回。未核代码或复现，不授DAY。

- `SF-2025-ARXIV-2506-21734` — Daily2025-07-01补Jun30；[HRM exact-v1](https://arxiv.org/html/2506.21734v1)§2全部机制/Eq1–3/伪码/ACT、§3.1–3.3与§6，2+2+2=6，末步梯度/segment detach与前向双时钟信用差额局部深入。root本日§31必要Source/6分/Ch17差额、§36逐字PRE/完整邻接通过并授指定窄位；Boyle已按稿实际保存；root本日§37已实际完整新增/两侧/本人注及限定两层检查非writer POST通过，接纳本项实际整合并释放指定窄位。保有限步非达点、首项非精确IFT、停器真值只在训练、Full与1000例/ARC增强分账及全部费用，不采通用AGI/低时延或将27M榜单回填原1B HRM-Text；未核图像/代码/复现，不授DAY。

- `SF-2025-ARXIV-2506-22049` — Daily2025-07-01补Jun30；[GPAS exact-v1](https://arxiv.org/html/2506.22049v1)§3–5/T1–5/A–B及C必要反侧，2+1+2=5，前向scale与局部反传identity分责的Ch17小差额局部深入。root本日§43必要Source/5分/当前完整Pre-Norm邻接差额通过；不授原轨迹梯度等价、无信息损失或简化上界下的真实梯度稳定，保gate spike/部分质量反退、未完成7B预算与全费。不核全部proof/图像/实现或复现；root已实际完整逐字PRE/当前两侧/本人拟注核验通过并授指定窄位；Boyle按许可实际保存并完整self-read新段/两侧/本人注；root本日§53已实际非writer完整新增/两侧/本人末注及限定两层检查POST通过，接纳实际整合并释放指定窄位。本注仅同步既成事实，不授DAY。

- `SF-2025-ARXIV-2506-22696` — Daily2025-07-02补Jul1；[exact-v1](https://arxiv.org/html/2506.22696v1)§2–4/6、C.1/C.2与E必要Source，2+1+2=5，矩阵residual替代/读写适配与statewidth具体差额深入。保初始化moment非训练稳定、attention-storage反侧、Eq21/25及Table9配置未闭不授recipe，Table4百分比不采、tensorcontraction墙钟反退、μTransfer与variant调参差及全部费用，未核完整proof/图像/代码/复现，不授加速/无损/生产SLO。Newton§19实际受限Source/5分/具体gap及逐字PRE通过，root已核当前完整邻接并授本单段/marker/本人注精确窄位；Godel按许可保存并顺读完整新增/前后/本人注，Newton§23实际非writer POST通过，root已实际完整读回接纳并释放该精确位。本注仅同步既成事实，不授DAY。

- `SF-2025-ARXIV-2505-00685` — Noether，Daily2025-05-03补May2；[exact-v1](https://arxiv.org/html/2505.00685v1)§2–7/Alg1、A/B.1/D/E/F必要，Ohm110日证/current、140实际Source/2+1+2=5/唯一Ch17具体差额通过。仅取矩标准化后的形状变换、训练noise与Batch runninglambda分责；保二阶近似/曲率guard、D常数冲突、joint假设/成对proxy、搜参/不稳定与V100完整费用。不采最优语义容量/独立性、对抗安全、全LLM兼容或精确recipe；未看QQ/曲线像素、核代码/C完整推导或复现；Ohm143逐字PRE通过，root已实际读稿/完整两侧与末注并授本单段/本人注；作者已真实保存，已完整self-read新增/完整两侧/本人注，Ohm148已实际非writer完整新增/完整两侧/本人注POST通过，按root最新一次POST即生效规则，本指定窄位已生效释放；本注仅同步既成事实，不授DAY。

- `SF-2025-ARXIV-2506-22389` — Boyle，Daily2025-07-01补Jun30；[exact-v1](https://arxiv.org/html/2506.22389v1)§2–5/Eq1–5/T1–3及A/B必要文字，2+1+2=5，模块访问顺序/当步attention支持差额深入。root本日§82实际有限Source/唯一Ch17/作者88.1逐字PRE通过并授固定loop完整取舍段后/RecurrentRetrofit前单段与本人注；保dense前层、active/驻留人口、反退、非异步runtime证据和全费。未核全部图像/C–F/实现或复现。Boyle按许可实际保存，已完整self-read，root本日§83已实际完整新增、全部直接两侧与本人注非writer POST通过，接纳实际整合并释放指定窄位；本注仅同步既成事实，不授DAY。

- `SF-2025-ARXIV-2507-01900` — Noether，Daily2025-07-04补Jul3；[HARP exact-v1](https://arxiv.org/html/2507.01900v1)§2.3/式3–5/Alg1、§3/T1–5、AppB/C/E，2+1+2=5，替代算子与必要理论反侧深入。Ohm18/19实际原域和24当前唯一Ch17差额复用；只采去QK/跨token混合、保逐tokenV/O残差与逐模型尺度校准的经验分支，不采Theorem1/Proposition2的一般保证，保质量反退、不同裁剪预算和全费用。未核全部proof/图像/代码/复现；Ohm27正式Source/5分/逐字PRE通过，root已授完整layer-redundancy段后/因果链块前指定单段及本人一注；作者已按许可实际保存，Ohm37已一次实际非writer完整新增/完整两侧/本人及前注POST通过，按root本次授权实际整合生效并释放该指定窄位；仅同步已发生事实，不授DAY。

- `SF-2026-ARXIV-2605-14521` — exactv1§2–5/Alg1及A/B必要恒等、D2–3/E1–2/G2–3，2+2+2=6，仅affine-centering折叠与实际consumer资格。保相同eps/γβ、fanout/残差/非线性/dropout边界、浮点/计时口径及全部图改写/执行费用；不授任意图或无条件训练等价，未核实现/复现。

- `SF-2025-ARXIV-2509-09650` — Carson，Daily2025-09-13补Sep12；[exact-v1](https://arxiv.org/html/2509.09650v1)§3、4.1–4.4/4.6–4.8/T2/3/5/6、A1/A6，2+1+2=5，条件均值等待/位置可读路径与条件正确分母的具体诊断差额；保任务/tokenizer支持、wordproblem/代码/跨模型反退与全费/原层退路。不采唯一电路、任意推理/剪枝净速，未看全部图像、核代码或复现。Zeno34必要Source/正式5分/唯一Ch17及35逐字PRE通过，root本次新授本原一段/独立marker/本人注，现已实际保存；Zeno40已一次实际nonwriter完整新增/完整直接两侧/本人注/限定差额POST通过，本指定窄位按root授权实际整合生效释放；仅同步既成事实，不第三读或预DAY。

- `SF-2026-ARXIV-2605-30523` — Daily2026-06-02补Jun01；exact-v1本日SUP必要命题/关键评价或理论条件，原6、具体gap深入。root R46首次必要准备、作者一次实际消费及具体owner/PRE，经root R50实际核通过授本原单段/本人注，现已真实保存root R51已真实完整新增/完整直接两侧/本人注POST通过，指定窄位释放。采用边界/决定性反侧/全部费与旧路回退近文，不授完整证明/实现或复现，只同步既成事实，不预DAY。

- `SF-2026-ARXIV-2605-31423` — Daily2026-06-02补Jun01；精确v1必要定义/支持和关键反侧见本日SUP，原7深入；只采用正文窄命题，不授全定理/无损或实用普遍保证。root R53实际必要Source/当前owner/原PRE通过并授本原单段/本人注，现已真实保存root R54已真实完整新增/完整直接两侧/本人注POST通过，指定窄位释放，未核可选实现或复现，只同步既成事实，不预DAY。
- `SF-2026-ARXIV-2610-25646` — Daily2026-10-21补Oct20；oct21_resume_core_author B-R23必要Source/actualowner/完整PRE原样通过，root授精确单段+本人注。作者已保存批准稿并自读完整邻接/本人注；独立复核者B-R30一次actualPOST通过，窄位生效释放，仅行政同步不第三读；未核代码/复现，不授DAY。
- `SF-2026-ARXIV-2610-25254` — Daily2026-10-21补Oct20；oct21_resume_core_author B-R34必要Source/actualowner/完整PRE原样通过，root授精确单段+本人注。作者已保存批准稿并自读完整邻接/本人注；独立复核者B-R36一次actualPOST通过，窄位生效释放，仅行政同步不第三读；未核代码/复现，不授DAY。
- `SF-2026-ARXIV-2610-25086` — Daily2026-10-21/Oct20；B31必要原源/actual owner/完整最小PRE已由独立复核者B-R39通过，依root精确窄授保存原批准单段。采用边界与反侧/全部费用保正文，不授通用保证或实现/复现。作者已自读实际完整新增/完整直接两侧/本注；独立复核者B-R42一次actualPOST通过，窄位生效释放，仅行政同步不第三读，不授DAY。
- `SF-2026-ARXIV-2610-25076` — Daily2026-10-21/Oct20；B32必要原源/actual owner/完整最小PRE已由独立复核者B-R40通过，依root精确窄授保存原批准单段。采用边界与反侧/全部费用保正文，不授通用保证或实现/复现。作者已自读实际完整新增/完整直接两侧/本注；独立复核者B-R42一次actualPOST通过，窄位生效释放，仅行政同步不第三读，不授DAY。
- `SF-2026-ARXIV-2610-24135` — Daily2026-10-21/Oct20；C02必要原源/actual owner/完整最小PRE已由独立复核者R204通过，依root精确窄授保存原批准单段。采用边界与反侧/全部费用保正文，不授通用保证或实现/复现。作者已自读实际完整新增/完整直接两侧/本注；独立复核者R213一次actualPOST通过，窄位生效释放，仅行政同步不第三读，不授DAY。

- `SF-2026-ARXIV-2606-00819` — root，Daily2026-06-03补Jun02，exact-v1 §2–4/Eqs1–7/Alg1/T1–3，2+1+2=5；必要Source/actual-owner及独立reader R112完整修后单段PRE通过，未采用作者原稿。只公式定义的readout Δ方向→已算residual增量插值候选；保α文字与公式冲突、非真gradient/幻觉标签、分布制备/修改后传播/cache/零范数未闭、反退及全费，不据质量表验收完整执行路径、不补hook/recipe或授无损/加速。未核图像素/代码/复现，批准修后单段已真实保存并完整自读，R114唯一非writer实际完整新段/直接两侧/本人注POST通过，实际I生效、窄位释放；不授DAY，不第三有效Source/PRE。

- `SF-2026-ARXIV-2606-16694` — Daily2026-06-17补Jun16；exact-v1 II/III/VI.1及必要Gaussian/tree公式，2+1+3=6，固定通信预算下统计选择/深度条件与受限key-patch证据具体缺口深入。保同噪声/大N、linear/pooling、受限非adaptive搜索、8seed与非同全成本；不授生产Bayes最优或加速，未核代码/复现。root必要/PRE与实际SAVE后POST分记本日SUP_REVIEW，不预签DAY。

- `SF-2026-SEED-RECYCLER-20261025` — 官方10-25日期稿§2–3与直接反侧，2+2+3=7；仅顶层→embedding反馈及浅pass监督/Prefill/深度外推分账。KV不被替代，保局部质量回退、非等预算路线与未披露服务条件。未核实现/图像素或复现。独立PRE与实际POST以Daily2026-10-26的REVIEW为准，未授DAY。

- `SF-2025-ARXIV-2510-01796` — Hilbert，Daily2025-10-04补Oct03BJT；[exact-v1](https://arxiv.org/html/2510.01796v1)§2.2–2.3/3–5/A1、式1–5/T1–3必要由Lagrange R267首备、作者另一角色采用，2+1+2=5。仅宽skip/窄校正与固定初始投影的预算分支；保完整/可训参数分账、线性升维/秩反侧、局部PSNR/前沿非普遍支配、搜索域不闭及全部投影/状态/搜索费。未核像素/code/复现，无实测Transformer或净速/SLO；整体PRE/真实SAVE/selfread/唯一POST只以本日canonical实际层为准，不由本注预签。

- `SF-2025-ARXIV-2510-02049` — Hilbert，Daily2025-10-04补Oct03BJT；[DNL exact-v1](https://arxiv.org/html/2510.02049v1)R328首次必要理论/实验标准层供作者一次采用，作者仅Eq7/正则与Prop3/Th1关键关系直核，2+1+2=5。仅tau缩放dense历史读取的积分记忆与跨深度正则/对象分责差额；保V0/b1显示界反侧、局部ODE特例、指定H1/W1,3与子序列/全局极小而非SGD/泛化、训练loss人口及全费。不采Prop3常数recipe/完整Gamma证明或一般深网稳定保证，未核全部长证明/supp、图像素/代码或复现；整体PRE/真实SAVE/selfread/唯一POST只本日canonical实际层，本注不预签。

- `SF-2025-ARXIV-2510-02206` — Hilbert，Daily2025-10-04补Oct03BJT；[Poolformer exact-v1](https://arxiv.org/html/2510.02206v1)R385唯一首次必要Ch3/4/5决定域，A362仅pool/因果对齐、实际gate/base系数proxy与T4.2/4.4–6关键另一角色核，2+2+2=6。仅嵌套pool-inner-unpool/fine skip与粗细状态物理时钟差额；保非逆恢复/未闭causalshift和完整recipe、base系数非唯一长依赖、valbest/宽state/YouTube反退、八位量化/异预算及全部训练采样费。不采无限记忆/全过拟合预防/LLM替代或净部署速；封面完成日/学校有限公开门不代公开钟，不造全球无早稿保证。未核Ch2全推导/曲线像素/音频/实现或复现；整体PRE/真实SAVE/fullselfread/唯一POST仅本日canonical真实后到层，本注不预签。

- `SF-2025-ARXIV-2510-07739` — Aquinas，Daily2025-10-11补Oct10；Godel R65首次exact-v1 §2–4/T1/B/T2/C/D/E1/E3/F必要整体消费，451180B原件，不第二Methods。2+2+2=6，仅共享core外逐轮router/可写embedding槽/加性buffer读写consumer差额深入；保AppD系数非自由/无损未证、router外推未定义、160M及单项反退/参数口径、全B×L×D状态与执行训练费，不采普遍表达力/稳定或净速。未核全曲线/代码/运行复现；整体PRE/真实SAVE/完整自读/solePOST仅本日canonical后到真实层。

- `SF-2025-ARXIV-2510-12773` — Herschel，Daily2025-10-16补Oct15；[exact-v1](https://arxiv.org/html/2510.12773v1) §3–5/6.1/T4/6.5必要，2+1+2=5，block执行身份差额深入。仅零/一/两次执行与已计算residual缩放分责；保gold搜索/teacher forcing、KV未闭、模型身份与OOD反退/全费，不采无损或普遍缓存兼容。未核代码/复现；整体PRE/真实SAVE/完整自读/sole actualPOST只本日canonical实际后到层。

- `SF-2025-ARXIV-2510-15425` — Daily2025-10-21补Oct20；writer首次exact-v1§4/Alg1/5.1/5.3/5.5，Lorentz R16 key，2+1+2=5，共输入branch/渐进聚合差额深入。仅v1 ParaFormer，不混当前TeamFormer；保300epoch/8A6000最多6rank与架构预算混杂、PF1反退/UAT非收敛，不补渲染伪码为实现。未核代码/复现。

- `SF-2025-ARXIV-2510-15304` — Daily2025-10-21补Oct20；Lorentz R14首次exact-v1§4.1–3/5.1/5.3–4，writer核§4.2 SBI与concat，2+1+2=5，layer/channel重构差额深入。保小校准/跨域/>2层反侧、mp/sp预算及symmetric-KL印式不闭，不采完整loss/83%绝对精度/无损。实际owner为Ch17，未核实现/复现。

- `SF-2026-ARXIV-2606-18023` — Daily2026-06-18补Jun17；exact18023v1，消费sole§116必要2–5/T2–4/A–B。仅PLT globalKV+localwindow与CLP错位信息接口；R train/eval匹配非runtime增轮，Ω/三诊断非因果，r2cos−.72/r4.04与r4步长更大反侧保留。M2W R4优R2、R2低base及thinking/SFT混杂不授单调/superadditive，bf16/7B配置/总1M GPUh非逐R净速；hardware/SLO未披，原6不变，未核artifact/复现，sole§118完整PRE通过，实际SAVE/selfread，待sole实际POST。
