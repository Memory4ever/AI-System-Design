# 第22章 Long Context

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Status:** Draft

**Roadmap Intent:** 长上下文为什么困难，位置编码、显存、注意力复杂度和检索增强如何互相影响。

## 本章要回答的问题

为什么把 context window 从 8K 扩到 128K、1M token，不只是修改一个长度参数？一个模型“允许输入很长”，是否就等于它能有效利用远处信息？Long Context 为什么会同时挑战位置表示、Attention、KV Cache、分布式执行和服务成本？

本章的核心判断是：**Long Context 不是一个单点能力，而是模型有效性与系统可承载性共同决定的结果。**任何只解决其中一层的方案，都不能自动得到可用的长上下文系统。

## 先拆开四种容易混淆的能力

讨论长上下文时，至少要区分四件事：

1. **Accepted length**：接口和模型能否接收这么多 token。
2. **Positional generalization**：模型是否能在更远位置保持稳定的位置关系。
3. **Effective utilization**：信息真的放进窗口后，模型是否能检索、组合并正确使用。
4. **System capacity**：训练和推理是否能在可接受的延迟、吞吐与成本下承载。

一个系统可以通过修改配置接受 128K token，却在远距离依赖上明显退化；也可以在离线 benchmark 上利用长上下文，却因单请求 KV Cache 太大而无法在线并发。把这四层合并成“支持 128K”，会掩盖真正的瓶颈。

## Prefill：平方增长首先出现在哪里

长度为 `T` 的 dense Self Attention 需要处理 `T x T` 的 token 关系。忽略投影等其他计算后，attention score 相关计算量通常随 `T^2` 增长。

FlashAttention 可以通过 IO-aware tiling 避免在 HBM 中完整物化大规模中间矩阵，并显著降低额外存储和数据搬运，但 exact dense attention 的二次计算关系并未因此消失。

所以长 prompt 会同时放大：

- Prefill compute。
- Attention 中间状态和 workspace。
- Prefill 排队时间与 `TTFT`。
- 单次请求对 batch 中其他请求的干扰。

## Decode：KV Cache 为什么线性增长也足够致命

使用 KV Cache 后，Decode 不再重复计算历史 token 的 K/V，但必须保存每一层的历史状态。对 batch size 为 1 的近似估算是：

```text
KV bytes ≈ 2 x L x T x H_kv x D_head x b
```

其中：

- `2` 表示 Key 和 Value。
- `L` 是 layer 数。
- `T` 是已缓存 token 数。
- `H_kv` 是 KV head 数。
- `D_head` 是每个 head 的维度。
- `b` 是每个元素的 bytes。

Multi-Query Attention 或 Grouped-Query Attention 可以减少 `H_kv`，量化可以减少 `b`，但 KV Cache 仍会随 token 数和并发请求数增长。上下文窗口扩大后，服务容量往往先受显存限制，而不是模型权重能否加载。

## 不同方案到底在移动哪个瓶颈

长上下文方案可以按它们改变的约束分类。

### 位置与训练分布

位置编码扩展、RoPE scaling、长序列继续训练等方法，主要解决模型是否能在更远位置保持有效表示。它们不能自动降低 Attention 或 KV Cache 成本。

### Attention 执行与分布

FlashAttention 优化单设备上的 IO。Ring Attention 把序列块分布到多个设备，在 blockwise attention 计算期间环形传递 K/V blocks，并尝试让通信与计算重叠。

它扩展了单设备可承载长度，但把容量问题转化为设备数量、互联带宽、负载均衡和分布式调度问题。它不是把 Attention 变成免费计算。

### KV Cache 分层与稀疏访问

Offload 把部分状态移到 CPU memory 或其他存储层级，用容量换取传输延迟。ShadowKV 是更具体的研究方案：它保存低秩 key cache、offload value cache，并按需重建被选择的稀疏 KV pairs。

因此不能把 ShadowKV 泛化成所有“KV 分层”的同义词。它依赖低秩结构、选择策略、workload 和硬件数据通路，收益必须在目标模型与请求分布上验证。

### Retrieval 与压缩

RAG、摘要、memory compression 等方法不扩大模型内部的 dense context window，而是选择哪些信息值得进入窗口。它们可能显著降低计算成本，但会引入 retrieval recall、切分、排序、信息丢失和新鲜度问题。

所以 RAG 不是 Long Context 的低配版本，也不是简单替代品。一个解决“窗口里能放多少”，另一个解决“有限窗口里应该放什么”。

## 工程决策不能只看最大长度

评估长上下文系统时，至少要观察：

- Prompt length 的真实分布，而不是只看最大值。
- `TTFT`、`TPOT` 和 tail latency 如何随长度变化。
- 单请求 KV Cache 与可承载并发。
- 模型在远距离检索、组合和干扰场景中的有效性。
- 是否需要跨 GPU sequence/context parallelism。
- Offload、prefix reuse、RAG 或压缩能否降低实际工作集。

“最大 context window”只是能力上限，不是生产系统的容量规划指标。

## 本章在知识树中的位置

```text
Position Encoding + Self Attention
→ Long Context
→ Prefill compute / KV Cache capacity
→ Ring Attention / offload / sparse access / retrieval
→ GPU Memory / PD disaggregation / inference scheduling
```

本章是 Part II 的收束节点之一：模型想看到更长序列，系统就必须为更多计算、状态和数据移动付费。

## 自检问题

1. accepted length、positional generalization 和 effective utilization 有什么区别？
2. FlashAttention 为什么没有消除 exact dense attention 的二次计算？
3. KV Cache 容量由哪些主要变量决定？
4. GQA/MQA 为什么能降低长上下文推理的 KV 成本？
5. Ring Attention 把单卡容量问题转化成了什么问题？
6. ShadowKV 为什么不能被泛化成所有 KV offload 方法？
7. RAG 与 Long Context 是替代关系还是互补关系？

## Review notes

本轮 Review 将 Long Context 拆成可接收长度、位置泛化、有效利用和系统容量四个层次；补充了 Prefill 与 KV Cache 的复杂度模型；并明确 Ring Attention、ShadowKV、offload 与 RAG 分别移动哪一类瓶颈。任何具体最大长度和性能收益仍需针对模型、硬件与 workload 重新验证。

Primary-source 校验入口：

- FlashAttention: https://arxiv.org/abs/2205.14135
- Ring Attention with Blockwise Transformers for Near-Infinite Context: https://arxiv.org/abs/2310.01889
- ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference: https://arxiv.org/abs/2410.21465
