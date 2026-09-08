# 第46章 Continuous Batching

**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场
**Stable Knowledge Node ID:** `INFER-CONTINUOUS-BATCHING`
**Legacy Chapter:** Ch42
**Status:** Draft

**Roadmap Intent:** 动态合并请求，提高 GPU 利用率。

## 本章要回答的问题

为什么传统 batching 在 LLM Serving 中不够用？为什么请求已经进入同一个 batch 后，还不能像普通深度学习 inference 那样“一起开始、一起结束”？Continuous Batching 到底连续在哪里？

本章的核心判断是：**LLM Serving 的 batch 不是一个静态数组，而是一个会在每个 iteration 重新构造的 token-work 集合。**Continuous Batching 不只填补空 slot，还要在有限 token budget 与 KV capacity 下共同决定 admission、Prefill、Decode、preemption 和 completion。

## 从 Static Batching 的问题开始

在普通模型推理中，batching 很自然：收集一批请求，拼成一个 batch，跑一次 forward，返回结果。

对于 LLM，这个思路在 Prefill 阶段仍然有用，但在 Decode 阶段会遇到问题。因为不同请求的输出长度不同，有的请求很快结束，有的请求要生成很久。

如果采用 static batching，系统会把一批请求放在一起执行，并等待整个 batch 都完成后，再开始下一批。这样会出现一个明显浪费：短请求已经结束，但它占用的 batch slot 不能立即被新请求使用，只能等最长请求完成。

一个直观类比是：static batching 像一辆公交车，必须等一批乘客一起上车、一起到站，下一批才能开始。对于生成长度差异很大的请求，这会让 GPU 出现空洞。

## Continuous Batching 的直觉

Continuous Batching 更像旋转门：有人完成就出去，有新请求就补进来。

在 Decode 的每一个 iteration，调度器都会重新决定当前 batch 里有哪些请求：

```text
iteration 1: A B C D
iteration 2: A B C D
iteration 3: A B   D   # C 完成
iteration 4: A B E D   # E 补位
iteration 5:   B E D   # A 完成
iteration 6: F B E D   # F 补位
```

这样，GPU 不必因为某些请求提前完成而等待整个 batch 清空。每个 Decode step 都可以尽量保持 batch 饱满，提高吞吐。

Continuous Batching 的关键不是“更大的 batch”，而是 **iteration-level scheduling**：调度决策发生在生成循环内部，而不是只发生在请求进入系统时。

这里的 iteration 不必永远等于“每个请求恰好生成一个 token”。Chunked prefill、speculative verification 和不同模型执行路径都可能让一次调度迭代推进不同数量的 token。稳定定义是：执行引擎只运行一个可重新调度的工作单元，下一轮前允许 batch membership 变化。

## 为什么 LLM 特别需要它

LLM 请求有几个特征，使 continuous batching 特别重要。

第一，生成长度不可预测。用户问一个简单问题可能只生成几十个 token，让模型写报告可能生成上千个 token。即使 prompt 长度相似，output length 也可能差异很大。

第二，Decode 阶段单步计算小但循环多。每一步只生成一个 token，但一个请求可能需要很多步。如果 batch 中有 slot 空着，浪费会被循环放大。

第三，GPU 昂贵。推理服务的成本很大程度上取决于 GPU 利用率。让 GPU 在 Decode 阶段持续有足够 work，是 serving engine 的核心目标之一。

第四，用户体验要求低延迟。系统不能为了攒大 batch 无限等待。Continuous Batching 让系统可以在不完全牺牲 latency 的情况下提高 throughput。

## 它和 KV Cache 的关系

Continuous Batching 不是单独存在的，它必须和 KV Cache 管理配合。

每个请求都有自己的 KV Cache，而且 cache 长度不同。当请求在 batch 中进出时，调度器必须知道：

- 请求当前生成到第几个 token。
- 它的 KV Cache 占用了多少显存。
- 它还能否继续生成。
- 新请求加入时是否有足够 KV memory。
- batch 中不同请求的 cache 如何被 kernel 访问。

所以 continuous batching 看起来是在“调请求”，实际上是在同时调计算和显存状态。

这也是为什么 PagedAttention、vLLM 这类系统会把 batching 和 KV Cache memory management 放在同一个设计框架中。没有高效的 cache 管理，动态 batch 会很快被显存碎片和生命周期复杂度拖垮。

## 从 Batch Size 到 Token Budget

固定 `batch_size=32` 不能完整描述一次 iteration。一个 Decode request 通常只推进一个 token，而一个 chunked Prefill request 可能推进数百个 tokens；两者的计算量、workspace 和 KV 增量不同。

更稳定的调度约束是：

```text
sum_r scheduled_tokens_r <= token_budget
new_KV_blocks <= free_or_reclaimable_blocks
```

Scheduler 先从 running/waiting requests 中选择本轮 work，再由 model runner 将这些 tokens 打包执行。Token budget 太小，GPU 可能吃不饱；太大，单轮时间和 TPOT 抖动会增加。

## 生成语义决定调度粒度：从 Token Iteration 到 Block Denoising

Autoregressive Decode 的已提交状态每步只追加一个 token，因此 token iteration 是自然的 scheduling quantum。Diffusion LM 的状态不同：一个 block 会经历多轮 denoising，同一轮中的请求可能处于不同 refinement step，也可能在不同时间完成当前 block。若仍把整个 batch 当成同步 token step，较早收敛的 block 会等待 straggler，已完成的 capacity 也不能及时回收。

对应的 Alternative Branch 是把一次可重调度 work unit 改成 block-denoise cycle：

```text
mutable blocks at heterogeneous denoising states
→ pack one denoise cycle under token / memory bounds
→ execute dense mixed-state layout
→ commit completed blocks and reclaim their slots
→ admit or advance the next blocks
```

这里 scheduler 拥有 block lifecycle 与 packing，generation algorithm 仍拥有 denoising semantics 和 completion rule。Block identity 至少要绑定 request、block position、denoise step、model revision 与 committed/mutable generation；只有完成规则成立后才能把 block 从 mutable state 变成输出，并释放对应 slot。

更小的 block 提高回收粒度，却增加 scheduling、metadata 和 denoising overhead；更大的 block 更容易形成高效 kernel，却会放大 straggler 和并行近似的质量风险。Mixed-state layout 还要求 kernel 能解释每个 block 的 step state。现有受限案例只覆盖单张 H200、BF16、离线 batch 和给定 diffusion models，没有证明 online arrival、fairness、tail SLO 或 multi-GPU。因而 AR 模型继续使用 token iteration；diffusion 分支只有在 block completion 和 mutable-state packing 的收益超过复杂度时成立。生成范式归第 24 章，本章只拥有 serving scheduling quantum。

## 一个 Iteration 小例子

假设本轮 token budget 为 8：

| Request | Phase | 可调度 tokens |
| --- | --- | ---: |
| A | Decode | 1 |
| B | Decode | 1 |
| C | Prefill | 12 |

若让 C 一次占满剩余 6 个 tokens，本轮计划是 `1+1+6=8`，C 还剩 6 个 prompt tokens。下一轮 A、B 仍可先各推进一个 token，再继续 C。若 C 独占完整 Prefill，A、B 的下一 token 必须等待更久。

这个例子说明 Continuous Batching 与 Chunked Prefill 的共同边界：batch membership 在变，单个 request 每轮推进量也可能不同。

## nano-vLLM：机制与具体 Policy 的分界

nano-vLLM 当前 scheduler 提供了一个简化对照：

```text
waiting queue --Prefill / recompute--> running queue
running queue --one-token Decode-----> running queue
running queue --finish---------------> release
running queue --preempt--------------> waiting queue
```

每次 `schedule()` 先扫描 `waiting`。只要选到至少一个 Prefill sequence，就返回
Prefill batch；只有没有 Prefill work 被选中时才构造 Decode batch。因此它实现了
iteration 边界上的动态 membership，却没有实现本章前述 `Decode + chunked Prefill`
同轮混合示例。两者不冲突：前者说明 Continuous Batching 的最小机制，后者说明
token-budget scheduler 可以采用的一种更一般 policy。

当 Decode 需要追加 block 而 free blocks 不足时，当前实现会 preempt sequence：
清空其 block table、把 `num_cached_tokens` 归零并放回 `waiting` 队首。恢复时要重新
走 Prefill，属于 **release-and-recompute**，不是 swap 或保留 KV。这个选择代码短、
ownership 清楚，却会把 memory pressure 转化为额外计算与 TTFT/TPOT 抖动。

这个案例提醒我们评估 scheduler 时必须分三层：

| 层次 | 问题 | nano-vLLM 当前选择 |
| --- | --- | --- |
| Mechanism | 是否在生成循环内部重新选择 work | 是 |
| Policy | Prefill/Decode 谁优先、能否同轮混合 | Prefill-first，同轮 phase-exclusive |
| State disposition | 抢占后 KV 怎么办 | 释放并 recompute |

所以不能只凭“支持 continuous batching”推断公平性、混合策略或抢占成本。必须继续
读取目标版本的 scheduling 与 block-management policy。

## Selective Determinism：把 Verify 变成第三类 Iteration Work

禁止 dynamic batching 可以得到最清楚的数值重放，batch-invariant kernels 则让所有 shape 使用固定 reduction
路径；前者损失利用率，后者把 determinism 的 kernel 税施加给全部请求。若只有 evaluation、audit 或 CI
traffic 需要复现，可以把 determinism 从 batch-wide execution mode 改成 request policy：普通 Decode 先走
高吞吐 fast path，标记请求积累固定窗口后进入 fixed-shape verifier。

```text
committed deterministic prefix
→ ordinary dynamic-batch decode produces private candidates
→ fixed-shape replay verifies a window, padded when necessary
→ commit longest matching prefix plus verifier's next token
→ overwrite candidate KV with verifier KV at the same boundary
→ discard suffix and resume after mismatch
```

这里 candidate tokens 在 commit 前不能 stream 给用户；只比较 token 也不够，因为 fast-path KV 可能已含数值
漂移，token length、stream cursor、block table 和 verified KV prefix 必须作为同一事务前进。Verifier 因而是
与 Prefill、Decode 竞争 token budget 和 GPU time 的第三类 work，window/group size 在 verification
arithmetic intensity、rollback length 与普通请求 tail SLO 之间取舍。

这条机制复用了 speculative proposal/verify/rollback 的结构，但目标是 reproducibility，不是用小 draft
减少 target serial steps。它还要求 model/tokenizer、precision、kernel/runtime、attention/collective config、
parallel topology、sampling parameters 与 seed 共同进入 determinism identity。全量 deterministic traffic、
prefix sharing 必须保留、rollback 不可接受或 verifier 干扰严重时，batch-invariant stack 仍是合理分支；
固定 batch 仍适合小规模 debugging。单一 SGLang/H100 prototype 不能证明跨 GPU、跨版本或 quantized/MoE
runtime 的 bitwise equivalence。

<!-- source-family:SF-2026-ARXIV-2605-28053 -->

固定窗口 verifier 让复现边界最清楚，但仍会验证大量本来不会翻转的 token。若已在目标 runtime 上校准，调度器可用
top-1 与 top-2 logit margin 作为触发信号：fast path 先产生 request-private token 与对应 KV；只有低 margin token
进入 reference path，reference verifier 决定 commit；若二者不一致，必须同时修复该 token 与当前 KV column，不能
只改输出文本。Trigger 只拥有“是否送验”的 proposal，reference path 才拥有提交权，scheduler 还要把稀疏 verifier
形成的 tail work 计入队列与 SLO。

在 token flip 稀疏时，这能少付 verifier 税；代价是 margin calibration drift、near-tie 漏检、reference path 成本和
尾延迟，高 margin 也只表示局部排序稳定，不表示语义正确。Audit/CI、flip 密集、quantized/MoE 或校准 OOD workload
应回退 always-on verifier、batch-invariant kernel 或固定 batch。exact-v1 只覆盖论文披露的五个模型、数据、BF16 与
batching 设置，不证明跨 kernel、硬件或版本的 bitwise equivalence。

<!-- source-family:SF-2026-ARXIV-2605-30218 -->

Continuous batching 通常假设每步只读 model state、只写 request-owned KV/token cursor；只要 request state 不混淆，任意兼容请求都可拼入同一 iteration。Test-time training 一类生成路径会在请求过程中更新私有参数或适配状态，此时调度键还必须包含 state owner、version、phase 与本步 READ/WRITE effect。只有 effect 兼容的请求才能共批，每次更新也只能提交到对应 request 的状态对象，不能因共享 kernel 把一个请求的学习结果泄漏给另一个请求。

Typed effect batching 保留利用率，却增加 copy-on-write、状态存储、phase fragmentation 和 rollback；更新版本错配会产生比 KV 串扰更隐蔽的语义污染。普通 immutable-weight decode 仍使用现有 continuous batching；私有状态很小或并发低时，逐请求执行可能比维护复杂 effect scheduler 更可靠。exact-v1 只支持披露 TTT workload 的 batching 约束，不证明所有在线学习算法可安全合批。

## Preemption 不是删除队列元素

KV 不足时，把请求从 running 移回 waiting 需要选择 state policy：

- 保留 KV：占 memory，恢复便宜。
- 释放后 recompute：节省 memory，恢复需要额外 Prefill。
- Offload：消耗 transfer bandwidth 与远端容量。

因此 preemption policy 同时影响计算、memory 和 latency。反复抢占同一个长请求还可能形成 livelock-like thrashing；runtime 需要通过 reserve、watermark 或 admission 约束避免没有请求真正前进。

## Trade-off

Continuous Batching 提高 GPU 利用率，但代价是调度器更复杂。

它需要更细粒度的请求状态管理。每个请求不再只是 pending / running / finished，而是处在 Prefill、Decode、waiting、swapped、finished 等不同状态中。

当 KV memory 不足时，调度器还要决定 admission、preemption 与 recomputation/swap policy。把一个请求从 running 集合移出并不免费：它已经占用的 KV Cache 要么保留、迁移、释放后重算，都会消耗不同资源。

它也会带来公平性问题。如果调度器总是优先填充容易完成的短请求，长请求可能被拖慢；如果总是照顾长请求，短请求的 tail latency 可能变差。

此外，Continuous Batching 和 Prefill 的关系也要小心。Prefill 通常计算密集，Decode 通常访存敏感。如果把大量 Prefill 请求直接插入 Decode batch，可能打乱 Decode 的稳定 token 输出节奏。因此实际系统常常需要区分 Prefill scheduling 和 Decode scheduling，甚至进一步走向 PD 分离。

## 工程实践中的判断

当一个 LLM 服务吞吐不高时，不能只看模型大小。需要问：

- Decode batch 是否经常不满？
- 是否有很多请求提前完成后留下空 slot？
- 调度器是否能在 iteration 级别插入新请求？
- KV Cache 显存是否限制了可进入 batch 的请求数？
- Prefill 是否阻塞了 Decode？
- 用户侧关注的是 `TTFT`，还是 overall throughput？

这些问题决定了 batching 策略是否真正有效。

## Batch 饱和后，请求数不再是容量尺度

在 Decode 阶段，active KV length 会改变每步 DRAM traffic。随着 batch 增大，系统可能先获得更高并行度，随后进入 bandwidth plateau；继续增加 request count 只会扩大排队、HBM 占用与尾延迟。调度器因此应同时观察 active sequence、KV footprint 与 bandwidth headroom，而不是把“大 batch”视为单调更优。

旧的固定 batch 在短上下文、同质请求或尚未饱和时仍然简单有效。一旦边际 throughput 接近零，admission 应停止扩 batch，把新请求留在队列或路由到其他 replica。该规则依赖真实硬件 profiling，不能从某个模型的饱和点外推通用阈值。

## 本章在知识树中的位置

Continuous Batching 连接了 Decode、KV Cache 和推理调度：

```text
Decode
→ KV Cache
→ Continuous Batching
→ PagedAttention
→ vLLM / SGLang
→ 推理调度
```

它不是一个孤立优化，而是现代 LLM serving engine 的基本调度方式之一。

## 从机制演进到系统设计

Continuous Batching 的调度量子最初是 autoregressive token iteration；block diffusion 等生成范式把它改成 denoise cycle，完成 block 后可立即回收 slot，并在不同 denoising state 间重新 packing。scheduler 必须同时约束 token、memory 与 provisional-state budget，而不是只数 active requests。

更细的 slot reuse 提高 occupancy，却增加异质状态对齐、临时结果与 commit boundary。denoise state 不兼容、质量合同不清或 batch 重排成本过高时，应回到同阶段 batching 或普通 AR iteration；determinism 与 preemption 仍需独立验证。

## 自检问题

1. Static Batching 为什么会在 LLM Decode 阶段浪费 GPU？
2. Continuous Batching 的“continuous”具体指什么？
3. 为什么 output length variance 会影响 batch 效率？
4. Continuous Batching 为什么必须理解 KV Cache？
5. Token budget 为什么比固定 batch size 更适合混合 Prefill/Decode？
6. Preemption 后三种 KV state policy 分别付出什么代价？
7. Continuous Batching 会带来哪些公平性和延迟 trade-off？
8. nano-vLLM 为什么属于 iteration-level scheduling，却不等于 mixed-phase batching？
9. Release-and-recompute 抢占把 memory pressure 转化成了什么代价？

## 多组件生成把 Batch 变成 Pipeline Feedback Control

自回归 LLM 的 iteration 通常由同一 decoder 推进；图像 diffusion serving 还包含 denoiser 与 VAE 等性能形态不同的组件。若只让 denoiser 满载，VAE backlog 会把已完成 latent 堵在队列里；若为 VAE 预留过多资源，又会降低 denoising throughput。Continuous Batching 因而从单队列 token admission 演进为 component-aware control：同时观察 denoising step、UNet/DiT work、VAE latency、共享资源 contention 和下游 queue feedback，再决定新请求进入、阶段切换与资源份额。

这一分支改善 pipeline balance，却新增跨组件状态、反馈振荡和公平性问题；作者 workload 的吞吐收益不能外推到不同分辨率、steps、hardware 或 SLO。单组件瓶颈稳定时，静态分区或普通 iteration-level batching 仍更简单。[受限证据：arXiv:2605.08835v1]

<!-- source-family:SF-2026-ARXIV-2605-08835 -->

## 小结

Continuous Batching 将 batch 从静态输入张量改造成 iteration-level scheduling result。它通过及时移除完成请求、补入新 work 和按 token budget 混合不同 phase，提高 weight reuse 与 GPU utilization。

代价是 scheduler 必须同时维护 token progress 与 KV residency。下一章继续处理这一耦合中的 memory 一侧：怎样让变长 KV state 不依赖大块连续显存。

## Review notes

本轮 Review 明确了 iteration-level scheduling 的稳定定义，并补充 admission、preemption 与 KV state 处置。Continuous Batching 的核心不是维护一个动态数组，而是在每个可重调度边界共同决定 token work 与 memory residency。

2026-07-30 用 nano-vLLM 区分 mechanism、policy 与 state disposition：它展示
动态 iteration membership，同时采用 Prefill-first、phase-exclusive batch 与
release-and-recompute preemption。上述三项均作为版本化实现事实，不改写
Continuous Batching 的通用定义。

Primary-source 校验入口：

- Orca: A Distributed Serving System for Transformer-Based Generative Models, USENIX OSDI 2022: https://www.usenix.org/conference/osdi22/presentation/yu
- nano-vLLM scheduler:
  https://github.com/GeeeekExplorer/nano-vllm/blob/main/nanovllm/engine/scheduler.py
- nano-vLLM KV block manager:
  https://github.com/GeeeekExplorer/nano-vllm/blob/main/nanovllm/engine/block_manager.py
- LLM-42（selective deterministic decode/verify/rollback；作者系统实验边界）:
  https://arxiv.org/abs/2601.17768
- BlockServe（block-grained diffusion-LM batching；Status: Experimental；单 H200 离线证据）:
  https://arxiv.org/abs/2607.08930v1

Orca 论文中的 iteration-level scheduling / selective batching 是机制来源；vLLM、TensorRT-LLM、SGLang 的具体 state machine 与 batch construction 属于各自版本实现。本章只保留机制不变量，不用某个引擎的参数或类名定义 Continuous Batching。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2607-08930:start -->
- `SF-2026-ARXIV-2607-08930` — Daily `2026-07-10`；primary `arXiv:2607.08930v1`；Books review `books-review:SF-2026-ARXIV-2607-08930`。

  **已吸收的语义增量：** 新增证据边界：Change the continuous-batching quantum from an autoregressive token iteration to a diffusion block-denoise cycle. Reclaim completed block slots immediately, align requests at heterogeneous denoising states in one dense layout, and admit work under a token/memory bounding box. 该 delta 已进入 `books/part-05-inference-system/46-continuous-batching.md#L88`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-08930:end -->
