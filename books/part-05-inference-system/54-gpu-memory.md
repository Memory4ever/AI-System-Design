# 第54章 GPU Memory

**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场
**Stable Knowledge Node ID:** `INFER-GPU-MEMORY`
**Legacy Chapter:** Ch50
**Status:** Draft

**Roadmap Intent:** 权重、激活、KV Cache、临时 buffer 如何争夺显存。

## 本章要回答的问题

为什么大模型系统经常不是算不动，而是装不下、搬不动、调不顺？GPU Memory 为什么会成为训练和推理共同的核心约束？

本章的核心判断是：**GPU inference capacity 不是“权重能否装入”的二元问题，而是 weights、resident KV、workspace、communication、fragmentation 和 safety reserve 对同一 HBM budget 的动态竞争。**任何调度和加速机制最终都必须满足这个物理约束。

## 从 memory hierarchy 开始

GPU 上并不是只有一种 memory。大致可以把它理解为：

```text
register / SRAM / shared memory / L2 cache
→ HBM
→ CPU memory
→ storage
```

越靠近计算单元，速度越快、容量越小、管理越精细；越远离计算单元，容量越大、访问越慢。

这解释了为什么很多优化并不是减少数学运算，而是减少 HBM 读写，或者把数据尽可能留在片上 memory 中。FlashAttention 的核心价值就在这里。

## 显存里到底有什么

训练时，显存至少包括：

- parameters
- gradients
- optimizer states
- activations
- temporary buffers
- communication buffers

推理时，显存至少包括：

- model weights
- KV Cache
- activation / workspace
- sampling / logits buffer
- runtime metadata
- communication buffers

这也是为什么训练和推理的优化路径不同。训练要处理 optimizer state 和 backward activation；推理要处理长生命周期 KV Cache 和动态请求。

做容量规划时，可以先建立两个近似下界：

```text
weight bytes ≈ parameter_count x bytes_per_weight

KV_bytes_per_token = 2 x L x H_kv x d_h x bytes_per_element

M_KV
= sum_(r=1)^R (T_p,r + T_o,r)
  x KV_bytes_per_token
```

其中 `R` 是 active request 数，`T_p,r`、`T_o,r` 是请求 `r` 已缓存的
prompt/output token 数，`L` 是 layer 数，`H_kv` 是 KV head 数，`d_h` 是每个
head dimension。这个写法沿用第 19、22、45 章的符号，并直接表达真实 batch
中的变长请求；物理 runtime 仍可能按 blocks、alignment 和不同 layout 分配。

它们都不是最终 `nvidia-smi` 数值，因为 allocator、workspace、CUDA graph、collective buffer、fragmentation 和 runtime reserve 还会占用空间。但如果连这两个下界都超过容量，任何调度参数都无法补救。

更完整的 admission 约束可以写成：

```text
M_HBM
>= M_weights
 + M_KV
 + M_workspace
 + M_communication
 + M_fragmentation
 + M_reserve
```

Scheduler 真正可分配的是扣除固定权重和峰值保留后的 KV budget，而不是 GPU 标称总显存。

定义：

```text
M_KV_usable
= M_HBM
 - M_weights
 - M_workspace
 - M_communication
 - M_fragmentation
 - M_reserve
```

若为了说明机制，假设 active requests 具有相同的 planned KV footprint
`M_KV_per_request`，并用 `R_admit` 表示可 admission 的请求数，容量上界才可以
近似写成：

```text
R_admit
<= floor(M_KV_usable / M_KV_per_request)
```

真实 workload 的请求长度不同，正确约束仍是前面的
`sum_r(T_p,r + T_o,r)`；scheduler 还要为未生成的 output tokens、block 粒度和
瞬时峰值留 margin。这个近似式只说明 HBM 怎样转化为 admission capacity，
不是固定并发承诺。

## 固定、动态与瞬时占用

容量分析应按生命周期区分：

| 类别 | 典型对象 | 特征 |
| --- | --- | --- |
| Fixed | weights、部分 graph/runtime state | 模型加载后长期驻留 |
| Request-dynamic | KV Cache、adapter state | 随并发与长度增长 |
| Step-peak | activations、logits、workspace、collective buffers | 随 batch shape 与 kernel 瞬时变化 |

只测 idle model memory 会漏掉高峰 workspace；只按最大 KV 填满剩余 HBM，又会让下一次大 Prefill 或 collective 没有工作空间。

## 一个可用容量小例子

假设一张 GPU 对当前进程可用 80 GiB：

```text
weights + fixed runtime = 45 GiB
peak workspace          = 8 GiB
communication           = 3 GiB
reserve                 = 4 GiB
```

则可规划给 resident KV 与其 fragmentation 的上限约为 20 GiB，而不是 35 GiB。若第45章的示例请求每个占 1 GiB logical KV，也不能直接 admission 20 个：block waste、长度增长和峰值并发仍需 margin。

这个数字只是算术示例，不对应特定 GPU、模型或 runtime。

### 一个有时效边界的硬件算例

2026 年 7 月，Hugging Face 在 AMD MI455X early-access hardware 上发布了一次
preliminary Transformers capacity study。AMD 官方规格给出的单卡容量为
`432 GB HBM4`；对照设备容量为 `192 GB`。测试加载了约 `64 GB` 的
Qwen3-32B BF16 weights，并报告新设备在 OOM 前支持超过三倍的并发请求。

这个结果不能当作通用 Serving benchmark，但可以用来校验固定成本为什么会
放大“剩余容量”差异。暂时忽略 workspace、communication、fragmentation 和
reserve，仅扣除相同 weights：

```text
new KV remainder / old KV remainder
= (432 GB - 64 GB) / (192 GB - 64 GB)
= 368 / 128
= 2.875
```

这里比较的是理想化 KV remainder，不是 throughput，也不是可以直接 admission
的 request 数。文章没有完整公开请求长度、KV dtype、allocator margin 和 OOM
判定，实际“超过三倍”不能由上式独立复现。

这个例子还应区分三种证据：

| 证据 | 能说明什么 | 不能说明什么 |
| --- | --- | --- |
| 官方 HBM 规格 | 物理容量和 peak bandwidth 上限 | 真实 workload 性能 |
| Framework compatibility tests | 一组模型能否通过当前测试 | kernel 已最优或数值全等 |
| Capacity study | 给定配置下的 OOM 边界 | TTFT、TPOT、throughput、goodput |

所以硬件容量升级首先改变 feasible region；能否转化为线上价值，仍由 model
footprint、request distribution、runtime maturity 和 SLO 共同决定。

## KV Cache 为什么改变推理显存

模型权重是相对固定的，加载后不会随请求持续增长。KV Cache 不同。它随 batch size、sequence length、layer 数、KV head 数、精度一起增长。

因此推理显存上限常常不是“模型能不能加载”，而是“还能容纳多少并发请求和上下文长度”。

这也解释了 PagedAttention、RadixAttention、ShadowKV、KV offload 的意义。它们都不是孤立技巧，而是在应对 KV Cache 变成主要 runtime state 后的 memory pressure。

多轮请求还要区分“有多少工作本来可以复用”与“这些状态能否留到下一次访问”。若单个 Prefill worker 不接收
Decode 产生的 response KV 回写，下一轮的历史回答与新增用户输入仍须在此处计算；即使容量足够保留所有已算
prefix，也不能让这部分新工作变成命中。因此应看可复用 block/token 工作量占总 Prefill 请求工作量的份额，
不能直接用“后续轮数占比”或 request hit rate 代替它。

在 whole-content LRU、Poisson 新会话及特定独立轮次增量/等待时间假设下，一个 mean-field 条件模型进一步把
命中工作量比例分成“固有可复用份额 × 下一轮在淘汰前到来的概率”。容量通过可容忍的 reuse interval 改变后一项，
不改变固定 workload 的前一项。这是容量规划的受限近似，不是实际 partial-block、ref-count 或 timestamp-based
缓存的通用定理；共享 prefix、路由和负载相关的 think time 都可能改变模型，不能把拟合出的留存时间当平台常数。

这种分解可以判断继续增加 HBM 是否还有复用空间，却不能替代原有 bytes/OOM 硬约束，也不直接证明 TTFT 或
goodput。复用身份仍由[第45章](45-why-kv-cache-speeds-up.md)定义，是否迁移 response KV 是
[第55章](55-pd-disaggregation.md)的传输与 ownership 选择，排队和尾延迟由
[第56章](56-inference-scheduling.md)联测。请求很少复用、状态身份不相容或等待分布明显漂移时，保守容量预算与
实际 trace replay 比依赖该近似更稳妥。

<!-- source-family:SF-2026-ARXIV-2609-02027 -->

## Fragmentation 与 Reserve 为什么真实存在

Logical free bytes 不一定能被目标 kernel 使用。Allocator 粒度、KV block 内部空位、CUDA graph capture pool、tensor alignment 和暂未释放的 asynchronous buffers 都会造成差异。

Reserve 不是“浪费掉的显存”，而是为 shape variation、collective、temporary allocation 和 failure recovery 保留的操作空间。Reserve 太大降低并发，太小会让系统在高负载时频繁 OOM 或 preempt。

## 三类缓解路径

### 减少 Bytes

Weight/KV quantization、GQA/MQA、压缩或稀疏 retention 直接减少 resident bytes，但需要质量与 kernel 验证。

KV retention 还存在两个不同粒度。Token eviction 先决定保留哪些历史位置，简单且适配现有 accelerator；但每个
被保留 token 的完整 K/V vector 仍需从 memory hierarchy 取回。当 vector traffic 成为新的带宽下限，系统可以继续
选择 token 内的 elements：

```text
full KV
→ token-level importance / eviction
→ element-level selection inside retained vectors
→ layout-aware fetch + bounded approximate attention
```

第二层选择与第一层不是免费相乘。它需要保存两级 importance state、校准允许的 accuracy loss，并把非连续访问、
metadata、sorting 和 kernel/accelerator 支持纳入成本；否则省下的 bytes 会被 fragmented access 与 ranking overhead
吃掉。可重配置 sorter 能复用两级排序 datapath，但会引入 silicon specialization，离线 per-task calibration 也不能
自动转移到 production workload。Full KV 仍是 correctness baseline；没有专用 kernel、向量访问尚未主导或严格
exactness 优先时，token-only retention 仍更合理。

### 提高利用率

Paging、prefix sharing 和更精确 admission 减少预留与碎片，却不改变每个有效 KV element 的逻辑需求。

### 扩展层级

CPU/SSD/off-node cache 扩大总容量，却加入 transfer latency、bandwidth contention 和 consistency。它们把“装不下”改成“何时值得搬”。

这里的 CPU 容量层以离散 GPU 与独立 host memory 为前提。在统一内存的移动 SoC 上，CPU 与 GPU 共享同一块物理 RAM，改变访问处理器不会凭空增加容量；压缩 KV 能减少实际占用，但压缩副本仍留在这块 RAM 中，压力继续上升时仍可能需要移到 flash。因而层级设计首先要核实物理容量边界，不能把逻辑上的 CPU/GPU 地址或访问路径重复记为两份空间。

当其他应用可以随时要求回收内存，问题也从固定 offload 比例变成“释放任意一部分后，怎样尽早恢复下一次请求”。细粒度 weight/KV buffer 可以独立释放与恢复，保留较早执行的层，并让 CPU 按后续依赖准备数据；GPU 只消费已就绪的共享 buffer，分配、解压和读取才有机会与计算重叠。收益取决于真实恢复关键路径，代价包括同步、压缩质量、带宽竞争和 profile 随温度或负载漂移；共享地址并不保证无需等待，也不能防止极端压力下进程被终止。内存充足、恢复开销很小或隔离要求更强时，常驻或简单串行恢复仍更可靠。<!-- source-family:SF-2026-ARXIV-2609-01338 -->

#### Peer GPU Spare Memory 是可撤销的中间 Cache Tier

单个模型独占固定 GPU、各卡 HBM 都接近饱和时，memory hierarchy 只需要在本卡 HBM 与 CPU/SSD 之间选择；多 GPU 节点同时承载异构请求后，有些 peer GPU 可能暂时拥有空闲 HBM，且 NVLink 路径比 host offload 更近。cache manager 可以把这些空闲页作为 opportunistic tier，按 model/expert/KV generation 注册 peer residency，并在计算 owner 需要容量或 topology/tenant policy 改变时撤销；canonical weight 或 KV 身份仍由原 owner 持有，peer 只保存可重建副本。

这条层级减少 host transfer，却会与 TP/PP collective、其他租户和 peer compute 争用互联，并新增 remote pointer、revocation、stale generation 与 tail-latency failure。拓扑不明、隔离要求高、peer 压力上升或副本无法及时回收时，应回退本地 HBM/CPU tier。`arXiv:2602.00328v1` 的 exact-v1 只在单机双 GPU NVLink 和作者所列模型/强制 offload 设置中验证 Harvest，不证明 NVSwitch、多租户、并行通信竞争或生产 SLO 下仍有同等收益。

<!-- source-family:SF-2026-ARXIV-2602-00328 -->

最简单的 offload 在当前 layer 请求某页后才开始搬运，容易保持正确顺序，却会把 CPU selection、PCIe transfer
和 GPU attention 串在 token critical path 上。当相邻 layer 的访问具有可预测结构时，可以让 CPU 提前一层计算
下一层候选集，并把 selection/transfer 与当前 GPU layer 重叠：

```text
reactive offload fetch
→ layer-ahead CPU candidate computation
→ asynchronous transfer with generation-tagged completion
→ GPU consumes only ready state at the target layer
→ miss / lag falls back to ordinary attention or a larger resident set
```

这不是让 CPU 取得 attention truth；它只拥有 pre-computation/prefetch proposal，目标 layer 的 GPU execution 与
cache owner 仍决定最终可见状态。收益取决于 CPU 核数、host memory bandwidth、PCIe 和 layer compute 是否足以
隐藏准备时间；CPU 落后、候选错误或同步过多时，预计算会变成浪费并拉高 tail latency。KV 能驻 HBM、Context 较短
或 host 很弱时，普通 GPU attention/offload 仍更稳定。事件时证据只覆盖 exact-v1 §3.2–§3.4 的 layer-ahead
CPU attention estimation、异步预取与 pipeline integration，以及 §4.3 的作者模型、batch 与硬件配置；不能把重叠
比例外推为跨平台常数。<!-- source-family:SF-2026-ARXIV-2603-27138 -->

### 层级的管理权不应默认属于 Framework

最初的 offload 实现往往由 model runtime 显式管理：它按 expert 或 layer 统计热度、固定 pinning，并决定何时从慢层加载。这在 workload 稳定、需要可预测尾延迟时最容易校验，但它也另建了一套与操作系统内存回收并行的 residency policy。

当 expert pool 超过 DRAM，而权重本来就以文件页形式存在时，可以让 kernel page cache 拥有 eviction / reclaim，runtime 只提供 model-aware admission 和预测建议。这把“专用 expert cache”重写为一个分层契约：

```text
kernel owns page residency and reclaim
runtime owns expert identity, admission and lookahead advice
scheduler owns capacity / latency SLO
```

收益是复用成熟的 recency 与回收机制，并在 domain shift 下避免静态热度表过期；代价是 page-cache hit/reclaim path 的额外开销，以及 cgroup、MGLRU、`mlock`、balloon 和 kernel revision 都会进入结果身份。因此 kernel-managed 不是一个通用更快结论；当回收路径不可控、SLO 极严或 expert working set 完全可常驻时，专用 arena 与静态 placement 仍然更稳定。

另一层容易被忽略的开销发生在“文件页已经可被 accelerator 读取”之后。普通 framework loader 仍会把它复制到自己的 allocation，产生额外的 ingestion copy。在 integrated 或 coherent-memory topology 上，producer 可以用 `MAP_SHARED` 映射 tensor，封装成 no-copy GPU buffer，再通过 DLPack 把同一存储导入 framework。但 zero-copy import 本身不够：activation residency 和 GPU ordering 也必须一起成立，否则只是把一次拷贝换成更慢的执行路径。

这个分支用 topology-specific implementation、页生命周期和 ordering 约束换取减少副本、缩短首次加载并让页继续可共享、可回收。跨 PCIe 或设备不能高效直读 file pages 时，resident copy 或 overlapped streaming 仍是正确路径。所以文件页 adoption 必须由 memory topology 决定，不能被封装成无条件的 loader 优化。

<!-- source-family:SF-2026-ARXIV-2608-12103 -->
<!-- source-family:SF-2026-ARXIV-2608-12114 -->

权重 offload 也应从“整层搬运”进一步区分到 conditional-compute state。MoE 的 active expert 由 router
决定，静态把全部 experts 常驻 HBM 最简单且延迟稳定；固定 offload 一部分 experts 能扩容，却忽略请求
分布变化。Router-conditioned expert cache 可按实际激活维护 hot set，进一步用前序层或历史路由预测下一
步 expert 并异步 prefetch：

```text
full expert residency
→ static host offload
→ router-conditioned expert cache
→ predicted asynchronous prefetch
```

这里与 GEMM tiling、FlashAttention 的共同点只是 IO-aware 的原理复用（`Principle Reuse`）：都把超过近端容量的状态
分块，并尝试用 pipeline 隐藏搬运。数学条件并不相同。GEMM 的 operand 与 reduction 顺序预先已知；online
softmax 还能用 running maximum 与 normalization sum 合并各 tile，避免 materialize 完整 attention matrix。
MoE router 则在看到当前 hidden state 后才选择一组不同的非线性函数 `Expert_e`，不存在一个小型 running
statistic 可以精确恢复任意尚未驻留的 expert weights。

因此 expert page miss 仍有不可消除的数据移动下界：`T_miss >= M_miss / B_slow`。Tiling、double buffering
和 prefetch 只能重叠这段时间；Prefill 或大 expert batch 可以用更多 token 摊薄一次加载，低并发 Decode 若为少量
token 搬入整个 expert，则往往无法用计算覆盖传输。模型级 expert/page 与 kernel 级 matrix tile 可以形成两级
执行，但前者管理 weight residency，后者才分解单个已选 operator，不能把相似类比写成同一种算法。

它与 KV tiering 只复用 locality 原则：expert identity 是 weight artifact，KV identity 是 request/prefix state，
正确性与失效条件不同。预测错误会产生 PCIe stall、cache thrash 与 tail latency；open PR/RFC 只能作为
Experimental evidence，不能当作稳定框架行为。模型较小、expert 分布均匀、带宽紧张或 SLO 严格时，
全驻留与静态 placement 仍更可预测。

即使更慢的 memory tier 能容纳全部 experts，“容量足够”也不等于“路由后的计算单元被充分占满”。请求只激活少量且分布偏斜的 experts 时，resident weights 解决的是供给带宽，未解决 core occupancy 与 hot-expert contention。更完整的执行路径需要把 co-activation placement、local multicast、load-aware fetch 与 router 输出共同规划：memory pool 只交付不可变 expert weights，router 仍拥有语义选择，executor 决定如何把已选工作映射到可用计算单元。

这条分支用专用 near-memory 组织、放置校准和更复杂的调度换取较高 bandwidth density；路由分布漂移、专家集中度低或硬件不可得时，通用 GPU/HBM 的常驻或按需加载仍更稳妥。`arXiv:2608.13962v1` 的结果来自作者 measured-plus-modeled ReRAM/H20 系统、Qwen3.5 与 GLM-5.2 workload，没有公开可部署芯片 artifact，不能把延迟、能效或 occupancy 结果写成现货硬件保证。

<!-- source-family:SF-2026-ARXIV-2608-13962 -->

更大的硬件系统也会把优化边界从单 accelerator 推到 rack/POD：HBM、互联、CPU、storage、power 与
cooling 必须按 training、prefill、decode 和 Agent workflow 的不同状态流共同设计。但厂商 platform
announcement 只能证明版本化产品事实和设计方向，不能把未披露的 workload benchmark 写成通用结论。

### Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页

<!-- daily-20260621:infer-gpu-memory:start -->
### 逆向硬件证据必须声明 claim provenance

对 ANE 的 datapath、roofline、compiler/on-disk format、weight compression、driver/firmware command protocol建立 measured/decompile-derived/predicted 三类 claim，并区分 direct private route 与 Core ML supported path。

**Trade-off、failure、共存与回退。** private runtime/driver 路径 undocumented、unsupported、version-fragile，只适合研究测量；预测项不能冒充芯片公开规格或 shipping contract。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。

#### Review notes

- `SF-2026-ARXIV-2606-22283` — primary `arXiv:2606.22283v1`；exact-v1 URL=`https://arxiv.org/html/2606.22283v1`；Method=`https://arxiv.org/html/2606.22283v1 — §Part II Reaching the ANE — Software stack; Dispatching without Core ML; §Part VI The Silicon — Datapath and MAC geometry; §Part VII The Toolchain and Encoding; §Part VIII System Internals`；Evaluation=`https://arxiv.org/html/2606.22283v1 — §Part III Performance and Fit — Roofline; Power and efficiency; Across the chip family; Appendix A Operation-by-device matrix; Appendix E Provenance`；Non-proof=`https://arxiv.org/html/2606.22283v1 — §Part V Practice — Pitfalls and limits; §Methodology; §Open questions; §Introduction — direct route is undocumented, unsupported and version-fragile`。
<!-- daily-20260621:infer-gpu-memory:end -->

静态量化在 workload、expert hotness 与 KV demand 稳定时最容易复现：model artifact 只有一个精度身份。MoE 与长上下文同时出现后，冷 expert weights 与活跃请求 KV 会竞争同一 HBM；把 weight footprint 永久固定在最坏情况，会拒绝本可服务的请求。

一种受控演进是把每个 expert linear block 的 bit-plane 当作 page，并区分 desired precision 与 committed precision。planner 可以依据离线 sensitivity、在线 routing 和 KV pressure 提议目标精度，但 memory manager 只有在状态转换完成后才能提交：降精度先降低 committed bitwidth 再释放多余页；升精度先加载页，再提高 committed bitwidth。kernel 始终只读取 committed state，避免把未完成搬运当作可执行 artifact。

权重因此从静态 artifact 扩展为受策略控制的 runtime state，也新增 calibration drift、prompt-conditioned policy、CPU-GPU traffic、mixed kernel 和失败恢复问题。quality policy、tenant 与 request identity 必须进入 trace；严格可复现、精度预算固定或 transfer cost 高时，静态 weights 仍更安全。当前证据限于三种 MoE、作者 workload 与无生产 arrival/tail-SLO 的实验。

<!-- source-family:SF-2026-ARXIV-2605-28095 -->

离线大批推理若沿用 data parallel，每张 GPU 复制完整 weights，控制最简单，却会把本可供 KV 与 batch 使用的 HBM 固定占满。节点内互联空闲且 workload 以 throughput 为目标时，可以把 layer weight 只放在 owner GPU：大批次让 owner 将 weights 流送给 peers（weight-as-stream），小尾批次则把 activations 送到 owner 计算（compute-as-service），运行时按传输量选择分支。

它用 fabric bandwidth、同步和 layer-owner 故障域换 HBM 容量，且只在传输可被大批计算摊薄、尾部 activation 明显小于 weights 时成立；在线 tail-SLO、跨节点慢链路或 owner hotspot 会使收益消失。常规 DP 在模型可装下、请求小或隔离优先时仍更可预测。作者离线推理实验不证明该设计适用于持续到达、跨机通信或任意模型形状。

### 混合序列模型需要 Typed Memory Pages

统一 page size、统一 eviction 在状态同构、访问路径相近时能降低 allocator 与 scheduler 复杂度；混合 Mamba–Transformer runtime 同时拥有 recurrent state、attention KV、weights 与临时 workspace，它们的更新频率、可重建性和 fault cost 不同。因而 page identity 应携带 state type、model/request revision、placement owner 与 recoverability，allocator 只能提供容量，执行计划才决定何种状态可迁移或驱逐。

Typed pages 能减少错误 eviction 并改善分层放置，但会增加页表、碎片、迁移路径和 kernel dispatch 复杂度；工作负载单一或状态规模很小时，统一页仍更合适。arXiv:2605.22416v1 的系统与实验只支持其混合架构和披露环境，不证明同一分页策略在所有 Mamba、Transformer、硬件与 SLO 下都占优。

<!-- source-family:SF-2026-ARXIV-2605-22416 -->

### Reserve Reclaim 先与更简单的 Chunk Policy 比较

Prefill 为峰值 workspace 预留 HBM、Decode 又长期闲置这部分时，可用 CUDA VMM 暂时把 reserve 页借给 KV pool，并在下一次 Prefill 前撤销映射。它证明 reserve 能成为可回收状态，却不意味着应先引入动态映射：降低 chunked-prefill 的 `max_num_batched_tokens` 可能以更小复杂度释放更多 KV，且对 TTFT 影响很小。正确顺序是先测简单 chunk baseline，再只为剩余容量窗口启用 VMM；后者带来映射抖动、回收 deadline 与 TP 下 reserve 稀释。`arXiv:2608.23658v1` 的负结果和机制只覆盖作者 runtime/hardware，不能外推统一阈值。

<!-- source-family:SF-2026-ARXIV-2608-23658 -->

### Storage-backed Inference 需要可证伪的资源证书

把模型或状态放到 storage-backed memory 时，逻辑 representation、语义 demand、scheduler request 与物理 traffic 不能混成一个“内存使用量”。Resource owner 应分别声明 RSS、page cache、board-wide memory 与 I/O authority；异步复用还要记录可保证 output exactness 的 horizon、fault cell 与失效回退。这样能区分“数据存在”“被请求”“真正传输”和“在限定 horizon 内等价”，代价是跨层 accounting 与更复杂发布证书；状态小或完全常驻时，普通 HBM accounting 仍足够。`arXiv:2608.23805v1` 只在作者单一主实验模型、设备与 64-token/logit/route horizon 上支持该机制，不证明 recurrent/upstream state 全局等价。

<!-- source-family:SF-2026-ARXIV-2608-23805 -->

## 硬件升级不是最终答案

### 从单设备 HBM 到异构近数据与池化状态

当瓶颈来自稀疏 attention 的 KV/index 访问或大量 LoRA adapter，而不是主模型 dense GEMM，把所有状态继续塞进 GPU HBM 会让容量和带宽一起竞争。异构分支可以把可分离的检索/索引工作下沉到 processing-near-memory，或把低复用 adapter 放入 CXL pooled memory 并在 near-data side 完成部分计算：

```text
GPU-owned dense state
→ classify latency-critical vs capacity-dominant state
→ place sparse/index/adapter state near pooled memory
→ microbatch, rebalance and overlap transfer
→ account end-to-end latency, energy and failure
```

它用新设备、NUMA/互联、模拟器校准和一致性协议换取 HBM 容量；收益只在目标访问稀疏、传输可隐藏且池端算子足够稳定时成立。普通 GPU、host offload 或 replication 在规模较小、链路拥塞、故障恢复要求高或硬件生态不成熟时仍更可靠。平台必须把 pooled-state owner、版本、location 与可见性写入同一 artifact/runtime contract。

#### Persistent Near-memory：容量层不再只是 Offload 终点

传统 host/NVMe offload 把容量层视为等待搬回 HBM 的冷存储，这在硬件通用、写入频繁或低并发时很合理；但当
模型权重和长生命周期 KV 的容量开始限制可接纳 batch，单纯扩大 offload 容量并不能消除传输边界。一个更激进、
仍处于实验阶段的分支，是让高带宽 persistent medium 靠近 accelerator，并用局部 SRAM、plane-level layout 与
prefetch 把它变成执行数据源，而不只是离线仓库：

```text
HBM-only residency
→ conventional host / storage offload
→ persistent near-memory pages + local execution cache
→ layout-aware parallel reads and prefetch
→ SLO-bounded capacity expansion
```

这里必须分开两种 owner：persistent tier 拥有 versioned weight/KV page 与 logical-to-physical mapping，HBM/SRAM
只是 execution cache。Mapping 或 placement 更新在 commit 前必须保留可读的旧地址；kernel 只消费当前 mapping，
不能反向拥有持久化语义。平台还要把 page layout、prefetch revision、endurance、write amplification、fault recovery、
request isolation 与 fallback bandwidth 写进同一合同。

收益是更大的可执行容量，代价则是新封装/控制器、异构恢复与技术假设。模拟器可以证明设计在假设参数下有可能，
不能证明尚未制造硬件的 yield、耐久性、可靠性或 production tail。Hot mutable state、严格 latency、写密集 workload
或缺少专用硬件时，HBM 与传统 offload 仍是更稳健的分支。

新的 GPU generation、低精度格式、高速互联和 memory hierarchy 会显著改变可行边界：更高算力、更大 HBM、更快互联、更低精度 tensor core，都会推动系统设计变化。具体型号与规格变化很快，不应成为本章的稳定主线。

但硬件升级不会消除系统问题。参数规模、上下文长度和并发需求也会继续增长。新的 FP4/FP8 能力需要软件栈、kernel、量化策略和质量评估配合。

所以正确的结论不是“等硬件变强”，而是“软硬件协同”。硬件给出新的约束和机会，runtime 必须重新组织计算、内存和调度。

## Trade-off

显存优化本质是 trade-off：

- 分片减少单卡显存，但增加通信。
- 重计算减少 activation 保存，但增加算力。
- 分页减少碎片，但增加 indirection 和 kernel 复杂度。
- offload 扩展容量，但引入 PCIe / network latency。
- 量化降低带宽和容量压力，但可能影响质量。
- 稀疏化减少访问量，但需要选择策略和精度验证。

没有一种策略永远最好。系统设计必须根据 workload、模型结构、硬件拓扑和服务目标选择组合。

显存优化首先要建立 workload-aware memory breakdown：从总容量扣除 weights、runtime reserve、workspace 与
communication buffers，得到真正可供动态 state 使用的 usable HBM，再比较 KV、batch 和 offload policy。标称容量
或单个优化名称不能直接推出可接纳并发；具体硬件只用于校验这条推导，不能成为长期假设。

### Embedding Hot Cache 与 KV Cache 竞争同一块 HBM

传统规划常把 embedding lookup 与 KV cache 分给两个独立 owner，但二者最终争用同一 HBM capacity 与 bandwidth。请求分布变化时，扩大 hot embedding cache 可能减少 lookup，却挤压 KV、增加 eviction 与 recompute；反向扩大 KV 又可能放大 embedding miss。更完整的 controller 要以请求 mix、sequence length 和 tail-latency SLO 联合分配，并让 allocation decision 带版本与观测窗口。

联合控制提高整体利用率，却增加预测误差和跨组件抖动。命中率或长度分布失真时，应回退到静态 reservation 或硬水位，避免两个 cache 相互驱逐。独立配额在 workload 稳定、隔离优先时仍然合理。

<!-- source-family:SF-WHEN-KV-MEETS-EMBEDDINGS-DYNAMIC-GPU-MEMORY-ALLOCATION-FOR-ACCELERATING- -->

## Physical Layout 与 Accessor View 可以分离

同一 tensor 在 prefill、decode 或 MoE routing 阶段可能由不同设备访问。重复维护多份布局会增加同步和容量，单一布局又可能不适合所有 accessor。一个折中是保存一份 physical object，通过 address translation 为 NPU、PIM 或不同 kernel 提供 logical view；translation 只改变访问视图，不拥有 tensor truth。

这类原型增加映射表和一致性成本，且可能被转换开销抵消。是否采用必须绑定实际设备、phase 与 workload，普通 GPU-only 路径仍可使用直接布局。

<!-- source-family: arxiv:2608.06989v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: physical-layout-logical-accessor-separation -->

启动路径还需要区分“字节已读取”与“权重已可执行”。Load-ready state 应原子绑定 artifact layout、连续可导出的 tensor address space、remote mapping lifetime、communicator readiness 与 clone completion；任一分量未提交，都不能让 scheduler 把 replica 标为 ready。预先布局和远端映射可减少碎片、串行 clone 与重复加载，却增加 fabric 依赖、地址生命周期和恢复复杂度；不支持相应互连或映射语义时，普通 loader/NCCL 初始化仍是可靠 fallback。

<!-- source-family: arxiv:2608.08482v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: load-ready-weight-state-atomic-commit -->

## Expert Cache 的结论依赖 Replay Methodology

缓存策略比较只有在 fused event 保持原子、workload 未被模板污染、capacity regime 按层归一化时才可复现。错误的 replay 顺序或回收手段会改变 hit path，甚至反转 LRU 与其他策略排名；offline oracle 也不等于可实现上界。评测因此要冻结 event semantics、reclaim mechanism、warm state 和容量，而不是只报告命中率。

<!-- source-family: arxiv:2608.07911v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: expert-cache-replay-methodology-contract -->

## 模型持续大于显存时，预取对象可以从 Tensor 缩到 Row Delta

传统 offload 在每层搬运完整 tensor；动态稀疏模型只激活少量 neuron，且相邻 token 的 active set 常有重叠。若 GPU 保留当前 resident rows，预测器只需从 storage 预取下一 token 新增的差集，从 whole-tensor streaming 演进为 sparse-row delta movement。

预测器只拥有 prefetch hint，真实 activation 决定 correctness；miss 会重新暴露随机 I/O stall，低 locality 还会让细粒度读取比顺序搬运更差。dense model、短序列或 host bandwidth 充足时，传统 offload 仍更简单。收益必须绑定稀疏度、storage path、缓存命中与预测开销。

## 本章在知识树中的位置

```text
模型规模 / 长上下文
→ GPU Memory
→ FlashAttention / ZeRO / PagedAttention / ShadowKV
→ PD 分离
→ GPU Scheduler / Cost
```

GPU Memory 是连接模型、训练、推理和平台成本的核心节点。

沿 Memory 横线，第 19、45 章定义 KV bytes 的来源与生命周期，第 47 章改变逻辑到物理 block 的映射，本章统一 weights、KV、workspace、communication 与 reserve 的 HBM budget；第 55 章再判断是否值得把 state 移到另一个 pool。沿 Compute 横线，本章只是 execution plan 的物理可行性约束，不是新的计算阶段。

### Chiplet Locality 需要 Layout 与 Placement 共同拥有

在 chiplet GPU 上，global address space 连续不代表访问落在本地 HBM。GEMM tile 若跨 chiplet interleave，CTA affinity 也无法阻止 remote traffic；因此 compiler/runtime 需要让 chiplet-local tile 在地址上连续，并让 page-granularity placement 与 CTA mapping 使用同一 locality contract。

布局变换减少 remote HBM traffic，却要求额外重排、静态 shape 信息与硬件 interleave knowledge；非 GEMM、动态 shape 或不同 interleave policy 下不保证收益。普通统一布局在可移植性和小工作负载上仍更简单。

### Long-context State 可以形成多级 Byte-addressable Tier

HBM 不足时，KV 与其他可预测状态不只在 GPU/host 间二选一，还可跨 host DRAM、CXL-hybrid memory 与 NVMe 形成 byte-addressable tier，并利用 model-weight 或 prefix access 的可预测性做 multi-tier DMA prefetch。另一条 I/O 分支把多 DRAM/SSD 汇成 bandwidth-weighted pool，以 user-space SPDK 避免单 host/filesystem 串行瓶颈。

扩容降低 HBM pressure 和 blocked I/O，却新增 prefetch miss、fabric contention、allocator metadata、failure recovery、SPDK 运维与硬件成本。访问不可预测、Context 短或状态可常驻 HBM 时，普通 paging 仍是更稳健的基线。

### MoE Expert Staging 可以消费时序与跨层激活相关性

Expert 完全常驻 HBM 最稳健但容量昂贵；按 router 结果再加载不会误取，却可能让权重 I/O 落在 critical path。一个中间分支利用相邻 token 和相邻层的 expert activation correlation，在 router 最终决定前预取高概率 expert，同时不改变 router 本身的选择权。Memory manager 只管理 residency proposal，模型路由仍决定实际执行。

Prefetch 以额外带宽、staging capacity 和错误加载换取潜在 stall reduction；相关性随模型、层和 workload 漂移，错误预测还会挤出真正需要的 expert。带宽紧张、命中率不稳定或模型较小时，on-demand loading 或更高常驻比例仍更可预测。

### Lossless Weight Compression 需要与 GEMM Tiling 联合调度

Bit-exact entropy coding 可以降低权重存储，却会在执行时引入 decode bandwidth 和状态。只有 tile-level ANS decode 与 GEMM tiling、prefetch 和 weight residency 使用同一 plan，解压才可能隐藏在计算流水中；高熵 tensor 收益很小，decode 甚至会成为新瓶颈。

这条分支不改变模型质量，但增加格式、kernel 与恢复复杂度。Batch、shape、模型和 GPU 改变后必须重新测量，普通未压缩或低比特量化权重仍是更简单的可共存选择。


### 新证据如何改变本章的设计边界

<!-- body-source:SF-2026-ARXIV-2606-21023 -->
**Demystifying Numerical Instability in LLM Inference: Achieving Reproducible Inference for Mission-Critical Tasks with HEAL 所揭示的约束变化。** 异构 GPU 上 greedy decode 仍会因 kernel-boundary downcast 累积而翻转；HEAL 用 INT16 Q/K/V 与双 16-bit GEMM 误差补偿换取接近 FP32 的功能复现性。这条路径只在 exact-v1 披露的任务与系统边界内成立；`arXiv:2606.21023v1 §6 Conclusion; Appendix B error, flip-rate and truncation studies` 记录了未证明范围。硬件、精度或 kernel identity 不匹配时回退到已验证精度路径并重新测量 memory/latency；原有简单路径在其假设成立时继续共存。

## 从机制演进到系统设计

GPU memory 优化从单一 HBM 容量规划演进到 locality、tiering、compression 与异构 device 的联合执行。Weights、KV、workspace 和 communication buffer具有不同可预测性与生命周期：chiplet placement 要与 layout 协同，长状态可以下沉 DRAM/CXL/NVMe，MoE weights 可按激活相关性 staging，压缩格式则必须与 GEMM tiling共同调度。

每减少一类常驻 bytes，通常都会增加 prefetch miss、decode bandwidth、remote access、metadata 或质量回退。低比特甚至可能通过更多 reasoning tokens 抬高总成本，因此验收单位应是完成请求/任务所需的峰值 memory、latency、energy 和 output quality，而不是单个 tensor 的压缩比。状态不可预测或迁移成本主导时，常驻 HBM 与未压缩布局仍更可靠。

## 自检问题

1. 为什么显存墙不等于单纯“显存容量不够”？
2. 训练和推理中显存主要分别被什么占用？
3. KV Cache 为什么让推理显存成为动态问题？
4. FlashAttention 为什么可以看作 memory hierarchy 优化？
5. Fixed、request-dynamic 与 step-peak memory 为什么要分开？
6. Reserve 为什么不是简单浪费？
7. offload、分页、量化分别交换了什么成本？
8. 为什么总 HBM 的倍率不等于 KV capacity 或 request concurrency 的倍率？
9. Hardware specification、compatibility test 与 Serving benchmark 分别能支持什么结论？
10. 为什么 expert paging 只能复用 tiling 的 IO-aware 原则，不能像 online softmax 一样消除所选 Expert 的权重读取？

### 模型大于内存时，Storage 成为显式权重层级

量化和 offload 通常仍假定压缩后存在一个可容纳模型的预算；当模型始终大于可驻留内存时，存储读取进入每 token 关键路径。利用相邻 token 的稀疏激活局部性，只预取新出现的权重行，可以把 OS demand paging 改为模型感知的 delta movement。收益依赖预测准确率、NVMe 延迟和 buffer 命中率；预测器成本、误取放大和缺页回退必须与权重精度一起计入执行计划。
<!-- source-family: arxiv:2608.22643v1; semantic-body-binding: storage-backed-delta-weight-prefetch -->

### Recurrent State 的量化误差会递归反馈

权重通常量化一次后重复读取，KV state 也多为写入后只读；recurrent state 却会经历 quantize、read、update、write 的循环，当前误差会成为下一步输入。它的 precision identity 因此要同时约束单步 error energy 与误差随时间的 decay / amplification，而不能沿用静态张量的平均量化误差。低比特状态仍可节省带宽，但必须在目标序列长度上验证稳定性，并保留高精度重置或 checkpoint。
<!-- source-family: arxiv:2608.27513v1; semantic-body-binding: recurrent-state-quantization-feedback -->

## 小结

Inference memory budget 是 Part V 所有机制的共同约束。Weights 决定固定底座，KV 决定随请求增长的容量，workspace 与 communication 决定瞬时峰值，fragmentation 和 reserve 决定逻辑公式与实际可分配空间的差距。

下一章讨论 PD 分离：当 Prefill 与 Decode 被放入不同 GPU pools，显存和计算压力可以独立规划，但 KV state 必须付出跨池移动成本。

#### 端侧 NPU 只有全链迁移才构成新的 Memory/Energy 分支

把单个 embedding 或 generation operator 放到 NPU，不能证明端侧 RAG 的系统收益，因为 reranking、跨设备搬运、模型加载和 host orchestration 仍可能占据主要内存、延迟与能耗。更完整的 contract 要把 embedding、reranking 与 generation 作为同一条 NPU-resident path 测量，并把加载顺序、static-graph 约束、context bound 与整机 energy/latency 一起纳入 owner。是否使用 NPU 因而是全链驻留与生命周期决策，不是算子级布尔值。

GPU、CPU 和 hybrid execution 仍与之共存；dynamic shape、超长上下文、模型不受支持或内存峰值超限时，hybrid path 可能更稳健。现有证据仅来自 Snapdragon X Elite 单机和 120-query corpus，不能外推其他 NPU 或线上多租户容量；迁移不完整时，新增 device transfer 还可能抵消节能收益。

## Review notes

- mzCache（Status: Experimental）：[arXiv:2609.01338v1](https://arxiv.org/html/2609.01338v1) 的 Android/Adreno 实验支持 UMA 共享 RAM 下的容量核算与可部分恢复分支；压缩仍占 RAM，恢复依赖 buffer readiness。实验不保证任意外部压力下进程存活或零等待，固定 profile 还受热降频影响；不将混合 kernel/allocation/overlap 收益全部归因驱逐策略。

- Multi-Turn LLM Conversations under the Least-Recently-Used Policy（Status: Experimental）：[arXiv:2609.02027v1](https://arxiv.org/html/2609.02027v1)。whole-content LRU 的 mean-field 分解与实践近似区分可复用工作量上限和容量留存；不把 block-work ratio 写成 request hit rate。实测绑定 Qwen3-8B BF16、1P/4D Ascend 配置及作者 trace；partial-tail 修正、负载相关等待、截断观察和后验分布拟合限制外推。没有生产 SLO 或任意缓存实现的保证。

- `SF-2026-ARXIV-2602-00328`（Status: Experimental）：exact-v1 支持将 peer GPU spare HBM 作为可撤销 cache tier 以及作者双 GPU NVLink 实验；证据不覆盖 NVSwitch、并发 model-parallel traffic、多租户隔离、生产 tail latency 或所有模型均自然产生可用余量。https://arxiv.org/html/2602.00328v1

- `SF-2026-ARXIV-2606-21023` — primary `arXiv:2606.21023v1`；Method=`arXiv:2606.21023v1 §2.3 The Microscopic Origin: Boundary Truncation; §3 HEAL; Appendix C HEAL Implementation`；Evaluation=`arXiv:2606.21023v1 §4 Evaluation; Appendix A Detailed Experimental Setup; Appendix D Additional Performance Results; Appendix E MCR-Bench`；Non-proof=`arXiv:2606.21023v1 §6 Conclusion; Appendix B error, flip-rate and truncation studies`；Artifact=`Not Disclosed — no later artifact used`。

- Tile-scheduled lossless weight compression（arXiv:2606.15789v1；Status: Experimental）：支持 ANS decode 与 GEMM tiling/residency 联合；结果绑定 Qwen/Mixtral、SGLang、batch 和作者 GPU。https://arxiv.org/html/2606.15789v1

- Spatiotemporal MoE expert staging（arXiv:2606.15453v1；Status: Experimental）：支持利用跨层与相邻 token 激活相关性预取 expert，且不改变 router；证据绑定作者模型、硬件和 workload，不证明生产命中率或 SLO。https://arxiv.org/html/2606.15453v1

- Chiplet-contiguous GEMM layout（arXiv:2606.11718v1；Status: Experimental）：收益绑定论文 chiplet/interleave、GEMM shape 与 runtime；论文无独立 limitations section，不外推到非 GEMM 或动态 shape。https://arxiv.org/html/2606.11718v1
- CXL-Hybrid long-context memory（arXiv:2606.12556v1；Status: Experimental）：多级 byte-addressable tier 与 ITME prefetch 只在测试拓扑和可预测访问下成立，不证明所有 KV access 都可隐藏。https://arxiv.org/html/2606.12556v1
- Pooled DRAM/SSD KV offload（arXiv:2606.14779v1；Status: Experimental）：bandwidth-weighted pool 与 SPDK passthrough 降低串行 I/O；不消除 allocator、failure recovery 和运维成本。https://arxiv.org/html/2606.14779v1

- End-to-end NPU RAG（arXiv:2606.11257v1；Status: Experimental）：把 embedding/reranking/generation 全链驻留与整机 energy/memory 作为独立分支；结论限定 Snapdragon X Elite 单机与 120-query corpus。https://arxiv.org/html/2606.11257v1

### 低比特收益还取决于同一 SM 内的 Compute Balance

低精度先减少 weight/activation footprint 与 memory traffic，但 W4A4 kernel 若让 Tensor Core 与 CUDA Core 工作失衡，理论 bit reduction 不会自动变成 throughput。Kernel owner 需要同时记录 quantization artifact、dequant/packing path、SM work mapping 与目标 batch regime；memory planner 只能消费经过质量 Gate 且有可执行 kernel 的 committed precision。

纯 W4A4 用更复杂的 intra-SM mapping 换高 batch 吞吐；低 batch、不同 GPU 或 kernel 未覆盖时，FP16、W4A16、W4A8 或 mixed fallback 仍合理。作者观察到 A100 在 batch≥64 才恢复优势，说明 benchmark batch 不能被误写为并发 SLO。Ch54 拥有 precision-residency identity，Ch49 拥有 runtime integration，Ch56 拥有 continuous batching 与请求调度。

- APEX4（arXiv:2606.08761v1；Status: Experimental）：证据绑定 A100-40G、RTX 3090、A40、L40S，LLaMA-2/3、Qwen2.5，WikiText-2/zero-shot/kernel/vLLM tests，batch sweep 至 256；不披露 external request concurrency 或 production SLO，也不证明所有 GPU 代际都应采用纯 W4A4。https://arxiv.org/html/2606.08761v1

- HiKV（arXiv:2607.22389v1；Status: Experimental）：https://arxiv.org/html/2607.22389v1
  - 证据边界：支持四个披露模型/任务、`<=1%` paper calibration 与 modeled TSMC 16nm accelerator 下的 token×element hierarchical selection；不证明 commercial GPU、生产并发/SLO 或 exact-attention 下的等效收益。

- KARAT（retrieval-sparse attention 的 PNM placement；Status: Experimental）: https://arxiv.org/abs/2608.03555
- PLoRA（CXL pooled memory + near-data multi-LoRA serving；Status: Experimental）: https://arxiv.org/abs/2608.05483

- Evidence boundary：MI455X capacity case 只验证“先扣固定成本，再比较动态容量”的推导；它不是本章的
  长期硬件假设，也不承担通用性能结论。

Primary-source 校验入口：

- FlashAttention: https://arxiv.org/abs/2205.14135
- FlashAttention-3: https://arxiv.org/abs/2407.08608
- ShadowKV: https://arxiv.org/abs/2410.21465
- PagedAttention / vLLM: https://arxiv.org/abs/2309.06180
- Hugging Face, "Hugging Face on AMD Instinct MI455X: First Transformers Results": https://huggingface.co/blog/badaoui/transformers-on-amd-mi455
- AMD Instinct MI455X official specifications: https://www.amd.com/en/products/accelerators/instinct/mi400/mi455x.html
- NVIDIA Vera Rubin platform announcement（版本化 POD co-design evidence）:
  https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer
- vLLM incremental MoE expert offloading PR #37190（Status: Experimental / open PR）:
  https://github.com/vllm-project/vllm/pull/37190

后续定稿时，任何具体 GPU 性能倍数、显存容量、模型规模和成本数字都必须重新查官方规格或论文来源。

- FlashAccel（persistent near-memory HBF co-design；Status: Experimental；端到端结果来自模拟器而非 fabricated hardware）：
  https://arxiv.org/abs/2607.10186v1
- PagedWeight（bit-plane weight pages、desired/committed precision 与 KV pressure；Status: Experimental）:
  https://arxiv.org/abs/2607.16184v1

### Daily integration evidence trace

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24506: `arXiv:2606.24506v1`; exact-v1 URL=`https://arxiv.org/html/2606.24506v1`; Method=`https://arxiv.org/html/2606.24506v1 — §3 CrossPool Design; KV Planner; Layer-wise Scheduler; Control Lowering`; Evaluation=`https://arxiv.org/html/2606.24506v1 — §5 Experiments; Context Scalability; Overall Performance`; Non-proof=`证据聚焦冷模型、低并发与给定 context/model mix；热点突发、跨租户 isolation、模型装载故障和高并发下 shared-pool contention 未证明，应能回退 dedicated allocation。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25285**：Primary `arXiv:2606.25285v1`；Method `https://arxiv.org/html/2606.25285v1 — §3 EPTS: Elastic Post-Training Sparsity`；Evaluation `https://arxiv.org/html/2606.25285v1 — §4 Experiments; Experimental Setup; Main Results`；未证明边界 `https://arxiv.org/html/2606.25285v1 — §Limitations and Discussion`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25519**：Primary `arXiv:2606.25519v1`；Method `https://arxiv.org/html/2606.25519v1 — §3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy`；Evaluation `https://arxiv.org/html/2606.25519v1 — §D Additional evaluation details; D.1 Benchmarks and evaluation protocol`；未证明边界 `https://arxiv.org/html/2606.25519v1 — §7 Can We Reduce Reasoning-Token Inflation; D.2 Model details`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26488**：Primary `arXiv:2606.26488v1`；Method `https://arxiv.org/html/2606.26488v1 — §Compression of recursive reasoners across precision, pruning, distillation and attention variants`；Evaluation `https://arxiv.org/html/2606.26488v1 — §Three tasks and two recursive architectures; local vs puzzle-exact accuracy`；未证明边界 `https://arxiv.org/html/2606.26488v1 — §Edge recursive models only; token-level preservation does not imply global-reasoning preservation`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Source-family integration record

<!-- recovered-daily-20260624:INFER-GPU-MEMORY:start -->
### 2026-06-24 evidence integration — INFER-GPU-MEMORY

相邻章 `books/part-05-inference-system/55-pd-disaggregation.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24506**：冷 MoE serving 将 stable weights 与 demand-driven KV 拆成独立资源池；planner virtualize shared KV，layer-wise scheduler/persistent kernel 只激活所需 weights 和 KV heads。 证据聚焦冷模型、低并发与给定 context/model mix；热点突发、跨租户 isolation、模型装载故障和高并发下 shared-pool contention 未证明，应能回退 dedicated allocation。

<!-- recovered-daily-20260624:INFER-GPU-MEMORY:end -->

<!-- recovered-daily-20260625:INFER-GPU-MEMORY:start -->
### 2026-06-25 evidence integration — INFER-GPU-MEMORY

- **SF-2026-ARXIV-2606-25285**：`3 EPTS: Elastic Post-Training Sparsity` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Limitations and Discussion` 是 `EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; Experimental Setup; Main Results` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25519**：`3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `7 Can We Reduce Reasoning-Token Inflation; D.2 Model details` 是 `Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models` 的 source-specific 反例/局限边界；若运行条件离开 `D Additional evaluation details; D.1 Benchmarks and evaluation protocol` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26488**：`Compression of recursive reasoners across precision, pruning, distillation and attention variants` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Edge recursive models only; token-level preservation does not imply global-reasoning preservation` 是 `What Survives When You Compress a Recursive Reasoner for the Edge?` 的 source-specific 反例/局限边界；若运行条件离开 `Three tasks and two recursive architectures; local vs puzzle-exact accuracy` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:INFER-GPU-MEMORY:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-23001:start -->
- `SF-2026-ARXIV-2606-23001` — Daily `2026-06-23`；primary `arXiv:2606.23001v1`；Books review `books-review:SF-2026-ARXIV-2606-23001`。

  **已吸收的语义增量：** EnerInfer: Energy-Aware On-Device LLM Inference 的 exact-v1 机制为：To address these challenges, we propose EnerInfer, the first on-device LLM inference framework that jointly manages energy efficiency, throughput, and thermal comfort for LLM workloads. 因此 把设备频率、功耗/温度估计、QoE 和模型/backend identity 联合验收。
<!-- daily-books-trace:SF-2026-ARXIV-2606-23001:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-08761:start -->
- `SF-2026-ARXIV-2606-08761` — Daily `2026-06-08`；primary `arXiv:2606.08761v1`；Books review `books-review:SF-2026-ARXIV-2606-08761`。

  **已吸收的语义增量：** APEX4 把 W4A4 的瓶颈定位到同一 SM 内 Tensor Core 与 CUDA Core 的 compute imbalance，并用 kernel mapping 避免 mixed-precision fallback。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08761:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11257:start -->
- `SF-2026-ARXIV-2606-11257` — Daily `2026-06-10`；primary `arXiv:2606.11257v1`；Books review `books-review:SF-2026-ARXIV-2606-11257`。

  **已吸收的语义增量：** 在 GPU Memory 章节补一个端侧 NPU 的全链 RAG memory/energy 分支，限定 Snapdragon X Elite、120-query 与单机测量，禁止外推其他 NPU。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11257:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11718:start -->
- `SF-2026-ARXIV-2606-11718` — Daily `2026-06-11`；primary `arXiv:2606.11718v1`；Books review `books-review:SF-2026-ARXIV-2606-11718`。

  **已吸收的语义增量：** Chiplet GPU 的 GEMM locality 需要让 chiplet-local tiles 在 global address space 连续，使 page-granularity placement 与 CTA affinity 一致。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11718:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-12556:start -->
- `SF-2026-ARXIV-2606-12556` — Daily `2026-06-11`；primary `arXiv:2606.12556v1`；Books review `books-review:SF-2026-ARXIV-2606-12556`。

  **已吸收的语义增量：** 长 context state 可跨 GPU/host/CXL-hybrid/NVMe 构成 byte-addressable tier，并利用 model-weight/prefix access 可预测性做 multi-tier DMA prefetch。
<!-- daily-books-trace:SF-2026-ARXIV-2606-12556:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14779:start -->
- `SF-2026-ARXIV-2606-14779` — Daily `2026-06-11`；primary `arXiv:2606.14779v1`；Books review `books-review:SF-2026-ARXIV-2606-14779`。

  **已吸收的语义增量：** KV offload 不应串行穿过单 host/SSD；应把多 DRAM/SSD 汇成 bandwidth-weighted pool，并以 user-space SPDK bypass filesystem。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14779:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15453:start -->
- `SF-2026-ARXIV-2606-15453` — Daily `2026-06-14`；primary `arXiv:2606.15453v1`；Books review `books-review:SF-2026-ARXIV-2606-15453`。

  **已吸收的语义增量：** MoE expert staging 可利用跨层与相邻 token 的 activation correlation 预取，并保持原 router 决策不变。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15453:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15789:start -->
- `SF-2026-ARXIV-2606-15789` — Daily `2026-06-15`；primary `arXiv:2606.15789v1`；Books review `books-review:SF-2026-ARXIV-2606-15789`。

  **已吸收的语义增量：** lossless weight compression要让tile-level ANS decode与GEMM tiling/weight residency联合调度，bit-exact减存储但新增decode bandwidth与kernel state
<!-- daily-books-trace:SF-2026-ARXIV-2606-15789:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-22283:start -->
- `SF-2026-ARXIV-2606-22283` — Daily `2026-06-21`；primary `arXiv:2606.22283v1`；Books review `books-review:SF-2026-ARXIV-2606-22283`。

  **已吸收的语义增量：** 对 ANE 的 datapath、roofline、compiler/on-disk format、weight compression、driver/firmware command protocol建立 measured/decompile-derived/predicted 三类 claim，并区分 direct private route 与 Core ML supported path。
<!-- daily-books-trace:SF-2026-ARXIV-2606-22283:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-10186:start -->
- `SF-2026-ARXIV-2607-10186` — Daily `2026-07-12`；primary `arXiv:2607.10186v1`；Books review `books-review:SF-2026-ARXIV-2607-10186`。

  **已吸收的语义增量：** 新增证据边界：Co-design an HBF stack and GPU attachment, distribute small SRAM buffers close to flash planes, map weights and KV into layouts that expose plane-level parallelism, prefetch future pages without stalling dependent kernels, and use an HBF-aware storage/programming layer to coordinate persistent and HBM/SRAM state. Capacity permits larger SLO-bounded batches; bandwidth and page latency remain the limiting constraints. 该 delta 已进入 `books/part-05-inference-system/54-gpu-memory.md#L262`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-10186:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-16184:start -->
- `SF-2026-ARXIV-2607-16184` — Daily `2026-07-18`；primary `arXiv:2607.16184v1`；Books review `books-review:SF-2026-ARXIV-2607-16184`。

  **已吸收的语义增量：** 新增证据边界：Weights and KV compete for the same HBM budget, so MoE weight precision can become mutable runtime state. A safe page table must commit lower precision before freeing pages and restore pages before committing higher precision; planner identity and per-request quality policy become part of serving correctness. 该 delta 已进入 `books/part-05-inference-system/54-gpu-memory.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-16184:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-22389:start -->
- `SF-2026-ARXIV-2607-22389` — Daily `2026-07-25`；primary `arXiv:2607.22389v1`；Books review `books-review:SF-2026-ARXIV-2607-22389`。

  **已吸收的语义增量：** 新增证据边界：Hierarchical token and element selection exposes intra-token vector fetch as a second KV bandwidth floor and co-designs ranking state with a reconfigurable sorter. 该 delta 已进入 `books/part-05-inference-system/54-gpu-memory.md#L188`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-22389:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-03555:start -->
- `SF-2026-ARXIV-2608-03555` — Daily `2026-08-05`；primary `arXiv:2608.03555v1`；Books review `books-review:SF-2026-ARXIV-2608-03555`。

  **已吸收的语义增量：** KARAT 将 retrieval sparse attention 的 KV/index 工作放到 PNM，并用 microbatch、重平衡和 configuration search 协调 GPU 与近存计算。作者在三种模型与 agent traces 上报告吞吐/TDP，但收益依赖 PNM 设备和模拟/原型合同，不能外推到普通 GPU fleet。
<!-- daily-books-trace:SF-2026-ARXIV-2608-03555:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-05483:start -->
- `SF-2026-ARXIV-2608-05483` — Daily `2026-08-07`；primary `arXiv:2608.05483v1`；Books review `books-review:SF-2026-ARXIV-2608-05483`。

  **已吸收的语义增量：** PLoRA 用 CXL pooled memory 与 near-data processing 承担多 LoRA 状态，把单 GPU 显存约束转成池化容量与传输/计算协同。系统管理器和模拟器由真实硬件校准，但主要结论仍受 H100 与四设备配置约束。
<!-- daily-books-trace:SF-2026-ARXIV-2608-05483:end -->
