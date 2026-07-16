# 第19章 KV Cache

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Status:** Draft

**Roadmap Intent:** 为什么生成时要缓存历史 Key/Value，它如何改变推理系统设计。

## 本章要回答的问题

Decoder-only 模型每次只生成一个新 token。如果前缀中历史 token 的 K/V 已经计算过，为什么还要在下一步重新投影？KV Cache 保存什么、为什么不保存 Query，又怎样从模型优化变成运行时状态？

本章的核心判断是：**KV Cache 用逐层保存历史 Key/Value，避免自回归 Decode 重复计算不变前缀；它用显存与状态管理换取更少计算。**本章解释 cache 的模型来源和 shape；Part IV 第41章负责 runtime capacity、生命周期、复用与 offload，第43章负责分页映射，第52章负责调度。

## 不使用 Cache 会重复什么

假设 prefix 已有 `t` 个 tokens，要生成第 `t+1` 个 token。最朴素做法是把完整 prefix 再送入所有 `L` 个 Transformer layers：

```text
[x_1,...,x_t]
-> recompute Q/K/V for every historical token
-> recompute all layer hidden states
-> use last position logits
```

下一步 prefix 变成 `t+1`，系统又从头处理 `[x_1,...,x_(t+1)]`。历史 token 的表示在 causal model 中不会因未来 token 出现而改变：位置 `i` 不能读取 `j>i`，因此它对应的 K/V 是可复用的。

如果仍反复重算，生成越长，重复工作越多。

## 为什么缓存 Key 和 Value

第14章单 head Attention：

```text
Attention(q_t,K_<=t,V_<=t)
= softmax(q_t K_<=t^T / sqrt(d_h) + mask) V_<=t
```

生成新 token 时，只需要新位置的 Query 去匹配全部历史 Keys，并聚合历史 Values。历史 K/V 已由各自 hidden state 投影得到，可以追加保存：

```text
K_cache = [k_1,k_2,...,k_t]
V_cache = [v_1,v_2,...,v_t]
```

新一步只计算：

```text
q_(t+1), k_(t+1), v_(t+1)
```

然后：

```text
K_cache <- append(k_(t+1))
V_cache <- append(v_(t+1))
```

## 为什么不缓存历史 Query

Query 表示“当前位置要读取什么”。生成第 `t+1` 个 token 时，需要的是新位置的 `q_(t+1)`；历史 `q_i` 已经完成过自己的读取，不会被未来位置再次用作 Key 或 Value。

同理，历史 Attention output 和 MLP output 也不直接供新 Query 匹配。真正跨 Decode steps 被 attention 读取的是每层历史 K/V，因此 cache 只保留它们。

这不是说其他中间状态毫无价值，而是它们不属于标准自回归 Attention 的最小可复用状态。

## 每层 Cache 的 shape

设：

- `B`：当前 cache batch/request 数。
- `T`：已缓存 sequence length。
- `H_kv`：Key/Value head 数。
- `d_h`：每个 head dimension。
- `L`：Transformer layer 数。

每层逻辑 shape 通常表示为：

```text
K_cache_l [B,H_kv,T,d_h]
V_cache_l [B,H_kv,T,d_h]
```

有些实现使用 `[B,T,H_kv,d_h]` 或分块 layout。逻辑元素数量相同，物理 layout 会影响 kernel 和 memory manager。

整个模型需要为每个 Attention layer 保存一组 K/V：

```text
KV elements = 2 * L * B * T * H_kv * d_h
```

若每个元素占 `b` bytes：

```text
KV bytes = 2 * L * B * T * H_kv * d_h * b
```

公式里的 `2` 表示 Key 与 Value，不是 double buffering。

这个写法假设 batch 内每个请求都按同一长度 `T` 计量。若活跃请求长度分别为 `T_r`，更准确的逻辑元素数是：

```text
KV elements = 2 * L * H_kv * d_h * sum_(r=1)^B T_r
```

`B*T` 可以是等长 batch 的精确值，也可以是 padding 后的容量上界；生产 runtime 的实际物理占用还会受 block size、alignment、replication 和 metadata 影响。

## 一个容量小例子

取一个极小模型：

```text
L = 2
B = 1
T = 4
H_kv = 2
d_h = 3
b = 2 bytes
```

KV Cache 为：

```text
2 * 2 * 1 * 4 * 2 * 3 * 2
= 192 bytes
```

若只把 `T` 从 4 增到 8，其他条件不变，cache 变成 384 bytes，呈线性增长。真实模型的 `L`、`T`、并发和 head dimensions 大得多，因此 KV Cache 会成为显存容量主项。

## Prefill 与 Decode 怎样写 Cache

Prefill 已知完整 prompt，可以并行计算 `T_prompt` 个 positions：

```text
prompt ids [B,T_prompt]
-> all layers
-> write K/V for every prompt position
```

完成后，每层 cache 长度为 `T_prompt`。

Decode 每步只有一个新 token：

```text
new token [B,1]
-> compute one new K/V per layer
-> read historical cache
-> append new K/V
-> cache length T <- T+1
```

因此 Prefill 主要批量创建状态，Decode 逐步读取并增长状态。Part IV 会进一步分析两阶段的 compute、bandwidth 与调度差异。

## 计算复杂度怎样变化

无 cache 时，第 `t` 步重新运行长度 `t` 的完整序列。仅 dense Attention 的前缀成对计算约为 `O(t^2)`，MLP/projection 也对全部 `t` 个 positions 重做。跨多个生成 steps 累积会非常昂贵。

有 cache 后，第 `t` 步只为新 token 做 projection 和 MLP，并让一个 Query 读取 `t` 个 Keys/Values：

```text
per-step attention ~ O(t * d_h) per head
```

跨输出长度求和仍随总生成长度近似二次增长，因为每个新 Query 要读取更长历史；KV Cache 没有让 Attention 变成常数成本。它消除的是对历史 token projection 与 hidden states 的重复计算。

所以应避免模糊地说“KV Cache 把所有推理从 O(n^2) 变成 O(n)”。必须注明是在比较单个 Decode step、Attention 部分还是完整生成过程。

## MHA、GQA、MQA 怎样影响容量

第15章已经定义：

```text
MHA: H_kv = H
GQA: 1 < H_kv < H
MQA: H_kv = 1
```

在其他变量相同时，KV bytes 与 `H_kv` 成正比。假设 `H=32`：

```text
MHA H_kv=32
GQA H_kv=8   -> cache约为MHA的1/4
MQA H_kv=1   -> cache约为MHA的1/32
```

这是逻辑元素数比较，不含 alignment、block allocation 和 metadata。减少 KV heads 可能影响模型质量与训练方式，属于架构 trade-off，不是 runtime 免费压缩。

## Position 与 Cache 的一致性

缓存的 K 通常已经应用对应位置的 RoPE 或其他位置机制。Decode 新 token 必须使用正确 position index，否则新 Query 与历史 Keys 的相对几何错误。

Prefix reuse 也要求模型配置、token ids、position ids、adapter 和相关 Attention 语义兼容。文本看起来相同但 normalization、special tokens 或 position 编号不同，cache 都未必可复用。

## Cache 没有解决什么

第一，它不减少模型权重。Decode 每步仍要执行每层 projection、MLP、Norm，并读取大量 weights。

第二，它不消除自回归依赖。下一 token 仍要等待上一步 token 被选择。

第三，它不消除历史读取。每步 Query 仍要访问已有 K/V，长上下文会增加 memory bandwidth。

第四，它不保证容量可管理。不同请求长度、生命周期和并发会造成动态分配、碎片和调度问题。

KV Cache 把重复计算问题转化为显存与状态问题，而不是让推理免费。

## 从模型状态到 Runtime 对象

模型公式只要求 K/V 可访问，生产 runtime 还必须决定：

- Cache 放在哪张 GPU。
- 怎样分块、分配与释放。
- 请求能否进入 batch。
- Prefix 是否可以复用。
- 是否 offload、迁移或跨 Prefill/Decode worker 传输。
- 抢占和失败时怎样处理状态。

这些属于第41～43章及后续推理系统。本章不提前展开 PagedAttention 或 scheduler，只建立它们必须管理的对象来源。

## 本章在知识树中的位置

```text
Decoder-only autoregressive loop
-> historical K/V are invariant
-> per-layer KV Cache [B,H_kv,T,d_h]
-> Prefill writes / Decode appends
-> GPU memory manager and scheduler
```

本章是 Part II 从模型机制通向 Part IV 的关键桥梁。第20章继续处理每步 logits 的 token 选择；第41章从 runtime 生命周期重新审视 cache，第43章改变其物理 placement，第50～52章再把它纳入 HBM、PD 与调度约束。

## 自检问题

1. Causal mask 为什么使历史 K/V 在未来生成中保持可复用？
2. 为什么缓存 K/V 而不缓存历史 Query？
3. 每层 K/V 的逻辑 shape 是什么？
4. `KV bytes` 公式中的各变量分别表示什么？
5. 小例子中 `T` 翻倍为什么 cache 也翻倍？
6. Prefill 与 Decode 怎样写入 cache？
7. 为什么 KV Cache 没有让完整生成变成线性或常数成本？
8. GQA/MQA 通过哪个变量降低 cache？
9. Position id 错误为什么会污染 cached K？
10. 第19、41、43、52章分别负责 KV Cache 的哪一层问题？

## 小结

KV Cache 利用 causal model 的不变量：未来 token 不会改变历史位置已计算的 K/V。保存这些逐层状态后，Decode 只处理新 token，并让新 Query 读取历史 cache。

它显著减少重复计算，却让每个请求拥有随长度增长的显存状态。`L`、`T`、`H_kv`、`d_h`、dtype 和并发共同决定容量，这正是模型架构开始约束推理 runtime 的位置。

## Review notes

本轮联章 Review 补充了变长请求下按 `sum T_r` 计算的逻辑容量，避免把等长 batch 公式误当成所有 runtime 的实际占用。本章仍只负责 KV Cache 的模型推导、shape、容量与 Prefill/Decode 写入语义。分页、碎片、prefix caching、offload、调度和 PD 传输保留给 Part IV。

Primary-source 校验入口：

- Noam Shazeer, "Fast Transformer Decoding: One Write-Head is All You Need", 2019: https://arxiv.org/abs/1911.02150
- Reiner Pope et al., "Efficiently Scaling Transformer Inference", 2022: https://arxiv.org/abs/2211.05102
- Joshua Ainslie et al., "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints", 2023: https://arxiv.org/abs/2305.13245
