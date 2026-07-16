# 第40章 Decode

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 逐 token 生成阶段串行性强，延迟敏感。

## 本章要回答的问题

Prefill 已经并行读完整段 prompt，为什么不能一次性生成完整答案？Decode 每一步读取和写入什么？为什么它常表现为 memory-bandwidth-sensitive，又为什么增大并发有时能改善效率、同时恶化单请求 latency？

本章的核心判断是：**Decode 是受 autoregressive dependency 约束的逐 token 状态机；单请求每一步的矩阵维度很小，却需要读取大量 weights 和历史 KV，因此性能由 memory movement、batch composition 与 iteration cadence 共同决定。**

本章使用 `R` 表示本轮 active requests，`T_r` 表示请求 `r` 当前历史长度，`d_model` 表示 hidden dimension，`V` 表示 vocabulary size。

## 为什么不能并行写出未来 Token

语言模型定义：

```text
p(y_1,...,y_T_o | x)
= product_i p(y_i | x, y_<i)
```

要计算 `y_i` 的分布，必须先知道实际选择的 `y_<i`。Sampling 可能使下一 token 不等于当前最高概率 token，stop conditions 也会动态结束请求。因此不能把未知的未来 positions 当作 Prefill 中已知的 prompt positions 一起 exact 执行。

这不是 GPU 不够强，而是计算图中存在真实 data dependency。

## 一次 Decode Step

对每个 active request，本轮输入通常只有最新 token：

```text
new token ids       [R, 1]
new hidden states   [R, 1, d_model]
Q_new               [R, H, 1, d_h]
K_new, V_new        [R, H_kv, 1, d_h]
historical K/V      variable T_r
next logits         [R, V]
```

逻辑流程是：

```text
read latest token
-> run all Transformer layers
-> each new Q attends to historical K/V
-> produce logits
-> sample / constrain next token
-> append K_new,V_new
-> stream token
-> update request state
```

Runtime 可能使用 packed token representation，因此物理 tensor 不一定真有 `[R,1,...]` 形状；逻辑上每个 request 仍只推进一个或少量 verified positions。

## KV Cache 消除了什么

KV Cache 避免对历史 tokens 重算 K/V 和完整 layer forward，但当前 Query 仍需读取历史 K/V 并完成 Attention。随着 `T_r` 增长：

- 新 token 的 projection/MLP work 大致不随历史长度增长。
- Attention 读取的 KV bytes 与 `T_r` 近似线性增长。
- Cache 本身也每步追加。

所以“有 KV Cache 后 Decode 是 O(1)”是错误的。它消除大量重复 work，却没有消除新 Query 与完整历史交互。

## 为什么单请求难以喂满 GPU

单请求每步只提供一个 token 的 dense projections。大权重矩阵需要从 HBM 读取，但矩阵的一侧很窄，weight reuse 有限。GPU compute units 可能在等待数据。

将多个 requests 合并后，同一份 weights 可以服务更多 tokens：

```text
single request: X [1, d] * W [d, 4d]
R requests:     X [R, d] * W [d, 4d]
```

`R` 增大通常提高 arithmetic intensity 和 token throughput，但会增加 KV 占用、每轮 work 和排队。更高吞吐并不自动意味着更低 TPOT。

## MoE 怎样改变 Decode 的执行形态

第 21 章说明 MoE 只激活部分 experts，第 36 章说明训练时 Expert Parallel 需要
token dispatch 与 All-to-All。这个模型契约会继续进入推理：每个 Decode
iteration 的 active tokens 先经 router 形成 expert assignments，再被发送到
持有目标 experts 的 ranks，执行较小的 expert GEMMs，最后合并回原 token
顺序。

```text
decode token states
-> router top-k assignments
-> expert dispatch / All-to-All
-> expert compute
-> combine outputs
```

单请求 Decode 的 token 数很少时，expert batch 可能过小，communication 和
launch overhead 更难摊薄；Continuous Batching 可以增加同轮 active tokens，
却也可能产生 expert load imbalance。MoE 降低的是每 token active parameter
compute，不自动降低权重驻留、跨 rank communication 或 TPOT。推理 runtime
可以重新选择 `TP/EP` layout，但不能改变 checkpoint 定义的 router 和 expert
语义。

## TPOT 与 Decode Cadence

一次 Decode iteration 的 wall time 不一定等于请求的 token interval。请求可能因 priority、preemption、KV transfer 或资源不足跳过某轮。

```text
TPOT
= scheduled execution time
 + waiting between eligible iterations
 + sampling / detokenization / streaming overhead
```

Engine kernel 变快若没有改变 queueing 与 eligibility，用户 TPOT 改善可能有限。

## 一个小规模调度例子

| Request | 历史长度 | 剩余上限 | 状态 |
| --- | ---: | ---: | --- |
| A | 100 | 2 | decoding |
| B | 1000 | 20 | decoding |
| C | 50 | 0 | finished |

本轮只应调度 A、B。C 必须退出 active set 并释放 KV。A 两轮后结束，新请求可以补入它留下的 token/memory budget，而不必等待 B。

Static batch 会让 A 的空位一直跟随 B；iteration-level scheduling 则在每轮重新形成 active batch。

## Decode 的结束条件

模型侧包括 EOS、stop token/sequence、最大输出长度和 grammar state 终止；系统侧包括 client cancellation、deadline、quota 和 worker/transfer failure。

结束条件必须与 sampling、detokenization 和 stream 一致。例如 stop string 可能跨 token boundary，系统不能只检查最后一个 token id。

## 常见优化分别改了什么

| 优化 | 主要改变 |
| --- | --- |
| Quantization | 降低 weights/KV bytes，可能增加转换或精度风险 |
| Continuous Batching | 提高跨请求 weight reuse |
| PagedAttention | 改善 KV allocation 与并发容量 |
| Speculative Decoding | 每次 target verification 推进多个 tokens |
| Prefix Cache | 跳过重复 prefix 的部分 Prefill |
| PD Disaggregation | 隔离 Prefill 对 Decode cadence 的干扰 |

它们都没有否定 autoregressive dependency，而是在计算、memory 或 scheduling 层改变执行方式。

## 工程观测

只监控 GPU utilization 不足以判断 Decode，还需观察：

- iteration latency 与 scheduled tokens。
- active / waiting requests。
- 每请求历史长度分布。
- KV utilization、allocation failure、preemption。
- TPOT P50/P95/P99。
- tokens/s 与满足 TPOT SLO 的 goodput。
- sampling、detokenization 和 stream queue latency。

高 utilization 可能来自一个长 iteration；如果它阻塞大量请求，系统仍可能交付较差的 tail latency。

## 本章在知识树中的位置

```text
Prefill
-> initial KV state
-> repeated Decode iterations
-> logits / sampling
-> append token and KV
-> finish or reschedule
```

本章承接第39章的 Prefill 输出，并把“逐 token 推进”交给第41章解释其核心状态。第42章将解决不同长度请求如何共享 GPU。

## 自检问题

1. Autoregressive factorization 为什么造成真实时间依赖？
2. Decode 的 logical shape 与 Prefill 有何不同？
3. KV Cache 消除了哪些 work，又保留了什么？
4. 为什么单请求 Decode 常难以充分复用 weights？
5. 增大 active batch 为什么可能同时提升吞吐并恶化 TPOT？
6. Iteration latency 为什么不必然等于请求 TPOT？
7. Speculative Decoding 是否消除了 autoregressive dependency？

## 小结

Decode 把模型推理变成持续的状态推进问题。每个请求内部必须按 token 顺序执行，但多个请求可以共享每轮模型执行。性能不只取决于 kernel，还取决于谁进入这一轮、携带多长历史以及何时再次获得资格。

下一章聚焦最重要的持久状态：KV Cache 为什么正确、节省了什么，以及它怎样把计算优化转化为显存管理问题。

## Review notes

本轮补齐 autoregressive factorization、logical shapes、TPOT 时间边界和 batch 小例子，并明确“Decode memory-bound”是由 workload 与 arithmetic intensity 决定的工程判断。

Primary-source entry points：

- Orca: https://www.usenix.org/conference/osdi22/presentation/yu
- DistServe: https://arxiv.org/abs/2401.09670
- Speculative Decoding: https://arxiv.org/abs/2211.17192
