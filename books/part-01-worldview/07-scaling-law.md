# 第7章 Scaling Law 为什么成立

**Knowledge Tree:** Part I 世界观：AI 为什么会发展成今天这样
**Stable Knowledge Node ID:** `WORLDVIEW-SCALING-LAW`
**Legacy Chapter:** Ch7
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

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20196:start -->
数据量也不只是公式中的一个标量。对具有可恢复离散状态的受控序列，可以把每个状态相对全局 next-token
baseline 的 KL 偏离乘以该状态出现质量，得到 predictive-contribution spectrum；随着样本增多，有效截断秩
`K(N)` 逐步覆盖尾部贡献，剩余谱质量可与 excess loss 联系起来。这提供了“更多数据究竟解锁了哪些预测结构”
的解释坐标，却不取代参数量、训练 compute 与模型族本身。

这条分支依赖 suffix-automaton state、经验分布和论文给定的尾部对齐假设；真实语料的 latent state 未必可唯一
恢复，谱估计也会受 tokenizer、长尾采样和有限样本影响。因此它只能作为受控诊断：假设或拟合失效时，仍应
回退联合 scaling experiment、held-out loss 与能力 slice，而不能把 spectrum 外推成通用 scaling law。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20196:end -->

## Kaplan 与 Chinchilla 的结论为什么不同

Kaplan 等人在 2020 年对语言模型进行了系统 scaling 实验，观察到模型规模、数据规模和 compute 与 cross-entropy loss 之间存在 power-law 关系，并据其拟合提出 compute-efficient training allocation。该研究的重要贡献，是把“规模通常有效”转成可以用小规模实验外推的定量问题。

Hoffmann 等人的 Chinchilla 工作在 2022 年重新研究 compute-optimal allocation，使用不同实验设计与更广的数据配置，得出更重视训练 token 的结论：在其研究范围内，许多大模型训练得不够充分；给定 compute，参数量与训练 token 应更均衡地扩大。

两者并不是一个正确、另一个毫无价值。差异说明 scaling exponent 和最优配置依赖实验覆盖、训练方法、数据与拟合假设。Chinchilla 修正了当时重要的工程判断，但它同样不是对所有架构、数据质量和后训练过程的永久常数。

架构也可能改变 exponent，而不只是移动同一条曲线的常数项。Looped/recursive transformer 提供了一个受控分支：训练时增加 core 的重复次数，或随 compute 增长模型深度/参数，并比较 shared-weight 与 untied growth，可以让 compute-optimal loss exponent 在受测尺度上发生变化。这个结果否定的是“exponent 与架构无关”的默认假设，不证明递归结构在生产规模永远取得指数级优势；作者的 FineWeb/FineWeb-Edu、有限模型梯度和 CORE 外推仍可能受 recipe、数据重复与拟合区间影响。平台做 scaling 决策时因此要把 architecture-growth rule 纳入 experiment identity，并保留 vanilla family 作为同预算对照，不能把旧 exponent 直接带入新架构。

<!-- source-family:arxiv:2609.19107v1 -->

对平台工程师，更重要的不是背诵某个固定 token-per-parameter 比例，而是理解方法：

```text
define target metric and budget
-> run controlled experiments
-> fit within observed regime
-> validate extrapolation
-> choose allocation
-> re-fit when recipe or constraints change
```

这里还要区分“观察到一条近似抛物线”与“估计到了真实 compute-optimal frontier”。沿每个 compute budget 只取
少量点、再分别拟合局部二次曲线，计算简单，也适合近似对称且采样覆盖充分的局部诊断；当 loss surface 非对称、
最优点靠近采样边界或 grid 偏心时，这个两阶段过程会把实验设计偏差写进 exponent。更稳健的分支是直接对联合
surface 拟合，并用 variable projection 等方法同时估计共享参数与每条 curve 的 nuisance terms：

```text
sparse IsoFLOP grid
→ per-budget local parabola minima
→ joint surface fit with explicit parameter coupling
→ recovery test on synthetic truth
→ held-out frontier validation
```

联合拟合减少结构性偏差，却提高初始化、数值条件和实验设计要求；若观测区域太窄，它也只会更精确地拟合一段
缺少外推信息的数据。因而 scaling study 不只要报告最终 exponent，还要保存 grid geometry、objective、optimizer、
数据 recipe、拟合器与 uncertainty。局部抛物线在只做邻域插值时仍有价值；跨数量级容量决策则必须检验参数恢复与
外推稳定性。事件时证据证明的是特定拟合方法在 synthetic 与公开 IsoFLOP 数据上的偏差，不直接证明任何新的
通用 token/parameter 常数。<!-- source-family:SF-2026-ARXIV-2603-22339 -->

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

这种反馈不只来自请求总量，还来自每个请求怎样使用模型。如果部署允许重复采样并可靠识别正确候选，训练规划就需要联合选择参数量 `N`、训练 token `D` 与尝试次数 `k`，而不是先按单次生成确定模型，再事后增加采样。较小但训练更充分的模型可能用更便宜的多次尝试补偿单次能力；代价是更多生成、验证和候选选择。若样本高度相关、验证器不可靠或必须单次低延迟回答，这条补偿路径就不成立，原来的单次能力与训练预算规划仍有意义。

[受限的联合拟合实验](https://arxiv.org/html/2604.01411v1#S3)以不到 1B 参数的 checkpoint 和八个任务检验这个分支，但 `pass@k` 衡量“至少一个候选正确”，不等于系统能选中它；其 `2Nk` 也只是每 token 推理 FLOPs 近似，不能省去输出长度、验证、内存和并发成本。工程上应把采样与选择合同一起固定，再测真实质量—成本前沿；大规模模型、不同任务与生产 SLO 必须重新验证，不能将拟合外推当作已完成的训练实验。
<!-- source-family:SF-2026-ARXIV-2604-01411 -->

### 扩宽只有在学习方向跨样本对齐时才可能转化为泛化收益

把网络扩宽并以 function-preserving 方式初始化，能够保留旧模型的函数，因此是低风险增加容量的起点；但“训练开始时函数不变”只说明没有立即破坏旧行为，不说明新增自由度会沿着测试分布需要的方向学习。有限训练样本下，训练梯度与独立测试梯度可能失配：参数更多时，模型既拥有更多有用更新方向，也拥有更多只适合当前样本的方向。

因此宽度扩展的 scaling experiment 还应测量新增参数方向在独立样本之间的梯度对齐，而不能只比较训练 loss 或 nominal width。一个受限的统计分支用 train/test gradient inner product 的均值与方差刻画这种有效对齐维度，并在保持函数的 residual expansion 中检验它能否预测 held-out loss 的初始变化。它把“容量增加”推进为“新增更新方向是否可由现有样本可靠估计”的问题，但只覆盖非零 population gradient、有限二阶矩和局部干预；不能推出更宽必然泛化更好，也不能替代完整训练后的 evaluation。

这条检查会增加独立数据切片、梯度采样与统计噪声成本，且局部对齐可能随训练阶段、数据 mixture 和 optimizer 改变。样本不足或置信区间跨过无收益区域时，应保留原宽度或先扩大数据与复验，而不是把 function-preserving expansion 当作自动获益。原有 loss scaling curve 在架构固定、数据充足且对齐假设已验证的范围内仍是更便宜的规划基线。

<!-- source-family:SF-2026-ARXIV-2607-24887 -->

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

跨表示或跨 domain 外推时，还要判断 transformation 保留了多少信息。双射变换可在同一统计问题上保留 scaling 关系；非双射变换会因信息分辨率下降而改变可达误差与曲线。experiment owner 因而必须把 transformation、目标域和有效 resolution 纳入外推身份，而不能只比较名义参数量、token 数或 compute。<!-- semantic-body-binding:SF-2026-ARXIV-2605-07546 -->

transformation-aware 判断能减少把表面同尺度误写成同规律，却依赖 resolution 的估计与任务语义是否可比。变换不可辨、留出尺度不支持或任务定义已经改变时，应回退目标域小规模 sweep，而不是搬用原曲线。exact-v1 的理论、语言、视觉、语音和两个跨域案例不构成通用 scaling law。

第三，数据不是无限可扩展的 IID 样本。高价值数据稀缺、重复和许可约束会改变边际收益。

第四，能源、芯片供给、网络、存储和组织执行能力都是 compute 之外的硬约束。

第五，平均 loss 不包含全部风险。安全、偏差、事实性、隐私和恶意使用必须单独评估。

Scaling Law 最有价值的使用方式，是在明确范围内提供可证伪预测，再用新实验持续更新，而不是把历史曲线当作信仰。

### 从单轴经验律到联合可检验外推

只固定参数量、数据量或训练 compute 之一时，用单轴 power law 近似损失趋势是合理的；但训练步数、推理 compute 与关键超参数共同变化后，原曲线不再拥有唯一解释。更稳健的做法，是把这些轴连同拟合区间与外推目标一起交给 scaling experiment owner，联合拟合后再用留出的规模点验证。这样可以减少把某一轴的收益错记到另一轴，却付出更多实验单元、交互项和模型选择风险；若联合模型在留出尺度上失配，应退回局部单轴曲线或重新分区，而不是继续扩大外推。exact-v1 证据只覆盖论文披露的视觉、语言、数学与 RL 实验及其参数域，不能证明统一函数在新架构、数据分布或生产 SLO 下仍成立。<!-- source-family:SF-2026-ARXIV-2605-26248 -->

### Token 的价值不是固定常数：compute-optimal 与 data-optimal 之间还有有效性函数

经典 compute-optimal 推导常把每个训练 token 视为同质新增证据；当数据开始重复、改写或合成扩增时，这个假设失效。可用 token effectiveness 表示 derived token 相对 fresh token 的边际训练价值，并让它随模型规模、tokens-per-parameter、扩增策略与扩增量变化。于是最优点不再只由参数和名义 token 数决定，而由 compute、可获得 fresh data 与边际有效性共同决定。

小规模模型和有限语料实验不能给出 frontier model 的普适 effectiveness 常数，扩增价值也会饱和。这个扩展的意义是要求规划者估计 marginal learning value 并保留不确定性，而不是把 synthetic/repeated tokens 按固定比例换算成新数据；无可靠估计时，经典 scaling law 仍是基线，但必须显式声明同质 token 假设。

<!-- source-family:SF-2026-ARXIV-2607-25271 -->

## 本章在知识树中的位置

第 6 章解释 Transformer 为什么提供可扩展训练结构，本章解释在这种结构及特定训练 regime 下，参数、数据和 compute 与 loss 呈现怎样的经验关系。第 8 章将讨论广泛能力为何可能随这些条件增强，以及为什么能力和可靠性不能只由 scaling curve 推导。

在全书后续部分，本章连接 Part IV 的数据与分布式训练、Part V 的推理成本、Part VI 的 GPU capacity 和 Cost。Scaling 从来不只是模型科学问题，它决定数据生产、集群投资和 Serving 经济性如何联合设计。

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

- `SF-2026-ARXIV-2605-07546`（Status: Theoretical / Experimental）：[exact-v1](https://arxiv.org/html/2605.07546v1) 支持在论文条件下区分信息保持变换与分辨率下降对 scaling 的影响；有限模型、任务与 resolution 估计不能外推为跨 domain 通用规律。

本章保留了简化公式用于建立直觉，但不把它们冒充 Kaplan 或 Chinchilla 的完整拟合方程。后续 Review 应在引用具体 exponent、比例或 compute 数字前回到原论文与适用区间，并继续把经验拟合、解释性直觉和工程启发分开。

优先核验入口：

- Jared Kaplan et al., "Scaling Laws for Neural Language Models", 2020: https://arxiv.org/abs/2001.08361
- Jordan Hoffmann et al., "Training Compute-Optimal Large Language Models", 2022: https://arxiv.org/abs/2203.15556
- Joel Hestness et al., "Deep Learning Scaling is Predictable, Empirically", 2017: https://arxiv.org/abs/1712.00409
- Mitchell Wortsman et al., "Small-scale proxies for large-scale Transformer training instabilities", 2023: https://arxiv.org/abs/2309.14322

<!-- daily-books-trace:SF-2026-ARXIV-2607-24887:start -->
- `SF-2026-ARXIV-2607-24887` — Daily `2026-07-29`；primary `arXiv:2607.24887v1`；正文锚点“扩宽只有在学习方向跨样本对齐时才可能转化为泛化收益”。
  证据只支持论文假设与受控 residual intervention 下的局部梯度对齐条件，不支持宽度增加必然改善长期训练或泛化。
<!-- daily-books-trace:SF-2026-ARXIV-2607-24887:end -->
