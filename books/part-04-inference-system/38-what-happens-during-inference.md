# 第38章 推理到底发生了什么

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 一个请求从 API 进入，到 token 流式返回，经历哪些阶段。

## 本章要回答的问题

一次 LLM 请求从 API 进入，到第一个 token 返回，再到完整答案流式输出，中间到底发生了什么？

如果把 LLM 推理理解成普通的 HTTP handler，就会错过大模型系统最核心的瓶颈。传统后端服务通常关心 request count、QPS、latency、CPU、memory、network；LLM 推理还必须关心 prompt length、generated tokens、Prefill、Decode、KV Cache、batch shape、GPU memory、memory bandwidth 和调度策略。

换句话说，LLM 推理不是一次普通函数调用，而是一段持续演化的计算过程。

## 从“调用模型”到“生成 token”

最简单的理解是：用户输入 prompt，模型返回 answer。

这个说法对产品接口是成立的，但对系统设计太粗了。对于 decoder-only LLM 来说，生成答案本质上是一个自回归过程：模型每次只预测下一个 token，然后把这个 token 接回上下文，再继续预测下一个 token。

因此，一个请求在系统内部通常可以拆成两个关键阶段：

```text
Request
→ Tokenize
→ Prefill
→ Decode loop
→ Detokenize / stream output
```

`Tokenize` 把文本变成 token id。`Prefill` 一次性处理已有 prompt，建立模型对上下文的内部状态。`Decode` 则逐 token 生成，每一步都依赖前面已经生成的内容。

这就是 LLM 推理和普通模型推理的第一处分叉：它不是输入一次、前向一次、输出一次，而是先处理上下文，再进入一个逐步生成的循环。

## Prefill 和 Decode 为什么必须分开看

Prefill 阶段处理的是已有 prompt。假设用户输入了 2000 个 token，模型需要一次性计算这些 token 在每一层中的表示，并生成后续 Decode 所需的 Key / Value 状态。这个阶段的计算量大，但并行度也高，因为 prompt 中所有 token 可以以矩阵形式批量处理。

Decode 阶段则不同。每一步只新增一个 token。模型需要基于当前 token 和历史 KV Cache 生成下一个 token。因为第 `t+1` 个 token 依赖第 `t` 个 token，Decode 天然带有串行性。

所以二者的资源画像不同：

```text
Prefill: 计算密集，矩阵规模大，并行度高
Decode : 访存密集，逐 token 串行，对 KV Cache 访问敏感
```

这是常见 workload 下的第一阶直觉，不是硬件无关的定律。短 prompt、小模型或低 batch 的 Prefill 也可能没有充分利用计算单元；较大 Decode batch、量化和不同模型结构也会改变算术强度。更严谨的判断应来自目标 workload 上的 profile。推理系统的第一条主线仍然成立：加速不能只说“让模型跑得更快”，而要先拆清楚到底是在加速 Prefill、Decode，还是二者之间的调度。

## 一次请求的系统路径

从平台视角看，一次 LLM 请求大致会经过这些层：

```text
Client
→ Gateway / API Server
→ Router / Scheduler
→ Tokenizer
→ Runtime / Inference Engine
→ GPU Worker
→ KV Cache Manager
→ Detokenizer
→ Streaming Response
```

Gateway 负责认证、限流、路由和协议适配。Scheduler 决定请求何时进入 batch、和哪些请求一起执行。Runtime 加载模型权重，并调度 GPU kernel。KV Cache Manager 管理每个请求的历史 attention state。Detokenizer 把 token id 还原成用户能读的文本，并通过 stream 返回。

这条路径里，模型只是其中一层。真正的 serving engine 要同时管理计算、内存、请求生命周期和输出流。

## 为什么加速目标不是单一指标

推理系统的优化目标可以先拆成三个维度：latency、throughput、cost。

`Latency` 关注用户等待时间，尤其是 `TTFT` 和 `TPOT`。用户是否觉得“卡”，通常不只取决于完整答案总耗时，还取决于第一个 token 什么时候出现，以及后续 token 是否持续稳定流出。

`Throughput` 关注单位时间内系统能生成多少 token 或处理多少请求。GPU 很昂贵，如果 batch 和调度设计不好，GPU 会因为等待、显存碎片或 batch 空洞而空转。

`Cost` 关注单位 token 或单位请求消耗的资源。模型越大、上下文越长、输出越长，成本越高。部署阶段常见的 KV Cache、量化、图优化、batching、speculative decoding，本质上都在试图用更少资源完成更多生成。

这三个目标不是总能同时优化。低 latency 往往倾向小 batch，高 throughput 往往倾向大 batch；低 cost 可能要求量化或更小模型，但质量又可能受到影响。因此推理系统是一个多目标权衡问题，而不是单纯“跑快一点”。

本书后续统一使用几个指标：

- `TTFT`：time to first token，主要受排队、tokenize、Prefill、KV Cache 写入和调度影响。
- `TPOT`：time per output token，也可理解为稳定生成阶段的 inter-token latency，主要受 Decode、KV Cache 读取、batching 和调度影响。
- `Throughput`：单位时间完成的 token 或请求量，通常和 batch occupancy、GPU utilization、KV memory capacity 相关。
- `Goodput`：在 TTFT、TPOT 等 SLO 约束内完成的有效请求速率。它防止系统用牺牲用户延迟的方式制造表面吞吐。

一次请求的端到端时间可以粗略拆成：

```text
request latency
≈ queue time
 + tokenize / routing overhead
 + prefill service time
 + decode iterations
 + stream / detokenize overhead
```

这也解释了为什么只有 GPU kernel profile 不足以证明服务更快：排队、batch admission、KV memory 和跨节点通信都可能主导用户可见延迟。

## 慢在哪里

大模型推理慢，至少有四类原因。

第一，模型参数规模大。每一步推理都需要读取大量权重并进行矩阵计算。即使计算单元足够强，权重和中间状态在不同 memory hierarchy 之间移动也会产生巨大开销。

第二，memory wall 明显。GPU HBM 带宽很高，但相比片上 SRAM / cache 仍然慢得多。许多优化并不是减少数学计算本身，而是减少 HBM 读写，或者把数据尽可能留在更快的片上存储里。

第三，attention 受序列长度影响。Prefill 阶段的 attention 需要处理 prompt 内 token 之间的关系，长上下文会放大计算和显存压力。后续章节会看到，FlashAttention、Ring Attention、ShadowKV 等技术都在不同层面回应这个问题。

第四，自回归 Decode 串行。生成 1000 个 token，不是一次性生成 1000 个位置，而是循环执行 1000 次。KV Cache 可以避免重复计算历史上下文，但它也把历史状态变成了显存压力。

## 为什么推理系统会演化出这么多技术

从这个视角看，后面的推理加速技术不是零散技巧，而是在回答不同瓶颈：

- KV Cache：减少 Decode 阶段对历史 token 的重复计算。
- Continuous Batching：减少不同请求生成长度不同造成的 GPU 空洞。
- PagedAttention：减少 KV Cache 动态增长带来的显存碎片和浪费。
- Speculative Decoding：缓解逐 token 串行生成的瓶颈。
- FlashAttention：减少 attention 计算中对 HBM 的中间矩阵读写。
- Quantization：降低权重和可能的 activation / cache 存储与带宽压力。
- PD 分离：把 Prefill 和 Decode 两种不同资源画像拆成不同部署单元。

这些技术共同说明：LLM 推理系统的核心战场在于 **token 生成过程中的计算、内存和调度协同**。

## 本章在知识树中的位置

本章是 Part IV 的入口。它不深入某一个优化算法，而是建立推理系统的基本地图：

```text
推理到底发生了什么
→ Prefill
→ Decode
→ KV Cache
→ Continuous Batching
→ PagedAttention
→ Speculative Decoding
→ TensorRT-LLM / vLLM / SGLang
→ GPU Memory
→ PD 分离
→ 推理调度
```

后续每一章都可以回到这个入口问题：它到底在优化 LLM 推理路径中的哪一段？

这组章节的内部阅读顺序可以理解为三层：

```text
阶段层：Prefill / Decode / KV Cache
机制层：Continuous Batching / PagedAttention / Speculative Decoding / GPU Memory / PD 分离
引擎层：TensorRT-LLM / vLLM / SGLang / 推理调度
```

阶段层回答“请求发生了什么”；机制层回答“瓶颈如何被重新组织”；引擎层回答“这些机制如何进入生产 runtime”。

## 自检问题

1. 为什么 LLM 推理不能简单类比普通 HTTP 服务？
2. Prefill 和 Decode 的资源画像有什么不同？
3. 为什么 request count 不能充分描述 LLM serving 负载？
4. `TTFT` 和 throughput 为什么可能互相冲突？
5. KV Cache 为什么既是加速手段，也是显存压力来源？
6. 如果一个推理系统 GPU 利用率很低，可能有哪些原因？
7. 为什么 PD 分离会从 Prefill / Decode 差异中自然出现？

## Review notes

本轮 Review 为 Prefill/Decode 的资源画像增加了适用条件，并把 queue time、service time、throughput 与 SLO goodput 放进同一条请求路径。后续章节中的任何“更快”都应说明改善了哪个阶段、哪个指标，以及是否牺牲其他约束。

Primary-source 校验入口：

- DistServe 对 TTFT / TPOT 与 Prefill / Decode 干扰的定义和问题化： https://arxiv.org/abs/2401.09670
- Orca 对 iteration-level scheduling 的问题化： https://www.usenix.org/conference/osdi22/presentation/yu
