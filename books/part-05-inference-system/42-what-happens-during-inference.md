# 第42章 推理到底发生了什么

**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场
**Stable Knowledge Node ID:** `INFER-REQUEST-LIFECYCLE`
**Legacy Chapter:** Ch38
**Status:** Draft

**Roadmap Intent:** 一个请求从 API 进入，到 token 流式返回，经历哪些阶段。

## 本章要回答的问题

Part IV 最终交付了一个可加载、可验证的模型资产。但模型文件并不会自己接收请求、管理显存、安排 GPU 工作或持续返回 token。一个请求从 API 到达后，究竟经过哪些状态？为什么 LLM inference 不能被理解成一次普通的 `forward()`？TTFT、TPOT、throughput 与 goodput 又分别测量哪一段系统行为？

本章的核心判断是：**LLM inference 是一个持续演化的 token-generation process，而不是一次无状态函数调用。**请求会依次经历输入处理、admission、Prefill、Decode、streaming 和完成清理；每一步都在改变 token progress、KV ownership、GPU memory 与调度资格。

本章使用 `T_p` 表示 prompt token 数，`T_o` 表示最终生成 token 数，`R` 表示 active requests 数，`t_a` 表示请求到达时间，`t_1` 表示第一个输出 token 可见时间，`t_i` 表示第 `i` 个输出 token 可见时间。

## 从“加载模型然后调用”开始

最朴素的 Serving 设计是：

```text
HTTP request
-> model.generate(prompt)
-> HTTP response
```

这个抽象对调用者很方便，却隐藏了系统最重要的事实：

- Prompt 长度和输出长度都可能不同。
- 第一个 token 与后续 token 的计算形态不同。
- 请求生成期间持续占有逐层 KV Cache。
- 不同请求可以在每个 Decode iteration 动态组合。
- 用户可能在完整答案结束前持续接收 stream。
- cancellation、timeout 和失败都需要回收状态。

普通 stateless handler 通常在一次调用里完成大部分工作；LLM 请求则可能在数百个 scheduler iterations 中保持存活。系统调度的不只是 request，而是 request 在某个 token position 上的运行时状态。

## 负载差异不是 HTTP 协议差异

传统后端也可能有长事务、streaming 和有状态计算，因此两者不是绝对二分。关键差异是：在 LLM Serving 中，变长、自回归和 GPU-resident state 从特殊情况变成了主导负载形态。

| 维度 | 传统后端服务的常见抽象 | LLM Serving 的主导抽象 |
| --- | --- | --- |
| 调度单位 | request、transaction 或 task | 携带 phase、token progress、KV ownership 和 SLO 的 request state |
| 工作量估计 | 路由和请求类型通常能给出较稳定边界 | 成本随 `T_p`、未知的 `T_o`、stop policy 与并发共同变化 |
| 执行形态 | 一次 handler 内完成主要计算 | Prefill 处理已知 prompt，Decode 按严格依赖逐 token 推进 |
| 活跃状态 | 常在外部存储或进程内维持业务状态 | 每个活跃序列持续占有 GPU KV Cache 与调度表项 |
| Batching | 固定批处理或 request-level worker pool | 每个 iteration 按 token budget 重新组合 active sequences |
| 用户 SLO | end-to-end latency、availability、error rate | TTFT、TPOT、deadline、request/token throughput 与 goodput |
| 路由依据 | endpoint health、区域和实例负载 | 还要考虑 model/adapter identity、prefix/KV locality 与可用 cache capacity |
| 扩缩容信号 | QPS、CPU、memory、queue length | 还需要长度分布、queued tokens、active sequences、KV occupancy 与分位数 SLO |

只按 QPS 比较两个请求，会把一个 `T_p = 32`、`T_o = 8` 的短交互与一个 `T_p = 32K`、输出长度未知的请求视为相同工作。只按“连接是否仍在”调度，也会忽略请求当前处在 Prefill、Decode、blocked streaming 还是释放阶段。后续章节会分别展开这些机制；本章先冻结它们共同依赖的状态契约。

## 从 Deployment Artifact 到执行身份

Part IV 第 35、41 章交付的是经过转换和验证的 deployment artifact。Runtime
加载时必须把它解析成一个不可含糊的 execution identity：

```text
model revision + architecture
+ tokenizer / special tokens / chat template
+ base model + adapter / merge state
+ dtype / quantization and KV format
+ runtime version + inference TP/PP/EP layout
+ generation / stop metadata
```

训练 checkpoint 的 rank/file layout 不能直接充当 Serving layout。Runtime
可以按目标 GPU topology 重新选择 inference `TP/PP/EP`，但新的 mapping、kernel
和 quantization path 必须已经通过 artifact conversion validation。类似地，动态
adapter 不是请求上的一个普通字符串：它参与权重选择、batch compatibility、
prefix-cache identity 和审计。

这组身份是后续状态机的静态前提。请求再携带 prompt tokens、sampling
parameters、SLO 和 runtime state。静态 artifact identity 与动态 request state
没有分开时，cache reuse、故障恢复和行为回归都无法可靠解释。

## 请求状态机

先冻结一个与具体框架无关的状态机：

```text
ARRIVED
  -> VALIDATED
  -> TOKENIZED
  -> WAITING_FOR_ADMISSION
  -> PREFILLING
  -> DECODING
  -> FINISHED
  -> RELEASED
```

还可能出现旁路：

```text
WAITING / PREFILLING / DECODING
  -> CANCELLED | TIMED_OUT | FAILED
  -> RELEASED
```

每次状态迁移都必须维护不变量。例如请求进入 `DECODING` 前，prompt 对应的初始 KV state 必须已经可用；进入 `RELEASED` 后，block、临时 buffer 和调度表项都不能继续被引用。

## 一次端到端请求

### API 与输入处理

Frontend 完成认证、限流、schema 校验、chat template、tokenization 和 generation parameters 归一化。Tokenizer 必须与模型资产一致；错误的 vocabulary、special tokens 或 chat template 不一定触发 GPU error，却会改变输入语义。

### Admission

请求不会因为已经到达就必然立刻运行。系统需要判断模型与 adapter 是否已加载、prompt 是否超过限制、是否有足够 KV blocks 和 token budget、排队后是否仍可能满足 SLO，以及租户配额和优先级是否允许进入。

Admission control 的目标不是让 queue 永不为空，而是避免接受一个注定造成 memory exhaustion 或大面积 SLO violation 的请求。

### Prefill

Prefill 一次处理 prompt tokens，得到第一个 next-token distribution，并在每一层写入 prompt 的 K/V。它决定第一个输出 token 何时可能产生，也是长 prompt 影响其他请求的主要入口。

### Decode loop

Decode 每轮处理当前新 token，读取历史 KV Cache，产生下一个 token，再追加新的 K/V。单个请求内部存在严格依赖：

```text
token_i
-> forward step
-> logits_i+1
-> sampling
-> token_i+1
```

不同请求可以在同一轮共同执行，但同一请求的第 `i+1` 步不能早于第 `i` 步完成。

### Streaming 与完成

Token 经 detokenization 后可以持续发送给客户端。模型侧停止条件包括 EOS、stop tokens 和最大生成长度；系统侧还包括 cancellation、deadline、quota 和 transport failure。

完成不是“最后一个 token 已算出”这么简单。Runtime 还必须释放 KV blocks、清理 request state、记录 usage 与 latency，并确保 stream 的终止语义对调用者可见。

## 实现案例：nano-vLLM 中的一次请求闭环

nano-vLLM 适合用来验证上述状态机，因为它把 engine loop、scheduler、block
manager 与 model runner 保留为几个可直接追踪的组件。这里讨论的是项目
`main` 分支在 2026-07-30 的实现，package version 为 `0.2.0`。它是作者明确定位
的轻量实现，用于观察机制；它既不是 vLLM 当前 V1 的源码缩写，也不能替代生产
Serving 对 streaming、cancellation、multi-model、故障恢复和分布式控制面的要求。

它的顶层循环可以压缩为：

```text
add_request(prompt)
-> tokenize
-> Sequence(status=WAITING, is_prefill=True)
-> Scheduler.add

while waiting or running:
    seqs, is_prefill = Scheduler.schedule()
    token_ids = ModelRunner.run(seqs, is_prefill)
    Scheduler.postprocess(seqs, token_ids, is_prefill)
    collect FINISHED sequences
```

这段循环揭示了 Serving Runtime 的核心 contract：scheduler 不执行模型，
model runner 不决定谁获得资源，postprocess 则必须把本轮计算结果提交回请求与
KV 状态。一次 iteration 只有在三者都完成后才算真正前进。

对一个没有 prefix hit 的请求，状态演化是：

| 时刻 | Scheduler / Sequence 状态 | Model runner 输入 | KV 状态 |
| --- | --- | --- | --- |
| 到达 | `WAITING`、`is_prefill=True` | 尚未执行 | 尚未分配 |
| Prefill 调度 | 预留 block，记录本轮 `num_scheduled_tokens`；若已排入 prompt 尾部，当前代码先置为 `RUNNING` | prompt 的未缓存区间 | 将新 K/V 写入 `slot_mapping` 指定位置 |
| Prefill 提交 | `postprocess` 提交本轮进度与首个生成 token | 最后 prompt position 已产生首 token logits | 初始 KV history 现在可供下一轮 Decode |
| Decode iteration | 每个 active sequence 调度 1 token | 每请求的 `last_token` | 读取历史 block table，并追加一个 position |
| 停止 | `FINISHED`，从 running 移除 | 不再进入下一轮 | 引用计数递减，block 可被回收 |

表中把“排入本轮”和“执行结果提交”分开，是因为当前代码会在完整 prompt work
被调度时先修改 `RUNNING` 标记，而真正可供下一轮使用的 KV 与生成 token 要等
`ModelRunner.run()` 成功返回并完成 `postprocess()`。通用 Runtime 可能采用不同
枚举，但不能省略 reservation 与 commit 的语义边界。

这个简化实现还暴露了一个重要的版本化 policy：当前 `schedule()` 只要选出了
Prefill work 就立即返回，因此同一次 model-run batch 是 Prefill 或 Decode
二选一，并不在同一轮混合两种 phase。它仍然可以在 iteration 边界让请求进入、
推进和退出，但“iteration-level scheduling”不等于“每个实现都必须把 Prefill
与 Decode 混在同一个 kernel batch”。第46章会继续拆解这个边界。

从第一性原理看，真正应从案例中保留的不是类名，而是四条不变量：

1. 调度结果必须同时满足 token budget 与 KV capacity。
2. Model runner 必须收到与 request progress 一致的 tokens、positions 和 KV
   mapping。
3. Sampling 结果只有在对应模型执行与 KV 写入完成后才能提交给 sequence。
4. Finish、preempt 或 failure 都必须定义 KV ownership 的处置方式。

## 指标必须绑定时间边界

### TTFT

```text
TTFT = t_1 - t_a
```

它包含 frontend、queueing、tokenization、admission、Prefill、首 token sampling 和首次传输。只测 GPU Prefill kernel 不能代表用户看到的 TTFT。

### TPOT

对 `T_o > 1` 的请求，一种常见定义是：

```text
TPOT = (t_T_o - t_1) / (T_o - 1)
```

它概括首 token 之后的平均输出节奏。逐 token 间隔也常称 inter-token latency；监控必须明确是否包含 streaming transport 与客户端 buffering。

### End-to-end latency

```text
E2E latency = t_T_o - t_a
E2E ~= TTFT + (T_o - 1) * TPOT
```

第二行只是忽略抖动后的分解，不是性能保证。输出长度本身由模型、sampling 和 stop policy 决定。

### Throughput 与 Goodput

Request throughput 统计完成请求数，token throughput 统计单位时间处理的 input/output tokens。二者不能互相替代：一个长上下文请求和一个短对话请求对系统的成本完全不同。

Goodput 只统计满足既定 SLO 的有效工作：

```text
goodput
= completed work satisfying TTFT / TPOT / deadline objectives
```

如果吞吐上升来自让更多请求超时，系统做了更多 work，却没有交付更多符合目标的 capability。

## 三层观察模型

Part V 后续章节按三层定位：

| 层次 | 关注对象 | 章节 |
| --- | --- | --- |
| Stage | Prefill、Decode、KV state | 43～45 |
| Mechanism | batching、paging、speculation、memory、PD、scheduling | 46～48、54～56 |
| Runtime / Control | TensorRT-LLM、vLLM、SGLang、Dynamo、KServe LLM | 49～53 |

Framework 会变化，这三层问题不会同时消失。一个新 Serving 项目首先应被问：它改变了哪个 stage、哪类状态、哪项资源约束或哪条 control loop？

推理预算本身也应进入 request contract。`reasoning_effort`、最大思考 token 或自适应计算开关不是普通展示参数：它们会改变 decode 路径、成本、deadline 与可比较的质量分布。Gateway 可以接收预算，admission 按租户与 SLO 判定是否允许，runtime 只执行已批准的上限；模型自报“还需要思考”最多是扩容提议，不能自行突破预算。固定预算在可预测延迟优先时仍是基线，自适应预算只有在额外计算的边际收益经过校准且可回退时才成立。<!-- semantic-body-binding:SF-2026-ARXIV-2608-16956 -->

第24章的 editable/block generation 还会改变 Stage contract：输出可能先处于 provisional state，再经 correction 或 verification commit。Part V 不重新定义生成概率，只负责让 mutable window、cache invalidation、rollback 和 user-visible streaming 在 runtime 中一致。图像、视频和 action workload 还要把 modality decoder 与不可逆 action deadline 纳入同一端到端时间边界。

## 为什么没有单一“推理性能”

推理系统至少同时面对长 prompt 的 TTFT、长输出的 TPOT、GPU token throughput、KV Cache capacity、P95/P99 tail latency、fairness、deadline 和成本。

优化其中一项可能伤害另一项。更大的 batch 可以提高 arithmetic intensity，却增加 queueing；保留更多 prefix cache 可以减少 Prefill，却占据 Decode 所需 KV capacity；激进 admission 可以提高短时 utilization，却可能让 tail latency 失控。

因此 benchmark 必须声明模型、precision、硬件、并行度、`T_p`/`T_o` 分布、并发、到达过程和 SLO。脱离 workload 的“快几倍”不能直接迁移为系统结论。

## Pipeline Fusion：减少 Handoff，也收紧 Failure Domain

多模态实时系统把同一个推理状态机扩展到连续输入与连续输出。传统 speech-to-speech 路径把
ASR、translation 和 TTS 分成独立 stages：每层容易替换、监控和回退，却累积等待与中间误差。
端到端 streaming model 可以边接收音频、边生成 acoustic/text tokens，用 lookahead 换取翻译质量，
从而减少完整 utterance barrier。

```text
modular cascade
  explicit boundaries + replaceability + broad fallback
  but repeated buffering / handoff / error propagation

end-to-end streaming
  shared state + lower coordination latency + voice continuity
  but tighter coupling / harder attribution / privacy and drift risk
```

这不是“fusion 一定优于 cascade”。长尾语言、独立合规过滤、离线高质量或局部替换优先时，
cascade 仍然合理；device deployment 还可能因 coverage、thermal 或 quality 保留 fallback。Lookahead
只是模型/runtime buffer，不能被当成完整端到端 latency；评估仍需加入 capture、network、queue、
playback、P95/P99 与错误恢复。2025 年 Google 的 S2ST 部署是该演进的受限案例，公开材料没有
完整硬件与 tail-SLO contract，因而正文只吸收 pipeline trade-off。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-20537:start -->
#### Graph-bound Execution State 需要独立的 Restore Contract

端侧 small-batch runtime 过去可以在进程启动时重建 graph、buffer 与 backend state；模型固定、启动不在关键路径时，这条路径最简单。物理 AI 的低延迟切换和故障恢复把启动成本带进 SLO 后，可以在经过声明的 graph boundary 捕获静态 buffer、执行位置与 backend metadata，形成可恢复的 execution-state capsule。Runtime 拥有 capsule schema、graph/artifact binding 与兼容性检查；scheduler 只能请求 restore，不能把旧 capsule 解释为当前图的有效状态。

这条路径用静态内存、图绑定和 backend 特化换更低恢复延迟，也新增 stale buffer、设备状态不完整和版本错配风险。恢复前必须验证 model/graph/kernel/device identity，失败时冷启动并重建状态；capsule 通过也不证明任务语义或物理动作安全。`arXiv:2606.20537v1` 只支持作者在其 on-device runtime、small-batch workload 与 graph contract 下的机制和实验，不能外推为任意 backend 的通用 checkpoint 格式。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-20537:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-25838:start -->
后端路由器可以依据请求级 confidence 在快速和高质量路径之间选择，但 confidence 只拥有 route proposal 权。阈值需按 workload 校准，并记录 fallback 与 outcome；漂移、低置信或高风险请求回退 canonical backend，不能把 router 自评分当成正确性。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-25838:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-28529:start -->
把 embodied inference optimization 从 per-step latency 扩展到 closed-loop task time、success 与 hardware-dependent sweet spot。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-28529:end -->

## 本章在知识树中的位置

```text
Part IV validated model artifact
-> model loading and identity
-> request state machine
-> Prefill
-> Decode + KV state
-> runtime mechanisms
-> serving engines
-> distributed orchestration
-> Part VI platform governance
```

第41章交付模型资产，本章把它接入在线 capability-delivery path。第43～45章会拆开 Stage 与状态；第46章以后再逐步回答如何调度、管理和扩展。这个 delivery path 只能执行已发布的 capability contract，不能通过更快的 runtime 修复训练数据、目标或 artifact conversion 的错误。

### 并行扩展必须先移出不可扩展的 Host Critical Path

增加 Tensor Parallel degree 在矩阵计算占主导时可以缩短单步执行；当 scheduler、输入输出搬运、sampling 与
post-processing 仍由一个串行 host path 承担，设备越多，Amdahl 串行项占比反而越高。此时问题不再是继续切分
matmul，而是把一次 iteration 拆成可重叠但仍有提交边界的阶段：scheduler 只发布本轮 work，异步 I/O 搬运
必要状态，device-side 或 sequence-parallel sampling 产生候选，request state owner 最后原子提交 token 与完成状态。

这种分解以更多 stream、buffer、event 与取消协议换取 overlap；任一异步阶段若读取旧 batch epoch、覆盖仍在使用的
buffer，或在 cancellation 后继续提交，都会把性能优化变成正确性错误。并行度选择因此必须绑定 model、batch、
sequence shape、sampling path 与硬件拓扑，以端到端 goodput 而不是 kernel speedup 验收。工作量很小、host overhead
不显著或 backend 缺少可靠异步状态机时，较低并行度和同步路径仍是更稳健的基线。exact-v1 的作者实验只支持其
系统与配置中的瓶颈迁移，不证明某个 TP degree 对其他 workload 普遍最优。

<!-- source-family:SF-ASYNC-INFERENCE-OVERHEADS -->

## 从机制演进到系统设计

请求生命周期最初以一次 prompt→response 为边界；会话、Agent 和交互式多模态 workload 出现后，request 之外还存在 idle、tool wait、state mutation 和下一 decision point。Runtime 可以利用空闲期把 session 推演到下一个 decision point，但结果只能作为 speculative state 保存，并绑定 base-state identity、模型与采样配置、confidence gate 和失效条件。下一次真实输入到达后，acceptance gate 重新核对这些身份；只有命中路径才原子提交预推进结果，任何用户输入、环境变化或 state drift 都使其失效并回到普通 Prefill/Decode。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-29565 -->

跨请求预推进把一部分 Prefill 和入口 Decode 移出 critical path，却会消耗闲时算力并引入 false accept、stale state、隐私保留和资源公平问题。它与 draft-model speculative decoding 不同：这里推测的是“下一次会话状态”，而不是同一请求中的 token；命中率、错误接纳率、能耗和取消成本必须一起进入 SLO。现有结果限专有 engine、单机量化 target 与 capability-gated fast path，较小 target 在受测配置下并未触发 gate，且大量收益来自测量常数上的闭式推导，不能外推为任意 session 的实测收益。置信漂移或任何 state mutation 都必须使预推进失效并恢复普通 Decode；单次无状态请求、低重复会话或状态频繁变化时，按需执行仍是更简单且更容易隔离的分支。

### Session-local Surrogate 必须携带切换与回退身份

所有 turns 都使用同一个大模型，在会话短、主题漂移大或质量边界严格时最稳健；长会话逐渐收敛到较窄的局部
响应分布后，继续为每轮支付完整 target-model 成本可能没有必要。一个条件分支利用早期 turns 估计 session-local
response manifold，以 target 产生的数据适配较小 surrogate，并在后续 turns 切换。request lifecycle 因而需要保存
base model、surrogate、soft prompt、适配数据、切换条件与 rollback policy，而不能只记录“当前模型名”。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11317:start -->
surrogate 只拥有低成本 response proposal，质量 gate 仍应比较 target/reference 并保留回退权。局部 manifold 估计错误、
主题漂移、长尾请求或适配延迟无法摊销时，应回到 target model；频繁切换还会引入 session consistency、缓存失效、
额外显存和 tail-latency 风险。现有证据只支持 exact-v1 披露的 dialogue distribution、target/surrogate 组合、适配
与 rollback 实验，不能外推为跨模型、跨部署或生产尾部的普遍收益。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11317:end -->

## 自检问题

1. 为什么 LLM inference 不能视为普通无状态 handler？
2. 请求进入 Decode 前必须满足哪些状态不变量？
3. TTFT 为什么不能只测 Prefill kernel？
4. TPOT 与 end-to-end latency 的关系是什么？
5. Request throughput 与 token throughput 为什么可能给出不同判断？
6. Goodput 相比 throughput 多加入了什么约束？
7. Cancellation 后为什么仍需要显式 RELEASED 状态？
8. Stage、mechanism 和 runtime 三层怎样帮助定位新框架？
9. nano-vLLM 的 `schedule -> run -> postprocess` 为什么是一个状态提交闭环？
10. 为什么“每轮只运行一种 phase”是实现 policy，而不是 Prefill/Decode 的定义？

## 小结

LLM Serving 的基本对象不是一次函数调用，而是携带 token progress、KV ownership、SLO 和生命周期的请求状态机。Prefill 决定上下文怎样进入模型，Decode 决定输出怎样逐步产生，runtime 则在两者之间持续管理 memory、batch 与 stream。

下一章从全局状态机进入第一段 GPU 主路径：Prefill 如何把 prompt 转换成初始 logits 和可供后续 Decode 使用的 KV state。

## Review notes

本轮将第42章重构为 Part V 的唯一全局入口，冻结请求状态、指标边界和三层章节地图。自检答案回填增加传统后端与 LLM Serving 的负载契约对照，并修正七 Part 改版后的章节编号。具体 paging、speculation、framework feature 与 cluster policy 均留给后续章节。

2026-07-30 增补 nano-vLLM implementation case，用最小 engine loop 连接请求状态、
token progress、模型执行与 KV ownership。只吸收可跨 Runtime 复用的状态契约；
当前 Prefill-first、phase-exclusive batch 等行为明确保留为版本化实现事实。

Primary-source / official entry points：

- Orca, iteration-level scheduling and selective batching, OSDI 2022: https://www.usenix.org/conference/osdi22/presentation/yu
- DistServe, TTFT/TPOT and goodput-oriented disaggregation: https://arxiv.org/abs/2401.09670
- vLLM V1 architecture: https://docs.vllm.ai/en/stable/design/arch_overview/
- nano-vLLM repository and project scope: https://github.com/GeeeekExplorer/nano-vllm
- nano-vLLM engine loop: https://github.com/GeeeekExplorer/nano-vllm/blob/main/nanovllm/engine/llm_engine.py
- nano-vLLM scheduler: https://github.com/GeeeekExplorer/nano-vllm/blob/main/nanovllm/engine/scheduler.py
- nano-vLLM request state: https://github.com/GeeeekExplorer/nano-vllm/blob/main/nanovllm/engine/sequence.py
- Google Research, "Real-time speech-to-speech translation", 2025
  （pipeline-fusion bounded case）:
  https://research.google/blog/real-time-speech-to-speech-translation/

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-27906 — primary arXiv:2606.27906v1; exact-v1 URL=https://arxiv.org/html/2606.27906v1; Method=https://arxiv.org/html/2606.27906v1 — §7.2. Methodology and Outcomes on Phi-3.5-V; Evaluation=https://arxiv.org/html/2606.27906v1 — §2. Platform and Experimental Setup; 3.1. Phase-Level Results; 6.1. Three-Backend Benchmark; Non-proof=https://arxiv.org/html/2606.27906v1 — §8. Discussion; 10. Conclusion。
- SF-2026-ARXIV-2606-28529 — primary arXiv:2606.28529v1; exact-v1 URL=https://arxiv.org/html/2606.28529v1; Method=https://arxiv.org/html/2606.28529v1 — §Optimization Methods.; B.1 Optimization Method Settings; Evaluation=https://arxiv.org/html/2606.28529v1 — §4 Experiments; 4.1 Setup; Simulation Task Setup.; Non-proof=https://arxiv.org/html/2606.28529v1 — §5 Conclusion; 6 Limitations; A.3 Assumptions and Limitations。
- SF-2026-ARXIV-2606-28565 — primary arXiv:2606.28565v1; exact-v1 URL=https://arxiv.org/html/2606.28565v1; Method=https://arxiv.org/html/2606.28565v1 — §2.1. Modern LLMs and Inference Frameworks; 3.3. Gaps in Existing Approaches; 4. Tool Architecture and Methodologies; Evaluation=https://arxiv.org/html/2606.28565v1 — §5.2. Production Kernel Microbenchmarking; 6. Experimental Setup; 7. Results and Analysis; Non-proof=https://arxiv.org/html/2606.28565v1 — §8. Conclusions; Appendix B Limitations。

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25838**：Primary `arXiv:2606.25838v1`；Method `https://arxiv.org/html/2606.25838v1 — §III Method; IV Confidence-Aware Routing`；Evaluation `https://arxiv.org/html/2606.25838v1 — §V Experiments; V-A Evaluation protocol; VI Deployment Patterns`；未证明边界 `https://arxiv.org/html/2606.25838v1 — §VII-C Limitations and future work`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

#### 2026-06-29 source-specific Review notes

Review note：`SF-2026-ARXIV-2606-29565`；Method `https://arxiv.org/html/2606.29565v1 — §2 Problem Formulation; speculative pre-positioning state machine`；Evaluation `https://arxiv.org/html/2606.29565v1 — §4 Experimental Setup; 5 Evaluation`；未证明边界 `https://arxiv.org/html/2606.29565v1 — §6 Discussion`。

<!-- june29-owner:INFER-REQUEST-LIFECYCLE:start -->
### 2026-06-29 来源范围补记

`SF-2026-ARXIV-2606-29565` 的既有审阅记录限 LayerScale 专有 engine、单 H100、70B-class 4-bit target 的 capability-gated fast path；8B BF16 不触发 gate，大量收益为测量常数上的闭式推导，并非任意会话与模型的实测收益。Method/Evaluation/Discussion 定位见上方 source-specific Review note。

<!-- june29-owner:INFER-REQUEST-LIFECYCLE:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-ASYNC-INFERENCE-OVERHEADS:start -->
- `SF-ASYNC-INFERENCE-OVERHEADS` — Daily `2026-06-02`；primary `arXiv:2606.01927v1`；Books review `books-review:SF-ASYNC-INFERENCE-OVERHEADS`。

  **已吸收的语义增量：** 补 scheduling/I/O overlap、sequence-parallel sampling 与 Amdahl optimal-TP 边界。
<!-- daily-books-trace:SF-ASYNC-INFERENCE-OVERHEADS:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20537:start -->
- `SF-2026-ARXIV-2606-20537` — Daily `2026-06-19`；primary `arXiv:2606.20537v1`；Books review `books-review:SF-2026-ARXIV-2606-20537`。

  **已吸收的语义增量：** `Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving` 路由到 `INFER-REQUEST-LIFECYCLE`：Execution-State Capsule 在 graph-boundary 捕获可恢复的静态 buffer/执行状态，使 on-device small-batch serving 可 checkpoint/restore，而非重建整个 runtime；FlashRT 拥有 capsule schema 与兼容性，失配时冷启动。代价是图绑定、静态内存和 backend 特化。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20537:end -->
