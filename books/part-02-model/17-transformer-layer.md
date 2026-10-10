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

若目标是给整个 block 的输入扰动一个可证明界，就要收紧分支本身，而不只保留 identity。一条条件构造把更新写成凸势的负梯度 Euler 步：MLP 为 `x−τWᵀReLU(Wx+b)` 且 `τ≤2/‖W‖²`；attention 把 value 与约定的投影绑定为 `V=A`，以 `x−η softmax(xᵀAy)Ay` 更新，在固定 compact domain 上限制 `η≤2/sup‖Ay‖²`。这样的 query 非扩张性依赖 tied weights、符号、步长与逐层域；普通自由 Q/K/V 的正向 residual 不自动满足。context 则有自己的 Wasserstein-1 Lipschitz 常数，不继承 query 的1。<!-- source-family:SF-2026-ARXIV-2602-15503 -->

[这一形式架构的近似定理](https://arxiv.org/html/2602.15503v1#S4)限定 scalar 目标，以及目标 Lipschitz 类与 lift/project 架构可实现类的交集；lift/project 自身也不能随意破坏界。它不授任意参数网络、vector 输出、可训练性或无限 token 的有限成本，更不是部署安全证明。逐层 compact domain 和 supremum 的认证可能很难，约束会限制表达与优化选择；缺少这些前提时，旧 residual、Norm、梯度/扰动实测与独立质量验收仍是工程基线。

表示还可在 Attention 与 MLP 更新之后走一条粗子空间修正分支：先把 hidden state 限制到较小空间，求解粗系数并延拓回原 shape，再以可调强度与原状态混合；若使用多个粗尺度，可另学非负归一化权重。[这一受限构造](https://arxiv.org/html/2603.09815v1#S6)改变的是每层内部的表示与额外计算，不是免费恢复原 identity，也不同于把输入 embedding 作为共享 anchor。真正正交的 P 下，`αI+(1−α)P` 在 `α∈[0,1]` 时不放大固定输入扰动；独立学习的 restriction/prolongation、带稳定项的 coarse solve 或多尺度混合，则不能仅凭“投影”名称继承此界。
<!-- source-family:SF-2026-ARXIV-2603-09815 -->

抑制某些方向有利，仍以任务信息主要留在保留子空间为前提：有用信号若在被压低方向，也会损失。有限 encoder 分类、人工类不平衡与句子噪声对照不能证明大规模生成模型普遍稳定或更快；全序列 temporal projection 还必须另证 causal prefix invariance。coarse solve/QR、额外参数、迭代、多尺度与训练调参都纳入训练和部署预算，学习到的 oblique operator 要检查条件数与放大而不自签平滑。算子、held-out 质量、因果性或完整费用未通过时，保留标准 residual/Norm 和原 Attention/MLP，不将启发式训练曲线当普遍收敛保证。
<!-- source-family:SF-2026-ARXIV-2603-09815 -->

跨层保留信息还可另开投影 anchor 分支，而不把第一层同时当作通用参考与逐层计算起点：从 input embedding 用额外的 Q/K/V/gate 投影构造共享 anchor，各层先归一化 anchor，再与当前投影学习混合，之后对混合 Q/K 执行 QKNorm/RoPE、计算 attention 并应用 gate。[ExoFormer 的受限分支](https://arxiv.org/html/2601.08131v1)改变的是 attention 子层的信息来源；这条有投影、有混合的旁路不等于原 identity residual，更不能直接继承上式的导数 I。原 identity path 仍保留其梯度短路职责。<!-- source-family:SF-2026-ARXIV-2601-08131 -->

新增四个投影带来额外参数与缓存/计算状态，归一化次序和 Q/K 尺度又影响能否稳定复用。作者约450M参数、10B tokens、H100/BF16、sequence2048的比较支持局部设计选择，不是完整容量匹配或长上下文证据；部分任务也未改善。外 anchor 模型内部 token similarity 更高、维度更低却表现较好，支持进一步检查“信息被外部分支承载”的 offloading 假说，不证明 token identity 必被保留或 collapse 具有普遍因果收益。成本、归一化或 held-out 质量不成立时，保留普通 residual、单值复用或单独 gated attention，而不因诊断曲线推荐所有层都外置 anchor。

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

标准 block 把非线性容量主要放在 Attention 权重和独立 MLP 中，Q/K/V 与输出等 projection 则保持线性，便于实现与成本核算。若目标是在较窄的中间空间增加逐位置函数容量，也可以从预训练开始，把任一线性 projection 改为 `xW + b + σ(xA)B`：A 将输入压到 rank r，σ 在瓶颈中作非线性变换，B 将结果投影回原输出 shape。它不改变该 projection 的外部接口，却改变了内部计算图；不同于[第30章 LoRA](../part-04-training-system/30-lora.md)的冻结基座加线性权重更新，这里的主矩阵也可训练，非线性支路通常不能合并成一个固定的 W，推理时仍须执行。<!-- source-family:SF-2026-ARXIV-2603-06492 -->

这种分支用额外参数、activation 与永久部署 FLOPs，交换达到某一训练损失所需步数的可能减少；因此应比较目标损失下的墙钟成本，而不是只比较步数。[NOBLE 的受限预训练对照](https://arxiv.org/html/2603.06492v1#S4)使用250M/1.5B模型、OpenWebText、长度1024及H100/BF16编译执行，不能直接外推大模型服务收益；ViT 对照中拟合损失改善也没有带来同幅度的验证准确率改善。瓶颈初始化与各参数组学习率另需调校，cosine 输出有界不保证整个支路 Jacobian 或梯度有界，作者的频率解释也不构成泛化证明。推理预算紧、局部收益不能覆盖新增计算或质量回归时，保留线性 projection 与独立 MLP；低秩非线性是有成本的架构分支，不是 residual/Norm 的替代稳定性保证。<!-- source-family:SF-2026-ARXIV-2603-06492 -->

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

## 不计算归一化，也要控制信号与导数的深度传播

如果把 Norm 换成逐元素饱和函数，节省的是归一化运算，不是自动保留原来的梯度条件。以 `tanh(αh)` 或 `erf(αh)` 为例，`α` 是函数输入的可学习尺度，初始化时决定激活方差与平均平方导数；它不是另加在 residual branch 外面的乘法 gate。残差累加、权重初始化和最终读出层共同决定 Jacobian 随深度的行为。较小的 `α` 可减弱分支的有效贡献、延后初始化信号放大，却也可能过小而使收敛变慢。因此“函数有界”与“整网可训练”不是同一件事，学习率、warmup、深度和输入尺度仍需联合检查。<!-- source-family:SF-2026-ARXIV-2604-11890 -->

[受限初始化分析](https://arxiv.org/html/2604.11890v1)比较了 Pre-LN 与这类替代函数的 APJN，即 Jacobian 平方 Frobenius 范数的均值；它不是每个奇异值都稳定的保证。推导使用宽模型、双向均匀 attention、独立高斯初始化与 token 置换对称等近似，CIFAR-100 上的 ViT 实验主要检验初期训练的稳定边界，并不证明 causal LM 或完整训练后的质量。最终读出层也会改变整体放大因子，不能只校准中间 block。成熟 Pre-Norm 在证据不足时仍是更稳妥的基线；尝试无归一化分支时，应分别验收初始化传播、实际收敛与任务质量，而不是凭匹配一个 APJN 数字就认定二者等价。

有界 activation 还会在 regularization 与容量瓶颈之间换位。任务所需信息量与参数容量的比例 `T/P`，连同架构，决定饱和约束是在限制无效变化还是截断必要表达；不能只凭函数有界就判定优劣。作者的跨设置分析只覆盖 `T/P < 1.84`，阈值 0.43 的 leave-one-setting-out 判别约为 50%，并不构成可自动选型的 controller。<!-- source-family:SF-2026-ARXIV-2604-23434 -->

估计任务信息需求、容量和跨架构校准增加实验成本，`T/P` 也不是线上可直接观测的充分统计量。应保留 matched learning curve、质量与饱和程度的联合检查；容量不足、阈值迁移失败或新任务未校准时，回退成熟 normalization/activation，而不是按单一比例静默替换架构。

逐 token 的 Norm 在训练初期输入尺度尚未稳定时仍是合理基线；若目标是移除推理路径上的归一化，还可把控制分成两个阶段：warmup 继续执行 Norm，同时收集其尺度统计，之后逐渐过渡到冻结、与 sample 无关的缩放。这样的常数才有机会折叠进相邻 linear 权重；LayerNorm 的 mean-centering/affine 结构仍需单独处理，不能把 RMS 的折叠规则直接套用。它改变训练轨迹和部署产物，校准窗口、gate schedule、冻结尺度与权重版本必须一起验收，而不是训练后直接删除 Norm。<!-- source-family:SF-2026-ARXIV-2602-10408 -->

内部尺度被冻结，并没有替最终读出层建立同一份合同。ε=0 的归一化读出具有零阶齐次性，径向梯度可为零；撤去这一锚后，正 margin 的交叉熵仍可能推动 logit scale 增长。保留 final Norm 与另加目标尺度 penalty 是不同分支，后者仅提供局部径向恢复力，不证明整个模型稳定。[TaperNorm 的受限对照](https://arxiv.org/html/2602.10408v1)中，移除更多 Norm 仍会损失部分 CE/任务质量；无 KV cache 的 forward microbenchmark 也不等完整生成提速。统计失配、OOD 尺度漂移或质量回归时，应保留动态 Norm/最终读出锚及原训练路径，而不是由可折叠性授予无条件替代。

## 层堆叠可以被解释成迭代优化，但不是 Hidden-state 真理

前面的 Jacobian 分析回答传播是否稳定，却还没有说明一层更新在执行什么算法。把更新解释成某种优化步骤，是比形状与梯度合同更强的命题，必须另加条件。

普通 residual layer 最稳妥的解释是对 representation 做逐层可学习更新；在受限函数类与分布假设下，也可以把 context-carried state 的层间变化构造成 normalized-gradient iteration。这个视角解释为何深度可能对应算法步数，但只要参数共享、归一化、目标构造或分布条件改变，就不能把 hidden state 直接命名为某个真实 optimizer state。

算法解释带来可分析的归纳偏置，却可能把存在性构造误当成实际机制。无法通过干预和跨设置验证时，应回退 representation-update 解释；现有 exact-v1 只证明作者定理与实验条件，不证明生产 LLM 在执行该优化器。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06609 -->

若目标是执行一个给定数值更新，而不只是为可学习层提供优化类比，算子与状态可以直接按算法构造：把当前矩阵和乘子放在 persistent registers，用无 softmax 的 linear attention 做矩阵积、bilinear/ReLU 子层做乘法和阈值，再清理 scratch 后交给下一块。外部控制器仍拥有更新步长、penalty schedule 与停止，丢掉乘子可能使同一矩阵对应的下一步不再唯一。[受限固定权重构造](https://arxiv.org/html/2610.10395v1)因此要求分测同状态/控制下的单步对齐、完整 residual stream 的反复交接，以及 solver 自身的任务结果；每步重新编码和 arithmetic replay 不代替 scratch-reset 验收。有限 float64 检查不授任意 kernel 精确，fixed-stage 的收缩和误差界也不认证外部 controller、因果恢复或普通训练必能学会该执行器。编码、宽状态、完整更新与精度/回归检查都付费；状态或数值条件失配时保留显式数值 solver、完整状态和 reference transition 测试，不把流畅输出或最终 graph 命中批准为算法正确。<!-- source-family:SF-2026-ARXIV-2610-10395 -->

## Layer “冗余”取决于干预协议

稳定地堆深之后，另一个问题才是哪些层值得保留。梯度是否健康、表示是否相似与一层能否删除不是同一个判断，必须分别检验。

相邻 residual states 相似，不必然说明层更新没有新增计算：累计状态包含前面的共同历史，即使各层更新互不相关、大小相同，基于全 lag 相似性的一个 effective-depth 摘要也可小于2。这个结构参照不是“只用了两层”的证明，更不是能力上限。比较实际模型时还须匹配 update 大小、初始状态 carry 和 update 相关性；这些参照可改变相对 gap 的符号，global accumulated-state 几何与某层的功能贡献不能互换。

Pooling、BOS幅度、归一化和相似性不变性都限定诊断看得见什么，相关 update 也不自动意味着可删除。作者有限 residual-carry 干预中，提高该摘要的强干预反而破坏训练；局部按摘要变化剪层又劣于专门的邻层指标。因而把该量用于校准表示几何，仍须以当前任务上的具体干预、剪后完整回归和实际执行成本决定 release；没有对应证据时保留原层，不能以更低 effective depth 宣称模型浅、capability差或获得免费剪枝。[必要定义与反证](https://arxiv.org/html/2609.31098v1) <!-- source-family:SF-2026-ARXIV-2609-31098 -->

逐层替换为某个固定 baseline，适合测“删除这一层后模型是否仍工作”；把两层互换，则测它们在上下文位置和 residual state 下是否可替代。这两个 protocol 改变的输入状态、下游补偿空间和 evaluator 都不同，因此不能从 replacement 影响小直接推出 layers 可交换或可安全剪枝。

任何 layer-redundancy 结论都应绑定 checkpoint、干预操作、位置、数据切片和 evaluator，并在剪枝后重新验证完整模型。受限实验可以暴露 protocol-dependent redundancy，但不证明跨模型或跨任务存在固定“无用层”；证据不一致时保留原层结构，或只把干预作为诊断而非 release 决策。

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

另一条分支不保存更多历史，而是改变当前状态的 carry 与 write。令 $X\in\mathbb R^{d\times d_v}$ 为层间状态，方向 $k(X)\in\mathbb R^d$、写入值 $v(X)\in\mathbb R^{d_v}$ 与 gate $\beta(X)\in[0,2]$ 由当前输入产生，可定义 $A(X)=I-\beta kk^\top/(k^\top k+\epsilon)$，再执行 $X'=A(X)X+\beta kv^\top$。同一 gate 同时控制旧投影的擦除与新值写入，不是先无条件删掉历史再补一个普通 residual。在单位方向、$\epsilon\to0$ 且固定输入的理想分析中，$A$ 在 $k$ 方向的特征值为 $1-\beta$，其余方向为 $1$：$\beta=0$ 保持状态，$\beta=1$ 擦除该方向后写入，$\beta=2$ 对 carry 做反射后写入；区间内 carry 的谱范数不超过 $1$，但一般并不等距。

这个算子界不等于整层 Jacobian 界：$k$、$v$ 与 $\beta$ 都依赖输入，导数还有这些分支与写入项；有限 $\epsilon$ 也不能直接照搬理想投影或精确反射。它提供的是 depth-wise rank-one 更新的替代结构，不是时间序列记忆的默认删除策略，更不能只从 carry 的谱推出训练稳定或质量收益。现有必要证据是结构与条件性分析，没有实测收益；采用前仍须训练匹配该接口，并验证方向归一化、gate 饱和、状态布局与执行成本。没有对应训练产物或任务回归不成立时，普通 residual 与现有 depth routing 仍是合理基线。由此再考虑下面的多流结构时，先分清改变单个状态的几何与增加状态流数量是两条不同分支。

### 多流 Residual 把 Layer Identity 从单一向量扩展为受控状态组

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23259:start -->
单一 residual stream 让层间接口稳定、实现简单，是默认可堆叠结构；当不同更新需要保留各自轨迹时，可以维护多条 residual state，再由 gate 与 attention pooling 决定哪些增量进入下一层。Layer identity 因而不仅是参数与 Norm，还包含 stream 数量、gate、pooling 与合并顺序。

多流结构增加表示容量，也增加显存、通信、gate collapse 和训练不稳定风险。exact-v1 只支持作者架构与实验，不证明 stream 越多越好；gate 饥饿、数值漂移或收益不足以覆盖状态成本时，应回退普通 residual 或较简单的 Attention Residual。arXiv:2605.23259v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23259:end -->

### 多流混合还要保留哪些几何约束

单一 residual 的 carry 路径是恒等映射；扩展为多流后，不能把读取、跨层传递和写回统称为一个 gate。令 `X` 的每一行是一条流，`H_pre` 将多流读入子层，`H_res` 混合并传递旧状态，`H_post` 将子层增量写回各流：

```text
X_next = H_res X + H_post^T F(H_pre X, W)
```

可学习的读写提高组合能力，但跨层 carry 变成 `H_res` 的乘积；若没有约束，它可能改变流均值，放大或削弱传播信号。一条替代分支把 carry mixer `M` 限制为非负双随机矩阵：每行、每列的和均为一，所以 `M1=1`、`1^T M=1^T`，且矩阵乘积仍满足这些约束。这保留了 carry 路径的均匀方向与流均值，并使这一路径的谱范数不超过一，却不等于恢复对任意向量的恒等映射：均匀平均矩阵会完全消掉流间差异。读写映射、子层增量和输入相关 mixer 的导数仍会改变完整 Jacobian，因此不能从 carry 的守恒推出整网梯度稳定。多流状态也增加访存和重算压力；子层 FLOPs 不变不是总执行成本不变。[受限机制证据：mHC v1 §3–5](https://arxiv.org/html/2512.24880v1#S4)

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

内部计算也可沿序列位置增长，而非只在当前位置反复运行共享 block。一个 continuous-thought 分支把 top-layer state 反馈为新的连续输入位置，写入后续 KV，只有需要可见输出时才作 vocabulary prediction。它保留了跨位置的 causal history，因此不是前述 same-position recurrence；省下输出词表接口不意味着省下追加位置的 attention、cache 或共享层执行。

训练可以并行 refinement，decode 却按这些连续位置顺序展开，二者的依赖图和实际成本不能互换。block application 数不等 FLOPs、KV 占用或 latency：同 block count 的物理加深仍可更好，vanilla baseline 也未按全部训练 FLOPs 匹配；分别训练的 K 不授予推理时任意切换预算。受限结果只支持参数容量与内部计算的一个取舍。串行等待、cache 增长或质量回退时，固定深层、原共享 loop 或可审查的显式 CoT 仍合理，不能把 continuous thought 写成免费计算。 [必要机制与反证](https://arxiv.org/html/2609.21605v1)。<!-- source-family:SF-2026-ARXIV-2609-21605 -->

跨位置反馈还可把可监督的中间思考留在辅助模块，而不追加主模型的输入位置：[一条受限分支](https://arxiv.org/html/2602.08332v1#S3)读取一个 input chunk 的深层表示，由轻量 head 生成自然语言 thoughts，再压成固定大小的状态，加到下一 chunk 的浅层表示。这样以状态递归替代主上下文中的思考 token，但仍运行辅助生成、压缩和原 causal KV 路径。

训练若已拥有逐 chunk 对齐的 gold thoughts，可以先压成 gold states 并 teacher-force 各位置，消去跨 chunk BPTT、并行计算 backbone；线上没有 gold history，chunk 之间仍要等待实际状态。预设后续状态为空再固定最早有效边界、重算后缀，只在空状态足够稀疏时改善 prefill，轮数不等 TTFT。有限 Qwen task fine-tuning 的 GSM 质量仍低显式 CoT；问题目标直到尾部才揭晓时，早期状态还会追错量。对齐教师、附加模块与重算都增加费用，thought 可见也不认证内部忠实性；监督缺失、目标晚揭晓或净成本不合算时，保留原 fixed stack、连续输入反馈与可独立验证的显式 CoT。<!-- source-family:SF-2026-ARXIV-2602-08332 -->

跨位置反馈也不必全部回到新的 input embedding。一个更细的旁路把过去位置的高层状态，经连接专属的线性投影，加到后续位置的低层更新：`h_l^i = LayerBlock_l(...) + α D_(s→l)(h_s^(i−g))`，其中 `s>l`、`g≥1`。它避免同一位置高层与低层互相等待，保留因果次序；改变的是内部层之间的状态路径，不是新增 vocabulary token。按 `g` 个位置分组可减少这条 downward 路径的串行前沿，却不取消普通 causal attention 对组内先前位置的读取，也会缩短可沿序列累积的反馈路径。训练与 prefill 因新增高→低依赖而损失部分并行性，投影参数、过去 hidden state 与执行开销仍需计费；autoregressive decode 本来串行，不等于旁路没有额外成本。[受限 fine-tuning 对照](https://arxiv.org/html/2602.17993v1#S4.SS4)中，group size 与增益 `α` 的组合会改变训练时间和质量，大分组配大增益还可退步；参数数近似匹配与单一 soft-token 控制不足以证明所有 latent reasoning 的优劣。任务不需要这种内部路径、串行准备成本超预算或更新失稳时，原 fixed stack、连续输入反馈和显式 CoT 仍应保留。<!-- source-family:SF-2026-ARXIV-2602-17993 -->

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

层级也可沿序列分辨率组织，而不只让两个module持有快慢时钟：对因果chunk作pooling，让不同分辨率以共享core及各自recurrence预算更新，再交回细粒度位置。粗状态包含哪个chunk必须显式定义；g−1 shift用于避免当前位置读取尚未到达的同chunk信息，overlap另影响覆盖与质量，不把二者合称因果保护，pool/upsample、边界和位置身份须保持同一因果图。它改变多分辨率依赖与局部执行预算，不是对完整token recurrence的精确缓存优化。<!-- source-family:SF-2026-ARXIV-2602-11698 -->

Pooling、交接和overlap仍有算量与细节损失，较少prefill FLOPs不等wall-clock、decode费用或长历史无损。[Spiral exact-v1](https://arxiv.org/html/2602.11698v1)在Pythia160M–1.4B/Pile250B/context4096的受限对照中，移除overlap会伤质量，而相关baseline也受益，不能把全部收益唯一归因于hierarchy。预算、chunk边界或质量不稳时，保留完整token recurrence、固定层深或显式CoT；需要可寻址历史时仍按第22章独立验收，不靠增加局部loop补回被合并的信息。<!-- source-family:SF-2026-ARXIV-2602-11698 -->

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
