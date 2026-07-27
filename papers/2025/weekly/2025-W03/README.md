# AI Research Weekly — 2025-W03

> Coverage Window: 2025-01-13～2025-01-19
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 2 项与长期 AI System 认知相关的证据：MiniMax-01、PRESERVE。重点不是记录发布热度，而是识别其改变了哪一项约束、机制与系统 trade-off。所有结论均按首次公开时间归档，性能或能力数字不脱离作者披露的模型、硬件、精度、输入输出、并发与 SLO 条件使用。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；访问日期统一为 2026-07-31。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：MiniMax-01（2025-01-14）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 保留：PRESERVE（2025-01-14）。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| MiniMax-01 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；Books Integration 前全文复核 |
| PRESERVE | 4 | 3 | 3 | 4 | 4 | 3 | 21/30 | Worth Watching；保留为通信/内存协同案例 |

### Deep Analysis 1 — MiniMax-01

- First Public: 2025-01-14
- Status: arXiv v1 / open weights
- Primary Source: https://arxiv.org/abs/2501.08313
- Evolution Relationship: Layering / Dependency

#### Why

长上下文扩展同时受到注意力复杂度、训练稳定性与跨卡通信约束；只替换 attention kernel 不能独立解决系统问题。

#### Principle and Mechanism

论文把 Lightning Attention、少量 softmax attention、MoE 与 sequence parallel 组合为混合架构，主张以线性注意力承担大部分长序列计算，并周期性保留 softmax attention 的内容寻址能力。

#### Trade-off and Evidence Boundary

线性状态降低随序列增长的计算与存储压力，但压缩历史会损失精确内容访问；混合层恢复表达力，同时重新引入二次复杂度与实现分支。作者长上下文数字不得脱离模型、硬件和测试设置外推。

#### Connection and Evolution

知识树位置：第 14、21、22、24、32 章。Must Read；Books Integration 前全文复核。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 2 — PRESERVE

- First Public: 2025-01-14
- Status: arXiv v1; Experimental
- Primary Source: https://arxiv.org/abs/2501.08192
- Evolution Relationship: Principle Reuse

#### Why

多卡推理同时受 HBM 读取与 collective 阻塞，关键不是单独加速某条路径，而是让数据搬运和通信重叠。

#### Principle and Mechanism

论文预取权重与 KV cache，并把内存读取隐藏在 collective communication 后；这是 dataflow overlap 的受限实例。

#### Trade-off and Evidence Boundary

重叠依赖可预测的执行顺序、额外 buffer 与硬件缓存配置；作者结果来自特定加速器，尚不能写成通用 runtime 结论。

#### Connection and Evolution

知识树位置：第 32、45、50、52 章。Worth Watching；保留为通信/内存协同案例。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### MiniMax-01

- **Candidate / Week / Score:** MiniMax-01 / 2025-W03 / 25/30。
- **Source Family ID:** `minimax01-hybrid-linear-attention-moe`。
- **Source Type:** 官方 technical report / arXiv 作者论文与开源权重说明。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-14 提交；截至访问日仅 v1。
- **Direct Primary Sources:** arXiv abstract、68 页 PDF 全文、官方链接的 repository/model artifacts，
  https://arxiv.org/abs/2501.08313；https://arxiv.org/pdf/2501.08313。
- **Related Primary Sources:** Lightning Attention 与 LASP 的原始论文由本报告 related-work/method
  回链；本 Packet 只把 MiniMax-01 实际采用的组合写为作者实现事实。
- **Access and Verification Status:** Verified；论文全文、公式、system design、evaluation 和
  ablation 可访问。训练数据细节和若干生产 serving 条件未完整公开。
- **Full-read Coverage:** 已读 metadata、Introduction/Background/Related Work、Lightning Attention
  method 与 tiling、hybrid architecture、MoE、training/inference parallelism、communication overlap、
  long-context curriculum、text/VL evaluation、ablation、efficiency、limitations/conclusion 与关键 appendix。
- **Original Problem:** dense softmax attention 的 pair compute 和中间状态随序列二次增长；纯 linear
  attention 虽以 recurrent summary 降低复杂度，却弱化精确 token retrieval；MoE 又增加 expert
  dispatch 与训练通信压力。
- **Why the Previous Design Was Reasonable:** dense attention 对任意位置内容寻址最直接，成熟 kernel
  与模型质量证据充分；pure linear/recurrent route 在长流式执行中具有有界 state 和线性成本。
- **Changed Constraint:** 模型希望同时扩展 active context、total parameter capacity 和训练/推理
  throughput，单独替换 attention kernel 无法处理 MoE、sequence parallel 与通信重叠。
- **Mechanism:** 80-layer text model 以 7 个 Lightning Attention block 配 1 个 softmax block 的
 周期混合；Lightning Attention 通过分块/tiling 维护 recurrent `K^T V` state，避免 materialize
  完整 attention matrix；32 experts、top-2 routing 的 MoE 提供 456B total/45.9B active parameters。
- **State Ownership:** linear attention recurrent state 与 periodic softmax KV 由每个 sequence/request
  拥有；expert weights 按 expert/tensor parallel layout 由 ranks 拥有；router 决定 token-to-expert
  dispatch。它们不是可互换的“长上下文状态”。
- **Control Flow / Data Flow:** tokens 经 Lightning blocks 更新压缩 state，每第八层进入 softmax
  attention 恢复内容寻址；MoE router 产生 top-2 assignments，经 All-to-All dispatch 到 experts、
  grouped computation 后 combine；长序列在 LASP/ring/sequence-parallel 路径中分片。
- **Implementation Details:** 报告披露 Lightning tiling、LASP、tensor/expert/sequence parallel、
  expert tensor parallel、global routing 与 compute-communication overlap；具体生产 scheduler、
  failure recovery 和跨请求 state lifecycle 不属于论文范围。
- **Evaluation Setup:** 通用文本、reasoning/coding、long-context retrieval/understanding 与 multimodal
  benchmarks；长上下文训练扩展到 1M tokens，并报告 inference extrapolation；包含 pure-linear vs
  hybrid、层比例、parallel scaling 和 context-length 相关实验。
- **Baselines / Ablations / Sensitivity:** 与 dense/open/proprietary model results 比较；ablation 表明
  pure linear attention 在若干能力上不足，周期 softmax layer 是质量补偿。厂商 benchmark 的
  prompt/evaluator 差异使跨模型数字不能视为严格同条件结论。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 报告的 inference memory/
  prefill 案例使用 8×H800、W8A16，并讨论 1M context；模型为 456B total/45.9B active。统一 batch、
  online concurrency、TTFT/TPOT SLO 未对全部结果披露，因此不把“4M”或速度数字写成通用能力。
- **What the Evidence Actually Proves:** 在作者系统中，linear/softmax hybrid、MoE 与多维并行可以
  共同训练/运行超长 context，并且 periodic softmax 对 pure linear 的内容访问缺口有实验支撑。
- **What It Does Not Prove:** 不证明固定 7:1 比例适用于其他模型/硬件，不证明 1M training 或 4M
  extrapolation 等于全范围有效利用，也不证明 linear attention 普遍替代 dense attention。
- **Limitations / Threats to Validity:** 单一团队训练与评测；proprietary data 与部分 engineering
  细节未披露；长上下文 benchmark 不能覆盖真实多租户 serving、知识正确性和 recovery。
- **Trade-offs / New Failure Modes:** pair compute 降低，但 recurrent compression 带来信息丢失；
  periodic softmax 恢复质量同时重引二次路径；MoE 引入 routing imbalance、All-to-All、expert
  capacity 与 topology sensitivity；多维并行增加 layout 和 checkpoint complexity。
- **Where the Previous Design Still Applies:** 对精确任意位置依赖、较短 context 或成熟 kernel 优先的
  workload，dense attention 仍合理；pure recurrent path 适合可容忍压缩误差的低成本流式任务。
- **Evolution Relationship:** `Layering / Dependency`：不是单一 attention 后继，而是 linear attention、
  periodic dense access、MoE 与 distributed runtime 的共同分层。
- **ROADMAP Node:** Ch22 主 owner；Ch14/21 给出 attention/MoE 前提；Ch32 解释多维并行与通信。
- **Target and Adjacent Chapters Read:** 已读 Ch14、Ch21、Ch22、Ch23 及 Ch31～33；并核对 Ch39、
  Ch41、Ch50 的 prefill/KV/memory contract。
- **Existing Coverage:** Ch22 已包含 hybrid linear/softmax 的演进、7:1 只是论文实例、pure linear
  边界和系统 trade-off；仍需在全 Evidence Gate 后确认表述没有把作者 extrapolation 外推。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch22，沉淀 hybrid linear/softmax 的共存边界。
  benchmark 清单写入 Books。
- **Changed Files or Rejection Reason:** 已复核 `books/part-02-model/22-long-context.md`；不保留型号 benchmark。
- **Open Questions:** hybrid ratio 如何随 memory hierarchy、retrieval distribution 与 SLO 改变；
  recurrent state 的 serving isolation、prefix reuse 与失败恢复是否有公开实现证据。

### PRESERVE

- **Candidate / Week / Score:** PRESERVE / 2025-W03 / 21/30。
- **Source Family ID:** `preserve-comm-memory-overlap-prefetch`。
- **Source Type:** arXiv 作者论文（Experimental；后续 EuroSys 2026 metadata 出现在 v2 页面）。
- **First-public Date / Revision History:** v1 2025-01-14；v2 2025-05-26。
- **Direct Primary Sources:** arXiv v2 HTML/abstract，https://arxiv.org/abs/2501.08192；
  https://arxiv.org/html/2501.08192。
- **Related Primary Sources:** 论文引用的 torch-npu、TorchDynamo、CANN Graph Engine/torchair 官方
  implementation context；没有公开通用 CUDA/NVIDIA implementation 可核验。
- **Access and Verification Status:** Verified for paper claims；method、实验、DSE 与 limitations 可读。
  跨硬件 portability 尚未验证。
- **Full-read Coverage:** 已读 metadata/revisions、Introduction、inference/TP background、method、
  graph insertion algorithm、framework integration、experimental setup/results、batch/length sensitivity、
  fused-kernel baseline、design-space exploration、related work、limitations、conclusion 与 scale-out appendix。
- **Original Problem:** tensor-parallel decode 同时受 HBM weight/KV reads 与 AllReduce latency 限制；
  GEMM-AllReduce fusion 只能覆盖相邻、有数据依赖允许的局部路径，难以处理相隔多个 op 的 KV reads。
- **Why the Previous Design Was Reasonable:** compute-communication overlap 直接利用 GEMM 与 collective
  的并行机会，kernel fusion 对稳定图和支持硬件可获得低 overhead；正常 cache hierarchy 也避免了
  显式 prefetch 的污染风险。
- **Changed Constraint:** decode 低 operational intensity、KV 随 context 增长，且 accelerator on-chip
  cache 变大，使“在 collective 等待期间搬下一层只读数据”成为新的 overlap 空间。
- **Mechanism:** compiler/graph optimizer 搜索 communication op 后的 MatMul/SelfAttention，估计将
  weight/KV 从 HBM 预取到 L2 的容量；只有 cumulative size 小于阈值时才插入 parallel-stream
  prefetch，并用 events 与主 stream 同步，避免 cache eviction/pollution。
- **State Ownership:** weights 为 model-replica read-only state；decode KV 属 request state、除最新
  entry 外在读取时只读；L2 residency 是 accelerator-local ephemeral cache state；graph optimizer
  拥有 insertion decision。
- **Control Flow / Data Flow:** host code→TorchDynamo/vendor compiler IR→graph optimizer 插入 prefetch→
  offline executable；runtime collective 在主 stream 运行时，parallel stream 搬 weight/KV 到 L2，
  event 后 compute 消费 cache-resident data。
- **Implementation Details:** 在 torch-npu/torchair、CANN Graph Engine 上实现；BFS 遍历至下一
  communication boundary，按 L2 capacity 停止插入。不是通用 runtime 自动保证。
- **Evaluation Setup:** Llama3-8B/70B、Qwen2-7B/72B、Phi-3-small/medium；batch 1～64、sequence 2K～32K；
  static equal-length batching，prefill/decode 取总长 2/3 与 1/3。
- **Baselines / Ablations / Sensitivity:** vanilla、PRESERVE 与 compute-communication fused kernels；
  检查 NPU 数、batch、sequence、KV heads/device、L2 capacity、network bandwidth 与 throughput-area DSE。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Huawei Atlas 800T A2，8×Ascend
  910B（64GB HBM、192MB L2、HCCS full mesh），weights/activations int8；主表 batch 4、16K max length。
  online concurrency、dynamic batching 和明确 TTFT/TPOT SLO 未评测。
- **What the Evidence Actually Proves:** 在上述 Ascend/CANN/static workload 中，显式 prefetch 可把
  一部分 HBM read 隐藏在 collective 后，收益随 model、TP degree、KV head layout、batch/length 和
  cache 容量显著变化；作者报告范围为 1.09×～1.61×。
- **What It Does Not Prove:** 不证明所有 GPU/NPU、dynamic batching、PCIe/IB scale-out 或任意 graph
  compiler 都能获得同样收益；也不证明“communication 越慢收益越高”。
- **Limitations / Threats to Validity:** 单一 vendor stack 与单机 full-mesh；静态等长 batch；需要
  足够 L2，prefetch 本身消耗 HBM bandwidth，cache pollution 可能反向减速；DSE 是模型化结果。
- **Trade-offs / New Failure Modes:** 用 L2 capacity 与额外 memory traffic 换 overlap；错误容量估计、
  dynamic shape、competing kernels/cache tenants、event synchronization 与 graph invalidation 都可能
  让预取失效或减速。
- **Where the Previous Design Still Applies:** compute-communication fused kernels 适合紧邻 op 且有
  成熟 kernel 的路径；无可隐藏 collective、L2 太小或高 batch compute-bound 时普通 execution 更合理。
- **Evolution Relationship:** `Principle Reuse`：dataflow overlap 从 compute↔communication 扩展到
  memory-read↔communication，不是通用新 collective algorithm。
- **ROADMAP Node:** Ch50 memory hierarchy 主 owner 候选；Ch32 collective/overlap 前提；Ch45 只作
  vendor execution-plan handoff；Ch52 负责 workload/SLO 调度边界。
- **Target and Adjacent Chapters Read:** 已读 Ch31～33、Ch45～47、Ch49～52。
- **Existing Coverage:** Ch32/Ch50 已有 overlap 与 memory hierarchy 原则，但没有这一受限 graph-
  inserted prefetch case；是否值得正文案例需等 75/75 去重，且不能写成跨硬件事实。
- **Integration Decision:** `Weekly Only — Experimental Hardware-specific Case`；受限 graph/hardware path 未形成通用设计结论。
  除非后续候选形成跨来源的 memory/communication evolution chain。
- **Changed Files or Rejection Reason:** 不改 Books；缺跨硬件、真实 serving workload 与独立复现。
  dynamic-serving evidence 不足，现有章节已覆盖上位原则。
- **Open Questions:** CUDA/ROCm 可移植实现、dynamic batching 下的 cache model、multi-node link
  sensitivity、prefetch contention 与 correctness/fallback contract。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- MiniMax-01 → 第 14、21、22、24、32 章（Layering / Dependency）
- PRESERVE → 第 32、45、50、52 章（Principle Reuse）

## Recommended Action

- MiniMax-01：Must Read；Books Integration 前全文复核
- PRESERVE：Worth Watching；保留为通信/内存协同案例

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 新增 papers/2025/weekly/2025-W03/README.md。
- 更新 books/part-02-model/22-long-context.md。

## Open Questions

- MiniMax-01 的混合比例是否会随硬件 memory hierarchy 与 retrieval workload 改变，仍需更多独立证据。
- PRESERVE 的 portability、buffer overhead 与失败回退尚不足以形成跨硬件结论。

## Sources

- MiniMax-01 — https://arxiv.org/abs/2501.08313（First Public: 2025-01-14；Accessed: 2026-07-31）
- PRESERVE — https://arxiv.org/abs/2501.08192（First Public: 2025-01-14；Accessed: 2026-07-31）
