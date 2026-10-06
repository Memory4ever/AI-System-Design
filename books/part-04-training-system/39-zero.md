# 第39章 ZeRO

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-ZERO`
**Legacy Chapter:** Ch35
**Status:** Draft

**Roadmap Intent:** 切分优化器状态、梯度和参数，降低显存占用。

## 本章要回答的问题

第 36 章的 Data Parallel 已把 batch 分给多张 GPU，为什么每张卡仍保存几乎相同的 parameters、gradients 和 optimizer states？ZeRO Stage 1/2/3 分别消除哪类副本？参数何时 gather、梯度何时 reduce-scatter、更新后怎样恢复一致视图？

本章的核心判断是：**ZeRO 在 data-parallel domain 内分片原本重复的 model states，并在计算或更新需要时通常通过 collective 临时恢复正确视图。**更高 stage 扩大 memory savings，也把 parameter lifecycle、communication overlap 与 distributed checkpoint 带入关键路径。第 36 章定义通信的公共 cost model；本章关注 AllGather 与 ReduceScatter 怎样服务 parameter/gradient ownership lifecycle，而不是重新比较 Ring、Tree 或 backend。

本章使用 `P` 表示参数量，`D` 表示 data-parallel degree，`b_p`、`b_g`、`b_o` 分别表示每 parameter 的 parameter、gradient 和 optimizer-state bytes。

## 标准 Data Parallel 的冗余

标准 DP 每 rank 保存：

```text
parameters       P * b_p
gradients        P * b_g
optimizer states P * b_o
```

每卡 model-state memory：

```text
M_DP = P * (b_p + b_g + b_o)
```

不同 ranks 处理不同 samples，但在同步 update 前后持有语义相同的模型状态。这个复制保证实现简单，也造成显存冗余。

Activation、temporary workspace 和 communication buffers 不属于这个公式。ZeRO 的直接目标是 model states，不是所有训练 memory。

## Stage 1：只分片 Optimizer States

Stage 1 在 `D` 个 ranks 之间分配 parameter ownership。每个 rank 只为 owned parameters 保存 optimizer states 和执行更新：

```text
M_Z1 ~= P * (b_p + b_g + b_o/D)
```

Parameters 与 gradients 仍完整存在。Owned shard 更新后，需要让其他 ranks 获得更新后的完整 parameters，通常通过 AllGather 或等价同步。

Stage 1 适合 optimizer states 是主要压力、完整 parameters/gradients 仍可容纳的场景。

上述 `D` 分片公式默认被处理的参数在同一个 DP group 内等价复制。MoE 同时使用 Expert Parallelism 时，这个前提不再对所有参数相同：各 expert 只放在自己的 EP rank 上、跨 DP 复制；attention 等非 expert 参数则跨 DP 和 EP 都复制。若仍把所有 optimizer state 只按 DP 分片，非 expert state 会在 EP rank 之间保留多余副本。一个更精确的 owner 选择是按参数复制域分组：expert state 在 DP 维度分片，非 expert state 在 DP×EP 维度分片，更新和 checkpoint 都保存对应 process-group/参数身份，而不能把两组 shard 当成同一组 offset。

这条分支减少的是可复制的 optimizer state 与相关更新压力，不改变 expert dispatch、forward/backward 或 activation 的成本；它还增加参数分类、跨组同步与恢复时重新分片的复杂度。EP 未启用、非 expert state 占比很小或 group 管理成本占主导时，普通 ZeRO-1 更简单。Aurora 上的受限 MoE 实验报告 optimizer step 的改进并不等于端到端训练等比例加速，也不能移植成其他 GPU/网络拓扑的通用收益。<!-- source-family:SF-2026-ARXIV-2604-00785 -->

### 分片与低比特状态压缩是两条不同的轴

ZeRO-1减少副本数，低比特optimizer则减少每个副本的`b_o`；二者可以组合，但不能用更少bytes证明更新等价。固定8-bit在统计稳定时简单；层与训练阶段的敏感度变化后，一条分支周期性收集gradient RMS、离散度及二阶统计，相对全局EMA选择各层状态精度，再对一阶moment作分块线性量化、二阶moment作对数量化。这里调整的是optimizer state，不是learning rate；分布式owner还需一致地执行精度与编码转换。

动态精度把容量压力换成统计同步、重编码与累积误差，也可能在低精度中先损失信息，之后升位并不能恢复它。[STQuant的受限实验](https://arxiv.org/html/2604.06836v1)覆盖GPT-2、ViT/RoBERTa及四卡/单卡A800 FP16；去掉空间因素的消融反而以较高平均bit换来更低PPL，说明目标是质量—容量取舍，不是每个组件都改善质量。不能据此保证大规模多模态收敛、端到端吞吐、常数辅助内存或checkpoint恢复；统计不稳定时保留固定精度基线，编码与精度策略则随optimizer state一起保存。<!-- source-family:SF-2026-ARXIV-2604-06836 -->

### 低秩状态还需要保存坐标身份

减少副本数与减少每个状态的 bit 数，都没有处理 activation 随 batch 和序列增长的压力。另一条可组合但并非 ZeRO 自身的分支，是在线学习输入 activation 的低秩基：forward 仍使用完整输入，只为 backward 保存投影；由投影得到低秩 weight gradient 和 optimizer state，再把更新映回完整权重。这不是冻结 base 只训练 adapter，也不保证 backward 与完整训练等价。

基随训练变化后，旧 moment 不能直接沿用原坐标。一个实现用 Oja 更新并重正交化 basis，以新旧基的重叠运输一阶 moment；二阶 moment 只保存逐坐标统计，无法精确恢复全部 cross-coordinate covariance，因此需要近似运输。basis、rank、运输规则和 moment 共同构成训练状态，而不是可随意替换的压缩附件。它用投影、重正交化、统计运输和近似更新换取容量，rank 或 subspace learning rate 失配会损害质量；梯度不集中、漂移过快或质量回归失败时，保留完整 activation、recompute 及普通分片更可靠。[OASIS 的有限实验](https://arxiv.org/html/2604.09406v1)有低 rank 退步，不能把 exact forward 写成精确训练或大规模分布式收敛保证。<!-- source-family:SF-2026-ARXIV-2604-09406 -->

## Stage 2：进一步分片 Gradients

Stage 2 让 gradient aggregation 直接产生 owned gradient shards：

```text
ReduceScatter(local gradients)
-> each rank keeps gradients for owned parameters
```

理想 memory：

```text
M_Z2 ~= P * (b_p + (b_g + b_o)/D)
```

Parameters 仍在每 rank replicated。Optimizer update 完成后，需要同步更新后的 parameter shards。

Gradient bucket、accumulation boundary 和 reduce-scatter timing 会影响 peak memory 与 overlap。不能只看 steady-state shard size。

<!-- semantic-body-binding:SF-2026-BYTEDANCE-VEOMNI-PR-781:start -->
HSDP 还把 collective 拆成 shard dimension 与 replicated dimension。每个 accumulation micro-step 的 local gradient
仍需 reduce-scatter 到 shard owner；replica 间 all-reduce 则只需在 optimizer commit 前的最后一个 micro-step 完成。
因此 runtime 必须把 accumulation index、replica group 和 sum/mean convention 作为 final-boundary identity，不能把
“延后 replica 同步”误实现成两类 collective 一并跳过。

这条路径减少 replicated communication 的执行次数，却不减少 model-state memory，并新增 boundary/group state 与数值
等价验收。final micro-step、membership 或 reduction convention 错误会造成 silent gradient/update divergence；不能
证明等价时，应回退每个 micro-step 的完整 reduce-scatter + replica all-reduce。现有 evidence 只覆盖 VeOmni 披露的
Qwen3.5-35B-A3B、FSDP2/offload、EP=8、MBS=1、GBS=128 日志；硬件、节点数、重复方差和收敛质量未披露，不能把
局部 timing 当作通用加速数字。
<!-- semantic-body-binding:SF-2026-BYTEDANCE-VEOMNI-PR-781:end -->

## Stage 3：连 Parameters 也分片

Stage 3 的长期驻留状态：

```text
parameter shard
gradient shard
optimizer shard
```

理想每卡：

```text
M_Z3 ~= P * (b_p + b_g + b_o) / D
```

但 layer forward/backward 需要对应完整 parameter view。Runtime 在使用前 AllGather 某个 module 的 parameters，计算后释放或重新分片：

```text
sharded parameters at rest
-> prefetch / AllGather module parameters
-> forward or backward compute
-> release / reshard
```

Stage 3 的核心不是“一次把完整模型 gather 回来”，而是按 module execution order 管理短生命周期 full views。Prefetch distance、reuse 和 bucket size 决定 communication 能否被计算覆盖。

固定均匀 shard 的另一个边界来自 optimizer 与 quantization 的结构语义。element-wise AdamW 可以在任意连续
offset 切分；matrix optimizer、row-wise state 或 block quantization 却可能要求一个原子 block 由同一 owner
持有。若 shard boundary 切穿 block，系统只能 padding、copy、gather 或改变算法。因而更一般的 placement contract 是：

```text
global tensor identity
+ indivisible row/block granularity
+ per-rank ragged ownership
+ planned padding/reorder metadata
+ persistent buffer and stream lifetime
+ checkpoint round-trip mapping
```

ragged placement 可以减少无意义 padding/copy，却新增近似 layout planning、granularity cliff、root imbalance、
pointer lifetime 和 checkpoint compatibility。规则 shape、普通 optimizer 或上游互操作优先时，均匀 FSDP shard
仍更简单。veScale-FSDP 为结构感知 shard planner 与 persistent buffer 提供了作者实验；这些实验不证明
所有模型、拓扑与 workload 的通用 production 收益，也不证明 zero-copy 没有 lifecycle 成本。

## 一个 1B 参数、8 Rank 小例子

沿用第 35 章的示例 precision：

```text
b_p = 2 bytes
b_g = 2 bytes
b_o = 12 bytes
P = 1B
D = 8
```

忽略 alignment、buffers 和 activations：

```text
Standard DP:
1B * (2+2+12) = 16 GB per rank

ZeRO-1:
1B * (2+2+12/8) = 5.5 GB per rank

ZeRO-2:
1B * (2+(2+12)/8) = 3.75 GB per rank

ZeRO-3:
1B * (2+2+12)/8 = 2 GB per rank
```

这些是 model-state lower-order estimates，不是实际 peak GPU memory。Stage 3 AllGather window、communication bucket、fragmentation 和 activations 都会增加占用。

## Stage 越高为什么不一定越快

更高 stage 覆盖更多状态，也提高 lifecycle frequency：

- Stage 1/2 主要在 optimizer/gradient boundary 通信。
- Stage 3 让 parameter gather 进入 module forward/backward 路径。
- Small modules 或 slow network 使 latency 更难隐藏。
- Prefetch 太早增加 peak memory，太晚让 GPU 等待。

若模型本来能放进显存，Stage 3 的额外 orchestration 可能降低吞吐。正确选择是满足 memory requirement 的最低复杂度 stage，再通过 profile 判断。

## ZeRO 没有解决 Activation OOM

训练总显存：

```text
model states
+ activations
+ temporary workspace
+ communication buffers
```

长 sequence、大 micro-batch 或深层 activation 可能占主导。此时可考虑：

- Activation checkpointing / recomputation。
- 减小 micro-batch，增加 accumulation。
- Sequence/Context Parallel。
- 更高效 Attention kernels。

继续提高 ZeRO stage 只减少 model-state 项，可能对总 peak 改善有限。

## Communication 不能只概括为“换显存”

需要分别问：

```text
what tensor?
which collective?
when in forward/backward?
how often?
can it overlap?
```

典型 pattern：

- Gradient ReduceScatter。
- Updated parameter AllGather。
- Stage 3 module parameter AllGather/prefetch。

Bucket 大小在 bandwidth utilization、launch latency、overlap 与 peak memory 之间折中。通信量相近的配置，也可能因为 critical-path placement 不同而性能悬殊。

### Shard Ownership 与同步粒度可以分别选择

每个 rank 在同一层执行 collective，适合样本长度与计算量接近、拓扑优化可充分利用的训练；长尾 sequence 的后训练则可能在每层、每个 microbatch 重复等待最慢 rank。参数、梯度和 optimizer state 仍可保持 FSDP 式分片，却把取参数与归还梯度拆成按需点对点操作：worker 向 shard owner 读取参数，将梯度发送给相应 owner 累加；同一 GPU 可以同时承担 worker 与 owner。这里改变的是通信推进方式，不是 state ownership，也不是重新发明 parameter server。

按需推进要求接收端不必与发送端同时进入同一个 collective。ODC 的实验实现用节点内 CUDA IPC、节点间 NVSHMEM/RDMA 取参数，并用轻量 daemon 累加梯度；它仍在整个 minibatch 梯度完成后同步更新，不允许各 worker 独立提交不同版本的模型。因此 asynchronous communication progress 不等于 asynchronous optimization。这个边界让 runtime 先平衡整个 minibatch 的计算量，再在每个 worker 内按显存容量打包 microbatch，而不要求每对 microbatch 都同样昂贵；长 sequence 的 memory 与 compute 增长不同，局部 packing 无法总是同时平衡两者。

代价同样来自通信边界的改变：该实现的跨节点点对点 primitive 带宽低于 NCCL collective，失去了部分分层拓扑优化。长 context 可用计算重叠隐藏它，短 microbatch 却可能重新受通信限制；把 parameter/gradient 分片限制在节点内、只让 optimizer state 跨节点分片可减少此压力，但增加每节点常驻状态。均匀负载或通信占主导时，普通 collective 仍是更简单的基线。这一分支只支持保留 minibatch barrier 下的负载均衡选择，不证明 rollout 端到端加速，也不把弹性、容错或异步 SGD 的未来设想当成已实现能力。

<!-- source-family:SF-2026-ARXIV-2601-19362 -->

## FSDP 与 ZeRO 的关系

ZeRO 是消除 DP model-state redundancy 的分阶段思想；FSDP 是围绕 fully sharded parameters/gradients/optimizer states 组织 module lifecycle 的实现家族。

两者在机制上高度相关，但 API、flattening、prefetch、state-dict 和 mixed-precision policy 可能不同。不能简单写成：

```text
FSDP == one exact DeepSpeed ZeRO implementation
```

更稳定的知识树位置是：

```text
data-parallel state sharding
-> ZeRO stages / FSDP-style runtime
```

Tensor Parallel 则切 operator 本身。TP group 内共同执行一个 model shard，DP/FSDP group 再对等价 shards 做复制或状态分片；它们可以组合。

## Offload 把状态放到更慢层级

ZeRO-Offload / ZeRO-Infinity 可以把 optimizer、parameters 或相关计算移向 CPU/NVMe：

```text
GPU capacity pressure
-> host / storage capacity
-> PCIe, CPU memory, CPU compute, NVMe IO pressure
```

Offload 是否有效取决于：

- State reuse distance。
- Prefetch 是否及时。
- Pinned host memory 与 NUMA placement。
- CPU optimizer throughput。
- PCIe/NVLink-C2C 和 NVMe bandwidth。

目标不是移出最多 bytes，而是在不让 GPU 等待的前提下，把 cold state 放到更大层级。

### Full Host Cache 用容量换跨节点 Communication

ZeRO/FSDP 在每次需要完整参数时通过 inter-node collective 重建 working set，在网络带宽充足、host memory 受限时最合理；若每个节点都有足够 DRAM 而跨节点链路成为瓶颈，可以让每个节点的 host memory 缓存完整参数，在节点内按 layer/operation 将 active shard stream 到 GPU。这样以 host capacity 与 PCIe traffic 换掉重复的 inter-node parameter collective：host cache 拥有完整 parameter generation，GPU 只拥有当前 working set，optimizer/gradient ownership 仍按并行计划提交，prefetch 不能让未完成的新版本提前可见。

完整 host cache 增加每节点内存、NUMA/pinned-buffer、CPU-GPU copy 与 cache coherence 成本；参数更新、恢复或 world-size 改变时，任一节点的 stale copy 都可能污染训练。网络较快、DRAM 不足或模型可完全驻留 HBM 时，普通 ZeRO/FSDP 仍更简单。`arXiv:2602.06499v1` 的 exact-v1 只支持 FCDP 在 4×8 A40、100Gbps EDR、所披露 FP16/FP32 与 DeepSpeed 配置下的 full host cache、prefetch 和作者结果，不证明不同拓扑、模型、optimizer 或 failure recovery 下的普遍优势。

<!-- source-family:SF-2026-ARXIV-2602-06499 -->

### 从 GPU-resident Shard 到 CPU-authoritative Layer Stream

ZeRO/FSDP 假设 state 分片后各 rank 的 active working set 能进入 accelerator；当总权重、gradient 与 optimizer
state 远超 HBM、但单层 working set 可容纳时，还可以让 CPU store 成为 authoritative state，每层执行前预取
临时 GPU cache，执行后把 gradient/update 归还 CPU：

```text
CPU master parameters + gradients + optimizer state
→ prefetch one/few layer working sets
→ GPU forward/backward
→ return gradient / apply CPU update
→ evict transient layer cache
```

这条流式路径还需要把“已预取”细化成可检查的buffer生命周期。层执行模板不能永久绑定一组驻留GPU权重指针，而是在Weights-Ready之后绑定当前working set；Backward-Done表示梯度已可搬回CPU，Buffer-Free则必须等相关offload排空后才允许复用。同一ping-pong槽位若在D2H完成前被下一层覆盖，forward可能正常，CPU optimizer却消费了错误梯度。H2D、compute、D2H分流和有界pinned staging slabs减少互相等待，但不是把整模型pin住，也不是删除这些依赖。

因此overlap只在计算足以覆盖搬运时隐藏延迟；PCIe或CPU更新成为瓶颈时仍会串行等待。事件、layer绑定、gradient accumulation和CPU update版本须一并进入checkpoint一致性边界。这是[流式训练实现](https://arxiv.org/html/2604.05091v1)对前述容量分支的具体落实，不改变ZeRO的状态owner，也不把H200 PCIe与GH200 C2C看成同一传输条件。<!-- source-family:SF-2026-ARXIV-2604-05091 -->

这是容量优先的 offload extreme，不是 ZeRO 的普遍后继。它以 PCIe traffic、CPU memory bandwidth、optimizer
latency、pinned-buffer pressure 和更长 step time 换取单卡容量；checkpoint 必须在 CPU update、next-layer prefetch
与 model-version commit 之间定义一致边界。NVMe offload 可继续扩大容量但增加更深 pipeline；多 GPU ZeRO 在
吞吐、训练时限或网络资源可用时仍合理。

MegaTrain 的作者结果只证明该 layer streaming 在披露模型/硬件/batch contract 下可运行；冲突的 ablation/context
数字、缺少 recovery/SLO/cost contract 与后续代码漂移使其保持 Experimental，不外推“单 GPU 更优”。

## ZeRO++ 移动 Communication 瓶颈

当 state sharding 解决显存，collective 可能成为主瓶颈。ZeRO++ 研究量化通信与分层 partition 等路径，尝试减少跨节点流量。

通信压缩可能引入额外 quantize/dequantize compute、数值误差和 topology assumptions。论文性能数字必须绑定模型、网络和并行配置，不能作为任意集群承诺。

若不能接受量化误差，另一条分支是利用参数在相邻更新间的位模式冗余，只传变化部分并编码其余字段。但当发送端依赖 hash cache、接收端依赖 exponent cache 和变化 bitmap 时，“无损”不仅取决于编码器，还取决于双方缓存是否对应同一代张量；有限 hash 的碰撞假设也不能替代确定性的相等检查。系统因此需要声明缓存重建、失配检测与全量回退策略，并把编码、缓存显存和同步成本计入 collective；这些是恢复设计要求，不代表已有有限训练测试验证了故障恢复。变化广泛、网络不再主导或缓存身份难以维持时，无状态传输仍是更简单的基线。

## Checkpoint 是 State Sharding 的正确性部分

每个 rank 只有局部 shards 时，单 rank `state_dict` 不是完整 checkpoint。系统必须保存：

- Global tensor metadata 与 shard offsets。
- Optimizer parameter ownership。
- DP/TP/PP 等 process-group layout。
- Step、scheduler、RNG 与 data cursor。

Same-world-size resume 只是最低门槛。生产平台还可能需要 DP degree 改变后的 optimizer reshard、weights consolidation 和 runtime artifact conversion。

如果训练可运行却无法可靠恢复，state sharding 仍未完成系统闭环。

## 工程选择与验证

选择 stage 前先做 memory breakdown：

```text
optimizer dominant -> consider Stage 1
gradient also large -> consider Stage 2
parameters cannot reside -> consider Stage 3 / TP
activations dominant -> recompute / sequence strategies
```

验证至少包括：

- Estimated vs measured model-state/peak memory。
- AllGather/ReduceScatter bytes、duration 与 overlap。
- Prefetch stalls 和 bucket occupancy。
- Short-run loss equivalence with unsharded reference。
- Checkpoint commit、resume 与 reshard。
- OOM/retry 后 state consistency。

## 本章在知识树中的位置

```text
Data Parallel state redundancy
-> optimizer / gradient / parameter sharding
-> ZeRO Stage 1 / 2 / 3
-> offload / communication optimization
-> DeepSpeed / FSDP runtime
-> distributed checkpoint
```

第 36 章定义 state sharding 的位置，本章解释 state lifecycle；第 40 章把它放进多维并行组合，第 41 章再讨论 DeepSpeed runtime policy。

在 Memory 横线上，本章减少长期驻留的 training model-state replicas；第 45 章以后处理的是 request KV、block mapping 与 inference HBM budget。两者都使用 sharding、gather、locality 等原则，却服务不同 identity、lifetime 和 correctness contract。

## 自检问题

1. 标准 DP 的 model-state memory 由哪些项组成？
2. ZeRO Stage 1、2、3 分别新增分片什么？
3. 1B 参数、8 ranks 示例怎样得到 5.5/3.75/2 GB？
4. Stage 3 为什么需要 module-level parameter lifecycle？
5. 更高 stage 为什么可能降低吞吐？
6. ZeRO 为什么不能直接解决 activation-dominant OOM？
7. Bucket size 在哪些目标间折中？
8. FSDP 与 ZeRO 应怎样放在同一机制树中？
9. Offload 把显存问题转成哪些系统瓶颈？
10. 为什么 distributed checkpoint 是 state sharding 的正确性要求？

## 小结

ZeRO 逐步分片 optimizer states、gradients 和 parameters，消除标准 DP 的冗余副本。Stage 提升带来更大的 model-state savings，也让 gather、prefetch、reshard 和 checkpoint 更深入执行路径。

它不是通用 OOM 开关。Activation、workspace、network、offload 层级和恢复语义必须分别建模。正确 ZeRO 配置应从 memory breakdown 出发，并用通信、吞吐、数值与 restore 共同验证。

## Review notes

- `SF-2026-ARXIV-2602-22437` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22437v1) §3–6与必要 block-optimizer/padding 消融。2+2+3=7，现有原子 block、ragged placement、近似规划与生命周期/fallback 已覆盖，不重复扩写；仅删除未核 artifact 断言，改为作者实验不授通用 production 收益，不否认其工业部署经历。root 原源/actual owner Existing 与窄纠正 PRE 通过；实际纠正正文、邻接与自身末注经 root 非作者 POST 通过，窄锁释放。未核 artifact/复现，不授日级完成。

- `SF-2026-ARXIV-2601-19362`，Status: Experimental：[ODC exact-v1](https://arxiv.org/html/2601.19362v1) §2–4、§5.1–5.4及§6.1–6.2支持按需 parameter gather/gradient scatter-accumulate、minibatch barrier 和 LB-Mini 分支。作者 LongAlign/SWE-Smith SFT、AIME GRPO 实验使用 R1-Distill-Qwen 1.5–32B、最多32×A100 80GB、NVSwitch及800Gbps/node RoCE；RL只统计训练，排除 rollout。SFT最高36%与RL最高10%不外推到任意负载；minibatch=1无收益、packing改善后差距缩小、跨节点 primitive 带宽低于 NCCL 均保留。必要原源与实际正文/相邻链路已由 root 独立复核通过，未运行实现或复现实验。

- `SF-2026-ARXIV-2604-09406`，Experimental：[exact-v1](https://arxiv.org/html/2604.09406v1) §3/Algorithm 1/§3.2、Tables 1–3、§4.3/5 支持在线 activation basis 与近似 moment transport 分支。受测 Llama-2 7B、Llama-3.2 1B 微调及 130M/350M C4 预训练；1B rank 32 的 GSM8K 23.78 低于 Adam 27.09，350M validation loss 也不是全面优于 LDAdam。未采用 peak-memory 倍率作为任意 hardware/batch/length 保证；未验证与 ZeRO 组合、distributed checkpoint restore 或全面训练加速。root 已完成必要原文与实际正文/相邻链路的写后独立复核，通过，本地实验未复现。

- [STQuant 2604.06836v1](https://arxiv.org/html/2604.06836v1)，Experimental；§3.2–3.5、Algorithm1、§4与Table4。采用按层/时间的gradient-statistics precision proposal及moment编码分工，不采用摘要的near-optimal/O(1)/万亿模型保证；Fisher/Hessian类比不是一般等式，算法与正文CV定义也需实现确认。作者内存统计不是全训练峰值，消融同时移动bit与PPL。

- [MegaTrain 2604.05091v1](https://arxiv.org/html/2604.05091v1)，Experimental；§3.1–3.4、§4及AppendixA。采用layer-template动态绑定、Weights-Ready/Backward-Done/Buffer-Free、有限host slab；不采用无条件隐藏搬运、跨互联普遍吞吐或未测试的故障恢复保证。

- `SF-2026-ARXIV-2604-00785`，Status: Experimental：[exact-v1 §3.2、Table 3](https://arxiv.org/html/2604.00785v1) 支持按 expert/non-expert 复制域选择 optimizer shard group；Aurora Intel PVC 的 optimizer-step 1.07–1.36× 与全步最高 1.19× 是作者特定模型/拓扑结果，不证明任意 EP/DP、checkpoint 恢复或跨硬件收益。

- `SF-2026-ARXIV-2609-04609`，CIERA，Status: Experimental：exact-v1 §2–4、Algorithm A 的双端缓存、字段编码和有限训练测试支持状态化无损通信分支；独立64-bit hash假设不是绝无碰撞证明，4/8/16卡实测与更大规模模拟分开。未采用普适加速数字，未验证失配/故障恢复；正文的重建与回退是设计要求。https://arxiv.org/html/2609.04609v1

- `SF-2026-ARXIV-2602-06499`（Status: Experimental）：exact-v1 支持 FCDP 的 per-node full host parameter cache、pinned NUMA-local buffers、dedicated CUDA stream 与作者 4×8 A40/100Gbps EDR 实验；不证明所有模型、网络、optimizer、精度或恢复路径上都优于 ZeRO/FSDP。https://arxiv.org/html/2602.06499v1

- MegaTrain（CPU-authoritative layer-streamed training；Status: Experimental）: https://arxiv.org/abs/2604.05091

本轮 Review 在既有 Stage 1/2/3 边界上补齐逐项 memory formula、1B/8-rank 小例子、parameter lifecycle、activation 非目标项、FSDP 关系、offload、ZeRO++ 与 checkpoint correctness。

Primary-source / official documentation 校验入口：

- Samyam Rajbhandari et al., "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models", 2019: https://arxiv.org/abs/1910.02054
- DeepSpeed ZeRO tutorial: https://www.deepspeed.ai/tutorials/zero/
- Jie Ren et al., "ZeRO-Offload: Democratizing Billion-Scale Model Training", 2021: https://arxiv.org/abs/2101.06840
- Guanhua Wang et al., "ZeRO++: Extremely Efficient Collective Communication for Giant Model Training", 2023: https://arxiv.org/abs/2306.10209
- PyTorch FSDP documentation: https://docs.pytorch.org/docs/stable/fsdp.html
- veScale-FSDP（structure-aware ragged shard placement；Status: Experimental）:
  https://arxiv.org/abs/2602.22437
