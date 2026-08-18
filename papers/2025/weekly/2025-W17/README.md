# AI Research Weekly — 2025-W17

> Coverage Window: 2025-04-21～2025-04-27
> Research Mode: Retrospective Primary-Source Backfill
> Re-audited: 2026-08-24
> Audit Status: Discovery Replay Closed — Primary-Source Review 61/66 Retained Rows Strict / 5 Unverified-Blocked
> Historical Books Gate: Closed

## Executive Summary

旧档案只保留 PyTorch 2.7 与 Kubernetes v1.33，远低于接近 Live Daily 的发现标准。按 2025-W17 的完整 ISO 窗口重放固定机构、学术索引与 AI Infra 后，本周账本闭合为 **80 个唯一 Source Family**：22 个高分、44 个中分、14 个低分。66 个 `20+` 候选中 61 个完成 strict Full Source Review；CameraBench、Roll the Dice、RealisDance-DiT、All-Angles Bench 与 Uni3C 因 event-time 正文无法完整取得，明确保留为 `Unverified / Blocked`，不以摘要冒充全文。14 个低分候选均完成来源、日期、评分与拒绝理由闭合；Disputed 为 0。

本周 Discovery Replay 已闭合，但 Candidate Evidence Gate 因 5 个 blocked family 仍为 `Not Passed`。它们可以在后续材料恢复时回补，不阻塞 W18 之后的 forward sweep；Historical Books Gate 继续关闭。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；本轮主来源 Accessed 为 2026-08-22。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。
- 4月21～27日 arXiv daily pages、后续 revision lineage 与可访问的 Scholar/OpenAlex/DBLP/Crossref metadata 已交叉回放；搜索结果用于召回，正文才用于机制结论。
- 固定机构逐项完成 `retained / routed / no material update` 记录；未找到事件不等于证明机构当周没有任何内部进展。
- 固定工程项目逐项检查 release/RFC/PR；只有 PyTorch 2.7、Kubernetes v1.33 与 SGLang v0.4.6 落在本周并达到保留门槛，其余为邻周路由或无长期机制增量。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留 OpenAI gpt-image-1 产品事实与 Anthropic malicious-use 报告 family；后者的 linked full report 已完成正文与案例边界审计。
- Google Lyria 2 / Music AI Sandbox为19分版本事实，完成低分闭合。
- Apple、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog：本窗口未发现达到本周 owner 门槛、且 first-public date 可归 W17 的新增机制 family。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 定位 74 个学术 source family；其中 61 个 `20+` family 可完成 event-time 全文审计，4 个学术 family 只能取得摘要/项目页而保持 blocked，低分论文按来源、日期与拒绝理由闭合。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 保留：PyTorch 2.7（2025-04-23）。
- 保留：Kubernetes v1.33（2025-04-23）。
- 保留：SGLang v0.4.6（GitHub release timestamp 为 2025-04-27；此前写作 2025-04-22 已纠正）。
- JAX、CUDA、Triton、vLLM、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA：未发现本窗口内达到本周独立 source-family 门槛的 release/RFC/PR；vLLM v0.8.4、DeepSpeed 0.16.7 与 Transformers 4.51.3 按 first-public date 回拨 W16。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| LUFFY | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete |
| OTC-PO | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| Efficient Pretraining Length Scaling / PHD Transformer | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| Adaptive Parallel Reasoning | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| FlowReasoner | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| Eagle2.5 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| TTRL | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete |
| Tina | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| Skywork-R1V2 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| AIMO-2 | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Full Source Review Complete |
| ThinkPRM | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| Paper2Code | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| Sparse Frontier | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete |
| BitNet v2 | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete |
| Kimi-Audio | 5 | 4 | 5 | 4 | 5 | 4 | 27/30 | Full Source Review Complete |
| Pleias-RAG | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete |
| PropRAG | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| OpenAI gpt-image-1 API | 3 | 4 | 4 | 5 | 3 | 2 | 21/30 | Full Source Review Complete — Version Fact |
| Anthropic Harms Framework | 2 | 3 | 3 | 5 | 3 | 3 | 19/30 | Low-score closure |
| Anthropic malicious-use report | 3 | 4 | 4 | 5 | 3 | 3 | 22/30 | Full Source Review Complete |
| PyTorch 2.7 | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete — Version Fact |
| Kubernetes v1.33 | 3 | 3 | 3 | 4 | 4 | 3 | 20/30 | Full Source Review Complete — Version Fact |
| SGLang v0.4.6 | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Full Source Review Complete — Versioned runtime |
| EasyEdit2 | 3 | 4 | 4 | 4 | 4 | 3 | 22/30 | Full Source Review Complete |
| Kuwain 1.5B | 3 | 4 | 4 | 4 | 4 | 3 | 22/30 | Full Source Review Complete |
| Trillion-7B technical report | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| VisuLogic | 3 | 4 | 4 | 4 | 4 | 3 | 22/30 | Full Source Review Complete |
| Describe Anything Model | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| Bitter Lesson from 2,000+ Multilingual Benchmarks | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Full Source Review Complete |
| LiveCC | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Full Source Review Complete |
| WALL-E 2.0 | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Full Source Review Complete |
| LLMs are Greedy Agents | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete |
| ReflectionFlow | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| Vidi | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| PHYBench | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Full Source Review Complete |
| Full-Stack Safety Survey | 2 | 4 | 3 | 4 | 4 | 5 | 22/30 | Full Source Review Complete — Secondary synthesis |
| Pre-DPO | 4 | 3 | 4 | 4 | 4 | 4 | 23/30 | Full Source Review Complete |
| I-Con | 4 | 3 | 3 | 5 | 4 | 5 | 24/30 | Full Source Review Complete |
| QuaDMix | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| MMLA benchmark | 3 | 2 | 3 | 4 | 4 | 4 | 20/30 | Full Source Review Complete |
| SAVA tokenizer adaptation | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| CameraBench | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Unverified / Blocked — event-time full text unavailable |
| Zero-shot Subject Video Generation | 4 | 4 | 4 | 4 | 4 | 5 | 25/30 | Full Source Review Complete |
| Step1X-Edit | 3 | 3 | 4 | 3 | 5 | 5 | 23/30 | Full Source Review Complete |
| RefVNLI | 3 | 3 | 4 | 4 | 4 | 5 | 23/30 | Full Source Review Complete |
| UniME | 4 | 4 | 4 | 4 | 4 | 5 | 25/30 | Full Source Review Complete |
| APC Mental Imagery | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| Token-Shuffle | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| TimeChat-Online | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| DyMU | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| Code-grounded math evaluation | 3 | 3 | 4 | 3 | 4 | 3 | 20/30 | Full Source Review Complete |
| Auto-SLURP | 3 | 4 | 4 | 4 | 4 | 3 | 22/30 | Full Source Review Complete |
| DRAGON distributional reward optimization | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| Quicksviewer adaptive video tokens | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| Roll the Dice, but Look Before You Leap | 4 | 4 | 4 | 3 | 4 | 4 | 23/30 | Unverified / Blocked — abstract only |
| RainbowPlus automated red teaming | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete |
| CRUST-Bench | 3 | 4 | 4 | 4 | 3 | 3 | 21/30 | Full Source Review Complete |
| IV-Bench image-centric video understanding | 3 | 3 | 4 | 4 | 3 | 3 | 20/30 | Full Source Review Complete |
| MR Video long-video MapReduce | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete |
| RePOPE hallucination re-evaluation | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Full Source Review Complete |
| ReDi joint image-feature diffusion | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete |
| DreamO unified image customization | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete |
| DeGLA global-local vision-language alignment | 4 | 4 | 4 | 4 | 3 | 3 | 22/30 | Full Source Review Complete |
| Semantic Orders for autoregressive image generation | 4 | 4 | 4 | 4 | 3 | 3 | 22/30 | Full Source Review Complete |
| RealisDance-DiT | 4 | 4 | 4 | 3 | 3 | 3 | 21/30 | Unverified / Blocked — abstract only |
| All-Angles Bench | 3 | 3 | 4 | 3 | 4 | 3 | 20/30 | Unverified / Blocked — abstract only |
| Uni3C unified 3D human control | 4 | 4 | 4 | 3 | 3 | 3 | 21/30 | Unverified / Blocked — abstract/project summary only |
| DianJin-R1 | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Low-score closure |
| IberBench | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| VideoVista Cultural | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| Conversational Assistant study | 2 | 2 | 3 | 4 | 3 | 2 | 16/30 | Low-score closure |
| Preferred-MedLLM | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Low-score closure |
| MultiMind | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Low-score closure |
| Google Lyria 2 / Music AI Sandbox | 2 | 3 | 4 | 5 | 3 | 2 | 19/30 | Low-score closure — Version Fact |
| CAPTURe occluded-object counting | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| IPBench intellectual-property reasoning | 3 | 2 | 3 | 4 | 3 | 3 | 18/30 | Low-score closure |
| ViSMaP long-video summarization | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| DiMeR diffusion mesh reconstruction | 3 | 3 | 3 | 3 | 3 | 3 | 18/30 | Low-score closure |
| 3DV-TON virtual try-on | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| Dynamic Camera Poses dataset | 3 | 3 | 3 | 3 | 3 | 3 | 18/30 | Low-score closure |

账目：80 rows；22 high、44 medium、14 low；61/66 retained Full Source Reviews strict complete；Review Pending 0；14/14 low-score closures；Blocked 5、Disputed 0。

### Deep Analysis 1 — PyTorch 2.7

- First Public: 2025-04-23
- Status: Official stable release
- Primary Source: https://pytorch.org/blog/pytorch-2-7/
- Evolution Relationship: Layering / Dependency

#### Why

新硬件和动态模型结构要求编译器既能缓存编译结果，又能保留可扩展 attention 与用户自定义语义。

#### Principle and Mechanism

2.7 加入 Blackwell/CUDA 12.8 支持、Mega Cache、FlexAttention inference 更新与 torch.compile 扩展；这些是版本化实现事实。

#### Trade-off and Evidence Boundary

编译缓存降低重复编译成本，却新增 cache key、可移植性和失效语义；FlexAttention 的可表达性仍受后端 kernel 与 shape coverage 约束。

#### Connection and Evolution

知识树位置：第 17、32、45 章。Worth Watching；版本细节留 Weekly。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 2 — Kubernetes v1.33

- First Public: 2025-04-23
- Status: Official stable release
- Primary Source: https://kubernetes.io/blog/2025/04/23/kubernetes-v1-33-release/
- Evolution Relationship: Layering / Dependency

#### Why

AI workload 依赖通用 orchestration 的资源、job 与生命周期语义，但通用 release 不能自动变成 AI-native scheduling。

#### Principle and Mechanism

官方 release 提供平台 API 演进事实；本周未发现单项变化足以改变 AI System 章节结论。

#### Trade-off and Evidence Boundary

平台升级带来能力与维护成本，需区分 Kubernetes primitive 与上层 training/serving control plane。

#### Connection and Evolution

知识树位置：第 53～61 章。Record Only；不写入 Books。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### PyTorch 2.7

- **Candidate / Week / Score:** PyTorch 2.7 / 2025-W17 / 23/30。
- **Source Family ID:** `pytorch-2.7-compiler-attention-distributed`。
- **Source Type:** 官方 release blog、GitHub v2.7.0 release notes、相关官方 tutorials/PR links；不是研究论文。
- **First-public Date / Revision History:** v2.7.0 与 blog 为 2025-04-23；v2.7.1 于 2025-06-04 修复 compile、FlexAttention、Distributed 等回归。2.7.1 只作为 revision evidence，不改写本周 first-public。
- **Direct Primary Sources:** PyTorch 2.7 Release blog；pytorch/pytorch v2.7.0 release notes。
- **Related Primary Sources:** v2.7.1 fix release；Native Context Parallel、Mega Cache、FlexAttention 官方教程和对应 PR。
- **Access and Verification Status:** Verified；blog、2.7.0 highlights/BC breaks/deprecations/regressions 与 2.7.1 corrections 已核对。3262 commits 不逐 PR 全读，机制结论只采用 release 明示范围。
- **Full-read Coverage:** compiler modes、Mega Cache、Blackwell/CUDA 12.8、Triton 3.3、Native Context Parallel、FlexAttention inference/x86、compatibility、tracked regressions、breaking changes、2.7.1 correctness fixes。
- **Original Problem:** 新 accelerator、可定制 attention 与重复编译使 framework 既要扩展 operator semantics，又要减少 cold compilation，并把长上下文 attention 分布到多设备。
- **Why the Previous Design Was Reasonable:** 每进程本地 compiler cache 简单且与环境绑定；固定 SDPA backend 便于优化；framework 等硬件稳定后再支持能降低 compatibility surface。
- **Changed Constraint:** Blackwell/CUDA 12.8 上线、dynamic/user-defined op behavior 增多、同一模型跨机器启动，以及长 context 训练需要 context parallel。
- **Mechanism:** Torch Function Modes 允许改写 torch ops；Mega Cache 序列化 compile artifacts 并在另一机器预填 cache；prototype Context Parallel 用 context manager 包住 SDPA 并支持 Flash/Efficient/cuDNN attention backends；FlexAttention inference 与 x86 modes 扩展 backend coverage。
- **State Ownership:** application/framework 拥有 graph、guards 与 cache artifacts；runtime/backend 拥有 compiled kernels；distributed process group 拥有 context-parallel collectives。Cache validity 不能由 artifact 文件自身完全证明。
- **Control Flow / Data Flow:** eager graph → Dynamo/Inductor capture/compile → cache artifacts save/load → guarded execution；CP 路径把 sequence/context 分片，经 supported SDPA backend 和 collective 形成结果。具体 backend 通信 schedule 需读对应实现/教程，release 本身未给统一算法。
- **Implementation Details:** Blackwell wheels绑定 CUDA 12.8，升级 cuDNN/NCCL/CUTLASS，带 Triton 3.3；Mega Cache 为 Beta；Blackwell、Native CP、FlexAttention inference 等为 Prototype。2.7 还迁移 manylinux_2_28/CXX11 ABI 等兼容边界。
- **Evaluation Setup:** release blog 没有统一 workload contract；各 feature 的性能数字/图若存在于 linked material，也不能组合成 framework-level benchmark。
- **Baselines / Ablations / Sensitivity:** `Not Applicable` 于 release aggregate；没有同一模型/硬件/shape 的统一 baseline、ablation 或 sensitivity。2.7.1 的回归清单反而证明 prototype/beta adoption 需要 correctness gate。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Blackwell 与 CUDA 12.8 compatibility 被披露；具体 GPU SKU、模型、precision、sequence length、batch、concurrency、SLO 对 aggregate release 均 `Not Disclosed`。
- **What the Evidence Actually Proves:** 2.7.0 提供这些版本化 API/支持等级，2.7.1 修复若干已知 correctness/performance regressions；它证明 framework surface 演进，不证明任一 workload 的净收益。
- **What It Does Not Prove:** 不证明 portable cache 可跨任意 driver/GPU/shape 复用、CP 对所有 topology 高效、FlexAttention 与专用 kernel 等价，或 prototype 已达到生产稳定性。
- **Limitations / Threats to Validity:** release-level evidence 混合 Beta/Prototype；兼容矩阵与后续 patch 会变化；缺少统一 benchmark contract；cache key/invalidations 与 distributed failure 语义需实现级验证。
- **Trade-offs / New Failure Modes:** 缓存减少 cold compile，却增加 graph/guard/compiler/driver identity 与 stale artifact 风险；op override 增加表达力也扩大 semantic divergence；CP 降低单卡 activation/attention 压力但引入 collective、topology 与 failure coupling。
- **Where the Previous Design Still Applies:** stable eager/compiled path、local cache、成熟 CUDA generation、短 context 或现有 parallel plan 已满足 SLO 时无需采用 prototype。
- **Evolution Relationship:** `Layering / Dependency`；framework 把硬件、compiler 与 distributed primitives 暴露给训练/推理系统，不直接改变模型算法结论。
- **ROADMAP Node:** Ch17、Ch32、Ch45；Ch32 拥有 communication/CP 原理，Ch17/45 只需版本 handoff。
- **Target and Adjacent Chapters Read:** Ch16–18、Ch31–33、Ch44–46 已读。
- **Existing Coverage:** Ch32 已从 communication collective、topology 和 parallel-dimension 推导 CP；Ch45/46 已强调 graph/kernel identity 与 backend contract。Mega Cache/Function Modes 是版本 API，未形成跨版本的新第一性原理。
- **Integration Decision:** `Weekly Only — Version/Product Fact`；单版本 compile/runtime 清单未形成独立长期机制。
- **Changed Files or Rejection Reason:** 不改 Books；后续稳定演进再按 artifact contract 联读。
- **Open Questions:** Mega Cache 的完整 compatibility key、跨 driver/arch invalidation、CP backend 的 topology sensitivity、2.7.1 之后仍存在的 silent correctness 风险。

### Kubernetes v1.33

- **Candidate / Week / Score:** Kubernetes v1.33 / 2025-W17 / 20/30。
- **Source Family ID:** `kubernetes-1.33-octarine`。
- **Source Type:** 官方 release blog、GitHub v1.33.0 release/changelog、KEP links；通用平台版本。
- **First-public Date / Revision History:** v1.33.0 发布于 2025-04-23；本周只记录 minor release，后续 patch releases 不反投影。
- **Direct Primary Sources:** Kubernetes v1.33 release blog；kubernetes/kubernetes v1.33.0 release notes/changelog。
- **Related Primary Sources:** KEP-753 sidecars、KEP-1287 in-place resize、KEP-4444/2433 traffic distribution、v1.33 DRA update；DRA 在 W35 另作为独立高分 family 审计。
- **Access and Verification Status:** Verified；64 KEP 的 release summary、stable/beta/alpha、deprecations/removals与 AI-relevant sections 已核对。并非 64 个 KEP 全部形成独立候选。
- **Full-read Coverage:** lifecycle、in-place resources、topology routing、CPU/SMT、affinity/spread、storage、HPA tolerance、CrashLoopBackOff、stop signal、DRA alpha additions、declarative validation、deprecations与 availability。
- **Original Problem:** 通用 orchestrator 需要在不破坏 API compatibility 的条件下逐步增强 workload lifecycle、resource mutation、placement、traffic 与 extensible device allocation。
- **Why the Previous Design Was Reasonable:** Pod replacement 保持 immutable-spec 简单语义；device plugins 和固定 resource names 易部署；alpha feature gates 限制未稳定 API 的 blast radius。
- **Changed Constraint:** stateful/long-running workloads希望不重启 resize，multi-zone traffic 需要 locality，GPU/NIC 等异构设备需要更丰富的 request/selection/taint/partition semantics。
- **Mechanism:** stable sidecar lifecycle；beta in-place Pod resource resize；GA topology-aware routing/trafficDistribution；placement refinements；alpha DRA device taints、prioritized alternatives 等。各 feature 有独立 KEP maturity，不应合并为“AI-native scheduler”。
- **State Ownership:** API server/controller 保存 desired state；scheduler/kubelet/CSI/DRA drivers 分别执行 placement、lifecycle与设备状态；业务级 training/serving controller 仍拥有 gang、checkpoint、model rollout 等语义。
- **Control Flow / Data Flow:** workload spec → admission/API storage → scheduler/device allocation → kubelet/container runtime；Service/EndpointSlice control path影响 traffic locality。每个 KEP 的 failure semantics不同。
- **Implementation Details:** v1.33 包含 18 stable、20 beta、24 alpha、2 deprecated/withdrawn enhancements；DRA additions仍是 alpha，不等于 GA。硬件 vendor driver行为不由 Kubernetes core release保证。
- **Evaluation Setup:** release notes不提供统一 AI workload benchmark；兼容与 conformance是版本发布语义，不是模型训练/推理性能实验。
- **Baselines / Ablations / Sensitivity:** `Not Applicable`；各 KEP有自己的 graduation evidence，本候选没有跨 feature ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** `Not Applicable / Not Disclosed`；这是 control-plane release，不包含模型、precision或服务 SLO contract。
- **What the Evidence Actually Proves:** v1.33 的 API/feature maturity与具体 version availability；DRA/resize/locality primitives扩大了上层 AI platform可组合能力。
- **What It Does Not Prove:** 不证明 Kubernetes 原生满足 gang scheduling、GPU topology optimization、model-aware routing、训练恢复或推理 SLO，也不证明 alpha DRA production-ready。
- **Limitations / Threats to Validity:** feature gates、driver adoption和 cloud-provider版本滞后；aggregate release掩盖不同 KEP maturity；迁移与 downgrade行为需集群级测试。
- **Trade-offs / New Failure Modes:** richer resource/lifecycle semantics减少重建，却增加 controller/driver version skew、partial update、admission和 rollback复杂度；topology preference可能与容量/公平性冲突。
- **Where the Previous Design Still Applies:** immutable replacement、extended resources/device plugin、显式 operator和外部 scheduler在简单或稳定集群仍合理；alpha DRA不是必然替代。
- **Evolution Relationship:** `Layering / Dependency`；Kubernetes primitive 是 AI platform substrate，不是 AI lifecycle control plane 本身。
- **ROADMAP Node:** Ch53–61；本 release 没有单一 Books owner，DRA family由 Ch59/W35审计。
- **Target and Adjacent Chapters Read:** Ch53–61 的章节边界及 Ch59–61 资源调度论点已读。
- **Existing Coverage:** Ch53 已区分通用 substrate 与 AI control plane，Ch59–61 已覆盖 device/topology/queue/gang语义；v1.33 aggregate没有新增需要跨版本沉淀的框架结论。
- **Integration Decision:** `Weekly Only — Version/Product Fact`。
- **Changed Files or Rejection Reason:** 不改 Books；版本功能不改变现有 platform/control-plane 结论。
- **Open Questions:** vendor DRA driver adoption、in-place resize 与 GPU memory/process semantics、alpha device taint/partition在失败与回滚下的行为。

### LUFFY — mixed-policy GRPO

- **Identity / date:** 2504.14945 v1，2025-04-21；后续至v5不改变owner week。
- **Problem → mechanism:** on-policy RLVR只能放大base已会行为，弱模型容易plateau；纯SFT又会僵化模仿。1条strong-policy off-policy trace与7条on-policy rollout进入同组advantage，Mixed-Policy GRPO用importance ratio校正，并以`x/(x+γ)`加重低概率关键token；policy、rollout、reward、verifier分别拥有状态。
- **Evaluation / boundary:** Qwen2.5-Math-7B为主，另含1.5B/Instruct/Llama3.1-8B、45K verified prompts、8 rollout、六个数学benchmark与γ ablation。证明该合同下能兼顾模仿和探索；不证明通用推理或生产稳定。
- **Trade-off / coexistence / owner:** teacher bias、off-policy mismatch、entropy collapse和额外采样；base足够强时on-policy仍合理。Owner `TRAIN-GRPO` Ch33/Legacy29；Ch32/34已读；Books Frozen — provisional Integrate。

### OTC-PO — tool-call productivity as a reward contract

- **Identity / date:** 2504.14870 v1，2025-04-21。
- **Problem → mechanism:** 只奖最终正确会诱发excessive tool calls；对每题/模型估计达到正确所需的最少调用数，在PPO/GRPO reward中联合correctness与tool-count deviation。轨迹保存调用计数、工具返回和verifier，policy决定内推还是外调。
- **Evidence boundary:** 在作者的Qwen/math/search-code合同下减少调用并保持accuracy；不证明最少调用等于最低端到端成本，也未覆盖工具失败/延迟分布。
- **Trade-off / owner:** reward misspecification可能压制必要探索；高不确定/外部事实任务仍需更多调用。Owner `AGENT-TOOL-CALLING` Ch78/Legacy74；Ch77/79已读；provisional Refine。

### Efficient Pretraining Length Scaling / PHD

- **Identity / date:** 2504.14992 v1，2025-04-21。
- **Mechanism:** original token提供全局KV，parallel hidden-decoding copies只作局部计算并立即丢弃；PHD-SWA保留O(1)局部cache，PHD-CSWA用chunk切断顺序依赖。persistent KV与ephemeral hidden KV分属不同生命周期。
- **Evaluation / boundary:** 151M级、100B-token curve、loss/downstream、prefill/decode/KV和SWA/CSWA变体。证明特定规模下length scaling可与部分cache/latency解耦；不证明大模型、长上下文或任意硬件。
- **Trade-off / owner:** 额外FLOPs、稀疏mask/kernel复杂度与局部状态丢失；无专用kernel时标准Transformer仍合理。Owner `MODEL-LONG-CONTEXT` Ch22；Ch21/23已读；provisional Integrate。

### Adaptive Parallel Reasoning

- **Identity / date:** 2504.15466 v1，2025-04-22。
- **Mechanism:** parent用`spawn()`创建有限context的并行children，`join()`只回传摘要后由parent合成；SGLang执行batching，SFT bootstrap后以端到端RL优化parent/child policy。
- **Evidence boundary:** Countdown等任务、4K/20K token和约5秒预算，比较sequential/SoS+/parallel并做context/temperature/compute ablation。只证明可分解任务内的learned allocation；不证明开放任务、共享工具状态或多Agent一致性。
- **Trade-off / owner:** error amplification、summary loss、spawn tax和取消/共享状态语义；小题或不可分题串行仍优。Owner `AGENT-WORKFLOW` Ch81/Legacy77；Ch80/82已读；provisional Integrate。

### FlowReasoner

- **Identity / date:** 2504.15257 v1，2025-04-21。
- **Mechanism / state:** 用可执行workflow承载reasoning control flow，生成、选择、执行、反馈形成闭环，终局reward塑造workflow policy；graph、节点产物与verifier是durable state，而非聊天文本。
- **Evidence boundary:** 在作者reasoning tasks和handcrafted/agent-search baselines下改善搜索组织；不证明任意工具环境可靠或workflow长期可复用。
- **Trade-off / owner:** graph bloat、错误传播、verifier overfit、执行成本；稳定SLO下固定流程更可审计。Owner `AGENT-WORKFLOW` Ch81；Ch79/80已读；provisional Refine。

### Eagle 2.5

- **Identity / date:** 2504.15271 v1，2025-04-21。
- **Mechanism:** vision encoder后进行长序列压缩和多尺度/时间建模，再与text token对齐；带时间与modality identity的visual representation是owner state。
- **Evidence boundary:** 报告的长视频、多图与视觉理解benchmark支持作者模型的扩展性；不证明通用streaming、实时latency或统一modality cache。
- **Trade-off / owner:** 压缩带来细节/时序丢失、位置漂移与训练成本；短图任务直接token仍简单。Owner `MULTIMODAL-REPRESENTATION` Ch23；Ch22/24已读；provisional Refine。

### TTRL

- **Identity / date:** 2504.16084 v1，2025-04-22。
- **Mechanism:** 同题多sample，以一致性/多数信号构造pseudo reward并在test time更新policy；model snapshot、rollout group与pseudo-label/confidence形成可变状态。
- **Evidence boundary:** 在答案可聚合、群体信号可靠的作者任务上可适配；不证明开放生成或高度相关错误下有效。
- **Trade-off / owner:** confirmation cascade、online drift、昂贵rollout和污染持久模型；低风险一次查询应只rerank不更新。Owner `TRAIN-GRPO` Ch33，handoff `AGENT-REFLECTION` Ch80；provisional Emerging。

### Tina

- **Identity / date:** 2504.15777 v1，2025-04-22。
- **Mechanism:** 冻结base，只对选定projection注入low-rank adapter；RL rollout/verifier只更新adapter，base artifact与adapter version分离。
- **Evidence boundary:** 数学reasoning下比较full FT、PEFT、rank和target modules，支持低秩更新可获得大部分作者测得收益；不证明所有模型/领域。
- **Trade-off / owner:** rank bottleneck、base-adapter coupling、merge/rollback和版本增殖；需结构性表征变化时full FT仍适用。Owner `TRAIN-LORA` Ch30/Legacy26；Ch29/31已读；provisional Refine。

### Skywork-R1V2

- **Identity / date:** 2504.16656 v1，2025-04-23。
- **Mechanism / evidence:** 公开base、math/code data、verifiable rewards与staged RL形成reasoning policy；rollout、reward、checkpoint分别版本化。作者benchmark只证明该recipe在列出的模型/任务有效，不证明产品推理或通用SOTA。
- **Trade-off / owner:** contamination、reward hacking、长输出成本；窄域可继续使用SFT或较小RL。Owner `TRAIN-GRPO` Ch33；Ch31/32已读；provisional Emerging。

### AIMO-2 Winning Solution

- **Identity / date:** 2504.16891 v1，2025-04-23。
- **Mechanism:** reasoning model与multi-sample、code execution、verifier、selection组成executable harness；weights、candidate traces、tool outputs和verdict必须分开归因。
- **Evidence boundary:** AIMO public/private competition证明model+harness组合；不等于模型单独能力或通用autonomy。
- **Trade-off / owner:** leakage、verifier blind spot与巨大inference budget；简单题单pass更经济。Owner `AGENT-TOOL-CALLING` Ch78，handoff `PLATFORM-EVALUATION-SYSTEM` Ch66 / `AGENT-PLANNING` Ch79；provisional Refine。

### ThinkPRM

- **Identity / date:** 2504.16828 v1，2025-04-23。
- **Mechanism:** evaluator对每个reasoning step生成检验/批判并聚合process score；verification trace与candidate solution分离，evaluator policy和evidence artifact是owner。
- **Evidence boundary:** 数学任务中比较PRM/outcome/self-consistency并做aggregation ablation；不证明judge校准、独立或适用于开放事实。
- **Trade-off / owner:** correlated error、verbosity bias、judge hacking、token成本；可执行verifier应优先。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66；Ch65/67已读；provisional Refine。

### Paper2Code

- **Identity / date:** 2504.17192 v1，2025-04-24。
- **Mechanism:** paper parsing、planning、code generation、execution/debug和artifact evaluation组成durable workflow；代码仓、环境、测试结果拥有状态，模型只提出变更。
- **Evidence boundary:** 论文重实现任务中优于单轮/无迭代baseline；不证明科学结果复现。
- **Trade-off / owner:** 环境漂移、测试不足、错误自动修补和依赖风险；小而明确实现仍可单轮。Owner `AGENT-WORKFLOW` Ch81；Ch78/83已读；provisional Integrate。

### Sparse Frontier

- **Identity / date:** 2504.17768 v1，2025-04-24。
- **Mechanism:** 按内容/层动态维护少量attention frontier，per-layer sparse index和selected KV取代完整pairwise matrix。
- **Evidence boundary:** long-context language/retrieval任务下提供quality–FLOPs/KV曲线；不证明任意kernel或distributed KV的wall-clock收益。
- **Trade-off / owner:** selection miss、索引维护和硬件不规则性；短context或高效dense kernel仍优。Owner `MODEL-LONG-CONTEXT` Ch22；Ch20/23已读；provisional Emerging。

### BitNet v2

- **Identity / date:** 2504.18415 v1，2025-04-25。
- **Mechanism:** 量化权重与activation/scale contract协同，训练保存高精度master/scale，执行走bit-linear kernel；quantized artifact、scale metadata和kernel compatibility共同定义identity。
- **Evidence boundary:** 作者模型的perplexity/downstream/memory/throughput支持特定实现；不证明通用GPU wall-clock、SLO或所有层同精度。
- **Trade-off / owner:** scale drift、outlier、unsupported ops和转换调试；BF16/INT8在生态优先时仍合理。Owner `INFER-TENSORRT-LLM` Ch49/Legacy45；Ch48/50已读；provisional Refine。

### Kimi-Audio

- **Identity / date:** 2504.18425 v1，2025-04-25。
- **Mechanism:** audio tokenizer/encoder将waveform变成时间化token，与language representation对齐；理解与生成decoder/codec分别读写，modality/timestamp/provenance identity贯穿数据流。
- **Evidence boundary:** 报告ASR、audio QA和speech generation任务支持统一模型；不证明实时full-duplex、生产latency或未公开内部机制。
- **Trade-off / owner:** token-rate/context inflation、codec artifact、语言/噪声偏差；专用ASR/TTS在低延迟窄任务仍优。Owner `MULTIMODAL-REPRESENTATION` Ch23；Ch22/24已读；provisional Integrate。

### Pleias-RAG
- **Identity / mechanism:** `2504.18225` v1，2025-04-25；350M/1B模型统一学习route/rewrite、rerank、literal quote与grounded answer，documents/quote spans/citation IDs属于external evidence state。
- **Evidence boundary:** HotPotQA、2Wiki与多欧洲语言支持该训练/检索合同，不证明quote蕴含claim、source可信或开放网页factuality。
- **Trade-off / owner:** synthetic bias与citation/retrieval成本；直接生成在事实需求低时仍合理。Owner `AGENT-RAG` Ch76；provisional Refine。

### PropRAG
- **Identity / mechanism:** `2504.18070` v1，2025-04-25；离线切context-rich propositions，在线以beam扩展/剪枝evidence paths；index/frontier/visited属于retriever state。
- **Evidence boundary:** 2Wiki/HotpotQA/MuSiQue Recall@5/F1支持该语料的multi-hop recall，不证明答案正确、freshness或大规模SLO。
- **Trade-off / owner:** extraction error、path explosion与失效成本；单跳仍用passage retrieval。Owner `AGENT-RAG` Ch76；provisional Integrate。

### OpenAI gpt-image-1 API
- **Identity / mechanism boundary:** official launch 2025-04-23；API支持generation/edit、quality/moderation与C2PA，内部模型/decoder未公开，固定为`Version Fact / Mechanism Not Disclosed`。
- **Evidence / trade-off / owner:** 只证明API surface与availability，不证明普适quality/latency；managed integration换vendor drift、policy与价格风险。Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24；Weekly Only。

### SGLang v0.4.6
- **Identity / mechanism:** GitHub tag `v0.4.6`，2025-04-27，commit `84022c0`；FA3、Mooncake/NIXL PD transfer、DeepGEMM/fusion与PD correctness fixes把prefill KV、transfer backend、decode buffer identity分离。
- **Evidence boundary:** release/PR只证明版本代码路径与修复，无统一model/hardware/length/concurrency/SLO benchmark。
- **Trade-off / owner:** backend matrix、version skew、timeout/cache identity；单机低并发仍简单。Owner `INFER-SGLANG` Ch51；provisional Refine。

### EasyEdit2
- **Identity / mechanism:** `2504.15133` v1，2025-04-21；从示例提取steering vector并在指定layer/activation注入，base只读，vector/layer/strength/scope构成versioned intervention artifact。
- **Evidence boundary:** 多行为任务支持统一steering framework，不证明因果、跨模型可移植或安全无旁路。
- **Trade-off / owner:** strength敏感、串扰与组合非交换；持久知识变化仍用SFT/edit。Owner `WORLDVIEW-REPRESENTATION` Ch5；provisional Refine。

### Kuwain 1.5B
- **Identity / mechanism:** `2504.15120` v1，2025-04-21；Arabic-heavy continual pretraining配原语言replay，base、mixture、corpus与checkpoint分开版本化。
- **Evidence boundary:** Arabic benchmarks支持该模型/比例的gain-retention点，不证明任意语言/tokenizer无损注入。
- **Trade-off / owner:** forgetting、mixture敏感与token fertility；资源足时joint pretraining仍合理。Owner `TRAIN-PRETRAINING` Ch28；No Change candidate。

### Trillion-7B
- **Identity / mechanism:** `2504.15431` v1，2025-04-21；tailored tokenizer、mixture与XLDA用aligned cross-lingual documents传递知识，document grouping/language ID/mixture是data state。
- **Evidence boundary:** 2T tokens、27 benchmarks、4 languages与59.4K H100 GPU-hours支持作者7B recipe，不证明XLDA单独贡献普适。
- **Trade-off / owner:** alignment构建、leakage与negative transfer；无parallel evidence仍用普通mixture。Owner `TRAIN-DATA` Ch27；provisional Integrate。

### VisuLogic
- **Identity / mechanism:** `2504.15279` v1，2025-04-21；1,000人工核验、六类视觉逻辑题及RL baseline，item/image/answer/category构成evaluation artifact。
- **Evidence boundary:** 多MLLM结果暴露vision-centric gap，不证明一般视觉智能、无污染或跨真实任务。
- **Trade-off / owner:** 小规模、category prior与静态泄漏；Owner `PLATFORM-EVALUATION-SYSTEM` Ch66；provisional Refine。

### Describe Anything Model
- **Identity / mechanism:** `2504.16072` v1，2025-04-22；focal prompt高分辨编码region，localized backbone融合局部/全局，DLC-SDP以半监督扩展。mask/track/time/provenance定义sample identity。
- **Evidence boundary:** image/video region benchmarks支持local-global fusion，不证明实时性、caption factuality或pseudo-label无偏。
- **Trade-off / owner:** token成本、tracking error与label amplification；粗粒度仍global caption。Owner `MULTIMODAL-REPRESENTATION` Ch23；provisional Refine。

### Bitter Lesson from 2,000+ Multilingual Benchmarks
- **Identity / mechanism:** `2504.15521` v1，2025-04-22；secondary audit覆盖2021–2024、148国、2,000+非英benchmarks，比较来源与human correlation。
- **Evidence boundary:** 支持translated-only coverage不足，不证明所有localized benchmarks更好或因果结论。
- **Trade-off / owner:** localization提高有效性但降低可比性并增加治理；Owner `PLATFORM-EVALUATION-SYSTEM` Ch66；provisional Refine。

### LiveCC
- **Identity / mechanism:** `2504.16030` v1，2025-04-22；按timestamp交织ASR words与frames，以Live-CC-5M预训练/Live-WhisperX SFT；stream cursor定义可见前缀。
- **Evidence boundary:** VideoMME/OVOBench/LiveSports支持作者7B setup，不证明真实latency、judge calibration或ASR鲁棒。
- **Trade-off / owner:** timestamp drift、ASR bias、token inflation与future leakage；offline caption仍适合非实时。Owner `MULTIMODAL-REPRESENTATION` Ch23，handoff `INFER-SCHEDULING` Ch56；provisional Integrate。

### WALL-E 2.0
- **Identity / mechanism:** `2504.15785` v1，2025-04-22；从trajectory抽action rules/KG/scene graph形成executable symbolic world model，以LLM做MPC look-ahead并循环更新规则。
- **Evidence boundary:** Mars/ALFWorld支持模拟环境中的alignment+MPC，不证明规则正确或现实物理/安全闭环。
- **Trade-off / owner:** brittle/stale rules与search cost；简单环境仍reactive/fixed rules。Owner `MULTIMODAL-WORLD-MODELS` Ch25，handoff `AGENT-PLANNING` Ch79；provisional Integrate。

### LLMs are Greedy Agents
- **Identity / mechanism:** `2504.16078` v1，2025-04-22；以self-generated CoT trajectories做RL并比较ε-greedy、自校正与self-consistency，policy/history/action/reward构成state。
- **Evidence boundary:** bandits/tic-tac-toe支持受控任务的exploration改善，不证明开放Agent或安全探索。
- **Trade-off / owner:** reward overfit、即时收益损失与trajectory cost；静态QA无需agentic RL。Owner `AGENT-PLANNING` Ch79；provisional Refine。

### ReflectionFlow
- **Identity / mechanism:** `2504.16080` v1，2025-04-22；noise/prompt/reflection三轴scaling，以GenRef训练FLUX执行generate→reflect→refine，image/version/reflection/seed构成迭代state。
- **Evidence boundary:** T2I tests支持作者model/benchmark中的refinement，不证明每轮单调、judge独立或跨diffusion普适。
- **Trade-off / owner:** 多轮compute、reflection bias、image drift与stop policy；简单prompt仍单次生成。Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24；provisional Refine。

### Vidi
- **Identity / mechanism:** `2504.15681` v1，2025-04-22；video/audio/text对齐后输出一个或多个time ranges，timestamp/query/range是first-class artifacts。
- **Evidence boundary:** VUE-TR支持hour-long temporal retrieval，不证明编辑正确、online latency或后续v3能力属于v1。
- **Trade-off / owner:** KV成本、A/V drift与range ambiguity；短片仍embedding retrieval。Owner `MULTIMODAL-REPRESENTATION` Ch23；provisional Refine。

### PHYBench
- **Identity / mechanism:** `2504.16074` v1，2025-04-22；500道原创physics problems及Expression Edit Distance evaluator。
- **Evidence boundary:** 对照AIME/GPQA等支持该static set的区分度，不证明general physical reasoning、实验能力或token scaling因果。
- **Trade-off / owner:** 泄漏、symbolic-equivalence blind spot；可执行simulator适用时更强。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66；provisional Refine。

### Full-Stack Safety Survey
- **Identity / mechanism:** `2504.15585` v1，2025-04-22；secondary synthesis以data→pretraining→post-training→deployment→commercialization组织800+ papers。
- **Evidence boundary:** 证明安全责任跨lifecycle，不把综述引用当primary replication或任一防御有效性。
- **Trade-off / owner:** taxonomy可能混合threat model/evidence；Owner `PLATFORM-SECURITY` Ch72；No Change。

### Pre-DPO
- **Identity / mechanism:** `2504.15843` v1，2025-04-22；先由同一preference data训练guiding reference，再用reference log-prob差调整正式DPO样本权重。
- **Evidence boundary:** AlpacaEval/Arena-Hard支持作者model/data，不证明human preference、任意β或judge无偏。
- **Trade-off / owner:** 额外checkpoint、double-use overfit与reference bias；高质量同分布pairs仍standard DPO。Owner `TRAIN-DPO` Ch34；provisional Refine。

### I-Con
- **Identity / mechanism:** `2504.16929` v1，2025-04-23；用supervisory conditional与representation-induced conditional间integrated KL统一多类representation losses。
- **Evidence boundary:** 理论连接23+方法及ImageNet案例支持统一重写，不证明optimization landscape/inductive bias等价或数字外推。
- **Trade-off / owner:** 统一视角可能隐藏estimator/normalization差异；Owner `WORLDVIEW-REPRESENTATION` Ch5；provisional Refine。

### QuaDMix
- **Identity / mechanism:** `2504.16511` v1，2025-04-23；quality/domain labels驱动参数化sampling，以小模型simulation+LightGBM搜索mixture后训练目标模型。
- **Evidence boundary:** 多data/model结果支持proxy-to-target合同，不证明ranking跨scale稳定或classifier无偏。
- **Trade-off / owner:** proxy mismatch、rare-domain suppression与搜索成本；明确小数据仍manual mixture。Owner `TRAIN-DATA` Ch27；provisional Refine。

### MMLA Benchmark
- **Identity / mechanism:** `2504.16427` v1，2025-04-23；61K+ utterances标注intent/emotion/dialogue act/style等human communication semantics。
- **Evidence boundary:** 8种LLM/MLLM branches支持该dataset中的gap，不证明真实用户状态、跨文化generalization或安全决策。
- **Trade-off / owner:** label subjectivity、privacy与domain shift；Owner `PLATFORM-EVALUATION-SYSTEM` Ch66；No Change。

### SAVA Tokenizer Adaptation
- **Identity / mechanism:** `2504.17025` v1，2025-04-23；用neural mapping把新Italian vocabulary对齐原embedding后做有限continual training，token map/embeddings/checkpoint共同定义artifact。
- **Evidence boundary:** Mistral/Llama Italian结果支持fertility-recovery路径，不证明所有语言或serving speed无损。
- **Trade-off / owner:** checkpoint/cache incompatibility与mapping error；多语共享时原tokenizer仍合理。Owner `MODEL-TOKENIZER` Ch11；provisional Refine。

### Zero-shot Subject-driven Video Generation
- **Identity / mechanism:** `2504.17816` v1，2025-04-23；把identity injection与motion preservation拆分并stochastic task switching，reference sampling/dropout抑制复制。
- **Evidence boundary:** 只采用v1可证内容；2026 v2/v3 compute与result不得反投W17。证明分解方向，不证明任意backbone。
- **Trade-off / owner:** identity-motion interference、forgetting与copy-paste；高价值subject仍可LoRA。Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24；provisional Integrate。

### Step1X-Edit
- **Identity / mechanism:** `2504.17761` v1，2025-04-24；MLLM读reference+instruction生成latent conditioning，再由diffusion decoder执行edit；reference/latent/seed/version定义transaction。
- **Evidence boundary:** GEdit-Bench支持该版本竞争性，不证明closed/open同机制、局部性或current repo等于event-time。
- **Trade-off / owner:** 双栈latency、identity drift、data/judge bias；简单局部编辑仍mask/ControlNet。Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24；provisional Refine。

### RefVNLI
- **Identity / mechanism:** `2504.17502` v1，2025-04-24；VNLI-style predictor联合评估reference subject、prompt与generated image。
- **Evidence boundary:** metric-human agreement只在训练/测试分布成立，不证明不可gaming或单score等于生成质量。
- **Trade-off / owner:** evaluator bias与两目标冲突；高风险仍分项+human review。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66；provisional Refine。

### UniME
- **Identity / mechanism:** `2504.17432` v1，2025-04-24；先从LLM teacher蒸馏text discriminative knowledge，再以hard-negative instruction tuning形成MLLM-derived embedding。
- **Evidence boundary:** MMEB与retrieval结果支持two-stage recipe，不证明一个embedding适合所有distance/SLO或后续v4结果属于v1。
- **Trade-off / owner:** teacher/mining成本、false negatives、index rebuild；简单ANN/短caption仍CLIP。Owner `MULTIMODAL-REPRESENTATION` Ch23，handoff `AGENT-RAG` Ch76；provisional Integrate。

### Anthropic Malicious-use Report
- **Identity / access / coverage:** `anthropic-malicious-use-2025-04`，官方报告 first-public 2025-04-24；已读报告正文、案例方法、检测与处置边界。它是厂商依据自身 abuse investigation 发布的 incident synthesis，不是独立攻击成功率实验。
- **Problem / old boundary / changed constraint:** 仅靠模型级拒答曾是合理起点，但 adversary 可把多轮账户、prompt、tool 与外部基础设施串成 campaign；约束从单次输出安全变成跨会话行为与 provenance 识别。
- **Mechanism / state / flow / implementation:** 平台把 account、conversation、artifact、时间与外部 indicator 作为 investigation state，按 detection→analyst review→enforcement/partner notification 流动；报告未披露完整 classifier、threshold、sampling 与误报矩阵。
- **Evaluation / evidence:** 案例证明被调查的具体滥用模式与处置事实，不证明总体发生率、检测召回率或对规避者的覆盖；硬件、模型精度、batch、concurrency 与 SLO 均 `Not Disclosed`。
- **Trade-offs / failure modes / coexistence:** 跨账户关联提升可见性，却引入 privacy、attribution error、selection bias 与不可审计阈值；模型拒答在低风险单轮场景仍必要但不充分。
- **Owner / disposition / open:** Owner `PLATFORM-SECURITY`（Ch72），邻接 Ch68/73；`Refine — Existing Argument` 仅为 provisional，Historical Books Gate 关闭。待验证 calibrated operating point、appeal/rollback 与第三方复现。

### APC Mental Imagery
- **Identity / access / coverage:** `2504.17207v1`，2025-04-24；已读 Method、训练实现、COMFORT++/3DSRBench evaluation、ablation 与 limitations。
- **Problem / mechanism:** 纯语言空间不显式保存物体的 3D 位置与朝向。APC 以 GroundingDINO/SAM 定位对象、DepthPro 恢复深度、Orient Anything 估计姿态，再把可控 scene representation 交给 Qwen2.5-VL-7B 推理；scene object、pose 与 reference frame 是状态 owner。
- **Control/data flow / implementation:** image→detect/segment→depth/orientation→结构化 spatial context→MLLM answer；作者报告 2×RTX 3090 训练，其他 batch/concurrency/SLO 未形成 serving contract。
- **Evaluation / evidence boundary:** COMFORT++、3DSRBench 与 component ablation 支持显式 3D cues 在这些 tasks 的收益；不证明真实机器人定位、遮挡下无误差或“mental imagery”是模型内部因果机制。
- **Trade-offs / old boundary:** 级联 detector/depth/orientation 会累积 calibration error 与 latency；简单 2D relation 或弱遮挡时端到端 VLM 更轻。
- **Owner / disposition:** Owner `MULTIMODAL-WORLD-MODELS`（Ch25），handoff `MULTIMODAL-REPRESENTATION`（Ch23）/`MULTIMODAL-EMBODIED-VLA`（Ch26）；`Emerging / Experimental`，不进 Books until gate。

### Token-Shuffle
- **Identity / access / coverage:** `2504.17789v1`，2025-04-24；已读 architecture、window shuffle/MLP、三阶段训练、baseline/ablation 与 limitations。
- **Problem / mechanism:** 高分辨率 AR image generation 的全局 token mixing 过贵，而固定 local window 又阻断跨窗依赖。Token-Shuffle 周期性重排 window membership，再以轻量 MLP 混合，使 2.7B 模型在局部计算预算下传播全局信息。
- **State / flow / implementation:** image tokens 按 layer/window permutation 改变邻接，attention/MLP 更新后再进入下一层；permutation schedule 与 positional identity 必须一致，否则 cache/layout 语义失配。
- **Evaluation / evidence:** 作者在公开 image-generation benchmarks 对比强 baseline 并做 shuffle/MLP ablation；结果只约束作者模型、分辨率与训练 recipe，硬件、online concurrency/SLO 不能外推。
- **Trade-offs / old boundary:** 重排降低 dense global attention 成本，却增加 layout bookkeeping、局部 artifact 与 kernel irregularity；低分辨率或质量优先 workload 仍可用 global attention。
- **Owner / disposition:** Owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `INFER-TENSORRT-LLM`（Ch49，execution-plan owner）；`Emerging / Experimental`。

### TimeChat-Online
- **Identity / access / coverage:** `2504.17343v1`，2025-04-24；已读 online architecture、DTD 数据、训练设置、baseline/ablation、limitations。
- **Problem / mechanism:** offline video QA 可偷看未来帧且 token 随时长增长。系统按时间游标只暴露到达帧，动态压缩历史 visual tokens，并在事件触发时回答。
- **State / flow / implementation:** 1 FPS frames→Qwen2.5-VL visual encoder→temporal token buffer/compression→online query/response；作者披露 64 frames、448 resolution、batch 128、8×A800，未披露生产并发与端到端 SLO。
- **Evaluation / evidence:** DTD 与 online benchmarks、token-reduction ablation 支持作者 setup 中的 streaming trade-off；不证明任意事件密度、摄像头延迟或真实多租户 serving。
- **Trade-offs / old boundary:** 压缩控制 KV/latency，却可能遗忘稀有早期证据并引入 trigger error；短视频或允许离线回看时全上下文仍更可靠。
- **Owner / disposition:** Owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `INFER-SCHEDULING`（Ch56）；`Refine — Existing Argument` provisional。

### DyMU
- **Identity / access / coverage:** `2504.17040v1`，2025-04-24；已读 DToMe、VTU、数据规模阈值构造、完整 evaluation、ablation 与 limitations。
- **Problem / mechanism:** 视频 MLLM 的相邻视觉 token 大量冗余，固定丢帧会损失事件。DToMe 按动态相似度合并 token，VTU 在层间更新被保留 token，使压缩与语义变化共同演进。
- **State / flow / implementation:** frame tokens→dynamic merge map→transformer layers→token update；merge assignment、position/time 与 surviving token identity 是 correctness state。阈值由约 25 万图像统计估计。
- **Evaluation / evidence:** 多 video benchmarks 与 DToMe/VTU ablation 支持作者模型上的精度-效率曲线；没有统一 production latency、batch/concurrency、GPU SKU 与 SLO 合同。
- **Trade-offs / old boundary:** 减少 token compute/KV，但错合并不可逆、阈值会 domain shift；短片、稀疏关键事件或充足预算时保留全 token 更合理。
- **Owner / disposition:** Owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `INFER-KV-CACHE`/Ch49；`Emerging / Experimental`。

### Code-grounded Math Evaluation
- **Identity / access / coverage:** `2504.17665v1`，2025-04-24；已读 evaluator pipeline、ASDiv/MATH500 setup、300-case manual audit、false-positive analysis 与 limitations。
- **Problem / mechanism:** string/exact-match 无法识别等价数学答案，也会接受碰巧匹配的错误推导。该 evaluator 把答案转为可执行 code/结构，再以 execution result 与结构约束判定。
- **State / flow / implementation:** model response→code/AST extraction→sandboxed execution→verdict+failure type；parser、runtime、timeout 与 environment version 构成 verifier identity。
- **Evaluation / evidence:** ASDiv、MATH500 与人工 300 样本审计说明 executable judging 可纠正部分 string-metric error；不证明所有数学语义可执行，也不证明 sandbox 安全或 judge 无偏。
- **Trade-offs / old boundary:** verifier 更精确但引入 code-generation/parser failure、资源预算与 attack surface；格式严格、答案唯一的任务仍可 exact match。
- **Owner / disposition:** Owner `PLATFORM-EVALUATION-SYSTEM`（Ch66）；`Refine — Existing Argument` provisional，需保留 verifier contract。

### Auto-SLURP
- **Identity / access / coverage:** `2504.18373v1`，2025-04-25；已读 benchmark construction、LangGraph/AutoGen harness、server simulation、error taxonomy、evaluation 与 limitations。
- **Problem / mechanism:** 静态 intent benchmark 只测分类，不测 Agent 是否在工具/API 约束下完成任务。Auto-SLURP 重标 SLURP 为 executable tasks，并把 planner、tool calls、server state 与 final outcome分离记录。
- **State / flow / implementation:** utterance→agent plan→tool/API calls→simulated service state→verifier；trace 与 environment snapshot 归 harness，而非模型权重。
- **Evaluation / evidence:** 多 framework/model 对比与 failure attribution 证明 harness 会显著改变 observed success；不证明模拟 server 等价真实系统，也不证明 framework 排名跨 prompt/tool schema 稳定。
- **Trade-offs / old boundary:** executable evaluation 更接近 workflow correctness，但成本更高且被环境实现污染；早期 intent regression 仍适合静态集。
- **Owner / disposition:** Owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `AGENT-WORKFLOW`（Ch81）；`Refine — Existing Argument` provisional。

### DRAGON Distributional Reward Optimization
- **Identity / access / coverage:** `2504.15217v1`，2025-04-21；已读 distributional objective、online generation、20 个 music reward functions、FAD/CLAP/Vendi 与 listening study；2025-11 v2/TMLR 只作 lineage。
- **Problem / mechanism:** 单一 scalar reward 把多维质量压成一个排序并导致 mode collapse。DRAGON 对 reward distribution 建模，在线从当前 policy 采样正负集合并优化相对分布，而非追逐固定 point target。
- **State / flow / implementation:** policy samples→reward-vector evaluation→positive/negative distribution sets→gradient update；reward family、sampling policy 与 current checkpoint 共同定义训练状态。
- **Evaluation / evidence:** music-generation baselines、diversity/quality metrics 与人工 listening 支持作者 workload；不证明 reward 维度无冲突、judge 无偏或可直接迁移语言模型 RL。
- **Trade-offs / old boundary:** 分布目标保留多样性，但增加 reward compute、sampling variance 与维度权重治理；目标明确且 reward 可靠时 scalar optimization 更简单。
- **Owner / disposition:** Owner `TRAIN-GRPO`（Ch33），handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）；`Emerging / Experimental`。

### Quicksviewer
- **Identity / access / coverage:** `2504.15270v1`，2025-04-21；已读 non-uniform cube sampler、3D resampler、progressive training、Video-MME evaluation 与 ablations。
- **Problem / mechanism:** uniform frame/token sampling 浪费预算于静态片段。Quicksviewer 用 Gumbel-Softmax 学习时空 cube density，再把每个 cube 重采样为固定 token 数，使预算随信息密度分配。
- **State / flow / implementation:** video→density predictor→non-uniform cubes→3D resampler→LLM tokens；cube boundaries、timestamps 与 sampling policy 决定 representation identity。训练分三阶段，作者报告约 0.8M samples。
- **Evaluation / evidence:** Video-MME 等 author tests 支持固定 token budget 下的精度收益；约 420 秒/1 FPS 等设置不等于实时 serving，GPU、batch/concurrency/SLO 不完整。
- **Trade-offs / old boundary:** 自适应采样节约 token，却可能漏掉短暂事件并增加不可规则 batching；均匀采样在短片或信息均匀时更稳。
- **Owner / disposition:** Owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `INFER-SCHEDULING`（Ch56）；`Emerging / Experimental`。

### RainbowPlus
- **Identity / access / coverage:** `2504.15047v1`，2025-04-21；已读 MAP-Elites archive、prompt mutation/diversity filter、六数据集/12模型、HarmBench、人评与 limitations。
- **Problem / mechanism:** 单一攻击搜索易集中于已知 prompt 模式。RainbowPlus 以人工定义行为维度维护 quality-diversity archive，循环 sample→mutate→filter→judge→archive update。
- **State / flow / implementation:** prompt population、archive cell、fitness 与 target response 构成 red-team state；作者实验使用 A40，但 batch/concurrency/production detection SLO 未披露。
- **Evaluation / evidence:** 对多模型与数据集的 attack-success/diversity 结果支持作者实现；不证明真实部署防御率，且原 Rainbow 为重实现，manual archive dimensions 带设计偏差。
- **Trade-offs / old boundary:** 更广覆盖换取更多 query/judge cost、archive bias 与 harmful artifact governance；已知 threat model 的确定性 regression suite 仍必要。
- **Owner / disposition:** Owner `PLATFORM-SECURITY`（Ch72），handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）；`Refine — Existing Argument` provisional。

### CRUST-Bench
- **Identity / access / coverage:** `2504.15254v1`，2025-04-21；已读 100 个 C repositories、3,085 interfaces、Rust wrapper/test construction、compiler/test/SWE-agent variants、coverage 与 limitations。
- **Problem / mechanism:** code generation benchmark 常只判编译或小函数，不测跨语言 ABI 与安全接口。CRUST-Bench 要求生成 safe Rust interface，再以 build、tests 与 coverage 逐层验证。
- **State / flow / implementation:** repo snapshot+C header→generated Rust→compiler→test harness→coverage/verdict；repository revision、toolchain 与 tests 是 evaluation identity。作者在 25 个项目测得平均约 67% coverage，全集平均约 958 LOC。
- **Evaluation / evidence:** single-shot 与 repair-agent baselines 显示 compiler/test feedback 改变成功率；不证明未覆盖路径安全、语义等价或 arbitrary C repo 可迁移。
- **Trade-offs / old boundary:** executable harness 更可信但昂贵、受 test adequacy/FFI undefined behavior 约束；小纯函数仍可用 unit tests。
- **Owner / disposition:** Owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `AGENT-WORKFLOW`（Ch81）；`Refine — Existing Argument` provisional。

### IV-Bench
- **Identity / access / coverage:** `2504.15415v1`，2025-04-22；已读 967 videos、2,585 image-text queries、13 tasks/5 categories、annotation QC、模型比较与 frame/resolution ablation。
- **Problem / mechanism:** video benchmarks 偏事件/动作，不能判断模型是否保留细粒度静态 visual evidence。IV-Bench 把 image-centric query 与 video context 对齐，显式测 object、attribute、text 与 spatial cues。
- **State / flow / implementation:** video/frames+query→model sampling policy→answer→task-specific score；frame count、resolution 与 sampling path 是 evaluation contract。
- **Evaluation / evidence:** 多模型最高分仍约 28.9，支持该集合对细粒度图像信息的区分度；不证明真实业务能力、无数据污染或低分根因只在 representation。
- **Trade-offs / old boundary:** 扩大静态证据覆盖但仍是 curated set，受 annotation/query priors 影响；动作理解 benchmark 仍是互补而非被替代。
- **Owner / disposition:** Owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `MULTIMODAL-REPRESENTATION`（Ch23）；`No Change — Already Covered` provisional。

### MR Video
- **Identity / access / coverage:** `2504.16082v1`，2025-04-22；已读 two-stage MapReduce、clip caption/entity normalization、query-time analysis、LVBench comparison 与 limitations。
- **Problem / mechanism:** 长视频不能整体塞进上下文，简单 uniform truncation 丢事件。第一阶段并行 map clips 并 reduce 成一致实体/时间摘要；第二阶段按 query map relevant summaries，再 reduce 成答案。
- **State / flow / implementation:** clip artifacts→global entity/timeline store→query-specific partial answers→final reducer；artifact version、time span、entity alias 与 provenance 必须可追踪。
- **Evaluation / evidence:** LVBench 等 author results 支持该 orchestration 在特定模型/分段设置的收益；不证明 summary 无损、并行线性扩展或 latency/成本满足生产 SLO。
- **Trade-offs / old boundary:** 并行降低 context pressure，却引入 summary drift、entity merge error 与 reducer bottleneck；短视频仍直接 end-to-end。
- **Owner / disposition:** Owner `AGENT-WORKFLOW`（Ch81），handoff `MULTIMODAL-REPRESENTATION`（Ch23）；`Emerging / Experimental`。

### RePOPE
- **Identity / access / coverage:** `2504.15707v1`，2025-04-22；已读 POPE/MSCOCO relabeling、class rebalance、model reranking、DASH-B comparison 与 limitations。
- **Problem / mechanism:** benchmark label noise 与 class imbalance 会把 metric 误差解释成 hallucination。RePOPE 重新核验 object labels、平衡 positive/negative，并重算 model ranking。
- **State / flow / implementation:** image+question→verified object annotation→answer normalization→confusion matrix；annotation version 与 sampling distribution 属于 evidence identity。
- **Evaluation / evidence:** 修订后 F1/排名变化证明原 benchmark 可扭曲结论；当模型超过约 90% 时饱和，不能证明通用事实性或 causal hallucination reduction。
- **Trade-offs / old boundary:** 清洗增强有效性但成本高、仍受 object ontology 限制；POPE 可作为快速 regression，需与 DASH-B/开放 claim verification 互补。
- **Owner / disposition:** Owner `PLATFORM-EVALUATION-SYSTEM`（Ch66）；`Refine — Existing Argument` provisional。

### ReDi Joint Image-Feature Diffusion
- **Identity / access / coverage:** `2504.16064v1`，2025-04-22；已读 joint denoising objective、VAE/DINOv2 branches、representation guidance、baselines/ablations；后续代码/revision 不反投本周。
- **Problem / mechanism:** 像素 latent diffusion 优化视觉保真但未必保存 discriminative semantics。ReDi 同时去噪 VAE image latents 与 DINOv2 feature latents，并用生成中的 feature branch 提供 guidance。
- **State / flow / implementation:** shared noise/time condition→two latent branches→joint loss→guided image denoising；feature extractor/version、latent scales 与 guidance weight 定义 artifact identity。
- **Evaluation / evidence:** author image-generation 与 representation metrics/ablations 支持双目标协同；不证明 feature semantics 等同世界模型、跨 backbone 稳定或 serving overhead 普适。
- **Trade-offs / old boundary:** semantic alignment 换来双分支训练/推理成本与 objective interference；纯视觉质量或 tight latency 下 standard diffusion 仍合理。
- **Owner / disposition:** Owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MULTIMODAL-REPRESENTATION`（Ch23）；`Emerging / Experimental`。

### DreamO
- **Identity / access / coverage:** `2504.16915v1`，2025-04-23；已读 uniform condition processing、routing constraint、placeholder binding、多阶段训练、qualitative/quantitative ablation 与 limitations。
- **Problem / mechanism:** subject、identity、style 与 composition 常需不同 adapter/pipeline。DreamO 把条件转为统一 token/feature interface，用 routing 约束和 placeholder position 把条件绑定到生成位置。
- **State / flow / implementation:** references/instruction→condition encoder→routed condition tokens→DiT denoising；reference identity、mask/position、seed 与 checkpoint 共同定义 generation transaction。
- **Evaluation / evidence:** customization/editing benchmarks 与 component ablation 支持作者 pipeline 的统一性；不证明内部 style model/data 无偏、所有条件组合可组合或 latency 优于专用方法。
- **Trade-offs / old boundary:** 统一接口减少系统碎片但增加 condition conflict、routing error 与训练数据要求；单 subject/单 task 仍可 LoRA/ControlNet。
- **Owner / disposition:** Owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）；`Emerging / Experimental`。

### DeGLA
- **Identity / access / coverage:** `2504.16801v1`，2025-04-23；已读 frozen/EMA teacher self-distillation、global alignment、local grounded contrast、2M negative captions、benchmarks/ablations 与 trade-off analysis。
- **Problem / mechanism:** global image-text contrast 对整体语义强，却忽略局部关系；只强化 local negatives 又可能损害 zero-shot transfer。DeGLA 用 teacher 保持 global geometry，同时以 grounded local contrast 纠正细粒度关系。
- **State / flow / implementation:** image/text→student embeddings；teacher target约束 global representation，negative captions 驱动 local relation separation；teacher/version/negative generator 是训练 provenance。
- **Evaluation / evidence:** VALSE、SugarCrepe、ARO 与 11 个 zero-shot datasets 支持作者模型上的 global-local balance；不证明 negatives 无生成偏差或所有 downstream task 同时受益。
- **Trade-offs / old boundary:** 增加 teacher compute、negative quality dependency 与双目标冲突；粗粒度 retrieval 仍可 standard contrastive learning。
- **Owner / disposition:** Owner `MULTIMODAL-REPRESENTATION`（Ch23）；`Refine — Existing Argument` provisional。

### Semantic Orders for Autoregressive Image Generation
- **Identity / access / coverage:** `2504.17069v1`，2025-04-23；已读 order prediction、content/location representation、distillation/fine-tuning、two-dataset evaluation 与 ablation。
- **Problem / mechanism:** raster order 是工程方便而非图像语义因果顺序。模型先预测 semantic content、location 与 generation order，再按该 order 自回归生成，使依赖更贴近 object/layout。
- **State / flow / implementation:** prompt→semantic units+locations+order→ordered token generation；order plan 与 spatial identity 必须在 decode/rollback 中保持一致。
- **Evaluation / evidence:** 作者在两个 datasets 报告相近训练成本与质量提升，且无需额外人工标注；不证明任意 scene 的最优 order、cache 友好性或端到端 wall-clock 优势。
- **Trade-offs / old boundary:** 更合语义但增加 planning error 与不规则 decode；小图、规则 layout 或高度优化 raster kernel 下固定顺序仍占优。
- **Owner / disposition:** Owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `INFER-SPECULATIVE-DECODING`；`Emerging / Experimental`。

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Blocked Evidence and Gate Ledger

- **CameraBench (`2504.15376v1`, 2025-04-22, 22/30):** arXiv identity、摘要、project/repository metadata 可核验，但 event-time PDF 过大且 HTML 正文不可取得；Method、camera-motion taxonomy、完整 baselines/ablation、hardware 与 limitations 未达到 full-read 标准。`Unverified / Blocked`；Owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `MULTIMODAL-REPRESENTATION`（Ch23）。可接受恢复材料：v1 PDF/HTML/TXT 或作者 manuscript。
- **Roll the Dice, but Look Before You Leap (`2504.15266v1`, 2025-04-21, 23/30):** 只能核验 identity、abstract 与 revision metadata；关键 look-ahead/sampling algorithm、state transition、baseline、ablation、compute budget 和 limitations 无法完整读取。`Unverified / Blocked`；provisional Owner `TRAIN-GRPO`（Ch33）。可接受恢复材料：v1 full text 或 official artifact 对应 commit。
- **RealisDance-DiT (`2504.14977v1`, 2025-04-21, 21/30):** 可核验 Wan2.1-based DiT、minimal modification、low-noise warmup 与 large-batch/small-iteration 的摘要事实，但正文、数据 provenance、完整 evaluation/ablation 与 failure cases 不可访问。`Unverified / Blocked`；provisional Owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MULTIMODAL-EMBODIED-VLA`（Ch26）。
- **All-Angles Bench (`2504.15280v1`, 2025-04-21, 20/30):** 可核验 2,100+ QA、90 scenes、6 tasks、27 MLLMs 的摘要级 identity；scene construction、annotation agreement、prompt/evaluator、contamination 与完整 results 无法读取。`Unverified / Blocked`；provisional Owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `MULTIMODAL-REPRESENTATION`（Ch23）。
- **Uni3C (`2504.14899v1`, 2025-04-21, 21/30):** 摘要/project summary 可核验 PCDController、monocular-depth point cloud、SMPL-X 与 frozen video backbone；event-time Method、training setup、baselines/ablation、sim/real boundary 与 limitations 不完整。`Unverified / Blocked`；provisional Owner `MULTIMODAL-EMBODIED-VLA`（Ch26），handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）。

Candidate Evidence Gate：`Not Passed`。80/80 scored owners 均有最终状态；61/66 retained owners strict complete，5/66 `Unverified / Blocked`，Review Pending 0；14/14低分闭合；Disputed 0。Discovery Replay 已闭合，blocked 写入恢复账本并允许 forward cursor 继续；Historical Books Gate保持关闭。

## Low-score Closure Ledger

- Anthropic Harms Framework（官方，2025-04-21，19）：来源与日期闭合；是 harm taxonomy/policy framework，不是技术机制或实验性系统结论。
- DianJin-R1（`2504.15716v1`，2025-04-22，18）、Preferred-MedLLM（`2504.18080v1`，2025-04-25，18）、MultiMind（`2504.18039v1`，2025-04-25，18）：均为窄金融、医疗或 Werewolf domain model case；来源与事件日期闭合，缺少改变通用 AI System 设计结论的证据。
- IberBench（`2504.16921v1`，2025-04-23，19）、VideoVista-CulturalLingo（`2504.17821v1`，2025-04-23，19）：领域 benchmark identity/date 闭合；适合保留评测覆盖事实，不建立新的机制 owner。
- Conversational Assistants for Heart Failure Patients（`2504.17753v1`，2025-04-24，16）：within-group user study 对比 neurosymbolic 与 ChatGPT，但样本和任务局限于 heart-failure food-salt assistant，不能外推为通用交互系统结论。
- Google Lyria 2 / Music AI Sandbox（官方，2025-04-24，19）：只保留产品版本事实；公开材料未披露可进入 Books 的实现机制。
- CAPTURe（`2504.15485v1`，19）：来源/日期与真实+合成遮挡计数任务可核验，但结论局限于四个 VLM 和窄视觉计数诊断，不建立新的通用机制 owner。
- IPBench（`2504.15524v1`，18）：双语、8类机制/20任务/16 LLM 的 benchmark identity 可核验；领域聚焦知识产权推理，缺少可迁移的 system mechanism。
- ViSMaP（`2504.15921v1`，19）：长视频无监督 summarization/meta-prompting 来源与日期闭合；主要是特定 pipeline/application evidence，不改变 token/state owner 结论。
- DiMeR（`2504.17670v1`，18）：diffusion mesh reconstruction identity 与 first-public date 闭合；属于窄 3D reconstruction workload，event-time evidence不足以形成长期跨系统结论。
- 3DV-TON（`2504.17414v1`，19）：3D virtual try-on family 与日期闭合；专用人体/服装生成案例，保留 archive，不提升为通用 multimodal mechanism。
- Dynamic Camera Poses（`2504.17788v1`，18）：dataset family 与日期闭合；主要提供 camera-motion 数据资产，不独立改变 world-model/生成系统 owner。

## Cross-Week Deduplication

- W16 spillback：RLVR limits、NodeRAG、MIG、multilingual reasoning、GenAI Act II、knowledge boundary、Thought Manipulation、video preference、uncertainty length bias、ToolRL、X-Teaming、ThoughtTerminator、UFO2、LeetCodeDataset、BookWorld，以及Gemini2.5 Flash、Meta FAIR、vLLM0.8.4、DeepSpeed0.16.7、Transformers4.51.3，均按v1/official date回拨，不在W17重复计分。
- PHYBench v2、Full-stack safety v2～v4、Step1X后续revision、UniME后续revision、subject-video 2026 revisions只记录lineage，不回投为W17证据。
- DRAGON 2025-11 revision/TMLR、ReDi 后续代码、Quicksviewer 后续修订均作为同一 Source Family lineage，不新增 W17 分数。
- 4月28日以后公开的 framework patch/release 路由 W18；SGLang v0.4.6 以 GitHub release timestamp 2025-04-27 归 W17。
- DeepMind MELODI publication只是2024 owner论文的related evidence，不计W17新分。

## Knowledge Tree Position

- Model/Training：LUFFY、OTC-PO、DRAGON、Pre-DPO、I-Con、QuaDMix 等 → `TRAIN-GRPO`、`TRAIN-DPO`、`WORLDVIEW-REPRESENTATION`、`TRAIN-DATA`。
- Multimodal：Quicksviewer、APC、Token-Shuffle、TimeChat-Online、DyMU、ReDi、DreamO、DeGLA、Semantic Orders 等 → Ch23～25，并向 Ch49/56 handoff runtime state。
- Evidence/Security：Anthropic report、RainbowPlus、CRUST-Bench、IV-Bench、RePOPE、Code-grounded evaluation、Auto-SLURP → Ch66/72。
- Agent Workflow：MR Video、Auto-SLURP → `AGENT-WORKFLOW`（Ch81）；分段 artifact/provenance 属于 workflow state，不归模型上下文 owner。
- PyTorch 2.7 → 第 17、32、45 章；Kubernetes v1.33 → 第 53～61 章（均为 Layering / Dependency）。

## Recommended Action

- 61 个 strict packet 保留 provisional disposition，等待年度 Historical Evidence Gate 后按 Stable Node owner 逐项复核；不能把 `Must Read` 或 20+ 自动解释为必须改 Books。
- 5 个 blocked family 暂时跳过并进入材料恢复清单；恢复全文前不得沿用摘要机制结论。
- PyTorch 2.7、Kubernetes v1.33 与 gpt-image-1 等版本事实留 Weekly；SGLang 只保留 versioned runtime evidence。

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

`Books Frozen — Historical Gate Closed`。整周 Discovery Replay 已闭合，但 5 个 retained family 仍 blocked；本轮只恢复 Weekly 证据。任何 provisional owner/disposition 都不表示 Books 已经吸收。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 将旧 2 项 baseline 扩展为 80 个唯一 Source Family，完成 61/66 retained strict reviews、5 个 blocked 恢复请求与 14/14 低分闭合。
- 纠正 SGLang v0.4.6 的 first-public date；补齐固定机构/工程 negative-evidence、event-date routing、revision lineage 与跨周去重。
- 本轮不修改Books、ROADMAP或DECISIONS。

## Open Questions

- CameraBench、Roll the Dice、RealisDance-DiT、All-Angles Bench 与 Uni3C 能否取得 event-time full text/artifact 并完成 strict review？
- 自适应视觉 token、semantic generation order 与 workflow MapReduce 的 identity/rollback contract 在真实 serving SLO 下如何测量？
- 已完成 packet 的 provisional Books owner 只能在年度 Historical Evidence Gate 通过后复核，当前不执行 Integration。

## Sources

- LUFFY — https://arxiv.org/abs/2504.14945（v1: 2025-04-21；Accessed: 2026-08-22）
- OTC-PO — https://arxiv.org/abs/2504.14870（v1: 2025-04-21；Accessed: 2026-08-22）
- Efficient Pretraining Length Scaling / PHD — https://arxiv.org/abs/2504.14992（v1: 2025-04-21；Accessed: 2026-08-22）
- Adaptive Parallel Reasoning — https://arxiv.org/abs/2504.15466（v1: 2025-04-22；Accessed: 2026-08-22）
- FlowReasoner — https://arxiv.org/abs/2504.15257（v1: 2025-04-21；Accessed: 2026-08-22）
- Eagle 2.5 — https://arxiv.org/abs/2504.15271（v1: 2025-04-21；Accessed: 2026-08-22）
- TTRL — https://arxiv.org/abs/2504.16084（v1: 2025-04-22；Accessed: 2026-08-22）
- Tina — https://arxiv.org/abs/2504.15777（v1: 2025-04-22；Accessed: 2026-08-22）
- Skywork-R1V2 — https://arxiv.org/abs/2504.16656（v1: 2025-04-23；Accessed: 2026-08-22）
- AIMO-2 Winning Solution — https://arxiv.org/abs/2504.16891（v1: 2025-04-23；Accessed: 2026-08-22）
- ThinkPRM — https://arxiv.org/abs/2504.16828（v1: 2025-04-23；Accessed: 2026-08-22）
- Paper2Code — https://arxiv.org/abs/2504.17192（v1: 2025-04-24；Accessed: 2026-08-22）
- Sparse Frontier — https://arxiv.org/abs/2504.17768（v1: 2025-04-24；Accessed: 2026-08-22）
- BitNet v2 — https://arxiv.org/abs/2504.18415（v1: 2025-04-25；Accessed: 2026-08-22）
- Kimi-Audio — https://arxiv.org/abs/2504.18425（v1: 2025-04-25；Accessed: 2026-08-22）
- Pleias-RAG — https://arxiv.org/abs/2504.18225（v1: 2025-04-25；Accessed: 2026-08-22）
- PropRAG — https://arxiv.org/abs/2504.18070（v1: 2025-04-25；Accessed: 2026-08-22）
- OpenAI gpt-image-1 API — https://openai.com/index/image-generation-api/（First Public: 2025-04-23；Accessed: 2026-08-22）
- Anthropic Harms Framework — https://www.anthropic.com/news/our-approach-to-understanding-and-addressing-ai-harms（First Public: 2025-04-21；Accessed: 2026-08-24）
- Anthropic malicious-use report — https://www.anthropic.com/news/detecting-and-countering-malicious-uses-of-claude-march-2025（First Public: 2025-04-23；Accessed: 2026-08-24）
- Google Lyria 2 / Music AI Sandbox — https://deepmind.google/blog/music-ai-sandbox-now-with-new-features-and-broader-access/（First Public: 2025-04-24；Accessed: 2026-08-24）
- SGLang v0.4.6 — https://github.com/sgl-project/sglang/releases/tag/v0.4.6（First Public: 2025-04-27；Accessed: 2026-08-24）
- EasyEdit2 — https://arxiv.org/abs/2504.15133（v1: 2025-04-21；Accessed: 2026-08-22）
- Kuwain 1.5B — https://arxiv.org/abs/2504.15120（v1: 2025-04-21；Accessed: 2026-08-22）
- Trillion-7B — https://arxiv.org/abs/2504.15431（v1: 2025-04-22；Accessed: 2026-08-22）
- VisuLogic — https://arxiv.org/abs/2504.15279（v1: 2025-04-21；Accessed: 2026-08-22）
- Describe Anything Model — https://arxiv.org/abs/2504.16072（v1: 2025-04-22；Accessed: 2026-08-22）
- Bitter Lesson from 2,000+ Multilingual Benchmarks — https://arxiv.org/abs/2504.15521（v1: 2025-04-22；Accessed: 2026-08-22）
- LiveCC — https://arxiv.org/abs/2504.16030（v1: 2025-04-22；Accessed: 2026-08-22）
- WALL-E 2.0 — https://arxiv.org/abs/2504.15785（v1: 2025-04-22；Accessed: 2026-08-22）
- LLMs are Greedy Agents — https://arxiv.org/abs/2504.16078（v1: 2025-04-22；Accessed: 2026-08-22）
- ReflectionFlow — https://arxiv.org/abs/2504.16080（v1: 2025-04-22；Accessed: 2026-08-22）
- Vidi — https://arxiv.org/abs/2504.15681（v1: 2025-04-22；Accessed: 2026-08-22）
- PHYBench — https://arxiv.org/abs/2504.16074（v1: 2025-04-22；Accessed: 2026-08-22）
- Full-Stack Safety Survey — https://arxiv.org/abs/2504.15585（v1: 2025-04-22；Accessed: 2026-08-22）
- Pre-DPO — https://arxiv.org/abs/2504.15843（v1: 2025-04-22；Accessed: 2026-08-22）
- I-Con — https://arxiv.org/abs/2504.16929（v1: 2025-04-23；Accessed: 2026-08-22）
- QuaDMix — https://arxiv.org/abs/2504.16511（v1: 2025-04-23；Accessed: 2026-08-22）
- MMLA Benchmark — https://arxiv.org/abs/2504.16427（v1: 2025-04-23；Accessed: 2026-08-22）
- SAVA Tokenizer Adaptation — https://arxiv.org/abs/2504.17025（v1: 2025-04-23；Accessed: 2026-08-22）
- Zero-shot Subject-driven Video Generation — https://arxiv.org/abs/2504.17816（v1: 2025-04-24；Accessed: 2026-08-22）
- Step1X-Edit — https://arxiv.org/abs/2504.17761（v1: 2025-04-24；Accessed: 2026-08-22）
- RefVNLI — https://arxiv.org/abs/2504.17502（v1: 2025-04-24；Accessed: 2026-08-22）
- UniME — https://arxiv.org/abs/2504.17432（v1: 2025-04-24；Accessed: 2026-08-22）
- CameraBench — https://arxiv.org/abs/2504.15376（v1: 2025-04-22；Unverified / Blocked: event-time full text unavailable）
- APC Mental Imagery — https://arxiv.org/abs/2504.17207（v1: 2025-04-24；Accessed: 2026-08-24）
- Token-Shuffle — https://arxiv.org/abs/2504.17789（v1: 2025-04-24；Accessed: 2026-08-24）
- TimeChat-Online — https://arxiv.org/abs/2504.17343（v1: 2025-04-24；Accessed: 2026-08-24）
- DyMU — https://arxiv.org/abs/2504.17040（v1: 2025-04-24；Accessed: 2026-08-24）
- Code-grounded math evaluation — https://arxiv.org/abs/2504.17665（v1: 2025-04-24；Accessed: 2026-08-24）
- Auto-SLURP — https://arxiv.org/abs/2504.18373（v1: 2025-04-25；Accessed: 2026-08-24）
- DRAGON — https://arxiv.org/abs/2504.15217（v1: 2025-04-21；Accessed: 2026-08-24）
- Quicksviewer — https://arxiv.org/abs/2504.15270（v1: 2025-04-21；Accessed: 2026-08-24）
- Roll the Dice, but Look Before You Leap — https://arxiv.org/abs/2504.15266（v1: 2025-04-21；Unverified / Blocked: abstract only）
- RainbowPlus — https://arxiv.org/abs/2504.15047（v1: 2025-04-21；Accessed: 2026-08-24）
- CRUST-Bench — https://arxiv.org/abs/2504.15254（v1: 2025-04-21；Accessed: 2026-08-24）
- IV-Bench — https://arxiv.org/abs/2504.15415（v1: 2025-04-22；Accessed: 2026-08-24）
- MR Video — https://arxiv.org/abs/2504.16082（v1: 2025-04-22；Accessed: 2026-08-24）
- RePOPE — https://arxiv.org/abs/2504.15707（v1: 2025-04-22；Accessed: 2026-08-24）
- ReDi — https://arxiv.org/abs/2504.16064（v1: 2025-04-22；Accessed: 2026-08-24）
- DreamO — https://arxiv.org/abs/2504.16915（v1: 2025-04-23；Accessed: 2026-08-24）
- DeGLA — https://arxiv.org/abs/2504.16801（v1: 2025-04-23；Accessed: 2026-08-24）
- Semantic Orders for Autoregressive Image Generation — https://arxiv.org/abs/2504.17069（v1: 2025-04-23；Accessed: 2026-08-24）
- RealisDance-DiT — https://arxiv.org/abs/2504.14977（v1: 2025-04-21；Unverified / Blocked: abstract only）
- All-Angles Bench — https://arxiv.org/abs/2504.15280（v1: 2025-04-21；Unverified / Blocked: abstract only）
- Uni3C — https://arxiv.org/abs/2504.14899（v1: 2025-04-21；Unverified / Blocked: abstract/project summary only）
- DianJin-R1 — https://arxiv.org/abs/2504.15716（v1: 2025-04-22；Source/date/rejection verified）
- IberBench — https://arxiv.org/abs/2504.16921（v1: 2025-04-23；Source/date/rejection verified）
- VideoVista-CulturalLingo — https://arxiv.org/abs/2504.17821（v1: 2025-04-23；Source/date/rejection verified）
- Conversational Assistants for Heart Failure Patients — https://arxiv.org/abs/2504.17753（v1: 2025-04-24；Source/date/rejection verified）
- Preferred-MedLLM — https://arxiv.org/abs/2504.18080（v1: 2025-04-25；Source/date/rejection verified）
- MultiMind — https://arxiv.org/abs/2504.18039（v1: 2025-04-25；Source/date/rejection verified）
- CAPTURe — https://arxiv.org/abs/2504.15485（v1: 2025-04-22；Source/date/rejection verified）
- IPBench — https://arxiv.org/abs/2504.15524（v1: 2025-04-22；Source/date/rejection verified）
- ViSMaP — https://arxiv.org/abs/2504.15921（v1: 2025-04-22；Source/date/rejection verified）
- DiMeR — https://arxiv.org/abs/2504.17670（v1: 2025-04-24；Source/date/rejection verified）
- 3DV-TON — https://arxiv.org/abs/2504.17414（v1: 2025-04-24；Source/date/rejection verified）
- Dynamic Camera Poses — https://arxiv.org/abs/2504.17788（v1: 2025-04-24；Source/date/rejection verified）
- PyTorch 2.7 — https://pytorch.org/blog/pytorch-2-7/（First Public: 2025-04-23；Accessed: 2026-07-31）
- PyTorch v2.7.0 release notes — https://github.com/pytorch/pytorch/releases/tag/v2.7.0（First Public: 2025-04-23；Accessed: 2026-07-31）
- PyTorch v2.7.1 fix release — https://github.com/pytorch/pytorch/releases/tag/v2.7.1（First Public: 2025-06-04；Accessed: 2026-07-31）
- Kubernetes v1.33 — https://kubernetes.io/blog/2025/04/23/kubernetes-v1-33-release/（First Public: 2025-04-23；Accessed: 2026-07-31）
- Kubernetes v1.33.0 release — https://github.com/kubernetes/kubernetes/releases/tag/v1.33.0（First Public: 2025-04-23；Accessed: 2026-07-31）
