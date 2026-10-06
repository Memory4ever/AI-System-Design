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

因此单一的 “SM utilization” 也不能证明模型已经把 GPU 用满。Decode 的小行 GEMM 可能触发了 Hopper 的矩阵指令，却只填充固定 64-row fragment 的少量有效行；同一个高利用率数字还会混合 fragment fill、occupancy、stall、wave quantization 与 kernel selection。诊断必须从原始 counter 和明确公式分别重建这些机制，并按 Prefill/Decode、batch、sequence、kernel role 与精度分片，否则容量不足、带宽受限和形状浪费会被误写成同一种“算力饱和”。

更细的计数器提高归因能力，却增加 profiler replay、采样扰动与硬件代际耦合；业务 SLO 仍须由端到端 trace 验收。H100 NVL、FlashAttention-3、cuBLASLt 和受测四类模型只支持该测量分解，不提供跨 GPU 或跨 runtime 的通用阈值。<!-- source-family:SF-2026-ARXIV-2609-12923 -->

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

在 weights、KV 与峰值空间已经满足上述容量约束之后，硬件还可能以容量换单位容量带宽。传统 HBM 配置常在增加带宽时一起购买更多容量，这对低 batch、反复读取 dense weights 的 decode 可能并不经济；一种受限加速器分支保持外部 interface 的带宽，调整内部 ranks、banks 与 subarrays 的容量配置，使更小的存储容量拥有更高的 BW/Cap。容量是可配置设计变量，不是可以忽略的 admission 条件：减小容量会缩窄可容纳的 batch 和 sequence length，不能由更高 BW/Cap 推出长上下文与高并发也同时最优。<!-- source-family:SF-2026-ARXIV-2602-18568 -->

这条分支用定制 memory、封装与协同设计成本换取特定负载的读取效率；每 GB 成本可能更高，扩展 compute units 后 activation broadcast 又可能成为瓶颈。现有证据主要是 H100 上的负载动机测量、部分 RTL 校验及校准后的 SystemC/HLS 与工艺投影，不是已制造芯片的全模型数值正确性或 serving SLO 验收；不同实验的 FP8 与 W4/A16 协议不能拼成同一端到端对照，整机收益也不能全归于 memory 容量定制。容量、模型精度或成本假设不成立时，保留 commodity HBM、缩小请求或采用既有分层方案，而不是靠带宽承诺放行超容量请求。

## 固定、动态与瞬时占用

容量分析应按生命周期区分：

| 类别 | 典型对象 | 特征 |
| --- | --- | --- |
| Fixed | weights、部分 graph/runtime state | 模型加载后长期驻留 |
| Request-dynamic | KV Cache、adapter state | 随并发与长度增长 |
| Step-peak | activations、logits、workspace、collective buffers | 随 batch shape 与 kernel 瞬时变化 |

只测 idle model memory 会漏掉高峰 workspace；只按最大 KV 填满剩余 HBM，又会让下一次大 Prefill 或 collective 没有工作空间。

瞬时峰也可能随同一请求的迭代状态切换。对每步重新计算双向状态的 masked diffusion LM，若 sampler 只消费 masked positions 的 logits，就可以用 gather-GEMM 直接读取这些位置，避免另建 gather buffer；但 FFN 仍覆盖完整序列，因而 masked-token 比例降低时，主峰可能从 logits 转到 FFN。只有看见完整执行图及其 tensor lifetime，才有资格跨算子复用空间：显式参数化 graph 的 alias 必须匹配实际读写，chunk-loop barrier 还须把输入寿命延长至全部 chunks 消费完。局部 graph break 下的 allocator 观察不能替完整生命周期背书。以当前 mask 数和总 token 数实例化候选计划，再只细分当前 logits 或 FFN 主峰，直到可容纳或遇到不可分块的容量下限；这是可行性启发式，不是所有形状的全局最优。<!-- source-family:SF-2026-ARXIV-2601-06562 -->

计划中的连续 workspace 地址也不等于已经占用相应物理显存。VMM 可以先保留虚拟范围，确定峰值与 tensor offsets 后再绑定物理页；实际 in-place kernels 必须遵循同一 alias、寿命与 barrier 合同。分块增加 kernel launch，图注册、搜索、规划和映射也支付成本；生命周期遗漏或算子写入方式不符会令复用失效，应回退原 allocator/dense execution，而不可分块峰超过容量时须拒绝或缩小请求。当前证据以 dummy input 测最大可容纳长度，不能由此宣布模型语义长上下文能力；单 diffusion-step latency 也不能替完整生成、并发和请求 SLO 验收。原有保守峰值保留在图不可完整验证或净收益不足时仍合理。

### 生命周期还会改变片上 Memory 的保护成本

上述分类不只决定容量何时释放，也可能决定存储保护需要持续多久。普通 SRAM/HBM 路径不要求 runtime 为每类 activation 单独选择刷新策略，因而易于验证；若边缘加速器以高密度 eDRAM 承载 workspace，统一刷新却会对短暂 Q/O 与长期 KV 支付同样的维持成本。一条条件分支同时按 lifetime 和 BF16 bit sensitivity 分银行：sign/exponent 保持标准刷新，短暂 Q/O mantissa 在已校准驻留时间内不刷新，长期 KV mantissa 则采用较宽但有限的刷新间隔。控制器拥有数据映射与刷新策略，模型执行仍须保持数值误差预算；“短命”并不允许同时放松敏感的 sign/exponent。<!-- source-family:SF-2026-ARXIV-2604-07396 -->

它用分银行、bit 重组与硬件耦合换取刷新能耗的减少，并新增驻留时间低估、相关错误及精度格式变化的失效风险。现有证据来自 H100 上的 lifetime 测量、3T cell/DESTINY 模型和 BF16 随机故障注入，而非已制造 NPU 的端到端验证；部分任务准确率仍有微小退步。因而不能把 workspace 刷新收益写成整机能耗、安全或生产质量保证。实际驻留超出校准范围、错误分布不符或硬件不支持分段保护时，统一刷新和原有存储路径仍是更可靠的选择。

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

容量选定后仍要决定**淘汰谁、以什么粒度淘汰**。常见直觉是“计算成本高的长 prefix 应永远压过 LRU”；但同一会话的连续轮次若短期内反复访问，whole-content LRU 可以以极低元数据成本保住活跃前缀。大量一次性前缀会污染它，此时快速降级 one-hit 项有意义；更深的共享树节点重算昂贵，才值得按重算成本选择连续的部分节点。逐块贪心清理虽然看似释放得精确，却可能留下不可复用的碎片。替代策略因此要与 session cadence、prefix-sharing、block layout 一起回放，而不能只比较平均 hit rate；它增加追踪、淘汰与碎片整理开销。两类生产 trace 和一组 H200/vLLM 实验显示优化策略改善作者设置的平均与尾部 TTFT，却同时使中位 TTFT 变差，不能写成普遍优于 LRU。[原始实验与限制](https://arxiv.org/html/2609.28870v1)只支持这些披露条件。
<!-- source-family:SF-2026-ARXIV-2609-28870 -->

<!-- source-family:SF-2026-ARXIV-2609-02027 -->

当请求前缀以页为单位复用、目标是选择达到指定命中率的 KV 容量时，可以用另一条更直接的测量路线：在实际访问流中计算每页的 LRU stack distance，一次 replay 生成多种容量对应的命中曲线，再寻找目标覆盖率的最小 working set。它比对每种候选容量分别部署或模拟更省成本，却只预测所选 LRU 语义和观测 trace 的容量—命中关系；它不替代 prefix identity 校验、请求级 TTFT/SLO 验证，也不能推断未来负载不漂移。KVSET 的作者在内部 coding-agent 请求 trace 上用 SGLang/Mooncake、H20、GLM-5.2 W4A8、FP8 KV 对照实际 cache 部署；这些条件支持该工作集估计器的局部准确性，不是任意 replacement policy 或生产 fleet 的容量保证。<!-- source-family:SF-2026-ARXIV-2609-27746 -->

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

#### 少读 Weight 与少读 KV 的交点

Activation sparsity 和 KV sparsity 都可能减少 decode 读取，但省掉的对象并不随 context 同样增长：batch=1 时 projection 权重读取近似固定，KV 读取随已缓存 token 数增长。因此短 context 更可能受益于少读权重，长 context 更可能受益于少读 KV；batch 增大又会让不同请求的 activation 选择取并集，削弱 weight-read 节省。这个 byte-budget 交点只是起点，还要加入各自 kernel 的固定成本、实际 dtype、layout 和选择开销。完整权重／KV 仍驻留的实现，不能把少读的 bytes 宣称为可分配 HBM 容量。

决定运行分支时，应在同一高效 dense kernel 上测两条 sparse 路径，以相同任务质量预算约束保留率，再计入 scoring、gather 和生成长度带来的摊销；更换低效 dense baseline 会人为放大同一 policy 的收益。[Sparsity Crossover v1 §3–7](https://arxiv.org/html/2609.33889v1)显示固定 window 的小 PPL 差异仍可伴随远距检索失败，选择型策略也有一次构造成本。批量、质量 gate 或输出长度改变时应重测边界，而不是只按 context 长度切换；短输出、稀疏 kernel 开销过大或质量不稳时，保留 dense 读取与简单固定 composition。

<!-- source-family:SF-2026-ARXIV-2609-33889 -->

#### 低比特收益还取决于同一 SM 内的 Compute Balance

低精度先减少 weight/activation footprint 与 memory traffic，但 W4A4 kernel 若让 Tensor Core 与 CUDA Core 工作失衡，理论 bit reduction 不会自动变成 throughput。Kernel owner 需要同时记录 quantization artifact、dequant/packing path、SM work mapping 与目标 batch regime；memory planner 只能消费经过质量 Gate 且有可执行 kernel 的 committed precision。

纯 W4A4 用更复杂的 intra-SM mapping 换高 batch 吞吐；低 batch、不同 GPU 或 kernel 未覆盖时，FP16、W4A16、W4A8 或 mixed fallback 仍合理。作者观察到 A100 在 batch≥64 才恢复优势，说明 benchmark batch 不能被误写为并发 SLO。Ch54 拥有 precision-residency identity，[Ch49](49-tensorrt-llm.md) 拥有 runtime integration，[Ch46](46-continuous-batching.md) 拥有 continuous batching，[Ch56](56-inference-scheduling.md) 拥有跨时间尺度的请求调度。

#### Recurrent State 的量化误差会递归反馈

权重通常量化一次后重复读取，KV state 也多为写入后只读；recurrent state 却会经历 quantize、read、update、write 的循环，当前误差会成为下一步输入。它的 precision identity 因此要同时约束单步 error energy 与误差随时间的 decay / amplification，而不能沿用静态张量的平均量化误差。低比特状态仍可节省带宽，但必须在目标序列长度上验证稳定性，并保留高精度重置或 checkpoint。
<!-- source-family: arxiv:2608.27513v1; semantic-body-binding: recurrent-state-quantization-feedback -->

若在**相同输入与 gates**下，浮点状态按 `S_t=A_t S_(t-1)+B_t` 更新，量化存储引入本步误差 `epsilon_t`，则误差可写为 `E_t=A_t E_(t-1)+epsilon_t`。这使两份平均重构误差相同的状态也可能有不同长期影响：保留时间更长的方向会累积更多误差，被当前 query 强烈读取的方向则更直接影响输出。Temporal calibration 可按近似 lifetime 分配 bit budget，spatial calibration 再按 readout sensitivity 拟合 scale；两者是不同敏感度，不是已经证明普遍最优的统一乘积目标。

时序也改变误差解释。一条实现路径先从上一压缩状态恢复并完成本步浮点更新，再产生当前 readout，最后量化写回下一步状态；当前新增的写回误差于是首先影响下一次更新。Packed codes、scales 和高精度 pivots 必须共同就绪才能被下步读取，后台 writeback 不能只完成其中一部分就宣告 ready，容量还要计双缓冲和元数据。它用校准、解包和同步成本换带宽；gate-only lifetime 是近似，且 token 改变会使未来输入/gates 分叉，上述条件误差关系不是整条生成轨迹的稳定保证。极低位宽、长输出或校准漂移时仍应提高精度或回退未压缩状态；GDN/KDA 的受限实验不证明任意 recurrent 架构都有同样收益。
<!-- source-family:SF-2026-ARXIV-2609-38169 -->

### 提高利用率

Paging、prefix sharing 和更精确 admission 减少预留与碎片，却不改变每个有效 KV element 的逻辑需求。

### 扩展层级

CPU/SSD/off-node cache 扩大总容量，却加入 transfer latency、bandwidth contention 和 consistency。它们把“装不下”改成“何时值得搬”。

若容量层换成 flash，增加容量还会引入有限的 write endurance：短活 activation 和 staging 留在 HBM，长期可复用 KV 才考虑下沉。Cache-aware 排序只改变先服务谁，不约束总 live KV；admission 可以按新请求即将锁住的 footprint 留出 headroom，其中包括已经命中的 prefix，不能把 cache hit 当作容量免费。Decode 仍会继续增长，完成的 session 也会释放锁，因此 admission buffer 是准入压力控制，不是每一时刻都保持不变的物理分区。

此时容量、placement 与 admission 要共同选择：较小 active batch 可能换来较少 cache churn、reload 与 flash 写入，但 HBF hit 不等于 HBM 带宽，吞吐改善也可能伴随更高 mean TPOT。[HBF 的受限 trace 模拟](https://arxiv.org/html/2609.39131v1)使用 B200 计算模型、16-bit 存储与 FP8 index timing proxy；复制 session 不产生独立新轨迹，寿命外推依赖均匀 wear、单位写放大和假定 P/E 次数，未包含完整 controller、静态 package power 或 latency SLO，轻负载能耗还可能变差。真实 endurance 不明、复用低或延迟优先时，HBM/host 仍是合理分支；先核写入流量、迁移与延迟，不用模拟寿命直接作设备或运行保证。<!-- source-family:SF-2026-ARXIV-2609-39131 -->

Host DRAM 的读取也不必一律先落到 GPU HBM：支持相应远端访问和 TMA 的设备，可让某个 operation 从 host 直接搬入 SMEM，绕过 HBM staging。此时应分别选择该 operation 的 offload 比率和最大 inflight 数；省掉中间副本不等于 host 链路无限快，并发太多仍会使远端请求拥塞。完整保留 HBM staging 的路径则在复用高、远端带宽不足或不支持直达时继续合理。<!-- source-family:SF-2026-ARXIV-2604-26074 -->

这个分支增加访问计划、SMEM 生命周期与 host-link 并发控制，受限 piecewise execution-bound 模型不证明一般 greedy 最优。作者 GH200/C2C 与 Blackwell/PCIe 的路径及离线32-token decode 测试不能混成线上尾延迟保证；shape、链路或重用条件失配时，应降低 inflight/offload、恢复 HBM staging，并按完整 operation 时间验收。

当长前缀的 KV 下沉到 NAND，普通块设备先通过 host 内存和文件/块 I/O 取回，即使介质本身变快，接口与 staging 仍可能占据 TTFT。内存语义的设备也不自动消除这段等待：serving engine 知道将消费哪些 KV chunk/层，设备却只看地址与缺页，双方若不交换计划，通用预取可能搬错数据。可选的协同接口让 engine 提交已验证身份的 chunk 与层访问计划，设备负责 NAND→本地 DRAM 的 staging 和完成进度，GPU 仅在对应数据 ready 后消费，并将下一层传输与当前层计算重叠。这样用 device DRAM、计划池和更紧的软硬件耦合换 TTFT；计划过期、布局转换、缺页或设备故障仍必须回退普通加载，不能把 memory-mapped 地址视为已就绪 KV。LM-CXD 的结果来自 CXL-SSD 仿真设备、vLLM/LMCache、L40S 和作者五组模型/前缀长度，并非现货 CXL-SSD、其他 NAND 或 production tail-SLO 的实测保证。<!-- source-family:SF-2026-ARXIV-2609-26828 -->

这里的 CPU 容量层以离散 GPU 与独立 host memory 为前提。在统一内存的移动 SoC 上，CPU 与 GPU 共享同一块物理 RAM，改变访问处理器不会凭空增加容量；压缩 KV 能减少实际占用，但压缩副本仍留在这块 RAM 中，压力继续上升时仍可能需要移到 flash。因而层级设计首先要核实物理容量边界，不能把逻辑上的 CPU/GPU 地址或访问路径重复记为两份空间。

当其他应用可以随时要求回收内存，问题也从固定 offload 比例变成“释放任意一部分后，怎样尽早恢复下一次请求”。细粒度 weight/KV buffer 可以独立释放与恢复，保留较早执行的层，并让 CPU 按后续依赖准备数据；GPU 只消费已就绪的共享 buffer，分配、解压和读取才有机会与计算重叠。收益取决于真实恢复关键路径，代价包括同步、压缩质量、带宽竞争和 profile 随温度或负载漂移；共享地址并不保证无需等待，也不能防止极端压力下进程被终止。内存充足、恢复开销很小或隔离要求更强时，常驻或简单串行恢复仍更可靠。<!-- source-family:SF-2026-ARXIV-2609-01338 -->

#### Peer GPU Spare Memory 是可撤销的中间 Cache Tier

单个模型独占固定 GPU、各卡 HBM 都接近饱和时，memory hierarchy 只需要在本卡 HBM 与 CPU/SSD 之间选择；多 GPU 节点同时承载异构请求后，有些 peer GPU 可能暂时拥有空闲 HBM，且 NVLink 路径比 host offload 更近。cache manager 可以把这些空闲页作为 opportunistic tier，按 model/expert/KV generation 注册 peer residency，并在计算 owner 需要容量或 topology/tenant policy 改变时撤销；canonical weight 或 KV 身份仍由原 owner 持有，peer 只保存可重建副本。

这条层级减少 host transfer，却会与 TP/PP collective、其他租户和 peer compute 争用互联，并新增 remote pointer、revocation、stale generation 与 tail-latency failure。拓扑不明、隔离要求高、peer 压力上升或副本无法及时回收时，应回退本地 HBM/CPU tier。`arXiv:2602.00328v1` 的 exact-v1 只在单机双 GPU NVLink 和作者所列模型/强制 offload 设置中验证 Harvest，不证明 NVSwitch、多租户、并行通信竞争或生产 SLO 下仍有同等收益。

仅把 peer 空闲 HBM 列为 cache tier，还不能保证借出时不损害出借方。若要跨租户弹性共享，资源合同必须同时约束借用者的远端访问成本和出借者的回收权：预先划分有直接链路的 memory slice，依据可预测的层访问提前搬回借入数据，并在出借方负载回升时于安全的请求边界撤销租借。控制器拥有借还、预取与抢占权；应用的 model/KV 身份和已提交状态不因迁移而改变。这个机制可利用分区碎片，但需要暴露部分访问模式、牺牲一部分可用带宽，并可能因两边突发、预取失准或回收引发尾延迟；硬隔离或工作集稳定时，静态分区仍更简单。EMA 的作者证据来自单机 4×A100-40GB/8×A100-80GB、LLaMA/OPT、ShareGPT/Alpaca、vLLM 原型，不能把“性能透明”外推成任意 topology、混合 TP/PP 或生产多租户的保证。<!-- source-family:SF-2026-ARXIV-2609-27040 -->

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

Peer GPU 上的机会性副本仍假设某张卡拥有主要 KV，而其他卡只是临时借用。长上下文 Prefill 使用 Context Parallel、且每个 rank 复制全部层 KV 时，容量压力来自更固定的跨 rank 冗余。另一条条件分支按层指定 KV 持有 rank：计算 rank 在该层 Attention 前取得持有者广播的 KV，只有传输完成、层与请求身份一致，才能消费它。这样把“在哪张卡存这一层”与“哪张卡执行这一层”分开，而不是把所有 rank 的完整 KV 当作并行的必要条件；Indexer 计算可以与下一次广播重叠，但 Indexer Cache 本身也须遵守 load-before-use。<!-- source-family:SF-2026-ZAI-SCALING-PAIN-LAYERSPLIT -->

这一分层用每层通信、同步与持有 rank 的故障/拥塞风险换单卡 KV 容量。智谱在 GLM-5.1、约 90% Prefix Cache 命中和 40k–120k 长度的 Coding Agent Prefill 中报告吞吐提高 10%–132%；其 Indexer 广播约为 KV 的八分之一是该设计与配置的量级，不能当任意 CP 模型的常数，更不能据吞吐推生产 TTFT 尾部保证。上下文较短、命中低、互联弱、rank 故障域难以隔离或广播无法被计算掩盖时，各 rank 保留完整 KV 或使用现有容量层级仍更容易验证。

### Capacity Planning 与 Placement/Prefetch 是两层问题

HBM/CPU/SSD tiering 先要按 session lifetime 与工作集判断各 tier 容量是否足够，再依据 recency、reuse frequency、link bandwidth 与 TTFT objective 决定块放在哪里、何时预取。只有存在可用带宽且预测命中时，prefetch 才是收益；capacity 不满足时，二阶 placement 优化不能掩盖根本缺口。<!-- source-family:SF-2026-ARXIV-2609-16215 -->

更细 placement 增加 metadata、预测错误和迁移流量。capacity 主导、workload 不稳定或 link model 不可信时，简单 recency/静态 tier 更可靠；作者 synthetic、batch=1、single-GPU simulator 不证明生产排序。

多进程超额申请显存时，allocator 的预留量也不等于下一次执行的真实 working set。若 scheduler 已知 task 的切换时间线，kernel 的访存模式又可由离线 profile 表达为 fixed、linear 或 strided launch-argument 模板，memory manager 可以按后续访问顺序决定保留与驱逐页，而非等 page fault 才发现新 task 缺页。把这份 working-set 信息随执行上下文移交，才可能区分整块预留、实际会触及的页，以及应提前搬入的页。

预取还要与执行依赖共同排程：双 copy engine 可以重叠迁出与迁入，compute 则只在自身依赖页 ready 后开始，不必等整个 context 完成换入。[MSched v1 §5–7](https://arxiv.org/html/2512.24637v1)的收益来自受控时间线、可预测访问与 oversubscription 条件下的 driver 管理；它不是未知未来负载上的全局 OPT。模板未覆盖的 pointer-chasing、误预测和驱动控制成本仍需由 demand paging 兜底。RTX5080 上 int8 Llama3-8B/llama.cpp 的多进程对照不能替代 serving 的 TTFT/TPOT 验收，更不能把相对 thrashing 的倍率解释成常驻显存路径加速；workload 不可预测、容量足够或控制成本超过迁移收益时，常驻分配或原 demand-paging 路径仍合理。<!-- source-family:SF-2026-ARXIV-2512-24637 -->

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

移动 integrated GPU 的首次执行还可能需要另一种生命周期：权重从磁盘进入 unified memory 后，仍要转换成 GPU texture 布局，释放原布局却不一定能立即回收尚在使用的 texture。若 model graph、执行顺序与容量模型可由 profile 固定，规划器可联合安排 disk load、texture transform、compute 与释放；某些 fusion 虽减少算子开销，却移除了层间的预取插入点，因此要比较保留融合和拆开后恢复 load/compute 重叠，而非始终追求最大 fusion。FlashMem 的局部实现支持这种冷启动联排，但离线 150 秒搜索中的 feasible 解不全是 optimal，常驻权重和临时 texture 要共同计入峰值；报告的平均内存也不是峰值容量保证。warm-start 对照重复 3–12 次时可能反而更快，额外 I/O 与功耗、不可重叠的 transform 仍是代价。有限手机、batch=1 的模型初始化加执行，尤其 SD 的 UNet 切片，不代表完整生成 pipeline 或 serving TTFT/TPOT；静态图变化、profile 失配或工作集可常驻时，原 resident/no-copy 路线仍更简单。<!-- source-family:SF-2026-ARXIV-2602-15379 -->

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

当 CPU 也能直接执行未驻留 expert 时，HBM miss 不必一律转成 GPU 权重补给。运行时可以按当前已选 expert 的 token 负载，以及实测 CPU 计算、GPU 搬运与计算的成本，联合选择在哪一侧执行，以两侧完成时间的较大值为规划目标；搬运与计算能否重叠仍由真实执行路径决定。预测下层所有 activated experts 也不够，预取对象应是计划交给 GPU 的高工作量部分，否则可能替 CPU 搬入它本可直接计算的权重。这增加 CPU/GPU 并行、代价校准以及 gate、cache 更新开销，高 hit rate 不能代替端到端时延。工作负载漂移、预测成本超过可隐藏时间或全 expert 本可驻留时，静态 placement 仍合理；局部规划模型也不自动证明容量约束已在实现中正确执行。<!-- source-family:SF-2026-ARXIV-2602-03495 -->

当 router 的预测价值不足、但各 MoE 层的执行顺序已知时，另一条分支不预测**哪些 expert 会被选中**，而是把 expert 权重从长期 HBM 驻留改为按层临时物化：保留稳定的逻辑 tensor 地址，让当前层的全部 expert 可供原 router 和 kernel 使用，同时预取下一层，并在计算完成后才回收上一层的物理页。这样不转移 router 的语义选择权，却把问题从“能否猜中路由”变成“host/GPU 压缩层能否在前一层计算期间搬完下一层”。两层滑动窗口、映射提交与 GPU stream 的读写顺序是正确性条件，不能只看平均 cache hit。

临时权重释放出的 HBM 还须与增长中的 KV 和 activation 共同规划；可根据 KV 压力降低额外常驻的 expert 数量，并按各存储后端的有效带宽分配加载量。但这不等于释放的字节立即扩大现有 serving engine 的 batch：若 KV 池在初始化时固定，动态扩容仍需要独立的 allocator/调度支持。整层全 expert 搬运也可能比路由选中 expert 的按需加载更贵；带宽不足、低并发或全权重本来可常驻时，原有静态/路由条件化方案继续成立。<!-- source-family:SF-2026-ARXIV-2604-02715 -->

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

容量评估还必须跨越单个组件：在冻结生成主干的多模态 pipeline 中，text encoder 只运行一次，缩短其耗时未必缩短整次生成；但 encoder 长期驻留的字节会挤压反复执行的 denoiser 工作集。若两者加 activation / scratch 超过可用设备容量，原本不在时延关键路径的 encoder 也能通过分页影响每个生成 step。一条条件化分支是用较小 encoder 加校准 translator 对齐原接口，释放工作集容量，再选择 denoiser 常驻或 weight streaming；资源 planner 拥有 residency，质量验收仍须核替换后的条件表示和最终生成，不能由 feature 相似度直接通过。

`arXiv:2609.21849v1` §4 / Figure 3 的 RTX 4070 Ti 12GB、1024² / 4-step 配置超过约 11.2GB 可用预算时，作者测得 denoising latency 退化约 40 倍；这不是一般分页倍率。0.6B encoder 加 187M translator 在 25% denoiser residency 下约 6.7GB，只付约 3% step-time 代价。另一台 96GB RTX PRO 6000 全部可驻留时，低 residency 反因 PCIe 补给赶不上计算而更慢；Table 3 同 BF16 整次时延仍为 0.47s，省 encoder 时间不等于 pipeline 加速。两平台不合并收益，24-prompt 匹配质量检查只属受限证据，扩大 matched 切片是后续验收建议；作者的 `2W_max + A_max` 仅属双缓冲配置，不是通用容量下界。质量回归或工作集本就能常驻时保留原 encoder / 全驻留；UMA 共享池也不能把 host offload 当成释放总内存。<!-- source-family:SF-2026-ARXIV-2609-21849 -->

即使更慢的 memory tier 能容纳全部 experts，“容量足够”也不等于“路由后的计算单元被充分占满”。请求只激活少量且分布偏斜的 experts 时，resident weights 解决的是供给带宽，未解决 core occupancy 与 hot-expert contention。更完整的执行路径需要把 co-activation placement、local multicast、load-aware fetch 与 router 输出共同规划：memory pool 只交付不可变 expert weights，router 仍拥有语义选择，executor 决定如何把已选工作映射到可用计算单元。

这条分支用专用 near-memory 组织、放置校准和更复杂的调度换取较高 bandwidth density；路由分布漂移、专家集中度低或硬件不可得时，通用 GPU/HBM 的常驻或按需加载仍更稳妥。`arXiv:2608.13962v1` 的结果来自作者 measured-plus-modeled ReRAM/H20 系统、Qwen3.5 与 GLM-5.2 workload，没有公开可部署芯片 artifact，不能把延迟、能效或 occupancy 结果写成现货硬件保证。

<!-- source-family:SF-2026-ARXIV-2608-13962 -->

更大的硬件系统也会把优化边界从单 accelerator 推到 rack/POD：HBM、互联、CPU、storage、power 与
cooling 必须按 training、prefill、decode 和 Agent workflow 的不同状态流共同设计。但厂商 platform
announcement 只能证明版本化产品事实和设计方向，不能把未披露的 workload benchmark 写成通用结论。

### Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页

### 多类 Cache 共享 HBM 时，Allocator 与 Router 必须共用一个 Contract

把 embedding hot cache 与 KV cache 固定切成两个显存池，在访问分布稳定、迁移代价高时最容易预测，也便于分别调优。但生成式推荐同时具有大规模 embedding lookup 和自回归 KV state；当 steady、trend 与 burst workload 改变两类 cache 的边际收益时，固定比例会让一侧空闲、另一侧 miss，并把 H2D refill 推入 P99 关键路径。此时 memory allocator 不能只按局部 hit rate 改分区，request router 也不能只按 node load 分发：二者必须读同一个 committed residency map、迁移进度、KV/embedding locality 与 tail-SLO budget。

在线策略可以提出新的分区比例和路由目标，但只有页面迁移完成后，memory manager 才能提交新容量视图；burst recovery 还应限制动作幅度或回退最后稳定分区，避免控制器追逐短时流量而产生 cache thrash。联合控制换来对 workload drift 的适应性，却增加 policy drift、跨节点路由、迁移流量和失败恢复。单一 cache、分布稳定、链路拥塞或严格确定性优先时，静态分区仍更可靠。`arXiv:2605.04450v1` 只在作者的生成式推荐系统、32-node A100、8K–15K sequences 与三类 workload regime 下验证该设计，不证明普通 LLM serving 拥有相同最优比例或延迟收益。

<!-- source-family:SF-WHEN-KV-MEETS-EMBEDDINGS-DYNAMIC-GPU-MEMORY-ALLOCATION-FOR-ACCELERATING- -->

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

### 双模式 Weight 与 KV 的非对称共享

固定精度和固定 weight/KV 分区，在质量优先、流量稳定时最容易解释，也避免运行中重载权重。突发请求让 KV 挤满 HBM 后，可以把可独立读取的低精度权重长期保留，只让高精度 residual 与 KV 共享物理容量：降到 fast 模式释放 residual 的使用权，回 full 模式则从 host 分块恢复 residual，全部恢复完成后才在 forward 边界切换。这个提交边界不同于单个请求边界；同一请求前后可能使用不同模式，恢复高精度不会撤销已经生成的低精度历史。

逻辑 free 也不等于可立即撤销所有虚拟映射：若 worker 仍有 in-flight KV 读取，共享页 manager 必须协调用途变化，而不能让 scheduler 回收直接破坏读地址。[DPS v1 IV–V](https://arxiv.org/html/2609.34380v1)采用长期 KV 映射、residual backing 与双模式 CUDA graph，因而增加 host residency、PCIe 传输、状态管理和 graph 成本。其 effective pass@1 同时含 SLO 与质量，不能证明精度等价；静态 FP8 有时已满足压力目标，低压力也可能不获益。质量门不允许模式混用、恢复带宽不足或共享页状态不可靠时，继续使用静态精度及明确的 KV 容量／admission 限制。

<!-- source-family:SF-2026-ARXIV-2609-34380 -->

### 离线批量推理的跨 GPU 权重共享

离线大批推理若沿用 data parallel，每张 GPU 复制完整 weights，控制最简单，却会把本可供 KV 与 batch 使用的 HBM 固定占满。节点内互联空闲且 workload 以 throughput 为目标时，可以把 layer weight 只放在 owner GPU：大批次让 owner 将 weights 流送给 peers（weight-as-stream），小尾批次则把 activations 送到 owner 计算（compute-as-service），运行时按传输量选择分支。

它用 fabric bandwidth、同步和 layer-owner 故障域换 HBM 容量，且只在传输可被大批计算摊薄、尾部 activation 明显小于 weights 时成立；在线 tail-SLO、跨节点慢链路或 owner hotspot 会使收益消失。常规 DP 在模型可装下、请求小或隔离优先时仍更可预测。作者离线推理实验不证明该设计适用于持续到达、跨机通信或任意模型形状。

### HBM Partition 是可版本化的 Runtime State

当 expert weights、KV 与 workspace 竞争 HBM 时，静态配额简单且可预测，但会在请求形态变化后同时制造 expert miss 与 KV spill。动态 controller 可以用 re-prefill cost、expert load、TTFT/TPOT SLO 和 topology 估计重映射 pages；它只提交 partition proposal，expert/KV owner、迁移完成和 rollback 仍由 runtime 负责。预测不稳或互连不足时，静态分区仍是更安全的共存方案。<!-- source-family:SF-2026-ARXIV-2609-13537 -->

异构 coherent memory 又引入另一条分支：HBM 与 host 可以并发取数，因此 residency 不只是冷热搬运，还要估计 overlap、contention、NUMA 和 coherence cost。没有一致寻址平台或 overlap 无法验收时，显式迁移与固定驻留仍更清晰。<!-- source-family:SF-2026-ARXIV-2609-13592 -->

### 混合序列模型需要 Typed Memory Pages

统一 page size、统一 eviction 在状态同构、访问路径相近时能降低 allocator 与 scheduler 复杂度；混合 Mamba–Transformer runtime 同时拥有 recurrent state、attention KV、weights 与临时 workspace，它们的更新频率、可重建性和 fault cost 不同。因而 page identity 应携带 state type、model/request revision、placement owner 与 recoverability，allocator 只能提供容量，执行计划才决定何种状态可迁移或驱逐。

Beam search 的 recurrent state 还可拆为共享 immutable root、分支 transition log 与按需 materialized state。这样不必为每条 beam 复制完整状态，却把 ancestry、replay 和版本一致性变成 memory contract；分支长、状态不可重建或普通 sampling 宽度很小时，直接复制仍更简单。该分支适用于可重放的线性/recurrent transition，不应外推到任意 hidden state。

<!-- source-family:SF-2026-ARXIV-2609-12399 -->

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

近存计算阵列中的动态 KV 还多一项空间约束：历史 full blocks 决定 attention 的计算与存储负载，仍在追加的 last block 则决定每步新 K/V 从 reduction endpoint 写到哪里。只平均分配容量可能平衡读取，却放大写入的 mesh traffic。一条条件性分支先按 token load 平衡各 PE；负载相同时，把 full blocks 放得远离中央 reduction/gather endpoints，为 last blocks 保留中心位置，再用未满块数与传输路径负载打破 last-block 的平局。CPU block manager 维护 request/free block identity，固定 PE-local backing 只提供物理地址；prompt KV transfer 完成后请求才进入 decode batch。这里改变的是 placement 与写入路径的共同选择，不改变 KV 的模型语义。<!-- source-family:arxiv:2603.04797v1 -->

这增加 CPU allocator、block metadata、mesh collectives 与硬件布局耦合；token count 也只是特定 tiled attention 的负载代理。块过大增加 fragmentation，过小放大管理与通信，不能仅按峰值带宽选型。Helios 的必要证据来自 FP16、八设备配置、Mooncake arrival/length workload 下的模拟器与综合，GPU baseline 则由实机 profile 支持；均匀 MoE routing 刻意排除了真实 expert imbalance，end-to-end 收益还受到 GPU prefill 限制。它不证明已有可部署芯片、通用 SLO 或任意 topology 的优选 placement；不支持该硬件、布局或 workload 假设时，保留普通 HBM paging、GPU execution 与更简单的 load-balanced allocation。[机制与受限评价](https://arxiv.org/html/2603.04797v1)见 §IV-A/IV-B、§V-A 与 §VI。

#### 端侧 NPU 只有全链迁移才构成新的 Memory/Energy 分支

把单个 embedding 或 generation operator 放到 NPU，不能证明端侧 RAG 的系统收益，因为 reranking、跨设备搬运、模型加载和 host orchestration 仍可能占据主要内存、延迟与能耗。更完整的 contract 要把 embedding、reranking 与 generation 作为同一条 NPU-resident path 测量，并把加载顺序、static-graph 约束、context bound 与整机 energy/latency 一起纳入 owner。是否使用 NPU 因而是全链驻留与生命周期决策，不是算子级布尔值。

GPU、CPU 和 hybrid execution 仍与之共存；dynamic shape、超长上下文、模型不受支持或内存峰值超限时，hybrid path 可能更稳健。现有证据仅来自 Snapdragon X Elite 单机和 120-query corpus，不能外推其他 NPU 或线上多租户容量；迁移不完整时，新增 device transfer 还可能抵消节能收益。

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

当 sparse KV 的选择集合每步随 Query 改变时，容量层还要共同决定“选什么”和“到哪里读”。Flash 的一页必须整体 sense，同一 plane 的读取会串行，运行时重排旧页又消耗 program/erase；因此只减少 token 数，不保证读取更快。一条条件性分支是在 HBM 驻留期间观察 co-selection，写入时固定 page composition，再由 base-die 对 page centroid 打分并生成本步的 physical page list。GQA 中多个 Query heads 共享一个 KV head 的物理预算，不能把每个 head 的 top-k 简单相加。Mean centroid score 是页内平均 logit，不是完整 Attention 的等价替代；按 plane 限额选择还会丢弃部分 global top-k，以质量换最忙 plane 的有界读取轮数。<!-- source-family:SF-2026-ARXIV-2609-23816 -->

这个选择路径也需要 commit 边界：单 writer 的 request-private append-only region 只有在 program 完成后才推进 HBM/HBF horizon，每个 decode step 在开始时固定该 horizon，HBM 在完成前继续保留待迁页；否则 Query 可能命中尚未可读的历史。Request 结束后整区回收可以免去任意 live-page relocation，但不能据此推导多 writer、通用 GC 或掉电恢复保证。更大 HBM window 可遮住 centroid scan、合并写入并降低磨损，却挤占可接纳并发；更严格的 plane cap 也可能改变注意力证据。

SPLASH 的 exact-v1 只以尚未商用的 HBF 模型、OpenHBF 模拟与 measured Blackwell kernels 支持该协同设计。五模型的 serving 模拟与单一 Llama3.1-8B 的质量实验不是同一保证；48-needle/64K/10% retrieval budget 下，该选择得分 0.50，低于 dense 的 0.86。其写放大 1.15、均匀磨损与约三十分钟保留期是寿命假设，不是硬件五年承诺。无法满足选择质量、窗口遮蔽或写寿命条件时，保留 dense HBM、传统 offload 或更保守的检索预算，不能只按容量与峰值带宽选型。

新的 GPU generation、低精度格式、高速互联和 memory hierarchy 会显著改变可行边界：更高算力、更大 HBM、更快互联、更低精度 tensor core，都会推动系统设计变化。具体型号与规格变化很快，不应成为本章的稳定主线。

但硬件升级不会消除系统问题。参数规模、上下文长度和并发需求也会继续增长。新的 FP4/FP8 能力需要软件栈、kernel、量化策略和质量评估配合。

所以正确的结论不是“等硬件变强”，而是“软硬件协同”。硬件给出新的约束和机会，runtime 必须重新组织计算、内存和调度。

### Compute-in-Flash 会改写 KV 表示合同

Flash 内执行受整数算子、写寿命和带宽约束，不能照搬 HBM 中的完整 KV layout。一个受限分支将 KV 表示为静态 dictionary 加 sparse coefficient，把设备内计算、传输和误差预算共同设计；dictionary、coefficient、模型层与设备 revision 因而成为 cache identity。<!-- source-family:SF-2026-ARXIV-2609-16161 -->

压缩与近存计算换取更低搬运，却引入 dictionary error、双副本、写放大和 prefill 支持缺口。两个 7–8B 模型、LongBench 与 analytical device model 不证明真实器件寿命或生产并发；越界时回退 HBM/host offload 或完整 KV。

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

## Physical Layout 与 Accessor View 可以分离

同一 tensor 在 prefill、decode 或 MoE routing 阶段可能由不同设备访问。重复维护多份布局会增加同步和容量，单一布局又可能不适合所有 accessor。一个折中是保存一份 physical object，通过 address translation 为 NPU、PIM 或不同 kernel 提供 logical view；translation 只改变访问视图，不拥有 tensor truth。

这类原型增加映射表和一致性成本，且可能被转换开销抵消。是否采用必须绑定实际设备、phase 与 workload，普通 GPU-only 路径仍可使用直接布局。

<!-- source-family: arxiv:2608.06989v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: physical-layout-logical-accessor-separation -->

启动路径还需要区分“字节已读取”与“权重已可执行”。Load-ready state 应原子绑定 artifact layout、连续可导出的 tensor address space、remote mapping lifetime、communicator readiness 与 clone completion；任一分量未提交，都不能让 scheduler 把 replica 标为 ready。预先布局和远端映射可减少碎片、串行 clone 与重复加载，却增加 fabric 依赖、地址生命周期和恢复复杂度；不支持相应互连或映射语义时，普通 loader/NCCL 初始化仍是可靠 fallback。

<!-- source-family: arxiv:2608.08482v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: load-ready-weight-state-atomic-commit -->

近存计算还可按状态类型分层：将FFN权重留在NAND附近执行，将attention与动态KV保留在LPDDR。介质错误不能只靠“数据已读”就允许输出提交；raw-read快检将错误segment暂时跳过后，scoreboard应等待慢纠正并补齐对应MAC结果，再使计算结果ready。NAND page与PE的数据宽度配合、权重放置、错误恢复authority和remaining attention/KV瓶颈要共同预算，不与前述KV压缩混为一条机制。

这以器件、错误检测/纠正和scoreboard状态换取更少搬运，KV增长、纠错拥塞与故障可能重新进入尾延迟。受限NVLLM来自模拟器和综合而非实机，INT8/RBER工作点不能外推任意模型，out-of-core GPU对照也不等同容量HBM GPU，movement energy不是总能耗。介质、错误率或质量不匹配时，保留DRAM/数字执行、完整ECC与保守offload。 [原文必要机制与限制](https://arxiv.org/html/2604.25699v1)。
<!-- source-family:SF-2026-ARXIV-2604-25699 -->

### Physical Region Map 应在写入时固定

如果 CPU/GPU 共享同一 KV backing，写入时固定 physical region map，可以让 logical KV identity 与访问位置分离；但 four-region format、allocator revision 与 accessor view 必须同一次提交，调度器只能选择已验证的访问路径，不能临时猜测 layout。kernel/framework 不兼容时应回退迁移式 tiering。<!-- source-family:SF-2026-ARXIV-2609-14507 -->

Storage-backed MoE 还需要分别测 internal flash/storage bandwidth 与 host-link bandwidth 两个 knee，再决定 flash、DRAM、HBM 的 staging。只证明容量可放下 experts 不等于 provisioning 可服务 token SLO；任一 bandwidth knee 不满足时，应回退 host offload、更小 resident model 或减少 active experts。<!-- source-family:SF-2026-ARXIV-2609-15636 -->

## Expert Cache 的结论依赖 Replay Methodology

缓存策略比较只有在 fused event 保持原子、workload 未被模板污染、capacity regime 按层归一化时才可复现。错误的 replay 顺序或回收手段会改变 hit path，甚至反转 LRU 与其他策略排名；offline oracle 也不等于可实现上界。评测因此要冻结 event semantics、reclaim mechanism、warm state 和容量，而不是只报告命中率。

<!-- source-family: arxiv:2608.07911v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: expert-cache-replay-methodology-contract -->

## 模型持续大于显存时，预取对象可以从 Tensor 缩到 Row Delta

传统 offload 在每层搬运完整 tensor；动态稀疏模型只激活少量 neuron，且相邻 token 的 active set 常有重叠。若 GPU 保留当前 resident rows，预测器只需从 storage 预取下一 token 新增的差集，从 whole-tensor streaming 演进为 sparse-row delta movement。

预测器只拥有 prefetch hint，真实 activation 决定 correctness；miss 会重新暴露随机 I/O stall，低 locality 还会让细粒度读取比顺序搬运更差。dense model、短序列或 host bandwidth 充足时，传统 offload 仍更简单。收益必须绑定稀疏度、storage path、缓存命中与预测开销。

### Speculative Verification Window 可以成为 Expert Staging 的有界 Lookahead

Storage-backed MoE 通常只能等 router 决定后按需加载 expert；speculative decode 的 verification window 提供了短期候选路径，可以让 runtime 按 acceptance probability、routing likelihood 与 movement cost 提前 staging，并利用 co-load 重排 flash layout、批处理 ready experts。该窗口只提供搬运 proposal，最终 router 与 verifier authority 不变。<!-- source-family:SF-2026-ARXIV-2609-14643 -->

收益依赖 acceptance 和 locality，代价是错预测 I/O、布局重组与 metadata。四个 MoE、五个 benchmark 和两类 mobile platform 不构成通用速度保证；命中不足或搬运成本超界时，应回退 on-demand load 或更小 resident model。

### Memory hierarchy 设计必须寻找 phase-specific working-set knee

简单增加片上 SRAM/cache 只在 working set 尚能提高命中率时持续节省能量；prefill 与 decode、context 长度、operator fusion 和 mapping 会把拐点推到不同位置。容量规划因此不能只比较 memory technology 的峰值 PPA，而要把 operator trace、层级流量、映射、cycle 与技术模型放进同一 evaluator，分别寻找各 phase 的 capacity knee。

设计期模拟能缩小搜索空间，却不能证明新 memory technology 已满足制造、频率、热和真实 workload 约束。模型假设不稳时，应保留现有 HBM/DRAM hierarchy 和实机 profile 作为基线，而不是把模拟节能数字写成部署保证。

<!-- source-family:SF-2026-ARXIV-2607-26491 -->

片上容量还可能首先承担排队与控制，而不只是缓存复用：稀疏行的非零数不同，固定同步 reduction 会被慢行拖住。一个受限 ASIC 分支为 partial sums 保存带 row identity 的 FIFO window，由行 orchestrator 的 FSM 根据输入非零项、上游消息和当前 window 选择 MAC、累积、flush 或向下游 bypass；小队列让本地计算与异步 reduction 分开推进。物理 scratchpad 容量固定，软件改变有效 window 和管理逻辑，因而同一片 SRAM 的可用性还取决于数据依赖的 control mapping，而非容量数字本身。[Canon v1 §4.1.1/6.3–6.5](https://arxiv.org/html/2602.17119v1)中较大 buffer 可吸收部分不平衡，却仍受最慢行、管理开销与算术强度限制；更多 buffer 不保证更快，高稀疏度维持同 compute throughput 还可能要求更多 off-chip 带宽。它增加 FSM/metadata、routing 与 scratchpad 的面积和功耗；22nm 综合与 cycle simulation、INT8 稀疏 kernel/attention mapping 只提供所述 ASIC 设计点，不是 GPU 程序、已制造硬件或完整 LLM 质量/SLO。相对 ZeD 的面积图/文字冲突和不同预处理假设不转成精确端到端倍数。规则 dense workload 仍可用更高效的 systolic/static mapping；动态控制净收益不足或硬件不可得时，保留实机 profile 与已验证 HBM/GPU 路线。<!-- source-family:SF-2026-ARXIV-2602-17119 -->

容量之外，channel 数量与 interleaving granularity 也不能独立最大化。更细的分散访问可以提高通道并行度，却减少 row-buffer locality；更粗的粒度保留连续行访问，又可能使一次 tile/block 只触达少量通道。3D-DRAM 设计还把 memory controller 面积和 DRAM 热功率放进同一个 logic-die 预算：增加带宽可能挤掉 compute area、降低允许频率，不能以峰值带宽推出更低 decode latency。设计期 evaluator 应联合选择 channel/row/layout、算子 tiling、compute 和热约束，再比较实际模型、batch 与 cloud/edge 工作点。<!-- source-family:SF-2026-ARXIV-2604-08044 -->

联合选择需要更复杂的时序、面积和热模型，也会扩大校准与假设误差；一种 workload 的优选配置不能直接成为通用最优。作者报告了性能模型与 3D test-chip 的分层对照、并测量材料参数供热模型使用，但这不等于所有探索架构都完成热实测或可部署验收；低 batch MoE 下另一设计仍可能更优。通用 HBM/DRAM 路线在硬件不可得、模型校准不足或功率边界漂移时继续成立，设计空间搜索只缩小需要验证的候选，而不替代实机与受限负载验收。<!-- source-family:SF-2026-ARXIV-2604-08044 -->

### 跨主机共享 KV 需要同时拥有寻址、顺序与故障语义

CXL memory pool 从交换层级演进到光学 full-crossbar，可以减少中间交换和 eviction cliff，但“所有 host 都能看到大地址空间”还不等于可用的 KV tier。shared allocator、offset identity、registration、producer-consumer rendezvous、coherence/failure domain 与 revoke 必须一起定义，scheduler 才能安全地把 KV 放入池中。

硬件 emulation 加 serving simulation 只能证明参数化模型下的潜力，不能冒充真实 appliance、connector 与多主机推理已完成。光学器件和共享故障域也是新增成本。物理端到端验证缺失时，这类 tier 只能作为 Experimental 选择，并保留本地重算或既有 CXL/HBM 路径。

<!-- source-family:SF-2026-ARXIV-2607-27187 -->

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

同一 NVMe-backed KV 资产还可以按 layer 的 K/V unit，在初始化时选择 page-cache 路径或直接 LBA 路径：前者复用操作系统缓存，后者显式管理 aligned extent 与 pinned DRAM staging。两条路径需要不相交的资产分配及明确的 extent 生命周期，lazy materialization 也必须保留 layer/K/V 身份；它不是请求运行中无条件热迁移，更不是 NVMe 直接进入 GPU。<!-- source-family:SF-2026-ARXIV-2604-26557 -->

直接路径减少通用缓存开销，却增加对齐、extent 回收、pinned 内存和调度成本。作者 DRAM 富余配置中全部采用 direct 路径反而最慢，说明缓存命中与 staging 必须按 workload 联合选择；内存足够或缓存稳定时保留 page-cache，分配/对齐不可验证时回退普通 I/O，不以单一路径的局部吞吐承诺 Serving SLO。

Sparse KV offload 还要把算法与 runtime 的接口分开：Index/Select/Attention 定义候选与读取语义，Offload/Retrieve 负责实际 page residency 和完成状态。按 head 维护活跃物理 page metadata，可避免把 worst-case 逻辑容量一律常驻 GPU；但 CPU tables 仍可 pinned 并由 GPU 直接读取，不能把“冷”误写成 GPU 完全不可访问。<!-- source-family:SF-2026-ARXIV-2604-26837 -->

这种分责节省部分驻留 metadata，却支付索引、selection、PCIe 读取和搬运成本，逻辑稀疏率不等净 TPOT 收益。作者线上较大 batch 的高 TPOT 反例与 dense 质量对照须保留；head 分布漂移、metadata 读取或 retrieve 成为瓶颈时，扩大 resident set、采用简单 offload 或回退 dense，不把静态容量收益当并发 SLO。

### MoE Expert Staging 可以消费时序与跨层激活相关性

Expert 完全常驻 HBM 最稳健但容量昂贵；按 router 结果再加载不会误取，却可能让权重 I/O 落在 critical path。一个中间分支利用相邻 token 和相邻层的 expert activation correlation，在 router 最终决定前预取高概率 expert，同时不改变 router 本身的选择权。Memory manager 只管理 residency proposal，模型路由仍决定实际执行。

单步预测进一步演进为 sequence prediction、deadline-aware prefetch 与 future-aware replacement：预测器提出未来 expert path，cache owner 依据到期时间和 miss cost 决定 residency，并保持 graph-compatible placement。它能利用长程相关性，却新增 predictor drift、miss burst 和 topology 依赖；命中率必须与端到端 wait、额外 metadata 和不同 PCIe/fabric 条件联合报告，预测失准时回退 router-confirmed load。

<!-- source-family:SF-2026-ARXIV-2609-12978 -->

跨层 routing history 还可以作为 predictor input：若前一层 expert 之外，更早层的稀疏选择仍提供条件信息，cache owner 不应把 expert path 固定成一阶 Markov 假设。历史特征只拥有 residency hint，不拥有路由或执行权；probe 的增量可预测性也不等于端到端 prefetch 收益。history state、额外推理开销或 drift 抵消等待时间时，应缩短窗口或回退相邻层/实际 router 信号。<!-- source-family:SF-2026-ARXIV-2609-17940 -->

Prefetch 以额外带宽、staging capacity 和错误加载换取潜在 stall reduction；相关性随模型、层和 workload 漂移，错误预测还会挤出真正需要的 expert。带宽紧张、命中率不稳定或模型较小时，on-demand loading 或更高常驻比例仍更可预测。

还有一条不能归入 prefetch 的分支：当 expert weights 常驻 SSD、读取时延无法靠缓存完全隐藏时，模型可以训练一个
per-layer prerouter，在当前层提前预测下一层的 expert，并让这次预测**直接成为下一层路由**。这样下一层权重读取可在
当前层计算期间启动，decode path 不再等待原 router 后再触发 I/O；但系统也失去了“预测错了再 fallback load”的语义，
近似误差已经进入模型行为。因而质量恢复必须在训练侧完成：冻结低比特 base weights，让 Recovery LoRA 沿实际 student
routing path 学习补偿，并在 serving 时保持未合并，避免 merge 后重新量化抹掉补偿。

这条路线把控制权从 `router-confirmed residency proposal` 移到 `trained routing decision`，以训练成本、额外 LoRA state 和
质量偏差换取 SSD latency overlap。它只适合可以重新训练路由并接受近似行为的模型；要求原始 router 语义、无法承担恢复
训练、或分布漂移使预测质量失效时，仍应回退常驻、on-demand loading 或只做不改变路由的 prefetch。Edge0 的证据绑定其
披露的 Qwen/Ling 模型、Mac 硬件、OpenCompass 评价与高方差同 session A/B 性能协议，不证明任意 MoE、SSD 或生产 SLO。

<!-- source-family:SF-2026-ARXIV-2609-18063 -->

### Lossless Weight Compression 需要与 GEMM Tiling 联合调度

Bit-exact entropy coding 可以降低权重存储，却会在执行时引入 decode bandwidth 和状态。只有 tile-level ANS decode 与 GEMM tiling、prefetch 和 weight residency 使用同一 plan，解压才可能隐藏在计算流水中；高熵 tensor 收益很小，decode 甚至会成为新瓶颈。

这条分支不改变模型质量，但增加格式、kernel 与恢复复杂度。Batch、shape、模型和 GPU 改变后必须重新测量，普通未压缩或低比特量化权重仍是更简单的可共存选择。


### 新证据如何改变本章的设计边界

<!-- body-source:SF-2026-ARXIV-2606-21023 -->
**Demystifying Numerical Instability in LLM Inference: Achieving Reproducible Inference for Mission-Critical Tasks with HEAL 所揭示的约束变化。** 异构 GPU 上 greedy decode 仍会因 kernel-boundary downcast 累积而翻转；HEAL 用 INT16 Q/K/V 与双 16-bit GEMM 误差补偿换取接近 FP32 的功能复现性。这条路径只在 exact-v1 披露的任务与系统边界内成立；`arXiv:2606.21023v1 §6 Conclusion; Appendix B error, flip-rate and truncation studies` 记录了未证明范围。硬件、精度或 kernel identity 不匹配时回退到已验证精度路径并重新测量 memory/latency；原有简单路径在其假设成立时继续共存。

## 从“可见的 CXL 容量”到可调度的跨节点共享 KV

把 CXL memory 接到主机只解决了物理可见性；Kubernetes 若不知道 region 的生命周期、参与节点和撤销条件，
调度器仍不能安全地把它当作共享 KV tier。可组合内存需要由资源控制面先分配 region，再在各参与 host 上物化为 DAX device，
通过 DRA/CDI 把同一物理 region 注入对应 Pods；serving connector 才能在共享介质内维护 slot directory 和 KV payload。

这条路径把 cache ownership 从单 worker 扩展为 `resource claim + shared region + slot key`。它能让请求跨节点调度后复用 prefix，
却新增 model/revision/layout discriminator、region revoke、eviction、copy 前后 key revalidation 和多租户容量记账。
公开可行性实验只有两节点、单 GPU、单 session、Qwen2.5-7B-Instruct 与 512 GiB appliance；作者明确没有验证 pooled-RDMA、
并发 tail latency 或 P/D handoff。因此本地 VRAM 命中仍是低延迟基线，身份不全或共享控制面失效时必须回到本地重算。

<!-- source-family:SF-2026-ARXIV-2609-10790 -->

## HBM 可靠性：把长跨度纠错移出常见路径

直接用长 codeword 保护每个 32 B HBM request，可以增强纠错，却会让所有读取承担 span 聚合、syndrome 与搜索成本，
难以匹配 LLM Decode 的 TB/s 流量。分层 ECC 的演进是：短 inner code 处理常见错误并显式 reject；只有无法局部解决的 chunk
才携带 address-derived erasure 进入长 outer code。写入侧用 span lock、data-before-parity commit、differential parity 和 poison state
保持同一代数据与 parity 配对。

收益来自把昂贵恢复变成 exception path，而不是“更强 ECC 没有代价”。新增状态包括 repair buffer、erasure mask、dirty/commit/poison
epoch 与 span ordering；错误率、稀疏写比例或队列压力超出设计域时，异常路径会反过来成为瓶颈。REACH 的证据来自公开模型流量、
Ramulator2 与 ASAP7 synthesized kernels，不是真实 HBM silicon；面积、功耗和带宽数字只能作为所述设计点的 feasibility evidence。

<!-- source-family:SF-2026-ARXIV-2609-10861 -->

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

## 小结

Inference memory budget 是 Part V 所有机制的共同约束。Weights 决定固定底座，KV 决定随请求增长的容量，workspace 与 communication 决定瞬时峰值，fragmentation 和 reserve 决定逻辑公式与实际可分配空间的差距。

下一章讨论 PD 分离：当 Prefill 与 Decode 被放入不同 GPU pools，显存和计算压力可以独立规划，但 KV state 必须付出跨池移动成本。

## Review notes

- Daily 2026-03-07：[Helios exact-v1](https://arxiv.org/html/2603.04797v1) §IV–V/Alg2、§VI。只采用full/last-block的token-load与mesh路径分配；固定backing地址和transfer-complete admission保留。FP16/八device/均匀MoE、A100测量与Helios硬件模拟分开，不授生产SLO或普遍block大小。root实际必要原文/正文及邻接非作者POST通过；未复现。

- Daily 2026-04-30：`2604.26074v1` §4.2–4.3/§6、`2604.26557v1` §IV–V、`2604.26837v1` §4.1/§5 的 operation remote→SMEM、双 NVMe 路径与活跃 metadata 窄命题，已由 apr29_close 独立 source→actual owner 核；作者实写，root已实际读取正文及前后衔接，非作者写后通过。均为受限作者实验，未复现、非生产 SLO。[DAK](https://arxiv.org/html/2604.26074v1)、[DualBlade](https://arxiv.org/html/2604.26557v1)、[SPIN](https://arxiv.org/html/2604.26837v1)。

- [STEPQuant v1](https://arxiv.org/html/2609.38169v1) §2–5、Appendix F/H；Daily 2026-09-30。相同inputs/gates条件下的误差传播、当前readout与后续packed writeback分离；time/space敏感度不是已证明统一最优，未复现。

- `SF-2026-ZAI-SCALING-PAIN-LAYERSPLIT`（Status: Experimental）：[智谱官方《Scaling Pain》](https://www.zhipuai.cn/zh/research/159)，2026-04-29 16:00 北京时间，§优化：KV Cache 分层存储 LayerSplit。采用 CP rank 按层持有 KV、Attention 前广播与 Indexer 计算重叠这一 Prefill 容量—通信分支；不同于闲置 peer HBM 副本或 layer weights 流送。约 90% prefix hit、GLM-5.1、40k–120k 的 10%–132% 吞吐增益仅为作者受限设置；Indexer 广播约为 KV 八分之一不可外推为通用常数，未证明生产 TTFT 尾部、低命中或弱互联收益。BugFix#2 的 Indexer read-before-ready 只作已有 tier readiness 的具体反例。作者 apr01 已读原文/正文/邻段，root 非作者实际写后复核通过；未复现实验。

- `SF-2026-ARXIV-2604-08044`：[ATLAS exact-v1 PDF](https://arxiv.org/pdf/2604.08044v1) §3.1–3.4/§4.2–4.3/§5。采用channel/interleaving/row locality与MC面积、compute/thermal共同选择的条件分支；cloud/edge/batch异质，低batch MoE保留Stratum优势。性能testchip分层验证、TDTR材料参数与探索架构热模型分开，不给通用16channel最优/生产交付保证。2+2+2=6、知识缺口深入，root必要原文与实际写后核验通过。

- SHIELD（Status: Experimental，SF-2026-ARXIV-2604-07396）：[exact-v1 PDF](https://arxiv.org/pdf/2604.07396v1) §II–IV/Alg1/TableII。采用 lifetime×BF16 bit sensitivity 的刷新策略分支，不采用“普遍保持准确率”或 NPU 整机节能结论。Q/O lifetime 测量绑定 H100、sequence2048；3T retention 与 DESTINY2MB 为模型，随机 mantissa fault injection 不等于真实相关器件错误。五模型/WikiText-2、PIQA、ARC-Easy 受限结果仍含切片退步；batch、生产并发/SLO未披露。作者侧必要源与正文已对读，待 root 非作者写后复核；未运行实现或复现实验。

- Edge0（Status: Experimental）：[arXiv:2609.18063v1](https://arxiv.org/html/2609.18063v1) §3.2 明确 prerouter prediction 直接成为下一层 routing，§3.3/§4 说明 Recovery LoRA 沿 student path 训练且 serving 时保持 unmerged；§5.1～5.4 的证据绑定披露的 Qwen/Ling、Mac、OpenCompass 与同-session A/B，§6 不支持外推任意 MoE、SSD 或生产 SLO。它不是 router-confirmed prefetch，也没有 misprediction fallback load 语义。

- mzCache（Status: Experimental）：[arXiv:2609.01338v1](https://arxiv.org/html/2609.01338v1) 的 Android/Adreno 实验支持 UMA 共享 RAM 下的容量核算与可部分恢复分支；压缩仍占 RAM，恢复依赖 buffer readiness。实验不保证任意外部压力下进程存活或零等待，固定 profile 还受热降频影响；不将混合 kernel/allocation/overlap 收益全部归因驱逐策略。

- Multi-Turn LLM Conversations under the Least-Recently-Used Policy（Status: Experimental）：[arXiv:2609.02027v1](https://arxiv.org/html/2609.02027v1)。whole-content LRU 的 mean-field 分解与实践近似区分可复用工作量上限和容量留存；不把 block-work ratio 写成 request hit rate。实测绑定 Qwen3-8B BF16、1P/4D Ascend 配置及作者 trace；partial-tail 修正、负载相关等待、截断观察和后验分布拟合限制外推。没有生产 SLO 或任意缓存实现的保证。

- `SF-2026-ARXIV-2602-00328`（Status: Experimental）：exact-v1 支持将 peer GPU spare HBM 作为可撤销 cache tier 以及作者双 GPU NVLink 实验；证据不覆盖 NVSwitch、并发 model-parallel traffic、多租户隔离、生产 tail latency 或所有模型均自然产生可用余量。https://arxiv.org/html/2602.00328v1

- `SF-2026-ARXIV-2606-21023` — primary `arXiv:2606.21023v1`；Method=`arXiv:2606.21023v1 §2.3 The Microscopic Origin: Boundary Truncation; §3 HEAL; Appendix C HEAL Implementation`；Evaluation=`arXiv:2606.21023v1 §4 Evaluation; Appendix A Detailed Experimental Setup; Appendix D Additional Performance Results; Appendix E MCR-Bench`；Non-proof=`arXiv:2606.21023v1 §6 Conclusion; Appendix B error, flip-rate and truncation studies`；Artifact=`Not Disclosed — no later artifact used`。

- Tile-scheduled lossless weight compression（arXiv:2606.15789v1；Status: Experimental）：支持 ANS decode 与 GEMM tiling/residency 联合；结果绑定 Qwen/Mixtral、SGLang、batch 和作者 GPU。https://arxiv.org/html/2606.15789v1

- Spatiotemporal MoE expert staging（arXiv:2606.15453v1；Status: Experimental）：支持利用跨层与相邻 token 激活相关性预取 expert，且不改变 router；证据绑定作者模型、硬件和 workload，不证明生产命中率或 SLO。https://arxiv.org/html/2606.15453v1

- Chiplet-contiguous GEMM layout（arXiv:2606.11718v1；Status: Experimental）：收益绑定论文 chiplet/interleave、GEMM shape 与 runtime；论文无独立 limitations section，不外推到非 GEMM 或动态 shape。https://arxiv.org/html/2606.11718v1
- CXL-Hybrid long-context memory（arXiv:2606.12556v1；Status: Experimental）：多级 byte-addressable tier 与 ITME prefetch 只在测试拓扑和可预测访问下成立，不证明所有 KV access 都可隐藏。https://arxiv.org/html/2606.12556v1
- Pooled DRAM/SSD KV offload（arXiv:2606.14779v1；Status: Experimental）：bandwidth-weighted pool 与 SPDK passthrough 降低串行 I/O；不消除 allocator、failure recovery 和运维成本。https://arxiv.org/html/2606.14779v1


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

- **SF-2026-ARXIV-2606-25519**：Primary `arXiv:2606.25519v1`；Method `https://arxiv.org/html/2606.25519v1 — §3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy`；Evaluation `https://arxiv.org/html/2606.25519v1 — §D Additional evaluation details; D.1 Benchmarks and evaluation protocol`；未证明边界 `https://arxiv.org/html/2606.25519v1 — §7 Can We Reduce Reasoning-Token Inflation; D.2 Model details`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26488**：Primary `arXiv:2606.26488v1`；Method `https://arxiv.org/html/2606.26488v1 — §Compression of recursive reasoners across precision, pruning, distillation and attention variants`；Evaluation `https://arxiv.org/html/2606.26488v1 — §Three tasks and two recursive architectures; local vs puzzle-exact accuracy`；未证明边界 `https://arxiv.org/html/2606.26488v1 — §Edge recursive models only; token-level preservation does not imply global-reasoning preservation`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-23001:start -->
- `SF-2026-ARXIV-2606-23001` — Daily `2026-06-23`；primary `arXiv:2606.23001v1`；Books review `books-review:SF-2026-ARXIV-2606-23001`。

  **已吸收的语义增量：** EnerInfer: Energy-Aware On-Device LLM Inference 的 exact-v1 机制为：To address these challenges, we propose EnerInfer, the first on-device LLM inference framework that jointly manages energy efficiency, throughput, and thermal comfort for LLM workloads. 因此 把设备频率、功耗/温度估计、QoE 和模型/backend identity 联合验收。
<!-- daily-books-trace:SF-2026-ARXIV-2606-23001:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-08761:start -->
- `SF-2026-ARXIV-2606-08761` — Daily `2026-06-08`；primary `arXiv:2606.08761v1`；Books review `books-review:SF-2026-ARXIV-2606-08761`。

  **已吸收的语义增量：** APEX4 把 W4A4 的瓶颈定位到同一 SM 内 Tensor Core 与 CUDA Core 的 compute imbalance，并用 kernel mapping 避免 mixed-precision fallback。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08761:end -->


<!-- daily-books-trace:SF-2026-ARXIV-2606-11718:start -->
- `SF-2026-ARXIV-2606-11718` — Daily `2026-06-11`；primary `arXiv:2606.11718v1`；Books review `books-review:SF-2026-ARXIV-2606-11718`。

  **已吸收的语义增量：** Chiplet GPU 的 GEMM locality 需要让 chiplet-local tiles 在 global address space 连续，使 page-granularity placement 与 CTA affinity 一致。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11718:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-12556:start -->
- `SF-2026-ARXIV-2606-12556` — Daily `2026-06-12`；primary `arXiv:2606.12556v1`；Books review `books-review:SF-2026-ARXIV-2606-12556`。

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
- `SF-2026-ARXIV-2607-16184` — Daily `2026-07-20`；primary `arXiv:2607.16184v1`；Books review `books-review:SF-2026-ARXIV-2607-16184`。

  **已吸收的语义增量：** 新增证据边界：Weights and KV compete for the same HBM budget, so MoE weight precision can become mutable runtime state. A safe page table must commit lower precision before freeing pages and restore pages before committing higher precision; planner identity and per-request quality policy become part of serving correctness. 该 delta 已进入 `books/part-05-inference-system/54-gpu-memory.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-16184:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-22389:start -->
- `SF-2026-ARXIV-2607-22389` — Daily `2026-07-27`；primary `arXiv:2607.22389v1`；Books review `books-review:SF-2026-ARXIV-2607-22389`。

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

- `SF-2026-ARXIV-2512-24637`：[exact v1](https://arxiv.org/html/2512.24637v1) §5 access templates、§6 scheduler timeline/driver eviction/双 CE、§7 evaluation。采用 scheduler 到 memory manager 的真实 working-set 与 page-ready 依赖；RTX5080 16GB 消费级显存不沿用原文 HBM 称呼，33.6–57.9×是相对 UM thrashing 的受限对照，不是生产 serving 或任意 CXL 性能保证。必要证据与实际 Capacity/Placement→新增段落→层级管理权及末注已 root 非作者审阅，写后通过；未运行代码或复现实验。

- `SF-2026-ARXIV-2602-03495`：[DALI exact v1](https://arxiv.org/html/2602.03495v1) §3–6/A1–3；采用 CPU 直接执行与 GPU 搬运/执行联合规划、仅对计划 GPU 高工作量专家预取的边界。作者 EPYC7532/RTX3090/PCIe4、三 MoE 模型与有限 batch 证据不提供跨设备或生产 SLO 保证；Eq9 容量约束在 Alg1 未显式体现，Alg2 evict TopK 与 prose 低 score 描述冲突，不授伪码正确性。必要原源与具体差异已 root 非作者核，root 实际写后复核通过，日级 Gate 待验；未核代码或复现实验。

- `SF-2026-ARXIV-2601-06562` — Daily `2026-01-14`；[Mosaic exact-v1](https://arxiv.org/html/2601.06562v1) §3、§4.2–4.5、§5.1–5.3。原7分；仅采用mask/tokens参数化的全loop alias/lifetime/barrier资格→动态峰chunk→VMM逻辑/物理分账。RTX3090-24GB/A10040GB、LLaDA8B/Dream7B/LLaDA-MoE，dummy-input容量及单step延迟不授语义长context或requestSLO；累积消融同时更换inplace算子，不授单因果/所有shape最优，precision/并发/完整质量预算Not Disclosed。未核代码/复现；root必要原源→owner独立通过，实际两段/邻接及末注已 root 非作者写后通过；日级Gate未授。

- `SF-2026-ARXIV-2602-15379` — Daily `2026-02-19`；[FlashMem exact-v1](https://arxiv.org/html/2602.15379v1) §3.1–3.2/4.1/5.2及必要Table7。2+1+2=5，weight load/texture lifetime/fusion插入点冷启动联排具体差额受影响深入；static profile/order、150s feasible非全面optimal、常驻与peak总量/平均非peak、warmstart反側/功耗/UNet非完整pipeline边界近正文。root必要原源/actual owner PRE通过；root实际正文/完整邻接及末注非作者POST通过，窄锁释放。未核代码或复现，不授servingSLO。

- `SF-2026-ARXIV-2602-17119` — Daily `2026-02-21`；[Canon exact-v1](https://arxiv.org/html/2602.17119v1) §2–2.2/4.1.1/5/6.1–6.5；2+2+2=6，row-window FSM 与有效 scratch 容量差额深入。仅受限 ASIC 分支，综合/模拟不是 GPU 或实机部署；最慢行、buffer/control/带宽成本、dense 反侧及面积/预处理边界近正文。root必要source/actual owner PRE通过并授窄锁；作者正文/完整邻接及末注已顺读，非作者POST通过，窄锁释放；未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-18568` — Daily `2026-02-25`；[exact-v1](https://arxiv.org/html/2602.18568v1) §III/VI/VII/IX。采用固定 interface 下容量参数化与 batch/length 可行域的窄硬件分支；每 GB 成本、activation broadcast、异精度协议、模拟而非实机及 commodity HBM 回退近正文。不采用整机宣传倍数或全模型数值质量保证。root 必要原源与实际 owner PRE 通过并授自身窄锁；作者实际顺读正文、完整邻接及自身末注；root 非作者 actual POST 通过，窄锁释放。未核实现或复现实验，非日级验收。
