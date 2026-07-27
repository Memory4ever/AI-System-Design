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

## Fragmentation 与 Reserve 为什么真实存在

Logical free bytes 不一定能被目标 kernel 使用。Allocator 粒度、KV block 内部空位、CUDA graph capture pool、tensor alignment 和暂未释放的 asynchronous buffers 都会造成差异。

Reserve 不是“浪费掉的显存”，而是为 shape variation、collective、temporary allocation 和 failure recovery 保留的操作空间。Reserve 太大降低并发，太小会让系统在高负载时频繁 OOM 或 preempt。

## 三类缓解路径

### 减少 Bytes

Weight/KV quantization、GQA/MQA、压缩或稀疏 retention 直接减少 resident bytes，但需要质量与 kernel 验证。

### 提高利用率

Paging、prefix sharing 和更精确 admission 减少预留与碎片，却不改变每个有效 KV element 的逻辑需求。

### 扩展层级

CPU/SSD/off-node cache 扩大总容量，却加入 transfer latency、bandwidth contention 和 consistency。它们把“装不下”改成“何时值得搬”。

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

它与 KV tiering 只复用 locality 原则：expert identity 是 weight artifact，KV identity 是 request/prefix state，
正确性与失效条件不同。预测错误会产生 PCIe stall、cache thrash 与 tail latency；open PR/RFC 只能作为
Experimental evidence，不能当作稳定框架行为。模型较小、expert 分布均匀、带宽紧张或 SLO 严格时，
全驻留与静态 placement 仍更可预测。

更大的硬件系统也会把优化边界从单 accelerator 推到 rack/POD：HBM、互联、CPU、storage、power 与
cooling 必须按 training、prefill、decode 和 Agent workflow 的不同状态流共同设计。但厂商 platform
announcement 只能证明版本化产品事实和设计方向，不能把未披露的 workload benchmark 写成通用结论。

## 硬件升级不是最终答案

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

## 小结

Inference memory budget 是 Part V 所有机制的共同约束。Weights 决定固定底座，KV 决定随请求增长的容量，workspace 与 communication 决定瞬时峰值，fragmentation 和 reserve 决定逻辑公式与实际可分配空间的差距。

下一章讨论 PD 分离：当 Prefill 与 Decode 被放入不同 GPU pools，显存和计算压力可以独立规划，但 KV state 必须付出跨池移动成本。

## Review notes

本轮 Review 增加了权重和 KV Cache 的容量下界，以及 scheduler 实际面对的 usable HBM 约束。随后通过一个明确标注日期与缺失条件的 MI455X capacity case 验证“先扣固定成本，再比较动态容量”的推导；该型号不是章节长期假设，也不承担通用性能结论。显存优化首先要有 workload-aware memory breakdown，不能只依据标称容量或单个优化名称。

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
