# 第41章 为什么 KV Cache 能提速

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 避免重复计算历史上下文，是 LLM 推理系统的核心状态。

## 本章要回答的问题

为什么 LLM 生成时几乎一定要使用 KV Cache？它到底缓存了什么？为什么它能显著降低 Decode 的重复计算？又为什么它会把推理系统从“计算问题”推向“显存管理问题”？

KV Cache 是理解现代 LLM inference runtime 的关键。没有它，Decode 会不断重复处理历史上下文；有了它，计算量下降，但 GPU memory、调度、分页、复用和 offload 都变成系统核心问题。

## 从重复计算开始

自回归模型每次只生成一个 token。假设 prompt 是：

```text
我 爱
```

模型先处理这两个 token，并预测下一个 token，例如：

```text
中
```

下一步模型要基于：

```text
我 爱 中
```

继续预测下一个 token。问题在于，“我”和“爱”的 Key / Value 表示在上一轮已经算过。如果每一步都把完整上下文重新跑一遍，就会产生大量重复计算。

KV Cache 的直觉很简单：历史 token 的 Key 和 Value 既然已经算过，就把它们保存下来。下一次 Decode 时，只为最新 token 计算新的 K/V，然后和缓存中的历史 K/V 一起做 attention。

## Attention 中到底缓存了什么

在 self-attention 中，每个 token 会产生 Query、Key、Value：

```text
Q = XWq
K = XWk
V = XWv
```

对于当前要生成的新 token，它需要用自己的 Query 去看历史 token 的 Key，并基于 attention 权重聚合历史 Value。历史 token 的 K/V 在生成过程中不会因为后续 token 改变，所以可以缓存。

可以把一次生成理解成：

```text
Prefill:
  计算 prompt 中所有 token 的 K/V
  写入 KV Cache

Decode step t:
  只计算新 token 的 K/V
  读取历史 KV Cache
  计算当前 token 对历史上下文的 attention
  生成下一个 token
  把新 token 的 K/V 追加进 KV Cache
```

这就是 KV Cache 的核心取舍：用空间换时间。

## 为什么它能提速

没有 KV Cache 时，生成第 `t` 个 token 需要重新处理长度为 `t` 的上下文。随着输出变长，每一步都重复扫描越来越长的历史。

有 KV Cache 后，历史 token 的 K/V 不再重复计算。每一步只需要处理新 token，并读取历史 cache 参与 attention。这样，Decode 阶段的瓶颈从“重复算历史”转向“读取和管理历史状态”。

这也是为什么 KV Cache 会改变推理系统设计。它不是一个普通 memoization 小技巧，而是把每个请求变成了一个持续增长的 runtime state。

## KV Cache 的代价

KV Cache 的代价是显存。

对 batch size 为 `B` 的近似估算是：

```text
KV bytes ≈ 2 x B x T x L x H_kv x D_head x b
```

其中 `2` 表示 Key 和 Value，`T` 是已缓存 token 数，`L` 是 layer 数，`H_kv` 是 KV head 数，`D_head` 是 head dimension，`b` 是每个元素的 bytes。实现中的 block padding、metadata、alignment 和并行分片还会增加或重新分布实际占用。

这个公式也解释了 MHA、GQA 与 MQA 的系统差异。GQA/MQA 让多个 Query heads 共享更少的 KV heads，从而降低 `H_kv`；它们减少 cache 容量与带宽，但属于模型架构选择，不是 runtime 可以对任意 checkpoint 无损打开的开关。

这会带来三个系统后果。

第一，batch size 受 KV Cache 限制。GPU 里除了权重，还要放 KV Cache、activation、temporary buffers。长上下文请求会迅速吃掉显存，导致可并发请求数下降。

第二，KV Cache 是动态增长的。不同请求的 prompt 长度、输出长度不同，cache 生命周期也不同。它不像模型权重那样加载后固定不变，而是在请求执行期间持续增长和释放。

第三，KV Cache 需要调度器理解。一个请求能否进入 batch，不只取决于 compute slot，还取决于是否有足够 KV memory。调度器要同时管理 token 生成进度、显存预算、请求优先级和公平性。

## 从缓存到内存管理

KV Cache 出现后，推理系统的核心矛盾发生了变化。

没有 cache，系统浪费在重复计算历史 token 上。有 cache，系统开始受限于 cache 的显存占用和访问效率。

这正是后续技术出现的原因：

- Continuous Batching 要在请求随时完成、随时加入的情况下管理动态 cache。
- PagedAttention 要解决 KV Cache 分配中的碎片化和浪费。
- RadixAttention 要在多个请求共享 prefix 时复用已有 KV。
- Long Context 技术要处理超长上下文下 KV Cache 爆炸。
- PD 分离要面对 Prefill 写入大量 cache、Decode 高频读取 cache 的不同资源画像。

KV Cache 因此成为从模型机制通向 AI Infra 的桥。它一头连着 Transformer attention，一头连着 GPU memory manager 和 serving scheduler。

## 常见误区

第一个误区是认为 KV Cache 只是在“存历史文本”。它存的不是文本，也不是 token id，而是每一层 attention 所需的 Key / Value 张量。

第二个误区是认为 KV Cache 只会带来收益。它减少计算，但增加显存占用。对于短输出、低并发场景，收益很直接；对于长上下文、高并发场景，KV memory 可能成为主要瓶颈。

第三个误区是认为 cache 管理只是底层实现细节。事实上，现代推理引擎的核心竞争力很大程度上来自 KV Cache 管理：什么时候分配、怎么分页、能否共享、如何回收、如何避免碎片、如何与调度器协同。

第四个误区是把 KV Cache 说成“把 Attention 从平方复杂度变成常数复杂度”。Cache 避免了历史 token 的 K/V projection 与前层计算被反复执行，但当前 Query 仍要读取并关注越来越长的历史 K/V。每个 Decode step 的 attention work 仍随已缓存长度增长。

## 本章在知识树中的位置

KV Cache 是 Part IV 的基础节点：

```text
Decode
→ KV Cache
→ Continuous Batching
→ PagedAttention
→ vLLM / SGLang
→ GPU Memory
→ PD 分离
→ 推理调度
```

理解 KV Cache 后，后面的 PagedAttention、RadixAttention、Long Context、PD 分离才不再是孤立技术，而是围绕同一个运行时状态展开的系统设计。

## 自检问题

1. KV Cache 缓存的是 token 文本、hidden states，还是 Key / Value 张量？
2. 为什么没有 KV Cache 时 Decode 会重复计算历史上下文？
3. KV Cache 为什么会随 batch size 和 sequence length 增长？
4. 为什么 KV Cache 会让推理调度从 compute scheduling 变成 compute + memory scheduling？
5. PagedAttention、RadixAttention、ShadowKV 分别在解决 KV Cache 的哪类问题？

## Review notes

本轮 Review 补齐了 KV Cache 的容量公式、MHA/GQA/MQA 差异，并纠正“使用 cache 后 Decode 成为常数复杂度”的误读。本章承担 runtime state 与显存/调度后果；第19章应承担模型侧 K/V 可复用性的推导，避免两章重复。

Primary-source 校验入口：

- PagedAttention / vLLM 对 KV Cache 动态增长、碎片和重复复制问题的描述： https://arxiv.org/abs/2309.06180
