# Daily Research — 2026-07-03

**规范：** V3
**窗口：** 2026-07-02T09:00:00+08:00 ～ 2026-07-03T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T16:30:00+08:00

## 1. 结论

本窗复用并核实 591 个去重 arXiv v1 原始身份，逐条按标题与完整摘要重新判断项目贡献；旧恢复队列 29 项中，10 个材料家族通过当前门槛，19 项因仅是领域应用、局部方法包装、通用 benchmark/Agent 组合或没有改变长期设计判断而转为 pre-denominator closure。关闭结果汇总在本报告的复核结论中，不在正文伪装成候选。

10 项均达到与评分相称的证据审阅深度，并重新检查撤回/纠错信号与首次公开 owner。旧报告标记为 `Integrate` 的机制已经出现在相应 Books 正文，本次统一改为“已有覆盖”；不重复追加，也不以 evidence trace 代替正文承载。独立复核已确认候选准入、证据边界与 body anchor 闭合。

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
| SRC-ARXIV | 复核本窗官方公告 owner、591 个去重 v1 身份及旧恢复队列；逐条标题、边界项完整摘要语义筛选后保留 10 项 | 已检查 | 无 |

本窗没有触发需要改变候选或结论的按需来源。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching](https://arxiv.org/html/2607.01299v1) | 2026-07-03T08:00:00+08:00 | For hybrid attention, reusable state is not always a list of per-token KV. A linear-attention segment may need both zero-state result and cumulative transition operator so segme…；`3+3+3=9` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [The risk of KV cache compression](https://arxiv.org/html/2607.01520v1) | 2026-07-03T08:00:00+08:00 | KV compressibility is context- and query-family-dependent rather than a fixed ratio. Response covariance gives a graded spectral risk boundary: fast decay permits sparse summari…；`3+3+3=9` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [OmniPilot: An Uncertainty-Aware LLM Inference Advisor for Heterogeneous GPU Clusters](https://arxiv.org/html/2607.01579v1) | 2026-07-03T08:00:00+08:00 | A configuration predictor should be admitted only when its expected decision value exceeds benchmark cost and should abstain outside calibrated cells. The scheduling chapter alr…；`2+2+2=6` | 标准完成 | 已有覆盖：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving](https://arxiv.org/html/2607.01617v1) | 2026-07-03T08:00:00+08:00 | When PD KV transfer and decode collectives share a fabric, software scheduling cannot eliminate head-of-line interference. Mapping the two traffic classes to physically distinct…；`3+3+2=8` | 深入完成 | 已有覆盖：`INFER-PD-DISAGGREGATION`，[Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [PHOENIX: Resilient LLM Training with Hot-Swapping via Zero-Overhead Checkpoint](https://arxiv.org/html/2607.01646v1) | 2026-07-03T08:00:00+08:00 | Persistent checkpoint-restart is not the only recovery branch. For frequent fail-stop node loss, the runtime can continuously maintain a committed in-memory recovery generation,…；`3+3+3=9` | 深入完成 | 已有覆盖：`TRAIN-CHECKPOINT`，[Ch35](../../../../books/part-04-training-system/35-checkpoint.md) |
| [SCAPE: Accurate and Efficient LLM Training with Extreme Sparse Communication](https://arxiv.org/html/2607.01678v1) | 2026-07-03T08:00:00+08:00 | Communication reduction can move from quantizing every dense value to transmitting a sparse optimizer-defined support. Reusing a temporally stable first-moment mask one step lat…；`3+3+2=8` | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Lynx: Progressive Speculative Quantization for accelerating KV Transfer in Long-Context Inference](https://arxiv.org/html/2607.01831v1) | 2026-07-03T08:00:00+08:00 | A PD handoff need not wait for the last exact KV byte before doing any work. A progressive protocol can transmit an approximate low-bit view first, execute speculatively, then v…；`3+3+2=8` | 深入完成 | 已有覆盖：`INFER-PD-DISAGGREGATION`，[Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [Towards Load-Aware Prefill Deflection for Disaggregated LLM Serving](https://arxiv.org/html/2607.02043v1) | 2026-07-03T08:00:00+08:00 | Static PD role boundaries can waste decode headroom while prefill queues violate TTFT. A controller may deflect chunked prefill onto decode workers only when a calibrated per-st…；`3+3+3=9` | 深入完成 | 已有覆盖：`INFER-PD-DISAGGREGATION`，[Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments](https://arxiv.org/html/2607.02440v1) | 2026-07-03T08:00:00+08:00 | Iterative agent-policy evaluation must version the environment, policy, feedback visibility and held-out boundary; local wins and post-hoc trajectories do not establish suite-wi…；`2+2+3=7` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [WorldDirector: Building Controllable World Simulators with Persistent Dynamic Memory](https://arxiv.org/html/2607.02517v1) | 2026-07-03T08:00:00+08:00 | Separating planned object state, appearance identity and chunk-local synthesis helps an object leave and re-enter view without relying on implicit video context alone. The World…；`2+2+3=7` | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |

## 4. 证据与知识整合

### [HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching](https://arxiv.org/html/2607.01299v1)

**系统推理。** 问题是 hybrid attention 中 recurrent state 不能像普通 KV 那样直接拼接复用。方法把线性层的 segment transition 组合、全注意力层的 seam window 修复和冷 Prefill 并行结合，改变可缓存状态的表示与合成规则；作者在 Qwen3.5-35B-A3B/H20 的指定负载上证明可行，未证明所有 recurrent 架构都能无损组合。代价是 seam 近似、segment 依赖与专用实现，短前缀或结构不匹配时普通 Prefill 仍适用。


<!-- claim:SF-2026-ARXIV-2607-01299:start -->For hybrid attention, reusable state is not always a list of per-token KV. A linear-attention segment may need both zero-state result and cumulative transition operator so segments compose in order; sparse full-attention layers then need bounded seam repair. This enables position-independent reuse but adds operator identity, numerical drift, seam policy, composition order and fallback semantics. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01299:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** For hybrid attention, reusable state is not always a list of per-token KV. A linear-attention segment may need both zero-state result and cumulative transition operator so segments compose in order; sparse full-attention layers then need bounded seam repair. This enables position-independent reuse but adds operator identity, numerical drift, seam policy, composition order and fallback semantics. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01299v1#S4 :: cached segment transition composition for recurrent linear-attention state, seam-window repair for full-attention layers and segment-parallel cold prefill; https://arxiv.org/html/2607.01299v1#S5 :: SGLang/FLA implementation path`；Evaluation：`https://arxiv.org/html/2607.01299v1#S6 :: author evaluation binds Qwen3.5-35B-A3B, one H20 node, disclosed datasets, prefix patterns and baselines; no production arrival/concurrency or independent replication is claimed`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01299v1#S3 :: ordinary KV splice cannot compose recurrent state, hidden-state suppression blocks old repair primitives, and seam approximation remains architecture/segment dependent; no separate limitations section is present`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-KV-CACHE` 的 [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [The risk of KV cache compression](https://arxiv.org/html/2607.01520v1)

**系统推理。** 问题是 KV compression 的平均精度指标会隐藏特定上下文上的灾难性语义损失。论文从谱结构和上下文条件解释风险，要求压缩策略带质量估计与 abstain/fallback；实验说明某些压缩在所测任务上风险高度不均，但不提供跨模型安全阈值。代价是风险探测、校准和保守回退带来的容量损失，收益是把“压缩率”改写为有条件的服务承诺。


<!-- claim:SF-2026-ARXIV-2607-01520:start -->KV compressibility is context- and query-family-dependent rather than a fixed ratio. Response covariance gives a graded spectral risk boundary: fast decay permits sparse summaries, while lookup-like or flat-tail contexts impose a near-full-cache lower bound. The theorem does not predict final semantics or remove runtime validation, but it explains when compression should abstain and why FullKV remains necessary. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01520:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** KV compressibility is context- and query-family-dependent rather than a fixed ratio. Response covariance gives a graded spectral risk boundary: fast decay permits sparse summaries, while lookup-like or flat-tail contexts impose a near-full-cache lower bound. The theorem does not predict final semantics or remove runtime validation, but it explains when compression should abstain and why FullKV remains necessary. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01520v1#S3 :: KV compression as sparse approximation of a context measure and response-covariance compressibility; https://arxiv.org/html/2607.01520v1#S4 :: query-aware/agnostic minimax upper and lower bounds; https://arxiv.org/html/2607.01520v1#S5 :: causal merge-reduce algorithms`；Evaluation：`https://arxiv.org/html/2607.01520v1#S6 and https://arxiv.org/html/2607.01520v1#A4 :: focused LongBench-v2 experiments on Qwen3-32B, single NVIDIA H100, stated budgets/baselines and one fixed seed for randomized methods`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01520v1#S4.SS3 :: spectral lower bounds show lookup-like contexts can require nearly full support; practical experiments are targeted, single-GPU/single-seed and do not establish semantic quality or production SLO generally`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-KV-CACHE` 的 [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [OmniPilot: An Uncertainty-Aware LLM Inference Advisor for Heterogeneous GPU Clusters](https://arxiv.org/html/2607.01579v1)

**系统推理。** 问题是异构 GPU 上仅按静态 profile 选执行配置会在负载变化时失准。方法以校准单元、在线不确定度和越界 abstain 约束 advisor 的决策权；作者结果只支持其硬件与配置网格内的推荐质量，不证明未观测区域可泛化。代价是持续 calibration、模型漂移监测和安全 fallback；已有 scheduling owner 已能承载。


<!-- claim:SF-2026-ARXIV-2607-01579:start -->A configuration predictor should be admitted only when its expected decision value exceeds benchmark cost and should abstain outside calibrated cells. The scheduling chapter already makes calibration identity, uncertainty, targeted silicon validation and rollback explicit, so this family strengthens that route without changing its owner. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01579:end -->

**旧方案与约束变化。** `Configuration search uses versioned primitive measurements and uncertainty-aware prediction only to narrow candidates; launch authority remains with targeted silicon validation, canary and rollback when calibration drifts or candidates are near-tied.`（`books/part-05-inference-system/56-inference-scheduling.md#L248-L301`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A configuration predictor should be admitted only when its expected decision value exceeds benchmark cost and should abstain outside calibrated cells. The scheduling chapter already makes calibration identity, uncertainty, targeted silicon validation and rollback explicit, so this family strengthens that route without changing its owner. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01579v1#method :: versioned feature extraction, inference-cost prediction and a value-of-information benchmark gate for launch placement`；Evaluation：`https://arxiv.org/html/2607.01579v1#evaluation :: author evaluation covers held-out cluster cells, placement accuracy, calibration, OOD abstention and ablations; no production scheduler trial is claimed`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01579v1#threats-to-validity and https://arxiv.org/html/2607.01579v1#scope-and-future-work :: synthetic/collected launch data, site-specific features, stale telemetry and limited OOD coverage constrain external validity`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：`已有覆盖`。

本次重新定位到 `INFER-SCHEDULING` 的 [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving](https://arxiv.org/html/2607.01617v1)

**系统推理。** 问题是 PD 分离后，KV transfer 与 decode collective 竞争同一网络会相互放大尾延迟。3D logic-stacked 设计把两类流量在物理路径与调度域上分开，重新分配通信 ownership；作者模拟/实验支持其指定拓扑下的隔离收益，不能证明所有集群都值得专用堆叠。代价是硬件/拓扑绑定、容量碎片和失效恢复复杂度，普通共享网络在规模较小时仍合理。


<!-- claim:SF-2026-ARXIV-2607-01617:start -->When PD KV transfer and decode collectives share a fabric, software scheduling cannot eliminate head-of-line interference. Mapping the two traffic classes to physically distinct link domains can protect the handoff critical path, but it spends packaging area, thermal/yield budget and topology flexibility; it remains an architecture-specific branch rather than a default PD requirement. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01617:end -->

**旧方案与约束变化。** `本章的核心判断是：**PD 分离利用 Prefill 与 Decode 在计算、memory、batch 和 SLO 上的差异实现独立资源规划，但必须用 KV transfer、跨池排队和更大故障面支付代价；它是否成立取决于 workload-specific break-even。**`（`books/part-05-inference-system/55-pd-disaggregation.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** When PD KV transfer and decode collectives share a fabric, software scheduling cannot eliminate head-of-line interference. Mapping the two traffic classes to physically distinct link domains can protect the handoff critical path, but it spends packaging area, thermal/yield budget and topology flexibility; it remains an architecture-specific branch rather than a default PD requirement. 它改变 `INFER-PD-DISAGGREGATION` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01617v1#S3 :: 3D logic-stacked serving architecture separates vertical KV-transfer traffic from lateral tensor-parallel collectives`；Evaluation：`https://arxiv.org/html/2607.01617v1#S4 :: in-house simulator studies Llama-3 8B/70B and OPT-175B under disclosed serving traces and iso-bandwidth comparisons; no fabricated chip or production deployment is evaluated`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01617v1#S3 :: package area, vertical-link bandwidth, thermals and yield constrain the architecture; https://arxiv.org/html/2607.01617v1#S4 :: results depend on the in-house simulator, modeled workloads and iso-bandwidth comparison. Queueing and KV ownership are explicit system non-proof boundaries, not claims attributed to the authors`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Alternative Branch`。
- Stable owner：`INFER-PD-DISAGGREGATION`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-PD-DISAGGREGATION` 的 [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [PHOENIX: Resilient LLM Training with Hot-Swapping via Zero-Overhead Checkpoint](https://arxiv.org/html/2607.01646v1)

**系统推理。** 问题是大模型训练故障恢复通常从持久 checkpoint 重启，恢复时间与 checkpoint 周期相互牵制。PHOENIX 将已提交状态的恢复 generation 保存在内存池，并用逻辑 shard identity 支持 hot-swap；作者结果证明其设置中的快速恢复路径，但不替代灾难恢复，也不证明跨故障域持久性。代价是备用内存、generation/commit 一致性和池本身的故障域。


<!-- claim:SF-2026-ARXIV-2607-01646:start -->Persistent checkpoint-restart is not the only recovery branch. For frequent fail-stop node loss, the runtime can continuously maintain a committed in-memory recovery generation, replicate only non-reconstructible optimizer shards, and replace a failed node by logical shard identity. This reduces replay and restart scope but depends on spare nodes, failure classification and explicit fallback for corruption or replica loss. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01646:end -->

**旧方案与约束变化。** `本章的核心判断是：**Training Checkpoint 是训练状态在某个逻辑 step 上的一致、可验证、可恢复事务，而不是若干 tensor 文件的集合。**它必须同时描述参数、优化器、随机性、数据进度、并行布局和配置；缺少任一关键状态，都可能让“恢复成功”只剩进程启动成功。`（`books/part-04-training-system/35-checkpoint.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Persistent checkpoint-restart is not the only recovery branch. For frequent fail-stop node loss, the runtime can continuously maintain a committed in-memory recovery generation, replicate only non-reconstructible optimizer shards, and replace a failed node by logical shard identity. This reduces replay and restart scope but depends on spare nodes, failure classification and explicit fallback for corruption or replica loss. 它改变 `TRAIN-CHECKPOINT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01646v1#S5 and https://arxiv.org/html/2607.01646v1#S6 :: per-step ping-pong host snapshots, peer replication of optimizer shards, failure classification, topology repair and logical-shard restoration`；Evaluation：`https://arxiv.org/html/2607.01646v1#S7 :: injected fail-stop/NCCL/storage faults on Perlmutter and Vista, up to 512 A100 or 64 GH200 GPUs and GPT-style models up to 65B; observed overlap and recovery are platform-bound`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01646v1#S5.SS3 and https://arxiv.org/html/2607.01646v1#S8 :: silent corruption/software bugs remain external fallback; redundancy, failure-domain independence, spare capacity, host/network headroom and two-system coverage limit generalization`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`TRAIN-CHECKPOINT`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `TRAIN-CHECKPOINT` 的 [Ch35](../../../../books/part-04-training-system/35-checkpoint.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [SCAPE: Accurate and Efficient LLM Training with Extreme Sparse Communication](https://arxiv.org/html/2607.01678v1)

**系统推理。** 问题是极稀疏通信若只在通信层剪枝，可能破坏优化器真正需要的更新支持集。SCAPE 让 optimizer 定义 sparse support 与 mask state，再由 runtime 执行通信；作者在指定训练任务中证明精度—通信折中，但不证明同一稀疏率适合所有模型。代价是 mask 生命周期、残差状态、负载不均与恢复一致性；密集 collective 在小规模或高变化阶段仍更稳健。


<!-- claim:SF-2026-ARXIV-2607-01678:start -->Communication reduction can move from quantizing every dense value to transmitting a sparse optimizer-defined support. Reusing a temporally stable first-moment mask one step later exposes synchronization overlap and avoids a second collective, but makes optimizer semantics, residual state, mask freshness and sparse representation part of the training contract. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01678:end -->

**旧方案与约束变化。** `本章的核心判断是：**分布式训练是在保持训练语义不变量的前提下，把计算、模型状态、activation 与通信映射到设备拓扑的约束优化。**每种并行只直接缓解某类瓶颈，并把一部分本地 memory/compute 问题转化成 collective、pipeline、同步或恢复问题。通信也不能被压缩成一个库名：必须分清语义、算法、runtime、transport 与物理拓扑。`（`books/part-04-training-system/36-distributed-training.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Communication reduction can move from quantizing every dense value to transmitting a sparse optimizer-defined support. Reusing a temporally stable first-moment mask one step later exposes synchronization overlap and avoids a second collective, but makes optimizer semantics, residual state, mask freshness and sparse representation part of the training contract. 它改变 `TRAIN-DISTRIBUTED-TRAINING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01678v1#S4 :: optimizer-aware first-moment masks, one-step-delayed refreshed synchronization, sharding-aligned mask ownership and reconstruction from one sparse synchronized buffer`；Evaluation：`https://arxiv.org/html/2607.01678v1#S5 :: GPT-345M/OpenWebText and Llama-500M/SlimPajama full pretraining uses 32 GH200 GPUs; Llama-500M and Llama-1.8B per-step profiling and strong-scaling studies span 4–64 GH200 GPUs, with disclosed sparsity, loss/tasks and timing measurements`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01678v1#S3 and https://arxiv.org/html/2607.01678v1#S4 :: mask stability and delayed reuse are empirical/optimizer-specific; https://arxiv.org/html/2607.01678v1#S5 :: evaluation is limited to the disclosed AdamS models and GH200 setup, while the paper notes PCIe offload may add overhead on other clusters; no dedicated limitations section establishes broader convergence`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-DISTRIBUTED-TRAINING`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `TRAIN-DISTRIBUTED-TRAINING` 的 [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Lynx: Progressive Speculative Quantization for accelerating KV Transfer in Long-Context Inference](https://arxiv.org/html/2607.01831v1)

**系统推理。** 问题是 PD 解耦中的 KV 传输常把压缩近似一次性提交，质量失败后没有渐进修正。Lynx 先传近似状态启动执行，再逐步验证/补全，改变 transfer 与 consumer 的 commit 顺序；作者结果支持其网络与模型下的重叠收益，未证明近似前缀在所有请求上安全。代价是版本化片段、验证开销、回滚和错误窗口，低延迟网络下直接精确传输仍可能更好。


<!-- claim:SF-2026-ARXIV-2607-01831:start -->A PD handoff need not wait for the last exact KV byte before doing any work. A progressive protocol can transmit an approximate low-bit view first, execute speculatively, then verify and correct against later refinements. It converts transfer latency into provisional computation, but requires generation identity, verification authority, rollback/correction and an exact commit frontier. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01831:end -->

**旧方案与约束变化。** `本章的核心判断是：**PD 分离利用 Prefill 与 Decode 在计算、memory、batch 和 SLO 上的差异实现独立资源规划，但必须用 KV transfer、跨池排队和更大故障面支付代价；它是否成立取决于 workload-specific break-even。**`（`books/part-05-inference-system/55-pd-disaggregation.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A PD handoff need not wait for the last exact KV byte before doing any work. A progressive protocol can transmit an approximate low-bit view first, execute speculatively, then verify and correct against later refinements. It converts transfer latency into provisional computation, but requires generation identity, verification authority, rollback/correction and an exact commit frontier. 它改变 `INFER-PD-DISAGGREGATION` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01831v1#S4 :: hierarchical KV quantization, prioritized low-bit-first transfer, speculative execution and verify/correct before exact commitment`；Evaluation：`https://arxiv.org/html/2607.01831v1#S6 :: author tests accuracy and latency on disclosed long-context models/tasks and Ascend-oriented LMCache/vLLM integration; production concurrency and independent replication are absent`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01831v1#S2 :: ordinary complete-transfer and linear-quantization bottlenecks motivate the design; https://arxiv.org/html/2607.01831v1#S4 :: hierarchical approximation plus verification/correction add provisional-state work; https://arxiv.org/html/2607.01831v1#S6 and https://arxiv.org/html/2607.01831v1#S8 :: benefit depends on the evaluated models/hardware and successful transfer/computation overlap. Early bytes not being committed exact state is this review's correctness boundary`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Alternative Branch`。
- Stable owner：`INFER-PD-DISAGGREGATION`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-PD-DISAGGREGATION` 的 [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Towards Load-Aware Prefill Deflection for Disaggregated LLM Serving](https://arxiv.org/html/2607.02043v1)

**系统推理。** 问题是 disaggregated serving 在 decode 繁忙时仍把 Prefill 固定送往原路径，会让负载与 TBT 风险恶化。方法只在预测 TBT slack 足够时 deflect Prefill，并保留原路径 fallback；作者在指定 trace/topology 上证明负载感知可改善目标指标，不能外推到模型漂移或突发流量。代价是 slack 预测、跨池状态迁移与错误路由，低负载时静态绑定更简单。


<!-- claim:SF-2026-ARXIV-2607-02043:start -->Static PD role boundaries can waste decode headroom while prefill queues violate TTFT. A controller may deflect chunked prefill onto decode workers only when a calibrated per-step model proves remaining TBT slack, with safety margin and fallback. This improves temporary capacity matching but couples estimation error, stale state and fairness to both SLOs. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-02043:end -->

**旧方案与约束变化。** `本章的核心判断是：**PD 分离利用 Prefill 与 Decode 在计算、memory、batch 和 SLO 上的差异实现独立资源规划，但必须用 KV transfer、跨池排队和更大故障面支付代价；它是否成立取决于 workload-specific break-even。**`（`books/part-05-inference-system/55-pd-disaggregation.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Static PD role boundaries can waste decode headroom while prefill queues violate TTFT. A controller may deflect chunked prefill onto decode workers only when a calibrated per-step model proves remaining TBT slack, with safety margin and fallback. This improves temporary capacity matching but couples estimation error, stale state and fairness to both SLOs. 它改变 `INFER-PD-DISAGGREGATION` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.02043v1#S4 :: TTFT estimator, decode-step feasibility model and greedy chunk schedule that borrows only predicted TBT slack`；Evaluation：`https://arxiv.org/html/2607.02043v1#S6 :: vLLM 0.18.1 implementation on A100 clusters with DeepSeek-v2-Lite, bursty traces and stated P95 TTFT/TBT SLOs; results are workload-specific`；Limitations/Counterevidence：`https://arxiv.org/html/2607.02043v1#S7 :: central dispatcher, stale 100-ms observations, estimator error, no migration and omitted prefix-cache interactions constrain deployment`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-PD-DISAGGREGATION`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-PD-DISAGGREGATION` 的 [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments](https://arxiv.org/html/2607.02440v1)

**系统推理。** 问题是评估 Agent 自我演进时，环境、策略、反馈和测试集若不共同版本化，提升无法归因。EvoPolicyGym 把这些对象拆成独立资产并要求 held-out promotion；作者 benchmark 只证明其任务集能暴露部分 evolution failure，不证明开放环境中的长期自治。代价是更多版本与回放成本，但换来可审计的策略升级证据。


<!-- claim:SF-2026-ARXIV-2607-02440:start -->Iterative agent-policy evaluation must version the environment, policy, feedback visibility and held-out boundary; local wins and post-hoc trajectories do not establish suite-wide reliability or causal credit. The evaluation chapter already owns these evidence limits. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-02440:end -->

**旧方案与约束变化。** `Evaluation evidence is valid only for a pinned subject, environment, evaluator and slice; iterative improvement must preserve held-out promotion boundaries and cannot infer causal credit from a convenient process score or local win.`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L724-L752`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Iterative agent-policy evaluation must version the environment, policy, feedback visibility and held-out boundary; local wins and post-hoc trajectories do not establish suite-wide reliability or causal credit. The evaluation chapter already owns these evidence limits. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.02440v1#S3 :: bounded environment-policy episodes, autonomous policy revision and explicit feedback/evaluation boundaries`；Evaluation：`https://arxiv.org/html/2607.02440v1#S4 and https://arxiv.org/html/2607.02440v1#S5 :: task-suite outcomes, post-hoc score trajectories and mechanism case studies under a fixed run protocol`；Limitations/Counterevidence：`https://arxiv.org/html/2607.02440v1#S5.SS3 :: diagnostics are post-hoc, task-family dependent and do not establish causal credit or open-ended safe self-improvement`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L673-L686`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`已有覆盖`。

本次重新定位到 `PLATFORM-EVALUATION-SYSTEM` 的 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [WorldDirector: Building Controllable World Simulators with Persistent Dynamic Memory](https://arxiv.org/html/2607.02517v1)

**系统推理。** 问题是视频 world simulator 容易把外观连续性误当作可控环境状态。WorldDirector 显式分开 object state、appearance memory 与 chunk synthesis，使控制输入能作用于持久动态；作者只在其生成任务与指标上证明可控性，未证明真实物理因果或 policy utility。代价是对象身份、跨 chunk 漂移和状态纠错，现有 World Model 章节已承载该边界。


<!-- claim:SF-2026-ARXIV-2607-02517:start -->Separating planned object state, appearance identity and chunk-local synthesis helps an object leave and re-enter view without relying on implicit video context alone. The World Model chapter already owns persistent revisable state, identity, chunk drift and the boundary between visual consistency and causal/closed-loop correctness. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-02517:end -->

**旧方案与约束变化。** `Persistent world state must preserve identity and mutation across revisit while remaining versioned, revisable and recoverable; visually consistent generation is lower-layer evidence and cannot substitute for action-conditioned or closed-loop correctness.`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L286-L320`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Separating planned object state, appearance identity and chunk-local synthesis helps an object leave and re-enter view without relying on implicit video context alone. The World Model chapter already owns persistent revisable state, identity, chunk drift and the boundary between visual consistency and causal/closed-loop correctness. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.02517v1#S3 :: trajectory planning, spatial/appearance conditioning, persistent dynamic context memory and causal chunk generation`；Evaluation：`https://arxiv.org/html/2607.02517v1#S4 :: author comparisons and ablations test identity/location persistence and promptable events in selected generated-video scenarios`；Limitations/Counterevidence：`https://arxiv.org/html/2607.02517v1#S4 and https://arxiv.org/html/2607.02517v1#S5 :: evaluation and conclusion are limited to selected synthetic/game video scenarios and acknowledge the domain gap; causal physics, unbounded horizon, closed-loop controllability and safe real-world action are explicit non-proof boundaries, while planner/projection, identity collision and chunk drift remain inferred system risks`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L701-L715`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`已有覆盖`。

本次重新定位到 `MULTIMODAL-WORLD-MODELS` 的 [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

所有性能数字仅在原文披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator 范围内解释；未披露字段保持 `Not Disclosed`，本次没有把作者 benchmark 写成通用生产结论。

## 5. 缺口与下一步

无

本窗没有外部材料请求或待执行工作；非作者独立语义复核已确认已有 Books 段落是机制正文，而非只有 trace。

## 6. 复核

复核者：主任务独立复核（非本报告作者）

结论：通过

独立复核逐项检查 10 个候选的窗口、exact-v1、三维评分、证据边界与 Books 正文 anchor；KV、训练恢复/通信、PD、Evaluation 和 World Model 的已有覆盖均可在正文定位。对 oversight、VLA 局部方法、Agent benchmark、memory testbed 与 world-model 应用项分层抽检，未发现共同筛选理由造成的系统性漏项。格式校验与 `git diff --check` 通过。
