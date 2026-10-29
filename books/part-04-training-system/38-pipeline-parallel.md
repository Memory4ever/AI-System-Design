# 第38章 Pipeline Parallel

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-PIPELINE-PARALLEL`
**Legacy Chapter:** Ch34
**Status:** Draft

**Roadmap Intent:** 把模型层切到多张卡上，流水线执行。

## 本章要回答的问题

Tensor Parallel 可以缩小单层，但整个深模型仍可能放不下。怎样沿 layer depth 切成多个 stages？为什么切完层后 GPU 仍会等待？Micro-batch、1F1B 和 interleaving 怎样改变 bubble、activation lifetime 与通信？

本章的核心判断是：**Pipeline Parallel 通过 layer partition 分担模型深度，真正的效率由 micro-batch schedule、stage balance 与 boundary communication 决定。**切层解决 capacity，流水线调度才决定这些 stages 是否持续工作。与第 36 章的 group collective 不同，PP 主要消费相邻 stage 间的 point-to-point 语义；这两种通信模式可以由同一底层 transport 承载，但 completion 与 ordering 契约不同。

本章使用 `p` 表示 pipeline stage 数，`m` 表示一个 optimizer step 中流过
pipeline 的 micro-batch 数，`B_micro` 表示每个 DP rank 的 micro-batch
samples，`D` 表示 data-parallel degree，`B_global` 表示 global batch size。
在本章的 pipeline schedule 中，`m` 对应 Part IV 统一公式中的
`gradient_accumulation_steps`。

## 只有 Layer Partition 会发生什么

把 `L` 层模型切为 `p` 个连续 stages：

```text
Stage 1: layers 1 ... l_1
Stage 2: layers l_1+1 ... l_2
...
Stage p: ... layer L + loss
```

Forward 时，Stage `i` 输出 activation 给 `i+1`；backward 时，activation gradient 反向传给 `i-1`。

若整个 batch 作为一个 unit：

```text
S1 forward -> S2 forward -> ... -> Sp forward
```

在 S1 工作时，后续 stages 空闲；在最后 stage 工作时，前面 stages 也在等待。Layer capacity 已经分散，设备利用率仍很低。

后面的 micro-batch 调度保留这条精确层依赖，只把不同样本的工作交错；另一条[数值求解分支](https://arxiv.org/html/2601.09026v1)则把 residual depth 看成离散时间轴，用 MGRIT 的局部并行 relaxation 与 coarse-grid 串行 correction 近似 activation，再近似 backward。它改变的是状态和梯度的求解精度，不是更好的普通 PP schedule。受测 neural-ODE 变体还把中间层步长设为 $1/L$，首尾 buffer 保持串行与原步长；这改变模型，不能直接把原 checkpoint 当作等价执行。<!-- source-family:SF-2026-ARXIV-2601-09026 -->

近似误差会使训练停滞或偏离，因而迭代次数与 residual 检查进入训练状态：误差升高时增加 solve iterations，必要时切回 exact serial forward/backward；fine/coarse evaluation 的 dropout mask 也必须一致。它增加 correction、通信和误差控制成本，浅模型或少设备时可能比串行慢，深度与 coarse 配置也改变质量取舍。作者部分 GPU 扩展实验同时扩大 batch，不能把该速度曲线当作等 global-batch 收益，局部恢复结果也不证明任意模型“同精度”。不满足模型、精度或预算条件时，保留精确 PP 与串行基线。

## Micro-batch 怎样填充 Pipeline

把 batch 拆成 `m` 个 micro-batches，不同 stages 可以同时处理不同 micro-batches：

```text
time 1: S1 F(mb1)
time 2: S1 F(mb2) | S2 F(mb1)
time 3: S1 F(mb3) | S2 F(mb2) | S3 F(mb1)
```

若 pipeline replica 中每 step 有 `m` 个 micro-batches：

```text
B_global = B_micro * m * D
```

这里假设每个 micro-batch sample 数相同。Variable-length sequence 仍可能让 token workload 和 stage time 不同。

Micro-batch 不是额外 optimizer step。通常所有 `m` 个 micro-batches 的 gradients 累积完成后，才执行一次同步 parameter update。

## Bubble 从哪里来

Pipeline 开始时需要 warm-up，结束时需要 drain。理想均衡、只考虑简单 forward pipeline 的 bubble fraction 近似：

```text
bubble_fraction ~= (p - 1) / (m + p - 1)
```

它用于建立方向，不是完整 training schedule 的通用公式。

例如 `p=4`：

```text
m=8:
bubble ~= 3 / 11 ~= 27.3%

m=32:
bubble ~= 3 / 35 ~= 8.6%
```

更多 micro-batches 可以摊薄 fill/drain，但 local micro-batch 过小会降低 GEMM efficiency，并增加 boundary messages 和 scheduler overhead。

异构 stage 还应把一次 fill 与稳态节拍拆开。只在纯 forward、固定服务时间、无限 buffer 且没有其他资源争用的模型里，`m` 个 micro-batches 的 makespan 才是 `Στ_j + (m−1)max τ_j`；把各 stage 都替成最慢时间，会高估一次 fill，而不改变该模型的稳态斜率。若链路只是无限并行的固定 delay，传输可另作 fill 加项；另开 NCCL stream 并不满足这个假设，真实带宽、backpressure、反向和变化的序列成本仍须进入实测。[受限递推分析](https://arxiv.org/html/2610.21815v1)验证的是这些模型，gateway 请求日志不是实际 PP stage trace。推导、profile 与容量检查都有成本；假设不满足时保留原 schedule 模型和真实流水测量，不能用这个式子签发训练或 serving SLO。<!-- source-family:SF-2026-ARXIV-2610-21815 -->

## GPipe：先 Forward，再 Backward

GPipe 风格 schedule 可抽象为：

```text
F(mb1), F(mb2), ..., F(mbm)
then
B(mbm), ..., B(mb2), B(mb1)
```

优点是 schedule 和同步 semantics 直观；缺点是许多 forward activations 要等待较久才进入 backward。若不 recompute，activation peak 随 outstanding micro-batches 增长。

Activation checkpointing 可以只保存 stage input 等边界并在 backward 前重算内部 activations，用额外 compute 换 memory。

当长序列的主要计算落在无参数的 Attention 核，继续整层切 stage 会让这部分仍主导填充与排空；另一条同步分支把 pre-Attention、Attention 和 post-Attention 分开，在不同 stages 上交错执行不同 micro-batches 的 Attention，参数投影与残差依赖仍须按原顺序完成。为减少传输 Q/K/V，可以连同输入移动 QKV 投影参数，但这把通信改成输入、参数与输出的联合账单，并不等于无状态或零开销。配合两路 FILO 时，保留 Attention 所需状态、重算较便宜的前后算子，再分块执行 MLP 以减轻碎片；存活状态仍随 micro-batch 数增长，调度整除条件、同一步梯度提交与真实峰值缓冲都要核验。[受限长序列训练对照](https://arxiv.org/html/2507.00394v1)中，短序列或较慢互联不能完全覆盖新增通信，重算也会降低吞吐；合成定长、随 stage 扩大的 global batch 与少量计时迭代不证明全程收敛或任意规模收益。只有依赖、质量和总通信/重算成本通过真实 workload 验收才采用该分支，否则保留整层 GPipe/1F1B 与原 checkpointing。<!-- source-family:SF-2025-ARXIV-2507-00394 -->

## 1F1B：缩短 Activation Lifetime

One-Forward-One-Backward 在 warm-up 后交替执行 forward 与 backward：

```text
warm-up forwards
-> steady state: 1F1B
-> drain backwards
```

较早 micro-batch 的 backward 可以更早开始，因此同时存活的 activations 通常少于 all-forward/all-backward schedule。

1F1B 没有消除 pipeline dependency 或所有 bubble。Schedule 还必须保证同一 optimizer step 内参数版本一致；同步训练通常在全部 micro-batches 完成后更新。允许跨 batch 异步更新的 pipeline 方法需要 weight stashing 或处理 stale parameters，属于不同算法假设。

序列长度差异还可在不切断样本身份的前提下进入1F1B：将超长因果序列切成有前后依赖的token块，把短序列按容量打包，再按stage选择保留哪些块内激活、哪些在反向重算。[InfiniPipe的受限v1](https://arxiv.org/html/2509.21275v1)用这一分工联合选择切片与重算，但长序列的后块仍依赖前块K/V，反向对前块的dKV也有自己的回收边界，checkpoint并未取消这些跨块状态；packing还必须保持各原样本的mask、位置与target归属。相似块数分组可减少局部等待，却增加多次填充/排空和规划开销，不能由受限cost model的最优解批准所有硬件或在线形状。样本/有效token的loss与梯度权重、RNG及最终optimizer提交应另作一致性验收，短程吞吐对照不证明同SGD或相同收敛。CPU规划、profile、打包、所有K/V与dKV驻留和传输、重算与独立质量回归均计费；依赖、容量或净收益不合时，保留完整样本的GPipe/1F1B、固定packing与较简单checkpoint，而不以更多切片默认获得免费并行。

<!-- source-family:SF-2025-ARXIV-2509-21275 -->

当网络混合dense、MoE与MTP模块时，stage balance也不能只数Transformer层：MTP中的transformer计算与vocabulary loss可能有不同成本，可拆成独立调度单位，让不同VPP stage分配不同数量甚至零个普通层，并只重算较合算的MTP部分。这样改的是同步1F1B内部的partition和activation lifetime，不是去掉参数版本边界。[Ling 2.0的受限报告](https://arxiv.org/html/2510.22115v1#S5.SS2)支持这一异构分区，但单MoE stage对routing imbalance更敏感，增加VPP也未必有净收益。应从真实forward/backward、loss与通信profile共同选择分区，并校验同一步loss/梯度、低精度scale和重算状态；FP8减的是具体张量/缓存成本，不能把active参数少直接当吞吐快。Profile、调度粒度、驻留、通信与收敛回归均付费；不均衡、显存或净吞吐失配时，保留较粗且已验的1F1B分区与完整重算，不把局部40%提升外推成任意模型/硬件的保证。
<!-- source-family:SF-2025-ARXIV-2510-22115 -->

### Split-Backward 与低精度状态：Schedule 之外还有执行合同

普通 1F1B 将一个 micro-batch 的 backward 视为相对完整、按栈回收的动作；在 eager 执行下，这让 activation lifetime 与依赖次序较容易追踪。若为了填补空隙，把反向拆成尽早传播的输入梯度 `dI` 和可延后的权重梯度 `dW`，再以捕获图复用固定地址，逻辑 micro-batch 与物理 buffer 就不再天然一一对应。低精度训练还持有 `amax` 历史、scale、量化权重缓存等不在显式 tensor 边上的可变状态；单一顺序 token 无法证明所保留任务的身份与版本，可能错绑或过早释放 tape、错序或重复更新 scaling state，或在 optimizer 提交后消费旧缓存。

因此这类 runtime 需要把四个合同分开：低精度 scale 更新的顺序；保留任务的逻辑身份与可重用物理槽的世代；参数提交版本与量化缓存版本；调用 stream 进入和离开捕获图的双向完成边界。`dI` 留下 `dW` 任务时，tape 仍归该 micro-batch 的逻辑身份所有，直到两类 consumer 均完成才可释放；optimizer commit 后旧权重缓存不能借相同地址冒充新版本。Checkpoint 保存持久数值状态，并在安静的更新边界重建进程内 graph、event 与槽位，而不是序列化旧地址。这样把吞吐优化从隐含栈次序变成可验证的状态转移，代价是世代检查、预留 buffer、额外显存和捕获 setup；静态 scale、即时 `dW` 或开销并非 launch 主导的 workload，仍可用更简单的 eager/full-backward 路径。

一项 exact-v1 实验在单节点 H800 PCIe / RTX 5880 Ada、短序列 `seq=256`、`microbatch=1` 的细粒度场景演示这种组合合同，并报告额外峰值显存与 setup 成本。其完整 step 收益混合了 split/full-backward、捕获与 gradient placement 等变化；只有局部消融能隔离其中一项，不能外推成“CUDA Graph 单项普遍加速”或长序列、多节点的训练结论。论文描述了实现和附属报告，但本次未核实可访问的代码 artifact，亦未独立复现。

上述 split-backward 仍可保持同步 optimizer step；下一节讨论跨更新边界的异步参数版本问题。

<!-- source-family:SF-2026-ARXIV-2609-23536 -->

## 异步 Pipeline：去掉 Bubble 会把成本移到参数版本

同步 GPipe / 1F1B 用 idle time 换取清晰的 step boundary：同一 logical step 的
micro-batches 看到可解释的参数版本。异步 schedule 让 stages 不等待整条 pipeline
完成便继续推进，可以缩小 fill/drain bubble，却使 forward、backward 与 optimizer
update 不再天然属于同一参数快照。

技术演进不应写成“异步取代同步”，而应保留约束迁移：

```text
synchronous GPipe / 1F1B
  -> 参数版本与恢复语义清晰
  -> 付出 fill / drain bubble

original PipeDream-style async
  -> stages 持续推进
  -> delay 随 stage / schedule 变化，需 weight stashing

constant one-step delay
  -> 把 variable staleness 约束为固定延迟
  -> 优化误差仍取决于 optimizer dynamics

optimizer-aware update + update-level correction
  -> 用前后两次 update 的差值补偿延迟
  -> 增加额外 model-sized state、噪声与 checkpoint 语义
```

2026 年的一项实验工作在 PipeDream-2BW 的固定一步 delay 下比较多种 optimizer，
观察到不同 optimizer 对 staleness 的敏感性明显不同，并提出 update-level
Error-Feedback correction。作者在 10B MoE、200B training tokens 的单一大规模设定中
报告与同步 baseline 相同的最终 validation loss；但论文没有给出端到端 wall-clock
实测，吞吐部分依赖通信完全重叠的 schedule model，而且更大 token budget、更多
模型结构与故障恢复仍未验证。

因此工程判断必须同时包含：

```text
schedule
x optimizer and its state
x correction state
x weight-version ownership
x checkpoint / replay boundary
x measured end-to-end throughput
```

当 bubble 的真实成本不高，或 reproducibility、恢复简单性和现有 runtime 成熟度更重要时，
同步 1F1B 仍是合理基线。只有固定 delay、optimizer 稳定性和端到端收益都经过目标 workload
验证后，异步分支才值得承担新增状态。

### 有界异步用多条反向流水填 Bubble，但不取消 Update Boundary

同步 1F1B 以 bubble 换来版本清楚，完全异步则可能让 forward 与 backward 相隔任意多个参数版本。一个中间分支
是把第一 stage 的 forward 限制在其 backward 之前最多领先两个 micro-batches，同时交错多条 reverse pipeline
填补空隙；所有参与本轮 gradient accumulation 的 micro-batches 完成后，optimizer 才提交一次 update。Scheduler
拥有多方向依赖与 readiness，optimizer 拥有参数提交边界，micro-batch receipt 必须记录所见版本，利用率不能通过
模糊 weight ownership 获得。

这种有界异步可在论文设置中减少 bubble 并保持收敛，但会增加多 pipeline 状态、activation queue、调度证明与故障
恢复复杂度；模型深度、网络拓扑或执行抖动变化时，两步上界和收益都可能失效。需要严格复现、内存余量小或异常
版本出现时，应回退同步 1F1B。exact-v1 只支持论文披露的 GPT/BERT、硬件、训练预算和附录 schedule，不证明任意
pipeline 拓扑都能得到相同利用率或收敛行为。

<!-- source-family:SF-2026-ARXIV-2605-29664 -->

### Runtime Variability 下由 Readiness 取得 Dispatch Authority

静态 1F1B 等 schedule 在设备同质、执行时间稳定时开销低且容易证明 bubble；runtime jitter、straggler 或动态 shape 出现后，计划时间不再等于任务真的可运行。readiness-driven runtime 让依赖已满足、buffer 已就绪的 micro-batch stage 进入 ready set，再由 dispatcher 选择执行，同时保留静态 schedule 作为正常路径与 fallback。

它可以绕开暂时阻塞并提高韧性，却引入 ready-state bookkeeping、额外队列、内存峰值和可能的公平性/确定性问题；错误 readiness 会破坏依赖或覆盖 activation。变异很小或严格复现优先时，静态计划仍更合适。exact-v1 只支持其披露 pipeline、variability injection、模型与硬件，不证明任意并行拓扑都降低 step tail 或保持同等内存上界。

<!-- source-family:SF-2026-ARXIV-2605-18750 -->

## Interleaving 为什么引入 Virtual Stages

若一个 physical device 只持有一个连续 stage，`p` 受设备数限制。Interleaved schedule 让一个 device 持有多个 non-contiguous model chunks / virtual stages：

```text
GPU 0: chunk 0, chunk 4
GPU 1: chunk 1, chunk 5
...
```

更细 chunks 可以缩短某些 bubble 并改善不均匀层分配，但会增加：

- Stage transitions 和 point-to-point messages。
- Schedule state machine 复杂度。
- Activation queues 与 chunk identity。
- Checkpoint layer-to-rank mapping。

Interleaving 不是免费把 bubble 归零；收益依赖 micro-batch、virtual stage 数和 communication/computation 比例。

## Boundary Communication 在传什么

若 stage boundary hidden states shape 为：

```text
[b,T,d_model]
```

Forward 发送 activations，backward 发送同 shape 的 gradients。每个 micro-batch、每个 boundary 都会发生一次方向相反的 point-to-point transfer。

Boundary bytes 取决于 dtype、sequence、micro-batch 和 partition location。将 boundary 放在特别大的 activation tensor 后面，可能让 PP communication 远高于按 layer 数平均的预期。

通信可以和相邻 stage compute 重叠，但 send/recv ordering 必须一致，否则容易 deadlock。

第 36 章的五层模型在这里可以直接用于定位：activation/gradient transfer 是语义，pipeline schedule 决定 message ordering，communication runtime 负责 send/recv 与 completion，transport 和 topology 决定实际路径。只看到 network bandwidth，无法解释 schedule ordering 或 buffer lifetime 导致的等待。

### 跨地域 Pipeline 需要同时调度路径、优先级与成本

单一机房内，固定 stage mapping 加局部带宽估计通常足够；跨地域链路的带宽、价格与故障域不同，schedule ordering 不能再与 transport path 分开。Pipeline control owner 需要联合持有 micro-batch priority、可用链路、路径成本与 completion state，并在带宽变化时重新分配。这样可减少远距离 bubble 与账单失控，代价是在线 pathfinding、控制开销和更大的 failure surface；预测失准或控制器故障时，应回退到静态安全路径或单区域执行。exact-v1 只支持 BACE-Pipe 的模拟器与 trace 条件，不证明任意云际网络或真实故障下的收益。<!-- source-family:SF-2026-ARXIV-2605-25375 -->

跨域延迟还可用额外在途micro-batch隐藏，而不只改网络路径：在同步1F1B中增加warmup forward，并调整依赖和非阻塞通信，使后续计算覆盖较长传输。[受限跨机房流水分支](https://arxiv.org/pdf/2510.12064v1)用更多activation驻留换重叠，增加量受HBM、micro-batch和原step提交边界共同约束，不能让通信未完成的状态提前消费。有限三机房910B/OTN/PFC条件下未见重传，不授任意WAN同可靠或光网必需；bubble下降也不等相同比例iteration加速。搜索sequence length即使固定total tokens仍会改变训练样本/上下文语义，模型尺寸口径与未披精度不能由系统倍率补齐。全部warmup/激活、profile/配置搜索、通信和独立训练质量均计费；容量、可靠传输或净step收益不合时保普通1F1B、较少在途与单区域执行，不由更多重叠批准同训练语义、零额外内存或跨域SLO。

<!-- source-family:SF-2025-ARXIV-2510-12064 -->

### 跨层 KV 共享会改变 Pipeline 的真实 Stage Cost

按层数或静态 FLOPs 切 stage，在每层计算同构时合理；若模型引入 tail-first cross-layer KV sharing，后层复用前层状态会改变 per-layer Attention FLOPs、activation/KV boundary 与 memory pressure。Partitioner 必须对新 checkpoint 的依赖图重新 profile，再决定 stage placement；它不能把共享当作免费的 runtime cache。该分支以模型结构改动和跨层耦合换取更均衡 pipeline，既有 checkpoint 不可改或通信超过节省时，普通 layer-local KV 仍成立。`arXiv:2608.15943v1` 的 KV-Pipe 证据限作者模型与训练/推理设置，不证明通用 PP 加速。

<!-- source-family:SF-2026-ARXIV-2608-15943 -->

## Stage Balance 比平均 Layer 数更重要

不同 layers 成本可能不同：

- Embedding 与 vocabulary projection。
- Dense Attention 与 sliding/local Attention。
- Dense MLP 与 MoE。
- 不同 hidden size 或 multimodal blocks。
- Activation recomputation policy。

Pipeline steady-state throughput 由最慢 stage 限制。应共同平衡：

```text
forward time
backward time
parameter / optimizer memory
activation peak
boundary bytes
```

平均切 `L/p` 层只是初始估算。实际 partition 需要 profile per-layer cost，并为 embedding/loss 等特殊模块留出预算。

把层切细会扩大可平衡的stage组合，也会让逐候选测量与搜索成本迅速增加，因此profile粒度和执行粒度不必始终相同。可以先保留重复module与非重复部分的结构，再对候选连续stage和同构device mesh去除重复测量，复用等价stage–mesh的计算、边界通信与memory画像，让细粒度partition不必为每处重复结构重新付一次准备费。等价仍取决于算子/shape、精度、重算和设备/链路条件；结构同名不授权跨环境复用，最终计划也须同时检查额外在途micro-batches的activation峰值和慢链路暴露时间。[受限v1设计](https://arxiv.org/html/2509.24859v1#S5)支持这条准备成本分工，但其warmup与DP公式内部不齐，不能据此签发完整最优调度；所报异构环境还包含以A100降频限存模拟V100，局部step计时不证明原生混合卡或长程收敛。Profile、剪枝/搜索、编译、重算与状态驻留都计费；结构、画像或净收益失效时，重新测量或保留较粗切层及成熟1F1B，而不是把复用称为零成本。

<!-- source-family:SF-2025-ARXIV-2509-24859 -->

即使GPU型号相同，静态profile也不等于持续运行时的stage成本：进排风位置、功率和温度导致的降频，可让原本等量的stage成为慢侧。可以先按实测热态分组，再把较重模块或少量层移给较冷的stage，但切层是离散的，降低温差不等于缩短完整step。[有限训练对照](https://arxiv.org/html/2509.10371v1#S6)在TP4、每节点两个stage且关闭DP时，80层/4stage的19/21分配改善效率，96层/8stage的11/13分配却在缩小温差时降低效率；这不是同SKU一律应非均匀切层的结论。应把完整step、暴露通信、memory峰值与稳定热态共同复测，计入telemetry、重排和状态迁移成本；原实验不证明在线重配置、硬件寿命或Serving SLO。热态变化、粗粒度切层或净收益不合时，保留固定已验分区与较简单placement，把设备健康/机箱散热交给平台处理，不以更均匀的温度替代训练吞吐和正确性验收。

<!-- source-family:SF-2025-ARXIV-2509-10371 -->

样本分配也可能制造等待，即使每个 micro-batch 的 packed total length 相同。EoD 阻断跨 document attention 后，可见 token 对的数量随内部 document 长度组成变化；若 backend 真正消费这种 block/sparse 可见性，长文档较多的样本会比相同 shape 的短文档组合更贵，dense mask 本身却不保证计算量减少。可按 subsequence 长度估计成本，重新分配完整样本以平衡各 rank，而不改全局训练人口、EoD 语义或 optimizer accumulation 提交。[有限训练说明](https://arxiv.org/html/2512.24157v1)只支持这个 attention-aware 调度入口，没有隔离该项的定量收益；统计、重排和 backend 校准仍付费。profile 未显示差异或重排成本更高时，保留固定 token 分配；layer partition、router balance 和运行时 readiness 仍各自负责原有压力。<!-- source-family:SF-2026-ARXIV-2512-24157 -->

同构 profile 选出的 expert 并行度，也不一定能直接带入异构 pipeline。可在各设备和链路上先测 dense/expert 计算、dispatch/combine、router 负载及 activation/optimizer 容量，再让 stage 层数、设备分配、expert tensor/parallel 度与 recompute 共同决定候选 step 计划。较快 stage 不必与较慢 stage 分同样层数，较大 expert group 也可能让跨类型通信抵消计算节省；成本模型应区分已重叠与暴露通信，不能重复加总。最终 layer/device/process mesh 与重计算策略必须一起 materialize，planner 只提供候选，不改变训练 batch、routing 语义或完整 step 提交。

这是校准窗口内的离线分支，不是在线适应保证。HAPMoE 的受限异构 MoE 对照支持联合计划与非均匀分区，却用 warmup、memory/router instrumentation 和搜索换较少 steady-state 等待；pruning 也可能错过模型外候选。路由持续改变、网络争用或设备失效会使原 profile 过期，短 search time 不能消去重新校准成本，作者没有验证动态重配置。收益不足或状态无法一致 materialize 时，保留同构子组、固定 EP 与成熟 1F1B，在实际 step time、峰值 memory 和任务/收敛合同上重新验收，而不是用低预测误差证明生产最优。[必要机制与反证](https://arxiv.org/html/2609.39350v1)。<!-- source-family:SF-2026-ARXIV-2609-39350 -->

还不必先假定所有可用GPU都参与：跨地域异构环境中，把active subset、连续层划分和stage顺序一起搜索，可能比在固定全员集合内平衡更合理；额外慢卡或弱链路会增加等待，较低active功率也未必降低整轮能耗。[受限联合规划](https://arxiv.org/html/2610.26178v1#S4)以profiled compute/双向链路、memory近似和idle/active功率提出time–energy候选，最优只相对于所选模型与搜索域。真实短程对照的基线强制全卡，不能把差额全归搜索器；未选设备、host、网络和机房成本也不能由active-pipeline能量自动消失。Profiling、subset搜索、部署/恢复和独立step/质量验收都付费；模型过期、状态容量或净费用不合时，保留同构子组、固定stage与成熟1F1B，不由少用卡或低预测代价认证长期收敛与全系统节能。<!-- source-family:SF-2026-ARXIV-2610-26178 -->

层数的离散粒度仍可能无法平衡多条完整 pipeline 副本，此时可让副本使用不同 local batch，再联合调整 stage；micro-batch 数成为比切层更细的负载旋钮。不同 TP/DP 切分的梯度必须按真实参数坐标分块、重组与融合，不能按物理 buffer 形状直接 AllReduce；不同样本数的权重、总 batch 和 accumulation 提交是另须验证的统计合同。[受限异构训练研究](https://arxiv.org/html/2610.22035v1)使用三阶段 heuristic 而非全局最优，核心描述未闭合所有不等 batch 的归一与 overshoot，短程 training loss 接近也不证明 exact SGD 或 heldout 等价。Profiling、搜索、重组通信和重算都付费；收益或统计身份未验收时，同构子组、统一 batch 与既有 1F1B 仍更稳妥。<!-- source-family:SF-2026-ARXIV-2610-22035 -->

## 一个不平衡小例子

假设 4 stages 的单 micro-batch compute time：

```text
[10, 10, 18, 10] ms
```

即使 fill/drain bubble 很小，steady-state cadence 仍受 18 ms stage 限制。其他 stages 每轮可能等待约 8 ms。

将一个 expensive layer 从 Stage 3 移到 Stage 4，若变成：

```text
[10, 10, 14, 14] ms
```

吞吐才真正改善。这个例子说明 schedule optimization 不能替代 partition balance。

## Tied Weights 与跨 Stage 依赖

Input embedding 和 output projection 可能 weight-tied，却位于第一和最后 stage。系统需要在初始化、gradient reduction、optimizer step 和 checkpoint 中维持同一逻辑参数。

类似的跨 stage shared parameters、skip connections 或 multimodal branches 都会破坏简单链式假设。Pipeline framework 必须显式表达这些依赖，不能仅按 layer index 推断。

## PP、TP 与 DP 怎样组合

常见 rank grid：

```text
TP inside each stage
PP across stage depth
DP across full pipeline replicas
```

一个完整 model replica 由 `TP * PP` ranks 组成；`D` 组 replicas 再处理不同 data。Global batch 仍由 `B_micro`、`m` 和 `D` 定义。

TP collective 高频，常放节点内；PP boundary messages 较少，常跨节点。这是经验起点，具体 topology 和 activation bytes 仍需 profile。

## Pipeline Parallel 没有解决什么

- 单个 layer 太大：需要 TP。
- DP optimizer-state duplication：需要 ZeRO/FSDP。
- 长 sequence activation/Attention：可能需要 CP/recompute。
- MoE expert placement：需要 EP。
- Data input 或 storage bottleneck：PP 不直接处理。

PP 也不会自动提高模型质量。它只改变同一 forward/backward graph 的设备执行方式。

## Checkpoint 与 Failure

每个 stage 只持有部分 layers。Checkpoint manifest 必须记录 layer/chunk 到 rank 的 global mapping，并在 PP degree 改变时支持 reshard。

任一 stage failure 都会让整个 pipeline 停止。部分 stage 的最新 tensors 不能与其他 stage 的旧 step 混合。异步 checkpoint 还要保证 snapshot 对所有 stages 和 optimizer state 属于同一 logical step。

固定stage映射的全线停止，也可在每个stage仍有可信参数副本时缩小为局部流恢复：为microbatch保留源/目标、实际经过的路径与所用activation和gradient，前向失联时另选下一stage的存活节点，反向缺段时从仍存活的前驱重做所缺forward，再接已保存的下游gradient。[受限flow分支](https://arxiv.org/html/2509.21221v1#S5)据此避免总是重做整条pipeline，但超时只形成故障怀疑，新节点必须取得同一stage/迭代的参数，聚合与下一轮接纳仍需共同更新边界；这些约束不等于已经证明任意消息重复或丢失下的exactly-once与同SGD轨迹。它用冗余stage容量、路径/中间态驻留、探测协调与部分重算换较小停顿，局部路由cost也只是代理，不提供全局最优或真实WAN预算保证。任一stage已无可信副本、参数/批次身份不合或恢复支持不足时，仍应停止并回committed checkpoint；不把fail-stop恢复延伸为恶意worker安全或任意故障可继续。

<!-- source-family:SF-2025-ARXIV-2509-21221 -->

Stage 仍在线也不等于计算正确：不可信 worker 可以返回形状合法却被扰动的 activation 或 gradient。一个受限分支在 forward/backward 的 stage 边界设置可信 verifier，以诚实 warm-up 建立统计基线，再用 EMA 与幅度、范数、符号或分布变化形成异常 sensor。被标记的样本不更新基线；上游异常可能污染后续 stage，因而 cascade 处理应暂停受污染统计的更新，不能把每个下游报警都归因为该 worker 作恶。它补充的是边界观测与隔离反馈，不改变 pipeline 的依赖语义。

这个受限 sensor 路径要求首尾 stage 可信、每个 stage 的恶意 worker 少于一半，并以诚实 warm-up 建立基线；还要定义阈值及 worker 归责策略。漂移与共谋会破坏这些前提，某些梯度符号攻击在作者实验中甚至没有被召回。隔离前应保留 stage、step、方向与上游事件关联，必要时重新计算或回退可信 worker，而不是由一次异常直接认证训练正确。[SENTINEL v1 §2–3、§5 Tables 1–3](https://arxiv.org/html/2603.03592v1)支持这个受限分支及其漏检，不提供完整密码学验证或任意去中心化训练的安全保证。<!-- source-family:SF-2026-ARXIV-2603-03592 -->

## 工程验证

### Schedule Abstraction 要先证明依赖合法，再比较 Bubble

手工枚举 1F1B/interleaving 在拓扑固定时清楚；stage、micro-batch 与资源约束组合增多后，可用统一 schedule representation 生成候选，并以依赖公式、表格或 simulator 检查合法性，再比较 bubble、memory 和 communication。收益是扩大设计空间，代价是 abstraction/simulator fidelity；生产发布仍须真实 workload 验证，简单拓扑保留手写 schedule。<!-- source-family:SF-2026-ARXIV-2605-24006 --> exact-v1 §III–IV 支持 schedule abstraction，§V simulator 结果不证明真实集群收益。

当流水线跨越高延迟或共享带宽的链路时，合法的计算顺序还不足以决定何时能继续执行：多个待发activation/gradient会竞争同一传输窗口，接收尚未就绪也会把等待传回发送端。可把计算块、消息的链路占用与到达延迟一起放进依赖调度，再将所得顺序降成匹配的非阻塞send/recv计划；输入梯度与权重梯度分离时，DP同步还须等待对应累积人口的权重梯度完成，ZeRO参数恢复则必须早于消费它的forward。[一条受限跨数据中心分支](https://arxiv.org/html/2507.00217v1)用约束求解或分块贪心选择计划，再提前发布匹配receive以减轻rendezvous等待，但模型中的带宽窗口与profile只给候选，不证明真实链路没有排队、控制握手或故障。其同质集群延迟注入、最小迭代时间和放宽batch/activation预算的结果，也不能签发异构WAN、完整训练收敛或生产最优；更多在途任务以buffer和存活状态换重叠，重计算未必划算。Profiling、求解、通信编排、额外buffer及重校准均计费；网络/内存估计过期或消息依赖无法验证时，保留固定1F1B/原通信次序、保守预算与完整step检查点恢复，而不以较少bubble越过参数版本和实际完成边界。
<!-- source-family:SF-2025-ARXIV-2507-00217 -->

Diffusion backbone 的 skip connection 会让“按连续层平均切分”产生跨 stage 回传：计算量看似均匀，通信和 activation lifetime 却被隐藏依赖放大。Planner 应先把 skip-connected layers 的 colocate constraint 纳入依赖图，再联合求解 partition 与 schedule，最后用真实 profile 校准 tuner。依赖合法性由 graph owner 判断，性能模型只负责排序候选，不能为了降低 bubble 改写计算图语义。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-25451:start -->
多模态训练还会同时包含 encoder、LLM 与 generator；若把三者简单串行，非 LLM 组件的 activation lifetime 随 micro-batch 数增长。一个 nested pipeline 分支把 encoder/generator 工作嵌入 LLM stage flow，用全局 operator table 保留 micro-batch dependency 和参数版本，使两类 activation memory 保持有界。Scheduler 可以生成计划，executor 仍必须拒绝违反数据依赖的重叠。

它以 readiness tracking、stage balance、边界通信和更复杂恢复换取显存；估时或依赖错误会覆盖 activation、制造新 bubble，甚至让 micro-batch 看到不一致权重。验证失败时应回退顺序 encoder→LLM→generator 或已经证明合法的 GPipe/1F1B。当前 artifact 未披露完整硬件、精度、拓扑和 tail SLO，不能把作者加速比写成通用结论。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-25451:end -->

强制 colocate 可能反过来造成 compute imbalance，ILP/DP 求解成本也会随模型和拓扑增长。作者结果只绑定受测 diffusion transformer 与集群配置；普通 transformer 或高速互联下，连续切分与手工 schedule 仍可能更便宜、更易验证。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.19163 -->

至少测量：

- Per-stage forward/backward time 与 idle fraction。
- Warm-up/steady/drain timeline。
- Outstanding activations 和 peak memory。
- Boundary send/recv bytes 与 duration。
- Micro-batch size 对 GEMM efficiency 的影响。
- Pipeline loss 与未切分 reference 的短程一致性。
- Same-layout resume 和 PP reshard/convert。

单一 aggregate GPU utilization 无法定位是 bubble、stage imbalance 还是 communication wait。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-07881:start -->
异步 Pipeline Parallel 允许相邻 stage 在有界 weight inconsistency 下继续推进，以减少同步 bubble；runtime 必须记录每个 microbatch 读取的 weight version，并用 staleness bound 决定接受、等待或回退同步 schedule。它用更复杂的版本状态和收敛风险换吞吐，不能把局部 bubble 降低外推成端到端训练收益。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-07881:end -->

## Pipeline Boundary 不一定只传 Activation

线性递归或 attention–recurrence hybrid 模型把长序列切成 chunk 后，还必须显式传播 recurrence boundary state 及其 gradient。chunk 长度因此同时影响计算平衡、state lifetime 和依赖深度；均匀切分可能让 attention 与 recurrence 阶段失衡。该分支扩展了传统 stage pipeline，但收益绑定模型结构和序列长度。

<!-- source-family: arxiv:2608.06838v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: sequence-pipeline-recurrence-boundary-state -->

另一条实验分支用局部目标解除全局 backprop update locking，使多个 chunk 并发更新。它减少等待，却引入 objective mismatch、跨 chunk representation drift 和新的 recovery state；大规模精确训练仍以全局 BP 为基线。只有局部目标经过收敛与下游验证时，才把并发更新当可接受近似。

<!-- source-family: arxiv:2608.07974v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: local-objective-unlocks-pipeline-updates -->

## 本章在知识树中的位置

```text
deep-model capacity bottleneck
-> layer / chunk partition
-> micro-batch schedule
-> Pipeline Parallel
-> TP x PP x DP runtime
-> Megatron process groups
```

本章只负责 layer depth 与 schedule。第 39 章转向 DP state redundancy，第 40 章再把 PP 与 TP、DP、CP、EP 组合。

在 Scheduling 横线上，本章按训练 dependency graph 分配 micro-batch execution slots；第 46、56 章把相同的有限执行机会问题改写为在线 token admission 与 iteration scheduling。两者属于 scheduling principle reuse，但训练 bubble 与在线 SLO 不是同一个目标函数。

## 从机制演进到系统设计

Pipeline Parallel 从固定 stage 与同步 microbatch schedule 出发，因为它最容易保持 forward/backward 依赖；层成本、异构链路或动态 workload 变化后，stage balance、schedule 和 activation movement 需要联合优化。runtime 可以重排 microbatch，却不能改变 global batch、loss weighting 或 tied-weight consistency。

更动态的 pipeline 降低 bubble，却增加 schedule state、跨 stage failure、activation pressure 和可复现性成本。模型较小、stage 稳定或通信主导时，固定 1F1B/GPipe 仍更可靠；任何 source-specific schedule 都必须在相同训练语义和收敛合同下比较。

## 自检问题

1. Layer partition 为什么解决 capacity 却不自动解决 utilization？
2. `B_global=B_micro*m*D` 中 `m` 为什么不是 optimizer steps？
3. `p=4,m=8` 与 `m=32` 的理想 bubble 有何差异？
4. GPipe 与 1F1B 怎样改变 activation lifetime？
5. Interleaving 为什么会增加 messages 和 schedule state？
6. Stage boundary 的 activation/gradient shape 怎样决定通信？
7. 为什么平均 layer 数不能保证 stage balance？
8. Tied embedding 为什么产生跨 stage 状态约束？
9. PP、TP 和 ZeRO 分别没有解决对方的什么问题？
10. 为什么 pipeline checkpoint 必须记录 global layer mapping？

## 小结

Pipeline Parallel 沿模型深度分散 layers 和训练状态，再用 micro-batches 让多个 stages 并行工作。Bubble、activation lifetime、boundary communication、stage imbalance 与 runtime variability 决定 capacity 收益能否转化为吞吐。

GPipe、1F1B 与 interleaving 是不同静态 schedule 选择；readiness-driven dispatch 则是在变异出现时接管有限调度权的分支。它们改变时间线、memory 与 communication，并需要 checkpoint、dependency 和 parameter-version semantics 配套。

## Review notes

- `SF-2025-ARXIV-2510-12064` — Herschel，Daily2025-10-16补Oct15；消费Cicero R18 official exact-v1 PDF II-B/III/IV首次必要，2+2+2=6，仅extra warmup/改1F1B/非阻塞通信与activation容量差额。保64×910B/TP8PP8/三DC/OTN-PFC、有限无重传非任意WAN、固定tokens改seq非同语义、72B/70B冲突/precision未披及全费，不授bubble等比例step或通用可靠。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

- `SF-2025-ARXIV-2509-24859` — Singer，Daily2025-10-01补Sep30；[HAPT exact-v1](https://arxiv.org/html/2509.24859v1)§3–6/式1–22与直接配置/脚注。R3原2+2+2=6日期/准入、R8有限必要有效；只重复module/stage–mesh画像复用→细粒度partition准备成本差额，不授式2/10–11不齐的warmup、DP可执行recipe或精确全最优。保A100模拟V100、kernel/NIC不同、peakFLOPs归一与memory差、3Gbps反侧及profile1248s/search133s和全费；未核曲线像素/代码/复现。原三项R10整体PRE通过，root本轮独立fresh新窄授后A17已逐字真实保存并完整自读全部新增/完整两侧/binding及本人注；Sartre R15本项唯一actualPOST通过，本段整合I2生效、指定正文/本人注窄位释放，仅同步既成行政态，不第三Source/PRE/POST或授DAY。

- `SF-2025-ARXIV-2509-21275` — Socrates，Daily2025-09-27补Sep26；[InfiniPipe/EPP exact-v1](https://arxiv.org/html/2509.21275v1) S3–6直接机制/对照及必要限制，2+2+2=6。root首备→作者38唯一另一角色实际采用；仅token切片/packing与stage-chunk重算、K/V和dKV寿命及统计提交分责，不继承后来Concertina/DPP。保受限costmodel/稳态bubble假设、baseline配置/质量未测与全费，不授exactSGD/全局最优/生产SLO。未核实现、全部图像素或复现。作者52原三项经Helmholtz R47整体纯PRE，root本轮fresh独立新窄授；原技术稿真实保存并完整自读新增/完整两侧binding及本人注，Helmholtz R51本项唯一actualPOST通过，I11生效且指定窄位释放；本尾仅行政同步既成，不第三Source/PRE/POST或授DAY。

- `SF-2025-ARXIV-2509-21221` — Socrates，Daily2025-09-27补Sep26；[GWTF exact-v1](https://arxiv.org/html/2509.21221v1) III–VII有限必要，2+2+2=6。仅可信stage副本/路径中间态下局部flow补算与同迭代参数资格；保timeout非truth、每stage至少一活、exactly-once/Byzantine未证、E1 costproxy与1024/18配置冲突、5GPU模拟地理人口/反退及全控制/恢复费。作者14→R15必要一次实际采用通过；作者22原三项/完整侧组经R21整体纯PRE通过，root本轮fresh独立新窄授后原技术稿真实保存，writer已完整顺读新增/直接两侧binding及本人注/两侧，Helmholtz R25本项唯一actualPOST已通过，I4生效且指定窄位即时释放；本尾仅行政同步既成，不授日级完成。未核图像素/代码/真实WAN或复现。

- `SF-2026-ARXIV-2610-26178` — Daily2026-10-21，exact-v1必要域与完整反侧见本日AUTHOR Resume R-A7；R86必要Source/actual owner/完整PRE通过，无代码核验/复现，实际POST见本日REVIEW。

- `SF-2026-ARXIV-2610-21815` — Daily2026-10-17窗10-16；[v1](https://arxiv.org/html/2610.21815v1) §2–5/7.1–2/9–10，2+1+2=5。仅采固定服务纯forward fill/steady分离；不采一般overlap插值、生产日志验证PP或训练通用保证。必要Source/PRE：ORG_B S39，经root独核后保存；实际非作者写后复核通过（ORG_B S47）。未复现。
- `SF-2026-ARXIV-2610-22035` — 同窗；[v1](https://arxiv.org/html/2610.22035v1) §3–4/6–8及必要反侧，2+2+2=6。仅采不等localbatch/真实gradient坐标分责；保heuristic、GBS/样本权重未闭与全费。必要Source/PRE：ORG_B S38，经root独核后保存；实际非作者写后复核通过（ORG_B S47），未核实现/复现。

- `SF-2026-ARXIV-2603-03592`：[exact-v1](https://arxiv.org/html/2603.03592v1) §2–3、§5 Tables 1–3；Daily 2026-03-06。只采用可信边界 verifier、EMA/cascade 与统计 sensor 的失效面，不采用收敛定理或完整抗攻击保证。作者源/owner/邻接与实际写后检查完成；root 必要源、实际正文及邻接独立写后复核通过，未复现实验。

本轮 Review 保留 layer partition 与 bubble 主线，补齐 global batch、`p=4` 小例子、GPipe/1F1B/interleaving、boundary tensor、stage imbalance、tied weights 和 checkpoint mapping。多维并行组合留给第 40 章。

Primary-source 校验入口：

- Yanping Huang et al., "GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism", 2018: https://arxiv.org/abs/1811.06965
- Deepak Narayanan et al., "PipeDream: Generalized Pipeline Parallelism for DNN Training", 2018: https://arxiv.org/abs/1806.03377
- Deepak Narayanan et al., "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM", 2021: https://arxiv.org/abs/2104.04473
- Philip Zmushko et al., "One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining", arXiv v1, 2026: https://arxiv.org/abs/2606.30634

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-07881:start -->
- `SF-2026-ARXIV-2606-07881` — Daily `2026-06-06`；primary `arXiv:2606.07881v1`；Books review `books-review:SF-2026-ARXIV-2606-07881`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07881:end -->

- `SF-2026-ARXIV-2512-24157` — Daily `2026-01-02`；[TeleChat3-MoE exact-v1](https://arxiv.org/html/2512.24157v1) §4.2 L251–254。6分attention-aware EoD样本调度gap深入，仅采用同packed length异document-cost及样本分配，区别layer placement/dense mask；无该项独立量化消融，不采用整体MFU/PP收益归因或生产SLO。未运行代码；root必要原源/owner及实际正文、邻接与末注非作者写后复核通过。

- `SF-2026-ARXIV-2601-09026` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.09026v1) §3.1–3.2/4.1–4.2与AppB/C。6分近似层求解替代分支gap深入，采用MGRIT/coarse串行与parallel relaxation、inexact state/gradient及iteration/exactserial退路；N-ODE h/buffer改变模型，fine/coarse dropout一致，不授drop-in等价或通用sameaccuracy/speed。有限depth/device与GPU-scaled batch反侧在正文附近。root必要源/owner写前通过，root实际两段、前后与末注POST通过，锁释放；未运行artifact或复现。

- `SF-2025-ARXIV-2507-00394` — Daily2025-07-03补Jul2；[exact-v1](https://arxiv.org/html/2507.00394v1) §2–5必要机制/T1–3与§6具体对照限制，2+2+2=6；无参数attention与QKV参数/残差分责、FILO活跃人口与重算/通信反退gap深入。仅采用受限partition/schedule分支，不授全程收敛、任意规模或通用加速；未核图像全点、代码或复现。Boyle实际Source/当前owner及保存后完整两侧/本人注已读；root§12必要Source/PRE通过并授本位，§13已实际完整新增、GPipe/1F1B两侧、本人注及目标diff非writer POST通过，本项整合生效、窄位释放；仅同步既成事实，不授整日完成。

- `SF-2025-ARXIV-2507-00217` — Boyle，Daily2025-07-03补Jul2；[exact-v1](https://arxiv.org/html/2507.00217v1)§2–8、AppB/D.1/F必要，2+2+2=6/具体owner差额深入。只采用链路资源/到达依赖与实际收发编排分层；保同质GH200注入、64次取min、profile/控制握手假设、batch/activation/recompute和完整成本，不授真实WAN/SLO、所有表最优或端到端收敛。USENIX同题四作者只出版角色，未核全部图像/实现/复现；root§38已实际必要Source/6分/具体gap/逐字PRE通过并授本窄位；Boyle已按批准稿实际保存并完整self-read，root§40已实际完整新增/完整直接两侧/本人注及限定diff-check非writer POST通过，本指定窄位生效释放；仅同步既成事实，不授DAY。

- `SF-2025-ARXIV-2509-10371` — Carson，Daily2025-09-16补Sep15BJT；root首次必要准备，本人REPAIR31实际一次非准备者采用exact-v1 §3–8与A.2/A.5/A.6及直接图注，2+1+2=5。只采用同SKU热态×PP切层粒度及温差/效率相反结果，保TP4/每node两stage/DP关闭、联合改变/统计未披与完整费用；8K/800G仅projection、寿命与inference SLO未证。只核Zenodo元数据角色，未核/执行归档code/trace或复现；Zeno45原三项PRE通过，root本轮fresh授本精确位，作者已真实保存；Zeno55唯一完整nonwriter actualPOST通过，I6生效/位释放，未DAY。

- `SF-2025-ARXIV-2510-22115`：Daily2025-10-29补窗；精确v1必要支持/直接反侧已读，未核代码或复现。新差额为MTP Transformer/loss独立partition与选择性recompute，区别普通异构fill模型和split dI/dW状态；保routing不均衡反侧，不复制整体Ling配方。
