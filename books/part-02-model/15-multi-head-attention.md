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

## 为什么 head 数不是越多越好

给定固定 `d_model`，增加 `H` 通常会减小 `d_h`。更多 heads 提供更多独立路由分布，但每个 head 的表示维度更小。

Head 数还受工程条件约束：

- `H*d_h` 与 projection shape 必须匹配。
- Q/K/V reshape 和 kernel 要支持目标 layout。
- Tensor Parallel 常要求 head 数能被并行度整除。
- Head 太小可能降低 GEMM 或 attention kernel 效率。
- Head 太多会增加 metadata、调度和 KV head 选择复杂度。

因此 `H` 是模型容量、每头维度与执行效率的联合选择。

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

本章只扩展多头结构，不重复第14章 softmax 小例子，也不提前展开第19章完整 KV Cache 容量。后续 Review 应继续区分 Query head 与 KV head，并以 checkpoint config 核验 `H`、`H_kv` 和 `d_h`。

- `SF-2026-ARXIV-2605-04279`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2605.04279v1) 支持在论文假设下区分总能量梯度流、per-head monotonicity 与 radial-shadow coupling；Radial Dominance 是充分条件。证据不支持把受限动力学外推为任意真实 Transformer 的 head 独立性、功能分工或训练保证。

Primary-source 校验入口：

- Attention Sensitivity Is Not Enough（Status: Experimental）：https://arxiv.org/html/2609.00064v1 。§3–5 的单模型受控实验支持注意力代理优化与行为改善不等价；分离 regularizer/evaluation loader 后仍须保留单模型、主要单 seed 与有限任务边界，不据此声称全部 in-context learning 消失或某一种 anchoring 独有优势。

- Multi-Head Low-Rank Attention（Status: Experimental）: https://arxiv.org/abs/2603.02188

- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
- Paul Michel et al., "Are Sixteen Heads Really Better than One?", 2019: https://arxiv.org/abs/1905.10650
- Noam Shazeer, "Fast Transformer Decoding: One Write-Head is All You Need", 2019: https://arxiv.org/abs/1911.02150
- Joshua Ainslie et al., "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints", 2023: https://arxiv.org/abs/2305.13245
