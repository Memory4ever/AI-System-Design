# 第41章 为什么 KV Cache 能提速

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 避免重复计算历史上下文，是 LLM 推理系统的核心状态。

## 本章要回答的问题

第19章已经从模型机制解释历史 K/V 为什么可复用。到了 Serving runtime，KV Cache 为什么会成为请求身份、显存容量、调度和跨节点传输的共同状态？它节省了哪些计算，仍保留哪些成本？容量怎样由模型结构、上下文长度和并发共同决定？

本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**

```text
L       Transformer layer count
H_kv    key/value head count
d_h     head dimension
b       bytes per element
T_r     current cached tokens of request r
```

## 如果完全不缓存

Prompt 长度为 `T_p`，已经生成 `i` 个 tokens 时，朴素 Decode 可以把全部 `T_p+i` 个 tokens 再送入模型，只取最后位置 logits。

```text
step 1: recompute T_p tokens
step 2: recompute T_p + 1 tokens
step 3: recompute T_p + 2 tokens
...
```

历史 positions 的 projections、Attention、MLP 和 layer outputs 被反复重算，但 causal mask 保证未来 tokens 不会改变历史位置已经得到的 K/V。这正是可缓存的不变量。

## 为什么缓存 K/V 而不是 Query

当前新 Query 需要和全部历史 Keys 比较，并用 Attention weights 聚合历史 Values：

```text
score_t  = Q_t * K_<=t^T
output_t = softmax(score_t) * V_<=t
```

未来 step 会产生新的 `Q_t+1`，旧 Query 不再作为被检索内容；历史 K/V 却被每一个未来 Query 使用。因此 runtime 保存 K/V，而不是完整历史 Q。

KV Cache 后每步仍需为新 token 运行全部 layers、读取历史 K/V、写入新 K/V。它没有让完整 Decode 变成常数成本，只消除了历史 tokens 的重复 layer computation。

## 逻辑 Shape 与容量公式

每层每个请求：

```text
K_l: [H_kv, T_r, d_h]
V_l: [H_kv, T_r, d_h]
```

每 token、跨所有 layers 的逻辑容量：

```text
KV_bytes_per_token
= 2 * L * H_kv * d_h * b
```

多个变长请求：

```text
M_KV_logical
= sum_r(T_r) * 2 * L * H_kv * d_h * b
```

它不包含 block internal fragmentation、allocator metadata、alignment、temporary workspace 和 reserve，因此不是实际 HBM 峰值。

## 一个容量小例子

```text
L    = 32
H_kv = 8
d_h  = 128
b    = 2 bytes
```

则：

```text
KV bytes/token
= 2 * 32 * 8 * 128 * 2
= 131072 bytes
= 128 KiB
```

一个缓存 8192 tokens 的请求，逻辑 KV 容量约为 1 GiB；八个同长度请求约需 8 GiB，仅计算 KV。这个例子不是具体模型 benchmark，只说明 `L`、`H_kv`、`d_h`、dtype、length 和 concurrency 如何相乘。

GQA/MQA 通过降低 `H_kv` 减少 cache，并不要求 query head count 同比例下降。

## KV Cache 的生命周期

```text
reserve / allocate
-> Prefill writes prompt blocks
-> Decode appends new positions
-> optionally share prefix blocks
-> evict or offload under pressure
-> free after finish / cancel / failure
```

关键不是“有一块 tensor”，而是每个 logical position 映射到哪个 physical block、由谁拥有、是否仍被其他请求引用。

### Prefix reuse

若多个请求拥有完全一致且 identity-compatible 的 prefix，runtime 可以复用已计算 KV blocks，减少 Prefill。匹配条件不仅是文本相同，还包括 token ids、model revision、adapter、position 与 execution identity。

共享 block 若随后需要被某个分支修改，应使用不可变 prefix 或 Copy-on-Write 语义，避免请求间污染。

### Eviction 与 Offload

当 HBM 不足时，系统可以拒绝请求、evict 并 recompute、offload 到 CPU/远端层级，或 preempt 请求让其他工作先运行。

Offload 只在 transfer cost 小于 recomputation 或 SLO 损失时有价值。更大的远端容量不会自动变成更高性能。

## 一致性不变量

读取 cache 前至少保证：

- Request position 与 cached length 一致。
- Block table 不引用已释放或重分配 block。
- K/V dtype、layout 与 Attention kernel 兼容。
- Model、adapter、RoPE/position configuration 一致。
- PD transfer 完成后数据对 Decode 可见。
- Cancellation 与 failure 不产生 use-after-free。

很多 KV bug 不会表现为 crash，而会产生流畅但错误的 token。系统验证不能只看 memory safety，还要用 deterministic prompts 对比分页、迁移或复用前后的 logits/token sequence。

## 从连续 Tensor 到 Block 管理

最简单的实现为每个请求预留最大连续 KV buffer。它访问简单，但输出长度未知，预留造成浪费；请求动态完成还会留下外部碎片。

按需扩展连续 buffer 又可能需要重新分配与复制。于是 runtime 将逻辑序列拆成固定大小 blocks，并通过 block table 建立映射。第43章的 PagedAttention 正是在这个约束下出现。

## 与第19章的职责边界

第19章负责 causal Attention 为什么允许复用、模型 shape 和 Prefill/Decode 写入语义。本章负责 cache 作为 request-owned runtime state 的容量、lifecycle、reuse、eviction 与 correctness。

两章共享公式，但系统职责不同。

## 本章在知识树中的位置

```text
causal model invariant
-> per-layer KV state
-> request memory ownership
-> dynamic allocation and sharing
-> Continuous Batching
-> PagedAttention
-> distributed KV transfer
```

KV Cache 将第40章 Decode loop 连接到后续 memory manager 和 scheduler。下一章先解决 active requests 为什么必须在每个 iteration 动态重组。

## 自检问题

1. 为什么未来 token 不会改变历史 K/V？
2. 为什么保存 K/V 而不是历史 Query？
3. KV Cache 消除了哪些重算，又保留哪些随历史长度增长的工作？
4. 容量公式中的系数 2 来自哪里？
5. GQA/MQA 通过哪个变量降低 cache？
6. Prefix reuse 为什么需要 model 与 position identity？
7. Eviction、offload 和 recomputation 分别交换什么？
8. 为什么 KV corruption 可能不触发 crash？

## 小结

KV Cache 是 LLM Serving 的核心状态契约：它以显存换取历史 computation reuse，让 Decode 只推进新位置。与此同时，每个 active request 都拥有随长度增长的 state，runtime 必须管理 allocation、sharing、transfer 和 release。

下一章讨论 Continuous Batching：请求长度和结束时间不同，scheduler 怎样在每一轮重新组合这些携带 KV state 的请求。

## Review notes

本轮将模型层公式扩展为多请求 runtime capacity，并加入 lifecycle、prefix identity、eviction/offload 和 correctness invariants。分页实现留给第43章，完整 HBM budget 留给第50章，跨 worker transfer 留给第51章。

Primary-source entry points：

- Multi-Query Attention: https://arxiv.org/abs/1911.02150
- GQA: https://arxiv.org/abs/2305.13245
- PagedAttention / vLLM: https://arxiv.org/abs/2309.06180
