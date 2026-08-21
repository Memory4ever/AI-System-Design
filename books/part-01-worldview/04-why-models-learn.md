# 第4章 模型为什么能够学习

**Knowledge Tree:** Part I 世界观：AI 为什么会发展成今天这样
**Stable Knowledge Node ID:** `WORLDVIEW-WHY-MODELS-LEARN`
**Legacy Chapter:** Ch4
**Status:** Draft

**Roadmap Intent:** 从函数近似、损失函数、梯度下降、表示学习理解“学习”的本质。

## 本章要回答的问题

程序员没有把识别图片、预测下一个 token 或翻译句子的全部规则写进代码，模型为什么仍能改善这些任务？“训练成功”究竟证明了什么，又没有证明什么？

本章的中心命题是：**模型学习，是在给定数据、参数化函数和目标函数的前提下，利用优化算法搜索参数，使经验风险下降；它既不等于理解世界，也不自动保证对未知数据泛化。**

这个定义刻意包含四个条件：模型能表示候选函数，目标函数能提供可计算的偏差信号，参数变化能被有效传播，数据中存在可利用的规律。缺少任何一个条件，增加训练时间都未必产生有用能力。

## 从手写规则到参数搜索

考虑一个垃圾邮件分类器。朴素方案是手写规则：出现某些词加分，发件域名异常加分，命中白名单减分。这种方案的优势是行为可解释，问题是规则数量会随语言、攻击方式和业务分布增长，规则之间还会互相冲突。

另一条路线是定义一个带参数的函数：

```text
y_hat = f_theta(x)
```

其中：

- `x` 是输入，例如邮件的特征或 token 序列；
- `theta` 是模型全部可训练参数；
- `f_theta` 是由模型架构规定的函数族；
- `y_hat` 是模型预测。

工程师不再逐条规定输入到输出的映射，而是提供训练样本 `(x_i, y_i)`，再定义预测偏离目标时应付出多大代价。学习问题由“写出规则”变成“在函数族中寻找一组参数”。

这并没有消除设计，只是改变了设计位置。人仍然选择数据、架构、输入表示、目标函数、优化器和评估标准。模型只能在这些选择构成的边界内学习。

## 先区分三个经常混在一起的问题

神经网络“能够学习”至少包含三个不同命题。

第一是 **representation capacity**：模型函数族里是否存在一个足够好的函数。Universal Approximation 一类结果讨论的是特定条件下的表示能力。它说明某些网络可以逼近一类函数，但不告诉我们需要多少参数、多少数据，也不保证训练算法能找到那组参数。

第二是 **optimization**：从当前参数出发，算法能否在可接受时间和资源内找到低训练损失区域。一个好解存在，不代表梯度下降一定到达；loss surface、初始化、数值精度、batch 噪声和学习率都会影响路径。

第三是 **generalization**：训练集上的低误差能否延续到未见样本。即使模型把训练集完全记住，经验风险也可以很低，但真实业务分布上的风险仍可能很高。

可以把三者写成三个不同问题：

```text
Can the function family express a useful solution?
Can optimization find a useful solution?
Will the solution work beyond the training samples?
```

本章主要回答第二个问题，并说明它如何依赖第一个问题。第三个问题及模型最终形成的表示，留给第 5 章。

## Loss 把任务目标变成局部信号

模型输出本身不能告诉优化器“哪里错了”。我们需要一个损失函数：

```text
L(y_hat, y)
```

`y` 是目标，`y_hat` 是预测，`L` 返回该样本上的代价。例如回归可用平方误差，分类或语言建模常用基于负对数似然的损失。不同 loss 表达不同偏好；它不是现实目标的天然真理，而是任务目标的可计算代理。

给定包含 `n` 个样本的训练集：

```text
D = {(x_i, y_i)} for i = 1, ..., n
```

经验风险定义为：

```text
R_hat(theta) = (1 / n) * sum_i L(f_theta(x_i), y_i)
```

其中 `R_hat(theta)` 是参数 `theta` 在有限训练集上的平均损失。训练的基本目标是寻找：

```text
theta_star = argmin_theta R_hat(theta)
```

这一定义非常重要，因为它同时说明了训练的力量与边界。只要损失可计算，模型就可以通过大量样本获得密集反馈；但优化器看见的只是 `R_hat`，看不见没有进入数据和 loss 的业务目标。

例如，一个回答在 token-level loss 上更可能，并不自动意味着它事实正确、安全或符合业务策略。那些目标需要通过数据构造、后训练、约束和 Evaluation 进入系统。

## 梯度下降：怎样从错误走向参数更新

如果参数很多，枚举所有 `theta` 不可行。梯度提供了当前位置上损失变化最快的方向：

```text
g_t = grad_theta R_hat(theta_t)
theta_(t+1) = theta_t - eta_t * g_t
```

其中：

- `t` 是训练步；
- `g_t` 是当前参数处的梯度；
- `eta_t` 是 learning rate；
- `theta_(t+1)` 是更新后的参数。

负梯度是局部下降方向，不是全局最优导航。学习率过小，训练进展缓慢；过大，更新可能越过有效区域甚至数值发散。实际优化器会加入 momentum、自适应缩放、weight decay 等机制，但核心仍是利用局部导数决定参数如何改变。

数据集通常太大，无法每一步计算完整平均损失。训练因而使用 mini-batch `B_t` 对梯度做估计：

```text
g_t = (1 / |B_t|) * sum_(i in B_t) grad_theta L(f_theta(x_i), y_i)
```

`|B_t|` 是 batch 中的样本数。这个估计带有噪声，但计算成本更低，也能持续提供更新方向。batch 变大时，梯度估计通常更稳定，却需要更多显存和并行设备，并可能改变优化动力学；batch 变小时，噪声更大但更新更频繁。

所以 batch size 不是单纯的吞吐参数。它同时连接统计估计、优化行为、显存容量和分布式通信。

## Backpropagation：把输出误差分配给每一层

深度网络是复合函数。以三层计算为例：

```text
h_1 = phi_1(x; theta_1)
h_2 = phi_2(h_1; theta_2)
y_hat = phi_3(h_2; theta_3)
```

最终 loss 只在输出端计算，但所有层的参数都影响输出。链式法则把这种影响向后展开：

```text
dL / dtheta_1
  = (dL / dy_hat)
  * (dy_hat / dh_2)
  * (dh_2 / dh_1)
  * (dh_1 / dtheta_1)
```

Backpropagation 不是另一种学习目标，而是高效计算这些梯度的算法。前向传播保存必要的中间激活，反向传播从 loss 出发复用局部导数，把 credit 或 blame 分配到各层参数。

这解释了深层表示为什么可以共同调整：早期层不需要人为指定“应该检测什么”，只要它产生的中间特征能通过后续计算降低最终 loss，梯度就会推动它被保留或强化。表示学习由此出现，但“具体学到了什么”仍取决于数据、架构和目标，第 5 章再展开。

深度也会带来困难。很多局部导数连续相乘，可能造成 vanishing gradient 或 exploding gradient；激活保存会占用大量显存；网络越大，反向传播的计算和通信成本越高。Residual connection、normalization、初始化和优化器设计，都是为了让梯度信号在深网络中更可用，而不是改变学习的基本定义。

## 为什么非线性不可缺少

如果每一层都只是线性变换，多层相乘仍然等价于一次线性变换：

```text
h_1 = W_1 x
h_2 = W_2 h_1
y   = W_3 h_2

y = W_3 W_2 W_1 x
  = W_equivalent x
```

加入 bias 也不改变结论：

```text
h_1 = W_1 x + b_1
y   = W_2 h_1 + b_2

y = W_2 W_1 x + W_2 b_1 + b_2
  = W_equivalent x + b_equivalent
```

因此任意深度的纯 affine network 仍属于同一个函数族：

```text
F_affine = {x -> W x + b}
```

它只能对空间执行 rotation、scaling、projection、shear 和 translation，不能表示 `x^2`、`abs(x)`、XOR，
也不能让不同输入区域使用不同变换。若中间 hidden width 小于输入/输出维度，矩阵乘积的 rank 还受最窄
bottleneck 限制；深度此时可能缩小可表达集合，而不是扩大它。

这不表示深层线性参数化毫无意义。`W = W_L...W_1` 会改变 optimization trajectory、implicit bias、矩阵分解
和可能的 low-rank preference；但这是：

```text
same function class
+ different parameterization and optimization bias
```

而不是获得新的非线性函数类别。

### 非线性让输入进入不同的局部计算区域

加入 activation：

```text
h = sigma(W_1 x + b_1)
y = W_2 h + b_2
```

一般无法再把 `sigma` 吸收到一个固定的 `W_equivalent` 中。以 ReLU 为例：

```text
ReLU(z) = max(0, z)
```

不同输入会激活不同 neurons，于是网络在不同区域执行不同 affine map：

```text
f(x) =
  W_A x + b_A,  x in region A
  W_B x + b_B,  x in region B
  ...
```

ReLU 在每个固定 activation region 内是线性的，但整个函数是 piecewise linear；“局部线性”不等于“全局线性”。
例如：

```text
abs(x) = ReLU(x) + ReLU(-x)
```

已经无法由一条全局直线表示。更深的网络继续组合这些 partitions，使简单局部变换形成复杂、层级化的函数。

可以把核心直觉写成：

> 线性层负责变换坐标，非线性让不同输入进入不同的局部计算区域；只有二者交替组合，深度才不再坍缩为一个固定矩阵。

## UAT 回答“能不能表示”

Universal Approximation Theorem 为上述直觉提供了表示能力边界。经典结果的一种抽象表述是：对紧致输入域
`K` 上的连续目标函数 `f` 和任意 `epsilon > 0`，在满足定理条件的 nonlinear activation 下，存在足够宽的
单隐层网络：

```text
f_hat(x)
= sum_(i=1)^m a_i * sigma(w_i^T x + b_i) + c
```

使得：

```text
sup_(x in K) |f(x) - f_hat(x)| < epsilon
```

Cybenko 的经典版本使用 continuous sigmoidal nonlinearity；后续结果把条件推广到更广的 activation family，
其中关键边界是 activation 不能让整个网络重新坍缩为有限维的多项式/线性函数族。对 `sigma(z)=z`，上式直接化为
`W x + b`，所以纯线性网络不具备这种 universal approximation property。

UAT 的重要结论是：

```text
suitable nonlinearity + sufficient width
→ broad approximation capacity
```

但它同时带来一个容易被忽略的反直觉：**一个 hidden layer 在理论上已经可以 universal approximate。**因此 UAT
不能单独回答“为什么现代网络还需要很深”。它也没有给出实际所需 width、数据和计算，更没有保证优化器能找到
那组参数。

UAT 是 existence theorem，不是 training theorem。它不能推出：

- 任意有限大小的网络都能达到目标误差；
- gradient descent 能在有限预算内找到存在的参数；
- 有限训练数据足以确定正确函数；
- 训练误差下降会产生 deployment generalization；
- 模型因此理解了任务或具备事实可靠性。

所以必须保持：

```text
Representable
!= Efficiently representable
!= Optimizable
!= Learnable from finite data
!= Generalizable
!= Reliable
```

## Depth Separation 回答“为什么要深”

如果浅层网络已经 universal，深度的主要价值就不是把“不可能表示”变成“可能表示”，而是**表达效率与组合式
inductive bias**。某些函数可以由深网络用 polynomial 数量的 units 表示，但浅网络若要达到相近误差，可能需要
exponential width。Depth Separation 理论研究的正是：

```text
同一个 target function
→ shallow network: how wide?
→ deep network: how many reusable compositions?
```

Telgarsky 构造了深层、窄网络可以表达，而显著更浅的网络必须指数级增宽才能逼近的函数；Eldan 与 Shamir 也证明，
在其构造与 activation 条件下，增加很少的 depth 就可能带来指数级 size separation。这些是特定函数族上的
theoretical separation，不表示所有任务都会获得相同倍数，也不表示更深一定更容易优化。

直觉上，浅层网络可能需要用大量 neurons 直接枚举复杂 input regions；深层网络则可以复用中间计算：

```text
pixels
→ edges
→ textures
→ parts
→ objects
→ relations
```

这不是说每层必然整齐对应一个人类概念，而是说 function composition 可以让后层重复利用前层形成的 features。
一个巨大 shallow lookup-like surface 与多层可复用 computation 都可能表示目标函数，后者在某些 compositional
tasks 上更紧凑。

UAT 与 Depth Separation 因而分别回答：

```text
纯线性 closure:
  为什么加深仍没有新函数类别？

UAT:
  非线性网络在足够容量下能逼近多广的函数？

Depth Separation:
  同一个函数用浅层和深层表示，参数规模可能差多少？
```

最完整的结论是：

> 线性层负责变换坐标，非线性让不同输入进入不同的局部计算区域，从而赋予网络通用函数逼近能力；深度再把这些非线性变换组织成可复用的层级组合，使某些复杂函数能够以远少于浅层网络的参数和计算来表达。

这条结论只关闭 representation-capacity 问题。梯度能否穿过深度、optimizer 能否找到解，属于本章前述
backpropagation/optimization 与第 17、28 章的稳定性问题；这些参数最终形成什么表示、为何泛化或失败，则由
下一章接手。

## 从算法到训练系统

公式里的一个更新步，在大模型训练中会展开成一条系统链路：读取并组织 batch，执行前向计算，保存或重算 activation，反向计算梯度，在设备间聚合或切分状态，更新参数，再定期评估和保存 checkpoint。

### Batch 与数据并行

当一个设备放不下所需 batch 或吞吐不足时，可以让多个 worker 处理不同 mini-batch 分片，再聚合梯度。数学上希望得到对更大 batch 的梯度估计，工程上却需要 collective communication、同步、故障处理和数据一致性。

worker 增加后，计算并不会无限线性加速。通信、straggler、拓扑和输入管道会逐渐成为瓶颈。有效 global batch 改变后，learning rate 和优化超参数也可能需要调整。分布式训练不是把单卡脚本复制多份，而是保持优化语义的同时改变执行图。

### Precision 与数值稳定性

较低 precision 可以减少显存和带宽，提升硬件吞吐，但梯度可能下溢、上溢或累积误差。Mixed precision 通常让高吞吐计算使用较低精度，同时让部分累加、缩放或主参数保留更高精度。

这再次说明“训练在跑”不等于“优化语义正确”。系统必须监控 loss、gradient norm、overflow、学习率和有效 token 数，否则硬件吞吐可能掩盖数值失败。

### 参数规模与状态切分

训练显存不只存权重，还包含梯度、优化器状态和 activation。参数规模扩大后，数据并行复制全部状态会触及单卡容量，进而需要 tensor parallel、pipeline parallel、ZeRO 或其他切分策略。它们改变参数和状态放在哪里、何时通信，但最终仍要实现与目标优化过程相容的更新。

### Checkpoint 与可复现性

一次 loss 下降只有在训练状态可追踪时才有工程意义。模型参数、优化器状态、scheduler、随机数状态、数据位置和并行配置都可能影响恢复语义。只保存最终权重可以用于推理，却未必足以继续训练或解释异常。

Part IV 会详细展开这些系统机制。本章要建立的连接是：梯度公式没有消失，它被映射成了 GPU 计算、显存状态、通信和容错问题。

## 训练成功为何不等于系统成功

第一，优化目标可能只是代理目标。模型忠实降低 loss，却可能钻指标空子，或忽略未被编码的安全、事实性和业务约束。

第二，训练数据只是总体分布的有限样本。经验风险低，不等于真实风险低，更不保证未来分布变化后仍然成立。

第三，训练可能存在数值或实现错误。错误的数据 masking、label shift、梯度缩放或分布式聚合，都可能生成看似平滑却语义错误的 loss 曲线。

第四，离线模型能力不等于在线系统能力。tokenizer、prompt template、quantization、runtime、sampling 和 context 都可能让线上行为偏离训练或评估环境。

因此，训练系统至少要同时观察 optimization health、evaluation quality 和 system correctness。单看训练 loss，是把“优化器完成了自己的工作”误当成“整个 AI System 达成了目标”。

## 本章在知识树中的位置

第 3 章把 `Data -> Training -> Checkpoint -> Evaluation` 定义为能力生产链。本章解释了 Training 节点的最小数学内核：参数化函数、loss、经验风险、梯度与 backpropagation。

第 5 章将沿着结果继续追问：参数更新后，中间表示到底编码了什么，为什么会记忆、泛化或在分布变化时失败。Part II 会展开具体模型结构，Part IV 会把本章的单步优化扩展为数据、并行、checkpoint 和后训练系统。

## 自检问题

1. `f_theta(x)` 中架构、参数、输入和输出分别扮演什么角色？
2. 经验风险与真实业务风险有什么区别？
3. 为什么 loss 是目标的代理，而不是任务价值本身？
4. representation capacity、optimization 和 generalization 为什么必须分开？
5. mini-batch gradient 为什么只是完整梯度的估计？batch size 会连接哪些系统约束？
6. Backpropagation 与 gradient descent 分别解决什么问题？
7. 为什么纯线性多层网络不能通过加深获得更强的函数类别？
8. ReLU 每个 activation region 内都线性，为什么整个网络仍是非线性的？
9. Universal Approximation 能支持什么结论，不能支持什么结论？
10. UAT 已说明单隐层足够时，Depth Separation 为什么仍然重要？
11. Representable、efficiently representable、optimizable 和 generalizable 有何区别？
12. mixed precision 为什么既是性能优化，也是数值正确性问题？
13. 为什么训练 loss 正常下降仍不足以批准模型上线？

## 小结

模型能够学习，不是因为网络会自发发现真理，而是因为我们构造了一个可微的参数化系统：数据提供经验，loss 把目标转成误差信号，backpropagation 计算每个参数对误差的影响，优化器据此反复更新参数。

这套机制强大，但边界清楚。函数可表示不等于解可找到，训练误差下降不等于未知数据上有效，离线优化成功更不等于生产系统可靠。保持这三层边界，后面讨论表示、Scaling Law 和大模型能力时才不会偷换概念。

## Review notes

本章只建立学习与优化的基础，不承担完整泛化理论，也不提前进入 Transformer 细节。后续 Review 应检查所有数学符号是否先定义，再检查每个工程概念是否仍能回到 batch、precision、state 或 communication，而不是变成分布式训练框架清单。

优先核验入口：

- David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams, "Learning representations by back-propagating errors", Nature, 1986: https://www.nature.com/articles/323533a0
- George Cybenko, "Approximation by superpositions of a sigmoidal function", 1989: https://link.springer.com/article/10.1007/BF02551274
- Kurt Hornik, Maxwell Stinchcombe, Halbert White, "Multilayer feedforward networks are universal approximators", 1989: https://doi.org/10.1016/0893-6080(89)90020-8
- Moshe Leshno et al., "Multilayer feedforward networks with a nonpolynomial activation function can approximate any function", 1993:
  https://doi.org/10.1016/S0893-6080(05)80131-5
- Matus Telgarsky, "Benefits of depth in neural networks", 2016: https://arxiv.org/abs/1602.04485
- Ronen Eldan, Ohad Shamir, "The Power of Depth for Feedforward Neural Networks", 2016:
  https://arxiv.org/abs/1512.03965
- Yann LeCun, Yoshua Bengio, Geoffrey Hinton, "Deep learning", Nature, 2015: https://www.nature.com/articles/nature14539
