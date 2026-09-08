# 第44章 Decode

**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场
**Stable Knowledge Node ID:** `INFER-DECODE`
**Legacy Chapter:** Ch40
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

## nano-vLLM：把一个 Decode Step 落到 Runtime Metadata

在 nano-vLLM 当前实现中，scheduler 从 `running` 队列选择 sequences，为每个
sequence 设置 `num_scheduled_tokens=1`，必要时为即将跨 block boundary 的 token
分配新 KV block。`prepare_decode()` 随后并不重传完整序列，而是为每个 active
request 构造：

```text
input_id      = last_token
position      = len(sequence) - 1
context_len   = len(sequence)
block_table   = logical history -> physical KV blocks
slot_mapping  = current position -> physical write slot
```

五项 metadata 分别回答“算哪个 token”“它处于哪个逻辑位置”“能看多长历史”
“历史 K/V 在哪里”和“新 K/V 写到哪里”。模型语义只要求当前 Query 能看到正确
的 causal history；paged KV layout 则要求 runner 额外提供后两项物理映射。

执行之后，sampler 为 batch 中每个 sequence 返回一个 token id。`postprocess()`
先提交本轮 KV progress，再将 sampled token 追加到 sequence，使它成为下一轮的
`last_token`：

```text
last_token_i
-> prepare Decode metadata
-> model forward / KV append
-> logits_i+1
-> sample token_i+1
-> append to Sequence
-> next iteration
```

到达 EOS 或 `max_tokens` 时，sequence 转为 `FINISHED`，block manager 递减其所有
blocks 的引用计数并把无其他引用的 blocks 放回 free list。这里“输出完成”和
“memory released”属于同一次状态提交；若只完成前者，长时间运行的服务最终仍会
耗尽 KV capacity。

这个案例还解释了 CUDA Graph 为什么更自然地服务 Decode。当前 runner 对非 eager、
batch token 数不超过其捕获上限的 Decode 路径按可容纳的 batch size replay graph；
Prefill 或超出该边界的执行走普通 model path。稳定原因不是“Decode 必须使用
CUDA Graph”，而是 Decode 的单步 shape 边界更容易预捕获，而变长 Prefill metadata
更动态。

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

第 21 章说明 MoE 只激活部分 experts，第 40 章说明训练时 Expert Parallel 需要
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

### Structured Output 要在预算耗尽前证明可完成

<!-- semantic-body-binding:SF-TRUNCPROOF-A-GUARDRAIL-FOR-LLM-BASED-JSON-GENERATION-UNDER-TOKEN-LENGTH-:start -->
Grammar-constrained decoding 保证每一步合法，却不保证剩余 token budget 足以闭合 JSON。Decoder 可根据 tokenizer 与
LL(1) grammar 计算最短 completion lower bound，只有仍可闭合的 token 才 admission；必要时提前选择 closure path。
它以额外 grammar state 和较窄输出空间换 syntactic completeness，不保证 schema 语义或事实正确。无硬预算、自由
文本或复杂非 LL(1) grammar 时，普通 constrained decode/后验校验仍更合适。
<!-- semantic-body-binding:SF-TRUNCPROOF-A-GUARDRAIL-FOR-LLM-BASED-JSON-GENERATION-UNDER-TOKEN-LENGTH-:end -->

### Depth 与 Session 都可以成为 Decode State

<!-- semantic-body-binding:SF-N-VIUM-MIXTURE-OF-EXITS-TRANSFORMER-FOR-ACCELERATED-EXACT-GENERATION:start -->
Early exit 通常减少每 token 计算却改变分布；mixture-of-exits 可以先让不同 token 在不同深度前进，再对需要的 token
补做 upper-layer compute，以保持目标 sampling contract。Runtime 由此同时调度 token × depth state。收益来自提高
有效并行度，代价是 deferred state、负载不均和硬件相关收益；补算或 exactness 条件不成立时回退完整深度。
<!-- semantic-body-binding:SF-N-VIUM-MIXTURE-OF-EXITS-TRANSFORMER-FOR-ACCELERATED-EXACT-GENERATION:end -->

<!-- semantic-body-binding:SF-ATTENTION-ONCE-IS-ALL-YOU-NEED-EFFICIENT-STREAMING-INFERENCE-WITH-STATEF:start -->
持续输入若每次把全历史重新 Prefill，query latency 随 session 增长。Stateful session 可让 runtime 持久推进 KV，只对
新 observation 和 query 执行增量 attention；这要求 session identity、model revision、position、expiry、tenant 与
recovery 全部显式化。它减少重复 Prefill，却增加长寿命显存、stale state 和跨 turn 隔离风险；短会话、更新模型或
无法证明 cache lineage 时仍应重新 Prefill。
<!-- semantic-body-binding:SF-ATTENTION-ONCE-IS-ALL-YOU-NEED-EFFICIENT-STREAMING-INFERENCE-WITH-STATEF:end -->

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

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15070:start -->
用 attention-state 判断推理是否收敛，再在 exit、logit injection 与 jump intervention 之间切换，把 overthinking 从固定 token budget 演进为 request-local control。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-15070:end -->

### Output Length 是随机工作量，不是固定配置

长文本服务如果只看平均输出质量，会掩盖 output-length distribution 的波动：少数异常长响应可以占住 KV、推高 TPOT 尾部并拖慢同批请求。decode admission 因此需要同时估计期望长度与方差，并把 hard token budget、stop contract 和超限行为写入请求身份。logits-level mitigation 可以改变长度倾向，却也可能改变内容分布，不能替代服务侧预算。

收益是把不可控的生成尾部变成可观测、可调度的 workload；代价是截断风险、预测误差和更复杂的用户契约。当长度估计不可靠时，系统应回退到保守预算、分段生成或显式续写，而不是用平均值承诺 SLO。固定上限在短回答、严格协议输出中仍然是更简单的选择。

<!-- source-family:SF-LONG-FORM-LENGTH-VOLATILITY -->

## 本章在知识树中的位置

```text
Prefill
-> initial KV state
-> repeated Decode iterations
-> logits / sampling
-> append token and KV
-> finish or reschedule
```

本章承接第43章的 Prefill 输出，并把“逐 token 推进”交给第45章解释其核心状态。第46章将解决不同长度请求如何共享 GPU。

## 从机制演进到系统设计

Decode 从逐 token kernel loop 演进成长期驻留的状态推进器后，故障恢复也从重启整个服务下沉到 token/KV/checkpoint boundary。Persistent kernel 或 JIT checkpoint 可以减少 launch 和恢复成本，但必须记录最后已提交 token、KV revision 与外部 stream effect，避免恢复后重复输出或重复副作用。

更细恢复粒度换来 device-resident metadata、checkpoint overhead 和更复杂的 communicator failure handling。状态无法证明一致或客户端已观察的输出不可撤销时，应回退请求级重算或终止，而不是猜测续跑。短请求和低故障率 workload 仍可能不值得承担持续 checkpoint 成本。

## 自检问题

1. Autoregressive factorization 为什么造成真实时间依赖？
2. Decode 的 logical shape 与 Prefill 有何不同？
3. KV Cache 消除了哪些 work，又保留了什么？
4. 为什么单请求 Decode 常难以充分复用 weights？
5. 增大 active batch 为什么可能同时提升吞吐并恶化 TPOT？
6. Iteration latency 为什么不必然等于请求 TPOT？
7. Speculative Decoding 是否消除了 autoregressive dependency？
8. Decode runner 为什么必须同时携带 `position`、`context_len` 与 `block_table`？
9. 为什么 sampled token 只能在本轮 KV progress 提交后成为下一轮输入？

## 端侧 Decode 的测量边界

服务器上常把更长 Context 或更大 KV 直接等同于更高 Decode latency；端侧 backend 却可能在不同长度跨过 kernel、tiling、memory mapping 或 accelerator fallback 的执行区间，延迟因而不是单调函数。测量工具本身还可能改变线程调度、缓存或功耗状态。可复现合同必须同时冻结 device/OS、backend、模型与量化、输入输出长度、batch/concurrency、warmup、功耗状态和 instrumentation mode，并报告 regime transition，而不只给一个平均 TPOT。

更完整的 contract 提高了定位能力，却增加实验矩阵和设备依赖；论文里的单设备曲线不能外推到其他 SoC、runtime 或热状态。服务端 workload 稳定且 profiler 干扰可忽略时，传统 latency sweep 仍然合理。[受限证据：arXiv:2605.08913v1]

<!-- source-family:SF-2026-ARXIV-2605-08913 -->

### Decode-only Compute Branch 仍必须尊重单一 KV Owner

某些额外计算只在 decode 阶段有价值，可以绕开 prefill 以降低总成本；但它不能暗中维护第二份不一致的历史状态。主模型 KV 或等价 recurrent state 应有唯一 owner，decode branch 只读取版本化快照并产出可验证的增量。这样保留 phase-specific 优化，同时避免 prefill/decode 分叉后出现无法解释的状态漂移。
<!-- source-family: arxiv:2608.12385v1; semantic-body-binding: decode-only-branch-single-state-owner -->

## 小结

Decode 把模型推理变成持续的状态推进问题。每个请求内部必须按 token 顺序执行，但多个请求可以共享每轮模型执行。性能不只取决于 kernel，还取决于谁进入这一轮、携带多长历史以及何时再次获得资格。

下一章聚焦最重要的持久状态：KV Cache 为什么正确、节省了什么，以及它怎样把计算优化转化为显存管理问题。

## Review notes

本轮补齐 autoregressive factorization、logical shapes、TPOT 时间边界和 batch 小例子，并明确“Decode memory-bound”是由 workload 与 arithmetic intensity 决定的工程判断。

2026-07-30 增补 nano-vLLM Decode step，把 `last_token`、position、context
length、block table、slot mapping 与 sequence/KV state commit 串成完整闭环，并将
CUDA Graph 保留为该实现的 execution optimization，而非 Decode 语义。

Primary-source entry points：

- Orca: https://www.usenix.org/conference/osdi22/presentation/yu
- DistServe: https://arxiv.org/abs/2401.09670
- Speculative Decoding: https://arxiv.org/abs/2211.17192
- nano-vLLM Decode preparation and CUDA Graph path:
  https://github.com/GeeeekExplorer/nano-vllm/blob/main/nanovllm/engine/model_runner.py
- nano-vLLM Decode scheduling, completion and KV release:
  https://github.com/GeeeekExplorer/nano-vllm/blob/main/nanovllm/engine/scheduler.py
- nano-vLLM sequence progress:
  https://github.com/GeeeekExplorer/nano-vllm/blob/main/nanovllm/engine/sequence.py

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-29066 — primary arXiv:2606.29066v1; exact-v1 URL=https://arxiv.org/html/2606.29066v1; Method=https://arxiv.org/html/2606.29066v1 — §Training objective; 4 Training; 4.2 Step-Size Policy Training; Evaluation=https://arxiv.org/html/2606.29066v1 — §5 Experiments; 5.3 Code Generation Evaluation; Setup; Non-proof=https://arxiv.org/html/2606.29066v1 — §7 Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-23521` — primary `arXiv:2606.23521v1`; Method=`arXiv:2606.23521v1 — §3. Design; §Host-mapped memory.; §4.3. Optional Cross-Architecture Execution and GPU-Initiated Networking`; Evaluation=`arXiv:2606.23521v1 — §2.4. Motivating Experiment: Host-Side Dirty Detection; §5. Evaluation`; non-proof=`arXiv:2606.23521v1 — §7. Discussion; §7.5. Limitations and Future Work; §8. Conclusion`; fallback=该 family 的 failure pressure 是：Losing this state after a GPU or communicator failure can discard minutes to hours of work, yet existing recovery mechanisms either restart the whole serving stack or require application-specific checkpoint logic inside every attention and runtime component. 披露的 evaluation signal 是：The persistent kernel consumes a lock-free ring buffer of compute, checkpoint, append-log, and recovery tasks, so the same always-on executor triggers dirty-page detection, stages deltas, and appends committed records to a CPU-visible log in CXL memory or host DRAM. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

### Source-family integration record

<!-- daily-20260628:INFER-DECODE:start -->
### Owner-merged minimal durable delta

Masked-diffusion decode 不必把每一步压成 token-or-mask。Request 可以为每个位置持有连续 x-prediction mixture、异步 progress 与 bounded re-edit state；只有通过 commit rule 的离散 token 才进入 visible frontier。这样 refinement 信息可跨 step 延续，而 cache、step policy 与 commit identity 仍可审计。

### Trade-off、failure、fallback 与 coexistence

连续 mixture 是否被 pretrained MDLM 正确解释只在两组模型/代码任务中验证；它增加 request state、alignment 与 kernel burden，质量或硬件不支持时回退标准 mask/unmask decoder。

<!-- daily-20260628:INFER-DECODE:end -->

<!-- recovered-daily-20260623:INFER-DECODE:start -->
### 2026-06-23 evidence integration — INFER-DECODE

相邻章 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-23521**：Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference 的 exact-v1 机制为：We present Concordia, a runtime that uses a device-resident persistent kernel as the substrate for fault-tolerant LLM inference. 因此 把 persistent-kernel checkpoint、恢复位置和重复 token/side-effect 防护绑定。 该 family 的 failure pressure 是：Losing this state after a GPU or communicator failure can discard minutes to hours of work, yet existing recovery mechanisms either restart the whole serving stack or require application-specific checkpoint logic inside every attention and runtime component. 披露的 evaluation signal 是：The persistent kernel consumes a lock-free ring buffer of compute, checkpoint, append-log, and recovery tasks, so the same always-on executor triggers dirty-page detection, stages deltas, and appends committed records to a CPU-visible log in CXL memory or host DRAM. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:INFER-DECODE:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-08411:start -->
- `SF-2026-ARXIV-2606-08411` — Daily `2026-06-08`；primary `arXiv:2606.08411v1`；Books review `books-review:SF-2026-ARXIV-2606-08411`。

  **已吸收的语义增量：** AsyncLane 用 lane tree 把 DLM 的 prefix refinement 与 frontier advancement 解耦，并以 shared-prefix batching、lookahead reuse 与 cache refresh 管理异步依赖。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08411:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15070:start -->
- `SF-2026-ARXIV-2606-15070` — Daily `2026-06-14`；primary `arXiv:2606.15070v1`；Books review `books-review:SF-2026-ARXIV-2606-15070`。

  **已吸收的语义增量：** 用 attention-state 判断推理是否收敛，再在 exit、logit injection 与 jump intervention 之间切换，把 overthinking 从固定 token budget 演进为 request-local control。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15070:end -->
