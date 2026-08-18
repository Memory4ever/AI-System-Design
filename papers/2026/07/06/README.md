# Daily Research — 2026-07-06

**Research Date:** 2026-07-06

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-05 09:00:00 ～ 2026-07-06 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 537 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 7 个。当前路由账目为 2 个 Deep、2 个 Standard、3 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-06 |
| Window End | 2026-07-06 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-06-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-26T18:00:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-05T09:00:00+08:00 | 2026-07-06T09:00:00+08:00 | 2026-08-26T18:00:00+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 537 | SF-2026-ARXIV-2607-04171<br>SF-2026-ARXIV-2607-04181<br>SF-2026-ARXIV-2607-04292<br>SF-2026-ARXIV-2607-04302<br>SF-2026-ARXIV-2607-04391<br>SF-2026-ARXIV-2607-04395<br>SF-2026-ARXIV-2607-04517 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-06T09:00:00+08:00 | coverage:SRC-ARXIV:20260706 | GAP-ARXIV-DIRECT-RESET-20260706 |

<!-- coverage:SRC-ARXIV:20260706:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 537 unique identities in this strict window; 7 routed families.<!-- coverage:SRC-ARXIV:20260706:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 7 个 family：exact v1 为 0 个 family 披露 artifact/evidence locator，其中 0 个提供外部 repository/project/demo locator，另有 7 个未披露；本日确认 0 个 family、0 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-04171 | arXiv:2607.04171v1 | paper-v1:2607.04171 | 2026-W27 | 2026-07-05 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-04171 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-04181 | arXiv:2607.04181v1 | paper-v1:2607.04181 | 2026-W27 | 2026-07-05 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-04181 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2607-04181 | yes |
| SF-2026-ARXIV-2607-04292 | arXiv:2607.04292v1 | paper-v1:2607.04292 | 2026-W27 | 2026-07-05 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-04292 | self | — | new_in_window | AGENT-MULTI-AGENT | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-04302 | arXiv:2607.04302v1 | paper-v1:2607.04302 | 2026-W27 | 2026-07-05 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-04302 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2607-04302 | yes |
| SF-2026-ARXIV-2607-04391 | arXiv:2607.04391v1 | paper-v1:2607.04391 | 2026-W28 | 2026-07-06 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-04391 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-04391 | no |
| SF-2026-ARXIV-2607-04395 | arXiv:2607.04395v1 | paper-v1:2607.04395 | 2026-W28 | 2026-07-06 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-04395 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-04395 | yes |
| SF-2026-ARXIV-2607-04517 | arXiv:2607.04517v1 | paper-v1:2607.04517 | 2026-W28 | 2026-07-06 | SRC-ARXIV | 1 | 1 | 0 | 2 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-04517 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-04171 | RP-6b8ef16b1176431b | closure | doi:10.48550/arxiv.2607.04171@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.04171@v1 | doi:10.48550/arxiv.2607.04171#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-04171 | complete |
| SF-2026-ARXIV-2607-04181 | RP-4526ccb507bc4310 | deep | arXiv:2607.04181v1 | SRC-ARXIV@arXiv:2607.04181v1 | https://arxiv.org/html/2607.04181v1#S3.SS1 through #S3.SS1.p4.1 :: feasible layer-replication configuration, request scatter/gather across consecutive layer segments and partitioned KV redistribution during configuration transition; https://arxiv.org/html/2607.04181v1#S3.SS2.p1.1 through #S3.SS2.p3.1 :: bidirectional chunked ring multicast for weights and fine-grained KV transfer overlapped with inter-token intervals; https://arxiv.org/html/2607.04181v1#S4.E1 through #S4.E10 and #S4.SS4 :: configuration search and migration cost model | https://arxiv.org/html/2607.04181v1#S4.SS1 and #S6.SS1 through #S6.SS3 :: Nano-vLLM-based prototype on four NVLink-connected H20 GPUs, Qwen3 8B/14B/32B, Alibaba/Azure trace replays and LongBench prompts; compares static vLLM and a threshold autoscaler using average/P99 latency and SLO attainment | https://arxiv.org/html/2607.04181v1#S4.SS2 and #S6.SS3 :: analytical ranking assumes homogeneous devices and divisible layer placements; no PCIe/Ethernet fabric, heterogeneous failure recovery, arbitrary graph, public artifact or production-fleet validation | Not Disclosed — v1 identifies a Nano-vLLM-based prototype but provides no CoCoScale repository, commit, tag or release | claim:SF-2026-ARXIV-2607-04181 | complete |
| SF-2026-ARXIV-2607-04292 | RP-e419adb5fed3d078 | closure | doi:10.48550/arxiv.2607.04292@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.04292@v1 | doi:10.48550/arxiv.2607.04292#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-04292 | complete |
| SF-2026-ARXIV-2607-04302 | RP-fe3ac22acabb985a | deep | arXiv:2607.04302v1 | SRC-ARXIV@arXiv:2607.04302v1 | https://arxiv.org/html/2607.04302v1#S4.SS1 through #S4.SS4 and #S4.E1 through #S4.E3 :: diagnose parameter-induced K-channel outliers after QK-RMSNorm, apply diagonal post-RoPE Q scaling with inverse K scaling, and gate static calibration; https://arxiv.org/html/2607.04302v1#S4.SS5 and #Thmtheorem1 :: reorder quantized P so numerator and denominator share the same tensor, fuse normalization into PV, and delimit the coherent-error result to fixed V | https://arxiv.org/html/2607.04302v1#S5, #S5.SS4 and #S6.T7 :: zero-shot option-likelihood and attention-error diagnostics across Qwen3-8B, Gemma2-9B, Llama3.1-8B, Mistral-7B and Phi-4B plus one Qwen3 long-context retrieval case; https://arxiv.org/html/2607.04302v1#A2.SS0.SSS0.Px1 through #A2.SS0.SSS0.Px7 :: scoring, prompt, dtype, calibration, hook, software/hardware and determinism settings | https://arxiv.org/html/2607.04302v1#S7.SS0.SSS0.Px3 and #Thmtheorem1 :: all latency numbers are theoretical instruction-scheduling estimates, target hardware was not available for direct validation, and the theorem holds V fixed; applicability also depends on the calibrated outlier regime, while gate thresholds are tested on five models only and the promised implementation artifact is absent | Not Disclosed — v1 promises the exact library, framework/toolkit and code in a future release; no public repository, commit or tag is identified | claim:SF-2026-ARXIV-2607-04302 | complete |
| SF-2026-ARXIV-2607-04391 | RP-25c2eb35c31cb479 | standard | arXiv:2607.04391v1 | SRC-ARXIV@arXiv:2607.04391v1 | https://arxiv.org/html/2607.04391v1#S3.SS1 through #S3.SS6 :: preserve immutable source evidence, build revisable relational metadata and semantic overlays, profile queries before deterministic SQL retrieval, and log retrieval/reformulation lifecycle | https://arxiv.org/html/2607.04391v1#S4 and #S4.SS4 :: experience report for one long-running single-user corpus; deployment statistics establish feasibility but no controlled retrieval comparison | https://arxiv.org/html/2607.04391v1#S4.SS4, #S5.SS5 and #S6 :: no multi-tenant isolation, poisoning test, multimodal completeness, comparative retrieval quality, reproducible benchmark or public artifact | Not Disclosed — v1 provides architecture and deployment statistics but no public repository, commit, release or reproducible benchmark artifact | claim:SF-2026-ARXIV-2607-04391 | complete |
| SF-2026-ARXIV-2607-04395 | RP-c50c7628c6b16c66 | standard | arXiv:2607.04395v1 | SRC-ARXIV@arXiv:2607.04395v1 | https://arxiv.org/html/2607.04395v1#S3.SS1 through #S3.SS4 :: model proposes NKI kernels, compiles with bounded timeout, executes random-input comparisons against a PyTorch reference and iterates for up to ten tool turns; SFT traces are compiler/execution filtered | https://arxiv.org/html/2607.04395v1#S4 and #S5.SS1 through #S5.SS2 :: NKIGen-Bench main/ablation evaluation on AWS Trainium; SFT and GRPO compared with named proprietary models; single runs without error bars and no kernel-runtime speed benchmark | https://arxiv.org/html/2607.04395v1#S6 and #S5.SS1 through #S5.SS2 :: SDK-specific, sparse binary reward can collapse group ranking signal, no public dataset/training trace/artifact, inference precision and runtime performance Not Disclosed | Not Disclosed — v1 cites official NKI samples but provides no public NKI-Agent repository, NKIGen-Bench snapshot, training trace, commit or release | claim:SF-2026-ARXIV-2607-04395 | complete |
| SF-2026-ARXIV-2607-04517 | RP-4f3075b920719184 | closure | doi:10.48550/arxiv.2607.04517@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.04517@v1 | doi:10.48550/arxiv.2607.04517#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-04517 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-04171:start -->
#### Teaching Tiny VLA Models Where to Look and How to Move

<!-- claim:SF-2026-ARXIV-2607-04171:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-04171:end -->

- Identity：`arXiv:2607.04171v1`；first-public（Asia/Shanghai）：`2026-07-05`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-04171:end -->

<!-- review:SF-2026-ARXIV-2607-04181:start -->
#### CoCoScale: Leveraging Layer-wise Scaling to Unlock the Potential of Online LLM Serving

<!-- claim:SF-2026-ARXIV-2607-04181:start -->A full model replica is not the only elastic unit. A controller can choose replication counts for consecutive Transformer layer segments; the scheduler scatters sub-batches across those replicas, gathers boundary activations and redistributes affected KV partitions during a configuration transition. This reduces whole-instance startup pressure on the evaluated topology but turns activation boundaries, KV ownership and transition coordination into correctness-critical scheduling state. The v1 manuscript does not define atomic configuration publication, route-version semantics or a state-transfer-plus-SLO commit protocol. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-04181:end -->

**旧方案与约束变化。** `Ch56 already evolves replica-level scaling toward stage and operator-DAG elasticity and requires profile, topology, state and failure-aware scheduling.`（`books/part-05-inference-system/56-inference-scheduling.md#L229`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A full model replica is not the only elastic unit. A controller can choose replication counts for consecutive Transformer layer segments; the scheduler scatters sub-batches across those replicas, gathers boundary activations and redistributes affected KV partitions during a configuration transition. This reduces whole-instance startup pressure on the evaluated topology but turns activation boundaries, KV ownership and transition coordination into correctness-critical scheduling state. The v1 manuscript does not define atomic configuration publication, route-version semantics or a state-transfer-plus-SLO commit protocol. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.04181v1#S3.SS1 through #S3.SS1.p4.1 :: feasible layer-replication configuration, request scatter/gather across consecutive layer segments and partitioned KV redistribution during configuration transition; https://arxiv.org/html/2607.04181v1#S3.SS2.p1.1 through #S3.SS2.p3.1 :: bidirectional chunked ring multicast for weights and fine-grained KV transfer overlapped with inter-token intervals; https://arxiv.org/html/2607.04181v1#S4.E1 through #S4.E10 and #S4.SS4 :: configuration search and migration cost model`；Evaluation：`https://arxiv.org/html/2607.04181v1#S4.SS1 and #S6.SS1 through #S6.SS3 :: Nano-vLLM-based prototype on four NVLink-connected H20 GPUs, Qwen3 8B/14B/32B, Alibaba/Azure trace replays and LongBench prompts; compares static vLLM and a threshold autoscaler using average/P99 latency and SLO attainment`；Limitations/Counterevidence：`https://arxiv.org/html/2607.04181v1#S4.SS2 and #S6.SS3 :: analytical ranking assumes homogeneous devices and divisible layer placements; no PCIe/Ethernet fabric, heterogeneous failure recovery, arbitrary graph, public artifact or production-fleet validation`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-04181:end -->

<!-- review:SF-2026-ARXIV-2607-04292:start -->
#### Agentic SABRE: An Uncertainty-Aware Neuro-Symbolic Multi-Agent Framework for Adaptive Ransomware Detection

<!-- claim:SF-2026-ARXIV-2607-04292:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-04292:end -->

- Identity：`arXiv:2607.04292v1`；first-public（Asia/Shanghai）：`2026-07-05`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-04292:end -->

<!-- review:SF-2026-ARXIV-2607-04302:start -->
#### HiFA4: Training-Free 4-bit FlashAttention on Ascend HIF4 NPUs for LLM Inference

<!-- claim:SF-2026-ARXIV-2607-04302:start -->Attention quantization should first diagnose asymmetric Q/K structure. When calibration confirms the K-outlier regime, a paired diagonal transform can scale Q and inversely scale K while preserving the unquantized attention score; a quantized-P reordering can then make the softmax numerator and denominator consume the same quantized tensor. The equality does not preserve the final quantized output, and the reordering removes one coherent error component rather than proving all Q/K/V error harmless. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-04302:end -->

**旧方案与约束变化。** `Ch49 already explains that lower bit width does not automatically accelerate attention and that distribution handling, calibration, fusion and runtime execution must be co-designed.`（`books/part-05-inference-system/49-tensorrt-llm.md#L263`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Attention quantization should first diagnose asymmetric Q/K structure. When calibration confirms the K-outlier regime, a paired diagonal transform can scale Q and inversely scale K while preserving the unquantized attention score; a quantized-P reordering can then make the softmax numerator and denominator consume the same quantized tensor. The equality does not preserve the final quantized output, and the reordering removes one coherent error component rather than proving all Q/K/V error harmless. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.04302v1#S4.SS1 through #S4.SS4 and #S4.E1 through #S4.E3 :: diagnose parameter-induced K-channel outliers after QK-RMSNorm, apply diagonal post-RoPE Q scaling with inverse K scaling, and gate static calibration; https://arxiv.org/html/2607.04302v1#S4.SS5 and #Thmtheorem1 :: reorder quantized P so numerator and denominator share the same tensor, fuse normalization into PV, and delimit the coherent-error result to fixed V`；Evaluation：`https://arxiv.org/html/2607.04302v1#S5, #S5.SS4 and #S6.T7 :: zero-shot option-likelihood and attention-error diagnostics across Qwen3-8B, Gemma2-9B, Llama3.1-8B, Mistral-7B and Phi-4B plus one Qwen3 long-context retrieval case; https://arxiv.org/html/2607.04302v1#A2.SS0.SSS0.Px1 through #A2.SS0.SSS0.Px7 :: scoring, prompt, dtype, calibration, hook, software/hardware and determinism settings`；Limitations/Counterevidence：`https://arxiv.org/html/2607.04302v1#S7.SS0.SSS0.Px3 and #Thmtheorem1 :: all latency numbers are theoretical instruction-scheduling estimates, target hardware was not available for direct validation, and the theorem holds V fixed; applicability also depends on the calibrated outlier regime, while gate thresholds are tested on five models only and the promised implementation artifact is absent`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-04302:end -->

<!-- review:SF-2026-ARXIV-2607-04391:start -->
#### Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture

<!-- claim:SF-2026-ARXIV-2607-04391:start -->The immutable source corpus remains evidence truth while relational metadata, semantic overlays and query profiles are revisable derived views. This is a concrete operational instance of the existing archive-versus-derived-memory contract, not a new canonical mechanism. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-04391:end -->

**旧方案与约束变化。** `Ch77 already separates compact control state from exact evidence archive and requires provenance, authorization, correction and auditability; Ch76 owns retrieval and Ch78 owns tool execution.`（`books/part-07-agent/77-memory.md#L1`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The immutable source corpus remains evidence truth while relational metadata, semantic overlays and query profiles are revisable derived views. This is a concrete operational instance of the existing archive-versus-derived-memory contract, not a new canonical mechanism. 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.04391v1#S3.SS1 through #S3.SS6 :: preserve immutable source evidence, build revisable relational metadata and semantic overlays, profile queries before deterministic SQL retrieval, and log retrieval/reformulation lifecycle`；Evaluation：`https://arxiv.org/html/2607.04391v1#S4 and #S4.SS4 :: experience report for one long-running single-user corpus; deployment statistics establish feasibility but no controlled retrieval comparison`；Limitations/Counterevidence：`https://arxiv.org/html/2607.04391v1#S4.SS4, #S5.SS5 and #S6 :: no multi-tenant isolation, poisoning test, multimodal completeness, comparative retrieval quality, reproducible benchmark or public artifact`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Principle Reuse`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-04391:end -->

<!-- review:SF-2026-ARXIV-2607-04395:start -->
#### NKI-Agent: Domain-Specific Fine-Tuning and Agentic Tool Use for Neuron Kernel Generation

<!-- claim:SF-2026-ARXIV-2607-04395:start -->An executable compiler and numerical reference can own kernel admission even when the model proposes candidates, but that binary verifier can be a weak group-relative learning signal when every candidate in a group fails together. This bounded accelerator case connects existing execution, RL and tool-authority principles without changing their canonical owners. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-04395:end -->

**旧方案与约束变化。** `Ch49 already treats learned kernel generation as candidate production while compiler/correctness checks own admission; Ch33 owns sparse group-relative reward failure and Ch78 owns typed execution authority.`（`books/part-05-inference-system/49-tensorrt-llm.md#L437-L458`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** An executable compiler and numerical reference can own kernel admission even when the model proposes candidates, but that binary verifier can be a weak group-relative learning signal when every candidate in a group fails together. This bounded accelerator case connects existing execution, RL and tool-authority principles without changing their canonical owners. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.04395v1#S3.SS1 through #S3.SS4 :: model proposes NKI kernels, compiles with bounded timeout, executes random-input comparisons against a PyTorch reference and iterates for up to ten tool turns; SFT traces are compiler/execution filtered`；Evaluation：`https://arxiv.org/html/2607.04395v1#S4 and #S5.SS1 through #S5.SS2 :: NKIGen-Bench main/ablation evaluation on AWS Trainium; SFT and GRPO compared with named proprietary models; single runs without error bars and no kernel-runtime speed benchmark`；Limitations/Counterevidence：`https://arxiv.org/html/2607.04395v1#S6 and #S5.SS1 through #S5.SS2 :: SDK-specific, sparse binary reward can collapse group ranking signal, no public dataset/training trace/artifact, inference precision and runtime performance Not Disclosed`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Principle Reuse`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-04395:end -->

<!-- review:SF-2026-ARXIV-2607-04517:start -->
#### VLA Grounder: Language-Conditioning Space Optimization for Black-Box VLA Models

<!-- claim:SF-2026-ARXIV-2607-04517:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-04517:end -->

- Identity：`arXiv:2607.04517v1`；first-public（Asia/Shanghai）：`2026-07-06`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-04517:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-04181 | Four concurrent model instances replaying 60-minute Alibaba and 130-minute Azure traces with LongBench prompts; separate Alpaca ablation | Qwen3-8B, Qwen3-14B, Qwen3-32B | 4 x NVIDIA H20 connected by NVLink | Not Disclosed | Trace-run distribution Not Disclosed; separate ablation uses 1,000 input tokens | Trace-run distribution Not Disclosed; separate ablation uses 64 output tokens | Dynamic sub-batches; exact sizes Not Disclosed | Four model instances; request concurrency Not Disclosed, and reported arrival rates are not concurrency counts | 30 s for the Alibaba replay and 27 s for the Azure replay | Nano-vLLM-based prototype compared with static vLLM and a threshold autoscaler; exact prototype commit Not Disclosed |
| SF-2026-ARXIV-2607-04302 | Zero-shot option-likelihood evaluation, attention-error diagnostics and one saturated long-context retrieval test | Qwen3-8B, Gemma2-9B, Llama3.1-8B, Mistral-7B, Phi-4B | Ascend HIF4 NPU is the target; public on-hardware timing is absent | HIF4 for QK^T/PV attention paths, BF16 elsewhere, FP16 online-softmax state | Benchmark-dependent; exact serving distribution Not Disclosed | Benchmark-dependent; exact serving distribution Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed; latency statements are theoretical instruction-scheduling estimates, not measured serving SLO | Official HIF4 QDQ reference comparing BF16, direct HIF4 and HiFA4; exact evaluator commit Not Disclosed |
| SF-2026-ARXIV-2607-04395 | NKIGen-Bench: 150 balanced held-out tasks for main evaluation and 60 for ablation | Qwen3-Coder-30B-A3B base/SFT/GRPO; Claude Sonnet 4 and Opus 4.8 comparisons | AWS Trainium Trn1 for kernel execution; SFT training uses 8 x A100 40GB | SFT BF16; evaluation inference precision Not Disclosed | Not Disclosed | Not Disclosed; up to 10 agent/tool turns | Evaluation per task; training batch 4 | Not Disclosed | Compiler timeout 120 s; no runtime-latency SLO and no kernel-speed benchmark | neuronx-cc compilation plus numerical allclose against a PyTorch reference at atol=rtol=1e-3; exact SDK/evaluator commit Not Disclosed |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-04181 | score_7_9;potential_books_delta | selected | DA-20260706-2607-04181 | — | V2=8/9；A full model replica is not the only elastic unit. A controller can choose replication counts for consecutive Transformer layer segments; the scheduler scatters sub-batches across those replicas, gathers boundary activations and redistributes affected KV partitions during a configuration transition. This reduces whole-instance startup pressure on the evaluated topology but turns activation boundaries, KV ownership and transition coordination into correctness-critical scheduling state. The v1 manuscript does not define atomic configuration publication, route-version semantics or a state-transfer-plus-SLO commit protocol.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260706-2607-04181 |
| SF-2026-ARXIV-2607-04302 | score_7_9;potential_books_delta | selected | DA-20260706-2607-04302 | — | V2=8/9；Attention quantization should first diagnose asymmetric Q/K structure. When calibration confirms the K-outlier regime, a paired diagonal transform can scale Q and inversely scale K while preserving the unquantized attention score; a quantized-P reordering can then make the softmax numerator and denominator consume the same quantized tensor. The equality does not preserve the final quantized output, and the reordering removes one coherent error component rather than proving all Q/K/V error harmless.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260706-2607-04302 |

<!-- analysis:DA-20260706-2607-04181:start -->
### CoCoScale: Leveraging Layer-wise Scaling to Unlock the Potential of Online LLM Serving

**旧方案为何合理。** Full-model replicas remain the simplest elasticity and failure-isolation unit when demand is steady, the fabric is slow, operational recovery dominates or the model cannot be divided cleanly.（现有命题定位：`books/part-05-inference-system/56-inference-scheduling.md#L229`）

**约束变化与机制。** A full model replica is not the only elastic unit. A controller can choose replication counts for consecutive Transformer layer segments; the scheduler scatters sub-batches across those replicas, gathers boundary activations and redistributes affected KV partitions during a configuration transition. This reduces whole-instance startup pressure on the evaluated topology but turns activation boundaries, KV ownership and transition coordination into correctness-critical scheduling state. The v1 manuscript does not define atomic configuration publication, route-version semantics or a state-transfer-plus-SLO commit protocol. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-SCHEDULING` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Layer-segment elasticity spends boundary communication, partitioned-KV migration and a larger partial-failure surface. A production implementation would additionally need configuration identity and safe transition acknowledgment, but those are project-inferred completion responsibilities rather than v1-proven protocol. The evidence is limited to four NVLink-connected H20 GPUs with homogeneous/divisibility assumptions; PCIe/Ethernet and production failure recovery remain unproved.

<!-- analysis:DA-20260706-2607-04181:end -->

<!-- analysis:DA-20260706-2607-04302:start -->
### HiFA4: Training-Free 4-bit FlashAttention on Ascend HIF4 NPUs for LLM Inference

**旧方案为何合理。** Symmetric Q/K quantization or a higher-precision fallback remains preferable when the calibrated K-outlier structure is absent, the gate is unstable, or a measured target-hardware path is unavailable.（现有命题定位：`books/part-05-inference-system/49-tensorrt-llm.md#L263`）

**约束变化与机制。** Attention quantization should first diagnose asymmetric Q/K structure. When calibration confirms the K-outlier regime, a paired diagonal transform can scale Q and inversely scale K while preserving the unquantized attention score; a quantized-P reordering can then make the softmax numerator and denominator consume the same quantized tensor. The equality does not preserve the final quantized output, and the reordering removes one coherent error component rather than proving all Q/K/V error harmless. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-TENSORRT-LLM` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** The route adds calibration artifacts, a gate, paired-transform correctness and backend-specific fusion. Current evidence is Experimental: five models, no public Ascend kernel timing, no implementation artifact and no production serving contract.

<!-- analysis:DA-20260706-2607-04302:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-04181 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L255 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2607-04181 | delta:SF-2026-ARXIV-2607-04181 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-04181 |
| SF-2026-ARXIV-2607-04302 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L441 | books/part-05-inference-system/48-speculative-decoding.md#L1 | existing:SF-2026-ARXIV-2607-04302 | delta:SF-2026-ARXIV-2607-04302 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-04302 |
| SF-2026-ARXIV-2607-04391 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2607-04391 | delta:SF-2026-ARXIV-2607-04391 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-04391 |
| SF-2026-ARXIV-2607-04395 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L437-L458 | books/part-04-training-system/33-grpo.md#L1 | existing:SF-2026-ARXIV-2607-04395 | delta:SF-2026-ARXIV-2607-04395 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-04395 |

<!-- books-review:SF-2026-ARXIV-2607-04181:start --><!-- existing:SF-2026-ARXIV-2607-04181:start -->对读 `books/part-05-inference-system/56-inference-scheduling.md#L255` 与相邻章节后，现有命题（`books/part-05-inference-system/56-inference-scheduling.md#L229`）为：Ch56 already evolves replica-level scaling toward stage and operator-DAG elasticity and requires profile, topology, state and failure-aware scheduling.<!-- existing:SF-2026-ARXIV-2607-04181:end --><!-- delta:SF-2026-ARXIV-2607-04181:start -->新增证据边界：A full model replica is not the only elastic unit. A controller can choose replication counts for consecutive Transformer layer segments; the scheduler scatters sub-batches across those replicas, gathers boundary activations and redistributes affected KV partitions during a configuration transition. This reduces whole-instance startup pressure on the evaluated topology but turns activation boundaries, KV ownership and transition coordination into correctness-critical scheduling state. The v1 manuscript does not define atomic configuration publication, route-version semantics or a state-transfer-plus-SLO commit protocol. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L255`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-04181:end --><!-- books-review:SF-2026-ARXIV-2607-04181:end -->

<!-- books-review:SF-2026-ARXIV-2607-04302:start --><!-- existing:SF-2026-ARXIV-2607-04302:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L441` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L263`）为：Ch49 already explains that lower bit width does not automatically accelerate attention and that distribution handling, calibration, fusion and runtime execution must be co-designed.<!-- existing:SF-2026-ARXIV-2607-04302:end --><!-- delta:SF-2026-ARXIV-2607-04302:start -->新增证据边界：Attention quantization should first diagnose asymmetric Q/K structure. When calibration confirms the K-outlier regime, a paired diagonal transform can scale Q and inversely scale K while preserving the unquantized attention score; a quantized-P reordering can then make the softmax numerator and denominator consume the same quantized tensor. The equality does not preserve the final quantized output, and the reordering removes one coherent error component rather than proving all Q/K/V error harmless. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L441`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-04302:end --><!-- books-review:SF-2026-ARXIV-2607-04302:end -->

<!-- books-review:SF-2026-ARXIV-2607-04391:start --><!-- existing:SF-2026-ARXIV-2607-04391:start -->对读 `books/part-07-agent/77-memory.md#L1` 与相邻章节后，现有命题（`books/part-07-agent/77-memory.md#L1`）为：Ch77 already separates compact control state from exact evidence archive and requires provenance, authorization, correction and auditability; Ch76 owns retrieval and Ch78 owns tool execution.<!-- existing:SF-2026-ARXIV-2607-04391:end --><!-- delta:SF-2026-ARXIV-2607-04391:start -->新增证据边界：The immutable source corpus remains evidence truth while relational metadata, semantic overlays and query profiles are revisable derived views. This is a concrete operational instance of the existing archive-versus-derived-memory contract, not a new canonical mechanism. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-04391:end --><!-- books-review:SF-2026-ARXIV-2607-04391:end -->

<!-- books-review:SF-2026-ARXIV-2607-04395:start --><!-- existing:SF-2026-ARXIV-2607-04395:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L437-L458` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L437-L458`）为：Ch49 already treats learned kernel generation as candidate production while compiler/correctness checks own admission; Ch33 owns sparse group-relative reward failure and Ch78 owns typed execution authority.<!-- existing:SF-2026-ARXIV-2607-04395:end --><!-- delta:SF-2026-ARXIV-2607-04395:start -->新增证据边界：An executable compiler and numerical reference can own kernel admission even when the model proposes candidates, but that binary verifier can be a weak group-relative learning signal when every candidate in a group fails together. This bounded accelerator case connects existing execution, RL and tool-authority principles without changing their canonical owners. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-04395:end --><!-- books-review:SF-2026-ARXIV-2607-04395:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260706-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260706; semantic-review:SA-20260706-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260706-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-04171; review:SF-2026-ARXIV-2607-04181; review:SF-2026-ARXIV-2607-04292; review:SF-2026-ARXIV-2607-04302; review:SF-2026-ARXIV-2607-04391; review:SF-2026-ARXIV-2607-04395; review:SF-2026-ARXIV-2607-04517; semantic-review:SA-20260706-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260706-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260706-2607-04181; analysis:DA-20260706-2607-04302; semantic-review:SA-20260706-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260706-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-04181; books-review:SF-2026-ARXIV-2607-04302; books-review:SF-2026-ARXIV-2607-04391; books-review:SF-2026-ARXIV-2607-04395; semantic-review:SA-20260706-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260706-COVERAGE:start -->Fresh-context review reconciled the exact window, partition totals, date bucket and denominator.<!-- semantic-review:SA-20260706-COVERAGE:end -->
<!-- semantic-review:SA-20260706-EVIDENCE:start -->Fresh-context review reconciled all 7 frozen families: 2 Deep, 2 Standard and 3 Closure; 0 pending and 0 blocked rows remain explicitly outside mechanism claims.<!-- semantic-review:SA-20260706-EVIDENCE:end -->
<!-- semantic-review:SA-20260706-SELECTION:start -->Fresh-context review reconciled 2 eligible Deep families: 2 selected and 0 not selected; the narrative limit does not downgrade any completed Source Review.<!-- semantic-review:SA-20260706-SELECTION:end -->
<!-- semantic-review:SA-20260706-BOOKS:start -->Fresh-context review checked current owner and adjacent chapter handoffs; 2 个 family 已定位到实际 Books 段落，2 个 family 的 No Change 结论可定位，0 个 Weekly Only disposition 已由逐 family Source Review 确认为不进入 Books。<!-- semantic-review:SA-20260706-BOOKS:end -->

## 8. Ignored Noise

537 个窗口内 identity 中，530 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：2 个 `Integrate`，2 个 `No Change — Existing Coverage`，0 个 `Weekly Only — Context`，3 个 `Rejected — Low Durability / Out of Scope`；Deep 2 / Standard 2。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/06/README.md`。
- 本日报长期 delta 已同步至：`books/part-05-inference-system/49-tensorrt-llm.md`、`books/part-05-inference-system/56-inference-scheduling.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [Teaching Tiny VLA Models Where to Look and How to Move](https://arxiv.org/abs/2607.04171v1) — first-public（Asia/Shanghai）：2026-07-05；accessed：2026-08-26
- [CoCoScale: Leveraging Layer-wise Scaling to Unlock the Potential of Online LLM Serving](https://arxiv.org/abs/2607.04181v1) — first-public（Asia/Shanghai）：2026-07-05；accessed：2026-08-27
- [Agentic SABRE: An Uncertainty-Aware Neuro-Symbolic Multi-Agent Framework for Adaptive Ransomware Detection](https://arxiv.org/abs/2607.04292v1) — first-public（Asia/Shanghai）：2026-07-05；accessed：2026-08-26
- [HiFA4: Training-Free 4-bit FlashAttention on Ascend HIF4 NPUs for LLM Inference](https://arxiv.org/abs/2607.04302v1) — first-public（Asia/Shanghai）：2026-07-05；accessed：2026-08-27
- [Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture](https://arxiv.org/abs/2607.04391v1) — first-public（Asia/Shanghai）：2026-07-06；accessed：2026-08-27
- [NKI-Agent: Domain-Specific Fine-Tuning and Agentic Tool Use for Neuron Kernel Generation](https://arxiv.org/abs/2607.04395v1) — first-public（Asia/Shanghai）：2026-07-06；accessed：2026-08-27
- [VLA Grounder: Language-Conditioning Space Optimization for Black-Box VLA Models](https://arxiv.org/abs/2607.04517v1) — first-public（Asia/Shanghai）：2026-07-06；accessed：2026-08-26
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
