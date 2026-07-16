# 第46章 vLLM

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 以 PagedAttention 和调度为核心的大模型 Serving 引擎。

## 本章要回答的问题

vLLM 为什么会成为 LLM Serving 的代表性引擎？如果第43章已经讲了 PagedAttention，那么 vLLM 章节还应该讲什么？

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

## Dynamic LoRA 进入 Runtime 后改变了什么

第 26 章给出 merge 与动态 adapter 两种资产策略。Merge 后 runtime 看到的是
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
资产密度，但把第 26、31 章的 lineage 与隔离要求带进 scheduler；是否 merge
应由 workload、变体数量、更新频率和 SLO 共同决定。

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

这也是为什么第42章、第43章和本章应该连着读。Continuous Batching 解决 batch 空洞，PagedAttention 解决 KV memory 动态管理，vLLM 把它们组织成可用系统。

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
7. vLLM 在 AI Platform 中通常处在哪一层？

## 小结

vLLM 将 request lifecycle、token scheduling、KV block ownership 和 GPU execution 组织为一个 Serving engine。PagedAttention 是历史起点，V1 Engine Core 才是理解当前系统组合的中心。

第47章继续比较另一种 runtime 抽象：当请求之间存在可复用的程序结构和 prefix tree 时，scheduler 还可以利用哪些信息。

## Review notes

本轮 Review 将 vLLM 从“PagedAttention 加 API”扩展为 request state、scheduler、KV Cache manager 与 workers 协作的 serving engine，并把与 TensorRT-LLM/SGLang 的比较改为历史主线而非互斥功能。第42章讲调度粒度，第43章讲 KV paging，本章讲这些机制如何进入完整 runtime。

时效性边界：本章已在 2026-07 按 stable V1 architecture、V1 guide 与 LoRA
feature documentation 核验。进程数量、scheduler policy 和 feature support
仍是版本化实现；稳定结论仅限 ownership 与 request/KV execution contract。

Primary-source 校验入口：

- vLLM V1 Architecture Overview: https://docs.vllm.ai/en/stable/design/arch_overview/
- vLLM V1 user guide and unified scheduling boundary: https://docs.vllm.ai/en/stable/usage/v1_guide/
- vLLM LoRA feature documentation: https://docs.vllm.ai/en/stable/features/lora/
- PagedAttention / vLLM paper: https://arxiv.org/abs/2309.06180
