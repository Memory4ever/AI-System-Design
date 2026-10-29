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

当比较的架构采用不同sequence-mixer时，训练context长度也应进入预算约束，而不只作为模型部署后的窗口参数。固定总训练tokens并不会固定混合历史的代价：dense Attention在更长序列内支付更多成对计算，chunkwise recurrent路径则在固定chunk与状态维度下有另一份成本函数。因此可先固定架构与长度T，以C_arch(N,D,T)=H重新扫参数量和训练tokens，再比较各自的loss最优配置。[受限xLSTM/Transformer对照](https://arxiv.org/html/2510.02228v1#S3.SS5)中，同预算下长context使拟合最优Transformer规模明显下降、xLSTM仅轻降，说明长度改变的不只是推理内存，也改变训练预算的分配点；这不把固定状态提升为无限精确记忆，相关读写机制仍由第22章解释。

这一配置差额只在同一分词、语料、训练recipe与长度条件内解释：不同context下的loss目标不可直接并成质量下降幅度，同参数的单卡推理也不等于同任务质量或现代最佳serving对照。局部二次IsoFLOP最优点、对Huber权重敏感的loss面和每模型重新拟合的有效吞吐，均不能签发全局最优、普适exponent或线上deadline；单query访问历史也不能照搬整块causal矩阵的省半系数。长context的任务收益、全部训练/选参、chunk/state或KV、真实prefill/decode和完整服务费用须分别验收，不能由较低FLOPs或拟合lower-bound批准部署必胜。长度、架构或执行实现变化而留出质量/预算失配时，保留原长度的局部scaling sweep、显式Attention/混合状态与独立任务实测，再重选配置，不把一条线性复杂度分支当作通用替代。

<!-- source-family:SF-2025-ARXIV-2510-02228 -->

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

解释斜率前，还应先核对同等训练算力下曲线处在什么绝对位置：若小模型端点尚未被合理优化，随后模型只是追上较强配方，也可能画出很陡的改善线，而不是获得更好的规模规律。一个[受限开放参考分支](https://arxiv.org/html/2509.09009v1)先用共同预算轴、匹配的任务/分词与数据口径比较参考点，再讨论随模型和 tokens 改变的趋势；参考线用于发现配方或小端点不足，不自动成为任意数据、架构或更大规模的最优前沿。绝对 loss、斜率、留出任务质量与搜索预算应分别保存，局部更低 loss 不识别语言混合或某个组件的唯一因果。参考制备、配方搜索、所有训练与外推回归都付费，近似 FLOPs 不等完整设备/数据成本。口径或参考支持不匹配时，保留当前配方的局部拟合与独立留出检验，不由较陡 exponent、更多同线点或一份公开 reference 直接配置大规模预算。

<!-- source-family:SF-2025-ARXIV-2509-09009 -->

联合拟合还要求实验能区分被解释的轴。固定 tokens-per-parameter、令 `D=kN` 沿一条射线扩大模型，适合比较这个配比下的局部趋势；但在 `L=E+A N^(-α)+B D^(-β)` 中，若 `α≈β`，两项在该射线上近乎成比例，数据主要约束组合系数，而非分别识别容量与数据的贡献。[受限理论与小模型对照](https://arxiv.org/html/2605.08541v1)因此把 TPP 跨度、Jacobian 条件与离开训练射线的留出点纳入实验设计；多次拟合或更多同射线点不能自动补回缺失的方向。其全矩阵渐近结论另需主导参数对、噪声与局部线性化假设，实验中的多射线配比也不等于单一 TPP；小模型、专门语料上的弱效和高 TPP 的宽区间不支持通用充分阈值或等算力收益。新增配比训练、拟合重启与外推验证都有成本；覆盖不足时保留组合系数或局部曲线，暂不依据不稳定的分项系数配置大规模预算。<!-- source-family:SF-2026-ARXIV-2605-08541 -->

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

即使暂时只研究loss到某一任务分数的关系，也要先固定“loss在哪份分布上测量”。同一批checkpoint换用另一份验证语料，其perplexity坐标和不同预训练语料所形成曲线的相对位置都可能变化；这不是模型在固定任务上的真实表现被重新训练或自动改善。[受限的下游scaling复核](https://arxiv.org/html/2507.00885v1)还显示，共用验证集并不足以消除架构、任务格式、示例数、答案选项和观测范围造成的差异。因此横坐标语料及版本、checkpoint人口、下游scorer和支持尺度应共同冻结，再检验残差、非单调区间与留出尺度，不能仅由同loss或一段近直线认证跨配方的能力等价。这增加重新评价、数据版本审校和外推实验费用；支持不足或比较失配时，保留原配方的局部loss规划与独立任务实测，不把一组曲线的分类比例推广为所有任务的成功率，也不因局部反例丢弃仍在已验范围有效的scaling方法。
<!-- source-family:SF-2025-ARXIV-2507-00885 -->

若预算问题转为“这份预训练 compute 下，经过不同后训练的模型目前能达到什么任务水平”，受控 loss scaling 不再直接给答案。一个条件分支对已测模型生态拟合高分位能力曲线，把同一 compute 附近不同 family、recipe 与评价时间的模型视为观察人口，而不是取单个最高分当作物理上限。[必要分位边界与校准](https://arxiv.org/html/2602.15327v1)采用 q=.98；其曲线的单调形状是拟合约束，不是已证明的普遍规律。应同时检查带符号 compute-bin 残差与覆盖率，以及时间滚动时共同 compute 区间的校准：只有这些已测人口和重叠区间可支持预算线索，不支持跨 compute 外推，也不把数学或 instruction-following 的 recipe 漂移当作单纯参数不足。<!-- source-family:SF-2026-ARXIV-2602-15327 -->

测量成本高时，还可按 metadata 上局部模型 Jacobian 的近似信息收益选择一批待评模型，以正则化和 bin balance 防止采样集中在少数区域；这增加拟合、选择与人口维护成本，参数量只是评价成本 proxy，并非实际 GPU-hours。有限任务上较小子集接近完整评价，不授所有任务低预算保真或真正最优；样本支持改变、held-out coverage 失配或新 recipe 出现时，应重新评价而不是延伸旧曲线。受控预训练 loss-scaling、后训练条件分位测量和完整任务评价解决不同预算问题，后者不是前者的直接演进；它们共存，亦都不能证明未测模型的能力、无污染或生产质量。

## 数据质量改变“D”的含义

公式里的 `D` 常被写成 token 数，但 token 并不等质。重复、低质量、过时、污染、错误或与目标分布无关的数据，边际价值不同。高质量筛选可能用更少 token 获得更高有效信息密度，但筛选也可能缩窄覆盖、引入偏见或丢失长尾。

数据混合还会改变能力分布。增加代码、数学、多语言或领域数据，可能改善对应任务，却影响其他分布上的 loss 和行为。一个聚合 scaling curve 无法替代 mixture design 和 slice evaluation。

所以工程上应区分 raw token、unique token、effective token 与目标分布覆盖。把所有数据按数量相加，会让 compute-optimal 结论失真。

复用预训练模型时，token预算还要按阶段拆开：首阶段曝光D1决定base的起点，第二阶段D2才是当前继续训练或扩容后消费的数据。固定base的局部D2曲线仍可拟合，但不同D1不一定只平移同一指数；[受限两阶段实验](https://arxiv.org/html/2510.06548v1#S4)用交互项使第二阶段有效指数随log(D1)改变，展示更好初始loss与更小追加收益可以同时出现。这是有限小模型/语料下的经验分支，不是过度训练的普遍饱和定律；width初始化保函数也不能替不保函数的depth stacking签字。应保存base checkpoint、两阶段语料/曝光、扩容规则与评价分布，分别比较固定既成资产的增量费用和另起base的全阶段费用，不能把sunk cost既隐藏又重复收取。拟合中的低loss留出选择、最终系数再用验证点及规模外推仍须独立核验，论文给出的巨大token阈值、compute最优关系与GPU小时估算不冒实测。全部base制备/扩容、再训练、拟合搜索与任务回归都计费；目标、初始化或外推失配时，保留当前base局部扫点、中间checkpoint与从零训练的同目标对照，不由一个较好base或统一token总量批准普适复用优势。<!-- source-family:SF-2025-ARXIV-2510-06548 -->

数据量还可拆成“多少篇独立上下文”与“每篇内观察多长”，二者不必由总 token 数互换。一个受限 next-token 统计模型先为每篇抽取局部 context function，再用共享语言规律与该局部函数生成序列；在同分布、平滑性和指定 Transformer 类下，其风险界把跨文档学习共享规律与从当前文档估计局部 context 分开。因而比较数据预算时，可以同时记录独立文档人口、长度分布与上下文覆盖，而不只保存二者的乘积；这是模型提示的诊断轴，不是同 token 预算下长文或短文必然更好的结论。

[这项受限风险分析](https://arxiv.org/html/2606.13280v1#S4)研究每篇仅末位置的经验风险最小化与期望 KL，并依赖有界 logits、平滑 latent functions、规则 context embeddings 及充分大架构；它不证明实践 SGD、全位置训练、真实长尾语料或能力指标具有同一 rate。词表增大同时改变估计与离散近似项，也不能推出越大越好。独立上下文制备、长度分组、训练与留出评价均增加费用；这些假设或留出曲线不合时，仍以固定 tokenizer/recipe 的局部 scaling sweep 和原数据配置为准，不用渐近上界替代 compute-optimal 实验。
<!-- source-family:SF-2026-ARXIV-2606-13280 -->

## 架构、稀疏性与后训练改变边界

参数量 `N` 也不是统一的能力或 compute 单位。Dense 模型每个 token 激活大部分参数；MoE 可以增加总参数容量而只激活部分专家；parameter sharing、低精度和不同 Attention 结构会改变每 token compute 与 memory。

后训练更不能简单并入 pretraining scaling。SFT、preference optimization、RL、tool feedback 和 inference-time compute 可能用较少额外 token 显著改变行为，但它们优化的目标和成本结构不同。基础模型 loss 低，为能力提供更好底座，不保证后训练后的可用性排序完全相同。

同样，训练 compute-optimal 不等于生命周期成本最优。更大的模型即使训练 loss 更低，可能在长期 Serving 中产生更高 GPU、latency 和 energy 成本。若模型要被调用数十亿次，推理成本可能反过来支持“训练更多、部署更小”的选择。

这种反馈不只来自请求总量，还来自每个请求怎样使用模型。如果部署允许重复采样并可靠识别正确候选，训练规划就需要联合选择参数量 `N`、训练 token `D` 与尝试次数 `k`，而不是先按单次生成确定模型，再事后增加采样。较小但训练更充分的模型可能用更便宜的多次尝试补偿单次能力；代价是更多生成、验证和候选选择。若样本高度相关、验证器不可靠或必须单次低延迟回答，这条补偿路径就不成立，原来的单次能力与训练预算规划仍有意义。

[受限的联合拟合实验](https://arxiv.org/html/2604.01411v1#S3)以不到 1B 参数的 checkpoint 和八个任务检验这个分支，但 `pass@k` 衡量“至少一个候选正确”，不等于系统能选中它；其 `2Nk` 也只是每 token 推理 FLOPs 近似，不能省去输出长度、验证、内存和并发成本。工程上应把采样与选择合同一起固定，再测真实质量—成本前沿；大规模模型、不同任务与生产 SLO 必须重新验证，不能将拟合外推当作已完成的训练实验。
<!-- source-family:SF-2026-ARXIV-2604-01411 -->

联合选择还可以包含同一训练轨迹上的 checkpoint 与预计服务到下一次 refresh 的 horizon，而不只比较最终模型大小。[有限 checkpoint×test-time-compute 对照](https://arxiv.org/html/2601.01332v1)将较早停止的训练节省与部署期新增生成、验证和选择成本一起考虑：请求量很小时额外推理或许能补偿较早 checkpoint，请求量扩大后同一分支可能失去成本优势。这里的质量投影可能失准，按 validation 最优曲线筛选还会引入选择偏差；pass@k 或 oracle 潜力也不等于真实部署选择器的成功率。工程上应固定 refresh horizon、checkpoint 候选人口与可执行的选择协议，保留训练成本差和完整部署成本，再用留出任务检验质量—成本前沿；不要用一个成本不等式证明准确率，也不要把某一 FLOPs 常数或投影节省率外推到所有服务配置。原来的单次质量与完整训练规划在投影不可靠、验证成本高或严格低延迟场景仍然合理。<!-- source-family:SF-2026-ARXIV-2601-01332 -->

### 扩宽只有在学习方向跨样本对齐时才可能转化为泛化收益

把网络扩宽并以 function-preserving 方式初始化，能够保留旧模型的函数，因此是低风险增加容量的起点；但“训练开始时函数不变”只说明没有立即破坏旧行为，不说明新增自由度会沿着测试分布需要的方向学习。有限训练样本下，训练梯度与独立测试梯度可能失配：参数更多时，模型既拥有更多有用更新方向，也拥有更多只适合当前样本的方向。

因此宽度扩展的 scaling experiment 还应测量新增参数方向在独立样本之间的梯度对齐，而不能只比较训练 loss 或 nominal width。一个受限的统计分支用 train/test gradient inner product 的均值与方差刻画这种有效对齐维度，并在保持函数的 residual expansion 中检验它能否预测 held-out loss 的初始变化。它把“容量增加”推进为“新增更新方向是否可由现有样本可靠估计”的问题，但只覆盖非零 population gradient、有限二阶矩和局部干预；不能推出更宽必然泛化更好，也不能替代完整训练后的 evaluation。

这条检查会增加独立数据切片、梯度采样与统计噪声成本，且局部对齐可能随训练阶段、数据 mixture 和 optimizer 改变。样本不足或置信区间跨过无收益区域时，应保留原宽度或先扩大数据与复验，而不是把 function-preserving expansion 当作自动获益。原有 loss scaling curve 在架构固定、数据充足且对齐假设已验证的范围内仍是更便宜的规划基线。

<!-- source-family:SF-2026-ARXIV-2607-24887 -->

深度的边际价值也要绑定跨上下文的数据几何。若线性回归上下文共用固定、可逆的输入协方差，受限Attention模型可把其逆矩阵学成共享预条件；在无噪声和无限长支持集的极限，单次更新就可能足够。若各上下文的协方差方向随机旋转，同一白化方向不能复用，重复更新才有机会消除更多残差。[受限ICL scaling分析](https://arxiv.org/html/2510.01098v1#S3)据此给出检验深度价值的条件分支，而非“更长context总能替代深度”或所有模型都应加深。其signed mask、线性回归与对称gradient-flow条件不是普通causal LLM；冻结投影rank、预训练时间、重复深度和context长度也不是可任意互换的参数/token预算。单轴渐近及作者计算proxy不授权真实LLM的联合有限资源最优形状，原文局部loss常数亦未闭。协方差人口构造、完整预训练/形状搜索、状态与留出及迁移回归都付费；分布、质量或净预算失配时，保留原架构族的局部scaling sweep和独立任务评价，不用toy极限替代容量规划。<!-- source-family:SF-2025-ARXIV-2510-01098 -->

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

当独特真实语料已固定，增加训练 compute 仍有多种不同去向：扩大单模型、联合重调 weight decay/learning rate/重复 epochs，或训练多个成员后平均 logits，再把成员生成的样本混入真实语料训练学生。它们不是同一条只增 token 的曲线：平均 logits 每次预测要调用全部成员，逐成员生成的合成池也不是从平均分布采样；独特 seed 数、重复训练 tokens、teacher 生成和 student 训练必须分别记账。受限小模型实验表明，重调正则可改变原先的过拟合趋势，但有限规模的 asymptote 拟合、局部超参数搜索及更高层外推都不构成无限 compute 或全局最优证书；混入真实数据的 token-matched 对照也不担保任意 self-training 都免于退化。全部成员训练/推理、搜索、生成池与学生训练均付费，有限 held-out loss 不替下游能力验收。外推、合成质量或总预算不稳时，保留单模型的局部 scaling sweep、真实数据混合与独立留出检验，不把固定数据写成固定总费用或免费扩容。

<!-- source-family:SF-2025-ARXIV-2509-14786 -->

有限语料还改变了曲线的优化对象：当唯一数据量`U`固定、compute不再是binding约束时，应考察在epochs、learning rate和regularization等已搜索范围内取得的损失包络`L*(N,U)`，而不是沿用固定`6ND`预算下的最优点。[受限数据约束实验](https://arxiv.org/html/2606.06888v1)发现，单纯相加的参数项与数据项不能拟合所测容量—数据交互，耦合的软瓶颈模型在留出数据规模上更合适；同文的masked-input辅助NTP也只是在保留AR目标下增加正则，需两次forward，不是省计算。有限模型尺度、超参数搜索和拟合渐近线仍不足以给frontier模型签发普适数据效率常数，新增重复训练、搜索与回归均须计费；留出点或新recipe失配时，回到局部曲线与原单模型基线，而不把“compute-rich”解释为无限免费计算。<!-- source-family:SF-2026-ARXIV-2606-06888 -->

当扩增方式是改写同一seed语料时，还可把rewrite fraction R和唯一natural token数T显式加入拟合面：除参数/训练token项外，分别估计随R变化的分布失配项，以及natural token反复出现的惩罚，而不把每个rewrite等价成fresh data。在source与rewrite近等长、生成足够FLOP-bound且不跨run摊销的近似下，一次student预算可写为6ND+4NᵣDR，后项包含source prefill和rewrite decode；teacher预训练/指令适配、judge与拟合实验仍须另计。[受限改写scaling对照](https://arxiv.org/html/2610.31867v1#S2)支持从小预算拟合、在留出budget选择有限R，但并非任意语料的连续全局最优；按部分域的gold-answer BPB胜teacher也不等完整能力超越，外部teacher的知识和少量强teacher指令数据不能消失。R、重复、自然语料质量和teacher改变后，分布floor与最优点都要重验；没有可验证外推或生成成本主导时，保自然数据/较小改写比例与局部sweep，不把合成数量或一个拟合asymptote当无限扩容保证。
<!-- source-family:SF-2026-ARXIV-2610-31867 -->

多语训练还应把目标语言、具名迁移语言和其余语料的曝光分账，而不是把所有token压成同一种有效数据量。可分别记录各来源的unique tokens与重复epochs，对重复曝光施加饱和函数，再拟合各来源对目标loss的权重；权重属于当前词表、模型族和混合协议，不是语言的固定属性。[受限多语scaling对照](https://arxiv.org/html/2510.22037v1#S3)用留出的模型规模、tokens、compute和mixture分别检验，显示只拟目标token会漏掉迁移，但部分语言对的transfer由估计器补齐，script/family相关也不等因果。迁移方向不必互惠，较大模型减轻干扰不意味着无限语言免费加入。训练全部拟合点、选来源与微调搜索均付费；公共checkpoint的预训练成本须另列，微调胜从头训练的局部交点不授普遍预算阈值。新语言、重复强度或外推失配时，回到局部配比sweep和原单语/多语基线。
<!-- source-family:SF-2025-ARXIV-2510-22037 -->

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

- `SF-2025-ARXIV-2510-01098`：Daily2025-10-03补Oct02；[ICL Scaling exact-v1](https://arxiv.org/html/2510.01098v1#S3)，2+1+3=6/协方差人口与深度选择gap深入。仅固定共享预条件与逐context旋转下迭代价值的受限分支；保signed mask/线性与GF、无噪声长context、Eq8局部常数反侧、单轴非联合有限资源、projection-rank非模型参数及全部训练/搜索/回归费。不采全DMFT/真实LLM最优shape或净速度，未核全附件/图像素/代码或复现。R21日门复用；root R48必要/actualowner/整体PRE与本次窄授通过，已真实SAVE/fullselfread；root R52唯一实际POST通过，指定窄位释放。仅行政同步既成，不预DAY。

- `SF-2025-ARXIV-2510-06548` — Daily2025-10-10补Oct09BJT；[exact-v1](https://arxiv.org/html/2510.06548v1)，2+1+3=6，作者A35唯一首次必要§2–6/B3–4/C1–5/D1–3。仅D1/D2 joint经验交互、初始loss与追加边际收益及资产费用资格差额；保0.1B grid/最大约1B、width FPI与stack不保函数、最低loss10%留出/最终fit含验证点，13T/300B阈值与Eq9未实证、3000GPUh理论估算及全费，不采普遍saturation/精确外推阈值或净速。未核全图像素/代码或训练复现；整体PRE/真实SAVE/完整自读/solePOST仅本日实际后到，不预签。

- `SF-2026-ARXIV-2606-13280` — Daily2026-06-13补Jun12；2+1+3=6；[exact-v1](https://arxiv.org/html/2606.13280v1) §2.2/3/4及B必要实际读；仅n文档与T内context统计轴，保末位置ERM/expectedKL、bounded/smooth/embedding/architecture假设、fixedW旧方法与真实长尾反侧，不采全部定理正确性/SGD/实践exponent或同token预算排序，未核实现/复现。root§27必要/actualowner/原两段PRE通过，按窄授真实保存；root§29唯一实际POST通过，指定窄位释放；仅行政同步既成，不预日级。

- `SF-2026-ARXIV-2606-06888` — Daily2026-06-09补Jun08；[exact-v1](https://arxiv.org/html/2606.06888v1) §2–4及Discussion必要域，2+2+3=7。仅调参后固定unique-data损失包络与容量—数据耦合，MIR作两forward额外正则例，不另复制Ch28；保72M–1.4B/有限留出、ELBO与NLL异义、拟合asymptote及全部搜索训练费。root必要源/actual owner/完整两侧已核并授本单段+注；作者已真实保存并完整自读新增、直接完整两侧及自身H2注；root SUP_REVIEW §6唯一非writer实际POST已通过，指定窄位已释放，不预DAY。未核代码/复现，不授DAY。

- `SF-2025-ARXIV-2509-14786` — Aristotle，Daily2025-09-20补Sep19；[exact-v1](https://arxiv.org/html/2509.14786v1) §2–3/4.1/4.3/5.4/6/A/B1/E1–3/H1–2必要，2+2+2=6。仅固定独特seed下正则/epochs、全成员logit消费者及逐成员teacher生成/学生token分账；保有限拟合/局部搜索/二三层未验、real混合条件及全部成员/搜索/生成/student费，不采无限实测/全局最优/免费扩容或免collapse。未核代码/复现；Einstein§15必要Source已实际采用，§17原三项纯PRE通过；root本轮完整fresh窄授后原技术稿真实保存，Einstein§19唯一非writer实际完整新增/直接两侧/外侧binding及本人注POST通过，本指定窄位生效释放；仅同步既成事实，不预日级。

- `SF-2026-ARXIV-2605-08541` — Daily2026-05-13补May12；exact-v1 partial raw中完整主文§3–5实际已读；3+2+3=8。只取固定ray近指数导致系数难辨及离ray验证，不授全矩阵无条件定理/通用必要充分TPP阈值；保CO12fan、不同预算、fitseed非trainingrepeat、专域弱效、高TPP跨50%CI与全费。未读全附录/核代码/复现，root R2必要Source、R6逐字PRE通过，指定正文/marker/本人注已按窄写权保存；root R7非作者完整正文/直接两侧/本人注actualPOST通过，窄位释放。 本次仅同步已成事实，不重写机制或认证实现/复现、全覆盖或整日Gate。

- `SF-2026-ARXIV-2601-01332` — Daily `2026-01-07`；[exact-v1](https://arxiv.org/html/2601.01332v1) §2–4/Limitations及 Appendix A成本口径。2+2+2=6，具体成本知识缺口必要深入；采用 checkpoint/refresh horizon 与实际 TTC 选择预算联合规划，不采用主文/Appendix A 不同 Ninfer 分母、常数6、92%投影或由成本约束推出 accuracy。留出选择偏差、pass@k/oracle 与部署选择器不同；root必要原源/owner写前通过，root实际一段、前后衔接与末注非作者POST通过，未复现。

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

- `SF-2026-ARXIV-2602-15327` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15327v1) §2–4/AppendixB/F。2+2+2=6，具体测量分配差额受影响深入；只采已测后训练人口q.98、signed compute-bin/rolling overlap校准及metadata局部Jacobian的成本近似测量分配，不授physical ceiling、compute外推、真正最优或全任务低预算。人口/recipe漂移、parameter-count成本proxy和旧受控loss路线近正文；root必要源/actualowner PRE及实际两段/完整邻接与末注非作者POST通过，窄锁释放，未核实现/复现。

- `SF-2025-ARXIV-2507-00885` — Boyle，Daily2025-07-03补Jul2；[exact-v1](https://arxiv.org/html/2507.00885v1)§2–7/Limitations/AppB–E必要，2+1+2=5，Ch7验证分布坐标小gap深入。仅采固定corpus/checkpoint/harness/支持范围的外推分责，不采39%普遍率、单一内部因果或buggySIQA正面结果；未逐点核图、原checkpoint/code或复现。root79已实际必要Source/当前owner/逐字PRE通过并授本单段/独立marker/本人注窄位；作者已按批准稿真实保存并实际完整顺读新增、完整直接两侧及本人注，限定检查通过；root81已一次真实非writer完整新增、完整两侧及本人注POST通过，实际整合生效并释放本指定窄位；本注仅同步既成事实，不授DAY。

- `SF-2025-ARXIV-2509-09009` — Carson，Daily2025-09-13补Sep12；[exact-v1](https://arxiv.org/html/2509.09009v1)§2–4/A–C/T1–5/7必要域，R26首Source/Zeno72一次独核正式2+1+2=5，唯一Ch7。只同compute绝对参考位置校准→再解斜率，保小端点suboptimal/局部任务反退、v1 .01/8dataset、配方/全搜索费用，不采compute-optimal/混语言因果/全scale最优。不倒填current .02/9，未核全图/实现/训练复现；Zeno77逐字PRE与root当前精确新授已过，作者按R54原一段/独立marker/本人注实际保存；Zeno81唯一实际nonwriter完整新增/完整直接两侧/本人注/限定diff POST通过，第13实际整合生效并释放指定窄位；本注仅同步既成事实，不第三核或预DAY。

- `SF-2025-ARXIV-2510-02228` — Hilbert，Daily2025-10-04补Oct03BJT；[xLSTM Scaling exact-v1](https://arxiv.org/html/2510.02228v1)A395唯一首次必要S2–4/E1–4/S6、A1.1–3/T1–3/C2/C3.1–4/E8–16/D1–3/E22–27决定域，原2+2+2=6，仅context/sequence-mixer成本进入预算与有限最优配置差额深入。保同T与跨Tloss资格、batch/recipe与拟合敏感、fixedstate非精确历史、singlequery系数/roofline非完整配方、matchedN非等质和全部训练/拟合/执行费，不采通用Pareto/最优shape/下游或生产SLO。未核全图像素/全部config表/源码/后v2或复现，关键独核/整体PRE/真实SAVE/fullselfread/solePOST仅本日canonical实际后到层，本注不预签。

- `SF-2026-ARXIV-2610-31867` — Daily2026-10-27，exact-v1 §2/3.1–3.3/5必要，2+2+2=6；仅R-dependent分布/重复项与rewrite生成—student预算接口。保同长/FLOP-bound/无摊销近似与不含teacher预训、GLM少量指令/LMjudge、有限R留出/3B反例、BPB非accuracy/整能力及全费；未核全附录/实现/复现，不授连续全局optimum或通用teacher上限。

- `SF-2025-ARXIV-2510-22037`：Daily 2025-10-29补窗；精确v1必要支持/直接反侧已读，未运行代码或复现。明确target/transfer/other及各自unique/repetition，非重复现有同质token有效性泛论；不录冲突常数或全局最优预算公式。
