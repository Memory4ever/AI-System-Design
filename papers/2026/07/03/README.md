# Daily Research — 2026-07-03

**Research Date:** 2026-07-03

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-02 09:00:00 ～ 2026-07-03 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 1214 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 26 个。当前路由账目为 10 个 Deep、3 个 Standard、13 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-03 |
| Window End | 2026-07-03 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-03-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-26T18:00:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-02T09:00:00+08:00 | 2026-07-03T09:00:00+08:00 | 2026-08-26T18:00:00+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 1214 | SF-2026-ARXIV-2607-01579<br>SF-2026-ARXIV-2607-01586<br>SF-2026-ARXIV-2607-01595<br>SF-2026-ARXIV-2607-01617<br>SF-2026-ARXIV-2607-01646<br>SF-2026-ARXIV-2607-01647<br>SF-2026-ARXIV-2607-01658<br>SF-2026-ARXIV-2607-01678<br>SF-2026-ARXIV-2607-01766<br>SF-2026-ARXIV-2607-01804<br>SF-2026-ARXIV-2607-01831<br>SF-2026-ARXIV-2607-01874<br>SF-2026-ARXIV-2607-01935<br>SF-2026-ARXIV-2607-01938<br>SF-2026-ARXIV-2607-02032<br>SF-2026-ARXIV-2607-02043<br>SF-2026-ARXIV-2607-02045<br>SF-2026-ARXIV-2607-02092<br>SF-2026-ARXIV-2607-02182<br>SF-2026-ARXIV-2607-02255<br>SF-2026-ARXIV-2607-02322<br>SF-2026-ARXIV-2607-02440<br>SF-2026-ARXIV-2607-02512<br>SF-2026-ARXIV-2607-02517<br>SF-2026-ARXIV-2607-02686<br>SF-2026-ARXIV-2607-02840 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-03T09:00:00+08:00 | coverage:SRC-ARXIV:20260703 | GAP-ARXIV-DIRECT-RESET-20260703 |

<!-- coverage:SRC-ARXIV:20260703:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 1214 unique identities in this strict window; 26 routed families.<!-- coverage:SRC-ARXIV:20260703:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 26 个 family：exact v1 为 6 个 family 披露 artifact/evidence locator，其中 6 个提供外部 repository/project/demo locator，另有 20 个未披露；本日确认 0 个 family、0 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-01579 | arXiv:2607.01579v1 | paper-v1:2607.01579 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-01579 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-01579 | no |
| SF-2026-ARXIV-2607-01586 | arXiv:2607.01586v1 | paper-v1:2607.01586 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-01586 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-01595 | arXiv:2607.01595v1 | paper-v1:2607.01595 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-01595 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-01617 | arXiv:2607.01617v1 | paper-v1:2607.01617 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-01617 | self | — | new_in_window | INFER-PD-DISAGGREGATION | Integrate | books-review:SF-2026-ARXIV-2607-01617 | no |
| SF-2026-ARXIV-2607-01646 | arXiv:2607.01646v1 | paper-v1:2607.01646 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-01646 | self | — | new_in_window | TRAIN-CHECKPOINT | Integrate | books-review:SF-2026-ARXIV-2607-01646 | no |
| SF-2026-ARXIV-2607-01647 | arXiv:2607.01647v1 | paper-v1:2607.01647 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-01647 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-01647 | no |
| SF-2026-ARXIV-2607-01658 | arXiv:2607.01658v1 | paper-v1:2607.01658 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-01658 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-01678 | arXiv:2607.01678v1 | paper-v1:2607.01678 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-01678 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2607-01678 | no |
| SF-2026-ARXIV-2607-01766 | arXiv:2607.01766v1 | paper-v1:2607.01766 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-01766 | self | — | new_in_window | AGENT-MULTI-AGENT | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-01804 | arXiv:2607.01804v1 | paper-v1:2607.01804 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-01804 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-01831 | arXiv:2607.01831v1 | paper-v1:2607.01831 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-01831 | self | — | new_in_window | INFER-PD-DISAGGREGATION | Integrate | books-review:SF-2026-ARXIV-2607-01831 | no |
| SF-2026-ARXIV-2607-01874 | arXiv:2607.01874v1 | paper-v1:2607.01874 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-01874 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-01874 | no |
| SF-2026-ARXIV-2607-01935 | arXiv:2607.01935v1 | paper-v1:2607.01935 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-01935 | self | — | new_in_window | AGENT-MEMORY | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-01938 | arXiv:2607.01938v1 | paper-v1:2607.01938 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-01938 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02032 | arXiv:2607.02032v1 | paper-v1:2607.02032 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-02032 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-02032 | no |
| SF-2026-ARXIV-2607-02043 | arXiv:2607.02043v1 | paper-v1:2607.02043 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-02043 | self | — | new_in_window | INFER-PD-DISAGGREGATION | Integrate | books-review:SF-2026-ARXIV-2607-02043 | no |
| SF-2026-ARXIV-2607-02045 | arXiv:2607.02045v1 | paper-v1:2607.02045 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02045 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02092 | arXiv:2607.02092v1 | paper-v1:2607.02092 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 1 | 1 | 0 | 2 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02092 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02182 | arXiv:2607.02182v1 | paper-v1:2607.02182 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02182 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02255 | arXiv:2607.02255v1 | paper-v1:2607.02255 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-02255 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-02255 | no |
| SF-2026-ARXIV-2607-02322 | arXiv:2607.02322v1 | paper-v1:2607.02322 | 2026-W27 | 2026-07-02 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02322 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02440 | arXiv:2607.02440v1 | paper-v1:2607.02440 | 2026-W27 | 2026-07-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-02440 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-02440 | no |
| SF-2026-ARXIV-2607-02512 | arXiv:2607.02512v1 | paper-v1:2607.02512 | 2026-W27 | 2026-07-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-02512 | self | — | new_in_window | TRAIN-LORA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-02512 | no |
| SF-2026-ARXIV-2607-02517 | arXiv:2607.02517v1 | paper-v1:2607.02517 | 2026-W27 | 2026-07-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-02517 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-02517 | no |
| SF-2026-ARXIV-2607-02686 | arXiv:2607.02686v1 | paper-v1:2607.02686 | 2026-W27 | 2026-07-03 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02686 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02840 | arXiv:2607.02840v1 | paper-v1:2607.02840 | 2026-W27 | 2026-07-03 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02840 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Rejected — Low Durability / Out of Scope | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-01579 | RP-825760fa1992a0da | standard | arXiv:2607.01579v1 | SRC-ARXIV@arXiv:2607.01579v1 | https://arxiv.org/html/2607.01579v1#method :: versioned feature extraction, inference-cost prediction and a value-of-information benchmark gate for launch placement | https://arxiv.org/html/2607.01579v1#evaluation :: author evaluation covers held-out cluster cells, placement accuracy, calibration, OOD abstention and ablations; no production scheduler trial is claimed | https://arxiv.org/html/2607.01579v1#threats-to-validity and https://arxiv.org/html/2607.01579v1#scope-and-future-work :: synthetic/collected launch data, site-specific features, stale telemetry and limited OOD coverage constrain external validity | Not Disclosed — v1 references telemetry utilities but does not link an event-time OmniPilot implementation | claim:SF-2026-ARXIV-2607-01579 | complete |
| SF-2026-ARXIV-2607-01586 | RP-cecdf71faad2df8c | closure | doi:10.48550/arxiv.2607.01586@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.01586@v1 | doi:10.48550/arxiv.2607.01586#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-01586 | complete |
| SF-2026-ARXIV-2607-01595 | RP-a45b902c671ab4a9 | closure | doi:10.48550/arxiv.2607.01595@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.01595@v1 | doi:10.48550/arxiv.2607.01595#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-01595 | complete |
| SF-2026-ARXIV-2607-01617 | RP-ffe9b5599da602a1 | deep | arXiv:2607.01617v1 | SRC-ARXIV@arXiv:2607.01617v1 | https://arxiv.org/html/2607.01617v1#S3 :: 3D logic-stacked serving architecture separates vertical KV-transfer traffic from lateral tensor-parallel collectives | https://arxiv.org/html/2607.01617v1#S4 :: in-house simulator studies Llama-3 8B/70B and OPT-175B under disclosed serving traces and iso-bandwidth comparisons; no fabricated chip or production deployment is evaluated | https://arxiv.org/html/2607.01617v1#S3 :: package area, vertical-link bandwidth, thermals and yield constrain the architecture; https://arxiv.org/html/2607.01617v1#S4 :: results depend on the in-house simulator, modeled workloads and iso-bandwidth comparison. Queueing and KV ownership are explicit system non-proof boundaries, not claims attributed to the authors | Not Disclosed — no event-time public simulator or hardware artifact is linked by v1 | claim:SF-2026-ARXIV-2607-01617 | complete |
| SF-2026-ARXIV-2607-01646 | RP-bb93b08d3c4fedc7 | deep | arXiv:2607.01646v1 | SRC-ARXIV@arXiv:2607.01646v1 | https://arxiv.org/html/2607.01646v1#S5 and https://arxiv.org/html/2607.01646v1#S6 :: per-step ping-pong host snapshots, peer replication of optimizer shards, failure classification, topology repair and logical-shard restoration | https://arxiv.org/html/2607.01646v1#S7 :: injected fail-stop/NCCL/storage faults on Perlmutter and Vista, up to 512 A100 or 64 GH200 GPUs and GPT-style models up to 65B; observed overlap and recovery are platform-bound | https://arxiv.org/html/2607.01646v1#S5.SS3 and https://arxiv.org/html/2607.01646v1#S8 :: silent corruption/software bugs remain external fallback; redundancy, failure-domain independence, spare capacity, host/network headroom and two-system coverage limit generalization | Not Disclosed — v1 describes a PyTorch/Megatron-LM implementation but does not link an event-time author repository/commit | claim:SF-2026-ARXIV-2607-01646 | complete |
| SF-2026-ARXIV-2607-01647 | RP-4bf5c32f26cc436a | standard | arXiv:2607.01647v1 | SRC-ARXIV@arXiv:2607.01647v1 | https://arxiv.org/html/2607.01647v1#S3 through https://arxiv.org/html/2607.01647v1#S5 :: task taxonomy, data-agent harness, trajectory capture and multi-level grading | https://arxiv.org/html/2607.01647v1#S6 :: selected agents are evaluated across the released task suite with task/skill slices; rankings remain model-plus-harness results | https://arxiv.org/html/2607.01647v1#S5 and https://arxiv.org/html/2607.01647v1#S6 :: the benchmark fixes its task construction, harness and grader/evaluation protocol; no dedicated limitations section is disclosed, so enterprise permission/schema drift and cross-harness validity remain explicit non-proof boundaries rather than author findings | https://github.com/AgenticDataBench/AgenticDataBench :: author repository linked by v1; event-time commit was not established | claim:SF-2026-ARXIV-2607-01647 | complete |
| SF-2026-ARXIV-2607-01658 | RP-cdc8f7701aea43bc | closure | doi:10.48550/arxiv.2607.01658@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.01658@v1 | doi:10.48550/arxiv.2607.01658#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-01658 | complete |
| SF-2026-ARXIV-2607-01678 | RP-618a2b3104ac2c84 | deep | arXiv:2607.01678v1 | SRC-ARXIV@arXiv:2607.01678v1 | https://arxiv.org/html/2607.01678v1#S4 :: optimizer-aware first-moment masks, one-step-delayed refreshed synchronization, sharding-aligned mask ownership and reconstruction from one sparse synchronized buffer | https://arxiv.org/html/2607.01678v1#S5 :: GPT-345M/OpenWebText and Llama-500M/SlimPajama full pretraining uses 32 GH200 GPUs; Llama-500M and Llama-1.8B per-step profiling and strong-scaling studies span 4–64 GH200 GPUs, with disclosed sparsity, loss/tasks and timing measurements | https://arxiv.org/html/2607.01678v1#S3 and https://arxiv.org/html/2607.01678v1#S4 :: mask stability and delayed reuse are empirical/optimizer-specific; https://arxiv.org/html/2607.01678v1#S5 :: evaluation is limited to the disclosed AdamS models and GH200 setup, while the paper notes PCIe offload may add overhead on other clusters; no dedicated limitations section establishes broader convergence | Not Disclosed — v1 states a Megatron-LM implementation but does not link an event-time author repository/commit | claim:SF-2026-ARXIV-2607-01678 | complete |
| SF-2026-ARXIV-2607-01766 | RP-83b1da08081d2510 | closure | doi:10.48550/arxiv.2607.01766@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.01766@v1 | doi:10.48550/arxiv.2607.01766#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-01766 | complete |
| SF-2026-ARXIV-2607-01804 | RP-e1a57df4e4c99df8 | closure | doi:10.48550/arxiv.2607.01804@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.01804@v1 | doi:10.48550/arxiv.2607.01804#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-01804 | complete |
| SF-2026-ARXIV-2607-01831 | RP-a4054cd3f2807f9b | deep | arXiv:2607.01831v1 | SRC-ARXIV@arXiv:2607.01831v1 | https://arxiv.org/html/2607.01831v1#S4 :: hierarchical KV quantization, prioritized low-bit-first transfer, speculative execution and verify/correct before exact commitment | https://arxiv.org/html/2607.01831v1#S6 :: author tests accuracy and latency on disclosed long-context models/tasks and Ascend-oriented LMCache/vLLM integration; production concurrency and independent replication are absent | https://arxiv.org/html/2607.01831v1#S2 :: ordinary complete-transfer and linear-quantization bottlenecks motivate the design; https://arxiv.org/html/2607.01831v1#S4 :: hierarchical approximation plus verification/correction add provisional-state work; https://arxiv.org/html/2607.01831v1#S6 and https://arxiv.org/html/2607.01831v1#S8 :: benefit depends on the evaluated models/hardware and successful transfer/computation overlap. Early bytes not being committed exact state is this review's correctness boundary | Not Disclosed — v1 cites LMCache-Ascend and vLLM-Ascend dependencies but no event-time author Lynx repository/commit | claim:SF-2026-ARXIV-2607-01831 | complete |
| SF-2026-ARXIV-2607-01874 | RP-caffa89928cf352e | deep | arXiv:2607.01874v1 | SRC-ARXIV@arXiv:2607.01874v1 | https://arxiv.org/html/2607.01874v1#S3 :: skill selection/following/composition/reflection decomposition, self-evolving trajectory rubrics and rubric-filtered offline training | https://arxiv.org/html/2607.01874v1#S4 :: rubric quality, agent skill-use and filtered-training ablations on selected libraries/tasks/models; judge and task contracts are pinned to the study | https://arxiv.org/html/2607.01874v1#S6 :: rubric induction/judging bias, skill overlap, library/task coverage and offline transfer limit claims; rubrics are not ground truth | Not Disclosed — no event-time author implementation repository is linked by v1 | claim:SF-2026-ARXIV-2607-01874 | complete |
| SF-2026-ARXIV-2607-01935 | RP-eb7371f4453723da | closure | doi:10.48550/arxiv.2607.01935@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.01935@v1 | doi:10.48550/arxiv.2607.01935#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-01935 | complete |
| SF-2026-ARXIV-2607-01938 | RP-d6f82a369ed76c29 | closure | doi:10.48550/arxiv.2607.01938@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.01938@v1 | doi:10.48550/arxiv.2607.01938#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-01938 | complete |
| SF-2026-ARXIV-2607-02032 | RP-de1a78a24fb61cfa | standard | arXiv:2607.02032v1 | SRC-ARXIV@arXiv:2607.02032v1 | https://arxiv.org/html/2607.02032v1#S3 :: calibrated regression plus local/global source-instance selection for a budgeted proxy benchmark | https://arxiv.org/html/2607.02032v1#S4 :: leave-one-model-out prediction across 14 models, four target agent benchmarks and 19 source benchmarks with cost/quality sweeps | https://arxiv.org/html/2607.02032v1#A6 :: small calibration population, model/task distribution shift, source/target correlation and target-harness dependence prevent proxy scores from replacing final executable evaluation | https://github.com/neulab/pace :: author repository linked by v1; event-time commit was not established | claim:SF-2026-ARXIV-2607-02032 | complete |
| SF-2026-ARXIV-2607-02043 | RP-190c136b7275ac42 | deep | arXiv:2607.02043v1 | SRC-ARXIV@arXiv:2607.02043v1 | https://arxiv.org/html/2607.02043v1#S4 :: TTFT estimator, decode-step feasibility model and greedy chunk schedule that borrows only predicted TBT slack | https://arxiv.org/html/2607.02043v1#S6 :: vLLM 0.18.1 implementation on A100 clusters with DeepSeek-v2-Lite, bursty traces and stated P95 TTFT/TBT SLOs; results are workload-specific | https://arxiv.org/html/2607.02043v1#S7 :: central dispatcher, stale 100-ms observations, estimator error, no migration and omitted prefix-cache interactions constrain deployment | https://github.com/sudokara/Kairos :: author repository linked by v1; event-time commit was not established | claim:SF-2026-ARXIV-2607-02043 | complete |
| SF-2026-ARXIV-2607-02045 | RP-671cdb1b2e0f8d7e | closure | doi:10.48550/arxiv.2607.02045@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02045@v1 | doi:10.48550/arxiv.2607.02045#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02045 | complete |
| SF-2026-ARXIV-2607-02092 | RP-3ca8bda672ed4718 | closure | doi:10.48550/arxiv.2607.02092@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02092@v1 | doi:10.48550/arxiv.2607.02092#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02092 | complete |
| SF-2026-ARXIV-2607-02182 | RP-dc3f67b205c3afd5 | closure | doi:10.48550/arxiv.2607.02182@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02182@v1 | doi:10.48550/arxiv.2607.02182#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02182 | complete |
| SF-2026-ARXIV-2607-02255 | RP-df94101ad7fac06f | deep | arXiv:2607.02255v1 | SRC-ARXIV@arXiv:2607.02255v1 | https://arxiv.org/html/2607.02255v1#S4 and https://arxiv.org/html/2607.02255v1#S5 :: five typed visibility layers, per-decision composition, bounded episodic memory and fixed-harness ablations | https://arxiv.org/html/2607.02255v1#S6 :: small-sample within-harness and cross-backbone trials with statistical appendix; observed differences are not universal rankings | https://arxiv.org/html/2607.02255v1#S9 :: small cells, one game/character/version, unmatched accumulating-context agents and architectural scope limit generalization | https://github.com/AlayaLab/AgenticSTS :: author repository linked by v1; event-time commit was not established | claim:SF-2026-ARXIV-2607-02255 | complete |
| SF-2026-ARXIV-2607-02322 | RP-8db183feb55b6315 | closure | doi:10.48550/arxiv.2607.02322@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02322@v1 | doi:10.48550/arxiv.2607.02322#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02322 | complete |
| SF-2026-ARXIV-2607-02440 | RP-a4656a87ea9a4356 | deep | arXiv:2607.02440v1 | SRC-ARXIV@arXiv:2607.02440v1 | https://arxiv.org/html/2607.02440v1#S3 :: bounded environment-policy episodes, autonomous policy revision and explicit feedback/evaluation boundaries | https://arxiv.org/html/2607.02440v1#S4 and https://arxiv.org/html/2607.02440v1#S5 :: task-suite outcomes, post-hoc score trajectories and mechanism case studies under a fixed run protocol | https://arxiv.org/html/2607.02440v1#S5.SS3 :: diagnostics are post-hoc, task-family dependent and do not establish causal credit or open-ended safe self-improvement | https://github.com/Linzwcs/EvoPolicyGym :: author repository linked by v1; the paper also links the EvoPolicyGym-Exp-data Hugging Face dataset and project page, but event-time commits/revisions were not established | claim:SF-2026-ARXIV-2607-02440 | complete |
| SF-2026-ARXIV-2607-02512 | RP-4b0ddf30fc6742d2 | deep | arXiv:2607.02512v1 | SRC-ARXIV@arXiv:2607.02512v1 | https://arxiv.org/html/2607.02512v1#S2 and https://arxiv.org/html/2607.02512v1#S3 :: compiler converts a natural-language specification into a pseudo-program and adapter/prefix artifact consumed by a pinned interpreter | https://arxiv.org/html/2607.02512v1#S4 through https://arxiv.org/html/2607.02512v1#S10 :: FuzzyBench training, main results, ablations, noisy-specification robustness, local execution and quantization studies | https://arxiv.org/html/2607.02512v1#A14 :: compiler/interpreter dependence, fuzzy-task coverage, behavioral inspection, specification drift and lack of deterministic equivalence bound the claim | https://github.com/programasweights :: author organization linked by v1; exact repository/commit for the event-time artifact was not established | claim:SF-2026-ARXIV-2607-02512 | complete |
| SF-2026-ARXIV-2607-02517 | RP-28c7bcd4ee0bc36b | deep | arXiv:2607.02517v1 | SRC-ARXIV@arXiv:2607.02517v1 | https://arxiv.org/html/2607.02517v1#S3 :: trajectory planning, spatial/appearance conditioning, persistent dynamic context memory and causal chunk generation | https://arxiv.org/html/2607.02517v1#S4 :: author comparisons and ablations test identity/location persistence and promptable events in selected generated-video scenarios | https://arxiv.org/html/2607.02517v1#S4 and https://arxiv.org/html/2607.02517v1#S5 :: evaluation and conclusion are limited to selected synthetic/game video scenarios and acknowledge the domain gap; causal physics, unbounded horizon, closed-loop controllability and safe real-world action are explicit non-proof boundaries, while planner/projection, identity collision and chunk drift remain inferred system risks | Not Disclosed — no event-time public WorldDirector implementation repository is linked by v1 | claim:SF-2026-ARXIV-2607-02517 | complete |
| SF-2026-ARXIV-2607-02686 | RP-e0b8437a94b221f7 | closure | doi:10.48550/arxiv.2607.02686@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02686@v1 | doi:10.48550/arxiv.2607.02686#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02686 | complete |
| SF-2026-ARXIV-2607-02840 | RP-a7c69fe7fd759271 | closure | doi:10.48550/arxiv.2607.02840@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02840@v1 | doi:10.48550/arxiv.2607.02840#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02840 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-01579:start -->
#### OmniPilot: An Uncertainty-Aware LLM Inference Advisor for Heterogeneous GPU Clusters

<!-- claim:SF-2026-ARXIV-2607-01579:start -->A configuration predictor should be admitted only when its expected decision value exceeds benchmark cost and should abstain outside calibrated cells. The scheduling chapter already makes calibration identity, uncertainty, targeted silicon validation and rollback explicit, so this family strengthens that route without changing its owner. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01579:end -->

**旧方案与约束变化。** `Configuration search uses versioned primitive measurements and uncertainty-aware prediction only to narrow candidates; launch authority remains with targeted silicon validation, canary and rollback when calibration drifts or candidates are near-tied.`（`books/part-05-inference-system/56-inference-scheduling.md#L248-L301`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A configuration predictor should be admitted only when its expected decision value exceeds benchmark cost and should abstain outside calibrated cells. The scheduling chapter already makes calibration identity, uncertainty, targeted silicon validation and rollback explicit, so this family strengthens that route without changing its owner. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01579v1#method :: versioned feature extraction, inference-cost prediction and a value-of-information benchmark gate for launch placement`；Evaluation：`https://arxiv.org/html/2607.01579v1#evaluation :: author evaluation covers held-out cluster cells, placement accuracy, calibration, OOD abstention and ablations; no production scheduler trial is claimed`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01579v1#threats-to-validity and https://arxiv.org/html/2607.01579v1#scope-and-future-work :: synthetic/collected launch data, site-specific features, stale telemetry and limited OOD coverage constrain external validity`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-01579:end -->

<!-- review:SF-2026-ARXIV-2607-01586:start -->
#### VLAFlow: A Unified Training Framework for Vision-Language-Action Models via Co-training and Future Latent Alignment

<!-- claim:SF-2026-ARXIV-2607-01586:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-01586:end -->

- Identity：`arXiv:2607.01586v1`；first-public（Asia/Shanghai）：`2026-07-02`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-01586:end -->

<!-- review:SF-2026-ARXIV-2607-01595:start -->
#### Safe and Adaptive Cloud Healing: Verifying LLM-Generated Recovery Plans with a Neural-Symbolic World Model

<!-- claim:SF-2026-ARXIV-2607-01595:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-01595:end -->

- Identity：`arXiv:2607.01595v1`；first-public（Asia/Shanghai）：`2026-07-02`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-01595:end -->

<!-- review:SF-2026-ARXIV-2607-01617:start -->
#### 3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving

<!-- claim:SF-2026-ARXIV-2607-01617:start -->When PD KV transfer and decode collectives share a fabric, software scheduling cannot eliminate head-of-line interference. Mapping the two traffic classes to physically distinct link domains can protect the handoff critical path, but it spends packaging area, thermal/yield budget and topology flexibility; it remains an architecture-specific branch rather than a default PD requirement. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01617:end -->

**旧方案与约束变化。** `本章的核心判断是：**PD 分离利用 Prefill 与 Decode 在计算、memory、batch 和 SLO 上的差异实现独立资源规划，但必须用 KV transfer、跨池排队和更大故障面支付代价；它是否成立取决于 workload-specific break-even。**`（`books/part-05-inference-system/55-pd-disaggregation.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** When PD KV transfer and decode collectives share a fabric, software scheduling cannot eliminate head-of-line interference. Mapping the two traffic classes to physically distinct link domains can protect the handoff critical path, but it spends packaging area, thermal/yield budget and topology flexibility; it remains an architecture-specific branch rather than a default PD requirement. 它改变 `INFER-PD-DISAGGREGATION` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01617v1#S3 :: 3D logic-stacked serving architecture separates vertical KV-transfer traffic from lateral tensor-parallel collectives`；Evaluation：`https://arxiv.org/html/2607.01617v1#S4 :: in-house simulator studies Llama-3 8B/70B and OPT-175B under disclosed serving traces and iso-bandwidth comparisons; no fabricated chip or production deployment is evaluated`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01617v1#S3 :: package area, vertical-link bandwidth, thermals and yield constrain the architecture; https://arxiv.org/html/2607.01617v1#S4 :: results depend on the in-house simulator, modeled workloads and iso-bandwidth comparison. Queueing and KV ownership are explicit system non-proof boundaries, not claims attributed to the authors`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Alternative Branch`。
- Stable owner：`INFER-PD-DISAGGREGATION`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-01617:end -->

<!-- review:SF-2026-ARXIV-2607-01646:start -->
#### DeadPool: Resilient LLM Training with Hot-Swapping via Zero-Overhead Checkpoint

<!-- claim:SF-2026-ARXIV-2607-01646:start -->Persistent checkpoint-restart is not the only recovery branch. For frequent fail-stop node loss, the runtime can continuously maintain a committed in-memory recovery generation, replicate only non-reconstructible optimizer shards, and replace a failed node by logical shard identity. This reduces replay and restart scope but depends on spare nodes, failure classification and explicit fallback for corruption or replica loss. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01646:end -->

**旧方案与约束变化。** `本章的核心判断是：**Training Checkpoint 是训练状态在某个逻辑 step 上的一致、可验证、可恢复事务，而不是若干 tensor 文件的集合。**它必须同时描述参数、优化器、随机性、数据进度、并行布局和配置；缺少任一关键状态，都可能让“恢复成功”只剩进程启动成功。`（`books/part-04-training-system/35-checkpoint.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Persistent checkpoint-restart is not the only recovery branch. For frequent fail-stop node loss, the runtime can continuously maintain a committed in-memory recovery generation, replicate only non-reconstructible optimizer shards, and replace a failed node by logical shard identity. This reduces replay and restart scope but depends on spare nodes, failure classification and explicit fallback for corruption or replica loss. 它改变 `TRAIN-CHECKPOINT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01646v1#S5 and https://arxiv.org/html/2607.01646v1#S6 :: per-step ping-pong host snapshots, peer replication of optimizer shards, failure classification, topology repair and logical-shard restoration`；Evaluation：`https://arxiv.org/html/2607.01646v1#S7 :: injected fail-stop/NCCL/storage faults on Perlmutter and Vista, up to 512 A100 or 64 GH200 GPUs and GPT-style models up to 65B; observed overlap and recovery are platform-bound`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01646v1#S5.SS3 and https://arxiv.org/html/2607.01646v1#S8 :: silent corruption/software bugs remain external fallback; redundancy, failure-domain independence, spare capacity, host/network headroom and two-system coverage limit generalization`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`TRAIN-CHECKPOINT`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-01646:end -->

<!-- review:SF-2026-ARXIV-2607-01647:start -->
#### AgenticDataBench: A Comprehensive Benchmark for Data Agents

<!-- claim:SF-2026-ARXIV-2607-01647:start -->Agent evaluation becomes more diagnostic when results are sliced by task skill and trajectory stage, but the measured subject remains model plus harness plus environment plus grader. The evaluation chapter already owns this typed evaluation identity and trajectory-level attribution. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01647:end -->

**旧方案与约束变化。** `An agent score belongs to a versioned evaluation subject composed of model, harness, tools/environment, task slice, trajectory and evaluator; a fluent final answer or aggregate leaderboard cannot erase component failures.`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L754-L776`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Agent evaluation becomes more diagnostic when results are sliced by task skill and trajectory stage, but the measured subject remains model plus harness plus environment plus grader. The evaluation chapter already owns this typed evaluation identity and trajectory-level attribution. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01647v1#S3 through https://arxiv.org/html/2607.01647v1#S5 :: task taxonomy, data-agent harness, trajectory capture and multi-level grading`；Evaluation：`https://arxiv.org/html/2607.01647v1#S6 :: selected agents are evaluated across the released task suite with task/skill slices; rankings remain model-plus-harness results`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01647v1#S5 and https://arxiv.org/html/2607.01647v1#S6 :: the benchmark fixes its task construction, harness and grader/evaluation protocol; no dedicated limitations section is disclosed, so enterprise permission/schema drift and cross-harness validity remain explicit non-proof boundaries rather than author findings`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L687-L700`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-01647:end -->

<!-- review:SF-2026-ARXIV-2607-01658:start -->
#### Teaching Vision-Language-Action Models What to See and Where to Look

<!-- claim:SF-2026-ARXIV-2607-01658:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-01658:end -->

- Identity：`arXiv:2607.01658v1`；first-public（Asia/Shanghai）：`2026-07-02`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-01658:end -->

<!-- review:SF-2026-ARXIV-2607-01678:start -->
#### SCAPE: Accurate and Efficient LLM Training with Extreme Sparse Communication

<!-- claim:SF-2026-ARXIV-2607-01678:start -->Communication reduction can move from quantizing every dense value to transmitting a sparse optimizer-defined support. Reusing a temporally stable first-moment mask one step later exposes synchronization overlap and avoids a second collective, but makes optimizer semantics, residual state, mask freshness and sparse representation part of the training contract. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01678:end -->

**旧方案与约束变化。** `本章的核心判断是：**分布式训练是在保持训练语义不变量的前提下，把计算、模型状态、activation 与通信映射到设备拓扑的约束优化。**每种并行只直接缓解某类瓶颈，并把一部分本地 memory/compute 问题转化成 collective、pipeline、同步或恢复问题。通信也不能被压缩成一个库名：必须分清语义、算法、runtime、transport 与物理拓扑。`（`books/part-04-training-system/36-distributed-training.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Communication reduction can move from quantizing every dense value to transmitting a sparse optimizer-defined support. Reusing a temporally stable first-moment mask one step later exposes synchronization overlap and avoids a second collective, but makes optimizer semantics, residual state, mask freshness and sparse representation part of the training contract. 它改变 `TRAIN-DISTRIBUTED-TRAINING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01678v1#S4 :: optimizer-aware first-moment masks, one-step-delayed refreshed synchronization, sharding-aligned mask ownership and reconstruction from one sparse synchronized buffer`；Evaluation：`https://arxiv.org/html/2607.01678v1#S5 :: GPT-345M/OpenWebText and Llama-500M/SlimPajama full pretraining uses 32 GH200 GPUs; Llama-500M and Llama-1.8B per-step profiling and strong-scaling studies span 4–64 GH200 GPUs, with disclosed sparsity, loss/tasks and timing measurements`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01678v1#S3 and https://arxiv.org/html/2607.01678v1#S4 :: mask stability and delayed reuse are empirical/optimizer-specific; https://arxiv.org/html/2607.01678v1#S5 :: evaluation is limited to the disclosed AdamS models and GH200 setup, while the paper notes PCIe offload may add overhead on other clusters; no dedicated limitations section establishes broader convergence`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-DISTRIBUTED-TRAINING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-01678:end -->

<!-- review:SF-2026-ARXIV-2607-01766:start -->
#### SimWorlds: A Multi-Agent System for Dynamic 3D Scene Creation

<!-- claim:SF-2026-ARXIV-2607-01766:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-01766:end -->

- Identity：`arXiv:2607.01766v1`；first-public（Asia/Shanghai）：`2026-07-02`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-01766:end -->

<!-- review:SF-2026-ARXIV-2607-01804:start -->
#### VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon

<!-- claim:SF-2026-ARXIV-2607-01804:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-01804:end -->

- Identity：`arXiv:2607.01804v1`；first-public（Asia/Shanghai）：`2026-07-02`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-01804:end -->

<!-- review:SF-2026-ARXIV-2607-01831:start -->
#### Lynx: Progressive Speculative Quantization for accelerating KV Transfer in Long-Context Inference

<!-- claim:SF-2026-ARXIV-2607-01831:start -->A PD handoff need not wait for the last exact KV byte before doing any work. A progressive protocol can transmit an approximate low-bit view first, execute speculatively, then verify and correct against later refinements. It converts transfer latency into provisional computation, but requires generation identity, verification authority, rollback/correction and an exact commit frontier. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01831:end -->

**旧方案与约束变化。** `本章的核心判断是：**PD 分离利用 Prefill 与 Decode 在计算、memory、batch 和 SLO 上的差异实现独立资源规划，但必须用 KV transfer、跨池排队和更大故障面支付代价；它是否成立取决于 workload-specific break-even。**`（`books/part-05-inference-system/55-pd-disaggregation.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A PD handoff need not wait for the last exact KV byte before doing any work. A progressive protocol can transmit an approximate low-bit view first, execute speculatively, then verify and correct against later refinements. It converts transfer latency into provisional computation, but requires generation identity, verification authority, rollback/correction and an exact commit frontier. 它改变 `INFER-PD-DISAGGREGATION` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01831v1#S4 :: hierarchical KV quantization, prioritized low-bit-first transfer, speculative execution and verify/correct before exact commitment`；Evaluation：`https://arxiv.org/html/2607.01831v1#S6 :: author tests accuracy and latency on disclosed long-context models/tasks and Ascend-oriented LMCache/vLLM integration; production concurrency and independent replication are absent`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01831v1#S2 :: ordinary complete-transfer and linear-quantization bottlenecks motivate the design; https://arxiv.org/html/2607.01831v1#S4 :: hierarchical approximation plus verification/correction add provisional-state work; https://arxiv.org/html/2607.01831v1#S6 and https://arxiv.org/html/2607.01831v1#S8 :: benefit depends on the evaluated models/hardware and successful transfer/computation overlap. Early bytes not being committed exact state is this review's correctness boundary`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Alternative Branch`。
- Stable owner：`INFER-PD-DISAGGREGATION`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-01831:end -->

<!-- review:SF-2026-ARXIV-2607-01874:start -->
#### SkillCoach: Self-Evolving Rubrics for Evaluating and Enhancing Agentic Skill-Use

<!-- claim:SF-2026-ARXIV-2607-01874:start -->Trajectory rubrics can turn final-outcome supervision into criterion-level diagnosis and filtered training data, but only after deterministic outcomes and evaluator validity are separated from judge interpretation. Existing evaluation ownership already defines that authority boundary. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-01874:end -->

**旧方案与约束变化。** `Deterministic schema, authorization and executable outcome evidence own verifiable verdicts; a rubric-driven judge is restricted to residual semantic ambiguity and must retain the complete trace, evaluator revision, variance and abstention path.`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L754-L776`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Trajectory rubrics can turn final-outcome supervision into criterion-level diagnosis and filtered training data, but only after deterministic outcomes and evaluator validity are separated from judge interpretation. Existing evaluation ownership already defines that authority boundary. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.01874v1#S3 :: skill selection/following/composition/reflection decomposition, self-evolving trajectory rubrics and rubric-filtered offline training`；Evaluation：`https://arxiv.org/html/2607.01874v1#S4 :: rubric quality, agent skill-use and filtered-training ablations on selected libraries/tasks/models; judge and task contracts are pinned to the study`；Limitations/Counterevidence：`https://arxiv.org/html/2607.01874v1#S6 :: rubric induction/judging bias, skill overlap, library/task coverage and offline transfer limit claims; rubrics are not ground truth`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L778-L791`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-01874:end -->

<!-- review:SF-2026-ARXIV-2607-01935:start -->
#### A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory

<!-- claim:SF-2026-ARXIV-2607-01935:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-01935:end -->

- Identity：`arXiv:2607.01935v1`；first-public（Asia/Shanghai）：`2026-07-02`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-01935:end -->

<!-- review:SF-2026-ARXIV-2607-01938:start -->
#### PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation

<!-- claim:SF-2026-ARXIV-2607-01938:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-01938:end -->

- Identity：`arXiv:2607.01938v1`；first-public（Asia/Shanghai）：`2026-07-02`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-01938:end -->

<!-- review:SF-2026-ARXIV-2607-02032:start -->
#### PACE: A Proxy for Agentic Capability Evaluation

<!-- claim:SF-2026-ARXIV-2607-02032:start -->A learned cheap benchmark can prioritize which expensive agent evaluations to run, but its validity is bounded by calibration models, target harness and distribution. The evaluation chapter already treats learned proxies as cost-saving sensors without correctness authority. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-02032:end -->

**旧方案与约束变化。** `A learned proxy may rank or filter candidates before expensive execution, but it must expose calibration identity, distribution validity, cost and abstention; final correctness and high-risk release claims remain with real executable evidence.`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L711-L727`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A learned cheap benchmark can prioritize which expensive agent evaluations to run, but its validity is bounded by calibration models, target harness and distribution. The evaluation chapter already treats learned proxies as cost-saving sensors without correctness authority. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.02032v1#S3 :: calibrated regression plus local/global source-instance selection for a budgeted proxy benchmark`；Evaluation：`https://arxiv.org/html/2607.02032v1#S4 :: leave-one-model-out prediction across 14 models, four target agent benchmarks and 19 source benchmarks with cost/quality sweeps`；Limitations/Counterevidence：`https://arxiv.org/html/2607.02032v1#A6 :: small calibration population, model/task distribution shift, source/target correlation and target-harness dependence prevent proxy scores from replacing final executable evaluation`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L820-L832`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-02032:end -->

<!-- review:SF-2026-ARXIV-2607-02043:start -->
#### Towards Load-Aware Prefill Deflection for Disaggregated LLM Serving

<!-- claim:SF-2026-ARXIV-2607-02043:start -->Static PD role boundaries can waste decode headroom while prefill queues violate TTFT. A controller may deflect chunked prefill onto decode workers only when a calibrated per-step model proves remaining TBT slack, with safety margin and fallback. This improves temporary capacity matching but couples estimation error, stale state and fairness to both SLOs. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-02043:end -->

**旧方案与约束变化。** `本章的核心判断是：**PD 分离利用 Prefill 与 Decode 在计算、memory、batch 和 SLO 上的差异实现独立资源规划，但必须用 KV transfer、跨池排队和更大故障面支付代价；它是否成立取决于 workload-specific break-even。**`（`books/part-05-inference-system/55-pd-disaggregation.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Static PD role boundaries can waste decode headroom while prefill queues violate TTFT. A controller may deflect chunked prefill onto decode workers only when a calibrated per-step model proves remaining TBT slack, with safety margin and fallback. This improves temporary capacity matching but couples estimation error, stale state and fairness to both SLOs. 它改变 `INFER-PD-DISAGGREGATION` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.02043v1#S4 :: TTFT estimator, decode-step feasibility model and greedy chunk schedule that borrows only predicted TBT slack`；Evaluation：`https://arxiv.org/html/2607.02043v1#S6 :: vLLM 0.18.1 implementation on A100 clusters with DeepSeek-v2-Lite, bursty traces and stated P95 TTFT/TBT SLOs; results are workload-specific`；Limitations/Counterevidence：`https://arxiv.org/html/2607.02043v1#S7 :: central dispatcher, stale 100-ms observations, estimator error, no migration and omitted prefix-cache interactions constrain deployment`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-PD-DISAGGREGATION`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-02043:end -->

<!-- review:SF-2026-ARXIV-2607-02045:start -->
#### PWM-ArtGen: Part World Model for Articulated Object Generation

<!-- claim:SF-2026-ARXIV-2607-02045:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02045:end -->

- Identity：`arXiv:2607.02045v1`；first-public（Asia/Shanghai）：`2026-07-02`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02045:end -->

<!-- review:SF-2026-ARXIV-2607-02092:start -->
#### Guided Action Flow: Q-Guided Inference for Flow-Matching Vision-Language-Action Policies

<!-- claim:SF-2026-ARXIV-2607-02092:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02092:end -->

- Identity：`arXiv:2607.02092v1`；first-public（Asia/Shanghai）：`2026-07-02`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02092:end -->

<!-- review:SF-2026-ARXIV-2607-02182:start -->
#### Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation

<!-- claim:SF-2026-ARXIV-2607-02182:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02182:end -->

- Identity：`arXiv:2607.02182v1`；first-public（Asia/Shanghai）：`2026-07-02`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02182:end -->

<!-- review:SF-2026-ARXIV-2607-02255:start -->
#### AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents

<!-- claim:SF-2026-ARXIV-2607-02255:start -->Long-horizon memory is more auditable when runtime visibility, write authority and archive fallback are typed rather than left to ad-hoc transcript accumulation. This mechanism is already integrated in the Memory chapter with the same small-sample and harness boundaries. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-02255:end -->

**旧方案与约束变化。** `Memory visibility is a fixed typed protocol: current state, retrieved rules, episodic summaries, validated skills and immutable archive have distinct budgets and writers, with fallback to raw evidence when retrieval or summaries fail.`（`books/part-07-agent/77-memory.md#L660-L679`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Long-horizon memory is more auditable when runtime visibility, write authority and archive fallback are typed rather than left to ad-hoc transcript accumulation. This mechanism is already integrated in the Memory chapter with the same small-sample and harness boundaries. 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.02255v1#S4 and https://arxiv.org/html/2607.02255v1#S5 :: five typed visibility layers, per-decision composition, bounded episodic memory and fixed-harness ablations`；Evaluation：`https://arxiv.org/html/2607.02255v1#S6 :: small-sample within-harness and cross-backbone trials with statistical appendix; observed differences are not universal rankings`；Limitations/Counterevidence：`https://arxiv.org/html/2607.02255v1#S9 :: small cells, one game/character/version, unmatched accumulating-context agents and architectural scope limit generalization`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L933-L958`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-02255:end -->

<!-- review:SF-2026-ARXIV-2607-02322:start -->
#### The Moving Eye: Enhancing VLA Spatial Generalization via Hybrid Dynamic Data Collection

<!-- claim:SF-2026-ARXIV-2607-02322:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02322:end -->

- Identity：`arXiv:2607.02322v1`；first-public（Asia/Shanghai）：`2026-07-02`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02322:end -->

<!-- review:SF-2026-ARXIV-2607-02440:start -->
#### EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments

<!-- claim:SF-2026-ARXIV-2607-02440:start -->Iterative agent-policy evaluation must version the environment, policy, feedback visibility and held-out boundary; local wins and post-hoc trajectories do not establish suite-wide reliability or causal credit. The evaluation chapter already owns these evidence limits. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-02440:end -->

**旧方案与约束变化。** `Evaluation evidence is valid only for a pinned subject, environment, evaluator and slice; iterative improvement must preserve held-out promotion boundaries and cannot infer causal credit from a convenient process score or local win.`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L724-L752`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Iterative agent-policy evaluation must version the environment, policy, feedback visibility and held-out boundary; local wins and post-hoc trajectories do not establish suite-wide reliability or causal credit. The evaluation chapter already owns these evidence limits. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.02440v1#S3 :: bounded environment-policy episodes, autonomous policy revision and explicit feedback/evaluation boundaries`；Evaluation：`https://arxiv.org/html/2607.02440v1#S4 and https://arxiv.org/html/2607.02440v1#S5 :: task-suite outcomes, post-hoc score trajectories and mechanism case studies under a fixed run protocol`；Limitations/Counterevidence：`https://arxiv.org/html/2607.02440v1#S5.SS3 :: diagnostics are post-hoc, task-family dependent and do not establish causal credit or open-ended safe self-improvement`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L673-L686`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-02440:end -->

<!-- review:SF-2026-ARXIV-2607-02512:start -->
#### Program-as-Weights: A Programming Paradigm for Fuzzy Functions

<!-- claim:SF-2026-ARXIV-2607-02512:start -->Repeated interpretation of a stable fuzzy specification can be moved off the request path into a versioned neural artifact, but the artifact remains behaviorally evaluated rather than code-equivalent. This branch and its identity/rollback contract are already integrated in the LoRA chapter. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-02512:end -->

**旧方案与约束变化。** `A natural-language specification may be compiled into a versioned adapter or prefix artifact only with a pinned compiler/interpreter/base, behavioral signature, promotion and revoke/recompile path; explicit programs remain preferable for high-risk deterministic rules.`（`books/part-04-training-system/30-lora.md#L291-L312`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Repeated interpretation of a stable fuzzy specification can be moved off the request path into a versioned neural artifact, but the artifact remains behaviorally evaluated rather than code-equivalent. This branch and its identity/rollback contract are already integrated in the LoRA chapter. 它改变 `TRAIN-LORA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.02512v1#S2 and https://arxiv.org/html/2607.02512v1#S3 :: compiler converts a natural-language specification into a pseudo-program and adapter/prefix artifact consumed by a pinned interpreter`；Evaluation：`https://arxiv.org/html/2607.02512v1#S4 through https://arxiv.org/html/2607.02512v1#S10 :: FuzzyBench training, main results, ablations, noisy-specification robustness, local execution and quantization studies`；Limitations/Counterevidence：`https://arxiv.org/html/2607.02512v1#A14 :: compiler/interpreter dependence, fuzzy-task coverage, behavioral inspection, specification drift and lack of deterministic equivalence bound the claim`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L411-L463`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`TRAIN-LORA`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-02512:end -->

<!-- review:SF-2026-ARXIV-2607-02517:start -->
#### WorldDirector: Building Controllable World Simulators with Persistent Dynamic Memory

<!-- claim:SF-2026-ARXIV-2607-02517:start -->Separating planned object state, appearance identity and chunk-local synthesis helps an object leave and re-enter view without relying on implicit video context alone. The World Model chapter already owns persistent revisable state, identity, chunk drift and the boundary between visual consistency and causal/closed-loop correctness. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-02517:end -->

**旧方案与约束变化。** `Persistent world state must preserve identity and mutation across revisit while remaining versioned, revisable and recoverable; visually consistent generation is lower-layer evidence and cannot substitute for action-conditioned or closed-loop correctness.`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L286-L320`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Separating planned object state, appearance identity and chunk-local synthesis helps an object leave and re-enter view without relying on implicit video context alone. The World Model chapter already owns persistent revisable state, identity, chunk drift and the boundary between visual consistency and causal/closed-loop correctness. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.02517v1#S3 :: trajectory planning, spatial/appearance conditioning, persistent dynamic context memory and causal chunk generation`；Evaluation：`https://arxiv.org/html/2607.02517v1#S4 :: author comparisons and ablations test identity/location persistence and promptable events in selected generated-video scenarios`；Limitations/Counterevidence：`https://arxiv.org/html/2607.02517v1#S4 and https://arxiv.org/html/2607.02517v1#S5 :: evaluation and conclusion are limited to selected synthetic/game video scenarios and acknowledge the domain gap; causal physics, unbounded horizon, closed-loop controllability and safe real-world action are explicit non-proof boundaries, while planner/projection, identity collision and chunk drift remain inferred system risks`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L701-L715`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-02517:end -->

<!-- review:SF-2026-ARXIV-2607-02686:start -->
#### ASK in the Dark: Uncertainty-Gated LLM Assistance under Partial Observability

<!-- claim:SF-2026-ARXIV-2607-02686:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02686:end -->

- Identity：`arXiv:2607.02686v1`；first-public（Asia/Shanghai）：`2026-07-03`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02686:end -->

<!-- review:SF-2026-ARXIV-2607-02840:start -->
#### TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training

<!-- claim:SF-2026-ARXIV-2607-02840:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02840:end -->

- Identity：`arXiv:2607.02840v1`；first-public（Asia/Shanghai）：`2026-07-03`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02840:end -->

## 4. Benchmark Contracts

本日报不转述性能 headline，`Benchmark Claim` 均为 `no`。论文实验只用于限定机制证据，不把不同模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 拼成跨论文排名。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-01617 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“When PD KV transfer and decode collectives share a fabric, software scheduling cannot eliminate head-of-line interference.”；V2=3/3/2。与同 owner 入选 `SF-2026-ARXIV-2607-02043` 相比，本项没有更高的 Design Delta / System Reach / Durability。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-01617 |
| SF-2026-ARXIV-2607-01646 | score_7_9;potential_books_delta | selected | DA-20260703-2607-01646 | — | V2=9/9；Persistent checkpoint-restart is not the only recovery branch. For frequent fail-stop node loss, the runtime can continuously maintain a committed in-memory recovery generation, replicate only non-reconstructible optimizer shards, and replace a failed node by logical shard identity. This reduces replay and restart scope but depends on spare nodes, failure classification and explicit fallback for corruption or replica loss.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260703-2607-01646 |
| SF-2026-ARXIV-2607-01678 | score_7_9;potential_books_delta | selected | DA-20260703-2607-01678 | — | V2=8/9；Communication reduction can move from quantizing every dense value to transmitting a sparse optimizer-defined support. Reusing a temporally stable first-moment mask one step later exposes synchronization overlap and avoids a second collective, but makes optimizer semantics, residual state, mask freshness and sparse representation part of the training contract.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260703-2607-01678 |
| SF-2026-ARXIV-2607-01831 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“A PD handoff need not wait for the last exact KV byte before doing any work.”；V2=3/3/2。与同 owner 入选 `SF-2026-ARXIV-2607-02043` 相比，本项没有更高的 Design Delta / System Reach / Durability。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-01831 |
| SF-2026-ARXIV-2607-01874 | score_7_9 | not_selected | — | — | 本 family 的独立增量为“Trajectory rubrics can turn final-outcome supervision into criterion-level diagnosis and filtered training data, but only after deterministic outcomes and evaluator validity are separated from judge interpretation.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-01678` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-01874 |
| SF-2026-ARXIV-2607-02043 | score_7_9;potential_books_delta | selected | DA-20260703-2607-02043 | — | V2=9/9；Static PD role boundaries can waste decode headroom while prefill queues violate TTFT. A controller may deflect chunked prefill onto decode workers only when a calibrated per-step model proves remaining TBT slack, with safety margin and fallback. This improves temporary capacity matching but couples estimation error, stale state and fairness to both SLOs.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260703-2607-02043 |
| SF-2026-ARXIV-2607-02255 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“Long-horizon memory is more auditable when runtime visibility, write authority and archive fallback are typed rather than left to ad-hoc transcript accumulation.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-01678` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-02255 |
| SF-2026-ARXIV-2607-02440 | score_7_9 | not_selected | — | — | 本 family 的独立增量为“Iterative agent-policy evaluation must version the environment, policy, feedback visibility and held-out boundary; local wins and post-hoc trajectories do not establish suite-wide reliability or causal credit.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-01678` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-02440 |
| SF-2026-ARXIV-2607-02512 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“Repeated interpretation of a stable fuzzy specification can be moved off the request path into a versioned neural artifact, but the artifact remains behaviorally evaluated rather than code-equivalent.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-01678` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-02512 |
| SF-2026-ARXIV-2607-02517 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“Separating planned object state, appearance identity and chunk-local synthesis helps an object leave and re-enter view without relying on implicit video context alone.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-01678` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-02517 |

<!-- analysis:DA-20260703-2607-02043:start -->
### Towards Load-Aware Prefill Deflection for Disaggregated LLM Serving

**旧方案为何合理。** 本章的核心判断是：**PD 分离利用 Prefill 与 Decode 在计算、memory、batch 和 SLO 上的差异实现独立资源规划，但必须用 KV transfer、跨池排队和更大故障面支付代价；它是否成立取决于 workload-specific break-even。** 当状态局部、规模较小、workload 稳定或 SLO 宽松时，这一基线仍然成立。（现有命题定位：`books/part-05-inference-system/55-pd-disaggregation.md#L14-L14`）

**约束变化与机制。** Static PD role boundaries can waste decode headroom while prefill queues violate TTFT. A controller may deflect chunked prefill onto decode workers only when a calibrated per-step model proves remaining TBT slack, with safety margin and fallback. This improves temporary capacity matching but couples estimation error, stale state and fairness to both SLOs. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-PD-DISAGGREGATION` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** 新机制以额外 metadata、选择/压缩误差、计算或恢复责任换取作者 workload 内的收益；未披露的 model、hardware、precision、length、batch、concurrency、SLO 与 evaluator 不做补推。旧方案仍在新增成本高于收益时成立，下一步需要跨 workload、故障与长期状态的独立验证。

<!-- analysis:DA-20260703-2607-02043:end -->

<!-- analysis:DA-20260703-2607-01646:start -->
### DeadPool: Resilient LLM Training with Hot-Swapping via Zero-Overhead Checkpoint

**旧方案为何合理。** 本章的核心判断是：**Training Checkpoint 是训练状态在某个逻辑 step 上的一致、可验证、可恢复事务，而不是若干 tensor 文件的集合。**它必须同时描述参数、优化器、随机性、数据进度、并行布局和配置；缺少任一关键状态，都可能让“恢复成功”只剩进程启动成功。 当状态局部、规模较小、workload 稳定或 SLO 宽松时，这一基线仍然成立。（现有命题定位：`books/part-04-training-system/35-checkpoint.md#L14-L14`）

**约束变化与机制。** Persistent checkpoint-restart is not the only recovery branch. For frequent fail-stop node loss, the runtime can continuously maintain a committed in-memory recovery generation, replicate only non-reconstructible optimizer shards, and replace a failed node by logical shard identity. This reduces replay and restart scope but depends on spare nodes, failure classification and explicit fallback for corruption or replica loss. 这条证据与现有主线的关系是 `Layering / Dependency`：它改变或补充 `TRAIN-CHECKPOINT` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** 新机制以额外 metadata、选择/压缩误差、计算或恢复责任换取作者 workload 内的收益；未披露的 model、hardware、precision、length、batch、concurrency、SLO 与 evaluator 不做补推。旧方案仍在新增成本高于收益时成立，下一步需要跨 workload、故障与长期状态的独立验证。

<!-- analysis:DA-20260703-2607-01646:end -->

<!-- analysis:DA-20260703-2607-01678:start -->
### SCAPE: Accurate and Efficient LLM Training with Extreme Sparse Communication

**旧方案为何合理。** 本章的核心判断是：**分布式训练是在保持训练语义不变量的前提下，把计算、模型状态、activation 与通信映射到设备拓扑的约束优化。**每种并行只直接缓解某类瓶颈，并把一部分本地 memory/compute 问题转化成 collective、pipeline、同步或恢复问题。通信也不能被压缩成一个库名：必须分清语义、算法、runtime、transport 与物理拓扑。 当状态局部、规模较小、workload 稳定或 SLO 宽松时，这一基线仍然成立。（现有命题定位：`books/part-04-training-system/36-distributed-training.md#L14-L14`）

**约束变化与机制。** Communication reduction can move from quantizing every dense value to transmitting a sparse optimizer-defined support. Reusing a temporally stable first-moment mask one step later exposes synchronization overlap and avoids a second collective, but makes optimizer semantics, residual state, mask freshness and sparse representation part of the training contract. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `TRAIN-DISTRIBUTED-TRAINING` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** 新机制以额外 metadata、选择/压缩误差、计算或恢复责任换取作者 workload 内的收益；未披露的 model、hardware、precision、length、batch、concurrency、SLO 与 evaluator 不做补推。旧方案仍在新增成本高于收益时成立，下一步需要跨 workload、故障与长期状态的独立验证。

<!-- analysis:DA-20260703-2607-01678:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-01617:start -->《3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving》已完成 Deep Source Review。本 family 的独立增量为“When PD KV transfer and decode collectives share a fabric, software scheduling cannot eliminate head-of-line interference.”；V2=3/3/2。与同 owner 入选 `SF-2026-ARXIV-2607-02043` 相比，本项没有更高的 Design Delta / System Reach / Durability。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-01617:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-01831:start -->《Lynx: Progressive Speculative Quantization for accelerating KV Transfer in Long-Context Inference》已完成 Deep Source Review。本 family 的独立增量为“A PD handoff need not wait for the last exact KV byte before doing any work.”；V2=3/3/2。与同 owner 入选 `SF-2026-ARXIV-2607-02043` 相比，本项没有更高的 Design Delta / System Reach / Durability。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-01831:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-01874:start -->《SkillCoach: Self-Evolving Rubrics for Evaluating and Enhancing Agentic Skill-Use》已完成 Deep Source Review。本 family 的独立增量为“Trajectory rubrics can turn final-outcome supervision into criterion-level diagnosis and filtered training data, but only after deterministic outcomes and evaluator validity are separated from judge interpretation.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-01678` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-01874:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-02255:start -->《AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents》已完成 Deep Source Review。本 family 的独立增量为“Long-horizon memory is more auditable when runtime visibility, write authority and archive fallback are typed rather than left to ad-hoc transcript accumulation.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-01678` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-02255:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-02440:start -->《EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments》已完成 Deep Source Review。本 family 的独立增量为“Iterative agent-policy evaluation must version the environment, policy, feedback visibility and held-out boundary; local wins and post-hoc trajectories do not establish suite-wide reliability or causal credit.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-01678` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-02440:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-02512:start -->《Program-as-Weights: A Programming Paradigm for Fuzzy Functions》已完成 Deep Source Review。本 family 的独立增量为“Repeated interpretation of a stable fuzzy specification can be moved off the request path into a versioned neural artifact, but the artifact remains behaviorally evaluated rather than code-equivalent.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-01678` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-02512:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-02517:start -->《WorldDirector: Building Controllable World Simulators with Persistent Dynamic Memory》已完成 Deep Source Review。本 family 的独立增量为“Separating planned object state, appearance identity and chunk-local synthesis helps an object leave and re-enter view without relying on implicit video context alone.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-01678` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-02517:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-01579 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L248-L301 | books/part-05-inference-system/55-pd-disaggregation.md#L14-L14; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L14-L14 | existing:SF-2026-ARXIV-2607-01579 | delta:SF-2026-ARXIV-2607-01579 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-01579 |
| SF-2026-ARXIV-2607-01617 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#L97 | books/part-05-inference-system/54-gpu-memory.md#L14-L14; books/part-05-inference-system/56-inference-scheduling.md#L14-L14 | existing:SF-2026-ARXIV-2607-01617 | delta:SF-2026-ARXIV-2607-01617 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2607-01617 |
| SF-2026-ARXIV-2607-01646 | TRAIN-CHECKPOINT | books/part-04-training-system/35-checkpoint.md#L273 | books/part-04-training-system/34-dpo.md#L14-L14; books/part-04-training-system/36-distributed-training.md#L14-L14 | existing:SF-2026-ARXIV-2607-01646 | delta:SF-2026-ARXIV-2607-01646 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2607-01646 |
| SF-2026-ARXIV-2607-01647 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L754-L776 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-01647 | delta:SF-2026-ARXIV-2607-01647 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-01647 |
| SF-2026-ARXIV-2607-01678 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L448 | books/part-04-training-system/35-checkpoint.md#L14-L14; books/part-04-training-system/37-tensor-parallel.md#L14-L14 | existing:SF-2026-ARXIV-2607-01678 | delta:SF-2026-ARXIV-2607-01678 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-01678 |
| SF-2026-ARXIV-2607-01831 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#L112 | books/part-05-inference-system/54-gpu-memory.md#L14-L14; books/part-05-inference-system/56-inference-scheduling.md#L14-L14 | existing:SF-2026-ARXIV-2607-01831 | delta:SF-2026-ARXIV-2607-01831 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2607-01831 |
| SF-2026-ARXIV-2607-01874 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L754-L776 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-01874 | delta:SF-2026-ARXIV-2607-01874 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-01874 |
| SF-2026-ARXIV-2607-02032 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L711-L727 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-02032 | delta:SF-2026-ARXIV-2607-02032 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-02032 |
| SF-2026-ARXIV-2607-02043 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#L250 | books/part-05-inference-system/54-gpu-memory.md#L14-L14; books/part-05-inference-system/56-inference-scheduling.md#L14-L14 | existing:SF-2026-ARXIV-2607-02043 | delta:SF-2026-ARXIV-2607-02043 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-02043 |
| SF-2026-ARXIV-2607-02255 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L660-L679 | books/part-07-agent/76-rag.md#L14-L14; books/part-07-agent/78-tool-calling.md#L14-L14 | existing:SF-2026-ARXIV-2607-02255 | delta:SF-2026-ARXIV-2607-02255 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-02255 |
| SF-2026-ARXIV-2607-02440 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L724-L752 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-02440 | delta:SF-2026-ARXIV-2607-02440 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-02440 |
| SF-2026-ARXIV-2607-02512 | TRAIN-LORA | books/part-04-training-system/30-lora.md#L291-L312 | books/part-04-training-system/29-sft.md#L14-L14; books/part-04-training-system/31-rlhf.md#L14-L14 | existing:SF-2026-ARXIV-2607-02512 | delta:SF-2026-ARXIV-2607-02512 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-02512 |
| SF-2026-ARXIV-2607-02517 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L286-L320 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-02517 | delta:SF-2026-ARXIV-2607-02517 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-02517 |

<!-- books-review:SF-2026-ARXIV-2607-01579:start --><!-- existing:SF-2026-ARXIV-2607-01579:start -->对读 `books/part-05-inference-system/56-inference-scheduling.md#L248-L301` 与相邻章节后，现有命题（`books/part-05-inference-system/56-inference-scheduling.md#L248-L301`）为：Configuration search uses versioned primitive measurements and uncertainty-aware prediction only to narrow candidates; launch authority remains with targeted silicon validation, canary and rollback when calibration drifts or candidates are near-tied.<!-- existing:SF-2026-ARXIV-2607-01579:end --><!-- delta:SF-2026-ARXIV-2607-01579:start -->新增证据边界：A configuration predictor should be admitted only when its expected decision value exceeds benchmark cost and should abstain outside calibrated cells. The scheduling chapter already makes calibration identity, uncertainty, targeted silicon validation and rollback explicit, so this family strengthens that route without changing its owner. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-01579:end --><!-- books-review:SF-2026-ARXIV-2607-01579:end -->

<!-- books-review:SF-2026-ARXIV-2607-01617:start --><!-- existing:SF-2026-ARXIV-2607-01617:start -->对读 `books/part-05-inference-system/55-pd-disaggregation.md#L97` 与相邻章节后，现有命题（`books/part-05-inference-system/55-pd-disaggregation.md#L14-L14`）为：本章的核心判断是：**PD 分离利用 Prefill 与 Decode 在计算、memory、batch 和 SLO 上的差异实现独立资源规划，但必须用 KV transfer、跨池排队和更大故障面支付代价；它是否成立取决于 workload-specific break-even。**<!-- existing:SF-2026-ARXIV-2607-01617:end --><!-- delta:SF-2026-ARXIV-2607-01617:start -->新增证据边界：When PD KV transfer and decode collectives share a fabric, software scheduling cannot eliminate head-of-line interference. Mapping the two traffic classes to physically distinct link domains can protect the handoff critical path, but it spends packaging area, thermal/yield budget and topology flexibility; it remains an architecture-specific branch rather than a default PD requirement. 该 delta 已进入 `books/part-05-inference-system/55-pd-disaggregation.md#L97`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-01617:end --><!-- books-review:SF-2026-ARXIV-2607-01617:end -->

<!-- books-review:SF-2026-ARXIV-2607-01646:start --><!-- existing:SF-2026-ARXIV-2607-01646:start -->对读 `books/part-04-training-system/35-checkpoint.md#L273` 与相邻章节后，现有命题（`books/part-04-training-system/35-checkpoint.md#L14-L14`）为：本章的核心判断是：**Training Checkpoint 是训练状态在某个逻辑 step 上的一致、可验证、可恢复事务，而不是若干 tensor 文件的集合。**它必须同时描述参数、优化器、随机性、数据进度、并行布局和配置；缺少任一关键状态，都可能让“恢复成功”只剩进程启动成功。<!-- existing:SF-2026-ARXIV-2607-01646:end --><!-- delta:SF-2026-ARXIV-2607-01646:start -->新增证据边界：Persistent checkpoint-restart is not the only recovery branch. For frequent fail-stop node loss, the runtime can continuously maintain a committed in-memory recovery generation, replicate only non-reconstructible optimizer shards, and replace a failed node by logical shard identity. This reduces replay and restart scope but depends on spare nodes, failure classification and explicit fallback for corruption or replica loss. 该 delta 已进入 `books/part-04-training-system/35-checkpoint.md#L273`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-01646:end --><!-- books-review:SF-2026-ARXIV-2607-01646:end -->

<!-- books-review:SF-2026-ARXIV-2607-01647:start --><!-- existing:SF-2026-ARXIV-2607-01647:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L754-L776` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L754-L776`）为：An agent score belongs to a versioned evaluation subject composed of model, harness, tools/environment, task slice, trajectory and evaluator; a fluent final answer or aggregate leaderboard cannot erase component failures.<!-- existing:SF-2026-ARXIV-2607-01647:end --><!-- delta:SF-2026-ARXIV-2607-01647:start -->新增证据边界：Agent evaluation becomes more diagnostic when results are sliced by task skill and trajectory stage, but the measured subject remains model plus harness plus environment plus grader. The evaluation chapter already owns this typed evaluation identity and trajectory-level attribution. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-01647:end --><!-- books-review:SF-2026-ARXIV-2607-01647:end -->

<!-- books-review:SF-2026-ARXIV-2607-01678:start --><!-- existing:SF-2026-ARXIV-2607-01678:start -->对读 `books/part-04-training-system/36-distributed-training.md#L448` 与相邻章节后，现有命题（`books/part-04-training-system/36-distributed-training.md#L14-L14`）为：本章的核心判断是：**分布式训练是在保持训练语义不变量的前提下，把计算、模型状态、activation 与通信映射到设备拓扑的约束优化。**每种并行只直接缓解某类瓶颈，并把一部分本地 memory/compute 问题转化成 collective、pipeline、同步或恢复问题。通信也不能被压缩成一个库名：必须分清语义、算法、runtime、transport 与物理拓扑。<!-- existing:SF-2026-ARXIV-2607-01678:end --><!-- delta:SF-2026-ARXIV-2607-01678:start -->新增证据边界：Communication reduction can move from quantizing every dense value to transmitting a sparse optimizer-defined support. Reusing a temporally stable first-moment mask one step later exposes synchronization overlap and avoids a second collective, but makes optimizer semantics, residual state, mask freshness and sparse representation part of the training contract. 该 delta 已进入 `books/part-04-training-system/36-distributed-training.md#L448`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-01678:end --><!-- books-review:SF-2026-ARXIV-2607-01678:end -->

<!-- books-review:SF-2026-ARXIV-2607-01831:start --><!-- existing:SF-2026-ARXIV-2607-01831:start -->对读 `books/part-05-inference-system/55-pd-disaggregation.md#L112` 与相邻章节后，现有命题（`books/part-05-inference-system/55-pd-disaggregation.md#L14-L14`）为：本章的核心判断是：**PD 分离利用 Prefill 与 Decode 在计算、memory、batch 和 SLO 上的差异实现独立资源规划，但必须用 KV transfer、跨池排队和更大故障面支付代价；它是否成立取决于 workload-specific break-even。**<!-- existing:SF-2026-ARXIV-2607-01831:end --><!-- delta:SF-2026-ARXIV-2607-01831:start -->新增证据边界：A PD handoff need not wait for the last exact KV byte before doing any work. A progressive protocol can transmit an approximate low-bit view first, execute speculatively, then verify and correct against later refinements. It converts transfer latency into provisional computation, but requires generation identity, verification authority, rollback/correction and an exact commit frontier. 该 delta 已进入 `books/part-05-inference-system/55-pd-disaggregation.md#L112`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-01831:end --><!-- books-review:SF-2026-ARXIV-2607-01831:end -->

<!-- books-review:SF-2026-ARXIV-2607-01874:start --><!-- existing:SF-2026-ARXIV-2607-01874:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L754-L776` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L754-L776`）为：Deterministic schema, authorization and executable outcome evidence own verifiable verdicts; a rubric-driven judge is restricted to residual semantic ambiguity and must retain the complete trace, evaluator revision, variance and abstention path.<!-- existing:SF-2026-ARXIV-2607-01874:end --><!-- delta:SF-2026-ARXIV-2607-01874:start -->新增证据边界：Trajectory rubrics can turn final-outcome supervision into criterion-level diagnosis and filtered training data, but only after deterministic outcomes and evaluator validity are separated from judge interpretation. Existing evaluation ownership already defines that authority boundary. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-01874:end --><!-- books-review:SF-2026-ARXIV-2607-01874:end -->

<!-- books-review:SF-2026-ARXIV-2607-02032:start --><!-- existing:SF-2026-ARXIV-2607-02032:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L711-L727` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L711-L727`）为：A learned proxy may rank or filter candidates before expensive execution, but it must expose calibration identity, distribution validity, cost and abstention; final correctness and high-risk release claims remain with real executable evidence.<!-- existing:SF-2026-ARXIV-2607-02032:end --><!-- delta:SF-2026-ARXIV-2607-02032:start -->新增证据边界：A learned cheap benchmark can prioritize which expensive agent evaluations to run, but its validity is bounded by calibration models, target harness and distribution. The evaluation chapter already treats learned proxies as cost-saving sensors without correctness authority. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-02032:end --><!-- books-review:SF-2026-ARXIV-2607-02032:end -->

<!-- books-review:SF-2026-ARXIV-2607-02043:start --><!-- existing:SF-2026-ARXIV-2607-02043:start -->对读 `books/part-05-inference-system/55-pd-disaggregation.md#L250` 与相邻章节后，现有命题（`books/part-05-inference-system/55-pd-disaggregation.md#L14-L14`）为：本章的核心判断是：**PD 分离利用 Prefill 与 Decode 在计算、memory、batch 和 SLO 上的差异实现独立资源规划，但必须用 KV transfer、跨池排队和更大故障面支付代价；它是否成立取决于 workload-specific break-even。**<!-- existing:SF-2026-ARXIV-2607-02043:end --><!-- delta:SF-2026-ARXIV-2607-02043:start -->新增证据边界：Static PD role boundaries can waste decode headroom while prefill queues violate TTFT. A controller may deflect chunked prefill onto decode workers only when a calibrated per-step model proves remaining TBT slack, with safety margin and fallback. This improves temporary capacity matching but couples estimation error, stale state and fairness to both SLOs. 该 delta 已进入 `books/part-05-inference-system/55-pd-disaggregation.md#L250`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-02043:end --><!-- books-review:SF-2026-ARXIV-2607-02043:end -->

<!-- books-review:SF-2026-ARXIV-2607-02255:start --><!-- existing:SF-2026-ARXIV-2607-02255:start -->对读 `books/part-07-agent/77-memory.md#L660-L679` 与相邻章节后，现有命题（`books/part-07-agent/77-memory.md#L660-L679`）为：Memory visibility is a fixed typed protocol: current state, retrieved rules, episodic summaries, validated skills and immutable archive have distinct budgets and writers, with fallback to raw evidence when retrieval or summaries fail.<!-- existing:SF-2026-ARXIV-2607-02255:end --><!-- delta:SF-2026-ARXIV-2607-02255:start -->新增证据边界：Long-horizon memory is more auditable when runtime visibility, write authority and archive fallback are typed rather than left to ad-hoc transcript accumulation. This mechanism is already integrated in the Memory chapter with the same small-sample and harness boundaries. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-02255:end --><!-- books-review:SF-2026-ARXIV-2607-02255:end -->

<!-- books-review:SF-2026-ARXIV-2607-02440:start --><!-- existing:SF-2026-ARXIV-2607-02440:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L724-L752` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L724-L752`）为：Evaluation evidence is valid only for a pinned subject, environment, evaluator and slice; iterative improvement must preserve held-out promotion boundaries and cannot infer causal credit from a convenient process score or local win.<!-- existing:SF-2026-ARXIV-2607-02440:end --><!-- delta:SF-2026-ARXIV-2607-02440:start -->新增证据边界：Iterative agent-policy evaluation must version the environment, policy, feedback visibility and held-out boundary; local wins and post-hoc trajectories do not establish suite-wide reliability or causal credit. The evaluation chapter already owns these evidence limits. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-02440:end --><!-- books-review:SF-2026-ARXIV-2607-02440:end -->

<!-- books-review:SF-2026-ARXIV-2607-02512:start --><!-- existing:SF-2026-ARXIV-2607-02512:start -->对读 `books/part-04-training-system/30-lora.md#L291-L312` 与相邻章节后，现有命题（`books/part-04-training-system/30-lora.md#L291-L312`）为：A natural-language specification may be compiled into a versioned adapter or prefix artifact only with a pinned compiler/interpreter/base, behavioral signature, promotion and revoke/recompile path; explicit programs remain preferable for high-risk deterministic rules.<!-- existing:SF-2026-ARXIV-2607-02512:end --><!-- delta:SF-2026-ARXIV-2607-02512:start -->新增证据边界：Repeated interpretation of a stable fuzzy specification can be moved off the request path into a versioned neural artifact, but the artifact remains behaviorally evaluated rather than code-equivalent. This branch and its identity/rollback contract are already integrated in the LoRA chapter. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-02512:end --><!-- books-review:SF-2026-ARXIV-2607-02512:end -->

<!-- books-review:SF-2026-ARXIV-2607-02517:start --><!-- existing:SF-2026-ARXIV-2607-02517:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L286-L320` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L286-L320`）为：Persistent world state must preserve identity and mutation across revisit while remaining versioned, revisable and recoverable; visually consistent generation is lower-layer evidence and cannot substitute for action-conditioned or closed-loop correctness.<!-- existing:SF-2026-ARXIV-2607-02517:end --><!-- delta:SF-2026-ARXIV-2607-02517:start -->新增证据边界：Separating planned object state, appearance identity and chunk-local synthesis helps an object leave and re-enter view without relying on implicit video context alone. The World Model chapter already owns persistent revisable state, identity, chunk drift and the boundary between visual consistency and causal/closed-loop correctness. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-02517:end --><!-- books-review:SF-2026-ARXIV-2607-02517:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260703-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260703; semantic-review:SA-20260703-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260703-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-01579; review:SF-2026-ARXIV-2607-01586; review:SF-2026-ARXIV-2607-01595; review:SF-2026-ARXIV-2607-01617; review:SF-2026-ARXIV-2607-01646; review:SF-2026-ARXIV-2607-01647; review:SF-2026-ARXIV-2607-01658; review:SF-2026-ARXIV-2607-01678; review:SF-2026-ARXIV-2607-01766; review:SF-2026-ARXIV-2607-01804; review:SF-2026-ARXIV-2607-01831; review:SF-2026-ARXIV-2607-01874; review:SF-2026-ARXIV-2607-01935; review:SF-2026-ARXIV-2607-01938; review:SF-2026-ARXIV-2607-02032; review:SF-2026-ARXIV-2607-02043; review:SF-2026-ARXIV-2607-02045; review:SF-2026-ARXIV-2607-02092; review:SF-2026-ARXIV-2607-02182; review:SF-2026-ARXIV-2607-02255; review:SF-2026-ARXIV-2607-02322; review:SF-2026-ARXIV-2607-02440; review:SF-2026-ARXIV-2607-02512; review:SF-2026-ARXIV-2607-02517; review:SF-2026-ARXIV-2607-02686; review:SF-2026-ARXIV-2607-02840; semantic-review:SA-20260703-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260703-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260703-2607-02043; analysis:DA-20260703-2607-01646; analysis:DA-20260703-2607-01678; semantic-review:SA-20260703-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260703-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-01579; books-review:SF-2026-ARXIV-2607-01617; books-review:SF-2026-ARXIV-2607-01646; books-review:SF-2026-ARXIV-2607-01647; books-review:SF-2026-ARXIV-2607-01678; books-review:SF-2026-ARXIV-2607-01831; books-review:SF-2026-ARXIV-2607-01874; books-review:SF-2026-ARXIV-2607-02032; books-review:SF-2026-ARXIV-2607-02043; books-review:SF-2026-ARXIV-2607-02255; books-review:SF-2026-ARXIV-2607-02440; books-review:SF-2026-ARXIV-2607-02512; books-review:SF-2026-ARXIV-2607-02517; semantic-review:SA-20260703-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260703-COVERAGE:start -->Fresh-context review reconciled the exact window, partition totals, date bucket and denominator.<!-- semantic-review:SA-20260703-COVERAGE:end -->
<!-- semantic-review:SA-20260703-EVIDENCE:start -->Fresh-context review reconciled all 26 frozen families: 10 Deep, 3 Standard and 13 Closure; 0 pending and 0 blocked rows remain explicitly outside mechanism claims.<!-- semantic-review:SA-20260703-EVIDENCE:end -->
<!-- semantic-review:SA-20260703-SELECTION:start -->Fresh-context review reconciled 10 eligible Deep families: 3 selected and 7 not selected; the narrative limit does not downgrade any completed Source Review.<!-- semantic-review:SA-20260703-SELECTION:end -->
<!-- semantic-review:SA-20260703-BOOKS:start -->Fresh-context review checked current owner and adjacent chapter handoffs; 5 个 family 已定位到实际 Books 段落，8 个 family 的 No Change 结论可定位，0 个 Weekly Only disposition 已由逐 family Source Review 确认为不进入 Books。<!-- semantic-review:SA-20260703-BOOKS:end -->

## 8. Ignored Noise

1214 个窗口内 identity 中，1188 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：5 个 `Integrate`，8 个 `No Change — Existing Coverage`，0 个 `Weekly Only — Context`，13 个 `Rejected — Low Durability / Out of Scope`；Deep 10 / Standard 3。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/03/README.md`。
- 本日报长期 delta 已同步至：`books/part-04-training-system/35-checkpoint.md`、`books/part-04-training-system/36-distributed-training.md`、`books/part-05-inference-system/55-pd-disaggregation.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [OmniPilot: An Uncertainty-Aware LLM Inference Advisor for Heterogeneous GPU Clusters](https://arxiv.org/abs/2607.01579v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-27
- [VLAFlow: A Unified Training Framework for Vision-Language-Action Models via Co-training and Future Latent Alignment](https://arxiv.org/abs/2607.01586v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-26
- [Safe and Adaptive Cloud Healing: Verifying LLM-Generated Recovery Plans with a Neural-Symbolic World Model](https://arxiv.org/abs/2607.01595v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-26
- [3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving](https://arxiv.org/abs/2607.01617v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-27
- [DeadPool: Resilient LLM Training with Hot-Swapping via Zero-Overhead Checkpoint](https://arxiv.org/abs/2607.01646v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-27
- [AgenticDataBench: A Comprehensive Benchmark for Data Agents](https://arxiv.org/abs/2607.01647v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-27
- [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-26
- [SCAPE: Accurate and Efficient LLM Training with Extreme Sparse Communication](https://arxiv.org/abs/2607.01678v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-27
- [SimWorlds: A Multi-Agent System for Dynamic 3D Scene Creation](https://arxiv.org/abs/2607.01766v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-26
- [VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon](https://arxiv.org/abs/2607.01804v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-26
- [Lynx: Progressive Speculative Quantization for accelerating KV Transfer in Long-Context Inference](https://arxiv.org/abs/2607.01831v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-27
- [SkillCoach: Self-Evolving Rubrics for Evaluating and Enhancing Agentic Skill-Use](https://arxiv.org/abs/2607.01874v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-27
- [A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory](https://arxiv.org/abs/2607.01935v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-26
- [PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation](https://arxiv.org/abs/2607.01938v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-26
- [PACE: A Proxy for Agentic Capability Evaluation](https://arxiv.org/abs/2607.02032v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-27
- [Towards Load-Aware Prefill Deflection for Disaggregated LLM Serving](https://arxiv.org/abs/2607.02043v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-27
- [PWM-ArtGen: Part World Model for Articulated Object Generation](https://arxiv.org/abs/2607.02045v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-26
- [Guided Action Flow: Q-Guided Inference for Flow-Matching Vision-Language-Action Policies](https://arxiv.org/abs/2607.02092v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-26
- [Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation](https://arxiv.org/abs/2607.02182v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-26
- [AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents](https://arxiv.org/abs/2607.02255v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-27
- [The Moving Eye: Enhancing VLA Spatial Generalization via Hybrid Dynamic Data Collection](https://arxiv.org/abs/2607.02322v1) — first-public（Asia/Shanghai）：2026-07-02；accessed：2026-08-26
- [EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments](https://arxiv.org/abs/2607.02440v1) — first-public（Asia/Shanghai）：2026-07-03；accessed：2026-08-27
- [Program-as-Weights: A Programming Paradigm for Fuzzy Functions](https://arxiv.org/abs/2607.02512v1) — first-public（Asia/Shanghai）：2026-07-03；accessed：2026-08-27
- [WorldDirector: Building Controllable World Simulators with Persistent Dynamic Memory](https://arxiv.org/abs/2607.02517v1) — first-public（Asia/Shanghai）：2026-07-03；accessed：2026-08-27
- [ASK in the Dark: Uncertainty-Gated LLM Assistance under Partial Observability](https://arxiv.org/abs/2607.02686v1) — first-public（Asia/Shanghai）：2026-07-03；accessed：2026-08-26
- [TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training](https://arxiv.org/abs/2607.02840v1) — first-public（Asia/Shanghai）：2026-07-03；accessed：2026-08-26
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
