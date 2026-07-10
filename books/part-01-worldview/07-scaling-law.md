# 第7章 Scaling Law 为什么成立

**Knowledge Tree:** Part I 世界观：AI 为什么会发展成今天这样
**Status:** Draft

**Roadmap Intent:** 理解参数、数据、算力之间的经验规律，以及为什么规模会带来能力跃迁。

## 本章要回答的问题

为什么扩大模型、数据和训练算力时，language modeling loss 往往呈现相对平滑、可拟合的下降规律？这种规律能指导什么决策，又为什么不能保证某项能力必然出现？

本章的中心命题是：**Scaling Law 是在特定模型族、数据分布、训练方法和观测范围内得到的经验性 power-law regularity。它能描述资源增加时 loss 的统计趋势，并帮助分配有限 compute，但不是能力增长的自然定律，更不是无限扩大的保证书。**

## 为什么先做实验，而不是先问“大模型多大才够”

训练大模型之前，团队必须决定参数量、训练 token 数、训练步数和硬件预算。朴素方案是把预算尽量用于更大参数量，因为更大模型具有更高表示容量。但如果数据太少，模型会在有限 token 上重复训练；如果模型太小，大量数据又可能无法被充分利用。

另一种方案是固定参数量，只增加数据。它能改善覆盖和统计估计，但当模型容量、优化或架构成为瓶颈时，额外 token 的边际收益会降低。

最昂贵的做法，是对每个预算直接训练多个完整大模型再比较。Scaling 研究尝试从一组较小实验中拟合规律，回答：在当前技术条件下，增加参数、数据或 compute 的边际收益如何变化？给定预算，资源应怎样分配？

因此 Scaling Law 首先是一种实验建模和工程决策工具，不是关于智能本质的哲学结论。

## Power law 的直觉

设：

- `N` 是非 embedding 参数量或研究中定义的模型规模；
- `D` 是训练 token 数或数据规模；
- `C` 是训练 compute；
- `L` 是验证集上的平均 loss；
- `L_inf` 是给定数据分布与任务下不可约损失的近似项。

一种简化的单变量经验关系是：

```text
L(N) = L_inf + A * N^(-alpha)
```

其中 `A > 0`，`alpha > 0` 是拟合常数。数据 scaling 可以类似写成：

```text
L(D) = L_inf + B * D^(-beta)
```

其中 `B > 0`，`beta > 0`。这意味着规模增加通常继续改善 loss，但边际收益递减：把资源扩大相同比例，获得的是相对稳定而非固定绝对值的改善。

去掉不可约项并取对数，可得到近似线性关系：

```text
log(L - L_inf) = log(A) - alpha * log(N)
```

所以研究者常在 log-log 图上观察近似直线。直线不是理论必然，它只是 power law 在这种坐标中的表现。斜率来自实验拟合，换模型族、数据、tokenizer、目标或训练 recipe 后可能改变。

## 参数、数据和 Compute 不能独立解释

真实训练同时受到参数与数据限制。一个用于建立直觉的联合形式是：

```text
L(N, D) = L_inf + A / N^alpha + B / D^beta
```

它表达两类可约误差：模型容量不足和数据不足。实际论文可能使用不同参数化、修正项和拟合方法，不能把这个简式当作通用精确方程。

对 dense Transformer 训练，compute 常可粗略表示为：

```text
C ~= k * N * D
```

`k` 汇总前向、反向和实现相关常数。这个近似用于思考资源分配，不包含所有 attention、embedding、稀疏激活、通信和硬件效率细节。

给定 `C`，增大 `N` 会迫使 `D` 下降，反之亦然。compute-optimal scaling 的问题就是：怎样选择 `N` 与 `D`，让预算约束下的预测 loss 最低。

这与“训练尽可能大的模型”不同。最大的可加载模型可能只看过很少数据；更小但训练 token 更多的模型，可能在同等 compute 下获得更低 loss，也可能在推理阶段更便宜。

## Kaplan 与 Chinchilla 的结论为什么不同

Kaplan 等人在 2020 年对语言模型进行了系统 scaling 实验，观察到模型规模、数据规模和 compute 与 cross-entropy loss 之间存在 power-law 关系，并据其拟合提出 compute-efficient training allocation。该研究的重要贡献，是把“规模通常有效”转成可以用小规模实验外推的定量问题。

Hoffmann 等人的 Chinchilla 工作在 2022 年重新研究 compute-optimal allocation，使用不同实验设计与更广的数据配置，得出更重视训练 token 的结论：在其研究范围内，许多大模型训练得不够充分；给定 compute，参数量与训练 token 应更均衡地扩大。

两者并不是一个正确、另一个毫无价值。差异说明 scaling exponent 和最优配置依赖实验覆盖、训练方法、数据与拟合假设。Chinchilla 修正了当时重要的工程判断，但它同样不是对所有架构、数据质量和后训练过程的永久常数。

对平台工程师，更重要的不是背诵某个固定 token-per-parameter 比例，而是理解方法：

```text
define target metric and budget
-> run controlled experiments
-> fit within observed regime
-> validate extrapolation
-> choose allocation
-> re-fit when recipe or constraints change
```

## 为什么会出现相对平滑的规律

目前没有一个简单理论完整解释所有神经网络 scaling 现象，但可以建立几个不越界的直觉。

第一，真实数据包含不同频率和复杂度的模式。小模型或小数据先捕捉高频、容易压缩的结构；资源增加后，系统可以继续拟合更稀有、更复杂的模式。大量模式的边际贡献叠加后，aggregate loss 可能表现得平滑。

第二，cross-entropy 是大量 token 预测误差的平均。即使单个样本行为离散，平均指标也会平滑掉很多局部波动。

第三，同一架构族和训练 recipe 引入稳定 inductive bias，使一组实验具有可比较性。若架构、数据处理和优化方式频繁改变，统一曲线更难成立。

这些都是解释性直觉，不是从第一性原理推出固定 exponent 的证明。观察到 power law 与知道其普适原因，是不同层次的结论。

## Loss 曲线不能直接推出具体能力

Language modeling loss 是对 token 分布预测的平均度量。它对整体建模质量敏感，却不直接等价于代码执行、数学推理、工具使用、安全拒答或某项 benchmark accuracy。

一个能力指标可能带阈值。例如任务按“最终答案完全正确”计分，底层概率即使平滑改善，只有越过决策边界时 accuracy 才变化。prompt、sampling 和评分函数也可能把连续变化映射成离散结果。

因此，不能从平滑 loss 曲线直接推导“某参数规模必然涌现某能力”，也不能因为某 benchmark 出现跳变就断言底层机制发生相变。第 8 章会专门讨论 emergence 的度量争议。

更稳健的做法是分层报告：

```text
training/validation loss trend
task-specific capability metrics
robustness and reliability metrics
production quality, latency, and cost
```

这些指标可以相关，但不能互相替代。

## 数据质量改变“D”的含义

公式里的 `D` 常被写成 token 数，但 token 并不等质。重复、低质量、过时、污染、错误或与目标分布无关的数据，边际价值不同。高质量筛选可能用更少 token 获得更高有效信息密度，但筛选也可能缩窄覆盖、引入偏见或丢失长尾。

数据混合还会改变能力分布。增加代码、数学、多语言或领域数据，可能改善对应任务，却影响其他分布上的 loss 和行为。一个聚合 scaling curve 无法替代 mixture design 和 slice evaluation。

所以工程上应区分 raw token、unique token、effective token 与目标分布覆盖。把所有数据按数量相加，会让 compute-optimal 结论失真。

## 架构、稀疏性与后训练改变边界

参数量 `N` 也不是统一的能力或 compute 单位。Dense 模型每个 token 激活大部分参数；MoE 可以增加总参数容量而只激活部分专家；parameter sharing、低精度和不同 Attention 结构会改变每 token compute 与 memory。

后训练更不能简单并入 pretraining scaling。SFT、preference optimization、RL、tool feedback 和 inference-time compute 可能用较少额外 token 显著改变行为，但它们优化的目标和成本结构不同。基础模型 loss 低，为能力提供更好底座，不保证后训练后的可用性排序完全相同。

同样，训练 compute-optimal 不等于生命周期成本最优。更大的模型即使训练 loss 更低，可能在长期 Serving 中产生更高 GPU、latency 和 energy 成本。若模型要被调用数十亿次，推理成本可能反过来支持“训练更多、部署更小”的选择。

## 从论文曲线到工程容量规划

Scaling Law 对 AI System 的直接价值，可以落在四类决策上。

第一，实验预算。用小规模 sweep 估计边际收益，提前淘汰明显不合理的 `N`、`D` 和 recipe 组合。

第二，集群规划。目标训练 token、模型规模和期限共同决定所需 accelerator time，但还要乘上 model FLOPs utilization、通信、故障和 checkpoint 开销。理论 FLOPs 不是实际完工时间。

第三，数据管道。若 compute 增长要求更多高质量 token，去重、过滤、配比、许可和吞吐会成为与 GPU 同等重要的瓶颈。

第四，训练与 Serving 联合优化。模型选择应同时考虑验证 loss、目标任务、推理吞吐、显存、量化可行性和调用总量，而不是只选择训练曲线上最低点。

一个更接近生产的决策目标可以写成：

```text
minimize lifecycle cost(N, D, runtime, traffic)
subject to capability >= target
           reliability >= threshold
           latency <= SLO
           data and compute budget are satisfied
```

这里的 capability 与 reliability 必须由独立 Evaluation 定义，不能直接用 pretraining loss 替代。

## Scaling 的适用边界

第一，外推距离越远，风险越大。拟合区间内近似直线，不保证跨多个数量级仍保持同一斜率。

第二，技术变化会造成 regime change。新的数据 mixture、optimizer、架构、tokenizer、precision 或训练目标可能使旧曲线失效。

第三，数据不是无限可扩展的 IID 样本。高价值数据稀缺、重复和许可约束会改变边际收益。

第四，能源、芯片供给、网络、存储和组织执行能力都是 compute 之外的硬约束。

第五，平均 loss 不包含全部风险。安全、偏差、事实性、隐私和恶意使用必须单独评估。

Scaling Law 最有价值的使用方式，是在明确范围内提供可证伪预测，再用新实验持续更新，而不是把历史曲线当作信仰。

## 本章在知识树中的位置

第 6 章解释 Transformer 为什么提供可扩展训练结构，本章解释在这种结构及特定训练 regime 下，参数、数据和 compute 与 loss 呈现怎样的经验关系。第 8 章将讨论广泛能力为何可能随这些条件增强，以及为什么能力和可靠性不能只由 scaling curve 推导。

在全书后续部分，本章连接 Part III 的数据与分布式训练、Part IV 的推理成本、Part V 的 GPU capacity 和 Cost。Scaling 从来不只是模型科学问题，它决定数据生产、集群投资和 Serving 经济性如何联合设计。

## 自检问题

1. 为什么 Scaling Law 是经验规律，而不是普适数学定律？
2. power law 在 log-log 图上为什么近似为直线？
3. `N`、`D`、`C`、`L` 分别表示什么？
4. 给定 compute 时，为什么参数量和 token 数之间存在分配问题？
5. Kaplan 与 Chinchilla 的差异说明了什么？
6. 为什么不应背诵一个永久有效的 token-per-parameter 比例？
7. 平滑的 validation loss 为什么不能直接证明某项能力连续或突然出现？
8. 为什么 token 数和参数量都不是跨数据、架构的统一质量单位？
9. 训练 compute-optimal 为什么可能不是生命周期成本最优？
10. 将一个 scaling 结论用于新模型族前，应重新验证哪些假设？

## 小结

Scaling Law 把“更多资源通常更好”变成了可实验、可拟合、可用于预算分配的工程问题。power-law 关系描述了边际收益递减，并揭示参数、数据与 compute 必须联合配置。

它的力量来自规律性，边界也来自规律性的条件性。数据质量、架构、训练方法、后训练、推理成本和 Evaluation 都可能改变最优决策。把 Scaling 当作实验模型而非自然法则，才能既利用它，又不把 loss 趋势误写成智能保证。

## Review notes

本章保留了简化公式用于建立直觉，但不把它们冒充 Kaplan 或 Chinchilla 的完整拟合方程。后续 Review 应在引用具体 exponent、比例或 compute 数字前回到原论文与适用区间，并继续把经验拟合、解释性直觉和工程启发分开。

优先核验入口：

- Jared Kaplan et al., "Scaling Laws for Neural Language Models", 2020: https://arxiv.org/abs/2001.08361
- Jordan Hoffmann et al., "Training Compute-Optimal Large Language Models", 2022: https://arxiv.org/abs/2203.15556
- Joel Hestness et al., "Deep Learning Scaling is Predictable, Empirically", 2017: https://arxiv.org/abs/1712.00409
- Mitchell Wortsman et al., "Small-scale proxies for large-scale Transformer training instabilities", 2023: https://arxiv.org/abs/2309.14322
