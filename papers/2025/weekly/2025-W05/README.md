# AI Research Weekly — 2025-W05

> Coverage Window: 2025-01-27～2025-02-02
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 3 项与长期 AI System 认知相关的证据：vLLM V1 Alpha、s1: Simple test-time scaling、OpenAI deep research。重点不是记录发布热度，而是识别其改变了哪一项约束、机制与系统 trade-off。所有结论均按首次公开时间归档，性能或能力数字不脱离作者披露的模型、硬件、精度、输入输出、并发与 SLO 条件使用。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；访问日期统一为 2026-07-31。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：OpenAI deep research（2025-02-02）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 保留：s1: Simple test-time scaling（2025-01-31）。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 保留：vLLM V1 Alpha（2025-01-27）。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| vLLM V1 Alpha | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Must Read；优先 refine 第 46 章而非复制版本清单 |
| s1: Simple test-time scaling | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Worth Watching；等待与后续 test-time scaling 证据串联 |
| OpenAI deep research | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Worth Watching；只保留系统问题，不写实现推断 |

### Deep Analysis 1 — vLLM V1 Alpha

- First Public: 2025-01-27
- Status: Official alpha architecture
- Primary Source: https://vllm.ai/blog/2025-01-27-v1-alpha-release
- Evolution Relationship: Direct Evolution

#### Why

V0 累积的 feature-specific execution paths 使 request state、scheduler 和 workers 难以共同演化；继续局部打补丁会放大控制面复杂度。

#### Principle and Mechanism

V1 合并 execution loop，简化 scheduler，重构 input preparation、tensor-parallel worker path，并把 prefix caching、torch.compile 与 piecewise CUDA Graph 放进统一执行架构。

#### Trade-off and Evidence Boundary

统一状态机降低长期复杂度，但 alpha 重构带来兼容性、覆盖率和迁移风险；prefix cache 的控制面开销降低不等于所有 workload 都有命中收益。

#### Connection and Evolution

知识树位置：第 38～43、46、50、52 章。Must Read；优先 refine 第 46 章而非复制版本清单。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 2 — s1: Simple test-time scaling

- First Public: 2025-01-31
- Status: arXiv v1; Experimental
- Primary Source: https://arxiv.org/abs/2501.19393
- Evolution Relationship: Principle Reuse

#### Why

reasoning 能力不只由训练规模决定；小而高质量的监督集合与 inference-time budget policy 也能改变模型表现。

#### Principle and Mechanism

论文构造 1,000 个样本的 s1K，并用 budget forcing 控制模型继续思考或提前结束。

#### Trade-off and Evidence Boundary

方法简单且可复现，但结论集中在数学 reasoning 与单一模型族；延长 token budget 会增加延迟和成本，且可能导致 overthinking。

#### Connection and Evolution

知识树位置：第 25、29、62 章。Worth Watching；等待与后续 test-time scaling 证据串联。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 3 — OpenAI deep research

- First Public: 2025-02-02
- Status: Official product/research preview
- Primary Source: https://openai.com/index/introducing-deep-research/
- Evolution Relationship: Layering / Dependency

#### Why

开放式研究任务需要把浏览、证据选择、迭代与综合组织成长时运行的 agent workflow。

#### Principle and Mechanism

官方材料证明产品形态和评测设置，但未完整公开 planner、browser policy、state ownership 与 failure recovery。

#### Trade-off and Evidence Boundary

长时 autonomous workflow 提升覆盖面，也放大来源污染、停止条件、成本、可追溯性与误引风险；产品 benchmark 不能直接沉淀为通用架构。

#### Connection and Evolution

知识树位置：第 72、74～77、80 章。Worth Watching；只保留系统问题，不写实现推断。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### vLLM V1 Alpha

- **Candidate / Week / Score:** vLLM V1 Alpha / 2025-W05 / 28/30。
- **Source Family ID:** `vllm-v0-to-v1-runtime`；与 W02 retrospective 联读。
- **Source Type:** 官方项目 architecture/release Blog + linked open-source repository/code paths。
- **First-public Date / Revision History:** 2025-01-27；文章记录 alpha 当时状态，后续 vLLM 版本行为
  必须另按 release/code 核验，不能反写为 alpha 原始事实。
- **Direct Primary Sources:** https://vllm.ai/blog/2025-01-27-v1-alpha-release；文章链接的 vLLM
  repository、V1 design/code references 与 benchmark configuration。
- **Related Primary Sources:** W02 官方 2024 retrospective/2025 vision 负责重构动机，不证明 V1 机制。
- **Access and Verification Status:** Verified for alpha architecture；Blog 与开源链接可访问。当前最新
  vLLM 行为不由该历史来源证明。
- **Full-read Coverage:** 已读 V0 problem statement、V1 system architecture、API server/EngineCore、
  scheduler/KV cache manager、worker request state、persistent batch、multimodal input/cache、
  prefix caching、torch.compile/piecewise CUDA graph、FlashAttention 3、benchmark setup、feature gaps、
  hardware support 与 migration caveats，并核对 linked code/design descriptions。
- **Original Problem:** V0 的 prefill/decode 和 feature-specific paths 分别演化，scheduler、input
  preparation、worker state 与 GPU batch 更新产生重复控制逻辑和 CPU overhead，阻碍 feature composition。
- **Why the Previous Design Was Reasonable:** 在早期快速加入 PagedAttention、continuous batching、
  speculative decoding 等能力时，分路径实现容易迭代并保留稳定用户；V0 在 feature parity 和旧硬件上
  仍有生产价值。
- **Changed Constraint:** feature 数量、multimodal model、prefix reuse、compile/CUDA graph 与高并发
  使“每个 feature 一条 loop”无法继续扩展；CPU orchestration 也开始限制 GPU utilization。
- **Mechanism:** API server 与独立 EngineCore 分离；scheduler 不再把 prefill/decode 当两种请求，
  每轮只为 request 分配 `num_tokens`，统一 chunked prefill、decode 与 prefix-cache resume；KV cache
  manager 分配 blocks。worker 保留 request-local state，control plane 只发送新增/完成等 diffs；
  Persistent Batch 原地更新 GPU input tensors；execution 用 torch.compile + piecewise CUDA graphs。
- **State Ownership:** API server 拥有 client/protocol state；EngineCore scheduler/KV manager 拥有全局
  request scheduling 与 logical block allocation；worker model runner 拥有 request execution state 和
  persistent GPU batch tensors；KV blocks 属 request/prefix-cache 生命周期。
- **Control Flow / Data Flow:** request→API preprocessing→EngineCore queue；每 iteration scheduler 选择
  requests/token counts 与 blocks→diff 发送 worker→persistent batch 更新→compiled/graph execution→
  sample result 回 scheduler/API；完成请求释放或缓存 state。
- **Implementation Details:** prefix caching 默认启用；multimodal preprocessing cache 与 encoder cache
  进入 unified path；FlashAttention 3、torch.compile、piecewise CUDA graph 减少 kernel/launch overhead；
  alpha 当时仅 NVIDIA Ampere+，feature parity 明确未完成。
- **Evaluation Setup:** 官方比较 V0/V1 serving throughput/latency，覆盖若干 models、input/output length
  与 concurrency；文章报告最高约 1.7×，但不是所有 workload 的稳定下界或独立结果。
- **Baselines / Ablations / Sensitivity:** V0 为主要 baseline；性能归因涉及 scheduler、compile、CUDA
  graph、persistent batch 等组合，缺少把每项机制完全独立的 ablation，因此不能给单项收益因果。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** benchmark 细节以文章配置为准；
  alpha support 为 NVIDIA Ampere+。不同结果的 model、length、concurrency 不应合并，正文不保留 1.7×；
  未建立跨 workload 统一 TTFT/TPOT/goodput contract。
- **What the Evidence Actually Proves:** 官方 alpha architecture 明确把调度对象统一为“每 request 本轮
  token 数”，并通过 state ownership + diff 更新减少 CPU control work；这是 request state machine 的
  结构演进，不只是新 kernel 清单。
- **What It Does Not Prove:** 不证明 V1 alpha feature complete、对所有模型更快或可无风险替代 V0；
  默认 prefix caching 不保证命中，compile/graphs 也不消除 dynamic-shape 与 memory trade-offs。
- **Limitations / Threats to Validity:** 项目自测；alpha 缺 encoder-decoder、Mamba、embedding，以及
  当时部分 logprobs、pipeline parallel、structured output、spec decode、metrics、LoRA；仅特定硬件。
- **Trade-offs / New Failure Modes:** unified loop 降低 path explosion，却把 correctness 集中到 shared
  scheduler/KV manager；duplicated worker state + diffs 引入 lost/out-of-order update、reconciliation、
  cancellation 与 recovery 问题；persistent batch 增加 slot compaction/stale tensor 风险；V0/V1 并存
  带 migration 与 observability 差异。
- **Where the Previous Design Still Applies:** V0 对缺失 feature、旧硬件、已有 integration 与迁移期
  production workload 仍合理；分离 prefill/decode 专用 engine 在极端 workload 或 PD architecture 中
  仍可作为 deployment decomposition。
- **Evolution Relationship:** `Direct Evolution`：V0 feature-specific loops→V1 unified token scheduler +
  explicit state ownership；不是“prefill/decode 已不再有物理差异”。
- **ROADMAP Node:** Ch46 主 owner；Ch38～43 给 phase/KV/batch 前提；Ch50/52 负责 memory 与 scheduling
  contract；不把具体 alpha feature list扩散到多章。
- **Target and Adjacent Chapters Read:** 已读 Ch38～47 与 Ch50～52，重点核对 Ch42、43、46、52。
- **Existing Coverage:** Ch46 已有 vLLM runtime 机制，但需在 Evidence Gate 后核对是否完整呈现
  V0→V1 control/state evolution，而不是只描述当前流程。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch46，补齐 V0→V1 的 control/state 演进。
  state owner/diff 与迁移 trade-off。
- **Changed Files or Rejection Reason:** 已更新 `books/part-04-inference-system/46-vllm.md`，保留 V0 与 alpha feature-gap 适用条件。
- **Open Questions:** diff reconciliation/cancellation semantics、EngineCore failure recovery、prefix cache
  invalidation、V0/V1 equivalence evidence，以及后续 release 是否改变这些 alpha contracts。

### s1: Simple test-time scaling

- **Candidate / Week / Score:** s1 / 2025-W05 / 24/30。
- **Source Family ID:** `s1-budget-forcing-test-time-scaling`。
- **Source Type:** arXiv 作者论文 + 官方开源 code/data/model。
- **First-public Date / Revision History:** v1 2025-01-31；v2 2025-02-03；v3 2025-03-01；按 v3 复核。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.19393；
  https://arxiv.org/pdf/2501.19393；https://github.com/simplescaling/s1。
- **Related Primary Sources:** Qwen2.5 technical report 为 base model contract；Gemini Thinking traces 是
  distilled data source，不证明 s1 自身发现了全部 reasoning behavior。
- **Access and Verification Status:** Verified；46 页论文、code/data links、methods、evaluation、ablation、
  discussion/limits 与 appendices 可访问。
- **Full-read Coverage:** 已读 metadata/revisions、Introduction/Related Work、59K→s1K curation、
  decontamination、budget forcing、control/scaling/performance metrics、training/evaluation、data/method
  ablations、limits、parallel alternatives、impact statement 与核心 appendices/hyperparameters。
- **Original Problem:** test-time compute scaling 的公开复现常依赖大规模 RL/search；问题是少量 curated
  SFT data 加简单 decoding intervention 是否足以产生可控的 sequential scaling。
- **Why the Previous Design Was Reasonable:** 普通 EOS 让模型自行决定 reasoning length，保持自然分布；
  prompt length-control 不改 decoder；parallel majority/Best-of-N 易于扩展并能减少单 trajectory failure。
- **Changed Constraint:** 需要显式控制 inference token budget，且希望以小训练预算验证 scaling behavior，
  而不是复现完整 frontier RL stack。
- **Mechanism:** 从 59,029 questions 按 quality、difficulty、diversity 筛到 1,000 s1K，reasoning traces
  来自 Gemini Flash Thinking；在 Qwen2.5-32B-Instruct 上 SFT。budget forcing 在超过上限时强制
  end-of-thinking delimiter，在模型欲结束但未达下限时抑制 delimiter 并追加 “Wait”。
- **State Ownership:** training dataset/trace lineage 由 SFT pipeline 拥有；decoder/runtime 拥有当前
  reasoning prefix、token budget 和 forced delimiter state；它不是持久 planning/workflow state。
- **Control Flow / Data Flow:** prompt→autoregressive reasoning→runtime 检查 thinking tokens/EOS→force stop
  或 append Wait→继续 decode→final answer；parallel baseline 生成多 trajectories 后 vote/reward select。
- **Implementation Details:** Qwen2.5-32B-Instruct，16×H100、PyTorch FSDP，SFT 26 minutes；data 使用
  8-gram eval decontamination。s1K 仍只有 53.6% samples 被 grader 判正确，论文将其视为学 reasoning
  process 的实验选择而非无噪声标签。
- **Evaluation Setup:** AIME24（30 questions）、MATH500、GPQA Diamond；thinking-token budget 为 compute
  proxy；定义 Control、average Scaling slope、maximum Performance；比较 token/step/class conditional、
  rejection sampling、budget forcing、majority voting 与 REBASE。
- **Baselines / Ablations / Sensitivity:** random/longest/diversity-only/full-59K data selections；不同 forcing
  strings；max/min budget；Qwen base与其他 reasoning models；论文发现 prompt step control 可通过改变
  每步长度规避约束，rejection sampling 还可能偏向“长而错误”trajectory。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** training hardware 为16×H100；
  model 32B；precision、global batch 与 serving concurrency/TTFT SLO 未形成完整 contract。AIME 从50%
  到57%发生在特定 forcing/token 设置，不能外推到开放任务。
- **What the Evidence Actually Proves:** 在 s1-32B 与三个 reasoning benchmarks 上，runtime 可直接
  控制 sequential token budget，并在一定范围观察正 scaling；curated 1K SFT 可激活 base model 已有
  reasoning behavior，data selection ablation 支持质量/难度/多样性的组合价值。
- **What It Does Not Prove:** 不证明 1K examples 普遍足够，不证明追加“Wait”提供新的可靠 reasoning
  algorithm，不证明更多 tokens 单调提高质量，也不证明 hidden reasoning faithful 或适用于开放域。
- **Limitations / Threats to Validity:** budget forcing 最终 plateau，并受 context window 限制；长生成可
  overthink/repeat/超窗；AIME 样本仅 30；base model 与 distilled Gemini traces 贡献难完全分离；
  reward-model tree search额外计算未计入 token proxy。
- **Trade-offs / New Failure Modes:** 获得硬 token controllability，却增加 latency/cost、forced-stop 截断、
  loop/repetition、overthinking 与 output-quality variance；parallel methods跨固定 window 扩展但增加
  aggregate compute 和 verifier dependency。
- **Where the Previous Design Still Applies:** unconstrained EOS 适合普通低延迟回答；parallel sampling 在
  可并行、可验证任务中仍有效；RL/search 在需要 learned policy 或更远 extrapolation 时仍可能必要。
- **Evolution Relationship:** `Principle Reuse`：training-time reasoning policy 与 inference-time compute
  budget 分离；不是 R1/k1.5 的替代路线。
- **ROADMAP Node:** Ch20 sampling/runtime control 与 Ch29 reasoning training 的边界；Ch52 负责 serving
  token budget；Ch62 负责 evaluation contract。
- **Target and Adjacent Chapters Read:** 已读 Ch19～22、Ch24～30、Ch38～42、Ch52、Ch62；重点核对
  Ch20/29/52 的 owner。
- **Existing Coverage:** 现有章节已强调 token budget、reasoning reward 与调度，但未明确 budget forcing
  的“control≠quality”案例；是否写入取决于后续 test-time scaling source family 去重。
- **Integration Decision:** `Refine — Existing Argument`；Ch20 拥有 stopping policy，Ch52 拥有 capacity/evaluation identity。
  Experimental Case`，不能仅凭 24/30 强行修改 Books。
- **Changed Files or Rejection Reason:** 已更新 `books/part-02-model/20-sampling.md` 与 `books/part-04-inference-system/52-inference-scheduling.md`。
- **Open Questions:** 跨 model/domain scaling、forced token 的 calibration、reasoning-token vs real GPU
  cost、overthinking detection 与 SLO-aware adaptive budget policy。

### OpenAI deep research

- **Candidate / Week / Score:** OpenAI deep research / 2025-W05 / 23/30。
- **Source Family ID:** `openai-deep-research-product-workflow`。
- **Source Type:** 官方 product/research preview + system behavior/benchmark disclosure；无公开 technical paper
  或 repository。
- **First-public Date / Revision History:** 2025-02-02 发布；页面包含后续 availability updates，原始
  release fact 与后改文案必须区分。
- **Direct Primary Sources:** https://openai.com/index/introducing-deep-research/ 及页面链接的官方
  benchmark/method descriptions。
- **Related Primary Sources:** 页面引用 Humanity's Last Exam、GAIA 等 benchmark；它们定义 evaluation，
  不公开产品内部 planner/runtime。
- **Access and Verification Status:** Verified as official product fact；`Mechanism Not Disclosed` for planner、
  browser policy、state store、retry/recovery 与 production topology。
- **Full-read Coverage:** 已读 announcement、training description、user workflow、tool/file/browser behavior、
  latency expectation、benchmark tables/footnotes、limitations、access/safety说明与页面 updates；不存在可
  全文阅读的 technical report/code。
- **Original Problem:** 开放研究需要跨大量网页和文件进行搜索、取证、比较与综合，单次 RAG/query 或
  短请求难承载长时 trajectory 与来源追踪。
- **Why the Previous Design Was Reasonable:** 人工 research/browser workflow 对来源权威、停止条件和
  纠错有强监督；普通 search+RAG 延迟低、易控制；短 agent loop 失败半径小。
- **Changed Constraint:** 用户愿意以 5～30 分钟 latency 换取更广 source coverage，并要求可回链引用、
  文件分析和多步工具使用。
- **Mechanism:** 官方只披露模型以 end-to-end RL 在 browsing/reasoning tasks 上训练，能够规划/执行
  multi-step trajectory、backtrack、浏览用户文件、使用 Python，并输出带 citations 的报告。
  planner decomposition、retrieval ranking、state schema 与 recovery algorithm 均 Not Disclosed。
- **State Ownership:** product 必然存在 run/tool/result state 是系统推断，官方页面未定义 owner、
  durability、identity、lease 或 authoritative transition；因此 Books 不得写成实现事实。
- **Control Flow / Data Flow:** 官方可观察行为是 user prompt/files→异步 research run→web/Python actions→
  cited synthesis；内部具体分支、parallelism、retry、human approval 与 artifact store 不公开。
- **Implementation Details:** Not Disclosed；不能从 UI 的“进度”或 5～30 分钟反推出 workflow engine。
- **Evaluation Setup:** 官方报告 GAIA 与 Humanity's Last Exam 等结果，部分 run 使用 browsing/Python；
  vendor model、tool access 与 benchmark scoring 条件需按表注读取。
- **Baselines / Ablations / Sensitivity:** 页面展示模型对比，但无公开 planner/tool ablation、cost/latency
  sensitivity 或 independent replication；产品不断更新也影响可复现性。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** hardware、precision、context length、
  batch/concurrency Not Disclosed；用户可观察 latency 约5～30分钟，但不是 availability/tail SLO。
- **What the Evidence Actually Proves:** 截至发布日期，官方提供一个可执行长时 web/file/Python research
  trajectory 并返回 citations 的产品；官方承认仍会 hallucinate、错误推断、难区分权威信息与 rumor，
  且 confidence calibration 较弱。
- **What It Does Not Prove:** 不证明内部采用特定 planner/workflow architecture，不证明 citations 与
  claims 必然 entail，不证明 benchmark 代表真实研究质量或 autonomy safety。
- **Limitations / Threats to Validity:** 厂商自报、模型/产品持续变化、内部机制与运行资源未披露；引用
  格式可能错误，source authority 与 inference errors 仍存在；compute-intensive 且 latency 长。
- **Trade-offs / New Failure Modes:** 更广搜索和长 trajectory 换来成本、stale/poisoned sources、错误
  累积、停止条件、citation mismatch、run cancellation/recovery 与权限/egress 风险。
- **Where the Previous Design Still Applies:** 快速/确定性 query、已知 corpus 与高风险结论更适合
  conventional search/RAG + human verification；固定 workflow 在任务结构稳定时更可预测。
- **Evolution Relationship:** `Layering / Dependency`：product capability 建立在 browsing、tool execution、
  evidence synthesis 与长时 orchestration 的组合上；不能把模型能力与 workflow runtime 混为一谈。
- **ROADMAP Node:** Ch77 workflow 负责长期原则；Ch72 retrieval/citation；Ch74 tool calling；Ch80 platform。
- **Target and Adjacent Chapters Read:** 已读 Ch71～80，重点 Ch72、74～77、80。
- **Existing Coverage:** Ch72 已覆盖 source authority/citation entailment；Ch77 已定义 durable workflow
  state、retry/budget/recovery；Ch80 已覆盖 run identity/evidence。公开来源没有新增可验证内部机制。
- **Integration Decision:** `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`；产品 workflow 不能反推内部 orchestration。
  Disclosed`，不修改 Books。
- **Changed Files or Rejection Reason:** 不改 Books；Ch72/74/77/80 已有 source、tool、workflow 与 platform ownership contract。
  现有长期 framework 已覆盖可观察风险。
- **Open Questions:** planner/state/recovery contract、citation entailment evaluation、source trust policy、
  tool sandbox/egress、cost/tail latency 与 run cancellation semantics。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- vLLM V1 Alpha → 第 38～43、46、50、52 章（Direct Evolution）
- s1: Simple test-time scaling → 第 25、29、62 章（Principle Reuse）
- OpenAI deep research → 第 72、74～77、80 章（Layering / Dependency）

## Recommended Action

- vLLM V1 Alpha：Must Read；优先 refine 第 46 章而非复制版本清单
- s1: Simple test-time scaling：Worth Watching；等待与后续 test-time scaling 证据串联
- OpenAI deep research：Worth Watching；只保留系统问题，不写实现推断

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 新增 papers/2025/weekly/2025-W05/README.md。
- 2025 Primary-Source Re-audit 进行中；本周尚未进入 Books Integration。

## Open Questions

- vLLM V1 的 diff reconciliation、cancellation、failure recovery 与 V0/V1 equivalence 如何验证。
- s1 的 token-budget scaling 能否跨模型、领域和真实 GPU cost 保持校准。
- OpenAI deep research 的 planner、state ownership 与 recovery 未公开，何时会出现可核验 technical report。

## Sources

- vLLM V1 Alpha — https://vllm.ai/blog/2025-01-27-v1-alpha-release（First Public: 2025-01-27；Accessed: 2026-07-31）
- s1: Simple test-time scaling — https://arxiv.org/abs/2501.19393（First Public: 2025-01-31；Accessed: 2026-07-31）
- OpenAI deep research — https://openai.com/index/introducing-deep-research/（First Public: 2025-02-02；Accessed: 2026-07-31）
