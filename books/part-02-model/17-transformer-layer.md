# 第17章 Transformer Layer

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-TRANSFORMER-LAYER`
**Legacy Chapter:** Ch17
**Status:** Draft

**Roadmap Intent:** Residual、Normalization、Attention、MLP 如何组成可堆叠模块。

## 本章要回答的问题

Multi-Head Attention 与 MLP 单独都能计算，为什么不能简单首尾相接并无限堆叠？梯度为什么会随深度消失或爆炸？Residual connection 和 Normalization 分别稳定了什么？Pre-Norm 与 Post-Norm 为什么会改变深层训练行为？

本章的核心判断是：**Transformer Layer 是一个保持 residual stream shape 不变、并显式管理跨层信息与梯度路径的可堆叠状态更新单元。**Attention 负责跨 token 混合，MLP 负责逐位置变换，Residual 保留信息与梯度短路，Normalization 控制子层输入尺度。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`d_model` 表示 hidden dimension，`H` 表示 Query head 数，`d_h` 表示单个 head dimension，`d_ff` 表示 MLP 中间维度，`L` 表示 layer 数。

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

## 梯度为什么会随深度消失或爆炸

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

## Normalization 控制什么

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

## Residual Stream 从单一累加状态走向 Depth-wise Routing

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

### Parameter Depth 与 Execution Depth 可以分离

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

## Dropout、precision 与训练/推理差异

训练时可能在 Attention weights、sub-layer outputs 或 residual branches 使用 dropout；推理时通常关闭。Mixed precision 会让 Norm、residual accumulation 与 softmax 的数值策略更重要。

章节公式描述逻辑语义，不代表每个算子都以相同 dtype 独立执行。Fused kernels 可以合并 Norm、projection、bias、activation 或 residual add，但需要保持 checkpoint 与数值容差内的模型语义。

## 本章没有解决什么

Transformer Layer 本身没有规定：

- 是双向还是 causal Attention。
- 输入输出任务怎样组织。
- 是否使用 encoder、decoder 或 decoder-only。
- 生成时怎样缓存 K/V。
- 最终 token 怎样采样。

这些分别属于第18～20章。Layer 是可堆叠计算单元，不是完整语言模型。

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

## 小结

Transformer Layer 通过 residual stream 把复杂计算组织成 shape 稳定的增量更新。Attention 混合上下文，MLP 变换逐位置 features，Residual 保留信息和梯度短路，Normalization 控制子层输入尺度。

Pre-Norm 与 Post-Norm 的差异不只是代码顺序，而是梯度路径设计。理解完整 shape 流后，模型深度、activation、KV Cache 与分布式切层之间的联系也变得可见。

## Review notes

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
