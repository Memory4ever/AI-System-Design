# 第44章 Speculative Decoding

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 用小模型猜测，大模型验证，缓解自回归串行瓶颈。

## 本章要回答的问题

自回归 Decode 每次只能生成一个 token，这是 LLM 推理延迟的根本瓶颈之一。Speculative Decoding 为什么能让大模型“看起来一次生成多个 token”？它为什么不是简单地用小模型替代大模型？它在什么条件下才真正有效？

Speculative Decoding 的直觉可以概括为一句话：**小模型先写草稿，大模型批量审稿。**

本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**

## 从 Decode 串行瓶颈开始

普通 Decode 的流程是：

```text
大模型生成 token 1
→ 把 token 1 接回上下文
→ 大模型生成 token 2
→ 把 token 2 接回上下文
→ 大模型生成 token 3
...
```

生成 `K` 个 token，就要运行 `K` 次大模型 forward。这个串行依赖无法简单通过扩大 batch 消除，因为同一个请求内部下一个 token 依赖上一个 token。

这就是 speculative decoding 试图突破的地方：既然大模型一步一步生成很慢，能不能先让一个便宜的 draft model 猜出多个未来 token，再让大模型一次性验证这些猜测？

## 草稿模型和目标模型

Speculative Decoding 通常有两个模型角色：

- `Draft model`：较小、较快，负责快速生成候选 token。
- `Target model`：原本要服务的较大模型，负责验证候选 token，并保证最终输出仍然符合目标模型的分布。

可以把流程拆成五步：

```text
1. 传统 baseline:
   target model 生成 4 个 token，需要 4 次计算。

2. 投机:
   draft model 快速生成 5 个候选 token。

3. 验证:
   target model 通过一次 forward 并行验证这些候选 token。

4. 接受 / 拒绝:
   连续通过的前缀 token 被接受。
   第一个不通过的位置之后全部丢弃。

5. 回退:
   target model 生成正确 token，进入下一轮。
```

如果 draft model 猜得足够准，那么大模型一次验证就能接受多个 token。这样，单位大模型 forward 产出的有效 token 数增加，Decode 吞吐和 latency 都可能改善。

## 为什么验证可以并行

自回归生成慢，是因为“生成下一个 token”依赖前一个 token 的结果。但如果 draft model 已经给出一串候选 token，大模型就可以把这串候选当作已知序列，计算每个位置上目标模型会给出的分布。

也就是说，大模型不需要一步一步“发现”这些 token，而是在一次前向中检查：

```text
如果上下文是 prefix，
draft token 1 是否可接受？
如果上下文是 prefix + draft token 1，
draft token 2 是否可接受？
...
```

这利用了 Transformer 在一个序列内部并行计算多个位置表示的能力。生成是串行的，但验证一段给定序列可以并行。

## 它不是近似替代

一个常见误解是：Speculative Decoding 就是用小模型替代大模型生成。

不是。小模型只负责提出候选，大模型仍然决定哪些 token 被接受。经典 speculative decoding / speculative sampling 的目标是在加速的同时保持目标模型原有输出分布。也就是说，系统希望加速的是采样过程，而不是换成另一个模型的行为。

这点很重要。否则它就只是模型压缩或蒸馏，而不是 speculative decoding。

## 接受规则为什么不能只是“两个模型输出相同”

在 greedy decoding 中，可以直观地比较 draft token 是否与 target 的选择一致。但在 sampling 中，如果只接受两个模型恰好采到相同 token，会改变目标分布或浪费大量候选。

经典 speculative sampling 根据 draft distribution `q` 与 target distribution `p` 计算接受概率；拒绝时再从经过校正的 residual distribution 采样。它的关键性质是：最终样本仍服从 target model 的分布，而不是仅仅“多数时候看起来一样”。

因此“target model 生成正确 token”只是一种直觉说法。严格系统实现必须区分 greedy verification 与 distribution-preserving sampling。

## Exact Acceptance 机制

设 draft distribution 为 `q(x)`，target distribution 为 `p(x)`。对 draft 采样出的 token `x`，经典 acceptance probability 是：

```text
a(x) = min(1, p(x) / q(x))
```

若接受，则继续验证下一 draft token；若拒绝，则从校正后的 residual distribution 采样：

```text
p_residual(x)
= normalize(max(0, p(x) - q(x)))
```

这组规则保证每个最终 token 的边缘分布仍来自 target model。工程实现还需处理 floating-point、zero probability、batch mask 和第一个 rejection 后的 KV rollback，但不能把规则简化成“概率更大就接受”。

## 接受长度小例子

Draft 一次提出 4 个 tokens。若前 3 个依次通过，第 4 个拒绝，则本轮 target verification 至少推进 3 个 accepted positions，并在拒绝位置按 target-corrected distribution 产生 replacement token；第 4 个以后依赖错误 prefix 的候选全部作废。

衡量收益时应记录：

```text
accepted_tokens_per_target_step
draft_cost
verification_cost
rollback / scheduling overhead
```

Acceptance rate 高不等于端到端加速一定高。若 draft 自身昂贵、verification shape 低效或 target batch 被打散，节省的 serial steps 可能被额外 work 抵消。

一个粗略的判断框架是：

```text
benefit exists when
cost(draft + one verification)
< cost(replaced target serial steps)
```

它是测量框架而非通用 speedup 公式；真实结果必须绑定模型、draft length、batch、hardware 和 workload。

## 什么时候有效

Speculative Decoding 的收益取决于几个条件。

第一，draft model 必须足够便宜。如果小模型生成候选的成本太高，就抵消了大模型少跑几次的收益。

第二，draft model 必须足够准。如果候选 token 很快被拒绝，大模型每次只接受一两个 token，收益有限。

第三，target model 的验证必须能高效并行。如果验证阶段本身开销很大，或者 batch / kernel / memory 状态让验证效率下降，收益也会变小。

第四，系统调度必须支持它。Speculative Decoding 改变了 Decode 的 token 产出形态：一个请求一次可能接受多个 token，也可能回退。这会影响 KV Cache 追加、batch scheduling、streaming 输出和 latency 统计。

## Trade-off

Speculative Decoding 的核心 trade-off 是：用额外的 draft computation 换取更少的 target model serial steps。

它适合 target model 很贵、draft model 很便宜、候选命中率高的场景。它不适合所有 workload。如果 prompt 分布复杂、draft model 和 target model 行为差异大，拒绝率高，收益会下降。

它也可能增加系统复杂度。服务端需要管理两个模型或一个带多 token prediction 能力的模型，需要处理候选 token 的 KV 状态，需要在验证后决定哪些 cache 可以保留、哪些需要回退。

此外，它和 batching 并不是天然独立的优化。一次请求接受多个 token，另一次请求只接受一个 token，会进一步增加 batch 内 token 进度差异。调度器需要能处理这种不均匀推进。

KV state 也必须事务化处理。Runtime 可以先把候选 K/V 写入临时 slots，验证后只提交 accepted prefix；也可以写入预留 blocks，再回滚被拒绝的 suffix。无论实现如何，block table、cached length 和 streamed tokens 必须在同一 accepted boundary 上一致。

## 和其他加速方法的关系

Speculative Decoding 解决的是 Decode 串行性问题。

它和 KV Cache 不冲突。KV Cache 仍然用于保存历史 K/V，只是 speculative verification 会让 cache 的追加和回退更复杂。

它和 Continuous Batching 也不冲突，但会让调度更复杂。不同请求在一次 iteration 中可能产出不同数量的 token。

它和量化、图优化、FlashAttention 属于不同层次。量化降低单次计算和带宽成本，图优化降低 kernel / memory overhead，Speculative Decoding 试图减少昂贵 target model serial step 的数量。

## 本章在知识树中的位置

```text
Decode
→ 自回归串行瓶颈
→ Speculative Decoding
→ KV Cache 状态管理
→ 推理调度
```

它是 Part IV 中少数直接挑战 Decode 串行性的技术之一。

## 自检问题

1. Speculative Decoding 为什么需要 draft model 和 target model？
2. 为什么生成是串行的，但验证候选 token 可以并行？
3. 为什么它不是简单的小模型替代？
4. acceptance rate 对加速效果有什么影响？
5. `min(1,p/q)` 与 residual sampling 怎样保持 target distribution？
6. 为什么 acceptance rate 高仍不保证端到端加速？
7. Speculative Decoding 会给 KV Cache 和 batching 带来哪些额外复杂度？

## 小结

Speculative Decoding 没有取消 autoregressive semantics，而是让便宜的 drafter 先提供已知候选，使 target model 能并行验证多个 positions。Exact acceptance 保护输出分布，系统收益则取决于 accepted progress 是否覆盖额外 draft、verification 和状态管理成本。

至此第42～44章分别从 batch membership、KV placement 和 serial target steps 三个正交方向优化 runtime。下一章开始把这些机制映射到实际 Serving stacks。

## Review notes

Primary-source 校验入口：

- Fast Inference from Transformers via Speculative Decoding: https://arxiv.org/abs/2211.17192
- Accelerating Large Language Model Decoding with Speculative Sampling: https://arxiv.org/abs/2302.01318

本轮 Review 补充了 greedy verification 与 distribution-preserving speculative sampling 的边界。当前章节只解释 classical speculative decoding；EAGLE、MTP、n-gram 等 drafter 路径不在本章展开，避免把不同候选生成机制混成一个算法。
