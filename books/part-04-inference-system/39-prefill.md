# 第39章 Prefill

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** Prompt 阶段一次性处理上下文，计算密集、可并行度高。

## 本章要回答的问题

请求变成 token ids 后，为什么不能直接进入逐 token 输出？Prefill 究竟计算了什么、写入了什么状态？为什么它常被概括为 compute-intensive，却不能在所有模型、长度和硬件上机械地称为 compute-bound？长 prompt 又为什么会伤害正在 Decode 的请求？

本章的核心判断是：**Prefill 将整段 prompt 映射为第一个 next-token distribution 和逐层 KV state；它利用 token 维度并行换取高 GPU efficiency，但工作量、显存峰值和调度占用会随 prompt 长度快速增长。**

本章使用 `B` 表示 sequence batch size，`T_p` 表示 prompt length，`d_model` 表示 hidden dimension，`L` 表示层数，`H_kv` 与 `d_h` 表示 KV heads 和 head dimension。

## 如果逐个 Token 读 Prompt

最直接的办法是像 Decode 一样，从 prompt 第一个 token 开始逐个运行模型。它在语义上可行，却浪费 causal attention 已知的并行性。

训练阶段已经能在 causal mask 下同时计算所有位置：位置 `t` 不读取未来 token，但不同位置的矩阵运算仍可一起执行。Prefill 复用了这条结构，把 `T_p` 个已知 tokens 一次送入模型。

```text
input ids        [B, T_p]
-> embedding     [B, T_p, d_model]
-> L layers      [B, T_p, d_model]
-> final logits  [B, T_p, V]
```

Serving 通常只需要最后一个 prompt position 的 next-token logits，但每一层、每个 prompt position 的 K/V 都要为后续 Decode 保留。

## Prefill 的两个输出

最后一个位置的 logits `[B,V]` 经过第20章的 sampling policy 得到第一个 output token。第一个 token 可见前经历的主要模型计算正是 Prefill。

每层还要写入：

```text
K_l, V_l: [B, H_kv, T_p, d_h]
```

物理 layout 可能因 kernel 和 runtime 不同而变化，但逻辑维度必须一致。Prefill 结束后，request 从“拥有 prompt ids”升级为“拥有可继续 Decode 的 position 与 KV history”。

## 计算量从哪里来

忽略常数和不同 Attention 变体，一层 dense Transformer 的主要工作可粗略拆为：

```text
linear / MLP projections: O(B * T_p * d_model^2)
prompt self-attention:    O(B * T_p^2 * d_model)
```

短到中等 context 下，大模型的 projection 与 MLP 可能占主要 FLOPs；`T_p` 很长时，Attention 的二次项变得重要。FlashAttention 降低中间矩阵对 HBM 的 IO，并不把 exact full Attention 的数学计算改成线性。

因此“Prefill 是 compute-bound”是一条 workload-dependent heuristic。它通常比单-token Decode 拥有更大的矩阵维度和更高 data reuse，更容易利用 GPU compute；是否真正达到 compute roofline，还取决于模型、kernel、precision、`T_p`、batch、通信和硬件。

## 一个 Shape 小例子

设：

```text
B       = 2
T_p     = 4
d_model = 8
H_kv    = 2
d_h     = 4
```

输入 hidden states 是 `[2,4,8]`。某一层产生的 K 和 V 各为 `[2,2,4,4]`。Prefill 完成后，每个请求拥有 4 个历史 positions 的 K/V；Decode 第一轮只需为新 token 计算一个 position，并读取这 4 个 positions。

Batch 中 prompt 长度不同时，padding 会做无效工作；packing 或 ragged/paged representation 能减少浪费，却提高 kernel 与 metadata 复杂度。

## TTFT 不等于 Prefill Kernel Time

```text
TTFT
= frontend + queueing + tokenization + admission
 + Prefill execution
 + first-token sampling + first stream delivery
```

优化 Prefill kernel 只减少其中一项。若请求仍在 queue 中等待 KV blocks，用户 TTFT 不会按 kernel 加速比例下降。反过来，prefix cache hit 可能跳过部分 Prefill work，即使模型 kernel 没有变化。

## 长 Prompt 为什么会干扰 Decode

Prefill 往往以较大 token block 占用 GPU。若同一 worker 同时承载延迟敏感的 Decode iterations，一个超长 prompt 可能延后后续 Decode step，造成 TPOT 抖动。

朴素方案是让 Prefill 一次跑完整 prompt，优点是大矩阵效率高，缺点是 scheduler 无法在中间插入 urgent Decode work。

### Chunked Prefill

Chunked Prefill 把 prompt 分成多个 token chunks：

```text
T_p = c_1 + c_2 + ... + c_n
```

每个 iteration 只调度部分 prompt tokens，使 scheduler 可以在 chunks 之间安排 Decode。它减少 head-of-line blocking，却带来更多调度边界、较小矩阵、复杂的 KV reservation，并可能增加单请求 TTFT。

所以 chunk size 是 throughput、TTFT 和 TPOT interference 之间的 policy，不是越小越公平。

## Batch Prefill 的权衡

将多个 prompts 合并能提高 GPU utilization，但等待凑 batch 会增加 queueing。长度差异还会造成 padding 或不规则 shape。

Runtime 可以按长度分桶、使用 token budget、chunk prompts 或将 Prefill 与 Decode 混合调度。它们都在回答同一问题：本轮处理多少新 prompt tokens，才能不牺牲过多 Decode cadence？

## 跨 Runtime 必须保留的身份

Prefill 产生的 KV state 只能由兼容的 Decode 继续使用。至少需要一致：

- Model weights、revision 与 adapter。
- Tokenizer、chat template 和 token ids。
- Position ids 与 RoPE configuration。
- KV dtype、layout、block size。
- TP/PP 等 parallel layout。

在单 worker 内，这些通常被 runtime 隐含保证；进入 PD 分离后，它们成为跨进程、跨节点的显式 transfer contract。

## 工程验证

Prefill benchmark 应同时记录 `T_p` 分布、batch tokens、queueing、kernel time、first-token sampling 与 TTFT 分位数。正确性验证则应比较 chunked/non-chunked、cached/non-cached 路径在相同 sampling 条件下的 logits 或 token sequence。

不能仅凭 GPU utilization 判断配置。一个长 Prefill 把 GPU 跑满，同时让所有 Decode 请求错过 TPOT SLO，仍是系统层失败。

## 本章在知识树中的位置

```text
request admitted
-> prompt tokens [B,T_p]
-> Prefill parallel compute
-> first-token logits
 + initial per-layer KV state
-> Decode loop
```

第38章定义完整请求状态机，本章负责从 tokenized request 到可 Decode state。第40章将解释为什么后续输出不能继续沿用同样的大块并行方式。

## 自检问题

1. Prefill 为什么能并行计算所有 prompt positions 而不违反 causal mask？
2. Prefill 的两个核心输出是什么？
3. 为什么只使用最后位置 logits，却必须保存所有位置 K/V？
4. 主要计算项如何随 `T_p` 增长？
5. 为什么“compute-bound”必须注明 workload 条件？
6. Chunked Prefill 在 TTFT、TPOT 和 throughput 之间怎样取舍？
7. PD handoff 前为什么要验证 model 与 KV layout identity？

## 小结

Prefill 利用已知 prompt 的 token-parallelism，高效形成第一个生成分布和初始 KV state。它比 Decode 更容易形成大矩阵计算，但长 prompt 会增加 work、显存和 scheduler occupancy。

Chunked Prefill 不改变模型语义，而是重新安排 work 的时间粒度。下一章进入 Decode，观察瓶颈怎样转向逐 token 访存与调度。

## Review notes

本轮补齐 Prefill 的 tensor contract、FLOPs 边界、TTFT 分解、chunked prefill 与长 prompt interference。章节不再无条件称其 compute-bound，也不提前展开 KV 容量和 PD deployment。

Primary-source entry points：

- DistServe: https://arxiv.org/abs/2401.09670
- Sarathi-Serve, chunked-prefills: https://arxiv.org/abs/2403.02310
- FlashAttention: https://arxiv.org/abs/2205.14135
