# Daily Research — 2026-07-07

**规范：** V3
**窗口：** 2026-07-06T09:00:00+08:00 ～ 2026-07-07T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T16:30:00+08:00

## 1. 结论

本窗复用并核实 1,295 个去重 arXiv v1 原始身份，逐条按标题与完整摘要重新判断项目贡献；旧恢复队列 42 项中，13 个材料家族通过当前门槛，29 项因仅是领域应用、局部方法包装、通用 benchmark/Agent 组合或没有改变长期设计判断而转为 pre-denominator closure。关闭结果汇总在本报告的复核结论中，不在正文伪装成候选。

13 项均达到与评分相称的证据审阅深度，并重新检查撤回/纠错信号与首次公开 owner。旧报告标记为 `Integrate` 的机制已经出现在相应 Books 正文，本次统一改为“已有覆盖”；不重复追加，也不以 evidence trace 代替正文承载。独立复核已确认候选准入、证据边界与 body anchor 闭合。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 该源在目标历史窗口后才成为每日固定源；本次不作追溯性覆盖断言 | 不适用 | 无 |
| SRC-ANTHROPIC | 该源在目标历史窗口后才成为每日固定源；本次不作追溯性覆盖断言 | 不适用 | 无 |
| SRC-GOOGLE-AI | 该源在目标历史窗口后才成为每日固定源；本次不作追溯性覆盖断言 | 不适用 | 无 |
| SRC-META-AI | 该源在目标历史窗口后才成为每日固定源；本次不作追溯性覆盖断言 | 不适用 | 无 |
| SRC-QWEN | 该源在目标历史窗口后才成为每日固定源；本次不作追溯性覆盖断言 | 不适用 | 无 |
| SRC-DEEPSEEK | 该源在目标历史窗口后才成为每日固定源；本次不作追溯性覆盖断言 | 不适用 | 无 |
| SRC-MOONSHOT | 该源在目标历史窗口后才成为每日固定源；本次不作追溯性覆盖断言 | 不适用 | 无 |
| SRC-TENCENT-HUNYUAN | 该源在目标历史窗口后才成为每日固定源；本次不作追溯性覆盖断言 | 不适用 | 无 |
| SRC-ZAI | 该源在目标历史窗口后才成为每日固定源；本次不作追溯性覆盖断言 | 不适用 | 无 |
| SRC-BYTEDANCE-SEED | 该源在目标历史窗口后才成为每日固定源；本次不作追溯性覆盖断言 | 不适用 | 无 |
| SRC-BAIDU-ERNIE | 该源在目标历史窗口后才成为每日固定源；本次不作追溯性覆盖断言 | 不适用 | 无 |
| SRC-XIAOMI-MIMO | 该源在目标历史窗口后才成为每日固定源；本次不作追溯性覆盖断言 | 不适用 | 无 |
| SRC-MINIMAX | 该源在目标历史窗口后才成为每日固定源；本次不作追溯性覆盖断言 | 不适用 | 无 |
| SRC-ARXIV | 复核本窗官方公告 owner、1,295 个去重 v1 身份及旧恢复队列；逐条标题、边界项完整摘要语义筛选后保留 13 项 | 已检查 | 无 |

本窗没有触发需要改变候选或结论的按需来源。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation](https://arxiv.org/html/2607.02577v1) | 2026-07-07T08:00:00+08:00 | Tool-calling evaluation must separate typed tool/action checks, outcome state and qualitative judgment. Deterministic gates should own verifiable invariants; a restricted judge …；`3+3+3=9` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling](https://arxiv.org/html/2607.02980v1) | 2026-07-07T08:00:00+08:00 | Teacher-distilled selection keeps dense attention as semantic owner; a coexisting branch can put an approximate chunk-mass selector directly into hierarchical forward attention …；`3+2+3=8` | 深入完成 | 已有覆盖：`MODEL-LONG-CONTEXT`，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [SPORK: Self-Speculative Forking to Accelerate Agentic LLM Inference](https://arxiv.org/html/2607.03333v1) | 2026-07-07T08:00:00+08:00 | Token speculation can be layered with read-only action speculation: fork the main model from shared prefix KV, confidence-gate an early tool probe, execute only read-only calls,…；`3+3+3=9` | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING`，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Online Linear Programming for Multi-Objective Routing in LLM Serving](https://arxiv.org/html/2607.03948v1) | 2026-07-07T08:00:00+08:00 | When output length is heterogeneous and KV grows over time, a queue snapshot cannot express the opportunity cost of admitting a request across future batch and memory capacity. …；`2+2+3=7` | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [CoCoScale: Leveraging Layer-wise Scaling to Unlock the Potential of Online LLM Serving](https://arxiv.org/html/2607.04181v1) | 2026-07-07T08:00:00+08:00 | A full model replica is not the only elastic unit. A controller can choose replication counts for consecutive Transformer layer segments; the scheduler scatters sub-batches acro…；`3+3+2=8` | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [HiFA4: Training-Free 4-bit FlashAttention on Ascend HIF4 NPUs for LLM Inference](https://arxiv.org/html/2607.04302v1) | 2026-07-07T08:00:00+08:00 | Attention quantization should first diagnose asymmetric Q/K structure. When calibration confirms the K-outlier regime, a paired diagonal transform can scale Q and inversely scal…；`3+2+3=8` | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture](https://arxiv.org/html/2607.04391v1) | 2026-07-07T08:00:00+08:00 | The immutable source corpus remains evidence truth while relational metadata, semantic overlays and query profiles are revisable derived views. This is a concrete operational in…；`2+2+2=6` | 标准完成 | 已有覆盖：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Elastic Gang: Per-Token Membership Change for a Hard-Barriered LLM Inference Gang Co-Scheduled with OS Processes](https://arxiv.org/html/2607.04668v1) | 2026-07-07T08:00:00+08:00 | A generation increments a global epoch; a core joins only after parking its tenant and ACKing that epoch. Each token snapshots requested intersect current-ACKed cores into one g…；`3+2+3=8` | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Multi-Turn On-Policy Distillation with Prefix Replay](https://arxiv.org/html/2607.04763v1) | 2026-07-07T08:00:00+08:00 | The teacher's recorded multi-turn history and observations are replayed as a prefix; the student generates the action only at the supervised step, and the teacher supplies dense…；`3+3+3=9` | 深入完成 | 已有覆盖：`TRAIN-SFT`，[Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses](https://arxiv.org/html/2607.05029v1) | 2026-07-07T08:00:00+08:00 | The v1 demonstrates forged-reasoning entries that persist through agent memory, amplify through repeated retrieval/consensus, and can evade or defeat tested defenses; SENTINEL r…；`3+3+3=9` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [KVpop -- Key-Value Cache Compression with Predictive Online Pruning](https://arxiv.org/html/2607.05061v1) | 2026-07-07T08:00:00+08:00 | Future attention mass after a protected window becomes the retention target. A boundary-focused loss trains a lightweight stateless or recurrent scorer; scoring may be delayed u…；`3+2+3=8` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation](https://arxiv.org/html/2607.05147v1) | 2026-07-07T08:00:00+08:00 | A semi-autoregressive drafter proposes multiple tokens with lightweight sequential dependency, while a confidence head predicts how far verification should extend. A hardware-aw…；`3+2+3=8` | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING`，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Weak-to-Strong Generalization via Direct On-Policy Distillation](https://arxiv.org/html/2607.05394v1) | 2026-07-07T08:00:00+08:00 | Instead of imitating a weaker post-RL teacher's final policy, Direct-OPD contrasts that teacher with its own pre-RL reference. The log policy ratio becomes a dense directional r…；`3+3+3=9` | 深入完成 | 已有覆盖：`TRAIN-SFT`，[Ch29](../../../../books/part-04-training-system/29-sft.md) |

## 4. 证据与知识整合

### [Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation](https://arxiv.org/html/2607.02577v1)

**系统推理。** 问题是 tool-calling benchmark 只看最终文本会把 schema、执行副作用和 judge 偏差混在一起。论文把参数类型、工具结果、状态变化与 evaluator 分账，并审计基准本身的有效性；实验只证明所审 benchmark 的失真模式，不能推出所有 Agent 的绝对能力。代价是更重的 trace、typed checker 和版本化 judge，收益是让 release gate 可解释。


<!-- claim:SF-2026-ARXIV-2607-02577:start -->Tool-calling evaluation must separate typed tool/action checks, outcome state and qualitative judgment. Deterministic gates should own verifiable invariants; a restricted judge may handle residual semantic ambiguity, but only with full trace preservation, repeated-run variance, human adjudication and versioned evaluator artifacts. Neither branch is ground truth by default. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-02577:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Tool-calling evaluation must separate typed tool/action checks, outcome state and qualitative judgment. Deterministic gates should own verifiable invariants; a restricted judge may handle residual semantic ambiguity, but only with full trace preservation, repeated-run variance, human adjudication and versioned evaluator artifacts. Neither branch is ground truth by default. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.02577v1#S3 :: trace-level disagreement taxonomy, reproducibility analysis, corrected evaluator and deterministic-first protocol with restricted judge fallback`；Evaluation：`https://arxiv.org/html/2607.02577v1#S4 :: author audit covers four tool-calling benchmark families, complete traces, expert adjudication and repeated judge runs; it does not establish a new model ranking`；Limitations/Counterevidence：`https://arxiv.org/html/2607.02577v1#S5 :: evidence diagnoses selected benchmark/evaluator configurations; artifact release was still pending and evaluator agreement does not prove task representativeness`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `PLATFORM-EVALUATION-SYSTEM` 的 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling](https://arxiv.org/html/2607.02980v1)

**系统推理。** 问题是长上下文稀疏注意力若只做局部 Top-k，会破坏层级信息流。方法把选择器嵌入 forward path 并分层组织稀疏连接，改变 token state 的可达性；作者在指定模型和任务上证明扩展性，未证明无限上下文或任意分布稳健。代价是 selector 训练、稀疏 kernel 与最坏切片退化，短上下文仍可用 dense attention。


<!-- claim:SF-2026-ARXIV-2607-02980:start -->Teacher-distilled selection keeps dense attention as semantic owner; a coexisting branch can put an approximate chunk-mass selector directly into hierarchical forward attention so next-token loss trains selection. This improves ownership alignment but adds landmark/query calibration, position-rule coupling, selector misses, union overfetch, continued-training cost and specialized sparse kernels; it remains an approximation rather than exact full attention. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-02980:end -->

**旧方案与约束变化。** `Native sparse attention already couples selector training, block/GQA granularity and kernels, while teacher-owned stop-gradient warm-up provides an auditable migration path from dense checkpoints.`（`books/part-02-model/22-long-context.md#L194-L228`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Teacher-distilled selection keeps dense attention as semantic owner; a coexisting branch can put an approximate chunk-mass selector directly into hierarchical forward attention so next-token loss trains selection. This improves ownership alignment but adds landmark/query calibration, position-rule coupling, selector misses, union overfetch, continued-training cost and specialized sparse kernels; it remains an approximation rather than exact full attention. 它改变 `MODEL-LONG-CONTEXT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.02980v1#S2.SS2 :: mean/max pooled chunk summaries cannot uniformly approximate query-dependent LogSumExp chunk mass; https://arxiv.org/html/2607.02980v1#S3 :: affine first-order chunk-mass surrogate and hierarchical inter-/intra-chunk normalization place retrieval scores in the forward path; https://arxiv.org/html/2607.02980v1#S4.SS1 through #S4.SS3 :: landmark/query calibration, HoPE/GQA variants, adjacent-query packing and checkpoint migration; https://arxiv.org/html/2607.02980v1#A1 and #A2 :: derivation and proof details`；Evaluation：`https://arxiv.org/html/2607.02980v1#S5.SS1 through #S5.SS3 :: 345M 8K/256K training, dense/sparse baselines, PPL, modified RULER/NIAH and ablations; https://arxiv.org/html/2607.02980v1#S6.SS1 and #S6.SS2 :: 1.4B from-scratch and OLMo3-7B conversion studies; https://arxiv.org/html/2607.02980v1#S7.SS1 and #S7.SS2 :: single-H800 SGLang/Triton inference and adjacent-query overlap; https://arxiv.org/html/2607.02980v1#A4 through #A8 :: recipes and evaluator details`；Limitations/Counterevidence：`https://arxiv.org/html/2607.02980v1#S4.SS1 and #S5.SS3 :: position encoding, query calibration and landmark choices materially affect extrapolation, and the calibration mechanism is not fully understood; https://arxiv.org/html/2607.02980v1#S6.SS2 :: 7B migration cost and short/general-task trade-offs remain recipe-bound; https://arxiv.org/html/2607.02980v1#S7.SS1 :: latency uses one H800, batch 1 and matched Triton kernels, with full attention faster below the reported crossover; Not Disclosed — no production concurrency/arrival/SLO study or independent replication`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L540-L549`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Alternative Branch`。
- Stable owner：`MODEL-LONG-CONTEXT`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `MODEL-LONG-CONTEXT` 的 [Ch22](../../../../books/part-02-model/22-long-context.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [SPORK: Self-Speculative Forking to Accelerate Agentic LLM Inference](https://arxiv.org/html/2607.03333v1)

**系统推理。** 问题是 Agent 推理中的工具动作等待会让 GPU 空转，但提前执行又可能产生不可逆副作用。SPORK 只并行 speculative read-only action，最终仍由目标轨迹验证并提交；作者结果支持其所测工具负载的等待隐藏，未证明有副作用动作可安全猜测。代价是分叉状态、取消、幂等与缓存污染，写操作必须保持串行 authority。


<!-- claim:SF-2026-ARXIV-2607-03333:start -->Token speculation can be layered with read-only action speculation: fork the main model from shared prefix KV, confidence-gate an early tool probe, execute only read-only calls, and admit the observation only after exact final action match. The main action retains commit authority; mismatches use serial fallback, while verified rejected-prefix tokens may be reused as ordinary draft. This spends probe compute and read traffic and adds calibration, cancellation and side-effect boundaries. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-03333:end -->

**旧方案与约束变化。** `Speculation is provisional work whose target/verifier owns commit; Agent phase hints may change proposal budgets but cannot change target authority, while tool authorization and side-effect classes remain outside the model.`（`books/part-05-inference-system/48-speculative-decoding.md#L489-L503`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Token speculation can be layered with read-only action speculation: fork the main model from shared prefix KV, confidence-gate an early tool probe, execute only read-only calls, and admit the observation only after exact final action match. The main action retains commit authority; mismatches use serial fallback, while verified rejected-prefix tokens may be reused as ordinary draft. This spends probe compute and read traffic and adds calibration, cancellation and side-effect boundaries. 它改变 `INFER-SPECULATIVE-DECODING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.03333v1#S2.SS2 :: overlap cost model and break-even condition; https://arxiv.org/html/2607.03333v1#S3 through #S5 :: forced-prefix self-probe, D1 prefix-KV fork, D2 confidence gate, D3 verified-prefix reuse, strict action-match commit and read-only manifest boundary; https://arxiv.org/html/2607.03333v1#A1, #A2 and #A8 :: derivation, partial-token acceptance and late-probe supersession`；Evaluation：`https://arxiv.org/html/2607.03333v1#S6.SS1 through #S6.SS6 :: Qwen3-4B/32B and Qwen3.5-35B-A3B on H20-3e, bf16, vLLM, greedy think-mode, GAIA/HotpotQA/tau2 latency and quality, component ablations, drafter comparison and break-even sweep; https://arxiv.org/html/2607.03333v1#A3 through #A7 :: BrowseComp, serving configuration and format-divergence details`；Limitations/Counterevidence：`https://arxiv.org/html/2607.03333v1#S6.SS3 and #S6.SS6 :: real-network nondeterminism, fast tools, short/no-think decode, format divergence, probe overhead and batching can shrink or reverse benefit; https://arxiv.org/html/2607.03333v1#S8 :: only read-only tools and open serving interfaces are in scope; https://arxiv.org/html/2607.03333v1#A6 through #A8 :: format collapse, small-model boundary and cancellation/supersession; exact action match does not undo quota, privacy or external side effects`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-SPECULATIVE-DECODING`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-SPECULATIVE-DECODING` 的 [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Online Linear Programming for Multi-Objective Routing in LLM Serving](https://arxiv.org/html/2607.03948v1)

**系统推理。** 问题是 LLM routing 同时面对成本、延迟和质量，静态权重无法反映未来 batch/KV 机会。在线线性规划把 shadow price 与未来资源价值带入路由；作者 trace 结果只支持其模型池与需求分布，未证明预测偏差下稳定。代价是在线估计、约束求解和公平性，负载简单时规则路由更可维护。


<!-- claim:SF-2026-ARXIV-2607-03948:start -->When output length is heterogeneous and KV grows over time, a queue snapshot cannot express the opportunity cost of admitting a request across future batch and memory capacity. An online controller can compare SLO-weighted benefit with time-indexed batch/KV shadow prices and update those prices from residual capacity plus historical predicted action columns. This makes cross-time commitment explicit but adds a separate production responsibility: output-length calibration must compare predicted with realized service without being misrepresented as the paper's price-update mechanism. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-03948:end -->

**旧方案与约束变化。** `Ch56 already separates admission, iteration scheduling, routing/placement and autoscaling and requires future-KV feasibility, goodput, calibration and fairness, but did not yet make future batch/KV scarcity an explicit per-request opportunity cost.`（`books/part-05-inference-system/56-inference-scheduling.md#L43-L90`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** When output length is heterogeneous and KV grows over time, a queue snapshot cannot express the opportunity cost of admitting a request across future batch and memory capacity. An online controller can compare SLO-weighted benefit with time-indexed batch/KV shadow prices and update those prices from residual capacity plus historical predicted action columns. This makes cross-time commitment explicit but adds a separate production responsibility: output-length calibration must compare predicted with realized service without being misrepresented as the paper's price-update mechanism. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.03948v1#S2.SS0.SSS0.Px2, #S2.SS0.SSS0.Px5 and #S2.SS0.SSS0.Px6 :: central buffering, release-when-startable admission and time-coupled batch/KV occupancy; https://arxiv.org/html/2607.03948v1#S3.SS1 through #S3.SS3 :: SLO-weighted action reward, online LP constraints, dual shadow prices, SAA history and projected subgradient updates; https://arxiv.org/html/2607.03948v1#A2.SS1 and #A2.SS3 :: pseudocode`；Evaluation：`https://arxiv.org/html/2607.03948v1#S4.SS1 :: Vidur-only simulation on four A100 GPUs with LMSYS-Chat-1M and synthetic P/D-ratio workloads; model, precision, batch/concurrency and exact serving SLO Not Disclosed; https://arxiv.org/html/2607.03948v1#S4.SS2 and #S4.SS3 :: RR/LOR/Random/Power-of-2 baselines, noisy length estimates, objective sweeps and an arrival-rate shift; https://arxiv.org/html/2607.03948v1#A3 :: broader sweeps and tail-weight sensitivity`；Limitations/Counterevidence：`https://arxiv.org/html/2607.03948v1#S6 :: simulation-only, without serving-engine integration, preemption, KV swapping, distributed coordination, heterogeneous priorities or fairness validation; https://arxiv.org/html/2607.03948v1#A1.SS0.SSS0.Px9 :: PD-mixing duration is input-dependent; no LLM-specific theorem/regret/convergence or component ablation. Event-time artifact only partially corresponds to the manuscript noisy-length/tail-objective interface.`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-SCHEDULING` 的 [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [CoCoScale: Leveraging Layer-wise Scaling to Unlock the Potential of Online LLM Serving](https://arxiv.org/html/2607.04181v1)

**系统推理。** 问题是在线 serving 的层间瓶颈不同，整模型同倍率复制会浪费资源。CoCoScale 按层段调整 replication，并在变化时重分布 KV/state；作者在指定模型与集群证明潜在收益，未证明频繁伸缩下无抖动。代价是层段路由、KV migration、版本一致性与恢复，稳定负载下固定副本仍合理。


<!-- claim:SF-2026-ARXIV-2607-04181:start -->A full model replica is not the only elastic unit. A controller can choose replication counts for consecutive Transformer layer segments; the scheduler scatters sub-batches across those replicas, gathers boundary activations and redistributes affected KV partitions during a configuration transition. This reduces whole-instance startup pressure on the evaluated topology but turns activation boundaries, KV ownership and transition coordination into correctness-critical scheduling state. The v1 manuscript does not define atomic configuration publication, route-version semantics or a state-transfer-plus-SLO commit protocol. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-04181:end -->

**旧方案与约束变化。** `Ch56 already evolves replica-level scaling toward stage and operator-DAG elasticity and requires profile, topology, state and failure-aware scheduling.`（`books/part-05-inference-system/56-inference-scheduling.md#L229`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A full model replica is not the only elastic unit. A controller can choose replication counts for consecutive Transformer layer segments; the scheduler scatters sub-batches across those replicas, gathers boundary activations and redistributes affected KV partitions during a configuration transition. This reduces whole-instance startup pressure on the evaluated topology but turns activation boundaries, KV ownership and transition coordination into correctness-critical scheduling state. The v1 manuscript does not define atomic configuration publication, route-version semantics or a state-transfer-plus-SLO commit protocol. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.04181v1#S3.SS1 through #S3.SS1.p4.1 :: feasible layer-replication configuration, request scatter/gather across consecutive layer segments and partitioned KV redistribution during configuration transition; https://arxiv.org/html/2607.04181v1#S3.SS2.p1.1 through #S3.SS2.p3.1 :: bidirectional chunked ring multicast for weights and fine-grained KV transfer overlapped with inter-token intervals; https://arxiv.org/html/2607.04181v1#S4.E1 through #S4.E10 and #S4.SS4 :: configuration search and migration cost model`；Evaluation：`https://arxiv.org/html/2607.04181v1#S4.SS1 and #S6.SS1 through #S6.SS3 :: Nano-vLLM-based prototype on four NVLink-connected H20 GPUs, Qwen3 8B/14B/32B, Alibaba/Azure trace replays and LongBench prompts; compares static vLLM and a threshold autoscaler using average/P99 latency and SLO attainment`；Limitations/Counterevidence：`https://arxiv.org/html/2607.04181v1#S4.SS2 and #S6.SS3 :: analytical ranking assumes homogeneous devices and divisible layer placements; no PCIe/Ethernet fabric, heterogeneous failure recovery, arbitrary graph, public artifact or production-fleet validation`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-SCHEDULING` 的 [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [HiFA4: Training-Free 4-bit FlashAttention on Ascend HIF4 NPUs for LLM Inference](https://arxiv.org/html/2607.04302v1)

**系统推理。** 问题是 4-bit attention 若只量化 Q/K/V，重排后的概率矩阵与 kernel 路径仍可能吞掉收益。HiFA4 联合 Q/K 变换和 quantized-P 重排以适配 Ascend 执行；作者只在 HIF4 NPU、指定模型和精度下证明效果，且最终输出不是数学精确等价。代价是硬件绑定、误差校准和专用 kernel。


<!-- claim:SF-2026-ARXIV-2607-04302:start -->Attention quantization should first diagnose asymmetric Q/K structure. When calibration confirms the K-outlier regime, a paired diagonal transform can scale Q and inversely scale K while preserving the unquantized attention score; a quantized-P reordering can then make the softmax numerator and denominator consume the same quantized tensor. The equality does not preserve the final quantized output, and the reordering removes one coherent error component rather than proving all Q/K/V error harmless. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-04302:end -->

**旧方案与约束变化。** `Ch49 already explains that lower bit width does not automatically accelerate attention and that distribution handling, calibration, fusion and runtime execution must be co-designed.`（`books/part-05-inference-system/49-tensorrt-llm.md#L263`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Attention quantization should first diagnose asymmetric Q/K structure. When calibration confirms the K-outlier regime, a paired diagonal transform can scale Q and inversely scale K while preserving the unquantized attention score; a quantized-P reordering can then make the softmax numerator and denominator consume the same quantized tensor. The equality does not preserve the final quantized output, and the reordering removes one coherent error component rather than proving all Q/K/V error harmless. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.04302v1#S4.SS1 through #S4.SS4 and #S4.E1 through #S4.E3 :: diagnose parameter-induced K-channel outliers after QK-RMSNorm, apply diagonal post-RoPE Q scaling with inverse K scaling, and gate static calibration; https://arxiv.org/html/2607.04302v1#S4.SS5 and #Thmtheorem1 :: reorder quantized P so numerator and denominator share the same tensor, fuse normalization into PV, and delimit the coherent-error result to fixed V`；Evaluation：`https://arxiv.org/html/2607.04302v1#S5, #S5.SS4 and #S6.T7 :: zero-shot option-likelihood and attention-error diagnostics across Qwen3-8B, Gemma2-9B, Llama3.1-8B, Mistral-7B and Phi-4B plus one Qwen3 long-context retrieval case; https://arxiv.org/html/2607.04302v1#A2.SS0.SSS0.Px1 through #A2.SS0.SSS0.Px7 :: scoring, prompt, dtype, calibration, hook, software/hardware and determinism settings`；Limitations/Counterevidence：`https://arxiv.org/html/2607.04302v1#S7.SS0.SSS0.Px3 and #Thmtheorem1 :: all latency numbers are theoretical instruction-scheduling estimates, target hardware was not available for direct validation, and the theorem holds V fixed; applicability also depends on the calibrated outlier regime, while gate thresholds are tested on five models only and the promised implementation artifact is absent`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-TENSORRT-LLM` 的 [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture](https://arxiv.org/html/2607.04391v1)

**系统推理。** 问题是 Agent memory 的多种视图若直接相互覆盖，会失去来源与可撤销性。MOSS 保留 immutable corpus，把摘要、索引和任务记忆作为可重建 derived views；作者原型支持这种组织方式，未证明生产并发、删除与隐私语义。代价是派生链 provenance、重建成本和一致性，强化而不改变现有 memory owner。


<!-- claim:SF-2026-ARXIV-2607-04391:start -->The immutable source corpus remains evidence truth while relational metadata, semantic overlays and query profiles are revisable derived views. This is a concrete operational instance of the existing archive-versus-derived-memory contract, not a new canonical mechanism. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-04391:end -->

**旧方案与约束变化。** `Ch77 already separates compact control state from exact evidence archive and requires provenance, authorization, correction and auditability; Ch76 owns retrieval and Ch78 owns tool execution.`（`books/part-07-agent/77-memory.md#L1`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The immutable source corpus remains evidence truth while relational metadata, semantic overlays and query profiles are revisable derived views. This is a concrete operational instance of the existing archive-versus-derived-memory contract, not a new canonical mechanism. 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.04391v1#S3.SS1 through #S3.SS6 :: preserve immutable source evidence, build revisable relational metadata and semantic overlays, profile queries before deterministic SQL retrieval, and log retrieval/reformulation lifecycle`；Evaluation：`https://arxiv.org/html/2607.04391v1#S4 and #S4.SS4 :: experience report for one long-running single-user corpus; deployment statistics establish feasibility but no controlled retrieval comparison`；Limitations/Counterevidence：`https://arxiv.org/html/2607.04391v1#S4.SS4, #S5.SS5 and #S6 :: no multi-tenant isolation, poisoning test, multimodal completeness, comparative retrieval quality, reproducible benchmark or public artifact`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Principle Reuse`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`已有覆盖`。

本次重新定位到 `AGENT-MEMORY` 的 [Ch77](../../../../books/part-07-agent/77-memory.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Elastic Gang: Per-Token Membership Change for a Hard-Barriered LLM Inference Gang Co-Scheduled with OS Processes](https://arxiv.org/html/2607.04668v1)

**系统推理。** 问题是推理 gang 的成员变化通常要在粗粒度 barrier 停机。Elastic Gang 以 generation epoch 与 membership latch 让变更落在 token 安全点；作者实验支持指定 runtime 的弹性，未证明任意 collective/故障都可无损跨越。代价是 epoch metadata、成员状态迁移和 barrier failure handling。


<!-- claim:SF-2026-ARXIV-2607-04668:start -->A generation increments a global epoch; a core joins only after parking its tenant and ACKing that epoch. Each token snapshots requested intersect current-ACKed cores into one generation-tagged participant latch, and barriers wait on the latched count rather than named cores. A core that misses the latch is outside the token, while row work stealing absorbs the missing share. Owner CAS plus idempotent teardown keeps failure paths from leaving a live gang. Scheduler owns requested membership and tenant migration; each core owns its epoch ACK; the generation latch owns the immutable per-token participant set; the inference engine owns row assignment and token commit. Control changes occur only at generation/token boundaries, while model rows and partial sums remain on the token data path. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-04668:end -->

**旧方案与约束变化。** `Ch56 already owns barrier-synchronized worker sets, scheduling-state transitions and work-conserving resource control, but does not yet distinguish requested membership from acknowledged token membership.`（`books/part-05-inference-system/56-inference-scheduling.md#L305-L335`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A generation increments a global epoch; a core joins only after parking its tenant and ACKing that epoch. Each token snapshots requested intersect current-ACKed cores into one generation-tagged participant latch, and barriers wait on the latched count rather than named cores. A core that misses the latch is outside the token, while row work stealing absorbs the missing share. Owner CAS plus idempotent teardown keeps failure paths from leaving a live gang. Scheduler owns requested membership and tenant migration; each core owns its epoch ACK; the generation latch owns the immutable per-token participant set; the inference engine owns row assignment and token commit. Control changes occur only at generation/token boundaries, while model rows and partial sums remain on the token data path. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.04668v1#S3.SS1; https://arxiv.org/html/2607.04668v1#S3.SS2; https://arxiv.org/html/2607.04668v1#S3.SS3; https://arxiv.org/html/2607.04668v1#S3.SS4; https://arxiv.org/html/2607.04668v1#S3.SS5; https://arxiv.org/html/2607.04668v1#S3.SS6 — gang state, ACK-latched epoch, generation-tagged participant latch, lend/migrate/return, ownership and invariants; https://arxiv.org/html/2607.04668v1#S4.SS1; https://arxiv.org/html/2607.04668v1#S4.SS2; https://arxiv.org/html/2607.04668v1#S4.SS3 — kernel integration, row partition/work stealing and syscall/control path`；Evaluation：`https://arxiv.org/html/2607.04668v1#S5.SS1; https://arxiv.org/html/2607.04668v1#S5.SS2; https://arxiv.org/html/2607.04668v1#S5.SS3; https://arxiv.org/html/2607.04668v1#S5.SS4; https://arxiv.org/html/2607.04668v1#S5.SS5; https://arxiv.org/html/2607.04668v1#S5.SS6; https://arxiv.org/html/2607.04668v1#S5.SS7; https://arxiv.org/html/2607.04668v1#S5.SS8 — hardware/model contract, static-policy ablation, saturation knee, bit-exact churn, latency/migration and governance sweeps`；Limitations/Counterevidence：`https://arxiv.org/html/2607.04668v1#S7 — one Zen 5 host, SMT confound, directional Linux comparison, pinned-process worst case and limited governance scope`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-SCHEDULING` 的 [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Multi-Turn On-Policy Distillation with Prefix Replay](https://arxiv.org/html/2607.04763v1)

**系统推理。** 问题是 on-policy distillation 的多轮训练会丢失旧前缀分布，使新策略只适配最近 rollout。方法以 prefix replay 保留历史条件并重新采样后续，改变训练数据的来源与版本；作者实验支持其任务中的稳定性，未证明 replay 不引入陈旧偏差。代价是存储、采样权重和 policy-version mismatch。


<!-- claim:SF-2026-ARXIV-2607-04763:start -->The teacher's recorded multi-turn history and observations are replayed as a prefix; the student generates the action only at the supervised step, and the teacher supplies dense conditional token targets at that student action. A step-decaying prefix sampler reduces exposure to late histories where teacher-forced state and student occupancy diverge. This trades live environment interaction for a reliability-aware replay distribution. The trajectory store owns immutable teacher prefix/observation provenance; the sampler owns which step becomes supervision; the student owns the current action distribution; the teacher owns the conditional target; no environment side effect is executed during student training. Replay freshness and environment version remain external debts. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-04763:end -->

**旧方案与约束变化。** `Ch29 already contains the full prefix-replay evolution chain, the two-sided distribution-shift debt, the teacher/environment provenance boundary and the conditions under which live OPD or ordinary offline SFT remains preferable.`（`books/part-04-training-system/29-sft.md#L255-L281`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The teacher's recorded multi-turn history and observations are replayed as a prefix; the student generates the action only at the supervised step, and the teacher supplies dense conditional token targets at that student action. A step-decaying prefix sampler reduces exposure to late histories where teacher-forced state and student occupancy diverge. This trades live environment interaction for a reliability-aware replay distribution. The trajectory store owns immutable teacher prefix/observation provenance; the sampler owns which step becomes supervision; the student owns the current action distribution; the teacher owns the conditional target; no environment side effect is executed during student training. Replay freshness and environment version remain external debts. 它改变 `TRAIN-SFT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.04763v1#S3 — two-sided distribution shift and prefix trap; https://arxiv.org/html/2607.04763v1#S4 — replayed teacher prefixes, student action at selected step, teacher token-distribution target and step-decaying sampling`；Evaluation：`https://arxiv.org/html/2607.04763v1#S5 and subsections — math/search environments, model pairs, training parity, schedule ablations and multi-environment pool`；Limitations/Counterevidence：`https://arxiv.org/html/2607.04763v1#S6 — pool coverage, teacher reliability and future mixed-environment/generalization limits`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L506-L544`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Alternative Branch`。
- Stable owner：`TRAIN-SFT`。
- Books disposition：`已有覆盖`。

本次重新定位到 `TRAIN-SFT` 的 [Ch29](../../../../books/part-04-training-system/29-sft.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses](https://arxiv.org/html/2607.05029v1)

**系统推理。** 问题是 Agent memory 可被伪造推理链注入，普通内容过滤无法识别“看似合理的来源”。论文构造 forged-memory attack 并要求读取时验证 provenance、authority 与因果依赖；实验只证明所测攻击/防御组合，不能给出通用安全保证。代价是签名、审计、冲突处理与拒绝可用性。


<!-- claim:SF-2026-ARXIV-2607-05029:start -->The v1 demonstrates forged-reasoning entries that persist through agent memory, amplify through repeated retrieval/consensus, and can evade or defeat tested defenses; SENTINEL reduces attacks in the author experiments but remains vulnerable to adaptive paraphrase and is not a complete memory-security proof. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-05029:end -->

**旧方案与约束变化。** `Ch72 already protects Agent instruction/config/memory and Ch77 already rejects provenance-correlated majority as independent evidence; neither explicitly freezes remembered completion claims below authoritative effect receipts.`（`books/part-06-ai-infrastructure/72-security.md#L416-L435`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** An attacker writes persistent memory entries that imitate a trusted reasoning trace and claim a safety check or prerequisite was already completed. Repetition creates correlated descendants, so majority/consensus logic may count one forged origin as apparently repeated support. SENTINEL layers lexical, provenance/taint, risk-pattern and reasoning checks, but its own ablation makes the Reasoning Guard load-bearing and the limitations show adaptive paraphrase can evade it. Project inference for the durable system contract: the memory store owns untrusted persisted claims and provenance; a security policy owns taint/risk routing; only the authoritative tool/environment/effect receipt can own whether an action actually completed. Read-time voting should collapse descendants sharing one provenance family before counting evidence. 它改变 `PLATFORM-SECURITY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.05029v1#S2 — agent/memory threat model; https://arxiv.org/html/2607.05029v1#S3.SS1; https://arxiv.org/html/2607.05029v1#S3.SS2; https://arxiv.org/html/2607.05029v1#S3.SS3 — forged reasoning injection and amplification; https://arxiv.org/html/2607.05029v1#S4.SS1; https://arxiv.org/html/2607.05029v1#S4.SS2; https://arxiv.org/html/2607.05029v1#S4.SS3; https://arxiv.org/html/2607.05029v1#S4.SS4; https://arxiv.org/html/2607.05029v1#S4.SS5; https://arxiv.org/html/2607.05029v1#S4.SS6 — layered SENTINEL design and weighted Reasoning Guard`；Evaluation：`https://arxiv.org/html/2607.05029v1#S5.SS1; https://arxiv.org/html/2607.05029v1#S5.SS2; https://arxiv.org/html/2607.05029v1#S5.SS3; https://arxiv.org/html/2607.05029v1#S5.SS4; https://arxiv.org/html/2607.05029v1#S5.SS5 — EHRAgent/ReAct-QA/RAP, three model families, 50 trials per cell, amplification and defense ablation`；Limitations/Counterevidence：`https://arxiv.org/html/2607.05029v1#S6 — adaptive paraphrase bypass, single-agent/single-store scope, simulated environments and absent real EHR/production validation`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-SECURITY`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `PLATFORM-SECURITY` 的 [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [KVpop -- Key-Value Cache Compression with Predictive Online Pruning](https://arxiv.org/html/2607.05061v1)

**系统推理。** 问题是 KV eviction 用当前 attention 打分会忽略 token 的未来价值。KVpop 训练预测器估计 future attention 并在线剪枝；作者在所测模型/任务上证明其保留策略收益，未证明跨域与长程漂移稳定。代价是预测器执行、训练数据偏差和错误不可恢复；不确定时需保留 exact fallback。


<!-- claim:SF-2026-ARXIV-2607-05061:start -->Future attention mass after a protected window becomes the retention target. A boundary-focused loss trains a lightweight stateless or recurrent scorer; scoring may be delayed until the eviction boundary to expose near-future context. Runtime retains a fixed top-k budget per head, separating learned importance prediction from regular memory allocation. The target-construction path uses future attention only during training; the online scorer owns a per-token priority estimate; the cache manager owns the hard capacity and top-k commit; the model's true future attention is unavailable at eviction time. Delayed scoring trades memory residency for a better observation window. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-05061:end -->

**旧方案与约束变化。** `Ch45 already contains the oracle-to-learned-eviction evolution, future-access target, stateful/stateless scorer, delayed-scoring trade-off, fixed-budget runtime boundary and KVpop evidence limits.`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L306-L359`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Future attention mass after a protected window becomes the retention target. A boundary-focused loss trains a lightweight stateless or recurrent scorer; scoring may be delayed until the eviction boundary to expose near-future context. Runtime retains a fixed top-k budget per head, separating learned importance prediction from regular memory allocation. The target-construction path uses future attention only during training; the online scorer owns a per-token priority estimate; the cache manager owns the hard capacity and top-k commit; the model's true future attention is unavailable at eviction time. Delayed scoring trades memory residency for a better observation window. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.05061v1#S3.SS1; https://arxiv.org/html/2607.05061v1#S3.SS2; https://arxiv.org/html/2607.05061v1#S3.SS3 — future-attention supervision, sparse target construction, stateless/stateful scorers and delayed scoring; https://arxiv.org/html/2607.05061v1#A1; https://arxiv.org/html/2607.05061v1#A2; https://arxiv.org/html/2607.05061v1#A3; https://arxiv.org/html/2607.05061v1#A3.SS1; https://arxiv.org/html/2607.05061v1#A3.SS2; https://arxiv.org/html/2607.05061v1#A3.SS3 — boundary loss, running top-k, scorer implementations and pseudocode`；Evaluation：`https://arxiv.org/html/2607.05061v1#S4.SS1; https://arxiv.org/html/2607.05061v1#S4.SS2; https://arxiv.org/html/2607.05061v1#S4.SS3 — Qwen3 setup, quality results, delayed-scoring and eviction analyses; https://arxiv.org/html/2607.05061v1#A4; https://arxiv.org/html/2607.05061v1#A5 — extended experimental details and sensitivity`；Limitations/Counterevidence：`https://arxiv.org/html/2607.05061v1#S5 — dense-attention retrofit scope, limited scorer families, homogeneous per-head budget and future hybrid directions`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L593-L607`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`已有覆盖`。

本次重新定位到 `INFER-KV-CACHE` 的 [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation](https://arxiv.org/html/2607.05147v1)

**系统推理。** 问题是固定 speculative schedule 不能同时适配草稿质量与输入难度。DSpark 用半自回归 drafter 生成候选，并按置信度调节验证节奏；作者结果只支持其模型与硬件组合，不能把 draft confidence 当成正确率。代价是调度器、校准漂移和拒绝后的浪费，target 始终保留 commit authority。


<!-- claim:SF-2026-ARXIV-2607-05147:start -->A semi-autoregressive drafter proposes multiple tokens with lightweight sequential dependency, while a confidence head predicts how far verification should extend. A hardware-aware scheduler maps confidence and target-device behavior into a variable verify window; the target model remains authoritative and rejected suffixes roll back. The drafter owns provisional tokens and confidence; scheduler owns proposal/verify length; target owns acceptance; runtime owns provisional KV, rollback and batch capacity. Confidence is an estimate, not the commit authority. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-05147:end -->

**旧方案与约束变化。** `Ch48 already treats verify depth as a capacity-aware policy, separates confidence from target commit authority and preserves rollback/KV/SLO boundaries using DSpark as Experimental evidence.`（`books/part-05-inference-system/48-speculative-decoding.md#L190-L230`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A semi-autoregressive drafter proposes multiple tokens with lightweight sequential dependency, while a confidence head predicts how far verification should extend. A hardware-aware scheduler maps confidence and target-device behavior into a variable verify window; the target model remains authoritative and rejected suffixes roll back. The drafter owns provisional tokens and confidence; scheduler owns proposal/verify length; target owns acceptance; runtime owns provisional KV, rollback and batch capacity. Confidence is an estimate, not the commit authority. 它改变 `INFER-SPECULATIVE-DECODING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.05147v1#S3.SS1; https://arxiv.org/html/2607.05147v1#S3.SS2; https://arxiv.org/html/2607.05147v1#S3.SS3 — semi-autoregressive drafter, confidence head, hardware-aware verify-length scheduler and training`；Evaluation：`https://arxiv.org/html/2607.05147v1#S4.SS1; https://arxiv.org/html/2607.05147v1#S4.SS2; https://arxiv.org/html/2607.05147v1#S4.SS3; https://arxiv.org/html/2607.05147v1#S5.SS1; https://arxiv.org/html/2607.05147v1#S5.SS2; https://arxiv.org/html/2607.05147v1#S5.SS3; https://arxiv.org/html/2607.05147v1#S5.SS4 — setup, quality/speed studies, component analysis and deployment observations`；Limitations/Counterevidence：`https://arxiv.org/html/2607.05147v1#S5; https://arxiv.org/html/2607.05147v1#S6; https://arxiv.org/html/2607.05147v1#S7 — model/hardware/traffic dependence, calibration drift and deployment-specific evidence`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L430-L444`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SPECULATIVE-DECODING`。
- Books disposition：`已有覆盖`。

本次重新定位到 `INFER-SPECULATIVE-DECODING` 的 [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Weak-to-Strong Generalization via Direct On-Policy Distillation](https://arxiv.org/html/2607.05394v1)

**系统推理。** 问题是把 on-policy distillation 的收益直接归因于强 teacher，会混淆 reference 约束与策略自身 rollout。Direct-OPD 使用 teacher/reference log-ratio 明确训练信号；作者实验支持其任务设置中的优化分支，未证明普遍 weak-to-strong。代价是额外 reference forward、版本一致性与 teacher bias。


<!-- claim:SF-2026-ARXIV-2607-05394:start -->Instead of imitating a weaker post-RL teacher's final policy, Direct-OPD contrasts that teacher with its own pre-RL reference. The log policy ratio becomes a dense directional reward evaluated on the stronger student's on-policy prefixes, transferring the change induced by RL rather than the weaker model's capability ceiling. Teacher/reference checkpoint identity jointly owns the policy-shift signal; the student owns sampled prefixes; token log-ratios provide dense supervision; adaptive KL owns proximity control. The method cannot create useful direction where the teacher/reference delta is irrelevant or unsupported on student states. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-05394:end -->

**旧方案与约束变化。** `Ch29 already distinguishes policy-shift transfer from final-policy imitation, preserves student-on-policy prefixes, checkpoint-pair identity, support/KL/length limits and the branch's coexistence with SFT/RL.`（`books/part-04-training-system/29-sft.md#L277-L281`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Instead of imitating a weaker post-RL teacher's final policy, Direct-OPD contrasts that teacher with its own pre-RL reference. The log policy ratio becomes a dense directional reward evaluated on the stronger student's on-policy prefixes, transferring the change induced by RL rather than the weaker model's capability ceiling. Teacher/reference checkpoint identity jointly owns the policy-shift signal; the student owns sampled prefixes; token log-ratios provide dense supervision; adaptive KL owns proximity control. The method cannot create useful direction where the teacher/reference delta is irrelevant or unsupported on student states. 它改变 `TRAIN-SFT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.05394v1#S2.SS1; https://arxiv.org/html/2607.05394v1#S2.SS2; https://arxiv.org/html/2607.05394v1#S2.SS3; https://arxiv.org/html/2607.05394v1#S2.SS4 — OPD preliminaries, teacher policy shift as implicit reward, Direct-OPD objective and adaptive KL`；Evaluation：`https://arxiv.org/html/2607.05394v1#S3.SS1; https://arxiv.org/html/2607.05394v1#S3.SS2; https://arxiv.org/html/2607.05394v1#S3.SS3 — model/task/training contract and matched baselines; https://arxiv.org/html/2607.05394v1#S4.SS1; https://arxiv.org/html/2607.05394v1#S4.SS2; https://arxiv.org/html/2607.05394v1#S4.SS3 — cross-token transfer, short-horizon effect and KL diagnostics; https://arxiv.org/html/2607.05394v1#A1; https://arxiv.org/html/2607.05394v1#A2; https://arxiv.org/html/2607.05394v1#A3 — experimental details and additional results`；Limitations/Counterevidence：`https://arxiv.org/html/2607.05394v1#S6 — dependence on meaningful teacher/reference improvement, student-visited support, response length and KL strength`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L778-L789`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Alternative Branch`。
- Stable owner：`TRAIN-SFT`。
- Books disposition：`已有覆盖`。

本次重新定位到 `TRAIN-SFT` 的 [Ch29](../../../../books/part-04-training-system/29-sft.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

所有性能数字仅在原文披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator 范围内解释；未披露字段保持 `Not Disclosed`，本次没有把作者 benchmark 写成通用生产结论。

## 5. 缺口与下一步

无

本窗没有外部材料请求或待执行工作；非作者独立语义复核已确认已有 Books 段落是机制正文，而非只有 trace。

## 6. 复核

复核者：主任务独立复核（非本报告作者）

结论：通过

独立复核逐项检查 13 个候选的窗口、exact-v1、评分、证据边界与 Books 路由，并核对 long-context、speculation、scheduling、execution、memory/security 与 SFT 正文。对 VLA 局部方法、领域 Agent、一般 verifier、训练数据复用和 survey 项分层抽检，未发现需要恢复的共同 false-negative。格式校验与 `git diff --check` 通过。
