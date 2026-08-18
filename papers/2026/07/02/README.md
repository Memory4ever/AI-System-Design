# Daily Research — 2026-07-02

**Research Date:** 2026-07-02

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-01 09:00:00 ～ 2026-07-02 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 1285 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 19 个。当前路由账目为 7 个 Deep、2 个 Standard、10 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-02 |
| Window End | 2026-07-02 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-02-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-26T18:00:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-01T09:00:00+08:00 | 2026-07-02T09:00:00+08:00 | 2026-08-26T18:00:00+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 1285 | SF-2026-ARXIV-2607-00351<br>SF-2026-ARXIV-2607-00466<br>SF-2026-ARXIV-2607-00482<br>SF-2026-ARXIV-2607-00501<br>SF-2026-ARXIV-2607-00666<br>SF-2026-ARXIV-2607-00760<br>SF-2026-ARXIV-2607-00908<br>SF-2026-ARXIV-2607-02604<br>SF-2026-ARXIV-2607-01299<br>SF-2026-ARXIV-2607-00972<br>SF-2026-ARXIV-2607-01065<br>SF-2026-ARXIV-2607-01071<br>SF-2026-ARXIV-2607-01104<br>SF-2026-ARXIV-2607-01211<br>SF-2026-ARXIV-2607-01212<br>SF-2026-ARXIV-2607-01224<br>SF-2026-ARXIV-2607-01378<br>SF-2026-ARXIV-2607-01425<br>SF-2026-ARXIV-2607-01520 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-02T09:00:00+08:00 | coverage:SRC-ARXIV:20260702 | GAP-ARXIV-DIRECT-RESET-20260702 |

<!-- coverage:SRC-ARXIV:20260702:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 1285 unique identities in this strict window; 19 routed families.<!-- coverage:SRC-ARXIV:20260702:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 19 个 family：exact v1 为 5 个 family 披露 artifact/evidence locator，其中 3 个提供外部 repository/project/demo locator，另有 14 个未披露；本日确认 0 个 family、0 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-00351 | arXiv:2607.00351v1 | paper-v1:2607.00351 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-00351 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-00466 | arXiv:2607.00466v1 | paper-v1:2607.00466 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-00466 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2607-00466 | no |
| SF-2026-ARXIV-2607-00482 | arXiv:2607.00482v1 | paper-v1:2607.00482 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-00482 | self | — | new_in_window | TRAIN-GRPO | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-00501 | arXiv:2607.00501v1 | paper-v1:2607.00501 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-00501 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-00501 | no |
| SF-2026-ARXIV-2607-00666 | arXiv:2607.00666v1 | paper-v1:2607.00666 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-00666 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-00760 | arXiv:2607.00760v1 | paper-v1:2607.00760 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-00760 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2607-00760 | no |
| SF-2026-ARXIV-2607-00908 | arXiv:2607.00908v1 | paper-v1:2607.00908 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-00908 | self | — | new_in_window | INFER-TENSORRT-LLM | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02604 | arXiv:2607.02604v1 | paper-v1:2607.02604 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02604 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-01299 | arXiv:2607.01299v1 | paper-v1:2607.01299 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-01299 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2607-01299 | no |
| SF-2026-ARXIV-2607-00972 | arXiv:2607.00972v1 | paper-v1:2607.00972 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-00972 | self | — | new_in_window | AGENT-RAG | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-01065 | arXiv:2607.01065v1 | paper-v1:2607.01065 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-01065 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-01065 | no |
| SF-2026-ARXIV-2607-01071 | arXiv:2607.01071v1 | paper-v1:2607.01071 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-01071 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-01071 | no |
| SF-2026-ARXIV-2607-01104 | arXiv:2607.01104v1 | paper-v1:2607.01104 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-01104 | self | — | new_in_window | TRAIN-PRETRAINING | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-01211 | arXiv:2607.01211v1 | paper-v1:2607.01211 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-01211 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-01211 | no |
| SF-2026-ARXIV-2607-01212 | arXiv:2607.01212v1 | paper-v1:2607.01212 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-01212 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-01224 | arXiv:2607.01224v1 | paper-v1:2607.01224 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-01224 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-01224 | no |
| SF-2026-ARXIV-2607-01378 | arXiv:2607.01378v1 | paper-v1:2607.01378 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-01378 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-01425 | arXiv:2607.01425v1 | paper-v1:2607.01425 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-01425 | self | — | new_in_window | AGENT-MULTI-AGENT | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-01520 | arXiv:2607.01520v1 | paper-v1:2607.01520 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-01520 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2607-01520 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-00351 | RP-9eebeac8313d8a45 | closure | doi:10.48550/arxiv.2607.00351@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.00351@v1 | doi:10.48550/arxiv.2607.00351#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-00351 | complete |
| SF-2026-ARXIV-2607-00466 | RP-3e1ea6fbdf689737 | deep | arXiv:2607.00466v1 | SRC-ARXIV@arXiv:2607.00466v1 | https://arxiv.org/html/2607.00466v1#S4 :: block-lifecycle-bound expert signatures, balanced offline clustering and locality-band online routing; https://arxiv.org/html/2607.00466v1#S5 :: vLLM proxy/hook/artifact implementation | https://arxiv.org/html/2607.00466v1#S6 :: author evaluation binds four MoE models, task/language workloads, 5 nodes with 40 AMD MI300X GPUs, 400 Gbps NDR, vLLM 0.21.0rc1, ROCm 7.2 and several P/D topologies | https://arxiv.org/html/2607.00466v1#S3.SS5 :: signature design, load/locality conflict and prefix-cache coherence are explicit challenges; the paper has no separate limitations section, so cross-model/workload drift, reclustering and worker churn remain evidence boundaries | https://arxiv.org/html/2607.00466v1#S5 :: implementation is described as about 2,000 lines on vLLM; no author event-time repository/commit is disclosed, so code-level claims stop at the manuscript | claim:SF-2026-ARXIV-2607-00466 | complete |
| SF-2026-ARXIV-2607-00482 | RP-b88d1c5b6255b1b1 | closure | doi:10.48550/arxiv.2607.00482@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.00482@v1 | doi:10.48550/arxiv.2607.00482#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-00482 | complete |
| SF-2026-ARXIV-2607-00501 | RP-e260ba3ba6ab0e12 | standard | arXiv:2607.00501v1 | SRC-ARXIV@arXiv:2607.00501v1 | https://arxiv.org/html/2607.00501v1#S3 :: native Metal runtime with descriptor-driven architectures, zero-allocation decode, fused specialized kernels and bounded chunked prefill | https://arxiv.org/html/2607.00501v1#S4 :: author measurements cover Qwen3, Llama 3.2 and Gemma 4 at Q4/Q8 on specified M3/M4 Pro devices against llama.cpp, MLX and uzu; no result is generalized beyond that hardware/software contract | https://arxiv.org/html/2607.00501v1#S5.SS1 :: Metal-only, single-device execution, no continuous batching or multi-request scheduling, and no tensor-parallel/distributed execution | https://github.com/basecompute/baseRT :: author repository linked by v1; event-time commit was not established and is not used for a version-specific claim | claim:SF-2026-ARXIV-2607-00501 | complete |
| SF-2026-ARXIV-2607-00666 | RP-91d47692d506a889 | closure | doi:10.48550/arxiv.2607.00666@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.00666@v1 | doi:10.48550/arxiv.2607.00666#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-00666 | complete |
| SF-2026-ARXIV-2607-00760 | RP-3f33fab07265026a | deep | arXiv:2607.00760v1 | SRC-ARXIV@arXiv:2607.00760v1 | https://arxiv.org/html/2607.00760v1#S4 :: dynamic token- and feature-dimension compression; https://arxiv.org/html/2607.00760v1#S5 :: packed layout, encode path, PackedAttention, double buffering and incremental strategy generation | https://arxiv.org/html/2607.00760v1#S6 :: author accuracy, microbenchmark and end-to-end serving evaluation; retained conclusions do not export headline speedups or quality numbers | https://arxiv.org/html/2607.00760v1#S7 :: evaluation is Decode-focused, compressed Prefill remains future work, and PackedAttention still uses CUDA cores rather than a broader optimized kernel path | Not Disclosed — no author event-time repository or exact implementation commit is linked by arXiv v1 | claim:SF-2026-ARXIV-2607-00760 | complete |
| SF-2026-ARXIV-2607-00908 | RP-c193e7d026514667 | closure | doi:10.48550/arxiv.2607.00908@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.00908@v1 | doi:10.48550/arxiv.2607.00908#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-00908 | complete |
| SF-2026-ARXIV-2607-02604 | RP-d0bd3c3e0a1687df | closure | doi:10.48550/arxiv.2607.02604@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02604@v1 | doi:10.48550/arxiv.2607.02604#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02604 | complete |
| SF-2026-ARXIV-2607-01299 | RP-d668a7c429958e3c | deep | arXiv:2607.01299v1 | SRC-ARXIV@arXiv:2607.01299v1 | https://arxiv.org/html/2607.01299v1#S4 :: cached segment transition composition for recurrent linear-attention state, seam-window repair for full-attention layers and segment-parallel cold prefill; https://arxiv.org/html/2607.01299v1#S5 :: SGLang/FLA implementation path | https://arxiv.org/html/2607.01299v1#S6 :: author evaluation binds Qwen3.5-35B-A3B, one H20 node, disclosed datasets, prefix patterns and baselines; no production arrival/concurrency or independent replication is claimed | https://arxiv.org/html/2607.01299v1#S3 :: ordinary KV splice cannot compose recurrent state, hidden-state suppression blocks old repair primitives, and seam approximation remains architecture/segment dependent; no separate limitations section is present | Not Disclosed — FLA and NCCL are dependencies, but v1 does not link an author event-time HYPIC repository/commit | claim:SF-2026-ARXIV-2607-01299 | complete |
| SF-2026-ARXIV-2607-00972 | RP-93d242fa6eaf0ed1 | closure | doi:10.48550/arxiv.2607.00972@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.00972@v1 | doi:10.48550/arxiv.2607.00972#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-00972 | complete |
| SF-2026-ARXIV-2607-01065 | RP-b47fcb6726d67465 | standard | arXiv:2607.01065v1 | SRC-ARXIV@arXiv:2607.01065v1 | https://arxiv.org/html/2607.01065v1#S5 :: gain-shape decomposition, assignment and centroid updates plus gradient-weighted variant | https://arxiv.org/html/2607.01065v1#S6 :: author evaluation covers synthetic vectors, several open models/datasets, perplexity, downstream tasks, ablations and a decoding-latency appendix; production concurrency and tail SLO are not disclosed | https://arxiv.org/html/2607.01065v1#S5.SS2 :: alternating updates optimize a practical surrogate and do not guarantee monotonic decrease of the original reconstruction objective; no separate limitations section is present | Not Disclosed — no author event-time public implementation is linked by arXiv v1 | claim:SF-2026-ARXIV-2607-01065 | complete |
| SF-2026-ARXIV-2607-01071 | RP-057264e3d7da282b | deep | arXiv:2607.01071v1 | SRC-ARXIV@arXiv:2607.01071v1 | https://arxiv.org/html/2607.01071v1#S3 :: five memory-decision relations, benchmark construction and role-aware rubrics; https://arxiv.org/html/2607.01071v1#A2 :: schema, dialogue and validation pipeline | https://arxiv.org/html/2607.01071v1#S4 :: generation, retrieval-versus-use attribution and scenario diagnostics across selected memory systems/backbones; the reported post-retrieval proportions are benchmark-bound | https://arxiv.org/html/2607.01071v1#A6 :: implementation coverage is incomplete for all listed memory frameworks; synthetic scenarios, LLM judging and backbone choice constrain external validity | https://github.com/XMUDeepLIT/MemSyco-Bench :: author repository linked by v1; exact event-time commit was not established | claim:SF-2026-ARXIV-2607-01071 | complete |
| SF-2026-ARXIV-2607-01104 | RP-b9bbf3fe9edf1d9b | closure | doi:10.48550/arxiv.2607.01104@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.01104@v1 | doi:10.48550/arxiv.2607.01104#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-01104 | complete |
| SF-2026-ARXIV-2607-01211 | RP-8ce9deaf3d391703 | deep | arXiv:2607.01211v1 | SRC-ARXIV@arXiv:2607.01211v1 | https://arxiv.org/html/2607.01211v1#S3 :: rebuild/replay of reference patches across machines and rounds; https://arxiv.org/html/2607.01211v1#S4 :: score-formula and low-speedup-tail sensitivity analysis | https://arxiv.org/html/2607.01211v1#S3.SS1 :: 740 reference patches across four cloud providers and 12 machine-round combinations, followed by task/ranking analysis; retained claim is reference validity and score sensitivity, not a new agent ranking | https://arxiv.org/html/2607.01211v1#S7 :: selected benchmarks, released artifacts, implementation choices and hardware variation limit generalization | Not Disclosed — the v1 manuscript describes released benchmark artifacts but does not provide an event-time author repository identifier used here | claim:SF-2026-ARXIV-2607-01211 | complete |
| SF-2026-ARXIV-2607-01212 | RP-0c224366c19d40c7 | closure | doi:10.48550/arxiv.2607.01212@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.01212@v1 | doi:10.48550/arxiv.2607.01212#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-01212 | complete |
| SF-2026-ARXIV-2607-01224 | RP-2e4865c93342c2ab | deep | arXiv:2607.01224v1 | SRC-ARXIV@arXiv:2607.01224v1 | https://arxiv.org/html/2607.01224v1#S2 :: file-system memory, scaffold-revision loop and separately trained memory specialist; https://arxiv.org/html/2607.01224v1#A1 :: fixed-seed promotion and training implementation | https://arxiv.org/html/2607.01224v1#S3 :: author evaluation covers three procedurally generated long-horizon games using Qwen2.5-32B-Instruct and specified baselines; leaderboard comparison is not treated as model equivalence | https://arxiv.org/html/2607.01224v1#S6 :: episodic memory resets between runs, evaluation is limited to games, and each environment uses a separate scaffold/specialist | https://github.com/autoLearnMem/AutoMem :: author code linked by v1; event-time commit was not established | claim:SF-2026-ARXIV-2607-01224 | complete |
| SF-2026-ARXIV-2607-01378 | RP-3129fd51266d2691 | closure | doi:10.48550/arxiv.2607.01378@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.01378@v1 | doi:10.48550/arxiv.2607.01378#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-01378 | complete |
| SF-2026-ARXIV-2607-01425 | RP-98460178a40115d4 | closure | doi:10.48550/arxiv.2607.01425@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.01425@v1 | doi:10.48550/arxiv.2607.01425#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-01425 | complete |
| SF-2026-ARXIV-2607-01520 | RP-c78710aafe18a50e | deep | arXiv:2607.01520v1 | SRC-ARXIV@arXiv:2607.01520v1 | https://arxiv.org/html/2607.01520v1#S3 :: KV compression as sparse approximation of a context measure and response-covariance compressibility; https://arxiv.org/html/2607.01520v1#S4 :: query-aware/agnostic minimax upper and lower bounds; https://arxiv.org/html/2607.01520v1#S5 :: causal merge-reduce algorithms | https://arxiv.org/html/2607.01520v1#S6 and https://arxiv.org/html/2607.01520v1#A4 :: focused LongBench-v2 experiments on Qwen3-32B, single NVIDIA H100, stated budgets/baselines and one fixed seed for randomized methods | https://arxiv.org/html/2607.01520v1#S4.SS3 :: spectral lower bounds show lookup-like contexts can require nearly full support; practical experiments are targeted, single-GPU/single-seed and do not establish semantic quality or production SLO generally | https://arxiv.org/html/2607.01520v1#A4 :: reproduction instructions are said to accompany supplementary material, but no stable public repository/commit is disclosed in v1 | claim:SF-2026-ARXIV-2607-01520 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-00351:start -->
#### Unleashing More Actions via Action Compositional Training for VLA Models

<!-- claim:SF-2026-ARXIV-2607-00351:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-00351:end -->

- Identity：`arXiv:2607.00351v1`；first-public（Asia/Shanghai）：`2026-07-01`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-00351:end -->

<!-- review:SF-2026-ARXIV-2607-00466:start -->
#### ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving

<!-- claim:SF-2026-ARXIV-2607-00466:start -->MoE Decode 的成本不仅由 queue length 决定，还由 batch 激活的 distinct expert working set 决定。把 prefill expert signature 与 KV block 生命周期绑定，再在 locality band 内做 load-aware routing，可以复用 expert weights；代价是 calibration/reclustering、signature metadata、load-locality conflict 和 prefix/worker epoch consistency。Dense 或 expert locality 弱时，普通 least-load routing 仍更合理。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-00466:end -->

**旧方案与约束变化。** `本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**`（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** MoE Decode 的成本不仅由 queue length 决定，还由 batch 激活的 distinct expert working set 决定。把 prefill expert signature 与 KV block 生命周期绑定，再在 locality band 内做 load-aware routing，可以复用 expert weights；代价是 calibration/reclustering、signature metadata、load-locality conflict 和 prefix/worker epoch consistency。Dense 或 expert locality 弱时，普通 least-load routing 仍更合理。 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.00466v1#S4 :: block-lifecycle-bound expert signatures, balanced offline clustering and locality-band online routing; https://arxiv.org/html/2607.00466v1#S5 :: vLLM proxy/hook/artifact implementation`；Evaluation：`https://arxiv.org/html/2607.00466v1#S6 :: author evaluation binds four MoE models, task/language workloads, 5 nodes with 40 AMD MI300X GPUs, 400 Gbps NDR, vLLM 0.21.0rc1, ROCm 7.2 and several P/D topologies`；Limitations/Counterevidence：`https://arxiv.org/html/2607.00466v1#S3.SS5 :: signature design, load/locality conflict and prefix-cache coherence are explicit challenges; the paper has no separate limitations section, so cross-model/workload drift, reclustering and worker churn remain evidence boundaries`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L518-L539`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-00466:end -->

<!-- review:SF-2026-ARXIV-2607-00482:start -->
#### Know When to Stop: Segment-Level Credit Assignment for Reducing Overthinking

<!-- claim:SF-2026-ARXIV-2607-00482:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-00482:end -->

- Identity：`arXiv:2607.00482v1`；first-public（Asia/Shanghai）：`2026-07-01`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-00482:end -->

<!-- review:SF-2026-ARXIV-2607-00501:start -->
#### BaseRT: Best-in-Class LLM Inference on Apple Silicon via Native Metal

<!-- claim:SF-2026-ARXIV-2607-00501:start -->A hardware-native engine can remove generic framework allocation, graph and dispatch overhead through preallocated buffers, descriptor-driven architecture differences and chip-specialized fusion. The gain trades portability and scheduling breadth for a narrower hardware contract; the chapter already owns this specialization-versus-portability branch and its benchmark boundary. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-00501:end -->

**旧方案与约束变化。** `A hardware-specialized execution path can fuse layout, precision, kernel and scheduling for a narrow workload, while the general library path retains broader coverage, portability and maintenance stability.`（`books/part-05-inference-system/49-tensorrt-llm.md#L146-L157`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A hardware-native engine can remove generic framework allocation, graph and dispatch overhead through preallocated buffers, descriptor-driven architecture differences and chip-specialized fusion. The gain trades portability and scheduling breadth for a narrower hardware contract; the chapter already owns this specialization-versus-portability branch and its benchmark boundary. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.00501v1#S3 :: native Metal runtime with descriptor-driven architectures, zero-allocation decode, fused specialized kernels and bounded chunked prefill`；Evaluation：`https://arxiv.org/html/2607.00501v1#S4 :: author measurements cover Qwen3, Llama 3.2 and Gemma 4 at Q4/Q8 on specified M3/M4 Pro devices against llama.cpp, MLX and uzu; no result is generalized beyond that hardware/software contract`；Limitations/Counterevidence：`https://arxiv.org/html/2607.00501v1#S5.SS1 :: Metal-only, single-device execution, no continuous batching or multi-request scheduling, and no tensor-parallel/distributed execution`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-00501:end -->

<!-- review:SF-2026-ARXIV-2607-00666:start -->
#### Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts

<!-- claim:SF-2026-ARXIV-2607-00666:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-00666:end -->

- Identity：`arXiv:2607.00666v1`；first-public（Asia/Shanghai）：`2026-07-01`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-00666:end -->

<!-- review:SF-2026-ARXIV-2607-00760:start -->
#### MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression

<!-- claim:SF-2026-ARXIV-2607-00760:start -->KV compression can jointly vary retained token count and per-token feature rank instead of treating eviction and quantization as isolated policies. This enlarges the quality-capacity search space but requires a packed physical layout, fused consumer kernel, background encoding, strategy versioning and fragmentation control; a logical compression ratio without these paths is not a serving gain. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-00760:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** KV compression can jointly vary retained token count and per-token feature rank instead of treating eviction and quantization as isolated policies. This enlarges the quality-capacity search space but requires a packed physical layout, fused consumer kernel, background encoding, strategy versioning and fragmentation control; a logical compression ratio without these paths is not a serving gain. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.00760v1#S4 :: dynamic token- and feature-dimension compression; https://arxiv.org/html/2607.00760v1#S5 :: packed layout, encode path, PackedAttention, double buffering and incremental strategy generation`；Evaluation：`https://arxiv.org/html/2607.00760v1#S6 :: author accuracy, microbenchmark and end-to-end serving evaluation; retained conclusions do not export headline speedups or quality numbers`；Limitations/Counterevidence：`https://arxiv.org/html/2607.00760v1#S7 :: evaluation is Decode-focused, compressed Prefill remains future work, and PackedAttention still uses CUDA cores rather than a broader optimized kernel path`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-00760:end -->

<!-- review:SF-2026-ARXIV-2607-00908:start -->
#### Beyond Activation Alignment:The Alignment-Diversity Tradeoff in Task-Aware LLM Quantization

<!-- claim:SF-2026-ARXIV-2607-00908:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-00908:end -->

- Identity：`arXiv:2607.00908v1`；first-public（Asia/Shanghai）：`2026-07-01`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-00908:end -->

<!-- review:SF-2026-ARXIV-2607-02604:start -->
#### DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation

<!-- claim:SF-2026-ARXIV-2607-02604:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02604:end -->

- Identity：`arXiv:2607.02604v1`；first-public（Asia/Shanghai）：`2026-07-01`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02604:end -->

<!-- review:SF-2026-ARXIV-2607-01299:start -->
#### HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching

<!-- claim:SF-2026-ARXIV-2607-01299:start -->For hybrid attention, reusable state is not always a list of per-token KV. A linear-attention segment may need both zero-state result and cumulative transition operator so segments compose in order; sparse full-attention layers then need bounded seam repair. This enables position-independent reuse but adds operator identity, numerical drift, seam policy, composition order and fallback semantics. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01299:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** For hybrid attention, reusable state is not always a list of per-token KV. A linear-attention segment may need both zero-state result and cumulative transition operator so segments compose in order; sparse full-attention layers then need bounded seam repair. This enables position-independent reuse but adds operator identity, numerical drift, seam policy, composition order and fallback semantics. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01299v1#S4 :: cached segment transition composition for recurrent linear-attention state, seam-window repair for full-attention layers and segment-parallel cold prefill; https://arxiv.org/html/2607.01299v1#S5 :: SGLang/FLA implementation path`；Evaluation：`https://arxiv.org/html/2607.01299v1#S6 :: author evaluation binds Qwen3.5-35B-A3B, one H20 node, disclosed datasets, prefix patterns and baselines; no production arrival/concurrency or independent replication is claimed`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01299v1#S3 :: ordinary KV splice cannot compose recurrent state, hidden-state suppression blocks old repair primitives, and seam approximation remains architecture/segment dependent; no separate limitations section is present`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-01299:end -->

<!-- review:SF-2026-ARXIV-2607-00972:start -->
#### Bayesian Uncertainty Propagation for Agentic RAG Pipelines: A Proof-of-Concept Study on Multi-Hop Question Answering

<!-- claim:SF-2026-ARXIV-2607-00972:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-00972:end -->

- Identity：`arXiv:2607.00972v1`；first-public（Asia/Shanghai）：`2026-07-01`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-00972:end -->

<!-- review:SF-2026-ARXIV-2607-01065:start -->
#### GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache

<!-- claim:SF-2026-ARXIV-2607-01065:start -->At extreme vector-quantization budgets, separately modeling vector direction and scale can preserve information that ordinary Euclidean centroids conflate. This is a quantizer-design branch, not proof of system speed: codebook lookup, metadata, kernel support and autoregressive error still determine whether sub-bit storage improves serving. Existing attention-distortion and effective-bit accounting already cover the lasting conclusion. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01065:end -->

**旧方案与约束变化。** `KV quantization must be evaluated at the attention consumer and over autoregressive feedback, with physical metadata, kernel and effective-bit costs included rather than inferred from tensor reconstruction alone.`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L452-L482`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** At extreme vector-quantization budgets, separately modeling vector direction and scale can preserve information that ordinary Euclidean centroids conflate. This is a quantizer-design branch, not proof of system speed: codebook lookup, metadata, kernel support and autoregressive error still determine whether sub-bit storage improves serving. Existing attention-distortion and effective-bit accounting already cover the lasting conclusion. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01065v1#S5 :: gain-shape decomposition, assignment and centroid updates plus gradient-weighted variant`；Evaluation：`https://arxiv.org/html/2607.01065v1#S6 :: author evaluation covers synthetic vectors, several open models/datasets, perplexity, downstream tasks, ablations and a decoding-latency appendix; production concurrency and tail SLO are not disclosed`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01065v1#S5.SS2 :: alternating updates optimize a practical surrogate and do not guarantee monotonic decrease of the original reconstruction objective; no separate limitations section is present`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-01065:end -->

<!-- review:SF-2026-ARXIV-2607-01071:start -->
#### MemSyco-Bench: Benchmarking Sycophancy in Agent Memory

<!-- claim:SF-2026-ARXIV-2607-01071:start -->Memory quality must separate retrieval success from downstream adoption: a relevant memory can be retrieved yet should be ignored, constrained, superseded or used only for personalization. The existing chapter already gives fact/retrieval-policy separation, authority, contradiction and post-retrieval risk gates, so this source strengthens evidence without changing the mechanism owner. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01071:end -->

**旧方案与约束变化。** `Memory retrieval is not fact adjudication: read policy must distinguish authority, valid time, contradiction, supersession and explicit unknown-current state before deciding whether to use or abstain.`（`books/part-07-agent/77-memory.md#L628-L658`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Memory quality must separate retrieval success from downstream adoption: a relevant memory can be retrieved yet should be ignored, constrained, superseded or used only for personalization. The existing chapter already gives fact/retrieval-policy separation, authority, contradiction and post-retrieval risk gates, so this source strengthens evidence without changing the mechanism owner. 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01071v1#S3 :: five memory-decision relations, benchmark construction and role-aware rubrics; https://arxiv.org/html/2607.01071v1#A2 :: schema, dialogue and validation pipeline`；Evaluation：`https://arxiv.org/html/2607.01071v1#S4 :: generation, retrieval-versus-use attribution and scenario diagnostics across selected memory systems/backbones; the reported post-retrieval proportions are benchmark-bound`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01071v1#A6 :: implementation coverage is incomplete for all listed memory frameworks; synthetic scenarios, LLM judging and backbone choice constrain external validity`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L716-L731`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-01071:end -->

<!-- review:SF-2026-ARXIV-2607-01104:start -->
#### CausalMix: Data Mixture as Causal Inference for Language Model Training

<!-- claim:SF-2026-ARXIV-2607-01104:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-01104:end -->

- Identity：`arXiv:2607.01104v1`；first-public（Asia/Shanghai）：`2026-07-01`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-01104:end -->

<!-- review:SF-2026-ARXIV-2607-01211:start -->
#### Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?

<!-- claim:SF-2026-ARXIV-2607-01211:start -->Executable evaluation must validate the reference artifact before judging candidates and must expose sensitivity to machine, repetition and aggregation rules. The evaluation chapter already contains this exact reference-first admission chain and its representativeness boundary. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01211:end -->

**旧方案与约束变化。** `Benchmark admission first rebuilds and replays the immutable reference artifact across machine and round, then measures infrastructure and scorer variance before candidates are compared.`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L729-L747`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Executable evaluation must validate the reference artifact before judging candidates and must expose sensitivity to machine, repetition and aggregation rules. The evaluation chapter already contains this exact reference-first admission chain and its representativeness boundary. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01211v1#S3 :: rebuild/replay of reference patches across machines and rounds; https://arxiv.org/html/2607.01211v1#S4 :: score-formula and low-speedup-tail sensitivity analysis`；Evaluation：`https://arxiv.org/html/2607.01211v1#S3.SS1 :: 740 reference patches across four cloud providers and 12 machine-round combinations, followed by task/ranking analysis; retained claim is reference validity and score sensitivity, not a new agent ranking`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01211v1#S7 :: selected benchmarks, released artifacts, implementation choices and hardware variation limit generalization`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L860-L874`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 3 / Durability 3 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-01211:end -->

<!-- review:SF-2026-ARXIV-2607-01212:start -->
#### FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action Model

<!-- claim:SF-2026-ARXIV-2607-01212:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-01212:end -->

- Identity：`arXiv:2607.01212v1`；first-public（Asia/Shanghai）：`2026-07-02`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-01212:end -->

<!-- review:SF-2026-ARXIV-2607-01224:start -->
#### AutoMem: Automated Learning of Memory as a Cognitive Skill

<!-- claim:SF-2026-ARXIV-2607-01224:start -->Memory policy can be optimized as a versioned artifact through a held-out promotion loop, while memory-operation proficiency can be trained separately from task-action authority. The existing Memory chapter already separates derived policy, validation, promotion/rollback and Workflow ownership, so the source is corroborating rather than a new owner mechanism. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01224:end -->

**旧方案与约束变化。** `A learned Memory policy is a derived, versioned procedural asset whose applicability, source episodes and validation results must pass held-out promotion and retain provenance and rollback.`（`books/part-07-agent/77-memory.md#L343-L433`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Memory policy can be optimized as a versioned artifact through a held-out promotion loop, while memory-operation proficiency can be trained separately from task-action authority. The existing Memory chapter already separates derived policy, validation, promotion/rollback and Workflow ownership, so the source is corroborating rather than a new owner mechanism. 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01224v1#S2 :: file-system memory, scaffold-revision loop and separately trained memory specialist; https://arxiv.org/html/2607.01224v1#A1 :: fixed-seed promotion and training implementation`；Evaluation：`https://arxiv.org/html/2607.01224v1#S3 :: author evaluation covers three procedurally generated long-horizon games using Qwen2.5-32B-Instruct and specified baselines; leaderboard comparison is not treated as model equivalence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01224v1#S6 :: episodic memory resets between runs, evaluation is limited to games, and each environment uses a separate scaffold/specialist`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L806-L819`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-01224:end -->

<!-- review:SF-2026-ARXIV-2607-01378:start -->
#### Neuro-Symbolic Safety Guidance for Vision-Language-Action Models via Constrained Flow Matching

<!-- claim:SF-2026-ARXIV-2607-01378:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-01378:end -->

- Identity：`arXiv:2607.01378v1`；first-public（Asia/Shanghai）：`2026-07-02`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-01378:end -->

<!-- review:SF-2026-ARXIV-2607-01425:start -->
#### Agent4cs: A Multi-agent System for Code Summarization in Large Hierarchical Codebases

<!-- claim:SF-2026-ARXIV-2607-01425:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-01425:end -->

- Identity：`arXiv:2607.01425v1`；first-public（Asia/Shanghai）：`2026-07-02`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-01425:end -->

<!-- review:SF-2026-ARXIV-2607-01520:start -->
#### The risk of KV cache compression

<!-- claim:SF-2026-ARXIV-2607-01520:start -->KV compressibility is context- and query-family-dependent rather than a fixed ratio. Response covariance gives a graded spectral risk boundary: fast decay permits sparse summaries, while lookup-like or flat-tail contexts impose a near-full-cache lower bound. The theorem does not predict final semantics or remove runtime validation, but it explains when compression should abstain and why FullKV remains necessary. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01520:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** KV compressibility is context- and query-family-dependent rather than a fixed ratio. Response covariance gives a graded spectral risk boundary: fast decay permits sparse summaries, while lookup-like or flat-tail contexts impose a near-full-cache lower bound. The theorem does not predict final semantics or remove runtime validation, but it explains when compression should abstain and why FullKV remains necessary. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01520v1#S3 :: KV compression as sparse approximation of a context measure and response-covariance compressibility; https://arxiv.org/html/2607.01520v1#S4 :: query-aware/agnostic minimax upper and lower bounds; https://arxiv.org/html/2607.01520v1#S5 :: causal merge-reduce algorithms`；Evaluation：`https://arxiv.org/html/2607.01520v1#S6 and https://arxiv.org/html/2607.01520v1#A4 :: focused LongBench-v2 experiments on Qwen3-32B, single NVIDIA H100, stated budgets/baselines and one fixed seed for randomized methods`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01520v1#S4.SS3 :: spectral lower bounds show lookup-like contexts can require nearly full support; practical experiments are targeted, single-GPU/single-seed and do not establish semantic quality or production SLO generally`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-01520:end -->

## 4. Benchmark Contracts

本日报不转述性能 headline，`Benchmark Claim` 均为 `no`。论文实验只用于限定机制证据，不把不同模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 拼成跨论文排名。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-00466 | score_7_9;potential_books_delta | selected | DA-20260702-2607-00466 | — | V2=9/9；MoE Decode 的成本不仅由 queue length 决定，还由 batch 激活的 distinct expert working set 决定。把 prefill expert signature 与 KV block 生命周期绑定，再在 locality band 内做 load-aware routing，可以复用 expert weights；代价是 calibration/reclustering、signature metadata、load-locality conflict 和 prefix/worker epoch consistency。Dense 或 expert locality 弱时，普通 least-load routing 仍更合理。；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260702-2607-00466 |
| SF-2026-ARXIV-2607-00760 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“KV compression can jointly vary retained token count and per-token feature rank instead of treating eviction and quantization as isolated policies.”；V2=3/3/2。与同 owner 入选 `SF-2026-ARXIV-2607-01520` 相比，本项没有更高的 Design Delta / System Reach / Durability。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-00760 |
| SF-2026-ARXIV-2607-01299 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“For hybrid attention, reusable state is not always a list of per-token KV.”；V2=3/3/3。HYPIC 与已入选的 KV compression risk 均为 9/9、均需 Integrate。长叙事优先保留后者，因为 response-spectrum 上下界给出跨 eviction、quantization 与 summary policy 可复用的 abstention/risk contract；HYPIC 的可组合 transition 则受 hybrid linear/full-attention architecture、segment operator 与 seam repair 约束，系统增量已在独立 Books 段落完整承载。 | analysis-decision:SF-2026-ARXIV-2607-01299 |
| SF-2026-ARXIV-2607-01071 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“Memory quality must separate retrieval success from downstream adoption: a relevant memory can be retrieved yet should be ignored, constrained, superseded or used only for personalization.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-01211` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-01071 |
| SF-2026-ARXIV-2607-01211 | score_7_9;potential_books_delta | selected | DA-20260702-2607-01211 | — | V2=8/9；Executable evaluation must validate the reference artifact before judging candidates and must expose sensitivity to machine, repetition and aggregation rules. The evaluation chapter already contains this exact reference-first admission chain and its representativeness boundary.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260702-2607-01211 |
| SF-2026-ARXIV-2607-01224 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“Memory policy can be optimized as a versioned artifact through a held-out promotion loop, while memory-operation proficiency can be trained separately from task-action authority.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-01211` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-01224 |
| SF-2026-ARXIV-2607-01520 | score_7_9;potential_books_delta | selected | DA-20260702-2607-01520 | — | V2=9/9；KV compressibility is context- and query-family-dependent rather than a fixed ratio. Response covariance gives a graded spectral risk boundary: fast decay permits sparse summaries, while lookup-like or flat-tail contexts impose a near-full-cache lower bound. The theorem does not predict final semantics or remove runtime validation, but it explains when compression should abstain and why FullKV remains necessary.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260702-2607-01520 |

<!-- analysis:DA-20260702-2607-01520:start -->
### The risk of KV cache compression

**旧方案为何合理。** 本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。** 当状态局部、规模较小、workload 稳定或 SLO 宽松时，这一基线仍然成立。（现有命题定位：`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）

**约束变化与机制。** KV compressibility is context- and query-family-dependent rather than a fixed ratio. Response covariance gives a graded spectral risk boundary: fast decay permits sparse summaries, while lookup-like or flat-tail contexts impose a near-full-cache lower bound. The theorem does not predict final semantics or remove runtime validation, but it explains when compression should abstain and why FullKV remains necessary. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-KV-CACHE` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** 新机制以额外 metadata、选择/压缩误差、计算或恢复责任换取作者 workload 内的收益；未披露的 model、hardware、precision、length、batch、concurrency、SLO 与 evaluator 不做补推。旧方案仍在新增成本高于收益时成立，下一步需要跨 workload、故障与长期状态的独立验证。

<!-- analysis:DA-20260702-2607-01520:end -->

<!-- analysis:DA-20260702-2607-00466:start -->
### ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving

**旧方案为何合理。** 本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。** 当状态局部、规模较小、workload 稳定或 SLO 宽松时，这一基线仍然成立。（现有命题定位：`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）

**约束变化与机制。** MoE Decode 的成本不仅由 queue length 决定，还由 batch 激活的 distinct expert working set 决定。把 prefill expert signature 与 KV block 生命周期绑定，再在 locality band 内做 load-aware routing，可以复用 expert weights；代价是 calibration/reclustering、signature metadata、load-locality conflict 和 prefix/worker epoch consistency。Dense 或 expert locality 弱时，普通 least-load routing 仍更合理。 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-SCHEDULING` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** 新机制以额外 metadata、选择/压缩误差、计算或恢复责任换取作者 workload 内的收益；未披露的 model、hardware、precision、length、batch、concurrency、SLO 与 evaluator 不做补推。旧方案仍在新增成本高于收益时成立，下一步需要跨 workload、故障与长期状态的独立验证。

<!-- analysis:DA-20260702-2607-00466:end -->

<!-- analysis:DA-20260702-2607-01211:start -->
### Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?

**旧方案为何合理。** Benchmark admission first rebuilds and replays the immutable reference artifact across machine and round, then measures infrastructure and scorer variance before candidates are compared. 当状态局部、规模较小、workload 稳定或 SLO 宽松时，这一基线仍然成立。（现有命题定位：`books/part-06-ai-infrastructure/66-evaluation-system.md#L729-L747`）

**约束变化与机制。** Executable evaluation must validate the reference artifact before judging candidates and must expose sensitivity to machine, repetition and aggregation rules. The evaluation chapter already contains this exact reference-first admission chain and its representativeness boundary. 这条证据与现有主线的关系是 `Layering / Dependency`：它改变或补充 `PLATFORM-EVALUATION-SYSTEM` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** 新机制以额外 metadata、选择/压缩误差、计算或恢复责任换取作者 workload 内的收益；未披露的 model、hardware、precision、length、batch、concurrency、SLO 与 evaluator 不做补推。旧方案仍在新增成本高于收益时成立，下一步需要跨 workload、故障与长期状态的独立验证。

<!-- analysis:DA-20260702-2607-01211:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-00760:start -->《MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression》已完成 Deep Source Review。本 family 的独立增量为“KV compression can jointly vary retained token count and per-token feature rank instead of treating eviction and quantization as isolated policies.”；V2=3/3/2。与同 owner 入选 `SF-2026-ARXIV-2607-01520` 相比，本项没有更高的 Design Delta / System Reach / Durability。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-00760:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-01299:start -->《HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching》已完成 Deep Source Review。本 family 的独立增量为“For hybrid attention, reusable state is not always a list of per-token KV.”；V2=3/3/3。HYPIC 与已入选的 KV compression risk 均为 9/9、均需 Integrate。长叙事优先保留后者，因为 response-spectrum 上下界给出跨 eviction、quantization 与 summary policy 可复用的 abstention/risk contract；HYPIC 的可组合 transition 则受 hybrid linear/full-attention architecture、segment operator 与 seam repair 约束，系统增量已在独立 Books 段落完整承载。<!-- analysis-decision:SF-2026-ARXIV-2607-01299:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-01071:start -->《MemSyco-Bench: Benchmarking Sycophancy in Agent Memory》已完成 Deep Source Review。本 family 的独立增量为“Memory quality must separate retrieval success from downstream adoption: a relevant memory can be retrieved yet should be ignored, constrained, superseded or used only for personalization.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-01211` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-01071:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-01224:start -->《AutoMem: Automated Learning of Memory as a Cognitive Skill》已完成 Deep Source Review。本 family 的独立增量为“Memory policy can be optimized as a versioned artifact through a held-out promotion loop, while memory-operation proficiency can be trained separately from task-action authority.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-01211` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-01224:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-00466 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L209 | books/part-05-inference-system/55-pd-disaggregation.md#L14-L14; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L14-L14 | existing:SF-2026-ARXIV-2607-00466 | delta:SF-2026-ARXIV-2607-00466 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-00466 |
| SF-2026-ARXIV-2607-00501 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L146-L157 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-00501 | delta:SF-2026-ARXIV-2607-00501 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-00501 |
| SF-2026-ARXIV-2607-00760 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L413 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2607-00760 | delta:SF-2026-ARXIV-2607-00760 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-00760 |
| SF-2026-ARXIV-2607-01299 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L584 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2607-01299 | delta:SF-2026-ARXIV-2607-01299 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-01299 |
| SF-2026-ARXIV-2607-01065 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L452-L482 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2607-01065 | delta:SF-2026-ARXIV-2607-01065 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-01065 |
| SF-2026-ARXIV-2607-01071 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L628-L658 | books/part-07-agent/76-rag.md#L14-L14; books/part-07-agent/78-tool-calling.md#L14-L14 | existing:SF-2026-ARXIV-2607-01071 | delta:SF-2026-ARXIV-2607-01071 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-01071 |
| SF-2026-ARXIV-2607-01211 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L729-L747 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-01211 | delta:SF-2026-ARXIV-2607-01211 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-01211 |
| SF-2026-ARXIV-2607-01224 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L343-L433 | books/part-07-agent/76-rag.md#L14-L14; books/part-07-agent/78-tool-calling.md#L14-L14 | existing:SF-2026-ARXIV-2607-01224 | delta:SF-2026-ARXIV-2607-01224 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-01224 |
| SF-2026-ARXIV-2607-01520 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L650 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2607-01520 | delta:SF-2026-ARXIV-2607-01520 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-01520 |

<!-- books-review:SF-2026-ARXIV-2607-00466:start --><!-- existing:SF-2026-ARXIV-2607-00466:start -->对读 `books/part-05-inference-system/56-inference-scheduling.md#L209` 与相邻章节后，现有命题（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）为：本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**<!-- existing:SF-2026-ARXIV-2607-00466:end --><!-- delta:SF-2026-ARXIV-2607-00466:start -->新增证据边界：MoE Decode 的成本不仅由 queue length 决定，还由 batch 激活的 distinct expert working set 决定。把 prefill expert signature 与 KV block 生命周期绑定，再在 locality band 内做 load-aware routing，可以复用 expert weights；代价是 calibration/reclustering、signature metadata、load-locality conflict 和 prefix/worker epoch consistency。Dense 或 expert locality 弱时，普通 least-load routing 仍更合理。 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L209`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-00466:end --><!-- books-review:SF-2026-ARXIV-2607-00466:end -->

<!-- books-review:SF-2026-ARXIV-2607-00501:start --><!-- existing:SF-2026-ARXIV-2607-00501:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L146-L157` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L146-L157`）为：A hardware-specialized execution path can fuse layout, precision, kernel and scheduling for a narrow workload, while the general library path retains broader coverage, portability and maintenance stability.<!-- existing:SF-2026-ARXIV-2607-00501:end --><!-- delta:SF-2026-ARXIV-2607-00501:start -->新增证据边界：A hardware-native engine can remove generic framework allocation, graph and dispatch overhead through preallocated buffers, descriptor-driven architecture differences and chip-specialized fusion. The gain trades portability and scheduling breadth for a narrower hardware contract; the chapter already owns this specialization-versus-portability branch and its benchmark boundary. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-00501:end --><!-- books-review:SF-2026-ARXIV-2607-00501:end -->

<!-- books-review:SF-2026-ARXIV-2607-00760:start --><!-- existing:SF-2026-ARXIV-2607-00760:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L413` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）为：本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**<!-- existing:SF-2026-ARXIV-2607-00760:end --><!-- delta:SF-2026-ARXIV-2607-00760:start -->新增证据边界：KV compression can jointly vary retained token count and per-token feature rank instead of treating eviction and quantization as isolated policies. This enlarges the quality-capacity search space but requires a packed physical layout, fused consumer kernel, background encoding, strategy versioning and fragmentation control; a logical compression ratio without these paths is not a serving gain. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L413`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-00760:end --><!-- books-review:SF-2026-ARXIV-2607-00760:end -->

<!-- books-review:SF-2026-ARXIV-2607-01299:start --><!-- existing:SF-2026-ARXIV-2607-01299:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L584` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）为：本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**<!-- existing:SF-2026-ARXIV-2607-01299:end --><!-- delta:SF-2026-ARXIV-2607-01299:start -->新增证据边界：For hybrid attention, reusable state is not always a list of per-token KV. A linear-attention segment may need both zero-state result and cumulative transition operator so segments compose in order; sparse full-attention layers then need bounded seam repair. This enables position-independent reuse but adds operator identity, numerical drift, seam policy, composition order and fallback semantics. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L584`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-01299:end --><!-- books-review:SF-2026-ARXIV-2607-01299:end -->

<!-- books-review:SF-2026-ARXIV-2607-01065:start --><!-- existing:SF-2026-ARXIV-2607-01065:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L452-L482` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L452-L482`）为：KV quantization must be evaluated at the attention consumer and over autoregressive feedback, with physical metadata, kernel and effective-bit costs included rather than inferred from tensor reconstruction alone.<!-- existing:SF-2026-ARXIV-2607-01065:end --><!-- delta:SF-2026-ARXIV-2607-01065:start -->新增证据边界：At extreme vector-quantization budgets, separately modeling vector direction and scale can preserve information that ordinary Euclidean centroids conflate. This is a quantizer-design branch, not proof of system speed: codebook lookup, metadata, kernel support and autoregressive error still determine whether sub-bit storage improves serving. Existing attention-distortion and effective-bit accounting already cover the lasting conclusion. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-01065:end --><!-- books-review:SF-2026-ARXIV-2607-01065:end -->

<!-- books-review:SF-2026-ARXIV-2607-01071:start --><!-- existing:SF-2026-ARXIV-2607-01071:start -->对读 `books/part-07-agent/77-memory.md#L628-L658` 与相邻章节后，现有命题（`books/part-07-agent/77-memory.md#L628-L658`）为：Memory retrieval is not fact adjudication: read policy must distinguish authority, valid time, contradiction, supersession and explicit unknown-current state before deciding whether to use or abstain.<!-- existing:SF-2026-ARXIV-2607-01071:end --><!-- delta:SF-2026-ARXIV-2607-01071:start -->新增证据边界：Memory quality must separate retrieval success from downstream adoption: a relevant memory can be retrieved yet should be ignored, constrained, superseded or used only for personalization. The existing chapter already gives fact/retrieval-policy separation, authority, contradiction and post-retrieval risk gates, so this source strengthens evidence without changing the mechanism owner. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-01071:end --><!-- books-review:SF-2026-ARXIV-2607-01071:end -->

<!-- books-review:SF-2026-ARXIV-2607-01211:start --><!-- existing:SF-2026-ARXIV-2607-01211:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L729-L747` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L729-L747`）为：Benchmark admission first rebuilds and replays the immutable reference artifact across machine and round, then measures infrastructure and scorer variance before candidates are compared.<!-- existing:SF-2026-ARXIV-2607-01211:end --><!-- delta:SF-2026-ARXIV-2607-01211:start -->新增证据边界：Executable evaluation must validate the reference artifact before judging candidates and must expose sensitivity to machine, repetition and aggregation rules. The evaluation chapter already contains this exact reference-first admission chain and its representativeness boundary. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-01211:end --><!-- books-review:SF-2026-ARXIV-2607-01211:end -->

<!-- books-review:SF-2026-ARXIV-2607-01224:start --><!-- existing:SF-2026-ARXIV-2607-01224:start -->对读 `books/part-07-agent/77-memory.md#L343-L433` 与相邻章节后，现有命题（`books/part-07-agent/77-memory.md#L343-L433`）为：A learned Memory policy is a derived, versioned procedural asset whose applicability, source episodes and validation results must pass held-out promotion and retain provenance and rollback.<!-- existing:SF-2026-ARXIV-2607-01224:end --><!-- delta:SF-2026-ARXIV-2607-01224:start -->新增证据边界：Memory policy can be optimized as a versioned artifact through a held-out promotion loop, while memory-operation proficiency can be trained separately from task-action authority. The existing Memory chapter already separates derived policy, validation, promotion/rollback and Workflow ownership, so the source is corroborating rather than a new owner mechanism. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-01224:end --><!-- books-review:SF-2026-ARXIV-2607-01224:end -->

<!-- books-review:SF-2026-ARXIV-2607-01520:start --><!-- existing:SF-2026-ARXIV-2607-01520:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L650` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）为：本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**<!-- existing:SF-2026-ARXIV-2607-01520:end --><!-- delta:SF-2026-ARXIV-2607-01520:start -->新增证据边界：KV compressibility is context- and query-family-dependent rather than a fixed ratio. Response covariance gives a graded spectral risk boundary: fast decay permits sparse summaries, while lookup-like or flat-tail contexts impose a near-full-cache lower bound. The theorem does not predict final semantics or remove runtime validation, but it explains when compression should abstain and why FullKV remains necessary. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L650`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-01520:end --><!-- books-review:SF-2026-ARXIV-2607-01520:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260702-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260702; semantic-review:SA-20260702-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260702-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-00351; review:SF-2026-ARXIV-2607-00466; review:SF-2026-ARXIV-2607-00482; review:SF-2026-ARXIV-2607-00501; review:SF-2026-ARXIV-2607-00666; review:SF-2026-ARXIV-2607-00760; review:SF-2026-ARXIV-2607-00908; review:SF-2026-ARXIV-2607-02604; review:SF-2026-ARXIV-2607-01299; review:SF-2026-ARXIV-2607-00972; review:SF-2026-ARXIV-2607-01065; review:SF-2026-ARXIV-2607-01071; review:SF-2026-ARXIV-2607-01104; review:SF-2026-ARXIV-2607-01211; review:SF-2026-ARXIV-2607-01212; review:SF-2026-ARXIV-2607-01224; review:SF-2026-ARXIV-2607-01378; review:SF-2026-ARXIV-2607-01425; review:SF-2026-ARXIV-2607-01520; semantic-review:SA-20260702-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260702-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260702-2607-01520; analysis:DA-20260702-2607-00466; analysis:DA-20260702-2607-01211; semantic-review:SA-20260702-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260702-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-00466; books-review:SF-2026-ARXIV-2607-00501; books-review:SF-2026-ARXIV-2607-00760; books-review:SF-2026-ARXIV-2607-01299; books-review:SF-2026-ARXIV-2607-01065; books-review:SF-2026-ARXIV-2607-01071; books-review:SF-2026-ARXIV-2607-01211; books-review:SF-2026-ARXIV-2607-01224; books-review:SF-2026-ARXIV-2607-01520; semantic-review:SA-20260702-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260702-COVERAGE:start -->Fresh-context review reconciled the exact window, partition totals, date bucket and denominator.<!-- semantic-review:SA-20260702-COVERAGE:end -->
<!-- semantic-review:SA-20260702-EVIDENCE:start -->Fresh-context review reconciled all 19 frozen families: 7 Deep, 2 Standard and 10 Closure; 0 pending and 0 blocked rows remain explicitly outside mechanism claims.<!-- semantic-review:SA-20260702-EVIDENCE:end -->
<!-- semantic-review:SA-20260702-SELECTION:start -->Fresh-context review reconciled 7 eligible Deep families: 3 selected and 4 not selected; the narrative limit does not downgrade any completed Source Review.<!-- semantic-review:SA-20260702-SELECTION:end -->
<!-- semantic-review:SA-20260702-BOOKS:start -->Fresh-context review checked current owner and adjacent chapter handoffs; 4 个 family 已定位到实际 Books 段落，5 个 family 的 No Change 结论可定位，0 个 Weekly Only disposition 已由逐 family Source Review 确认为不进入 Books。<!-- semantic-review:SA-20260702-BOOKS:end -->

## 8. Ignored Noise

1285 个窗口内 identity 中，1266 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：4 个 `Integrate`，5 个 `No Change — Existing Coverage`，0 个 `Weekly Only — Context`，10 个 `Rejected — Low Durability / Out of Scope`；Deep 7 / Standard 2。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/02/README.md`。
- 本日报长期 delta 已同步至：`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`、`books/part-05-inference-system/56-inference-scheduling.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [Unleashing More Actions via Action Compositional Training for VLA Models](https://arxiv.org/abs/2607.00351v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-26
- [ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving](https://arxiv.org/abs/2607.00466v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-27
- [Know When to Stop: Segment-Level Credit Assignment for Reducing Overthinking](https://arxiv.org/abs/2607.00482v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-26
- [BaseRT: Best-in-Class LLM Inference on Apple Silicon via Native Metal](https://arxiv.org/abs/2607.00501v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-27
- [Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts](https://arxiv.org/abs/2607.00666v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-26
- [MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression](https://arxiv.org/abs/2607.00760v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-27
- [Beyond Activation Alignment:The Alignment-Diversity Tradeoff in Task-Aware LLM Quantization](https://arxiv.org/abs/2607.00908v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-26
- [DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation](https://arxiv.org/abs/2607.02604v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-26
- [HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching](https://arxiv.org/abs/2607.01299v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-27
- [Bayesian Uncertainty Propagation for Agentic RAG Pipelines: A Proof-of-Concept Study on Multi-Hop Question Answering](https://arxiv.org/abs/2607.00972v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-26
- [GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache](https://arxiv.org/abs/2607.01065v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-27
- [MemSyco-Bench: Benchmarking Sycophancy in Agent Memory](https://arxiv.org/abs/2607.01071v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-27
- [CausalMix: Data Mixture as Causal Inference for Language Model Training](https://arxiv.org/abs/2607.01104v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-26
- [Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?](https://arxiv.org/abs/2607.01211v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-27
- [FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action Model](https://arxiv.org/abs/2607.01212v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-26
- [AutoMem: Automated Learning of Memory as a Cognitive Skill](https://arxiv.org/abs/2607.01224v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-27
- [Neuro-Symbolic Safety Guidance for Vision-Language-Action Models via Constrained Flow Matching](https://arxiv.org/abs/2607.01378v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-26
- [Agent4cs: A Multi-agent System for Code Summarization in Large Hierarchical Codebases](https://arxiv.org/abs/2607.01425v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-26
- [The risk of KV cache compression](https://arxiv.org/abs/2607.01520v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-27
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
