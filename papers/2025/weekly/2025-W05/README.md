# AI Research Weekly — 2025-W05

> Coverage Window: 2025-01-27～2025-02-02
> Research Mode: Retrospective Discovery and Evidence Rebuild
> Rebuild Started: 2026-08-18
> Accessed: 2026-08-18
> Backfilled: 2026-07-31
> Weekly Evidence Gate: Passed — 55/55 candidates have final evidence dispositions；39/39 `20+` candidates have non-template Full Source Reviews；16/16 low-score candidates have verified identity/date/score/rejection records
> Books Integration: Deferred by user request

## Executive Summary

旧档只保留 vLLM V1、s1 与 OpenAI deep research，漏掉 PyTorch 2.6、Janus-Pro、Streaming DiLoCo、
SFT/RL generalization、FP4 training、tokenizer scaling、guardrail/evaluation 与 multimodal benchmark 等系统证据。
W06 discovery replay 发现 Hugging Face 的推荐日期晚于 arXiv v1，回拨出 Reward-Guided Speculative
Decoding、Constitutional Classifiers、ChunkKV、SafeRAG 等 25 项遗漏。当前 census 因而扩展为 55 项：
39 项达到 `20+` 全文门槛，16 项进入低分 identity/date/score/rejection 核验。性能数字仅在模型、硬件、
精度、长度、batch/concurrency 与 evaluator
条件可定位时使用；Books Gate 本阶段保持关闭。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；本轮访问日期统一为 2026-08-18。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。
- 1 月27～2 月2 日聚合页面出现的更早 v1 已回拨 W04；Transformers 4.48.1 归 W04，4.48.2 归本周。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Janus-Pro（2025-01-27）、OpenAI deep research（2025-02-02）；Constitutional Classifiers 的
  论文 v1 为 2025-01-31，2月3日 Anthropic Blog 与2月13日 demo update 仅作同 family 后续证据。
- 低分核验：Qwen2.5-Max、Mistral Small 3、OpenAI o3-mini；三者主要是版本/产品事实，公开材料不足以支持内部机制外推。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

### Discovery Census

- `20+`：Mixture-of-Mamba、SFT Memorizes RL Generalizes、FP4 Training、Over-Tokenized Transformer、
  Open Problems in Mechanistic Interpretability、TAID、Critique Fine-Tuning、Atla Selene Mini、o3-mini
  external safety testing、Virus、Underthinking、GuardReasoner、Streaming DiLoCo、SANA 1.5、WildChat-50M、
  MedXpertQA、PhysBench 与 s1。
- W06 spillback `20+`：Reward-Guided Speculative Decoding、Scalable-Softmax、PixelWorld、
  Constitutional Classifiers、SAeUron、large-model learning-rate scheduling、adversarial inference-time
  compute、ChunkKV、SafeRAG、MM-IQ、Rethinking Mixture-of-Agents、Concept Steerers、Federated
  Sketching LoRA 与 Activation Approximation Safety。
- 后续 W06 discovery spillback `20+`：RAG Interrogation Attack、HackerRank-ASTRA 与 Weak-to-Strong Diffusion。
- 低分核验：MR.Q、DiffSplat、LLMs Think Too Fast、CowPilot。它们分别受项目主线相关性、窄域
  representation recipe、单环境 causal evidence 与研究原型边界限制。
- W06 spillback 低分核验：SSQR、Multi-View Geometric Diffusion、news summarization、INT、AIN 与
  pathology foundation-model site shift，以及 Text-to-CAD；它们保留 domain/retrieval/evaluation 警示，
  但没有形成新的主干 owner。
- 后续 W06 spillback 低分核验：low-resource programming-language code generation empirical study。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 保留：vLLM V1 Alpha、PyTorch 2.6。
- 低分核验：Transformers 4.48.2 compatibility patch；无独立长期机制。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| vLLM V1 Alpha | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| PyTorch 2.6 | 5 | 5 | 5 | 5 | 5 | 1 | 26/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| Streaming DiLoCo | 5 | 5 | 5 | 5 | 4 | 2 | 26/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| Janus-Pro | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| Mixture-of-Mamba | 5 | 4 | 4 | 5 | 4 | 3 | 25/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| SFT Memorizes, RL Generalizes | 5 | 5 | 4 | 5 | 4 | 2 | 25/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| FP4 Training | 5 | 5 | 4 | 5 | 4 | 2 | 25/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| s1: Simple test-time scaling | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| Over-Tokenized Transformer | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| GuardReasoner | 4 | 4 | 5 | 5 | 4 | 2 | 24/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| SANA 1.5 | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| OpenAI deep research | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Complete Full Source Review；Weekly Only — Mechanism Not Disclosed |
| Open Problems in Mechanistic Interpretability | 3 | 4 | 4 | 5 | 4 | 3 | 23/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| TAID | 4 | 4 | 4 | 5 | 3 | 3 | 23/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| Critique Fine-Tuning | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| Virus harmful fine-tuning attack | 4 | 5 | 4 | 5 | 4 | 1 | 23/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| WildChat-50M | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| Early external o3-mini safety testing | 3 | 4 | 4 | 5 | 4 | 2 | 22/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| Underthinking / Thought Switching Penalty | 4 | 4 | 4 | 5 | 4 | 1 | 22/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| MedXpertQA | 3 | 4 | 4 | 5 | 4 | 2 | 22/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| PhysBench | 3 | 4 | 4 | 5 | 4 | 2 | 22/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| Atla Selene Mini | 3 | 4 | 4 | 5 | 3 | 2 | 21/30 | Complete Full Source Review；Books Pending — Integration Deferred |
| Constitutional Classifiers | 5 | 5 | 5 | 5 | 5 | 2 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| ChunkKV | 5 | 5 | 5 | 5 | 4 | 1 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| Reward-Guided Speculative Decoding | 5 | 5 | 4 | 5 | 4 | 1 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Learning-Rate Scheduling for Large Model Training | 5 | 4 | 4 | 5 | 4 | 2 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| SafeRAG | 4 | 5 | 5 | 5 | 4 | 1 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Trading Inference-Time Compute for Adversarial Robustness | 4 | 5 | 4 | 5 | 4 | 1 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| Scalable-Softmax | 4 | 4 | 3 | 5 | 4 | 2 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| PixelWorld | 4 | 4 | 4 | 5 | 3 | 2 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| SAeUron | 4 | 4 | 4 | 5 | 3 | 2 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| MM-IQ | 3 | 4 | 4 | 5 | 4 | 1 | 21/30 | Full Review Complete；Books Pending — Integration Deferred |
| Activation Approximation Safety | 4 | 5 | 4 | 5 | 5 | 3 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| Rethinking Mixture-of-Agents | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Federated Sketching LoRA | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Concept Steerers | 4 | 3 | 3 | 5 | 3 | 2 | 20/30 | Full Review Complete；Books Pending — Integration Deferred |
| RAG Interrogation Attack | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| HackerRank-ASTRA | 3 | 4 | 4 | 5 | 4 | 1 | 21/30 | Full Review Complete；Books Pending — Integration Deferred |
| Weak-to-Strong Diffusion | 4 | 4 | 4 | 5 | 3 | 2 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| Qwen2.5-Max | 2 | 4 | 4 | 5 | 3 | 1 | 19/30 | Low-score Verified；Weekly Only — Version Fact / Mechanism Not Disclosed |
| Mistral Small 3 | 2 | 4 | 4 | 5 | 3 | 1 | 19/30 | Low-score Verified；Weekly Only — Model Release Fact |
| OpenAI o3-mini | 2 | 4 | 4 | 5 | 3 | 1 | 19/30 | Low-score Verified；Weekly Only — Product Contract / Mechanism Not Disclosed |
| MR.Q | 4 | 3 | 3 | 5 | 2 | 2 | 19/30 | Low-score Verified；Weekly Only — General RL Research |
| DiffSplat | 4 | 3 | 4 | 5 | 2 | 1 | 19/30 | Low-score Verified；Weekly Only — Narrow 3D Generation Case |
| LLMs Think Too Fast | 3 | 3 | 3 | 5 | 3 | 1 | 18/30 | Low-score Verified；Weekly Only — Single-environment Exploratory Study |
| CowPilot | 3 | 3 | 4 | 5 | 2 | 1 | 18/30 | Low-score Verified；Weekly Only — Research Prototype |
| SSQR | 4 | 3 | 3 | 5 | 2 | 2 | 19/30 | Low-score Verified；Weekly Only — Narrow KG Representation Case |
| Multi-View Geometric Diffusion | 4 | 3 | 4 | 5 | 2 | 1 | 19/30 | Low-score Verified；Weekly Only — Narrow 3D Generation Case |
| AIN | 3 | 4 | 4 | 5 | 2 | 1 | 19/30 | Low-score Verified；Weekly Only — Language-Specific Multimodal Model Case |
| Pathology Foundation Model Site Shift | 3 | 4 | 4 | 5 | 2 | 1 | 19/30 | Low-score Verified；Weekly Only — Domain Robustness Case |
| News Summarization Capability Study | 3 | 3 | 4 | 5 | 2 | 1 | 18/30 | Low-score Verified；Weekly Only — Narrow Task Evaluation |
| INT Promptable Segmentation | 3 | 3 | 3 | 5 | 2 | 1 | 17/30 | Low-score Verified；Weekly Only — Narrow Vision Recipe |
| Transformers 4.48.2 | 1 | 2 | 4 | 5 | 3 | 1 | 16/30 | Low-score Verified；Weekly Only — Compatibility Patch |
| Text-to-CAD / CADFusion | 4 | 3 | 3 | 5 | 2 | 2 | 19/30 | Low-score Verified；Weekly Only — Narrow CAD Generation Case |
| Low-Resource Programming-Language Code Generation | 3 | 3 | 4 | 5 | 3 | 1 | 19/30 | Low-score Verified；Weekly Only — Narrow Empirical Study |

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

知识树位置：`INFER-REQUEST-LIFECYCLE`～`INFER-VLLM` 与 `INFER-SCHEDULING`。Archive Must Read；
Books Integration 本阶段延期。未来判断必须围绕 unified state/control evolution，而不是复制版本清单。

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

知识树位置：`MODEL-SAMPLING`、`TRAIN-SFT` / `TRAIN-RLHF`、`INFER-SCHEDULING` 与
`PLATFORM-EVALUATION-SYSTEM`。Archive Must Read；Books Integration 延期，等待与后续 test-time
scaling 证据串联。

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

知识树位置：`AGENT-RAG`、`AGENT-TOOL`、`AGENT-WORKFLOW` 与 `AGENT-PLATFORM`。Weekly Only；
只保留产品能力、系统问题和机制未披露边界，不写内部实现推断。

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
- **ROADMAP Node:** `INFER-VLLM`（Ch50）主 owner；`INFER-REQUEST-LIFECYCLE`～`INFER-CONTINUOUS-BATCHING`
  （Ch42～47）提供 phase/KV/batch 前提，`INFER-MEMORY-MANAGEMENT` 与 `INFER-SCHEDULING`（Ch54、56）
  负责 fleet memory 与 scheduling contract；不把 alpha feature list 扩散到多章。
- **Target and Adjacent Chapters Read:** 已核对当前 Ch42～51、Ch54～56，重点核对 Ch46～50 与 Ch56 的
  request-state、engine 与 scheduler owner；旧记录的 Ch46/50/52 属 legacy 编号。
- **Existing Coverage:** Ch46 已有 vLLM runtime 机制，但需在 Evidence Gate 后核对是否完整呈现
  V0→V1 control/state evolution，而不是只描述当前流程。
- **Integration Decision:** `Books Pending — Integration Deferred`；历史 Weekly 阶段只记录 V0→V1 的
  control/state 演进候选，不执行章节写入。
- **Changed Files or Rejection Reason:** 仅更新 W05；用户明确要求本阶段不做 Books Integration。
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
- **ROADMAP Node:** `MODEL-SAMPLING`（Ch20）负责 stopping policy，`TRAIN-SFT`（Ch29）与
  `TRAIN-RLHF`（Ch31）负责训练来源，`INFER-SCHEDULING`（Ch56）负责 serving token budget，
  `PLATFORM-EVALUATION-SYSTEM`（Ch66）负责 quality/cost evidence。
- **Target and Adjacent Chapters Read:** 已核对 Ch19～22、Ch28～34、Ch42～45、Ch54～56 与 Ch66；
  明确 training policy、decode control、fleet capacity 与 evaluation 的 owner 边界。
- **Existing Coverage:** 现有章节已强调 token budget、reasoning reward 与调度，但未明确 budget forcing
  的“control≠quality”案例；是否写入取决于后续 test-time scaling source family 去重。
- **Integration Decision:** `Books Pending — Integration Deferred`；即使未来作为 Experimental Case，
  也不能仅凭 24/30 或单一 benchmark 强行修改 Books。
- **Changed Files or Rejection Reason:** 仅更新 W05；用户明确要求本阶段不做 Books Integration。
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
- **ROADMAP Node:** `AGENT-WORKFLOW`（Ch81）负责长期原则；`AGENT-RAG`（Ch76）负责 retrieval/citation，
  `AGENT-TOOL`（Ch78）负责 tool execution，`AGENT-PLATFORM`（Ch84）负责 run lifecycle。
- **Target and Adjacent Chapters Read:** 已核对 Ch74～84，重点 Ch76、Ch78～81 与 Ch84。
- **Existing Coverage:** Ch72 已覆盖 source authority/citation entailment；Ch77 已定义 durable workflow
  state、retry/budget/recovery；Ch80 已覆盖 run identity/evidence。公开来源没有新增可验证内部机制。
- **Integration Decision:** `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`；产品 workflow 不能反推内部 orchestration。
  Disclosed`，不修改 Books。
- **Changed Files or Rejection Reason:** 仅更新 W05；公开材料没有足够内部机制，且用户明确要求本阶段
  不做 Books Integration。
- **Open Questions:** planner/state/recovery contract、citation entailment evaluation、source trust policy、
  tool sandbox/egress、cost/tail latency 与 run cancellation semantics。

### PyTorch 2.6

- **Candidate / Week / Score:** PyTorch 2.6 / 2025-W05 / 26/30。
- **Source Family ID:** `pytorch-2-6-compile-export-packaging-security`。
- **Source Type:** 官方 release blog、release notes、RFC/文档链接。
- **First-public Date / Revision History:** 2025-01-29 GA；后续网页编辑不反写 release-time contract。
- **Direct Primary Sources:** https://pytorch.org/blog/pytorch2-6/；https://github.com/pytorch/pytorch/releases/tag/v2.6.0。
- **Related Primary Sources:** `set_stance`、`triton_op`、AOTInductor packaging、Manylinux/CXX11 ABI 与 `weights_only` 官方文档。
- **Access and Verification Status:** Verified；release、beta/prototype、packaging、ABI 与 breaking-change 边界可访问。
- **Full-read Coverage:** 已读 PT2、AOTInductor、custom Triton op、dynamic shape、CPU/Intel GPU、binary packaging、security default 与 migration notes。
- **Original Problem:** eager/compile/export/deployment 各自演化，使 recompile policy、custom kernel visibility、artifact portability 与 ABI 生命周期割裂。
- **Why the Previous Design Was Reasonable:** eager fallback、Python wheel 与直接链接 libtorch 适合研究迭代；`torch.load` 默认完整 unpickle 保持历史兼容。
- **Changed Constraint:** compiled model 要跨进程/环境交付，custom Triton kernel 要进入 compiler graph，安全默认值和 binary ABI 也必须可治理。
- **Mechanism:** `set_stance` 控制重编译策略；`triton_op` 暴露 kernel 实现给 compile；PT2 archive 封装 artifacts/metadata；稳定 C ABI 支撑 AOTInductor compatibility；`weights_only` 默认收紧加载面。
- **State Ownership:** compiler cache 拥有 specialization；export/package 拥有 graph、binary 与 metadata；runtime 拥有 ABI compatibility；artifact loader 拥有反序列化 policy。
- **Control Flow / Data Flow:** Python module→capture/compile→stance 处理 guard miss→Inductor/Triton lowering→PT2 archive→C++/Python runtime；load policy 在 artifact 入口先验证允许类型。
- **Implementation Details:** Python 3.13 compile、AOT minifier、FP16 x86、FlexAttention CPU 与 CUTLASS/CK backend 为不同 maturity 项，不能合并成统一性能承诺。
- **Evaluation Setup:** release 给 feature validation 范围而非统一 benchmark；CPU FP16、Intel GPU、FlexAttention 与 backend 各有独立硬件/文档条件。
- **Baselines / Ablations / Sensitivity:** 无跨 release 统一 ablation；feature maturity 使用 Beta/Prototype，必须按 workload 与 backend 单独验证。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** CUDA 12.6.3、ROCm 6.2.4、XPU、Manylinux 2.28/CXX11 ABI 与 x86 FP16被披露；无统一模型、长度、batch 或 SLO。
- **What the Evidence Actually Proves:** framework release 把 compile policy、artifact packaging、ABI 与 secure loading提升为显式 contract，而非仅增加算子。
- **What It Does Not Prove:** 不证明 `torch.compile` 对所有模型更快、PT2 archive 跨任意环境稳定，或 prototype backend 可直接生产采用。
- **Limitations / Threats to Validity:** release summary 不是独立性能研究；3892 commits 的行为不能由单页完整归因；部分 binary ABI 仍是迁移期实验状态。
- **Trade-offs / New Failure Modes:** 更稳定 artifact/runtime contract 增加版本矩阵、guard/recompile、archive provenance 与 extension ABI 管理；secure default 可能破坏旧 checkpoint。
- **Where the Previous Design Still Applies:** eager 适合动态研究路径；旧 wheel/Conda 适合冻结环境；完整 pickle 仅可在受信 artifact 与显式风险接受下使用。
- **Evolution Relationship:** `Direct Evolution`：eager/Python-bound deployment→captured graph→packaged compiled artifact→ABI/security-governed runtime。
- **ROADMAP Node:** `TRAIN-DISTRIBUTED-TRAINING`（Ch36）负责 framework/runtime contract；handoff `INFER-TENSORRT-LLM` Ch49、`PLATFORM-MODEL-REGISTRY` Ch59、`PLATFORM-SECURITY` Ch72。
- **Target and Adjacent Chapters Read:** 已核对 Ch35～41、Ch49、Ch57～59、Ch72 的 artifact/runtime ownership。
- **Existing Coverage:** Books 已覆盖 compile/export 与 artifact provenance；本阶段仅确认 owner，不执行正文判断。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；未修改 Books，未保存脱离 backend/workload 的性能数字。
- **Open Questions:** PT2 archive schema evolution、custom-op trust boundary、guard-cache observability 与跨版本 ABI conformance 如何被持续验证。

### Streaming DiLoCo

- **Candidate / Week / Score:** Streaming DiLoCo / 2025-W05 / 26/30。
- **Source Family ID:** `streaming-diloco-overlapped-low-bandwidth-training`。
- **Source Type:** arXiv v1 research paper + author implementation details/appendices。
- **First-public Date / Revision History:** v1 2025-01-30；后续 revision 作为同 family 核验，不改变 W05 owner。
- **Direct Primary Sources:** https://arxiv.org/html/2501.18512v1；https://arxiv.org/abs/2501.18512。
- **Related Primary Sources:** DiLoCo/local-SGD/gradient-compression papers定义前代，不证明本论文收益。
- **Access and Verification Status:** Verified；算法、同步/overlap/quantization ablation、scaling与appendices可访问。
- **Full-read Coverage:** 已读 inner/outer optimizer、fragment schedule、async send/block receive、mixing、E3M0、memory、replica/step/fragment/quantization ablations与future work。
- **Original Problem:** 每步全量同步要求低延迟高带宽共置网络，限制跨站点或弱互连训练；普通 DiLoCo 又在 outer step 形成 burst 和 barrier。
- **Why the Previous Design Was Reasonable:** synchronous data parallel 提供清晰一致性；DiLoCo 以多 local steps 换少量同步，在稳定同速 replica 下简单有效。
- **Changed Constraint:** 跨集群链路带宽小且延迟高，outer-gradient burst 仍会阻塞计算；完整模型一次同步也造成峰值内存/带宽。
- **Mechanism:** 把参数划分 fragments，按顺序/strided schedule 每 H 步仅同步部分；通信异步覆盖后续 inner steps，再以 mixing factor 合并 stale outer update；传输可量化到 E3M0、累加保持 FP32。
- **State Ownership:** 每个 replica 拥有 local parameters/optimizer；fragment schedule 拥有同步时钟；outer optimizer 拥有跨 replica delta；transport 拥有 in-flight fragment/version。
- **Control Flow / Data Flow:** local SGD→计算某 fragment 的 H-step delta→async all-reduce/send→继续 τ 个 inner steps→receive旧版本 delta→outer optimizer→与当前 fragment加权合并。
- **Implementation Details:** streaming降低 peak bandwidth，overlap降低 exposed time，低精度降低总 bits；三者是可组合但不同的控制旋钮。
- **Evaluation Setup:** 多语言模型规模、replica 数、inner steps、网络速度与同步 fragment 设置；比较 standard training、DiLoCo、FedPart及组件消融。
- **Baselines / Ablations / Sensitivity:** 明确消融 fragment 数/顺序、overlap/slack、quantized outer gradients、replicas 与 H；并测 compute utilization 与 scaling。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 论文披露模型/replica/网络模拟和 FP32 accumulation/E3M0 transfer；结果依链接速度、τ、H 与 fragment count，非通用 wall-time 保证。
- **What the Evidence Actually Proves:** 在作者实验中，把同步粒度从完整模型改为版本化 fragment，可同时平滑带宽并与计算重叠；量化 outer delta在测试范围未显著退化。
- **What It Does Not Prove:** 不证明跨任意异构/故障网络无损，也不证明 staleness、低精度和局部漂移在 frontier-scale 长训练中无累积影响。
- **Limitations / Threats to Validity:** 受控实验与网络模型；真实跨区域 failure、straggler、optimizer checkpoint、elastic membership和长期收敛证据有限。
- **Trade-offs / New Failure Modes:** 降低通信峰值却引入 fragment version、stale merge、in-flight recovery、schedule skew、局部漂移和额外参数副本/缓冲。
- **Where the Previous Design Still Applies:** 高带宽共置集群与严格同步仍优先；小模型/短训练或更新高度耦合时，完整同步更简单且风险更低。
- **Evolution Relationship:** `Direct Evolution`：同步全量 collective→periodic local SGD→fragment streaming→communication/compute overlap→low-bit outer delta。
- **ROADMAP Node:** `TRAIN-DISTRIBUTED-TRAINING`（Ch36）主 owner；handoff `TRAIN-PIPELINE-PARALLEL` Ch38、`TRAIN-CHECKPOINT` Ch35 与 communication 横轴。
- **Target and Adjacent Chapters Read:** 已核对 Ch35～41，尤其 collective consistency、PP overlap、checkpoint/recovery 与 optimizer state。
- **Existing Coverage:** Books 已有异步 pipeline 与 delayed update；本研究增加跨 replica fragment ownership 分支，正文判断延后。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；作者带宽/速度数字保留在实验 contract 内。
- **Open Questions:** elastic replica如何重新分配fragment version；partial checkpoint如何恢复in-flight outer update；真实WAN jitter下α/τ如何自适应。

### Janus-Pro

- **Candidate / Week / Score:** Janus-Pro / 2025-W05 / 25/30。
- **Source Family ID:** `janus-pro-decoupled-visual-encoding-unified-ar`。
- **Source Type:** arXiv technical report + official repository/model artifact。
- **First-public Date / Revision History:** repository release 2025-01-27；paper v1 2025-01-29；同 family 分别记录 release 与 report。
- **Direct Primary Sources:** https://arxiv.org/html/2501.17811；https://github.com/deepseek-ai/Janus。
- **Related Primary Sources:** Janus predecessor定义原始decoupling；SigLIP/VQ tokenizer为依赖。
- **Access and Verification Status:** Verified；architecture、training stages、data scaling、evaluation与generation code可访问。
- **Full-read Coverage:** 已读 decoupled encoders、unified AR transformer、adaptors、三阶段训练、data/model scaling、understanding/generation benchmarks与repository inference path。
- **Original Problem:** 理解需要高层语义特征，生成需要可重建离散视觉 code；共享同一 visual encoder会让两个目标争夺表示空间。
- **Why the Previous Design Was Reasonable:** 单 encoder 简化参数、token identity与联合训练；小规模统一模型首先验证可行性是合理起点。
- **Changed Constraint:** 统一模型扩展到更大数据/7B时，短 prompt 生成稳定性和理解能力暴露 representation conflict。
- **Mechanism:** understanding 用 SigLIP+adapter，generation 用 VQ tokenizer/code embedding+adapter；两种 token 映射到同一 autoregressive language transformer，但保持输入 codec 解耦。
- **State Ownership:** modality-specific encoder/tokenizer拥有原始信号语义；adapter拥有共享空间映射；AR transformer拥有跨 token sequence state；decoder拥有视觉重建。
- **Control Flow / Data Flow:** image→SigLIP→understanding tokens或image→VQ IDs→generation tokens→shared transformer；生成时自回归采样视觉 IDs→VQ decoder还原图像。
- **Implementation Details:** 1B/7B；理解与生成使用独立 head/path，repository展示 BF16、KV cache、CFG conditional/unconditional paired batches与576 image tokens。
- **Evaluation Setup:** GQA、POPE、MME、SEED、MMBench、MM-Vet、MMMU；生成用 GenEval/DPG-Bench，图像分辨率384×384。
- **Baselines / Ablations / Sensitivity:** 与 unified/task-specific模型和 Janus 比较；改善由训练策略、数据和规模共同产生，缺完整单因素因果隔离。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 1B/7B、384²、576 visual tokens；repo示例 BF16/parallel samples，训练硬件、serving concurrency与SLO未完整披露。
- **What the Evidence Actually Proves:** understanding/generation可共享序列模型而不必共享 visual codec；representation ownership的解耦在作者任务上更稳健。
- **What It Does Not Prove:** 不证明统一AR优于diffusion、benchmark提升完全来自decoupling，也不证明高分辨率/视频/实时服务可扩展。
- **Limitations / Threats to Validity:** 低分辨率、作者 benchmark、数据/规模/strategy同时变化；安全、版权、生成 latency与codec artifact未充分评估。
- **Trade-offs / New Failure Modes:** 减少task conflict，却增加双encoder参数、两套token identity、adapter alignment、codec版本与generation exposure bias。
- **Where the Previous Design Still Applies:** 单 encoder适合资源受限、任务接近或只做理解；diffusion适合并行修正/高保真图像；专用模型仍可换更强质量。
- **Evolution Relationship:** `Alternative Branch`：shared visual encoder→decoupled modality objectives + shared AR backbone；不是理解/生成必须统一的结论。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24、`MODEL-SAMPLING` Ch20。
- **Target and Adjacent Chapters Read:** 已核对 Ch22～25、Ch18～20 与 Ch27 的 representation/objective boundary。
- **Existing Coverage:** Ch23已定义 modality-specific codec/shared space；Janus-Pro是受限案例，是否新增正文待Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把作者榜单写成统一架构通用优势。
- **Open Questions:** 两套codec如何共享provenance/version；高分辨率与视频token成本；CFG paired state如何进入continuous batching。

### Mixture-of-Mamba

- **Candidate / Week / Score:** Mixture-of-Mamba / 2025-W05 / 25/30。
- **Source Family ID:** `mixture-of-mamba-modality-aware-ssm-sparsity`。
- **Source Type:** arXiv v1 experimental architecture paper。
- **First-public Date / Revision History:** v1 2025-01-27；本周按 v1 归档。
- **Direct Primary Sources:** https://arxiv.org/html/2501.16295v1；https://arxiv.org/abs/2501.16295。
- **Related Primary Sources:** Mamba、Mixture-of-Transformers、MoE-Mamba/BlackMamba为baseline/ancestry。
- **Access and Verification Status:** Verified；method、three settings、component ablation、scale与appendix可访问。
- **Full-read Coverage:** 已读 modality router、four projection decoupling、Transfusion/Chameleon/speech settings、FLOP-to-loss comparison、component synergy与causal-attention caveat。
- **Original Problem:** dense Mamba block让不同 modality共享全部projection，既承担互相冲突的统计结构，也无法按 modality稀疏分配参数容量。
- **Why the Previous Design Was Reasonable:** dense weights参数共享简单、无router/capacity failure；MoE只放MLP可复用成熟dispatch而不触碰SSM recurrence。
- **Changed Constraint:** text/image/speech联合预训练扩大表示冲突，模型容量增长但希望 active compute不同比例增长。
- **Mechanism:** 按已知 modality ID在 Mamba `in/x/dt/out` projections选择专用权重；SSM recurrence框架保留，稀疏性进入 block内部而非仅MLP。
- **State Ownership:** tokenizer/data pipeline拥有 modality label；router是确定性 modality dispatch；各projection expert拥有参数；SSM state仍按sequence/token流演化。
- **Control Flow / Data Flow:** interleaved tokens+modality mask→对应projection experts→conv/SSM scan→modality-specific output projection→下层；无学习型top-k容量竞争。
- **Implementation Details:** 在163M～1.5B尺度，比较 dense Mamba、MoM与Flex-Attention；四个projection可单独或联合解耦。
- **Evaluation Setup:** Transfusion连续image objective、Chameleon离散image AR、Chameleon+speech三模态；以training/validation loss与达到目标loss的相对FLOPs衡量。
- **Baselines / Ablations / Sensitivity:** four-projection组合消融显示联合解耦收益非简单相加；scale sweep与不同 modality均有结果。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型规模与相对FLOPs披露；硬件、precision、sequence/batch和serving SLO并未形成完整contract。
- **What the Evidence Actually Proves:** 已知modality可作为稀疏路由信号，使SSM block内部容量分离；作者设置中达到同loss所需FLOPs下降。
- **What It Does Not Prove:** 不证明loss改善等同下游质量，不证明适用于未知/混合modality boundary，也不证明kernel/communication效率达到理论active FLOPs。
- **Limitations / Threats to Validity:** modality标签是oracle；Flex-Attention含图像内bidirectional而作者SSM严格causal，baseline不完全同构；未报告生产dispatch成本。
- **Trade-offs / New Failure Modes:** 避免learned-router imbalance，却依赖正确modality segmentation；参数/optimizer state增加，跨模态共享减少，expert placement会引入通信。
- **Where the Previous Design Still Applies:** 单模态或高度共享任务用dense Mamba更简单；学习型MoE适合token级语义路由；attention仍适合精确随机访问。
- **Evolution Relationship:** `Alternative Branch`：dense SSM→MLP-only MoE hybrid→modality-aware sparse SSM projections。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `MODEL-MOE` Ch21、`TRAIN-TENSOR-PARALLEL` Ch37。
- **Target and Adjacent Chapters Read:** 已核对 Ch21～24、Ch36～38 与 Ch49 的 routing/placement boundary。
- **Existing Coverage:** Books已有modality identity与MoE routing distinction；本研究提供两者交叉案例，正文判断延后。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；相对FLOPs不脱离loss/model setting外推。
- **Open Questions:** modality boundary动态变化时如何路由；experts跨device placement；参数增加是否抵消activation savings；与learned router如何组合。

### SFT Memorizes, RL Generalizes

- **Candidate / Week / Score:** SFT Memorizes, RL Generalizes / 2025-W05 / 25/30。
- **Source Family ID:** `sft-vs-rl-generalization-controlled-environments`。
- **Source Type:** arXiv v1 controlled post-training study。
- **First-public Date / Revision History:** v1 2025-01-28；后续版本不改变本周 owner。
- **Direct Primary Sources:** https://arxiv.org/html/2501.17161v1；https://arxiv.org/abs/2501.17161。
- **Related Primary Sources:** GeneralPoints/V-IRL environment artifacts与base VLM/LLM依赖用于复核。
- **Access and Verification Status:** Verified；task design、training pipeline、compute matching、ablations、failure cases与limitations可访问。
- **Full-read Coverage:** 已读 text/vision variants、SFT trajectories、outcome RL、verification-step sensitivity、compute estimation、hyperparameter ablation与RL failure cases。
- **Original Problem:** SFT与RL常同时存在于post-training pipeline，真实模型上难分辨“模仿已见轨迹”与“从reward学习可泛化策略”。
- **Why the Previous Design Was Reasonable:** SFT稳定、样本可控、易注入格式/知识；在in-distribution imitation与缺reward/verifier时仍是首选。
- **Changed Constraint:** 需要跨规则、视觉布局和路线变化泛化，并可自动验证最终结果，而非只复现演示轨迹。
- **Mechanism:** 在GeneralPoints/V-IRL构造ID/OOD variants；SFT学习专家轨迹，RL用outcome/step verification优化policy；比较同compute近似下的泛化。
- **State Ownership:** environment拥有 transition/reward；SFT dataset拥有示范轨迹；RL rollout buffer/policy拥有探索分布；verifier拥有反馈语义。
- **Control Flow / Data Flow:** task state→policy action→environment transition→outcome/step verifier→RL update；SFT路径则固定state-action trajectory→token loss。
- **Implementation Details:** text与vision版本、不同verification steps、冻结/不冻结vision encoder、suboptimal SFT与多学习率均被检查。
- **Evaluation Setup:** GeneralPoints arithmetic card game与V-IRL navigation；ID/OOD rule/visual variations；per-step accuracy和episode success。
- **Baselines / Ablations / Sensitivity:** SFT/RL compute matching、learning-rate sweep、1/3/5/10 verification steps、without-SFT与overfit-checkpoint failure。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 论文披露训练设置但不构成serving contract；环境狭窄，V-IRL overall success对两类方法均低。
- **What the Evidence Actually Proves:** 在两个可验证受控环境中，outcome RL较SFT更能利用interaction distribution并获得OOD收益；更多verification steps改善该实验的泛化。
- **What It Does Not Prove:** 不证明RL普遍泛化、SFT只能记忆，也不证明开放域、人类偏好或无可靠verifier任务有同样结果。
- **Limitations / Threats to Validity:** 两个synthetic/simplified环境；SFT数据与RL exploration分布不同；视觉识别与策略学习贡献难完全分离；overall success很低。
- **Trade-offs / New Failure Modes:** RL获得探索和credit assignment，却增加rollout成本、reward hacking、verifier bias、policy collapse与checkpoint sensitivity；SFT仍提供初始化/格式稳定性。
- **Where the Previous Design Still Applies:** 行为模仿、格式对齐、稀缺interaction、无可靠reward或严格可控输出时SFT更合理；RL通常依赖良好初始化。
- **Evolution Relationship:** `Alternative Branch`：demonstration imitation与outcome optimization承担不同职责，不是RL对SFT的单向替代。
- **ROADMAP Node:** `TRAIN-SFT`（Ch29）与 `TRAIN-RLHF`（Ch31）边界；主 owner Ch31，handoff Ch33、Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch28～34、Ch66 的data/reward/evaluation contract。
- **Existing Coverage:** Books已强调SFT/RL分工；论文提供受控证据边界，是否refine待Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把标题命题外推为所有foundation-model post-training事实。
- **Open Questions:** 更开放任务的verifier reliability、equal-compute定义、RL对pretraining prior依赖与失败checkpoint的可恢复性。

### FP4 Training

- **Candidate / Week / Score:** Optimizing LLM Training Using FP4 Quantization / 2025-W05 / 25/30。
- **Source Family ID:** `fp4-training-dge-occ`。
- **Source Type:** arXiv v1 quantized-training paper。
- **First-public Date / Revision History:** v1 2025-01-28；本周按 v1 归档。
- **Direct Primary Sources:** https://arxiv.org/html/2501.17116v1；https://arxiv.org/abs/2501.17116。
- **Related Primary Sources:** FP8/MS-AMP/Transformer Engine和hardware FP4工作作为baseline。
- **Access and Verification Status:** Verified；DGE、OCC、implementation、main/ablation、limitations与appendix可访问。
- **Full-read Coverage:** 已读FP4 format/block quantization、differentiable gradient estimator、outlier clamp+compensation、training setup、zero-shot eval、granularity与component ablation。
- **Original Problem:** 直接W4A4训练因非可微quantization与activation outlier造成梯度偏差、underflow和NaN，理论低bit吞吐无法转化为稳定训练。
- **Why the Previous Design Was Reasonable:** BF16/FP8训练稳定、hardware/toolchain成熟；STE实现简单且在较高bit可接受。
- **Changed Constraint:** 模型规模让训练memory/compute成为瓶颈，而FP4 hardware路径要求forward与backward都可用极低precision。
- **Mechanism:** forward直接FP4；DGE用可微近似校正weight gradient；OCC按quantile截断activation，并用稀疏高精度残差补偿outliers。
- **State Ownership:** quantizer拥有scale/block与clamp threshold；DGE拥有backward surrogate；sparse residual path拥有outlier index/value；optimizer保留master/update state。
- **Control Flow / Data Flow:** tensor→block quantize/clamp→FP4 GEMM + sparse residual matmul→loss；backward经DGE correction传播→optimizer update。
- **Implementation Details:** residual约0.2%～2% nonzero；直接activation cast会发散；granularity和threshold影响稳定性/overhead。
- **Evaluation Setup:** LLaMA-family多尺度pretraining与zero-shot tasks；1.3B/10B-token ablation；BF16、两种FP8与direct FP4比较。
- **Baselines / Ablations / Sensitivity:** 分别消融DGE、OCC、precision与quantization granularity；direct W4A4产生NaN是关键negative result。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 1.3B ablation用10B DCLM tokens、batch256；主实验模型/训练配置披露，但硬件端到端speedup和通信/SLO不完整。
- **What the Evidence Actually Proves:** 在作者软件仿真/实现与模型范围内，DGE+OCC可使FP4训练loss/下游结果接近BF16，并避免direct cast发散。
- **What It Does Not Prove:** 不证明任意模型/optimizer稳定，不证明理论FP4 GEMM收益等于端到端训练加速，也不证明稀疏补偿在所有hardware高效。
- **Limitations / Threats to Validity:** 最大模型/训练token远小于frontier run；hardware kernel、energy、distributed collective与长期optimizer stability证据有限。
- **Trade-offs / New Failure Modes:** 降bit节省memory/compute，却增加scale/calibration、sparse residual、surrogate-gradient bias、threshold drift与silent divergence风险。
- **Where the Previous Design Still Applies:** BF16/FP8适合稳定性优先或缺FP4 kernel；weight-only/activation-higher-bit适合outlier重的模型。
- **Evolution Relationship:** `Direct Evolution`：BF16→FP8→naive FP4 failure→gradient correction + outlier residual的mixed-path FP4。
- **ROADMAP Node:** `TRAIN-PRETRAINING`（Ch28）主 owner；handoff `TRAIN-DISTRIBUTED-TRAINING` Ch36、`INFER-TENSORRT-LLM` Ch49。
- **Target and Adjacent Chapters Read:** 已核对 Ch28、Ch35～37、Ch49/54 的precision、optimizer与hardware execution边界。
- **Existing Coverage:** Books已有precision与outlier原则；本论文是训练侧受限案例，正文判断延后。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不保留无端到端hardware contract的“加速”外推。
- **Open Questions:** native FP4 hardware实测、distributed scaling、optimizer master-state成本、长期scale drift和silent correctness monitor。

### Over-Tokenized Transformer

- **Candidate / Week / Score:** Over-Tokenized Transformer / 2025-W05 / 24/30。
- **Source Family ID:** `over-tokenized-transformer-input-vocabulary-scaling`。
- **Source Type:** arXiv v1 architecture/scaling paper。
- **First-public Date / Revision History:** v1 2025-01-28；后续 revision不改变owner。
- **Direct Primary Sources:** https://arxiv.org/html/2501.16975v1；https://arxiv.org/abs/2501.16975。
- **Related Primary Sources:** OLMo2/OLMoE、n-gram tokenization、multi-token prediction用于baseline/dependency。
- **Access and Verification Status:** Verified；method、engineering、scaling sweeps、ablations、appendices与over-decoding negative branch可访问。
- **Full-read Coverage:** 已读 input/output vocab解耦、n-gram hashing/decomposition、dense/MoE实验、vocab/token budget、hierarchical encoding与slow-start。
- **Original Problem:** tokenizer通常被固定为模型前置件，embedding/output head受同一vocabulary绑定；扩大词表会显著增加softmax/参数，因而很少进入scaling设计。
- **Why the Previous Design Was Reasonable:** 共享input/output vocab便于weight tying、生成一致性和artifact管理；subword vocab在数据/compute受限时性价比高。
- **Changed Constraint:** 当模型/data扩大，输入序列压缩与局部multi-gram表示可能比继续增大hidden layers更高效，但输出softmax不需要同样扩张。
- **Mechanism:** 仅扩 input vocabulary，用multi-gram token embedding/hierarchical decomposition聚合输入；输出仍保留基础vocab，自回归目标不变。
- **State Ownership:** base tokenizer拥有可生成token identity；over-encoding layer拥有input-only multi-gram identity；output head只拥有base vocabulary。
- **Control Flow / Data Flow:** raw text→base tokens→并行构造n-gram IDs→多粒度embedding组合→Transformer→base-vocab logits→正常decode。
- **Implementation Details:** vocabulary scaling、hash/decomposition避免完整组合爆炸；hierarchical representation比naive 3-gram更稳，但大词表需要更多tokens越过slow start。
- **Evaluation Setup:** dense与MoE模型、不同规模/词表/训练token；用loss、downstream tasks、参数/FLOP匹配比较。
- **Baselines / Ablations / Sensitivity:** vocabulary size、base tokenizer、hierarchical vs naive、input over-encoding vs output over-decoding；后者需充分训练才可能改善。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型/训练token与FLOP设置披露；硬件、serving memory/cache、吞吐/latency SLO不完整。
- **What the Evidence Actually Proves:** 在作者训练范围内，input vocabulary是独立scaling axis；解耦input/output可获取部分大模型收益而避免同步扩大softmax。
- **What It Does Not Prove:** 不证明词表越大越好、任何语言/代码都服从同一log-linear关系，或“no additional cost”包含tokenizer、embedding lookup与serving memory。
- **Limitations / Threats to Validity:** 依赖特定数据/tokenizer/model family；large-vocab slow start、rare n-gram sparsity、跨语言公平和artifact migration评估不足。
- **Trade-offs / New Failure Modes:** 缩短effective sequence却增加embedding参数、稀疏更新、hash collision、token provenance与cache identity复杂度。
- **Where the Previous Design Still Applies:** 小模型/短训练、开放词形语言或内存受限部署仍适合普通subword；shared vocab便于weight tying与简化runtime。
- **Evolution Relationship:** `Alternative Branch`：固定subword→扩大shared vocab→input/output解耦的over-encoding→多粒度hierarchical input。
- **ROADMAP Node:** `MODEL-TOKENIZER`（Ch11）主 owner；handoff `MODEL-EMBEDDING` Ch12、`TRAIN-PRETRAINING` Ch28、`INFER-KV-CACHE` Ch45。
- **Target and Adjacent Chapters Read:** 已核对 Ch11～13、Ch18、Ch28 与 Ch42～45 的token identity/lifecycle。
- **Existing Coverage:** Books已有tokenizer影响sequence/compute；该论文提供input-only scaling分支，正文判断延后。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不使用脱离训练token/模型的“double-size equivalence”。
- **Open Questions:** multilingual/code tokenizer、embedding sharding、hash collision、KV/cache identity与checkpoint vocabulary migration。

### Open Problems in Mechanistic Interpretability

- **Candidate / Week / Score:** Open Problems in Mechanistic Interpretability / 2025-W05 / 23/30。
- **Source Family ID:** `mechanistic-interpretability-open-problems-evidence-ladder`。
- **Source Type:** arXiv position/synthesis paper with extensive primary-literature map。
- **First-public Date / Revision History:** v1 2025-01-27；position paper按v1 owner归档。
- **Direct Primary Sources:** https://arxiv.org/html/2501.16496v1；https://arxiv.org/abs/2501.16496。
- **Related Primary Sources:** 引用的causal intervention、SAE、circuit与monitoring papers分别承担经验支持。
- **Access and Verification Status:** Verified as research agenda；不是单项机制benchmark。
- **Full-read Coverage:** 已读reverse-engineering/concept-based两路线、decomposition-description-validation、automation、monitor/control/prediction、model-family与socio-technical/governance问题及问题清单。
- **Original Problem:** interpretability常把相关可视化、feature naming或局部ablation直接称作“机制解释”，缺统一验证层级与deployment contract。
- **Why the Previous Design Was Reasonable:** neuron/head/layer是现成架构单位，probe/activation map成本低；早期模型规模允许人工inspection。
- **Changed Constraint:** superposition、distributed computation、model scale和安全用途要求解释不仅可读，还要causal、覆盖充分、可审计并抗分布变化。
- **Mechanism:** 论文提出两种方向：从components寻找roles的reverse engineering，与从concept寻找components；共同闭环为decompose→hypothesize→causally validate。
- **State Ownership:** model artifact拥有weights/activations；analysis pipeline拥有decomposition/feature dictionary；human/automated interpreter拥有hypothesis；evaluation拥有causal test与coverage。
- **Control Flow / Data Flow:** model traces→component/feature decomposition→semantic description→intervention/counterfactual→behavior change evidence→更新或否定解释。
- **Implementation Details:** SAE、circuit discovery、automation、HCI和cross-model methods是工具分支；论文不规定单一标准栈。
- **Evaluation Setup:** 无统一benchmark；证据来自既有文献案例和公开open questions，适合定义evidence gate而非性能排名。
- **Baselines / Ablations / Sensitivity:** 对方法家族做概念比较；没有可将position conclusions视为实验ablation的统一设置。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Not Disclosed / not applicable；使用时必须另绑定目标模型、layer、dataset与intervention。
- **What the Evidence Actually Proves:** 领域尚未解决decomposition validity、semantic faithfulness、automation和治理转化；causal validation应高于仅相关描述。
- **What It Does Not Prove:** 不证明现有interpretability可可靠监控frontier model，也不证明某个feature/circuit等同人类概念或安全保证。
- **Limitations / Threats to Validity:** position paper选择和分类受作者判断；引用证据跨模型/任务异质；研究议程不是部署验证。
- **Trade-offs / New Failure Modes:** 更高evidence标准提高可信度，却增加compute、人审和coverage成本；自动解释会引入model-on-model correlated error与Goodhart。
- **Where the Previous Design Still Applies:** exploratory probe/visualization适合生成假设；小模型手工reverse engineering仍有教育/调试价值，但不能冒充release gate。
- **Evolution Relationship:** `Principle Reuse`：observational probe→causal intervention→coverage/replication→operational monitor与治理证据。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `WORLDVIEW-REPRESENTATION` Ch5、`PLATFORM-MONITORING` Ch67、`PLATFORM-SECURITY` Ch72。
- **Target and Adjacent Chapters Read:** 已核对 Ch5、Ch17、Ch66～73 的evidence ladder与governance boundary。
- **Existing Coverage:** Books已有interpretability evidence ladder；本论文是结构化支持来源，正文判断延后。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把agenda陈述写成已完成能力。
- **Open Questions:** causal sufficiency、feature stability、cross-model replication、monitor latency与policy决策阈值如何统一验收。

### TAID

- **Candidate / Week / Score:** TAID / 2025-W05 / 23/30。
- **Source Family ID:** `taid-temporally-adaptive-interpolated-distillation`。
- **Source Type:** arXiv v1 distillation method paper。
- **First-public Date / Revision History:** v1 2025-01-28；按 v1归档。
- **Direct Primary Sources:** https://arxiv.org/html/2501.16937v1；https://arxiv.org/abs/2501.16937。
- **Related Primary Sources:** forward/reverse/skew KL、on-policy KD与teacher/student model reports为baseline。
- **Access and Verification Status:** Verified；theory、algorithm、instruction/pretraining experiments、capacity-gap/stability analysis与appendices可访问。
- **Full-read Coverage:** 已读 adaptive interpolation、schedule、mode collapse proof、teacher-student pairs、MT-Bench/perplexity、capacity-gap与image-classification negative comparison。
- **Original Problem:** 直接teacher→small student KL在容量差大时，要么平均多种mode造成模糊，要么reverse-like目标只追单一mode并collapse。
- **Why the Previous Design Was Reasonable:** fixed KL简单、稳定且无需student-generated on-policy data；teacher/student接近时成本低。
- **Changed Constraint:** 更大teacher与更小deployable student之间gap扩大，固定target在训练早期离student过远并造成optimization instability。
- **Mechanism:** 构造student/teacher distribution的时间自适应插值target，从接近student逐渐移向teacher；课程速度随训练状态调整。
- **State Ownership:** teacher logits提供knowledge target；student拥有current distribution；scheduler拥有interpolation coefficient/time state；optimizer更新student。
- **Control Flow / Data Flow:** input→teacher/student logits→按coefficient混合intermediate target→distillation loss→student update→schedule推进。
- **Implementation Details:** 不依赖on-policy student generation；可用于instruction tuning/pretraining，并扩展到1.5B LLM与2B VLM案例。
- **Evaluation Setup:** 多teacher-student size/architecture pairs、MT-Bench、language modeling/perplexity与图像分类对照。
- **Baselines / Ablations / Sensitivity:** 与KL variants、on-policy approaches、不同interpolation schedules/capacity gaps比较，并分析mode averaging/collapse。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型pair与训练配置披露；hardware/serving SLO不完整，不能把KD质量直接换算部署收益。
- **What the Evidence Actually Proves:** 在作者模型/任务中，curriculum-like target interpolation改善大capacity-gap distillation稳定性与结果。
- **What It Does Not Prove:** 不证明任何teacher/student都最优，不证明offline KD消除exposure bias，也不证明理论mode分析覆盖真实高维全部行为。
- **Limitations / Threats to Validity:** 依赖teacher logits、schedule和selected benchmarks；on-policy结合只是future work；safety/behavior retention未完整测量。
- **Trade-offs / New Failure Modes:** 稳定target transition却增加schedule state与teacher inference成本；过慢欠蒸馏，过快重新暴露capacity shock。
- **Where the Previous Design Still Applies:** small gap或资源紧时fixed KL更简单；on-policy KD适合必须对齐student rollout distribution的任务。
- **Evolution Relationship:** `Direct Evolution`：fixed teacher target→skew/interpolated target→time-adaptive curriculum；与on-policy KD为可组合分支。
- **ROADMAP Node:** `TRAIN-SFT`（Ch29）主 owner；handoff `TRAIN-PRETRAINING` Ch28、`TRAIN-CHECKPOINT` Ch35。
- **Target and Adjacent Chapters Read:** 已核对 Ch28～31、Ch35 的teacher/student artifact与objective lifecycle。
- **Existing Coverage:** Books已有distillation概念但未必有temporal target ownership；是否refine待Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不外推作者MT-Bench结果。
- **Open Questions:** schedule自动化、teacher drift、token-levelconfidence calibration、safety retention与distributed teacher-logit caching。

### Critique Fine-Tuning

- **Candidate / Week / Score:** Critique Fine-Tuning / 2025-W05 / 23/30。
- **Source Family ID:** `critique-finetuning-noisy-response-analysis`。
- **Source Type:** arXiv v1 post-training/data paper。
- **First-public Date / Revision History:** v1 2025-01-29；按 v1归档。
- **Direct Primary Sources:** https://arxiv.org/html/2501.17703v1；https://arxiv.org/abs/2501.17703。
- **Related Primary Sources:** WebInstruct、MetaMath、NuminaMath与teacher GPT-4o作为data依赖。
- **Access and Verification Status:** Verified；dataset construction、objective、training、ablation、limitations与case studies可访问。
- **Full-read Coverage:** 已读50K critique data、SFT baselines、single/two-stage self-critique、dataset/response/teacher ablation、noisy critique与self-evaluation failures。
- **Original Problem:** 标准SFT只模仿“正确答案”，既浪费大量noisy responses，也未直接训练模型识别错误类型和修正依据。
- **Why the Previous Design Was Reasonable:** imitation objective稳定、输出契约直接、无需在inference增加critique步骤；高质量答案充足时有效。
- **Changed Constraint:** web-scaleinstruction data有噪声，teacher生成/验证成本高；希望从错误答案中提取更密集监督。
- **Mechanism:** 输入=query+noisy response，target=teacher critique；模型学习错误定位/解释。部署可直接回答或先自评再修正，但训练与推理模式需区分。
- **State Ownership:** source dataset拥有query/response；teacher拥有critique label；CFT model学习error representation；inference harness拥有是否调用self-critique的workflow。
- **Control Flow / Data Flow:** noisy pair→teacher critique generation/filter→CFT token loss→checkpoint；可选inference为answer→critique→revise。
- **Implementation Details:** WebInstruct 50K，扩展MetaMath/NuminaMath；Qwen2.5/Math/DeepSeek-Math等7B/32B；1 epoch、global batch512、lr5e-6。
- **Evaluation Setup:** MATH/Minerva/GSM8K/AIME/AMC/OlympiadBench及STEM扩展；MATH-500选checkpoint。
- **Baselines / Ablations / Sensitivity:** noisy SFT、verified SFT、GPT-4o-answer SFT、CFT；data source、response source与teacher critique model消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model family/batch/lr披露；hardware/precision、critique-token成本、serving latency/SLO不完整。
- **What the Evidence Actually Proves:** 在作者math/STEM设置，学习critique比模仿同源response更有效利用noisy data；监督对象变化可改变generalization。
- **What It Does Not Prove:** 不证明self-critique可靠、不证明所有domain优于clean SFT，也不证明teacher critique无偏或能校正未知错误。
- **Limitations / Threats to Validity:** critique本身有错漏；model可能不会正确评价自己；数学任务有可验证结构，开放域迁移未证。
- **Trade-offs / New Failure Modes:** 获取更密集错误监督，却依赖teacher quality，可能学到批评风格而非causal correction；两阶段推理增加token/latency并可循环误判。
- **Where the Previous Design Still Applies:** clean demonstration、格式对齐与低延迟任务仍用SFT；外部verifier优于self-critique时应保持分层。
- **Evolution Relationship:** `Alternative Branch`：imitate answer→filter/verify answer→learn critique→可选critique-and-revise workflow。
- **ROADMAP Node:** `TRAIN-SFT`（Ch29）主 owner；handoff `AGENT-REFLECTION` Ch80、`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch29～34、Ch66、Ch80～81 的training/evaluator/workflow boundary。
- **Existing Coverage:** Books已有reflection与verifier区分；该论文提供training-side critique分支，正文判断延后。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不保留脱离dataset/model的4–10%宣传数字。
- **Open Questions:** critique factuality、teacher bias、direct-answer能力损失、self-revision termination与跨domain replication。

### Atla Selene Mini

- **Candidate / Week / Score:** Atla Selene Mini / 2025-W05 / 21/30。
- **Source Family ID:** `atla-selene-small-general-purpose-evaluator`。
- **Source Type:** arXiv v1 technical report + open-weight model artifact。
- **First-public Date / Revision History:** v1 2025-01-27；后续 artifact revision为同family。
- **Direct Primary Sources:** https://arxiv.org/html/2501.17195v1；官方 Hugging Face/Ollama model links。
- **Related Primary Sources:** Judge Arena、Prometheus/FlowJudge/Glider与evaluation datasets为baseline。
- **Access and Verification Status:** Verified；data mix/filtering、training、11-benchmark evaluation与prompt robustness可访问。
- **Full-read Coverage:** 已读 evaluator problem、task taxonomy、public+synthetic critique data、training pipeline、absolute/classification/pairwise tests、bias/robustness与limitations。
- **Original Problem:** off-the-shelf LLM-as-judge成本高，易受length/position/self-preference和prompt wording影响；人工评价不可扩展。
- **Why the Previous Design Was Reasonable:** 大通用模型zero-shot judge无需训练专用artifact，能快速覆盖新rubric并生成解释。
- **Changed Constraint:** 需要低成本、可部署、跨多类评测且prompt稳定的evaluator，并能固定版本复算release evidence。
- **Mechanism:** 用公共evaluation data加synthetic critiques并过滤质量，训练small language model同时处理absolute scoring、classification与pairwise judgement。
- **State Ownership:** evaluation dataset拥有rubric/labels；synthetic pipeline拥有critique provenance；judge model拥有versioned decision function；harness拥有prompt/order/randomization。
- **Control Flow / Data Flow:** task+response(s)+rubric→prompt template→judge score/class/critique→aggregation/calibration→与human/reference对比。
- **Implementation Details:** open weights；11 benchmarks与Judge Arena；通过多prompt格式检查鲁棒性，但model card/runtime contract仍需单独版本化。
- **Evaluation Setup:** absolute、classification、pairwise三类benchmark；与小/大judge及community arena比较。
- **Baselines / Ablations / Sensitivity:** data filtering/synthetic critique与prompt format分析；部分比较使用不同model size与data，非完全等成本。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model size/benchmarks披露；inference hardware、precision、throughput与judge SLO未完整公开。
- **What the Evidence Actually Proves:** 专用小judge在作者11-benchmark范围可接近或超过更大prompted judge，并降低version/cost门槛。
- **What It Does Not Prove:** 不证明与人类价值普遍一致、不消除position/self-preference，也不证明同一judge可评自己或分布外任务。
- **Limitations / Threats to Validity:** synthetic critique teacher bias、benchmark overlap、arena selection与rubric shift；aggregate平均可能掩盖任务失败。
- **Trade-offs / New Failure Modes:** 低成本/固定artifact换来domain coverage与更新负担；judge版本漂移会改变历史分数，correlated error会污染release gate。
- **Where the Previous Design Still Applies:** 高风险/新domain仍需人审；通用大judge适合低频复杂rubric；rule/verifier适合可执行correctness。
- **Evolution Relationship:** `Layering / Dependency`：human review→prompted LLM judge→specialized small judge→calibrated ensemble/human escalation。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `PLATFORM-MODEL-REGISTRY` Ch59、`PLATFORM-MONITORING` Ch67。
- **Target and Adjacent Chapters Read:** 已核对 Ch59、Ch66～69、Ch73 的judge artifact/evidence/release ownership。
- **Existing Coverage:** Books已有judge uncertainty与versioning；本报告提供small-judge案例，正文判断延后。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把leaderboard平均写成通用可靠性。
- **Open Questions:** calibration、人类disagreement、cross-language/domain、judge更新后的历史replay与ensemble correlated failure。

### Early External Safety Testing of o3-mini

- **Candidate / Week / Score:** Early external o3-mini safety testing / 2025-W05 / 22/30。
- **Source Family ID:** `o3-mini-external-astral-predeployment-safety-test`。
- **Source Type:** arXiv v1 external pre-deployment evaluation。
- **First-public Date / Revision History:** v1 2025-01-29；测试early beta，不等于1月31日release build。
- **Direct Primary Sources:** https://arxiv.org/html/2501.17749v1；https://arxiv.org/abs/2501.17749。
- **Related Primary Sources:** ASTRAL prior paper与OpenAI o3-mini system card用于方法/release边界，不合并版本结论。
- **Access and Verification Status:** Verified；generation pipeline、two test suites、manual confirmation、taxonomy与discussion可访问。
- **Full-read Coverage:** 已读RAG/few-shot/topic-seeding prompt generation、LLM classifier、manual adjudication、10,080 inputs、category counts、comparisons与threats。
- **Original Problem:** 静态safety benchmark会陈旧且易污染；pre-deployment外部tester需要自动生成新攻击并处理oracle成本。
- **Why the Previous Design Was Reasonable:** 固定benchmark可复现、便于版本比较；人工red team质量高且能理解policy语境。
- **Changed Constraint:** safety taxonomy、新闻语境和攻击措辞快速变化，人工生成/标注无法覆盖大输入空间。
- **Mechanism:** ASTRAL用RAG、few-shot与topic/style seeds生成unsafe prompts；目标模型响应后由LLM evaluator初筛，再人工确认unsafe/unknown样本。
- **State Ownership:** generator拥有prompt provenance；target beta拥有response；judge拥有provisional class；human reviewer拥有confirmed label；policy taxonomy定义violation语义。
- **Control Flow / Data Flow:** retrieve context→generate prompt→query target→automatic classify safe/unsafe/unknown→manual review flagged cases→category/report aggregation。
- **Implementation Details:** 14 categories、10,080 inputs、87 manually confirmed unsafe；safe-but-policy-violation与unknown单列，避免二元标签丢失。
- **Evaluation Setup:** 两个test suites、三种generation variants；与作者此前对旧模型的ASTRAL结果做非完全同版本比较。
- **Baselines / Ablations / Sensitivity:** RAG、RAG+FS、RAG+FS+topic seed；manual confirmation揭示judge false positives/unknown。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** early o3-mini beta、API-like testing；内部model/hardware/decoding与release parity未披露。
- **What the Evidence Actually Proves:** 动态prompt generation + human escalation能在特定beta暴露未被automatic judge可靠处理的unsafe cases。
- **What It Does Not Prove:** 不证明release o3-mini的总体unsafe rate、优于历史模型，也不证明未被flag样本安全；分母不是部署流量分布。
- **Limitations / Threats to Validity:** beta/release drift、LLM judge selection bias、只人工复核subset、policy interpretation与历史comparison不等价。
- **Trade-offs / New Failure Modes:** 提高新颖攻击覆盖，却降低严格复现；RAG可带入污染/敏感内容；judge漏报决定人工看不到什么。
- **Where the Previous Design Still Applies:** 固定regression suite适合release gate；专家red team适合高风险category；生产monitor负责真实流量而非替代测试。
- **Evolution Relationship:** `Layering / Dependency`：static benchmark→generated/adaptive tests→judge triage→human confirmation→versioned release/production evidence。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `PLATFORM-EVALUATION-SYSTEM` Ch66、`PLATFORM-MONITORING` Ch67。
- **Target and Adjacent Chapters Read:** 已核对 Ch66～73 的policy taxonomy、sampling、evaluator与release gate。
- **Existing Coverage:** Books已有dynamic red-team和human escalation；本研究提供beta-version caution案例，正文判断延后。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不引用跨版本“更安全”结论作为事实。
- **Open Questions:** full-sample manual audit、release parity、judge recall calibration、prompt provenance privacy与production drift linkage。

### Virus: Harmful Fine-tuning Attack

- **Candidate / Week / Score:** Virus harmful fine-tuning attack / 2025-W05 / 23/30。
- **Source Family ID:** `virus-bilevel-harmful-finetuning-guardrail-bypass`。
- **Source Type:** arXiv v1 adversarial fine-tuning study + author code。
- **First-public Date / Revision History:** v1 2025-01-29；按 v1归档。
- **Direct Primary Sources:** https://arxiv.org/html/2501.17433v1；https://github.com/git-disl/Virus。
- **Related Primary Sources:** harmful fine-tuning、GCG与moderation baselines承担比较。
- **Access and Verification Status:** Verified；threat model、bilevel objective、algorithm、experiments、ablations与limitations可访问。
- **Full-read Coverage:** 已读guardrail pipeline、mixed-data gradient target、moderation bypass objective、GCG optimization、harmful ratio/model experiments与defense discussion。
- **Original Problem:** fine-tuning service只在数据入口做moderation；攻击者可提交表面benign但训练梯度近似harmful data的样本，绕过content filter后改变模型行为。
- **Why the Previous Design Was Reasonable:** 输入moderation低成本、可解释，能挡直接harmful samples；训练后再全量安全评估昂贵。
- **Changed Constraint:** 可微/可查询guard model与victim gradient提供optimization surface，data semantics与training effect不再一致。
- **Mechanism:** 双目标优化token：一项使guard判benign，一项使victim更新梯度接近benign+harmful mix；以GCG迭代离散token，随后用于fine-tuning。
- **State Ownership:** provider guard拥有ingress label；attacker拥有poison data；trainer拥有parameter update；post-train safety evaluator应拥有最终行为证据。
- **Control Flow / Data Flow:** benign/harmful seed→计算victim gradient target→对input token做bilevel/GCG优化→moderation通过→fine-tune→harmfulness评估。
- **Implementation Details:** paper报告100% leakage与高gradient cosine的受控案例；harmful ratio、models与utility accuracy被同时检查。
- **Evaluation Setup:** 多attack baselines、harmful proportions、harmful score与finetune accuracy；guardrail moderation在环。
- **Baselines / Ablations / Sensitivity:** benign fine-tuning、mixing attack、guardrail jailbreak、只优化单目标与Virus；比较gradient similarity/leakage。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** victim/guard与训练设置在论文中披露；生产service、hidden moderation、rate limit与SLO不等价。
- **What the Evidence Actually Proves:** 在作者white/gray-box-like设置，ingress content moderation不足以保证parameter-update safety；训练效果需要独立验证。
- **What It Does Not Prove:** 不证明所有闭源fine-tuning服务可被同法攻击，也不证明公开moderation实现与生产相同。
- **Limitations / Threats to Validity:** access/gradient assumptions、有限模型与taxonomy；真实provider可能有data/behavior/anomaly多层防御。
- **Trade-offs / New Failure Modes:** 更强data scanning增加false positives但仍可能漏掉gradient-aligned poison；post-train eval增加成本且可能被adaptive attack优化。
- **Where the Previous Design Still Applies:** ingress moderation仍挡显式滥用并减少攻击面，但必须与data provenance、training anomaly与post-train regression组合。
- **Evolution Relationship:** `Direct Evolution`：content-only input guard→update-aware data risk→post-training behavioral gate→continuous artifact governance。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `TRAIN-DATA` Ch27、`TRAIN-SFT` Ch29、`PLATFORM-MODEL-REGISTRY` Ch59。
- **Target and Adjacent Chapters Read:** 已核对 Ch27～31、Ch59、Ch66、Ch72～73 的training/artifact security boundary。
- **Existing Coverage:** Books已有fine-tuning supply-chain threat；该论文提供gradient-effect反例，正文判断延后。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不提供可操作攻击步骤之外的必要机制概述。
- **Open Questions:** black-box transfer、secure enclave训练、gradient anomaly detection、post-train red-team coverage与customer rollback contract。

### Underthinking / Thought Switching Penalty

- **Candidate / Week / Score:** Underthinking / Thought Switching Penalty / 2025-W05 / 22/30。
- **Source Family ID:** `underthinking-thought-switching-penalty`。
- **Source Type:** arXiv v1 reasoning-analysis and decoding paper。
- **First-public Date / Revision History:** v1 2025-01-30；后续版本不改变owner。
- **Direct Primary Sources:** https://arxiv.org/html/2501.18585v1；https://arxiv.org/abs/2501.18585。
- **Related Primary Sources:** QwQ-32B-Preview、DeepSeek-R1与MATH/GPQA/AIME作为tested artifacts。
- **Access and Verification Status:** Verified；metric、thought segmentation、decoding penalty、experiments、sensitivity与cases可访问。
- **Full-read Coverage:** 已读underthinking definition、difficulty/token/switch analysis、transition-token heuristic、Tip equations、α/β settings、benchmark comparisons与failure interpretation。
- **Original Problem:** 增加reasoning tokens不保证深度；模型可能频繁切换“alternative”路径，消耗更多token却未充分探索任何一条。
- **Why the Previous Design Was Reasonable:** 标准sampling让模型自由终止/转向，保持训练分布；更高temperature或长budget鼓励多样探索。
- **Changed Constraint:** long-CoT使token budget成为系统资源，必须区分productive depth、必要backtracking与无效switching。
- **Mechanism:** 用thought-transition词和正确轨迹比例定义underthinking指标；Tip在新thought开始后的β tokens内对switch词logits减α，延迟再次切换。
- **State Ownership:** decoder拥有current thought start、penalty window与budget；heuristic词表定义switch event；evaluator拥有correctness/efficiency label。
- **Control Flow / Data Flow:** decode token→检测transition→更新Ψ→窗口内调整switch logits→继续采样→按answer correctness和thought allocation评估。
- **Implementation Details:** 无需finetune；在QwQ上验证Tip，分析QwQ/DeepSeek-R1；α/β是runtime policy而非模型内学得能力。
- **Evaluation Setup:** MATH500、GPQA Diamond、AIME2024；比较correct/incorrect token use、thought counts与Tip accuracy。
- **Baselines / Ablations / Sensitivity:** standard decoding与不同penalty强度/时长；难度与模型对照；transition检测依赖lexical heuristic。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** models/benchmarks与token counts披露；hardware/concurrency/TTFT-TPOT和真实cost未完整披露。
- **What the Evidence Actually Proves:** 在可见CoT和三项benchmark中，长而错误回答常伴更频繁switch；简单logit policy可改变该行为并改善部分结果。
- **What It Does Not Prove:** 不证明switching是错误的唯一因果，也不证明隐藏reasoning或开放任务适用；抑制转向可能阻止必要backtracking。
- **Limitations / Threats to Validity:** thought segmentation/transition词主观；只两个model family、数学/科学任务；accuracy改善可能来自长度变化。
- **Trade-offs / New Failure Modes:** 增强局部坚持却可能造成错误路径锁定、重复、长延迟和语言依赖；runtime需要新state和观测。
- **Where the Previous Design Still Applies:** standard decoding适合短答案；多路径/parallel search适合可验证任务；必要backtracking不应被一律惩罚。
- **Evolution Relationship:** `Alternative Branch`：固定/增大budget→测量productive token→switch-aware decoding→未来adaptive stop/backtrack policy。
- **ROADMAP Node:** `MODEL-SAMPLING`（Ch20）主 owner；handoff `INFER-SCHEDULING` Ch56、`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch19～22、Ch42～44、Ch56、Ch66 的decode state和evaluation contract。
- **Existing Coverage:** s1拥有budget forcing；Tip是同周相反压力“更多token≠更深”，需要family联读后再决定正文。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把lexical metric当作faithful reasoning measure。
- **Open Questions:** language/model-independentthought boundary、必要backtracking识别、SLO-aware adaptive policy与hidden-CoT可观测性。

### GuardReasoner

- **Candidate / Week / Score:** GuardReasoner / 2025-W05 / 24/30。
- **Source Family ID:** `guardreasoner-reasoning-sft-hard-sample-dpo`。
- **Source Type:** arXiv v1 safeguard model paper + open data/code/models。
- **First-public Date / Revision History:** v1 2025-01-30；artifact作为同family。
- **Direct Primary Sources:** https://arxiv.org/html/2501.18492v1；https://github.com/yueliu1999/GuardReasoner。
- **Related Primary Sources:** Llama Guard、WildGuard、HarmBench、SafeRLHF等定义baselines/tasks。
- **Access and Verification Status:** Verified；data generation、R-SFT、hard-sample DPO、13 benchmarks、ablations、appendix与artifacts可访问。
- **Full-read Coverage:** 已读127K/460K data、reasoning trace construction、self/ensemble hard preferences、1B/3B/8B training、three guard tasks与case studies。
- **Original Problem:** label-only guard难处理隐晦、多步和policy-dependent harm；通用LLM+CoT成本高且解释未专门校准。
- **Why the Previous Design Was Reasonable:** classifier/label-only guard低延迟、输出稳定、易接入policy engine；规则模型适合明确taxonomy。
- **Changed Constraint:** safety inputs/outputs更复杂，guard既要判定又要说明依据并跨benchmark泛化。
- **Mechanism:** 构造含详细reasoning steps的guard dataset，用R-SFT学习判定链；再从hard samples构造self/ensemble preference做DPO。
- **State Ownership:** policy schema拥有类别定义；training data拥有reasoning/label provenance；guard model输出reasoning+label；gateway/policy engine拥有最终enforcement。
- **Control Flow / Data Flow:** input/response+policy→guard reasoning→moderation label→policy action；training为synthetic/curated traces→R-SFT→hard-sample pair→DPO。
- **Implementation Details:** 1B/3B/8B open models；13 benchmarks覆盖prompt/response harmfulness与related tasks；ensemble preference通常优于self。
- **Evaluation Setup:** 25 models、多guard benchmarks、F1与weighted average；比较API、general LLM+CoT、专用guard。
- **Baselines / Ablations / Sensitivity:** vanilla、R-SFT、R-SFT+HS-DPO self/ensemble；model size与reasoning visibility比较。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** sizes/data/benchmarks披露；hardware、precision、reasoning-token latency、production concurrency/SLO未完整披露。
- **What the Evidence Actually Proves:** 在作者13-benchmark范围，显式reasoning supervision和hard-sample preference改善专用guard F1及可读解释。
- **What It Does Not Prove:** 不证明reasoning faithful、可防adaptive attack或优于所有API；F1平均不定义业务operating point。
- **Limitations / Threats to Validity:** synthetic trace/teacher bias、taxonomy mismatch、benchmark contamination、reasoning leakage与cost；unsafe corpus本身需治理。
- **Trade-offs / New Failure Modes:** 提高复杂判定能力，却增加latency、prompt injection surface、explanation-policy inconsistency和sensitive reasoning logging风险。
- **Where the Previous Design Still Applies:** label-only small guard适合高QPS初筛；deterministic rules适合硬policy；human review负责高影响/uncertain cases。
- **Evolution Relationship:** `Layering / Dependency`：rules/classifier→specialized guard→reasoning guard→uncertainty/human escalation，而非单一模型替代全部层。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `PLATFORM-GATEWAY` Ch62、`PLATFORM-EVALUATION-SYSTEM` Ch66、`PLATFORM-LOGGING` Ch68。
- **Target and Adjacent Chapters Read:** 已核对 Ch62、Ch66～73 的guard placement、policy/evidence/logging contract。
- **Existing Coverage:** Books已有guardrail分层与uncertainty；该论文是reasoning-guard实验分支，正文判断延后。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不外推作者平均F1或把reasoning当忠实解释。
- **Open Questions:** calibrated abstention、policy versioning、adversarial robustness、reasoning redaction与gateway latency budget。

### SANA 1.5

- **Candidate / Week / Score:** SANA 1.5 / 2025-W05 / 24/30。
- **Source Family ID:** `sana-linear-dit-train-inference-scaling`。
- **Source Type:** arXiv v1 text-to-image systems/model paper。
- **First-public Date / Revision History:** v1 2025-01-30；按 v1归档。
- **Direct Primary Sources:** https://arxiv.org/html/2501.18427v1；https://arxiv.org/abs/2501.18427。
- **Related Primary Sources:** SANA 1.0、DiT baselines与VLM judge用于ancestry/evaluation。
- **Access and Verification Status:** Verified；growth/pruning/inference scaling、training、ablation、misuse与appendices可访问。
- **Full-read Coverage:** 已读linear attention DiT、depth growth、8-bit optimizer、block importance pruning、sampling-vs-step scaling、VLM selection、data SFT与misuse。
- **Original Problem:** 直接训练更深DiT昂贵；deployment又需模型尺寸/latency分支；增加denoising steps并不总如多样sample+verifier有效。
- **Why the Previous Design Was Reasonable:** 从头训练单一规模最简单，固定steps提供确定latency；post-hoc pruning避免维护多训练pipeline。
- **Changed Constraint:** 需要复用较小checkpoint扩到4.8B，同时生成多个部署尺寸，并把额外inference compute分配给最有效策略。
- **Mechanism:** 按block importance插入/初始化新层做depth growth；反向用importance指导pruning；inference生成多samples并用fine-tuned VLM选择，比较增加steps。
- **State Ownership:** base checkpoint/optimizer拥有training state；growth/pruning policy拥有layer lineage；sampler拥有candidate set；VLM judge拥有selection score。
- **Control Flow / Data Flow:** 1.6B checkpoint→grow layers→continued train/SFT→importance prune variants；prompt→N samples→VLM score/select→output。
- **Implementation Details:** final4.8B/60 layers；64 A100（8 DGX）、global batch1024–4096；8-bit optimizer与高质量data SFT组合。
- **Evaluation Setup:** text-to-image FID/CLIP/GenEval/DPG，A100 BF16；throughput batch10、latency batch1/20 steps；inference scaling最多2048 samples。
- **Baselines / Ablations / Sensitivity:** optimizer、initialization、block importance、growth/pruning size、steps vs sample count、judge与data tuning。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** A100 BF16，batch/steps明确；prompt mix、judge cost、2048-sample总GPU-hours与production SLO并未完整统一。
- **What the Evidence Actually Proves:** 在作者T2I setup，checkpoint growth/pruning可形成可复用模型族；额外compute的分配策略比单纯“更多steps”重要。
- **What It Does Not Prove:** 不证明linear DiT或best-of-N普遍优于AR/diffusion baselines，也不证明2048 samples具生产经济性。
- **Limitations / Threats to Validity:** VLM judge bias、作者benchmark、候选采样总成本、data/licensing与misuse；multiple interventions归因耦合。
- **Trade-offs / New Failure Modes:** growth复用training investment但有initialization shock；pruning降延迟但损能力；best-of-N提质却线性放大compute与judge correlated error。
- **Where the Previous Design Still Applies:** 固定小模型/steps适合严格latency；从头训练适合architecture变更；人工选择适合高价值创作。
- **Evolution Relationship:** `Direct Evolution`：single-scale training→checkpoint growth→importance-derived model family→inference candidate generation+selection。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `TRAIN-CHECKPOINT` Ch35、`INFER-SCHEDULING` Ch56、`PLATFORM-COST` Ch70。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～25、Ch28、Ch35、Ch56、Ch66/70 的artifact/candidate/evaluator cost。
- **Existing Coverage:** Books已有diffusion iterative correction与best-of-N成本；本论文提供同family联合案例，正文判断延后。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；所有性能数字绑定A100/BF16/batch/steps。
- **Open Questions:** judge compute accounting、candidate diversity collapse、layer-lineage registry、pruned model calibration与安全filter placement。

### WildChat-50M

- **Candidate / Week / Score:** WildChat-50M / 2025-W05 / 23/30。
- **Source Family ID:** `wildchat-50m-synthetic-posttraining-data-mix`。
- **Source Type:** arXiv v1 dataset/systematic post-training study + released artifacts。
- **First-public Date / Revision History:** v1 2025-01-30；dataset updates需按artifact version另核验。
- **Direct Primary Sources:** https://arxiv.org/html/2501.18511v1；https://arxiv.org/abs/2501.18511。
- **Related Primary Sources:** WildChat prompts、Tulu-3 mix、50 data-generating models与judge benchmarks为dependencies。
- **Access and Verification Status:** Verified；generation pipeline、runtime/VRAM analysis、data mix、SFT evaluation、judge preference analysis与limitations可访问。
- **Full-read Coverage:** 已读50-model generation、1M+ conversations/model、multi-turn composition、DGM quality/cost、Re-Wild filtering/mix、SFT baselines与preference heritability。
- **Original Problem:** academic post-training缺大规模可比较synthetic corpora；只看teacher benchmark无法知道生成cost、style/factuality如何传给student。
- **Why the Previous Design Was Reasonable:** 单强teacher生成简单、质量较高且pipeline易控制；人工/公开instruction data更接近真实分布。
- **Changed Constraint:** 需要测量不同size/architecture DGM在同prompt corpus上的质量、成本与student downstream effect，并避免依赖单闭源teacher。
- **Mechanism:** 50个0.5B～104B open models各参与百万级multi-turn conversations，记录runtime/VRAM；从数据中构造Re-Wild mix训练Llama-3.1-8B Base并对比。
- **State Ownership:** prompt corpus拥有source/license；DGM version/config拥有generation provenance；conversation turn拥有parentage；data mixer拥有filter/weights；student checkpoint拥有training lineage。
- **Control Flow / Data Flow:** real prompt seed→多DGM生成multi-turn transcripts→quality/cost分析→filter/remix→SFT→ground-truth与LLM-judge evaluation。
- **Implementation Details:** 约125M transcript turns；模型每conversation平均2–3 turns；比较DGM style/factuality与VRAM/runtime。
- **Evaluation Setup:** Re-Wild vs Tulu-3等SFT mixes；MT-Bench、preference rates及standard post-training benchmarks；人工抽查judge反转案例。
- **Baselines / Ablations / Sensitivity:** DGM identity/size、data mix、judge preference与factuality/style分析；不同judge可能继承teacher偏好。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** generation runtime/VRAM按模型记录；统一fleet/hardware、energy、prompt length分布和SLO需查artifact，不能汇总成单一成本。
- **What the Evidence Actually Proves:** DGM选择影响synthetic data的style/factuality和student结果；数据生成器本身应成为versioned training dependency。
- **What It Does Not Prove:** 不证明更多synthetic data单调更好、不证明judge preference等于事实质量，也不证明Re-Wild普遍优于所有human data。
- **Limitations / Threats to Validity:** prompt/privacy/licensing、teacher contamination、judge heritability、model-version与generation config巨大；大corpus难完全审计。
- **Trade-offs / New Failure Modes:** 开放多teacher提高多样性/可研究性，却放大provenance、重复、toxicity、style bias、storage与regeneration成本。
- **Where the Previous Design Still Applies:** 高质量human data用于关键行为；单teacher适合可控domain；retrieval/ground-truth verifier适合事实型任务。
- **Evolution Relationship:** `Direct Evolution`：single-source demonstrations→synthetic teacher data→multi-DGM comparative corpus→lineage-aware data mix/evaluation。
- **ROADMAP Node:** `TRAIN-DATA`（Ch27）主 owner；handoff `TRAIN-SFT` Ch29、`PLATFORM-EVALUATION-SYSTEM` Ch66、`PLATFORM-COST` Ch70。
- **Target and Adjacent Chapters Read:** 已核对 Ch27～29、Ch59、Ch66/70/72 的data lineage、artifact与governance。
- **Existing Coverage:** Books已有synthetic data provenance；该论文提供DGM-as-dependency证据，正文判断延后。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把LLM-judge preference当ground truth。
- **Open Questions:** transcript privacy/license、dedup/contamination、DGM config reproducibility、data revocation与quality-cost Pareto front。

### MedXpertQA

- **Candidate / Week / Score:** MedXpertQA / 2025-W05 / 22/30。
- **Source Family ID:** `medxpertqa-expert-multimodal-medical-evaluation`。
- **Source Type:** arXiv v1 benchmark paper + official dataset/repository。
- **First-public Date / Revision History:** v1 2025-01-30；v2 2025-02-20；v3 2025-06-06；本周按v1，revision用于同family核验。
- **Direct Primary Sources:** https://arxiv.org/pdf/2501.18362v1；https://arxiv.org/abs/2501.18362；https://github.com/TsinghuaC3I/MedXpertQA。
- **Related Primary Sources:** source exams/medical benchmarks与evaluated model cards定义data/evaluation context。
- **Access and Verification Status:** Verified；HTML错配以v1 PDF、abs与repository闭合；v1/v3 model-count差异保留revision boundary。
- **Full-read Coverage:** 已读data sources、hierarchical/AI filtering、rewriting/option augmentation、physician review、Text/MM splits、reasoning subset、model evaluation与limitations。
- **Original Problem:** 旧medical benchmark范围窄、难度饱和，多模态题常由image caption自动生成，缺真实临床信息与专科决策复杂度。
- **Why the Previous Design Was Reasonable:** licensing/annotation成本使公开exam和caption-derived VQA易规模化；单一choice accuracy便于比较。
- **Changed Constraint:** frontier models需要更难、多专科、多image type和复杂clinical context，同时必须控制训练污染与错误标注。
- **Mechanism:** 汇集licensing/specialty exams与image-rich sources；按human difficulty、8 AI experts/14 votes、semantic duplicate过滤；重写题干/扩充distractors，最终由持证医师review。
- **State Ownership:** source/license拥有原题约束；transformation pipeline拥有synthetic lineage；physician review拥有最终correction；benchmark version拥有split/answer identity。
- **Control Flow / Data Flow:** source questions→difficulty/model filtering→dedup→rewrite/option augmentation→expert review→Text/MM/reasoning subsets→model evaluation。
- **Implementation Details:** 4460 questions、17 specialties、11 systems；MM 2005 questions/2839 images；v1评16 models，后续摘要为18，不能混用。
- **Evaluation Setup:** text/multimodal multiple choice与reasoning subset；比较proprietary/open models，按specialty/system/task分析。
- **Baselines / Ablations / Sensitivity:** 与MedQA/MedMCQA/MMLU medical及传统medical VQA比较；数据pipeline各环节并非完整因果ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model API/version和prompt需查表；hardware/precision多为closed-model Not Disclosed，非deployment SLO。
- **What the Evidence Actually Proves:** benchmark design把难度、专科coverage、multimodal clinical context与human review提升为显式evaluation data contract。
- **What It Does Not Prove:** multiple-choice正确不等于临床安全/完整diagnosis，不证明synthetic rewrite消除contamination，也不支持真实部署。
- **Limitations / Threats to Validity:** exam-to-clinic gap、US-centric sources、licensing/privacy、closed model drift、option artifacts和expert disagreement。
- **Trade-offs / New Failure Modes:** 提高难度/coverage却牺牲开放式决策真实性；rewrite减污染但可能引入语义错误，expert review成本高且会版本漂移。
- **Where the Previous Design Still Applies:** 基础benchmark适合回归/能力分层；真实临床评测需longitudinal workflow、calibration、human oversight与安全outcome。
- **Evolution Relationship:** `Direct Evolution`：caption VQA/通用exam→专科多模态exam→reasoning subset→未来workflow/executable clinical evaluation。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `MULTIMODAL-REPRESENTATION` Ch23、`PLATFORM-SECURITY` Ch72。
- **Target and Adjacent Chapters Read:** 已核对 Ch23、Ch66～73 的domain evaluation/data governance boundary。
- **Existing Coverage:** Books已有domain-specific evaluation contract；本benchmark是medical受限案例，正文判断延后。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；v1/v3数字分别标注，不混合revision。
- **Open Questions:** contamination audit、expert disagreement、open-ended clinical actions、patient safety outcome与dataset license/revocation。

### PhysBench

- **Candidate / Week / Score:** PhysBench / 2025-W05 / 22/30。
- **Source Family ID:** `physbench-physical-world-evaluation-and-physagent`。
- **Source Type:** arXiv v1/v2 论文 + 作者项目页 + 官方评测 repository/dataset。
- **First-public Date / Revision History:** v1 2025-01-27；v2 2025-01-29；本周按 v1 归档，v2 用于
  完整 HTML、附录和 revision 边界复核；repository 显示 2024-12 已先行发布部分评测结果，但论文事件
  仍按可唯一定位的 arXiv v1 归属 W05。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.16411；
  https://arxiv.org/html/2501.16411v2；https://physbench.github.io/；
  https://github.com/physical-superintelligence-lab/PhysBench。
- **Related Primary Sources:** 作者公开的 Hugging Face dataset 与 EvalAI leaderboard 用于 dataset/version
  identity；被评模型各自 model card 定义输入能力，不证明 PhysBench 的通用外部有效性。
- **Access and Verification Status:** Verified；arXiv HTML 2076 行全文、appendices、project page、dataset
  contract 与 evaluation repository 可访问；repository 同时披露 training split、3D assets 与剩余代码在
  当时尚未全部发布，因此 artifact completeness 不是 Full。
- **Full-read Coverage:** 已读 metadata/revisions、Introduction/Related Work、四类/19 子类任务、五步数据
  流水线、annotation/quality/contamination protocol、75 个 VLM 的三类输入设置、相关性与 error analysis、
  PhysAgent 三阶段流程、prompt/oracle baselines、knowledge-transfer 与 embodied experiments、全部关键
  appendices、limitations、reproducibility 声明和 repository evaluation path。
- **Original Problem:** 通用 VQA 主要测识别、常识和语言推理，不能区分模型是否理解质量、摩擦、深度、
  光照、碰撞和流体等会影响物理行动的属性与动态；因此 VLM 在普通 benchmark 的高分无法直接成为
  embodied agent 的安全证据。
- **Why the Previous Design Was Reasonable:** 单图 VQA、模拟刚体 benchmark 与预定义 physics module 更易
  收集、标注和自动评分，也能隔离特定 perception/reasoning 能力；在封闭任务中，规则化 oracle 的
  failure surface 更小。
- **Changed Constraint:** VLM 开始承担开放语言条件下的 embodied planning，需要同时处理真实、模拟、
  image、video 与 interleaved evidence，并区分 perception、knowledge、reasoning 和 execution errors。
- **Mechanism:** PhysBench 用 web、simulation 与 real-world captures 构造 10,002 个 test entries，按
  object property、relationship、scene、dynamics 四域组织；PhysAgent 先按任务激活物理知识 prompt，再
  调用 Depth Anything、SAM、GroundingDINO 等视觉 foundation model，最后由 VLM reasoning/self-check
  综合答案。
- **State Ownership:** benchmark version 拥有 question/media/answer/split identity；annotation pipeline
  拥有 source、physical-principle、caption、question 与 review lineage；PhysAgent orchestration 拥有
  task class、retrieved knowledge、tool outputs 与 reasoning context；robot environment 才拥有真实/模拟
  action outcome，不能由 benchmark answer state 替代。
- **Control Flow / Data Flow:** media collection→caption/physical-principle annotation→question generation→
  automatic filtering + expert review→task/capability classification→model-specific image/video/interleaved
  adaptation→answer extraction/scoring；PhysAgent 为 question→task activation→vision tools + knowledge
  memory→VLM reasoning/self-check→answer，embodied branch 再把输出交给 MOKA controller 执行。
- **Implementation Details:** test 为 10,002 entries，另有 200-entry validation；来源含 Blender simulation、
  web 与 real captures。evaluation 使用 VLMEvalKit，多数模型 temperature=0；不支持 multi-image 的模型
  使用 frame merge 或 sequential input，导致不同模型并非完全同一 observation contract。
- **Evaluation Setup:** 75 个 VLM 分 image、video、general/interleaved 三类；test subset 对 general model
  为 10,002，而 image/video 去除 interleaved entries。另在 200-entry subset 比较 prompting、ContPhy 与
  PhysAgent，并在 MuJoCo、Franka Emika、MOKA 上测试 5 类 manipulation task。
- **Baselines / Ablations / Sensitivity:** 与 15 个 VLM benchmarks 比相关性；比较 model/data/frame scaling、
  CoT、description-CoT、pure-language reasoning、ContPhy、PhysAgent、few-shot/fine-tune knowledge transfer
  和 visual prompting。论文没有对 PhysAgent 的 memory、task classifier、各视觉工具和 self-check 做
  完整 factorial ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 论文披露各模型规模、输入适配、
  prompt/hyperparameters，但闭源模型 hardware/precision、batch/concurrency 与 serving SLO 为
  `Not Disclosed`；robot study 是小规模 simulation task，不是 production control-loop SLO。
- **What the Evidence Actually Proves:** 在作者定义的 multiple-choice contract 中，大量 VLM 在物理属性、
  场景和动态上仍有明显 gap；输入表示和任务类别会改变可比性；作者实验表明显式 perception tools 与
  physics memory 的组合在其 subset 上优于若干 prompting/oracle baselines，并在 5 个 simulation tasks
  中减少部分 reasoning errors。
- **What It Does Not Prove:** 不证明 multiple-choice accuracy 等价于可校准的 world model，不证明
  PhysAgent 的 18.4% 相对提升可跨模型/数据/真实机器人泛化，不证明物理知识缺失是唯一因果来源，
  也不证明 reasoning improvement 必然降低 execution error 或满足 physical safety。
- **Limitations / Threats to Validity:** 数据仍不覆盖真实物理世界全貌，部分来自既有数据并有版权/污染
  风险；GPT-4o-mini answer extraction 会 hallucinate；multiple choice 简化开放式 reasoning；不同模型
  的 frame merge/sequence 适配破坏严格同分布比较；作者承认少量 annotation error 仍可能存在。
- **Trade-offs / New Failure Modes:** 更广物理 taxonomy 与 interleaved media 提升诊断覆盖，却引入昂贵
  annotation、media/license/version lineage、输入适配偏差和 evaluator error；tool-augmented PhysAgent
  可补 perception/knowledge，却新增 task misclassification、tool invocation、信息损失、memory staleness
  与 tool-output provenance failure。
- **Where the Previous Design Still Applies:** 单图 VQA 适合低成本回归，窄域 simulator 适合可控因果实验，
  规则 physics module 在任务封闭且 safety envelope 明确时仍更可验证；真实机器人 release 仍需 control
  frequency、calibration、action safety、human override 与 failure recovery 证据。
- **Evolution Relationship:** `Layering / Dependency`：通用 VQA→physical benchmark→error decomposition→
  tool/memory-assisted perception reasoning→embodied execution；benchmark、world model 与 controller 是
  不同层，不能写成直接替代关系。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff
  `MULTIMODAL-REPRESENTATION`（Ch23）、`MULTIMODAL-WORLD-MODELS`（Ch25）、
  `MULTIMODAL-EMBODIED-VLA`（Ch26）与 `PLATFORM-SECURITY`（Ch72）。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～26 与 Ch66～73，确认 representation、world state、
  action outcome、evaluation evidence 与 physical safety 的 owner 不混合。
- **Existing Coverage:** Books 已区分 perception、world-state prediction、physical action 和 executable
  evaluation；本 family 提供重要受限案例，但是否 refine 由后续 Books Integration 单独决定。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；本阶段不修改 Books，也不把作者 improvement 数字
  提升为通用设计结论。
- **Open Questions:** 是否能建立同一 observation contract 下的 cross-model evaluation；如何把
  answer accuracy 扩展为 calibrated transition prediction、action outcome 和 physical safety evidence；
  PhysAgent component ablation、真实机器人复现与 dataset version/revocation contract 仍待补强。

### Constitutional Classifiers

- **Candidate / Week / Score:** Constitutional Classifiers / 2025-W05 / 27/30。
- **Source Family ID:** `anthropic-constitutional-classifiers-2025`。
- **Source Type:** Anthropic 作者论文 + 官方 research Blog + 公开 red-team update。
- **First-public Date / Revision History:** arXiv v1 2025-01-31；官方 Blog 2025-02-03；live-demo 结果于 2025-02-13 更新，均作为同一 family 的后续证据而不重复计分。
- **Direct Primary Sources:** https://arxiv.org/html/2501.18837v1；https://arxiv.org/abs/2501.18837；https://www.anthropic.com/news/constitutional-classifiers。
- **Related Primary Sources:** Anthropic Responsible Scaling Policy 与 bug-bounty scope 只定义部署/threat context，不替代论文实验。
- **Access and Verification Status:** Verified；全文、方法、红队协议、automated evaluation、appendix、limitations 和后续 demo failure 均可访问。
- **Full-read Coverage:** 已读 constitution/data generation、input/output classifier、synthetic augmentation、prototype/updated system、human red team、automated attacks、benign traffic、compute/overrefusal、attack taxonomy、appendix 和 limitations。
- **Original Problem:** model-level safety tuning 无法阻止输入变换、长上下文与 universal jailbreak；部署需要独立、可更新的 policy enforcement layer。
- **Why the Previous Design Was Reasonable:** 仅依赖 policy model refusal 路径简单、延迟低且避免额外误拒；静态关键词过滤在封闭 taxonomy 中便宜可审计。
- **Changed Constraint:** 攻击可自适应、跨语言和跨格式，且高危 CBRN policy 需要在模型更新之外快速修订 guard contract。
- **Mechanism:** 用自然语言 constitution 定义 allowed/disallowed classes，合成并扩增 prompts/completions，训练 input 与 output classifiers；请求与生成结果分别过 guard，命中则阻断。
- **State Ownership:** constitution/policy taxonomy 由安全治理层拥有；classifier weights、threshold 与版本由 safeguard service 拥有；policy model 不拥有最终 deployment admission decision。
- **Control Flow / Data Flow:** request→input classifier→policy model→output classifier→allow/block；synthetic generator→augmentation→labeled corpus→classifier training/evaluation→versioned deployment。
- **Implementation Details:** prototype 与改进版并非同一 operating point；benign contractor data 用于降低 overrefusal；完整模型参数、serving topology 与 threshold rollout 细节 Not Disclosed。
- **Evaluation Contract:** 183 active participants、约 3,000 小时、10 个 forbidden queries 的 prototype universal-jailbreak contest；另有 10,000 synthetic attacks、5,000 production conversations 与 Claude 3.5 Sonnet snapshots。
- **Baselines / Ablations / Sensitivity / Overhead:** 与 unguarded model 比较；论文/Blog披露 updated system 的 jailbreak、overrefusal 与 compute trade-off，但 prototype→updated 改动不是完整独立 ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Claude 3.5 Sonnet June/October 2024 snapshots 已披露；硬件、precision、batch/concurrency、classifier latency tail 与生产 SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在给定 CBRN taxonomy 与攻击协议下，synthetic constitution data 可训练出实用 guard；但后续 demo 确实出现 universal jailbreak，证明“未发现攻击”不是安全证明。
- **What It Does Not Prove:** 不证明 universal robustness、不覆盖所有 harm taxonomy、不证明低平均误拒等价于分群公平，也不证明 classifier 可替代 model training、rate limit、monitoring 与 incident response。
- **Limitations / Threats to Validity:** adaptive attacker、taxonomy drift、synthetic-data blind spots、prototype/updated mismatch、contest success definition 与 production traffic sampling 均限制外推。
- **Trade-offs / New Failure Modes:** defense-in-depth 提高可更新性，却新增 classifier false positive/negative、policy/version skew、双重推理成本、output streaming rollback 与 fail-open/fail-closed 决策。
- **Where the Previous Design Still Applies:** 低风险 workload 可保留 model-native refusal；确定性格式/关键词规则适合 cheap prefilter；高风险场景应与 classifier、monitoring 和 human escalation 叠加。
- **Evolution Relationship:** `Layering / Dependency`：model alignment→external input/output guard→adaptive red team→deployment feedback；不是 guard 取代模型安全训练。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）、`PLATFORM-GATEWAY`（Ch62）与 `PLATFORM-OBSERVABILITY`（Ch67）。
- **Target and Adjacent Chapters Read:** 已核对 Ch62、Ch66～73，确认 policy、operating point、evidence 与 release gate 分层。
- **Existing Coverage:** Books 已要求 threat model、guard operating point 与 release evidence；本 family 提供 synthetic policy compiler→runtime guard→red-team feedback 的受限演进证据。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把 4.4%、0.38% 或 23.7% 脱离攻击/traffic/model contract 写成通用性能事实。
- **Open Questions:** threshold/version 如何原子发布；streaming output 如何撤销；adaptive attack regression set、policy drift 与 incident replay 如何治理。

### ChunkKV

- **Candidate / Week / Score:** ChunkKV / 2025-W05 / 25/30。
- **Source Family ID:** `chunkkv-semantic-kv-compression`。
- **Source Type:** 作者论文 / arXiv + official artifact references。
- **First-public Date / Revision History:** v1 2025-02-01；后续 revision 作为同一 family 演进，不改变 owner week。
- **Direct Primary Sources:** https://arxiv.org/html/2502.00299v1；https://arxiv.org/abs/2502.00299。
- **Related Primary Sources:** H2O、SnapKV、PyramidKV 等只作 token-level compression baselines；LongBench/NIAH/GSM8K/JailbreakV 定义 evaluation contract。
- **Access and Verification Status:** Verified；method、algorithm、experiments、ablation、appendix 与 limitations 可访问。
- **Full-read Coverage:** 已读 chunk importance、semantic grouping、layer-wise index reuse、prefill/decode路径、implementation、LongBench/NIAH/reasoning/safety evaluations、compression sensitivity、chunk-size与index-reuse ablation、limitations。
- **Original Problem:** long-context decode 的 KV memory/attention cost 随 retained token 增长；token-wise pruning 容易破坏语义片段并重复计算每层索引。
- **Why the Previous Design Was Reasonable:** token-level importance 粒度细、适合 sparse salient tokens，且不需要预设 semantic chunk；完整 KV 在高准确性或短上下文时最稳妥。
- **Changed Constraint:** 更长 prompts、aggressive compression 与 instruction/reasoning workload 使局部 token 分数无法保存跨 token 依赖，index selection overhead 也不可忽略。
- **Mechanism:** 以固定 chunk 为 retention unit，根据 chunk importance 保留语义连续片段；利用相邻层 retained-index 相似性复用 index，减少逐层选择开销。
- **State Ownership:** request KV manager 拥有 retained chunk identity、position 与 layer mapping；model runner 执行 gather/attention；eviction 后原始 KV 不可由 decode 自动恢复。
- **Control Flow / Data Flow:** prefill 生成全量 K/V→计算 chunk score→选择 chunks/index→跨层复用或更新 index→压缩 KV 进入后续 decode attention。
- **Implementation Details:** selection 与 cache layout 必须保留 position semantics；固定 chunk size 是核心超参；论文未定义 production eviction rollback、prefix-cache sharing 与 allocator integration。
- **Evaluation Contract:** LongBench、Needle-In-A-Haystack、GSM8K、JailbreakV；覆盖 instruction-tuned 与 reasoning model，比较多个 compression ratio 与 baselines。
- **Baselines / Ablations / Sensitivity / Overhead:** token-level methods 为 baseline；包含 chunk size、compression ratio、layer-wise reuse 与不同 tasks/models 的 sensitivity；端到端 serving tail latency 证据不足。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/benchmark/context 与 compression ratio 按论文披露；统一 GPU、precision、batch/concurrency、allocator fragmentation 与 TTFT/TPOT SLO 并未完整闭合。
- **What the Evidence Actually Proves:** 作者设置下，semantic chunk retention 在 aggressive compression 可优于若干 token-wise baseline，layer reuse 能减少 selection overhead。
- **What It Does Not Prove:** 不证明固定 chunk 对所有语言/代码最佳，不保证精确等价，不证明作者最高提升可跨 model、prompt 或 production scheduler 复现。
- **Limitations / Threats to Validity:** 固定 chunk 难适配语义边界；benchmark 与模型覆盖有限；compression-induced safety/recall failure、prefix identity 和 online workload drift 未充分测量。
- **Trade-offs / New Failure Modes:** memory/attention cost 下降，却新增 lossy eviction、chunk-boundary error、layer index staleness、shared-prefix identity mismatch 与不可逆 recall loss。
- **Where the Previous Design Still Applies:** 短 context、高正确性、低 concurrency 或 cache 有余量时保留全量 KV；token-wise pruning 仍适合稀疏关键信号且语义连续性弱的任务。
- **Evolution Relationship:** `Alternative Branch`：full KV→token-level eviction→semantic chunk retention→layer-index reuse；各分支按质量/内存/选择开销共存。
- **ROADMAP Node:** `INFER-KV-CACHE`（Ch45）主 owner；handoff `INFER-MEMORY-MANAGEMENT`（Ch54）、`MODEL-LONG-CONTEXT`（Ch22）与 `INFER-SCHEDULING`（Ch56）。
- **Target and Adjacent Chapters Read:** 已核对 Ch43～48 与 Ch54～56，区分 model context capability、request KV identity、allocator 与 fleet scheduling。
- **Existing Coverage:** Books 已覆盖 paged allocation 与 KV identity；ChunkKV 补充“保留哪些状态”的 lossy policy，但是否吸收待 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不保留脱离 model/context/compression ratio 的 10% headline。
- **Open Questions:** adaptive chunk boundary、prefix sharing、eviction rollback、distributed KV transfer 与 SLO-aware compression 如何共同定义。

### Reward-Guided Speculative Decoding

- **Candidate / Week / Score:** Reward-Guided Speculative Decoding / 2025-W05 / 24/30。
- **Source Family ID:** `reward-guided-biased-speculative-reasoning`。
- **Source Type:** 作者论文 / arXiv（Experimental）。
- **First-public Date / Revision History:** v1 2025-01-31；v2 2025-02-14；v3 2025-06-26；owner 以 v1 归 W05。
- **Direct Primary Sources:** https://arxiv.org/html/2501.19324v1；https://arxiv.org/abs/2501.19324。
- **Related Primary Sources:** standard speculative decoding、process reward models 与 search methods 只作机制/baseline lineage。
- **Access and Verification Status:** Verified；algorithm、proof、experiments、computation analysis、ablation 与 appendix 可访问。
- **Full-read Coverage:** 已读 mixture distribution、acceptance criterion、optimal threshold proof、RSD algorithm、reasoning/search baselines、FLOP proxy、threshold/PRM/model-merge ablation、additional results 与 discussion。
- **Original Problem:** exact speculative decoding 保持 target distribution，却在 draft/target 分歧大的多步 reasoning 上大量拒绝；始终调用 target 又成本高。
- **Why the Previous Design Was Reasonable:** exactness 给出清晰概率语义和 correctness contract，适合一般生成；target-only 在 reward 不可靠时避免额外 policy bias。
- **Changed Constraint:** reasoning trajectory 可按 step 评价，用户愿意交换分布 exactness、质量与 compute；draft/target gap 使 token-exact acceptance 不再是唯一目标。
- **Mechanism:** draft 生成 reasoning step，process reward model 打分；超过 threshold 接受 draft，否则调用 target 生成该 step，形成 reward-conditioned biased mixture。
- **State Ownership:** decoder controller 拥有 trajectory、threshold 与 routing；draft/target 各自拥有 KV；PRM 拥有 step score，不能视为 ground truth。
- **Control Flow / Data Flow:** prompt+accepted steps→draft step→PRM score→accept 或 target fallback→append trajectory→直到 EOS；每次 fallback 改变后续上下文与两模型 cache path。
- **Implementation Details:** 论文以 step 为 unit 而非并行 token block；threshold 是 cost-quality knob；未公开 production batching、cache reconciliation、failure recovery 或 multi-tenant fairness。
- **Evaluation Contract:** Qwen2.5-Math 1.5B draft/7B target、Skywork-o1 PRM，并扩展更大 target；GSM8K、MATH500、OlympiadBench、GPQA、MMLU-STEM、GaoKao 等 reasoning tasks。
- **Baselines / Ablations / Sensitivity / Overhead:** target-only、parallel decode/search baselines；threshold、reward function、reasoning complexity 和 model merge sensitivity；主要成本指标是 estimated FLOPs。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model family 与 tasks 已披露；硬件、precision、batch/concurrency、真实 wall-clock、TTFT/TPOT 和 serving SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在作者 reasoning/PRM contract 中，step-level reward routing 能减少 target invocations，并建立 bias-quality-cost 的可调分支。
- **What It Does Not Prove:** 不保持 target distribution exactness，不证明 PRM 对开放域可靠，不证明 FLOP reduction 等于延迟/goodput improvement，也不证明 target 每步期望 reward 必然更高。
- **Limitations / Threats to Validity:** reward hacking、threshold calibration、draft/target/PRM correlated error、limited tasks/models 与 FLOP proxy 限制外推。
- **Trade-offs / New Failure Modes:** 降低 target compute，却新增 PRM inference、routing state、distribution shift、错误 step commit、dual-cache divergence 和不可逆 trajectory contamination。
- **Where the Previous Design Still Applies:** exact speculative decoding 适合必须保持 target distribution 的 API；target-only 适合高风险或 reward 不可验证任务；best-of-N/search 适合可并行且预算充足场景。
- **Evolution Relationship:** `Alternative Branch`：exact speculation 保概率语义；reward-guided routing 主动购买 bias 以换取 reasoning quality/compute trade-off。
- **ROADMAP Node:** `INFER-SPECULATIVE-DECODING`（Ch48）主 owner；handoff `MODEL-SAMPLING`（Ch20）、`INFER-SCHEDULING`（Ch56）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已核对 Ch44～50 与 Ch56、66，确认 proposal、verification、commit 与 evidence contract 分层。
- **Existing Coverage:** Books 已区分 exact speculation 与 heuristic proposal；本 family 进一步把 reward controller 明确为有偏分支。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把作者 FLOP 与 accuracy 数字写成通用 serving 结论。
- **Open Questions:** PRM operating point、cache rollback、batched target fallback、fairness 与在线 drift calibration 如何闭合。

### Learning-Rate Scheduling for Large Model Training

- **Candidate / Week / Score:** The Surprising Agreement Between Convex Optimization Theory and Learning-Rate Scheduling for Large Model Training / 2025-W05 / 24/30。
- **Source Family ID:** `convex-theory-large-model-lr-schedules`。
- **Source Type:** 作者论文 / arXiv（theory + empirical）。
- **First-public Date / Revision History:** v1 2025-01-31；v2 2025-07-23；owner 以 v1 归 W05。
- **Direct Primary Sources:** https://arxiv.org/html/2501.18965v1；https://arxiv.org/abs/2501.18965。
- **Related Primary Sources:** SGD convex theory、warmup/stable-decay/cosine schedules 与 LLM training recipes 只作 lineage/baseline。
- **Access and Verification Status:** Verified；theorems、proofs、large-model experiments、ablations、appendix 与 limitations 可访问。
- **Full-read Coverage:** 已读 convex bound、schedule objective、WSD/cosine/linear-decay比较、time-transfer、optimizer/data/model experiments、ablation、appendix proofs 与 limitations。
- **Original Problem:** large-model LR schedule 通常靠 expensive sweeps；不同 training horizon 变更使已调 schedule 难复用。
- **Why the Previous Design Was Reasonable:** cosine decay、warmup 与 WSD 是稳定经验法；小规模 sweep 在固定 token budget 和 optimizer 下可行。
- **Changed Constraint:** model/data/compute scale 提升后，重复 full-run tuning 成本过高，且 horizon 经常在训练中调整。
- **Mechanism:** 用 convex SGD upper bound 解释 schedule 的 cumulative step/noise trade-off，并据此比较/构造可扩展 schedule；将短 horizon 调优信息迁移到更长训练。
- **State Ownership:** trainer/optimizer 拥有 step、base LR、warmup/decay horizon 与 optimizer state；scheduler policy 必须与 checkpoint 恢复和 planned token budget 一致。
- **Control Flow / Data Flow:** configured horizon/shape→per-step LR→optimizer update→loss/validation evidence；延长 horizon 时 schedule state 与 checkpoint 一起迁移，而非仅改 config。
- **Implementation Details:** 理论主要针对 convex SGD；LLM 实验用 AdamW 等非凸设置验证相关趋势，而非证明 theorem 条件成立。
- **Evaluation Contract:** 多个 model sizes、datasets、optimizers 和 schedule families；比较 validation loss、horizon transfer 与 hyperparameter sensitivity。
- **Baselines / Ablations / Sensitivity / Overhead:** cosine、constant/linear、WSD 等；检查 warmup、decay fraction、training duration、optimizer/model/data变化；调参成本仍存在。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** paper 披露各实验 model/data/token budget；硬件、precision、global batch/parallel topology 并非所有结果完整统一，且无 serving SLO。
- **What the Evidence Actually Proves:** convex-style bound 可作为 schedule 设计解释器，并在作者 LLM experiments 中与若干 empirical ordering 一致。
- **What It Does Not Prove:** 不证明非凸 AdamW dynamics 被 convex theory 完整解释，不保证跨 architecture/data/scale 零调参，也不证明某 schedule 永远最优。
- **Limitations / Threats to Validity:** theory-assumption gap、有限 model scale、optimizer/data interaction 与 validation noise；后续 v2 不能反写为 v1 已有证据。
- **Trade-offs / New Failure Modes:** 可减少 blind sweep，却新增对 horizon estimate、scheduler/checkpoint version 和 optimizer coupling 的依赖；错误延长可能造成过早 decay 或恢复不连续。
- **Where the Previous Design Still Applies:** 固定预算且已有成熟 recipe 时 cosine/WSD 仍合理；任务变化大或 instability 强时 empirical sweep 仍必要。
- **Evolution Relationship:** `Principle Reuse`：convex optimization 不是替代 empirical scaling，而是为 schedule family、horizon 与 noise trade-off 提供解释层。
- **ROADMAP Node:** `TRAIN-PRETRAINING`（Ch28）主 owner；handoff `TRAIN-CHECKPOINT`（Ch35）、`TRAIN-DISTRIBUTED-TRAINING`（Ch36）与 `PLATFORM-OBSERVABILITY`（Ch67）。
- **Target and Adjacent Chapters Read:** 已核对 Ch27～30、Ch35～36 与 Ch67，确认 schedule state 属训练 runtime，不是孤立超参表。
- **Existing Coverage:** Books 已覆盖 optimizer/schedule 与 checkpoint；本 family 提供 horizon-change 的理论解释和 failure boundary。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把理论 agreement 写成普适定律。
- **Open Questions:** AdamW/momentum/weight decay 的联合理论、elastic world size 下 effective batch/LR、mid-run horizon extension 与 exact resume 如何验证。

### SafeRAG

- **Candidate / Week / Score:** SafeRAG / 2025-W05 / 24/30。
- **Source Family ID:** `saferag-threat-taxonomy-benchmark`。
- **Source Type:** 作者论文 / benchmark artifact（Experimental）。
- **First-public Date / Revision History:** v1 2025-01-28；v2 2025-02-23；owner 以 v1 归 W05。
- **Direct Primary Sources:** https://arxiv.org/html/2501.18636v1；https://arxiv.org/abs/2501.18636。
- **Related Primary Sources:** RAG systems、retrievers、LLMs 与 attack baselines 只定义被测 stack；不能把其厂商主张并入 SafeRAG。
- **Access and Verification Status:** Verified；taxonomy、dataset construction、attack/defense evaluation、metrics、appendix 和 limitations 可访问。
- **Full-read Coverage:** 已读 silver noise、inter-context conflict、soft advertisement、white DoS 四类 threat，knowledge-base injection、retrieval/generation metrics、models/retrievers、defense comparison、case analysis 与 limitations。
- **Original Problem:** RAG 把外部 corpus 变成运行时输入；传统 LLM safety evaluation 不覆盖 retrieval poisoning、context conflict 和 availability attack。
- **Why the Previous Design Was Reasonable:** 静态可信 corpus 与 offline indexing 时，retrieval relevance/QA accuracy 是主要目标；model guard 可处理直接 malicious prompts。
- **Changed Constraint:** corpus 开放更新、第三方文档与 adversarial content 进入 index 后，data-plane content 可改变 retrieval、answer 和 availability。
- **Mechanism:** 构建多种 poisoned knowledge-base scenarios，分别评估 retriever 是否召回攻击内容、generator 是否采纳，以及 defenses 在 utility/security 两侧的表现。
- **State Ownership:** corpus owner 管文档/provenance；index service 管 chunk/embedding/version；retriever 管 candidate set；generator 只消费 context，不应拥有 source trust 决策。
- **Control Flow / Data Flow:** clean/poisoned documents→chunk/index→query retrieval→ranked context→LLM answer→security/utility evaluator；防御可插在 ingest、retrieve、rerank 或 generate 前后。
- **Implementation Details:** benchmark 是 controlled testbed，不是 production isolation design；index freshness、tenant ACL、delete/rebuild、streaming moderation 与 incident recovery Not Disclosed。
- **Evaluation Contract:** 多 RAG methods、retrievers/LLMs、四 attack classes 与 utility/security metrics；具体 model/config 按 paper tables。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 defenses 与攻击强度/系统组件；并非所有 defenses 在相同 latency、cost 与 clean-utility operating point 下比较。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/retriever/dataset 已披露；hardware、precision、concurrency、index scale、p95 latency 与 production SLO 不完整。
- **What the Evidence Actually Proves:** RAG security failure 可发生在 corpus→retrieval→generation 不同层，单看 final answer accuracy 会掩盖攻击路径。
- **What It Does Not Prove:** 不证明 taxonomy 穷尽所有攻击，不证明某 defense 普适最优，不证明 benchmark poison rate 对真实 tenant/index 分布有代表性。
- **Limitations / Threats to Validity:** synthetic/constructed attacks、有限 corpora/models、judge reliability、data contamination 与 missing operational controls 限制外推。
- **Trade-offs / New Failure Modes:** provenance/filters/reranking 可减攻击，却增加 false rejection、latency、stale policy、index/version skew 与 availability pressure；过强防御会损害 recall。
- **Where the Previous Design Still Applies:** 单租户、封闭且签名 corpus 可用简单 relevance-first RAG；高风险开放 ingest 需要 provenance、ACL、scan、quarantine、delete/rebuild 与 runtime guards。
- **Evolution Relationship:** `Layering / Dependency`：prompt safety→RAG data-plane threat model→layered ingest/retrieval/generation defense。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `AGENT-RAG`（Ch76）、`PLATFORM-EVALUATION-SYSTEM`（Ch66）与 `PLATFORM-MODEL-REGISTRY`（Ch59）。
- **Target and Adjacent Chapters Read:** 已核对 Ch59、66～73 与 Ch75～77，区分 corpus provenance、index state、generation evidence 与 agent memory。
- **Existing Coverage:** Books 已有 RAG provenance 与 prompt-injection boundary；本 family 增加四类 retrieval-layer threat 的 evidence map。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把 benchmark ranking 写成 production security guarantee。
- **Open Questions:** signed ingestion、tenant isolation、poisoned-chunk deletion、embedding/index rebuild 和 post-incident replay 如何形成统一 contract。

### Trading Inference-Time Compute for Adversarial Robustness

- **Candidate / Week / Score:** Trading Inference-Time Compute for Adversarial Robustness / 2025-W05 / 23/30。
- **Source Family ID:** `defender-attacker-inference-compute-robustness`。
- **Source Type:** 作者论文 / arXiv（Experimental）。
- **First-public Date / Revision History:** v1 2025-01-31；当前 owner/revision identity 已核验。
- **Direct Primary Sources:** https://arxiv.org/html/2501.18841v1；https://arxiv.org/abs/2501.18841。
- **Related Primary Sources:** reasoning models、adversarial attacks 与 safety evaluations 只作 baseline/threat lineage。
- **Access and Verification Status:** Verified；attack construction、defender/attacker scaling、experiments、negative results、discussion 与 limitations 可访问。
- **Full-read Coverage:** 已读 threat settings、attack families、inference-time compute interventions、reasoning-model attacks、cases where scaling fails、evaluation protocol、appendix 和 limitations。
- **Original Problem:** test-time reasoning 改善 benign tasks，但 adversary 也能增加 compute；安全结论若只测固定 attacker/defender budget 会混淆能力与 robustness。
- **Why the Previous Design Was Reasonable:** 固定-budget benchmark 便于可比；单次 greedy/standard sampling 成本可控且攻击面较小。
- **Changed Constraint:** reasoning models 暴露可调 compute budget，defender 与 attacker 都可扩展 search/sampling，robustness 成为双边资源博弈。
- **Mechanism:** 分别改变 defender/attacker inference budget，测量 attack success/robustness 曲线，并设计针对 reasoning process 的攻击以识别 scaling 失效区域。
- **State Ownership:** evaluator 拥有 threat model、budgets、attack success predicate；model/runtime 拥有 token/search state；系统不能让被测模型自报是否安全。
- **Control Flow / Data Flow:** task+threat spec→attacker compute 生成 perturbation→defender model 以给定 budget 推理→external verifier判定→绘制双边 scaling frontier。
- **Implementation Details:** paper 是 evaluation protocol，不公开 production guard/runtime；不同 attacks 的 search state、early stop 与 verifier quality 决定结果。
- **Evaluation Contract:** 多类 adversarial tasks/reasoning models 与 budgets；存在 compute 改善、饱和和反向的不同区域。
- **Baselines / Ablations / Sensitivity / Overhead:** fixed vs scaled inference、不同 attack/defense budget 与 model；不是 hardware-normalized latency/cost benchmark。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** models、budgets/tasks 按论文披露；hardware、precision、batch/concurrency、serving SLO 不完整。
- **What the Evidence Actually Proves:** robustness 必须报告 attacker 与 defender budget；更多 reasoning token 并非单调提高安全性。
- **What It Does Not Prove:** 不证明 compute scaling 是部署 defense，不覆盖所有 adaptive attacks，也不证明某模型在真实 tool/environment 中安全。
- **Limitations / Threats to Validity:** benchmark threat coverage、verifier validity、model snapshots、compute proxy 与 adaptive attack sophistication 限制外推。
- **Trade-offs / New Failure Modes:** defender compute 可提高部分任务鲁棒性，却增加成本/延迟/DoS 面；attacker 也可扩展，且长 reasoning 可能提供新的 injection/manipulation surface。
- **Where the Previous Design Still Applies:** bounded low-risk tasks 可固定 budget；高风险 release gate 应同时 sweep attacker/defender budgets，并结合 deterministic guards/human review。
- **Evolution Relationship:** `Principle Reuse`：test-time scaling 从能力优化扩展为双边 security resource contract，而非单向“思考更久更安全”。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）与 `INFER-SCHEDULING`（Ch56）。
- **Target and Adjacent Chapters Read:** 已核对 Ch56、66～73，确认 compute budget、threat model、verifier 与 deployment gate 分层。
- **Existing Coverage:** Books 已要求 attacker model 与 operating point；本 family 增加双边 compute frontier。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不外推“更多 compute 提高安全”。
- **Open Questions:** 如何用 dollar/latency/energy 统一预算；adaptive multi-turn/tool attacks 与 queue DoS 如何纳入 release gate。

### Scalable-Softmax

- **Candidate / Week / Score:** Scalable-Softmax Is Superior for Attention / 2025-W05 / 22/30。
- **Source Family ID:** `scalable-softmax-length-dependent-attention`。
- **Source Type:** 单作者论文 / arXiv（Experimental）。
- **First-public Date / Revision History:** v1 2025-01-31；无后续 revision。
- **Direct Primary Sources:** https://arxiv.org/html/2501.19399v1；https://arxiv.org/abs/2501.19399。
- **Related Primary Sources:** standard softmax attention、length extrapolation 与 RoPE methods 只作 baseline lineage。
- **Access and Verification Status:** Verified；公式、experiments、analysis、appendix 与 disclosed limitations 可访问。
- **Full-read Coverage:** 已读 length-dependent scaling definition、attention entropy/gradient reasoning、language/vision experiments、train/test length transfer、baseline comparisons、appendix 与 limitations。
- **Original Problem:** softmax normalization 随 candidate count 增长会稀释最大 attention probability，使不同 sequence length 的 attention sharpness 不一致。
- **Why the Previous Design Was Reasonable:** 标准 softmax 简单稳定、硬件/kernel 成熟，在 train/test length 接近时表现可靠。
- **Changed Constraint:** inference context 超过 training length 后，position method 即使可外推，attention normalization 仍可能随 token count 改变。
- **Mechanism:** 根据当前 sequence length 对 attention logits/softmax temperature 进行尺度修正，以维持长序列下的 selectivity。
- **State Ownership:** attention layer 根据 visible key count 计算 scale；position encoding 与 cache manager 不拥有该 normalization policy。
- **Control Flow / Data Flow:** QK logits→length-dependent rescaling→softmax→weighted V；训练与推理必须使用一致或可解释的 length rule。
- **Implementation Details:** 属模型算子改变，需要 kernel/compiler 支持或额外 scale；对 causal prefix 每位置长度不同的实现细节影响效率。
- **Evaluation Contract:** 作者在语言与视觉 tasks、不同 train/test lengths 和 model sizes 上与 standard softmax 等比较。
- **Baselines / Ablations / Sensitivity / Overhead:** 检查 length、scale function 与 tasks；缺广泛大模型、production serving 与独立复现。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** paper 披露实验模型/长度；大规模硬件、precision、batch/concurrency、kernel latency 与 SLO 未完整披露。
- **What the Evidence Actually Proves:** 作者设置显示 normalization policy 本身可影响 length generalization，不能把所有长上下文问题都归于 position encoding。
- **What It Does Not Prove:** 不证明该变体对 frontier LLM 普遍优于标准 softmax，不证明可替代 long-context training、RoPE extension 或 retrieval。
- **Limitations / Threats to Validity:** 单作者、有限规模/tasks、缺独立复现和系统 overhead；scale 与 data/optimizer/architecture 可能交互。
- **Trade-offs / New Failure Modes:** 可能改善长序列 selectivity，却改变训练动态、短序列 calibration、attention entropy 和 kernel compatibility。
- **Where the Previous Design Still Applies:** 固定长度或 train/test matched workload 继续使用标准 softmax；外部 memory/retrieval 适合无需扩大 dense attention 的场景。
- **Evolution Relationship:** `Alternative Branch`：position extrapolation 处理“在哪里”，scalable softmax 处理“多少候选下如何归一化”，两者可叠加而非互相替代。
- **ROADMAP Node:** `MODEL-ATTENTION`（Ch15）主 owner；handoff `MODEL-LONG-CONTEXT`（Ch22）、`TRAIN-PRETRAINING`（Ch28）与 `INFER-TENSORRT-LLM`（Ch49）。
- **Target and Adjacent Chapters Read:** 已核对 Ch14～17、Ch22、28 与 Ch49，确认数学机制、training contract 与 kernel implementation 分层。
- **Existing Coverage:** Books 已覆盖 softmax/long-context；本 family 是 normalization 维度的 experimental branch。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把单篇结果写成普适 superiority。
- **Open Questions:** frontier-scale replication、FlashAttention kernel cost、mixed lengths、KV paging 与 calibration 的交互。

### PixelWorld

- **Candidate / Week / Score:** PixelWorld / 2025-W05 / 22/30。
- **Source Family ID:** `pixelworld-rendered-text-unified-input`。
- **Source Type:** 作者论文 / arXiv（Experimental）。
- **First-public Date / Revision History:** v1 2025-01-31；v2/v3 2025-05-21/10-21；owner 以 v1 归 W05。
- **Direct Primary Sources:** https://arxiv.org/html/2501.19339v1；https://arxiv.org/abs/2501.19339。
- **Related Primary Sources:** pixel-based language models、vision encoders 与 OCR/multimodal baselines 只作 lineage。
- **Access and Verification Status:** Verified；method、data rendering、training、multi-task evaluation、latency analysis、appendix 与 limitations 可访问。
- **Full-read Coverage:** 已读 text-to-image rendering、vision encoder/LLM coupling、pretraining/finetuning tasks、text/multimodal comparisons、reasoning/coding failures、token/latency trade-off 与 limitations。
- **Original Problem:** tokenizer/Unicode/layout 分裂文本与视觉输入；统一 pixel interface 可减少 modality-specific parser/tokenizer 假设。
- **Why the Previous Design Was Reasonable:** discrete text tokens 高压缩、便于 exact copy/code 与成熟 KV/runtime；vision tokens 为高维连续输入提供专用 inductive bias。
- **Changed Constraint:** multilingual typography、documents、tables与GUI把文字内容、layout和视觉语义混在同一 surface，单纯 text tokenizer 丢失呈现信息。
- **Mechanism:** 把文本渲染为像素，通过 vision encoder 投影到 LLM token space，与图像共享输入 pipeline，再在多任务数据上训练。
- **State Ownership:** renderer 拥有 font/layout/locale contract；vision encoder 生成 patch tokens；LLM 只消费 projected sequence，不能恢复未保留的 rendering metadata。
- **Control Flow / Data Flow:** raw text/document→deterministic rendering→patching/vision encoding→projector→LLM→task output。
- **Implementation Details:** pixel sequence 往往比 text tokens 长；font、resolution、patch size 与 rendering errors 成为数据/runtime contract。
- **Evaluation Contract:** text understanding、classification、multimodal tasks、reasoning/coding 等；比较 token-based 与 pixel-based variants。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 encoder/model sizes、tasks 与 representations；作者报告 pixel input latency 可达 token route 数倍，但不是统一 production SLO。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** paper 披露模型与 task；硬件、precision、batch/concurrency 与完整端到端 SLO 不统一。
- **What the Evidence Actually Proves:** unified pixel interface 在部分 multilingual/multimodal tasks 可工作，并显式暴露 representation compression 与 universality trade-off。
- **What It Does Not Prove:** 不证明 tokenizer 可被普遍淘汰；reasoning/coding 尤其小模型可能下降，像素接口也不自动获得 provenance 或 OCR correctness。
- **Limitations / Threats to Validity:** rendering domain shift、视觉 token 膨胀、字体/分辨率敏感、有限模型规模与 task coverage。
- **Trade-offs / New Failure Modes:** 统一 modality boundary，却增加 token length、latency、visual ambiguity、exact-copy failure 和 renderer version dependency。
- **Where the Previous Design Still Applies:** text/code/API 输入继续使用 discrete tokens；layout-rich document/GUI 与低资源 script 可选择 pixel branch 或 hybrid route。
- **Evolution Relationship:** `Alternative Branch`：tokenized text 与 rendered-pixel input 是按 workload 选择的 representation branch，不是线性替代。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `MODEL-TOKENIZER`（Ch11）、`INFER-REQUEST-LIFECYCLE`（Ch42）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已核对 Ch11、Ch23～24、Ch42～45 与 Ch66，确认 representation identity 与 serving cost 分层。
- **Existing Coverage:** Books 已有 modality-specific/shared token space；本 family 提供极端统一化分支及其 latency/accuracy 边界。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把作者 case 写成“everything should be pixels”。
- **Open Questions:** hybrid router、renderer provenance、accessibility、exact copy/code 与 multimodal batching 如何共同设计。

### SAeUron

- **Candidate / Week / Score:** SAeUron / 2025-W05 / 22/30。
- **Source Family ID:** `saeuron-sae-diffusion-unlearning`。
- **Source Type:** 作者论文 + official repository/artifacts（Experimental）。
- **First-public Date / Revision History:** v1 2025-01-29；v2 2025-01-31；v3 2025-05-21；owner 以 v1 归 W05。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.18052；https://arxiv.org/pdf/2501.18052v1；https://github.com/cywinski/SAeUron。
- **Related Primary Sources:** UnlearnCanvas、I2P、SAE 与 diffusion unlearning baselines 只定义实验 contract。
- **Access and Verification Status:** Verified via same-ID PDF + repository；experimental HTML 曾错配无关内容，异常保留而未据其推断。
- **Full-read Coverage:** 已读 SAE training across denoising timesteps、feature scoring/intervention、multi-concept unlearning、concept/style/nudity evaluations、adversarial attacks、utility preservation、ablation、appendix 与 limitations。
- **Original Problem:** fine-tune/erase diffusion weights 成本高且难解释；概念在不同 timestep/activation 中分布，单点编辑可能损害 unrelated generation。
- **Why the Previous Design Was Reasonable:** weight fine-tuning/negative guidance 直接、无需单独 representation model；封闭概念和离线模型可接受重新训练。
- **Changed Constraint:** 需要可审计、可组合、低成本地移除多个概念，并在 adversarial prompts 下保持效果。
- **Mechanism:** 在 diffusion activations 上训练 SAE，识别与目标概念相关 sparse features；生成时跨 denoising timesteps 抑制/调整这些 features，而非重训基础模型。
- **State Ownership:** base diffusion weights 保持不变；SAE dictionary、concept-feature mapping 与 intervention strength 由 unlearning policy artifact 拥有。
- **Control Flow / Data Flow:** prompt→diffusion denoising activations→SAE encode→target feature intervention→decode/continue denoising→image evaluation。
- **Implementation Details:** 一个 SAE 可承载多概念，但 mapping/threshold 与 base model/timestep 强耦合；artifact version mismatch 会导致无效或过度干预。
- **Evaluation Contract:** UnlearnCanvas concepts/styles、I2P nudity、utility/fidelity metrics 与 adversarial prompts；作者比较多种 unlearning methods。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 weight-based/guidance baselines、feature choices、timesteps、多概念与 attacks；production latency/VRAM 与 independent replication 不完整。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** diffusion model/datasets 按论文披露；hardware、precision、batch/concurrency、online latency/SLO 不完整。
- **What the Evidence Actually Proves:** 作者设置下，SAE feature intervention 可作为可解释的 inference-time unlearning branch，并对若干 adversarial prompts 保持效果。
- **What It Does Not Prove:** 不证明概念被从模型知识中删除，不保证跨 base/revision 转移，也不证明 SAE feature 具有唯一因果语义或覆盖所有攻击。
- **Limitations / Threats to Validity:** feature entanglement、benchmark/attack coverage、自动 metric、artifact coupling 与 HTML mismatch；作者实验不是 production removal guarantee。
- **Trade-offs / New Failure Modes:** 避免重训、支持复用，却新增 SAE training/storage、feature-selection error、collateral suppression、version skew 与 bypass attack。
- **Where the Previous Design Still Applies:** 需要强删除/法规证明时 weight/data-level retraining 仍可能必要；低风险 personalization 可用 prompt/negative guidance。
- **Evolution Relationship:** `Alternative Branch`：data/weight unlearning 改模型本体；SAE intervention 在 runtime 加可解释 policy layer。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）、`PLATFORM-MODEL-REGISTRY`（Ch59）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已核对 Ch24、59、66～73，确认生成机制、policy artifact、evidence 与 security owner。
- **Existing Coverage:** Books 已区分 guard、weight edit 与 artifact policy；本 family 提供 SAE runtime intervention 的实验分支。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把 benchmark success 表述成法规或普适删除证明。
- **Open Questions:** feature provenance、base-model upgrade migration、multi-policy conflict、rollback、adaptive red team 与 measurable removal definition。

### MM-IQ

- **Candidate / Week / Score:** MM-IQ / 2025-W05 / 21/30。
- **Source Family ID:** `mm-iq-visual-abstraction-benchmark`。
- **Source Type:** 作者 benchmark paper / arXiv（Experimental）。
- **First-public Date / Revision History:** v1 2025-02-02；后续 revision 归同一 family。
- **Direct Primary Sources:** https://arxiv.org/html/2502.00698v1；https://arxiv.org/abs/2502.00698。
- **Related Primary Sources:** AVR/IQ benchmarks 与被测 model cards 只定义 lineage/identity；不把厂商主张并入证据。
- **Access and Verification Status:** Verified；construction、quality control、tasks、evaluation、failure analysis、RL pilot、appendix 与 limitations 可访问。
- **Full-read Coverage:** 已读 2,710-test/4,776-train construction、8 reasoning paradigms、model prompts/parameters、human comparison、error taxonomy、RL pilot、examples、appendix 与 limitations。
- **Original Problem:** broad multimodal benchmarks 混合 knowledge、language、OCR 与 reasoning，难定位 abstract visual reasoning failure。
- **Why the Previous Design Was Reasonable:** broad benchmark 更贴近 general product tasks；multiple-choice 便于低成本、可复算比较。
- **Changed Constraint:** 需要减少领域知识/语言混杂，区分 perception error、rule discovery 与 reasoning process。
- **Mechanism:** 汇集并质检 visual IQ-style problems，按八类 paradigm 分组；以统一 multiple-choice contract 测模型并人工分析错误。
- **State Ownership:** dataset/version owner 管题目、label、split 与 license；runner 管 prompt/generation params；evaluator 管 answer extraction，模型解释不是 ground truth。
- **Control Flow / Data Flow:** item/image→model prompt→response→answer extraction/score→paradigm/error aggregation；training set 可另用于 RL，但不能污染 test。
- **Implementation Details:** 被测模型 generation 参数不同；部分 error analysis 人工完成；完整 contamination audit 与 executable artifact reproducibility 不充分。
- **Evaluation Contract:** 2,710 test items、8 paradigms、四选一 random baseline；多 open/proprietary LMM 与 human comparison；appendix列 generation settings。
- **Baselines / Ablations / Sensitivity / Overhead:** model-to-model与 reasoning/non-reasoning比较、人工 failure analysis、有限 RL pilot；没有系统性 prompt/evaluator/contamination sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model snapshots/output limits 披露；API hardware/precision、batch/concurrency 与 serving SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在该题库/runner下，多数模型接近 chance，错误同时来自视觉理解与抽象规则；benchmark 可诊断而非证明“人类式智能”。
- **What It Does Not Prove:** 不证明 general intelligence、world-model 或 embodied ability；人类 51.27% 与模型分数受样本/接口影响，不能跨版本直接比较。
- **Limitations / Threats to Validity:** 资源限制使 RL baseline 很弱；题源/license/contamination、answer extraction、multiple-choice shortcut 与不同 API settings 限制外推。
- **Trade-offs / New Failure Modes:** taxonomy 提升诊断性，却牺牲开放式/interactive realism；公开 train set 增加 benchmark overfitting 与 test leakage 风险。
- **Where the Previous Design Still Applies:** MMMU/Video-MMMU 等 broad tasks 仍衡量应用能力；interactive/executable evaluation 才能覆盖 tool/environment outcome。
- **Evolution Relationship:** `Layering / Dependency`：broad capability benchmark→abstraction-focused diagnostic→interactive/executable evidence，三层互补。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `MULTIMODAL-WORLD-MODELS`（Ch25）。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～26 与 Ch65～68，确认 perception、reasoning、world state 与 evidence boundary。
- **Existing Coverage:** Books 已区分 score、capability 与 deployment claim；本 family 提供 paradigm/error decomposition 案例。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不保留脱离 model snapshot/runner 的 headline ranking。
- **Open Questions:** contamination-resistant private split、prompt normalization、open-response verifier 与 temporal/interactive abstraction evaluation 如何建立。

### Rethinking Mixture-of-Agents

- **Candidate / Week / Score:** Rethinking Mixture-of-Agents / 2025-W05 / 24/30。
- **Source Family ID:** `self-moa-quality-diversity-test-time-ensemble`。
- **Source Type:** 作者论文 / arXiv v1（Experimental）。
- **First-public Date / Revision History:** v1 2025-02-02；owner 按 v1 归 W05，后续推荐日期不形成新事件。
- **Direct Primary Sources:** https://arxiv.org/html/2502.00674v1；https://arxiv.org/abs/2502.00674。
- **Related Primary Sources:** 原 MoA 论文和所用 model/benchmark 文档只定义 lineage 与 evaluation contract。
- **Access and Verification Status:** Verified；正文、统计分析、scaling experiment 与 appendices 可访问。
- **Full-read Coverage:** 已读 Introduction、Related Work、Self-/Mixed-MoA 设置、quality-diversity 分析、200+ experiments、Self-MoA-Seq、MT-Bench/USC 补充结果、normalization 与 conclusion。
- **Original Problem:** 多模型 ensemble 把“模型身份多样性”当作收益来源，却可能将低质量 proposer 带入聚合，混淆 diversity 与 average quality 的贡献。
- **Why the Previous Design Was Reasonable:** 不同模型具有互补数据、architecture 与 specialization；未知任务上并行询问多个模型可降低单模型盲点，且 aggregator 能综合候选。
- **Changed Constraint:** test-time compute 可以通过同模型 repeated sampling 获得 in-model diversity；当 proposer 质量差异大时，跨模型 diversity 的边际收益可能低于质量损失。
- **Mechanism:** Self-MoA 从一个最强 proposer 重复采样并由 aggregator 综合；Self-MoA-Seq 用固定窗口迭代合并当前 synthesis 与新样本，绕开 aggregator context 上限。
- **State Ownership:** proposer policy 拥有 sample distribution；orchestrator 拥有 sample count、model identity 与 window；aggregator 拥有 synthesis，不应把其回答当作可验证 ground truth。
- **Control Flow / Data Flow:** query→并行或重复 proposer sampling→candidate set→aggregator synthesis；Seq 版本把 synthesis 作为下一窗口状态，直至预算或停止条件触发。
- **Implementation Details:** 同模型样本依赖 temperature/seed；Mixed-MoA 还需 routing/model availability；Seq 版本压缩上下文但引入顺序依赖和 early-synthesis lock-in。
- **Evaluation Contract:** AlpacaEval 2.0、MT-Bench、MMLU-redux、CRUX、MATH；六 proposer 或 task-specific models，固定 aggregator/temperature，并以多组组合分析 quality-diversity。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 individual、Mixed-MoA、Self-MoA、TaskBest、USC 与 sample 6→30；多样性用 Vendi Score，统计回归显示质量相关更强，但没有真实服务成本/SLO 对齐。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型、sample 数、temperature 与部分 context constraint 披露；hardware、precision、并发、端到端 latency/cost 与 production SLO 为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者模型/任务/aggregator 设置中，强单模型 repeated sampling 是必须比较的 baseline；cross-model diversity 的收益受 proposer quality 与 task specialization 约束。
- **What It Does Not Prove:** 不证明单模型 ensemble 普遍优于 multi-agent/multi-model；也不证明 benchmark synthesis 等价于工具协作、共享状态或执行结果正确性。
- **Limitations / Threats to Validity:** LLM-as-judge、有限模型年代、任务与 prompt、事先知道 TaskBest、sample correlation、缺真实 cost/failure study；少数近等质 specialized mixture 仍略胜 Self-MoA。
- **Trade-offs / New Failure Modes:** 降低 model-routing complexity，却增加同源 correlated error、采样成本与 aggregator bottleneck；Seq 增加 order sensitivity、state drift 和不可逆摘要损失。
- **Where the Previous Design Still Applies:** 任务类型未知、模型能力互补、工具/数据权限不同或需要独立 failure domains 时，Mixed-MoA / bounded multi-agent 仍合理。
- **Evolution Relationship:** `Alternative Branch`：cross-model diversity 与 in-model repeated sampling 是 quality/diversity/cost contract 下的两条分支，而非线性替代。
- **ROADMAP Node:** `AGENT-MULTI-AGENT`（Ch82）主 owner；handoff `MODEL-SAMPLING`（Ch20）、`INFER-SCHEDULING`（Ch56）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已核对 Ch20、Ch56、Ch66、Ch81～84，确认 ensemble policy、capacity、evidence 与 multi-agent runtime 分层。
- **Existing Coverage:** Books 已有 single-agent headroom、communication tax 与 error amplification；本 family 提供 quality-diversity 分解及 repeated-sampling baseline。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把作者 benchmark 写成“多 Agent 无价值”。
- **Open Questions:** 如何在 token/GPU cost、tail latency、correlated failure、task routing 与 executable verifier 下比较 Self-/Mixed-MoA。

### Federated Sketching LoRA

- **Candidate / Week / Score:** Federated Sketching LoRA / 2025-W05 / 24/30。
- **Source Family ID:** `fslora-heterogeneous-federated-submatrix-update`。
- **Source Type:** 作者论文 / arXiv v1（Experimental）。
- **First-public Date / Revision History:** v1 2025-01-31；后续 v2～v4 归同一 family，历史结论锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2501.19389v1；https://arxiv.org/abs/2501.19389。
- **Related Primary Sources:** LoRA、federated LoRA、HeteroLoRA、FedStackLoRA 与 compression baselines 只定义比较分支。
- **Access and Verification Status:** Verified；公式、算法、收敛分析、实验、ablation 与 proof appendices 可访问。
- **Full-read Coverage:** 已读 problem formulation、random-k diagonal sketch、gradient sparsity、server/device algorithm、compression comparison、smoothness/variance/heterogeneity assumptions、convergence theorem、RoBERTa/LLaMA experiments、communication budget、ablation 与 proofs。
- **Original Problem:** federated LoRA 的客户端资源异构使统一 rank 浪费强设备或排除弱设备；每端不同 rank 又难以无损聚合成一致 global adapter。
- **Why the Previous Design Was Reasonable:** 固定 rank 让参数 shape、optimizer state 与 aggregation 简单；同构集群或小规模受控设备中容易复现与维护。
- **Changed Constraint:** on-device clients 的 compute、memory、uplink 与 participation 差异显著，统一 local LoRA capacity 不再可行。
- **Mechanism:** server 保持完整 global LoRA A/B；每轮为设备采样 random-k diagonal sketch，仅下发/更新相应 rows/columns；稀疏 local gradients 回传后聚合到 global modules。
- **State Ownership:** server 拥有 canonical adapter、round 与 aggregation state；client 只拥有本轮 sketch/submatrix、local optimizer/data；sketch distribution 决定长期 coverage。
- **Control Flow / Data Flow:** server 选择 clients/sketches→下发 global submatrix→local SGD→上传 sparse updates→server 按索引聚合→进入下一轮。
- **Implementation Details:** sketch ratio `k_i/r` 显式映射设备资源；结构稀疏减少 local compute/memory/communication，但需要索引一致性、稀疏更新和全局覆盖管理。
- **Evaluation Contract:** RoBERTa on GLUE 与 LLaMA-3.2-3B on Commonsense170K，多设备 non-IID data、不同 ranks/sketch ratios、固定 upload budgets；比较 vanilla federated LoRA、HeteroLoRA、FedStackLoRA 等。
- **Baselines / Ablations / Sensitivity / Overhead:** 检查有/无 sketch、global rank、sketch ratio、更多 devices 与 top-k compression 组合；理论收益依赖 bounded variance、smoothness 和 gradient dissimilarity 假设。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/dataset/local hyperparameters 与通信预算披露；真实手机硬件、断连、secure aggregation、precision、网络 tail 与 wall-clock SLO 不完整。
- **What the Evidence Actually Proves:** 在作者模拟的异构 federated setting 中，submatrix sketching 可把资源差异编码为 update sparsity，并呈现 convergence/communication/accuracy trade-off。
- **What It Does Not Prove:** 不证明真实 cross-device deployment、privacy、Byzantine robustness 或任意 non-IID/participation pattern 下稳定；理论假设不等同生产保证。
- **Limitations / Threats to Validity:** 小规模设备模拟、有限模型/任务、客户端可用性与网络故障未建模、server canonical state 单点、无 DP/secure aggregation 威胁模型。
- **Trade-offs / New Failure Modes:** 扩大设备参与和降低带宽，却引入 sketch coverage starvation、stale submatrices、index/version mismatch、公平性与收敛速度差异。
- **Where the Previous Design Still Applies:** 同构高带宽集群、中心化训练或只需少量稳定客户端时，固定-rank LoRA / standard FedAvg 更简单、可预测。
- **Evolution Relationship:** `Direct Evolution`：uniform-rank federated LoRA→heterogeneous local rank→server-owned global adapter + sampled submatrix updates。
- **ROADMAP Node:** `TRAIN-LORA`（Ch30）主 owner；handoff `TRAIN-DISTRIBUTED-TRAINING`（Ch36）、`PLATFORM-SECURITY`（Ch72）与 `PLATFORM-MULTI-TENANT`（Ch71）。
- **Target and Adjacent Chapters Read:** 已核对 Ch29～31、Ch35～41 与 Ch71～72，确认 adapter lifecycle、distributed state 与 privacy/security 未被混同。
- **Existing Coverage:** Books 已有 LoRA rank/adapter 与分布式聚合基础；本 family 提供 resource-aware submatrix ownership 分支。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把模拟通信预算外推为真实端侧吞吐。
- **Open Questions:** dropout/rejoin、optimizer state、secure aggregation、DP accounting、client fairness 与 sketch coverage 如何联合设计。

### Activation Approximation Safety

- **Candidate / Week / Score:** Activation Approximation Safety / 2025-W05 / 26/30。
- **Source Family ID:** `activation-approximation-safety-quad-a`。
- **Source Type:** 作者安全研究 / arXiv v1（Experimental）。
- **First-public Date / Revision History:** v1 2025-02-02；v2 2025-06-10，owner 与历史实验边界锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.00840v1；https://arxiv.org/abs/2502.00840。
- **Related Primary Sources:** polynomialization、sparsification、activation quantization 与 DPO/jailbreak baselines 只定义被测变换和 threat model。
- **Access and Verification Status:** Verified；threat model、10-model assessment、three approximation families、defense、ablation、limitations 与 attack appendices 可访问。
- **Full-read Coverage:** 已读 Background、threat model、evaluation setup、approximation-error analysis、layer sensitivity、activation clustering、QuadA、adaptive attacks、ablation、limitations、prompt templates 与 conclusion。
- **Original Problem:** deployment optimization 通常以 perplexity/utility 近似不变为安全代理，却未验证 activation error 是否破坏已对齐模型的 refusal boundary。
- **Why the Previous Design Was Reasonable:** polynomial/sparse/quantized activation 可降低 private inference 或资源受限推理成本；若任务 loss 与 PPL 基本稳定，工程上容易假设行为语义被保留。
- **Changed Constraint:** safety behavior 可能依赖比通用 utility 更脆弱的 early-layer activation geometry，微小近似误差可先破坏拒答而不显著损害可读性。
- **Mechanism:** 论文测量多种 approximation error，定位 safety-sensitive early layers 与 harmful activation shift；QuadA 在 safety alignment 时向敏感层注入基于 maximum viable approximation 的扰动，使 policy 对部署误差更鲁棒。
- **State Ownership:** deployment plan 拥有 approximation method/level；model artifact 拥有 alignment weights；release evidence 必须绑定二者组合，不能把 base model safety card复用于任意 execution plan。
- **Control Flow / Data Flow:** aligned model + approximation plan→layer activation perturbation→harmful/benign prompts→ASR/PPL；defense 分支先估计 viable error/sensitive layers→带扰动 DPO→重新评测。
- **Implementation Details:** 测试 polynomialization、TEAL-style sparsity、SmoothQuant/OmniQuant-style activation quantization；QuadA 只在选择层注入扰动，避免全层 noise 损害 utility。
- **Evaluation Contract:** 10 个 aligned LLM、7 类/实例化 approximation techniques、ASR/PPL/utility、安全 prompts 与 GCG/AutoDAN/DRA 等 adaptive attacks；作者比较 DPO 与 QuadA。
- **Baselines / Ablations / Sensitivity / Overhead:** 原模型、不同 approximation levels、DPO、扰动幅度、sensitive/non-sensitive/all-layer ablation；未给完整端到端 private-inference latency/cost 或独立复现。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/approximation setting 与 safety metrics 披露；hardware、kernel、sequence length、batch/concurrency、latency/SLO 和私有推理协议完整成本为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 作者设置中，utility-preserving activation approximations 可能显著提高 jailbreak ASR；deployment execution plan 是安全证据的一部分，而不是透明优化层。
- **What It Does Not Prove:** 不证明所有量化/稀疏化必然不安全，不证明 QuadA 对未知攻击、模型版本或更强 approximation 普遍有效，也不等同独立红队验证。
- **Limitations / Threats to Validity:** authors' attack/evaluator set、部分 approximation 为模拟、真实协议与 kernel 差异、ASR judge误差、模型年代有限；trainer需能访问模型并重新对齐。
- **Trade-offs / New Failure Modes:** 近似提升效率/隐私可计算性，却新增 safety regression；robust alignment 增加训练与版本矩阵，错误估计 viable error 或 layer set 会造成漏防或 utility 损失。
- **Where the Previous Design Still Applies:** 受控低误差、完整组合评测和低风险 workload 可继续使用 approximation；无法重训时需要更保守 execution plan、外部 guard 与 release gate。
- **Evolution Relationship:** `Layering / Dependency`：model alignment→execution-plan approximation→组合安全评测→approximation-aware alignment；后层不能继承前层证据。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `INFER-TENSORRT-LLM`（Ch49）、`PLATFORM-EVALUATION-SYSTEM`（Ch66）与 `PLATFORM-PRODUCTION`（Ch73）。
- **Target and Adjacent Chapters Read:** 已核对 Ch48～50、Ch66～73，确认 execution plan、evidence、security 与 release gate 的 owner。
- **Existing Coverage:** Books 已有 quantization/compile 与 safety release boundary；本 family补足“优化组合必须重新认证”的因果案例。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不保留脱离 approximation/model/attack contract 的 headline ASR。
- **Open Questions:** 如何把 model×kernel×precision×protocol×policy 的组合测试压缩成可维护 certification matrix，并监测线上 drift。

### Concept Steerers

- **Candidate / Week / Score:** Concept Steerers / 2025-W05 / 20/30。
- **Source Family ID:** `concept-steerers-ksae-diffusion-control`。
- **Source Type:** 作者论文 + official code repository（Experimental）。
- **First-public Date / Revision History:** v1 2025-01-31；后续 v2/v3 归同一 family，历史结论锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2501.19066v1；https://arxiv.org/abs/2501.19066；https://github.com/kim-dahye/steerers。
- **Related Primary Sources:** concept erasure、negative guidance、LoRA 与 adversarial-prompt baselines 只定义比较范围。
- **Access and Verification Status:** Verified；method、four experiment groups、efficiency、ablation、implementation appendix 与 repository 可访问。
- **Full-read Coverage:** 已读 text encoder/k-SAE formulation、concept-vector extraction、positive/negative steering、I2P/COCO/violence/style/object experiments、四类 adversarial prompts、runtime、capacity/strength ablations、future work 与 implementation details。
- **Original Problem:** 每概念 fine-tune/LoRA/weight erasure 成本高、版本耦合强；step-wise reward/guidance 又增加 generation latency，且概念控制难解释。
- **Why the Previous Design Was Reasonable:** weight-level editing 可持久改变模型，negative prompt/guidance 无需额外 representation model；少量固定 policy 时实现简单。
- **Changed Constraint:** 平台需要对多个动态概念快速启停、审计与组合，同时尽量保持基础生成质量并应对 adversarial prompts。
- **Mechanism:** 在 text-encoder embeddings 上训练 k-sparse autoencoder，识别与目标概念相关 latent direction；推理时在 text representation 上正/负 steering，再进入不变的 diffusion denoising。
- **State Ownership:** base generator 保持不变；k-SAE dictionary、concept direction 与 steering strength 是独立 policy artifact，必须绑定 text encoder/base model/version。
- **Control Flow / Data Flow:** prompt→text encoder embedding→k-SAE encode/feature selection→directional intervention→diffusion generator→image safety/quality evaluation。
- **Implementation Details:** 一个 k-SAE 可承载多个概念，不需每概念 LoRA；作用点在 text embedding 而非每个 denoising step，降低在线额外计算，但依赖 concept labeling 与 latent disentanglement。
- **Evaluation Contract:** SD1.4/SDXL-Turbo/FLUX 等生成器、I2P/COCO、nudity/violence/style/object属性、Ring-A-Bell/MMA-Diffusion/P4D/UnLearnDiffAtk；使用 ASR/FID/CLIP 等指标。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 ESD/UCE/RECE/SLD/SAFREE/TraSCE 等，测试 k-SAE capacity、negative steering、direction choice 与 steering strength；约 5× 为作者特定设置，不是平台 SLO。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/dataset/steering settings 披露；hardware、precision、batch/concurrency、端到端 latency 与 production SLO 不完整。
- **What the Evidence Actually Proves:** 作者设置中，text-embedding sparse-feature intervention 是无需重训 base model 的可控生成分支，并在已测攻击/指标上保持较好安全-质量折中。
- **What It Does Not Prove:** 不证明 feature 是唯一因果概念、不保证跨模型/version/语言迁移，也不等于概念从模型中删除或所有攻击被覆盖。
- **Limitations / Threats to Validity:** 自动 safety classifier、有限攻击与概念、text-only steering、repository/revision coupling、未验证 region-level/local control 与生产延迟。
- **Trade-offs / New Failure Modes:** policy 切换快且可解释性更强，却新增 dictionary drift、feature entanglement、over-suppression、strength conflict、artifact mismatch 与 adaptive bypass。
- **Where the Previous Design Still Applies:** 法规要求持久删除或高风险 policy 时仍需 data/weight-level remediation；开放式创作和低风险场景可用 prompt/guidance。
- **Evolution Relationship:** `Alternative Branch`：weight edit、denoising guidance 与 representation steering 在 persistence、cost、auditability 和 bypass risk 上分叉。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）、`PLATFORM-MODEL-REGISTRY`（Ch59）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已核对 Ch24、Ch59、Ch66～73，确认生成机制、policy artifact 和 safety evidence 分层。
- **Existing Coverage:** Books 已有 runtime guard、weight edit 与 SAE intervention；本 family补充 text-embedding k-SAE policy branch。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不将作者 ASR/速度数字外推到其他生成器或 policy。
- **Open Questions:** 多语言/多概念组合、region steering、policy conflict、base upgrade migration 与持续 red-team 如何闭环。

### RAG Interrogation Attack

- **Candidate / Week / Score:** RAG Interrogation Attack / 2025-W05 / 26/30。
- **Source Family ID:** `rag-black-box-document-membership-interrogation`。
- **Source Type:** 作者 security paper / arXiv v1（Experimental）。
- **First-public Date / Revision History:** v1 2025-02-01；v2 2025-06-30 为同 family revision，owner 锁定 W05。
- **Direct Primary Sources:** https://arxiv.org/html/2502.00306v1；https://arxiv.org/abs/2502.00306。
- **Related Primary Sources:** prior RAG-MIA/data-extraction attacks、LakeraGuard 与被测 retriever/generator 文档只定义 baselines/threat model。
- **Access and Verification Status:** Verified；全文、threat model、experiments、ablations、failure cases、countermeasures、prompts 与 ROC appendices 可访问。
- **Full-read Coverage:** 已读 RAG/data-membership background、black-box adversary、prior-attack detectability、three-stage IA、query generation/answering/aggregation、datasets/model combinations、n/k ablation、failure/cost/countermeasure 与 appendices。
- **Original Problem:** RAG 避免把私有文档写入模型参数，却在每次检索后把命中文档放进 prompt；传统 privacy argument 没覆盖 datastore membership 可由黑盒输出推断。
- **Why the Previous Design Was Reasonable:** non-parametric knowledge 便于更新、删除和权限控制；query rewrite 与 prompt-injection detector 可拦截显式 context extraction。
- **Changed Constraint:** 攻击者不需越狱或索取原文，只需生成自然且只能由目标文档回答的问题，并聚合回答正确性，就能绕过“异常 prompt”检测。
- **Mechanism:** auxiliary LLM 为目标文档生成约 30 个 specific yes/no queries 和 ground-truth answers；对 victim RAG 黑盒提问，按 answer correctness 聚合 membership score。
- **State Ownership:** datastore/index 拥有 membership；retriever 决定 top-k exposure；generator把 retrieved evidence 转为 observable output；gateway只能看到自然 queries，无法单靠 prompt shape判定攻击。
- **Control Flow / Data Flow:** target document→auxiliary query/answer generation→victim query rewrite/retrieval→generator answer→correctness classifier→multi-query membership inference。
- **Implementation Details:** 不需 retriever/generator/hyperparameter knowledge，但假设攻击者有同分布 non-members 作 threshold calibration，且目标文档足够长、具体、能生成区分性问题。
- **Evaluation Contract:** 多 datasets、retrievers/generators、query rewriting 与 detectors；比较 prior MI/extraction attacks，以 ROC/AUC、TPR@low-FPR、detector rate、question count、retrieval k 和 financial cost评估。
- **Baselines / Ablations / Sensitivity / Overhead:** 扫 n queries 与 top-k；prior attacks 在 detector 下退化，IA 在作者设置中保持 stealth；k 增大因上下文干扰降低攻击，但并未消失。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** retriever/generator/dataset/query count/top-k 披露；provider hardware/precision、batch/concurrency、index规模与生产 SLO 不完整。
- **What the Evidence Actually Proves:** 在明确 black-box threat model 下，RAG datastore membership 可以通过自然查询的统计输出被推断；query rewriting/prompt-injection detection 不是充分隐私边界。
- **What It Does Not Prove:** 不证明所有短/通用文档、所有 RAG pipeline 或生产 guard 都同样脆弱，也不等于直接抽取文档内容。
- **Limitations / Threats to Validity:** 目标需足够长且specific、需要 target document 与同分布 non-members、LLM可能凭参数知识回答、有限 detector/model/index配置、作者实验缺独立复现。
- **Trade-offs / New Failure Modes:** 减少可观察 answer specificity可防 leakage，却降低 RAG utility；加入噪声/拒答/访问节流会损害可用性并可能仍被多查询平均消除。
- **Where the Previous Design Still Applies:** 公开知识库、低敏感语料或有强身份/ACL/query-budget 的封闭系统可继续标准 RAG；高敏感库需 per-document policy、telemetry 和 privacy testing。
- **Evolution Relationship:** `Direct Evolution`：parameter leakage threat model→retrieved-context leakage→natural-query membership inference→utility-aware privacy controls。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `AGENT-RAG`（Ch76）、`PLATFORM-MONITORING`（Ch67）与 `PLATFORM-GATEWAY`（Ch62）。
- **Target and Adjacent Chapters Read:** 已核对 Ch62、Ch66～73 与 Ch75～77，确认 retrieval state、access policy、telemetry 与 privacy evaluation 分层。
- **Existing Coverage:** Books 已有 RAG poisoning/prompt injection；本 family 补足 datastore membership privacy threat。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不把作者 30 queries/成本数字外推到其他 provider 或 index。
- **Open Questions:** per-document ACL、answer indistinguishability、rate limits、private retrieval、deletion evidence 与 legitimate repeated research query 如何平衡。

### HackerRank-ASTRA

- **Candidate / Week / Score:** HackerRank-ASTRA / 2025-W05 / 21/30。
- **Source Family ID:** `hackerrank-astra-multifile-consistency-evaluation`。
- **Source Type:** 作者 benchmark paper + released dataset（Experimental）。
- **First-public Date / Revision History:** v1 2025-01-31；无后续 arXiv revision，owner 归 W05。
- **Direct Primary Sources:** https://arxiv.org/html/2502.00226v1；https://arxiv.org/abs/2502.00226；https://huggingface.co/datasets/hackerrank/astra-benchmark。
- **Related Primary Sources:** SWE-bench、DevEval 与被测 model/version docs 只定义 lineage/comparison。
- **Access and Verification Status:** Verified；method、65 tasks、32-run consistency、taxonomy、format/failure analysis、limitations 与 dataset可访问。
- **Full-read Coverage:** 已读 benchmark design、problem taxonomy、prompt/output contract、scoring、models/settings、32 independent runs、mean/pass@1/median-SD、skill analysis、format effects、common errors、length correlation、related work、limitations 与 dataset。
- **Original Problem:** 单文件 pass@k 难以代表真实项目修改，也掩盖同一模型多次运行的不稳定；一次成功不能说明可依赖性。
- **Why the Previous Design Was Reasonable:** standalone coding题容易执行、评分与防污染；对模型算法能力比较成本低，适合早期迭代。
- **Changed Constraint:** production coding需要跨文件、framework contract、format escaping 与重复可用性，模型输出 stochasticity 成为系统风险。
- **Mechanism:** 构造 65 个 multi-file project tasks 与 main/subskill taxonomy；每模型每题运行 32 次，结合 test score、mean pass@1 与 per-question score standard deviation衡量 correctness和consistency。
- **State Ownership:** dataset/version owner 拥有 tasks/tests/taxonomy；runner 拥有 prompt、temperature与output parser；model provider 拥有 opaque snapshot，结果不能跨版本继承。
- **Control Flow / Data Flow:** task files/spec→model generation→XML/JSON multi-file parsing→tests/subskill scoring→32-run aggregation→correctness/variance报告。
- **Implementation Details:** 被测模型默认 temperature/context各异；XML/JSON format本身影响结果；guardrail refusal、escaping错误与代码逻辑错误分别记录。
- **Evaluation Contract:** 65 projects、主要偏 frontend/React/Angular，5 model snapshots，32 runs per task；报告 mean score、pass@1、median SD、paired tests与skill breakdown。
- **Baselines / Ablations / Sensitivity / Overhead:** 跨模型、XML/JSON、input/output length与skills比较；没有 agentic iterative feedback、tool execution loop或广泛 backend/language coverage。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** API model snapshots、context limits、default temperature、run count披露；provider hardware/precision/batch/concurrency/cost/SLO未披露。
- **What the Evidence Actually Proves:** 在该 runner/tasks 下，平均正确率相近的模型可有显著不同的 run-to-run consistency；format contract与guardrail也会成为 failure source。
- **What It Does Not Prove:** 不证明某模型普遍最可靠；不代表 repository agent、interactive debugging、真实 CI 或 backend software lifecycle能力。
- **Limitations / Threats to Validity:** 仅65题、front-end偏置、有限模型、直接输出无反馈、public benchmark污染风险、parser/test harness对结果敏感。
- **Trade-offs / New Failure Modes:** repeated-run evaluation更接近可靠性，却增加成本；公开复杂任务提升 realism，也增加环境漂移、test leakage 与 harness ownership问题。
- **Where the Previous Design Still Applies:** unit-function benchmarks仍适合低成本模型迭代；真实 Agent评估需在 ASTRA-like artifact correctness之上加入 tools、state与feedback loop。
- **Evolution Relationship:** `Layering / Dependency`：single-file answer→multi-file artifact→repeated consistency→agentic repository workflow。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `AGENT-TOOL-CALLING`（Ch78）、`AGENT-WORKFLOW`（Ch81）与 `PLATFORM-PRODUCTION`（Ch73）。
- **Target and Adjacent Chapters Read:** 已核对 Ch66～73 与 Ch78～84，确认 model capability、harness、artifact与workflow不混为一谈。
- **Existing Coverage:** Books 已区分 pass@k与executable artifacts；本 family增加 repeated consistency和format contract案例。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不保留脱离 snapshot/runner/task mix 的模型排名。
- **Open Questions:** 如何加入 hermetic environments、iterative tests、repo history、security policy、cost和failure recovery而保持可复算。

### Weak-to-Strong Diffusion

- **Candidate / Week / Score:** Weak-to-Strong Diffusion / 2025-W05 / 22/30。
- **Source Family ID:** `w2sd-reflective-diffusion-sampling`。
- **Source Type:** 作者论文 / arXiv v1（Experimental）。
- **First-public Date / Revision History:** v1 2025-02-01；v2/v3 归同一 family，owner 锁定 W05。
- **Direct Primary Sources:** https://arxiv.org/html/2502.00473v1；https://arxiv.org/abs/2502.00473。
- **Related Primary Sources:** diffusion inversion、guidance、resampling及 weak/strong model pairs只定义机制 lineage。
- **Access and Verification Status:** Verified；theory、method、multi-branch experiments、runtime comparison、appendices 与 proof可访问。
- **Full-read Coverage:** 已读 score/diffusion preliminaries、density-gradient difference、reflection loop、1D/2D/real visualizations、weight/LoRA/MoE/condition/sampler branches、cumulative combination、magnitude/runtime sensitivity、datasets/metrics、video results、proof与inversion-error analysis。
- **Original Problem:** 已训练 diffusion model 与理想数据分布有残余 gap；重训/偏好微调昂贵，普通 guidance只能改变条件强度而不直接利用模型质量差。
- **Why the Previous Design Was Reasonable:** 单模型 denoising loop简单、稳定且部署成熟；classifier-free guidance与fine-tuning分别适合 prompt adherence和持久改模。
- **Changed Constraint:** 平台常同时拥有 weak/strong checkpoints、LoRA、MoE experts或samplers；它们之间的score difference可成为无需新训练的inference signal。
- **Mechanism:** 估计 weak与strong model的density-gradient difference，把它当作 strong→ideal direction近似；sampling中交替 denoising、inversion和difference-guided reflection修正trajectory。
- **State Ownership:** base/weak/strong models和pair identity属于artifact registry；sampler拥有timestep、latent、reflection count和difference scale；组合多个difference需显式顺序与版本。
- **Control Flow / Data Flow:** noisy latent→strong denoise→weak/strong score difference→inversion/reflection→修正latent→继续denoise；可累积weight、condition、pipeline差异。
- **Implementation Details:** 每次reflection增加额外 score evaluations；作者用减少standard denoise steps匹配time budget；效果依赖pair方向、difference magnitude和inversion approximation。
- **Evaluation Contract:** image/video、UNet/DiT/MoE、多个 weak/strong pairs，Pick-a-Pic/DrawBench/GenEval/VBench等；使用AES/PickScore/HPSv2/MPS及human preference。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较standard sampling、不同pair、LoRA/MoE/CFG/sampler difference、累计组合、scale和同时间预算；许多结论依赖自动偏好指标。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** models/steps/metrics与相对time设置披露；hardware、precision、batch/concurrency、memory与production latency/SLO不完整。
- **What the Evidence Actually Proves:** 在作者选择的pair和生成评测中，model-difference可作为runtime correction signal；收益不是免费，必须计入额外score/inversion计算。
- **What It Does Not Prove:** 不证明任意弱强pair都指向真实分布、不保证自动偏好提升等于物理/语义正确，也不证明同吞吐/并发下优于重训或普通sampling。
- **Limitations / Threats to Validity:** pair选择与“ideal direction”假设、inversion error、metric bias、有限模型/数据、无独立复现与生产memory/throughput评估。
- **Trade-offs / New Failure Modes:** 复用现有artifacts避免训练，却增加双模型storage/compute、pair version skew、trajectory instability、组合冲突与动态shape成本。
- **Where the Previous Design Still Applies:** 单checkpoint低延迟服务仍用standard sampler；高频固定domain可通过fine-tune/distillation摊销，W2SD适合有明确强弱pair且可接受额外compute的quality tier。
- **Evolution Relationship:** `Alternative Branch`：retrain/adapter、guidance、resampling与model-difference reflection按artifact cost和online compute分叉。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `INFER-REQUEST-LIFECYCLE`（Ch42）、`INFER-SCHEDULING`（Ch56）与 `PLATFORM-MODEL-REGISTRY`（Ch59）。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～25、Ch42、Ch56～59，确认generation mechanism、runtime budget与artifact pair分层。
- **Existing Coverage:** Books 已有diffusion correction branch；本 family补足用checkpoint difference驱动reflection的runtime选择。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W05；不将HPS胜率写成通用quality或production性能结论。
- **Open Questions:** pair selection、artifact compatibility、batched dual-model execution、rollback、physical consistency与cost-aware routing如何闭环。

### Low-Score Verification Ledger

| Candidate | Identity / Date Check | Evidence Boundary | Final Disposition |
| --- | --- | --- | --- |
| Qwen2.5-Max | 官方 Blog，2025-01-28 | 公开 MoE/训练数据与 benchmark 为厂商描述，缺 technical report、implementation 与完整 workload contract | `Weekly Only — Version Fact / Mechanism Not Disclosed` |
| Mistral Small 3 | 官方 release，2025-01-30 | 可核对 model size、license 与 deployment positioning；训练/runtime 内部机制未公开 | `Weekly Only — Model Release Fact` |
| OpenAI o3-mini | 官方 product/model release，2025-01-31 | 可核对产品、reasoning effort 与 safety/evaluation披露；architecture、training 与 serving contract 未公开 | `Weekly Only — Product Contract / Mechanism Not Disclosed` |
| MR.Q | arXiv v1，2025-01-27 | 提出用于连续控制的 model-free RL 方法；与当前 AI System 主线关联弱，且证据集中在作者控制任务 | `Weekly Only — General RL Research` |
| DiffSplat | arXiv v1，2025-01-28 | 单图 3D Gaussian 生成的 diffusion recipe，属于窄域 representation/generation 案例，未形成通用系统 owner 缺口 | `Weekly Only — Narrow 3D Generation Case` |
| LLMs Think Too Fast | arXiv v1，2025-01-29 | 单环境 observational/intervention study；“thinking speed”指标不能当作普遍 causal reasoning contract | `Weekly Only — Single-environment Exploratory Study` |
| CowPilot | arXiv v1，2025-01-28 | 证明 human-agent collaborative web-navigation prototype 可运行；仅五个网站 case study，生产 workflow 证据有限 | `Weekly Only — Research Prototype` |
| SSQR | arXiv v1，2025-01-30 | self-supervised VQ 把 KG triples 压成与 text embedding 对齐的量化表示；作者 KG/QA 设置不足以证明通用 RAG 或 memory owner 变化 | `Weekly Only — Narrow KG Representation Case` |
| Multi-View Geometric Diffusion | arXiv v1，2025-01-30 | zero-shot novel-view/depth 的多视图几何 diffusion 机制与项目页已核验；属于窄域 3D 生成分支，缺长期 AI System owner 缺口 | `Weekly Only — Narrow 3D Generation Case` |
| AIN | arXiv v1，2025-01-31；v2 2025-02-04 | Arabic-centric multimodal data/model/evaluation identity 已核验；模型 recipe 与语言覆盖有价值，但不形成独立通用 representation 机制 | `Weekly Only — Language-Specific Multimodal Model Case` |
| Pathology Foundation Model Site Shift | arXiv v1，2025-01-29；v2 2025-02-01 | medical-center distribution shift、foundation-model embeddings 与 downstream comparison 已核验；重要 domain robustness 警示但证据窄且临床外推受限 | `Weekly Only — Domain Robustness Case` |
| News Summarization Capability Study | arXiv v1，2025-01-30 | 模型/数据/summary quality analysis 已核验；单一任务研究不改变通用 evaluation、RAG 或 workflow 设计结论 | `Weekly Only — Narrow Task Evaluation` |
| INT Promptable Segmentation | arXiv v1，2025-01-30 | instance-specific negative mining 与 segmentation evaluation identity 已核验；属于窄域 vision training recipe | `Weekly Only — Narrow Vision Recipe` |
| Transformers 4.48.2 | 官方 GitHub Release，2025-01-30 | compatibility/bug-fix release，没有独立长期机制；4.48.1 已按发布日期回拨 W04 | `Weekly Only — Compatibility Patch` |
| Text-to-CAD / CADFusion | arXiv v1，2025-01-31；v2 2025-02-05 | alternating sequential supervision 与 rendered-visual feedback 对 CAD parametric generation 有效，但属于窄域 artifact workflow；缺通用 Agent/runtime owner 与完整工程 contract | `Weekly Only — Narrow CAD Generation Case` |
| Low-Resource Programming-Language Code Generation | arXiv v1，2025-01-31 | R/Racket上比较fine-tuning、ICL与translation objective；结果显示策略随模型规模改变，但仅两种语言与六模型，属于窄域empirical branch | `Weekly Only — Narrow Empirical Study` |

## Evidence Level

- **Level A — Direct Primary Evidence:** 官方 release/design 文档、arXiv 全文、作者 repository 与
  artifact；39 个 `20+` 候选均已读取正文、关键 appendices 与可获得 artifact。
- **Level B — Official Version Fact:** Qwen2.5-Max、Mistral Small 3、o3-mini 与 Transformers 4.48.2
  只证明厂商/项目公开的版本 contract；未披露机制一律写为 `Not Disclosed`。
- **Level C — Author Experimental Result:** 论文 benchmark 只在作者披露的 model、data、hardware、
  precision、length、batch/concurrency 与 evaluator contract 内成立；缺项显式记录，不外推生产 SLO。
- **Project Inference:** 跨来源的 owner、state/control-flow 与 evolution 连接属于本项目推断，已与官方
  事实和作者实验分开，不使用社区评论作为机制证据。

## Cross-Week Deduplication

- `Transformers 4.48.1` 首发 2025-01-20，已回拨 W04；本周只保留 2025-01-30 的 4.48.2。
- Janus-Pro、PhysBench、s1 等后续 revision 均保留在同一 Source Family，不按修订日重复计分。
- OpenAI o3-mini 产品发布与 external safety testing 是两个 Source Family：前者是 version/product
  contract，后者是独立 pre-deployment evidence；不合并成厂商自证。
- SFT/RL、s1/Underthinking、Critique/Atla、Virus/GuardReasoner 分别形成训练、decode、evaluator 与
  security 的演进关系，但不是相互替代路线。
- W06 discovery 页面中的推荐日期不作 event date：本次 25 项均按 arXiv v1 回拨 W05；MatAnyone 回拨
  W04，TracksTo4D 因 first-public 为 2024 年未重复计入 2025。
- `Rethinking Mixture-of-Agents` 的 v1 为 2025-02-02，归 W05；W06 只保留 2025-02-03 起首发的候选。
  Concept Steerers、FSLoRA、Text-to-CAD 与 Activation Approximation Safety 同理按 v1 回拨，不按 HF 推荐日计事件。
- RAG Interrogation Attack、HackerRank-ASTRA、Weak-to-Strong Diffusion 与 low-resource code study 也由
  2月6～7日推荐页回拨；其中前三项完成全文审计，后一项完成低分处置。

## Knowledge Tree Position

- `INFER-VLLM` / `INFER-SCHEDULING`：vLLM V1、s1 与 Underthinking，分别拥有 engine state、fleet
  capacity 与 decode-control/evidence 边界。
- `TRAIN-PRETRAINING` / `TRAIN-SFT` / `TRAIN-RLHF` / `TRAIN-DISTRIBUTED-TRAINING`：FP4、TAID、
  Critique FT、SFT-vs-RL 与 Streaming DiLoCo。
- `MODEL-TOKENIZER` / `MODEL-MOE` / `MULTIMODAL-REPRESENTATION`：Over-Tokenized、Mixture-of-Mamba、
  Janus-Pro；SANA 1.5 归 `MULTIMODAL-GENERATIVE-PARADIGMS`。
- `PLATFORM-EVALUATION-SYSTEM`：Atla、MedXpertQA、PhysBench 与 interpretability research agenda；
  `PLATFORM-SECURITY`：external o3-mini testing、Virus、GuardReasoner。
- `TRAIN-DATA`：WildChat-50M；`AGENT-WORKFLOW`：deep research 只保留产品能力与未公开机制边界。
- `AGENT-MULTI-AGENT`：Rethinking Mixture-of-Agents；其结论是 quality/diversity/cost 的条件分支，
  不把 repeated sampling 当作 multi-agent workflow 的通用替代。
- `TRAIN-LORA`：Federated Sketching LoRA；`PLATFORM-SECURITY`：Activation Approximation Safety 与
  Concept Steerers，分别约束 execution-plan certification 与生成 policy artifact。
- `PLATFORM-SECURITY` / `AGENT-RAG`：RAG Interrogation Attack；`PLATFORM-EVALUATION-SYSTEM`：
  HackerRank-ASTRA；`MULTIMODAL-GENERATIVE-PARADIGMS`：Weak-to-Strong Diffusion。
- `INFER-SPECULATIVE-DECODING` / `INFER-KV-CACHE`：Reward-Guided Speculative Decoding 与 ChunkKV；
  前者是有偏 routing branch，后者是 lossy semantic retention branch。
- `MODEL-ATTENTION` / `MULTIMODAL-REPRESENTATION`：Scalable-Softmax 与 PixelWorld；分别处理
  length-dependent normalization 和 rendered-pixel representation，不否定标准 softmax/tokenizer。
- `TRAIN-PRETRAINING`：learning-rate scheduling；`PLATFORM-SECURITY`：Constitutional Classifiers、
  SafeRAG、adversarial compute 与 SAeUron；`PLATFORM-EVALUATION-SYSTEM`：MM-IQ。

## Recommended Action

- **Archive:** W05 Weekly Evidence Gate 通过；55/55 候选有最终 disposition，39/39 高分完成非模板化
  Full Source Review，16/16 低分完成 identity/date/score/rejection 核验。
- **Books:** 全部可吸收项保持 `Books Pending — Integration Deferred`；deep research 与三项模型发布只
  保留 version/product fact，不从能力反推内部 architecture。
- **Follow-up:** 后续周按 Source Family 串联 vLLM V1、test-time compute、post-training、physical-world
  evaluation、guardrail 与 low-bandwidth training 的演进，不让后发方案覆盖旧方案适用条件。

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

`Historical Books Gate: Closed`。用户明确要求先完成 2025 Weekly；本周未修改 `books/`。所有
`Books Pending` 只表示未来需要逐 Source Family 重新读取 owner 与相邻章节，不表示已吸收或必须修改。

## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。
- Hugging Face Daily Papers 只作 discovery cursor；所有保留机制均回到 arXiv/作者项目，营销式二手摘要
  与没有唯一 identity 的标题不进入评分表。

## Repository Changes

- 幂等重建 `papers/2025/weekly/2025-W05/README.md`：从旧 3 项扩展为 55 项候选 census。
- 补齐 39 个 Full Source Review、16 项低分核验、fixed-source/academic/infra coverage、跨周去重、
  Stable Node owner 与 Books Gate 冻结状态。
- `Transformers 4.48.1` 已按首发日期回拨 W04；本周只记录 4.48.2。
- W06 discovery spillback 恢复 17 个 `20+` Source Family 与 8 个低分候选；所有 event owner 均按
  arXiv v1 而非 Hugging Face 推荐日期确定，并联读 Constitutional Classifiers 的后续官方失败更新。
- 未修改 `books/`，未创建 2025 Daily。

## Open Questions

- vLLM V1 的 diff reconciliation、cancellation、failure recovery 与 V0/V1 equivalence 如何验证。
- test-time token control、Underthinking 与真实 GPU cost/SLO 能否形成跨模型校准的 policy。
- Streaming DiLoCo 在 failure/rejoin、heterogeneous link 与 optimizer/checkpoint recovery 下是否仍稳定。
- FP4 training、Mixture-of-Mamba 与 Janus-Pro 的收益如何在不同 hardware/kernel/runtime 下闭合端到端
  contract，而不是停在作者 FLOP/quality 指标。
- Virus、GuardReasoner 与 external safety testing 能否共享 threat taxonomy、operating point 与 release gate，
  又不把 guard reasoning 当作忠实解释。
- PhysBench 如何从 multiple-choice 扩展到 transition/action/safety evidence；PhysAgent 的 component
  ablation、真实机器人和 artifact completeness 仍需后续证据。
- OpenAI deep research 的 planner、state ownership、citation entailment 与 recovery 仍未公开。
- reward-guided decoding 的 PRM drift、ChunkKV 的 lossy rollback、SafeRAG 的 poisoned-index delete/rebuild、
  Constitutional Classifiers 的 policy/version atomicity 与双边 adversarial compute budget 仍需后续系统证据。
- Self-/Mixed-MoA 的真实 GPU/token/tail-latency contract、FSLoRA 的 dropout/secure aggregation、activation
  approximation 的组合认证矩阵，以及 k-SAE steering 的 artifact drift 与 adaptive bypass 仍需后续证据。

## Sources

- vLLM V1 Alpha — https://vllm.ai/blog/2025-01-27-v1-alpha-release（First Public: 2025-01-27；Accessed: 2026-08-18）
- PyTorch 2.6 — https://pytorch.org/blog/pytorch2-6/（First Public: 2025-01-29；Accessed: 2026-08-18）
- Streaming DiLoCo — https://arxiv.org/abs/2501.18512（v1: 2025-01-30；Accessed: 2026-08-18）
- Janus-Pro — https://arxiv.org/abs/2501.17811（v1: 2025-01-28；Accessed: 2026-08-18）
- Mixture-of-Mamba — https://arxiv.org/abs/2501.16295（v1: 2025-01-27；Accessed: 2026-08-18）
- SFT Memorizes, RL Generalizes — https://arxiv.org/abs/2501.17161（v1: 2025-01-28；Accessed: 2026-08-18）
- Training LLMs with MXFP4 — https://arxiv.org/abs/2501.17116（v1: 2025-01-28；Accessed: 2026-08-18）
- s1: Simple test-time scaling — https://arxiv.org/abs/2501.19393（v1: 2025-01-31；Accessed: 2026-08-18）
- Over-Tokenized Transformer — https://arxiv.org/abs/2501.16975（v1: 2025-01-28；Accessed: 2026-08-18）
- GuardReasoner — https://arxiv.org/abs/2501.18492（v1: 2025-01-30；Accessed: 2026-08-18）
- SANA 1.5 — https://arxiv.org/abs/2501.18427（v1: 2025-01-30；Accessed: 2026-08-18）
- OpenAI deep research — https://openai.com/index/introducing-deep-research/（First Public: 2025-02-02；Accessed: 2026-08-18）
- Open Problems in Mechanistic Interpretability — https://arxiv.org/abs/2501.16496（v1: 2025-01-27；Accessed: 2026-08-18）
- TAID — https://arxiv.org/abs/2501.16937（v1: 2025-01-28；Accessed: 2026-08-18）
- Critique Fine-Tuning — https://arxiv.org/abs/2501.17703（v1: 2025-01-28；Accessed: 2026-08-18）
- Atla Selene Mini — https://arxiv.org/abs/2501.17195（v1: 2025-01-28；Accessed: 2026-08-18）
- Early External Safety Testing of o3-mini — https://arxiv.org/abs/2501.17749（v1: 2025-01-28；Accessed: 2026-08-18）
- Virus — https://arxiv.org/abs/2501.17433（v1: 2025-01-28；Accessed: 2026-08-18）
- Underthinking — https://arxiv.org/abs/2501.18585（v1: 2025-01-30；Accessed: 2026-08-18）
- WildChat-50M — https://arxiv.org/abs/2501.18511（v1: 2025-01-30；Accessed: 2026-08-18）
- MedXpertQA — https://arxiv.org/abs/2501.18362（v1: 2025-01-30；Accessed: 2026-08-18）
- PhysBench — https://arxiv.org/abs/2501.16411（v1: 2025-01-27；Accessed: 2026-08-18）
- Constitutional Classifiers — https://arxiv.org/html/2501.18837v1；https://www.anthropic.com/news/constitutional-classifiers（paper v1: 2025-01-31；official Blog: 2025-02-03；Accessed: 2026-08-18）
- ChunkKV — https://arxiv.org/html/2502.00299v1；https://arxiv.org/abs/2502.00299（v1: 2025-02-01；Accessed: 2026-08-18）
- Reward-Guided Speculative Decoding — https://arxiv.org/html/2501.19324v1；https://arxiv.org/abs/2501.19324（v1: 2025-01-31；Accessed: 2026-08-18）
- Learning-Rate Scheduling for Large Model Training — https://arxiv.org/html/2501.18965v1；https://arxiv.org/abs/2501.18965（v1: 2025-01-31；Accessed: 2026-08-18）
- SafeRAG — https://arxiv.org/html/2501.18636v1；https://arxiv.org/abs/2501.18636（v1: 2025-01-28；Accessed: 2026-08-18）
- Trading Inference-Time Compute for Adversarial Robustness — https://arxiv.org/html/2501.18841v1；https://arxiv.org/abs/2501.18841（v1: 2025-01-31；Accessed: 2026-08-18）
- Scalable-Softmax — https://arxiv.org/html/2501.19399v1；https://arxiv.org/abs/2501.19399（v1: 2025-01-31；Accessed: 2026-08-18）
- PixelWorld — https://arxiv.org/html/2501.19339v1；https://arxiv.org/abs/2501.19339（v1: 2025-01-31；Accessed: 2026-08-18）
- SAeUron — https://arxiv.org/abs/2501.18052；https://arxiv.org/pdf/2501.18052v1；https://github.com/cywinski/SAeUron（v1: 2025-01-29；Accessed: 2026-08-18；same-ID PDF used after HTML mismatch）
- MM-IQ — https://arxiv.org/html/2502.00698v1；https://arxiv.org/abs/2502.00698（v1: 2025-02-02；Accessed: 2026-08-18）
- Rethinking Mixture-of-Agents — https://arxiv.org/html/2502.00674v1；https://arxiv.org/abs/2502.00674（v1: 2025-02-02；Accessed: 2026-08-18）
- Federated Sketching LoRA — https://arxiv.org/html/2501.19389v1；https://arxiv.org/abs/2501.19389（v1: 2025-01-31；Accessed: 2026-08-18）
- Activation Approximation Safety — https://arxiv.org/html/2502.00840v1；https://arxiv.org/abs/2502.00840（v1: 2025-02-02；Accessed: 2026-08-18）
- Concept Steerers — https://arxiv.org/html/2501.19066v1；https://arxiv.org/abs/2501.19066；https://github.com/kim-dahye/steerers（v1: 2025-01-31；Accessed: 2026-08-18）
- Text-to-CAD / CADFusion — https://arxiv.org/abs/2501.19054（v1: 2025-01-31；Accessed: 2026-08-18）
- RAG Interrogation Attack — https://arxiv.org/html/2502.00306v1；https://arxiv.org/abs/2502.00306（v1: 2025-02-01；Accessed: 2026-08-18）
- HackerRank-ASTRA — https://arxiv.org/html/2502.00226v1；https://arxiv.org/abs/2502.00226；https://huggingface.co/datasets/hackerrank/astra-benchmark（v1: 2025-01-31；Accessed: 2026-08-18）
- Weak-to-Strong Diffusion — https://arxiv.org/html/2502.00473v1；https://arxiv.org/abs/2502.00473（v1: 2025-02-01；Accessed: 2026-08-18）
- Low-Resource Programming-Language Code Generation — https://arxiv.org/abs/2501.19085（v1: 2025-01-31；Accessed: 2026-08-18）
- SSQR — https://arxiv.org/abs/2501.18119（v1: 2025-01-30；Accessed: 2026-08-18）
- Multi-View Geometric Diffusion — https://arxiv.org/abs/2501.18804（v1: 2025-01-30；Accessed: 2026-08-18）
- AIN — https://arxiv.org/abs/2502.00094（v1: 2025-01-31；Accessed: 2026-08-18）
- Pathology Foundation Model Site Shift — https://arxiv.org/abs/2501.18055（v1: 2025-01-29；Accessed: 2026-08-18）
- News Summarization Capability Study — https://arxiv.org/abs/2501.18128（v1: 2025-01-30；Accessed: 2026-08-18）
- INT Promptable Segmentation — https://arxiv.org/abs/2501.18753（v1: 2025-01-30；Accessed: 2026-08-18）
- Qwen2.5-Max — https://qwenlm.github.io/blog/qwen2.5-max/（First Public: 2025-01-28；Accessed: 2026-08-18）
- Mistral Small 3 — https://mistral.ai/news/mistral-small-3（First Public: 2025-01-30；Accessed: 2026-08-18）
- OpenAI o3-mini — https://openai.com/index/openai-o3-mini/（First Public: 2025-01-31；Accessed: 2026-08-18）
- MR.Q — https://arxiv.org/abs/2501.16142（v1: 2025-01-27；Accessed: 2026-08-18）
- DiffSplat — https://arxiv.org/abs/2501.16764（v1: 2025-01-28；Accessed: 2026-08-18）
- Large Language Models Think Too Fast To Explore Effectively — https://arxiv.org/abs/2501.18009（v1: 2025-01-29；Accessed: 2026-08-18）
- CowPilot — https://arxiv.org/abs/2501.16609（v1: 2025-01-28；Accessed: 2026-08-18）
- Transformers 4.48.2 — https://github.com/huggingface/transformers/releases/tag/v4.48.2（First Public: 2025-01-30；Accessed: 2026-08-18）
