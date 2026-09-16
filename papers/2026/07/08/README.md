# Daily Research — 2026-07-08

**规范：** V3
**窗口：** 2026-07-07T09:00:00+08:00 ～ 2026-07-08T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T16:30:00+08:00

## 1. 结论

本窗复用并核实 489 个去重 arXiv v1 原始身份，逐条按标题与完整摘要重新判断项目贡献；旧恢复队列 20 项中，17 个材料家族通过当前门槛，3 项因仅是领域应用、局部方法包装、通用 benchmark/Agent 组合或没有改变长期设计判断而转为 pre-denominator closure。关闭结果汇总在本报告的复核结论中，不在正文伪装成候选。

17 项均达到与评分相称的证据审阅深度，并重新检查撤回/纠错信号与首次公开 owner。旧报告标记为 `Integrate` 的机制已经出现在相应 Books 正文，本次统一改为“已有覆盖”；不重复追加，也不以 evidence trace 代替正文承载。独立复核已确认候选准入、证据边界与 body anchor 闭合。

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
| SRC-ARXIV | 复核本窗官方公告 owner、489 个去重 v1 身份及旧恢复队列；逐条标题、边界项完整摘要语义筛选后保留 17 项 | 已检查 | 无 |

本窗没有触发需要改变候选或结论的按需来源。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Is Your NPU Ready for LLMs? Dissecting the Hidden Efficiency Bottlenecks in Mobile LLM Inference](https://arxiv.org/html/2607.05475v1) | 2026-07-08T08:00:00+08:00 | Mobile backend choice is phase dependent: prefill exposes large compute-dense shapes that can fit NPU strengths, while single-token decode exposes small dynamic kernels and memo…；`2+3+3=8` | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Akashic: A Low-Overhead LLM Inference Service with MemAttention](https://arxiv.org/html/2607.05708v1) | 2026-07-08T08:00:00+08:00 | Instead of rewriting full memory or independently summarizing fixed segments, MemAttention compacts one bounded chunk and reconciles it against a small related set before commit…；`3+3+2=8` | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [SpanUQ: Span-Level Uncertainty Quantification for Large Language Model Generation](https://arxiv.org/html/2607.05721v1) | 2026-07-08T08:00:00+08:00 | The paper shows that a model-specific white-box probe can jointly identify semantic spans and rank uncertainty under its factual-English benchmark; it does not turn probe output…；`3+3+3=9` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Think Before You Grid-Search: Floor-First Triage for LLM Serving](https://arxiv.org/html/2607.05876v1) | 2026-07-08T08:00:00+08:00 | Replace immediate grid search with a versioned resource vector for weight/KV bytes, FLOPs, communication bytes/messages and capacity; compute optimistic and no-overlap bounds, i…；`2+3+3=8` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [PolicyShiftGuard: Benchmarking and Improving Policy-Adaptive Image Guardrails](https://arxiv.org/html/2607.05910v1) | 2026-07-08T08:00:00+08:00 | Treat moderation as a relation between content evidence and a versioned runtime policy, not an intrinsic image label. Randomize policy presentation to remove slot shortcuts, the…；`3+2+3=8` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [MoWorld: A Flash World Model](https://arxiv.org/html/2607.06216v1) | 2026-07-08T08:00:00+08:00 | Authors report a 14B MoE video world model with history selection, few-step causal distillation and NPU execution optimizations under their visual/system benchmark; this does no…；`3+3+2=8` | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition](https://arxiv.org/html/2607.06256v1) | 2026-07-08T08:00:00+08:00 | The authors show a large clean-snapshot versus chained-rollout gap for the same checkpoints and trace failures to readiness/grounding/control under a small BEHAVIOR-1K pilot; th…；`3+3+3=9` | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [AlayaWorld: Long-Horizon and Playable Video World Generation](https://arxiv.org/html/2607.06291v1) | 2026-07-08T08:00:00+08:00 | A proposed full-stack route combines autoregressive video generation with explicit camera/geometry cache, compressed history, rollout-error replay and distilled sampling to purs…；`2+3+2=7` | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Estimating Uncertainty from Reasoning: A Large-Scale Study of Multi- and Crosslingual MCQA Performance in LLMs](https://arxiv.org/html/2607.06327v1) | 2026-07-08T08:00:00+08:00 | The authors report multilingual MCQA correlations under their nine-model/22-language contract; results concern correctness discrimination of elicited reasoning and do not establ…；`2+2+3=7` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ActionCache: Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement](https://arxiv.org/html/2607.06370v1) | 2026-07-08T08:00:00+08:00 | Authors report action-head latency/success trade-offs for pi_0.5 and GR00T-N1.6 on their simulation and real-robot contracts; they do not prove cached actions remain safe under …；`3+2+2=7` | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [SIEVE: Structure-Aware Data Selection for Imitation Learning with VLA Models](https://arxiv.org/html/2607.06442v1) | 2026-07-08T08:00:00+08:00 | Authors report that SIEVE-selected subsets can outperform full-data training in their VLA/simulator contracts; they do not establish that discovered clusters are true skills or …；`3+3+3=9` | 深入完成 | 已有覆盖：`TRAIN-DATA`，[Ch27](../../../../books/part-04-training-system/27-data.md) |
| [FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference](https://arxiv.org/html/2607.06519v1) | 2026-07-08T08:00:00+08:00 | Exploit adjacent-layer correlation without assuming uniform redundancy: share low-frequency depth components, retain sparse layer-specific residuals, and route each head among s…；`3+2+2=7` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [DepthWeave-KV: Token-Adaptive Cross-Layer Residual Factorization for Long-Context KV Cache Compression](https://arxiv.org/html/2607.06523v1) | 2026-07-08T08:00:00+08:00 | Represent neighboring-layer K/V with shared low-rank bases, then allocate token-specific residual rank from online attention-output error rather than a uniform cache budget; fus…；`3+2+2=7` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation](https://arxiv.org/html/2607.06558v1) | 2026-07-08T08:00:00+08:00 | Authors report policy gains from mixed real and generated data and feasibility of synthetic-only transfer on their tasks; they do not prove the generated video is a physically v…；`3+3+2=8` | 深入完成 | 已有覆盖：`TRAIN-DATA`，[Ch27](../../../../books/part-04-training-system/27-data.md) |
| [RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation](https://arxiv.org/html/2607.06559v1) | 2026-07-08T08:00:00+08:00 | Co-generate appearance, depth and optical flow so predictive state carries geometry and motion, then expose internal predictive features to a one-forward policy instead of placi…；`3+2+2=7` | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Vision as Unified Multimodal Generation](https://arxiv.org/html/2607.06560v1) | 2026-07-08T08:00:00+08:00 | Convert heterogeneous annotations into a shared sample contract—visual inputs, natural-language task/schema instruction, and a text/image/mixed response that can be deterministi…；`3+3+3=9` | 深入完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Lift3D-VLA: Lifting VLA Models to 3D Geometry and Dynamics-Aware Manipulation](https://arxiv.org/html/2607.06564v1) | 2026-07-08T08:00:00+08:00 | Authors report simulation, real-task and OOD gains under their sensor/task contract; synthesized point clouds, depth sensors and 25-rollout simulator slices do not prove general…；`2+2+3=7` | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |

## 4. 证据与知识整合

### [Is Your NPU Ready for LLMs? Dissecting the Hidden Efficiency Bottlenecks in Mobile LLM Inference](https://arxiv.org/html/2607.05475v1)

**系统推理。** 问题是移动 NPU 上 Prefill 与 Decode 的算术强度、内存行为和 kernel 瓶颈不同，不能用单一 tokens/s 判断。论文分阶段测量并揭示 phase-dependent bottleneck；作者数据只覆盖指定 NPU、模型和实现，未证明其他端侧硬件相同。代价是双套优化路径、设备特定 profiling 与更复杂的 runtime 选择。


<!-- claim:SF-2026-ARXIV-2607-05475:start -->Mobile backend choice is phase dependent: prefill exposes large compute-dense shapes that can fit NPU strengths, while single-token decode exposes small dynamic kernels and memory traffic that can favor CPU. Framework offload coverage, graph/static-shape constraints, quantization support, tensor-layout conversion, host polling, sleep latency, DVFS and affinity determine whether nominal NPU capability becomes end-to-end efficiency. The framework owns operator partition/offload and layout conversions; backend runtimes own executable graph/quantization constraints; host CPU owns polling, wake/sleep and thread scheduling; request phase and KV state determine current shape. A backend switch is therefore a state-transfer/control decision, not a free dispatch choice. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-05475:end -->

**旧方案与约束变化。** `Ch49 already treats execution planning as model x shape x precision x hardware x kernel selection, but its accelerator discussion does not yet make host control and prefill/decode backend asymmetry explicit.`（`books/part-05-inference-system/49-tensorrt-llm.md#L41-L67`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Mobile backend choice is phase dependent: prefill exposes large compute-dense shapes that can fit NPU strengths, while single-token decode exposes small dynamic kernels and memory traffic that can favor CPU. Framework offload coverage, graph/static-shape constraints, quantization support, tensor-layout conversion, host polling, sleep latency, DVFS and affinity determine whether nominal NPU capability becomes end-to-end efficiency. The framework owns operator partition/offload and layout conversions; backend runtimes own executable graph/quantization constraints; host CPU owns polling, wake/sleep and thread scheduling; request phase and KV state determine current shape. A backend switch is therefore a state-transfer/control decision, not a free dispatch choice. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.05475v1#S3.SS1; https://arxiv.org/html/2607.05475v1#S3.SS2; https://arxiv.org/html/2607.05475v1#S3.SS3; https://arxiv.org/html/2607.05475v1#S3.SS4 — four-device hardware matrix, throughput/energy method and controlled protocol; https://arxiv.org/html/2607.05475v1#S5; https://arxiv.org/html/2607.05475v1#S6; https://arxiv.org/html/2607.05475v1#S7 — framework gaps, backend optimization and host/backend scheduling mechanisms`；Evaluation：`https://arxiv.org/html/2607.05475v1#S4 and #S8 — five frameworks, three backends, model/quantization matrix, cross-layer studies and estimated best-practice combination`；Limitations/Counterevidence：`Not Disclosed — v1 has no dedicated limitations section; bounded by four Qualcomm phones, selected framework versions, closed QNN behavior, author-only measurement and estimated rather than deployed combined optimization`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 3 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-TENSORRT-LLM` 的 [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Akashic: A Low-Overhead LLM Inference Service with MemAttention](https://arxiv.org/html/2607.05708v1)

**系统推理。** 问题是长上下文服务把所有历史常驻会超出显存，把每次都远端取回又受延迟支配。Akashic 以 MemAttention 对有限 chunk 做检索/聚合并把计算靠近 memory tier；作者实验支持其栈内的开销收益，未证明任意 query 都能在有限候选中保真。代价是 chunk identity、索引漂移、tier failure 与一致性。


<!-- claim:SF-2026-ARXIV-2607-05708:start -->Instead of rewriting full memory or independently summarizing fixed segments, MemAttention compacts one bounded chunk and reconciles it against a small related set before commit. The Memory Manager then observes co-access and physically co-locates likely co-retrieved chunks, using out-of-place relocation and garbage collection to reduce fragmentation without changing logical memory identity. Logical memory units own semantic identity, provenance and revision; the reconciliation policy owns derived cross-chunk updates; retrieval owns the selected evidence set; the storage manager owns physical placement, relocation and GC. Physical moves must not create a second semantic truth or silently change authorization/deletion state. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-05708:end -->

**旧方案与约束变化。** `Ch77 owns logical memory identity, provenance, derived views, retrieval and lifecycle, but does not yet make physical co-access placement a separate state owner; Ch42 owns request/runtime cost rather than memory semantics.`（`books/part-07-agent/77-memory.md#L314-L343`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Instead of rewriting full memory or independently summarizing fixed segments, MemAttention compacts one bounded chunk and reconciles it against a small related set before commit. The Memory Manager then observes co-access and physically co-locates likely co-retrieved chunks, using out-of-place relocation and garbage collection to reduce fragmentation without changing logical memory identity. Logical memory units own semantic identity, provenance and revision; the reconciliation policy owns derived cross-chunk updates; retrieval owns the selected evidence set; the storage manager owns physical placement, relocation and GC. Physical moves must not create a second semantic truth or silently change authorization/deletion state. 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.05708v1#S3.SS1; https://arxiv.org/html/2607.05708v1#S3.SS2 — heterogeneous context density and semantic/physical locality gap; https://arxiv.org/html/2607.05708v1#S4.SS1; https://arxiv.org/html/2607.05708v1#S4.SS2; https://arxiv.org/html/2607.05708v1#S4.SS3 — chunk-bounded MemAttention, cross-chunk reconciliation, locality-aware Memory Manager and implementation`；Evaluation：`https://arxiv.org/html/2607.05708v1#S5.SS1; https://arxiv.org/html/2607.05708v1#S5.SS2; https://arxiv.org/html/2607.05708v1#S5.SS3; https://arxiv.org/html/2607.05708v1#S5.SS4; https://arxiv.org/html/2607.05708v1#S5.SS5 — LoCoMo/SWE-bench/BrowseComp/WebArena setup, quality, concurrency, locality/storage and ablation/sensitivity`；Limitations/Counterevidence：`Not Disclosed — v1 has no dedicated limitations section; claim boundary is constrained by author-only four-benchmark evaluation, absent event-time code, mixed harness/model dependencies, and no crash recovery, privacy/deletion, authorization or production multi-tenancy study`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `AGENT-MEMORY` 的 [Ch77](../../../../books/part-07-agent/77-memory.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [SpanUQ: Span-Level Uncertainty Quantification for Large Language Model Generation](https://arxiv.org/html/2607.05721v1)

**系统推理。** 问题是 token entropy 或整句单分数无法定位长输出中真正不确定的语义片段。SpanUQ 用多层 hidden state 预测 span 集合及不确定度；作者在英文事实性数据和五个 backbone 上证明检测/排序能力，未把 probe 输出变成真值概率。代价是白盒访问、标注与部署切片校准，外部 evidence 仍是最终 authority。


<!-- claim:SF-2026-ARXIV-2607-05721:start -->The paper shows that a model-specific white-box probe can jointly identify semantic spans and rank uncertainty under its factual-English benchmark; it does not turn probe output into truth probability or remove deployment-slice calibration. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-05721:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Move uncertainty from token noise or one sequence score to typed semantic spans, distilling multi-sample claim support into a single-pass probe while preserving an explicit external-verification boundary. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.05721v1#S3 (frozen-LLM multi-layer hidden-state fusion, DETR-style span set prediction, Mixture-of-Beta uncertainty and iterative refinement)`；Evaluation：`https://arxiv.org/html/2607.05721v1#S4 (20K-prompt/approximately-293K-span benchmark, five backbones, human-checked test labels, calibration/detection metrics and component ablations)`；Limitations/Counterevidence：`https://arxiv.org/html/2607.05721v1#S5 (white-box hidden-state access, English factuality scope, expensive label construction, confident-wrong risk and external-verification boundary)`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `PLATFORM-EVALUATION-SYSTEM` 的 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Think Before You Grid-Search: Floor-First Triage for LLM Serving](https://arxiv.org/html/2607.05876v1)

**系统推理。** 问题是 serving 优化直接 grid search 会在尚未识别物理下界时浪费试验并误判瓶颈。方法先建立 weight/KV、FLOPs、通信 bytes/messages 与 capacity 的资源向量，比较 optimistic/no-overlap floor 后才 profiling；案例只证明对所述 671B MoE/H20 配置的诊断价值，未给出可达性能保证。代价是准确建模和版本化 workload，但能区分物理墙与实现残差。


<!-- claim:SF-2026-ARXIV-2607-05876:start -->Replace immediate grid search with a versioned resource vector for weight/KV bytes, FLOPs, communication bytes/messages and capacity; compute optimistic and no-overlap bounds, identify the first binding wall as load changes, compare observed steady-state service time against the bound, and open a profiler only when the residual is material. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-05876:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Replace immediate grid search with a versioned resource vector for weight/KV bytes, FLOPs, communication bytes/messages and capacity; compute optimistic and no-overlap bounds, identify the first binding wall as load changes, compare observed steady-state service time against the bound, and open a profiler only when the residual is material. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.05876v1#S3 (five-dimensional resource account; optimistic max and no-overlap sum floors; wall ordering)`；Evaluation：`https://arxiv.org/html/2607.05876v1#S5 (DeepSeek-V3.2-style 671B MoE/MLA case study on 16 H20; concurrency-dependent TP/DP walls and reconciliation)`；Limitations/Counterevidence：`https://arxiv.org/html/2607.05876v1#S5.SS6 (physical bounds are not achievable expectations; P50 service time diagnoses residual while P99 validates SLO; queueing is outside the resource floor)`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 3 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `PLATFORM-EVALUATION-SYSTEM` 的 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [PolicyShiftGuard: Benchmarking and Improving Policy-Adaptive Image Guardrails](https://arxiv.org/html/2607.05910v1)

**系统推理。** 问题是 moderation 不能把图像固有标签与运行时政策混为一谈。PolicyShiftGuard 把决策建模为 content evidence 与 versioned policy 的关系，并用同图不同政策对消除位置捷径；作者只在七类、28项英文静态图像政策上证明适应性。代价是政策版本、配对数据和冲突解释，不能外推到视频或开放政策。


<!-- claim:SF-2026-ARXIV-2607-05910:start -->Treat moderation as a relation between content evidence and a versioned runtime policy, not an intrinsic image label. Randomize policy presentation to remove slot shortcuts, then train matched same-image pass/block pairs so the decision must change when the authoritative boundary changes. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-05910:end -->

**旧方案与约束变化。** `本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**`（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Treat moderation as a relation between content evidence and a versioned runtime policy, not an intrinsic image label. Randomize policy presentation to remove slot shortcuts, then train matched same-image pass/block pairs so the decision must change when the authoritative boundary changes. 它改变 `PLATFORM-SECURITY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.05910v1#S3 (runtime policy bundle, randomized-policy SFT, same-image boundary pairs and pair-margin objective)`；Evaluation：`https://arxiv.org/html/2607.05910v1#S4 (Adaptive and held-out policy-shift splits, F1/PSS, latency); https://arxiv.org/html/2607.05910v1#A5 (rerun and breakdown details); https://arxiv.org/html/2607.05910v1#S5 (boundary-pair and training-branch ablations)`；Limitations/Counterevidence：`https://arxiv.org/html/2607.05910v1#A1 (static images, English structured policies, finite seven-category/28-policy catalog)`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L802-L812`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-SECURITY`。
- Books disposition：`已有覆盖`。

本次重新定位到 `PLATFORM-SECURITY` 的 [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [MoWorld: A Flash World Model](https://arxiv.org/html/2607.06216v1)

**系统推理。** 问题是实时视频 world model 同时受历史长度、rollout drift 与 NPU residency 约束。MoWorld 联合语义历史选择、自 rollout 蒸馏和模块/并行/kernel 共设计；作者只在其 14B MoE/NPU 与视觉指标上证明速度和生成质量，未证明 action-sufficient causal dynamics。代价是检索误差、distillation bias 与平台绑定。


<!-- claim:SF-2026-ARXIV-2607-06216:start -->Authors report a 14B MoE video world model with history selection, few-step causal distillation and NPU execution optimizations under their visual/system benchmark; this does not prove an action-sufficient causal environment model. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-06216:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Treat real-time world-model deployment as joint state and runtime design: bound persistent history by semantic retrieval, train the causal student on its own rollout distribution, and co-design residency/parallelism/kernels around streaming latency. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.06216v1#S3 (camera-conditioned long-horizon pretraining and curriculum on NPU clusters); https://arxiv.org/html/2607.06216v1#S4 (recent/initial/camera-related latent history selection, causal flow-matching warmup and self-forcing few-step distillation); https://arxiv.org/html/2607.06216v1#S5 (module residency, pipeline, parallelism and kernel co-design for streaming inference)`；Evaluation：`https://arxiv.org/html/2607.06216v1#S6 (VBench-I2V and in-house camera-control quality plus system performance/cost measurements)`；Limitations/Counterevidence：`https://arxiv.org/html/2607.06216v1#S6 (visual/image-to-video metrics do not prove causal dynamics, policy utility or physical correctness); https://arxiv.org/html/2607.06216v1#S8 (headline performance remains tied to the disclosed MoWorld/NPU stack)`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `MULTIMODAL-WORLD-MODELS` 的 [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition](https://arxiv.org/html/2607.06256v1)

**系统推理。** 问题是 VLA 单项 skill 在 clean snapshot 成功，不代表前一 skill 的真实终态满足下一项入口。论文把 current postcondition 与 next-skill readiness 分开，并在 chained rollout 中验证；十个 BEHAVIOR-1K pilot 证明存在显著 handoff gap，未证明所提 predicate 完整或总体失败率。代价是 typed contract、多视角 verifier、replan 与人工恢复。


<!-- claim:SF-2026-ARXIV-2607-06256:start -->The authors show a large clean-snapshot versus chained-rollout gap for the same checkpoints and trace failures to readiness/grounding/control under a small BEHAVIOR-1K pilot; they do not estimate population failure rates or prove the proposed next-skill predicate. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-06256:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Separate skill-local success from compositional readiness: a completed skill must establish both its own postcondition and a typed admission predicate for the next skill under the actual chained terminal state. 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.06256v1#S2 (next-skill readiness as a typed relation beyond the current skill postcondition); https://arxiv.org/html/2607.06256v1#S3 (typed skill contract, bounded Plan-Act-Verify-Replan and multi-view verification)`；Evaluation：`https://arxiv.org/html/2607.06256v1#S4 (same checkpoints under clean boundary snapshots versus chained terminal states; progress and failure attribution across ten BEHAVIOR-1K tasks)`；Limitations/Counterevidence：`https://arxiv.org/html/2607.06256v1#S5 (small pilot traces, verifier/category bias, underspecified object identity and missing no-recovery/oracle-reset ablations)`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `MULTIMODAL-EMBODIED-VLA` 的 [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [AlayaWorld: Long-Horizon and Playable Video World Generation](https://arxiv.org/html/2607.06291v1)

**系统推理。** 问题是长视频生成的外观连续性不足以维持可修订的世界状态。AlayaWorld 组合 camera/geometry cache、压缩历史、rollout-error replay 与蒸馏采样；v1 主要提供定性和有限生成证据，未证明物理因果、闭环 policy utility 或完整 release 承诺。代价是几何依赖、缓存一致性和长期误差积累。


<!-- claim:SF-2026-ARXIV-2607-06291:start -->A proposed full-stack route combines autoregressive video generation with explicit camera/geometry cache, compressed history, rollout-error replay and distilled sampling to pursue long-horizon playable worlds. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-06291:end -->

**旧方案与约束变化。** `Ch25 already owns recent/view-indexed/compressed history, stale-state risk, transition-aware belief and the distinction between visual persistence and causal world-state truth; AlayaWorld is a qualitative bounded case, not a new canonical mechanism.`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L293`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A proposed full-stack route combines autoregressive video generation with explicit camera/geometry cache, compressed history, rollout-error replay and distilled sampling to pursue long-horizon playable worlds. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.06291v1#S3 (AR-DiT pipeline, prompt switching, camera control/3D cache, history compression, error bank and few-step distillation)`；Evaluation：`https://arxiv.org/html/2607.06291v1#S4 (reported forward-exploration examples/metrics; incomplete relative to the paper's own release promise)`；Limitations/Counterevidence：`https://arxiv.org/html/2607.06291v1#S3.SS1 (3D-cache complexity, depth/geometry dependence and dynamic-object limits); https://arxiv.org/html/2607.06291v1#S4 (only qualitative camera/action/loop-closure/long-horizon evidence in event-time v1)`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L677-L688`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 3 / Durability 2 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`已有覆盖`。

本次重新定位到 `MULTIMODAL-WORLD-MODELS` 的 [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Estimating Uncertainty from Reasoning: A Large-Scale Study of Multi- and Crosslingual MCQA Performance in LLMs](https://arxiv.org/html/2607.06327v1)

**系统推理。** 问题是跨语言 reasoning 的自信分数可能混合语言熟悉度、题型和答案正确性。研究在多语言 MCQA 上比较 reasoning-derived uncertainty；结果只支持封闭选项与所测模型，不能外推为开放生成的校准概率。代价是按语言/任务分片校准与 evaluator 偏差，现有 Evaluation owner 已承载。


<!-- claim:SF-2026-ARXIV-2607-06327:start -->The authors report multilingual MCQA correlations under their nine-model/22-language contract; results concern correctness discrimination of elicited reasoning and do not establish open-ended factual calibration. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-06327:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Make uncertainty calibration slice-aware not only by domain, but by generation language, model scale/family and estimator access contract; method rankings can reverse across these slices. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.06327v1#S3 (parallel multilingual MCQA with exact answer labels, long-form reasoning, nine uncertainty estimators and scale/language slices)`；Evaluation：`https://arxiv.org/html/2607.06327v1#S4 (22 languages, model-scale and reasoning-language comparisons, threshold-transfer analysis and 95% confidence intervals)`；Limitations/Counterevidence：`https://arxiv.org/html/2607.06327v1#S5 (MCQA/elicited-reasoning scope, target-language usability trade-off, training-pipeline confounding and open-ended correctness left open)`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `PLATFORM-EVALUATION-SYSTEM` 的 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [ActionCache: Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement](https://arxiv.org/html/2607.06370v1)

**系统推理。** 问题是 VLA 重复场景可复用上一动作，但直接缓存会在环境细微变化时造成危险执行。ActionCache 先检索候选 action，再由当前观察做 refinement；作者结果支持所测机器人任务的加速，未证明 unseen aliasing 或安全边界。代价是缓存身份、相似度错误、校正延迟与强制 fallback。


<!-- claim:SF-2026-ARXIV-2607-06370:start -->Authors report action-head latency/success trade-offs for pi_0.5 and GR00T-N1.6 on their simulation and real-robot contracts; they do not prove cached actions remain safe under unseen state aliasing or environment change. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-06370:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Move warm-starting from same-episode temporal continuity to versioned output retrieval: reuse a prior action chunk only when an action-relevant multimodal key passes admission, refine it for a bounded number of flow steps, otherwise fall back to the base policy. 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.06370v1#S3 (external multimodal key, action-chunk value, thresholded hit/miss, zero/few-step refinement and full-generation fallback)`；Evaluation：`https://arxiv.org/html/2607.06370v1#S4 (VLABench and real-robot success/latency trade-offs, threshold/key/cache/NFE ablations)`；Limitations/Counterevidence：`https://arxiv.org/html/2607.06370v1#S4 (finite cache and task distributions, similarity proxy, author-selected hit threshold, action-head rather than end-to-end latency); https://arxiv.org/html/2607.06370v1#S5 (claims limited to the evaluated VLA/action spaces)`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `MULTIMODAL-EMBODIED-VLA` 的 [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [SIEVE: Structure-Aware Data Selection for Imitation Learning with VLA Models](https://arxiv.org/html/2607.06442v1)

**系统推理。** 问题是 imitation data 仅按样本相似度筛选，会忽略 primitive 与 transition 对策略学习的作用。SIEVE 用结构化动作/状态转移覆盖选择数据；作者实验只证明其任务中的样本效率，cluster 不等于真实 skill。代价是结构提取、覆盖偏差和分布漂移，原始广覆盖数据在未知任务上仍重要。


<!-- claim:SF-2026-ARXIV-2607-06442:start -->Authors report that SIEVE-selected subsets can outperform full-data training in their VLA/simulator contracts; they do not establish that discovered clusters are true skills or that central trajectories cover safety-critical tails. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-06442:end -->

**旧方案与约束变化。** `本章的核心判断是：**训练数据不是等待模型消费的原料，而是对模型行为分布的可执行 specification。**收集、过滤、去重、配比和采样共同定义经验风险中的样本权重；数据 pipeline 的任何偏差，都会通过梯度进入 checkpoint。`（`books/part-04-training-system/27-data.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Replace trajectory-count coverage with reusable-structure coverage: allocate budget over primitive compositions and transition interfaces under diminishing returns, then choose stable representatives within each structural bucket. 它改变 `TRAIN-DATA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.06442v1#Sx3 (gripper-boundary segmentation, V-JEPA2/PCA primitive clustering, reuse/discriminability criterion, diminishing-return structural exposure and medoid selection)`；Evaluation：`https://arxiv.org/html/2607.06442v1#Sx4 (Bridge-V2, Fractal and GR00T-X-Sim across two VLA heads; full/random/DemInf/SCIZOR baselines, fixed/proportional steps and component ablations)`；Limitations/Counterevidence：`https://arxiv.org/html/2607.06442v1#Sx4 (primitive identity depends on segmentation/encoder/clustering; simulator success and medoid centrality do not prove physical diversity or rare-failure coverage); https://arxiv.org/html/2607.06442v1#Sx5 (conclusions remain within imitation-learning data selection)`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-DATA`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `TRAIN-DATA` 的 [Ch27](../../../../books/part-04-training-system/27-data.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference](https://arxiv.org/html/2607.06519v1)

**系统推理。** 问题是各层 KV 频率结构不同，统一压缩强度会在关键层丢失信息。FreqDepthKV 跨层共享频率基并按深度分配残差，同时保留 exact route；作者实验支持指定模型与长上下文任务，未证明跨架构稳定。代价是频域变换、共享误差和专用 kernel。


<!-- claim:SF-2026-ARXIV-2607-06519:start -->Exploit adjacent-layer correlation without assuming uniform redundancy: share low-frequency depth components, retain sparse layer-specific residuals, and route each head among shared, residual and exact cache modes using prompt-local attention-logit reconstruction evidence. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-06519:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Exploit adjacent-layer correlation without assuming uniform redundancy: share low-frequency depth components, retain sparse layer-specific residuals, and route each head among shared, residual and exact cache modes using prompt-local attention-logit reconstruction evidence. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.06519v1#S3 (adjacent-layer DCT-style low-frequency sharing, sparse high-frequency residuals, per-head shared/residual/exact routing from prefill probes)`；Evaluation：`https://arxiv.org/html/2607.06519v1#S4 (32K QA/retrieval/summarization/code metrics plus throughput, TTFT and peak KV memory); https://arxiv.org/html/2607.06519v1#S5 (factorization, residual, routing, reconstruction loss, exact fallback and block-size variants)`；Limitations/Counterevidence：`Not Disclosed — exact v1 provides no dedicated limitations section; model/checkpoint, hardware, precision, batch/concurrency and production-serving integration are not sufficiently disclosed for portable performance claims`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-KV-CACHE` 的 [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [DepthWeave-KV: Token-Adaptive Cross-Layer Residual Factorization for Long-Context KV Cache Compression](https://arxiv.org/html/2607.06523v1)

**系统推理。** 问题是跨层 KV 冗余可压缩，但固定低秩会忽略 token 难度差异。DepthWeave 共享基并为 token 分配 residual rank，以 fused kernel 消费；作者结果支持所测容量—质量折中，未证明所有 token 路由可靠。代价是 rank metadata、fragmentation、融合实现和错误累积。


<!-- claim:SF-2026-ARXIV-2607-06523:start -->Represent neighboring-layer K/V with shared low-rank bases, then allocate token-specific residual rank from online attention-output error rather than a uniform cache budget; fuse basis lookup, residual dequantization and projection to avoid returning all savings as decode overhead. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-06523:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Represent neighboring-layer K/V with shared low-rank bases, then allocate token-specific residual rank from online attention-output error rather than a uniform cache budget; fuse basis lookup, residual dequantization and projection to avoid returning all savings as decode overhead. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.06523v1#S3 (neighbor-layer low-rank bases, token-conditional residual rank, online attention-output error tracking and fused execution)`；Evaluation：`https://arxiv.org/html/2607.06523v1#S4 (16K-128K retrieval slices; main 64K greedy-512 protocol; quality, memory, TTFT, throughput, perplexity and reconstruction error); https://arxiv.org/html/2607.06523v1#S5 (basis sharing, token router, residual reconstruction/gates and fused-kernel ablations)`；Limitations/Counterevidence：`https://arxiv.org/html/2607.06523v1#S7 (single compressed layout; batching, prefix reuse, PD disaggregation and multi-tenant pools left open); no standalone limitations section`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `INFER-KV-CACHE` 的 [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation](https://arxiv.org/html/2607.06558v1)

**系统推理。** 问题是 teleoperation 数据昂贵，生成式 world model 可补充动作条件轨迹。RynnWorld-Teleop 用 action-conditioned 视频生成产生训练数据；作者只证明合成数据在其任务中的增益，未证明生成 transition 等同真实物理。代价是 simulator bias、动作标定和现实验证，真实采集仍是 authority。


<!-- claim:SF-2026-ARXIV-2607-06558:start -->Authors report policy gains from mixed real and generated data and feasibility of synthetic-only transfer on their tasks; they do not prove the generated video is a physically valid transition or that one model transfers across robot kinematics without adaptation. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-06558:end -->

**旧方案与约束变化。** `本章的核心判断是：**训练数据不是等待模型消费的原料，而是对模型行为分布的可执行 specification。**收集、过滤、去重、配比和采样共同定义经验风险中的样本权重；数据 pipeline 的任何偏差，都会通过梯度进入 checkpoint。`（`books/part-04-training-system/27-data.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Decouple operator time from physical robot recording by driving an action-conditioned video world model with human hand poses, retargeting the pose stream to a robot schema and treating the generated egocentric sequence plus action label as a derived training trajectory. 它改变 `TRAIN-DATA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.06558v1#S3 (depth-aware hand-skeleton conditioning, human-to-robot progressive training and causal autoregressive distillation); https://arxiv.org/html/2607.06558v1#S4 (pose-stream capture, retargeting and synthetic state-action trajectory construction)`；Evaluation：`https://arxiv.org/html/2607.06558v1#S5 (35-trial real-robot tasks, real-only/synthetic-only/mixed policy data, video/world-model comparisons and conditioning/distillation ablations)`；Limitations/Counterevidence：`https://arxiv.org/html/2607.06558v1#S6 (deformable/liquid physics failures and per-platform fine-tuning); synthetic pixels and pose labels do not establish physical contact truth`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-DATA`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `TRAIN-DATA` 的 [Ch27](../../../../books/part-04-training-system/27-data.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation](https://arxiv.org/html/2607.06559v1)

**系统推理。** 问题是机器人策略需要同时理解外观、深度、流和动作后果，而分离模型会产生状态不一致。RynnWorld-4D 共享 RGB/depth/flow predictive representation 并接 one-pass policy；作者实验支持所测 manipulation，未证明开放世界因果充分性。代价是多任务权重、传感器同步和错误耦合。


<!-- claim:SF-2026-ARXIV-2607-06559:start -->Co-generate appearance, depth and optical flow so predictive state carries geometry and motion, then expose internal predictive features to a one-forward policy instead of placing iterative video denoising on every action step. The generated world branch and control branch share representation but have different latency and authority contracts. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-06559:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Co-generate appearance, depth and optical flow so predictive state carries geometry and motion, then expose internal predictive features to a one-forward policy instead of placing iterative video denoising on every action step. The generated world branch and control branch share representation but have different latency and authority contracts. 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.06559v1#S3 (projective RGB/depth/flow representation, tri-branch diffusion and single-forward predictive-feature policy)`；Evaluation：`https://arxiv.org/html/2607.06559v1#S4 (50 held-out video sequences; six real-robot tasks, 35 consecutive trials/task, 120s success bound, TIANJI M6/WUJI HAND/D435i); https://arxiv.org/html/2607.06559v1#S4.SS4 (modality/representation and policy component ablations)`；Limitations/Counterevidence：`https://arxiv.org/html/2607.06559v1#S5 (about 9Hz on RTX 5090; egocentric optimization; multi-view/multi-robot open)`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L665-L676`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `MULTIMODAL-EMBODIED-VLA` 的 [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Vision as Unified Multimodal Generation](https://arxiv.org/html/2607.06560v1)

**系统推理。** 问题是文本、图像与视频各自建模会复制语义接口并限制跨模态生成。论文以统一响应 contract 和共享表示组织生成，但作者结果只覆盖其训练数据、模型与评价，不能推出所有模态应采用同一 factorization。代价是 token budget、目标冲突、采样与 cache 路径复杂化。


<!-- claim:SF-2026-ARXIV-2607-06560:start -->Convert heterogeneous annotations into a shared sample contract—visual inputs, natural-language task/schema instruction, and a text/image/mixed response that can be deterministically decoded back into boxes, masks, dense maps or camera records—so one generative model can learn many vision tasks without task-specific heads. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-06560:end -->

**旧方案与约束变化。** `本章的核心判断是：**生成范式的差别首先是概率分解、状态可变性与 commit protocol 的差别，随后才表现为 kernel、cache 和 latency 差别。**“一次生成更多 token”不自动等于更快；“允许修正”也不自动等于更准。必须把 proposal work、verification/correction、memory、并发和输出提交一起计算。`（`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Convert heterogeneous annotations into a shared sample contract—visual inputs, natural-language task/schema instruction, and a text/image/mixed response that can be deterministically decoded back into boxes, masks, dense maps or camera records—so one generative model can learn many vision tasks without task-specific heads. 它改变 `MULTIMODAL-GENERATIVE-PARADIGMS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.06560v1#S3 (common instruction-response schema for structured vision, dense geometry, segmentation and multi-view geometry); https://arxiv.org/html/2607.06560v1#S4 (native text/image/mixed generation and typed decoding)`；Evaluation：`https://arxiv.org/html/2607.06560v1#S5 (task-family benchmarks against specialists and multimodal baselines); https://arxiv.org/html/2607.06560v1#S6 (data mixture/capability preservation and task-family analyses)`；Limitations/Counterevidence：`https://arxiv.org/html/2607.06560v1#S7 (task-specific decoding/evaluation remains; converted/pseudo targets and data mixture bound conclusions)`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L701-L712`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-GENERATIVE-PARADIGMS`。
- Books disposition：历史写回已完成；本次判定为 `已有覆盖`。

本次重新定位到 `MULTIMODAL-GENERATIVE-PARADIGMS` 的 [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

### [Lift3D-VLA: Lifting VLA Models to 3D Geometry and Dynamics-Aware Manipulation](https://arxiv.org/html/2607.06564v1)

**系统推理。** 问题是 2D VLA 表示难以稳定表达三维几何与动态。Lift3D 将 3D geometry/dynamics 引入动作条件表示；作者只在特定传感器与 manipulation 任务上证明收益，未证明跨 embodiment 或 sim-to-real。代价是标定、传感器同步、3D 表示成本和失效回退。


<!-- claim:SF-2026-ARXIV-2607-06564:start -->Authors report simulation, real-task and OOD gains under their sensor/task contract; synthesized point clouds, depth sensors and 25-rollout simulator slices do not prove general physical dynamics. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-06564:end -->

**旧方案与约束变化。** `Ch23/25/26 already separate modality-specific representation identity, RGB-D/flow predictive state, typed action chunks, calibration and contact failure. Lift3D-VLA is a bounded implementation branch, not a missing owner.`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L127`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Preserve explicit geometry while reusing a 2D foundation encoder, supervise both current/future point-cloud structure, and distribute temporal action prediction across intermediate-to-deep LLM layers. 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.06564v1#S4 (shared 2D/3D encoder with modality-specific tokenization, geometry-centric MAE and layer-wise temporal action modeling)`；Evaluation：`https://arxiv.org/html/2607.06564v1#S5 (MetaWorld/RLBench, component ablations, 8 real tasks and OOD object/light/background tests)`；Limitations/Counterevidence：`https://arxiv.org/html/2607.06564v1#S5.SS6 (pour-direction, grasp, contact and depth-related failure cases); https://arxiv.org/html/2607.06564v1#S6 (transparent/reflective depth failure and missing fine contact closed loop)`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`已有覆盖`。

本次重新定位到 `MULTIMODAL-EMBODIED-VLA` 的 [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有正文命题与证据边界已承载该 family，本任务不重复追加，独立复核已确认 body anchor。

所有性能数字仅在原文披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator 范围内解释；未披露字段保持 `Not Disclosed`，本次没有把作者 benchmark 写成通用生产结论。

## 5. 缺口与下一步

无

本窗没有外部材料请求或待执行工作；非作者独立语义复核已确认已有 Books 段落是机制正文，而非只有 trace。

## 6. 复核

复核者：主任务独立复核（非本报告作者）

结论：通过

独立复核逐项检查 17 个候选的窗口、exact-v1、评分、证据边界和 Books 路由，并核对 execution、memory、evaluation/security、World Model/VLA、Training Data、KV 与生成范式正文。三个排除项按局部应用、重复机制和缺少长期边界变化复查，未发现漏掉的系统性增量。格式校验与 `git diff --check` 通过。
