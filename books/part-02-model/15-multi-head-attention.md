# 第15章 Multi-Head Attention

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-MULTI-HEAD-ATTENTION`
**Legacy Chapter:** Ch15
**Status:** Draft

**Roadmap Intent:** 为什么需要多个注意力头，从不同子空间捕捉关系。

## 本章要回答的问题

第14章的单个 Attention head 已能让 token 按内容读取上下文，为什么还需要多个 head？Multi-Head Attention 如何在多个投影子空间并行建立关系，又为什么会演化出 MQA 和 GQA？

本章的核心判断是：**Multi-Head Attention 不是重复计算同一份注意力，而是让多个可学习投影并行构造不同路由子空间，再把这些结果组合回统一 hidden state。**Head 数增加了表达路径，也增加了投影、layout、KV state 与并行约束。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`d_model` 表示 hidden dimension，`H` 表示 Query head 数，`H_kv` 表示 Key/Value head 数，`d_h` 表示单个 head dimension。

## 单个 head 的表达瓶颈

一个 head 对每个 Query 只产生一行归一化权重，并用同一套 Q/K/V projection 决定所有关系。它可以同时给多个位置分配权重，但全部匹配共享一个子空间和一套 score 几何。

序列中可能同时存在不同关系：

- 局部搭配与远距离依赖。
- 语法主从关系与实体指代。
- 内容相关 token 与格式边界。
- 当前位置的多种候选读取策略。

朴素方案是把单 head 的维度做得更大。容量增加了，但所有关系仍竞争同一个 score matrix。Multi-Head 的思路是让模型并行学习多组投影，每组独立产生 attention distribution。

## 从单头投影到多个 head

输入保持：

```text
X shape = [B,T,d_model]
```

常见配置满足：

```text
H * d_h = d_model
```

但这是常见设计，不是数学必然。可将大投影矩阵写为：

```text
W_Q [d_model,H*d_h]
W_K [d_model,H*d_h]
W_V [d_model,H*d_h]
```

投影后 reshape 和 transpose：

```text
Q = X W_Q -> [B,T,H*d_h] -> [B,H,T,d_h]
K = X W_K -> [B,T,H*d_h] -> [B,H,T,d_h]
V = X W_V -> [B,T,H*d_h] -> [B,H,T,d_h]
```

每个 head 独立执行第14章的公式：

```text
head_h = softmax(Q_h K_h^T / sqrt(d_h) + M) V_h
head_h shape = [B,T,d_h]
```

所有 heads 合在一个张量中：

```text
heads shape = [B,H,T,d_h]
```

## Concat 与输出投影

Head outputs 不直接相加，而是先把 head 维移回 token 后面，再 concat：

```text
[B,H,T,d_h]
-> transpose [B,T,H,d_h]
-> concat    [B,T,H*d_h]
```

随后使用 output projection：

```text
W_O [H*d_h,d_model]
Y = Concat(head_1,...,head_H) W_O
Y shape = [B,T,d_model]
```

`W_O` 让不同 heads 的信息重新混合，并把输出恢复到 residual stream 的 `d_model`。如果简单平均 heads，会提前丢失“哪部分信息来自哪个投影子空间”的自由度。

保留 concat 并不要求输出混合一定使用任意可学习的稠密矩阵。若参数和执行预算先触及边界，可以保留 Q/K/V 与各 head 的内容路由，把输出改为固定的全局混合 basis，再学习逐通道 scale 与 bias，例如 `alpha ⊙ (Y H) + beta`。固定 Hadamard 型变换用加减法组织混合，取消的是 `W_O` 的任意矩阵自由度，而不是把多个 head 平均成一个，也不减少 attention score 的 `T²` 项。basis、归一化、支持的维数和具体 kernel 都属于新架构的执行合同；固定变换可逆不代表任意已训练 `W_O` 能无损替换，后续 affine 也不恢复任意矩阵的表达范围。<!-- source-family:SF-2026-ARXIV-2603-08343 -->

这个分支用更小的可学习混合空间换取参数与算术预算，同时要求其余投影在训练中适应固定 basis。实际收益仍须比较质量、训练时间和完整推理路径，而不能把算术复杂度降低直接写成加速保证。[受限实现与评价](https://arxiv.org/html/2603.08343v1)只在较小训练模型上检验质量，较大随机初始化配置的执行测量不证明同规模模型已训练可用；小配置存在速度反侧，成熟 GEMM 与尚未优化的变换实现也可能抵消理论节省。任务需要更自由的 head 重组、维数或 kernel 不支持、质量或总时间回归时，保留稠密 `W_O`。这与下面扩大匹配空间的设计是不同预算分支，不能共用一项表达力或速度结论。

输出投影混合已经聚合好的 head；若要改变 softmax 之前谁能与谁匹配，就需要另一种接口。一条受限分支先在 head 轴分别线性混合 Q/K/V，给每个 head 生成 P 组 pseudo-tokens，再把原长度 N 交错成 NP 个虚拟位置，按这些位置执行 causal attention 与 RoPE。这不是增加输出 W_O，也不是 GQA 减少 KV heads；它扩大匹配空间，同时把全局 attention 的每 head 工作量推到 O(P²N²d)。[必要机制与预算控制](https://arxiv.org/html/2602.21371v1#S4)通过局部窗口/周期性全局层约束比较预算，但 FLOP 近似匹配和 FlashAttention 兼容不等于 KV、位置编码、训练或延迟免费。无位置的代数包含关系也不授旧 RoPE checkpoint 无损转换；有限任务有反退，预算紧或改动接口未验收时仍保留 MHA/GQA，而不把更多可表达关系当成已学可靠算法。<!-- source-family:SF-2026-ARXIV-2602-21371 -->

## 一个两 head 小例子

设 `d_model=4`、`H=2`、`d_h=2`。某个 token 在两个 heads 聚合后的输出分别为：

```text
head_1 = [1.0, 0.0]
head_2 = [0.2, 0.8]
```

Concat 得到：

```text
z = [1.0, 0.0, 0.2, 0.8]    shape [4]
```

若为了演示令 `W_O` 为 `4x4` identity，最终输出就是 `z`。真实训练中的 `W_O` 会学习如何混合这四个分量。这个例子说明 heads 的输出被保留后再组合，而不是先压成一份平均结果。

多个 heads 是否真的分别对应“语法头”“指代头”，需要实验验证。可视化某个 attention pattern 只能提供行为线索，不能保证每个 head 有稳定、单一的人类概念。

## Head 怎样分化，又为什么会冗余

`H` 是训练前写进架构的超参数，不是模型先观察问题、再像 MoE router 一样动态决定要启动多少个 heads。标准 MHA/GQA 的一次 forward 会生成全部 Query heads，并沿 checkpoint 固定的分组执行 Attention；MoE router 选择的是 FFN Experts，不能替代 Attention head 的路由语义。

不同 heads 接收同一批 token、服务同一个最终 loss，但各自拥有不同投影参数，并通过不同 score matrix、concat 位置与 `W_O` 路径接收梯度。随机初始化和训练过程会打破完全对称，使它们可能形成互补路由；这不是“每个 head 被分配一个领域”的监督，也不保证最终彼此独立。即使初始化时令投影近似正交，联合优化也可以再次把它们推向相关子空间。

因此，多头结构提供的是**可分化的表达路径**，不是 `H` 份必然有效的独立能力。已有剪枝研究表明，特定训练模型和任务中的一些 heads 可在较小质量变化下移除；这能证明冗余可能存在，却不能推出所有层、所有输入都有同一组“无效 heads”，也不能把 post-hoc 分析直接等同于生产加速。真正跳过 head 需要训练期 pruning、gating 或稀疏执行 contract，并让 checkpoint、kernel 与评估共同支持。

BOS 上的注意力概率质量集中只是一个诊断模式，移除某个 head 对当前任务影响小，也不证明它永远没有可训练容量。资源允许时，可以把定点恢复作为 pruning/gating 之外的替代分支：重初始化选中 head 的 Q/K/V 投影，将其 output projection 置零以降低初始残差扰动，再冻结其他参数，只对目标参数短训。[BLOOM 的受限实验](https://arxiv.org/html/2603.09616v1#S3)支持这条方法分支，而不证明所有 sink 都源于同一位置病因或所有被剪 heads 都值得恢复。冻结权重也不冻结共享 residual stream 的输入，目标头改变后，未改头的 attention 行为仍可能漂移，因此干预验收不能只看选中 heads。<!-- source-family:SF-2026-ARXIV-2603-09616 -->

恢复的诊断容量与最终任务效用必须分账：按 BOS mass 阈值重新变“健康”，不等于 held-out 质量、语言分布和真实任务保持。该实验的完整手术只在 BLOOM-1b7 上验证，出现 held-out perplexity 上升和生成语料印记；额外健康头的单 seed、单列瞬时训练 loss 改善也不能签发通用收益。训练语料、阈值、短训预算与全模型回归均有成本，原文斜率公式/表与“高索引斜率更陡”的归因冲突不在这里采用。质量回退或预算无法摊销时，保留原 heads，或继续采用已验证的 pruning/gating 与实际执行路径，而不是用一张 head-health 图替代质量验收。<!-- source-family:SF-2026-ARXIV-2603-09616 -->

head的干预单位也不必是整个输出上的固定方向。一个受限分支分别拟合可信与扰动activation的混合分布，离线按运输耦合选择目标component，在线依据当前membership实施局部均值修正。[Scalpel的必要机制](https://arxiv.org/html/2602.09541v1)由此区分component概率调节与全head平移；row argmax的映射不是在线执行完整Schrödinger bridge，membership或熵也不是答案truth。组件拟合、probe选择与离线耦合均付费，有限POPE二值人口、head选择和自适应输入仍影响结果，部分模型/切片有反侧。分布漂移或效用回归时应降低/关闭干预，保留原attention与独立输出验证，不由局部混合模型签发事实或安全性。 <!-- source-family:SF-2026-ARXIV-2602-09541 -->

## 为什么 head 数不是越多越好

给定固定 `d_model`，增加 `H` 通常会减小 `d_h`。更多 heads 提供更多独立路由分布，但每个 head 的表示维度更小。

Head 数还受工程条件约束：

- `H*d_h` 与 projection shape 必须匹配。
- Q/K/V reshape 和 kernel 要支持目标 layout。
- Tensor Parallel 常要求 head 数能被并行度整除。
- Head 太小可能降低 GEMM 或 attention kernel 效率。
- Head 太多会增加 metadata、调度和 KV head 选择复杂度。

因此 `H` 是模型容量、每头维度与执行效率的联合选择。

把多个 heads 放进同一 fused kernel，可以减少中间存储与启动成本，却不能据“最后只有一个聚合输出”就假定任意 dense 多头、跨层计算都能按实例数摊薄。单个 head 难算，不自动证明 `L×H` 个实例同样难算；这需要单独的 direct-sum 论证。[受限理论构造](https://arxiv.org/abs/2603.11332v1)把独立问题编码到各 head 与层，在 sum-aggregation、每 head 宽 `m=Θ(log N)`、`L/H` 与序列长度 `N` 多项式相关、逐项输出误差至多 `1/(10N)` 时，给出基于 3-OV/SETH 假设的 `LHN^(2−o(1))` 最坏情形时间下界。它不是各 head 必须串行的调度定理；concat 推广还要重参数化宽度，不能直接拿论文的 `m` 代替固定 `d_model` 下的 `d_h`，更不证明每个已训练 checkpoint 都没有冗余。<!-- source-family:SF-2026-ARXIV-2603-11332 -->

大宽度分支则把完整 softmax 计算与多个独立矩阵乘积联系起来：允许实数加减乘除及 `exp/ln` 的扩展算术电路，可通过同量级成本抽取偏导恢复各乘积。其 `m=Θ(N)` 构造得到 `LHN^(ω−o(1))−O(LHN²)` 的电路规模下界，其中 `ω` 是矩阵乘法指数，`ω>2` 时前项才支配减项；对象是所有输入与可变权重的精确计算，不是推理时需要执行反向，也不是 Word-RAM、有限精度或生产延迟下界。Full-attention、宽度和最坏情形条件不能自动搬给 causal mask、共享 KV 或实际数据分布。因此，保持原 dense 算子时仍可通过融合、layout 和并行改善常数与 IO；省略计算则须明确近似误差、结构、共享或剪枝合同，并验收质量与总成本。条件不符时保留成熟 dense MHA/GQA，不把理论下界解释为所有加速都不可能，也不让不同计算模型下的一项速度测量反证该定理。

## MHA、MQA、GQA 为什么出现

标准 Multi-Head Attention 中 Query、Key、Value 都有 `H` 个 heads：

```text
MHA: H_q = H_kv = H

Q [B,H,T,d_h]
K [B,H,T,d_h]
V [B,H,T,d_h]
```

自回归推理中，每个 KV head 的历史 K/V 都要进入 KV Cache。为了减少 cache 和 memory bandwidth，可以让 Query heads 共享较少的 K/V heads。

Multi-Query Attention：

```text
MQA: H_q = H, H_kv = 1

Q [B,H,T,d_h]
K [B,1,T,d_h]
V [B,1,T,d_h]
```

Grouped-Query Attention：

```text
GQA: H_q = H, 1 < H_kv < H

Q [B,H,T,d_h]
K [B,H_kv,T,d_h]
V [B,H_kv,T,d_h]
```

GQA 把 Query heads 分组，同一组共享一个 KV head，在 MHA 表达自由度与 MQA cache 效率之间折中。

这里的“共享”是一项架构约束与 inductive bias，不是先证明组内若干 KV heads 数学上相似，再做无损合并。从头训练 GQA 时，每组从一开始就只有一套 `W_K/W_V`，Query heads 会共同适应该表示；把既有 MHA checkpoint 转成 GQA 时，才需要聚合旧 K/V projections 并继续训练，转换结果也不是 runtime 等价改写。

MQA 把约束推到极端：不同 Query heads 仍能产生不同 attention weights，决定“查哪些位置”，但所有 heads 共用同一套 Key 索引特征和 Value 内容表示。GQA 保留多个 KV groups，使不同组还能学习不同的“怎样被匹配”和“取回什么”。所以从 MHA 到 GQA 再到 MQA，是 `H_kv`、KV 带宽与表示瓶颈之间的连续取舍，不是发现所有 KV heads 都相似后的必然终点。

## 一个 GQA 分组例子

假设：

```text
H = 8
H_kv = 2
```

则每个 KV head 服务 4 个 Query heads：

```text
Q heads 0..3 -> KV head 0
Q heads 4..7 -> KV head 1
```

相较 `H_kv=8` 的 MHA，K/V projection 与 cache head 数下降到四分之一。Query 计算仍有 8 个 heads，模型没有减少 Query 路由数。

这不是 runtime 可对任意 MHA checkpoint 无损打开的选项。`H_kv` 决定模型参数 shape 和训练语义，必须由架构与 checkpoint 支持。

## 参数与 KV 状态的连接

忽略 bias，标准 MHA 的四个 projection 参数近似为：

```text
P_MHA ~= 4 * d_model^2
```

这里假设 `H*d_h=d_model`。GQA/MQA 主要减少 K/V projection 输出维度，Query 与 output projection 不一定减少同样比例。

推理 KV Cache 的核心 head 维度则由 `H_kv` 决定：

```text
KV elements per layer ~= 2 * B * T * H_kv * d_h
```

第19章会加入 layer 数 `L`、dtype bytes 和请求生命周期，完整推导 cache 容量。本章只建立模型架构到 `H_kv` 的接口。

## Multi-Head 与 Tensor Parallel

Attention projection 的 head 维度提供自然切分边界。不同 GPU 可以持有不同 Query/KV heads，局部计算后再在 output projection 周围聚合。

但不能简单认为“一张卡一个 head”。实际 Tensor Parallel 会考虑矩阵 column/row partition、GQA 的 KV replication、head divisibility 和 collective placement。第37章负责完整 TP 机制；本章只指出模型 head layout 会约束并行布局。

## 从共享 KV 到可执行的压缩状态

减少 KV heads 回答了总状态有多大；分布式部署继续追问每个设备究竟要持有、读取多少状态。因而下面两条路线是不同约束下的架构分支，不是 MQA 必然继续替代 GQA 的下一代。

### 压缩状态还必须暴露可执行的分片轴

MQA、GQA 与低秩 KV 压缩都试图减少每个 token 留下的状态，但“总状态更小”不等于“每个设备读取的状态也按并行度下降”。把全部 KV heads 压进一个共享 latent state，在单卡或较小 Tensor Parallel 下很合理；当 Decode 受每个 rank 的 HBM 带宽限制时，这个共享对象却可能需要在每个 rank 复制，形成新的 bandwidth floor。

因此架构压缩还要回答一个运行时问题：压缩后的坐标是否保留了可以映射到设备的 partition axis。一条可行演进是把单个 latent state 分成多个独立 latent heads，每个 head 在本地完成上投影和 Attention，再在输出边界聚合：

```text
shared latent KV
-> multiple latent heads
-> head-to-rank placement
-> local projection and attention
-> output aggregation
```

它以更多 projection、聚合、初始化耦合和 checkpoint/kernel 复杂度，换取 per-rank KV 读取随并行度缩减的可能。增加 latent heads 还会改变多路求和的 variance，不能被当作纯 layout rewrite。反过来，在 TP 较小、通信比 HBM 读取更贵或成熟 kernel 更重要时，单 latent MLA、GQA 乃至 MHA 仍可能是更好的设计。

这里的长期原则是：**模型状态的 shape 同时定义表达空间和系统可分片性。**第37章负责实际 placement 与 collective；本章只负责确保模型架构没有在压缩状态时无意删除运行时所需的切分维度。


### 同一 Attention 权重可以暴露多条 KV 路径，但前提必须在训练时成立

分片轴处理的是跨设备布局；另一类约束来自同一模型在不同硬件上会遇到不同的计算/带宽比例，此时才需要考虑多条预先训练并验证的执行路径。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-15250:start -->
普通 MHA、GQA 与 MQA checkpoint 的投影形状不同，runtime 不能在部署时把它们当成可无损互换的 cache policy。GQLA 的条件分支是在模型设计与训练阶段建立共享权重，使同一 checkpoint 同时支持 MQA-absorb 的 compact-cache 路径和 per-group GQA 的 expanded-cache 路径；runtime 再依据 hardware roofline、Tensor Parallel 布局与当前 memory/compute 压力选择已验收的执行视图。模型权重拥有语义，runtime 只拥有路径选择，不能现场发明新的 attention factorization。

多路径身份必须绑定 checkpoint、group/repetition factor、projection transformation、precision、TP layout 与路径校验结果。compact path 节省 KV 却可能增加 compute，expanded path 反之；训练/转换成本和双路径回归也随之增加。exact-v1 只支持 §3 的 GQLA/TransGQLA 与 §4–5 所测模型和硬件，不证明任意既有 checkpoint 可无损改写。roofline 未校准、路径数值不一致或实现只支持一种布局时，应回退冻结的 MHA/GQA/MQA 单一路径。<!-- source-family:SF-2026-ARXIV-2605-15250 -->
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15250:end -->


## 怎样区分路由分工、参数坐标与行为证据

到这里，多头结构的计算与状态代价已经明确，但一个 head 究竟做了什么，还不能仅由数量、可视化或参数值读出。下面区分三类容易混淆的问题：路由是否有用、训练动力学是否独立，以及参数坐标是否唯一。

### 注意力图与平均传播只是诊断线索

注意力图中看起来不同的读取模式，首先只是待验证的行为线索。把这类诊断量直接变成训练目标，还会改变它原先作为线索的意义。例如，放大 matched 与 mismatched demonstrations 的注意力行距离，可以仅通过把权重集中到不同格式 token 而接近指标上限，并不保证取回了与答案有关的 Value。因而“路由对上下文更敏感”与“模型更会利用上下文”必须由独立行为对照区分；训练代理、测量代理与最终能力验收不能互相替代。这不否定注意力分析，而是要求被直接优化的解释指标重新接受行为检验。

平均 attention 可以解释群体表征传播趋势，但 context-specific routing 与 value computation 位于对平均的 deviation 中；把 mean-field fit 当成单个输入的机制解释，会掩盖稀有 head、token 和样本路径。<!-- source-family:SF-2026-ARXIV-2609-16382 -->

统计分解提供诊断视角，不等于因果证明。有限 corpus/model 且部分 family 需单独处理；个例、安全或精确 attribution 场景应回退真实 activation measurement、ablation 与干预。

### 几何分离不等于训练独立

即使进一步约束各 head 的 score 或输出方向近似正交，也不能推出它们的训练动力学彼此独立。各 head 仍读取同一 token trajectory，并在共享 residual stream 与最终 loss 中相遇；球面归一化下的径向投影还会把一个 head 的更新影子带入另一个 head 的能量变化。因而，总体能量存在下降方向，不代表每个 head 的局部能量或聚类过程都单调。只有在额外的 Radial Dominance 等充分条件成立时，才能把更强的逐 head 单调性当作理论结论，而不能把它写成真实 Transformer 的普遍事实。<!-- semantic-body-binding:SF-2026-ARXIV-2605-04279 -->

这条边界没有否定 head 正交化：它仍可作为减少表示重叠的 inductive bias。代价是新增约束与优化耦合，且“几何上更分离”仍需任务行为、因果干预和可执行 kernel 分别验收。相关理论主要依赖 sphere-normalized、score symmetry、scalar 或 equiangular 等受限设定，不证明 heads 已获得独立人类功能；条件不成立时，应回到联合系统的 loss、residual state 与端到端行为，而不是据单 head 能量作提交判断。

### 换基等价不等于功能冗余

另一个层次的冗余发生在同一 head 的参数坐标内部，而不是多个 heads 做了相同工作。以下 `W_Q/W_K/W_V` 均指该 head 对应的投影块，而非前文全部 heads 合并后的大矩阵。暂不加入位置旋转和 bias，沿本章行向量记法，任取可逆的 `d_h × d_h` 矩阵 `S`，令 `W_Q' = W_Q S`、`W_K' = W_K S^{-T}`，则 `W_Q' W_K'^T = W_Q S S^{-1} W_K^T = W_Q W_K^T`，所以全部输入的 score 与 attention weights 不变。Value 与该 head 对应的输出块 `W_O^(h) [d_h,d_model]` 也有类似换基：`W_V' = W_V R`、`W_O^(h)' = R^{-1} W_O^(h)`。参数可以不同，执行的函数却相同；这叫参数化的不唯一性，不能据单个坐标大小给特征赋予唯一语义。

这种换基不会自动减少 heads、矩阵 shape 或 FLOPs，也不保证优化器按相同轨迹训练。GQA 共享 K/V 后，组内换基必须共同兼容共享参数；RoPE 又要求变换保留位置旋转结构，不能套用任意可逆矩阵。因此，可辨识程度、head 功能冗余与可兑现的推理加速是三个不同问题：前者要固定参数等价关系，后两者仍须任务因果验证与 checkpoint/kernel 合同。第16章的非线性 FFN 也不能照搬这里两个线性因子的任意换基。[受限证据：QK/OV 因子化与共享结构约束，arXiv:2609.01231v1 §4](https://arxiv.org/html/2609.01231v1)

### 从观察 Head 到有条件地干预轨迹

理解参数等价关系之后，还要区分“解释一个 head”和“修改它来改善输出”。后者多了一份干预收益与副作用都必须验证的责任。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21770:start -->
固定 activation steering 对所有生成步骤施加同一方向，在错误模式稳定时实现简单；若错误表现为特定 attention head 沿轨迹偏离低维 correctness manifold，这种全程干预会同时扰动原本正确的步骤。一个条件分支把 head-to-manifold distance 当作 trajectory sensor，只在越过校准阈值时把状态投影回已学子空间。距离只拥有 intervention proposal，端到端 verifier 才拥有正确性判定。

该分支需要白盒 activation、对比轨迹、子空间和阈值校准，并增加逐步监测开销；过强投影会损坏正确轨迹。exact-v1 的受测模型、任务和 head 不能证明 correctness manifold 跨模型稳定，也不能把 proximity 当作 correctness certificate。head/任务漂移、阈值失校或 utility regression 超界时，应关闭投影，回退无 steering、较弱静态 steering 或外部 verifier-guided retry。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21770:end -->

多语言任务还要把语言形式与答案内容作为两个干预目标，而不是给所有失败共用一个“正确性方向”。一条受限诊断分支分别构造含义相同但语言错误的输入、语言正确但含义被破坏的输入，再将干净轨迹的 head activation patch 回对应条件；在 teacher-forced 的参考输出前缀上比较预测变化，用来选择后续 steering 候选。两种 corruption、参考前缀及观察 token 位置共同定义 sensor，不能把位置间的 KL 差或可干预性直接称为模型自然使用的唯一语言无关 code。部署时应分别验语言遵循与内容正确性，定位有效也不保证自由生成有效：[必要机制与反侧](https://arxiv.org/html/2602.04613v1)中 token 0 也可能有用，低资源语言和较强缩放仍会失败。对比构造、白盒 patch、位置与强度校准增加成本；目标与 utility 验收不成立时，关闭该干预，回退显式语言指令、较弱 steering 或无 steering，而不继承普遍的少量 head 控制保证。<!-- source-family:SF-2026-ARXIV-2602-04613 -->

干预粒度也不一定是整个 head 或整层向量。用列向量记法写线性输出 `y = Σ_i x_i W[:,i]`，每项由一个输入 scalar 与对应权重列组成；它与本章行向量 `x W` 的记法互为转置，这种 activation unit（AU）不是 neuron、head 或 SAE feature 的同义词。一条受限分支先在目标/非目标对比输入中按 activation 差的符号一致性选 AU，再按排名给当前输入 scalar 施加 `x_i → (1+γ_i)x_i` 的缩放。排序只是干预候选，不识别唯一内部因果；负向 γ 足够大时 `1+γ_i` 可以为负，不能称为保符号控制。对比 pairs、矩阵/层坐标、选择数 k 与强度 α 都需要任务内校准，细粒度选择仍增加定位和监测成本，也可能伤害无关能力；更少单元不保证更好。独立目标与 utility 回归失效时应关闭该分支，回退无 steering、较弱粗粒度 steering 或外部 verifier，而不由受限激活排序签发功能控制保证。<!-- source-family:SF-2026-ARXIV-2602-04428 -->


## 本章在知识树中的位置

```text
Single-head Self Attention
-> H parallel routing subspaces
-> concat [B,T,H*d_h]
-> output projection [B,T,d_model]
-> MHA / GQA / MQA
-> Transformer Layer / KV Cache
```

第14章定义单 head 路由，本章定义多 head 组合。多个位置的信息已经汇入当前位置，但还需要在这个位置内部组合特征、形成非线性变换；第16章接手这一问题，第17章再将两者组成完整 layer。第19章使用本章的 `H_kv` 推导运行时状态。

## 自检问题

1. 把单 head 维度做大与增加多个 heads 有什么结构差异？
2. Q/K/V 怎样从 `[B,T,d_model]` reshape 为 `[B,H,T,d_h]`？
3. 为什么 head outputs 先 concat 再经过 `W_O`？
4. 固定 `d_model` 时，增加 `H` 会怎样改变 `d_h`？
5. MHA、MQA、GQA 的 `H_kv` 分别是多少？
6. `H=8,H_kv=2` 时 Query heads 如何分组？
7. GQA 主要减少哪部分参数和运行时状态？
8. 为什么 runtime 不能为任意 checkpoint 无损切换 MHA 到 MQA？
9. Head layout 为什么会约束 Tensor Parallel？
10. Attention head 的可视化为什么不等于完整机制解释？
11. 为什么同一 loss 可以让 heads 分化，却不能保证每个 head 都独立有效？
12. GQA 的共享为什么是训练约束，而不是组内 KV 相似性的定理？

## 小结

Multi-Head Attention 让多个投影子空间并行构造上下文路由，再通过 concat 和 output projection 恢复统一 residual stream。它扩展了单 head 的表达路径，同时引入 head dimension、layout 与并行约束。

MQA 和 GQA 进一步把 Query head 数与 KV head 数解耦，用共享 K/V 换取更低 KV Cache 和 memory bandwidth。这条模型架构选择会在第19章变成具体推理容量。

## Review notes

- `SF-2026-ARXIV-2603-11332` — 2026-03-14 补查；[exact-v1 PDF](https://arxiv.org/pdf/2603.11332v1) §2.1–2.2/Definitions2.7–2.8、Theorems3.1/4.4/5.1、必要梯度抽取接口、§6与AppendixC。2+2+2=6，具体长期缺口定点深入；sum/concat宽度重参数化、1/(10N)逐项误差、可变W/X、exact-real eAC及减项保留，不授causal/GQA、Word-RAM、硬件延迟或固定checkpoint保证。mar14_supplement 必要Source/实际owner提案与root实际独立原证/完整H选择至MHA邻接通过后窄写；mar14_supplement 已实际回对必要原证并顺读新增正文、完整局部邻接及本人末注，非writer POST通过、窄锁释放，不授日级完成。未核代码或复现，不重复推导全部证明。

- `SF-2026-ARXIV-2603-09616` — Daily `2026-03-12`补查；[exact-v1](https://arxiv.org/html/2603.09616v1) §3、§4.1–4.7、§5.1–5.5/Appendix B–C。2+1+3=6，中心位置归因反侧额外深入；只采用目标 QKV 重初/output 置零/gradient mask 短训与冻结参数不冻结共享输入的条件分支。health/任务效用分账、held-out 与语料印记反侧、单 seed 与有限模型边界近文；斜率公式/表冲突隔离。C4 validation split 用于训练，Table3 所谓 held-out 样本划分未由本轮实现核验，不把局部 PPL 写作独立泛化认证。未执行代码/复现实验；必要 Source 与逐字 PRE 由非作者 review_mar12 实际核通过；root 窄写后 review_mar12 已实际顺读新正文、完整局部邻接与自身末注并回对必要原证，POST 通过，不授日级完成。

- `SF-2026-ARXIV-2602-21371`：exact-v1 §4、实验与local/global预算说明；只采用softmax前head混合/虚拟位置与P²成本分责。图示和方法window缩放不同，不混用；理想无position证明不授RoPE转换，未核实现或复现。 非原 packet 作者必要原证/actual owner PRE 与窄写完成；root 已实际顺读正文、完整邻接与自身末注，POST 通过。

本章只扩展多头结构，不重复第14章 softmax 小例子，也不提前展开第19章完整 KV Cache 容量。后续 Review 应继续区分 Query head 与 KV head，并以 checkpoint config 核验 `H`、`H_kv` 和 `d_h`。

- `SF-2026-ARXIV-2605-04279`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2605.04279v1) 支持在论文假设下区分总能量梯度流、per-head monotonicity 与 radial-shadow coupling；Radial Dominance 是充分条件。证据不支持把受限动力学外推为任意真实 Transformer 的 head 独立性、功能分工或训练保证。

Primary-source 校验入口：

- Attention Sensitivity Is Not Enough（Status: Experimental）：https://arxiv.org/html/2609.00064v1 。§3–5 的单模型受控实验支持注意力代理优化与行为改善不等价；分离 regularizer/evaluation loader 后仍须保留单模型、主要单 seed 与有限任务边界，不据此声称全部 in-context learning 消失或某一种 anchoring 独有优势。

- Multi-Head Low-Rank Attention（Status: Experimental）: https://arxiv.org/abs/2603.02188

- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
- Paul Michel et al., "Are Sixteen Heads Really Better than One?", 2019: https://arxiv.org/abs/1905.10650
- Noam Shazeer, "Fast Transformer Decoding: One Write-Head is All You Need", 2019: https://arxiv.org/abs/1911.02150
- Joshua Ainslie et al., "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints", 2023: https://arxiv.org/abs/2305.13245

- `SF-2026-ARXIV-2602-04428` — Daily `2026-02-06`；[AUSteer exact-v1](https://arxiv.org/html/2602.04428v1) §3–5及Appendix B/C，2+2+2=6，仅对 scalar-granularity steering 与成本边界的具体缺口深入。AU 是输入 scalar × 权重列，contrastive sign-consistency 与排名缩放不证明 neuron/head/SAE 等价或内部唯一因果；负缩放不授保符号，k/α 任务相关，部分 utility 切片退步保留。激活数量与跨实现 baseline 不作端到端速度证据，不采用普遍 fewer-is-better 或全附录理论。root 必要原源→具体 owner 已核并授窄锁；root 实际正文/279–299前后邻接及341源注 POST 通过，日级 Gate 待验，未复现实验。

- `SF-2026-ARXIV-2602-04613` — Daily `2026-02-06`；[Meaning and Language exact-v1](https://arxiv.org/html/2602.04613v1) §3–6。原2+2+2=6，具体双corruption × teacher-forced观察位置接口缺口深入；语言/含义分别构造与输出验收，patch/位置KL不授唯一内部code或普遍1%控制。token0、低资源语言、强α及utility反侧和白盒校准成本保留。未运行代码或复现；root实际必要原源/owner写前通过，root实际Ch15 275–301含287新段及345末注POST通过，日级Gate未验。

- `SF-2026-ARXIV-2602-09541` — Daily `2026-02-12`补遗漏；[exact-v1](https://arxiv.org/html/2602.09541v1)。本日具名必要方法、关键评价与直接反侧由root独立Source限定通过，actual owner/局部邻接及逐字拟文PRE通过后授窄锁；作者已写最小差额，review_20260214非作者实际新正文、完整局部邻接及本人末注POST通过，窄锁释放，不授DAY。原件与配置/中心争议边界见本日同名前缀review笔记；未核artifact或复现。

- `SF-2026-ARXIV-2603-08343` — Daily `2026-03-11`补遗漏；[exact-v1](https://arxiv.org/html/2603.08343v1) §4–6：固定 head-mixing basis 与可学习 affine 是改变架构自由度的替代分支，不是任意 checkpoint 的等价替换。保留小模型质量范围、随机初始化大配置与实际 kernel 成本边界；root 已读必要方法、评价与反侧，并核 Ch14/16 交接后写入正文。非写入者 supplement_20260311 已实际回对原证并顺读新增两段、完整局部邻接与末注，写后复核通过，不授日级完成；未运行代码或复现实验。
