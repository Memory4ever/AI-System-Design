# Daily Research — 2026-07-02

**规范：** V3
**窗口：** 2026-07-01T09:00:00+08:00 ～ 2026-07-02T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T16:10:00+08:00

## 1. 结论

本窗复用并核实 549 个去重 arXiv v1 原始身份，逐条按标题与完整摘要重新判断项目贡献；旧恢复队列 17 项中，8 个材料家族通过当前门槛，9 项因仅是领域应用、局部方法包装、通用 benchmark/Agent 组合或没有改变长期设计判断而转为 pre-denominator closure。关闭结果汇总在本报告的复核结论中，不在正文伪装成候选。

8 项均达到与评分相称的证据审阅深度，并重新检查撤回/纠错信号与首次公开 owner。旧报告标记为 `Integrate` 的机制已经出现在相应 Books 正文，本次统一改为“已有覆盖”；不重复追加，也不以 evidence trace 代替正文承载。独立复核已确认候选准入、证据边界与 body anchor 闭合。

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
| SRC-ARXIV | 复核本窗官方公告 owner、549 个去重 v1 身份及旧恢复队列；逐条标题、边界项完整摘要语义筛选后保留 8 项 | 已检查 | 无 |

本窗没有触发需要改变候选或结论的按需来源。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [SmoothAgent: Efficient Long-Horizon LLM-Based Agent Serving with Lookahead Context Engineering](https://arxiv.org/html/2607.00151v1) | 2026-07-02T08:00:00+08:00 | When a context rewrite is segment-decomposable, its transformed KV can be prepared as best-effort lookahead and promoted only at the semantic commit point. This removes work fro…；`3+3+2=8` | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving](https://arxiv.org/html/2607.00466v1) | 2026-07-02T08:00:00+08:00 | MoE Decode 的成本不仅由 queue length 决定，还由 batch 激活的 distinct expert working set 决定。把 prefill expert signature 与 KV block 生命周期绑定，再在 locality band 内做 load-aware routing，可以复用 expert wei…；`3+3+3=9` | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [BaseRT: Best-in-Class LLM Inference on Apple Silicon via Native Metal](https://arxiv.org/html/2607.00501v1) | 2026-07-02T08:00:00+08:00 | A hardware-native engine can remove generic framework allocation, graph and dispatch overhead through preallocated buffers, descriptor-driven architecture differences and chip-s…；`2+2+2=6` | 标准完成 | 已有覆盖：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression](https://arxiv.org/html/2607.00760v1) | 2026-07-02T08:00:00+08:00 | KV compression can jointly vary retained token count and per-token feature rank instead of treating eviction and quantization as isolated policies. This enlarges the quality-cap…；`3+3+2=8` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache](https://arxiv.org/html/2607.01065v1) | 2026-07-02T08:00:00+08:00 | At extreme vector-quantization budgets, separately modeling vector direction and scale can preserve information that ordinary Euclidean centroids conflate. This is a quantizer-d…；`2+2+2=6` | 标准完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [MemSyco-Bench: Benchmarking Sycophancy in Agent Memory](https://arxiv.org/html/2607.01071v1) | 2026-07-02T08:00:00+08:00 | Memory quality must separate retrieval success from downstream adoption: a relevant memory can be retrieved yet should be ignored, constrained, superseded or used only for perso…；`2+2+3=7` | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?](https://arxiv.org/html/2607.01211v1) | 2026-07-02T08:00:00+08:00 | Executable evaluation must validate the reference artifact before judging candidates and must expose sensitivity to machine, repetition and aggregation rules. The evaluation cha…；`2+3+3=8` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [AutoMem: Automated Learning of Memory as a Cognitive Skill](https://arxiv.org/html/2607.01224v1) | 2026-07-02T08:00:00+08:00 | Memory policy can be optimized as a versioned artifact through a held-out promotion loop, while memory-operation proficiency can be trained separately from task-action authority…；`2+2+3=7` | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |

## 4. 证据与知识整合

### [SmoothAgent: Efficient Long-Horizon LLM-Based Agent Serving with Lookahead Context Engineering](https://arxiv.org/html/2607.00151v1)

**系统推理。** 问题是长轨迹 Agent 在语义边界反复重写上下文，把本可提前的工作留在关键路径。方法把主状态与 lookahead 状态分离，只对可分段变换提前计算，并在语义 commit 点原子提升；作者实验支持其在所测 context 策略、并发和部署形态下缩短关键路径，但没有证明任意重写都可分解，也没有证明生产尾延迟。代价是双份状态、freshness/cancel 语义和调度模型漂移；slack 消失时必须回退同步路径。


<!-- claim:SF-2026-ARXIV-2607-00151:start -->When a context rewrite is segment-decomposable, its transformed KV can be prepared as best-effort lookahead and promoted only at the semantic commit point. This removes work from the critical path without changing context policy, but requires separate main/lookahead state, freshness and cancellation semantics, latency-aware admission and synchronous fallback when slack disappears. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-00151:end -->

**旧方案与约束变化。** `本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**`（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** When a context rewrite is segment-decomposable, its transformed KV can be prepared as best-effort lookahead and promoted only at the semantic commit point. This removes work from the critical path without changing context policy, but requires separate main/lookahead state, freshness and cancellation semantics, latency-aware admission and synchronous fallback when slack disappears. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.00151v1#S3 :: segment-decomposable context transforms, separate lookahead state and atomic promotion/commit; https://arxiv.org/html/2607.00151v1#S4 :: latency-critical versus best-effort scheduling under TTFT/TBT slack`；Evaluation：`https://arxiv.org/html/2607.00151v1#S6 :: author evaluation covers several context strategies, agent frameworks, concurrency settings and co-located/disaggregated serving; no headline speedup is retained`；Limitations/Counterevidence：`https://arxiv.org/html/2607.00151v1#S3.SS2 :: non-decomposable transforms cannot be safely advanced; https://arxiv.org/html/2607.00151v1#S4 :: stale latency models or contention can violate foreground SLO, requiring synchronous fallback`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-SCHEDULING` 的 [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving](https://arxiv.org/html/2607.00466v1)

**系统推理。** 问题是 PD 分离的 MoE decode 只看队列长度会忽略实际激活的 expert working set。方法把 prefill 得到的 expert signature 绑定到 KV block 生命周期，在 locality band 内再按负载路由，从而改变 routing owner 所观察的状态；作者在指定 MoE、MI300X 集群和网络上证明该局部性可以被利用，但没有证明跨模型与流量长期稳定。代价是 signature 元数据、重聚类、负载与局部性冲突，以及 prefix/KV/worker epoch 一致性。


<!-- claim:SF-2026-ARXIV-2607-00466:start -->MoE Decode 的成本不仅由 queue length 决定，还由 batch 激活的 distinct expert working set 决定。把 prefill expert signature 与 KV block 生命周期绑定，再在 locality band 内做 load-aware routing，可以复用 expert weights；代价是 calibration/reclustering、signature metadata、load-locality conflict 和 prefix/worker epoch consistency。Dense 或 expert locality 弱时，普通 least-load routing 仍更合理。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-00466:end -->

**旧方案与约束变化。** `本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**`（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** MoE Decode 的成本不仅由 queue length 决定，还由 batch 激活的 distinct expert working set 决定。把 prefill expert signature 与 KV block 生命周期绑定，再在 locality band 内做 load-aware routing，可以复用 expert weights；代价是 calibration/reclustering、signature metadata、load-locality conflict 和 prefix/worker epoch consistency。Dense 或 expert locality 弱时，普通 least-load routing 仍更合理。 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.00466v1#S4 :: block-lifecycle-bound expert signatures, balanced offline clustering and locality-band online routing; https://arxiv.org/html/2607.00466v1#S5 :: vLLM proxy/hook/artifact implementation`；Evaluation：`https://arxiv.org/html/2607.00466v1#S6 :: author evaluation binds four MoE models, task/language workloads, 5 nodes with 40 AMD MI300X GPUs, 400 Gbps NDR, vLLM 0.21.0rc1, ROCm 7.2 and several P/D topologies`；Limitations/Counterevidence：`https://arxiv.org/html/2607.00466v1#S3.SS5 :: signature design, load/locality conflict and prefix-cache coherence are explicit challenges; the paper has no separate limitations section, so cross-model/workload drift, reclustering and worker churn remain evidence boundaries`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L518-L539`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-SCHEDULING` 的 [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [BaseRT: Best-in-Class LLM Inference on Apple Silicon via Native Metal](https://arxiv.org/html/2607.00501v1)

**系统推理。** 问题是通用执行框架在端侧 Apple GPU 上承担了分配、图构建与 dispatch 开销。方法以预分配 buffer、架构描述符和 Metal 专用融合收窄执行契约；作者只在指定芯片、模型与量化配置上证明其实现收益，不能外推到多请求调度或分布式推理。所得是窄硬件路径的效率，付出的是可移植性、模型覆盖与维护成本，通用引擎在异构和快速演进场景仍更合理。


<!-- claim:SF-2026-ARXIV-2607-00501:start -->A hardware-native engine can remove generic framework allocation, graph and dispatch overhead through preallocated buffers, descriptor-driven architecture differences and chip-specialized fusion. The gain trades portability and scheduling breadth for a narrower hardware contract; the chapter already owns this specialization-versus-portability branch and its benchmark boundary. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-00501:end -->

**旧方案与约束变化。** `A hardware-specialized execution path can fuse layout, precision, kernel and scheduling for a narrow workload, while the general library path retains broader coverage, portability and maintenance stability.`（`books/part-05-inference-system/49-tensorrt-llm.md#L146-L157`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A hardware-native engine can remove generic framework allocation, graph and dispatch overhead through preallocated buffers, descriptor-driven architecture differences and chip-specialized fusion. The gain trades portability and scheduling breadth for a narrower hardware contract; the chapter already owns this specialization-versus-portability branch and its benchmark boundary. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.00501v1#S3 :: native Metal runtime with descriptor-driven architectures, zero-allocation decode, fused specialized kernels and bounded chunked prefill`；Evaluation：`https://arxiv.org/html/2607.00501v1#S4 :: author measurements cover Qwen3, Llama 3.2 and Gemma 4 at Q4/Q8 on specified M3/M4 Pro devices against llama.cpp, MLX and uzu; no result is generalized beyond that hardware/software contract`；Limitations/Counterevidence：`https://arxiv.org/html/2607.00501v1#S5.SS1 :: Metal-only, single-device execution, no continuous batching or multi-request scheduling, and no tensor-parallel/distributed execution`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`已有覆盖`。

本次重新定位到 `INFER-TENSORRT-LLM` 的 [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression](https://arxiv.org/html/2607.00760v1)

**系统推理。** 问题是把 KV eviction 与 quantization 分开优化会错过 token 数和特征秩的联合预算空间。方法让策略同时选择保留 token 与每 token rank，并以 packed layout、后台编码和 fused consumer kernel 落地；作者实验支持其所测长上下文负载中的质量—容量收益，但没有证明逻辑压缩率自动转化为任意 serving 吞吐。代价是布局碎片、策略版本、双缓冲和专用 kernel，Prefill 路径仍未闭合。


<!-- claim:SF-2026-ARXIV-2607-00760:start -->KV compression can jointly vary retained token count and per-token feature rank instead of treating eviction and quantization as isolated policies. This enlarges the quality-capacity search space but requires a packed physical layout, fused consumer kernel, background encoding, strategy versioning and fragmentation control; a logical compression ratio without these paths is not a serving gain. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-00760:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** KV compression can jointly vary retained token count and per-token feature rank instead of treating eviction and quantization as isolated policies. This enlarges the quality-capacity search space but requires a packed physical layout, fused consumer kernel, background encoding, strategy versioning and fragmentation control; a logical compression ratio without these paths is not a serving gain. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.00760v1#S4 :: dynamic token- and feature-dimension compression; https://arxiv.org/html/2607.00760v1#S5 :: packed layout, encode path, PackedAttention, double buffering and incremental strategy generation`；Evaluation：`https://arxiv.org/html/2607.00760v1#S6 :: author accuracy, microbenchmark and end-to-end serving evaluation; retained conclusions do not export headline speedups or quality numbers`；Limitations/Counterevidence：`https://arxiv.org/html/2607.00760v1#S7 :: evaluation is Decode-focused, compressed Prefill remains future work, and PackedAttention still uses CUDA cores rather than a broader optimized kernel path`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-KV-CACHE` 的 [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache](https://arxiv.org/html/2607.01065v1)

**系统推理。** 问题是在极低 bit 预算下，普通欧氏码本把向量方向与尺度混为一谈。方法以 gain-shape 残差量化分别编码方向和尺度；作者在其模型、数据集和困惑度/任务指标上证明重构与质量改进，但没有证明 sub-bit 存储必然带来端到端 serving 加速。代价包括码本查找、scale 元数据、kernel 支持和自回归误差积累，系统判断仍需按有效 bit 与 attention consumer 验收。


<!-- claim:SF-2026-ARXIV-2607-01065:start -->At extreme vector-quantization budgets, separately modeling vector direction and scale can preserve information that ordinary Euclidean centroids conflate. This is a quantizer-design branch, not proof of system speed: codebook lookup, metadata, kernel support and autoregressive error still determine whether sub-bit storage improves serving. Existing attention-distortion and effective-bit accounting already cover the lasting conclusion. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01065:end -->

**旧方案与约束变化。** `KV quantization must be evaluated at the attention consumer and over autoregressive feedback, with physical metadata, kernel and effective-bit costs included rather than inferred from tensor reconstruction alone.`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L452-L482`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** At extreme vector-quantization budgets, separately modeling vector direction and scale can preserve information that ordinary Euclidean centroids conflate. This is a quantizer-design branch, not proof of system speed: codebook lookup, metadata, kernel support and autoregressive error still determine whether sub-bit storage improves serving. Existing attention-distortion and effective-bit accounting already cover the lasting conclusion. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01065v1#S5 :: gain-shape decomposition, assignment and centroid updates plus gradient-weighted variant`；Evaluation：`https://arxiv.org/html/2607.01065v1#S6 :: author evaluation covers synthetic vectors, several open models/datasets, perplexity, downstream tasks, ablations and a decoding-latency appendix; production concurrency and tail SLO are not disclosed`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01065v1#S5.SS2 :: alternating updates optimize a practical surrogate and do not guarantee monotonic decrease of the original reconstruction objective; no separate limitations section is present`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`已有覆盖`。

本次重新定位到 `INFER-KV-CACHE` 的 [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [MemSyco-Bench: Benchmarking Sycophancy in Agent Memory](https://arxiv.org/html/2607.01071v1)

**系统推理。** 问题是 Agent memory 的“检索到”常被误当成“应该采用”。论文把 retrieval 与 adoption 分开，区分应使用、忽略、约束、覆盖和只作个性化的关系；基准只证明所构造场景能暴露 sycophancy，不能给出真实部署中的发生率或权威真值。代价是 authority、valid-time、contradiction 与 judge 元数据；因此它强化现有 read policy，而不产生新的 memory owner。


<!-- claim:SF-2026-ARXIV-2607-01071:start -->Memory quality must separate retrieval success from downstream adoption: a relevant memory can be retrieved yet should be ignored, constrained, superseded or used only for personalization. The existing chapter already gives fact/retrieval-policy separation, authority, contradiction and post-retrieval risk gates, so this source strengthens evidence without changing the mechanism owner. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01071:end -->

**旧方案与约束变化。** `Memory retrieval is not fact adjudication: read policy must distinguish authority, valid time, contradiction, supersession and explicit unknown-current state before deciding whether to use or abstain.`（`books/part-07-agent/77-memory.md#L628-L658`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Memory quality must separate retrieval success from downstream adoption: a relevant memory can be retrieved yet should be ignored, constrained, superseded or used only for personalization. The existing chapter already gives fact/retrieval-policy separation, authority, contradiction and post-retrieval risk gates, so this source strengthens evidence without changing the mechanism owner. 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01071v1#S3 :: five memory-decision relations, benchmark construction and role-aware rubrics; https://arxiv.org/html/2607.01071v1#A2 :: schema, dialogue and validation pipeline`；Evaluation：`https://arxiv.org/html/2607.01071v1#S4 :: generation, retrieval-versus-use attribution and scenario diagnostics across selected memory systems/backbones; the reported post-retrieval proportions are benchmark-bound`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01071v1#A6 :: implementation coverage is incomplete for all listed memory frameworks; synthetic scenarios, LLM judging and backbone choice constrain external validity`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L716-L731`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`已有覆盖`。

本次重新定位到 `AGENT-MEMORY` 的 [Ch77](../../../../books/part-07-agent/77-memory.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?](https://arxiv.org/html/2607.01211v1)

**系统推理。** 问题是可执行优化 benchmark 可能连 reference patch 都无法稳定复现，却仍对 Agent 排名。方法先跨机器和轮次重建、回放 reference artifact，再分析分数公式与小加速尾部的敏感性；740 个 reference patch 的结果证明该验收链必要，但不证明新的通用 Agent 排名。代价是重复执行、环境版本化和方差预算，收益是把候选能力与基础设施噪声分账。


<!-- claim:SF-2026-ARXIV-2607-01211:start -->Executable evaluation must validate the reference artifact before judging candidates and must expose sensitivity to machine, repetition and aggregation rules. The evaluation chapter already contains this exact reference-first admission chain and its representativeness boundary. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01211:end -->

**旧方案与约束变化。** `Benchmark admission first rebuilds and replays the immutable reference artifact across machine and round, then measures infrastructure and scorer variance before candidates are compared.`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L729-L747`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Executable evaluation must validate the reference artifact before judging candidates and must expose sensitivity to machine, repetition and aggregation rules. The evaluation chapter already contains this exact reference-first admission chain and its representativeness boundary. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01211v1#S3 :: rebuild/replay of reference patches across machines and rounds; https://arxiv.org/html/2607.01211v1#S4 :: score-formula and low-speedup-tail sensitivity analysis`；Evaluation：`https://arxiv.org/html/2607.01211v1#S3.SS1 :: 740 reference patches across four cloud providers and 12 machine-round combinations, followed by task/ranking analysis; retained claim is reference validity and score sensitivity, not a new agent ranking`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01211v1#S7 :: selected benchmarks, released artifacts, implementation choices and hardware variation limit generalization`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L860-L874`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 3 / Durability 3 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`已有覆盖`。

本次重新定位到 `PLATFORM-EVALUATION-SYSTEM` 的 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [AutoMem: Automated Learning of Memory as a Cognitive Skill](https://arxiv.org/html/2607.01224v1)

**系统推理。** 问题是手工 memory policy 难以随任务演进，同时又不能把学习到的记忆操作直接升级为行动权限。方法把 memory policy 作为可版本化派生资产，以 held-out promotion/rollback 更新，并把记忆操作能力与 task action authority 分离；作者只在三个程序化游戏和各自 scaffold 上证明可学性，不能外推到开放环境。代价是环境特定训练、评估集治理和失败回滚。


<!-- claim:SF-2026-ARXIV-2607-01224:start -->Memory policy can be optimized as a versioned artifact through a held-out promotion loop, while memory-operation proficiency can be trained separately from task-action authority. The existing Memory chapter already separates derived policy, validation, promotion/rollback and Workflow ownership, so the source is corroborating rather than a new owner mechanism. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01224:end -->

**旧方案与约束变化。** `A learned Memory policy is a derived, versioned procedural asset whose applicability, source episodes and validation results must pass held-out promotion and retain provenance and rollback.`（`books/part-07-agent/77-memory.md#L343-L433`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Memory policy can be optimized as a versioned artifact through a held-out promotion loop, while memory-operation proficiency can be trained separately from task-action authority. The existing Memory chapter already separates derived policy, validation, promotion/rollback and Workflow ownership, so the source is corroborating rather than a new owner mechanism. 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01224v1#S2 :: file-system memory, scaffold-revision loop and separately trained memory specialist; https://arxiv.org/html/2607.01224v1#A1 :: fixed-seed promotion and training implementation`；Evaluation：`https://arxiv.org/html/2607.01224v1#S3 :: author evaluation covers three procedurally generated long-horizon games using Qwen2.5-32B-Instruct and specified baselines; leaderboard comparison is not treated as model equivalence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01224v1#S6 :: episodic memory resets between runs, evaluation is limited to games, and each environment uses a separate scaffold/specialist`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L806-L819`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`已有覆盖`。

本次重新定位到 `AGENT-MEMORY` 的 [Ch77](../../../../books/part-07-agent/77-memory.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

所有性能数字仅在原文披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator 范围内解释；未披露字段保持 `Not Disclosed`，本次没有把作者 benchmark 写成通用生产结论。

## 5. 缺口与下一步

无

本窗没有外部材料请求或待执行工作；非作者独立语义复核已确认已有 Books 段落是机制正文，而非只有 trace。

## 6. 复核

复核者：主任务独立复核（非本报告作者）

结论：通过

独立复核逐项检查 8 个候选的窗口、exact-v1、评分、证据边界和 Books 路由，并核对 scheduling、KV、execution、evaluation 与 memory 章节正文。对旧队列中的模型卡、VLA 局部适配、量化局部改进、RAG uncertainty 与 data-mixture 项分层抽检，未发现应恢复而被系统性漏掉的长期设计增量。格式校验与 `git diff --check` 通过。
