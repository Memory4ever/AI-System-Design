# 第50章 LLM Serving Engine：以 vLLM 为例

**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场
**Stable Knowledge Node ID:** `INFER-VLLM`
**Legacy Chapter:** Ch46
**Status:** Draft

**Roadmap Intent:** 让 scheduler、KV Cache manager 与 model workers 围绕同一 request state contract 协作。

## 本章要回答的问题

vLLM 为什么会成为 LLM Serving 的代表性引擎？如果第47章已经讲了 PagedAttention，那么 vLLM 章节还应该讲什么？

本章的核心判断是：**vLLM 的核心价值不只是实现 PagedAttention，而是让 scheduler、KV Cache manager 与 model workers 围绕同一 request state contract 协作，把可变 token work 变成持续的 GPU execution。**

PagedAttention 是 vLLM 的历史性设计起点，但不是今天描述 vLLM 的充分条件。当前架构还要区分 API/entrypoint、engine core、scheduler、KV Cache manager、model runner 与 GPU workers；prefix caching、structured output、speculative decoding、KV transfer 等能力也会继续改变 runtime state。

## Serving 引擎不是模型 loader

加载模型权重只是第一步。真正的在线 serving 还要解决：

- 请求何时进入 batch。
- 每个请求的 KV Cache 如何分配、扩展、释放。
- 输出长度不同的请求如何动态进出。
- prefix / parallel sampling / beam search 是否可以共享 cache。
- 用户看到的 stream 是否稳定。

vLLM 的系统切入点是：LLM Serving 的吞吐受 KV Cache memory utilization 强烈限制。如果 cache 管不好，GPU 上装不下足够多的并发请求，再强的 compute 也会空转。

## PagedAttention 在 vLLM 中的位置

PagedAttention 把请求的 KV Cache 切成 block，用 block table 做逻辑到物理的映射。这个机制减少了预留最大长度造成的浪费，也降低了动态分配连续显存的碎片问题。

但在 vLLM 里，PagedAttention 只是底座。它需要和 scheduler 一起工作：

```text
Scheduler 决定哪些请求运行
Block manager 决定 KV Cache 放在哪里
Attention kernel 根据 block table 读取 K/V
Output processor 处理采样和流式返回
```

所以 vLLM 的系统问题不是单点算法，而是 “memory-aware scheduling”。

从请求生命周期看，可以把稳定边界写成：

```text
API process 接收和流式返回请求
→ engine core 维护 request state 并做 scheduling
→ KV Cache manager 处理 block allocation / reuse / eviction
→ workers / model runner 执行模型与 collectives
```

具体进程数量和类名会随版本变化，但控制面状态与 GPU execution 的分离是理解 serving engine 的关键。

## 当前 V1 的稳定架构边界

按当前官方 V1 architecture，可以用三类进程理解：

```text
API server
  request parsing / tokenization / streaming
       |
Engine Core
  scheduler + KV Cache management
       |
GPU workers / model runner
  model execution + collectives
```

Data Parallel 时可能存在多个 API servers、Engine Cores 与额外 coordination；具体数量取决于 TP、PP、DP 配置。本章不把某个进程数写成永恒接口，重点是 ownership：HTTP lifecycle、scheduling state 和 device execution 不能由多个组件无约束地同时修改。

V1 scheduler 使用 token budget 统一描述待处理工作，使 chunked prefill、prefix hit、Decode 与 speculative tokens 能进入同一调度框架。这比“Prefill queue 加 Decode queue”的静态想象更接近当前实现，但内部 policy 仍会继续演进。

### V0 到 V1：统一的是控制对象，不是阶段物理特征

早期为 Prefill、Decode 和新增 features 分别演化 execution paths 是合理的：它缩短单项能力落地
路径，也保护已有 workload。但随着 prefix reuse、multimodal、compile/CUDA graph 与 speculative
work 组合，feature-specific loops 会复制 scheduler、input preparation 和 worker-state 更新。

V1 的结构变化是把“request 本轮获得多少 token work”提升为统一调度对象，由 Engine Core 拥有
全局 request/KV state，worker 保留 device execution state，并通过增量变化维护 persistent batch。
它降低 path explosion 和 CPU orchestration，却把 correctness 集中到共享 scheduler/KV manager，
新增 lost/out-of-order diff、cancellation reconciliation、stale slot 和 Engine Core recovery 风险。

这条演进不意味着 Prefill 与 Decode 的计算特征消失，也不要求所有旧 deployment 立即迁移。
V0 在缺失 feature、旧硬件或成熟 integration 上仍可能更稳；PD separation 也仍可在 deployment
层拆开两种 phase。应把 V1 alpha 的 feature gaps 和硬件边界留在历史证据中，而不是用后续 stable
文档倒写成 2025 初始实现已经具备的保证。

### nano-vLLM 不是当前 vLLM V1 的架构说明

nano-vLLM 用少量组件重现 request、scheduler、paged KV 与 model runner 的核心
协作，适合阅读 Prefill/Decode 主路径；但它当前采用两个本地队列、Prefill-first
且单轮 phase-exclusive 的调度模型。不能从这些类名和 policy 反向推断 vLLM V1
Engine Core 的完整行为。

两者之间值得迁移的是问题，而不是一一对应的实现：谁拥有 request progress，谁
预留 KV blocks，谁生成 execution metadata，谁在完成或抢占时提交/释放状态。
第42～46章使用 nano-vLLM 回答最小机制，本章仍以 vLLM 官方 V1 文档和目标版本
代码回答生产 engine 的具体架构。

## 一个 Request 的 Engine 流

```text
API server receives request
-> Engine Core admits request
-> KV manager finds cached prefix / allocates blocks
-> scheduler emits scheduled token counts
-> workers execute model
-> Engine Core updates request and KV state
-> output returns to API server
```

若 block allocation 失败，请求不能假装已被调度；若 external KV load 尚未完成，model execution 也不能提前读取。Scheduler output 因此是计算计划和 memory reservation 的联合结果。

## 可复用 KV 首先是一份语义契约

Prefix caching 的复用条件相对清晰：相同、identity-compatible 的 token prefix 在相同
causal history 下产生 KV。把一个 document 独立 Prefill，再放到任意 instruction、history
或 document order 中，问题就不再只是 cache key 与物理搬运。

对于使用 RoPE 的模型，key 可以按目标 position 重新旋转；但 rotation 只修正位置相位，
不能补回 cache 构建时不存在的前序 Context。换言之，KV 不是 document 的无条件 embedding，
而是由 `document + visible causal context + model execution identity` 共同产生的状态。只检查
tensor shape、position 和 checksum，仍可能得到数值可加载、语义不可组合的 cache。

由此形成三条长期并存的分支：

```text
exact prefix reuse
  只复用相同 causal prefix，语义边界最强

position-independent linking + online repair
  允许重排 document，但在请求路径重算部分 context-dependent state

offline semantic cache compilation
  训练 Writer 生成可被固定 Reader 消费的 KV，把在线成本移到训练与 cache construction
```

它们不是“后者替代前者”。Exact prefix reuse 适合重复模板和共享历史；online repair 在
composition 经常变化但可接受额外 TTFT 时保留更强的 request-specific correction；offline
compiler 适合高复用、相对稳定的 document corpus，却新增 compiler/adaptor version、训练域、
cache rebuild、跨域退化与 Reader compatibility。无论采用哪条分支，scheduler 只有在
semantic compatibility 已验证后才能把外部 KV 计为可用 token work。

SemPIC 是第三条分支的实验性证据：它让 LoRA-enabled Writer 通过原生 per-layer KV 接口
接受 behavioral distillation，而 Reader 与 cache-hit decode path 保持不变。论文也保留了
边界——位置独立不等于 Context 独立，attention deviation 与 task quality 仍有 residual，
训练时的 KV gradient checkpointing 还以额外重计算换显存。这里吸收的是 cache
composition contract，不把该预印本写成 vLLM 已支持的功能或生产收益保证。

## KV Cache 从 HBM 分配器演化为分层数据面

PagedAttention 最初解决的是单个 GPU 内部的逻辑 block 到物理 HBM block 映射。随着
prefix reuse、KV transfer 和 offloading 进入 serving engine，KV Cache 的系统边界已经
扩展为：

```text
request / prefix identity
→ HBM cache group
→ host or shared-memory tier
→ object-store tier
```

这里的关键变化不是“多了一层更慢的存储”，而是 KV Cache 从 allocator-owned memory
变成了有 identity、ownership、lifecycle 和 evidence 的数据面。每个 tier 都必须回答：

- 哪个 model revision、adapter、attention backend 与 cache layout 产生了这份 KV；
- 哪个 Data Parallel replica 拥有可写区域，哪些副本只能读取；
- load、hit、miss、eviction 和 transfer failure 如何进入 metrics 与 tracing；
- 远端 object store 的 credential 由谁提供、如何轮换，失败是否允许回退；
- 外部 KV 尚未完成校验与装载时，scheduler 能否把 request 交给 model runner。

vLLM `v0.26.0` 中的 per-KV-cache-group attention backend、tier-owned events、
object-store workload identity 与 DP-replica-aware offload region，是这一演化的版本化
实现证据，不应被写成所有 serving engine 都已经具备的通用能力。但它们揭示了稳定的
系统原则：**一旦 KV 跨越 device boundary，cache key、replica ownership、credential
boundary 与 observability 就成为正确性协议，而不再只是性能参数。**

分层 KV 可以用容量换取 HBM 命中率，并提高跨请求或跨实例复用机会；代价是远端延迟、
序列化与网络带宽进入 token critical path，stale cache 和跨租户泄漏风险也更高。因此
是否启用 offload 不能只看峰值吞吐，而要同时测量目标 workload 下的 hit rate、P99
首 token 延迟、恢复行为、隔离边界和对象存储成本。

分层状态继续扩展后，release unit 也不能只写成“KV backend 版本”。同一 request 的 cache layout、tier
policy、Pipeline connector handshake、scheduler accounting、frontend/parser 与 input validation 必须解析到
一组兼容 revision：

```text
request + protocol identity
→ typed KVCacheSpec / block layout
→ per-request tier and offload lifecycle
→ connector handshake across pipeline ranks
→ scheduler-visible transfer and token accounting
→ parser / frontend result and pre-GPU security gate
```

Cache manager 拥有 layout，tier policy 拥有 load/evict hook，connector 拥有跨 stage transfer completion，
scheduler 只在这些状态验证后推进 token frontier；parser 则不能用协议兼容假设掩盖 request-id、tool-call、
reasoning 或 UTF-8/config validation 差异。vLLM v0.23.0 为这些 owners 同时演进提供 release-scoped evidence，
不证明任意 feature combination 已 production-safe。HBM-only、单 frontend、无 connector 的旧路径在小规模、
稳定 workload 中仍更简单；feature gating 与 fail-fast compatibility 优先于强行组合。

### 从 Whole-cache Offload 到 Sparse Working-set Prefetch

KV tiering 若每层都把完整历史搬回 GPU，只把容量问题变成 PCIe/network bandwidth 问题。长 Agent Decode 的另一
分支是让完整 KV 留在 pinned CPU 或 remote prefill-side memory，预测下一层可能读取的 block/head，只把 working
set 预取进 HBM，并让 prefetch、gather、attention 与 cleanup 流水重叠：

```text
complete cold KV in host / remote tier
→ query-dependent sparse block-head selection
→ versioned prefetch into staging buffers
→ attention consumes only completed working set
→ cleanup / reuse, with dense fallback on miss or drift
```

Tier manager 拥有 location、capacity 与 freshness；selector 拥有 model/workload revision；connector/NIXL path 拥有
transfer completion；scheduler 只有在依赖状态可见后才能推进 token frontier。它用 selector error、prefetch miss、
NUMA/host contention、remote retry 和 staging capacity 换取 HBM residency，不能把“远端更大”写成“推理更快”。
OasisKV 的 vLLM prototype、H100/RoCE 与指定长上下文实验支持机制可行性，不证明其他 interconnect、continuous
multi-tenant arrival 或 tail SLO 下的净收益。Whole-cache offload 在链路充足、实现简单时仍成立；HBM 足够或
selector 不可信时 dense residency 最可靠。

## Dynamic LoRA 进入 Runtime 后改变了什么

第 30 章给出 merge 与动态 adapter 两种资产策略。Merge 后 runtime 看到的是
独立完整权重；动态 LoRA 则让请求身份变成：

```text
base model revision + adapter revision
```

Serving engine 需要管理 adapter load/cache/eviction、base compatibility、rank 与
target-module constraints，并保证 prefix cache key 包含 adapter identity。否则
相同 token prefix 可能错误复用由另一组有效权重产生的 KV。

Multi-adapter batching 也不是把任意 adapters 无成本混入同一 batch。Runtime
必须让每个 token 使用对应低秩增量，kernel/layout 支持、同轮 adapter 数量和
adapter working set 都会影响 batch efficiency。动态 adapter 提高共享 base 的
资产密度，但把第 30、35 章的 lineage 与隔离要求带进 scheduler；是否 merge
应由 workload、变体数量、更新频率和 SLO 共同决定。

### 异步调度跨越 Pipeline Stage 后，Request State 也要分布式提交

单 stage 的异步 scheduler 可以在上一轮 device work 尚未完全返回 CPU 时准备下一轮，减少 host bubble；
同步调度在控制路径较短、调试和取消语义优先时仍更简单。加入 Pipeline Parallel 后，问题不再只是“CPU
是否等待 GPU”，而是多个 stage 对同一 request 的 token frontier 何时达成一致：

```text
Engine Core schedules request/token rows
→ stage 0 starts work and emits ordered handoff
→ downstream stages consume the same schedule epoch
→ final stage returns committed token results
→ Engine Core advances request state or reconciles abort
```

中间 stage 的 completion 不能独立宣告 token 已提交；chunked request、abort/retry 与 empty row 都必须保持
stage ordering 和 row identity，否则下游可能消费旧 activation，CPU 又把同一 token 重排。异步 PP 可以覆盖
host orchestration，却新增 in-flight schedule epoch、cross-stage backpressure、cancellation propagation 与恢复
状态。vLLM v0.16.0 的 release/PR 证明该版本开始支持并修正这一实现路径，不证明任意 PP topology 都会提速；
其公开 benchmark 未完整披露 hardware 与 workload contract，因此正文只保留 distributed request-state
commit 机制。

### 从重建进程到恢复执行状态

容器镜像、权重缓存和预热副本分别减少软件安装、model load 与容量到达等待；当 kernel warmup、graph compile、
CUDA context 和 runtime setup 本身已进入冷启动 critical path，下一步才是保存 host 与 device execution state：

```text
image + immutable weights
→ warmed engine / prewarmed replica
→ quiesce serving runtime
→ checkpoint host process + device mappings/state
→ restore under a compatibility gate
→ rebuild external connections and admit traffic
```

Snapshot owner 必须冻结 model/runtime revision、GPU architecture/topology、driver/CUDA、filesystem、network/
credential freshness 与 quiesce epoch；readiness 只能在 external connections、KV policy 和 health checks 重建后重新
成立。它以更快的 capacity arrival 换来 privileged restore agent、大 artifact、tampering surface、stale file descriptor、
device mismatch 和 multi-node partial restore。小模型、频繁 revision、跨硬件迁移或强 portability 场景继续适合普通
cold start/weight cache；snapshot 不是 image 的普遍替代。

NVIDIA Dynamo Snapshot 证明了 single-GPU preview 路径可以保存这类状态，并明确保留了未 upstream CRIU 优化、
multi-GPU/multi-node 与 live-traffic 空白。本章因此吸收 restore contract，不保留厂商 startup multiplier，也不把
preview 写成 vLLM 当前稳定能力。

## Failure 与 Backpressure

Serving engine 还必须处理客户端断开、GPU worker failure、KV load failure、queue overload 和 tokenizer/model mismatch。Backpressure 应在 admission 和 queue 层显式表现，而不是等待 HBM allocation 失败。

正确性测试要覆盖 prefix hit/miss、block reuse、preemption、cancellation 和相同 prompt 在不同 batch composition 下的输出一致性；性能测试则绑定目标版本，因为 scheduler 与 cache manager 正在快速变化。

## 和 Continuous Batching 的关系

Continuous Batching 让请求在 Decode iteration 之间动态进出。PagedAttention 让这种动态进出不会被连续显存分配拖垮。

二者组合起来，才形成高吞吐 serving：

```text
请求完成 → 释放 KV blocks
新请求进入 → 分配新的 KV blocks
batch 保持饱满 → GPU 利用率提高
```

这也是为什么第46章、第47章和本章应该连着读。Continuous Batching 解决 batch 空洞，PagedAttention 解决 KV memory 动态管理，vLLM 把它们组织成可用系统。

## vLLM 和其他引擎的边界

vLLM 适合把“通用 LLM serving”做成工程产品：API、调度、batching、KV 管理、分布式执行、模型适配。

它和 TensorRT-LLM 的关注点有重叠，但历史主线不同。TensorRT-LLM 更突出面向 NVIDIA GPU 的 engine / kernel / quantization 优化；vLLM 更突出 serving scheduler 与 KV Cache 管理。二者都在持续扩展，不能把这种主线差异误写成互斥功能表。

它和 SGLang 也有重叠。SGLang 论文从 structured language model programs 与 RadixAttention 切入，但当前两者都覆盖更广的 Serving 能力。章节比较应回答“各自用什么核心抽象组织 runtime”，而不是根据某个版本断言只有谁支持某项功能。

## Trade-off

vLLM 把许多系统复杂度封装起来，但使用者仍然需要理解底层约束。

长上下文请求会消耗大量 KV blocks；高并发会放大 scheduler 和 memory manager 压力；多租户场景还要考虑配额、公平性和隔离。

因此学习 vLLM 不能停留在命令行参数，而要看它在知识树中的位置：它是把 LLM runtime 的核心状态管理产品化。

## 本章在知识树中的位置

```text
KV Cache
→ PagedAttention
→ Continuous Batching
→ vLLM
→ KServe LLM / AI Platform
```

vLLM 是从单个推理优化走向 production serving engine 的关键节点。

## 自检问题

1. 为什么 vLLM 不能只理解为 PagedAttention？
2. vLLM 的 scheduler 和 block manager 分别解决什么问题？
3. Continuous Batching 和 PagedAttention 为什么互相依赖？
4. vLLM 和 TensorRT-LLM 的关注点有什么不同？
5. 当前 V1 中 API server、Engine Core 与 worker 的 ownership 怎样划分？
6. 为什么 scheduler output 同时也是 memory reservation decision？
7. KV Cache 跨越 HBM、host memory 与 object store 后，为什么 ownership 和 identity 会成为正确性问题？
8. vLLM 在 AI Platform 中通常处在哪一层？
9. 为什么 nano-vLLM 可用于学习主路径，却不能作为 vLLM V1 的架构证据？
10. 为什么 RoPE re-rotation 不能单独证明 independently compiled KV 可安全组合？

## 小结

vLLM 将 request lifecycle、token scheduling、KV block ownership 和 GPU execution 组织为一个 Serving engine。PagedAttention 是历史起点，V1 Engine Core 才是理解当前系统组合的中心。

第51章继续比较另一种 runtime 抽象：当请求之间存在可复用的程序结构和 prefix tree 时，scheduler 还可以利用哪些信息。

## Review notes

- NVIDIA Dynamo Snapshot（execution-state restore preview；Official Engineering Evidence）:
  https://developer.nvidia.com/blog/nvidia-dynamo-snapshot-fast-startup-for-inference-workloads-on-kubernetes/

本轮 Review 将 vLLM 从“PagedAttention 加 API”扩展为 request state、scheduler、KV Cache manager 与 workers 协作的 serving engine，并把与 TensorRT-LLM/SGLang 的比较改为历史主线而非互斥功能。第46章讲调度粒度，第47章讲 KV paging，本章讲这些机制如何进入完整 runtime。

时效性边界：本章已在 2026-07 按 stable V1 architecture、V1 guide 与 LoRA
feature documentation 核验。进程数量、scheduler policy 和 feature support
仍是版本化实现；稳定结论仅限 ownership 与 request/KV execution contract。

2026-07-30 增补 nano-vLLM 边界说明：将其定位为第42～46章的最小实现案例，
不把教学实现的队列、phase policy 或类结构当作 vLLM V1 的当前架构证据。

Primary-source 校验入口：

- nano-vLLM repository and stated lightweight scope:
  https://github.com/GeeeekExplorer/nano-vllm
- vLLM V1 Architecture Overview: https://docs.vllm.ai/en/stable/design/arch_overview/
- vLLM V1 user guide and unified scheduling boundary: https://docs.vllm.ai/en/stable/usage/v1_guide/
- vLLM V1 alpha architecture announcement（historical boundary）:
  https://blog.vllm.ai/2025/01/27/v1-alpha-release.html
- vLLM LoRA feature documentation: https://docs.vllm.ai/en/stable/features/lora/
- PagedAttention / vLLM paper: https://arxiv.org/abs/2309.06180
- vLLM v0.26.0 release: https://github.com/vllm-project/vllm/releases/tag/v0.26.0
- vLLM PR #47063, workload identity for object-store KV tier:
  https://github.com/vllm-project/vllm/pull/47063
- vLLM PR #47987, DP-replica-aware shared offload region:
  https://github.com/vllm-project/vllm/pull/47987
- vLLM v0.23.0 release（version-sensitive typed request-state evolution）:
  https://github.com/vllm-project/vllm/releases/tag/v0.23.0
- SemPIC（Status: Experimental；position-independent KV 的语义可组合性案例）:
  https://arxiv.org/abs/2607.28069
- vLLM v0.16.0 release（版本事实）: https://github.com/vllm-project/vllm/releases/tag/v0.16.0
- vLLM PR #32618（async scheduling + Pipeline Parallel request-state path）:
  https://github.com/vllm-project/vllm/pull/32618
- OasisKV（sparse off-HBM working-set prefetch；Status: Experimental）:
  https://arxiv.org/abs/2608.08097
