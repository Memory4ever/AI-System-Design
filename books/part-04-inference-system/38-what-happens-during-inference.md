# 第38章 推理到底发生了什么

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 一个请求从 API 进入，到 token 流式返回，经历哪些阶段。

## 本章要回答的问题

Part III 最终交付了一个可加载、可验证的模型资产。但模型文件并不会自己接收请求、管理显存、安排 GPU 工作或持续返回 token。一个请求从 API 到达后，究竟经过哪些状态？为什么 LLM inference 不能被理解成一次普通的 `forward()`？TTFT、TPOT、throughput 与 goodput 又分别测量哪一段系统行为？

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

## 从 Deployment Artifact 到执行身份

Part III 第 31、37 章交付的是经过转换和验证的 deployment artifact。Runtime
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

Part IV 后续章节按三层定位：

| 层次 | 关注对象 | 章节 |
| --- | --- | --- |
| Stage | Prefill、Decode、KV state | 39～41 |
| Mechanism | batching、paging、speculation、memory、PD、scheduling | 42～44、50～52 |
| Runtime / Control | TensorRT-LLM、vLLM、SGLang、Dynamo、KServe LLM | 45～49 |

Framework 会变化，这三层问题不会同时消失。一个新 Serving 项目首先应被问：它改变了哪个 stage、哪类状态、哪项资源约束或哪条 control loop？

## 为什么没有单一“推理性能”

推理系统至少同时面对长 prompt 的 TTFT、长输出的 TPOT、GPU token throughput、KV Cache capacity、P95/P99 tail latency、fairness、deadline 和成本。

优化其中一项可能伤害另一项。更大的 batch 可以提高 arithmetic intensity，却增加 queueing；保留更多 prefix cache 可以减少 Prefill，却占据 Decode 所需 KV capacity；激进 admission 可以提高短时 utilization，却可能让 tail latency 失控。

因此 benchmark 必须声明模型、precision、硬件、并行度、`T_p`/`T_o` 分布、并发、到达过程和 SLO。脱离 workload 的“快几倍”不能直接迁移为系统结论。

## 本章在知识树中的位置

```text
Part III validated model artifact
-> model loading and identity
-> request state machine
-> Prefill
-> Decode + KV state
-> runtime mechanisms
-> serving engines
-> distributed orchestration
-> Part V platform governance
```

第37章交付模型资产，本章把它接入在线 capability-delivery path。第39～41章会拆开 Stage 与状态；第42章以后再逐步回答如何调度、管理和扩展。这个 delivery path 只能执行已发布的 capability contract，不能通过更快的 runtime 修复训练数据、目标或 artifact conversion 的错误。

## 自检问题

1. 为什么 LLM inference 不能视为普通无状态 handler？
2. 请求进入 Decode 前必须满足哪些状态不变量？
3. TTFT 为什么不能只测 Prefill kernel？
4. TPOT 与 end-to-end latency 的关系是什么？
5. Request throughput 与 token throughput 为什么可能给出不同判断？
6. Goodput 相比 throughput 多加入了什么约束？
7. Cancellation 后为什么仍需要显式 RELEASED 状态？
8. Stage、mechanism 和 runtime 三层怎样帮助定位新框架？

## 小结

LLM Serving 的基本对象不是一次函数调用，而是携带 token progress、KV ownership、SLO 和生命周期的请求状态机。Prefill 决定上下文怎样进入模型，Decode 决定输出怎样逐步产生，runtime 则在两者之间持续管理 memory、batch 与 stream。

下一章从全局状态机进入第一段 GPU 主路径：Prefill 如何把 prompt 转换成初始 logits 和可供后续 Decode 使用的 KV state。

## Review notes

本轮将第38章重构为 Part IV 的唯一全局入口，冻结请求状态、指标边界和三层章节地图。具体 paging、speculation、framework feature 与 cluster policy 均留给后续章节。

Primary-source / official entry points：

- Orca, iteration-level scheduling and selective batching, OSDI 2022: https://www.usenix.org/conference/osdi22/presentation/yu
- DistServe, TTFT/TPOT and goodput-oriented disaggregation: https://arxiv.org/abs/2401.09670
- vLLM V1 architecture: https://docs.vllm.ai/en/stable/design/arch_overview/
