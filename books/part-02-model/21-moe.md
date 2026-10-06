# 第21章 MoE

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-MOE`
**Legacy Chapter:** Ch21
**Status:** Draft

**Roadmap Intent:** 稀疏专家模型如何扩大容量，同时控制计算成本。

## 本章要回答的问题

Dense MLP 扩大参数量时，每个 token 都要经过更多参数。能否让模型拥有更大总容量，却只让每个 token 激活其中少数部分？Mixture of Experts 为什么会把一个 MLP 设计变成动态路由、负载均衡和 All-to-All 问题？

本章的核心判断是：**MoE 将总参数容量与单 token active parameters 部分解耦，代价是让模型每次前向都动态决定计算与通信路径。**稀疏的是激活路径，不代表 expert weights 使用稀疏矩阵存储。

第 20 章已经闭合从 logits 到 next token 的生成主干。本章不是 Sampling 后新增一个执行阶段，而是回到第 16 章的 MLP 子层：保持 Transformer Layer 的外部 shape contract 不变，只替换其中的容量组织方式。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`d_model` 表示 hidden dimension，`E` 表示 expert 数，`k` 表示每个 token 选择的 expert 数。

## 从 Dense MLP 的绑定关系开始

第16章的 Dense MLP 对所有 token 使用同一组参数：

```text
x -> W_up -> activation/gate -> W_down -> y
```

若把 `d_ff` 扩大，总参数与每 token FLOPs 同时上升。模型容量和执行成本被绑定。

一种朴素方案是准备多个不同 MLP，但让每个 token 仍执行全部 experts 后再平均。这增加了容量，却没有减少 active compute。

MoE 增加一个 Router，每个 token 只进入 top-`k` experts：

```text
token state
-> router
-> selected expert MLPs
-> weighted combination
```

## Router 的 tensor shape

输入 hidden states：

```text
X [B,T,d_model]
```

Router projection 为：

```text
W_r [d_model,E]
R = X W_r              [B,T,E]
P = softmax(R,-1)      [B,T,E]
```

对每个 token，选择概率最高的 `k` 个 expert ids，形成集合 `S(x)`。抽象输出：

```text
y = sum_(e in S(x)) g_e(x) * Expert_e(x)
```

`g_e(x)` 是选中 expert 的路由权重，可能在 top-k 集合内重新归一化。不同架构可使用 top-1、top-2 或其他 routing，稳定问题都是“谁被选中、权重多少、负载怎样”。

Linear router 保留输入在方向上的符号；另一条受限分支为每个 expert 学正交低秩基 `U_e`，用 `κ_e ||U_e^T x||²` 作为 softmax logit，让相反方向但相同投影能量得到同一 affinity。[子空间路由的原版本机制](https://arxiv.org/html/2602.17798v1#S3)改变的是如何度量 token 与 expert 的匹配，不证明这些子空间就是独立语义专家。基与 concentration 仍需训练；固定 logits 时增大共同尺度使熵下降，是所有 softmax 的性质，不是此路由独有的无 collapse 保证，论文的 balance 界也依赖 uniform mixture 与 affinity separation。原 Algorithm 1 求和全部 experts，软概率变尖不自动跳过计算；若要稀疏执行，Top-k/threshold、capacity 与 dispatch 仍须另验。每 token 的投影路由为 `O(N d k_r)` 而非 linear 的 `O(N d)`，还增加基约束与校准成本；已披露主要实验配置限350M/1.3B，不能把未对应的摘要规模或局部负载收益外推为所有 corpus 保证。符号信息有用、负载或质量回归、计算不合算时，linear router、auxiliary loss 与原 dense/shared 路径继续合理。<!-- source-family:SF-2026-ARXIV-2602-17798 -->

## 一个 top-2 小例子

假设 `E=4`，某 token 的 router probabilities 为：

```text
P = [0.10,0.60,0.20,0.10]
```

Top-2 选择 expert 1 和 2。若在选中集合内归一化：

```text
g_1 = 0.60 / (0.60+0.20) = 0.75
g_2 = 0.20 / (0.60+0.20) = 0.25
```

若两个 expert outputs 为：

```text
E_1(x) = [1,0]
E_2(x) = [0,2]
```

组合输出：

```text
y = 0.75*[1,0] + 0.25*[0,2]
  = [0.75,0.50]
```

此 token 没有执行 expert 0 和 3。实际系统还要把 token dispatch 到持有这些 experts 的设备。

## Total parameters 与 Active parameters

设单个 expert MLP 参数量为 `P_expert`。忽略 router 和共享层：

```text
total expert parameters  ~= E * P_expert
active expert parameters ~= k * P_expert per token
```

当 `E` 增大、`k` 固定时，总容量可扩展，而单 token expert compute 主要由 `k` 决定。

但整模型 active compute 还包含 Attention、shared layers、router、communication 与 combine。不能用 `k/E` 直接声称端到端 FLOPs 或 latency 同比例下降。

稀疏执行也不必意味着只有被选 expert 的参数参与构造。一个替代分支把每层多个基底的参数以 token-independent 有符号系数组成有限 block codebook，再让 token 只选少数合成 blocks 执行；参数参与、实际 nonlinear block 执行与派生权重 materialization 是三项不同预算。预合成只对固定权重和合成配置有效，不能把 `f(sum W)` 当作 `sum f(W)`，也不保证每个基底在每次请求都有非零或可解释贡献；full participation 因而不是 dense 全执行的同义词。

合成移出请求路径不等于合成成本消失：缓存 blocks 增加 memory，训练更新或量化/布局改变后须重新合成并验收，较小 expert pool 下甚至可能缓存更多派生权重。受限 parameter-matched 训练同时改变模块与 routing，不能将全部质量收益归于参与方式；图像任务的 cache 实测也不替 LLM 的 runtime、通信或 SLO。权重 identity、量化数值或 memory 预算不成立时，保留普通 Top-k expert、按需 materialization 或原 dense 路径，不由一个 active-parameter 数字授权整图提速。 [必要机制与反证](https://arxiv.org/html/2609.21346v1)。<!-- source-family:SF-2026-ARXIV-2609-21346 -->

## 为什么负载均衡是模型正确性的一部分

如果 router 总把 tokens 送到少数 experts：

- 热门 expert 超载或产生排队。
- 其他 experts 缺少训练信号。
- 矩阵 batch 不均匀，硬件利用率下降。
- 超出容量的 tokens 可能被丢弃或转发。

理想路由同时追求 specialization 与 balanced load，但二者可能冲突。训练通常加入 auxiliary load-balancing objective，让平均 router probability 与实际 token assignment 不要过度集中。

Auxiliary loss 是代理约束，不证明所有 experts 语义均匀，也不保证每个 batch 完全平衡。权重过强还可能牺牲内容路由质量。

同样，某 expert 在一个领域中经常被选中，并不等于它对该领域输出最重要。可以在固定输入与冻结模型下分账测量：先记录原 router 的选择频率，再对某个 expert 的 pre-softmax gate logit 作规定幅度扰动，观察输出分布 KL 的变化。[受限 MoE 探测](https://arxiv.org/html/2601.10159v1)因此把 domain activation 与 routing sensitivity 配对，而不是用热门 expert 直接命名“数学专家”。后者仍是局部扰动敏感性：logit 改变可能同时改变 Top-k membership 和其他 expert 的相对权重，不能视为隔离单 expert 功能的因果干预。<!-- source-family:SF-2026-ARXIV-2601-10159 -->

这条诊断分支增加重复 forward、扰动和评价成本；不同输入、层与扰动幅度须保留身份。三个 checkpoint 与三个任务的局部结果不支持通用专家本体或句首 driver 定律，词面、长度与位置也未被完整配对控制；原文 specialization 指标定义与高低口径不一致，不能照搬阈值选 expert。单纯调 gate 与额外 router LoRA 训练应分别计费，未披露的精度、seed 和端到端预算不能补猜。频率与敏感性不一致时保留原 router 和质量验收，再决定是否调整；负载与 capacity 仍由下面的执行约束负责。

路由频率以外，输入表示的多个因素还可能落到同一个共享路由组合上；均衡 token 数并不隔离这种 composition collision。一条受限替代分支把 post-attention 表示切成若干 head slices，各用 private router/bank 将切片映射到完整维输出，再求和，使路由组合与总/激活容量成为可分别比较的对象。切片和线性 probe 不认证真实语义因素，也不保证仍对应原 attention head 的功能；不采用原文遗漏被更新 composition 负贡献的一般遗忘下界。[必要机制与匹配预算对照](https://arxiv.org/html/2602.12587v1)支持有限持续学习中的这一容量组织，但任务与 head 数有反退，不能称消除遗忘。它增加 router、训练、聚合与 dispatch/通信成本；组合诊断不稳、质量或执行预算回归时，仍保留共享 router、原 expert pool 与独立 retention 验收，不由更丰富组合自签 specialization。<!-- source-family:SF-2026-ARXIV-2602-12587 -->

从探测转向编辑时，冻结 router 参数仍不等于保留原路由：某层 expert 的 down-projection 输出改变后，后续层 router 消费的 hidden input 也会改变。一条有限 preservation 分支先收集应保留的 expert 输入，将更新投影到这些 keys 协方差的低特征值子空间，再按固定 gate 权重联合拟合多个 active experts 的输出；block coordinate 更新处理它们在同一 token 输出上的耦合，而非让每个 expert 独立取得全部目标变化。只有固定 features/gates 下的**精确 nullspace**满足更新乘 preservation keys 为零；阈值选择的 near-null 子空间只是近似约束，未采到的输入与 Top-k membership 变化仍需另验。<!-- source-family:SF-2026-ARXIV-2602-10965 -->

协方差采集、投影、缓存与局部线性求解把一部分成本前移，但不让路由稳定成为免费或全局保证。[MoEEdit 的受限对照](https://arxiv.org/html/2602.10965v1)有同方法去 projection 的局部支持，也有编辑层范围不一致的跨方法混杂、泛化指标退步及非零 routing KL；小扰动 softmax 分析略去 Top-k，不能替代离散边界验收。保留人口、regularization、编辑层与 preprocessing 成本应进入同一 artifact identity；路由或保留任务回归失败时，恢复未编辑 reference、原 router 与独立质量检查，而不是凭参数冻结自授输入不变。

路由权重解释了单个 token 如何使用容量，负载均衡则约束一批 token 如何共享容量。即使训练目标鼓励均衡，某一轮仍可能拥挤，因此执行前还需要明确每个 expert 能接收多少 token。

## Capacity 怎样约束 Expert

一个常见抽象是为每个 expert 设置 token capacity。令 `N` 为本轮参与路由的有效 token states 数；没有 padding 或被屏蔽位置时可取 `N=B*T`。Top-`k` 会产生约 `N*k` 次 expert assignments，平均每 expert 负载为：

```text
average load = N * k / E
```

Capacity 可以写成：

```text
capacity ~= capacity_factor * N * k / E
```

`capacity_factor > 1` 提供不均衡余量。具体论文与实现对 batch、group、rounding 和 top-k 的定义可能不同，这个公式只用于理解方向。

当 token 超出 capacity，系统可能 drop、选择备选 expert、增加 padding，或采用 dropless execution。每种选择都会影响质量、显存、通信和吞吐。

## Expert Parallelism 为什么需要 All-to-All

Experts 分布在不同 GPU 上时，本地 token 未必选择本地 expert。系统必须按 destination 重新排列并发送 tokens：

```text
local token states
-> dispatch by expert id
-> All-to-All
-> local expert GEMMs
-> All-to-All return
-> restore original token order
```

逻辑上，dispatch 输入可看作 `[N,d_model]` token states 和 `[N,k]` routes。物理上需要 grouped GEMM、padding 或动态 shape 来处理每个 expert 的不同 token count。

Grouped GEMM 不是把 MoE 改成一个数学上的稀疏矩阵乘法。它把多个共享 dtype 和部分 layout 约束、但拥有不同 `M_e` 的 expert GEMMs 交给一次 library/kernel 调度：减少逐 expert launch 和 padding 机会，却仍要处理空 expert、长尾 `M_e`、metadata、对齐与负载不均。Dense GEMM、grouped GEMM 与通信融合属于第49章的 execution mapping；本章只拥有 router 如何产生这些不规则 expert batches。

Expert Parallel 与其他并行维度不同：

```text
Tensor Parallel    split one operator
Pipeline Parallel  split layer depth
Data Parallel      split samples
Expert Parallel    split expert set and dynamic token routes
```

组合后 process groups、checkpoint 和容错都会更复杂。

## Combine 把动态路径还原成同一个 Layer 输出

上面的 return 只把结果送回来源设备，还没有完成模型语义。系统要按原 token 与 expert assignment 恢复对应关系，再使用该 token 的路由权重加权求和；top-2 例子中的 `[0.75,0.50]` 正是这一步的结果。忽略容量溢出的特殊处理，并将有效位置回填原 batch/sequence 布局，逻辑形状可以写为：

```text
expert outputs associated with routes [N,k,d_model]
+ route weights                       [N,k]
-> weighted sum over selected experts [N,d_model]
-> restore batch / sequence layout    [B,T,d_model]
```

至此，router 选择、负载约束、capacity、dispatch、expert compute 与 combine 构成一个闭环。它替换的是 MLP 内部路径，输出仍可接回原 Layer 的 residual stream；后面各条分支改变的是这个闭环的不同约束，不能绕过输出对应关系和质量验收。

## 通信为何可能吃掉稀疏收益

MoE 减少的是未选 expert GEMMs，但新增：

- Router projection 与 top-k。
- Token permutation、packing 与 metadata。
- 跨设备 All-to-All。
- 不均衡造成的小 GEMM 或 idle time。
- Expert weights 的总存储与加载。

互联较慢、batch 较小或路由高度不均衡时，MoE 可能无法把 active FLOPs 优势转成 latency/throughput 优势。

所以性能结论必须绑定 `E`、`k`、expert batch、topology、precision、sequence 和并行策略。

## 推理时为什么仍然不免费

推理中 Router 仍逐 token 决定 expert。Batch 内 tokens 可能分散到多个 experts，Decode 每步 token 数又可能较少，导致 expert GEMM 难以形成高效率大矩阵。

总 expert weights 也必须放在 GPU 集群、CPU 或其他层级。Active parameters 少不等于 total capacity 不占存储。

在线系统还需要考虑：

- 请求之间路由分布是否稳定。
- Expert placement 与热点。
- Tensor/Expert Parallel 的拓扑。
- 每步 All-to-All 对 TPOT 的影响。
- 容量不足时是否允许 drop。

模型 router 已经决定这些运行时策略必须存在。本章后半只解释它们如何约束模型语义与部署身份，具体调度、通信实现和性能调优仍交给训练与推理系统章节。

### 稀疏收益取决于 Expert Branch 在整网中的 Compute Leverage

<!-- semantic-body-binding:SF-2026-ARXIV-2605-15484:start -->
只报告 active parameters 或固定 top-k，在 expert branch 占整网计算的大部分时能近似说明节省；若 backbone 的 dense 部分主导 FLOPs，同样的稀疏率几乎不改变总成本。matched-compute 评估因此要显式记录 expert-compute ratio、top-k、dispatch axis 与整网 FLOPs，而不是把 router 局部稀疏直接升级为系统收益。模型 owner 决定可访问容量，executor 才测量实现后的真实 leverage。

提高 expert branch 占比可以放大条件计算收益，也会放大 routing error、capacity overflow 和通信；只调整 top-k 甚至可能在固定架构下反转 sparse-vs-dense 排序。batch-axis Soft-MoE 在 per-sample CNN 中还可能跨样本混合不该共享的状态。exact-v1 只支持 §3 的 hard/soft routing、§4–5 的视觉模型与受控 sweep，不证明该阈值跨 Transformer、硬件和 workload 普适。leverage 低、batch 语义不允许混合或通信成为主导时，应回退 Dense/较小 expert pool 或重新设计 backbone，而不是继续增加 experts。<!-- source-family:SF-2026-ARXIV-2605-15484 -->
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15484:end -->

## 扩大容量时，先决定稀疏单位与共享边界

基础闭环已经成立，但“更多参数、较少激活”还没有决定参数应放在哪里。以下分支分别改变架构预算、共享方式、路由单位和序列单位：它们可以在条件允许时组合，也可能相互冲突，不能排列成所有模型都应依次升级的路线。

### Total / Active Parameters 只是约束坐标，不是架构答案

`total parameters` 近似描述权重容量与存储压力，`active parameters` 近似描述单 token 经过的 expert
compute；它们是比较 MoE 的必要坐标，却不能唯一确定 architecture。相同两个预算仍可能由不同的
depth `l`、width `d`、expert count `E`、Top-K `k` 与 expert granularity `g` 组成：

```text
memory / parameter budget
-> choose depth, width, expert count and granularity
compute budget
-> choose active experts and dense-core size
-> derive executable dispatch and communication shape
```

增加 experts 会扩大可路由容量，但为了守住固定 total budget，可能迫使 dense core 变窄或变浅；增加
Top-K 可能让更多容量参与单 token 计算，却同步增加 GEMM、dispatch 与 All-to-All。相同 sparsity ratio
`E/k` 也不表示相同质量或系统成本，因为 `E` 和 `k` 分别改变 weight residency、expert batch、routing
choice 与 communication fan-out。

总容量相同也不能只按深度单调增加 experts：冻结同一 backbone、固定 router、replay 与 load-balancing 目标后，改变各层专家分配仍会影响不同任务的收益与遗忘。[HuBERT 上的有限分配对照](https://arxiv.org/html/2602.12746v1)把24层分四组，各组六层分别配2/4/6/8个 LoRA experts，实际120个专家实例而非全模型20个；更偏深层的同预算方案并未更好。它支持按层分配作为独立配置轴，不授 speech 或其他 LLM 的通用 depth 规律；ASR/LID readout 不同、英语保留及部分指标反退都须分别验收。专家驻留、Top-K 路由、replay 与任务 readout 有实际费用，trainable 比例不等总内存或时延；人口、readout 或执行预算改变后重新校准，收益不稳时保留固定分配、普通 LoRA 与已验证 replay，不以深层路由频率代替功能证据。 <!-- source-family:SF-2026-ARXIV-2602-12746 -->

小中规模搜索中拟合出的 exponent 可以帮助生成候选，不能成为跨规模定律。真实设计还必须把 HBM、
parallel divisibility、load imbalance、topology、kernel efficiency、training tokens 与 Serving SLO 加入
约束；当这些条件变化时，论文搜索空间内的“最优”也会变化。因此 total/active parameters 继续作为
model-card 粗 contract，architecture search 则必须用 loss evidence 与 system cost model 联合裁决。

同宽 expert 让 GEMM、placement 与容量估算简单；若不同 token 确实需要不同 FFN 宽度，可以先路由到宽度组、再选组内 expert。结构预算随之多出两层责任：模型 owner 选择宽度与组间/组内路由，执行 owner 则决定每设备是否放置跨所有宽度组的一套 expert。后者能使**静态参数组合**对称，却不能保证动态 token 工作量或 GPU 时间对称；组内路由、padding、通信和真实利用率仍需分别验收。宽度选择错误、窄组欠训练或大 expert 热点会破坏收益；布局成本高或质量差异不足时，同宽 expert 与固定 placement 仍是可靠路径。[异宽分组的 exact-v1](https://arxiv.org/html/2604.23108v1)只给受测模型的质量、路由比例与布局证据，不把 activated parameters 或难度 proxy 升格为真实时延保证。

<!-- source-family:SF-2026-ARXIV-2604-23108 -->

另一条宽度分支不增加不同宽度的 expert 组，而在同一个 expert 内共享嵌套 prefix：上投影取前若干列，下投影取对应行，使较窄路径复用较宽路径的参数。要让这些切片可用，训练同时计算全宽和随机宽度的 loss；它增加双 forward 成本，也要求不同 prefix 获得足够训练，不是对任意既有 checkpoint 做无代价的 post-training 弹性化。router 仍先选择 experts，随后才把已选 expert 的概率映射为宽度，不能把“切同一 expert”与“去另一个 expert”当作相同容量决策。

宽度映射可以用概率的幂变换调节集中程度，再按目标额度分配、裁剪和离散化；但裁剪后的实际总量未必严格等于输入额度。受测配方为各额度冻结 backbone/router、用有限校准数据选择一个映射参数，不能把校准最优推广到任意输入或精确预算控制。[受限原始证据](https://arxiv.org/html/2602.06154v1)只支持从初训中学习多宽 prefix 的质量—MFLOPs 取舍，未验证任意后训练弹性、真实 latency 或 Agent/self-speculation 应用；离散切片的梯度实现也未在必要原文中充分披露。prefix 欠训练、校准失配或真实执行成本不合算时，固定宽度或已验收的异宽分组仍是合理回退。<!-- source-family:SF-2026-ARXIV-2602-06154 -->

固定 `depth / width / top-k` 的 MoE 最容易分别优化训练与 Serving；当同一权重族要覆盖多档 latency、memory 与 cost budget 时，可以把这些选择变成训练期采样的 subnetwork path。这样一次训练产生多个执行点，却把“模型版本”扩成：

```text
shared checkpoint
+ active depth / expert subset / top-k profile
+ profile calibration and quality envelope
+ kernel / collective / placement plan
```

共享参数会让不同路径的梯度互相干扰，低频子网可能欠训练；每个 profile 还需要独立的 quality、capacity 与 SLO 验证。固定模型在 workload 稳定、极致性能或认证边界严格时仍更容易优化。Elastic super-network 因而是 deployment portfolio 的条件分支，不是 MoE 的默认终点。

### Shared-first 与 Routed-residual 是另一种容量分工

传统 MoE 先由 Router 决定 token 进入哪些专家，公共能力也可能被稀疏路由切碎。另一条分支让共享路径先承担稳定公共变换，再只把剩余误差交给专家路由；它降低了公共知识对路由抖动的敏感性，却会把共享层变成新瓶颈，并不能消除 expert collapse。两种结构应按公共容量、路由熵、通信和尾部质量共同验收，而不是把 shared-first 当作无条件升级。
<!-- source-family: arxiv:2608.10392v1; semantic-body-binding: shared-first-routed-residual-capacity-boundary -->

共享 forward 并不阻止 routed experts 在训练时继续追逐同一更新方向。若公共容量用固定左右谱基的投影 $P_U,P_V$ 表示，可以把一次梯度 $G$ 拆成 common 更新 $P_UG+(I-P_U)GP_V$ 与 unique 更新 $(I-P_U)G(I-P_V)$，分别交给公共权重和双侧互补的 expert 权重；后一项在固定基下避开两侧 common 坐标，前一项却可有两个交叉分量、rank 达到 $2k$，不是天然 rank-$k$ 更新。这是 update authority 的分责，不等于专家语义互斥。[SD-MoE 的受限证据](https://arxiv.org/html/2602.12556v1#S3)每16步刷新 SVD 基，但参数、optimizer 与基更新后是否重新对齐仍需独立检验，不能把固定基投影性质延伸为整个训练持续严格正交；刷新和不同学习率也有成本，所测吞吐约下降5%，且存在任务反退。应同时验收实际参数子空间、质量和训练预算；刷新漂移、尾部任务掉分或成本不合算时，普通共享路径、原 routed MoE 与 dense 仍是合理回退。<!-- source-family:SF-2026-ARXIV-2602-12556 -->

已有 dense checkpoint 转成 shared/routed 分工时，也不能只按权重大小拆专家。一个条件初始化分支先在校准样本上统计 SwiGLU gate 的输入激活 profile，以跨样本变动决定各层共享比例，把稳定高激活 neuron 留在共享路径，其余聚类成专家；切片须保持同一 neuron 的 gate、up、down 对应，router 可由 gate 向量初始化。但初始化方便不表示函数保持：剪枝时的无权重求和与继续预训练时的 softmax 加权已是不同计算。[ExpertWeaver 的有限对照](https://arxiv.org/html/2602.15521v1#S3)中，25% active sparsity 仍明显掉分，全部权重仍存，校准及 200B token 继续预训练、SFT 也有成本；固定单 GPU 并发的吞吐收益不能推广成总训练更省或所有负载 SLO 改善。于是共享比例与 expert 切片应绑定校准人口、计算函数和训练 artifact，验收质量、权重驻留及实际 dispatch 成本；分布失配或预算不合算时，原 dense、原生 MoE 和更充分训练仍是共存选择。<!-- source-family:SF-2026-ARXIV-2602-15521 -->

### 先改变通信坐标，再扩大稀疏容量

标准 MoE 在 `d_model` 维 token state 上 routing、dispatch 和 expert compute。增加 experts 可以扩大总容量，但每个 assignment 搬运的 payload 仍与 hidden width 绑定；当 All-to-All bytes 或低延迟下的 expert weight load 成为瓶颈时，仅继续增加 experts/top-k 会放大系统压力。

一个条件分支是在 routing 前先把表示投影到较窄的 latent coordinate，在 latent space 完成 expert dispatch 与计算，再上投影回主干：

```text
full-width token state
-> down projection to latent coordinate
-> route and dispatch latent state
-> latent expert compute
-> up projection to full-width residual path
```

这把优化顺序从“先扩大 expert set，再补通信优化”改成“先降低每次 route 的 state width，再决定容量和 top-k”。收益是 routed weights 与 All-to-All payload 有机会随 latent width 缩减；代价是 down/up projection、latent information bottleneck、更多 expert-placement 组合和新的初始化/训练耦合。Router、shared path 或需要高保真表示的层也未必适合全部压入同一 coordinate。

Dense MLP 在模型较小和 portability 优先时仍合理；标准 full-width MoE 在互联充足、机制简单和质量可预测性更重要时继续成立。Latent-coordinate MoE 只有在 projection cost、信息损失与 placement 复杂度能被 communication/weight-read 收益覆盖时才有意义。模型报告中的整体能力与 Serving headline 不能证明这一个组件的独立贡献。

### 从完整独立 Experts 到组内与跨层参数共享

另一条降低 small-batch weight traffic 的分支不缩小 token coordinate，而是改变 experts 的参数独立性。标准 MoE 为每个 expert 保留完整 MLP，提供最大的专门化自由，却会在一次请求命中多个 experts 时搬运大量相似权重；department-style 组织让一组 experts 共享 trunk，仅保留较小 private delta，并用两级 router 先选组再选私有分支：

```text
token state
→ route to shared department trunk
→ route to small private expert delta
→ combine into residual path
```

共享提高 weight reuse、缩小工作集，却用表示耦合、两级 routing 与潜在 expert interference 换取内存收益。需要强独立专业化、共享部分形成负迁移或大 batch 已能摊薄独立 weight load 时，标准 experts 仍更合理。`arXiv:2608.14385v1` 只在作者的 7B pretraining 与 DeepSeek-V3 microbenchmark、A40/H100 配置上支持这一 operating point，不证明跨节点吞吐、训练稳定性或语义专业化普遍改善。

<!-- source-family:SF-2026-ARXIV-2608-14385 -->

跨层也可以共享 expert parameters，同时保留每层独立的 attention 与 router。这样减少的是 resident expert weights 和对应 optimizer state，不是逐 token active compute；每层 router 仍拥有自己的 token dispatch，不能因为底层参数相同就合并路由统计。共享版本必须作为单一 expert artifact 更新，而 layer-local routing receipt 继续分别保存。

这种 tying 用近似成倍的 expert-memory 缩减换取层特化能力和更新独立性，多个层对同一权重的梯度还会形成新的耦合。目标模型确有跨层冗余、memory 是主瓶颈且 kernel 能复用布局时，这是一条可选分支；质量回归、并行布局不利或层间功能差异明显时，应回退独立 experts。作者模型与训练规模只证明该 operating point 可行，不支持所有 MoE 都存在相同冗余。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.16825 -->

### 稀疏单位也可以从 FFN 提升为状态更新 Block

<!-- semantic-body-binding:SF-2026-ARXIV-2605-09516:start -->
条件计算也可以把稀疏单位从 FFN expert 提升为 thin layer block。传统 token-to-expert MoE 保留完整层深，router 只决定每个 token 进入哪些 FFN；这在需要稳定全局读、kernel 主要围绕 expert GEMM 优化时仍最容易执行。若约束变成“层级状态更新本身也应按输入选择”，block router 可以提出少量 thin blocks，同时保留 shared softmax attention 负责全局读取，让 routed recurrent/Delta-style block 承担稀疏状态更新。Router 只拥有 block proposal，residual path 和训练目标仍决定这些更新如何组合。

这条分支扩大了条件容量的粒度，却引入低秩宽度上限、dispatch 碎片、专用 kernel 缺口和训练不稳定；纯 routed attention 还可能丢失全局覆盖。现有证据限作者的模型、数据、实现和 evaluator，不能外推到任意规模、硬件或 SLO。全局访问不可牺牲、路由难以校准或执行栈只能高效支持完整 block 时，dense block 或传统 expert FFN 仍是正确回退。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-09516:end -->

### Expert 粒度缩到向量后，Router 与执行顺序都必须重写

传统 MoE 把一个完整 MLP 作为 expert，router 的候选数有限，选中后的 token batch 也容易交给 grouped GEMM；
它在显存和通信可接受时保持了清晰的模块边界。把 expert 继续细化到 vector-level atomic unit 可以扩大组合容量，
却让平坦路由的候选空间、随机 weight lookup 和小算子数量同时失控。此时不能只减小 expert 而沿用旧执行路径：
router 可以把大索引分解为 Cartesian-product coordinates，executor 则从 token-centric gather 改为
expert-centric scheduling，把共享同一 atomic expert 的 token 聚集后执行规则矩阵运算。

```text
token state
→ factorized atomic-expert coordinates
→ selected atomic expert set
→ expert-centric regrouping
→ dense batched execution
→ combine into shared residual path
```

模型层拥有 factorization、shared dense branch 与 combine semantics；runtime 只拥有 permutation、batch formation 和
kernel plan，不能为了 GEMM 方便改写已选择的 atomic experts。更细粒度换来更大组合空间，也新增 coordinate
collision、router calibration、irregular regroup、metadata 与 shared-branch 归因问题。候选规模小、batch 太小、
通信昂贵或 kernel 不支持稳定 regroup 时，粗粒度 expert 仍更合理。exact-v1 只在作者的模型、七个 benchmark 与
实现上支持机制可行性，不证明 atomic granularity 普遍优于 coarse/fine-grained MoE。

<!-- source-family:SF-2026-ARXIV-2602-05711 -->

### 不经过平坦 Expert Router 的树形条件计算

平坦 Top-K 易于把 token 分组成 expert batch，但候选集合扩大后，routing 和聚集本身也会成为成本。一条替代分支把 FFN 的计算单元组织成多棵二叉树：每个 token 只走一条 root-to-leaf 路径，节点的线性响应同时决定下一分支并贡献输出，而非先由独立 router 选出完整 MLP experts。硬选择使用停止梯度，只有被访问节点参与该路径的计算。这保留输入相关的条件容量，却把平行 expert 选择换成顺序 traversal；更少激活不意味着现有 GPU 上必然更快。

树形组织也没有自动消除负载偏斜。若节点响应先经 GELU 再累加，正负响应的梯度不对称可能使部分路径逐渐失去利用率；把非线性移到稀疏累加之后可以改变这种偏置，却未必改善最终任务质量。另一种选择是利用稳定低访问路径做结构剪枝，让一部分动态稀疏固化为静态稀疏。这里要分别验证路径利用、剪枝后的质量和实际执行成本，不能把“更均匀”或“更稀疏”直接等同于更好模型。

这种机制需要重新训练或有受控条件的适配，并引入深度串行依赖、硬路由梯度限制及专用执行支持。作者的受测 GPT/OPT 模型说明它可形成条件计算分支，但同 token 预算的部分从零训练结果仍弱于 dense baseline，利用预训练 Attention 的微调结果不能冒充完全相同的从零训练对照。其效率讨论明确保留理论/模拟与非即用部署边界，因此不据 layer-level headline 推出端到端 Serving 收益。Dense MLP 或常规 MoE 在成熟 kernel、质量可预测性和简单部署更重要时仍成立。

<!-- source-family:SF-2026-ARXIV-2604-08565 -->

### Conditional Compute 之前也可以先压缩 Sequence

标准 MoE 在 token sequence 上逐 token routing，保留最直接的语义与位置边界；长上下文下，attention state
和 expert dispatch 都随 token 数增长。一条实验性分支先由 encoder 把相邻 tokens 聚成可变 concept/chunk，
在压缩序列上执行 MoE，再由 decoder 展开：

```text
tokens → learned boundaries → concepts → MoE compute → dechunk / decode
```

这不是“MoE 自动获得更长上下文”。Compression ratio 同时改变可见状态长度、每个 concept 的 active
compute 和重建难度；边界漂移会把不同语义错误合并，过强压缩尤其损伤需要细粒度步骤的 reasoning。
Token-level MoE 在精确 alignment、短序列或边界不稳定时仍合理；concept route 只有在压缩收益能覆盖
encoder/decoder、重建误差与专用 kernel 成本时成立。论文的 matched-compute 与 Hopper 结果只证明所列
模型和长度上的分支可行性，不构成通用最优比例。

### Expert Pool 可以扩展，但 Expansion 也属于 Checkpoint Identity

一次性训练最终规模的 expert pool 要在开始前冻结容量，并为尚未证明有用的专家支付训练和通信成本。渐进扩展让模型从较小 pool 开始，在后续阶段复制或初始化新 expert、继续训练并调整 token budget；它把“模型容量”从静态超参数变为训练过程中的可迁移状态。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13247 -->

因此 checkpoint 不能只记录权重，还要记录 expansion stage、router revision、expert mapping、optimizer state 和 learning-rate continuity。扩展可能复制对称性、扰动 routing 或让新 expert 长期欠训练；受限实验规模小于 frontier MoE，scaling fit 也未覆盖所有 optimizer 超参数。路由不能重新平衡或阶段迁移不稳定时，应回退固定 expert pool，或延长当前阶段再扩容。

扩展时还要回答“复制谁”，而不是只决定增加多少专家。保留已有 expert 的 warm start，可以减少从零形成能力的阶段；按梯度或 saliency 的有限 utility 代理选择复制对象，试图把新增容量放在当前训练分布较有用的位置。但代理大不等于新 expert 必然学到互补能力：复制同时带来对称性和 router 重新分配，后续 CPT 不足时收益仍可能消失。固定 top-k 只约束单 token 选择数量，不使新增 weight、optimizer state、驻留和通信成本自动为零。

因此扩容收益要按完整训练路线记账：先前训练是否为沉没成本、复制/扩展操作、继续训练预算、最终质量与下游回归分别报告，不能将“只算扩展后的省时”和“从头训练的总预算”放在同一个比例里。[受限 MoE 对照](https://arxiv.org/html/2604.19835v1)支持 utility-copy 这一选择分支，凸 OCO 里的共享最优解/提升假设却不是非凸网络的收敛保证；目标分布改变、复制偏置或 CPT 预算不足时，延长当前阶段、均匀扩展或固定最终 pool 仍是合理替代。<!-- source-family:SF-2026-ARXIV-2604-19835 -->

### Expert 数量改变后，超参数也需要架构身份

Dense FFN 或固定 expert 配置中，直接复用一组已经调好的 learning rate、初始化尺度和 width scaling，在架构不变时成本最低，也容易比较实验。当 Dense FFN 被拆成更多、更窄或更宽的 experts 后，总参数、单 token active parameters、router 分配和每个 expert 实际接收的样本量不再同步变化；此时把旧超参数原样搬过去，会把“条件计算机制是否有效”与“参数化是否失配”混在同一次训练里。

更稳健的演进是把超参数从某个 checkpoint 的经验数字提升为带架构坐标的 scaling identity：training owner 明确 dense width、expert width/count、top-k、初始化与 optimizer scale 之间的变换，router 仍拥有 token-to-expert 选择，runtime 仍只执行已发布的稀疏路径。这样可以减少每一种 MoE 形态都重新网格搜索的成本，并让 dense-to-MoE 对照更可解释；代价是参数化公式本身也要经过规模、数据和 optimizer family 的校准，错误迁移会表现为训练不稳、expert 饥饿或把架构差异误判成优化收益。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23893:start -->
当架构变化很小、训练预算足以独立调参，或目标 optimizer/数据分布离校准域很远时，逐配置 tuning 仍是可信 fallback；统一 scaling rule 是可迁移的起点，不是免调参保证。`arXiv:2605.23893v1` 的 §3 与 §5 支持在作者披露的 Dense FFN/MoE 配置间构造并评估这类超参数迁移，§6 不证明任意 expert topology、模型规模、数据或 optimizer 都保持最优。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23893:end -->

这里还需要把 `activation ratio` 与 expert count 分开。总参数相同、active parameters 相近，并不保证每个 expert
接收相同频率或拥有相同梯度噪声；稀疏度变化会同时移动最优 learning rate 与 batch size，不能只用 total/activated
parameter count 解释。训练 recipe 因而应把 activation ratio、routing rule、data/token budget、optimizer 与 schedule
共同绑定到 architecture identity，在固定 active compute 的对照中重新校准，而不是把 dense 或较密 MoE 的超参数直接外推。

更细的 scaling law 可以减少全网格搜索，却仍是 empirical prior。`arXiv:2609.08690v1` 用 1,800 次 pretraining runs、
最高 6B non-embedding parameters 和 held-out 12B、1/64 active MoE 支持“activation ratio 是额外坐标”；其证据只来自
单一 hybrid linear-attention/MLA backbone、Muon、特定数据和 sigmoid auxiliary-loss-free routing，validation loss 也不等于
下游能力。架构、optimizer 或 routing 超出该校准域时，应回退邻近规模 sweep，而不是沿拟合幂律盲推。

<!-- source-family:SF-2026-ARXIV-2609-08690 -->

## 路由训练与状态：均衡、选择和贡献不能混成一个目标

改变容量组织后，下一问是 router 如何学会使用它。基础 auxiliary loss 只限制负载集中；计算是否值得、expert 是否获得有效训练以及输出贡献多少，需要不同证据。先分清训练信号，再讨论从 batch 内统计、历史状态或外部记忆产生路由的分支。

### 负载代理与计算价值 Teacher 分开验收

计算价值 teacher 与负载稳定 auxiliary 还要分开验有效性。在 conditional-depth 的 full/cheap 当层分叉上，用未来层全部执行 full 的 loss 差作稳定标签，衡量的是该未来策略下的局部价值；部署 gate 若只允许部分未来层 full，标签并不自动代表其真实预算下的价值。quality teacher 应绑定分叉状态、未来执行策略与实际 gate，而 load/util/rank proxy 仍只管理稳定性，不因它可优化便取得任务收益真值。<!-- source-family:SF-2026-ARXIV-2604-17228 -->

生成标签需要额外分支执行，按部署策略重估也可能增加噪声和训练成本。原文小 frozen backbone 的消融中删除某些辅助项能改善部分配置，但没有 on-policy oracle 或充分权重扫描，不能把 future-policy mismatch 定为唯一原因，低预算两 seed 还有反向结果；披露的 V100 窄壁时也不是完整服务收益。固定预算 proxy 在负载稳定优先时仍合理，价值标签失准则应降低其权重、重做匹配策略的校准或回退无 teacher 的已验收路由，而不是称所有 auxiliary 均有害。<!-- source-family:SF-2026-ARXIV-2604-17228 -->

训练期的 assignment 信号还可以来自外部 dense 模型的 feature 空间，而不只由当前被选 expert 的任务梯度产生。一条受限分支冻结 dense feature backbone，在其中间特征上另训练受负载与熵约束的辅助 router，再把辅助 router 的分布作为 stop-gradient 目标，以 KL 约束 student router。冻结的是 feature 提供者，不是辅助 router；这为稀疏任务反馈提供较平滑的选择目标，却不使均衡 proxy 成为每个 token 应由哪个 expert 处理的语义真值，也不同于从已有激活路径虚拟移除 expert 所得的任务贡献先验。<!-- source-family:SF-2026-ARXIV-2604-21330 -->

指导时长、teacher 所读层位和额外资产必须一起验收。所测视觉模型中，早期指导、末层特征与只模仿路由出现不同甚至反向结果；外部 router 在线参与的 upper bound 不是 student 的部署收益。dense teacher、特征计算和辅助 loss 增加训练成本，原文的 epoch 时间与不含 teacher 的参数计数也不能证明零开销或任意 LLM 路由稳定。任务反馈充分或指导失配时，应保留原 Top-k 联合训练、缩短指导时程或回退已验收的负载约束，并分别测任务质量与真实执行负载。<!-- source-family:SF-2026-ARXIV-2604-21330 -->

路由信号也可以来自当前token刚形成的attention history，而不只来自hidden-state投影或外部teacher。一个受限分支把最近attention权重的时间窗口和频域视图变为辅助expert logits，以学习gate与原router logits混合；gate表示可训练权重，不是可靠性已经校准的概率。即使attention与expert参数被冻结，只更新router也会改变expert输出，进而改变后层hidden state与attention行为；“参数未更新”因此不等于“该计算路径的行为没有被干预”。

这条耦合既可能帮助局部推理，也可能损伤检索：在受测模型中，全部层接入与仅深层接入出现不同任务取舍，不能把layer depth当成普遍功能分界，attention sink与收益相关也未证明其必要因果作用。额外视图、gate和权重materialization增加成本，所测实现的active层不能直接沿用FlashAttention；较短错误回答不证明端到端SLO改善。任务回归、窗口失配或内核成本超界时，应保留原hidden-state router、减少接入层位，并以matched任务切片与实际执行开销决定是否启用。 [原文必要机制与反证](https://arxiv.org/html/2609.20974v1)。<!-- source-family:SF-2026-ARXIV-2609-20974 -->

### Global Balance、局部负载与训练动态分别观测

负载均衡还必须区分两个时间尺度：optimizer step 的 global batch 均衡可避免 expert 长期闲置，但同一步里不同 rank 的 microbatch 即使互相抵消，仍可能在 All-to-All 和 grouped GEMM 上形成局部 straggler。用每个分片的 quantile 再取平均并不等于全局 quantile；若边际值以 BF16 表示，可按高、低字节两次汇总直方图，求得与数据分片无关的全局 order statistic，同时用有界的 local load-error gradient 修正 microbatch 路由。前者由全局路由偏置 controller 按 step 更新，后者只改变训练时 router score 的梯度；executor 不得把较低的负载 proxy 当作已测的通信吞吐。

精确 global 统计需要额外 collective，局部修正过强还会扰乱 attention logits；直接 shard-average、近似 histogram 或较简单的辅助损失在路由倾斜小、互联紧张及训练稳定性优先时仍是合理分支。作者只在一种 7.5B、256 experts、top-6 的模型和单 seed 训练上报告 global/local MaxVio 与下游结果，Local MaxVio 只是 dispatch 代理，未测真实 EP throughput，也未证明跨模型、精度或规模的普遍收益。<!-- source-family:SF-2026-ARXIV-2609-28053 -->

即使统计人口不变，负载反馈的更新律仍会改变controller动态。只按负载误差的正负给expert bias固定步长，接近平衡点时也不区分轻微和严重偏差；一个条件分支先以平均负载归一各expert误差，再用tanh软限幅，把更新去均值并经momentum EMA平滑后加到bias。bias只改变Top-k支持集，输出贡献仍使用未加bias的router scores，不能把均衡控制量当成语义权重。[SMEBU原版本机制](https://arxiv.org/html/2602.17004v1#S2.SS3)因此增加bias和momentum状态、限幅尺度与恢复时的身份管理；这是工程要求，不代表作者已经验证所有checkpoint/reset边界。归一只处理此统计口径下的量纲，不保证不同batch组成、optimizer或通信形状的动态相同。该技术报告把此更新与精度改为BF16、z-loss修复、额外auxiliary loss、dense层数及attention mask等六项共同改变，且明确未做消融，不能把loss稳定唯一归给更新律，也不能称aux-free消除了所有辅助项。更新过慢、反馈振荡或质量回归时，原sign controller、较简单的auxiliary约束与显式capacity继续合理；实际通信吞吐仍需另验，不由更平滑bias签发无振荡或省算保证。<!-- source-family:SF-2026-ARXIV-2602-17004 -->

<!-- body-source:SF-2026-ARXIV-2606-22325 -->
把 MoE collapse 从单一 load-balance 指标提升为 routing dynamics：多种平衡正则最终可进入相似退化吸引域，必须同时观察 expert specialization、token flow 与训练阶段。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；结论受模型规模、数据和 router family 限制；观测到共同吸引域不证明所有 MoE 必然 collapse。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

### Routing Information 是选择性代理，不是生产阈值

把 router 看成从输入到 expert identity 的随机信道，可以把选择信息量与 expert bank 可达到的 distortion 分开：路由携带的信息越少，控制、索引和潜在通信越容易压缩，但可区分的 expert path 也越少，任务损失下界随之收紧。这个视角补充了 load balance，却不能替代真实 token、capacity、placement 与 collective 测量；information estimator 只提供 workload-specific 选择性信号，scheduler 仍拥有执行决策权。

该分解用可分析代理换取额外分布估计，并会在 expert bank 非有限、连续路由或分布漂移时失真。估计不稳定或系统不满足假设时，应回退现有 load、quality、capacity 和通信合同。`arXiv:2605.05278v1` 只在有限预训练 CNN expert bank、MNIST 与离散选择规则中验证，理论界也较松；它不证明分布式 LLM MoE 存在通用信息阈值。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05278 -->

### 从 Batch-relative Balance 到 Population Routing State

固定 top-`k` 的优点是每个 token 的 active compute 可预测，batch 内辅助损失也容易估计平均负载；但它把
“选择哪些 expert”和“必须选择几个 expert”绑定在一起。Expert Choice 反过来让每个 expert 从当前 batch
挑选 tokens，可以精确控制 batch load，却使同一个 token 的 route 依赖同批其他 tokens，因而不适合 causal
Decode、跨请求 batching 或 batch composition 持续变化的场景。

一种中间分支把 batch 内排序压缩成每个 expert 的历史 cutoff。训练 controller 估计各 expert score 的
population quantile，并用 EMA 等状态持续更新；单 token 到达时只需比较自己的 score 与 cutoff，route 不再
依赖未来或同批 token：

```text
token-choice + fixed top-k
-> batch-level expert choice
-> population-estimated per-expert cutoff
-> causal variable-fanout dispatch
```

它获得 causal routing 与长期期望负载，却把严格 batch balance 换成瞬时负载波动。Cutoff、warmup phase、
capacity/drop policy 和估计分布都成为 checkpoint-adjacent state；冷启动、domain shift 或 workers 使用不同
cutoff revision 时，可能出现 expert starvation、零路由 token、burst imbalance 或 OOM。训练期 capacity drop
与推理期 uncapped fanout 也仍是 training-serving gap。因而 fixed top-`k` 在 strict latency/capacity 优先时
继续成立，batch-level Expert Choice 在 offline 或完整 batch 可见时仍合理；population threshold 只有在
state versioning、drift detection、admission guard 与 rollback 同时存在时才是可执行方案。

### 从中心 Top-K 到 Expert 自激活，控制面并未消失

上面的 population cutoff 仍由一个外部 Router 为所有 experts 生成分数，只是把 batch 内排序改成可因果执行的阈值比较。若 Router 的小投影难以表达各 expert 自己的适用条件，还可以让每个 expert 从输入的低秩内部 gate 计算激活强度，加可学习的 expert-local bias，再与全局阈值比较；这使选择不必经过中心 Softmax/Top-K，且每个 token 的激活数可随内容变化。它改变的是**选择信号的所有权**，不是取消了路由、预算或执行计划：训练仍要用可微代理和辅助损失控制 token/expert 负载，全局阈值仍指定密度，executor 仍需处理动态 fanout、空路由、热 expert 与容量峰值。<!-- source-family:SF-2026-ARXIV-2604-00801 -->

自激活减少中心排序的同步路径，却增加各 expert gate 的计算、密度反馈和训练稳定性约束；阈值在推理期移动还可能让质量与计算量在不同任务上异向变化。固定 Top-K 保证每 token 工作量，在严格 HBM/尾延迟预算或旧 Router 已充分校准时仍更可预测；按总体分布维护的 cutoff 也比逐 expert 内生 gate 更容易审计。现有受限证据来自从头训练、OpenWebText、最大约 0.8B 参数和九项英语 benchmark；作者的 Expert Parallel 性能模型/小尺度测试不能证明 frontier MoE 或生产 serving 的端到端收益。<!-- source-family:SF-2026-ARXIV-2604-00801 -->

### 选择支持集与输出贡献权重分别控制

路由还要分开两个经常被 softmax 混在一起的控制量：**选择哪些分支**，以及**被选分支各自贡献多少**。归一化权重容易
微分，也适合真正需要竞争性 specialization 的 top-1/soft mixture；但在声明激活 `k` 个 adapter 或 expert 时，权重高度集中
可能造成“计算了 `k` 个、有效容量却接近 1”的假象。可用 effective support 之类的量检查这一差异，而不能只看 top-k 数量。

另一条分支让 router 只产生离散 subset，被选分支使用固定贡献系数；它把支持度固定为 `k`，却放弃 input-dependent
contribution magnitude，并把训练变成 policy-gradient 或其他离散优化问题。训练时 stochastic subset 与推理时 deterministic
top-k 还会产生 distribution gap。Router policy、adapter/expert 参数、selection rule 和 contribution rule 因而必须共同版本化。
ReMix 在单一模型家族和若干任务上的结果只证明这种分责可以避免其定义下的 routing collapse；它没有覆盖大规模 MoE、
adapter paging、batch locality 或多租户 serving。Softmax mixture 在 top-1、规模较小或需要平滑端到端优化时仍合理；离散选择
只有在额外训练方差与推理状态成本小于有效容量收益时才成立。

### Dispatch 与 Aggregation 是两种不同责任

前一分支通过固定贡献系数约束有效支持度；另一方向是保留已选 expert IDs，却为其输出另学组合权重。两者都分开选择与贡献，但并不采用相同的训练目标或容量约束。

Top-k router 同时决定“哪些 expert 计算”和“这些结果以多大权重提交”时，选择与信任被耦合。固定 expert IDs 和计算量后，单独学习 aggregation 仍可能改变结果，说明 dispatch 负责容量与通信，aggregation 才负责对候选 expert 输出的 commitment。

拆分增加一个 head 和校准状态，也可能在小模型上得不偿失；传统 router 在路由稳定、实现简单优先时仍合理。该结论来自有限模型，不应外推成所有 MoE 必须解耦，但系统监控和负载均衡不能把 aggregation weight 误当 dispatch identity。

<!-- source-family: arxiv:2608.08853v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: expert-dispatch-vs-aggregation-ownership -->

### 从参数化 Router 到带检索记忆的 Router

训练得到的 parametric router 是最稳妥的起点：它没有外部索引，前向路径短，模型版本一旦冻结，
路由语义也随之冻结。在训练分布稳定、在线延迟严格或缺少可信参考样本时，这种设计仍然最合理。
它的边界是，遇到 distribution shift 时只能依靠参数中已经学到的决策面，不能直接复用“相似 token
曾经怎样路由更好”的局部经验。

一种受限的演进路径，是把 expert assignment 拆成参数化先验与检索修正。[kNN-MoE 的 exact-v1](https://arxiv.org/html/2601.02144v1)离线在有标签 reference 序列上优化 token-specific routing logits，但保存的 value 是经过 Top-K softmax 的稀疏 assignment，而不是 logits；hidden representation 作为 per-layer key。在线以近邻相似度加权这些 assignment，再与原 router 的 assignment 线性混合，直接用于 expert 输出加权。有限梯度步所得值不是全局最优，平均相似度也不是 assignment 正确的校准概率；原 router 仍是检索低可信、索引失效或查询失败时的 fallback。

```text
hidden state
-> parametric Top-K assignment
+ neighbor assignments from versioned per-layer memory
-> similarity-weighted assignment mixture
-> potentially larger support union and weighted expert outputs
```

混合 assignment 的非零支持集可能是原路由与多个近邻支持集的并集，不能继续假定每个 token 固定只执行 `k` 个 expert；若另行 re-Top-K，应将其视为需要独立验收的截断规则。先混合 logits、再 Top-K 也是可设计的另一实现，不是上述原文的在线机制。这项变化把 router 扩展成需要治理的运行时状态：收益是将逐 token 优化移出 critical path，代价包括 reference 标签和索引构建、检索延迟、额外显存以及支持集扩张后的 dispatch 成本。reference provenance、freshness、tenant isolation、delete/supersession 和 rollback 必须随模型版本保存；错误标签、reference drift 或 OOD query 仍可能注入错误路由。受限实验依赖可访问且与 test 相近的 reference set，不证明开放域或 expert-parallel 生产系统普遍更优。<!-- source-family:SF-2026-ARXIV-2601-02144 -->

因此这里的技术演进不是 `learned router -> retrieval router` 的替代关系，而是：

```text
frozen parametric router
-> optional retrieval correction with confidence
-> versioned memory and observable fallback
```

当检索修正真正进入生产时，模型层还必须把 memory revision 和 routing decision 交给第56章的调度与
观测契约；expert placement、All-to-All 和 fault recovery 仍不能由相似度检索单独解决。

### 外部记忆也可以承载容量，而不只修正路由

前一分支的检索结果只修正 expert 选择；如果读取对象本身是冻结表征，改变的就是容量载体而不只是 routing logits。这两种外部状态因此需要分开讨论。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20948:start -->
条件计算不一定要求在线激活可训练 expert。一条替代分支把另一个冻结模型的 hidden states 预先组织成
conditional n-gram memory，再由当前 token state 路由读取；它把一部分容量从参数与在线 expert compute 转成
离线 memory artifact 与检索。收益是复用冻结表征，代价是 memory 规模、构建版本、路由 miss、分布漂移和
读取带宽；它也不具备 MoE expert 的在线可训练性。memory freshness、覆盖或延迟不达标时，应回退本模型 dense
MLP / 常规 MoE，并把 grafting model、tokenizer、corpus 和索引版本纳入同一身份。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20948:end -->

### Execution Phase 可以成为 Router State，但不能成为隐藏标签

token-level router 在每个位置独立选择 expert，适合语义局部且执行阶段不可观测的生成；跨多个环境步骤的 Agent 则可能需要让历史状态参与选择。[一条受限行为路由分支](https://arxiv.org/html/2602.17038v1)将观测、目标的 pooled 表示与近五步历史 LSTM 交给 router，每步硬选一个 LoRA expert，并以相邻 routing probabilities 的相似性代理惩罚切换。这里的 phase 是事后定义的连续同 expert 区间，不是 workflow/runtime 提供的 planning、tool-use 等显式标签；可命名的行为模式也不证明 expert 拥有真实语义能力。原式只有单个 pooled K/V，普通 cross-attention 的单项 softmax 不会建立多位置的目标选择；正温度也不改变 hard argmax 的选择，主要改变软概率与梯度代理。因此不能把名称中的 phase-aware、cross-attention 或退火直接当作因果解释，训练出来的分段更不能改写 runtime 的真实执行状态。

这条路线用历史编码、多个 adapter、straight-through 路由及 occupancy/切换正则换跨步的选择约束，却增加代理梯度偏差、切换滞后、router collapse 与专家闲置；过强一致性会阻止真正需要的变化。作者 ALFWorld/WebShop 的有限对照支持局部配置，四 expert 不证明普遍最优，增至六个反而退步；额外 adapter 容量与完整训练费用也未被独立隔离。45 次 intra-action token 变化与平均 8.4 次相邻环境步切换不共享统计单位，不能直接相减证明阶段稳定性。验收须同时保存 phase 定义、时间尺度、expert utilization、task return 与完整成本；没有可信历史状态、任务无需跨步保持或质量—费用不改善时，单 adapter、原 token-level router 或 trajectory-level 固定选择仍合理，而不是由可解释的命名取代实际测量。

<!-- SF-2026-ARXIV-2602-17038 -->

## 把固定 Capacity 扩展为有边界的计算预算

固定 top-k 与 capacity factor 为基础闭环提供可预测形状。只有当不同 token、层或执行步骤的计算价值不同，才需要重新分配预算；平均 active count、瞬时 capacity 和任务质量仍是三份不能互相替代的验收条件。

### 去噪步骤改变时，Expert Capacity 也可能需要改变

上述 token-choice 路由让每个 token 自选 experts，适合因果解码：未来 token 尚不可见，系统只能在已出现的状态上分配计算。Masked diffusion 则在每轮同时处理整段序列，允许反过来由每个 expert 在当前 batch 中选择固定数量的 token。Expert-choice 可把每个 expert 的负载变成显式容量，减少不均衡；但**负载固定不等于每个 token 都命中 routed expert**。低容量步骤可能留下未被 routed expert 选中的 token，需要 shared expert 或其他兜底路径，并把覆盖率与质量一起验收。

更深一层，去噪各轮的 mask ratio 不同，固定容量虽易规划，却假设每轮额外计算的边际收益相同。若低 mask-ratio 阶段已有较丰富上下文，增加该阶段 expert 容量可能比早期高遮蔽阶段更有用；可在平均 FLOPs 预算相同的前提下按步骤重分配容量，再共同测训练损失、输出质量、逐步覆盖率与实际吞吐。这是一条 workload-specific 的计算策略，不是“越晚越多”普适定律：低容量阶段的 token 覆盖和退化风险、schedule 调参与 dispatch 形状变化都可能抵消收益。原 token-choice 在严格因果流式解码、缺乏全序列视图或需要简单逐 token 语义时仍合理。现有 exact-v1 证据只比较作者的 masked-diffusion MoE、OpenWebText/Nemotron-CC 与披露的 Megatron 配置；附录实际观察到 routed expert 未选中部分 token，不能沿用正文中绝对化的“零 token dropped”说法。[原始研究](https://arxiv.org/html/2604.01622v1)支持上述受限分支。<!-- source-family:SF-2026-ARXIV-2604-01622 -->

### 从固定 Top-k 到受总预算约束的 Variable-k

固定 top-k 给每个 token 相同 expert 数，shape、capacity planning 和 All-to-All buffer 都容易预测；当 token 难度与 expert 分歧差异很大时，它也会在低分歧位置浪费计算，在高分歧位置过早提交。一个条件分支先按 router probability 从高到低累积质量，达到 nucleus threshold 后形成初始 expert set；若已选 experts 的输出分歧仍高，再扩展集合。最后由 budget thermostat 调整阈值，使整个 workload 的平均 active experts 不超过发布预算。

```text
router distribution
→ cumulative-mass proposal
→ disagreement-based expansion
→ workload-level budget thermostat
→ selected experts and weighted aggregation
```

Router 拥有逐 token 的候选与分歧信号，budget controller 拥有跨请求平均计算约束，capacity/placement owner 仍决定这些选择能否执行；不能把预算压力偷偷写进 expert 语义。该分支把 compute 从“每个 token 固定”变为“难点多用、易点少用”，但没有增加总模型容量，也不能把 router mass 当作通用 epistemic uncertainty。动态集合会放大 load variance、dispatch fragmentation、buffer 预留和 OOD calibration drift，平均预算满足也不等于尾部 SLO 满足。

只有在 matched-compute evaluation 同时覆盖质量、专家负载和尾延迟时，variable-k 才能作为发布分支；分布漂移、kernel 只支持固定 shape、capacity 溢出或置信信号未校准时，应回退已验证的 fixed top-k。现有结果只覆盖作者披露的两个 backbone 与任务，不能外推为普遍路由最优。

<!-- source-family:SF-2026-ARXIV-2607-26052 -->

选择动态门槛前，还需要一个更便宜的反证：先在同一模型和任务上测 uniform reduced-k 的质量—计算曲线，再判断逐 token 动态分配 是否真有额外价值。保留 shared experts、对 routed weights 重归一化的静态分支，可能已减少大量调用；动态规则可依据相对权重、累积概率质量、expert 相似性或校准的 layer/token 特征调整调用数，并在不同预算区间分别验收。单步 QA 与完整自回归生成必须分开，前者可接受的局部裁剪不保证后者累积误差可接受，平均 active experts 也不等实际 dispatch 延迟。

[细粒度 MoE 受限对照](https://arxiv.org/html/2609.25809v1)的动态比较允许约 10% compute overspend，并从四种动态规则 中取较好结果；固定-k 重复结果选择较低值也会偏利动态，不能当严格等预算或稳健的精确优势。静态 speedup 测量不属于动态算法，硬件细节不足时更不外推生产 SLO。额外门槛搜索、生成回归与不规则 buffer 成本须进入验收；未显示稳定额外收益或预算严格时，原 fixed top-k/已验收 reduced-k 更简单，只有可比完整生成质量和执行成本均支持时才启用动态分支。<!-- source-family:SF-2026-ARXIV-2609-25809 -->

### 层级计划分配额度，Token Admission 决定额度给谁

层间分配还可以与逐 token 分配分开。固定 top-k 易规划，却假设每层少调用一个 expert 的质量代价相同；一个有界分支先在冻结模型和校准集上逐层试不同预算，记录相对 perplexity 变化，再以动态规划选择满足总预算的层级配置。这里优化的是可加的校准 surrogate，不是已经证明的端到端任务最优，更不是重新解释 expert 的语义。运行时再以该层预算给每个 token 保留最低调用数，并在原 router 候选内对剩余 token–expert 对统一排序分配：层级计划决定平均额度，逐 token admission 决定额度实际给谁，capacity/placement 仍负责执行。

这一分支增加校准、全层候选比较和动态 dispatch 成本，perplexity 排序也可能在任务或流量变化时失效；最低调用数防止部分 token 被完全饿死，却不保证语义质量或尾部 SLO。作者在 DeepSeek-V2-Lite、Qwen1.5-MoE-A2.7B、OLMoE 和单 H100 的有限对照中观察到预算收紧时的质量收益，但组合分配并非每个模型都优于仅 token 分配。Expert load 的相关性只描述负载排序，不证明 specialization 保留或多机通信收益；论文尚未联合建模 placement 与通信，候选大小和预算公式的张力也不足以支持通用最优保证。发布时应分别验收校准集外质量、实际分配、负载和测得延迟；校准失配或执行形状不支持时，固定 top-k 与已有 thermostat 仍是合理旧路径。[原始研究](https://arxiv.org/html/2604.08133v1)支持这一受限的两级分配分支。<!-- source-family:SF-2026-ARXIV-2604-08133 -->

### 用反事实路径审计 Router，而不把分数当贡献

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07260:start -->
Top-k score 高只说明 router 偏好某条路径，不能证明该 expert 对最终序列有因果贡献。对准备进入发布决策的路由，可以在保持 active-expert budget 不变时采样或替换少量备选 routes，比较 realized-token probability、序列结果与负载变化，从而估计 counterfactual route utility。该审计只提出诊断和更新建议；原 router 仍给出默认选择，训练/发布 owner 才能提交参数或策略变更。

反事实路由增加额外 forward、方差与归因歧义，并可能因替换 expert 造成分布外状态；它也不能从 token probability 自动推出任务正确性。作者证据只支持所测 MoE、任务和采样合同，不证明一个通用的最优 router。只有 matched-compute 对照同时覆盖 end-to-end quality、load 与运行成本时才能采用；预算不足、替换不稳定或 evaluator 不可靠时，回退标准 top-k，并继续以 load、capacity overflow 和 held-out quality 做保守监控。<!-- source-family:SF-2026-ARXIV-2605-07260 -->
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07260:end -->

### 离线 Expert 贡献先验与当前 Router Signal 不同

逐层预算和运行时 counterfactual 审计分别回答“计算放在哪层”与“替换当前路线是否有益”；校准阶段还可以在已经激活的 expert 集合中虚拟移除一个 expert、对其余权重再归一化，观察 hard-token 预测损失变化，冻结为 offline contribution prior，再与当前 router signal 融合。层级 hard/easy loss ratio 可另调 expert 预算。校准语料、checkpoint、已激活集合、归一化与融合系数共同定义该 artifact；它不是在线穷举所有路线，也没有覆盖未选 experts，更不是当前问题的知识 oracle。

这个分支减少在线试探，却支付离线 forward、归一化归因歧义与先验漂移。`arXiv:2604.14246v1` 的 CoR 在单 H100 80GB、DeepSeek-V2-Lite/Qwen3-30B-A3B/GPT-OSS20B 上提供受限对照；DeepSeek Trivia 42.25→41.89、GSM 20.02→17.52 说明不能只据校准 loss 宣布任务全面改善。近似保持平均 active expert 数，也不等同 FLOPs、通信、latency 或 SLO 等预算。发布仍须分别核校准集外质量、实际负载和测得成本；校准失配、移除效应不稳或 dispatch 形状固定时，原 Top-k 与既有预算 controller 继续成立，不能让静态 prior 覆盖新的运行证据。

<!-- source-family:SF-2026-ARXIV-2604-14246 -->

### Post-training 后再增加可跳过路径，不等于删除旧 Experts

已经完成 post-training 的 static top-k MoE 若直接减少 top-k，会改变原 router 的概率质量和行为。一个更保守的
实验性分支是在保留原 experts 的同时注入 parameter-free、zero-output routes，再用 frozen original model 做
distillation，使 router 学会在可省略的 token 上把部分质量交给 zero path：

```text
post-trained static top-k MoE
→ inject zero-output candidate routes
→ SFT / on-policy distillation against frozen original behavior
→ balance normal-group versus zero-group usage
→ dynamic per-token compute with fallback to original experts
```

Zero route 不创造能力，只表达“此处某些 expert update 可省略”。Normal experts 之间不应被新的 balance objective
强行均匀化，否则会破坏原有 specialization。它获得按 token 调节 compute 的可能，却新增 teacher dependence、
route collapse、quality drift、kernel shape 和 rollback state。ZEDA 的作者结果仅支持其 checkpoint、单 H200
phase-throughput 与训练样本合同，不证明生产 latency/SLO 或“跳过一半 experts”可跨模型复用。原 static top-k
在低风险、分布漂移或 distillation evidence 不足时仍是正确旧方案。

## 专家化、模块化与更新边界

可变预算回答调用多少容量，并不回答某个 expert 拥有什么知识。要决定能否独立部署、微调或撤销专家，必须从联合训练形成的条件样本分布出发，再用行为与干预证据验证模块边界。

参数几何是便宜的诊断代理，却不能直接定义功能分离。设两个线性 expert 的映射为 $W_i,W_j$，向量化权重正交只给出 $\operatorname{tr}(W_i^T W_j)=0$，并不要求整个 $W_i^T W_j$ 为零；对固定输入 $x$，输出内积仍是 $x^T W_i^T W_j x$，可以非零。非线性、router 形成的条件输入分布和后续读出还会进一步改变行为。因此 weight-space penalty 可以表达一种参数偏好，但不能替代实际路由样本上的 activation、任务行为与干预验收。<!-- source-family:SF-2026-ARXIV-2601-00457 -->

一个受限 NanoGPT-MoE 实验中，baseline 的 weight overlap 已很低，co-activated expert 的输出 overlap 却仍高；对 up-projection 加入所测正交 penalty 后，参数 overlap 反而升高，任务收益随数据和 seed 改变。这不证明所有 MoE 正则化无效，也不能从相关性检验的高 p 值推出统计独立。新目标应分别检查它是否改变参数代理、真实路由输出和任务质量，并保留负载约束；行为证据不足时，原联合训练与 load balancing 仍是合理基线，而不是用更漂亮的几何指标宣布专家已成为独立模块。

### 统计偏好不是固定知识部门

Expert 可能对某些 token 类型、语言或模式表现出统计偏好，但 router/expert specialization 是训练结果，不保证每个 expert 对应一个可命名领域。

因此，诊断 expert 的“工作”不能只数它被 route 了多少次。被选中只是获得处理机会，输出可能接近零；可先用 `g_i(x) × ||E_i(x)||₂` 衡量写入 residual stream 的幅度，再从高贡献片段、promoted tokens 和 held-out 对照提出功能假设。受限 MoE 分析中，标签常对应括号闭合、形态或语义操作，而非完整的“代码领域”；k-sparse probe 则检查概念是否能由少量坐标读出。二者分别刻画可读性与候选功能，不能把大输出范数、route 频率或自然语言标签直接等同于因果必要性。<!-- source-family:SF-2026-ARXIV-2604-02178 -->

这条诊断路线用更细的功能解释换取样本、探针及解释器成本，也引入 best-layer 选择与自动标签偏差：同系列 LLM 解释和评分不是独立真值，局部 logit attribution 不替代删除/替换后完整行为验收。所测模型未覆盖最大的 MoE，expert 也未被证明完全 monosemantic；不能按这些标签直接裁成可部署的领域子网。Placement 与 capacity 仍以真实负载和质量为准；标签不稳定时回退路由统计与具体行为干预，而不是预先给专家划知识部门。

标准 MoE 也不是先把数据按“数学、代码、语言”拆开，再逐个训练独立 experts。通常 shared layers、router 与 experts 在同一个端到端 objective 下 joint optimization：一个 token 的主任务梯度只进入它实际选择的 expert paths，shared layers 接收跨 routes 的信号，router 同时受到主任务信号与 load-balancing/capacity 约束。于是每个 expert 看到的是 router 动态形成的条件样本分布，而不是人工声明且永久不变的领域 dataset。

稀疏更新会形成 specialization，却也可能造成 rich-get-richer、expert starvation 与共同表示漂移；这正是 load balancing 属于训练正确性而不只是设备利用率的原因。按领域预训练独立模块后再组合属于另一种 modular composition 路线，需要额外解决 router calibration、shared coordinate、冲突和联合 Evaluation，不能被当作 MoE 的默认训练方式。

把 expert 命名为“数学专家”或“代码专家”需要行为、路由和干预证据。负载均衡还会主动阻止所有相关 token 只集中到单一 expert。

MoE 的稳定定义是 conditional computation，不是人工预先划分知识部门。

### 组合兼容 Dense Experts 与同一 Checkpoint 破对称是不同起点

前面的标准联合训练与独立模块组合需要不同的初始化条件；以下先沿独立模块组合展开，再比较从同一 dense 模型拆分专家的分支。

这条组合路线也不只有“随机初始化 Router 后做联合微调”一种收尾。如果各 Dense Expert 来自兼容的架构、词表与初始化，且保留带领域标签的校准样本，可以平均非 MLP 参数、保留各自 MLP 为 Expert，再从合并模型的中间表示累积特征统计，以闭式 ridge regression 初始化逐层 Router。这样将 Router 校准从反向传播优化改为一次带标签的前向统计与线性求解，适用于无法集中进行多任务再训练、但能提供相容专家和校准数据的情形。它并非“训练免费”：独立专家训练、校准样本前向、统计矩阵与求解仍有成本；深层 Router 所用特征还来自按领域指定 Expert 的路径，而非最终 Router 的真实路径，形成分布偏差。若专家坐标不兼容、领域标签不足或输入跨域混合，联合训练或微调仍可能更稳健。作者在 115M/3B Llama 系列和披露任务上的结果只说明这条受限分支可行，不证明任意模型组合后都无需校准或保持原专家能力。<!-- source-family:SF-2026-ARXIV-2603-29765 -->

另一条初始化分支不是组合独立训练的领域模型，而是从同一 dense checkpoint 中打破 expert 对称性。简单复制 FFN 可以在初始化时保留原函数，却让各专家起点相同；若保有代表性 activation 校准样本，可以先按输入方向聚类，利用各簇的协方差对第一层线性映射作 whitening / truncated-SVD 近似，再按簇 centroid 初始化 router，并以 dense EMA teacher 的 expert ensemble 输出约束 Top-k 路径。这里输入分区形成不同初始化先验，不是已发现固定的知识领域；第一层矩阵的加权近似也不等于优化了完整非线性 FFN 的输出目标，不能宣称整块函数被精确保留。

它把初始化选择与校准分布、rank 和 teacher 目标绑定，增加聚类/矩阵分解、校准前向与后续蒸馏成本；破对称也可能先损伤 dense 基线。作者的 CLIP ViT、八 expert / Top-2 实验中，ensemble 蒸馏单独使用并非各指标都改善，组合消融不能证明低 router entropy 就代表正确语义或真实吞吐。输入远离校准域、近似造成退步或 teacher 成本不合算时，复制初始化后联合训练、普通 upcycling 或现有独立专家组合仍应保留；训练 owner 再验质量和负载，而不是由初始化几何替运行时作性能承诺。<!-- source-family:SF-2026-ARXIV-2604-13508 -->

### 从统计 Expert 偏好到可部署模块，需要改变 Objective

标准 token-level routing 优先优化 next-token loss 与负载均衡。它允许同一 document 的 tokens 分散到很多
experts，因此“某些 expert 对某领域有偏好”并不意味着系统能只加载一个较小、语义完整的 expert 子集。
若部署目标真的需要 domain-selectable modules，训练目标就必须显式增加更长作用域的约束，例如让同一
document 先选择共享 expert pool，再让各 token 在 pool 内 routing：

```text
document identity
→ shared candidate expert pool
→ token-level top-k inside the pool
→ global load-balance signal
→ domain validation selects a versioned deployment subset
```

这样得到的 modularity 是 objective、data boundary 与 deployment selector 共同塑造的结果，不是对 router
可视化后的命名。它可以减少已知窄域的 resident experts，却新增 selector dataset bias、subset staleness、
global-balance collective、未知 domain fallback 和逐层 expert-list versioning。通用混合流量、domain 不稳定或
selector evidence 不足时，完整 standard MoE 仍是更稳妥的旧方案。EMO 的作者实验只在其 architecture-matched
checkpoint、corpus、task 与 validation contract 下支持“小 expert subset 可以保留更多任务表现”，不证明
experts 已成为 faithful capability modules，也不证明 latency 会随参数子集同比下降。

### Routing Overlap 也限定 Post-training 的参数更新域

可部署子集与可安全更新子集不是同一个问题。即使没有改变原 objective，也可以先按目标语言、层级和任务记录 expert 的经验激活频次，再依据语言specificity ratio、共享频次的变异系数与绝对频次选择更新域：浅深层较独有的 routes 与中层共享 routes，应承担不同的更新预算，再冻结未选 experts 与 router。此时 selector 只提出待更新域；“偏向某语言”并不赋予 expert 独占该语言能力的语义身份。<!-- source-family:SF-2026-ARXIV-2604-03592 -->

只有 router 固定、非目标语言实际走到的支持集与更新域不相交等条件成立时，才可推导对应路径未被改写；现实 overlap 和输入漂移会破坏这个前提。减少待更新参数可以节省 gradient/optimizer state，却不消除全模型常驻和 activation 成本，也增加 profile 偏差与他语回归测试。作者 multilingual MoE 的个别目标语言劣于 Top-K，剪除其余 experts 更会损伤其他语言；overlap 不稳、共享能力重要或新域未被校准时，应扩大更新域、回退普通 SFT/adapter，而不是把低 routing 频次视作无影响证明。

### 长尾 Expert 低频不等于无知识

MoE SFT 中用全局 load-balancing loss 或 dense mixing 阻止 router collapse，容易实现并能保持所有 expert 获得梯度；但额外梯度也可能干扰任务相关 routing。反过来，按激活频率直接剪除低频 expert，会把“少被调用”误当成“没有贡献”。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-23036:start -->
一个实验性分支以 bias-driven routing 让任务相关 expert 保持活跃、让部分长尾 expert 稀疏化，同时增加 always-active gated condenser path，为否则可能 gradient-starved 的信息提供持续可训练通道。Router bias、sparse experts 与 condenser 分别拥有 route proposal、条件容量和共享巩固路径；它避免强制所有 expert 均匀，却新增 condenser bottleneck、route bias drift 与额外常驻计算。完整 load balancing 在 workload 多样、expert utilization 是主要瓶颈时仍合理；没有证据证明长尾信息可迁移或 condenser 稳定时，应保留原 experts 并回退现有 SFT。作者实验限于 GPT-OSS/DeepSeek MoE、选定数据与 8×H100，不给出通用 router optimum。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-23036:end -->

### 知识 Expert 必须与 Backbone State 分开版本化

RAG 把知识留在外部、易于更新和引用；普通 fine-tuning 把知识写入共享参数、运行路径短，却会让更新、撤销和冲突处理牵动整个模型。中间分支可以把领域知识编译成独立 expert，只在末端 FFN 与 backbone 输出组合，使 backbone KV state 保持可复用。Knowledge registry 持有 expert 版本与撤销，router 只提出选择，末端组合才形成派生输出。

这种解耦降低高频知识更新对 backbone 的干扰，却限制了知识参与深层推理的机会，并增加 expert/router 生命周期与冲突仲裁。需要可引用出处、细粒度权限或频繁更正时，RAG 仍是主路径；需要广泛重塑表征时，专门 fine-tuning 更合适。小模型和有限 corpus 上的实验不能证明末层注入普遍优于这些旧方案。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.14243 -->

## 执行约束：把已选路径变成可部署的工作集

到这里，模型已定义谁可被调用、如何训练和如何组合；runtime 还要回答这些路径能否在当前设备、显存与拓扑下执行。以下按执行形状、通信图、权重驻留和批次复用展开。保持已选路径的优化与改变模型函数的分支必须分别验收，不能把局部负载代理当作端到端收益。

### 极稀疏路由也要产生可执行形状

当 `E` 很大而 `k` 仍很小时，平衡问题还会从平均 loss 扩展到 executable shape。
若每个 expert 的 token count 在 critical path 上持续变化，runtime 可能需要动态
allocation、host synchronization 或大量 padding；这些成本会抵消稀疏计算收益。
因此有些模型会在训练时把 router balancing 与静态 dispatch shape 联合设计。

Kimi K3 报告中的极稀疏 MoE 是这一原则的版本化案例：作者把 quantile-based balancing、
固定 expert-parallel shape 与无 host synchronization 的关键路径放在同一设计中。
该案例不能外推为通用最优 router，也不能用厂商 benchmark 证明其他实现失败；它提供的
长期认识是，**routing objective 不只塑造模型质量，也塑造 communication shape、kernel
batch 与可预测性。**这是模型机制与训练 runtime 的 `Layering / Dependency`，不是
用系统技巧替代 load-balancing objective。

### 保持依赖的 Kernel 融合与改变依赖的架构分支

训练路径还会把 activation、transpose、quantization 与 backward derivative 暴露在每个 expert GEMM 周围。
逐算子实现最易调试和移植，却会让中间 BF16 tensor 反复往返 HBM，并让动态 token count 触发 host
synchronization。一个更深的 execution branch 把 activation/scale/clamp、quantize/transpose 或 dActivation
放进 grouped GEMM epilogue，并用 device-side dynamic scheduling 避免 host 读取每个 `M_e`；同时故意限制
kernel occupancy，为 Expert Parallel collective 留出 SM headroom：

```text
router-owned token/expert assignment
→ grouped dynamic expert shapes
→ fused epilogue and graphable device schedule
→ explicit SM margin for communication overlap
```

Fusion 获得较少 HBM traffic 与 graph capture 机会，却绑定 weight layout、dtype/support matrix、compile cache、
expert-shape heuristic 和 correctness matrix。占满 SM 也未必最佳，headroom 又可能在通信很少时浪费算力。
NVIDIA 2026 的 SM100 fused-kernel 材料只支持这一机制边界，不证明其厂商端到端百分比由单一 fusion 导致。
Unfused/composable path 在非目标硬件、稀有 shape、数值诊断或 portability 优先时仍合理。

另一条分支不是在同一函数内重排执行，而是主动改变模型依赖：让 dispatch 使用前层完整 state、后续 attention 先消费尚未包含部分 expert 输出的 activation，再把迟到项接回 residual。最终补齐所有加项不等于恢复原来的非线性函数，因此这种重叠必须作为新架构训练，分别验收质量与系统收益，不能直接对原 checkpoint 宣称免费等价重排；无法承担重训与质量复验时，仍应选择上述保持原依赖的执行优化。

### 改写通信图需要显式模型身份

标准 Expert Parallelism 让全局 router 把 token 发往任意 expert，表达自由但会形成跨全部设备的 all-to-all。若模型结构
允许把 expert 与 KV heads 重组为若干相对独立的 group，通信图可以改写为组内 all-to-all，再用组间 all-reduce 合并
必要的共享结果。这里的收益来自**重新参数化模型**，不是 runtime 在不改变语义的情况下少发消息；group membership、
head/expert layout 与 checkpoint 都成为模型身份。

局部化 dispatch 可降低全局交换压力，却新增组间 reduction、容量碎片和训练/迁移成本；单设备没有通信收益，错误分组
还会限制 token 能访问的容量。现有 exact-v1 只支持作者拓扑和模型下的通信与质量结果，不证明它可直接替换任意既有
MoE checkpoint。已有模型不可重训、规模较小或全局带宽充足时，标准全局 all-to-all 仍成立；第 49 章只接手冻结通信图
的 kernel/collective lowering。<!-- source-family:SF-2026-ARXIV-2605-06206 -->

### Topology-conditioned Multicast 是 Dispatch 的替代分支

在 direct-connect fabric 上，MoE dispatch 不一定要让 source 分别向每个 selected expert 发送完整 activation。若 selected experts 可作为受控 relay，可以建立 source-rooted multicast tree，并在反向 combine tree 上做 partial reduction；这样用多跳与 relay state 换取 source-link congestion。

Router 仍只拥有 token→expert 语义，tree/weight catalog 属于 topology-aware runtime。该分支新增 relay ordering、fault recovery、deadlock 与 topology epoch；强交换网络、小 fanout、故障频繁或 ordering 难验证时，普通 unicast/All-to-All 仍更合理。训练侧 transport/runtime 细节回到第 36 章。

### Router 选择 Expert，Placement 决定这次选择能否低成本执行

标准 Expert Parallel 先固定每个 expert 的设备位置，再让 router 产生 token assignments。它简单、稳定，
但热点 expert 或跨慢链路 dispatch 会把模型层的 balance objective 变成 runtime straggler。只复制热门
experts 可以缓解排队，却会产生 replica capacity、参数同步、optimizer migration 与 placement 决策。

一种更明确的分层是：router 继续拥有 token→expert choice，placement controller 根据 expert demand、
device capacity 与 topology cost 决定 replica→device mapping，并用 repair step 把连续优化结果变成离散可执行布局：

```text
router-owned token / expert demand
→ capacity and topology-aware replica plan
→ discrete placement repair
→ executable dispatch
→ observed load feeds the next placement epoch
```

这不是用 placement 修复错误 router。Replica plan 必须绑定 checkpoint、expert revision、parallel group、
fabric topology 与生效 epoch；迁移期间还要处理 optimizer/checkpoint 一致性、双写或 quiescence。TAOT 的
4×8 A800、Qwen3-30B-A3B 实验只支持 topology-aware replica placement 在该 contract 下可行，未覆盖故障恢复、
多租户或 optimizer migration。固定 placement 在 workload 稳定、迁移昂贵或规模较小时仍是正确旧分支。

训练分布上的均衡和常见流量的 demand trace，还不能保证用户可选择的输入都均衡。重复片段可让许多 token 选择少数 experts；这些 experts 若落在同一设备，才会把 expert 集中转成 device straggler，同样的 top-k 分散到不同设备则可能仍平衡。因此 worst-case 输入检查应同时冻结 router、top-k、expert-to-device mapping 与 placement epoch，分开记录 expert concentration、device load 和实际执行延迟；不能用一个静态负载上界代替端到端测量。<!-- source-family:SF-2026-ARXIV-2512-23995 -->

这增加输入分布扫描与 placement 重验成本，也不能穷尽恶意输入。受测 router 模拟、本地 MoE kernel 和远程 API 的 TTFT 是三种不同证据：远程延迟还受网络、缓存及 provider 路径影响，不足识别隐藏模型是否为 MoE 或采用多少 EP 设备。更分散的 placement、在线负载重平衡或异常输入筛查都需另验质量、误拒与响应窗口，不从模拟覆盖率签发防御保证；低风险稳定流量仍可采用原均衡与固定布局，出现分布漂移再重开受影响 epoch。

Placement 还可分开跨层 transition affinity 与每层近期 activation load：先将筛选后的少量 affinity-linked experts 固定到人工指定 anchor GPU，再把其他 experts 按新负载 greedy 分布，并按 epoch 刷新。它优先降低跨层搬运，却可能增加 anchor 局部 imbalance；容量不足时必须收紧 threshold/top-E、裁 affinity pool，不是所有关联都可同时驻留，也不是昂贵 MILP 已获在线最优。随机输入 profile 不认证真实流量依赖，计数可陈旧，迁移、参数 identity 与生效 epoch 仍由 runtime controller 负责。有限实现的 baseline 与实现版本不同，主性能关闭 prefix cache，不能与另一人口的缓存 hit 提升合并为质量/SLO 保证。Profile、调参与搬迁付费，稳定负载或容量冲突时保留固定 placement、普通 EPLB 与原 dispatch。<!-- source-family:SF-2026-ARXIV-2602-21626 -->

### 固定显存下，副本数量与精度预算必须联合选择

固定显存预算还会限制“复制热点 expert”这条路径：若所有原件保持同一精度，新增副本可能根本放不下。一个受限的
replicate-and-quantize 分支先在 calibration set 上分开 load 与 importance，再复制 heavy-hitter experts，并量化副本
及低重要度原件以守住原 memory envelope。这里 frequency 只决定容量压力，不能独自代表语义重要度：

```text
router trace + per-expert load
+ quality sensitivity under a frozen calibration identity
→ choose replicas and precision per expert
→ validate memory, load and quality together
→ publish one placement / precision epoch
```

Router 不变，placement owner 持有 replica mapping，quantization artifact 持有每个 expert 的 format/scale，runtime 按同一
epoch dispatch。它用 calibration、量化误差和更复杂的 artifact 组合换并行容量；traffic/importance drift、错误 scale、
副本版本不一致或热点迁移都可能同时破坏质量与平衡。显存充足、热点不稳定、质量回归不可接受时，应只重排、不量化
或回退单副本。exact-v1 的作者结果只支持所测 sparse MoE 与 calibration contract，不证明 ±0.6% 一类结果跨模型成立。

<!-- source-family:SF-2026-ARXIV-2602-19938 -->

若压缩对象不是副本的位宽，而是 expert 权重的低秩表示，预算还要决定每组保留多少 rank。一条受限分支把 experts 按校准 routing frequency 分组，共享低秩 basis，再用归一化频率与奇异值谱的 effective rank 共同提出组内 rank 分配：频率反映这组被读取的机会，谱反映其权重的可压缩结构，二者都不是质量重要度真值。较小组保留最低 rank，稀疏 one-hot 投影则把未被低秩近似解释的残差映入较小 latent 空间，再以可训练残差修正权重。这与前面的 replica/precision 选择共存，改变的是参数表示，而不改变 router 的 token 选择语义。

分组、校准人口、rank 与残差预算须一同绑定 artifact；残差本身占用参数预算，最低 rank 的取整规则也不能直接证明总预算精确守恒。投影列归一后在 latent 空间满足正交条件，不代表任意全维残差或任务语义无损。[受限原始证据](https://arxiv.org/html/2602.09316v1)只压 expert up/gate，校准集、压缩率及权重融合系数会改变质量，部分任务与更激进工作点仍退步；未给端到端部署吞吐。因此 rank/frequency 是 compression proposal，仍需与统一 rank、单信号分配及原权重在同一任务切片比较；预算宽裕、组内结构不共享或长尾回归时，保留独立权重、统一 rank 或原精度路径。<!-- source-family:SF-2026-ARXIV-2602-09316 -->

### 低频 Expert 的精度需求不能由热度替代

精度预算与调用频率之间甚至可能呈相反关系：在一个具预训练路由对齐假设的二元 MoE 模型中，低频相关特征对应的 expert activation 更弱，量化噪声更容易吃掉分类 margin，因此可能需要更多 bits，而非因为“冷”就被压得更低。一条实验性分支以训练前后 router row 的范数差排序，并用 expert 内神经元权重的最大方差修正；它把较小范数变化或异常高方差作为高精度候选，但这些量只是 precision proposal，不是语义重要度真值，更不是一般 MoE 中“低频必需高精度”的定律。

这个分支还把初始化身份带进了量化合同。只有收敛 checkpoint、没有初始 router 时，直接用 final norm 代替 norm change 的经验支持来自重新初始化并微调的 Switch 实验；未知初始化、不同优化历史或分布迁移下不能默认排序等价。量化 artifact 应保存所用 router revision、初始化可得性、方差统计及位宽规则，并在冻结的任务切片上与统一位宽、frequency-based 和误差校准方案比较，而不把一个廉价 proxy 的通过当作所有专家都保持功能。

[受限原始证据](https://arxiv.org/html/2604.06515v1)的 Switch/Mixtral 结果也不是无损或全面胜出：低平均位宽存在其他校准方案更好的工作点，不同任务排名不一致；尤其更激进的压缩会改变质量边界。收益是减少昂贵逐 expert 校准的候选搜索，代价是初始化假设、proxy 失配及长尾能力回归。初始化无法核实、质量切片不稳或预算充足时，保留统一精度或更直接的误差校准仍合理。这里拥有的是 expert precision 分配机制，具体 scale、kernel 和运行效率仍由量化 artifact 与推理执行章节验收。<!-- source-family:SF-2026-ARXIV-2604-06515 -->

### 副本预算还要为 KV Cache 留出可用并发

即使不改变精度，副本预算也不该平均分给每层：不同层的热点倾斜和新增一个副本带来的负载改善可能相差很大。
在固定显存下，可以先用代表性路由轨迹估计各层的边际收益，再选择副本数与设备位置；否则给低收益层增加副本，
可能只挤掉 KV Cache，却没有解除真正的 straggler。规划时还须限制每台设备的 expert 容量差：同一 Data Parallel
rank 的可用并发会受 KV 空间最小的设备约束，不能用全组平均剩余显存推算容量。这把前面的 placement 决策与
推理系统的 sequence capacity 接在一起，而不是另起一个只优化专家均衡度的目标。

这种离线估计用更高的画像、重规划和迁移成本换显存与负载的联合效率；流量分布漂移、设备容量不齐或副本版本
不一致时必须重新验收或回退。负载稳定、显存宽裕、平均分配已满足并发目标时，简单副本方案仍然成立。
现有证据只支持作者在 BF16 DeepSeek-R1/Kimi-K2、A100 集群与所测输入输出长度、数据集及 SGLang 配置下的
比较，不证明任何 MoE 部署都能得到相同的 goodput。<!-- source-family:SF-2026-ARXIV-2603-28768 -->

### Batch-aware Expert Sharing 只能改执行集合，不能改 Router 语义

逐 token Top-K 在请求独立、batch 小时最直接；continuous batching 和 speculative candidates 会扩大同一轮被激活的
expert union，使每个 expert 只得到很小工作量，weight traffic 与 expert-parallel 峰值重新成为瓶颈。一个中间分支是
保留每个 token 的 gating scores，却在 batch boundary 上选择可共享的有限 expert set：optimizer 以总 gating mass 为
proposal objective，hierarchical selector 先处理请求/候选相关性，runtime 只让通过 admission 的 token 使用共享集合。

共享集合不是新的模型真值。Router 仍拥有 token→expert scores，sharing policy 只能在显式质量预算内压缩本 batch 的
可执行 expert union，并把被裁剪 mass、batch composition、speculative-tree identity 与 fallback 写入回执。收益是更大
expert batch、更低 peak load 和更少 weight activation；代价是 token-specific specialization 损失、不同请求相互影响、
batch churn、selector cost 与 fairness。高风险请求、低相关 batch、质量预算不足或 expert 全驻留时，应回退原始 Top-K。
作者结果只覆盖其模型、batch、expert-parallel 与 speculative 设置，不能成为通用吞吐或质量承诺。

<!-- source-family:SF-2026-ARXIV-2602-07265 -->

### Prefill 与 Decode 可以使用不同 Expert Set，但必须共享误差合同

prefill 的 token 之间差异大，适合按 token 保留专家；decode 的小 batch 则可能让路由碎片化，使 batch-level expert pool 更利于复用。两种 phase-specific 策略不能只比较命中率，而要在相同输出近似误差、capacity、drop policy 和 batch 条件下验收，并把 retained set 写入执行身份。这样可以降低部署成本，但也增加跨阶段状态切换与回退复杂度。
<!-- source-family: arxiv:2608.24938v1; semantic-body-binding: phase-specific-expert-retention-contract -->

### Router 连续性必须与 Expert Residency 共同设计

标准 MoE objective 只要求每个 token 选出合适 Expert；当 Expert 跨设备、权重不能全部常驻时，相邻 token 在 Expert 集合间频繁跳转会把稀疏计算收益重新付给权重搬运与 All-to-All。一个可部署的分支是在质量与负载均衡约束之外，对路由的时间连续性施加受限偏好；runtime 再依据真实访问压力、容量与 3.5D 拓扑决定 hot Expert 的 residency，而不是让 Router 直接拥有 placement 权。

这条路径以更小的 weight churn 和通信换取路由自由度、热点持续时间估计与错误预取风险。连续性过强会压低专家多样性，历史热度在 workload 漂移后也会把旧热点固化；模型小、Expert 可全驻留或网络不是瓶颈时，原始逐 token 路由仍更合理。相关 exact-v1 实验只支持作者模型、拓扑和访问分布，不形成通用 locality 系数。

仅靠 runtime 预测下一次 Top-k，仍要接受模型每个 token 改选的事实；若换入成本是主约束，可以让模型在一段 token 内先保留较大的可用 Expert 集合，再由原 Router 在集合内选择本 token 实际计算的少数分支。另一个控制头决定何时终止当前集合并选新集合，训练目标为这种切换加入代价。这样，Router 仍拥有 token 级激活，控制头拥有跨 token 的候选集合，runtime 才拥有权重驻留与真实搬运；三者不能混成一个“更稳定的路由”指标。<!-- source-family:SF-2026-ARXIV-2604-20156 -->

时间驻留减少可观察的集合切换，却以选择自由度、额外控制头和训练耦合换取潜在加载收益。集合过窄或切换惩罚过强会损害质量；各层独立切换也未必能合成一次高效换入。一个受限后训练实验在单一 MoE 模型上同时看到较低切换率和任务正确率退步，但没有实现专家卸载或测量真实传输、端到端延迟。因而只有把控制头、Expert 容量、具体硬件加载时间和质量预算共同校准，才能判断它是否比逐 token Top-k 加 runtime 预取更合算；全驻留和稳定小模型继续保留原路径。

<!-- source-family:SF-2026-ARXIV-2607-08780 -->
<!-- source-family:SF-2026-ARXIV-2607-11586 -->

## 本章在知识树中的位置

```text
Transformer Layer
-> Attention branch unchanged
-> Dense MLP [B,T,d_model]
   replaced by router probabilities [B,T,E]
   -> top-k expert paths
   -> Expert Parallel / All-to-All
   -> combined output [B,T,d_model]
-> residual stream shape unchanged
```

本章沿参数容量轴扩展第 16 章的 MLP；第 22 章则沿序列容量轴重新汇总 Position、Attention 与 KV Cache。两者都改变主干的可扩展边界，但不是前后依赖的两个算子。第 36、40 章接住 Expert Parallel、All-to-All 与 checkpoint mapping，第 44 章接住 MoE Decode 的小 expert batches 和通信，第 49～52 章再由 runtime 执行与扩展这些机制。本章保持模型语义为主。

## 从机制演进到系统设计

MoE 最初只把 Dense MLP 的全部激活改成 top-k 条件激活；在 expert 数量和并行规模继续增长后，真正的新约束不再只是平均负载，而是 router state 是否稳定、specialization 是否形成，以及 token flow 能否被当前 topology 高效执行。相同 token id 也不意味着相同内部路径，因此 routing pattern 可以作为诊断信号，却不能直接拥有正确性结论。

这条演进把 router 从一个局部分类器变成模型与 runtime 共享的受观测状态：训练侧同时检查 load、specialization 与 collapse dynamics，执行侧再决定 placement、dispatch 和 grouped GEMM。收益是扩大总容量并保留条件计算；代价是路由漂移、热点 expert、All-to-All 与诊断成本。Dense MLP 在规模较小或通信主导时仍是更稳健的分支，静态 load-balance 指标也仍是必要但不充分的 baseline。

## 自检问题

1. MoE 中“稀疏”指 weights 还是 active paths？
2. Router 为什么输出 `[B,T,E]`？
3. Top-2 小例子如何重新归一化路由权重？
4. Total parameters 与 active parameters 为什么可以分离？
5. Load-balancing loss 在约束什么？
6. Capacity factor 用什么代价缓解负载不均？
7. Expert Parallel 为什么产生两次 All-to-All？
8. Active FLOPs 下降为什么不保证推理 latency 同比例下降？
9. MoE expert 为什么不能直接命名为固定人类领域？
10. MoE 与 Dense MLP、Tensor Parallel 的边界分别是什么？
11. Grouped GEMM 减少了什么执行开销，又没有消除哪些路由不均衡成本？
12. 为什么标准 MoE 是 router、shared layers 与 experts 的 joint optimization，而不是按人类领域逐 expert 独立训练？

## 小结

MoE 把 Dense MLP 改造成条件计算：Router 为每个 token 选择少数 experts，使总容量可随 expert 数增加，而单 token expert compute 主要随 top-k 增长。

代价是路由成为模型与系统共同状态。负载均衡、capacity、token dispatch、All-to-All、expert placement 和小 GEMM 效率决定稀疏参数能否转化为真实收益。

参数容量的扩展到此回到同一个判断：被选中的容量是否在质量与执行约束内真正有用。第 22 章转向另一条正交轴——序列容量，把 Position、Attention 与 KV Cache 的约束放在一起，而不是在 MoE 后再增加一个算子。

## Review notes

- `SF-2026-ARXIV-2602-21626`：[v1 Algorithm 3 / §IV–V](https://arxiv.org/html/2602.21626v1)。fixed-anchor affinity pool + remaining greedy load，不采 MILP 全局最优；vLLM 0.9.1/0.9.2 差异、主性能 prefix cache disabled 与独立 ShareGPT hit 人口保留。非原 packet 作者必要原证/owner PRE 后窄写；root已实际顺读正文、完整邻接与自身末注，POST通过，未复现。

- `SF-2026-ARXIV-2602-17004` — Daily `2026-02-21`；[Trinity exact-v1](https://arxiv.org/html/2602.17004v1) §2.3 Eq15–28、§3.3、§6；2+2+2=6，仅SMEBU幅度/软限幅/center/EMA反馈律的实际差额深入。六项联合/no-ablation与bias不进输出gate边界近正文，不采稳定因果、全部训练/推理速度或checkpoint已实现隔离。root必要原源/actual owner PRE通过并授窄锁；作者正文/完整邻接及末注已顺读，root非作者实际正文/完整邻接及自身末注POST通过，窄锁释放，未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-17798` — Daily `2026-02-24`；[GrMoE exact-v1](https://arxiv.org/html/2602.17798v1) §3.1–3.4/Algorithm1、Theorem2条件与§6.1。2+1+2=5，平方投影affinity的实际gap与独占温度/无collapse误读纠正深入；fixed-logit熵单调是通用softmax事实，uniformmixture/separation不自动成立，dense mixture不等稀疏执行。v1摘要2.7B与主要实验配置未充分对应，不补造版本归因；成本、负侧与linear共存近正文。root 必要原源/actual owner PRE通过并授单段+自身末注窄锁；作者正文/完整邻接已读，root 实际正文、完整邻接与自身末注非作者POST通过，窄锁释放。未核代码/复现，非日级Gate。

- `SF-2026-ARXIV-2602-12587` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12587v1) §2/Eqs12–17、§3/5及A.2。2+1+2=5，private head-slice routing/composition budget差额深入；Theorem2.2遗漏S内负项的中心反例隔离，不进入Books正面证据，probe非语义真值与TRACE反侧/执行费用近正文。root必要源/反例/actual owner PRE通过并授窄锁；作者已顺读实际单段/完整邻接，root实际正文/完整邻接/末注非作者POST通过，窄锁释放；未核实现或复现，不授日级Gate。

- `SF-2026-ARXIV-2602-12556` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12556v1) §3/common-unique投影、periodicSVD、Table1/3与必要配置。2+1+2=5，固定谱基的梯度分责深入；common tangent rank≤2k，刷新/optimizer后持续正交及semantic specialization未认证，任务反退/约5%训练吞吐代价保留。root必要源/actual owner PRE通过并授一段窄锁；作者已顺读正文/完整邻接；root非作者实际正文/完整邻接及末注POST通过，窄锁已释放。未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-10965` — Daily `2026-02-13`；[MoEEdit exact-v1](https://arxiv.org/html/2602.10965v1) §3、Tables1–3与必要配置。2+1+2=5，routing preservation设计反侧深入；只采用冻结router≠冻结输入、coupled output fit与exact-null/near-null分工，不采Top-k/全域严格不变、所有BCD收敛或跨方法公平性能。root实际必要原源与current owner/邻接PRE通过授Ch21窄锁；实际两段正文、前后邻接与末注已由root非作者POST通过，窄锁释放，日级未授；未核代码或复现。

- `SF-2026-ARXIV-2602-06154` — Daily `2026-02-10`；[exact-v1](https://arxiv.org/html/2602.06154v1) §2.2–2.4、§3必要对照/transfer、§5及A1。5=2+1+2标准审阅，root 必要原源与具体 owner 写前核通过；采用 nested expert prefix 与 full/random width 训练的分工，保留 clip 后非严格预算、校准和欠训练边界。GPT2/OWT、4×A100 DDP，MFLOPs不作实测 latency，未核离散梯度实现、未复现实验；root 实际正文/邻接及源注非作者POST通过，日级Gate未授。

- `SF-2026-ARXIV-2601-02144` — Daily `2026-01-07`；[exact-v1](https://arxiv.org/html/2601.02144v1) §4.1–4.2、Implementation Details、§6.6/Limitations，原2+1+2=5，现正文实现归属冲突触发受影响内容深入，不因此提高评分。纠正 memory value 为 Top-K softmax assignment、在线 assignment mixture/支持并集；logit mixing 保留为另一实现，未授全局最优或相似度即正确概率。root 必要原源和窄纠错写前及实际正文/图/末注 POST 通过，未复现。

- `SF-2026-ARXIV-2601-00457`（Experimental）：[exact-v1](https://arxiv.org/html/2601.00457v1)，§2、§3.1–3.4、§4、Limitations。采用 flattened-weight trace 与固定输入 quadratic form 的对象区别，以及参数代理不替代功能验收的受限反证；正文修正原文将 trace 称为“所有元素之和”的措辞。约130M、8 experts/top-2、6 layers、10K iterations；TinyStories 5 seeds、WikiText/PTB 3 seeds，未用辅助 load-balancing loss。WikiText 局部改善、PTB 高方差与 λ/架构限制保留，不外推所有正则化或统计独立；hardware/precision=`Not Disclosed`。root 必要原源、具体 owner 及实际新增正文/邻接的非作者写后复核通过；未复现实验。

- `SF-2026-ARXIV-2604-19835`（Experimental）：[exact-v1](https://arxiv.org/html/2604.19835v1)，§3.1–3.2、§4.2、§5.3。采用 utility-copy 与全训练路线成本分账，不采用凸 OCO 到非凸训练的收敛外推；固定 top-k 不能免除扩展状态/通信。source→owner经apr24_close独立核，实际新增正文已由apr24_close非作者写后核；未复现实验。

- `SF-2026-ARXIV-2604-20156`（Experimental）：[exact-v1](https://arxiv.org/html/2604.20156v1) §3–5/Table2–3/§10，Daily 2026-04-23。吸收 per-layer option mask、termination/deliberation cost 与原 token Router 分责，不采用真实卸载/节时收益。作者单一 gpt-oss-20b、4×H200 BF16+LoRA 训练、每 benchmark 200题，mask16 与8存在能力退步；只单训练 run，switch proxy 不等设备 residency 证据。apr20_resume 已非作者 source→实际 owner及实际正文/相邻段写后复核通过（`daily-20260423/V3_APR20_LAST_TWO_INDEPENDENT.md`），未复现实验。

- `SF-2026-ARXIV-2604-21330`（Experimental）：[exact-v1](https://arxiv.org/html/2604.21330v1) §3/Eq6–9/Algorithm1、§4.2 Table3、§5.2–5.4 Tables5–7、J.4。采用冻结 dense features、可训练辅助 router 到 student 的 stop-gradient KL 指导分支；末层、仅模仿及指导时长反例、teacher 资产和受限视觉实验保留。apr02 必要 source→实际 owner 采用复核通过；root 实际顺读新正文及其与负载代理、global/local balance 的衔接后，非作者写后复核通过，未复现实验。

- `SF-2026-ARXIV-2604-17228`：[exact-v1](https://arxiv.org/html/2604.17228v1)，Daily 2026-04-21；§3.3/§4/§5.4/§5.6/§6。采用 stability aux 与计算价值 teacher 的未来策略/部署 gate 分账，不把 mismatch 假说定为唯一成因。frozen backbone、低预算 seed 反例与 V100 窄壁时保留。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-13508`，Experimental：[exact-v1](https://arxiv.org/html/2604.13508v1) §3.1–3.4 Eq7–13、§4.4/Table3。采用同 base 的 activation 分区初始化、第一层线性近似与 dense EMA / Top-k 条件分支；不采用 Eq7 已被最优求解、完整 FFN 保持或 router 熵即语义/吞吐保证。CLIP 校准域、rank 和 EESD 单独退步保留。root 必要来源→实际 owner 采用与真实正文/相邻衔接写后独立通过，未复现实验。

- `SF-2026-ARXIV-2604-14246` — [CoR v1](https://arxiv.org/html/2604.14246v1)，Daily `2026-04-17`。采用 §3.2.1–3.3/Eq3–9 的已激活hard-token virtual ablation→offline prior→runtime router融合，保留 Tables1–3 任务退步与active-count非等成本。复用 apr01 有效必要原文/当前owner PASS（daily-20260417/v3-reopen-notes.md「三项source→owner」收据）；root已对读采用定位/当前gap认可复用，root已实际顺读正文与两侧/复用有效必要证据后写后独立PASS；真实整合，本批章锁释放。

- `SF-2026-ARXIV-2604-08133`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.08133v1) §3.2–3.3、§4–6、Tables4/7、Appendix A.1–A.2。Alloc-L以逐层PPL sensitivity的加性surrogate做DP；Alloc-T在原候选内先每token保留floor、再分配剩余预算。Eq7候选大小与Eq9预算张力不采用最优保证；负载ρ=.93–.99不证明expert语义或EP通信收益。三模型、WikiText2及20任务受限，Qwen部分joint低于token-only；单H10080GB、随机prompt batch8/input32/decode128、五warmup/十次测量，不是生产SLO，精度/并发合同未完整披露。未复现实验；待root必要原文/实际正文写后独立复核，不代表整日报验收。

- `SF-2026-ARXIV-2604-06515`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.06515v1) §3.3、§4.1–4.3、§5.1–5.4/Tables1–4。norm change 是 final norm 减 initial norm，不是参数差向量范数；rare-feature 理论限二元单相关 token、初始 alignment 与定量位宽前提。final-norm proxy 只以重新初始化 Switch 检验；Mixtral各任务/低平均位宽有反例，不采用lossless或生产latency/SLO。未复现实验；必要原文、实际正文及相邻衔接的非作者复核通过（root），不代表整日报验收。

- 树形条件 FFN（Status: Experimental；`SF-2026-ARXIV-2604-08565`）：https://arxiv.org/html/2604.08565v1 ，§3、§5.1–5.2、§6 Tables 1–3、§7–8。硬二叉路径与节点输出共用响应，GELU 位置影响梯度偏斜；均衡不保证质量更优，统计剪枝需验收。125M 三 seed 对照与 OPT-1.3B/26B tokens 受限证据不能外推更大模型；FT 复用已有 Attention，不能视为从零训练同预算。§7 表格称单 A100 layer-level runtime，§8 又明确理论/模拟潜力及非 deployment-ready，因此正文不采用加速数字。训练实验精度、端到端输入输出长度/并发/Serving SLO 未由此证据完整建立；未复现实验。本次写后非作者原文、实际正文及相邻交接复核通过（root），尚不代表整日报验收。

- `SF-2026-ARXIV-2604-03592`（Experimental）：[exact-v1](https://arxiv.org/html/2604.03592v1) §3–5、Appendix C。exact preservation限fixed router与不交支持集；Qwen3-30B-A3B/Phi-3.5-MoE、single H200/BF16、batch2×acc8、lr2e-5；Phi Bengali46.89低于TopK49.51，pruning损伤他语。参数更新比例不能当总显存/服务收益，未复现实验；本次写后独立复核通过（root）。

- Instella-MoE，https://arxiv.org/html/2609.00791v1 ，§2.1.3、§3.3.1/Table13、§3.4 与 Appendix A：FarSkip 的 partial/outdated activation 属于架构变化，而不是同函数调度等价。200B tokens / 48K steps、固定设置与 seed 的单次对照只支持受限平均质量比较，各任务有升降；不采用未绑定完整 workload/SLO 的速度 headline，也不据此否定标准 MoE 内可行的通信重叠。

- `SF-2026-ARXIV-2604-00801`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.00801v1) §3.1–3.2、§4、§5、Appendix B 与 Limitations 支持 expert-local gate、bias、global density threshold 及受限训练/EP 结果；不支持“无需任何控制面”、已验证大模型迁移或生产 SLO。
- `SF-2026-ARXIV-2602-05711`（Status: Experimental）：primary=`arXiv:2602.05711v1`；Method=`§2 Methodology`；Evaluation=`§3.2 Main Results`；Non-proof=`§3.3 Ablation Studies`。只支持 Cartesian Product Router 与 expert-centric execution 在作者 atomic-expert 模型/实现中的机制和结果，不证明通用粒度最优或生产 SLO。
- `SF-2026-ARXIV-2602-07265`（Status: Experimental）：primary=`arXiv:2602.07265v1`；Method=`§3.4 Practical Algorithm`；Evaluation=`§6 Experiments`；Non-proof=`§7 Conclusion`。只支持所测 batch、speculative candidates 与 expert-parallel 环境中的共享 expert-set admission，不证明所有 batch composition 下保持质量或吞吐。
- `SF-2026-ARXIV-2602-19938`（Status: Experimental）：primary=`arXiv:2602.19938v1`；Method=`§2 Method: Replicate-and-Quantize for Efficient SMoE Inference`；Evaluation=`§3.2 Results`；Non-proof=`§5 Conclusion`。只支持所测模型中按 calibration 分离 load/importance、复制热点并量化以守住内存预算；不外推其他模型、精度、硬件或长期 traffic drift。

- `SF-2026-ARXIV-2602-17038` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17038v1) Phase-Aware Router/Temporal Consistency、实验 Tables2–4、Appendix B/C。2+2+2=6，实际原文纠正 learned contiguous expert-run 与显式 workflow phase 的混淆；single pooled K/V、hard argmax 温度、STE 及两个切换分母边界近正文。root 必要原源/actual owner PRE通过并授原两段/自身末注窄锁；作者正文/完整邻接已顺读，root非作者实际正文/完整邻接及自身末注POST通过，窄锁释放。未核实现/复现，不授阶段语义、宣传因果或生产收益，非日级验收。

- `SF-2026-ARXIV-2604-23036`（Status: Experimental）：exact-v1 支持 bias routing 与 always-active gated condenser 在作者 GPT-OSS/DeepSeek MoE SFT 合同中保留长尾 expert 信息；不证明低频 expert 的通用语义、跨模型最优 routing 或生产收益。https://arxiv.org/abs/2604.23036v1

- `SF-2026-ARXIV-2606-22325` — primary `arXiv:2606.22325v1`；Method=`arXiv:2606.22325v1 §2 Problem Setup; §3 Routing Dynamics and Collapse Analysis`；Evaluation=`arXiv:2606.22325v1 §4 Experiments; §5 Ablations`；Non-proof=`arXiv:2606.22325v1 §6 Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- MoX: Efficient MoE Routing on Direct-Connect Topologies（arXiv:2607.20220v1；Status: Experimental）：https://arxiv.org/html/2607.20220v1
  - 证据边界：支持披露 topology/workload 假设下的 routing/tree algorithm 与 simulation/proxy 改善；不证明 deadlock-free 实现、故障行为、真实硬件时序，或相对 switch fabric 的普遍收益。

本轮联章 Review 明确 MoE 是第 16 章 Dense MLP 的条件化替换，不是 Sampling 的后继阶段，并区分有效 token states、padding positions 与 top-k expert assignments。既有 active/total parameters、load balance、All-to-All、`[B,T,E]` router shape、top-2 演算和 capacity 近似保持不变。Grouped GEMM 只作为 router 产生不规则 expert batches 后的执行接口，kernel 与通信融合仍由第49章及后续 Runtime 章节拥有。

Nemotron 3 Super 的公开报告为 latent-coordinate routing/expert compute 提供了一个受限实现案例；正文只吸收“state coordinate 决定 dispatch bytes”的长期机制，不保留模型规模、top-k、量化或跨 runtime benchmark headline。

Primary-source 校验入口：

- ConceptMoE（learned sequence compression before conditional compute；作者实验边界）:
  https://arxiv.org/abs/2601.21420
- Nemotron 3 Super Technical Report（Status: Experimental）: https://arxiv.org/abs/2604.12374
- EMO（document-scoped expert pool 与 versioned subset；Status: Experimental）:
  https://arxiv.org/abs/2605.06663
- ZEDA / Post-Trained MoE（zero-output dynamic-compute route；Status: Experimental）:
  https://arxiv.org/abs/2605.18643
- NVIDIA sync-free MoE fused kernels（SM100-bounded implementation evidence）:
  https://developer.nvidia.com/blog/boosting-moe-training-throughput-with-advanced-fusion-kernels/

- Noam Shazeer et al., "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer", 2017: https://arxiv.org/abs/1701.06538
- Dmitry Lepikhin et al., "GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding", 2020: https://arxiv.org/abs/2006.16668
- William Fedus, Barret Zoph, Noam Shazeer, "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity", 2021: https://arxiv.org/abs/2101.03961
- Kimi Team, "Kimi K3: Open Frontier Intelligence", arXiv v1, 2026（受限系统案例）: https://arxiv.org/abs/2607.24653
- "Routing by Analogy: kNN-Augmented Expert Assignment for Mixture-of-Experts", arXiv:2601.02144（受限实验案例）: https://arxiv.org/abs/2601.02144
- "Towards Principled Design of Mixture-of-Experts Language Models under Memory and Inference Constraints"
  （受限 scaling-law 案例）: https://arxiv.org/abs/2601.08215
- ERNIE 5.0 Technical Report（elastic depth/width/sparsity；作者模型边界）: https://arxiv.org/abs/2602.04705
- TAOT（topology-aware expert replica placement；Status: Experimental）: https://arxiv.org/abs/2608.03676

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22798` — primary `arXiv:2606.22798v1`; Method=`arXiv:2606.22798v1 — §Does the Same Token Mean the Same State? MoE Routing as Signal for Reasoning Control; §MoE routing.; §3 Analysis of Anchor-Conditioned Routing`; Evaluation=`arXiv:2606.22798v1 — §3 Analysis of Anchor-Conditioned Routing; §5.3 Analysis`; non-proof=`arXiv:2606.22798v1 — §7 Conclusion; §A.13 Failure case studies`; fallback=该 family 的 failure pressure 是：In sparse Mixture-of-Experts language models, does the same token id imply the same router state and the same experts producing it? 披露的 evaluation signal 是：Its value is the interface: the same selector gives direct pass@1 on code, where exact-string voting is ill-defined, and the same routing-density principle, re-anchored to the agentic boundary, improves best-of-16 patch selection on SWE-bench Verified over random, where patches have no answer string to vote on. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2607-20220:start -->
- `SF-2026-ARXIV-2607-20220` — Daily `2026-07-23`；primary `arXiv:2607.20220v1`；Books review `books-review:SF-2026-ARXIV-2607-20220`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: source-to-destination unicast dispatch -> selected-expert multicast tree -> reverse-tree partial reduction under direct-connect congestion 该 delta 已进入 `books/part-02-model/21-moe.md#L242`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-20220:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-26052:start -->
- `SF-2026-ARXIV-2607-26052` — Daily `2026-07-29`；primary `arXiv:2607.26052v1`；正文锚点“从固定 Top-k 到受总预算约束的 Variable-k”。
  证据限作者披露的 matched-compute、两个 backbone 与任务，不证明 router mass 是通用不确定度或满足生产尾部 SLO。
<!-- daily-books-trace:SF-2026-ARXIV-2607-26052:end -->

- `SF-2026-ARXIV-2512-23995`：[exact v1](https://arxiv.org/html/2512.23995v1) §3.3/Eqs3–4、§3.4、§4.1–4.3/§5.3。采用输入分布、expert集中与placement条件共同决定device负载的反证边界；router覆盖模拟不等kernel延迟，remote平均TTFT不证明隐藏MoE身份、tail SLO或生产DoS。必要原源、限定命题及实际正文/邻接已由root非作者复核通过，未运行攻击或复现实验。

- `SF-2026-ARXIV-2601-10159` — Daily `2026-01-17`；[exact-v1](https://arxiv.org/html/2601.10159v1) §2.2/3.2/Table1、C1。6分 activation frequency 与 gate-perturbation/output-KL 分账的具体 gap 深入；不授 expert ontology、阈值或隔离语义因果，Top-k/renormalization/LoRA与预算限制近正文。未核实现或复现；root必要原源/owner写前通过，root实际两段/前后邻接及末注非作者POST通过，窄锁释放；日级Gate未授。

- `SF-2026-ARXIV-2602-09316` — Daily `2026-02-12`；[exact-v1](https://arxiv.org/html/2602.09316v1) §3.1–3.4/Alg1、Table2–5。具体 owner 差额受影响深入：rank/frequency shared-basis 与 sparse latent residual；不授全维无损、语义重要度或端到端吞吐。root 必要原源/具体 owner 写前通过并授窄锁；root 已实际顺读两段、完整邻接与本末注，非作者 POST 通过，窄锁释放。未核代码/复现，非日级 Gate。

- `SF-2026-ARXIV-2602-15521` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15521v1) §3–4/Tables2–3、A2/F/L；2+1+2=5，激活 profile/shared 比例及 dense 切片转 softmax routing 的函数变化深入。全部权重、25% sparsity 掉分、校准/CPT/SFT 与单 GPU 固定并发限制保留，不授函数保持或总成本/SLO 保证。root 必要原源及 actual owner PRE 通过并授窄锁；作者已顺读正文/完整邻接，root 实际正文/完整邻接/末注非作者 POST 通过，窄锁释放，未核实现或复现，非日级 Gate。

- `SF-2026-ARXIV-2602-12746` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12746v1) 必要方法/关键控制/直接限制；2+1+2=5，具体owner差额定点深入。仅采用正文条件机制；相关理论/效果强保证隔离，成本与回退近正文。root必要原源/actualowner PRE通过并授窄锁；作者正文/完整邻接已顺读，root非作者实际正文/完整邻接/末注POST通过，窄锁释放，未核实现或复现，非日级Gate。
