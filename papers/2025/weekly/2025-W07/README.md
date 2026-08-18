# AI Research Weekly — 2025-W07

> Coverage Window: 2025-02-10～2025-02-16
> Research Mode: Retrospective Discovery and Evidence Rebuild
> Accessed: 2026-08-18
> Audit Status: Candidate Evidence Gate Passed — 73/73 scored; 51/51 `20+` Full Source Reviews; 22/22 low-score dispositions; 42/42 spillback owner families closed; 1 additional family moved to W06
> Historical Books Gate: Closed — Weekly only

## Executive Summary

本周首轮 discovery replay 已确认 31 项候选，其中 13 项达到 20 分并完成逐项 Full Source Review，18 项完成 identity、arXiv v1 / 官方发布日期、评分和拒绝边界核验。W08 look-ahead 随后发现 Hugging Face 2 月17～18日推荐页中另有 42 个 Source Family 的 arXiv v1 实际落在 2 月10～16日，另有 `Jailbreaking to Jailbreak` 应回拨 W06；这些候选不能按推荐日留在 W08。对 42 项逐项重评后，38 项达到 `20+` 并完成全文审计，4 项完成低分拒绝核验；整周最终为 73/73 scoring、51/51 高分 Full Source Review、22/22 低分 disposition，Candidate Evidence Gate 通过。新增的 MUDDFormer 不是按 Hugging Face 推荐日归档，而是按 arXiv v1 的 2025-02-13 归入本周，并保留 5 月 v2 与当前 repository 只作后续 revision evidence 的边界。

旧版 Books Integration 声明已撤回。本轮只修复 Weekly 证据体系；所有可吸收候选统一标记为 Books Pending，未修改 books/。

## Coverage Window and Limitations

- 事件以官方发布日期、GitHub Release 时间或 arXiv v1 时间归档；Hugging Face 推荐日不替代 first-public date。
- arXiv HTML/PDF 用于正文；Google Scholar、OpenAlex、DBLP、Semantic Scholar 与 Hugging Face 用于发现和去重；Crossref 只核对 metadata。
- 本周发现 CODESIM、UniCMs、Competitive Programming、APE、Hypencoder、Éclair、CAD-Editor 等 v1 早于 2025-02-10，已列入前周 spillback ledger，不在 W07 重复计分。
- 2 月17～18日推荐页恢复的 42 个 W07 owner family 已逐项闭合；另有 1 项归 W06。推荐日只承担 discovery 作用，不替代 arXiv v1 事件日期。
- 后续 revision 只用于核验演进和限制，不作为 W07 新事件；2026 revision 的新增实验不得反推为 2025 已知事实。
- 历史回填不补造 Daily。性能数字必须绑定作者披露条件；Not Disclosed 字段不做推断。

## 1. 模型与研究机构

按固定顺序复核 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- Google Research: Building AI for the pluralistic society（2025-02-13），保留为 18/30 的官方研究综述；没有公开新的 executable mechanism。
- 其余机构在本窗口未发现需要独立建档且无法由论文 Source Family 表达的高分官方事件。

## 2. 论文与学术来源

按 arXiv v1 日期重放 2025-02-10～2025-02-16，并用 discovery indexes 交叉去重。高分项目覆盖 training、inference、distributed runtime、security、agent data 与 multimodal data scaling；低分项目没有被静默删除，详见低分账本。

## 3. AI Infra 与工程项目

复核 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA 的 Release/RFC/重要 PR。

- 本窗口未发现达到 20 分且拥有独立长期机制证据的正式 Release；issue、修复讨论和预发布状态不作为 release event。
- vLLM 0.7.3、Transformers 4.49 等落在 W08，按正式发布日期归后周。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Online Scheduling for LLM Inference with KV Cache Constraints | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review; Books deferred |
| Native Sparse Attention | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review; Books deferred |
| Can 1B LLM Surpass 405B LLM? | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review; Books deferred |
| OREAL | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review; Books deferred |
| Matryoshka Quantization | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Full Source Review; Books deferred |
| Jakiro | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review; Books deferred |
| InSTA | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review; Books deferred |
| Hephaestus | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review; Books deferred |
| Scaling VLM Pre-training to 100B Data | 5 | 4 | 4 | 5 | 4 | 5 | 27/30 | Full Source Review; Books deferred |
| Auditing Prompt Caching | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Source Review; Books deferred |
| TransMLA | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full Source Review; Books deferred |
| Distillation Scaling Laws | 5 | 5 | 5 | 5 | 5 | 5 | 30/30 | Full Source Review; Books deferred |
| LASP-2 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Source Review; Books deferred |
| MUDDFormer | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Spillback Full Source Review; Books deferred |
| LLaDA / Large Language Diffusion Models | 5 | 5 | 4 | 5 | 5 | 5 | 29/30 | Spillback Full Source Review; Books deferred |
| The Danger of Overthinking | 5 | 4 | 4 | 5 | 4 | 4 | 26/30 | Spillback Full Source Review; Books deferred |
| Step-Video-T2V | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Spillback Full Source Review; Books deferred |
| Region-Adaptive Sampling | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Spillback Full Source Review; Books deferred |
| ZeroBench | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Spillback Full Source Review; Books deferred |
| MM-RLHF | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Spillback Full Source Review; Books deferred |
| ImageRAG | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Spillback Full Source Review; Books deferred |
| DarwinLM | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Spillback Full Source Review; Books deferred |
| FoNE | 4 | 3 | 3 | 5 | 4 | 3 | 22/30 | Spillback Full Source Review; Books deferred |
| Precise Parameter Localization for Textual Generation | 4 | 3 | 4 | 5 | 4 | 3 | 23/30 | Spillback Full Source Review; Books deferred |
| Selective Self-to-Supervised Fine-Tuning | 4 | 3 | 4 | 5 | 4 | 3 | 23/30 | Spillback Full Source Review; Books deferred |
| STMA | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Spillback Full Source Review; Books deferred |
| CRANE | 5 | 4 | 4 | 5 | 4 | 3 | 25/30 | Spillback Full Source Review; Books deferred |
| The Mirage of Model Editing | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Spillback Full Source Review; Books deferred |
| I Think, Therefore I Diffuse | 4 | 3 | 4 | 5 | 4 | 3 | 23/30 | Spillback Full Source Review; Books deferred |
| ReLearn | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Spillback Full Source Review; Books deferred |
| Knowledge Circuits for Continual Pre-Training | 4 | 3 | 3 | 5 | 5 | 4 | 24/30 | Spillback Full Source Review; Books deferred |
| IHEval | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Spillback Full Source Review; Books deferred |
| Talk Structurally, Act Hierarchically | 4 | 3 | 3 | 5 | 4 | 3 | 22/30 | Spillback Full Source Review; Books deferred |
| Dyve | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Spillback Full Source Review; Books deferred |
| CALM | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Spillback Full Source Review; Books deferred |
| SURGE | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Spillback Full Source Review; Books deferred |
| EQ-VAE | 5 | 4 | 4 | 5 | 4 | 3 | 25/30 | Spillback Full Source Review; Books deferred |
| Counterexample-Driven Conceptual Reasoning | 4 | 3 | 3 | 5 | 4 | 3 | 22/30 | Spillback Full Source Review; Books deferred |
| Diverse Inference and Verification | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Spillback Full Source Review; Books deferred |
| Better Embeddings with Coupled Adam | 5 | 5 | 4 | 5 | 5 | 3 | 27/30 | Spillback Full Source Review; Books deferred |
| Data Valuation for Instruction Fine-Tuning / NN-CIFT | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Spillback Full Source Review; Books deferred |
| Cluster and Predict Latent Patches / CAPI | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Spillback Full Source Review; Books deferred |
| small Models, BIG Impact | 4 | 3 | 4 | 5 | 4 | 2 | 22/30 | Spillback Full Source Review; Books deferred |
| Text-guided Sparse Voxel Pruning / TSP3D | 4 | 4 | 4 | 5 | 3 | 2 | 22/30 | Spillback Full Source Review; Books deferred |
| V2V-LLM | 4 | 3 | 3 | 5 | 4 | 2 | 21/30 | Spillback Full Source Review; Books deferred |
| MRS: Fast Sampler for Mean Reverting Diffusion | 5 | 4 | 4 | 5 | 3 | 2 | 23/30 | Spillback Full Source Review; Books deferred |
| CLaMP 3 | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Spillback Full Source Review; Books deferred |
| Memory, Benchmark & Robots / MIKASA | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Spillback Full Source Review; Books deferred |
| Cuckoo | 5 | 4 | 4 | 5 | 4 | 2 | 24/30 | Spillback Full Source Review; Books deferred |
| Show Me the Work | 4 | 4 | 5 | 5 | 4 | 2 | 24/30 | Spillback Full Source Review; Books deferred |
| Data-Efficient Atomic Property Pretraining | 5 | 4 | 5 | 5 | 4 | 3 | 26/30 | Spillback Full Source Review; Books deferred |
| We Can't Understand AI Using Our Existing Vocabulary | 3 | 3 | 2 | 4 | 3 | 3 | 18/30 | Low-score verified; position paper |
| AdaPTS | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Low-score verified |
| Agentic End-to-End Protein Design / VibeGen | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Low-score verified; narrow domain evidence |
| Ask in Any Modality survey | 3 | 3 | 4 | 4 | 3 | 2 | 19/30 | Low-score verified; survey only |
| Building AI for the pluralistic society | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Weekly only; mechanism not disclosed |
| ReasonFlux | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Low-score verified |
| EVEv2 | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score verified |
| Efficient-vDiT | 4 | 4 | 3 | 4 | 2 | 2 | 19/30 | Low-score verified |
| CodeI/O | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score verified |
| Demonstration Structure for Reasoning | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score verified |
| Goedel-Prover | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Low-score verified |
| Mask-Enhanced Autoregressive Prediction | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Low-score verified |
| Vision SAEs | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Low-score verified |
| BenchMAX | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Low-score verified |
| Continuous Concepts | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Low-score verified |
| WorldGUI | 3 | 3 | 4 | 4 | 3 | 2 | 19/30 | Low-score verified |
| DPO-Shift | 3 | 3 | 4 | 4 | 3 | 2 | 19/30 | Low-score verified |
| Next Block Prediction | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Low-score verified |
| EmbodiedBench | 3 | 3 | 4 | 4 | 3 | 2 | 19/30 | Low-score verified |
| Thai Reasoning Model Merge | 3 | 2 | 3 | 4 | 3 | 2 | 17/30 | Low-score verified |
| Predictive Red Teaming | 4 | 3 | 4 | 4 | 2 | 2 | 19/30 | Low-score verified |
| FailSafe Long-Context QA | 3 | 3 | 3 | 4 | 2 | 2 | 17/30 | Low-score verified |

### Spillback Recovery Ledger

以下账本记录 W08 look-ahead 恢复的 42 个 W07 owner family；38 项 `20+` 已完成 Full Source Review，
4 项完成低分 identity/date/score/rejection 核验，没有候选因原始低估而被静默省略。

| Candidate | arXiv / Primary ID | First-public | Review Status |
| --- | --- | --- | --- |
| MUDDFormer | 2502.12170 | 2025-02-13 | Full Review Complete |
| LLaDA | 2502.09992 | 2025-02-14 | Full Review Complete |
| The Danger of Overthinking | 2502.08235 | 2025-02-12 | Full Review Complete |
| Step-Video-T2V | 2502.10248 | 2025-02-14 | Full Review Complete |
| Region-Adaptive Sampling | 2502.10389 | 2025-02-14 | Full Review Complete |
| ZeroBench | 2502.09696 | 2025-02-13 | Full Review Complete |
| MM-RLHF | 2502.10391 | 2025-02-14 | Full Review Complete |
| ImageRAG | 2502.09411 | 2025-02-13 | Full Review Complete |
| DarwinLM | 2502.07780 | 2025-02-11 | Full Review Complete |
| FoNE | 2502.09741 | 2025-02-13 | Full Review Complete |
| Precise Parameter Localization | 2502.09935 | 2025-02-14 | Full Review Complete |
| Diverse Inference and Verification | 2502.09955 | 2025-02-14 | Full Review Complete |
| Selective Self-to-Supervised Fine-Tuning | 2502.08130 | 2025-02-12 | Full Review Complete |
| STMA | 2502.10177 | 2025-02-14 | Full Review Complete |
| CRANE | 2502.09061 | 2025-02-13 | Full Review Complete |
| The Mirage of Model Editing | 2502.11177 | 2025-02-16 | Full Review Complete |
| I Think, Therefore I Diffuse | 2502.10458 | 2025-02-14 | Full Review Complete |
| ReLearn | 2502.11190 | 2025-02-16 | Full Review Complete |
| Knowledge Circuits for Continual Pre-Training | 2502.11196 | 2025-02-16 | Full Review Complete |
| IHEval | 2502.08745 | 2025-02-12 | Full Review Complete |
| Talk Structurally, Act Hierarchically | 2502.11098 | 2025-02-16 | Full Review Complete |
| SURGE | 2502.11167 | 2025-02-16 | Full Review Complete |
| EQ-VAE | 2502.09509 | 2025-02-13 | Full Review Complete |
| Dyve | 2502.11157 | 2025-02-16 | Full Review Complete |
| Counterexample-Driven Conceptual Reasoning | 2502.10454 | 2025-02-12 | Full Review Complete |
| CALM | 2502.08820 | 2025-02-12 | Full Review Complete |
| Better Embeddings with Coupled Adam | 2502.08441 | 2025-02-12 | Full Review Complete |
| Data Valuation for Instruction Fine-Tuning | 2502.09969 | 2025-02-14 | Full Review Complete |
| Cluster and Predict Latent Patches | 2502.08769 | 2025-02-12 | Full Review Complete |
| We Can't Understand AI Using Our Existing Vocabulary | 2502.07586 | 2025-02-11 | Low-score verified |
| AdaPTS | 2502.10235 | 2025-02-14 | Low-score verified |
| Small Models, Big Impact | 2502.10140 | 2025-02-14 | Full Review Complete |
| Text-guided Sparse Voxel Pruning | 2502.10392 | 2025-02-14 | Full Review Complete |
| V2V-LLM | 2502.09980 | 2025-02-14 | Full Review Complete |
| Cluster-Aware Latent Diffusion / MRS | 2502.07856 | 2025-02-11 | Full Review Complete |
| CLaMP 3 | 2502.10362 | 2025-02-14 | Full Review Complete |
| Agentic End-to-End Protein Design | 2502.10173 | 2025-02-14 | Low-score verified |
| Ask in Any Modality survey | 2502.08826 | 2025-02-12 | Low-score verified |
| Memory, Benchmark & Robots | 2502.10550 | 2025-02-14 | Full Review Complete |
| Cuckoo | 2502.11275 | 2025-02-16 | Full Review Complete |
| Show Me the Work | 2502.09083 | 2025-02-13 | Full Review Complete |
| Data-Efficient Atomic Property Pretraining | 2502.11085 | 2025-02-16 | Full Review Complete |
| Jailbreaking to Jailbreak | 2502.09638 | 2025-02-09 | Moved to W06; not scored in W07 |

## Deep Analysis

### 1. Prompt caching：性能 identity 变成安全 identity

- **Why:** prefix reuse 原本只被视为减少 prefill 的性能优化，但共享命名空间使 latency 依赖其他用户历史。
- **Principle:** cache key 的内容相等不等于 authorization domain 相等；tenant/organization 必须进入 cache identity。
- **Mechanism:** 两账户 warm/probe 与统计假设检验可以区分 per-user、per-organization 和 global sharing。
- **Trade-off:** 更强隔离降低跨租户 hit rate，却减少 timing side channel，并让 policy 能被审计。
- **Connection:** INFER-KV-CACHE → PLATFORM-MULTI-TENANT → PLATFORM-SECURITY。
- **Evolution:** content-addressed reuse → tenant-scoped reuse → disclosure、audit 与 mitigation；不是简单关闭缓存。

### 2. LASP-2：通信拓扑必须服从状态代数

- **Why:** LASP-1 的 ring/P2P 对线性注意力的固定尺寸 memory state 仍形成串行依赖。
- **Principle:** 当跨 chunk 状态可结合且大小不随序列长度增长时，可先并行计算局部状态，再用 collective 重建前缀。
- **Mechanism:** local K^T V → single AllGather → causal prefix sum → local intra/inter output；hybrid 层复用对齐的 collective。
- **Trade-off:** 提升并行度和 overlap，但复制 gathered states、依赖 collective 稳定性，且 causal intra-chunk 仍有局部成本。
- **Connection:** MODEL-LONG-CONTEXT → TRAIN-DISTRIBUTED-TRAINING → TRAIN-TENSOR-PARALLEL。
- **Evolution:** ring state handoff → associative state exchange；二者是 topology/workload 条件分支。

### 3. Distillation Scaling Laws：teacher 不是免费的常量

- **Why:** “更强 teacher 总是更好”忽略 teacher 训练成本、student capacity gap 与 teacher 复用次数。
- **Principle:** 应把 teacher loss、student size、distillation tokens 与生命周期复用共同纳入 compute allocation。
- **Mechanism:** 通过多组 fixed/isoFLOP sweep 拟合 broken-power-law，再求已有 teacher 与新训练 teacher 两种最优解。
- **Trade-off:** 规划更可预测，但系数只在研究的 language-model regime 内成立，外推会产生新风险。
- **Connection:** WORLDVIEW-SCALING-LAW → TRAIN-PRETRAINING → PLATFORM-COST。
- **Evolution:** teacher-as-free distillation → teacher/student joint accounting → reusable model asset economics。

## Low-score Verification Ledger

| Candidate | First-public | Primary Source | Score | Final Disposition |
| --- | --- | --- | ---: | --- |
| Building AI for the pluralistic society | 2025-02-13 | https://research.google/blog/building-ai-for-the-pluralistic-society/ | 18/30 | Official synthesis; durable governance framing but no new executable system mechanism. |
| ReasonFlux | 2025-02-10 | https://arxiv.org/abs/2502.06772 | 19/30 | Interesting hierarchical thought templates; narrow math evidence and incomplete production contract. |
| EVEv2 | 2025-02-10 | https://arxiv.org/abs/2502.06788 | 19/30 | Encoder-free VLM baseline; primarily architecture/evaluation refinement. |
| Efficient-vDiT | 2025-02-10 | https://arxiv.org/abs/2502.06155 | 19/30 | Attention tiling is useful but video-specific and kernel conclusions are workload-bound. |
| CodeI/O | 2025-02-11 | https://arxiv.org/abs/2502.07316 | 19/30 | Reasoning-data construction recipe; no distinct AI-system ownership mechanism. |
| LLMs Learn Reasoning from Demonstration Structure | 2025-02-11 | https://arxiv.org/abs/2502.07374 | 19/30 | Data-efficiency evidence; later revisions and benchmark transfer require family-level review. |
| Goedel-Prover | 2025-02-11 | https://arxiv.org/abs/2502.07640 | 19/30 | Strong formal-proof data flywheel but domain-specific and v1/v3 claims differ. |
| Mask-Enhanced Autoregressive Prediction | 2025-02-11 | https://arxiv.org/abs/2502.07490 | 19/30 | Objective variant; v3 is a 2026 revision and v1 generalization remains limited. |
| Interpretable and Testable Vision Features via SAEs | 2025-02-10 | https://arxiv.org/abs/2502.06755 | 19/30 | Causal feature intervention is valuable; limited to frozen vision models/tasks. |
| BenchMAX | 2025-02-11 | https://arxiv.org/abs/2502.07346 | 18/30 | Multilingual evaluation asset; no new platform mechanism beyond coverage discipline. |
| LLM Pretraining with Continuous Concepts | 2025-02-12 | https://arxiv.org/abs/2502.08524 | 19/30 | Promising objective/representation branch, but limited scale and independent replication. |
| WorldGUI | 2025-02-12 | https://arxiv.org/abs/2502.08047 | 19/30 | Dynamic-start evaluation is useful; current latest revision materially post-dates v1. |
| DPO-Shift | 2025-02-11 | https://arxiv.org/abs/2502.07599 | 19/30 | Clear preference-loss trade-off, but a local objective variant rather than system redesign. |
| Next Block Prediction | 2025-02-11 | https://arxiv.org/abs/2502.07737 | 19/30 | Semi-AR video branch; reported speed is resolution/model specific. |
| EmbodiedBench | 2025-02-13 | https://arxiv.org/abs/2502.09560 | 19/30 | Useful simulated benchmark; no real-world evidence and mainly evaluation coverage. |
| Thai Reasoning via Model Merging | 2025-02-13 | https://arxiv.org/abs/2502.09056 | 17/30 | Open recipe with narrow language/domain scope; not a general lifecycle mechanism. |
| Predictive Red Teaming | 2025-02-10 | https://arxiv.org/abs/2502.06575 | 19/30 | Important safety framing, but predictive degradation remains task/policy dependent. |
| FailSafe Long-Context QA for Finance | 2025-02-10 | https://arxiv.org/abs/2502.06329 | 17/30 | Domain benchmark and perturbation set; not a new long-context mechanism. |

## Full Source Review

### Online Scheduling for LLM Inference with KV Cache Constraints

- **Candidate / Week / Score:** Online Scheduling for LLM Inference with KV Cache Constraints / 2025-W07 / 24/30.
- **Source Family ID:** `kv-constrained-online-llm-scheduling`.
- **Source Type:** arXiv author paper; theory and trace-driven simulation.
- **First-public Date / Revision History:** v1 2025-02-10; v2 2025-02-13; v3 withdrawn; latest v5 2026-01-15 used only to check revisions.
- **Direct Primary Sources:** https://arxiv.org/abs/2502.07115; https://arxiv.org/html/2502.07115.
- **Related Primary Sources:** Vidur and LMSYS-Chat-1M define the trace/simulator context; they do not prove the scheduling theorem.
- **Access and Verification Status:** Verified; theorem, algorithms, experiments and appendices were readable.
- **Full-read Coverage:** metadata/revisions, formulation, offline IP, impossibility result, MC-SF, proofs, synthetic/trace experiments, prediction error and discussion.
- **Original Problem:** online serving must jointly minimize flow time and preserve future KV feasibility while output length is unknown.
- **Why the Previous Design Was Reasonable:** FCFS/SJF are reasonable when service time is known, memory footprint is static or preemption is cheap.
- **Changed Constraint:** decode length is unknown and each generated token grows KV state; current free blocks no longer imply future feasibility.
- **Mechanism:** MC-SF retains active requests, orders admissions by predicted output length and checks future KV growth against memory capacity.
- **State Ownership:** single-worker scheduler owns waiting/active sets, predictions and memory budget; requests own prompt and generated-token state.
- **Control Flow / Data Flow:** arrival -> queue -> retain active set -> shortest predicted admission -> future-memory check -> one-token round -> release on completion.
- **Implementation Details:** non-preemptive unit-round model; per-round worst-case O(M^2); not a vLLM/SGLang implementation.
- **Evaluation Contract:** synthetic trials plus 10K LMSYS subset through Vidur for Llama-2-70B on 2xA100.
- **Baselines / Ablations / Sensitivity / Overhead:** offline optimum, FCFS and shortest-first variants; prediction-error sensitivity epsilon 0.2/0.5/0.8 and reserve study.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 2xA100; Llama-2-70B; simulator treats words as tokens; precision, TP details, real concurrency and TTFT/TPOT SLO not disclosed.
- **What the Evidence Actually Proves:** fully adversarial online scheduling lacks a workload-independent constant ratio; future-KV admission helps under paper assumptions.
- **What It Does Not Prove:** does not prove a production-optimal policy or cover distributed routing, prefix reuse, priorities and preemption cost.
- **Limitations / Threats to Validity:** prediction upper bounds and simplified token latency are central assumptions; live tail behavior was not measured.
- **Trade-offs / New Failure Modes:** conservative reserve reduces dead ends but lowers utilization; shortest-first risks starvation; prediction drift adds control cost.
- **Where the Previous Design Still Applies:** FCFS remains reasonable for narrow lengths, abundant memory or fairness-first service; offline batches can use global optimization.
- **Evolution Relationship:** Principle Reuse: current-capacity admission -> future-state feasibility invariant.
- **ROADMAP Node:** INFER-SCHEDULING (Ch56; legacy Ch52).
- **Target and Adjacent Chapters Read:** Read Ch45-47 and Ch54-56 to verify KV ownership, batching, memory and SLO handoffs.
- **Existing Coverage:** Books already discuss workload-aware scheduling; this Weekly only records the stronger future-feasibility evidence.
- **Integration Decision:** `Books Pending — Integration Deferred`.
- **Changed Files or Rejection Reason:** Weekly only; Historical Books Gate remains closed.
- **Open Questions:** multi-worker extension, calibrated length bounds, prefix-aware memory identity and fairness under tail SLO.

### Native Sparse Attention

- **Candidate / Week / Score:** Native Sparse Attention / 2025-W07 / 27/30.
- **Source Family ID:** `native-sparse-attention`.
- **Source Type:** arXiv author paper plus public kernel/model artifact.
- **First-public Date / Revision History:** v1 2025-02-16; later revisions remain the same Source Family.
- **Direct Primary Sources:** https://arxiv.org/abs/2502.11089; https://arxiv.org/html/2502.11089.
- **Related Primary Sources:** MiniMax-01 supplies the preceding linear-attention branch; later DSA work is a follow-on, not evidence for the v1 claim.
- **Access and Verification Status:** Verified; method, training design, kernels, experiments and appendices were readable.
- **Full-read Coverage:** metadata, sparse branches, selector/indexer, backward path, kernel mapping, pretraining/continued-training setup, ablations and limitations.
- **Original Problem:** dense attention remains quadratic, while post-hoc sparsification leaves the model unadapted and often maps poorly to GPU memory hierarchy.
- **Why the Previous Design Was Reasonable:** dense attention is exact and regular; sliding windows are simple and fast when long-range recall is not required.
- **Changed Constraint:** long-context training and serving require lower accessed KV volume without losing local or selected global evidence.
- **Mechanism:** combines compressed coarse tokens, fine-grained selected token blocks and a sliding window; sparsity is present during training and kernels align selection granularity with hardware.
- **State Ownership:** each layer owns compressed states, selected token indices and local window state; GQA heads share selection groups.
- **Control Flow / Data Flow:** Q/K/V -> compressed branch and selector scores -> top blocks -> local window -> branch outputs/gates -> attention output.
- **Implementation Details:** specialized forward/backward kernels avoid materializing dense attention; index selection and branch fusion are part of the model contract.
- **Evaluation Contract:** author pretraining and continued-training experiments over long contexts compare dense, sliding and sparse variants with kernel measurements.
- **Baselines / Ablations / Sensitivity / Overhead:** dense attention, sliding-window and other sparse schemes; branch/index ablations and context-length sensitivity.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** author GPU/model/length settings only; reported memory-volume and speed figures are not portable without kernel, topology and batch details.
- **What the Evidence Actually Proves:** training-native, hardware-aligned sparsity can preserve the tested quality while reducing accessed attention state in the disclosed settings.
- **What It Does Not Prove:** does not prove universal replacement of dense attention or portability across hardware and serving stacks.
- **Limitations / Threats to Validity:** selector misses become semantic failures; irregular load, kernel maintenance and checkpoint compatibility remain open.
- **Trade-offs / New Failure Modes:** less KV traffic and longer context in exchange for selection state, nonuniform work and specialized kernels.
- **Where the Previous Design Still Applies:** dense attention remains preferable for short contexts, exact recall, unsupported hardware or low engineering budget.
- **Evolution Relationship:** Direct Evolution: fixed local sparsity -> learned multi-branch sparsity trained with the model.
- **ROADMAP Node:** MODEL-LONG-CONTEXT (Ch22), handoff to INFER-KV-CACHE and INFER-TENSORRT-LLM.
- **Target and Adjacent Chapters Read:** Read Ch14-15, Ch22 and Ch45/49 to separate model sparsity from runtime paging.
- **Existing Coverage:** Books contain a provisional sparse-attention route; this Weekly preserves the v1 evidence boundary for later gate review.
- **Integration Decision:** `Books Pending — Integration Deferred`.
- **Changed Files or Rejection Reason:** Weekly only; no Books modification in this phase.
- **Open Questions:** selector recall telemetry, cross-hardware kernels, cache identity and failure recovery.

### Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling

- **Candidate / Week / Score:** Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling / 2025-W07 / 26/30.
- **Source Family ID:** `reward-aware-compute-optimal-tts`.
- **Source Type:** arXiv author paper and OpenR2 artifact.
- **First-public Date / Revision History:** v1 2025-02-10.
- **Direct Primary Sources:** https://arxiv.org/abs/2502.06703; https://arxiv.org/html/2502.06703.
- **Related Primary Sources:** OpenR2 is the experiment framework; compared PRMs and policy checkpoints define the measured contract.
- **Access and Verification Status:** Verified; HTML includes setup, algorithms, full result tables, cases and limitations.
- **Full-read Coverage:** metadata, formulation, BoN/beam/DVTS, reward-aware allocation, difficulty grouping, MATH-500/AIME24, PRM bias, FLOP comparison, appendices.
- **Original Problem:** extra inference compute is useful only if sampling/search policy and verifier fit the model and problem.
- **Why the Previous Design Was Reasonable:** fixed BoN or majority voting is simple, parallel and robust when verifier quality and problem difficulty are stable.
- **Changed Constraint:** policy families, PRMs and difficulty levels produce different returns and can make more search harmful.
- **Mechanism:** selects among BoN, beam and DVTS under budgets 4/16/64/256 using reward-aware strategy and absolute pass-rate difficulty bins.
- **State Ownership:** orchestrator owns budget and search policy; policy model owns proposals; PRM owns scores; answer aggregation owns final selection.
- **Control Flow / Data Flow:** prompt -> estimate difficulty -> choose policy/PRM/search/budget -> generate branches -> score/vote -> return answer.
- **Implementation Details:** OpenR2; beam width 4; temperature 0 for CoT and 0.7 otherwise; total generation cap 8192 tokens.
- **Evaluation Contract:** MATH-500 and AIME24; Llama3/Qwen2.5 policies 0.5B-72B and PRMs 1.5B-72B.
- **Baselines / Ablations / Sensitivity / Overhead:** CoT, majority vote, BoN, beam and DVTS; multiple scoring/voting rules and PRM families.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** hardware and concurrency not disclosed; budgets are sample counts, not a production latency/cost SLO.
- **What the Evidence Actually Proves:** best allocation is conditional on policy, verifier and difficulty; some small models beat larger baselines under the paper's extra-compute contract.
- **What It Does Not Prove:** headline size comparisons do not establish equal cost, latency, data or general capability.
- **Limitations / Threats to Validity:** two math benchmarks, imperfect PRMs and oracle-like difficulty estimation limit generalization.
- **Trade-offs / New Failure Modes:** more search can improve accuracy but multiplies tokens, verifier cost and correlated-error risk.
- **Where the Previous Design Still Applies:** single-pass or fixed BoN remains better when latency is strict, verifier is weak or tasks are easy.
- **Evolution Relationship:** Alternative Branch: model scaling -> inference-time search with verifier-aware allocation.
- **ROADMAP Node:** WORLDVIEW-SCALING-LAW and INFER-SCHEDULING.
- **Target and Adjacent Chapters Read:** Read Ch7, Ch20 and Ch56 to separate quality scaling from fleet scheduling.
- **Existing Coverage:** Books discuss test-time compute conceptually; this evidence adds conditional allocation rather than a new universal law.
- **Integration Decision:** `Books Pending — Integration Deferred`.
- **Changed Files or Rejection Reason:** Weekly only.
- **Open Questions:** online calibration, tail latency, verifier drift, budget fairness and cross-domain validity.

### Exploring the Limit of Outcome Reward for Learning Mathematical Reasoning (OREAL)

- **Candidate / Week / Score:** Exploring the Limit of Outcome Reward for Learning Mathematical Reasoning (OREAL) / 2025-W07 / 26/30.
- **Source Family ID:** `oreal-outcome-reward-rl`.
- **Source Type:** arXiv author paper plus released code/data/model.
- **First-public Date / Revision History:** v1 2025-02-10.
- **Direct Primary Sources:** https://arxiv.org/abs/2502.06781; https://arxiv.org/html/2502.06781.
- **Related Primary Sources:** Numina, MATH and AMC/AIME define training/evaluation data; Qwen2.5-72B-Instruct is also used as verifier.
- **Access and Verification Status:** Verified; theory, algorithm, training recipe, evaluation and appendices were readable.
- **Full-read Coverage:** KL-regularized derivation, positive BoN behavior cloning, negative reward shaping, token importance model, on-policy data, ablations and discussion.
- **Original Problem:** binary final-answer rewards are sparse and treat partially correct long reasoning trajectories as undifferentiated.
- **Why the Previous Design Was Reasonable:** outcome-only RL is cheap and objective when final answers are rule-checkable; SFT on good traces is stable.
- **Changed Constraint:** long CoT makes sparse reward credit assignment and positive/negative imbalance increasingly severe.
- **Mechanism:** pairs one correct and one incorrect rollout, reshapes negative rewards for gradient consistency and learns token-level importance weights from outcome labels.
- **State Ownership:** policy owns generation; verifier owns binary reward; token model owns importance weights; trainer owns sampling/filtering and updates.
- **Control Flow / Data Flow:** question -> 16 rollouts -> rule plus 72B verifier -> retain 0<p<0.8 -> pair positive/negative -> token weighting -> policy update.
- **Implementation Details:** on-policy loop initialized from SFT/RFT models; code/model/data released; exact production fault handling absent.
- **Evaluation Contract:** MATH-500 and related math sets with 7B/32B models; author reports pass@1 comparisons.
- **Baselines / Ablations / Sensitivity / Overhead:** SFT/RFT, outcome-reward RL and distilled reasoning models; component ablations for shaping and token weights.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** hardware, precision and full training-token/SLO contract not disclosed; 16 trajectories per question disclosed.
- **What the Evidence Actually Proves:** outcome feedback can support a more structured RL objective and the proposed components help in the tested math setting.
- **What It Does Not Prove:** does not prove general token credit assignment or superiority across open-ended tasks.
- **Limitations / Threats to Validity:** verifier errors, math-only rewards and selected-query filtering can bias the learned policy.
- **Trade-offs / New Failure Modes:** denser learning signal without step labels, but adds a learned reward component and verifier/model feedback loops.
- **Where the Previous Design Still Applies:** plain outcome RL remains attractive for short trajectories and reliable exact-match tasks.
- **Evolution Relationship:** Direct Evolution: terminal reward -> shaped pairwise outcome signal plus learned token importance.
- **ROADMAP Node:** TRAIN-RLHF / TRAIN-PPO / TRAIN-GRPO.
- **Target and Adjacent Chapters Read:** Read Ch31-33 and Ch66 to separate optimizer mechanics from evaluator evidence.
- **Existing Coverage:** Books already distinguish process and outcome rewards; final integration needs source-family comparison with later GRPO work.
- **Integration Decision:** `Books Pending — Integration Deferred`.
- **Changed Files or Rejection Reason:** Weekly only.
- **Open Questions:** reward-model calibration, verifier contamination, non-math transfer and stability at larger scale.

### Matryoshka Quantization

- **Candidate / Week / Score:** Matryoshka Quantization / 2025-W07 / 27/30.
- **Source Family ID:** `matryoshka-multiscale-quantization`.
- **Source Type:** arXiv author paper; OmniQuant/QAT experiments.
- **First-public Date / Revision History:** v1 2025-02-10; v2 2025-02-24; v3 2025-03-03.
- **Direct Primary Sources:** https://arxiv.org/abs/2502.06786; https://arxiv.org/html/2502.06786.
- **Related Primary Sources:** OmniQuant and QAT are base algorithms; Gemma-2 and Mistral checkpoints define model scope.
- **Access and Verification Status:** Verified; method, training details, ablations, errata and deployment discussion were readable.
- **Full-read Coverage:** nested integer representation, slicing, multi-scale loss, co-distillation, interpolation, mix-and-match, deployment and appendices.
- **Original Problem:** operators often maintain separate checkpoints for int8/int4/int2 quality-latency tiers.
- **Why the Previous Design Was Reasonable:** one quantized checkpoint per precision is easy to tune and validate because each objective is isolated.
- **Changed Constraint:** fleet heterogeneity and dynamic SLOs benefit from choosing precision without storing/retraining every variant.
- **Mechanism:** co-trains nested most-significant-bit slices at multiple precisions with weighted losses and optional co-distillation; supports sliced intermediate precisions.
- **State Ownership:** single master weight tensor owns nested bits; deployment policy chooses exposed precision; kernel owns packing/dequantization semantics.
- **Control Flow / Data Flow:** float weights -> joint multi-precision objective -> nested integer representation -> slice selected bits -> precision-specific kernel.
- **Implementation Details:** evaluated with OmniQuant and QAT; layerwise mix-and-match and extra-bit outlier representation are extensions.
- **Evaluation Contract:** Gemma-2 2B/9B and Mistral 7B; perplexity plus ARC/BoolQ/HellaSwag/PIQA/Winogrande.
- **Baselines / Ablations / Sensitivity / Overhead:** independently trained/sliced int8/int4/int2, OmniQuant and QAT; weightings, co-distillation and layer-mix ablations.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** hardware, serving batch/concurrency and kernel SLO not disclosed; accuracy deltas are model/task specific.
- **What the Evidence Actually Proves:** one trained representation can expose multiple tested bit-widths and improve low-bit slices relative to naive slicing.
- **What It Does Not Prove:** does not prove arbitrary runtime precision switching is free or that all kernels exploit the format efficiently.
- **Limitations / Threats to Validity:** joint objectives can compromise individual optima; deployment support and activation/KV quantization are separate.
- **Trade-offs / New Failure Modes:** fewer artifacts and flexible precision for more complex training, validation matrix and kernel compatibility.
- **Where the Previous Design Still Applies:** separate checkpoints remain better when one precision dominates or certification requires isolated artifacts.
- **Evolution Relationship:** Direct Evolution: fixed-precision artifact -> nested multi-precision artifact with deployment-time selection.
- **ROADMAP Node:** INFER-TENSORRT-LLM and PLATFORM-MODEL-REGISTRY.
- **Target and Adjacent Chapters Read:** Read Ch49, Ch54 and Ch59 to trace numeric format, memory and artifact identity.
- **Existing Coverage:** Books cover quantization trade-offs but not yet a final decision on multi-precision artifact ownership.
- **Integration Decision:** `Books Pending — Integration Deferred`.
- **Changed Files or Rejection Reason:** Weekly only.
- **Open Questions:** activation/KV extension, rollback identity, kernel support and per-tenant precision policy.

### Jakiro: Boosting Speculative Decoding with Decoupled Multi-Head via MoE

- **Candidate / Week / Score:** Jakiro: Boosting Speculative Decoding with Decoupled Multi-Head via MoE / 2025-W07 / 26/30.
- **Source Family ID:** `jakiro-decoupled-speculative-heads`.
- **Source Type:** arXiv author paper plus public code.
- **First-public Date / Revision History:** v1 2025-02-10.
- **Direct Primary Sources:** https://arxiv.org/abs/2502.06282; https://arxiv.org/html/2502.06282.
- **Related Primary Sources:** EAGLE/EAGLE-2, Medusa and Hydra define comparison branches.
- **Access and Verification Status:** Verified; architecture, training, speed/acceptance tables and appendices were readable.
- **Full-read Coverage:** draft-tree coupling diagnosis, MoE heads, hybrid AR/parallel proposal, contrastive feature training, MT-Bench/spec-bench evaluation.
- **Original Problem:** multiple draft heads derived from one representation produce correlated candidates and limited branch diversity.
- **Why the Previous Design Was Reasonable:** shared-head/tree drafting is compact and reduces draft overhead while target verification preserves exactness.
- **Changed Constraint:** acceptance length, not raw candidate count, becomes the bottleneck as draft capacity saturates.
- **Mechanism:** decouples same-step candidates through expert heads and uses initial autoregressive tokens followed by parallel drafting with contrastive feature separation.
- **State Ownership:** draft model owns expert routing and proposal tree; target model owns verification/commit; scheduler owns rollback and batch timing.
- **Control Flow / Data Flow:** target feature -> draft MoE heads -> hybrid proposal tree -> target parallel verify -> accept prefix -> rollback rejected suffix.
- **Implementation Details:** compares lossless speculative-sampling methods; public code; non-greedy methods with relaxed acceptance excluded.
- **Evaluation Contract:** Vicuna/Llama2-chat/Llama3-instruct on MT-Bench and related sets; four-run averages on A100-40G.
- **Baselines / Ablations / Sensitivity / Overhead:** standard speculative sampling, Medusa/Hydra context and EAGLE/EAGLE-2; acceptance-length and speed tables.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** A100-40G; named model families; precision, batch/concurrency and production SLO not fully disclosed.
- **What the Evidence Actually Proves:** candidate decoupling improves acceptance/speed in the tested single-GPU setup while target verification keeps distributional correctness.
- **What It Does Not Prove:** does not prove fleet-level throughput gain or benefit under large mixed batches and memory pressure.
- **Limitations / Threats to Validity:** extra experts and tree state add memory/kernel overhead; speed depends on target/draft balance.
- **Trade-offs / New Failure Modes:** more diverse proposals and acceptance for additional draft compute, routing state and rollback complexity.
- **Where the Previous Design Still Applies:** single-head or n-gram drafting remains simpler for small models, short outputs or low acceptance variance.
- **Evolution Relationship:** Direct Evolution: coupled multi-head proposal -> specialized decoupled proposal -> target-controlled commit.
- **ROADMAP Node:** INFER-SPECULATIVE-DECODING (Ch48).
- **Target and Adjacent Chapters Read:** Read Ch44-48 and Ch56 to verify decode, batching, commit and scheduler boundaries.
- **Existing Coverage:** Books already frame speculation as proposal/verify/commit; Jakiro is a constrained mechanism case.
- **Integration Decision:** `Books Pending — Integration Deferred`.
- **Changed Files or Rejection Reason:** Weekly only.
- **Open Questions:** batch interaction, expert placement, draft-cache identity and tail-latency break-even.

### InSTA: Towards Internet-Scale Training For Agents

- **Candidate / Week / Score:** InSTA: Towards Internet-Scale Training For Agents / 2025-W07 / 26/30.
- **Source Family ID:** `insta-agent-data-flywheel`.
- **Source Type:** arXiv author paper plus released dataset.
- **First-public Date / Revision History:** v1 2025-02-10; later v2 adds updated experiments.
- **Direct Primary Sources:** https://arxiv.org/abs/2502.06776; https://arxiv.org/html/2502.06776.
- **Related Primary Sources:** Mind2Web and WebLINX are supervised baselines; the released insta-150k-v2 dataset is the artifact.
- **Access and Verification Status:** Verified; pipeline, safeguards, training, capability analysis and extensive appendices were readable.
- **Full-read Coverage:** task proposer, agent rollout, judge, 150K-site crawl, 2.2M screenshots/actions, filtering, fine-tuning, safety and limitations.
- **Original Problem:** human-authored web-agent tasks and demonstrations do not scale with the changing internet.
- **Why the Previous Design Was Reasonable:** curated demonstrations are high-quality, legally clearer and easier to audit.
- **Changed Constraint:** site/task diversity and UI drift demand a data-generation loop that can produce and score trajectories at larger scale.
- **Mechanism:** LLM proposer annotates sites with tasks, an agent executes them, and a judge labels trajectories; accepted traces become training data.
- **State Ownership:** crawler owns site snapshot; proposer owns task hypothesis; executor owns action trace; judge owns evaluation label; curator owns dataset admission.
- **Control Flow / Data Flow:** site discovery -> task proposal -> safe filtering -> browser rollout -> screenshot/action trace -> judge reasoning -> dataset -> fine-tune/evaluate.
- **Implementation Details:** 150K sites, 150K trajectories, 2.2M screenshots and 2.2M action traces; appendix specifies Qwen3-1.7B fine-tuning and baselines.
- **Evaluation Contract:** fine-tuning and capability analysis against Mind2Web/WebLINX-style tasks with success/judge metrics.
- **Baselines / Ablations / Sensitivity / Overhead:** human/static datasets and alternate training sources; data-size and task-type analyses.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** browser fleet hardware, rollout concurrency, failure/retry SLO and full website policy contract not disclosed.
- **What the Evidence Actually Proves:** a proposer-executor-judge loop can generate a large auditable agent dataset and improve tested web-agent behavior.
- **What It Does Not Prove:** does not prove judge correctness, legal permission, safe live deployment or internet-wide generalization.
- **Limitations / Threats to Validity:** agents can affect websites/analytics, ingest harmful content and inherit judge/model bias.
- **Trade-offs / New Failure Modes:** scale and diversity for provenance, consent, contamination, evaluator bias and expensive replay.
- **Where the Previous Design Still Applies:** human curation remains preferable for high-risk domains, stable workflows and precise labels.
- **Evolution Relationship:** Direct Evolution: fixed demonstrations -> model-generated tasks and trajectories -> judged data flywheel.
- **ROADMAP Node:** TRAIN-DATA with AGENT-WORKFLOW handoff.
- **Target and Adjacent Chapters Read:** Read Ch27, Ch66 and Ch81-84 to separate data admission, evaluation and runtime execution.
- **Existing Coverage:** Books cover data provenance and workflow state; final integration must preserve the live-web safety boundary.
- **Integration Decision:** `Books Pending — Integration Deferred`.
- **Changed Files or Rejection Reason:** Weekly only.
- **Open Questions:** site consent, replay determinism, judge calibration, identity/versioning and deletion.

### Hephaestus: Improving Fundamental Agent Capabilities through Continual Pre-Training

- **Candidate / Week / Score:** Hephaestus: Improving Fundamental Agent Capabilities through Continual Pre-Training / 2025-W07 / 26/30.
- **Source Family ID:** `hephaestus-agent-pretraining-data`.
- **Source Type:** arXiv author paper plus data/model artifacts.
- **First-public Date / Revision History:** v1 2025-02-10.
- **Direct Primary Sources:** https://arxiv.org/abs/2502.06589; https://arxiv.org/html/2502.06589.
- **Related Primary Sources:** API-Bank/API-Pack and function-calling benchmarks define source/evaluation context.
- **Access and Verification Status:** Verified; data construction, scaling study, training setup, benchmarks and limitations were readable.
- **Full-read Coverage:** 103B corpus, 76,537 APIs, documentation/trajectory mixture, filtering, scaling law, continual pretraining, IFT, ablations and appendix.
- **Original Problem:** instruction tuning teaches output format but may not supply broad API knowledge and intrinsic multi-step tool reasoning.
- **Why the Previous Design Was Reasonable:** SFT on curated calls is cheap, controllable and effective when the API set is small and stable.
- **Changed Constraint:** large and changing tool ecosystems require both documentation knowledge and trajectory priors before instruction tuning.
- **Mechanism:** constructs Hephaestus-Forge from seed/retrieved agent data and general text, fits data-mixture scaling behavior, then continual-pretrains and instruction-tunes.
- **State Ownership:** corpus pipeline owns document/trajectory provenance; pretraining owns broad capability; IFT owns task formatting; runtime still owns real tool authorization.
- **Control Flow / Data Flow:** seed sources -> retrieval/filtering -> docs plus trajectories -> mixture selection -> continual pretraining -> IFT -> tool benchmark.
- **Implementation Details:** 103B agent-specific tokens, 76,537 APIs; TP8/PP2 pretraining and TP4/PP2 IFT.
- **Evaluation Contract:** agent/function-calling and general benchmarks with mixture/scale ablations.
- **Baselines / Ablations / Sensitivity / Overhead:** prompting and IFT-only agent models plus alternate data mixes.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Hephaestus-8B base: 128 A100-40G for 11.1 days; IFT: 16 A100-40G for 11.6 hours; serving SLO not disclosed.
- **What the Evidence Actually Proves:** broad agent-oriented pretraining data and mixture choice improve tested intrinsic tool capabilities beyond IFT-only baselines.
- **What It Does Not Prove:** does not prove safe tool execution, general APIs or production workflow reliability.
- **Limitations / Threats to Validity:** base-model pretraining data is undisclosed, complicating mixture attribution; benchmark/tool leakage remains possible.
- **Trade-offs / New Failure Modes:** broader tool priors for large data/compute cost, provenance burden and potential obsolete API knowledge.
- **Where the Previous Design Still Applies:** IFT-only remains rational for narrow, controlled and frequently changing private APIs.
- **Evolution Relationship:** Layering / Dependency: generic pretraining -> agent corpus continual pretraining -> instruction formatting -> runtime authorization.
- **ROADMAP Node:** TRAIN-DATA / TRAIN-PRETRAINING with AGENT-TOOL-CALLING handoff.
- **Target and Adjacent Chapters Read:** Read Ch27-29 and Ch78/84 to keep learned tool priors separate from execution policy.
- **Existing Coverage:** Books already separate model capability and runtime authority; this source strengthens the data-mixture branch.
- **Integration Decision:** `Books Pending — Integration Deferred`.
- **Changed Files or Rejection Reason:** Weekly only.
- **Open Questions:** data freshness, API deprecation, contamination, provenance and whether smaller targeted corpora dominate.

### Scaling Pre-training to One Hundred Billion Data for Vision Language Models

- **Candidate / Week / Score:** Scaling Pre-training to One Hundred Billion Data for Vision Language Models / 2025-W07 / 27/30.
- **Source Family ID:** `webli-100b-vlm-data-scaling`.
- **Source Type:** arXiv author paper; large-scale empirical study.
- **First-public Date / Revision History:** v1 2025-02-11; later v2 is post-window revision.
- **Direct Primary Sources:** https://arxiv.org/abs/2502.07617; https://arxiv.org/html/2502.07617.
- **Related Primary Sources:** WebLI subsets and benchmark papers define data/evaluation contracts.
- **Access and Verification Status:** Verified; dataset construction, training setup, scaling curves, inclusivity analyses and limitations were readable.
- **Full-read Coverage:** 1B/10B/100B subsets, filtering/rebalancing, contrastive VLM, Western/inclusive benchmarks, ablations and limitations.
- **Original Problem:** more web data may saturate common benchmarks while changing coverage of long-tail languages and cultures.
- **Why the Previous Design Was Reasonable:** smaller filtered English-heavy corpora are cheaper and optimize established benchmark distributions.
- **Changed Constraint:** multilingual/global deployment values tail coverage that average Western benchmarks under-measure.
- **Mechanism:** trains matched contrastive VLMs on nested WebLI scales and compares raw, quality-filtered and language-rebalanced mixtures.
- **State Ownership:** data pipeline owns sampling/filtering/language identity; trainer owns model scale; evaluation suite owns coverage claims.
- **Control Flow / Data Flow:** web image-text pairs -> sample/filter/rebalance -> contrastive pretraining -> Western and inclusivity evaluations.
- **Implementation Details:** WebLI-100B with 1%/10% nested subsets; ViT-H up to about 600M; 50% token dropping in some runs.
- **Evaluation Contract:** COCO/ImageNet-style tasks plus Crossmodal-3600, Dollar Street, GeoDE and related inclusivity sets.
- **Baselines / Ablations / Sensitivity / Overhead:** 1B/10B/100B, raw versus filtered/rebalanced data and OpenCLIP comparisons.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** accelerator hardware, precision and full compute/SLO not disclosed; model size capped at ViT-H.
- **What the Evidence Actually Proves:** returns can saturate on common benchmarks while long-tail cultural/language coverage still improves under this data source.
- **What It Does Not Prove:** does not prove 100B examples are compute-optimal or inclusivity is captured by the chosen benchmarks.
- **Limitations / Threats to Validity:** Crossmodal-3600 covers only 36 languages/3600 images; web-data bias and model-size cap constrain generalization.
- **Trade-offs / New Failure Modes:** tail coverage and diversity for vast compute, governance, filtering and diminishing average-benchmark returns.
- **Where the Previous Design Still Applies:** smaller high-quality corpora remain preferable for bounded domains, fixed languages and limited compute.
- **Evolution Relationship:** Direct Evolution: uniform scale-up -> coverage-aware data scaling and evaluation.
- **ROADMAP Node:** TRAIN-DATA with MULTIMODAL-REPRESENTATION and PLATFORM-EVALUATION-SYSTEM.
- **Target and Adjacent Chapters Read:** Read Ch23, Ch27-28 and Ch66 to separate representation, data and evaluation claims.
- **Existing Coverage:** Books cover data quality/coverage; source adds evidence that saturation is benchmark-distribution dependent.
- **Integration Decision:** `Books Pending — Integration Deferred`.
- **Changed Files or Rejection Reason:** Weekly only.
- **Open Questions:** compute-normalized optima, consent/dedup, tail-language quality and downstream generative transfer.

### Auditing Prompt Caching in Language Model APIs

- **Candidate / Week / Score:** Auditing Prompt Caching in Language Model APIs / 2025-W07 / 29/30.
- **Source Family ID:** `prompt-cache-timing-audit`.
- **Source Type:** arXiv author paper; black-box statistical API audit.
- **First-public Date / Revision History:** v1 2025-02-11; v2 2025-07-13.
- **Direct Primary Sources:** https://arxiv.org/abs/2502.07776; https://arxiv.org/html/2502.07776.
- **Related Primary Sources:** provider cache documentation and responsible-disclosure responses define policy changes.
- **Access and Verification Status:** Verified; threat model, hypothesis tests, provider audit, mitigations and appendices were readable.
- **Full-read Coverage:** cache levels, attacker model, p-values, 17-provider audit, timing controls, architecture leakage, mitigations and disclosure.
- **Original Problem:** shared prefix caches make response time depend on another request's history, creating a cross-user side channel.
- **Why the Previous Design Was Reasonable:** global sharing maximizes hit rate and amortizes prefill across tenants.
- **Changed Constraint:** multi-tenant APIs make cache identity a confidentiality boundary, not only a performance key.
- **Mechanism:** two accounts submit controlled prefixes; timing samples feed a valid statistical test for per-user, per-organization or global sharing.
- **State Ownership:** provider owns cache namespace/TTL; organization owns tenant boundary; auditor owns probes and inference; user owns prompt confidentiality.
- **Control Flow / Data Flow:** victim warms prefix -> attacker sends matched/control probes -> collect latency -> hypothesis test -> infer sharing level -> disclose.
- **Implementation Details:** audits run September-October 2024; 17 providers, caching detected in 8 and global sharing in 7; at least five providers changed behavior/docs.
- **Evaluation Contract:** real API timing experiments with control prompts and false-positive-calibrated p-values.
- **Baselines / Ablations / Sensitivity / Overhead:** null of no caching plus documented per-organization providers; sensitivity to latency noise and prompt lengths.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** provider models/hardware/internal cache algorithms mostly undisclosed; network timing and rate limits are part of the observed environment.
- **What the Evidence Actually Proves:** black-box timing can reveal cache-sharing policy in tested APIs and global namespaces create plausible prefix-membership leakage.
- **What It Does Not Prove:** does not demonstrate full prompt extraction at scale or prove current provider behavior after mitigations.
- **Limitations / Threats to Validity:** network noise, unknown TTL/eviction and provider changes affect reproducibility; extraction attacks remain expensive.
- **Trade-offs / New Failure Modes:** cross-tenant hit rate versus confidentiality, isolation, observability and disclosure.
- **Where the Previous Design Still Applies:** global sharing may be acceptable for public/common prefixes or trusted single-tenant deployments.
- **Evolution Relationship:** Direct Evolution: content-addressed reuse -> tenant-scoped cache identity and auditable policy.
- **ROADMAP Node:** INFER-KV-CACHE / PLATFORM-MULTI-TENANT / PLATFORM-SECURITY.
- **Target and Adjacent Chapters Read:** Read Ch45, Ch71-72 and Ch67-69 to connect cache state, isolation and evidence.
- **Existing Coverage:** Books discuss cache identity and tenancy; this is strong evidence for timing side channels and namespace ownership.
- **Integration Decision:** `Books Pending — Integration Deferred`.
- **Changed Files or Rejection Reason:** Weekly only.
- **Open Questions:** constant-time masking cost, TTL disclosure, organization boundaries and post-mitigation replication.

### TransMLA: Multi-Head Latent Attention Is All You Need

- **Candidate / Week / Score:** TransMLA: Multi-Head Latent Attention Is All You Need / 2025-W07 / 24/30.
- **Source Family ID:** `transmla-gqa-to-mla-migration`.
- **Source Type:** arXiv author paper plus public code and vLLM benchmark.
- **First-public Date / Revision History:** v1 2025-02-11; revisions through v5 2025-06-12.
- **Direct Primary Sources:** https://arxiv.org/abs/2502.07864; https://arxiv.org/html/2502.07864.
- **Related Primary Sources:** DeepSeek MLA/Absorb and MHA2MLA define architecture and baseline.
- **Access and Verification Status:** Verified; conversion derivation, PCA/rotation, fine-tuning, benchmarks and limitations were readable.
- **Full-read Coverage:** GQA/MLA expressiveness, RoRoPE/FreqFold, KV balancing, joint low-rank approximation, training recovery, vLLM benchmark and appendix.
- **Original Problem:** existing GQA checkpoints cannot benefit from MLA cache compression without retraining or lossy conversion.
- **Why the Previous Design Was Reasonable:** keeping GQA preserves checkpoint compatibility, mature kernels and known quality.
- **Changed Constraint:** KV traffic dominates long-context serving and existing model investment makes from-scratch MLA training costly.
- **Mechanism:** rotates/folds positional key components, balances key/value norms, jointly low-rank approximates NoPE keys and values, then fine-tunes converted model.
- **State Ownership:** converted checkpoint owns projections and positional transformation; runtime owns Absorb-compatible kernels and compressed KV layout.
- **Control Flow / Data Flow:** collect calibration activations -> rotate RoPE key space -> KV norm balance -> PCA factorization -> fine-tune -> MLA-compatible serve.
- **Implementation Details:** converts SmolLM-1.7B and Llama2-7B; evaluates compression stages and vLLM integration.
- **Evaluation Contract:** six quality benchmarks before/after conversion/recovery plus 8K-context serving benchmark.
- **Baselines / Ablations / Sensitivity / Overhead:** original GQA and MHA2MLA; compression/training-token and key/value balancing analyses.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** reported 93% KV reduction and 10.6x speedup bind to Llama2-7B/8K and paper vLLM setup; hardware/concurrency details incomplete.
- **What the Evidence Actually Proves:** a calibrated conversion can recover much of tested quality while changing KV representation.
- **What It Does Not Prove:** does not prove migration is lossless, architecture-universal or faster under all batches/hardware.
- **Limitations / Threats to Validity:** calibration distribution, positional approximation and recovery tokens are new dependencies.
- **Trade-offs / New Failure Modes:** reuse checkpoint investment and reduce KV for conversion complexity, retraining and kernel lock-in.
- **Where the Previous Design Still Applies:** native GQA remains preferable for short contexts, unsupported runtimes and strict checkpoint fidelity.
- **Evolution Relationship:** Alternative Branch: retrain native MLA versus migrate GQA checkpoint with calibrated low-rank transformation.
- **ROADMAP Node:** MODEL-MULTI-HEAD-ATTENTION / INFER-KV-CACHE.
- **Target and Adjacent Chapters Read:** Read Ch15, Ch19, Ch45 and Ch49 to separate representation from execution.
- **Existing Coverage:** Books cover MLA and KV compression; this source is a migration case, not a universal architecture verdict.
- **Integration Decision:** `Books Pending — Integration Deferred`.
- **Changed Files or Rejection Reason:** Weekly only.
- **Open Questions:** calibration drift, fine-tuning budget, quantization interaction and serving break-even.

### Distillation Scaling Laws

- **Candidate / Week / Score:** Distillation Scaling Laws / 2025-W07 / 30/30.
- **Source Family ID:** `distillation-compute-allocation-laws`.
- **Source Type:** arXiv author paper; large controlled scaling study.
- **First-public Date / Revision History:** v1 2025-02-12; v2 2025-07-25.
- **Direct Primary Sources:** https://arxiv.org/abs/2502.08606; https://arxiv.org/html/2502.08606.
- **Related Primary Sources:** teacher/student checkpoints and language-modeling datasets define the fitted regime.
- **Access and Verification Status:** Verified; derivation, three experiment protocols, extrapolation, compute optima, theory and appendices were readable.
- **Full-read Coverage:** background, loss law, 143M-12.6B models, fixed/isoFLOP protocols, capacity gap, compute allocation, kernel-regression explanation and limitations.
- **Original Problem:** distillation budget must be split between teacher quality, student size and student tokens; a stronger teacher is not always better.
- **Why the Previous Design Was Reasonable:** choose the strongest available teacher and train the student as long as budget allows is simple and often effective.
- **Changed Constraint:** teacher creation cost and student capacity gap matter when optimizing total compute or serving many students.
- **Mechanism:** fits a broken-power-law student loss from teacher loss, student size and distillation tokens, then solves compute-optimal allocations for existing/new teacher cases.
- **State Ownership:** planner owns total compute; teacher training owns teacher loss; student training owns capacity/tokens; evaluator owns loss measurement.
- **Control Flow / Data Flow:** choose teacher/student regime -> run fixed/isoFLOP sweeps -> fit coefficients -> predict loss -> allocate teacher/student compute.
- **Implementation Details:** decoder models 143M-12.6B, MHA, Pre-RMSNorm, RoPE, sequence length 4096 and muP-style hyperparameter transfer.
- **Evaluation Contract:** three complementary sweep protocols with held-out extrapolation and capacity-gap analysis.
- **Baselines / Ablations / Sensitivity / Overhead:** supervised learning, existing-teacher distillation and jointly trained teacher/student allocations.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** language-model loss only; hardware and wall-clock/SLO not disclosed; teacher/student data are non-repeated by design.
- **What the Evidence Actually Proves:** within the studied regime, returns follow a fitted law and optimal allocation differs sharply between reusable and one-off teachers.
- **What It Does Not Prove:** does not prove the same coefficients for modalities, tasks, architectures or post-training.
- **Limitations / Threats to Validity:** language modeling only, finite model range, idealized FLOP accounting and fitted functional form.
- **Trade-offs / New Failure Modes:** predictable planning and reusable teachers for calibration experiments and risk of extrapolation beyond the fitted regime.
- **Where the Previous Design Still Applies:** supervised learning remains preferable for one student when its teacher must also be trained under the studied budgets.
- **Evolution Relationship:** Direct Evolution: teacher-is-free assumption -> explicit teacher/student lifecycle accounting.
- **ROADMAP Node:** WORLDVIEW-SCALING-LAW / TRAIN-PRETRAINING.
- **Target and Adjacent Chapters Read:** Read Ch7, Ch28 and Ch70 to connect empirical law, training choice and cost accounting.
- **Existing Coverage:** Books cover compute/data scaling; this source introduces teacher reuse as an asset-lifecycle variable.
- **Integration Decision:** `Books Pending — Integration Deferred`.
- **Changed Files or Rejection Reason:** Weekly only.
- **Open Questions:** post-training transfer, multi-modal coefficients, teacher amortization horizon and data-rights accounting.

### LASP-2: Rethinking Sequence Parallelism for Linear Attention and Its Hybrid

- **Candidate / Week / Score:** LASP-2: Rethinking Sequence Parallelism for Linear Attention and Its Hybrid / 2025-W07 / 29/30.
- **Source Family ID:** `lasp2-linear-attention-sequence-parallelism`.
- **Source Type:** arXiv author paper plus Linear-MoE code.
- **First-public Date / Revision History:** v1 2025-02-11.
- **Direct Primary Sources:** https://arxiv.org/abs/2502.07563; https://arxiv.org/html/2502.07563.
- **Related Primary Sources:** LASP-1, Ring Attention and Linear-Llama3 define prior system/architecture branches.
- **Access and Verification Status:** Verified; equations, forward/backward algorithms, cost model, experiments and compatibility appendices were readable.
- **Full-read Coverage:** linear recurrent state, masked/unmasked algorithms, AllGather workflow, LASP-2H, theoretical cost, 2M context experiments, convergence and ablations.
- **Original Problem:** ring/P2P sequence parallelism serializes transfer of recurrent memory states and fragments communication overlap.
- **Why the Previous Design Was Reasonable:** ring exchange bounds per-link traffic and is natural when each sequence chunk depends on the prior chunk.
- **Changed Constraint:** linear attention's right-product state is fixed-size in sequence length and can be globally combined rather than forwarded tokenwise.
- **Mechanism:** each rank computes local K^T V state, one AllGather distributes states, prefix sums reconstruct causal inter-chunk state; intra-chunk masked work remains local.
- **State Ownership:** rank owns local sequence chunk and local memory state; SP group owns gathered state set; prefix order defines causal ownership.
- **Control Flow / Data Flow:** shard sequence -> local Q/K/V and memory -> AllGather states -> prefix sum -> local intra/inter outputs -> backward AllGather gradients.
- **Implementation Details:** one AllGather per forward/backward; cached prefix states in HBM; LASP-2H uses aligned collectives for hybrid standard-attention layers.
- **Evaluation Contract:** Linear-Llama3 pure/hybrid models, up to 2048K tokens on 64 GPUs; speed, scale, convergence and hybrid-ratio ablations.
- **Baselines / Ablations / Sensitivity / Overhead:** LASP-1 ring/P2P, Ring Attention and AllGather context parallelism.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 64-GPU/2048K headline; exact accelerator/topology/precision for every table must remain table-bound; no serving SLO.
- **What the Evidence Actually Proves:** for the paper's linear-state algebra, communication can be reorganized around fixed-size states and improve measured training speed.
- **What It Does Not Prove:** does not make AllGather universally better; standard attention and topology-dependent collectives retain different costs.
- **Limitations / Threats to Validity:** state tensor scales with hidden dimension and world size; causal intra-chunk work stays quadratic; collective stragglers remain.
- **Trade-offs / New Failure Modes:** more parallel compute and easier overlap for replicated gathered state, collective sensitivity and HBM cached prefixes.
- **Where the Previous Design Still Applies:** ring remains rational when state cannot be compactly combined, world size is large relative to state or topology favors neighbor exchange.
- **Evolution Relationship:** Direct Evolution: sequential ring state handoff -> associative state gather/prefix reconstruction -> hybrid aligned collectives.
- **ROADMAP Node:** TRAIN-DISTRIBUTED-TRAINING / TRAIN-TENSOR-PARALLEL.
- **Target and Adjacent Chapters Read:** Read Ch14, Ch22 and Ch36-38 to distinguish attention algebra, long-context model and communication plan.
- **Existing Coverage:** Books cover collective trade-offs; this source supplies an algebra-driven communication redesign case.
- **Integration Decision:** `Books Pending — Integration Deferred`.
- **Changed Files or Rejection Reason:** Weekly only.
- **Open Questions:** topology break-even, failure recovery, variable-length packing and interaction with TP/PP.

### LLaDA / Large Language Diffusion Models

- **Candidate / Week / Score:** LLaDA / 2025-W07 / 29/30。
- **Source Family ID:** `arxiv:2502.09992`。
- **Source Type:** Primary research paper + author code/model artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-14；W07 锁定 v1，后续 revision 不重复计分。
- **Direct Primary Sources:** https://arxiv.org/html/2502.09992v1；https://arxiv.org/abs/2502.09992。
- **Related Primary Sources:** 作者公开 repository/model artifact（以论文链接版本为准）。
- **Access and Verification Status:** v1 HTML 全文可读；metadata、Method、training、sampling、evaluation、appendix 与限制已核验。
- **Full-read Coverage:** 已读 Abstract、Introduction、masked-diffusion derivation、architecture、2.3T-token pretraining、SFT、sampling/remasking、matched 1B comparison、8B evaluation、appendix 与 scaling caveat。
- **Original Problem:** 文本 AR 推理的串行深度随输出长度增长，而已有 diffusion LM 缺少从头训练的大规模证据。
- **Why the Previous Design Was Reasonable:** causal factorization、append-only output、KV reuse 与 streaming contract 清晰，训练可 teacher-forcing 并行。
- **Changed Constraint:** 当目标变成多位置并行更新与双向条件化时，token 不再天然按左到右一次提交。
- **Mechanism:** 随机采样 mask ratio，对 masked tokens 做带 `1/t` 权重的交叉熵；推理从全 mask 开始，按 schedule 与 confidence 逐轮 unmask/remask。
- **State Ownership:** 模型拥有每轮 token posterior；sampler 拥有 mask schedule、length、steps 与 commit；runtime 不能把 provisional token 当稳定前缀。
- **Control Flow / Data Flow:** clean sequence → random masking → bidirectional Transformer loss；inference 为 all-mask state → parallel predictions → remask/select → repeated refinement → final commit。
- **Implementation Details:** 1B 与 8B decoder-style Transformer 取消 causal mask；v1 8B 用 MHA 而非 GQA，因为标准 AR KV cache 不适配该采样过程；FFN 相应缩小以近似参数规模。
- **Evaluation Contract:** 1B 使用尽量匹配 architecture/data 的 AR baseline；8B 报告 zero/few-shot、instruction 与 reasoning benchmarks；模型、prompt、sampling steps 和生成长度属于结果 identity。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 AR baselines、mask schedule 与 semi-AR remasking；作者未因 outlier 强行拟合定量 scaling curve；多轮 full-sequence forward 是主要推理成本。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 1B/8B；2.3T tokens；pretraining length 4096（1% 随机 1～4096）；约 0.13M H800 GPU-hours；global batch 1280、local batch 4/GPU；precision、线上并发与 SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在作者训练与评测合同内，masked diffusion 可以从头扩展到 8B，并形成有竞争力的文本模型分支。
- **What It Does Not Prove:** 不证明 diffusion 普遍快于 AR、可直接获得低延迟 streaming，也不证明作者 benchmark 等于生产 goodput。
- **Limitations / Threats to Validity:** 8B 与 AR 不完全等结构；sampler/length 是额外超参；缺少 serving concurrency、cache、tail latency 与独立复现合同。
- **Trade-offs / New Failure Modes:** 获得并行 token 更新与双向条件，付出多轮重算、mutable state、stop/stream commit、cache invalidation 与 schedule calibration。
- **Where the Previous Design Still Applies:** 低延迟 token streaming、成熟 KV runtime、短输出、严格 append-only 工具协议仍优先 AR。
- **Evolution Relationship:** `Alternative Branch`：AR append-only factorization ↔ masked diffusion iterative refinement，不是单向替代。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `INFER-KV-CACHE`、`INFER-SCHEDULING`。
- **Target and Adjacent Chapters Read:** 已读 Ch23 representation、Ch24 generation、Ch25 world-model 边界与相关 runtime handoff。
- **Existing Coverage:** Ch24 已拥有 mutable token、commit、cache 与 block diffusion 主线；该论文提供大规模文本 diffusion 的受限证据。
- **Integration Decision:** `Books Pending — Refine Existing Argument`；Historical Books Gate 关闭。
- **Changed Files or Rejection Reason:** 仅补 W07；不把作者 benchmark 或 H800 训练量写成通用 latency 结论。
- **Open Questions:** 如何让 sampler policy 暴露给 batch/SLO scheduler，并定义可流式、可回滚的 token commit？

### The Danger of Overthinking

- **Candidate / Week / Score:** The Danger of Overthinking / 2025-W07 / 26/30。
- **Source Family ID:** `arxiv:2502.08235`。
- **Source Type:** Primary empirical agent paper + released evaluation setup。
- **First-public Date / Revision History:** arXiv v1 2025-02-12；W07 使用 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.08235v1；https://arxiv.org/abs/2502.08235。
- **Related Primary Sources:** SWE-bench Verified 与 OpenHands/CodeAct 官方 artifacts。
- **Access and Verification Status:** v1 全文可读；轨迹 taxonomy、selection experiment、judge 与成本边界已核验。
- **Full-read Coverage:** 已读 task setup、single-agent harness、三类 overthinking、function-calling comparison、lowest-overthinking selection、cost/results、examples、limitations 与 appendix。
- **Original Problem:** 更多 reasoning tokens 在交互式软件工程中可能推迟必要 action、产生无关 action，或过早停止。
- **Why the Previous Design Was Reasonable:** 在纯推理任务中增加 internal search 常提高覆盖率，而且减少外部 tool round-trip。
- **Changed Constraint:** Agent 的信息来自环境；不行动就拿不到新证据，错误 action 还会改变后续状态。
- **Mechanism:** 对 trajectories 标注 Analysis Paralysis、Rogue Actions、Premature Disengagement，并在多次采样中选择低-overthinking 轨迹比较成功率与成本。
- **State Ownership:** runtime 拥有 tool/environment state 与预算；模型只提出 reasoning/action；judge 的标签不是环境真值。
- **Control Flow / Data Flow:** issue/context → reasoning/action alternation → environment observation → trajectory judge → outcome tests/cost accounting。
- **Implementation Details:** OpenHands CodeAct single-agent；Claude Sonnet 3.5 judge temperature 0、200K context，judge 不看最终 outcome；o1 隐藏 reasoning 因而只能分析可见行为。
- **Evaluation Contract:** SWE-bench Verified；成功由 harness/tests 决定，overthinking 由模型 judge；多样本选择需要额外调用成本。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 high/low reasoning、native function calling 与文本式交互；两样本低-overthinking选择约 27.3%/$800，对照 high-reasoning 29.1%/$1400，均为作者合同。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** hosted frontier models；200K judge context；hardware/precision/concurrency/tail SLO Not Disclosed；成本按作者 API 价格快照。
- **What the Evidence Actually Proves:** 在一个真实代码 harness 中，observable reasoning/action pattern 与成本、成功存在可测关系，更多 reasoning 不是单调收益。
- **What It Does Not Prove:** 不证明 overthinking 对失败有因果性，也不证明一种固定 reasoning budget 适用于所有 Agent。
- **Limitations / Threats to Validity:** 单领域/单 harness、judge 依赖、隐藏 reasoning、4018 与3908 trajectory 计数不一致、selection 需要额外样本。
- **Trade-offs / New Failure Modes:** 限制 reasoning 可降成本，却可能错过困难任务所需搜索；积极 action 可取证，也会增加副作用和错误状态。
- **Where the Previous Design Still Applies:** 无外部信息增益、tool 高风险或一次 action 不可逆时，先做较深内部规划仍合理。
- **Evolution Relationship:** `Direct Evolution`：unbounded think-then-act → evidence-aware action/reasoning budget → runtime stop/escalate policy。
- **ROADMAP Node:** `AGENT-PLANNING`，handoff `AGENT-TOOL-CALLING`、`AGENT-REFLECTION`、`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读 Ch78 Tool Calling、Ch79 Planning、Ch80 Reflection 的 action、replan 与 stopping 边界。
- **Existing Coverage:** Ch79 已区分 plan 与状态图；该研究补充 reasoning budget 必须与 environment information gain 联合治理。
- **Integration Decision:** `Books Pending — Refine Existing Argument`。
- **Changed Files or Rejection Reason:** 仅补 W07；不把相关性 taxonomy 改写为根因证明。
- **Open Questions:** 如何用可校准的 information gain、risk 与deadline在线选择 think、act、ask 或 stop？

### Step-Video-T2V

- **Candidate / Week / Score:** Step-Video-T2V / 2025-W07 / 29/30。
- **Source Family ID:** `arxiv:2502.10248`。
- **Source Type:** Primary model/system technical report + project artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-14；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.10248v1；https://arxiv.org/abs/2502.10248。
- **Related Primary Sources:** 论文项目页及作者公开模型/代码链接。
- **Access and Verification Status:** v1 全文、system sections、evaluation 与 appendix 已核验。
- **Full-read Coverage:** 已读 data pipeline、Video-VAE、DiT/flow matching、Video-DPO、distillation、H800 cluster、parallel emulator、VAE/attention kernels、mixed-resolution balancing、human evaluation 与 limitations。
- **Original Problem:** 高分辨率长视频把数据质量、3D attention activation、VAE codec 与跨机通信同时推到瓶颈。
- **Why the Previous Design Was Reasonable:** 单机/固定分辨率训练易复现，传统 VAE 与标准 TP/DP 足以支持较小图像或短视频。
- **Changed Constraint:** 30B video DiT、巨大 activation、混合 aspect/length 和月级千卡训练要求数据、codec、parallel plan 与 telemetry 联合设计。
- **Mechanism:** 16×16×8 Video-VAE 压缩；3D full attention DiT + flow matching；head-wise CP/self-attention、sequence-wise CP/cross-attention；独立 inference cluster 做 encoder/VAE，training cluster 做 DiT。
- **State Ownership:** data pipeline 拥有 clip/caption/quality lineage；VAE 拥有 latent identity；parallel runtime 拥有 rank/topology；telemetry 拥有 failure evidence。
- **Control Flow / Data Flow:** raw video → segmentation/filter/caption/balance → VAE/text encoding RPC → latent batches → DiT parallel train → checkpoint → DPO/distill → video decode/evaluation。
- **Implementation Details:** StepRPC over TCP/RDMA、StepTelemetry、StepMind；parallel emulator 选择 TP/SP/CP/PP/VPP；RoPE3D、自定义 fused norm/modulation、channel-last VAE 与 temporal/spatial multi-GPU decode。
- **Evaluation Contract:** 作者模型 540p 与公开/商业模型 720p/1080p 混合比较；人工 preference 和多项自动指标共同使用，分辨率是显著 confounder。
- **Baselines / Ablations / Sensitivity / Overhead:** 报告 VAE、parallel/kernel 与训练方法 ablations；3D full-attention activation 在指定配置约120GB；CP NIC 开销与 TP NVLink 可同量级，均为作者配置。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 30B、48 layers/48 heads/head-dim128/FFN24576；数千 H800，node 1.6Tbps RoCEv2；训练约一月；precision、完整 batch/concurrency/SLO 部分 Not Disclosed。
- **What the Evidence Actually Proves:** 在作者 workload 上，video model 必须把 codec、data、parallelism、network 与 observability 作为同一训练系统求解。
- **What It Does Not Prove:** 不证明其质量排名可跨分辨率比较，也不证明某个并行组合在其他 topology 上最优。
- **Limitations / Threats to Validity:** instruction following/physics 仍失败；human labels 昂贵；DPO/reward 自动化不足；closed cluster/artifact 限制复现。
- **Trade-offs / New Failure Modes:** 极大压缩和并行提高可训练性，却引入 latent distortion、RPC backpressure、rank imbalance、mixed-shape padding、VAE/DiT version skew。
- **Where the Previous Design Still Applies:** 小模型、短视频、固定 shape 或单机可容纳时，简单 DP/TP 与本地 codec 路径更易治理。
- **Evolution Relationship:** `Layering / Dependency`：video representation → distributed training runtime → model alignment，不是单项 architecture 替代。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `TRAIN-DISTRIBUTED-TRAINING`、`TRAIN-MEGATRON`。
- **Target and Adjacent Chapters Read:** 已读 Ch23～25 及 Ch36/40/41 的 communication、topology 与 runtime policy 边界。
- **Existing Coverage:** Ch24 已区分视频 workload；该报告为 codec-aware parallel training 提供完整受限系统案例。
- **Integration Decision:** `Books Pending — Refine Existing Argument`。
- **Changed Files or Rejection Reason:** 仅补 W07；所有性能数字保留 resolution、model、H800 与 cluster 条件。
- **Open Questions:** parallel emulator 如何用真实 queue、failure rate、energy 与 checkpoint recovery 校准离线估计？

### Region-Adaptive Sampling

- **Candidate / Week / Score:** Region-Adaptive Sampling / 2025-W07 / 24/30。
- **Source Family ID:** `arxiv:2502.10389`。
- **Source Type:** Primary research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-14；W07 使用 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.10389v1；https://arxiv.org/abs/2502.10389。
- **Related Primary Sources:** 作者 artifact/project links（若由论文公开）。
- **Access and Verification Status:** v1 Method、evaluation、human study 与 ablations 已核验。
- **Full-read Coverage:** 已读 token-dropping policy、cache reuse、error reset、KV recovery、SD3/Lumina experiments、COCO/human evaluation、hardware 与限制。
- **Original Problem:** DiT 每个 denoising step 重算所有 spatial tokens，即使部分区域已基本稳定。
- **Why the Previous Design Was Reasonable:** dense full refresh shape 固定、kernel 成熟，避免遗漏仍影响全局的 token。
- **Changed Constraint:** 相邻 denoising steps 的局部变化不均匀，允许把 compute 预算集中到 active regions。
- **Mechanism:** 根据前一步输出选择 active regions；inactive tokens 复用 cached noise；周期 dense error reset 防止 starvation；保留 dropped tokens 的 K/V 参与注意力。
- **State Ownership:** sampler 拥有 active mask 与 refresh schedule；cache 拥有 token version；model attention 仍消费完整 K/V context。
- **Control Flow / Data Flow:** previous denoiser output → region score/mask → active-token compute + inactive cache reuse → KV recovery → merged output → periodic dense reset。
- **Implementation Details:** training-free 注入 SD3 与 Lumina-Next sampling；dynamic ratio、region selection、reset、KV recovery 均为独立控制面。
- **Evaluation Contract:** 10K COCO samples，FID/sFID/CLIP；human study 14 prompts/1400 votes；speed 在 A100 80GB，实验集群另报 4×8 A100 40GB。
- **Baselines / Ablations / Sensitivity / Overhead:** 与 dense sampling/其他 token reduction 比较；四个组件 ablation 均显示作用；headline 2.36×/2.51×与人评约1.6× operating point 不同。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** SD3、Lumina-Next；A100 80GB speed，4×8 A100 40GB experiments；precision/batch/concurrency/SLO Not Disclosed。
- **What the Evidence Actually Proves:** trajectory-conditioned sparse refresh 能在作者两类 DiT 与数据合同下降低 denoising compute，并保留可比质量区间。
- **What It Does Not Prove:** 不证明 confidence 等于 cache validity，也不证明 irregular mask 在高并发 serving 中保持相同 goodput。
- **Limitations / Threats to Validity:** 模型/数据范围有限；缺少生产 batching、graph capture、tail latency 与独立复现；正文没有充分展开 worst-case mask 漂移。
- **Trade-offs / New Failure Modes:** 节省 dense compute，新增 selector cost、漏刷 active region、cache staleness、动态 shape 与 dense-reset 峰值。
- **Where the Previous Design Still Applies:** step 数少、全局变化广、exact refresh 或固定-shape kernel 优先时继续 dense sampling。
- **Evolution Relationship:** `Direct Evolution`：fixed dense refresh → trajectory-conditioned sparse refresh + bounded reset。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `INFER-EXECUTION`、`INFER-SCHEDULING`。
- **Target and Adjacent Chapters Read:** 已读 Ch23～25 与 Ch49 execution owner 的 cache/shape handoff。
- **Existing Coverage:** Ch24 已有 trajectory-conditioned refresh 主线；该论文提供其 selector/reset/KV 实例。
- **Integration Decision:** `Books Pending — No Change or Review-note Evidence`，待 Books Gate 去重。
- **Changed Files or Rejection Reason:** 仅补 W07；headline speedup 不脱离 GPU/model/metric contract。
- **Open Questions:** active mask 如何进入 batch scheduler，并用可观测 error budget 触发 reset？

### ZeroBench

- **Candidate / Week / Score:** ZeroBench / 2025-W07 / 24/30。
- **Source Family ID:** `arxiv:2502.09696`。
- **Source Type:** Primary benchmark paper + dataset artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-13；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.09696v1；https://arxiv.org/abs/2502.09696。
- **Related Primary Sources:** benchmark dataset/evaluation code linked by authors。
- **Access and Verification Status:** v1 全文、construction、parsing、pass@k 与 limitations 已核验。
- **Full-read Coverage:** 已读 100-question/334-subquestion construction、20-model filtering、exact-match parser、full-resolution input、pass@1/pass@5/k-of-k、error analysis 与 caveats。
- **Original Problem:** 现有 multimodal benchmarks 接近饱和，难以区分前沿模型的 perception/reasoning failure。
- **Why the Previous Design Was Reasonable:** broad benchmark 适合测总体能力和历史趋势，且不会故意把所有现有模型筛成零分。
- **Changed Constraint:** 研究者需要一个专门聚焦当前 unsolved tail 的压力测试，而不是稳定人口的通用分数。
- **Mechanism:** 人工构造并经20个模型筛选，只保留所有受测模型均失败的问题；严格答案解析与 pass/reliability variants 记录不同失败模式。
- **State Ownership:** dataset owner 决定题目人口；parser/scorer 拥有接受语义；model 只拥有回答，不拥有“零分”解释。
- **Control Flow / Data Flow:** candidate questions → human curation → multi-model filter → retained zero-score set → full-resolution inference → exact parser → aggregate/subquestion metrics。
- **Implementation Details:** 100 problems、334 subquestions；部分 parsing failure 由 Gemini 2 Flash 处理 o1-pro/QVQ outputs；token cap 未给出答案按失败。
- **Evaluation Contract:** 20 LMMs；greedy pass@1、stochastic pass@5 与 k/k consistency；full-resolution images；模型版本、prompt、output cap 属 run identity。
- **Baselines / Ablations / Sensitivity / Overhead:** 跨模型和 error categories 分析；由于 adversarial selection，不能与自然 task population 的平均准确率直接比较。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** hosted/open 20 LMMs；image resolution 尽量保真；hardware/precision/batch/concurrency/SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在作者人为选择的 hard-tail 集合与解析规则下，所测模型在 v1 时全部为零或近零。
- **What It Does Not Prove:** 不证明模型普遍没有多模态能力，也不证明未来模型的一点非零分具有广泛部署意义。
- **Limitations / Threats to Validity:** 选择偏差、100题规模、作者构题分布、parser/judge依赖与快速饱和风险。
- **Trade-offs / New Failure Modes:** 提升难度分辨率，却牺牲代表性和纵向稳定性；benchmark 进步可能来自适配筛选人口。
- **Where the Previous Design Still Applies:** 产品覆盖、slice fairness、稳定回归仍需要自然分布和版本化标准 benchmark。
- **Evolution Relationship:** `Alternative Branch`：representative evaluation ↔ adversarial hard-tail evaluation，两者必须并存。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`，handoff `MULTIMODAL-REPRESENTATION`。
- **Target and Adjacent Chapters Read:** 已读 Ch65 resource boundary、Ch66 evaluation、Ch67 monitoring 与 Ch23 representation contract。
- **Existing Coverage:** Ch66 已区分 task population 与 benchmark generator；ZeroBench 是明确的 adversarial-selection 案例。
- **Integration Decision:** `Books Pending — No Change or Review-note Evidence`。
- **Changed Files or Rejection Reason:** 仅补 W07；不把“zero”外推成通用模型结论。
- **Open Questions:** hard-tail benchmark 如何定期补题、冻结版本并防止 leaderboard-driven contamination？

### MM-RLHF

- **Candidate / Week / Score:** MM-RLHF / 2025-W07 / 27/30。
- **Source Family ID:** `arxiv:2502.10391`。
- **Source Type:** Primary research paper + preference dataset/artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-14；W07 使用 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.10391v1；https://arxiv.org/abs/2502.10391。
- **Related Primary Sources:** 作者 dataset/code/model links。
- **Access and Verification Status:** v1 全文、data pipeline、reward model、DPO/evaluation 与 limitations 已核验。
- **Full-read Coverage:** 已读 120K human pairs、image/video/safety taxonomy、critique expansion、reward heads、MM-DPO、small-model self-improvement、27 benchmarks、ablations 与 out-of-domain failure。
- **Original Problem:** multimodal preference alignment 同时面对视觉证据、语言质量与 safety，单一 scalar/小域数据易失真。
- **Why the Previous Design Was Reasonable:** scalar reward 和标准 DPO interface 简单，能复用文本 RLHF pipeline。
- **Changed Constraint:** multimodal response quality 有多维理由，且弱模型自采样经常缺少有用 preference contrast。
- **Mechanism:** 人工偏好对附简洁理由；GPT-4o扩写 critique；reward model 同时生成 critique 与 scalar；MM-DPO 按 reward 差动态缩放 pair update。
- **State Ownership:** human annotations 拥有原始 preference；teacher扩写是 derived evidence；reward model 拥有 proxy score；policy trainer 拥有 update，不得把 proxy 当 ground truth。
- **Control Flow / Data Flow:** multimodal prompt/responses → human preference/rationale → teacher critique expansion → critique+scalar RM → weighted DPO → benchmark/human evaluation。
- **Implementation Details:** 120K pairs、10 quality dimensions；实验覆盖 InternVL2-1B、LLaVA-OneVision 0.5B/7B 等；全部 pair 训练而非硬过滤。
- **Evaluation Contract:** image/video/safety 共27 benchmarks；比较 SFT、标准 DPO、reward-weighted variants 与不同数据来源；judge/model版本是结果 identity。
- **Baselines / Ablations / Sensitivity / Overhead:** human preference pairs 显著优于小模型 self-generated pairs；reward model 在有限自然图像/对话域过拟合；critique/scalar/dynamic scaling 分项比较。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型规模披露，hardware、precision、sequence length、batch、concurrency 与 SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在作者数据/模型合同内，显式 critique 与 human preference 能改善 multimodal reward modeling 和 DPO operating point。
- **What It Does Not Prove:** 不证明 GPT-4o 扩写理由无偏，也不证明 scalar reward 在新 modality/domain 可校准迁移。
- **Limitations / Threats to Validity:** teacher bias、RM domain shift、弱模型样本同质/错误、硬件与训练成本不透明、benchmark judge相关性。
- **Trade-offs / New Failure Modes:** 更丰富 supervision 增加可诊断性，却引入 rationale fabrication、reward hacking、derived-label provenance 与多目标权重漂移。
- **Where the Previous Design Still Applies:** 单一可验证目标、低数据量或 teacher 不可信时，简单 preference loss/规则 verifier 更稳。
- **Evolution Relationship:** `Direct Evolution`：scalar preference → critique-conditioned reward → dynamically weighted preference optimization。
- **ROADMAP Node:** `TRAIN-RLHF`，handoff `TRAIN-DPO`、`PLATFORM-EVALUATION-SYSTEM`、`MULTIMODAL-REPRESENTATION`。
- **Target and Adjacent Chapters Read:** 已读 Ch29～34 post-training chain、Ch23 modality boundary 与 Ch66 evidence contract。
- **Existing Coverage:** Books 已有 reward/judge 非真值边界；该 family 补 multimodal rationale provenance 与弱模型 self-sampling 边界。
- **Integration Decision:** `Books Pending — Refine Existing Argument`。
- **Changed Files or Rejection Reason:** 仅补 W07；不保留脱离模型/数据/judge 的平均提升数字。
- **Open Questions:** derived critique 如何记录 teacher version、原始 rationale、冲突与审计回滚？

### ImageRAG

- **Candidate / Week / Score:** ImageRAG / 2025-W07 / 24/30。
- **Source Family ID:** `arxiv:2502.09411`。
- **Source Type:** Primary research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-13；W07 使用 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.09411v1；https://arxiv.org/abs/2502.09411。
- **Related Primary Sources:** 作者 code/project 与所用 LAION/domain retrieval assets。
- **Access and Verification Status:** v1 workflow、retrieval/rerank、evaluation、ablations 与 limitations 已核验。
- **Full-read Coverage:** 已读 initial generation、VLM gate、missing-concept query、retrieval、reference-conditioned regeneration、SDXL/OmniGen、database/reranker ablations 与 failure cases。
- **Original Problem:** text-to-image model 的参数知识缺少长尾视觉概念，单靠 prompt 不能补回具体 appearance。
- **Why the Previous Design Was Reasonable:** one-shot generator 路径短，不维护外部 image corpus、retriever 与 retry state。
- **Changed Constraint:** 目标概念稀有或域外时，外部视觉 exemplar 比语言描述包含更多可用条件。
- **Mechanism:** 先生成；VLM 判断缺失概念并生成 retrieval captions；从 image DB 检索/rerank；reference-conditioned model 重生成，无需专门 RAG training。
- **State Ownership:** generator 拥有 provisional image；VLM gate 拥有 repair proposal；retriever/corpus 拥有 exemplar provenance；workflow 决定 retry/commit。
- **Control Flow / Data Flow:** prompt → initial image → VLM match/missing concepts → image query → retrieve/rerank → reference-conditioned regeneration → evaluate/commit。
- **Implementation Details:** 适配 SDXL 与 OmniGen；比较 BM25、CLIP、SigLIP、GPT rerank；corpus 含 LAION subsets 与 domain datasets。
- **Evaluation Contract:** 多数据集比较 one-shot、text retrieval 与 image retrieval；corpus size/relevance、VLM gate 和 base generator 均为结果条件。
- **Baselines / Ablations / Sensitivity / Overhead:** 更大相关 corpus 通常有益；小且无关 corpus 可伤害强模型；不同 reranker/gate 有独立 ablation；增加一次或多次 generation cost。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** SDXL/OmniGen；retrieval DB披露；hardware、precision、batch、concurrency、latency SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在作者 datasets 和 reference-capable generators 上，外部图像检索可修复部分长尾概念生成。
- **What It Does Not Prove:** 不证明 VLM gate 正确，也不证明 RAG 对 counting、layout 或任何未学能力有效。
- **Limitations / Threats to Validity:** corpus coverage/copyright、false-positive gate、base model无能力吸收reference、额外延迟与未披露硬件。
- **Trade-offs / New Failure Modes:** 获得可更新外部视觉知识，新增 retrieval poisoning、exemplar授权、gate误判、重复生成成本和 provenance 责任。
- **Where the Previous Design Still Applies:** 常见概念、强 generator、低延迟或不能维护可信 corpus 时继续 one-shot。
- **Evolution Relationship:** `Layering / Dependency`：one-shot generation → detect evidence gap → visual retrieval → bounded regeneration。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`，handoff `MULTIMODAL-GENERATIVE-PARADIGMS`、`AGENT-RAG`。
- **Target and Adjacent Chapters Read:** 已读 Ch23～25 与 Agent RAG/context owner 的 retrieval/provenance handoff。
- **Existing Coverage:** Ch24 已有 plan/generate/validate/retry；该研究提供 image retrieval 作为 repair evidence 的实例。
- **Integration Decision:** `Books Pending — Refine Existing Argument`。
- **Changed Files or Rejection Reason:** 仅补 W07；不将作者图像指标外推成通用 RAG 质量。
- **Open Questions:** 视觉 exemplar 的版权、tenant scope、revision 与 deletion 如何进入 retrieval identity？

### DarwinLM

- **Candidate / Week / Score:** DarwinLM / 2025-W07 / 27/30。
- **Source Family ID:** `arxiv:2502.07780`。
- **Source Type:** Primary research paper + pruning/search artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-11；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.07780v1；https://arxiv.org/abs/2502.07780。
- **Related Primary Sources:** 作者 repository与 sparse model artifacts。
- **Access and Verification Status:** v1 全文、search、post-training、hardware accounting 与 limitations 已核验。
- **Full-read Coverage:** 已读 module sparsity database、OBS/ZipLM pruning、evolutionary mutation、KL fitness、multistage offspring selection、calibration、10B-token tuning、baselines、runtime 与 limitations。
- **Original Problem:** uniform layer/module pruning 忽略不同 attention/MLP 组件的敏感度，巨大组合空间又无法穷举。
- **Why the Previous Design Was Reasonable:** uniform sparsity 易配置、硬件 shape 稳定，局部 pruning score 可低成本计算。
- **Changed Constraint:** 给定 target parameter/FLOP budget 时，需要搜索 non-uniform structured sparsity，并预估 post-training recovery。
- **Mechanism:** 预建各层 attention/MLP sparsity候选；进化搜索 mutation；用 dense-vs-sparse output KL 评估；对 offspring 做递增 token 的短训练/淘汰。
- **State Ownership:** search controller 拥有 architecture genome与budget；calibration set 定义 fitness；post-training optimizer 拥有 recovery trajectory。
- **Control Flow / Data Flow:** dense model → layerwise pruning database → population mutation → KL/multistage tuning selection → chosen sparse architecture → 10B-token post-training → task evaluation。
- **Implementation Details:** Llama2-7B、Llama3.1-8B、Qwen2.5-14B；200 generations、16 offspring；多阶段 1K～8K eval tokens与10K～200K tuning tokens。
- **Evaluation Contract:** FineWeb-Edu post-training；perplexity/zero-shot tasks；不同 sparsity levels/models；搜索与训练成本分开报告。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比 uniform/ShortGPT/ShearedLlama等；16-sequence search fitness与2048×4096完整 calibration边界不同；multistage selection降低全量训练浪费。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** pruning/search 10×L40S；post-training 40×H100约13h、10B tokens；batch 1024/1152/2048依模型；precision/concurrency/SLO Not Disclosed；跨硬件时长不等价。
- **What the Evidence Actually Proves:** 在作者模型和预算内，training-aware nonuniform structured search 优于若干固定 pruning baselines。
- **What It Does Not Prove:** 不证明 KL proxy 在其他任务/数据可靠，也不证明 sparse parameter count 自动转换为部署 latency/energy 收益。
- **Limitations / Threats to Validity:** 搜索与fine-tune成本高、task robustness有限、跨硬件比较未归一、需要可用 calibration data。
- **Trade-offs / New Failure Modes:** 获得 budget-specific architecture，新增搜索成本、proxy overfit、shape/kernel不匹配、post-training data依赖与artifact proliferation。
- **Where the Previous Design Still Applies:** 需要固定规则 shape、极低搜索预算或成熟 kernel 只支持少数组合时，uniform pruning仍合理。
- **Evolution Relationship:** `Direct Evolution`：uniform pruning → sensitivity-aware candidates → training-aware architecture search。
- **ROADMAP Node:** `INFER-EXECUTION`，handoff `TRAIN-PRETRAINING`、`PLATFORM-MODEL-REGISTRY`。
- **Target and Adjacent Chapters Read:** 已读 Ch28 pretraining、Ch49 execution plan 与 artifact/registry相邻 owner。
- **Existing Coverage:** Books 已有 compile/shape与artifact identity；该论文补“结构选择必须把恢复训练计入 fitness”。
- **Integration Decision:** `Books Pending — Refine Existing Argument`。
- **Changed Files or Rejection Reason:** 仅补 W07；不把跨 L40S/A100/H100 wall time作归一速度结论。
- **Open Questions:** search fitness 如何直接纳入真实 kernel、memory、energy、batch 与 tail-SLO，而不只用 KL/参数量？

### FoNE

- **Candidate / Week / Score:** FoNE / 2025-W07 / 22/30。
- **Source Family ID:** `arxiv:2502.09741`。
- **Source Type:** Primary research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-13；W07 使用 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.09741v1；https://arxiv.org/abs/2502.09741。
- **Related Primary Sources:** 作者公开 implementation（若由论文链接）。
- **Access and Verification Status:** v1 formulation、synthetic experiments、ablations、efficiency与限制已核验。
- **Full-read Coverage:** 已读 number parser、Fourier circular embedding、digit decoder/loss、addition/subtraction/multiplication、data-efficiency、token/timing、modulus/sin-cos ablations 与 caveats。
- **Original Problem:** subword tokenization 将数值按词频切分，弱化位值、进位与连续 magnitude structure。
- **Why the Previous Design Was Reasonable:** 通用 tokenizer 无需独立 numeric execution path，能统一处理文本与数字字符串。
- **Changed Constraint:** 精确算术要求可组合 digit/place representation，且长数字的 token cost 与数据量迅速增长。
- **Mechanism:** parser 将数字替换为 `[Num]`；以多组 base-10 period 的 sin/cos表示数值；专用 decoder按位预测数字并用 circular similarity训练。
- **State Ownership:** tokenizer/parser 拥有数字边界；numeric encoder拥有 value representation；special decoder拥有 digit output；普通 LM 仍拥有上下文。
- **Control Flow / Data Flow:** text parse → number extraction → Fourier embedding + token embedding → Transformer → digit-wise numeric decoder / text head → reassembly。
- **Implementation Details:** 每位约2维 Fourier feature，period按10的幂；synthetic arithmetic 上比较 subword/digit baselines 与 GPT2-Large variants。
- **Evaluation Contract:** 加减乘 synthetic datasets、不同digit lengths与训练数据规模；token reduction和wall-time只在作者实现下解释。
- **Baselines / Ablations / Sensitivity / Overhead:** mod10有效而mod5/7失败；sin+cos优于单一/naive digit；作者报告6位小数加法约64×数据效率与3×/6×token减少。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 小型Transformer/GPT2-Large variants；hardware、precision、batch、concurrency、SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在 synthetic base-10 arithmetic 中，显式数值 inductive bias 可明显改善样本与token效率。
- **What It Does Not Prove:** 不证明能替代通用 tokenizer，也不证明对开放文本、浮点、单位、科学记数或真实计算器可靠。
- **Limitations / Threats to Validity:** base-10与synthetic bias、parser依赖、范围/精度/负数和单位边界、缺少外部复现和硬件合同。
- **Trade-offs / New Failure Modes:** 获得 numeric structure，新增双通道token identity、parser ambiguity、decoder integration、range overflow与非十进制迁移成本。
- **Where the Previous Design Still Applies:** 数字主要是ID/文本片段、无需精确算术或 schema不稳定时，普通 tokenizer更简单。
- **Evolution Relationship:** `Alternative Branch`：generic tokenization ↔ typed numeric representation，不是全局替代。
- **ROADMAP Node:** `MODEL-TOKENIZER`，handoff `MODEL-EMBEDDING`、`AGENT-TOOL-CALLING`。
- **Target and Adjacent Chapters Read:** 已读 Tokenizer/Embedding相邻章节及 Tool Calling 中 authoritative computation边界。
- **Existing Coverage:** Books 已有 representation identity；该研究补“数值可作为 typed side channel”，但仍应把高可靠计算交给工具。
- **Integration Decision:** `Books Pending — Structural Example`。
- **Changed Files or Rejection Reason:** 仅补 W07；不把synthetic data-efficiency外推通用 reasoning。
- **Open Questions:** typed number path 如何处理 locale、unit、precision、NaN/Inf 与 tool-verifiable exact computation？

### Precise Parameter Localization for Textual Generation in Diffusion Models

- **Candidate / Week / Score:** Precise Parameter Localization for Textual Generation in Diffusion Models / 2025-W07 / 23/30。
- **Source Family ID:** `arxiv:2502.09935`。
- **Source Type:** Primary research paper + project artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-14；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.09935v1；https://arxiv.org/abs/2502.09935；https://t2i-text-loc.github.io/。
- **Related Primary Sources:** paper-linked benchmark/code artifacts。
- **Access and Verification Status:** v1 全文、appendices与project page可核；无独立复现。
- **Full-read Coverage:** 已读 background、patch/injection、three-model localization、specialization、74,285-image LoRA、editing/toxic-text applications、baselines、timesteps、dataset-size/layer-count ablations、appendix与conclusion。
- **Original Problem:** text-to-image diffusion 的视觉文字能力纠缠在庞大模型中，全量 adaptation 会破坏图像质量与多样性。
- **Why the Previous Design Was Reasonable:** 全部 cross-attention LoRA 不需要先做因果定位，适合能力分布未知时的通用 adaptation。
- **Changed Constraint:** 若只有少数层实际控制文字内容，扩大可训练范围会增加 overfit、mode collapse 与编辑副作用。
- **Mechanism:** 对目标 prompt 缓存 text K/V，并逐层 patch 到 source generation；用OCR与image alignment定位高响应 attention层；只在这些层训练LoRA或做运行时替换。
- **State Ownership:** base model拥有视觉生成；localized attention K/V拥有文本内容干预；OCR/toxicity classifier仅是评估/guard proxy。
- **Control Flow / Data Flow:** source/target prompts → target K/V cache → per-layer patch into source denoising → OCR/image metrics → selected layers → localized LoRA/edit/safety intervention。
- **Implementation Details:** SDXL定位3/70层、DeepFloyd IF 1/22、SD3 1/24；约0.61%/0.21%/0.23%参数；联合/交叉attention均只替换text components。
- **Evaluation Contract:** SimpleBench/CreativeBench各400 prompts，100 validation/300 test；OCR F1/LD/CLIP-T与MSE/SSIM/PSNR；三种diffusion architecture。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比all-attention LoRA、P2P/P2P*、negative prompt、Safe Diffusion、Prompt Swap；20K～200K data与1/2/3/10/30/70 injected layers显示text/background trade-off。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** SDXL/DeepFloyd IF/SD3；74,285 MARIO-LAION images用于主LoRA；hardware、precision、batch、concurrency/SLO Not Disclosed；execution time仅作者环境。
- **What the Evidence Actually Proves:** 在三模型和窄文字任务中，少量attention层对视觉文字有强因果干预作用，局部 adaptation 可减轻全层LoRA collapse。
- **What It Does Not Prove:** 不证明这些层“ solely”拥有所有文字因果，也不证明toxicity classifier/patch是完整安全系统或跨模型层号稳定。
- **Limitations / Threats to Validity:** OCR/classifier bias、单词模板、模型范围有限、缺硬件/复现、层定位可能随checkpoint/语言/字体漂移。
- **Trade-offs / New Failure Modes:** 局部更新提高保真和效率，新增 localization cost、layer identity drift、proxy误判、K/V patch版本不一致与文本/背景权衡。
- **Where the Previous Design Still Applies:** 目标能力分散、任务变化大、没有可信定位数据时，全层或更宽 adaptation仍可能合理。
- **Evolution Relationship:** `Direct Evolution`：broad LoRA → causal localization → narrow LoRA/runtime intervention。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `TRAIN-LORA`、`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读 Ch23～25、LoRA owner与Security/Evaluation handoff。
- **Existing Coverage:** Ch24 已讨论 mutable/intermediate state；该family补“先定位owner再adapt”的机制案例。
- **Integration Decision:** `Books Pending — Refine Existing Argument`。
- **Changed Files or Rejection Reason:** 仅补 W07；参数百分比只保留三checkpoint/该定位法边界。
- **Open Questions:** localized layer identity 如何随model revision、adapter、language与quantization进入registry/evaluation run？

### Selective Self-to-Supervised Fine-Tuning

- **Candidate / Week / Score:** Selective Self-to-Supervised Fine-Tuning / 2025-W07 / 23/30。
- **Source Family ID:** `arxiv:2502.08130`。
- **Source Type:** Primary empirical research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-12；W07 锁定 v1，后续 revision 只用于家族演进核验。
- **Direct Primary Sources:** https://arxiv.org/html/2502.08130v1；https://arxiv.org/abs/2502.08130。
- **Related Primary Sources:** GSM8K、MBPP、Natural Questions 及论文列出的 generalization benchmarks。
- **Access and Verification Status:** v1 HTML 全文可读；Method、实验、judge contract、泛化评估与限制已核验。
- **Full-read Coverage:** 已读 Abstract、Introduction、Related Work、selection/paraphrase pipeline、training setup、in/out-domain evaluation、case study、limitations 与 appendix。
- **Original Problem:** 标准 SFT 强迫模型模仿外部 target，即使模型自己的正确表达已足够，可能增加与基座分布的偏移并损害泛化。
- **Why the Previous Design Was Reasonable:** gold response 可直接监督、实现简单，在模型无法生成正确解时也是最可靠的行为目标。
- **Changed Constraint:** 基座已经能正确回答部分样本时，所有 token 一律覆盖为同一 gold wording 会浪费已有能力并放大 distribution shift。
- **Mechanism:** 先让模型生成回答；若 equivalence judge 判定正确，就用 self-generated response 训练，否则让模型 paraphrase gold；paraphrase 仍不正确时回退 gold。
- **State Ownership:** base model 生成 candidate；equivalence judge 拥有选择门槛；data pipeline 保存 candidate、gold、judge 与 fallback lineage；trainer 只消费已选 target。
- **Control Flow / Data Flow:** prompt → self response → equivalence check → self target 或 gold paraphrase → second check → gold fallback → ordinary SFT loss。
- **Implementation Details:** 不是新 loss，而是训练前 target-selection pipeline；选择质量依赖任务级等价判定，开放式任务可需更强 LLM judge。
- **Evaluation Contract:** Mistral-Instruct-v2 7B；GSM8K、MBPP、NQ 为训练/域内任务，另测 MMLU、TruthfulQA、HellaSwag、WinoGrande 泛化。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比 gold SFT、self-training 与混合分支；作者报告 GSM8K/MBPP 域内提升并检查跨任务回退；judge、paraphrase 与二次核验构成额外推理开销。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Mistral-Instruct-v2 7B；关键 hardware、precision、完整 length/batch/concurrency 与 serving SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在作者三类任务合同内，按正确性选择 self target 可以减少无条件 gold imitation 的部分泛化损失。
- **What It Does Not Prove:** 不证明 self-generated target 普遍优于专家答案，也不证明 LLM judge 在开放式任务可靠或对所有基座有效。
- **Limitations / Threats to Validity:** judge false positive 会固化错误；paraphrase 可能仍泄漏 gold；任务和单一 7B 模型有限，正文个别泛化描述存在疑似措辞错误。
- **Trade-offs / New Failure Modes:** 降低 target mismatch，付出额外生成、judge 成本、selection bias、错误自确认和更复杂的数据 provenance。
- **Where the Previous Design Still Applies:** 基座能力弱、答案唯一且可验证、合规 wording 必须固定或 judge 不可信时，直接 gold SFT 仍更合理。
- **Evolution Relationship:** `Direct Evolution`：uniform gold imitation → correctness-gated self target → provenance-preserving fallback。
- **ROADMAP Node:** `TRAIN-SFT`，handoff `TRAIN-DATA` 与 `PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读 Ch28 Pretraining、Ch29 SFT、Ch30 LoRA，确认本机制改变 target construction 而非 parameterization。
- **Existing Coverage:** Ch29 已有 demonstration schedule、selective update 与 evidence boundary；本 family 提供具体 selection pipeline 的受限证据。
- **Integration Decision:** `Books Pending — Refine Existing Argument`；Historical Books Gate 关闭。
- **Changed Files or Rejection Reason:** 仅补 W07；不复述未绑定完整训练合同的 headline improvement。
- **Open Questions:** equivalence judge 如何校准，并在错误 self target 写入前提供 abstain、人工复核与回滚？

### STMA: A Spatio-Temporal Memory Agent for Long-Horizon Embodied Task Planning

- **Candidate / Week / Score:** STMA / 2025-W07 / 24/30。
- **Source Family ID:** `arxiv:2502.10177`。
- **Source Type:** Primary agent-system paper + simulated environment evaluation。
- **First-public Date / Revision History:** arXiv v1 2025-02-14；W07 使用 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.10177v1；https://arxiv.org/abs/2502.10177。
- **Related Primary Sources:** TextWorld environment and cited ReAct、Reflexion、AdaPlanner baselines。
- **Access and Verification Status:** v1 全文、算法、实验、ablations、案例与 limitations 已核验。
- **Full-read Coverage:** 已读 POMDP formulation、temporal summarizer、spatial knowledge graph、retrieval/aggregation、planner、critic、四级任务、baseline、ablation、case study 与 appendix。
- **Original Problem:** 长时 embodied task 同时要求记住历史动作结果和空间关系；仅保留文本 history 会超长，只有静态图又会丢时间变化。
- **Why the Previous Design Was Reasonable:** 短任务用完整 trajectory 最忠实；环境小且稳定时单一 spatial map 足够，避免额外 summarizer 与 graph maintenance。
- **Changed Constraint:** 任务跨房间、对象状态和多步依赖增长，agent 必须压缩时间证据并按当前 observation 修正空间 belief。
- **Mechanism:** temporal buffer 周期摘要历史；spatial memory 维护动态 relation graph；retriever/aggregator 构造 belief，planner 生成多步 plan，critic 在每个 action 前用最新状态检查。
- **State Ownership:** environment 拥有真实状态；temporal memory 拥有轨迹摘要；spatial graph 拥有派生 belief；planner/critic 只能提出和检查 action，不能把 belief 冒充事实。
- **Control Flow / Data Flow:** observation/action history → temporal summary + graph update → relevant relation retrieval → plan → pre-action critic → environment transition → observation reconciliation。
- **Implementation Details:** belief 分为 temporal 与 spatial components；knowledge graph 由 LLM 更新，错误 relation 会传播到 planner；critic 提供逐步而非仅终局校验。
- **Evaluation Contract:** TextWorld 32 个 cooking tasks、四个难度级别、未知 rooms/items；主要使用 Qwen2.5-72B，并含 proprietary-model comparison。
- **Baselines / Ablations / Sensitivity / Overhead:** ReAct、Reflexion、AdaPlanner；去除 memory、summarizer、spatial belief、critic 的 ablations；“no memory zero”部分由任务构造决定。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Qwen2.5-72B；simulated text environment；hardware、precision、context-length operating point、并发与控制 SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在作者 TextWorld 合同内，把 temporal compression、spatial belief 与 action-time critic 分责可提升长程任务完成。
- **What It Does Not Prove:** 不证明 dynamic graph 等于真实 world state，不证明 31.25% success/24.7% average score 可迁移到视觉机器人或生产 Agent。
- **Limitations / Threats to Validity:** text-only simulator、任务偏向 memory、单一主要开源模型、LLM summary/graph error、无真实 sensor/action latency。
- **Trade-offs / New Failure Modes:** 更长 horizon 可控性换来 summary loss、graph staleness、relation hallucination、critic overhead 与 belief/ground-truth 混淆。
- **Where the Previous Design Still Applies:** 短任务、完全可观测环境、状态可由 transactional system 直接读取时，完整 history 或显式 state machine 更简单可信。
- **Evolution Relationship:** `Layering / Dependency`：trajectory history → typed temporal/spatial memory → observation-conditioned plan/critic loop。
- **ROADMAP Node:** `AGENT-MEMORY`，handoff `AGENT-PLANNING`、`AGENT-REFLECTION` 与 `MULTIMODAL-WORLD-MODELS`。
- **Target and Adjacent Chapters Read:** 已读 Ch76 RAG、Ch77 Memory、Ch78 Tool Calling 与 Ch79 Planning 的 state/action owner 边界。
- **Existing Coverage:** Ch77 已区分 fact、derived memory 与 world state；该论文补充 text-world 中的 spatio-temporal decomposition 案例。
- **Integration Decision:** `Books Pending — No Change or Review-note Evidence`。
- **Changed Files or Rejection Reason:** 仅补 W07；不把模拟 benchmark 成功率外推为 embodied reliability。
- **Open Questions:** 如何用 timestamp、contradiction、sensor confidence 与 authoritative state 修正图，并度量 summary/graph 各自的错误贡献？

### CRANE: Reasoning with Constrained LLM Generation

- **Candidate / Week / Score:** CRANE / 2025-W07 / 25/30。
- **Source Family ID:** `arxiv:2502.09061`。
- **Source Type:** Primary theory + system evaluation paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-13；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.09061v1；https://arxiv.org/abs/2502.09061。
- **Related Primary Sources:** SynCode and formal-language constrained decoding baselines referenced by authors。
- **Access and Verification Status:** v1 HTML 全文、theorem、algorithm、experiments、ablations 与 appendices 已核验。
- **Full-read Coverage:** 已读 formal grammar、expressiveness theorem、augmented grammar construction、delimiter algorithm、GSM-Symbolic/FOLIO setup、all model tables、error cases 与 appendix proof。
- **Original Problem:** 对完整输出施加 grammar 能保证 parse validity，却也可能禁止自然语言 chain-of-thought，从而损害需要推理后再结构化提交的任务。
- **Why the Previous Design Was Reasonable:** 输出从第一 token 起都属于机器协议时，全程 constrained decoding 可提供确定的语法边界并简化 parser。
- **Changed Constraint:** 当同一 response 同时承载自由推理和 formal answer 时，reasoning language 与 commit grammar 的表达能力不同。
- **Mechanism:** 用 augmented grammar 保留任意 reasoning prefix，并通过显式 delimiters 进入/退出 constrained segment；decoder 仅对最终 formal span 应用 grammar mask。
- **State Ownership:** model 拥有自由 reasoning tokens；constraint engine 拥有 formal-span token mask；trusted executor/parser 仍拥有 schema、semantic validation 与执行授权。
- **Control Flow / Data Flow:** prompt → unconstrained reasoning → start delimiter → grammar-constrained answer → end delimiter → parse/semantic check。
- **Implementation Details:** delimiters S1/S2 切换 decoder mode；理论结果是对特定 formalization 的表达性论证，不是任意现实 LLM 的正确性保证。
- **Evaluation Contract:** GSM-Symbolic 与 FOLIO；Qwen2.5 1.5B/7B Coder/Math、Llama-3.1-8B、DeepSeek-R1-Distill variants；greedy decoding，FOLIO 最多 800 new tokens、2-shot。
- **Baselines / Ablations / Sensitivity / Overhead:** unconstrained CoT、SynCode full constraint 与 CRANE；同时测 task accuracy、parse；分段方法常增加 output tokens 和 mode-switch overhead。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 48-core Xeon Silver 4214R + 2×RTX A5000；模型如上；precision、batch/concurrency 和 serving SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在作者 symbolic tasks 中，把 reasoning 与 formal commit 分段能同时改善 parse validity 并避免全程 grammar 的部分表达限制。
- **What It Does Not Prove:** 不证明 delimiter 一定被正确产生，不保证 formal answer 语义正确，更不授予 tool execution 权限。
- **Limitations / Threats to Validity:** 两类任务、有限模型、greedy setting；theorem 的抽象机器假设与实际 decoder 有距离；delimiter failure 未消失。
- **Trade-offs / New Failure Modes:** 获得结构合法性与推理自由，付出更多 token、mode state、delimiter injection/omission、grammar version drift 和 parser mismatch。
- **Where the Previous Design Still Applies:** 完全结构化、无需自然语言 reasoning、低延迟或 schema 极窄时，全程 constraint 更简单；只需文本答案时 unconstrained generation 仍合理。
- **Evolution Relationship:** `Direct Evolution`：full-output grammar → reasoning/commit split → typed proposal + semantic/authorization gate。
- **ROADMAP Node:** `AGENT-TOOL-CALLING`，handoff `PLATFORM-EVALUATION-SYSTEM` 与 inference sampling。
- **Target and Adjacent Chapters Read:** 已读 Ch77 Memory、Ch78 Tool Calling、Ch79 Planning，确认 grammar 只拥有 proposal syntax，不拥有 action authority。
- **Existing Coverage:** Ch78 已区分 typed proposal、validation 与 execution；CRANE 补充为什么 constraint boundary 应贴近 commit boundary。
- **Integration Decision:** `Books Pending — Refine Existing Argument`。
- **Changed Files or Rejection Reason:** 仅补 W07；不把 parse accuracy 写成 tool-task success。
- **Open Questions:** delimiter、grammar revision 与 semantic validator 如何进入 trace identity，并在 partial streaming 时安全回滚？

### The Mirage of Model Editing: Revisiting Evaluation in the Wild

- **Candidate / Week / Score:** The Mirage of Model Editing / 2025-W07 / 27/30。
- **Source Family ID:** `arxiv:2502.11177`。
- **Source Type:** Primary evaluation paper + QAEdit benchmark artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-16；W07 使用 v1。
- **Direct Primary Sources:** https://arxiv.org/pdf/2502.11177v1；https://arxiv.org/abs/2502.11177。
- **Related Primary Sources:** EasyEdit implementation；Natural Questions、TriviaQA、SimpleQA、ZsRE、CounterFact datasets。
- **Access and Verification Status:** v1 PDF 全文可读；dataset construction、four-module comparison、single/sequential editing、appendix 与 limitations 已核验。
- **Full-read Coverage:** 已读 related work、QAEdit 19,249-sample construction、six methods/three models、input/generation/truncation/metric controls、batch sensitivity、sequential retention、judge prompt、hardware 与 limitations。
- **Original Problem:** model-editing 文献常在 teacher forcing、gold-length truncation 和 token overlap 下报告近满分，但这些设置泄漏 target 并隐藏 autoregressive error propagation。
- **Why the Previous Design Was Reasonable:** token-level受控设置便于隔离单次参数更新、降低开放式生成和 judge 噪声，适合诊断 edit 是否进入模型。
- **Changed Constraint:** 部署需要 context-guided prompt、自然停止、autoregressive decoding 与连续多次 edit；评测必须覆盖真实 generation contract。
- **Mechanism:** 把 evaluation 拆成 input、generation strategy、output truncation、metric 四个独立模块，逐项替换为 deployment-like contract，并增加 sample-wise/mini-batch sequential editing。
- **State Ownership:** edit method 拥有参数/side memory 更新；evaluation harness 拥有 prompt、decode、stop、judge 与 dataset revision；模型不能用 gold tokens 作为隐藏测试输入。
- **Control Flow / Data Flow:** source QA → subject/paraphrase/locality construction → edit original model → natural AR generation → LLM judge/locality → repeated edits → previous-batch regression。
- **Implementation Details:** QAEdit 来自 NQ、TriviaQA、SimpleQA；GPT-4 提取 subject/paraphrase；GPT-4o-mini binary judge；GRACE、WISE、FT-M、MEND、R-ROME、MEMIT 经 EasyEdit。
- **Evaluation Contract:** Llama-2-7B-chat、Mistral-7B-v0.1、Llama-3-8B；greedy decoding；单次与最多 1000 sequential edits；QAEdit 及两个经典 editing datasets。
- **Baselines / Ablations / Sensitivity / Overhead:** 四模块逐项控制，batch size 对 FT-M/MEMIT 的相反敏感性，20-sample batch 的旧知识回退；MEND/Llama-3 因 architecture incompatibility 排除。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** mini-batch 上限受 80GB A800 约束；模型如上；precision、完整 latency/concurrency 与 production SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在这些参数编辑方法/模型上，teacher forcing、target-length truncation 与 match ratio 可显著夸大结果；连续编辑暴露 retention/locality 崩塌。
- **What It Does Not Prove:** 不证明所有 model editing 都无效，也不覆盖 external-memory/in-context editing 或所有模型规模；GPT judge 不是绝对真值。
- **Limitations / Threats to Validity:** 代表性而非穷尽方法；只评 parameter-based editing；数据含 GPT 构造字段；自然 prompt 仍是有限模板，资源约束限制 batch。
- **Trade-offs / New Failure Modes:** 更真实评测降低 headline、提高成本和 judge 方差，却暴露 error propagation、stop failure、旧 edit 被覆盖和 locality damage。
- **Where the Previous Design Still Applies:** 研究内部 component diagnosis 可保留 teacher-forced probe，但必须与 deployment-like AR outcome 分开命名；单次低风险 edit 仍可先做窄评测。
- **Evolution Relationship:** `Direct Evolution`：token-local edit probe → deployment-like generation evaluation → sequential state regression gate。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`，handoff `TRAIN-SFT` 与 `PLATFORM-MODEL-REGISTRY`。
- **Target and Adjacent Chapters Read:** 已读 Ch65 resource/scheduler、Ch66 Evaluation、Ch67 Monitoring 的 subject/environment/scorer/decision 边界。
- **Existing Coverage:** Ch66 已把 workload、harness、judge、slice 与 release decision 分开；该论文提供 evaluation leakage 的强受限案例。
- **Integration Decision:** `Books Pending — Refine Existing Argument`。
- **Changed Files or Rejection Reason:** 仅补 W07；所有百分比保持 dataset、model、method、decode 与 edit-count 条件。
- **Open Questions:** 如何建立无 gold-token 泄漏、可重复 judge、长期 edit provenance 与 selective rollback 的生产 release gate？

### I Think, Therefore I Diffuse

- **Candidate / Week / Score:** I Think, Therefore I Diffuse / 2025-W07 / 23/30。
- **Source Family ID:** `arxiv:2502.10458`。
- **Source Type:** Primary multimodal research paper + project page。
- **First-public Date / Revision History:** arXiv v1 2025-02-14；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.10458v1；https://arxiv.org/abs/2502.10458；https://mizhenxing.github.io/ThinkDiff/。
- **Related Primary Sources:** FLUX.1-dev、T5、Qwen2-VL、EVA-CLIP、CoBSAT artifacts referenced by authors。
- **Access and Verification Status:** v1 HTML、Method、实验、ablations、appendix limitations 与 project page 已核验。
- **Full-read Coverage:** 已读 shared feature-space assumption、aligner、LVLM/CLIP branches、random masking、training resources、CoBSAT tables、RMSNorm/input-token ablations、qualitative composition 与 limitations。
- **Original Problem:** reconstruction-based diffusion adapters擅长复制显式视觉条件，却缺少可扩展的 multimodal in-context reasoning supervision。
- **Why the Previous Design Was Reasonable:** 直接用 diffusion reconstruction loss 训练，目标与输出像素/latent 一致，适合 fidelity、editing 与局部控制。
- **Changed Constraint:** reasoning data 稀缺，而一些 diffusion decoder 与 encoder-decoder LLM 共享 T5 encoder input space，可利用文本 proxy task 对齐 VLM features。
- **Mechanism:** 冻结 VLM/LLM/diffusion，仅训练两层 aligner；训练时接 LLM decoder 做文本预测，推理时替换为 diffusion decoder；LVLM 分支随机 mask generated-token features 避免一一映射 shortcut。
- **State Ownership:** source VLM 拥有 multimodal features；aligner 拥有 feature mapping；decoder replacement 依赖共享 encoder-space contract；生成模型仍拥有 image trajectory。
- **Control Flow / Data Flow:** image/text → Qwen2-VL generated features 或 CLIP tokens → aligner → T5 decoder proxy loss；inference 将 T5 decoder 替换为 FLUX/CogVideoX decoder生成。
- **Implementation Details:** aligner 为 Linear-GELU-Linear-RMSNorm，RMSNorm 从 T5 encoder final norm 初始化；仅 aligner 更新；CLIP branch 还拼接 partial caption encoding。
- **Evaluation Contract:** FLUX.1-dev/T5、Qwen2-VL 或 EVA-CLIP；CoBSAT 2-shot/4-shot；LVLM branch 25K steps、global batch 96、4×A100 5h；CLIP branch 100K steps、batch 168、4×A100 一天。
- **Baselines / Ablations / Sensitivity / Overhead:** SEED-LLaMA、Emu、GILL、FLUX API；无 RMSNorm/default init、不 mask、input-token features ablations；CLIP composition 大量为 qualitative evidence。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 4×A100；模型与 batch 如上；precision、inference latency、并发、resolution-normalized cost 与 serving SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在作者 CoBSAT/模型合同内，proxy text alignment 能把特定 VLM feature 映射到共享 decoder input space，且 masking/norm initialization 对结果关键。
- **What It Does Not Prove:** 不证明 feature spaces 天然等价、不证明“reasoning”从 VLM 无损迁移，也不证明 qualitative image/video composition 具有通用 task correctness。
- **Limitations / Threats to Validity:** decoder compatibility 依赖共享 encoder family；CoBSAT 范围窄；fidelity 非重点；需要更强 VLM/data/diffusion；缺端到端 serving contract。
- **Trade-offs / New Failure Modes:** 低成本复用现有模型，新增 feature-scale mismatch、proxy shortcut、decoder incompatibility、隐藏 VLM 错误和多模型版本耦合。
- **Where the Previous Design Still Applies:** fidelity-first editing、decoder不共享表示空间、或能获得直接 reasoning-generation pairs 时，reconstruction/direct diffusion tuning 更清晰。
- **Evolution Relationship:** `Layering / Dependency`：modality representation → proxy alignment → diffusion generation；不是 AR 与 diffusion 的替代关系。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`，handoff `MULTIMODAL-GENERATIVE-PARADIGMS`。
- **Target and Adjacent Chapters Read:** 已读 Ch23 Representation、Ch24 Generative Paradigms、Ch25 World Models，确认本工作止于 representation-to-generator alignment。
- **Existing Coverage:** Ch23 已有 connector shortcut、scale/provenance identity；该论文补充 proxy decoder 与 normalization 的具体受限证据。
- **Integration Decision:** `Books Pending — Refine Existing Argument`。
- **Changed Files or Rejection Reason:** 仅补 W07；不把作者 accuracy 或训练资源跨 resolution/model 外推。
- **Open Questions:** decoder compatibility 如何形成可测 artifact contract，并在 base/VLM/codec 任一 revision 后自动失效？

### ReLearn: Unlearning via Learning for Large Language Models

- **Candidate / Week / Score:** ReLearn / 2025-W07 / 25/30。
- **Source Family ID:** `arxiv:2502.11190`。
- **Source Type:** Primary unlearning paper + official code repository。
- **First-public Date / Revision History:** arXiv v1 2025-02-16；v2 2025-03-20、v3 2025-05-28；W07 结论锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/pdf/2502.11190v1；https://arxiv.org/abs/2502.11190；https://github.com/zjunlp/unlearn。
- **Related Primary Sources:** KnowUnDo Privacy、TOFU、GA、NPO、SURE baselines。
- **Access and Verification Status:** v1 PDF 全文、code identity、metrics、pipeline、robustness、mechanistic probes、hyperparameters 与 limitations 已核验。
- **Full-read Coverage:** 已读 problem/metrics、question-answer augmentation、content verification、generic-data mixing、LoRA training、two datasets/two models、human/general tasks、precision/jailbreak robustness、representation analysis、appendix 与 examples。
- **Original Problem:** 反向优化压低敏感 target probability 时，可能破坏后续 token distribution，获得“忘记”却生成重复或无关文本。
- **Why the Previous Design Was Reasonable:** GA/NPO 直接针对待删除样本，目标明确且不需合成替代知识；retraining-from-scratch 成本过高。
- **Changed Constraint:** 合规系统不仅要 target absence，还要 retention、relevance、fluency 与对 quantization/jailbreak 的稳健性。
- **Mechanism:** 为 forget questions 生成 wording/context/noise/logic variants，再生成 relevant but privacy-free answers，经 LLM content verification 后与 generic instruction data 混合，用正向 cross-entropy/LoRA 学习替代响应。
- **State Ownership:** source forget/retain sets 拥有删除请求 identity；generator/verifier 拥有派生数据 lineage；trainer 产生新 adapter/model；evaluation gate 决定是否满足 forgetting/retention/linguistic contract。
- **Control Flow / Data Flow:** forget QA → question augmentation → privacy-free answer synthesis → content verification → diversification + generic data → LoRA positive training → KFR/KRR/LS + attack/regression evaluation。
- **Implementation Details:** KFR/KRR 结合 entity coverage 与 NLI；LS 汇总词汇/句法/丰富度；关键训练使用 LoRA r=8、alpha=16、dropout=0.1。
- **Evaluation Contract:** Llama-2-7B-chat、Gemma-2-2B-it；KnowUnDo Privacy、TOFU；GA/NPO及正则变体；MMLU/GSM8K、人评、precision/jailbreak 与 mechanistic analysis。
- **Baselines / Ablations / Sensitivity / Overhead:** 多种 GA/NPO retain losses、SURE、ReLearn；报告不同模型/数据、precision 与 attack；未提供 retrain-from-scratch 的严格 gold equivalence。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** single A100 40GB；ReLearn lr/epoch 随数据表变化，batch 1、accumulation 4；线上并发、latency/SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在两个 synthetic/public unlearning contracts 中，正向替代训练比所测 reverse baselines 更好平衡 target forgetting、retention 与语言质量。
- **What It Does Not Prove:** 不证明参数中目标信息已被不可恢复地删除，不等于法律层面的 certified deletion，也不覆盖所有 extraction attacks。
- **Limitations / Threats to Validity:** 合成数据与 LLM verifier 可引入新风险；metrics 对细微知识不敏感；缺理论保证、retraining oracle 和大规模 production evidence。
- **Trade-offs / New Failure Modes:** 保存语言能力，付出合成/审核成本、新隐私泄漏、vague-answer policy bias、metric gaming 与 source-to-derived deletion propagation。
- **Where the Previous Design Still Applies:** 可完整重训的小模型/高风险删除应优先 retrain；目标窄且有强攻击评测时 reverse optimization 仍可作对照而非唯一门槛。
- **Evolution Relationship:** `Alternative Branch`：reverse suppression ↔ positive replacement learning；二者都必须受 certified evidence 与 retention gate 约束。
- **ROADMAP Node:** `PLATFORM-SECURITY`，handoff `TRAIN-SFT`、`TRAIN-LORA` 与 `PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读 Ch71 Multi-tenancy、Ch72 Security、Ch73 Production Best Practice，并回读 Ch29/30 的 objective 与 adapter边界。
- **Existing Coverage:** Security 已区分 deletion request、derived artifacts 与验证；该论文补充 response-quality-preserving unlearning 分支，但不能升级为 certified deletion。
- **Integration Decision:** `Books Pending — Refine Existing Argument`。
- **Changed Files or Rejection Reason:** 仅补 W07；不把 KFR/KRR 当作不可恢复删除证明。
- **Open Questions:** 如何用独立 attacker、retraining oracle、artifact lineage 与 legal policy 建立可审计 deletion certificate？

### How Do LLMs Acquire New Knowledge? A Knowledge Circuits Perspective on Continual Pre-Training

- **Candidate / Week / Score:** Knowledge Circuits for Continual Pre-Training / 2025-W07 / 24/30。
- **Source Family ID:** `arxiv:2502.11196`。
- **Source Type:** Primary mechanistic-interpretability research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-16；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.11196v1；https://arxiv.org/abs/2502.11196。
- **Related Primary Sources:** cited EAP/circuit-discovery methods and synthetic factual-knowledge construction。
- **Access and Verification Status:** v1 HTML 全文、equations、training setup、circuit metrics、appendices、forgetting analysis 与 limitations 已核验。
- **Full-read Coverage:** 已读 background、synthetic dataset、continual-pretraining setup、circuit discovery、performance/topology/components analyses、whole-model transfer、head identification、forgetting/replay 与 limitations。
- **Original Problem:** 行为评测能看到新事实是否学会，却不能说明训练过程中哪些 component cooperation 形成、稳定或重组。
- **Why the Previous Design Was Reasonable:** checkpoint accuracy/loss 便宜、可扩展，对生产训练监控足够；完整 circuit discovery 计算昂贵且解释依赖方法假设。
- **Changed Constraint:** 若要推断 curriculum、forgetting 或知识编辑机制，需要观察中间 checkpoints 的计算子图，而非只看终局 probe。
- **Mechanism:** 在 synthetic subject-relation-attribute 数据上 continual pretrain，小模型每个 checkpoint 用 edge-attribution/circuit discovery 得到 sparse subgraph，再跟踪 Hit@10、edge/node Jaccard、centralization、head roles 与 layer evolution。
- **State Ownership:** training run 拥有 checkpoint/data order；discovery method 产生派生 circuit identity；circuit 不是模型内显式存储对象，必须绑定 threshold、task 与 checkpoint。
- **Control Flow / Data Flow:** synthetic facts/frequencies → continual pretraining checkpoints → clean/corrupt factual-recall pairs → edge attribution/sparse circuit → topology/component metrics → forgetting/replay comparison。
- **Implementation Details:** GPT-2 Small/Medium、TinyLlama-1.1B、Phi-1.5；constant LR/AdamW；专门 attention head 用 DLA source-token ratio threshold 分类；replay实验跟踪旧 circuit edge变化。
- **Evaluation Contract:** synthetic biographies、city/major/company factual recall；不同 relevant/complete knowledge 与frequency；Hit@10、Jaccard、centralization、DLA；全部训练在2×A100。
- **Baselines / Ablations / Sensitivity / Overhead:** 对 whole-model behavior、不同知识相关性/频率、模型 family/scale、topology alignment 与 replay intervention；原 specialized-head code unavailable，作者自行 reimplementation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 2×A100；124M/355M/1.1B/1.3B；block 1024/2048、batch 32/16/4/2；precision、wall-clock 和 production SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在受控 synthetic factual recall 中，作者发现相关知识学得更快，circuit topology 呈 formation→optimization shift，并观察 deep-to-shallow component pattern。
- **What It Does Not Prove:** 不证明同一电路演进适用于互联网规模、多模态、instruction/RL 训练或真实事实；circuit 是方法依赖的派生解释。
- **Limitations / Threats to Validity:** 小模型、decoder-only、synthetic triples、单一 next-token continual-pretraining technique；threshold与discovery approximation影响结论；无原 specialized-head code。
- **Trade-offs / New Failure Modes:** 中间机制可见性换来巨大分析成本、threshold instability、false circuit identity 与将相关性误写为因果规律的风险。
- **Where the Previous Design Still Applies:** 大规模训练的默认控制仍以 loss、held-out behavior、data lineage 和 regression 为主；circuit analysis 适合受控诊断而非在线 release oracle。
- **Evolution Relationship:** `Explanatory Analogy`：behavior-only checkpoint monitoring → circuit-level diagnostic evidence；不是新的 training runtime。
- **ROADMAP Node:** `TRAIN-PRETRAINING`，handoff `PLATFORM-EVALUATION-SYSTEM` 与 model interpretability evidence ladder。
- **Target and Adjacent Chapters Read:** 已读 Ch27 Data、Ch28 Pretraining、Ch29 SFT，确认本工作只支持受控 continual-pretraining 诊断，不改变通用 objective。
- **Existing Coverage:** Pretraining 已区分 loss、知识与能力；该论文补中间 checkpoint/circuit 证据，但不支持普适知识存储论。
- **Integration Decision:** `Books Pending — No Change or Review-note Evidence`。
- **Changed Files or Rejection Reason:** 仅补 W07；不把 formation/optimization phase shift 外推为大模型定律。
- **Open Questions:** circuit identity 在随机种子、data order、规模与 discovery threshold 改变时是否稳定，并能否预测真实 forgetting 而非事后解释？

### IHEval: Evaluating Language Models on Following the Instruction Hierarchy

- **Candidate / Week / Score:** IHEval / 2025-W07 / 26/30。
- **Source Family ID:** `arxiv:2502.08745`。
- **Source Type:** Primary benchmark research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-12；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.08745v1；https://arxiv.org/abs/2502.08745。
- **Related Primary Sources:** IFEval、TensorTrust、OpenAI instruction hierarchy work 与 benchmark task sources。
- **Access and Verification Status:** v1 HTML 全文、task cards、evaluation criteria、完整结果与数据构造 appendix 已核验。
- **Full-read Coverage:** 已读 metadata、introduction、related work、definition、三种设置、九项任务、difficulty、programmatic evaluator、13 模型实验、prompt/scale/conflict analyses、appendices 与 conclusion。
- **Original Problem:** 单输入 instruction-following 分数不能判断模型在 system、user、history 与 tool output 冲突时是否遵循优先级。
- **Why the Previous Design Was Reasonable:** 单输入 benchmark 更容易构造和自动评分；早期应用也较少同时暴露多种 provenance 的输入。
- **Changed Constraint:** Agent 与 tool-augmented application 把不可信外部内容和高优先级 policy 放入同一上下文，instruction conflict 成为安全与一致性问题。
- **Mechanism:** 对同一底层任务构造 reference、aligned、conflict 三种输入，并在 rule following、task execution、safety defense、tool use 四类九项任务中比较主 instruction 的完成度。
- **State Ownership:** benchmark 拥有 task/priority label；application runtime 应拥有 authenticated provenance 与 authorization；模型只生成响应，不能成为 priority 的唯一 authority。
- **Control Flow / Data Flow:** source task → 拆分不同 provenance instruction → 生成 aligned/conflict variant → deterministic decode → strict/loose programmatic scoring → 与 reference delta 比较。
- **Implementation Details:** 3,538 examples；Claude 辅助生成的 rule-following 消息全部人工复核；tool use 同时覆盖 intrinsic 与 injected conflicting instruction。
- **Evaluation Contract:** 13 个 GPT、Claude、LLaMA、Mistral、Qwen 模型；temperature 0；最终分数跨 difficulty，并在适用任务跨 strict/loose metric 平均。
- **Baselines / Ablations / Sensitivity / Overhead:** reference/aligned/conflict 对照、模型规模、instruction strictness、显式 hierarchy prompting、不同 conflict pair；未报告训练 intervention 或部署成本。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型版本已披露；provider hardware、precision、context length、batch、concurrency 与 production SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在该 benchmark 和被测版本中，hierarchical conflict 显著降低主 instruction 完成度，且显式提示优先级没有稳定消除问题。
- **What It Does Not Prove:** 不证明模型 failure 等同于真实 breach，也不证明固定文本层级足以实现 runtime authorization 或 prompt-injection 防御。
- **Limitations / Threats to Validity:** safety task 为模拟场景；programmatic metric 可能漏掉语义正确输出；任务构造与固定 priority contract 限制外部有效性；没有提出或验证解决机制。
- **Trade-offs / New Failure Modes:** 可复现、低成本的 conflict probe 换来简化 provenance、policy 与环境；若把 benchmark priority 当真实 authority，会掩盖身份认证和 effect-time authorization。
- **Where the Previous Design Still Applies:** 单输入 evaluation 仍适合隔离基础 task capability；无多来源输入的受控 pipeline 不需要完整 hierarchy suite。
- **Evolution Relationship:** `Layering / Dependency`：instruction following → provenance-aware conflict evaluation → authenticated runtime policy gate；benchmark 只覆盖中间证据层。
- **ROADMAP Node:** `PLATFORM-SECURITY`，handoff `PLATFORM-EVALUATION-SYSTEM` 与 `AGENT-TOOL-CALLING`。
- **Target and Adjacent Chapters Read:** 已读 Ch71 Multi-tenancy、Ch72 Security、Ch73 Production Best Practice，并回读 Ch66 Evaluation 与 Ch78 Tool Calling。
- **Existing Coverage:** Security 已要求 authenticated instruction provenance，Evaluation 已分离 model、runtime 与 outcome；IHEval 提供 model-level conflict probe，但不改变 runtime authority 结论。
- **Integration Decision:** `Books Pending — Refine Existing Argument`。
- **Changed Files or Rejection Reason:** 仅补 W07；不把 48% 等作者结果外推到其他模型版本或生产安全率。
- **Open Questions:** 如何把 benchmark priority 与 cryptographic identity、tool trust label、policy version 和 effect-time authorization 联合为可执行 evaluation contract？

### Talk Structurally, Act Hierarchically: A Collaborative Framework for LLM Multi-Agent Systems

- **Candidate / Week / Score:** Talk Structurally, Act Hierarchically / 2025-W07 / 22/30。
- **Source Family ID:** `arxiv:2502.11098`。
- **Source Type:** Primary multi-agent research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-16；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.11098v1；https://arxiv.org/abs/2502.11098。
- **Related Primary Sources:** ReAct、AutoGPT、AgentVerse、GPTSwarm、AgentPrune 与 OKG comparison sources。
- **Access and Verification Status:** v1 HTML 全文、formalization、algorithms、experiments、ablations、API-cost tables 与 appendices 已核验。
- **Full-read Coverage:** 已读 communication graph、agent/team definition、structured message、hierarchical teams、generator-evaluator-revisor loop、datasets、baselines、ablations、cost 与 limitations boundary。
- **Original Problem:** flat natural-language collaboration 容易丢失 task background、中间结果与 responsibility，复杂任务还会让所有 Agent 在同一通信平面相互干扰。
- **Why the Previous Design Was Reasonable:** 小团队、短任务和低并发下，flat broadcast/round-robin 易实现，也避免 hierarchy 带来的 supervisor bottleneck。
- **Changed Constraint:** task decomposition 和 specialist role 增加后，需要限制通信范围、保留结构化上下文，并把局部结果逐级汇总。
- **Mechanism:** 为 Agent 配置 role/plugins/memory，以 message、background、intermediate output 结构化传递信息；用 nested team 与 supervisor 组织 generator、evaluator、summary、threshold 和 revisor 的迭代。
- **State Ownership:** Agent memory 属于各 Agent；team supervisor 聚合局部输出；外部 runtime 仍应拥有 shared task state、iteration budget 与 terminal decision。
- **Control Flow / Data Flow:** task → hierarchical team assignment → structured messages → specialist outputs → evaluator-team review → supervisor summary/threshold → revise or terminate。
- **Implementation Details:** 使用固定 communication graph 与按任务触发的 communication event；主实验以 GPT-4o 为 backbone、temperature 0，o1-preview 使用 temperature 1。
- **Evaluation Contract:** MMLU 五领域、WikiQA 与 camera ad headline generation；比较 correctness/quality、token/API cost 和多种 agent framework。
- **Baselines / Ablations / Sensitivity / Overhead:** GPT-4o voting、o1-preview、ReAct、AutoGPT、AgentVerse、GPTSwarm、AgentPrune、OKG；移除 evaluation supervisor/team、改普通通信以及删除 message components 的 ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** API model/version 与部分 token/cost 披露；provider hardware、precision、真实并发、tail latency 与 workflow SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在作者任务与预算设置中，structured messages 和 hierarchical evaluation loop 对若干质量指标有正向贡献，并显式暴露显著 token/API cost。
- **What It Does Not Prove:** 不证明 hierarchy 普遍优于单 Agent、flat team 或 majority voting，也不证明收益在等成本、真实共享状态与失败恢复下成立。
- **Limitations / Threats to Validity:** task set 窄且多为静态 benchmark；共享环境、副作用、权限、crash recovery 和 adversarial agent 未被系统评估；同源模型错误高度相关。
- **Trade-offs / New Failure Modes:** 更清晰的责任与局部聚合换来 supervisor bottleneck、summary loss、communication tax、共享错误放大和更高成本。
- **Where the Previous Design Still Applies:** 单 Agent headroom 足够、任务不可独立分解或消息成本超过并行收益时，单 Agent/flat coordination 仍更合理。
- **Evolution Relationship:** `Alternative Branch`：flat collaboration ↔ hierarchical team；不是 Agent 数量增加后的必然下一代。
- **ROADMAP Node:** `AGENT-MULTI-AGENT`，handoff `AGENT-WORKFLOW`、`AGENT-REFLECTION` 与 `AGENT-MEMORY`。
- **Target and Adjacent Chapters Read:** 已读 Ch80 Reflection、Ch81 Workflow、Ch82 Multi-Agent、Ch83 MCP，核对 feedback、durable state、topology 与 protocol owner。
- **Existing Coverage:** Multi-Agent 已要求 single-agent baseline、coordination tax、message/state 分离和 aggregation evidence；论文是结构化 hierarchy 的受限案例，不构成新通用结论。
- **Integration Decision:** `Books Pending — No Change or Review-note Evidence`。
- **Changed Files or Rejection Reason:** 仅补 W07；不把 benchmark improvement 写成 multi-agent scaling law。
- **Open Questions:** 在相同 token、wall-clock 与 verifier budget 下，hierarchy 何时跨过 supervisor bottleneck，并如何恢复被 summary 丢失的 evidence provenance？

### Dyve: Thinking Fast and Slow for Dynamic Process Verification

- **Candidate / Week / Score:** Dyve / 2025-W07 / 25/30。
- **Source Family ID:** `arxiv:2502.11157`。
- **Source Type:** Primary verifier research paper with public code/data/model artifacts。
- **First-public Date / Revision History:** arXiv v1 2025-02-16；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.11157v1；https://arxiv.org/abs/2502.11157。
- **Related Primary Sources:** ProcessBench、OmegaPRM、Math-Shepherd、RLHFlow 与 released Dyve artifacts。
- **Access and Verification Status:** v1 HTML 全文、data pipeline、training、ProcessBench/Best-of-N experiments、appendix 与 artifact links 已核验。
- **Full-read Coverage:** 已读 process-verification formulation、System 1/2 routing、step labels、1.2M noisy rollout filtering、117K training set、evaluation、ablation、hardware 与 limitations。
- **Original Problem:** 固定短 verifier 对难推理不足，固定长 chain-of-thought verifier 又把成本和错误机会施加到每个候选步骤。
- **Why the Previous Design Was Reasonable:** uniform verifier 简单、batchable，且在单一难度分布下容易校准和部署。
- **Changed Constraint:** step difficulty 和 error ambiguity 高度不均，verification budget 应按需要分配而非固定展开。
- **Mechanism:** verifier 对每个 step 动态选择直接 System 1 判断或最长 8192-token 的 System 2 analysis，并在检测到首个错误时停止。
- **State Ownership:** verifier runtime 拥有 step cursor、mode 与 stop decision；generator 拥有 candidate trajectory；最终 acceptance gate 不能由 verifier 的自然语言解释单独拥有。
- **Control Flow / Data Flow:** math query → candidate rollout → step-wise verifier → dynamic fast/slow route → first-error label or final-correct label → ProcessBench/Best-of-N selection。
- **Implementation Details:** 从约 15K GSM8K/MATH query 各采样 20 trajectories，汇合约 1.2M noisy rollouts，经 DeepSeek-V3 judge 过滤/平衡为约 117K examples；排除 PRM800K 以降低泄漏。
- **Evaluation Contract:** ProcessBench 3,400 cases，覆盖 GSM8K、MATH、OlympiadBench、OmniMATH；以 correct/erroneous accuracy 的 harmonic F1 评估，并在 MATH-500 做 Best-of-N。
- **Baselines / Ablations / Sensitivity / Overhead:** outcome/process reward/verifier baselines、fast-only/slow-only/dynamic 分支与 routing/data ablations；MATH-500 outcome 因工具不一致由作者人工复核。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8×A800-SXM4-80GB；responses 1–8192 tokens；训练/推理 precision、production batch/concurrency、tail-latency SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在作者 math process benchmarks 中，动态分配 reasoning tokens 的 verifier 在所测 accuracy-cost 边界优于固定分支，并能用于 Best-of-N ranking。
- **What It Does Not Prove:** 不证明 verifier 是 correctness oracle，也不证明数学上的 first-error detection 能迁移到 tool/environment workflow 或高风险 release gate。
- **Limitations / Threats to Validity:** 自动 judge label 仍有噪声；难度和数据多样性有限；manual outcome correction 降低纯自动复现性；routing error 会同时浪费预算和错过关键步骤。
- **Trade-offs / New Failure Modes:** 按难度节省平均成本，代价是 route calibration、variable latency、judge contamination、step-boundary dependency 与 slow-path tail amplification。
- **Where the Previous Design Still Applies:** deterministic tests、短解答或风险要求一致 exhaustive verification 时，固定 verifier 更简单可靠。
- **Evolution Relationship:** `Direct Evolution`：uniform process verifier → budget-aware fast/slow verifier → 仍需 external acceptance authority。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-REFLECTION` 与 `INFER-SCHEDULING`。
- **Target and Adjacent Chapters Read:** 已读 Ch65 Observability、Ch66 Evaluation、Ch67 AI Cost，并回读 Ch80 Reflection 与 Ch56 Scheduling。
- **Existing Coverage:** Evaluation 已把 judge 写成有预算的 evidence-acquisition policy；Dyve 提供 step-level routing 案例，不改变 scorer 非绝对真相的结论。
- **Integration Decision:** `Books Pending — Refine Existing Argument`。
- **Changed Files or Rejection Reason:** 仅补 W07；作者 math benchmark 不外推为通用 Agent verifier contract。
- **Open Questions:** route uncertainty 如何校准，fast/slow verifier 如何共享 batch，并如何把 variable verification latency 纳入 end-to-end SLO 与 false-accept budget？

### CALM: A Unified Conversational Agentic Language Model

- **Candidate / Week / Score:** CALM / 2025-W07 / 24/30。
- **Source Family ID:** `arxiv:2502.08820`。
- **Source Type:** Primary instruction-tuning research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-12；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.08820v1；https://arxiv.org/abs/2502.08820。
- **Related Primary Sources:** SNIPS、Hammer、ToolAce、MultiWOZ 2.4、API-Bank 与 BFCL V3 source families。
- **Access and Verification Status:** v1 HTML 全文、data construction、objectives、training setup、benchmarks、ablations 与 appendix 已核验。
- **Full-read Coverage:** 已读 TOD/LA problem framing、CALM-IT mixture、CRA/ReAct generation、action/response objectives、LoRA/QLoRA training、three benchmark evaluations、ablations 与 conclusion。
- **Original Problem:** task-oriented dialogue 擅长多轮 state tracking 但受限于预定义 API，language agent 擅长 function calling 却常忽略长对话状态与自然响应。
- **Why the Previous Design Was Reasonable:** 分开训练便于使用各自成熟数据和 metric，也减少 objective/data interference。
- **Changed Constraint:** 真实 assistant 同时需要对话状态、工具动作和用户可读响应，单一 specialized dataset 无法覆盖完整 interaction contract。
- **Mechanism:** CALM-IT 交织 dialogue state tracking、single/multi-turn API call 与 conversational ReAct data，并联合训练 action prediction 和 response generation。
- **State Ownership:** training data 定义可学习 interaction prior；模型生成 belief/action/response；runtime 仍拥有真实 conversation state、tool authorization、effect receipt 与 recovery。
- **Control Flow / Data Flow:** SNIPS/Hammer/ToolAce/生成 CRA 数据 → 311,583-sample mixture → LoRA/QLoRA fine-tuning → state/action/response decode → MultiWOZ/API-Bank/BFCL evaluation。
- **Implementation Details:** mixture 包含 13,028 SNIPS、13,819 Hammer、202,500 ToolAce 与 82,236 generated CRA/ReAct samples，共约 211M tokens；Llama 3.1 8B、3.3 70B、3.1 405B。
- **Evaluation Contract:** MultiWOZ 2.4（999 test，Success/JGA）、API-Bank（314 dialogues、753 API calls）和 BFCL V3（1800+ items，AST/executable accuracy）。
- **Baselines / Ablations / Sensitivity / Overhead:** specialized TOD/LA baselines、不同 model scale、移除 DST 或 CRA data 的 ablation；部分专项 metric 在移除广泛 mixture 后反而提高，暴露 objective interference。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8×H100；8B/70B 为 bf16 LoRA r16 alpha32、batch 8、3 epochs、lr 1e-4，约 8h/60h；405B 为 nf4 QLoRA 一 epoch；serving concurrency/SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在三套 benchmark 中，联合 data mixture 可让同一模型兼顾部分 multi-turn dialogue 与 function-calling 指标，并显示不同 mixture component 的贡献与冲突。
- **What It Does Not Prove:** 不证明统一模型掌握真实 tool state、authorization、idempotency 或 side-effect recovery，也不证明一种 mixture 对所有 API/domain 最优。
- **Limitations / Threats to Validity:** generated CRA data 继承 teacher bias；benchmark 环境有限；multi-turn function calling 仍低；405B recipe 与较小模型不完全可比；论文没有独立 formal limitations section。
- **Trade-offs / New Failure Modes:** 统一 interaction prior 减少 model handoff，却增加 data mixture interference、格式耦合、过时 API knowledge 和 runtime/model state confusion。
- **Where the Previous Design Still Applies:** API 固定、风险高或 dialogue/tool owner 明确分离时，specialized model 或 deterministic workflow 仍更易审计。
- **Evolution Relationship:** `Layering / Dependency`：separate TOD/LA specialization → joint interaction training → runtime authorization and durable workflow 仍独立存在。
- **ROADMAP Node:** `TRAIN-SFT`，handoff `AGENT-CONTEXT`、`AGENT-TOOL-CALLING` 与 `AGENT-WORKFLOW`。
- **Target and Adjacent Chapters Read:** 已读 Ch28 Pretraining、Ch29 SFT、Ch30 LoRA，并回读 Ch76 Context、Ch78 Tool Calling 与 Ch81 Workflow。
- **Existing Coverage:** SFT 已将 demonstration distribution 与 runtime contract 分离；CALM 强化 mixture/objective 分支，但不支持把 learned action 当已执行 action。
- **Integration Decision:** `Books Pending — Refine Existing Argument`。
- **Changed Files or Rejection Reason:** 仅补 W07；不把 benchmark Success/AST accuracy 外推为生产 Agent reliability。
- **Open Questions:** 如何同时版本化 dialogue state、API schema、training mixture 与 runtime receipts，并在 mixture conflict 下选择 task-specific stopping point？

### SURGE: On the Potential of Large Language Models as General-Purpose Surrogate Code Executors

- **Candidate / Week / Score:** SURGE / 2025-W07 / 25/30。
- **Source Family ID:** `arxiv:2502.11167`。
- **Source Type:** Primary benchmark research paper with released code/dataset。
- **First-public Date / Revision History:** arXiv v1 2025-02-16；v2 2025-03-03、v3 2025-04-03、v4 2025-09-28、v5 2026-05-25；W07 只使用 v1。
- **Direct Primary Sources:** https://arxiv.org/pdf/2502.11167v1；https://arxiv.org/abs/2502.11167；https://github.com/Imbernoulli/SURGE。
- **Related Primary Sources:** McEval、DebugBench、LeanWorkbook、Goedel-Prover 与 benchmark input repositories。
- **Access and Verification Status:** v1 PDF 17 页、dataset construction、metrics、model tables、analysis、appendices 与 event-time artifact identity 已核验；原 HTML transport blocker 已解除。
- **Full-read Coverage:** 已读 metadata/revision、introduction、related work、八类 dataset pipeline、evaluation metrics、14 模型三种 prompting setting、runtime correlation、error analysis、conclusion 与 task appendices。
- **Original Problem:** code-generation benchmark 不能回答模型能否在不执行程序时预测 output、error 或 compiler/environment-dependent behavior。
- **Why the Previous Design Was Reasonable:** 真实 execution、compiler 或 proof checker 提供强 ground truth；传统 surrogate 只在狭窄数值 workload 内建模，边界更清楚。
- **Changed Constraint:** 执行可能昂贵、危险、超时或依赖不可用环境，因而需要测量 LLM 是否可作为有误差的 cheap proxy。
- **Mechanism:** 构建 multi-language、competition、repository、scientific computing、time-consuming、buggy、differential environment 与 Lean proof 八类 1,160 项任务，让模型直接预测执行结果，再按任务特定 metric 与真实执行对比。
- **State Ownership:** executable artifact、compiler/runtime config 与 ground truth 属于 harness；模型只拥有 prediction；release/verification gate 不能把 prediction 升格为 execution receipt。
- **Control Flow / Data Flow:** source problem/repository → executable refactor/manual validation → versioned execution environment → ground-truth output/error → model prediction under prompt setting → task-specific scorer/error taxonomy。
- **Implementation Details:** ML/CL/BG 由 LLM 辅助补全后人工与真实执行检查；RL 含 60 项、DR 含 200 项，其余每类 150 项；BG 对无限循环使用 30 秒过滤。
- **Evaluation Contract:** 10 个 open-weight 与 4 个 closed model；0-shot direct、0-shot CoT、few-shot CoT；temperature 0；exact match、edit/similarity、RAE、rank correlation、Jaccard 等按 subset 选择。
- **Baselines / Ablations / Sensitivity / Overhead:** chat/code、模型规模、direct/CoT/few-shot、真实 runtime bucket 与人工核验 error categories；v1 仅给 formal-language scale trend，未给完整训练 recipe 或独立重复实验。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型版本和部分 context-bound repository 条件披露；evaluation/training hardware、precision、batch、并发、API latency/SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在 v1 SURGE tasks 中，模型表现随 task 类型显著变化，真实执行越长的 TC 样本越难，且 CoT/few-shot 在所测配置中通常提高 proxy accuracy。
- **What It Does Not Prove:** 不证明 LLM 可以安全替代 execution、compiler、test 或 theorem prover，也不证明 runtime 与难度存在因果关系或 scale 最终可消除误差。
- **Limitations / Threats to Validity:** v1 没有正式 limitations section；仅 1,160 项且多由作者/LLM 重构；metric heterogeneous；closed model 不可复现；环境、prompt 和后续 revision 会改变结果。
- **Trade-offs / New Failure Modes:** cheap/no-execution prediction 换来 silent false positive、environment hallucination、distribution shift 和把高置信解释误当 receipt 的风险。
- **Where the Previous Design Still Applies:** 只要程序可在 sandbox 中可靠运行，真实 execution 仍是 default oracle；surrogate 更适合排序、triage 或决定执行预算。
- **Evolution Relationship:** `Layering / Dependency`：static code understanding → execution-outcome proxy → sandbox/verified execution gate；proxy 不替代 ground truth。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-TOOL-CALLING`、`AGENT-REFLECTION` 与 `PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读 Ch65 Observability、Ch66 Evaluation、Ch67 AI Cost，并回读 Ch72 Security、Ch78 Tool Calling 与 Ch80 Reflection。
- **Existing Coverage:** Evaluation 已要求 executable evidence 与 artifact/environment identity；SURGE 扩展 proxy capability 的分布画像，但不改变 execution receipt 的 authority。
- **Integration Decision:** `Books Pending — Refine Existing Argument`。
- **Changed Files or Rejection Reason:** 仅补 W07；v2-v5 的后续变化不反填 v1，作者平均分不外推为部署可靠性。
- **Open Questions:** 如何把 surrogate uncertainty 校准为 execution-budget policy，并防止 attacker 利用 false accept 绕过 sandbox 与 proof checker？

### EQ-VAE: Equivariance Regularized Latent Space for Improved Generative Image Modeling

- **Candidate / Week / Score:** EQ-VAE / 2025-W07 / 25/30。
- **Source Family ID:** `arxiv:2502.09509`。
- **Source Type:** Primary multimodal generative-model research paper with code/project artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-13；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.09509v1；https://arxiv.org/abs/2502.09509；https://eq-vae.github.io/。
- **Related Primary Sources:** SD-VAE/SDXL-VAE/SD3-VAE、VQ-GAN、DiT、SiT、REPA 与 MaskGIT source families。
- **Access and Verification Status:** v1 HTML 全文、equations、continuous/discrete extension、implementation、generative comparisons 与 transformation ablations 已核验。
- **Full-read Coverage:** 已读 latent-model framing、related work、equivariance definition、explicit-collapse failure、implicit objective、transform design、five-epoch fine-tuning、DiT/SiT/REPA/MaskGIT evaluation 与 ablations。
- **Original Problem:** latent autoencoder 只优化 reconstruction/regularization 时，旋转或缩放后的语义相近 image 可能映射到结构复杂且不等变的 latent，使第二阶段 generator 学习额外几何。
- **Why the Previous Design Was Reasonable:** KL/codebook regularization 和 reconstruction loss 直接控制容量与保真度，兼容成熟 latent diffusion pipeline。
- **Changed Constraint:** 第二阶段 generator 的 convergence 也取决于 latent geometry，单看 reconstruction quality 无法衡量表示是否易学。
- **Mechanism:** 对 input image 编码后在 latent 上施加 scale/rotation，再让 decoder 重建对应变换后的 image；用 reconstruction/adversarial supervision 隐式约束 equivariance，并以概率保留 identity transform 防止损失原 reconstruction。
- **State Ownership:** autoencoder checkpoint 拥有 latent coordinate contract；generator checkpoint 依赖该 contract；artifact registry 必须把 encoder/decoder revision 与 downstream generator 绑定。
- **Control Flow / Data Flow:** image → encoder → sampled latent transform → decoder → transformed-image reconstruction/adversarial loss → fine-tuned latent codec → downstream generative training。
- **Implementation Details:** OpenImages 上 fine-tune autoencoder 5 epochs、batch 10；默认 identity probability 0.5，scale 0.25–1 和 90-degree rotations；continuous 与 pre-quantization discrete features 均测试。
- **Evaluation Contract:** ImageNet 256×256；DiT/SiT/REPA batch 256，MaskGIT 300 epochs；以 rFID、gFID、sFID、IS、precision/recall、equivariance error 和 intrinsic dimension 比较。
- **Baselines / Ablations / Sensitivity / Overhead:** 多个 VAE/VQ-GAN、DiT/SiT/REPA/MaskGIT；rotation、isotropic/anisotropic scale、组合 transform 和 regularization strength；作者报告 training-step/epoch convergence 对比。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** image/model/batch/epoch 已披露；训练 accelerator、precision、wall-clock、serving batch/concurrency 与 SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在所测 image datasets 和 latent generators 中，equivariance regularization 改善 latent transform consistency，并在相同 pipeline 下减少达到若干 FID 水平所需训练步数。
- **What It Does Not Prove:** 不证明所有 semantic transformation 都应等变，不证明作者的“7×”跨 hardware/optimizer 可复现，也不证明生成 quality 只由 latent geometry 决定。
- **Limitations / Threats to Validity:** 没有正式 limitations section；只测 2D scale/rotation 与 ImageNet/OpenImages；FID 不是完整 perceptual contract；anisotropic scale 已显示 reconstruction trade-off。
- **Trade-offs / New Failure Modes:** 更易学的 latent geometry 换来 codec fine-tune、transform bias、artifact incompatibility 和错误 symmetry 假设；过强约束可损害细节。
- **Where the Previous Design Still Applies:** domain transformation 不具语义保持性、codec 已冻结认证或 generator 不受 latent geometry 限制时，标准 reconstruction/KL/codebook objective 仍更稳妥。
- **Evolution Relationship:** `Direct Evolution`：compress-and-reconstruct latent → geometry-aware latent contract → downstream generator co-design。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`，handoff `MULTIMODAL-GENERATIVE-PARADIGMS` 与 `TRAIN-PRETRAINING`。
- **Target and Adjacent Chapters Read:** 已读 Ch23 Multimodal Representation、Ch24 Generative Paradigms、Ch25 World Models，并回读 Ch27 Data 与 Ch28 Pretraining。
- **Existing Coverage:** Ch23 已强调 representation identity 与 modality contract；EQ-VAE 增加 symmetry/learnability 案例，不足以建立通用 transformation policy。
- **Integration Decision:** `Books Pending — Refine Existing Argument`。
- **Changed Files or Rejection Reason:** 仅补 W07；所有 speedup 保留作者的 image/model/epoch 条件，不写成通用训练加速。
- **Open Questions:** codec revision 如何与 generator checkpoint、sampling pipeline 和 rollback 绑定，并如何为不同 domain 学习而非手工指定等变群？

### CounterMATH: Counterexample-Driven Conceptual Reasoning in Mathematical LLMs

- **Candidate / Week / Score:** Counterexample-Driven Conceptual Reasoning / 2025-W07 / 22/30。
- **Source Family ID:** `arxiv:2502.10454`。
- **Source Type:** Primary benchmark and instruction-tuning research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-12；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.10454v1；https://arxiv.org/abs/2502.10454。
- **Related Primary Sources:** Counterexamples in Real Analysis/Functional Analysis/Topology textbooks、ProofNet、NaturalProof、MATH 与 GSM8K。
- **Access and Verification Status:** v1 HTML 全文、data curation、prompts、judge validation、SFT pipeline、OOD evaluation 与 appendices 已核验。
- **Full-read Coverage:** 已读 benchmark motivation、1,216-item construction、baseline/model prompts、F1/example metrics、100-case human check、1,025-sample training-data pipeline、SFT/OOD results、token analysis 与 appendices。
- **Original Problem:** 常规数学 benchmark 偏向计算或已见 proof pattern，不能单独判断模型能否用 counterexample 识别概念边界。
- **Why the Previous Design Was Reasonable:** arithmetic/competition tasks 易自动评分，并对许多实际 math workload 有直接价值；形式化 prover 则提供强 correctness。
- **Changed Constraint:** 大学数学中的概念理解需要构造反例和解释 theorem condition，final numeric answer 隐藏这种 failure。
- **Mechanism:** 从四类中文数学教材提取 statement-rationale pair，专家核验并翻译为 1,216-item CounterMATH；再从 30K+ proof data 过滤/改写 1,025 个 counterexample samples 对 Qwen2.5-Math-7B 做 SFT。
- **State Ownership:** dataset curator 拥有 statement/reference identity；GPT-4o judge 只产生派生 score；formal or expert verification 才能拥有高风险 proof correctness。
- **Control Flow / Data Flow:** textbook/OCR → expert label/filter → supervised translation validation → model response → lexical + judge metric；training branch为 proof corpus → judge filter/refine → SFT → CounterMATH/OOD evaluation。
- **Implementation Details:** vendor annotators抽取 1,274 pairs，作者数学背景专家保留 1,216；GPT-4o 翻译后再审核；judge 对 100 samples 的 extraction/alignment 与人工比较。
- **Evaluation Contract:** 多个 7B–70B+ open/closed math models；default CoT/hint prompt；macro F1、example proportion、strict/loose alignment；SFT 后测 CounterMATH、MATH、GSM8K。
- **Baselines / Ablations / Sensitivity / Overhead:** base models、hint prompt、ICL observation、SFT、OOD；没有等算力多 seed、formal proof checker 或独立 dataset replication。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model family 与 dataset size 已披露；SFT hardware、precision、sequence length、batch、wall-clock、serving SLO Not Disclosed。
- **What the Evidence Actually Proves:** CounterMATH 揭示被测模型在反例构造上的差异；少量专门 SFT 在作者 benchmark 和所测 MATH/GSM8K 设置中改变若干指标。
- **What It Does Not Prove:** 不证明模型真正掌握抽象概念，不证明 OOD gain 来自 counterexample mechanism 而非 data/format overlap，也不证明自然语言 proof 正确。
- **Limitations / Threats to Validity:** 单一教材来源族、翻译与 GPT judge bias、类别不平衡、1,025-sample SFT、无 formal verification/多 seed；作者把 metric gain 解释为 conceptual reasoning 仍需克制。
- **Trade-offs / New Failure Modes:** 专门 probe 暴露概念边界，代价是 domain coverage 窄、annotation/judge 成本和针对 benchmark 格式过拟合。
- **Where the Previous Design Still Applies:** arithmetic、code execution 或 formal theorem proving 目标仍应使用对应可执行 benchmark；CounterMATH 是补充维度而非替代。
- **Evolution Relationship:** `Layering / Dependency`：answer-level math score → reasoning-technique probe → targeted SFT → formal/expert verification remains authority。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`，handoff `TRAIN-SFT` 与 `AGENT-REFLECTION`。
- **Target and Adjacent Chapters Read:** 已读 Ch65 Observability、Ch66 Evaluation、Ch67 AI Cost，并回读 Ch29 SFT 与 Ch80 Reflection。
- **Existing Coverage:** Evaluation 已要求拆开 answer、process 与 executable evidence；该来源增加 counterexample probe，但不改变 scorer/judge 边界。
- **Integration Decision:** `Books Pending — No Change or Review-note Evidence`。
- **Changed Files or Rejection Reason:** 仅补 W07；不把作者 OOD 提升解释为普遍 conceptual understanding。
- **Open Questions:** 如何以 formal checker 或独立专家验证 counterexample correctness，并把 concept coverage、translation 与 contamination 作为 dataset identity？

### Diverse Inference and Verification for Advanced Reasoning

- **Candidate / Week / Score:** Diverse Inference and Verification for Advanced Reasoning / 2025-W07 / 26/30。
- **Source Family ID:** `arxiv:2502.09955`。
- **Source Type:** Primary research paper；arXiv metadata 与可核对 v1 标识的公开全文镜像联合核验。
- **First-public Date / Revision History:** arXiv v1 2025-02-14；当前 arXiv history 仅列 v1，W07 锁定该 165 页版本。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.09955；https://arxiv.org/pdf/2502.09955v1；公开全文镜像 https://www.researchgate.net/publication/389055678_Diverse_Inference_and_Verification_for_Advanced_Reasoning。
- **Related Primary Sources:** 作者主页 https://cs-people.bu.edu/idrori/；paper 声明 publication 后公开 artifact，但 v1 未给可复算 release/commit。
- **Access and Verification Status:** Full Review Complete；arXiv PDF 因体积超出当前传输限制，但逐页文本可由带 `arXiv:2502.09955v1` 标识的公开全文镜像核验，并与 arXiv metadata/abstract 交叉确认。
- **Full-read Coverage:** metadata、Introduction、diverse inference formulation、IMO/ARC/HLE methods、perfect/imperfect verifier discussion、test-time simulation/RL、agent-graph meta-learning、evaluation/ablation tables、relevant appendices、conclusion；全文没有独立 limitations 章节。
- **Original Problem:** 单一模型或单一推理方法在 hard reasoning task 上覆盖有限；增加 samples 只有在候选具有互补性且结果可验证时才能转化为可信收益。
- **Why the Previous Design Was Reasonable:** single-model self-consistency 或 best-of-N 接口简单、成本可预测，在同质错误较少或 verifier 足够准确时是合理 baseline。
- **Changed Constraint:** IMO、ARC、HLE 等任务同时暴露 model diversity、method diversity、verification quality 与 test-time budget 的耦合，单一 sampler 无法覆盖所有错误模式。
- **Mechanism:** 并行组合多模型、多 prompting/search/solver 方法与 Agent graph；IMO 用 Lean 验证 autoformalized proof，ARC 用代码在 training examples 上执行筛选，HLE 用 best-of-N 作为 imperfect selection；部分任务再用 simulation、RL 与 meta-learning 修改 prompt、code、data、nodes/edges。
- **State Ownership:** 每个 solver 拥有候选轨迹；task-specific verifier 拥有接受判定；orchestrator 拥有预算、方法集合与 agent-graph revision；但 v1 没有公开生产级 persistence、rollback 或 artifact identity contract。
- **Control Flow / Data Flow:** task → diverse model/method fan-out → candidate proof/code/answer → Lean、execution tests 或 imperfect selector → accept/aggregate；simulation/RL 生成新 task state/trajectory，meta-layer 根据 run trace 做 A/B test 并修改 graph。
- **Implementation Details:** IMO 组合 LEAP、Z3、RTO、BoN、SC、MoA、MCTS、PV 等分支并 autoformalize 到 Lean；ARC 汇聚 16 类模型/方法与 synthesized programs；appendix 给出 game state/observation/transition/reward 与大量 agent-graph示例。
- **Evaluation Contract:** 2024 IMO combinatorics、ARC 400-puzzle evaluation set、HLE 100-question sample；核心指标是任一可验证 candidate 的 coverage/accuracy，另有 method/category ablations 与 diversity coverage curve。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较单一模型/方法、逐步增加方法的 coverage、HLE 不同 N、IMO/ARC/HLE 多种 method/category；没有统一 token、latency、API price 或 orchestration overhead accounting。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 使用多种闭源与开源模型、Lean、Python execution 与 RL/game simulation；hardware、precision、context length、parallel concurrency、wall-clock、cost 与 production SLO 多数 Not Disclosed。
- **What the Evidence Actually Proves:** 在三个指定 benchmark 与作者实现中，异质 solver 集合扩大了至少一个候选通过 verifier 的覆盖；verifier 类型决定 sample scaling 是否可信，perfect/imperfect verifier 的差异是核心系统变量。
- **What It Does Not Prove:** ARC training-example execution 不能证明 unseen test transformation 正确；HLE best-of-N 不是 perfect verifier；headline accuracy 不证明相同方法对任意 domain、model mix 或预算都可靠、鲁棒、可扩展。
- **Limitations / Threats to Validity:** benchmark/solver 集合高度定制；artifact 未在 v1 形成可复算 release；闭源模型版本与成本不完整；大量方法与 appendices 提高选择偏差风险；缺少独立 limitations 章节和统一 statistical uncertainty。
- **Trade-offs / New Failure Modes:** diversity 提高 coverage，却引入 orchestration cost、duplicate correlated errors、verifier exploitation、model/version drift、budget unfairness、tool/environment mismatch 与 graph mutation rollback 问题。
- **Where the Previous Design Still Applies:** 可单模型高置信完成、预算严格、latency 受限或 verifier 不可得的任务，single-agent/self-consistency 仍可能更稳定；异质 ensemble 不是默认替代。
- **Evolution Relationship:** `Alternative Branch`：single-model sampling → heterogeneous solver portfolio；`Layering / Dependency`：收益依赖 verifier authority 与 workflow orchestration，而不是模型数量本身。
- **ROADMAP Node:** Primary `AGENT-MULTI-AGENT`；handoff `AGENT-WORKFLOW`、`AGENT-REFLECTION`、`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读 Ch80 Reflection、Ch81 Workflow、Ch82 Multi-Agent、Ch83 MCP；并对照 Ch66 Evaluation 的 executable evidence contract。
- **Existing Coverage:** Books 已区分 single-agent headroom、communication tax、shared state 与 error amplification；本候选为 verifier-aware diversity 提供受限案例，不自动改变既有结论。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；Historical Books Gate Closed。
- **Changed Files or Rejection Reason:** 仅补 W07；不保留脱离 model mix、verifier、task split 与预算的 headline 数字，不把 ARC training tests 称为语义 perfect verifier。
- **Open Questions:** 如何对 solver correlation、marginal coverage、verifier false-positive、cost/latency budget 与 graph revision rollback 建立可审计 contract？

### Better Embeddings with Coupled Adam

- **Candidate / Week / Score:** Better Embeddings with Coupled Adam / 2025-W07 / 27/30。
- **Source Family ID:** `arxiv:2502.08441`。
- **Source Type:** Primary research paper + author code artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-12；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.08441v1；https://arxiv.org/abs/2502.08441；https://github.com/flxst/coupled-adam。
- **Related Primary Sources:** nanoGPT https://github.com/karpathy/nanoGPT；Modalities https://github.com/Modalities/modalities，均用于论文实验实现背景。
- **Access and Verification Status:** Full Review Complete；HTML 正文、公式、algorithm、evaluation、ablation、limitations 与 appendices 已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、embedding-gradient derivation、Coupled Adam algorithm、small/large experiments、evaluation、scaled/SGD ablation、statistical appendix、hyperparameters、limitations 与 code link。
- **Original Problem:** next-token training 中 embedding vectors 常整体偏离原点而呈 anisotropy，既有“common enemy”解释没有说明 optimizer 的 token-dependent scaling 如何破坏零和更新。
- **Why the Previous Design Was Reasonable:** Adam 对稀疏、频率长尾的 token parameter 提供自适应步长，通常比 SGD 更稳，是 LLM training 的合理默认值。
- **Changed Constraint:** 对 embedding matrix，按 token row 独立估计 second moment 会把 unigram frequency 转化为不同 effective learning rate，使本来求和为零的 gradient 变成非零更新和。
- **Mechanism:** 仅对 embedding rows 将 bias-corrected second moments 在 vocabulary 维求平均，再用同一 denominator 更新所有 token rows；非 embedding 参数继续标准 Adam。
- **State Ownership:** optimizer state 仍由训练 runtime 持有；first moment 保持逐参数，embedding second-moment scale 从 token-row private state 变为 vocabulary-coupled state。
- **Control Flow / Data Flow:** LM loss → embedding gradients → per-row first/second moments → vocabulary all-row average of second moment → shared effective scale → embedding update；其他参数走原 Adam branch。
- **Implementation Details:** Algorithm 1 只替换 embedding update 的 second moment；实验分别使用 nanoGPT 与 Modalities，weight tying、cosine schedule、DDP/FSDP 等配置在 appendix 披露。
- **Evaluation Contract:** small grid 为 125M/355M/760M × 5B/10B/20B tokens、3 seeds；large 为 1.3B/2.6B × 26B/52B 及 105B/210B tokens、单次运行；比较 test loss、LM Harness downstream accuracy 与 embedding isotropy/semantic metrics。
- **Baselines / Ablations / Sensitivity / Overhead:** Standard Adam、SGD、scaled Coupled Adam；报告显著性/error analysis；large runs 无多 seed，straightforward implementation 未单独量化 communication/kernel overhead。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** small seq 1024、约 100K tokens/batch，large seq 2048、约 500K tokens/batch；BF16、DDP/FSDP；总实验约 20,000 GPU-hours，但具体各 run GPU 型号与 production SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在披露的 dense decoder、token budget 与 schedule 中，shared embedding second moment 一致改善 embedding-specific metrics；部分大数据设置的 upstream/downstream 指标改善。
- **What It Does Not Prove:** 不能证明所有大模型或 MoE/多模态模型都会提高 end-task quality；large runs 只有单 seed，个别表格并非所有指标都优于 Standard Adam。
- **Limitations / Threats to Validity:** 只测 dense decoder 至 2.6B；始终 cosine decay；residual mean shift 是否来自 weight tying 未验证；实现未针对效率优化；模型/数据 family 有限。
- **Trade-offs / New Failure Modes:** vocabulary coupling 恢复零和性质，却削弱 rare-token 独立 adaptivity，并可能引入跨 shard reduction、embedding-specific optimizer path、checkpoint compatibility 与 tied/untied weight divergence。
- **Where the Previous Design Still Applies:** 非 embedding 参数和稀疏 row 需要独立 adaptivity、embedding quality 不是瓶颈、或分片通信成本高时，标准 Adam 仍合理。
- **Evolution Relationship:** `Direct Evolution`：per-token Adam second moment → embedding-specific coupled moment；`Alternative Branch`：SGD、Adalayer 等保留不同 adaptivity/geometry trade-off。
- **ROADMAP Node:** Primary `TRAIN-PRETRAINING`；handoff `MODEL-EMBEDDING`、`TRAIN-DISTRIBUTED-TRAINING`。
- **Target and Adjacent Chapters Read:** 已读 Ch12 Embedding、Ch27 Data、Ch28 Pretraining、Ch36 Distributed Training、Ch37 Tensor Parallel。
- **Existing Coverage:** Books 已覆盖 optimizer state 与 distributed ownership，但尚无 embedding-row adaptivity 导致 representation geometry 的具体因果案例。
- **Integration Decision:** `Books Pending — New Mechanism Candidate`；Historical Books Gate Closed。
- **Changed Files or Rejection Reason:** 仅补 W07；不把 embedding metric 改善外推为通用 downstream gain，不把 20K GPU-hours拆成未披露 hardware 性能数字。
- **Open Questions:** 在 vocab-parallel、untied embedding、MoE/multimodal vocabulary 与 infinite schedule 中，coupled state 应在哪个 shard 聚合，收益是否仍成立？

### Data Valuation using Neural Networks for Efficient Instruction Fine-Tuning (NN-CIFT)

- **Candidate / Week / Score:** Data Valuation using Neural Networks for Efficient Instruction Fine-Tuning / 2025-W07 / 24/30。
- **Source Family ID:** `arxiv:2502.09969`。
- **Source Type:** Primary research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-14；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.09969v1；https://arxiv.org/abs/2502.09969。
- **Related Primary Sources:** baseline family DELIFT、LESS、SelectIT 由论文逐项引用；v1 只声明 code 为 Apache 2.0，未提供可核对 repository URL/commit。
- **Access and Verification Status:** Full Review Complete；method、evaluation、hyperparameter grid、appendices、limitations 与 artifact license 已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、problem setting、InfluenceNetwork architecture/training、subset selection、cost/evaluation tables、169-run sensitivity、smaller-subset appendix、baseline formulas、limitations/license。
- **Original Problem:** pairwise influence-based instruction-data valuation 要在大型 embedding/LM 上重复计算 train–target pairs，新数据到达后还要重算，成本高且难以持续更新。
- **Why the Previous Design Was Reasonable:** 直接 influence function 绑定当前 model、train sample 与 target sample，解释清楚且无需学习额外 surrogate；数据规模较小时精度优先。
- **Changed Constraint:** instruction pool 与 target set 扩大且持续变化，完整 pairwise valuation 的 forward/backward 成本成为瓶颈，需要把昂贵函数蒸馏为可复用估计器。
- **Mechanism:** 用 bge-large-en-v1.5 得到两条 1024-d embedding，拼成 2048-d 输入；2-layer ReLU InfluenceNetwork（hidden 100、204,900 参数）学习原 influence function 的少量 pair labels，再估计剩余 pairs 并执行 subset selection。
- **State Ownership:** 原 influence function 拥有 teacher labels；InfluenceNetwork parameters 拥有 surrogate state；data pipeline 必须持有 embedding/model/version 与 train/target split identity。
- **Control Flow / Data Flow:** data pairs → expensive influence on u×u seed quadrant → InfluenceNetwork fit → remaining pair scores → ranking/subset v → QLoRA 或 ICL → downstream evaluation。
- **Implementation Details:** u=0.05 时 pairwise training labels 为 5%×5%=0.25%；20 epochs、lr 1e-4；默认 v=0.3，另做 u/v grid 与 network-size study。
- **Evaluation Contract:** MixInstruct、Alpaca 各 15K train/5K val/5K test；Phi-3-small-8k-instruct 7.39B 与 Llama-3.1-8B 8.03B；QLoRA/ICL；ROUGE-1、BGE、Prometheus-7B judge；所有主要表格单次运行。
- **Baselines / Ablations / Sensitivity / Overhead:** DELIFT、DELIFT(SE)、LESS、SelectIT、DistilGPT2 surrogate、Random、Initial、Full Data；169 组 u=v grid、1–5 layers/46 hidden-size组合；2×A40 wall time用于 valuation cost。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 2×NVIDIA A40；模型与数据规模披露；precision、sequence length、batch、并发与 SLO Not Disclosed；不将 77–99% wall-time reduction 跨硬件外推。
- **What the Evidence Actually Proves:** 在两套 instruction dataset、两模型和四种 teacher influence family 中，小 surrogate 用极少 pair labels近似 influence score，并在作者 subset selection/evaluation 下接近原方法；论文报告平均 performance difference 约 1.39%。
- **What It Does Not Prove:** 不能证明 surrogate 学到 causal data value、可跨 embedding/model/version 复用，或对 task-specific selection、continual learning、其他语言/domain 保持有效。
- **Limitations / Threats to Validity:** 依赖 teacher influence 与大量 annotated data；仍是 quadratic pair scoring；不支持 task-specific selection/continual learning；single-run、LLM judge 与 embedding metric 带来方差/偏差。
- **Trade-offs / New Failure Modes:** 显著降低 teacher compute，但新增 surrogate drift、embedding-version coupling、ranking error、stale data value、quadratic tail 与 judge contamination。
- **Where the Previous Design Still Applies:** 小数据、high-stakes selection、teacher influence 可负担或需要 model-specific精确 trace 时，直接 influence function 仍更合适。
- **Evolution Relationship:** `Layering / Dependency`：精确 influence teacher → learned surrogate → subset policy；不是 surrogate 对 influence theory 的替代。
- **ROADMAP Node:** Primary `TRAIN-DATA`；handoff `TRAIN-SFT`、`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读 Ch27 Data、Ch28 Pretraining、Ch29 SFT、Ch30 LoRA、Ch65 Evidence、Ch66 Evaluation。
- **Existing Coverage:** Books 已要求 data lineage、versioned artifact 与 evaluation contract；NN-CIFT 增加 valuation surrogate 的 freshness/identity 案例。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；Historical Books Gate Closed。
- **Changed Files or Rejection Reason:** 仅补 W07；headline time reduction 与 1.39% 差异保留 2×A40、dataset/model/metric、single-run 边界。
- **Open Questions:** 如何检测 surrogate 在 model、embedding、data distribution 或 objective 变化后的失效，并将 uncertainty 传播到 subset/release decision？

### Cluster and Predict Latent Patches for Improved Masked Image Modeling (CAPI)

- **Candidate / Week / Score:** Cluster and Predict Latent Patches for Improved Masked Image Modeling / 2025-W07 / 24/30。
- **Source Family ID:** `arxiv:2502.08769`。
- **Source Type:** Primary research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-12；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.08769v1；https://arxiv.org/abs/2502.08769。
- **Related Primary Sources:** paper 与 appendix 给出完整 recipe、model UID 与 build logs；v1 未提供可核验 official repository commit。
- **Access and Verification Status:** Full Review Complete；method、formula、implementation、evaluation、ablation、compute/environment appendix 与 model UID 表已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、target/loss/predictor branches、online clustering/Sinkhorn、cross-attention predictor、datasets/recipe、classification/segmentation evaluation、ablations、compute footprint、model list；无独立 limitations 章节。
- **Original Problem:** pixel reconstruction 过度关注 low-level detail，latent target 更 semantic 但 online teacher/student head coupling 易不稳定、target/prediction token distribution mismatch，并对 mask/crop hyperparameter 敏感。
- **Why the Previous Design Was Reasonable:** MAE pixel target简单稳定；iBOT/DINO projection head可生成 semantic target；I-JEPA asymmetric latent prediction减少像素依赖，各自在相应稳定性/性能约束下合理。
- **Changed Constraint:** 要同时获得 stable training、强 local representation 与 scalable masked prediction，需要把 target formation 与 predictor gradient path 解耦，并避免 positional cluster collapse。
- **Mechanism:** EMA teacher patch features 经 L2 projection 与 online prototypes形成 cluster assignment；modified Sinkhorn按固定 patch position 做 balancing；student encoder只看可见 patches，cross-attention predictor为少量 masked queries独立读取 encoder output并预测 assignment。
- **State Ownership:** EMA teacher持有缓慢更新的 target representation；prototype matrix持有 online cluster state；student encoder/predictor持有可训练 prediction state；register tokens提供 information buffer。
- **Control Flow / Data Flow:** image → mask 65% → visible patches/student encoder → 7 masked queries/cross-attention predictor；完整/teacher view → EMA features → online clustering + positional Sinkhorn → assignment target → cross-entropy update student/predictor/prototypes。
- **Implementation Details:** ViT-L约300M、12-block cross-attention predictor无self-attention、16 registers、16,384 prototypes、inverse-block+roll mask、teacher momentum=1-lr、cluster lr=0.5lr；recipe含 model UID。
- **Evaluation Contract:** ImageNet-1k/22k、Places205、LVD-142M pretraining；冻结 backbone 后以 attentive probe 做 classification、linear/kNN head做 ADE20K/Pascal VOC/Cityscapes segmentation；224×224 evaluation。
- **Baselines / Ablations / Sensitivity / Overhead:** MAE、iBOT、I-JEPA、AIM、DINOv2 等；ablate target/loss/predictor、mask、crop、register、position encoding、Sinkhorn/prototype等；default ablation多为少量 runs/2 seeds，比较协议不完全同算力。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** bf16、FSDP、batch 16,384、224 image、ViT-L；单个 LVD run 32×A100×180h=5,763 A100-hours；整个项目3.75M A100-hours；在线 serving/SLO 不适用。
- **What the Evidence Actually Proves:** 在披露的 vision SSL contract 中，显式 online clustering 与解耦 predictor 提高 masked latent prediction 稳定性，并在冻结特征分类/分割上缩小与 DINOv2 类方法的差距。
- **What It Does Not Prove:** 不能证明 CAPI 是通用 multimodal tokenizer、对生成任务/视频/语言有效，或在等算力、等数据下全面优于所有 contrastive/self-distillation 方法；DINOv2 在部分任务仍更强。
- **Limitations / Threats to Validity:** 无正式 limitations 章节；只测 vision/ViT-L 至300M；总搜索成本极高；global representation依赖额外 predictor/probe；部分 baseline data/model size不同；ablation seed有限。
- **Trade-offs / New Failure Modes:** 显式 cluster target提高透明性/稳定性，却新增 prototype collapse、position balancing bias、EMA lag、distributed all-reduce、large-batch依赖与高搜索成本。
- **Where the Previous Design Still Applies:** 计算受限、pixel fidelity重要或简单重建已足够时 MAE仍合理；需要强 global semantics且可承受 self-distillation 时 DINOv2/iBOT branch仍成立。
- **Evolution Relationship:** `Direct Evolution`：pixel target → latent target → explicit clustered latent target；`Alternative Branch`：contrastive/self-distillation 与 reconstruction保持不同目标。
- **ROADMAP Node:** Primary `MULTIMODAL-REPRESENTATION`；handoff `TRAIN-PRETRAINING`、`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读 Ch23 Multimodal Representation、Ch24 Generative Paradigms、Ch25 World Models、Ch27 Data、Ch28 Pretraining、Ch66 Evaluation。
- **Existing Coverage:** Ch23 已说明 patch/token identity 与 modality boundary；CAPI补充 target/predictor/cluster state 分离的受限机制，不等于跨模态统一表示。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；Historical Books Gate Closed。
- **Changed Files or Rejection Reason:** 仅补 W07；性能数字绑定 dataset、ViT-L、frozen-probe protocol、bf16/FSDP/batch与A100成本，不写成通用 SOTA。
- **Open Questions:** prototype/EMA state 在不同 data mixture、world size、batch与连续训练中如何 version、恢复和检测 collapse？

### small Models, BIG Impact

- **Candidate / Week / Score:** small Models, BIG Impact / 2025-W07 / 22/30。
- **Source Family ID:** `arxiv:2502.10140`。
- **Source Type:** Primary research paper + official code artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-14；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.10140v1；https://arxiv.org/abs/2502.10140。
- **Related Primary Sources:** https://github.com/d-gurgurov/Knowledge-Driven-Adaptation-LLMs。
- **Access and Verification Status:** Full Review Complete；正文、appendices、hyperparameters、逐语言结果与官方代码入口已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、adapter/data method、30-language setup、MLM/TC/NER/SA results、large-model comparison、correlation、discussion、conclusion 与 appendices；无独立 limitations 章节。
- **Original Problem:** 低资源语言既缺原始文本，也难以承担大模型全量适配；模型规模、adapter capacity、pretraining coverage 与结构化/非结构化数据如何共同决定效果并不清楚。
- **Why the Previous Design Was Reasonable:** full fine-tuning 直接调整全部参数，continued pretraining 可利用目标语言文本；大模型 prompting 则避免维护每种语言的专用训练流水线，在数据和算力充足时都合理。
- **Changed Constraint:** 当每种语言只有少量文本或知识图谱、算力受限且需要维护 30 种语言时，训练参数量与数据覆盖的匹配比单纯扩大 backbone 更重要。
- **Mechanism:** 在 mBERT/XLM-R 上分别训练 Sequential Bottleneck、Invertible Bottleneck 与 LoRA language adapter，再堆叠 task adapter；GlotCC 文本与自然语言化 ConceptNet triples形成不同 adaptation distributions，并测试 adapter fusion。
- **State Ownership:** frozen backbone 持有共享 multilingual representation；language adapter 持有目标语言增量状态；task adapter 持有任务状态；数据源和 chat/tokenization recipe 持有 adaptation identity。
- **Control Flow / Data Flow:** GlotCC/ConceptNet → language-specific MLM/CLM adapter → frozen backbone + language adapter → task adapter → FLORES/SIB-200/WikiANN/sentiment evaluation。
- **Implementation Details:** mBERT、XLM-R-base 比较三类 adapter；LLaMA-3-8B 因算力仅测 Seq_bn_inv/5 languages；GlotCC 每语种最多 1GB，ConceptNet 转句；language adapter 最多 100k/25k steps，batch 16、lr 1e-4。
- **Evaluation Contract:** 30 个 low-resource languages；FLORES-200 pseudo-perplexity、SIB-200 topic F1、WikiANN NER F1 与多源 sentiment F1；另在 5 种语言上比较 LLaMA-3 与若干公开模型。
- **Baselines / Ablations / Sensitivity / Overhead:** 无 adapter、full fine-tuning、不同 adapter、Glot/ConceptNet/fusion、XLM-R-large 与大模型 prompting；逐语言 appendices 揭示平均值掩盖的异质性，但缺统一等算力比较。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型与 batch/steps/lr 已披露；训练 hardware、precision、sequence length、并发与 serving SLO 为 Not Disclosed。
- **What the Evidence Actually Proves:** 在作者的语言、数据与任务 contract 下，小型 multilingual backbone 的 parameter-efficient adaptation 可在较少可训练参数下取得有竞争力结果；adapter 架构与数据类型的优劣随任务和 pretraining coverage 改变。
- **What It Does Not Prove:** 不能证明小模型普遍优于大模型、ConceptNet 普遍优于文本、pseudo-perplexity 可替代 downstream evaluation，或 adapter 一定优于等算力 full fine-tuning。
- **Limitations / Threats to Validity:** LLaMA 仅 5 种语言/一种 adapter；大模型比较的训练与推理协议不统一；无训练硬件/方差披露；数据质量、tokenizer coverage 与语言分类可能混杂模型规模结论。
- **Trade-offs / New Failure Modes:** adapter 降低参数与 artifact 成本，却新增 adapter/backbone/tokenizer 兼容、语言与任务组合爆炸、数据版本漂移及 stacked-adapter 干扰。
- **Where the Previous Design Still Applies:** 有充足目标数据、需要最大化单域能力或 backbone 本身不覆盖目标 script 时，full fine-tuning/continued pretraining 仍合理；通用多语言请求中大模型 prompting 可减少运维分支。
- **Evolution Relationship:** `Alternative Branch`：full fine-tuning / large-model prompting ↔ small-backbone adapter；不是单向替代。
- **ROADMAP Node:** Primary `TRAIN-SFT`；handoff `TRAIN-DATA`、`TRAIN-PRETRAINING`。
- **Target and Adjacent Chapters Read:** 已读 Ch27 Data、Ch28 Pretraining、Ch29 SFT 与 Ch30 LoRA。
- **Existing Coverage:** Books 已解释 SFT/LoRA 与 data-objective coupling；本文补充 adapter capacity、pretraining coverage、structured/unstructured data 的联合 operating point。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；Historical Books Gate Closed。
- **Changed Files or Rejection Reason:** 仅补 W07；不把跨协议平均分写成模型规模定律。
- **Open Questions:** 如何以每语言 token coverage、tokenizer fertility、trainable parameters 与 lifecycle cost 建立可迁移的 adapter selection policy？

### Text-guided Sparse Voxel Pruning for Efficient 3D Visual Grounding

- **Candidate / Week / Score:** TSP3D / 2025-W07 / 22/30。
- **Source Family ID:** `arxiv:2502.10392`。
- **Source Type:** Primary research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-14；v2 2025-03-11；W07 证据锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.10392v1；https://arxiv.org/abs/2502.10392。
- **Related Primary Sources:** paper appendices/build logs；v1 未发现可锁定的 official repository commit。
- **Access and Verification Status:** Full Review Complete；method、loss、datasets、implementation、runtime table、ablations 与 limitations 已核验。
- **Full-read Coverage:** Introduction/Related Work、architecture analysis、TGP、CBA、training loss、ScanRefer/ReferIt3D evaluation、cost appendix、ablation、qualitative cases 与 limitations。
- **Original Problem:** 两阶段 3D grounding 重复提取特征，单阶段方案又常在最高分辨率 sparse voxels 上做昂贵融合，且盲目 pruning 会丢失目标与上下文。
- **Why the Previous Design Was Reasonable:** detector→grounder 的两阶段接口可复用成熟 detector 并隔离错误；不剪枝的高分辨率特征保留所有候选，在小场景或算力充足时更稳。
- **Changed Constraint:** 3D scene token 数与 cross-modal interaction 成为 runtime 瓶颈，需要让语言条件参与计算预算分配，同时保留被误剪的关键信息恢复路径。
- **Mechanism:** Text-Guided Pruning 先对 voxel FPS、与文本 cross-attention，再预测 keep mask；Completion-Based Addition 从较低层补回缺失位置，形成 coarse-to-fine sparse feature fusion。
- **State Ownership:** sparse backbone 持有多尺度 voxel state；文本 encoder 持有 query state；pruning mask 决定 active compute set；CBA 持有补回候选与位置 correspondence。
- **Control Flow / Data Flow:** point cloud→voxel pyramid；description→text features；cross-attention→retain probabilities→threshold mask→sparse self-attention；低层 completion→detection/grounding heads。
- **Implementation Details:** PyTorch；1cm 初始 voxel、分层尺度、scene/target thresholds 0.7/0.3、completion threshold 0.15；pruning/completion/class/bbox losses 等权。
- **Evaluation Contract:** ScanRefer 51,583 descriptions；Nr3D/Sr3D；Acc@IoU 与 target-selection accuracy；作者复现 baseline 并报告 FPS。
- **Baselines / Ablations / Sensitivity / Overhead:** two-stage 与 single-stage baselines；TGP、CBA、level 与 upsampling ablation；TGP 明显改善 accuracy 但相对 naive concatenation 降低 FPS，CBA 再增加开销。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/dataset/voxel thresholds 已披露；FPS 的具体 hardware、precision、batch/concurrency 与 latency SLO 在正文可见信息中 Not Disclosed，不能跨系统外推。
- **What the Evidence Actually Proves:** 在披露 3DVG datasets 与作者复现环境中，query-conditioned active-set pruning 可同时改变计算量与表示质量，completion path 能缓解部分信息损失。
- **What It Does Not Prove:** 不能证明该阈值适用于 streaming RGB-D、机器人闭环或所有 sparse backbones，也不能在缺硬件合同下把 12.43 FPS 视为通用速度。
- **Limitations / Threats to Validity:** 只用 reconstructed point clouds；cross-attention 本身仍重；baseline speed 来自作者复现；硬件/precision 未披露；online sensor drift 与 pruning error recovery 未测。
- **Trade-offs / New Failure Modes:** 条件剪枝把算力聚焦相关 voxels，却新增 threshold brittleness、query bias、误剪不可逆性、completion overhead 与 mask calibration failure。
- **Where the Previous Design Still Applies:** 安全关键感知、目标很小或 query 不稳定时保留完整 features 更稳；已有可靠 detector 或对象复用率高时 two-stage 仍合理。
- **Evolution Relationship:** `Direct Evolution`：dense/high-resolution fusion → text-conditioned active set → completion-backed pruning；two-stage 保持 `Alternative Branch`。
- **ROADMAP Node:** Primary `MULTIMODAL-REPRESENTATION`；handoff `MULTIMODAL-EMBODIED-VLA`、`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读 Ch23 Representation、Ch24 Generative Paradigms、Ch26 Embodied VLA 与 Ch66 Evaluation。
- **Existing Coverage:** Ch23 已定义 modality/coordinate identity；TSP3D 增加 representation state 同时作为 conditional compute boundary 的受限案例。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；Historical Books Gate Closed。
- **Changed Files or Rejection Reason:** 仅补 W07；速度数字保留 Not Disclosed hardware 边界。
- **Open Questions:** pruning mask 如何随 sensor time、query revision 与 safety envelope 版本化，并在 streaming 场景支持 late recovery？

### V2V-LLM

- **Candidate / Week / Score:** V2V-LLM / 2025-W07 / 21/30。
- **Source Family ID:** `arxiv:2502.09980`。
- **Source Type:** Primary research paper + benchmark dataset。
- **First-public Date / Revision History:** arXiv v1 2025-02-14；后续 v2-v4 不反推 W07。
- **Direct Primary Sources:** https://arxiv.org/html/2502.09980v1；https://arxiv.org/abs/2502.09980。
- **Related Primary Sources:** V2V4Real base dataset and paper-linked supplementary material。
- **Access and Verification Status:** Full Review Complete；dataset curation、architecture、training、fusion baselines、metrics、ablations、appendices 与 failure cases 已核验。
- **Full-read Coverage:** Introduction/Related Work、V2V-QA schema、feature extraction/fusion、LLaVA adaptation、evaluation metrics、grounding/object/planning results、communication cost、ablation 与 limitation。
- **Original Problem:** cooperative driving 既要融合多车 LiDAR perception，又要把 grounding、risk object 与 trajectory planning 放进统一可评测接口；传统 fusion benchmark 不覆盖语言条件决策。
- **Why the Previous Design Was Reasonable:** early fusion 保留 raw sensor detail，intermediate fusion 降低带宽且适合专用 perception；模块化 planner 的状态和安全边界更清晰，在实时/安全场景仍合理。
- **Changed Constraint:** 需要基于多车状态回答不同车辆的语义问题并生成 trajectory，fusion output 不再只是 detector feature，而要成为 LLM 可消费且带通信成本的 representation。
- **Mechanism:** 多车 LiDAR 经 3D detector 产生 scene map 与 object vectors，经 projector 对齐语言 embedding；冻结 Vicuna/encoder，仅训练 projector 与 LoRA，使 LLM 聚合 perception tokens 和 question tokens。
- **State Ownership:** 各 CAV 拥有本地 sensor/frame state；fusion layer拥有共享 scene/object representation；LLM/LoRA持有问答策略；trajectory 输出仍需外部 controller/safety owner。
- **Control Flow / Data Flow:** synchronized LiDAR→per-CAV feature extraction→scene/object feature transfer→projector→LLM+question→grounding/notable object/trajectory answer。
- **Implementation Details:** V2V-QA 基于两车 V2V4Real，7,105 train + 1,993 test frames/CAV、10Hz、576,693 QA；LLaVA-v1.5-7B/Vicuna backbone，batch 32，Q1 1 epoch、其他 10 epochs。
- **Evaluation Contract:** grounding F1、notable-object precision/recall、1/2/3s trajectory L2、collision rate 与 communication MB；比较 no/early/intermediate/LLM fusion。
- **Baselines / Ablations / Sensitivity / Overhead:** 同 projector/LLM 下替换 feature fusion；scene-only、object-only 与 combined ablation；combined communication 0.203MB，但未评端到端 network jitter、packet loss 与 closed-loop latency。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** LLaVA-v1.5-7B、batch 32、10Hz dataset 已披露；GPU、precision、token length、online concurrency、deadline/SLO 为 Not Disclosed。
- **What the Evidence Actually Proves:** 在 V2V-QA 离线 split 中，scene+object tokens 的 LLM fusion 可在给定通信量下改善作者定义的 planning/object metrics，并揭示 feature level 对不同任务的影响。
- **What It Does Not Prove:** 不证明系统可安全闭环驾驶、满足 10Hz deadline、容忍网络/时钟故障或泛化到多于两车；自然语言 trajectory 也不等于 actuator command。
- **Limitations / Threats to Validity:** base dataset 无 HD map；作者展示逆向车道 failure；问答由标注规则生成；离线 split/两车限制；没有 real-time、calibration drift 或 safety intervention evaluation。
- **Trade-offs / New Failure Modes:** LLM fusion提升语义统一性，却增加 feature transfer、projector alignment、hallucinated trajectory、stale-frame aggregation 与不可解释 fusion ownership。
- **Where the Previous Design Still Applies:** 高安全等级、硬 deadline、网络不可靠或任务 taxonomy 稳定时，模块化 perception/planning 与 intermediate fusion 更易验证和降级。
- **Evolution Relationship:** `Layering / Dependency`：cooperative perception fusion → language-conditioned decision interface；不是 VLM 替代 planner/controller。
- **ROADMAP Node:** Primary `MULTIMODAL-EMBODIED-VLA`；handoff `MULTIMODAL-REPRESENTATION`、`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读 Ch23 Representation、Ch25 World Models、Ch26 Embodied VLA 与 Ch66 Evaluation。
- **Existing Coverage:** Ch26 已区分 proposal、controller、environment feedback；V2V-LLM补充 distributed sensor ownership 与 communication contract 案例。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；Historical Books Gate Closed。
- **Changed Files or Rejection Reason:** 仅补 W07；所有 planning 数字限定于离线 V2V-QA。
- **Open Questions:** 如何将 frame timestamp、pose/calibration、packet freshness 与 safety override 纳入 cooperative VLA 的 typed state？

### MRS: A Fast Sampler for Mean Reverting Diffusion

- **Candidate / Week / Score:** MRS / 2025-W07 / 23/30。
- **Source Family ID:** `arxiv:2502.07856`。
- **Source Type:** Primary research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-11；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.07856v1；https://arxiv.org/abs/2502.07856。
- **Related Primary Sources:** paper appendices include proofs, algorithms, full task metrics, numerical stability and wall-clock analysis。
- **Access and Verification Status:** Full Review Complete；公式、proofs、ODE/SDE algorithms、evaluation、parameter ablations 与 appendices 已核验。
- **Full-read Coverage:** MR diffusion background、noise/data/velocity parameterizations、reverse SDE/PF-ODE semi-analytical derivation、algorithms、10 restoration tasks、NFE/solver ablations、stability analysis、runtime appendix、conclusion；无独立 limitations 章节。
- **Original Problem:** Mean-Reverting diffusion 把 condition 写进 SDE structure，适合 restoration，却无法直接复用标准 diffusion fast samplers，通常需要数百次 network function evaluations。
- **Why the Previous Design Was Reasonable:** posterior sampling/Euler-Maruyama faithful follow discretized reverse process，易实现且在高 NFE 下稳定；修改 score 的 conditional diffusion 也有成熟 sampler ecosystem。
- **Changed Constraint:** restoration latency 要求把 NFE 降到个位数/十位数，同时保留 MR SDE 的 condition structure，必须利用其线性部分而非直接移植通用 solver。
- **Mechanism:** 分别求 reverse-time SDE 与 probability-flow ODE 的 semi-analytical solution；解析处理 mean-reverting linear terms，只用 exponential integrator 近似 neural nonlinear integral，并支持 noise/data/velocity parameterization 变换。
- **State Ownership:** SDE schedule与 condition mean `mu` 持有 process state；network持有 score/data prediction；solver持有 time grid、历史 prediction buffer 与 stochastic increments。
- **Control Flow / Data Flow:** degraded condition + terminal noise→time schedule→每步 network prediction→analytic linear update + integral approximation→ODE deterministic 或 SDE stochastic next state→restored image。
- **Implementation Details:** 一阶/二阶 ODE/SDE variants；data prediction在 low NFE 更稳定；算法显式缓存先前 prediction 形成 multi-step estimate。
- **Evaluation Contract:** 10 类 image restoration degradation；沿用既有 MR checkpoints，仅替换 sampler；LPIPS/FID 为主，PSNR/SSIM 辅助；比较 NFE 5/10/20/50 等。
- **Baselines / Ablations / Sensitivity / Overhead:** posterior sampling、Euler；noise vs data prediction、ODE vs SDE、time-step choices与 numerical stability；作者结果显示 SDE 大 NFE、ODE 小 NFE 各有优势，非单一赢家。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** datasets/checkpoints/NFE 与 wall-clock appendix可见；通用 deployment 的 hardware、precision、batch/concurrency/SLO 不构成统一披露，延迟不能跨环境外推。
- **What the Evidence Actually Proves:** 对作者使用的 MR restoration checkpoints，结构匹配的 semi-analytical solver 可在更低 NFE 保持指标，并揭示 network parameterization 与 numerical stability 的强耦合。
- **What It Does Not Prove:** 不证明所有 diffusion 都能 5-step sampling、MRS 适用于标准 VP/VE diffusion、生成任务或不同 noise schedules，也不保证作者指标等于 perceptual correctness。
- **Limitations / Threats to Validity:** 限于 MR diffusion/restoration；复用既有 checkpoints；无正式 limitations；solver order、schedule与 prediction parameterization耦合；低 NFE 的 ODE/SDE优势依任务改变。
- **Trade-offs / New Failure Modes:** 减少 NFE 和 wall time，却新增 solver derivation/implementation complexity、time-grid sensitivity、buffer error、low-NFE numerical instability 与 stochastic reproducibility差异。
- **Where the Previous Design Still Applies:** 高 NFE 可接受、实现简单/可移植性优先或 process 不满足 MR 解析结构时，Euler/posterior或通用 sampler仍合理。
- **Evolution Relationship:** `Direct Evolution`：generic discretization → process-specific semi-analytical integration；ODE 与 SDE 是条件分支。
- **ROADMAP Node:** Primary `MULTIMODAL-GENERATIVE-PARADIGMS`；handoff `PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读 Ch23 Representation、Ch24 Generative Paradigms、Ch25 World Models 与 Ch66 Evaluation。
- **Existing Coverage:** Ch24 已以 state transition/commit contract 比较 diffusion；MRS补充 sampler必须匹配 process algebra 与 parameterization 的机制案例。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；Historical Books Gate Closed。
- **Changed Files or Rejection Reason:** 仅补 W07；不把 restoration NFE 外推到文本/视频 generation。
- **Open Questions:** 如何在相同 quality target 下联合选择 parameterization、solver、time grid、NFE 与 hardware kernel，并给出可复现 latency/energy contract？

### CLaMP 3

- **Candidate / Week / Score:** CLaMP 3 / 2025-W07 / 23/30。
- **Source Family ID:** `arxiv:2502.10362`。
- **Source Type:** Primary research paper + official repository/dataset/model artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-14；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.10362v1；https://arxiv.org/abs/2502.10362。
- **Related Primary Sources:** https://github.com/sanderwood/clamp3；https://sanderwood.github.io/clamp3/。
- **Access and Verification Status:** Full Review Complete；model/data method、training order、evaluation、appendices、leakage analysis、limitations 与 artifact 已核验。
- **Full-read Coverage:** Introduction、InfoNCE/staged alignment、encoders、M4-RAG curation、WikiMT-X、training settings、English/multilingual/emergent retrieval、classification appendices、leakage 与 limitations。
- **Original Problem:** audio、symbolic score、performance signal 与多语言 text 缺少全配对数据，直接 all-to-all alignment 成本高且会发生 modality interference 与 representation drift。
- **Why the Previous Design Was Reasonable:** 单模态/成对 contrastive encoder 在有足够 paired data 时目标清楚；独立 retrieval systems 可保留 temporal/task-specific representation，避免一个 shared space 吞掉细节。
- **Changed Constraint:** 希望未直接配对的 music modalities 也可互检索，并扩展到未参与 alignment 的语言，需要一个共享 anchor 与可控的 sequential alignment protocol。
- **Mechanism:** 以 multilingual text 为 bridge；依次 align symbolic/text 与 audio/text，交替 freeze/unfreeze text encoder 修复 representation drift；各 modality 用专用 transformer encoder，InfoNCE 对齐 shared space。
- **State Ownership:** text encoder持有跨语言 anchor；symbolic/audio encoders持有 modality state；freeze schedule决定谁可移动；M4-RAG metadata 与 WikiMT-X triplets持有 supervision/evaluation identity。
- **Control Flow / Data Flow:** web music identity→RAG metadata curation/translation→text pairs；symbolic/audio features→modality encoders→staged contrastive alignment→shared embeddings→direct或 emergent cross-modal retrieval。
- **Implementation Details:** XLM-R-base text encoder；M3 symbolic encoder；frozen MERT features + 12-layer audio transformer；四阶段 freeze/unfreeze；M4-RAG 2.31M pairs、WikiMT-X 1,000 triplets。
- **Evaluation Contract:** text↔symbolic/audio retrieval、多语言与未见语言、symbolic↔audio emergent retrieval；8×H800，symbolic 4 days/batch1024，audio 1 day/batch2048，mixed precision。
- **Baselines / Ablations / Sensitivity / Overhead:** TTMR++、CLaMP2 与不同 modality alignment orders；appendix列 variants/classification/leakage；未做全量 temporal retrieval 或统一原始数据等算力比较。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8×H800、mixed precision、100 epochs、batch 1024/2048、symbolic最多512 patches/32768 chars、audio 5s/embedding；online concurrency/SLO 不适用。
- **What the Evidence Actually Proves:** 在披露 music datasets 中，text-anchored staged alignment 能形成一定未直接配对 modality retrieval，并显示 alignment order/freeze state 是系统机制而非无关 recipe。
- **What It Does Not Prove:** 不证明 shared embedding 保留音乐时间结构、自动理解未见语言、适用所有 modalities，或 emergent retrieval 的较低绝对分数已足够生产使用。
- **Limitations / Threats to Validity:** global embedding丢 temporal dynamics；多语言 benchmark依赖 machine translation；web/RAG metadata有 provenance/noise；标题/艺术家 identity可能引入 shortcut；部分 released pairs少于论文总量。
- **Trade-offs / New Failure Modes:** text bridge减少 all-pairs supervision，却引入 anchor bias、translation noise、stage-order sensitivity、freeze/unfreeze drift、metadata leakage 与 shared-space collision。
- **Where the Previous Design Still Applies:** 有原生 paired data、时间结构关键或 modality-specific metrics 更重要时，直接 pairwise/temporal model仍更合理。
- **Evolution Relationship:** `Direct Evolution`：pairwise alignment → anchor-mediated staged alignment；modality-specific encoders保持 `Layering / Dependency`。
- **ROADMAP Node:** Primary `MULTIMODAL-REPRESENTATION`；handoff `TRAIN-DATA`、`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读 Ch23 Representation、Ch24 Generative Paradigms、Ch27 Data 与 Ch66 Evaluation。
- **Existing Coverage:** Ch23 已定义 shared token/feature space 的 identity 与信息损失；CLaMP3补充 bridge ownership、alignment order 与 drift repair。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；Historical Books Gate Closed。
- **Changed Files or Rejection Reason:** 仅补 W07；不把作者 SOTA 表述写成跨域通用结论。
- **Open Questions:** 多阶段 alignment 如何检测 anchor drift、modality collision 与 metadata shortcut，并让原始配对/翻译 provenance进入 embedding identity？

### Memory, Benchmark & Robots / MIKASA

- **Candidate / Week / Score:** Memory, Benchmark & Robots: A Benchmark for Solving Complex Tasks with Reinforcement Learning / 2025-W07 / 24/30。
- **Source Family ID:** `arxiv:2502.10550`。
- **Source Type:** Primary research paper + benchmark artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-14；后续 revision 不反推 W07。
- **Direct Primary Sources:** https://arxiv.org/html/2502.10550v1；https://arxiv.org/abs/2502.10550。
- **Related Primary Sources:** paper-linked MIKASA repository/environment artifact。
- **Access and Verification Status:** Full Review Complete；formalization、task taxonomy、environment/API、observation/reward variants、PPO baselines、appendices 与 artifact 已核验。
- **Full-read Coverage:** motivation/related work、POMDP/correlation horizon、MIKASA-Base、MIKASA-Robo、task groups、Gymnasium/ManiSkill3 implementation、observation/reward modes、PPO-MLP/LSTM experiments 与 limitations-by-design。
- **Original Problem:** memory 能力常被平均 episodic-return 掩盖；机器人任务又混合 perception、control、reward shaping 与 history dependence，难以判断 agent 失败究竟来自记忆还是其他组件。
- **Why the Previous Design Was Reasonable:** standard RL suites便于比较控制算法；memoryless policy在 Markov state 完整可见时更简单、更稳定，不应为了“有 memory”强制引入 recurrent state。
- **Changed Constraint:** 当当前 observation 不足以决定正确 action、任务依赖 object/spatial/sequential history 或 memory capacity 时，benchmark 必须显式控制 correlation horizon 与可见状态。
- **Mechanism:** 将 memory-intensive task 组织为 object、spatial、sequential、capacity 四类；Base 用可诊断 vector/image tasks，Robo 用 ManiSkill3 tabletop tasks，并提供 state/RGB/joints/prompt 与 dense/sparse reward 分支。
- **State Ownership:** environment拥有 hidden task/world state；observation wrapper决定暴露窗口；policy recurrent state持有推断历史；reward function持有 credit signal；benchmark manifest持有 task/seed/schema identity。
- **Control Flow / Data Flow:** hidden environment state→partial observation→MLP/LSTM policy state update→action→transition/reward→episode metric；oracle state与视觉 observation形成诊断对照。
- **Implementation Details:** MIKASA-Base 两级任务；MIKASA-Robo 32 tasks/12 groups；Gymnasium API、ManiSkill3；比较 PPO-MLP 与 PPO-LSTM、dense/sparse rewards 和多 observation modes。
- **Evaluation Contract:** task success/return 按 task family、observation、reward mode 与 policy memory architecture 切片；state+dense baseline用于确认 task可解，RGB+joints/sparse暴露 memory/perception/credit难点。
- **Baselines / Ablations / Sensitivity / Overhead:** memoryless MLP vs recurrent LSTM、oracle/vector vs image/joint observation、dense vs sparse reward；未覆盖 transformer memory、model-based RL 或 production robot recovery。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** environment/task/policy family披露；训练硬件、precision、并行环境数、完整 sample budget 与 real-time SLO 为 Not Disclosed。
- **What the Evidence Actually Proves:** benchmark decomposition 可把“需要历史”从一般控制难度中部分隔离；同一任务在 oracle/dense 与 partial/sparse contract 下呈现不同失败面。
- **What It Does Not Prove:** 不证明 LSTM 是最佳 memory、仿真成功能迁移真实机器人、所有失败都来自 memory，或 benchmark taxonomy覆盖真实长期 agent state。
- **Limitations / Threats to Validity:** simulator/task设计、reward shaping与 observation schema决定难度；baseline较窄；缺真实硬件、domain randomization与 long-horizon safety；无统一 compute budget披露。
- **Trade-offs / New Failure Modes:** 显式 memory benchmark提高诊断性，却新增 benchmark overfitting、hidden-state leakage、reward shortcut、recurrent-state reset bug 与 task-family coverage bias。
- **Where the Previous Design Still Applies:** 完全 Markov、短 horizon 或状态估计由外部系统可靠提供时，memoryless policy更易训练、验证与部署。
- **Evolution Relationship:** `Direct Evolution`：aggregate RL task score → controlled memory taxonomy → embodied partial-observation stress；不是从无记忆到必有记忆的单向替代。
- **ROADMAP Node:** Primary `AGENT-MEMORY`；handoff `MULTIMODAL-EMBODIED-VLA`、`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读 Ch26 Embodied VLA、Ch66 Evaluation、Ch76 RAG、Ch77 Memory 与 Ch78 Tool Calling。
- **Existing Coverage:** Ch77 已定义 typed memory/write/read state；MIKASA补充 environment-hidden state 与 policy memory 的可诊断 evaluation contract。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；Historical Books Gate Closed。
- **Changed Files or Rejection Reason:** 仅补 W07；不把 simulator PPO result 外推成机器人能力。
- **Open Questions:** 如何把 memory correctness、staleness、reset、capacity 与 physical safety 分离成可复现的 evaluation slices？

### Cuckoo

- **Candidate / Week / Score:** Cuckoo: An IE-centric Approach to Bootstrapping Generative LLMs for Information Extraction / 2025-W07 / 24/30。
- **Source Family ID:** `arxiv:2502.11275`。
- **Source Type:** Primary research paper + official artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-16；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.11275v1；https://arxiv.org/abs/2502.11275。
- **Related Primary Sources:** paper-linked code/model/data artifacts。
- **Access and Verification Status:** Full Review Complete；data-generation pipeline、objective、baselines、task suites、ablations、appendices 与 limitations 已核验。
- **Full-read Coverage:** motivation/related work、Next-Token Extraction、C4/TuluV3 relabeling、RoBERTa continual pretraining/few-shot adaptation、basic/query/instruction IE evaluation、data ablation、limitations 与 artifact。
- **Original Problem:** extractive IE models需要昂贵结构化 labels，而生成式 LLM 的大规模 pretraining/post-training corpora 已包含可重用文本，却不能直接训练 token-level extractor。
- **Why the Previous Design Was Reasonable:** 人工 NER/RE/QA 标注提供高精度 schema；generative LLM统一任务接口但推理成本高；两者在质量或通用性优先时合理。
- **Changed Constraint:** 希望把已有 LLM data infrastructure 转换为小型 encoder 的 IE supervision，同时覆盖 basic、query-based 与 instruction-following extraction。
- **Mechanism:** Next-Token Extraction 将原文本转为 token extraction/tagging objective，以 C4 与 TuluV3 构造大规模 supervision；RoBERTa先 continual pretrain，再少样本适配具体 IE schema。
- **State Ownership:** source corpus持有原始 provenance；NTE transform持有 label-generation policy；encoder持有通用 extraction representation；task adapter/head持有 schema-specific state。
- **Control Flow / Data Flow:** raw/preference/instruction text→NTE automatic labels→continual encoder training→few-shot task adaptation→span/tag/query extraction。
- **Implementation Details:** 约 102.6M extractive examples；C4与TuluV3两类数据；RoBERTa-based tagger；Rainbow Cuckoo组合数据分支。
- **Evaluation Contract:** NER/RE、SQuAD/SQuADv2/DROP query extraction 与 instruction-following IE；比较 NuNER、MetaIE、MRQA、OPT 等，并分拆 C4-only/Tulu-only/mixed。
- **Baselines / Ablations / Sensitivity / Overhead:** 同规模/资源下的 encoder和 generative baselines、source-data ablation与模型变体；未给出跨所有 schema 的统一 annotation-noise审计。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/data/task披露；训练 hardware、precision、sequence length、batch、online concurrency与SLO在可见 v1 中 Not Disclosed。
- **What the Evidence Actually Proves:** 在作者任务集上，将 LLM corpus重标成 extractive objective 可为小 encoder提供可迁移 supervision；source mixture 对任务族表现有差异。
- **What It Does Not Prove:** 不证明自动 labels 等同人工 ground truth、IE 可覆盖开放生成、102.6M样本都独立高质量，或方法对任意 language/domain/schema有效。
- **Limitations / Threats to Validity:** generative label enumeration效率问题；只系统研究 C4 source；small RoBERTa capacity可能饱和；自动 labeling继承 source noise、license与偏差；硬件/成本未披露。
- **Trade-offs / New Failure Modes:** 复用现有 data pipeline降低专门标注成本，却新增 objective-induced label bias、span boundary error、schema drift、source provenance继承与 duplicate supervision。
- **Where the Previous Design Still Applies:** 高风险 schema、精确 ontology、长尾实体或审计要求高时，人工标注与 task-specific extractor仍更可靠；开放输出需求仍需 generative model。
- **Evolution Relationship:** `Principle Reuse`：generative corpus → objective-specific relabeling → small encoder specialization；不是生成式模型被 encoder 替代。
- **ROADMAP Node:** Primary `TRAIN-DATA`；handoff `TRAIN-PRETRAINING`、`TRAIN-SFT`。
- **Target and Adjacent Chapters Read:** 已读 Ch27 Data、Ch28 Pretraining、Ch29 SFT 与 Ch30 LoRA。
- **Existing Coverage:** Ch27 已将 data pipeline视为可执行 specification；Cuckoo补充同一 corpus经 objective transform产生不同 capability contract。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；Historical Books Gate Closed。
- **Changed Files or Rejection Reason:** 仅补 W07；不把自动 supervision 数量当作 ground-truth 数量。
- **Open Questions:** NTE transform 的版本、误标率、license inheritance 与 schema supersession 如何进入 dataset manifest 和 release gate？

### Show Me the Work

- **Candidate / Week / Score:** Show Me the Work: Fact-Checkers' Requirements for Explainable Automated Fact-Checking / 2025-W07 / 24/30。
- **Source Family ID:** `arxiv:2502.09083`。
- **Source Type:** Primary qualitative research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-13；CHI 2025；W07 锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.09083v1；https://arxiv.org/abs/2502.09083。
- **Related Primary Sources:** interview protocol and paper appendices where provided。
- **Access and Verification Status:** Full Review Complete；study design、participant context、coding/themes、findings、design implications 与 limitations 已核验。
- **Full-read Coverage:** AFC/XAI background、10-professional fact-checker interviews、analysis method、process/evidence/uncertainty requirements、reader-vs-operator explanation、tool triangulation、limitations 与 design implications。
- **Original Problem:** automated fact-checking often exposes verdict/confidence or post-hoc rationale，却不提供专业 fact-checker需要的 evidence path、source quality、uncertainty与可复验操作。
- **Why the Previous Design Was Reasonable:** 单一 verdict/confidence适合快速筛选和大规模 triage；面向普通读者的简短 explanation可降低认知负担，在低风险场景仍有价值。
- **Changed Constraint:** 专业 operator要承担发布责任，必须知道系统如何检索、为何信任来源、哪些步骤可重复，以及 uncertainty来自 evidence还是 model。
- **Mechanism:** 通过半结构化访谈归纳 explanation contract：展示 process、evidence-source relation、uncertainty、replicability与 verifiability，并区分给 reader 的叙事与给 operator 的 decision trace。
- **State Ownership:** evidence store持有原始来源；retrieval/verification pipeline持有过程轨迹；scorer持有 verdict与 uncertainty；human fact-checker持有最终 editorial decision。
- **Control Flow / Data Flow:** claim→search/query trail→source selection与quality judgment→evidence-to-claim relation→provisional verdict/uncertainty→human triangulation→publish/reject/revise。
- **Implementation Details:** 10 名多国专业 fact-checkers，约1小时 Zoom 半结构化访谈，参与补偿50美元；质性编码形成主题，不实现 production AFC system。
- **Evaluation Contract:** 研究对象是 operator requirements，不是模型准确率；证据来自 participant narratives、cross-participant themes 与 examples。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较现有 AFC/XAI输出与工作实践需求；没有系统 benchmark、A/B test或 causal ablation，不能量化界面效果。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 不适用；participant/sample/protocol已披露，任何运行时模型硬件指标均不存在。
- **What the Evidence Actually Proves:** 该样本中的专业 fact-checkers重视可追溯过程与 source reliability，且 operator explanation 与公众 explanation 是不同 contracts。
- **What It Does Not Prove:** 不定义通用 UI、不证明某 explanation 提高准确率、不代表所有国家/语言/组织，也不验证 LLM rationale 等于真实执行轨迹。
- **Limitations / Threats to Validity:** 样本小、English interviews、自我报告、专业背景异质、无部署实验；研究者编码与招募可能影响主题。
- **Trade-offs / New Failure Modes:** 详细 decision trace提高审计和复验，却增加认知负担、敏感 source exposure、日志成本与 automation bias；伪造的“过程解释”比无解释更危险。
- **Where the Previous Design Still Applies:** 面向读者的低风险摘要或大规模初筛仍可使用简洁 verdict/confidence，但不得替代 operator evidence view。
- **Evolution Relationship:** `Direct Evolution`：verdict → rationale → evidence-linked execution trace；reader summary保持 `Alternative Branch`。
- **ROADMAP Node:** Primary `PLATFORM-EVALUATION-SYSTEM`；handoff `PLATFORM-OBSERVABILITY`、`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读 Ch65 Evidence/Observability相邻内容、Ch66 Evaluation 与 Ch72 Security/Governance边界。
- **Existing Coverage:** Ch66 已定义 claim→evidence→measurement→decision；本文补充 human operator对可复验 process lineage 的需求证据。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；Historical Books Gate Closed。
- **Changed Files or Rejection Reason:** 仅补 W07；质性发现不外推成统一产品规范。
- **Open Questions:** 如何让系统展示真实 query/retrieval/scoring trace，同时保护 source隐私、控制认知负担并防止 post-hoc rationale冒充 execution evidence？

### Data-Efficient Pretraining for Atomic Property Prediction

- **Candidate / Week / Score:** Towards Data-Efficient Pretraining for Atomic Property Prediction / 2025-W07 / 26/30。
- **Source Family ID:** `arxiv:2502.11085`。
- **Source Type:** Primary research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-16；v2 2026-01 修改标题/实验；W07只使用 v1 标题与证据。
- **Direct Primary Sources:** https://arxiv.org/html/2502.11085v1；https://arxiv.org/abs/2502.11085。
- **Related Primary Sources:** paper-linked model/data artifacts and cited EquiformerV2/JMP baselines。
- **Access and Verification Status:** Full Review Complete；v1 method、CSI、datasets、budget定义、ID/OOD experiments、baselines、appendices 与 revision boundary 已核验。
- **Full-read Coverage:** motivation/related work、computational budget、chemical similarity index、feature extraction/sampling、GemNet/JMP setup、rMD17/MD22/SPICE/QM9/QMOF/MatBench evaluation、ID/OOD analysis、appendices；无独立 limitations 章节。
- **Original Problem:** atomic foundation pretraining常把“更多结构”当作默认改进，却忽略固定 compute budget 下数据与 downstream chemistry 的相似性，混合大量不相关数据可能稀释有效更新。
- **Why the Previous Design Was Reasonable:** 大规模 diverse pretraining扩大覆盖并支持未知 downstream tasks；若模型会复用到多个领域或 OOD是目标，规模和多样性仍有价值。
- **Changed Constraint:** 目标任务已知且 pretraining compute受限时，需要在样本数之外度量 upstream-downstream alignment，决定把有限 steps给哪类结构。
- **Mechanism:** 定义 `C = epochs × unique samples processed` 的预算；用 OC20-pretrained EquiformerV2 node embeddings构造 Chemical Similarity Index，比较 ANI-1x、Transition-1x、OC20、OC22及混合数据，再训练 GemNet/JMP。
- **State Ownership:** dataset manifest持有 chemical distribution/provenance；feature extractor版本持有 CSI geometry；sampling policy持有 compute allocation；checkpoint持有 learned representation；downstream split持有 target contract。
- **Control Flow / Data Flow:** upstream candidates→fixed feature extractor→balanced sample embeddings→CSI ranking→budget-constrained sampling/pretraining→downstream fine-tuning→ID/OOD metrics。
- **Implementation Details:** CSI使用 EquiformerV2 features与图级聚合，class-balanced sampling约10k；比较 GemNet-OC-S/L和JMP；v1 limited budget 10M samples versus JMP 240M reference。
- **Evaluation Contract:** ID: rMD17、MD22、SPICE、QM9；OOD: QMOF/MatBench等；比较相同/不同 upstream mixtures、budget与模型规模；任务指标按 property dataset定义。
- **Baselines / Ablations / Sensitivity / Overhead:** random/mixed/single-source pretraining、10M vs larger budget、GemNet variants与JMP；ID中 aligned data常更好，OOD中 diversity可反超，CSI在部分 OOD dataset不稳定。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** data/model/sample budget披露；hardware、precision、batch、wall-clock/energy与 serving SLO为 Not Disclosed。
- **What the Evidence Actually Proves:** 在作者 atomic datasets 与固定样本预算下，task-aligned upstream data可比盲目混合更有效；增加不相似数据在 ID场景可能伤害，但 OOD可能需要多样性。
- **What It Does Not Prove:** 不证明小数据普遍优于大数据、CSI是因果/通用 data-quality metric、10M与240M是等 FLOP，或 atomic结论可直接迁移语言/视觉。
- **Limitations / Threats to Validity:** CSI依赖 feature extractor、sampling与graph aggregation；hardware/FLOP未披露；domain限定原子系统；target已知假设不适用于开放 foundation model；v2新增证据不能回写v1。
- **Trade-offs / New Failure Modes:** alignment提高固定预算效率，却新增 target overfitting、embedding-version coupling、selection bias、覆盖缺失与 OOD regression；diverse mixture则付出更多无效更新换未知任务保险。
- **Where the Previous Design Still Applies:** downstream未知、多任务复用、OOD覆盖优先或 selection metric不可靠时，大规模 diverse pretraining仍合理。
- **Evolution Relationship:** `Direct Evolution`：scale-first collection → budget-aware aligned selection → alignment/diversity conditional branch。
- **ROADMAP Node:** Primary `TRAIN-DATA`；handoff `TRAIN-PRETRAINING`、`PLATFORM-COST`、`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读 Ch27 Data、Ch28 Pretraining、Ch66 Evaluation 与 Ch70 Cost。
- **Existing Coverage:** Ch27 已强调 sampling weights定义训练分布；本文补充 fixed-budget下 alignment metric本身也必须 version和验证。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；Historical Books Gate Closed。
- **Changed Files or Rejection Reason:** 仅补 W07；保留 v1 标题、10M sample budget与 Not Disclosed FLOP边界。
- **Open Questions:** data-alignment scorer怎样跨 feature extractor版本校准，并把 OOD coverage risk与 compute savings共同纳入 sampling policy？

### MUDDFormer: From One Accumulated Residual Stream to Token-conditioned Multiway Depth Routing

- **Candidate / Week / Score:** MUDDFormer: Breaking Residual Bottlenecks in Transformers via Multiway Dynamic Dense Connections / 2025-W07 / 28/30（Technical Novelty 5、System Impact 5、Practical Value 4、Source Reliability 4、Project Relevance 5、Longevity 5）。
- **Source Family ID:** `muddformer-multiway-dynamic-dense-connections`。
- **Source Type:** arXiv author paper（v1）+ official JAX/PyTorch repository + pretrained-model links；后续 ICML 接收与 v2 只作 revision lineage。
- **First-public Date / Revision History:** arXiv v1 2025-02-13 10:26:27 UTC，属于 W07；v2 2025-05-28，不能把后续会议/文本变化倒写成 W07 事实。W08 ledger 原以 2 月17日 discovery/recommendation date 归档，现已纠正。
- **Direct Primary Sources:** https://arxiv.org/html/2502.12170v1；https://arxiv.org/abs/2502.12170；https://github.com/Caiyun-AI/MUDDFormer。
- **Related Primary Sources:** official repository 同时提供 JAX training、PyTorch inference 与三个 model links；当前 `main` 已有 20 commits，但公开页面未给出可唯一锁定到 2025-02-13 的 immutable commit，因此只验证公开机制与 artifact family，不把当前代码状态冒充 event-time implementation。
- **Access and Verification Status:** Verified for v1 paper, equations, pseudocode, experiments, ablations, efficiency contract and current official artifact identity；event-time commit、container、dataset/checkpoint digest 为 Not Disclosed。
- **Full-read Coverage:** metadata/revision、Abstract、Introduction、Method 2.1～2.6、scaling、300B-token Pythia training、downstream evaluation、representation/head analysis、training/inference efficiency、component/sparsity ablations、Related Work、Conclusion、pseudocode、complexity derivation、hyperparameters/baselines、ViT appendix 与 visualization；论文没有独立 Limitations / Threats section，限制由实验合同与未披露项重建。
- **Original Problem:** 标准 Transformer 把所有早期层信息压进单个逐层累加的 residual stream。它提供稳定 shape 与 identity path，却让后层无法显式区分历史来源；深层表示相似、部分深层可删除和跨层 circuit 通信受限提示 residual channel 可能成为 depth bottleneck。
- **Why the Previous Design Was Reasonable:** `x + F(x)` 的状态、参数和执行都简单，支持成熟的逐层 kernel、activation checkpointing、Pipeline Parallel 与 per-layer KV ownership；在中等深度、吞吐或跨 stage 带宽优先时，单一 residual stream 仍是低风险默认方案。
- **Changed Constraint:** 当模型希望从更深网络获得增益、不同 token 需要读取不同历史层、且 Q/K/V/Residual 四种输入承担不同语义时，固定等权累加或跨 token 共享的静态 layer weights 缺少 source identity 与 input-conditioned routing。
- **Mechanism:** 演进链是 `single residual → static dense layer weighting → per-token dynamic depth weighting → Q/K/V/R four-way dynamic depth weighting`。第 `i` 层用 `GELU(RMSNorm(X_i)W1)W2 + a_i` 生成每个 token 对 `X_0...X_i` 的权重；四个 Depth-wise Aggregate 分别构造下一 block 的 Q、K、V、Residual 输入。上层 FFN 宽度再从 `0.5 d_ff` 线性增加到 `1.5 d_ff`，保持总 FFN 参数预算近似不变；高 depth/width 比可选 PrePostDANorm。
- **State Ownership:** checkpoint 拥有每层四路 DA 参数、static prior、FFN width schedule 与可选 norm；training runtime 拥有全部历史 activations、反向图、重算与跨 stage transport；inference runtime 必须持有或增量归约 depth-history state，并保持 Q/K/V/R、layer、token、request 与 checkpoint identity；repository/model card 应拥有 code/model digest，但 event-time digest 未披露。
- **Control Flow / Data Flow:** embedding `X0` 进入历史列表；第 `i` 个 block 使用上一步形成的四路 aggregate 计算 Attention/FFN 得到 `Xi`；`Xi` 追加到 history；由当前 hidden state 生成四组 token-wise layer weights；加权历史输出形成下一层 Q/K/V/R；最后返回 residual aggregate。该路径把横向 token Attention 与纵向 depth routing 组合，却也让每层依赖所有被保留历史 states。
- **Implementation Details:** `W2=0`，static prior 在当前层位置初始化为 1、其余为 0，使训练起点退化为普通 Transformer；作者指出该初始化对性能关键。理论额外参数约 `eta/6`，额外 FLOPs 约 `eta/(3+rho/4)`，其中 `eta=(L+3)/D`、`rho=T/D`；v1 实现用 JAX 训练、PyTorch 2.5.1 `torch.compile` 推理，没有自定义 Pallas/Triton kernel。全量 1x1 depth connectivity 最强但 I/O 较高，2x2 dilation/periodicity 是稀疏折中。
- **Evaluation Contract:** scaling sweep 覆盖 405M/7B、834M/15B、1.4B/26B tokens 及 34/42-layer deep-narrow variants，context 2048；large-scale 训练 MUDDPythia 1.4B/2.8B 于 Pile 300B tokens，并用 LM Evaluation Harness 做 0-shot/5-shot；ViT-S/16 在 ImageNet-1k 以 90/300 epochs 作跨模态附录。作者同时测试 untrained Transformer++ shape 的训练/推理效率。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比 Transformer、Transformer++、DenseFormer、Hyper-Connections、DDFormer；405M ablation 逐步加入 static、dynamic、multiway、FFN reallocation，并逐路移除 Q/K/V/R dense connection，V/R 移除影响最大。全连接、2x2 与 sliding-window variants 展示 quality/throughput trade-off；没有多 seed/error bars、跨数据集 language replication、optimizer/length/topology 全面 sensitivity 或独立 reproduction。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** training efficiency：TPU v5p-128、Transformer++ shape 1.3B/2.8B/6.9B、context 2048、batch 2M tokens，MUDD throughput 为 baseline 的 89.8%/84.0%/95.6%；inference：单 NVIDIA A100 80GB、prompt 4096、batch 1、生成 128 tokens、3 次均值，MUDD speed 为 88.1%/90.0%/94.0%。训练/推理 precision、warmup、并发、prefill/decode 分解、p50/p99、TP/PP topology 与 SLO 为 Not Disclosed。
- **What the Evidence Actually Proves:** 在作者 v1 的 Pile/Pythia 与 Transformer++ 配方内，动态、multiway 和长程 depth connections 分别有增量；MUDDPythia 2.8B 的 Pile perplexity 与平均下游结果接近 Pythia 6.9B，MUDDFormer 2.8B 配方在所列 0/5-shot 平均值上更高。理论 FLOPs 增量很小，但真实吞吐损失显著高于 FLOPs 估计，证明 small ops 与 I/O 必须单独计量。
- **What It Does Not Prove:** `1.8x～2.4x compute` 是 loss-curve / model comparison 下的作者等效估计，不是等 wall-clock、等能耗、等硬件或生产 SLO 证明；attention-head activation 是作者定义的相关性指标，不因 2.4x 激活率就因果证明 in-context learning 机制；ViT 单数据集结果不证明通用 multimodal 优势；当前 repository 也不是 v1 结果的独立复现。
- **Limitations / Threats to Validity:** 论文无独立 limitations section；语言证据集中 Pile/Pythia、最大 2.8B MUDD model、context 2048/4096 与有限 downstream suites；没有 seed uncertainty；效率在 untrained models 上测量；作者训练结果与硬件效率不是同一模型/同一环境；全历史 activation residency、Pipeline stage crossing、checkpoint conversion、KV migration 和 failure recovery 未量化；current repo 到 event-time commit 的 lineage 不完整。
- **Trade-offs / New Failure Modes:** 显式 depth source identity 与 per-token routing换来更强深层表达和条件路径，却增加 activation memory、small-op launch、read/write traffic、kernel fusion需求与跨 stage communication；dynamic weights 可能饱和或错路由，历史 state 丢失/错序会污染四路输入，稀疏连接可恢复速度但损失部分 long-range path，FFN reallocation 与 MUDD 还存在配方耦合。
- **Where the Previous Design Still Applies:** 模型较浅、batch/latency 可预测性优先、Pipeline bandwidth 紧张、serving stack 未支持 depth-state lifecycle、或增益没有在目标数据/规模复现时，标准 Pre-Norm residual 仍更合理；static/sparse depth aggregation适合动态路由成本过高但希望保留部分 layer identity 的场景。
- **Evolution Relationship:** `Direct Evolution`：单一累加 residual → 静态跨层聚合 → token-conditioned depth routing → Q/K/V/R 多路 routing；`Alternative Branch`：全 dense、dilated/periodic sparse、sliding window 与普通 residual 按 quality、memory、communication、latency 条件共存，不是后者必然替代前者。
- **ROADMAP Node:** canonical owner `MODEL-TRANSFORMER-LAYER`（Current Ch17；Legacy Ch17）；handoffs to `MODEL-SELF-ATTENTION`、`MODEL-FFN`、`MODEL-DECODER-ONLY`、`TRAIN-PRETRAINING`、`TRAIN-DISTRIBUTED-TRAINING`、`INFER-TENSORRT-LLM` 与 `PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** read Part II guide and full Ch16 FFN、Ch17 Transformer Layer、Ch18 Decoder-only；inspected Ch28 Pretraining、Ch36 Distributed Training、Ch49 GPU Execution 与 Ch66 Evaluation boundaries。Ch17 owns residual/depth routing，Ch16 owns width reallocation，Ch28 owns training recipe，Ch36 owns activation/stage communication，Ch49 owns realized kernel/I/O cost，Ch66 owns comparable workload evidence。
- **Existing Coverage:** Ch17 已从 single residual、gated/scaled carry-transform、explicit depth-history selection 写到 block summaries / bounded slots，并明确 activation、跨 stage transport 与推理 I/O 成本；MUDDFormer 提供一个更早且机制更具体的四路动态 dense branch，以及“理论 FLOPs 很小但实测吞吐仍下降”的证据。该证据值得未来 refine 既有论证，但不需要新增章节，也不能在 Historical Books Gate 关闭时写入正文。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；future Books Gate should place the durable residual-to-depth-routing evolution in Ch17 and use only short handoffs to Ch16/Ch36/Ch49；不把 MUDDFormer 写成标准 Transformer 的必然替代。
- **Changed Files or Rejection Reason:** corrected owner Week from W08 to W07；added v1-locked score、30-field Source Review、artifact/revision boundary、workload contract、Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** event-time commit/model/data/container digests；v1→v2 exact claim/code delta；trained-model serving under batch>1、long context、TP/PP and tail SLO；activation/checkpoint/communication growth by depth；fused-kernel feasibility；routing collapse/robustness；seed uncertainty and independent reproduction；MoE/long-context/speculation compatibility；depth-state migration, rollback and fault recovery。

### Spillback Low-Score Verification

- **We Can't Understand AI Using Our Existing Vocabulary** — `arxiv:2502.07586`，v1 2025-02-11，18/30。正文是关于 human-machine conceptual vocabulary 的 position paper，提出问题与术语建议，但没有新的 executable mechanism、implementation 或可验证 system contract；`Weekly Only`。Primary: https://arxiv.org/abs/2502.07586。
- **AdaPTS** — `arxiv:2502.10235`，v1 2025-02-14，19/30。论文以 adapters 把 multivariate series 映射到 latent dimensions，使 independent univariate forecasting foundation model可复用；机制可读，但证据集中于 time-series forecasting、owner与本书现有 data/representation主线的长期增量有限，且不提升为通用 multivariate architecture结论；`Weekly Only`。Primary: https://arxiv.org/html/2502.10235v1。
- **Agentic End-to-End Protein Design / VibeGen** — `arxiv:2502.10173`，v1 2025-02-14，19/30。公开材料描述由 LLM/agents编排 protein generation、filtering与analysis 的领域 workflow，但实验集中于 protein-design case，artifact/evaluator与 wet-lab validity不足以形成跨域 Agent机制；`Weekly Only — Domain Case`。Primary: https://arxiv.org/html/2502.10173v1。
- **Ask in Any Modality: A Comprehensive Survey on Multimodal Retrieval-Augmented Generation** — `arxiv:2502.08826`，v1 2025-02-12，19/30。作为 survey 能帮助 taxonomy/discovery，但不提供新的 primary mechanism或独立实验；其引用的具体方法应回到各自 Source Family审计，不能用 survey 替代；`Weekly Only — Survey`。Primary: https://arxiv.org/html/2502.08826v1。

## Evidence Level

- 当前 51 项 `20+` 候选均回到 arXiv HTML/PDF、官方 Blog、公开 v1 全文镜像或作者 artifact 并形成 30 字段 Full Source Review；22 项低分均完成 identity/date/score/rejection 核验，因此 W07 Candidate Evidence Gate Passed。
- 作者 benchmark 只证明披露模型、数据、硬件与实现下的结果；缺失 hardware、precision、batch、concurrency 或 SLO 时显式记录 Not Disclosed。
- 跨论文的技术演进和 ROADMAP owner 是本项目推断，不冒充作者结论。
- 低分候选仍保留 primary identity、first-public date 与拒绝原因，后续出现新证据可重开 Source Family。

## Cross-Week Deduplication and Spillback

- 以 Source Family ID + primary identifier + first-public date 去重；revision 不重复计分。
- CODESIM（2502.05664）、UniCMs（2502.05415）、Competitive Programming（2502.06807）、APE（2502.05431）、Hypencoder（2502.05364）、Éclair（2502.04223）、CAD-Editor（2502.03997）均早于 W07，进入 W06 或更早周 spillback ledger。
- vLLM 0.7.3、Transformers 4.49 等正式事件归 W08；NSA 虽被后续 discovery page 再次推荐，owner 仍为 W07。
- MUDDFormer 的 arXiv v1 是 2025-02-13；2 月17日只是一条后续 discovery/recommendation 线索，owner 已从 W08 纠正为 W07。5 月 v2 与当前 repository 只作 revision/artifact lineage，不重复计分。
- 同一 family 的后续实验、release 或工程集成只建立 evolution link，不用后发版本覆盖 v1 边界。

## Knowledge Tree Position

- Model / Training: WORLDVIEW-SCALING-LAW、MODEL-TRANSFORMER-LAYER、MODEL-LONG-CONTEXT、TRAIN-DATA、TRAIN-PRETRAINING、TRAIN-DISTRIBUTED-TRAINING、TRAIN-RLHF/PPO/GRPO。
- Inference / Runtime: INFER-KV-CACHE、INFER-SPECULATIVE-DECODING、INFER-SCHEDULING、INFER-TENSORRT-LLM。
- Platform / Security: PLATFORM-MODEL-REGISTRY、PLATFORM-MULTI-TENANT、PLATFORM-SECURITY、PLATFORM-COST。
- Agent / Multimodal handoff: AGENT-WORKFLOW、AGENT-TOOL-CALLING、MULTIMODAL-REPRESENTATION、PLATFORM-EVALUATION-SYSTEM。

## Recommended Action

- 当前 51 个高分 Source Family：Weekly evidence complete；全部进入 Books Pending，不在 Historical Books Gate 开启前写入 Books。MUDDFormer 后续应在 Ch17 refine 既有 depth-routing 论证，而不是新增论文式章节。
- 22 个低分候选：Weekly only；其中 4 项来自 W08 look-ahead spillback，均已完成 identity、日期、评分与拒绝边界核验。
- 前周 spillback：在对应 owner Weekly 独立补录和验收，不在 W07 冒充完成。

## Event-Date Daily Decision

历史回填不创建 Daily。事件日、版本边界、spillback 与 source family 直接记录在 Weekly。

## Books Integration Decision

Historical Books Gate: Closed。W07 没有执行 Books Integration；旧版“Books Gate 已完成”和 changed books paths 均已撤回。Must Read 只表示值得进入后续 Books Gate，不等于已修改书稿。

## Ignored Noise

- 纯产品宣传、未提供 primary source 的转述、issue-level 使用问题、预发布分支与无 workload contract 的排行榜。
- Hugging Face 推荐日期、搜索抓取日期、后续论文 revision 日期不作为 first-public date。
- Narrow application paper 不是因为主题不重要被删除，而是因本周未形成新的长期 AI-system ownership/mechanism 进入低分账本。

## Repository Changes

- 幂等重建 papers/2025/weekly/2025-W07/README.md。
- 更新 papers/2025/weekly/README.md 的年度 census、cursor 与 spillback 状态。
- 本周未修改 books/，未执行 stage、commit 或 push。

## Open Questions

- Prompt cache tenant scoping 如何与 prefix-sharing 收益、constant-time mitigation 和 organization policy 共同建模？
- LASP-2 在不同拓扑、world size 与 hybrid ratio 下何时优于 ring？
- Distillation law 如何扩展到 post-training、多模态与 teacher reuse accounting？
- TTS/OREAL 的 verifier drift、budget fairness 与 tail latency 如何进入 production contract？
- InSTA/Hephaestus 的 web/API provenance、删除、过期与 judge calibration 如何审计？
- Conditional pruning、multi-CAV fusion 与 memory benchmark 如何把 state identity、freshness 与 failure recovery 纳入统一 evaluation contract？
- Data alignment、adapter capacity 与 corpus relabeling 的选择策略如何在预算、覆盖和 OOD 风险之间校准？
- Dynamic depth routing 在 TP/PP、activation recomputation、长上下文和 batch>1 serving 下的 memory/communication/tail-latency contract 如何建立？

## Sources

- Online Scheduling for LLM Inference with KV Cache Constraints — https://arxiv.org/abs/2502.07115（First Public: 2025-02-10；Accessed: 2026-08-18）
- Native Sparse Attention — https://arxiv.org/abs/2502.11089（First Public: 2025-02-16；Accessed: 2026-08-18）
- Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling — https://arxiv.org/abs/2502.06703（First Public: 2025-02-10；Accessed: 2026-08-18）
- Exploring the Limit of Outcome Reward for Learning Mathematical Reasoning (OREAL) — https://arxiv.org/abs/2502.06781（First Public: 2025-02-10；Accessed: 2026-08-18）
- Matryoshka Quantization — https://arxiv.org/abs/2502.06786（First Public: 2025-02-10；Accessed: 2026-08-18）
- Jakiro: Boosting Speculative Decoding with Decoupled Multi-Head via MoE — https://arxiv.org/abs/2502.06282（First Public: 2025-02-10；Accessed: 2026-08-18）
- InSTA: Towards Internet-Scale Training For Agents — https://arxiv.org/abs/2502.06776（First Public: 2025-02-10；Accessed: 2026-08-18）
- Hephaestus: Improving Fundamental Agent Capabilities through Continual Pre-Training — https://arxiv.org/abs/2502.06589（First Public: 2025-02-10；Accessed: 2026-08-18）
- Scaling Pre-training to One Hundred Billion Data for Vision Language Models — https://arxiv.org/abs/2502.07617（First Public: 2025-02-11；Accessed: 2026-08-18）
- Auditing Prompt Caching in Language Model APIs — https://arxiv.org/abs/2502.07776（First Public: 2025-02-11；Accessed: 2026-08-18）
- TransMLA: Multi-Head Latent Attention Is All You Need — https://arxiv.org/abs/2502.07864（First Public: 2025-02-11；Accessed: 2026-08-18）
- Distillation Scaling Laws — https://arxiv.org/abs/2502.08606（First Public: 2025-02-12；Accessed: 2026-08-18）
- LASP-2: Rethinking Sequence Parallelism for Linear Attention and Its Hybrid — https://arxiv.org/abs/2502.07563（First Public: 2025-02-11；Accessed: 2026-08-18）
- MUDDFormer — https://arxiv.org/html/2502.12170v1；artifact: https://github.com/Caiyun-AI/MUDDFormer（First Public: 2025-02-13；Accessed: 2026-08-18）
- Building AI for the pluralistic society — https://research.google/blog/building-ai-for-the-pluralistic-society/（First Public: 2025-02-13；Accessed: 2026-08-18）
- ReasonFlux — https://arxiv.org/abs/2502.06772（First Public: 2025-02-10；Accessed: 2026-08-18）
- EVEv2 — https://arxiv.org/abs/2502.06788（First Public: 2025-02-10；Accessed: 2026-08-18）
- Efficient-vDiT — https://arxiv.org/abs/2502.06155（First Public: 2025-02-10；Accessed: 2026-08-18）
- CodeI/O — https://arxiv.org/abs/2502.07316（First Public: 2025-02-11；Accessed: 2026-08-18）
- LLMs Learn Reasoning from Demonstration Structure — https://arxiv.org/abs/2502.07374（First Public: 2025-02-11；Accessed: 2026-08-18）
- Goedel-Prover — https://arxiv.org/abs/2502.07640（First Public: 2025-02-11；Accessed: 2026-08-18）
- Mask-Enhanced Autoregressive Prediction — https://arxiv.org/abs/2502.07490（First Public: 2025-02-11；Accessed: 2026-08-18）
- Interpretable and Testable Vision Features via SAEs — https://arxiv.org/abs/2502.06755（First Public: 2025-02-10；Accessed: 2026-08-18）
- BenchMAX — https://arxiv.org/abs/2502.07346（First Public: 2025-02-11；Accessed: 2026-08-18）
- LLM Pretraining with Continuous Concepts — https://arxiv.org/abs/2502.08524（First Public: 2025-02-12；Accessed: 2026-08-18）
- WorldGUI — https://arxiv.org/abs/2502.08047（First Public: 2025-02-12；Accessed: 2026-08-18）
- DPO-Shift — https://arxiv.org/abs/2502.07599（First Public: 2025-02-11；Accessed: 2026-08-18）
- Next Block Prediction — https://arxiv.org/abs/2502.07737（First Public: 2025-02-11；Accessed: 2026-08-18）
- EmbodiedBench — https://arxiv.org/abs/2502.09560（First Public: 2025-02-13；Accessed: 2026-08-18）
- Thai Reasoning via Model Merging — https://arxiv.org/abs/2502.09056（First Public: 2025-02-13；Accessed: 2026-08-18）
- Predictive Red Teaming — https://arxiv.org/abs/2502.06575（First Public: 2025-02-10；Accessed: 2026-08-18）
- FailSafe Long-Context QA for Finance — https://arxiv.org/abs/2502.06329（First Public: 2025-02-10；Accessed: 2026-08-18）
- LLaDA / Large Language Diffusion Models — https://arxiv.org/abs/2502.09992（First Public: 2025-02-14；Accessed: 2026-08-18）
- The Danger of Overthinking — https://arxiv.org/abs/2502.08235（First Public: 2025-02-12；Accessed: 2026-08-18）
- Step-Video-T2V — https://arxiv.org/abs/2502.10248（First Public: 2025-02-14；Accessed: 2026-08-18）
- Region-Adaptive Sampling — https://arxiv.org/abs/2502.10389（First Public: 2025-02-14；Accessed: 2026-08-18）
- ZeroBench — https://arxiv.org/abs/2502.09696（First Public: 2025-02-13；Accessed: 2026-08-18）
- MM-RLHF — https://arxiv.org/abs/2502.10391（First Public: 2025-02-14；Accessed: 2026-08-18）
- ImageRAG — https://arxiv.org/abs/2502.09411（First Public: 2025-02-13；Accessed: 2026-08-18）
- DarwinLM — https://arxiv.org/abs/2502.07780（First Public: 2025-02-11；Accessed: 2026-08-18）
- FoNE — https://arxiv.org/abs/2502.09741（First Public: 2025-02-13；Accessed: 2026-08-18）
- Precise Parameter Localization for Textual Generation — https://arxiv.org/abs/2502.09935（First Public: 2025-02-14；Accessed: 2026-08-18）
- Selective Self-to-Supervised Fine-Tuning — https://arxiv.org/abs/2502.08130（First Public: 2025-02-12；Accessed: 2026-08-18）
- STMA — https://arxiv.org/abs/2502.10177（First Public: 2025-02-14；Accessed: 2026-08-18）
- CRANE — https://arxiv.org/abs/2502.09061（First Public: 2025-02-13；Accessed: 2026-08-18）
- The Mirage of Model Editing — https://arxiv.org/abs/2502.11177（First Public: 2025-02-16；Accessed: 2026-08-18）
- I Think, Therefore I Diffuse — https://arxiv.org/abs/2502.10458（First Public: 2025-02-14；Accessed: 2026-08-18）
- ReLearn — https://arxiv.org/abs/2502.11190（First Public: 2025-02-16；Accessed: 2026-08-18）
- Knowledge Circuits for Continual Pre-Training — https://arxiv.org/abs/2502.11196（First Public: 2025-02-16；Accessed: 2026-08-18）
- IHEval — https://arxiv.org/abs/2502.08745（First Public: 2025-02-12；Accessed: 2026-08-18）
- Talk Structurally, Act Hierarchically — https://arxiv.org/abs/2502.11098（First Public: 2025-02-16；Accessed: 2026-08-18）
- Dyve — https://arxiv.org/abs/2502.11157（First Public: 2025-02-16；Accessed: 2026-08-18）
- CALM — https://arxiv.org/abs/2502.08820（First Public: 2025-02-12；Accessed: 2026-08-18）
- SURGE — https://arxiv.org/abs/2502.11167；v1 PDF: https://arxiv.org/pdf/2502.11167v1（First Public: 2025-02-16；Accessed: 2026-08-18）
- EQ-VAE — https://arxiv.org/abs/2502.09509（First Public: 2025-02-13；Accessed: 2026-08-18）
- CounterMATH — https://arxiv.org/abs/2502.10454（First Public: 2025-02-12；Accessed: 2026-08-18）
- Diverse Inference and Verification for Advanced Reasoning — https://arxiv.org/abs/2502.09955；v1 full-text mirror: https://www.researchgate.net/publication/389055678_Diverse_Inference_and_Verification_for_Advanced_Reasoning（First Public: 2025-02-14；Accessed: 2026-08-18）
- Better Embeddings with Coupled Adam — https://arxiv.org/html/2502.08441v1（First Public: 2025-02-12；Accessed: 2026-08-18）
- Data Valuation using Neural Networks for Efficient Instruction Fine-Tuning — https://arxiv.org/html/2502.09969v1（First Public: 2025-02-14；Accessed: 2026-08-18）
- Cluster and Predict Latent Patches for Improved Masked Image Modeling — https://arxiv.org/html/2502.08769v1（First Public: 2025-02-12；Accessed: 2026-08-18）
- small Models, BIG Impact — https://arxiv.org/html/2502.10140v1；code: https://github.com/d-gurgurov/Knowledge-Driven-Adaptation-LLMs（First Public: 2025-02-14；Accessed: 2026-08-18）
- Text-guided Sparse Voxel Pruning for Efficient 3D Visual Grounding — https://arxiv.org/html/2502.10392v1（First Public: 2025-02-14；Accessed: 2026-08-18）
- V2V-LLM — https://arxiv.org/html/2502.09980v1（First Public: 2025-02-14；Accessed: 2026-08-18）
- MRS: A Fast Sampler for Mean Reverting Diffusion — https://arxiv.org/html/2502.07856v1（First Public: 2025-02-11；Accessed: 2026-08-18）
- CLaMP 3 — https://arxiv.org/html/2502.10362v1；artifact: https://github.com/sanderwood/clamp3（First Public: 2025-02-14；Accessed: 2026-08-18）
- Memory, Benchmark & Robots / MIKASA — https://arxiv.org/html/2502.10550v1（First Public: 2025-02-14；Accessed: 2026-08-18）
- Cuckoo — https://arxiv.org/html/2502.11275v1（First Public: 2025-02-16；Accessed: 2026-08-18）
- Show Me the Work — https://arxiv.org/html/2502.09083v1（First Public: 2025-02-13；Accessed: 2026-08-18）
- Towards Data-Efficient Pretraining for Atomic Property Prediction — https://arxiv.org/html/2502.11085v1（First Public: 2025-02-16；Accessed: 2026-08-18）
- We Can't Understand AI Using Our Existing Vocabulary — https://arxiv.org/abs/2502.07586（First Public: 2025-02-11；Accessed: 2026-08-18）
- AdaPTS — https://arxiv.org/html/2502.10235v1（First Public: 2025-02-14；Accessed: 2026-08-18）
- Agentic End-to-End Protein Design / VibeGen — https://arxiv.org/html/2502.10173v1（First Public: 2025-02-14；Accessed: 2026-08-18）
- Ask in Any Modality survey — https://arxiv.org/html/2502.08826v1（First Public: 2025-02-12；Accessed: 2026-08-18）
