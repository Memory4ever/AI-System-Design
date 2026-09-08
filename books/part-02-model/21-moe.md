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

小中规模搜索中拟合出的 exponent 可以帮助生成候选，不能成为跨规模定律。真实设计还必须把 HBM、
parallel divisibility、load imbalance、topology、kernel efficiency、training tokens 与 Serving SLO 加入
约束；当这些条件变化时，论文搜索空间内的“最优”也会变化。因此 total/active parameters 继续作为
model-card 粗 contract，architecture search 则必须用 loss evidence 与 system cost model 联合裁决。

固定 `depth / width / top-k` 的 MoE 最容易分别优化训练与 Serving；当同一权重族要覆盖多档 latency、memory 与 cost budget 时，可以把这些选择变成训练期采样的 subnetwork path。这样一次训练产生多个执行点，却把“模型版本”扩成：

```text
shared checkpoint
+ active depth / expert subset / top-k profile
+ profile calibration and quality envelope
+ kernel / collective / placement plan
```

共享参数会让不同路径的梯度互相干扰，低频子网可能欠训练；每个 profile 还需要独立的 quality、capacity 与 SLO 验证。固定模型在 workload 稳定、极致性能或认证边界严格时仍更容易优化。Elastic super-network 因而是 deployment portfolio 的条件分支，不是 MoE 的默认终点。

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

另一条降低 small-batch weight traffic 的分支不缩小 token coordinate，而是改变 experts 的参数独立性。标准 MoE 为每个 expert 保留完整 MLP，提供最大的专门化自由，却会在一次请求命中多个 experts 时搬运大量相似权重；department-style 组织让一组 experts 共享 trunk，仅保留较小 private delta，并用两级 router 先选组再选私有分支：

```text
token state
→ route to shared department trunk
→ route to small private expert delta
→ combine into residual path
```

共享提高 weight reuse、缩小工作集，却用表示耦合、两级 routing 与潜在 expert interference 换取内存收益。需要强独立专业化、共享部分形成负迁移或大 batch 已能摊薄独立 weight load 时，标准 experts 仍更合理。`arXiv:2608.14385v1` 只在作者的 7B pretraining 与 DeepSeek-V3 microbenchmark、A40/H100 配置上支持这一 operating point，不证明跨节点吞吐、训练稳定性或语义专业化普遍改善。

<!-- source-family:SF-2026-ARXIV-2608-14385 -->

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

## 为什么负载均衡是模型正确性的一部分

如果 router 总把 tokens 送到少数 experts：

- 热门 expert 超载或产生排队。
- 其他 experts 缺少训练信号。
- 矩阵 batch 不均匀，硬件利用率下降。
- 超出容量的 tokens 可能被丢弃或转发。

理想路由同时追求 specialization 与 balanced load，但二者可能冲突。训练通常加入 auxiliary load-balancing objective，让平均 router probability 与实际 token assignment 不要过度集中。

Auxiliary loss 是代理约束，不证明所有 experts 语义均匀，也不保证每个 batch 完全平衡。权重过强还可能牺牲内容路由质量。

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

路由还要分开两个经常被 softmax 混在一起的控制量：**选择哪些分支**，以及**被选分支各自贡献多少**。归一化权重容易
微分，也适合真正需要竞争性 specialization 的 top-1/soft mixture；但在声明激活 `k` 个 adapter 或 expert 时，权重高度集中
可能造成“计算了 `k` 个、有效容量却接近 1”的假象。可用 effective support 之类的量检查这一差异，而不能只看 top-k 数量。

另一条分支让 router 只产生离散 subset，被选分支使用固定贡献系数；它把支持度固定为 `k`，却放弃 input-dependent
contribution magnitude，并把训练变成 policy-gradient 或其他离散优化问题。训练时 stochastic subset 与推理时 deterministic
top-k 还会产生 distribution gap。Router policy、adapter/expert 参数、selection rule 和 contribution rule 因而必须共同版本化。
ReMix 在单一模型家族和若干任务上的结果只证明这种分责可以避免其定义下的 routing collapse；它没有覆盖大规模 MoE、
adapter paging、batch locality 或多租户 serving。Softmax mixture 在 top-1、规模较小或需要平滑端到端优化时仍合理；离散选择
只有在额外训练方差与推理状态成本小于有效容量收益时才成立。

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

### Topology-conditioned Multicast 是 Dispatch 的替代分支

在 direct-connect fabric 上，MoE dispatch 不一定要让 source 分别向每个 selected expert 发送完整 activation。若 selected experts 可作为受控 relay，可以建立 source-rooted multicast tree，并在反向 combine tree 上做 partial reduction；这样用多跳与 relay state 换取 source-link congestion。

Router 仍只拥有 token→expert 语义，tree/weight catalog 属于 topology-aware runtime。该分支新增 relay ordering、fault recovery、deadlock 与 topology epoch；强交换网络、小 fanout、故障频繁或 ordering 难验证时，普通 unicast/All-to-All 仍更合理。训练侧 transport/runtime 细节回到第 36 章。

逻辑上，dispatch 输入可看作 `[N,d_model]` token states 和 `[N,k]` routes。物理上需要 grouped GEMM、padding 或动态 shape 来处理每个 expert 的不同 token count。

Grouped GEMM 不是把 MoE 改成一个数学上的稀疏矩阵乘法。它把多个共享 dtype 和部分 layout 约束、但拥有不同 `M_e` 的 expert GEMMs 交给一次 library/kernel 调度：减少逐 expert launch 和 padding 机会，却仍要处理空 expert、长尾 `M_e`、metadata、对齐与负载不均。Dense GEMM、grouped GEMM 与通信融合属于第49章的 execution mapping；本章只拥有 router 如何产生这些不规则 expert batches。

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

Expert Parallel 与其他并行维度不同：

```text
Tensor Parallel    split one operator
Pipeline Parallel  split layer depth
Data Parallel      split samples
Expert Parallel    split expert set and dynamic token routes
```

组合后 process groups、checkpoint 和容错都会更复杂。

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

这些运行时策略不在本章展开，但模型 router 已经决定它们必须存在。

## 从参数化 Router 到带检索记忆的 Router

训练得到的 parametric router 是最稳妥的起点：它没有外部索引，前向路径短，模型版本一旦冻结，
路由语义也随之冻结。在训练分布稳定、在线延迟严格或缺少可信参考样本时，这种设计仍然最合理。
它的边界是，遇到 distribution shift 时只能依靠参数中已经学到的决策面，不能直接复用“相似 token
曾经怎样路由更好”的局部经验。

一种受限的演进路径，是把 expert assignment 拆成参数化先验与检索修正：离线为参考 token 优化
routing logits，以 hidden representation 为 key、优化后的 logits 为 value 建立 per-layer memory；
在线检索近邻，根据相似度置信度在 continuous logit space 混合原 router 与 retrieved logits，最后
仍由 Top-K 产生 executable route。这样没有用 memory 替代 router，而是保留原 router 作为低置信度、
索引失效或查询失败时的 fallback。

```text
hidden state
-> parametric routing logits
+ nearest-neighbor lookup in versioned per-layer memory
-> confidence-weighted logit correction
-> Top-K expert ids and weights
-> dispatch
```

这项变化把 router 从纯模型函数扩展成一份需要治理的运行时状态。收益来自把逐请求优化移出
critical path；代价则是 index latency、额外显存，以及 reference set 的 provenance、freshness、
tenant isolation、delete/supersession 和 rollback。相似度高也不等于 expert assignment 正确；错误
标签、reference drift 或 OOD query 会系统性注入错误路由。检索实验能证明的只是特定模型、参考集和
benchmark 下的局部改进，不能证明开放域或 expert-parallel 生产系统中普遍更优。

因此这里的技术演进不是 `learned router -> retrieval router` 的替代关系，而是：

```text
frozen parametric router
-> optional retrieval correction with confidence
-> versioned memory and observable fallback
```

当检索修正真正进入生产时，模型层还必须把 memory revision 和 routing decision 交给第56章的调度与
观测契约；expert placement、All-to-All 和 fault recovery 仍不能由相似度检索单独解决。

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

### 长尾 Expert 低频不等于无知识

MoE SFT 中用全局 load-balancing loss 或 dense mixing 阻止 router collapse，容易实现并能保持所有 expert 获得梯度；但额外梯度也可能干扰任务相关 routing。反过来，按激活频率直接剪除低频 expert，会把“少被调用”误当成“没有贡献”。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-23036:start -->
一个实验性分支以 bias-driven routing 让任务相关 expert 保持活跃、让部分长尾 expert 稀疏化，同时增加 always-active gated condenser path，为否则可能 gradient-starved 的信息提供持续可训练通道。Router bias、sparse experts 与 condenser 分别拥有 route proposal、条件容量和共享巩固路径；它避免强制所有 expert 均匀，却新增 condenser bottleneck、route bias drift 与额外常驻计算。完整 load balancing 在 workload 多样、expert utilization 是主要瓶颈时仍合理；没有证据证明长尾信息可迁移或 condenser 稳定时，应保留原 experts 并回退现有 SFT。作者实验限于 GPT-OSS/DeepSeek MoE、选定数据与 8×H100，不给出通用 router optimum。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-23036:end -->

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

### Execution Phase 可以成为 Router State，但不能成为隐藏标签

token-level router 在每个位置独立选择 expert，适合语义局部且执行阶段不可观测的生成；Agent RL 的 planning、tool use、observation assimilation 与 answer commit 具有不同动作分布，把它们全部交给同一瞬时 router，可能在 phase boundary 上反复切换或让高频阶段吞噬容量。条件分支可以把显式 phase state 作为 router 输入，并对相邻时刻施加有限 temporal consistency：workflow/runtime 拥有 phase transition，router 只据此提出 expert mixture，expert weights 或 LoRA expert 仍是版本化 artifact，不能由模型在无证据时自行改写 phase。

phase-aware routing 可以降低跨阶段梯度冲突、形成行为 specialization，却会增加 phase annotation/recognition error、切换滞后、router collapse 和专家闲置；过强一致性还会阻止真正的阶段转换。阶段边界不可靠、任务不是多阶段或 token-level evidence 已足够时，原有 top-k router 仍更可解释。任何收益都必须同时报告 phase definition、expert utilization、task return 与额外 routing/communication cost，不能把可命名 expert 当作真实能力所有权。

<!-- SF-2026-ARXIV-2602-17038 -->

## MoE 与模型“专家化”的边界

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

Expert 可能对某些 token 类型、语言或模式表现出统计偏好，但 router/expert specialization 是训练结果，不保证每个 expert 对应一个可命名领域。

标准 MoE 也不是先把数据按“数学、代码、语言”拆开，再逐个训练独立 experts。通常 shared layers、router 与 experts 在同一个端到端 objective 下 joint optimization：一个 token 的主任务梯度只进入它实际选择的 expert paths，shared layers 接收跨 routes 的信号，router 同时受到主任务信号与 load-balancing/capacity 约束。于是每个 expert 看到的是 router 动态形成的条件样本分布，而不是人工声明且永久不变的领域 dataset。

稀疏更新会形成 specialization，却也可能造成 rich-get-richer、expert starvation 与共同表示漂移；这正是 load balancing 属于训练正确性而不只是设备利用率的原因。按领域预训练独立模块后再组合属于另一种 modular composition 路线，需要额外解决 router calibration、shared coordinate、冲突和联合 Evaluation，不能被当作 MoE 的默认训练方式。

把 expert 命名为“数学专家”或“代码专家”需要行为、路由和干预证据。负载均衡还会主动阻止所有相关 token 只集中到单一 expert。

MoE 的稳定定义是 conditional computation，不是人工预先划分知识部门。

### Expert 数量改变后，超参数也需要架构身份

Dense FFN 或固定 expert 配置中，直接复用一组已经调好的 learning rate、初始化尺度和 width scaling，在架构不变时成本最低，也容易比较实验。当 Dense FFN 被拆成更多、更窄或更宽的 experts 后，总参数、单 token active parameters、router 分配和每个 expert 实际接收的样本量不再同步变化；此时把旧超参数原样搬过去，会把“条件计算机制是否有效”与“参数化是否失配”混在同一次训练里。

更稳健的演进是把超参数从某个 checkpoint 的经验数字提升为带架构坐标的 scaling identity：training owner 明确 dense width、expert width/count、top-k、初始化与 optimizer scale 之间的变换，router 仍拥有 token-to-expert 选择，runtime 仍只执行已发布的稀疏路径。这样可以减少每一种 MoE 形态都重新网格搜索的成本，并让 dense-to-MoE 对照更可解释；代价是参数化公式本身也要经过规模、数据和 optimizer family 的校准，错误迁移会表现为训练不稳、expert 饥饿或把架构差异误判成优化收益。

当架构变化很小、训练预算足以独立调参，或目标 optimizer/数据分布离校准域很远时，逐配置 tuning 仍是可信 fallback；统一 scaling rule 是可迁移的起点，不是免调参保证。`arXiv:2605.23893v1` 的 §3 与 §5 支持在作者披露的 Dense FFN/MoE 配置间构造并评估这类超参数迁移，§6 不证明任意 expert topology、模型规模、数据或 optimizer 都保持最优。

<!-- source-family:SF-2026-ARXIV-2605-23893 -->

## Dispatch 与 Aggregation 是两种不同责任

Top-k router 同时决定“哪些 expert 计算”和“这些结果以多大权重提交”时，选择与信任被耦合。固定 expert IDs 和计算量后，单独学习 aggregation 仍可能改变结果，说明 dispatch 负责容量与通信，aggregation 才负责对候选 expert 输出的 commitment。

拆分增加一个 head 和校准状态，也可能在小模型上得不偿失；传统 router 在路由稳定、实现简单优先时仍合理。该结论来自有限模型，不应外推成所有 MoE 必须解耦，但系统监控和负载均衡不能把 aggregation weight 误当 dispatch identity。

<!-- source-family: arxiv:2608.08853v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: expert-dispatch-vs-aggregation-ownership -->

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

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22325 -->
把 MoE collapse 从单一 load-balance 指标提升为 routing dynamics：多种平衡正则最终可进入相似退化吸引域，必须同时观察 expert specialization、token flow 与训练阶段。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；结论受模型规模、数据和 router family 限制；观测到共同吸引域不证明所有 MoE 必然 collapse。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

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

### Prefill 与 Decode 可以使用不同 Expert Set，但必须共享误差合同

prefill 的 token 之间差异大，适合按 token 保留专家；decode 的小 batch 则可能让路由碎片化，使 batch-level expert pool 更利于复用。两种 phase-specific 策略不能只比较命中率，而要在相同输出近似误差、capacity、drop policy 和 batch 条件下验收，并把 retained set 写入执行身份。这样可以降低部署成本，但也增加跨阶段状态切换与回退复杂度。
<!-- source-family: arxiv:2608.24938v1; semantic-body-binding: phase-specific-expert-retention-contract -->

### Shared-first 与 Routed-residual 是另一种容量分工

传统 MoE 先由 Router 决定 token 进入哪些专家，公共能力也可能被稀疏路由切碎。另一条分支让共享路径先承担稳定公共变换，再只把剩余误差交给专家路由；它降低了公共知识对路由抖动的敏感性，却会把共享层变成新瓶颈，并不能消除 expert collapse。两种结构应按公共容量、路由熵、通信和尾部质量共同验收，而不是把 shared-first 当作无条件升级。
<!-- source-family: arxiv:2608.10392v1; semantic-body-binding: shared-first-routed-residual-capacity-boundary -->

## 小结

MoE 把 Dense MLP 改造成条件计算：Router 为每个 token 选择少数 experts，使总容量可随 expert 数增加，而单 token expert compute 主要随 top-k 增长。

代价是路由成为模型与系统共同状态。负载均衡、capacity、token dispatch、All-to-All、expert placement 和小 GEMM 效率决定稀疏参数能否转化为真实收益。


## Review notes

- Instella-MoE，https://arxiv.org/html/2609.00791v1 ，§2.1.3、§3.3.1/Table13、§3.4 与 Appendix A：FarSkip 的 partial/outdated activation 属于架构变化，而不是同函数调度等价。200B tokens / 48K steps、固定设置与 seed 的单次对照只支持受限平均质量比较，各任务有升降；不采用未绑定完整 workload/SLO 的速度 headline，也不据此否定标准 MoE 内可行的通信重叠。

- `SF-2026-ARXIV-2602-05711`（Status: Experimental）：primary=`arXiv:2602.05711v1`；Method=`§2 Methodology`；Evaluation=`§3.2 Main Results`；Non-proof=`§3.3 Ablation Studies`。只支持 Cartesian Product Router 与 expert-centric execution 在作者 atomic-expert 模型/实现中的机制和结果，不证明通用粒度最优或生产 SLO。
- `SF-2026-ARXIV-2602-07265`（Status: Experimental）：primary=`arXiv:2602.07265v1`；Method=`§3.4 Practical Algorithm`；Evaluation=`§6 Experiments`；Non-proof=`§7 Conclusion`。只支持所测 batch、speculative candidates 与 expert-parallel 环境中的共享 expert-set admission，不证明所有 batch composition 下保持质量或吞吐。
- `SF-2026-ARXIV-2602-19938`（Status: Experimental）：primary=`arXiv:2602.19938v1`；Method=`§2 Method: Replicate-and-Quantize for Efficient SMoE Inference`；Evaluation=`§3.2 Results`；Non-proof=`§5 Conclusion`。只支持所测模型中按 calibration 分离 load/importance、复制热点并量化以守住内存预算；不外推其他模型、精度、硬件或长期 traffic drift。

- `SF-2026-ARXIV-2602-17038`（Status: Experimental）：exact-v1 的 Method/Phase-Aware Router/Temporal Consistency/Behavioral Experts 定义 phase-conditioned routing，Experiments/Main Results/Ablation Studies 给出作者设置中的结果，Supplementary failure analysis 暴露 gradient conflict、entropy mismatch 与 simplicity bias；它不证明 phase 标签普适、行为 expert 可解释或生产 serving 收益。https://arxiv.org/html/2602.17038v1

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

### Source-family integration record

<!-- recovered-daily-20260623:MODEL-MOE:start -->
### 2026-06-23 evidence integration — MODEL-MOE

相邻章 `books/part-02-model/22-long-context.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22798**：Does the Same Token Mean the Same State? MoE Routing as Signal for Reasoning Control 的 exact-v1 机制为：Holding the emitted token id fixed at repeated anchors, we find it does not: the experts that produce it still separate task context, trajectory history, and reasoning-effort mode. 因此 把 router state 视为内部诊断/选择信号，而不是未经验证的正确性证明。 该 family 的 failure pressure 是：In sparse Mixture-of-Experts language models, does the same token id imply the same router state and the same experts producing it? 披露的 evaluation signal 是：Its value is the interface: the same selector gives direct pass@1 on code, where exact-string voting is ill-defined, and the same routing-density principle, re-anchored to the agentic boundary, improves best-of-16 patch selection on SWE-bench Verified over random, where patches have no answer string to vote on. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:MODEL-MOE:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2607-20220:start -->
- `SF-2026-ARXIV-2607-20220` — Daily `2026-07-23`；primary `arXiv:2607.20220v1`；Books review `books-review:SF-2026-ARXIV-2607-20220`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: source-to-destination unicast dispatch -> selected-expert multicast tree -> reverse-tree partial reduction under direct-connect congestion 该 delta 已进入 `books/part-02-model/21-moe.md#L242`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-20220:end -->
